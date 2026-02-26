# Memo — Q2 Track A bounded increment (paired post-fix perturbation sentinel)

## Objective
Complete the pending paired post-fix perturbation sentinel under unchanged v3 diagnostic guardrails, while keeping v2-tight baseline frozen.

## Command (fixed-seed, reproducible)
```powershell
python nl_quartic_line_sampling.py --mode perturbation --perturb-trials 200 --seed 2026031211 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-v3weierstrass-sentinel2-seed-2026031211.txt
```

## Result
- `perturbed_smooth_pass=160/200`
- `perturbed_line_detected=0/160`, incidents `0`
- `perturbed_conic_template_detected=0/160`, incidents `0`
- `perturbed_elliptic_template_detected=0/160`, incidents `0`
- `perturbed_elliptic_v2_surrogate_detected=0/160`, incidents `0`

## Conservative readout
- Paired post-fix perturbation sentinel remained clean in this finite run.
- Two-channel post-fix negative-control coverage is now re-established (random sentinel2 + perturbation sentinel2).
- v3 remains diagnostic-only; v2-tight remains frozen baseline.

## Not claimed
- No Picard-rank certification.
- No Noether–Lefschetz membership certification.
- No claim that surrogate template hits/counters certify geometric containment.
