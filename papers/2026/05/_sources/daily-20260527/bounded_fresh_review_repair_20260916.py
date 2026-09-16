#!/usr/bin/env python3
"""Apply the bounded 2026-05-27 repair found by fresh non-author review.

Scope is deliberately limited to two closure false negatives and the stale
Evidence projection of the already-applied sixteen root bindings.  It does not
edit shared Books and it does not expand the frozen owner corpus.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/27/README.md"


def load(name: str):
    return json.loads((HERE / name).read_text())


def dump(name: str, value) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


REOPENED = {
    "2605.25333": {
        "source_family_id": "SF-2026-ARXIV-2605-25333",
        "title": "Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution",
        "proposition": (
            "流式视频 KV cache 只有在条目保留原始时间/相机 identity，且训练显式暴露局部观测失效到历史可靠锚点的非局部恢复边时，"
            "才会从容量缓冲演进为动态状态记忆；仅扩大 cache 不会自动学会选择可靠历史。"
        ),
        "method": "§3.2 PM-RoPE; §3.3 Dynamic Memory with Streaming KV Cache; §3.4 Training Scheme for Dynamic Memory",
        "evaluation": "§4.1–§4.4 STEVO-Bench/VBench, component ablations and KV-importance diagnostics",
        "limitations": "§5 Conclusion and Limitation: bounded interruption types; camera/depth quality and pose-error boundary",
        "boundary": (
            "exact-v1 证明的是作者 video diffusion backbone、camera/depth pipeline、STEVO-Bench/VBench 与受控 interruption 下的"
            "非局部历史检索机制；它不解决全部物理推理，camera/depth/pose error 会污染监督，也不证明生成 cache 是环境事实、"
            "开放世界状态或安全控制 authority。失败时回退显式 state memory、短窗口重算或新 observation 校正。"
        ),
        "score": {"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8},
        "owner_node": "MULTIMODAL-WORLD-MODELS",
        "owner_path": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
        "decision": "No Change — Existing Coverage",
        "coverage_anchor": "Memory 架构为何从静态 cache 演进",
        "existing": (
            "短视频可缓存最近 frames 或 KV；视角反复切换、物体离开画面再返回时，单一短窗口会遗忘状态。"
            "正文已把 recent-frame cache → view-indexed/static-dynamic memory → transition-aware persistent belief 写成演进，"
            "并明确 cache placement 不能替代 world-state semantics。"
        ),
        "difference": (
            "ReMind 提供 original-position/camera-aware KV addressing、node-drop/noisy-memory/reference-cache curriculum 与"
            "受限 recovery evidence，但没有改变正文既有的 dynamic-memory owner、观测校正、stale-state 与 fallback 判断。"
        ),
    },
    "2605.25522": {
        "source_family_id": "SF-2026-ARXIV-2605-25522",
        "title": "Co-Designing Graph-based Approximate Nearest Neighbor Search at Billion Scale for Processing-in-Memory",
        "proposition": (
            "十亿级 graph ANNS 迁移到 PIM 不能只下沉距离计算：index footprint、跨 PU graph traversal、host coordination 与弱算力"
            "必须联合 co-design；compact index 和异步 mini-batch pipeline 会把瓶颈转移到 host rerank/transfer，并形成"
            "overfetch–recall–throughput 的显式边界。"
        ),
        "method": "§II-C co-design challenges; §IV-A compact index; §IV-B asynchronous pipeline; §IV-C multiplication-free kernel",
        "evaluation": "§V-A–§V-E: three billion-scale datasets, CPU/GPU/PIM baselines, ablations and scalability",
        "limitations": (
            "No dedicated Limitations section; §V-D shows host rerank/transfer domination and overfetch trade-off; "
            "§V-E scale-out/emerging-PIM results include simulation/projection beyond the measured UPMEM system"
        ),
        "boundary": (
            "exact-v1 的端到端证据绑定三套 billion-scale datasets、披露的 dual-Xeon/A100/UPMEM 配置和 recall@10；"
            "host rerank 已成为主要瓶颈，multi-node/emerging-PIM 部分含模拟或投影，不能外推到任意 index、硬件、并发或生产尾延迟。"
            "容量、互联或 recall contract 不满足时应回退 CPU/GPU 或既有 ANN 数据面。"
        ),
        "score": {"design_delta": 3, "system_reach": 3, "durability": 2, "total": 8},
        "owner_node": "AGENT-RAG",
        "owner_path": "books/part-07-agent/76-rag.md",
        "decision": "Integrate",
        "coverage_anchor": "多向量检索的数据面要避免搬运高精度向量",
        "existing": (
            "正文已说明检索表示与执行成本不可分，并用 GPU 低精度 candidate generation、CPU 高精度 refinement 解释"
            "host/device movement、额外副本、量化误差和一致性成本。"
        ),
        "difference": (
            "现有正文没有承载 graph ANNS 在 PIM 的 index-layout/partition/communication/scheduler/kernel 联合设计，"
            "也没有明确 compact index 把瓶颈移到 host rerank 后的 overfetch–recall fallback，因此属于长期语义增量。"
        ),
    },
}


# 1. Reopen exactly two identities inside the frozen 692-owner corpus.
screening = load("screening-outcomes-v3.json")
seen = set()
for item in screening["items"]:
    aid = item["arxiv_id"]
    if aid not in REOPENED:
        continue
    seen.add(aid)
    item["screening_status"] = "retained"
    item["screening_reason"] = (
        "fresh non-author title+full-abstract challenge reopened this family: "
        + REOPENED[aid]["proposition"]
        + "；exact-v1 review then bounded the claim and Books disposition."
    )
assert seen == set(REOPENED)
screening["retained_count"] = 91
screening["pre_denominator_closure_count"] = 601
screening["conservation"] = "692 = 91 retained + 601 pre-denominator closure + 0 withdrawn"
challenge = screening["false_positive_negative_challenge"]
challenge["retained_after_rebuild"] = 91
challenge["reopened_from_stale_projection"] = 17
challenge["closure_count_after_challenge"] = 601
challenge["fresh_reviewer_reopened"] = sorted(REOPENED)
dump("screening-outcomes-v3.json", screening)


# 2. Synchronize old root writebacks and add the two exact-v1 reviews.
evidence = load("evidence-review-v3.json")
queue = load("root-books-writeback-queue-v3.json")
old_queue_ids = {item["arxiv_id"] for item in queue["items"]}
assert len(old_queue_ids) == 16
for item in evidence["items"]:
    if item["arxiv_id"] in old_queue_ids:
        item["books_decision"] = "Applied"

for aid, spec in REOPENED.items():
    evidence["items"].append({
        "arxiv_id": aid,
        "source_family_id": spec["source_family_id"],
        "title": spec["title"],
        "primary_evidence_version": f"arXiv:{aid}v1",
        "retrieval_route": "official arXiv exact-v1 HTML",
        "method_locator": spec["method"],
        "evaluation_locator": spec["evaluation"],
        "limitations_locator": spec["limitations"],
        "claim_boundary": spec["boundary"],
        "adopted_proposition": spec["proposition"],
        "score": spec["score"],
        "review_depth": "deep",
        "completion_result": "complete",
        "owner_node": spec["owner_node"],
        "books_decision": spec["decision"],
        "evidence_reuse_basis": "fresh non-author reopened the closure and reviewed official exact-v1 HTML",
    })
evidence["items"].sort(key=lambda item: item["arxiv_id"])
evidence["count"] = 91
evidence["deep_complete_count"] = 91
evidence["standard_complete_count"] = 0
evidence["blocked_count"] = 0
evidence["score_distribution"] = {"7": 22, "8": 59, "9": 10}
dump("evidence-review-v3.json", evidence)
dump("exact-v1-review-packet.json", {
    "schema": "daily-exact-v1-review-packet-v3",
    "report_date": "2026-05-27",
    "items": evidence["items"],
})


# 3. Add one bounded No Change comparison and one true Integrate decision.
books = load("books-comparison-v3.json")
for aid, spec in REOPENED.items():
    books["items"].append({
        "arxiv_id": aid,
        "source_family_id": spec["source_family_id"],
        "owner_node": spec["owner_node"],
        "owner_path": spec["owner_path"],
        "adjacent_paths": ([
            "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
            "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        ] if aid == "2605.25333" else [
            "books/part-07-agent/75-context.md",
            "books/part-07-agent/77-memory.md",
        ]),
        "adopted_proposition": spec["proposition"],
        "existing_proposition": spec["existing"],
        "coverage_anchor": spec["coverage_anchor"],
        "coverage_difference": spec["difference"],
        "evidence_boundary": spec["boundary"],
        "decision": spec["decision"],
        "binding_marker": None,
        "author_check": (
            "Main-body heading/excerpt before the first H2 Review notes already carries the durable proposition; exact difference is recorded."
            if spec["decision"].startswith("No Change") else
            "Current main body carries the general data-movement premise but not the adopted PIM graph-ANNS co-design delta; root serialized writeback is required."
        ),
    })
books["items"].sort(key=lambda item: item["arxiv_id"])
books["count"] = 91
books["applied_count"] = 57
books["no_change_count"] = 33
books["pending_integrate_count"] = 1
dump("books-comparison-v3.json", books)
dump("books-current-content-comparison.json", books)


# 4. Preserve sixteen applied queue entries and add one exact root writeback.
queue["items"].append({
    "arxiv_id": "2605.25522",
    "source_family_id": REOPENED["2605.25522"]["source_family_id"],
    "owner": "root",
    "owner_node": "AGENT-RAG",
    "target_path": "books/part-07-agent/76-rag.md",
    "unique_anchor": "多向量检索的数据面要避免搬运高精度向量",
    "adopted_proposition": REOPENED["2605.25522"]["proposition"],
    "proposed_delta": (
        "在通用 host/device retrieval data-plane 之后增加 PIM graph-ANNS 分支：compact index 先减少分区和 remote traversal，"
        "异步 mini-batch pipeline 重叠 host dispatch/PU search/rerank；host rerank/transfer 成为新瓶颈时，必须用相同 recall 下的"
        "overfetch、QPS、energy 和 tail latency 决定是否保留该分支。"
    ),
    "evidence_boundary": REOPENED["2605.25522"]["boundary"],
    "trade_off": "PIM residency 与高内部带宽换来 index 副本、partition、host coordination、overfetch 和专用 kernel 复杂度。",
    "failure_mode": "跨 PU 通信、load imbalance 或 host rerank/transfer 可吞掉 PIM 收益；过小 overfetch 则直接损害 recall。",
    "fallback": "无法在同一 recall 与端到端 workload 下闭合时，回退已验证的 CPU/GPU ANN、普通 hybrid refinement 或容量扩展。",
    "exact_v1_locators": {
        "method": REOPENED["2605.25522"]["method"],
        "evaluation": REOPENED["2605.25522"]["evaluation"],
        "limitations": REOPENED["2605.25522"]["limitations"],
    },
    "status": "pending_root_serialized_writeback",
})
queue["items"].sort(key=lambda item: item["arxiv_id"])
queue["status"] = "one_bounded_root_writeback_pending_then_new_fresh_review"
queue["pending_count"] = 1
queue["note"] = (
    "Sixteen earlier entries remain applied_pending_fresh_review. Fresh closure challenge reopened 2605.25522 and found one true AGENT-RAG delta; "
    "only that bounded binding is pending root writeback."
)
dump("root-books-writeback-queue-v3.json", queue)


# 5. Synchronize source and author audit counts without claiming final passage.
coverage = load("source-coverage-v3.json")
for source in coverage["sources"]:
    if source["source_id"] == "SRC-ARXIV":
        source["limitation"] = "691 arXiv raw = 90 retained + 601 closure"
dump("source-coverage-v3.json", coverage)

audit = load("author-adversarial-audit-v3.json")
audit["status"] = "fresh_review_bounded_repair_pending_one_root_writeback_and_new_fresh_review"
audit["challenges"]["false_negative"] = (
    "Fresh challenge reopened 2605.25333 and 2605.25522 from the frozen 601-closure partition; no source/date expansion occurred."
)
audit["challenges"]["evidence"] = "91 exact-v1/page records have method, evaluation and limitations/counterevidence locators"
audit["challenges"]["books"] = "57 Applied + 33 No Change + 1 bounded Integrate (2605.25522) pending root writeback"
audit["gates"]["candidate_denominator"] = "BOUNDED_REPAIR_PENDING_NEW_FRESH_REVIEW"
audit["gates"]["evidence"] = "BOUNDED_REPAIR_PENDING_NEW_FRESH_REVIEW"
audit["gates"]["books"] = "ONE_BOUNDED_ROOT_WRITEBACK_PENDING"
audit["gates"]["fresh_non_author"] = "REPAIR_AUTHOR_CANNOT_SELF_SIGN"
dump("author-adversarial-audit-v3.json", audit)


# 6. Update the human-readable report with the same frozen projection.
text = REPORT.read_text()
text = text.replace("692 = 89 retained + 603 pre-denominator closure + 0 withdrawn", "692 = 91 retained + 601 pre-denominator closure + 0 withdrawn")
text = text.replace("89 项均完成 exact-v1/官方技术页深入审阅", "91 项均完成 exact-v1/官方技术页深入审阅")
text = text.replace("89 deep + 0 standard + 0 blocked", "91 deep + 0 standard + 0 blocked")
text = text.replace("22 score7 + 57 score8 + 10 score9", "22 score7 + 59 score8 + 10 score9")
text = text.replace("57 Applied + 32 No Change + 0 pending Integrate", "57 Applied + 33 No Change + 1 pending Integrate")
text = text.replace("32 项均记录", "33 项均记录")
text = text.replace("原 16 项 gap 已由 root 串行写入 canonical owner，并通过 paired marker 与位置检查。报告仍保持 Ongoing，等待不同 fresh non-author 做写后语义终审。", "原 16 项 gap 已由 root 串行写入 canonical owner，并通过 paired marker 与位置检查；fresh closure challenge 另恢复两项，其中 2605.25333 为现有覆盖，2605.25522 形成一项新的有界 root writeback。报告保持 Ongoing，等待该写回和新的 fresh non-author 复核。")
text = text.replace("691 arXiv raw = 88 retained + 603 closure", "691 arXiv raw = 90 retained + 601 closure")

def add_table_row(before_aid: str, aid: str, spec: dict) -> None:
    global text
    needle = f"| [{before_aid} "
    pos = text.index(needle)
    score = spec["score"]
    if spec["decision"].startswith("No Change"):
        decision = f"已有覆盖 [章节](../../../../{spec['owner_path']})：{spec['owner_node']}"
    else:
        decision = f"整合：待 root 串行写回 [章节](../../../../{spec['owner_path']})：{spec['owner_node']}"
    row = (
        f"| [{aid} {spec['title']}](https://arxiv.org/html/{aid}v1) | 2026-05-27T08:00:00+08:00 | "
        f"{spec['proposition']}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']} | 深入完成 | {decision} |\n"
    )
    text = text[:pos] + row + text[pos:]

add_table_row("2605.25338", "2605.25333", REOPENED["2605.25333"])
add_table_row("2605.25535", "2605.25522", REOPENED["2605.25522"])

def add_detail(before_aid: str, aid: str, spec: dict) -> None:
    global text
    needle = f"### [{before_aid} "
    pos = text.index(needle)
    comparison = (
        f"- **当前正文承载：** `{spec['coverage_anchor']}` — {spec['existing']}\n"
        f"- **差异判断：** {spec['difference']}\n"
        if spec["decision"].startswith("No Change") else ""
    )
    check = (
        "Main-body heading/excerpt before the first H2 Review notes already carries the durable proposition; exact difference is recorded."
        if spec["decision"].startswith("No Change") else
        "Current main body carries the general premise but not the PIM graph-ANNS co-design delta; root serialized writeback is required."
    )
    block = (
        f"### [{aid} {spec['title']}](https://arxiv.org/html/{aid}v1)\n\n"
        f"- **采用命题：** {spec['proposition']}\n"
        f"- **方法定位：** {spec['method']}\n"
        f"- **评价定位：** {spec['evaluation']}\n"
        f"- **限制/反证：** {spec['limitations']}\n"
        f"- **证据边界：** {spec['boundary']}\n"
        f"{comparison}"
        f"- **Books：** `{spec['decision']}`；owner 为 `{spec['owner_node']}` / [`{spec['owner_path']}`](../../../../{spec['owner_path']})。{check}\n\n"
    )
    text = text[:pos] + block + text[pos:]

add_detail("2605.25338", "2605.25333", REOPENED["2605.25333"])
add_detail("2605.25535", "2605.25522", REOPENED["2605.25522"])

gap_start = text.index("## 5. 缺口与下一步")
review_start = text.index("## 6. 复核", gap_start)
gap = """## 5. 缺口与下一步

Evidence 无 candidate blocker。Meta official Publications 的稳定日期列表与 MiMo 未标日期卡片继续作为来源级隔离项，不用于正面 no-hit。fresh challenge 在冻结 692 owner corpus 内恢复 `2605.25333` 与 `2605.25522`；没有扩日期或来源。当前只剩 `2605.25522` 一项精确 root Books writeback，见 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260527/root-books-writeback-queue-v3.json)。写回后必须由另一位未参与本次有界修复的 fresh non-author 复核 601 closure、91 Evidence/score、33 No Change 与 58 Applied binding；本 reviewer 已成为 repair author，不能自签 Complete。

"""
text = text[:gap_start] + gap + text[review_start:]
text = text.replace("- **复核者：** 待不同 fresh non-author reviewer。", "- **复核者：** fresh non-author challenge 已执行；因发现并实施有界修复，本 reviewer 已转为 repair author。")
text = re.sub(r"- \*\*结论：\*\*.*", "- **结论：** 未通过最终 Gate（两项 closure 已修复；一项 root Books writeback 与新的 fresh Gate pending）。", text, count=1)
text = re.sub(r"- \*\*作者检查：\*\*.*", "- **作者检查：** 冻结 corpus 守恒为 692=91+601；91 项 exact-v1 Evidence 已完成；原 16 个 paired binding 保持不变，新增 2605.25522 进入唯一 pending root queue。", text, count=1)
REPORT.write_text(text)


# Final mechanical invariants for this bounded repair.
assert len(screening["items"]) == 692
retained = {item["arxiv_id"] for item in screening["items"] if item["screening_status"] == "retained"}
closures = {item["arxiv_id"] for item in screening["items"] if item["screening_status"] == "pre_denominator_closure"}
eids = {item["arxiv_id"] for item in evidence["items"]}
bids = {item["arxiv_id"] for item in books["items"]}
assert len(retained) == 91 and len(closures) == 601 and retained == eids == bids
assert sum(item["decision"] == "Applied" for item in books["items"]) == 57
assert sum(item["decision"].startswith("No Change") for item in books["items"]) == 33
assert sum(item["decision"] == "Integrate" for item in books["items"]) == 1
assert sum(item["status"] == "pending_root_serialized_writeback" for item in queue["items"]) == 1

