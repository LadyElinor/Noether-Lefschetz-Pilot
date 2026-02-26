# Memo — Q2 Track A bounded increment (v3 positive sentinel4)

## Objective
Run one bounded, fixed-seed v3 positive-control sentinel increment while preserving strict theorem-vs-heuristic boundaries and keeping v2-tight baseline frozen.

## Command (reproducible)
```powershell
python nl_quartic_line_sampling.py --mode positive-control --seed 2026031614 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-positive-v3weierstrass-sentinel4-seed-2026031614.txt
```

## Result snapshot
- explicit Weierstrass fixtures (`a=-1,b=0`, `a=-2,b=3`) each recorded `elliptic_template_hits=1`
- all other listed positive-bank entries remained `elliptic_template_hits=0`
- line/conic channels remained active on expected tagged special families

## Conservative readout
- This bounded rotated-seed positive sentinel reproduced the same directional v3 positive-bank pattern seen previously.
- This is finite heuristic operational evidence only.
- v2-tight remains the frozen baseline profile; v3 remains diagnostic/experimental.

## Not claimed
- No Picard-rank claim.
- No Noether-Lefschetz membership claim.
- No geometric certification from finite heuristic incidents/non-incidents.
