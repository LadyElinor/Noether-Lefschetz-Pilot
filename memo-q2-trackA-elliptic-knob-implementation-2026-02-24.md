# Memo — Q2 Track A elliptic knob minimal implementation (2026-02-24)

Implemented in `nl_quartic_line_sampling.py`:

- Added CLI flag:
  - `--max-elliptic-templates` (default `0`; disabled by default)
- Added deterministic surrogate template bank path:
  - `candidate_elliptic_templates(...)`
- Added heuristic predicate wrapper:
  - `elliptic_template_contained(...)`
- Added summary metrics in random/stratified/perturbation/positive-control output:
  - `*_elliptic_template_*` fields (detected counts + incidents)
- Preserved backward compatibility:
  - Existing commands run unchanged.
  - Default behavior remains effectively Q1-compatible with explicit zero elliptic-template counts.

Smoke checks run:
- `python nl_quartic_line_sampling.py --help`
- `python nl_quartic_line_sampling.py --mode random --samples 3 --seed 1 --max-elliptic-templates 5`
- `python nl_quartic_line_sampling.py --mode perturbation --seed 2 --perturb-trials 5 --max-elliptic-templates 0`

Boundary reminder:
- Elliptic-template metrics are **heuristic surrogate template incidents only**.
- No elliptic-curve certification, Picard-rank inference, or NL-membership inference is made.
