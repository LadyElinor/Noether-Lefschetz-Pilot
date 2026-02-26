# Stratified Results by Coefficient Bound (2026-02-23)

## Command (exact)
```bash
python nl_quartic_line_sampling.py --mode stratified --samples-per-bound 260 --stratified-bounds 1,2,3 --seed 202602232 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --smooth-points-per-prime 120 --smooth-primes 5,7 > run-stratified-seed-202602232.txt
```

## Configuration
- Bounds: `1, 2, 3`
- Samples per bound: `260`
- Candidate line bank: `258`
- Smoothness heuristic: sampled mod 5 and mod 7 points

## Reported strata
- `coeff_bound=1`, seed `202603232`:
  - smooth-pass: `212/260 = 0.8154`
  - line-detected among analyzed: `8/212 = 0.0377`
  - line incidents: `20`
- `coeff_bound=2`, seed `202604232`:
  - smooth-pass: `214/260 = 0.8231`
  - line-detected among analyzed: `0/214 = 0.0000`
  - line incidents: `0`
- `coeff_bound=3`, seed `202605232`:
  - smooth-pass: `229/260 = 0.8808`
  - line-detected among analyzed: `0/229 = 0.0000`
  - line incidents: `0`

## Conservative interpretation
- These are stratified heuristic rates under one fixed finite line bank.
- The non-monotonic line-detection behavior here should be treated as pilot-level noise, not structural evidence.
- No Picard-rank or NL-locus claims follow from these rates.
