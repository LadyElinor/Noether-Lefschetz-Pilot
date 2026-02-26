# Expanded Pilot Results (2026-02-23)

## Exact command lines used
```bash
python nl_quartic_line_sampling.py --samples 300 --seed 20260223 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --smooth-points-per-prime 120 --smooth-primes 5,7 --include-determinantal > run-expanded-seed-20260223.txt

python nl_quartic_line_sampling.py --samples 220 --seed 20260224 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --smooth-points-per-prime 120 --smooth-primes 5,7 --include-determinantal > run-expanded-seed-20260224.txt
```

## Configuration summary
- Quartic monomials: 35
- Candidate line bank size: 258 (seed 20260223 run), 260 (seed 20260224 run)
- Smoothness heuristic: sampled points over primes 5 and 7 (120 points/prime)
- Coefficient sampling window: `[-2,2]`

## Run A (seed=20260223, samples=300)
- smoothness_screen_pass: 247
- smoothness_screen_flagged: 53
- random_samples_analyzed_for_lines: 247
- random_samples_with_any_detected_line: 1/247
- total_detected_line_incidents: 1

Special-bank highlights:
- engineered forced-line: line_hits=11, smoothness heuristic flagged
- forced-conic: line_hits=1, conic containment test = yes, smoothness heuristic flagged
- Fermat quartic: line_hits=0, smoothness heuristic pass
- optional determinantal-style: line_hits=7, smoothness heuristic flagged

## Run B (seed=20260224, samples=220)
- smoothness_screen_pass: 194
- smoothness_screen_flagged: 26
- random_samples_analyzed_for_lines: 194
- random_samples_with_any_detected_line: 3/194
- total_detected_line_incidents: 6

Special-bank highlights:
- engineered forced-line: line_hits=17, smoothness heuristic flagged
- forced-conic: line_hits=3, conic containment test = yes, smoothness heuristic flagged
- Fermat quartic: line_hits=0, smoothness heuristic pass
- optional determinantal-style: line_hits=6, smoothness heuristic flagged

## Conservative interpretation
- The expanded scan finds occasional line-incidence positives among random quartics after the smoothness-screen pass.
- Positive hits are **finite-bank incidence detections only**.
- Negative hits are **not** evidence of generic Picard rank.
- Smoothness results are **heuristic flags/passes**, not discriminant-level certification.
