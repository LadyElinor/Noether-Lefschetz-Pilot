# Memo — Conic Round (2026-02-23)

## 1) Source-anchored theorem vs heuristic tiers

### Theorem-level context (external; not proved by this script)
- **[THM-Q4-VG-PIC1]** Very general quartic surfaces in \(\mathbf{P}^3\) have Picard rank 1 (classical Noether–Lefschetz consequence).
- **[THM-NL4-PROPER-CU]** The degree-4 Noether–Lefschetz locus is proper and presented as a countable union of proper subloci/components in the period/Hodge framing.
- **[CTX-DET-CODIM1]** Determinantal-style quartics are standardly discussed as lying in special Noether–Lefschetz-type families, including codimension-1 component context in classical treatments.

**Source-lock status:** theorem statements are treated as standard literature facts, but this repo currently does not pin exact bibliographic metadata (edition/page-level locking partial). Keep citations conservative until source pinning is completed.

### Exact checks implemented here
- Exact symbolic restriction test for candidate **lines**.
- Exact symbolic restriction test for a small bank of parameterized **conic templates**.
- Exact check for the fixed test conic \(x=s^2, y=st, z=t^2, w=0\) in the forced-conic construction.

### Heuristic-only layers
- Mod-\(p\) sampled smoothness screen (not full singularity/discriminant computation).
- Finite bank incidence rates (lines + conic templates) under seeded sampling.
- Proxy perturbation rates near a local baseline (not exact van Luijk polynomial).

## 2) Conic-enhanced probing added
- Script now includes a lightweight conic-template bank (`--max-conic-templates`, stdlib-only).
- Templates are intentionally cheap and incomplete (coordinate-plane style parameterized conics).
- Reproducibility maintained via deterministic seed flow.

## 3) Perturbation extension (proxy baseline only)
- Re-ran perturbation mode with small noise controls (`noise_bound=1` and `2`).
- Reported detection rates **after smoothness-screen pass filtering**.
- Label kept strict: `proxy_baseline_not_van_luijk_exact`.

## 4) Blockers
- Exact van Luijk polynomial not pinned locally.
- Bibliographic source-locking for theorem tags is partial.
- Conic coverage remains deliberately incomplete; no global conic search.

## 5) Next steps
1. Add pinned bibliography file with exact references for [THM-Q4-VG-PIC1], [THM-NL4-PROPER-CU], [CTX-DET-CODIM1].
2. If exact van Luijk polynomial is supplied, add separate exact-baseline perturbation mode (kept disjoint from proxy mode).
3. Optionally add multi-seed replication for conic-template rates.
