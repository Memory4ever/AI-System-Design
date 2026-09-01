#!/usr/bin/env python3
"""Build deterministic SFT, preference, rollout, and evaluation fixtures."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from dataclasses import dataclass
from pathlib import Path


SEED = 3407
SYSTEM_RULE = '只输出一个 JSON 对象，不要解释，格式必须为 {"answer": <integer>}。'


@dataclass(frozen=True)
class Problem:
    expression: str
    answer: int
    distribution: str

    @property
    def prompt(self) -> str:
        return f"计算 {self.expression}。{SYSTEM_RULE}"

    @property
    def response(self) -> str:
        return json.dumps({"answer": self.answer}, ensure_ascii=False)


def build_in_distribution() -> list[Problem]:
    problems: dict[str, Problem] = {}
    for a in range(2, 22):
        for b in range(1, 11):
            candidates = (
                Problem(f"{a} + {b}", a + b, "in_distribution"),
                Problem(f"{a + b} - {b}", a, "in_distribution"),
                Problem(f"{a} * {b}", a * b, "in_distribution"),
            )
            for problem in candidates:
                problems[problem.expression] = problem
    values = list(problems.values())
    random.Random(SEED).shuffle(values)
    return values


def build_ood() -> list[Problem]:
    problems: list[Problem] = []
    for i in range(1, 13):
        problems.extend(
            [
                Problem(f"({i} + 7) * 3", (i + 7) * 3, "compositional_ood"),
                Problem(f"-{i} + 5", -i + 5, "negative_ood"),
                Problem(f"{i * 12} / 4", i * 3, "division_ood"),
            ]
        )
    return problems


def rejected_response(problem: Problem, index: int) -> str:
    variants = (
        json.dumps({"answer": problem.answer + 1}, ensure_ascii=False),
        f"答案是 {problem.answer}",
        json.dumps({"result": problem.answer}, ensure_ascii=False),
        f"verified: {json.dumps({'answer': problem.answer + 2})}",
    )
    return variants[index % len(variants)]


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def build_records() -> dict[str, list[dict]]:
    in_distribution = build_in_distribution()
    train = in_distribution[:120]
    valid = in_distribution[120:150]
    evaluation = valid + build_ood()

    def base_record(problem: Problem, index: int, split: str) -> dict:
        return {
            "id": f"arith-{split}-{index:04d}",
            "prompt": problem.prompt,
            "answer": str(problem.answer),
            "distribution": problem.distribution,
        }

    sft_train = [
        {**base_record(problem, index, "train"), "response": problem.response}
        for index, problem in enumerate(train)
    ]
    sft_valid = [
        {**base_record(problem, index, "valid"), "response": problem.response}
        for index, problem in enumerate(valid)
    ]
    preference_train = []
    for index, problem in enumerate(train):
        prefix = f"User: {problem.prompt}\nAssistant: "
        preference_train.append(
            {
                **base_record(problem, index, "train"),
                "chosen": prefix + problem.response,
                "rejected": prefix + rejected_response(problem, index),
            }
        )
    preference_valid = []
    for index, problem in enumerate(valid):
        prefix = f"User: {problem.prompt}\nAssistant: "
        preference_valid.append(
            {
                **base_record(problem, index, "valid"),
                "chosen": prefix + problem.response,
                "rejected": prefix + rejected_response(problem, index + 1),
            }
        )
    prompts_train = [base_record(problem, index, "train") for index, problem in enumerate(train)]
    prompts_valid = [base_record(problem, index, "valid") for index, problem in enumerate(valid)]
    eval_records = [
        base_record(problem, index, "evaluation") for index, problem in enumerate(evaluation)
    ]
    return {
        "sft_train.jsonl": sft_train,
        "sft_valid.jsonl": sft_valid,
        "preference_train.jsonl": preference_train,
        "preference_valid.jsonl": preference_valid,
        "prompts_train.jsonl": prompts_train,
        "prompts_valid.jsonl": prompts_valid,
        "evaluation.jsonl": eval_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parents[1] / "data")
    args = parser.parse_args()
    records = build_records()
    for name, rows in records.items():
        write_jsonl(args.output_dir / name, rows)
        print(f"wrote {name}: {len(rows)} rows")
    manifest = {
        "schema_version": 1,
        "generator": "scripts/build_dataset.py",
        "seed": SEED,
        "files": {},
    }
    for name, rows in sorted(records.items()):
        payload = (args.output_dir / name).read_bytes()
        manifest["files"][name] = {
            "rows": len(rows),
            "sha256": hashlib.sha256(payload).hexdigest(),
        }
    (args.output_dir / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("wrote MANIFEST.json")


if __name__ == "__main__":
    main()
