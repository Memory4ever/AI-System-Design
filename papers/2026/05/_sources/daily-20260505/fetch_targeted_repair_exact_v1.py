#!/usr/bin/env python3
"""Fetch exact-v1 HTML for the bounded 2026-05-05 repair set only."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "arxiv-v1-html"
OUT.mkdir(exist_ok=True)

TARGETS = (
    "2605.00836",
    "2605.00939",
    "2605.01047",
    "2605.01111",
    "2605.01148",
    "2605.01167",
    "2605.01172",
    "2605.01199",
    "2605.01327",
    "2605.01347",
    "2605.01373",
    "2605.01374",
    "2605.01429",
    "2605.01506",
    "2605.01609",
    "2605.01642",
    "2605.01653",
    "2605.01710",
    "2605.01732",
    "2605.01733",
    "2605.01749",
    "2605.01771",
    "2605.01782",
    "2605.01789",
    "2605.01844",
    "2605.01899",
    "2605.01929",
    "2605.02144",
    "2605.02152",
    "2605.02196",
    "2605.02269",
    "2605.02398",
    "2605.02442",
    "2605.02469",
    "2605.02647",
    "2605.02765",
)


def fetch(arxiv_id: str) -> tuple[str, str]:
    path = OUT / f"{arxiv_id}v1.html"
    if path.exists() and path.stat().st_size > 1000:
        return arxiv_id, f"cached:{path.stat().st_size}"
    request = urllib.request.Request(
        f"https://arxiv.org/html/{arxiv_id}v1",
        headers={"User-Agent": "AI-System-Design research audit (non-commercial)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            body = response.read()
        path.write_bytes(body)
        return arxiv_id, f"ok:{len(body)}"
    except (urllib.error.URLError, TimeoutError) as error:
        return arxiv_id, f"blocked:{type(error).__name__}:{error}"


def main() -> None:
    results: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = [pool.submit(fetch, arxiv_id) for arxiv_id in TARGETS]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort()
    output = {"requested": len(TARGETS), "results": results}
    (HERE / "targeted-repair-exact-v1-fetch-results.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
