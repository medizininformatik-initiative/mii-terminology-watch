"""termwatch command line.

  python -m termwatch versions
  python -m termwatch baseline  --package DIR --out baselines/NAME --sct VERSION_URI --loinc 2.82 [--keep-display loinc]
  python -m termwatch compare   --baseline baselines/NAME --package DIR [--sct VERSION_URI] [--loinc 2.83] --out reports/NAME.json
  python -m termwatch report    --compare reports/NAME.json [--md FILE] [--csv FILE]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from .ontoserver import LOINC, SCT, TerminologyServer


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="termwatch")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("versions", help="list SNOMED CT and LOINC versions on the server")
    b = sub.add_parser("baseline", help="expand all watched ValueSets under baseline versions")
    b.add_argument("--package", required=True); b.add_argument("--out", required=True)
    b.add_argument("--sct", required=True, help="SNOMED version URI, e.g. http://snomed.info/sct/900000000000207008/version/20260701")
    b.add_argument("--loinc", required=True, help="LOINC version, e.g. 2.82")
    b.add_argument("--keep-display", default="loinc", help="comma list of systems whose displays are stored (sct,loinc)")
    b.add_argument("--max-total", type=int, default=500000); b.add_argument("--only", default=""); b.add_argument("--workers", type=int, default=4)
    c = sub.add_parser("compare", help="compare baseline against target versions")
    c.add_argument("--baseline", required=True); c.add_argument("--package", required=True); c.add_argument("--out", required=True)
    c.add_argument("--sct"); c.add_argument("--loinc"); c.add_argument("--max-total", type=int, default=500000); c.add_argument("--only", default=""); c.add_argument("--workers", type=int, default=4)
    r = sub.add_parser("report", help="render a comparison as Markdown and CSV")
    r.add_argument("--compare", required=True); r.add_argument("--md"); r.add_argument("--csv")
    a = ap.parse_args(argv)

    if a.cmd == "versions":
        ts = TerminologyServer()
        for s in (SCT, LOINC):
            print(s)
            for v in ts.code_system_versions(s):
                print("  ", v)
        return 0
    if a.cmd == "baseline":
        from .baseline import run_baseline
        keep = {SCT: "sct" in a.keep_display, LOINC: "loinc" in a.keep_display}
        run_baseline(a.package, a.out, {SCT: a.sct, LOINC: a.loinc}, keep, a.max_total, a.only, a.workers)
        return 0
    if a.cmd == "compare":
        from .compare import run_compare
        targets = {}
        if a.sct: targets[SCT] = a.sct
        if a.loinc: targets[LOINC] = a.loinc
        if not targets:
            print("give at least one of --sct / --loinc", file=sys.stderr); return 2
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
    return 1
