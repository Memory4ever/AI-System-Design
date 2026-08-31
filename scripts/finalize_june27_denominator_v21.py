#!/usr/bin/env python3
"""Freeze the fully screened 2026-06-27 durable AI-System denominator.

The provisional ledger is the frozen identity/title/abstract input.  This
script records one source-specific decision for every identity; routing is
used only to report recall and false-negative audit coverage.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260627"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"


# Admission is deliberately strict: every row states the durable mechanism or
# contract that justifies Source Review.  It is not a title-keyword shortlist.
RETAIN = {
    "2606.27632": ("PLATFORM-SECURITY", "把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。"),
    "2606.27634": ("PLATFORM-MONITORING", "把 sequential LoRA personalization 的 checkpoint、reference-set drift 与遗忘监控绑定为持续适配合同。"),
    "2606.27650": ("AGENT-PLATFORM", "把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。"),
    "2606.27669": ("PLATFORM-EVALUATION-SYSTEM", "把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。"),
    "2606.27679": ("PLATFORM-MONITORING", "给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。"),
    "2606.27681": ("MULTIMODAL-WORLD-MODELS", "用 strict mediation 让 textual belief state 成为唯一可测试的预测状态，阻断 history bypass。"),
    "2606.27683": ("PLATFORM-SECURITY", "揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。"),
    "2606.27704": ("PLATFORM-SECURITY", "把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。"),
    "2606.27709": ("TRAIN-DATA", "证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。"),
    "2606.27732": ("MULTIMODAL-GENERATIVE-PARADIGMS", "用 asymmetric bidirectional sidecar 重构 diffusion-LM 的右上下文、KV cache 与 parallel decode 取舍。"),
    "2606.27739": ("TRAIN-GRPO", "把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。"),
    "2606.27743": ("INFER-SCHEDULING", "把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。"),
    "2606.27757": ("AGENT-PLANNING", "把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。"),
    "2606.27780": ("MULTIMODAL-WORLD-MODELS", "给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。"),
    "2606.27791": ("MODEL-LONG-CONTEXT", "以 answer-token NLL degradation 选择保留 full-attention 的层，改变 hybrid attention 的 calibration owner。"),
    "2606.27797": ("TRAIN-DISTRIBUTED-TRAINING", "按 teacher/student 不对称分别选择模型分片与拓扑通信，改变 KD runtime partition contract。"),
    "2606.27806": ("AGENT-PLANNING", "以 parametric transition model 校验 agent imagined delta，并把 disagreement 变成 targeted revision gate。"),
    "2606.27814": ("TRAIN-GRPO", "在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。"),
    "2606.27826": ("PLATFORM-EVALUATION-SYSTEM", "把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。"),
    "2606.27841": ("PLATFORM-COST", "把 inference energy estimation 从整模型 proxy 拆成可跨任务/架构迁移的 layer-wise measurement contract。"),
    "2606.27866": ("MODEL-MOE", "把一次性 MoE compression artifact 改成 nested subnet family 与可在线切换的 budget state。"),
    "2606.27906": ("INFER-REQUEST-LIFECYCLE", "以真实 mobile SoC 证据拆开 vision encoder、prefill、decode、cache 与 thermal phase 的 backend placement。"),
    "2606.27934": ("PLATFORM-EVALUATION-SYSTEM", "用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。"),
    "2606.27936": ("PLATFORM-SECURITY", "证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。"),
    "2606.27944": ("PLATFORM-SECURITY", "以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。"),
    "2606.27962": ("PLATFORM-FOUNDATIONS", "把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。"),
    "2606.27976": ("AGENT-RAG", "把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。"),
    "2606.27997": ("PLATFORM-EVALUATION-SYSTEM", "把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。"),
    "2606.28011": ("AGENT-WORKFLOW", "把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。"),
    "2606.28013": ("PLATFORM-EVALUATION-SYSTEM", "把 autoformalization 的 type correctness 与 semantic equivalence 交叉分层，防止单标量误归因。"),
    "2606.28037": ("PLATFORM-EVALUATION-SYSTEM", "以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。"),
    "2606.28050": ("PLATFORM-EVALUATION-SYSTEM", "用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。"),
    "2606.28061": ("PLATFORM-SECURITY", "把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。"),
    "2606.28070": ("PLATFORM-FOUNDATIONS", "提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。"),
    "2606.28116": ("PLATFORM-MONITORING", "从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。"),
    "2606.28128": ("MULTIMODAL-WORLD-MODELS", "把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。"),
    "2606.28153": ("PLATFORM-SECURITY", "区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。"),
    "2606.28166": ("TRAIN-GRPO", "让 senior/junior 交替共同生成 RLVR rollout，把 handoff compatibility 变成训练目标。"),
    "2606.28187": ("AGENT-MULTI-AGENT", "把 multi-agent interaction 建成可反传 attribution graph，以 token-level influence 分配错误责任。"),
    "2606.28235": ("AGENT-PLATFORM", "用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。"),
    "2606.28276": ("MULTIMODAL-EMBODIED-VLA", "把 video-to-sim reconstruction、digital cousins、policy training 与 sim-to-real rank validity 绑定。"),
    "2606.28277": ("PLATFORM-EVALUATION-SYSTEM", "把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。"),
    "2606.28279": ("AGENT-WORKFLOW", "用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。"),
    "2606.28322": ("PLATFORM-EVALUATION-SYSTEM", "以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。"),
    "2606.28430": ("PLATFORM-EVALUATION-SYSTEM", "用 no-op ablation 揭示 coding agent 可通过 oracle 却未交付可复用 artifact 的 construction-validity failure。"),
    "2606.28433": ("PLATFORM-EVALUATION-SYSTEM", "要求 RL evaluation 区分把 simulator 当目标与把 simulator 当 deployment proxy 的两套约束。"),
    "2606.28434": ("AGENT-MEMORY", "把 coding-agent compression timing、granularity 与剩余 context budget 变成 agent-controlled memory action。"),
    "2606.28436": ("TRAIN-GRPO", "把 coding post-training verifier 从 executable environment 改成 repository-evidence judge，改变 reward authority 与 non-proof 边界。"),
    "2606.28438": ("TRAIN-DATA", "证明 recursive code self-training 的 model-coupled gate 会 rubber-stamp collapse，要求 exogenous verification。"),
    "2606.28455": ("MULTIMODAL-WORLD-MODELS", "把 event readout、context-relative emphasis 与 causal sensitivity 分开评估 latent physical structure。"),
    "2606.28471": ("TRAIN-DATA", "以 capability slice 将 evaluation failure 反向映射为可检验 data intervention，并允许判定 data 非根因。"),
    "2606.28479": ("TRAIN-LORA", "用 matched-update controls 分离 DP guarantee、pseudonymization 与 optimizer-step memorization effect。"),
    "2606.28480": ("PLATFORM-EVALUATION-SYSTEM", "把 terminal-use agent 扩展到非 coding workflow，并用 deterministic setup/execution scoring 约束 release claim。"),
    "2606.28514": ("AGENT-MULTI-AGENT", "以真实异步倒计时、信息不对称与不可单独完成任务测量实时 collaboration。"),
    "2606.28529": ("INFER-REQUEST-LIFECYCLE", "把 embodied inference optimization 从 per-step latency 扩展到 closed-loop task time、success 与 hardware-dependent sweet spot。"),
    "2606.28551": ("TRAIN-DATA", "用固定 model/token budget 与多数据类型 corpus 建立 VLM data curation、mixing 与 release artifact 的可复算合同。"),
    "2606.28560": ("MODEL-LONG-CONTEXT", "以 matched small-model study 反证 learned sparse spacing 必然优于 static schedule，并暴露 train-length 与 extrapolation 的反向取舍。"),
    "2606.28562": ("TRAIN-GRPO", "按 student competence 在 token、phase、prompt 三个尺度控制 on-policy distillation supervision。"),
    "2606.28565": ("INFER-REQUEST-LIFECYCLE", "把 serving scheduler、kernel、communication 与 host overhead 组合成 token/kernel-level capacity simulator。"),
    "2606.28574": ("PLATFORM-EVALUATION-SYSTEM", "把 LLM coder 的表面一致性与 theoretical construct validity 分开，并要求 clause-level extractive evidence。"),
    "2606.28615": ("PLATFORM-EVALUATION-SYSTEM", "把 free-text explanation sufficiency 绑定显式 input distribution 与 self-consistent information metric。"),
    "2606.28639": ("PLATFORM-SECURITY", "给 static/dynamic alignment certification 划出 expressivity、soundness、completeness 与 tractability 的形式边界。"),
    "2606.28649": ("PLATFORM-SECURITY", "把 robot prompt injection threat surface 扩展到 OCR、audio 与 LiDAR-derived system context，并测 firewall bypass。"),
    "2606.28661": ("PLATFORM-EVALUATION-SYSTEM", "区分 test-time sampling coverage 与可部署 selection，并定义 modal/correlation ceiling 的停止边界。"),
}


def first_sentence(text: str) -> str:
    compact = " ".join(text.split())
    match = re.search(r"(?<=[.!?])\s", compact)
    sentence = compact[: match.start() + 1] if match else compact
    return sentence[:320]


def closure_class(row: dict) -> tuple[str, str]:
    title = row["title"].lower()
    abstract = row["abstract"].lower()
    joined = title + " " + abstract
    if any(term in title for term in ("survey", "position:", "towards ", "framework : a proposed", "review")):
        return "survey_or_position", "综述、立场或尚未验证的框架没有形成可写入长期系统判断的 primary mechanism/evaluation delta"
    if any(term in joined for term in ("medical", "clinical", "patient", "disease", "protein", "cell", "brain", "histopath", "biodiversity", "athlete", "battery")):
        return "domain_local_application", "贡献与证据绑定于医疗、生物或行业任务，未改变通用 AI-System state/data/control 或 release contract"
    if any(term in joined for term in ("forecasting", "recommendation", "classification", "segmentation", "recognition", "image generation", "video generation")):
        return "task_local_model_delta", "报告的是单任务表示、预测或生成质量变化，未建立可跨系统复用的 ownership 或 evaluation-release contract"
    if row["screening_route"] == "not_routed_by_keyword_contract" and not any(
        term in joined for term in ("llm", "language model", "agent", "world model", "vla", "gpu", "training", "inference")
    ):
        return "route_negative_non_ai_system", "route-negative 复核确认主题属于非 AI-System 的控制、网络、数学或领域工程，不能因分类相邻而扩池"
    if any(term in title for term in ("benchmark", "dataset", "empirical analysis", "comparison")):
        return "benchmark_without_durable_contract", "benchmark/dataset 只报告局部能力或数据集结果，没有改变可复算的系统 evaluation/release 判断"
    return "local_method_without_system_delta", "方法改进停留在局部模型、任务或数据集，未改变长期 AI-System 机制、所有权、平台合同或既有 Books 判断"


def main() -> None:
    provisional = json.loads(PROVISIONAL.read_text())
    rows = provisional["identities"]
    raw_ids = {row["arxiv_id"] for row in rows}
    if not set(RETAIN) <= raw_ids:
        raise SystemExit(f"retained identity missing from raw ledger: {sorted(set(RETAIN) - raw_ids)}")

    audited = []
    for row in rows:
        aid = row["arxiv_id"]
        base = dict(row)
        base["source_family_id"] = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        base["title_abstract_sha256"] = hashlib.sha256(
            (row["title"] + "\n" + row["abstract"]).encode()
        ).hexdigest()
        if aid in RETAIN:
            owner, reason = RETAIN[aid]
            base.update(
                screening_status="retained_durable_candidate",
                screening_decision="retain",
                proposed_owner=owner,
                screening_reason=reason,
            )
        else:
            kind, boundary = closure_class(row)
            base.update(
                screening_status="pre_denominator_closure_complete",
                screening_decision="closure",
                proposed_owner="—",
                closure_kind=kind,
                screening_reason=(
                    f"《{row['title']}》的摘要问题为：{first_sentence(row['abstract'])} "
                    f"本 family 的边界判断：{boundary}。"
                ),
            )
        audited.append(base)

    retained = [row for row in audited if row["screening_decision"] == "retain"]
    closures = [row for row in audited if row["screening_decision"] == "closure"]
    denominator_hash = hashlib.sha256(
        "\n".join(sorted(RETAIN)).encode()
    ).hexdigest()[:8]
    denominator_id = f"DEN-20260627-{denominator_hash}"
    for row in audited:
        row["denominator_id"] = denominator_id

    route = {}
    for name in sorted({row["screening_route"] for row in audited}):
        group = [row for row in audited if row["screening_route"] == name]
        route[name] = {
            "raw": len(group),
            "retained": sum(row["screening_decision"] == "retain" for row in group),
            "closure": sum(row["screening_decision"] == "closure" for row in group),
        }
    assert len(audited) == 384
    assert len(retained) == len(RETAIN) == 64
    assert len(closures) == 320
    assert sum(v["raw"] for v in route.values()) == 384
    assert route["not_routed_by_keyword_contract"]["raw"] == 84

    payload = dict(provisional)
    payload.update(
        schema="daily-v2.1-screening-ledger-final-v1",
        denominator_id=denominator_id,
        denominator_status="frozen_after_full_title_abstract_semantic_screen",
        retained_source_families=len(retained),
        pre_denominator_closures=len(closures),
        route_reconciliation=route,
        identities=audited,
    )
    (PACKET / "screening-ledger.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    (PACKET / "candidate-denominator.json").write_text(
        json.dumps(
            {
                "schema": "daily-v2.1-candidate-denominator-v1",
                "denominator_id": denominator_id,
                "raw": 384,
                "retained": 64,
                "closures": 320,
                "route_reconciliation": route,
                "candidates": retained,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )
    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open("w", newline="") as handle:
        fields = [
            "source_family_id", "arxiv_id", "screening_route", "title",
            "decision", "owner", "reason", "title_abstract_sha256",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in audited:
            writer.writerow(
                {
                    "source_family_id": row["source_family_id"],
                    "arxiv_id": row["arxiv_id"],
                    "screening_route": row["screening_route"],
                    "title": row["title"],
                    "decision": row["screening_decision"],
                    "owner": row["proposed_owner"],
                    "reason": row["screening_reason"],
                    "title_abstract_sha256": row["title_abstract_sha256"],
                }
            )
    print(
        json.dumps(
            {
                "denominator_id": denominator_id,
                "raw": 384,
                "retained": 64,
                "closures": 320,
                "route": route,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
