# Memo — Expanded NL Quartic Pilot (2026-02-23)

## What was completed
1. Expanded random sampling with deterministic seed controls (runs at 300 and 220 samples).
2. Added lightweight smoothness filter heuristic (mod-p sampled singular-point screen).
3. Expanded special-case bank:
   - forced-line construction,
   - forced-conic style construction (with explicit conic-parametrization containment check),
   - Fermat quartic labeled as literature-known special example,
   - optional determinantal-style example kept as optional.
4. Improved line-incidence coverage using:
   - capped deterministic line bank from primitive point pairs,
   - randomized line probes.
5. Produced updated docs and results files.

## Evidence tiers
### Tier 1: theorem/literature-known context (not proven here)
- Fermat quartic is classically special in the literature.
- General NL/Picard-rank theory is external to this script.

### Tier 2: exact algebraic checks implemented here
- Exact integer substitution test for line containment on each candidate line.
- Exact test for the specific conic parametrization \(x=s^2, y=st, z=t^2, w=0\) in the forced-conic example.

### Tier 3: heuristic-only outputs
- Smoothness screen via sampled mod-5/mod-7 points.
- Finite candidate-line-bank incidence statistics from random sampling.

## Blockers / limitations
- No full singularity/discriminant computation.
- No projective-equivalence deduplication beyond simple canonical normalization.
- No explicit Picard-rank or transcendental lattice computation.
- Candidate bank remains finite and incomplete by design.

## Next practical steps
1. Add optional larger prime set for smoother heuristic confidence bands.
2. Add repeat-run aggregator utility across many seeds.
3. Add optional finite-field exact sweep for very small fields (still heuristic w.r.t. char 0 smoothness).
4. If moving beyond pilot: integrate CAS-backed singularity/rank routines (Sage/Magma) with strict claim boundaries.

## Files touched
- `nl_quartic_line_sampling.py`
- `README.md`
- `results-expanded.md`
- `memo-expanded-2026-02-23.md`
- run logs: `run-expanded-seed-20260223.txt`, `run-expanded-seed-20260224.txt`
