# Memo Guide

This file groups the memo layer in `noether-lefschetz-pilot` by purpose so readers do not have to reconstruct intent from filenames alone.

## Use rule
Read memos only after:
1. `README.md`
2. `pilot-status.md`
3. `reproducibility-manifest-v3-frozen.md`
4. `q2-definitive-summary.md`

Memos are interpretation-history aids, not the canonical current state.

## Memo families

### A. Early pilot expansion / next-step memos
Use these to understand the earliest bounded expansion of the pilot before the heavier Q2 Track A layer.

Files:
- `memo-conic-round-2026-02-23.md`
- `memo-expanded-2026-02-23.md`
- `memo-next-2026-02-23.md`
- `memo-next2-2026-02-23.md`

Read when:
- you want the early rationale behind expanded line/conic scanning
- you are auditing how the pilot moved from initial exploration into more structured execution

### B. Track A implementation / calibration memos
Use these to understand how the elliptic-related Track A layer was added and tuned.

Files:
- `memo-q2-trackA-elliptic-knob-implementation-2026-02-24.md`
- `memo-q2-trackA-v2-implementation-and-calibration-2026-02-24.md`
- `memo-q2-trackA-v2-tightening-2026-02-25.md`
- `memo-q2-trackA-v2-relax-positive-2026-03-07.md`
- `memo-q2-trackA-v3-design-positive-2026-03-08.md`

Read when:
- you want to understand why v2 was introduced
- you need the rationale for tightening/relaxing thresholds
- you are tracing the move from v2 to v3-weierstrass logic

### C. Spillover / sentinel evolution memos
Use these to track the bounded experimental progression of v3 guardrails across random, positive, and perturbation sentinel passes.

Files:
- `memo-q2-trackA-v3-spillover-gate-2026-03-09.md`
- `memo-q2-trackA-v3-spillover-gate-large-2026-03-10.md`
- `memo-q2-trackA-v3-sentinel-rotated-seed-2026-03-11.md`
- `memo-q2-trackA-v3-sentinel2-and-cli-bridge-2026-03-12.md`
- `memo-q2-trackA-v3-paired-perturb-sentinel2-2026-03-12.md`
- `memo-q2-trackA-v3-positive-sentinel3-2026-03-13.md`
- `memo-q2-trackA-v3-random-sentinel3-2026-03-14.md`
- `memo-q2-trackA-v3-perturb-sentinel3-2026-02-25.md`
- `memo-q2-trackA-v3-positive-sentinel4-2026-02-25.md`
- `memo-q2-trackA-v3-random-sentinel4-2026-02-25.md`
- `memo-q2-trackA-v3-perturb-sentinel4-2026-02-25.md`
- `memo-q2-trackA-v3-positive-sentinel5-2026-02-25.md`
- `memo-q2-trackA-v3-random-sentinel5-2026-02-25.md`
- `memo-q2-trackA-v3-perturb-sentinel5-2026-02-25.md`

Read when:
- you want the evolution of spillover checks and fixed-seed sentinels
- you are auditing whether v3 stayed clean on negative-control style surfaces while retaining positive-bank sensitivity

### D. Determinism / receipt hardening memos
Use these to understand the determinism-comparison and receipt-hardening layer rather than the detector behavior itself.

Files:
- `memo-q2-trackA-determinism-micro-pass-2026-02-25.md`
- `memo-q2-trackA-determinism-perturb-micro-pass-2026-02-25.md`
- `memo-q2-trackA-determinism-v3-random-sentinel5-rerun-2026-02-25.md`
- `memo-q2-trackA-determinism-pert-v3-sentinel5-rerun-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-hardening-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-encoding-hardening-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-keymatch-hardening-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-min-shared-keys-hardening-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-negative-control-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-random-hardening-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-random-v3-sentinel5-rerun-vs-rerun2-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-pert-v3-key-coverage-hardening-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-pert-v3-min7-calibration-2026-02-25.md`
- `memo-q2-trackA-determinism-receipt-require-identical-2026-02-25.md`

Read when:
- you are auditing reproducibility guarantees
- you care about receipt semantics, key matching, shared-key thresholds, or rerun comparison policy
- you are debugging whether a difference is detector drift or receipt-policy drift

## Suggested memo reading paths

### Minimal memo path
1. `memo-q2-trackA-v2-implementation-and-calibration-2026-02-24.md`
2. `memo-q2-trackA-v3-design-positive-2026-03-08.md`
3. `memo-q2-trackA-v3-spillover-gate-2026-03-09.md`
4. `memo-q2-trackA-determinism-receipt-hardening-2026-02-25.md`

### Detector-evolution path
1. family B
2. family C

### Reproducibility-audit path
1. family D
2. matching `run-*` artifacts
3. `q2_trackA_determinism_receipt.py`

## Operating rule
Do not infer current project state from the last memo you opened. Use memos to explain how the project got here, not to override `pilot-status.md` or the frozen manifest.
