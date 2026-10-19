"""termwatch command line.

  python -m termwatch versions
  python -m termwatch baseline  --package DIR --out baselines/NAME --sct VERSION_URI --loinc 2.82 --icd10gm 2026 ... [--watch sct,loinc,...] [--group mii|package|host|REGEX]
  python -m termwatch compare   --baseline baselines/NAME --package DIR [--sct VERSION_URI] [--loinc 2.83] [--system KEY=VERSION ...] --out reports/NAME.json
  python -m termwatch report    --compare reports/NAME.json [--md FILE] [--csv FILE]
  python -m termwatch explorer  --baseline baselines/NAME --compare reports/A.json [reports/B.json ...] --out explorer/
  python -m termwatch discover  --package DIR          (which code systems does the package bind, which does the server version)
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from .ontoserver import TerminologyServer
from .systems import REGISTRY, key_of, parse_versions, parse_watch, system_for


def _add_version_args(p, required_hint=""):
    for url, s in REGISTRY.items():
        p.add_argument(f"--{s['key']}", help=f"{s['label']} version{required_hint}")
    p.add_argument("--system", action="append", default=[], metavar="KEY=VERSION",
                   help="version for any code system (registry key or URL); repeatable")


def _versions_from(a) -> dict:
    out = parse_versions(a.system)
    for url, s in REGISTRY.items():
        v = getattr(a, s["key"].replace("-", "_"), None)
        if v:
            out[url] = v
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="termwatch")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("versions", help="list the versions of the watched code systems on the server")
    v.add_argument("--watch", help="comma list of registry keys or URLs (default: sct,loinc,icd10gm,ops,atc,hgnc; 'all' for the whole registry)")
    d = sub.add_parser("discover", help="list the code systems the package binds and the versions the server has for them")
    d.add_argument("--package", required=True)
    b = sub.add_parser("baseline", help="expand all watched ValueSets under baseline versions")
    b.add_argument("--package", required=True); b.add_argument("--out", required=True)
    _add_version_args(b, " (ValueSets of a watched system without a version are skipped)")
    b.add_argument("--watch", help="comma list of watched code systems (keys or URLs); default sct,loinc,icd10gm,ops,atc,hgnc; "
                                   "'auto' = every system the package binds that the server has at least one version of "
                                   "(baseline version = latest on the server unless given explicitly)")
    b.add_argument("--group", default="mii", help="lane grouping: mii (default), package, host, or a regex with one group over the canonical URL")
    b.add_argument("--keep-display", default="loinc,icd10gm,ops,atc,hgnc", help="comma list of systems whose displays are stored (never sct)")
    b.add_argument("--max-total", type=int, default=500000); b.add_argument("--only", default=""); b.add_argument("--workers", type=int, default=4)
    c = sub.add_parser("compare", help="compare baseline against target versions")
    c.add_argument("--baseline", required=True); c.add_argument("--package", required=True); c.add_argument("--out", required=True)
    _add_version_args(c)
    c.add_argument("--max-total", type=int, default=500000); c.add_argument("--only", default=""); c.add_argument("--workers", type=int, default=4)
    r = sub.add_parser("report", help="render a comparison as Markdown and CSV")
    r.add_argument("--compare", required=True); r.add_argument("--md"); r.add_argument("--csv")
    e = sub.add_parser("explorer", help="build the self-contained HTML explorer (subway map of ValueSets x releases)")
    e.add_argument("--baseline", required=True); e.add_argument("--compare", nargs="*", default=[]); e.add_argument("--out", required=True)
    e.add_argument("--expected", action="append", default=[], metavar="KEY=VERSION", help="release expected next but not on the server yet (drawn as a grey column); repeatable")
    a = ap.parse_args(argv)

    if a.cmd == "versions":
        ts = TerminologyServer()
        for s in parse_watch(a.watch):
            print(f"{s}  ({key_of(s)})")
            for v in ts.code_system_versions(s):
                print("  ", v)
        return 0
    if a.cmd == "discover":
        from .discover import discover, format_table
        print(format_table(discover(a.package, TerminologyServer())))
        return 0
    if a.cmd == "baseline":
        from .baseline import run_baseline
        from .systems import SCT
        versions = _versions_from(a)
        if (a.watch or "").strip() == "auto":
            from .discover import auto_watch, discover, format_table, latest_versions
            rows = discover(a.package, TerminologyServer())
            print(format_table(rows), file=sys.stderr)
            watched = auto_watch(rows)
            for s, v in latest_versions(rows).items():
                if s not in versions:
                    versions[s] = v
                    print(f"baseline version for {key_of(s)} not given, using latest on server: {v}", file=sys.stderr)
        else:
            watched = parse_watch(a.watch)
        keep_keys = {k.strip() for k in a.keep_display.split(",") if k.strip()}
        keep = {s: (key_of(s) in keep_keys and s != SCT) for s in watched}
        if not versions:
            print("give at least one code-system version (--sct, --loinc, --icd10gm, ... or --system KEY=VERSION)", file=sys.stderr); return 2
        run_baseline(a.package, a.out, versions, keep, a.max_total, a.only, a.workers, watched, a.group)
        return 0
    if a.cmd == "compare":
        from .compare import run_compare
        targets = _versions_from(a)
        if not targets:
            print("give at least one target version (--sct, --loinc, --icd10gm, ... or --system KEY=VERSION)", file=sys.stderr); return 2
        run_compare(a.baseline, a.package, targets, a.out, a.max_total, a.only, a.workers)
        return 0
    if a.cmd == "report":
        from .report import render_markdown, write_csv
        cmp = json.load(open(a.compare, encoding="utf-8"))
        md = render_markdown(cmp)
        if a.md:
            open(a.md, "w", encoding="utf-8").write(md)
        else:
            sys.stdout.write(md)
        if a.csv:
            write_csv(cmp, a.csv)
        return 0
    if a.cmd == "explorer":
        from pathlib import Path
        from .explorer import build, write_explorer
        expected = {key_of(system_for(k)): v for k, v in (x.split("=", 1) for x in a.expected)}
        data = build(Path(a.baseline), [Path(c) for c in a.compare], expected)
        out = write_explorer(data, Path(a.out))
        print(f"wrote {out} ({len(data['valuesets'])} ValueSets, {len(data['shared'])} shared changes)")
        return 0
    return 1
