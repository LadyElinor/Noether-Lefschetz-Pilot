# Memo — Q2 Track A bounded increment (v3 perturbation sentinel3)

## Objective
Execute one bounded, fixed-seed v3 perturbation sentinel increment after the random sentinel3 check while keeping v2-tight baseline frozen and theorem-vs-heuristic boundaries explicit.

## Command (reproducible)
```powershell
python nl_quartic_line_sampling.py --mode perturbation --perturb-trials 200 --seed 2026031511 --perturbation-baseline van_luijk_exact_2007 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-v3weierstrass-sentinel3-seed-2026031511.txt
```

## Result snapshot
- `perturbed_smooth_pass=166/200`
- `perturbed_line_detected=0/166`
- `perturbed_conic_template_detected=0/166`
- `perturbed_elliptic_template_detected=0/166`
- `perturbed_elliptic_v2_surrogate_detected=0/166`

## Conservative readout
- In this bounded rotated-seed pass, the van-Luijk perturbation negative-control channel remained clean on tracked heuristic detections under unchanged v3 guardrails.
- This is finite heuristic operational evidence only.
- v2-tight remains the frozen baseline profile.

## Not claimed
- No Picard-rank claim.
- No Noether-Lefschetz membership claim.
- No claim that zero incidents certify generic smoothness or geometric stability.
