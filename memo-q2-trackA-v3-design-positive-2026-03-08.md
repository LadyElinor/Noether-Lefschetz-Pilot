# Memo — Q2 Track A v3 design positive-only check (2026-03-08 label)

## Why this block
v2 threshold tuning (strict and one-step relaxation) did not recover robust elliptic hits on enriched positive bank. This motivated a surrogate redesign test (v3) rather than further threshold-only adjustments.

## v3 prototype implemented
- New probe mode: `v3-weierstrass`
- New explicit positive constructors:
  - `explicit_elliptic_weierstrass_plane_a-1_b0_L1111`
  - `explicit_elliptic_weierstrass_plane_a-2_b3_L1111`
- v3 detector checks whether `F|_{w=0}` is proportional to a low-height Weierstrass cubic times linear form (`C3 * L`) from a small fixed bank.
- This is a heuristic match predicate, not an elliptic-curve certification pipeline.

## Commands
```powershell
python nl_quartic_line_sampling.py --mode positive-control --seed 2026030813 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v2-resultant --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --include-determinantal | Tee-Object -FilePath run-q2-trackA-positive-v2tight-v3bank-seed-2026030813.txt

python nl_quartic_line_sampling.py --mode positive-control --seed 2026030814 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --include-determinantal | Tee-Object -FilePath run-q2-trackA-positive-v3weierstrass-seed-2026030814.txt
```

## Comparison summary
- v2-tight on expanded bank:
  - explicit Weierstrass entries remained `elliptic_template_hits=0`
  - one non-Weierstrass proxy (`engineered_elliptic_square_proxy_b`) showed sparse v2 hits
- v3-weierstrass:
  - explicit Weierstrass entries each showed `elliptic_template_hits=1`
  - other listed non-Weierstrass specials were `0` in this run

## Readout
- v3 prototype recovers intended positive-only sensitivity directionally.
- Keep v2-tight profile as locked safety baseline.
- Next requirement before any profile recommendation change: run random + van-Luijk perturbation checks under `v3-weierstrass` to estimate spillover.

## Not Claimed
- No Picard-rank certification.
- No NL-membership certification.
- No full smoothness certification from sampled modular screen.
- No claim that v3 incidents certify embedded elliptic curves.
