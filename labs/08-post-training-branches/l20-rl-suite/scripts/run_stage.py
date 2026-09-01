#!/usr/bin/env python3
"""Render or execute one OpenRLHF stage from the structured experiment contract."""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


SUITE_DIR = Path(__file__).resolve().parents[1]
PLACEHOLDER = re.compile(r"\$\{([A-Z0-9_]+)\}")
ONLINE_STAGES = {"ppo", "rloo", "grpo"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def substitutions(profile: dict, artifact_root: Path, base_model: str) -> dict[str, str]:
    return {
        "SUITE_DIR": str(SUITE_DIR),
        "DATA_DIR": str(SUITE_DIR / "data"),
        "ARTIFACT_ROOT": str(artifact_root),
        "BASE_MODEL": base_model,
        "GPU_COUNT": str(profile["gpu_count"]),
        "MAX_LEN": str(profile["max_len"]),
        "ROLLOUT_MAX_NEW_TOKENS": str(profile["rollout_max_new_tokens"]),
        "OFFLINE_TRAIN_BATCH_SIZE": str(profile["offline_train_batch_size"]),
        "PPO_TRAIN_BATCH_SIZE": str(profile["ppo_train_batch_size"]),
        "GROUP_TRAIN_BATCH_SIZE": str(profile["group_train_batch_size"]),
        "TRAIN_MICRO_BATCH_SIZE": str(profile["train_micro_batch_size"]),
        "ROLLOUT_BATCH_SIZE": str(profile["rollout_batch_size"]),
        "ROLLOUT_MICRO_BATCH_SIZE": str(profile["rollout_micro_batch_size"]),
        "SAMPLES_PER_PROMPT": str(profile["samples_per_prompt"]),
        "ZERO_STAGE": str(profile["zero_stage"]),
        "VLLM_GPU_MEMORY_UTILIZATION": str(profile["vllm_gpu_memory_utilization"]),
    }


def resolve(value: str, values: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise ValueError(f"unknown config placeholder: {key}")
        return values[key]

    return PLACEHOLDER.sub(replace, value)


def flatten_args(args: dict, values: dict[str, str]) -> list[str]:
    rendered: list[str] = []
    for key, value in args.items():
        rendered.append(key)
        if value is True:
            continue
        if value is False or value is None:
            rendered.pop()
            continue
        rendered.append(resolve(str(value), values))
    return rendered


def validate_model_identity(model: str) -> None:
    lowered = model.lower()
    if lowered.endswith(".gguf") or "-gguf" in lowered:
        raise ValueError(
            "GGUF is an inference artifact, not the trainable Hugging Face checkpoint required by this suite"
        )
    if model == "REQUIRED_HF_MODEL_PATH":
        raise ValueError("set MODEL_ID to a trainable Hugging Face checkpoint or local safetensors directory")


def preflight(stage: str, profile: dict, base_model: str, artifact_root: Path) -> None:
    validate_model_identity(base_model)
    if not profile["enabled"] and os.environ.get("ALLOW_DISABLED_PROFILE") != "1":
        raise ValueError("profile is disabled; set ALLOW_DISABLED_PROFILE=1 after reviewing its memory budget")
    if shutil.which("nvidia-smi") is None:
        raise RuntimeError("nvidia-smi was not found; execute this stage in the NVIDIA L20 environment")
    result = subprocess.run(
        ["nvidia-smi", "--query-gpu=index", "--format=csv,noheader"],
        check=True,
        capture_output=True,
        text=True,
    )
    visible = len([line for line in result.stdout.splitlines() if line.strip()])
    if visible < profile["gpu_count"]:
        raise RuntimeError(f"profile requires {profile['gpu_count']} GPUs, but nvidia-smi exposes {visible}")
    if stage in {"reward", "dpo", *ONLINE_STAGES} and not (artifact_root / "sft").exists():
        raise FileNotFoundError(f"missing SFT artifact: {artifact_root / 'sft'}")
    if stage == "ppo" and not (artifact_root / "reward").exists():
        raise FileNotFoundError(f"missing Reward Model artifact: {artifact_root / 'reward'}")


def build_command(stage: str, profile_name: str, artifact_root: Path, base_model_override: str | None) -> tuple[list[str], dict]:
    profiles = load_json(SUITE_DIR / "configs/profiles.json")["profiles"]
    stages = load_json(SUITE_DIR / "configs/stages.json")["stages"]
    if profile_name not in profiles:
        raise ValueError(f"unknown profile {profile_name}; choose from {', '.join(profiles)}")
    if stage not in stages:
        raise ValueError(f"unknown stage {stage}; choose from {', '.join(stages)}")
    profile = profiles[profile_name]
    stage_config = stages[stage]
    base_model = base_model_override or os.environ.get("MODEL_ID") or profile["base_model"]
    validate_model_identity(base_model)
    values = substitutions(profile, artifact_root, base_model)
    module_args = ["python3", "-m", stage_config["module"], *flatten_args(stage_config["args"], values)]
    if stage_config["kind"] == "offline":
        command = ["deepspeed", "--num_gpus", str(profile["gpu_count"]), "--module", stage_config["module"]]
        command.extend(flatten_args(stage_config["args"], values))
    else:
        ray_address = os.environ.get("RAY_ADDRESS", "http://127.0.0.1:8265")
        runtime_env = json.dumps(
            {
                "working_dir": str(SUITE_DIR),
                "excludes": ["/artifacts/", "/outputs/", "/reports/", "/generated-jobs/"],
            },
            separators=(",", ":"),
        )
        command = [
            "ray",
            "job",
            "submit",
            f"--address={ray_address}",
            f"--runtime-env-json={runtime_env}",
            "--",
            *module_args,
        ]
    receipt = {
        "stage": stage,
        "profile": profile_name,
        "base_model": base_model,
        "gpu_count": profile["gpu_count"],
        "artifact_root": str(artifact_root),
        "framework": "OpenRLHF 0.10.2",
        "status": "Not Run",
        "command": command,
    }
    return command, receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True)
    parser.add_argument("--profile", default="smoke-1xl20")
    parser.add_argument("--artifact-root", type=Path, default=SUITE_DIR / "artifacts")
    parser.add_argument("--model-id")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()

    artifact_root = args.artifact_root.resolve()
    command, receipt = build_command(args.stage, args.profile, artifact_root, args.model_id)
    print(shlex.join(command))
    if not args.execute:
        if args.receipt:
            args.receipt.parent.mkdir(parents=True, exist_ok=True)
            args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return

    receipt_path = args.receipt or artifact_root / "receipts" / f"{args.stage}.json"
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    profile = load_json(SUITE_DIR / "configs/profiles.json")["profiles"][args.profile]
    try:
        preflight(args.stage, profile, receipt["base_model"], artifact_root)
        executable = command[0]
        if shutil.which(executable) is None:
            raise RuntimeError(f"required executable was not found: {executable}")
    except Exception as error:
        receipt.update(
            {
                "status": "Preflight Failed",
                "error": f"{type(error).__name__}: {error}",
                "finished_at_utc": datetime.now(timezone.utc).isoformat(),
                "experiment_gate": "Not Evaluated",
            }
        )
        receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        raise

    receipt.update(
        {
            "status": "Process Running",
            "started_at_utc": datetime.now(timezone.utc).isoformat(),
            "experiment_gate": "Not Evaluated",
        }
    )
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    completed = subprocess.run(command, check=False, cwd=SUITE_DIR)
    receipt["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
    receipt["return_code"] = completed.returncode
    if completed.returncode == 0:
        receipt["status"] = "Process Exited 0"
        receipt["experiment_gate"] = "Pending Checkpoint Reload and Held-out Evaluation"
    else:
        receipt["status"] = "Process Failed"
        receipt["experiment_gate"] = "Not Evaluated"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(completed.returncode, command)


if __name__ == "__main__":
    main()
