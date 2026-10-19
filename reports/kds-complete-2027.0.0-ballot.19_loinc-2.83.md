# Terminology release impact: de.medizininformatikinitiative.kerndatensatz.complete 2027.0.0-ballot.19

| | Baseline | Target |
|---|---|---|
| LOINC | 2.82 | 2.83 |
| SNOMED CT | 20260701 | 20260701 |

Generated 2026-10-19T02:16:19 against https://ontoserver.mii-termserv.de/fhir (570 server calls).

## Summary

| Severity | ValueSets |
|---|---:|
| BREAKING | 2 |
| SIGNIFICANT | 5 |
| MINOR | 0 |
| NONE | 79 |

Severity rules: BREAKING = a member of an enumerated include or a filter anchor was inactivated, or a member became inactive; SIGNIFICANT = members dropped out of a filter-defined ValueSet or displays changed; MINOR = new members only.

Pinned ValueSets (all includes carry a version) do not change at runtime until the pin is moved; unpinned ones change with the next terminology load on the server.

## Per module

| Module | ValueSets compared | BREAKING | SIGNIFICANT | MINOR | unchanged |
|---|---:|---:|---:|---:|---:|
| bildgebung | 2 | 0 | 1 | 0 | 1 |
| icu | 10 | 0 | 0 | 0 | 10 |
| labor | 2 | 1 | 0 | 0 | 1 |
| lungenfunktion | 20 | 0 | 0 | 0 | 20 |
| mikrobio | 18 | 0 | 2 | 0 | 16 |
| mtb | 3 | 0 | 0 | 0 | 3 |
| onko | 13 | 0 | 0 | 0 | 13 |
| patho | 4 | 1 | 1 | 0 | 2 |
| pro | 5 | 0 | 0 | 0 | 5 |
| seltene | 9 | 0 | 1 | 0 | 8 |

## Module `bildgebung`

### SIGNIFICANT · `mii-vs-bildgebung-diagnostic-report-code-lnc` (UNPINNED, filter)

MII VS Bildgebung DiagnosticReport Code Loinc  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/ValueSet/mii-vs-bildgebung-diagnostic-report-code-lnc`  
Members: 7222 → 7228


**Display changed:**

| Code | Old | New |
|---|---|---|
| `106814-7` | RF Guidance for Guidance of Stomach | RF Guidance of Stomach |
| `106815-4` | RF Guidance for Guidance of Ankle - left | RF Guidance of Ankle - left |
| `106816-2` | RF Guidance for Guidance of Ankle - right | RF Guidance of Ankle - right |
| `106817-0` | RF Guidance for Guidance of Lower extremity - left | RF Guidance of Lower extremity - left |
| `106818-8` | RF Guidance for Guidance of Lower extremity - right | RF Guidance of Lower extremity - right |
| `106819-6` | RFA Guidance for Guidance of Vessel | RFA Guidance of Vessel |
| `106820-4` | RF Guidance for Guidance of Sinuses | RF Guidance of Sinuses |
| `106821-2` | RF Guidance for Guidance of Skull | RF Guidance of Skull |
| `107418-6` | US Guidance for radioactive seed localization of Breast - left | Guidance for placement of magnetic seeds in Breast - left |
| `107419-4` | US Guidance for radioactive seed localization of Axilla - bilateral | US Guidance for Guidance for placement of magnetic seeds in Axilla - bilateral |

**New members (6):**

| Code | Display |
|---|---|
| `107289-1` | RF Guidance for insertion of dialysis catheter of Peritoneal space |
| `107438-4` | RF Guidance for Guidance for percutaneous retrograde balloon embolization of gastric vein |
| `113116-8` | XR Ankle+Foot - bilateral Views |
| `115584-5` | NM Prostate Views |
| `115585-2` | XR Teeth Views |
| `115638-9` | CT Kidney and Ureter and Urinary bladder WO contrast IV |

## Module `labor`

### BREAKING · `mii-vs-labor-order-codes` (pinned, filter)

MII VS Labor Order Codes  
`https://www.medizininformatik-initiative.de/fhir/core/modul-labor/ValueSet/ValueSetOrderCodes`  
Members: 59035 → 61770


**Members now inactive (stop using):**

| Code | Display | Status / successor |
|---|---|---|
| `105085-5` | Deprecated Neisseria gonorrhoeae rRNA [Presence] in Specimen by Molecular genetics | DEPRECATED |
| `107370-9` | Deprecated Burst forming unit erythroid [#/area] in Plasma | DEPRECATED |
| `107371-7` | Deprecated Common myeloid progenitor cell [#/area] in Plasma | DEPRECATED |
| `108067-0` | Deprecated Chick Pea IgG Ab [Units/volume] in Serum or Plasma by Immunoassay | DEPRECATED |
| `42493-7` | Deprecated Catecholamines Free fractionated [Mass/volume] in Plasma | DEPRECATED |
| `87505-4` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87506-2` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Expired - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87507-0` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Planned Discharge - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87508-8` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Unplanned Discharge - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87509-6` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Admission - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `89963-3` | Deprecated Inpatient Rehabilitation Facility - Patient Assessment Instrument (IRF-PAI) - version 3.0 during assessment period [CMS Assessment] | DEPRECATED |

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `67579-3` | At any time in your life, have you ever been unfairly fired | status ACTIVE | - |
| `67581-9` | For unfair reasons, have you ever not been hired for a job | status ACTIVE | - |
| `67582-7` | Have you ever been unfairly denied a promotion | status ACTIVE | - |
| `67583-5` | Have you ever been unfairly stopped, searched, questioned, physically threatened or abused by the police | status ACTIVE | - |
| `67584-3` | Have you ever been unfairly denied a bank loan | status ACTIVE | - |
| `67585-0` | Have you ever received service from someone such as a plumber or car mechanic that was worse than what other people get | status ACTIVE | - |
| `67671-8` | Have you ever been unfairly discouraged by a teacher or advisor from continuing your education | status ACTIVE | - |
| `67672-6` | Have you ever been unfairly prevented from moving into a neighborhood because the landlord or a realtor refused to sell or rent you a house or apartment | status ACTIVE | - |
| `67673-4` | Have you ever moved into a neighborhood where neighbors made life difficult for you or your family | status ACTIVE | - |

**New members (2744):**

| Code | Display |
|---|---|
| `104622-6` | Chronic pain and high impact chronic pain [HICP] |
| `105306-5` | Parenting stress questionnaire OBVL-K |
| `105451-9` | Parenting stress questionnaire OBVL |
| `106879-0` | PROMIS Pediatric Item Bank - Gen Pop v3.0 - Anxiety Short Form 8a |
| `106931-9` | Extended hurt, insulted, threaten, scream [E-HITS] |
| `106966-5` | Revised trauma score RTS |
| `106970-7` | PROMIS Scale v1.2 - Global Physical Health 4a |
| `107289-1` | RF Guidance for insertion of dialysis catheter of Peritoneal space |
| `107438-4` | RF Guidance for Guidance for percutaneous retrograde balloon embolization of gastric vein |
| `111513-8` | Klebsiella pneumoniae+Klebsiella variicola+Klebsiella quasipneumoniae DNA [NCncRange] in Bronchoalveolar aspirate by NAA with non-probe detection |
| `111514-6` | Microscopic observation [Identifier] in Fistula by Gram stain |
| `111515-3` | Fungus identified in Prostatic fluid by Culture |
| `111533-6` | Specimen Count [#] by calculation |
| `111534-4` | BVA Panel |
| `112279-5` | Respiratory pathogens 5-plexA DNA and RNA panel - Nasopharynx by NAA with non-probe detection |
| `112337-1` | California serogroup IgM Ab [Titer] in Serum by Immunofluorescence |
| `112338-9` | Arbovirus IgM panel - Serum by Immunofluorescence |
| `112449-4` | Chimerism post transplant panel without cell selection - Specimen |
| `112460-1` | Chimerism post transplant cell selection panel - Specimen |
| `112588-9` | Birth Notification Note |
| `112589-7` | Newborn Discharge Summary Note |
| `112590-5` | Postpartum Summary Note |
| `112592-1` | Creatinine [Moles/volume] in Urine by Automated test strip |
| `112593-9` | Creatinine [Mass/volume] in Urine by Automated test strip |
| `112595-4` | Albumin [Mass/volume] in Urine by Automated test strip |
| `112598-8` | Borrelia burgdorferi IgM Ab [Presence] in Serum or Plasma by IA.STTT |
| `112599-6` | Borrelia burgdorferi IgG Ab [Presence] in Serum or Plasma by IA.STTT |
| `112613-5` | Expanded Food Security Screener [FSS-Exp] |
| `112614-3` | Neurofilament light chain [Moles/volume] in Plasma by Immunoassay |
| `112615-0` | Guselkumab Ab [Mass/volume] in Serum or Plasma by Immunoassay |
| `112616-8` | Guselkumab Ab Panel - Serum or Plasma |
| `112617-6` | Plasma cells assessment in Blood Narrative |
| `112618-4` | Abnormal plasma cells [#] in Blood by Flow cytometry (FC) |
| `112619-2` | Total plasma cells counted [#] in Blood by Flow cytometry (FC) |
| `112620-0` | Cells Counted Total [#] in Blood by Flow cytometry (FC) |
| `112622-6` | Polyclonal plasma cells [#] in Blood by Flow cytometry (FC) |
| `112623-4` | Polyclonal plasma cells/Cells counted in Blood by Flow cytometry (FC) |
| `112624-2` | Plasma cells assessment panel - Blood by Flow cytometry (FC) |
| `112626-7` | Liver Transplant intraoperative panel - Specimen |
| `112627-5` | Abnormal plasma cells/Cells counted in Blood by Flow cytometry (FC) |

… 2704 more, see the CSV.

## Module `mikrobio`

### SIGNIFICANT · `mii-vs-mikrobio-spezifische-mikroskopie-tests-loinc` (pinned, filter)

MII VS Mikrobio Spezifische Mikroskopie Tests [LOINC]  
`https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-spezifische-mikroskopie-tests-loinc`  
Members: 23 → 71


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `107527-4` | Clue cells [Presence] in Vaginal fluid by Gram stain | status ACTIVE | - |

**Display changed:**

| Code | Old | New |
|---|---|---|
| `88113-6` | Erythrocytes [Presence] in Cerebral spinal fluid by Gram stain | Erythrocytes [Presence] in Cerebrospinal Fluid by Gram stain |
| `88114-4` | Leukocytes [Presence] in Cerebral spinal fluid by Gram stain | Leukocytes [Presence] in Cerebrospinal Fluid by Gram stain |

**New members (49):**

| Code | Display |
|---|---|
| `113024-4` | Yeast [Presence] in Urethra by Gram stain |
| `113025-1` | Gram negative bacteria [Presence] in Urethra by Gram stain |
| `113026-9` | Gram negative bacilli [Presence] in Urethra by Gram stain |
| `113027-7` | Gram positive bacilli [Presence] in Urethra by Gram stain |
| `113028-5` | Gram positive bacteria [Presence] in Urethra by Gram stain |
| `113029-3` | Gram negative bacteria [Presence] in Bronchoalveolar lavage by Gram stain |
| `113030-1` | Gram negative bacilli [Presence] in Bronchoalveolar lavage by Gram stain |
| `113031-9` | Gram positive bacilli [Presence] in Bronchoalveolar lavage by Gram stain |
| `113032-7` | Gram positive bacteria [Presence] in Bronchoalveolar lavage by Gram stain |
| `113034-3` | Gram negative bacteria [Presence] in Synovial fluid by Gram stain |
| `113035-0` | Gram negative bacilli [Presence] in Synovial fluid by Gram stain |
| `113036-8` | Gram positive bacilli [Presence] in Synovial fluid by Gram stain |
| `113038-4` | Mobiluncus sp [Presence] in Vaginal fluid by Gram stain |
| `113039-2` | Gram negative bacteria [Presence] in Vaginal fluid by Gram stain |
| `113040-0` | Gram negative bacilli [Presence] in Vaginal fluid by Gram stain |
| `113041-8` | Gram positive bacilli [Presence] in Vaginal fluid by Gram stain |
| `113042-6` | Gram positive bacteria [Presence] in Vaginal fluid by Gram stain |
| `113045-9` | Yeast [Presence] in Pleural fluid by Gram stain |
| `113053-3` | Yeast [Presence] in Peritoneal fluid by Gram stain |
| `113058-2` | Leukocytes [Presence] in Peritoneal fluid by Gram stain |
| `113059-0` | Gram positive bacteria [Presence] in Sputum by Gram stain |
| `113060-8` | Yeast [Presence] in Bronchoalveolar aspirate by Gram stain |
| `113061-6` | Gram negative bacteria [Presence] in Bronchoalveolar aspirate by Gram stain |
| `113062-4` | Gram negative bacilli [Presence] in Bronchoalveolar aspirate by Gram stain |
| `113063-2` | Gram positive bacilli [Presence] in Bronchoalveolar aspirate by Gram stain |
| `113064-0` | Gram positive bacteria [Presence] in Bronchoalveolar aspirate by Gram stain |
| `113065-7` | Gram negative bacilli [Presence] in Pericardial fluid by Gram stain |
| `113066-5` | Gram positive bacilli [Presence] in Pericardial fluid by Gram stain |
| `113067-3` | Gram negative bacteria [Presence] in Pericardial fluid by Gram stain |
| `113068-1` | Gram negative bacteria [Presence] in Wound shallow by Gram stain |
| `113069-9` | Gram negative bacilli [Presence] in Wound shallow by Gram stain |
| `113070-7` | Gram positive bacilli [Presence] in Wound shallow by Gram stain |
| `113071-5` | Yeast [Presence] in Tissue by Gram stain |
| `113072-3` | Gram negative bacteria [Presence] in Tissue by Gram stain |
| `113073-1` | Gram negative bacilli [Presence] in Tissue by Gram stain |
| `113074-9` | Gram positive bacilli [Presence] in Tissue by Gram stain |
| `113075-6` | Gram positive bacteria [Presence] in Tissue by Gram stain |
| `113078-0` | Gram negative bacteria [Presence] in Aspirate by Gram stain |
| `113079-8` | Gram negative bacilli [Presence] in Aspirate by Gram stain |
| `113080-6` | Gram positive bacilli [Presence] in Aspirate by Gram stain |

… 9 more, see the CSV.

### SIGNIFICANT · `mii-vs-mikrobio-virulenz-loinc` (pinned, enumerated)

MII VS Mikrobio Virulenz [LOINC]  
`https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-virulenz-loinc`  
Members: 61 → 61


**Display changed:**

| Code | Old | New |
|---|---|---|
| `87380-2` | Escherichia coli Stx2e-Toxin stx2e-Gen [Nachweis] in Isolat mittels Nukleinsäureamplifikation mit Sondendetektion | Escherichia coli Stx2e toxin stx2e gene [Presence] in Isolate by NAA with probe detection |

## Module `patho`

### BREAKING · `mii-vs-patho-all-loinc` (UNPINNED, whole-system)

MII VS Patho All [LOINC]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-all-loinc`  
Members: 252210 → 257269


**Members now inactive (stop using):**

| Code | Display | Status / successor |
|---|---|---|
| `105085-5` | Deprecated Neisseria gonorrhoeae rRNA [Presence] in Specimen by Molecular genetics | DEPRECATED |
| `105445-1` | Deprecated T-score 65-69 = borderline clinical range | DEPRECATED |
| `107370-9` | Deprecated Burst forming unit erythroid [#/area] in Plasma | DEPRECATED |
| `107371-7` | Deprecated Common myeloid progenitor cell [#/area] in Plasma | DEPRECATED |
| `108067-0` | Deprecated Chick Pea IgG Ab [Units/volume] in Serum or Plasma by Immunoassay | DEPRECATED |
| `1385-4` | Deprecated Catecholamines Free fractionated [Mass/volume] in Plasma --1 hour post 300 ug cloNIDine PO | DEPRECATED |
| `1386-2` | Deprecated Catecholamines Free fractionated [Mass/volume] in Plasma --2 hours post 300 ug cloNIDine PO | DEPRECATED |
| `1387-0` | Deprecated Catecholamines Free fractionated [Mass/volume] in Plasma --3 hours post 300 ug cloNIDine PO | DEPRECATED |
| `1388-8` | Deprecated Catecholamines Free fractionated [Mass/volume] in Plasma --pre 300 ug cloNIDine PO | DEPRECATED |
| `21000-5` | Deprecated Erythrocyte distribution width [Entitic volume] by Automated count | DEPRECATED |
| `42493-7` | Deprecated Catecholamines Free fractionated [Mass/volume] in Plasma | DEPRECATED |
| `87505-4` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87506-2` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Expired - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87507-0` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Planned Discharge - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87508-8` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Unplanned Discharge - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `87509-6` | Deprecated Long-Term Care Hospital (LTCH) Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) - Admission - version 4.00 during assessment period [CMS Assessment] | DEPRECATED |
| `89963-3` | Deprecated Inpatient Rehabilitation Facility - Patient Assessment Instrument (IRF-PAI) - version 3.0 during assessment period [CMS Assessment] | DEPRECATED |

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `LA30356-2` |  | no longer in filter / unknown | - |
| `LA30984-1` |  | no longer in filter / unknown | - |
| `LL6913-9` |  | no longer in filter / unknown | - |
| `LL6942-8` |  | no longer in filter / unknown | - |
| `LL6943-6` |  | no longer in filter / unknown | - |
| `LP112581-6` |  | no longer in filter / unknown | - |
| `LP173213-2` |  | no longer in filter / unknown | - |
| `LP227533-9` |  | no longer in filter / unknown | - |
| `LP227551-1` |  | no longer in filter / unknown | - |
| `LP227569-3` |  | no longer in filter / unknown | - |
| `LP227570-1` |  | no longer in filter / unknown | - |
| `LP227571-9` |  | no longer in filter / unknown | - |
| `LP227586-7` |  | no longer in filter / unknown | - |
| `LP227591-7` |  | no longer in filter / unknown | - |
| `LP227638-6` |  | no longer in filter / unknown | - |
| `LP227648-5` |  | no longer in filter / unknown | - |
| `LP227658-4` |  | no longer in filter / unknown | - |
| `LP227659-2` |  | no longer in filter / unknown | - |
| `LP227660-0` |  | no longer in filter / unknown | - |
| `LP227676-6` |  | no longer in filter / unknown | - |
| `LP227687-3` |  | no longer in filter / unknown | - |
| `LP227715-2` |  | no longer in filter / unknown | - |
| `LP227717-8` |  | no longer in filter / unknown | - |
| `LP227726-9` |  | no longer in filter / unknown | - |
| `LP227747-5` |  | no longer in filter / unknown | - |
| `LP227749-1` |  | no longer in filter / unknown | - |
| `LP227828-3` |  | no longer in filter / unknown | - |
| `LP227842-4` |  | no longer in filter / unknown | - |
| `LP227858-0` |  | no longer in filter / unknown | - |
| `LP227859-8` |  | no longer in filter / unknown | - |
| `LP227906-7` |  | no longer in filter / unknown | - |
| `LP227919-0` |  | no longer in filter / unknown | - |
| `LP227921-6` |  | no longer in filter / unknown | - |
| `LP227923-2` |  | no longer in filter / unknown | - |
| `LP227925-7` |  | no longer in filter / unknown | - |
| `LP227932-3` |  | no longer in filter / unknown | - |
| `LP227935-6` |  | no longer in filter / unknown | - |
| `LP227956-2` |  | no longer in filter / unknown | - |
| `LP227960-4` |  | no longer in filter / unknown | - |
| `LP228058-6` |  | no longer in filter / unknown | - |
| `LP228087-5` |  | no longer in filter / unknown | - |
| `LP228089-1` |  | no longer in filter / unknown | - |
| `LP228120-4` |  | no longer in filter / unknown | - |
| `LP228133-7` |  | no longer in filter / unknown | - |
| `LP228135-2` |  | no longer in filter / unknown | - |
| `LP228136-0` |  | no longer in filter / unknown | - |
| `LP228179-0` |  | no longer in filter / unknown | - |
| `LP228181-6` |  | no longer in filter / unknown | - |
| `LP228182-4` |  | no longer in filter / unknown | - |
| `LP228229-3` |  | no longer in filter / unknown | - |
| `LP228244-2` |  | no longer in filter / unknown | - |
| `LP228294-7` |  | no longer in filter / unknown | - |
| `LP228299-6` |  | no longer in filter / unknown | - |
| `LP228300-2` |  | no longer in filter / unknown | - |
| `LP228332-5` |  | no longer in filter / unknown | - |
| `LP228342-4` |  | no longer in filter / unknown | - |
| `LP228358-0` |  | no longer in filter / unknown | - |
| `LP228359-8` |  | no longer in filter / unknown | - |
| `LP228391-1` |  | no longer in filter / unknown | - |
| `LP228393-7` |  | no longer in filter / unknown | - |
| `LP228395-2` |  | no longer in filter / unknown | - |
| `LP228399-4` |  | no longer in filter / unknown | - |
| `LP228402-6` |  | no longer in filter / unknown | - |
| `LP228417-4` |  | no longer in filter / unknown | - |
| `LP228418-2` |  | no longer in filter / unknown | - |
| `LP228424-0` |  | no longer in filter / unknown | - |
| `LP228427-3` |  | no longer in filter / unknown | - |
| `LP228430-7` |  | no longer in filter / unknown | - |
| `LP228437-2` |  | no longer in filter / unknown | - |
| `LP228445-5` |  | no longer in filter / unknown | - |
| `LP228480-2` |  | no longer in filter / unknown | - |
| `LP228481-0` |  | no longer in filter / unknown | - |
| `LP228491-9` |  | no longer in filter / unknown | - |
| `LP228518-9` |  | no longer in filter / unknown | - |
| `LP228520-5` |  | no longer in filter / unknown | - |
| `LP228522-1` |  | no longer in filter / unknown | - |
| `LP228539-5` |  | no longer in filter / unknown | - |
| `LP228564-3` |  | no longer in filter / unknown | - |
| `LP228571-8` |  | no longer in filter / unknown | - |
| `LP228583-3` |  | no longer in filter / unknown | - |
| `LP228612-0` |  | no longer in filter / unknown | - |
| `LP228644-3` |  | no longer in filter / unknown | - |
| `LP228680-7` |  | no longer in filter / unknown | - |
| `LP228686-4` |  | no longer in filter / unknown | - |
| `LP228702-9` |  | no longer in filter / unknown | - |
| `LP228708-6` |  | no longer in filter / unknown | - |
| `LP228736-7` |  | no longer in filter / unknown | - |
| `LP228738-3` |  | no longer in filter / unknown | - |
| `LP228778-9` |  | no longer in filter / unknown | - |
| `LP228787-0` |  | no longer in filter / unknown | - |
| `LP228793-8` |  | no longer in filter / unknown | - |
| `LP228794-6` |  | no longer in filter / unknown | - |
| `LP228801-9` |  | no longer in filter / unknown | - |
| `LP228802-7` |  | no longer in filter / unknown | - |
| `LP228805-0` |  | no longer in filter / unknown | - |
| `LP228809-2` |  | no longer in filter / unknown | - |
| `LP228856-3` |  | no longer in filter / unknown | - |
| `LP228889-4` |  | no longer in filter / unknown | - |
| `LP228947-0` |  | no longer in filter / unknown | - |
| `LP228948-8` |  | no longer in filter / unknown | - |
| `LP229046-0` |  | no longer in filter / unknown | - |
| `LP229048-6` |  | no longer in filter / unknown | - |
| `LP229070-0` |  | no longer in filter / unknown | - |
| `LP229073-4` |  | no longer in filter / unknown | - |
| `LP229076-7` |  | no longer in filter / unknown | - |
| `LP229081-7` |  | no longer in filter / unknown | - |
| `LP229091-6` |  | no longer in filter / unknown | - |
| `LP229093-2` |  | no longer in filter / unknown | - |
| `LP229102-1` |  | no longer in filter / unknown | - |
| `LP229103-9` |  | no longer in filter / unknown | - |
| `LP229107-0` |  | no longer in filter / unknown | - |
| `LP229126-0` |  | no longer in filter / unknown | - |
| `LP229129-4` |  | no longer in filter / unknown | - |
| `LP229134-4` |  | no longer in filter / unknown | - |
| `LP229136-9` |  | no longer in filter / unknown | - |
| `LP229208-6` |  | no longer in filter / unknown | - |
| `LP229224-3` |  | no longer in filter / unknown | - |
| `LP229225-0` |  | no longer in filter / unknown | - |
| `LP229314-2` |  | no longer in filter / unknown | - |
| `LP229332-4` |  | no longer in filter / unknown | - |
| `LP229353-0` |  | no longer in filter / unknown | - |
| `LP229357-1` |  | no longer in filter / unknown | - |
| `LP229365-4` |  | no longer in filter / unknown | - |
| `LP229400-9` |  | no longer in filter / unknown | - |
| `LP229411-6` |  | no longer in filter / unknown | - |
| `LP229430-6` |  | no longer in filter / unknown | - |
| `LP229432-2` |  | no longer in filter / unknown | - |
| `LP229434-8` |  | no longer in filter / unknown | - |
| `LP229526-1` |  | no longer in filter / unknown | - |
| `LP229559-2` |  | no longer in filter / unknown | - |
| `LP229587-3` |  | no longer in filter / unknown | - |
| `LP229604-6` |  | no longer in filter / unknown | - |
| `LP229609-5` |  | no longer in filter / unknown | - |
| `LP229616-0` |  | no longer in filter / unknown | - |
| `LP229624-4` |  | no longer in filter / unknown | - |
| `LP229633-5` |  | no longer in filter / unknown | - |
| `LP229645-9` |  | no longer in filter / unknown | - |
| `LP229661-6` |  | no longer in filter / unknown | - |
| `LP229664-0` |  | no longer in filter / unknown | - |
| `LP229667-3` |  | no longer in filter / unknown | - |
| `LP229673-1` |  | no longer in filter / unknown | - |
| `LP229682-2` |  | no longer in filter / unknown | - |
| `LP229780-4` |  | no longer in filter / unknown | - |
| `LP229786-1` |  | no longer in filter / unknown | - |
| `LP229806-7` |  | no longer in filter / unknown | - |
| `LP229817-4` |  | no longer in filter / unknown | - |
| `LP229826-5` |  | no longer in filter / unknown | - |
| `LP229827-3` |  | no longer in filter / unknown | - |
| `LP229833-1` |  | no longer in filter / unknown | - |
| `LP229864-6` |  | no longer in filter / unknown | - |
| `LP229866-1` |  | no longer in filter / unknown | - |
| `LP229880-2` |  | no longer in filter / unknown | - |
| `LP229883-6` |  | no longer in filter / unknown | - |
| `LP229889-3` |  | no longer in filter / unknown | - |
| `LP229904-0` |  | no longer in filter / unknown | - |
| `LP229934-7` |  | no longer in filter / unknown | - |
| `LP229948-7` |  | no longer in filter / unknown | - |
| `LP229960-2` |  | no longer in filter / unknown | - |
| `LP265806-2` |  | no longer in filter / unknown | - |
| `LP266134-8` |  | no longer in filter / unknown | - |
| `LP281344-4` |  | no longer in filter / unknown | - |
| `LP281345-1` |  | no longer in filter / unknown | - |
| `LP281346-9` |  | no longer in filter / unknown | - |
| `LP281347-7` |  | no longer in filter / unknown | - |
| `LP281348-5` |  | no longer in filter / unknown | - |
| `LP281349-3` |  | no longer in filter / unknown | - |
| `LP281350-1` |  | no longer in filter / unknown | - |
| `LP281351-9` |  | no longer in filter / unknown | - |
| `LP285006-5` |  | no longer in filter / unknown | - |
| `LP310191-4` |  | no longer in filter / unknown | - |
| `LP310192-2` |  | no longer in filter / unknown | - |
| `LP310193-0` |  | no longer in filter / unknown | - |
| `LP310194-8` |  | no longer in filter / unknown | - |
| `LP310195-5` |  | no longer in filter / unknown | - |
| `LP310196-3` |  | no longer in filter / unknown | - |
| `LP310197-1` |  | no longer in filter / unknown | - |
| `LP310198-9` |  | no longer in filter / unknown | - |
| `LP310199-7` |  | no longer in filter / unknown | - |
| `LP310200-3` |  | no longer in filter / unknown | - |
| `LP310201-1` |  | no longer in filter / unknown | - |
| `LP310230-0` |  | no longer in filter / unknown | - |
| `LP310233-4` |  | no longer in filter / unknown | - |
| `LP310234-2` |  | no longer in filter / unknown | - |
| `LP310235-9` |  | no longer in filter / unknown | - |
| `LP310236-7` |  | no longer in filter / unknown | - |
| `LP310237-5` |  | no longer in filter / unknown | - |
| `LP380837-7` |  | no longer in filter / unknown | - |
| `LP393195-5` |  | no longer in filter / unknown | - |
| `LP401685-5` |  | no longer in filter / unknown | - |
| `LP401694-7` |  | no longer in filter / unknown | - |
| `LP401695-4` |  | no longer in filter / unknown | - |
| `LP401729-1` |  | no longer in filter / unknown | - |
| `LP409325-0` |  | no longer in filter / unknown | - |
| `LP409334-2` |  | no longer in filter / unknown | - |
| `LP409346-6` |  | no longer in filter / unknown | - |
| `LP409347-4` |  | no longer in filter / unknown | - |
| `LP409348-2` |  | no longer in filter / unknown | - |
| `LP409351-6` |  | no longer in filter / unknown | - |
| `LP409354-0` |  | no longer in filter / unknown | - |
| `LP409357-3` |  | no longer in filter / unknown | - |
| `LP409362-3` |  | no longer in filter / unknown | - |
| `LP409364-9` |  | no longer in filter / unknown | - |
| `LP409365-6` |  | no longer in filter / unknown | - |
| `LP409366-4` |  | no longer in filter / unknown | - |
| `LP409373-0` |  | no longer in filter / unknown | - |
| `LP409378-9` |  | no longer in filter / unknown | - |
| `LP409380-5` |  | no longer in filter / unknown | - |
| `LP409390-4` |  | no longer in filter / unknown | - |
| `LP409395-3` |  | no longer in filter / unknown | - |
| `LP409410-0` |  | no longer in filter / unknown | - |
| `LP409414-2` |  | no longer in filter / unknown | - |
| `LP409418-3` |  | no longer in filter / unknown | - |
| `LP409430-8` |  | no longer in filter / unknown | - |
| `LP409433-2` |  | no longer in filter / unknown | - |
| `LP409440-7` |  | no longer in filter / unknown | - |
| `LP409450-6` |  | no longer in filter / unknown | - |
| `LP409452-2` |  | no longer in filter / unknown | - |
| `LP409457-1` |  | no longer in filter / unknown | - |
| `LP409465-4` |  | no longer in filter / unknown | - |
| `LP409467-0` |  | no longer in filter / unknown | - |
| `LP409471-2` |  | no longer in filter / unknown | - |
| `LP409472-0` |  | no longer in filter / unknown | - |
| `LP409479-5` |  | no longer in filter / unknown | - |
| `LP409482-9` |  | no longer in filter / unknown | - |
| `LP409486-0` |  | no longer in filter / unknown | - |
| `LP409508-1` |  | no longer in filter / unknown | - |
| `LP409512-3` |  | no longer in filter / unknown | - |
| `LP409519-8` |  | no longer in filter / unknown | - |
| `LP409531-3` |  | no longer in filter / unknown | - |
| `LP409532-1` |  | no longer in filter / unknown | - |
| `LP409536-2` |  | no longer in filter / unknown | - |
| `LP409537-0` |  | no longer in filter / unknown | - |
| `LP409538-8` |  | no longer in filter / unknown | - |
| `LP409540-4` |  | no longer in filter / unknown | - |
| `LP409548-7` |  | no longer in filter / unknown | - |
| `LP409555-2` |  | no longer in filter / unknown | - |
| `LP409556-0` |  | no longer in filter / unknown | - |
| `LP409558-6` |  | no longer in filter / unknown | - |
| `LP409564-4` |  | no longer in filter / unknown | - |
| `LP409579-2` |  | no longer in filter / unknown | - |
| `LP409586-7` |  | no longer in filter / unknown | - |
| `LP409613-9` |  | no longer in filter / unknown | - |
| `LP409624-6` |  | no longer in filter / unknown | - |
| `LP409627-9` |  | no longer in filter / unknown | - |
| `LP409629-5` |  | no longer in filter / unknown | - |
| `LP409630-3` |  | no longer in filter / unknown | - |
| `LP409645-1` |  | no longer in filter / unknown | - |
| `LP409648-5` |  | no longer in filter / unknown | - |
| `LP409653-5` |  | no longer in filter / unknown | - |
| `LP409654-3` |  | no longer in filter / unknown | - |
| `LP409660-0` |  | no longer in filter / unknown | - |
| `LP409665-9` |  | no longer in filter / unknown | - |
| `LP409667-5` |  | no longer in filter / unknown | - |
| `LP409669-1` |  | no longer in filter / unknown | - |
| `LP409674-1` |  | no longer in filter / unknown | - |
| `LP409685-7` |  | no longer in filter / unknown | - |
| `LP409686-5` |  | no longer in filter / unknown | - |
| `LP409687-3` |  | no longer in filter / unknown | - |
| `LP409691-5` |  | no longer in filter / unknown | - |
| `LP409694-9` |  | no longer in filter / unknown | - |
| `LP409703-8` |  | no longer in filter / unknown | - |
| `LP409708-7` |  | no longer in filter / unknown | - |
| `LP409730-1` |  | no longer in filter / unknown | - |
| `LP409731-9` |  | no longer in filter / unknown | - |
| `LP409733-5` |  | no longer in filter / unknown | - |
| `LP409742-6` |  | no longer in filter / unknown | - |
| `LP409745-9` |  | no longer in filter / unknown | - |
| `LP409746-7` |  | no longer in filter / unknown | - |
| `LP409749-1` |  | no longer in filter / unknown | - |
| `LP409766-5` |  | no longer in filter / unknown | - |
| `LP409782-2` |  | no longer in filter / unknown | - |
| `LP409786-3` |  | no longer in filter / unknown | - |
| `LP409793-9` |  | no longer in filter / unknown | - |
| `LP409838-2` |  | no longer in filter / unknown | - |
| `LP409840-8` |  | no longer in filter / unknown | - |
| `LP409847-3` |  | no longer in filter / unknown | - |
| `LP409850-7` |  | no longer in filter / unknown | - |
| `LP409862-2` |  | no longer in filter / unknown | - |
| `LP409865-5` |  | no longer in filter / unknown | - |
| `LP409876-2` |  | no longer in filter / unknown | - |
| `LP409879-6` |  | no longer in filter / unknown | - |
| `LP409881-2` |  | no longer in filter / unknown | - |
| `LP409897-8` |  | no longer in filter / unknown | - |
| `LP409901-8` |  | no longer in filter / unknown | - |
| `LP409907-5` |  | no longer in filter / unknown | - |
| `LP409908-3` |  | no longer in filter / unknown | - |
| `LP409913-3` |  | no longer in filter / unknown | - |
| `LP409916-6` |  | no longer in filter / unknown | - |
| `LP409917-4` |  | no longer in filter / unknown | - |
| `LP409919-0` |  | no longer in filter / unknown | - |
| `LP409931-5` |  | no longer in filter / unknown | - |
| `LP409939-8` |  | no longer in filter / unknown | - |
| `LP409951-3` |  | no longer in filter / unknown | - |
| `LP409952-1` |  | no longer in filter / unknown | - |
| `LP410029-5` |  | no longer in filter / unknown | - |
| `LP410031-1` |  | no longer in filter / unknown | - |
| `LP410035-2` |  | no longer in filter / unknown | - |
| `LP410039-4` |  | no longer in filter / unknown | - |
| `LP410041-0` |  | no longer in filter / unknown | - |
| `LP410043-6` |  | no longer in filter / unknown | - |
| `LP410047-7` |  | no longer in filter / unknown | - |
| `LP410049-3` |  | no longer in filter / unknown | - |
| `LP410054-3` |  | no longer in filter / unknown | - |
| `LP410055-0` |  | no longer in filter / unknown | - |
| `LP410057-6` |  | no longer in filter / unknown | - |
| `LP410059-2` |  | no longer in filter / unknown | - |
| `LP410076-6` |  | no longer in filter / unknown | - |
| `LP410077-4` |  | no longer in filter / unknown | - |
| `LP410079-0` |  | no longer in filter / unknown | - |
| `LP410080-8` |  | no longer in filter / unknown | - |
| `LP410081-6` |  | no longer in filter / unknown | - |
| `LP410084-0` |  | no longer in filter / unknown | - |
| `LP410090-7` |  | no longer in filter / unknown | - |
| `LP410097-2` |  | no longer in filter / unknown | - |
| `LP410104-6` |  | no longer in filter / unknown | - |
| `LP410105-3` |  | no longer in filter / unknown | - |
| `LP410122-8` |  | no longer in filter / unknown | - |
| `LP410124-4` |  | no longer in filter / unknown | - |
| `LP410128-5` |  | no longer in filter / unknown | - |
| `LP410130-1` |  | no longer in filter / unknown | - |
| `LP410133-5` |  | no longer in filter / unknown | - |
| `LP410136-8` |  | no longer in filter / unknown | - |
| `LP410148-3` |  | no longer in filter / unknown | - |
| `LP410151-7` |  | no longer in filter / unknown | - |
| `LP410153-3` |  | no longer in filter / unknown | - |
| `LP410155-8` |  | no longer in filter / unknown | - |
| `LP410158-2` |  | no longer in filter / unknown | - |
| `LP410161-6` |  | no longer in filter / unknown | - |
| `LP410167-3` |  | no longer in filter / unknown | - |
| `LP410190-5` |  | no longer in filter / unknown | - |
| `LP410201-0` |  | no longer in filter / unknown | - |
| `LP410212-7` |  | no longer in filter / unknown | - |
| `LP410230-9` |  | no longer in filter / unknown | - |
| `LP410243-2` |  | no longer in filter / unknown | - |
| `LP410244-0` |  | no longer in filter / unknown | - |
| `LP410248-1` |  | no longer in filter / unknown | - |
| `LP410264-8` |  | no longer in filter / unknown | - |
| `LP410275-4` |  | no longer in filter / unknown | - |
| `LP410280-4` |  | no longer in filter / unknown | - |
| `LP410284-6` |  | no longer in filter / unknown | - |
| `LP410285-3` |  | no longer in filter / unknown | - |
| `LP410288-7` |  | no longer in filter / unknown | - |
| `LP410297-8` |  | no longer in filter / unknown | - |
| `LP410299-4` |  | no longer in filter / unknown | - |
| `LP410319-0` |  | no longer in filter / unknown | - |
| `LP410323-2` |  | no longer in filter / unknown | - |
| `LP410328-1` |  | no longer in filter / unknown | - |
| `LP410329-9` |  | no longer in filter / unknown | - |
| `LP410338-0` |  | no longer in filter / unknown | - |
| `LP410343-0` |  | no longer in filter / unknown | - |
| `LP410345-5` |  | no longer in filter / unknown | - |
| `LP410354-7` |  | no longer in filter / unknown | - |
| `LP410362-0` |  | no longer in filter / unknown | - |
| `LP410370-3` |  | no longer in filter / unknown | - |
| `LP410371-1` |  | no longer in filter / unknown | - |
| `LP410379-4` |  | no longer in filter / unknown | - |
| `LP410384-4` |  | no longer in filter / unknown | - |
| `LP411202-7` |  | no longer in filter / unknown | - |
| `LP411301-7` |  | no longer in filter / unknown | - |
| `LP411524-4` |  | no longer in filter / unknown | - |
| `LP418761-5` |  | no longer in filter / unknown | - |
| `LP421070-6` |  | no longer in filter / unknown | - |
| `LP427339-9` |  | no longer in filter / unknown | - |
| `LP427340-7` |  | no longer in filter / unknown | - |
| `LP427341-5` |  | no longer in filter / unknown | - |
| `LP427342-3` |  | no longer in filter / unknown | - |
| `LP427343-1` |  | no longer in filter / unknown | - |
| `LP427344-9` |  | no longer in filter / unknown | - |
| `LP427400-9` |  | no longer in filter / unknown | - |
| `LP427401-7` |  | no longer in filter / unknown | - |
| `LP427402-5` |  | no longer in filter / unknown | - |
| `LP427431-4` |  | no longer in filter / unknown | - |
| `LP427432-2` |  | no longer in filter / unknown | - |
| `LP427433-0` |  | no longer in filter / unknown | - |
| `LP427434-8` |  | no longer in filter / unknown | - |
| `LP427440-5` |  | no longer in filter / unknown | - |
| `LP427928-9` |  | no longer in filter / unknown | - |
| `LP429665-5` |  | no longer in filter / unknown | - |
| `LP429666-3` |  | no longer in filter / unknown | - |
| `LP429680-4` |  | no longer in filter / unknown | - |
| `LP429681-2` |  | no longer in filter / unknown | - |
| `LP431487-0` |  | no longer in filter / unknown | - |
| `LP431491-2` |  | no longer in filter / unknown | - |
| `LP431492-0` |  | no longer in filter / unknown | - |
| `LP431493-8` |  | no longer in filter / unknown | - |
| `LP431494-6` |  | no longer in filter / unknown | - |
| `LP431498-7` |  | no longer in filter / unknown | - |
| `LP431508-3` |  | no longer in filter / unknown | - |
| `LP431509-1` |  | no longer in filter / unknown | - |
| `LP431510-9` |  | no longer in filter / unknown | - |
| `LP432007-5` |  | no longer in filter / unknown | - |
| `LP432009-1` |  | no longer in filter / unknown | - |
| `LP432010-9` |  | no longer in filter / unknown | - |
| `LP432012-5` |  | no longer in filter / unknown | - |
| `LP432013-3` |  | no longer in filter / unknown | - |
| `LP432014-1` |  | no longer in filter / unknown | - |
| `LP432015-8` |  | no longer in filter / unknown | - |
| `LP432020-8` |  | no longer in filter / unknown | - |
| `LP432022-4` |  | no longer in filter / unknown | - |
| `LP432023-2` |  | no longer in filter / unknown | - |
| `LP432025-7` |  | no longer in filter / unknown | - |
| `LP432026-5` |  | no longer in filter / unknown | - |
| `LP432028-1` |  | no longer in filter / unknown | - |
| `LP432029-9` |  | no longer in filter / unknown | - |
| `LP434175-8` |  | no longer in filter / unknown | - |
| `LP436285-3` |  | no longer in filter / unknown | - |
| `LP436417-2` |  | no longer in filter / unknown | - |
| `LP436847-0` |  | no longer in filter / unknown | - |
| `LP436926-2` |  | no longer in filter / unknown | - |
| `LP436928-8` |  | no longer in filter / unknown | - |
| `LP437048-4` |  | no longer in filter / unknown | - |
| `LP437310-8` |  | no longer in filter / unknown | - |
| `LP437311-6` |  | no longer in filter / unknown | - |
| `LP439139-9` |  | no longer in filter / unknown | - |
| `LP441983-6` |  | no longer in filter / unknown | - |
| `LP441985-1` |  | no longer in filter / unknown | - |
| `LP441986-9` |  | no longer in filter / unknown | - |
| `LP441988-5` |  | no longer in filter / unknown | - |
| `LP442789-6` |  | no longer in filter / unknown | - |
| `LP442814-2` |  | no longer in filter / unknown | - |
| `LP444235-8` |  | no longer in filter / unknown | - |
| `LP444258-0` |  | no longer in filter / unknown | - |
| `LP444267-1` |  | no longer in filter / unknown | - |
| `LP444272-1` |  | no longer in filter / unknown | - |
| `LP444350-5` |  | no longer in filter / unknown | - |
| `LP445866-9` |  | no longer in filter / unknown | - |
| `LP445944-4` |  | no longer in filter / unknown | - |
| `LP446396-6` |  | no longer in filter / unknown | - |
| `LP446436-0` |  | no longer in filter / unknown | - |
| `LP447152-2` |  | no longer in filter / unknown | - |
| `LP447344-5` |  | no longer in filter / unknown | - |
| `LP447443-5` |  | no longer in filter / unknown | - |
| `LP448076-2` |  | no longer in filter / unknown | - |
| `LP448077-0` |  | no longer in filter / unknown | - |
| `LP448078-8` |  | no longer in filter / unknown | - |
| `LP448145-5` |  | no longer in filter / unknown | - |
| `LP448670-2` |  | no longer in filter / unknown | - |
| `LP448714-8` |  | no longer in filter / unknown | - |
| `LP450167-4` |  | no longer in filter / unknown | - |
| `LP450263-1` |  | no longer in filter / unknown | - |

**New members (5499):**

| Code | Display |
|---|---|
| `104622-6` | Chronic pain and high impact chronic pain [HICP] |
| `104624-2` | How often did pain limit your life or work activities |
| `105306-5` | Parenting stress questionnaire OBVL-K |
| `105311-5` | I can calm my child down when he/she gets angry |
| `105317-2` | Total score OBVL-K |
| `105318-0` | Transformed score parenting stress questionnaire short version OBVL-K |
| `105425-3` | How often did you have pain |
| `105438-6` | Total score OBVL |
| `105439-4` | Transformed score depressive mood OBVL |
| `105440-2` | Transformed score parent child relationship problems OBVL |
| `105441-0` | Parent child relationship problems [Score] OBVL |
| `105442-8` | Transformed score parenting problems OBVL |
| `105443-6` | Transformed score parental role restriction OBVL |
| `105446-9` | Transformed score physical health problems OBVL |
| `105451-9` | Parenting stress questionnaire OBVL |
| `105452-7` | I feel happy with my child |
| `105453-5` | My child listens to me |
| `105454-3` | I enjoy life |
| `105455-0` | Raising my child leaves me with too little personal time |
| `106103-5` | I feel cheerful when my child is with me |
| `106217-3` | I feel happy |
| `106218-1` | My child keeps me from other activities |
| `106219-9` | I feel satisfied with my child |
| `106221-5` | I am in charge when I am with my child |
| `106222-3` | Sometimes I do not see the point of living |
| `106223-1` | I would like to visit friends and acquaintances more often but I am unable to because of my child |
| `106224-9` | When I am with my child I feel good |
| `106225-6` | I am patient with my child |
| `106226-4` | I frequently feel good |
| `106227-2` | I have less contact with friends than I used to because of my child |
| `106228-0` | I feel calm when my child is with me |
| `106229-8` | Interaction with my child is easy |
| `106230-6` | I am frequently in a bad mood |
| `106231-4` | I cannot leave the house much at all because of my child |
| `106232-2` | My child is a source of enjoyment |
| `106234-8` | I know I am doing a good job as a parent |
| `106235-5` | I hate myself |
| `106236-3` | I have little contact with others because of my child |
| `106237-1` | I am good at correcting my child when necessary |
| `106238-9` | I view the future positively |

… 5459 more, see the CSV.

### SIGNIFICANT · `mii-vs-patho-service-request-code` (UNPINNED, filter)

MII VS Patho Service Request Code  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-service-request-code`  
Members: 6815 → 6826


**Display changed:**

| Code | Old | New |
|---|---|---|
| `100019-9` | ALK gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ALK gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100020-7` | GNA11 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GNA11 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100021-5` | GNAQ gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GNAQ gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100022-3` | IDH1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | IDH1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100023-1` | IDH2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | IDH2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100024-9` | SETBP1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SETBP1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100025-6` | SRSF2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SRSF2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100026-4` | MET gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MET gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100027-2` | SMAD4 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SMAD4 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `100028-0` | FBXW7 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FBXW7 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `102038-7` | ROS proto-oncogene 1 mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ROS proto-oncogene 1 mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `104293-6` | PDGFRA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PDGFRA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `104321-5` | CXCR4 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CXCR4 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `105939-3` | RUNX1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | RUNX1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `105940-1` | DNMT3A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | DNMT3A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `106870-9` | NGR1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NGR1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `106873-3` | NTRK gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NTRK gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `111525-2` | Hereditary paraganglioma-pheochromocytoma multigene analysis [Mass/volume] in Blood or Tissue by Molecular genetics method | Hereditary paraganglioma-pheochromocytoma multigene analysis in Blood or Tissue by Molecular genetics method |
| `20990-8` | APC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | APC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21081-5` | ASPA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ASPA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21247-2` | DMD gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | DMD gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21619-2` | APOE gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | APOE gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21624-2` | ATM gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ATM gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21626-7` | ATP7B gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ATP7B gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21636-6` | BRCA1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BRCA1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21641-6` | CACNA1S gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CACNA1S gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21646-5` | CBS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CBS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21652-3` | CDH1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CDH1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21654-9` | CFTR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CFTR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21657-2` | COL2A1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | COL2A1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21659-8` | CTNNB1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CTNNB1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21665-5` | EGFR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | EGFR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21667-1` | F5 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | F5 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21670-5` | F7 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | F7 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21672-1` | F8 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | F8 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21674-7` | FGFR2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FGFR2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21676-2` | FGFR3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FGFR3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21680-4` | G6PD gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | G6PD gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21685-3` | HADHB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HADHB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21687-9` | HBA1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HBA1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21689-5` | HBB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HBB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21692-9` | PRSS1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PRSS1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21694-5` | HFE gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HFE gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21698-6` | HRAS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HRAS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21700-0` | Kallmann syndrome gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Kallmann syndrome gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21702-6` | KRAS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | KRAS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21704-2` | MT-ATP6 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MT-ATP6 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21709-1` | MTHFR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MTHFR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21715-8` | MXI1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MXI1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21716-6` | NB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21717-4` | NF1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NF1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21719-0` | NRAS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NRAS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21721-6` | OTC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | OTC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21723-2` | SERPINA1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SERPINA1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21727-3` | PMP22 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PMP22 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21729-9` | PSAP gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PSAP gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21731-5` | RB1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | RB1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21733-1` | RET gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | RET gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21735-6` | SNCA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SNCA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21739-8` | TP53 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TP53 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21740-6` | TRAF3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TRAF3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `21742-2` | WT1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | WT1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `22070-7` | HP gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HP gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `22071-5` | Gaucher 3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Gaucher 3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `22072-3` | Gaucher 2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Gaucher 2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `22073-1` | Gaucher 1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Gaucher 1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `24476-4` | F2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | F2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `30005-3` | CYP21A2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CYP21A2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `32630-6` | MSH2 gene+MLH1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MSH2 gene+MLH1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `32632-2` | HEXA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HEXA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `32639-7` | FANCC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FANCC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `32640-5` | BLM gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BLM gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `32641-3` | SMPD1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SMPD1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `32653-8` | DYS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | DYS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `34658-5` | MCOLN1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MCOLN1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `34722-9` | EGR2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | EGR2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `34727-8` | DMPK gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | DMPK gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35137-9` | MECP2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MECP2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35295-5` | BTK gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BTK gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35296-3` | PAX3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PAX3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35297-1` | LMNA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | LMNA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35299-7` | PSEN1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PSEN1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35302-9` | HYAL1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HYAL1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35304-5` | CLA2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CLA2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35354-0` | COL1A1+COL1A2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | COL1A1+COL1A2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35355-7` | PABPN1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PABPN1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35357-3` | PEO gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PEO gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35379-7` | HNPCC genes mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HNPCC genes mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35461-3` | ELN gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ELN gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `35744-2` | TP73L gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TP73L gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `36911-6` | SCA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SCA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `36920-7` | PROP1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PROP1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38411-5` | TOR1A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TOR1A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38529-4` | CMTX2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CMTX2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38530-2` | BRCA2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BRCA2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38532-8` | SPG3A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SPG3A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38533-6` | TCOF1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TCOF1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38537-7` | ARX gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ARX gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38895-9` | ELA2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ELA2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38896-7` | F9 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | F9 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38907-2` | NIPA1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NIPA1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38918-9` | ABCC8 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ABCC8 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38919-7` | LITAF gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | LITAF gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38920-5` | MFN2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MFN2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38921-3` | MSH6 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MSH6 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38922-1` | PTCH gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PTCH gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38923-9` | SDHC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SDHC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38924-7` | TBX5 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TBX5 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38925-4` | RS1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | RS1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38929-6` | FAH gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FAH gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38930-4` | EXT1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | EXT1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `38931-2` | TRPS1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TRPS1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `39080-7` | EPM2A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | EPM2A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `39089-8` | PLP1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PLP1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `40471-5` | FBN1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FBN1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `40871-6` | CNBP gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CNBP gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `40970-6` | VWF gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | VWF gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `40994-6` | CPEO syndrome gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CPEO syndrome gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `40995-3` | Mitochondria Genes mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Mitochondria Genes mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41042-3` | WFS1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | WFS1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41043-1` | VHL gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | VHL gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41044-9` | UGT1A1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | UGT1A1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41045-6` | TYR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TYR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41046-4` | TWIST1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TWIST1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41047-2` | TSC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TSC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41048-0` | TPMT gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TPMT gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41049-8` | TNFRSF1A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TNFRSF1A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41050-6` | TH gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TH gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41051-4` | SPINK1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SPINK1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41052-2` | SPAST gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SPAST gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41053-0` | SMN1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SMN1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41055-5` | SLC26A4 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SLC26A4 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41056-3` | SLC22A18 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SLC22A18 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41058-9` | SH2D1A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SH2D1A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41059-7` | SFTPC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SFTPC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41060-5` | SFTPB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SFTPB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41061-3` | SDHD gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SDHD gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41062-1` | SDHB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SDHB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41063-9` | RPS6KA3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | RPS6KA3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41064-7` | PYGM gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PYGM gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41065-4` | PTPN11 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PTPN11 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41066-2` | PRX gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PRX gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41068-8` | PRF1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PRF1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41069-6` | PPT1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PPT1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41070-4` | Peripheral neuropathy gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Peripheral neuropathy gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41071-2` | PARK2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PARK2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41072-0` | PANK2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PANK2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41073-8` | NR0B1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NR0B1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41075-3` | NPHS1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NPHS1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41076-1` | NPDC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NPDC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41077-9` | NOTCH3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NOTCH3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41078-7` | NIPBL gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NIPBL gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41079-5` | NEFL gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NEFL gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41080-3` | Myotonic dystrophy gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Myotonic dystrophy gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41081-1` | MUTYH gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MUTYH gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41082-9` | MT-TK gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MT-TK gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41083-7` | MTM1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MTM1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41084-5` | MSH2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MSH2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41085-2` | MPZ gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MPZ gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41086-0` | MLH1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MLH1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41087-8` | Mitochondrial myopathy gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Mitochondrial myopathy gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41088-6` | MERRF gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MERRF gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41089-4` | MEN1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MEN1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41090-2` | MELAS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MELAS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41091-0` | MEFV gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MEFV gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41092-8` | MAPT gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MAPT gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41093-6` | LHON syndrome gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | LHON syndrome gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41094-4` | LAMA2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | LAMA2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41095-1` | L1CAM gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | L1CAM gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41098-5` | GPC3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GPC3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41099-3` | GLA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GLA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41100-9` | GJB6 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GJB6 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41101-7` | GJB2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GJB2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41102-5` | GJB1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GJB1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41103-3` | Gene XXX mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Gene XXX mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41104-1` | GBA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GBA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41105-8` | FSHD gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FSHD gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41106-6` | FXN gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FXN gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41107-4` | FMR1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FMR1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41108-2` | FGF23 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FGF23 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41109-0` | FGD1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FGD1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41110-8` | CSTB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CSTB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41111-6` | COL5A1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | COL5A1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41112-4` | CMT axonal gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CMT axonal gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41113-2` | Chronic lymphocytic leukemia gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | Chronic lymphocytic leukemia gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41114-0` | CATCH22 syndrome gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CATCH22 syndrome gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41115-7` | NOD2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NOD2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41116-5` | ATP7A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ATP7A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41117-3` | AS+PWS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | AS+PWS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41118-1` | AR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | AR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41119-9` | APTX gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | APTX gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41120-7` | ALDOB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ALDOB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41121-5` | ACADS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ACADS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41750-1` | COCH gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | COCH gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `41872-3` | PDCD10 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PDCD10 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `42318-6` | GALT gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GALT gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `42321-0` | HTT gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HTT gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `42777-3` | AKT1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | AKT1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `42780-7` | CCND1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CCND1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `42783-1` | ERBB2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ERBB2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `42785-6` | FGFR1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FGFR1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `42794-8` | MYC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MYC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `43097-5` | COL3A1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | COL3A1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `43277-3` | GDAP1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GDAP1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `43310-2` | FBN2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FBN2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `43358-1` | UNC13D gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | UNC13D gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `43747-5` | OCA2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | OCA2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `44606-2` | ALOX3+ALOX12B gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ALOX3+ALOX12B gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `44617-9` | PWS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PWS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `44803-5` | GNE gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GNE gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `45190-6` | CASR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CASR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `45191-4` | CAPN3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CAPN3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `45284-7` | DPYD gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | DPYD gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `46207-7` | PKD1 gene+PKD2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PKD1 gene+PKD2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `47955-0` | EYA1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | EYA1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `47959-2` | GFAP gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GFAP gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `47968-3` | PINK1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PINK1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `47974-1` | THRB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | THRB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48024-4` | AS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | AS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48026-9` | ITGA2B gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ITGA2B gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48028-5` | SERPINE1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SERPINE1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48029-3` | PKLR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PKLR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48033-5` | TTR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TTR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48580-5` | KCNQ1OT1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | KCNQ1OT1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48732-2` | NCF1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NCF1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48733-0` | NCF2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NCF2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48734-8` | CYBB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CYBB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48972-4` | FGFR2 gene+FGFR3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FGFR2 gene+FGFR3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48974-0` | MDCR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MDCR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48975-7` | GPR143 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | GPR143 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48976-5` | POLG gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | POLG gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48977-3` | SGCG gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SGCG gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48979-9` | TSC1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TSC1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `48980-7` | TSC2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TSC2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `49215-7` | PKHD1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PKHD1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `49504-4` | CMT demyelinating gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CMT demyelinating gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `49506-9` | MYOC gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MYOC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `49678-6` | CPT2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CPT2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `49704-0` | SH3TC2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SH3TC2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `49706-5` | ARSA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ARSA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `49707-3` | KCNQ2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | KCNQ2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `50722-8` | VKORC1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | VKORC1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `51476-0` | ABCB4 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ABCB4 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `51778-9` | YY1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | YY1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `51779-7` | CFH gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CFH gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53726-6` | KCNC3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | KCNC3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53727-4` | SOS1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SOS1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53841-3` | ATRX gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ATRX gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53849-6` | HTC2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | HTC2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53852-0` | COL2A1 gene+COL11A1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | COL2A1 gene+COL11A1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53855-3` | DNAI1+DNAH5 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | DNAI1+DNAH5 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53862-9` | FIG4 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FIG4 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53876-9` | LRRK2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | LRRK2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53877-7` | NAGS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NAGS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53883-5` | OCRL1 mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | OCRL1 mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `53897-5` | SPAST gene + KIAA0196 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SPAST gene + KIAA0196 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `54448-6` | NPM1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NPM1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `55135-8` | BCR-ABL1 kinase domain mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BCR-ABL1 kinase domain mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `56022-7` | ACE gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ACE gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `56158-9` | PCSK9 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PCSK9 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `56159-7` | LDLR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | LDLR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `56752-9` | APOB gene+LDLR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | APOB gene+LDLR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `56883-2` | BCHE gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BCHE gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57308-9` | CYP11B1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CYP11B1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57309-7` | PRNP gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PRNP gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57310-5` | SRY gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SRY gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57753-6` | IKBKG gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | IKBKG gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57758-5` | TNFRSF13B gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TNFRSF13B gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57759-3` | WAS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | WAS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57908-6` | AIRE gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | AIRE gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57909-4` | ADNFLE gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ADNFLE gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57918-5` | CACNA1S+SCN4A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CACNA1S+SCN4A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57927-6` | CDKN2A+CDK4 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CDKN2A+CDK4 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57931-8` | CFTR+PRSS1+SPINK1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CFTR+PRSS1+SPINK1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57951-6` | CPVT1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CPVT1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57962-3` | FECH gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FECH gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `57963-1` | FLCN gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FLCN gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `58010-0` | MSH2 gene+MLH1 gene+MSH6 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MSH2 gene+MLH1 gene+MSH6 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `58483-9` | BRAF gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BRAF gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `58987-9` | ITGB3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ITGB3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `58988-7` | FGB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FGB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `59067-9` | ALAS2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ALAS2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `60033-8` | PIK3CA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PIK3CA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `64012-8` | CEBPA gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CEBPA gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `68467-0` | APOB+LDLR+PCSK9 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | APOB+LDLR+PCSK9 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `69363-0` | SERPINA10 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SERPINA10 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `69364-8` | ATP1A2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ATP1A2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `72696-8` | SLC40A1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SLC40A1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `72881-6` | UGT2B15 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | UGT2B15 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `72883-2` | CYP2E1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CYP2E1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `74004-3` | ABCB1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ABCB1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77171-7` | KIT gene exon 11 mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | KIT gene exon 11 mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77172-5` | KIT gene exon 9 mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | KIT gene exon 9 mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77174-1` | CALR gene exon 9 mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CALR gene exon 9 mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77200-4` | SI gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SI gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77628-6` | PSEN2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PSEN2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77629-4` | PARK7 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PARK7 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77630-2` | ALS2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ALS2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77631-0` | VAPB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | VAPB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77632-8` | ANG gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ANG gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77633-6` | TARDBP gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TARDBP gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77634-4` | FUS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FUS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `77750-8` | DLD gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | DLD gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `79568-2` | ABCD1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | ABCD1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `80715-6` | FSHR gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | FSHR gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `81420-2` | KRAS and NRAS gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | KRAS and NRAS gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `89323-0` | APOB gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | APOB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `92843-2` | FLT3 gene p.Asp835 mutations [Presence] in Blood or Tissue by Molecular genetics method | FLT3 gene p.Asp835 mutations found [Presence] in Blood or Tissue by Molecular genetics method |
| `96964-2` | EZH2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | EZH2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `96965-9` | CARD11 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CARD11 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `96966-7` | CD79A gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CD79A gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `96967-5` | CD79B gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | CD79B gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `96968-3` | TNFAIP3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | TNFAIP3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `96969-1` | MYD88 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | MYD88 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `99126-5` | NOTCH1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | NOTCH1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `99127-3` | BIRC3 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | BIRC3 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `99128-1` | PLCG2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | PLCG2 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `99129-9` | SF3B1 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal | SF3B1 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |

**New members (11):**

| Code | Display |
|---|---|
| `112739-8` | SLCO1B1 gene allele [Genotype] in Blood or Tissue by Molecular genetics method Nominal |
| `113019-4` | CYP3A4 gene.c.1461_1462insA [Presence] in Blood or Tissue by Molecular genetics method |
| `113020-2` | CYP3A5 gene.g.14690G>A [Presence] in Blood or Tissue by Molecular genetics method |
| `115587-8` | CLRN1 mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `115588-6` | PCDH15 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `115589-4` | BCKDHB gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `115590-2` | TMEM216 gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `115591-0` | G6PC gene mutations found [Identifier] in Blood or Tissue by Targeted gene mutation analysis Nominal |
| `115592-8` | HBA1 and HBA2 gene mutations found [Identifier] in Blood or Tissue by Molecular genetics method Nominal |
| `115593-6` | Spinal muscular atrophy associated mutation [Identifier] in Blood or Tissue by Molecular genetics method Nominal |
| `115595-1` | Inherited diseases screen Result in Blood or Tissue by Molecular genetics method Nominal |

## Module `seltene`

### SIGNIFICANT · `mii-vs-seltene-nbs-dbs-all` (UNPINNED, filter)

MII VS Seltene Erkrankungen NBS alle Trockenblut-Analyte (LOINC)  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-seltene/ValueSet/mii-vs-seltene-nbs-dbs-all`  
Members: 608 → 610


**Display changed:**

| Code | Old | New |
|---|---|---|
| `54083-1` | CFTR gene mutations found [Identifier] in DBS by Molecular genetics method Nominal | CFTR gene mutations found [Identifier] in DBS by Targeted gene mutation analysis Nominal |
| `62300-9` | Lysosomal storage disorders newborn screening panel | Lysosomal disorders newborn screening panel |
| `62301-7` | Lysosomal storage disorders newborn screen interpretation | Lysosomal disorders newborn screen interpretation |
| `62302-5` | Lysosomal storage disorders suspected [Identifier] in DBS | Lysosomal disorders suspected [Identifier] in DBS |
| `62303-3` | Lysosomal storage disorders newborn screening comment-discussion | Lysosomal disorders newborn screening comment-discussion |

**New members (2):**

| Code | Display |
|---|---|
| `115574-6` | Sickle cells [Presence] in DBS |
| `115576-1` | Amino acids [Presence] in DBS |

