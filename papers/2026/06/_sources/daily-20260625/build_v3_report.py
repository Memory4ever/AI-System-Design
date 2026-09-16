#!/usr/bin/env python3
"""Configure the shared June V3 recovery builder for 2026-06-25."""

from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[5]
builder = runpy.run_path(
    ROOT / "papers/2026/06/_sources/daily-20260624/build_v3_report.py",
    run_name="daily_v3_shared",
)
globals_for_main = builder["main"].__globals__
globals_for_main["DAY"] = "2026-06-25"
globals_for_main["SOURCE_DIR"] = ROOT / "papers/2026/06/_sources/daily-20260625"
globals_for_main["REPORT"] = ROOT / "papers/2026/06/25/README.md"
globals_for_main["SELECTED"] = set(
    "24934 24957 24996 24998 25091 25097 25098 25115 25161 "
    "25189 25191 25349 25353 25447 25449 25487 25519 "
    "25605 25721 25759 25760 25782 25819 26027 26028 26057 "
    "26071".split()
)
globals_for_main["INTEGRATE_IDS"] = {"25353"}
globals_for_main["CLOSURE_OVERRIDES"] = {
    "25082": "通用 AI/ML job 的单 MIG simulation/RL repartitioning；题摘没有 LLM token、KV、parallel state 或大模型 lifecycle contract",
    "25285": "EPTS/MS-HiLoRA 与 feature mixer 是多稀疏度局部模型压缩 recipe；可部署多个 sparsity 不等于 runtime/serving control contract",
    "25453": "EmuGEMM 面向科学计算高精度 GEMM 的低精度 Tensor Core 精度模拟；不是大模型或大模型基础设施特有的长期机制",
    "25608": "把既有 HybridRAG、KG 与 Multi-LLM 组合用于德国 IT-Grundschutz 认证；贡献对象是垂直认证流程，没有新的通用 security authority/effect/release 机制",
}
builder["main"]()
