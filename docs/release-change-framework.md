# Release Change Framework for SNOMED CT and LOINC

**Status:** proposal, 2026-10-19
**Scope:** detect content changes between two releases of SNOMED CT (International + German edition) and LOINC (Loinc.csv + German deDE translation), and turn them into (A) a human-readable Release Change Report for coder/content-creator training and general dissemination and (B) a technical Specification Impact Diff for existing ValueSets and specifications (MII KDS, HL7 DE, local code lists).

---

## 1. What exists today (survey)

### 1.1 Lübeck: TerminoDiff (Wiedekopf et al., MIE 2022)

The Lübeck release-comparison tool is **TerminoDiff** (Wiedekopf J, Drenkhahn C, Rosenau L, Ulrich H, Kock-Schoppenhauer AK, Ingenerf J. *TerminoDiff – Detecting Semantic Differences in HL7 FHIR CodeSystems.* Stud Health Technol Inform 2022;294:362-366, DOI 10.3233/SHTI220475). Repo: https://github.com/skfit-uni-luebeck/TerminoDiff (Kotlin, Compose desktop GUI, GPL-3).

Note: a tool named "TermDiff" authored by Tessa Ohlsen could not be verified. Ohlsen's cross-version work targets ICD-10-GM/OPS (crosswalk ConceptMaps, MIE 2024, DOI 10.3233/SHTI240652; Covhisto, GMDS 2025, DOI 10.3233/SHTI251394). The `termdiff` directory in this container is our own prototype, not the Lübeck tool.

| Aspect | TerminoDiff |
|---|---|
| Input | two FHIR R4 `CodeSystem` resources (file or terminology-server read/vread). No RF2, no LOINC CSV, no ValueSet, no ConceptMap. |
| Diff levels | metadata (string + keyed-list diffs), concepts (display, definition, `property`, `designation`, unilateral add/remove), edge graph (added/removed parent/child, colour-coded JGraphT view) |
| Output | interactive GUI; generation of a FHIR `ConceptMap` old→new. No Markdown/HTML/JSON report export. |
| Gaps stated by authors | ValueSet/ConceptMap diffing "likely with TS support" (open); large CodeSystems heavy in graph view |

Takeaways to reuse: the three-level diff model (metadata / concept / edge), ConceptMap-as-transition-artefact, and the scoping review of ontology diff tools (COnto-Diff, PROMPTDIFF, ChImp) at https://skfit-uni-luebeck.github.io/TerminoDiff/SLR.html.

### 1.2 Leipzig: TOP Framework and "Tracking Changes" (IMISE, SMITH)

**TOP = Terminology- and Ontology-based Phenotyping** (Uciteli, Beger, Schäfermeier et al.; https://github.com/Onto-Med; J Biomed Semantics 2026, DOI 10.1186/s13326-026-00364-7). It models executable phenotypes whose entities carry codes (`CodeSystem{uri, version, latest}`, `Code`, `CodeScope: SELF|SUBTREE|LEAVES`) resolved through OLS4, not a FHIR terminology server. Phenotype entities are versioned, but there is **no** code-validity re-check after a terminology release, no code-list diff, and no change report. "Backward compatibility with previous versions of phenotype definitions" is listed as future work.

The relevant Leipzig piece is a sibling project: Schäfermeier et al., *Tracking Changes for Inter-Version Interoperability in Heterogeneous Evolving Medical Terminologies*, GMDS 2024 (DOI 10.3205/24gmds059) and SHTI 317:190-199 (DOI 10.3233/SHTI240855). Method: declarative import (CSV/XML/OWL) → common data model → semantic + lexical change detection → **changes represented as an ontology and queried with semantic query languages**; detects additions, deletions, relocations, renamings, and distinguishes refinement/consolidation when the publisher ships inter-version mappings. No public repo verified (`Onto-Med/bubastis-semlex` fork is a plausible engine).

Takeaways to reuse: a terminology-agnostic **common change model** with a small, fixed change taxonomy, and the idea that the diff itself is a queryable artefact (we will use a FHIR-native representation rather than OWL).

### 1.3 SNOMED International

- RF2 `Delta` plus `effectiveTime`/`active` are the canonical change carriers. Terminology Services Guide §4.9 defines the change matrix: none→active = **Addition**, active→active with changed row = **Change**, active→inactive = **Inactivation**, inactive→active = **Reactivation**. It states explicitly that Snowstorm/FHIR do not expose this directly.
- Historical association refsets (SAME AS, REPLACED BY, POSSIBLY EQUIVALENT TO, ALTERNATIVE, WAS A, MOVED TO, PARTIALLY EQUIVALENT TO) and the concept/description inactivation indicator refsets carry *reason* and *replacement*.
- Release notes are curated (release-notes-service, Elasticsearch line items), brief, and hand-written; "Early Visibility Release Notifications" pre-announce breaking changes.
- Tooling: `delta-generator-tool` (two Full archives → Delta), `rf2-diff-generator` (JSON diff report, archived 2023), `reporting-engine` + Reporting Platform (authoring community), `release-validation-framework` (RVF), Daily Build browser summary (new / inactivated / reactivated concepts, description and refset changes). Snowstorm offers only branch-vs-branch `reviews`/`merge-reviews`, not per-release views.
- NHS England publishes **usage-weighted** inactivation lists ("High Volume Usage Concept Inactivations", instance counts per inactivated concept) and an "Inactives Fact Sheet" requiring suppliers to surface inactive codes in templates/searches and offer replacements via association refsets.
- SNOMED CT-AU release notes: Release Summary / Inclusions / Change Summary / Future Changes, no counts, internal risk matrix.

### 1.4 LOINC (Regenstrief) and BfArM German translation

- `Loinc.csv` `STATUS` ∈ ACTIVE / TRIAL / DISCOURAGED / DEPRECATED; `MapTo` table (`LOINC, MAP_TO, COMMENT`) carries 1:n successors for DISCOURAGED/DEPRECATED.
- `CHNG_TYP` ∈ NAM (component renamed), MAJ (other primary axis), MIN (secondary field), DEL (deprecated), UND (undeprecated), PANEL.
- `ChangeSnapshot/LoincChangeSnapshot.csv` (status changes and all changed Loinc.csv fields, excludes new terms) and `PartChangeSnapshot.csv`; release notes ship CSVs "new terms and totals by type", "term status changes". Answer lists are re-published in full.
- German translation (BfArM, linguistic variant `deDE15`, ~16,000 terms, biannual, monthly from March 2027) with its own release notes; deprecated terms annotated "(Do not use this term anymore)".
- No third-party LOINC release diff tool found.

### 1.5 Value-set impact tooling elsewhere

| Tool | What it does | Reusable idea |
|---|---|---|
| FHIR `$expand` with `system-version` | expand the same ValueSet under two code-system versions | expansion-pair diff, works on Ontoserver today |
| `ValueSet/$compare` (FHIR Tooling IG, live on tx.fhir.org) | membership relation `same / subset / superset / overlapping / disjoint` | result vocabulary |
| IG Publisher previous-version comparison | profile/VS/CS diff vs last publication | integrate into IG build |
| VSAC Comparison Tool | side-by-side 2–5 VS versions, red/grey rows, Excel | per-ValueSet rendering |
| OHDSI Alathea (`phenotypechangesinvocabupdate`) | flags concept-set members that became non-standard / changed domain after vocab update, counts affected patients | usage-weighted impact |
| Erasmus MC VocabularyVersioning / Tantalus | stacked deltas "inspired by SNOMED versioning", tracks concept sets/cohorts | delta stacking over multiple releases |
| UMLS MRCUI / DELETEDCUI / MERGEDCUI | per-release deleted/merged/bequeathed identifiers | successor semantics |
| Cimino 1998 Desiderata; Ceusters & Mullin 2019 | concept permanence, graceful evolution; evidence it is violated | rationale for successor resolution |

**Gap:** none of SNOMED International, NCTS/Ontoserver, Regenstrief, TOP or TerminoDiff ships a ValueSet- or specification-level impact report for a SNOMED/LOINC release. That is the framework's core contribution.

---

## 2. Requirements

**R1 Release ingest** — SNOMED International, SNOMED German edition (BfArM/MLDS), LOINC (Loinc.csv, MapTo, ChangeSnapshot, AnswerLists), LOINC deDE. Primary from release files; fallback via FHIR terminology server (MII Ontoserver) using `$lookup`/`$expand` with explicit versions.

**R2 Common change model** — one taxonomy for both terminologies, provenance-tagged (publisher-declared vs computed).

**R3 Specification inventory** — crawl FHIR packages (KDS modules, HL7 DE Basisprofile, local IGs), extract every binding to SNOMED/LOINC: `ValueSet.compose` (enumerated and filter/ECL), `ElementDefinition.binding`, `Questionnaire.answerOption`/`answerValueSet`, `ConceptMap` source/target, SQL-on-FHIR ViewDefinition constants, CQL valueset declarations.

**R4 Impact computation** — per include and per ValueSet: added / removed / inactivated / relabelled / relocated members; ECL anchor validity; LOINC filter property drift; severity.

**R5 Human report** — tiered (coder/content creator, implementer, management), German and English, with replacement guidance, domain grouping, and training-ready examples.

**R6 Technical diff** — JSON + CSV/XLSX + FHIR artefacts (ConceptMap of successors, proposed ValueSet revisions, OperationOutcome-style findings), diffable in git, consumable by CI.

**R7 Reproducibility** — every number traceable to release IDs (`effectiveTime`, LOINC version, package version), rerunnable, tested on fixtures.

**R8 Cadence** — SNOMED International monthly, German edition May/Nov, LOINC Feb/Aug, deDE monthly from 2027; KDS BOM yearly with ballots.

Baseline from the KDS complete package 2026.1.0 (312 ValueSets):

| System | ValueSets | enumerated codes | filter includes | version-pinned includes |
|---|---:|---:|---:|---:|
| SNOMED CT | 98 | 553 | 50 (is-a 26, descendent-of 18, ECL `constraint` 5, code is-a 1) | 17 of 117 |
| LOINC | 40 | 281 | 36 (CLASS 30, STATUS 32, METHOD_TYP 26, PROPERTY 15, SCALE_TYP 15, SYSTEM 5, ORDER_OBS 5, CLASSTYPE 4) | 0 of 64 |

Unpinned filter includes mean a KDS ValueSet silently changes membership with every terminology release; that is exactly what the impact diff must make visible.

---

## 3. Architecture

```
            ┌──────────────┐   ┌──────────────┐   ┌──────────────────┐
  sources   │ SNOMED RF2   │   │ LOINC CSV    │   │ FHIR TS fallback │
            │ Intl + DE    │   │ + MapTo      │   │ (Ontoserver,     │
            │ Snapshot/Δ   │   │ + ChangeSnap │   │  $expand/$lookup)│
            └──────┬───────┘   └──────┬───────┘   └────────┬─────────┘
                   ▼                  ▼                     ▼
  L1 ingest   parsers/rf2        parsers/loinc        parsers/fhir_ts
                   └──────────────────┴─────────────────────┘
                                      ▼
  L2 diff     engine/  → ChangeSet in the Common Change Model (CCM)
              (computed snapshot diff  ⊕  publisher-declared deltas, cross-checked)
                                      ▼
  L3 enrich   enrichers/  successors (hist. assoc., MapTo), hierarchy context,
              translations (SNOMED DE, deDE), usage counts (optional, DIZ SQL-on-FHIR)
                                      ▼
  L4 impact   impact/  SpecInventory (FHIR packages, ViewDefinitions, CQL)
              × ChangeSet  → ImpactSet per ValueSet / binding / mapping
                                      ▼
  L5 render   renderers/  (A) Release Change Report  (B) Spec Impact Diff
              md / html / docx / social   json / csv / xlsx / FHIR Bundle / PR
```

Layers L1, L2 and L5 exist in `termdiff` for SNOMED RF2 (pandas merge diff, Jinja2 renderers). L1-LOINC, L3 successors, L4 and the FHIR outputs are new.

### 3.1 Common Change Model (CCM)

```
ChangeSet
  release_from, release_to            # e.g. SCT INT 20260701 → 20260801; LOINC 2.81 → 2.82
  source_kind: computed | declared    # snapshot diff vs Delta/ChangeSnapshot
  changes: [Change]

Change
  system          : sct | loinc
  entity          : concept | designation | edge | property | refset_member | answer_list | mapping
  subject         : code (+ designation id / edge id where applicable)
  kind            : ADDITION | INACTIVATION | REACTIVATION | RENAME | RELOCATION
                  | PROPERTY_CHANGE | STATUS_CHANGE | SUCCESSOR_LINK | TRANSLATION_CHANGE
  old, new        : values (FSN, parent set, STATUS, CHNG_TYP fields …)
  reason          : SCT inactivation indicator | LOINC CHNG_TYP
  successors      : [{code, relation}]   # SAME AS, REPLACED BY, POSSIBLY EQUIVALENT TO, MapTo …
  domain          : SCT semantic tag / top-level hierarchy | LOINC CLASS
  module          : SCT moduleId (Intl vs DE extension) | LOINC core vs deDE
  provenance      : declared | computed | both
  severity        : BREAKING | SIGNIFICANT | MINOR | COSMETIC   (rule-based, see 3.3)
```

Mapping of native signals onto CCM kinds:

| CCM kind | SNOMED signal | LOINC signal |
|---|---|---|
| ADDITION | concept row new, active=1 | new LOINC in Loinc.csv |
| INACTIVATION | active 1→0 + inactivation indicator | STATUS → DEPRECATED (CHNG_TYP DEL) or → DISCOURAGED |
| REACTIVATION | active 0→1 | CHNG_TYP UND |
| RENAME | FSN/PT description change (Intl or DE language refset) | CHNG_TYP NAM (COMPONENT) / LONG_COMMON_NAME change |
| RELOCATION | inferred IS-A parent set changed | CLASS change (MAJ) |
| PROPERTY_CHANGE | defining relationship / refset membership change | MAJ / MIN on any axis (PROPERTY, SYSTEM, SCALE_TYP, METHOD_TYP …) |
| STATUS_CHANGE | definition status, moduleId move | TRIAL → ACTIVE |
| SUCCESSOR_LINK | historical association refset member | MapTo row |
| TRANSLATION_CHANGE | DE language refset / DE description change | deDE LinguisticVariant change |

### 3.2 Specification inventory and impact computation

Inventory (`SpecInventory`) is built once per run from a list of FHIR packages (`~/.fhir/packages`, Simplifier/registry tgz) plus optional ViewDefinition and CQL directories. Each binding is normalised to `Include{system, version?, concepts[] | filter}`.

Impact per include:

| Include type | Method | Detected |
|---|---|---|
| enumerated | join concept list with ChangeSet | members INACTIVATED / RENAMED / RELOCATED; successor proposals |
| SCT is-a / descendent-of / ECL | expand under `release_from` and `release_to` (local: snowstorm ECL; remote: `$expand` with `system-version`), set-diff | GROWN (new members), SHRUNK (inactivated members), anchor concept inactivated → BROKEN |
| LOINC property filter (CLASS=, STATUS=, …) | evaluate filter on both Loinc.csv versions | GROWN / SHRUNK; filter value no longer exists → BROKEN |
| whole system | count only | counts |

ValueSet verdict uses the FHIR `$compare` vocabulary: `same | superset | subset | overlapping | broken`, plus a severity derived from the worst member change and from whether the include is version-pinned (pinned = informational only, unpinned = live impact).

Downstream: a binding in a `StructureDefinition` inherits its ValueSet's verdict; `ConceptMap` entries whose source/target became inactive are flagged; ViewDefinition/CQL constant codes are checked like enumerated includes.

### 3.3 Severity rules (initial)

| Severity | Rule |
|---|---|
| BREAKING | member or ECL anchor inactivated in an unpinned include; ConceptMap target inactivated; LOINC DEPRECATED in enumerated include |
| SIGNIFICANT | RELOCATION changing is-a membership; LOINC DISCOURAGED; MAJ axis change on a member; FSN/LN change on a member used as display in instances |
| MINOR | ADDITION into an ECL-defined ValueSet (grown); MIN change; new synonym |
| COSMETIC | translation-only change, definition text |

Usage weighting (optional, NHS-style): if a DIZ provides counts per code (SQL-on-FHIR `count(*) by code`), impact is multiplied into a "patients/instances affected" column, as in OHDSI Alathea.

---

## 4. Output A: Release Change Report (human-readable)

Audience tiers in one document, rendered from the same ChangeSet + ImpactSet:

1. **Executive summary** (management, newsletter, social snippet): counts per CCM kind and domain, headline changes, pinned vs live impact on KDS modules.
2. **For coders and content creators** (training section, DE):
   - *Nicht mehr verwenden* — inactivated/deprecated codes with reason and recommended successor, grouped by domain, ordered by usage if available.
   - *Neu verfügbar* — additions in domains covered by the inventory (not all 10k+ additions), with FSN/LN and German term where present.
   - *Umbenannt / verschoben* — FSN, LN, parent moves with before/after.
   - *Deutsche Übersetzung* — new/changed DE terms (SNOMED DE edition, LOINC deDE).
   - Worked examples: three to five changes walked through with "what you coded before / what you code now / why", generated from the highest-severity items.
   - Glossary of change kinds and SNOMED inactivation reasons / LOINC CHNG_TYP.
3. **For implementers**: per affected package and ValueSet, verdict, member deltas, proposed fixes; link to the technical diff.
4. **Appendix**: methodology, release identifiers, cross-check of computed vs declared deltas (discrepancies listed, following Covhisto's finding that publisher tables miss changes).

Formats: Markdown (git), HTML (static site per release), DOCX (dissemination), one-paragraph social/newsletter snippet. Existing Jinja2 templates in `templates/` are the starting point.

## 5. Output B: Specification Impact Diff (technical)

- `changeset.json` — full CCM, one file per terminology and release pair, stable ordering so git diffs are meaningful.
- `impact.json` — per package → ValueSet → include → member deltas with severity and verdict.
- `impact.csv` / `.xlsx` — flat table for review meetings and ballot comments.
- FHIR artefacts (R4 Bundle):
  - `ConceptMap` old-code → successor (SAME AS / REPLACED BY / MapTo) restricted to codes actually used in the inventory;
  - proposed `ValueSet` revisions (enumerated includes with inactivated members removed or replaced, `version` pinned), marked `experimental=true` for review;
  - `OperationOutcome`-style findings list with severity, for CI gating.
- CI integration: GitHub Action triggered on new release availability; on BREAKING findings open a PR against the owning spec repo with the proposed ValueSet revisions and the per-ValueSet markdown section in the PR body.

---

## 6. Implementation plan (termdiff v2)

| # | Work package | Builds on | Notes |
|---|---|---|---|
| 1 | LOINC parser (`parsers/loinc`): Loinc.csv, MapTo, LoincChangeSnapshot, AnswerList, deDE variant | parser Protocol | map CHNG_TYP to CCM |
| 2 | CCM models replace `ConceptChange`; keep `ChangeType`, add kinds, provenance, successors | `models/` | pydantic, JSON schema export |
| 3 | SNOMED successors + inactivation reasons from association/indicator refsets; DE language refset diff | `engine/`, `parsers/rf2` | currently missing |
| 4 | Declared-delta cross-check: RF2 Delta and LoincChangeSnapshot vs computed diff, discrepancy report | `engine/` | reproducibility appendix |
| 5 | `SpecInventory`: FHIR package crawler (ValueSet, bindings, Questionnaire, ConceptMap), ViewDefinition + CQL extractors | new `impact/` | start with KDS complete 2026.1.0 |
| 6 | Impact engine: enumerated join, ECL/is-a expansion under two versions (snowstorm local or Ontoserver `system-version`), LOINC filter evaluation | new `impact/` | Ontoserver needs ≥2 versions loaded |
| 7 | Severity rules + optional usage weighting | `engine/classifier.py` | configurable YAML |
| 8 | Report renderers: tiered Markdown/HTML/DOCX, DE/EN, worked examples | `renderers/`, `templates/` | extend existing |
| 9 | FHIR outputs: ConceptMap, proposed ValueSets, findings Bundle | new `renderers/fhir` | |
| 10 | CI: release watcher, GitHub Action, PR generation | `cli.py` | |
| 11 | Fixtures: mini RF2 pairs incl. association refsets; mini LOINC pair; mini FHIR package | `tests/fixtures` | |

Suggested first milestone: WP 1, 2, 3, 5, 6 on the KDS complete package with SNOMED International 2026-07 → 2026-08 and LOINC 2.81 → 2.82, producing `impact.csv` and the coder section of the report.

## 7. Open decisions

- **Expansion engine for ECL**: local snowstorm (full control, two versions side by side) vs MII Ontoserver `$expand` with `system-version` (no install, but requires both versions loaded and rate limits). Recommendation: Ontoserver first, snowstorm when offline runs are needed.
- **German edition handling**: diff Intl and DE edition separately (module-aware) so that DE extension changes are reported in their own section.
- **Report language**: DE for coder section, EN for implementer/technical sections, or fully bilingual via template switch.
- **Where the inventory lives**: static list of packages in config vs auto-discovery from `~/.fhir/packages` and the KDS BOM.
- **Governance**: who reviews BREAKING findings before a PR is opened (TC Terminologien / TF KDS), and whether the report is published on mii-termserv.de or the KDS site.

## 8. Sources

- Wiedekopf et al. 2022, TerminoDiff, DOI 10.3233/SHTI220475; https://github.com/skfit-uni-luebeck/TerminoDiff
- Ohlsen, Wiedekopf, Ingenerf 2024, ICD-10 crosswalks, DOI 10.3233/SHTI240652; Ohlsen, Müller, Ingenerf 2025, Covhisto, DOI 10.3233/SHTI251394
- TOP Framework: https://www.imise.uni-leipzig.de/en/Research/TOP ; https://github.com/Onto-Med ; Beger et al. 2026, DOI 10.1186/s13326-026-00364-7
- Schäfermeier et al. 2024, Tracking Changes, DOI 10.3205/24gmds059 and 10.3233/SHTI240855
- SNOMED Terminology Services Guide §4.9: https://docs.snomed.org/snomed-ct-practical-guides/snomed-ct-terminology-services-guide/4-terminology-service-types/4.9-identify-changes-to-the-terminology
- IHTSDO tools: https://github.com/IHTSDO/delta-generator-tool , https://github.com/IHTSDO/rf2-diff-generator , https://github.com/IHTSDO/reporting-engine , https://github.com/IHTSDO/release-validation-framework , https://github.com/IHTSDO/release-notes-service
- NHS England SNOMED CT notices: https://nhsengland.kahootz.com/t_c_home/view?objectID=17185264 ; Inactives Fact Sheet: https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134407/SNOMED_CT_Inactives_Fact_sheet_v1.0.pdf
- LOINC: https://loinc.org/change-snapshot/ ; https://loinc.org/kb/release-notes-archive/2.77 ; https://loinc.org/kb/users-guide/editorial-policies-and-procedures/classification-of-loinc-term-status ; BfArM deDE: https://www.bfarm.de/EN/Code-systems/Terminologies/LOINC-UCUM/LOINC-and-RELMA/German-Translation/_node.html
- FHIR ValueSet comparison: https://build.fhir.org/ig/FHIR/fhir-tools-ig/en/valueset-comparison.html ; Ontoserver ValueSet API: https://ontoserver.csiro.au/docs/6/api-fhir-valueset.html
- VSAC Comparison Tool: https://www.nlm.nih.gov/vsac/support/usingvsac/valuesetcomparisontool.html
- OHDSI: https://github.com/ohdsi/phenotypechangesinvocabupdate ; https://github.com/mi-erasmusmc/VocabularyVersioning ; https://github.com/OHDSI/Vocabulary-v5.0/releases
- UMLS change files: https://nlm.nih.gov/research/umls/implementation_resources/query_diagrams/er7.html
- Ceusters & Bona 2016, PMC5333315; Cimino 1998 Desiderata, DOI 10.1055/s-0038-1634558
