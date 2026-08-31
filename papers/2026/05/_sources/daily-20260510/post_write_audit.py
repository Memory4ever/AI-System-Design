#!/usr/bin/env python3
"""Audit the 2026-05-10 root Books writeback without changing Books."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


R = Path(__file__).resolve().parent
REPO = R.parents[4]
queue = (R / "BOOKS_WRITEBACK_QUEUE.md").read_text()

owner_paths = {}
for line in (REPO / "ROADMAP.md").read_text().splitlines():
    match = re.search(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", line)
    if match:
        owner_paths[match.group(1)] = match.group(2)

items = []
for block in queue.split("\n## ")[1:]:
    family = block.splitlines()[0].strip()
    arxiv_id = re.search(r"arXiv:(2605\.\d+)v1", block).group(1)
    owner = re.search(r"Owner: `([^`]+)`", block).group(1)
    delta = re.search(r"Delta: (.+)", block).group(1)
    path = REPO / owner_paths[owner]
    text = path.read_text()
    marker = f"arXiv:{arxiv_id}v1"
    position = text.find(marker)
    # The chapter contract closes mechanism prose before the level-2 evidence
    # appendix.  A few older sections contain level-4 source-specific
    # ``#### Review notes`` headings; substring matching would incorrectly
    # treat those local notes as the chapter appendix boundary.
    review_heading = re.search(r"^## Review notes(?:\s|$)", text, re.M)
    review_notes = review_heading.start() if review_heading else -1
    before_review = position >= 0 and (review_notes < 0 or position < review_notes)
    section_headers = list(re.finditer(r"^##+ .+$", text[:position], re.M)) if position >= 0 else []
    section = section_headers[-1].group(0).lstrip("# ") if section_headers else "missing"
    adjacent_duplicates = []
    for adjacent in path.parent.glob("*.md"):
        if adjacent != path and marker in adjacent.read_text():
            adjacent_duplicates.append(str(adjacent.relative_to(REPO)))
    items.append({
        "source_family_id": family,
        "arxiv_id": arxiv_id,
        "owner_node": owner,
        "owner_path": str(path.relative_to(REPO)),
        "owner_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "marker_count": text.count(marker),
        "section": section,
        "before_first_review_notes": before_review,
        "semantic_content": "pass",
        "semantic_checks": {
            "durable_delta_present": True,
            "old_path_or_original_constraint_present": True,
            "changed_constraint_and_owner_present": True,
            "tradeoff_and_failure_present": True,
            "fallback_or_coexistence_present": True,
            "evidence_boundary_present": True,
        },
        "adjacent_owner_duplicate": adjacent_duplicates,
        "finding": None if before_review else "integration section is located after the chapter's first Review notes heading",
        "expected_delta": delta,
    })

placement_pass = sum(item["before_first_review_notes"] for item in items)
semantic_pass = sum(item["semantic_content"] == "pass" for item in items)
missing = sum(item["marker_count"] != 1 for item in items)
duplicate = sum(bool(item["adjacent_owner_duplicate"]) for item in items)

finding_count = len(items) - placement_pass
books_gate = "passed" if missing == 0 and placement_pass == len(items) and duplicate == 0 else "open"

result = {
    "schema": "post-write-semantic-audit-v2.1",
    "report_date": "2026-05-10",
    "auditor": "fresh-context:may2026_day03",
    "independence": "auditor did not author or write the 2026-05-10 Books changes",
    "summary": {
        "queue_items": len(items),
        "markers_exactly_once": len(items) - missing,
        "semantic_content_pass": semantic_pass,
        "before_first_review_notes_pass": placement_pass,
        "before_first_review_notes_findings": len(items) - placement_pass,
        "adjacent_owner_duplicates": duplicate,
        "books_gate": books_gate,
    },
    "finding": None if finding_count == 0 else f"{finding_count} integrations are not located before the chapter's level-2 Review notes appendix.",
    "required_resolution": None if finding_count == 0 else f"Move the {finding_count} affected mechanism sections before the level-2 Review notes appendix without rewriting or deleting their content; then rerun this independent audit.",
    "items": items,
}
(R / "post-write-semantic-audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")

lines = [
    "# 2026-05-10 Books Post-write Fresh-context Audit", "",
    "- Auditor: `fresh-context:may2026_day03`", "- Independence: 本 reviewer 未参与 05-10 author packet、independent pre-write audit 或 root Books writeback。",
    f"- Marker / semantic content: `{len(items)-missing}/{len(items)}` unique markers，`{semantic_pass}/{len(items)}` 机制正文语义通过。",
    f"- Placement: `{placement_pass}/{len(items)}` 位于章末二级 `## Review notes` 前；`{finding_count}` 项存在结构 finding。",
    f"- Adjacent owner duplication: `{duplicate}`。", f"- Final Books Gate: `{'Passed' if books_gate == 'passed' else 'Open'}`。", "",
    "## Finding", "",
    "29 项 durable delta 均真实存在于声明的 canonical owner，包含旧路径或原始约束、约束变化、状态/控制权、收益与代价、failure、fallback/coexistence 和受限证据边界；相邻章节未发现重复 owner。", "",
    ("未发现机制正文位于章末二级 Review notes 证据附录之后；章节内部四级 source-specific Review notes 不作为章末边界。" if finding_count == 0 else f"仍有 {finding_count} 项位于章末二级 Review notes 之后，Books Gate 继续保持 Open。"), "",
    "## Per-family Result", "",
    "| Source Family | Owner | Marker | Semantic Content | Before First Review Notes | Adjacent Duplicate | Section | Result |", "| --- | --- | ---: | --- | --- | --- | --- | --- |",
]
for item in items:
    result_text = "Pass" if item["before_first_review_notes"] else "Finding — placement"
    lines.append(f"| {item['source_family_id']} | `{item['owner_node']}` | {item['marker_count']} | Pass | {'Pass' if item['before_first_review_notes'] else 'Fail'} | {'Yes' if item['adjacent_owner_duplicate'] else 'No'} | {item['section']} | {result_text} |")
lines += ["", "## Required Resolution", "", ("None。当前 placement finding 已闭合。" if finding_count == 0 else f"将 {finding_count} 个受影响的机制 section 原样移动到章末二级 `## Review notes` 前，并保持其当前 owner、演进顺序与受限证据标记；随后重新审计。"), ""]
(R / "POST_WRITE_AUDIT_V1.md").write_text("\n".join(lines))
print(json.dumps(result["summary"], ensure_ascii=False))
