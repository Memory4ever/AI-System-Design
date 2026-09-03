#!/usr/bin/env python3
"""Freeze the latest nonempty report bodies before canonical owner rewrites."""

from __future__ import annotations

import gzip
import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent / "precanonical-report-snapshots-v1.json.gz"


def main() -> None:
    reports = []
    for month in ("06", "07"):
        for path in sorted((ROOT / f"papers/2026/{month}").glob("[0-9][0-9]/README.md")):
            body = path.read_text(encoding="utf-8")
            reports.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": hashlib.sha256(body.encode()).hexdigest(),
                    "body": body,
                }
            )
    payload = {
        "schema": "precanonical-report-snapshots-v1",
        "generated_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "report_count": len(reports),
        "reports": reports,
    }
    with gzip.open(OUT, "wt", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False)
        handle.write("\n")


if __name__ == "__main__":
    main()
