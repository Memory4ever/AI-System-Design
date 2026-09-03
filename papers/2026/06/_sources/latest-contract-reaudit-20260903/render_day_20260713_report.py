#!/usr/bin/env python3
"""Render the author-side V2.1 report and frozen Books queue for 2026-07-13.

The script consumes only date-local frozen semantic decisions and exact-v1
reviews.  It intentionally leaves all four fresh-context semantic audits open:
the author of the evidence packet cannot certify their own work, and Books
writeback belongs to the root sequential owner.
"""

from __future__ import annotations

import gzip
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260713"
REPORT = ROOT / "papers/2026/07/13/README.md"
MONTH_QUEUE = ROOT / "papers/2026/07/_sources/BOOKS_WRITEBACK_QUEUE_latest-contract.json"
DAY_QUEUE = PACKET / "BOOKS_WRITEBACK_QUEUE_V2.1.json"
DECISIONS = PACKET / "fresh-context-semantic-decisions-v2.1.json.gz"
DENOMINATOR = PACKET / "candidate-denominator-v2.1.json"
HTML_DIR = PACKET / "exact-v1-html"
GENERATED_AT = "2026-09-03T22:30:00+08:00"

FORCED_OVERRIDES = {
    "2607.08883": "release_security_contract",
    "2607.09053": "books_conflict",
    "2607.09156": "books_conflict",
    "2607.09306": "books_conflict",
    "2607.09349": "books_conflict",
    "2607.09492": "books_conflict",
    "2607.09532": "release_security_contract",
}

SELECTED = {
    "SF-2026-ARXIV-2607-08782": "DA-20260713-01",
    "SF-2026-ARXIV-2607-09207": "DA-20260713-02",
    "SF-2026-ARXIV-2607-09153": "DA-20260713-03",
}


def md(value: object) -> str:
    """Keep generated table cells on one physical row."""
    text = re.sub(r"\s+", " ", str(value)).strip()
    return text.replace("|", "&#124;")


def canonical_multi(value: str) -> str:
    items = []
    for raw in value.split(";"):
        item = unicodedata.normalize("NFC", raw.strip())
        if item and item not in {"—", "-", "N/A", "n/a"}:
            items.append(item)
    return ";".join(sorted(items))


def body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def provenance(candidate: dict[str, str], receipt: dict[str, str], body: str) -> str:
    fields = [
        "review-completion-v1",
        candidate["Source Family ID"],
        candidate["Event Identity"],
        candidate["Primary Identifier"],
        canonical_multi(candidate["Supporting Source IDs"]),
        receipt["Primary Evidence Version"],
        canonical_multi(receipt["Reviewed Evidence Versions"]),
        receipt["Review Route"],
    ]
    if candidate["Review Override"] != "none":
        fields.append(f"review-override:{candidate['Review Override']}")
    fields.extend(
        [
            canonical_multi(receipt["Method / Identity Locators"]),
            canonical_multi(receipt["Evaluation Locators"]),
            canonical_multi(receipt["Limitations / Counterevidence Locators"]),
            canonical_multi(receipt["Artifact Locators"]),
            receipt["Claim Boundary Ref"],
            candidate["Review Ref"],
            f"review-body-sha256:{body_sha256(body)}",
        ]
    )
    return "RP-" + hashlib.sha256("|".join(fields).encode("utf-8")).hexdigest()[:16]


def exact_title(arxiv_id: str, fallback: str) -> str:
    path = HTML_DIR / f"{arxiv_id}v1.html.gz"
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as handle:
        prefix = handle.read(160_000)
    match = re.search(r"<title[^>]*>(.*?)</title>", prefix, re.I | re.S)
    if not match:
        return fallback
    title = re.sub(r"<[^>]+>", " ", match.group(1))
    return re.sub(r"\s+", " ", html.unescape(title)).strip()


def load_reviews() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for path in sorted(PACKET.glob("source-review-batch-*-v2.1.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("status") != "complete":
            raise RuntimeError(f"incomplete review batch: {path}")
        for review in payload["reviews"]:
            result[review["source_family_id"]] = review
    return result


def review_body(title: str, admission: dict, review: dict) -> str:
    family = review["source_family_id"]
    score = review["score_v2"]
    method = "; ".join(review["method_locators"])
    evaluation = "; ".join(review["evaluation_locators"]) or (
        "Not Required — exact v1 is a conceptual position paper and makes no empirical performance claim"
    )
    limitations = "; ".join(review["limitations_locators"])
    return "\n".join(
        [
            f"### {title}",
            "",
            f"<!-- claim:{family}:start -->{review['claim']} 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:{family}:end -->",
            "",
            f"**为什么进入候选分母。** {admission['reason']}",
            "",
            f"**机制与状态边界。** {review['mechanism']}",
            "",
            f"**证据证明什么。** {review['proved']}",
            "",
            f"**证据没有证明什么。** {review['not_proved']}",
            "",
            f"**Evaluation contract。** Method / identity：{method}。Evaluation：{evaluation}。Limitations / counterevidence：{limitations}。",
            "",
            f"**Artifact boundary。** {review['artifact_boundary']}",
            "",
            f"**Trade-off 与共存边界。** {review['trade_off']}",
            "",
            f"- Score V2：Design Delta {score['design_delta']} / System Reach {score['system_reach']} / Durability {score['durability']} = **{score['total']}/9**。",
            f"- Stable owner 候选：`{review['stable_node_id']}`；evidence-stage relation：`{review['evolution_relation']}`。",
            f"- Books 候选路由（尚非最终决定）：`{review['books_disposition']}`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。",
        ]
    )


def selected_narrative(title: str, review: dict, unit: str) -> str:
    family = review["source_family_id"]
    opening = {
        "DA-20260713-01": "静态 expert placement 在热点稳定、迁移代价高且预测价值有限时仍然合理；请求分布发生漂移后，placement 才从一次性部署选择变成带预测误差和迁移成本的在线控制问题。",
        "DA-20260713-02": "固定 rollout / training 资源池在同步训练与稳定生成成本下简单可靠；异步 RL 中两侧处理率和 policy staleness 持续变化，固定切分会让一侧空闲而另一侧堆积。",
        "DA-20260713-03": "独立 text verifier 具有跨模型、跨进程和跨信任域的可移植性；当同一生成器刚完成长轨迹且 compatible verifier 反复评分时，丢弃 exact KV 再重做 prefill 才成为主要冗余。",
    }[unit]
    return "\n".join(
        [
            f"<!-- analysis:{unit}:start -->",
            f"### {title}",
            "",
            f"**旧方案为何合理、约束何时改变。** {opening}",
            "",
            f"**机制如何改写 control / data / state。** {review['mechanism']}",
            "",
            f"**可成立的证据边界。** {review['proved']} 但 {review['not_proved']}",
            "",
            f"**收益、代价与下一重压力。** {review['trade_off']} 这意味着新机制是有条件的演进，而不是对旧方案的无条件替代。",
            "",
            f"关联完整 Source Review：`review:{family}`。",
            f"<!-- analysis:{unit}:end -->",
        ]
    )


def main() -> None:
    with gzip.open(DECISIONS, "rt", encoding="utf-8") as handle:
        semantic = json.load(handle)
    denominator = json.loads(DENOMINATOR.read_text(encoding="utf-8"))
    reviews = load_reviews()
    admissions = {
        item["source_family_id"]: item
        for item in semantic["items"]
        if item["decision"] == "retain_in_candidate_denominator"
    }
    if set(admissions) != set(reviews) or len(reviews) != 62:
        raise RuntimeError("frozen denominator and exact-v1 review set do not match")

    titles: dict[str, str] = {}
    candidates: dict[str, dict[str, str]] = {}
    receipts: dict[str, dict[str, str]] = {}
    bodies: dict[str, str] = {}
    for family in sorted(reviews):
        review = reviews[family]
        admission = admissions[family]
        arxiv_id = review["primary_evidence"].removeprefix("arXiv:").removesuffix("v1")
        title = exact_title(arxiv_id, admission["title"])
        titles[family] = title
        score = review["score_v2"]
        route = "deep" if score["total"] >= 7 or arxiv_id in FORCED_OVERRIDES else "standard"
        override = FORCED_OVERRIDES.get(arxiv_id, "none")
        candidate = {
            "Source Family ID": family,
            "Primary Identifier": f"arXiv:{arxiv_id}v1",
            "Event Identity": f"paper-v1:{arxiv_id}",
            "Owner Week": "2026-W29",
            "First-public Date": "2026-07-13",
            "Supporting Source IDs": "SRC-ARXIV",
            "Design Delta": str(score["design_delta"]),
            "System Reach": str(score["system_reach"]),
            "Durability": str(score["durability"]),
            "Total": str(score["total"]),
            "Candidate State": "retained",
            "Review Status": f"{route}_complete",
            "Access Status": "accessible",
            "Review Override": override,
            "Review Ref": f"review:{family}",
            "Owner Report Ref": "self",
            "Prior Review Ref": "—",
            "Reconciliation": "new_in_window",
            "Stable Node ID": review["stable_node_id"],
            "Books Disposition": "Not Assessed",
            "Books Review Ref": "—",
            "Benchmark Claim": "no",
        }
        method = "; ".join(review["method_locators"])
        evaluation = "; ".join(review["evaluation_locators"]) or (
            "Not Required — conceptual paper has no empirical evaluation contract"
        )
        limitations = "; ".join(review["limitations_locators"])
        artifact = review["artifact_boundary"]
        if not re.search(r"https?://|Not (?:Disclosed|Required|Verified)", artifact):
            artifact = "Not Disclosed — " + artifact
        receipt = {
            "Review Route": route,
            "Primary Evidence Version": f"arXiv:{arxiv_id}v1",
            "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{arxiv_id}v1",
            "Method / Identity Locators": method,
            "Evaluation Locators": evaluation,
            "Limitations / Counterevidence Locators": limitations,
            "Artifact Locators": artifact,
            "Claim Boundary Ref": f"claim:{family}",
            "Completion Result": "complete",
        }
        body = review_body(title, admission, review)
        receipt["Review Provenance ID"] = provenance(candidate, receipt, body)
        candidates[family] = candidate
        receipts[family] = receipt
        bodies[family] = body

    candidate_families = ";".join(sorted(candidates))
    decision_counts = Counter(
        item["decision_kind"]
        for item in semantic["items"]
        if item["decision"] == "pre_denominator_closure"
    )
    deep_families = [family for family in sorted(candidates) if int(candidates[family]["Total"]) >= 7 or candidates[family]["Review Override"] != "none"]
    standard_count = len(candidates) - len(deep_families)

    out: list[str] = [
        "# Daily Research — 2026-07-13",
        "",
        "**Research Date:** 2026-07-13",
        "",
        "**Timezone:** Asia/Shanghai",
        "",
        "**Strict Window:** 2026-07-12 09:00:00 ～ 2026-07-13 09:00:00（北京时间，左闭右开）",
        "",
        "**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源",
        "",
        "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较",
        "",
        "## Executive Summary",
        "",
        f"本窗口从官方 arXiv first-public owner inventory 枚举 **{semantic['raw_identity_count']}** 个唯一 identity；逐项读取 title 与完整 abstract 后，冻结为 **{len(candidates)}** 个候选，**{semantic['pre_denominator_closure_count']}** 个 family-specific pre-denominator closure，retain rate 为 **{semantic['retain_rate'] * 100:.2f}%**。候选随后全部取得 exact v1：{len(candidates)}/{len(candidates)} 已完成非模板化 Source Review，其中 Deep {len(deep_families)}、Standard {standard_count}、blocked 0。",
        "",
        "本次修正了两个重要 provenance 问题：`2607.08974` 不再沿用 metadata-only 低估，而按 exact v1 的 VLM-to-VLA 机制进入 Deep Review；`2607.09306` 只审阅首发 v1 的 companion-memory lifecycle，明确隔离 7 月 30 日实质改题的 v3，后者不能倒灌首发窗口。",
        "",
        "这仍不是 Complete：本泳道没有 Books 写权限，62 项 Books disposition 暂为 `Not Assessed`；Coverage、Evidence、Deep Selection 与 Books 四项 fresh-context Semantic Audit 也必须由未参与主要写作的 reviewer 完成。",
        "",
        "## 1. Coverage",
        "",
        "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |",
        "| --- | --- |",
        "| Contract Version | V2.1 |",
        "| Score Schema | V2 |",
        "| Report Type | Daily |",
        "| Window Start | 2026-07-13 |",
        "| Window End | 2026-07-13 |",
        "| Registry Version | 2026-08-25 |",
        "| Coverage Mode | Full Replay |",
        "| Baseline Report | — |",
        "| Changed Source IDs | — |",
        "| Previous Denominator ID | — |",
        f"| Denominator ID | {denominator['denominator_id']} |",
        f"| Denominator Frozen At | {denominator['frozen_at']} |",
        "| Completion Status | In Progress |",
        "| Coverage Gate | Open |",
        "| Evidence Gate | Open |",
        "| Books Gate | Open |",
        "",
        "### Source Coverage Receipt",
        "",
        "<!-- coverage:SRC-ARXIV:20260713:start -->",
        "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-07-12T09:00:00+08:00 | 2026-07-13T09:00:00+08:00 | {semantic['executed_at']} | official arXiv monthly category listings; v1 submission history; availability schedule; DataCite DOI created used only to reconcile announcement cycle | checked | {semantic['raw_identity_count']} | {candidate_families} | all registered category pages, show=2000; cross-category identity dedup complete | 2026-07-13T09:00:00+08:00 | sha256:{denominator['denominator_id'].rsplit(':', 1)[-1]} | — |",
        "<!-- coverage:SRC-ARXIV:20260713:end -->",
        "",
        "### Coverage Limitations",
        "",
        "- 当前 `official-arxiv-first-public-owner-receipt-v1.json` 专门记录旧 4 项候选的 owner 移动；完整 337 项的 canonical owner truth 在 raw inventory 与全局 owner reconciliation 中，不得把该 4 项收据误读成当日分母。",
        "- DataCite 只用于 identity/date 交叉检验；技术 claim 全部回到 exact arXiv v1 HTML。",
        "- Coverage 的 author-side receipt 已闭合，但独立 false-positive / false-negative Semantic Audit 尚未签收，因此 Coverage Gate 保持 Open。",
        "",
        "## 2. Candidate Ledger",
        "",
        "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    candidate_cols = list(next(iter(candidates.values())).keys())
    for family in sorted(candidates):
        out.append("| " + " | ".join(md(candidates[family][column]) for column in candidate_cols) + " |")

    out.extend(
        [
            "",
            "## 3. Review Completion Receipt",
            "",
            "<!-- validator:review-completion-v1 -->",
            "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    receipt_cols = [
        "Review Provenance ID", "Review Route", "Primary Evidence Version", "Reviewed Evidence Versions",
        "Method / Identity Locators", "Evaluation Locators", "Limitations / Counterevidence Locators",
        "Artifact Locators", "Claim Boundary Ref", "Completion Result",
    ]
    for family in sorted(receipts):
        out.append("| " + md(family) + " | " + " | ".join(md(receipts[family][column]) for column in receipt_cols) + " |")

    out.extend(["", "### Source Reviews", ""])
    for family in sorted(bodies):
        out.extend([f"<!-- review:{family}:start -->", bodies[family], f"<!-- review:{family}:end -->", ""])

    out.extend(
        [
            "## 4. Benchmark Contracts",
            "",
            "None。本报告保留每篇论文自己的 evaluation locator 与 claim boundary，但不转录任何可跨配置复用的数值性能主张；因此 Candidate Ledger 的 `Benchmark Claim` 均为 `no`。这不表示论文没有实验。",
            "",
            "## 5. Deep Analysis Selection",
            "",
            "<!-- validator:deep-analysis-selection-v1 -->",
            "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    selection_rows = []
    for family in deep_families:
        candidate = candidates[family]
        review = reviews[family]
        eligibility = ["score_7_9"]
        if candidate["Review Override"] != "none":
            eligibility.append("forced_review")
        if family in SELECTED:
            unit = SELECTED[family]
            decision = "selected"
            rationale = (
                f"V2={candidate['Total']}/9；{review['claim']}；该 family 分别代表在线 placement control、异步 RL 双向资源控制或跨阶段 exact state reuse，提供本日报最清晰且互不重复的三条系统演进主轴。"
            )
            narrative = f"analysis:{unit}"
        else:
            unit = "—"
            decision = "not_selected"
            rationale = (
                f"V2={candidate['Total']}/9；{review['claim']}；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。"
            )
            narrative = f"analysis-decision:{family}"
        selection_rows.append((family, ";".join(eligibility), decision, unit, "—", rationale, narrative))
    for row in selection_rows:
        out.append("| " + " | ".join(md(value) for value in row) + " |")

    out.extend(["", "### Selection Decisions", ""])
    for family in deep_families:
        if family in SELECTED:
            continue
        review = reviews[family]
        out.extend(
            [
                f"<!-- analysis-decision:{family}:start -->",
                f"`{family}` 已完成 exact-v1 Deep Review。其机制焦点是：{review['mechanism']} 本日报不将它压入三条入选叙事，因为这会混淆 `{review['stable_node_id']}` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:{family}`。",
                f"<!-- analysis-decision:{family}:end -->",
                "",
            ]
        )

    out.extend(["### Selected Analysis Narratives", ""])
    for family, unit in SELECTED.items():
        out.extend([selected_narrative(titles[family], reviews[family], unit), ""])

    out.extend(
        [
            "## 6. Books Comparison",
            "",
            "<!-- validator:books-comparison-v1 -->",
            "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            "",
            "None。Evidence-stage owner 与 proposed route 已写入 date-local frozen queue，但本泳道没有 Books 写权限，也没有把候选建议伪装成完成的章节比较。root 必须按日期顺序读取目标及相邻章节后，逐 family 写回最终 disposition。",
            "",
            "## 7. Semantic Audit",
            "",
            "<!-- validator:semantic-audit-v1 -->",
            "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            "| SA-20260713-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260713 | GAP-20260713-COVERAGE-INDEPENDENT：主要作者已完成 337 项全量语义判断，但 false-positive 与 false-negative 尚未由未参与写作的 reviewer 逐项签收 | Pending — 独立 reviewer 对 canonical raw inventory 与 semantic decisions 做全量反向审计，并记录具体 finding / resolution | open |",
            "| SA-20260713-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260713-EVIDENCE-INDEPENDENT：62 个 RP 绑定 exact v1，但 claim scope、locator 与 artifact boundary 尚需独立反证审阅 | Pending — 独立 reviewer 校验 62 个 review body 与 exact-v1 locator 一致性；发现问题则重开具体 family | open |",
            "| SA-20260713-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260713-SELECTION-INDEPENDENT：42 个 eligible family 的三项长叙事选择尚未由独立 reviewer 比较系统影响、反证优先级与跨 owner 独立性 | Pending — 独立 reviewer 对 selection pool 与 3 个 selected unit 做 adversarial comparison | open |",
            "| SA-20260713-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260713-BOOKS-ROOT：62 项尚未逐一对读目标及相邻 Books 章节，最终 disposition 未成立 | Pending — root sequential owner 消费 date-local queue，完成 Books Comparison / writeback 或明确 No Change / Structural route | open |",
            "",
            "## 8. Ignored Noise",
            "",
            f"共有 {semantic['pre_denominator_closure_count']} 个 identity 在 title + 完整 abstract 阶段得到 family-specific closure；它们仍保留在 `fresh-context-semantic-decisions-v2.1.json.gz`，没有被静默丢弃，也没有接受不适用的 Score V2。",
            "",
        ]
    )
    for kind, count in sorted(decision_counts.items()):
        out.append(f"- `{kind}`：{count}")

    proposed_counts = Counter(review["books_disposition"] for review in reviews.values())
    out.extend(
        [
            "",
            "## 9. Recommended Action",
            "",
            f"1. 先由独立 reviewer 审阅 Coverage、Evidence 与 Deep Analysis Selection；任何 finding 必须回到具体 family 修复，不能只改 Gate 文本。",
            f"2. root 再消费冻结队列，逐项比较 Books。当前只作为建议起点的计数为：Integrate {proposed_counts['Integrate']}、No Change {proposed_counts['No Change — Existing Coverage']}、Structural Candidate {proposed_counts['Structural Candidate']}；这些不是最终 Books Decision。",
            "3. `2607.09306` 的 v3 作为 2026-07-30 的重要 revision 另行路由，首发日报只能引用 exact v1。",
            "",
            "## 10. Repository Changes",
            "",
            "- 重建 `papers/2026/07/13/README.md`，用 337→62 的 frozen denominator 替换旧 4 项临时报告。",
            "- 新增 `papers/2026/07/_sources/daily-20260713/BOOKS_WRITEBACK_QUEUE_V2.1.json`，并更新 7 月月级冻结队列中的 7 月 13 日条目。",
            "- 没有修改 Books、ROADMAP、docs、Learning State、Weekly 或共享 validator。",
            "",
            "## 11. Open Questions",
            "",
            "- 独立 false-negative audit 是否发现 275 项 closure 中仍存在满足 denominator admission 的 family？",
            "- 42 个 proposed Integrate 是否在 Books 已由其他 Source Family 承载，因而应改为 `No Change — Existing Coverage`？",
            "- `2607.09306` v1→v3 的实质改题是否形成需要重开 2026-07-30 Daily 的 important revision？",
            "",
            "## 12. Sources",
            "",
        ]
    )
    for family in sorted(candidates):
        arxiv_id = candidates[family]["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        out.append(f"- [{titles[family]}](https://arxiv.org/html/{arxiv_id}v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03")

    out.extend(
        [
            "",
            "## 13. Final Status",
            "",
            f"Author-side Coverage screening、denominator、exact-v1 access、62/62 Source Review 与 42-family Deep Selection receipt 已构建；Books 写回仍冻结，四项独立 Semantic Audit 尚未完成。",
            "",
            "State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。",
            "",
        ]
    )

    REPORT.write_text("\n".join(out), encoding="utf-8")

    queue_entries = []
    for family in sorted(reviews):
        review = reviews[family]
        arxiv_id = candidates[family]["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        queue_entries.append(
            {
                "date": "2026-07-13",
                "source_family_id": family,
                "primary_identifier": f"arXiv:{arxiv_id}v1",
                "review_provenance_id": receipts[family]["Review Provenance ID"],
                "stable_node_id": review["stable_node_id"],
                "proposed_books_disposition": review["books_disposition"],
                "evolution_relation": review["evolution_relation"],
                "report": "papers/2026/07/13/README.md",
                "queue_status": "frozen_pending_independent_audit_and_root_books_comparison",
                "reason": "Exact-v1 evidence review is author-complete; final Books disposition requires independent semantic audit and root sequential chapter comparison.",
            }
        )
    day_queue = {
        "schema": "books-writeback-queue-v2.1",
        "report_date": "2026-07-13",
        "generated_at": GENERATED_AT,
        "status": "frozen",
        "write_authority": "root-sequential-owner-only",
        "entry_count": len(queue_entries),
        "proposed_disposition_counts": dict(sorted(proposed_counts.items())),
        "entries": queue_entries,
    }
    DAY_QUEUE.write_text(json.dumps(day_queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    month = json.loads(MONTH_QUEUE.read_text(encoding="utf-8"))
    preserved = [entry for entry in month.get("entries", []) if entry.get("date") != "2026-07-13"]
    month["generated_at"] = GENERATED_AT
    month["status"] = "frozen"
    month["write_authority"] = "root-sequential-owner-only"
    month["entries"] = sorted(preserved + queue_entries, key=lambda item: (item.get("date", ""), item.get("source_family_id", "")))
    month["entry_count"] = len(month["entries"])
    MONTH_QUEUE.write_text(json.dumps(month, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    denominator["status"] = "frozen_author_evidence_complete_independent_audit_and_books_pending"
    denominator["review_completion"] = {"expected": 62, "complete": 62, "blocked": 0}
    denominator["deep_analysis_selection"] = {"eligible": len(deep_families), "selected": 3, "author_receipt": "complete"}
    denominator["books_status"] = "frozen_pending_root_sequential_comparison"
    DENOMINATOR.write_text(json.dumps(denominator, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "report": REPORT.relative_to(ROOT).as_posix(),
        "raw": semantic["raw_identity_count"],
        "retained": len(candidates),
        "closures": semantic["pre_denominator_closure_count"],
        "deep": len(deep_families),
        "standard": standard_count,
        "queue": len(queue_entries),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
