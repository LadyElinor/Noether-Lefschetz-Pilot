# Memo — Q2 Track A determinism receipt perturbation key-coverage hardening (2026-02-25)

## Scope
One bounded calibration/hardening increment for strict determinism receipt policy in perturbation mode.

## Improvement implemented
Updated `q2_trackA_determinism_receipt.py` tracked summary key list to include perturbation-run fields already present in logs:
- `base_smoothness_screen`
- `gate_guardrail_threshold`

Rationale:
- prior strict check (`--require-min-shared-keys 7`) failed on perturbation sentinel artifacts with only 5 shared tracked keys,
- while deterministic replay itself already passed (`byte_identical_sha256: true`, `text_identical: true`).

## Validation step completed
Re-ran strict receipt check on existing same-seed perturbation replay pair:
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt`
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111-rerun.txt`

Receipt artifact:
- `run-q2-trackA-determinism-receipt-pert-v3-sentinel5-min7-require-identical-recalibrated-seed-2026032111.txt`

Strict flags:
- `--require-identical`
- `--require-key-match`
- `--require-min-shared-keys 7`

## Observed readout
- `byte_identical_sha256: true`
- `text_identical: true`
- `shared_summary_key_count: 7`
- `shared_summary_key_match: true`
- `require_identical_check: pass`
- `require_min_shared_keys_check: pass`
- `require_key_match_check: pass`

## Conservative interpretation
- This increment improves strict-policy usability for perturbation sentinel receipts by aligning tracked key coverage with fields actually emitted by the current run logs.
- Result remains finite implementation-level calibration evidence only; no geometric, Picard-rank, or Noether–Lefschetz claim is implied.
