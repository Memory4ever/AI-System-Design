#!/usr/bin/env python3
"""Fetch exact-v1 identity and manuscript evidence for lane A candidates."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import time
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
UA = "AI-System-Design Historical Daily V2.1 March lane A/1.0"
WITHDRAWN = (
    "this paper has been withdrawn", "this submission has been withdrawn",
    "withdrawn by the author", "this paper was withdrawn",
)


def fetch(url: str, timeout: int) -> bytes:
    last = None
    for attempt in range(5):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except Exception as error:
            last = error
            time.sleep(1 + attempt * 1.5)
    raise RuntimeError(f"{url}: {last}")


def sha(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def one(packet: Path, aid: str) -> dict:
    directory = packet / "exact-v1-bodies"
    directory.mkdir(parents=True, exist_ok=True)
    abs_path = directory / f"{aid}v1.abs.html"
    try:
        abs_body = abs_path.read_bytes() if abs_path.exists() else fetch(f"https://arxiv.org/abs/{aid}v1", 90)
        if not abs_path.exists():
            abs_path.write_bytes(abs_body)
    except Exception as error:
        return {"arxiv_id": aid, "withdrawn": False, "body_route": "blocked", "error": str(error)}
    lower = abs_body.decode(errors="ignore").lower()
    phrase = next((value for value in WITHDRAWN if value in lower), None)
    identity = {
        "arxiv_id": aid,
        "withdrawn": bool(phrase),
        "withdrawal_phrase": phrase or "—",
        "identity_url": f"https://arxiv.org/abs/{aid}v1",
        "identity_path": abs_path.relative_to(ROOT).as_posix(),
        "identity_sha256": sha(abs_body),
    }
    if phrase:
        return dict(identity, body_route="not_fetched_withdrawn", body_path="—", error="—")
    html_path = directory / f"{aid}v1.html"
    try:
        body = html_path.read_bytes() if html_path.exists() else fetch(f"https://arxiv.org/html/{aid}v1", 150)
        if not html_path.exists():
            html_path.write_bytes(body)
        return dict(identity, body_route="official_html_v1", body_url=f"https://arxiv.org/html/{aid}v1", body_path=html_path.relative_to(ROOT).as_posix(), body_sha256=sha(body), error="—")
    except Exception as html_error:
        pdf_path = directory / f"{aid}v1.pdf"
        try:
            body = pdf_path.read_bytes() if pdf_path.exists() else fetch(f"https://arxiv.org/pdf/{aid}v1", 240)
            if not pdf_path.exists():
                pdf_path.write_bytes(body)
            return dict(identity, body_route="official_pdf_v1", body_url=f"https://arxiv.org/pdf/{aid}v1", body_path=pdf_path.relative_to(ROOT).as_posix(), body_sha256=sha(body), error=f"HTML unavailable: {html_error}")
        except Exception as pdf_error:
            return dict(identity, body_route="blocked", body_path="—", error=f"HTML: {html_error}; PDF: {pdf_error}")


def main() -> None:
    for day in range(1, 9):
        packet = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
        ledger = json.loads((packet / "screening-ledger-author.json").read_text())
        ids = [x["arxiv_id"] for x in ledger["identities"] if x["screening_decision"] == "retained"]
        rows = []
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = {pool.submit(one, packet, aid): aid for aid in ids}
            for future in as_completed(futures):
                rows.append(future.result())
        rows.sort(key=lambda x: x["arxiv_id"])
        payload = {
            "schema": "daily-v2.1-exact-v1-access-receipt-v1",
            "report_date": f"2026-03-{day:02d}",
            "candidate_count": len(ids),
            "withdrawn_count": sum(x["withdrawn"] for x in rows),
            "accessible_count": sum(x["body_route"].startswith("official_") for x in rows),
            "blocked_count": sum(x["body_route"] == "blocked" for x in rows),
            "rows": rows,
        }
        (packet / "exact-v1-access-receipt.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({key: payload[key] for key in ("report_date", "candidate_count", "withdrawn_count", "accessible_count", "blocked_count")}))


if __name__ == "__main__":
    main()
