# Results Guide

This file distinguishes canonical result summaries from specialized result notes and raw evidence-adjacent summaries inside `noether-lefschetz-pilot`.

## Use rule
Read result files in this order:
1. `q2-definitive-summary.md`
2. `nl-definitive-summary.md`
3. only then the specialized `results-*.md` files relevant to your question

If you start in a specialized result note, you can easily mistake a local calibration episode for the current canonical state.

## Canonical results spines

### 1. `q2-definitive-summary.md`
Role:
- canonical compact results spine for Q2 Track A
- best starting point for current Track A interpretation

Use when:
- you want the official compact readout of Track A evolution
- you need block labels, seeds, command logs, and conservative readouts in one place

### 2. `nl-definitive-summary.md`
Role:
- canonical compact results spine for the earlier NL finite-scan block

Use when:
- you want the pre-Track-A definitive scan summary
- you are auditing the earlier line/conic-centered stage of the project

## Specialized result notes
These are useful, but they are scoped artifacts rather than the first canonical entrypoint.

### A. Track A orientation / calibration notes
- `results-q2-trackA-overview.md`
- `results-q2-trackA-controls.md`
- `results-q2-trackA-validation.md`

Use when:
- you need a narrower view of Track A calibration behavior
- you want controls-focused or validation-focused slices rather than the whole Q2 summary

### B. Early pilot scan notes
- `results-initial.md`
- `results-expanded.md`
- `results-large-batch.md`
- `results-stratified.md`
- `results-positive-control.md`
- `results-perturbation.md`
- `results-perturbation-next.md`

Use when:
- you are reconstructing early pilot evolution
- you want stage-specific context before the definitive summary layer stabilized

### C. Specialized method / contrast notes
- `results-conic-enhanced.md`
- `results-conic-expanded-bank.md`
- `results-coverage-extension.md`
- `results-determinantal-contrast.md`
- `results-vanluijk-exact-perturbation.md`
- `results-vanluijk-stability-grid.md`

Use when:
- you are auditing a specific enhancement, contrast, or perturbation exercise
- you need the narrower rationale behind a block summarized elsewhere

## Evidence-adjacent status
Many `results-*.md` files sit between summary and evidence:
- more interpretive than raw `run-*.txt`
- less canonical than `q2-definitive-summary.md` or `nl-definitive-summary.md`

Treat them as scoped explanatory artifacts, not as automatic statements of current project status.

## Recommended reading paths

### Path A: current Track A state
1. `pilot-status.md`
2. `q2-definitive-summary.md`
3. `results-q2-trackA-overview.md` only if more narrative context is needed

### Path B: earlier NL scan state
1. `pilot-status.md`
2. `nl-definitive-summary.md`
3. specialized early `results-*` files only if you need stage-by-stage detail

### Path C: audit a specific phenomenon
1. start with the relevant definitive summary
2. find the matching specialized `results-*` note if it exists
3. then inspect the referenced `run-*.txt` artifact

## Operating rule
If two result files appear to conflict, prefer:
1. the frozen/current status surfaces,
2. then the relevant definitive summary,
3. then the specialized result note,
4. then the raw evidence artifact.
