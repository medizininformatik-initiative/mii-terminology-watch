"""Compare a baseline against newer code-system versions and classify the impact."""
from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List

from .baseline import expand_members
from .inventory import drop_pinned_of_multi, inline_valueset_refs, load_package, restrict_to_watched, version_modes
from .ontoserver import TerminologyServer
from .systems import DEFAULT_WATCHED, spec

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
    watched = meta.get("watched") or inv.get("watched") or DEFAULT_WATCHED
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
        if base.get("static"):
            results.append({**_head(e), "severity": "NONE", "note": "every include is pinned, nothing to compare"})
            return
        vs = drop_pinned_of_multi(restrict_to_watched(inline_valueset_refs(by_url[e["url"]], by_url), watched), e.get("multi_version", []))
        versions = {s: target_versions.get(s, base_versions.get(s)) for s in e["systems"]}
        versions = {s: v for s, v in versions.items() if v}
        t0 = time.time()
        force, soft = version_modes(e, versions)
        contains, info = ts.expand(vs, force, max_total=max_total, soft_versions=soft)
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
            if spec(inc["system"]).get("anchors"):
                for f in inc.get("filters", []):
                    if f.get("property") in ("concept", "code") and f.get("op") in ("is-a", "descendent-of"):
                        anchors.append((inc["system"], f["value"]))
            if inc["kind"] == "enumerated":
                anchors += [(inc["system"], c) for c in inc["concepts"]]
        whole = {inc["system"] for inc in e["includes"] if inc["kind"] == "whole-system"}

        def _successors(sys_, code):
            return ts.sct_successors(code, versions[sys_]) if spec(sys_).get("successors") == "sct" else []

        def _status(sys_, code):
            """(status_text, inactive, exists, display) for a code under the target version."""
            sp = spec(sys_)
            if sp.get("status") == "lookup":
                lk = ts.lookup(sys_, code, versions[sys_], (sp["status_property"],))
                st = (lk.get("properties", {}).get(sp["status_property"]) or [None])[0]
                return st, (st is not None and st != "ACTIVE"), bool(lk.get("display") or st), lk.get("display") or ""
            v = ts.validate(sys_, code, versions[sys_])
            exists = bool(v.get("result")) or v.get("inactive") is not None
            return ("inactive" if v.get("inactive") else "active" if exists else None), bool(v.get("inactive")), exists, v.get("display") or ""

        def _removed(key):
            sys_, code = key.split("|", 1)
            rec = {"code": code, "system": sys_, "display": old[key].get("display", "")}
            st, inactive, exists, disp = _status(sys_, code)
            rec["display"] = rec["display"] or disp
            rec["inactive"] = inactive
            if not exists:
                rec["reason"] = "not in this code system version"
            elif inactive:
                rec["reason"] = f"status {st}" if spec(sys_).get("status") == "lookup" else "inactivated"
                rec["successors"] = _successors(sys_, code)
            elif sys_ in whole:
                rec["reason"] = f"status {st}, dropped from the whole-system include"
            else:
                rec["reason"] = f"status {st}, no longer matches the filter (property changed)"
            return rec
        detail_removed: List[dict] = _pmap(_removed, removed)

        def _inactivated(key):
            sys_, code = key.split("|", 1)
            rec = {"code": code, "system": sys_, "display": new[key]["display"]}
            if spec(sys_).get("status") == "lookup":
                rec["status"] = _status(sys_, code)[0]
            rec["successors"] = _successors(sys_, code)
            return rec
        detail_inactivated: List[dict] = _pmap(_inactivated, inactivated)

        def _anchor(item):
            sys_, code = item
            st, inactive, exists, disp = _status(sys_, code)
            if not exists or inactive:
                return {"code": code, "system": sys_, "display": disp, "inactive": inactive,
                        "reason": "not in this code system version" if not exists else f"status {st}",
                        "successors": _successors(sys_, code) if inactive else []}
            return None
        anchors_broken = [a for a in _pmap(_anchor, anchors) if a]
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
