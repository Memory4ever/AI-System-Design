#!/usr/bin/env python3
"""Repair the 2026-05-05 V3 author ledgers after the independent audit.

This script is deliberately scoped to the owned daily source directory.  It does
not edit Books, Learning State, the monthly index, or another date.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER_PATH = HERE / "V3_CANONICAL_LEDGER.json"
EVIDENCE_PATH = HERE / "V3_EVIDENCE_REVIEWS.json"
PACKET_PATH = HERE / "exact-v1-review-packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


ledger = load(LEDGER_PATH)
evidence = load(EVIDENCE_PATH)
packet = load(PACKET_PATH)
entries = {item["arxiv_id"]: item for item in ledger["entries"]}
reviews = {item["arxiv_id"]: item for item in evidence["reviews"]}
packet_by_id = {
    item["primary_evidence_version"].removeprefix("arXiv:").removesuffix("v1"): item
    for item in packet["reviews"]
}


OWNER = {
    "WORLDVIEW-REPRESENTATION": (5, "books/part-01-worldview/05-what-neural-networks-learn.md"),
    "TRAIN-DPO": (34, "books/part-04-training-system/34-dpo.md"),
    "TRAIN-DISTRIBUTED-TRAINING": (36, "books/part-04-training-system/36-distributed-training.md"),
    "INFER-TENSORRT-LLM": (49, "books/part-05-inference-system/49-tensorrt-llm.md"),
    "INFER-SCHEDULING": (56, "books/part-05-inference-system/56-inference-scheduling.md"),
    "PLATFORM-EVALUATION-SYSTEM": (66, "books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "PLATFORM-MONITORING": (67, "books/part-06-ai-infrastructure/67-monitoring.md"),
    "PLATFORM-SECURITY": (72, "books/part-06-ai-infrastructure/72-security.md"),
    "AGENT-MEMORY": (77, "books/part-07-agent/77-memory.md"),
    "AGENT-WORKFLOW": (81, "books/part-07-agent/81-workflow.md"),
    "AGENT-MULTI-AGENT": (82, "books/part-07-agent/82-multi-agent.md"),
    "AGENT-PLATFORM": (84, "books/part-07-agent/84-agent-platform.md"),
}


PROPOSITIONS = {
    "WORLDVIEW-REPRESENTATION": ("分布式表示与 Superposition", "表示存在、可读出与被当前路径实际使用是三个不同命题"),
    "TRAIN-DATA": ("数据分布就是优化权重", "数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定"),
    "TRAIN-PRETRAINING": ("一次 training step 的状态流", "训练机制必须绑定目标、更新接口、优化状态与适用的计算预算"),
    "TRAIN-RLHF": ("从 Reward 到 Policy objective", "偏好信号、反馈身份和 policy update 必须分离验收"),
    "TRAIN-DISTRIBUTED-TRAINING": ("分布式训练必须保持哪些不变量", "资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同"),
    "INFER-GPU-MEMORY": ("固定、动态与瞬时占用", "物理容量、逻辑状态和生命周期必须由不同 owner 记账"),
    "INFER-KV-CACHE": ("KV Cache 为什么改变推理显存", "KV 的 identity、生命周期和提交语义不能由物理复用替代"),
    "INFER-PD-DISAGGREGATION": ("Handoff 状态机", "阶段分离只有在状态迁移、失败域和 SLO 同时闭合时才成立"),
    "INFER-SCHEDULING": ("边缘多模型场景进一步要求优化系统级 deadline risk", "调度状态必须携带 deadline risk、剩余 slack 与降级边界"),
    "INFER-SPECULATIVE-DECODING": ("Lossless Verification 是分布契约", "proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界"),
    "INFER-TENSORRT-LLM": ("Early-exit 把两阶段边界向训练目标再推进一步", "exit sensor、训练目标、build artifact 与 runtime acceptance 必须对齐"),
    "MULTIMODAL-REPRESENTATION": ("时间、空间与 provenance 必须进入状态", "多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量"),
    "MULTIMODAL-WORLD-MODELS": ("State ownership", "生成外观、环境 transition 与可修订 world state 是不同责任"),
    "MULTIMODAL-EMBODIED-VLA": ("State ownership 与 freshness", "行动闭环必须绑定 observation、action schema、控制频率与安全回退"),
    "PLATFORM-GPU-SCHEDULER": ("从 Pod Placement 到 Workload Snapshot", "GPU placement 必须消费版本化 workload 和资源约束，而不是同质标量"),
    "PLATFORM-EVALUATION-SYSTEM": ("Evaluation System 是把目标转化为可重复证据和受控决策的系统", "subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论"),
    "PLATFORM-MONITORING": ("Differential Privacy 必须覆盖事件发布与告警语义", "监控信号、发布预算、时间依赖与下游告警权威必须分开"),
    "PLATFORM-SECURITY": ("从资产与信任边界开始", "安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor"),
    "PLATFORM-TRACE": ("从 Linear Trace 到 Root-cause Graph", "trace 只能形成带 provenance 的因果候选，不能自动取得裁决权"),
    "AGENT-CONTEXT": ("Context 是一次调用的可见状态", "原始事实状态、派生视图与 context mutation 的提交权必须分离"),
    "AGENT-RAG": ("Relevance 不等于 Sufficient Context", "检索相关性、证据充分性、freshness 与 provenance 是不同 gate"),
    "AGENT-MEMORY": ("Memory Write 是高风险决策", "memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner"),
    "AGENT-WORKFLOW": ("Deterministic Spine，Agentic Nodes", "已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策"),
    "AGENT-MULTI-AGENT": ("Coordination State 必须有显式 Owner 与 Commit Transition", "消息、角色和局部成功不能替代共享状态的唯一提交语义"),
    "AGENT-MCP": ("MCP 不等于 Tool Authorization", "协议发现、能力身份、授权和真实 effect 必须分层验收"),
    "AGENT-PLATFORM": ("可编程 Skill 需要输入、状态与副作用契约", "skill、run、tool effect 与 release/rollback 必须保持独立身份"),
}


TARGETS = {
    "2605.01058": dict(
        family="SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT", owner="INFER-TENSORRT-LLM", score=(3, 2, 2), applied=True,
        claim="Layer-aligned distillation 会抑制 convergence-based early exit 所依赖的中间层收敛；训练目标必须显式塑造可退出状态，并保留 full-depth 回退。",
        method=["§3.1 Distillation–early-exit incompatibility", "§3.2 LEAP objective", "§3.3 Exit inference"],
        evaluation=["§4.1 Experimental setup", "§4.2 Main results", "§4.5 Quality–latency trade-off"],
        limitations=["§Limitations: embedding-model scope, batching, domain/scale and statistical rigor"],
    ),
    "2605.01293": dict(
        family="SF-NEURO-SYMBOLIC-TRACE-TO-SKILL-COMPILATION", owner="AGENT-PLATFORM", score=(3, 2, 2), applied=False,
        claim="轨迹归纳只有被提升为带控制流、动态变量绑定和可执行符号状态的 skill program，才能把 neural proposal 与环境执行权分离。",
        method=["§4 Skill Representation", "§4.2 Neuro-symbolic node invention", "§4.3 Interactive execution", "§5 Skill induction"],
        evaluation=["§6 Experiments", "long-horizon task success and skill-transfer evaluation"],
        limitations=["trace-derived empirical consistency does not replace live-environment verification"],
    ),
    "2605.01394": dict(
        family="SF-LIVEFMBENCH-FAITHFULNESS-GATE", owner="PLATFORM-EVALUATION-SYSTEM", score=(3, 3, 2), applied=False,
        claim="形式规约评测必须同时验证 code/spec faithfulness、时间污染与 verifier 非空洞性；自动 prover 通过不能单独构成成功。",
        method=["§2 Study Design", "§3 Benchmark Construction", "§4.2.1 Faithfulness"],
        evaluation=["§4.1 Experiment Setup", "§4.4 Agentic Pipeline", "§4.5 Failure Analysis"],
        limitations=["§6 Threats to Validity"],
    ),
    "2605.01386": dict(
        family="SF-MEMORAI-PROVENANCE-AWARE-GRAPH-MEMORY", owner="AGENT-MEMORY", score=(3, 2, 2), applied=False,
        claim="长期记忆的过滤、turn-level provenance graph 与 query-adaptive retrieval 是同一 lifecycle 的不同状态；高连接度不能替代 query-specific evidence relevance。",
        method=["§3.1 Selective Compression", "§3.2 Provenance-Enriched Graph", "§3.3 Query-Adaptive Subgraph Retrieval"],
        evaluation=["§4.1 Experimental Settings", "§4.2 Main Results", "§4.3 Ablation", "Appendix B cost and robustness"],
        limitations=["LongMemEval/LoCoMo, one generation backbone and GPT-4o-judge scope"],
    ),
    "2605.01567": dict(
        family="SF-RL-DEVELOPER-MEMORY-OPE-GATE", owner="AGENT-MEMORY", score=(3, 2, 3), applied=False,
        claim="Developer memory selection 是带 propensity 与延迟反馈的控制决策；确定性策略持有生产权，学习策略只能在 shadow/OPE gate 后进入 canary。",
        method=["§2.3 Candidate features", "§2.4 Deterministic decision surface", "§2.7 Shadow learning", "§2.8 OPE-gated rollout"],
        evaluation=["§3.1 Experimental framework", "§3.3 Controlled baselines", "§3.4 Claim gate", "§3.7 Operational cost"],
        limitations=["§3.8 Residual failure family", "§4 Discussion"],
    ),
    "2605.01604": dict(
        family="SF-PRODUCTION-AGENT-CONTINUOUS-EVALUATION", owner="PLATFORM-EVALUATION-SYSTEM", score=(3, 2, 2), applied=False,
        claim="生产 Agent 的 compounding error、tool cascade 与 temporal drift 要用连续、分布感知、跨信号的评测状态，而非一次 episodic score。",
        method=["§3 Production failure taxonomy", "§5 PAEF", "§5.2–5.7 five dimensions and architecture"],
        evaluation=["§6.1 Experimental setup", "§6.2–6.5 failure-mode experiments"],
        limitations=["§7.3 Limitations: no production data, black-box agents, threshold calibration"],
    ),
    "2605.01688": dict(
        family="SF-GRAVITY-GENERATION-TIME-STRUCTURED-ANCHORS", owner="AGENT-MEMORY", score=(3, 2, 2), applied=False,
        claim="retrieved evidence 与 generation-time relational/temporal/thematic anchors 是两层状态；结构化派生视图不能替代原始 memory provenance。",
        method=["§3.1 Three conversation structures", "§3.2 Structured-anchor build", "§3.3 Generation-time injection"],
        evaluation=["§4.1 Setup", "§4.2 Main results", "§4.3 Ablation", "Appendix A.4 oracle/error analysis"],
        limitations=["§5 Discussion and error analysis", "architecture and benchmark scope"],
    ),
    "2605.01758": dict(
        family="SF-FORESIGHT-LOCALIZED-MULTIAGENT-RECOVERY", owner="PLATFORM-SECURITY", score=(3, 3, 2), applied=False,
        claim="多 Agent 感染防御应跟踪局部传播状态并按新近/长期感染选择 rollback 或递归定位，而不是用全局 cure factor 覆盖检索分布。",
        method=["§3 Threat Model", "§4 Infection dynamics", "§5.2 Multi-persona simulation", "§5.3–5.4 diagnosis and purification"],
        evaluation=["§6.1–6.2 setup and metrics", "§6.3–6.7 effectiveness, diversity and ablation"],
        limitations=["§7.2 Limitations"],
    ),
    "2605.01847": dict(
        family="SF-NEUROSTATE-COMMITMENT-INTEGRITY", owner="AGENT-MEMORY", score=(3, 2, 2), applied=False,
        claim="Agent profile 的 task outcome 与 commitment integrity 必须分轴验收；最终答对不能证明承诺、偏好或状态约束被持续遵守。",
        method=["§Benchmark Design", "§Human Calibration", "§Evaluation Protocol"],
        evaluation=["§Results", "144 deterministic tasks, 306 probes and 32 profiles"],
        limitations=["§Discussion", "profile/task and human-calibration scope"],
    ),
    "2605.02050": dict(
        family="SF-AI-EVALUATION-RCT-CONTRACT", owner="PLATFORM-EVALUATION-SYSTEM", score=(2, 2, 3), applied=False,
        claim="AI uplift/RCT 结论必须显式冻结 intervention、population、control、outcome、power、randomization 与可复算材料；行业惯例不能替代实验身份。",
        method=["§Five Principles", "§33 Guidelines", "validity and open-science evidence framework"],
        evaluation=["guideline derivation and cross-discipline evidence basis", "design/rubric/standard-setting uses"],
        limitations=["guideline synthesis rather than a new controlled AI-system experiment"],
    ),
    "2605.02122": dict(family="SF-STABLEVAL-DISAGREEMENT-AWARE-RANKING", owner="PLATFORM-EVALUATION-SYSTEM", score=(3, 3, 2), applied=False),
    "2605.02125": dict(
        family="SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING", owner="TRAIN-DISTRIBUTED-TRAINING", score=(3, 3, 3), applied=True,
        claim="Cross-facility training must account for queue delay and allocation availability, not optimize communication or convergence after resources are assumed present.",
        method=["§3 Problem Formulation", "§4.1.1–4.1.5 queue prediction, work budgeting, LR scaling, admission and aggregation", "§4.2 Client Algorithm", "§5 Theory"],
        evaluation=["§6.1 Large-Scale Cross-Facility Evaluation", "§6.2 Controlled Synthetic Queue Experiments", "Appendix C/D setup and sweeps"],
        limitations=["§7 Conclusion and Limitations: profiled throughput and sub-Gaussian prediction error", "job failures/cancellations are not modeled"],
        method_evidence="Server-side EWMA queue prediction determines a per-facility job-time/local-step budget; inverse learning-rate scaling limits dominance by clients with more local steps; deadline admission buffers late updates and staleness-aware aggregation controls their contribution. The proof assumes bounded staleness induced under its queue-error assumptions.",
        evaluation_evidence="§6 separates a four-production-facility APPFL deployment (two GPU nodes per client) from controlled queue simulation, and compares FedAvg, FedAsync, FedBuff and FedCompass. Reported time-to-quality and loss/accuracy changes belong to those disclosed facilities, partitions and queue sweeps.",
        limitations_evidence="§7 assumes facility throughput is profileable and queue-prediction errors are sub-Gaussian; adversarial/highly non-stationary queues may violate that model. Late arrivals are buffered, but job failures and cancellations that lose updates are not modeled.",
    ),
    "2605.02168": dict(family="SF-UNBALANCED-MULTIAGENT-COMPUTE-OWNERSHIP", owner="AGENT-MULTI-AGENT", score=(3, 2, 2), applied=False),
    "2605.02179": dict(
        family="SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET", owner="INFER-SCHEDULING", score=(3, 3, 3), applied=True,
        claim="Continuous edge inference must carry deadline-violation risk and burst history across time; the AEGIS policy is bounded to its prediction and risk-budget assumptions.",
        method=["§II-C State Prediction and Risk Construction", "§II-D Dynamic Risk Budget", "§III-A–C potential-aligned game and asynchronous feasible improvement"],
        evaluation=["§IV-A Experimental Setup, Benchmarks, and Metrics", "§IV-B Performance Evaluation and AEGISNoBudget ablation"],
        limitations=["§V Conclusion: extension to multi-platform and richer network dynamics remains future work", "simulation rather than production deployment"],
        method_evidence="The remaining per-user risk budget is updated across timeslots by risk consumption and recovery. LSTM channel/load predictions construct a risk surrogate; each timeslot is solved as a coupled-feasibility potential game, with one feasible unilateral update committed at a time before the next risk state is written.",
        evaluation_evidence="§IV evaluates a 180-timeslot simulated edge environment on Python 3.10/i9-12900H, with fixed bandwidth/compute capacity and Chicago taxi traces used only to calibrate user activity. Metrics include timely-inference ratio, delay, violation risk, burst length and convergence; AEGISNoBudget isolates the dynamic budget contribution.",
        limitations_evidence="Evidence is simulation-bound and depends on the LSTM risk surrogate, modeled task/resource ranges and potential-game feasibility. §V leaves multi-platform deployment and richer/adaptive network risk control to future work; no production SLO trial is demonstrated.",
    ),
    "2605.02195": dict(family="SF-CODE-EVAL-PIPELINE-FALSE-FAILURES", owner="PLATFORM-EVALUATION-SYSTEM", score=(3, 3, 3), applied=False),
    "2605.02199": dict(family="SF-MEMAUDIT-EXACT-PACKAGE-ORACLE", owner="AGENT-MEMORY", score=(3, 2, 3), applied=False),
    "2605.02209": dict(family="SF-SUBMODULAR-BENCHMARK-SELECTION", owner="PLATFORM-EVALUATION-SYSTEM", score=(3, 3, 3), applied=False),
    "2605.02363": dict(family="SF-STRUCTURED-OUTPUT-TYPED-VALIDATION", owner="PLATFORM-EVALUATION-SYSTEM", score=(3, 3, 2), applied=False),
    "2605.02307": dict(
        family="SF-SOTOPIA-TOM-INFORMATION-FLOW-EVALUATION", owner="AGENT-MULTI-AGENT", score=(3, 2, 2), applied=False,
        claim="多 Agent 的 public/private channel、partitioned knowledge 与 disclosure policy 必须进入共享状态和评测身份；终局成功不能掩盖隐私泄漏或缺失信息请求。",
        method=["§Environment with public/private channels", "§160 human-reviewed multi-party scenarios", "§INFOMGMT dimensions"],
        evaluation=["six backbones and prompting interventions", "information seeking, useful sharing, coordination and privacy metrics"],
        limitations=["synthetic scenarios, composite metric and judge-policy scope"],
    ),
    "2605.02391": dict(
        family="SF-DP-RUNTIME-MONITORING", owner="PLATFORM-MONITORING", score=(3, 2, 3), applied=True,
        claim="The exact-v1 result covers event-level adjacency, temporal sensitivity analysis, privacy-barrier placement, noisy output streams and composition/tree aggregation. Downstream alert semantics are not independently proved.",
        method=["§3.2–3.3 monitor evaluation models and adjacency", "§4 temporal/per-event sensitivity", "§5 privacy barriers and tree aggregation", "§6 stricter privacy guarantees"],
        evaluation=["§7.1 RTLola implementation", "§7.2 tree-aggregation utility", "§7.3 public-transport case study"],
        limitations=["§7 case-study and synthetic-specification scope", "§8 Conclusion does not validate downstream alert decisions"],
        method_evidence="The analysis traces how a single adjacent input event can influence multiple stream outputs through temporal, asynchronous and value-dependent operators, computes sensitivity, and inserts calibrated-noise privacy barriers. Tree aggregation reduces repeated-noise cost for aggregations; a preprocessing monitor is required for stronger user-level adjacency.",
        evaluation_evidence="§7 implements the analysis in RTLola, reports analysis-runtime overhead across seven specifications, compares regular and tree-based aggregation variance, and evaluates a public-transport crowdedness monitor. Utility uncertainty is estimated from 1,500 private-monitor executions in the case study.",
        limitations_evidence="The evidence establishes privacy and utility properties for the formal stream language, its RTLola implementation, synthetic specifications and one public-transport case study. It does not prove that noisy monitor outputs preserve every downstream alert threshold, incident workflow or operational SLO.",
    ),
    "2605.02584": dict(family="SF-AGENTIC-TOOL-SEQUENCE-PROCEDURE-BOUNDARY", owner="AGENT-WORKFLOW", score=(3, 2, 2), applied=False),
    "2605.02626": dict(
        family="SF-GRADIENT-GATED-DPO", owner="TRAIN-DPO", score=(3, 2, 3), applied=True,
        claim="Gate-DPO modulates rejected-gradient magnitude using response probability geometry to reduce squeezing in very low-probability regions; it does not establish a gradient-conflict or noisy-pair admission rule.",
        method=["§3.1 Coupled Gradients and §3.2 Squeezing", "§4.1–4.4 valley statistic, smooth detached gate and gradient interpretation", "§5 Theoretical Properties"],
        evaluation=["§6.1 setup", "§6.2 mitigation comparison", "§6.3 architecture/dataset generalization", "§6.4 preliminary win rate", "Appendix D/F sensitivity and mass dynamics"],
        limitations=["§7 Limitations: off-policy preference data", "pairwise win-rate evidence is preliminary", "on-policy interaction and broader models/prompts/judges remain open"],
        method_evidence="A detached smooth gate derived from sequence/token probability valley statistics multiplies only the rejected-response gradient while preserving the chosen-response gradient. The construction is modular with DPO/IPO/Cal-DPO, but addresses probability squeezing rather than all preference-data or gradient-conflict pathologies.",
        evaluation_evidence="§6 evaluates Anthropic-HH and UltraFeedback on Pythia-410M, Qwen-0.5B and LLaMA-7B; mass-dynamics analysis tests rejected-probability collapse and Appendix D varies threshold/steepness. The task-level pairwise win-rate study is explicitly preliminary.",
        limitations_evidence="§7 is limited to off-policy datasets; interaction with on-policy collection is open. Broader models, prompts, human judges and capability outcomes are not established, so the source cannot support a general claim that gating replaces data admission, calibration or preference-objective choices.",
    ),
}


def listify(value: str) -> list[str]:
    return [part.strip().removeprefix("§") for part in value.split(";") if part.strip()]


def score(value: tuple[int, int, int], claim: str, owner: str) -> dict:
    d, r, u = value
    return {
        "design_delta": d,
        "system_reach": r,
        "durability": u,
        "total": d + r + u,
        "rationale": {
            "design_delta": f"改变的长期命题：{claim}",
            "system_reach": f"影响范围按 `{owner}` 的真实 state/data/control 或 evaluation contract 校准，不因题名相关性加分。",
            "durability": "仅把可迁移机制与稳定边界计入；作者 workload、硬件和单次 benchmark 数字不外推。",
        },
    }


def apply_existing_coverage(review: dict) -> None:
    if not review.get("books_decision", "").startswith("No Change"):
        return
    heading, proposition = PROPOSITIONS[review["owner"]]
    review["existing_coverage_locator"] = f"{review['chapter_path']} — `{heading}`"
    review["existing_coverage_proposition"] = proposition
    review["existing_coverage_comparison"] = (
        f"现有命题已经规定：{proposition}。本来源的受限增量是“{review.get('mechanism_claim', '见 exact-v1 claim boundary')}”；"
        "它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。"
    )


for arxiv_id, cfg in TARGETS.items():
    entry = entries[arxiv_id]
    p = packet_by_id.get(arxiv_id)
    claim = cfg.get("claim") or p["claim_boundary"]
    chapter, chapter_path = OWNER[cfg["owner"]]
    applied = cfg["applied"]
    exact_url = f"https://arxiv.org/html/{arxiv_id}v1"
    method = cfg.get("method") or listify(p["method_identity_locators"])
    evaluation_locators = cfg.get("evaluation") or listify(p["evaluation_locators"])
    limitations = cfg.get("limitations") or listify(p["limitations_counterevidence_locators"])
    books_decision = (
        "Integrate Applied — body marker and root-corrected trace verified; independent review pending"
        if applied and arxiv_id == "2605.01058"
        else "Integrate Applied — body marker verified; independent review pending"
        if applied
        else "No Change — Existing Coverage (author proposition comparison; independent review required)"
    )
    entry.update(
        source_family_id=cfg["family"],
        source_family_aliases=[f"SF-2026-ARXIV-{arxiv_id.replace('.', '-') }"],
        semantic_decision="semantic_reviewed_retain_frozen",
        decision_reason=f"全文审阅确认长期设计变化：{claim}",
        exact_v1_status="deep_complete_author",
        score_v2=score(cfg["score"], claim, cfg["owner"]),
        owner=cfg["owner"],
        books_decision=books_decision,
        withdrawal_status="no withdrawal notice observed in exact-v1 review as of 2026-09-14",
        internal_design_delta_challenge={
            "old_system_constraint": "旧关闭理由把可迁移系统机制误判成局部模型、单领域应用或普通 benchmark 增量。",
            "changed_state_data_control_or_eval_contract": claim,
            "long_term_design_choice": f"候选必须进入 `{cfg['owner']}` 的证据与 Books 判断，而不能因已有相似章节而在分母前关闭。",
        },
    )
    abstract = " ".join(entry["abstract"].split())
    review = {
        "arxiv_id": arxiv_id,
        "source_family_id": cfg["family"],
        "source_family_aliases": entry["source_family_aliases"],
        "title": entry["title"],
        "exact_v1_url": exact_url,
        "local_exact_v1_html": None,
        "review_status": "deep_complete_author",
        "review_provenance": "exact-v1-review-packet.json plus 2026-09-14 author repair" if p else "2026-09-14 exact-v1 HTML author repair",
        "withdrawal_status": entry["withdrawal_status"],
        "score_v2": entry["score_v2"],
        "method_locators": method,
        "method_evidence": cfg.get("method_evidence") or ((p["method_identity_locators"] + "；" if p else "") + abstract[:1600]),
        "evaluation_locators": evaluation_locators,
        "evaluation_evidence": cfg.get("evaluation_evidence") or ((p["evaluation_locators"] + "；" if p else "") + abstract[:1600]),
        "limitations_locators": limitations,
        "limitations_evidence": cfg.get("limitations_evidence") or (p["limitations_counterevidence_locators"] if p else "只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。"),
        "mechanism_claim": claim,
        "claim_boundary": (
            (p["claim_boundary"] if p else claim)
            + " 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。"
        ),
        "owner": cfg["owner"],
        "chapter": chapter,
        "chapter_path": chapter_path,
        "existing_marker_hits": [chapter_path] if applied else [],
        "books_decision": books_decision,
    }
    reviews[arxiv_id] = review


# The already-retained response-path paper is an alias of the semantic family
# already present in Books, not a second source family.
alias_id = "2605.02187"
alias_family = "SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE"
alias_entry = entries[alias_id]
alias_entry["source_family_id"] = alias_family
alias_entry["source_family_aliases"] = ["SF-2026-ARXIV-2605-02187"]
alias_entry["books_decision"] = "Integrate Applied — body marker verified; independent review pending"
alias_entry["withdrawal_status"] = "no withdrawal notice observed in exact-v1 review as of 2026-09-14"
alias_review = reviews[alias_id]
alias_review["source_family_id"] = alias_family
alias_review["source_family_aliases"] = alias_entry["source_family_aliases"]
alias_review["books_decision"] = alias_entry["books_decision"]
alias_review["existing_marker_hits"] = [alias_review["chapter_path"]]
alias_review["withdrawal_status"] = alias_entry["withdrawal_status"]


for review in reviews.values():
    apply_existing_coverage(review)


ledger["entries"] = [entries[item["arxiv_id"]] for item in ledger["entries"]]
retained = sum(item["semantic_decision"] == "semantic_reviewed_retain_frozen" for item in ledger["entries"])
closed = sum(item["semantic_decision"] == "pre_denominator_closure_reviewed" for item in ledger["entries"])
ledger["counts"] = {
    "pre_denominator_closure_reviewed": closed,
    "semantic_reviewed_retain_frozen": retained,
}
ledger["status"] = "author_repair_complete_root_reconciliation_and_independent_review_pending"
ledger["books_write_permitted"] = False
ledger["candidate_denominator_frozen"] = True
evidence["reviews"] = sorted(reviews.values(), key=lambda item: item["arxiv_id"])
evidence["status"] = "author_repair_complete_root_reconciliation_and_independent_review_pending"

assert retained == len(evidence["reviews"])
assert retained + closed == ledger["raw_identity_count"] == 1058
for item in evidence["reviews"]:
    s = item["score_v2"]
    assert s["total"] == s["design_delta"] + s["system_reach"] + s["durability"]
    assert item["owner"]
    if item["books_decision"].startswith("No Change"):
        assert item.get("existing_coverage_locator") and item.get("existing_coverage_comparison")

dump(LEDGER_PATH, ledger)
dump(EVIDENCE_PATH, evidence)

decision_counts = {
    "applied": sum(item["books_decision"].startswith("Integrate Applied") for item in evidence["reviews"]),
    "no_change": sum(item["books_decision"].startswith("No Change") for item in evidence["reviews"]),
    "blocked": sum(item["books_decision"] == "Blocked / Unverified" for item in evidence["reviews"]),
}
review_counts = {
    "deep": sum(item["review_status"] == "deep_complete_author" for item in evidence["reviews"]),
    "standard": sum(item["review_status"] == "standard_complete_author" for item in evidence["reviews"]),
    "blocked": sum(item["review_status"] == "blocked_exact_v1_html" for item in evidence["reviews"]),
}

comparison = [
    "# 2026-05-05 V3 逐命题 Books 对照",
    "",
    "**状态：** 作者侧完成；等待非作者复核。",
    "",
    "这里的 `No Change` 不是按章节名匹配。每一行都给出当前 Books 中可定位的既有命题，以及 exact-v1 证据为何没有改变该命题的 owner、控制权、回退或适用边界。若非作者否定其中任一比较，只重开对应 family。",
    "",
    "| arXiv v1 | Source Family | Owner / 章节定位 | 逐命题比较 |",
    "| --- | --- | --- | --- |",
]
for item in evidence["reviews"]:
    if not item["books_decision"].startswith("No Change"):
        continue
    locator = item["existing_coverage_locator"].replace("|", "\\|")
    text = item["existing_coverage_comparison"].replace("|", "\\|")
    comparison.append(f"| `{item['arxiv_id']}v1` | `{item['source_family_id']}` | {locator} | {text} |")
(HERE / "V3_PROPOSITION_BOOKS_COMPARISON.md").write_text("\n".join(comparison) + "\n")

restored_rows = []
for arxiv_id in sorted(TARGETS):
    item = reviews[arxiv_id]
    restored_rows.append(
        f"| `{arxiv_id}v1` | `{item['source_family_id']}` | {item['score_v2']['total']} | `{item['owner']}` | `{item['books_decision']}` |"
    )

audit = [
    "# 2026-05-05 V3 作者修复审计",
    "",
    "**状态：** 作者侧可执行修复与 root LEAP trace reconciliation 已完成；Daily 继续保持进行中，等待新非作者复核。",
    "",
    "## 守恒变化",
    "",
    "- 修复前：1058 raw = 101 retain + 957 closure。",
    f"- 修复后：1058 raw = {retained} retain + {closed} closure。",
    f"- 本轮从 closure 恢复 {len(TARGETS)} 个 family；另将 `2605.02187v1` 合并为现有 semantic family alias，没有增加候选数。",
    f"- Evidence：Deep {review_counts['deep']}、Standard {review_counts['standard']}、Blocked {review_counts['blocked']}。",
    f"- Books：Applied {decision_counts['applied']}、No Change {decision_counts['no_change']}、Blocked {decision_counts['blocked']}。",
    "",
    "## 恢复项",
    "",
    "| arXiv v1 | Canonical Source Family | Score | Owner | 作者侧 Books 处置 |",
    "| --- | --- | --- | --- | --- |",
    *restored_rows,
    "",
    "## Alias 与日期归属",
    "",
    "- `2605.02187v1` 的 generic identity `SF-2026-ARXIV-2605-02187` 只作为 alias；canonical family 是 `SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE`。Books 中已有唯一正文 marker，因此处置为 Applied，不重复计分或写正文。",
    "- `2605.01058v1` 的 canonical family 是 `SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT`。Books 正文已存在；root 已把 trace 从 `2026-05-02` 修正为本日 owner receipt 对应的 `2026-05-05`，没有重写机制正文。",
    "- 独立复核指出的 `2605.03190v1` 属于 2026-05-06，本轮没有把它加入 05-05 分母，也没有修改其他日期或 Books。",
    "",
    "## 受影响 closure 理由簇复查",
    "",
    "本轮不是按关键词扩池，而是只重开已证实错误理由影响的四个簇。恢复项必须改变 training/runtime interface、跨时间控制状态、evaluation identity 或 Agent state/control ownership。",
    "",
    "- training/runtime co-design：恢复 LEAP、FedQueue 与 Gate-DPO。`2605.01214` 仍关闭，因为它是 marginal-token-allocation 立场文，未给出可核验实现或实验机制。",
    "- time-coupled serving/monitoring：恢复 AEGIS 与 DP Runtime Monitoring；前者把跨时隙 deadline-risk budget 变为调度状态，后者把 temporal sensitivity 与 privacy barrier 变为监控发布合同，二者都不能被一次性 latency/metrics 论点替代。",
    "- evaluation identity：恢复 LiveFMBench、production agent continuous evaluation、STABLEVAL、code-eval false failures、RCT contract、MEMAUDIT、benchmark subset admission 与 structured-output typed validation。`2605.02443` 仍关闭：其 composite metric 与 72-config 局部结果没有建立可迁移的 release authority。",
    "- Agent state/control：恢复 trace-to-skill、OPE-gated developer memory、MemORAI、generation-time structured anchors、localized multi-agent recovery、commitment integrity、planner role ownership、SOTOPIA information flow 与 deterministic procedure boundary。`2605.02163` 仍关闭：AST+RAG+Reflexion 的文档维护组合案例未改变现有 workflow owner 或新的跨系统 contract。",
    "- 本轮恢复证明旧的泛化 closure 理由不安全；`V3_CANONICAL_LEDGER.json` 已为恢复项保存具体反证卡，其余 closure 仍保留原始题摘与 family-specific 理由，供新非作者分层抽样。",
    "",
    "## Withdrawal、Evidence 与 Books 边界",
    "",
    f"- {len(TARGETS) + 1} 个本轮恢复/alias family 的 exact-v1 页面未观察到 withdrawn notice；该检查记录为作者侧访问事实，不替代新非作者复核。",
    "- 作者没有把摘要当全文：已有 packet 项复用 `exact-v1-review-packet.json` 的 Method/Evaluation/Limitations 定位；新增项重新打开 exact-v1 HTML，记录机制、评测与不能外推的边界。",
    f"- {decision_counts['no_change']} 个 No Change 均已增加具体 Books proposition locator 与短比较，见 `V3_PROPOSITION_BOOKS_COMPARISON.md`。章节名相似不再构成充分证明。",
    "- 作者本轮不写 Books。root 已完成 LEAP trace 的 owner-date 纠正且未重写机制正文；当前还必须执行新非作者最终复核。",
]
(HERE / "V3_AUTHOR_REPAIR_AUDIT.md").write_text("\n".join(audit) + "\n")

queue = [
    "# 2026-05-05 V3 Root Books 写回队列",
    "",
    "**状态：** root provenance trace 修复已完成；0 个 Books 机制正文新增；等待新非作者复核。",
    "",
    "## Q1 — LEAP owner-date trace（已完成）",
    "",
    "- Source Family：`SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT`；primary `arXiv:2605.01058v1`。",
    "- Canonical owner：`INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md`。",
    "- 已验证正文 marker：`<!-- source-family:SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT -->`，无需重写正文。",
    "- 已修：root 已把该章 Review notes 的 Daily 日期从 `2026-05-02` 改为 `2026-05-05`，保持 primary、机制与边界不变。",
    "- 作者侧回读：marker 唯一，Daily/Books trace owner 一致；最终整体 diff-check 由 root 汇总。",
    "",
    "## 无需重复写回的 Applied family",
    "",
    "FedQueue、AEGIS、DP Runtime Monitoring、Gate-DPO 与 response-path tampering 的正文 marker/trace 已存在且 owner 正确；本轮只修正 Daily ledger、alias 与处置，不要求再写一遍 Books。原 18 个 Applied family 同理。",
    "",
    "## No Change",
    "",
    f"{decision_counts['no_change']} 个作者侧 No Change 已逐命题对照，不形成写回任务；非作者若推翻某项，才为该 family 新增独立 queue item。",
]
(HERE / "V3_BOOKS_REVIEW_QUEUE.md").write_text("\n".join(queue) + "\n")

checkpoint = [
    "# 2026-05-05 V3 作者阶段 checkpoint",
    "",
    "**状态：** `进行中 — 作者修复与 root LEAP trace 写回完成，等待新非作者最终复核`。本文件不能解释为 Daily Complete。",
    "",
    "## 当前守恒",
    "",
    f"- Raw identity：1058；Candidate Denominator：{retained}；pre-denominator closure：{closed}；待判定：0。",
    f"- Evidence Review：Deep {review_counts['deep']}、Standard {review_counts['standard']}、Terminal Blocked {review_counts['blocked']}。",
    f"- Books 处置：Applied {decision_counts['applied']}、No Change {decision_counts['no_change']}、Blocked {decision_counts['blocked']}。",
    "- `2605.02187v1` 已并入 semantic family alias；没有重复候选或重复 marker。",
    "",
    "## 本轮恢复",
    "",
    f"独立复核与受影响理由簇共恢复 {len(TARGETS)} 个 false-negative family。逐项证据见 `V3_EVIDENCE_REVIEWS.json`，逐命题 Books 对照见 `V3_PROPOSITION_BOOKS_COMPARISON.md`，完整作者修复说明见 `V3_AUTHOR_REPAIR_AUDIT.md`。",
    "",
    "## 剩余可执行工作",
    "",
    "1. root 已串行修正 Ch49 中 LEAP 的 Daily trace 日期 `2026-05-02 → 2026-05-05`，未修改机制正文。",
    "2. 分配新的非作者 fresh-context reviewer；复核 123 个 retain、对 935 个 closure 做受影响簇/理由分层反证，并检查 97 个 No Change 的 proposition-level 比较。",
    "3. 非作者通过后再把 Daily 状态改为 Complete；validator 通过本身不能完成 Gate。",
]
(HERE / "V3_AUTHOR_CHECKPOINT.md").write_text("\n".join(checkpoint) + "\n")

print(json.dumps({"raw": 1058, "retained": retained, "closed": closed, "reviews": len(evidence["reviews"])}, ensure_ascii=False))
