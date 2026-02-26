# Q2 Track A — Controls Note (Initial)

## Control families used

- `GEN_CTRL_RANDOM_QUARTIC_B2`
  - Random quartics with bounded coefficients (`coeff_bound=2`), post sampled smoothness screen.

- `POS_CTRL_ENGINEERED_ELLIPTIC_QUARTIC_PROXYBANK`
  - Current initial bank reuses known special constructions from Q1 (engineered line, forced conic, Fermat, determinantal-style proxy) as scanner-sensitivity references while elliptic-template channel is bootstrapped.

- `VAN_LUIJK_EXACT_2007_H0_Q2_TRACKA`
  - Exact-baseline perturbation block (`van_luijk_exact_2007`) with deterministic tiny-noise arithmetic.

## Why this control setup is acceptable for initial block
- It preserves continuity with Q1 reliability checks.
- It verifies backward compatibility and deterministic behavior after adding elliptic-template metrics.
- It avoids premature theorem-level interpretation while elliptic-specific construction bank is still being expanded.

## Limitation
- Positive controls are not yet elliptic-specific certified families; they are scanner calibration controls.
- CI-style enriched entries (`engineered_elliptic_ci_q1q2_mix_a/b`) were added, but under tightened v2 thresholds they have not yet produced robust elliptic-selective hits.
- Therefore, sparse/zero elliptic-template incidents are not interpreted as negative evidence about elliptic-incidence prevalence.
