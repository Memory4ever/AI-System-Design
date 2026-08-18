#!/usr/bin/env python3
"""Report chat-template token lengths with the exact local tokenizer."""

from __future__ import annotations

import json
from pathlib import Path

from transformers import AutoTokenizer


RUN_ROOT = Path(__file__).resolve().parents[1]
MODEL = Path("/Users/apple/Downloads/Qwen3.5-4B")


def percentile(values: list[int], fraction: float) -> int:
    index = min(len(values) - 1, round((len(values) - 1) * fraction))
    return sorted(values)[index]


def main() -> None:
    tokenizer = AutoTokenizer.from_pretrained(MODEL, local_files_only=True)
    for split in ("train", "validation"):
        rows = [
            json.loads(line)
            for line in (RUN_ROOT / "dataset" / f"{split}.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        lengths = [
            len(
                tokenizer.apply_chat_template(
                    row["messages"], tokenize=True, add_generation_prompt=False
                )["input_ids"]
            )
            for row in rows
        ]
        print(
            f"{split}: count={len(lengths)} min={min(lengths)} "
            f"p50={percentile(lengths, 0.50)} p95={percentile(lengths, 0.95)} max={max(lengths)}"
        )


if __name__ == "__main__":
    main()
