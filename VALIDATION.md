# Validation and evaluator-style review

## Evidence categories

- **Unit tests:** six deterministic tests check missing measurement/code handling, preservation of inputs, nested-field normalization, invalid-year rejection, and duplicate-key merge rejection.
- **Artifact tests:** two tests inspect saved execution, plots, hashes and final schema; nine parametrized checks require intent comments in assessment/cleaning cells; a raw-to-final reconstruction test verifies the stored CSV against the source transformations. The new comment checks failed against the reviewed baseline before the comments were added.
- **Runtime:** `python run_notebook.py` completed from a new kernel with real public data acquisition, followed by a successful cached rerun. All 26 nonempty code cells are executed. Cached execution is not presented as a fresh network download.
- **Visual inspection:** both saved PNGs were opened and checked for readable titles, labels, units, legends and unclipped content. The saved notebook explicitly embeds these PNGs; merely creating image files would not meet that gate.
- **Provenance:** exact source bytes, request URLs, UTC retrieval timestamps and SHA-256 hashes are retained. The notebook asserts raw-source immutability after cleaning and round-trips the final CSV.

## Review findings and resolutions

| Finding | Resolution and regression evidence |
|---|---|
| Non-interactive plotting backend created files but initially did not embed figures | Explicit image display embeds both PNGs; artifact test failed before correction and passes afterward |
| Missing-code counts overlap null measurements | Initial 120 missing codes disclosed; 24 overlapping nulls removed first and remaining 96 excluded separately |
| Missing values actually belong to aggregates | Narrative identifies `Not classified` and income groups, without claiming country-level gaps |
| Source aggregate codes differ | Join audit discloses unmatched keys; final scope guard removes zero rows, not a fabricated cleaning result |
| Strong income/health correlation could be overstated | Descriptive language, unbalanced coverage, noncausal limitations and preselected-country caveat retained |
| Notebook lacked literal code comments required by rubric | Added concise intent comments to source-generation, assessment and cleaning cells; nine regression cases verify their presence |
| Public source was incorrectly treated as replacing the course ZIP | Corrected requirements/README; local committed-tree ZIP is prepared and tested separately from publication; actual upload remains external |
| Missing ISO codes for aggregates may be intentional | Defined completeness relative to the analytical schema and disclosed evaluator-interpretation risk; no claim of corrupt country records |
| Cleaned data correctness was not covered by artifact regression | Added a reconstruction assertion matching all final rows and fields to the raw-source transformations |

## Reproducible acceptance commands

```bash
python -m pytest -q
python run_notebook.py
python -m pytest -q
git diff --check
```

Eighteen tests pass. The separate reusable Udacity notebook-evidence checker also passes: 26/26 executed code cells and 24 with visible results. The revised notebook is executed from a new kernel using preserved, hash-verified source snapshots; clean-checkout and extracted-package checks are performed at the final handoff. The final remote commit and visibility are verified separately, rather than embedding a self-referential commit hash here.

## Limits

No external Udacity evaluator has graded this revision. Public GitHub publication is the requested deliverable, not proof that a course submission was uploaded. Live endpoints can revise observations, so refreshed analyses require renewed narrative and result checks. The two quality issues are distinct completeness defects in different API fields; neither is manufactured, and removing irrelevant columns is not counted as a quality fix.
