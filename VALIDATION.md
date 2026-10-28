# Validation and evaluator-style review

## Evidence categories

- **Unit tests:** six deterministic tests check missing measurement/code handling, preservation of inputs, nested-field normalization, invalid-year rejection, and duplicate-key merge rejection.
- **Artifact tests:** two tests inspect the actual saved notebook and raw/final data. They require execution counts, no error outputs, embedded PNG output in each of the two plot cells, no assignment placeholders, valid raw hashes, sample sizes, complete final fields and unique country-year keys.
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

## Reproducible acceptance commands

```bash
python -m pytest -q
python run_notebook.py
python -m pytest -q
git diff --check
```

Eight tests pass. The separate reusable Udacity notebook-evidence checker also passes: 26/26 executed code cells and 24 with visible results. A local clone of the committed project passed all eight tests before and after a fresh-kernel cached execution, using the validated project interpreter. The final remote commit and visibility are verified separately in the handoff, rather than embedding a self-referential commit hash here.

## Limits

No external Udacity evaluator has graded this revision. Public GitHub publication is the requested deliverable, not proof that a course submission was uploaded. Live endpoints can revise observations, so refreshed analyses require renewed narrative and result checks. The two quality issues are distinct completeness defects in different API fields; neither is manufactured, and removing irrelevant columns is not counted as a quality fix.
