# Memo — Q2 Track A v2 tightening loop (2026-02-25)

## Objective
Reduce v2 surrogate false-positive pressure in random and van-Luijk negative-control regions while retaining at least limited positive-bank sensitivity.

## Code changes
In `nl_quartic_line_sampling.py`:
- Added tunable v2 knobs:
  - `--elliptic-v2-cross-prime-count` (default 2)
  - `--elliptic-v2-min-rootcount` (default 2)
- Threaded both knobs through random/stratified/positive/perturbation paths.
- v2 predicate now uses these thresholds in repeated-root cross-prime checks.

## Calibration rerun (same seeds, tightened params)
Tightened parameters used:
- `--elliptic-v2-cross-prime-count 3`
- `--elliptic-v2-min-rootcount 3`

Logs:
- `run-q2-trackA-random-v2tight-seed-2026030212.txt`
- `run-q2-trackA-positive-v2tight-seed-2026030213.txt`
- `run-q2-trackA-pert-v2tight-seed-2026030211.txt`

## Before/after snapshot
- Random block (`2026030212`):
  - before: `8/61`, incidents `9`
  - after: `0/61`, incidents `0`
- Van-Luijk perturbation block (`2026030211`):
  - before: `5/78`, incidents `5`
  - after: `0/78`, incidents `0`
- Positive bank (`2026030213`):
  - before: mixed non-zero across some specials
  - after: reduced, but engineered line special retained non-zero elliptic-template hits

## Interpretation
- Tightening materially improved negative-control cleanliness in this calibration batch.
- Positive-bank sensitivity is reduced but not eliminated.
- v2 remains a heuristic surrogate only; no geometric certification or NL/Picard inference is supported.

## Next
- Run larger-batch stability check under tightened settings.
- Expand elliptic-specific positive constructions to avoid overfitting to legacy special families.
