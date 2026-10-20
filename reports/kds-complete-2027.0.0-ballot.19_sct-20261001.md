# Terminology release impact: de.medizininformatikinitiative.kerndatensatz.complete 2027.0.0-ballot.19

| | Baseline | Target |
|---|---|---|
| ATC | 2026 | 2026 |
| ICD-10-GM | 2026 | 2026 |
| OPS | 2026 | 2026 |
| LOINC | 2.82 | 2.82 |
| SNOMED CT | 20260701 | 20261001 |
| HGNC | 20250704 | 20250704 |

Generated 2026-10-20T02:39:56 against https://ontoserver.mii-termserv.de/fhir + rf2:SnomedCT_InternationalRF2_PRODUCTION_20261001T120000Z.zip (5504 server calls).

## Summary

| Severity | ValueSets |
|---|---:|
| BREAKING | 4 |
| SIGNIFICANT | 17 |
| MINOR | 8 |
| NONE | 107 |

Severity rules: BREAKING = a member of an enumerated include or a filter anchor was inactivated, or a member became inactive; SIGNIFICANT = members dropped out of a filter-defined ValueSet or displays changed; MINOR = new members only.

Pinned ValueSets (all includes carry a version) do not change at runtime until the pin is moved; unpinned ones change with the next terminology load on the server.

## Per module

| Module | ValueSets compared | BREAKING | SIGNIFICANT | MINOR | unchanged |
|---|---:|---:|---:|---:|---:|
| bildgebung | 5 | 0 | 3 | 0 | 2 |
| biobank | 9 | 0 | 3 | 3 | 3 |
| diagnose | 2 | 0 | 2 | 0 | 0 |
| dokument | 4 | 0 | 0 | 1 | 3 |
| icu | 21 | 0 | 0 | 0 | 21 |
| kardio | 9 | 2 | 0 | 2 | 5 |
| labor | 4 | 0 | 0 | 0 | 4 |
| lungenfunktion | 12 | 0 | 2 | 0 | 10 |
| mikrobio | 22 | 1 | 1 | 0 | 20 |
| molgen | 4 | 0 | 0 | 0 | 4 |
| mtb | 4 | 0 | 0 | 0 | 4 |
| onko | 22 | 1 | 1 | 2 | 18 |
| patho | 7 | 0 | 4 | 0 | 3 |
| person | 1 | 0 | 0 | 0 | 1 |
| prozedur | 3 | 0 | 1 | 0 | 2 |
| seltene | 7 | 0 | 0 | 0 | 7 |

## Module `bildgebung`

### SIGNIFICANT · `mii-vs-bildgebung-findings-sct` (pinned, filter)

MII VS Bildgebung Findings SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/ValueSet/mii-vs-bildgebung-findings-sct`  
Members: 129012 → 129411


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `10562009` | Malignant hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373612000 Maternal disorder in labor due to malignant hypertension |
| `105709005` | Disease caused by Rhabdiasoidea | inactivated (Outdated) | - |
| `106005003` | Hypertension AND/OR vomiting complicating pregnancy childbirth AND/OR puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension, PARTIALLY EQUIVALENT TO → 90325002 Vomiting of pregnancy |
| `106008001` | Delivery AND/OR maternal condition affecting management | inactivated (Classification derived) | REPLACED BY → 1269075002 Maternal disorder during intrapartum period |
| `106009009` | Fetal condition affecting obstetrical care of mother | inactivated (Classification derived) | REPLACED BY → 70591005 Fetal disorder |
| `106010004` | Pelvic dystocia AND/OR uterine disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 79748007 Maternal dystocia, POSSIBLY EQUIVALENT TO → 12337004 Disorder of uterus, POSSIBLY EQUIVALENT TO → 1381465004 Labor dystocia |
| `10741911000119103` | Abnormal cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381664008 Abnormal cervix during antenatal and/or intrapartum period |
| `10743831000119100` | Neoplasm of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381663002 Neoplasm of uterus during antenatal and/or intrapartum period |
| `10743881000119104` | Suspected fetal abnormality affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 609520005 Disorder of fetal structure, PARTIALLY EQUIVALENT TO → 609415007 Fetal disorder suspected |
| `10749811000119108` | Obstetric anesthesia with central nervous system complication in childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `10808861000119105` | Maternal distress during childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period, POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period |
| `10835971000119109` | Anti-A sensitization in pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388946008 Maternal anti-A isoimmunization during antenatal and/or intrapartum period |
| `10853001` | Obstetrical complication of general anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380040003 Maternal disorder due to administration of general anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `10884004` | Threatened miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 6383007 Premature labor |
| `10897531000119101` | Open wound of female external genitalia | inactivated (Duplicate) | SAME AS → 210438000 Open wound of vulva |
| `10950002` | Vulval hematoma during delivery | inactivated (Duplicate) | SAME AS → 249217005 Maternal hematoma of vulva during intrapartum period |
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `111438007` | Hypertension secondary to renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373660002 Hypertension due to renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `111447004` | Placental condition affecting management of mother | inactivated (Classification derived) | REPLACED BY → 125586008 Disorder of placenta |
| `111459000` | Infection of nipple, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum |
| `1142291001` | Achromotrichia of eyebrow | inactivated (Erroneous) | REPLACED BY → 1402357002 Achromotrichia of eyebrow |
| `1145232003` | Premature grayness of hair of body | inactivated (Erroneous) | REPLACED BY → 1402358007 Premature grayness of hair of body |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1186810009` | Erythropoietic protoporphyria due to gain of function of erythroid-specific aminolevulinic acid synthase 2 | inactivated (Duplicate) | SAME AS → 1197360001 X-linked dominant erythropoietic protoporphyria |
| `11914001` | Transverse OR oblique presentation of fetus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 73161006 Transverse lie, POSSIBLY EQUIVALENT TO → 63750008 Oblique lie |
| `120001000119107` | Group B streptococcus carrier complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1397016006 Maternal group B streptococcus carrier during antenatal and/or intrapartum period |
| `1208862000` | Acquired poliosis of eyelash | inactivated (Erroneous) | REPLACED BY → 1402368002 Acquired poliosis of eyelash |
| `1220564001` | Incomplete induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373920001 Shock due to and following incomplete termination of pregnancy |
| `1220586000` | Incomplete induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373870002 Renal failure due to and following incomplete termination of pregnancy |
| `1220625008` | Incomplete induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376019002 Metabolic disorder due to and following incomplete termination of pregnancy |
| `1220626009` | Incomplete induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379949004 Pelvic inflammatory disease due to and following incomplete termination of pregnancy |
| `1220630007` | Incomplete induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376023005 Embolism due to and following incomplete termination of pregnancy |
| `1220631006` | Incomplete induced termination of pregnancy complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379950004 Delayed hemorrhage due to and following incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379951000 Excessive hemorrhage due to and following incomplete induced termination of pregnancy |
| `1220632004` | Incomplete induced termination of pregnancy complicated by damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379948007 Traumatic injury of soft tissue of pelvis during incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379947002 Traumatic injury of pelvic organ during incomplete termination of pregnancy |
| `1220657009` | Damage to pelvic organs and/or tissue due to and following complete induced termination of pregnancy | inactivated (Classification derived) | REPLACED BY → 1375964006 Traumatic injury of pelvic organ during complete termination of pregnancy |
| `1254988002` | Substance dependence in mother complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `1269073009` | Fetal disorder due to disorder of amniotic cavity and/or membrane | inactivated (Classification derived) | REPLACED BY → 1384151007 Fetal disorder due to disorder of extraembryonic membrane |
| `1269102002` | Fetal disorder due to maternal disorder during pregnancy | inactivated (Duplicate) | SAME AS → 609429008 Fetal disorder due to disease in mother |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `1269476005` | At increased risk for complication during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1392349003 At increased risk for maternal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1392350003 At increased risk for fetal disorder during intrapartum period |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `128076000` | Bone AND/OR joint disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380433009 Maternal disorder of bone and/or joint during antenatal and/or intrapartum and/or postpartum period |
| `12867002` | Fetal distress affecting management of mother | inactivated (Classification derived) | REPLACED BY → 130955003 Nonreassuring fetal status |
| `1354494000` | Induced termination of pregnancy complicated by damage to urethra | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376018005 Traumatic injury of urethra during termination of pregnancy |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | - |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | - |
| `13866000` | Fetal acidemia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382318006 Fetal acidemia |
| `13943000` | Failed attempted termination of pregnancy complicated by embolism | inactivated (Duplicate) | SAME AS → 198812002 Failed attempted termination of pregnancy with embolism |
| `14022007` | Fetal death, affecting management of mother | inactivated (Classification derived) | REPLACED BY → 276507005 Fetal death |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `14240001` | Poliosis | inactivated (Erroneous) | REPLACED BY → 1402362001 Poliosis |
| `1474004` | Hypertensive heart AND renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373630007 Disorder during maternal intrapartum period due to hypertensive heart and renal disease |
| `1538006` | Fetal malformation of central nervous system affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 9721000119107 Fetal malformation of central nervous system |
| `15406009` | Retromammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388404009 Retromammary abscess during postpartum |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `162135003` | Urine looks pale | inactivated (Duplicate) | SAME AS → 167234002 Pale urine |
| `162863004` | Body mass index 25-29 - overweight | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2, ALTERNATIVE → 1407012005 Overweight in adulthood |
| `162864005` | Body mass index 30+ - obesity | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 414916001 Obesity, ALTERNATIVE → 414915002 Obese, ALTERNATIVE → 1407009007 Adult body mass index greater than or equal to 30 kg/m2 |
| `1639007` | Abnormality of organs AND/OR soft tissues of pelvis affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 199446000 Maternal abnormality of pelvic soft tissue during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1381684007 Maternal disorder of pelvic organ during antenatal and/or intrapartum period |
| `169887003` | Birth length equal to third centile | inactivated (Erroneous) | REPLACED BY → 1411483000 Birth length equal to or less than third centile |
| `171000119107` | Maternal obesity complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380417006 Maternal obesity during antenatal and/or intrapartum and/or postpartum period |
| `17594002` | Fetal bradycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240299002 Fetal bradycardia |
| `18237006` | Parenchymatous mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388396000 Parenchymatous mastitis during postpartum |
| `18416000` | Essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373617006 Disorder during maternal intrapartum period due to essential hypertension |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `190737001` | Iminoacidopathy | inactivated (Outdated) | REPLACED BY → 37800003 Disorder of proline AND/OR hydroxyproline metabolism |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `197140007` | Secondary megacolon - congenital | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 197141006 Secondary acquired megacolon, POSSIBLY EQUIVALENT TO → 204739008 Congenital aganglionic megacolon |
| `19773009` | Infection of the breast AND/OR nipple associated with childbirth | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum, PARTIALLY EQUIVALENT TO → 1388391005 Infection of breast during postpartum |
| `198609003` | Complication of pregnancy, childbirth and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269101009 Maternal disorder during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder |
| `198617006` | Delivery of viable fetus in abdominal pregnancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 237253003 Viable fetus in abdominal pregnancy |
| `198655001` | Complete miscarriage with genital tract or pelvic infection | inactivated (Classification derived) | REPLACED BY → 1397373004 Genital tract infection due to and following complete miscarriage |
| `198656000` | Complete miscarriage with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397338001 Excessive hemorrhage due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397337006 Delayed hemorrhage due to and following complete miscarriage |
| `198657009` | Complete miscarriage with damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397364007 Traumatic injury of soft tissue of pelvis due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397371002 Traumatic injury of organ of pelvis due to and following complete miscarriage |
| `19866007` | Previous operation to cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381692003 Maternal disorder due to previous uterine cervix surgery during antenatal and/or intrapartum period |
| `198806007` | Failed attempted termination of pregnancy with genital tract or pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection, PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection |
| `198807003` | Failed attempted termination of pregnancy with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198808008` | Failed attempted termination of pregnancy with damage to pelvic organ or tissues | inactivated (Classification derived) | REPLACED BY → 1375968009 Failed attempted abortion with traumatic injury to pelvic organ |
| `198832001` | Damage to pelvic organs or tissues following abortive pregnancy | inactivated (Classification derived) | REPLACED BY → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `198874006` | Failed medical termination of pregnancy, complicated by genital tract or pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373432005 Failed medical abortion with pelvic infection, POSSIBLY EQUIVALENT TO → 1373431003 Failed medical abortion with genital tract infection |
| `198875007` | Failed medical termination of pregnancy, complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198941007` | Hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `198942000` | Benign essential hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `198949009` | Renal hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `198997005` | Pre-eclampsia or eclampsia with pre-existing hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 67359005 Pre-eclampsia added to pre-existing hypertension, PARTIALLY EQUIVALENT TO → 69909000 Eclampsia added to pre-existing hypertension |
| `199005000` | Pre-existing hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1373810005 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertension |
| `199006004` | Pre-existing hypertensive heart disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373739002 Maternal disorder during antenatal and/or intrapartum and/or postpartum period due to hypertensive heart disease |
| `199007008` | Pre-existing hypertensive heart and renal disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373732006 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertensive heart and renal disease |
| `199008003` | Pre-existing secondary hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380416002 Pre-existing secondary hypertension during antenatal and/or intrapartum and/or postpartum period |
| `199203001` | Viral hepatitis complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380412000 Maternal viral hepatitis during antenatal and/or intrapartum and/or postpartum period |
| `199257008` | Mental disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1396772000 Mental disorder during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1258898000 Mental disorder during puerperium |
| `199279003` | Orthopedic disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period |
| `199293005` | Disease of the respiratory system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1380415003 Maternal disorder of respiratory system during antenatal and/or intrapartum and/or postpartum period |
| `199294004` | Disease of the digestive system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1376007005 Maternal disorder of digestive system during antenatal and/or intrapartum and/or postpartum period |
| `199295003` | Disease of skin and subcutaneous tissue complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1380413005 Maternal disorder of skin and/or subcutaneous tissue during antenatal and/or intrapartum and/or postpartum period |
| `199296002` | Endocrine, nutritional and metabolic disease complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380430007 Maternal nutritional disorder during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1380431006 Maternal metabolic disorder during antenatal and/or intrapartum and/or postpartum period |
| `199297006` | Disease of nervous system complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380418001 Maternal disorder of nervous system during antenatal and/or intrapartum and/or postpartum period |
| `199305006` | Complications specific to multiple gestation | inactivated (Classification derived) | REPLACED BY → 1379972002 Maternal disorder due to multiple pregnancy |
| `199314001` | Normal delivery but ante- or post- natal conditions present | inactivated (Classification derived) | REPLACED BY → 48782003 Delivery normal |
| `199322008` | Triplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 64254006 Triplet pregnancy |
| `199326006` | Quadruplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 60810003 Quadruplet pregnancy |
| `199578005` | Fetal-maternal hemorrhage with antenatal problem | inactivated (Classification derived) | REPLACED BY → 71028008 Fetal-maternal hemorrhage |
| `199595002` | Labor and delivery complication by meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period |
| `199596001` | Labor and delivery complicated by fetal heart rate anomaly with meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389112004 Abnormal fetal heart rate with meconium stained amniotic fluid during intrapartum period |
| `199597005` | Labor and delivery complicated by biochemical evidence of fetal stress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389146003 Fetal distress with fetal acidosis during intrapartum period |
| `199678003` | Amniotic cavity infection with antenatal problem | inactivated (Classification derived) | REPLACED BY → 10573002 Infection of amniotic cavity |
| `199745000` | Complication occurring during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `199935005` | Fourth degree perineal tear during delivery with postnatal problem | inactivated (Classification derived) | REPLACED BY → 399031001 Fourth degree perineal laceration |
| `200046004` | Complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1381276002 Maternal disorder due to administration of anesthesia during intrapartum period |
| `200054002` | Obstetric anesthesia with cardiac complications | inactivated (Classification derived) | REPLACED BY → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200061003` | Obstetric anesthesia with central nervous system complications | inactivated (Classification derived) | REPLACED BY → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200077002` | Cardiac complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period |
| `200078007` | Central nervous system complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `200985008` | Parapsoriasis varioliformis | inactivated (Outdated) | REPLACED BY → 86487001 Acute lichenoid pityriasis |
| `201174003` | Poliosis eccentrica | inactivated (Erroneous) | REPLACED BY → 1402372003 Poliosis eccentrica |
| `201175002` | Poliosis - acquired | inactivated (Erroneous) | REPLACED BY → 1402371005 Acquired poliosis |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | - |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | - |
| `20753005` | Hypertensive heart disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373738005 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart disease |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `20845005` | Meconium in amniotic fluid affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor, PARTIALLY EQUIVALENT TO → 2132004 Meconium in amniotic fluid noted before labor in liveborn infant |
| `213202009` | Complications of attempted introduction of fertilized ovum following in vitro fertilization | inactivated (Classification derived) | REPLACED BY → 1379976004 Disorder due to embryo transfer following in vitro fertilization |
| `21346009` | Double uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381658001 Maternal congenital duplication of uterus during antenatal and/or intrapartum period |
| `22173004` | Excessive fetal growth affecting management of mother | inactivated (Classification derived) | REPLACED BY → 199616008 Large for gestation age fetus |
| `22281000119101` | Post-term pregnancy of 40 to 42 weeks | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 63503002 Gestation period, 41 weeks, POSSIBLY EQUIVALENT TO → 46230007 Gestation period, 40 weeks, POSSIBLY EQUIVALENT TO → 90968009 Post-term pregnancy |
| `22288000` | Neoplasm of cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381666005 Neoplasm of cervix uteri during antenatal and/or intrapartum period |
| `223003` | Neoplasm of body of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381678009 Neoplasm of body of uterus during antenatal and/or intrapartum period |
| `22753004` | Fetal AND/OR placental disorder affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1193535003 Fetal disorder due to placental disorder, PARTIALLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `22966008` | Hypertensive heart AND renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373627000 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart and renal disease |
| `23001005` | Stenosis AND/OR stricture of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381651007 Maternal stenosis of cervix during antenatal and/or intrapartum period |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `23171006` | Delayed AND/OR secondary postpartum hemorrhage | inactivated (Classification derived) | REPLACED BY → 156241003 Secondary postpartum hemorrhage |
| `23717007` | Benign essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `237171000` | Stenosis of vagina in pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1396771007 Stenosis of vagina during antenatal and/or intrapartum period |
| `237256006` | Disorder of pelvic size and disproportion | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199416003 Mixed feto-pelvic disproportion, POSSIBLY EQUIVALENT TO → 275426009 Pelvic disproportion, POSSIBLY EQUIVALENT TO → 25749005 Fetopelvic disproportion, POSSIBLY EQUIVALENT TO → 199397009 Cephalopelvic disproportion |
| `237330001` | Obstetric injury of urinary bladder | inactivated (Duplicate) | SAME AS → 54679003 Traumatic injury of urinary bladder during obstetric procedure |
| `237342006` | Fat embolism - obstetric | inactivated (Duplicate) | SAME AS → 2261009 Obstetrical pulmonary fat embolism |
| `238419741000119109` | Alpha thalassemia trait in mother complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373734007 Maternal disorder due to alpha thalassemia trait during antenatal and/or intrapartum period |
| `23894009` | Acne varioliformis | inactivated (Duplicate) | SAME AS → 201228005 Necrotizing lymphocytic folliculitis |
| `239884000` | Malemud disease | inactivated (Nonconformance to editorial policy) | - |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | - |
| `248663000` | Upper sternal shock | inactivated (Classification derived) | REPLACED BY → 248690009 Added heart sounds |
| `249079005` | Fontanelles presenting | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249083005 Posterior fontanelle presenting, POSSIBLY EQUIVALENT TO → 249082000 Anterior fontanelle presenting |
| `25053000` | Obstetrical central nervous system complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26078007` | Hypertension secondary to renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `26224003` | Failed attempted termination of pregnancy complicated by genital-pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection, PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection |
| `26623000` | Failed attempted termination of pregnancy complicated by delayed and/or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion |
| `267207004` | Congenital cardiovascular disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `267257007` | Labor and delivery complicated by fetal heart rate anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389144000 Abnormal fetal heart rate during intrapartum period |
| `267276009` | Obstetric anesthesia with pulmonary complications | inactivated (Classification derived) | REPLACED BY → 1379971009 Maternal pulmonary disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `267280004` | Venous complication of pregnancy and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379964004 Maternal venous disorder due to pregnancy during antenatal and/or intrapartum and/or postpartum period |
| `267322007` | Pregnancy with orthopedic problem | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 9111000119104 Musculoskeletal problem in pregnancy |
| `267350007` | Obstetric anesthesia problems | inactivated (Classification derived) | REPLACED BY → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26828006` | Rectocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381657006 Maternal rectocele during antenatal and/or intrapartum period |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `270498000` | Fetal malposition and malpresentation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 289365005 Finding of malposition of fetus, POSSIBLY EQUIVALENT TO → 80002007 Malpresentation of fetus |
| `27075004` | Venereal disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375996003 Maternal sexually transmitted infectious disease during antenatal and/or intrapartum and/or postpartum period |
| `273982004` | Obstetric problem affecting fetus | inactivated (Classification derived) | REPLACED BY → 609429008 Fetal disorder due to disease in mother |
| `273983009` | Maternal cord or placental problem | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 429260008 Disorder of umbilical cord, POSSIBLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `276263005` | Porphobilinogen deaminase deficiency | inactivated (Duplicate) | SAME AS → 234422006 Acute intermittent porphyria |
| `276580005` | Atypical isoimmunization of newborn | inactivated (Outdated) | - |
| `284670008` | Nutritionally compromised | inactivated (Duplicate) | SAME AS → 445261000124106 Impaired nutritional status |
| `28664002` | Herpes iris | inactivated (Outdated) | REPLACED BY → 1407145007 Erythema multiforme with vesiculobullous target-shaped lesion |
| `288261009` | Was malpresentation pre-labor | inactivated (Erroneous) | REPLACED BY → 80002007 Malpresentation of fetus |
| `29259002` | Malignant hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373611007 Disorder during maternal antenatal and/or intrapartum period due to malignant hypertension |
| `29421008` | Failed attempted termination of pregnancy complicated by renal failure | inactivated (Duplicate) | SAME AS → 198809000 Failed attempted termination of pregnancy with renal failure |
| `29847008` | Obstetrical complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `3033000` | Bone AND/OR joint disorder of pelvis in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380435002 Maternal disorder of pelvic ring during antenatal and/or intrapartum and/or postpartum period |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `307333004` | Rhesus isoimmunization due to anti-D | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381908006 Hemolytic disease of fetus and/or neonate due to Rhesus anti-D isoimmunization, POSSIBLY EQUIVALENT TO → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `307334005` | Rhesus isoimmunization due to anti-c | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381903002 Hemolytic disease of fetus and/or neonate due to Rhesus anti-c isoimmunization, POSSIBLY EQUIVALENT TO → 1381901000 Maternal Rhesus isoimmunization due to anti-c during antenatal and/or intrapartum period |
| `307335006` | Rhesus isoimmunization due to anti-E | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381907001 Maternal Rhesus isoimmunization due to anti-E during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 1381909003 Hemolytic disease of fetus and/or neonate due to Rhesus anti-E isoimmunization |
| `307336007` | Rhesus isoimmunization due to anti-Cw | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381906005 Hemolytic disease of fetus and/or neonate due to Rhesus anti-Cw isoimmunization, POSSIBLY EQUIVALENT TO → 1381905009 Maternal Rhesus isoimmunization due to anti-Cw during antenatal and/or intrapartum period |
| `307735008` | Complete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397334004 Excessive hemorrhage due to and following complete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397335003 Delayed hemorrhage due to and following complete inevitable miscarriage |
| `307752007` | Incomplete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397343008 Excessive hemorrhage due to and following incomplete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397344002 Delayed hemorrhage due to and following incomplete inevitable miscarriage |
| `31026002` | Obstetrical complication of sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period |
| `31383003` | Neoplasm of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381650008 Neoplasm of vagina during pregnancy |
| `31407004` | Pre-existing hypertension complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373620003 Disorder during maternal postpartum period due to pre-existing hypertension |
| `31516002` | Viral disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375992001 Maternal viral disorder during antenatal and/or intrapartum and/or postpartum period |
| `31801000146106` | Pre-existing maternal disease complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373736009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing disease |
| `31821006` | Uterine scar from previous surgery affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381695001 Maternal disorder due to uterine scar from previous surgery during antenatal and/or intrapartum period |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `32999002` | Complication of obstetrical surgical wound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380090004 Disorder of surgical wound following obstetric surgical procedure during antenatal and/or intrapartum and/or postpartum period |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `34273003` | Hypertensive heart disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373628005 Disorder during maternal postpartum period due to hypertensive heart and renal disease |
| `34694006` | Pre-existing hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `35716006` | Cracked nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258917005 Postpartum cracked nipple |
| `35746009` | Uterine fibroids affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381668006 Uterine leiomyoma during antenatal and/or intrapartum period |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `36297009` | Septate vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381660004 Maternal septate vagina during antenatal and/or intrapartum period |
| `362972006` | Disorder of labor / delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1382290001 Disorder of mother and/or fetus during intrapartum period, POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `36428009` | Gestation period, 42 weeks | inactivated (Nonconformance to editorial policy) | REPLACED BY → 90968009 Post-term pregnancy |
| `367390009` | Hypertension in the obstetric context | inactivated (Classification derived) | REPLACED BY → 288250001 Maternal hypertension |
| `36916008` | Bone AND/OR joint disorder of back in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380434003 Maternal disorder of vertebral column during antenatal and/or intrapartum and/or postpartum period |
| `370056005` | Tumor invasion into bronchus, in situ | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370057001` | Tumor invasion into bronchus, invasive | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370480003` | Hepatoportal microvascular dysplasia | inactivated (Nonconformance to editorial policy) | - |
| `372043009` | Hydrops of allantois | inactivated (Nonconformance to editorial policy) | - |
| `37618003` | Chronic hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `387833009` | Premature canities | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 297994000 Gray hair, POSSIBLY EQUIVALENT TO → 1402360009 Premature canities |
| `3885002` | ABO isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381701007 Maternal ABO isoimmunization during antenatal and/or intrapartum period |
| `39101000119109` | Pregnancy with isoimmunization from irregular blood group incompatibility | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381698004 Maternal irregular blood group isoimmunization during antenatal and/or intrapartum period |
| `39727004` | Hypertension secondary to renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373624007 Disorder during maternal postpartum period due to renal hypertension |
| `39763004` | Abnormal glucose tolerance in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 372046001 Glucose tolerance test during pregnancy, childbirth and puerperium outside reference range |
| `397949005` | Poor fetal growth affecting management | inactivated (Classification derived) | REPLACED BY → 22033007 Fetal growth restriction |
| `398276003` | Placental insufficiency affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237292005 Placental insufficiency |
| `399363000` | Late fetal death affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237364002 Stillbirth |
| `4006006` | Fetal tachycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240298005 Fetal tachycardia |
| `4026005` | Interstitial mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388393008 Interstitial mastitis during postpartum |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `40609001` | Infectious disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1376002004 Maternal infection during antenatal and/or intrapartum and/or postpartum period |
| `408512008` | Body mass index 40+ - severely obese | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407010002 Adult body mass index greater than or equal to 40 kg/m2, ALTERNATIVE → 83911000119104 Severe obesity |
| `41215002` | Congenital abnormality of uterus, affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381683001 Maternal disorder due to congenital abnormality of uterus during antenatal and/or intrapartum period |
| `412768003` | Body mass index 20-24 - normal | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 43664005 Normal weight, ALTERNATIVE → 1407013000 Adult body mass index 18.5-24.9 kg/m2 |
| `413567003` | Aplastic anemia associated with pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379966002 Maternal aplastic anemia during antenatal and/or intrapartum period |
| `415110002` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 415112005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 109989006 Multiple myeloma |
| `41527003` | Glycogen storage disease type VIII | inactivated (Outdated) | REPLACED BY → 235908005 Glycogen phosphorylase kinase deficiency |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `42537006` | Secondary perineal tear in the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 6234006 Second degree perineal laceration |
| `42686001` | Fetal chromosomal abnormality affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 267253006 Fetal chromosomal abnormality |
| `427090001` | Body mass index less than 16.5 | inactivated (Outdated) | REPLACED BY → 1407014006 Adult body mass index less than 18.5 kg/m2 |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `428530009` | Heterozygous sitosterolemia | inactivated (Erroneous) | REPLACED BY → 1409234007 Compound heterozygous sitosterolemia |
| `43329005` | Infestation by Knemidokoptes pilae | inactivated (Nonconformance to editorial policy) | - |
| `43651009` | Acquired stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381681004 Maternal disorder due to acquired stenosis of vagina during antenatal and/or intrapartum period |
| `43970002` | Congenital stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381682006 Maternal disorder due to congenital stenosis of vagina during antenatal and/or intrapartum period |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `443006` | Cystocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381656002 Maternal cystocele during antenatal and/or intrapartum period |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `44795003` | Rhesus isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381697009 Maternal Rhesus isoimmunization during antenatal and/or intrapartum period |
| `45079001` | Acromion left anterior position | inactivated (Duplicate) | SAME AS → 249108000 Shoulder left anterior position |
| `45759004` | Rigid perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381659009 Rigid perineum during antenatal and/or intrapartum period |
| `45828008` | Anemia in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 156140005 Maternal anemia during antenatal and/or intrapartum and/or postpartum period |
| `46273003` | Abscess of nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388401001 Abscess of nipple during postpartum |
| `473429002` | Tuberculoma of spinal cord confirmed | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1411612005 Tuberculoma of spinal cord confirmed |
| `47507006` | Rieger anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 417604002 Axenfeld-Rieger syndrome, POSSIBLY EQUIVALENT TO → 1416355004 Rieger anomaly |
| `4783006` | Maternal diabetes mellitus with hypoglycemia affecting fetus OR newborn | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388261002 Disorder of fetus due to hypoglycemia of mother with diabetes mellitus, PARTIALLY EQUIVALENT TO → 1388262009 Disorder of neonate due to hypoglycemia of mother with diabetes mellitus |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `48200009` | Bone AND/OR joint disorder of lower extremities in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380436001 Maternal musculoskeletal disorder of lower limb during antenatal and/or intrapartum and/or postpartum period |
| `48485000` | Miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 10761191000119104 Preterm labor in third trimester with preterm delivery in third trimester |
| `48552006` | Hypertension secondary to renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension |
| `48739004` | Miscarriage with cardiac arrest and/or cardiac failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10760181000119109 Cardiac arrest due to miscarriage, PARTIALLY EQUIVALENT TO → 1397851002 Cardiac failure due to and following miscarriage |
| `49102001` | Hypertensive heart AND renal disease in obstetric context | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373667004 Pre-existing hypertensive heart and renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `49171007` | Hypertensive renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `49342001` | Stricture of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381676008 Stricture of vagina during antenatal and/or intrapartum period |
| `49364005` | Subareolar abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388403003 Subareolar abscess during postpartum |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `50120008` | Abnormal acid-base balance affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382350001 Maternal disorder of acid-base balance during antenatal and/or intrapartum and/or postpartum period |
| `50305006` | Acquired poliosis circumscripta | inactivated (Erroneous) | REPLACED BY → 1402366003 Acquired poliosis circumscripta |
| `50557007` | Healed pelvic floor repair affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381680003 Maternal disorder due to previous pelvic floor repair during antenatal and/or intrapartum period |
| `51154004` | Obstetrical pulmonary complication of anesthesia AND/OR sedation | inactivated (Classification derived) | REPLACED BY → 1386327009 Maternal disorder of lung due to administration of anesthesia and/or sedation during intrapartum period |
| `51495008` | Cerebral anoxia following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1396086006 Maternal cerebral anoxia due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1396087002 Maternal cerebral anoxia due to and following sedation during intrapartum period |
| `541000119105` | Hypertension complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `5534004` | Senile arteritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 129573006 Atherosclerotic occlusive disease, POSSIBLY EQUIVALENT TO → 698816006 Chronic occlusion of artery of extremity |
| `55472006` | Submammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388402008 Submammary abscess during postpartum |
| `55581002` | Meconium in amniotic fluid first noted during labor AND/OR delivery in liveborn infant | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor |
| `55613002` | Engorgement of breasts associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388405005 Engorgement of breast during postpartum, POSSIBLY EQUIVALENT TO → 34831003 Neonatal engorgement of breast |
| `55704005` | Abscess of breast, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258867002 Postpartum abscess of breast |
| `56313000` | Abnormal placenta affecting management of mother | inactivated (Classification derived) | REPLACED BY → 33552005 Anomaly of placenta |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `57220000` | Obstetrical complication of local anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380039000 Maternal disorder due to administration of local anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `57873008` | Hypertensive renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373623001 Disorder during maternal postpartum period due to hypertensive renal disease |
| `5852008` | Acromion right anterior position | inactivated (Duplicate) | SAME AS → 249107005 Shoulder right anterior position |
| `58881007` | Polyp of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381662007 Polyp of cervix during antenatal and/or intrapartum period |
| `58990004` | Miscarriage complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397368005 Traumatic injury of organ of pelvis due to and following miscarriage, POSSIBLY EQUIVALENT TO → 1397367000 Traumatic injury of soft tissue of pelvis due to and following miscarriage |
| `59136001` | Thyroid disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375993006 Maternal thyroid disorder during antenatal and/or intrapartum and/or postpartum period |
| `5939002` | Failed attempted termination of pregnancy complicated by metabolic disorder | inactivated (Duplicate) | SAME AS → 198810005 Failed attempted termination of pregnancy with metabolic disorder |
| `59733002` | Hypertensive heart disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373818003 Disorder during maternal intrapartum period due to pre-existing hypertensive heart disease |
| `59919008` | Failed attempted termination of pregnancy with complication | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 49416000 Failed attempted termination of pregnancy |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `609447002` | Induced termination of pregnancy complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `609449004` | Induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373901003 Embolism due to and following termination of pregnancy |
| `609450004` | Induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379953002 Pelvic inflammatory disease due to and following termination of pregnancy |
| `609451000` | Induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373900002 Metabolic disorder due to and following termination of pregnancy |
| `609452007` | Induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373872005 Renal failure due to and following termination of pregnancy |
| `609453002` | Induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609454008` | Induced termination of pregnancy complicated by acute necrosis of liver | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379940000 Acute necrosis of liver due to induced termination of pregnancy |
| `609455009` | Induced termination of pregnancy complicated by acute renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376024004 Acute renal failure due to and following termination of pregnancy |
| `609456005` | Induced termination of pregnancy complicated by afibrinogenemia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376015008 Afibrinogenemia due to induced termination of pregnancy |
| `609457001` | Induced termination of pregnancy complicated by air embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373908009 Air embolism due to and following termination of pregnancy |
| `609458006` | Induced termination of pregnancy complicated by amniotic fluid embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379939002 Amniotic fluid embolism due to and following termination of pregnancy |
| `609459003` | Induced termination of pregnancy complicated by blood-clot embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376026002 Thromboembolism due to and following termination of pregnancy |
| `609461007` | Induced termination of pregnancy complicated by cerebral anoxia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376016009 Cerebral anoxia due to induced termination of pregnancy |
| `609462000` | Induced termination of pregnancy complicated by defibrination syndrome | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379937000 Disseminated intravascular coagulation due to induced termination of pregnancy |
| `609463005` | Induced termination of pregnancy complicated by electrolyte imbalance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379932006 Electrolyte imbalance due to induced termination of pregnancy |
| `609464004` | Induced termination of pregnancy complicated by endometritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373904006 Endometritis due to induced termination of pregnancy |
| `609465003` | Induced termination of pregnancy complicated by fat embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373907004 Fat embolism due to and following termination of pregnancy |
| `609466002` | Induced termination of pregnancy complicated by intravascular hemolysis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379954008 Intravascular hemolysis due to induced termination of pregnancy |
| `609467006` | Induced termination of pregnancy complicated by laceration of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376027006 Laceration of intestine during termination of pregnancy |
| `609468001` | Induced termination of pregnancy complicated by laceration of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379942008 Laceration of broad ligament during termination of pregnancy |
| `609469009` | Induced termination of pregnancy complicated by laceration of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376029009 Laceration of cervix during termination of pregnancy |
| `609470005` | Induced termination of pregnancy complicated by laceration of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376031000 Laceration of uterus during termination of pregnancy |
| `609471009` | Induced termination of pregnancy complicated by laceration of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376030004 Laceration of vagina during termination of pregnancy |
| `609472002` | Induced termination of pregnancy complicated by acute renal failure with oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379956005 Acute renal failure with oliguria due to induced termination of pregnancy |
| `609473007` | Induced termination of pregnancy complicated by parametritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373906008 Parametritis due to induced termination of pregnancy |
| `609474001` | Induced termination of pregnancy complicated by pelvic peritonitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376020008 Pelvic peritonitis due to induced termination of pregnancy |
| `609475000` | Induced termination of pregnancy complicated by perforation of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376028001 Traumatic perforation of intestine during termination of pregnancy |
| `609476004` | Induced termination of pregnancy complicated by perforation of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379931004 Traumatic perforation of uterine cervix during termination of pregnancy |
| `609477008` | Induced termination of pregnancy complicated by perforation of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379935008 Traumatic perforation of uterus during termination of pregnancy |
| `609478003` | Induced termination of pregnancy complicated by perforation of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379930003 Traumatic perforation of vagina during termination of pregnancy |
| `609479006` | Induced termination of pregnancy complicated by postoperative shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609480009` | Induced termination of pregnancy complicated by pulmonary embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376021007 Pulmonary embolism due to and following termination of pregnancy |
| `609482001` | Induced termination of pregnancy complicated by renal tubular necrosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379938005 Acute renal tubular necrosis due to induced termination of pregnancy |
| `609483006` | Induced termination of pregnancy complicated by salpingitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373903000 Salpingitis due to induced termination of pregnancy |
| `609484000` | Induced termination of pregnancy complicated by salpingo-oophoritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376025003 Salpingo-oophoritis due to induced termination of pregnancy |
| `609486003` | Induced termination of pregnancy complicated by septic embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373918004 Septic embolism due to and following termination of pregnancy |
| `609487007` | Induced termination of pregnancy complicated by septic shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373909001 Septic shock due to and following termination of pregnancy |
| `609489005` | Induced termination of pregnancy complicated by soap embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373912003 Soap embolism due to and following termination of pregnancy |
| `609490001` | Induced termination of pregnancy complicated by uremia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373898004 Uremia due to induced termination of pregnancy |
| `609491002` | Induced termination of pregnancy complicated by urinary tract infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379952007 Urinary tract infection due to and following induced termination of pregnancy |
| `609493004` | Induced termination of pregnancy complicated by tetanus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373899007 Tetanus due to and following induced termination of pregnancy |
| `609494005` | Induced termination of pregnancy complicated by pelvic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373875007 Disorder of pelvis due to induced termination of pregnancy |
| `609496007` | Complication occurring during pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder, POSSIBLY EQUIVALENT TO → 173300003 Disorder of pregnancy |
| `609498008` | Induced termination of pregnancy complicated by laceration of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379929008 Laceration of urinary bladder during termination of pregnancy |
| `609499000` | Induced termination of pregnancy complicated by laceration of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379943003 Laceration of periurethral tissue during termination of pregnancy |
| `609500009` | Induced termination of pregnancy complicated by perforation of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379936009 Traumatic perforation of urinary bladder during termination of pregnancy |
| `609501008` | Induced termination of pregnancy complicated by perforation of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379941001 Traumatic perforation of broad ligament during termination of pregnancy |
| `609502001` | Induced termination of pregnancy complicated by perforation of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379944009 Traumatic perforation of periurethral tissue during termination of pregnancy |
| `609503006` | Induced termination of pregnancy complicated by urinary bladder damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373915001 Traumatic injury of urinary bladder during termination of pregnancy |
| `609504000` | Induced termination of pregnancy complicated by bowel damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373905007 Traumatic injury of intestine during termination of pregnancy |
| `609505004` | Induced termination of pregnancy complicated by broad ligament damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379933001 Traumatic injury of broad ligament during termination of pregnancy |
| `609506003` | Induced termination of pregnancy complicated by cardiac arrest | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373916000 Cardiac arrest due to induced termination of pregnancy |
| `609507007` | Induced termination of pregnancy complicated by cardiac failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376017000 Cardiac failure due to induced termination of pregnancy |
| `609508002` | Induced termination of pregnancy complicated by cervix damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373911005 Traumatic injury of uterine cervix during termination of pregnancy |
| `609510000` | Induced termination of pregnancy complicated by infectious disease | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376022000 Infectious disease due to and following induced termination of pregnancy |
| `609511001` | Induced termination of pregnancy complicated by periurethral tissue damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379955009 Periurethral traumatic injury during termination of pregnancy |
| `609512008` | Induced termination of pregnancy complicated by oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373902005 Oliguria due to induced termination of pregnancy |
| `609513003` | Induced termination of pregnancy complicated by uterus damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373914002 Traumatic injury of uterus during termination of pregnancy |
| `609514009` | Induced termination of pregnancy complicated by vaginal damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373917009 Traumatic injury of vagina during termination of pregnancy |
| `61714007` | Metabolic disturbance in labor AND/OR delivery | inactivated (Classification derived) | REPLACED BY → 1395830004 Maternal metabolic disease during intrapartum period |
| `61947007` | Deaf mutism | inactivated (Outdated) | - |
| `62612003` | Fibrosis of perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381677004 Fibrosis of perineum during antenatal and/or intrapartum period |
| `62657007` | Cardiac arrest AND/OR failure following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386325001 Maternal cardiac arrest due to administration of anesthesia and/or sedation during intrapartum period, POSSIBLY EQUIVALENT TO → 1386326000 Maternal cardiac failure due to administration of anesthesia and/or sedation during intrapartum period |
| `63287004` | Benign essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373658004 Benign pre-existing essential hypertension during antenatal and/or intrapartum and/or postpartum period |
| `64171002` | Obstetrical cardiac complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386323008 Maternal disorder of heart due to administration of anesthesia and/or sedation during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1386324002 Maternal disorder of heart due to administration of anesthesia and/or sedation during intrapartum period |
| `65402008` | Pre-existing hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `65409004` | Obstetrical complication of anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `6636004` | Congenital cardiovascular disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `66709007` | Hypertensive renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373622006 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive renal disease |
| `66958002` | Isoimmunization from non-ABO, non-Rh blood-group incompatibility affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381707006 Maternal non-ABO, non-Rhesus blood-group isoimmunization during antenatal and/or intrapartum period |
| `68214002` | Lymphangitis of breast associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388394002 Lymphangitis of breast during postpartum |
| `69302000` | Termination of pregnancy on demand | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 57797005 Termination of pregnancy |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | - |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | - |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `699950009` | Anti-D isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `71639005` | Galactorrhea associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388264005 Maternal galactorrhea during postpartum period |
| `71874008` | Benign essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373569006 Maternal disorder during labor due to benign essential hypertension |
| `72022006` | Essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373656000 Pre-existing essential hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `721166000` | Human immunodeficiency virus complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380419009 Maternal human immunodeficiency virus infection during antenatal and/or intrapartum and/or postpartum period |
| `721177006` | Injury complicating pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402307005 Maternal injury during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 426997005 Maternal traumatic injury during antenatal and/or intrapartum period |
| `721201001` | Protozoal disease complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1376000007 Maternal disorder caused by Protozoa during antenatal and/or intrapartum and/or postpartum period |
| `721203003` | Sequela of complication of pregnancy childbirth and the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380411007 Disorder due to and following maternal disorder during antenatal and/or intrapartum and/or postpartum period |
| `722595002` | Overweight in adulthood with body mass index of 25 or more but less than 30 | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407012005 Overweight in adulthood, ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2 |
| `72280009` | Achromotrichia | inactivated (Erroneous) | REPLACED BY → 1402356006 Achromotrichia |
| `723091005` | Fistula of vagina and/or rectum and/or urinary bladder due to complication occurring during labor and/or delivery | inactivated (Classification derived) | REPLACED BY → 1395886004 Genital tract fistula following vaginal delivery |
| `724497009` | Disease of circulatory system complicating pregnancy childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380409003 Maternal circulatory disorder during antenatal and/or intrapartum and/or postpartum period |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `72860003` | Disorder of amniotic cavity AND/OR membrane | inactivated (Classification derived) | REPLACED BY → 609522002 Disorder of extraembryonic membrane |
| `73030000` | Hypertensive renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373661003 Pre-existing hypertensive renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `735492001` | Obstructed labor due to shoulder dystocia | inactivated (Duplicate) | SAME AS → 89700002 Shoulder girdle dystocia |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `737329004` | Damage to pelvic organs and tissues following ectopic pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397365008 Traumatic injury of soft tissue of pelvis due to and following ectopic pregnancy, POSSIBLY EQUIVALENT TO → 1397370001 Traumatic injury of organ of pelvis due to and following ectopic pregnancy |
| `737330009` | Damage to pelvic organs and tissues following molar pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397366009 Traumatic injury of soft tissue of pelvis due to and following molar pregnancy, POSSIBLY EQUIVALENT TO → 1397369002 Traumatic injury of organ of pelvis due to and following molar pregnancy |
| `73813001` | Elastosis senilis | inactivated (Outdated) | REPLACED BY → 43982006 Solar degeneration |
| `73837001` | Failed attempted termination of pregnancy with cardiac arrest and/or failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10750641000119101 Cardiac arrest due to failed attempted abortion, PARTIALLY EQUIVALENT TO → 1373227006 Failed attempted abortion with cardiac failure |
| `74227009` | Apraxic aphonia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441913003 Aphonia, POSSIBLY EQUIVALENT TO → 1407180006 Acquired apraxia of speech |
| `74955002` | Retracted nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388400000 Retraction of nipple during postpartum |
| `75150001` | Renal disease in pregnancy AND/OR puerperium without hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 733839001 Postpartum acute renal failure, PARTIALLY EQUIVALENT TO → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension, PARTIALLY EQUIVALENT TO → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `76037007` | Rigid cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381674006 Rigid cervix uteri during antenatal and/or intrapartum period |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `76751001` | Diabetes mellitus in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199223000 Maternal diabetes mellitus during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 609563008 Pre-existing diabetes mellitus in pregnancy |
| `76871004` | Previous surgery to vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381679001 Maternal disorder due to previous vaginal surgery during antenatal and/or intrapartum period |
| `77285007` | Placental infarct affecting management of mother | inactivated (Classification derived) | REPLACED BY → 268585006 Placental infarct |
| `77563000` | Obstruction by bony pelvis | inactivated (Duplicate) | SAME AS → 199757009 Obstructed labor caused by bony pelvis |
| `778075008` | Pityriasis simplex capitis | inactivated (Duplicate) | SAME AS → 400201008 Pityriasis capitis |
| `78381004` | Heart disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375991008 Maternal heart disorder during antenatal and/or intrapartum and/or postpartum period |
| `78697003` | Nonpurulent mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388395001 Nonpurulent mastitis during postpartum |
| `78808002` | Essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373618001 Disorder during maternal antenatal and/or intrapartum period due to essential hypertension |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79355007` | Hypertensive heart disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373662005 Pre-existing hypertensive heart disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | - |
| `79839005` | Perineal laceration involving vulva | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 237332009 Vulval tear, POSSIBLY EQUIVALENT TO → 1388876002 First degree laceration of perineum and laceration of vulva during vaginal delivery of fetus |
| `80818002` | Previous surgery to perineum AND/OR vulva affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1381693008 Maternal disorder due to previous procedure on perineum during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1381694002 Maternal disorder due to previous procedure on vulva during antenatal and/or intrapartum period |
| `81557008` | Parasitic disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375999005 Maternal disorder caused by parasite during antenatal and/or intrapartum and/or postpartum period |
| `81626002` | Malignant hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373657009 Malignant hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `8218002` | Chronic hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `83243004` | Rigid pelvic floor affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381673000 Rigid pelvic floor during antenatal and/or intrapartum period |
| `84007008` | Shock during AND/OR following labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381592008 Maternal shock due to and following delivery, POSSIBLY EQUIVALENT TO → 1381590000 Maternal shock during intrapartum period |
| `8445003` | Neoplasm of vulva affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381661000 Neoplasm of vulva during antenatal and/or intrapartum period |
| `84939004` | Rubella in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 270497005 Maternal rubella during antenatal and/or intrapartum and/or postpartum period |
| `85542007` | Perineal laceration involving skin | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388874004 Laceration of skin of perineum, POSSIBLY EQUIVALENT TO → 1388873005 First degree laceration of skin of perineum during vaginal delivery of fetus |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `86041002` | Pre-existing hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `87383005` | Maternal distress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period, POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period |
| `8762007` | Chronic hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `87840008` | Galactocele associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388398004 Galactocele during postpartum period |
| `88320008` | Drug tolerance | inactivated (Nonconformance to editorial policy) | REPLACED BY → 365992008 Drug tolerance - finding |
| `89672000` | Retromammary mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388397009 Retromammary mastitis during postpartum |
| `90645002` | Failed attempted termination of pregnancy without complication | inactivated (Nonconformance to editorial policy) | REPLACED BY → 49416000 Failed attempted termination of pregnancy |
| `9297001` | Bicornuate uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381667001 Bicornate uterus during antenatal and/or intrapartum period |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |
| `95606005` | Maternal drug exposure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `95607001` | Maternal drug use | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `9720009` | Cicatrix of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381675007 Cicatrix of cervix during antenatal and/or intrapartum period |

**New members (838):**

| Code | Display |
|---|---|
| `1000081000220104` | Impaired prone position tolerance in infancy |
| `1011481000220101` | Calcification of left ventricular outflow tract |
| `1011491000220103` | Rupture of aortic annulus |
| `1011661000220107` | In-hospital stroke |
| `1011671000220101` | In-hospital myocardial infarction |
| `103406000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A1 |
| `103407009` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A2 |
| `103408004` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A3 |
| `103409007` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B1 |
| `103410002` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B2 |
| `103411003` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B3 |
| `103412005` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C1 AIDS (acquired immunodeficiency syndrome) |
| `103413000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C2 AIDS (acquired immunodeficiency syndrome) |
| `103414006` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C3 AIDS (acquired immunodeficiency syndrome) |
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `11851561000119100` | Nonvenomous insect bite of posterior chest wall |
| `12206071000119108` | Osteolysis of bone adjacent to right ankle joint prosthesis |
| `12206111000119101` | Osteolysis of bone adjacent to right elbow joint prosthesis |
| `12206151000119100` | Osteolysis of bone adjacent to right finger joint prosthesis |
| `12208881000119103` | Osteolysis of bone adjacent to right shoulder joint prosthesis |
| `12217281000119101` | Osteolysis of bone adjacent to left ankle joint prosthesis |
| `12217321000119106` | Osteolysis of bone adjacent to left elbow joint prosthesis |
| `12217361000119101` | Osteolysis of bone adjacent to left finger joint prosthesis |
| `12217481000119102` | Osteolysis of bone adjacent to left shoulder joint prosthesis |
| `129769006` | Calcification cluster |
| `134098971000119103` | Osteolysis of bone adjacent to finger joint prosthesis |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |
| `1373227006` | Failed attempted abortion with cardiac failure |

… 798 more, see the CSV.

### SIGNIFICANT · `mii-vs-bildgebung-imaging-procedure-code-sct` (pinned, filter)

MII VS Bildgebung ImagingProcedure Code SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/ValueSet/mii-vs-bildgebung-imaging-procedure-code-sct`  
Members: 7563 → 9661


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1196926008` | Computed tomography triple phase study of pancreas | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1398941000 CT triple phase of pancreas with contrast |
| `1196930006` | Computed tomography dual phase study of kidney | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1399227008 CT dual phase of kidney with contrast |
| `418447007` | US scan of orbits | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 127671000146102 Ultrasonography of right orbit proper, POSSIBLY EQUIVALENT TO → 1399538009 Ultrasonography of orbit proper, POSSIBLY EQUIVALENT TO → 127661000146108 Ultrasonography of left orbit proper |
| `430266004` | Radionuclide two-phase bone imaging of wrist | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1404502002 Radionuclide two-phase imaging of bone of wrist region |
| `431895007` | Ultrasonography of graft | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401842000 Ultrasonography of vascular graft |
| `432275005` | Radionuclide imaging of bone of wrist | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1404456006 Radionuclide imaging of bone of carpus, POSSIBLY EQUIVALENT TO → 1404457002 Radionuclide imaging of bone of wrist region |
| `432396001` | Percutaneous pyeloplasty using fluoroscopic guidance | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1406753002 Fluoroscopy guided percutaneous reconstruction of ureteropelvic junction |
| `432779000` | Computed tomography dacryocystography of lacrimal canaliculus | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1397944005 CT dacryocystography of lacrimal canaliculus with contrast |
| `433023004` | Fluoroscopic dacryocystoplasty | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401820001 Fluoroscopy guided dilation of lacrimal drainage system with contrast |
| `433717001` | Percutaneous injection of alcohol using fluoroscopic guidance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402089004 Percutaneous injection of alcohol using fluoroscopic guidance |
| `438305004` | CT dual phase study of liver | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1399230001 CT dual phase of liver with contrast |
| `438591004` | Computed tomography triple phase study of liver | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1398939001 CT triple phase of liver with contrast |
| `438814001` | Fluoroscopy guided percutaneous transluminal embolization of branch of iliac vein with contrast | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1409194003 Fluoroscopy guided percutaneous transluminal embolization of common iliac vein with contrast, POSSIBLY EQUIVALENT TO → 1409196001 Fluoroscopy guided percutaneous transluminal embolization of external iliac vein with contrast, POSSIBLY EQUIVALENT TO → 1409195002 Fluoroscopy guided percutaneous transluminal embolization of internal iliac vein with contrast |
| `440514007` | CT dual phase study of pancreas | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1399231002 CT dual phase of pancreas with contrast |
| `718008007` | Three dimensional cone beam CT of mandible | inactivated (Duplicate) | SAME AS → 718007002 Cone beam CT of mandible |

**New members (2113):**

| Code | Display |
|---|---|
| `1041731000000106` | MRI of right acetabulum |
| `1046851000000102` | Magnetic resonance venography of bilateral iliac veins |
| `1077571000000106` | Magnetic resonance venography of left iliac vein |
| `1094061000000105` | Plain X-ray of tissue specimen of bilateral breasts |
| `1097641000000108` | PET MRI of bilateral breasts |
| `1097651000000106` | PET MRI of bilateral breasts with contrast |
| `1097701000000103` | PET MRI of bilateral carotid arteries |
| `1097711000000101` | PET MRI of bilateral carotid arteries with contrast |
| `1099521000000105` | Ultrasonography guided localization of iodine 125 radioactive seed to axillary lymph node |
| `1099531000000107` | Ultrasonography guided localization of iodine 125 radioactive seed to left axillary lymph node |
| `1099541000000103` | Ultrasonography guided localization of iodine 125 radioactive seed to lymph node of bilateral axilla |
| `1099551000000100` | Ultrasonography guided localization of iodine 125 radioactive seed to right axillary lymph node |
| `1099871000000106` | Fluoroscopy guided percutaneous transluminal balloon occlusion of vein of left lower limb with contrast |
| `1099881000000108` | Fluoroscopy guided percutaneous transluminal balloon occlusion of vein of right lower limb with contrast |
| `1099891000000105` | Fluoroscopy guided percutaneous transluminal balloon occlusion of vein of bilateral lower limbs with contrast |
| `1103491000000104` | PET MRI of left breast |
| `1103501000000105` | PET MRI of right breast |
| `1103511000000107` | PET MRI of left breast with contrast |
| `1103521000000101` | PET MRI of right breast with contrast |
| `1103531000000104` | PET MRI of left carotid artery |
| `1103541000000108` | PET MRI of right carotid artery |
| `1103551000000106` | PET MRI of left carotid artery with contrast |
| `1103561000000109` | PET MRI of right carotid artery with contrast |
| `1103591000000103` | Radionuclide imaging of sentinel lymph node of left breast |
| `1103601000000109` | Radionuclide imaging of sentinel lymph node of right breast |
| `1103611000000106` | Radionuclide imaging of sentinel lymph node of bilateral breasts |
| `1105061000000104` | Dual energy X-ray absorptiometry of right femur |
| `1105071000000106` | Dual energy X-ray absorptiometry of left femur |
| `1105121000000106` | Dual energy X-ray absorptiometry of bilateral femurs |
| `1105161000000103` | Dual energy X-ray absorptiometry of femur |
| `1108751000000107` | CT of bilateral adrenals with contrast washout |
| `1110811000000104` | CT of bilateral temporal bones, brain and neck with contrast |
| `1111001000000103` | CT dual phase of bilateral kidneys with contrast |
| `1111441000000108` | CT triple phase of bilateral adrenals with contrast |
| `1111801000000107` | CT triple phase of bilateral kidneys with contrast |
| `1113411000000106` | Magnetic resonance venography of right iliac vein |
| `1118531000000107` | Ultrasonography guided percutaneous fine needle aspiration biopsy of bilateral inguinal regions |
| `1123651000000100` | Ultrasonography guided percutaneous fine needle aspiration biopsy of left inguinal region |
| `1126581000000101` | Fluoroscopic arthrography of right ankle joint with contrast |
| `1126611000000107` | Fluoroscopic arthrography of left ankle joint with contrast |

… 2073 more, see the CSV.

### SIGNIFICANT · `mii-vs-bildgebung-observation-body-site-sct` (pinned, filter)

MII VS Bildgebung Observation Body Site SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/ValueSet/mii-vs-bildgebung-observation-body-site-sct`  
Members: 45088 → 45993


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `110708006` | Middle ear and mastoid cells | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure, POSSIBLY EQUIVALENT TO → 57222008 Structure of mastoid cell |
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `118974004` | Entire subdivision of female genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361386004 Entire female genital system |
| `118975003` | Entire subdivision of male genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361340001 Entire male genital system |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `18971008` | Entire iliopectineal bursa | inactivated (Duplicate) | SAME AS → 289364009 Entire iliopsoas bursa |
| `190802005` | Pelvic lipomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1416374007 Pelvic lipomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `289465009` | Structure of iliopectineal bursa | inactivated (Duplicate) | SAME AS → 9320007 Structure of iliopsoas bursa |
| `361107003` | Entire genital system | inactivated (Duplicate) | SAME AS → 278875001 Entire reproductive system |
| `363667005` | Middle ear and mastoid structure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 59066005 Mastoid structure, POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure |
| `399456004` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1187107005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 1162576007 Plasma cell myeloma |
| `405952001` | Parameningeal structure in the context of malignancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 406121007 Structure of subregion of head |
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
| `732139009` | Entire middle ear and mastoid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 181185000 Entire middle ear, POSSIBLY EQUIVALENT TO → 265784008 Entire mastoid |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (940):**

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
| `1381538009` | Structure of lumen of uterine cervix |
| `1381539001` | Entire lumen of uterine cervix |
| `1395883007` | Bone structure of finger joint region |
| `1395884001` | Bone structure of finger joint region of left hand |
| `1395885000` | Bone structure of finger joint region of right hand |
| `1395887008` | Entire bone of finger joint region |
| `1396106007` | Skin structure of left half of thoracic segment of trunk |
| `1396107003` | Skin structure of right half of thoracic segment of trunk |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399105005` | Structure of left thoracodorsal artery |
| `1399106006` | Structure of right thoracodorsal artery |
| `1399107002` | Structure of left superior epigastric artery |
| `1399108007` | Structure of right superior epigastric artery |
| `1399109004` | Structure of blood vessel of left hand |
| `1399110009` | Structure of blood vessel of right hand |
| `1399237003` | Structure of left inferior epigastric artery |
| `1399238008` | Structure of right inferior epigastric artery |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |

… 900 more, see the CSV.

## Module `biobank`

### SIGNIFICANT · `mii-vs-biobank-body-structures-sct` (pinned, filter)

MII VS Biobank BodyStructures SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-body-structures-sct`  
Members: 45088 → 45993


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `110708006` | Middle ear and mastoid cells | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure, POSSIBLY EQUIVALENT TO → 57222008 Structure of mastoid cell |
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `118974004` | Entire subdivision of female genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361386004 Entire female genital system |
| `118975003` | Entire subdivision of male genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361340001 Entire male genital system |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `18971008` | Entire iliopectineal bursa | inactivated (Duplicate) | SAME AS → 289364009 Entire iliopsoas bursa |
| `190802005` | Pelvic lipomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1416374007 Pelvic lipomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `289465009` | Structure of iliopectineal bursa | inactivated (Duplicate) | SAME AS → 9320007 Structure of iliopsoas bursa |
| `361107003` | Entire genital system | inactivated (Duplicate) | SAME AS → 278875001 Entire reproductive system |
| `363667005` | Middle ear and mastoid structure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 59066005 Mastoid structure, POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure |
| `399456004` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1187107005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 1162576007 Plasma cell myeloma |
| `405952001` | Parameningeal structure in the context of malignancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 406121007 Structure of subregion of head |
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
| `732139009` | Entire middle ear and mastoid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 181185000 Entire middle ear, POSSIBLY EQUIVALENT TO → 265784008 Entire mastoid |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (940):**

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
| `1381538009` | Structure of lumen of uterine cervix |
| `1381539001` | Entire lumen of uterine cervix |
| `1395883007` | Bone structure of finger joint region |
| `1395884001` | Bone structure of finger joint region of left hand |
| `1395885000` | Bone structure of finger joint region of right hand |
| `1395887008` | Entire bone of finger joint region |
| `1396106007` | Skin structure of left half of thoracic segment of trunk |
| `1396107003` | Skin structure of right half of thoracic segment of trunk |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399105005` | Structure of left thoracodorsal artery |
| `1399106006` | Structure of right thoracodorsal artery |
| `1399107002` | Structure of left superior epigastric artery |
| `1399108007` | Structure of right superior epigastric artery |
| `1399109004` | Structure of blood vessel of left hand |
| `1399110009` | Structure of blood vessel of right hand |
| `1399237003` | Structure of left inferior epigastric artery |
| `1399238008` | Structure of right inferior epigastric artery |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |

… 900 more, see the CSV.

### SIGNIFICANT · `mii-vs-biobank-laboratory-procedure-sct` (pinned, filter)

MII VS Biobank Laboratory Procedure SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-laboratory-procedure-sct`  
Members: 5095 → 5095


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `406911000` | Permethrin stain method | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 59209009 Toxicology testing for insecticide, ALTERNATIVE → 127790008 Staining method |

**New members (1):**

| Code | Display |
|---|---|
| `448651000124104` | Microscopic examination of cervical Papanicolaou smear and human papillomavirus deoxyribonucleic acid detection |

### SIGNIFICANT · `mii-vs-biobank-substance-additive-sct` (pinned, filter)

MII VS Biobank Substance Additive  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-substance-additive-sct`  
Members: 29284 → 29279


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1496005` | Proto-oncogene | inactivated (Duplicate) | SAME AS → 1396287006 Proto-oncogene structure |
| `2343002` | Guthion | inactivated (Duplicate) | SAME AS → 14674009 Azinphos-methyl |
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
| `412223007` | Recombinant human regular insulin | inactivated (Duplicate) | SAME AS → 420609005 Human regular insulin |
| `710220009` | Common millet | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 29178009 Common millet, POSSIBLY EQUIVALENT TO → 1411501003 Common millet seed, POSSIBLY EQUIVALENT TO → 1411504006 Common millet seed extract |
| `725636004` | 3-ureidopropionate | inactivated (Nonconformance to editorial policy) | REPLACED BY → 709844000 N-carbamoyl-beta-alanine |

**New members (276):**

| Code | Display |
|---|---|
| `1155891000168102` | Hylan G-F 20 |
| `120993002` | Human herpes simplex virus antigen |
| `1382771000168104` | Ferrous bisglycinate |
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
| `1401867002` | Chikungunya virus-like particle antigen adsorbed |
| `1401967003` | Tegomil fumarate |
| `1402177004` | Chromium nicotinate |
| `1402178009` | 4-cresyl acetate |
| `1402181004` | Chelated chromium |
| `1402187000` | Codeine polistirex |
| `1402239001` | Crinecerfont |
| `1402243002` | Corticotropin releasing factor type 1 receptor antagonist |
| `1402245009` | Daprodustat |

… 236 more, see the CSV.

### MINOR · `mii-vs-biobank-cellline-morphology-sct` (pinned, filter)

MII VS Biobank Cellinie Morphology SCT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/mii-vs-biobank-cellline-morphology-sct`  
Members: 397 → 398


**New members (1):**

| Code | Display |
|---|---|
| `390791000210107` | Gene sequence variant |

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
Members: 1843 → 1848


**New members (5):**

| Code | Display |
|---|---|
| `1397846008` | Combined genital and rectal specimen |
| `1397847004` | Combined genital and pharyngeal and rectal specimen |
| `1404538009` | Cell culture lysate specimen |
| `1409191006` | Pooled respiratory specimen |
| `8021000009107` | Bacterial isolate specimen |

## Module `diagnose`

### SIGNIFICANT · `mii-vs-diagnose-bodystructure-snomed` (pinned, filter)

MII VS Diagnose BodyStructure SNOMED  
`https://www.medizininformatik-initiative.de/fhir/core/modul-diagnose/ValueSet/mii-vs-diagnose-bodystructure-snomed`  
Members: 45088 → 45993


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `110708006` | Middle ear and mastoid cells | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure, POSSIBLY EQUIVALENT TO → 57222008 Structure of mastoid cell |
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `118974004` | Entire subdivision of female genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361386004 Entire female genital system |
| `118975003` | Entire subdivision of male genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361340001 Entire male genital system |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `18971008` | Entire iliopectineal bursa | inactivated (Duplicate) | SAME AS → 289364009 Entire iliopsoas bursa |
| `190802005` | Pelvic lipomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1416374007 Pelvic lipomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `289465009` | Structure of iliopectineal bursa | inactivated (Duplicate) | SAME AS → 9320007 Structure of iliopsoas bursa |
| `361107003` | Entire genital system | inactivated (Duplicate) | SAME AS → 278875001 Entire reproductive system |
| `363667005` | Middle ear and mastoid structure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 59066005 Mastoid structure, POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure |
| `399456004` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1187107005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 1162576007 Plasma cell myeloma |
| `405952001` | Parameningeal structure in the context of malignancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 406121007 Structure of subregion of head |
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
| `732139009` | Entire middle ear and mastoid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 181185000 Entire middle ear, POSSIBLY EQUIVALENT TO → 265784008 Entire mastoid |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (940):**

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
| `1381538009` | Structure of lumen of uterine cervix |
| `1381539001` | Entire lumen of uterine cervix |
| `1395883007` | Bone structure of finger joint region |
| `1395884001` | Bone structure of finger joint region of left hand |
| `1395885000` | Bone structure of finger joint region of right hand |
| `1395887008` | Entire bone of finger joint region |
| `1396106007` | Skin structure of left half of thoracic segment of trunk |
| `1396107003` | Skin structure of right half of thoracic segment of trunk |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399105005` | Structure of left thoracodorsal artery |
| `1399106006` | Structure of right thoracodorsal artery |
| `1399107002` | Structure of left superior epigastric artery |
| `1399108007` | Structure of right superior epigastric artery |
| `1399109004` | Structure of blood vessel of left hand |
| `1399110009` | Structure of blood vessel of right hand |
| `1399237003` | Structure of left inferior epigastric artery |
| `1399238008` | Structure of right inferior epigastric artery |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |

… 900 more, see the CSV.

### SIGNIFICANT · `mii-vs-diagnose-diagnosecodes-snomed` (pinned, filter)

MII VS Diagnose Diagnose-Codes SNOMED  
`https://www.medizininformatik-initiative.de/fhir/core/modul-diagnose/ValueSet/diagnoses-sct`  
Members: 137458 → 137864


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `10562009` | Malignant hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373612000 Maternal disorder in labor due to malignant hypertension |
| `105709005` | Disease caused by Rhabdiasoidea | inactivated (Outdated) | - |
| `106005003` | Hypertension AND/OR vomiting complicating pregnancy childbirth AND/OR puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension, PARTIALLY EQUIVALENT TO → 90325002 Vomiting of pregnancy |
| `106008001` | Delivery AND/OR maternal condition affecting management | inactivated (Classification derived) | REPLACED BY → 1269075002 Maternal disorder during intrapartum period |
| `106009009` | Fetal condition affecting obstetrical care of mother | inactivated (Classification derived) | REPLACED BY → 70591005 Fetal disorder |
| `106010004` | Pelvic dystocia AND/OR uterine disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 79748007 Maternal dystocia, POSSIBLY EQUIVALENT TO → 12337004 Disorder of uterus, POSSIBLY EQUIVALENT TO → 1381465004 Labor dystocia |
| `10741911000119103` | Abnormal cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381664008 Abnormal cervix during antenatal and/or intrapartum period |
| `10743831000119100` | Neoplasm of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381663002 Neoplasm of uterus during antenatal and/or intrapartum period |
| `10743881000119104` | Suspected fetal abnormality affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 609520005 Disorder of fetal structure, PARTIALLY EQUIVALENT TO → 609415007 Fetal disorder suspected |
| `10749811000119108` | Obstetric anesthesia with central nervous system complication in childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `10808861000119105` | Maternal distress during childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period, POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period |
| `10835971000119109` | Anti-A sensitization in pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388946008 Maternal anti-A isoimmunization during antenatal and/or intrapartum period |
| `10853001` | Obstetrical complication of general anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380040003 Maternal disorder due to administration of general anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `10884004` | Threatened miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 6383007 Premature labor |
| `10897531000119101` | Open wound of female external genitalia | inactivated (Duplicate) | SAME AS → 210438000 Open wound of vulva |
| `10950002` | Vulval hematoma during delivery | inactivated (Duplicate) | SAME AS → 249217005 Maternal hematoma of vulva during intrapartum period |
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `111438007` | Hypertension secondary to renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373660002 Hypertension due to renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `111447004` | Placental condition affecting management of mother | inactivated (Classification derived) | REPLACED BY → 125586008 Disorder of placenta |
| `111459000` | Infection of nipple, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum |
| `1142291001` | Achromotrichia of eyebrow | inactivated (Erroneous) | REPLACED BY → 1402357002 Achromotrichia of eyebrow |
| `1145232003` | Premature grayness of hair of body | inactivated (Erroneous) | REPLACED BY → 1402358007 Premature grayness of hair of body |
| `1156096005` | Past pregnancy history of complication occurring during labor and delivery | inactivated (Outdated) | REPLACED BY → 1389463009 Past pregnancy history of maternal disorder during intrapartum period |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1186810009` | Erythropoietic protoporphyria due to gain of function of erythroid-specific aminolevulinic acid synthase 2 | inactivated (Duplicate) | SAME AS → 1197360001 X-linked dominant erythropoietic protoporphyria |
| `11914001` | Transverse OR oblique presentation of fetus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 73161006 Transverse lie, POSSIBLY EQUIVALENT TO → 63750008 Oblique lie |
| `120001000119107` | Group B streptococcus carrier complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1397016006 Maternal group B streptococcus carrier during antenatal and/or intrapartum period |
| `1208862000` | Acquired poliosis of eyelash | inactivated (Erroneous) | REPLACED BY → 1402368002 Acquired poliosis of eyelash |
| `1220564001` | Incomplete induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373920001 Shock due to and following incomplete termination of pregnancy |
| `1220586000` | Incomplete induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373870002 Renal failure due to and following incomplete termination of pregnancy |
| `1220625008` | Incomplete induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376019002 Metabolic disorder due to and following incomplete termination of pregnancy |
| `1220626009` | Incomplete induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379949004 Pelvic inflammatory disease due to and following incomplete termination of pregnancy |
| `1220630007` | Incomplete induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376023005 Embolism due to and following incomplete termination of pregnancy |
| `1220631006` | Incomplete induced termination of pregnancy complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379950004 Delayed hemorrhage due to and following incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379951000 Excessive hemorrhage due to and following incomplete induced termination of pregnancy |
| `1220632004` | Incomplete induced termination of pregnancy complicated by damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379948007 Traumatic injury of soft tissue of pelvis during incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379947002 Traumatic injury of pelvic organ during incomplete termination of pregnancy |
| `1220657009` | Damage to pelvic organs and/or tissue due to and following complete induced termination of pregnancy | inactivated (Classification derived) | REPLACED BY → 1375964006 Traumatic injury of pelvic organ during complete termination of pregnancy |
| `1254988002` | Substance dependence in mother complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `1269073009` | Fetal disorder due to disorder of amniotic cavity and/or membrane | inactivated (Classification derived) | REPLACED BY → 1384151007 Fetal disorder due to disorder of extraembryonic membrane |
| `1269102002` | Fetal disorder due to maternal disorder during pregnancy | inactivated (Duplicate) | SAME AS → 609429008 Fetal disorder due to disease in mother |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `1269476005` | At increased risk for complication during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1392349003 At increased risk for maternal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1392350003 At increased risk for fetal disorder during intrapartum period |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `128076000` | Bone AND/OR joint disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380433009 Maternal disorder of bone and/or joint during antenatal and/or intrapartum and/or postpartum period |
| `12867002` | Fetal distress affecting management of mother | inactivated (Classification derived) | REPLACED BY → 130955003 Nonreassuring fetal status |
| `1354494000` | Induced termination of pregnancy complicated by damage to urethra | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376018005 Traumatic injury of urethra during termination of pregnancy |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | - |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | - |
| `1362092008` | Complication occurring during pregnancy absent | inactivated (Outdated) | REPLACED BY → 1389061004 Maternal disorder during antenatal and/or intrapartum period absent |
| `13866000` | Fetal acidemia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382318006 Fetal acidemia |
| `13943000` | Failed attempted termination of pregnancy complicated by embolism | inactivated (Duplicate) | SAME AS → 198812002 Failed attempted termination of pregnancy with embolism |
| `14022007` | Fetal death, affecting management of mother | inactivated (Classification derived) | REPLACED BY → 276507005 Fetal death |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `14240001` | Poliosis | inactivated (Erroneous) | REPLACED BY → 1402362001 Poliosis |
| `1474004` | Hypertensive heart AND renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373630007 Disorder during maternal intrapartum period due to hypertensive heart and renal disease |
| `1538006` | Fetal malformation of central nervous system affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 9721000119107 Fetal malformation of central nervous system |
| `15406009` | Retromammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388404009 Retromammary abscess during postpartum |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `161579008` | H/O: perinatal problem | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401818004 History of perinatal disorder of fetus and/or early neonate |
| `162135003` | Urine looks pale | inactivated (Duplicate) | SAME AS → 167234002 Pale urine |
| `162863004` | Body mass index 25-29 - overweight | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2, ALTERNATIVE → 1407012005 Overweight in adulthood |
| `162864005` | Body mass index 30+ - obesity | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 414916001 Obesity, ALTERNATIVE → 414915002 Obese, ALTERNATIVE → 1407009007 Adult body mass index greater than or equal to 30 kg/m2 |
| `1639007` | Abnormality of organs AND/OR soft tissues of pelvis affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 199446000 Maternal abnormality of pelvic soft tissue during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1381684007 Maternal disorder of pelvic organ during antenatal and/or intrapartum period |
| `169887003` | Birth length equal to third centile | inactivated (Erroneous) | REPLACED BY → 1411483000 Birth length equal to or less than third centile |
| `171000119107` | Maternal obesity complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380417006 Maternal obesity during antenatal and/or intrapartum and/or postpartum period |
| `17594002` | Fetal bradycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240299002 Fetal bradycardia |
| `18237006` | Parenchymatous mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388396000 Parenchymatous mastitis during postpartum |
| `18416000` | Essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373617006 Disorder during maternal intrapartum period due to essential hypertension |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `190737001` | Iminoacidopathy | inactivated (Outdated) | REPLACED BY → 37800003 Disorder of proline AND/OR hydroxyproline metabolism |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `197140007` | Secondary megacolon - congenital | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 197141006 Secondary acquired megacolon, POSSIBLY EQUIVALENT TO → 204739008 Congenital aganglionic megacolon |
| `19773009` | Infection of the breast AND/OR nipple associated with childbirth | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum, PARTIALLY EQUIVALENT TO → 1388391005 Infection of breast during postpartum |
| `198609003` | Complication of pregnancy, childbirth and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269101009 Maternal disorder during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder |
| `198617006` | Delivery of viable fetus in abdominal pregnancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 237253003 Viable fetus in abdominal pregnancy |
| `198655001` | Complete miscarriage with genital tract or pelvic infection | inactivated (Classification derived) | REPLACED BY → 1397373004 Genital tract infection due to and following complete miscarriage |
| `198656000` | Complete miscarriage with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397338001 Excessive hemorrhage due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397337006 Delayed hemorrhage due to and following complete miscarriage |
| `198657009` | Complete miscarriage with damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397364007 Traumatic injury of soft tissue of pelvis due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397371002 Traumatic injury of organ of pelvis due to and following complete miscarriage |
| `19866007` | Previous operation to cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381692003 Maternal disorder due to previous uterine cervix surgery during antenatal and/or intrapartum period |
| `198806007` | Failed attempted termination of pregnancy with genital tract or pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection, PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection |
| `198807003` | Failed attempted termination of pregnancy with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198808008` | Failed attempted termination of pregnancy with damage to pelvic organ or tissues | inactivated (Classification derived) | REPLACED BY → 1375968009 Failed attempted abortion with traumatic injury to pelvic organ |
| `198832001` | Damage to pelvic organs or tissues following abortive pregnancy | inactivated (Classification derived) | REPLACED BY → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `198874006` | Failed medical termination of pregnancy, complicated by genital tract or pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373432005 Failed medical abortion with pelvic infection, POSSIBLY EQUIVALENT TO → 1373431003 Failed medical abortion with genital tract infection |
| `198875007` | Failed medical termination of pregnancy, complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198941007` | Hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `198942000` | Benign essential hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `198949009` | Renal hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `198997005` | Pre-eclampsia or eclampsia with pre-existing hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 67359005 Pre-eclampsia added to pre-existing hypertension, PARTIALLY EQUIVALENT TO → 69909000 Eclampsia added to pre-existing hypertension |
| `199005000` | Pre-existing hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1373810005 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertension |
| `199006004` | Pre-existing hypertensive heart disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373739002 Maternal disorder during antenatal and/or intrapartum and/or postpartum period due to hypertensive heart disease |
| `199007008` | Pre-existing hypertensive heart and renal disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373732006 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertensive heart and renal disease |
| `199008003` | Pre-existing secondary hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380416002 Pre-existing secondary hypertension during antenatal and/or intrapartum and/or postpartum period |
| `199203001` | Viral hepatitis complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380412000 Maternal viral hepatitis during antenatal and/or intrapartum and/or postpartum period |
| `199257008` | Mental disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1396772000 Mental disorder during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1258898000 Mental disorder during puerperium |
| `199279003` | Orthopedic disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period |
| `199293005` | Disease of the respiratory system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1380415003 Maternal disorder of respiratory system during antenatal and/or intrapartum and/or postpartum period |
| `199294004` | Disease of the digestive system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1376007005 Maternal disorder of digestive system during antenatal and/or intrapartum and/or postpartum period |
| `199295003` | Disease of skin and subcutaneous tissue complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1380413005 Maternal disorder of skin and/or subcutaneous tissue during antenatal and/or intrapartum and/or postpartum period |
| `199296002` | Endocrine, nutritional and metabolic disease complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380430007 Maternal nutritional disorder during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1380431006 Maternal metabolic disorder during antenatal and/or intrapartum and/or postpartum period |
| `199297006` | Disease of nervous system complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380418001 Maternal disorder of nervous system during antenatal and/or intrapartum and/or postpartum period |
| `199305006` | Complications specific to multiple gestation | inactivated (Classification derived) | REPLACED BY → 1379972002 Maternal disorder due to multiple pregnancy |
| `199314001` | Normal delivery but ante- or post- natal conditions present | inactivated (Classification derived) | REPLACED BY → 48782003 Delivery normal |
| `199322008` | Triplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 64254006 Triplet pregnancy |
| `199326006` | Quadruplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 60810003 Quadruplet pregnancy |
| `199578005` | Fetal-maternal hemorrhage with antenatal problem | inactivated (Classification derived) | REPLACED BY → 71028008 Fetal-maternal hemorrhage |
| `199595002` | Labor and delivery complication by meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period |
| `199596001` | Labor and delivery complicated by fetal heart rate anomaly with meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389112004 Abnormal fetal heart rate with meconium stained amniotic fluid during intrapartum period |
| `199597005` | Labor and delivery complicated by biochemical evidence of fetal stress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389146003 Fetal distress with fetal acidosis during intrapartum period |
| `199678003` | Amniotic cavity infection with antenatal problem | inactivated (Classification derived) | REPLACED BY → 10573002 Infection of amniotic cavity |
| `199745000` | Complication occurring during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `199935005` | Fourth degree perineal tear during delivery with postnatal problem | inactivated (Classification derived) | REPLACED BY → 399031001 Fourth degree perineal laceration |
| `200046004` | Complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1381276002 Maternal disorder due to administration of anesthesia during intrapartum period |
| `200054002` | Obstetric anesthesia with cardiac complications | inactivated (Classification derived) | REPLACED BY → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200061003` | Obstetric anesthesia with central nervous system complications | inactivated (Classification derived) | REPLACED BY → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200077002` | Cardiac complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period |
| `200078007` | Central nervous system complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `200985008` | Parapsoriasis varioliformis | inactivated (Outdated) | REPLACED BY → 86487001 Acute lichenoid pityriasis |
| `201174003` | Poliosis eccentrica | inactivated (Erroneous) | REPLACED BY → 1402372003 Poliosis eccentrica |
| `201175002` | Poliosis - acquired | inactivated (Erroneous) | REPLACED BY → 1402371005 Acquired poliosis |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | - |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | - |
| `20753005` | Hypertensive heart disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373738005 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart disease |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `20845005` | Meconium in amniotic fluid affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor, PARTIALLY EQUIVALENT TO → 2132004 Meconium in amniotic fluid noted before labor in liveborn infant |
| `213202009` | Complications of attempted introduction of fertilized ovum following in vitro fertilization | inactivated (Classification derived) | REPLACED BY → 1379976004 Disorder due to embryo transfer following in vitro fertilization |
| `21346009` | Double uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381658001 Maternal congenital duplication of uterus during antenatal and/or intrapartum period |
| `22173004` | Excessive fetal growth affecting management of mother | inactivated (Classification derived) | REPLACED BY → 199616008 Large for gestation age fetus |
| `22281000119101` | Post-term pregnancy of 40 to 42 weeks | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 63503002 Gestation period, 41 weeks, POSSIBLY EQUIVALENT TO → 46230007 Gestation period, 40 weeks, POSSIBLY EQUIVALENT TO → 90968009 Post-term pregnancy |
| `22288000` | Neoplasm of cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381666005 Neoplasm of cervix uteri during antenatal and/or intrapartum period |
| `223003` | Neoplasm of body of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381678009 Neoplasm of body of uterus during antenatal and/or intrapartum period |
| `22753004` | Fetal AND/OR placental disorder affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1193535003 Fetal disorder due to placental disorder, PARTIALLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `22966008` | Hypertensive heart AND renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373627000 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart and renal disease |
| `23001005` | Stenosis AND/OR stricture of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381651007 Maternal stenosis of cervix during antenatal and/or intrapartum period |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `23171006` | Delayed AND/OR secondary postpartum hemorrhage | inactivated (Classification derived) | REPLACED BY → 156241003 Secondary postpartum hemorrhage |
| `23717007` | Benign essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `237171000` | Stenosis of vagina in pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1396771007 Stenosis of vagina during antenatal and/or intrapartum period |
| `237256006` | Disorder of pelvic size and disproportion | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199416003 Mixed feto-pelvic disproportion, POSSIBLY EQUIVALENT TO → 275426009 Pelvic disproportion, POSSIBLY EQUIVALENT TO → 25749005 Fetopelvic disproportion, POSSIBLY EQUIVALENT TO → 199397009 Cephalopelvic disproportion |
| `237330001` | Obstetric injury of urinary bladder | inactivated (Duplicate) | SAME AS → 54679003 Traumatic injury of urinary bladder during obstetric procedure |
| `237342006` | Fat embolism - obstetric | inactivated (Duplicate) | SAME AS → 2261009 Obstetrical pulmonary fat embolism |
| `238419741000119109` | Alpha thalassemia trait in mother complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373734007 Maternal disorder due to alpha thalassemia trait during antenatal and/or intrapartum period |
| `23894009` | Acne varioliformis | inactivated (Duplicate) | SAME AS → 201228005 Necrotizing lymphocytic folliculitis |
| `239884000` | Malemud disease | inactivated (Nonconformance to editorial policy) | - |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | - |
| `248663000` | Upper sternal shock | inactivated (Classification derived) | REPLACED BY → 248690009 Added heart sounds |
| `249079005` | Fontanelles presenting | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249083005 Posterior fontanelle presenting, POSSIBLY EQUIVALENT TO → 249082000 Anterior fontanelle presenting |
| `25053000` | Obstetrical central nervous system complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26078007` | Hypertension secondary to renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `26224003` | Failed attempted termination of pregnancy complicated by genital-pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection, PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection |
| `26623000` | Failed attempted termination of pregnancy complicated by delayed and/or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion |
| `267207004` | Congenital cardiovascular disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `267257007` | Labor and delivery complicated by fetal heart rate anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389144000 Abnormal fetal heart rate during intrapartum period |
| `267276009` | Obstetric anesthesia with pulmonary complications | inactivated (Classification derived) | REPLACED BY → 1379971009 Maternal pulmonary disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `267280004` | Venous complication of pregnancy and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379964004 Maternal venous disorder due to pregnancy during antenatal and/or intrapartum and/or postpartum period |
| `267322007` | Pregnancy with orthopedic problem | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 9111000119104 Musculoskeletal problem in pregnancy |
| `267350007` | Obstetric anesthesia problems | inactivated (Classification derived) | REPLACED BY → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26828006` | Rectocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381657006 Maternal rectocele during antenatal and/or intrapartum period |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `270498000` | Fetal malposition and malpresentation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 289365005 Finding of malposition of fetus, POSSIBLY EQUIVALENT TO → 80002007 Malpresentation of fetus |
| `27075004` | Venereal disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375996003 Maternal sexually transmitted infectious disease during antenatal and/or intrapartum and/or postpartum period |
| `273982004` | Obstetric problem affecting fetus | inactivated (Classification derived) | REPLACED BY → 609429008 Fetal disorder due to disease in mother |
| `273983009` | Maternal cord or placental problem | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 429260008 Disorder of umbilical cord, POSSIBLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `276263005` | Porphobilinogen deaminase deficiency | inactivated (Duplicate) | SAME AS → 234422006 Acute intermittent porphyria |
| `276580005` | Atypical isoimmunization of newborn | inactivated (Outdated) | - |
| `284670008` | Nutritionally compromised | inactivated (Duplicate) | SAME AS → 445261000124106 Impaired nutritional status |
| `28664002` | Herpes iris | inactivated (Outdated) | REPLACED BY → 1407145007 Erythema multiforme with vesiculobullous target-shaped lesion |
| `288261009` | Was malpresentation pre-labor | inactivated (Erroneous) | REPLACED BY → 80002007 Malpresentation of fetus |
| `29259002` | Malignant hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373611007 Disorder during maternal antenatal and/or intrapartum period due to malignant hypertension |
| `29421008` | Failed attempted termination of pregnancy complicated by renal failure | inactivated (Duplicate) | SAME AS → 198809000 Failed attempted termination of pregnancy with renal failure |
| `29847008` | Obstetrical complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `3033000` | Bone AND/OR joint disorder of pelvis in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380435002 Maternal disorder of pelvic ring during antenatal and/or intrapartum and/or postpartum period |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `307333004` | Rhesus isoimmunization due to anti-D | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381908006 Hemolytic disease of fetus and/or neonate due to Rhesus anti-D isoimmunization, POSSIBLY EQUIVALENT TO → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `307334005` | Rhesus isoimmunization due to anti-c | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381903002 Hemolytic disease of fetus and/or neonate due to Rhesus anti-c isoimmunization, POSSIBLY EQUIVALENT TO → 1381901000 Maternal Rhesus isoimmunization due to anti-c during antenatal and/or intrapartum period |
| `307335006` | Rhesus isoimmunization due to anti-E | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381907001 Maternal Rhesus isoimmunization due to anti-E during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 1381909003 Hemolytic disease of fetus and/or neonate due to Rhesus anti-E isoimmunization |
| `307336007` | Rhesus isoimmunization due to anti-Cw | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381906005 Hemolytic disease of fetus and/or neonate due to Rhesus anti-Cw isoimmunization, POSSIBLY EQUIVALENT TO → 1381905009 Maternal Rhesus isoimmunization due to anti-Cw during antenatal and/or intrapartum period |
| `307735008` | Complete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397334004 Excessive hemorrhage due to and following complete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397335003 Delayed hemorrhage due to and following complete inevitable miscarriage |
| `307752007` | Incomplete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397343008 Excessive hemorrhage due to and following incomplete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397344002 Delayed hemorrhage due to and following incomplete inevitable miscarriage |
| `31026002` | Obstetrical complication of sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period |
| `31383003` | Neoplasm of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381650008 Neoplasm of vagina during pregnancy |
| `31407004` | Pre-existing hypertension complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373620003 Disorder during maternal postpartum period due to pre-existing hypertension |
| `31516002` | Viral disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375992001 Maternal viral disorder during antenatal and/or intrapartum and/or postpartum period |
| `31801000146106` | Pre-existing maternal disease complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373736009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing disease |
| `31821006` | Uterine scar from previous surgery affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381695001 Maternal disorder due to uterine scar from previous surgery during antenatal and/or intrapartum period |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `32999002` | Complication of obstetrical surgical wound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380090004 Disorder of surgical wound following obstetric surgical procedure during antenatal and/or intrapartum and/or postpartum period |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `34273003` | Hypertensive heart disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373628005 Disorder during maternal postpartum period due to hypertensive heart and renal disease |
| `34694006` | Pre-existing hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `35716006` | Cracked nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258917005 Postpartum cracked nipple |
| `35746009` | Uterine fibroids affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381668006 Uterine leiomyoma during antenatal and/or intrapartum period |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `36297009` | Septate vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381660004 Maternal septate vagina during antenatal and/or intrapartum period |
| `362972006` | Disorder of labor / delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1382290001 Disorder of mother and/or fetus during intrapartum period, POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `36428009` | Gestation period, 42 weeks | inactivated (Nonconformance to editorial policy) | REPLACED BY → 90968009 Post-term pregnancy |
| `367390009` | Hypertension in the obstetric context | inactivated (Classification derived) | REPLACED BY → 288250001 Maternal hypertension |
| `36916008` | Bone AND/OR joint disorder of back in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380434003 Maternal disorder of vertebral column during antenatal and/or intrapartum and/or postpartum period |
| `370056005` | Tumor invasion into bronchus, in situ | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370057001` | Tumor invasion into bronchus, invasive | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370480003` | Hepatoportal microvascular dysplasia | inactivated (Nonconformance to editorial policy) | - |
| `370914009` | Death or serious disability (kernicterus) associated with failure to identify and treat hyperbilirubinemia in neonates | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 370909005 Serious reportable event associated with care management, PARTIALLY EQUIVALENT TO → 419620001 Death, PARTIALLY EQUIVALENT TO → 21134002 Disability |
| `372043009` | Hydrops of allantois | inactivated (Nonconformance to editorial policy) | - |
| `37618003` | Chronic hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `387833009` | Premature canities | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 297994000 Gray hair, POSSIBLY EQUIVALENT TO → 1402360009 Premature canities |
| `3885002` | ABO isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381701007 Maternal ABO isoimmunization during antenatal and/or intrapartum period |
| `39101000119109` | Pregnancy with isoimmunization from irregular blood group incompatibility | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381698004 Maternal irregular blood group isoimmunization during antenatal and/or intrapartum period |
| `39727004` | Hypertension secondary to renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373624007 Disorder during maternal postpartum period due to renal hypertension |
| `39763004` | Abnormal glucose tolerance in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 372046001 Glucose tolerance test during pregnancy, childbirth and puerperium outside reference range |
| `397949005` | Poor fetal growth affecting management | inactivated (Classification derived) | REPLACED BY → 22033007 Fetal growth restriction |
| `398276003` | Placental insufficiency affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237292005 Placental insufficiency |
| `399363000` | Late fetal death affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237364002 Stillbirth |
| `4006006` | Fetal tachycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240298005 Fetal tachycardia |
| `4026005` | Interstitial mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388393008 Interstitial mastitis during postpartum |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `40609001` | Infectious disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1376002004 Maternal infection during antenatal and/or intrapartum and/or postpartum period |
| `408512008` | Body mass index 40+ - severely obese | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407010002 Adult body mass index greater than or equal to 40 kg/m2, ALTERNATIVE → 83911000119104 Severe obesity |
| `41215002` | Congenital abnormality of uterus, affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381683001 Maternal disorder due to congenital abnormality of uterus during antenatal and/or intrapartum period |
| `412768003` | Body mass index 20-24 - normal | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 43664005 Normal weight, ALTERNATIVE → 1407013000 Adult body mass index 18.5-24.9 kg/m2 |
| `413567003` | Aplastic anemia associated with pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379966002 Maternal aplastic anemia during antenatal and/or intrapartum period |
| `415110002` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 415112005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 109989006 Multiple myeloma |
| `41527003` | Glycogen storage disease type VIII | inactivated (Outdated) | REPLACED BY → 235908005 Glycogen phosphorylase kinase deficiency |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `42537006` | Secondary perineal tear in the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 6234006 Second degree perineal laceration |
| `42686001` | Fetal chromosomal abnormality affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 267253006 Fetal chromosomal abnormality |
| `427090001` | Body mass index less than 16.5 | inactivated (Outdated) | REPLACED BY → 1407014006 Adult body mass index less than 18.5 kg/m2 |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `428530009` | Heterozygous sitosterolemia | inactivated (Erroneous) | REPLACED BY → 1409234007 Compound heterozygous sitosterolemia |
| `43329005` | Infestation by Knemidokoptes pilae | inactivated (Nonconformance to editorial policy) | - |
| `43651009` | Acquired stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381681004 Maternal disorder due to acquired stenosis of vagina during antenatal and/or intrapartum period |
| `43970002` | Congenital stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381682006 Maternal disorder due to congenital stenosis of vagina during antenatal and/or intrapartum period |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `443006` | Cystocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381656002 Maternal cystocele during antenatal and/or intrapartum period |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `44795003` | Rhesus isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381697009 Maternal Rhesus isoimmunization during antenatal and/or intrapartum period |
| `45079001` | Acromion left anterior position | inactivated (Duplicate) | SAME AS → 249108000 Shoulder left anterior position |
| `450891000124109` | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | inactivated (Outdated) | REPLACED BY → 1389464003 Past pregnancy history of disorder of antenatal and/or intrapartum and/or postnatal period |
| `45759004` | Rigid perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381659009 Rigid perineum during antenatal and/or intrapartum period |
| `45828008` | Anemia in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 156140005 Maternal anemia during antenatal and/or intrapartum and/or postpartum period |
| `46273003` | Abscess of nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388401001 Abscess of nipple during postpartum |
| `473429002` | Tuberculoma of spinal cord confirmed | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1411612005 Tuberculoma of spinal cord confirmed |
| `47507006` | Rieger anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 417604002 Axenfeld-Rieger syndrome, POSSIBLY EQUIVALENT TO → 1416355004 Rieger anomaly |
| `4783006` | Maternal diabetes mellitus with hypoglycemia affecting fetus OR newborn | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388261002 Disorder of fetus due to hypoglycemia of mother with diabetes mellitus, PARTIALLY EQUIVALENT TO → 1388262009 Disorder of neonate due to hypoglycemia of mother with diabetes mellitus |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `48200009` | Bone AND/OR joint disorder of lower extremities in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380436001 Maternal musculoskeletal disorder of lower limb during antenatal and/or intrapartum and/or postpartum period |
| `48485000` | Miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 10761191000119104 Preterm labor in third trimester with preterm delivery in third trimester |
| `48552006` | Hypertension secondary to renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension |
| `48739004` | Miscarriage with cardiac arrest and/or cardiac failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10760181000119109 Cardiac arrest due to miscarriage, PARTIALLY EQUIVALENT TO → 1397851002 Cardiac failure due to and following miscarriage |
| `49102001` | Hypertensive heart AND renal disease in obstetric context | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373667004 Pre-existing hypertensive heart and renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `49171007` | Hypertensive renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `49342001` | Stricture of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381676008 Stricture of vagina during antenatal and/or intrapartum period |
| `49364005` | Subareolar abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388403003 Subareolar abscess during postpartum |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `50120008` | Abnormal acid-base balance affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382350001 Maternal disorder of acid-base balance during antenatal and/or intrapartum and/or postpartum period |
| `50305006` | Acquired poliosis circumscripta | inactivated (Erroneous) | REPLACED BY → 1402366003 Acquired poliosis circumscripta |
| `50557007` | Healed pelvic floor repair affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381680003 Maternal disorder due to previous pelvic floor repair during antenatal and/or intrapartum period |
| `51154004` | Obstetrical pulmonary complication of anesthesia AND/OR sedation | inactivated (Classification derived) | REPLACED BY → 1386327009 Maternal disorder of lung due to administration of anesthesia and/or sedation during intrapartum period |
| `51495008` | Cerebral anoxia following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1396086006 Maternal cerebral anoxia due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1396087002 Maternal cerebral anoxia due to and following sedation during intrapartum period |
| `541000119105` | Hypertension complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `5534004` | Senile arteritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 129573006 Atherosclerotic occlusive disease, POSSIBLY EQUIVALENT TO → 698816006 Chronic occlusion of artery of extremity |
| `55472006` | Submammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388402008 Submammary abscess during postpartum |
| `55581002` | Meconium in amniotic fluid first noted during labor AND/OR delivery in liveborn infant | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor |
| `55613002` | Engorgement of breasts associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388405005 Engorgement of breast during postpartum, POSSIBLY EQUIVALENT TO → 34831003 Neonatal engorgement of breast |
| `55704005` | Abscess of breast, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258867002 Postpartum abscess of breast |
| `56313000` | Abnormal placenta affecting management of mother | inactivated (Classification derived) | REPLACED BY → 33552005 Anomaly of placenta |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `57220000` | Obstetrical complication of local anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380039000 Maternal disorder due to administration of local anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `57873008` | Hypertensive renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373623001 Disorder during maternal postpartum period due to hypertensive renal disease |
| `5852008` | Acromion right anterior position | inactivated (Duplicate) | SAME AS → 249107005 Shoulder right anterior position |
| `58881007` | Polyp of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381662007 Polyp of cervix during antenatal and/or intrapartum period |
| `58990004` | Miscarriage complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397368005 Traumatic injury of organ of pelvis due to and following miscarriage, POSSIBLY EQUIVALENT TO → 1397367000 Traumatic injury of soft tissue of pelvis due to and following miscarriage |
| `59136001` | Thyroid disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375993006 Maternal thyroid disorder during antenatal and/or intrapartum and/or postpartum period |
| `5939002` | Failed attempted termination of pregnancy complicated by metabolic disorder | inactivated (Duplicate) | SAME AS → 198810005 Failed attempted termination of pregnancy with metabolic disorder |
| `59733002` | Hypertensive heart disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373818003 Disorder during maternal intrapartum period due to pre-existing hypertensive heart disease |
| `59919008` | Failed attempted termination of pregnancy with complication | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 49416000 Failed attempted termination of pregnancy |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `609447002` | Induced termination of pregnancy complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `609449004` | Induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373901003 Embolism due to and following termination of pregnancy |
| `609450004` | Induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379953002 Pelvic inflammatory disease due to and following termination of pregnancy |
| `609451000` | Induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373900002 Metabolic disorder due to and following termination of pregnancy |
| `609452007` | Induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373872005 Renal failure due to and following termination of pregnancy |
| `609453002` | Induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609454008` | Induced termination of pregnancy complicated by acute necrosis of liver | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379940000 Acute necrosis of liver due to induced termination of pregnancy |
| `609455009` | Induced termination of pregnancy complicated by acute renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376024004 Acute renal failure due to and following termination of pregnancy |
| `609456005` | Induced termination of pregnancy complicated by afibrinogenemia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376015008 Afibrinogenemia due to induced termination of pregnancy |
| `609457001` | Induced termination of pregnancy complicated by air embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373908009 Air embolism due to and following termination of pregnancy |
| `609458006` | Induced termination of pregnancy complicated by amniotic fluid embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379939002 Amniotic fluid embolism due to and following termination of pregnancy |
| `609459003` | Induced termination of pregnancy complicated by blood-clot embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376026002 Thromboembolism due to and following termination of pregnancy |
| `609461007` | Induced termination of pregnancy complicated by cerebral anoxia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376016009 Cerebral anoxia due to induced termination of pregnancy |
| `609462000` | Induced termination of pregnancy complicated by defibrination syndrome | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379937000 Disseminated intravascular coagulation due to induced termination of pregnancy |
| `609463005` | Induced termination of pregnancy complicated by electrolyte imbalance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379932006 Electrolyte imbalance due to induced termination of pregnancy |
| `609464004` | Induced termination of pregnancy complicated by endometritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373904006 Endometritis due to induced termination of pregnancy |
| `609465003` | Induced termination of pregnancy complicated by fat embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373907004 Fat embolism due to and following termination of pregnancy |
| `609466002` | Induced termination of pregnancy complicated by intravascular hemolysis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379954008 Intravascular hemolysis due to induced termination of pregnancy |
| `609467006` | Induced termination of pregnancy complicated by laceration of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376027006 Laceration of intestine during termination of pregnancy |
| `609468001` | Induced termination of pregnancy complicated by laceration of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379942008 Laceration of broad ligament during termination of pregnancy |
| `609469009` | Induced termination of pregnancy complicated by laceration of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376029009 Laceration of cervix during termination of pregnancy |
| `609470005` | Induced termination of pregnancy complicated by laceration of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376031000 Laceration of uterus during termination of pregnancy |
| `609471009` | Induced termination of pregnancy complicated by laceration of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376030004 Laceration of vagina during termination of pregnancy |
| `609472002` | Induced termination of pregnancy complicated by acute renal failure with oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379956005 Acute renal failure with oliguria due to induced termination of pregnancy |
| `609473007` | Induced termination of pregnancy complicated by parametritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373906008 Parametritis due to induced termination of pregnancy |
| `609474001` | Induced termination of pregnancy complicated by pelvic peritonitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376020008 Pelvic peritonitis due to induced termination of pregnancy |
| `609475000` | Induced termination of pregnancy complicated by perforation of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376028001 Traumatic perforation of intestine during termination of pregnancy |
| `609476004` | Induced termination of pregnancy complicated by perforation of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379931004 Traumatic perforation of uterine cervix during termination of pregnancy |
| `609477008` | Induced termination of pregnancy complicated by perforation of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379935008 Traumatic perforation of uterus during termination of pregnancy |
| `609478003` | Induced termination of pregnancy complicated by perforation of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379930003 Traumatic perforation of vagina during termination of pregnancy |
| `609479006` | Induced termination of pregnancy complicated by postoperative shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609480009` | Induced termination of pregnancy complicated by pulmonary embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376021007 Pulmonary embolism due to and following termination of pregnancy |
| `609482001` | Induced termination of pregnancy complicated by renal tubular necrosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379938005 Acute renal tubular necrosis due to induced termination of pregnancy |
| `609483006` | Induced termination of pregnancy complicated by salpingitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373903000 Salpingitis due to induced termination of pregnancy |
| `609484000` | Induced termination of pregnancy complicated by salpingo-oophoritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376025003 Salpingo-oophoritis due to induced termination of pregnancy |
| `609486003` | Induced termination of pregnancy complicated by septic embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373918004 Septic embolism due to and following termination of pregnancy |
| `609487007` | Induced termination of pregnancy complicated by septic shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373909001 Septic shock due to and following termination of pregnancy |
| `609489005` | Induced termination of pregnancy complicated by soap embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373912003 Soap embolism due to and following termination of pregnancy |
| `609490001` | Induced termination of pregnancy complicated by uremia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373898004 Uremia due to induced termination of pregnancy |
| `609491002` | Induced termination of pregnancy complicated by urinary tract infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379952007 Urinary tract infection due to and following induced termination of pregnancy |
| `609493004` | Induced termination of pregnancy complicated by tetanus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373899007 Tetanus due to and following induced termination of pregnancy |
| `609494005` | Induced termination of pregnancy complicated by pelvic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373875007 Disorder of pelvis due to induced termination of pregnancy |
| `609496007` | Complication occurring during pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder, POSSIBLY EQUIVALENT TO → 173300003 Disorder of pregnancy |
| `609498008` | Induced termination of pregnancy complicated by laceration of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379929008 Laceration of urinary bladder during termination of pregnancy |
| `609499000` | Induced termination of pregnancy complicated by laceration of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379943003 Laceration of periurethral tissue during termination of pregnancy |
| `609500009` | Induced termination of pregnancy complicated by perforation of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379936009 Traumatic perforation of urinary bladder during termination of pregnancy |
| `609501008` | Induced termination of pregnancy complicated by perforation of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379941001 Traumatic perforation of broad ligament during termination of pregnancy |
| `609502001` | Induced termination of pregnancy complicated by perforation of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379944009 Traumatic perforation of periurethral tissue during termination of pregnancy |
| `609503006` | Induced termination of pregnancy complicated by urinary bladder damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373915001 Traumatic injury of urinary bladder during termination of pregnancy |
| `609504000` | Induced termination of pregnancy complicated by bowel damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373905007 Traumatic injury of intestine during termination of pregnancy |
| `609505004` | Induced termination of pregnancy complicated by broad ligament damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379933001 Traumatic injury of broad ligament during termination of pregnancy |
| `609506003` | Induced termination of pregnancy complicated by cardiac arrest | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373916000 Cardiac arrest due to induced termination of pregnancy |
| `609507007` | Induced termination of pregnancy complicated by cardiac failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376017000 Cardiac failure due to induced termination of pregnancy |
| `609508002` | Induced termination of pregnancy complicated by cervix damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373911005 Traumatic injury of uterine cervix during termination of pregnancy |
| `609510000` | Induced termination of pregnancy complicated by infectious disease | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376022000 Infectious disease due to and following induced termination of pregnancy |
| `609511001` | Induced termination of pregnancy complicated by periurethral tissue damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379955009 Periurethral traumatic injury during termination of pregnancy |
| `609512008` | Induced termination of pregnancy complicated by oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373902005 Oliguria due to induced termination of pregnancy |
| `609513003` | Induced termination of pregnancy complicated by uterus damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373914002 Traumatic injury of uterus during termination of pregnancy |
| `609514009` | Induced termination of pregnancy complicated by vaginal damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373917009 Traumatic injury of vagina during termination of pregnancy |
| `61714007` | Metabolic disturbance in labor AND/OR delivery | inactivated (Classification derived) | REPLACED BY → 1395830004 Maternal metabolic disease during intrapartum period |
| `61947007` | Deaf mutism | inactivated (Outdated) | - |
| `62612003` | Fibrosis of perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381677004 Fibrosis of perineum during antenatal and/or intrapartum period |
| `62657007` | Cardiac arrest AND/OR failure following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386325001 Maternal cardiac arrest due to administration of anesthesia and/or sedation during intrapartum period, POSSIBLY EQUIVALENT TO → 1386326000 Maternal cardiac failure due to administration of anesthesia and/or sedation during intrapartum period |
| `63287004` | Benign essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373658004 Benign pre-existing essential hypertension during antenatal and/or intrapartum and/or postpartum period |
| `64171002` | Obstetrical cardiac complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386323008 Maternal disorder of heart due to administration of anesthesia and/or sedation during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1386324002 Maternal disorder of heart due to administration of anesthesia and/or sedation during intrapartum period |
| `65402008` | Pre-existing hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `65409004` | Obstetrical complication of anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `6636004` | Congenital cardiovascular disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `66709007` | Hypertensive renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373622006 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive renal disease |
| `66958002` | Isoimmunization from non-ABO, non-Rh blood-group incompatibility affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381707006 Maternal non-ABO, non-Rhesus blood-group isoimmunization during antenatal and/or intrapartum period |
| `68214002` | Lymphangitis of breast associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388394002 Lymphangitis of breast during postpartum |
| `69302000` | Termination of pregnancy on demand | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 57797005 Termination of pregnancy |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | - |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | - |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `699950009` | Anti-D isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `71639005` | Galactorrhea associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388264005 Maternal galactorrhea during postpartum period |
| `71874008` | Benign essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373569006 Maternal disorder during labor due to benign essential hypertension |
| `72022006` | Essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373656000 Pre-existing essential hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `721166000` | Human immunodeficiency virus complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380419009 Maternal human immunodeficiency virus infection during antenatal and/or intrapartum and/or postpartum period |
| `721177006` | Injury complicating pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402307005 Maternal injury during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 426997005 Maternal traumatic injury during antenatal and/or intrapartum period |
| `721201001` | Protozoal disease complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1376000007 Maternal disorder caused by Protozoa during antenatal and/or intrapartum and/or postpartum period |
| `721203003` | Sequela of complication of pregnancy childbirth and the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380411007 Disorder due to and following maternal disorder during antenatal and/or intrapartum and/or postpartum period |
| `722595002` | Overweight in adulthood with body mass index of 25 or more but less than 30 | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407012005 Overweight in adulthood, ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2 |
| `72280009` | Achromotrichia | inactivated (Erroneous) | REPLACED BY → 1402356006 Achromotrichia |
| `723091005` | Fistula of vagina and/or rectum and/or urinary bladder due to complication occurring during labor and/or delivery | inactivated (Classification derived) | REPLACED BY → 1395886004 Genital tract fistula following vaginal delivery |
| `724497009` | Disease of circulatory system complicating pregnancy childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380409003 Maternal circulatory disorder during antenatal and/or intrapartum and/or postpartum period |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `72860003` | Disorder of amniotic cavity AND/OR membrane | inactivated (Classification derived) | REPLACED BY → 609522002 Disorder of extraembryonic membrane |
| `73030000` | Hypertensive renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373661003 Pre-existing hypertensive renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `735492001` | Obstructed labor due to shoulder dystocia | inactivated (Duplicate) | SAME AS → 89700002 Shoulder girdle dystocia |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `737329004` | Damage to pelvic organs and tissues following ectopic pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397365008 Traumatic injury of soft tissue of pelvis due to and following ectopic pregnancy, POSSIBLY EQUIVALENT TO → 1397370001 Traumatic injury of organ of pelvis due to and following ectopic pregnancy |
| `737330009` | Damage to pelvic organs and tissues following molar pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397366009 Traumatic injury of soft tissue of pelvis due to and following molar pregnancy, POSSIBLY EQUIVALENT TO → 1397369002 Traumatic injury of organ of pelvis due to and following molar pregnancy |
| `73813001` | Elastosis senilis | inactivated (Outdated) | REPLACED BY → 43982006 Solar degeneration |
| `73837001` | Failed attempted termination of pregnancy with cardiac arrest and/or failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10750641000119101 Cardiac arrest due to failed attempted abortion, PARTIALLY EQUIVALENT TO → 1373227006 Failed attempted abortion with cardiac failure |
| `74227009` | Apraxic aphonia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441913003 Aphonia, POSSIBLY EQUIVALENT TO → 1407180006 Acquired apraxia of speech |
| `74955002` | Retracted nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388400000 Retraction of nipple during postpartum |
| `75150001` | Renal disease in pregnancy AND/OR puerperium without hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 733839001 Postpartum acute renal failure, PARTIALLY EQUIVALENT TO → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension, PARTIALLY EQUIVALENT TO → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `76037007` | Rigid cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381674006 Rigid cervix uteri during antenatal and/or intrapartum period |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `76751001` | Diabetes mellitus in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199223000 Maternal diabetes mellitus during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 609563008 Pre-existing diabetes mellitus in pregnancy |
| `76871004` | Previous surgery to vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381679001 Maternal disorder due to previous vaginal surgery during antenatal and/or intrapartum period |
| `77285007` | Placental infarct affecting management of mother | inactivated (Classification derived) | REPLACED BY → 268585006 Placental infarct |
| `77563000` | Obstruction by bony pelvis | inactivated (Duplicate) | SAME AS → 199757009 Obstructed labor caused by bony pelvis |
| `778075008` | Pityriasis simplex capitis | inactivated (Duplicate) | SAME AS → 400201008 Pityriasis capitis |
| `78381004` | Heart disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375991008 Maternal heart disorder during antenatal and/or intrapartum and/or postpartum period |
| `78697003` | Nonpurulent mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388395001 Nonpurulent mastitis during postpartum |
| `78808002` | Essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373618001 Disorder during maternal antenatal and/or intrapartum period due to essential hypertension |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79355007` | Hypertensive heart disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373662005 Pre-existing hypertensive heart disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | - |
| `79839005` | Perineal laceration involving vulva | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 237332009 Vulval tear, POSSIBLY EQUIVALENT TO → 1388876002 First degree laceration of perineum and laceration of vulva during vaginal delivery of fetus |
| `80818002` | Previous surgery to perineum AND/OR vulva affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1381693008 Maternal disorder due to previous procedure on perineum during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1381694002 Maternal disorder due to previous procedure on vulva during antenatal and/or intrapartum period |
| `81557008` | Parasitic disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375999005 Maternal disorder caused by parasite during antenatal and/or intrapartum and/or postpartum period |
| `81626002` | Malignant hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373657009 Malignant hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `8218002` | Chronic hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `83243004` | Rigid pelvic floor affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381673000 Rigid pelvic floor during antenatal and/or intrapartum period |
| `84007008` | Shock during AND/OR following labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381592008 Maternal shock due to and following delivery, POSSIBLY EQUIVALENT TO → 1381590000 Maternal shock during intrapartum period |
| `8445003` | Neoplasm of vulva affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381661000 Neoplasm of vulva during antenatal and/or intrapartum period |
| `84939004` | Rubella in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 270497005 Maternal rubella during antenatal and/or intrapartum and/or postpartum period |
| `85542007` | Perineal laceration involving skin | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388874004 Laceration of skin of perineum, POSSIBLY EQUIVALENT TO → 1388873005 First degree laceration of skin of perineum during vaginal delivery of fetus |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `86041002` | Pre-existing hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `87383005` | Maternal distress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period, POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period |
| `8762007` | Chronic hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `87840008` | Galactocele associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388398004 Galactocele during postpartum period |
| `88320008` | Drug tolerance | inactivated (Nonconformance to editorial policy) | REPLACED BY → 365992008 Drug tolerance - finding |
| `89672000` | Retromammary mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388397009 Retromammary mastitis during postpartum |
| `90645002` | Failed attempted termination of pregnancy without complication | inactivated (Nonconformance to editorial policy) | REPLACED BY → 49416000 Failed attempted termination of pregnancy |
| `9297001` | Bicornuate uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381667001 Bicornate uterus during antenatal and/or intrapartum period |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |
| `95606005` | Maternal drug exposure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `95607001` | Maternal drug use | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `9720009` | Cicatrix of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381675007 Cicatrix of cervix during antenatal and/or intrapartum period |

**New members (850):**

| Code | Display |
|---|---|
| `1000081000220104` | Impaired prone position tolerance in infancy |
| `1011441000220106` | History of cardiovascular procedure |
| `1011481000220101` | Calcification of left ventricular outflow tract |
| `1011491000220103` | Rupture of aortic annulus |
| `1011661000220107` | In-hospital stroke |
| `1011671000220101` | In-hospital myocardial infarction |
| `103406000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A1 |
| `103407009` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A2 |
| `103408004` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A3 |
| `103409007` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B1 |
| `103410002` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B2 |
| `103411003` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B3 |
| `103412005` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C1 AIDS (acquired immunodeficiency syndrome) |
| `103413000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C2 AIDS (acquired immunodeficiency syndrome) |
| `103414006` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C3 AIDS (acquired immunodeficiency syndrome) |
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `11851561000119100` | Nonvenomous insect bite of posterior chest wall |
| `12206071000119108` | Osteolysis of bone adjacent to right ankle joint prosthesis |
| `12206111000119101` | Osteolysis of bone adjacent to right elbow joint prosthesis |
| `12206151000119100` | Osteolysis of bone adjacent to right finger joint prosthesis |
| `12208881000119103` | Osteolysis of bone adjacent to right shoulder joint prosthesis |
| `12217281000119101` | Osteolysis of bone adjacent to left ankle joint prosthesis |
| `12217321000119106` | Osteolysis of bone adjacent to left elbow joint prosthesis |
| `12217361000119101` | Osteolysis of bone adjacent to left finger joint prosthesis |
| `12217481000119102` | Osteolysis of bone adjacent to left shoulder joint prosthesis |
| `129769006` | Calcification cluster |
| `134098971000119103` | Osteolysis of bone adjacent to finger joint prosthesis |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |

… 810 more, see the CSV.

## Module `dokument`

### MINOR · `mii-vs-dokument-fachgebiet` (pinned, filter)

MII VS Dokument Fachgebiet  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-dokument/ValueSet/mii-vs-dokument-fachgebiet`  
Members: 266 → 268


**New members (2):**

| Code | Display |
|---|---|
| `1409616001` | Pediatric neuroradiology |
| `1409617005` | Head and neck radiology |

## Module `kardio`

### BREAKING · `mii-vs-kardio-extended-mii-diagnosecodes-snomed` (pinned, enumerated)

MII VS Kardio Extended MII DiagnoseCodes [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-extended-mii-diagnosecodes-snomed`  
Members: 137458 → 137864

- **Filter/enumerated anchor inactive:** `368009:{116676008=49755003,363698007=17401000},{246112005=24484000}`  — no successor

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `10562009` | Malignant hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373612000 Maternal disorder in labor due to malignant hypertension |
| `105709005` | Disease caused by Rhabdiasoidea | inactivated (Outdated) | - |
| `106005003` | Hypertension AND/OR vomiting complicating pregnancy childbirth AND/OR puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension, PARTIALLY EQUIVALENT TO → 90325002 Vomiting of pregnancy |
| `106008001` | Delivery AND/OR maternal condition affecting management | inactivated (Classification derived) | REPLACED BY → 1269075002 Maternal disorder during intrapartum period |
| `106009009` | Fetal condition affecting obstetrical care of mother | inactivated (Classification derived) | REPLACED BY → 70591005 Fetal disorder |
| `106010004` | Pelvic dystocia AND/OR uterine disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 79748007 Maternal dystocia, POSSIBLY EQUIVALENT TO → 12337004 Disorder of uterus, POSSIBLY EQUIVALENT TO → 1381465004 Labor dystocia |
| `10741911000119103` | Abnormal cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381664008 Abnormal cervix during antenatal and/or intrapartum period |
| `10743831000119100` | Neoplasm of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381663002 Neoplasm of uterus during antenatal and/or intrapartum period |
| `10743881000119104` | Suspected fetal abnormality affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 609520005 Disorder of fetal structure, PARTIALLY EQUIVALENT TO → 609415007 Fetal disorder suspected |
| `10749811000119108` | Obstetric anesthesia with central nervous system complication in childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `10808861000119105` | Maternal distress during childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period, POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period |
| `10835971000119109` | Anti-A sensitization in pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388946008 Maternal anti-A isoimmunization during antenatal and/or intrapartum period |
| `10853001` | Obstetrical complication of general anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380040003 Maternal disorder due to administration of general anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `10884004` | Threatened miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 6383007 Premature labor |
| `10897531000119101` | Open wound of female external genitalia | inactivated (Duplicate) | SAME AS → 210438000 Open wound of vulva |
| `10950002` | Vulval hematoma during delivery | inactivated (Duplicate) | SAME AS → 249217005 Maternal hematoma of vulva during intrapartum period |
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `111438007` | Hypertension secondary to renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373660002 Hypertension due to renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `111447004` | Placental condition affecting management of mother | inactivated (Classification derived) | REPLACED BY → 125586008 Disorder of placenta |
| `111459000` | Infection of nipple, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum |
| `1142291001` | Achromotrichia of eyebrow | inactivated (Erroneous) | REPLACED BY → 1402357002 Achromotrichia of eyebrow |
| `1145232003` | Premature grayness of hair of body | inactivated (Erroneous) | REPLACED BY → 1402358007 Premature grayness of hair of body |
| `1156096005` | Past pregnancy history of complication occurring during labor and delivery | inactivated (Outdated) | REPLACED BY → 1389463009 Past pregnancy history of maternal disorder during intrapartum period |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1186810009` | Erythropoietic protoporphyria due to gain of function of erythroid-specific aminolevulinic acid synthase 2 | inactivated (Duplicate) | SAME AS → 1197360001 X-linked dominant erythropoietic protoporphyria |
| `11914001` | Transverse OR oblique presentation of fetus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 73161006 Transverse lie, POSSIBLY EQUIVALENT TO → 63750008 Oblique lie |
| `120001000119107` | Group B streptococcus carrier complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1397016006 Maternal group B streptococcus carrier during antenatal and/or intrapartum period |
| `1208862000` | Acquired poliosis of eyelash | inactivated (Erroneous) | REPLACED BY → 1402368002 Acquired poliosis of eyelash |
| `1220564001` | Incomplete induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373920001 Shock due to and following incomplete termination of pregnancy |
| `1220586000` | Incomplete induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373870002 Renal failure due to and following incomplete termination of pregnancy |
| `1220625008` | Incomplete induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376019002 Metabolic disorder due to and following incomplete termination of pregnancy |
| `1220626009` | Incomplete induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379949004 Pelvic inflammatory disease due to and following incomplete termination of pregnancy |
| `1220630007` | Incomplete induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376023005 Embolism due to and following incomplete termination of pregnancy |
| `1220631006` | Incomplete induced termination of pregnancy complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379950004 Delayed hemorrhage due to and following incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379951000 Excessive hemorrhage due to and following incomplete induced termination of pregnancy |
| `1220632004` | Incomplete induced termination of pregnancy complicated by damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379948007 Traumatic injury of soft tissue of pelvis during incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379947002 Traumatic injury of pelvic organ during incomplete termination of pregnancy |
| `1220657009` | Damage to pelvic organs and/or tissue due to and following complete induced termination of pregnancy | inactivated (Classification derived) | REPLACED BY → 1375964006 Traumatic injury of pelvic organ during complete termination of pregnancy |
| `1254988002` | Substance dependence in mother complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `1269073009` | Fetal disorder due to disorder of amniotic cavity and/or membrane | inactivated (Classification derived) | REPLACED BY → 1384151007 Fetal disorder due to disorder of extraembryonic membrane |
| `1269102002` | Fetal disorder due to maternal disorder during pregnancy | inactivated (Duplicate) | SAME AS → 609429008 Fetal disorder due to disease in mother |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `1269476005` | At increased risk for complication during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1392349003 At increased risk for maternal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1392350003 At increased risk for fetal disorder during intrapartum period |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `128076000` | Bone AND/OR joint disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380433009 Maternal disorder of bone and/or joint during antenatal and/or intrapartum and/or postpartum period |
| `12867002` | Fetal distress affecting management of mother | inactivated (Classification derived) | REPLACED BY → 130955003 Nonreassuring fetal status |
| `1354494000` | Induced termination of pregnancy complicated by damage to urethra | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376018005 Traumatic injury of urethra during termination of pregnancy |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | - |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | - |
| `1362092008` | Complication occurring during pregnancy absent | inactivated (Outdated) | REPLACED BY → 1389061004 Maternal disorder during antenatal and/or intrapartum period absent |
| `13866000` | Fetal acidemia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382318006 Fetal acidemia |
| `13943000` | Failed attempted termination of pregnancy complicated by embolism | inactivated (Duplicate) | SAME AS → 198812002 Failed attempted termination of pregnancy with embolism |
| `14022007` | Fetal death, affecting management of mother | inactivated (Classification derived) | REPLACED BY → 276507005 Fetal death |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `14240001` | Poliosis | inactivated (Erroneous) | REPLACED BY → 1402362001 Poliosis |
| `1474004` | Hypertensive heart AND renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373630007 Disorder during maternal intrapartum period due to hypertensive heart and renal disease |
| `1538006` | Fetal malformation of central nervous system affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 9721000119107 Fetal malformation of central nervous system |
| `15406009` | Retromammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388404009 Retromammary abscess during postpartum |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `161579008` | H/O: perinatal problem | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401818004 History of perinatal disorder of fetus and/or early neonate |
| `162135003` | Urine looks pale | inactivated (Duplicate) | SAME AS → 167234002 Pale urine |
| `162863004` | Body mass index 25-29 - overweight | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2, ALTERNATIVE → 1407012005 Overweight in adulthood |
| `162864005` | Body mass index 30+ - obesity | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 414916001 Obesity, ALTERNATIVE → 414915002 Obese, ALTERNATIVE → 1407009007 Adult body mass index greater than or equal to 30 kg/m2 |
| `1639007` | Abnormality of organs AND/OR soft tissues of pelvis affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 199446000 Maternal abnormality of pelvic soft tissue during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1381684007 Maternal disorder of pelvic organ during antenatal and/or intrapartum period |
| `169887003` | Birth length equal to third centile | inactivated (Erroneous) | REPLACED BY → 1411483000 Birth length equal to or less than third centile |
| `171000119107` | Maternal obesity complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380417006 Maternal obesity during antenatal and/or intrapartum and/or postpartum period |
| `17594002` | Fetal bradycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240299002 Fetal bradycardia |
| `18237006` | Parenchymatous mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388396000 Parenchymatous mastitis during postpartum |
| `18416000` | Essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373617006 Disorder during maternal intrapartum period due to essential hypertension |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `190737001` | Iminoacidopathy | inactivated (Outdated) | REPLACED BY → 37800003 Disorder of proline AND/OR hydroxyproline metabolism |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `197140007` | Secondary megacolon - congenital | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 197141006 Secondary acquired megacolon, POSSIBLY EQUIVALENT TO → 204739008 Congenital aganglionic megacolon |
| `19773009` | Infection of the breast AND/OR nipple associated with childbirth | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum, PARTIALLY EQUIVALENT TO → 1388391005 Infection of breast during postpartum |
| `198609003` | Complication of pregnancy, childbirth and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269101009 Maternal disorder during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder |
| `198617006` | Delivery of viable fetus in abdominal pregnancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 237253003 Viable fetus in abdominal pregnancy |
| `198655001` | Complete miscarriage with genital tract or pelvic infection | inactivated (Classification derived) | REPLACED BY → 1397373004 Genital tract infection due to and following complete miscarriage |
| `198656000` | Complete miscarriage with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397338001 Excessive hemorrhage due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397337006 Delayed hemorrhage due to and following complete miscarriage |
| `198657009` | Complete miscarriage with damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397364007 Traumatic injury of soft tissue of pelvis due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397371002 Traumatic injury of organ of pelvis due to and following complete miscarriage |
| `19866007` | Previous operation to cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381692003 Maternal disorder due to previous uterine cervix surgery during antenatal and/or intrapartum period |
| `198806007` | Failed attempted termination of pregnancy with genital tract or pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection, PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection |
| `198807003` | Failed attempted termination of pregnancy with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198808008` | Failed attempted termination of pregnancy with damage to pelvic organ or tissues | inactivated (Classification derived) | REPLACED BY → 1375968009 Failed attempted abortion with traumatic injury to pelvic organ |
| `198832001` | Damage to pelvic organs or tissues following abortive pregnancy | inactivated (Classification derived) | REPLACED BY → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `198874006` | Failed medical termination of pregnancy, complicated by genital tract or pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373432005 Failed medical abortion with pelvic infection, POSSIBLY EQUIVALENT TO → 1373431003 Failed medical abortion with genital tract infection |
| `198875007` | Failed medical termination of pregnancy, complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198941007` | Hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `198942000` | Benign essential hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `198949009` | Renal hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `198997005` | Pre-eclampsia or eclampsia with pre-existing hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 67359005 Pre-eclampsia added to pre-existing hypertension, PARTIALLY EQUIVALENT TO → 69909000 Eclampsia added to pre-existing hypertension |
| `199005000` | Pre-existing hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1373810005 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertension |
| `199006004` | Pre-existing hypertensive heart disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373739002 Maternal disorder during antenatal and/or intrapartum and/or postpartum period due to hypertensive heart disease |
| `199007008` | Pre-existing hypertensive heart and renal disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373732006 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertensive heart and renal disease |
| `199008003` | Pre-existing secondary hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380416002 Pre-existing secondary hypertension during antenatal and/or intrapartum and/or postpartum period |
| `199203001` | Viral hepatitis complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380412000 Maternal viral hepatitis during antenatal and/or intrapartum and/or postpartum period |
| `199257008` | Mental disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1396772000 Mental disorder during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1258898000 Mental disorder during puerperium |
| `199279003` | Orthopedic disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period |
| `199293005` | Disease of the respiratory system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1380415003 Maternal disorder of respiratory system during antenatal and/or intrapartum and/or postpartum period |
| `199294004` | Disease of the digestive system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1376007005 Maternal disorder of digestive system during antenatal and/or intrapartum and/or postpartum period |
| `199295003` | Disease of skin and subcutaneous tissue complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1380413005 Maternal disorder of skin and/or subcutaneous tissue during antenatal and/or intrapartum and/or postpartum period |
| `199296002` | Endocrine, nutritional and metabolic disease complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380430007 Maternal nutritional disorder during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1380431006 Maternal metabolic disorder during antenatal and/or intrapartum and/or postpartum period |
| `199297006` | Disease of nervous system complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380418001 Maternal disorder of nervous system during antenatal and/or intrapartum and/or postpartum period |
| `199305006` | Complications specific to multiple gestation | inactivated (Classification derived) | REPLACED BY → 1379972002 Maternal disorder due to multiple pregnancy |
| `199314001` | Normal delivery but ante- or post- natal conditions present | inactivated (Classification derived) | REPLACED BY → 48782003 Delivery normal |
| `199322008` | Triplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 64254006 Triplet pregnancy |
| `199326006` | Quadruplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 60810003 Quadruplet pregnancy |
| `199578005` | Fetal-maternal hemorrhage with antenatal problem | inactivated (Classification derived) | REPLACED BY → 71028008 Fetal-maternal hemorrhage |
| `199595002` | Labor and delivery complication by meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period |
| `199596001` | Labor and delivery complicated by fetal heart rate anomaly with meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389112004 Abnormal fetal heart rate with meconium stained amniotic fluid during intrapartum period |
| `199597005` | Labor and delivery complicated by biochemical evidence of fetal stress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389146003 Fetal distress with fetal acidosis during intrapartum period |
| `199678003` | Amniotic cavity infection with antenatal problem | inactivated (Classification derived) | REPLACED BY → 10573002 Infection of amniotic cavity |
| `199745000` | Complication occurring during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `199935005` | Fourth degree perineal tear during delivery with postnatal problem | inactivated (Classification derived) | REPLACED BY → 399031001 Fourth degree perineal laceration |
| `200046004` | Complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1381276002 Maternal disorder due to administration of anesthesia during intrapartum period |
| `200054002` | Obstetric anesthesia with cardiac complications | inactivated (Classification derived) | REPLACED BY → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200061003` | Obstetric anesthesia with central nervous system complications | inactivated (Classification derived) | REPLACED BY → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200077002` | Cardiac complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period |
| `200078007` | Central nervous system complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `200985008` | Parapsoriasis varioliformis | inactivated (Outdated) | REPLACED BY → 86487001 Acute lichenoid pityriasis |
| `201174003` | Poliosis eccentrica | inactivated (Erroneous) | REPLACED BY → 1402372003 Poliosis eccentrica |
| `201175002` | Poliosis - acquired | inactivated (Erroneous) | REPLACED BY → 1402371005 Acquired poliosis |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | - |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | - |
| `20753005` | Hypertensive heart disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373738005 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart disease |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `20845005` | Meconium in amniotic fluid affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor, PARTIALLY EQUIVALENT TO → 2132004 Meconium in amniotic fluid noted before labor in liveborn infant |
| `213202009` | Complications of attempted introduction of fertilized ovum following in vitro fertilization | inactivated (Classification derived) | REPLACED BY → 1379976004 Disorder due to embryo transfer following in vitro fertilization |
| `21346009` | Double uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381658001 Maternal congenital duplication of uterus during antenatal and/or intrapartum period |
| `22173004` | Excessive fetal growth affecting management of mother | inactivated (Classification derived) | REPLACED BY → 199616008 Large for gestation age fetus |
| `22281000119101` | Post-term pregnancy of 40 to 42 weeks | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 63503002 Gestation period, 41 weeks, POSSIBLY EQUIVALENT TO → 46230007 Gestation period, 40 weeks, POSSIBLY EQUIVALENT TO → 90968009 Post-term pregnancy |
| `22288000` | Neoplasm of cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381666005 Neoplasm of cervix uteri during antenatal and/or intrapartum period |
| `223003` | Neoplasm of body of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381678009 Neoplasm of body of uterus during antenatal and/or intrapartum period |
| `22753004` | Fetal AND/OR placental disorder affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1193535003 Fetal disorder due to placental disorder, PARTIALLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `22966008` | Hypertensive heart AND renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373627000 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart and renal disease |
| `23001005` | Stenosis AND/OR stricture of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381651007 Maternal stenosis of cervix during antenatal and/or intrapartum period |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `23171006` | Delayed AND/OR secondary postpartum hemorrhage | inactivated (Classification derived) | REPLACED BY → 156241003 Secondary postpartum hemorrhage |
| `23717007` | Benign essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `237171000` | Stenosis of vagina in pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1396771007 Stenosis of vagina during antenatal and/or intrapartum period |
| `237256006` | Disorder of pelvic size and disproportion | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199416003 Mixed feto-pelvic disproportion, POSSIBLY EQUIVALENT TO → 275426009 Pelvic disproportion, POSSIBLY EQUIVALENT TO → 25749005 Fetopelvic disproportion, POSSIBLY EQUIVALENT TO → 199397009 Cephalopelvic disproportion |
| `237330001` | Obstetric injury of urinary bladder | inactivated (Duplicate) | SAME AS → 54679003 Traumatic injury of urinary bladder during obstetric procedure |
| `237342006` | Fat embolism - obstetric | inactivated (Duplicate) | SAME AS → 2261009 Obstetrical pulmonary fat embolism |
| `238419741000119109` | Alpha thalassemia trait in mother complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373734007 Maternal disorder due to alpha thalassemia trait during antenatal and/or intrapartum period |
| `23894009` | Acne varioliformis | inactivated (Duplicate) | SAME AS → 201228005 Necrotizing lymphocytic folliculitis |
| `239884000` | Malemud disease | inactivated (Nonconformance to editorial policy) | - |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | - |
| `248663000` | Upper sternal shock | inactivated (Classification derived) | REPLACED BY → 248690009 Added heart sounds |
| `249079005` | Fontanelles presenting | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249083005 Posterior fontanelle presenting, POSSIBLY EQUIVALENT TO → 249082000 Anterior fontanelle presenting |
| `25053000` | Obstetrical central nervous system complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26078007` | Hypertension secondary to renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `26224003` | Failed attempted termination of pregnancy complicated by genital-pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection, PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection |
| `26623000` | Failed attempted termination of pregnancy complicated by delayed and/or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion |
| `267207004` | Congenital cardiovascular disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `267257007` | Labor and delivery complicated by fetal heart rate anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389144000 Abnormal fetal heart rate during intrapartum period |
| `267276009` | Obstetric anesthesia with pulmonary complications | inactivated (Classification derived) | REPLACED BY → 1379971009 Maternal pulmonary disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `267280004` | Venous complication of pregnancy and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379964004 Maternal venous disorder due to pregnancy during antenatal and/or intrapartum and/or postpartum period |
| `267322007` | Pregnancy with orthopedic problem | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 9111000119104 Musculoskeletal problem in pregnancy |
| `267350007` | Obstetric anesthesia problems | inactivated (Classification derived) | REPLACED BY → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26828006` | Rectocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381657006 Maternal rectocele during antenatal and/or intrapartum period |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `270498000` | Fetal malposition and malpresentation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 289365005 Finding of malposition of fetus, POSSIBLY EQUIVALENT TO → 80002007 Malpresentation of fetus |
| `27075004` | Venereal disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375996003 Maternal sexually transmitted infectious disease during antenatal and/or intrapartum and/or postpartum period |
| `273982004` | Obstetric problem affecting fetus | inactivated (Classification derived) | REPLACED BY → 609429008 Fetal disorder due to disease in mother |
| `273983009` | Maternal cord or placental problem | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 429260008 Disorder of umbilical cord, POSSIBLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `276263005` | Porphobilinogen deaminase deficiency | inactivated (Duplicate) | SAME AS → 234422006 Acute intermittent porphyria |
| `276580005` | Atypical isoimmunization of newborn | inactivated (Outdated) | - |
| `284670008` | Nutritionally compromised | inactivated (Duplicate) | SAME AS → 445261000124106 Impaired nutritional status |
| `28664002` | Herpes iris | inactivated (Outdated) | REPLACED BY → 1407145007 Erythema multiforme with vesiculobullous target-shaped lesion |
| `288261009` | Was malpresentation pre-labor | inactivated (Erroneous) | REPLACED BY → 80002007 Malpresentation of fetus |
| `29259002` | Malignant hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373611007 Disorder during maternal antenatal and/or intrapartum period due to malignant hypertension |
| `29421008` | Failed attempted termination of pregnancy complicated by renal failure | inactivated (Duplicate) | SAME AS → 198809000 Failed attempted termination of pregnancy with renal failure |
| `29847008` | Obstetrical complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `3033000` | Bone AND/OR joint disorder of pelvis in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380435002 Maternal disorder of pelvic ring during antenatal and/or intrapartum and/or postpartum period |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `307333004` | Rhesus isoimmunization due to anti-D | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381908006 Hemolytic disease of fetus and/or neonate due to Rhesus anti-D isoimmunization, POSSIBLY EQUIVALENT TO → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `307334005` | Rhesus isoimmunization due to anti-c | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381903002 Hemolytic disease of fetus and/or neonate due to Rhesus anti-c isoimmunization, POSSIBLY EQUIVALENT TO → 1381901000 Maternal Rhesus isoimmunization due to anti-c during antenatal and/or intrapartum period |
| `307335006` | Rhesus isoimmunization due to anti-E | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381907001 Maternal Rhesus isoimmunization due to anti-E during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 1381909003 Hemolytic disease of fetus and/or neonate due to Rhesus anti-E isoimmunization |
| `307336007` | Rhesus isoimmunization due to anti-Cw | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381906005 Hemolytic disease of fetus and/or neonate due to Rhesus anti-Cw isoimmunization, POSSIBLY EQUIVALENT TO → 1381905009 Maternal Rhesus isoimmunization due to anti-Cw during antenatal and/or intrapartum period |
| `307735008` | Complete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397334004 Excessive hemorrhage due to and following complete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397335003 Delayed hemorrhage due to and following complete inevitable miscarriage |
| `307752007` | Incomplete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397343008 Excessive hemorrhage due to and following incomplete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397344002 Delayed hemorrhage due to and following incomplete inevitable miscarriage |
| `31026002` | Obstetrical complication of sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period |
| `31383003` | Neoplasm of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381650008 Neoplasm of vagina during pregnancy |
| `31407004` | Pre-existing hypertension complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373620003 Disorder during maternal postpartum period due to pre-existing hypertension |
| `31516002` | Viral disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375992001 Maternal viral disorder during antenatal and/or intrapartum and/or postpartum period |
| `31801000146106` | Pre-existing maternal disease complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373736009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing disease |
| `31821006` | Uterine scar from previous surgery affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381695001 Maternal disorder due to uterine scar from previous surgery during antenatal and/or intrapartum period |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `32999002` | Complication of obstetrical surgical wound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380090004 Disorder of surgical wound following obstetric surgical procedure during antenatal and/or intrapartum and/or postpartum period |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `34273003` | Hypertensive heart disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373628005 Disorder during maternal postpartum period due to hypertensive heart and renal disease |
| `34694006` | Pre-existing hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `35716006` | Cracked nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258917005 Postpartum cracked nipple |
| `35746009` | Uterine fibroids affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381668006 Uterine leiomyoma during antenatal and/or intrapartum period |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `36297009` | Septate vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381660004 Maternal septate vagina during antenatal and/or intrapartum period |
| `362972006` | Disorder of labor / delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1382290001 Disorder of mother and/or fetus during intrapartum period, POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `36428009` | Gestation period, 42 weeks | inactivated (Nonconformance to editorial policy) | REPLACED BY → 90968009 Post-term pregnancy |
| `367390009` | Hypertension in the obstetric context | inactivated (Classification derived) | REPLACED BY → 288250001 Maternal hypertension |
| `36916008` | Bone AND/OR joint disorder of back in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380434003 Maternal disorder of vertebral column during antenatal and/or intrapartum and/or postpartum period |
| `370056005` | Tumor invasion into bronchus, in situ | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370057001` | Tumor invasion into bronchus, invasive | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370480003` | Hepatoportal microvascular dysplasia | inactivated (Nonconformance to editorial policy) | - |
| `370914009` | Death or serious disability (kernicterus) associated with failure to identify and treat hyperbilirubinemia in neonates | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 370909005 Serious reportable event associated with care management, PARTIALLY EQUIVALENT TO → 419620001 Death, PARTIALLY EQUIVALENT TO → 21134002 Disability |
| `372043009` | Hydrops of allantois | inactivated (Nonconformance to editorial policy) | - |
| `37618003` | Chronic hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `387833009` | Premature canities | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 297994000 Gray hair, POSSIBLY EQUIVALENT TO → 1402360009 Premature canities |
| `3885002` | ABO isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381701007 Maternal ABO isoimmunization during antenatal and/or intrapartum period |
| `39101000119109` | Pregnancy with isoimmunization from irregular blood group incompatibility | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381698004 Maternal irregular blood group isoimmunization during antenatal and/or intrapartum period |
| `39727004` | Hypertension secondary to renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373624007 Disorder during maternal postpartum period due to renal hypertension |
| `39763004` | Abnormal glucose tolerance in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 372046001 Glucose tolerance test during pregnancy, childbirth and puerperium outside reference range |
| `397949005` | Poor fetal growth affecting management | inactivated (Classification derived) | REPLACED BY → 22033007 Fetal growth restriction |
| `398276003` | Placental insufficiency affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237292005 Placental insufficiency |
| `399363000` | Late fetal death affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237364002 Stillbirth |
| `4006006` | Fetal tachycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240298005 Fetal tachycardia |
| `4026005` | Interstitial mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388393008 Interstitial mastitis during postpartum |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `40609001` | Infectious disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1376002004 Maternal infection during antenatal and/or intrapartum and/or postpartum period |
| `408512008` | Body mass index 40+ - severely obese | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407010002 Adult body mass index greater than or equal to 40 kg/m2, ALTERNATIVE → 83911000119104 Severe obesity |
| `41215002` | Congenital abnormality of uterus, affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381683001 Maternal disorder due to congenital abnormality of uterus during antenatal and/or intrapartum period |
| `412768003` | Body mass index 20-24 - normal | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 43664005 Normal weight, ALTERNATIVE → 1407013000 Adult body mass index 18.5-24.9 kg/m2 |
| `413567003` | Aplastic anemia associated with pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379966002 Maternal aplastic anemia during antenatal and/or intrapartum period |
| `415110002` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 415112005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 109989006 Multiple myeloma |
| `41527003` | Glycogen storage disease type VIII | inactivated (Outdated) | REPLACED BY → 235908005 Glycogen phosphorylase kinase deficiency |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `42537006` | Secondary perineal tear in the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 6234006 Second degree perineal laceration |
| `42686001` | Fetal chromosomal abnormality affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 267253006 Fetal chromosomal abnormality |
| `427090001` | Body mass index less than 16.5 | inactivated (Outdated) | REPLACED BY → 1407014006 Adult body mass index less than 18.5 kg/m2 |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `428530009` | Heterozygous sitosterolemia | inactivated (Erroneous) | REPLACED BY → 1409234007 Compound heterozygous sitosterolemia |
| `43329005` | Infestation by Knemidokoptes pilae | inactivated (Nonconformance to editorial policy) | - |
| `43651009` | Acquired stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381681004 Maternal disorder due to acquired stenosis of vagina during antenatal and/or intrapartum period |
| `43970002` | Congenital stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381682006 Maternal disorder due to congenital stenosis of vagina during antenatal and/or intrapartum period |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `443006` | Cystocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381656002 Maternal cystocele during antenatal and/or intrapartum period |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `44795003` | Rhesus isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381697009 Maternal Rhesus isoimmunization during antenatal and/or intrapartum period |
| `45079001` | Acromion left anterior position | inactivated (Duplicate) | SAME AS → 249108000 Shoulder left anterior position |
| `450891000124109` | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | inactivated (Outdated) | REPLACED BY → 1389464003 Past pregnancy history of disorder of antenatal and/or intrapartum and/or postnatal period |
| `45759004` | Rigid perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381659009 Rigid perineum during antenatal and/or intrapartum period |
| `45828008` | Anemia in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 156140005 Maternal anemia during antenatal and/or intrapartum and/or postpartum period |
| `46273003` | Abscess of nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388401001 Abscess of nipple during postpartum |
| `473429002` | Tuberculoma of spinal cord confirmed | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1411612005 Tuberculoma of spinal cord confirmed |
| `47507006` | Rieger anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 417604002 Axenfeld-Rieger syndrome, POSSIBLY EQUIVALENT TO → 1416355004 Rieger anomaly |
| `4783006` | Maternal diabetes mellitus with hypoglycemia affecting fetus OR newborn | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388261002 Disorder of fetus due to hypoglycemia of mother with diabetes mellitus, PARTIALLY EQUIVALENT TO → 1388262009 Disorder of neonate due to hypoglycemia of mother with diabetes mellitus |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `48200009` | Bone AND/OR joint disorder of lower extremities in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380436001 Maternal musculoskeletal disorder of lower limb during antenatal and/or intrapartum and/or postpartum period |
| `48485000` | Miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 10761191000119104 Preterm labor in third trimester with preterm delivery in third trimester |
| `48552006` | Hypertension secondary to renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension |
| `48739004` | Miscarriage with cardiac arrest and/or cardiac failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10760181000119109 Cardiac arrest due to miscarriage, PARTIALLY EQUIVALENT TO → 1397851002 Cardiac failure due to and following miscarriage |
| `49102001` | Hypertensive heart AND renal disease in obstetric context | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373667004 Pre-existing hypertensive heart and renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `49171007` | Hypertensive renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `49342001` | Stricture of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381676008 Stricture of vagina during antenatal and/or intrapartum period |
| `49364005` | Subareolar abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388403003 Subareolar abscess during postpartum |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `50120008` | Abnormal acid-base balance affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382350001 Maternal disorder of acid-base balance during antenatal and/or intrapartum and/or postpartum period |
| `50305006` | Acquired poliosis circumscripta | inactivated (Erroneous) | REPLACED BY → 1402366003 Acquired poliosis circumscripta |
| `50557007` | Healed pelvic floor repair affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381680003 Maternal disorder due to previous pelvic floor repair during antenatal and/or intrapartum period |
| `51154004` | Obstetrical pulmonary complication of anesthesia AND/OR sedation | inactivated (Classification derived) | REPLACED BY → 1386327009 Maternal disorder of lung due to administration of anesthesia and/or sedation during intrapartum period |
| `51495008` | Cerebral anoxia following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1396086006 Maternal cerebral anoxia due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1396087002 Maternal cerebral anoxia due to and following sedation during intrapartum period |
| `541000119105` | Hypertension complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `5534004` | Senile arteritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 129573006 Atherosclerotic occlusive disease, POSSIBLY EQUIVALENT TO → 698816006 Chronic occlusion of artery of extremity |
| `55472006` | Submammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388402008 Submammary abscess during postpartum |
| `55581002` | Meconium in amniotic fluid first noted during labor AND/OR delivery in liveborn infant | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor |
| `55613002` | Engorgement of breasts associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388405005 Engorgement of breast during postpartum, POSSIBLY EQUIVALENT TO → 34831003 Neonatal engorgement of breast |
| `55704005` | Abscess of breast, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258867002 Postpartum abscess of breast |
| `56313000` | Abnormal placenta affecting management of mother | inactivated (Classification derived) | REPLACED BY → 33552005 Anomaly of placenta |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `57220000` | Obstetrical complication of local anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380039000 Maternal disorder due to administration of local anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `57873008` | Hypertensive renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373623001 Disorder during maternal postpartum period due to hypertensive renal disease |
| `5852008` | Acromion right anterior position | inactivated (Duplicate) | SAME AS → 249107005 Shoulder right anterior position |
| `58881007` | Polyp of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381662007 Polyp of cervix during antenatal and/or intrapartum period |
| `58990004` | Miscarriage complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397368005 Traumatic injury of organ of pelvis due to and following miscarriage, POSSIBLY EQUIVALENT TO → 1397367000 Traumatic injury of soft tissue of pelvis due to and following miscarriage |
| `59136001` | Thyroid disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375993006 Maternal thyroid disorder during antenatal and/or intrapartum and/or postpartum period |
| `5939002` | Failed attempted termination of pregnancy complicated by metabolic disorder | inactivated (Duplicate) | SAME AS → 198810005 Failed attempted termination of pregnancy with metabolic disorder |
| `59733002` | Hypertensive heart disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373818003 Disorder during maternal intrapartum period due to pre-existing hypertensive heart disease |
| `59919008` | Failed attempted termination of pregnancy with complication | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 49416000 Failed attempted termination of pregnancy |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `609447002` | Induced termination of pregnancy complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `609449004` | Induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373901003 Embolism due to and following termination of pregnancy |
| `609450004` | Induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379953002 Pelvic inflammatory disease due to and following termination of pregnancy |
| `609451000` | Induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373900002 Metabolic disorder due to and following termination of pregnancy |
| `609452007` | Induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373872005 Renal failure due to and following termination of pregnancy |
| `609453002` | Induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609454008` | Induced termination of pregnancy complicated by acute necrosis of liver | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379940000 Acute necrosis of liver due to induced termination of pregnancy |
| `609455009` | Induced termination of pregnancy complicated by acute renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376024004 Acute renal failure due to and following termination of pregnancy |
| `609456005` | Induced termination of pregnancy complicated by afibrinogenemia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376015008 Afibrinogenemia due to induced termination of pregnancy |
| `609457001` | Induced termination of pregnancy complicated by air embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373908009 Air embolism due to and following termination of pregnancy |
| `609458006` | Induced termination of pregnancy complicated by amniotic fluid embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379939002 Amniotic fluid embolism due to and following termination of pregnancy |
| `609459003` | Induced termination of pregnancy complicated by blood-clot embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376026002 Thromboembolism due to and following termination of pregnancy |
| `609461007` | Induced termination of pregnancy complicated by cerebral anoxia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376016009 Cerebral anoxia due to induced termination of pregnancy |
| `609462000` | Induced termination of pregnancy complicated by defibrination syndrome | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379937000 Disseminated intravascular coagulation due to induced termination of pregnancy |
| `609463005` | Induced termination of pregnancy complicated by electrolyte imbalance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379932006 Electrolyte imbalance due to induced termination of pregnancy |
| `609464004` | Induced termination of pregnancy complicated by endometritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373904006 Endometritis due to induced termination of pregnancy |
| `609465003` | Induced termination of pregnancy complicated by fat embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373907004 Fat embolism due to and following termination of pregnancy |
| `609466002` | Induced termination of pregnancy complicated by intravascular hemolysis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379954008 Intravascular hemolysis due to induced termination of pregnancy |
| `609467006` | Induced termination of pregnancy complicated by laceration of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376027006 Laceration of intestine during termination of pregnancy |
| `609468001` | Induced termination of pregnancy complicated by laceration of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379942008 Laceration of broad ligament during termination of pregnancy |
| `609469009` | Induced termination of pregnancy complicated by laceration of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376029009 Laceration of cervix during termination of pregnancy |
| `609470005` | Induced termination of pregnancy complicated by laceration of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376031000 Laceration of uterus during termination of pregnancy |
| `609471009` | Induced termination of pregnancy complicated by laceration of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376030004 Laceration of vagina during termination of pregnancy |
| `609472002` | Induced termination of pregnancy complicated by acute renal failure with oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379956005 Acute renal failure with oliguria due to induced termination of pregnancy |
| `609473007` | Induced termination of pregnancy complicated by parametritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373906008 Parametritis due to induced termination of pregnancy |
| `609474001` | Induced termination of pregnancy complicated by pelvic peritonitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376020008 Pelvic peritonitis due to induced termination of pregnancy |
| `609475000` | Induced termination of pregnancy complicated by perforation of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376028001 Traumatic perforation of intestine during termination of pregnancy |
| `609476004` | Induced termination of pregnancy complicated by perforation of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379931004 Traumatic perforation of uterine cervix during termination of pregnancy |
| `609477008` | Induced termination of pregnancy complicated by perforation of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379935008 Traumatic perforation of uterus during termination of pregnancy |
| `609478003` | Induced termination of pregnancy complicated by perforation of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379930003 Traumatic perforation of vagina during termination of pregnancy |
| `609479006` | Induced termination of pregnancy complicated by postoperative shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609480009` | Induced termination of pregnancy complicated by pulmonary embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376021007 Pulmonary embolism due to and following termination of pregnancy |
| `609482001` | Induced termination of pregnancy complicated by renal tubular necrosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379938005 Acute renal tubular necrosis due to induced termination of pregnancy |
| `609483006` | Induced termination of pregnancy complicated by salpingitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373903000 Salpingitis due to induced termination of pregnancy |
| `609484000` | Induced termination of pregnancy complicated by salpingo-oophoritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376025003 Salpingo-oophoritis due to induced termination of pregnancy |
| `609486003` | Induced termination of pregnancy complicated by septic embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373918004 Septic embolism due to and following termination of pregnancy |
| `609487007` | Induced termination of pregnancy complicated by septic shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373909001 Septic shock due to and following termination of pregnancy |
| `609489005` | Induced termination of pregnancy complicated by soap embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373912003 Soap embolism due to and following termination of pregnancy |
| `609490001` | Induced termination of pregnancy complicated by uremia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373898004 Uremia due to induced termination of pregnancy |
| `609491002` | Induced termination of pregnancy complicated by urinary tract infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379952007 Urinary tract infection due to and following induced termination of pregnancy |
| `609493004` | Induced termination of pregnancy complicated by tetanus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373899007 Tetanus due to and following induced termination of pregnancy |
| `609494005` | Induced termination of pregnancy complicated by pelvic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373875007 Disorder of pelvis due to induced termination of pregnancy |
| `609496007` | Complication occurring during pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder, POSSIBLY EQUIVALENT TO → 173300003 Disorder of pregnancy |
| `609498008` | Induced termination of pregnancy complicated by laceration of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379929008 Laceration of urinary bladder during termination of pregnancy |
| `609499000` | Induced termination of pregnancy complicated by laceration of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379943003 Laceration of periurethral tissue during termination of pregnancy |
| `609500009` | Induced termination of pregnancy complicated by perforation of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379936009 Traumatic perforation of urinary bladder during termination of pregnancy |
| `609501008` | Induced termination of pregnancy complicated by perforation of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379941001 Traumatic perforation of broad ligament during termination of pregnancy |
| `609502001` | Induced termination of pregnancy complicated by perforation of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379944009 Traumatic perforation of periurethral tissue during termination of pregnancy |
| `609503006` | Induced termination of pregnancy complicated by urinary bladder damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373915001 Traumatic injury of urinary bladder during termination of pregnancy |
| `609504000` | Induced termination of pregnancy complicated by bowel damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373905007 Traumatic injury of intestine during termination of pregnancy |
| `609505004` | Induced termination of pregnancy complicated by broad ligament damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379933001 Traumatic injury of broad ligament during termination of pregnancy |
| `609506003` | Induced termination of pregnancy complicated by cardiac arrest | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373916000 Cardiac arrest due to induced termination of pregnancy |
| `609507007` | Induced termination of pregnancy complicated by cardiac failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376017000 Cardiac failure due to induced termination of pregnancy |
| `609508002` | Induced termination of pregnancy complicated by cervix damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373911005 Traumatic injury of uterine cervix during termination of pregnancy |
| `609510000` | Induced termination of pregnancy complicated by infectious disease | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376022000 Infectious disease due to and following induced termination of pregnancy |
| `609511001` | Induced termination of pregnancy complicated by periurethral tissue damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379955009 Periurethral traumatic injury during termination of pregnancy |
| `609512008` | Induced termination of pregnancy complicated by oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373902005 Oliguria due to induced termination of pregnancy |
| `609513003` | Induced termination of pregnancy complicated by uterus damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373914002 Traumatic injury of uterus during termination of pregnancy |
| `609514009` | Induced termination of pregnancy complicated by vaginal damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373917009 Traumatic injury of vagina during termination of pregnancy |
| `61714007` | Metabolic disturbance in labor AND/OR delivery | inactivated (Classification derived) | REPLACED BY → 1395830004 Maternal metabolic disease during intrapartum period |
| `61947007` | Deaf mutism | inactivated (Outdated) | - |
| `62612003` | Fibrosis of perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381677004 Fibrosis of perineum during antenatal and/or intrapartum period |
| `62657007` | Cardiac arrest AND/OR failure following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386325001 Maternal cardiac arrest due to administration of anesthesia and/or sedation during intrapartum period, POSSIBLY EQUIVALENT TO → 1386326000 Maternal cardiac failure due to administration of anesthesia and/or sedation during intrapartum period |
| `63287004` | Benign essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373658004 Benign pre-existing essential hypertension during antenatal and/or intrapartum and/or postpartum period |
| `64171002` | Obstetrical cardiac complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386323008 Maternal disorder of heart due to administration of anesthesia and/or sedation during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1386324002 Maternal disorder of heart due to administration of anesthesia and/or sedation during intrapartum period |
| `65402008` | Pre-existing hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `65409004` | Obstetrical complication of anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `6636004` | Congenital cardiovascular disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `66709007` | Hypertensive renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373622006 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive renal disease |
| `66958002` | Isoimmunization from non-ABO, non-Rh blood-group incompatibility affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381707006 Maternal non-ABO, non-Rhesus blood-group isoimmunization during antenatal and/or intrapartum period |
| `68214002` | Lymphangitis of breast associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388394002 Lymphangitis of breast during postpartum |
| `69302000` | Termination of pregnancy on demand | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 57797005 Termination of pregnancy |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | - |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | - |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `699950009` | Anti-D isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `71639005` | Galactorrhea associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388264005 Maternal galactorrhea during postpartum period |
| `71874008` | Benign essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373569006 Maternal disorder during labor due to benign essential hypertension |
| `72022006` | Essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373656000 Pre-existing essential hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `721166000` | Human immunodeficiency virus complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380419009 Maternal human immunodeficiency virus infection during antenatal and/or intrapartum and/or postpartum period |
| `721177006` | Injury complicating pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402307005 Maternal injury during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 426997005 Maternal traumatic injury during antenatal and/or intrapartum period |
| `721201001` | Protozoal disease complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1376000007 Maternal disorder caused by Protozoa during antenatal and/or intrapartum and/or postpartum period |
| `721203003` | Sequela of complication of pregnancy childbirth and the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380411007 Disorder due to and following maternal disorder during antenatal and/or intrapartum and/or postpartum period |
| `722595002` | Overweight in adulthood with body mass index of 25 or more but less than 30 | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407012005 Overweight in adulthood, ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2 |
| `72280009` | Achromotrichia | inactivated (Erroneous) | REPLACED BY → 1402356006 Achromotrichia |
| `723091005` | Fistula of vagina and/or rectum and/or urinary bladder due to complication occurring during labor and/or delivery | inactivated (Classification derived) | REPLACED BY → 1395886004 Genital tract fistula following vaginal delivery |
| `724497009` | Disease of circulatory system complicating pregnancy childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380409003 Maternal circulatory disorder during antenatal and/or intrapartum and/or postpartum period |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `72860003` | Disorder of amniotic cavity AND/OR membrane | inactivated (Classification derived) | REPLACED BY → 609522002 Disorder of extraembryonic membrane |
| `73030000` | Hypertensive renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373661003 Pre-existing hypertensive renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `735492001` | Obstructed labor due to shoulder dystocia | inactivated (Duplicate) | SAME AS → 89700002 Shoulder girdle dystocia |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `737329004` | Damage to pelvic organs and tissues following ectopic pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397365008 Traumatic injury of soft tissue of pelvis due to and following ectopic pregnancy, POSSIBLY EQUIVALENT TO → 1397370001 Traumatic injury of organ of pelvis due to and following ectopic pregnancy |
| `737330009` | Damage to pelvic organs and tissues following molar pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397366009 Traumatic injury of soft tissue of pelvis due to and following molar pregnancy, POSSIBLY EQUIVALENT TO → 1397369002 Traumatic injury of organ of pelvis due to and following molar pregnancy |
| `73813001` | Elastosis senilis | inactivated (Outdated) | REPLACED BY → 43982006 Solar degeneration |
| `73837001` | Failed attempted termination of pregnancy with cardiac arrest and/or failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10750641000119101 Cardiac arrest due to failed attempted abortion, PARTIALLY EQUIVALENT TO → 1373227006 Failed attempted abortion with cardiac failure |
| `74227009` | Apraxic aphonia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441913003 Aphonia, POSSIBLY EQUIVALENT TO → 1407180006 Acquired apraxia of speech |
| `74955002` | Retracted nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388400000 Retraction of nipple during postpartum |
| `75150001` | Renal disease in pregnancy AND/OR puerperium without hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 733839001 Postpartum acute renal failure, PARTIALLY EQUIVALENT TO → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension, PARTIALLY EQUIVALENT TO → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `76037007` | Rigid cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381674006 Rigid cervix uteri during antenatal and/or intrapartum period |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `76751001` | Diabetes mellitus in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199223000 Maternal diabetes mellitus during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 609563008 Pre-existing diabetes mellitus in pregnancy |
| `76871004` | Previous surgery to vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381679001 Maternal disorder due to previous vaginal surgery during antenatal and/or intrapartum period |
| `77285007` | Placental infarct affecting management of mother | inactivated (Classification derived) | REPLACED BY → 268585006 Placental infarct |
| `77563000` | Obstruction by bony pelvis | inactivated (Duplicate) | SAME AS → 199757009 Obstructed labor caused by bony pelvis |
| `778075008` | Pityriasis simplex capitis | inactivated (Duplicate) | SAME AS → 400201008 Pityriasis capitis |
| `78381004` | Heart disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375991008 Maternal heart disorder during antenatal and/or intrapartum and/or postpartum period |
| `78697003` | Nonpurulent mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388395001 Nonpurulent mastitis during postpartum |
| `78808002` | Essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373618001 Disorder during maternal antenatal and/or intrapartum period due to essential hypertension |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79355007` | Hypertensive heart disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373662005 Pre-existing hypertensive heart disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | - |
| `79839005` | Perineal laceration involving vulva | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 237332009 Vulval tear, POSSIBLY EQUIVALENT TO → 1388876002 First degree laceration of perineum and laceration of vulva during vaginal delivery of fetus |
| `80818002` | Previous surgery to perineum AND/OR vulva affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1381693008 Maternal disorder due to previous procedure on perineum during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1381694002 Maternal disorder due to previous procedure on vulva during antenatal and/or intrapartum period |
| `81557008` | Parasitic disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375999005 Maternal disorder caused by parasite during antenatal and/or intrapartum and/or postpartum period |
| `81626002` | Malignant hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373657009 Malignant hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `8218002` | Chronic hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `83243004` | Rigid pelvic floor affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381673000 Rigid pelvic floor during antenatal and/or intrapartum period |
| `84007008` | Shock during AND/OR following labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381592008 Maternal shock due to and following delivery, POSSIBLY EQUIVALENT TO → 1381590000 Maternal shock during intrapartum period |
| `8445003` | Neoplasm of vulva affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381661000 Neoplasm of vulva during antenatal and/or intrapartum period |
| `84939004` | Rubella in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 270497005 Maternal rubella during antenatal and/or intrapartum and/or postpartum period |
| `85542007` | Perineal laceration involving skin | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388874004 Laceration of skin of perineum, POSSIBLY EQUIVALENT TO → 1388873005 First degree laceration of skin of perineum during vaginal delivery of fetus |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `86041002` | Pre-existing hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `87383005` | Maternal distress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period, POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period |
| `8762007` | Chronic hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `87840008` | Galactocele associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388398004 Galactocele during postpartum period |
| `88320008` | Drug tolerance | inactivated (Nonconformance to editorial policy) | REPLACED BY → 365992008 Drug tolerance - finding |
| `89672000` | Retromammary mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388397009 Retromammary mastitis during postpartum |
| `90645002` | Failed attempted termination of pregnancy without complication | inactivated (Nonconformance to editorial policy) | REPLACED BY → 49416000 Failed attempted termination of pregnancy |
| `9297001` | Bicornuate uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381667001 Bicornate uterus during antenatal and/or intrapartum period |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |
| `95606005` | Maternal drug exposure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `95607001` | Maternal drug use | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `9720009` | Cicatrix of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381675007 Cicatrix of cervix during antenatal and/or intrapartum period |

**New members (850):**

| Code | Display |
|---|---|
| `1000081000220104` | Impaired prone position tolerance in infancy |
| `1011441000220106` | History of cardiovascular procedure |
| `1011481000220101` | Calcification of left ventricular outflow tract |
| `1011491000220103` | Rupture of aortic annulus |
| `1011661000220107` | In-hospital stroke |
| `1011671000220101` | In-hospital myocardial infarction |
| `103406000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A1 |
| `103407009` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A2 |
| `103408004` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A3 |
| `103409007` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B1 |
| `103410002` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B2 |
| `103411003` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B3 |
| `103412005` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C1 AIDS (acquired immunodeficiency syndrome) |
| `103413000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C2 AIDS (acquired immunodeficiency syndrome) |
| `103414006` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C3 AIDS (acquired immunodeficiency syndrome) |
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `11851561000119100` | Nonvenomous insect bite of posterior chest wall |
| `12206071000119108` | Osteolysis of bone adjacent to right ankle joint prosthesis |
| `12206111000119101` | Osteolysis of bone adjacent to right elbow joint prosthesis |
| `12206151000119100` | Osteolysis of bone adjacent to right finger joint prosthesis |
| `12208881000119103` | Osteolysis of bone adjacent to right shoulder joint prosthesis |
| `12217281000119101` | Osteolysis of bone adjacent to left ankle joint prosthesis |
| `12217321000119106` | Osteolysis of bone adjacent to left elbow joint prosthesis |
| `12217361000119101` | Osteolysis of bone adjacent to left finger joint prosthesis |
| `12217481000119102` | Osteolysis of bone adjacent to left shoulder joint prosthesis |
| `129769006` | Calcification cluster |
| `134098971000119103` | Osteolysis of bone adjacent to finger joint prosthesis |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |

… 810 more, see the CSV.

### BREAKING · `mii-vs-kardio-klappenvitium-snomedct` (pinned, enumerated, filter)

MII VS Kardio Klappenvitium [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-klappenvitium-snomedct`  
Members: 814 → 815

- **Filter/enumerated anchor inactive:** `368009:{116676008=49755003,363698007=17401000},{246112005=24484000}`  — no successor

**New members (1):**

| Code | Display |
|---|---|
| `1011491000220103` | Rupture of aortic annulus |

### MINOR · `mii-vs-kardio-atherosklerotisches-ereignis-snomedct` (UNPINNED, filter)

MII VS Kardio Atherosklerotisches Ereignis [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-atherosklerotisches-ereignis-snomedct`  
Members: 372 → 421


**New members (49):**

| Code | Display |
|---|---|
| `1381732008` | Perinatal fetal and/or neonatal ischemic stroke |
| `153051000000108` | Fluoroscopic angiography of bilateral carotid arteries with contrast and bilateral insertion of stent |
| `153061000000106` | Fluoroscopic angiography of left carotid artery with contrast and insertion of stent |
| `153071000000104` | Fluoroscopic angiography of right carotid artery with contrast and insertion of stent |
| `153201000000104` | Fluoroscopy guided percutaneous transluminal angioplasty of right internal carotid artery with contrast |
| `153211000000102` | Fluoroscopy guided percutaneous transluminal angioplasty of left internal carotid artery with contrast |
| `153221000000108` | Fluoroscopy guided percutaneous transluminal angioplasty of bilateral internal carotid arteries with contrast |
| `153241000000101` | Fluoroscopic angiography of right internal carotid artery with contrast and insertion of stent graft |
| `153251000000103` | Fluoroscopic angiography of left internal carotid artery with contrast and insertion of stent graft |
| `153261000000100` | Fluoroscopic angiography of bilateral internal carotid arteries with contrast and bilateral insertion of stent graft |
| `153271000000107` | Fluoroscopic angiography of right external carotid artery with contrast and insertion of stent graft |
| `153281000000109` | Fluoroscopic angiography of left external carotid artery with contrast and insertion of stent graft |
| `153291000000106` | Fluoroscopic angiography of bilateral external carotid arteries with contrast and bilateral insertion of stent graft |
| `153301000000105` | Fluoroscopic angiography of right common carotid artery with contrast and insertion of stent graft |
| `153311000000107` | Fluoroscopic angiography of left common carotid artery with contrast and insertion of stent graft |
| `153321000000101` | Fluoroscopic angiography of bilateral common carotid arteries with contrast and bilateral insertion of stent graft |
| `153331000000104` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of right internal carotid artery with contrast |
| `153341000000108` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of left internal carotid artery with contrast |
| `153351000000106` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of bilateral internal carotid arteries with contrast |
| `153361000000109` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of right external carotid artery with contrast |
| `153371000000102` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of left external carotid artery with contrast |
| `153381000000100` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of bilateral external carotid arteries with contrast |
| `153391000000103` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of right common carotid artery with contrast |
| `153401000000100` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of left common carotid artery with contrast |
| `153411000000103` | Fluoroscopy guided percutaneous transluminal cutting balloon angioplasty of bilateral common carotid arteries with contrast |
| `153421000000109` | Fluoroscopic angiography of right internal carotid artery with contrast and insertion of stent |
| `153431000000106` | Fluoroscopic angiography of left internal carotid artery with contrast and insertion of stent |
| `153441000000102` | Fluoroscopic angiography of right external carotid artery with contrast and insertion of stent |
| `153451000000104` | Fluoroscopic angiography of left external carotid artery with contrast and insertion of stent |
| `153461000000101` | Fluoroscopic angiography of bilateral external carotid arteries with contrast and bilateral insertion of stent |
| `153471000000108` | Fluoroscopic angiography of right common carotid artery with contrast and insertion of stent |
| `153481000000105` | Fluoroscopic angiography of left common carotid artery with contrast and insertion of stent |
| `153491000000107` | Fluoroscopic angiography of bilateral common carotid arteries with contrast and bilateral insertion of stent |
| `153501000000101` | Fluoroscopic angiography of right internal carotid artery with contrast and insertion of drug eluting stent |
| `153511000000104` | Fluoroscopic angiography of left internal carotid artery with contrast and insertion of drug eluting stent |
| `153521000000105` | Fluoroscopic angiography of bilateral internal carotid arteries with contrast and bilateral insertion of drug eluting stent |
| `153531000000107` | Fluoroscopic angiography of right external carotid artery with contrast and insertion of drug eluting stent |
| `153541000000103` | Fluoroscopic angiography of left external carotid artery with contrast and insertion of drug eluting stent |
| `153551000000100` | Fluoroscopic angiography of bilateral external carotid arteries with contrast and bilateral insertion of drug eluting stent |
| `153561000000102` | Fluoroscopic angiography of right common carotid artery with contrast and insertion of drug eluting stent |

… 9 more, see the CSV.

### MINOR · `mii-vs-kardio-nyha-klassen-snomedct` (UNPINNED, filter)

MII VS Kardio NYHA Klassen [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-kardio/ValueSet/mii-vs-kardio-nyha-klassen-snomedct`  
Members: 4 → 12


**New members (8):**

| Code | Display |
|---|---|
| `60061000234106` | Left ventricular failure, New York Heart Association Classification Class I |
| `60071000234100` | Left ventricular failure, New York Heart Association Classification Class II |
| `60081000234102` | Left ventricular failure, New York Heart Association Classification Class III |
| `60091000234104` | Left ventricular failure, New York Heart Association Classification Class IV |
| `60101000234109` | Right ventricular failure, New York Heart Association Classification Class IV |
| `60111000234107` | Right ventricular failure, New York Heart Association Classification Class III |
| `60121000234100` | Right ventricular failure, New York Heart Association Classification Class II |
| `60131000234102` | Right ventricular failure, New York Heart Association Classification Class I |

## Module `lungenfunktion`

### SIGNIFICANT · `mii-vs-lufu-sct-findings` (pinned, filter)

MII VS Lufu SCT Findings  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-lungenfunktion/ValueSet/mii-vs-lufu-sct-findings`  
Members: 5103 → 5122


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `199293005` | Disease of the respiratory system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1380415003 Maternal disorder of respiratory system during antenatal and/or intrapartum and/or postpartum period |
| `267276009` | Obstetric anesthesia with pulmonary complications | inactivated (Classification derived) | REPLACED BY → 1379971009 Maternal pulmonary disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `51154004` | Obstetrical pulmonary complication of anesthesia AND/OR sedation | inactivated (Classification derived) | REPLACED BY → 1386327009 Maternal disorder of lung due to administration of anesthesia and/or sedation during intrapartum period |
| `51495008` | Cerebral anoxia following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1396086006 Maternal cerebral anoxia due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1396087002 Maternal cerebral anoxia due to and following sedation during intrapartum period |
| `609461007` | Induced termination of pregnancy complicated by cerebral anoxia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376016009 Cerebral anoxia due to induced termination of pregnancy |

**New members (24):**

| Code | Display |
|---|---|
| `1376016009` | Cerebral anoxia due to induced termination of pregnancy |
| `1379971009` | Maternal pulmonary disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `1380415003` | Maternal disorder of respiratory system during antenatal and/or intrapartum and/or postpartum period |
| `1386327009` | Maternal disorder of lung due to administration of anesthesia and/or sedation during intrapartum period |
| `1396086006` | Maternal cerebral anoxia due to and following anesthesia during intrapartum period |
| `1396087002` | Maternal cerebral anoxia due to and following sedation during intrapartum period |
| `1401642003` | Discomfort in throat |
| `1404527009` | Hantavirus cardiopulmonary syndrome caused by Orthohantavirus sinnombreense |
| `1404528004` | Hantavirus cardiopulmonary syndrome caused by Orthohantavirus andesense |
| `1406951008` | Aspiration pneumonitis following anesthesia |
| `1409187001` | Hyperemia of palatine tonsil |
| `1409258006` | Enlargement of bilateral palatine tonsils |
| `1409259003` | Hypertrophy of palatine tonsil |
| `1409309009` | Hypertrophy of left palatine tonsil |
| `1409310004` | Hypertrophy of right palatine tonsil |
| `383518801000119109` | Ventriculopleural shunt malfunction |
| `484141000087104` | Closed fracture of left maxillary sinus |
| `484151000087101` | Closed fracture of maxillary sinus |
| `484161000087103` | Closed fracture of right maxillary sinus |
| `484171000087107` | Fracture of maxillary sinus |
| `484311000087103` | Left hemopneumothorax |
| `484321000087106` | Right hemopneumothorax |
| `484331000087108` | Left hemothorax |
| `484341000087102` | Right hemothorax |

### SIGNIFICANT · `mii-vs-lufu-sct-observable` (pinned, filter)

MII VS Lufu SCT Observable  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-lungenfunktion/ValueSet/mii-vs-lufu-sct-observable`  
Members: 190 → 189


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `313221000` | Respiratory percentage | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 251880004 Respiratory measure |

## Module `mikrobio`

### BREAKING · `mii-vs-mikrobio-allgemeine-bestimmung-ergebnis-snomed` (pinned, enumerated)

MII VS Mikrobio Allgemeine Bestimmung Ergebnis [SNOMED]  
`https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-allgemeine-bestimmung-ergebnis-snomed`  
Members: 24678 → 24836


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `106652005` | Superfamily Rhabdiasoidea | inactivated (Outdated) | - |
| `113562007` | Clostridium adrichii | inactivated (Erroneous) | REPLACED BY → 432614007 Acetivibrio aldrichii |
| `114095004` | Paenibacillus gluconolyticus | inactivated (Erroneous) | REPLACED BY → 430611008 Paenibacillus glucanolyticus |
| `116663002` | Sin Nombre virus | inactivated (Duplicate) | SAME AS → 1389076007 Orthohantavirus sinnombreense |
| `12127000` | Clostridium dormicaceticum | inactivated (Erroneous) | REPLACED BY → 113574006 Andreesenella formicacetica |
| `302608002` | Alpha non-hemolytic streptococcus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 414871004 Non-Beta-hemolytic Streptococcus, POSSIBLY EQUIVALENT TO → 22339002 Gamma-hemolytic Streptococcus, POSSIBLY EQUIVALENT TO → 60631002 Alpha-hemolytic streptococcus |
| `49445003` | Genus Hantavirus | inactivated (Outdated) | REPLACED BY → 735350007 Orthohantavirus |
| `64620000` | Asdravirus | inactivated (Nonconformance to editorial policy) | - |
| `90736006` | Eimeria ninakolyakimovae | inactivated (Erroneous) | REPLACED BY → 57949004 Eimeria ninakohlyakimovae |

**New members (167):**

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
| `1407056005` | Carbapenemase-producing Pseudomonas putida |
| `1407057001` | Carbapenemase-producing Pseudomonas otitidis |
| `1407058006` | Carbapenemase-producing Pseudomonas nitroreducens |
| `1407059003` | Carbapenemase-producing Pseudomonas monteilii |
| `1407060008` | Carbapenemase-producing Pseudomonas fulva |
| `1407061007` | Carbapenemase-producing Pseudomonas fluorescens |
| `1407062000` | Carbapenemase-producing Pseudomonas citronellolis |
| `1407063005` | Carbapenemase-producing Pseudomonas alcaligenes |
| `1407064004` | Carbapenemase-producing Proteus vulgaris |
| `1407065003` | Carbapenemase-producing Enterobacter ludwigii |
| `1407066002` | Carbapenemase-producing Burkholderia |
| `1407067006` | Carbapenemase-producing Alcaligenes |
| `1407068001` | Carbapenemase-producing Aeromonas |
| `1407069009` | Carbapenemase-producing Achromobacter |
| `1407088002` | Orthohantavirus tulaense |
| `1407106002` | Orthohantavirus wufangense |
| `1407107006` | Wùfeng Chodsigoa smithii orthohantavirus 1 |
| `1407137002` | Orthohantavirus tigrayense |
| `1407138007` | Orthohantavirus thailandense |
| `1407139004` | Orthohantavirus tatenalense |
| `1407140002` | Orthohantavirus sangassouense |
| `1407141003` | Orthohantavirus sagercreekense |

… 127 more, see the CSV.

### SIGNIFICANT · `mii-vs-mikrobio-organismen-snomedct` (pinned, filter)

MII VS Mikrobio Organismen [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-organismen-snomedct`  
Members: 24677 → 24835


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `106652005` | Superfamily Rhabdiasoidea | inactivated (Outdated) | - |
| `113562007` | Clostridium adrichii | inactivated (Erroneous) | REPLACED BY → 432614007 Acetivibrio aldrichii |
| `114095004` | Paenibacillus gluconolyticus | inactivated (Erroneous) | REPLACED BY → 430611008 Paenibacillus glucanolyticus |
| `116663002` | Sin Nombre virus | inactivated (Duplicate) | SAME AS → 1389076007 Orthohantavirus sinnombreense |
| `12127000` | Clostridium dormicaceticum | inactivated (Erroneous) | REPLACED BY → 113574006 Andreesenella formicacetica |
| `302608002` | Alpha non-hemolytic streptococcus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 414871004 Non-Beta-hemolytic Streptococcus, POSSIBLY EQUIVALENT TO → 22339002 Gamma-hemolytic Streptococcus, POSSIBLY EQUIVALENT TO → 60631002 Alpha-hemolytic streptococcus |
| `49445003` | Genus Hantavirus | inactivated (Outdated) | REPLACED BY → 735350007 Orthohantavirus |
| `64620000` | Asdravirus | inactivated (Nonconformance to editorial policy) | - |
| `90736006` | Eimeria ninakolyakimovae | inactivated (Erroneous) | REPLACED BY → 57949004 Eimeria ninakohlyakimovae |

**New members (167):**

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
| `1407056005` | Carbapenemase-producing Pseudomonas putida |
| `1407057001` | Carbapenemase-producing Pseudomonas otitidis |
| `1407058006` | Carbapenemase-producing Pseudomonas nitroreducens |
| `1407059003` | Carbapenemase-producing Pseudomonas monteilii |
| `1407060008` | Carbapenemase-producing Pseudomonas fulva |
| `1407061007` | Carbapenemase-producing Pseudomonas fluorescens |
| `1407062000` | Carbapenemase-producing Pseudomonas citronellolis |
| `1407063005` | Carbapenemase-producing Pseudomonas alcaligenes |
| `1407064004` | Carbapenemase-producing Proteus vulgaris |
| `1407065003` | Carbapenemase-producing Enterobacter ludwigii |
| `1407066002` | Carbapenemase-producing Burkholderia |
| `1407067006` | Carbapenemase-producing Alcaligenes |
| `1407068001` | Carbapenemase-producing Aeromonas |
| `1407069009` | Carbapenemase-producing Achromobacter |
| `1407088002` | Orthohantavirus tulaense |
| `1407106002` | Orthohantavirus wufangense |
| `1407107006` | Wùfeng Chodsigoa smithii orthohantavirus 1 |
| `1407137002` | Orthohantavirus tigrayense |
| `1407138007` | Orthohantavirus thailandense |
| `1407139004` | Orthohantavirus tatenalense |
| `1407140002` | Orthohantavirus sangassouense |
| `1407141003` | Orthohantavirus sagercreekense |

… 127 more, see the CSV.

## Module `onko`

### BREAKING · `mii-vs-onko-prostata-operation-snomedct` (UNPINNED, enumerated, filter)

MII VS Onko Prostata Operation SNOMED CT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-prostata-operation-snomedct`  
Members: 190 → 189


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `725959008` | Transurethral insertion of prostatic urethral lift implant | status active, no longer matches the filter (property changed) | - |

### SIGNIFICANT · `mii-vs-onko-koerperstruktur-sct` (UNPINNED, filter)

MII VS Onkologie Körperstruktur (SNOMED CT)  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-koerperstruktur-sct`  
Members: 45088 → 45993


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `110708006` | Middle ear and mastoid cells | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure, POSSIBLY EQUIVALENT TO → 57222008 Structure of mastoid cell |
| `1156631003` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 703822002 Indeterminate dendritic cell tumor |
| `1186646003` | Malignant histiocytic neoplasm | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `1187282008` | Polyostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `1187283003` | Monostotic Langerhans cell histiocytosis | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `118974004` | Entire subdivision of female genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361386004 Entire female genital system |
| `118975003` | Entire subdivision of male genital system | inactivated (Nonconformance to editorial policy) | REPLACED BY → 361340001 Entire male genital system |
| `128810002` | Eosinophilic granuloma | inactivated (Outdated) | REPLACED BY → 1187281001 Single system Langerhans cell histiocytosis |
| `128811003` | Langerhans cell histiocytosis, multifocal | inactivated (Outdated) | REPLACED BY → 110450007 Langerhans cell histiocytosis |
| `128920006` | Malignant histiocytosis | inactivated (Outdated) | REPLACED BY → 1396874009 Malignant histiocytic macrophage neoplasm |
| `14494009` | Meningeal sarcomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 9395006 Sarcomatosis |
| `18971008` | Entire iliopectineal bursa | inactivated (Duplicate) | SAME AS → 289364009 Entire iliopsoas bursa |
| `190802005` | Pelvic lipomatosis | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1416374007 Pelvic lipomatosis |
| `23041001` | Sinus histiocytosis | inactivated (Outdated) | REPLACED BY → 1295376005 Rosai-Dorfman disease |
| `244079007` | Skin of eardrum | inactivated (Duplicate) | SAME AS → 39725007 Outer epithelial layer of tympanic membrane |
| `289465009` | Structure of iliopectineal bursa | inactivated (Duplicate) | SAME AS → 9320007 Structure of iliopsoas bursa |
| `361107003` | Entire genital system | inactivated (Duplicate) | SAME AS → 278875001 Entire reproductive system |
| `363667005` | Middle ear and mastoid structure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 59066005 Mastoid structure, POSSIBLY EQUIVALENT TO → 25342003 Middle ear structure |
| `399456004` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1187107005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 1162576007 Plasma cell myeloma |
| `405952001` | Parameningeal structure in the context of malignancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 406121007 Structure of subregion of head |
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
| `732139009` | Entire middle ear and mastoid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 181185000 Entire middle ear, POSSIBLY EQUIVALENT TO → 265784008 Entire mastoid |
| `788217009` | Structure of hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788196007 Structure of hair follicle of foot |
| `788257007` | Entire hair follicle of heel | inactivated (Erroneous) | REPLACED BY → 788256003 Entire hair follicle of foot |

**New members (940):**

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
| `1381538009` | Structure of lumen of uterine cervix |
| `1381539001` | Entire lumen of uterine cervix |
| `1395883007` | Bone structure of finger joint region |
| `1395884001` | Bone structure of finger joint region of left hand |
| `1395885000` | Bone structure of finger joint region of right hand |
| `1395887008` | Entire bone of finger joint region |
| `1396106007` | Skin structure of left half of thoracic segment of trunk |
| `1396107003` | Skin structure of right half of thoracic segment of trunk |
| `1396874009` | Malignant histiocytic macrophage neoplasm |
| `1397665002` | Skin and/or subcutaneous tissue structure of calf of leg |
| `1397666001` | Entire skin and subcutaneous tissue of calf of leg |
| `1397669008` | Skin and/or subcutaneous tissue structure of sacral region of back |
| `1397670009` | Entire skin and/or subcutaneous tissue structure of sacral region of back |
| `1399105005` | Structure of left thoracodorsal artery |
| `1399106006` | Structure of right thoracodorsal artery |
| `1399107002` | Structure of left superior epigastric artery |
| `1399108007` | Structure of right superior epigastric artery |
| `1399109004` | Structure of blood vessel of left hand |
| `1399110009` | Structure of blood vessel of right hand |
| `1399237003` | Structure of left inferior epigastric artery |
| `1399238008` | Structure of right inferior epigastric artery |
| `1399566001` | CD79A gene |
| `1399567005` | CD79B gene |
| `1399568000` | CDHR1 gene |
| `1399569008` | CDKL5 gene |

… 900 more, see the CSV.

### MINOR · `mii-vs-onko-mamma-intraoperatives-imaging-praeparat` (UNPINNED, filter)

MII VS Onkologie Mamma Intraoperatives Imaging Präparat  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-mamma-intraoperatives-imaging-praeparat`  
Members: 12 → 13


**New members (1):**

| Code | Display |
|---|---|
| `1094061000000105` | Plain X-ray of tissue specimen of bilateral breasts |

### MINOR · `mii-vs-onko-mamma-operation-sct` (UNPINNED, filter)

MII VS Onkologie Mamma Operation SNOMED CT  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-mamma-operation-sct`  
Members: 368 → 382


**New members (14):**

| Code | Display |
|---|---|
| `1397403002` | Digital tomosynthesis guided vacuum assisted excision of breast |
| `156841000000108` | Ultrasonography guided vacuum assisted excision of left breast |
| `156851000000106` | Ultrasonography guided vacuum assisted excision of right breast |
| `156861000000109` | Ultrasonography guided vacuum assisted excision of bilateral breasts |
| `156901000000102` | Stereotactic plain X-ray guided vacuum assisted excision of lesion of left breast |
| `156911000000100` | Stereotactic plain X-ray guided vacuum assisted excision of lesion of right breast |
| `156921000000106` | Stereotactic plain X-ray guided vacuum assisted excision of lesion of bilateral breasts |
| `156931000000108` | Ultrasonography guided vacuum assisted excision of lesion of left breast |
| `156941000000104` | Ultrasonography guided vacuum assisted excision of lesion of right breast |
| `156951000000101` | Ultrasonography guided vacuum assisted excision of lesion of bilateral breasts |
| `1771741000000104` | Digital tomosynthesis guided vacuum assisted excision of right breast |
| `1812601000000107` | Digital tomosynthesis guided vacuum assisted excision of left breast |
| `1812611000000109` | Digital tomosynthesis guided vacuum assisted excision of bilateral breasts |
| `664411000146106` | Lumpectomy of breast using implantable magnetic lesion localization marker |

## Module `patho`

### SIGNIFICANT · `mii-vs-patho-collection-method-snomed-ct` (UNPINNED, filter)

MII VS Patho Collection Method [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-collection-method-snomed-ct`  
Members: 11024 → 11296


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `174625005` | Endoscopic change of biliary stent | inactivated (Duplicate) | SAME AS → 709467007 Fluoroscopy guided endoscopic retrograde cholangiopancreatography with replacement of bile duct stent |
| `176374004` | Hook ablation of posterior urethral valve | status active, no longer matches the filter (property changed) | - |
| `23864003` | Esophagoscopy for biopsy and collection of specimen by brushing or washing | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 71658001 Esophagoscopy for biopsy, POSSIBLY EQUIVALENT TO → 1370946001 Esophagoscopy with brush biopsy and washing |
| `265455000` | Endoscopic sphincterotomy of sphincter of Oddi and removal of calculus | inactivated (Duplicate) | SAME AS → 235583009 Fluoroscopy guided endoscopic retrograde cholangiopancreatography with sphincterotomy of sphincter of Oddi and calculus removal |
| `288010005` | Urethral removal of ureteric calculus | inactivated (Nonconformance to editorial policy) | - |
| `66399003` | Take-down of cerebral ventricular shunt | inactivated (Duplicate) | SAME AS → 288846002 Cerebrospinal fluid shunt removal |

**New members (278):**

| Code | Display |
|---|---|
| `1118531000000107` | Ultrasonography guided percutaneous fine needle aspiration biopsy of bilateral inguinal regions |
| `1123651000000100` | Ultrasonography guided percutaneous fine needle aspiration biopsy of left inguinal region |
| `1126681000000100` | Pneumocystography of left breast |
| `1126691000000103` | Pneumocystography of right breast |
| `1126701000000103` | Cone beam CT guided aspiration of left lower limb |
| `1126711000000101` | Cone beam CT guided aspiration of right lower limb |
| `1126721000000107` | Cone beam CT guided aspiration of bilateral lower limbs |
| `1126751000000102` | Cone beam CT guided aspiration of bilateral upper limbs |
| `1126761000000104` | Cone beam CT guided aspiration of left upper limb |
| `1126771000000106` | Cone beam CT guided aspiration of right upper limb |
| `1128771000000107` | Ultrasonography guided percutaneous fine needle aspiration biopsy of right inguinal region |
| `1137361000000102` | Cone beam CT guided biopsy of left lower limb |
| `1137371000000109` | Cone beam CT guided biopsy of right lower limb |
| `1137381000000106` | Cone beam CT guided biopsy of bilateral lower limbs |
| `1137391000000108` | Cone beam CT guided biopsy of left upper limb |
| `1137401000000106` | Cone beam CT guided biopsy of right upper limb |
| `1137411000000108` | Cone beam CT guided biopsy of bilateral upper limbs |
| `1147091000000107` | Fluoroscopy guided aspiration of left elbow region |
| `1147101000000104` | Fluoroscopy guided aspiration of right elbow region |
| `1147161000000100` | Fluoroscopy guided aspiration of bilateral feet |
| `1147171000000107` | Fluoroscopy guided aspiration of left foot |
| `1147181000000109` | Fluoroscopy guided aspiration of right foot |
| `1147191000000106` | Fluoroscopy guided aspiration of bilateral hands |
| `1147201000000108` | Fluoroscopy guided aspiration of left hand |
| `1147211000000105` | Fluoroscopy guided aspiration of right hand |
| `1147221000000104` | Aspiration of bilateral hip regions using fluoroscopic guidance |
| `1147231000000102` | Fluoroscopy guided aspiration of left hip region |
| `1147241000000106` | Fluoroscopy guided aspiration of right hip region |
| `1147431000000101` | Fluoroscopy guided biopsy of left knee region |
| `1147451000000108` | Fluoroscopy guided biopsy of right knee region |
| `1147461000000106` | Fluoroscopy guided biopsy of bilateral knee regions |
| `1147471000000104` | Fluoroscopy guided biopsy of left shoulder region |
| `1147481000000102` | Fluoroscopy guided biopsy of right shoulder region |
| `1147491000000100` | Fluoroscopy guided biopsy of bilateral shoulder regions |
| `1147501000000106` | Fluoroscopy guided biopsy of left wrist region |
| `1147521000000102` | Fluoroscopy guided biopsy of right wrist region |
| `1147531000000100` | Fluoroscopy guided biopsy of bilateral wrist regions |
| `1147721000000107` | Fluoroscopy guided aspiration of bilateral knee regions |
| `1147731000000109` | Fluoroscopy guided aspiration of left knee region |
| `1147741000000100` | Fluoroscopy guided aspiration of right knee region |

… 238 more, see the CSV.

### SIGNIFICANT · `mii-vs-patho-problem-list-snomed-ct` (UNPINNED, filter)

MII VS Patho Problem List [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-problem-list-snomed-ct`  
Members: 129019 → 129419

- Content note (not a release change): anchor `409586006` Complaint was already status inactive (Nonconformance to editorial policy) under the baseline
- Content note (not a release change): anchor `248536006` Finding of functional performance and activity was already status inactive (Nonconformance to editorial policy) under the baseline

**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `10562009` | Malignant hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373612000 Maternal disorder in labor due to malignant hypertension |
| `105709005` | Disease caused by Rhabdiasoidea | inactivated (Outdated) | - |
| `106005003` | Hypertension AND/OR vomiting complicating pregnancy childbirth AND/OR puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension, PARTIALLY EQUIVALENT TO → 90325002 Vomiting of pregnancy |
| `106008001` | Delivery AND/OR maternal condition affecting management | inactivated (Classification derived) | REPLACED BY → 1269075002 Maternal disorder during intrapartum period |
| `106009009` | Fetal condition affecting obstetrical care of mother | inactivated (Classification derived) | REPLACED BY → 70591005 Fetal disorder |
| `106010004` | Pelvic dystocia AND/OR uterine disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 79748007 Maternal dystocia, POSSIBLY EQUIVALENT TO → 12337004 Disorder of uterus, POSSIBLY EQUIVALENT TO → 1381465004 Labor dystocia |
| `10741911000119103` | Abnormal cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381664008 Abnormal cervix during antenatal and/or intrapartum period |
| `10743831000119100` | Neoplasm of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381663002 Neoplasm of uterus during antenatal and/or intrapartum period |
| `10743881000119104` | Suspected fetal abnormality affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 609520005 Disorder of fetal structure, PARTIALLY EQUIVALENT TO → 609415007 Fetal disorder suspected |
| `10749811000119108` | Obstetric anesthesia with central nervous system complication in childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `10808861000119105` | Maternal distress during childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period, POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period |
| `10835971000119109` | Anti-A sensitization in pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388946008 Maternal anti-A isoimmunization during antenatal and/or intrapartum period |
| `10853001` | Obstetrical complication of general anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380040003 Maternal disorder due to administration of general anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `10884004` | Threatened miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 6383007 Premature labor |
| `10897531000119101` | Open wound of female external genitalia | inactivated (Duplicate) | SAME AS → 210438000 Open wound of vulva |
| `10950002` | Vulval hematoma during delivery | inactivated (Duplicate) | SAME AS → 249217005 Maternal hematoma of vulva during intrapartum period |
| `111360009` | Obstipation | inactivated (Outdated) | REPLACED BY → 236069009 Chronic constipation |
| `111362001` | Anal furunculosis | inactivated (Nonconformance to editorial policy) | - |
| `111438007` | Hypertension secondary to renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373660002 Hypertension due to renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `111447004` | Placental condition affecting management of mother | inactivated (Classification derived) | REPLACED BY → 125586008 Disorder of placenta |
| `111459000` | Infection of nipple, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum |
| `1142291001` | Achromotrichia of eyebrow | inactivated (Erroneous) | REPLACED BY → 1402357002 Achromotrichia of eyebrow |
| `1145232003` | Premature grayness of hair of body | inactivated (Erroneous) | REPLACED BY → 1402358007 Premature grayness of hair of body |
| `1156495004` | Dendritic cell sarcoma | inactivated (Classification derived) | REPLACED BY → 721313009 Indeterminate dendritic cell neoplasm |
| `1163527006` | Epilepsy due to parasitic disease | inactivated (Erroneous) | REPLACED BY → 1397332000 Epilepsy due to parasitic disease of brain |
| `1163529009` | Epilepsy due to bacterial endocarditis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373925006 Epilepsy due to infectious abscess of brain, POSSIBLY EQUIVALENT TO → 1373924005 Epilepsy due to infectious disease |
| `1179359005` | Maternal epilepsy due to perinatal stroke | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380178003 Epilepsy due to and following stroke |
| `1179360000` | Fetal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `1179547007` | Neonatal epilepsy due to perinatal stroke | inactivated (Erroneous) | REPLACED BY → 1381734009 Epilepsy due to and following perinatal fetal and/or neonatal stroke |
| `118612006` | Malignant histiocytosis (clinical) | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `1186810009` | Erythropoietic protoporphyria due to gain of function of erythroid-specific aminolevulinic acid synthase 2 | inactivated (Duplicate) | SAME AS → 1197360001 X-linked dominant erythropoietic protoporphyria |
| `11914001` | Transverse OR oblique presentation of fetus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 73161006 Transverse lie, POSSIBLY EQUIVALENT TO → 63750008 Oblique lie |
| `120001000119107` | Group B streptococcus carrier complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1397016006 Maternal group B streptococcus carrier during antenatal and/or intrapartum period |
| `1208862000` | Acquired poliosis of eyelash | inactivated (Erroneous) | REPLACED BY → 1402368002 Acquired poliosis of eyelash |
| `1220564001` | Incomplete induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373920001 Shock due to and following incomplete termination of pregnancy |
| `1220586000` | Incomplete induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373870002 Renal failure due to and following incomplete termination of pregnancy |
| `1220625008` | Incomplete induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376019002 Metabolic disorder due to and following incomplete termination of pregnancy |
| `1220626009` | Incomplete induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379949004 Pelvic inflammatory disease due to and following incomplete termination of pregnancy |
| `1220630007` | Incomplete induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376023005 Embolism due to and following incomplete termination of pregnancy |
| `1220631006` | Incomplete induced termination of pregnancy complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379950004 Delayed hemorrhage due to and following incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379951000 Excessive hemorrhage due to and following incomplete induced termination of pregnancy |
| `1220632004` | Incomplete induced termination of pregnancy complicated by damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379948007 Traumatic injury of soft tissue of pelvis during incomplete termination of pregnancy, POSSIBLY EQUIVALENT TO → 1379947002 Traumatic injury of pelvic organ during incomplete termination of pregnancy |
| `1220657009` | Damage to pelvic organs and/or tissue due to and following complete induced termination of pregnancy | inactivated (Classification derived) | REPLACED BY → 1375964006 Traumatic injury of pelvic organ during complete termination of pregnancy |
| `1254988002` | Substance dependence in mother complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `1260371006` | Epilepsy due to perinatal cerebral ischemia | inactivated (Erroneous) | REPLACED BY → 1381728002 Epilepsy due to and following perinatal fetal and/or neonatal ischemic cerebrovascular accident |
| `1260377005` | Epilepsy due to congenital anomaly of brain | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1372772007 Epilepsy due to intracranial structural abnormality |
| `1269073009` | Fetal disorder due to disorder of amniotic cavity and/or membrane | inactivated (Classification derived) | REPLACED BY → 1384151007 Fetal disorder due to disorder of extraembryonic membrane |
| `1269102002` | Fetal disorder due to maternal disorder during pregnancy | inactivated (Duplicate) | SAME AS → 609429008 Fetal disorder due to disease in mother |
| `126944002` | Brain disorder resulting from a period of impaired oxygen delivery to the brain | inactivated (Erroneous) | REPLACED BY → 1381325002 Hypoxic brain injury |
| `1269476005` | At increased risk for complication during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1392349003 At increased risk for maternal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1392350003 At increased risk for fetal disorder during intrapartum period |
| `127070008` | Malignant histiocytic disorder | inactivated (Outdated) | REPLACED BY → 1399256008 Malignant histiocytic macrophage neoplasm |
| `128076000` | Bone AND/OR joint disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380433009 Maternal disorder of bone and/or joint during antenatal and/or intrapartum and/or postpartum period |
| `12867002` | Fetal distress affecting management of mother | inactivated (Classification derived) | REPLACED BY → 130955003 Nonreassuring fetal status |
| `1354494000` | Induced termination of pregnancy complicated by damage to urethra | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376018005 Traumatic injury of urethra during termination of pregnancy |
| `1354668000` | Fibrositis of upper limb | inactivated (Outdated) | - |
| `1354669008` | Fibrositis of upper arm | inactivated (Outdated) | - |
| `13866000` | Fetal acidemia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382318006 Fetal acidemia |
| `13943000` | Failed attempted termination of pregnancy complicated by embolism | inactivated (Duplicate) | SAME AS → 198812002 Failed attempted termination of pregnancy with embolism |
| `14022007` | Fetal death, affecting management of mother | inactivated (Classification derived) | REPLACED BY → 276507005 Fetal death |
| `140391000119101` | Ulcer of toe due to type 2 diabetes mellitus | inactivated (Duplicate) | SAME AS → 10656271000119102 Skin ulcer of toe due to diabetes mellitus type 2 |
| `14240001` | Poliosis | inactivated (Erroneous) | REPLACED BY → 1402362001 Poliosis |
| `1474004` | Hypertensive heart AND renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373630007 Disorder during maternal intrapartum period due to hypertensive heart and renal disease |
| `1538006` | Fetal malformation of central nervous system affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 9721000119107 Fetal malformation of central nervous system |
| `15406009` | Retromammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388404009 Retromammary abscess during postpartum |
| `15954901000119100` | Pendulous left breast | inactivated (Duplicate) | SAME AS → 15954981000119108 Ptosis of left breast |
| `15954941000119103` | Bilateral pendulous breasts | inactivated (Duplicate) | SAME AS → 15955061000119104 Bilateral ptotic breasts |
| `162135003` | Urine looks pale | inactivated (Duplicate) | SAME AS → 167234002 Pale urine |
| `162863004` | Body mass index 25-29 - overweight | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2, ALTERNATIVE → 1407012005 Overweight in adulthood |
| `162864005` | Body mass index 30+ - obesity | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 414916001 Obesity, ALTERNATIVE → 414915002 Obese, ALTERNATIVE → 1407009007 Adult body mass index greater than or equal to 30 kg/m2 |
| `1639007` | Abnormality of organs AND/OR soft tissues of pelvis affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 199446000 Maternal abnormality of pelvic soft tissue during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1381684007 Maternal disorder of pelvic organ during antenatal and/or intrapartum period |
| `169887003` | Birth length equal to third centile | inactivated (Erroneous) | REPLACED BY → 1411483000 Birth length equal to or less than third centile |
| `171000119107` | Maternal obesity complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380417006 Maternal obesity during antenatal and/or intrapartum and/or postpartum period |
| `17594002` | Fetal bradycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240299002 Fetal bradycardia |
| `18237006` | Parenchymatous mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388396000 Parenchymatous mastitis during postpartum |
| `18416000` | Essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373617006 Disorder during maternal intrapartum period due to essential hypertension |
| `187794005` | Malignant neoplasm of Islets of Langerhans | inactivated (Duplicate) | SAME AS → 254611009 Malignant neoplasm of endocrine pancreas |
| `190737001` | Iminoacidopathy | inactivated (Outdated) | REPLACED BY → 37800003 Disorder of proline AND/OR hydroxyproline metabolism |
| `197028009` | Dietetic gastritis | inactivated (Duplicate) | SAME AS → 1401596005 Allergic gastritis caused by food |
| `197030006` | Dietetic enterocolitis | inactivated (Duplicate) | SAME AS → 1401594008 Allergic enterocolitis caused by food |
| `197140007` | Secondary megacolon - congenital | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 197141006 Secondary acquired megacolon, POSSIBLY EQUIVALENT TO → 204739008 Congenital aganglionic megacolon |
| `19773009` | Infection of the breast AND/OR nipple associated with childbirth | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388392003 Infection of nipple during postpartum, PARTIALLY EQUIVALENT TO → 1388391005 Infection of breast during postpartum |
| `198609003` | Complication of pregnancy, childbirth and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269101009 Maternal disorder during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder |
| `198617006` | Delivery of viable fetus in abdominal pregnancy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 237253003 Viable fetus in abdominal pregnancy |
| `198655001` | Complete miscarriage with genital tract or pelvic infection | inactivated (Classification derived) | REPLACED BY → 1397373004 Genital tract infection due to and following complete miscarriage |
| `198656000` | Complete miscarriage with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397338001 Excessive hemorrhage due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397337006 Delayed hemorrhage due to and following complete miscarriage |
| `198657009` | Complete miscarriage with damage to pelvic organs or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397364007 Traumatic injury of soft tissue of pelvis due to and following complete miscarriage, POSSIBLY EQUIVALENT TO → 1397371002 Traumatic injury of organ of pelvis due to and following complete miscarriage |
| `19866007` | Previous operation to cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381692003 Maternal disorder due to previous uterine cervix surgery during antenatal and/or intrapartum period |
| `198806007` | Failed attempted termination of pregnancy with genital tract or pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection, PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection |
| `198807003` | Failed attempted termination of pregnancy with delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198808008` | Failed attempted termination of pregnancy with damage to pelvic organ or tissues | inactivated (Classification derived) | REPLACED BY → 1375968009 Failed attempted abortion with traumatic injury to pelvic organ |
| `198832001` | Damage to pelvic organs or tissues following abortive pregnancy | inactivated (Classification derived) | REPLACED BY → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `198874006` | Failed medical termination of pregnancy, complicated by genital tract or pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373432005 Failed medical abortion with pelvic infection, POSSIBLY EQUIVALENT TO → 1373431003 Failed medical abortion with genital tract infection |
| `198875007` | Failed medical termination of pregnancy, complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion |
| `198941007` | Hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `198942000` | Benign essential hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `198949009` | Renal hypertension complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `198997005` | Pre-eclampsia or eclampsia with pre-existing hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 67359005 Pre-eclampsia added to pre-existing hypertension, PARTIALLY EQUIVALENT TO → 69909000 Eclampsia added to pre-existing hypertension |
| `199005000` | Pre-existing hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1373810005 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertension |
| `199006004` | Pre-existing hypertensive heart disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373739002 Maternal disorder during antenatal and/or intrapartum and/or postpartum period due to hypertensive heart disease |
| `199007008` | Pre-existing hypertensive heart and renal disease complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1373732006 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to pre-existing hypertensive heart and renal disease |
| `199008003` | Pre-existing secondary hypertension complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380416002 Pre-existing secondary hypertension during antenatal and/or intrapartum and/or postpartum period |
| `199203001` | Viral hepatitis complicating pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380412000 Maternal viral hepatitis during antenatal and/or intrapartum and/or postpartum period |
| `199257008` | Mental disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1396772000 Mental disorder during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1258898000 Mental disorder during puerperium |
| `199279003` | Orthopedic disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period |
| `199293005` | Disease of the respiratory system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1380415003 Maternal disorder of respiratory system during antenatal and/or intrapartum and/or postpartum period |
| `199294004` | Disease of the digestive system complicating pregnancy, childbirth and/or the puerperium | inactivated (Classification derived) | REPLACED BY → 1376007005 Maternal disorder of digestive system during antenatal and/or intrapartum and/or postpartum period |
| `199295003` | Disease of skin and subcutaneous tissue complicating pregnancy, childbirth and/or puerperium | inactivated (Classification derived) | REPLACED BY → 1380413005 Maternal disorder of skin and/or subcutaneous tissue during antenatal and/or intrapartum and/or postpartum period |
| `199296002` | Endocrine, nutritional and metabolic disease complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380430007 Maternal nutritional disorder during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 1380431006 Maternal metabolic disorder during antenatal and/or intrapartum and/or postpartum period |
| `199297006` | Disease of nervous system complicating pregnancy, childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380418001 Maternal disorder of nervous system during antenatal and/or intrapartum and/or postpartum period |
| `199305006` | Complications specific to multiple gestation | inactivated (Classification derived) | REPLACED BY → 1379972002 Maternal disorder due to multiple pregnancy |
| `199314001` | Normal delivery but ante- or post- natal conditions present | inactivated (Classification derived) | REPLACED BY → 48782003 Delivery normal |
| `199322008` | Triplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 64254006 Triplet pregnancy |
| `199326006` | Quadruplet pregnancy with antenatal problem | inactivated (Classification derived) | REPLACED BY → 60810003 Quadruplet pregnancy |
| `199578005` | Fetal-maternal hemorrhage with antenatal problem | inactivated (Classification derived) | REPLACED BY → 71028008 Fetal-maternal hemorrhage |
| `199595002` | Labor and delivery complication by meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period |
| `199596001` | Labor and delivery complicated by fetal heart rate anomaly with meconium in amniotic fluid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389112004 Abnormal fetal heart rate with meconium stained amniotic fluid during intrapartum period |
| `199597005` | Labor and delivery complicated by biochemical evidence of fetal stress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389146003 Fetal distress with fetal acidosis during intrapartum period |
| `199678003` | Amniotic cavity infection with antenatal problem | inactivated (Classification derived) | REPLACED BY → 10573002 Infection of amniotic cavity |
| `199745000` | Complication occurring during labor and delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `199935005` | Fourth degree perineal tear during delivery with postnatal problem | inactivated (Classification derived) | REPLACED BY → 399031001 Fourth degree perineal laceration |
| `200046004` | Complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1381276002 Maternal disorder due to administration of anesthesia during intrapartum period |
| `200054002` | Obstetric anesthesia with cardiac complications | inactivated (Classification derived) | REPLACED BY → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200061003` | Obstetric anesthesia with central nervous system complications | inactivated (Classification derived) | REPLACED BY → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `200077002` | Cardiac complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period |
| `200078007` | Central nervous system complications of anesthesia during labor and delivery | inactivated (Classification derived) | REPLACED BY → 1379975000 Maternal central nervous system disorder due to anesthesia during intrapartum period |
| `200766001` | Parakeratosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 56585003 Parakeratosis of skin, POSSIBLY EQUIVALENT TO → 65068000 Parakeratosis |
| `200948000` | Pityriasis rubra (Hebra) | inactivated (Outdated) | REPLACED BY → 399992009 Erythroderma |
| `200985008` | Parapsoriasis varioliformis | inactivated (Outdated) | REPLACED BY → 86487001 Acute lichenoid pityriasis |
| `201174003` | Poliosis eccentrica | inactivated (Erroneous) | REPLACED BY → 1402372003 Poliosis eccentrica |
| `201175002` | Poliosis - acquired | inactivated (Erroneous) | REPLACED BY → 1402371005 Acquired poliosis |
| `202848009` | Scapulohumeral fibrositis | inactivated (Outdated) | - |
| `203104007` | Fibrositis of neck | inactivated (Outdated) | - |
| `20753005` | Hypertensive heart disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373738005 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart disease |
| `20759009` | Dietetic jejunitis | inactivated (Duplicate) | SAME AS → 1401593002 Allergic jejunitis caused by food |
| `20845005` | Meconium in amniotic fluid affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor, PARTIALLY EQUIVALENT TO → 2132004 Meconium in amniotic fluid noted before labor in liveborn infant |
| `213202009` | Complications of attempted introduction of fertilized ovum following in vitro fertilization | inactivated (Classification derived) | REPLACED BY → 1379976004 Disorder due to embryo transfer following in vitro fertilization |
| `21346009` | Double uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381658001 Maternal congenital duplication of uterus during antenatal and/or intrapartum period |
| `22173004` | Excessive fetal growth affecting management of mother | inactivated (Classification derived) | REPLACED BY → 199616008 Large for gestation age fetus |
| `22281000119101` | Post-term pregnancy of 40 to 42 weeks | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 63503002 Gestation period, 41 weeks, POSSIBLY EQUIVALENT TO → 46230007 Gestation period, 40 weeks, POSSIBLY EQUIVALENT TO → 90968009 Post-term pregnancy |
| `22288000` | Neoplasm of cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381666005 Neoplasm of cervix uteri during antenatal and/or intrapartum period |
| `223003` | Neoplasm of body of uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381678009 Neoplasm of body of uterus during antenatal and/or intrapartum period |
| `22753004` | Fetal AND/OR placental disorder affecting management of mother | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1193535003 Fetal disorder due to placental disorder, PARTIALLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `22966008` | Hypertensive heart AND renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373627000 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive heart and renal disease |
| `23001005` | Stenosis AND/OR stricture of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381651007 Maternal stenosis of cervix during antenatal and/or intrapartum period |
| `230441003` | Drug-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1382151008 Acute symptomatic epileptic seizure due to poisoning |
| `23171006` | Delayed AND/OR secondary postpartum hemorrhage | inactivated (Classification derived) | REPLACED BY → 156241003 Secondary postpartum hemorrhage |
| `23717007` | Benign essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373728000 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to benign essential hypertension |
| `237171000` | Stenosis of vagina in pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1396771007 Stenosis of vagina during antenatal and/or intrapartum period |
| `237256006` | Disorder of pelvic size and disproportion | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199416003 Mixed feto-pelvic disproportion, POSSIBLY EQUIVALENT TO → 275426009 Pelvic disproportion, POSSIBLY EQUIVALENT TO → 25749005 Fetopelvic disproportion, POSSIBLY EQUIVALENT TO → 199397009 Cephalopelvic disproportion |
| `237330001` | Obstetric injury of urinary bladder | inactivated (Duplicate) | SAME AS → 54679003 Traumatic injury of urinary bladder during obstetric procedure |
| `237342006` | Fat embolism - obstetric | inactivated (Duplicate) | SAME AS → 2261009 Obstetrical pulmonary fat embolism |
| `238419741000119109` | Alpha thalassemia trait in mother complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373734007 Maternal disorder due to alpha thalassemia trait during antenatal and/or intrapartum period |
| `23894009` | Acne varioliformis | inactivated (Duplicate) | SAME AS → 201228005 Necrotizing lymphocytic folliculitis |
| `239884000` | Malemud disease | inactivated (Nonconformance to editorial policy) | - |
| `240044003` | Fibrositis and nodular fasciitis | inactivated (Outdated) | - |
| `248663000` | Upper sternal shock | inactivated (Classification derived) | REPLACED BY → 248690009 Added heart sounds |
| `249079005` | Fontanelles presenting | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249083005 Posterior fontanelle presenting, POSSIBLY EQUIVALENT TO → 249082000 Anterior fontanelle presenting |
| `25053000` | Obstetrical central nervous system complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379974001 Maternal central nervous system disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26078007` | Hypertension secondary to renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `26224003` | Failed attempted termination of pregnancy complicated by genital-pelvic infection | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1373272003 Failed attempted abortion with pelvic infection, PARTIALLY EQUIVALENT TO → 1373273008 Failed attempted abortion with genital tract infection |
| `26623000` | Failed attempted termination of pregnancy complicated by delayed and/or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397362006 Excessive hemorrhage due to and following failed attempted abortion, POSSIBLY EQUIVALENT TO → 1397361004 Delayed hemorrhage due to and following failed attempted abortion |
| `267207004` | Congenital cardiovascular disorders during pregnancy, childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `267257007` | Labor and delivery complicated by fetal heart rate anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389144000 Abnormal fetal heart rate during intrapartum period |
| `267276009` | Obstetric anesthesia with pulmonary complications | inactivated (Classification derived) | REPLACED BY → 1379971009 Maternal pulmonary disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `267280004` | Venous complication of pregnancy and/or puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379964004 Maternal venous disorder due to pregnancy during antenatal and/or intrapartum and/or postpartum period |
| `267322007` | Pregnancy with orthopedic problem | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1380410008 Maternal disorder of musculoskeletal system during antenatal and/or intrapartum and/or postpartum period, PARTIALLY EQUIVALENT TO → 9111000119104 Musculoskeletal problem in pregnancy |
| `267350007` | Obstetric anesthesia problems | inactivated (Classification derived) | REPLACED BY → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `26828006` | Rectocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381657006 Maternal rectocele during antenatal and/or intrapartum period |
| `269480005` | Benign islet cell neoplasm | inactivated (Duplicate) | SAME AS → 254614001 Benign neoplasm of endocrine pancreas |
| `270498000` | Fetal malposition and malpresentation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 289365005 Finding of malposition of fetus, POSSIBLY EQUIVALENT TO → 80002007 Malpresentation of fetus |
| `27075004` | Venereal disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375996003 Maternal sexually transmitted infectious disease during antenatal and/or intrapartum and/or postpartum period |
| `273982004` | Obstetric problem affecting fetus | inactivated (Classification derived) | REPLACED BY → 609429008 Fetal disorder due to disease in mother |
| `273983009` | Maternal cord or placental problem | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 429260008 Disorder of umbilical cord, POSSIBLY EQUIVALENT TO → 125586008 Disorder of placenta |
| `274776000` | Finding of alcohol in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402002006 Finding of alcohol in blood, POSSIBLY EQUIVALENT TO → 1402003001 Finding of substance with alcohol structure in blood specimen |
| `276263005` | Porphobilinogen deaminase deficiency | inactivated (Duplicate) | SAME AS → 234422006 Acute intermittent porphyria |
| `276580005` | Atypical isoimmunization of newborn | inactivated (Outdated) | - |
| `284670008` | Nutritionally compromised | inactivated (Duplicate) | SAME AS → 445261000124106 Impaired nutritional status |
| `28664002` | Herpes iris | inactivated (Outdated) | REPLACED BY → 1407145007 Erythema multiforme with vesiculobullous target-shaped lesion |
| `288261009` | Was malpresentation pre-labor | inactivated (Erroneous) | REPLACED BY → 80002007 Malpresentation of fetus |
| `29259002` | Malignant hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373611007 Disorder during maternal antenatal and/or intrapartum period due to malignant hypertension |
| `29421008` | Failed attempted termination of pregnancy complicated by renal failure | inactivated (Duplicate) | SAME AS → 198809000 Failed attempted termination of pregnancy with renal failure |
| `29847008` | Obstetrical complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `30173002` | Primary fibrositis | inactivated (Outdated) | REPLACED BY → 95417003 Primary fibromyalgia syndrome |
| `3033000` | Bone AND/OR joint disorder of pelvis in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380435002 Maternal disorder of pelvic ring during antenatal and/or intrapartum and/or postpartum period |
| `30719001` | Dietetic enteritis of intestine | inactivated (Duplicate) | SAME AS → 1401590004 Allergic enteritis of intestine caused by food |
| `307333004` | Rhesus isoimmunization due to anti-D | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381908006 Hemolytic disease of fetus and/or neonate due to Rhesus anti-D isoimmunization, POSSIBLY EQUIVALENT TO → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `307334005` | Rhesus isoimmunization due to anti-c | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381903002 Hemolytic disease of fetus and/or neonate due to Rhesus anti-c isoimmunization, POSSIBLY EQUIVALENT TO → 1381901000 Maternal Rhesus isoimmunization due to anti-c during antenatal and/or intrapartum period |
| `307335006` | Rhesus isoimmunization due to anti-E | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381907001 Maternal Rhesus isoimmunization due to anti-E during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 1381909003 Hemolytic disease of fetus and/or neonate due to Rhesus anti-E isoimmunization |
| `307336007` | Rhesus isoimmunization due to anti-Cw | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381906005 Hemolytic disease of fetus and/or neonate due to Rhesus anti-Cw isoimmunization, POSSIBLY EQUIVALENT TO → 1381905009 Maternal Rhesus isoimmunization due to anti-Cw during antenatal and/or intrapartum period |
| `307735008` | Complete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397334004 Excessive hemorrhage due to and following complete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397335003 Delayed hemorrhage due to and following complete inevitable miscarriage |
| `307752007` | Incomplete inevitable miscarriage complicated by delayed or excessive hemorrhage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397343008 Excessive hemorrhage due to and following incomplete inevitable miscarriage, POSSIBLY EQUIVALENT TO → 1397344002 Delayed hemorrhage due to and following incomplete inevitable miscarriage |
| `31026002` | Obstetrical complication of sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380049002 Maternal disorder due to administration of sedative during antenatal and/or intrapartum and/or postpartum period |
| `31383003` | Neoplasm of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381650008 Neoplasm of vagina during pregnancy |
| `31407004` | Pre-existing hypertension complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373620003 Disorder during maternal postpartum period due to pre-existing hypertension |
| `31516002` | Viral disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375992001 Maternal viral disorder during antenatal and/or intrapartum and/or postpartum period |
| `31801000146106` | Pre-existing maternal disease complicating pregnancy | inactivated (Classification derived) | REPLACED BY → 1373736009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing disease |
| `31821006` | Uterine scar from previous surgery affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381695001 Maternal disorder due to uterine scar from previous surgery during antenatal and/or intrapartum period |
| `322112361000132104` | Scar epilepsy | inactivated (Outdated) | REPLACED BY → 1372772007 Epilepsy due to intracranial structural abnormality |
| `32999002` | Complication of obstetrical surgical wound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380090004 Disorder of surgical wound following obstetric surgical procedure during antenatal and/or intrapartum and/or postpartum period |
| `33687004` | Dietetic gastroenteritis | inactivated (Duplicate) | SAME AS → 1401597001 Allergic gastroenteritis caused by food |
| `34273003` | Hypertensive heart disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373628005 Disorder during maternal postpartum period due to hypertensive heart and renal disease |
| `34694006` | Pre-existing hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `35217003` | Gross' disease | inactivated (Outdated) | REPLACED BY → 716685003 Solitary rectal ulcer syndrome |
| `35716006` | Cracked nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258917005 Postpartum cracked nipple |
| `35746009` | Uterine fibroids affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381668006 Uterine leiomyoma during antenatal and/or intrapartum period |
| `361268000` | Alcohol-induced epilepsy | inactivated (Erroneous) | REPLACED BY → 1365922007 Acute symptomatic epileptic seizure due to ethyl alcohol poisoning |
| `36175004` | Furuncle of heel | inactivated (Erroneous) | REPLACED BY → 91541006 Abscess of heel |
| `36199004` | Pendulous breast | inactivated (Duplicate) | SAME AS → 248804005 Ptotic breast |
| `36297009` | Septate vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381660004 Maternal septate vagina during antenatal and/or intrapartum period |
| `362972006` | Disorder of labor / delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1382290001 Disorder of mother and/or fetus during intrapartum period, POSSIBLY EQUIVALENT TO → 1269434002 Fetal disorder during intrapartum period, POSSIBLY EQUIVALENT TO → 1269075002 Maternal disorder during intrapartum period |
| `36428009` | Gestation period, 42 weeks | inactivated (Nonconformance to editorial policy) | REPLACED BY → 90968009 Post-term pregnancy |
| `367390009` | Hypertension in the obstetric context | inactivated (Classification derived) | REPLACED BY → 288250001 Maternal hypertension |
| `36916008` | Bone AND/OR joint disorder of back in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380434003 Maternal disorder of vertebral column during antenatal and/or intrapartum and/or postpartum period |
| `370056005` | Tumor invasion into bronchus, in situ | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370057001` | Tumor invasion into bronchus, invasive | inactivated (Erroneous) | REPLACED BY → 370055009 Tumor invasion into bronchus |
| `370480003` | Hepatoportal microvascular dysplasia | inactivated (Nonconformance to editorial policy) | - |
| `372043009` | Hydrops of allantois | inactivated (Nonconformance to editorial policy) | - |
| `37618003` | Chronic hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `387817006` | Deficiency of phosphorylase b kinase | inactivated (Duplicate) | SAME AS → 124329006 Deficiency of phosphorylase kinase |
| `387833009` | Premature canities | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 297994000 Gray hair, POSSIBLY EQUIVALENT TO → 1402360009 Premature canities |
| `3885002` | ABO isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381701007 Maternal ABO isoimmunization during antenatal and/or intrapartum period |
| `39101000119109` | Pregnancy with isoimmunization from irregular blood group incompatibility | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381698004 Maternal irregular blood group isoimmunization during antenatal and/or intrapartum period |
| `39727004` | Hypertension secondary to renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373624007 Disorder during maternal postpartum period due to renal hypertension |
| `39763004` | Abnormal glucose tolerance in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 372046001 Glucose tolerance test during pregnancy, childbirth and puerperium outside reference range |
| `397949005` | Poor fetal growth affecting management | inactivated (Classification derived) | REPLACED BY → 22033007 Fetal growth restriction |
| `398276003` | Placental insufficiency affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237292005 Placental insufficiency |
| `399363000` | Late fetal death affecting management of mother | inactivated (Classification derived) | REPLACED BY → 237364002 Stillbirth |
| `4006006` | Fetal tachycardia affecting management of mother | inactivated (Classification derived) | REPLACED BY → 240298005 Fetal tachycardia |
| `4026005` | Interstitial mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388393008 Interstitial mastitis during postpartum |
| `404169008` | Malignant histiocytosis involving skin | inactivated (Classification derived) | REPLACED BY → 1402004007 Malignant histiocytic macrophage neoplasm of skin |
| `40609001` | Infectious disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1376002004 Maternal infection during antenatal and/or intrapartum and/or postpartum period |
| `408512008` | Body mass index 40+ - severely obese | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407010002 Adult body mass index greater than or equal to 40 kg/m2, ALTERNATIVE → 83911000119104 Severe obesity |
| `41215002` | Congenital abnormality of uterus, affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381683001 Maternal disorder due to congenital abnormality of uterus during antenatal and/or intrapartum period |
| `412768003` | Body mass index 20-24 - normal | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 43664005 Normal weight, ALTERNATIVE → 1407013000 Adult body mass index 18.5-24.9 kg/m2 |
| `413567003` | Aplastic anemia associated with pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379966002 Maternal aplastic anemia during antenatal and/or intrapartum period |
| `415110002` | Plasma cell myeloma/plasmacytoma | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 415112005 Plasmacytoma, POSSIBLY EQUIVALENT TO → 109989006 Multiple myeloma |
| `41527003` | Glycogen storage disease type VIII | inactivated (Outdated) | REPLACED BY → 235908005 Glycogen phosphorylase kinase deficiency |
| `416389007` | Gastrointestinal disorder due to food allergy | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401588000 Allergic disorder of gastrointestinal tract caused by food |
| `417349008` | Closed fracture dislocation of proximal interphalangeal joint of digit of hand | inactivated (Erroneous) | REPLACED BY → 1401963004 Closed fracture dislocation of proximal interphalangeal joint of finger |
| `42537006` | Secondary perineal tear in the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 6234006 Second degree perineal laceration |
| `42686001` | Fetal chromosomal abnormality affecting obstetrical care | inactivated (Classification derived) | REPLACED BY → 267253006 Fetal chromosomal abnormality |
| `427090001` | Body mass index less than 16.5 | inactivated (Outdated) | REPLACED BY → 1407014006 Adult body mass index less than 18.5 kg/m2 |
| `427921009` | Chronic ulcer of ankle | inactivated (Duplicate) | SAME AS → 10637751000119102 Chronic ulcer of skin of ankle |
| `428530009` | Heterozygous sitosterolemia | inactivated (Erroneous) | REPLACED BY → 1409234007 Compound heterozygous sitosterolemia |
| `43329005` | Infestation by Knemidokoptes pilae | inactivated (Nonconformance to editorial policy) | - |
| `43651009` | Acquired stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381681004 Maternal disorder due to acquired stenosis of vagina during antenatal and/or intrapartum period |
| `43970002` | Congenital stenosis of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381682006 Maternal disorder due to congenital stenosis of vagina during antenatal and/or intrapartum period |
| `442766007` | High alcohol level in blood | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441685000 High alcohol level in blood |
| `443006` | Cystocele affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381656002 Maternal cystocele during antenatal and/or intrapartum period |
| `444768009` | Chronic ulcer of sacral region | inactivated (Duplicate) | SAME AS → 10642351000119100 Chronic skin ulcer of sacrum |
| `44795003` | Rhesus isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381697009 Maternal Rhesus isoimmunization during antenatal and/or intrapartum period |
| `45079001` | Acromion left anterior position | inactivated (Duplicate) | SAME AS → 249108000 Shoulder left anterior position |
| `45759004` | Rigid perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381659009 Rigid perineum during antenatal and/or intrapartum period |
| `45828008` | Anemia in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 156140005 Maternal anemia during antenatal and/or intrapartum and/or postpartum period |
| `46273003` | Abscess of nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388401001 Abscess of nipple during postpartum |
| `473429002` | Tuberculoma of spinal cord confirmed | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1411612005 Tuberculoma of spinal cord confirmed |
| `47507006` | Rieger anomaly | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 417604002 Axenfeld-Rieger syndrome, POSSIBLY EQUIVALENT TO → 1416355004 Rieger anomaly |
| `4783006` | Maternal diabetes mellitus with hypoglycemia affecting fetus OR newborn | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1388261002 Disorder of fetus due to hypoglycemia of mother with diabetes mellitus, PARTIALLY EQUIVALENT TO → 1388262009 Disorder of neonate due to hypoglycemia of mother with diabetes mellitus |
| `48012003` | Boil of tunica vaginalis | inactivated (Erroneous) | REPLACED BY → 33724004 Abscess of tunica vaginalis |
| `48200009` | Bone AND/OR joint disorder of lower extremities in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1380436001 Maternal musculoskeletal disorder of lower limb during antenatal and/or intrapartum and/or postpartum period |
| `48485000` | Miscarriage in third trimester | inactivated (Erroneous) | REPLACED BY → 10761191000119104 Preterm labor in third trimester with preterm delivery in third trimester |
| `48552006` | Hypertension secondary to renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension |
| `48739004` | Miscarriage with cardiac arrest and/or cardiac failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10760181000119109 Cardiac arrest due to miscarriage, PARTIALLY EQUIVALENT TO → 1397851002 Cardiac failure due to and following miscarriage |
| `49102001` | Hypertensive heart AND renal disease in obstetric context | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373667004 Pre-existing hypertensive heart and renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `49171007` | Hypertensive renal disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373596009 Disorder during maternal intrapartum period due to renal hypertension |
| `49342001` | Stricture of vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381676008 Stricture of vagina during antenatal and/or intrapartum period |
| `49364005` | Subareolar abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388403003 Subareolar abscess during postpartum |
| `49464009` | Dietetic sigmoiditis | inactivated (Duplicate) | SAME AS → 1401595009 Allergic sigmoiditis caused by food |
| `50120008` | Abnormal acid-base balance affecting management of mother | inactivated (Classification derived) | REPLACED BY → 1382350001 Maternal disorder of acid-base balance during antenatal and/or intrapartum and/or postpartum period |
| `50305006` | Acquired poliosis circumscripta | inactivated (Erroneous) | REPLACED BY → 1402366003 Acquired poliosis circumscripta |
| `50557007` | Healed pelvic floor repair affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381680003 Maternal disorder due to previous pelvic floor repair during antenatal and/or intrapartum period |
| `51154004` | Obstetrical pulmonary complication of anesthesia AND/OR sedation | inactivated (Classification derived) | REPLACED BY → 1386327009 Maternal disorder of lung due to administration of anesthesia and/or sedation during intrapartum period |
| `51495008` | Cerebral anoxia following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1396086006 Maternal cerebral anoxia due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1396087002 Maternal cerebral anoxia due to and following sedation during intrapartum period |
| `541000119105` | Hypertension complicating pregnancy, childbirth and the puerperium, antepartum | inactivated (Classification derived) | REPLACED BY → 1373731004 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to hypertension |
| `55028001` | Boil of vas deferens | inactivated (Erroneous) | REPLACED BY → 39235000 Abscess of vas deferens |
| `5534004` | Senile arteritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 129573006 Atherosclerotic occlusive disease, POSSIBLY EQUIVALENT TO → 698816006 Chronic occlusion of artery of extremity |
| `55472006` | Submammary abscess associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388402008 Submammary abscess during postpartum |
| `55581002` | Meconium in amniotic fluid first noted during labor AND/OR delivery in liveborn infant | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1389111006 Meconium stained amniotic fluid during intrapartum period, PARTIALLY EQUIVALENT TO → 206269002 Liveborn with labor meconium in liquor |
| `55613002` | Engorgement of breasts associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388405005 Engorgement of breast during postpartum, POSSIBLY EQUIVALENT TO → 34831003 Neonatal engorgement of breast |
| `55704005` | Abscess of breast, associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258867002 Postpartum abscess of breast |
| `56313000` | Abnormal placenta affecting management of mother | inactivated (Classification derived) | REPLACED BY → 33552005 Anomaly of placenta |
| `56557000` | Fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `57220000` | Obstetrical complication of local anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380039000 Maternal disorder due to administration of local anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `57873008` | Hypertensive renal disease complicating AND/OR reason for care during puerperium | inactivated (Classification derived) | REPLACED BY → 1373623001 Disorder during maternal postpartum period due to hypertensive renal disease |
| `5852008` | Acromion right anterior position | inactivated (Duplicate) | SAME AS → 249107005 Shoulder right anterior position |
| `58881007` | Polyp of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381662007 Polyp of cervix during antenatal and/or intrapartum period |
| `58990004` | Miscarriage complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397368005 Traumatic injury of organ of pelvis due to and following miscarriage, POSSIBLY EQUIVALENT TO → 1397367000 Traumatic injury of soft tissue of pelvis due to and following miscarriage |
| `59136001` | Thyroid disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375993006 Maternal thyroid disorder during antenatal and/or intrapartum and/or postpartum period |
| `5939002` | Failed attempted termination of pregnancy complicated by metabolic disorder | inactivated (Duplicate) | SAME AS → 198810005 Failed attempted termination of pregnancy with metabolic disorder |
| `59733002` | Hypertensive heart disease complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373818003 Disorder during maternal intrapartum period due to pre-existing hypertensive heart disease |
| `59919008` | Failed attempted termination of pregnancy with complication | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 49416000 Failed attempted termination of pregnancy |
| `6051000119109` | Chronic ulcer of calf | inactivated (Duplicate) | SAME AS → 10640791000119105 Chronic ulcer of skin of calf |
| `609447002` | Induced termination of pregnancy complicated by damage to pelvic organs and/or tissues | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1389152002 Traumatic injury of pelvic organ during termination of pregnancy |
| `609449004` | Induced termination of pregnancy complicated by embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373901003 Embolism due to and following termination of pregnancy |
| `609450004` | Induced termination of pregnancy complicated by genital-pelvic infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379953002 Pelvic inflammatory disease due to and following termination of pregnancy |
| `609451000` | Induced termination of pregnancy complicated by metabolic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373900002 Metabolic disorder due to and following termination of pregnancy |
| `609452007` | Induced termination of pregnancy complicated by renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373872005 Renal failure due to and following termination of pregnancy |
| `609453002` | Induced termination of pregnancy complicated by shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609454008` | Induced termination of pregnancy complicated by acute necrosis of liver | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379940000 Acute necrosis of liver due to induced termination of pregnancy |
| `609455009` | Induced termination of pregnancy complicated by acute renal failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376024004 Acute renal failure due to and following termination of pregnancy |
| `609456005` | Induced termination of pregnancy complicated by afibrinogenemia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376015008 Afibrinogenemia due to induced termination of pregnancy |
| `609457001` | Induced termination of pregnancy complicated by air embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373908009 Air embolism due to and following termination of pregnancy |
| `609458006` | Induced termination of pregnancy complicated by amniotic fluid embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379939002 Amniotic fluid embolism due to and following termination of pregnancy |
| `609459003` | Induced termination of pregnancy complicated by blood-clot embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376026002 Thromboembolism due to and following termination of pregnancy |
| `609461007` | Induced termination of pregnancy complicated by cerebral anoxia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376016009 Cerebral anoxia due to induced termination of pregnancy |
| `609462000` | Induced termination of pregnancy complicated by defibrination syndrome | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379937000 Disseminated intravascular coagulation due to induced termination of pregnancy |
| `609463005` | Induced termination of pregnancy complicated by electrolyte imbalance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379932006 Electrolyte imbalance due to induced termination of pregnancy |
| `609464004` | Induced termination of pregnancy complicated by endometritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373904006 Endometritis due to induced termination of pregnancy |
| `609465003` | Induced termination of pregnancy complicated by fat embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373907004 Fat embolism due to and following termination of pregnancy |
| `609466002` | Induced termination of pregnancy complicated by intravascular hemolysis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379954008 Intravascular hemolysis due to induced termination of pregnancy |
| `609467006` | Induced termination of pregnancy complicated by laceration of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376027006 Laceration of intestine during termination of pregnancy |
| `609468001` | Induced termination of pregnancy complicated by laceration of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379942008 Laceration of broad ligament during termination of pregnancy |
| `609469009` | Induced termination of pregnancy complicated by laceration of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376029009 Laceration of cervix during termination of pregnancy |
| `609470005` | Induced termination of pregnancy complicated by laceration of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376031000 Laceration of uterus during termination of pregnancy |
| `609471009` | Induced termination of pregnancy complicated by laceration of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376030004 Laceration of vagina during termination of pregnancy |
| `609472002` | Induced termination of pregnancy complicated by acute renal failure with oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379956005 Acute renal failure with oliguria due to induced termination of pregnancy |
| `609473007` | Induced termination of pregnancy complicated by parametritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373906008 Parametritis due to induced termination of pregnancy |
| `609474001` | Induced termination of pregnancy complicated by pelvic peritonitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376020008 Pelvic peritonitis due to induced termination of pregnancy |
| `609475000` | Induced termination of pregnancy complicated by perforation of bowel | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376028001 Traumatic perforation of intestine during termination of pregnancy |
| `609476004` | Induced termination of pregnancy complicated by perforation of cervix | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379931004 Traumatic perforation of uterine cervix during termination of pregnancy |
| `609477008` | Induced termination of pregnancy complicated by perforation of uterus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379935008 Traumatic perforation of uterus during termination of pregnancy |
| `609478003` | Induced termination of pregnancy complicated by perforation of vagina | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379930003 Traumatic perforation of vagina during termination of pregnancy |
| `609479006` | Induced termination of pregnancy complicated by postoperative shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373919007 Postoperative shock due to and following termination of pregnancy |
| `609480009` | Induced termination of pregnancy complicated by pulmonary embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376021007 Pulmonary embolism due to and following termination of pregnancy |
| `609482001` | Induced termination of pregnancy complicated by renal tubular necrosis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379938005 Acute renal tubular necrosis due to induced termination of pregnancy |
| `609483006` | Induced termination of pregnancy complicated by salpingitis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373903000 Salpingitis due to induced termination of pregnancy |
| `609484000` | Induced termination of pregnancy complicated by salpingo-oophoritis | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376025003 Salpingo-oophoritis due to induced termination of pregnancy |
| `609486003` | Induced termination of pregnancy complicated by septic embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373918004 Septic embolism due to and following termination of pregnancy |
| `609487007` | Induced termination of pregnancy complicated by septic shock | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373909001 Septic shock due to and following termination of pregnancy |
| `609489005` | Induced termination of pregnancy complicated by soap embolism | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373912003 Soap embolism due to and following termination of pregnancy |
| `609490001` | Induced termination of pregnancy complicated by uremia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373898004 Uremia due to induced termination of pregnancy |
| `609491002` | Induced termination of pregnancy complicated by urinary tract infection | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379952007 Urinary tract infection due to and following induced termination of pregnancy |
| `609493004` | Induced termination of pregnancy complicated by tetanus | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373899007 Tetanus due to and following induced termination of pregnancy |
| `609494005` | Induced termination of pregnancy complicated by pelvic disorder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373875007 Disorder of pelvis due to induced termination of pregnancy |
| `609496007` | Complication occurring during pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 70591005 Fetal disorder, POSSIBLY EQUIVALENT TO → 173300003 Disorder of pregnancy |
| `609498008` | Induced termination of pregnancy complicated by laceration of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379929008 Laceration of urinary bladder during termination of pregnancy |
| `609499000` | Induced termination of pregnancy complicated by laceration of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379943003 Laceration of periurethral tissue during termination of pregnancy |
| `609500009` | Induced termination of pregnancy complicated by perforation of urinary bladder | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379936009 Traumatic perforation of urinary bladder during termination of pregnancy |
| `609501008` | Induced termination of pregnancy complicated by perforation of broad ligament | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379941001 Traumatic perforation of broad ligament during termination of pregnancy |
| `609502001` | Induced termination of pregnancy complicated by perforation of periurethral tissue | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379944009 Traumatic perforation of periurethral tissue during termination of pregnancy |
| `609503006` | Induced termination of pregnancy complicated by urinary bladder damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373915001 Traumatic injury of urinary bladder during termination of pregnancy |
| `609504000` | Induced termination of pregnancy complicated by bowel damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373905007 Traumatic injury of intestine during termination of pregnancy |
| `609505004` | Induced termination of pregnancy complicated by broad ligament damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379933001 Traumatic injury of broad ligament during termination of pregnancy |
| `609506003` | Induced termination of pregnancy complicated by cardiac arrest | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373916000 Cardiac arrest due to induced termination of pregnancy |
| `609507007` | Induced termination of pregnancy complicated by cardiac failure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376017000 Cardiac failure due to induced termination of pregnancy |
| `609508002` | Induced termination of pregnancy complicated by cervix damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373911005 Traumatic injury of uterine cervix during termination of pregnancy |
| `609510000` | Induced termination of pregnancy complicated by infectious disease | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1376022000 Infectious disease due to and following induced termination of pregnancy |
| `609511001` | Induced termination of pregnancy complicated by periurethral tissue damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1379955009 Periurethral traumatic injury during termination of pregnancy |
| `609512008` | Induced termination of pregnancy complicated by oliguria | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373902005 Oliguria due to induced termination of pregnancy |
| `609513003` | Induced termination of pregnancy complicated by uterus damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373914002 Traumatic injury of uterus during termination of pregnancy |
| `609514009` | Induced termination of pregnancy complicated by vaginal damage | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373917009 Traumatic injury of vagina during termination of pregnancy |
| `61714007` | Metabolic disturbance in labor AND/OR delivery | inactivated (Classification derived) | REPLACED BY → 1395830004 Maternal metabolic disease during intrapartum period |
| `61947007` | Deaf mutism | inactivated (Outdated) | - |
| `62612003` | Fibrosis of perineum affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381677004 Fibrosis of perineum during antenatal and/or intrapartum period |
| `62657007` | Cardiac arrest AND/OR failure following anesthesia AND/OR sedation in labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386325001 Maternal cardiac arrest due to administration of anesthesia and/or sedation during intrapartum period, POSSIBLY EQUIVALENT TO → 1386326000 Maternal cardiac failure due to administration of anesthesia and/or sedation during intrapartum period |
| `63287004` | Benign essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373658004 Benign pre-existing essential hypertension during antenatal and/or intrapartum and/or postpartum period |
| `64171002` | Obstetrical cardiac complication of anesthesia AND/OR sedation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1386323008 Maternal disorder of heart due to administration of anesthesia and/or sedation during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379970005 Maternal cardiac disorder due to anesthesia during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 1379973007 Maternal cardiac disorder due to and following anesthesia during intrapartum period, POSSIBLY EQUIVALENT TO → 1386324002 Maternal disorder of heart due to administration of anesthesia and/or sedation during intrapartum period |
| `65402008` | Pre-existing hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373619009 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertension |
| `65409004` | Obstetrical complication of anesthesia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380038008 Maternal disorder due to administration of anesthesia during antenatal and/or intrapartum and/or postpartum period |
| `6636004` | Congenital cardiovascular disorder in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1379961007 Maternal congenital cardiovascular disorder during antenatal and/or intrapartum and/or postpartum period |
| `66709007` | Hypertensive renal disease complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373622006 Disorder during maternal antenatal and/or intrapartum period due to pre-existing hypertensive renal disease |
| `66958002` | Isoimmunization from non-ABO, non-Rh blood-group incompatibility affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381707006 Maternal non-ABO, non-Rhesus blood-group isoimmunization during antenatal and/or intrapartum period |
| `68214002` | Lymphangitis of breast associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388394002 Lymphangitis of breast during postpartum |
| `69302000` | Termination of pregnancy on demand | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 57797005 Termination of pregnancy |
| `698614006` | Acquired deaf mutism | inactivated (Outdated) | - |
| `698615007` | Congenital deaf mutism | inactivated (Outdated) | - |
| `698764006` | Post infectious grand mal epilepsy | inactivated (Outdated) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `698767004` | Post-cerebrovascular accident epilepsy | inactivated (Duplicate) | SAME AS → 1380178003 Epilepsy due to and following stroke |
| `699950009` | Anti-D isoimmunization affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381696000 Maternal anti-D isoimmunization during antenatal and/or intrapartum period |
| `700237005` | Supra-eruption of tooth | inactivated (Duplicate) | SAME AS → 109644008 Overeruption of tooth |
| `71639005` | Galactorrhea associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388264005 Maternal galactorrhea during postpartum period |
| `71874008` | Benign essential hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373569006 Maternal disorder during labor due to benign essential hypertension |
| `72022006` | Essential hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373656000 Pre-existing essential hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `721166000` | Human immunodeficiency virus complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1380419009 Maternal human immunodeficiency virus infection during antenatal and/or intrapartum and/or postpartum period |
| `721177006` | Injury complicating pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402307005 Maternal injury during antenatal and/or intrapartum period, POSSIBLY EQUIVALENT TO → 426997005 Maternal traumatic injury during antenatal and/or intrapartum period |
| `721201001` | Protozoal disease complicating pregnancy childbirth and the puerperium | inactivated (Classification derived) | REPLACED BY → 1376000007 Maternal disorder caused by Protozoa during antenatal and/or intrapartum and/or postpartum period |
| `721203003` | Sequela of complication of pregnancy childbirth and the puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1380411007 Disorder due to and following maternal disorder during antenatal and/or intrapartum and/or postpartum period |
| `722595002` | Overweight in adulthood with body mass index of 25 or more but less than 30 | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 1407012005 Overweight in adulthood, ALTERNATIVE → 1407011003 Adult body mass index 25-29.9 kg/m2 |
| `72280009` | Achromotrichia | inactivated (Erroneous) | REPLACED BY → 1402356006 Achromotrichia |
| `723091005` | Fistula of vagina and/or rectum and/or urinary bladder due to complication occurring during labor and/or delivery | inactivated (Classification derived) | REPLACED BY → 1395886004 Genital tract fistula following vaginal delivery |
| `724497009` | Disease of circulatory system complicating pregnancy childbirth and puerperium | inactivated (Classification derived) | REPLACED BY → 1380409003 Maternal circulatory disorder during antenatal and/or intrapartum and/or postpartum period |
| `724549005` | Epilepsy due to infectious disease of central nervous system | inactivated (Erroneous) | REPLACED BY → 1373924005 Epilepsy due to infectious disease |
| `724787004` | Epilepsy due to cerebrovascular accident | inactivated (Erroneous) | REPLACED BY → 1380178003 Epilepsy due to and following stroke |
| `724988000` | Epilepsy co-occurrent and due to degenerative brain disorder | inactivated (Duplicate) | SAME AS → 1340125003 Epilepsy syndrome with progressive neurological deterioration |
| `724989008` | Epilepsy co-occurrent and due to mesial temporal sclerosis | inactivated (Duplicate) | SAME AS → 770643005 Mesial temporal lobe epilepsy with hippocampal sclerosis |
| `724991000` | Epilepsy co-occurrent and due to demyelinating disorder | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1372950000 Epilepsy due to demyelinating disease of brain |
| `724992007` | Epilepsy co-occurrent and due to dementia | inactivated (Erroneous) | REPLACED BY → 1373650006 Epilepsy due to neurodegenerative dementia |
| `72547003` | Dietetic colitis | inactivated (Duplicate) | SAME AS → 1401589008 Allergic colitis caused by food |
| `72860003` | Disorder of amniotic cavity AND/OR membrane | inactivated (Classification derived) | REPLACED BY → 609522002 Disorder of extraembryonic membrane |
| `73030000` | Hypertensive renal disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373661003 Pre-existing hypertensive renal disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `735492001` | Obstructed labor due to shoulder dystocia | inactivated (Duplicate) | SAME AS → 89700002 Shoulder girdle dystocia |
| `737194006` | Dietetic enteritis of small intestine | inactivated (Duplicate) | SAME AS → 1401591000 Allergic enteritis of small intestine caused by food |
| `737329004` | Damage to pelvic organs and tissues following ectopic pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397365008 Traumatic injury of soft tissue of pelvis due to and following ectopic pregnancy, POSSIBLY EQUIVALENT TO → 1397370001 Traumatic injury of organ of pelvis due to and following ectopic pregnancy |
| `737330009` | Damage to pelvic organs and tissues following molar pregnancy | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1397366009 Traumatic injury of soft tissue of pelvis due to and following molar pregnancy, POSSIBLY EQUIVALENT TO → 1397369002 Traumatic injury of organ of pelvis due to and following molar pregnancy |
| `73813001` | Elastosis senilis | inactivated (Outdated) | REPLACED BY → 43982006 Solar degeneration |
| `73837001` | Failed attempted termination of pregnancy with cardiac arrest and/or failure | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 10750641000119101 Cardiac arrest due to failed attempted abortion, PARTIALLY EQUIVALENT TO → 1373227006 Failed attempted abortion with cardiac failure |
| `74227009` | Apraxic aphonia | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 441913003 Aphonia, POSSIBLY EQUIVALENT TO → 1407180006 Acquired apraxia of speech |
| `74955002` | Retracted nipple associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388400000 Retraction of nipple during postpartum |
| `75150001` | Renal disease in pregnancy AND/OR puerperium without hypertension | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 733839001 Postpartum acute renal failure, PARTIALLY EQUIVALENT TO → 1373626009 Disorder during maternal antenatal and/or intrapartum period due to renal hypertension, PARTIALLY EQUIVALENT TO → 1373733001 Disorder during maternal antenatal and/or intrapartum and/or postpartum period due to renal hypertension |
| `76037007` | Rigid cervix uteri affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381674006 Rigid cervix uteri during antenatal and/or intrapartum period |
| `76118001` | Dietetic ileitis | inactivated (Duplicate) | SAME AS → 1401592007 Allergic ileitis caused by food |
| `76751001` | Diabetes mellitus in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 199223000 Maternal diabetes mellitus during antenatal and/or intrapartum and/or postpartum period, POSSIBLY EQUIVALENT TO → 609563008 Pre-existing diabetes mellitus in pregnancy |
| `76871004` | Previous surgery to vagina affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381679001 Maternal disorder due to previous vaginal surgery during antenatal and/or intrapartum period |
| `77285007` | Placental infarct affecting management of mother | inactivated (Classification derived) | REPLACED BY → 268585006 Placental infarct |
| `77563000` | Obstruction by bony pelvis | inactivated (Duplicate) | SAME AS → 199757009 Obstructed labor caused by bony pelvis |
| `778075008` | Pityriasis simplex capitis | inactivated (Duplicate) | SAME AS → 400201008 Pityriasis capitis |
| `78381004` | Heart disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375991008 Maternal heart disorder during antenatal and/or intrapartum and/or postpartum period |
| `78697003` | Nonpurulent mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388395001 Nonpurulent mastitis during postpartum |
| `78808002` | Essential hypertension complicating AND/OR reason for care during pregnancy | inactivated (Classification derived) | REPLACED BY → 1373618001 Disorder during maternal antenatal and/or intrapartum period due to essential hypertension |
| `78818007` | Decreased skin sensitivity | inactivated (Duplicate) | SAME AS → 398026008 Reduced sensation of skin |
| `79254009` | Flail elbow | inactivated (Duplicate) | SAME AS → 296641000119105 Flail joint of elbow |
| `79355007` | Hypertensive heart disease in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373662005 Pre-existing hypertensive heart disease during maternal antenatal and/or intrapartum and/or postpartum period |
| `79442007` | Deafmutism-retinal degeneration syndrome | inactivated (Outdated) | - |
| `79839005` | Perineal laceration involving vulva | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 237332009 Vulval tear, POSSIBLY EQUIVALENT TO → 1388876002 First degree laceration of perineum and laceration of vulva during vaginal delivery of fetus |
| `80818002` | Previous surgery to perineum AND/OR vulva affecting pregnancy | inactivated (Classification derived) | PARTIALLY EQUIVALENT TO → 1381693008 Maternal disorder due to previous procedure on perineum during antenatal and/or intrapartum period, PARTIALLY EQUIVALENT TO → 1381694002 Maternal disorder due to previous procedure on vulva during antenatal and/or intrapartum period |
| `81557008` | Parasitic disease in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 1375999005 Maternal disorder caused by parasite during antenatal and/or intrapartum and/or postpartum period |
| `81626002` | Malignant hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373657009 Malignant hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `8218002` | Chronic hypertension complicating AND/OR reason for care during childbirth | inactivated (Classification derived) | REPLACED BY → 1373621004 Disorder during maternal intrapartum period due to pre-existing hypertension |
| `82381000119103` | Epileptic dementia with behavioral disturbance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1373650006 Epilepsy due to neurodegenerative dementia, POSSIBLY EQUIVALENT TO → 1340125003 Epilepsy syndrome with progressive neurological deterioration, POSSIBLY EQUIVALENT TO → 1591000119103 Dementia with behavioral disturbance |
| `83134002` | Dietetic diarrhea | inactivated (Duplicate) | SAME AS → 1401598006 Allergic diarrhea caused by food |
| `83243004` | Rigid pelvic floor affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381673000 Rigid pelvic floor during antenatal and/or intrapartum period |
| `84007008` | Shock during AND/OR following labor AND/OR delivery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1381592008 Maternal shock due to and following delivery, POSSIBLY EQUIVALENT TO → 1381590000 Maternal shock during intrapartum period |
| `8445003` | Neoplasm of vulva affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381661000 Neoplasm of vulva during antenatal and/or intrapartum period |
| `84939004` | Rubella in mother complicating pregnancy, childbirth AND/OR puerperium | inactivated (Classification derived) | REPLACED BY → 270497005 Maternal rubella during antenatal and/or intrapartum and/or postpartum period |
| `85542007` | Perineal laceration involving skin | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388874004 Laceration of skin of perineum, POSSIBLY EQUIVALENT TO → 1388873005 First degree laceration of skin of perineum during vaginal delivery of fetus |
| `85879003` | Secondary fibrositis | inactivated (Outdated) | REPLACED BY → 203082005 Fibromyalgia |
| `85920003` | Constipation by outlet obstruction | inactivated (Outdated) | REPLACED BY → 713411004 Obstructive defecation syndrome |
| `86041002` | Pre-existing hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `870766001` | Acneiform eruption due to bromine compound | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 8007005 Bromoderma, POSSIBLY EQUIVALENT TO → 1406864008 Bromoderma tuberosum |
| `87383005` | Maternal distress | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 249196008 Maternal distress due to pain during maternal intrapartum period, POSSIBLY EQUIVALENT TO → 200164009 Maternal exhaustion during intrapartum period, POSSIBLY EQUIVALENT TO → 1409197005 Maternal emotional distress during intrapartum period |
| `8762007` | Chronic hypertension in obstetric context | inactivated (Classification derived) | REPLACED BY → 1373659007 Pre-existing hypertension during maternal antenatal and/or intrapartum and/or postpartum period |
| `87840008` | Galactocele associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388398004 Galactocele during postpartum period |
| `88320008` | Drug tolerance | inactivated (Nonconformance to editorial policy) | REPLACED BY → 365992008 Drug tolerance - finding |
| `89672000` | Retromammary mastitis associated with childbirth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1388397009 Retromammary mastitis during postpartum |
| `90645002` | Failed attempted termination of pregnancy without complication | inactivated (Nonconformance to editorial policy) | REPLACED BY → 49416000 Failed attempted termination of pregnancy |
| `9297001` | Bicornuate uterus affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381667001 Bicornate uterus during antenatal and/or intrapartum period |
| `95344007` | Ulcer of lower extremity | inactivated (Duplicate) | SAME AS → 711168000 Ulcer of skin of lower extremity |
| `95606005` | Maternal drug exposure | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `95607001` | Maternal drug use | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1254981008 Substance dependence during pregnancy, childbirth and/or puerperium |
| `9720009` | Cicatrix of cervix affecting pregnancy | inactivated (Classification derived) | REPLACED BY → 1381675007 Cicatrix of cervix during antenatal and/or intrapartum period |

**New members (839):**

| Code | Display |
|---|---|
| `1000081000220104` | Impaired prone position tolerance in infancy |
| `1011481000220101` | Calcification of left ventricular outflow tract |
| `1011491000220103` | Rupture of aortic annulus |
| `1011661000220107` | In-hospital stroke |
| `1011671000220101` | In-hospital myocardial infarction |
| `103406000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A1 |
| `103407009` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A2 |
| `103408004` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category A3 |
| `103409007` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B1 |
| `103410002` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B2 |
| `103411003` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category B3 |
| `103412005` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C1 AIDS (acquired immunodeficiency syndrome) |
| `103413000` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C2 AIDS (acquired immunodeficiency syndrome) |
| `103414006` | HIV (human immunodeficiency virus) CDC (Centers for Disease Control and Prevention) category C3 AIDS (acquired immunodeficiency syndrome) |
| `10677431000119101` | Acantholytic disorder |
| `11305001000119101` | Secondary osteoporotic fracture of right tibia |
| `11305041000119104` | Secondary osteoporotic fracture of left tibia |
| `11305321000119108` | Secondary osteoporotic fracture of right fibula |
| `11305361000119103` | Secondary osteoporotic fracture of left fibula |
| `11313121000119107` | Secondary osteoporotic fracture of right ulna |
| `11313161000119102` | Secondary osteoporotic fracture of left ulna |
| `11851561000119100` | Nonvenomous insect bite of posterior chest wall |
| `12206071000119108` | Osteolysis of bone adjacent to right ankle joint prosthesis |
| `12206111000119101` | Osteolysis of bone adjacent to right elbow joint prosthesis |
| `12206151000119100` | Osteolysis of bone adjacent to right finger joint prosthesis |
| `12208881000119103` | Osteolysis of bone adjacent to right shoulder joint prosthesis |
| `12217281000119101` | Osteolysis of bone adjacent to left ankle joint prosthesis |
| `12217321000119106` | Osteolysis of bone adjacent to left elbow joint prosthesis |
| `12217361000119101` | Osteolysis of bone adjacent to left finger joint prosthesis |
| `12217481000119102` | Osteolysis of bone adjacent to left shoulder joint prosthesis |
| `129769006` | Calcification cluster |
| `134098971000119103` | Osteolysis of bone adjacent to finger joint prosthesis |
| `1372771000` | Intracranial structural abnormality |
| `1372772007` | Epilepsy due to intracranial structural abnormality |
| `1372773002` | Congenital malformation of cortical development |
| `1372774008` | Epilepsy due to congenital malformation of cortical development |
| `1372777001` | Epilepsy due to neoplasm of brain |
| `1372949000` | Demyelinating disease of brain |
| `1372950000` | Epilepsy due to demyelinating disease of brain |
| `1373227006` | Failed attempted abortion with cardiac failure |

… 799 more, see the CSV.

### SIGNIFICANT · `mii-vs-patho-processing-procedure-snomed-ct` (UNPINNED, filter)

MII VS Patho Processing Procedure [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-processing-procedure-snomed-ct`  
Members: 5096 → 5096


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `406911000` | Permethrin stain method | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 59209009 Toxicology testing for insecticide, ALTERNATIVE → 127790008 Staining method |

**New members (1):**

| Code | Display |
|---|---|
| `448651000124104` | Microscopic examination of cervical Papanicolaou smear and human papillomavirus deoxyribonucleic acid detection |

### SIGNIFICANT · `mii-vs-patho-service-request-code` (UNPINNED, filter)

MII VS Patho Service Request Code  
`https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/ValueSet/mii-vs-patho-service-request-code`  
Members: 6815 → 6815


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `406911000` | Permethrin stain method | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 59209009 Toxicology testing for insecticide, ALTERNATIVE → 127790008 Staining method |

**New members (1):**

| Code | Display |
|---|---|
| `448651000124104` | Microscopic examination of cervical Papanicolaou smear and human papillomavirus deoxyribonucleic acid detection |

## Module `prozedur`

### SIGNIFICANT · `mii-vs-prozedur-prozeduren-snomedct` (pinned, filter)

MII VS Prozedur Prozeduren [SNOMED CT]  
`https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/ValueSet/procedures-sct`  
Members: 60697 → 62931


**Members no longer in the ValueSet:**

| Code | Display | Reason | Successor |
|---|---|---|---|
| `1196926008` | Computed tomography triple phase study of pancreas | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1398941000 CT triple phase of pancreas with contrast |
| `1196930006` | Computed tomography dual phase study of kidney | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1399227008 CT dual phase of kidney with contrast |
| `127803005` | Lung residual volume measurement | inactivated (Duplicate) | SAME AS → 252473009 Residual lung volume test |
| `1303747009` | Intravenous shockwave lithotripsy of atherosclerotic plaque of artery | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1404843006 Imaging guided intravascular shockwave balloon lithotripsy of atherosclerotic plaque of artery, POSSIBLY EQUIVALENT TO → 1404837009 Fluoroscopy guided intravascular shockwave balloon lithotripsy of atherosclerotic plaque of artery with contrast |
| `15872003` | Injection of alcohol into retrobulbar space | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402088007 Injection of alcohol into retrobulbar space |
| `174625005` | Endoscopic change of biliary stent | inactivated (Duplicate) | SAME AS → 709467007 Fluoroscopy guided endoscopic retrograde cholangiopancreatography with replacement of bile duct stent |
| `232183005` | Insertion of bone anchors for subcutaneous bone anchored hearing aid | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401724004 Implantation of magnetic hearing aid bone anchor, POSSIBLY EQUIVALENT TO → 232184004 Implantation of percutaneous hearing aid bone anchor |
| `232663008` | Airway procedure | inactivated (Outdated) | REPLACED BY → 387662008 Respiratory tract procedure |
| `234724006` | Tooth or teeth preparation | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1407172004 Preparation of teeth, POSSIBLY EQUIVALENT TO → 1407171006 Preparation of tooth |
| `234743006` | Bridge preparation of tooth or teeth | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1407193001 Bridge preparation of tooth, POSSIBLY EQUIVALENT TO → 1407194007 Bridge preparation of teeth |
| `236178000` | Therapeutic ureteroscopic operation on ureter | inactivated (Nonconformance to editorial policy) | REPLACED BY → 387717002 Ureteroscopy |
| `236842007` | Subcutaneous alcohol injection of the vulva | inactivated (Outdated) | - |
| `23864003` | Esophagoscopy for biopsy and collection of specimen by brushing or washing | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 71658001 Esophagoscopy for biopsy, POSSIBLY EQUIVALENT TO → 1370946001 Esophagoscopy with brush biopsy and washing |
| `239462008` | Hydrodistension of joint | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402226000 Imaging guided hydrodistension of joint |
| `239463003` | Hydrodistension of shoulder joint | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402227009 Imaging guided hydrodistension of glenohumeral joint |
| `265455000` | Endoscopic sphincterotomy of sphincter of Oddi and removal of calculus | inactivated (Duplicate) | SAME AS → 235583009 Fluoroscopy guided endoscopic retrograde cholangiopancreatography with sphincterotomy of sphincter of Oddi and calculus removal |
| `271490000` | Open endoscopic operation on colon | inactivated (Outdated) | REPLACED BY → 34264006 Intraoperative colonoscopy |
| `287531000` | Enteroscopy via paracentesis | inactivated (Nonconformance to editorial policy) | - |
| `288010005` | Urethral removal of ureteric calculus | inactivated (Nonconformance to editorial policy) | - |
| `29380005` | Insertion of pessary into cervix | inactivated (Erroneous) | REPLACED BY → 1401562003 Insertion of cervical pessary into vagina |
| `307189004` | Alcohol injection of liver metastases | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1258912004 Percutaneous injection of alcohol into neoplasm of liver |
| `312339003` | Stereotactic injection of alcohol to Gasserian ganglion | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402008005 Stereotactic injection of glycerol to Gasserian ganglion, POSSIBLY EQUIVALENT TO → 1402007000 Stereotactic injection of alcohol to Gasserian ganglion |
| `32845008` | Alcohol measurement, urine | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 271289006 Urine alcohol measurement, POSSIBLY EQUIVALENT TO → 1402000003 Measurement of substance with alcohol structure in urine specimen |
| `359578003` | Percutaneous endoscopy through jejunostomy | inactivated (Erroneous) | REPLACED BY → 53402007 Endoscopy of small intestine through artificial stoma |
| `37127001` | Injection of inner ear with alcohol | inactivated (Outdated) | - |
| `386745004` | Transurethral cystoscopy | inactivated (Duplicate) | SAME AS → 142505009 Cystoscopy |
| `406911000` | Permethrin stain method | inactivated (Nonconformance to editorial policy) | ALTERNATIVE → 59209009 Toxicology testing for insecticide, ALTERNATIVE → 127790008 Staining method |
| `418447007` | US scan of orbits | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 127671000146102 Ultrasonography of right orbit proper, POSSIBLY EQUIVALENT TO → 1399538009 Ultrasonography of orbit proper, POSSIBLY EQUIVALENT TO → 127661000146108 Ultrasonography of left orbit proper |
| `430266004` | Radionuclide two-phase bone imaging of wrist | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1404502002 Radionuclide two-phase imaging of bone of wrist region |
| `431895007` | Ultrasonography of graft | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401842000 Ultrasonography of vascular graft |
| `432275005` | Radionuclide imaging of bone of wrist | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1404456006 Radionuclide imaging of bone of carpus, POSSIBLY EQUIVALENT TO → 1404457002 Radionuclide imaging of bone of wrist region |
| `432396001` | Percutaneous pyeloplasty using fluoroscopic guidance | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1406753002 Fluoroscopy guided percutaneous reconstruction of ureteropelvic junction |
| `432779000` | Computed tomography dacryocystography of lacrimal canaliculus | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1397944005 CT dacryocystography of lacrimal canaliculus with contrast |
| `433023004` | Fluoroscopic dacryocystoplasty | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1401820001 Fluoroscopy guided dilation of lacrimal drainage system with contrast |
| `433717001` | Percutaneous injection of alcohol using fluoroscopic guidance | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402089004 Percutaneous injection of alcohol using fluoroscopic guidance |
| `438305004` | CT dual phase study of liver | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1399230001 CT dual phase of liver with contrast |
| `438591004` | Computed tomography triple phase study of liver | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1398939001 CT triple phase of liver with contrast |
| `438814001` | Fluoroscopy guided percutaneous transluminal embolization of branch of iliac vein with contrast | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1409194003 Fluoroscopy guided percutaneous transluminal embolization of common iliac vein with contrast, POSSIBLY EQUIVALENT TO → 1409196001 Fluoroscopy guided percutaneous transluminal embolization of external iliac vein with contrast, POSSIBLY EQUIVALENT TO → 1409195002 Fluoroscopy guided percutaneous transluminal embolization of internal iliac vein with contrast |
| `440514007` | CT dual phase study of pancreas | inactivated (Nonconformance to editorial policy) | REPLACED BY → 1399231002 CT dual phase of pancreas with contrast |
| `442321000` | Measurement of alcohol in blood specimen | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402001004 Measurement of substance with alcohol structure in blood specimen, POSSIBLY EQUIVALENT TO → 167009006 Blood alcohol level |
| `53797006` | Esophagoscopy for destruction of lesion or tumor | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1370964008 Esophagoscopy for destruction of lesion, POSSIBLY EQUIVALENT TO → 1370965009 Esophagoscopy for destruction of tumor |
| `55648009` | Endoscopic dilation of pancreatic duct | inactivated (Duplicate) | SAME AS → 174639005 Fluoroscopy guided endoscopic retrograde pancreatography with dilation of pancreatic duct |
| `60196006` | Injection of alcohol into sympathetic nerve | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402014003 Injection of alcohol into sympathetic nerve |
| `63267000` | Alcohol measurement | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1401999009 Measurement of substance with alcohol structure, POSSIBLY EQUIVALENT TO → 430837008 Alcohol measurement |
| `66399003` | Take-down of cerebral ventricular shunt | inactivated (Duplicate) | SAME AS → 288846002 Cerebrospinal fluid shunt removal |
| `718008007` | Three dimensional cone beam CT of mandible | inactivated (Duplicate) | SAME AS → 718007002 Cone beam CT of mandible |
| `76572000` | Measurement of lung volume | inactivated (Duplicate) | SAME AS → 252472004 Lung volume test |
| `88572002` | Injection of alcohol into nerve | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402006009 Injection of glycerol into nerve, POSSIBLY EQUIVALENT TO → 1402005008 Injection of alcohol into nerve |
| `88851005` | Cerebral ventricular to thoracic cavity shunt | inactivated (Outdated) | REPLACED BY → 1395914006 Creation of ventriculopleural shunt |
| `89516003` | Spinal injection of alcohol | inactivated (Ambiguous) | POSSIBLY EQUIVALENT TO → 1402012004 Spinal injection of alcohol |

**New members (2284):**

| Code | Display |
|---|---|
| `1031691000124108` | Assessment using Drug Abuse Screening Test 10-item version |
| `1031701000124108` | Assessment using Drug Abuse Screening Test 20-item version |
| `1031711000124106` | Assessment using Drug Abuse Screening Test 28-item version |
| `1041731000000106` | MRI of right acetabulum |
| `1046851000000102` | Magnetic resonance venography of bilateral iliac veins |
| `106881000146108` | Parenteral administration of iron supplement |
| `1077571000000106` | Magnetic resonance venography of left iliac vein |
| `1094061000000105` | Plain X-ray of tissue specimen of bilateral breasts |
| `1097641000000108` | PET MRI of bilateral breasts |
| `1097651000000106` | PET MRI of bilateral breasts with contrast |
| `1097701000000103` | PET MRI of bilateral carotid arteries |
| `1097711000000101` | PET MRI of bilateral carotid arteries with contrast |
| `1099521000000105` | Ultrasonography guided localization of iodine 125 radioactive seed to axillary lymph node |
| `1099531000000107` | Ultrasonography guided localization of iodine 125 radioactive seed to left axillary lymph node |
| `1099541000000103` | Ultrasonography guided localization of iodine 125 radioactive seed to lymph node of bilateral axilla |
| `1099551000000100` | Ultrasonography guided localization of iodine 125 radioactive seed to right axillary lymph node |
| `1099871000000106` | Fluoroscopy guided percutaneous transluminal balloon occlusion of vein of left lower limb with contrast |
| `1099881000000108` | Fluoroscopy guided percutaneous transluminal balloon occlusion of vein of right lower limb with contrast |
| `1099891000000105` | Fluoroscopy guided percutaneous transluminal balloon occlusion of vein of bilateral lower limbs with contrast |
| `1103491000000104` | PET MRI of left breast |
| `1103501000000105` | PET MRI of right breast |
| `1103511000000107` | PET MRI of left breast with contrast |
| `1103521000000101` | PET MRI of right breast with contrast |
| `1103531000000104` | PET MRI of left carotid artery |
| `1103541000000108` | PET MRI of right carotid artery |
| `1103551000000106` | PET MRI of left carotid artery with contrast |
| `1103561000000109` | PET MRI of right carotid artery with contrast |
| `1103591000000103` | Radionuclide imaging of sentinel lymph node of left breast |
| `1103601000000109` | Radionuclide imaging of sentinel lymph node of right breast |
| `1103611000000106` | Radionuclide imaging of sentinel lymph node of bilateral breasts |
| `1105061000000104` | Dual energy X-ray absorptiometry of right femur |
| `1105071000000106` | Dual energy X-ray absorptiometry of left femur |
| `1105121000000106` | Dual energy X-ray absorptiometry of bilateral femurs |
| `1105161000000103` | Dual energy X-ray absorptiometry of femur |
| `1108751000000107` | CT of bilateral adrenals with contrast washout |
| `1110811000000104` | CT of bilateral temporal bones, brain and neck with contrast |
| `1111001000000103` | CT dual phase of bilateral kidneys with contrast |
| `1111441000000108` | CT triple phase of bilateral adrenals with contrast |
| `1111801000000107` | CT triple phase of bilateral kidneys with contrast |
| `1113411000000106` | Magnetic resonance venography of right iliac vein |

… 2244 more, see the CSV.

