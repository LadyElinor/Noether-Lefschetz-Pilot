# Reproducibility Manifest — v3-frozen
Date: 2026-02-26
Project: Noether-Lefschetz Pilot (v3-Weierstrass frozen)

## Frozen profile
- mode: random / positive-control / perturbation
- elliptic-probe-mode: v3-weierstrass
- max-quadric-templates: 20
- max-elliptic-templates: 30
- v3-prime-sample: 31
- v3-min-points: 15

## Acceptance gates (pre-freeze)
1) Positive acceptance
   command: python nl_quartic_line_sampling.py --mode positive-control --seed 2026031914 --elliptic-probe-mode v3-weierstrass --max-quadric-templates 20 --output-json > validation_pos_audit.log 2>&1
   expected/readout: gate_positive_hits=2, gate_positive_total=2, gate_positive_pass=1

2) Guardrail acceptance
   command: python nl_quartic_line_sampling.py --mode perturbation --perturbation-baseline van_luijk_exact_2007 --perturb-trials 500 --seed 2026031915 --elliptic-probe-mode v3-weierstrass --max-quadric-templates 20 --output-json > validation_neg_audit.log 2>&1
   expected/readout: gate_guardrail_fp_hits=0, gate_guardrail_fp_rate=0.0, gate_guardrail_pass=1

## Mapping runs
- Batch-S command family seed: 202603201
  analyzed_n: 421
  elliptic_hits_k: 0
  upper95_wilson: ~0.0090
  artifacts: batch_s_results.json, batch_s_run.log

- Batch-M command family seed: 202603202
  analyzed_n: 1985
  elliptic_hits_k: 0
  upper95_wilson: ~0.0019
  artifacts: batch_m_transcript.log

- Batch-L command:
  python nl_quartic_line_sampling.py --mode random --samples 10000 --seed 202603203 --elliptic-probe-mode v3-weierstrass --max-quadric-templates 20 --max-elliptic-templates 30 --v3-prime-sample 31 --v3-min-points 15 --smooth-primes 5,7,11,13,17 --smooth-points-per-prime 160 --output-json > batch_l_transcript.log 2>&1
  analyzed_n: 7978
  elliptic_hits_k: 0
  line_hit_samples: 24
  conic_hit_samples: 4
  upper95_wilson: ~0.00048

## Freeze policy
- This release is immutable for WP3/WP4 reporting.
- Any new detector/threshold/template changes must be labeled v4-experimental.
