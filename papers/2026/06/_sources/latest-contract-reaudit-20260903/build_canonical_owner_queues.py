#!/usr/bin/env python3
"""Build canonical per-day candidate move queues without mutating Daily prose."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent
OWNER_TSV = AUDIT / "owner-recovery/owner-reconciliation.tsv"
WITHDRAWN = {"2606.24369"}
SHANGHAI = ZoneInfo("Asia/Shanghai")


def table_rows(text: str, marker: str) -> dict[str, list[str]]:
    match = re.search(
        rf"<!-- {re.escape(marker)} -->\n(.*?)(?=\n(?:<!--|##|###)|\Z)", text, re.S
    )
    rows: dict[str, list[str]] = {}
    if not match:
        return rows
    for line in match.group(1).splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*:?-+", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0].startswith("SF-"):
            rows[cells[0]] = cells
    return rows


def iso_week(value: str) -> str:
    year, week, _ = date.fromisoformat(value).isocalendar()
    return f"{year}-W{week:02d}"


def main() -> None:
    source: dict[str, dict] = {}
    for month in ("06", "07"):
        for report in sorted((ROOT / f"papers/2026/{month}").glob("[0-9][0-9]/README.md")):
            text = report.read_text(encoding="utf-8")
            candidates = table_rows(text, "validator:candidate-ledger-v2.1")
            reviews = table_rows(text, "validator:review-completion-v1")
            for family, cells in candidates.items():
                source[family] = {
                    "source_report_date": f"2026-{month}-{report.parent.name}",
                    "source_report": report.relative_to(ROOT).as_posix(),
                    "candidate_cells": cells,
                    "review_cells": reviews.get(family),
                    "review_block_present": f"<!-- review:{family}:start -->" in text,
                    "claim_block_present": f"<!-- claim:{family}:start -->" in text,
                }

    owner_rows = [
        row for row in csv.DictReader(OWNER_TSV.open(encoding="utf-8"), delimiter="\t")
        if row["arxiv_id"] not in WITHDRAWN
    ]
    queues: dict[str, list[dict]] = {}
    blocked: list[dict] = []
    external: list[dict] = []
    missing: list[dict] = []
    for owner in owner_rows:
        family = owner["source_family_id"]
        bundle = source.get(family)
        if bundle is None:
            missing.append({"source_family_id": family, "reason": "candidate row missing"})
            continue
        target = owner["resolved_owner_report_date"]
        item = {
            "source_family_id": family,
            "primary_identifier": owner["primary_identifier"],
            "title": owner["title"],
            "source_report_date": bundle["source_report_date"],
            "resolved_owner_report_date": target,
            "owner_week": iso_week(target),
            "datacite_created_utc": owner["datacite_created"],
            "normal_schedule_owner_date": owner["schedule_owner_report_date"],
            "schedule_matches_datacite_owner": owner["schedule_matches_datacite_owner"],
            "reconciliation": owner["reconciliation"],
            "candidate_cells": bundle["candidate_cells"],
            "review_cells": bundle["review_cells"],
            "review_block_present": bundle["review_block_present"],
            "claim_block_present": bundle["claim_block_present"],
            "transfer_ready": bool(
                bundle["review_cells"]
                and bundle["review_block_present"]
                and bundle["claim_block_present"]
            ),
        }
        if owner["reconciliation"] == "identifier_month_conflict_ambiguous":
            blocked.append(item)
        elif not ("2026-06-01" <= target <= "2026-07-31"):
            external.append(item)
        else:
            queues.setdefault(target, []).append(item)

    for target in sorted(
        f"2026-{month}-{day:02d}"
        for month, last in (("06", 30), ("07", 31))
        for day in range(1, last + 1)
    ):
        month = target[5:7]
        packet = ROOT / f"papers/2026/{month}/_sources/daily-{target.replace('-', '')}"
        packet.mkdir(parents=True, exist_ok=True)
        items = sorted(queues.get(target, []), key=lambda item: item["source_family_id"])
        payload = {
            "schema": "canonical-owner-candidate-queue-v1",
            "target_report_date": target,
            "generated_at": datetime.now(SHANGHAI).isoformat(),
            "status": "ready_for_report_rebuild" if all(i["transfer_ready"] for i in items) else "blocked",
            "candidate_count": len(items),
            "moved_in": sum(i["source_report_date"] != target for i in items),
            "already_owned": sum(i["source_report_date"] == target for i in items),
            "transfer_ready": sum(i["transfer_ready"] for i in items),
            "items": items,
        }
        (packet / "canonical-owner-candidate-queue-v1.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    audit_payload = {
        "schema": "canonical-owner-rebuild-checkpoint-v1",
        "generated_at": datetime.now(SHANGHAI).isoformat(),
        "candidate_rows": len(owner_rows),
        "queued_within_june_july": sum(len(items) for items in queues.values()),
        "ambiguous": blocked,
        "external_owner_handoffs": external,
        "missing_source_bundles": missing,
        "per_target_counts": dict(sorted((key, len(value)) for key, value in queues.items())),
        "transfer_readiness": dict(
            Counter(
                "ready" if item["transfer_ready"] else "missing_review_bundle"
                for items in queues.values() for item in items
            )
        ),
    }
    (AUDIT / "canonical-owner-rebuild-checkpoint.json").write_text(
        json.dumps(audit_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
