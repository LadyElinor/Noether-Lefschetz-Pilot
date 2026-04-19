# Pilot Index

This file is the orientation map for `noether-lefschetz-pilot`.
Use it to find the canonical reading order and the current status surfaces before opening older memos or run logs.

## Read this first
1. `README.md`
2. `pilot-status.md`
3. `reproducibility-manifest-v3-frozen.md`
4. `q2-definitive-summary.md`

If you only need the current frozen picture, stop there.

## Canonical file roles

### Orientation
- `README.md` — scope, boundaries, main modes, major command profiles.
- `pilot-index.md` — reading order and file-role map.
- `pilot-status.md` — current/frozen/experimental status spine.

### Frozen / canonical state
- `reproducibility-manifest-v3-frozen.md` — frozen v3 profile and acceptance gates.
- `q2-definitive-summary.md` — canonical compact results spine for Track A blocks.
- `releases/v3-frozen-2026-02-26/` — frozen release surface.

### Current result summaries
- `results-guide.md` — canonical vs specialized results navigation guide.
- `results-q2-trackA-overview.md` — initial Track A overview and calibration narrative.
- `results-q2-trackA-controls.md` — control-facing readouts.
- `results-q2-trackA-validation.md` — validation-oriented readouts.
- `nl-definitive-summary.md` — definitive summary for the earlier NL scan block.

### Core execution files
- `nl_quartic_line_sampling.py` — main finite-scan pilot.
- `q2_trackA_determinism_receipt.py` — determinism/receipt comparison helper.

### Specs / design notes
- `SPEC-q2-trackA-elliptic-knob-minimal.md`
- `SPEC-q2-trackA-elliptic-v2-resultant-surrogate.md`

### Memo layer
- `memo-guide.md` — grouped memo reading guide by purpose.
- `memo-q2-*.md` — bounded development notes for Track A evolution.
- `memo-*.md` — earlier bounded pilot notes.

Read memos only after the canonical status surfaces above.

### Raw run artifacts
- `run-*.txt`
- `batch_*`
- `validation_*`

These are evidence artifacts, not the first place to reconstruct project state.

## Recommended reading paths

### Path A: understand current frozen state fast
1. `README.md`
2. `pilot-status.md`
3. `reproducibility-manifest-v3-frozen.md`
4. `q2-definitive-summary.md`

### Path B: understand how the detector evolved
1. `README.md`
2. `results-q2-trackA-overview.md`
3. `q2-definitive-summary.md`
4. selected `memo-q2-*` files

### Path C: audit a specific claim
1. Identify the claim in `q2-definitive-summary.md` or `README.md`
2. Open the referenced `run-*.txt` artifact
3. Cross-check against `reproducibility-manifest-v3-frozen.md`
4. Check the nearest memo only if interpretation history matters

## Operating rule
If a file is not clearly current, frozen, experimental, or raw evidence, treat it as secondary until `pilot-status.md` places it.
