"""Discover which code systems a package binds to and which of them the server versions."""
from __future__ import annotations

from collections import Counter
from typing import Dict, List

from .inventory import load_package
from .ontoserver import TerminologyServer
from .systems import key_of, label_of, version_sort_key


def discover(package_dir: str, ts: TerminologyServer) -> List[dict]:
    """One row per code system used in the package's ValueSet includes/excludes."""
    by_url = load_package(package_dir)
    n_vs: Counter = Counter()
    for vs in by_url.values():
        comp = vs.get("compose", {})
        for inc in comp.get("include", []) + comp.get("exclude", []):
            if inc.get("system"):
                n_vs[inc["system"]] += 1
    rows = []
    for system, n in n_vs.most_common():
        try:
            versions = sorted({v for v in ts.code_system_versions(system) if v}, key=version_sort_key)
        except Exception as ex:  # server error for this system: report, do not abort
            versions, err = [], str(ex)[:80]
        else:
            err = None
        rows.append({"system": system, "key": key_of(system), "label": label_of(system), "includes": n,
                     "versions": versions, "latest": versions[-1] if versions else None, "error": err})
    return rows


def auto_watch(rows: List[dict], min_versions: int = 1) -> List[str]:
    return [r["system"] for r in rows if len(r["versions"]) >= min_versions]


def latest_versions(rows: List[dict]) -> Dict[str, str]:
    return {r["system"]: r["latest"] for r in rows if r["latest"]}


def format_table(rows: List[dict]) -> str:
    out = [f"{'key':10} {'includes':>8} {'versions':>8}  {'latest':22} system"]
    for r in rows:
        tag = "" if len(r["versions"]) > 1 else ("  (single version: baseline only)" if r["versions"] else "  (not on server)")
        out.append(f"{r['key'][:10]:10} {r['includes']:>8} {len(r['versions']):>8}  {str(r['latest'] or '-')[:22]:22} {r['system']}{tag}")
    return "\n".join(out)
