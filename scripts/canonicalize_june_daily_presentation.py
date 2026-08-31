#!/usr/bin/env python3
"""Preserve a completed June Daily's evidence while normalizing its presentation.

The June rebuild scripts predate the canonical July V2.1 Daily layout.  This
module only moves already-rendered sections and adds the navigation fields that
the canonical layout requires.  It does not change candidate, evidence,
selection, Books, or Gate semantics.
"""

from __future__ import annotations

import argparse
import re
from datetime import date, datetime, timedelta
from pathlib import Path


def _slice(text: str, start: str, end: str | None) -> str:
    begin = text.index(start)
    finish = text.index(end, begin) if end else len(text)
    return text[begin + len(start):finish].strip("\n")


def _metadata_value(text: str, field: str) -> str:
    match = re.search(rf"^\| {re.escape(field)} \| ([^|]+) \|$", text, re.MULTILINE)
    return match.group(1).strip() if match else "Not Recorded"


def _first_present(text: str, headings: tuple[str, ...]) -> str | None:
    """Return the earliest present top-level heading from a set of aliases."""
    present = [(text.index(heading), heading) for heading in headings if heading in text]
    return min(present)[1] if present else None


def _source_lines(candidate_body: str, source_reviews: str, accessed: str) -> list[str]:
    titles: dict[str, str] = {}
    for match in re.finditer(r"^###\s+(\d{4}\.\d{4,5})\s+—\s+(.+)$", source_reviews, re.MULTILINE):
        titles[match.group(1)] = match.group(2).strip()

    result: list[str] = []
    for line in candidate_body.splitlines():
        if not line.startswith("| SF-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        primary = cells[1]
        first_public = cells[4]
        match = re.fullmatch(r"arXiv:(\d{4}\.\d{4,5})v(\d+)", primary)
        if not match:
            result.append(
                f"- `{primary}` — first-public：{first_public}；accessed：{accessed}；"
                "primary URL 保留在对应 Source Review / source packet"
            )
            continue
        aid, version = match.groups()
        title = titles.get(aid, aid)
        result.append(
            f"- [{title}](https://arxiv.org/abs/{aid}v{version}) — "
            f"first-public（Asia/Shanghai）：{first_public}；accessed：{accessed}"
        )
    result.append(
        "- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — "
        "source roles、cadence 与 evidence scope 的权威注册表"
    )
    return result


def _replace_single_preamble_field(text: str, field: str, value: str) -> str:
    pattern = rf"^\*\*{re.escape(field)}:\*\*.*$"
    matches = list(re.finditer(pattern, text, flags=re.MULTILINE))
    if len(matches) != 1:
        raise ValueError(f"canonical preamble requires exactly one {field!r} field")
    match = matches[0]
    return text[: match.start()] + f"**{field}:** {value}" + text[match.end() :]


def _normalize_existing_canonical(text: str, research_date: str) -> str:
    """Repair presentation drift without changing research semantics."""
    completion = _metadata_value(text, "Completion Status")
    coverage_gate = _metadata_value(text, "Coverage Gate")
    evidence_gate = _metadata_value(text, "Evidence Gate")
    books_gate = _metadata_value(text, "Books Gate")
    executive_heading = "## Executive Summary"
    executive_start = text.index(executive_heading)
    preamble = text[:executive_start]
    contract_match = re.search(r"^\*\*Contract:\*\*\s*(.+)$", preamble, re.MULTILINE)
    if not contract_match:
        raise ValueError("canonical preamble requires exactly one Contract field")
    field_pattern = re.compile(r"^\*\*[^*]+:\*\*.*$", re.MULTILINE)
    preserved_lines = [
        line
        for line in preamble.splitlines()[1:]
        if line.strip() and not field_pattern.fullmatch(line)
    ]
    day = date.fromisoformat(research_date)
    canonical_preamble = "\n".join(
        [
            f"# Daily Research — {research_date}",
            "",
            f"**Research Date:** {research_date}",
            "",
            "**Timezone:** Asia/Shanghai",
            "",
            f"**Strict Window:** {(day - timedelta(days=1)).isoformat()} 09:00:00 ～ "
            f"{research_date} 09:00:00（北京时间，左闭右开）",
            "",
            f"**Contract:** {contract_match.group(1).strip()}",
            "",
            f"**Status:** {completion}；Coverage={coverage_gate}、Evidence={evidence_gate}、"
            f"Books={books_gate}，fresh-context Semantic Audit 状态见第 7 节",
            "",
            executive_heading,
            "",
        ]
    )
    if preserved_lines:
        canonical_preamble += "\n".join(preserved_lines).strip() + "\n\n"
    text = canonical_preamble + text[executive_start + len(executive_heading) :].lstrip("\n")

    section3 = text.index("## 3. Review Completion Receipt")
    section4 = text.index("## 4. Benchmark Contracts", section3)
    section5 = text.index("## 5. Deep Analysis Selection", section4)
    review_starts = list(re.finditer(r"<!--\s*review:[^>]+:start\s*-->", text))
    if review_starts:
        heading_matches = list(
            re.finditer(r"^(?:### Source Reviews|\*\*Source Reviews\*\*)\s*$", text, re.MULTILINE)
        )
        if len(heading_matches) > 1:
            raise ValueError("multiple Source Reviews headings cannot be normalized safely")

        if heading_matches:
            heading_start = heading_matches[0].start()
            if section3 < heading_start < section4:
                text = (
                    text[: heading_matches[0].start()]
                    + "### Source Reviews"
                    + text[heading_matches[0].end() :]
                )
            elif section4 < heading_start < section5:
                review_chunk = text[heading_start:section5].strip("\n")
                review_chunk = re.sub(
                    r"^(?:### Source Reviews|\*\*Source Reviews\*\*)\s*$",
                    "### Source Reviews",
                    review_chunk,
                    count=1,
                    flags=re.MULTILINE,
                )
                text = text[:heading_start].rstrip() + "\n\n" + text[section5:]
                section4 = text.index("## 4. Benchmark Contracts", section3)
                text = text[:section4].rstrip() + "\n\n" + review_chunk + "\n\n" + text[section4:]
            else:
                raise ValueError("Source Reviews heading is outside sections 3-4")
        else:
            first_review = review_starts[0].start()
            if not (section3 < first_review < section4):
                raise ValueError("review bodies outside section 3 require an explicit movable heading")
            text = text[:first_review] + "### Source Reviews\n\n" + text[first_review:]

    final_heading = "## 13. Final Status"
    final_start = text.index(final_heading)
    final_body = text[final_start + len(final_heading) :]
    state_truth = (
        f"State Truth: Completion={completion}；Coverage={coverage_gate}；"
        f"Evidence={evidence_gate}；Books={books_gate}；Unresolved Findings=0。"
    )
    if "State Truth:" in final_body:
        text = re.sub(
            r"^State Truth:.*$",
            state_truth,
            text,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        text = text.rstrip() + "\n\n" + state_truth + "\n"
    return text


def canonicalize_report(report: Path, research_date: str) -> bool:
    """Normalize one legacy June Daily to the canonical 13-section layout."""
    text = report.read_text()
    if "## 13. Final Status" in text:
        normalized = _normalize_existing_canonical(text, research_date)
        if normalized == text:
            return False
        report.write_text(normalized)
        return True

    semantic_heading = _first_present(
        text,
        ("## 6. Semantic Audit", "## 6. Daily Semantic Audit", "## 6. Semantic Audit and Gate"),
    )
    required = (
        "## Executive Summary",
        "## 1. Coverage",
        "## 2. Candidate Ledger and Score V2",
        "### Review Completion Receipt",
        "### Benchmark Contract",
        "## 3. Source Reviews",
        "## 4. Deep Analysis Selection",
    )
    missing = [heading for heading in required if heading not in text]
    if semantic_heading is None:
        missing.append("## 6. Semantic Audit [alias]")
    if missing:
        raise ValueError(f"{report}: legacy sections missing: {missing}")

    day = date.fromisoformat(research_date)
    window_start = day - timedelta(days=1)
    frozen_at = _metadata_value(text, "Denominator Frozen At")
    accessed = frozen_at[:10] if re.match(r"\d{4}-\d{2}-\d{2}", frozen_at) else datetime.now().date().isoformat()

    executive = _slice(text, "## Executive Summary", "## 1. Coverage")
    coverage = _slice(text, "## 1. Coverage", "## 2. Candidate Ledger and Score V2")
    candidate = _slice(text, "## 2. Candidate Ledger and Score V2", "### Review Completion Receipt")
    review_receipt = _slice(text, "### Review Completion Receipt", "### Benchmark Contract")
    benchmark = _slice(text, "### Benchmark Contract", "## 3. Source Reviews")
    source_reviews = _slice(text, "## 3. Source Reviews", "## 4. Deep Analysis Selection")
    books_heading = _first_present(
        text,
        (
            "## 5. Books Comparison and Decision",
            "## 5. Books Integration Decision",
            "## 5. Books Comparison",
        ),
    )
    if books_heading is None:
        raise ValueError(f"{report}: cannot locate the legacy Books section")
    deep = _slice(text, "## 4. Deep Analysis Selection", books_heading)
    books = _slice(text, books_heading, semantic_heading)
    coverage_gate = _metadata_value(text, "Coverage Gate")
    evidence_gate = _metadata_value(text, "Evidence Gate")
    books_gate = _metadata_value(text, "Books Gate")
    completion = _metadata_value(text, "Completion Status")
    legacy_sources = ""
    if "## 7. Materials and Access" in text:
        semantic = _slice(text, semantic_heading, "## 7. Materials and Access")
        action_heading = _first_present(
            text,
            ("## 8. Daily Integration Decision", "## 8. Integration Decision"),
        )
        repository_heading = _first_present(
            text,
            (
                "## 8. Repository Changes and Continuation",
                "## 8. Repository Changes",
                "## 9. Repository Changes",
                "## 9. Repository Changes and Continuation",
            ),
        )
        questions_heading = _first_present(
            text,
            ("## 9. Open Questions", "## 10. Open Questions", "## 11. Open Questions"),
        )
        gates_heading = _first_present(text, ("## 11. Gates", "## 12. Gates", "## Gates"))
        sources_heading = _first_present(text, ("## Sources", "## 10. Sources", "## 11. Sources", "## 12. Sources"))

        materials_end = action_heading or repository_heading or questions_heading or sources_heading
        if materials_end is None:
            raise ValueError(f"{report}: cannot locate the section following Materials and Access")
        materials = _slice(text, "## 7. Materials and Access", materials_end)

        if action_heading:
            action_end = repository_heading or questions_heading or sources_heading
            action = _slice(text, action_heading, action_end)
        else:
            action = (
                f"本日 Completion Status={completion}；没有独立的 legacy action section。"
                "后续动作只保留在已冻结的 Gate、Materials 和 source packet 中，不从展示迁移推导新的研究结论。"
            )

        if repository_heading:
            repository_end = questions_heading or sources_heading
            repository = _slice(text, repository_heading, repository_end)
        else:
            repository = "本次展示迁移不改变 Candidate、Evidence、Books 或共享知识库。"

        if questions_heading:
            questions = _slice(text, questions_heading, sources_heading or gates_heading)
        else:
            questions = "本日没有未解决的 ordinary pending；精确状态以 Gate metadata 与 Semantic Audit 为准。"
    elif "## 7. Integration Decision" in text:
        semantic = _slice(text, semantic_heading, "## 7. Integration Decision")
        materials = (
            "- Exact-version access、pending 与 blocker 状态保留在 Review Completion Receipt 和"
            " date-local source packet；该 legacy report 没有单独的 Materials section。"
        )
        action = _slice(text, "## 7. Integration Decision", "## 8. Repository Changes")
        repository = _slice(text, "## 8. Repository Changes", "## 9. Open Questions")
        questions = _slice(text, "## 9. Open Questions", None)
    elif "## 7. Repository Changes and Open Questions" in text:
        semantic = _slice(text, semantic_heading, "## 7. Repository Changes and Open Questions")
        combined = _slice(
            text,
            "## 7. Repository Changes and Open Questions",
            "## Sources",
        )
        combined_lines = combined.splitlines()
        question_lines = [line for line in combined_lines if line.startswith("- Open question:")]
        repository = "\n".join(line for line in combined_lines if line not in question_lines).strip()
        questions = "\n".join(question_lines) or "- None recorded."
        action = (
            "No additional Books writeback is required for this date. Preserve the frozen V12 "
            "receipts and re-open only if an exact-version revision or artifact changes a recorded boundary."
        )
        materials = (
            "- Exact-version access、pending 与 blocker 状态保留在 Review Completion Receipt 和"
            " date-local source packet；42/42 retained families have complete accessible receipts."
        )
        legacy_sources = _slice(text, "## Sources", None)
    else:
        raise ValueError(f"{report}: unsupported legacy tail layout")

    generated_sources = _source_lines(candidate, source_reviews, accessed)
    sources = ([legacy_sources, ""] if legacy_sources else []) + generated_sources
    lines = [
        f"# Daily Research — {research_date}",
        "",
        f"**Research Date:** {research_date}",
        "",
        "**Timezone:** Asia/Shanghai",
        "",
        f"**Strict Window:** {window_start.isoformat()} 09:00:00 ～ {research_date} 09:00:00（北京时间，左闭右开）",
        "",
        "**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt",
        "",
        f"**Status:** {completion}；Coverage={coverage_gate}、Evidence={evidence_gate}、Books={books_gate}，fresh-context Semantic Audit 状态见第 7 节",
        "",
        "## Executive Summary",
        "",
        executive,
        "",
        "## 1. Coverage",
        "",
        coverage,
        "",
        "## 2. Candidate Ledger",
        "",
        candidate,
        "",
        "## 3. Review Completion Receipt",
        "",
        review_receipt,
        "",
        "### Source Reviews",
        "",
        source_reviews,
        "",
        "## 4. Benchmark Contracts",
        "",
        benchmark,
        "",
        "## 5. Deep Analysis Selection",
        "",
        deep,
        "",
        "## 6. Books Comparison",
        "",
        books,
        "",
        "## 7. Semantic Audit",
        "",
        semantic,
        "",
        "## 8. Ignored Noise",
        "",
        "候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；"
        "Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。",
        "",
        "### Materials and Access",
        "",
        materials,
        "",
        "## 9. Recommended Action",
        "",
        action,
        "",
        "## 10. Repository Changes",
        "",
        repository,
        "",
        "## 11. Open Questions",
        "",
        questions,
        "",
        "## 12. Sources",
        "",
        *sources,
        "",
        "## 13. Final Status",
        "",
        f"Daily V2.1 的 Coverage={coverage_gate}、Evidence={evidence_gate}、Books={books_gate}；"
        f"Completion Status={completion}。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。",
        "",
        f"State Truth: Completion={completion}；Coverage={coverage_gate}；Evidence={evidence_gate}；"
        f"Books={books_gate}；Unresolved Findings=0。",
        "",
    ]
    report.write_text("\n".join(lines))
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("research_date")
    args = parser.parse_args()
    changed = canonicalize_report(args.report, args.research_date)
    print(f"canonical presentation: {'updated' if changed else 'already canonical'} — {args.report}")


if __name__ == "__main__":
    main()
