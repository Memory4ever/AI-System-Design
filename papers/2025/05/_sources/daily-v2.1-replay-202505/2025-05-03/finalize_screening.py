#!/usr/bin/env python3
"""Freeze the 2025-05-03 semantic-screening decisions from the official snapshot."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "screening-ledger.json"

OWNERS = {
    "2505.03814": "PLATFORM-EVALUATION-SYSTEM",
    "2505.01162": "TRAIN-RLHF",
    "2505.01049": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2505.01386": "PLATFORM-COST",
    "2505.01538": "AGENT-RAG",
    "2505.01484": "PLATFORM-SECURITY",
    "2505.01420": "PLATFORM-EVALUATION-SYSTEM",
    "2505.01481": "PLATFORM-EVALUATION-SYSTEM",
    "2505.01067": "PLATFORM-SECURITY",
    "2505.01524": "PLATFORM-SECURITY",
    "2505.03804": "INFER-TENSORRT-LLM",
    "2505.02854": "PLATFORM-EVALUATION-SYSTEM",
    "2505.01618": "TRAIN-PRETRAINING",
    "2505.00982": "TRAIN-DISTRIBUTED-TRAINING",
    "2505.01572": "INFER-SPECULATIVE-DECODING",
    "2505.01099": "TRAIN-PIPELINE-PARALLEL",
    "2505.01595": "PLATFORM-EVALUATION-SYSTEM",
    "2505.01637": "INFER-TENSORRT-LLM",
    "2505.01616": "PLATFORM-EVALUATION-SYSTEM",
    "2505.00949": "INFER-SCHEDULING",
    "2505.01164": "AGENT-RAG",
    "2505.01479": "AGENT-PLANNING",
    "2505.01592": "PLATFORM-EVALUATION-SYSTEM",
}


def closure(title: str, abstract: str, categories: list[str]) -> tuple[str, str]:
    text = f"{title} {abstract}".lower()
    cat = ",".join(categories)
    if any(k in text for k in ("survey", "systematic review", "position:", "perspective")):
        return "survey_or_position", (
            f"《{title}》是综述、立场或问题盘点；可作 discovery clue，但未给出会改变长期 AI-System "
            "state/data/control ownership 或 release contract 的新机制。"
        )
    if any(k in text for k in ("medical", "clinical", "radiolog", "patient", "tumor", "health", "agricultur", "crop", "farm", "water management")):
        return "domain_application", (
            f"《{title}》验证特定医疗、农业或行业 workload；其贡献停留在领域任务/数据，不改变通用 AI-System 合同。"
        )
    if any(k in text for k in ("segmentation", "object detection", "pose estimation", "depth estimation", "image enhancement", "forecasting", "classification")):
        return "local_model_quality", (
            f"《{title}》主要改善单一视觉/预测任务的模型质量；未改变训练、推理、平台或 evaluation 的长期 owner。"
        )
    if any(k in text for k in ("robot", "driving", "autonomous", "navigation", "manipulation", "visuomotor", "embodied")):
        return "embodied_local_method", (
            f"《{title}》是特定机器人、驾驶或 embodied task 方法；没有形成可跨 workload 复用的 world-state/control contract。"
        )
    if any(k in text for k in ("federated", "wireless", "6g", "satellite", "vehicular", "iot", "network")):
        return "adjacent_system", (
            f"《{title}》属于联邦学习、网络或通信相邻系统；本窗口证据未改变本书 AI model lifecycle 的核心控制面。"
        )
    if any(k in text for k in ("quantum", "wasserstein", "bilevel", "optimality", "convergence", "causal graph", "theorem")):
        return "general_theory", (
            f"《{title}》提供一般优化/统计理论或局部算法；尚未连接到可验证的 AI-System workload、state owner 与运行约束。"
        )
    if any(k in text for k in ("attack", "security", "privacy", "watermark", "vulnerab", "poison")):
        return "local_security_case", (
            f"《{title}》覆盖一个局部攻击、防御或 privacy case；未改变现有 provenance、authorization、supply-chain 或 release-gate 主线。"
        )
    if any(k in text for k in ("rag", "agent", "llm", "language model", "transformer", "diffusion", "foundation model")):
        return "ai_local_method", (
            f"《{title}》虽属于 AI 研究，但只呈现局部方法、prompt、数据或 benchmark 增量；未达到长期机制候选门槛。"
        )
    return "out_of_scope", (
        f"《{title}》（{cat}）与注册窗口有关，但没有改变本项目 AI-System 知识树中的机制、所有权或证据合同。"
    )


data = json.loads(LEDGER.read_text())
for item in data["records"]:
    arxiv_id = item["arxiv_id"]
    item["semantic_screen_status"] = "complete"
    if arxiv_id in OWNERS:
        item["semantic_decision_kind"] = "retained"
        item["stable_node_id"] = OWNERS[arxiv_id]
        item["family_specific_reason"] = (
            "保留：title+abstract 显示其直接改变长期 AI-System mechanism、state/data/control ownership、"
            "evaluation/release contract 或训练/推理/平台设计判断；进入 exact-v1 Source Review。"
        )
        item["closure_bucket"] = "retained"
    else:
        bucket, reason = closure(item["title"], item["abstract"], item["categories"])
        item["semantic_decision_kind"] = "pre-denominator-closure"
        item["stable_node_id"] = "—"
        item["family_specific_reason"] = reason
        item["closure_bucket"] = bucket

counts = Counter(item["closure_bucket"] for item in data["records"])
data["semantic_screen_completed_at"] = "2026-08-31T18:20:00+08:00"
data["candidate_denominator_count"] = counts["retained"]
data["pre_denominator_closure_count"] = len(data["records"]) - counts["retained"]
data["closure_reason_counts"] = dict(sorted(counts.items()))
canonical = "\n".join(sorted(f"arxiv:{item['arxiv_id']}" for item in data["records"] if item["semantic_decision_kind"] == "retained"))
data["denominator_id"] = "DEN-20250503-" + hashlib.sha256(canonical.encode()).hexdigest()[:20]
LEDGER.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

columns = [
    "arxiv_id", "source_family_key", "submitted_v1_utc", "submitted_v1_asia_shanghai",
    "title", "abstract", "categories", "screening_route", "prior_weekly_trace",
    "semantic_screen_status", "semantic_decision_kind", "stable_node_id",
    "closure_bucket", "family_specific_reason",
]
with (ROOT / "screening-ledger.tsv").open("w", newline="") as fh:
    writer = csv.DictWriter(
        fh, fieldnames=columns, delimiter="\t", extrasaction="ignore", lineterminator="\n"
    )
    writer.writeheader()
    for item in data["records"]:
        row = dict(item)
        row["categories"] = ";".join(item["categories"])
        writer.writerow(row)

(ROOT / "retained-arxiv-ids.txt").write_text(
    "".join(
        f"{item['arxiv_id']}\n"
        for item in data["records"]
        if item["semantic_decision_kind"] == "retained"
    )
)

print(json.dumps({
    "registered": len(data["records"]),
    "retained": counts["retained"],
    "closed": len(data["records"]) - counts["retained"],
    "denominator_id": data["denominator_id"],
    "closure_reason_counts": data["closure_reason_counts"],
}, ensure_ascii=False, indent=2))
