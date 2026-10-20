# kds-terminology-watch

Watches SNOMED CT / LOINC releases for impact on MII KDS ValueSets. Stdlib-only Python (>=3.9), no third-party deps.
Intended to move to the MII GitHub organisation; keep it free of local paths and secrets.

## Run
```bash
set -a; source .env; set +a          # TERMWATCH_CERT / TERMWATCH_KEY / TERMWATCH_KEY_PASS for the MII Ontoserver
PYTHONPATH=src python3 -m termwatch versions|baseline|compare|report ...   # see README
```
Do NOT run python with `-I` here: it ignores PYTHONPATH.

## Layout
- `src/termwatch/ontoserver.py` FHIR TS client ($expand with force-system-version, $validate-code, $lookup, $translate on SNOMED historical ConceptMaps)
- `src/termwatch/rf2.py` local SNOMED CT backend over RF2 Snapshot archives (`compare --rf2 PATH`), same interface as the
  server client; `Router` sends SCT calls for versions it holds there, the rest to the server. Pickle cache in `~/.cache/termwatch`.
  Verified: RF2 20260701 reproduces the server baseline for all 134 SNOMED ValueSets (Ontoserver keeps an inactive is-a
  anchor itself in the expansion, flagged inactive; the backend does the same).
- `src/termwatch/inventory.py` package crawler (ValueSets with SNOMED/LOINC includes, pins, module)
- `src/termwatch/baseline.py` expansions under baseline versions, compact per-system code lists
- `src/termwatch/compare.py` membership diff + severity; `report.py` Markdown per module + CSV
- `baselines/<package-version>/` committed baseline; `reports/` committed Markdown/CSV, JSON ignored

## Conventions
- Baseline files store SNOMED codes only (no displays, licensing); LOINC displays are kept.
- Severity: BREAKING (inactivated member / anchor), SIGNIFICANT (removed from filter, relabelled), MINOR (added), NONE.
- New baseline = new directory named after the KDS package version; never overwrite an old one.
- `src/termwatch/explorer.py` + `explorer_template.html`: `termwatch explorer` builds the subway-map page
  (`explorer/index.html`, data embedded, plus `data.json`). Modelled on the MII
  `mii-kerndatensatz-versionhistory` explorer (plain SVG, no framework). Compare runs against older
  releases are inverted so lanes extend backwards; cap of 120 items per change list in the page.


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
- Generic over code systems since 2026-10-19: `src/termwatch/systems.py` registry (SCT, LOINC, ICD-10-GM, OPS, ATC,
  HGNC + Alpha-ID, Orphanet, UCUM), `discover` command, `--watch auto|all|list`, `--group`, `--system KEY=VERSION`.
  ValueSets that pin several versions of one system are expanded without the pinned includes (soft `system-version`);
  fully pinned ones are stored as `static`. Baseline for ballot.19 now also covers ICD-10-GM/OPS/ATC 2026 and HGNC 20250704.
- Package to use: `~/.fhir/packages/de.medizininformatikinitiative.kerndatensatz.complete#2027.0.0-ballot.19/package`
  (if the cache was cleared: the ballot.19 tgz in the local kerndatensatz-complete build repo, extracted to a scratch dir).
- Anchors already inactive/unknown under the baseline are `anchors_preexisting` (content findings), not release changes.
- `TERMWATCH_DEBUG=1` prints tracebacks for per-ValueSet compare failures.
- Issues: beads (`bd ready`), prefix `tw`.
