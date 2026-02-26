# Memo — Q2 Track A determinism receipt calibration (random v3 sentinel5 rerun-vs-rerun2)

Date: 2026-02-25
Scope: `hodge-conjecture/noether-lefschetz-pilot`

## Increment completed
Ran one additional strict determinism-receipt check comparing the two existing same-seed random sentinel5 replay artifacts:

- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun.txt`
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`

Command profile:
- `--require-key-match --require-min-shared-keys 7`

New receipt artifact:
- `run-q2-trackA-determinism-receipt-random-v3-sentinel5-rerun-vs-rerun2-seed-2026032012.txt`

## Key readout
- `byte_identical_sha256: false`
- `text_identical: false`
- `shared_summary_key_count: 7`
- `shared_summary_key_match: true`
- `require_min_shared_keys_check: pass`
- `require_key_match_check: pass`

## Conservative interpretation
This bounded check shows a useful calibration split: full-file determinism is not present for this pair, while tracked summary counters remain matched under strict key-coverage policy. This is implementation-level validation only and does not imply any geometric/Picard-rank/Noether–Lefschetz claim.
