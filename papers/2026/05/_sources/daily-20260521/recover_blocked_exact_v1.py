#!/usr/bin/env python3
"""Retry official exact-v1 HTML, then official PDF, for blocked audit items."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATH = HERE / "exact-v1-recovered-provenance.json"
payload = json.loads(PATH.read_text())

for item in payload["items"]:
    if item["status"] == "accessible":
        continue
    aid = item["arxiv_id"]
    html_url = f"https://arxiv.org/html/{aid}v1"
    proc = subprocess.run(["curl", "-fsSL", "--retry", "3", "--retry-delay", "2", "--max-time", "90", html_url], capture_output=True)
    if proc.returncode == 0 and len(proc.stdout) > 2000:
        body = proc.stdout
        text = body.decode("utf-8", "replace")
        headings = []
        for level, raw in re.findall(r"<h([1-4])[^>]*>(.*?)</h\1>", text, re.S | re.I):
            heading = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw)).strip()
            if heading and heading not in headings:
                headings.append(heading)
        item.update(status="accessible", retrieval_route="official arXiv exact-v1 HTML", url=html_url,
                    retrieved_at=datetime.now(timezone.utc).isoformat(), sha256=hashlib.sha256(body).hexdigest(),
                    bytes=len(body), headings=headings, method_excerpts=[], evaluation_excerpts=[], limitations_excerpts=[])
        continue

    pdf_url = f"https://arxiv.org/pdf/{aid}v1"
    proc = subprocess.run(["curl", "-fsSL", "--retry", "3", "--retry-delay", "2", "--max-time", "120", pdf_url], capture_output=True)
    if proc.returncode or not proc.stdout.startswith(b"%PDF"):
        item.update(status="blocked", html_url=html_url, pdf_url=pdf_url,
                    stderr=proc.stderr.decode("utf-8", "replace")[-1000:])
        continue
    pdf = proc.stdout
    conv = subprocess.run(["pdftotext", "-layout", "-", "-"], input=pdf, capture_output=True)
    text = conv.stdout.decode("utf-8", "replace") if conv.returncode == 0 else ""
    headings = []
    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if re.match(r"^(\d+(\.\d+)*\.?\s+|APPENDIX\s+|LIMITATIONS?$|CONCLUSION$|EXPERIMENTS?$)", line, re.I) and len(line) < 160:
            if line not in headings:
                headings.append(line)
    item.update(status="accessible", retrieval_route="official arXiv exact-v1 PDF", url=pdf_url,
                retrieved_at=datetime.now(timezone.utc).isoformat(), sha256=hashlib.sha256(pdf).hexdigest(),
                bytes=len(pdf), headings=headings[:80], text_excerpt=text[:5000],
                method_excerpts=[], evaluation_excerpts=[], limitations_excerpts=[])

PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"accessible": sum(x["status"] == "accessible" for x in payload["items"]),
                  "blocked": [x["arxiv_id"] for x in payload["items"] if x["status"] != "accessible"]}))
