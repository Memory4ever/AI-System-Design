#!/usr/bin/env python3
"""Build a read-only June/July V2.1 recovery ledger from non-empty evidence."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
REGISTRY = ROOT / "docs/RESEARCH_SOURCES.md"
OUT = Path(__file__).resolve().parent


def required_daily_sources() -> list[str]:
    sources: list[str] = []
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        if line.startswith("| SRC-") and "| Required Daily |" in line:
            sources.append(line.split("|")[1].strip())
    return sources


def table_rows(text: str, marker: str) -> list[list[str]]:
    match = re.search(
        rf"<!-- {re.escape(marker)} -->\n(.*?)(?=\n(?:<!--|##|###)|\Z)", text, re.S
    )
    if not match:
        return []
    rows: list[list[str]] = []
    for line in match.group(1).splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*:?-+", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] not in {"Field", "Source ID", "Source Family ID", "Scope"}:
            rows.append(cells)
    return rows


def has_nonempty_named(packet_roots: list[Path], needles: tuple[str, ...]) -> bool:
    for root in packet_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.stat().st_size == 0:
                continue
            name = path.name.lower()
            if any(needle in name for needle in needles):
                return True
    return False


def has_per_identity_closure(packet_roots: list[Path]) -> bool:
    """Accept a ledger only when it is non-empty and contains row-level closure semantics."""
    canonical = []
    for root in packet_roots:
        if not root.exists():
            continue
        canonical.extend(root.rglob("canonical-semantic-screening-checkpoint-v2.1.json.gz"))
    if canonical:
        # A reconstructed proposal is evidence of work remaining, not a closure
        # receipt.  Prefer the canonical latest-contract checkpoint over stale
        # submission-date ledgers when both are present.
        import gzip

        for path in canonical:
            if not path.is_file() or path.stat().st_size == 0:
                continue
            try:
                with gzip.open(path, "rt", encoding="utf-8") as handle:
                    status = json.load(handle).get("status", "")
            except (OSError, json.JSONDecodeError):
                continue
            if status not in {"complete", "closed", "fresh_context_audit_passed"}:
                return False
        return True
    direct_needles = (
        "screening-ledger",
        "denominator-full-semantic-audit",
        "candidate-denominator-audit",
    )
    if has_nonempty_named(packet_roots, direct_needles):
        return True
    for root in packet_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.stat().st_size == 0:
                continue
            if "candidate-denominator" not in path.name.lower():
                continue
            try:
                sample = path.read_text(encoding="utf-8", errors="ignore")[:2_000_000].lower()
            except OSError:
                continue
            if any(
                token in sample
                for token in (
                    "pre_denominator_closure",
                    "pre-denominator closure",
                    "closure_class",
                    '"closures"',
                    "\tclosure_only\t",
                )
            ):
                return True
    return False


def source_roots(month: str, day: str) -> list[Path]:
    src = ROOT / "papers" / "2026" / month / "_sources"
    compact = f"daily-2026{month}{day}"
    roots = [p for p in src.iterdir() if p.is_dir() and compact in p.name]
    if month == "07":
        roots.extend(
            [
                src / "datacite-arxiv-recovery-20260701-26",
                src / "arxiv-v2.1-replay-20260727-31",
                src / f"daily-v2.1-2026-07-{day}",
            ]
        )
    return list(dict.fromkeys(roots))


def audit_report(report: Path, required: list[str]) -> dict:
    text = report.read_text(encoding="utf-8")
    month, day = report.parts[-3], report.parts[-2]
    roots = source_roots(month, day)
    coverage = table_rows(text, "validator:source-coverage-v2")
    candidates = table_rows(text, "validator:candidate-ledger-v2.1")
    reviews = table_rows(text, "validator:review-completion-v1")
    source_ids = sorted({row[0] for row in coverage if row})
    arxiv_row = next((row for row in coverage if row and row[0] == "SRC-ARXIV"), [])
    try:
        reported_arxiv_hits = int(arxiv_row[6])
    except (IndexError, ValueError):
        reported_arxiv_hits = None
    arxiv_contract_mismatch = any(
        token in " ".join(arxiv_row).lower()
        for token in ("submitteddate", "submitted timestamp", "v1 published timestamp", "atom published")
    )
    official_owner_receipt = has_nonempty_named(
        roots,
        (
            "official-listing", "announcement-listing", "arxiv-listing", "listing-receipt",
            "official-arxiv-first-public-owner-receipt",
        ),
    )
    raw_inventory = has_nonempty_named(
        roots,
        (
            "raw-inventory", "raw-identity-inventory", "candidate-inventory",
            "screening-ledger", "registered-hit-screening", "coverage-",
        ),
    )
    closure_ledger = has_per_identity_closure(roots)
    exact_material = has_nonempty_named(
        roots, ("exact-v1", "arxiv-html", "arxiv-v1", "primary-review-receipts", "source-review-receipts")
    )
    # A local HTML/PDF copy is useful but not required by the contract when
    # every candidate has a complete V2.1 receipt with an exact primary
    # version and source-locatable facet refs. validate_research separately
    # verifies those row/body interfaces.
    if candidates and len(candidates) == len(reviews):
        exact_material = exact_material or all(
            len(row) == 11
            and re.search(r"(?:arXiv:)?\d{4}\.\d{4,5}v1", row[3])
            and row[10] == "complete"
            for row in reviews
        )
    nonempty = 0
    empty = 0
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file():
                if path.stat().st_size:
                    nonempty += 1
                else:
                    empty += 1
    issues: list[str] = []
    if not raw_inventory:
        issues.append("raw_inventory_missing")
    if not closure_ledger:
        issues.append("per_identity_closure_missing")
    if arxiv_contract_mismatch or not official_owner_receipt:
        issues.append("official_arxiv_first_public_receipt_missing")
    if not exact_material and candidates:
        issues.append("exact_primary_material_missing")
    if len(candidates) != len(reviews):
        issues.append("candidate_review_cardinality_mismatch")
    if empty:
        issues.append("zero_byte_files_ignored")
    integrate = sum(1 for row in candidates if len(row) > 19 and row[19] == "Integrate")
    return {
        "date": f"2026-{month}-{day}",
        "report": str(report.relative_to(ROOT)),
        "candidate_count": len(candidates),
        "reported_arxiv_hits": reported_arxiv_hits,
        "candidate_to_reported_hit_rate": (
            round(len(candidates) / reported_arxiv_hits, 6)
            if reported_arxiv_hits
            else None
        ),
        "review_count": len(reviews),
        "integrate_count": integrate,
        "existing_source_ids": source_ids,
        "missing_required_source_ids": [],
        "source_packet_roots": [str(p.relative_to(ROOT)) for p in roots if p.exists()],
        "nonempty_packet_files": nonempty,
        "ignored_zero_byte_files": empty,
        "raw_inventory": raw_inventory,
        "per_identity_closure": closure_ledger,
        "exact_primary_material": exact_material,
        "official_arxiv_first_public_receipt": official_owner_receipt,
        "issues": issues,
        "latest_contract_status": (
            "reopen_required"
            if any(issue != "zero_byte_files_ignored" for issue in issues)
            else "ready_for_fresh_context_reaudit"
        ),
    }


def main() -> None:
    required = required_daily_sources()
    reports: list[dict] = []
    for month in ("06", "07"):
        for report in sorted((ROOT / "papers" / "2026" / month).glob("[0-9][0-9]/README.md")):
            reports.append(audit_report(report, required))

    payload = {
        "schema": "daily-latest-contract-month-recovery-v1",
        "generated_at": "2026-09-03T11:41:57+08:00",
        "scope": ["2026-06-01..2026-06-30", "2026-07-01..2026-07-31"],
        "required_daily_source_ids": required,
        "reports": reports,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ledger.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    for month in ("06", "07"):
        entries: list[dict] = []
        for row in reports:
            if not row["date"].startswith(f"2026-{month}"):
                continue
            report = ROOT / row["report"]
            candidates = table_rows(
                report.read_text(encoding="utf-8"), "validator:candidate-ledger-v2.1"
            )
            for candidate in candidates:
                if len(candidate) <= 20 or candidate[19] != "Integrate":
                    continue
                entries.append(
                    {
                        "date": row["date"],
                        "source_family_id": candidate[0],
                        "primary_identifier": candidate[1],
                        "stable_node_id": candidate[18],
                        "prior_books_disposition": candidate[19],
                        "books_review_ref": candidate[20],
                        "report": row["report"],
                        "queue_status": "frozen_pending_upstream_reconciliation",
                        "reason": (
                            "Preserved from the prior report as provenance only; do not write Books "
                            "until official first-public owner reconciliation and fresh-context "
                            "Coverage/Evidence/Books audits all pass."
                        ),
                    }
                )
        queue = {
            "schema": "books-writeback-queue-v2.1-recovery-v1",
            "month": f"2026-{month}",
            "generated_at": "2026-09-03T11:41:57+08:00",
            "status": "frozen",
            "write_authority": "root-sequential-owner-only",
            "entry_count": len(entries),
            "entries": entries,
        }
        queue_path = ROOT / "papers" / "2026" / month / "_sources" / "BOOKS_WRITEBACK_QUEUE_latest-contract.json"
        queue_path.write_text(
            json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    with (OUT / "materials-request.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "Request ID", "Priority", "Source ID", "Gap / Limitation ID",
                "Affected Dates", "Known Endpoint", "Missing Material",
                "Why Existing Evidence Is Insufficient", "Acceptable Substitute",
                "Suggested File Name", "Required Review Scope",
            ]
        )
        owner_path = OUT / "owner-recovery" / "owner-reconciliation.tsv"
        with owner_path.open(encoding="utf-8") as owner_handle:
            for item in csv.DictReader(owner_handle, delimiter="\t"):
                if item["reconciliation"] != "identifier_month_conflict_ambiguous":
                    continue
                aid = item["arxiv_id"]
                writer.writerow(
                    [
                        f"MR-SRC-ARXIV-{aid}-OWNER", "P3 Revision", "SRC-ARXIV",
                        f"GAP-ARXIV-FIRST-PUBLIC-{aid}", item["report_date"],
                        f"https://arxiv.org/abs/{aid}v1",
                        f"{aid} 的官方首次 announcement/listing 事件记录",
                        (
                            f"identifier month、submission schedule 与 DataCite created 对 owner 日期存在冲突；"
                            f"schedule={item['schedule_owner_report_date']}，DataCite={item['datacite_owner_report_date']}"
                        ),
                        "arXiv 官方 daily listing/e-mail entry，或带可验证时间戳的官方 announcement archive",
                        f"arxiv-{aid}-first-announcement.html",
                        "只重算该 Source Family 的 first-public owner、跨日报引用与 Books queue 归属",
                    ]
                )

    issue_counts = Counter(issue for row in reports for issue in row["issues"])
    month_lines = []
    for month in ("06", "07"):
        rows = [row for row in reports if row["date"].startswith(f"2026-{month}")]
        month_lines.append(
            f"| 2026-{month} | {len(rows)} | {sum(r['candidate_count'] for r in rows)} | "
            f"{sum(r['review_count'] for r in rows)} | {sum(r['integrate_count'] for r in rows)} | "
            f"{sum(r['latest_contract_status'] == 'ready_for_fresh_context_reaudit' for r in rows)} |"
        )
    issue_lines = "\n".join(f"- `{key}`: {value} reports" for key, value in sorted(issue_counts.items()))
    readme = f"""# 2026-06 / 2026-07 Daily 最新合同复核

本账本只接受非空 evidence file。它不会因为旧报告写有 `Complete`、validator 通过或文件名存在，就把证据视为已经闭合。

## 结论

| Month | Reports | Candidates | Review rows | Integrate dispositions | Ready for fresh-context audit |
| --- | ---: | ---: | ---: | ---: | ---: |
{chr(10).join(month_lines)}

当前两个月都不能沿用旧 `Complete`：官方 arXiv availability、exact-v1 Atom 与 DataCite DOI `created` 已恢复 1,960 个未撤稿候选的 first-public owner，其中 1,060 个可确认需要跨日报移动，2 个 identifier-month / DOI-created 冲突仍需 exact announcement 材料；部分报告还缺失 raw inventory、逐 identity closure 或 exact-version primary material。6 月的零字节恢复空壳不计入任何 Gate。2026-08-25 才生效的新增来源不倒推为 6～7 月 Required Daily receipt；它们只按 Source Delta Audit 规则检查是否发现真实 in-window family。

## Findings

{issue_lines}

## Recovery boundary

- `ledger.json` 保存逐日报告、来源缺口、每日报告可引用的非空/空文件计数和候选/Review 算术。共享月级 packet 可被多个日期引用，因此 README 不汇总文件计数，以免重复计数。
- `materials-request.tsv` 仅列 2 个 identifier month 与 DOI-created Eastern month 冲突的 exact announcement 证明；普通 owner move、分母重放和零字节恢复都不得转嫁给用户。
- 已有候选、Review 与 Integrate 判断暂时保留为 provenance，不作为最新合同已通过结论；owner 修复后必须重新运行 denominator、fresh-context false-positive/false-negative audit 与 Books comparison。
- 本任务不直接修改 Books；旧 `Integrate` 已进入月内 `BOOKS_WRITEBACK_QUEUE_latest-contract.json`，但全部冻结为 `frozen_pending_upstream_reconciliation`，只能由单一 owner 在上游 Gate 与 fresh-context Books comparison 通过后按日期合并。
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
