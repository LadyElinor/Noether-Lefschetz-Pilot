# Memo — Q2 Track A v3 perturbation sentinel5 (2026-02-25)

## Bounded increment completed
Executed one rotated fixed-seed perturbation sentinel under unchanged Track A guardrails (v2-tight frozen; v3 diagnostic-only):

```bash
python nl_quartic_line_sampling.py --mode perturbation --perturb-trials 200 --seed 2026032111 --perturbation-baseline van_luijk_exact_2007 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19
```

Log:
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt`

## Key readout (heuristic only)
- `perturbed_smooth_pass=142/200`
- `perturbed_line_detected=0/142`
- `perturbed_conic_template_detected=0/142`
- `perturbed_elliptic_template_detected=0/142`
- `perturbed_elliptic_v2_surrogate_detected=0/142`
- gate guardrail summary from run output: `gate_guardrail_fp_hits=0`, `gate_guardrail_fp_total=142`, `gate_guardrail_fp_rate=0.000000`, `gate_guardrail_pass=1`

## Conservative interpretation
- This rotated-seed perturbation sentinel5 remained clean across tracked heuristic channels in this bounded run.
- Supports continued diagnostic-only v3 monitoring under unchanged guardrails.
- v2-tight remains frozen baseline; no theorem-level or NL-membership claims are made.

## Documentation updated
- `q2-definitive-summary.md` (added perturbation sentinel5 row)
- `results-q2-trackA-validation.md` (added v3 perturbation sentinel5 section)
