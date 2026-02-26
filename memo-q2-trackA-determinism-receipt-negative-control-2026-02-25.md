# Memo — Q2 Track A determinism receipt negative-control check (2026-02-25)

## Bounded increment completed
Ran one explicit negative-control validation of the new `--require-identical` guard in `q2_trackA_determinism_receipt.py`.

## Validation step
Compared two intentionally different same-day artifacts:
- A: `run-q2-trackA-determinism-random-seed-2026022516-pass1.txt`
- B: `run-q2-trackA-determinism-pert-seed-2026022517-pass1.txt`
- receipt: `run-q2-trackA-determinism-receipt-negative-control-random-vs-pert-seed-2026022516-2026022517.txt`

Observed output:
- `byte_identical_sha256: false`
- `text_identical: false`
- `require_identical_check: fail`
- process exit code: `1`

## Conservative interpretation
- The strict guardrail path fails closed as intended on non-identical artifacts.
- This is an implementation-level hardening/validation step only; it does not add any geometric/NL/Picard-rank claim.
