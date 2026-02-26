# Results — Coverage Extension (Day 4)

Date: 2026-02-23

## Chosen extension
Expanded **conic template bank diagnostics** with one representative positive-control run (heuristic only).

## Command
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode positive-control --seed 2026022644 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 128 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 --include-determinantal | Tee-Object -FilePath noether-lefschetz-pilot/run-coverage-extension-conic-bank-seed-2026022644.txt
```

## Key outputs
- candidate lines: `256`
- candidate conic templates: `128`
- engineered_xG3_plus_yH3: `line_hits=15`, `conic_template_hits=1`
- forced_conic_(xz-y^2)Q2+wR3: `line_hits=2`, `conic_template_hits=2`
- fermat_x4+y4+z4+w4_literature_known_special: `line_hits=0`, `conic_template_hits=0`
- determinantal_style_proxy_2x2_quadric_det: `line_hits=4`, `conic_template_hits=0`

## Conservative interpretation
- This run is a scanner-sensitivity diagnostic on tagged special families, not a generic-family incidence estimate.
- Smoothness statuses come from sampled modular checks and remain heuristic.
- No claim is made here about Picard rank or Noether–Lefschetz membership.
