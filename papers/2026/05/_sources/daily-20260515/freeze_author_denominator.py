#!/usr/bin/env python3
"""Freeze the 2026-05-15 author denominator after full title+abstract review."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "screening-ledger-provisional.json"
OUT = ROOT / "screening-ledger-final.json"

RETAIN = {
    "2605.14241", "2605.14249", "2605.14271", "2605.14305", "2605.14421",
    "2605.14460", "2605.14473", "2605.14483", "2605.14591", "2605.14636",
    "2605.14859", "2605.14932", "2605.15030", "2605.15051", "2605.15079",
    "2605.15109", "2605.15132", "2605.15164", "2605.15184", "2605.15185",
    "2605.15238", "2605.15257", "2605.15338", "2605.15377", "2605.15384",
    "2605.15422", "2605.16436", "2605.16439", "2605.18859",
    # Non-author fresh-context recovery.  These families change a durable
    # control/evidence/runtime contract and therefore cannot remain closures.
    "2605.14290", "2605.14415", "2605.14498", "2605.14514", "2605.14570",
    "2605.14678", "2605.14744", "2605.14747", "2605.14786", "2605.14865",
    "2605.14906", "2605.14968", "2605.14978", "2605.15034", "2605.15100",
    "2605.15118", "2605.15128", "2605.15138", "2605.15152", "2605.15155",
    "2605.15172", "2605.15178", "2605.15188", "2605.15403", "2605.15425",
    "2605.15466", "2605.15477",
}


def first_sentence(text: str) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", clean)
    return parts[0][:360]


data = json.loads(SRC.read_text())
rows = data["identities"]
seen = {row["arxiv_id"] for row in rows}
missing = sorted(RETAIN - seen)
if missing:
    raise SystemExit(f"retained IDs missing from window: {missing}")

for row in rows:
    aid = row["arxiv_id"]
    abstract_sentence = first_sentence(row.get("abstract", ""))
    if aid in RETAIN:
        row["screening_status"] = "retained_pending_exact_v1_review"
        row["screening_reason"] = (
            f"{row['title']}：摘要披露的核心问题是“{abstract_sentence}”。该 family 可能改变长期 AI System 的状态、"
            "控制权、evidence/evaluation contract 或训练/推理/平台设计判断，因此进入 denominator；最终结论必须由 exact-v1 决定。"
        )
    else:
        row["screening_status"] = "pre_denominator_closed"
        row["screening_reason"] = (
            f"{row['title']}：其明确研究对象为“{abstract_sentence}”。title+abstract 审计未发现它改变通用 AI System 的"
            " state/data/control ownership、evaluation/release contract 或 Books 既有设计判断；当前只形成领域方法、局部模型改进、"
            "单任务 benchmark/应用证据或非系统性分析。若 exact-v1/artifact 后续显示跨 workload 的新 owner、控制边界或可复算系统合同，则重开。"
        )

data["gate_status"] = "author_denominator_frozen_pending_exact_v1_and_independent_audit"
data["retained_candidates"] = len(RETAIN)
data["pre_denominator_closed"] = len(rows) - len(RETAIN)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
(ROOT / "candidate-ids.txt").write_text("\n".join(sorted(RETAIN)) + "\n")
print(json.dumps({"registered": len(rows), "retained": len(RETAIN), "closures": len(rows) - len(RETAIN)}, ensure_ascii=False))
