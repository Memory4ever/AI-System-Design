#!/usr/bin/env python3
"""Configure the shared June V3 recovery builder for 2026-06-29."""

from pathlib import Path
import json
import runpy


ROOT = Path(__file__).resolve().parents[5]
builder = runpy.run_path(
    ROOT / "papers/2026/06/_sources/daily-20260624/build_v3_report.py",
    run_name="daily_v3_shared",
)
globals_for_main = builder["main"].__globals__
globals_for_main["DAY"] = "2026-06-29"
globals_for_main["SOURCE_DIR"] = ROOT / "papers/2026/06/_sources/daily-20260629"
globals_for_main["REPORT"] = ROOT / "papers/2026/06/29/README.md"
globals_for_main["SELECTED"] = set(
    "27406 27409 27416 27457 27472 27511 27550 27567 27578 "
    "27580 27669 27679 27683 27743 27797 27806 27934 "
    "27944 28013 28050 28061 28116 28235 28279".split()
)
globals_for_main["INTEGRATE_IDS"] = {"27797", "27806"}
globals_for_main["CLOSURE_OVERRIDES"] = {
    "27558": "LinkedIn race/ethnicity fairness measurement 的通用产品 ML 隐私方案；不是大模型或大模型基础设施贡献",
    "27841": "面向 295 个通用 neural architectures 的 task-independent layer-wise energy estimator；没有形成 LLM-specific inference/service contract",
    "27997": "主要对象是 TSC/推荐数据集子集选择，MTEB 只是补充实验；排名保持是通用 benchmark 方法，不是大模型系统贡献",
}
builder["main"]()

audit_path = globals_for_main["SOURCE_DIR"] / "v3-admission-audit-20260910.json"
audit = json.loads(audit_path.read_text())
audit["independent_boundary_audit"] = {
    "reviewed_at": "2026-09-10T21:20:00+08:00",
    "retained_or_recovered": ["27567", "27679", "27934", "27944", "28061", "28235"],
    "closure_upheld": ["27650", "28276"],
    "fresh_de_admitted": ["27558", "27841", "27997"],
    "finding": "six general agent-control and evaluation papers remain retained; 27558, 27841, and 27997 are family-specific pre-denominator closures",
}
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
