#!/usr/bin/env python3
"""Fetch exact-v1 arXiv HTML for the frozen 2026-07-13 denominator."""

from __future__ import annotations

import gzip
import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260713"
DECISIONS = PACKET / "fresh-context-semantic-decisions-v2.1.json.gz"
OUT = PACKET / "exact-v1-html"
MANIFEST = PACKET / "exact-v1-access-manifest-v2.1.json"
USER_AGENT = "AI-System-Design research audit/2.1 (primary-source recovery)"


def fetch(url: str) -> tuple[bytes | None, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                body = response.read()
                content_type = response.headers.get("Content-Type", "")
                if response.status == 200 and len(body) > 1000:
                    return body, content_type
                error = f"http_{response.status}_bytes_{len(body)}"
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            error = f"{type(exc).__name__}:{exc}"
        time.sleep(2 ** attempt)
    return None, error


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with gzip.open(DECISIONS, "rt", encoding="utf-8") as handle:
        decisions = json.load(handle)
    retained = [
        item for item in decisions["items"]
        if item["decision"] == "retain_in_candidate_denominator"
    ]
    prior = {}
    if MANIFEST.exists():
        prior = {item["arxiv_id"]: item for item in json.loads(MANIFEST.read_text())["items"]}

    results = []
    for index, item in enumerate(retained, 1):
        arxiv_id = item["arxiv_id"]
        target = OUT / f"{arxiv_id}v1.html.gz"
        old = prior.get(arxiv_id)
        if target.exists() and target.stat().st_size > 0 and old and old.get("status") == "accessible":
            results.append(old)
            continue
        url = f"https://arxiv.org/html/{arxiv_id}v1"
        body, detail = fetch(url)
        if body is None:
            results.append({
                "arxiv_id": arxiv_id,
                "url": url,
                "status": "html_failed_pdf_fallback_pending",
                "detail": detail,
            })
        else:
            with gzip.open(target, "wb") as handle:
                handle.write(body)
            results.append({
                "arxiv_id": arxiv_id,
                "url": url,
                "status": "accessible",
                "content_type": detail,
                "bytes": len(body),
                "sha256": hashlib.sha256(body).hexdigest(),
                "snapshot": target.relative_to(ROOT).as_posix(),
            })
        print(f"[{index}/{len(retained)}] {arxiv_id} {results[-1]['status']}", flush=True)
        time.sleep(0.8)

        # Preserve a restartable checkpoint after each exact source.
        MANIFEST.write_text(json.dumps({
            "schema": "exact-v1-access-manifest-v2.1",
            "report_date": "2026-07-13",
            "status": "in_progress",
            "expected": len(retained),
            "accessible": sum(result["status"] == "accessible" for result in results),
            "pending": sum(result["status"] != "accessible" for result in results),
            "items": results,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    status = "complete" if all(result["status"] == "accessible" for result in results) else "fallback_pending"
    MANIFEST.write_text(json.dumps({
        "schema": "exact-v1-access-manifest-v2.1",
        "report_date": "2026-07-13",
        "status": status,
        "expected": len(retained),
        "accessible": sum(result["status"] == "accessible" for result in results),
        "pending": sum(result["status"] != "accessible" for result in results),
        "items": results,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
