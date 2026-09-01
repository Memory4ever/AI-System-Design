#!/usr/bin/env python3
"""Recover exact-v1 arXiv metadata for the 2026-04-25 revision-risk set.

This helper is deliberately date-local.  It reads the month-level adjudication
as a frozen input, excludes later-announcement identities, and saves each
official versioned abs response with a digest and parse receipt.  It does not
make denominator or Books decisions.
"""

from __future__ import annotations

import hashlib
import html
from html.parser import HTMLParser
import json
import re
import time
import unicodedata
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SOURCE_ROOT = ROOT / "papers/2026/04/_sources"
PACKET = SOURCE_ROOT / "daily-20260425"
ADJUDICATION = SOURCE_ROOT / "april-24-25-arxiv-primary-precedence-adjudication.json"
SNAPSHOT_DIR = PACKET / "exact-v1-abs"
RECEIPT = PACKET / "exact-v1-abs-recovery-receipt.json"
USER_AGENT = "AI-System-Design/2.1 historical-daily-exact-v1-recovery (contact: local-research-audit)"


class AbsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, set[str]]] = []
        self.title_depth: int | None = None
        self.abstract_depth: int | None = None
        self.history_depth: int | None = None
        self.title_parts: list[str] = []
        self.abstract_parts: list[str] = []
        self.history_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        self.stack.append((tag, classes))
        depth = len(self.stack)
        if tag == "h1" and "title" in classes and self.title_depth is None:
            self.title_depth = depth
        if tag == "blockquote" and "abstract" in classes and self.abstract_depth is None:
            self.abstract_depth = depth
        if values.get("id") == "submission-history" and self.history_depth is None:
            self.history_depth = depth

    def handle_endtag(self, tag: str) -> None:
        depth = len(self.stack)
        if self.title_depth == depth:
            self.title_depth = None
        if self.abstract_depth == depth:
            self.abstract_depth = None
        if self.history_depth == depth:
            self.history_depth = None
        if self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.title_depth is not None:
            self.title_parts.append(data)
        if self.abstract_depth is not None:
            self.abstract_parts.append(data)
        if self.history_depth is not None:
            self.history_parts.append(data)


def compact(value: str, prefix: str | None = None) -> str:
    value = unicodedata.normalize("NFKC", html.unescape(value))
    value = re.sub(r"\s+", " ", value).strip()
    if prefix:
        value = re.sub(rf"^{re.escape(prefix)}(?:\s*:\s*|\s+)", "", value, flags=re.I)
    return value.strip()


def parse_abs(raw: bytes) -> dict[str, object]:
    text = raw.decode("utf-8", errors="ignore")
    parser = AbsParser()
    parser.feed(text)
    title = compact(" ".join(parser.title_parts), "Title")
    abstract = compact(" ".join(parser.abstract_parts), "Abstract")
    history = compact(" ".join(parser.history_parts))
    lowered = text.lower()
    withdrawal_markers = [
        marker
        for marker in (
            "this paper has been withdrawn",
            "submission has been withdrawn",
            "withdrawn by the authors",
            "removed from arxiv",
        )
        if marker in lowered
    ]
    return {
        "title": title,
        "abstract": abstract,
        "submission_history": history,
        "withdrawn": bool(withdrawal_markers),
        "withdrawal_markers": withdrawal_markers,
    }


def fetch(url: str) -> tuple[bytes | None, list[dict[str, object]]]:
    attempts: list[dict[str, object]] = []
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                raw = response.read()
                attempts.append({"attempt": attempt, "status": response.status, "bytes": len(raw)})
                return raw, attempts
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            attempts.append({"attempt": attempt, "status": getattr(exc, "code", None), "error": repr(exc)})
            if attempt < 5:
                time.sleep(2 ** (attempt - 1))
    return None, attempts


def main() -> None:
    adjudication = json.loads(ADJUDICATION.read_text(encoding="utf-8"))
    removed = {
        item["arxiv_id"]
        for item in adjudication["identifier_month_adjudication"]["items"]
        if item["report_date"] == "2026-04-25"
    }
    risks = [
        item
        for item in adjudication["latest_revision_metadata_adjudication"]["items"]
        if item["report_date"] == "2026-04-25" and item["arxiv_id"] not in removed
    ]
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    prior: dict[str, dict[str, object]] = {}
    if RECEIPT.exists():
        saved = json.loads(RECEIPT.read_text(encoding="utf-8"))
        prior = {row["arxiv_id"]: row for row in saved.get("rows", [])}

    rows: list[dict[str, object]] = []
    for index, item in enumerate(risks, start=1):
        identifier = item["arxiv_id"]
        url = f"https://arxiv.org/abs/{identifier}v1"
        target = SNAPSHOT_DIR / f"{identifier}v1.abs.html"
        if target.exists():
            raw = target.read_bytes()
            attempts = prior.get(identifier, {}).get("attempts", [{"attempt": 0, "status": "reused_frozen_snapshot"}])
        else:
            raw, attempts = fetch(url)
            if raw is not None:
                target.write_bytes(raw)
            time.sleep(3.1)
        if raw is None:
            rows.append({
                "arxiv_id": identifier,
                "source_family_id": item["source_family_id"],
                "url": url,
                "status": "blocked_after_bounded_retries",
                "attempts": attempts,
            })
            continue
        parsed = parse_abs(raw)
        parse_complete = bool(parsed["title"] and parsed["abstract"])
        rows.append({
            "arxiv_id": identifier,
            "source_family_id": item["source_family_id"],
            "url": url,
            "path": str(target.relative_to(ROOT)),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "status": "accessible_exact_v1_metadata" if parse_complete else "blocked_parse_incomplete",
            "title": parsed["title"],
            "abstract": parsed["abstract"],
            "submission_history": parsed["submission_history"],
            "withdrawn": parsed["withdrawn"],
            "withdrawal_markers": parsed["withdrawal_markers"],
            "attempts": attempts,
        })
        if index % 20 == 0:
            print(f"exact-v1 abs {index}/{len(risks)}", flush=True)

    receipt = {
        "schema": "arxiv-exact-v1-abs-recovery-receipt-v1",
        "report_date": "2026-04-25",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_adjudication": str(ADJUDICATION.relative_to(ROOT)),
        "later_announcement_excluded": len(removed),
        "revision_risk_after_owner_removal": len(risks),
        "accessible": sum(row["status"] == "accessible_exact_v1_metadata" for row in rows),
        "blocked": sum(row["status"] != "accessible_exact_v1_metadata" for row in rows),
        "withdrawn": sum(bool(row.get("withdrawn")) for row in rows),
        "rate_limit_seconds": 3.1,
        "retry_policy": "five attempts with exponential backoff 1,2,4,8 seconds",
        "rows": rows,
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in ("revision_risk_after_owner_removal", "accessible", "blocked", "withdrawn")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
