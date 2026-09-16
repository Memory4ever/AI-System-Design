#!/usr/bin/env python3
"""Configure the shared June V3 recovery builder for 2026-06-26."""

from pathlib import Path
import json
import runpy


ROOT = Path(__file__).resolve().parents[5]
builder = runpy.run_path(
    ROOT / "papers/2026/06/_sources/daily-20260624/build_v3_report.py",
    run_name="daily_v3_shared",
)
globals_for_main = builder["main"].__globals__
globals_for_main["DAY"] = "2026-06-26"
globals_for_main["SOURCE_DIR"] = ROOT / "papers/2026/06/_sources/daily-20260626"
globals_for_main["REPORT"] = ROOT / "papers/2026/06/26/README.md"
globals_for_main["SELECTED"] = set(
    "26156 26185 26298 26300 26344 26356 26377 26383 26429 26449 "
    "26453 26472 26479 26511 26524 26607 26649 26666 26669 26721 "
    "26744 26836 26875 26918 26924 26978 26979 26990 26997 "
    "27009 27027 27045 27153 27154 27226 27288".split()
)
globals_for_main["INTEGRATE_IDS"] = {"26383"}
globals_for_main["CLOSURE_OVERRIDES"] = {
    "27005": "通用异构 AI model population 的 fairness/interpretability composite-utility simulation；没有大模型特有 workload/state 或真实基础设施 contract",
}
builder["main"]()

audit_path = globals_for_main["SOURCE_DIR"] / "v3-admission-audit-20260910.json"
audit = json.loads(audit_path.read_text())
audit["independent_boundary_audit"] = {
    "reviewed_at": "2026-09-10T21:20:00+08:00",
    "retained_or_recovered": ["26383", "26453", "26836", "26918", "26978", "27045", "27226"],
    "closure_upheld": ["26456", "27079"],
    "fresh_de_admitted": ["27005"],
    "finding": "seven general performance, evaluation, agent-control, and resource-contract papers remain retained; 27005 is a generic AI resource-allocation simulation and is closed before the candidate denominator",
}
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
