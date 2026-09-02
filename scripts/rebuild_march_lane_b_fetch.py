#!/usr/bin/env python3
"""Fetch official exact-v1 identity and body evidence for March lane B."""

from __future__ import annotations

import hashlib
import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "AI-System-Design Historical Daily V2.1 March lane B/1.0"
WITHDRAWN = ("this paper has been withdrawn", "this submission has been withdrawn", "withdrawn by the author")


def fetch(url: str, timeout: int = 90) -> bytes:
    last: Exception | None = None
    for attempt in range(4):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except Exception as error:
            last = error
            time.sleep(1.0 + attempt * 1.5)
    raise RuntimeError(f"{url}: {last}")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def one(packet: Path, aid: str) -> dict:
    body_dir = packet / "exact-v1-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    abs_path = body_dir / f"{aid}v1.abs.html"
    try:
        abs_body = abs_path.read_bytes() if abs_path.exists() else fetch(f"https://arxiv.org/abs/{aid}v1")
        if not abs_path.exists(): abs_path.write_bytes(abs_body)
    except Exception as error:
        return {"arxiv_id": aid, "withdrawn": False, "body_route": "blocked", "identity_path": "—", "body_path": "—", "error": str(error)}
    lower = abs_body.decode(errors="ignore").lower()
    phrase = next((x for x in WITHDRAWN if x in lower), None)
    if phrase:
        return {
            "arxiv_id": aid, "withdrawn": True, "withdrawal_phrase": phrase,
            "identity_url": f"https://arxiv.org/abs/{aid}v1",
            "identity_path": abs_path.relative_to(ROOT).as_posix(), "identity_sha256": sha(abs_body),
            "body_route": "not_fetched_withdrawn", "body_path": "—", "error": "—",
        }
    html_path = body_dir / f"{aid}v1.html"
    try:
        body = html_path.read_bytes() if html_path.exists() else fetch(f"https://arxiv.org/html/{aid}v1", 120)
        if not html_path.exists(): html_path.write_bytes(body)
        return {
            "arxiv_id": aid, "withdrawn": False, "withdrawal_phrase": "—",
            "identity_url": f"https://arxiv.org/abs/{aid}v1",
            "identity_path": abs_path.relative_to(ROOT).as_posix(), "identity_sha256": sha(abs_body),
            "body_route": "official_html_v1", "body_url": f"https://arxiv.org/html/{aid}v1",
            "body_path": html_path.relative_to(ROOT).as_posix(), "body_sha256": sha(body), "error": "—",
        }
    except Exception as html_error:
        pdf_path = body_dir / f"{aid}v1.pdf"
        try:
            body = pdf_path.read_bytes() if pdf_path.exists() else fetch(f"https://arxiv.org/pdf/{aid}v1", 180)
            if not pdf_path.exists(): pdf_path.write_bytes(body)
            return {
                "arxiv_id": aid, "withdrawn": False, "withdrawal_phrase": "—",
                "identity_url": f"https://arxiv.org/abs/{aid}v1",
                "identity_path": abs_path.relative_to(ROOT).as_posix(), "identity_sha256": sha(abs_body),
                "body_route": "official_pdf_v1", "body_url": f"https://arxiv.org/pdf/{aid}v1",
                "body_path": pdf_path.relative_to(ROOT).as_posix(), "body_sha256": sha(body),
                "error": f"HTML unavailable: {html_error}",
            }
        except Exception as pdf_error:
            return {
                "arxiv_id": aid, "withdrawn": False, "withdrawal_phrase": "—",
                "identity_url": f"https://arxiv.org/abs/{aid}v1",
                "identity_path": abs_path.relative_to(ROOT).as_posix(), "identity_sha256": sha(abs_body),
                "body_route": "blocked", "body_path": "—",
                "error": f"HTML: {html_error}; PDF: {pdf_error}",
            }


def main() -> None:
    for day in range(9, 17):
        packet = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
        ledger = json.loads((packet / "screening-ledger-author.json").read_text())
        ids = [row["arxiv_id"] for row in ledger["identities"] if row["screening_decision"] == "retained"]
        rows = []
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = {pool.submit(one, packet, aid): aid for aid in ids}
            for future in as_completed(futures): rows.append(future.result())
        rows.sort(key=lambda row: row["arxiv_id"])
        payload = {
            "schema": "daily-v2.1-exact-v1-access-receipt-v1", "report_date": f"2026-03-{day:02d}",
            "candidate_count": len(ids), "withdrawn_count": sum(row["withdrawn"] for row in rows),
            "accessible_count": sum(row["body_route"].startswith("official_") for row in rows),
            "blocked_count": sum(row["body_route"] == "blocked" for row in rows), "rows": rows,
        }
        (packet / "exact-v1-access-receipt.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({k: payload[k] for k in ("report_date", "candidate_count", "withdrawn_count", "accessible_count", "blocked_count")}))


if __name__ == "__main__":
    main()
