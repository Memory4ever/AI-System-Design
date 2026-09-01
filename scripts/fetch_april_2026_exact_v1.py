#!/usr/bin/env python3
"""Fetch official arXiv identity pages and exact-v1 bodies for April Daily candidates."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UA = "AI-System-Design Daily V2.1 evidence review/1.0"
WITHDRAWN_PHRASES = (
    "this paper has been withdrawn",
    "the paper has been withdrawn",
    "this submission has been withdrawn",
    "withdrawn by the author",
)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dates", nargs="+", help="report dates as YYYY-MM-DD")
    return parser.parse_args()


def fetch(url: str, timeout: int = 90) -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    last: Exception | None = None
    for attempt in range(1, 5):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), response.headers.get("Content-Type", "")
        except Exception as error:
            last = error
            if attempt < 4:
                time.sleep(attempt * 1.5)
    assert last is not None
    raise last


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_screening_ledger(packet: Path) -> tuple[dict, Path]:
    """Load the independently frozen ledger, with legacy fallback."""
    final_path = packet / "screening-ledger-final.json"
    legacy_path = packet / "screening-ledger.json"
    path = final_path if final_path.exists() else legacy_path
    return json.loads(path.read_text(encoding="utf-8")), path


def retained_arxiv_ids(ledger: dict) -> list[str]:
    rows = ledger.get("identities", ledger.get("rows", []))
    return sorted({
        row["arxiv_id"]
        for row in rows
        if row.get("screening_decision") == "retained"
        or row.get("candidate_state") == "retained"
        or row.get("screening_status") == "candidate_denominator"
    })


def challenged_arxiv_ids(packet: Path) -> list[str]:
    """Return explicit false-negative challenges that still require exact-v1 adjudication."""
    ids = set()
    paths = (
        packet / "independent-high-risk-closure-challenges.json",
        packet / "independent-denominator-adjudication.json",
    )
    pending_states = {
        "false_negative_challenge_pending_exact_v1",
        "false_negative_retained_pending_exact_v1",
    }
    for path in paths:
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        ids.update(
            row["arxiv_id"]
            for row in payload.get("items", [])
            if row.get("status") in pending_states and row.get("arxiv_id")
        )
    return sorted(ids)


def fetch_one(packet: Path, aid: str) -> dict:
    body_dir = packet / "exact-v1-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    abs_path = body_dir / f"{aid}v1.abs.html"
    if abs_path.exists():
        abs_body = abs_path.read_bytes()
    else:
        abs_body, _ = fetch(f"https://arxiv.org/abs/{aid}v1")
        abs_path.write_bytes(abs_body)
    lower = abs_body.decode("utf-8", errors="ignore").lower()
    withdrawal_phrase = next((phrase for phrase in WITHDRAWN_PHRASES if phrase in lower), None)
    row = {
        "arxiv_id": aid,
        "identity_url": f"https://arxiv.org/abs/{aid}v1",
        "identity_path": abs_path.relative_to(ROOT).as_posix(),
        "identity_sha256": digest(abs_body),
        "withdrawn": bool(withdrawal_phrase),
        "withdrawal_phrase": withdrawal_phrase or "—",
        "body_route": "not_fetched_withdrawn" if withdrawal_phrase else "pending",
        "body_url": "—",
        "body_path": "—",
        "body_sha256": "—",
        "error": "—",
    }
    if withdrawal_phrase:
        return row

    html_path = body_dir / f"{aid}v1.html"
    pdf_path = body_dir / f"{aid}v1.pdf"
    try:
        if html_path.exists():
            body = html_path.read_bytes()
        else:
            body, content_type = fetch(f"https://arxiv.org/html/{aid}v1")
            if "html" not in content_type.lower() and not body.lstrip().startswith(b"<"):
                raise ValueError(f"unexpected HTML content type: {content_type}")
            html_path.write_bytes(body)
        row.update({
            "body_route": "official_html_v1",
            "body_url": f"https://arxiv.org/html/{aid}v1",
            "body_path": html_path.relative_to(ROOT).as_posix(),
            "body_sha256": digest(body),
        })
        return row
    except Exception as html_error:
        try:
            if pdf_path.exists():
                body = pdf_path.read_bytes()
            else:
                body, _ = fetch(f"https://arxiv.org/pdf/{aid}v1", timeout=120)
                if not body.startswith(b"%PDF"):
                    raise ValueError("official PDF endpoint did not return a PDF")
                pdf_path.write_bytes(body)
            row.update({
                "body_route": "official_pdf_v1",
                "body_url": f"https://arxiv.org/pdf/{aid}v1",
                "body_path": pdf_path.relative_to(ROOT).as_posix(),
                "body_sha256": digest(body),
                "error": f"HTML unavailable: {type(html_error).__name__}: {html_error}",
            })
            return row
        except Exception as pdf_error:
            row.update({
                "body_route": "blocked",
                "error": (
                    f"HTML {type(html_error).__name__}: {html_error}; "
                    f"PDF {type(pdf_error).__name__}: {pdf_error}"
                ),
            })
            return row


def process(raw_date: str) -> None:
    compact = raw_date.replace("-", "")
    packet = ROOT / f"papers/2026/04/_sources/daily-{compact}"
    ledger, ledger_path = load_screening_ledger(packet)
    retained_ids = retained_arxiv_ids(ledger)
    challenge_ids = challenged_arxiv_ids(packet)
    ids = sorted(set(retained_ids) | set(challenge_ids))
    rows: list[dict] = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_id = {executor.submit(fetch_one, packet, aid): aid for aid in ids}
        for future in as_completed(future_to_id):
            aid = future_to_id[future]
            try:
                rows.append(future.result())
            except Exception as error:
                rows.append({
                    "arxiv_id": aid,
                    "identity_url": f"https://arxiv.org/abs/{aid}v1",
                    "identity_path": "—",
                    "identity_sha256": "—",
                    "withdrawn": False,
                    "withdrawal_phrase": "—",
                    "body_route": "blocked",
                    "body_url": "—",
                    "body_path": "—",
                    "body_sha256": "—",
                    "error": f"identity/body fetch failed: {type(error).__name__}: {error}",
                })
    rows.sort(key=lambda row: row["arxiv_id"])
    payload = {
        "schema": "daily-v2.1-exact-v1-access-receipt-v1",
        "report_date": raw_date,
        "screening_ledger": ledger_path.relative_to(ROOT).as_posix(),
        "candidate_count": len(retained_ids),
        "false_negative_challenge_count": len(challenge_ids),
        "fetch_identity_count": len(ids),
        "withdrawn_count": sum(row["withdrawn"] for row in rows),
        "accessible_count": sum(row["body_route"].startswith("official_") for row in rows),
        "blocked_count": sum(row["body_route"] == "blocked" for row in rows),
        "rows": rows,
    }
    (packet / "exact-v1-access-receipt.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({key: payload[key] for key in (
        "report_date", "candidate_count", "false_negative_challenge_count",
        "fetch_identity_count", "withdrawn_count", "accessible_count", "blocked_count"
    )}))


def main() -> None:
    for raw_date in arguments().dates:
        process(raw_date)


if __name__ == "__main__":
    main()
