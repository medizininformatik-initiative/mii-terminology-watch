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
- `src/termwatch/inventory.py` package crawler (ValueSets with SNOMED/LOINC includes, pins, module)
- `src/termwatch/baseline.py` expansions under baseline versions, compact per-system code lists
- `src/termwatch/compare.py` membership diff + severity; `report.py` Markdown per module + CSV
- `baselines/<package-version>/` committed baseline; `reports/` committed Markdown/CSV, JSON ignored

## Conventions
- Baseline files store SNOMED codes only (no displays, licensing); LOINC displays are kept.
- Severity: BREAKING (inactivated member / anchor), SIGNIFICANT (removed from filter, relabelled), MINOR (added), NONE.
- New baseline = new directory named after the KDS package version; never overwrite an old one.
