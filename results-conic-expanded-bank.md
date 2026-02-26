# Results: Random Run with Expanded Conic Bank (2026-02-23)

## Command
```bash
python nl_quartic_line_sampling.py --mode random --samples 220 --seed 202602251 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 100 --smooth-primes 5,7
```

## Setup snapshot
- seed: `202602251`
- random samples: `220`
- candidate lines: `257`
- conic template bank size: `64` (expanded deterministic bank)

## Aggregate output
- smoothness_screen_pass: `176`
- smoothness_screen_flagged: `44`
- analyzed after smoothness screen: `176`
- random_samples_with_any_detected_line: `0/176`
- random_samples_with_any_detected_conic_template: `0/176`
- total_detected_line_incidents: `0`
- total_detected_conic_template_incidents: `0`

## Notes
- Special-bank checks in same run still show expected hits for engineered controls.
- This random batch produced no line/conic-template detections under the finite bank.
- Non-detection is not evidence of NL-genericity, smoothness proof, or Picard-rank behavior.
