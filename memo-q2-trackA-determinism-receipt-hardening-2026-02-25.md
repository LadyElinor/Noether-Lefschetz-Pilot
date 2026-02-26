# Memo — Q2 Track A determinism receipt hardening increment (2026-02-25)

## Objective
Make one concrete calibration/hardening improvement for Q2 Track A by converting prior same-seed perturbation determinism checks into a reproducible, hash-based receipt workflow.

## Improvement implemented
Added helper script:
- `q2_trackA_determinism_receipt.py`

What it does (operational check only):
- compares two run-output files,
- computes SHA256 for each file,
- reports byte-level identity verdict,
- reports text identity verdict,
- emits key summary counters when present.

## Validation run (bounded)
Receipt generated from existing same-seed perturbation reruns:
- input A: `run-q2-trackA-determinism-pert-seed-2026022517-pass1.txt`
- input B: `run-q2-trackA-determinism-pert-seed-2026022517-pass2.txt`
- output receipt: `run-q2-trackA-determinism-receipt-pert-seed-2026022517.txt`

Key readout:
- `sha256_a == sha256_b` (`ef3bda4993ccc67d9113eb1dc947d029bdc7bce654bdd58610495aa3e19fd3da`)
- `byte_identical_sha256: true`
- `text_identical: true`

## Conservative interpretation
- This strengthens implementation-level determinism auditing by adding a reproducible byte-hash receipt layer.
- Evidence remains finite and operational only; no mathematical/geometric claim (Picard rank or NL membership) is implied.
