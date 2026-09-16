#!/usr/bin/env python3
"""Fetch immutable arXiv v1 HTML for the frozen 2026-05-05 denominator."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "V3_CANONICAL_LEDGER.json"
OUT = HERE / "arxiv-v1-html"
OUT.mkdir(exist_ok=True)


def fetch(arxiv_id: str) -> tuple[str, str]:
    path = OUT / f"{arxiv_id}v1.html"
    if path.exists() and path.stat().st_size > 1000:
        return arxiv_id, "cached"
    request = urllib.request.Request(
        f"https://arxiv.org/html/{arxiv_id}v1",
        headers={"User-Agent": "AI-System-Design research audit (non-commercial)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read()
        path.write_bytes(body)
        return arxiv_id, f"ok:{len(body)}"
    except (urllib.error.URLError, TimeoutError) as error:
        return arxiv_id, f"blocked:{type(error).__name__}:{error}"


def main() -> None:
    payload = json.loads(LEDGER.read_text())
    ids = [
        entry["arxiv_id"]
        for entry in payload["entries"]
        if "retain" in entry["semantic_decision"]
    ]
    results = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(fetch, arxiv_id): arxiv_id for arxiv_id in ids}
        for future in as_completed(futures):
            results.append(future.result())
            time.sleep(0.08)
    results.sort()
    (HERE / "exact-v1-fetch-results.json").write_text(
        json.dumps({"requested": len(ids), "results": results}, ensure_ascii=False, indent=2) + "\n"
    )
    counts: dict[str, int] = {}
    for _, status in results:
        key = status.split(":", 1)[0]
        counts[key] = counts.get(key, 0) + 1
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
