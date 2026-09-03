#!/usr/bin/env python3
"""Materialize per-Daily arXiv first-public owner reconciliation receipts."""

from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent
OWNER_TSV = AUDIT / "owner-recovery/owner-reconciliation.tsv"
WITHDRAWN = {"2606.24369"}
AMBIGUOUS = "identifier_month_conflict_ambiguous"
SHANGHAI = ZoneInfo("Asia/Shanghai")


def update_report_coverage(report_date: str, counts: Counter, packet: Path) -> None:
    month, day = report_date[5:7], report_date[8:10]
    report = ROOT / f"papers/2026/{month}/{day}/README.md"
    text = report.read_text(encoding="utf-8")
    lines = text.splitlines()
    receipt_ref = (
        Path(os.path.relpath(packet, report.parent)).as_posix()
        + "/official-arxiv-first-public-owner-receipt-v1.json"
    )
    gap = (
        f"GAP-ARXIV-EXACT-OWNER-{report_date.replace('-', '')}"
        if counts[AMBIGUOUS]
        else f"GAP-ARXIV-CANONICAL-REDISTRIBUTION-{report_date.replace('-', '')}"
    )
    for index, line in enumerate(lines):
        if not line.startswith("| SRC-ARXIV |"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 12:
            continue
        cells[4] = "arXiv official availability schedule + exact-v1 Atom + DataCite DOI created"
        cells[5] = "incomplete"
        # ``incomplete`` must keep at least one machine-visible closure field open.
        # Batch provenance belongs in Closure Evidence; the cursor stays Pending
        # until the canonical candidate redistribution has been replayed.
        cells[8] = "—"
        cells[9] = "2026-09-03T12:10:00+08:00"
        cells[10] = (
            f"{receipt_ref}; coverage:SRC-ARXIV:{report_date.replace('-', '')}; "
            "unclosed: canonical candidate redistribution pending"
        )
        cells[11] = gap
        lines[index] = "| " + " | ".join(cells) + " |"
        break
    text = "\n".join(lines) + "\n"
    text = re.sub(
        r"arXiv 归属仍缺官方逐日 announcement/listing receipt。",
        "arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。",
        text,
    )
    text = text.replace(
        "latest-contract arXiv first-public owner receipt incomplete",
        "official first-public receipt restored; candidate/denominator canonical redistribution pending",
    )
    report.write_text(text, encoding="utf-8")


def main() -> None:
    rows = [
        row for row in csv.DictReader(OWNER_TSV.open(encoding="utf-8"), delimiter="\t")
        if row["arxiv_id"] not in WITHDRAWN
    ]
    by_report: dict[str, list[dict]] = {}
    for row in rows:
        # The receipt is an owner-Daily artifact.  Grouping by the report that
        # happened to contain the candidate before reconciliation recreates the
        # very spillback error this pass is meant to remove.  Resolved families
        # therefore follow their canonical owner; only genuinely ambiguous
        # families remain attached to their current report until exact mailing
        # evidence resolves the conflict.
        owner_report_date = (
            row["report_date"]
            if row["reconciliation"] == AMBIGUOUS
            else row["resolved_owner_report_date"]
        )
        by_report.setdefault(owner_report_date, []).append(row)

    for report_date, items in sorted(by_report.items()):
        month = report_date[5:7]
        compact = report_date.replace("-", "")
        packet = ROOT / f"papers/2026/{month}/_sources/daily-{compact}"
        packet.mkdir(parents=True, exist_ok=True)
        normalized = []
        for row in items:
            normalized.append(
                {
                    "source_family_id": row["source_family_id"],
                    "primary_identifier": row["primary_identifier"],
                    "arxiv_v1_submitted_utc": row["published"],
                    "normal_schedule_owner_date": row["schedule_owner_report_date"],
                    "datacite_doi": row["datacite_doi"],
                    "datacite_created_utc": row["datacite_created"],
                    "resolved_owner_report_date": row["resolved_owner_report_date"],
                    "schedule_matches_datacite_owner": row["schedule_matches_datacite_owner"],
                    "reconciliation": row["reconciliation"],
                    "title": row["title"],
                }
            )
        counts = Counter(item["reconciliation"] for item in normalized)
        payload = {
            "schema": "official-arxiv-first-public-owner-receipt-v1",
            "report_date": report_date,
            "generated_at": datetime.now(SHANGHAI).isoformat(),
            "status": "blocked" if counts[AMBIGUOUS] else "resolved_pending_report_rebuild",
            "candidate_identity_count": len(normalized),
            "reconciliation_counts": dict(sorted(counts.items())),
            "evidence_contract": {
                "arxiv_availability": "../latest-contract-reaudit-20260903/owner-recovery/arxiv-availability.html.gz",
                "arxiv_atom_batches": "../latest-contract-reaudit-20260903/owner-recovery/candidate-atom-*.xml.gz",
                "datacite_exact_id_batches": "../latest-contract-reaudit-20260903/owner-recovery/candidate-datacite-*.json.gz",
                "canonical_ledger": "../latest-contract-reaudit-20260903/owner-recovery/owner-reconciliation.tsv",
                "date_semantics": (
                    "arXiv v1 submission history + normal 20:00 Eastern availability schedule; "
                    "DataCite DOI immutable created timestamp independently identifies the actual "
                    "registration/announcement cycle. Schedule divergence is recorded as QA delay; "
                    "identifier-month conflict remains ambiguous."
                ),
            },
            "items": normalized,
        }
        (packet / "official-arxiv-first-public-owner-receipt-v1.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        update_report_coverage(report_date, counts, packet)

    ambiguous = [row for row in rows if row["reconciliation"] == AMBIGUOUS]
    with (AUDIT / "materials-request.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "Request ID", "Priority", "Source ID", "Source Family ID", "Current Report",
                "Known Endpoints", "Missing Material", "Why Existing Evidence Is Insufficient",
                "Acceptable Substitute", "Suggested File Name", "Required Review Scope",
            ]
        )
        for row in ambiguous:
            writer.writerow(
                [
                    f"MR-ARXIV-OWNER-{row['arxiv_id']}", "P3 Revision", "SRC-ARXIV",
                    row["source_family_id"], row["report_date"],
                    (
                        f"https://arxiv.org/abs/{row['arxiv_id']}v1 ; "
                        f"https://api.datacite.org/dois/10.48550/arxiv.{row['arxiv_id']}"
                    ),
                    "事件时官方 announcement/listing 邮件或页面，能证明首次公开所在 mailing batch",
                    (
                        "arXiv identifier month and DataCite DOI created Eastern month conflict; "
                        "submission timestamp plus normal schedule cannot distinguish a deferred "
                        "mailing from delayed DOI registration."
                    ),
                    "arXiv 官方 mailing/RSS export、带时间戳的官方 listing snapshot 或作者收到的 posting notice",
                    f"arxiv-{row['arxiv_id']}-first-announcement.txt",
                    "锁定 owner Daily；随后重跑该 family 的跨日报去重、selection 与 Books decision",
                ]
            )

    summary = {
        "schema": "official-arxiv-first-public-owner-recovery-summary-v1",
        "candidate_rows_after_withdrawn_exclusion": len(rows),
        "resolved_owner": sum(row["reconciliation"] != AMBIGUOUS for row in rows),
        "ambiguous_owner": len(ambiguous),
        "owner_consistent_in_current_report": sum(
            row["reconciliation"] == "owner_confirmed_by_datacite" for row in rows
        ),
        "owner_move_required": sum(
            row["reconciliation"] == "owner_move_required" for row in rows
        ),
        "withdrawn_excluded": len(WITHDRAWN),
    }
    (AUDIT / "owner-recovery-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
