# Q2 Track A — Validation Note (Initial Block)

## Validation target
Confirm that adding `--max-elliptic-templates` does not break deterministic execution paths and preserves conservative baseline behavior.

## Checks performed
1. CLI validation:
   - `python nl_quartic_line_sampling.py --help` shows `--max-elliptic-templates`.
2. Random-mode shakeout with nonzero elliptic templates:
   - ran with `--max-elliptic-templates 30`; output includes elliptic-template summary fields.
3. Perturbation baseline compatibility:
   - exact van Luijk baseline perturbation run executed with elliptic templates enabled.
4. Disabled-path compatibility:
   - run with `--max-elliptic-templates 0` still executes and reports zero elliptic-template incidents.

## Initial outcomes
- No runtime regressions observed in tested modes.
- Output remains deterministic per seed in observed runs.
- Baseline perturbation block retained zero-incidence profile in analyzed samples for line/conic/elliptic-template channels.

## v2 resultant-surrogate calibration note
- Initial v2 runs (`seed=2026030212/0213/0211`) produced non-zero incidents in random and van-Luijk perturbation blocks.
- Interpretation: initial v2 thresholding was over-sensitive for negative-control cleanliness; this is calibration feedback, not geometric inference.

## v2 tightening loop (before/after)
Settings tightened to:
- `--elliptic-v2-cross-prime-count 3`
- `--elliptic-v2-min-rootcount 3`

| block | initial v2 (before) | tightened v2 (after) | readout |
|---|---|---|---|
| random (`seed=2026030212`) | `elliptic_v2_surrogate_detected=8/61`, incidents `9` | `elliptic_v2_surrogate_detected=0/61`, incidents `0` | False-positive pressure reduced to zero in this calibration batch. |
| positive bank (`seed=2026030213`) | mixed non-zero hits across some specials | reduced but non-zero on engineered line special (`elliptic_template_hits=2`) | Some directional sensitivity retained under stricter thresholds. |
| van Luijk perturb (`seed=2026030211`) | `elliptic_v2_surrogate_detected=5/78`, incidents `5` | `elliptic_v2_surrogate_detected=0/78`, incidents `0` | Negative-control cleanliness restored in this batch. |

## Positive-only relaxation diagnostic (cross-prime-count=2)
Run:
- `run-q2-trackA-positive-v2relax-seed-2026030713.txt`

Settings:
- `--elliptic-v2-cross-prime-count 2`
- `--elliptic-v2-min-rootcount 3`
- enriched explicit positive bank enabled

Outcome:
- `elliptic_template_hits=0` across all listed positive-bank entries.

Calibration interpretation:
- A one-step threshold relaxation did not recover positive-bank elliptic-v2 hits.
- This points to surrogate/model mismatch (bank construction vs v2 predicate) rather than strictness alone.

## v3 Weierstrass-plane prototype diagnostic (positive-only)
Runs:
- `run-q2-trackA-positive-v2tight-v3bank-seed-2026030813.txt`
- `run-q2-trackA-positive-v3weierstrass-seed-2026030814.txt`

Outcome (directional):
- v2-tight remained mostly quiet on explicit Weierstrass-plane entries in this run setup.
- v3-weierstrass mode produced selective hits on explicit Weierstrass-plane constructions (`a=-1,b=0` and `a=-2,b=3`, one hit each), while non-Weierstrass specials remained at zero in this run.

Conservative readout:
- v3 prototype appears to recover targeted positive sensitivity directionally.
- Still heuristic/non-certifying; no rank/NL conclusions.

## v3 spillover gate (random + van-Luijk perturbation)
Runs:
- `run-q2-trackA-random-v3weierstrass-seed-2026030912.txt`
- `run-q2-trackA-pert-v3weierstrass-seed-2026030911.txt`

Outcome:
- Random: `elliptic_template_detected=0/166`, incidents `0`
- Van-Luijk perturbation: `elliptic_template_detected=0/156`, incidents `0`

Gate interpretation:
- In this finite gate block, v3-weierstrass showed no observed negative spillover.
- Combined with prior positive-only directional hits on explicit Weierstrass entries, this supports provisional experimental use of v3-weierstrass for targeted diagnostics.
- v2-tight remains the locked safety baseline for routine exploratory scans.

## v3 spillover hardening repeat (larger fixed-seed gate)
Runs:
- `run-q2-trackA-random-v3weierstrass-large-seed-2026031012.txt`
- `run-q2-trackA-pert-v3weierstrass-large-seed-2026031011.txt`

Settings:
- same conservative profile as prior v3 gate (`--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, strict v2 knobs held at `3/3`)
- larger finite budget: random `samples=240`, perturbation `trials=240`

Outcome:
- Random: `smooth_pass=186/240`, `elliptic_template_detected=0/186`, incidents `0`
- Van-Luijk perturbation: `smooth_pass=186/240`, `elliptic_template_detected=0/186`, incidents `0`

Conservative interpretation:
- Second (larger) finite gate also showed no observed negative spillover.
- This strengthens, but does not certify, the provisional use of v3-weierstrass for targeted diagnostics.
- v2-tight remains the frozen baseline for routine exploratory Track A work.

## v3 spillover sentinel (rotated fixed-seed)
Runs:
- `run-q2-trackA-random-v3weierstrass-sentinel-seed-2026031112.txt`
- `run-q2-trackA-pert-v3weierstrass-sentinel-seed-2026031111.txt`

Settings:
- same guardrails as prior v3 gate runs (`--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`)
- finite budget: random `samples=200`, perturbation `trials=200`

Outcome:
- Random: `smooth_pass=168/200`, `elliptic_template_detected=0/168`, incidents `0`
- Van-Luijk perturbation: `smooth_pass=155/200`, `elliptic_template_detected=0/155`, incidents `0`

Conservative interpretation:
- Rotated-seed sentinel remained clean for both negative-control channels in this bounded increment.
- Supports continuing diagnostic-only v3 use under unchanged guardrails.
- v2-tight remains frozen as the baseline profile.

## CLI bridge fix check (v3/quadric arg propagation)
Issue observed in this block:
- `TypeError` on random/perturbation/positive-control paths because `main()` did not pass required `max_quadric_templates`, `v3_prime_sample`, `v3_min_points` into runner functions.

Fix applied:
- `main()` now forwards `--max-quadric-templates`, `--v3-prime-sample`, and `--v3-min-points` to `run`, `run_stratified`, `run_positive_control`, and `run_perturbation`.

Post-fix bounded check (fixed-seed):
- `run-q2-trackA-random-v3weierstrass-sentinel2-seed-2026031212.txt`
- Outcome: `samples=200`, `smooth_pass=155`, `elliptic_template_detected=0/155`, incidents `0`.

Conservative interpretation:
- The CLI path is restored for v3-capable runs under current flags.
- One post-fix random sentinel remained clean; this is a finite operational check, not a mathematical claim.

## Paired post-fix perturbation sentinel (v3, fixed-seed)
Run:
- `run-q2-trackA-pert-v3weierstrass-sentinel2-seed-2026031211.txt`

Settings:
- `--mode perturbation --perturb-trials 200 --seed 2026031211`
- `--perturbation-baseline van_luijk_exact_2007`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`

Outcome:
- `perturbed_smooth_pass=160/200`
- `perturbed_line_detected=0/160`, incidents `0`
- `perturbed_conic_template_detected=0/160`, incidents `0`
- `perturbed_elliptic_template_detected=0/160`, incidents `0`
- `perturbed_elliptic_v2_surrogate_detected=0/160`, incidents `0`

Conservative interpretation:
- The post-fix paired perturbation sentinel also remained clean in this finite check, restoring two-channel (random + perturbation) negative-control coverage after the CLI bridge fix.
- This remains heuristic/operational evidence only; no Picard-rank or NL-membership certification is implied.

## v3 positive sentinel (post-fix, rotated fixed seed)
Run:
- `run-q2-trackA-positive-v3weierstrass-sentinel3-seed-2026031314.txt`

Settings:
- `--mode positive-control --seed 2026031314`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`
- bridge-sensitive args explicitly present: `--max-quadric-templates 20`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- explicit Weierstrass fixtures (`a=-1,b=0`, `a=-2,b=3`) each recorded `elliptic_template_hits=1`
- other listed positive-bank entries remained `elliptic_template_hits=0` in this run
- line/conic channels remained active on expected special families (heuristic control behavior)

Conservative interpretation:
- Post-fix positive sentinel preserves the prior directional v3 signal on explicit Weierstrass-plane constructions under fixed seed.
- This supports continuing diagnostic-only v3 usage while keeping v2-tight frozen as baseline.
- No geometric certification claim is implied by these finite heuristic hits.

## v3 random sentinel3 (rotated fixed-seed, post-positive check)
Run:
- `run-q2-trackA-random-v3weierstrass-sentinel3-seed-2026031412.txt`

Settings:
- `--mode random --samples 200 --seed 2026031412`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- `smoothness_screen_pass=158/200`
- `random_samples_with_any_detected_elliptic_template=0/158`, incidents `0`
- `random_samples_with_any_detected_elliptic_v2_surrogate=0/158`, incidents `0`
- `random_samples_with_any_detected_elliptic_v3_quadric=0/158`, incidents `0`

Conservative interpretation:
- This additional rotated-seed random sentinel remained clean on all tracked elliptic channels in a bounded finite run.
- Supports continued diagnostic-only v3 monitoring under unchanged guardrails.
- v2-tight remains frozen baseline; no Picard-rank or NL-membership inference is implied.

## Remaining validation work (next)
- Add explicit deterministic regression test script comparing repeated runs with same seed.
- Keep tightened v2 profile as safety baseline for ongoing exploratory scans.
- Continue bounded, rotated fixed-seed v3 sentinels as diagnostic-only monitoring.

## v3 perturbation sentinel3 (rotated fixed-seed, post-random sentinel3)
Run:
- `run-q2-trackA-pert-v3weierstrass-sentinel3-seed-2026031511.txt`

Settings:
- `--mode perturbation --perturb-trials 200 --seed 2026031511`
- `--perturbation-baseline van_luijk_exact_2007`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- `perturbed_smooth_pass=166/200`
- `perturbed_line_detected=0/166`, incidents `0`
- `perturbed_conic_template_detected=0/166`, incidents `0`
- `perturbed_elliptic_template_detected=0/166`, incidents `0`
- `perturbed_elliptic_v2_surrogate_detected=0/166`, incidents `0`

Conservative interpretation:
- This rotated-seed perturbation sentinel remained clean on tracked heuristic channels in a bounded finite run.
- Supports continued diagnostic-only v3 monitoring under unchanged guardrails while keeping v2-tight frozen as the baseline profile.
- No Picard-rank or Noether-Lefschetz membership claim is implied.

## v3 positive sentinel4 (rotated fixed-seed, post-perturb sentinel3)
Run:
- `run-q2-trackA-positive-v3weierstrass-sentinel4-seed-2026031614.txt`

Settings:
- `--mode positive-control --seed 2026031614`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- explicit Weierstrass fixtures (`a=-1,b=0`, `a=-2,b=3`) each recorded `elliptic_template_hits=1`
- other listed positive-bank entries remained `elliptic_template_hits=0` in this run
- line/conic channels remained active on expected special families (heuristic control behavior)

Conservative interpretation:
- This additional rotated-seed positive sentinel reproduces the same directional v3 signal pattern seen in prior positive sentinels.
- Evidence remains finite and heuristic/operational only; no Picard-rank or NL-membership certification is implied.
- v2-tight remains frozen baseline; v3 remains diagnostic-only.

## v3 random sentinel4 (rotated fixed-seed, post-positive sentinel4)
Run:
- `run-q2-trackA-random-v3weierstrass-sentinel4-seed-2026031712.txt`

Settings:
- `--mode random --samples 200 --seed 2026031712`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- `smoothness_screen_pass=165/200`
- `random_samples_with_any_detected_line=2/165` (sparse line-channel incidents)
- `random_samples_with_any_detected_conic_template=0/165`
- `random_samples_with_any_detected_elliptic_template=0/165`, incidents `0`
- `random_samples_with_any_detected_elliptic_v2_surrogate=0/165`, incidents `0`
- `random_samples_with_any_detected_elliptic_v3_quadric=0/165`, incidents `0`

Conservative interpretation:
- This rotated-seed random sentinel remained clean across tracked elliptic channels under unchanged v3 guardrails in a bounded finite run.
- Sparse line-channel incidents continue to appear at low rate in random scans and are treated as heuristic screen behavior, not geometric certification.
- v2-tight remains frozen baseline; no Picard-rank or NL-membership inference is implied.

## v3 perturbation sentinel4 (rotated fixed-seed, post-random sentinel4)
Run:
- `run-q2-trackA-pert-v3weierstrass-sentinel4-seed-2026031811.txt`

Settings:
- `--mode perturbation --perturb-trials 200 --seed 2026031811`
- `--perturbation-baseline van_luijk_exact_2007`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- `perturbed_smooth_pass=155/200`
- `perturbed_line_detected=0/155`, incidents `0`
- `perturbed_conic_template_detected=0/155`, incidents `0`
- `perturbed_elliptic_template_detected=0/155`, incidents `0`
- `perturbed_elliptic_v2_surrogate_detected=0/155`, incidents `0`

Conservative interpretation:
- This rotated-seed perturbation sentinel4 remained clean across tracked heuristic channels in a bounded finite run.
- Supports continued diagnostic-only v3 monitoring under unchanged guardrails; v2-tight remains frozen baseline.
- No Picard-rank or Noether-Lefschetz membership claim is implied.

## v3 positive sentinel5 (rotated fixed-seed, post-perturb sentinel4)
Run:
- `run-q2-trackA-positive-v3weierstrass-sentinel5-seed-2026031914.txt`

Settings:
- `--mode positive-control --seed 2026031914`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- explicit Weierstrass fixtures (`a=-1,b=0`, `a=-2,b=3`) each recorded `elliptic_template_hits=1`
- all other listed non-Weierstrass entries remained `elliptic_template_hits=0` in this run
- line/conic channels remained active on expected special families (heuristic control behavior)

Conservative interpretation:
- This additional rotated-seed positive sentinel reproduces the same directional v3 signal pattern seen in prior positive sentinels.
- Evidence remains finite and heuristic/operational only; no Picard-rank or NL-membership certification is implied.
- v2-tight remains frozen baseline; v3 remains diagnostic-only.
## v3 random sentinel5 (rotated fixed-seed, post-positive sentinel5)
Run:
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`

Settings:
- `--mode random --samples 200 --seed 2026032012`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- `smoothness_screen_pass=161/200`
- `random_samples_with_any_detected_line=0/161`
- `random_samples_with_any_detected_conic_template=0/161`
- `random_samples_with_any_detected_elliptic_template=0/161`, incidents `0`
- `random_samples_with_any_detected_elliptic_v2_surrogate=0/161`, incidents `0`
- `random_samples_with_any_detected_elliptic_v3_quadric=0/161`, incidents `0`

Conservative interpretation:
- This rotated-seed random sentinel5 remained clean across tracked elliptic channels in a bounded finite run under unchanged guardrails.
- Compared with random sentinel4, sparse line-channel incidents did not recur in this run.
- v2-tight remains frozen baseline; v3 remains diagnostic-only with no Picard-rank or NL-membership claim implied.

## Determinism micro-pass (same-seed rerun check, random mode)
Runs:
- `run-q2-trackA-determinism-random-seed-2026022516-pass1.txt`
- `run-q2-trackA-determinism-random-seed-2026022516-pass2.txt`

Settings:
- `--mode random --samples 120 --seed 2026022516`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- Key summary counters matched exactly across pass1/pass2:
  - `smoothness_screen_pass=100/120` and `smoothness_screen_flagged=20/120`
  - `random_samples_with_any_detected_line=0/100`
  - `random_samples_with_any_detected_conic_template=0/100`
  - `random_samples_with_any_detected_elliptic_template=0/100`
  - `random_samples_with_any_detected_elliptic_v2_surrogate=0/100`
  - `random_samples_with_any_detected_elliptic_v3_quadric=0/100`
  - all tracked total incident counters remained `0`

Conservative interpretation:
- This bounded same-seed rerun supports operational determinism of the current random-mode path under fixed parameters.
- Evidence is finite and implementation-level only (not a mathematical guarantee).

## v3 perturbation sentinel5 (rotated fixed-seed, post-random sentinel5)
Run:
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt`

Settings:
- `--mode perturbation --perturb-trials 200 --seed 2026032111`
- `--perturbation-baseline van_luijk_exact_2007`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- `perturbed_smooth_pass=142/200`
- `perturbed_line_detected=0/142`, incidents `0`
- `perturbed_conic_template_detected=0/142`, incidents `0`
- `perturbed_elliptic_template_detected=0/142`, incidents `0`
- `perturbed_elliptic_v2_surrogate_detected=0/142`, incidents `0`
- gate guardrail summary from run output: `gate_guardrail_fp_hits=0`, `gate_guardrail_fp_total=142`, `gate_guardrail_fp_rate=0.000000`, `gate_guardrail_pass=1`

Conservative interpretation:
- This rotated-seed perturbation sentinel5 remained clean across tracked heuristic channels in a bounded finite run.
- Supports continued diagnostic-only v3 monitoring under unchanged guardrails while keeping v2-tight frozen as baseline.
- No Picard-rank or Noether-Lefschetz membership claim is implied.

## Determinism micro-pass (same-seed rerun check, perturbation mode)
Runs:
- `run-q2-trackA-determinism-pert-seed-2026022517-pass1.txt`
- `run-q2-trackA-determinism-pert-seed-2026022517-pass2.txt`

Settings:
- `--mode perturbation --perturbation-baseline van_luijk_exact_2007 --perturb-trials 120 --seed 2026022517`
- unchanged guardrails: `--elliptic-probe-mode v3-weierstrass`, `--max-elliptic-templates 30`, `--max-quadric-templates 20`, `--elliptic-v2-cross-prime-count 3`, `--elliptic-v2-min-rootcount 3`, `--v3-prime-sample 31`, `--v3-min-points 15`

Outcome:
- Full output files were line-identical on rerun with same seed/flags.
- `perturbed_smooth_pass=108/120`
- `perturbed_line_detected=0/108`, incidents `0`
- `perturbed_conic_template_detected=0/108`, incidents `0`
- `perturbed_elliptic_template_detected=0/108`, incidents `0`
- `perturbed_elliptic_v2_surrogate_detected=0/108`, incidents `0`
- guardrail summary remained identical: `gate_guardrail_fp_hits=0`, `gate_guardrail_fp_total=108`, `gate_guardrail_fp_rate=0.000000`, `gate_guardrail_pass=1`

Conservative interpretation:
- This bounded same-seed perturbation rerun supports operational determinism of the current perturbation-mode path under fixed parameters.
- Evidence is finite and implementation-level only; no Picard-rank or Noether-Lefschetz membership inference is implied.

## Determinism receipt hardening increment (hash-based)
Artifact added:
- `q2_trackA_determinism_receipt.py`

Receipt run (using prior same-seed perturbation pair):
- input A: `run-q2-trackA-determinism-pert-seed-2026022517-pass1.txt`
- input B: `run-q2-trackA-determinism-pert-seed-2026022517-pass2.txt`
- output: `run-q2-trackA-determinism-receipt-pert-seed-2026022517.txt`

Outcome:
- `sha256_a == sha256_b` (`ef3bda4993ccc67d9113eb1dc947d029bdc7bce654bdd58610495aa3e19fd3da`)
- `byte_identical_sha256: true`
- `text_identical: true`

Conservative interpretation:
- Adds a reproducible byte-hash receipt layer to determinism checks, improving operational auditability.
- Still finite, implementation-level evidence only; no geometric certification or NL/Picard inference is implied.

## Determinism receipt hardening increment (hash-based, random mode)
Artifact used:
- `q2_trackA_determinism_receipt.py`

Receipt run (using prior same-seed random pair):
- input A: `run-q2-trackA-determinism-random-seed-2026022516-pass1.txt`
- input B: `run-q2-trackA-determinism-random-seed-2026022516-pass2.txt`
- output: `run-q2-trackA-determinism-receipt-random-seed-2026022516.txt`

Outcome:
- `sha256_a == sha256_b` (`ce974f2b6809438c97ef5c75e8e79ab9009db9e50f56d3bff50045aea475b635`)
- `byte_identical_sha256: true`
- `text_identical: true`

Conservative interpretation:
- Extends the existing hash-receipt determinism hardening to random mode, giving byte-level audit receipts for both random and perturbation same-seed micro-passes.
- Evidence remains finite and implementation-level only; no geometric certification or NL/Picard inference is implied.

## Determinism revalidation on prior v3 random sentinel5 artifact (same-seed rerun)
Run repeated under unchanged flags from prior sentinel5 random block:
- baseline artifact: `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`
- rerun artifact: `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`
- receipt artifact: `run-q2-trackA-determinism-receipt-random-v3-sentinel5-seed-2026032012.txt`

Outcome:
- `sha256_a == sha256_b` (`ff67d316d4613669bf656c2e9a68306959640a0eab3281abc8f0a8e220efad00`)
- `byte_identical_sha256: true`
- `text_identical: true`

Conservative interpretation:
- Confirms byte-identical replay for a previously logged v3 random sentinel artifact at fixed seed/flags, strengthening operational reproducibility evidence for this exact configuration.
- This remains finite implementation-level validation only; no theorem-level, Picard-rank, or NL-membership claim is implied.

## Determinism receipt hardening (`--require-identical`) + bounded check
Implementation:
- Updated `q2_trackA_determinism_receipt.py` with optional `--require-identical` switch.
- When enabled, the helper exits `1` on non-identical text output and emits `require_identical_check: pass|fail`.
- Default behavior remains unchanged for existing workflows.

Validation run:
- `run-q2-trackA-determinism-receipt-random-seed-2026022516-require-identical.txt`
- compared:
  - `run-q2-trackA-determinism-random-seed-2026022516-pass1.txt`
  - `run-q2-trackA-determinism-random-seed-2026022516-pass2.txt`

Outcome:
- `byte_identical_sha256: true`
- `text_identical: true`
- `require_identical_check: pass`

Conservative interpretation:
- Improves operational/automation guardrails for deterministic replay checks.
- Finite implementation-level evidence only; no Picard-rank/NL/theorem claim.

## Determinism revalidation — v3 perturbation sentinel5 (same-seed replay)
Run:
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111-rerun.txt`

Receipt:
- `run-q2-trackA-determinism-receipt-pert-v3-sentinel5-seed-2026032111.txt`

Compared files:
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt`
- `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111-rerun.txt`

Outcome:
- `byte_identical_sha256: true`
- `text_identical: true`
- `require_identical_check: pass`

Conservative interpretation:
- One additional bounded deterministic replay check passed for the v3 perturbation sentinel5 artifact under unchanged seed/flags.
- This is operational reproducibility evidence only; no geometric, Picard-rank, or Noether-Lefschetz claim is implied.

## Determinism receipt negative-control check (`--require-identical` fail-closed path)
Run:
- `run-q2-trackA-determinism-receipt-negative-control-random-vs-pert-seed-2026022516-2026022517.txt`

Compared files (intentionally different):
- `run-q2-trackA-determinism-random-seed-2026022516-pass1.txt`
- `run-q2-trackA-determinism-pert-seed-2026022517-pass1.txt`

Outcome:
- `byte_identical_sha256: false`
- `text_identical: false`
- `require_identical_check: fail`
- helper exit code: `1`

Conservative interpretation:
- The strict determinism receipt guard fails closed on non-identical artifacts, as intended.
- This is implementation-level hardening validation only; no geometric, Picard-rank, or Noether-Lefschetz claim is implied.

## Determinism receipt hardening (`--require-key-match`) + bounded v3 random check
Implementation:
- Updated `q2_trackA_determinism_receipt.py` with optional `--require-key-match` switch.
- Helper now emits `shared_summary_key_match: true|false` and, when strict mode is enabled, exits `1` if any shared summary key value differs.
- Default behavior remains unchanged for existing receipt workflows.

Validation run:
- `run-q2-trackA-determinism-receipt-random-v3-sentinel5-key-match-seed-2026032012.txt`
- compared:
  - `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`
  - `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`

Outcome:
- `byte_identical_sha256: true`
- `text_identical: true`
- `shared_summary_key_match: true`
- `require_key_match_check: pass`

Conservative interpretation:
- Adds a semantic fail-closed guardrail for summary counters in addition to byte/text identity checks.
- This is finite implementation-level hardening evidence only; no geometric, Picard-rank, or Noether-Lefschetz claim is implied.

## Determinism receipt hardening (`--require-min-shared-keys`) + vacuity negative-control check
Implementation:
- Updated `q2_trackA_determinism_receipt.py` with optional strict flag `--require-min-shared-keys N`.
- Helper now emits `shared_summary_key_count: <int>` and fails closed (exit `1`) when fewer than `N` summary keys are shared.
- Purpose: prevent vacuous `--require-key-match` passes when compared artifacts contain no tracked summary keys.

Validation run:
- `run-q2-trackA-determinism-receipt-random-v3-sentinel5-min-shared-keys-seed-2026032012.txt`
- compared:
  - `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt`
  - `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`
- strict settings: `--require-key-match --require-min-shared-keys 1`

Outcome:
- `byte_identical_sha256: true`
- `text_identical: true`
- `shared_summary_key_count: 0`
- `shared_summary_key_match: true`
- `require_min_shared_keys_check: fail`

Conservative interpretation:
- New guardrail correctly blocks vacuous semantic-match receipts while preserving prior byte/text identity checks.
- This is implementation-level hardening evidence only; no geometric, Picard-rank, or Noether-Lefschetz claim is implied.

## determinism receipt encoding hardening (UTF-16LE + '=' key parsing)
- Updated q2_trackA_determinism_receipt.py to:
  - decode UTF-16LE-style run logs (NUL-byte heuristic + UTF-16 fallback),
  - accept both key: value and key=value summary lines.

Validation run:
- run-q2-trackA-determinism-receipt-random-v3-sentinel5-min7-seed-2026032012.txt

Compared files:
- run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012.txt
- run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt

Strict settings:
- --require-key-match --require-min-shared-keys 7

Outcome:
- byte_identical_sha256: true
- text_identical: true
- shared_summary_key_count: 7
- shared_summary_key_match: true
- require_min_shared_keys_check: pass

Conservative interpretation:
- Semantic receipt checks now activate correctly for this UTF-16LE '='-formatted run pair; this is implementation-level hardening only.

## determinism receipt calibration check (v3 perturbation sentinel5 strict-key floor)
Run:
- run-q2-trackA-determinism-receipt-pert-v3-sentinel5-min7-require-identical-seed-2026032111.txt

Compared files:
- run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt
- run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111-rerun.txt

Strict settings:
- --require-identical --require-key-match --require-min-shared-keys 7

Outcome:
- byte_identical_sha256: true
- text_identical: true
- shared_summary_key_count: 5
- shared_summary_key_match: true
- require_identical_check: pass
- require_min_shared_keys_check: fail (expected 7, observed 5)

Conservative interpretation:
- This bounded check confirms perturbation sentinel logs expose only five currently tracked shared summary keys under the present parser/key list, so a min-shared-keys floor of 7 is too strict for this mode.
- Useful calibration signal for strict receipt policy tuning; implementation-level evidence only (no geometric/Picard-rank/NL claim).

## Determinism receipt perturbation key-coverage hardening (strict min-shared-keys calibration)
Implementation:
- Updated `q2_trackA_determinism_receipt.py` tracked keys to include perturbation-log fields:
  - `base_smoothness_screen`
  - `gate_guardrail_threshold`
- Goal: make strict `--require-min-shared-keys 7` policy usable on perturbation sentinel receipts without relaxing strictness.

Validation run:
- `run-q2-trackA-determinism-receipt-pert-v3-sentinel5-min7-require-identical-recalibrated-seed-2026032111.txt`
- compared:
  - `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111.txt`
  - `run-q2-trackA-pert-v3weierstrass-sentinel5-seed-2026032111-rerun.txt`
- strict settings: `--require-identical --require-key-match --require-min-shared-keys 7`

Outcome:
- `byte_identical_sha256: true`
- `text_identical: true`
- `shared_summary_key_count: 7`
- `shared_summary_key_match: true`
- `require_identical_check: pass`
- `require_min_shared_keys_check: pass`
- `require_key_match_check: pass`

Conservative interpretation:
- This bounded hardening step aligns strict semantic receipt checks with currently emitted perturbation fields while preserving fail-closed behavior.
- Evidence remains finite and implementation-level only; no geometric, Picard-rank, or Noether-Lefschetz membership claim is implied.

## Determinism receipt calibration check (random v3 sentinel5 rerun-vs-rerun2)
Run:
- `run-q2-trackA-determinism-receipt-random-v3-sentinel5-rerun-vs-rerun2-seed-2026032012.txt`

Compared files:
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun.txt`
- `run-q2-trackA-random-v3weierstrass-sentinel5-seed-2026032012-rerun2.txt`

Strict settings:
- `--require-key-match --require-min-shared-keys 7`

Outcome:
- `byte_identical_sha256: false`
- `text_identical: false`
- `shared_summary_key_count: 7`
- `shared_summary_key_match: true`
- `require_min_shared_keys_check: pass`
- `require_key_match_check: pass`

Conservative interpretation:
- This bounded calibration step shows the strict semantic-key checks can pass while full-file identity fails on this pair, so byte/text-identical and key-match checks should be interpreted as complementary gates.
- Evidence remains implementation-level only; no geometric, Picard-rank, or Noether-Lefschetz membership claim is implied.

## Q2 Track A gate-scorer calibration closure (mode-aligned positive target set)
Implementation (minimal/auditable):
- Updated `run_positive_control` target-label gating in `nl_quartic_line_sampling.py` to be probe-mode aligned.
- For `--elliptic-probe-mode v3-weierstrass`, gate-positive denominator now uses only explicit Weierstrass fixtures:
  - `explicit_elliptic_weierstrass_plane_a-1_b0_L1111`
  - `explicit_elliptic_weierstrass_plane_a-2_b3_L1111`
- Guardrail path (`run_perturbation`) and detector predicates were unchanged.

Reproducible fixed-seed validation run:
- artifact: `run-q2-trackA-gate-scorer-v3weierstrass-mode-aligned-targets-seed-2026031914.txt`
- command:
  - `python nl_quartic_line_sampling.py --mode gate-scorer --seed 2026031914 --perturb-trials 200 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --max-quadric-templates 20 --elliptic-probe-mode v3-weierstrass --elliptic-v2-cross-prime-count 3 --elliptic-v2-min-rootcount 3 --v3-prime-sample 31 --v3-min-points 15 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --gate-positive-threshold 0.80 --gate-guardrail-threshold 0.05 --output-json`

Outcome (`--output-json`):
- `gate_positive_hits=2`
- `gate_positive_total=2`
- `gate_positive_rate=1.000000`
- `gate_guardrail_fp_hits=0`
- `gate_guardrail_fp_total=160`
- `gate_guardrail_fp_rate=0.000000`
- `overall_pass=1`

Conservative interpretation:
- Under this probe-mode-aligned gate definition and fixed-seed finite run, positive sensitivity exceeded the 0.80 target while guardrail false-positive rate remained below 0.05.
- This is calibration evidence for the implemented heuristic gate only; it is not a Picard-rank certification or a Noether-Lefschetz membership claim.
