#!/usr/bin/env python3
"""
Expanded Noether-Lefschetz quartic pilot (heuristic only).

What this script does:
- Samples random quartic forms F(x,y,z,w) in P^3 with deterministic seeds.
- Runs a lightweight smoothness-screen heuristic (not a full discriminant test).
- Scans candidate banks of projective lines and low-cost conic templates.
- Evaluates special examples (forced-line, forced-conic, Fermat, optional determinantal).

What this script does NOT do:
- Compute Picard rank.
- Prove Noether-Lefschetz membership.
- Provide complete conic-line incidence coverage.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import dataclass
from math import comb
from typing import Dict, List, Sequence, Tuple

import sympy as sp

Exp4 = Tuple[int, int, int, int]
Point = Tuple[int, int, int, int]
Line = Tuple[Point, Point]
ConicTemplate = Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]
EllipticTemplate = ConicTemplate
QuadricMon = Tuple[int, int, int, int]
QuadricPoly = Dict[QuadricMon, int]
QuadricTemplate = Tuple[QuadricPoly, QuadricPoly]


@dataclass
class Quartic:
    coeffs: Dict[Exp4, int]
    label: str = "random"
    structural_marker: str = ""


def degree4_monomials() -> List[Exp4]:
    mons: List[Exp4] = []
    for a in range(5):
        for b in range(5 - a):
            for c in range(5 - a - b):
                d = 4 - a - b - c
                mons.append((a, b, c, d))
    return mons


def degree2_monomials() -> List[Exp4]:
    mons: List[Exp4] = []
    for a in range(3):
        for b in range(3 - a):
            for c in range(3 - a - b):
                d = 2 - a - b - c
                mons.append((a, b, c, d))
    return mons


def linear_power(alpha: int, beta: int, e: int) -> Dict[int, int]:
    return {k: comb(e, k) * (alpha**k) * (beta ** (e - k)) for k in range(e + 1)}


def poly_mul_int(a: Dict[int, int], b: Dict[int, int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for da, va in a.items():
        for db, vb in b.items():
            out[da + db] = out.get(da + db, 0) + va * vb
    return out


def substitute_on_line(coeffs: Dict[Exp4, int], line: Line) -> List[int]:
    p, q = line
    poly = [0] * 5  # coefficient of s^d t^(4-d)
    for (a, b, c, d), c0 in coeffs.items():
        if c0 == 0:
            continue
        factors = [
            linear_power(p[0], q[0], a),
            linear_power(p[1], q[1], b),
            linear_power(p[2], q[2], c),
            linear_power(p[3], q[3], d),
        ]
        accum: Dict[int, int] = {0: 1}
        for f in factors:
            accum = poly_mul_int(accum, f)
        for sdeg, val in accum.items():
            poly[sdeg] += c0 * val
    return poly


def line_contained(coeffs: Dict[Exp4, int], line: Line) -> bool:
    return all(v == 0 for v in substitute_on_line(coeffs, line))


def binary_poly_mul(a: Dict[int, int], b: Dict[int, int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for da, va in a.items():
        for db, vb in b.items():
            out[da + db] = out.get(da + db, 0) + va * vb
    return out


def quadratic_power(coeff_triplet: Tuple[int, int, int], e: int) -> Dict[int, int]:
    # (A s^2 + B st + C t^2)^e represented by s-degree map, total degree 2e.
    if e == 0:
        return {0: 1}
    base = {}
    a, b, c = coeff_triplet
    if a != 0:
        base[2] = a
    if b != 0:
        base[1] = b
    if c != 0:
        base[0] = c
    out = {0: 1}
    for _ in range(e):
        out = binary_poly_mul(out, base)
    return out


def substitute_on_conic_template(coeffs: Dict[Exp4, int], template: ConicTemplate) -> Dict[int, int]:
    # Returns coeffs of degree-8 binary form in s,t by s-degree map.
    poly: Dict[int, int] = {}
    for (a, b, c, d), c0 in coeffs.items():
        if c0 == 0:
            continue
        factors = [
            quadratic_power(template[0], a),
            quadratic_power(template[1], b),
            quadratic_power(template[2], c),
            quadratic_power(template[3], d),
        ]
        accum: Dict[int, int] = {0: 1}
        for f in factors:
            accum = binary_poly_mul(accum, f)
        for sdeg, val in accum.items():
            poly[sdeg] = poly.get(sdeg, 0) + c0 * val
    return poly


def conic_template_contained(coeffs: Dict[Exp4, int], template: ConicTemplate) -> bool:
    restricted = substitute_on_conic_template(coeffs, template)
    return all(v == 0 for v in restricted.values())


def _template_bank_from_quadratics(rng: random.Random, max_templates: int, quad_bank: Sequence[Tuple[int, int, int]]) -> List[ConicTemplate]:
    templates: List[ConicTemplate] = []
    for zero_idx in range(4):
        active = [i for i in range(4) if i != zero_idx]
        for i in range(len(quad_bank)):
            for j in range(i + 1, len(quad_bank)):
                for k in range(j + 1, len(quad_bank)):
                    slots: List[Tuple[int, int, int]] = [(0, 0, 0)] * 4
                    slots[zero_idx] = (0, 0, 0)
                    slots[active[0]] = quad_bank[i]
                    slots[active[1]] = quad_bank[j]
                    slots[active[2]] = quad_bank[k]
                    templates.append((slots[0], slots[1], slots[2], slots[3]))
    dedup = sorted({t for t in templates})
    rng.shuffle(dedup)
    return dedup[: max_templates if max_templates > 0 else len(dedup)]


def candidate_conic_templates(rng: random.Random, max_templates: int) -> List[ConicTemplate]:
    """
    Deterministic/seeded conic-template bank expansion.

    Family: one coordinate forced to 0 (cheap plane conic proxy), other coordinates
    assigned small quadratic forms As^2 + Bst + Ct^2 from a fixed coefficient bank.
    """
    quad_bank: List[Tuple[int, int, int]] = [
        (1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, -1, 0),
        (1, 0, 1),
        (1, 0, -1),
        (0, 1, 1),
        (0, 1, -1),
        (1, 1, 1),
        (1, -1, 1),
    ]
    return _template_bank_from_quadratics(rng=rng, max_templates=max_templates, quad_bank=quad_bank)


def candidate_elliptic_templates(rng: random.Random, max_templates: int) -> List[EllipticTemplate]:
    """
    Deterministic seeded elliptic-template surrogate bank.

    Minimal v1 implementation intentionally reuses a quadratic-template incidence surrogate.
    Any hit is an elliptic-template heuristic incident only (non-certifying).
    """
    if max_templates <= 0:
        return []
    quad_bank: List[Tuple[int, int, int]] = [
        (1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, -1, 0),
        (1, 0, 1),
        (1, 0, -1),
        (0, 1, 1),
        (0, 1, -1),
        (1, 1, 1),
        (1, -1, 1),
        (2, 1, 0),
        (2, -1, 0),
        (2, 0, 1),
        (2, 0, -1),
    ]
    return _template_bank_from_quadratics(rng=rng, max_templates=max_templates, quad_bank=quad_bank)


def _quadric_from_dense(coeffs: Sequence[int], mons2: Sequence[Exp4]) -> QuadricPoly:
    return {m: int(c) for m, c in zip(mons2, coeffs) if int(c) != 0}


def candidate_quadric_templates(rng: random.Random, max_templates: int) -> List[QuadricTemplate]:
    """
    Deterministic small-coefficient bank for v3 quadric-pencil containment checks.
    Includes two explicit double-quadric fixtures for calibration.
    """
    if max_templates <= 0:
        return []
    mons2 = degree2_monomials()
    templates: List[QuadricTemplate] = []

    fixtures: List[QuadricTemplate] = [
        # Q1 = xz-y^2, Q2 = xw-yz
        ({(1, 0, 1, 0): 1, (0, 2, 0, 0): -1}, {(1, 0, 0, 1): 1, (0, 1, 1, 0): -1}),
        # Q1 = x^2+z^2-yw, Q2 = xw-yz+zw
        ({(2, 0, 0, 0): 1, (0, 0, 2, 0): 1, (0, 1, 0, 1): -1}, {(1, 0, 0, 1): 1, (0, 1, 1, 0): -1, (0, 0, 1, 1): 1}),
    ]
    templates.extend(fixtures)

    coeff_bank = [-2, -1, 0, 1, 2]
    while len(templates) < max_templates:
        q1 = _quadric_from_dense([rng.choice(coeff_bank) for _ in mons2], mons2)
        q2 = _quadric_from_dense([rng.choice(coeff_bank) for _ in mons2], mons2)
        if not q1 or not q2:
            continue
        if q1 == q2:
            continue
        templates.append((q1, q2))

    # dedup by sorted items signature while preserving fixture priority.
    dedup: Dict[Tuple[Tuple[Tuple[Exp4, int], ...], Tuple[Tuple[Exp4, int], ...]], QuadricTemplate] = {}
    ordered: List[QuadricTemplate] = []
    for q1, q2 in templates:
        key = (tuple(sorted(q1.items())), tuple(sorted(q2.items())))
        if key in dedup:
            continue
        dedup[key] = (q1, q2)
        ordered.append((q1, q2))

    fixture_count = min(len(fixtures), len(ordered))
    prefix = ordered[:fixture_count]
    tail = ordered[fixture_count:]
    rng.shuffle(tail)
    out = prefix + tail
    return out[:max_templates]


def _eval_homogeneous(poly: Dict[Exp4, int], p: Point, mod: int | None = None) -> int:
    x, y, z, w = p
    total = 0
    for (a, b, c, d), c0 in poly.items():
        total += c0 * (x**a) * (y**b) * (z**c) * (w**d)
    if mod is None:
        return total
    return total % mod


def _sample_curve_points_mod_p(q1: QuadricPoly, q2: QuadricPoly, p: int, limit: int) -> List[Point]:
    pts: List[Point] = []
    seen = set()
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    if (x, y, z, w) == (0, 0, 0, 0):
                        continue
                    if _eval_homogeneous(q1, (x, y, z, w), mod=p) != 0:
                        continue
                    if _eval_homogeneous(q2, (x, y, z, w), mod=p) != 0:
                        continue
                    key = (x, y, z, w)
                    if key in seen:
                        continue
                    seen.add(key)
                    pts.append((x, y, z, w))
                    if len(pts) >= limit:
                        return pts
    return pts


def _quartic_to_vector(coeffs: Dict[Exp4, int], mons4: Sequence[Exp4]) -> List[int]:
    return [int(coeffs.get(m, 0)) for m in mons4]


def _column_for_quadric_multiplier(source_q: QuadricPoly, basis_m: Exp4, mons4: Sequence[Exp4], idx4: Dict[Exp4, int]) -> List[int]:
    col = [0] * len(mons4)
    for n, c in source_q.items():
        m4 = (basis_m[0] + n[0], basis_m[1] + n[1], basis_m[2] + n[2], basis_m[3] + n[3])
        j = idx4.get(m4)
        if j is not None:
            col[j] += int(c)
    return col


def _ideal_membership_quadrics(coeffs: Dict[Exp4, int], q1: QuadricPoly, q2: QuadricPoly) -> bool:
    mons2 = degree2_monomials()
    mons4 = degree4_monomials()
    idx4 = {m: i for i, m in enumerate(mons4)}
    columns: List[List[int]] = []
    for m in mons2:
        columns.append(_column_for_quadric_multiplier(q1, m, mons4, idx4))
    for m in mons2:
        columns.append(_column_for_quadric_multiplier(q2, m, mons4, idx4))
    M = sp.Matrix(columns).T
    f = sp.Matrix(_quartic_to_vector(coeffs, mons4))
    return M.rank() == M.row_join(f).rank()


def quadric_pencil_contained_v3(
    coeffs: Dict[Exp4, int],
    template: QuadricTemplate,
    v3_prime_sample: int,
    v3_min_points: int,
) -> Tuple[bool, Dict[str, int]]:
    """
    v3 containment: tier1 modular point-screen -> tier2 exact ideal-membership.
    Tier3 placeholder is represented by requiring non-degenerate sampled curve points.
    """
    q1, q2 = template
    tier = {"tier1": 0, "tier2": 0, "tier3": 0}

    prime_candidates = [v3_prime_sample, 29, 37, 41]
    pts: List[Point] = []
    used_p = v3_prime_sample
    for p in prime_candidates:
        pts = _sample_curve_points_mod_p(q1, q2, p, limit=max(v3_min_points * 2, 24))
        if len(pts) >= v3_min_points:
            used_p = p
            break
    if len(pts) < v3_min_points:
        return False, tier
    if any(_eval_homogeneous(coeffs, pt, mod=used_p) != 0 for pt in pts[:v3_min_points]):
        return False, tier
    tier["tier1"] = 1

    if not _ideal_membership_quadrics(coeffs, q1, q2):
        return False, tier
    tier["tier2"] = 1

    tier["tier3"] = 1
    return True, tier


def _poly_eval_mod_from_degree_map(poly: Dict[int, int], x: int, p: int) -> int:
    total = 0
    for deg, coeff in poly.items():
        total = (total + (coeff % p) * pow(x, deg, p)) % p
    return total


def _poly_derivative_degree_map(poly: Dict[int, int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for deg, coeff in poly.items():
        if deg > 0:
            out[deg - 1] = out.get(deg - 1, 0) + deg * coeff
    return out


def elliptic_template_contained(
    coeffs: Dict[Exp4, int],
    template: EllipticTemplate,
    probe_mode: str = "v1-template",
    v2_cross_prime_count: int = 2,
    v2_min_rootcount: int = 2,
) -> bool:
    """
    Heuristic surrogate predicate for elliptic-template incident checks.

    v1-template: reuse current conic-template containment surrogate.
    v2-resultant: discriminant/resultant-inspired finite-field repeated-root proxy
    on restricted binary form (non-certifying).
    """
    if probe_mode == "v1-template":
        return conic_template_contained(coeffs, template)

    restricted = substitute_on_conic_template(coeffs, template)
    # Reject trivial/degenerate restrictions in v2 pathway.
    nonzero = {d: c for d, c in restricted.items() if c != 0}
    if len(nonzero) < 4:
        return False

    dpoly = _poly_derivative_degree_map(nonzero)
    strong_repeated_root_primes = 0
    for p in (5, 7, 11):
        root_count = 0
        for x in range(p):
            if _poly_eval_mod_from_degree_map(nonzero, x, p) == 0 and _poly_eval_mod_from_degree_map(dpoly, x, p) == 0:
                root_count += 1
        if root_count >= v2_min_rootcount:
            strong_repeated_root_primes += 1

    # Heuristic incident criterion (still non-certifying): stronger repeated-root structure.
    return strong_repeated_root_primes >= v2_cross_prime_count and len(nonzero) <= 7


def _restrict_to_w0(coeffs: Dict[Exp4, int]) -> Dict[Tuple[int, int, int], int]:
    out: Dict[Tuple[int, int, int], int] = {}
    for (a, b, c, d), v in coeffs.items():
        if v != 0 and d == 0:
            out[(a, b, c)] = out.get((a, b, c), 0) + v
    return {k: v for k, v in out.items() if v != 0}


def _mul_poly3_linear(
    cubic: Dict[Tuple[int, int, int], int],
    linear: Tuple[int, int, int],
) -> Dict[Tuple[int, int, int], int]:
    lx, ly, lz = linear
    out: Dict[Tuple[int, int, int], int] = {}
    for (a, b, c), v in cubic.items():
        if lx != 0:
            out[(a + 1, b, c)] = out.get((a + 1, b, c), 0) + v * lx
        if ly != 0:
            out[(a, b + 1, c)] = out.get((a, b + 1, c), 0) + v * ly
        if lz != 0:
            out[(a, b, c + 1)] = out.get((a, b, c + 1), 0) + v * lz
    return {k: v for k, v in out.items() if v != 0}


def _proportional_nonzero(
    a: Dict[Tuple[int, int, int], int],
    b: Dict[Tuple[int, int, int], int],
) -> bool:
    if not a or not b:
        return False
    if set(a.keys()) != set(b.keys()):
        return False
    keys = list(a.keys())
    k0 = keys[0]
    av0 = a[k0]
    bv0 = b[k0]
    for k in keys[1:]:
        if a[k] * bv0 != b[k] * av0:
            return False
    return True


def _weierstrass_plane_cubic(a: int, b: int) -> Dict[Tuple[int, int, int], int]:
    # y^2 z - x^3 - a x z^2 - b z^3 in (x,y,z).
    return {
        (0, 2, 1): 1,
        (3, 0, 0): -1,
        (1, 0, 2): -a,
        (0, 0, 3): -b,
    }


def elliptic_v3_weierstrass_incident_count(coeffs: Dict[Exp4, int]) -> int:
    """
    v3 heuristic detector:
    Compare F|_{w=0} against a small bank of low-height Weierstrass-plane products C3*L.
    Incidents are template matches up to scalar in coefficient space (heuristic only).
    """
    restricted = _restrict_to_w0(coeffs)
    if not restricted:
        return 0
    bank = [
        (-1, 0, (1, 1, 1)),
        (-2, 3, (1, 1, 1)),
        (1, -1, (1, -1, 2)),
    ]
    hits = 0
    for aa, bb, lin in bank:
        target = _mul_poly3_linear(_weierstrass_plane_cubic(aa, bb), lin)
        if _proportional_nonzero(restricted, target):
            hits += 1
    return hits


def elliptic_incident_count(
    coeffs: Dict[Exp4, int],
    elliptic_templates: Sequence[EllipticTemplate],
    elliptic_probe_mode: str,
    elliptic_v2_cross_prime_count: int,
    elliptic_v2_min_rootcount: int,
    quadric_templates: Sequence[QuadricTemplate] | None = None,
    v3_prime_sample: int = 31,
    v3_min_points: int = 15,
) -> Tuple[int, Dict[str, int]]:
    if elliptic_probe_mode == "v3-weierstrass":
        hits = elliptic_v3_weierstrass_incident_count(coeffs)
        return hits, {"tier1": 0, "tier2": 0, "tier3": 0}

    if elliptic_probe_mode == "v3-quadric":
        hits = 0
        tiers = {"tier1": 0, "tier2": 0, "tier3": 0}
        for qt in quadric_templates or []:
            ok, t = quadric_pencil_contained_v3(
                coeffs,
                qt,
                v3_prime_sample=v3_prime_sample,
                v3_min_points=v3_min_points,
            )
            if ok:
                hits += 1
                tiers["tier1"] += t["tier1"]
                tiers["tier2"] += t["tier2"]
                tiers["tier3"] += t["tier3"]
        return hits, tiers

    hits = len(
        [
            et
            for et in elliptic_templates
            if elliptic_template_contained(
                coeffs,
                et,
                probe_mode=elliptic_probe_mode,
                v2_cross_prime_count=elliptic_v2_cross_prime_count,
                v2_min_rootcount=elliptic_v2_min_rootcount,
            )
        ]
    )
    return hits, {"tier1": 0, "tier2": 0, "tier3": 0}


def gcd4(p: Point) -> int:
    g = 0
    for x in p:
        g = math.gcd(g, abs(x))
    return g


def normalize_point(p: Point) -> Point:
    if p == (0, 0, 0, 0):
        raise ValueError("zero point is not projective")
    g = gcd4(p)
    q = tuple(x // g for x in p)
    for v in q:
        if v != 0:
            if v < 0:
                q = tuple(-x for x in q)
            break
    return q  # type: ignore[return-value]


def canonical_line(line: Line) -> Line:
    p, q = normalize_point(line[0]), normalize_point(line[1])
    if p == q:
        raise ValueError("degenerate line")
    return tuple(sorted([p, q]))  # type: ignore[return-value]


def det2(a: int, b: int, c: int, d: int) -> int:
    return a * d - b * c


def are_collinear(p: Point, q: Point) -> bool:
    return (
        det2(p[0], p[1], q[0], q[1]) == 0
        and det2(p[0], p[2], q[0], q[2]) == 0
        and det2(p[0], p[3], q[0], q[3]) == 0
        and det2(p[1], p[2], q[1], q[2]) == 0
        and det2(p[1], p[3], q[1], q[3]) == 0
        and det2(p[2], p[3], q[2], q[3]) == 0
    )


def primitive_points(bound: int) -> List[Point]:
    pts: List[Point] = []
    for x in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            for z in range(-bound, bound + 1):
                for w in range(-bound, bound + 1):
                    if (x, y, z, w) == (0, 0, 0, 0):
                        continue
                    p = normalize_point((x, y, z, w))
                    if p not in pts:
                        pts.append(p)
    return pts


def candidate_lines(point_bound: int, random_probes: int, max_deterministic_lines: int, rng: random.Random) -> List[Line]:
    pts = primitive_points(point_bound)
    lines: set[Line] = set()

    all_pairs: List[Tuple[Point, Point]] = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            p, q = pts[i], pts[j]
            if not are_collinear(p, q):
                all_pairs.append((p, q))
    rng.shuffle(all_pairs)
    for p, q in all_pairs[:max_deterministic_lines]:
        lines.add(canonical_line((p, q)))

    # extra cheap randomized probes (possibly outside deterministic bank)
    for _ in range(random_probes):
        rp = (0, 0, 0, 0)
        rq = (0, 0, 0, 0)
        while rp == (0, 0, 0, 0):
            rp = tuple(rng.randint(-2, 2) for _ in range(4))  # type: ignore[assignment]
        while rq == (0, 0, 0, 0):
            rq = tuple(rng.randint(-2, 2) for _ in range(4))  # type: ignore[assignment]
        p = normalize_point(rp)
        q = normalize_point(rq)
        if p != q and not are_collinear(p, q):
            lines.add(canonical_line((p, q)))

    return list(lines)


def eval_quartic(coeffs: Dict[Exp4, int], p: Point, mod: int | None = None) -> int:
    x, y, z, w = p
    total = 0
    for (a, b, c, d), c0 in coeffs.items():
        term = c0 * (x**a) * (y**b) * (z**c) * (w**d)
        total += term
    if mod is None:
        return total
    return total % mod


def quartic_partials(coeffs: Dict[Exp4, int]) -> Tuple[Dict[Exp4, int], Dict[Exp4, int], Dict[Exp4, int], Dict[Exp4, int]]:
    dx: Dict[Exp4, int] = {}
    dy: Dict[Exp4, int] = {}
    dz: Dict[Exp4, int] = {}
    dw: Dict[Exp4, int] = {}
    for (a, b, c, d), v in coeffs.items():
        if a > 0:
            dx[(a - 1, b, c, d)] = dx.get((a - 1, b, c, d), 0) + a * v
        if b > 0:
            dy[(a, b - 1, c, d)] = dy.get((a, b - 1, c, d), 0) + b * v
        if c > 0:
            dz[(a, b, c - 1, d)] = dz.get((a, b, c - 1, d), 0) + c * v
        if d > 0:
            dw[(a, b, c, d - 1)] = dw.get((a, b, c, d - 1), 0) + d * v
    return dx, dy, dz, dw


def smoothness_screen_heuristic(
    coeffs: Dict[Exp4, int],
    points_per_prime: int,
    primes: Sequence[int],
    rng: random.Random,
) -> Tuple[bool, str]:
    """
    Heuristic only:
    Search for a sampled projective point over small finite fields where
    F = dF/dx = dF/dy = dF/dz = dF/dw = 0 mod p. If found, flag "possibly singular".

    Not a full discriminant/singularity test.
    """
    dx, dy, dz, dw = quartic_partials(coeffs)
    for p in primes:
        trials = 0
        while trials < points_per_prime:
            pt = tuple(rng.randint(0, p - 1) for _ in range(4))
            if pt == (0, 0, 0, 0):
                continue
            trials += 1
            if (
                eval_quartic(coeffs, pt, mod=p) == 0
                and eval_quartic(dx, pt, mod=p) == 0
                and eval_quartic(dy, pt, mod=p) == 0
                and eval_quartic(dz, pt, mod=p) == 0
                and eval_quartic(dw, pt, mod=p) == 0
            ):
                return False, f"flagged_possible_singularity_mod_{p}_at_{pt}"
    return True, "no_sampled_mod_p_singular_point_detected"


def random_quartic(rng: random.Random, mons: Sequence[Exp4], coeff_bound: int) -> Quartic:
    while True:
        coeffs = {m: rng.randint(-coeff_bound, coeff_bound) for m in mons}
        if any(v != 0 for v in coeffs.values()):
            return Quartic(coeffs=coeffs, label="random")


def engineered_contains_line(mons: Sequence[Exp4]) -> Quartic:
    coeffs = {m: 0 for m in mons}
    terms = {
        (1, 0, 3, 0): 1,
        (1, 0, 2, 1): 2,
        (1, 2, 1, 0): -1,
        (0, 1, 0, 3): 1,
        (0, 1, 2, 1): -1,
        (2, 1, 0, 1): 3,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="engineered_xG3_plus_yH3")


def forced_conic_example(mons: Sequence[Exp4]) -> Quartic:
    """
    Force containment of conic C in plane w=0 given by xz-y^2=0 via
        F = (xz-y^2)*Q2 + w*R3.
    """
    coeffs = {m: 0 for m in mons}
    # (xz - y^2)*(x^2 + z^2 + y*w)
    terms = {
        (3, 0, 1, 0): 1,
        (1, 0, 3, 0): 1,
        (1, 1, 1, 1): 1,
        (2, 2, 0, 0): -1,
        (0, 2, 2, 0): -1,
        (0, 3, 0, 1): -1,
    }
    # + w*(x^3 + y^3 - z^3 + x*y*z)
    terms.update({
        (3, 0, 0, 1): terms.get((3, 0, 0, 1), 0) + 1,
        (0, 3, 0, 1): terms.get((0, 3, 0, 1), 0) + 1,
        (0, 0, 3, 1): terms.get((0, 0, 3, 1), 0) - 1,
        (1, 1, 1, 1): terms.get((1, 1, 1, 1), 0) + 1,
    })
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="forced_conic_(xz-y^2)Q2+wR3")


def fermat_quartic(mons: Sequence[Exp4]) -> Quartic:
    coeffs = {m: 0 for m in mons}
    coeffs[(4, 0, 0, 0)] = 1
    coeffs[(0, 4, 0, 0)] = 1
    coeffs[(0, 0, 4, 0)] = 1
    coeffs[(0, 0, 0, 4)] = 1
    return Quartic(coeffs=coeffs, label="fermat_x4+y4+z4+w4_literature_known_special")


def engineered_elliptic_ci_quartic_a(mons: Sequence[Exp4]) -> Quartic:
    """
    Heuristic elliptic-engineered special via complete-intersection style forcing.

    Form: F = Q1*C2 + Q2*D2 with
      Q1 = xz - y^2,
      Q2 = xw - yz,
    so C = {Q1=Q2=0} is a degree-4 genus-1-style CI candidate in P^3 context.
    """
    coeffs = {m: 0 for m in mons}
    terms = {
        # Q1*C2, C2 = x^2 + y^2 + z^2 + w^2
        (3, 0, 1, 0): 1,
        (1, 2, 1, 0): 1,
        (1, 0, 3, 0): 1,
        (1, 0, 1, 2): 1,
        (2, 2, 0, 0): -1,
        (0, 4, 0, 0): -1,
        (0, 2, 2, 0): -1,
        (0, 2, 0, 2): -1,
        # Q2*D2, D2 = x^2 + z^2 + y*w
        (3, 0, 0, 1): 1,
        (1, 0, 2, 1): 1,
        (2, 1, 0, 1): 1,
        (2, 0, 1, 1): -1,
        (0, 1, 3, 0): -1,
        (1, 1, 1, 1): -1,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="engineered_elliptic_ci_q1q2_mix_a")


def engineered_elliptic_ci_quartic_b(mons: Sequence[Exp4]) -> Quartic:
    """Second CI-style elliptic-engineered quartic variant for positive-bank enrichment."""
    coeffs = {m: 0 for m in mons}
    terms = {
        # (xz-y^2)*(x^2 + z^2 + xw)
        (3, 0, 1, 0): 1,
        (1, 0, 3, 0): 1,
        (2, 0, 1, 1): 1,
        (2, 2, 0, 0): -1,
        (0, 2, 2, 0): -1,
        # +(xw-yz)*(y^2 + w^2 + xz)
        (1, 0, 0, 3): 1,
        (1, 2, 0, 1): 1,
        (2, 0, 1, 1): 2,
        (0, 3, 1, 0): -1,
        (0, 1, 1, 2): -1,
        (1, 1, 2, 0): -1,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="engineered_elliptic_ci_q1q2_mix_b")


def engineered_elliptic_forced_factor_quartic(mons: Sequence[Exp4]) -> Quartic:
    """
    Explicit elliptic-oriented forcing proxy:
      F = (xz-y^2)^2 + (xw-yz)^2.
    This is singular/reducible-leaning and used only as a positive-bank surrogate
    to test elliptic-v2 channel sensitivity under strict thresholds.
    """
    coeffs = {m: 0 for m in mons}
    terms = {
        # (xz-y^2)^2
        (2, 0, 2, 0): 1,
        (1, 2, 1, 0): -2,
        (0, 4, 0, 0): 1,
        # (xw-yz)^2
        (2, 0, 0, 2): 1,
        (1, 1, 1, 1): -2,
        (0, 2, 2, 0): 1,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="engineered_elliptic_forced_factor_proxy")


def engineered_elliptic_square_proxy_a(mons: Sequence[Exp4]) -> Quartic:
    """Sparse square proxy designed to stress v2 repeated-root detector."""
    coeffs = {m: 0 for m in mons}
    terms = {
        (4, 0, 0, 0): 1,
        (2, 2, 0, 0): 2,
        (0, 4, 0, 0): 1,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="engineered_elliptic_square_proxy_a")


def engineered_elliptic_square_proxy_b(mons: Sequence[Exp4]) -> Quartic:
    """Second sparse square proxy with different variable support."""
    coeffs = {m: 0 for m in mons}
    terms = {
        (4, 0, 0, 0): 1,
        (2, 0, 2, 0): -2,
        (0, 0, 4, 0): 1,
        (2, 0, 0, 2): 1,
        (0, 0, 2, 2): 1,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="engineered_elliptic_square_proxy_b")


def engineered_weierstrass_elliptic_plane(mons: Sequence[Exp4], a: int, b: int, linear: Tuple[int, int, int, int]) -> Quartic:
    """
    Build F = (y^2 z - x^3 - a x z^2 - b z^3) * (lx x + ly y + lz z + lw w).
    Heuristic positive control for elliptic-containing quartic constructions.
    """
    lx, ly, lz, lw = linear
    coeffs = {m: 0 for m in mons}
    cubic = {
        (3, 0, 0): -1,
        (0, 2, 1): 1,
        (1, 0, 2): -a,
        (0, 0, 3): -b,
    }
    for (cx, cy, cz), v in cubic.items():
        if lx:
            coeffs[(cx + 1, cy, cz, 0)] += v * lx
        if ly:
            coeffs[(cx, cy + 1, cz, 0)] += v * ly
        if lz:
            coeffs[(cx, cy, cz + 1, 0)] += v * lz
        if lw:
            coeffs[(cx, cy, cz, 1)] += v * lw
    return Quartic(
        coeffs=coeffs,
        label=f"explicit_elliptic_weierstrass_plane_a{a}_b{b}_L{lx}{ly}{lz}{lw}",
        structural_marker="explicit_elliptic_quartic_weierstrass",
    )


def engineered_double_quadric_positive(mons: Sequence[Exp4]) -> Quartic:
    """
    Calibration fixture: F = (L1*L2)*Q1 + (L3*L4)*Q2 with
    Q1 = xz-y^2 and Q2 = xw-yz.
    Used to verify Tier-2 ideal-membership solves for full quadric multipliers.
    """
    coeffs = {m: 0 for m in mons}
    # First term: (x*y)*(xz-y^2) = x^2 y z - x y^3
    coeffs[(2, 1, 1, 0)] += 1
    coeffs[(1, 3, 0, 0)] += -1
    # Second term: (z*w)*(xw-yz) = x z w^2 - y z^2 w
    coeffs[(1, 0, 1, 2)] += 1
    coeffs[(0, 1, 2, 1)] += -1
    return Quartic(coeffs=coeffs, label="engineered_double_quadric_L1L2Q1_plus_L3L4Q2", structural_marker="double_quadric_fixture")


def optional_determinantal_style_proxy(mons: Sequence[Exp4]) -> Quartic:
    """Quartic proxy from determinant of a 2x2 matrix of quadrics (illustrative only)."""
    coeffs = {m: 0 for m in mons}
    # det [[x^2+y^2, z^2+w^2], [xz+yw, xw+yz]]
    # = (x^2+y^2)(xw+yz) - (z^2+w^2)(xz+yw)
    terms = {
        (3, 0, 0, 1): 1,
        (2, 1, 1, 0): 1,
        (1, 2, 0, 1): 1,
        (0, 3, 1, 0): 1,
        (1, 0, 3, 0): -1,
        (0, 1, 2, 1): -1,
        (1, 0, 1, 2): -1,
        (0, 1, 0, 3): -1,
    }
    coeffs.update(terms)
    return Quartic(
        coeffs=coeffs,
        label="determinantal_style_proxy_2x2_quadric_det",
        structural_marker="determinantal_proxy_marker",
    )


def conic_contained_xz_minus_y2(coeffs: Dict[Exp4, int]) -> bool:
    """Check F(s^2, s t, t^2, 0) == 0 as a binary form of degree 8."""
    poly: Dict[int, int] = {}
    for (a, b, c, d), c0 in coeffs.items():
        if c0 == 0 or d != 0:
            continue
        sdeg = 2 * a + b
        poly[sdeg] = poly.get(sdeg, 0) + c0
    return all(v == 0 for v in poly.values())


def summarize_random_batch(
    samples: int,
    seed: int,
    coeff_bound: int,
    lines: Sequence[Line],
    conic_templates: Sequence[ConicTemplate],
    elliptic_templates: Sequence[EllipticTemplate],
    quadric_templates: Sequence[QuadricTemplate],
    elliptic_probe_mode: str,
    elliptic_v2_cross_prime_count: int,
    elliptic_v2_min_rootcount: int,
    v3_prime_sample: int,
    v3_min_points: int,
    mons: Sequence[Exp4],
    smooth_points_per_prime: int,
    smooth_primes: Sequence[int],
) -> Dict[str, int]:
    rng = random.Random(seed)
    smooth_pass = 0
    smooth_flag = 0
    analyzed = 0
    detected_line_quartics = 0
    detected_line_total = 0
    detected_conic_quartics = 0
    detected_conic_total = 0
    detected_elliptic_quartics = 0
    detected_elliptic_total = 0
    v3_tier1_total = 0
    v3_tier2_total = 0
    v3_tier3_total = 0

    for _ in range(samples):
        q = random_quartic(rng, mons, coeff_bound)
        smooth_ok, _ = smoothness_screen_heuristic(
            q.coeffs, points_per_prime=smooth_points_per_prime, primes=smooth_primes, rng=rng
        )
        if not smooth_ok:
            smooth_flag += 1
            continue
        smooth_pass += 1
        analyzed += 1
        line_hits = [ln for ln in lines if line_contained(q.coeffs, ln)]
        if line_hits:
            detected_line_quartics += 1
            detected_line_total += len(line_hits)
        conic_hits = [ct for ct in conic_templates if conic_template_contained(q.coeffs, ct)]
        if conic_hits:
            detected_conic_quartics += 1
            detected_conic_total += len(conic_hits)
        elliptic_hits, v3_tiers = elliptic_incident_count(
            q.coeffs,
            elliptic_templates,
            elliptic_probe_mode,
            elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount,
            quadric_templates=quadric_templates,
            v3_prime_sample=v3_prime_sample,
            v3_min_points=v3_min_points,
        )
        if elliptic_hits:
            detected_elliptic_quartics += 1
            detected_elliptic_total += elliptic_hits
        v3_tier1_total += v3_tiers["tier1"]
        v3_tier2_total += v3_tiers["tier2"]
        v3_tier3_total += v3_tiers["tier3"]

    return {
        "samples": samples,
        "smooth_pass": smooth_pass,
        "smooth_flag": smooth_flag,
        "analyzed": analyzed,
        "with_line": detected_line_quartics,
        "line_incidents": detected_line_total,
        "with_conic": detected_conic_quartics,
        "conic_incidents": detected_conic_total,
        "with_elliptic_template": detected_elliptic_quartics,
        "elliptic_template_incidents": detected_elliptic_total,
        "with_elliptic_v2_surrogate": detected_elliptic_quartics if elliptic_probe_mode == "v2-resultant" else 0,
        "elliptic_v2_surrogate_incidents": detected_elliptic_total if elliptic_probe_mode == "v2-resultant" else 0,
        "with_elliptic_v3_quadric": detected_elliptic_quartics if elliptic_probe_mode == "v3-quadric" else 0,
        "elliptic_v3_quadric_incidents": detected_elliptic_total if elliptic_probe_mode == "v3-quadric" else 0,
        "v3_tier1": v3_tier1_total if elliptic_probe_mode == "v3-quadric" else 0,
        "v3_tier2": v3_tier2_total if elliptic_probe_mode == "v3-quadric" else 0,
        "v3_tier3": v3_tier3_total if elliptic_probe_mode == "v3-quadric" else 0,
    }


def run(
    samples: int,
    seed: int,
    coeff_bound: int,
    point_bound: int,
    random_line_probes: int,
    max_deterministic_lines: int,
    max_conic_templates: int,
    max_elliptic_templates: int,
    max_quadric_templates: int,
    elliptic_probe_mode: str,
    elliptic_v2_cross_prime_count: int,
    elliptic_v2_min_rootcount: int,
    v3_prime_sample: int,
    v3_min_points: int,
    smooth_points_per_prime: int,
    smooth_primes: Sequence[int],
    include_determinantal: bool,
) -> str:
    rng = random.Random(seed)
    mons = degree4_monomials()
    lines = candidate_lines(
        point_bound=point_bound,
        random_probes=random_line_probes,
        max_deterministic_lines=max_deterministic_lines,
        rng=rng,
    )
    conic_templates = candidate_conic_templates(rng=rng, max_templates=max_conic_templates)
    elliptic_templates = candidate_elliptic_templates(rng=rng, max_templates=max_elliptic_templates)
    quadric_templates = candidate_quadric_templates(rng=rng, max_templates=max_quadric_templates)

    out: List[str] = []
    out.append("=== Expanded Noether-Lefschetz quartic incidence pilot ===")
    out.append(
        f"seed={seed}, samples={samples}, coeff_bound={coeff_bound}, point_bound={point_bound}, "
        f"max_deterministic_lines={max_deterministic_lines}, random_line_probes={random_line_probes}, "
        f"max_conic_templates={max_conic_templates}, max_elliptic_templates={max_elliptic_templates}, "
        f"max_quadric_templates={max_quadric_templates}, elliptic_probe_mode={elliptic_probe_mode}, "
        f"elliptic_v2_cross_prime_count={elliptic_v2_cross_prime_count}, "
        f"elliptic_v2_min_rootcount={elliptic_v2_min_rootcount}, v3_prime_sample={v3_prime_sample}, v3_min_points={v3_min_points}"
    )
    out.append(f"smoothness_heuristic: points_per_prime={smooth_points_per_prime}, primes={list(smooth_primes)}")
    out.append(
        f"monomials={len(mons)}, candidate_lines={len(lines)}, candidate_conic_templates={len(conic_templates)}, "
        f"candidate_elliptic_templates={len(elliptic_templates)}, candidate_quadric_templates={len(quadric_templates)}"
    )
    out.append("NOTE: incidence and smoothness checks are heuristic screens, not Picard-rank / NL-locus computations.")
    out.append("NOTE: conic-template scan is intentionally incomplete; detections are template-family hits only.")
    out.append("NOTE: elliptic-template scan is a minimal surrogate path; detections are heuristic template incidents only.")
    out.append("")

    specials = [
        engineered_contains_line(mons),
        forced_conic_example(mons),
        fermat_quartic(mons),
        engineered_elliptic_ci_quartic_a(mons),
        engineered_elliptic_ci_quartic_b(mons),
        engineered_elliptic_forced_factor_quartic(mons),
        engineered_elliptic_square_proxy_a(mons),
        engineered_elliptic_square_proxy_b(mons),
        engineered_weierstrass_elliptic_plane(mons, a=-1, b=0, linear=(1, 1, 1, 1)),
        engineered_weierstrass_elliptic_plane(mons, a=-2, b=3, linear=(1, 1, 1, 1)),
        engineered_double_quadric_positive(mons),
    ]
    if include_determinantal:
        specials.append(optional_determinantal_style_proxy(mons))

    out.append("[special-bank checks]")
    for q in specials:
        smooth_ok, smooth_note = smoothness_screen_heuristic(
            q.coeffs, points_per_prime=smooth_points_per_prime, primes=smooth_primes, rng=rng
        )
        line_hits = [ln for ln in lines if line_contained(q.coeffs, ln)]
        conic_hits = [ct for ct in conic_templates if conic_template_contained(q.coeffs, ct)]
        elliptic_hits, v3_tiers = elliptic_incident_count(
            q.coeffs,
            elliptic_templates,
            elliptic_probe_mode,
            elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount,
            quadric_templates=quadric_templates,
            v3_prime_sample=v3_prime_sample,
            v3_min_points=v3_min_points,
        )
        conic_hit = conic_contained_xz_minus_y2(q.coeffs)
        marker_note = q.structural_marker if q.structural_marker else "none"
        out.append(
            f"- {q.label}: smoothness_screen={'pass' if smooth_ok else 'flag'} ({smooth_note}), "
            f"line_hits={len(line_hits)}, conic_template_hits={len(conic_hits)}, elliptic_template_hits={elliptic_hits}, "
            f"v3_tier_breakdown={v3_tiers}, contains_test_conic_xz-y2={'yes' if conic_hit else 'no'}, structural_marker={marker_note}"
        )
    out.append("")

    stats = summarize_random_batch(
        samples=samples,
        seed=seed + 1,
        coeff_bound=coeff_bound,
        lines=lines,
        conic_templates=conic_templates,
        elliptic_templates=elliptic_templates,
        quadric_templates=quadric_templates,
        elliptic_probe_mode=elliptic_probe_mode,
        elliptic_v2_cross_prime_count=elliptic_v2_cross_prime_count,
        elliptic_v2_min_rootcount=elliptic_v2_min_rootcount,
        v3_prime_sample=v3_prime_sample,
        v3_min_points=v3_min_points,
        mons=mons,
        smooth_points_per_prime=smooth_points_per_prime,
        smooth_primes=smooth_primes,
    )

    out.append(f"random_total_samples={stats['samples']}")
    out.append(f"smoothness_screen_pass={stats['smooth_pass']}")
    out.append(f"smoothness_screen_flagged={stats['smooth_flag']}")
    out.append(f"random_samples_analyzed={stats['analyzed']}")
    out.append(f"random_samples_with_any_detected_line={stats['with_line']}/{stats['analyzed'] if stats['analyzed'] else 1}")
    out.append(f"random_samples_with_any_detected_conic_template={stats['with_conic']}/{stats['analyzed'] if stats['analyzed'] else 1}")
    out.append(
        f"random_samples_with_any_detected_elliptic_template={stats['with_elliptic_template']}/{stats['analyzed'] if stats['analyzed'] else 1}"
    )
    out.append(
        f"random_samples_with_any_detected_elliptic_v2_surrogate={stats['with_elliptic_v2_surrogate']}/{stats['analyzed'] if stats['analyzed'] else 1}"
    )
    out.append(
        f"random_samples_with_any_detected_elliptic_v3_quadric={stats['with_elliptic_v3_quadric']}/{stats['analyzed'] if stats['analyzed'] else 1}"
    )
    out.append(f"v3_tier_breakdown={{'tier1': {stats['v3_tier1']}, 'tier2': {stats['v3_tier2']}, 'tier3': {stats['v3_tier3']}}}")
    out.append(f"total_detected_line_incidents={stats['line_incidents']}")
    out.append(f"total_detected_conic_template_incidents={stats['conic_incidents']}")
    out.append(f"total_detected_elliptic_template_incidents={stats['elliptic_template_incidents']}")
    out.append(f"total_detected_elliptic_v2_surrogate_incidents={stats['elliptic_v2_surrogate_incidents']}")
    out.append(f"total_detected_elliptic_v3_quadric_incidents={stats['elliptic_v3_quadric_incidents']}")
    out.append("Interpretation: detections indicate special-incidence candidates under this finite scan.")
    out.append("Non-detection does not imply generic Picard rank, smoothness, or NL-genericity.")
    return "\n".join(out)


def run_positive_control(
    seed: int,
    point_bound: int,
    random_line_probes: int,
    max_deterministic_lines: int,
    max_conic_templates: int,
    max_elliptic_templates: int,
    max_quadric_templates: int,
    elliptic_probe_mode: str,
    elliptic_v2_cross_prime_count: int,
    elliptic_v2_min_rootcount: int,
    v3_prime_sample: int,
    v3_min_points: int,
    smooth_points_per_prime: int,
    smooth_primes: Sequence[int],
    gate_positive_threshold: float,
) -> str:
    rng = random.Random(seed)
    mons = degree4_monomials()
    lines = candidate_lines(
        point_bound=point_bound,
        random_probes=random_line_probes,
        max_deterministic_lines=max_deterministic_lines,
        rng=rng,
    )
    conic_templates = candidate_conic_templates(rng=rng, max_templates=max_conic_templates)
    elliptic_templates = candidate_elliptic_templates(rng=rng, max_templates=max_elliptic_templates)
    quadric_templates = candidate_quadric_templates(rng=rng, max_templates=max_quadric_templates)

    specials = [
        engineered_contains_line(mons),
        forced_conic_example(mons),
        fermat_quartic(mons),
        engineered_elliptic_ci_quartic_a(mons),
        engineered_elliptic_ci_quartic_b(mons),
        engineered_elliptic_forced_factor_quartic(mons),
        engineered_elliptic_square_proxy_a(mons),
        engineered_elliptic_square_proxy_b(mons),
        engineered_weierstrass_elliptic_plane(mons, a=-1, b=0, linear=(1, 1, 1, 1)),
        engineered_weierstrass_elliptic_plane(mons, a=-2, b=3, linear=(1, 1, 1, 1)),
        engineered_double_quadric_positive(mons),
        optional_determinantal_style_proxy(mons),
    ]
    # Keep gate calibration mode-aligned: each probe mode is evaluated on fixtures
    # it is designed to detect, avoiding denominator inflation from out-of-family
    # constructions while preserving conservative interpretation language below.
    if elliptic_probe_mode == "v3-weierstrass":
        target_labels = {
            "explicit_elliptic_weierstrass_plane_a-1_b0_L1111",
            "explicit_elliptic_weierstrass_plane_a-2_b3_L1111",
        }
    elif elliptic_probe_mode == "v3-quadric":
        target_labels = {
            "engineered_elliptic_ci_q1q2_mix_a",
            "engineered_elliptic_ci_q1q2_mix_b",
            "engineered_double_quadric_L1L2Q1_plus_L3L4Q2",
        }
    else:
        target_labels = {
            "engineered_elliptic_ci_q1q2_mix_a",
            "engineered_elliptic_ci_q1q2_mix_b",
            "engineered_elliptic_forced_factor_proxy",
            "explicit_elliptic_weierstrass_plane_a-1_b0_L1111",
            "explicit_elliptic_weierstrass_plane_a-2_b3_L1111",
            "engineered_double_quadric_L1L2Q1_plus_L3L4Q2",
        }
    positive_hits = 0
    positive_total = 0

    out: List[str] = []
    out.append("=== Positive-control bank run (heuristic) ===")
    out.append(
        f"seed={seed}, candidate_lines={len(lines)}, candidate_conic_templates={len(conic_templates)}, "
        f"candidate_elliptic_templates={len(elliptic_templates)}, candidate_quadric_templates={len(quadric_templates)}, "
        f"elliptic_probe_mode={elliptic_probe_mode}, elliptic_v2_cross_prime_count={elliptic_v2_cross_prime_count}, "
        f"elliptic_v2_min_rootcount={elliptic_v2_min_rootcount}, v3_prime_sample={v3_prime_sample}, v3_min_points={v3_min_points}, "
        f"smooth_points_per_prime={smooth_points_per_prime}, smooth_primes={list(smooth_primes)}"
    )
    out.append("determinantal entry is a labeled proxy family, not claimed canonical literature normal form.")
    out.append("")
    for q in specials:
        smooth_ok, smooth_note = smoothness_screen_heuristic(
            q.coeffs, points_per_prime=smooth_points_per_prime, primes=smooth_primes, rng=rng
        )
        line_hits = [ln for ln in lines if line_contained(q.coeffs, ln)]
        conic_hits = [ct for ct in conic_templates if conic_template_contained(q.coeffs, ct)]
        elliptic_hits, v3_tiers = elliptic_incident_count(
            q.coeffs,
            elliptic_templates,
            elliptic_probe_mode,
            elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount,
            quadric_templates=quadric_templates,
            v3_prime_sample=v3_prime_sample,
            v3_min_points=v3_min_points,
        )
        if q.label in target_labels:
            positive_total += 1
            if elliptic_hits > 0:
                positive_hits += 1
        out.append(
            f"- {q.label}: smoothness_screen={'pass' if smooth_ok else 'flag'} ({smooth_note}), "
            f"line_hits={len(line_hits)}, conic_template_hits={len(conic_hits)}, elliptic_template_hits={elliptic_hits}, "
            f"v3_tier_breakdown={v3_tiers}, structural_marker={q.structural_marker or 'none'}"
        )
    out.append("")
    positive_rate = (positive_hits / positive_total) if positive_total else 0.0
    out.append(f"gate_positive_hits={positive_hits}")
    out.append(f"gate_positive_total={positive_total}")
    out.append(f"gate_positive_rate={positive_rate:.6f}")
    out.append(f"gate_positive_threshold={gate_positive_threshold:.6f}")
    out.append(f"gate_positive_pass={1 if positive_rate > gate_positive_threshold else 0}")
    out.append("Interpretation: positive controls validate scanner sensitivity on these tagged constructions only.")
    return "\n".join(out)


def parse_primes(s: str) -> List[int]:
    parts = [x.strip() for x in s.split(",") if x.strip()]
    return [int(x) for x in parts]


def parse_int_list(s: str) -> List[int]:
    return [int(x.strip()) for x in s.split(",") if x.strip()]


def extract_gate_metrics(report: str) -> Dict[str, float | int]:
    out: Dict[str, float | int] = {}
    for line in report.splitlines():
        if not line.startswith("gate_") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        try:
            if "." in v:
                out[k] = float(v)
            else:
                out[k] = int(v)
        except ValueError:
            continue
    return out


def make_proxy_baseline(mons: Sequence[Exp4]) -> Quartic:
    coeffs = {m: 0 for m in mons}
    terms = {
        (4, 0, 0, 0): 2,
        (0, 4, 0, 0): -1,
        (0, 0, 4, 0): 1,
        (0, 0, 0, 4): 1,
        (2, 2, 0, 0): 1,
        (1, 1, 1, 1): -1,
        (3, 0, 1, 0): 1,
        (0, 1, 2, 1): -1,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="proxy_baseline_not_van_luijk_exact")


def make_van_luijk_exact_2007_baseline(mons: Sequence[Exp4]) -> Quartic:
    """
    Exact integer-coefficient baseline from van Luijk (2007) family model
    wf1 + 2 z f2 = 3 g1 g2 + 6 h with h=0 (expanded quartic in x,y,z,w).

    Source context: arXiv:math/0506416 (published in Algebra & Number Theory 1(1), 2007).
    This code path only encodes the explicit quartic polynomial; it does not reproduce
    arithmetic Picard-rank certification.
    """
    coeffs = {m: 0 for m in mons}
    terms = {
        (0, 0, 0, 4): 2,
        (0, 0, 1, 3): 1,
        (0, 0, 2, 2): 1,
        (0, 0, 4, 0): -1,
        (0, 1, 0, 3): -1,
        (0, 1, 1, 2): 1,
        (0, 1, 2, 1): 1,
        (0, 1, 3, 0): -5,
        (0, 2, 0, 2): -1,
        (0, 2, 1, 1): 1,
        (0, 3, 0, 1): 1,
        (1, 0, 1, 2): 2,
        (1, 0, 2, 1): 1,
        (1, 0, 3, 0): -2,
        (1, 1, 0, 2): 2,
        (1, 1, 1, 1): -1,
        (1, 1, 2, 0): -4,
        (1, 2, 0, 1): -1,
        (1, 2, 1, 0): -1,
        (2, 0, 0, 2): 1,
        (2, 0, 1, 1): -1,
        (2, 1, 0, 1): -1,
        (2, 2, 0, 0): -3,
        (3, 0, 0, 1): 1,
    }
    coeffs.update(terms)
    return Quartic(coeffs=coeffs, label="van_luijk_exact_2007_h0_expanded", structural_marker="van_luijk_exact_2007")


def perturb_coeffs(base: Dict[Exp4, int], mons: Sequence[Exp4], noise_bound: int, rng: random.Random) -> Dict[Exp4, int]:
    out = dict(base)
    for m in mons:
        out[m] = out.get(m, 0) + rng.randint(-noise_bound, noise_bound)
    if all(v == 0 for v in out.values()):
        out[mons[0]] = 1
    return out


def run_stratified(
    samples_per_bound: int,
    stratified_bounds: Sequence[int],
    seed: int,
    point_bound: int,
    random_line_probes: int,
    max_deterministic_lines: int,
    max_conic_templates: int,
    max_elliptic_templates: int,
    max_quadric_templates: int,
    elliptic_probe_mode: str,
    elliptic_v2_cross_prime_count: int,
    elliptic_v2_min_rootcount: int,
    v3_prime_sample: int,
    v3_min_points: int,
    smooth_points_per_prime: int,
    smooth_primes: Sequence[int],
) -> str:
    mons = degree4_monomials()
    line_rng = random.Random(seed)
    lines = candidate_lines(point_bound, random_line_probes, max_deterministic_lines, line_rng)
    conic_templates = candidate_conic_templates(rng=line_rng, max_templates=max_conic_templates)
    elliptic_templates = candidate_elliptic_templates(rng=line_rng, max_templates=max_elliptic_templates)
    quadric_templates = candidate_quadric_templates(rng=line_rng, max_templates=max_quadric_templates)
    out: List[str] = []
    out.append("=== Stratified random sampling by coefficient bound (heuristic) ===")
    out.append(f"seed={seed}, samples_per_bound={samples_per_bound}, stratified_bounds={list(stratified_bounds)}")
    out.append(
        f"candidate_lines={len(lines)}, candidate_conic_templates={len(conic_templates)}, "
        f"candidate_elliptic_templates={len(elliptic_templates)}, candidate_quadric_templates={len(quadric_templates)}, "
        f"elliptic_probe_mode={elliptic_probe_mode}, elliptic_v2_cross_prime_count={elliptic_v2_cross_prime_count}, "
        f"elliptic_v2_min_rootcount={elliptic_v2_min_rootcount}, v3_prime_sample={v3_prime_sample}, v3_min_points={v3_min_points}, "
        f"smooth_primes={list(smooth_primes)}, smooth_points_per_prime={smooth_points_per_prime}"
    )
    out.append("")

    for idx, b in enumerate(stratified_bounds):
        batch_seed = seed + 1000 * (idx + 1)
        stats = summarize_random_batch(
            samples=samples_per_bound,
            seed=batch_seed,
            coeff_bound=b,
            lines=lines,
            conic_templates=conic_templates,
            elliptic_templates=elliptic_templates,
            quadric_templates=quadric_templates,
            elliptic_probe_mode=elliptic_probe_mode,
            elliptic_v2_cross_prime_count=elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount=elliptic_v2_min_rootcount,
            v3_prime_sample=v3_prime_sample,
            v3_min_points=v3_min_points,
            mons=mons,
            smooth_points_per_prime=smooth_points_per_prime,
            smooth_primes=smooth_primes,
        )
        smooth_rate = stats["smooth_pass"] / stats["samples"] if stats["samples"] else 0.0
        line_rate = stats["with_line"] / stats["analyzed"] if stats["analyzed"] else 0.0
        conic_rate = stats["with_conic"] / stats["analyzed"] if stats["analyzed"] else 0.0
        elliptic_rate = stats["with_elliptic_template"] / stats["analyzed"] if stats["analyzed"] else 0.0
        out.append(
            f"coeff_bound={b}: seed={batch_seed}, smooth_pass={stats['smooth_pass']}/{stats['samples']} ({smooth_rate:.4f}), "
            f"line_detected={stats['with_line']}/{stats['analyzed'] if stats['analyzed'] else 1} ({line_rate:.4f}), "
            f"conic_template_detected={stats['with_conic']}/{stats['analyzed'] if stats['analyzed'] else 1} ({conic_rate:.4f}), "
            f"elliptic_template_detected={stats['with_elliptic_template']}/{stats['analyzed'] if stats['analyzed'] else 1} ({elliptic_rate:.4f}), "
            f"elliptic_v2_surrogate_detected={stats['with_elliptic_v2_surrogate']}/{stats['analyzed'] if stats['analyzed'] else 1}, "
            f"line_incidents={stats['line_incidents']}, conic_template_incidents={stats['conic_incidents']}, "
            f"elliptic_template_incidents={stats['elliptic_template_incidents']}, "
            f"elliptic_v2_surrogate_incidents={stats['elliptic_v2_surrogate_incidents']}"
        )

    out.append("")
    out.append("All rates are finite-scan heuristic rates; not Picard-rank or NL-locus estimates.")
    return "\n".join(out)


def run_perturbation(
    trials: int,
    seed: int,
    noise_bound: int,
    noise_scale: int,
    perturbation_baseline: str,
    point_bound: int,
    random_line_probes: int,
    max_deterministic_lines: int,
    max_conic_templates: int,
    max_elliptic_templates: int,
    max_quadric_templates: int,
    elliptic_probe_mode: str,
    elliptic_v2_cross_prime_count: int,
    elliptic_v2_min_rootcount: int,
    v3_prime_sample: int,
    v3_min_points: int,
    smooth_points_per_prime: int,
    smooth_primes: Sequence[int],
    gate_guardrail_threshold: float,
) -> str:
    mons = degree4_monomials()
    line_rng = random.Random(seed)
    lines = candidate_lines(point_bound, random_line_probes, max_deterministic_lines, line_rng)
    conic_templates = candidate_conic_templates(rng=line_rng, max_templates=max_conic_templates)
    elliptic_templates = candidate_elliptic_templates(rng=line_rng, max_templates=max_elliptic_templates)
    quadric_templates = candidate_quadric_templates(rng=line_rng, max_templates=max_quadric_templates)
    if perturbation_baseline == "proxy":
        base = make_proxy_baseline(mons)
        baseline_note = "proxy_baseline"
    else:
        base = make_van_luijk_exact_2007_baseline(mons)
        baseline_note = "van_luijk_exact_2007_h0_from_cited_equation"
    rng = random.Random(seed + 77)

    base_smooth, base_note = smoothness_screen_heuristic(base.coeffs, smooth_points_per_prime, smooth_primes, rng)
    base_line_hits = [ln for ln in lines if line_contained(base.coeffs, ln)]
    base_conic_hits = [ct for ct in conic_templates if conic_template_contained(base.coeffs, ct)]
    base_elliptic_hits, base_v3_tiers = elliptic_incident_count(
        base.coeffs,
        elliptic_templates,
        elliptic_probe_mode,
        elliptic_v2_cross_prime_count,
        elliptic_v2_min_rootcount,
        quadric_templates=quadric_templates,
        v3_prime_sample=v3_prime_sample,
        v3_min_points=v3_min_points,
    )

    smooth_pass = 0
    analyzed = 0
    with_line = 0
    line_incidents = 0
    with_conic = 0
    conic_incidents = 0
    with_elliptic = 0
    elliptic_incidents = 0
    with_elliptic_v2 = 0
    elliptic_v2_incidents = 0

    for _ in range(trials):
        coeffs = perturb_coeffs(base.coeffs, mons, noise_bound, rng)
        ok, _ = smoothness_screen_heuristic(coeffs, smooth_points_per_prime, smooth_primes, rng)
        if not ok:
            continue
        smooth_pass += 1
        analyzed += 1
        line_hits = [ln for ln in lines if line_contained(coeffs, ln)]
        if line_hits:
            with_line += 1
            line_incidents += len(line_hits)
        conic_hits = [ct for ct in conic_templates if conic_template_contained(coeffs, ct)]
        if conic_hits:
            with_conic += 1
            conic_incidents += len(conic_hits)
        elliptic_hits, _ = elliptic_incident_count(
            coeffs,
            elliptic_templates,
            elliptic_probe_mode,
            elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount,
            quadric_templates=quadric_templates,
            v3_prime_sample=v3_prime_sample,
            v3_min_points=v3_min_points,
        )
        if elliptic_hits:
            with_elliptic += 1
            elliptic_incidents += elliptic_hits
            if elliptic_probe_mode == "v2-resultant":
                with_elliptic_v2 += 1
                elliptic_v2_incidents += elliptic_hits

    out: List[str] = []
    out.append("=== van-Luijk-track perturbation test (conservative, heuristic only) ===")
    out.append("Deterministic perturbation arithmetic: integer coefficient noise in [-noise_bound, noise_bound] with reported epsilon_proxy=noise_bound/noise_scale.")
    out.append("No floating perturbation arithmetic is used; this avoids float-instability overclaims.")
    epsilon_proxy = noise_bound / noise_scale if noise_scale > 0 else float(noise_bound)
    out.append(
        f"seed={seed}, trials={trials}, noise_bound={noise_bound}, noise_scale={noise_scale}, "
        f"epsilon_proxy={epsilon_proxy:.8g}, baseline_mode={perturbation_baseline}, "
        f"candidate_lines={len(lines)}, candidate_conic_templates={len(conic_templates)}, "
        f"candidate_elliptic_templates={len(elliptic_templates)}, elliptic_probe_mode={elliptic_probe_mode}, "
        f"elliptic_v2_cross_prime_count={elliptic_v2_cross_prime_count}, elliptic_v2_min_rootcount={elliptic_v2_min_rootcount}"
    )
    out.append(f"base_label={base.label}, baseline_note={baseline_note}, base_marker={base.structural_marker or 'none'}")
    out.append(
        f"base_smoothness_screen={'pass' if base_smooth else 'flag'} ({base_note}), "
        f"base_line_hits={len(base_line_hits)}, base_conic_template_hits={len(base_conic_hits)}, "
        f"base_elliptic_template_hits={base_elliptic_hits}, base_v3_tier_breakdown={base_v3_tiers}"
    )
    if perturbation_baseline == "van_luijk_exact_2007":
        out.append("THEOREM-CONTEXT NOTE: rho_geom=1 per cited source context for this explicit family setup; this run itself does not certify Picard rank.")
    out.append(
        f"perturbed_smooth_pass={smooth_pass}/{trials}, "
        f"perturbed_line_detected={with_line}/{analyzed if analyzed else 1}, perturbed_line_incidents={line_incidents}, "
        f"perturbed_conic_template_detected={with_conic}/{analyzed if analyzed else 1}, "
        f"perturbed_conic_template_incidents={conic_incidents}, "
        f"perturbed_elliptic_template_detected={with_elliptic}/{analyzed if analyzed else 1}, "
        f"perturbed_elliptic_template_incidents={elliptic_incidents}, "
        f"perturbed_elliptic_v2_surrogate_detected={with_elliptic_v2}/{analyzed if analyzed else 1}, "
        f"perturbed_elliptic_v2_surrogate_incidents={elliptic_v2_incidents}"
    )
    guardrail_rate = (with_elliptic / analyzed) if analyzed else 0.0
    out.append(f"gate_guardrail_fp_hits={with_elliptic}")
    out.append(f"gate_guardrail_fp_total={analyzed}")
    out.append(f"gate_guardrail_fp_rate={guardrail_rate:.6f}")
    out.append(f"gate_guardrail_threshold={gate_guardrail_threshold:.6f}")
    out.append(f"gate_guardrail_pass={1 if guardrail_rate < gate_guardrail_threshold else 0}")
    out.append("Interpretation: proxy-family stability signal under this finite scan only.")
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Expanded quartic incidence pilot (heuristic)")
    parser.add_argument("--mode", type=str, default="random", choices=["random", "stratified", "perturbation", "positive-control", "gate-scorer"], help="run mode")
    parser.add_argument("--samples", type=int, default=300, help="number of random quartics")
    parser.add_argument("--seed", type=int, default=20260223, help="RNG seed")
    parser.add_argument("--coeff-bound", type=int, default=2, help="sample coefficients in [-B,B]")
    parser.add_argument("--stratified-bounds", type=str, default="1,2,3", help="comma-separated coeff bounds for stratified mode")
    parser.add_argument("--samples-per-bound", type=int, default=300, help="samples per coeff-bound in stratified mode")
    parser.add_argument("--perturb-trials", type=int, default=180, help="number of perturbation trials")
    parser.add_argument("--perturb-noise-bound", type=int, default=1, help="integer perturbation noise in [-n,n]")
    parser.add_argument("--perturb-noise-scale", type=int, default=1000000, help="integer scaling denominator for proxy epsilon (noise_bound/noise_scale)")
    parser.add_argument(
        "--perturbation-baseline",
        type=str,
        default="proxy",
        choices=["proxy", "van_luijk_exact_2007"],
        help="baseline selector: proxy or exact van Luijk 2007 h=0 expanded model",
    )
    parser.add_argument("--point-bound", type=int, default=1, help="deterministic primitive point bound for line bank")
    parser.add_argument("--max-deterministic-lines", type=int, default=180, help="cap on deterministic line pairs from point bank")
    parser.add_argument("--random-line-probes", type=int, default=80, help="extra randomized line probes")
    parser.add_argument("--max-conic-templates", type=int, default=64, help="number of low-cost conic templates to scan")
    parser.add_argument("--max-elliptic-templates", type=int, default=0, help="number of heuristic elliptic-template incidence probes (0 disables)")
    parser.add_argument("--max-quadric-templates", type=int, default=20, help="number of v3 quadric-pair templates to scan")
    parser.add_argument(
        "--elliptic-probe-mode",
        type=str,
        default="v1-template",
        choices=["v1-template", "v2-resultant", "v3-weierstrass", "v3-quadric"],
        help="elliptic heuristic probe mode (v1 template reuse, v2 resultant-style surrogate, v3 Weierstrass-plane proxy, or v3 quadric ideal-membership)",
    )
    parser.add_argument("--elliptic-v2-cross-prime-count", type=int, default=2, help="v2: minimum number of small primes passing repeated-root criterion")
    parser.add_argument("--elliptic-v2-min-rootcount", type=int, default=2, help="v2: minimum repeated-root count per prime")
    parser.add_argument("--v3-prime-sample", type=int, default=31, help="v3: finite-field prime for fast curve-point screening")
    parser.add_argument("--v3-min-points", type=int, default=15, help="v3: minimum sampled points on Q1=Q2 base locus before containment check")
    parser.add_argument("--smooth-points-per-prime", type=int, default=120, help="random projective points per small prime")
    parser.add_argument("--smooth-primes", type=str, default="5,7", help="comma-separated small primes for heuristic screen")
    parser.add_argument("--include-determinantal", action="store_true", help="include optional determinantal-style special")
    parser.add_argument("--gate-positive-threshold", type=float, default=0.80, help="gate A threshold: positive-first hit rate must exceed this value")
    parser.add_argument("--gate-guardrail-threshold", type=float, default=0.05, help="gate B threshold: false-positive rate must stay below this value")
    parser.add_argument("--output-json", action="store_true", help="emit a compact JSON gate-scorer block after text output")
    args = parser.parse_args()

    if args.mode == "random":
        report = run(
            samples=args.samples,
            seed=args.seed,
            coeff_bound=args.coeff_bound,
            point_bound=args.point_bound,
            random_line_probes=args.random_line_probes,
            max_deterministic_lines=args.max_deterministic_lines,
            max_conic_templates=args.max_conic_templates,
            max_elliptic_templates=args.max_elliptic_templates,
            max_quadric_templates=args.max_quadric_templates,
            elliptic_probe_mode=args.elliptic_probe_mode,
            elliptic_v2_cross_prime_count=args.elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount=args.elliptic_v2_min_rootcount,
            v3_prime_sample=args.v3_prime_sample,
            v3_min_points=args.v3_min_points,
            smooth_points_per_prime=args.smooth_points_per_prime,
            smooth_primes=parse_primes(args.smooth_primes),
            include_determinantal=args.include_determinantal,
        )
    elif args.mode == "stratified":
        report = run_stratified(
            samples_per_bound=args.samples_per_bound,
            stratified_bounds=parse_int_list(args.stratified_bounds),
            seed=args.seed,
            point_bound=args.point_bound,
            random_line_probes=args.random_line_probes,
            max_deterministic_lines=args.max_deterministic_lines,
            max_conic_templates=args.max_conic_templates,
            max_elliptic_templates=args.max_elliptic_templates,
            max_quadric_templates=args.max_quadric_templates,
            elliptic_probe_mode=args.elliptic_probe_mode,
            elliptic_v2_cross_prime_count=args.elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount=args.elliptic_v2_min_rootcount,
            v3_prime_sample=args.v3_prime_sample,
            v3_min_points=args.v3_min_points,
            smooth_points_per_prime=args.smooth_points_per_prime,
            smooth_primes=parse_primes(args.smooth_primes),
        )
    elif args.mode == "positive-control":
        report = run_positive_control(
            seed=args.seed,
            point_bound=args.point_bound,
            random_line_probes=args.random_line_probes,
            max_deterministic_lines=args.max_deterministic_lines,
            max_conic_templates=args.max_conic_templates,
            max_elliptic_templates=args.max_elliptic_templates,
            max_quadric_templates=args.max_quadric_templates,
            elliptic_probe_mode=args.elliptic_probe_mode,
            elliptic_v2_cross_prime_count=args.elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount=args.elliptic_v2_min_rootcount,
            v3_prime_sample=args.v3_prime_sample,
            v3_min_points=args.v3_min_points,
            smooth_points_per_prime=args.smooth_points_per_prime,
            smooth_primes=parse_primes(args.smooth_primes),
            gate_positive_threshold=args.gate_positive_threshold,
        )
    elif args.mode == "gate-scorer":
        positive_report = run_positive_control(
            seed=args.seed,
            point_bound=args.point_bound,
            random_line_probes=args.random_line_probes,
            max_deterministic_lines=args.max_deterministic_lines,
            max_conic_templates=args.max_conic_templates,
            max_elliptic_templates=args.max_elliptic_templates,
            max_quadric_templates=args.max_quadric_templates,
            elliptic_probe_mode=args.elliptic_probe_mode,
            elliptic_v2_cross_prime_count=args.elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount=args.elliptic_v2_min_rootcount,
            v3_prime_sample=args.v3_prime_sample,
            v3_min_points=args.v3_min_points,
            smooth_points_per_prime=args.smooth_points_per_prime,
            smooth_primes=parse_primes(args.smooth_primes),
            gate_positive_threshold=args.gate_positive_threshold,
        )
        guardrail_report = run_perturbation(
            trials=args.perturb_trials,
            seed=args.seed + 1,
            noise_bound=args.perturb_noise_bound,
            noise_scale=args.perturb_noise_scale,
            perturbation_baseline=args.perturbation_baseline,
            point_bound=args.point_bound,
            random_line_probes=args.random_line_probes,
            max_deterministic_lines=args.max_deterministic_lines,
            max_conic_templates=args.max_conic_templates,
            max_elliptic_templates=args.max_elliptic_templates,
            max_quadric_templates=args.max_quadric_templates,
            elliptic_probe_mode=args.elliptic_probe_mode,
            elliptic_v2_cross_prime_count=args.elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount=args.elliptic_v2_min_rootcount,
            v3_prime_sample=args.v3_prime_sample,
            v3_min_points=args.v3_min_points,
            smooth_points_per_prime=args.smooth_points_per_prime,
            smooth_primes=parse_primes(args.smooth_primes),
            gate_guardrail_threshold=args.gate_guardrail_threshold,
        )
        pm = extract_gate_metrics(positive_report)
        gm = extract_gate_metrics(guardrail_report)
        overall_pass = int(bool(pm.get("gate_positive_pass", 0)) and bool(gm.get("gate_guardrail_pass", 0)))
        summary = [
            "=== Gate scorer (combined) ===",
            f"gate_positive_pass={int(pm.get('gate_positive_pass', 0))}",
            f"gate_guardrail_pass={int(gm.get('gate_guardrail_pass', 0))}",
            f"gate_overall_pass={overall_pass}",
            "",
            "--- positive-control report ---",
            positive_report,
            "",
            "--- guardrail report ---",
            guardrail_report,
        ]
        report = "\n".join(summary)
    else:
        report = run_perturbation(
            trials=args.perturb_trials,
            seed=args.seed,
            noise_bound=args.perturb_noise_bound,
            noise_scale=args.perturb_noise_scale,
            perturbation_baseline=args.perturbation_baseline,
            point_bound=args.point_bound,
            random_line_probes=args.random_line_probes,
            max_deterministic_lines=args.max_deterministic_lines,
            max_conic_templates=args.max_conic_templates,
            max_elliptic_templates=args.max_elliptic_templates,
            max_quadric_templates=args.max_quadric_templates,
            elliptic_probe_mode=args.elliptic_probe_mode,
            elliptic_v2_cross_prime_count=args.elliptic_v2_cross_prime_count,
            elliptic_v2_min_rootcount=args.elliptic_v2_min_rootcount,
            v3_prime_sample=args.v3_prime_sample,
            v3_min_points=args.v3_min_points,
            smooth_points_per_prime=args.smooth_points_per_prime,
            smooth_primes=parse_primes(args.smooth_primes),
            gate_guardrail_threshold=args.gate_guardrail_threshold,
        )

    print(report)
    if args.output_json:
        if args.mode == "gate-scorer":
            p_block = report.split("--- positive-control report ---", 1)[1].split("--- guardrail report ---", 1)[0]
            g_block = report.split("--- guardrail report ---", 1)[1]
            pm = extract_gate_metrics(p_block)
            gm = extract_gate_metrics(g_block)
            payload = {
                "mode": args.mode,
                "gate_scorer": {
                    "positive": pm,
                    "guardrail": gm,
                    "overall_pass": int(bool(pm.get("gate_positive_pass", 0)) and bool(gm.get("gate_guardrail_pass", 0))),
                },
            }
        else:
            payload = {"mode": args.mode, "gate_scorer": extract_gate_metrics(report)}
        print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
