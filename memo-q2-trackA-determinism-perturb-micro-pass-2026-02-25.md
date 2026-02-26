# Memo — Q2 Track A perturbation determinism micro-pass (2026-02-25)

## Objective
Execute one bounded hardening validation step for Track A: same-seed rerun determinism check for perturbation mode under the current conservative v3 diagnostic guardrails.

## Runs
- `run-q2-trackA-determinism-pert-seed-2026022517-pass1.txt`
- `run-q2-trackA-determinism-pert-seed-2026022517-pass2.txt`

Command profile (both passes):
- `--mode perturbation --perturbation-baseline van_luijk_exact_2007`
- `--perturb-trials 120 --seed 2026022517`
- `--coeff-bound 2 --point-bound 1`
- `--max-deterministic-lines 180 --random-line-probes 80`
- `--max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20`
- `--elliptic-probe-mode v3-weierstrass`
- `--elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3`
- `--v3-prime-sample 31 --v3-min-points 15`
- `--smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19`

## Readout (pass1 vs pass2)
- Full output files are line-identical (`Compare-Object` yielded no diffs).
- `perturbed_smooth_pass=108/120`
- `perturbed_line_detected=0/108`, incidents `0`
- `perturbed_conic_template_detected=0/108`, incidents `0`
- `perturbed_elliptic_template_detected=0/108`, incidents `0`
- `perturbed_elliptic_v2_surrogate_detected=0/108`, incidents `0`
- guardrail summary matched exactly: `gate_guardrail_fp_hits=0`, `gate_guardrail_fp_total=108`, `gate_guardrail_fp_rate=0.000000`, `gate_guardrail_pass=1`

## Conservative interpretation
- This bounded same-seed rerun supports operational determinism of the current perturbation-mode path under fixed parameters.
- Treated strictly as implementation hardening evidence in finite tests; no geometric certification or NL/Picard inference is implied.
