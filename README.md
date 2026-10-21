# kds-terminology-watch

Watches SNOMED CT and LOINC releases for their impact on the ValueSets of the MII Kerndatensatz (KDS).
It takes a **baseline** (a KDS package expanded under the terminology versions it was balloted with) and
**compares** it against newer terminology versions on a FHIR terminology server, producing a per-module
Markdown report for the KDS module teams and a flat CSV for technical follow-up.

Current baseline: `de.medizininformatikinitiative.kerndatensatz.complete 2027.0.0-ballot.19`
with SNOMED CT International `20260701` and LOINC `2.82`. Compared so far: LOINC 2.81 / 2.83,
ICD-10-GM / OPS / ATC 2025, SNOMED CT International 20260401 / 20260901 / 20261001 (the last two from
RF2 archives, see below).

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

python -m termwatch discover --package "$PKG"          # which code systems does the package bind, which does the server version?
python -m termwatch versions                            # versions of the watched systems on the server

python -m termwatch baseline --package "$PKG" --out baselines/kds-complete-2027.0.0-ballot.19 \
    --sct http://snomed.info/sct/900000000000207008/version/20260701 --loinc 2.82 \
    --icd10gm 2026 --ops 2026 --atc 2026 --hgnc 20250704
python -m termwatch compare  --baseline baselines/kds-complete-2027.0.0-ballot.19 --package "$PKG" \
    --loinc 2.83 --out reports/kds-complete-2027.0.0-ballot.19_loinc-2.83.json
python -m termwatch report   --compare reports/kds-complete-2027.0.0-ballot.19_loinc-2.83.json \
    --md reports/kds-complete-2027.0.0-ballot.19_loinc-2.83.md --csv reports/kds-complete-2027.0.0-ballot.19_loinc-2.83.csv
```

### SNOMED CT releases the server does not have yet (RF2 archives)

The MII Ontoserver lags the SNOMED International release train by a few months. `--rf2` points
`compare` at an RF2 release archive (zip or extracted directory with `Snapshot/`); the version it holds
is then answered locally and everything else still goes to the server:

```bash
python -m termwatch compare --baseline baselines/kds-complete-2027.0.0-ballot.19 --package "$PKG" \
    --sct http://snomed.info/sct/900000000000207008/version/20261001 \
    --rf2 ~/terminologies/SnomedCT_InternationalRF2_PRODUCTION_20261001T120000Z.zip \
    --out reports/kds-complete-2027.0.0-ballot.19_sct-20261001.json
```

The archive is parsed once (concepts, inferred is-a relationships, preferred terms, historical
associations, inactivation reasons; ~10 s) and cached under `~/.cache/termwatch` (`TERMWATCH_CACHE`).
Edition and date are read from the archive name; `--rf2 PATH=VERSION_URI` overrides that.
Validated against the server: expanding all 134 SNOMED ValueSets of ballot.19 from the 20260701
archive reproduces the server baseline exactly. Supported: enumerated includes, `is-a` /
`descendent-of` filters, ECL with `<`, `<<`, `>`, `>>`, `AND`, `OR`, `MINUS` and brackets.
Refined ECL raises an expansion error, like the server does for invalid ECL. Inactivation reasons
(Duplicate, Outdated, Ambiguous, Classification derived, …) are reported next to the successors.

### Decision tooling for inactivated codes

`termwatch decide` turns the successor lists of a comparison into decisions: one item per code, the
historical associations (the same data Snowstorm / Ontoserver expose as implicit ConceptMaps) as ranked
candidates, and a status that says how much a human has to do.

```bash
python -m termwatch decide --compare reports/kds-complete-2027.0.0-ballot.19_sct-20261001.json \
    --baseline baselines/kds-complete-2027.0.0-ballot.19 --out decisions/kds-complete-2027.0.0-ballot.19_sct-20261001 \
    --rf2 .../SnomedCT_InternationalRF2_PRODUCTION_20260701T120000Z.zip --rf2 .../SnomedCT_InternationalRF2_PRODUCTION_20261001T120000Z.zip
```

| Status | Meaning |
|---|---|
| auto | a single SAME AS / REPLACED BY successor, resolved without a human |
| proposed | several candidates, exactly one survives the signals (member of the re-expanded ValueSet, active, same top-level hierarchy, term overlap); to confirm |
| open | several candidates survive; a human picks, the shortlist is ranked |
| none | no historical association; the module team decides |
| out-of-filter | the code is still active and only dropped out of the filter; data stays valid |

Outputs: `decisions.json` (decisions survive re-runs, a decision is per code and applies to every ValueSet),
`summary.md` as agenda for a terminology council, `ConceptMap-<valueset>.json` drafts (R4, old → new SNOMED
version, equivalence from the association: SAME AS = equal, REPLACED BY = equivalent, WAS A = wider,
POSSIBLY / PARTIALLY EQUIVALENT TO = inexact, open items unmatched with the candidates in a comment) and
`review.html`, a self-contained page to pick candidates and export `decisions.json`. The review pages are
published under `explorer/decisions/`. For SNOMED CT 20261001 the ranking leaves 110 open and 137 unresolvable
codes for people, out of 824 inactivated codes across 20 ValueSets.

### Any package, any code system

Nothing in the pipeline is tied to the Kerndatensatz. Three switches make it run against another
specification or terminology server:

- `--watch` chooses the code systems. Default: SNOMED CT, LOINC, ICD-10-GM, OPS, ATC, HGNC.
  `--watch auto` watches every system the package binds that the server has at least one version of
  (`discover` shows that list), `--watch all` the whole registry, or give keys/URLs explicitly.
  `--system URL=VERSION` sets a version for any system, including ones not in the registry.
- `--group` chooses how ValueSets are grouped into lanes: `mii` (default, `modul-<name>` in the canonical),
  `package`, `host`, or a regular expression with one capturing group over the canonical URL.
- `TERMWATCH_FHIR_BASE` points at any FHIR terminology server that supports `$expand` with
  `force-system-version` / `system-version` (Ontoserver, tx.fhir.org, HAPI with the right loaders).

Per-system behaviour lives in one table in `src/termwatch/systems.py`: how a release is spelled,
how the status of a code is read (LOINC `STATUS` property, otherwise `$validate-code`), whether
is-a filter values are checked as anchors (SNOMED CT), and where successors come from (SNOMED CT
historical associations). A system without an entry gets the generic adapter.

ValueSets that union several pinned yearly releases of one system (the KDS diagnosis ValueSet
includes ICD-10-GM 2009 through 2026) are expanded without the pinned includes: those never change,
only unpinned includes follow a new release. A ValueSet whose includes are all pinned is kept as a
static lane; its only "change" is the module team adding the next year.

`PYTHONPATH=src` is needed when running from the checkout without `pip install -e .`.
No third-party dependencies (Python ≥ 3.9).

## Repository layout

```
baselines/<package-version>/inventory.json      watched ValueSets with includes, pins, module
baselines/<package-version>/baseline.json       versions, server, timestamp
baselines/<package-version>/expansions/*.json   member codes per ValueSet under the baseline versions
reports/                                        comparison JSON (ignored) + Markdown/CSV reports (committed)
src/termwatch/                                  ontoserver.py rf2.py inventory.py baseline.py compare.py report.py explorer.py decide.py cli.py
decisions/<run>/                                decisions.json, summary.md, ConceptMap-*.json, review.html
```

## Explorer (human-facing view)

Live: https://medizininformatik-initiative.github.io/mii-terminology-watch/ (rebuilt from `explorer/` on every push to `main`).

`termwatch explorer` renders a self-contained HTML page in the style of the MII
[Kerndatensatz version-history explorer](https://github.com/medizininformatik-initiative/mii-kerndatensatz-versionhistory):
a subway map whose columns are terminology releases and whose lanes are ValueSets.

```bash
python -m termwatch explorer --baseline baselines/kds-complete-2027.0.0-ballot.19 \
  --compare reports/kds-complete-2027.0.0-ballot.19_loinc-2.83.json reports/..._loinc-2.81.json \
  --out explorer/
```

Reading the map:

| Element | Meaning |
|---|---|
| Column | a SNOMED CT or LOINC release; the vertical accent line marks the ballot's pinned version |
| Lane | one ValueSet of the chosen module (one map per code system) |
| Segment colour | what happened to the ValueSet's members between two releases: unchanged, new codes, display texts changed, active codes dropped out of the filter, codes inactivated / filter anchor inactive |
| Dashed segment | the ValueSet is pinned, so the change only takes effect when the module team moves the pin |
| Station size | member count (log scale); a filled red/amber station is an interchange, i.e. members were inactivated or removed |
| Vertical dashed link | the same code change hits several ValueSets of the module; the `+n VS` badge counts ValueSets in other modules |
| Grey column | a release that is expected but not yet on the server or in an RF2 archive (`--expected KEY=VERSION`) |

The detail panel shows the counts, a "what to do" list derived from the include type and pin status,
the affected codes with status and successors, and a code search over all change lists.
Any number of compare runs can be combined; runs against an older release are inverted automatically,
so the lanes extend backwards in time.

## Limitations

- SNOMED ECL/is-a expansions exclude inactive concepts, so an inactivated member shows up as *removed*
  and is then confirmed via `$validate-code` (reason "inactivated (Outdated)" etc.); LOINC members stay in
  the expansion with `inactive=true`.
- Filter/enumerated anchors that were already inactive or unknown under the baseline are reported as
  `anchors_preexisting` (content findings) and do not raise the severity of a release.
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
