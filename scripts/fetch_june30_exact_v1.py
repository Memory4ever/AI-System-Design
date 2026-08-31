#!/usr/bin/env python3
"""Fetch frozen exact-v1 arXiv HTML/PDF evidence for the 2026-06-30 packet."""

from __future__ import annotations

import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260630"
OUT = PACKET / "arxiv-v1"
IDS = PACKET / "candidate-ids-v1.txt"
UA = "AI-System-Design/1.0 exact-version research audit"


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ids = [line.strip() for line in IDS.read_text().splitlines() if line.strip()]
    html_count = pdf_count = failed = 0
    for index, aid in enumerate(ids, 1):
        html_path = OUT / f"{aid}v1.html"
        pdf_path = OUT / f"{aid}v1.pdf"
        if html_path.exists() and html_path.stat().st_size > 1000:
            html_count += 1
            print(f"[{index}/{len(ids)}] cached html {aid}", flush=True)
            continue
        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            pdf_count += 1
            print(f"[{index}/{len(ids)}] cached pdf {aid}", flush=True)
            continue
        try:
            body = fetch(f"https://arxiv.org/html/{aid}v1")
            if b"<html" not in body[:1000].lower() or len(body) < 1000:
                raise ValueError("response is not a usable HTML paper")
            html_path.write_bytes(body)
            html_count += 1
            print(f"[{index}/{len(ids)}] html {aid} {len(body)}", flush=True)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError) as html_error:
            try:
                body = fetch(f"https://export.arxiv.org/pdf/{aid}v1")
                if not body.startswith(b"%PDF"):
                    raise ValueError("response is not a PDF")
                pdf_path.write_bytes(body)
                pdf_count += 1
                print(f"[{index}/{len(ids)}] pdf {aid} {len(body)} ({html_error})", flush=True)
            except Exception as pdf_error:
                failed += 1
                print(f"[{index}/{len(ids)}] FAILED {aid}: html={html_error}; pdf={pdf_error}", flush=True)
        time.sleep(0.35)
    print({"families": len(ids), "html": html_count, "pdf": pdf_count, "failed": failed})


if __name__ == "__main__":
    main()
