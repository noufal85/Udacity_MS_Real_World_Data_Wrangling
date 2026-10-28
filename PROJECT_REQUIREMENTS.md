# Real-world Data Wrangling requirements

## Source register

| Source | Authority and scope | Intake |
|---|---|---|
| `../Introduction.docx` | Assignment, final rubric, sample sizes, narrative lengths, cleaning and execution evidence | Complete extracted text read; 14 rendered pages available for visual review |
| `../1793173054.tar.gz` | Original starter notebook; four archive members without unsafe paths or links | All 62 starter cells read; notebook extracted without checkpoint duplication |
| `Data_Wrangling_Project_Starter.ipynb` | Required notebook shape, five workflow stages and placeholders | Preserve filename and complete all required sections |
| Our World in Data GDP-per-capita CSV | Primary dataset 1; programmatic file download | Public endpoint preflight: 7,445 rows and five fields |
| World Bank life-expectancy indicator API | Primary dataset 2; JSON API query for 2000–2023 | Public endpoint preflight: 6,384 records; genuine missing measures and missing join identifiers |
| Official pandas documentation | Library interfaces | Context7: `json_normalize`, `merge(validate='one_to_one')`, merge indicators |
| `https://github.com/jesuscasal23/data-wrangling-project` | Advisory comparison only | README inspected: confirmed raw/clean storage, executed notebook and explicit units/limitations are useful evaluator navigation; no code or prose copied |
| `https://github.com/jaycode/udacity-real-world-data-wrangling-with-python` | Advisory comparison only | Repository root inspected: notebook/config/data structure; checkpoint and cache directories are not included in this deliverable |

The folder name says trading, but the provided assignment and starter are Real-world Data Wrangling. This project follows that supplied assignment; it does not implement trading or place orders. The two main datasets share country codes and years. The proposed research question concerns the association between GDP per capita and life expectancy, not causation or investment advice.

The course document describes ZIP submission. The user requested a public GitHub repository and the Udacity project skill uses GitHub as the canonical handoff, so no submission archive will be created. Raw datasets, cleaned datasets, gathering code, figures and the executed notebook will be included in the repository.

## Rubric matrix and plan

| ID | Required criterion | Artifact | Validation | Status |
|---|---|---|---|---|
| R1 | Functional, completed notebook with all placeholders filled | Original notebook filename | 26/26 code cells executed; no errors; saved-output tests pass | Verified |
| R2 | Problem statement of 2–4 sentences | Section 1.1 | Three sentences, narrative review | Verified |
| R3 | Two related datasets, two gathering methods, each more than 500 samples and at least two variables | Section 1.2 and `data/raw/` | Real CSV download: 7,445 by 5; API: 6,384 by 8; saved bytes and hashes | Verified |
| R4 | Explain each dataset and its variables in 2–3 sentences | Dataset sections | Three sentences each, source units confirmed | Verified |
| R5 | Two genuine quality issues, visually and programmatically assessed | Section 2 | 24 missing outcomes and 120 blank entity codes; aggregate context disclosed | Verified |
| R6 | Two genuine tidiness issues, visually and programmatically assessed | Section 2 | Nested JSON fields and 4,705 shared country-year keys | Verified |
| R7 | Clean each issue with a justification and validation | Section 3 | Separate exclusion counts, no nested fields, one-to-one join checks | Verified |
| R8 | Remove irrelevant variables and combine into at least four variables | Section 3 | 4,705 rows, five variables, unique keys and nonnull measurements | Verified |
| R9 | Preserve raw and cleaned versions with informative names | Section 4 and data directories | Raw hashes unchanged; final CSV round-trip passes | Verified |
| R10 | Answer the research question with at least two interpreted plots | Section 5 | Both figures visually inspected and embedded in saved notebook; two sentences per interpretation | Verified |
| R11 | Reflection/next steps in 2–4 sentences | Section 5.2 | Three sentences, limitations and next steps included | Verified |
| R12 | Public `Udacity_MS_Real_World_Data_Wrangling` repository | GitHub | Repository created; exact-commit and clean-checkout verification required before handoff | Publication verification pending |

Sequence: validate source metadata and genuine issues; write focused cleaning tests; implement transparent reusable transformations; populate all starter sections; gather and preserve real data; execute the notebook; inspect outputs and plots; run rubric and evidence checks from a clean checkout; publish the reviewed revision. No fabricated data defects or mock analysis results will be used.
