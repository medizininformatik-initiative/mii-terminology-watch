# kds-terminology-watch

Watches SNOMED CT and LOINC releases for their impact on the ValueSets of the MII Kerndatensatz (KDS).
It takes a **baseline** (a KDS package expanded under the terminology versions it was balloted with) and
**compares** it against newer terminology versions on a FHIR terminology server, producing a per-module
Markdown report for the KDS module teams and a flat CSV for technical follow-up.

Current baseline: `de.medizininformatikinitiative.kerndatensatz.complete 2027.0.0-ballot.19`
with SNOMED CT International `20260701` and LOINC `2.82`.

## Why

Ballot.19 pins 79 SNOMED CT includes to the July 2026 International edition and 56 LOINC includes to 2.82,
but 108 SNOMED and 70 LOINC includes are unpinned and change membership with every terminology load.
Everything from the SNOMED August 2026 release and LOINC 2.83 onwards is therefore relevant for the
module teams preparing the next KDS versions. This tool makes those changes visible per ValueSet and per module.

## How it works

1. `inventory` — reads every `ValueSet-*.json` of a FHIR package, keeps those with SNOMED CT or LOINC
   includes, records kind (enumerated / filter / whole-system), version pin and module.
2. `baseline` — expands each ValueSet on the terminology server with `force-system-version` set to the
   baseline versions (`activeOnly=false`) and stores the member codes. SNOMED displays are not stored
   (licensing); LOINC displays are.
3. `compare` — re-expands under the target versions and classifies per ValueSet:
   added, removed (with `$validate-code` and SNOMED historical associations REPLACED BY / SAME AS /
   POSSIBLY EQUIVALENT TO … via `ConceptMap/$translate`), newly inactive (LOINC STATUS), display changes,
   and inactive filter/enumerated anchors. Severity: BREAKING / SIGNIFICANT / MINOR / NONE.
4. `report` — Markdown grouped by module and severity, plus CSV.

Server operations used: `ValueSet/$expand` (with `force-system-version`, paging), `CodeSystem/$validate-code`,
`CodeSystem/$lookup`, `ConceptMap/$translate` on implicit SNOMED historical ConceptMaps. Tested against the
MII Ontoserver (SU-TermServ).

## Usage

```bash
cp .env.example .env        # set certificate paths for the MII Ontoserver (DFN client certificate)
set -a; source .env; set +a

PKG="$HOME/.fhir/packages/de.medizininformatikinitiative.kerndatensatz.complete#2027.0.0-ballot.19/package"

python -m termwatch versions
python -m termwatch baseline --package "$PKG" --out baselines/kds-complete-2027.0.0-ballot.19 \
    --sct http://snomed.info/sct/900000000000207008/version/20260701 --loinc 2.82
python -m termwatch compare  --baseline baselines/kds-complete-2027.0.0-ballot.19 --package "$PKG" \
    --loinc 2.83 --out reports/ballot19_loinc-2.83.json
python -m termwatch report   --compare reports/ballot19_loinc-2.83.json \
    --md reports/ballot19_loinc-2.83.md --csv reports/ballot19_loinc-2.83.csv
```

`PYTHONPATH=src` is needed when running from the checkout without `pip install -e .`.
No third-party dependencies (Python ≥ 3.9).

## Repository layout

```
baselines/<package-version>/inventory.json      watched ValueSets with includes, pins, module
baselines/<package-version>/baseline.json       versions, server, timestamp
baselines/<package-version>/expansions/*.json   member codes per ValueSet under the baseline versions
reports/                                        comparison JSON (ignored) + Markdown/CSV reports (committed)
src/termwatch/                                  ontoserver.py inventory.py baseline.py compare.py report.py cli.py
```

## Limitations

- SNOMED ECL/is-a expansions exclude inactive concepts, so an inactivated member shows up as *removed*
  and is then confirmed via `$validate-code`; LOINC members stay in the expansion with `inactive=true`.
- LOINC `MapTo` successors are not exposed by the server; add the LOINC release files to resolve them (planned).
- ValueSets that reference other ValueSets are inlined from the same package; cross-package references
  are passed to the server as-is.
- Expansions above `--max-total` (default 500 000, page size 50 000) are truncated and marked.

## Roadmap

See `docs/` in the companion design document (Release Change Framework): LOINC release-file parser (MapTo,
CHNG_TYP), SNOMED RF2 delta cross-check, German edition / deDE translation tracking, usage-weighted
impact, CI run on new server versions with automatic PRs against module repositories.

## Licence

Code, documentation and reports: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (see `LICENSE`).
SNOMED CT and LOINC content remain under their own licences; baselines store code identifiers only
(plus LOINC display text).
