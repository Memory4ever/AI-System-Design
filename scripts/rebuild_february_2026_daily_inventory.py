#!/usr/bin/env python3
"""Materialize strict Beijing-window inventories for February 2026.

The input is the independently recovered arXiv announcement receipt.  Existing
Weekly reports are deliberately not read: Historical Daily discovery and
ownership must stand on primary-source identity/provenance alone.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone
import gzip
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH = ROOT / "papers/2026/02"
RECOVERY = MONTH / "_sources/february-2026-arxiv-announcement-recovery.json.gz"
BEIJING = timezone(timedelta(hours=8))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    with gzip.open(RECOVERY, "rt", encoding="utf-8") as handle:
        recovery = json.load(handle)
    grouped = {f"2026-02-{day:02d}": [] for day in range(1, 29)}
    for source in recovery["records"]:
        owner = source["owner_report_date"]
        if owner not in grouped:
            continue
        row = dict(source)
        row.update({
            "identity": f"{source['arxiv_id']}v1",
            "source_family_id": (
                "SF-2026-ARXIV-2602-" + source["arxiv_id"].split(".", 1)[1]
            ),
            "primary_category": (source.get("categories") or [""])[0],
            "route": "registered_category_full_title_abstract_screen",
            "source_url": f"https://arxiv.org/abs/{source['arxiv_id']}v1",
        })
        grouped[owner].append(row)

    recovery_hash = sha256(RECOVERY)
    for report_date, identities in grouped.items():
        day = int(report_date[-2:])
        end = datetime.combine(date(2026, 2, day), time(9), BEIJING)
        start = end - timedelta(days=1)
        identities.sort(key=lambda row: row["arxiv_id"])
        packet = MONTH / "_sources" / f"daily-202602{day:02d}"
        packet.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema": "daily-v2.1-arxiv-announcement-owned-inventory-v1",
            "report_date": report_date,
            "window_beijing": {"start": start.isoformat(), "end": end.isoformat()},
            "independent_historical_daily": True,
            "weekly_dependency": "none",
            "authority_boundary": recovery["authority_boundary"],
            "official_schedule_url": recovery["official_schedule_url"],
            "recovery_receipt": {
                "path": RECOVERY.relative_to(ROOT).as_posix(),
                "sha256": recovery_hash,
            },
            "registered_total": len(identities),
            "full_title_abstract_screen_required": len(identities),
            "identities": identities,
        }
        (packet / "inventory.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        )
        print(json.dumps({"date": report_date, "raw": len(identities)}))


if __name__ == "__main__":
    main()
