#!/usr/bin/env python3
"""Fetch exact-v1 arXiv HTML for the frozen 2026-07-14 denominator."""

from __future__ import annotations

import gzip
import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260714"
REPORT_DATE = "2026-07-14"
DECISIONS = PACKET / "fresh-context-semantic-decisions-v2.1.json.gz"
OUT = PACKET / "exact-v1-html"
MANIFEST = PACKET / "exact-v1-access-manifest-v2.1.json"
USER_AGENT = "AI-System-Design research audit/2.1 (primary-source recovery)"


def fetch(url: str) -> tuple[bytes | None, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    error = "not_attempted"
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


def checkpoint(results: list[dict], expected: int, status: str) -> None:
    MANIFEST.write_text(json.dumps({
        "schema": "exact-v1-access-manifest-v2.1",
        "report_date": REPORT_DATE,
        "status": status,
        "expected": expected,
        "accessible": sum(x["status"] == "accessible" for x in results),
        "pending": sum(x["status"] != "accessible" for x in results),
        "items": results,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with gzip.open(DECISIONS, "rt", encoding="utf-8") as handle:
        decisions = json.load(handle)
    retained = [x for x in decisions["items"] if x["decision"] == "retain_in_candidate_denominator"]
    prior = {}
    if MANIFEST.exists():
        prior = {x["arxiv_id"]: x for x in json.loads(MANIFEST.read_text())["items"]}
    results = []
    for index, item in enumerate(retained, 1):
        aid = item["arxiv_id"]
        target = OUT / f"{aid}v1.html.gz"
        old = prior.get(aid)
        if target.exists() and target.stat().st_size > 0 and old and old.get("status") == "accessible":
            results.append(old)
            continue
        url = f"https://arxiv.org/html/{aid}v1"
        body, detail = fetch(url)
        if body is None:
            results.append({"arxiv_id": aid, "url": url, "status": "html_failed_pdf_fallback_pending", "detail": detail})
        else:
            with gzip.open(target, "wb") as handle:
                handle.write(body)
            results.append({
                "arxiv_id": aid, "url": url, "status": "accessible", "content_type": detail,
                "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                "snapshot": target.relative_to(ROOT).as_posix(),
            })
        print(f"[{index}/{len(retained)}] {aid} {results[-1]['status']}", flush=True)
        checkpoint(results, len(retained), "in_progress")
        time.sleep(0.45)
    checkpoint(results, len(retained), "complete" if all(x["status"] == "accessible" for x in results) else "fallback_pending")


if __name__ == "__main__":
    main()
