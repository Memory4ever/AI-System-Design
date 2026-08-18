#!/usr/bin/env python3
"""Generate deterministic base or adapter outputs with the local MLX runtime."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import mlx.core as mx
from mlx_lm import generate, load
from mlx_lm.sample_utils import make_sampler


RUN_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = "/Users/apple/Downloads/Qwen3.5-4B"


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cases", type=Path, default=RUN_ROOT / "dataset" / "test.jsonl")
    parser.add_argument("--adapter-path", type=str)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--max-tokens", type=int, default=512)
    args = parser.parse_args()

    cases = read_jsonl(args.cases)
    if args.limit:
        cases = cases[: args.limit]

    started = time.time()
    model, tokenizer = load(MODEL_PATH, adapter_path=args.adapter_path)
    load_seconds = time.time() - started
    sampler = make_sampler(temp=0.7, top_p=0.8, top_k=20)

    rows: list[dict[str, object]] = []
    for index, case in enumerate(cases):
        mx.random.seed(3407 + index)
        messages = [
            {"role": "system", "content": case["system"]},
            {"role": "user", "content": case["prompt"]},
        ]
        prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
        prompt_ids = tokenizer.encode(prompt, add_special_tokens=False)
        sample_started = time.time()
        output = generate(
            model,
            tokenizer,
            prompt_ids,
            max_tokens=args.max_tokens,
            sampler=sampler,
            verbose=False,
        )
        rows.append(
            {
                **case,
                "output": output,
                "seed": 3407 + index,
                "elapsed_seconds": round(time.time() - sample_started, 3),
                "adapter_path": args.adapter_path,
            }
        )
        print(f"[{index + 1}/{len(cases)}] {case['id']}", flush=True)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )
    print(f"model_load_seconds={load_seconds:.3f}")
    print(f"total_seconds={time.time() - started:.3f}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
