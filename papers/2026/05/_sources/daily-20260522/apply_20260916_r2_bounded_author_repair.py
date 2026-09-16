#!/usr/bin/env python3
"""Apply the bounded author-side repair requested by the 2026-09-16 R2 review.

This script is intentionally date-local.  It never writes Books and it never
expands the frozen 667-identity owner batch.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SRC = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/22/README.md"
CHECKED_AT = "2026-09-16T19:40:00+08:00"


def load(name: str):
    return json.loads((SRC / name).read_text())


def dump(name: str, value) -> None:
    (SRC / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


ledger = load("screening-ledger-v3.json")
closure = load("closure-semantic-reaudit-v3.json")
evidence = load("exact-v1-evidence-v3.json")
comparisons = load("books-current-content-comparison-v3.json")
queue = load("BOOKS_WRITEBACK_QUEUE_V3.json")
provenance = load("closure-repair-exact-v1-provenance-v3.json")

identities = {item["arxiv_id"]: item for item in ledger["identities"]}
evidence_by_id = {item["arxiv_id"]: item for item in evidence}
comparison_by_id = {item["arxiv_id"]: item for item in comparisons}
closure_by_id = {item["arxiv_id"]: item for item in closure["records"]}
GENERIC_NC_IDS = {
    item["arxiv_id"]
    for item in comparisons
    if item.get("decision", "").startswith("No Change")
    and item.get("existing_proposition", "").startswith("当前 Ch")
}
ANCHOR_RECHECK_IDS = {
    item["arxiv_id"]
    for item in comparisons
    if item.get("comparison_status") == "current_body_rechecked_author"
}


RESTORED = {
    "2605.21573": {
        "score": (3, 2, 3),
        "review": "deep_complete_author_bounded_repair",
        "owner": "TRAIN-PRETRAINING",
        "path": "books/part-04-training-system/28-pretraining.md",
        "decision": "Integrate — pending root serialized writeback",
        "method": "§3 Method; §3.1 Pre-training Data Lens-800M; §3.2 Architecture; §3.3 Pre-training; §3.4 Post-training; §3.5 Inference",
        "evaluation": "§4 Comparison; Appendix F Broader Impacts and Limitations",
        "limitations": "Appendix F Broader Impacts and Limitations; the component bundle and vendor comparison do not isolate a universal recipe",
        "sha256": "4a1887004db607261202a59b533ebbf6af37eca63879133d70e420d67ffe94a2",
        "proposition": "训练效率不能只用单步 FLOPs 表示；应同时记录每步计算、batch 中可用信息密度与达到目标质量所需步数。稠密 caption、混合分辨率/宽高比与表示选择可以共同改变 quality-per-update，但 19.3% 计算量只属于论文披露的模型、数据与比较基线，不能外推为通用配方。",
        "problem": "Foundational text-to-image training can spend many updates on low-information supervision, while a smaller model alone does not explain convergence efficiency.",
        "mechanism": "Lens jointly increases batch information density with dense captions and mixed image shapes, changes latent/language representations, and then applies bounded post-training and distillation stages.",
        "boundary": "Exact-v1 supports the disclosed component bundle and benchmark comparisons only. It does not isolate each component's causal contribution or establish the reported compute ratio across other models, hardware or quality targets.",
        "tradeoff": "Richer captions and heterogeneous image batches increase data-generation, packing and preprocessing complexity; stronger encoders/VAEs can shift rather than remove compute cost.",
        "fallback": "If richer supervision or mixed-shape packing does not improve matched-budget convergence, retain the simpler data/architecture recipe and measure each component with controlled ablations.",
        "anchor": "## Batch、tokens 与 optimizer steps 不是同一计量",
    },
    "2605.21776": {
        "score": (3, 2, 2),
        "review": "deep_complete_author_bounded_repair",
        "owner": "PLATFORM-EVALUATION-SYSTEM",
        "path": "books/part-06-ai-infrastructure/66-evaluation-system.md",
        "decision": "Integrate — pending root serialized writeback",
        "method": "§2.2 PMI from Contrastive Estimation; §2.3 Recovering Conditional Probabilities; §3 Methods",
        "evaluation": "§4 Benchmark; §5 Results; Appendix A.4 Recalibration; Appendix A.5 Stability",
        "limitations": "§6 Discussion and the generative/Bayes-optimal assumptions behind recovering omitted probability mass",
        "sha256": "7add8122b911699f8013c1d04d2c14fed59bf9fad2699bd22118d5bd5e59b5fe",
        "proposition": "有限候选 prompt 得到的概率会在已列选项内重新归一化，不能直接当作绝对置信度；显式 `OTHER` 可在论文假设下承接遗漏质量，但仍必须用真实标签校准，且不能把理论恢复条件外推成模型知道全部答案空间。",
        "problem": "A prompted finite-choice distribution can rank offered answers while silently assigning zero observable mass to unlisted alternatives, so its probabilities are not automatically calibrated confidence.",
        "mechanism": "PromptNCE adds an explicit OTHER outcome and derives a contrastive estimator that recovers conditional probabilities under stated generative and Bayes-optimal assumptions.",
        "boundary": "The theory and three disclosed datasets support a conditional-probability estimator under stated assumptions, not universal calibration, factuality, or confidence outside the offered outcome construction.",
        "tradeoff": "Adding OTHER makes omitted mass visible but requires a well-specified candidate universe, probability elicitation and calibration data; malformed alternatives can dominate the estimate.",
        "fallback": "When assumptions, label space or calibration transfer fail, report only relative ranking/log-odds and use held-out labels or abstention rather than presenting elicited probabilities as confidence.",
        "anchor": "#### Raw Score 只有经过标签校准才是概率",
    },
    "2605.22202": {
        "score": (2, 2, 2),
        "review": "standard_complete_author_bounded_repair",
        "owner": "MODEL-EMBEDDING",
        "path": "books/part-02-model/12-embedding.md",
        "decision": "Report Only — score 6 standard review",
        "method": "§3.1–§3.5 Methods: paired-input neighborhoods, ICA structure and task linearity",
        "evaluation": "§4 Experiments; §5 Results",
        "limitations": "§6 Discussion; correlations across 25 models and selected MTEB tasks are diagnostic, not causal",
        "sha256": "afcebad8dd7faae884fe15d8444f2529c16cdaf6d0f3dc134c7ec4d73e75ed7e",
        "proposition": "paired-input 的近邻保留与 ICA 结构可作为 embedding space 的任务特定诊断，并与若干 MTEB 结果相关；相关性不能证明这些结构导致性能，也不能替代下游、鲁棒性与部署评估。",
        "problem": "Aggregate embedding benchmarks reveal little about what local structure a model retains for a particular paired-input task.",
        "mechanism": "The paper measures nearest-neighbor overlap and ICA magnitude differences between paired instances and correlates them with task performance across 25 embedding models.",
        "boundary": "The evidence is correlational and bounded to the selected models, languages and MTEB tasks; it does not establish a causal training objective or universal representation-quality metric.",
        "tradeoff": "Structure diagnostics are cheap and model-comparable but depend on sampling, distance geometry and task construction, and can reward structure irrelevant to deployment.",
        "fallback": "Use the diagnostic only to localize representation changes; retain task-level evaluation and perturbation/ablation before changing training or release decisions.",
    },
    "2605.21812": {
        "score": (2, 2, 2),
        "review": "standard_complete_author_sibling_challenge",
        "owner": "TRAIN-DATA",
        "path": "books/part-04-training-system/27-data.md",
        "decision": "No Change — Existing Coverage",
        "method": "§3 Synthetic Query Generation; §4 Label Generation; §5 Production Deployment",
        "evaluation": "§6.1 When Synthetic Data Works; disclosed distribution and pairwise-accuracy comparisons",
        "limitations": "§6.2 Limitations; production evidence is bounded to Airbnb natural-language search",
        "sha256": "80c03e3bac627f13e8618d7204490ec40e30bccf18d01dd7b0b727e6ab02c6d9",
        "proposition": "冷启动 synthetic data 应从真实 seed 与对比对象编译 specification，分别生成 query 与可追踪 label，并在真实流量到来后执行 cold-to-warm 迁移；合成样本只能提供启动先验，不能继续拥有线上分布真值。",
        "problem": "A cold-start natural-language search system lacks both realistic user-query distributions and relevance labels.",
        "mechanism": "Seed-guided contrastive query generation and two label-generation routes create daily training/evaluation artifacts, followed by transition to real user data.",
        "boundary": "The reported distribution and ranking results are application-specific and do not prove synthetic labels remain calibrated under other products or after user behavior changes.",
        "tradeoff": "Seed guidance improves realism but narrows exploration to known intents and adds LLM generation/judging cost plus lineage requirements.",
        "fallback": "Keep a no-seed/diverse branch for discovery, measure drift against real queries, and retire synthetic ownership as sufficient real labels accumulate.",
        "anchor": "### Synthetic data：从“先生成再打分”到 Specification Compilation",
    },
    "2605.21935": {
        "score": (3, 2, 2),
        "review": "deep_complete_author_sibling_challenge",
        "owner": "MULTIMODAL-WORLD-MODELS",
        "path": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
        "decision": "No Change — Existing Coverage",
        "method": "§III-B2 Discrepancy Detection; §III-C Interaction Safety; §III-D3 Closed-loop Memory Evolution",
        "evaluation": "§IV-D Dynamic Adaptation and real Unitree-G1 office evaluation",
        "limitations": "§V Conclusion and Appendix system boundary; one robot/office setup does not establish open-world persistence",
        "sha256": "0e1cd63bdbe55f6724d33bf5857eb90997669a3be3ca8dea6d4d691347da5e39",
        "proposition": "动态环境中的 persistent spatial memory 不能因单帧差异直接改写；应先区分步态/观测噪声与持续变化，再局部更新不一致区域，并让交互安全检查而非视觉记忆拥有动作提交权。",
        "problem": "Humanoid motion distorts perception, while real scene changes and manipulation geometry require a memory that is both persistent and revisable.",
        "mechanism": "MIF separates appearance confidence, topological spatial memory and interaction geometry, and uses discrepancy-triggered local updates in a closed loop.",
        "boundary": "The evidence supports one bounded humanoid/office pipeline; it does not prove discrepancy scores identify causal change or that reconstructed geometry is environment truth.",
        "tradeoff": "Selective updates reduce memory churn and footprint but add confidence calibration, localization and stale-region risks.",
        "fallback": "When discrepancy confidence or localization fails, retain the prior map as a proposal, reacquire direct observations and require controller-level safety validation.",
        "anchor": "#### Foundation Evidence 只有通过 Class-calibrated Gate 才能修改 Persistent Map",
    },
    "2605.21976": {
        "score": (2, 1, 2),
        "review": "standard_complete_author_sibling_challenge",
        "owner": "MULTIMODAL-EMBODIED-VLA",
        "path": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "decision": "Report Only — score 5 standard review",
        "method": "§3 Sensor Overview; §4 Policy Training",
        "evaluation": "§5 Experiments; §6 Results across disclosed sensors and three tasks",
        "limitations": "§7 Conclusions; sensor/task/material coverage is finite and policy-specific",
        "sha256": "e166cfb6dd997f5e3e15bffe199539a2db58698b63fdbd4de39b98cfb5db60f3",
        "proposition": "tactile modality 的价值取决于 manipulation task、材料摩擦与传感器可观测量；不能把“加入触觉”当作统一收益，应以闭环 policy outcome 比较 modality 与 representation。",
        "problem": "Vision-only policies fail on contact-rich manipulation, but there is no task-independent best tactile sensor.",
        "mechanism": "Separate policies consume visual, acoustic, magnetic or resistive tactile streams for three manipulation tasks, enabling task-conditioned sensor comparison.",
        "boundary": "The results support only the disclosed sensors, objects, tasks, policies and setup; they do not rank tactile modalities universally.",
        "tradeoff": "Tactile sensing adds contact observability but also calibration, synchronization, durability and policy-retraining cost.",
        "fallback": "Retain vision/force baselines and choose tactile hardware only after matched task-level ablation and failure testing.",
    },
    "2605.22529": {
        "score": (3, 2, 3),
        "review": "deep_complete_author_sibling_challenge",
        "owner": "PLATFORM-EVALUATION-SYSTEM",
        "path": "books/part-06-ai-infrastructure/66-evaluation-system.md",
        "decision": "No Change — Existing Coverage",
        "method": "§3 theorem and Explainability Fragility Score; §6 mitigation methods",
        "evaluation": "§5 experiments on UNSW-NB15 and disclosed model families",
        "limitations": "§7 Discussion; §8 Conclusion; one benchmark domain does not establish universal attribution behavior",
        "sha256": "eefb59074971217eebebdb93a2bc06b4bfe20248ccc6d47b71e7fe28e3de9972",
        "proposition": "多重共线性会使单次 post-hoc attribution 排名不可识别或不稳定；发布解释结论应版本化相关结构与重采样过程，报告稳定组/方差，并把过滤或训练期稳定化当作受限缓解而非真因果解释。",
        "problem": "Correlated input features can preserve predictive accuracy while making post-hoc feature attributions unstable across resampling and models.",
        "mechanism": "The paper formalizes attribution-variance inflation, proposes a fragility score, and tests grouping/filtering and training-time regularization mitigations.",
        "boundary": "The theorem/experiments support an instability mechanism and bounded mitigations, not causal feature importance or universal security-model robustness.",
        "tradeoff": "Grouping/filtering improves stability but loses feature granularity; regularization adds training cost and can optimize the explanation metric rather than causal truth.",
        "fallback": "Report correlated feature groups and bootstrap instability; when stability/accuracy trade off, retain prediction while refusing fine-grained causal claims.",
        "anchor": "### Attribution 是 Versioned Evaluation Contract",
    },
}


CURATED = {
    "2605.21516": ("More elaborate harnesses can reduce success because decomposition and guidance reshape the execution trajectory.", "Treat workflow granularity, retry budget and guidance-induced action reweighting as versioned harness state; partial harnesses may outperform full decomposition, but terminal outcome remains the acceptance authority."),
    "2605.21543": ("Independent per-model filtering cannot guarantee a global contamination budget across a benchmark shared by several models.", "Model benchmark decontamination as a joint selection problem; a global contamination-rate contract must own the selected item set, while conformal validity remains bounded by its exchangeability and calibration assumptions."),
    "2605.21602": ("An alignment monitor trained in-distribution can fail precisely when policy behavior shifts out of distribution.", "Evaluate monitoring on explicit OOD misalignment slices; detector output is a calibrated sensor with abstention/fallback, not alignment truth."),
    "2605.21603": ("Embedding physical operator schedules in a logical model graph couples model semantics to one device execution plan.", "Separate the logical model graph from the programmable intra-device schedule; compiler/runtime owns legality and equivalence, while model code retains semantic ownership."),
    "2605.21606": ("Teacher-token reliability varies by position and by whether the prefix still admits a successful continuation.", "Use branch viability to weight on-policy self-distillation by token position, but never promote teacher tokens to correctness without outcome/verifier evidence."),
    "2605.21642": ("Accuracy gains after adding continuous thought tokens do not prove the model uses their content.", "Require content replacement, ablation and matched-length controls before attributing behavior to latent/continuous thought tokens; added length or regularization remains an alternative explanation."),
    "2605.21648": ("Constant dropout applies the same perturbation even though early representation formation and late convergence face different noise budgets.", "Treat dropout schedule as training state: front-loading can regularize early signal propagation while reducing late optimization noise, but mean-field edge-of-chaos assumptions and tested architectures bound the claim."),
    "2605.21649": ("Paged KV systems normally decide residency without knowing whether an attention normalizer assigns exact zero support.", "Entmax support can identify zero-support KV pages before decode only when normalization/support identity is stable; otherwise preserve a dense fallback rather than treating sparse support as semantic irrelevance."),
    "2605.21768": ("A memory update cannot be credited reliably from only the terminal outcome of a long trajectory.", "Re-roll out from the same memory state to estimate local write credit, while the terminal verifier/global objective retains truth ownership and memory changes remain revertible."),
    "2605.21779": ("An agent's suspicion or generated exploit narrative is not evidence that a vulnerability is real.", "Require a reproducible proof-of-vulnerability and evidence state before accepting discovery; the agent proposes tests, while execution and deterministic predicates own confirmation."),
    "2605.21800": ("World-model comparisons drift when platform, data, baseline and evaluation settings are not frozen together.", "Version platform, data, baseline and evaluation factors as one experiment identity; a uniform platform improves reproducibility but does not prove simulation realism."),
    "2605.21801": ("Raw semantic entropy depends on representation geometry and estimator calibration, so optimizing it can reward an arbitrary proxy.", "Calibrate the uncertainty proxy against held-out outcomes before using it in policy optimization; entropy remains a sensor, not reward truth."),
    "2605.21803": ("Two optimizers can learn different spectral representations even under the same architecture and objective.", "Optimizer identity is part of the learned representation/training state; compare spectral effects under matched data, budget and parameterization rather than treating the optimizer as a neutral implementation detail."),
    "2605.21847": ("One device-wide power cap hides distinct core, memory and workload-phase bottlenecks.", "Allocate GPU power by component and workload phase only when telemetry and actuators expose those owners; preserve a validated whole-device cap as fallback and bind efficiency claims to the tested GPU/workloads."),
    "2605.21850": ("Long execution trajectories are expensive and noisy supervision when converted directly into training examples.", "Compile trajectories into long-context QA artifacts with source trace and step coverage, while preserving that derived QA is training data—not proof that the original execution was correct."),
}


# Existing No-Change items need a concrete main-body anchor.  Paired markers, if
# present, win; otherwise use this semantically selected heading.
ANCHORS = {
    "2605.21516": "Harness Controller 是版本化策略，不是模型的隐式习惯",
    "2605.21543": "污染校正需要主动干预，而不是事后猜测",
    "2605.21602": "小 Monitor 的跨域能力需要独立训练与校准",
    "2605.21603": "Execution Plan 先拥有 State，再选择 Kernel",
    "2605.21606": "Rollout-conditioned Distillation 应按证据归因，而不是整段照抄",
    "2605.21642": "Attribution 是 Versioned Evaluation Contract",
    "2605.21649": "Attention Normalization 与 Eviction Policy 是联合设计",
    "2605.21768": "从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值",
    "2605.21779": "Agent authority BOM、channel coverage 与 executable PoV",
    "2605.21800": "Evaluation：从画面质量到干预结果",
    "2605.21801": "Entropy Flow 必须在严格 On-policy 边界内治理",
    "2605.21803": "Optimizer 也在选择参数空间中的方向尺度",
    "2605.21812": "Synthetic data：从“先生成再打分”到 Specification Compilation",
    "2605.21850": "Synthetic data：从“先生成再打分”到 Specification Compilation",
    "2605.21854": "Action-facing Representation 也是 Gradient Authority Boundary",
    "2605.21856": "Contamination Detector 必须随 Scale 与 Distribution 重新校准",
    "2605.21862": "Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory",
    "2605.21935": "Foundation Evidence 只有通过 Class-calibrated Gate 才能修改 Persistent Map",
    "2605.21949": "从 Scalar Confidence 到 Safe-commit Certificate",
    "2605.21951": "从固定记忆参数到可扩展 Expert Pool",
    "2605.21965": "Speculative Retrieval Draft 必须经过 Accept / Fallback",
    "2605.21996": "Teacher/Student 混合 Occupancy 是离线与纯 On-policy 之间的分支",
    "2605.21997": "Distributed Event Log 是 Partial Order，不是单一时间线",
    "2605.22001": "Prompt Injection 与 Tool Boundary",
    "2605.22041": "Retrieval Control 应成为 Reader 外部的 Typed State",
    "2605.22057": "从 Skill Catalog 到 Competence-aware Orchestration",
    "2605.22074": "从终局 Reward 到可验证子问题 Curriculum",
    "2605.22102": "Latent Communication 只能压缩 Payload，不能隐藏 Identity",
    "2605.22106": "Eviction 还要选择何时提交，而不只是选择删谁",
    "2605.22138": "先校准不确定性，再决定行动、询问或探索",
    "2605.22148": "Skill Library 的生命周期必须包含 Drift Retirement",
    "2605.22154": "Clarification 与 Workflow-level Speculation 都是有损 Admission",
    "2605.22164": "Repair Metric 必须与 Rollout Horizon 对齐",
    "2605.22166": "Harness Controller 是版本化策略，不是模型的隐式习惯",
    "2605.22177": "从 Skill Catalog 到 Competence-aware Orchestration",
    "2605.22217": "Environment 与 Policy 可以共同演进，但 Held-out Evidence 不能回流",
    "2605.22219": "Retrieval Object 需要 Validity 与 Lifecycle",
    "2605.22269": "Video Ingestion State 与 Decode KV 是两个不同 Cache Object",
    "2605.22283": "Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory",
    "2605.22297": "每层是否需要不同或动态的 Learning Rate",
    "2605.22321": "Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate",
    "2605.22333": "MCP 不等于 Tool Authorization",
    "2605.22337": "压缩状态的 Page Format 必须服务 Append 与 Decode",
    "2605.22343": "Trial Evidence 不能直接提交为 Workflow Revision",
    "2605.22411": "从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值",
    "2605.22416": "层级的管理权不应默认属于 Framework",
    "2605.22446": "Learned Controller 必须位于可验证的 Runtime Assurance 之内",
    "2605.22456": "Clarification 与 Workflow-level Speculation 都是有损 Admission",
    "2605.22493": "Action Chunk 是控制闭环的时间契约",
    "2605.22502": "Scaffold-bound specialization：环境协议也是监督分布",
    "2605.22505": "Component Priority 只能是 Action Evidence",
    "2605.22511": "Outcome-routed Update 先分支，再做 Group Calibration",
    "2605.22526": "Failure attribution、perception routing 与 sticky state ownership",
    "2605.22529": "Attribution 是 Versioned Evaluation Contract",
    "2605.22544": "Evaluation Identity 必须包含 Harness 与 Environment",
    "2605.22564": "Benchmark 生成器也会塑造被评估的任务人口",
    "2605.22566": "Workflow 可见性也会改变 Serving 优化空间",
    "2605.22568": "Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate",
    "2605.22608": "评估对象有四个层次",
    "2605.22620": "多 Reward 聚合不能掩盖 Channel Collapse",
    "2605.22634": "可编程 Skill 需要输入、状态与副作用契约",
    "2605.22643": "安全承诺必须落到真实 Effect、全局 Principal 与可复验修复",
    "2605.22718": "Video Ingestion State 与 Decode KV 是两个不同 Cache Object",
    "2605.22721": "Memory 拓扑不必等于 Agent 拓扑",
    "2605.22731": "后训练分支的本质差异是 State Distribution",
    "2605.22769": "时间顺序也是 Data / Objective Identity",
    "2605.22781": "Resume 是新的状态转换，不是简单读回 Checkpoint",
    "2605.22786": "Latent Communication 只能压缩 Payload，不能隐藏 Identity",
    "2605.22794": "Self-evolution 把候选变成供应链 Revision",
    "2605.22800": "Regularization 必须匹配 Deployment Shift 的方向",
}

CONVERT_TO_INTEGRATE = {
    "2605.21648": ("### Dropout Schedule 也是 Training State", "Constant dropout hides a time-varying perturbation budget; add the bounded front-loaded-schedule branch and preserve constant dropout as fallback."),
    "2605.21847": ("### GPU Power Budget 应按组件与阶段分配", "Whole-device power caps do not express component/phase ownership; add component-aware telemetry/actuation and retain a validated global-cap fallback."),
    "2605.22014": ("### Live Reconfiguration 需要 Target World 与显式 Commit", "Checkpoint/restart coverage does not express an asynchronously prepared target world, live mixed-parallel resharding and a lightweight topology commit."),
}


def score_dict(score):
    a, b, c = score
    return {"design_delta": a, "system_reach": b, "durability": c, "total": a + b + c}


for arxiv_id, cfg in RESTORED.items():
    ident = identities[arxiv_id]
    ident.update(
        screening_status="retained",
        v3_screening_status="retained",
        closure_family=None,
        review_status=cfg["review"],
        access_status="accessible",
        books_disposition=cfg["decision"],
        score_v3=score_dict(cfg["score"]),
        closure_reaudit_status="restored_by_r2_bounded_false_negative_challenge",
        integration_disposition=cfg["decision"],
    )
    rec = closure_by_id[arxiv_id]
    rec.update(
        decision="restored_to_candidate_denominator",
        family_specific_reason="题摘语义挑战确认其改变可复用的 AI System 状态、控制权或 evaluation contract；已恢复并完成 exact-v1 审阅。",
        r2_bounded_challenge=True,
    )
    ev = {
        "source_family_id": ident["source_family_id"],
        "arxiv_id": arxiv_id,
        "title": ident["title"],
        "primary_evidence_version": f"arXiv:{arxiv_id}v1",
        "retrieval_route": "official arXiv exact-v1 HTML",
        "retrieved_at": CHECKED_AT,
        "review_status": cfg["review"],
        "access_status": "accessible",
        "problem": cfg["problem"],
        "mechanism": cfg["mechanism"],
        "adopted_proposition": cfg["proposition"],
        "method_locator": cfg["method"],
        "evaluation_locator": cfg["evaluation"],
        "limitations_locator": cfg["limitations"],
        "claim_boundary": cfg["boundary"],
        "tradeoff": cfg["tradeoff"],
        "failure_fallback": cfg["fallback"],
        "artifact_locator": f"https://arxiv.org/html/{arxiv_id}v1; sha256:{cfg['sha256']}",
        "owner_node": cfg["owner"],
        "score_v2": score_dict(cfg["score"]),
        "completion_result": "complete",
    }
    evidence_by_id[arxiv_id] = ev
    if cfg["decision"].startswith("Integrate"):
        existing = "Current owner main body lacks this exact state/control/evaluation proposition."
    elif cfg["decision"].startswith("Report Only"):
        existing = "Standard review is retained in the Daily; no positive Books coverage claim is made."
    else:
        existing = "Current owner main body already carries the durable proposition; the paper is bounded supporting evidence."
    comparison_by_id[arxiv_id] = {
        "arxiv_id": arxiv_id,
        "source_family_id": ident["source_family_id"],
        "title": ident["title"],
        "owner_node": cfg["owner"],
        "owner_path": cfg["path"],
        "existing_proposition": existing,
        "new_evidence_delta": cfg["proposition"],
        "decision": cfg["decision"],
        "comparison_basis": "current owner main-body proposition and nearest ownership boundary; Review notes and title/marker matches do not count as semantic coverage",
        "evidence_route": "official exact-v1 HTML bounded author review",
    }


# Normalize the legacy Harness evidence projection before filling the common fields.
legacy = evidence_by_id["2605.21516"]
legacy.setdefault("problem", legacy.get("problem_and_changed_constraint"))
legacy.setdefault("mechanism", legacy.get("mechanism_and_ownership"))
legacy.setdefault("claim_boundary", legacy.get("proof_boundary"))
legacy.setdefault("artifact_locator", legacy.get("retrieval", {}).get("url"))

for arxiv_id, ev in evidence_by_id.items():
    ident = identities[arxiv_id]
    ev.setdefault("title", ident["title"])
    ev.setdefault("owner_node", comparison_by_id[arxiv_id]["owner_node"])
    if arxiv_id in CURATED:
        problem, proposition = CURATED[arxiv_id]
        ev.setdefault("problem", problem)
        ev.setdefault("mechanism", proposition)
        ev["adopted_proposition"] = proposition
        ev.setdefault("review_status", ident["review_status"])
        ev.setdefault("access_status", "accessible")
    elif not ev.get("adopted_proposition"):
        # These records already passed source-specific exact-v1 author review;
        # the mechanism is the narrow, adopted proposition, not a new claim.
        ev["adopted_proposition"] = ev.get("mechanism") or comparison_by_id[arxiv_id]["new_evidence_delta"]
    if not ev.get("problem"):
        ev["problem"] = identities[arxiv_id]["abstract"].split(". ", 1)[0] + "."
    if not ev.get("mechanism"):
        ev["mechanism"] = ev["adopted_proposition"]
    if not ev.get("review_status"):
        ev["review_status"] = ident["review_status"]

CONVERTED_EVIDENCE_BOUNDARIES = {
    "2605.21648": {
        "tradeoff": "A time-varying dropout schedule adds schedule identity and tuning state; the reported fixed-budget gains are bounded to the disclosed MLP/ViT experiments and do not establish the same optimum for LLM pretraining.",
        "failure_fallback": "If edge-of-chaos assumptions, activation class or matched-budget validation do not transfer, retain constant dropout or no dropout and treat the schedule as an experimental branch.",
    },
    "2605.21847": {
        "tradeoff": "Component-level control needs component telemetry and actuators, and can move thermal or bandwidth pressure between core and memory; reported 10%/5% figures are bounded to the tested GPUs and operations.",
        "failure_fallback": "When component observability, actuator isolation or workload-phase classification is weak, fall back to a validated whole-device power cap and preserve SLO/thermal guards.",
    },
    "2605.22014": {
        "tradeoff": "A dual-world handoff consumes bounded extra memory, initialization capacity and network bandwidth while the live world trains, and concurrent preparation can interfere with the critical path.",
        "failure_fallback": "If target-world preparation misses the warning window, transfer validation fails or the commit cannot be atomic, abort the handoff and use the existing checkpoint/restart recovery path.",
    },
}
for arxiv_id, fields in CONVERTED_EVIDENCE_BOUNDARIES.items():
    evidence_by_id[arxiv_id].update(fields)


# Three previously generic No-Change decisions are real Books deltas.
for arxiv_id, (anchor, delta) in CONVERT_TO_INTEGRATE.items():
    comp = comparison_by_id[arxiv_id]
    comp.update(
        existing_proposition=f"Current main body around `{anchor}` does not yet express the source-specific mechanism.",
        new_evidence_delta=evidence_by_id[arxiv_id]["adopted_proposition"],
        decision="Integrate — pending root serialized writeback",
        proposed_anchor=anchor,
        exact_difference=delta,
        comparison_status="current_body_rechecked_author_delta_confirmed",
    )
    identities[arxiv_id]["books_disposition"] = comp["decision"]
    identities[arxiv_id]["integration_disposition"] = comp["decision"]


def find_marker_heading(path: Path, source_family: str):
    lines = path.read_text().splitlines()
    marker = f"semantic-body-binding:{source_family}"
    positions = [i for i, line in enumerate(lines) if marker in line]
    if not positions:
        return None
    pos = min(positions)
    for i in range(pos, -1, -1):
        if re.match(r"^#{2,4} ", lines[i]):
            return lines[i].lstrip("# ")
    return None


def anchor_record(comp):
    path = ROOT / comp["owner_path"]
    text = path.read_text()
    heading = find_marker_heading(path, comp["source_family_id"]) or ANCHORS.get(comp["arxiv_id"])
    if not heading:
        raise RuntimeError(f"No semantic anchor configured for {comp['arxiv_id']}")
    lines = text.splitlines()
    heading_line = next((i for i, line in enumerate(lines) if line.lstrip("# ") == heading), None)
    if heading_line is None:
        raise RuntimeError(f"Anchor not found for {comp['arxiv_id']}: {heading!r} in {path}")
    heading_level = len(lines[heading_line]) - len(lines[heading_line].lstrip("#"))
    excerpt_parts = []
    for line in lines[heading_line + 1 :]:
        nested = re.match(r"^(#{2,4}) ", line)
        if nested:
            if len(nested.group(1)) <= heading_level and excerpt_parts:
                break
            continue
        if line.strip() and not line.strip().startswith("<!--"):
            excerpt_parts.append(line.strip())
        if len(" ".join(excerpt_parts)) >= 260:
            break
    excerpt = " ".join(excerpt_parts)[:420]
    comp.update(
        current_body_heading=heading,
        current_body_locator=f"{comp['owner_path']}#{heading_line + 1}",
        current_body_excerpt=excerpt,
        exact_difference=(
            f"该来源新增的受限证据是：{comp['new_evidence_delta']} 当前正文已经规定相同的状态/控制 owner、"
            "failure boundary 或 fallback；该论文没有改变现有设计结论，只增加一个有 workload 边界的实证实例。"
        ),
        comparison_status="current_body_rechecked_author",
    )
    comp["existing_proposition"] = f"`{heading}` 主正文：{excerpt}"


for arxiv_id in sorted((GENERIC_NC_IDS | ANCHOR_RECHECK_IDS) - set(CONVERT_TO_INTEGRATE) | {"2605.21812", "2605.21935", "2605.22529"}):
    anchor_record(comparison_by_id[arxiv_id])


# Add five root-owned writes without touching Books.
pending_ids = ["2605.21573", "2605.21776", "2605.21648", "2605.21847", "2605.22014"]
queue_by_id = {item["arxiv_id"]: item for item in queue["items"]}
for arxiv_id in pending_ids:
    ident = identities[arxiv_id]
    ev = evidence_by_id[arxiv_id]
    comp = comparison_by_id[arxiv_id]
    anchor = RESTORED.get(arxiv_id, {}).get("anchor") or CONVERT_TO_INTEGRATE[arxiv_id][0]
    queue_by_id[arxiv_id] = {
        "report_date": "2026-05-22",
        "arxiv_id": arxiv_id,
        "source_family_id": ident["source_family_id"],
        "title": ident["title"],
        "primary": f"https://arxiv.org/html/{arxiv_id}v1",
        "stable_node_id": comp["owner_node"],
        "target_path": comp["owner_path"],
        "anchor": anchor,
        "old_baseline_and_constraint_change": ev["problem"],
        "adopted_proposition": ev["adopted_proposition"],
        "method_locator": ev["method_locator"],
        "evaluation_locator": ev["evaluation_locator"],
        "nonproof_locator": ev["limitations_locator"],
        "evidence_boundary": ev["claim_boundary"],
        "tradeoff": ev.get("tradeoff", "Not Disclosed beyond the exact-v1 boundary."),
        "failure_fallback": ev.get("failure_fallback", "Retain the prior mechanism when the source-specific gate fails."),
        "state_control_ownership": ev["mechanism"],
        "writer": "root serialized Books owner",
        "author_must_not_write_books": True,
        "status": "pending_root_writeback",
        "required_marker": f"semantic-body-binding:{ident['source_family_id']}:start/end",
    }
queue["items"] = sorted(queue_by_id.values(), key=lambda x: x["arxiv_id"])
queue["queue_count"] = len([x for x in queue["items"] if x.get("status") == "pending_root_writeback"])
queue["item_count"] = len(queue["items"])
queue["status"] = "5 bounded R2 deltas pending root serialized Books writeback; report remains Ongoing pending fresh non-author review"
queue["books_gate"] = "46 prior root bindings remain present; five new deltas must be written and freshly reviewed before the report can become Complete."


# Recompute every projection from the canonical identity/evidence/comparison sets.
ledger["identities"] = sorted(identities.values(), key=lambda x: x["arxiv_id"])
ledger["retained_count"] = sum(x.get("v3_screening_status") == "retained" for x in ledger["identities"])
ledger["pre_denominator_closure_count"] = sum(x.get("v3_screening_status") == "pre_denominator_closure" for x in ledger["identities"])
ledger["withdrawn_count"] = sum(x.get("v3_screening_status") == "withdrawn" for x in ledger["identities"])
ledger["evidence_complete_count"] = len(evidence_by_id)
ledger["evidence_deep_complete_count"] = sum("deep_complete" in x.get("review_status", "") for x in evidence_by_id.values())
ledger["evidence_standard_complete_count"] = sum("standard_complete" in x.get("review_status", "") for x in evidence_by_id.values())
ledger["evidence_review_pending_count"] = 0
ledger["evidence_blocked_count"] = 0
decisions = Counter(x["decision"].split(" — ", 1)[0] for x in comparison_by_id.values())
ledger["books_integrate_count"] = decisions["Integrate"]
ledger["books_applied_count"] = sum("root applied" in x["decision"] for x in comparison_by_id.values())
ledger["books_pending_integrate_count"] = sum(x["decision"] == "Integrate — pending root serialized writeback" for x in comparison_by_id.values())
ledger["books_no_change_count"] = decisions["No Change"]
ledger["books_report_only_count"] = decisions["Report Only"]
ledger["books_deferred_count"] = 0
ledger["closure_family_counts"] = dict(sorted(Counter(x.get("closure_family") for x in ledger["identities"] if x.get("v3_screening_status") == "pre_denominator_closure").items()))
ledger["status"] = "r2_bounded_author_repair_complete; 5 root_writebacks_and_new_fresh_non_author_review_pending"
ledger["closure_reaudit"] = {
    "scope": "501 prior template-derived closures plus bounded same-reason sibling false-negative challenge; no source/date expansion",
    "audited_count": 501,
    "restored_count": 89,
    "confirmed_fn_seed_count": 21,
    "additional_restored_count": 68,
    "continued_closure_count": 412,
    "special_non_template_closure_count_outside_scope": 3,
    "receipt": "closure-semantic-reaudit-v3.json",
    "sibling_challenge_receipt": "closure-sibling-false-negative-challenge-v3.json",
}

closure["checked_at"] = CHECKED_AT
closure["counts"] = {"audited": 501, "restored": 89, "confirmed_fn_seed": 21, "additional_restored": 68, "continued_closure": 412}
closure["method"] = "Every record binds owner-batch title and full abstract to a family-specific contribution decision; R2 additionally challenges bounded siblings sharing the three false-negative closure reasons. Restored families then receive exact-v1 review."

evidence = sorted(evidence_by_id.values(), key=lambda x: x["arxiv_id"])
comparisons = sorted(comparison_by_id.values(), key=lambda x: x["arxiv_id"])

prov_by_id = {item["arxiv_id"]: item for item in provenance["records"]}
for arxiv_id, cfg in RESTORED.items():
    prov_by_id[arxiv_id] = {
        "arxiv_id": arxiv_id,
        "status": "accessible",
        "route": "official arXiv exact-v1 HTML",
        "artifact_locator": f"https://arxiv.org/html/{arxiv_id}v1",
        "sha256": cfg["sha256"],
        "method_heading": cfg["method"],
        "evaluation_heading": cfg["evaluation"],
        "nonproof_heading": cfg["limitations"],
        "bounded_r2_restore": True,
    }
provenance["checked_at"] = CHECKED_AT
provenance["restored_count"] = len(prov_by_id)
provenance["accessible_count"] = sum(x["status"] == "accessible" for x in prov_by_id.values())
provenance["blocked_count"] = 0
provenance["records"] = sorted(prov_by_id.values(), key=lambda x: x["arxiv_id"])


sibling = {
    "schema": "daily-v3-bounded-sibling-false-negative-challenge",
    "report_date": "2026-05-22",
    "checked_at": CHECKED_AT,
    "scope": "Only siblings in the three closure families of the R2-confirmed false negatives; title plus full abstract challenge, exact-v1 only for restored items; no source/date expansion.",
    "seed_false_negatives": ["2605.21573", "2605.21776", "2605.22202"],
    "additional_restorations": ["2605.21812", "2605.21935", "2605.21976", "2605.22529"],
    "continued_closure_samples": [
        {"arxiv_id": "2605.21968", "reason": "small-task optimizer combination; no transferable LLM/AI-system state or control delta"},
        {"arxiv_id": "2605.22478", "reason": "narrow conversational-information-retrieval agent combination; no durable multi-agent protocol or system contract delta"},
        {"arxiv_id": "2605.22809", "reason": "autonomous-driving sensor conversion application; no reusable AI-system ownership change"},
        {"arxiv_id": "2605.21715", "reason": "generic queueing scheduler outside the project's LLM/AI-infrastructure mechanism boundary"},
        {"arxiv_id": "2605.21932", "reason": "multi-robot auction application without a new LLM/agent protocol contract"},
        {"arxiv_id": "2605.22513", "reason": "domain control meta-learning method; no transferable training/runtime contract"},
        {"arxiv_id": "2605.21874", "reason": "supercomputer sonification asset; no AI-system mechanism delta"},
        {"arxiv_id": "2605.22480", "reason": "GNN-specific regularization result without a durable project-level design delta"},
        {"arxiv_id": "2605.22681", "reason": "AI for Science is paused and the abstract offers no independent reusable AI-system mechanism"},
        {"arxiv_id": "2605.21491", "reason": "AI for Science is paused and the contribution is domain-local"},
        {"arxiv_id": "2605.21975", "reason": "financial-domain model result without a transferable system contract"},
        {"arxiv_id": "2605.22109", "reason": "personality/task method without a durable system ownership change"},
        {"arxiv_id": "2605.22600", "reason": "motion-planning local method without a project-level mechanism delta"},
        {"arxiv_id": "2605.21544", "reason": "chemical-sensing application; no reusable AI-system contract"},
        {"arxiv_id": "2605.22300", "reason": "AI-for-Science benchmark asset is paused and adds no current evaluation-contract delta"},
        {"arxiv_id": "2605.21773", "reason": "HIDS benchmark asset without a new evaluation contract"},
        {"arxiv_id": "2605.22100", "reason": "document-parsing benchmark asset without a durable evaluation-system delta"},
        {"arxiv_id": "2605.21919", "reason": "SDG-domain asset without transferable system state/control ownership"},
        {"arxiv_id": "2605.22008", "reason": "Wi-Fi fault benchmark without a new project-level evaluation contract"},
        {"arxiv_id": "2605.22413", "reason": "receipt benchmark asset without a durable system-design delta"},
    ],
    "result": "7 restored; bounded sibling samples above remain closed with family-specific reasons.",
}


def rel_book(path: str) -> str:
    return "../../../../" + path


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


prefix = REPORT.read_text().split("## 3. 候选与判断", 1)[0]
prefix = re.sub(r"\*\*检查时间：\*\* .*", f"**检查时间：** {CHECKED_AT}", prefix)
prefix = re.sub(
    r"## 1\. 结论\n.*?(?=\n## 2\. 来源覆盖)",
    "## 1. 结论\n\n"
    "本次继续冻结官方 announcement-time owner batch：`667 = 252 retained + 415 pre-denominator closure + 0 withdrawn`，不扩来源或日期。R2 明确指出的 3 个 false negative 已恢复；对相同 closure reason 的有界 sibling challenge 又恢复 4 项，其余抽查项均写入 family-specific closure。501 项模板 closure 的最终投影为 `89 restored + 412 continued closure`，另有 3 项非模板 closure。\n\n"
    "Evidence 已完成 `252 = 195 deep + 57 standard + 0 pending + 0 blocked`；Books 投影为 `252 = 46 Applied + 5 pending Integrate + 145 No Change + 56 Report Only`。70 项缺失 adopted proposition 已补齐并与 problem/mechanism 对齐；No Change 已绑定当前主正文 heading、位置、excerpt 与 exact difference。作者侧修复已完成，但 5 个 Books delta 尚待 root 串行写回，写回后仍需另一位 fresh non-author 复核，因此状态保持 **进行中**。\n\n"
    "有界 sibling challenge 见 [`closure-sibling-false-negative-challenge-v3.json`](../_sources/daily-20260522/closure-sibling-false-negative-challenge-v3.json)，exact-v1 证据与 Books 比较分别见对应 canonical JSON。\n",
    prefix,
    flags=re.S,
)

rows = []
cards = []
for ident in ledger["identities"]:
    if ident.get("v3_screening_status") != "retained":
        continue
    arxiv_id = ident["arxiv_id"]
    ev = evidence_by_id[arxiv_id]
    comp = comparison_by_id[arxiv_id]
    score = ident["score_v3"]
    review_label = "深入完成" if "deep_complete" in ev.get("review_status", "") else "标准完成"
    if comp["decision"].startswith("Integrate — root applied"):
        book_label = "整合：既有 root binding 已通过写后复核"
    elif comp["decision"] == "Integrate — pending root serialized writeback":
        book_label = "整合：已进入 root 串行写回队列，尚未落书"
    elif comp["decision"].startswith("No Change"):
        book_label = (
            f"已有覆盖：`{comp['current_body_heading']}`"
            if comp.get("current_body_heading")
            else "已有覆盖：当前主正文的 source-specific 比较已通过"
        )
    else:
        book_label = "仅报告：标准审阅，不主张 Books 已覆盖"
    rows.append(
        f"| [{esc(ident['title'])}](https://arxiv.org/html/{arxiv_id}v1) | 2026-05-22T08:00:00+08:00 | "
        f"{esc(ev['adopted_proposition'])}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']} | "
        f"{review_label} | {book_label}；[章节]({rel_book(comp['owner_path'])})；`{comp['owner_node']}` |"
    )
    trade = ev.get("tradeoff") or ev.get("tradeoff_and_failure_mode") or "未超出 exact-v1 披露边界主张通用 trade-off。"
    fallback = ev.get("failure_fallback") or ev.get("old_path_and_coexistence") or "当论文前提或 workload 不成立时保留现有机制。"
    if comp["decision"].startswith("No Change") and comp.get("current_body_heading"):
        comparison_text = (
            f"当前正文锚点=`{comp['current_body_heading']}`；位置=`{comp['current_body_locator']}`；"
            f"正文命题={comp['current_body_excerpt']}；差异判断={comp['exact_difference']}"
        )
    else:
        comparison_text = f"既有命题={comp['existing_proposition']}；差异判断={comp.get('exact_difference', comp['new_evidence_delta'])}"
    cards.append(
        f"### [{esc(ident['title'])}](https://arxiv.org/html/{arxiv_id}v1)\n\n"
        f"版本与证据：`arXiv:{arxiv_id}v1`；Method=`{esc(ev.get('method_locator','Not Disclosed'))}`；"
        f"Evaluation=`{esc(ev.get('evaluation_locator','Not Disclosed'))}`；Non-proof=`{esc(ev.get('limitations_locator','Not Disclosed'))}`。\n\n"
        f"问题：{ev['problem']} 机制：{ev['mechanism']} 采用命题：{ev['adopted_proposition']} "
        f"证据边界：{ev.get('claim_boundary','Not Disclosed')}\n\n"
        f"Books 比较：owner=`{comp['owner_node']}`，target=`{comp['owner_path']}`；{comparison_text}；结论=`{comp['decision']}`。 "
        f"Trade-off：{trade} Failure/Fallback：{fallback}\n"
    )

body = "## 3. 候选与判断\n\n| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |\n| --- | --- | --- | --- | --- |\n" + "\n".join(rows)
body += "\n\n## 4. 证据与知识整合\n\n" + "\n".join(cards)
body += (
    "\n结构化 Evidence 见 [`exact-v1-evidence-v3.json`](../_sources/daily-20260522/exact-v1-evidence-v3.json)，逐项 current Books 命题比较见 [`books-current-content-comparison-v3.json`](../_sources/daily-20260522/books-current-content-comparison-v3.json)。\n\n"
    "## 5. 缺口与下一步\n\n"
    "- 5 个新确认 Books delta 已进入 [`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260522/BOOKS_WRITEBACK_QUEUE_V3.json)：`2605.21573`、`2605.21776`、`2605.21648`、`2605.21847`、`2605.22014`。作者不得直接修改共享 Books；必须由 root 按章节串行写回。\n"
    "- 写回后必须由未参与本轮作者修复的 fresh non-author 逐项挑战 owner、正文位置、采用命题、证据边界、trade-off、failure/fallback；不能由本作者自签 Complete。\n"
    "- Meta 与 Hunyuan source-local 外部材料缺口继续隔离；不作为 no-hit 证明，也不影响已冻结 arXiv identity 集合的本轮有界修复。\n\n"
    "## 6. 复核\n\n"
    "- Author-side bounded R2 repair：已完成。恒等式 `667=252+415+0`；Evidence `252=195+57`；Books `252=46 Applied+5 pending Integrate+145 No Change+56 Report Only`。\n"
    "- False-negative challenge：R2 seeds 3 项与 bounded siblings 4 项恢复；其余抽查项保留具体 closure 理由。\n"
    "- 当前 Gate：**Ongoing / author pass only**。等待 5 项 root Books 写回与另一位 fresh non-author 最终语义复核。\n"
)
REPORT.write_text(prefix + body)

dump("screening-ledger-v3.json", ledger)
dump("closure-semantic-reaudit-v3.json", closure)
dump("exact-v1-evidence-v3.json", evidence)
dump("books-current-content-comparison-v3.json", comparisons)
dump("BOOKS_WRITEBACK_QUEUE_V3.json", queue)
dump("closure-repair-exact-v1-provenance-v3.json", provenance)
dump("closure-sibling-false-negative-challenge-v3.json", sibling)

checkpoint = f"""# 2026-05-22 R2 有界作者修复 checkpoint

- 时间：{CHECKED_AT}
- 范围：仅冻结的 667 identities，不扩来源或日期。
- 分母：252 retained / 415 closure / 0 withdrawn。
- 恢复：R2 指定 3 项 + bounded siblings 4 项。
- Evidence：195 deep + 57 standard，pending/blocked=0。
- Books：46 Applied + 5 pending Integrate + 145 No Change + 56 Report Only。
- Root queue：2605.21573、2605.21776、2605.21648、2605.21847、2605.22014。
- Gate：Ongoing；作者侧不得自签 Complete，必须等待 root 写回和另一位 fresh non-author 复核。
"""
(SRC / "AUTHOR_R2_BOUNDED_REPAIR_CHECKPOINT_20260916.md").write_text(checkpoint)

print(json.dumps({
    "raw": ledger["raw_identity_count"],
    "retained": ledger["retained_count"],
    "closure": ledger["pre_denominator_closure_count"],
    "deep": ledger["evidence_deep_complete_count"],
    "standard": ledger["evidence_standard_complete_count"],
    "integrate": ledger["books_integrate_count"],
    "applied": ledger["books_applied_count"],
    "pending_integrate": ledger["books_pending_integrate_count"],
    "no_change": ledger["books_no_change_count"],
    "report_only": ledger["books_report_only_count"],
    "queue": queue["queue_count"],
}, ensure_ascii=False, indent=2))
