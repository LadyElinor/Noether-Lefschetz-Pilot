# van-Luijk-style Perturbation Results (Proxy Family, 2026-02-23)

## Command (exact)
```bash
python nl_quartic_line_sampling.py --mode perturbation --perturb-trials 220 --perturb-noise-bound 1 --seed 202602233 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --smooth-points-per-prime 120 --smooth-primes 5,7 > run-perturbation-seed-202602233.txt
```

## Important scope statement
- The exact van Luijk published quartic polynomial is **not** included locally in this pilot.
- Therefore this is explicitly a **proxy/placeholder family** test.
- We do **not** claim this baseline is van Luijk’s exact example.

## Proxy setup and results
- Candidate line bank: `257`
- Baseline label: `proxy_baseline_not_van_luijk_exact`
- Baseline smoothness screen: `pass` (heuristic)
- Baseline detected lines in current bank: `0`

Perturbations (integer noise in `[-1,1]` on coefficients):
- smooth-pass: `184/220 = 0.8364`
- line-detected among analyzed: `3/184 = 0.0163`
- total detected line incidents: `6`

## Conservative interpretation
- This is a local stability probe for one proxy family under small coefficient perturbations.
- Results are finite-scan heuristic signals only, not evidence about Picard rank or the actual van Luijk model.
