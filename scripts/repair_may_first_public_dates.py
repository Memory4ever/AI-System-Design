#!/usr/bin/env python3
"""Repair proven May 2026 Candidate Ledger first-public dates.

The source audit is the only repair input.  Every finding is revalidated against
the exact date-local screening ledger and the current README before any file is
written.  The operation is fail-closed and idempotent; it never changes review,
score, Books, or Gate fields.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUDIT = ROOT / "papers/2026/05/_sources/may-first-public-date-audit.json"
DEFAULT_RECEIPT = ROOT / "papers/2026/05/_sources/may-first-public-date-repair-receipt.json"
LOCAL_ZONE = ZoneInfo("Asia/Shanghai")
REQUIRED_COLUMNS = {
    "Source Family ID",
    "Primary Identifier",
    "Owner Week",
    "First-public Date",
}
EVIDENCE_RE = re.compile(
    r"^(?P<ledger>[^#;]+)#(?P<identity>\d{4}\.\d{4,5}v1)\."
    r"(?P<field>[^;]+);(?P<readme>[^#;]+)#.+$"
)
ARXIV_RE = re.compile(r"(?<!\d)(\d{4}\.\d{4,5})v1(?!\d)")


def clean_cell(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == "`":
        return value[1:-1]
    return value


def format_like(original: str, value: str) -> str:
    original = original.strip()
    return f"`{value}`" if len(original) >= 2 and original[0] == original[-1] == "`" else value


def ledger_rows(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("identities", "items", "rows"):
            rows = payload.get(key)
            if isinstance(rows, list):
                return rows
    raise ValueError("screening ledger has no supported identity list")


def candidate_table(text: str, path: Path) -> tuple[list[str], list[tuple[int, list[str]]]]:
    heading = "## 2. Candidate Ledger"
    heading_at = text.find(heading)
    if heading_at < 0:
        raise ValueError(f"missing Candidate Ledger: {path}")
    lines = text.splitlines()
    heading_line = next((i for i, line in enumerate(lines) if line.strip() == heading), None)
    if heading_line is None:
        raise ValueError(f"ambiguous Candidate Ledger heading: {path}")
    header_line = next(
        (
            i
            for i in range(heading_line + 1, len(lines))
            if lines[i].startswith("| Source Family ID |")
            and "First-public Date" in lines[i]
        ),
        None,
    )
    if header_line is None:
        raise ValueError(f"missing Candidate Ledger table: {path}")
    headers = [cell.strip() for cell in lines[header_line].strip().strip("|").split("|")]
    missing = REQUIRED_COLUMNS - set(headers)
    if missing:
        raise ValueError(f"missing Candidate Ledger columns {sorted(missing)}: {path}")
    rows: list[tuple[int, list[str]]] = []
    for index in range(header_line + 2, len(lines)):
        line = lines[index]
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            raise ValueError(f"malformed Candidate Ledger row at {path}:{index + 1}")
        rows.append((index, cells))
    return headers, rows


def iso_week(local_date: date) -> str:
    iso_year, iso_week_number, _ = local_date.isocalendar()
    return f"{iso_year}-W{iso_week_number:02d}"


def strict_window(report: str) -> tuple[datetime, datetime]:
    report_date = date.fromisoformat(report)
    end = datetime.combine(report_date, time(9, 0), tzinfo=LOCAL_ZONE)
    return end - timedelta(days=1), end


def parse_evidence_path(root: Path, finding: dict[str, Any]) -> tuple[Path, str, str, Path]:
    match = EVIDENCE_RE.fullmatch(finding.get("evidence_path", ""))
    if not match:
        raise ValueError(f"invalid evidence_path: {finding.get('report')} {finding.get('family')}")
    ledger = root / match.group("ledger")
    readme = root / match.group("readme")
    for path in (ledger, readme):
        if not path.is_file():
            raise ValueError(f"missing evidence file: {path}")
        try:
            path.resolve().relative_to(root.resolve())
        except ValueError as exc:
            raise ValueError(f"evidence path escapes repository: {path}") from exc
    return ledger, match.group("identity"), match.group("field"), readme


def find_exact_ledger_row(
    ledger: Path,
    identity: str,
    timestamp_field: str,
    raw_timestamp: str,
) -> dict[str, Any]:
    rows = ledger_rows(json.loads(ledger.read_text(encoding="utf-8")))
    arxiv_id = identity.removesuffix("v1")
    matches = [
        row
        for row in rows
        if row.get("identity") == identity
        or (row.get("arxiv_id") == arxiv_id and identity == f"{arxiv_id}v1")
    ]
    if len(matches) != 1:
        raise ValueError(f"exact identity count {len(matches)} for {identity} in {ledger}")
    row = matches[0]
    if timestamp_field not in row:
        raise ValueError(f"timestamp field {timestamp_field} missing for {identity} in {ledger}")
    if row[timestamp_field] != raw_timestamp:
        raise ValueError(f"timestamp evidence drift for {identity} in {ledger}")
    return row


def prepare_repairs(root: Path, audit_path: Path) -> tuple[dict[Path, str], dict[str, Any]]:
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    if audit.get("schema") != "may-first-public-date-audit-v1":
        raise ValueError(f"unsupported audit schema: {audit.get('schema')}")
    findings = audit.get("findings")
    if not isinstance(findings, list) or len(findings) != audit.get("summary", {}).get("mismatch_count"):
        raise ValueError("audit finding count does not match summary")
    identities = [(item.get("report"), item.get("family")) for item in findings]
    if len(identities) != len(set(identities)):
        raise ValueError("audit contains duplicate report/family findings")

    original_texts: dict[Path, str] = {}
    rendered_lines: dict[Path, list[str]] = {}
    receipt_items: list[dict[str, Any]] = []
    date_changes = 0
    owner_week_changes = 0
    already_correct = 0

    for finding in findings:
        report = finding.get("report", "")
        family = finding.get("family", "")
        ledger, identity, timestamp_field, readme = parse_evidence_path(root, finding)
        if readme not in original_texts:
            original_texts[readme] = readme.read_text(encoding="utf-8")
            rendered_lines[readme] = original_texts[readme].splitlines()

        raw_timestamp = finding.get("raw_timestamp", "")
        find_exact_ledger_row(ledger, identity, timestamp_field, raw_timestamp)
        instant = datetime.fromisoformat(raw_timestamp.replace("Z", "+00:00"))
        if instant.tzinfo is None:
            raise ValueError(f"timestamp lacks timezone: {report} {family}")
        instant = instant.astimezone(timezone.utc)
        window_start, window_end = strict_window(report)
        if not (window_start <= instant.astimezone(LOCAL_ZONE) < window_end):
            raise ValueError(
                f"timestamp outside strict window: {report} {family} {raw_timestamp} "
                f"not in [{window_start.isoformat()}, {window_end.isoformat()})"
            )
        local_instant = instant.astimezone(LOCAL_ZONE)
        expected_date = local_instant.date().isoformat()
        expected_owner_week = iso_week(local_instant.date())
        if expected_date != finding.get("expected_local_date"):
            raise ValueError(f"audit local-date drift: {report} {family}")

        current_text = "\n".join(rendered_lines[readme]) + (
            "\n" if original_texts[readme].endswith("\n") else ""
        )
        headers, rows = candidate_table(current_text, readme)
        family_col = headers.index("Source Family ID")
        primary_col = headers.index("Primary Identifier")
        owner_col = headers.index("Owner Week")
        date_col = headers.index("First-public Date")
        matches = [(line_index, cells) for line_index, cells in rows if clean_cell(cells[family_col]) == family]
        if len(matches) != 1:
            raise ValueError(f"candidate row count {len(matches)} for {report} {family}")
        line_index, cells = matches[0]
        primary_ids = ARXIV_RE.findall(clean_cell(cells[primary_col]))
        expected_arxiv_id = identity.removesuffix("v1")
        if len(primary_ids) != 1 or primary_ids[0] != expected_arxiv_id:
            raise ValueError(f"primary identifier mismatch for {report} {family}: {cells[primary_col]}")

        date_before = clean_cell(cells[date_col])
        owner_before = clean_cell(cells[owner_col])
        audited_before = finding.get("current_field")
        if date_before not in {audited_before, expected_date}:
            raise ValueError(
                f"current First-public Date drift for {report} {family}: "
                f"{date_before} not in {{{audited_before}, {expected_date}}}"
            )
        date_changed = date_before != expected_date
        owner_changed = owner_before != expected_owner_week
        if date_changed:
            cells[date_col] = format_like(cells[date_col], expected_date)
            date_changes += 1
        if owner_changed:
            cells[owner_col] = format_like(cells[owner_col], expected_owner_week)
            owner_week_changes += 1
        if not date_changed and not owner_changed:
            already_correct += 1
        rendered_lines[readme][line_index] = "| " + " | ".join(cells) + " |"
        receipt_items.append(
            {
                "report": report,
                "family": family,
                "primary_identifier": identity,
                "raw_timestamp": raw_timestamp,
                "local_instant": local_instant.isoformat(),
                "strict_window": f"[{window_start.isoformat()}, {window_end.isoformat()})",
                "readme": str(readme.relative_to(root)),
                "date_before": date_before,
                "date_after": expected_date,
                "owner_week_before": owner_before,
                "owner_week_after": expected_owner_week,
                "date_changed": date_changed,
                "owner_week_changed": owner_changed,
            }
        )

    rendered: dict[Path, str] = {}
    for path, lines in rendered_lines.items():
        suffix = "\n" if original_texts[path].endswith("\n") else ""
        new_text = "\n".join(lines) + suffix
        if new_text != original_texts[path]:
            rendered[path] = new_text

    receipt = {
        "schema": "may-first-public-date-repair-receipt-v1",
        "source_audit": str(audit_path.relative_to(root)),
        "timezone": "Asia/Shanghai",
        "summary": {
            "findings_validated": len(findings),
            "reports_validated": len({item["report"] for item in receipt_items}),
            "files_changed": len(rendered),
            "date_changes": date_changes,
            "owner_week_changes": owner_week_changes,
            "already_correct": already_correct,
        },
        "items": receipt_items,
    }
    return rendered, receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--audit", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--apply", action="store_true", help="write validated README repairs and receipt")
    args = parser.parse_args()

    root = args.root.resolve()
    audit = args.audit.resolve() if args.audit else root / DEFAULT_AUDIT.relative_to(ROOT)
    receipt_path = args.receipt.resolve() if args.receipt else root / DEFAULT_RECEIPT.relative_to(ROOT)
    rendered, receipt = prepare_repairs(root, audit)
    if args.apply:
        for path, text in sorted(rendered.items(), key=lambda pair: str(pair[0])):
            path.write_text(text, encoding="utf-8")
        if rendered or not receipt_path.exists():
            receipt_path.write_text(
                json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    mode = "applied" if args.apply else "dry-run"
    print(json.dumps({"mode": mode, **receipt["summary"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
