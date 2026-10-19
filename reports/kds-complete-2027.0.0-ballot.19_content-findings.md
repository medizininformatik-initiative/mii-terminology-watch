# Content findings while baselining kds.complete 2027.0.0-ballot.19

Found by expanding every SNOMED CT / LOINC ValueSet of the package on the MII Ontoserver
(SNOMED CT International 20260701, LOINC 2.82), 2026-10-19. These are ballot-relevant defects in the
ValueSet definitions themselves, independent of any terminology release.

| Module | ValueSet | Finding | Suggested fix |
|---|---|---|---|
| icu | `mii-vs-icu-delirium-interpretation` | SNOMED include contains placeholder code `xxx` with display "No delirium (finding)"; expansion fails | replace with a real concept (e.g. a "no delirium" finding) or model absence via a separate answer |
| lungenfunktion | `mii-vs-lufu-sct-procedure` | ECL `< 251880004 122869004 \|Measurement procedure (procedure)\|` is syntactically invalid (two concept ids without operator); expansion fails | probably `< 251880004 OR < 122869004`, or `< 251880004 |Pulmonary function test| ` alone |
| kardio | `mii-vs-kardio-extended-mii-diagnosecodes-snomed`, `mii-vs-kardio-klappenvitium-snomedct` | reference a CodeSystem supplement (`valueset-supplement` extension, modul-kardio) that is not loaded on the MII Ontoserver; expansion fails unless the extension is dropped | publish the supplement to the terminology server or remove the extension from the ballot package |
| labor | `mii-vs-labor-laborbereich` | mixes LOINC with a code system not available on the server; whole-ValueSet expansion fails on the server | pin/upload the missing CodeSystem; for the watch, only SNOMED/LOINC includes are expanded |

Also observed: 108 SNOMED and 70 LOINC includes are unpinned (no `version`), while the balloted versions are
SNOMED CT International 20260701 and LOINC 2.82. See `baselines/kds-complete-2027.0.0-ballot.19/inventory.json`.
