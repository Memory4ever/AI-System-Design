#!/usr/bin/env python3
"""Generate deterministic evaluation outputs with vLLM."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--evaluation", type=Path, default=Path(__file__).parents[1] / "data/evaluation.jsonl")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tensor-parallel-size", type=int, default=1)
    parser.add_argument("--max-model-len", type=int, default=1024)
    parser.add_argument("--max-tokens", type=int, default=160)
    parser.add_argument("--seed", type=int, default=3407)
    args = parser.parse_args()

    from vllm import LLM, SamplingParams

    rows = read_jsonl(args.evaluation)
    prompts = [f"User: {row['prompt']}\nAssistant: " for row in rows]
    model = LLM(
        model=args.model,
        tensor_parallel_size=args.tensor_parallel_size,
        max_model_len=args.max_model_len,
        seed=args.seed,
        trust_remote_code=False,
    )
    sampling = SamplingParams(temperature=0.0, max_tokens=args.max_tokens, seed=args.seed)
    generated = model.generate(prompts, sampling)
    records = [
        {
            "id": row["id"],
            "model": args.model,
            "prompt": prompt,
            "output": prompt + result.outputs[0].text,
        }
        for row, prompt, result in zip(rows, prompts, generated)
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
