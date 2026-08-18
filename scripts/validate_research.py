#!/usr/bin/env python3
"""Validate versioned research contracts and their Markdown integrity.

Legacy Score V1 reports remain compatible. New V2 reports additionally expose
small machine-readable tables whose meaning is owned by the shared contracts.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple
from urllib.parse import unquote


REGISTRY_MARKER = "<!-- validator:source-registry-v1 -->"
REGISTRY_END_MARKER = "<!-- validator:source-registry-end -->"
METADATA_MARKER = "<!-- validator:report-metadata-v2 -->"
SOURCE_COVERAGE_V1_MARKER = "<!-- validator:source-coverage-v1 -->"
CANDIDATE_LEDGER_V2_MARKER = "<!-- validator:candidate-ledger-v2 -->"
SOURCE_COVERAGE_MARKER = "<!-- validator:source-coverage-v2 -->"
CANDIDATE_LEDGER_MARKER = "<!-- validator:candidate-ledger-v2.1 -->"
REVIEW_COMPLETION_MARKER = "<!-- validator:review-completion-v1 -->"
DEEP_ANALYSIS_SELECTION_MARKER = "<!-- validator:deep-analysis-selection-v1 -->"
BOOKS_COMPARISON_MARKER = "<!-- validator:books-comparison-v1 -->"
SEMANTIC_AUDIT_MARKER = "<!-- validator:semantic-audit-v1 -->"
BENCHMARK_MARKER = "<!-- validator:benchmark-contract-v1 -->"
MATERIALS_REQUEST_MARKER = "<!-- validator:materials-request-v1 -->"

REGISTRY_COLUMNS = [
    "Source ID",
    "Source Group",
    "Authority Role",
    "Cadence",
    "Official Endpoints",
    "Event Trigger / Topic Filter",
    "Date Semantics",
    "Pagination / Cursor",
    "Expected Coverage Receipt",
    "Allowed Claim Scope",
    "Fallback",
    "Effective Date",
    "Aliases",
]

METADATA_COLUMNS = ["Field", "Value"]
SOURCE_COVERAGE_COLUMNS = [
    "Source ID",
    "Window Start",
    "Window End",
    "Executed At",
    "Endpoint / Filter",
    "Result",
    "Hits",
    "Candidate Source Families",
    "Pagination / Cursor",
    "Window Watermark",
    "Closure Evidence",
    "Gap / Limitation ID",
]
SOURCE_COVERAGE_V1_COLUMNS = [
    "Source ID",
    "Endpoint / Filter",
    "Result",
    "Hits",
    "Candidate Source Families",
    "Pagination / Cursor",
    "Gap / Limitation ID",
]
CANDIDATE_COLUMNS = [
    "Source Family ID",
    "Primary Identifier",
    "Event Identity",
    "Owner Week",
    "First-public Date",
    "Supporting Source IDs",
    "Design Delta",
    "System Reach",
    "Durability",
    "Total",
    "Candidate State",
    "Review Status",
    "Access Status",
    "Review Override",
    "Review Ref",
    "Owner Report Ref",
    "Prior Review Ref",
    "Reconciliation",
    "Stable Node ID",
    "Books Disposition",
    "Books Review Ref",
    "Benchmark Claim",
]
CANDIDATE_V2_COLUMNS = [
    column
    for column in CANDIDATE_COLUMNS
    if column not in {"Owner Report Ref", "Prior Review Ref", "Reconciliation"}
]
REVIEW_COMPLETION_COLUMNS = [
    "Source Family ID",
    "Review Provenance ID",
    "Review Route",
    "Primary Evidence Version",
    "Reviewed Evidence Versions",
    "Method / Identity Locators",
    "Evaluation Locators",
    "Limitations / Counterevidence Locators",
    "Artifact Locators",
    "Claim Boundary Ref",
    "Completion Result",
]
DEEP_ANALYSIS_SELECTION_COLUMNS = [
    "Source Family ID",
    "Eligibility",
    "Decision",
    "Analysis Unit ID",
    "Subsumed By",
    "Priority Rationale",
    "Narrative Ref",
]
BOOKS_COMPARISON_COLUMNS = [
    "Source Family ID",
    "Stable Node ID",
    "Target Chapter Ref",
    "Adjacent Chapter Refs",
    "Existing Proposition",
    "New Evidence Delta",
    "Evolution Relation",
    "Decision",
    "Books Review Ref",
]
SEMANTIC_AUDIT_COLUMNS = [
    "Audit ID",
    "Auditor",
    "Scope",
    "Reviewed Refs",
    "Findings",
    "Resolution",
    "Status",
]
BENCHMARK_COLUMNS = [
    "Source Family ID",
    "Workload",
    "Model",
    "Hardware",
    "Precision",
    "Input Length",
    "Output Length",
    "Batch",
    "Concurrency",
    "SLO",
    "Evaluator",
]
MATERIALS_REQUEST_COLUMNS = [
    "Request ID",
    "Priority",
    "Source Family ID",
    "Source ID",
    "Gap / Limitation ID",
    "Owner Week",
    "Known Identifiers / URLs",
    "Missing Material",
    "Why Existing Evidence Is Insufficient",
    "Acceptable Substitute",
    "Suggested File Name",
    "Required Review Scope",
]

AUTHORITY_ROLES = {
    "Creator Primary",
    "Primary Manuscript",
    "Independent Evaluator",
    "Review Authority",
    "Formal Publisher",
    "Benchmark / Standard Owner",
    "Artifact Provenance",
    "Analytical Dataset",
    "Discovery / Metadata",
}
CADENCES = {
    "Required Daily",
    "Required Weekly",
    "Periodic / Venue Season",
    "Event Trigger",
    "Discovery / Recovery Backstop",
}
REPORT_TYPES = {"Daily", "Sunday Weekly", "Historical Weekly"}
SOURCE_RESULTS = {"checked", "no_hit", "incomplete", "failed", "not_due"}
COVERAGE_MODES = {"Full Replay", "Delta Audit"}
CANDIDATE_STATES = {
    "retained",
    "closure_only",
    "revision",
    "duplicate",
    "spillback",
    "out_of_scope",
}
REVIEW_STATUSES = {
    "deep_complete",
    "standard_complete",
    "closure_complete",
    "pending",
    "blocked",
    "not_required",
}
ACCESS_STATUSES = {"accessible", "partial", "blocked", "unverified", "disputed"}
REVIEW_OVERRIDES = {
    "none",
    "correction",
    "release_security_contract",
    "books_conflict",
    "knowledge_gap",
    "important_revision",
}
BOOKS_DISPOSITIONS = {
    "Integrate",
    "No Change — Existing Coverage",
    "Structural Candidate",
    "Weekly Only — Context",
    "Version Fact / Mechanism Not Disclosed",
    "Blocked / Unverified",
    "Disputed",
    "Rejected — Low Durability / Out of Scope",
    "Not Assessed",
}
MATERIALS_PRIORITIES = {
    "P0 Identity",
    "P1 Full Text",
    "P2 Artifact",
    "P3 Revision",
    "P4 Discovery Export",
}
EMPTY_VALUES = {"", "-", "—", "n/a", "N/A"}
ABSENT_VALUES = EMPTY_VALUES | {"Not Applicable"}

RECONCILIATIONS = {
    "new_in_window",
    "earlier_owner_pending",
    "earlier_owner_written_back",
    "same_window_revision",
    "reused_unchanged",
    "spillback_reference",
    "out_of_scope",
}
REVIEW_ROUTES = {"deep", "standard", "closure", "not_required"}
REVIEW_COMPLETION_RESULTS = {"complete", "pending", "blocked", "not_required"}
ANALYSIS_ELIGIBILITY = {
    "score_7_9",
    "forced_review",
    "potential_books_delta",
    "potential_structural_gap",
    "cross_cutting_correction",
}
ANALYSIS_DECISIONS = {"selected", "subsumed", "not_selected"}
SEMANTIC_SCOPES = {"coverage", "evidence", "deep_analysis_selection", "books"}
SEMANTIC_STATUSES = {"passed", "open", "not_applicable"}
EVOLUTION_RELATIONS = {
    "Direct Evolution",
    "Layering / Dependency",
    "Principle Reuse",
    "Explanatory Analogy",
    "Alternative Branch",
}
GENERIC_COMPLETION_WORDS = {
    "checked",
    "closed",
    "complete",
    "completed",
    "done",
    "read",
    "reviewed",
    "verified",
    "已检查",
    "已完成",
    "已阅读",
    "已验证",
}


class RegistryRecords(dict):
    """Registry rows plus the declared registry snapshot version."""

    def __init__(self, version: Optional[date]) -> None:
        super().__init__()
        self.version = version


def _cells(line: str) -> List[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_separator(cells: Sequence[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def _table_after_marker(text: str, marker: str) -> Tuple[List[Dict[str, str]], List[str]]:
    errors: List[str] = []
    marker_count = text.count(marker)
    if marker_count != 1:
        if marker_count == 0:
            return [], [f"missing marker {marker}"]
        errors.append(f"marker {marker} must appear exactly one time; found {marker_count}")
    position = text.find(marker)
    if position < 0:
        return [], errors

    lines = text[position + len(marker) :].splitlines()
    table_start: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip().startswith("|"):
            table_start = index
            break
        if line.strip().startswith("<!-- validator:"):
            break
    if table_start is None:
        errors.append(f"marker {marker} is not followed by a Markdown table")
        return [], errors

    table_lines: List[str] = []
    for line in lines[table_start:]:
        if not line.strip().startswith("|"):
            break
        table_lines.append(line)
    if len(table_lines) < 2:
        errors.append(f"table after {marker} is missing its separator row")
        return [], errors

    headers = _cells(table_lines[0])
    separator = _cells(table_lines[1])
    if len(separator) != len(headers) or not _is_separator(separator):
        errors.append(f"table after {marker} has an invalid separator row")

    rows: List[Dict[str, str]] = []
    for number, line in enumerate(table_lines[2:], start=1):
        values = _cells(line)
        if len(values) != len(headers):
            errors.append(
                f"table after {marker} row {number} has {len(values)} cells; expected {len(headers)}"
            )
            continue
        rows.append(dict(zip(headers, values)))
    return rows, errors


def _expect_columns(text: str, marker: str, expected: Sequence[str]) -> Tuple[List[Dict[str, str]], List[str]]:
    rows, errors = _table_after_marker(text, marker)
    position = text.find(marker)
    if position >= 0:
        following = text[position + len(marker) :].splitlines()
        header = next((_cells(line) for line in following if line.strip().startswith("|")), [])
        if header and header != list(expected):
            errors.append(
                f"table after {marker} has schema {header}; expected {list(expected)}"
            )
    return rows, errors


def _split_multi(value: str) -> List[str]:
    return [
        item.strip()
        for item in re.split(r"<br\s*/?>|;", value)
        if item.strip() and item.strip() not in ABSENT_VALUES
    ]


def _html_ref_marker(value: str) -> str:
    return f"<!-- {value} -->"


def _has_evidence_body_after_marker(text: str, marker: str) -> bool:
    position = text.find(marker)
    if position < 0:
        return False
    tail = text[position + len(marker) :]
    next_marker = re.search(r"<!--\s*(?:review:|books-review:|validator:)[^>]*-->", tail)
    segment = tail[: next_marker.start()] if next_marker else tail
    for line in segment.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("<!--"):
            continue
        visible = re.sub(r"<[^>]+>", "", stripped)
        visible = re.sub(r"[`*_#>|\[\](){}~-]", "", visible).strip()
        if re.search(r"[A-Za-z0-9\u4e00-\u9fff]", visible):
            return True
    return False


def _is_reasoned_exception(value: str) -> bool:
    """Accept an explicit Not Required/Disclosed value only when it carries a reason."""
    match = re.fullmatch(
        r"(Not Required|Not Disclosed|Not Applicable|Pending)\s+[—-]\s+(.+)", value.strip()
    )
    return bool(match and match.group(2).strip().casefold() not in GENERIC_COMPLETION_WORDS)


def _is_specific_reference(value: str) -> bool:
    """Recognize a locator or stable ref by shape, never by prose length."""
    stripped = value.strip().strip("`")
    if stripped in ABSENT_VALUES or stripped.casefold() in GENERIC_COMPLETION_WORDS:
        return False
    if _is_reasoned_exception(stripped):
        return True
    return bool(
        re.search(r"https://|doi:|arxiv:|commit[:=/]|release[:=/]|#[A-Za-z0-9]|\b(?:section|table|figure|appendix|page|line)[-:= ]*[A-Za-z0-9]", stripped, re.IGNORECASE)
        or re.fullmatch(r"(?:coverage|review|claim|analysis|books-review|existing|delta|dispute):[A-Za-z0-9_.:/-]+", stripped)
        or re.fullmatch(r"sha256:[a-fA-F0-9]{32,}", stripped)
    )


def _is_source_locator(value: str) -> bool:
    stripped = value.strip().strip("`")
    if _is_reasoned_exception(stripped):
        return True
    if re.match(
        r"^(?:coverage|review|claim|analysis|books-review|existing|delta|dispute):",
        stripped,
    ):
        return False
    return _is_specific_reference(stripped)


def _is_stable_deep_facet_locator(value: str) -> bool:
    """Reject a bare paper URL plus a generic reviewer paraphrase.

    A Deep receipt must route a reviewer to a stable fragment, an explicit
    numbered section/table/appendix, an exact unique source heading, or a
    reasoned Not Disclosed/Required boundary.  Merely writing ``Method
    passages`` after the paper root is not reproducible evidence routing.
    """
    stripped = value.strip().strip("`")
    if _is_reasoned_exception(stripped):
        return True
    if re.search(r"(?:https?://|arxiv:)[^\s|<>]+#[A-Za-z0-9]", stripped, re.IGNORECASE):
        return True
    return bool(
        re.search(
            r"§|\b(?:appendix|appendices)\b|\btable\s+[A-Za-z0-9]|\bfigure\s+[A-Za-z0-9]|"
            r"\bequation\s+[A-Za-z0-9]|\bmethodology\s*:|\bexperiments\s*:|"
            r"\bscope and limitations\b",
            stripped,
            re.IGNORECASE,
        )
    )


def _bounded_segment(text: str, ref: str, label: str, errors: List[str]) -> Optional[str]:
    """Return the content of one explicit ref range; headings cannot extend it."""
    base = ref.strip().strip("`")
    if base in ABSENT_VALUES:
        errors.append(f"{label} cannot be empty")
        return None
    start = f"<!-- {base}:start -->"
    end = f"<!-- {base}:end -->"
    start_count = text.count(start)
    end_count = text.count(end)
    if start_count != 1:
        errors.append(f"{label} {base} requires exactly one start marker")
    if end_count != 1:
        errors.append(f"{label} {base} requires exactly one end marker")
    if start_count != 1 or end_count != 1:
        return None
    start_at = text.find(start)
    end_at = text.find(end)
    if end_at <= start_at:
        errors.append(f"{label} {base} end marker must follow its start marker")
        return None
    return text[start_at + len(start) : end_at]


def _expected_review_provenance(
    family: str,
    candidate: Mapping[str, str],
    route: str,
    evidence_version: str,
    reviewed_evidence_versions: str,
    method_locators: str,
    evaluation_locators: str,
    limitations_locators: str,
    artifact_locators: str,
    claim_ref: str,
    review_ref: str,
    review_body_sha256: str,
) -> str:
    def canonical_multi(value: str) -> str:
        items = []
        for raw_item in value.split(";"):
            item = unicodedata.normalize("NFC", raw_item.strip())
            if item and item not in ABSENT_VALUES:
                items.append(item)
        return ";".join(sorted(items))

    canonical = "|".join(
        (
            "review-completion-v1",
            family,
            candidate.get("Event Identity", ""),
            candidate.get("Primary Identifier", ""),
            canonical_multi(candidate.get("Supporting Source IDs", "")),
            evidence_version,
            canonical_multi(reviewed_evidence_versions),
            route,
            *(
                (f"review-override:{candidate.get('Review Override', '')}",)
                if candidate.get("Review Override") not in {None, "", "none"}
                else ()
            ),
            canonical_multi(method_locators),
            canonical_multi(evaluation_locators),
            canonical_multi(limitations_locators),
            canonical_multi(artifact_locators),
            claim_ref,
            review_ref,
            f"review-body-sha256:{review_body_sha256}",
        )
    )
    return "RP-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def _normalized_body_sha256(body: str) -> str:
    """Hash bounded review prose using the report contract's exact normalization."""
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    normalized = "\n".join(lines)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def validate_markdown_structure(text: str) -> List[str]:
    """Check heading continuity and balanced fenced code blocks."""
    errors: List[str] = []
    open_fence: Optional[Tuple[str, int, int]] = None
    previous_heading: Optional[int] = None

    for line_number, line in enumerate(text.splitlines(), start=1):
        if open_fence is None:
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if opening:
                marker = opening.group(1)
                open_fence = (marker[0], len(marker), line_number)
                continue
        else:
            closing = re.match(r"^ {0,3}(`{3,}|~{3,})[ \t]*$", line)
            if closing:
                marker = closing.group(1)
                if marker[0] == open_fence[0] and len(marker) >= open_fence[1]:
                    open_fence = None
            continue
        if open_fence is not None:
            continue

        heading_match = re.match(r"^(#{1,6})\s+\S", line)
        if not heading_match:
            continue
        level = len(heading_match.group(1))
        if previous_heading is not None and level > previous_heading + 1:
            errors.append(
                f"line {line_number}: heading level jumps from H{previous_heading} to H{level}"
            )
        previous_heading = level

    if open_fence is not None:
        errors.append(f"line {open_fence[2]}: unclosed code fence")
    return errors


def _markdown_inline_targets(text: str) -> List[str]:
    targets: List[str] = []
    cursor = 0
    while True:
        opener = text.find("](", cursor)
        if opener < 0:
            break
        line_start = text.rfind("\n", 0, opener) + 1
        if text.rfind("[", line_start, opener) < 0:
            cursor = opener + 2
            continue
        start = opener + 2
        if start < len(text) and text[start] == "<":
            end = text.find(">", start + 1)
            close = text.find(")", end + 1) if end >= 0 else -1
            if end >= 0 and close >= 0:
                targets.append(text[start : end + 1])
                cursor = close + 1
                continue
        depth = 0
        index = start
        while index < len(text):
            char = text[index]
            if char == "\\" and index + 1 < len(text):
                index += 2
                continue
            if char == "\n":
                break
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    targets.append(text[start:index])
                    index += 1
                    break
                depth -= 1
            index += 1
        cursor = max(index, opener + 2)
    return targets


def _mask_markdown_code(text: str) -> str:
    """Mask fenced and inline code while preserving offsets and line breaks."""
    characters = list(text)
    open_fence: Optional[Tuple[str, int]] = None
    offset = 0
    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        if open_fence is None:
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", content)
            if opening:
                marker = opening.group(1)
                open_fence = (marker[0], len(marker))
        else:
            closing = re.match(r"^ {0,3}(`{3,}|~{3,})[ \t]*$", content)
            if closing:
                marker = closing.group(1)
                if marker[0] == open_fence[0] and len(marker) >= open_fence[1]:
                    open_fence = None
        if open_fence is not None or re.match(r"^ {0,3}(`{3,}|~{3,})", content):
            for index in range(offset, offset + len(content)):
                characters[index] = " "
        offset += len(line)

    masked = "".join(characters)
    characters = list(masked)
    index = 0
    while index < len(masked):
        if masked[index] != "`":
            index += 1
            continue
        end_run = index
        while end_run < len(masked) and masked[end_run] == "`":
            end_run += 1
        marker = masked[index:end_run]
        search = end_run
        closing_index = -1
        while True:
            candidate = masked.find(marker, search)
            if candidate < 0:
                break
            before_is_tick = candidate > 0 and masked[candidate - 1] == "`"
            after = candidate + len(marker)
            after_is_tick = after < len(masked) and masked[after] == "`"
            if not before_is_tick and not after_is_tick:
                closing_index = candidate
                break
            search = candidate + len(marker)
        if closing_index < 0:
            index = end_run
            continue
        for position in range(index, closing_index + len(marker)):
            characters[position] = " "
        index = closing_index + len(marker)
    return "".join(characters)


def validate_local_markdown_links(text: str, document_path: Path, root: Path) -> List[str]:
    """Resolve local inline Markdown links and images relative to their document."""
    errors: List[str] = []
    root = root.resolve()
    for raw_target in _markdown_inline_targets(_mask_markdown_code(text)):
        value = raw_target.strip()
        if value.startswith("<") and ">" in value:
            target = value[1 : value.index(">")]
        else:
            target = value.split(maxsplit=1)[0]
        target = re.sub(r"\\([\\() ])", r"\1", target)
        target = unquote(target)
        if not target or target.startswith("#"):
            continue
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
            continue
        target = target.split("#", 1)[0]
        target = re.sub(r":\d+(?::\d+)?$", "", target)
        if not target:
            continue
        candidate = Path(target)
        if not candidate.is_absolute():
            candidate = document_path.parent / candidate
        candidate = candidate.resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            try:
                display = document_path.resolve().relative_to(root)
            except ValueError:
                display = document_path
            errors.append(f"{display}: local Markdown link escapes repository root {raw_target!r}")
            continue
        if not candidate.exists():
            try:
                display = document_path.resolve().relative_to(root)
            except ValueError:
                display = document_path
            errors.append(f"{display}: missing local Markdown link {raw_target!r}")
    return errors


def parse_stable_node_ids(text: str) -> Tuple[set, List[str]]:
    """Parse canonical Stable Node IDs from ROADMAP's node mapping table."""
    errors: List[str] = []
    nodes: set = set()
    rows = re.findall(
        r"^\|\s*`([A-Z][A-Z0-9-]+)`\s*\|\s*Ch\d+\s*\|\s*`books/[^`]+`\s*\|",
        text,
        flags=re.MULTILINE,
    )
    if not rows:
        errors.append("ROADMAP Stable Node mapping table contains no parseable nodes")
    for node_id in rows:
        if node_id in nodes:
            errors.append(f"duplicate Stable Node ID {node_id} in ROADMAP mapping table")
        nodes.add(node_id)
    return nodes, errors


def _extract_urls(value: str) -> List[str]:
    markdown_urls = re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", value)
    plain_urls = re.findall(r"(?<!\()https?://[^\s<]+", value)
    return markdown_urls + [url.rstrip(".,)") for url in plain_urls]


def _parse_iso_date(value: str, label: str, errors: List[str]) -> Optional[date]:
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label} must use YYYY-MM-DD: {value!r}")
        return None


def _parse_iso_datetime(value: str, label: str, errors: List[str]) -> Optional[datetime]:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        errors.append(f"{label} must use an ISO-8601 timestamp: {value!r}")
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        errors.append(f"{label} must include an explicit UTC offset: {value!r}")
        return None
    return parsed


def _registry_version(text: str, errors: List[str]) -> Optional[date]:
    matches = re.findall(r"^注册表版本：\s*(\S+)\s*$", text, flags=re.MULTILINE)
    if len(matches) != 1:
        errors.append(f"source registry must declare exactly one 注册表版本; found {len(matches)}")
        return None
    return _parse_iso_date(matches[0], "source registry version", errors)


def validate_registry_text(text: str) -> Tuple[Dict[str, Dict[str, str]], List[str]]:
    rows, errors = _expect_columns(text, REGISTRY_MARKER, REGISTRY_COLUMNS)
    registry_version = _registry_version(text, errors)
    records: Dict[str, Dict[str, str]] = RegistryRecords(registry_version)
    aliases: Dict[str, str] = {}
    endpoints: Dict[str, str] = {}

    end_count = text.count(REGISTRY_END_MARKER)
    if end_count != 1:
        errors.append(f"marker {REGISTRY_END_MARKER} must appear exactly one time; found {end_count}")
    elif text.find(REGISTRY_END_MARKER) < text.find(REGISTRY_MARKER):
        errors.append(f"marker {REGISTRY_END_MARKER} must follow {REGISTRY_MARKER}")

    for number, row in enumerate(rows, start=1):
        source_id = row.get("Source ID", "").strip("`")
        prefix = f"registry row {number}"
        if not re.fullmatch(r"[A-Z][A-Z0-9-]+", source_id):
            errors.append(f"{prefix}: invalid Source ID {source_id!r}")
        if source_id in records:
            errors.append(f"{prefix}: duplicate Source ID {source_id}")
        else:
            records[source_id] = row

        role = row.get("Authority Role", "")
        if role not in AUTHORITY_ROLES:
            errors.append(f"{prefix}: invalid Authority Role {role!r}")
        cadence = row.get("Cadence", "")
        if cadence not in CADENCES:
            errors.append(f"{prefix}: invalid Cadence {cadence!r}")
        if cadence in {"Periodic / Venue Season", "Event Trigger", "Discovery / Recovery Backstop"}:
            trigger = row.get("Event Trigger / Topic Filter", "")
            if trigger in ABSENT_VALUES:
                errors.append(f"{prefix}: cadence {cadence} requires a trigger or filter")

        urls = _extract_urls(row.get("Official Endpoints", ""))
        if not urls:
            errors.append(f"{prefix}: Official Endpoints must contain at least one HTTPS URL")
        for endpoint in urls:
            if not endpoint.startswith("https://"):
                errors.append(f"{prefix}: Official Endpoint must use HTTPS: {endpoint}")
            if endpoint in endpoints and endpoints[endpoint] != source_id:
                errors.append(
                    f"{prefix}: duplicate Official Endpoint {endpoint} also belongs to {endpoints[endpoint]}"
                )
            endpoints[endpoint] = source_id

        effective = row.get("Effective Date", "")
        effective_date = _parse_iso_date(effective, f"{prefix} Effective Date", errors)
        if effective_date and registry_version and effective_date > registry_version:
            errors.append(
                f"{prefix}: Effective Date {effective} cannot be later than registry version {registry_version.isoformat()}"
            )
        for alias in _split_multi(row.get("Aliases", "")):
            key = alias.casefold()
            if key in aliases:
                errors.append(
                    f"{prefix}: duplicate alias {alias!r}; already belongs to {aliases[key]}"
                )
            else:
                aliases[key] = source_id

        for required in REGISTRY_COLUMNS:
            if row.get(required, "") in ABSENT_VALUES and required not in {"Aliases", "Fallback"}:
                errors.append(f"{prefix}: {required} cannot be empty")

    fallback_graph: Dict[str, List[str]] = {source_id: [] for source_id in records}
    for number, row in enumerate(rows, start=1):
        source_id = row.get("Source ID", "").strip("`")
        for fallback in _split_multi(row.get("Fallback", "")):
            fallback_id = fallback.strip("`")
            if not re.fullmatch(r"[A-Z][A-Z0-9-]+", fallback_id):
                errors.append(f"registry row {number}: invalid Fallback Source ID {fallback_id!r}")
                continue
            if fallback_id not in records:
                errors.append(f"registry row {number}: unknown Fallback Source ID {fallback_id}")
            elif source_id in fallback_graph:
                fallback_graph[source_id].append(fallback_id)

    states: Dict[str, int] = {}
    stack: List[str] = []
    reported_cycles: set = set()

    def visit(source_id: str) -> None:
        states[source_id] = 1
        stack.append(source_id)
        for fallback_id in fallback_graph.get(source_id, []):
            if states.get(fallback_id, 0) == 0:
                visit(fallback_id)
            elif states.get(fallback_id) == 1:
                start = stack.index(fallback_id)
                cycle = tuple(stack[start:] + [fallback_id])
                signature = frozenset(cycle)
                if signature not in reported_cycles:
                    reported_cycles.add(signature)
                    errors.append("Fallback cycle: " + " -> ".join(cycle))
        stack.pop()
        states[source_id] = 2

    for source_id in fallback_graph:
        if states.get(source_id, 0) == 0:
            visit(source_id)
    return records, errors


def _metadata(rows: Sequence[Mapping[str, str]], errors: List[str]) -> Dict[str, str]:
    values: Dict[str, str] = {}
    for row in rows:
        key = row.get("Field", "")
        value = row.get("Value", "")
        if key in values:
            errors.append(f"duplicate report metadata field {key!r}")
        values[key] = value
    required = {
        "Score Schema",
        "Report Type",
        "Window Start",
        "Window End",
        "Registry Version",
        "Coverage Mode",
        "Baseline Report",
        "Changed Source IDs",
        "Denominator ID",
        "Previous Denominator ID",
        "Denominator Frozen At",
        "Completion Status",
        "Coverage Gate",
        "Evidence Gate",
        "Books Gate",
    }
    for key in sorted(required - set(values)):
        errors.append(f"missing report metadata field {key}")
    for key in required & set(values):
        if key not in {
            "Baseline Report",
            "Changed Source IDs",
            "Previous Denominator ID",
        } and values[key] in (EMPTY_VALUES if key == "Books Gate" else ABSENT_VALUES):
            errors.append(f"report metadata field {key} cannot be empty")
    return values


def _validate_window(metadata: Mapping[str, str], errors: List[str]) -> None:
    report_type = metadata.get("Report Type", "")
    if report_type not in REPORT_TYPES:
        errors.append(f"invalid Report Type {report_type!r}")
    start = _parse_iso_date(metadata.get("Window Start", ""), "Window Start", errors)
    end = _parse_iso_date(metadata.get("Window End", ""), "Window End", errors)
    if not start or not end:
        return
    if report_type == "Daily" and start != end:
        errors.append("Daily Window Start and Window End must be the same natural day")
    if report_type in {"Sunday Weekly", "Historical Weekly"}:
        if start.weekday() != 0 or end.weekday() != 6 or end - start != timedelta(days=6):
            errors.append(f"{report_type} must cover one complete ISO Monday-Sunday window")


def _registry_effective_version(
    registry: Mapping[str, Mapping[str, str]],
    errors: Optional[List[str]] = None,
) -> Optional[date]:
    effective_dates: List[date] = []
    for source_id, row in registry.items():
        try:
            effective_dates.append(date.fromisoformat(row.get("Effective Date", "")))
        except ValueError:
            if errors is not None:
                errors.append(
                    f"registry Source ID {source_id}: Effective Date must use YYYY-MM-DD: "
                    f"{row.get('Effective Date', '')!r}"
                )
            continue
    declared_version = getattr(registry, "version", None)
    if isinstance(declared_version, date):
        return declared_version
    return max(effective_dates) if effective_dates else None


def _due_source_ids(
    report_type: str,
    registry: Mapping[str, Mapping[str, str]],
    applicable_through: Optional[date],
) -> set:
    due = {"Required Daily"}
    if report_type in {"Sunday Weekly", "Historical Weekly"}:
        due.add("Required Weekly")
    source_ids = set()
    for source_id, row in registry.items():
        if row.get("Cadence") not in due:
            continue
        try:
            effective_date = date.fromisoformat(row.get("Effective Date", ""))
        except ValueError:
            continue
        if applicable_through is None or effective_date <= applicable_through:
            source_ids.add(source_id)
    return source_ids


def _int(value: str, label: str, errors: List[str]) -> Optional[int]:
    try:
        return int(value)
    except ValueError:
        errors.append(f"{label} must be an integer: {value!r}")
        return None


def _validate_benchmarks(
    text: str,
    claims: Mapping[str, bool],
    errors: List[str],
) -> None:
    claimed = {family for family, is_claimed in claims.items() if is_claimed}
    if BENCHMARK_MARKER not in text:
        for family in sorted(claimed):
            errors.append(f"benchmark claim {family} is missing from {BENCHMARK_MARKER}")
        return
    rows, table_errors = _expect_columns(text, BENCHMARK_MARKER, BENCHMARK_COLUMNS)
    errors.extend(table_errors)
    by_family: Dict[str, Mapping[str, str]] = {}
    for row in rows:
        family = row.get("Source Family ID", "")
        if family in ABSENT_VALUES:
            errors.append("benchmark contract Source Family ID cannot be empty")
        if family in by_family:
            errors.append(f"duplicate benchmark contract for {family}")
        by_family[family] = row
        for column in BENCHMARK_COLUMNS[1:]:
            if row.get(column, "") in ABSENT_VALUES:
                errors.append(f"benchmark contract {family}: {column} cannot be empty; use Not Disclosed")
        if family not in claims:
            errors.append(f"benchmark contract {family} has no Candidate Ledger row")
        elif not claims[family]:
            errors.append(f"benchmark contract {family} requires Benchmark Claim yes")
    for family in sorted(claimed):
        if family not in by_family:
            errors.append(f"benchmark claim {family} is missing from {BENCHMARK_MARKER}")


def _validate_materials_requests(
    text: str,
    candidate_access: Mapping[str, Tuple[str, str]],
    source_failures: Mapping[Tuple[str, str], str],
    errors: List[str],
) -> None:
    required_families = {
        family
        for family, (access, _) in candidate_access.items()
        if access in {"blocked", "unverified"}
    }
    if MATERIALS_REQUEST_MARKER not in text:
        for family in sorted(required_families):
            errors.append(f"candidate {family}: blocked or unverified evidence requires a Materials Request")
        for source_id, gap_id in sorted(source_failures):
            errors.append(
                f"failed source {source_id} / {gap_id} requires a Materials Request"
            )
        return

    rows, table_errors = _expect_columns(text, MATERIALS_REQUEST_MARKER, MATERIALS_REQUEST_COLUMNS)
    errors.extend(table_errors)
    request_ids: set = set()
    family_counts: Dict[str, int] = {}
    source_counts: Dict[Tuple[str, str], int] = {}
    for number, row in enumerate(rows, start=1):
        request_id = row.get("Request ID", "").strip("`")
        family = row.get("Source Family ID", "").strip("`")
        source_id = row.get("Source ID", "").strip("`")
        gap_id = row.get("Gap / Limitation ID", "").strip("`")
        prefix = f"materials request row {number}"
        if request_id in ABSENT_VALUES or not request_id.startswith("MR-"):
            errors.append(f"{prefix}: Request ID must be a non-empty MR-* identity")
        elif request_id in request_ids:
            errors.append(f"{prefix}: duplicate Request ID {request_id}")
        request_ids.add(request_id)

        priority = row.get("Priority", "").strip("`")
        if priority not in MATERIALS_PRIORITIES:
            errors.append(f"{prefix}: invalid Priority {priority!r}")
        for column in MATERIALS_REQUEST_COLUMNS[5:]:
            if row.get(column, "").strip("`") in ABSENT_VALUES:
                errors.append(f"{prefix}: {column} cannot be empty")

        has_family = family not in ABSENT_VALUES
        has_source = source_id not in ABSENT_VALUES
        has_gap = gap_id not in ABSENT_VALUES
        if has_family and not has_source and not has_gap:
            family_counts[family] = family_counts.get(family, 0) + 1
            candidate = candidate_access.get(family)
            if candidate is None or candidate[0] not in {"blocked", "unverified", "disputed"}:
                errors.append(
                    f"{prefix}: Source Family ID {family} does not map to blocked, unverified or disputed evidence"
                )
            elif row.get("Owner Week", "").strip("`") != candidate[1]:
                errors.append(f"{prefix}: Owner Week does not match candidate {family}")
        elif not has_family and has_source and has_gap:
            source_key = (source_id, gap_id)
            source_counts[source_key] = source_counts.get(source_key, 0) + 1
            expected_owner = source_failures.get(source_key)
            if expected_owner is None:
                errors.append(
                    f"{prefix}: Source ID {source_id} / Gap {gap_id} does not map to a blocking failed source receipt"
                )
            elif row.get("Owner Week", "").strip("`") != expected_owner:
                errors.append(
                    f"{prefix}: Owner Week does not match failed source {source_id} / {gap_id}"
                )
        else:
            errors.append(
                f"{prefix}: use exactly one mapping: Source Family ID, or Source ID plus Gap / Limitation ID"
            )

    for family in sorted(required_families):
        count = family_counts.get(family, 0)
        if count != 1:
            errors.append(f"candidate {family}: blocked or unverified evidence requires exactly one Materials Request")
    for family, count in sorted(family_counts.items()):
        if count > 1:
            errors.append(f"Source Family ID {family} has duplicate Materials Request rows")
    for source_key in sorted(source_failures):
        count = source_counts.get(source_key, 0)
        if count != 1:
            errors.append(
                f"failed source {source_key[0]} / {source_key[1]} requires exactly one Materials Request"
            )
    for (source_id, gap_id), count in sorted(source_counts.items()):
        if count > 1:
            errors.append(
                f"Source ID {source_id} / Gap {gap_id} has duplicate Materials Request rows"
            )


def _is_specific_statement(value: str) -> bool:
    stripped = value.strip().strip("`")
    return stripped not in ABSENT_VALUES and stripped.casefold() not in GENERIC_COMPLETION_WORDS


def _required_review_route(row: Mapping[str, str]) -> str:
    if row.get("Review Override") != "none":
        return "deep"
    if row.get("Candidate State") not in {"retained", "closure_only"}:
        return "not_required"
    try:
        total = int(row.get("Total", ""))
    except ValueError:
        return "not_required"
    if total >= 7:
        return "deep"
    if total >= 5:
        return "standard"
    return "closure"


def _validate_v21_completion_interfaces(
    text: str,
    metadata: Mapping[str, str],
    candidates: Mapping[str, Mapping[str, str]],
    stable_node_ids: Optional[set],
    errors: List[str],
) -> None:
    review_rows, table_errors = _expect_columns(
        text, REVIEW_COMPLETION_MARKER, REVIEW_COMPLETION_COLUMNS
    )
    errors.extend(table_errors)
    analysis_rows, table_errors = _expect_columns(
        text, DEEP_ANALYSIS_SELECTION_MARKER, DEEP_ANALYSIS_SELECTION_COLUMNS
    )
    errors.extend(table_errors)
    books_rows, table_errors = _expect_columns(
        text, BOOKS_COMPARISON_MARKER, BOOKS_COMPARISON_COLUMNS
    )
    errors.extend(table_errors)
    audit_rows, table_errors = _expect_columns(
        text, SEMANTIC_AUDIT_MARKER, SEMANTIC_AUDIT_COLUMNS
    )
    errors.extend(table_errors)

    review_by_family: Dict[str, Mapping[str, str]] = {}
    seen_provenance: Dict[str, str] = {}
    for number, receipt in enumerate(review_rows, start=1):
        family = receipt.get("Source Family ID", "").strip("`")
        prefix = f"Review Completion row {number}"
        if family in ABSENT_VALUES:
            errors.append(f"{prefix}: Source Family ID cannot be empty")
            continue
        if family in review_by_family:
            errors.append(f"{prefix}: duplicate Source Family ID {family}")
        review_by_family[family] = receipt
        candidate = candidates.get(family)
        if candidate is None:
            errors.append(f"{prefix}: unknown Source Family ID {family}")
            continue
        route = receipt.get("Review Route", "")
        result = receipt.get("Completion Result", "")
        if route not in REVIEW_ROUTES:
            errors.append(f"{prefix}: invalid Review Route {route!r}")
        expected_route = _required_review_route(candidate)
        if route != expected_route:
            errors.append(
                f"{prefix}: Review Route {route!r} does not match required route {expected_route!r}"
            )
        if result not in REVIEW_COMPLETION_RESULTS:
            errors.append(f"{prefix}: invalid Completion Result {result!r}")
        review_status = candidate.get("Review Status", "")
        expected_status = {
            ("deep", "complete"): "deep_complete",
            ("standard", "complete"): "standard_complete",
            ("closure", "complete"): "closure_complete",
            ("not_required", "not_required"): "not_required",
        }.get((route, result))
        if result == "blocked":
            expected_status = "blocked"
        if result == "pending":
            expected_status = "pending"
        if expected_status and review_status != expected_status:
            errors.append(
                f"{prefix}: Completion Result {result!r} and route {route!r} "
                f"require Review Status {expected_status!r}"
            )

        evidence_version = receipt.get("Primary Evidence Version", "").strip("`")
        reviewed_versions_value = receipt.get("Reviewed Evidence Versions", "").strip("`")
        reviewed_versions = _split_multi(reviewed_versions_value)
        if re.match(r"^[A-Z][A-Z0-9-]+@", evidence_version):
            errors.append(
                f"{prefix}: Primary Evidence Version must contain the exact version only, "
                "without a Source ID prefix"
            )
        if result == "pending":
            if not _is_reasoned_exception(evidence_version) and not _is_source_locator(evidence_version):
                errors.append(
                    f"{prefix}: pending Primary Evidence Version must identify known evidence "
                    "or the concrete unfinished scope"
                )
        elif route != "not_required" and result != "blocked":
            if not _is_source_locator(evidence_version) or not re.search(r"\d", evidence_version):
                errors.append(f"{prefix}: Primary Evidence Version must identify a versioned source")
        elif route == "not_required" and not _is_reasoned_exception(evidence_version):
            errors.append(f"{prefix}: not_required route needs a reasoned Primary Evidence Version")

        if result == "complete":
            if not reviewed_versions:
                errors.append(f"{prefix}: Reviewed Evidence Versions cannot be empty for a completed review")
            elif len(reviewed_versions) != len(set(reviewed_versions)):
                errors.append(f"{prefix}: Reviewed Evidence Versions must be unique")
            for version in reviewed_versions:
                if (
                    not re.match(r"^[A-Z][A-Z0-9-]+@.+", version)
                    or not _is_source_locator(version)
                    or not re.search(r"\d", version)
                ):
                    errors.append(
                        f"{prefix}: Reviewed Evidence Versions must use "
                        "Source ID@concrete versioned evidence"
                    )
            matching_reviewed_versions = [
                version
                for version in reviewed_versions
                if version == evidence_version
                or ("@" in version and version.split("@", 1)[1] == evidence_version)
            ]
            if len(matching_reviewed_versions) != 1:
                errors.append(
                    f"{prefix}: Reviewed Evidence Versions must include exactly one "
                    "Source ID entry whose version part matches Primary Evidence Version"
                )
        elif result in {"pending", "blocked"}:
            if not reviewed_versions and not _is_reasoned_exception(reviewed_versions_value):
                errors.append(
                    f"{prefix}: {result} Reviewed Evidence Versions must list known versions "
                    "or the concrete unfinished boundary"
                )
        elif result == "not_required" and not _is_reasoned_exception(reviewed_versions_value):
            errors.append(
                f"{prefix}: not_required Reviewed Evidence Versions needs an explicit reason"
            )

        facet_columns = {
            "Method / Identity Locators": route in {"deep", "standard", "closure"},
            "Evaluation Locators": route in {"deep", "standard"},
            "Limitations / Counterevidence Locators": route in {"deep", "standard"},
            "Artifact Locators": route == "deep",
        }
        for column, required in facet_columns.items():
            value = receipt.get(column, "").strip("`")
            if result in {"blocked", "pending"}:
                if not _is_source_locator(value):
                    errors.append(
                        f"{prefix}: {result} receipt must record a locator or reasoned boundary for {column}"
                    )
            elif required:
                if not _is_source_locator(value):
                    errors.append(f"{prefix}: {column} requires a source locator or a reasoned exception")
            elif not _is_source_locator(value):
                errors.append(f"{prefix}: {column} must use a source locator or reasoned Not Required value")
            if (
                route == "deep"
                and result == "complete"
                and column != "Artifact Locators"
                and not _is_stable_deep_facet_locator(value)
            ):
                errors.append(
                    f"{prefix}: {column} for a completed Deep review must identify a stable "
                    "fragment, numbered section/table/appendix, exact unique heading, or reasoned exception"
                )

        if route == "deep" and result == "complete":
            concrete_facets = [
                receipt.get(column, "").strip("`")
                for column in facet_columns
                if not _is_reasoned_exception(receipt.get(column, "").strip("`"))
            ]
            if len(concrete_facets) != len(set(concrete_facets)):
                errors.append(
                    f"{prefix}: deep review facets cannot borrow one locator for distinct evidence claims"
                )

        claim_ref = receipt.get("Claim Boundary Ref", "").strip("`")
        review_ref = candidate.get("Review Ref", "").strip("`")
        if result != "pending" and claim_ref != f"claim:{family}":
            errors.append(f"{prefix}: Claim Boundary Ref must equal claim:{family}")
        if result == "pending" and not (
            claim_ref == f"claim:{family}" or _is_reasoned_exception(claim_ref)
        ):
            errors.append(
                f"{prefix}: pending Claim Boundary Ref must be bounded or state a concrete pending reason"
            )
        if result == "complete" and review_ref != f"review:{family}":
            errors.append(f"candidate {family}: Review Ref must equal review:{family}")
        review_segment: Optional[str] = None
        review_body_sha256 = ""
        if result != "pending":
            review_segment = _bounded_segment(
                text, review_ref, f"candidate {family} Review Ref", errors
            )
            if review_segment is not None:
                review_body_sha256 = _normalized_body_sha256(review_segment)

        provenance = receipt.get("Review Provenance ID", "").strip("`")
        if result == "pending":
            if provenance not in ABSENT_VALUES:
                errors.append(f"{prefix}: pending Review Provenance ID must be —")
        else:
            expected_provenance = _expected_review_provenance(
                family,
                candidate,
                route,
                evidence_version,
                reviewed_versions_value,
                receipt.get("Method / Identity Locators", "").strip("`"),
                receipt.get("Evaluation Locators", "").strip("`"),
                receipt.get("Limitations / Counterevidence Locators", "").strip("`"),
                receipt.get("Artifact Locators", "").strip("`"),
                claim_ref,
                review_ref,
                review_body_sha256,
            )
            if provenance != expected_provenance:
                errors.append(
                    f"{prefix}: Review Provenance ID {provenance!r} does not match "
                    f"recomputed {expected_provenance!r}"
                )
            previous = seen_provenance.get(provenance)
            if previous and previous != family:
                errors.append(f"Review Provenance ID {provenance} is reused across {previous} and {family}")
            seen_provenance[provenance] = family
        if result == "complete":
            claim_segment = _bounded_segment(text, claim_ref, f"{prefix} Claim Boundary Ref", errors)
            if claim_segment is not None and review_segment is not None:
                claim_start = text.find(f"<!-- {claim_ref}:start -->")
                claim_end = text.find(f"<!-- {claim_ref}:end -->")
                review_start = text.find(f"<!-- {review_ref}:start -->")
                review_end = text.find(f"<!-- {review_ref}:end -->")
                if not (review_start < claim_start < claim_end < review_end):
                    errors.append(f"{prefix}: Claim Boundary Ref must be contained by Review Ref")

    for family, candidate in candidates.items():
        status = candidate.get("Review Status", "")
        receipt = review_by_family.get(family)
        if status in {"deep_complete", "standard_complete", "closure_complete", "blocked", "not_required"}:
            if receipt is None:
                errors.append(f"candidate {family}: Review Completion receipt is required for status {status}")
        elif status == "pending" and receipt is None:
            errors.append(f"candidate {family}: pending review requires a pending Review Completion receipt")

    eligible: Dict[str, set] = {}
    allowed_eligibility: Dict[str, set] = {}
    for family, candidate in candidates.items():
        facts: set = set()
        try:
            if int(candidate.get("Total", "")) >= 7:
                facts.add("score_7_9")
        except ValueError:
            pass
        if candidate.get("Review Override") != "none":
            facts.add("forced_review")
        if candidate.get("Review Override") == "correction":
            facts.add("cross_cutting_correction")
        stable_node = candidate.get("Stable Node ID", "").strip("`")
        allowed = set(facts)
        if candidate.get("Candidate State") in {"retained", "closure_only"}:
            if stable_node in ABSENT_VALUES:
                allowed.add("potential_structural_gap")
            else:
                allowed.add("potential_books_delta")
        allowed_eligibility[family] = allowed
        if facts:
            eligible[family] = facts

    covered_eligible: Dict[str, str] = {}
    selected_eligibility: Dict[str, set] = {}
    selected_units: set = set()
    subsumed_targets: List[Tuple[str, str, str]] = []
    for number, row in enumerate(analysis_rows, start=1):
        family = row.get("Source Family ID", "").strip("`")
        unit = row.get("Analysis Unit ID", "").strip("`")
        prefix = f"Deep Analysis Selection row {number}"
        if family in ABSENT_VALUES:
            errors.append(f"{prefix}: Source Family ID cannot be empty")
        elif family in covered_eligible:
            errors.append(f"{prefix}: duplicate Source Family ID {family}")
        else:
            covered_eligible[family] = unit
        candidate = candidates.get(family)
        if candidate is None:
            errors.append(f"{prefix}: unknown Source Family ID {family}")
        eligibility = set(_split_multi(row.get("Eligibility", "")))
        selected_eligibility[family] = eligibility
        unknown_eligibility = eligibility - ANALYSIS_ELIGIBILITY
        if unknown_eligibility:
            errors.append(f"{prefix}: invalid Eligibility {sorted(unknown_eligibility)}")
        declared_prebooks = eligibility & {"potential_books_delta", "potential_structural_gap"}
        required = eligible.get(family, set()) | declared_prebooks
        if declared_prebooks:
            eligible[family] = required
        if candidate is not None and not required:
            errors.append(f"{prefix}: Source Family ID {family} is not pre-Books eligible")
        missing_basis = required - eligibility
        if missing_basis:
            errors.append(
                f"{prefix}: eligibility for {family} must include {', '.join(sorted(missing_basis))}"
            )
        unsupported_basis = eligibility - allowed_eligibility.get(family, required)
        if unsupported_basis:
            errors.append(
                f"{prefix}: eligibility for {family} is unsupported by Candidate Ledger facts: "
                f"{', '.join(sorted(unsupported_basis))}"
            )
        decision = row.get("Decision", "")
        if decision not in ANALYSIS_DECISIONS:
            errors.append(f"{prefix}: invalid Decision {decision!r}")
        subsumed_by = row.get("Subsumed By", "").strip("`")
        if decision == "selected":
            if unit in ABSENT_VALUES:
                errors.append(f"{prefix}: selected row requires a non-empty Analysis Unit ID")
            selected_units.add(unit)
            if subsumed_by not in ABSENT_VALUES:
                errors.append(f"{prefix}: selected row must not set Subsumed By")
        elif decision == "subsumed":
            if unit not in ABSENT_VALUES:
                errors.append(f"{prefix}: subsumed row must set Analysis Unit ID to —")
            if subsumed_by in ABSENT_VALUES:
                errors.append(f"{prefix}: subsumed row requires Subsumed By")
            else:
                subsumed_targets.append((prefix, family, subsumed_by))
        elif decision == "not_selected":
            if unit not in ABSENT_VALUES:
                errors.append(f"{prefix}: not_selected row must set Analysis Unit ID to —")
            if subsumed_by not in ABSENT_VALUES:
                errors.append(f"{prefix}: not_selected row must not set Subsumed By")
        rationale = row.get("Priority Rationale", "")
        if not _is_specific_statement(rationale):
            errors.append(f"{prefix}: Priority Rationale must state a concrete selection basis")
        narrative_ref = row.get("Narrative Ref", "").strip("`")
        if decision == "subsumed":
            expected_narrative_ref = f"analysis:{subsumed_by}"
        elif decision == "not_selected":
            expected_narrative_ref = f"analysis-decision:{family}"
        else:
            expected_narrative_ref = f"analysis:{unit}"
        if narrative_ref != expected_narrative_ref:
            errors.append(f"{prefix}: Narrative Ref must equal {expected_narrative_ref}")
        _bounded_segment(text, narrative_ref, f"{prefix} Narrative Ref", errors)
    for prefix, family, selected_unit in subsumed_targets:
        if selected_unit not in selected_units:
            errors.append(
                f"{prefix}: Subsumed By {selected_unit!r} must reference an existing selected unit"
            )
    for family in sorted(set(eligible) - set(covered_eligible)):
        errors.append(f"eligible family {family} is missing from Deep Analysis Selection")
    if eligible and not selected_units:
        errors.append("Deep Analysis Selection requires at least 1 selected unit when eligible families exist")
    if len(selected_units) > 3:
        errors.append("Deep Analysis Selection may select at most 3 units")

    required_books = {
        family
        for family, candidate in candidates.items()
        if candidate.get("Books Disposition")
        in {"Integrate", "No Change — Existing Coverage", "Structural Candidate"}
    }
    books_by_family: Dict[str, Mapping[str, str]] = {}
    for number, row in enumerate(books_rows, start=1):
        family = row.get("Source Family ID", "").strip("`")
        prefix = f"Books Comparison row {number}"
        if family in books_by_family:
            errors.append(f"{prefix}: duplicate Source Family ID {family}")
        books_by_family[family] = row
        candidate = candidates.get(family)
        if candidate is None:
            errors.append(f"{prefix}: unknown Source Family ID {family}")
            continue
        decision = row.get("Decision", "")
        if decision != candidate.get("Books Disposition"):
            errors.append(f"{prefix}: Decision must match Candidate Ledger Books Disposition")
        required_selection_fact = {
            "Integrate": "potential_books_delta",
            "Structural Candidate": "potential_structural_gap",
        }.get(decision)
        if required_selection_fact and required_selection_fact not in selected_eligibility.get(
            family, set()
        ):
            errors.append(
                f"{prefix}: {decision} requires Deep Analysis Selection Eligibility "
                f"{required_selection_fact} before the Books decision"
            )
        node = row.get("Stable Node ID", "").strip("`")
        candidate_node = candidate.get("Stable Node ID", "").strip("`")
        if decision == "Structural Candidate":
            if node in ABSENT_VALUES or "considered:" not in node.casefold():
                errors.append(f"{prefix}: Structural Candidate must list considered Stable Node owners")
        elif node != candidate_node:
            errors.append(f"{prefix}: Stable Node ID must match Candidate Ledger")
        if stable_node_ids is not None and decision != "Structural Candidate" and node not in stable_node_ids:
            errors.append(f"{prefix}: unknown Stable Node ID {node}")
        for column in ("Target Chapter Ref", "Adjacent Chapter Refs"):
            values = _split_multi(row.get(column, ""))
            if not values or any(not _is_specific_reference(value) for value in values):
                errors.append(f"{prefix}: {column} requires concrete chapter/section references")
        existing_ref = row.get("Existing Proposition", "").strip("`")
        delta_ref = row.get("New Evidence Delta", "").strip("`")
        if existing_ref != f"existing:{family}":
            errors.append(f"{prefix}: Existing Proposition must equal existing:{family}")
        if delta_ref != f"delta:{family}":
            errors.append(f"{prefix}: New Evidence Delta must equal delta:{family}")
        _bounded_segment(text, existing_ref, f"{prefix} Existing Proposition", errors)
        _bounded_segment(text, delta_ref, f"{prefix} New Evidence Delta", errors)
        relation = row.get("Evolution Relation", "")
        if relation not in EVOLUTION_RELATIONS and not (
            relation.startswith("Not Applicable") and _is_reasoned_exception(relation)
        ):
            errors.append(f"{prefix}: invalid Evolution Relation {relation!r}")
        books_ref = row.get("Books Review Ref", "").strip("`")
        if books_ref != f"books-review:{family}":
            errors.append(f"{prefix}: Books Review Ref must equal books-review:{family}")
        if books_ref != candidate.get("Books Review Ref", "").strip("`"):
            errors.append(f"{prefix}: Books Review Ref must match Candidate Ledger")
        _bounded_segment(text, books_ref, f"{prefix} Books Review Ref", errors)
    for family in sorted(required_books - set(books_by_family)):
        errors.append(f"candidate {family}: Books Comparison receipt is required")

    audits: Dict[str, Mapping[str, str]] = {}
    audit_ids: set = set()
    for number, row in enumerate(audit_rows, start=1):
        prefix = f"Semantic Audit row {number}"
        audit_id = row.get("Audit ID", "").strip("`")
        if audit_id in ABSENT_VALUES or audit_id in audit_ids:
            errors.append(f"{prefix}: Audit ID must be non-empty and unique")
        audit_ids.add(audit_id)
        scope = row.get("Scope", "")
        if scope not in SEMANTIC_SCOPES:
            errors.append(f"{prefix}: invalid Scope {scope!r}")
            continue
        if scope in audits:
            errors.append(f"{prefix}: duplicate semantic audit scope {scope}")
        audits[scope] = row
        auditor = row.get("Auditor", "")
        if not re.fullmatch(r"(?:fresh-context|human):[A-Za-z0-9._-]+", auditor):
            errors.append(f"{prefix}: Auditor must identify a fresh-context or human reviewer")
        status = row.get("Status", "")
        if status not in SEMANTIC_STATUSES:
            errors.append(f"{prefix}: invalid Status {status!r}")
        refs = _split_multi(row.get("Reviewed Refs", ""))
        if not refs:
            errors.append(f"{prefix}: Reviewed Refs cannot be empty")
        if len(refs) != len(set(refs)):
            errors.append(f"{prefix}: Reviewed Refs must be unique")
        for ref in refs:
            if f"<!-- {ref}:start -->" not in text and ref not in {
                REVIEW_COMPLETION_MARKER.strip("<!--> "),
                DEEP_ANALYSIS_SELECTION_MARKER.strip("<!--> "),
                BOOKS_COMPARISON_MARKER.strip("<!--> "),
            }:
                errors.append(f"{prefix}: Reviewed Ref {ref} has no bounded evidence target")
        findings = row.get("Findings", "")
        resolution = row.get("Resolution", "")
        if status == "passed":
            if findings not in ABSENT_VALUES and findings.casefold() != "none":
                errors.append(f"{prefix}: passed audit requires zero unresolved findings")
            if resolution not in ABSENT_VALUES and not _is_specific_statement(resolution):
                errors.append(f"{prefix}: Resolution must be a concrete repair ref or —")
        elif status == "open":
            if findings in ABSENT_VALUES or findings.casefold() == "none":
                errors.append(f"{prefix}: open audit requires a concrete finding ID and impact")
            if resolution in ABSENT_VALUES:
                errors.append(f"{prefix}: open audit requires a concrete pending resolution")
        elif status == "not_applicable" and (
            scope != "books" or metadata.get("Report Type") != "Historical Weekly"
        ):
            errors.append(f"{prefix}: not_applicable is allowed only for Historical books scope")

    required_scopes = {"coverage", "evidence", "deep_analysis_selection", "books"}
    for scope in sorted(required_scopes - set(audits)):
        errors.append(f"V2.1 report requires semantic audit scope {scope}")
    books_audit = audits.get("books", {})
    if books_audit.get("Status") == "passed":
        books_reviewed_refs = set(_split_multi(books_audit.get("Reviewed Refs", "")))
        expected_candidate_refs = {
            f"review:{family}"
            for family, candidate in candidates.items()
            if candidate.get("Books Disposition") == "Weekly Only — Context"
            and candidate.get("Review Status")
            in {"deep_complete", "standard_complete", "closure_complete"}
        }
        missing_candidate_refs = sorted(expected_candidate_refs - books_reviewed_refs)
        if missing_candidate_refs:
            errors.append(
                "passed books audit must review every Weekly Only candidate disposition "
                "via per-family Review Ref, including mixed Books Comparison reports; missing "
                + ", ".join(missing_candidate_refs)
            )
    if metadata.get("Completion Status") == "Complete":
        applicable_scopes = set(required_scopes)
        if metadata.get("Books Gate") == "Not Applicable":
            applicable_scopes.remove("books")
        for scope in sorted(applicable_scopes):
            if scope not in audits or audits[scope].get("Status") != "passed":
                errors.append(f"Completion Status Complete requires semantic audit scope {scope} passed")
        if metadata.get("Books Gate") == "Not Applicable":
            books_audit = audits.get("books")
            if books_audit and books_audit.get("Status") != "not_applicable":
                errors.append("Historical Books Gate Not Applicable requires books semantic audit not_applicable")
    gate_scope = {
        "Coverage Gate": "coverage",
        "Evidence Gate": "evidence",
        "Books Gate": "books",
    }
    for gate, scope in gate_scope.items():
        if metadata.get(gate) == "Passed" and (
            scope not in audits or audits[scope].get("Status") != "passed"
        ):
            errors.append(f"{gate} Passed requires semantic audit scope {scope} passed")

    if audits.get("coverage", {}).get("Status") == "open" and metadata.get(
        "Coverage Gate"
    ) != "Open":
        errors.append("open coverage semantic audit requires Coverage Gate Open")
    if any(
        audits.get(scope, {}).get("Status") == "open"
        for scope in ("evidence", "deep_analysis_selection")
    ):
        if metadata.get("Evidence Gate") != "Open":
            errors.append(
                "open evidence/deep_analysis_selection semantic audit requires Evidence Gate Open"
            )
        if metadata.get("Books Gate") != "Open":
            errors.append(
                "open evidence/deep_analysis_selection semantic audit requires Books Gate Open"
            )
    if audits.get("books", {}).get("Status") == "open" and metadata.get("Books Gate") != "Open":
        errors.append("open books semantic audit requires Books Gate Open")

    material_rows: List[Dict[str, str]] = []
    if MATERIALS_REQUEST_MARKER in text:
        material_rows, _ = _expect_columns(text, MATERIALS_REQUEST_MARKER, MATERIALS_REQUEST_COLUMNS)
    material_families = {row.get("Source Family ID", "").strip("`") for row in material_rows}
    for family, candidate in candidates.items():
        if candidate.get("Access Status") != "disputed":
            continue
        dispute_ref = f"dispute:{family}"
        if family not in material_families and f"<!-- {dispute_ref}:start -->" not in text:
            errors.append(
                f"candidate {family}: disputed evidence requires a bounded dispute ref or Materials Request"
            )


def validate_report_text(
    text: str,
    registry: Mapping[str, Mapping[str, str]],
    strict: bool = False,
    stable_node_ids: Optional[set] = None,
) -> List[str]:
    """Validate one report; legacy/unmarked Score V1 reports are accepted unchanged."""
    if METADATA_MARKER not in text:
        if strict:
            return [f"missing marker {METADATA_MARKER}; strict reports require metadata Score Schema V2"]
        return []

    errors: List[str] = validate_markdown_structure(text)
    v21_markers = {
        SOURCE_COVERAGE_MARKER,
        CANDIDATE_LEDGER_MARKER,
        REVIEW_COMPLETION_MARKER,
        DEEP_ANALYSIS_SELECTION_MARKER,
        BOOKS_COMPARISON_MARKER,
        SEMANTIC_AUDIT_MARKER,
    }
    present_v21 = {marker for marker in v21_markers if marker in text}
    is_v21 = bool(present_v21)
    if is_v21 and present_v21 != v21_markers:
        for marker in sorted(v21_markers - present_v21):
            errors.append(f"V2.1 report is missing marker {marker}")
    metadata_rows, table_errors = _expect_columns(text, METADATA_MARKER, METADATA_COLUMNS)
    errors.extend(table_errors)
    coverage_marker = SOURCE_COVERAGE_MARKER if is_v21 else SOURCE_COVERAGE_V1_MARKER
    coverage_columns = SOURCE_COVERAGE_COLUMNS if is_v21 else SOURCE_COVERAGE_V1_COLUMNS
    candidate_marker = CANDIDATE_LEDGER_MARKER if is_v21 else CANDIDATE_LEDGER_V2_MARKER
    candidate_columns = CANDIDATE_COLUMNS if is_v21 else CANDIDATE_V2_COLUMNS
    coverage_rows, table_errors = _expect_columns(text, coverage_marker, coverage_columns)
    errors.extend(table_errors)
    candidate_rows, table_errors = _expect_columns(text, candidate_marker, candidate_columns)
    errors.extend(table_errors)

    metadata = _metadata(metadata_rows, errors)
    if is_v21:
        if metadata.get("Contract Version") != "V2.1":
            errors.append("V2.1 report metadata requires Contract Version V2.1")
    elif strict:
        errors.append(
            "strict report validation requires Contract Version V2.1 and the V2.1 report interfaces"
        )
    if metadata.get("Score Schema") != "V2":
        errors.append(f"report metadata Score Schema must be V2: {metadata.get('Score Schema', '')!r}")
    _validate_window(metadata, errors)
    completion = metadata.get("Completion Status", "")
    if completion not in {"Complete", "Conditional", "In Progress"}:
        errors.append(f"invalid Completion Status {completion!r}")
    gate_values = {
        "Coverage Gate": {"Closed", "Conditional Pass", "Open"},
        "Evidence Gate": {"Passed", "Conditional Pass", "Open"},
        "Books Gate": {"Passed", "Conditional Pass", "Open", "Not Applicable"},
    }
    for gate, allowed in gate_values.items():
        value = metadata.get(gate, "")
        if value and value not in allowed:
            errors.append(f"invalid {gate} value {value!r}")

    report_type = metadata.get("Report Type", "")
    books_gate = metadata.get("Books Gate", "")
    if books_gate == "Not Applicable" and report_type != "Historical Weekly":
        errors.append("Books Gate Not Applicable is allowed only for Historical Weekly")
    if books_gate == "Passed" and metadata.get("Coverage Gate") != "Closed":
        errors.append("Books Gate Passed requires Coverage Gate Closed")
    if books_gate == "Passed" and metadata.get("Evidence Gate") != "Passed":
        errors.append("Books Gate Passed requires Evidence Gate Passed")
    registry_version = _parse_iso_date(metadata.get("Registry Version", ""), "Registry Version", errors)
    current_registry_version = _registry_effective_version(registry, errors)
    if registry_version and current_registry_version and registry_version != current_registry_version:
        errors.append(
            "Registry Version "
            f"{registry_version.isoformat()} does not match loaded registry version "
            f"{current_registry_version.isoformat()}"
        )

    coverage_mode = metadata.get("Coverage Mode", "")
    if coverage_mode not in COVERAGE_MODES:
        errors.append(f"invalid Coverage Mode {coverage_mode!r}")
    baseline_report = metadata.get("Baseline Report", "")
    changed_source_ids = _split_multi(metadata.get("Changed Source IDs", ""))
    previous_denominator_id = metadata.get("Previous Denominator ID", "")
    if len(changed_source_ids) != len(set(changed_source_ids)):
        errors.append("Changed Source IDs must be unique")
    if coverage_mode == "Delta Audit" and report_type != "Historical Weekly":
        errors.append("Delta Audit is allowed only for Historical Weekly reports")
    if coverage_mode == "Full Replay":
        if (
            baseline_report not in ABSENT_VALUES
            or changed_source_ids
            or previous_denominator_id not in ABSENT_VALUES
        ):
            errors.append(
                "Full Replay requires empty Baseline Report, Changed Source IDs, "
                "and Previous Denominator ID"
            )
        # Registry Version identifies the loaded registry snapshot. Source
        # applicability is temporal: a source added on 2026-08-25 must not be
        # retroactively required by a report whose window ended earlier.
        if report_type == "Historical Weekly":
            # A newly generated Historical Weekly is an explicit current-contract
            # replay. It therefore executes the loaded registry, even when the
            # event window predates the registry snapshot.
            applicability_date = registry_version
        else:
            # Live reports and explicitly reconstructed Dailies follow the source
            # contract that was effective for their event window. Later registry
            # additions do not create impossible retroactive Daily receipts.
            applicability_date = _parse_iso_date(
                metadata.get("Window End", ""), "Window End applicability", []
            )
        due_ids = _due_source_ids(report_type, registry, applicability_date)
    elif coverage_mode == "Delta Audit":
        if (
            baseline_report in ABSENT_VALUES
            or not changed_source_ids
            or previous_denominator_id in ABSENT_VALUES
        ):
            errors.append(
                "Delta Audit requires Baseline Report, Changed Source IDs, "
                "and Previous Denominator ID"
            )
        unknown_changed = sorted(set(changed_source_ids) - set(registry))
        for source_id in unknown_changed:
            errors.append(f"Delta Audit references unknown Changed Source ID {source_id}")
        due_ids = set(changed_source_ids)
    else:
        due_ids = set()

    denominator_id = metadata.get("Denominator ID", "")
    if denominator_id in ABSENT_VALUES:
        errors.append("Denominator ID cannot be empty")
    if (
        coverage_mode == "Delta Audit"
        and previous_denominator_id not in ABSENT_VALUES
        and previous_denominator_id == denominator_id
    ):
        errors.append("Delta Audit requires a new Denominator ID")
    _parse_iso_datetime(
        metadata.get("Denominator Frozen At", ""),
        "Denominator Frozen At",
        errors,
    )

    window_start = _parse_iso_date(metadata.get("Window Start", ""), "Window Start", [])
    window_end = _parse_iso_date(metadata.get("Window End", ""), "Window End", [])
    report_owner_week = ""
    if window_start:
        iso_year, iso_week, _ = window_start.isocalendar()
        report_owner_week = f"{iso_year}-W{iso_week:02d}"
    seen_coverage: Dict[str, Mapping[str, str]] = {}
    receipt_families: Dict[str, set] = {}
    blocking_failure = False
    incomplete_coverage = False
    blocking_source_failures: Dict[Tuple[str, str], str] = {}
    for number, row in enumerate(coverage_rows, start=1):
        source_id = row.get("Source ID", "").strip("`")
        prefix = f"source coverage row {number}"
        if source_id not in registry:
            errors.append(f"{prefix}: unknown Source ID {source_id}")
        if source_id in seen_coverage:
            errors.append(f"{prefix}: duplicate Source ID {source_id}")
        seen_coverage[source_id] = row
        cadence = registry.get(source_id, {}).get("Cadence", "")
        if cadence in {"Required Daily", "Required Weekly"} and source_id not in due_ids:
            errors.append(f"{prefix}: non-due Required source {source_id} must be omitted")
        result = row.get("Result", "")
        if result not in SOURCE_RESULTS:
            errors.append(f"{prefix}: invalid Result {result!r}")
        if row.get("Endpoint / Filter", "") in ABSENT_VALUES:
            errors.append(f"{prefix}: Endpoint / Filter cannot be empty")
        if is_v21:
            receipt_start = _parse_iso_datetime(
                row.get("Window Start", ""), f"{prefix} Window Start", errors
            )
            receipt_end = _parse_iso_datetime(
                row.get("Window End", ""), f"{prefix} Window End", errors
            )
            if receipt_start and window_start and receipt_start.date() > window_end:
                errors.append(f"{prefix}: execution window does not overlap the report archive day/window")
            if receipt_end and window_start and receipt_end.date() < window_start:
                errors.append(f"{prefix}: execution window does not overlap the report archive day/window")
            if receipt_start and receipt_end and receipt_start > receipt_end:
                errors.append(f"{prefix}: Window Start must not be after Window End")
            _parse_iso_datetime(row.get("Executed At", ""), f"{prefix} Executed At", errors)
            watermark = row.get("Window Watermark", "").strip("`")
            closure_evidence = row.get("Closure Evidence", "").strip("`")
            cursor = row.get("Pagination / Cursor", "").strip("`")
            requires_closure = result in {"checked", "no_hit", "not_due"}
            if requires_closure or watermark not in ABSENT_VALUES:
                _parse_iso_datetime(watermark, f"{prefix} Window Watermark", errors)
            if requires_closure or closure_evidence not in ABSENT_VALUES:
                if not _is_specific_reference(closure_evidence):
                    errors.append(
                        f"{prefix}: Closure Evidence must be a source-locatable receipt, snapshot, or hash"
                    )
                elif closure_evidence.startswith("coverage:"):
                    _bounded_segment(text, closure_evidence, f"{prefix} Closure Evidence", errors)
            if requires_closure or cursor not in ABSENT_VALUES:
                if not _is_specific_reference(cursor):
                    errors.append(
                        f"{prefix}: Pagination / Cursor must record a page count, final cursor, or reasoned exception"
                    )
            endpoint_filter = row.get("Endpoint / Filter", "")
            if (
                "api.github.com/repos/" in endpoint_filter
                and "/commits?until=" in endpoint_filter
                and "per_page=1" in endpoint_filter
                and "final_cursor=end" in cursor
            ):
                errors.append(
                    f"{prefix}: a GitHub commit-selection query with per_page=1 cannot claim final_cursor=end; "
                    "record first-result selection and intentional non-traversal of older history"
                )
            if result == "incomplete" and all(
                value not in ABSENT_VALUES for value in (watermark, closure_evidence, cursor)
            ):
                errors.append(
                    f"{prefix}: incomplete must identify at least one unclosed cursor, watermark, or closure field"
                )
        hits = _int(row.get("Hits", ""), f"{prefix} Hits", errors)
        if hits is not None and hits < 0:
            errors.append(f"{prefix}: Hits cannot be negative")
        families = _split_multi(row.get("Candidate Source Families", ""))
        if len(families) != len(set(families)):
            errors.append(f"{prefix}: Candidate Source Families must be unique")
        if result == "no_hit":
            if hits is not None and hits != 0:
                errors.append(f"{prefix}: no_hit requires Hits 0")
            if families:
                errors.append(f"{prefix}: no_hit cannot list candidate families")
        if result == "checked":
            if hits == 0:
                errors.append(f"{prefix}: checked with Hits 0 must use no_hit")
            if hits is not None and hits > 0 and not families:
                errors.append(f"{prefix}: checked source with Hits greater than 0 requires candidate families")
        if result == "not_due" and ((hits is not None and hits != 0) or families):
            errors.append(f"{prefix}: not_due requires Hits 0 and no candidate families")
        if result == "not_due":
            endpoint_filter = row.get("Endpoint / Filter", "").strip().casefold()
            generic_not_due = {
                "未触发",
                "未到期",
                "not triggered",
                "not due",
                "not_due",
            }
            if endpoint_filter in generic_not_due:
                errors.append(
                    f"{prefix}: not_due requires a concrete Endpoint / Filter, not only {endpoint_filter!r}"
                )
            if cadence in {"Required Daily", "Required Weekly"}:
                errors.append(f"{prefix}: Required source {source_id} cannot use not_due")
        if result == "incomplete":
            incomplete_coverage = True
            gap_id = row.get("Gap / Limitation ID", "").strip("`")
            if gap_id in ABSENT_VALUES:
                errors.append(f"{prefix}: incomplete source requires Gap / Limitation ID")
        for family in families:
            receipt_families.setdefault(family, set()).add(source_id)
        if result == "failed":
            gap_id = row.get("Gap / Limitation ID", "").strip("`")
            if gap_id in ABSENT_VALUES:
                errors.append(f"{prefix}: failed source requires Gap / Limitation ID")
            closure = registry.get(source_id, {}).get("Pagination / Cursor", "")
            if "Non-deterministic backstop" not in closure:
                blocking_failure = True
                if gap_id not in ABSENT_VALUES:
                    blocking_source_failures[(source_id, gap_id)] = report_owner_week
        if (not is_v21 or result in {"checked", "no_hit", "not_due"}) and row.get(
            "Pagination / Cursor", ""
        ) in ABSENT_VALUES:
            errors.append(f"{prefix}: Pagination / Cursor cannot be empty")
    for source_id in sorted(due_ids - set(seen_coverage)):
        errors.append(f"missing due Source ID {source_id} in Source Coverage Receipt")
    if coverage_mode == "Delta Audit":
        unexpected = sorted(set(seen_coverage) - set(changed_source_ids))
        for source_id in unexpected:
            errors.append(f"Delta Audit receipt contains unchanged Source ID {source_id}")
    if blocking_failure and metadata.get("Coverage Gate") == "Closed":
        errors.append("Coverage Gate cannot be Closed while a source result is failed")
    if incomplete_coverage and metadata.get("Coverage Gate") != "Open":
        errors.append("Coverage Gate must be Open while a source result is incomplete")
    if incomplete_coverage and completion != "In Progress":
        errors.append("incomplete source coverage requires Completion Status In Progress")

    pending = False
    unresolved_access = False
    books_not_assessed = False
    benchmark_claims: Dict[str, bool] = {}
    candidate_access: Dict[str, Tuple[str, str]] = {}
    candidate_by_family: Dict[str, Mapping[str, str]] = {}
    earlier_owner_pending = False
    seen_families: set = set()
    for number, row in enumerate(candidate_rows, start=1):
        family = row.get("Source Family ID", "")
        prefix = f"candidate {family or number}"
        if not family:
            errors.append(f"candidate row {number}: Source Family ID cannot be empty")
        if family in seen_families:
            errors.append(f"{prefix}: duplicate Source Family ID")
        seen_families.add(family)
        candidate_by_family[family] = row

        primary_identifier = row.get("Primary Identifier", "")
        event_identity = row.get("Event Identity", "")
        if primary_identifier in ABSENT_VALUES:
            errors.append(f"{prefix}: Primary Identifier cannot be empty")
        if event_identity in ABSENT_VALUES:
            errors.append(f"{prefix}: Event Identity cannot be empty")

        first_public = _parse_iso_date(row.get("First-public Date", ""), f"{prefix} First-public Date", errors)
        owner_week = row.get("Owner Week", "")
        if first_public:
            iso_year, iso_week, _ = first_public.isocalendar()
            expected_owner = f"{iso_year}-W{iso_week:02d}"
            if owner_week != expected_owner:
                errors.append(
                    f"{prefix}: Owner Week {owner_week!r} does not match first-public date owner {expected_owner}"
                )

        candidate_state = row.get("Candidate State", "")
        supporting_source_ids = _split_multi(row.get("Supporting Source IDs", ""))
        review = row.get("Review Status", "")
        access = row.get("Access Status", "")
        override = row.get("Review Override", "")
        review_ref = row.get("Review Ref", "").strip("`")
        disposition = row.get("Books Disposition", "")
        books_review_ref = row.get("Books Review Ref", "").strip("`")
        benchmark = row.get("Benchmark Claim", "")
        if candidate_state not in CANDIDATE_STATES:
            errors.append(f"{prefix}: invalid Candidate State {candidate_state!r}")
        if report_type == "Daily" and candidate_state == "spillback":
            errors.append(
                f"{prefix}: Daily candidate cannot use spillback to skip Score V2; "
                "deduplicate first, then score every newly discovered Source Family"
            )
        if not supporting_source_ids:
            errors.append(f"{prefix}: Supporting Source IDs cannot be empty")
        if len(supporting_source_ids) != len(set(supporting_source_ids)):
            errors.append(f"{prefix}: Supporting Source IDs must be unique")
        for source_id in supporting_source_ids:
            if source_id not in registry:
                errors.append(f"{prefix}: unknown Supporting Source ID {source_id}")
            elif source_id not in seen_coverage:
                errors.append(f"{prefix}: Supporting Source ID {source_id} has no Source Coverage Receipt")
            elif family not in _split_multi(seen_coverage[source_id].get("Candidate Source Families", "")):
                errors.append(
                    f"{prefix}: Supporting Source ID {source_id} receipt does not list family {family}"
                )
        if review not in REVIEW_STATUSES:
            errors.append(f"{prefix}: invalid Review Status {review!r}")
        if access not in ACCESS_STATUSES:
            errors.append(f"{prefix}: invalid Access Status {access!r}")
        if override not in REVIEW_OVERRIDES:
            errors.append(f"{prefix}: invalid Review Override {override!r}")
        if disposition not in BOOKS_DISPOSITIONS:
            errors.append(f"{prefix}: invalid Books Disposition {disposition!r}")
        if benchmark not in {"yes", "no"}:
            errors.append(f"{prefix}: Benchmark Claim must be yes or no")
        benchmark_claims[family] = benchmark == "yes"
        candidate_access[family] = ("blocked" if review == "blocked" else access, owner_week)

        completed_review = review in {"deep_complete", "standard_complete", "closure_complete"}
        if completed_review and review_ref in ABSENT_VALUES:
            errors.append(f"{prefix}: completed Review Status requires Review Ref")
        if review_ref not in ABSENT_VALUES and not is_v21:
            expected_review_ref = f"review:{family}"
            if review_ref != expected_review_ref:
                errors.append(f"{prefix}: Review Ref must equal {expected_review_ref}")
            marker = _html_ref_marker(review_ref)
            count = text.count(marker)
            if count != 1:
                errors.append(f"{prefix}: Review Ref {review_ref} must have exactly one HTML marker")
            elif not _has_evidence_body_after_marker(text, marker):
                errors.append(f"{prefix}: Review Ref {review_ref} requires evidence body after its marker")
        if books_review_ref not in ABSENT_VALUES and not is_v21:
            expected_books_review_ref = f"books-review:{family}"
            if books_review_ref != expected_books_review_ref:
                errors.append(f"{prefix}: Books Review Ref must equal {expected_books_review_ref}")
            marker = _html_ref_marker(books_review_ref)
            count = text.count(marker)
            if count != 1:
                errors.append(f"{prefix}: Books Review Ref {books_review_ref} must have exactly one HTML marker")
            elif not _has_evidence_body_after_marker(text, marker):
                errors.append(
                    f"{prefix}: Books Review Ref {books_review_ref} requires evidence body after its marker"
                )

        if candidate_state in {"retained", "closure_only"}:
            scores = [
                _int(row.get(name, ""), f"{prefix} {name}", errors)
                for name in ("Design Delta", "System Reach", "Durability")
            ]
            for name, score in zip(("Design Delta", "System Reach", "Durability"), scores):
                if score is not None and not 0 <= score <= 3:
                    errors.append(f"{prefix}: {name} must be between 0 and 3")
            total = _int(row.get("Total", ""), f"{prefix} Total", errors)
            if all(score is not None for score in scores) and total is not None:
                expected_total = sum(scores)  # type: ignore[arg-type]
                if total != expected_total:
                    errors.append(f"{prefix}: Total {total} does not equal {expected_total}")
                if candidate_state == "closure_only" and total > 4:
                    errors.append(f"{prefix}: closure_only requires Score 0-4")
                if candidate_state == "retained" and total <= 4 and override == "none":
                    errors.append(f"{prefix}: retained requires Score 5-9 or a Review Override")
                if total >= 7 and review not in {"deep_complete", "pending", "blocked"}:
                    errors.append(
                        f"{prefix}: Score 7-9 requires Review Status deep_complete, pending, or blocked"
                    )
                elif 5 <= total <= 6 and review not in {
                    "standard_complete", "deep_complete", "pending", "blocked"
                }:
                    errors.append(
                        f"{prefix}: Score 5-6 requires standard/deep completion, pending, or blocked"
                    )
                elif total <= 4 and review not in {
                    "closure_complete", "standard_complete", "deep_complete", "pending", "blocked"
                }:
                    errors.append(f"{prefix}: Score 0-4 requires identity/date closure or deeper review")
        else:
            score_values = [row.get(name, "") for name in ("Design Delta", "System Reach", "Durability", "Total")]
            if any(value not in ABSENT_VALUES for value in score_values):
                errors.append(f"{prefix}: non-owner state {candidate_state} must not carry a score")

        if (
            report_type != "Daily"
            and candidate_state in {"retained", "closure_only"}
            and first_public
            and window_start
            and window_end
        ):
            if not window_start <= first_public <= window_end:
                errors.append(f"{prefix}: owner candidate is outside report window")

        if override != "none" and review not in {"deep_complete", "pending", "blocked"}:
            errors.append(
                f"{prefix}: Review Override {override} requires deep route completion, pending, or blocked"
            )
        if review == "pending":
            pending = True
        if is_v21:
            reconciliation = row.get("Reconciliation", "")
            owner_report_ref = row.get("Owner Report Ref", "").strip("`")
            prior_review_ref = row.get("Prior Review Ref", "").strip("`")
            if reconciliation not in RECONCILIATIONS:
                errors.append(f"{prefix}: invalid Reconciliation {reconciliation!r}")
            if reconciliation == "new_in_window":
                if owner_report_ref != "self" or prior_review_ref not in ABSENT_VALUES:
                    errors.append(
                        f"{prefix}: new_in_window requires Owner Report Ref self and no Prior Review Ref"
                    )
            elif reconciliation == "earlier_owner_pending":
                earlier_owner_pending = True
                if owner_report_ref in ABSENT_VALUES or owner_report_ref == "self":
                    errors.append(
                        f"{prefix}: earlier_owner_pending requires a concrete Owner Report Ref"
                    )
            elif reconciliation == "earlier_owner_written_back":
                if owner_report_ref in ABSENT_VALUES or owner_report_ref == "self":
                    errors.append(
                        f"{prefix}: earlier_owner_written_back requires a concrete Owner Report Ref"
                    )
            elif reconciliation == "same_window_revision":
                if owner_report_ref in ABSENT_VALUES:
                    errors.append(
                        f"{prefix}: {reconciliation} requires Owner Report Ref"
                    )
                if candidate_state != "revision":
                    errors.append(
                        f"{prefix}: same_window_revision requires Candidate State revision"
                    )
                if override != "important_revision":
                    errors.append(
                        f"{prefix}: same_window_revision requires important_revision override"
                    )
            elif reconciliation == "spillback_reference":
                if report_type not in {"Sunday Weekly", "Historical Weekly"}:
                    errors.append(
                        f"{prefix}: spillback_reference is allowed only for Sunday Weekly "
                        "or Historical Weekly"
                    )
                if owner_report_ref in ABSENT_VALUES or owner_report_ref == "self":
                    errors.append(
                        f"{prefix}: spillback_reference requires a concrete non-self "
                        "Owner Report Ref"
                    )
            elif reconciliation == "reused_unchanged":
                if owner_report_ref in ABSENT_VALUES or prior_review_ref in ABSENT_VALUES:
                    errors.append(
                        f"{prefix}: reused_unchanged requires Owner Report Ref and Prior Review Ref"
                    )
            elif reconciliation == "out_of_scope" and candidate_state != "out_of_scope":
                errors.append(f"{prefix}: Reconciliation out_of_scope requires Candidate State out_of_scope")
            if prior_review_ref not in ABSENT_VALUES and not re.fullmatch(
                r"RP-[a-f0-9]{16}", prior_review_ref
            ):
                errors.append(
                    f"{prefix}: Prior Review Ref must identify a frozen RP-* Review Provenance ID"
                )
            if access == "partial" and review not in {"pending", "blocked"}:
                errors.append(f"{prefix}: Access Status partial requires Review Status pending or blocked")
            if review == "blocked" and access not in {"partial", "blocked", "unverified"}:
                errors.append(
                    f"{prefix}: Review Status blocked requires partial, blocked, or unverified access"
                )
        if access in {"blocked", "unverified", "disputed"} or review == "blocked":
            unresolved_access = True
        if disposition == "Not Assessed":
            books_not_assessed = True
        if access in {"blocked", "unverified", "disputed"} and disposition in {
            "Integrate",
            "No Change — Existing Coverage",
        }:
            errors.append(f"{prefix}: Access Status {access} cannot use Books Disposition {disposition}")
        if disposition == "Blocked / Unverified" and not (
            access in {"blocked", "unverified"} or (access == "partial" and review == "blocked")
        ):
            errors.append(
                f"{prefix}: Blocked / Unverified requires blocked/unverified access "
                "or partial access with Review Status blocked"
            )
        if disposition == "Disputed" and access != "disputed":
            errors.append(f"{prefix}: Disputed requires Access Status disputed")
        stable_node_id = row.get("Stable Node ID", "").strip("`")
        if disposition in {"Integrate", "No Change — Existing Coverage"}:
            if stable_node_id in ABSENT_VALUES:
                errors.append(f"{prefix}: {disposition} requires Stable Node ID")
            elif stable_node_ids is not None and stable_node_id not in stable_node_ids:
                errors.append(f"{prefix}: unknown Stable Node ID {stable_node_id}")
        if disposition == "Structural Candidate" and stable_node_id not in ABSENT_VALUES:
            errors.append(f"{prefix}: Structural Candidate requires Stable Node ID to be absent")
        if books_gate == "Not Applicable":
            if disposition != "Not Assessed":
                errors.append(
                    f"{prefix}: Books Gate Not Applicable requires Books Disposition Not Assessed"
                )
            if books_review_ref not in ABSENT_VALUES:
                errors.append(
                    f"{prefix}: Books Gate Not Applicable cannot carry Books Review Ref"
                )
        if disposition in {"Integrate", "No Change — Existing Coverage"} and books_review_ref in ABSENT_VALUES:
            errors.append(f"{prefix}: {disposition} requires Books Review Ref")
        if disposition == "Integrate":
            if candidate_state != "retained":
                errors.append(f"{prefix}: Integrate requires Candidate State retained")
            if review != "deep_complete":
                errors.append(f"{prefix}: Integrate requires deep_complete Review Status")
            if access != "accessible":
                errors.append(f"{prefix}: Integrate requires Access Status accessible")
        if disposition == "No Change — Existing Coverage":
            if not completed_review:
                errors.append(
                    f"{prefix}: No Change — Existing Coverage requires completed evidence review"
                )
            if access != "accessible":
                errors.append(
                    f"{prefix}: No Change — Existing Coverage requires Access Status accessible"
                )

    for family in sorted(set(receipt_families) - seen_families):
        errors.append(f"receipt family {family} is missing from Candidate Ledger")

    if is_v21:
        pending = pending or earlier_owner_pending
        if earlier_owner_pending and completion != "In Progress":
            errors.append("earlier_owner_pending reconciliation requires Completion Status In Progress")
        if earlier_owner_pending and metadata.get("Evidence Gate") != "Open":
            errors.append("earlier_owner_pending reconciliation requires Evidence Gate Open")
        if earlier_owner_pending and metadata.get("Books Gate") != "Open":
            errors.append("earlier_owner_pending reconciliation requires Books Gate Open")
        _validate_v21_completion_interfaces(
            text,
            metadata,
            candidate_by_family,
            stable_node_ids,
            errors,
        )

    _validate_materials_requests(text, candidate_access, blocking_source_failures, errors)

    if pending and metadata.get("Evidence Gate") == "Passed":
        errors.append("Evidence Gate cannot be Passed while Review Status pending exists")
    if pending and metadata.get("Evidence Gate") != "Open":
        errors.append("Evidence Gate must be Open while Review Status pending exists")
    if pending and completion != "In Progress":
        errors.append("Review Status pending requires Completion Status In Progress")
    if unresolved_access and metadata.get("Evidence Gate") == "Passed":
        errors.append("Evidence Gate cannot be Passed while blocked, unverified or disputed evidence exists")
    if books_not_assessed and metadata.get("Books Gate") == "Passed":
        errors.append("Books Gate cannot be Passed while Books Disposition Not Assessed exists")
    if pending and metadata.get("Books Gate") == "Passed":
        errors.append("Books Gate cannot be Passed while pending work exists")
    if completion == "Complete":
        non_terminal_gates = [
            gate
            for gate in ("Coverage Gate", "Evidence Gate", "Books Gate")
            if metadata.get(gate) in {"Open", "Conditional Pass"}
        ]
        if non_terminal_gates:
            errors.append(
                "Completion Status Complete requires terminal gates; found: "
                + ", ".join(non_terminal_gates)
            )
    if completion == "In Progress" and not pending:
        terminal_gates = (
            metadata.get("Coverage Gate") == "Closed"
            and metadata.get("Evidence Gate") == "Passed"
            and metadata.get("Books Gate") in {"Passed", "Not Applicable"}
        )
        if terminal_gates:
            errors.append("Completion Status In Progress conflicts with terminal gates and no pending review")
    if completion == "Conditional":
        if pending or incomplete_coverage or earlier_owner_pending:
            errors.append(
                "Completion Status Conditional cannot close ordinary pending review, "
                "incomplete coverage, or unreconciled earlier-owner work"
            )
        open_gates = [
            gate
            for gate in ("Coverage Gate", "Evidence Gate", "Books Gate")
            if metadata.get(gate) == "Open"
        ]
        if open_gates:
            errors.append(f"Completion Status Conditional cannot coexist with Open gate(s): {', '.join(open_gates)}")
        qualified = (
            metadata.get("Coverage Gate") == "Conditional Pass" and blocking_failure
        ) or (
            metadata.get("Evidence Gate") == "Conditional Pass" and unresolved_access
        ) or (
            metadata.get("Books Gate") == "Conditional Pass"
            and (blocking_failure or unresolved_access)
        )
        if not qualified:
            errors.append("Completion Status Conditional requires an external coverage or evidence limitation")
    if metadata.get("Coverage Gate") == "Conditional Pass" and not blocking_failure:
        errors.append("Coverage Gate Conditional Pass requires a blocking failed source")
    if metadata.get("Evidence Gate") == "Conditional Pass" and not unresolved_access:
        errors.append("Evidence Gate Conditional Pass requires blocked, unverified or disputed evidence")
    if blocking_failure and metadata.get("Books Gate") == "Passed":
        errors.append("Books Gate cannot be Passed while a blocking source failure exists")
    if unresolved_access and metadata.get("Books Gate") == "Passed":
        errors.append("Books Gate cannot be Passed while unresolved evidence exists")
    if metadata.get("Books Gate") == "Conditional Pass" and not (blocking_failure or unresolved_access):
        errors.append("Books Gate Conditional Pass requires an external coverage or evidence limitation")
    if incomplete_coverage and metadata.get("Books Gate") != "Open":
        errors.append("Books Gate must be Open while source coverage is incomplete")
    _validate_benchmarks(text, benchmark_claims, errors)
    return errors


def _resolve_report_path(path: Path, root: Path) -> Path:
    return (path if path.is_absolute() else root / path).resolve()


def validate_report_collection(
    reports: Sequence[Tuple[Path, str]],
    root: Path,
    registry: Optional[Mapping[str, Mapping[str, str]]] = None,
) -> List[str]:
    """Validate identities and ownership across a set of Score V2 reports."""
    errors: List[str] = []
    root = root.resolve()
    snapshots: Dict[Path, Tuple[Dict[str, str], List[Dict[str, str]]]] = {}
    snapshot_texts: Dict[Path, str] = {}
    legacy_baseline_digests: Dict[Path, str] = {}
    baselines: Dict[Path, Path] = {}
    denominators: Dict[str, Path] = {}

    def register_snapshot(path: Path, text: str) -> None:
        if path in snapshots:
            return
        if METADATA_MARKER not in text:
            errors.append(f"Baseline Report {path} must contain {METADATA_MARKER}")
            return
        metadata_rows, _ = _expect_columns(text, METADATA_MARKER, METADATA_COLUMNS)
        if CANDIDATE_LEDGER_MARKER in text:
            candidate_rows, _ = _expect_columns(text, CANDIDATE_LEDGER_MARKER, CANDIDATE_COLUMNS)
        else:
            candidate_rows, _ = _expect_columns(
                text, CANDIDATE_LEDGER_V2_MARKER, CANDIDATE_V2_COLUMNS
            )
        metadata_errors: List[str] = []
        metadata = _metadata(metadata_rows, metadata_errors)
        errors.extend(f"report {path}: {error}" for error in metadata_errors)
        if metadata.get("Score Schema") != "V2":
            errors.append(f"report {path} metadata Score Schema must be V2")
        snapshots[path] = (metadata, candidate_rows)
        snapshot_texts[path] = text

        denominator_id = metadata.get("Denominator ID", "")
        if denominator_id not in ABSENT_VALUES:
            previous = denominators.get(denominator_id)
            if previous and previous != path:
                errors.append(
                    f"duplicate Denominator ID {denominator_id} in {previous} and {path}"
                )
            else:
                denominators[denominator_id] = path

        if metadata.get("Coverage Mode") == "Delta Audit":
            baseline_value = metadata.get("Baseline Report", "")
            if baseline_value not in ABSENT_VALUES:
                baseline = _resolve_report_path(Path(baseline_value), root)
                baselines[path] = baseline
                if baseline == path:
                    errors.append(f"Delta report {path} cannot reference itself as Baseline Report")

    for supplied_path, text in reports:
        if METADATA_MARKER not in text:
            continue
        register_snapshot(_resolve_report_path(supplied_path, root), text)

    attempted_baselines: set = set()
    while True:
        unresolved = {
            baseline
            for baseline in baselines.values()
            if baseline not in snapshots and baseline not in attempted_baselines
        }
        if not unresolved:
            break
        for baseline in sorted(unresolved, key=str):
            attempted_baselines.add(baseline)
            if not baseline.exists():
                continue
            try:
                baseline_bytes = baseline.read_bytes()
                baseline_text = baseline_bytes.decode("utf-8")
            except (OSError, UnicodeError) as exc:
                errors.append(f"cannot read Baseline Report {baseline}: {exc}")
                continue
            if METADATA_MARKER not in baseline_text:
                legacy_baseline_digests[baseline] = hashlib.sha256(baseline_bytes).hexdigest()
                continue
            register_snapshot(baseline, baseline_text)

    for path, baseline in baselines.items():
        if baseline not in snapshots and not baseline.exists():
            errors.append(f"Delta report {path} references missing Baseline Report {baseline}")
        if baseline in snapshots:
            current_metadata = snapshots[path][0]
            baseline_metadata = snapshots[baseline][0]
            for field in ("Report Type", "Window Start", "Window End"):
                if current_metadata.get(field) != baseline_metadata.get(field):
                    errors.append(
                        f"Delta report {path} Baseline Report disagrees on {field}"
                    )
            expected_previous = baseline_metadata.get("Denominator ID", "")
            actual_previous = current_metadata.get("Previous Denominator ID", "")
            if expected_previous in ABSENT_VALUES:
                errors.append(f"Delta report {path} V2 Baseline Report has no Denominator ID")
            elif actual_previous != expected_previous:
                errors.append(
                    f"Delta report {path} Previous Denominator ID {actual_previous!r} "
                    f"does not match Baseline Report denominator {expected_previous!r}"
                )
        elif baseline in legacy_baseline_digests:
            current_metadata = snapshots[path][0]
            baseline_value = current_metadata.get("Baseline Report", "").strip("`")
            expected_previous = (
                f"legacy:{baseline_value}@sha256:{legacy_baseline_digests[baseline]}"
            )
            actual_previous = current_metadata.get("Previous Denominator ID", "").strip("`")
            if actual_previous != expected_previous:
                errors.append(
                    f"Delta report {path} legacy baseline identity {actual_previous!r} "
                    f"does not match {expected_previous!r}"
                )

        if registry is not None:
            current_metadata = snapshots[path][0]
            try:
                current_registry_version = date.fromisoformat(
                    current_metadata.get("Registry Version", "")
                )
            except ValueError:
                current_registry_version = None
            changed_ids = set(_split_multi(current_metadata.get("Changed Source IDs", "")))
            due_ids = _due_source_ids(
                current_metadata.get("Report Type", ""), registry, current_registry_version
            )
            baseline_registry_version: Optional[date] = None
            if baseline in snapshots:
                try:
                    baseline_registry_version = date.fromisoformat(
                        snapshots[baseline][0].get("Registry Version", "")
                    )
                except ValueError:
                    baseline_registry_version = None
            if baseline_registry_version is None:
                for source_id in sorted(due_ids - changed_ids):
                    errors.append(
                        f"Delta report {path}: baseline registry version is unavailable; "
                        f"Changed Source IDs must include currently due Required Source ID {source_id}"
                    )
            else:
                newly_effective = set()
                for source_id in due_ids:
                    try:
                        effective_date = date.fromisoformat(
                            registry[source_id].get("Effective Date", "")
                        )
                    except ValueError:
                        continue
                    if effective_date > baseline_registry_version:
                        newly_effective.add(source_id)
                for source_id in sorted(newly_effective - changed_ids):
                    errors.append(
                        f"Delta report {path}: missing newly effective Required Source ID "
                        f"{source_id} since baseline Registry Version "
                        f"{baseline_registry_version.isoformat()}"
                    )

    for path in baselines:
        seen_chain: set = set()
        cursor = path
        while cursor in baselines:
            if cursor in seen_chain:
                errors.append(f"Baseline Report cycle detected at {cursor}")
                break
            seen_chain.add(cursor)
            cursor = baselines[cursor]

    def is_lineage_related(left: Path, right: Path) -> bool:
        cursor = right
        visited: set = set()
        while cursor in baselines and cursor not in visited:
            visited.add(cursor)
            cursor = baselines[cursor]
            if cursor == left:
                return True
        return False

    primary_families: Dict[str, Tuple[str, Path]] = {}
    event_identities: Dict[str, Tuple[str, str, Path]] = {}
    family_rows: Dict[str, List[Tuple[Path, Mapping[str, str]]]] = {}
    for path, (_, rows) in snapshots.items():
        for row in rows:
            family = row.get("Source Family ID", "")
            primary = row.get("Primary Identifier", "")
            event = row.get("Event Identity", "")
            family_rows.setdefault(family, []).append((path, row))
            if primary not in ABSENT_VALUES:
                existing = primary_families.get(primary)
                if existing and existing[0] != family:
                    errors.append(
                        f"Primary Identifier {primary} maps to both {existing[0]} and {family}"
                    )
                else:
                    primary_families[primary] = (family, path)
            if event not in ABSENT_VALUES:
                existing_event = event_identities.get(event)
                identity = (family, primary)
                if existing_event and existing_event[:2] != identity:
                    errors.append(
                        f"Event Identity {event} maps to conflicting family or primary identifier"
                    )
                else:
                    event_identities[event] = (family, primary, path)

    for family, occurrences in family_rows.items():
        def has_revision_owner_link(left: Path, right: Path) -> bool:
            for occurrence_path, occurrence_row in occurrences:
                if occurrence_path not in {left, right}:
                    continue
                if occurrence_row.get("Reconciliation") != "same_window_revision":
                    continue
                owner_value = occurrence_row.get("Owner Report Ref", "").strip("`")
                if owner_value in ABSENT_VALUES or owner_value == "self":
                    continue
                if _resolve_report_path(Path(owner_value), root) == (
                    right if occurrence_path == left else left
                ):
                    return True
            return False

        identity_occurrences = [
            (
                path,
                (
                    row.get("Primary Identifier", ""),
                    row.get("Event Identity", ""),
                    row.get("Owner Week", ""),
                    row.get("First-public Date", ""),
                ),
            )
            for path, row in occurrences
        ]
        identity_conflict = False
        for index, (left_path, left_identity) in enumerate(identity_occurrences):
            for right_path, right_identity in identity_occurrences[index + 1 :]:
                if left_identity == right_identity:
                    continue
                if (
                    not is_lineage_related(left_path, right_path)
                    and not is_lineage_related(right_path, left_path)
                    and not has_revision_owner_link(left_path, right_path)
                ):
                    identity_conflict = True
                    break
            if identity_conflict:
                break
        if identity_conflict:
            errors.append(f"Source Family {family} has conflicting primary identifier or owner identity")
        owner_paths_by_cadence: Dict[str, List[Path]] = {}
        for path, row in occurrences:
            if row.get("Candidate State") not in {"retained", "closure_only"}:
                continue
            report_type = snapshots[path][0].get("Report Type", "")
            cadence = "Daily" if report_type == "Daily" else "Weekly"
            owner_paths_by_cadence.setdefault(cadence, []).append(path)
        for owner_paths in owner_paths_by_cadence.values():
            unique_owner_paths = sorted(set(owner_paths), key=str)
            for index, left in enumerate(unique_owner_paths):
                for right in unique_owner_paths[index + 1 :]:
                    if not is_lineage_related(left, right) and not is_lineage_related(right, left):
                        errors.append(
                            f"Source Family {family} has multiple unrelated owner reports: {left} and {right}"
                        )

    for path, (metadata, rows) in snapshots.items():
        report_type = metadata.get("Report Type", "")
        for row in rows:
            reconciliation = row.get("Reconciliation", "")
            daily_owner_relation = report_type == "Daily" and reconciliation in {
                "earlier_owner_written_back",
                "same_window_revision",
                "reused_unchanged",
            }
            weekly_spillback = (
                report_type in {"Sunday Weekly", "Historical Weekly"}
                and reconciliation == "spillback_reference"
            )
            if not (daily_owner_relation or weekly_spillback):
                continue
            family = row.get("Source Family ID", "")
            owner_value = row.get("Owner Report Ref", "").strip("`")
            prior_ref = row.get("Prior Review Ref", "").strip("`")
            if owner_value in ABSENT_VALUES:
                continue
            owner_path = path if owner_value == "self" else _resolve_report_path(Path(owner_value), root)
            owner_snapshot = snapshots.get(owner_path)
            if owner_snapshot is None:
                if not owner_path.exists():
                    errors.append(
                        f"Report {path} candidate {family}: Owner Report Ref {owner_value} is missing"
                    )
                    continue
                try:
                    owner_text = owner_path.read_text(encoding="utf-8")
                except (OSError, UnicodeError) as exc:
                    errors.append(
                        f"Report {path} candidate {family}: cannot read Owner Report Ref "
                        f"{owner_value}: {exc}"
                    )
                    continue
                if CANDIDATE_LEDGER_MARKER in owner_text:
                    owner_rows, _ = _expect_columns(
                        owner_text, CANDIDATE_LEDGER_MARKER, CANDIDATE_COLUMNS
                    )
                elif CANDIDATE_LEDGER_V2_MARKER in owner_text:
                    owner_rows, _ = _expect_columns(
                        owner_text, CANDIDATE_LEDGER_V2_MARKER, CANDIDATE_V2_COLUMNS
                    )
                else:
                    errors.append(
                        f"Report {path} candidate {family}: Owner Report Ref {owner_value} "
                        "has no candidate ledger"
                    )
                    continue
            else:
                owner_rows = owner_snapshot[1]
                owner_text = snapshot_texts.get(owner_path, "")
            matching = [candidate for candidate in owner_rows if candidate.get("Source Family ID") == family]
            if not matching:
                errors.append(
                    f"Report {path} candidate {family}: Owner Report Ref {owner_value} "
                    "does not contain the Source Family"
                )
            else:
                owner_review_rows: List[Dict[str, str]] = []
                if REVIEW_COMPLETION_MARKER in owner_text:
                    owner_review_rows, _ = _expect_columns(
                        owner_text, REVIEW_COMPLETION_MARKER, REVIEW_COMPLETION_COLUMNS
                    )
                frozen_provenance = {
                    receipt.get("Review Provenance ID", "").strip("`")
                    for receipt in owner_review_rows
                    if receipt.get("Source Family ID", "").strip("`") == family
                    and receipt.get("Completion Result", "")
                    in {"complete", "blocked", "not_required"}
                    and re.fullmatch(
                        r"RP-[a-f0-9]{16}",
                        receipt.get("Review Provenance ID", "").strip("`"),
                    )
                }
                if reconciliation == "earlier_owner_written_back" and not frozen_provenance:
                    errors.append(
                        f"Report {path} candidate {family}: Owner Report Ref {owner_value} "
                        "does not contain frozen review provenance"
                    )
                if reconciliation == "spillback_reference" and not frozen_provenance:
                    errors.append(
                        f"Report {path} candidate {family}: spillback_reference Owner Report Ref "
                        f"{owner_value} does not contain non-pending provenance"
                    )
                if prior_ref not in ABSENT_VALUES and prior_ref not in frozen_provenance:
                    errors.append(
                        f"Report {path} candidate {family}: Owner Report Ref {owner_value} "
                        f"does not contain Prior Review Ref {prior_ref}"
                    )
    return errors


def validate_contract_bundle(root: Path) -> List[str]:
    errors: List[str] = []
    paths = {
        "research": root / "docs" / "RESEARCH_CONTRACT.md",
        "sources": root / "docs" / "RESEARCH_SOURCES.md",
        "reports": root / "docs" / "REPORT_CONTRACTS.md",
        "daily": root / "CODEX_DAILY_RESEARCH_PROMPT.md",
        "historical": root / "CODEX_HISTORICAL_RESEARCH_PROMPT.md",
    }
    texts: Dict[str, str] = {}
    for name, path in paths.items():
        if not path.exists():
            errors.append(f"missing contract file {path.relative_to(root)}")
            continue
        texts[name] = path.read_text(encoding="utf-8")

    for name, text in texts.items():
        errors.extend(f"{paths[name].name}: {error}" for error in validate_markdown_structure(text))
        errors.extend(validate_local_markdown_links(text, paths[name], root))

    if "sources" in texts:
        _, registry_errors = validate_registry_text(texts["sources"])
        errors.extend(registry_errors)
    if "research" in texts:
        for term in ("Design Delta", "System Reach", "Durability"):
            if term not in texts["research"]:
                errors.append(f"docs/RESEARCH_CONTRACT.md is missing Score V2 dimension {term}")
    if "reports" in texts:
        for marker in (
            METADATA_MARKER,
            SOURCE_COVERAGE_MARKER,
            CANDIDATE_LEDGER_MARKER,
            REVIEW_COMPLETION_MARKER,
            DEEP_ANALYSIS_SELECTION_MARKER,
            BOOKS_COMPARISON_MARKER,
            SEMANTIC_AUDIT_MARKER,
            MATERIALS_REQUEST_MARKER,
        ):
            if marker not in texts["reports"]:
                errors.append(f"docs/REPORT_CONTRACTS.md is missing {marker}")
        if not re.search(
            r"^\|\s*Books Gate\s*\|[^\n]*Conditional Pass",
            texts["reports"],
            flags=re.MULTILINE,
        ):
            errors.append("docs/REPORT_CONTRACTS.md Books Gate must publish Conditional Pass")
    required_links = (
        "docs/RESEARCH_CONTRACT.md",
        "docs/RESEARCH_SOURCES.md",
        "docs/REPORT_CONTRACTS.md",
    )
    for name in ("daily", "historical"):
        if name not in texts:
            continue
        for link in required_links:
            if link not in texts[name]:
                errors.append(f"{paths[name].name} must reference {link}")
    return errors


def _iter_markdown(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
    elif path.is_dir():
        yield from sorted(path.rglob("*.md"))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", action="append", type=Path, default=[])
    parser.add_argument("--audit", action="append", type=Path, default=[])
    args = parser.parse_args(argv)

    root = args.root.resolve()
    errors = validate_contract_bundle(root)
    stable_node_ids: Optional[set] = None
    roadmap_path = root / "ROADMAP.md"
    if not roadmap_path.exists():
        errors.append(f"missing ROADMAP node mapping file {roadmap_path}")
    else:
        try:
            roadmap_text = roadmap_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read ROADMAP node mapping file {roadmap_path}: {exc}")
        else:
            stable_node_ids, roadmap_errors = parse_stable_node_ids(roadmap_text)
            errors.extend(roadmap_errors)
    registry: Dict[str, Dict[str, str]] = {}
    registry_path = root / "docs" / "RESEARCH_SOURCES.md"
    if registry_path.exists():
        registry, _ = validate_registry_text(registry_path.read_text(encoding="utf-8"))

    strict_paths = {
        (path if path.is_absolute() else root / path).resolve()
        for path in args.report
    }
    report_paths: List[Path] = list(strict_paths)
    for audit_path in args.audit:
        resolved = audit_path if audit_path.is_absolute() else root / audit_path
        if not resolved.exists():
            errors.append(f"audit path does not exist: {resolved}")
            continue
        discovered = list(_iter_markdown(resolved))
        if not discovered:
            errors.append(f"audit path contains no Markdown reports: {resolved}")
            continue
        report_paths.extend(discovered)
    seen: set = set()
    v2_reports: List[Tuple[Path, str]] = []
    v21_count = 0
    v20_count = 0
    legacy_count = 0
    for path in report_paths:
        path = path.resolve()
        if path in seen:
            continue
        seen.add(path)
        if not path.exists():
            errors.append(f"report path does not exist: {path}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read report path {path}: {exc}")
            continue
        if METADATA_MARKER in text:
            if CANDIDATE_LEDGER_MARKER in text:
                v21_count += 1
            else:
                v20_count += 1
            v2_reports.append((path, text))
            for error in validate_local_markdown_links(text, path, root):
                errors.append(error)
            for error in validate_report_text(
                text,
                registry,
                strict=path in strict_paths,
                stable_node_ids=stable_node_ids,
            ):
                try:
                    display = path.relative_to(root)
                except ValueError:
                    display = path
                errors.append(f"{display}: {error}")
        else:
            legacy_count += 1
            if path in strict_paths:
                for error in validate_report_text(text, registry, strict=True):
                    try:
                        display = path.relative_to(root)
                    except ValueError:
                        display = path
                    errors.append(f"{display}: {error}")

    errors.extend(validate_report_collection(v2_reports, root, registry))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "Schema / consistency validation passed; "
        f"checked {v21_count} V2.1 report(s) and {v20_count} earlier Score V2 report(s); "
        f"legacy skipped: {legacy_count}; semantic completeness not validated for legacy/V2.0. "
        "A validator pass confirms interface consistency, not semantic truth; "
        "V2.1 semantic claims remain attributable to the recorded fresh-context/human auditor."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
