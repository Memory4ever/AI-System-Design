#!/usr/bin/env python3
"""Freeze official exact-v1 HTML provenance for the 2026-05-22 audit set."""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = json.loads((HERE / "screening-ledger-final.json").read_text())["identities"]
BY_ID = {row["arxiv_id"]: row for row in LEDGER}
AUTHOR = {row["arxiv_id"] for row in LEDGER if row["screening_status"] == "retained"}
RECOVER = set("""
2605.21856 2605.21949 2605.21996 2605.22001 2605.22057
2605.22102 2605.22138 2605.22164 2605.22177 2605.22217
2605.22219 2605.22269 2605.22283 2605.22337 2605.22343
2605.22411 2605.22493 2605.22502 2605.22505 2605.22511
2605.22526 2605.22544 2605.22564 2605.22568 2605.22608
2605.22620 2605.22718 2605.22721 2605.22769 2605.22794
2605.22800 2605.22891 2605.22894 2605.22896 2605.22905
2605.22949 2605.23019 2605.23055 2605.23058 2605.23067
2605.23078 2605.24044 2605.27428
""".split())
IDS = sorted(AUTHOR | RECOVER)
assert set(IDS) <= set(BY_ID)


def headings(body: str) -> list[str]:
    values = re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", body, flags=re.I | re.S)
    out = []
    for value in values:
        text = re.sub(r"<[^>]+>", " ", value)
        text = re.sub(r"&(?:nbsp|amp|lt|gt);", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            out.append(text)
    return out


def excerpts(body: str, pattern: str) -> list[str]:
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&(?:nbsp|amp|lt|gt|quot|#x27);", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    matches = []
    for found in re.finditer(pattern, text, flags=re.I):
        left = max(0, found.start() - 180)
        right = min(len(text), found.end() + 520)
        snippet = text[left:right].strip()
        if snippet and snippet not in matches:
            matches.append(snippet)
        if len(matches) == 3:
            break
    return matches


def fetch(aid: str) -> dict:
    url = f"https://arxiv.org/html/{aid}v1"
    proc = subprocess.run(
        ["curl", "-fsSL", "--retry", "3", "--retry-delay", "2", "--max-time", "120", url],
        capture_output=True,
    )
    body = proc.stdout
    status = "accessible" if len(body) > 20_000 and b"<html" in body[:2000].lower() else "blocked"
    decoded = body.decode("utf-8", "replace") if status == "accessible" else ""
    return {
        "arxiv_id": aid,
        "title": BY_ID[aid]["title"],
        "url": url,
        "status": status,
        "curl_exit": proc.returncode,
        "stderr": proc.stderr.decode("utf-8", "replace")[-500:],
        "retrieval_route": "official arXiv exact-v1 HTML",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sha256": hashlib.sha256(body).hexdigest() if body else None,
        "bytes": len(body),
        "headings": headings(decoded) if status == "accessible" else [],
        "method_excerpts": excerpts(decoded, r"method|architecture|framework|algorithm|system design") if decoded else [],
        "evaluation_excerpts": excerpts(decoded, r"experiment|evaluation|benchmark|results") if decoded else [],
        "limitations_excerpts": excerpts(decoded, r"limitation|failure mode|future work|discussion") if decoded else [],
    }


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    items = list(pool.map(fetch, IDS))

payload = {
    "schema": "exact-v1-provenance-v1",
    "report_date": "2026-05-22",
    "scope": "author candidates plus independently recovered false negatives",
    "items": items,
}
(HERE / "exact-v1-independent-provenance.json").write_text(
    json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps({
    "requested": len(items),
    "accessible": sum(x["status"] == "accessible" for x in items),
    "blocked": [x["arxiv_id"] for x in items if x["status"] != "accessible"],
}, ensure_ascii=False))
