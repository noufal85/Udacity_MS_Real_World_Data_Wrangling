# Course submission package

The supplied assignment requires a ZIP containing the completed Jupyter Notebook and the gathered/stored datasets. A public repository is useful for source review, but does not prove this upload has occurred.

## Local artifact

The prepared file is named `Udacity_MS_Real_World_Data_Wrangling_submission.zip`, beside the repository directory. It contains one project directory with:

- The executed `Data_Wrangling_Project_Starter.ipynb` and both saved plots.
- `wrangling.py`, required by the notebook, plus the execution/authoring helpers.
- Original raw CSV/JSON snapshots, source metadata and provenance checksums.
- Cleaned datasets and the final five-column country-year CSV, with exclusion/cleaning audits.
- Dependency specifications, tests, README and rubric/validation notes.

Git history, virtual environments, caches, editor checkpoints and credentials are not included. The ZIP is created from the committed tree, not an unreviewed directory listing. It is kept outside the source repository to avoid nesting or committing generated submission packages.

## Recreate and check

Run from a clean repository after committing the reviewed files:

```bash
git archive --format=zip --prefix=Udacity_MS_Real_World_Data_Wrangling/ --output=../Udacity_MS_Real_World_Data_Wrangling_submission.zip HEAD
python -m zipfile -t ../Udacity_MS_Real_World_Data_Wrangling_submission.zip
```

Git records the source commit in the ZIP comment. At handoff the archive is checked for integrity, safe paths, a complete file allowlist and byte-for-byte agreement with the committed source. An extracted copy is tested and its notebook run from a fresh kernel using the validated project environment.

After extracting, enter the project directory and follow the README setup instructions. Cached source payloads make normal notebook reruns independent of network downloads; the local Jupyter kernel still requires permission to open its sockets.

## Remaining external step

Upload the ZIP through the course's project-submission interface and verify the confirmation there. Course UI upload rules may differ from the saved reference; follow the live interface if it imposes additional file-size or naming constraints. No upload, accepted alternative submission format, reviewer approval or grade is asserted by this repository.
