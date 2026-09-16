#!/usr/bin/env python3
"""Extract per-identity arXiv version/comment evidence for the bounded May 11 repair.

The input pages are the 191 official arXiv abstract pages fetched for this
repair.  The script does not discover or screen any additional identity.
"""

from __future__ import annotations

import html
import json
from pathlib import Path
import re


SOURCE_DIR = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[5]
LEDGER = SOURCE_DIR / "V3_SCREENING_LEDGER_20260914.json"
OWNER_RECEIPT = (
    ROOT
    / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260511/arxiv-owner-receipt.json"
)
PAGE_DIR = Path("/private/tmp/arxiv-20260511-recovery-pages")
OUTPUT = SOURCE_DIR / "V3_ORDINARY_RECOVERY_OFFICIAL_BASIS_20260915.json"


def clean_markup(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def extract_page(arxiv_id: str) -> dict[str, object]:
    page_path = PAGE_DIR / f"{arxiv_id}.html"
    body = page_path.read_text(encoding="utf-8")
    if f'arXiv:{arxiv_id}' not in body:
        raise ValueError(f"official page identity mismatch: {arxiv_id}")

    current_match = re.search(
        rf'<meta property="og:url" content="https://arxiv\.org/abs/{re.escape(arxiv_id)}v(\d+)"',
        body,
    )
    if not current_match:
        raise ValueError(f"current version not found: {arxiv_id}")

    comment_match = re.search(
        r'<td class="tablecell comments[^>]*>(.*?)</td>', body, re.DOTALL
    )
    comments = clean_markup(comment_match.group(1)) if comment_match else "Not Disclosed"

    history_match = re.search(
        r'<div class="submission-history">(.*?)</div>', body, re.DOTALL
    )
    if not history_match:
        raise ValueError(f"submission history not found: {arxiv_id}")
    history = history_match.group(1)
    versions = re.findall(r'\[v(\d+)\]', history)
    timestamps = re.findall(
        r'((?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+\d{1,2}\s+[A-Z][a-z]{2}\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+UTC)',
        clean_markup(history),
    )
    if len(versions) != len(timestamps):
        raise ValueError(
            f"version/timestamp mismatch: {arxiv_id} {versions=} {timestamps=}"
        )

    return {
        "official_abs_url": f"https://arxiv.org/abs/{arxiv_id}",
        "exact_review_version": f"arXiv:{arxiv_id}v1",
        "exact_review_url": f"https://arxiv.org/html/{arxiv_id}v1",
        "current_version_at_check": f"v{current_match.group(1)}",
        "submission_history": [
            {"version": f"v{version}", "submitted_at_utc": timestamp}
            for version, timestamp in zip(versions, timestamps)
        ],
        "official_comments_at_check": comments,
    }


def main() -> None:
    ledger = json.loads(LEDGER.read_text())
    receipt = json.loads(OWNER_RECEIPT.read_text())
    receipt_by_id = {item["arxiv_id"]: item for item in receipt["identities"]}
    recovery = [
        item
        for item in ledger["entries"]
        if item["receipt_route"] == "datacite_initial_created_owner_proxy"
    ]
    if len(recovery) != 191:
        raise ValueError(f"expected 191 bounded recovery identities, got {len(recovery)}")

    items = []
    for item in recovery:
        arxiv_id = item["arxiv_id"]
        owner = receipt_by_id[arxiv_id]
        page = extract_page(arxiv_id)
        page.update(
            {
                "arxiv_id": arxiv_id,
                "source_family_id": item["source_family_id"],
                "owner_route": owner["owner_receipt_route"],
                "owner_event_basis": {
                    "datacite_initial_created_utc": owner[
                        "datacite_initial_created_timestamp"
                    ],
                    "arxiv_v1_updated_metadata_utc": owner[
                        "v1_updated_timestamp_revision_metadata_only"
                    ],
                    "arxiv_v1_submission_provenance_utc": owner[
                        "v1_submission_timestamp_provenance_only"
                    ],
                    "current_datacite_updated_revision_only_utc": owner[
                        "datacite_current_updated_timestamp_revision_only"
                    ],
                    "current_oai_datestamps_revision_only": owner[
                        "oai_current_datestamps"
                    ],
                    "owner_day": "2026-05-11",
                    "interpretation": (
                        "DataCite initial-created is the frozen owner-day proxy; "
                        "submission timestamp is provenance only; later current-version "
                        "and OAI dates are not reclassified as this window's revision event."
                    ),
                },
                "checked_at": "2026-09-15T22:40:00+08:00",
            }
        )
        items.append(page)

    OUTPUT.write_text(
        json.dumps(
            {
                "schema": "ai-system-design.v3-ordinary-recovery-official-basis",
                "report_date": "2026-05-11",
                "scope": "exactly the 191 frozen datacite owner-proxy recovery identities",
                "official_page_source": "https://arxiv.org/abs/<arxiv_id>",
                "checked_at": "2026-09-15T22:40:00+08:00",
                "items": items,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )


if __name__ == "__main__":
    main()
