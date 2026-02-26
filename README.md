# Noether–Lefschetz Quartic Pilot (Heuristic, stdlib-only)

## Scope and boundaries
This folder is a **finite-scan heuristic pilot** for quartic surfaces in \(\mathbf{P}^3\).

It does **not** compute:
- Picard rank,
- full discriminant/smoothness certification,
- Noether–Lefschetz locus membership.

All outputs are screening signals only.

## Script
- `nl_quartic_line_sampling.py`
- Python stdlib only.

## Modes
- `--mode random`: random quartic batch + special-bank checks.
- `--mode positive-control`: special-family bank only (including determinantal-style proxy).
- `--mode stratified`: random sampling across coefficient bounds.
- `--mode perturbation`: conservative perturbation mode with deterministic integer-noise arithmetic.

## Controls used in this project
- **True positive-control (theorem-context family):** quartics explicitly constructed to contain low-degree curves (e.g., engineered line-containing forms `xG3+yH3`; forced-conic template family). These are intended to produce detectable special behavior in finite scans.
- **True generic-control (theorem-context label):** a *very general smooth quartic* is expected to have Picard rank 1 (external theorem context). In-code random screened quartics are only a computational proxy and are not theorem certification.

## Positive-control additions
- Added labeled determinantal-style constructor:
  - `determinantal_style_proxy_2x2_quadric_det`
  - structural marker: `determinantal_proxy_marker`
- This is explicitly a **proxy**, not claimed canonical literature normal form.

## van Luijk baseline integration (exact vs proxy)
Two perturbation baselines are available:
- `--perturbation-baseline proxy`
- `--perturbation-baseline van_luijk_exact_2007`

The exact baseline is encoded as the explicit integer-expanded quartic from van Luijk’s published family model
\(wf_1+2zf_2=3g_1g_2+6h\) with \(h=0\), using the explicit `f1,f2,g1,g2` equation in the source context.

Boundary: theorem-context statements (e.g., “\(\rho_{geom}=1\) per cited source context”) are kept textually separate from heuristic run outputs.

## Deterministic tiny-noise arithmetic
Perturbation uses integer coefficient noise with a documented scale:
- `--perturb-noise-bound n`
- `--perturb-noise-scale S`
- reported proxy epsilon = `n / S`

Example: `n=1, S=1000000` gives `epsilon_proxy=1e-6` in a scaled-integer sense.
No floating arithmetic is used in perturbation mode (to avoid float-instability overclaims).

## Conic-template bank
- Deterministic seeded template generation expanded.
- Typical operational range: `--max-conic-templates 50..100` (default `64`).
- Scan remains incomplete; non-detection is not evidence of conic absence.

## Elliptic-template knob (Q2 minimal)
- Added CLI flag: `--max-elliptic-templates` (default `0`, disabled by default).
- Current implementation is a deterministic surrogate template-incidence path intended for calibration.
- Any `elliptic_template_*` output is heuristic/non-certifying template behavior only; it is not an elliptic-curve certification pipeline.

### Current calibrated Track A profile
- `--elliptic-probe-mode v2-resultant`
- `--elliptic-v2-cross-prime-count 3`
- `--elliptic-v2-min-rootcount 3`
- `--max-elliptic-templates 30`

## Definitive block v1 (pre-registered)
Fixed parameters:
- `point-bound=1`
- `max-deterministic-lines=180`
- `random-line-probes=80`
- `max-conic-templates=64`
- `smooth-points-per-prime=100`
- `smooth-primes=5,7`

Fixed seeds:
- Generic control block seed: `2026022301`
- Positive control block seed: `2026022302`

Control-family labels (for docs/results):
- `GEN_CTRL_TRUE_RANDOM_QUARTIC_B2` (random quartics with `coeff-bound=2`)
- `POS_CTRL_TRUE_FORCED_CONIC` (forced-conic special family in positive bank)

Commands:
```bash
python nl_quartic_line_sampling.py --mode random --samples 80 --seed 2026022301 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 100 --smooth-primes 5,7

python nl_quartic_line_sampling.py --mode positive-control --seed 2026022302 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 100 --smooth-primes 5,7 --include-determinantal
```

## Perturbation command example (exact van Luijk baseline)
```bash
python nl_quartic_line_sampling.py --mode perturbation --seed 2026022607 --perturb-trials 160 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 100 --smooth-primes 5,7
```

Boundary reminder: all runs are heuristic scan outputs only; no Picard-rank or NL-membership inference is permitted from scan counts.
