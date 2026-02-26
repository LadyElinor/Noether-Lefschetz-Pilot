# NL Definitive Summary (v1 block)

Pre-registered parameters were fixed as documented in `README.md` and `../execution-sprint-2weeks.md`.

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| definitive-generic-v1 | GEN_CTRL_TRUE_RANDOM_QUARTIC_B2 | 2026022301 | `run-definitive-random-seed-2026022301.txt` | `samples=80`, `smoothness_pass=71`, `flagged=9`, `line_detected_samples=1/71`, `conic_detected_samples=0/71` | Finite scan found low incidence in analyzed random subset; this is calibration behavior only, not evidence of generic Picard rank or NL-genericity. |
| definitive-positive-v1 | POS_CTRL_TRUE_FORCED_CONIC | 2026022302 | `run-definitive-positive-control-seed-2026022302.txt` | `family=forced_conic_(xz-y^2)Q2+wR3`, `line_hits=3`, `conic_template_hits=0`, `smoothness_screen=flag` | Positive-control family produced scanner hits, supporting sensitivity on tagged constructions only; no NL-membership claim. |
| definitive-vanluijk-perturb-v1 | VAN_LUIJK_EXACT_2007_H0_TINY_NOISE | 2026022607 | `run-vanluijk-exact-perturb-seed-2026022607.txt` | `trials=160`, `smooth_pass=139`, `line_detected=0/139`, `conic_template_detected=0/139`, `epsilon_proxy=1e-6` | Tiny-noise finite-scan run around exact labeled baseline showed no scanned line/conic-template detections; theorem-context rho_geom=1 note remains external-source context only, not run-certified. |

## Added block — van Luijk stability mini-grid (Day 4)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| stability-grid-1e-6-v1 | VAN_LUIJK_EXACT_2007_H0_GRID | 2026022641 | `run-vanluijk-stability-grid-noise1e-6-seed-2026022641.txt` | `trials=140`, `smooth_pass=112`, `line_detected=0/112`, `conic_template_detected=0/112`, `epsilon_proxy=1e-6` | Finite-scan perturbation stratum showed no scanned line/conic-template detections in analyzed samples; non-certifying. |
| stability-grid-1e-5-v1 | VAN_LUIJK_EXACT_2007_H0_GRID | 2026022642 | `run-vanluijk-stability-grid-noise1e-5-seed-2026022642.txt` | `trials=140`, `smooth_pass=117`, `line_detected=0/117`, `conic_template_detected=0/117`, `epsilon_proxy=1e-5`, `baseline_smoothness=flag` | Same finite-scan non-detection profile; sampled modular smoothness flag occurred in baseline screen and is treated as heuristic-screen variability. |
| stability-grid-1e-4-v1 | VAN_LUIJK_EXACT_2007_H0_GRID | 2026022643 | `run-vanluijk-stability-grid-noise1e-4-seed-2026022643.txt` | `trials=140`, `smooth_pass=103`, `line_detected=0/103`, `conic_template_detected=0/103`, `epsilon_proxy=1e-4`, `baseline_smoothness=flag` | Same finite-scan non-detection profile at larger proxy perturbation; no Picard-rank/NL inference. |

### Exact command lines for stability mini-grid
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022641 --perturb-trials 140 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath noether-lefschetz-pilot/run-vanluijk-stability-grid-noise1e-6-seed-2026022641.txt
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022642 --perturb-trials 140 --perturb-noise-bound 1 --perturb-noise-scale 100000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath noether-lefschetz-pilot/run-vanluijk-stability-grid-noise1e-5-seed-2026022642.txt
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022643 --perturb-trials 140 --perturb-noise-bound 1 --perturb-noise-scale 10000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath noether-lefschetz-pilot/run-vanluijk-stability-grid-noise1e-4-seed-2026022643.txt
```

## Added block — Day 5 determinantal contrast (2026-02-23)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| day5-determinantal-positive-control-v1 | DET_PROXY_TAGGED_BANK_CHECK | 2026022701 | `run-determinantal-contrast-positive-control-seed-2026022701.txt` | `det_proxy_smoothness=flag`, `det_proxy_line_hits=3`, `det_proxy_conic_template_hits=0`, `marker=determinantal_proxy_marker` | Tagged determinantal-style proxy produced finite-scan line hits in the positive bank; scanner-sensitivity evidence only. |
| day5-proxy-perturbation-v1 | PROXY_BASELINE_TINY_NOISE | 2026022702 | `run-determinantal-contrast-perturb-proxy-seed-2026022702.txt` | `trials=120`, `smooth_pass=96`, `line_detected=0/96`, `conic_template_detected=0/96`, `epsilon_proxy=1e-6` | Tiny-noise perturbation around proxy baseline showed no scanned line/conic-template detections in analyzed trials; non-certifying finite-scan outcome. |
| day5-random-vs-detproxy-contrast-v1 | RANDOM_B2_PLUS_SPECIAL_BANK | 2026022703 | `run-determinantal-contrast-random-plus-bank-seed-2026022703.txt` | `random_analyzed=36`, `random_line_detected=0/36`, `random_conic_detected=0/36`, `det_proxy_line_hits=6` | Same-run contrast showed tagged special entry with scanner hits while sampled random subset had none under this budget; no Picard/NL inference. |

### Exact command lines for Day 5 determinantal contrast
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode positive-control --seed 2026022701 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath noether-lefschetz-pilot/run-determinantal-contrast-positive-control-seed-2026022701.txt
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022702 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline proxy --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 | Tee-Object -FilePath noether-lefschetz-pilot/run-determinantal-contrast-perturb-proxy-seed-2026022702.txt
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode random --samples 40 --seed 2026022703 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 140 --smooth-primes 5,7,11,13 --include-determinantal | Tee-Object -FilePath noether-lefschetz-pilot/run-determinantal-contrast-random-plus-bank-seed-2026022703.txt
```

## Added block — Day 5.5 validation micro-pass (2026-02-24)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| day5_5-vanluijk-micro-pass-a-v1 | VAN_LUIJK_EXACT_2007_H0_VALIDATION | 2026022801 | `run-validation-micro-pass-primes-5-7-11-13-17-seed-2026022801.txt` | `trials=120`, `smooth_pass=88`, `line_detected=0/88`, `conic_template_detected=0/88`, `epsilon_proxy=1e-6`, `max_conic_templates=96` | Expanded-template + expanded-prime finite scan preserved zero scanned line/conic-template detections in analyzed perturbations; non-certifying. |
| day5_5-vanluijk-micro-pass-b-v1 | VAN_LUIJK_EXACT_2007_H0_VALIDATION | 2026022802 | `run-validation-micro-pass-primes-5-7-11-13-19-seed-2026022802.txt` | `trials=120`, `smooth_pass=92`, `line_detected=0/92`, `conic_template_detected=0/92`, `epsilon_proxy=1e-5`, `max_conic_templates=96` | Same zero-detection profile under alternate added-prime set at higher proxy epsilon; no Picard/NL inference. |
| day5_5-vanluijk-micro-pass-c-v1 | VAN_LUIJK_EXACT_2007_H0_VALIDATION | 2026022819 | `run-validation-micro-pass-primes-5-7-11-13-17-19-seed-2026022819.txt` | `trials=120`, `smooth_pass=88`, `line_detected=0/88`, `conic_template_detected=0/88`, `epsilon_proxy=1e-6`, `max_conic_templates=96`, `smooth_primes=5,7,11,13,17,19` | Combined-added-prime rerun preserved zero-detection profile in analyzed perturbations; non-certifying finite-scan outcome. |

### Exact command lines for Day 5.5 validation micro-pass
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022801 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --smooth-points-per-prime 180 --smooth-primes 5,7,11,13,17 | Tee-Object -FilePath noether-lefschetz-pilot/run-validation-micro-pass-primes-5-7-11-13-17-seed-2026022801.txt
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022802 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 100000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --smooth-points-per-prime 180 --smooth-primes 5,7,11,13,19 | Tee-Object -FilePath noether-lefschetz-pilot/run-validation-micro-pass-primes-5-7-11-13-19-seed-2026022802.txt
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022819 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --smooth-points-per-prime 180 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath noether-lefschetz-pilot/run-validation-micro-pass-primes-5-7-11-13-17-19-seed-2026022819.txt
```

Audit notes:
- No Picard-rank claims.
- No Noether–Lefschetz locus membership claims.
- Smoothness outcomes are heuristic sampled modular screens only.
