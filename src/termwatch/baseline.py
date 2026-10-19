"""Create a baseline: expand every watched ValueSet under the baseline code-system versions."""
from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

from .inventory import build_inventory, drop_pinned_of_multi, inline_valueset_refs, load_package, restrict_to_watched, version_modes
from .ontoserver import TerminologyServer


DISPLAY_LIMIT = 50000  # above this many members, displays are not stored (whole-system ValueSets)


def write_json(path: str, obj: dict) -> None:
    """Indented header keys, compact one-line 'members' block (keeps big expansions small and diffs readable)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    head = {k: v for k, v in obj.items() if k != "members"}
    with open(path, "w", encoding="utf-8") as f:
        if "members" not in obj:
            json.dump(obj, f, indent=1, ensure_ascii=False, sort_keys=True)
            f.write("\n")
            return
        f.write("{\n")
        for k in sorted(head):
            f.write(f" {json.dumps(k)}: {json.dumps(head[k], ensure_ascii=False)},\n")
        f.write(' "members": ' + json.dumps(obj["members"], ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n}\n")


def compact_members(contains: Dict[str, dict], keep_display: Dict[str, bool]) -> dict:
    """Store members per system as sorted code lists: {system: {codes: [...], inactive: [...], display: {code: text}?}}"""
    out: Dict[str, dict] = {}
    for c in contains.values():
        m = out.setdefault(c["system"], {"codes": [], "inactive": []})
        m["codes"].append(c["code"])
        if c["inactive"]:
            m["inactive"].append(c["code"])
        if keep_display.get(c["system"], False):
            m.setdefault("display", {})[c["code"]] = c["display"]
    for m in out.values():
        m["codes"].sort(); m["inactive"].sort()
    return out


def expand_members(members: dict) -> Dict[str, dict]:
    """Inverse of compact_members: key 'system|code' -> {inactive, display?}"""
    out: Dict[str, dict] = {}
    for system, m in members.items():
        inactive = set(m.get("inactive", []))
        disp = m.get("display", {})
        for code in m["codes"]:
            rec = {"inactive": code in inactive}
            if code in disp:
                rec["display"] = disp[code]
            out[f"{system}|{code}"] = rec
    return out


def run_baseline(package_dir: str, out_dir: str, versions: Dict[str, str], keep_display: Dict[str, bool],
                 max_total: int = 500000, only: str = "", workers: int = 4,
                 watched: Optional[List[str]] = None, group: str = "mii") -> None:
    ts = TerminologyServer()
    inv = build_inventory(package_dir, watched, group)
    by_url = load_package(package_dir)
    write_json(os.path.join(out_dir, "inventory.json"), inv)
    meta = {"package": inv["package"], "versions": versions, "watched": inv["watched"], "group": group,
            "server": ts.base, "created": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "max_total": max_total, "display_kept_for": [s for s, k in keep_display.items() if k]}
    write_json(os.path.join(out_dir, "baseline.json"), meta)
    n = len(inv["valuesets"])
    done = [0]

    def work(item):
        i, e = item
        if only and only not in e["id"]:
            return
        target = os.path.join(out_dir, "expansions", f"{e['id']}.json")
        if os.path.exists(target):
            try:
                if not json.load(open(target, encoding="utf-8")).get("error"):
                    return
            except Exception:
                pass
        missing = [s for s in e["systems"] if s not in versions]
        if missing:
            print(f"[{i}/{n}] {e['id']}: skipped, no baseline version for {', '.join(missing)}", file=sys.stderr, flush=True)
            return
        vs = drop_pinned_of_multi(restrict_to_watched(inline_valueset_refs(by_url[e["url"]], by_url), inv["watched"]), e.get("multi_version", []))
        if not vs["compose"].get("include"):
            write_json(target, {"id": e["id"], "url": e["url"], "versions": {}, "total": 0, "truncated": False, "error": None,
                                "static": True, "members": {}})
            print(f"[{i}/{n}] {e['id']}: every include is pinned, nothing to watch", file=sys.stderr, flush=True)
            return
        t0 = time.time()
        force, soft = version_modes(e, versions)
        contains, info = ts.expand(vs, force, max_total=max_total, soft_versions=soft)
        big = (info.get("total") or 0) > DISPLAY_LIMIT
        write_json(target, {"id": e["id"], "url": e["url"], "versions": {s: versions[s] for s in e["systems"] if s in versions},
                            "soft_versions": sorted(soft),
                            "total": info.get("total"), "truncated": info.get("truncated"), "error": info.get("error"),
                            "display_dropped": big,
                            "members": compact_members(contains, {} if big else keep_display)})
        print(f"[{i}/{n}] {e['id']}: total={info.get('total')} {'TRUNCATED ' if info.get('truncated') else ''}{'ERROR ' + str(info.get('error'))[:80] if info.get('error') else ''}({time.time()-t0:.1f}s)", file=sys.stderr, flush=True)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(work, enumerate(inv["valuesets"], 1)))
