#!/usr/bin/env python3
"""Configure the shared June V3 recovery builder for 2026-06-30."""

from pathlib import Path
import json
import runpy


ROOT = Path(__file__).resolve().parents[5]
builder = runpy.run_path(
    ROOT / "papers/2026/06/_sources/daily-20260624/build_v3_report.py",
    run_name="daily_v3_shared",
)
globals_for_main = builder["main"].__globals__
globals_for_main["DAY"] = "2026-06-30"
globals_for_main["SOURCE_DIR"] = ROOT / "papers/2026/06/_sources/daily-20260630"
globals_for_main["REPORT"] = ROOT / "papers/2026/06/30/README.md"
globals_for_main["SELECTED"] = set(
    "28361 28379 28425 28430 28434 28436 28565 28661 28679 28690 "
    "28739 28781 28831 28839 28925 28958 29033 "
    "29054 29073 29094 29151 29159 29207 29225 29279 29424 29472 "
    "29490 29554 29563 29565 29601 29629 29708 29718 29788 "
    "29871 29914 29920 29957 29982 29986 30005 30119 30265 30383 "
    "30389 30391 30449 30531 30560 30566 30602 30634".split()
)
globals_for_main["INTEGRATE_IDS"] = {"28361", "28661", "29151", "29472", "29565", "29601"}
globals_for_main["CLOSURE_OVERRIDES"] = {
    "28666": "把既有 TRiSM、least privilege 与 defence-in-depth 用于医疗报告；题摘给出垂直实证，没有新增可迁移的 agent security state/authority contract",
    "29030": "在 MCQ agent 中插入错误 memory 并测 accuracy/ASR，只复现 memory 可污染输出；没有 memory admission/provenance/repair 或新的评估控制契约",
    "29775": "摘要明确目标是 MIG 上的 smaller ML models；MF-MARL repartition 与 heuristic scheduling 是通用 GPU job scheduler，不是大模型基础设施特有贡献",
}
builder["main"]()

audit_path = globals_for_main["SOURCE_DIR"] / "v3-admission-audit-20260910.json"
audit = json.loads(audit_path.read_text())
audit["independent_boundary_audit"] = {
    "reviewed_at": "2026-09-10T21:20:00+08:00",
    "retained_or_recovered": ["28839", "28925", "29054", "29159", "29490", "29914", "29920", "30566"],
    "closure_upheld": ["28385", "28900", "29580"],
    "fresh_de_admitted": ["28666", "29030", "29775"],
    "finding": "eight general agent-control and evaluation papers remain retained; 28666, 29030, and 29775 are family-specific pre-denominator closures",
    "false_positive_corrections": {
        "28955": "generic value-based RL on gridworld and MuJoCo, not a large-model or LLM-infrastructure contribution",
        "29038": "agent-based model plus evolutionary optimization pipeline, not an LLM-agent evaluation contribution",
    },
}
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
