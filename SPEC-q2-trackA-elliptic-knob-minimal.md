# Minimal Implementation Spec — Q2 Track A Elliptic Knob

Purpose: add a minimal, auditable extension to the existing quartic scanner so Q2 Track A can run with an explicit elliptic-template knob while preserving Q1-style conservative boundaries.

## Scope (minimal)
Implement only:
1) new CLI argument,
2) deterministic template generation placeholder path,
3) per-sample/per-run summary fields,
4) no theorem-level inference logic.

Do **not** implement full elliptic-curve certification, j-invariant computation, genus proof, or NL-membership logic in this minimal pass.

---

## 1) CLI/API changes

File: `nl_quartic_line_sampling.py`

### 1.1 Add argument
- `--max-elliptic-templates` (int, default `0`)
- Help text:
  - `number of heuristic elliptic-template incidence probes (0 disables)`

Behavior:
- `0` => no elliptic probing (backward compatible with Q1 output behavior).
- `>0` => run placeholder elliptic template scan path.

### 1.2 Optional future-safe argument (stub only; optional)
- `--elliptic-template-family` default `basic`
- Values (initial): `basic`
- If omitted in minimal pass, document as deferred.

---

## 2) Data model additions

### 2.1 Per-sample fields (in-memory)
Add nullable/integer fields:
- `elliptic_template_hits`
- `elliptic_template_detected` (boolean)

Definition (heuristic):
- `elliptic_template_detected = (elliptic_template_hits > 0)`

### 2.2 Per-run aggregate fields
Add counts mirroring line/conic style:
- `elliptic_template_detected_samples`
- `elliptic_template_incidents`
- if perturbation mode: `perturbed_elliptic_template_detected`, `perturbed_elliptic_template_incidents`

All labels must include “template” to avoid implying certified elliptic-curve detection.

---

## 3) Minimal algorithm path (placeholder)

### 3.1 Deterministic template generation
Create a deterministic generator seeded by run RNG that outputs up to `max_elliptic_templates` candidate templates.

Template requirements (minimal):
- lightweight polynomial-incidence surrogate only,
- integer coefficients,
- deterministic under seed.

### 3.2 Incidence probe
For each quartic and each template, run a bounded heuristic incidence predicate (analogous in spirit to current conic-template pathway).

Constraints:
- no symbolic genus proof,
- no heavy CAS dependency,
- keep runtime bounded and predictable.

### 3.3 Output semantics
If predicate passes, increment `elliptic_template_hits`.

Required wording in logs/results:
- “elliptic-template heuristic incidence”
- “non-certifying finite scan”

Forbidden wording:
- “found elliptic curve” (without template qualifier)
- any Picard/NL inference.

---

## 4) Logging and report format updates

### 4.1 Console output
Add fields alongside existing line/conic metrics, e.g.:
- random mode summary: `elliptic_template_detected_samples=X/Y`, `elliptic_template_incidents=Z`
- perturbation mode summary: `perturbed_elliptic_template_detected=A/B`, `perturbed_elliptic_template_incidents=C`

### 4.2 Result markdown rows
In future Q2 result docs, include columns:
- `elliptic_template_detected`
- `elliptic_template_incidents`

And include inferential-limit sentence:
> Elliptic-template flags are heuristic template incidents only; they do not certify existence of embedded elliptic curves.

---

## 5) Backward compatibility

- Existing commands must run unchanged when `--max-elliptic-templates` is omitted.
- Existing output fields for Q1 flows remain present.
- New metrics appear as zeros or are omitted only when knob is 0 (prefer explicit zero for audit clarity).

---

## 6) Test plan (minimal)

Add/extend lightweight tests (or smoke checks):

1. **CLI parsing test**
- `--max-elliptic-templates 0` and `>0` parse correctly.

2. **Determinism test**
- same seed + same params => same elliptic-template incident counts.

3. **No-op compatibility test**
- with `--max-elliptic-templates 0`, run summaries match pre-feature behavior except optional explicit zero fields.

4. **Output field presence test**
- with nonzero knob, summary contains elliptic-template metrics.

---

## 7) Suggested first-run Q2 command set (after implementation)

```powershell
python nl_quartic_line_sampling.py --mode random --samples 120 --seed 2026030102 --coeff-bound 2 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-random-seed-2026030102.txt

python nl_quartic_line_sampling.py --mode positive-control --seed 2026030103 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 --include-determinantal | Tee-Object -FilePath run-q2-trackA-positive-seed-2026030103.txt

python nl_quartic_line_sampling.py --mode perturbation --seed 2026030101 --perturb-trials 140 --perturb-noise-bound 1 --perturb-noise-scale 1000000 --perturbation-baseline van_luijk_exact_2007 --point-bound 1 --max-deterministic-lines 180 --random-line-probes 80 --max-conic-templates 96 --max-elliptic-templates 30 --smooth-points-per-prime 160 --smooth-primes 5,7,11,13,17,19 | Tee-Object -FilePath run-q2-trackA-pert-seed-2026030101.txt
```

---

## 8) Acceptance criteria

- Feature merged with default-off behavior.
- Deterministic output verified.
- Q2 prereg command lines become runnable as written.
- Documentation updated with explicit non-claims and template-only semantics.
