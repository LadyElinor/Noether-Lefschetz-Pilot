# Memo — Q2 Track A determinism receipt hardening (`--require-identical`) (2026-02-25)

## Bounded increment completed
Added a conservative CI-friendly hardening switch to the determinism receipt helper:
- file: `q2_trackA_determinism_receipt.py`
- new flag: `--require-identical`
- behavior: returns nonzero exit (`1`) if compared outputs are not text-identical; prints `require_identical_check: pass|fail`.

This enables a stricter guardrail for automated regression checks without changing default behavior.

## Validation step
Ran the hardened path on the existing same-seed random determinism pair:
- input A: `run-q2-trackA-determinism-random-seed-2026022516-pass1.txt`
- input B: `run-q2-trackA-determinism-random-seed-2026022516-pass2.txt`
- receipt: `run-q2-trackA-determinism-receipt-random-seed-2026022516-require-identical.txt`

Key readout:
- `byte_identical_sha256: true`
- `text_identical: true`
- `require_identical_check: pass`

## Conservative interpretation
- This is an implementation-level robustness improvement for deterministic replay auditing.
- It does not add any geometric/NL/Picard-rank claim; evidence remains finite and operational.
