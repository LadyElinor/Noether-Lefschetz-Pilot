# Results — van Luijk exact baseline perturbation (tiny-noise block)

Date: 2026-02-23

## Pre-registered style command
```powershell
python noether-lefschetz-pilot/nl_quartic_line_sampling.py --mode perturbation --seed 2026022607 --perturb-trials 160 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 64 --smooth-points-per-prime 100 --smooth-primes 5,7 | Tee-Object -FilePath noether-lefschetz-pilot/run-vanluijk-exact-perturb-seed-2026022607.txt
```

## Captured output (verbatim)
```text
=== van-Luijk-track perturbation test (conservative, heuristic only) ===
Deterministic perturbation arithmetic: integer coefficient noise in [-noise_bound, noise_bound] with reported epsilon_proxy=noise_bound/noise_scale.
No floating perturbation arithmetic is used; this avoids float-instability overclaims.
seed=2026022607, trials=160, noise_bound=1, noise_scale=1000000, epsilon_proxy=1e-06, baseline_mode=van_luijk_exact_2007, candidate_lines=259, candidate_conic_templates=64
base_label=van_luijk_exact_2007_h0_expanded, baseline_note=van_luijk_exact_2007_h0_from_cited_equation, base_marker=van_luijk_exact_2007
base_smoothness_screen=pass (no_sampled_mod_p_singular_point_detected), base_line_hits=0, base_conic_template_hits=0
THEOREM-CONTEXT NOTE: rho_geom=1 per cited source context for this explicit family setup; this run itself does not certify Picard rank.
perturbed_smooth_pass=139/160, perturbed_line_detected=0/139, perturbed_line_incidents=0, perturbed_conic_template_detected=0/139, perturbed_conic_template_incidents=0
Interpretation: proxy-family stability signal under this finite scan only.
```

## Conservative interpretation
- This run uses the exact coded baseline label `van_luijk_exact_2007_h0_expanded` with deterministic integer-scaled tiny noise (`1/10^6` proxy epsilon).
- Within this finite scan configuration, no sampled line/conic-template hits were detected in analyzed perturbed trials.
- This is a finite-scan heuristic stability observation only; it is not Picard-rank certification and not NL-membership evidence.
