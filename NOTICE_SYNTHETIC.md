# Synthetic-data notice

This repository is a development scaffold for the CABP manuscript.

## What is legitimately synthetic

The manuscript explicitly describes the focal five-alternative decision exercise as a **controlled synthetic decision fixture**. The Stage-I and Stage-II files in this repository are therefore synthetic study materials, not measurements from a completed building project.

## What must not be misrepresented

The file `data/reference_projects_36_synthetic.csv` contains synthetic placeholder rows identified as `SYN_R01`–`SYN_R36`. These rows are **not observed completed projects**.

If the article states that the 36-project reference set is empirical, completed, observed, case-derived, or otherwise based on real projects, the synthetic file must be replaced with the genuine project-level matrix and its provenance documentation before submission of the final open-data archive.

## Derived draft values

Some files under `derived/` preserve numerical values currently stated in the manuscript so that discrepancies can be audited during revision. Values marked `DRAFT_REPORTED_REGENERATE` are not certified as outputs of the current placeholder 36-project reference matrix.

Before a final DOI-bearing release:
1. replace all empirical placeholders;
2. rerun CRITIC, entropy, geometric weighting, VIKOR, bootstrap, leave-one-out, candidate-removal, external-anchor, and uncertainty analyses;
3. regenerate all tables and figures from those outputs;
4. verify every manuscript number against the archived files.

This notice should remain in the development repository even after replacement so the version history is transparent.
