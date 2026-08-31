#!/usr/bin/env python3
"""Apply the root-requested exact-v1 denominator challenge for 2026-05-03.

This is an author-side repair packet.  It must not be interpreted as the
independent fresh-context Semantic Audit required to close the Daily Gates.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
JSON_PATH = HERE / "screening-ledger-v2.1.json"
TSV_PATH = HERE / "screening-ledger-v2.1.tsv"


REOPEN = {
    "2605.01186": ("SF-ATTACK-AGENT-TERMINAL-FINGERPRINT", "PLATFORM-SECURITY", [3, 3, 3]),
    "2605.01247": ("SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT", "PLATFORM-SECURITY", [3, 3, 2]),
    "2605.01284": ("SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN", "AGENT-RAG", [3, 3, 3]),
    "2605.01293": ("SF-LOGIC-GROUNDED-SKILL-INDUCTION", "AGENT-WORKFLOW", [3, 3, 3]),
    "2605.01471": ("SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY", "PLATFORM-EVALUATION-SYSTEM", [3, 3, 3]),
    "2605.01560": ("SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE", "AGENT-WORKFLOW", [3, 3, 3]),
    "2605.01566": ("SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION", "AGENT-MULTI-AGENT", [3, 3, 2]),
    "2605.01660": ("SF-AGENT-GENERATED-VERIFIED-COMPILER", "PLATFORM-EVALUATION-SYSTEM", [3, 3, 3]),
}


CLOSE = {
    "2605.01208": (
        "exact-v1 的 Faithful-Agent 在 mobile-GUI workload 中用 evidence-perturbation SFT、"
        "abstention 与 GuAE/GRPO 解决 sparse-reward rollout group 的 advantage collapse，并以"
        " thought-action consistency reward 提高所测 Trap success。该增量仍是特定 VLM-agent"
        " 的 post-training objective/estimator 分支：它没有把 evidence identity、action commit、"
        " runtime verifier 或 recovery owner 外移成可跨 agent 复用的系统合同，且没有证明跨 GUI、"
        "模型与 live-environment drift 的校准。因此保留为 pre-denominator closure。重开条件："
        "后续证据需证明训练外的 verifier/abstention state 能在 action boundary 可靠执行，并披露"
        "OOD、延迟、恢复与错误拒绝边界。"
    ),
    "2605.01346": (
        "exact-v1 的 CHASE 用 competing temporal hypotheses 的 score margin 训练 selective"
        " predictor，在 GUV hidden-connectivity simulator 与少量真实视频 qualitative transfer"
        " 中决定 commit/abstain。它把单一 confidence 改为结构化歧义比较，但证明范围仍绑定"
        "该物理推断任务与作者 coverage/risk protocol；没有给出可跨 workload 校准的 uncertainty"
        " state、平台 release threshold 或 action authority。因此保留为领域 selective-prediction"
        " closure。重开条件：跨模型、跨任务校准与真实 action-boundary deployment 证明该 margin"
        " 可作为通用 release/commit sensor。"
    ),
    "2605.01415": (
        "exact-v1 以 decision-energy density、irreversibility 与三类 sovereignty boundary"
        "提出制度/系统安全框架，并给出 boundary-stabilization 的形式化论述。它能够解释为何"
        "单节点不应同时拥有评估、选择与不可逆执行权，但当前证据主要是概念模型：没有可操作"
        " threat model、runtime reference monitor、false-positive/availability budget、绕过实验"
        "或跨系统部署验证，因而不能直接改变现有 Security enforcement contract。保留为"
        "pre-denominator closure。重开条件：把 boundary theorem 映射到可执行授权状态机并用"
        "真实或可复现实验验证 enforcement、fallback 与责任隔离。"
    ),
    "2605.01489": (
        "exact-v1 的 SciResearcher 构建 frontier-science 的 agentic data pipeline，并用该数据"
        "进行 SFT 与 agentic RL，报告 HLE-Bio/Chem-Gold、SuperGPQA-Hard-Biology 与 TRQA-"
        "Literature 上的模型结果。其核心增量是科学领域的自动任务/证据数据构造与一个 8B 模型，"
        "而不是新的通用 data owner、provenance admission、optimizer/checkpoint 或 workflow"
        " commit contract；跨领域与数据污染/正确性边界也未闭合。因此保留为领域 data-method"
        " closure。重开条件：证明其数据 lineage、verification 与 curriculum 机制能跨领域稳定"
        "改变通用 Training/Agent lifecycle。"
    ),
    "2605.01502": (
        "exact-v1 的 RADMI 在 seismic-facies segmentation 中用相邻 decoder layer 的 mutual"
        " information aggregation 作为单次前向 uncertainty proxy，并与 deep-ensemble"
        " uncertainty 的相关性比较。该结果是 encoder-decoder dense-prediction 的局部 sensor，"
        "没有证明它是 calibrated epistemic probability、能跨 architecture/task 保持排序，或"
        "足以拥有 release/abstain/action commit 权。因此保留为模型局部 uncertainty-method"
        " closure。重开条件：跨域校准、failure slice 与 downstream decision-cost 实验证明其能"
        "改变平台级 uncertainty/evaluation contract。"
    ),
    "2605.08138": (
        "exact-v1 的 DataArc-SynData-Toolkit 把多路径、多模态、多语言 synthetic-data"
        " generation 封装为配置驱动 pipeline、统一 schema 与可视化/CLI，并在若干应用场景"
        "报告效率/质量。它主要是工具集成与产品化实现；正文没有建立新的 dataset identity、"
        "source/license lineage、quality-owner、contamination gate 或 downstream rollback"
        " invariant，也没有证明跨模型/任务的因果收益。因此保留为 toolkit closure。重开条件："
        "提供版本化数据 lineage、可复算质量合同、污染/授权传播和训练后回滚证据，使 Data"
        " lifecycle 的 owner 或 gate 发生变化。"
    ),
}


data = json.loads(JSON_PATH.read_text())
by_id = {row["arxiv_id"]: row for row in data["rows"]}

for arxiv_id, (family, owner, score) in REOPEN.items():
    by_id[arxiv_id].update(
        screening_decision="retain",
        source_family_id=family,
        stable_node_id=owner,
        score_v2=score,
        closure_reason="—",
    )

for arxiv_id, reason in CLOSE.items():
    by_id[arxiv_id].update(
        screening_decision="pre_denominator_closure",
        source_family_id="—",
        stable_node_id="—",
        score_v2=[],
        closure_reason=reason,
    )

reopened = set(data.get("false_negative_author_audit", {}).get("reopened", []))
reopened.update(REOPEN)
data["candidate_denominator_count"] = sum(
    row["screening_decision"] == "retain" for row in data["rows"]
)
data["pre_denominator_closure_count"] = sum(
    row["screening_decision"] == "pre_denominator_closure" for row in data["rows"]
)
data["retained_candidates"] = data["candidate_denominator_count"]
data["pre_denominator_closures"] = data["pre_denominator_closure_count"]
data["false_negative_author_audit"] = {
    "reopened": sorted(reopened),
    "challenged_exact_v1": sorted(set(REOPEN) | set(CLOSE)),
    "result": (
        "sixteen false negatives corrected across author-side audits; latest exact-v1 "
        "root challenge reopened eight and retained six family-specific closures; "
        "independent fresh-context audit remains open"
    ),
}

JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
fields = list(data["rows"][0])
with TSV_PATH.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
    writer.writeheader()
    writer.writerows(data["rows"])

print(data["candidate_denominator_count"], data["pre_denominator_closure_count"])
