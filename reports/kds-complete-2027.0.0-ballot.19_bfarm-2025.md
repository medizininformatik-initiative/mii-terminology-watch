# Terminology release impact: de.medizininformatikinitiative.kerndatensatz.complete 2027.0.0-ballot.19

| | Baseline | Target |
|---|---|---|
| ATC | 2026 | 2025 |
| ICD-10-GM | 2026 | 2025 |
| OPS | 2026 | 2025 |
| LOINC | 2.82 | 2.82 |
| SNOMED CT | 20260701 | 20260701 |
| HGNC | 20250704 | 20250704 |

Generated 2026-10-19T20:21:46 against https://ontoserver.mii-termserv.de/fhir (4011 server calls).

## Summary

| Severity | ValueSets |
|---|---:|
| BREAKING | 10 |
| SIGNIFICANT | 2 |
| MINOR | 1 |
| NONE | 6 |

Severity rules: BREAKING = a member of an enumerated include or a filter anchor was inactivated, or a member became inactive; SIGNIFICANT = members dropped out of a filter-defined ValueSet or displays changed; MINOR = new members only.

Pinned ValueSets (all includes carry a version) do not change at runtime until the pin is moved; unpinned ones change with the next terminology load on the server.

## Per module

| Module | ValueSets compared | BREAKING | SIGNIFICANT | MINOR | unchanged |
|---|---:|---:|---:|---:|---:|
| diagnose | 1 | 0 | 0 | 0 | 1 |
| kardio | 2 | 0 | 1 | 0 | 1 |
| medikation | 1 | 0 | 0 | 0 | 1 |
| onko | 14 | 10 | 1 | 1 | 2 |
| prozedur | 1 | 0 | 0 | 0 | 1 |

## Module `kardio`

### SIGNIFICANT · `mii-vs-kardio-kardiale-deviceimplantation-ops` (UNPINNED, filter)

MII VS Kardio Kardiale Devicemimplantation [OPS]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-kardiale-deviceimplantation-ops`  
Members: 95 → 91


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `5-377.j0` | Implantation eines Herzschrittmachers, Defibrillators und Ereignis-Rekorders: Defibrillator mit extravasaler Elektrode: Mit subkutaner Elektrode | not in this code system version | - |
| `5-377.j1` | Implantation eines Herzschrittmachers, Defibrillators und Ereignis-Rekorders: Defibrillator mit extravasaler Elektrode: Mit substernaler Elektrode | not in this code system version | - |
| `5-377.k0` | Implantation eines Herzschrittmachers, Defibrillators und Ereignis-Rekorders: Intrakardialer Impulsgenerator: Rechtsventrikulär | not in this code system version | - |
| `5-377.k1` | Implantation eines Herzschrittmachers, Defibrillators und Ereignis-Rekorders: Intrakardialer Impulsgenerator: Rechtsatrial | not in this code system version | - |

**Display changed:**

| Code | Old | New |
|---|---|---|
| `5-377.j` | Implantation eines Herzschrittmachers, Defibrillators und Ereignis-Rekorders: Defibrillator mit extravasaler Elektrode | Implantation eines Herzschrittmachers, Defibrillators und Ereignis-Rekorders: Defibrillator mit subkutaner Elektrode |

## Module `onko`

### BREAKING · `mii-vs-onko-ops-nuklearmedizin` (UNPINNED, enumerated, filter)

MII VS Onkologie OPS Nuklearmedizin  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-ops-nuklearmedizin`  
Members: 69 → 68


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `8-530.d3` | Therapie mit offenen Radionukliden: Intravenöse Radioliganden-Therapie: Therapie mit Actinium-225-PSMA-Liganden aus patientenindividueller Eigenherstellung | not in this code system version | - |

**Display changed:**

| Code | Old | New |
|---|---|---|
| `8-531.2` | Radiojodtherapie: Radiojodtherapie mit 5 GBq I-131 oder mehr | Radiojodtherapie: Radiojodtherapie mit 5 oder mehr GBq I-131 |
| `8-531.20` | Radiojodtherapie: Radiojodtherapie mit 5 GBq I-131 oder mehr: Ohne Gabe von rekombinantem Thyreotropin (rh-TSH) | Radiojodtherapie: Radiojodtherapie mit 5 oder mehr GBq I-131: Ohne Gabe von rekombinantem Thyreotropin (rh-TSH) |
| `8-531.21` | Radiojodtherapie: Radiojodtherapie mit 5 GBq I-131 oder mehr: Mit Gabe von rekombinantem Thyreotropin (rh-TSH) | Radiojodtherapie: Radiojodtherapie mit 5 oder mehr GBq I-131: Mit Gabe von rekombinantem Thyreotropin (rh-TSH) |

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen` (UNPINNED, enumerated)

MII VS Onkologie Systemische Therapie Substanzen  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen`  
Members: 445 → 428

- **Filter/enumerated anchor inactive:** `L01XE50`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE36`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX22`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX70`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE17`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX49`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE41`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE43`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX86`  — no successor
- **Filter/enumerated anchor inactive:** `L01FF14`  — no successor
- **Filter/enumerated anchor inactive:** `L01EP01`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX45`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE28`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE38`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX61`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE16`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE06`  — no successor
- **Filter/enumerated anchor inactive:** `L01FX35`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA25`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX59`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE46`  — no successor
- **Filter/enumerated anchor inactive:** `L01FF15`  — no successor
- **Filter/enumerated anchor inactive:** `L01FX36`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE10`  — no successor
- **Filter/enumerated anchor inactive:** `L01EB12`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE54`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX63`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX47`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE01`  — no successor
- **Filter/enumerated anchor inactive:** `L01EM06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX62`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX50`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE07`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE53`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE29`  — no successor
- **Filter/enumerated anchor inactive:** `L01FX37`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE44`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE39`  — no successor
- **Filter/enumerated anchor inactive:** `L01EE05`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE45`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX54`  — no successor
- **Filter/enumerated anchor inactive:** `L01XY03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XL12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX46`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE35`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE33`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX42`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX84`  — no successor
- **Filter/enumerated anchor inactive:** `L01XY02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE52`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE42`  — no successor
- **Filter/enumerated anchor inactive:** `L01EK05`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX39`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE18`  — no successor
- **Filter/enumerated anchor inactive:** `L01EP03`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA10`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE05`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE04`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX60`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE09`  — no successor
- **Filter/enumerated anchor inactive:** `L01EP02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX71`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX17`  — no successor
- **Filter/enumerated anchor inactive:** `L01EC04`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX14`  — no successor
- **Filter/enumerated anchor inactive:** `L01EE06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE15`  — no successor
- **Filter/enumerated anchor inactive:** `L01EX29`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX43`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX38`  — no successor
- **Filter/enumerated anchor inactive:** `L01EH04`  — no successor

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `L01EB12` | Firmonertinib | not in this code system version | - |
| `L01EC04` | Tovorafenib | not in this code system version | - |
| `L01EE05` | Mirdametinib | not in this code system version | - |
| `L01EE06` | Tunlametinib | not in this code system version | - |
| `L01EH04` | Zongertinib | not in this code system version | - |
| `L01EK05` | Rivoceranib | not in this code system version | - |
| `L01EM06` | Inavolisib | not in this code system version | - |
| `L01EP01` | Capmatinib | not in this code system version | - |
| `L01EP02` | Tepotinib | not in this code system version | - |
| `L01EP03` | Savolitinib | not in this code system version | - |
| `L01EX29` | Vimseltinib | not in this code system version | - |
| `L01FF14` | Camrelizumab | not in this code system version | - |
| `L01FF15` | Envafolimab | not in this code system version | - |
| `L01FX35` | Datopotamab deruxtecan | not in this code system version | - |
| `L01FX36` | Patritumab deruxtecan | not in this code system version | - |
| `L01FX37` | Linvoseltamab | not in this code system version | - |
| `L01XL12` | Obecabtagen autoleucel | not in this code system version | - |
| `L01XX84` | Pelabresib | not in this code system version | - |
| `L01XX86` | Calaspargase pegol | not in this code system version | - |

**New members (2):**

| Code | Display |
|---|---|
| `L01EX17` | Capmatinib |
| `L01EX21` | Tepotinib |

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2018` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2018  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2018`  
Members: 237 → 237

- **Filter/enumerated anchor inactive:** `L01XE13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE36`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX22`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE17`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX49`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC07`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC28`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC11`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX45`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE28`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE38`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE16`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE06`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA25`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE10`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX47`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE01`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX50`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE07`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE29`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE39`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC17`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC15`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX46`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE35`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE33`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX42`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC18`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE42`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX39`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE18`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA10`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE05`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE04`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE09`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX17`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE15`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX43`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX38`  — no successor

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2019` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2019  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2019`  
Members: 240 → 240

- **Filter/enumerated anchor inactive:** `L01XE13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE36`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX22`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE17`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX49`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC07`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE41`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE43`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX45`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE28`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE38`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE16`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC28`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA25`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX59`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE46`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE10`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX47`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE01`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC11`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX50`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE07`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE29`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE44`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE39`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE45`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX54`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC17`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC15`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX46`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE35`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE33`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX42`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC18`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE42`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX39`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE18`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA10`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE05`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE04`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE09`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX17`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE15`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX43`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX38`  — no successor

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2020` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2020  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2020`  
Members: 244 → 244

- **Filter/enumerated anchor inactive:** `L01XE50`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE36`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX22`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE17`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX49`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC07`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE41`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE43`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX45`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE28`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE38`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX61`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE16`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC28`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA25`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX59`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE46`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE10`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE54`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX63`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX47`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE01`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC11`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX62`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX50`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE07`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE53`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE29`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE44`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE39`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE45`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX54`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC17`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC15`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX46`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE35`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE33`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX42`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC18`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE52`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE42`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC02`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX39`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE18`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA10`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE05`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE04`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX60`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE09`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX17`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE25`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX14`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XE15`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX43`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX38`  — no successor

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2021` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2021  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2021`  
Members: 323 → 325

- **Filter/enumerated anchor inactive:** `L04AA34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC32`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC31`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX70`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC07`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC19`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC12`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC06`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC24`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC28`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA25`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX59`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC26`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC11`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX62`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA13`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC17`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC15`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC08`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC18`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC13`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA10`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX71`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XC14`  — no successor

**New members (2):**

| Code | Display |
|---|---|
| `L01EX17` | Capmatinib |
| `L01EX21` | Tepotinib |

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2022` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2022  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2022`  
Members: 376 → 378

- **Filter/enumerated anchor inactive:** `L04AA34`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX70`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA26`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA25`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX59`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX62`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA13`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XY02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA10`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX51`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX71`  — no successor

**New members (2):**

| Code | Display |
|---|---|
| `L01EX17` | Capmatinib |
| `L01EX21` | Tepotinib |

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2023` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2023  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2023`  
Members: 395 → 397

- **Filter/enumerated anchor inactive:** `L04AA34`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA26`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA25`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA21`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX59`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA27`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX62`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA13`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA23`  — no successor
- **Filter/enumerated anchor inactive:** `L01XY03`  — no successor
- **Filter/enumerated anchor inactive:** `L01XY02`  — no successor
- **Filter/enumerated anchor inactive:** `L04AA10`  — no successor

**New members (2):**

| Code | Display |
|---|---|
| `L01EX17` | Capmatinib |
| `L01EX21` | Tepotinib |

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2024` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2024  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2024`  
Members: 413 → 415

- **Filter/enumerated anchor inactive:** `L01XX59`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX62`  — no successor

**New members (2):**

| Code | Display |
|---|---|
| `L01EX17` | Capmatinib |
| `L01EX21` | Tepotinib |

### BREAKING · `mii-vs-onko-systemische-therapie-substanzen-2026` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2026  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2026`  
Members: 444 → 425

- **Filter/enumerated anchor inactive:** `L01XX86`  — no successor
- **Filter/enumerated anchor inactive:** `L01FF14`  — no successor
- **Filter/enumerated anchor inactive:** `L01EP01`  — no successor
- **Filter/enumerated anchor inactive:** `L01FX35`  — no successor
- **Filter/enumerated anchor inactive:** `L01FF15`  — no successor
- **Filter/enumerated anchor inactive:** `L01EB12`  — no successor
- **Filter/enumerated anchor inactive:** `L01EM06`  — no successor
- **Filter/enumerated anchor inactive:** `L01FX37`  — no successor
- **Filter/enumerated anchor inactive:** `L01EE05`  — no successor
- **Filter/enumerated anchor inactive:** `L01XL12`  — no successor
- **Filter/enumerated anchor inactive:** `L01FX36`  — no successor
- **Filter/enumerated anchor inactive:** `L01XX84`  — no successor
- **Filter/enumerated anchor inactive:** `L01EK05`  — no successor
- **Filter/enumerated anchor inactive:** `L01EP03`  — no successor
- **Filter/enumerated anchor inactive:** `L01EP02`  — no successor
- **Filter/enumerated anchor inactive:** `L01EC04`  — no successor
- **Filter/enumerated anchor inactive:** `L01EE06`  — no successor
- **Filter/enumerated anchor inactive:** `L01EX29`  — no successor
- **Filter/enumerated anchor inactive:** `L01EH04`  — no successor

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `L01EB12` | Firmonertinib | not in this code system version | - |
| `L01EC04` | Tovorafenib | not in this code system version | - |
| `L01EE05` | Mirdametinib | not in this code system version | - |
| `L01EE06` | Tunlametinib | not in this code system version | - |
| `L01EH04` | Zongertinib | not in this code system version | - |
| `L01EK05` | Rivoceranib | not in this code system version | - |
| `L01EM06` | Inavolisib | not in this code system version | - |
| `L01EP01` | Capmatinib | not in this code system version | - |
| `L01EP02` | Tepotinib | not in this code system version | - |
| `L01EP03` | Savolitinib | not in this code system version | - |
| `L01EX29` | Vimseltinib | not in this code system version | - |
| `L01FF14` | Camrelizumab | not in this code system version | - |
| `L01FF15` | Envafolimab | not in this code system version | - |
| `L01FX35` | Datopotamab deruxtecan | not in this code system version | - |
| `L01FX36` | Patritumab deruxtecan | not in this code system version | - |
| `L01FX37` | Linvoseltamab | not in this code system version | - |
| `L01XL12` | Obecabtagen autoleucel | not in this code system version | - |
| `L01XX84` | Pelabresib | not in this code system version | - |
| `L01XX86` | Calaspargase pegol | not in this code system version | - |

### SIGNIFICANT · `mii-vs-onko-icd10-meldepflichtige-tumoren` (pinned, filter)

MII VS Onkologie ICD-10-GM Meldepflichtige Tumoren  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-icd10-meldepflichtige-tumoren`  
Members: 836 → 834


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `C43.50` | Bösartiges Melanom der Perianalhaut | not in this code system version | - |
| `C43.59` | Bösartiges Melanom sonstiger und nicht näher bezeichneter Teile des Rumpfes | not in this code system version | - |

### MINOR · `mii-vs-onko-systemische-therapie-substanzen-2025` (pinned, enumerated)

MII VS Onkologie Systemische Therapie Substanzen ATC 2025  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-substanzen-2025`  
Members: 419 → 421


**New members (2):**

| Code | Display |
|---|---|
| `L01EX17` | Capmatinib |
| `L01EX21` | Tepotinib |

