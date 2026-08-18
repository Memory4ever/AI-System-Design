#!/usr/bin/env python3
"""Synchronize rendered July Review Provenance IDs into durable receipts.

The renderer owns the canonical RP hash because it sees the final normalized
claim body, evidence locators and benchmark contract.  After rendering, this
tool copies those IDs back to the day packet and central ledger so the report,
packet and ledger remain one auditable provenance chain.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26"
LEDGER_PATH = SOURCE_DIR / "primary-review-receipts.json"
PACKET_DIR = SOURCE_DIR / "daily-review-packets"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rendered_rps(report_path: Path) -> dict[str, str]:
    lines = report_path.read_text(encoding="utf-8").splitlines()
    try:
        marker = lines.index("<!-- validator:review-completion-v1 -->")
    except ValueError as exc:
        raise ValueError(f"{report_path}: missing review-completion marker") from exc

    header = [cell.strip() for cell in lines[marker + 1].strip("|").split("|")]
    family_col = header.index("Source Family ID")
    rp_col = header.index("Review Provenance ID")
    result: dict[str, str] = {}
    for line in lines[marker + 3 :]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(header):
            raise ValueError(f"{report_path}: malformed review row: {line[:120]}")
        family, rp = cells[family_col], cells[rp_col]
        if not re.fullmatch(r"RP-[0-9a-f]{16}", rp):
            raise ValueError(f"{report_path}: invalid RP for {family}: {rp}")
        if family in result and result[family] != rp:
            raise ValueError(f"{report_path}: duplicate family with conflicting RP: {family}")
        result[family] = rp
    if not result:
        raise ValueError(f"{report_path}: no rendered Review Provenance rows")
    return result


def arxiv_id(family: str) -> str:
    match = re.fullmatch(r"SF-\d{4}-ARXIV-(\d{4})[.-](\d{4,5})", family)
    if not match:
        raise ValueError(f"Cannot derive arXiv ID from {family}")
    return f"{match.group(1)}.{match.group(2)}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    report_path = ROOT / f"papers/2026/07/{args.date[-2:]}/README.md"
    packet_path = PACKET_DIR / f"{args.date}.json"
    packet = load_json(packet_path)
    ledger = load_json(LEDGER_PATH)
    rps = rendered_rps(report_path)

    packet_families: set[str] = set()
    changed = 0
    for key in ("full_source_reviews", "families", "closure_reviews"):
        for review in packet.get(key, []):
            family = review.get("source_family") or review.get("source_family_id")
            if not family:
                continue
            packet_families.add(family)
            rp = rps.get(family)
            if not rp:
                raise ValueError(f"{packet_path}: rendered RP missing for {family}")
            if review.get("review_provenance_id") != rp:
                review["review_provenance_id"] = rp
                changed += 1

            identifier = arxiv_id(family)
            central = packet.setdefault("central_receipts", {}).get(identifier)
            shared = ledger.get(identifier)
            if central is None or shared is None:
                raise ValueError(f"{family}: missing packet or shared central receipt")
            if central.get("review_provenance_id") != rp:
                central["review_provenance_id"] = rp
                changed += 1
            if shared.get("review_provenance_id") != rp:
                shared["review_provenance_id"] = rp
                changed += 1

    extra = set(rps) - packet_families
    if extra:
        raise ValueError(f"{report_path}: rendered families not owned by packet: {sorted(extra)}")

    if args.write:
        write_json(packet_path, packet)
        write_json(LEDGER_PATH, ledger)
    print(json.dumps({"date": args.date, "families": len(packet_families), "updates": changed, "write": args.write}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
