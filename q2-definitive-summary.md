# Q2 Definitive Summary (Track A, early block)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-initial-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030102 | `run-q2-trackA-random-seed-2026030102.txt` | `samples=60`, `smooth_pass=46`, `line_detected=0/46`, `conic_template_detected=0/46`, `elliptic_template_detected=0/46` | Initial random-proxy batch showed zero incidents in analyzed samples under finite scan budget; non-certifying. |
| q2-trackA-positive-initial-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_QUARTIC_PROXYBANK | 2026030103 | `run-q2-trackA-positive-seed-2026030103.txt` | engineered/determinantal line hits observed; forced-conic template hit observed; `elliptic_template_hits=0` on listed bank entries | Scanner sensitivity on tagged specials remains visible for prior line/conic channels; elliptic-template surrogate channel showed no incidents in this initial bank. |
| q2-trackA-perturb-initial-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030101 | `run-q2-trackA-pert-seed-2026030101.txt` | `trials=80`, `smooth_pass=72`, `line_detected=0/72`, `conic_template_detected=0/72`, `elliptic_template_detected=0/72`, `epsilon_proxy=1e-6` | Initial exact-baseline perturbation block retained zero incident profile across line/conic/elliptic-template channels in analyzed perturbations; non-certifying. |

## Added block — Track A v2 resultant-surrogate pilot

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v2-initial-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030212 | `run-q2-trackA-random-v2-seed-2026030212.txt` | `samples=80`, `smooth_pass=61`, `elliptic_template_detected=8/61`, `elliptic_v2_surrogate_incidents=9` | v2 surrogate produced non-zero incidents in random analyzed samples, indicating this surrogate is sensitive and may still be over-inclusive at current thresholds. |
| q2-trackA-positive-v2-initial-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_QUARTIC_PROXYBANK | 2026030213 | `run-q2-trackA-positive-v2-seed-2026030213.txt` | engineered/forced-conic specials had non-zero `elliptic_template_hits`; Fermat/determinantal entries varied | Positive bank shows selective v2 hits on some specials; current signal is mixed and requires additional calibration before interpretation. |
| q2-trackA-perturb-v2-initial-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030211 | `run-q2-trackA-pert-v2-seed-2026030211.txt` | `trials=100`, `smooth_pass=78`, `elliptic_template_detected=5/78`, `elliptic_v2_surrogate_incidents=5` | Non-zero v2 incidents appear in baseline perturbations; treat as surrogate false-positive pressure until stricter filters are added. |

## Added block — Track A v2 tightened-threshold pilot

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v2-tight-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030212 | `run-q2-trackA-random-v2tight-seed-2026030212.txt` | `samples=80`, `smooth_pass=61`, `elliptic_template_detected=0/61`, `elliptic_v2_surrogate_incidents=0`, `v2_cross_prime_count=3`, `v2_min_rootcount=3` | Tightened v2 thresholds eliminated random-block v2 incidents in analyzed samples. |
| q2-trackA-positive-v2-tight-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_QUARTIC_PROXYBANK | 2026030213 | `run-q2-trackA-positive-v2tight-seed-2026030213.txt` | engineered line-special retained non-zero `elliptic_template_hits=2`; others mostly zero under tightened thresholds | Tightening preserved limited positive-bank sensitivity while reducing broad over-triggering. |
| q2-trackA-perturb-v2-tight-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030211 | `run-q2-trackA-pert-v2tight-seed-2026030211.txt` | `trials=100`, `smooth_pass=78`, `elliptic_template_detected=0/78`, `elliptic_v2_surrogate_incidents=0`, `v2_cross_prime_count=3`, `v2_min_rootcount=3` | Tightened v2 thresholds restored clean negative-control behavior in analyzed van-Luijk perturbations. |

## Added block — Track A v2 tightened-threshold larger calibration

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v2-tight-large-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030312 | `run-q2-trackA-random-v2tight-large-seed-2026030312.txt` | `samples=240`, `smooth_pass=186`, `elliptic_v2_surrogate_detected=0/186`, `incidents=0` | Larger random calibration preserved zero v2 incidents under tightened thresholds. |
| q2-trackA-random-v2-tight-large-repeat-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030312 | `run-q2-trackA-random-v2tight-large-repeat-seed-2026030312.txt` | `samples=240`, `smooth_pass=186`, `elliptic_v2_surrogate_detected=0/186`, `incidents=0` | Deterministic repeat matched the primary large random block exactly under identical seed/parameters. |
| q2-trackA-positive-v2-tight-large-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_QUARTIC_PROXYBANK | 2026030313 | `run-q2-trackA-positive-v2tight-large-seed-2026030313.txt` | positive bank retained line/conic sensitivity; `elliptic_template_hits=0` in this seed | Tightened v2 profile is conservative; elliptic surrogate sensitivity is currently sparse on this positive-bank composition. |
| q2-trackA-perturb-v2-tight-large-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030311 | `run-q2-trackA-pert-v2tight-large-seed-2026030311.txt` | `trials=240`, `smooth_pass=185`, `elliptic_v2_surrogate_detected=0/185`, `incidents=0` | Larger van-Luijk perturbation block stayed clean under tightened v2 thresholds. |
| q2-trackA-perturb-v2-tight-rerun-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030319 | `run-q2-trackA-pert-v2tight-rerun-seed-2026030319.txt` | `trials=140`, `smooth_pass=106`, `elliptic_v2_surrogate_detected=0/106`, `incidents=0` | Validation rerun confirms clean negative-control behavior at tightened settings. |

## Added block — Track A positive-bank enrichment pass (CI-style additions)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v2-tight-enriched-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030412 | `run-q2-trackA-random-v2tight-enriched-seed-2026030412.txt` | `samples=200`, `smooth_pass=154`, `elliptic_v2_surrogate_detected=1/154`, `incidents=1` | Random block remained near-zero under enriched-bank code path; small residual incident count recorded for continued monitoring. |
| q2-trackA-positive-v2-tight-enriched-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_CI_BANK | 2026030413 | `run-q2-trackA-positive-v2tight-enriched-seed-2026030413.txt` | enriched CI-style positives included; `elliptic_template_hits=0` across listed bank entries under tightened profile | CI-style enrichment did not yet produce robust elliptic-v2 selective hits at current strict thresholds. |
| q2-trackA-perturb-v2-tight-enriched-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030411 | `run-q2-trackA-pert-v2tight-enriched-seed-2026030411.txt` | `trials=200`, `smooth_pass=162`, `elliptic_v2_surrogate_detected=0/162`, `incidents=0` | Negative-control cleanliness held in enriched pass. |

## Recommended v2 calibration profile (current)
- `--elliptic-probe-mode v2-resultant`
- `--elliptic-v2-cross-prime-count 3`
- `--elliptic-v2-min-rootcount 3`
- Keep `--max-elliptic-templates 30` for current-cost calibration runs.

Freeze note: this profile is the current Track A calibrated baseline for production exploratory runs, unless future enrichment evidence necessitates revision.

## Added block — Track A explicit-elliptic positive-bank test

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v2-tight-explicit-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030512 | `run-q2-trackA-random-v2tight-explicit-elliptic-seed-2026030512.txt` | `samples=200`, `smooth_pass=163`, `elliptic_v2_surrogate_detected=0/163`, `incidents=0` | Random negative-control remained clean under explicit-bank code path. |
| q2-trackA-positive-v2-tight-explicit-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_CI_BANK_PLUS_FACTOR | 2026030513 | `run-q2-trackA-positive-v2tight-explicit-elliptic-seed-2026030513.txt` | explicit CI/factor elliptic-engineered specials included; `elliptic_template_hits=0` across bank entries at strict thresholds | Explicit enrichment did not recover elliptic-v2 hits under current strict profile; indicates low sensitivity for current surrogate-bank pairing. |
| q2-trackA-positive-v2-tight-stronger-explicit-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_EXPLICIT_BANK_V2 | 2026030613 | `run-q2-trackA-positive-v2tight-stronger-elliptic-seed-2026030613.txt` | added square-style elliptic proxies (`engineered_elliptic_square_proxy_a/b`) plus prior CI/factor entries; still `elliptic_template_hits=0` across bank entries | Stronger explicit-positive attempt still yields zero elliptic-v2 hits at strict thresholds; further model change likely required (v3 or controlled relaxation). |
| q2-trackA-positive-v2-relax-diagnostic-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_EXPLICIT_BANK_V2 | 2026030713 | `run-q2-trackA-positive-v2relax-seed-2026030713.txt` | one-step relaxation (`cross_prime_count=2`, `min_rootcount=3`) with enriched explicit bank; `elliptic_template_hits=0` across all listed entries | Positive-only relaxation diagnostic did not recover elliptic-v2 sensitivity; suggests surrogate/model mismatch rather than threshold-only issue. |
| q2-trackA-perturb-v2-tight-explicit-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030511 | `run-q2-trackA-pert-v2tight-explicit-elliptic-seed-2026030511.txt` | `trials=200`, `smooth_pass=155`, `elliptic_v2_surrogate_detected=0/155`, `incidents=0` | Van-Luijk perturbation negative-control remained clean. |

## Added block — Track A v3 Weierstrass-plane positive-only comparison

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-positive-v2tight-v3bank-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_WEIERSTRASS_BANK | 2026030813 | `run-q2-trackA-positive-v2tight-v3bank-seed-2026030813.txt` | v2-tight on bank including explicit Weierstrass-plane quartics; only sparse non-Weierstrass proxy hit (`engineered_elliptic_square_proxy_b: elliptic_template_hits=2`), explicit Weierstrass entries remained `0` | Confirms v2 pathway does not reliably activate on explicit Weierstrass-plane constructions in this setup. |
| q2-trackA-positive-v3weierstrass-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_WEIERSTRASS_BANK | 2026030814 | `run-q2-trackA-positive-v3weierstrass-seed-2026030814.txt` | v3 mode produced selective hits on explicit Weierstrass entries (`a=-1,b=0` and `a=-2,b=3`: `elliptic_template_hits=1` each), with `0` on other listed non-Weierstrass specials | v3 prototype recovers intended positive-bank sensitivity directionally; still heuristic and not elliptic-curve certification. |

## Added block — Track A v3 spillover gate (random + van-Luijk perturbation)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v3weierstrass-gate-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026030912 | `run-q2-trackA-random-v3weierstrass-seed-2026030912.txt` | `samples=200`, `smooth_pass=166`, `elliptic_template_detected=0/166`, `incidents=0` | v3 random negative-control remained clean in this gate run. |
| q2-trackA-perturb-v3weierstrass-gate-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026030911 | `run-q2-trackA-pert-v3weierstrass-seed-2026030911.txt` | `trials=200`, `smooth_pass=156`, `elliptic_template_detected=0/156`, `incidents=0` | v3 van-Luijk perturbation negative-control remained clean in this gate run. |

## Added block — Track A v3 spillover gate hardening repeat (larger, fixed-seed)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v3weierstrass-gate-large-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026031012 | `run-q2-trackA-random-v3weierstrass-large-seed-2026031012.txt` | `samples=240`, `smooth_pass=186`, `elliptic_template_detected=0/186`, `incidents=0` | Larger random repeat remained clean in this finite v3 gate pass. |
| q2-trackA-perturb-v3weierstrass-gate-large-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026031011 | `run-q2-trackA-pert-v3weierstrass-large-seed-2026031011.txt` | `trials=240`, `smooth_pass=186`, `elliptic_template_detected=0/186`, `incidents=0`, `epsilon_proxy=1e-6` | Larger van-Luijk perturbation repeat remained clean in this finite v3 gate pass. |

## Added block — Track A v3 spillover sentinel (rotated fixed seed)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v3weierstrass-sentinel-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026031112 | `run-q2-trackA-random-v3weierstrass-sentinel-seed-2026031112.txt` | `samples=200`, `smooth_pass=168`, `elliptic_template_detected=0/168`, `incidents=0` | Rotated-seed random sentinel stayed clean in this finite v3 gate check. |
| q2-trackA-perturb-v3weierstrass-sentinel-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026031111 | `run-q2-trackA-pert-v3weierstrass-sentinel-seed-2026031111.txt` | `trials=200`, `smooth_pass=155`, `elliptic_template_detected=0/155`, `incidents=0`, `epsilon_proxy=1e-6` | Rotated-seed van-Luijk perturbation sentinel stayed clean in this finite v3 gate check. |

## Added block — Track A v3 random sentinel (post-CLI bridge fix)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v3weierstrass-sentinel2-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026031212 | `run-q2-trackA-random-v3weierstrass-sentinel2-seed-2026031212.txt` | `samples=200`, `smooth_pass=155`, `elliptic_template_detected=0/155`, `incidents=0` | Additional fixed-seed random sentinel remained clean under unchanged v3 guardrails in this finite pass. |

## Added block — Track A v3 paired perturbation sentinel (post-CLI bridge fix)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-perturb-v3weierstrass-sentinel2-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026031211 | `run-q2-trackA-pert-v3weierstrass-sentinel2-seed-2026031211.txt` | `trials=200`, `smooth_pass=160`, `line_detected=0/160`, `conic_template_detected=0/160`, `elliptic_template_detected=0/160`, `incidents=0`, `epsilon_proxy=1e-6` | Paired fixed-seed van-Luijk perturbation sentinel remained clean in all tracked heuristic channels for this finite post-fix gate pass. |

## Added block — Track A v3 positive sentinel (rotated fixed seed, post-bridge)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-positive-v3weierstrass-sentinel3-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_WEIERSTRASS_BANK | 2026031314 | `run-q2-trackA-positive-v3weierstrass-sentinel3-seed-2026031314.txt` | explicit Weierstrass entries again showed `elliptic_template_hits=1` each (`a=-1,b=0` and `a=-2,b=3`); all other listed bank entries stayed `0` in this run | Fixed-seed positive sentinel reproduced directional v3 sensitivity on explicit Weierstrass-plane constructions without broad activation across the rest of the bank; heuristic only. |

## Added block — Track A v3 random sentinel (rotated fixed seed, post-positive check)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v3weierstrass-sentinel3-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026031412 | `run-q2-trackA-random-v3weierstrass-sentinel3-seed-2026031412.txt` | `samples=200`, `smooth_pass=158`, `elliptic_template_detected=0/158`, `elliptic_v2_surrogate_detected=0/158`, `elliptic_v3_quadric_detected=0/158`, `incidents=0` | Additional rotated-seed random sentinel remained clean on elliptic channels under unchanged v3 guardrails in this finite post-positive-check pass. |

## Notes
- `elliptic_template_*` fields are heuristic surrogate template metrics from a minimal v1/v2/v3 implementation.
- v2 initial thresholds were over-permissive; tightened settings (`cross_prime_count=3`, `min_rootcount=3`) substantially improved negative-control cleanliness in calibration and follow-up blocks.
- Under current strict profile, explicit positive-bank enrichment has not yet yielded robust elliptic-v2 selective detections.
- v2-tight remains the frozen baseline; v3-weierstrass stays diagnostic/experimental despite repeated finite clean spillover sentinels.
- No Picard-rank or NL-membership inference is made from these counts.

## Added block — Track A v3 paired perturbation sentinel (rotated fixed seed, post-random sentinel3)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-perturb-v3weierstrass-sentinel3-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026031511 | `run-q2-trackA-pert-v3weierstrass-sentinel3-seed-2026031511.txt` | `trials=200`, `smooth_pass=166`, `line_detected=0/166`, `conic_template_detected=0/166`, `elliptic_template_detected=0/166`, `elliptic_v2_surrogate_detected=0/166`, `incidents=0`, `epsilon_proxy=1e-6` | Additional rotated-seed van-Luijk perturbation sentinel remained clean across tracked heuristic channels under unchanged v3 guardrails in this finite pass. |

## Added block - Track A v3 positive sentinel4 (rotated fixed seed, post-perturb sentinel3)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-positive-v3weierstrass-sentinel4-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_WEIERSTRASS_BANK | 2026031614 | `run-q2-trackA-positive-v3weierstrass-sentinel4-seed-2026031614.txt` | explicit Weierstrass entries again showed `elliptic_template_hits=1` each (`a=-1,b=0` and `a=-2,b=3`); all other listed non-Weierstrass entries stayed `0` on elliptic channel in this run | Additional rotated-seed positive sentinel reproduced directional v3 sensitivity on explicit Weierstrass-plane fixtures without broad elliptic activation across the remaining bank; heuristic only. |

## Added block — Track A v3 random sentinel4 (rotated fixed seed, post-positive sentinel4)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v3weierstrass-sentinel4-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026031712 | `run-q2-trackA-random-v3weierstrass-sentinel4-seed-2026031712.txt` | `samples=200`, `smooth_pass=165`, `line_detected=2/165`, `conic_template_detected=0/165`, `elliptic_template_detected=0/165`, `elliptic_v2_surrogate_detected=0/165`, `elliptic_v3_quadric_detected=0/165`, `incidents=0` on elliptic channels | Rotated-seed random sentinel4 remained clean on tracked elliptic channels under unchanged v3 guardrails; sparse line incidents persisted at low level in this finite scan, consistent with prior heuristic random-screen behavior. |

## Added block — Track A v3 paired perturbation sentinel4 (rotated fixed seed, post-random sentinel4)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-perturb-v3weierstrass-sentinel4-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026031811 | `run-q2-trackA-pert-v3weierstrass-sentinel4-seed-2026031811.txt` | `trials=200`, `smooth_pass=155`, `line_detected=0/155`, `conic_template_detected=0/155`, `elliptic_template_detected=0/155`, `elliptic_v2_surrogate_detected=0/155`, `incidents=0`, `epsilon_proxy=1e-6` | Rotated-seed perturbation sentinel4 remained clean across tracked heuristic channels under unchanged v3 guardrails in this bounded finite pass; v3 evidence remains diagnostic-only. |

## Added block — Track A v3 positive sentinel5 (rotated fixed seed, post-perturb sentinel4)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-positive-v3weierstrass-sentinel5-v1 | POS_CTRL_ENGINEERED_ELLIPTIC_WEIERSTRASS_BANK | 2026031914 | `run-q2-trackA-positive-v3weierstrass-sentinel5-seed-2026031914.txt` | explicit Weierstrass entries again showed `elliptic_template_hits=1` each (`a=-1,b=0` and `a=-2,b=3`); all other listed non-Weierstrass entries stayed `0` on elliptic channel in this run | Additional rotated-seed positive sentinel reproduced directional v3 sensitivity on explicit Weierstrass-plane fixtures without broad elliptic activation across the remaining bank; heuristic only. |

## Added block - Track A v3 random sentinel5 (rotated fixed seed, post-positive sentinel5)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-random-v3weierstrass-sentinel5-v1 | GEN_CTRL_RANDOM_QUARTIC_B2 | 2026032012 | `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt` | `samples=200`, `smooth_pass=161`, `line_detected=0/161`, `conic_template_detected=0/161`, `elliptic_template_detected=0/161`, `elliptic_v2_surrogate_detected=0/161`, `elliptic_v3_quadric_detected=0/161`, elliptic incidents `0` | Rotated-seed random sentinel5 remained clean on tracked elliptic channels under unchanged v3 guardrails in this bounded finite pass; sparse line incidents seen in sentinel4 did not recur here. |

## Added block — Track A v3 paired perturbation sentinel5 (rotated fixed seed, post-random sentinel5)

| block_label | family_label | seed | command_log | key_output_fields | conservative_readout |
|---|---|---:|---|---|---|
| q2-trackA-perturb-v3weierstrass-sentinel5-v1 | VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA | 2026032111 | `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt` | `trials=200`, `smooth_pass=142`, `line_detected=0/142`, `conic_template_detected=0/142`, `elliptic_template_detected=0/142`, `elliptic_v2_surrogate_detected=0/142`, incidents `0`, `epsilon_proxy=1e-6` | Rotated-seed perturbation sentinel5 remained clean across tracked heuristic channels in this bounded finite pass under unchanged v3 guardrails; v3 evidence remains diagnostic-only and v2-tight remains frozen baseline. |
