# pbk_cd_cui_2026

## Notes

<notes>
  <body xmlns="http://www.w3.org/1999/xhtml">
    <p>Cd PBK (Cui et al, 2026):  Notes: Some changes in parameters needs to be set active when modeling factory dust and women </p>
  </body>
</notes>

## Creators

*not specified*

## Overview

| key                          | value                                      |
|:-----------------------------|:-------------------------------------------|
| Modelled species/orgamism(s) | *not specified*                            |
| Model chemical(s)            | http://purl.obolibrary.org/obo/CHEBI_22978 |
| Input route(s)               | 1 (inhalation)                             |
| Time resolution              | d                                          |
| Amounts unit                 | ug                                         |
| Volume unit                  | L                                          |
| Number of compartments       | 12                                         |
| Number of species            | 26                                         |
| Number of parameters         | 98 (43 external / 55 internal)             |

## Diagram

![Diagram](pbk_cd_cui_2026.report.svg)

## Compartments

| id               | name                 | unit   | model qualifier                            |
|:-----------------|:---------------------|:-------|:-------------------------------------------|
| Lung             | Lung                 | L      | http://purl.obolibrary.org/obo/PBPKO_00559 |
| GILumen          | GI Lumen             | L      | http://purl.obolibrary.org/obo/PBPKO_00478 |
| ExtraTissueBlood | Extra Tissue Blood   | L      | *not specified*                            |
| LiverBlood       | liver blood          | L      | http://purl.obolibrary.org/obo/PBPKO_00558 |
| LiverTissue      | liver tissue         | L      | http://purl.obolibrary.org/obo/PBPKO_00558 |
| KidneyBlood      | kidney blood         | L      | http://purl.obolibrary.org/obo/PBPKO_00557 |
| KidneyTissue     | Kidney tissue        | L      | http://purl.obolibrary.org/obo/PBPKO_00557 |
| RestofBodyBlood  | rest of body blood   | L      | http://purl.obolibrary.org/obo/PBPKO_00450 |
| RestofBodyTissue | rest of body tissue  | L      | http://purl.obolibrary.org/obo/PBPKO_00450 |
| Filtrate         | filtrate compartment | L      | http://purl.obolibrary.org/obo/PBPKO_00397 |
| Urine            | urine compartment    | L      | http://purl.obolibrary.org/obo/PBPKO_00556 |
| Feces            | feces compartment    | L      | http://purl.obolibrary.org/obo/PBPKO_00555 |

## Species

| id                 | name                                               | unit   | model qualifier                            |
|:-------------------|:---------------------------------------------------|:-------|:-------------------------------------------|
| ALU                | amount in lung                                     | ug     | http://purl.obolibrary.org/obo/PBPKO_00504 |
| AGILumen           | amount in gut lumen                                | ug     | http://purl.obolibrary.org/obo/PBPKO_06009 |
| AETB_Free          | free amount in extra tissue blood                  | ug     | *not specified*                            |
| AETB_PP            | Plasma protein bound amount in extra tissue blood  | ug     | *not specified*                            |
| AETB_RBC           | Red blood cell bound amount in extra tissue blood  | ug     | *not specified*                            |
| ALiverB_Free       | free amount in liver blood                         | ug     | *not specified*                            |
| ALiverB_PP         | Plasma protein bound amount in liver blood         | ug     | *not specified*                            |
| ALiverB_RBC        | Red blood cell bound amount in liver blood         | ug     | *not specified*                            |
| ALiverT_Free       | free amount in liver tissue                        | ug     | *not specified*                            |
| ALiverT_MT         | metallothionine bound amount in liver tissue       | ug     | *not specified*                            |
| AKidneyB_Free      | free amount in kidney blood                        | ug     | *not specified*                            |
| AKidneyB_PP        | Plasma protein bound amount in kidney blood        | ug     | *not specified*                            |
| AKidneyB_RBC       | Red blood cell bound amount in kidney blood        | ug     | *not specified*                            |
| AKidneyT_Free      | free amount in kidney tissue                       | ug     | *not specified*                            |
| AKidneyT_MT        | metallothionine bound amount in kidney tissue      | ug     | *not specified*                            |
| ARBB_Free          | free amount in rest of body blood                  | ug     | *not specified*                            |
| ARBB_PP            | Plasma protein bound amount in rest of body blood  | ug     | *not specified*                            |
| ARBB_RBC           | Red blood cell bound amount in rest of body blood  | ug     | *not specified*                            |
| ARBT_Free          | free amount in rest of body tissue                 | ug     | *not specified*                            |
| AFiltrate_Free     | free amount in filtrate                            | ug     | *not specified*                            |
| AFiltrate_MT       | metallothionine bound amount in filtrate           | ug     | *not specified*                            |
| AUrineFiltrate     | amount urine from filtrate                         | ug     | http://purl.obolibrary.org/obo/PBPKO_00272 |
| AUrineKidneyTissue | amount in urine from kidney tissue                 | ug     | http://purl.obolibrary.org/obo/PBPKO_00272 |
| AFecesUnabsorbed   | amount in feces from unabsorbed GI lumen fraction  | ug     | http://purl.obolibrary.org/obo/PBPKO_00273 |
| AFecesBile         | amount in feces from biliary excretion             | ug     | http://purl.obolibrary.org/obo/PBPKO_00273 |
| AFecesIT           | amount in feces from from intestine walls excreted | ug     | http://purl.obolibrary.org/obo/PBPKO_00273 |

## Transfer equations

| id   | from           | to                 | equation                  |
|:-----|:---------------|:-------------------|:--------------------------|
| _J0  | ALU            | AGILumen           | C4 * ALU                  |
| _J1  | ALU            | AETB_Free          | uptake2_Lung              |
| _J2  | ALU            | AETB_PP            | uptake1_Lung              |
| _J3  | AGILumen       | ALiverB_Free       | uptake2_GI                |
| _J4  | AGILumen       | ALiverB_PP         | uptake1_GI                |
| _J5  | AETB_Free      | ALiverB_Free       | QL * CABlood_Free         |
| _J6  | AETB_PP        | ALiverB_PP         | QL * CABlood_PP           |
| _J7  | AETB_RBC       | ALiverB_RBC        | QL * CABlood_RBC          |
| _J8  | AETB_Free      | AKidneyB_Free      | QK * CABlood_Free         |
| _J9  | AETB_PP        | AKidneyB_PP        | QK * CABlood_PP           |
| _J10 | AETB_RBC       | AKidneyB_RBC       | QK * CABlood_RBC          |
| _J11 | AETB_Free      | ARBB_Free          | QRB * CABlood_Free        |
| _J12 | AETB_PP        | ARBB_PP            | QRB * CABlood_PP          |
| _J13 | AETB_RBC       | ARBB_RBC           | QRB * CABlood_RBC         |
| _J14 | AETB_PP        | AETB_Free          | k5 * AETB_PP              |
| _J15 | AETB_Free      | AETB_PP            | k6 * AETB_Free * PP       |
| _J16 | AETB_RBC       | AETB_Free          | C16 * AETB_RBC            |
| _J17 | AETB_Free      | AETB_RBC           | CX * AETB_Free * RBC      |
| _J18 | ALiverB_Free   | AETB_Free          | QL * CVLiverB_Free        |
| _J19 | ALiverB_Free   | ALiverB_PP         | k6 * ALiverB_Free * PP    |
| _J20 | ALiverB_Free   | ALiverB_RBC        | CX * ALiverB_Free * RBC   |
| _J21 | ALiverB_PP     | AETB_PP            | QL * CVLiverB_PP          |
| _J22 | ALiverB_PP     | ALiverB_Free       | k5 * ALiverB_PP           |
| _J23 | ALiverB_RBC    | AETB_RBC           | QL * CVLiverB_RBC         |
| _J24 | ALiverB_RBC    | ALiverB_Free       | C16 * ALiverB_RBC         |
| _J25 | ALiverT_Free   | ALiverB_Free       | C13 * CLiverT_Free        |
| _J26 | ALiverB_Free   | ALiverT_Free       | C12 * CVLiverB_Free       |
| _J27 | ALiverT_MT     | ALiverT_Free       | k12 * ALiverT_MT          |
| _J28 | ALiverT_Free   | ALiverT_MT         | k13 * ALiverT_Free * MTL  |
| _J29 | ALiverT_MT     | ALiverB_PP         | C14 * CLiverT_MT          |
| _J30 | AKidneyB_Free  | AETB_Free          | QK * CVKidneyB_Free       |
| _J31 | AKidneyB_Free  | AKidneyB_PP        | k6 * AKidneyB_Free * PP   |
| _J32 | AKidneyB_Free  | AKidneyB_RBC       | CX * AKidneyB_Free * RBC  |
| _J33 | AKidneyB_PP    | AETB_PP            | QK * CVKidneyB_PP         |
| _J34 | AKidneyB_PP    | AKidneyB_Free      | k5 * AKidneyB_PP          |
| _J35 | AKidneyB_RBC   | AETB_RBC           | QK * CVKidneyB_RBC        |
| _J36 | AKidneyB_RBC   | AKidneyB_Free      | C16 * AKidneyB_RBC        |
| _J37 | AKidneyT_MT    | AKidneyT_Free      | k20 * AKidneyT_MT         |
| _J38 | AKidneyT_Free  | AKidneyT_MT        | k21 * AKidneyT_Free * MTK |
| _J39 | AKidneyT_Free  | AKidneyB_Free      | C18 * CKidneyT_Free       |
| _J40 | AFiltrate_MT   | AKidneyT_MT        | C17 * AFiltrate_MT        |
| _J41 | ARBB_Free      | AETB_Free          | QRB * CVRBB_Free          |
| _J42 | ARBB_Free      | ARBB_PP            | k6 * ARBB_Free * PP       |
| _J43 | ARBB_Free      | ARBB_RBC           | CX * ARBB_Free * RBC      |
| _J44 | ARBB_PP        | AETB_PP            | QRB * CVRBB_PP            |
| _J45 | ARBB_PP        | ARBB_Free          | k5 * ARBB_PP              |
| _J46 | ARBB_RBC       | AETB_RBC           | QRB * CVRBB_RBC           |
| _J47 | ARBB_RBC       | ARBB_Free          | C16 * ARBB_RBC            |
| _J48 | ARBT_Free      | ARBB_Free          | C10 * CRBT_Free           |
| _J49 | ARBB_Free      | ARBT_Free          | C9 * CVRBB_Free           |
| _J50 | AKidneyB_Free  | AFiltrate_Free     | k16 * CVKidneyB_Free      |
| _J51 | AKidneyB_PP    | AFiltrate_MT       | k15 * CVKidneyB_PP        |
| _J52 | AFiltrate_Free | AUrineFiltrate     | k18 * AFiltrate_Free      |
| _J53 | AFiltrate_MT   | AUrineFiltrate     | (1 - C17) * AFiltrate_MT  |
| _J54 | AKidneyT_Free  | AUrineKidneyTissue | C19 * AKidneyT_Free       |
| _J55 | AKidneyT_MT    | AUrineKidneyTissue | C19 * AKidneyT_MT         |
| _J56 | ALiverT_Free   | AFecesBile         | C15 * ALiverT_Free        |
| _J57 | ARBT_Free      | AFecesIT           | C11 * ARBT_Free           |

## ODEs

| species            | equation                                                                                                                                                                                                                                                                                                                                                                                                         |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALU                | d[ALU]/dt = - C4 * ALU            - uptake2_Lung            - uptake1_Lung                                                                                                                                                                                                                                                                                                                                       |
| AGILumen           | d[AGILumen]/dt = C4 * ALU                 - uptake2_GI                 - uptake1_GI                                                                                                                                                                                                                                                                                                                              |
| AETB_Free          | d[AETB_Free]/dt = uptake2_Lung                  - QL * CABlood_Free                  - QK * CABlood_Free                  - QRB * CABlood_Free                  + k5 * AETB_PP                  - k6 * AETB_Free * PP                  + C16 * AETB_RBC                  - CX * AETB_Free * RBC                  + QL * CVLiverB_Free                  + QK * CVKidneyB_Free                  + QRB * CVRBB_Free |
| AETB_PP            | d[AETB_PP]/dt = uptake1_Lung                - QL * CABlood_PP                - QK * CABlood_PP                - QRB * CABlood_PP                - k5 * AETB_PP                + k6 * AETB_Free * PP                + QL * CVLiverB_PP                + QK * CVKidneyB_PP                + QRB * CVRBB_PP                                                                                                         |
| AETB_RBC           | d[AETB_RBC]/dt = - QL * CABlood_RBC                 - QK * CABlood_RBC                 - QRB * CABlood_RBC                 - C16 * AETB_RBC                 + CX * AETB_Free * RBC                 + QL * CVLiverB_RBC                 + QK * CVKidneyB_RBC                 + QRB * CVRBB_RBC                                                                                                                    |
| ALiverB_Free       | d[ALiverB_Free]/dt = uptake2_GI                     + QL * CABlood_Free                     - QL * CVLiverB_Free                     - k6 * ALiverB_Free * PP                     - CX * ALiverB_Free * RBC                     + k5 * ALiverB_PP                     + C16 * ALiverB_RBC                     + C13 * CLiverT_Free                     - C12 * CVLiverB_Free                                     |
| ALiverB_PP         | d[ALiverB_PP]/dt = uptake1_GI                   + QL * CABlood_PP                   + k6 * ALiverB_Free * PP                   - QL * CVLiverB_PP                   - k5 * ALiverB_PP                   + C14 * CLiverT_MT                                                                                                                                                                                       |
| ALiverB_RBC        | d[ALiverB_RBC]/dt = QL * CABlood_RBC                    + CX * ALiverB_Free * RBC                    - QL * CVLiverB_RBC                    - C16 * ALiverB_RBC                                                                                                                                                                                                                                                  |
| ALiverT_Free       | d[ALiverT_Free]/dt = - C13 * CLiverT_Free                     + C12 * CVLiverB_Free                     + k12 * ALiverT_MT                     - k13 * ALiverT_Free * MTL                     - C15 * ALiverT_Free                                                                                                                                                                                               |
| ALiverT_MT         | d[ALiverT_MT]/dt = - k12 * ALiverT_MT                   + k13 * ALiverT_Free * MTL                   - C14 * CLiverT_MT                                                                                                                                                                                                                                                                                          |
| AKidneyB_Free      | d[AKidneyB_Free]/dt = QK * CABlood_Free                      - QK * CVKidneyB_Free                      - k6 * AKidneyB_Free * PP                      - CX * AKidneyB_Free * RBC                      + k5 * AKidneyB_PP                      + C16 * AKidneyB_RBC                      + C18 * CKidneyT_Free                      - k16 * CVKidneyB_Free                                                       |
| AKidneyB_PP        | d[AKidneyB_PP]/dt = QK * CABlood_PP                    + k6 * AKidneyB_Free * PP                    - QK * CVKidneyB_PP                    - k5 * AKidneyB_PP                    - k15 * CVKidneyB_PP                                                                                                                                                                                                            |
| AKidneyB_RBC       | d[AKidneyB_RBC]/dt = QK * CABlood_RBC                     + CX * AKidneyB_Free * RBC                     - QK * CVKidneyB_RBC                     - C16 * AKidneyB_RBC                                                                                                                                                                                                                                           |
| AKidneyT_Free      | d[AKidneyT_Free]/dt = k20 * AKidneyT_MT                      - k21 * AKidneyT_Free * MTK                      - C18 * CKidneyT_Free                      - C19 * AKidneyT_Free                                                                                                                                                                                                                                   |
| AKidneyT_MT        | d[AKidneyT_MT]/dt = - k20 * AKidneyT_MT                    + k21 * AKidneyT_Free * MTK                    + C17 * AFiltrate_MT                    - C19 * AKidneyT_MT                                                                                                                                                                                                                                            |
| ARBB_Free          | d[ARBB_Free]/dt = QRB * CABlood_Free                  - QRB * CVRBB_Free                  - k6 * ARBB_Free * PP                  - CX * ARBB_Free * RBC                  + k5 * ARBB_PP                  + C16 * ARBB_RBC                  + C10 * CRBT_Free                  - C9 * CVRBB_Free                                                                                                                  |
| ARBB_PP            | d[ARBB_PP]/dt = QRB * CABlood_PP                + k6 * ARBB_Free * PP                - QRB * CVRBB_PP                - k5 * ARBB_PP                                                                                                                                                                                                                                                                              |
| ARBB_RBC           | d[ARBB_RBC]/dt = QRB * CABlood_RBC                 + CX * ARBB_Free * RBC                 - QRB * CVRBB_RBC                 - C16 * ARBB_RBC                                                                                                                                                                                                                                                                     |
| ARBT_Free          | d[ARBT_Free]/dt = - C10 * CRBT_Free                  + C9 * CVRBB_Free                  - C11 * ARBT_Free                                                                                                                                                                                                                                                                                                        |
| AFiltrate_Free     | d[AFiltrate_Free]/dt = k16 * CVKidneyB_Free                       - k18 * AFiltrate_Free                                                                                                                                                                                                                                                                                                                         |
| AFiltrate_MT       | d[AFiltrate_MT]/dt = - C17 * AFiltrate_MT                     + k15 * CVKidneyB_PP                     - (1 - C17) * AFiltrate_MT                                                                                                                                                                                                                                                                                |
| AUrineFiltrate     | d[AUrineFiltrate]/dt = k18 * AFiltrate_Free                       + (1 - C17) * AFiltrate_MT                                                                                                                                                                                                                                                                                                                     |
| AUrineKidneyTissue | d[AUrineKidneyTissue]/dt = C19 * AKidneyT_Free                           + C19 * AKidneyT_MT                                                                                                                                                                                                                                                                                                                     |
| AFecesBile         | d[AFecesBile]/dt = C15 * ALiverT_Free                                                                                                                                                                                                                                                                                                                                                                            |
| AFecesIT           | d[AFecesIT]/dt = C11 * ARBT_Free                                                                                                                                                                                                                                                                                                                                                                                 |

## Assignment rules

| variable         | assignment                                                                                                                                                                                    |
|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtraTissueBlood | VETB                                                                                                                                                                                          |
| LiverBlood       | VLiverB                                                                                                                                                                                       |
| LiverTissue      | VLiverT                                                                                                                                                                                       |
| KidneyBlood      | VKidneyB                                                                                                                                                                                      |
| KidneyTissue     | VKidneyT                                                                                                                                                                                      |
| RestofBodyBlood  | VRBB                                                                                                                                                                                          |
| RestofBodyTissue | VRBT                                                                                                                                                                                          |
| Age              | time / 365 + AgeInit                                                                                                                                                                          |
| VB               | FVB * BWl                                                                                                                                                                                     |
| VL               | Iwa * pow(BWl / BWa, 0.85)                                                                                                                                                                    |
| VLiverB          | FVLB * VL                                                                                                                                                                                     |
| VLiverT          | (1 - FVLB) * VL                                                                                                                                                                               |
| VK               | kwa * pow(BWl / BWa, 0.84)                                                                                                                                                                    |
| VKidneyB         | FVKB * VK                                                                                                                                                                                     |
| VKidneyT         | (1 - FVKB) * VK                                                                                                                                                                               |
| A                | VB - VLiverB - VKidneyB                                                                                                                                                                       |
| B                | BWl - VL - VK                                                                                                                                                                                 |
| VETB             | (A - FVRBB * B) / (1 - FVRBB)                                                                                                                                                                 |
| VRB              | B - VETB                                                                                                                                                                                      |
| VRBB             | FVRBB * VRB                                                                                                                                                                                   |
| VRBT             | (1 - FVRBB) * VRB                                                                                                                                                                             |
| Lbm              | 0.88 * BWl                                                                                                                                                                                    |
| tmp              | (Lbm - 8.58) / 0.0272 / 1000                                                                                                                                                                  |
| UCER             | piecewise(0.5, lt(tmp, 0.5), tmp)                                                                                                                                                             |
| QCB              | 15 * pow(BWl, 0.74) * 24                                                                                                                                                                      |
| QL               | FQL * QCB                                                                                                                                                                                     |
| QK               | FQK * QCB                                                                                                                                                                                     |
| FQRB             | 1 - FQL - FQK                                                                                                                                                                                 |
| QRB              | FQRB * QCB                                                                                                                                                                                    |
| C14              | f9 * QL                                                                                                                                                                                       |
| C13              | f10 * QL                                                                                                                                                                                      |
| C12              | f11 * QL                                                                                                                                                                                      |
| k15              | f15 * QK                                                                                                                                                                                      |
| k16              | f16 * QK                                                                                                                                                                                      |
| C17              | piecewise(C17x - C17x / 3 * (Age - 30) / 50, gt(Age, 30), C17x)                                                                                                                               |
| C19              | piecewise(C19x + C21 * (Age - 30), gt(Age, 30), C19x)                                                                                                                                         |
| C18              | f22 * QK                                                                                                                                                                                      |
| C10              | f23 * QRB                                                                                                                                                                                     |
| C9               | f24 * QRB                                                                                                                                                                                     |
| CABlood_Free     | AETB_Free / VETB                                                                                                                                                                              |
| CABlood_PP       | AETB_PP / VETB                                                                                                                                                                                |
| CABlood_RBC      | AETB_RBC / VETB                                                                                                                                                                               |
| CVLiverB_Free    | ALiverB_Free / VLiverB                                                                                                                                                                        |
| CVLiverB_PP      | ALiverB_PP / VLiverB                                                                                                                                                                          |
| CVLiverB_RBC     | ALiverB_RBC / VLiverB                                                                                                                                                                         |
| CLiverT_Free     | ALiverT_Free / VLiverT                                                                                                                                                                        |
| CLiverT_MT       | ALiverT_MT / VLiverT                                                                                                                                                                          |
| CVKidneyB_Free   | AKidneyB_Free / VKidneyB                                                                                                                                                                      |
| CVKidneyB_PP     | AKidneyB_PP / VKidneyB                                                                                                                                                                        |
| CVKidneyB_RBC    | AKidneyB_RBC / VKidneyB                                                                                                                                                                       |
| CKidneyT_Free    | AKidneyT_Free / VKidneyT                                                                                                                                                                      |
| CKidneyT_MT      | AKidneyT_MT / VKidneyT                                                                                                                                                                        |
| CVRBB_Free       | ARBB_Free / VRBB                                                                                                                                                                              |
| CVRBB_PP         | ARBB_PP / VRBB                                                                                                                                                                                |
| CVRBB_RBC        | ARBB_RBC / VRBB                                                                                                                                                                               |
| CRBT_Free        | ARBT_Free / VRBT                                                                                                                                                                              |
| uptakeTotal_Lung | C3 * ALU                                                                                                                                                                                      |
| uptake1_Lung     | piecewise(0, leq(uptakeTotal_Lung + uptakeTotal_GI, 0), C8 * uptakeTotal_Lung / (uptakeTotal_Lung + uptakeTotal_GI), gt(C7 * (uptakeTotal_Lung + uptakeTotal_GI), C8), C7 * uptakeTotal_Lung) |
| uptakeTotal_GI   | C6 * AGILumen                                                                                                                                                                                 |
| uptake2_Lung     | uptakeTotal_Lung - uptake1_Lung                                                                                                                                                               |
| uptake1_GI       | piecewise(0, leq(uptakeTotal_Lung + uptakeTotal_GI, 0), C8 * uptakeTotal_GI / (uptakeTotal_Lung + uptakeTotal_GI), gt(C7 * (uptakeTotal_Lung + uptakeTotal_GI), C8), C7 * uptakeTotal_GI)     |
| uptake2_GI       | uptakeTotal_GI - uptake1_GI                                                                                                                                                                   |

## Parameters

| id               | name                                                                                                                                      | unit            | model qualifier                            |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:-------------------------------------------|
| AgeInit          | *not specified*                                                                                                                           | *not specified* | *not specified*                            |
| Age              | Age                                                                                                                                       | y               | http://purl.obolibrary.org/obo/PBPKO_00521 |
| BWa              | average bodyweight                                                                                                                        | kg              | http://purl.obolibrary.org/obo/PBPKO_00008 |
| BWl              | age-dependent bodyweight                                                                                                                  | kg              | http://purl.obolibrary.org/obo/PBPKO_00008 |
| FVB              | Fractional total blood volume                                                                                                             | dimensionless   | *not specified*                            |
| VB               | Total blood volume                                                                                                                        | L               | *not specified*                            |
| Iwa              | Average adult liver weight                                                                                                                | kg              | *not specified*                            |
| VL               | Liver volume                                                                                                                              | L               | http://purl.obolibrary.org/obo/PBPKO_00077 |
| FVLB             | Fractional Liver Blood volume                                                                                                             | dimensionless   | http://purl.obolibrary.org/obo/PBPKO_00078 |
| VLiverB          | Liver Blood volume                                                                                                                        | L               | *not specified*                            |
| VLiverT          | Liver Tissue volume                                                                                                                       | L               | *not specified*                            |
| kwa              | Average adult kidney weight                                                                                                               | kg              | *not specified*                            |
| VK               | Kidney volume                                                                                                                             | L               | http://purl.obolibrary.org/obo/PBPKO_00079 |
| FVKB             | Fractional kidney blood volume                                                                                                            | dimensionless   | http://purl.obolibrary.org/obo/PBPKO_00080 |
| VKidneyB         | Kidney Blood volume                                                                                                                       | L               | *not specified*                            |
| VKidneyT         | Kidney Tissue volume                                                                                                                      | L               | *not specified*                            |
| FVRBB            | Fractional RB blood volume                                                                                                                | dimensionless   | http://purl.obolibrary.org/obo/PBPKO_00106 |
| A                | intermediate variable to calculate blood volume for rest of body                                                                          | L               | *not specified*                            |
| B                | intermediate variable to calculate volume for rest of body                                                                                | L               | *not specified*                            |
| VETB             | Extra-tissue blood volume                                                                                                                 | L               | *not specified*                            |
| VRB              | Rest of body volume                                                                                                                       | L               | http://purl.obolibrary.org/obo/PBPKO_00105 |
| VRBB             | Rest of body blood volume                                                                                                                 | L               | *not specified*                            |
| VRBT             | Rest of body tissue volume                                                                                                                | L               | *not specified*                            |
| Lbm              | lean body mass                                                                                                                            | kg              | *not specified*                            |
| tmp              | predicts daily creatinine excretion from lean body mass                                                                                   | g/d             | *not specified*                            |
| UCER             | Urinary creatinine excretion rate                                                                                                         | g/d             | *not specified*                            |
| QCB              | cardiac output rate                                                                                                                       | L/d             | http://purl.obolibrary.org/obo/PBPKO_00013 |
| FQL              | fraction of blood flow to liver                                                                                                           | dimensionless   | http://purl.obolibrary.org/obo/PBPKO_00025 |
| QL               | blood flow rate to liver                                                                                                                  | L/d             | http://purl.obolibrary.org/obo/PBPKO_00024 |
| FQK              | fraction of blood flow to kidney                                                                                                          | dimensionless   | http://purl.obolibrary.org/obo/PBPKO_00027 |
| QK               | blood flow rate to kidney                                                                                                                 | L/d             | http://purl.obolibrary.org/obo/PBPKO_00026 |
| FQRB             | fraction of blood flow to restbody                                                                                                        | dimensionless   | http://purl.obolibrary.org/obo/PBPKO_00051 |
| QRB              | blood flow rate to restbody                                                                                                               | L/d             | http://purl.obolibrary.org/obo/PBPKO_00050 |
| C5               | Fraction of Cd in GI tract to be absorbed                                                                                                 | dimensionless   | *not specified*                            |
| C7               | Fraction of Cd absorbed as CdMT                                                                                                           | dimensionless   | *not specified*                            |
| C3               | Rate constant of absorption of Cd in Lung to ETB                                                                                          | /d              | *not specified*                            |
| C4               | Rate constant of transfer of Cd in Lung to GI-tract                                                                                       | /d              | *not specified*                            |
| C6               | Rate constant of absorption of Cd in Intestine lumen to Liver Blood                                                                       | /d              | *not specified*                            |
| C8               | Maximum CdMT absorption rate                                                                                                              | /d              | *not specified*                            |
| k5               | Rate constant of dissociation of plasma protein-bound Cd (CdPP) into Free Cd and PP                                                       | /d              | *not specified*                            |
| k6               | Rate constant of association of Free Cd and PP to form CdPP                                                                               | /d              | *not specified*                            |
| CX               | Rate constant of sequestration of Free Cd into RBC                                                                                        | /d              | *not specified*                            |
| C16              | Rate constant of CdRBC turnover                                                                                                           | /d              | *not specified*                            |
| f9               | Coefficient of CdMT efflux from Liver Tissue to Liver Blood relative to Liver Blood flow                                                  | dimensionless   | *not specified*                            |
| f10              | Coefficient of Free Cd efflux from Liver Tissue to Liver Blood relative to Liver Blood flow                                               | dimensionless   | *not specified*                            |
| f11              | Coefficient of Free Cd influx from Liver Blood to Liver Tissue relative to Liver Blood flow                                               | dimensionless   | *not specified*                            |
| C14              | Rate constant of CdMT efflux from Liver Tissue to Liver Blood                                                                             | L/d             | *not specified*                            |
| C13              | Rate constant of Free Cd efflux from Liver Tissue to Liver Blood                                                                          | L/d             | *not specified*                            |
| C12              | Rate constant of Free Cd influx from Liver Blood to Liver Tissue                                                                          | L/d             | *not specified*                            |
| k12              | Rate constant of dissociation of CdMT into Free Cd and MT in Liver Tissue                                                                 | /d              | *not specified*                            |
| k13              | Rate constant of association of Free Cd and MT to form CdMT in Liver Tissue                                                               | /d              | *not specified*                            |
| C15              | Rate constant of Free Cd excretion from Liver Tissue to feces via bile                                                                    | /d              | *not specified*                            |
| f15              | Coefficient of CdMT filtration from Kidney Blood to Filtrate relative to Kidney Blood flow                                                | dimensionless   | *not specified*                            |
| f16              | Coefficient of Free Cd filtration from Kidney Blood to Filtrate relative to Kidney Blood flow                                             | dimensionless   | *not specified*                            |
| k15              | Rate constant of CdMT filtration from Kidney Blood to Filtrate                                                                            | L/d             | *not specified*                            |
| k16              | Rate constant of Free Cd filtration from Kidney Blood to Filtrate                                                                         | L/d             | *not specified*                            |
| C17x             | Age-dependent rate constant of CdMT reabsorption from Filtrate to Kidney Tissue                                                           | /d              | *not specified*                            |
| C17              | Rate constant of CdMT reabsorption from Filtrate to Kidney Tissue for age <= 30                                                           | /d              | *not specified*                            |
| k18              | Rate constant of Free Cd excretion from Filtrate to urine                                                                                 | /d              | *not specified*                            |
| C21              | Coefficient of increase of rate constant of Free Cd and CdMT excretion from Kidney Tissue to urine for age >30 (unit in /d y)             | *not specified* | *not specified*                            |
| C19x             | Age-dependent rate constant of Free Cd and CdMT excretion from Kidney Tissue to urine                                                     | /d              | *not specified*                            |
| C19              | Rate constant of Free Cd and CdMT excretion from Kidney Tissue to urine for age <= 30                                                     | /d              | *not specified*                            |
| k20              | Rate constant of dissociation of CdMT in Kidney Tissue into Free Cd and MT in Kidney Tissue                                               | /d              | *not specified*                            |
| k21              | Rate constant of association of Free Cd and MT to form CdMT in Kidney Tissue                                                              | /d              | *not specified*                            |
| f22              | Coefficient of Free Cd efflux from Kidney Tissue to Kidney Blood relative to Kidney Blood flow                                            | dimensionless   | *not specified*                            |
| C18              | Rate constant of Free Cd efflux from Kidney Tissue to Kidney Blood                                                                        | L/d             | *not specified*                            |
| f23              | Coefficient of Free Cd efflux from RB Tissue to RB Blood relative to RB Blood flow                                                        | dimensionless   | *not specified*                            |
| f24              | Coefficient of Free Cd influx from RB Blood to RB Tissue relative to RB Blood flow                                                        | dimensionless   | *not specified*                            |
| C10              | Rate constant of Free Cd efflux from RB Tissue to RB Blood                                                                                | L/d             | *not specified*                            |
| C9               | Rate constant of Free Cd influx from RB Blood to RB Tissue                                                                                | L/d             | *not specified*                            |
| C11              | Rate constant of Cd excretion from RB Tissue to feces representing fecal Cd sourced from intestine excretion and intestine wall sloughing | /d              | *not specified*                            |
| PP               | Free plasma protein                                                                                                                       | dimensionless   | *not specified*                            |
| RBC              | Free red blood cells                                                                                                                      | dimensionless   | *not specified*                            |
| MTL              | Free Metallothionine in Liver Tissue                                                                                                      | dimensionless   | *not specified*                            |
| MTK              | Free Metallothionine in Kidney Tissue                                                                                                     | dimensionless   | *not specified*                            |
| CABlood_Free     | unbound concentration in arterial blood                                                                                                   | ug/L            | *not specified*                            |
| CABlood_PP       | plasma protein bound concentration in arterial blood                                                                                      | ug/L            | *not specified*                            |
| CABlood_RBC      | red blood cell bound concentration in arterial blood                                                                                      | ug/L            | *not specified*                            |
| CVLiverB_Free    | unbound concentration in liver venouse blood                                                                                              | ug/L            | *not specified*                            |
| CVLiverB_PP      | protein plasma bound concentration in liver venouse blood                                                                                 | ug/L            | *not specified*                            |
| CVLiverB_RBC     | red blood cell bound concentration in liver venouse blood                                                                                 | ug/L            | *not specified*                            |
| CLiverT_Free     | unbound concentration in liver tissue                                                                                                     | ug/L            | *not specified*                            |
| CLiverT_MT       | metallothionine bound concentration in liver tissue                                                                                       | ug/L            | *not specified*                            |
| CVKidneyB_Free   | unbound concentration in kidney venouse blood                                                                                             | ug/L            | *not specified*                            |
| CVKidneyB_PP     | protein plasma bound concentration in kidney venouse blood                                                                                | ug/L            | *not specified*                            |
| CVKidneyB_RBC    | red blood cell bound concentration in kidney venouse blood                                                                                | ug/L            | *not specified*                            |
| CKidneyT_Free    | unbound concentration in kidney tissue                                                                                                    | ug/L            | *not specified*                            |
| CKidneyT_MT      | metallothionine bound concentration in kidney tissue                                                                                      | ug/L            | *not specified*                            |
| CVRBB_Free       | unbound concentration in rest of body venouse blood                                                                                       | ug/L            | *not specified*                            |
| CVRBB_PP         | protein plasma bound concentration in rest of body venouse blood                                                                          | ug/L            | *not specified*                            |
| CVRBB_RBC        | red blood cell bound concentration in rest of body venouse blood                                                                          | ug/L            | *not specified*                            |
| CRBT_Free        | unbound concentration in rest of body tissue                                                                                              | ug/L            | *not specified*                            |
| uptakeTotal_Lung | total daily amount in Lung                                                                                                                | ug/d            | *not specified*                            |
| uptake1_Lung     | fraction of total daily amount in Lung to protein plasma bound amount in extra tissue blood                                               | ug/d            | *not specified*                            |
| uptakeTotal_GI   | total daily amount in GI tract                                                                                                            | ug/d            | *not specified*                            |
| uptake2_Lung     | fraction of total daily amount in Lung to free amount in extra tissue blood                                                               | ug/d            | *not specified*                            |
| uptake1_GI       | fraction of total daily amount in GI tract to protein plasma bound amount in liver blood                                                  | ug/d            | *not specified*                            |
| uptake2_GI       | fraction of total daily amount in GI tract to free amount in liver blood                                                                  | ug/d            | *not specified*                            |

