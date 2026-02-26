# Memo — Q2 Track A v3 spillover gate (2026-03-09 label)

## Objective
Execute the immediate next-step gate after v3 positive-only signal recovery: check negative spillover risk of `v3-weierstrass` on random and van-Luijk perturbation controls.

## Commands
```powershell
python nl_quartic_line_sampling.py --mode random --samples 200 --seed 2026030912 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-v3weierstrass-seed-2026030912.txt

python nl_quartic_line_sampling.py --mode perturbation --seed 2026030911 --perturb-trials 200 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-v3weierstrass-seed-2026030911.txt
```

## Results
- Random gate block: `smooth_pass=166/200`, `elliptic_template_detected=0/166`, incidents `0`
- Van-Luijk perturbation gate block: `smooth_pass=156/200`, `elliptic_template_detected=0/156`, incidents `0`

## Interpretation
- No observed negative spillover in this finite v3 gate run.
- Together with prior positive-only v3 hit recovery on explicit Weierstrass constructions, this supports **provisional experimental** use of `v3-weierstrass` for targeted diagnostics.
- Keep v2-tight frozen baseline unchanged for routine exploratory work.

## Not Claimed
- No Picard-rank certification.
- No Noether–Lefschetz membership certification.
- No full smoothness certification from sampled modular checks.
- No claim that v3 incidents certify embedded elliptic curves.

## Next gate hardening
- Repeat v3 spillover gate at larger scale (>=240 random, >=240 perturbation) before broad recommendation changes.
