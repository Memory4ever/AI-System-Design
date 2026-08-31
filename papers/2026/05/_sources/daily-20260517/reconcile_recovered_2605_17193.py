#!/usr/bin/env python3
"""Reconcile recovered exact-v1 evidence for arXiv:2605.17193v1."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
sys.path.insert(0, str(REPO))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

REPORT = REPO / "papers/2026/05/17/README.md"
ARXIV_ID = "2605.17193"
FAMILY = "SF-2026-ARXIV-2605-17193"
PDF_URL = "https://arxiv.org/pdf/2605.17193v1"
PDF_SHA = "edde49ce22de86ac25ad4d676f9003afec5c11513bee35438ca8db965322abe7"
METHOD = "PDF section Methods; Supplementary Note 1 §§1.1–1.8; Supplementary Notes 2–3 intervention definitions"
EVALUATION = "PDF section Results: Semantic Collapse in Extended Open-Ended Simulations; Semantic Collapse Resists Intervention; Diagnosing Mechanisms of Semantic Collapse; Supplementary Note 3 §3.7"
LIMITS = "PDF section Discussion; Supplementary Note 3 §3.7 non-causal regression boundary; Supplementary Note 5 heuristic-theory and predictive-regularity boundaries"
ARTIFACT = f"official exact-v1 PDF={PDF_URL}; bytes=4076663; sha256={PDF_SHA}; immutable code/data commit Not Disclosed"


def load(name: str):
    return json.loads((ROOT / name).read_text())


def dump(name: str, value) -> None:
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def target(items: list[dict]) -> dict:
    matches = [item for item in items if item.get("arxiv_id") == ARXIV_ID]
    assert len(matches) == 1, len(matches)
    return matches[0]


screening_reason = (
    "Exact-v1 shows that closed-loop multi-LLM exchanges can recursively condition later outputs on model-generated history, "
    "producing semantic contraction despite lexical variation. The authors test disclosed triadic and mixed-model settings, "
    "200–1,000 rounds and twelve intervention categories. This is durable evidence against treating additional agents, turns or "
    "surface diversity as independent information, but it does not prove universal collapse outside the disclosed closed-loop, "
    "text-only protocol or establish the recursive-channel explanation causally."
)

for name in ("screening-ledger-final.json", "screening-ledger-independent-final.json"):
    obj = load(name)
    item = target(obj["identities"])
    item.update(
        screening_status="retained",
        screening_reason=screening_reason,
        owner_node="AGENT-MULTI-AGENT",
        review_status="deep_complete",
        access_status="accessible",
        integration_disposition="No Change — Existing Coverage",
        result_boundary=(
            "Exact-v1 supports semantic contraction only in the authors' disclosed closed-loop simulations and metrics; "
            "it does not establish universal multi-agent collapse, causal channel dynamics, or externally grounded systems."
        ),
        independent_audit="exact_v1_recovered_no_change_existing_coverage",
    )
    obj["retained_candidates"] = 31
    obj["pre_denominator_closed"] = 248
    obj["candidate_denominator"] = 31
    obj["pre_denominator_closures"] = 248
    obj["gate_status"] = "complete"
    obj["independent_reconciliation"].update(exact_v1_complete=31, exact_v1_blocked=0)
    dump(name, obj)

# Canonical TSV follows the independent-final ledger.
ledger = load("screening-ledger-independent-final.json")
with (ROOT / "screening-ledger-independent-final.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["arxiv_id", "source_family_id", "title", "status", "reason", "review", "access", "owner", "disposition", "audit"])
    for item in ledger["identities"]:
        writer.writerow([
            item.get("arxiv_id", ""), item.get("source_family_id", ""), item.get("title", ""),
            item.get("screening_status", ""), item.get("screening_reason", ""), item.get("review_status", ""),
            item.get("access_status", ""), item.get("owner_node", ""), item.get("integration_disposition", ""),
            item.get("independent_audit", ""),
        ])

for name in ("exact-v1-review-packet.json", "exact-v1-independent-review-packet.json"):
    obj = load(name)
    item = target(obj["items"])
    item.update(
        review_route="deep",
        method_identity_locators=METHOD,
        evaluation_locators=EVALUATION,
        limitations_counterevidence_locators=LIMITS,
        artifact_locators=ARTIFACT,
        completion_result="complete",
    )
    dump(name, obj)

owner = REPO / "books/part-07-agent/82-multi-agent.md"
adjacent = [REPO / "books/part-07-agent/81-workflow.md", REPO / "books/part-07-agent/83-mcp.md"]
comparison = {
    "arxiv_id": ARXIV_ID,
    "source_family_id": FAMILY,
    "owner_node": "AGENT-MULTI-AGENT",
    "owner_path": "books/part-07-agent/82-multi-agent.md",
    "adjacent_paths": ["books/part-07-agent/81-workflow.md", "books/part-07-agent/83-mcp.md"],
    "owner_sha256": hashlib.sha256(owner.read_bytes()).hexdigest(),
    "adjacent_sha256": {str(path.relative_to(REPO)): hashlib.sha256(path.read_bytes()).hexdigest() for path in adjacent},
    "existing_proposition": (
        "Ch82 already states that multiple personas do not create independent evidence, same-model/context agents share correlated "
        "errors, more interaction can increase convergence, and low-independence systems should fall back to a single Agent, "
        "independent proposals, deterministic verification or human adjudication. Ch81 owns durable workflow state and Ch83 protocol "
        "interoperability; neither duplicates this failure boundary."
    ),
    "new_evidence_delta": (
        "Exact-v1 adds longitudinal evidence: in disclosed closed-loop text simulations, semantic diversity contracts while lexical "
        "variation persists, and twelve tested surface/deep interventions do not produce a Bonferroni-significant diversity gain. "
        "The regression is not causal and the recursive-channel theory is explicitly heuristic."
    ),
    "decision": "No Change — Existing Coverage",
    "reviewer": "exact-v1-recovery:may2026_day03",
}
for name in ("books-current-content-comparison.json", "books-current-content-comparison-independent.json"):
    items = load(name)
    items = [item for item in items if item.get("arxiv_id") != ARXIV_ID]
    items.append(comparison)
    items.sort(key=lambda item: item["arxiv_id"])
    assert len(items) == 31
    dump(name, items)

request = load("materials-request.json")
request["items"] = [item for item in request["items"] if item.get("source_family_id") != FAMILY]
assert not request["items"]
dump("materials-request.json", request)

coverage = load("coverage-receipt.json")
coverage["ledger_sha256"] = hashlib.sha256((ROOT / "screening-ledger-independent-final.json").read_bytes()).hexdigest()
coverage["status"] = "closed_evidence_recovered"
dump("coverage-receipt.json", coverage)

audit = load("semantic-independent-audit.json")
audit["evidence"].update(deep_complete=31, blocked=[], status="passed")
audit["books"].update(current_content_comparison=31, ordinary_pending=0)
audit["remaining_findings"] = []
audit["recovery_reconciliation"] = {
    "source_family_id": FAMILY,
    "result": "exact_v1_recovered",
    "disposition": "No Change — Existing Coverage",
    "receipt": "RECOVERY_2605.17193.md",
}
dump("semantic-independent-audit.json", audit)

author = load("semantic-author-audit.json")
author["recovery_reconciliation"] = {
    "historical_author_blocker": FAMILY,
    "current_status": "resolved_by_later_exact_v1_recovery",
    "canonical_truth": "semantic-independent-audit.json",
}
dump("semantic-author-audit.json", author)

post = load("books-post-write-semantic-audit.json")
post["external_blockers"] = []
post["counts"]["external_evidence_blockers"] = 0
post["recovery_reconciliation"] = {
    "source_family_id": FAMILY,
    "books_decision": "No Change — Existing Coverage",
    "queue_change": 0,
}
dump("books-post-write-semantic-audit.json", post)

queue = load("BOOKS_WRITEBACK_QUEUE.json")
queue["counts"]["external_blockers"] = 0
queue["recovery_reconciliation"] = {
    "source_family_id": FAMILY,
    "status": "resolved_no_change_existing_coverage",
    "receipt": "RECOVERY_2605.17193.md",
}
dump("BOOKS_WRITEBACK_QUEUE.json", queue)

text = REPORT.read_text()
ledger_sha = coverage["ledger_sha256"]
text = text.replace(
    "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass。22/22 Books 写回已通过独立 post-write semantic audit；2605.17193 exact-v1 为唯一精确外部 blocker。",
    "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。31/31 candidate 均完成 exact-v1 Review；22/22 Books 写回已通过独立 post-write semantic audit，2605.17193 经恢复后判定为 No Change — Existing Coverage。",
)
text = text.replace(
    "30/31 exact-v1 完成 source-specific Review；2605.17193 只有 identity/abstract，已建立一对一 Materials Request。",
    "31/31 exact-v1 完成 source-specific Review；2605.17193 official PDF 已恢复并完成 Method、Evaluation、limitations 与 Books challenge。",
)
text = text.replace("| Completion Status | Conditional |", "| Completion Status | Complete |")
text = text.replace("| Evidence Gate | Conditional Pass |", "| Evidence Gate | Passed |")
text = text.replace("| Books Gate | Conditional Pass |", "| Books Gate | Passed |")
text = re.sub(
    r"(screening-ledger-independent-final\.json#sha256=)[0-9a-f]+",
    rf"\g<1>{ledger_sha}",
    text,
    count=1,
)
text = text.replace(" | GAP-20260517-2605-17193-V1 |", " | — |", 1)
text = re.sub(
    r"<!-- coverage:SRC-ARXIV:20260517:start -->.*?<!-- coverage:SRC-ARXIV:20260517:end -->",
    "<!-- coverage:SRC-ARXIV:20260517:start -->279/279 independent screening 与 248 个 family-specific closure 已闭合，Coverage=Closed。31/31 retained family 完成 exact-v1；2605.17193 official PDF 以完整 Content-Length 与 SHA-256 恢复，HTML 404 不再构成 blocker。<!-- coverage:SRC-ARXIV:20260517:end -->",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    rf"^\| {re.escape(FAMILY)} \|.*$",
    f"| {FAMILY} | arXiv:2605.17193v1 | paper-v1:2605.17193 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:{FAMILY} | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:{FAMILY} | no |",
    text,
    count=1,
    flags=re.M,
)
text = re.sub(
    rf"^\| {re.escape(FAMILY)} \| RP-eded8359312ca1e5 \|.*$",
    f"| {FAMILY} | RP-eded8359312ca1e5 | deep | arXiv:2605.17193v1 | SRC-ARXIV@arXiv:2605.17193v1 | {METHOD} | {EVALUATION} | {LIMITS} | {ARTIFACT} | claim:{FAMILY} | complete |",
    text,
    count=1,
    flags=re.M,
)
review_body = f"""<!-- review:{FAMILY}:start -->
#### Multi-LLM Systems Exhibit Robust Semantic Collapse

问题与机制：旧假设是增加 Agent、模型异质性、讨论轮数或表面采样多样性能够持续扩大搜索空间；当各 Agent 的后续 Context 反复由同一闭环中的模型输出构成时，历史不再是独立证据，而会成为递归 conditioning state。exact-v1 在作者披露的 closed-loop text simulations 中把 lexical diversity、within-run semantic displacement 与 aligned cross-run diversity 分开测量，显示词汇继续增长时语义支持仍可收缩。

Evaluation contract：三种主要模型各进行三次 1,000-round triadic run，其余干预通常使用 200 rounds、每条件三次；十二类干预覆盖 temperature、output budget、prompt、retrieval packing、model mixing、uncensored variants、activation steering、GRPO、population size、framework 与 noise。论文报告 62 个 baseline comparisons 经 Bonferroni correction 后没有正且显著的 semantic-diversity 改善。该结论绑定作者选择的模型、closed-loop scaffold、embedding model、window statistics 与 run-level clustering。

Trade-off / failure：结果支持把“独立 evidence 与外部 renewal”作为 Multi-Agent admission 条件，而不是继续增加同源对话；但它不证明开放工具环境、外部人类/数据持续注入、不同任务拓扑或所有语义度量都会 collapse。Supplementary Note 3 明确回归不构成机制或因果证明，Supplementary Note 5 也把 recursive-channel 理论作为 heuristic guide；immutable code/data commit 为 Not Disclosed。

Evidence locators：Method=`{METHOD}`；Evaluation=`{EVALUATION}`；Counterevidence=`{LIMITS}`；Artifact=`{ARTIFACT}`。

<!-- claim:{FAMILY}:start -->exact-v1 只支持作者 closed-loop、text-only、多模型/多轮与所列 intervention protocol 下的 semantic contraction；不支持“所有 Multi-Agent 都必然退化”，也不证明 recursive-channel explanation 为因果机制。<!-- claim:{FAMILY}:end -->

Books Decision=`No Change — Existing Coverage`：Ch82 已明确拥有同源 Agent 的 correlated error、证据独立性、趋同风险、coordination tax 与 single-Agent / independent verifier fallback；该论文强化现有判断，但没有新增独立状态 owner 或控制机制。
<!-- review:{FAMILY}:end -->"""
text = re.sub(
    rf"<!-- review:{re.escape(FAMILY)}:start -->.*?<!-- review:{re.escape(FAMILY)}:end -->",
    review_body,
    text,
    count=1,
    flags=re.S,
)
text = text.replace(
    f"| {FAMILY} | score_7_9 | not_selected | — | — | 完整 Source Review 已完成或被精确 blocker 冻结；Top-3 不改变审计义务 | analysis-decision:{FAMILY} |",
    f"| {FAMILY} | score_7_9 | not_selected | — | — | exact-v1 Review 已恢复并完成；Top-3 不改变审计义务，且 current Books comparison 判定 No Change | analysis-decision:{FAMILY} |",
)
text = text.replace(
    f"<!-- analysis-decision:{FAMILY}:start -->该 family 已完成独立 Review 或精确 blocker 冻结；未进入 Top-3 不等于未审计。<!-- analysis-decision:{FAMILY}:end -->",
    f"<!-- analysis-decision:{FAMILY}:start -->该 family 已完成 exact-v1 Review 与 current Books challenge；未进入 Top-3 不等于未审计，No Change 也不等于低分。<!-- analysis-decision:{FAMILY}:end -->",
)
text = re.sub(
    rf"^\| {re.escape(FAMILY)} \| AGENT-MULTI-AGENT \|.*$",
    f"| {FAMILY} | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:{FAMILY} | delta:{FAMILY} | Principle Reuse | No Change — Existing Coverage | books-review:{FAMILY} |",
    text,
    count=1,
    flags=re.M,
)
books_block = f"""<!-- books-review:{FAMILY}:start -->
<!-- existing:{FAMILY}:start -->Ch82 已说明 same-model/context agents 共享 correlated error，只有独立 evidence、可验证接口或真实责任分解才可能产生增量；正文还保留趋同、coordination tax、single-Agent、independent proposals、deterministic verifier 与人工 adjudication fallback。Ch81 只拥有 durable workflow state，Ch83 只拥有 protocol interoperability。<!-- existing:{FAMILY}:end -->
<!-- delta:{FAMILY}:start -->exact-v1 在作者 closed-loop text simulations 中提供纵向 evidence：词汇变化可继续增长而语义支持收缩，十二类已测 surface/deep intervention 在 Bonferroni correction 后没有显著提升；但 regression 非 causal，recursive-channel theory 是 heuristic，且未覆盖外部 evidence renewal。<!-- delta:{FAMILY}:end --> Decision=`No Change — Existing Coverage`；无需新增 Books queue 或重复正文。
<!-- books-review:{FAMILY}:end -->"""
text = re.sub(
    rf"<!-- books-review:{re.escape(FAMILY)}:start -->.*?<!-- books-review:{re.escape(FAMILY)}:end -->",
    books_block,
    text,
    count=1,
    flags=re.S,
)
text = text.replace(
    "30 exact-v1 reviews complete; one external blocker has a precise Materials Request",
    "31/31 exact-v1 reviews complete; recovered PDF identity, locators and non-proof boundary independently reconciled",
)
text = text.replace(
    "22/22 queue 已由 root 串行写回，并通过不同 reviewer 的 post-write semantic audit；ordinary pending=0。2605.17193 待 exact-v1 材料恢复后单独重开 Evidence/Books。",
    "22/22 queue 已由 root 串行写回并通过独立 post-write semantic audit；2605.17193 exact-v1 恢复后判定 No Change — Existing Coverage。ordinary pending=0、external blocker=0，无新增 Books 写回。",
)
text = text.replace(
    "- 新增/更新 05-17 date-local independent ledger、exact-v1 receipts、Books comparison/queue、audit 与 canonical Daily。",
    "- 新增/更新 05-17 date-local independent ledger、exact-v1 receipts、Books comparison/queue、audit 与 canonical Daily；恢复 2605.17193 official exact-v1 PDF 并关闭唯一 Materials Request。",
)
text = text.replace("- 能否取得 2605.17193v1 official/author exact-v1 full text？", "- 无；当前 denominator、Evidence、Books Decision 与 post-write audit 均无未解决项。")
text = text.replace(
    "[Multi-LLM Systems Exhibit Robust Semantic Collapse](https://arxiv.org/abs/2605.17193v1) — exact-v1 identity only; body blocked；first-public 2026-05-16；accessed 2026-09-01",
    "[Multi-LLM Systems Exhibit Robust Semantic Collapse](https://arxiv.org/pdf/2605.17193v1) — official exact-v1 PDF；first-public 2026-05-16；accessed 2026-09-01",
)
text = re.sub(
    r"### Materials Request Ledger\n\n<!-- validator:materials-request-v1 -->.*?(?=\n## 13\. Final Status)",
    "### Materials Request Ledger\n\nNo open materials requests. The former `MR-2605-17193-V1` was closed by `RECOVERY_2605.17193.md`.\n",
    text,
    count=1,
    flags=re.S,
)
text = text.replace("Completion Status: `Conditional`", "Completion Status: `Complete`")
text = text.replace("Evidence: `Conditional Pass`", "Evidence: `Passed`")
text = text.replace("Books: `Conditional Pass`", "Books: `Passed`")
text = text.replace("unresolved findings: 1", "unresolved findings: 0")
text = text.replace(
    "确定性 Coverage、30 个 accessible family 的 Evidence 与 22/22 Books 写回均已闭合；ordinary pending=0。唯一剩余条件是 2605.17193 exact-v1 外部材料，其精确 Materials Request 已记录。",
    "确定性 Coverage、31/31 candidate Evidence、31/31 current Books comparison 与 22/22 Books 写回均已闭合；2605.17193 exact-v1 已恢复并判定 No Change — Existing Coverage。ordinary pending=0、external blocker=0。",
)

review_segment = re.search(
    rf"<!-- review:{re.escape(FAMILY)}:start -->(.*?)<!-- review:{re.escape(FAMILY)}:end -->",
    text,
    re.S,
)
assert review_segment is not None
candidate = {
    "Event Identity": "paper-v1:2605.17193",
    "Primary Identifier": "arXiv:2605.17193v1",
    "Supporting Source IDs": "SRC-ARXIV",
    "Review Override": "none",
}
provenance = _expected_review_provenance(
    FAMILY,
    candidate,
    "deep",
    "arXiv:2605.17193v1",
    "SRC-ARXIV@arXiv:2605.17193v1",
    METHOD,
    EVALUATION,
    LIMITS,
    ARTIFACT,
    f"claim:{FAMILY}",
    f"review:{FAMILY}",
    _normalized_body_sha256(review_segment.group(1)),
)
text = re.sub(
    rf"^(\| {re.escape(FAMILY)} \| )RP-[0-9a-f]+( \| deep \|)",
    rf"\g<1>{provenance}\g<2>",
    text,
    count=1,
    flags=re.M,
)
REPORT.write_text(text)
