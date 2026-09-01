#!/usr/bin/env python3
"""Score saved model outputs with a verifier independent from the trainer."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from reward_func import score_text


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evaluation", type=Path, default=Path(__file__).parents[1] / "data/evaluation.jsonl")
    parser.add_argument("--outputs", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    expected = {row["id"]: row for row in read_jsonl(args.evaluation)}
    outputs = read_jsonl(args.outputs)
    if len(outputs) != len(expected):
        raise SystemExit(f"expected {len(expected)} outputs, found {len(outputs)}")

    by_distribution: dict[str, dict[str, int]] = {}
    seen: set[str] = set()
    details = []
    for row in outputs:
        sample_id = row["id"]
        if sample_id in seen or sample_id not in expected:
            raise SystemExit(f"duplicate or unknown output id: {sample_id}")
        seen.add(sample_id)
        target = expected[sample_id]
        score = score_text(row["output"], target["answer"])
        bucket = by_distribution.setdefault(
            target["distribution"], {"count": 0, "exact": 0, "strict_format": 0, "shortcut": 0}
        )
        bucket["count"] += 1
        bucket["exact"] += int(score.exact)
        bucket["strict_format"] += int(score.strict_format)
        bucket["shortcut"] += int(score.shortcut)
        details.append({"id": sample_id, **score.__dict__})

    summary = {"count": len(outputs), "by_distribution": {}}
    for name, counts in sorted(by_distribution.items()):
        denominator = counts["count"]
        summary["by_distribution"][name] = {
            "count": denominator,
            "exact_accuracy": counts["exact"] / denominator,
            "strict_format_rate": counts["strict_format"] / denominator,
            "shortcut_rate": counts["shortcut"] / denominator,
        }
    payload = {"summary": summary, "details": details}
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    print(rendered)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
