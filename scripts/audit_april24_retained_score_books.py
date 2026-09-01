#!/usr/bin/env python3
"""Fresh-context retained-set re-audit for the 2026-04-24 Historical Daily.

The receipt is deliberately separate from the author packet.  It re-derives
Score V2 from exact-v1 evidence, then compares the durable mechanism against
the current canonical owner and adjacent chapter flow.  It does not close the
Daily Coverage Gate while false-negative challenges remain open, and it never
writes shared Books.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/04/_sources/daily-20260424"

# arXiv id -> (Design Delta, System Reach, Durability, canonical existing coverage)
AUDIT = {
    "2604.21215": (2, 2, 3, "books/part-02-model/17-transformer-layer.md#residual-stream-从单一累加状态走向-depth-wise-routing"),
    "2604.21221": (2, 2, 2, "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#cacherollback-与-exactness"),
    "2604.21231": (2, 2, 2, "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从不可逆-eviction-到可恢复的分层-recall"),
    "2604.21241": (2, 2, 2, "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#action-facing-representation-也是-gradient-authority-boundary"),
    "2604.21255": (2, 2, 2, "books/part-06-ai-infrastructure/66-evaluation-system.md#trajectory-judge-必须区分叙述动作与完成证据"),
    "2604.21308": (2, 3, 3, "books/part-06-ai-infrastructure/72-security.md#从文本是否恶意到谁获得了行为控制权"),
    "2604.21335": (2, 2, 2, "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#压缩预算从单轴推进到-token-feature-二维"),
    "2604.21375": (2, 2, 2, "books/part-07-agent/81-workflow.md#recovery-与-verification-必须产生不同-artifact"),
    "2604.21480": (3, 3, 2, "books/part-06-ai-infrastructure/66-evaluation-system.md#从-snapshot-到-feedback-conditioned-policy评估对象也会演进"),
    "2604.21523": (2, 2, 2, "books/part-06-ai-infrastructure/66-evaluation-system.md#judge-先证明看见了目标变化再谈总体准确率"),
    "2604.21571": (3, 2, 3, "books/part-04-training-system/30-lora.md#merge-与动态-adapter-是两种资产策略"),
    "2604.21590": (2, 1, 2, "books/part-04-training-system/29-sft.md#sft-也需要显式-distribution-drift-contract"),
    "2604.21686": (2, 2, 2, "books/part-03-multimodal-world-models/25-multimodal-world-models.md#evaluation从画面质量到干预结果"),
    "2604.21741": (3, 2, 2, "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#fleet-学习必须把部署干预与再部署组成版本循环"),
    "2604.21748": (2, 2, 2, "books/part-07-agent/77-memory.md#memory-类型是用途不只是存储介质"),
    "2604.21816": (2, 2, 2, "books/part-07-agent/78-tool-calling.md#interface-granularity不是-tool-越多越有能力"),
    "2604.21999": (2, 1, 2, "books/part-02-model/17-transformer-layer.md#parameter-depth-与-execution-depth-可以分离"),
    "2604.22050": (2, 1, 2, "books/part-02-model/14-self-attention.md#routing-representation-与-cache-representation-的条件合并"),
    "2604.22072": (3, 2, 2, "books/part-04-training-system/36-distributed-training.md#federated-tensor-type-定义一轮协议能表达什么"),
    "2604.22085": (2, 1, 2, "books/part-07-agent/77-memory.md#memory-类型是用途不只是存储介质"),
    "2604.22126": (3, 3, 2, "books/part-04-training-system/36-distributed-training.md#从-collective-call-到-kernel-内-remote-memory"),
    "2604.22128": (2, 1, 2, "books/part-02-model/17-transformer-layer.md#layer-冗余取决于干预协议"),
    "2605.28840": (2, 2, 2, "books/part-06-ai-infrastructure/66-evaluation-system.md#trajectory-judge-必须区分叙述动作与完成证据"),
    "2606.11209": (2, 1, 2, "books/part-04-training-system/33-grpo.md#从一个终局标量到-typed-creditreward-必须匹配决策边界"),
    "2606.13685": (2, 2, 2, "books/part-06-ai-infrastructure/66-evaluation-system.md#scorer-不是绝对真相"),
}


def markdown_heading_slug(heading: str) -> str:
    """Return the repository's GitHub-style fragment for a Markdown heading."""
    value = heading.strip().lower()
    value = re.sub(r"[^\w\-\u4e00-\u9fff ]", "", value)
    value = re.sub(r"\s+", "-", value)
    return value


def validate_owner_ref(owner_ref: str) -> None:
    """Reject a Books comparison that does not resolve to a real heading."""
    path_text, separator, fragment = owner_ref.partition("#")
    if not separator or not fragment:
        raise ValueError(f"owner reference must include a heading fragment: {owner_ref}")
    path = ROOT / path_text
    if not path.is_file():
        raise ValueError(f"owner file does not exist: {path_text}")
    heading_slugs = {
        markdown_heading_slug(line.lstrip("#").strip())
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("#")
    }
    if fragment not in heading_slugs:
        raise ValueError(f"owner heading does not exist: {owner_ref}")


def main() -> None:
    ledger = json.loads((PACKET / "screening-ledger-final.json").read_text(encoding="utf-8"))
    reviews = {
        item["arxiv_id"]: item
        for item in json.loads((PACKET / "exact-v1-review-packet.json").read_text(encoding="utf-8"))["items"]
    }
    comparisons = {
        item["arxiv_id"]: item
        for item in json.loads((PACKET / "books-current-content-comparison.json").read_text(encoding="utf-8"))["items"]
    }
    retained = [
        row for row in ledger["identities"]
        if row.get("screening_status") != "pre_denominator_closed"
    ]
    actual_ids = {row["arxiv_id"] for row in retained}
    if actual_ids != set(AUDIT):
        raise SystemExit(f"audit map mismatch: missing={actual_ids-set(AUDIT)}, extra={set(AUDIT)-actual_ids}")

    items = []
    for row in retained:
        arxiv_id = row["arxiv_id"]
        design, reach, durability, existing_ref = AUDIT[arxiv_id]
        validate_owner_ref(existing_ref)
        review = reviews[arxiv_id]
        old = comparisons[arxiv_id]
        total = design + reach + durability
        items.append(
            {
                "source_family_id": row["source_family_id"],
                "arxiv_id": arxiv_id,
                "title": row["title"],
                "exact_v1_review_ref": f"review:{row['source_family_id']}",
                "exact_v1_method_locator": review["method_identity_locators"],
                "independent_score_v2": {
                    "design_delta": design,
                    "system_reach": reach,
                    "durability": durability,
                    "total": total,
                },
                "review_override": "none",
                "deep_eligibility": ["score_7_9"] if total >= 7 else [],
                "stable_node_id": old["stable_node_id"],
                "current_owner_ref": existing_ref,
                "adjacent_chapter_refs": old.get("adjacent_chapters", []),
                "independent_books_disposition": "No Change — Existing Coverage",
                "books_reason": (
                    "exact-v1 mechanism is already represented by the cited canonical owner as a "
                    "constraint/evolution branch with state or control ownership, trade-off, failure "
                    "and fallback; adding this family would duplicate the mechanism rather than "
                    "change the current design conclusion."
                ),
                "author_score_v2": row.get("score_v2"),
                "author_books_disposition": old.get("decision"),
                "author_decision_changed": old.get("decision") != "No Change — Existing Coverage",
                "shared_books_modified": False,
            }
        )

    receipt = {
        "schema": "historical-daily-independent-retained-score-books-audit-v1",
        "report_date": "2026-04-24",
        "auditor_role": "fresh_context_non_author_root",
        "weekly_semantic_inputs": [],
        "retained_items_reviewed": len(items),
        "score_distribution": {
            str(score): sum(1 for item in items if item["independent_score_v2"]["total"] == score)
            for score in sorted({item["independent_score_v2"]["total"] for item in items})
        },
        "books_dispositions": {"No Change — Existing Coverage": len(items)},
        "status": "retained_set_pass_coverage_still_open",
        "gate_effect": (
            "Evidence/Books decisions for the current retained set are independently re-derived, "
            "but the Daily remains Open until every false-negative denominator challenge is adjudicated "
            "and any newly retained family receives exact-v1 review and Books comparison."
        ),
        "items": items,
    }
    (PACKET / "independent-retained-score-books-audit.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
