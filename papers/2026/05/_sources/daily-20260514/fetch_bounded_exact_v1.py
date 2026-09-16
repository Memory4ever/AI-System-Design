#!/usr/bin/env python3
"""Fetch only the 05-14 bounded repair set from an HTML rendering of arXiv v1."""

from __future__ import annotations

import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "exact-v1-html-bounded"
OUT.mkdir(exist_ok=True)
DIRECT_OUT = HERE / "exact-v1-html-direct"
DIRECT_OUT.mkdir(exist_ok=True)

OLD = json.loads((HERE / "v3-author-recert.json").read_text())["retained_ids"]
REOPEN = """
2605.12517 2605.12529 2605.12565 2605.12574 2605.12694
2605.12765 2605.12813 2605.12869 2605.12975 2605.13043
2605.13050 2605.13105 2605.13115 2605.13130 2605.13155
2605.13162 2605.13179 2605.13213 2605.13255 2605.13277
2605.13290 2605.13329 2605.13334 2605.13352 2605.13369
2605.13429 2605.13438 2605.13448 2605.13467 2605.13486
2605.13511 2605.13534 2605.13537 2605.13625 2605.13632
2605.13652 2605.13687 2605.13695 2605.13724 2605.13757
2605.13829
""".split()


def fetch(aid: str) -> dict:
    target = OUT / f"{aid}v1.html"
    if target.exists() and target.stat().st_size > 40_000:
        return {"arxiv_id": aid, "status": "cached", "bytes": target.stat().st_size}
    urls = [
        f"https://ar5iv.labs.arxiv.org/html/{aid}",
        f"https://arxiv.org/html/{aid}v1",
    ]
    errors = []
    for url in urls:
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design evidence audit/1.0"})
            with urllib.request.urlopen(request, timeout=90) as response:
                data = response.read()
            if len(data) < 40_000:
                raise ValueError(f"short response: {len(data)}")
            target.write_bytes(data)
            return {"arxiv_id": aid, "status": "fetched", "url": url, "bytes": len(data)}
        except Exception as exc:  # exact error retained in manifest
            errors.append(f"{url}: {type(exc).__name__}: {exc}")
            time.sleep(1)
    return {"arxiv_id": aid, "status": "blocked", "errors": errors}


def fetch_direct(aid: str) -> dict:
    target = DIRECT_OUT / f"{aid}v1.html"
    if target.exists() and target.stat().st_size > 40_000:
        return {"arxiv_id": aid, "status": "cached", "bytes": target.stat().st_size}
    url = f"https://arxiv.org/html/{aid}v1"
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design evidence audit/1.0"})
        with urllib.request.urlopen(request, timeout=180) as response:
            data = response.read()
        if len(data) < 40_000:
            raise ValueError(f"short response: {len(data)}")
        target.write_bytes(data)
        return {"arxiv_id": aid, "status": "fetched", "url": url, "bytes": len(data)}
    except Exception as exc:
        return {"arxiv_id": aid, "status": "blocked", "errors": [f"{url}: {type(exc).__name__}: {exc}"]}


def main() -> None:
    ids = list(dict.fromkeys(OLD + REOPEN))
    results = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(fetch_direct, aid): aid for aid in ids}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(result["arxiv_id"], result["status"], result.get("bytes", ""), flush=True)
    results.sort(key=lambda item: item["arxiv_id"])
    manifest = {
        "schema": "bounded-exact-v1-fetch-v1",
        "report_date": "2026-05-14",
        "scope": {"existing_retained": len(OLD), "reopened_closures": len(REOPEN), "total": len(ids)},
        "items": results,
    }
    (HERE / "bounded-exact-v1-direct-fetch.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
