# Large Random Batch Results (2026-02-23)

## Command (exact)
```bash
python nl_quartic_line_sampling.py --mode random --samples 1000 --seed 202602231 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --smooth-points-per-prime 120 --smooth-primes 5,7 --include-determinantal > run-large-seed-202602231.txt
```

## Summary
- Target met: **1000** random quartics (no resume needed).
- Candidate line bank: 257
- Smoothness screen config: primes 5,7 with 120 sampled projective points each

### Reported counts
- `random_total_samples=1000`
- `smoothness_screen_pass=829`
- `smoothness_screen_flagged=171`
- `random_samples_analyzed_for_lines=829`
- `random_samples_with_any_detected_line=3/829`
- `total_detected_line_incidents=6`

### Derived rates
- Smooth-pass rate: `829/1000 = 0.8290`
- Line-detection rate among smooth-pass samples: `3/829 ≈ 0.0036`

## Conservative interpretation
- This is a finite-bank incidence scan + sampled mod-p smoothness heuristic.
- Positive detections are **special-incidence candidates under this scan only**.
- Non-detection is **not** evidence for generic Picard rank, NL-genericity, or global smoothness.
