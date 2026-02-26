# Memo — Q2 Track A v3 positive sentinel5 (2026-02-25)

## Bounded increment completed
Executed one fixed-seed positive-control sentinel under unchanged Track A guardrails (v2-tight frozen; v3 diagnostic-only):

```bash
python nl_quartic_line_sampling.py --mode positive-control --seed 2026031914 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19
```

Log:
- `run-q2-trackA-positive-v3weierstrass-sentinel5-seed-2026031914.txt`

## Key readout (heuristic only)
- explicit Weierstrass fixtures (`a=-1,b=0`, `a=-2,b=3`) each had `elliptic_template_hits=1`
- all other listed non-Weierstrass entries had `elliptic_template_hits=0`

## Conservative interpretation
- Reproduces the same directional v3 positive-bank sensitivity pattern seen in prior sentinels.
- Supports continued diagnostic-only v3 use under unchanged guardrails.
- v2-tight remains frozen baseline; no theorem-level or NL-membership claims are made.

## Documentation updated
- `q2-definitive-summary.md` (added sentinel5 positive row)
- `results-q2-trackA-validation.md` (added v3 positive sentinel5 section)
