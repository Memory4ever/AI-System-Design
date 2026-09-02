#!/usr/bin/env python3
"""Mechanical reconciliation for the March 2026 Historical Daily rebuild.

This audit proves file/interface consistency only.  It deliberately does not
claim that title/abstract screening, source interpretation, Books disposition,
or manuscript prose is semantically correct; those require a different author
and fresh-context review under the research contracts.
"""

from __future__ import annotations

import argparse
import gzip
import json
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH = ROOT / "papers/2026/03"
RECOVERY = MONTH / "_sources/march-2026-arxiv-announcement-recovery.json.gz"


def march_dates() -> list[str]:
    current = date(2026, 3, 1)
    end = date(2026, 4, 1)
    result: list[str] = []
    while current < end:
        result.append(current.isoformat())
        current += timedelta(days=1)
    return result


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-closed",
        action="store_true",
        help="also require Completion=Complete and all three Gates to be closed",
    )
    args = parser.parse_args()

    with gzip.open(RECOVERY, "rt") as handle:
        recovery = json.load(handle)
    expected = recovery["owner_report_counts"]
    failures: list[str] = []
    summaries: list[dict] = []
    candidate_owner: dict[str, str] = {}
    review_owner: dict[str, str] = {}

    if recovery["announcement_anomaly_count"] != 0:
        failures.append("announcement recovery contains anomalies")
    if recovery["doi_creation_missing_count"] != 0:
        failures.append("announcement recovery contains DOI records without creation time")
    if recovery["scheduled_match_count"] != recovery["unique_arxiv_identifier_count"]:
        failures.append("not every recovered arXiv identifier matches an official announcement slot")

    for report_date in march_dates():
        day = report_date[-2:]
        report = MONTH / day / "README.md"
        source_dir = MONTH / "_sources" / f"daily-{report_date.replace('-', '')}"
        ledger_path = source_dir / "screening-ledger-final.json"
        packet_path = source_dir / "exact-v1-review-packet.json"
        queue_path = source_dir / "BOOKS_WRITEBACK_QUEUE.json"
        for path in (report, ledger_path, packet_path, queue_path):
            if not path.exists():
                failures.append(f"{report_date}: missing {path.relative_to(ROOT)}")
        if not all(path.exists() for path in (report, ledger_path, packet_path, queue_path)):
            continue

        ledger = load_json(ledger_path)
        packet = load_json(packet_path)
        queue = load_json(queue_path)
        identities = ledger.get("identities", [])
        candidates = [row for row in identities if row.get("screening_status") == "candidate_denominator"]
        closures = [row for row in identities if row.get("screening_status") == "pre_denominator_closure"]
        withdrawn = ledger.get("withdrawn_primary_sources", [])
        packet_items = packet.get("items", [])
        queue_items = queue.get("items", [])
        candidate_ids = {
            item.get("source_family_id") for item in candidates
        }
        review_ids = {
            item.get("source_family_id") for item in packet_items
        }
        integrate_ids = {
            item.get("source_family_id")
            for item in packet_items
            if item.get("books_disposition") == "Integrate"
        }
        queue_ids = {
            item.get("source_family_id") for item in queue_items
        }
        raw = ledger.get("registered_window_identities")
        expected_raw = expected.get(report_date, 0)

        checks = {
            "raw_matches_recovery": raw == expected_raw,
            "screened_matches_raw": ledger.get("screened_identities") == raw,
            # Withdrawn identities remain part of the raw inventory and are
            # closed before the denominator; they are therefore a subset of
            # closures rather than a third additive bucket.
            "ledger_arithmetic": raw == len(candidates) + len(closures),
            "declared_candidate_count": ledger.get("candidate_denominator") == len(candidates),
            "declared_closure_count": ledger.get("pre_denominator_closures") == len(closures),
            "weekly_dependency_zero": ledger.get("weekly_dependency_count") == 0,
            "review_packet_complete": review_ids == candidate_ids
            and len(packet_items) == len(candidates)
            and all(item.get("result") == "complete" for item in packet_items),
            "withdrawn_not_retained": not any(item.get("withdrawn") for item in packet_items),
            "withdrawn_are_closures": {
                item.get("arxiv_id") if isinstance(item, dict) else item for item in withdrawn
            }.issubset({row.get("arxiv_id") for row in closures}),
            "review_ids_unique": len({item.get("review_provenance_id") for item in packet_items})
            == len(packet_items),
            "queue_matches_integrate": queue_ids == integrate_ids,
            "queue_lifecycle_closed": queue.get("status")
            == ("applied_postwrite_verified" if queue_items else "no_writeback_required")
            and all(
                item.get("writeback_status") == "applied_postwrite_verified"
                for item in queue_items
            ),
        }
        if queue_items:
            postwrite_path = source_dir / "postwrite-semantic-audit.json"
            if not postwrite_path.exists():
                checks["postwrite_audit_closed"] = False
            else:
                postwrite = load_json(postwrite_path)
                passed_ids = {
                    item.get("source_family_id")
                    for item in postwrite.get("items", [])
                    if item.get("status") == "passed"
                    and item.get("marker_count") == 1
                }
                checks["postwrite_audit_closed"] = (
                    postwrite.get("status") == "passed"
                    and not postwrite.get("unresolved_findings")
                    and passed_ids == queue_ids
                )
        proposal_path = source_dir / "denominator-screening-proposal.json"
        if proposal_path.exists():
            proposal = load_json(proposal_path)
            checks["proposal_is_superseded"] = (
                proposal.get("artifact_status")
                == "superseded_by_screening_ledger_final"
                and proposal.get("superseded_by") == "screening-ledger-final.json"
            )
        for name, passed in checks.items():
            if not passed:
                failures.append(f"{report_date}: {name} failed")

        for family in candidate_ids:
            previous = candidate_owner.setdefault(family, report_date)
            if previous != report_date:
                failures.append(
                    f"{family}: candidate appears in both {previous} and {report_date}"
                )
        for family in review_ids:
            previous = review_owner.setdefault(family, report_date)
            if previous != report_date:
                failures.append(
                    f"{family}: review appears in both {previous} and {report_date}"
                )

        text = report.read_text()
        if "Weekly dependency=0" not in text:
            failures.append(f"{report_date}: report does not declare Weekly dependency=0")
        if args.require_closed:
            has_disputed = any(
                item.get("books_disposition") == "Disputed"
                for item in packet_items
            )
            expected_markers = (
                (
                    "| Completion Status | Conditional |",
                    "| Coverage Gate | Closed |",
                    "| Evidence Gate | Conditional Pass |",
                    "| Books Gate | Conditional Pass |",
                )
                if has_disputed
                else (
                    "| Completion Status | Complete |",
                    "| Coverage Gate | Closed |",
                    "| Evidence Gate | Passed |",
                    "| Books Gate | Passed |",
                )
            )
            for marker in expected_markers:
                if marker not in text:
                    failures.append(f"{report_date}: missing final marker {marker}")

        summaries.append(
            {
                "date": report_date,
                "raw": raw,
                "retained": len(candidates),
                "closures": len(closures),
                "withdrawn": len(withdrawn),
                "reviewed": len(packet_items),
                "books_queue": len(queue_items),
            }
        )

    print(json.dumps({"days": summaries, "failures": failures}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
