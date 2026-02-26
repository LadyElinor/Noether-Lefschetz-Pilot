# Memo — Q2 Track A v3 spillover gate hardening (larger fixed-seed repeat)

## Objective
Execute one bounded increment: repeat the v3-weierstrass spillover gate at larger finite budget while keeping the v2-tight baseline frozen.

## Commands (fixed-seed, reproducible)
```powershell
python nl_quartic_line_sampling.py --mode random --samples 240 --seed 2026031012 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-v3weierstrass-large-seed-2026031012.txt

python nl_quartic_line_sampling.py --mode perturbation --seed 2026031011 --perturb-trials 240 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-v3weierstrass-large-seed-2026031011.txt
```

## Results
- Random gate repeat: `smooth_pass=186/240`, `elliptic_template_detected=0/186`, incidents `0`
- Van-Luijk perturbation repeat: `smooth_pass=186/240`, `elliptic_template_detected=0/186`, incidents `0`

## Conservative readout
- Larger finite repeat remained clean for both negative-control channels.
- This supports continued **diagnostic-only** use of v3-weierstrass under guardrails.
- v2-tight remains frozen as the baseline profile.

## Not claimed
- No Picard-rank certification.
- No Noether–Lefschetz membership certification.
- No claim that v3 hits/non-hits certify elliptic-curve containment.
