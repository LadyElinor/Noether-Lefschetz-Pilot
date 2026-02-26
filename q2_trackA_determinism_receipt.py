#!/usr/bin/env python3
"""
Q2 Track A determinism receipt helper.

Compares two run-output files and emits a compact, auditable receipt:
- byte-level SHA256 hashes
- full-text equality verdict
- selected summary counters (if present)

Conservative use: operational implementation check only.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

KEYS = [
    "smoothness_screen_pass",
    "smoothness_screen_flagged",
    "random_samples_with_any_detected_line",
    "random_samples_with_any_detected_conic_template",
    "random_samples_with_any_detected_elliptic_template",
    "random_samples_with_any_detected_elliptic_v2_surrogate",
    "random_samples_with_any_detected_elliptic_v3_quadric",
    "base_smoothness_screen",
    "perturbed_smooth_pass",
    "perturbed_line_detected",
    "perturbed_conic_template_detected",
    "perturbed_elliptic_template_detected",
    "perturbed_elliptic_v2_surrogate_detected",
    "gate_guardrail_fp_hits",
    "gate_guardrail_fp_total",
    "gate_guardrail_fp_rate",
    "gate_guardrail_threshold",
    "gate_guardrail_pass",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def decode_text(data: bytes) -> str:
    """Best-effort text decode for mixed run-log encodings (UTF-8 / UTF-16LE)."""
    if b"\x00" in data:
        try:
            return data.decode("utf-16")
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace")


def extract_keyvals(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for key in KEYS:
        m = re.search(rf"^{re.escape(key)}\s*[:=]\s*(.+)$", text, flags=re.MULTILINE)
        if m:
            out[key] = m.group(1).strip()
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--a", required=True, help="first run output file")
    p.add_argument("--b", required=True, help="second run output file")
    p.add_argument("--label", default="determinism-check", help="receipt label")
    p.add_argument(
        "--require-identical",
        action="store_true",
        help="exit with code 1 if compared files are not text-identical",
    )
    p.add_argument(
        "--require-key-match",
        action="store_true",
        help="exit with code 1 if any shared summary key has differing values",
    )
    p.add_argument(
        "--require-min-shared-keys",
        type=int,
        default=0,
        help="exit with code 1 if fewer than this many summary keys are shared",
    )
    args = p.parse_args()

    pa = Path(args.a)
    pb = Path(args.b)

    ba = pa.read_bytes()
    bb = pb.read_bytes()

    ta = decode_text(ba)
    tb = decode_text(bb)

    same_text = ta == tb
    ha = sha256_bytes(ba)
    hb = sha256_bytes(bb)

    kva = extract_keyvals(ta)
    kvb = extract_keyvals(tb)

    all_keys = sorted(set(kva) | set(kvb))
    shared_keys = sorted(set(kva) & set(kvb))
    mismatched_shared_keys = [k for k in shared_keys if kva[k] != kvb[k]]

    print(f"label: {args.label}")
    print(f"file_a: {pa.name}")
    print(f"file_b: {pb.name}")
    print(f"sha256_a: {ha}")
    print(f"sha256_b: {hb}")
    print(f"byte_identical_sha256: {str(ha == hb).lower()}")
    print(f"text_identical: {str(same_text).lower()}")
    print(f"shared_summary_key_count: {len(shared_keys)}")
    print(f"shared_summary_key_match: {str(len(mismatched_shared_keys) == 0).lower()}")

    if all_keys:
        print("summary_keys_present:")
        for k in all_keys:
            va = kva.get(k, "<missing>")
            vb = kvb.get(k, "<missing>")
            status = "match" if va == vb else "diff"
            print(f"  - {k}: a={va} | b={vb} | {status}")

    if args.require_identical and not same_text:
        print("require_identical_check: fail")
        return 1
    if args.require_identical:
        print("require_identical_check: pass")

    if args.require_min_shared_keys > len(shared_keys):
        print("require_min_shared_keys_check: fail")
        print(f"require_min_shared_keys_expected: {args.require_min_shared_keys}")
        print(f"require_min_shared_keys_observed: {len(shared_keys)}")
        return 1
    if args.require_min_shared_keys > 0:
        print("require_min_shared_keys_check: pass")
        print(f"require_min_shared_keys_expected: {args.require_min_shared_keys}")
        print(f"require_min_shared_keys_observed: {len(shared_keys)}")

    if args.require_key_match and mismatched_shared_keys:
        print("require_key_match_check: fail")
        print("require_key_match_mismatched_keys:")
        for k in mismatched_shared_keys:
            print(f"  - {k}")
        return 1
    if args.require_key_match:
        print("require_key_match_check: pass")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
