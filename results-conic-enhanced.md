# Conic-Enhanced Extension Results (2026-02-23)

## Exact commands used
```bash
python nl_quartic_line_sampling.py --mode random --samples 220 --seed 202602239 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 12 --smooth-points-per-prime 100 --smooth-primes 5,7 --include-determinantal > run-conic-enhanced-random-seed-202602239.txt

python nl_quartic_line_sampling.py --mode perturbation --perturb-trials 180 --perturb-noise-bound 1 --seed 202602240 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 12 --smooth-points-per-prime 100 --smooth-primes 5,7 > run-conic-perturb-noise1-seed-202602240.txt

python nl_quartic_line_sampling.py --mode perturbation --perturb-trials 180 --perturb-noise-bound 2 --seed 202602241 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 12 --smooth-points-per-prime 100 --smooth-primes 5,7 > run-conic-perturb-noise2-seed-202602241.txt
```

## Random conic-enhanced run (seed 202602239)
- Candidate lines: `260`
- Candidate conic templates: `12`
- Smoothness screen pass: `177/220 = 0.8045`
- Line-detected among smooth-pass set: `1/177 = 0.0056`
- Conic-template-detected among smooth-pass set: `0/177 = 0.0000`
- Total line incidents: `3`
- Total conic-template incidents: `0`

Special-bank sanity signals:
- Forced-conic example: `conic_template_hits=3`, `contains_test_conic_xz-y2=yes`
- This confirms the conic template path can trigger on engineered conic-bearing input.

## Proxy perturbation round (post smoothness-screen rates)
> Exact van Luijk polynomial is not pinned in this folder; these are **proxy baseline only** runs.

### Noise bound 1 (seed 202602240)
- Smooth-pass: `148/180 = 0.8222`
- Line-detected among smooth-pass set: `2/148 = 0.0135`
- Conic-template-detected among smooth-pass set: `0/148 = 0.0000`
- Line incidents: `3`
- Conic-template incidents: `0`

### Noise bound 2 (seed 202602241)
- Smooth-pass: `155/180 = 0.8611`
- Line-detected among smooth-pass set: `1/155 = 0.0065`
- Conic-template-detected among smooth-pass set: `0/155 = 0.0000`
- Line incidents: `1`
- Conic-template incidents: `0`

## Conservative interpretation
- These are finite-scan heuristic detection rates only.
- No claim is made about Picard rank or Noether–Lefschetz locus membership.
- Conic-template non-detection means only: no hit in this small, incomplete template family.
