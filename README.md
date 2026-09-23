# CABP — Conservation Admissibility Before Preference

Open-data and reproducibility repository for the manuscript:

**Conservation Admissibility Before Preference: A Value-Constrained Decision Framework for Adaptive Reuse of Industrial Heritage Buildings**

## Repository status — IMPORTANT

This repository contains a **synthetic / placeholder reproducibility scaffold** prepared from the numerical structure reported in the manuscript draft. The focal five-alternative decision exercise is explicitly synthetic in the manuscript.

The 36-row reference matrix is also currently synthetic and is labelled `SYN_R01`–`SYN_R36`. It is constructed so that the current CRITIC, entropy, geometric BWM×CRITIC and TOPSIS comparator results can be reproduced from the archived files. **It must not be described as observed completed real-world projects.** If the manuscript retains an empirical 36-project calibration claim, replace these rows with the genuine project-level data and regenerate all dependent outputs before the final DOI-bearing release.

## Contents

- `data/stage1_admissibility.csv` — five alternatives and Stage-I gate values/statuses.
- `metadata/stage1_rules.csv` — threshold, direction, and evidence-role definitions for G1–G5.
- `data/stage2_performance_matrix.csv` — criterion-level P1–P4 synthetic performance matrix.
- `metadata/criteria_dictionary.csv` — definitions, directions, units, and evidence-source roles for HC1–EE3.
- `data/bwm_weights.csv` — primary BWM vector.
- `data/comparator_weights_draft.csv` — BWM, CRITIC-reference, geometric BWM×CRITIC, entropy-reference, and equal-weight vectors.
- `data/reference_projects_36_synthetic.csv` — synthetic 36-row reference matrix.
- `derived/dimension_profiles.csv` — values behind Table 3 dimension summaries.
- `derived/topsis_draft_results.csv` — values behind Table 4 TOPSIS results.
- `derived/vikor_draft_orders.csv` — VIKOR orders currently reported in the draft.
- `derived/robustness_draft_summary.csv` — sensitivity/robustness result register.
- `analysis/reproduce_primary.py` — reproduces primary BWM-TOPSIS and equal-weight TOPSIS.
- `analysis/reproduce_reference_and_table4.py` — derives CRITIC/entropy reference weights, geometric BWM×CRITIC weights, and reproduces all four Table 4 TOPSIS rows.
- `NOTICE_SYNTHETIC.md` — data-status and replacement requirements.
- `LICENSE-DATA.md` — CC0 1.0 data dedication.

## Internal numerical consistency

The current synthetic fixture is constructed so that:

- Table 3 dimension means round to the manuscript values.
- BWM-TOPSIS closeness values reproduce **P1 0.3660, P2 0.5984, P3 0.8224, P4 0.4849**.
- Geometric BWM×CRITIC (lambda=.5) reproduces **0.3665, 0.5710, 0.8038, 0.5049**.
- Entropy-reference weighting reproduces **0.2360, 0.5093, 0.8215, 0.5597**.
- Equal-weight TOPSIS reproduces **0.3503, 0.5729, 0.8047, 0.5196**.
- The primary order is **P3 > P2 > P4 > P1**.

The robustness register retains the manuscript-draft targets for the 2,000 bootstrap, 36 leave-one-out, parameter sweeps, candidate removal, external anchors and 5,000 uncertainty perturbations. These result-level targets should be regenerated from the final archived data before publication if any inputs are replaced.

## Open-data release workflow

For journal submission requiring a persistent identifier:

1. Finalize all data that the manuscript actually claims to analyse.
2. Regenerate all derived weights, rankings, robustness outputs, tables, and figure-source values.
3. Create a tagged GitHub release.
4. Archive that exact release in a DOI-minting repository such as Zenodo.
5. Insert the resulting DOI and repository landing page into the manuscript Data Availability statement.

A GitHub URL provides public access and version control, but it is not itself a DOI or accession number.

## Licence

Unless a file states otherwise, the data and tabular materials are dedicated to the public domain under **CC0 1.0 Universal**. See `LICENSE-DATA.md`.

## Citation status

**Current status: development / synthetic scaffold.** It is suitable for reproducing the controlled synthetic decision fixture, but it must not be used as evidence that 36 real completed projects were observed unless those rows are replaced by genuine project records.
