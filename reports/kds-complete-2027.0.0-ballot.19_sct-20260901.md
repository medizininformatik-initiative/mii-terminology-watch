# Terminology release impact: de.medizininformatikinitiative.kerndatensatz.complete 2027.0.0-ballot.19

| | Baseline | Target |
|---|---|---|
| ATC | 2026 | 2026 |
| ICD-10-GM | 2026 | 2026 |
| OPS | 2026 | 2026 |
| LOINC | 2.82 | 2.82 |
| SNOMED CT | 20260701 | 20260901 |
| HGNC | 20250704 | 20250704 |

Generated 2026-10-21T05:57:18 against https://ontoserver.mii-termserv.de/fhir + rf2:SnomedCT_InternationalRF2_PRODUCTION_20260901T120000Z.zip (2326 server calls).

## Summary

| Severity | ValueSets |
|---|---:|
| BREAKING | 3 |
| SIGNIFICANT | 13 |
| MINOR | 5 |
| NONE | 115 |

Severity rules: BREAKING = a member of an enumerated include or a filter anchor was inactivated, or a member became inactive; SIGNIFICANT = members dropped out of a filter-defined ValueSet or displays changed; MINOR = new members only.

Pinned ValueSets (all includes carry a version) do not change at runtime until the pin is moved; unpinned ones change with the next terminology load on the server.

## Per module

| Module | ValueSets compared | BREAKING | SIGNIFICANT | MINOR | unchanged |
|---|---:|---:|---:|---:|---:|
| bildgebung | 5 | 0 | 3 | 0 | 2 |
| biobank | 9 | 0 | 2 | 2 | 5 |
| diagnose | 2 | 0 | 2 | 0 | 0 |
| dokument | 4 | 0 | 0 | 0 | 4 |
| icu | 21 | 0 | 0 | 0 | 21 |
| kardio | 9 | 2 | 0 | 1 | 6 |
| labor | 4 | 0 | 0 | 0 | 4 |
| lungenfunktion | 12 | 0 | 1 | 1 | 10 |
| mikrobio | 22 | 1 | 1 | 0 | 20 |
| molgen | 4 | 0 | 0 | 0 | 4 |
| mtb | 4 | 0 | 0 | 0 | 4 |
| onko | 22 | 0 | 1 | 1 | 20 |
| patho | 7 | 0 | 2 | 0 | 5 |
| person | 1 | 0 | 0 | 0 | 1 |
| prozedur | 3 | 0 | 1 | 0 | 2 |
| seltene | 7 | 0 | 0 | 0 | 7 |

## Module `bildgebung`

### SIGNIFICANT · `mii-vs-bildgebung-findings-sct` (pinned, filter)

MII VS Bildgebung Findings SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/ValueSet/mii-vs-bildgebung-findings-sct`  
Members: 129012 → 129233


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | POSSIBLY REPLACED BY → 102556003 Pain in upper limb, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | POSSIBLY REPLACED BY → 771083005 Pain in upper arm, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 45326000 Pain of shoulder region |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 81680005 Neck pain |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | POSSIBLY REPLACED BY → 400138001 Nodular fasciitis, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `61947007` | Deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 15188001 Hearing loss |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 721294001 Acquired hearing loss |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 95828007 Congenital deafness, POSSIBLY REPLACED BY → 88052002 Mutism |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | POSSIBLY REPLACED BY → 237619009 Maternally inherited diabetes and deafness, POSSIBLY REPLACED BY → 57838006 Retinitis pigmentosa-deafness syndrome |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |

**New members (295):**

| Code | Display |
|---|---|
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |
| `1373253003` | Epilepsy due to hypoxic ischemic encephalopathy |
| `1373254009` | Epilepsy due to hypoxic brain injury |
| `1373650006` | Epilepsy due to neurodegenerative dementia |
| `1373651005` | Epilepsy due to and following ischemic stroke |
| `1373652003` | Epilepsy due to and following hemorrhagic stroke |
| `1373665007` | Vascular malformation of brain |
| `1373666008` | Congenital vascular malformation of brain |
| `1373706000` | Epilepsy due to vascular malformation of brain |
| `1373783006` | Histiocytic macrophage neoplasm |
| `1373924005` | Epilepsy due to infectious disease |
| `1373925006` | Epilepsy due to infectious abscess of brain |
| `1375929002` | Abscess of brain due to infection |
| `1375930007` | Neonatal infectious disease of central nervous system |
| `1380178003` | Epilepsy due to and following stroke |
| `1381325002` | Hypoxic brain injury |
| `1381452008` | Epilepsy due to congenital vascular malformation of brain |
| `1381728002` | Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1381731001` | Perinatal fetal and/or neonatal stroke |
| `1381732008` | Perinatal fetal and/or neonatal ischemic stroke |
| `1381733003` | Perinatal fetal and/or neonatal hemorrhagic stroke |
| `1381734009` | Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1382151008` | Acute symptomatic epileptic seizure due to poisoning |
| `1388506008` | Epilepsy due to anti-leucine-rich glioma-inactivated 1 encephalitis |
| `1388507004` | Epilepsy due to anti-NMDA (N-methyl-D-aspartate) receptor encephalitis |
| `1388508009` | Epilepsy due to cerebral hemorrhage |
| `1389043008` | Epilepsy due to genetic disease |

… 255 more, see the CSV.

### SIGNIFICANT · `mii-vs-bildgebung-imaging-procedure-code-sct` (pinned, filter)

MII VS Bildgebung ImagingProcedure Code SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/ValueSet/mii-vs-bildgebung-imaging-procedure-code-sct`  
Members: 7563 → 7566


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `433717001` | Percutaneous injection of alcohol using fluoroscopic guidance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402089004 Percutaneous injection of alcohol using fluoroscopic guidance |

**New members (4):**

| Code | Display |
|---|---|
| `1397517008` | Percutaneous transluminal repair of atrioventricular (non-mitral, non-tricuspid) valve using imaging guidance |
| `1401645001` | Imaging guided transbronchial localization of lung lesion |
| `1401646000` | Imaging guided percutaneous localization of lung lesion |
| `1402089004` | Percutaneous injection of alcohol using fluoroscopic guidance |

### SIGNIFICANT · `mii-vs-bildgebung-observation-body-site-sct` (pinned, filter)

MII VS Bildgebung Observation Body Site SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/ValueSet/mii-vs-bildgebung-observation-body-site-sct`  
Members: 45088 → 45366


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `420329002` | Bone structure of malleus | inactivated (Duplicate) | SAME AS → 34080009 Malleus structure |
| `421793000` | Bone structure of incus | inactivated (Duplicate) | SAME AS → 35395007 Incus structure |
| `422057008` | Bone structure of stapes | inactivated (Duplicate) | SAME AS → 22718006 Stapes structure |
| `422258005` | Bone structure of auditory ossicle | inactivated (Duplicate) | SAME AS → 41845008 Ear ossicle structure |
| `68801007` | Giant cell reticulosis | inactivated (Outdated) | REPLACED BY → 1295213006 Reticulohistiocytosis |
| `70839004` | Epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `727196004` | Entire epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `727838004` | Entire skin of eardrum | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `731915001` | Entire bone of malleus | inactivated (Duplicate) | SAME AS → 264090005 Entire malleus |
| `731916000` | Entire bone of incus | inactivated (Duplicate) | SAME AS → 272649008 Entire incus |
| `731918004` | Entire bone of stapes | inactivated (Duplicate) | SAME AS → 264199009 Entire stapes |
| `731919007` | Entire bone of auditory ossicle | inactivated (Duplicate) | SAME AS → 181184001 Entire ossicle of ear |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (302):**

| Code | Display |
|---|---|
| `1373338008` | Langerhans cell neoplasm |
| `1373340003` | Plasmacytoid dendritic cell neoplasm |
| `1373341004` | Histiocytic macrophage neoplasm |
| `1373346009` | MPDCP (mature plasmacytoid dendritic cell proliferation) associated with myeloid neoplasm |
| `1373377006` | Malignant dendritic cell neoplasm |
| `1373423008` | ALK-positive histiocytosis |
| `1380193004` | Mesenchymal neoplasm |
| `1380194005` | Stroma derived neoplasm of lymphoid tissue |
| `1380195006` | Mesenchymal sarcoma |
| `1380196007` | Hematopoietic sarcoma |
| `1380197003` | Splenic vascular stromal tumor |
| `1380198008` | Littoral cell angioma |
| `1380199000` | Sclerosing angiomatoid nodular transformation of spleen |
| `1380200002` | Malignant mesenchymal dendritic cell neoplasm |
| `1380408006` | EBV-positive inflammatory follicular dendritic cell sarcoma |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |
| `1399570009` | CDKN2B gene |
| `1399571008` | CERKL gene |
| `1399572001` | CES1 gene |
| `1399573006` | CFH gene |
| `1399574000` | CHD7 gene |
| `1399587006` | Structure of bony palate |
| `1399588001` | Entire bony palate |
| `1399590000` | CHIC2 gene |
| `1399591001` | CHRNA3 gene |
| `1399592008` | NLRP3 gene |
| `1399593003` | CLCN7 gene |
| `1399594009` | DNAAF3 gene |
| `1399595005` | ATP2B3 gene |
| `1399596006` | CLCN1 gene |
| `1399597002` | CLCN5 gene |
| `1399598007` | CLN3 gene |

… 262 more, see the CSV.

## Module `biobank`

### SIGNIFICANT · `mii-vs-biobank-body-structures-sct` (pinned, filter)

MII VS Biobank BodyStructures SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-body-structures-sct`  
Members: 45088 → 45366


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `420329002` | Bone structure of malleus | inactivated (Duplicate) | SAME AS → 34080009 Malleus structure |
| `421793000` | Bone structure of incus | inactivated (Duplicate) | SAME AS → 35395007 Incus structure |
| `422057008` | Bone structure of stapes | inactivated (Duplicate) | SAME AS → 22718006 Stapes structure |
| `422258005` | Bone structure of auditory ossicle | inactivated (Duplicate) | SAME AS → 41845008 Ear ossicle structure |
| `68801007` | Giant cell reticulosis | inactivated (Outdated) | REPLACED BY → 1295213006 Reticulohistiocytosis |
| `70839004` | Epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `727196004` | Entire epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `727838004` | Entire skin of eardrum | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `731915001` | Entire bone of malleus | inactivated (Duplicate) | SAME AS → 264090005 Entire malleus |
| `731916000` | Entire bone of incus | inactivated (Duplicate) | SAME AS → 272649008 Entire incus |
| `731918004` | Entire bone of stapes | inactivated (Duplicate) | SAME AS → 264199009 Entire stapes |
| `731919007` | Entire bone of auditory ossicle | inactivated (Duplicate) | SAME AS → 181184001 Entire ossicle of ear |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (302):**

| Code | Display |
|---|---|
| `1373338008` | Langerhans cell neoplasm |
| `1373340003` | Plasmacytoid dendritic cell neoplasm |
| `1373341004` | Histiocytic macrophage neoplasm |
| `1373346009` | MPDCP (mature plasmacytoid dendritic cell proliferation) associated with myeloid neoplasm |
| `1373377006` | Malignant dendritic cell neoplasm |
| `1373423008` | ALK-positive histiocytosis |
| `1380193004` | Mesenchymal neoplasm |
| `1380194005` | Stroma derived neoplasm of lymphoid tissue |
| `1380195006` | Mesenchymal sarcoma |
| `1380196007` | Hematopoietic sarcoma |
| `1380197003` | Splenic vascular stromal tumor |
| `1380198008` | Littoral cell angioma |
| `1380199000` | Sclerosing angiomatoid nodular transformation of spleen |
| `1380200002` | Malignant mesenchymal dendritic cell neoplasm |
| `1380408006` | EBV-positive inflammatory follicular dendritic cell sarcoma |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |
| `1399570009` | CDKN2B gene |
| `1399571008` | CERKL gene |
| `1399572001` | CES1 gene |
| `1399573006` | CFH gene |
| `1399574000` | CHD7 gene |
| `1399587006` | Structure of bony palate |
| `1399588001` | Entire bony palate |
| `1399590000` | CHIC2 gene |
| `1399591001` | CHRNA3 gene |
| `1399592008` | NLRP3 gene |
| `1399593003` | CLCN7 gene |
| `1399594009` | DNAAF3 gene |
| `1399595005` | ATP2B3 gene |
| `1399596006` | CLCN1 gene |
| `1399597002` | CLCN5 gene |
| `1399598007` | CLN3 gene |

… 262 more, see the CSV.

### SIGNIFICANT · `mii-vs-biobank-substance-additive-sct` (pinned, filter)

MII VS Biobank Substance Additive  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-substance-additive-sct`  
Members: 29284 → 29127


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1496005` | Proto-oncogene | inactivated (Duplicate) | SAME AS → 1396287006 Proto-oncogene structure |
| `256927003` | A*0101 | inactivated (Outdated) | REPLACED BY → 1401958003 A*01:01:01:01 allele |
| `256928008` | A*0201 | inactivated (Outdated) | - |
| `256929000` | A*0202 | inactivated (Outdated) | REPLACED BY → 1401957008 A*02:02:01:01 allele |
| `256930005` | A*0203 | inactivated (Outdated) | - |
| `256931009` | A*0204 | inactivated (Outdated) | REPLACED BY → 1401956004 A*02:04:01 allele |
| `256932002` | A*0205 | inactivated (Outdated) | - |
| `256933007` | A*0206 | inactivated (Outdated) | - |
| `256934001` | A*0207 | inactivated (Outdated) | REPLACED BY → 1401955000 A*02:07:01:01 allele |
| `256935000` | A*0208 | inactivated (Outdated) | REPLACED BY → 1401954001 A*02:08 allele |
| `256936004` | A*0209 | inactivated (Outdated) | REPLACED BY → 1401953007 A*02:09:01:01 allele |
| `256937008` | A*0210 | inactivated (Outdated) | REPLACED BY → 1401952002 A*02:10 allele |
| `256938003` | A*0211 | inactivated (Outdated) | REPLACED BY → 1401951009 A*02:11:01:01 allele |
| `256939006` | A*0212 | inactivated (Outdated) | REPLACED BY → 1401950005 A*02:12 allele |
| `256940008` | A*0301 | inactivated (Outdated) | - |
| `256941007` | A*0302 | inactivated (Outdated) | REPLACED BY → 1401949005 A*03:02:01:01 allele |
| `256942000` | A*1101 | inactivated (Outdated) | - |
| `256943005` | A*1102 | inactivated (Outdated) | - |
| `256944004` | A*2301 | inactivated (Outdated) | - |
| `256945003` | A*2401 | inactivated (Outdated) | - |
| `256946002` | A*2501 | inactivated (Outdated) | - |
| `256947006` | A*2601 | inactivated (Outdated) | - |
| `256948001` | A*2901 | inactivated (Outdated) | - |
| `256949009` | A*2902 | inactivated (Outdated) | - |
| `256950009` | A*3001 | inactivated (Outdated) | - |
| `256951008` | A*3002 | inactivated (Outdated) | - |
| `256953006` | A*31011 | inactivated (Erroneous) | REPLACED BY → 1401948002 A*31:01:02:01 allele |
| `256954000` | A*31012 | inactivated (Outdated) | REPLACED BY → 1401948002 A*31:01:02:01 allele |
| `256955004` | A*3201 | inactivated (Outdated) | - |
| `256956003` | A*3301 | inactivated (Outdated) | - |
| `256957007` | A*3401 | inactivated (Outdated) | - |
| `256958002` | A*3402 | inactivated (Outdated) | REPLACED BY → 1401947007 A*34:02:01:01 allele |
| `256959005` | A*3601 | inactivated (Outdated) | REPLACED BY → 1401946003 A*36:01:01:01 allele |
| `256960000` | A*4301 | inactivated (Outdated) | REPLACED BY → 1401945004 A*43:01 allele |
| `256961001` | A*6601 | inactivated (Outdated) | REPLACED BY → 1401944000 A*66:01:01:01 allele |
| `256962008` | A*6602 | inactivated (Outdated) | REPLACED BY → 1401943006 A*66:02:01:01 allele |
| `256963003` | A*6801 | inactivated (Outdated) | - |
| `256964009` | A*6802 | inactivated (Outdated) | - |
| `256966006` | A*6901 | inactivated (Outdated) | REPLACED BY → 1401942001 A*69:01:01:01 allele |
| `256967002` | A*7401 | inactivated (Outdated) | REPLACED BY → 1401941008 A*74:01:01:01 allele |
| `256968007` | B*0701 | inactivated (Outdated) | - |
| `256969004` | B*0702 | inactivated (Outdated) | - |
| `256970003` | B*0703 | inactivated (Outdated) | REPLACED BY → 1401939007 B*07:03 allele |
| `256971004` | B*0801 | inactivated (Outdated) | REPLACED BY → 1401938004 B*08:01:01:01 allele |
| `256972006` | B*1301 | inactivated (Outdated) | - |
| `256973001` | B*1302 | inactivated (Outdated) | - |
| `256974007` | B*1401 | inactivated (Outdated) | REPLACED BY → 1401937009 B*14:01:01:01 allele |
| `256975008` | B*1402 | inactivated (Outdated) | - |
| `256976009` | B*1501 | inactivated (Outdated) | REPLACED BY → 1401936000 B*15:01:01:01 allele |
| `256977000` | B*1502 | inactivated (Outdated) | REPLACED BY → 1401935001 B*15:02:01:01 allele |
| `256978005` | B*1503 | inactivated (Outdated) | - |
| `256979002` | B*1504 | inactivated (Outdated) | REPLACED BY → 1401934002 B*15:04:01:01 allele |
| `256980004` | B*1801 | inactivated (Outdated) | - |
| `256981000` | B*2701 | inactivated (Outdated) | REPLACED BY → 1401933008 B*27:01 allele |
| `256982007` | B*2702 | inactivated (Outdated) | REPLACED BY → 1401932003 B*27:02:01:01 allele |
| `256983002` | B*2703 | inactivated (Outdated) | REPLACED BY → 1401931005 B*27:03:01:01 allele |
| `256984008` | B*2704 | inactivated (Outdated) | - |
| `256985009` | B*2705 | inactivated (Outdated) | - |
| `256986005` | B*2706 | inactivated (Outdated) | REPLACED BY → 1401930006 B*27:06:01:01 allele |
| `256987001` | B*2707 | inactivated (Outdated) | REPLACED BY → 1401929001 B*27:07:01:01 allele |
| `256988006` | B*3501 | inactivated (Outdated) | REPLACED BY → 1401928009 B*35:01:01:01 allele |
| `256989003` | B*3502 | inactivated (Outdated) | - |
| `256990007` | B*3503 | inactivated (Outdated) | - |
| `256991006` | B*3504 | inactivated (Outdated) | - |
| `256992004` | B*3505 | inactivated (Outdated) | REPLACED BY → 1401927004 B*35:05:01:01 allele |
| `256993009` | B*3506 | inactivated (Outdated) | REPLACED BY → 1401926008 B*35:06 allele |
| `256994003` | B*3701 | inactivated (Outdated) | - |
| `256995002` | B*3801 | inactivated (Outdated) | - |
| `256996001` | B*3901 | inactivated (Outdated) | - |
| `256997005` | B*3902 | inactivated (Outdated) | - |
| `256998000` | B*4001 | inactivated (Outdated) | - |
| `256999008` | B*4002 | inactivated (Outdated) | - |
| `257000006` | B*4003 | inactivated (Outdated) | REPLACED BY → 1401925007 B*40:03:01:01 allele |
| `257001005` | B*4004 | inactivated (Outdated) | REPLACED BY → 1401924006 B*40:04:01:01 allele |
| `257002003` | B*4005 | inactivated (Outdated) | REPLACED BY → 1401923000 B*40:05:01:01 allele |
| `257003008` | B*4101 | inactivated (Outdated) | REPLACED BY → 1401922005 B*41:01:01:01 allele |
| `257004002` | B*4201 | inactivated (Outdated) | - |
| `257005001` | B*4401 | inactivated (Erroneous) | REPLACED BY → 1401921003 B*44:02:01:01 allele |
| `257006000` | B*4402 | inactivated (Outdated) | - |
| `257007009` | B*4403 | inactivated (Outdated) | - |
| `257008004` | B*4501 | inactivated (Outdated) | REPLACED BY → 1401920002 B*45:01:01:01 allele |
| `257009007` | B*4601 | inactivated (Outdated) | - |
| `257010002` | B*4701 | inactivated (Outdated) | - |
| `257011003` | B*4801 | inactivated (Outdated) | - |
| `257012005` | B*4901 | inactivated (Outdated) | - |
| `257013000` | B*5001 | inactivated (Outdated) | - |
| `257014006` | B*5101 | inactivated (Outdated) | - |
| `257015007` | B*5103 | inactivated (Outdated) | REPLACED BY → 1401919008 B*51:03 allele |
| `257016008` | B*5201 | inactivated (Outdated) | - |
| `257017004` | B*5301 | inactivated (Outdated) | - |
| `257018009` | B*5401 | inactivated (Outdated) | REPLACED BY → 1401918000 B*54:01:01:01 allele |
| `257019001` | B*5501 | inactivated (Outdated) | - |
| `257020007` | B*5601 | inactivated (Outdated) | - |
| `257021006` | B*5602 | inactivated (Outdated) | REPLACED BY → 1401916001 B*56:02:01:01 allele |
| `257022004` | B*5701 | inactivated (Outdated) | - |
| `257023009` | B*5702 | inactivated (Outdated) | - |
| `257024003` | B*5801 | inactivated (Outdated) | REPLACED BY → 1401915002 B*58:01:01:01 allele |
| `257025002` | B*7801 | inactivated (Outdated) | REPLACED BY → 1401914003 B*78:01:01:01 allele |
| `257026001` | B*7901 | inactivated (Erroneous) | REPLACED BY → 1401913009 B*15:18:01:01 allele |
| `257027005` | Cw*0101 | inactivated (Erroneous) | REPLACED BY → 1401906009 C*01:02:01:01 allele |
| `257028000` | Cw*0102 | inactivated (Outdated) | - |
| `257029008` | Cw*0201 | inactivated (Erroneous) | REPLACED BY → 1401907000 C*02:02:02:01 allele |
| `257030003` | Cw*02021 | inactivated (Outdated) | REPLACED BY → 1401908005 C*02:02:01 allele |
| `257031004` | Cw*02022 | inactivated (Outdated) | REPLACED BY → 1401907000 C*02:02:02:01 allele |
| `257032006` | Cw*0301 | inactivated (Erroneous) | REPLACED BY → 1401911006 C*03:04:01:01 allele |
| `257033001` | Cw*0302 | inactivated (Outdated) | - |
| `257034007` | Cw*0401 | inactivated (Outdated) | - |
| `257035008` | Cw*0501 | inactivated (Outdated) | - |
| `257036009` | Cw*0601 | inactivated (Erroneous) | REPLACED BY → 1401910007 C*06:02:01:01 allele |
| `257037000` | Cw*0701 | inactivated (Outdated) | - |
| `257038005` | Cw*0702 | inactivated (Outdated) | - |
| `257039002` | Cw*0801 | inactivated (Outdated) | - |
| `257040000` | Cw*0802 | inactivated (Outdated) | - |
| `257042008` | Cw*1201 | inactivated (Erroneous) | REPLACED BY → 1401973002 C*12:02:02:01 allele |
| `257043003` | Cw*1202 | inactivated (Outdated) | - |
| `257044009` | Cw*1301 | inactivated (Outdated) | - |
| `257045005` | Cw*1401 | inactivated (Duplicate) | SAME AS → 1401909002 C*14:02:01:01 allele |
| `257046006` | DPA1*0101 | inactivated (Erroneous) | REPLACED BY → 1401902006 DPA1*01:03:01:01 allele |
| `257047002` | DPA1*0102 | inactivated (Erroneous) | REPLACED BY → 1401902006 DPA1*01:03:01:01 allele |
| `257048007` | DPA1*0103 | inactivated (Outdated) | - |
| `257049004` | DPA1*0201 | inactivated (Outdated) | - |
| `257050004` | DPA1*02021 | inactivated (Outdated) | - |
| `257051000` | DPA1*02022 | inactivated (Outdated) | REPLACED BY → 1401905008 DPA1*02:02:02:01 allele |
| `257052007` | DPA1*0301 | inactivated (Outdated) | REPLACED BY → 1401904007 DPA1*03:01:01:01 allele |
| `257053002` | DPA1*0401 | inactivated (Outdated) | REPLACED BY → 1401903001 DPA1*04:01:01:01 allele |
| `257054008` | DPB1*0101 | inactivated (Outdated) | - |
| `257055009` | DPB1*0201 | inactivated (Outdated) | - |
| `257056005` | DPB1*02011 | inactivated (Erroneous) | REPLACED BY → 1401694001 DPB1*02:01:02:01 allele |
| `257057001` | DPB1*02012 | inactivated (Outdated) | REPLACED BY → 1401760009 DPB1*02:01:02 allele |
| `257058006` | DPB1*0202 | inactivated (Outdated) | REPLACED BY → 1401753003 DPB1*02:02:01:01 allele |
| `257059003` | DPB1*0301 | inactivated (Outdated) | - |
| `257060008` | DPB1*0401 | inactivated (Outdated) | - |
| `257061007` | DPB1*0402 | inactivated (Outdated) | REPLACED BY → 1401756006 DPB1*04:02:01:01 allele |
| `257062000` | DPB1*0501 | inactivated (Outdated) | - |
| `257063005` | DPB1*0601 | inactivated (Outdated) | REPLACED BY → 1401758007 DPB1*06:01:01:01 allele |
| `257064004` | DPB1*0801 | inactivated (Outdated) | REPLACED BY → 1401761008 DPB1*08:01 allele |
| `257065003` | DPB1*0901 | inactivated (Outdated) | REPLACED BY → 1401762001 DPB1*09:01:01:01 allele |
| `257066002` | DPB1*1101 | inactivated (Outdated) | - |
| `257068001` | DPB1*1301 | inactivated (Outdated) | REPLACED BY → 1401750000 DPB1*13:01:01:01 allele |
| `257069009` | DPB1*1401 | inactivated (Outdated) | REPLACED BY → 1401749000 DPB1*14:01:01:01 allele |
| `257070005` | DPB1*1501 | inactivated (Outdated) | REPLACED BY → 1401748008 DPB1*15:01:01:01 allele |
| `257071009` | DPB1*1601 | inactivated (Outdated) | REPLACED BY → 1401747003 DPB1*16:01:01:01 allele |
| `257072002` | DPB1*1701 | inactivated (Outdated) | REPLACED BY → 1401746007 DPB1*17:01:01:01 allele |
| `257073007` | DPB1*1801 | inactivated (Outdated) | REPLACED BY → 1401745006 DPB1*18:01:01:01 allele |
| `257074001` | DPB1*1901 | inactivated (Outdated) | REPLACED BY → 1401743004 DPB1*19:01:01:01 allele |
| `257075000` | DPB1*2001 | inactivated (Outdated) | - |
| `257076004` | DPB1*2101 | inactivated (Outdated) | REPLACED BY → 1401739003 DPB1*21:01:01 allele |
| `257077008` | DPB1*2201 | inactivated (Outdated) | REPLACED BY → 1401738006 DPB1*22:01:01:01 allele |
| `257078003` | DPB1*2301 | inactivated (Outdated) | REPLACED BY → 1401737001 DPB1*23:01:01:01 allele |
| `257079006` | DPB1*2401 | inactivated (Outdated) | REPLACED BY → 1401736005 DPB1*24:01 allele |
| `257080009` | DPB1*2501 | inactivated (Outdated) | REPLACED BY → 1401695000 DPB1*25:01 allele |
| `257081008` | DPB1*2601 | inactivated (Outdated) | - |
| `257082001` | DPB1*2701 | inactivated (Outdated) | REPLACED BY → 1401583009 DPB1*27:01 allele |
| `257083006` | DPB1*2801 | inactivated (Outdated) | REPLACED BY → 1401582004 DPB1*28:01:01:01 allele |
| `257084000` | DPB1*3001 | inactivated (Outdated) | REPLACED BY → 1401581006 DPB1*30:01:01:01 allele |
| `257085004` | DPB1*3101 | inactivated (Outdated) | REPLACED BY → 1401580007 DPB1*31:01:01:01 allele |
| `257086003` | DPB1*3201 | inactivated (Outdated) | REPLACED BY → 1401579009 DPB1*32:01 allele |
| `257087007` | DPB1*3301 | inactivated (Outdated) | REPLACED BY → 1401578001 DPB1*33:01:01:01 allele |
| `257088002` | DPB1*3401 | inactivated (Outdated) | REPLACED BY → 1401577006 DPB1*34:01:01:01 allele |
| `257089005` | DPB1*3501 | inactivated (Outdated) | REPLACED BY → 1401576002 DPB1*621:01 allele |
| `257090001` | DPB1*3601 | inactivated (Outdated) | REPLACED BY → 1401575003 DPB1*36:01 allele |
| `257091002` | DQA1*0101 | inactivated (Outdated) | - |
| `257092009` | DQA1*0102 | inactivated (Outdated) | - |
| `257093004` | DQA1*0103 | inactivated (Outdated) | REPLACED BY → 1401901004 DQA1*01:03:01:01 allele |
| `257094005` | DQA1*0104 | inactivated (Outdated) | - |
| `257095006` | DQA1*0201 | inactivated (Outdated) | REPLACED BY → 1401900003 DQA1*02:01:01:01 allele |
| `257096007` | DQA1*03011 | inactivated (Outdated) | REPLACED BY → 1401899008 DQA1*03:01:01:01 allele |
| `257097003` | DQA1*03012 | inactivated (Erroneous) | REPLACED BY → 1401693007 DQA1*03:02:01:01 allele |
| `257098008` | DQA1*0302 | inactivated (Outdated) | REPLACED BY → 1401693007 DQA1*03:02:01:01 allele |
| `257099000` | DQA1*0401 | inactivated (Outdated) | - |
| `257100008` | DQA1*0501 | inactivated (Outdated) | - |
| `257101007` | DQA1*05011 | inactivated (Outdated) | REPLACED BY → 1401898000 DQA1*05:01:01:01 allele |
| `257102000` | DQA1*05012 | inactivated (Outdated) | REPLACED BY → 1401897005 DQA1*05:01:02 allele |
| `257103005` | DQA1*05013 | inactivated (Erroneous) | REPLACED BY → 1401692002 DQA1*05:01:08:01 allele |
| `257104004` | DQA1*0601 | inactivated (Outdated) | - |
| `257105003` | DQB1*0501 | inactivated (Outdated) | - |
| `257106002` | DQB1*0502 | inactivated (Outdated) | - |
| `257107006` | DQB1*05031 | inactivated (Outdated) | REPLACED BY → 1401896001 DQB1*05:03:01:01 allele |
| `257108001` | DQB1*05032 | inactivated (Outdated) | REPLACED BY → 1401895002 DQB1*05:03:02 allele |
| `257109009` | DQB1*0504 | inactivated (Outdated) | REPLACED BY → 1401894003 DQB1*05:04:01 allele |
| `257110004` | DQB1*0601 | inactivated (Outdated) | - |
| `257111000` | DQB1*0602 | inactivated (Outdated) | - |
| `257112007` | DQB1*0603 | inactivated (Outdated) | - |
| `257113002` | DQB1*0604 | inactivated (Outdated) | - |
| `257114008` | DQB1*0605 | inactivated (Outdated) | - |
| `257115009` | DQB1*0606 | inactivated (Outdated) | REPLACED BY → 1401893009 DQB1*06:06 allele |
| `257116005` | DQB1*0201 | inactivated (Outdated) | - |
| `257117001` | DQB1*0301 | inactivated (Outdated) | - |
| `257118006` | DQB1*0302 | inactivated (Outdated) | - |
| `257119003` | DQB1*03031 | inactivated (Erroneous) | REPLACED BY → 1401691009 DQB1*03:03:02:01 allele |
| `257120009` | DQB1*03032 | inactivated (Outdated) | REPLACED BY → 1401691009 DQB1*03:03:02:01 allele |
| `257121008` | DQB1*0304 | inactivated (Outdated) | REPLACED BY → 1401892004 DQB1*03:04:01:01 allele |
| `257122001` | DQB1*0401 | inactivated (Outdated) | - |
| `257123006` | DQB1*0402 | inactivated (Outdated) | REPLACED BY → 1401891006 DQB1*04:02:01:01 allele |
| `257124000` | DRB1*0101 | inactivated (Outdated) | - |
| `257125004` | DRB1*0102 | inactivated (Outdated) | - |
| `257126003` | DRB1*0103 | inactivated (Outdated) | REPLACED BY → 1401890007 DRB1*01:03:01:01 allele |
| `257127007` | DRB1*1501 | inactivated (Outdated) | - |
| `257128002` | DRB1*1502 | inactivated (Outdated) | - |
| `257129005` | DRB1*1503 | inactivated (Outdated) | - |
| `257130000` | DRB1*1601 | inactivated (Outdated) | - |
| `257132008` | DRB1*1602 | inactivated (Outdated) | - |
| `257133003` | DRB1*0301 | inactivated (Outdated) | - |
| `257134009` | DRB1*0302 | inactivated (Outdated) | - |
| `257135005` | DRB1*0303 | inactivated (Outdated) | REPLACED BY → 1401889003 DRB1*03:03 allele |
| `257136006` | DRB1*0401 | inactivated (Outdated) | - |
| `257137002` | DRB1*0402 | inactivated (Outdated) | REPLACED BY → 1401888006 DRB1*04:02:01 allele |
| `257138007` | DRB1*0403 | inactivated (Outdated) | - |
| `257139004` | DRB1*0404 | inactivated (Outdated) | - |
| `257140002` | DRB1*0405 | inactivated (Outdated) | - |
| `257141003` | DRB1*0406 | inactivated (Outdated) | - |
| `257142005` | DRB1*0407 | inactivated (Outdated) | - |
| `257143000` | DRB1*0408 | inactivated (Outdated) | - |
| `257144006` | DRB1*0409 | inactivated (Outdated) | REPLACED BY → 1401887001 DRB1*04:09:01:01 allele |
| `257145007` | DRB1*0410 | inactivated (Outdated) | REPLACED BY → 1401886005 DRB1*04:10:01 allele |
| `257146008` | DRB1*0411 | inactivated (Outdated) | REPLACED BY → 1401885009 DRB1*04:11:01:01 allele |
| `257147004` | DRB1*0412 | inactivated (Outdated) | REPLACED BY → 1401884008 DRB1*04:12 allele |
| `257148009` | DRB1*11011 | inactivated (Outdated) | REPLACED BY → 1401883002 DRB1*11:01:01:01 allele |
| `257149001` | DRB1*11012 | inactivated (Outdated) | REPLACED BY → 1401872006 DRB1*11:01:02:01 allele |
| `257150001` | DRB1*1102 | inactivated (Outdated) | - |
| `257151002` | DRB1*1103 | inactivated (Outdated) | REPLACED BY → 1401865005 DRB1*11:03:01:01 allele |
| `257152009` | DRB1*11041 | inactivated (Outdated) | REPLACED BY → 1401864009 DRB1*11:04:01:01 allele |
| `257153004` | DRB1*11042 | inactivated (Outdated) | REPLACED BY → 1401863003 DRB1*11:04:02 allele |
| `257154005` | DRB1*1105 | inactivated (Outdated) | REPLACED BY → 1401862008 DRB1*11:05 allele |
| `257155006` | DRB1*1202 | inactivated (Outdated) | - |
| `257156007` | DRB1*1301 | inactivated (Outdated) | - |
| `257157003` | DRB1*1302 | inactivated (Outdated) | - |
| `257158008` | DRB1*1303 | inactivated (Outdated) | - |
| `257160005` | DRB1*1305 | inactivated (Outdated) | REPLACED BY → 1401841007 DRB1*13:05:01:01 allele |
| `257161009` | DRB1*1306 | inactivated (Outdated) | REPLACED BY → 1401840008 DRB1*13:06 allele |
| `257162002` | DRB1*1401 | inactivated (Outdated) | - |
| `257163007` | DRB1*1402 | inactivated (Outdated) | REPLACED BY → 1401839006 DRB1*14:02:01:01 allele |
| `257164001` | DRB1*1403 | inactivated (Outdated) | - |
| `257165000` | DRB1*1404 | inactivated (Outdated) | REPLACED BY → 1401838003 DRB1*14:04:01:01 allele |
| `257166004` | DRB1*1405 | inactivated (Outdated) | - |
| `257167008` | DRB1*1406 | inactivated (Outdated) | - |
| `257168003` | DRB1*1407 | inactivated (Outdated) | - |
| `257170007` | DRB1*1408 | inactivated (Outdated) | REPLACED BY → 1401776000 DRB1*14:08 allele |
| `257171006` | DRB1*0701 | inactivated (Outdated) | - |
| `257172004` | DRB1*0702 | inactivated (Erroneous) | REPLACED BY → 1401690005 DRB1*07:01:01:01 allele |
| `257173009` | DRB1*0801 | inactivated (Outdated) | - |
| `257174003` | DRB1*08021 | inactivated (Outdated) | REPLACED BY → 1401772003 DRB1*08:02:01:01 allele |
| `257175002` | DRB1*08022 | inactivated (Outdated) | REPLACED BY → 1401773008 DRB1*08:02:02 allele |
| `257176001` | DRB1*08031 | inactivated (Erroneous) | REPLACED BY → 1401689001 DRB1*08:03:02:01 allele |
| `257177005` | DRB1*08032 | inactivated (Outdated) | REPLACED BY → 1401689001 DRB1*08:03:02:01 allele |
| `257178000` | DRB1*0804 | inactivated (Outdated) | - |
| `257179008` | DRB1*0805 | inactivated (Outdated) | REPLACED BY → 1401766003 DRB1*08:05 allele |
| `257180006` | DRB1*09011 | inactivated (Erroneous) | REPLACED BY → 1401688009 DRB1*09:01:02:01 allele |
| `257181005` | DRB1*09012 | inactivated (Outdated) | REPLACED BY → 1401688009 DRB1*09:01:02:01 allele |
| `257182003` | DRB1*1001 | inactivated (Outdated) | - |
| `257183008` | DRB3*0101 | inactivated (Outdated) | - |
| `257184002` | DRB3*0201 | inactivated (Outdated) | REPLACED BY → 1401837008 DRB3*02:01 allele |
| `257185001` | DRB3*0202 | inactivated (Outdated) | - |
| `257186000` | DRB3*0301 | inactivated (Outdated) | - |
| `257187009` | DRB4*0101 | inactivated (Outdated) | - |
| `257188004` | DRB5*0101 | inactivated (Outdated) | - |
| `257189007` | DRB5*0102 | inactivated (Outdated) | REPLACED BY → 1401836004 DRB5*01:02:01:01 allele |
| `257190003` | DRB5*0201 | inactivated (Erroneous) | REPLACED BY → 1401687004 DRB5*02:02:01:01 allele |
| `257191004` | DRB5*0202 | inactivated (Outdated) | REPLACED BY → 1401687004 DRB5*02:02:01:01 allele |
| `260071009` | Human leukocyte antigen allele | inactivated (Outdated) | - |
| `260072002` | Human leukocyte antigen A allele | inactivated (Outdated) | REPLACED BY → 1401684006 HLA-A gene |
| `260073007` | Human leukocyte antigen B allele | inactivated (Outdated) | REPLACED BY → 1401683000 HLA-B gene |
| `260074001` | Human leukocyte antigen C allele | inactivated (Outdated) | REPLACED BY → 1401682005 HLA-C gene |
| `260075000` | Human leukocyte antigen DRB1 allele | inactivated (Outdated) | REPLACED BY → 1401673004 HLA-DRB1 gene |
| `260076004` | DRB1*1409 | inactivated (Outdated) | REPLACED BY → 1401686008 DRB1*14:09 allele |
| `260077008` | DRB1*1410 | inactivated (Outdated) | REPLACED BY → 1401685007 DRB1*14:10:01:01 allele |
| `260078003` | Human leukocyte antigen DRB3 allele | inactivated (Outdated) | REPLACED BY → 1401681003 HLA-DRB3 gene |
| `260079006` | Human leukocyte antigen DRB4 allele | inactivated (Outdated) | REPLACED BY → 1401680002 HLA-DRB4 gene |
| `260080009` | Human leukocyte antigen DRB5 allele | inactivated (Outdated) | REPLACED BY → 1401679000 HLA-DRB5 gene |
| `260081008` | Human leukocyte antigen DQA1 allele | inactivated (Outdated) | REPLACED BY → 1401678008 HLA-DQA1 gene |
| `260082001` | Human leukocyte antigen DQB1 allele | inactivated (Outdated) | REPLACED BY → 1401677003 HLA-DQB1 gene |
| `260083006` | Human leukocyte antigen DPA1 allele | inactivated (Outdated) | REPLACED BY → 1401676007 HLA-DPA1 gene |
| `260084000` | Human leukocyte antigen DPB1 allele | inactivated (Outdated) | REPLACED BY → 1401574004 HLA-DPB1 gene |
| `260085004` | DPB199*2901 | inactivated (Erroneous) | REPLACED BY → 1401675006 DPB1*29:01:01 allele |
| `264831008` | DPB1*2901 | inactivated (Outdated) | REPLACED BY → 1401675006 DPB1*29:01:01 allele |
| `278315003` | DRB1*1304 | inactivated (Duplicate) | SAME AS → 1401674005 DRB1*13:04 allele |
| `405840007` | RET proto-oncogene | inactivated (Duplicate) | SAME AS → 1401573005 RET gene |
| `725636004` | 3-ureidopropionate | inactivated (Nonconformance to editorial policy) | REPLACED BY → 709844000 N-carbamoyl-beta-alanine |

**New members (121):**

| Code | Display |
|---|---|
| `120993002` | Human herpes simplex virus antigen |
| `1397190001` | Technetium (99m-Tc) ethylenediamine N,N'-diacetic acid, hydrazinonicotinamide-Tyr3-octreotide |
| `1401555007` | Borrelia burgdorferi serotype 1 outer surface protein A antigen |
| `1401556008` | Borrelia afzelii serotype 2 outer surface protein A antigen |
| `1401557004` | Borrelia garinii serotype 3 outer surface protein A antigen |
| `1401558009` | Borrelia bavariensis serotype 4 outer surface protein A antigen |
| `1401559001` | Borrelia garinii serotype 5 outer surface protein A antigen |
| `1401560006` | Borrelia garinii serotype 6 outer surface protein A antigen |
| `1401609004` | Adagrasib |
| `1401615004` | Afamitresgene autoleucel |
| `1401620004` | Amifostine anhydrous |
| `1401628006` | Benzgalantamine |
| `1401629003` | Benzhydrocodone hydrochloride |
| `1401630008` | Benzocaine hydrochloride |
| `1401631007` | Benzgalantamine gluconate |
| `1401632000` | Betibeglogene autotemcel |
| `1401633005` | Bexagliflozin |
| `1401634004` | Bismuth tribromophenate |
| `1401635003` | Brompheniramine tannate |
| `1401636002` | Calcium saccharate |
| `1401637006` | Glucaric acid |
| `1401654003` | Beta-glucuronidase inhibitor |
| `1401727006` | Avacincaptad pegol sodium |
| `1401781009` | 5-hydroxyindole-3-acetate |
| `1401794006` | Calcium L-threonate |
| `1401795007` | Threonic acid |
| `1401809001` | Carbetapentane tannate |
| `1401810006` | Cefprozil anhydrous |
| `1401812003` | Chondroitin sulfate A sodium |
| `1401967003` | Tegomil fumarate |
| `1402177004` | Chromium nicotinate |
| `1402178009` | 4-cresyl acetate |
| `1402181004` | Chelated chromium |
| `1402187000` | Codeine polistirex |
| `1402239001` | Crinecerfont |
| `1402243002` | Corticotropin releasing factor type 1 receptor antagonist |
| `1402245009` | Daprodustat |
| `1402250003` | Dasiglucagon |
| `1402254007` | Dasiglucagon hydrochloride |
| `1402314007` | V-Y flap |

… 81 more, see the CSV.

### MINOR · `mii-vs-biobank-containertyp-sct` (pinned, filter)

MII VS Biobank Containertyp SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-containertyp-sct`  
Members: 126 → 129


**New members (3):**

| Code | Display |
|---|---|
| `1003474008` | Oral specimen collection swab |
| `1402168006` | Specimen collection swab |
| `717328001` | Oral specimen collection device |

### MINOR · `mii-vs-biobank-probenart-sct` (pinned, filter)

MII VS Biobank Probenart SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-probenart-sct`  
Members: 1843 → 1847


**New members (4):**

| Code | Display |
|---|---|
| `1397846008` | Combined genital and rectal specimen |
| `1397847004` | Combined genital and pharyngeal and rectal specimen |
| `1404538009` | Cell culture lysate specimen |
| `8021000009107` | Bacterial isolate specimen |

## Module `diagnose`

### SIGNIFICANT · `mii-vs-diagnose-bodystructure-snomed` (pinned, filter)

MII VS Diagnose BodyStructure SNOMED  
`https://www.medizininformatik-initiative.de/fhir/core/modul-diagnose/ValueSet/mii-vs-diagnose-bodystructure-snomed`  
Members: 45088 → 45366


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `420329002` | Bone structure of malleus | inactivated (Duplicate) | SAME AS → 34080009 Malleus structure |
| `421793000` | Bone structure of incus | inactivated (Duplicate) | SAME AS → 35395007 Incus structure |
| `422057008` | Bone structure of stapes | inactivated (Duplicate) | SAME AS → 22718006 Stapes structure |
| `422258005` | Bone structure of auditory ossicle | inactivated (Duplicate) | SAME AS → 41845008 Ear ossicle structure |
| `68801007` | Giant cell reticulosis | inactivated (Outdated) | REPLACED BY → 1295213006 Reticulohistiocytosis |
| `70839004` | Epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `727196004` | Entire epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `727838004` | Entire skin of eardrum | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `731915001` | Entire bone of malleus | inactivated (Duplicate) | SAME AS → 264090005 Entire malleus |
| `731916000` | Entire bone of incus | inactivated (Duplicate) | SAME AS → 272649008 Entire incus |
| `731918004` | Entire bone of stapes | inactivated (Duplicate) | SAME AS → 264199009 Entire stapes |
| `731919007` | Entire bone of auditory ossicle | inactivated (Duplicate) | SAME AS → 181184001 Entire ossicle of ear |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (302):**

| Code | Display |
|---|---|
| `1373338008` | Langerhans cell neoplasm |
| `1373340003` | Plasmacytoid dendritic cell neoplasm |
| `1373341004` | Histiocytic macrophage neoplasm |
| `1373346009` | MPDCP (mature plasmacytoid dendritic cell proliferation) associated with myeloid neoplasm |
| `1373377006` | Malignant dendritic cell neoplasm |
| `1373423008` | ALK-positive histiocytosis |
| `1380193004` | Mesenchymal neoplasm |
| `1380194005` | Stroma derived neoplasm of lymphoid tissue |
| `1380195006` | Mesenchymal sarcoma |
| `1380196007` | Hematopoietic sarcoma |
| `1380197003` | Splenic vascular stromal tumor |
| `1380198008` | Littoral cell angioma |
| `1380199000` | Sclerosing angiomatoid nodular transformation of spleen |
| `1380200002` | Malignant mesenchymal dendritic cell neoplasm |
| `1380408006` | EBV-positive inflammatory follicular dendritic cell sarcoma |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |
| `1399570009` | CDKN2B gene |
| `1399571008` | CERKL gene |
| `1399572001` | CES1 gene |
| `1399573006` | CFH gene |
| `1399574000` | CHD7 gene |
| `1399587006` | Structure of bony palate |
| `1399588001` | Entire bony palate |
| `1399590000` | CHIC2 gene |
| `1399591001` | CHRNA3 gene |
| `1399592008` | NLRP3 gene |
| `1399593003` | CLCN7 gene |
| `1399594009` | DNAAF3 gene |
| `1399595005` | ATP2B3 gene |
| `1399596006` | CLCN1 gene |
| `1399597002` | CLCN5 gene |
| `1399598007` | CLN3 gene |

… 262 more, see the CSV.

### SIGNIFICANT · `mii-vs-diagnose-diagnosecodes-snomed` (pinned, filter)

MII VS Diagnose Diagnose-Codes SNOMED  
`https://www.medizininformatik-initiative.de/fhir/core/modul-diagnose/ValueSet/diagnoses-sct`  
Members: 137458 → 137681


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | POSSIBLY REPLACED BY → 102556003 Pain in upper limb, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | POSSIBLY REPLACED BY → 771083005 Pain in upper arm, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 45326000 Pain of shoulder region |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 81680005 Neck pain |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | POSSIBLY REPLACED BY → 400138001 Nodular fasciitis, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `370914009` | Death or serious disability (kernicterus) associated with failure to identify and treat hyperbilirubinemia in neonates | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 370909005 Serious reportable event associated with care management, PARTIALLY EQUIVALENT TO → 419620001 Death, PARTIALLY EQUIVALENT TO → 21134002 Disability |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `61947007` | Deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 15188001 Hearing loss |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 721294001 Acquired hearing loss |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 95828007 Congenital deafness, POSSIBLY REPLACED BY → 88052002 Mutism |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | POSSIBLY REPLACED BY → 237619009 Maternally inherited diabetes and deafness, POSSIBLY REPLACED BY → 57838006 Retinitis pigmentosa-deafness syndrome |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |

**New members (298):**

| Code | Display |
|---|---|
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |
| `1373253003` | Epilepsy due to hypoxic ischemic encephalopathy |
| `1373254009` | Epilepsy due to hypoxic brain injury |
| `1373650006` | Epilepsy due to neurodegenerative dementia |
| `1373651005` | Epilepsy due to and following ischemic stroke |
| `1373652003` | Epilepsy due to and following hemorrhagic stroke |
| `1373665007` | Vascular malformation of brain |
| `1373666008` | Congenital vascular malformation of brain |
| `1373706000` | Epilepsy due to vascular malformation of brain |
| `1373783006` | Histiocytic macrophage neoplasm |
| `1373924005` | Epilepsy due to infectious disease |
| `1373925006` | Epilepsy due to infectious abscess of brain |
| `1375929002` | Abscess of brain due to infection |
| `1375930007` | Neonatal infectious disease of central nervous system |
| `1380178003` | Epilepsy due to and following stroke |
| `1381325002` | Hypoxic brain injury |
| `1381452008` | Epilepsy due to congenital vascular malformation of brain |
| `1381728002` | Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1381731001` | Perinatal fetal and/or neonatal stroke |
| `1381732008` | Perinatal fetal and/or neonatal ischemic stroke |
| `1381733003` | Perinatal fetal and/or neonatal hemorrhagic stroke |
| `1381734009` | Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1382151008` | Acute symptomatic epileptic seizure due to poisoning |
| `1388506008` | Epilepsy due to anti-leucine-rich glioma-inactivated 1 encephalitis |
| `1388507004` | Epilepsy due to anti-NMDA (N-methyl-D-aspartate) receptor encephalitis |
| `1388508009` | Epilepsy due to cerebral hemorrhage |
| `1389043008` | Epilepsy due to genetic disease |

… 258 more, see the CSV.

## Module `kardio`

### BREAKING · `mii-vs-kardio-extended-mii-diagnosecodes-snomed` (pinned, enumerated)

MII VS Kardio Extended MII DiagnoseCodes [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-extended-mii-diagnosecodes-snomed`  
Members: 137458 → 137681

- **Filter/enumerated anchor inactive:** `368009:{116676008=49755003,363698007=17401000},{246112005=24484000}`  — no successor

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | POSSIBLY REPLACED BY → 102556003 Pain in upper limb, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | POSSIBLY REPLACED BY → 771083005 Pain in upper arm, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 45326000 Pain of shoulder region |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 81680005 Neck pain |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | POSSIBLY REPLACED BY → 400138001 Nodular fasciitis, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `370914009` | Death or serious disability (kernicterus) associated with failure to identify and treat hyperbilirubinemia in neonates | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 370909005 Serious reportable event associated with care management, PARTIALLY EQUIVALENT TO → 419620001 Death, PARTIALLY EQUIVALENT TO → 21134002 Disability |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `61947007` | Deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 15188001 Hearing loss |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 721294001 Acquired hearing loss |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 95828007 Congenital deafness, POSSIBLY REPLACED BY → 88052002 Mutism |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | POSSIBLY REPLACED BY → 237619009 Maternally inherited diabetes and deafness, POSSIBLY REPLACED BY → 57838006 Retinitis pigmentosa-deafness syndrome |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |

**New members (298):**

| Code | Display |
|---|---|
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |
| `1373253003` | Epilepsy due to hypoxic ischemic encephalopathy |
| `1373254009` | Epilepsy due to hypoxic brain injury |
| `1373650006` | Epilepsy due to neurodegenerative dementia |
| `1373651005` | Epilepsy due to and following ischemic stroke |
| `1373652003` | Epilepsy due to and following hemorrhagic stroke |
| `1373665007` | Vascular malformation of brain |
| `1373666008` | Congenital vascular malformation of brain |
| `1373706000` | Epilepsy due to vascular malformation of brain |
| `1373783006` | Histiocytic macrophage neoplasm |
| `1373924005` | Epilepsy due to infectious disease |
| `1373925006` | Epilepsy due to infectious abscess of brain |
| `1375929002` | Abscess of brain due to infection |
| `1375930007` | Neonatal infectious disease of central nervous system |
| `1380178003` | Epilepsy due to and following stroke |
| `1381325002` | Hypoxic brain injury |
| `1381452008` | Epilepsy due to congenital vascular malformation of brain |
| `1381728002` | Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1381731001` | Perinatal fetal and/or neonatal stroke |
| `1381732008` | Perinatal fetal and/or neonatal ischemic stroke |
| `1381733003` | Perinatal fetal and/or neonatal hemorrhagic stroke |
| `1381734009` | Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1382151008` | Acute symptomatic epileptic seizure due to poisoning |
| `1388506008` | Epilepsy due to anti-leucine-rich glioma-inactivated 1 encephalitis |
| `1388507004` | Epilepsy due to anti-NMDA (N-methyl-D-aspartate) receptor encephalitis |
| `1388508009` | Epilepsy due to cerebral hemorrhage |
| `1389043008` | Epilepsy due to genetic disease |

… 258 more, see the CSV.

### BREAKING · `mii-vs-kardio-klappenvitium-snomedct` (pinned, enumerated, filter)

MII VS Kardio Klappenvitium [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-klappenvitium-snomedct`  
Members: 814 → 814

- **Filter/enumerated anchor inactive:** `368009:{116676008=49755003,363698007=17401000},{246112005=24484000}`  — no successor

### MINOR · `mii-vs-kardio-atherosklerotisches-ereignis-snomedct` (UNPINNED, filter)

MII VS Kardio Atherosklerotisches Ereignis [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-atherosklerotisches-ereignis-snomedct`  
Members: 372 → 373


**New members (1):**

| Code | Display |
|---|---|
| `1381732008` | Perinatal fetal and/or neonatal ischemic stroke |

## Module `lungenfunktion`

### SIGNIFICANT · `mii-vs-lufu-sct-observable` (pinned, filter)

MII VS Lufu SCT Observable  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-lungenfunktion/ValueSet/mii-vs-lufu-sct-observable`  
Members: 190 → 189


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `313221000` | Respiratory percentage | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 251880004 Respiratory measure |

### MINOR · `mii-vs-lufu-sct-findings` (pinned, filter)

MII VS Lufu SCT Findings  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-lungenfunktion/ValueSet/mii-vs-lufu-sct-findings`  
Members: 5103 → 5114


**New members (11):**

| Code | Display |
|---|---|
| `1401642003` | Discomfort in throat |
| `1404527009` | Hantavirus cardiopulmonary syndrome caused by Orthohantavirus sinnombreense |
| `1404528004` | Hantavirus cardiopulmonary syndrome caused by Orthohantavirus andesense |
| `484141000087104` | Closed fracture of left maxillary sinus |
| `484151000087101` | Closed fracture of maxillary sinus |
| `484161000087103` | Closed fracture of right maxillary sinus |
| `484171000087107` | Fracture of maxillary sinus |
| `484311000087103` | Left hemopneumothorax |
| `484321000087106` | Right hemopneumothorax |
| `484331000087108` | Left hemothorax |
| `484341000087102` | Right hemothorax |

## Module `mikrobio`

### BREAKING · `mii-vs-mikrobio-allgemeine-bestimmung-ergebnis-snomed` (pinned, enumerated)

MII VS Mikrobio Allgemeine Bestimmung Ergebnis [SNOMED]  
`https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-allgemeine-bestimmung-ergebnis-snomed`  
Members: 24678 → 24700


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `116663002` | Sin Nombre virus | inactivated (Duplicate) | SAME AS → 1389076007 Orthohantavirus sinnombreense |
| `49445003` | Genus Hantavirus | inactivated (Outdated) | REPLACED BY → 735350007 Orthohantavirus |

**New members (24):**

| Code | Display |
|---|---|
| `1401660003` | Aspergillus alliaceus |
| `1401661004` | Yersinia proxima |
| `1401662006` | Trichosporon austroamericanum |
| `1401663001` | Narasimhella hyalinospora |
| `1401664007` | Narasimhella |
| `1402103004` | Escherichia coli serotype O176:H4 |
| `1402104005` | Escherichia coli serotype O75:H1 |
| `1402105006` | Escherichia coli serotype O158:H42 |
| `1402426003` | Affinundibacterium |
| `1402432008` | Neoundibacterium |
| `1402433003` | Parundibacterium |
| `1402434009` | Profundibacterium |
| `1402435005` | Pseudundibacterium |
| `1402436006` | Cognatundibacterium |
| `1404518008` | Bandavirus bhanjanagarense |
| `1404777005` | Harzia acremonioides |
| `1404778000` | Phanerochaete livescens |
| `1406835004` | Salmonella serovar I 6,8:i:- |
| `484031000087106` | Phialophora macrospora |
| `484051000087102` | Cutaneotrichosporon cyanovorans |
| `80711000122106` | Neisseria meningitidis serogroup H |
| `80721000122100` | Neisseria meningitidis serogroup I |
| `80731000122102` | Neisseria meningitidis serogroup K |
| `80741000122105` | Neisseria meningitidis serogroup L |

### SIGNIFICANT · `mii-vs-mikrobio-organismen-snomedct` (pinned, filter)

MII VS Mikrobio Organismen [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-organismen-snomedct`  
Members: 24677 → 24699


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `116663002` | Sin Nombre virus | inactivated (Duplicate) | SAME AS → 1389076007 Orthohantavirus sinnombreense |
| `49445003` | Genus Hantavirus | inactivated (Outdated) | REPLACED BY → 735350007 Orthohantavirus |

**New members (24):**

| Code | Display |
|---|---|
| `1401660003` | Aspergillus alliaceus |
| `1401661004` | Yersinia proxima |
| `1401662006` | Trichosporon austroamericanum |
| `1401663001` | Narasimhella hyalinospora |
| `1401664007` | Narasimhella |
| `1402103004` | Escherichia coli serotype O176:H4 |
| `1402104005` | Escherichia coli serotype O75:H1 |
| `1402105006` | Escherichia coli serotype O158:H42 |
| `1402426003` | Affinundibacterium |
| `1402432008` | Neoundibacterium |
| `1402433003` | Parundibacterium |
| `1402434009` | Profundibacterium |
| `1402435005` | Pseudundibacterium |
| `1402436006` | Cognatundibacterium |
| `1404518008` | Bandavirus bhanjanagarense |
| `1404777005` | Harzia acremonioides |
| `1404778000` | Phanerochaete livescens |
| `1406835004` | Salmonella serovar I 6,8:i:- |
| `484031000087106` | Phialophora macrospora |
| `484051000087102` | Cutaneotrichosporon cyanovorans |
| `80711000122106` | Neisseria meningitidis serogroup H |
| `80721000122100` | Neisseria meningitidis serogroup I |
| `80731000122102` | Neisseria meningitidis serogroup K |
| `80741000122105` | Neisseria meningitidis serogroup L |

## Module `onko`

### SIGNIFICANT · `mii-vs-onko-koerperstruktur-sct` (UNPINNED, filter)

MII VS Onkologie Körperstruktur (SNOMED CT)  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-koerperstruktur-sct`  
Members: 45088 → 45366


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `420329002` | Bone structure of malleus | inactivated (Duplicate) | SAME AS → 34080009 Malleus structure |
| `421793000` | Bone structure of incus | inactivated (Duplicate) | SAME AS → 35395007 Incus structure |
| `422057008` | Bone structure of stapes | inactivated (Duplicate) | SAME AS → 22718006 Stapes structure |
| `422258005` | Bone structure of auditory ossicle | inactivated (Duplicate) | SAME AS → 41845008 Ear ossicle structure |
| `68801007` | Giant cell reticulosis | inactivated (Outdated) | REPLACED BY → 1295213006 Reticulohistiocytosis |
| `70839004` | Epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `727196004` | Entire epithelial layer of tympanic membrane | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `727838004` | Entire skin of eardrum | inactivated (Duplicate) | SAME AS → 727009001 Entire outer epithelial layer of tympanic membrane |
| `731915001` | Entire bone of malleus | inactivated (Duplicate) | SAME AS → 264090005 Entire malleus |
| `731916000` | Entire bone of incus | inactivated (Duplicate) | SAME AS → 272649008 Entire incus |
| `731918004` | Entire bone of stapes | inactivated (Duplicate) | SAME AS → 264199009 Entire stapes |
| `731919007` | Entire bone of auditory ossicle | inactivated (Duplicate) | SAME AS → 181184001 Entire ossicle of ear |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (302):**

| Code | Display |
|---|---|
| `1373338008` | Langerhans cell neoplasm |
| `1373340003` | Plasmacytoid dendritic cell neoplasm |
| `1373341004` | Histiocytic macrophage neoplasm |
| `1373346009` | MPDCP (mature plasmacytoid dendritic cell proliferation) associated with myeloid neoplasm |
| `1373377006` | Malignant dendritic cell neoplasm |
| `1373423008` | ALK-positive histiocytosis |
| `1380193004` | Mesenchymal neoplasm |
| `1380194005` | Stroma derived neoplasm of lymphoid tissue |
| `1380195006` | Mesenchymal sarcoma |
| `1380196007` | Hematopoietic sarcoma |
| `1380197003` | Splenic vascular stromal tumor |
| `1380198008` | Littoral cell angioma |
| `1380199000` | Sclerosing angiomatoid nodular transformation of spleen |
| `1380200002` | Malignant mesenchymal dendritic cell neoplasm |
| `1380408006` | EBV-positive inflammatory follicular dendritic cell sarcoma |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |
| `1399570009` | CDKN2B gene |
| `1399571008` | CERKL gene |
| `1399572001` | CES1 gene |
| `1399573006` | CFH gene |
| `1399574000` | CHD7 gene |
| `1399587006` | Structure of bony palate |
| `1399588001` | Entire bony palate |
| `1399590000` | CHIC2 gene |
| `1399591001` | CHRNA3 gene |
| `1399592008` | NLRP3 gene |
| `1399593003` | CLCN7 gene |
| `1399594009` | DNAAF3 gene |
| `1399595005` | ATP2B3 gene |
| `1399596006` | CLCN1 gene |
| `1399597002` | CLCN5 gene |
| `1399598007` | CLN3 gene |

… 262 more, see the CSV.

### MINOR · `mii-vs-onko-mamma-operation-sct` (UNPINNED, filter)

MII VS Onkologie Mamma Operation SNOMED CT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-mamma-operation-sct`  
Members: 368 → 369


**New members (1):**

| Code | Display |
|---|---|
| `664411000146106` | Lumpectomy of breast using implantable magnetic lesion localization marker |

## Module `patho`

### SIGNIFICANT · `mii-vs-patho-collection-method-snomed-ct` (UNPINNED, filter)

MII VS Patho Collection Method [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-collection-method-snomed-ct`  
Members: 11024 → 11032


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `66399003` | Take-down of cerebral ventricular shunt | inactivated (Duplicate) | SAME AS → 288846002 Cerebrospinal fluid shunt removal |

**New members (9):**

| Code | Display |
|---|---|
| `1401978006` | Valve-sparing aortic root replacement with reimplantation technique |
| `1401979003` | Valve-sparing aortic root replacement using remodeling technique |
| `1401980000` | Composite aortic valve and root replacement with coronary artery reimplantation |
| `1401982008` | Single-stage total aortic arch replacement with stented elephant trunk implantation |
| `1402316009` | Bronchial suction via flexible bronchoscope |
| `175339005` | Repair of aorta with subclavian flap |
| `397861001` | Bronchial suction via fiberoptic bronchoscope |
| `664411000146106` | Lumpectomy of breast using implantable magnetic lesion localization marker |
| `95141000146108` | Open aneurysmectomy of ascending aorta |

### SIGNIFICANT · `mii-vs-patho-problem-list-snomed-ct` (UNPINNED, filter)

MII VS Patho Problem List [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-problem-list-snomed-ct`  
Members: 129019 → 129241

- Content note (not a release change): anchor `409586006` Complaint was already status inactive (Nonconformance to editorial policy) under the baseline
- Content note (not a release change): anchor `248536006` Finding of functional performance and activity was already status inactive (Nonconformance to editorial policy) under the baseline

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | POSSIBLY REPLACED BY → 102556003 Pain in upper limb, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | POSSIBLY REPLACED BY → 771083005 Pain in upper arm, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 45326000 Pain of shoulder region |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | POSSIBLY REPLACED BY → 203082005 Fibromyalgia, POSSIBLY REPLACED BY → 81680005 Neck pain |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | POSSIBLY REPLACED BY → 400138001 Nodular fasciitis, POSSIBLY REPLACED BY → 203082005 Fibromyalgia |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `61947007` | Deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 15188001 Hearing loss |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 88052002 Mutism, POSSIBLY REPLACED BY → 721294001 Acquired hearing loss |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | POSSIBLY REPLACED BY → 95828007 Congenital deafness, POSSIBLY REPLACED BY → 88052002 Mutism |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | POSSIBLY REPLACED BY → 237619009 Maternally inherited diabetes and deafness, POSSIBLY REPLACED BY → 57838006 Retinitis pigmentosa-deafness syndrome |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |

**New members (296):**

| Code | Display |
|---|---|
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |
| `1373253003` | Epilepsy due to hypoxic ischemic encephalopathy |
| `1373254009` | Epilepsy due to hypoxic brain injury |
| `1373650006` | Epilepsy due to neurodegenerative dementia |
| `1373651005` | Epilepsy due to and following ischemic stroke |
| `1373652003` | Epilepsy due to and following hemorrhagic stroke |
| `1373665007` | Vascular malformation of brain |
| `1373666008` | Congenital vascular malformation of brain |
| `1373706000` | Epilepsy due to vascular malformation of brain |
| `1373783006` | Histiocytic macrophage neoplasm |
| `1373924005` | Epilepsy due to infectious disease |
| `1373925006` | Epilepsy due to infectious abscess of brain |
| `1375929002` | Abscess of brain due to infection |
| `1375930007` | Neonatal infectious disease of central nervous system |
| `1380178003` | Epilepsy due to and following stroke |
| `1381325002` | Hypoxic brain injury |
| `1381452008` | Epilepsy due to congenital vascular malformation of brain |
| `1381728002` | Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1381731001` | Perinatal fetal and/or neonatal stroke |
| `1381732008` | Perinatal fetal and/or neonatal ischemic stroke |
| `1381733003` | Perinatal fetal and/or neonatal hemorrhagic stroke |
| `1381734009` | Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1382151008` | Acute symptomatic epileptic seizure due to poisoning |
| `1388506008` | Epilepsy due to anti-leucine-rich glioma-inactivated 1 encephalitis |
| `1388507004` | Epilepsy due to anti-NMDA (N-methyl-D-aspartate) receptor encephalitis |
| `1388508009` | Epilepsy due to cerebral hemorrhage |
| `1389043008` | Epilepsy due to genetic disease |

… 256 more, see the CSV.

## Module `prozedur`

### SIGNIFICANT · `mii-vs-prozedur-prozeduren-snomedct` (pinned, filter)

MII VS Prozedur Prozeduren [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/ValueSet/procedures-sct`  
Members: 60697 → 60732


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `127803005` | Lung residual volume measurement | inactivated (Duplicate) | SAME AS → 252473009 Residual lung volume test |
| `15872003` | Injection of alcohol into retrobulbar space | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402088007 Injection of alcohol into retrobulbar space |
| `232183005` | Insertion of bone anchors for subcutaneous bone anchored hearing aid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401724004 Implantation of magnetic hearing aid bone anchor, POSSIBLY EQUIVALENT TO → 232184004 Implantation of percutaneous hearing aid bone anchor |
| `236842007` | Subcutaneous alcohol injection of the vulva | inactivated (Outdated) | - |
| `29380005` | Insertion of pessary into cervix | inactivated (Erroneous) | REPLACED BY → 1401562003 Insertion of cervical pessary into vagina |
| `307189004` | Alcohol injection of liver metastases | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258912004 Percutaneous injection of alcohol into neoplasm of liver |
| `312339003` | Stereotactic injection of alcohol to Gasserian ganglion | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402008005 Stereotactic injection of glycerol to Gasserian ganglion, POSSIBLY EQUIVALENT TO → 1402007000 Stereotactic injection of alcohol to Gasserian ganglion |
| `32845008` | Alcohol measurement, urine | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 271289006 Urine alcohol measurement, POSSIBLY EQUIVALENT TO → 1402000003 Measurement of substance with alcohol structure in urine specimen |
| `37127001` | Injection of inner ear with alcohol | inactivated (Outdated) | POSSIBLY REPLACED BY → 1402090008 Injection of inner ear with gentamicin, POSSIBLY REPLACED BY → 1402091007 Injection of inner ear with corticosteroid and/or corticosteroid derivative |
| `433717001` | Percutaneous injection of alcohol using fluoroscopic guidance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402089004 Percutaneous injection of alcohol using fluoroscopic guidance |
| `442321000` | Measurement of alcohol in blood specimen | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402001004 Measurement of substance with alcohol structure in blood specimen, POSSIBLY EQUIVALENT TO → 167009006 Blood alcohol level |
| `60196006` | Injection of alcohol into sympathetic nerve | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402014003 Injection of alcohol into sympathetic nerve |
| `63267000` | Alcohol measurement | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401999009 Measurement of substance with alcohol structure, POSSIBLY EQUIVALENT TO → 430837008 Alcohol measurement |
| `66399003` | Take-down of cerebral ventricular shunt | inactivated (Duplicate) | SAME AS → 288846002 Cerebrospinal fluid shunt removal |
| `76572000` | Measurement of lung volume | inactivated (Duplicate) | SAME AS → 252472004 Lung volume test |
| `88572002` | Injection of alcohol into nerve | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402006009 Injection of glycerol into nerve, POSSIBLY EQUIVALENT TO → 1402005008 Injection of alcohol into nerve |
| `89516003` | Spinal injection of alcohol | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402012004 Spinal injection of alcohol |

**New members (52):**

| Code | Display |
|---|---|
| `106881000146108` | Parenteral administration of iron supplement |
| `1397514001` | Patch repair of hypoplastic aortic arch |
| `1397515000` | Repair of supravalvular pulmonary trunk using patch |
| `1397516004` | Total cavopulmonary connection with intracardiac conduit |
| `1397517008` | Percutaneous transluminal repair of atrioventricular (non-mitral, non-tricuspid) valve using imaging guidance |
| `1399589009` | Assessment using Gold Coast Criteria |
| `1401561005` | Insertion of supporting pessary into vagina |
| `1401562003` | Insertion of cervical pessary into vagina |
| `1401645001` | Imaging guided transbronchial localization of lung lesion |
| `1401646000` | Imaging guided percutaneous localization of lung lesion |
| `1401724004` | Implantation of magnetic hearing aid bone anchor |
| `1401759004` | Percutaneous endoscopic cecostomy |
| `1401978006` | Valve-sparing aortic root replacement with reimplantation technique |
| `1401979003` | Valve-sparing aortic root replacement using remodeling technique |
| `1401980000` | Composite aortic valve and root replacement with coronary artery reimplantation |
| `1401982008` | Single-stage total aortic arch replacement with stented elephant trunk implantation |
| `1401999009` | Measurement of substance with alcohol structure |
| `1402000003` | Measurement of substance with alcohol structure in urine specimen |
| `1402001004` | Measurement of substance with alcohol structure in blood specimen |
| `1402005008` | Injection of alcohol into nerve |
| `1402006009` | Injection of glycerol into nerve |
| `1402007000` | Stereotactic injection of alcohol to Gasserian ganglion |
| `1402008005` | Stereotactic injection of glycerol to Gasserian ganglion |
| `1402012004` | Spinal injection of alcohol |
| `1402014003` | Injection of alcohol into sympathetic nerve |
| `1402087002` | Assessment using 10-item Eating Assessment Tool |
| `1402088007` | Injection of alcohol into retrobulbar space |
| `1402089004` | Percutaneous injection of alcohol using fluoroscopic guidance |
| `1402090008` | Injection of inner ear with gentamicin |
| `1402091007` | Injection of inner ear with corticosteroid and/or corticosteroid derivative |
| `1402107003` | Assessment using FRAIL (Fatigue, Resistance, Ambulation, Illnesses, and Loss of weight) scale |
| `1402109000` | Assessment using Fried Frailty Phenotype scale |
| `1402115000` | Pulmonary valvuloplasty of fetus |
| `1402116004` | Aortic valvuloplasty of fetus |
| `1402122008` | Assessment using Charlson Comorbidity Index |
| `1402123003` | Assessment using Strength, Assistance walking, Rising from chair, Climbing stairs and Falls questionnaire |
| `1402139005` | Repair of fetal myelomeningocele |
| `1402141006` | Radiofrequency ablation of umbilical cord |
| `1402144003` | Occlusion of umbilical cord using bipolar coagulation |
| `1402308000` | Assessment using Frailty Trait Scale-5 |

… 12 more, see the CSV.

