#!/usr/bin/env python3
"""Render a single-node Kubernetes Job as JSON for a selected L20 profile."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SUITE_DIR = Path(__file__).resolve().parents[1]


def dns_label(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")
    return normalized[:63].rstrip("-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True, choices=("sft", "reward", "dpo", "ppo", "rloo", "grpo"))
    parser.add_argument("--profile", required=True)
    parser.add_argument("--image", required=True)
    parser.add_argument("--pvc", required=True, help="PVC containing the repository and persistent artifacts")
    parser.add_argument("--run-id", required=True, help="Unique identity used by the Job and artifact directory")
    parser.add_argument("--namespace", default="default")
    parser.add_argument("--repo-subpath", default="AI-System-Design")
    parser.add_argument("--model-id")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    job_profiles = json.loads((SUITE_DIR / "jobs/profiles.json").read_text(encoding="utf-8"))["profiles"]
    experiment_profiles = json.loads((SUITE_DIR / "configs/profiles.json").read_text(encoding="utf-8"))["profiles"]
    if args.profile not in job_profiles or args.profile not in experiment_profiles:
        raise SystemExit(f"unknown profile: {args.profile}")
    resources = job_profiles[args.profile]
    if resources["gpu_count"] != experiment_profiles[args.profile]["gpu_count"]:
        raise SystemExit("GPU count differs between experiment and Job profiles")

    suite_path = f"/workspace/{args.repo_subpath}/labs/08-post-training-branches/l20-rl-suite"
    environment = [
        {"name": "STAGE", "value": args.stage},
        {"name": "PROFILE", "value": args.profile},
        {"name": "GPU_COUNT", "value": str(resources["gpu_count"])},
        {"name": "ARTIFACT_ROOT", "value": f"{suite_path}/artifacts"},
        {"name": "TOKENIZERS_PARALLELISM", "value": "false"},
        {"name": "NCCL_DEBUG", "value": "WARN"},
    ]
    if args.model_id:
        environment.append({"name": "MODEL_ID", "value": args.model_id})

    run_id = dns_label(args.run_id)
    if not run_id:
        raise SystemExit("run-id must contain at least one lowercase letter or digit")
    name = dns_label(f"rl-lab-{args.stage}-{run_id}")
    for item in environment:
        if item["name"] == "ARTIFACT_ROOT":
            item["value"] = f"{suite_path}/artifacts/{run_id}"
    manifest = {
        "apiVersion": "batch/v1",
        "kind": "Job",
        "metadata": {"name": name, "namespace": args.namespace},
        "spec": {
            "backoffLimit": 0,
            "template": {
                "metadata": {
                    "labels": {
                        "app.kubernetes.io/name": "l20-rl-lab",
                        "ai-system-design/stage": args.stage,
                        "ai-system-design/profile": args.profile,
                        "ai-system-design/run-id": run_id,
                    }
                },
                "spec": {
                    "restartPolicy": "Never",
                    "containers": [
                        {
                            "name": "trainer",
                            "image": args.image,
                            "imagePullPolicy": "IfNotPresent",
                            "workingDir": suite_path,
                            "command": ["bash", "scripts/run_in_job.sh"],
                            "env": environment,
                            "resources": {
                                "requests": {
                                    "cpu": resources["cpu"],
                                    "memory": resources["memory"],
                                    "nvidia.com/gpu": str(resources["gpu_count"]),
                                },
                                "limits": {
                                    "cpu": resources["cpu"],
                                    "memory": resources["memory"],
                                    "nvidia.com/gpu": str(resources["gpu_count"]),
                                },
                            },
                            "volumeMounts": [{"name": "workspace", "mountPath": "/workspace"}],
                        }
                    ],
                    "volumes": [
                        {"name": "workspace", "persistentVolumeClaim": {"claimName": args.pvc}}
                    ],
                },
            },
        },
    }
    rendered = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
