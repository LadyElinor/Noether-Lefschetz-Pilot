# Memo — Q2 Track A v2 implementation + calibration (2026-02-24)

## Implemented
In `nl_quartic_line_sampling.py`:
- Added `--elliptic-probe-mode` with choices:
  - `v1-template` (default)
  - `v2-resultant`
- Added v2 surrogate pathway in `elliptic_template_contained(...)`:
  - restriction polynomial generation,
  - derivative map,
  - finite-field repeated-root proxy checks,
  - stricter threshold than initial draft.
- Added v2 summary fields:
  - `*_elliptic_v2_surrogate_*` in random/stratified/perturbation summaries.

## Runs executed (v2)
- `run-q2-trackA-random-v2-seed-2026030212.txt`
- `run-q2-trackA-positive-v2-seed-2026030213.txt`
- `run-q2-trackA-pert-v2-seed-2026030211.txt`

## Key outcomes
- Random analyzed block produced non-zero v2 incidents (`8/61`, incidents `9`).
- Positive bank produced mixed non-zero v2 incidents on some specials.
- Van-Luijk perturbation analyzed block produced non-zero v2 incidents (`5/78`, incidents `5`).

## Interpretation
- v2 surrogate is operational and deterministic but currently too permissive for clean negative-control separation.
- Treat as calibration stage only.
- No geometric claim (elliptic-curve existence, Picard rank, NL membership) is supported by these v2 hits.

## Next tuning targets
- Strengthen degeneracy rejection.
- Increase cross-prime consistency requirement.
- Add explicit exclusion checks against simple collapse channels before counting v2 hits.
