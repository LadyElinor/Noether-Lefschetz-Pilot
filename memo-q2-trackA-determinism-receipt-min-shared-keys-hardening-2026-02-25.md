# Memo — Q2 Track A determinism receipt min-shared-keys hardening (2026-02-25)

## Scope
Implementation-level hardening for deterministic receipt checks in `q2_trackA_determinism_receipt.py`.

## Increment completed
- Added optional strict flag:
  - `--require-min-shared-keys N`
- Added explicit metric output:
  - `shared_summary_key_count: <int>`
- New behavior under strict mode:
  - exits nonzero if `shared_summary_key_count < N`.

Rationale: avoid vacuous `--require-key-match` passes when no summary keys are present in either file.

## Validation step (bounded)
Run artifact:
- `run-q2-trackA-determinism-receipt-random-v3-sentinel5-min-shared-keys-seed-2026032012.txt`

Compared files:
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`

Command intent:
- strict key-match plus `--require-min-shared-keys 1`.

Observed readout:
- `byte_identical_sha256: true`
- `text_identical: true`
- `shared_summary_key_count: 0`
- `shared_summary_key_match: true`
- `require_min_shared_keys_check: fail`

## Conservative interpretation
- Hardening behaves as intended: receipt now fails closed when key-match would otherwise be vacuous due to zero shared keys.
- This is finite implementation/validation evidence only; no geometric, Picard-rank, or Noether–Lefschetz claim is implied.
