# Pilot Status

This file is the compact status spine for `noether-lefschetz-pilot`.

## Current high-level state
- Project type: finite-scan heuristic pilot for quartic surfaces in `P^3`
- Claim posture: non-certifying screening only
- Forbidden inferences: Picard-rank claims, full smoothness certification, Noether-Lefschetz membership claims

## Canonical current surfaces
- `README.md` — operational scope and command-level orientation
- `reproducibility-manifest-v3-frozen.md` — frozen profile and acceptance gates
- `q2-definitive-summary.md` — compact canonical results spine for Track A
- `pilot-index.md` — file map and reading order

## Frozen state
### v3 frozen baseline
Canonical file:
- `reproducibility-manifest-v3-frozen.md`

Meaning:
- accepted for WP3/WP4 reporting
- immutable for reporting purposes
- detector/threshold/template changes after this point belong in experimental surfaces, not retroactive reinterpretation

Associated frozen surface:
- `releases/v3-frozen-2026-02-26/`

## Experimental state
### v4 experimental
Canonical marker:
- `v4-experimental/README.md`

Use this for:
- detector changes after the v3 freeze
- threshold changes
- new template families
- model/knob experiments not yet admitted into the frozen reporting surface

## Raw evidence layer
These are evidence artifacts rather than orientation files:
- `run-*.txt`
- `batch_*`
- `validation_*`
- `results-*.md`
- `memo-*.md`

They matter, but they should be interpreted through the canonical current/frozen surfaces above.

## Recommended current reading order
1. `README.md`
2. `pilot-index.md`
3. `reproducibility-manifest-v3-frozen.md`
4. `q2-definitive-summary.md`
5. relevant `results-*` or `memo-*` artifacts only as needed

## Current interpretation rule
If a statement seems stronger than the README boundaries or stronger than the frozen manifest allows, the stronger reading should be rejected unless a newer explicitly named experimental surface supersedes it.
