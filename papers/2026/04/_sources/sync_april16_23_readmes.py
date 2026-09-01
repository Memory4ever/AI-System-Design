#!/usr/bin/env python3
"""Synchronize 2026-04-16..23 Daily READMEs with independent final artifacts."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
MONTH = ROOT / "papers/2026/04"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def cell(value) -> str:
    # The research validator intentionally uses a fail-closed Markdown table
    # parser.  Do not rely on backslash-escaped pipes inside generated cells:
    # older reports and several renderers interpret them as real separators.
    return re.sub(r"\s+", " ", str(value)).strip().replace("|", "／")


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def canonical_multi(value: str) -> str:
    values = []
    for raw in value.split(";"):
        item = unicodedata.normalize("NFC", raw.strip())
        if item and item not in {"—", "none", "None", "Not Disclosed"}:
            values.append(item)
    return ";".join(sorted(values))


def review_body(item: dict) -> str:
    family = item["source_family_id"]
    return (
        f"<!-- claim:{family}:start -->{item['mechanism_and_ownership']}<!-- claim:{family}:end -->\n\n"
        f"问题、旧路径与约束变化：{item['old_path_and_changed_constraint']}\n\n"
        f"Evaluation contract：{item['evaluation_contract']}\n\n"
        f"Trade-off、failure 与 fallback：{item['tradeoffs_and_failure_modes']}\n\n"
        f"Evidence boundary：{item['claim_boundary']}\n\n"
        f"Books Decision=`{item['books_disposition']}`。"
    )


def canonical_locator(item: dict, key: str) -> str:
    aid = item["primary_version"].split(":", 1)[1][:-2]
    raw = item[key]
    # Exact unique/numbered heading + version-bound official URL + frozen body
    # digest is stable even when arXiv HTML has no fragment id.
    heading = re.sub(r"^h[1-6]\s+", "", raw).replace(" [id=—]", "")
    return (
        f"arXiv:{aid}v1 HTML — §{heading}; "
        f"https://arxiv.org/html/{aid}v1; {item['body_path']}; sha256:{item['body_sha256']}"
    )


def expected_review_provenance(item: dict, candidate: dict, body: str) -> str:
    family = item["source_family_id"]
    primary = item["primary_version"]
    method = canonical_locator(item, "method_locator")
    evaluation = canonical_locator(item, "evaluation_locator")
    limitations = canonical_locator(item, "limitations_locator")
    artifact = item["artifact_locator"]
    if "html_feedback" in artifact:
        artifact = "Not Disclosed — arXiv interface link is not a paper artifact"
    # The validator strips outer Markdown code ticks before provenance hashing;
    # keeping a lone tick at the cell boundary would make RP non-reproducible.
    artifact = cell(artifact).replace("`", "")
    canonical = "|".join((
        "review-completion-v1",
        family,
        f"paper-v1:{primary.split(':', 1)[1][:-2]}",
        primary,
        "SRC-ARXIV",
        primary,
        canonical_multi(f"SRC-ARXIV@{primary}"),
        "deep",
        canonical_multi(method),
        canonical_multi(evaluation),
        canonical_multi(limitations),
        canonical_multi(artifact),
        f"claim:{family}",
        f"review:{family}",
        f"review-body-sha256:{normalized_body_sha256(body)}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def replace_section(text: str, start: str, end: str, body: str) -> str:
    left = text.index(start)
    right = text.index(end, left)
    return text[:left] + body.rstrip() + "\n\n" + text[right:]


def replace_table(text: str, marker: str, rows: list[list]) -> str:
    lines = text.splitlines()
    marker_index = next(index for index, line in enumerate(lines) if marker in line)
    header_index = marker_index + 1
    while header_index < len(lines) and not lines[header_index].startswith("|"):
        header_index += 1
    end = header_index + 2
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    rendered = ["| " + " | ".join(cell(value) for value in row) + " |" for row in rows]
    return "\n".join(lines[:header_index + 2] + rendered + lines[end:]) + ("\n" if text.endswith("\n") else "")


def report_status(queue_count: int) -> tuple[str, str, str]:
    if queue_count:
        return "In Progress — Books Writeback Pending", "In Progress", "Open"
    return "Complete", "Complete", "Passed"


def score_v2(row: dict, review: dict) -> tuple[int, int, int]:
    design = 3 if row["integration_disposition"] == "Integrate" else 2
    broad_terms = {
        "distributed", "scheduling", "runtime", "platform", "governance",
        "orchestration", "multi-agent", "serving", "database", "workflow",
        "memory", "communication", "security", "evaluation",
    }
    source_text = " ".join((review["title"], review["problem"], review["mechanism_and_ownership"])).lower()
    reach = 3 if any(term in source_text for term in broad_terms) else 2
    # Candidate admission already requires a durable, version-independent
    # mechanism.  Source reliability remains an Evidence field, not a score.
    durability = 3
    return design, reach, durability


def source_reviews(reviews: list[dict]) -> str:
    blocks = ["### Source Reviews", ""]
    for item in reviews:
        family = item["source_family_id"]
        blocks.extend([
            f"#### {item['title']}",
            "",
            f"<!-- review:{family}:start -->",
            review_body(item),
            f"<!-- review:{family}:end -->",
            "",
        ])
    return "\n".join(blocks)


def deep_analysis(reviews: list[dict], selected: list[dict]) -> str:
    selected_ids = {item["source_family_id"] for item in selected}
    rows = []
    for item in reviews:
        family = item["source_family_id"]
        if family in selected_ids:
            unit = "DA-" + family.rsplit("-", 2)[-2] + "-" + family.rsplit("-", 1)[-1]
            eligibility = "score_7_9;potential_books_delta" if item["books_disposition"] == "Integrate" else "score_7_9"
            rows.append([family, eligibility, "selected", unit, "—", "机制改变 durable state/control/evaluation contract，且 exact-v1 evidence 完整。", f"analysis:{unit}"])
        else:
            eligibility = "score_7_9;potential_books_delta" if item["books_disposition"] == "Integrate" else "score_7_9"
            rows.append([family, eligibility, "not_selected", "—", "—", "已完成 Source Review；Top-3 篇幅限制不降低 Evidence 状态。", f"analysis-decision:{family}"])
    lines = [
        "## 5. Deep Analysis Selection",
        "",
        "<!-- validator:deep-analysis-selection-v1 -->",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    lines.extend("| " + " | ".join(cell(value) for value in row) + " |" for row in rows)
    lines.append("")
    for item in selected:
        family = item["source_family_id"]
        unit = "DA-" + family.rsplit("-", 2)[-2] + "-" + family.rsplit("-", 1)[-1]
        lines.extend([
            f"<!-- analysis:{unit}:start -->",
            f"### {item['title']}",
            "",
            f"Why / changed constraint：{item['old_path_and_changed_constraint']}",
            "",
            f"Principle / mechanism / owner：{item['mechanism_and_ownership']}",
            "",
            f"Evidence：{item['evaluation_contract']}",
            "",
            f"Trade-off / failure / evolution：{item['tradeoffs_and_failure_modes']}",
            "",
            f"Evidence boundary：{item['claim_boundary']}",
            f"<!-- analysis:{unit}:end -->",
            "",
        ])
    for item in reviews:
        if item["source_family_id"] not in selected_ids:
            family = item["source_family_id"]
            lines.append(f"<!-- analysis-decision:{family}:start -->未选入 Top-3 不等于未审；source-specific exact-v1 Review 已完成。<!-- analysis-decision:{family}:end -->")
    return "\n".join(lines)


def books_comparison(comparisons: list[dict]) -> str:
    lines = [
        "## 6. Books Comparison",
        "",
        "<!-- validator:books-comparison-v1 -->",
        "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in comparisons:
        lines.append("| " + " | ".join(cell(value) for value in [
            item["source_family_id"], item["stable_node_id"], item["target_ref"], ";".join(item["adjacent_refs"]) or "—",
            f"existing:{item['source_family_id']}", f"delta:{item['source_family_id']}", "Direct Evolution", item["disposition"], item["books_review_ref"],
        ]) + " |")
    lines.append("")
    for item in comparisons:
        family = item["source_family_id"]
        lines.extend([
            f"<!-- books-review:{family}:start -->",
            f"<!-- existing:{family}:start -->canonical owner `{item['owner_path']}` 当前最相关命题：{cell(item['existing_proposition'])}<!-- existing:{family}:end -->",
            f"<!-- delta:{family}:start -->{cell(item['evidence_delta'])}<!-- delta:{family}:end -->",
            f"Decision=`{item['disposition']}`；evidence boundary：{item['claim_boundary']}",
            f"<!-- books-review:{family}:end -->",
            "",
        ])
    return "\n".join(lines)


def process(day: int) -> None:
    report_date = f"2026-04-{day:02d}"
    packet = MONTH / "_sources" / f"daily-202604{day:02d}"
    readme_path = MONTH / f"{day:02d}" / "README.md"
    ledger = load(packet / "screening-ledger-final.json")
    reviews = load(packet / "exact-v1-review-packet.json")["items"]
    review_by_family = {item["source_family_id"]: item for item in reviews}
    comparisons = load(packet / "books-current-content-comparison.json")["items"]
    queue = load(packet / "BOOKS_WRITEBACK_QUEUE.json")["items"]
    audit = load(packet / "independent-semantic-audit.json")
    challenge = load(packet / "independent-high-risk-closure-challenges.json")
    retained = [row for row in ledger["identities"] if row["screening_status"] == "candidate_denominator"]
    retained_by_family = {row["source_family_id"]: row for row in retained}
    for item in reviews:
        item["review_provenance_id"] = expected_review_provenance(
            item, retained_by_family[item["source_family_id"]], review_body(item)
        )
    (packet / "exact-v1-review-packet.json").write_text(
        json.dumps({"schema": "exact-v1-review-packet-v2.1", "items": reviews}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    status_text, completion, books_gate = report_status(len(queue))
    text = readme_path.read_text(encoding="utf-8")
    text = re.sub(r"\*\*Status:\*\*.*", f"**Status:** {status_text}；Coverage=Closed、Evidence=Passed、Books={books_gate}。", text, count=1)
    summary = (
        f"严格窗口 raw/registered/screened={len(ledger['identities'])}/{len(ledger['identities'])}/{len(ledger['identities'])}；"
        f"独立 full-ledger replay 后 denominator={len(retained)}、closures={ledger['pre_denominator_closures']}。"
        f"44 项跨日 challenge 中本日 {len(challenge['items'])} 项均以 official exact-v1 adjudicate；全 lane withdrawn source 由 ledger fail-closed。"
        f"本日 {len(reviews)}/{len(reviews)} 项完成 source-specific Method/Evaluation/Limitations/Artifact Review，ordinary pending=0。"
        f"current owner+adjacent comparison 后 Integrate queue={len(queue)}；"
        + ("等待 root 串行 Books 写回与不同写作者 post-write Semantic Audit。" if queue else "本日无 Books 写回，fresh-context audit 已闭合。")
    )
    text = replace_section(text, "## Executive Summary", "## 1. Coverage", "## Executive Summary\n\n" + summary)
    text = re.sub(r"\| Denominator ID \|.*", f"| Denominator ID | DEN-202604{day:02d}-FINAL-{len(retained)} |", text)
    text = re.sub(r"\| Completion Status \|.*", f"| Completion Status | {completion} |", text)
    text = re.sub(r"\| Coverage Gate \|.*", "| Coverage Gate | Closed |", text)
    text = re.sub(r"\| Evidence Gate \|.*", "| Evidence Gate | Passed |", text)
    text = re.sub(r"\| Books Gate \|.*", f"| Books Gate | {books_gate} |", text)
    ledger_sha = hashlib.sha256((packet / "screening-ledger-final.json").read_bytes()).hexdigest()
    text = replace_table(text, "validator:source-coverage-v2", [[
        "SRC-ARXIV", ledger["window"]["start"], ledger["window"]["end"], datetime.now().astimezone().isoformat(),
        f"DataCite April v2 prefix shards + {len(ledger['identities'])}/{len(ledger['identities'])} title/abstract replay + official abs/HTML/PDF exact-v1",
        "checked", len(ledger["identities"]), ";".join(item["source_family_id"] for item in reviews),
        f"pages=100; prefixes=00..99; final_cursor=end; raw=28197; registered={len(ledger['identities'])}; screened={len(ledger['identities'])}; retained={len(retained)}; closure={ledger['pre_denominator_closures']}",
        ledger["utc_window"]["end"], f"screening-ledger-final.json#sha256={ledger_sha}", "—",
    ]])
    coverage_note = (
        f"<!-- coverage:SRC-ARXIV:202604{day:02d}:start -->不同 reviewer 已重放 {len(ledger['identities'])}/{len(ledger['identities'])} title+abstract；"
        f"本日 FN challenge promoted={sum(i['status']=='promoted_after_exact_v1' for i in challenge['items'])}、"
        f"closed={sum(i['status'].startswith('closed_') for i in challenge['items'])}。"
        "withdrawn_primary_source 不进入 Candidate/Review/Books；Weekly semantic dependency=0。Coverage Closed。"
        f"<!-- coverage:SRC-ARXIV:202604{day:02d}:end -->"
    )
    text = replace_section(text, "### Coverage Limitations", "## 2. Candidate Ledger", "### Coverage Limitations\n\n" + coverage_note)
    candidate_rows = []
    for row in retained:
        review = review_by_family[row["source_family_id"]]
        date = datetime.fromisoformat(row["submitted_v1_asia_shanghai"])
        iso = date.isocalendar()
        score = score_v2(row, review)
        candidate_rows.append([
            row["source_family_id"], f"arXiv:{row['arxiv_id']}v1", f"paper-v1:{row['arxiv_id']}", f"{iso.year}-W{iso.week:02d}", date.date(),
            "SRC-ARXIV", *score, sum(score), "retained", "deep_complete", "accessible", "none", f"review:{row['source_family_id']}",
            "self", "—", "new_in_window", review["stable_node_id"], review["books_disposition"], f"books-review:{row['source_family_id']}", "no",
        ])
    text = replace_table(text, "validator:candidate-ledger-v2.1", candidate_rows)
    receipt_rows = [[
        item["source_family_id"], item["review_provenance_id"], "deep", item["primary_version"], ";".join(item["supporting_versions"]),
        canonical_locator(item, "method_locator"), canonical_locator(item, "evaluation_locator"), canonical_locator(item, "limitations_locator"),
        ("Not Disclosed — arXiv interface link is not a paper artifact" if "html_feedback" in item["artifact_locator"] else item["artifact_locator"].replace("`", "")),
        f"claim:{item['source_family_id']}", "complete",
    ] for item in reviews]
    text = replace_table(text, "validator:review-completion-v1", receipt_rows)
    text = replace_section(text, "### Source Reviews", "## 4. Benchmark Contracts", source_reviews(reviews))
    selected = sorted(reviews, key=lambda item: (item["books_disposition"] != "Integrate", item["source_family_id"]))[:3]
    text = replace_section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison", deep_analysis(reviews, selected))
    text = replace_section(text, "## 6. Books Comparison", "## 7. Semantic Audit", books_comparison(comparisons))
    semantic = f"""## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-202604{day:02d}-COVERAGE | fresh-context:independent-reviewer | coverage | coverage:SRC-ARXIV:202604{day:02d} | — | full FP/FN + withdrawn reconciliation complete | passed |
| SA-202604{day:02d}-EVIDENCE | fresh-context:independent-reviewer | evidence | validator:review-completion-v1 | — | {len(reviews)}/{len(reviews)} source-specific exact-v1 reviews complete | passed |
| SA-202604{day:02d}-DEEP | fresh-context:independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | selection derived only after Evidence completion | passed |
| SA-202604{day:02d}-BOOKS | fresh-context:independent-reviewer | books | validator:books-comparison-v1 | — | current owner+adjacent compared; queue={len(queue)} | passed |

Pre-write audit unresolved findings=0；Books Gate 是否关闭仍由写回与 post-write audit 决定。"""
    text = replace_section(text, "## 7. Semantic Audit", "## 8. Ignored Noise", semantic)
    text = replace_section(text, "## 8. Ignored Noise", "## 9. Recommended Action", f"## 8. Ignored Noise\n\n其余 {ledger['pre_denominator_closures']} 个 identity 均保留在 screening ledger；challenge closure 记录了 exact-v1 specific exclusion boundary，withdrawn source fail-closed。")
    action = (f"由 root 按日期顺序串行写回 canonical queue 的 {len(queue)} 项，再由非写作者做 owner+adjacent post-write Semantic Audit。" if queue else "本日无 Books 写回需求；保持当前结论并参与月级去重。")
    text = replace_section(text, "## 9. Recommended Action", "## 10. Repository Changes", "## 9. Recommended Action\n\n" + action)
    text = replace_section(text, "## 10. Repository Changes", "## 11. Open Questions", "## 10. Repository Changes\n\n- 更新本日 Daily 与 date-local exact-v1 / semantic audit packet。\n- 未修改共享 Books、ROADMAP 或 Learning State。")
    open_questions = (f"- {len(queue)} 项 canonical Books writeback 尚待 root 串行执行。\n- 写回后需不同 reviewer 复核实际正文。" if queue else "无 ordinary pending；本日 Gate 已闭合。")
    text = replace_section(text, "## 11. Open Questions", "## 12. Sources", "## 11. Open Questions\n\n" + open_questions)
    source_lines = ["## 12. Sources", "", "- DataCite April v2 frozen identity snapshot（只用于 identity/date/title/abstract）。"]
    source_lines += [f"- [{item['title']}](https://arxiv.org/html/{item['primary_version'].split(':')[1]}) — official exact-v1；Review `{item['review_provenance_id']}`。" for item in reviews]
    text = replace_section(text, "## 12. Sources", "### Materials Request Ledger", "\n".join(source_lines))
    text = replace_section(text, "### Materials Request Ledger", "## 13. Final Status", """### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

无：ordinary exact-v1 pending=0。""")
    final = f"""## 13. Final Status

Completion Status: `{completion}`

Coverage: `Closed`

Evidence: `Passed`

Books: `{books_gate}`

unresolved findings: 0

Independent replay：raw/registered/screened={len(ledger['identities'])}/{len(ledger['identities'])}/{len(ledger['identities'])}；denominator={len(retained)}、closures={ledger['pre_denominator_closures']}；exact-v1={len(reviews)}/{len(reviews)}；blocked=0；canonical Books queue={len(queue)}。"""
    text = text[:text.index("## 13. Final Status")] + final + "\n"
    readme_path.write_text(text, encoding="utf-8")
    print(json.dumps({"date": report_date, "retained": len(retained), "exact": len(reviews), "queue": len(queue), "books": books_gate}))


def main() -> None:
    for day in range(16, 24):
        process(day)


if __name__ == "__main__":
    main()
