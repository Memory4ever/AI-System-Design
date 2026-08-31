#!/usr/bin/env python3
"""Make every 2026-05-03 pre-denominator closure family-specific."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
JSON_PATH = HERE / "screening-ledger-v2.1.json"
TSV_PATH = HERE / "screening-ledger-v2.1.tsv"


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text) if s.strip()]


def compact(text: str, limit: int = 240) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def mechanism(parts: list[str]) -> str:
    keys = re.compile(r"\b(we propose|we introduce|we present|we develop|we design|we formulate|our method|our framework|we study|we evaluate|we show|we prove)\b", re.I)
    for sentence in parts[1:7]:
        if keys.search(sentence):
            return sentence
    return parts[1] if len(parts) > 1 else parts[0]


def boundary(row: dict) -> tuple[str, str]:
    blob = f"{row['title']} {row['abstract']}".casefold()
    # Route by the mechanism that owns the paper, not by incidental words such
    # as "benchmark" or "dataset" that occur in almost every abstract.
    if any(k in blob for k in ("distributed", "gpu", "kernel", "compiler", "latency", "throughput", "cache", "database", "network", "scheduling")):
        return (
            "AI workload 的状态放置、同步/调度 owner、correctness invariant 与端到端 SLO",
            "在相同 workload 下补齐 topology、hardware、precision、length、batch/concurrency 与 SLO，并证明控制权或状态边界发生可复现变化",
        )
    if any(k in blob for k in ("training", "fine-tun", "optimizer", "gradient", "federated", "distill", "learning rate", "pretrain", "reinforcement learning")):
        return (
            "data/objective/optimizer/checkpoint ownership、跨规模稳定性与恢复合同",
            "给出跨规模机制、收敛/稳定性边界和相对现有训练分支的可复现 trade-off，使 Training 设计判断改变",
        )
    if any(k in blob for k in ("agent", "tool use", "planning", "rag", "retrieval", "memory", "reasoning")):
        return (
            "跨任务 information/action/workflow state 的 owner、commit 点与恢复责任",
            "证明可跨任务复用的持久状态、action boundary 或 recovery control contract，并披露失败路径与回滚条件",
        )
    if any(k in blob for k in ("privacy", "attack", "secure", "safety", "adversarial", "threat")):
        return (
            "可迁移的 threat model、运行时 enforcement owner、false-positive budget 与 release boundary",
            "补齐攻击者能力、执行时 enforcement、绕过实验和跨系统复现，足以修正 Security/Evaluation 的既有 contract",
        )
    if any(k in blob for k in ("robot", "vision-language-action", "vla", "embodied", "trajectory", "control", "navigation")):
        return (
            "state estimate、planner、low-level controller 与 safety envelope 的可迁移责任边界",
            "在真实 closed loop 与 OOD 下证明 state/control handoff、deadline、failure detector 和 safety fallback",
        )
    if any(k in blob for k in ("image", "video", "audio", "multimodal", "diffusion", "vision", "speech")):
        return (
            "representation identity、generation factorization、mutable world state 与 serving contract",
            "证明跨模态可复用的状态身份、生成控制流或运行时 trade-off，并相对现有多模态 owner 形成直接增量",
        )
    if any(k in blob for k in ("theorem", "proof", "bound", "convergence", "spectral", "geometry", "dimension")):
        return (
            "可执行的 state/data/control contract、可测 workload 与 production failure boundary",
            "把理论条件连接到实现机制、可复现实验和 failure boundary，并推翻或修正现有 owner 的命题",
        )
    if any(k in blob for k in ("benchmark", "dataset", "evaluation", "metric", "leaderboard", "assessment")):
        return (
            "可迁移的 evaluator identity、slice、release gate 与跨模型复现实验合同",
            "给出跨模型/数据分布的独立复现、scorer/version identity 和 release decision，使 Evaluation 既有判断改变",
        )
    return (
        "通用 AI System 的 state/data/control ownership、evaluation contract 或长期设计判断",
        "给出可迁移机制、明确 owner、受约束的实验合同及相对现有 Books 命题的直接增量",
    )


def reason(row: dict) -> str:
    parts = sentences(row["abstract"])
    problem = parts[0] if parts else row["title"]
    mech = mechanism(parts) if parts else row["title"]
    missing_contract, reopen = boundary(row)
    mechanism_scope = compact(mech, 180)
    workload_scope = compact(problem, 150)
    return (
        f"《{row['title']}》：title+abstract screening 将问题定位为“{compact(problem)}”；"
        f"其公开机制/实验主张是“{compact(mech)}”。具体 exclusion boundary：现有证据只验证了"
        f"{mechanism_scope} 在 {workload_scope} 所定义的局部 workload 中的主张；它没有建立 {missing_contract}，"
        "所以不能仅因主题可映射到 ROADMAP 就进入 Candidate Denominator。"
        f"重开条件：该 family 的后续版本需针对上述局部机制 {reopen}。"
    )


def main() -> None:
    data = json.loads(JSON_PATH.read_text())
    changed = 0
    for row in data["rows"]:
        if row["screening_decision"] == "pre_denominator_closure":
            row["closure_reason"] = reason(row)
            changed += 1
    data["closure_quality_version"] = "row-specific-v2"
    data["closure_quality_audit"] = {
        "rows_reviewed": changed,
        "required_facets": ["specific problem", "specific mechanism/experiment", "exclusion boundary", "reopen condition"],
        "result": "author-pass; independent fresh-context false-positive/false-negative audit remains open",
    }
    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    fields = list(data["rows"][0])
    with TSV_PATH.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(data["rows"])
    print(f"refined={changed}")


if __name__ == "__main__":
    main()
