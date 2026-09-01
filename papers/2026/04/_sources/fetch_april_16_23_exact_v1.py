#!/usr/bin/env python3
"""Fetch official exact-v1 arXiv HTML for the April 16--23 author lane.

This helper consumes only the strict-window semantic admission decisions in
``build_april_16_23_lane.py``.  It does not read Weekly reports or reuse their
review state.  Each response stays in the owning date-local source packet so
the subsequent review renderer can cite and hash the exact body it read.
"""

from __future__ import annotations

import importlib.util
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
GENERATOR = Path(__file__).with_name("build_april_16_23_lane.py")


def load_generator():
    spec = importlib.util.spec_from_file_location("april_lane", GENERATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def fetch(day: int, arxiv_id: str) -> tuple[int, str, str]:
    target_dir = ROOT / "papers/2026/04/_sources" / f"daily-202604{day:02d}" / "exact-v1-html"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{arxiv_id}v1.html"
    if target.exists() and target.stat().st_size > 10_000:
        return day, arxiv_id, "cached"
    proc = subprocess.run(
        [
            "curl", "--http1.1", "-L", "--fail", "--silent", "--show-error",
            "--retry", "4", "--retry-all-errors", "--retry-delay", "2", "--max-time", "60",
            "-o", str(target), f"https://arxiv.org/html/{arxiv_id}v1",
        ],
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0 and target.exists() and target.stat().st_size > 10_000:
        return day, arxiv_id, "downloaded"
    if target.exists():
        target.unlink()
    return day, arxiv_id, "failed:" + proc.stderr.strip()[:240]


def main() -> None:
    module = load_generator()
    jobs = [(day, arxiv_id) for day in range(16, 24) for arxiv_id in module.SELECTED[day]]
    results = []
    # arXiv rate-limits/reset bursts aggressively.  Two bounded workers are
    # deliberate: exact-version completeness is more important than speed.
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(fetch, day, arxiv_id) for day, arxiv_id in jobs]
        for future in as_completed(futures):
            results.append(future.result())
    failed = [(day, aid, status) for day, aid, status in results if status.startswith("failed:")]
    print(f"exact-v1 html: total={len(results)} ok={len(results)-len(failed)} failed={len(failed)}")
    for day, aid, status in sorted(failed):
        print(f"2026-04-{day:02d} {aid} {status}")


if __name__ == "__main__":
    main()
