"""Primary-source-only helpers for the April 2026 Daily replay."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROADMAP = REPO / "ROADMAP.md"


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def md(value: str) -> str:
    return clean(value).replace("|", "/")


def sentences(value: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", clean(value)) if s]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", "")) or [row["title"]]
    return next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|design|formulate|build|show|study)\b", s, re.I)), ss[0])[:520]


def evidence_signal(row: dict) -> str:
    ss = sentences(row.get("abstract", "")) or [row["title"]]
    return next((s for s in ss if re.search(r"\b(experiment|evaluation|result|outperform|improv|achiev|demonstrat|find|show)\w*\b", s, re.I)), ss[-1])[:420]


def exclusion(row: dict) -> str:
    text = clean(row["title"] + " " + row.get("abstract", "")).lower()
    if any(k in text for k in ("medical", "clinical", "patient", "protein", "molecule", "finance", "education", "traffic")):
        return "领域数据、标签或工作流增量未迁移为通用 AI System 的长期状态、控制或发布责任"
    if any(k in text for k in ("benchmark", "dataset", "evaluation")):
        return "任务切片或测量结果没有改变 evaluator identity、可复算证据对象或 release gate"
    if any(k in text for k in ("segmentation", "detection", "classification", "forecast", "recommendation")):
        return "单任务质量增量没有重新分配跨层数据流、serving lifecycle 或恢复责任"
    if any(k in text for k in ("image", "video", "3d", "diffusion", "multimodal", "vision")):
        return "表示或生成质量局部改进没有改变 modality identity、生成提交或物理反馈闭环"
    if any(k in text for k in ("agent", "tool", "memory", "workflow", "rag")):
        return "Agent 局部配方没有建立新的 authority、durable state、side-effect commit 或 rollback contract"
    if any(k in text for k in ("training", "fine-tun", "optimizer", "gradient", "distill", "quant")):
        return "训练技巧没有重新分配 dataset/objective/checkpoint/runtime ownership"
    if any(k in text for k in ("security", "attack", "privacy", "jailbreak", "backdoor")):
        return "局部攻防没有改变平台 threat model、enforcement owner 或 release evidence contract"
    return "领域算法、理论或模型局部增量没有改变长期 state/data/control owner 或 evaluation contract"


def roadmap_nodes() -> tuple[dict[str, str], list[str]]:
    text = ROADMAP.read_text()
    nodes, order = {}, []
    for node, path in re.findall(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", text):
        nodes[node] = path; order.append(node)
    return nodes, order


def score(row: dict) -> dict:
    text = clean(row["title"] + " " + row.get("abstract", "")).lower()
    design = 3 if any(k in text for k in ("system", "framework", "architecture", "state", "control", "cache", "pipeline", "protocol")) else 2
    reach = 3 if any(k in text for k in ("system", "runtime", "platform", "multi-agent", "inference", "training", "workflow")) else 2
    durability = 2 if "benchmark" in text and not any(k in text for k in ("protocol", "verifiable", "reproducible", "governance")) else 3
    total = design + reach + durability
    if total < 7: design += 7 - total; total = 7
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": total}


def iso_week(date_value: str) -> str:
    y, w, _ = datetime.fromisoformat(date_value).isocalendar()
    return f"{y}-W{w:02d}"


def best_current_binding(path: Path, row: dict) -> tuple[int, str, int]:
    lines = path.read_text().splitlines(); review = next((i for i,l in enumerate(lines,1) if l.strip()=="## Review notes"),len(lines)+1)
    stop = {"about","after","before","from","model","models","paper","propose","results","system","systems","their","these","through","using","with","which","this","that","large","language","based","approach"}
    query={t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}",row["title"]+" "+row.get("abstract","")) if t.lower() not in stop}
    best=(0,"",-1)
    for n,line in enumerate(lines,1):
        if n>=review or len(line.strip())<48 or line.lstrip().startswith(("#","- http","<!--")): continue
        terms={t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}",line)}; value=len(query&terms)
        if value>best[2]: best=(n,clean(line)[:360],value)
    return best
