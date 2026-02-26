# Memo — Q2 Track A determinism micro-pass (2026-02-25)

## Objective
Execute one concrete hardening validation step for Track A: same-seed rerun determinism check under the current conservative v3 diagnostic guardrails.

## Runs
- `run-q2-trackA-determinism-random-seed-2026022516-pass1.txt`
- `run-q2-trackA-determinism-random-seed-2026022516-pass2.txt`

Command profile (both passes):
- `--mode random --samples 120 --seed 2026022516`
- `--coeff-bound 2 --point-bound 1`
- `--max-deterministic-lines 180 --random-line-probes 80`
- `--max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20`
- `--elliptic-probe-mode v3-weierstrass`
- `--elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3`
- `--v3-prime-sample 31 --v3-min-points 15`
- `--smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19`

## Readout (pass1 vs pass2)
- Exact match on tracked summary counters.
- `smoothness_screen_pass=100/120`, `smoothness_screen_flagged=20/120`
- analyzed random samples: `100`
- line/conic/elliptic(v1,v2,v3) detected-sample rates all `0/100`
- total line/conic/elliptic(v1,v2,v3) incident counters all `0`

## Conservative interpretation
- This bounded rerun supports operational determinism for the current random-mode pipeline under fixed seed + fixed parameters.
- Treated strictly as implementation hardening evidence; no geometric certification or NL/Picard inference is implied.
