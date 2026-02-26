# Memo — Q2 Track A v2 positive-only relaxation diagnostic (2026-03-07 label)

## Purpose
Test whether one-step relaxation of v2 thresholding can recover elliptic-v2 hits on the enriched explicit positive bank without touching the locked safety baseline.

## Command
```powershell
python nl_quartic_line_sampling.py --mode positive-control --seed 2026030713 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v2-resultant --elliptic-v2-cross-prime-count 2 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --include-determinantal | Tee-Object -FilePath run-q2-trackA-positive-v2relax-seed-2026030713.txt
```

## Enriched bank composition in this run
- engineered_elliptic_ci_q1q2_mix_a
- engineered_elliptic_ci_q1q2_mix_b
- engineered_elliptic_forced_factor_proxy
- engineered_elliptic_square_proxy_a
- engineered_elliptic_square_proxy_b
- plus legacy special controls (engineered line, forced conic, Fermat, determinantal proxy)

## Outcome
- `elliptic_template_hits=0` across all listed positive-bank entries.
- Line/conic channels still show non-zero hits on some specials.

## Interpretation
- One-step relaxation (`cross_prime_count=2`) did not recover elliptic-v2 sensitivity on the enriched positive bank.
- This suggests current issue is not primarily threshold strictness; likely surrogate-model mismatch (predicate vs positive construction family).

## Recommendation
- Keep v2-tight baseline locked for safety/clean negatives.
- Move to v3 redesign (explicit elliptic template family / stronger surrogate construction) rather than further threshold-only relaxation.
