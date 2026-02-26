# Memo — Q2 Track A bounded increment (v3 random sentinel3)

## Objective
Execute one bounded, fixed-seed v3 random sentinel increment after the latest positive sentinel while keeping v2-tight baseline frozen and theorem-vs-heuristic boundaries explicit.

## Command (reproducible)
```powershell
python nl_quartic_line_sampling.py --mode random --samples 200 --seed 2026031412 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-v3weierstrass-sentinel3-seed-2026031412.txt
```

## Result snapshot
- `random_total_samples=200`
- `smoothness_screen_pass=158`
- `random_samples_with_any_detected_elliptic_template=0/158`
- `random_samples_with_any_detected_elliptic_v2_surrogate=0/158`
- `random_samples_with_any_detected_elliptic_v3_quadric=0/158`

## Conservative readout
- In this bounded rotated-seed pass, the random negative-control channel remained clean on tracked elliptic detections under unchanged v3 guardrails.
- This is finite heuristic operational evidence only.
- v2-tight remains the frozen baseline profile.

## Not claimed
- No Picard-rank claim.
- No Noether–Lefschetz membership claim.
- No claim that zero incidents certify genericity or smoothness.
