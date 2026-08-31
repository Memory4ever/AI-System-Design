#!/usr/bin/env python3
"""Fetch and index official exact-v1 HTML for 2026-05-21 audit candidates."""
from __future__ import annotations

import concurrent.futures
import hashlib
import html
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

IDS = """
2605.20696 2605.20749 2605.20752 2605.20756 2605.20774 2605.20798
2605.20833 2605.20866 2605.20876 2605.20948 2605.21061 2605.21103
2605.21127 2605.21177 2605.21266 2605.21273 2605.21347 2605.21384
2605.21467 2605.21468 2605.21482 2605.21486 2605.21606 2605.21642
2605.21648 2605.21649 2605.21768 2605.21801 2605.21803 2605.21810
2605.22882 2605.22884 2605.26128 2605.26132
""".split()


def clean(value: str) -> str:
    value = re.sub(r"<math.*?</math>", " [formula] ", value, flags=re.S | re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def fetch(aid: str) -> dict:
    url = f"https://arxiv.org/html/{aid}v1"
    proc = subprocess.run(
        ["curl", "-fsSL", "--max-time", "45", url],
        check=False,
        capture_output=True,
    )
    body = proc.stdout
    if proc.returncode or len(body) < 2000:
        return {
            "arxiv_id": aid,
            "url": url,
            "status": "blocked",
            "curl_exit": proc.returncode,
            "stderr": proc.stderr.decode("utf-8", "replace")[-500:],
        }
    text = body.decode("utf-8", "replace")
    title_match = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
    headings = []
    for level, raw in re.findall(r"<h([1-4])[^>]*>(.*?)</h\1>", text, re.S | re.I):
        heading = clean(raw)
        if heading and heading not in headings:
            headings.append(heading)
    paragraphs = [clean(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", text, re.S | re.I)]
    paragraphs = [x for x in paragraphs if len(x) >= 80]
    method = [x for x in paragraphs if re.search(r"\b(we propose|we introduce|our method|our framework|our system|our approach|architecture|algorithm)\b", x, re.I)][:4]
    evaluation = [x for x in paragraphs if re.search(r"\b(experiment|evaluate|benchmark|dataset|ablation|result)\b", x, re.I)][:4]
    limitations = [x for x in paragraphs if re.search(r"\b(limit|scope|future work|does not|cannot|restricted|only evaluate|threat to validity)\b", x, re.I)][-4:]
    return {
        "arxiv_id": aid,
        "url": url,
        "status": "accessible",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sha256": hashlib.sha256(body).hexdigest(),
        "bytes": len(body),
        "title": clean(title_match.group(1)) if title_match else "",
        "headings": headings,
        "method_excerpts": method,
        "evaluation_excerpts": evaluation,
        "limitations_excerpts": limitations,
    }


with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    items = list(pool.map(fetch, IDS))

payload = {
    "schema": "exact-v1-provenance-and-reading-index-v1",
    "report_date": "2026-05-21",
    "items": items,
}
(HERE / "exact-v1-recovered-provenance.json").write_text(
    json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps({"accessible": sum(x["status"] == "accessible" for x in items), "blocked": [x["arxiv_id"] for x in items if x["status"] != "accessible"]}))
