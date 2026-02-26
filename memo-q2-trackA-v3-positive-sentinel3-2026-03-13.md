# Memo — Q2 Track A bounded increment (v3 positive sentinel3)

## Objective
Execute one bounded, fixed-seed v3 diagnostic increment while preserving strict theorem-vs-heuristic boundaries and keeping v2-tight frozen.

## Command (reproducible)
```powershell
python nl_quartic_line_sampling.py --mode positive-control --seed 2026031314 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --include-determinantal | Tee-Object -FilePath run-q2-trackA-positive-v3weierstrass-sentinel3-seed-2026031314.txt
```

## Result snapshot
- Explicit Weierstrass fixtures remained directionally active:
  - `explicit_elliptic_weierstrass_plane_a-1_b0_L1111`: `elliptic_template_hits=1`
  - `explicit_elliptic_weierstrass_plane_a-2_b3_L1111`: `elliptic_template_hits=1`
- Other listed positive-bank entries stayed at `elliptic_template_hits=0` in this run.

## Conservative readout
- This fixed-seed sentinel reproduces prior directional v3 positive-bank sensitivity without broad activation.
- Treat strictly as finite heuristic diagnostics.
- v2-tight remains the frozen baseline profile.

## Not claimed
- No Picard-rank claim.
- No Noether–Lefschetz membership claim.
- No claim that template hits certify elliptic-curve containment.
