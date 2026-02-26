# Memo — Q2 Track A v3 spillover sentinel (rotated fixed seed)

## Objective
Execute one bounded increment: run a rotated-seed v3 spillover sentinel while keeping the v2-tight baseline frozen.

## Commands (fixed-seed, reproducible)
```powershell
python nl_quartic_line_sampling.py --mode random --samples 200 --seed 2026031112 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-v3weierstrass-sentinel-seed-2026031112.txt

python nl_quartic_line_sampling.py --mode perturbation --seed 2026031111 --perturb-trials 200 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-v3weierstrass-sentinel-seed-2026031111.txt
```

## Results
- Random sentinel: `smooth_pass=168/200`, `elliptic_template_detected=0/168`, incidents `0`
- Van-Luijk perturbation sentinel: `smooth_pass=155/200`, `elliptic_template_detected=0/155`, incidents `0`

## Conservative readout
- Rotated-seed sentinel remained clean in both negative-control channels for this finite pass.
- This supports continued diagnostic-only use of v3-weierstrass under current guardrails.
- v2-tight remains frozen as the baseline profile.

## Not claimed
- No Picard-rank certification.
- No Noether–Lefschetz membership certification.
- No claim that heuristic elliptic-template counts certify elliptic-curve containment.
