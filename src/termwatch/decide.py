"""Decision tooling for inactivated codes: rank successor candidates, keep human decisions, emit ConceptMaps.

Input is a compare JSON (successors come from the SNOMED historical association refsets, i.e. the
same data Snowstorm/Ontoserver expose as implicit ConceptMaps). Output per run:

  decisions.json          one item per (ValueSet, code) with ranked candidates, status and the decision
  summary.md              agenda for a terminology council: counts per ValueSet, open items with shortlists
  ConceptMap-<vs>.json    FHIR R4 draft map old version -> new version per ValueSet
  review.html             self-contained page to pick candidates and export decisions.json

Statuses: auto (single SAME AS / REPLACED BY successor), proposed (several candidates, exactly one
survives the signals), open (several candidates), none (no successor), out-of-filter (code still
active, only dropped out of the filter), decided (a human decision is recorded).
Re-running keeps every recorded decision (merge key ValueSet + code).
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Dict, List, Optional

from .baseline import expand_members
from .systems import SCT, short_version

EQUIVALENCE = {"SAME AS": "equal", "REPLACED BY": "equivalent", "WAS A": "wider", "ALTERNATIVE": "relatedto",
               "POSSIBLY EQUIVALENT TO": "inexact", "PARTIALLY EQUIVALENT TO": "inexact", "POSSIBLY REPLACED BY": "inexact", "MOVED TO": "unmatched"}
AUTO_ASSOCIATIONS = ("SAME AS", "REPLACED BY")
ROOT = "138875005"
STOP = {"of", "the", "and", "or", "to", "in", "by", "with", "due", "a", "an", "and/or"}


def _tokens(s: str) -> set:
    return {t for t in re.findall(r"[a-z0-9]+", (s or "").lower()) if t not in STOP}


class _Hierarchy:
    """Top-level hierarchy of a concept from an RF2 release (optional signal)."""

    def __init__(self, release) -> None:
        self.r = release
        self.top = set(release.children.get(ROOT, []))

    def of(self, code: str) -> set:
        return self.r.ancestors(code, include_self=True) & self.top


def build(compare: dict, baseline_dir: Path, releases: Optional[dict] = None, previous: Optional[dict] = None) -> dict:
    releases = releases or {}
    old_h = next((_Hierarchy(r) for v, r in releases.items() if v == compare["baseline_versions"].get(SCT)), None)
    new_h = next((_Hierarchy(r) for v, r in releases.items() if v == compare["target_versions"].get(SCT)), None)
    new_r = new_h.r if new_h else None
    prev = {(d["valueset"], d["code"]): d for d in (previous or {}).get("items", [])}
    prev_by_code = {d["code"]: d for d in (previous or {}).get("items", []) if d.get("decision")}  # a decision is per code, applies to every ValueSet
    items: List[dict] = []
    for r in compare["results"]:
        if not (r.get("removed") or r.get("inactivated")):
            continue
        bpath = baseline_dir / "expansions" / f"{r['id']}.json"
        old = expand_members(json.load(open(bpath, encoding="utf-8"))["members"]) if bpath.exists() else {}
        removed = {x["code"] for x in r.get("removed", [])}
        added = {x["code"] for x in r.get("added", [])}

        def in_new_vs(code: str) -> bool:
            return code in added or (f"{SCT}|{code}" in old and code not in removed)

        for x in r.get("removed", []) + r.get("inactivated", []):
            if x.get("system", SCT) != SCT:
                continue
            still_active = x in r.get("removed", []) and not x.get("inactive") and "not in this code system version" not in x.get("reason", "")
            old_top = old_h.of(x["code"]) if old_h else set()
            old_tok = _tokens(x.get("display", ""))
            cands = []
            for s in x.get("successors", []):
                sig = {"in_valueset": in_new_vs(s["code"]), "association": s["association"]}
                if new_h:
                    sig["active"] = s["code"] in new_r.active
                    sig["same_hierarchy"] = bool(old_top & new_h.of(s["code"])) if old_top else None
                tok = _tokens(s.get("display", ""))
                sig["term_overlap"] = round(len(old_tok & tok) / len(old_tok | tok), 2) if old_tok and tok else 0.0
                score = (3 if sig["in_valueset"] else 0) + (1 if sig.get("same_hierarchy") else 0) + sig["term_overlap"] \
                    + (1 if s["association"] in AUTO_ASSOCIATIONS else 0) - (5 if sig.get("active") is False else 0)
                cands.append({"code": s["code"], "display": s.get("display", ""), "association": s["association"],
                              "equivalence": EQUIVALENCE.get(s["association"], "relatedto"), "score": round(score, 2), "signals": sig})
            cands.sort(key=lambda c: -c["score"])
            if still_active:
                status, proposal = "out-of-filter", None
            elif not cands:
                status, proposal = "none", None
            elif len(cands) == 1 and cands[0]["association"] in AUTO_ASSOCIATIONS and cands[0]["signals"].get("active", True):
                status, proposal = "auto", cands[0]["code"]
            else:
                survivors = [c for c in cands if c["signals"]["in_valueset"] and c["signals"].get("active", True)]
                if len(survivors) == 1:
                    status, proposal = "proposed", survivors[0]["code"]
                else:
                    status, proposal = "open", (cands[0]["code"] if cands and cands[0]["score"] - (cands[1]["score"] if len(cands) > 1 else -9) >= 2 else None)
            item = {"valueset": r["id"], "module": r["module"], "pinned": r["pinned"], "kinds": r.get("kinds", []),
                    "code": x["code"], "display": x.get("display", ""), "reason": x.get("reason") or x.get("status") or "",
                    "candidates": cands, "status": status, "proposal": proposal, "decision": None}
            p = prev.get((r["id"], x["code"])) or prev_by_code.get(x["code"])
            if p and p.get("decision"):
                item["decision"] = p["decision"]
                item["status"] = "decided"
            items.append(item)
    items.sort(key=lambda i: (i["module"], i["valueset"], i["code"]))
    pkg = compare["package"]
    pkg = f"{pkg.get('name')} {pkg.get('version')}" if isinstance(pkg, dict) else str(pkg)
    return {"package": pkg, "system": SCT, "from": compare["baseline_versions"].get(SCT), "to": compare["target_versions"].get(SCT),
            "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "items": items}


def concept_maps(dec: dict) -> Dict[str, dict]:
    """One R4 ConceptMap per ValueSet: decided + auto + proposed entries, open ones as unmatched with the candidates in a comment."""
    by_vs: Dict[str, List[dict]] = {}
    for it in dec["items"]:
        if it["status"] != "out-of-filter":
            by_vs.setdefault(it["valueset"], []).append(it)
    out = {}
    frm, to = short_version(SCT, dec["from"]), short_version(SCT, dec["to"])
    for vs, its in by_vs.items():
        elements = []
        for it in its:
            chosen = (it["decision"] or {}).get("target") or it["proposal"] if it["status"] in ("decided", "auto", "proposed") else None
            cand = {c["code"]: c for c in it["candidates"]}
            if chosen and chosen in cand:
                eq = (it["decision"] or {}).get("equivalence") or cand[chosen]["equivalence"]
                target = [{"code": chosen, "display": cand[chosen]["display"], "equivalence": eq,
                           "comment": f"{it['status']}: {cand[chosen]['association']}; {it['reason']}" + (f"; {it['decision'].get('note')}" if it.get("decision", {}) and it["decision"].get("note") else "")}]
            elif chosen:
                target = [{"code": chosen, "equivalence": (it["decision"] or {}).get("equivalence", "relatedto"), "comment": f"decided outside the candidate list; {it['reason']}"}]
            else:
                target = [{"equivalence": "unmatched", "comment": f"{it['status']}: {it['reason']}; candidates: " +
                           (", ".join(f"{c['code']} ({c['association']})" for c in it["candidates"]) or "none")}]
            elements.append({"code": it["code"], "display": it["display"], "target": target})
        decided = sum(1 for it in its if it["status"] in ("decided", "auto", "proposed"))
        out[vs] = {"resourceType": "ConceptMap", "id": f"{vs}-sct-{frm}-{to}", "status": "draft",
                   "name": f"{vs}_sct_{frm}_{to}", "title": f"Überleitung {vs}: SNOMED CT {frm} → {to}",
                   "date": dec["generated"][:10], "publisher": "MII Terminology Watch (draft)",
                   "description": f"Successors for members of {vs} inactivated between SNOMED CT International {frm} and {to}. "
                                  f"{decided} of {len(its)} elements resolved (auto / proposed / decided), the rest unmatched pending a decision.",
                   "sourceUri": f"{SCT}|{dec['from']}", "targetUri": f"{SCT}|{dec['to']}",
                   "group": [{"source": SCT, "sourceVersion": dec["from"], "target": SCT, "targetVersion": dec["to"], "element": elements}]}
    return out


def summary_md(dec: dict) -> str:
    frm, to = short_version(SCT, dec["from"]), short_version(SCT, dec["to"])
    L = [f"# Decisions: SNOMED CT {frm} → {to} ({dec['package']})", "",
         "Status: auto = single SAME AS / REPLACED BY successor; proposed = one candidate survives the signals "
         "(member of the re-expanded ValueSet, active, same hierarchy); open = several candidates; none = no successor; "
         "out-of-filter = code still active, only dropped out of the filter (data stays valid).", ""]
    stat = ["auto", "proposed", "open", "none", "out-of-filter", "decided"]
    rows: Dict[str, Dict[str, int]] = {}
    for it in dec["items"]:
        rows.setdefault(f"{it['module']} / `{it['valueset']}`", {s: 0 for s in stat})[it["status"]] += 1
    tot = {s: sum(r[s] for r in rows.values()) for s in stat}
    L.append("| ValueSet | " + " | ".join(stat) + " |"); L.append("|---|" + "---:|" * len(stat))
    for k, r in rows.items():
        L.append(f"| {k} | " + " | ".join(str(r[s]) for s in stat) + " |")
    L.append("| **total** | " + " | ".join(f"**{tot[s]}**" for s in stat) + " |")
    uniq = {s: len({i["code"] for i in dec["items"] if i["status"] == s}) for s in stat}
    L.append("| **distinct codes** | " + " | ".join(f"**{uniq[s]}**" for s in stat) + " |")
    L += ["", f"A decision is taken once per code and applies to every ValueSet it sits in: {uniq['open']} open + {uniq['none']} without successor "
              f"need a human, {uniq['proposed']} proposals to confirm, {uniq['auto']} resolved automatically.", ""]
    seen = set()
    for st, title in (("open", "Open: several candidates"), ("proposed", "Proposed: confirm"), ("none", "No successor")):
        its = [i for i in dec["items"] if i["status"] == st and (i["code"] not in seen or st == "none")]
        if not its:
            continue
        L += [f"## {title} ({len(its)})", ""]
        for it in its:
            seen.add(it["code"])
            vss = sorted({j["valueset"] for j in dec["items"] if j["code"] == it["code"]})
            L.append(f"- `{it['code']}` {it['display']} — {it['reason']} — in {', '.join(f'`{v}`' for v in vss)}")
            for c in it["candidates"][:6]:
                sig = c["signals"]
                flags = [c["association"], "in VS" if sig["in_valueset"] else "not in VS"]
                if sig.get("same_hierarchy") is not None:
                    flags.append("same hierarchy" if sig["same_hierarchy"] else "other hierarchy")
                if sig.get("active") is False:
                    flags.append("INACTIVE")
                mark = " ← proposal" if c["code"] == it["proposal"] else ""
                L.append(f"    - `{c['code']}` {c['display']} ({'; '.join(flags)}; score {c['score']}){mark}")
        L.append("")
    return "\n".join(L)


def write_all(dec: dict, out_dir: Path, template: Optional[Path] = None) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json.dump(dec, open(out_dir / "decisions.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    (out_dir / "summary.md").write_text(summary_md(dec), encoding="utf-8")
    for vs, cm in concept_maps(dec).items():
        json.dump(cm, open(out_dir / f"ConceptMap-{vs}.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    template = template or Path(__file__).with_name("decide_template.html")
    html = template.read_text(encoding="utf-8").replace("/*__DATA__*/null", json.dumps(dec, ensure_ascii=False))
    (out_dir / "review.html").write_text(html, encoding="utf-8")
