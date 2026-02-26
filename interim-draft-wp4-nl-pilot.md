# A Heuristic Incidence Scanner for Quartic K3 Surfaces: Calibrated v3-Weierstrass Results and Sparse Random-Mapping Evidence

**Status:** Interim draft (computational note style)  
**Project:** Noether–Lefschetz Pilot (WP4 synthesis)  
**Scope:** Finite, reproducible heuristic probing of algebraic-cycle incidence on smooth quartic surfaces in $\mathbb{P}^3$.

---

## Abstract
We present a reproducible computational pilot for incidence-style detection of algebraic cycles on quartic K3 surfaces, with emphasis on disciplined claim boundaries. The scanner combines line/conic template channels with an elliptic proxy channel (v3-Weierstrass), calibrated against engineered positive controls and guardrail negatives. Across random sweeps up to 10,000 samples (7,978 analyzed after smoothness screening), we observe zero elliptic detections under frozen v3 settings, giving a Wilson 95% upper bound of approximately 0.048% for detected elliptic incidence at current probe depth. In contrast, lower-complexity channels (line/conic) remain active, yielding an empirical codimension-style gradient consistent with theoretical expectations. We explicitly do **not** claim Picard-rank certification, NL-membership completeness, or Hodge-theorem-level proof.

---

## 1. Problem Framing and Claim Discipline
The Noether–Lefschetz (NL) locus is theoretically rich, but computationally difficult to probe in finite runs without overclaiming. This pilot targets a narrower objective:

1. build a reproducible incidence scanner,
2. calibrate sensitivity/specificity via explicit controls,
3. map finite-sample sparsity under fixed random protocols,
4. maintain strict separation between heuristic detections and theorem-level statements.

### Not Claimed (hard boundary)
- Non-detection does **not** certify $\rho=1$.
- Detections are heuristic incidence signals, not full NL-component proof.
- Random scans here are finite-template and finite-prime probes, not exhaustive geometric classification.

---

## 2. Method Overview
### 2.1 Tiered elliptic proxy (v3-Weierstrass)
- **Tier 1:** modular candidate screening over selected primes.
- **Tier 2:** exact ideal-membership style linear checks via SymPy (matrix-form linear systems in implementation).
- **Tier 3:** genus-consistency proxy via adjunction-style checks (heuristic, non-proof).

### 2.2 Reproducibility invariants
- Fixed seeds for all reported runs.
- Frozen parameter profiles for cross-batch comparability.
- Command-level artifact logging to transcript files.

---

## 3. Calibration and Mapping Results
## 3.1 Control and batch summary
| Phase | Analyzed N | Elliptic Hits k | Rate | Interpretation |
|---|---:|---:|---:|---|
| Calibration (positive) | 2 | 2 | 100% | Engineered specials detected under aligned v3 scoring. |
| Guardrail (negative) | 160 | 0 | 0.00% | No guardrail false positives in baseline set. |
| Batch-S | 421 | 0 | 0.00% | Initial random sparsity indication. |
| Batch-M | 1,985 | 0 | 0.00% | Elliptic channel quiet; line channel active. |
| Batch-L | 7,978 | 0 | 0.00% | Deep random sweep; elliptic channel remains quiet. |

### 3.2 Wilson upper bounds (95% CI, k=0)
| Batch | n analyzed | Upper bound | Approx ceiling |
|---|---:|---:|---:|
| S | 421 | 0.0090 | 1 in 111 |
| M | 1,985 | 0.0019 | 1 in 526 |
| L | 7,978 | 0.00048 | 1 in 2,083 |

### 3.3 Channel gradient
In Batch-L, lower-complexity channels remain active (line/conic detections present) while elliptic detections remain absent under the current probe. This line→conic→elliptic sparsity gradient is a central empirical observation of this pilot.

---

## 4. Interpretation
### What the results support
- A stable, reproducible scanner with strong guardrail behavior on tested negatives.
- Empirical evidence that detected elliptic incidence is highly sparse under current finite probe depth.
- A practical measurement of computational difficulty for random elliptic hits in this setup.

### What they do not support
- Any disproof of NL-density in the theoretical sense.
- Any universal decision procedure for Hodge-type questions.
- Any claim that non-detected random samples are NL-generic in a formal algebro-geometric sense.

---

## 5. Reproducibility Snapshot
Primary executable: `nl_quartic_line_sampling.py`  
Frozen Batch-L run profile (executed):

```bash
python nl_quartic_line_sampling.py \
  --mode random \
  --samples 10000 \
  --seed 202603203 \
  --elliptic-probe-mode v3-weierstrass \
  --max-quadric-templates 20 \
  --max-elliptic-templates 30 \
  --v3-prime-sample 31 \
  --v3-min-points 15 \
  --smooth-primes 5,7,11,13,17 \
  --smooth-points-per-prime 160 \
  --output-json > batch_l_transcript.log 2>&1
```

Key artifact: `batch_l_transcript.log`

---

## 6. Next Validation Step (pre-freeze)
Before declaring v3 profile frozen for downstream work, run a final two-command acceptance gate:
1. Positive acceptance check (engineered aligned positives).
2. Guardrail acceptance check (Van-Luijk-style baseline with extended perturbation count).

If both pass at current thresholds, freeze v3 settings and shift to report polish + optional targeted model-expansion experiments.

---

## References (short list)
- Voisin, *Hodge Theory and Complex Algebraic Geometry*.
- Hartshorne, *Algebraic Geometry*.
- Huybrechts, *Lectures on K3 Surfaces*.
- Wilson (1927), score interval for sparse-proportion confidence bounds.
