# Initial Run Results (2026-02-23)

## Command
```bash
python nl_quartic_line_sampling.py --samples 40 --seed 20260223 --coeff-bound 2
```

Environment: Python 3.13.5

## Output summary
- Candidate monomials: 35 (quartic terms in 4 variables)
- Candidate lines checked per quartic: 45
- Special sanity case (`F=x*G3+y*H3`): detector reported 14 contained lines in this finite bank (confirms positive-path functionality)
- Random sample runs: `0/40` quartics with any detected contained line
- Total random detected line incidents: `0`

## Interpretation (conservative)
- The detector behaves as expected on an engineered positive case.
- For this small coefficient window and finite candidate-line bank, random quartics produced no detected line incidences.
- This supports use as a **screening heuristic only**.
- It is **not** evidence of Picard rank, not a proof of genericity, and not an NL-locus computation.

## Next practical extensions
1. Increase sample count and coefficient ranges.
2. Expand candidate line bank (carefully controlling duplicates/projective equivalence).
3. Add engineered families with known geometric constraints for calibration.
