#!/usr/bin/env python3
"""Validate the dataset and score saved base/adapter generations."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


RUN_ROOT = Path(__file__).resolve().parents[1]
DATASET = RUN_ROOT / "dataset"
HEADINGS = ("问题", "原理", "机制", "权衡", "系统连接", "演进")


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate_dataset() -> None:
    train = read_jsonl(DATASET / "train.jsonl")
    validation = read_jsonl(DATASET / "validation.jsonl")
    test = read_jsonl(DATASET / "test.jsonl")
    regression = read_jsonl(DATASET / "regression.jsonl")
    assert len(train) == 100, len(train)
    assert len(validation) == 20, len(validation)
    assert len(test) == 20, len(test)
    assert len(regression) == 10, len(regression)

    prompts: set[str] = set()
    for split_name, rows in (("train", train), ("validation", validation)):
        for index, row in enumerate(rows):
            messages = row["messages"]
            assert [message["role"] for message in messages] == ["system", "user", "assistant"]
            prompt = messages[1]["content"].strip()
            answer = messages[2]["content"]
            assert prompt not in prompts, f"duplicate prompt: {prompt}"
            prompts.add(prompt)
            positions = [answer.find(f"## {heading}") for heading in HEADINGS]
            assert all(position >= 0 for position in positions), (split_name, index, positions)
            assert positions == sorted(positions), (split_name, index, positions)

    for row in test:
        assert row["prompt"].strip() not in prompts, row["prompt"]
        assert len(row["expected_concepts"]) >= 4
    for row in regression:
        assert row["prompt"].strip() not in prompts
        assert row["expected_concepts"]
    print("dataset validation: PASS")


def score_outputs(path: Path) -> None:
    rows = read_jsonl(path)
    structure_passes = 0
    concept_hits = 0
    concept_total = 0
    for row in rows:
        output = str(row.get("output", ""))
        expected = [str(item).lower() for item in row.get("expected_concepts", [])]
        positions = [
            match.start() if (match := re.search(rf"(?m)^## {re.escape(heading)}\s*$", output)) else -1
            for heading in HEADINGS
        ]
        structure_passes += int(all(position >= 0 for position in positions) and positions == sorted(positions))
        lowered = output.lower()
        concept_hits += sum(concept in lowered for concept in expected)
        concept_total += len(expected)
    count = len(rows)
    print(f"samples={count}")
    print(f"structure_pass_rate={structure_passes / count:.3f}")
    print(f"concept_recall={concept_hits / concept_total:.3f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-dataset", action="store_true")
    parser.add_argument("--outputs", type=Path)
    args = parser.parse_args()
    if args.validate_dataset:
        validate_dataset()
    if args.outputs:
        score_outputs(args.outputs)
    if not args.validate_dataset and not args.outputs:
        parser.error("choose --validate-dataset or --outputs")


if __name__ == "__main__":
    main()
