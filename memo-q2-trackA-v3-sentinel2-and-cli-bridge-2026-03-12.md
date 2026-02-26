# Memo — Q2 Track A bounded increment (v3 sentinel + CLI bridge fix)

## Objective
Keep v2-tight baseline frozen and execute one conservative v3 diagnostic increment with fixed-seed reproducibility.

## Block actions
1. **Unblocked runner wiring** in `nl_quartic_line_sampling.py`:
   - forwarded `max_quadric_templates`, `v3_prime_sample`, `v3_min_points` from CLI `main()` into all run paths (`run`, `run_stratified`, `run_positive_control`, `run_perturbation`).
2. **Executed one bounded v3 diagnostic** (random sentinel, fixed seed).

## Command (fixed-seed, reproducible)
```powershell
python nl_quartic_line_sampling.py --mode random --samples 200 --seed 2026031212 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-v3weierstrass-sentinel2-seed-2026031212.txt
```

## Result
- Random sentinel (post-fix): `smooth_pass=155/200`, `elliptic_template_detected=0/155`, incidents `0`.

## Conservative readout
- CLI execution path is operational again for v3-capable runs with explicit guardrail args.
- This finite sentinel remained clean; treat as operational validation only.
- v2-tight remains frozen baseline.

## Not claimed
- No Picard-rank certification.
- No Noether–Lefschetz membership certification.
- No claim that heuristic elliptic-template counts certify elliptic-curve containment.
