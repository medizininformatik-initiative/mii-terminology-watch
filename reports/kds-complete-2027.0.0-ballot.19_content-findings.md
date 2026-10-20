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

Found by the SNOMED CT comparisons (20260401 / 20260901 / 20261001, 2026-10-20) as anchors that were already
broken under the baseline (`anchors_preexisting`), i.e. defects independent of the release:

| Module | ValueSet | Finding | Suggested fix |
|---|---|---|---|
| icu | `mii-vs-icu-devicemetric-extrakorporale-verfahren` | enumerated code `18274404` does not exist in SNOMED CT International (any of 20260401–20261001) | check the intended concept (typo / wrong system) |
| kardio | `mii-vs-kardio-extended-mii-diagnosecodes-snomed`, `mii-vs-kardio-klappenvitium-snomedct` | enumerated include contains the post-coordinated expression `368009:{116676008=49755003,363698007=17401000},{246112005=24484000}`; not expandable as a code | precoordinate (request a concept) or move to a supplement/extension |
| seltene | `mii-vs-seltene-genetic-basis` | `268298002`, `429252008`, `718211000119104` are unknown in the International edition (the last is a US-extension identifier); `264530000` *Hereditary disease* is inactive (Duplicate) | replace by International concepts / the SAME AS target |
| mtb | `mii-vs-mtb-tumorausbreitung` | enumerated `255127006` is inactive (Ambiguous) | pick the intended successor |
| patho | `mii-vs-patho-problem-list-snomed-ct` | is-a anchors `409586006` *Complaint* and `248536006` *Finding of functional performance and activity* are inactive (Nonconformance to editorial policy); their subtrees are empty | replace by `1269496002` (REPLACED BY) resp. drop, the content is under `404684003` already |

Also observed: 108 SNOMED and 70 LOINC includes are unpinned (no `version`), while the balloted versions are
SNOMED CT International 20260701 and LOINC 2.82. See `baselines/kds-complete-2027.0.0-ballot.19/inventory.json`.
