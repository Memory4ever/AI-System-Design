#!/usr/bin/env python3
"""Capture the reproducibility fields that should accompany an L20 run."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path


SUITE_DIR = Path(__file__).resolve().parents[1]


def command_output(command: list[str]) -> str:
    try:
        return subprocess.run(command, check=True, capture_output=True, text=True).stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        return f"Not Available: {error}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_head": command_output(["git", "rev-parse", "HEAD"]),
        "git_status": command_output(["git", "status", "--short"]),
        "python": platform.python_version(),
        "pip_freeze": command_output(["python3", "-m", "pip", "freeze"]),
        "nvidia_smi": command_output(["nvidia-smi", "-q"]),
        "nvidia_topology": command_output(["nvidia-smi", "topo", "-m"]),
        "suite_dir": str(SUITE_DIR),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
