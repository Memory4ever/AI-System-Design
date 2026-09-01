#!/usr/bin/env python3
"""OpenRLHF-compatible reward function plus dependency-free scoring helpers."""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass


ASSISTANT_MARKER = "Assistant:"
FINAL_JSON = re.compile(r"\{\s*\"answer\"\s*:\s*(-?\d+)\s*\}\s*$")


@dataclass(frozen=True)
class Score:
    exact: bool
    strict_format: bool
    shortcut: bool

    def reward(self, mode: str = "faithful") -> float:
        if mode == "shortcut":
            return 1.0 if self.shortcut else 0.0
        if mode != "faithful":
            raise ValueError(f"unsupported REWARD_MODE: {mode}")
        return (0.8 if self.exact else 0.0) + (0.2 if self.strict_format else 0.0)


def candidate_text(query: str) -> str:
    return query.rsplit(ASSISTANT_MARKER, 1)[-1].strip()


def score_text(query: str, label: str | int) -> Score:
    candidate = candidate_text(query)
    match = FINAL_JSON.fullmatch(candidate)
    parsed = int(match.group(1)) if match else None
    expected = int(label)
    return Score(
        exact=parsed == expected,
        strict_format=match is not None,
        shortcut="verified" in candidate.lower(),
    )


def reward_func(queries, prompts, labels):
    """Return the OpenRLHF 0.10.2 local reward-function contract."""
    import torch

    del prompts
    mode = os.environ.get("REWARD_MODE", "faithful")
    scores = [score_text(query, label) for query, label in zip(queries, labels)]
    rewards = torch.tensor([score.reward(mode) for score in scores], dtype=torch.float32)
    exact = torch.tensor([float(score.exact) for score in scores], dtype=torch.float32)
    return {
        "rewards": rewards,
        "scores": exact,
        "extra_logs": {
            "exact_accuracy": exact.mean().item(),
            "strict_format_rate": sum(score.strict_format for score in scores) / max(len(scores), 1),
            "shortcut_rate": sum(score.shortcut for score in scores) / max(len(scores), 1),
        },
    }


if __name__ == "__main__":
    sample = 'User: 1 + 1\nAssistant: ' + json.dumps({"answer": 2})
    print(score_text(sample, "2"))
