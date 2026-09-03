#!/usr/bin/env python3
"""Bind legacy empty Daily denominator IDs to their owning report window."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY_EMPTY = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def denominator_id(report_date: str) -> str:
    return "sha256:" + hashlib.sha256((report_date + "\n").encode()).hexdigest()


def target_files(report_date: str) -> list[Path]:
    year, month, day = report_date.split("-")
    packet = ROOT / "papers" / year / month / "_sources" / f"daily-{year}{month}{day}"
    paths = [ROOT / "papers" / year / month / day / "README.md"]
    paths.extend(sorted(packet.glob("screening-ledger-*.json")))
    return paths


def repair(report_date: str, *, apply: bool) -> list[Path]:
    changed: list[Path] = []
    replacement = denominator_id(report_date)
    for path in target_files(report_date):
        text = path.read_text()
        if LEGACY_EMPTY not in text:
            continue
        changed.append(path)
        if apply:
            path.write_text(text.replace(LEGACY_EMPTY, replacement))
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dates", nargs="+")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    for report_date in args.dates:
        paths = repair(report_date, apply=args.apply)
        action = "updated" if args.apply else "would update"
        for path in paths:
            print(f"{action}: {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
