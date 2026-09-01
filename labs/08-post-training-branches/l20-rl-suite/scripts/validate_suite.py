#!/usr/bin/env python3
"""Validate dataset identity, config references, and experiment invariants."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from reward_func import score_text
from run_stage import build_command


SUITE_DIR = Path(__file__).resolve().parents[1]
REQUIRED_DATA = {
    "sft_train.jsonl": 120,
    "sft_valid.jsonl": 30,
    "preference_train.jsonl": 120,
    "preference_valid.jsonl": 30,
    "prompts_train.jsonl": 120,
    "prompts_valid.jsonl": 30,
    "evaluation.jsonl": 66,
}
STAGES = {"sft", "reward", "dpo", "ppo", "rloo", "grpo"}


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def validate_data() -> None:
    manifest = json.loads((SUITE_DIR / "data/MANIFEST.json").read_text(encoding="utf-8"))
    if manifest["seed"] != 3407 or set(manifest["files"]) != set(REQUIRED_DATA):
        raise AssertionError("dataset manifest identity does not match the suite contract")
    datasets = {}
    for name, expected_count in REQUIRED_DATA.items():
        path = SUITE_DIR / "data" / name
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if manifest["files"][name] != {"rows": expected_count, "sha256": digest}:
            raise AssertionError(f"{name}: manifest digest or count mismatch")
        rows = read_jsonl(path)
        if len(rows) != expected_count:
            raise AssertionError(f"{name}: expected {expected_count}, found {len(rows)}")
        ids = [row["id"] for row in rows]
        if len(ids) != len(set(ids)):
            raise AssertionError(f"{name}: duplicate ids")
        datasets[name] = rows

    train_prompts = {row["prompt"] for row in datasets["prompts_train.jsonl"]}
    valid_prompts = {row["prompt"] for row in datasets["prompts_valid.jsonl"]}
    if train_prompts & valid_prompts:
        raise AssertionError("train/validation prompt leakage")

    for row in datasets["sft_train.jsonl"] + datasets["sft_valid.jsonl"]:
        score = score_text(row["response"], row["answer"])
        if not score.exact or not score.strict_format:
            raise AssertionError(f"invalid SFT target: {row['id']}")
    for row in datasets["preference_train.jsonl"] + datasets["preference_valid.jsonl"]:
        chosen = score_text(row["chosen"], row["answer"])
        rejected = score_text(row["rejected"], row["answer"])
        if not chosen.exact or rejected.exact:
            raise AssertionError(f"invalid preference ordering: {row['id']}")


def validate_configs() -> None:
    profiles = json.loads((SUITE_DIR / "configs/profiles.json").read_text(encoding="utf-8"))
    stages = json.loads((SUITE_DIR / "configs/stages.json").read_text(encoding="utf-8"))
    if set(stages["stages"]) != STAGES:
        raise AssertionError("stage set drifted from the lab contract")
    if profiles["runtime"]["version"] != "0.10.2":
        raise AssertionError("OpenRLHF version must be reviewed before changing the CLI contract")
    unresolved = re.compile(r"\$\{[^}]+\}")
    for profile_name, profile in profiles["profiles"].items():
        if profile["ppo_train_batch_size"] != profile["rollout_batch_size"]:
            raise AssertionError(f"{profile_name}: PPO train batch must match one sample per rollout prompt")
        expected_group_batch = profile["rollout_batch_size"] * profile["samples_per_prompt"]
        if profile["group_train_batch_size"] != expected_group_batch:
            raise AssertionError(
                f"{profile_name}: group train batch must equal rollout batch times samples per prompt"
            )
        if not profile["enabled"]:
            continue
        for stage in sorted(STAGES):
            command, receipt = build_command(stage, profile_name, SUITE_DIR / "artifacts", None)
            rendered = " ".join(command)
            if unresolved.search(rendered):
                raise AssertionError(f"unresolved placeholder in {profile_name}/{stage}")
            if receipt["status"] != "Not Run":
                raise AssertionError("rendering a command must not claim execution")


def main() -> None:
    validate_data()
    validate_configs()
    print("PASS: dataset schemas, split isolation, preference ordering, and stage configs")


if __name__ == "__main__":
    main()
