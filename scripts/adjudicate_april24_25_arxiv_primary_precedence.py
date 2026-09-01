#!/usr/bin/env python3
"""Adjudicate the 2026-04-24/25 arXiv date and revision disputes.

This script is intentionally read-only with respect to Daily reports and Books.  It
uses the frozen Daily ledgers to enumerate both disputed populations and writes a
month-local adjudication receipt plus a repair manifest.

The two populations must not be conflated:

* an identifier month different from the API ``published`` month is evidence that
  the author submission was announced later; arXiv assigns the final identifier
  in the month of first announcement and does not back-date it;
* an API result whose returned identity is v2+ is only a revision-contamination
  *risk*.  Actual title/abstract drift is established only by comparison with a
  versioned v1 primary artifact.  Missing v1 metadata remains unresolved.
"""

from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "papers/2026/04/_sources"
OUTPUT = SOURCE_ROOT / "april-24-25-arxiv-primary-precedence-adjudication.json"
MANIFEST = SOURCE_ROOT / "april-24-25-arxiv-repair-manifest.json"

DAYS = {
    "2026-04-24": SOURCE_ROOT / "daily-20260424",
    "2026-04-25": SOURCE_ROOT / "daily-20260425",
}

OFFICIAL_SOURCES = {
    "availability": {
        "url": "https://info.arxiv.org/help/availability.html",
        "locators": [
            "Availability of submissions: quality-assurance checks can take one to four days or longer",
            "A note about arXiv-id assignments: final identifier is assigned when the work is announced",
            "identifier cannot be back-dated and is assigned in the month of first announcement",
        ],
        "claim": "Submission time and public announcement are distinct; identifier YYMM is the first-announcement month.",
    },
    "api_manual": {
        "url": "https://info.arxiv.org/help/api/user-manual.html",
        "locators": [
            "Entry Metadata: published is when the first version was submitted and processed",
            "Entry Metadata: updated is when the retrieved version was submitted and processed",
            "Version Information: id_list may request a specific version such as v1; otherwise latest is returned",
        ],
        "claim": "API published/updated fields are version processing timestamps; unversioned search results may carry latest-version metadata.",
    },
    "identifier": {
        "url": "https://info.arxiv.org/help/arxiv_identifier.html",
        "locators": ["new identifier scheme: YYMM.number"],
        "claim": "The identifier exposes an announcement-month namespace, but not an exact announcement day.",
    },
    "monthly_list_example": {
        "url": "https://arxiv.org/list/cs.CL/2026-06",
        "locators": ["Authors and titles for June 2026", "arXiv:2606.11211"],
        "claim": "2606.11211 appears in the official June 2026 browse listing, not an April listing.",
    },
    "versioned_abs_example": {
        "url": "https://arxiv.org/abs/2606.11211v1",
        "locators": ["Submitted on 24 Apr 2026", "Submission history [v1] Fri, 24 Apr 2026 04:46:16 UTC", "Current browse context 2026-06"],
        "claim": "The page itself distinguishes the older author submission timestamp from the later June browse/announcement namespace.",
    },
}


class MetadataParser(HTMLParser):
    """Extract title/abstract text from official abs or experimental HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._stack: list[tuple[str, set[str]]] = []
        self._capture_doc_title_depth: int | None = None
        self._capture_h1_title_depth: int | None = None
        self._capture_abs_depth: int | None = None
        self.doc_title_parts: list[str] = []
        self.h1_title_parts: list[str] = []
        self.abstract_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = set(dict(attrs).get("class", "").split())
        self._stack.append((tag, classes))
        depth = len(self._stack)
        if tag == "title" and self._capture_doc_title_depth is None:
            self._capture_doc_title_depth = depth
        if tag == "h1" and "title" in classes and self._capture_h1_title_depth is None:
            self._capture_h1_title_depth = depth
        if self._capture_abs_depth is None and (
            (tag == "blockquote" and "abstract" in classes) or "ltx_abstract" in classes
        ):
            self._capture_abs_depth = depth

    def handle_endtag(self, tag: str) -> None:
        depth = len(self._stack)
        if self._capture_doc_title_depth == depth:
            self._capture_doc_title_depth = None
        if self._capture_h1_title_depth == depth:
            self._capture_h1_title_depth = None
        if self._capture_abs_depth == depth:
            self._capture_abs_depth = None
        if self._stack:
            self._stack.pop()

    def handle_data(self, data: str) -> None:
        if self._capture_doc_title_depth is not None:
            self.doc_title_parts.append(data)
        if self._capture_h1_title_depth is not None:
            self.h1_title_parts.append(data)
        if self._capture_abs_depth is not None:
            self.abstract_parts.append(data)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def revision(identity: str) -> int:
    match = re.search(r"v(\d+)$", identity or "")
    return int(match.group(1)) if match else 1


def identifier_month(arxiv_id: str) -> str | None:
    match = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", arxiv_id)
    return f"20{match.group(1)}-{match.group(2)}" if match else None


def normalize(value: str, prefix: str | None = None) -> str:
    value = html.unescape(value)
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"\s+", " ", value).strip()
    if prefix:
        value = re.sub(rf"^{re.escape(prefix)}(?:\s*[:.]\s*|\s+)", "", value, flags=re.I)
    value = re.sub(r"^\[\d{4}\.\d{4,5}v1\]\s*", "", value)
    return value.strip()


def semantic_fingerprint(value: str) -> str:
    """Comparison fingerprint tolerant of punctuation/HTML rendering only."""

    value = normalize(value).lower()
    value = re.sub(r"\\(?:mathrm|mathbf|mathbb|text|operatorname)\s*\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"[^\w]+", "", value, flags=re.UNICODE)
    return value


def parse_primary_html(path: Path) -> tuple[str | None, str | None]:
    parser = MetadataParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    # Official abs pages expose both a document <title> and an h1 title.  The h1
    # is authoritative and avoids accidentally concatenating the same title twice.
    title_parts = parser.h1_title_parts or parser.doc_title_parts
    title = normalize(" ".join(title_parts), "Title")
    abstract = normalize(" ".join(parser.abstract_parts), "Abstract")
    return title or None, abstract or None


def build_exact_v1_index() -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}
    for path in (ROOT / "papers/2026").rglob("*"):
        if not path.is_file():
            continue
        match = re.fullmatch(r"(\d{4}\.\d{4,5})v1(?:\.abs)?\.html", path.name)
        if match:
            index.setdefault(match.group(1), []).append(path)
    for paths in index.values():
        paths.sort(key=lambda p: (not p.name.endswith(".abs.html"), len(str(p)), str(p)))
    return index


def compare_v1(identity: dict[str, Any], paths: list[Path]) -> dict[str, Any]:
    attempts = []
    for path in paths:
        title, abstract = parse_primary_html(path)
        attempts.append({
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "title_recovered": bool(title),
            "abstract_recovered": bool(abstract),
        })
        if not title or not abstract:
            continue
        current_title = normalize(identity.get("title", ""))
        current_abstract = normalize(identity.get("abstract", ""))
        title_same = semantic_fingerprint(title) == semantic_fingerprint(current_title)
        abstract_same = semantic_fingerprint(abstract) == semantic_fingerprint(current_abstract)
        return {
            "comparison_status": "v1_equivalent" if title_same and abstract_same else "later_revision_metadata_drift_confirmed",
            "title_changed": not title_same,
            "abstract_changed": not abstract_same,
            "exact_v1_title": title,
            "latest_result_title": current_title,
            "exact_v1_abstract_sha256": hashlib.sha256(abstract.encode()).hexdigest(),
            "latest_result_abstract_sha256": hashlib.sha256(current_abstract.encode()).hexdigest(),
            "exact_v1_abstract_excerpt": abstract[:280],
            "latest_result_abstract_excerpt": current_abstract[:280],
            "primary_artifact": attempts[-1],
            "attempts": attempts,
        }
    return {
        "comparison_status": "v1_metadata_unresolved",
        "title_changed": None,
        "abstract_changed": None,
        "attempts": attempts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if regenerated output differs")
    args = parser.parse_args()

    exact_index = build_exact_v1_index()
    prefix_items: list[dict[str, Any]] = []
    revision_items: list[dict[str, Any]] = []
    day_summary: dict[str, Any] = {}

    for report_date, directory in DAYS.items():
        ledger_path = directory / "screening-ledger-final.json"
        ledger = load(ledger_path)
        prefix_count = 0
        revision_count = 0
        for identity in ledger["identities"]:
            arxiv_id = identity["arxiv_id"]
            namespace_month = identifier_month(arxiv_id)
            submitted_month = identity["published_v1_utc"][:7]
            retained = identity.get("candidate_state") == "retained"
            if namespace_month and namespace_month != submitted_month:
                prefix_count += 1
                prefix_items.append({
                    "report_date": report_date,
                    "arxiv_id": arxiv_id,
                    "source_family_id": identity.get("source_family_id"),
                    "title": identity.get("title"),
                    "candidate_state": identity.get("candidate_state"),
                    "identifier_announcement_month": namespace_month,
                    "author_submission_processed_utc": identity.get("published_v1_utc"),
                    "current_stored_first_public_date": identity.get("first_public_date"),
                    "adjudication": "not_an_april_first_public_identity",
                    "reason": (
                        "Official arXiv policy assigns the final YYMM identifier in the month of first announcement and does not back-date it. "
                        "The older API/abs v1 timestamp is author submission/processing time, not public announcement time."
                    ),
                    "repair_action": "Remove from April raw/registered/candidate/review/Books paths; recover exact announcement day from the official monthly/daily listing and replay in that owner Daily.",
                    "was_retained": retained,
                    "official_abs_url": f"https://arxiv.org/abs/{arxiv_id}v1",
                    "official_monthly_list_url": f"https://arxiv.org/list/{identity.get('primary_category', 'cs')}/{namespace_month}",
                })

            if revision(identity.get("api_version_identity", "")) > 1:
                revision_count += 1
                comparison = compare_v1(identity, exact_index.get(arxiv_id, []))
                revision_items.append({
                    "report_date": report_date,
                    "arxiv_id": arxiv_id,
                    "source_family_id": identity.get("source_family_id"),
                    "api_version_identity": identity.get("api_version_identity"),
                    "candidate_state": identity.get("candidate_state"),
                    "was_retained": retained,
                    "latest_result_title": identity.get("title"),
                    **comparison,
                    "repair_action": (
                        "Replay title+abstract screening from recovered exact-v1 metadata."
                        if comparison["comparison_status"] == "later_revision_metadata_drift_confirmed"
                        else "No metadata repair required for title+abstract screening."
                        if comparison["comparison_status"] == "v1_equivalent"
                        else "Recover versioned v1 title+abstract from official abs/API/PDF before accepting historical screening."
                    ),
                })

        day_summary[report_date] = {
            "ledger": str(ledger_path.relative_to(ROOT)),
            "ledger_sha256": sha256(ledger_path),
            "registered_identities": ledger["registered_identities"],
            "identifier_month_conflicts": prefix_count,
            "v2_plus_metadata_risk": revision_count,
        }

    prefix_by_day = {
        day: sum(item["report_date"] == day for item in prefix_items) for day in DAYS
    }
    revision_status = {
        status: sum(item["comparison_status"] == status for item in revision_items)
        for status in ("later_revision_metadata_drift_confirmed", "v1_equivalent", "v1_metadata_unresolved")
    }
    retained_prefix = [item for item in prefix_items if item["was_retained"]]
    retained_revision = [item for item in revision_items if item["was_retained"]]
    prefix_keys = {(item["report_date"], item["arxiv_id"]) for item in prefix_items}
    revision_prefix_overlap = [
        item for item in revision_items
        if (item["report_date"], item["arxiv_id"]) in prefix_keys
    ]
    unresolved_revision = [
        item for item in revision_items if item["comparison_status"] == "v1_metadata_unresolved"
    ]

    receipt = {
        "schema": "arxiv-primary-precedence-adjudication/v1",
        "scope": ["2026-04-24", "2026-04-25"],
        "independence": "No Weekly artifact was used. No Daily or Books file was modified.",
        "primary_source_precedence": [
            {
                "rank": 1,
                "evidence": "official announcement/listing event and final YYMM identifier assignment",
                "use": "first-public owner month/day",
                "boundary": "YYMM proves announcement month only; exact day requires official daily listing/announcement receipt.",
            },
            {
                "rank": 2,
                "evidence": "official exact-version abs/API/HTML/PDF",
                "use": "v1 identity, title, abstract and content",
                "boundary": "abs/API published and submission-history timestamps are submission/processing time, not first-public time.",
            },
            {
                "rank": 3,
                "evidence": "unversioned search API entry",
                "use": "discovery only when returned identity is v2+",
                "boundary": "latest title/summary cannot be used as historical v1 screening evidence without a versioned comparison.",
            },
        ],
        "official_sources": OFFICIAL_SOURCES,
        "day_summary": day_summary,
        "identifier_month_adjudication": {
            "scanned": len(prefix_items),
            "by_day": prefix_by_day,
            "retained_affected": len(retained_prefix),
            "closure_affected": len(prefix_items) - len(retained_prefix),
            "decision": "All 68 are later-announcement identities, not April first-public identities. Prefix mismatch is not a harmless anomaly under a first-public contract.",
            "items": prefix_items,
        },
        "latest_revision_metadata_adjudication": {
            "scanned": len(revision_items),
            "retained_affected": len(retained_revision),
            "identifier_month_overlap": len(revision_prefix_overlap),
            "april_replay_population_after_owner_removal": len(revision_items) - len(revision_prefix_overlap),
            "comparison_counts": revision_status,
            "comparison_coverage": {
                "exact_v1_metadata_compared": revision_status["later_revision_metadata_drift_confirmed"] + revision_status["v1_equivalent"],
                "compared_retained": sum(
                    item["was_retained"] and item["comparison_status"] != "v1_metadata_unresolved"
                    for item in revision_items
                ),
                "compared_closures": sum(
                    (not item["was_retained"]) and item["comparison_status"] != "v1_metadata_unresolved"
                    for item in revision_items
                ),
                "confirmed_drift_retained": sum(
                    item["was_retained"] and item["comparison_status"] == "later_revision_metadata_drift_confirmed"
                    for item in revision_items
                ),
                "unresolved_retained": sum(
                    item["was_retained"] and item["comparison_status"] == "v1_metadata_unresolved"
                    for item in revision_items
                ),
                "unresolved_closures": sum(
                    (not item["was_retained"]) and item["comparison_status"] == "v1_metadata_unresolved"
                    for item in revision_items
                ),
            },
            "decision": (
                "The 468 v2+ rows are a risk set, not 468 proven semantic contaminations. "
                "Only versioned v1 comparison can establish drift; unresolved rows must be replayed fail-closed."
            ),
            "items": revision_items,
        },
        "gate_effect": {
            "coverage": "Open until all 68 are removed from April active paths and all 468 v2+ rows are replayed from exact-v1 title+abstract or precisely blocked.",
            "evidence": "Open for retained affected families until corrected ownership and exact-v1 screening are reconciled.",
            "books": "No Books mutation authorized by this audit. Existing traces for mis-owned families require root reconciliation after corrected owner review.",
        },
        "repair_manifest": str(MANIFEST.relative_to(ROOT)),
    }

    manifest = {
        "schema": "arxiv-april24-25-repair-manifest/v1",
        "source_receipt": str(OUTPUT.relative_to(ROOT)),
        "fail_closed": True,
        "remove_from_april_active_paths": prefix_items,
        "later_announcement_and_revision_overlap": revision_prefix_overlap,
        "replay_in_april_after_owner_removal": [
            item for item in revision_items
            if (item["report_date"], item["arxiv_id"]) not in prefix_keys
            and item["comparison_status"] != "v1_equivalent"
        ],
        "replay_from_exact_v1_metadata": [
            item for item in revision_items if item["comparison_status"] != "v1_equivalent"
        ],
        "confirmed_metadata_drift": [
            item for item in revision_items if item["comparison_status"] == "later_revision_metadata_drift_confirmed"
        ],
        "v1_metadata_recovery_requests": [
            {
                "report_date": item["report_date"],
                "arxiv_id": item["arxiv_id"],
                "source_family_id": item["source_family_id"],
                "endpoints": [
                    f"https://arxiv.org/abs/{item['arxiv_id']}v1",
                    f"https://export.arxiv.org/api/query?id_list={item['arxiv_id']}v1",
                    f"https://arxiv.org/html/{item['arxiv_id']}v1",
                    f"https://arxiv.org/pdf/{item['arxiv_id']}v1",
                ],
                "required_fields": ["v1 title", "v1 abstract", "withdrawn/removal state"],
            }
            for item in unresolved_revision
        ],
        "root_reconciliation_steps": [
            "Freeze official first-announcement list receipts for all 68 and route each family to its actual owner Daily.",
            "Remove all 68 from April raw/registered/denominator/review/selection/Books paths before recalculating counts.",
            "Recover exact-v1 title+abstract for every unresolved v2+ row and replay semantic screening; do not assume the latest title/summary is equivalent.",
            "For confirmed drift, re-run denominator admission and downstream Review/Books only if v1 remains admitted.",
            "Run an independent fresh-context audit after repair; validator success alone is insufficient.",
        ],
    }

    if len(prefix_items) != 68:
        raise SystemExit(f"expected 68 identifier-month conflicts, got {len(prefix_items)}")
    if len(revision_items) != 468:
        raise SystemExit(f"expected 468 v2+ risk rows, got {len(revision_items)}")

    rendered_receipt = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    rendered_manifest = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered_receipt:
            raise SystemExit(f"stale or missing: {OUTPUT}")
        if not MANIFEST.exists() or MANIFEST.read_text(encoding="utf-8") != rendered_manifest:
            raise SystemExit(f"stale or missing: {MANIFEST}")
        return
    OUTPUT.write_text(rendered_receipt, encoding="utf-8")
    MANIFEST.write_text(rendered_manifest, encoding="utf-8")


if __name__ == "__main__":
    main()
