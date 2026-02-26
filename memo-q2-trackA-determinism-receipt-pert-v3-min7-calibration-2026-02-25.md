# Memo — Q2 Track A determinism receipt perturbation min-shared-keys calibration (2026-02-25)

## Scope
Bounded calibration/hardening validation for strict determinism receipt policy in perturbation mode.

## Validation step completed
Executed strict receipt check on an existing same-seed v3 perturbation replay pair:
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt`
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111-rerun.txt`

Receipt artifact:
- `run-q2-trackA-determinism-receipt-pert-v3-sentinel5-min7-require-identical-seed-2026032111.txt`

Strict flags used:
- `--require-identical`
- `--require-key-match`
- `--require-min-shared-keys 7`

## Observed readout
- `byte_identical_sha256: true`
- `text_identical: true`
- `shared_summary_key_count: 5`
- `shared_summary_key_match: true`
- `require_identical_check: pass`
- `require_min_shared_keys_check: fail` (`expected=7`, `observed=5`)

## Conservative interpretation
- Deterministic replay itself remains intact (byte/text identical).
- This strict-policy check fails because perturbation sentinel logs currently expose only five tracked shared summary keys under the present parser/key list.
- Practical calibration signal: a global `--require-min-shared-keys 7` floor is over-strict for this perturbation-mode artifact class unless parser/key coverage is expanded.
- Finite implementation-level evidence only; no geometric, Picard-rank, or Noether–Lefschetz claim is implied.
