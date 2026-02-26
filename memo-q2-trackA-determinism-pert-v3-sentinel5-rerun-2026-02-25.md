# Memo — Q2 Track A determinism revalidation on v3 perturbation sentinel5 (2026-02-25)

## Bounded increment completed
Performed one same-seed rerun of the previously recorded v3 perturbation sentinel5 configuration and generated a strict determinism receipt.

Rerun command (unchanged flags):
```bash
python nl_quartic_line_sampling.py --mode perturbation --perturb-trials 200 --seed 2026032111 --perturbation-baseline van_luijk_exact_2007 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19
```

Artifacts:
- baseline: `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt`
- rerun: `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111-rerun.txt`
- receipt: `run-q2-trackA-determinism-receipt-pert-v3-sentinel5-seed-2026032111.txt`

## Key receipt readout
- `sha256_a == sha256_b` (`022da4b3cff490452842a0f4a9123718a346c08b2fe74fee06bd831254a288d1`)
- `byte_identical_sha256: true`
- `text_identical: true`
- `require_identical_check: pass`

## Conservative interpretation
- This bounded step confirms byte-identical replay for one prior v3 perturbation sentinel artifact under fixed seed/flags.
- Evidence is operational and finite only; no Picard-rank, Noether-Lefschetz, or theorem-level claim is made.

## Documentation updated
- `results-q2-trackA-validation.md` (added determinism revalidation section for perturbation sentinel5)
