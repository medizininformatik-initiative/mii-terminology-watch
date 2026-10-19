"""Build the human-facing "Terminologie-Fahrplan" explorer.

Input: a baseline directory (inventory + expansions) and one or more compare
JSON files (any direction, any system).  Output: one self-contained HTML file
(data embedded) plus data.json, in the style of the MII Kerndatensatz
version-history explorer: x = terminology releases, one lane per ValueSet,
segment colour = what happened to the ValueSet's content between releases.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional

from .systems import key_of, label_of, short_version, spec, version_sort_key

ITEM_CAP = 120  # per change list and ValueSet; the full lists stay in the compare JSON


def _category(tx: dict) -> str:
    """Worst thing that happened, in subway colours."""
    if tx["anch"] or tx["inact"]:
        return "inactivated"
    if tx["rem"]:
        return "removed"
    if tx["rel"]:
        return "relabelled"
    if tx["add"] or tx["react"]:
        return "added"
    return "identical"


def _advice(vs: dict, tx: dict) -> List[str]:
    out = []
    kinds = set(vs.get("kinds", []))
    if tx["anch"]:
        out.append("Filter-Anker (is-a / descendant-of) ist inaktiv: ECL bzw. Filter neu definieren, sonst wird der ValueSet leer.")
    if tx["inact"]:
        if "enumerated" in kinds:
            out.append("Inaktivierte Codes aus der Aufzählung entfernen oder durch den Nachfolger ersetzen (Spalte „Nachfolger“).")
        else:
            out.append("Inaktivierte Codes bleiben in Bestandsdaten gültig, dürfen aber nicht mehr neu kodiert werden: Kodier-Hinweise und Mapping-Tabellen anpassen.")
        if vs.get("pinned"):
            out.append("ValueSet ist gepinnt: Änderung wird erst beim Versionswechsel im Package wirksam. Vor dem Pin-Wechsel prüfen.")
        else:
            out.append("ValueSet ist nicht gepinnt: Änderung wird mit dem nächsten Terminologie-Load auf dem Server sofort wirksam.")
    if tx["rem"]:
        out.append("Aktive Codes sind aus dem Filter gefallen (Eigenschaft geändert): Filter-Definition prüfen, ob die Codes weiterhin gewollt sind.")
    if tx["rel"]:
        out.append("Anzeigetexte haben sich geändert: Schulungsunterlagen, Dokumentation und Display-Tabellen aktualisieren.")
    if tx["add"] and not (tx["inact"] or tx["rem"] or tx["anch"] or tx["rel"]):
        out.append("Nur neue Codes: keine Korrektur nötig, Kodierende über die neuen Möglichkeiten informieren.")
    return out


def _items(lst: List[dict], keys: List[str]) -> List[dict]:
    return [{k: x.get(k) for k in keys if x.get(k) not in (None, "", [])} for x in lst[:ITEM_CAP]]


def load_compares(paths: List[Path]) -> List[dict]:
    return [json.loads(p.read_text()) for p in paths]


def build(baseline_dir: Path, compare_paths: List[Path], expected: Optional[Dict[str, str]] = None) -> dict:
    inv = json.loads((baseline_dir / "inventory.json").read_text())
    base = json.loads((baseline_dir / "baseline.json").read_text())
    compares = load_compares(compare_paths)
    url_of: Dict[str, str] = {}  # key -> system url

    # releases per system: baseline + every target seen
    releases: Dict[str, Dict[str, dict]] = {}
    for sys_url, v in base["versions"].items():
        k = key_of(sys_url); url_of[k] = sys_url
        releases.setdefault(k, {})[short_version(sys_url, v)] = {"v": short_version(sys_url, v), "uri": v, "baseline": True}
    for c in compares:
        for sys_url, v in c["target_versions"].items():
            k = key_of(sys_url); url_of[k] = sys_url
            releases.setdefault(k, {}).setdefault(short_version(sys_url, v), {"v": short_version(sys_url, v), "uri": v, "baseline": False})

    vsets: Dict[str, dict] = {}
    for v in inv["valuesets"]:
        systems = [key_of(s) for s in v["systems"] if s in base["versions"]]
        if not systems:
            continue
        exp_path = baseline_dir / "expansions" / f"{v['id']}.json"
        n_base, n_inactive, err, static = None, 0, None, False
        if exp_path.exists():
            e = json.loads(exp_path.read_text())
            err = e.get("error")
            static = bool(e.get("static"))
            if not err and not static:
                n_base = e.get("total")
                n_inactive = sum(len(m.get("inactive", [])) for m in e.get("members", {}).values())
        kinds = sorted({i["kind"] for i in v["includes"]})
        vsets[v["id"]] = {
            "id": v["id"], "url": v["url"], "title": v.get("title") or v["id"], "module": v["module"],
            "systems": systems, "pinned": v["pinned"], "kinds": kinds, "status": v.get("status"),
            "multi_version": [key_of(s) for s in v.get("multi_version", [])],
            "error": err, "static": static,
            "n_includes": len(v["includes"]),
            "n_enumerated": sum(len(i.get("concepts", [])) for i in v["includes"]),
            "states": {}, "transitions": {},
        }
        for sk in systems:
            bv = short_version(url_of[sk], base["versions"].get(url_of[sk], ""))
            vsets[v["id"]]["states"][f"{sk}|{bv}"] = {"n": n_base, "inactive": n_inactive}

    shared: Dict[str, dict] = {}
    for c in compares:
        for r in c["results"]:
            vs = vsets.get(r["id"])
            if not vs or "versions_target" not in r:  # skipped / static / failed entries carry only a note
                continue
            for sys_url, tv in r["versions_target"].items():
                bv_full = r["versions_baseline"].get(sys_url)
                if bv_full == tv:
                    continue
                sk = key_of(sys_url)
                a, b = short_version(sys_url, bv_full), short_version(sys_url, tv)
                forward = version_sort_key(a) < version_sort_key(b)
                frm, to = (a, b) if forward else (b, a)
                added, removed = r["added"], r["removed"]
                inact = r["inactivated"]
                react = [x if isinstance(x, dict) else {"code": x.split("|", 1)[-1]} for x in r["reactivated"]]
                rel = [{"code": x["code"], "display_old": x.get("old", x.get("display_old")), "display_new": x.get("new", x.get("display_new"))} for x in r["relabelled"]]
                if not forward:  # compare ran against an older release: invert the direction
                    added, removed = removed, added
                    inact, react = react, inact
                    rel = [{**x, "display_old": x.get("display_new"), "display_new": x.get("display_old")} for x in rel]
                anchors = r["anchors_broken"] if forward else []  # backwards: "not in older version" = addition, already in added
                enumerated = "enumerated" in vs.get("kinds", [])
                tx = {
                    "from": frm, "to": to, "system": sk,
                    "add": len(added), "rem": len(removed), "inact": len(inact), "react": len(react),
                    "rel": len(rel), "anch": len(anchors),
                    "n_from": r["count_baseline"] if forward else r["count_target"],
                    "n_to": r["count_target"] if forward else r["count_baseline"],
                    "severity": ("BREAKING" if anchors or inact or (removed and enumerated) else "SIGNIFICANT" if removed or rel
                                 else "MINOR" if added or react else "NONE"),
                    "truncated": r.get("truncated", False),
                    "items": {
                        "inactivated": _items(inact, ["code", "display", "status", "reason", "successors"]),
                        "anchors": _items(anchors, ["code", "display", "status", "reason", "successors", "kind"]),
                        "removed": _items(removed, ["code", "display", "reason", "successors", "status"]),
                        "relabelled": _items(rel, ["code", "display_old", "display_new"]),
                        "added": _items(added, ["code", "display"]),
                        "reactivated": _items(react, ["code", "display"]),
                    },
                }
                tx["cat"] = _category(tx)
                tx["advice"] = _advice(vs, tx)
                key = f"{sk}|{frm}|{to}"
                vs["transitions"][key] = tx
                vs["states"][f"{sk}|{to}"] = {"n": tx["n_to"], "inactive": None}
                vs["states"].setdefault(f"{sk}|{frm}", {"n": tx["n_from"], "inactive": None})
                for kind, lst in (("inactivated", inact), ("anchor", anchors), ("removed", removed)):
                    for x in lst:
                        sid = f"{key}|{x['code']}"
                        s = shared.setdefault(sid, {"system": sk, "from": frm, "to": to, "code": x["code"],
                                                    "display": x.get("display"), "kind": kind, "valuesets": []})
                        if r["id"] not in s["valuesets"]:
                            s["valuesets"].append(r["id"])

    modules = defaultdict(lambda: {"n_vs": 0, "pinned": 0, "systems": defaultdict(int)})
    for v in vsets.values():
        m = modules[v["module"]]
        m["n_vs"] += 1
        m["pinned"] += 1 if v["pinned"] else 0
        for s in v["systems"]:
            m["systems"][s] += 1

    order = [key_of(s) for s in base["versions"]]
    for k in releases:
        releases[k] = sorted(releases[k].values(), key=lambda r: version_sort_key(r["v"]))

    return {
        "generated": base["created"],
        "package": base["package"],
        "server": base.get("server"),
        "group_label": {"mii": "Modul", "package": "Package", "host": "Host"}.get(base.get("group", "mii"), "Gruppe"),
        "expected": expected or {},
        "systems": {k: {"label": label_of(url_of[k]), "url": url_of[k], "yearly": bool(spec(url_of[k]).get("yearly")),
                        "releases": releases[k]} for k in order if k in releases},
        "modules": [{"short": k, "n_vs": v["n_vs"], "pinned": v["pinned"], "systems": dict(v["systems"])} for k, v in sorted(modules.items())],
        "valuesets": sorted(vsets.values(), key=lambda v: (v["module"], v["id"])),
        "shared": [s for s in shared.values() if len(s["valuesets"]) > 1],
        "compares": [{"created": c["created"], "target_versions": c["target_versions"], "calls": c.get("calls")} for c in compares],
    }


def write_explorer(data: dict, out_dir: Path, template: Path | None = None) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "data.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    tpl = (template or Path(__file__).with_name("explorer_template.html")).read_text()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = tpl.replace("/*__DATA__*/null", payload)
    out = out_dir / "index.html"
    out.write_text(html)
    return out
