#!/usr/bin/env python3
"""Validate pairwise result structure and reversal audit consistency."""
import json
import sys
from pathlib import Path

REQUIRED = {"pair_id", "left", "right", "overall", "confidence", "near_tie", "position_variant", "decision_hinge", "evidence_locators"}

def winner(edge):
    if edge["overall"] == "tie":
        return "tie"
    return edge["left"] if edge["overall"] == "left" else edge["right"]

def validate(data):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != "1.0" or not isinstance(data.get("edges"), list):
        return ["root must contain schema_version 1.0 and an edges array"]
    seen = set()
    variants = {}
    for index, edge in enumerate(data["edges"]):
        label = f"edges[{index}]"
        if not isinstance(edge, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = REQUIRED - edge.keys()
        if missing:
            errors.append(f"{label} missing: {', '.join(sorted(missing))}")
            continue
        if not all(isinstance(edge[k], str) and edge[k].strip() for k in ("pair_id", "left", "right", "decision_hinge")):
            errors.append(f"{label} IDs and decision_hinge must be non-empty strings")
        if edge.get("left") == edge.get("right"):
            errors.append(f"{label} left and right must differ")
        if edge.get("overall") not in ("left", "right", "tie"):
            errors.append(f"{label} overall must be left, right, or tie")
        if edge.get("confidence") not in ("high", "medium", "low"):
            errors.append(f"{label} confidence must be high, medium, or low")
        if not isinstance(edge.get("near_tie"), bool):
            errors.append(f"{label} near_tie must be boolean")
        if edge.get("position_variant") not in ("original", "reversed"):
            errors.append(f"{label} position_variant must be original or reversed")
        if not isinstance(edge.get("evidence_locators"), list) or not all(isinstance(x, str) for x in edge.get("evidence_locators", [])):
            errors.append(f"{label} evidence_locators must be an array of strings")
        key = (edge.get("pair_id"), edge.get("position_variant"))
        if key in seen:
            errors.append(f"duplicate pair_id/position_variant: {key[0]}/{key[1]}")
        seen.add(key)
        variants.setdefault(edge.get("pair_id"), []).append(edge)
    for pair_id, group in variants.items():
        original = [e for e in group if e.get("position_variant") == "original"]
        reversed_edges = [e for e in group if e.get("position_variant") == "reversed"]
        if len(original) != 1:
            errors.append(f"{pair_id} must have exactly one original edge")
        if len(reversed_edges) > 1:
            errors.append(f"{pair_id} may have at most one reversed audit")
        if original and reversed_edges:
            a, b = original[0], reversed_edges[0]
            if a.get("left") != b.get("right") or a.get("right") != b.get("left"):
                errors.append(f"{pair_id} reversed audit must swap left and right IDs")
            elif winner(a) != winner(b):
                errors.append(f"{pair_id} reversed audit changed substantive direction")
    return errors

def main():
    if len(sys.argv) != 2:
        print("usage: python scripts/validate_results.py RESULTS.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}")
        return 1
    errors = validate(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID edges={len(data['edges'])}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
