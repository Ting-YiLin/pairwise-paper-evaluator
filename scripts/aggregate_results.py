#!/usr/bin/env python3
"""Summarize original edges only; reversed audits are not extra votes."""
import json
import sys
from pathlib import Path
from validate_results import validate

def summarize(data):
    originals = [edge for edge in data["edges"] if edge["position_variant"] == "original"]
    wins = ties = 0
    for edge in originals:
        if edge["overall"] == "tie":
            ties += 1
        elif edge["overall"] == "left":
            wins += 1
    n = len(originals)
    return {"original_edges": n, "wins_for_left_target": wins, "ties": ties,
            "target_score": (wins + 0.5 * ties) / n if n else None,
            "interpretation": "Local summary for this specified edge set only; not a universal rank or acceptance probability."}

def main():
    if len(sys.argv) != 2:
        print("usage: python scripts/aggregate_results.py RESULTS.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}")
        return 1
    errors = validate(data)
    if errors:
        print("INVALID: run scripts/validate_results.py for details")
        return 1
    print(json.dumps(summarize(data), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
