# CABP — Conservation Admissibility Before Preference

Open-data and reproducibility repository for the manuscript:

**Conservation Admissibility Before Preference: A Value-Constrained Decision Framework for Adaptive Reuse of Industrial Heritage Buildings**

## Repository status — IMPORTANT

This repository currently contains a **synthetic / placeholder reproducibility scaffold** prepared from the numerical structure reported in the manuscript draft. It is intended to support transparent development of the controlled synthetic decision fixture and to provide the exact file schema for later replacement of any empirical/reference-project inputs.

**Do not describe the current 36-project scaffold as observed or completed real-world projects.** If the manuscript continues to describe the 36-project reference set as an empirical calibration source, those records must be replaced by the actual project-level data before the repository is cited as the final open dataset.

The focal Stage-I/Stage-II decision fixture is intentionally synthetic in the manuscript and can therefore legitimately be archived as synthetic study material, provided that this is stated consistently in the article.

## Contents

- `data/stage1_admissibility.csv` — five alternatives and Stage-I gate values/statuses.
- `metadata/stage1_rules.csv` — threshold, direction, and evidence-role definitions for G1–G5.
- `data/stage2_performance_matrix.csv` — criterion-level P1–P4 synthetic performance matrix.
- `metadata/criteria_dictionary.csv` — definitions, directions, units, and evidence-source roles for HC1–EE3.
- `data/bwm_weights.csv` — primary BWM vector used by the draft-consistent TOPSIS fixture.
- `data/comparator_weights_draft.csv` — draft-consistent weight vectors for BWM, CRITIC-reference, geometric BWM×CRITIC, entropy-reference, and equal-weight comparisons.
- `data/reference_projects_36_synthetic.csv` — clearly labelled synthetic 36-row reference-data scaffold; replace with the real reference-project matrix if empirical claims are retained.
- `derived/topsis_draft_results.csv` — draft-reported TOPSIS closeness values and orders.
- `derived/robustness_draft_summary.csv` — draft-reported sensitivity/robustness summary values.
- `analysis/reproduce_primary.py` — reproduces the primary BWM-TOPSIS and equal-weight TOPSIS calculations from the focal synthetic fixture.
- `NOTICE_SYNTHETIC.md` — data-status and replacement requirements.
- `LICENSE-DATA.md` — CC0 1.0 data dedication.

## Internal consistency of the focal fixture

The current focal Stage-II matrix is constructed so that:

- Table 3 dimension means round to the manuscript values.
- Primary BWM-TOPSIS closeness values round to **P1 0.3660, P2 0.5984, P3 0.8224, P4 0.4849**.
- Equal-weight TOPSIS closeness values round to **P1 0.3503, P2 0.5729, P3 0.8047, P4 0.5196**.
- The primary order is **P3 > P2 > P4 > P1**.

The comparator/reference and robustness files preserve values currently reported in the draft for manuscript-audit purposes. They must be regenerated from the final reference dataset before final archival release.

## Open-data release workflow

For journal submission, use a versioned archival release with a persistent identifier. A practical workflow is:

1. Replace all placeholder/reference-project data that are claimed as empirical.
2. Regenerate all derived weights, rankings, sensitivity outputs, tables, and figure-source values from the final data.
3. Create a tagged GitHub release.
4. Archive that release in a DOI-minting repository such as Zenodo.
5. Use the resulting DOI and repository landing page in the manuscript Data Availability statement.

GitHub is useful for version control, but a GitHub URL alone is not a persistent identifier such as a DOI.

## Licence

Unless a file states otherwise, the data and tabular materials in this repository are dedicated to the public domain under **CC0 1.0 Universal**. See `LICENSE-DATA.md`.

## Citation status

**Current status: development / synthetic scaffold.** Do not cite this development snapshot as the final empirical data archive until the reference-project inputs and all derived outputs have been finalized.
