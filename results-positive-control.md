# Results: Positive Control Round (2026-02-23)

## Command
```bash
python nl_quartic_line_sampling.py --mode positive-control --seed 202602252 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 100 --smooth-primes 5,7
```

## Setup snapshot
- seed: `202602252`
- candidate lines: `259`
- conic templates scanned: `64`
- smoothness screen: sampled points over primes 5,7 (heuristic only)

## Control-family labels
- `POS_CTRL_TRUE_FORCED_CONIC` -> `forced_conic_(xz-y^2)Q2+wR3`
- `POS_CTRL_PROXY_DETERMINANTAL` -> `determinantal_style_proxy_2x2_quadric_det`

## Key outputs
- `engineered_xG3_plus_yH3`: line_hits=12, conic_template_hits=0, smoothness_screen=flag
- `forced_conic_(xz-y^2)Q2+wR3`: line_hits=2, conic_template_hits=1, smoothness_screen=flag
- `fermat_x4+y4+z4+w4_literature_known_special`: line_hits=0, conic_template_hits=0, smoothness_screen=pass
- `determinantal_style_proxy_2x2_quadric_det`: line_hits=8, conic_template_hits=0, smoothness_screen=flag, structural_marker=`determinantal_proxy_marker`

## Interpretation boundary
- This validates that scanner signals fire on tagged special constructions (line hits and/or marker).
- Determinantal entry is explicitly a **proxy family**, not claimed canonical literature normal form.
- No Picard-rank or NL-membership claim is made.
