# Results — van Luijk exact-track stability mini-grid

Date: 2026-02-23

## Fixed run pattern (all strata)
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed {SEED} --perturb-trials 140 --perturb-noise-bound 1 --perturb-noise-scale {SCALE} --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath {LOG_PATH}
```

## Stability comparison (compact)

| epsilon_proxy | seed | trials | smooth_pass | line_detected / analyzed | conic_template_detected / analyzed | baseline_smoothness_screen | log |
|---:|---:|---:|---:|---:|---:|---|---|
| 1e-6 | 2026022641 | 140 | 112 | 0 / 112 | 0 / 112 | pass | `run-vanluijk-stability-grid-noise1e-6-seed-2026022641.txt` |
| 1e-5 | 2026022642 | 140 | 117 | 0 / 117 | 0 / 117 | flag (sampled mod-5 point) | `run-vanluijk-stability-grid-noise1e-5-seed-2026022642.txt` |
| 1e-4 | 2026022643 | 140 | 103 | 0 / 103 | 0 / 103 | flag (sampled mod-5 point) | `run-vanluijk-stability-grid-noise1e-4-seed-2026022643.txt` |

## Conservative readout
- Across all three proxy-noise strata in this finite scan, no analyzed perturbation sample triggered scanned line detection or scanned conic-template detection.
- The baseline smoothness screen changed across seeded runs (pass vs sampled modular flag), consistent with heuristic point-sampling variability rather than certification.
- The theorem-context note (`rho_geom=1` for this explicit family in cited source context) remains external context only; these runs do **not** certify Picard rank and do **not** establish NL membership.
