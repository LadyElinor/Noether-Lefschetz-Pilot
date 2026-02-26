# Memo — Q2 Track A determinism revalidation on v3 random sentinel5 (2026-02-25)

## Bounded increment completed
Performed one same-seed rerun of the previously recorded v3 random sentinel5 configuration and generated a hash receipt.

Rerun command (unchanged flags):
```bash
python nl_quartic_line_sampling.py --mode random --seed 2026032012 --samples 200 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19
```

Artifacts:
- baseline: `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`
- rerun: `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`
- receipt: `run-q2-trackA-determinism-receipt-random-v3-sentinel5-seed-2026032012.txt`

## Key receipt readout
- `sha256_a == sha256_b` (`ff67d316d4613669bf656c2e9a68306959640a0eab3281abc8f0a8e220efad00`)
- `byte_identical_sha256: true`
- `text_identical: true`

## Conservative interpretation
- This bounded step confirms byte-identical replay for one prior v3 random sentinel artifact under fixed seed/flags.
- Evidence is operational and finite only; no Picard-rank, Noether-Lefschetz, or theorem-level claim is made.
