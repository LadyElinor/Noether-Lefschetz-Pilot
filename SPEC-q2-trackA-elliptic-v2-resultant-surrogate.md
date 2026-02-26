# Spec — Q2 Track A Elliptic v2 (Resultant-Based Surrogate)

Goal: upgrade elliptic incidence probing from v1 template reuse to a stronger but still lightweight/heuristic surrogate.

## Scope
Implement a new optional path that evaluates quartic restrictions against a small parameterized genus-1-inspired family and uses resultant/discriminant-style sanity checks as **heuristic flags**.

This remains non-certifying:
- no proof of embedded elliptic curve existence,
- no genus certification theorem pipeline,
- no Picard/NL inference.

---

## 1) CLI additions

In `nl_quartic_line_sampling.py`:

- `--elliptic-probe-mode` with values:
  - `v1-template` (default; current behavior)
  - `v2-resultant` (new surrogate)
- Keep existing `--max-elliptic-templates` knob for candidate count.

Compatibility:
- default behavior unchanged.

---

## 2) v2 conceptual probe

For each candidate parameter tuple in a fixed seeded bank:
1. Build a low-cost parametric map into \(\mathbf{P}^3\) (binary-form based, degree-controlled).
2. Restrict quartic \(F\) along that map to a binary form (or pair of forms) with parameter dependence.
3. Compute lightweight symbolic invariants (resultant/discriminant proxy checks) over integers/mod small primes.
4. Flag incident when invariants satisfy pre-registered heuristic criteria.

Output label must say: `elliptic_resultant_surrogate_hits`.

---

## 3) Heuristic flag criteria (pre-registered)

A candidate is counted as a v2 surrogate hit only if all hold:
- restriction is not identically zero for trivial reasons,
- resultant/discriminant proxy indicates a non-generic algebraic relation,
- simple degeneracy filters pass (avoid obvious singular/line/conic collapse cases).

These are screening criteria only; not a genus proof.

---

## 4) Data and output fields

Add fields (alongside existing v1 fields):
- per-sample: `elliptic_v2_surrogate_hits`
- per-run:
  - `elliptic_v2_surrogate_detected_samples`
  - `elliptic_v2_surrogate_incidents`

When mode is `v1-template`, v2 fields should be explicit zeros for audit clarity.

---

## 5) Validation plan

1. Determinism check:
- same seed and params => identical v2 counts.

2. Negative-control check:
- van Luijk perturbation baseline should remain low/zero under initial small budget.

3. Special-control contrast:
- positive bank should show at least nontrivial contrast potential vs random in pilot-scale runs (if not, revise candidate bank design before scaling).

4. Runtime bound:
- ensure v2 mode stays practical for `samples ~ 100` on current environment.

---

## 6) Initial command set (after implementation)

```powershell
python nl_quartic_line_sampling.py --mode random --samples 120 --seed 2026030202 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v2-resultant --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-v2-seed-2026030202.txt

python nl_quartic_line_sampling.py --mode positive-control --seed 2026030203 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v2-resultant --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --include-determinantal | Tee-Object -FilePath run-q2-trackA-positive-v2-seed-2026030203.txt

python nl_quartic_line_sampling.py --mode perturbation --seed 2026030201 --perturb-trials 120 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --elliptic-probe-mode v2-resultant --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-v2-seed-2026030201.txt
```

---

## 7) Required wording in reports

- “elliptic v2 resultant-based surrogate incidents”
- “finite heuristic screen, non-certifying”
- “no Picard-rank / NL-membership inference from these hits”

