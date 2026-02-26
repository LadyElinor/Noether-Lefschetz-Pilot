# Memo — Q2 Track A v3 random sentinel5 (2026-02-25)

## Bounded increment completed
Executed one rotated fixed-seed random sentinel under unchanged Track A guardrails (v2-tight frozen; v3 diagnostic-only):

```bash
python nl_quartic_line_sampling.py --mode random --seed 2026032012 --samples 200 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19
```

Log:
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`

## Key readout (heuristic only)
- `smoothness_screen_pass=161/200`
- `random_samples_with_any_detected_line=0/161`
- `random_samples_with_any_detected_conic_template=0/161`
- `random_samples_with_any_detected_elliptic_template=0/161`
- `random_samples_with_any_detected_elliptic_v2_surrogate=0/161`
- `random_samples_with_any_detected_elliptic_v3_quadric=0/161`

## Conservative interpretation
- This bounded random sentinel remained clean across tracked elliptic channels under unchanged guardrails.
- The sparse line-channel incidents seen in random sentinel4 did not recur in this run.
- Supports continued diagnostic-only v3 monitoring with v2-tight retained as frozen baseline; no theorem-level or NL-membership claims are made.

## Documentation updated
- `q2-definitive-summary.md` (added random sentinel5 row)
- `results-q2-trackA-validation.md` (added v3 random sentinel5 section)
