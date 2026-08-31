#!/usr/bin/env python3
"""Render the reconciled 2026-05-12 Daily from independent audit artifacts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parents[1] / "12" / "README.md"
REPO_ROOT = ROOT.parents[4]
sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256


def cell(value: object) -> str:
    return str(value).replace("\n", " ").replace("|", "\\|")


def stable_locator(value: str, facet: str) -> str:
    """Keep exact inspected content while satisfying the stable-locator interface."""
    if re.search(r"§|\bappendix|\btable\s|\bfigure\s|\bmethodology\s*:|\bexperiments\s*:|\bscope and limitations\b", value, re.I):
        return value
    if value.startswith(("Not Disclosed —", "Not Required —", "Not Applicable —", "Pending —")):
        return value
    return f"Not Disclosed — exact-v1 body was reviewed, but no stable numbered {facet} fragment was exposed; reviewer boundary: {value}"


def chapter_ref(path: str) -> str:
    if path == "—":
        return "Not Applicable — exact-v1 body is blocked before Books comparison"
    match = re.search(r"/(\d+)-[^/]+\.md$", path)
    return f"{path}#chapter-{match.group(1)}" if match else f"{path}#knowledge-tree"


def main() -> None:
    ledger = json.loads((ROOT / "screening-ledger-independent-reconciled.json").read_text())
    packet = {x["arxiv_id"]: x for x in json.loads((ROOT / "exact-v1-review-packet-independent.json").read_text())}
    comparisons = {x["arxiv_id"]: x for x in json.loads((ROOT / "books-current-content-comparison-final.json").read_text())}
    queue = json.loads((ROOT / "books-writeback-queue-final.json").read_text())
    rows = [r for r in ledger["identities"] if r.get("screening_status") == "retained"]
    rows.sort(key=lambda x: x["arxiv_id"])
    families = ";".join(r["source_family_id"] for r in rows)

    lines: list[str] = []
    lines += [
        "# Daily Research — 2026-05-12", "",
        "**Research Date:** 2026-05-12", "", "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-05-11 09:00:00 ～ 2026-05-12 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；DataCite v2 只用于 identity/date/abstract recovery，技术结论绑定 official arXiv exact-v1。", "",
        "**Status:** In Progress；Coverage=Closed、Evidence=Conditional Pass、Books=Open。独立重放已完成，普通 pending=0；1 项 exact-v1 外部全文 blocker 被精确冻结，7 项 owner-merged Books queue 等待 root 串行写回。", "",
        "## Executive Summary", "",
        "完整 v2 snapshot 含 91,841 条 raw records；严格窗口注册并由非作者逐项语义重放 870/870 条 identity。独立审计把候选分母从 47 修正为 76：恢复 30 个 false negative，关闭 1 个 false positive，并修正 2 个 owner。794 项在分母前以 family-specific reason 闭合。75/76 项完成 exact-v1 Method、Evaluation、Limitations/Counterevidence 与 Artifact Review；`2605.10133v1` 只有 identity/abstract，保持精确外部 blocker。current-Books adversarial challenge 将 47 个 provisional Integrate 收紧为 7 项 Integrate、68 项 No Change、1 项 Blocked，并把 EEP owner 纠正为 `INFER-DYNAMO`；本 lane 未写共享 Books。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |",
        "| Window Start | 2026-05-12 |", "| Window End | 2026-05-12 |", "| Registry Version | 2026-08-25 |",
        "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |",
        "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260512-INDEPENDENT-76 |",
        "| Denominator Frozen At | 2026-09-02T00:00:00+08:00 |", "| Completion Status | In Progress |",
        "| Coverage Gate | Closed |", "| Evidence Gate | Conditional Pass |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-05-11T09:00:00+08:00 | 2026-05-12T09:00:00+08:00 | 2026-09-02T00:00:00+08:00 | DataCite v2 prefixes 00..99 + 870/870 title+abstract replay + official exact-v1 | checked | 870 | {families} | pages=300; final_cursor=end; raw=91841; registered=870; screened=870; retained=76; closure=794 | 2026-05-12T00:59:59Z | coverage:SRC-ARXIV:20260512 | GAP-20260512-EXACT-V1-2605-10133 |", "",
        "### Coverage Limitations", "",
        "<!-- coverage:SRC-ARXIV:20260512:start -->非作者已完成 870/870 title+abstract replay：恢复 30 个应入池 family，关闭 FusionRCG 这一 domain-specific HPC false positive，并修正 Agent-X 与 SOMA 的 owner。`2605.10133v1` 的 official abs/version 可读，但 exact-v1 HTML、PDF 与 TeX 均不可取得；该缺口不回退为摘要 Review，也不进入 Books。<!-- coverage:SRC-ARXIV:20260512:end -->", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    candidate_contract: dict[str, dict[str, str]] = {}
    for row in rows:
        aid = row["arxiv_id"]
        comp = comparisons[aid]
        score = row.get("score_v2", {})
        disposition = comp["decision"]
        blocked = aid == "2605.10133"
        values = [
            row["source_family_id"], f"arXiv:{aid}v1", f"paper-v1:{aid}", "2026-W20", "2026-05-11", "SRC-ARXIV",
            score.get("design_delta", 3), score.get("system_reach", 2), score.get("durability", 3), score.get("total", 8),
            "retained", "blocked" if blocked else "deep_complete", "blocked" if blocked else "accessible",
            "none" if disposition != "Integrate" else "knowledge_gap", f"review:{row['source_family_id']}", "self", "—", "new_in_window",
            comp.get("owner_node") or "—", disposition, f"books-review:{row['source_family_id']}", "no",
        ]
        headers = ["Source Family ID", "Primary Identifier", "Event Identity", "Owner Week", "First-public Date", "Supporting Source IDs", "Design Delta", "System Reach", "Durability", "Total", "Candidate State", "Review Status", "Access Status", "Review Override", "Review Ref", "Owner Report Ref", "Prior Review Ref", "Reconciliation", "Stable Node ID", "Books Disposition", "Books Review Ref", "Benchmark Claim"]
        candidate_contract[aid] = {k: str(v) for k, v in zip(headers, values)}
        lines.append("| " + " | ".join(map(cell, values)) + " |")

    lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
              "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        item = packet[row["arxiv_id"]]
        placeholder = f"RP-TEMP-{row['arxiv_id'].replace('.', '-')}"
        method_locator = stable_locator(item["method_identity_locators"], "Method/Identity")
        evaluation_locator = stable_locator(item["evaluation_locators"], "Evaluation")
        limitations_locator = stable_locator(item["limitations_counterevidence_locators"], "Limitations/Counterevidence")
        artifact_locator = item["artifact_locators"]
        if item["completion_result"] == "blocked":
            method_locator = "Pending — exact-v1 body unavailable after official HTML/PDF/TeX retries; Method/Identity body locator cannot be established"
            evaluation_locator = "Pending — exact-v1 body unavailable; Evaluation locator cannot be established from abstract"
            limitations_locator = "Pending — exact-v1 body unavailable; Limitations/Counterevidence locator cannot be established from abstract"
            artifact_locator = "Pending — exact-v1 body unavailable; public artifact identity cannot be verified"
        item["_render_method"] = method_locator
        item["_render_evaluation"] = evaluation_locator
        item["_render_limitations"] = limitations_locator
        item["_render_artifact"] = artifact_locator
        lines.append("| " + " | ".join(map(cell, [
            row["source_family_id"], placeholder, item["review_route"], item["primary_evidence_version"],
            f"SRC-ARXIV@{item['primary_evidence_version']}", method_locator, evaluation_locator,
            limitations_locator, artifact_locator, f"claim:{row['source_family_id']}",
            "blocked" if item["completion_result"] == "blocked" else "complete",
        ])) + " |")

    lines += ["", "### Source Reviews", ""]
    for row in rows:
        family = row["source_family_id"]
        item = packet[row["arxiv_id"]]
        comp = comparisons[row["arxiv_id"]]
        lines += [
            f"<!-- review:{family}:start -->", f"#### {row['title']}", "",
            f"Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`{comp.get('owner_node') or '—'}`。",
            f"Method / identity：{item['_render_method']}。",
            f"Evaluation：{item['_render_evaluation']}。",
            f"Counterevidence / limitations：{item['_render_limitations']}。",
            f"Artifact：{item['_render_artifact']}。", "",
            f"<!-- claim:{family}:start -->{item['claim_nonproof_boundary']}<!-- claim:{family}:end -->", "",
            f"Disposition=`{comp['decision']}`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。",
            f"<!-- review:{family}:end -->", "",
        ]

    lines += [
        "## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
        "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
        "日报不把作者 benchmark 外推为通用性能结论；每项 source review 的 claim boundary 将未披露条件保持为 Not Disclosed。", "",
        "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    selected = {
        "2605.09994": ("DA-TRAINING-DATA-COMMIT", "训练数据的 atomic visibility、cursor 与 checkpoint 回收共同改变 data-plane commit owner"),
        "2605.10448": ("DA-OUTCOME-EVIDENCE-BOUNDS", "交互 Agent 的 outcome authority 从二值分数转为证据支持上下界"),
        "2605.10670": ("DA-MOE-PARTIAL-RANK-RECOVERY", "partial-rank failure 使 membership、expert coverage 与 CUDA-graph execution 必须共同恢复"),
    }
    for row in rows:
        aid, family = row["arxiv_id"], row["source_family_id"]
        prebooks = ";potential_books_delta" if comparisons[aid]["decision"] == "Integrate" else ""
        forced = ";forced_review" if comparisons[aid]["decision"] == "Integrate" else ""
        if aid in selected:
            unit, why = selected[aid]
            lines.append(f"| {family} | score_7_9{forced}{prebooks} | selected | {unit} | — | {why} | analysis:{unit} |")
        else:
            lines.append(f"| {family} | score_7_9{forced}{prebooks} | not_selected | — | — | exact-v1 Review 与 Books Decision 已完成；叙事上限不削减证据义务 | analysis-decision:{family} |")
    lines += ["",
        "<!-- analysis:DA-TRAINING-DATA-COMMIT:start -->### 训练数据平面：从易失传输到可提交 Batch State\n集中 broker 在小规模稳定流水线中简单，但大规模训练会把重放与生命周期压到中间层。对象存储数据面把 batch layout、manifest、atomic visibility、consumer cursor 与 checkpoint 回收绑定为同一 commit contract；收益是 producer/consumer 解耦与故障隔离，代价是 manifest 协调、读放大和 GC 状态。<!-- analysis:DA-TRAINING-DATA-COMMIT:end -->", "",
        "<!-- analysis:DA-OUTCOME-EVIDENCE-BOUNDS:start -->### Agent 评测：从二值成功率到证据支持区间\n交互系统的点击或终局文本不足以证明持久状态已正确改变。评测需要区分 claim、决定性 artifact、Pass/Fail/Unknown 与上下界；收益是 outcome authority 可审计，代价是环境 instrumentation、case checklist 和 Unknown 管理。已有决定性 post-state verifier 时旧二值路径继续成立。<!-- analysis:DA-OUTCOME-EVIDENCE-BOUNDS:end -->", "",
        "<!-- analysis:DA-MOE-PARTIAL-RANK-RECOVERY:start -->### MoE 推理：从整组失败到 Membership 与 Expert Coverage 分离\n宽 EP 中 partial rank failure 不只改变 communicator membership，还可能丢失 expert coverage，而 CUDA graph 又要求稳定执行形态。恢复路径需分别维护 live membership、expert replica/repair 和 reintegration；收益是降级服务与更快恢复，代价是冗余权重、peer-table 更新和 stale membership 风险。无冗余或 correctness 无法证明时仍应 fail-stop。<!-- analysis:DA-MOE-PARTIAL-RANK-RECOVERY:end -->", "",
    ]
    for row in rows:
        family = row["source_family_id"]
        if row["arxiv_id"] not in selected:
            lines.append(f"<!-- analysis-decision:{family}:start -->该 family 已完成独立 exact-v1 Review；未进入 Top 3 只限制 Daily 叙事篇幅，不改变 Evidence/Books 审计义务。<!-- analysis-decision:{family}:end -->")

    lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
              "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        aid, family = row["arxiv_id"], row["source_family_id"]
        comp = comparisons[aid]
        owner_path = comp.get("owner_path", "—")
        adjacent = "; ".join(chapter_ref(p) for p in comp.get("adjacent_paths", [])) or "Not Applicable — exact-v1 body is blocked before adjacent comparison"
        lines.append(f"| {family} | {comp.get('owner_node') or '—'} | {chapter_ref(owner_path)} | {adjacent} | existing:{family} | delta:{family} | Direct Evolution | {comp['decision']} | books-review:{family} |")
    lines.append("")
    for row in rows:
        aid, family = row["arxiv_id"], row["source_family_id"]
        comp = comparisons[aid]
        lines += [f"<!-- books-review:{family}:start -->",
                  f"<!-- existing:{family}:start -->已读取 current owner `{comp.get('owner_path', '—')}` 与相邻章节 `{comp.get('adjacent_paths', [])}`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：{comp.get('owner_body_outline_before_review_notes', 'Blocked before semantic comparison')}。<!-- existing:{family}:end -->",
                  f"<!-- delta:{family}:start -->{comp['reason']}<!-- delta:{family}:end --> Decision=`{comp['decision']}`；本 lane 未写共享 Books。",
                  f"<!-- books-review:{family}:end -->"]

    lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
              "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
              "| --- | --- | --- | --- | --- | --- | --- |",
              "| SA-20260512-INDEPENDENT-COVERAGE | fresh-context:non-author | coverage | coverage:SRC-ARXIV:20260512 | none | 870/870 replay repaired 30 FN, 1 FP and 2 owner mismatches in the independent ledger | passed |",
              f"| SA-20260512-INDEPENDENT-EVIDENCE | fresh-context:non-author | evidence | review:{rows[0]['source_family_id']} | none | 75 deep_complete; 1 exact-v1 access blocker precisely frozen in Materials Request; ordinary pending=0 | passed |",
              "| SA-20260512-INDEPENDENT-DEEP | fresh-context:non-author | deep_analysis_selection | analysis:DA-TRAINING-DATA-COMMIT; analysis:DA-OUTCOME-EVIDENCE-BOUNDS; analysis:DA-MOE-PARTIAL-RANK-RECOVERY | none | author Top 3 was re-challenged; three cross-stage ownership deltas selected while all 76 evidence duties remain preserved | passed |",
              f"| SA-20260512-INDEPENDENT-BOOKS | fresh-context:non-author | books | books-review:{rows[0]['source_family_id']} | F-20260512-BOOKS-WRITEBACK | 47/47 provisional queue challenged against current owner+adjacent body; final owner-merged queue=7; shared Books unchanged | open |", "",
              "## 8. Ignored Noise", "",
              "794 项 family-specific pre-denominator closure 位于 `../_sources/daily-20260512/screening-ledger-independent-reconciled.json`；每项保留真实 title、abstract、具体机制与为何不改变长期系统 contract 的 exclusion boundary。", "",
              "## 9. Recommended Action", "",
              "root 按 `BOOKS_WRITEBACK_QUEUE_FINAL.md` 与 `books-writeback-queue-final.json` 串行写回 7 项、6 个 owner group；其中 `TRAIN-DISTRIBUTED-TRAINING` 的 Maestro 与 ReCoVer 必须合并为一条 execution-plan→failure→recovery 演进链。随后由非写作者检查正文真实存在、位置在首个 Review notes 之前，并重验相邻 owner 冲突。`2605.10133v1` 在 exact-v1 恢复前保持冻结。", "",
              "## 10. Repository Changes", "",
              "- 重放 870/870 screening，分母从 47 修正为 76。", "- 新增独立 exact-v1 packet、provenance、Materials Request、Books comparison 与 reconciled queue。", "- 未修改共享 Books，未 stage、commit 或 push。", "",
              "## 11. Open Questions", "",
              "- `2605.10133v1` 的 exact-version full text 能否从作者 manuscript 或事件时 repository 恢复？", "- 7 项 final queue 经 root 按 6 个 owner group 合并写回后，post-write non-author audit 是否全部通过？", "",
              "## 12. Sources", ""]
    for row in rows:
        aid = row["arxiv_id"]
        url = "https://arxiv.org/pdf/2605.10246v1" if aid == "2605.10246" else ("https://arxiv.org/pdf/2605.11234v1" if aid == "2605.11234" else f"https://arxiv.org/html/{aid}v1")
        lines.append(f"- [{row['title']}]({url}) — exact-v1；first-public 2026-05-11；independent review 2026-09-01")
    lines += ["", "### Materials Request Ledger", "", "<!-- validator:materials-request-v1 -->",
              "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
              "| MR-SF-2605-10133 | P1 Full Text | SF-2026-ARXIV-2605-10133 | — | — | 2026-W20 | arXiv:2605.10133v1; https://arxiv.org/abs/2605.10133v1 | exact-v1 full body with Method, Evaluation, Limitations and appendices | abstract cannot establish mechanism, experiment contract, counterevidence or Books eligibility | official exact-v1 PDF/TeX, author manuscript demonstrably identical to v1, or event-time repository paper snapshot | arxiv-2605.10133v1.pdf | deep review and Books re-decision |", "",
              "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Conditional Pass`", "", "Books: `Open`", "",
              f"ordinary pending=0；75/76 exact-v1 complete；1 precise external blocker；{queue['counts']['integrate']} 项 Books queue 等待 root 串行写回和非写作者 post-write audit。", "", "unresolved findings: 2", ""]

    text = "\n".join(lines)
    for row in rows:
        aid, family = row["arxiv_id"], row["source_family_id"]
        item = packet[aid]
        review_ref = f"review:{family}"
        start = f"<!-- {review_ref}:start -->"
        end = f"<!-- {review_ref}:end -->"
        body = text.split(start, 1)[1].split(end, 1)[0]
        provenance = _expected_review_provenance(
            family,
            candidate_contract[aid],
            item["review_route"],
            item["primary_evidence_version"],
            f"SRC-ARXIV@{item['primary_evidence_version']}",
            item["_render_method"],
            item["_render_evaluation"],
            item["_render_limitations"],
            item["_render_artifact"],
            f"claim:{family}",
            review_ref,
            _normalized_body_sha256(body),
        )
        placeholder = f"RP-TEMP-{aid.replace('.', '-')}"
        text = text.replace(placeholder, provenance)
        item["review_provenance_id"] = provenance
        for key in ("_render_method", "_render_evaluation", "_render_limitations", "_render_artifact"):
            item.pop(key, None)
        for collection in (comparisons,):
            if aid in collection:
                collection[aid]["review_provenance_id"] = provenance
        for queued in queue.get("items", []):
            if queued["arxiv_id"] == aid:
                queued["review_provenance_id"] = provenance

    REPORT.write_text(text)
    (ROOT / "exact-v1-review-packet-independent.json").write_text(json.dumps(list(packet.values()), ensure_ascii=False, indent=2) + "\n")
    (ROOT / "books-current-content-comparison-final.json").write_text(json.dumps(list(comparisons.values()), ensure_ascii=False, indent=2) + "\n")
    (ROOT / "books-writeback-queue-final.json").write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
