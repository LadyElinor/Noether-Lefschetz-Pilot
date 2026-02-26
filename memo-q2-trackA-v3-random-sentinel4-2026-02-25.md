# Memo — Q2 Track A v3 random sentinel4 (2026-02-25)

## Bounded increment completed
Executed one fixed-seed random sentinel under unchanged Track A guardrails (v2-tight frozen; v3 diagnostic-only):

```bash
python nl_quartic_line_sampling.py --mode random --samples 200 --seed 2026031712 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 100 --smooth-primes 5,7
```

Log:
- `run-q2-trackA-random-v3weierstrass-sentinel4-seed-2026031712.txt`

## Key readout (heuristic only)
- `smoothness_screen_pass=165/200`
- `line_detected=2/165`
- `conic_template_detected=0/165`
- `elliptic_template_detected=0/165`
- `elliptic_v2_surrogate_detected=0/165`
- `elliptic_v3_quadric_detected=0/165`

## Conservative interpretation
- Elliptic channels remained clean in this rotated-seed random sentinel.
- Low-rate random line-channel hits persist and remain treated as finite-screen heuristic incidents.
- No theorem-level claims inferred; no Picard-rank or Noether–Lefschetz membership conclusions.

## Documentation updated
- `q2-definitive-summary.md` (added sentinel4 random block row)
- `results-q2-trackA-validation.md` (added v3 random sentinel4 validation section)
