# Results: Conservative Perturbation Next Round (2026-02-23)

## Command
```bash
python nl_quartic_line_sampling.py --mode perturbation --seed 202602253 --perturb-trials 180 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_2007_placeholder --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 100 --smooth-primes 5,7
```

## Conservative baseline policy
- Exact van Luijk 2007 quartic polynomial is not present in project sources.
- Used `--perturbation-baseline van_luijk_2007_placeholder` (explicit placeholder mode).
- Placeholder mode is non-exact and currently backed by proxy coefficients.

## Tiny-noise proxy semantics
- integer noise bound: `1`
- integer scale: `1,000,000`
- reported `epsilon_proxy = 1e-6` in scaled-integer sense
- true floating 1e-6 perturbation arithmetic is **not** modeled in this implementation

## Aggregate output
- baseline label: `van_luijk_2007_placeholder_uses_proxy_coeffs`
- baseline marker: `van_luijk_placeholder_mode`
- baseline smoothness screen: pass
- baseline line hits: `0`
- baseline conic-template hits: `0`
- perturbed smooth pass: `152/180`
- perturbed line detected: `6/152` (line incidents `14`)
- perturbed conic-template detected: `0/152` (incidents `0`)

## Interpretation boundary
- This is a proxy-family stability probe under finite scans only.
- No claim is made about van Luijk’s exact published quartic, Picard rank, or NL-membership.
