"""Render comparison results as Markdown (per module, for the KDS teams) and CSV (technical)."""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from typing import Dict, List

from .systems import label_of  # noqa: E402


class _Labels(dict):
    def __missing__(self, k):
        return label_of(k)


SYSTEM_SHORT = _Labels()


def _ver(v: str) -> str:
    return v.rsplit("/", 1)[-1] if v and "/" in v else (v or "-")


def render_markdown(cmp: dict) -> str:
    rs = cmp["results"]
    pkg = cmp["package"]
    lines: List[str] = []
    lines.append(f"# Terminology release impact: {pkg['name']} {pkg['version']}\n")
    lines.append("| | Baseline | Target |\n|---|---|---|")
    for s in sorted(set(cmp["baseline_versions"]) | set(cmp["target_versions"])):
        lines.append(f"| {SYSTEM_SHORT[s]} | {_ver(cmp['baseline_versions'].get(s))} | {_ver(cmp['target_versions'].get(s, cmp['baseline_versions'].get(s)))} |")
    lines.append(f"\nGenerated {cmp['created']} against {cmp['server']} ({cmp['calls']} server calls).\n")
    sev = Counter(r["severity"] for r in rs)
    lines.append("## Summary\n")
    lines.append("| Severity | ValueSets |\n|---|---:|")
    for k in ("BREAKING", "SIGNIFICANT", "MINOR", "NONE"):
        lines.append(f"| {k} | {sev.get(k, 0)} |")
    lines.append("")
    lines.append("Severity rules: BREAKING = a member of an enumerated include or a filter anchor was inactivated, or a member became inactive; "
                 "SIGNIFICANT = members dropped out of a filter-defined ValueSet or displays changed; MINOR = new members only.\n")
    lines.append("Pinned ValueSets (all includes carry a version) do not change at runtime until the pin is moved; "
                 "unpinned ones change with the next terminology load on the server.\n")
    by_mod: Dict[str, List[dict]] = defaultdict(list)
    for r in rs:
        by_mod[r["module"]].append(r)
    lines.append("## Per module\n")
    lines.append("| Module | ValueSets compared | BREAKING | SIGNIFICANT | MINOR | unchanged |\n|---|---:|---:|---:|---:|---:|")
    for mod, items in sorted(by_mod.items()):
        c = Counter(r["severity"] for r in items)
        lines.append(f"| {mod} | {len(items)} | {c.get('BREAKING',0)} | {c.get('SIGNIFICANT',0)} | {c.get('MINOR',0)} | {c.get('NONE',0)} |")
    lines.append("")
    for mod, items in sorted(by_mod.items()):
        affected = [r for r in items if r["severity"] != "NONE"]
        if not affected:
            continue
        lines.append(f"## Module `{mod}`\n")
        for r in affected:
            pin = "pinned" if r["pinned"] else "UNPINNED"
            lines.append(f"### {r['severity']} · `{r['id']}` ({pin}, {', '.join(r['kinds'])})\n")
            lines.append(f"{r['title'] or ''}  \n`{r['url']}`  ")
            if "count_baseline" in r:
                lines.append(f"Members: {r['count_baseline']} → {r['count_target']}" + ("  (expansion truncated)" if r.get("truncated") else "") + "\n")
            if r.get("note"):
                lines.append(f"> {r['note']}\n")
            for a in r.get("anchors_broken", []):
                succ = ", ".join(f"{s['association']} → {s['code']} {s['display']}" for s in a.get("successors", [])) or "no successor"
                lines.append(f"- **Filter/enumerated anchor inactive:** `{a['code']}` {a['display']} — {succ}")
            for a in r.get("anchors_preexisting", []):
                lines.append(f"- Content note (not a release change): anchor `{a['code']}` {a.get('display') or ''} was already {a.get('reason', 'inactive')} under the baseline")
            if r.get("inactivated"):
                lines.append("\n**Members now inactive (stop using):**\n")
                lines.append("| Code | Display | Status / successor |\n|---|---|---|")
                for m in r["inactivated"]:
                    succ = m.get("status") or ", ".join(f"{s['association']} → {s['code']} {s['display']}" for s in m.get("successors", [])) or "no successor"
                    lines.append(f"| `{m['code']}` | {m.get('display','')} | {succ} |")
            if r.get("removed"):
                lines.append("\n**Members no longer in the ValueSet:**\n")
                lines.append("| Code | Display | Reason | Successor |\n|---|---|---|---|")
                for m in r["removed"]:
                    succ = ", ".join(f"{s['association']} → {s['code']} {s['display']}" for s in m.get("successors", [])) or "-"
                    lines.append(f"| `{m['code']}` | {m.get('display','')} | {m.get('reason','')} | {succ} |")
            if r.get("relabelled"):
                lines.append("\n**Display changed:**\n")
                lines.append("| Code | Old | New |\n|---|---|---|")
                for m in r["relabelled"]:
                    lines.append(f"| `{m['code']}` | {m['old']} | {m['new']} |")
            if r.get("added"):
                lines.append(f"\n**New members ({len(r['added'])}):**\n")
                show = r["added"][:40]
                lines.append("| Code | Display |\n|---|---|")
                for m in show:
                    lines.append(f"| `{m['code']}` | {m['display']} |")
                if len(r["added"]) > 40:
                    lines.append(f"\n… {len(r['added']) - 40} more, see the CSV.")
            lines.append("")
    return "\n".join(lines) + "\n"


def write_csv(cmp: dict, path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["module", "valueset_id", "valueset_url", "pinned", "severity", "change", "system", "code", "display_old", "display_new", "reason_or_status", "successors"])
        for r in cmp["results"]:
            base = [r["module"], r["id"], r["url"], r["pinned"], r["severity"]]
            for a in r.get("anchors_broken", []):
                w.writerow(base + ["anchor_inactive", a.get("system", "http://snomed.info/sct"), a["code"], a["display"], "", a.get("reason", "inactive"), "; ".join(f"{s['association']}:{s['code']}" for s in a.get("successors", []))])
            for a in r.get("anchors_preexisting", []):
                w.writerow(base + ["anchor_preexisting", a.get("system", "http://snomed.info/sct"), a["code"], a.get("display", ""), "", a.get("reason", "inactive"), ""])
            for m in r.get("inactivated", []):
                w.writerow(base + ["inactivated", m["system"], m["code"], m.get("display", ""), "", m.get("status", ""), "; ".join(f"{s['association']}:{s['code']}" for s in m.get("successors", []))])
            for m in r.get("removed", []):
                w.writerow(base + ["removed", m["system"], m["code"], m.get("display", ""), "", m.get("reason", ""), "; ".join(f"{s['association']}:{s['code']}" for s in m.get("successors", []))])
            for m in r.get("relabelled", []):
                w.writerow(base + ["relabelled", "", m["code"], m["old"], m["new"], "", ""])
            for m in r.get("added", []):
                w.writerow(base + ["added", m["system"], m["code"], "", m["display"], "", ""])
