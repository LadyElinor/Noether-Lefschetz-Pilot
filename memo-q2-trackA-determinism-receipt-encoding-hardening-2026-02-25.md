# Memo — Q2 Track A determinism receipt encoding hardening (2026-02-25)

## Scope
Implementation-level hardening for deterministic receipt extraction in `q2_trackA_determinism_receipt.py`.

## Increment completed
- Hardened log decoding in receipt helper:
  - added `decode_text()` with UTF-16-aware fallback when NUL bytes are present.
- Hardened key parsing format:
  - summary key extraction now accepts both `key: value` and `key=value` lines.

Rationale: many existing run artifacts are UTF-16LE and use `=` separators, which previously produced vacuous `shared_summary_key_count=0` despite real summary counters being present.

## Validation step (bounded)
Run artifact:
- `run-q2-trackA-determinism-receipt-random-v3-sentinel5-min7-seed-2026032012.txt`

Compared files:
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`

Strict settings:
- `--require-key-match --require-min-shared-keys 7`

Observed readout:
- `byte_identical_sha256: true`
- `text_identical: true`
- `shared_summary_key_count: 7`
- `shared_summary_key_match: true`
- `require_min_shared_keys_check: pass`

## Conservative interpretation
- Receipt semantic checks now correctly engage on UTF-16LE/equal-sign run logs and no longer fail vacuously in this tested pair.
- This is finite implementation/validation evidence only; no geometric, Picard-rank, or Noether–Lefschetz claim is implied.
