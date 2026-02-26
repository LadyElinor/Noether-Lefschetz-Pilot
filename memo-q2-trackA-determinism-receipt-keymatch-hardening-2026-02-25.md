# Memo — Q2 Track A determinism receipt key-match hardening (2026-02-25)

## Scope
Conservative implementation hardening for deterministic replay checks in `noether-lefschetz-pilot`.

## Increment completed
- Extended `q2_trackA_determinism_receipt.py` with strict `--require-key-match` mode.
- Added explicit receipt field `shared_summary_key_match: true|false`.
- Strict mode now exits non-zero if any shared summary key differs between compared artifacts.

## Bounded validation
- Receipt: `run-q2-trackA-determinism-receipt-random-v3-sentinel5-key-match-seed-2026032012.txt`
- Compared same-seed replay pair:
  - `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`
  - `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`
- Observed: byte hash match, text match, shared summary key match, strict check pass.

## Claim boundary
Operational reproducibility hardening only (finite run evidence). No theorem-level, Picard-rank, or NL-membership claim.
