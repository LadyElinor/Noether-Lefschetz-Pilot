# Q2 Track A — Initial Elliptic-Incidence Probe Overview (Heuristic)

Date: 2026-02-24  
Scope: initial fixed-seed shakeout using new `--max-elliptic-templates` knob (minimal surrogate implementation).

## Boundary reminder
- All outputs are finite heuristic scan outcomes only.
- No Picard-rank certification claims.
- No NL-membership claims.
- Elliptic-template metrics are surrogate template incidents, not elliptic-curve certification.

## Commands run
```powershell
python nl_quartic_line_sampling.py --mode random --samples 60 --seed 2026030102 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-seed-2026030102.txt

python nl_quartic_line_sampling.py --mode positive-control --seed 2026030103 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --include-determinantal | Tee-Object -FilePath run-q2-trackA-positive-seed-2026030103.txt

python nl_quartic_line_sampling.py --mode perturbation --seed 2026030101 --perturb-trials 80 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-seed-2026030101.txt
```

## Snapshot results

| block | seed | key outputs | conservative readout |
|---|---:|---|---|
| random proxy | 2026030102 | `smooth_pass=46/60`, `line_detected=0/46`, `conic_detected=0/46`, `elliptic_template_detected=0/46` | Initial random block remained zero-incidence across line/conic/elliptic-template scans in analyzed samples. |
| positive bank | 2026030103 | engineered line hits present; forced-conic template hit present; determinantal proxy line hits present; `elliptic_template_hits=0` on bank entries | Scanner sensitivity remains visible on tagged special constructions; elliptic-template surrogate produced no incidents in this initial bank. |
| exact-baseline perturbation | 2026030101 | `smooth_pass=72/80`, `line_detected=0/72`, `conic_detected=0/72`, `elliptic_template_detected=0/72` | Negative-control style stability remained zero-incidence under this finite perturbation batch. |

## Immediate takeaways
1. The new elliptic-template knob is operational and deterministic in normal runs.
2. Initial shakeout (v1-template) showed no elliptic-template incidents in sampled random/special-bank/van-Luijk analyzed subsets.
3. This was conservative for a minimal surrogate v1 and did not imply absence of elliptic curves.

## v2 resultant-surrogate addendum (same day)
Additional seeded triad runs with `--elliptic-probe-mode v2-resultant`:
- `run-q2-trackA-random-v2-seed-2026030212.txt`
- `run-q2-trackA-positive-v2-seed-2026030213.txt`
- `run-q2-trackA-pert-v2-seed-2026030211.txt`

Snapshot:
- random analyzed: `elliptic_template_detected=8/61`, `elliptic_v2_surrogate_incidents=9`
- positive bank: mixed non-zero hits on some specials
- van-Luijk perturbation analyzed: `elliptic_template_detected=5/78`, `elliptic_v2_surrogate_incidents=5`

Calibration readout:
- v2 surrogate currently appears over-sensitive for clean negative-control separation and needs stricter filtering before any broader use.
