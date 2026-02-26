## Executive Summary: Noether-Lefschetz Pilot (v3-Weierstrass)

**Project:** WP4 – Synthesis & Final Reporting  
**Scope:** Heuristic detection of algebraic cycles on smooth quartic surfaces in $\mathbb{P}^3$.  
**Status:** **Experimental Phase Complete.**

### 1. Core Methodology & Invariants
The pilot utilized a tiered geometric probe (v3-Weierstrass) to detect the presence of genus-1, degree-4 algebraic curves (elliptic quartics) on smooth K3 surfaces.

- **Tier 1:** Modular point-screening over $\mathbb{F}_p$ for base-locus candidates.
- **Tier 2:** Exact ideal-membership verification ($F \in \langle Q_1, Q_2 \rangle$) via SymPy linear system solvers (35x20 matrix).
- **Tier 3:** Genus-consistency proxy via adjunction-style checks (heuristic; non-proof).

---

### 2. Final Metric Synthesis

| Phase | $N$ (Samples) | Elliptic Hits ($k$) | Success Rate | Significance |
| --- | --- | --- | --- | --- |
| **Calibration (Pos)** | 2 | 2 | 100% | Sensitivity to engineered specials confirmed. |
| **Guardrail (Neg)** | 160 | 0 | 0.00% | Specificity against $\rho=1$ baseline confirmed. |
| **Batch-S** | 421 | 0 | 0.00% | Initial sparsity check ($<0.9\%$ density). |
| **Batch-M** | 1,985 | 0 | 0.00% | Active line-channel (6 hits) validates probe wakefulness. |
| **Batch-L** | 7,978 | 0 | 0.00% | **Deep-space scan.** Density ceiling pushed to $<0.05\%$. |

---

### 3. Wilson Density Bounds
Using the Wilson Score Interval (95% CI) for sparse-hit regimes ($k=0$):

| Batch | Analyzed ($n$) | Upper Bound (95% CI) | Density Ceiling (approx.) |
| --- | --- | --- | --- |
| **Batch-S** | 421 | 0.0090 | 1 in 111 |
| **Batch-M** | 1,985 | 0.0019 | 1 in 526 |
| **Batch-L** | 7,978 | **0.00048** | **1 in 2,083** |

---

### 4. Claims & Limitations

> #### ⚠️ Not Claimed
> - **Picard rank:** Non-detection does **not** certify $\rho=1$; it only indicates no detections within the finite template bank used here.
> - **NL completeness:** This scan does not enumerate all components of the Noether-Lefschetz locus (e.g., non-complete-intersection curves or higher-degree embeddings).
> - **Existence proofs:** Detections are heuristic signals, not formal proofs of the Hodge Conjecture.

#### What this supports
- **Computational sparsity:** Under this probe depth and random sampling protocol, elliptic detections are empirically very rare ($<0.05\%$ at 95% confidence).
- **Instrument discipline:** The v3 probe separates engineered Hodge-active controls from guardrail baselines with zero guardrail false positives in the tested set.

#### What this does not support
- It does **not** disprove theoretical density of the Noether-Lefschetz locus.
- It does **not** provide a universal decision procedure for the Hodge Conjecture in higher dimensions.

---

### 5. Reproducibility Appendix

**Primary artifact:** `nl_quartic_line_sampling.py` (v3-Weierstrass branch)  
**Calibration seed:** `2026031914`

**Batch-L execution command (frozen run):**

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
