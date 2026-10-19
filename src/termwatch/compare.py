"""Compare a baseline against newer code-system versions and classify the impact."""
from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List

from .baseline import expand_members
from .inventory import inline_valueset_refs, load_package, restrict_to_watched
from .ontoserver import LOINC, SCT, TerminologyServer

SEVERITY_ORDER = ["BREAKING", "SIGNIFICANT", "MINOR", "NONE"]


def _severity(vs_entry: dict, removed: list, inactivated: list, added: list, relabelled: list, anchors_broken: list) -> str:
    enumerated = any(i["kind"] == "enumerated" for i in vs_entry["includes"])
    if anchors_broken or (removed and enumerated) or inactivated:
        return "BREAKING"
    if removed or relabelled:
        return "SIGNIFICANT"
    if added:
        return "MINOR"
    return "NONE"


def run_compare(baseline_dir: str, package_dir: str, target_versions: Dict[str, str], out_path: str,
                max_total: int = 500000, only: str = "", workers: int = 4) -> dict:
    ts = TerminologyServer()
    meta = json.load(open(os.path.join(baseline_dir, "baseline.json"), encoding="utf-8"))
    inv = json.load(open(os.path.join(baseline_dir, "inventory.json"), encoding="utf-8"))
    by_url = load_package(package_dir)
    base_versions = meta["versions"]
    changed_systems = {s for s, v in target_versions.items() if base_versions.get(s) != v}
    results: List[dict] = []
    n = len(inv["valuesets"])
    def work(item):
        i, e = item
        if only and only not in e["id"]:
            return
        try:
            _work(i, e)
        except Exception as ex:  # one ValueSet must never lose the whole run
            results.append({**_head(e), "severity": "NONE", "note": f"compare failed: {type(ex).__name__}: {str(ex)[:160]}"})
            print(f"[{i}/{n}] {e['id']}: COMPARE ERROR {type(ex).__name__}: {str(ex)[:120]}", file=sys.stderr, flush=True)

    def _work(i, e):
        if not (set(e["systems"]) & changed_systems):
            return
        bpath = os.path.join(baseline_dir, "expansions", f"{e['id']}.json")
        if not os.path.exists(bpath):
            return
        base = json.load(open(bpath, encoding="utf-8"))
        if base.get("error"):
            results.append({**_head(e), "severity": "NONE", "note": f"baseline error: {base['error'][:120]}"})
            return
        if e["url"] not in by_url:
            results.append({**_head(e), "severity": "NONE", "note": "ValueSet not found in package directory"})
            return
        vs = restrict_to_watched(inline_valueset_refs(by_url[e["url"]], by_url))
        versions = {s: target_versions.get(s, base_versions.get(s)) for s in e["systems"]}
        t0 = time.time()
        contains, info = ts.expand(vs, versions, max_total=max_total)
        if info.get("error"):
            results.append({**_head(e), "severity": "BREAKING", "note": f"expansion failed under target: {info['error'][:200]}"})
            print(f"[{i}/{n}] {e['id']}: EXPANSION ERROR", file=sys.stderr, flush=True)
            return
        old = expand_members(base["members"])
        new = {k: {"inactive": c["inactive"], "display": c["display"]} for k, c in contains.items()}
        removed = sorted(set(old) - set(new))
        added = sorted(set(new) - set(old))
        inactivated = sorted(k for k in set(old) & set(new) if new[k]["inactive"] and not old[k]["inactive"])
        reactivated = sorted(k for k in set(old) & set(new) if old[k]["inactive"] and not new[k]["inactive"])
        relabelled = sorted(k for k in set(old) & set(new) if "display" in old[k] and old[k]["display"] != new[k]["display"])
        # enumerated-include anchors and filter anchors: check that they still resolve as active
        anchors_broken: List[dict] = []
        anchors = []
        for inc in e["includes"]:
            if inc["system"] not in changed_systems:
                continue
            for f in inc.get("filters", []):
                if inc["system"] == SCT and f.get("property") in ("concept", "code") and f.get("op") in ("is-a", "descendent-of"):
                    anchors.append((SCT, f["value"]))
            if inc["kind"] == "enumerated":
                anchors += [(inc["system"], c) for c in inc["concepts"]]
        def _removed(key):
            sys_, code = key.split("|", 1)
            rec = {"code": code, "system": sys_, "display": old[key].get("display", "")}
            if sys_ == SCT:
                v = ts.validate(SCT, code, versions[SCT])
                rec["inactive"] = v.get("inactive")
                rec["display"] = rec["display"] or (v.get("display") or "")
                rec["reason"] = "inactivated" if v.get("inactive") else ("unknown-code" if not v.get("result") else "no longer in filter (moved)")
                if v.get("inactive"):
                    rec["successors"] = ts.sct_successors(code, versions[SCT])
            else:
                lk = ts.lookup(LOINC, code, versions[LOINC], ("STATUS",))
                rec["display"] = rec["display"] or (lk.get("display") or "")
                st = (lk["properties"].get("STATUS") or [None])[0]
                rec["reason"] = (f"status {st}, no longer matches the filter (property changed)" if st == "ACTIVE"
                                 else f"status {st}" if st else "unknown code")
            return rec
        detail_removed: List[dict] = _pmap(_removed, removed)

        def _inactivated(key):
            sys_, code = key.split("|", 1)
            rec = {"code": code, "system": sys_, "display": new[key]["display"]}
            if sys_ == LOINC:
                lk = ts.lookup(LOINC, code, versions[LOINC], ("STATUS",))
                rec["status"] = (lk["properties"].get("STATUS") or [None])[0]
            else:
                rec["successors"] = ts.sct_successors(code, versions[SCT])
            return rec
        detail_inactivated: List[dict] = _pmap(_inactivated, inactivated)
        for sys_, code in anchors:
            if sys_ == SCT:
                v = ts.validate(SCT, code, versions[SCT])
                if not v.get("result") or v.get("inactive"):
                    anchors_broken.append({"code": code, "display": v.get("display") or "", "inactive": v.get("inactive"),
                                           "successors": ts.sct_successors(code, versions[SCT]) if v.get("inactive") else []})
        sev = _severity(e, removed, inactivated, added, relabelled, anchors_broken)
        results.append({**_head(e), "versions_baseline": {s: base_versions.get(s) for s in e["systems"]}, "versions_target": versions,
                        "count_baseline": len(old), "count_target": len(new), "severity": sev,
                        "added": [{"code": k.split("|", 1)[1], "system": k.split("|", 1)[0], "display": new[k]["display"]} for k in added],
                        "removed": detail_removed, "inactivated": detail_inactivated, "reactivated": reactivated,
                        "relabelled": [{"code": k.split("|", 1)[1], "old": old[k].get("display"), "new": new[k]["display"]} for k in relabelled],
                        "anchors_broken": anchors_broken, "truncated": info.get("truncated")})
        print(f"[{i}/{n}] {e['id']}: {sev} +{len(added)} -{len(removed)} inact {len(inactivated)} relabel {len(relabelled)} ({time.time()-t0:.1f}s)", file=sys.stderr, flush=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(work, enumerate(inv["valuesets"], 1)))
    out = {"package": inv["package"], "baseline_versions": base_versions, "target_versions": target_versions,
           "server": ts.base, "created": time.strftime("%Y-%m-%dT%H:%M:%S"), "calls": ts.calls,
           "results": sorted(results, key=lambda r: (SEVERITY_ORDER.index(r["severity"]), r["module"], r["id"]))}
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    json.dump(out, open(out_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return out


def _pmap(fn, items, workers: int = 8) -> list:
    """Run per-code server lookups concurrently, preserving order."""
    items = list(items)
    if len(items) < 2:
        return [fn(x) for x in items]
    with ThreadPoolExecutor(max_workers=min(workers, len(items))) as pool:
        return list(pool.map(fn, items))


def _head(e: dict) -> dict:
    return {"id": e["id"], "url": e["url"], "title": e["title"], "module": e["module"], "pinned": e["pinned"],
            "kinds": sorted({i["kind"] for i in e["includes"]}), "systems": e["systems"]}
