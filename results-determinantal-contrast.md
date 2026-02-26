# Determinantal Contrast Batch (Day 5, 2026-02-23)

Purpose: small, auditable contrast runs centered on the labeled `determinantal_style_proxy_2x2_quadric_det` entry in the existing pilot tooling.

Boundary conditions:
- Heuristic finite scans only.
- No Picard-rank or Noether–Lefschetz membership claims.
- The determinantal object is a labeled proxy family in-code, not a canonical normal-form claim.

## Commands (exact)
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode positive-control --seed 2026022701 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath noether-lefschetz-pilot/run-determinantal-contrast-positive-control-seed-2026022701.txt

python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022702 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline proxy --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath noether-lefschetz-pilot/run-determinantal-contrast-perturb-proxy-seed-2026022702.txt

python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode random --samples 40 --seed 2026022703 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 --include-determinantal | Tee-Object -FilePath noether-lefschetz-pilot/run-determinantal-contrast-random-plus-bank-seed-2026022703.txt
```

## Compact snapshot table

| run | seed | focal output snapshot | conservative interpretation |
|---|---:|---|---|
| positive-control bank | 2026022701 | `determinantal_style_proxy_2x2_quadric_det`: `smoothness_screen=flag`, `line_hits=3`, `conic_template_hits=0`, `structural_marker=determinantal_proxy_marker` | Tagged proxy is detectable as special under this finite bank/line scan; this is scanner-behavior evidence only. |
| perturbation (proxy baseline) | 2026022702 | `trials=120`, `smooth_pass=96`, `line_detected=0/96`, `conic_template_detected=0/96`, `epsilon_proxy=1e-6` | Tiny-noise proxy perturbation batch showed no scanned line/conic-template detections in analyzed trials; non-certifying finite-scan result. |
| random + special-bank contrast | 2026022703 | random analyzed `36`; random line/conic detections `0/36`; same run’s determinantal proxy line hits `6` in special-bank block | In-run contrast: tagged special entry shows scanner hits while sampled random block showed none under this scan budget; no NL/Picard inference. |

## Inferential limits (explicit)
- Smoothness outcomes are sampled modular-screen outcomes, not full singularity certification.
- Line/conic-template banks are incomplete finite scans.
- No theorem-level conclusions are drawn from these outputs.

## Validation addendum — van Luijk micro-pass freeze check (2026-02-24)

Purpose: quick post-Day-5 stability confirmation near the exact van Luijk baseline, with expanded conic templates and broader smoothness-prime sets.

### Commands (exact)
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022801 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --smooth-points-per-prime 180 --smooth-primes 5,7,11,13,17 | Tee-Object -FilePath noether-lefschetz-pilot/run-validation-micro-pass-primes-5-7-11-13-17-seed-2026022801.txt

python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022802 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 100000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --smooth-points-per-prime 180 --smooth-primes 5,7,11,13,19 | Tee-Object -FilePath noether-lefschetz-pilot/run-validation-micro-pass-primes-5-7-11-13-19-seed-2026022802.txt
```

### Snapshot table

| run | seed | key output fields | conservative interpretation |
|---|---:|---|---|
| micro-pass A (eps 1e-6) | 2026022801 | `trials=120`, `smooth_pass=88`, `line_detected=0/88`, `conic_template_detected=0/88`, `max_conic_templates=96`, `smooth_primes=5,7,11,13,17` | Expanded finite scan remained at zero scanned line/conic-template detections in analyzed perturbed samples. |
| micro-pass B (eps 1e-5) | 2026022802 | `trials=120`, `smooth_pass=92`, `line_detected=0/92`, `conic_template_detected=0/92`, `max_conic_templates=96`, `smooth_primes=5,7,11,13,19` | Same zero-detection profile under alternate added-prime set and larger proxy epsilon. |

Validation note (conservative): this micro-pass supports heuristic stability of the previously observed zero/near-zero detection regime around the exact van Luijk baseline under expanded scan settings. It does not certify smoothness, Picard rank, or NL membership.
