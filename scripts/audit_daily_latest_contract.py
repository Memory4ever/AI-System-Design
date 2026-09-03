#!/usr/bin/env python3
"""Inventory every formal Daily against the current V2.1 evidence contract.

This is deliberately a *readiness* audit.  It proves whether the report and
its recoverable source packet expose enough material for a new independent
semantic review; it never upgrades a report merely because its own embedded
Semantic Audit table says ``passed``.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Mapping, Sequence, Set, Tuple

from scripts import validate_research as validator


DAILY_PATH = re.compile(r"^papers/(\d{4})/(\d{2})/(\d{2})/README\.md$")
AUDIT_VERSION = "daily-latest-contract-readiness-v1"


@dataclass
class SourcePacketSignals:
    packet_present: bool = False
    nonempty_file_count: int = 0
    empty_file_count: int = 0
    coverage_receipt: bool = False
    screening_ledger: bool = False
    per_identity_closures: bool = False
    raw_inventory: bool = False
    exact_primary_material: bool = False
    arxiv_owner_receipt: bool = False


def discover_daily_reports(root: Path) -> List[Path]:
    papers = root / "papers"
    if not papers.exists():
        return []
    reports: List[Path] = []
    for path in papers.rglob("README.md"):
        try:
            relative = path.relative_to(root).as_posix()
        except ValueError:
            continue
        if DAILY_PATH.fullmatch(relative):
            reports.append(path)
    return sorted(reports)


def _table(text: str, marker: str, columns: Sequence[str]) -> List[Dict[str, str]]:
    if marker not in text:
        return []
    rows, _errors = validator._expect_columns(text, marker, columns)
    return rows


def _metadata(text: str) -> Dict[str, str]:
    rows = _table(text, validator.METADATA_MARKER, validator.METADATA_COLUMNS)
    errors: List[str] = []
    return validator._metadata(rows, errors) if rows else {}


def _candidate_rows(text: str) -> List[Dict[str, str]]:
    return _table(text, validator.CANDIDATE_LEDGER_MARKER, validator.CANDIDATE_COLUMNS)


def _review_rows(text: str) -> List[Dict[str, str]]:
    return _table(text, validator.REVIEW_COMPLETION_MARKER, validator.REVIEW_COMPLETION_COLUMNS)


def _semantic_scopes(text: str) -> Dict[str, str]:
    rows = _table(text, validator.SEMANTIC_AUDIT_MARKER, validator.SEMANTIC_AUDIT_COLUMNS)
    return {row.get("Scope", ""): row.get("Status", "") for row in rows}


def _arxiv_receipt_due(coverage_rows: Sequence[Mapping[str, str]]) -> bool:
    return any(
        row.get("Source ID") == "SRC-ARXIV" and row.get("Result") != "not_due"
        for row in coverage_rows
    )


def _report_source_refs(root: Path, report: Path, text: str) -> Set[Path]:
    refs: Set[Path] = set()
    month = report.parents[1]
    source_root = month / "_sources"
    date_compact = "".join(report.parts[-4:-1])
    date_iso = "-".join(report.parts[-4:-1])

    if source_root.exists():
        patterns = (
            f"daily-{date_compact}",
            f"daily-v2.1-{date_iso}",
            date_iso,
            date_compact,
        )
        for path in source_root.rglob("*"):
            if any(token in path.name or token in path.as_posix() for token in patterns):
                refs.add(path if path.is_dir() else path.parent)

    # Reports from earlier generations often point at an aggregate monthly
    # replay rather than a per-day directory.  Resolve only explicit local
    # references; a nearby _sources directory alone is not evidence.
    for raw in re.findall(r"(?:papers/\d{4}/\d{2}/)?_sources/[A-Za-z0-9_.@/\-]+", text):
        clean = raw.rstrip(".,;:)]}`")
        candidate = (month / clean) if clean.startswith("_sources/") else (root / clean)
        if candidate.exists():
            refs.add(candidate if candidate.is_dir() else candidate.parent)
    for raw in re.findall(r"(?:\.\./)+_sources/[A-Za-z0-9_.@/\-]+", text):
        candidate = (report.parent / raw.rstrip(".,;:)]}`")).resolve()
        if candidate.exists():
            refs.add(candidate if candidate.is_dir() else candidate.parent)
    return refs


def _read_signal_text(paths: Sequence[Path]) -> str:
    chunks: List[str] = []
    for directory in paths:
        if not directory.exists():
            continue
        files = [directory] if directory.is_file() else directory.rglob("*")
        for path in files:
            if not path.is_file() or path.suffix.lower() not in {".json", ".md", ".tsv", ".txt"}:
                continue
            try:
                if path.stat().st_size > 5_000_000:
                    continue
                chunks.append(path.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                continue
    return "\n".join(chunks).casefold()


def source_packet_signals(root: Path, report: Path, text: str) -> Tuple[SourcePacketSignals, List[str]]:
    refs = sorted(_report_source_refs(root, report, text), key=str)
    files: List[Path] = []
    for ref in refs:
        if ref.is_file():
            files.append(ref)
        elif ref.exists():
            files.extend(path for path in ref.rglob("*") if path.is_file())
    nonempty_files: List[Path] = []
    empty_files: List[Path] = []
    for path in files:
        try:
            (nonempty_files if path.stat().st_size > 0 else empty_files).append(path)
        except OSError:
            empty_files.append(path)

    # A recovered path or filename is not evidence when its content is empty.
    # Filesystem recovery may preserve directory trees and names without the
    # receipt, ledger, or review body they used to contain.
    names = "\n".join(path.as_posix().casefold() for path in nonempty_files)
    bodies = _read_signal_text(refs)
    combined = names + "\n" + bodies
    signals = SourcePacketSignals(
        packet_present=bool(nonempty_files),
        nonempty_file_count=len(nonempty_files),
        empty_file_count=len(empty_files),
        coverage_receipt=bool(re.search(r"coverage[-_ ]receipt|coverage-\d{4}-\d{2}-\d{2}|coverage receipt", combined)),
        screening_ledger=bool(re.search(r"screening[-_ ]ledger|candidate[-_ ]denominator|denominator\.json|registered[-_ ]hit[-_ ]screening", combined)),
        per_identity_closures=bool(re.search(r"pre[-_ ]denominator|reason_code|screening_reason|screening_decision", bodies)),
        raw_inventory=bool(re.search(r"inventory|enumeration|manifest|snapshot|\.xml(?:\.gz)?|arxiv[-_ ]screen(?:ing)?", names)),
        exact_primary_material=bool(re.search(r"exact[-_ ]v1|arxiv[-_ ].*v1\.(?:html|pdf)|review[-_ ]packet|primary[-_ ]review", names)),
        # A listing snapshot proves that an identity appeared on a page, but
        # not whether the appearance was a new announcement or a replacement.
        # Current OAI datestamps have the same ambiguity.  Require an explicit
        # event-classified ownership receipt so revisions cannot be reassigned
        # to the day on which the latest metadata was announced.
        arxiv_owner_receipt=bool(
            re.search(
                r'"ownership_method"\s*:\s*"(?:official_)?(?:new_announcement|announcement_reconciled|first_announcement)',
                bodies,
            )
            or re.search(
                r'"owner_proof"\s*:\s*"official_new_announcement"',
                bodies,
            )
        ),
    )
    display = []
    for path in refs:
        try:
            display.append(path.relative_to(root).as_posix())
        except ValueError:
            display.append(path.as_posix())
    return signals, display


def classify_latest_contract(
    *,
    validator_errors: Sequence[str],
    candidate_count: int,
    review_count: int,
    semantic_scopes: Mapping[str, str],
    signals: SourcePacketSignals,
    arxiv_due: bool = False,
    historical_weekly_dependency: bool = False,
) -> List[str]:
    issues: List[str] = []
    if validator_errors:
        issues.append("report_interface_invalid")
    if not signals.packet_present:
        issues.append("source_packet_missing")
    if not signals.raw_inventory:
        issues.append("raw_inventory_missing")
    if not signals.screening_ledger:
        issues.append("screening_ledger_missing")
    if not signals.per_identity_closures:
        issues.append("per_identity_closure_missing")
    if arxiv_due and not signals.arxiv_owner_receipt:
        issues.append("arxiv_owner_date_receipt_missing")
    if historical_weekly_dependency:
        issues.append("historical_daily_weekly_dependency")
    if candidate_count != review_count:
        issues.append("candidate_review_count_mismatch")
    required_scopes = {"coverage", "evidence", "deep_analysis_selection", "books"}
    if set(semantic_scopes) != required_scopes or any(
        semantic_scopes.get(scope) != "passed" for scope in required_scopes
    ):
        issues.append("embedded_semantic_audit_not_passed")
    return issues


def next_recovery_action(issues: Sequence[str]) -> str:
    issue_set = set(issues)
    if "report_interface_invalid" in issue_set:
        return "repair_report_interface"
    if "source_packet_missing" in issue_set or "raw_inventory_missing" in issue_set:
        return "restore_or_replay_raw_inventory"
    if "historical_daily_weekly_dependency" in issue_set:
        return "independent_historical_discovery_replay"
    if "arxiv_owner_date_receipt_missing" in issue_set:
        return "recover_official_listing_owner_receipt"
    if "screening_ledger_missing" in issue_set or "per_identity_closure_missing" in issue_set:
        return "replay_full_semantic_screening"
    if "candidate_review_count_mismatch" in issue_set:
        return "repair_candidate_review_frontier"
    if "embedded_semantic_audit_not_passed" in issue_set:
        return "resolve_embedded_semantic_findings"
    return "fresh_context_semantic_reaudit"


def audit_report(root: Path, report: Path, registry, stable_node_ids: Set[str]) -> Dict[str, object]:
    text = report.read_text(encoding="utf-8")
    metadata = _metadata(text)
    candidates = _candidate_rows(text)
    reviews = _review_rows(text)
    semantics = _semantic_scopes(text)
    coverage_rows = _table(text, validator.SOURCE_COVERAGE_MARKER, validator.SOURCE_COVERAGE_COLUMNS)
    # A zero-hit claim needs the same frozen official listing/announcement
    # evidence as a positive hit.  Otherwise an empty denominator can pass by
    # assertion alone, which is exactly the false-negative mode this audit is
    # meant to expose.
    arxiv_due = _arxiv_receipt_due(coverage_rows)
    historical_weekly_dependency = bool(
        re.search(r"prior discovery baseline|weekly[-_ ]derived|从.*weekly.*(?:seed|候选|review|评分)|weekly/.+baseline", text, re.IGNORECASE)
    )
    validation_errors = validator.validate_report_text(
        text,
        registry,
        strict=True,
        stable_node_ids=stable_node_ids,
    )
    signals, packet_refs = source_packet_signals(root, report, text)
    issues = classify_latest_contract(
        validator_errors=validation_errors,
        candidate_count=len(candidates),
        review_count=len(reviews),
        semantic_scopes=semantics,
        signals=signals,
        arxiv_due=arxiv_due,
        historical_weekly_dependency=historical_weekly_dependency,
    )
    integration_count = sum(row.get("Books Disposition") == "Integrate" for row in candidates)
    pending_count = sum(
        row.get("Review Status") in {"pending", "blocked"}
        or row.get("Access Status") in {"blocked", "unverified", "disputed"}
        or row.get("Books Disposition") in {"Blocked / Unverified", "Disputed", "Not Assessed"}
        for row in candidates
    )
    return {
        "report": report.relative_to(root).as_posix(),
        "date": metadata.get("Window End", ""),
        "completion_status": metadata.get("Completion Status", ""),
        "coverage_gate": metadata.get("Coverage Gate", ""),
        "evidence_gate": metadata.get("Evidence Gate", ""),
        "books_gate": metadata.get("Books Gate", ""),
        "candidate_count": len(candidates),
        "review_count": len(reviews),
        "integrate_count": integration_count,
        "pending_or_conditional_count": pending_count,
        "embedded_semantic_scopes": semantics,
        "source_packet_signals": asdict(signals),
        "arxiv_due": arxiv_due,
        "historical_weekly_dependency": historical_weekly_dependency,
        "source_packet_refs": packet_refs,
        "validator_error_count": len(validation_errors),
        "validator_errors": validation_errors,
        "readiness_issues": issues,
        "next_action": next_recovery_action(issues),
        "readiness_status": "ready_for_fresh_context_reaudit" if not issues else "reopen_required",
        "fresh_context_reaudit": "pending",
    }


def _month_key(row: Mapping[str, object]) -> str:
    return str(row.get("date", ""))[:7]


def _display_output_path(output: Path, root: Path) -> str:
    try:
        return output.relative_to(root).as_posix()
    except ValueError:
        return output.as_posix()


def render_summary(rows: Sequence[Mapping[str, object]], generated_at: str) -> str:
    months: Dict[str, List[Mapping[str, object]]] = {}
    issue_counts: Dict[str, int] = {}
    for row in rows:
        months.setdefault(_month_key(row), []).append(row)
        for issue in row["readiness_issues"]:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
    lines = [
        "# Daily Latest-Contract Audit Ledger",
        "",
        f"- Audit version: `{AUDIT_VERSION}`",
        f"- Generated at: `{generated_at}`",
        f"- Formal Daily reports: **{len(rows)}**",
        "- Semantic rule: readiness is not acceptance; every row remains `fresh_context_reaudit=pending` until a new independent review closes it.",
        "",
        "## Month Summary",
        "",
        "| Month | Reports | Candidates | Integrate | Machine-ready | Reopen required | Pending / Conditional Families |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for month, items in sorted(months.items()):
        lines.append(
            "| {month} | {reports} | {candidates} | {integrate} | {ready} | {reopen} | {pending} |".format(
                month=month,
                reports=len(items),
                candidates=sum(int(item["candidate_count"]) for item in items),
                integrate=sum(int(item["integrate_count"]) for item in items),
                ready=sum(item["readiness_status"] == "ready_for_fresh_context_reaudit" for item in items),
                reopen=sum(item["readiness_status"] == "reopen_required" for item in items),
                pending=sum(int(item["pending_or_conditional_count"]) for item in items),
            )
        )
    lines.extend([
        "",
        "## Reopen Reasons",
        "",
        "| Reason | Reports | Meaning |",
        "| --- | ---: | --- |",
    ])
    meanings = {
        "arxiv_owner_date_receipt_missing": "缺少冻结的官方 announcement/listing 收据；Submitted:v1 或 registry timestamp 不足以证明 Daily owner。",
        "raw_inventory_missing": "缺少可复算的原始枚举或 snapshot。",
        "per_identity_closure_missing": "没有为分母外 identity 保存逐项、family-specific closure。",
        "screening_ledger_missing": "缺少全量 title+abstract screening ledger。",
        "source_packet_missing": "对应来源包不存在，或只剩 0 字节空壳。",
        "historical_daily_weekly_dependency": "Historical Daily 仍显式依赖旧 Weekly discovery/review。",
        "candidate_review_count_mismatch": "Candidate 与 Review Completion 数量不一致。",
        "embedded_semantic_audit_not_passed": "报告内至少一个 Semantic Audit scope 未通过。",
        "report_interface_invalid": "V2.1 机器接口或跨字段约束不成立。",
    }
    for issue, count in sorted(issue_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{issue}` | {count} | {meanings.get(issue, '需要人工复核。')} |")
    action_counts: Dict[str, int] = {}
    for row in rows:
        action = str(row["next_action"])
        action_counts[action] = action_counts.get(action, 0) + 1
    lines.extend([
        "",
        "## Next Executable Checkpoint",
        "",
        "| Action | Reports |",
        "| --- | ---: |",
    ])
    for action, count in sorted(action_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{action}` | {count} |")
    lines.extend([
        "",
        "## Report Ledger",
        "",
        "| Date | Candidates / Reviews | Integrate | Packet Files (non-empty / empty) | Inventory | Screening | Closures | Interface | Readiness | Next Action | Semantic Reaudit | Issues |",
        "| --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    for row in rows:
        signals = row["source_packet_signals"]
        issues = ", ".join(row["readiness_issues"]) or "—"
        lines.append(
            f"| {row['date']} | {row['candidate_count']} / {row['review_count']} | {row['integrate_count']} | "
            f"{signals['nonempty_file_count']} / {signals['empty_file_count']} | {'yes' if signals['raw_inventory'] else 'no'} | "
            f"{'yes' if signals['screening_ledger'] else 'no'} | {'yes' if signals['per_identity_closures'] else 'no'} | "
            f"{'pass' if row['validator_error_count'] == 0 else 'fail'} | {row['readiness_status']} | {row['next_action']} | pending | {issues} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "- `ready_for_fresh_context_reaudit` 只表示现有报告和证据包足以进入新的独立语义复核，不表示语义已再次验收。",
        "- `reopen_required` 表示至少一个 Coverage / denominator / report interface 机械前置条件缺失。",
        "- 文件路径存在但大小为 0 时不构成 Receipt、Ledger 或 Primary Material；它只说明曾有恢复目标。",
        "- 详细 validator findings、证据包路径和逐日报表位于同目录 `ledger.json`。",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    registry, registry_errors = validator.validate_registry_text(
        (root / "docs/RESEARCH_SOURCES.md").read_text(encoding="utf-8")
    )
    stable_nodes, roadmap_errors = validator.parse_stable_node_ids(
        (root / "ROADMAP.md").read_text(encoding="utf-8")
    )
    if registry_errors or roadmap_errors:
        for error in registry_errors + roadmap_errors:
            print(error)
        return 2

    rows = [audit_report(root, report, registry, stable_nodes) for report in discover_daily_reports(root)]
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    output = args.output or root / "papers/_sources/daily-latest-contract-audit-20260903"
    if not output.is_absolute():
        output = root / output
    output.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": AUDIT_VERSION,
        "generated_at": generated_at,
        "semantic_acceptance_policy": "readiness_does_not_imply_acceptance",
        "reports": rows,
    }
    (output / "ledger.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (output / "README.md").write_text(render_summary(rows, generated_at), encoding="utf-8")
    output_display = _display_output_path(output, root)
    print(
        json.dumps(
            {
                "reports": len(rows),
                "ready": sum(row["readiness_status"] == "ready_for_fresh_context_reaudit" for row in rows),
                "reopen": sum(row["readiness_status"] == "reopen_required" for row in rows),
                "output": output_display,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
