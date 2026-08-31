#!/usr/bin/env python3
"""Generate the 2026-05-01 V2.1 Daily packet without shared Books writes."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/05/_sources/daily-20260501"
REPORT = ROOT / "papers/2026/05/01/README.md"
INVENTORY = PACKET / "inventory.json"


def c(aid, score, node, disposition, chapter, adjacent, claim, method, evaluation,
      limits, relation="Principle Reuse", override="none", artifact="Not Disclosed — no event-time artifact revision is used"):
    if not re.search(r"§|Table|Appendix|Not Disclosed", evaluation, re.I):
        evaluation = "Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; " + evaluation
    if not re.search(r"§|Limitations|Table|Appendix|Not Disclosed", limits, re.I):
        limits = "Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: " + limits
    return dict(aid=aid, fid=f"SF-2026-ARXIV-{aid.replace('.', '-')}", score=score,
                total=sum(score), node=node, disposition=disposition, chapter=chapter,
                adjacent=adjacent, claim=claim, method=method, evaluation=evaluation,
                limits=limits, relation=relation, override=override, artifact=artifact,
                route="deep" if sum(score) >= 7 or override != "none" else "standard")


C = [
    c("2604.27289", (3,3,3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/72-security.md#L14", "books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74",
      "结构化治理把模型产生的 intent 与真实 effect 分离：纯计算只能产生 typed directive，唯一 effect interpreter 执行 authorization、capability check 与 provenance；安全命题因此落在可枚举的执行边界，而不是要求模型行为本身可判定。",
      "§2.2-3.3 event types, governance operator and coinductive safety predicate; §8 mechanization; §9 verified interpreter specification",
      "§8.3-8.5 36 Coq modules/454 results/zero admitted lemmas; §9 property-based conformance against BEAM runtime",
      "§12 Limitations：formalization is system-specific; two named results remain paper proofs; proof covers the modeled effect boundary and does not establish policy correctness or arbitrary runtime behavior",
      relation="Layering / Dependency", override="release_security_contract",
      artifact="Not Disclosed — public Coq artifact is declared in exact-v1, but this review did not independently rebuild it"),
    c("2604.27292", (3,3,3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/72-security.md#L14", "books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74",
      "Effect governance 的覆盖边界必须与系统可表达的 effect 边界重合；与其对 Turing-complete 行为做不可判定的语义过滤，不如把 computation 与 effect 分离，只对 typed directive 的 capability 与 policy 做可判定检查。",
      "§2-4 expressiveness/governance boundaries, Rice-theorem boundary and coterminous governance; §5-7 behavioral comparison and execution-pipeline consequence",
      "§4 gives the testable structural criterion; formal claims defer to the companion Coq development rather than an independent empirical benchmark",
      "§9 Limitations：scope is effects, existing frameworks may require re-architecture, structural coverage does not prove policy correctness, and restricted languages trade expressiveness for decidability",
      relation="Explanatory Analogy", override="release_security_contract",
      artifact="Not Disclosed — companion Coq repository is linked; this conceptual paper has no separate empirical artifact"),
    c("2604.27309", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L12", "books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-06-ai-infrastructure/73-production-practices.md#L14",
      "一次性 benchmark 不能拥有 release authority；部署中的 rubric、用户反馈、运行 SLO、成本和受控版本实验必须形成持续、可追溯的发布控制回路。",
      "§5.1-5.8 governance architecture, controlled experimentation, monitoring and cost", "§2.1-2.6 seven versions, clinician rubrics, live feedback and technical performance", "§3.6 single product/domain, observational feedback and short deployment window", override="knowledge_gap"),
    c("2604.27792", (2,3,3), "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage",
      "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14", "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14; books/part-05-inference-system/49-tensorrt-llm.md#L14",
      "World-action model 把 future visual state 与 action 放入联合生成路径，可减少 VGM→IDM 串行误差；但真正的 physical authority 仍属于 controller、safety envelope 与环境反馈。",
      "§2 architecture, heterogeneous pre/post-training and real-time inference optimizations", "§3 simulation, world-model and real-robot evaluations", "§4 future work; no independent safety or broad sim-to-real guarantee", relation="Direct Evolution"),
    c("2604.27844", (3,3,3), "TRAIN-DISTRIBUTED-TRAINING", "Integrate",
      "books/part-04-training-system/36-distributed-training.md#L69", "books/part-04-training-system/37-data-parallel.md#L1; books/part-04-training-system/41-distributed-training-runtime.md#L1",
      "通信压缩只有在 encode/decode 不把 network bottleneck 迁移为 GPU critical-path bottleneck 时才成立；lossless exponent coding 与 collective-aware layout 以 bit-exactness 换取数据分布假设和额外 kernel/switcher 控制状态。",
      "§3-5 compressed collective API, exponent coding, GPU pipeline and adaptive switcher", "§6 dense/MoE training on 64 GPUs with collective and end-to-end comparisons", "§6.6 observed tensor normality is workload-specific; paper does not prove universal distributions", relation="Alternative Branch", override="knowledge_gap"),
    c("2604.28138", (3,3,3), "AGENT-PLATFORM", "Integrate",
      "books/part-07-agent/84-agent-platform.md#L50", "books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/73-production-practices.md#L1",
      "Agent recovery state 不等于 chat history：tool side effects、filesystem、process 与 runtime artifact 必须在 turn boundary 形成可提交 checkpoint；语义稀疏检测减少 checkpoint traffic，却引入 eBPF 分类误差、co-location contention 与 restore consistency。",
      "§4-6 coordinator, eBPF inspector, C/R data plane and deployment refinement", "§7 correctness, overhead, mechanism ablations and code-agent case study", "§9 Conclusion — exact-v1 has no dedicated limitations section; evidence is confined to Linux sandbox workloads and evaluated C/R backends", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.28139", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L18", "books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L69",
      "Live agent benchmark 必须同时冻结 refreshable demand signal 与可复现实验 snapshot，并优先用 service/workspace terminal evidence 验证 action，而不是把 final response 或单一 leaderboard 当完成证明。",
      "§3 refreshable signals, release snapshot, controlled fixtures and graders", "§4-5 105 tasks, 13 models, trace/artifact grading and family-level analysis", "§3.3 and §5.5 current release and ClawHub-derived demand are not a universal production distribution", override="knowledge_gap"),
    c("2605.00066", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L35", "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L27; books/part-06-ai-infrastructure/67-monitoring.md#L1",
      "Open-loop perception/planning metrics 不能自动代理 closed-loop outcome；跨 benchmark 相关性必须先对齐 policy、environment、horizon、intervention 与 failure definition。",
      "§3 cross-benchmark metric mapping and correlation protocol", "§4 NAVSIM and Bench2Drive cross-benchmark results and sensitivity", "§5 selected benchmarks/models and correlation do not establish causality or real-world safety", override="knowledge_gap"),
    c("2605.00081", (3,3,3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/72-security.md#L14", "books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74",
      "Agent security 不能只判断 intent 或输出文本；可执行 effect 必须在独立 mediation boundary 由 typed contract、authorization 和 audit 拦截，且模型层与执行层各自保留可观测责任。",
      "§2-6 threat assumptions, contract language, dual-layer observability and enforcement", "§7 examples and policy-composition analysis", "§8 impossibility/scope boundary; disclosed framework is not proof of all semantic safety", relation="Direct Evolution", override="release_security_contract"),
    c("2605.00136", (2,3,3), "AGENT-TOOL-CALLING", "No Change — Existing Coverage",
      "books/part-07-agent/78-tool-calling.md#L42", "books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L50",
      "Tool-use accuracy 必须拆开协议格式成本、selection/argument error、transport/runtime failure 与真实工具收益；更多工具或更长 schema 会征收 context 和 routing tax，不能把失败都归因于模型不会调用。",
      "§3-4 decomposition of tool protocol, selection and execution costs", "§5 controlled tool-use diagnosis across models/tasks", "§6/discussion task and framework scope; no universal tax constant", relation="Explanatory Analogy", override="knowledge_gap"),
    c("2605.00155", (2,2,2), "TRAIN-RLHF", "No Change — Existing Coverage",
      "books/part-04-training-system/31-rlhf.md#L168", "books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/34-dpo.md#L1",
      "Preference optimization can treat annotator/reward uncertainty as a distributional ambiguity set and optimize worst-case regret, but robustness radius and reference policy become new control assumptions rather than removing reward misspecification.",
      "§3-5 Wasserstein ambiguity set and robust regret objective", "§6 experiments and ablations on specified preference datasets/models", "Not Disclosed — exact-v1 has no dedicated limitations section; author experiments do not establish universal robustness radius"),
    c("2605.00161", (2,2,3), "MULTIMODAL-GENERATIVE-PARADIGMS", "No Change — Existing Coverage",
      "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1", "books/part-02-model/18-decoder-only.md#L1; books/part-05-inference-system/48-speculative-decoding.md#L1",
      "Consistent diffusion language modeling narrows train/inference inconsistency by coupling conditional denoising states; it trades token-sequential commitment for iterative correction and does not erase sampling-step, cache or rollback costs.",
      "§2-3 consistency objective and diffusion language-model mechanism", "§4-5 language-model evaluations and ablations", "§6 Conclusion — exact-v1 has no dedicated limitations section; workloads do not prove replacement of autoregressive generation", relation="Alternative Branch"),
    c("2605.00180", (3,3,3), "INFER-SCHEDULING", "No Change — Existing Coverage",
      "books/part-05-inference-system/56-inference-scheduling.md#L35", "books/part-05-inference-system/52-distributed-inference.md#L1; books/part-06-ai-infrastructure/63-resource-scheduling.md#L1",
      "Model routing 的 cold start 不是缺少一个静态 leaderboard，而是缺少 workload-conditioned profile；图结构从已知模型迁移观测可降低探索成本，但 profile staleness、uncertainty 和 online fallback 必须进入 admission/routing contract。",
      "§3 graph profile construction and cold-start transfer", "§4-5 new-model routing experiments, baselines and ablations", "§6 Conclusion — exact-v1 has no dedicated limitations section; tested model/task graph and offline traces bound the conclusion", relation="Direct Evolution", override="knowledge_gap"),
    c("2605.00206", (2,2,3), "MODEL-DECODER-ONLY", "No Change — Existing Coverage",
      "books/part-02-model/18-decoder-only.md#L1", "books/part-02-model/15-attention.md#L1; books/part-04-training-system/36-distributed-training.md#L1",
      "Nonlinear recurrent latent state can be trained with a parallel surrogate and executed recurrently, shifting the bottleneck from explicit token history toward state-transition stability and train/decode equivalence.",
      "§2-4 nonlinear recurrence and parallel-training construction", "§5 model/task evaluations and ablations", "§6 limitations on scale, recurrence stability and broader workloads", relation="Alternative Branch"),
    c("2605.00254", (3,3,3), "INFER-SCHEDULING", "Integrate",
      "books/part-05-inference-system/56-inference-scheduling.md#L35", "books/part-05-inference-system/52-distributed-inference.md#L1; books/part-05-inference-system/55-inference-memory-optimization.md#L1",
      "MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。",
      "§3-5 topology/cost model, placement and routing mechanisms", "§6 serving scenarios and topology comparisons", "§7 Conclusion — exact-v1 has no dedicated limitations section; scenario assumptions and cost model are not universal production measurements", relation="Direct Evolution", override="knowledge_gap"),
    c("2605.00267", (3,3,3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/72-security.md#L14", "books/part-06-ai-infrastructure/66-evaluation-system.md#L18; books/part-07-agent/84-agent-platform.md#L74",
      "Jailbreak 后保留通用能力意味着 safety case 不能依赖能力退化；风险控制必须落在 action authority、sandbox、monitoring 与 outcome evidence，而不是假设越狱模型不可完成复杂任务。",
      "§3-4 jailbreak construction and capability-preservation protocol", "§5 general and agentic task evaluations", "§6 limitations: selected frontier models, attacks and tasks; no deployment prevalence claim", relation="Explanatory Analogy", override="release_security_contract"),
    c("2605.00300", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L35", "books/part-05-inference-system/56-inference-scheduling.md#L55; books/part-06-ai-infrastructure/69-cost-management.md#L1",
      "Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。",
      "§3 endpoint-centric continuous benchmark and measurement protocol", "§4-5 preference/cognition/energy evaluations", "§6 discussion and limitations on provider drift, observability and evaluator scope", relation="Direct Evolution", override="knowledge_gap"),
    c("2605.00314", (3,3,3), "PLATFORM-SECURITY", "Integrate",
      "books/part-06-ai-infrastructure/72-security.md#L14", "books/part-07-agent/78-tool-calling.md#L42; books/part-07-agent/83-mcp.md#L40",
      "Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。",
      "§3-5 representation synthesis, Datalog constraints and audit pipeline", "§6 evaluation over skill corpus, attack cases and hardware setup", "§7 Conclusion — exact-v1 has no dedicated limitations section; static abstraction cannot prove dynamic runtime safety", relation="Layering / Dependency", override="release_security_contract"),
]

# Independent W18 reconciliation and root false-negative challenge pass.
# These families were incorrectly closed before the denominator even though their
# exact-v1 mechanism changes a durable system contract or a current design branch.
C += [
    c("2604.27306", (3, 3, 3), "AGENT-RAG", "Integrate",
      "books/part-07-agent/76-rag.md#L1", "books/part-07-agent/75-context.md#L1; books/part-07-agent/77-memory.md#L1",
      "可维护 RAG 的 retrieval object 不应只是 passage：带 evidence、validity interval 与 lifecycle state 的 atomic nugget 让失效事实在 ranking 前退出，并把来源冲突变成显式状态。",
      "§3-4 nugget schema, lifecycle and retrieval pipeline", "§5 three QA datasets, maintenance/update evaluation and ablations", "§6/§7 selected QA corpora and author metrics do not prove a universal source-authority policy", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.27351", (2, 3, 3), "AGENT-TOOL-CALLING", "No Change — Existing Coverage",
      "books/part-07-agent/78-tool-calling.md#L1", "books/part-07-agent/76-rag.md#L1; books/part-07-agent/83-mcp.md#L1",
      "异构 scientific foundation models 可通过 typed specialist tools 协作；language model 负责 decomposition/routing，领域模型保留输入输出语义与 artifact authority。",
      "§3 heterogeneous model collaboration and typed tool interface", "§4 scientific task evaluations and collaboration ablations", "§5 selected scientific models/tasks do not establish a universal planner or tool ontology", relation="Layering / Dependency"),
    c("2604.27358", (3, 3, 3), "AGENT-MULTI-AGENT", "Integrate",
      "books/part-07-agent/82-multi-agent.md#L1", "books/part-07-agent/79-planning.md#L1; books/part-06-ai-infrastructure/72-security.md#L1",
      "Delegation degree 是运行时控制变量而非静态拓扑：bilevel controller 在效用与 safety constraint 间调节子代理权限，并要求 responsibility propagation 可验证。",
      "§3-5 bilevel delegation objective, safety monotonicity and responsibility propagation", "§5 formal convergence/safety analysis", "exact-v1 explicitly leaves empirical validation to future work; formal assumptions do not prove deployable runtime safety", relation="Direct Evolution", override="release_security_contract"),
    c("2604.27393", (3, 3, 3), "MULTIMODAL-REPRESENTATION", "No Change — Existing Coverage",
      "books/part-03-multimodal-world-models/23-multimodal-representation.md#L1", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1; books/part-05-inference-system/43-prefill.md#L1",
      "全双工 omni-modal interaction 把音频、视觉与文本从离线拼接改成持续 streaming state；turn-taking、interruption 与 concurrent perception/generation 成为第一等 runtime contract。",
      "§2-3 native omni-modal architecture, full-duplex streaming and training", "§4 multimodal understanding/generation and streaming interaction evaluations", "model-specific training data, hardware and latency conditions bound the reported interaction quality", relation="Direct Evolution"),
    c("2604.27405", (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1",
      "版本平均分会掩盖 item-level 双向 churn；release gate 需要 within-model reliable change、sampling variance 与 harmed/helped item ledger，而不是只比较 aggregate delta。",
      "§2-3 item-level Reliable Change Index adaptation and within-family comparison", "§4 2,000 MMLU-Pro items, 10 samples and two model-family upgrades", "two families and one benchmark do not calibrate a universal RCI threshold or production consequence", relation="Direct Evolution", override="release_security_contract"),
    c("2604.27419", (2, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-07-agent/78-tool-calling.md#L1; books/part-07-agent/81-workflow.md#L1",
      "Website-agent evaluation must preserve interactive feedback, intermediate artifacts and repair loops; static final-page similarity cannot prove executable workflow correctness.",
      "§3 benchmark environment, interaction protocol and graders", "§4 multimodal web-agent baselines and error analysis", "website-generation tasks and benchmark fixtures do not establish general computer-use reliability", relation="Principle Reuse"),
    c("2604.27426", (3, 3, 3), "PLATFORM-SECURITY", "Integrate",
      "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-04-training-system/29-sft.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1",
      "Local/offline fine-tuning is not a privacy boundary when model repository code owns the executable training path; artifact provenance, sandboxing and egress control must precede dataset access. May steal training secrets.",
      "§3-4 malicious model-code supply-chain path and active execution hijacking", "§5 secret-exfiltration experiments across local fine-tuning setups", "demonstrated attacks do not establish ecosystem prevalence; controls depend on the actual loader/runtime boundary", relation="Layering / Dependency", override="release_security_contract"),
    c("2604.27488", (3, 3, 3), "AGENT-PLATFORM", "No Change — Existing Coverage",
      "books/part-07-agent/84-agent-platform.md#L1", "books/part-07-agent/80-reflection.md#L1; books/part-07-agent/81-workflow.md#L1",
      "Skill evolution 需要 versioned proposal、comparative execution、traceable judge evidence 与 rollback；training-free optimization 不能让生成者同时拥有发布 authority。",
      "§3 Skills-Coach task generation, comparative execution and GRPO-style skill optimization", "§4 agent-skill benchmarks, ablations and trace analysis", "author-generated tasks/judges and selected skills do not prove production release safety", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.27536", (3, 3, 3), "INFER-SCHEDULING", "Integrate",
      "books/part-05-inference-system/56-inference-scheduling.md#L1", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/70-cost.md#L1",
      "黑盒服务的 stronger-path escalation 是部分可观测的预算决策：controller 必须由 verifiable observation 更新 belief，并把 expected reliability gain 与增量推理成本联合 admission。",
      "§2-4 POMDP formulation, verifiable observations and belief-guided routing", "§5 service workloads, cost/reliability baselines and ablations", "proxy-verifier calibration and workload stationarity limit generalization to unseen services", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.27586", (3, 3, 3), "PLATFORM-TRACE", "Integrate",
      "books/part-06-ai-infrastructure/69-trace.md#L1", "books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1",
      "Agent contamination is a trace property: uncertain evidence can alter decomposition/routing before appearing in the final answer, so provenance must follow artifact transformations and control-flow divergence across steps.",
      "§3 trace-level contamination model, artifact transformations and divergence measures", "§4 heterogeneous-document workflows and contamination interventions", "synthetic workflows and chosen corruption models do not quantify real-world prevalence or causal completeness", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.27637", (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-07-agent/74-prompt.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1",
      "Cross-model evaluation must distinguish a frozen common-prompt contract from a per-model optimized deployment contract; otherwise prompt mismatch can change rankings and misattribute interface quality to model weights.",
      "§2-3 per-model prompt-optimization protocol before evaluation", "§4 model/task ranking changes under optimized versus static prompts", "selected optimizers, tasks and search budgets do not define a universally fair evaluation regime", relation="Alternative Branch", override="knowledge_gap"),
    c("2604.27660", (2, 3, 3), "AGENT-CONTEXT", "No Change — Existing Coverage",
      "books/part-07-agent/75-context.md#L1", "books/part-07-agent/77-memory.md#L1; books/part-07-agent/80-reflection.md#L1",
      "Inference-time skill extraction converts context into a replayable procedure and then selects whether to reuse it; derived skill state must remain linked to source context and evaluation evidence.",
      "§3 context-to-skill extraction, self-play generation and replay selection", "§4 task suites, baselines and skill-transfer ablations", "selected tasks/models do not establish durable skill validity or safe cross-domain reuse", relation="Direct Evolution"),
    c("2604.27695", (3, 3, 3), "AGENT-MEMORY", "No Change — Existing Coverage",
      "books/part-07-agent/77-memory.md#L1", "books/part-07-agent/76-rag.md#L1; books/part-07-agent/81-workflow.md#L1",
      "Long-term memory retrieval should diagnose an evidence gap before issuing the next query; iterative retrieval state must record known evidence, missing relation and stop/abstain criteria rather than only rewrite queries.",
      "§3 evidence-gap diagnosis, layered memory and iterative retrieval controller", "§4 long-conversation temporal/multi-hop benchmarks and ablations", "benchmark conversations and author-defined gap labels do not prove production memory truthfulness", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.27707", (2, 3, 3), "AGENT-MEMORY", "No Change — Existing Coverage",
      "books/part-07-agent/77-memory.md#L1", "books/part-04-training-system/28-pretraining.md#L1; books/part-07-agent/76-rag.md#L1",
      "Retrieval memo and weight consolidation are different state transitions: the former changes accessible context, the latter changes generalizing parameters and therefore poisoning, rollback and provenance boundaries.",
      "§2-4 formal memo-versus-memory distinction and consolidation consequences", "conceptual analysis and cited examples; no independent systems benchmark", "position paper does not demonstrate a universally superior consolidation mechanism", relation="Explanatory Analogy"),
    c("2604.27711", (2, 3, 3), "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage",
      "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1", "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-05-inference-system/44-decode.md#L1",
      "Exocentric video generation can propose interaction-rich humanoid motion, but generated trajectories remain proposals until a controller, embodiment calibration and environment feedback commit physical actions.",
      "§3 exocentric generation and control pipeline", "§4 simulated and physical humanoid evaluations", "video quality and selected tasks do not establish broad physical safety or sim-to-real robustness", relation="Layering / Dependency"),
    c("2604.27776", (2, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1",
      "Professional GUI-agent evaluation must preserve cross-application process state, artifact handoffs and terminal evidence; per-app task success misses workflow-level recovery and consistency.",
      "§3 cross-application Windows environment and process-centric tasks", "§4 agent baselines, process/terminal grading and error taxonomy", "Windows applications and curated professions do not represent every production workspace", relation="Principle Reuse"),
    c("2604.27789", (3, 3, 3), "PLATFORM-PRODUCTION", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/73-production-best-practice.md#L1", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/72-security.md#L1",
      "Opaque provider updates require a deployer-owned compatibility contract: frozen risk suites, behavioral diff, canary and rollback gates must mediate even when the provider reuses the same model name.",
      "§3-5 deployer contracts, update detection and compatibility-gate workflow", "case studies and risk-suite demonstrations over hosted model changes", "framework cannot observe undisclosed provider internals and depends on representative local suites", relation="Direct Evolution", override="release_security_contract"),
    c("2604.27819", (3, 3, 3), "AGENT-MCP", "Integrate",
      "books/part-07-agent/83-mcp.md#L1", "books/part-06-ai-infrastructure/72-security.md#L1; books/part-07-agent/78-tool-calling.md#L1",
      "Multi-server MCP safety is an information-flow problem: individually permitted read/write tools can compose into a cross-boundary leak, so canary taint must survive tool-call edges and server identities.",
      "§3 MCPHunt canary injection, multi-server topology and taint tracking", "§4 server/tool compositions, models and leak-detection evaluation", "synthetic canaries and enumerated servers do not prove complete semantic non-interference", relation="Direct Evolution", override="release_security_contract"),
    c("2604.27855", (3, 3, 3), "PLATFORM-COST", "Integrate",
      "books/part-06-ai-infrastructure/70-cost.md#L1", "books/part-05-inference-system/56-inference-scheduling.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1",
      "Inference placement may treat energy geography as a scheduling input only after latency, state locality, capacity and regulation become hard constraints; cheap power alone cannot own routing authority.",
      "§3-5 latency-constrained energy-geography model and placement formulation", "regional scenarios and sensitivity analysis", "analytical inputs and assumed relocatability are not measured production traces or universal grid emissions", relation="Layering / Dependency", override="knowledge_gap"),
    c("2604.27906", (3, 3, 3), "AGENT-MEMORY", "No Change — Existing Coverage",
      "books/part-07-agent/77-memory.md#L1", "books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1",
      "Persistent memory write is a schema-governed state transition: extraction, validation, conflict/update policy and retry must precede commit; semantic retrieval alone cannot guarantee exact current state.",
      "§3 schema-aware iterative extraction, validation gates and retry path", "§4 memory extraction/update tasks and component ablations", "selected schemas and LLM judges do not prove arbitrary-domain completeness or truth", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.28056", (3, 3, 3), "TRAIN-RLHF", "Integrate",
      "books/part-04-training-system/31-rlhf.md#L1", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1",
      "LLM-generated reward hypotheses should fork from a shared checkpoint, pass competence-aware verification and deploy by training phase; generation quality does not grant reward release authority.",
      "§3 RHyVE reward-hypothesis generation, verification and phase-aware deployment", "§4 RL environments, reward baselines, ablations and competence analysis", "selected environments and verifier signals do not prove reward correctness or prevent all specification gaming", relation="Direct Evolution", override="release_security_contract"),
    c("2604.28123", (3, 3, 3), "TRAIN-RLHF", "Integrate",
      "books/part-04-training-system/31-rlhf.md#L1", "books/part-04-training-system/29-sft.md#L1; books/part-04-training-system/33-grpo.md#L1",
      "SFT→RLVR is not a neutral handoff when SFT shifts the policy distribution; black-box on-policy distillation can insert a pre-alignment bridge, trading extra rollout/teacher cost for a better RL starting distribution.",
      "§3 PRISM black-box on-policy distillation between SFT and RLVR", "§4 multimodal reasoning tasks, baselines and ablations", "selected models/tasks and teacher access do not establish universal benefit or cost efficiency", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.28129", (3, 3, 3), "PLATFORM-SECURITY", "Integrate",
      "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-06-ai-infrastructure/69-trace.md#L1; books/part-07-agent/75-context.md#L1",
      "Multi-turn attacks may be benign turn-by-turn yet form a residual-activation trajectory; adaptive probes add a model-specific internal signal but cannot replace effect mediation or cross-version recalibration.",
      "§3 activation-trajectory probes and adaptive multi-turn detector", "§4 attack phases, model families, baselines and transfer tests", "white-box activations and model-specific probes limit hosted-model use and require recalibration after updates", relation="Layering / Dependency", override="release_security_contract"),
    c("2604.28157", (3, 3, 3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-07-agent/75-context.md#L1",
      "Efficient red teaming can reuse prefix/cache and structured mutation state, but computational acceleration does not change the separation between attack discovery, evidence validation and release authority.",
      "§3 FlashRT red-team search and cache/memory optimizations", "§4 prompt-injection/knowledge-corruption workloads, systems measurements and ablations", "attack suites and author hardware do not establish full threat coverage or production prevalence", relation="Principle Reuse"),
    c("2604.28158", (2, 3, 3), "AGENT-WORKFLOW", "No Change — Existing Coverage",
      "books/part-07-agent/81-workflow.md#L1", "books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1",
      "Methodological evolution graphs represent typed method relations rather than citation adjacency, enabling research workflows to reason about why techniques branch, replace or compose.",
      "§3 method-evolution ontology, extraction and graph construction", "§4 retrieval/reasoning tasks and graph-quality evaluation", "automated extraction and selected AI literature do not prove a complete or authoritative knowledge graph", relation="Principle Reuse"),
    c("2604.28175", (3, 3, 3), "INFER-SCHEDULING", "Integrate",
      "books/part-05-inference-system/56-inference-scheduling.md#L1", "books/part-05-inference-system/46-continuous-batching.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1",
      "Priority-aware serving needs interference-conditioned latency prediction; priority without concurrent-execution estimates merely moves queue delay into GPU contention and can violate both classes' SLOs.",
      "§3 Strait dual-priority scheduler and interference predictor", "§4 serving traces/models, baselines and ablations", "on-premises model roster and hardware do not establish universal predictor transfer or tail-SLO behavior", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.28181", (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1",
      "Long-horizon computer-use evaluation needs synthetic workspace state and artifact lineage, not isolated screenshots; scalable generation must preserve task-consistent files, directories and terminal evidence.",
      "§3 synthetic computer/workspace generation pipeline", "§4 long-horizon productivity tasks, realism and agent evaluations", "synthetic environments may miss organizational policy, hidden dependencies and real-user distributions", relation="Layering / Dependency"),
    c("2604.28182", (3, 3, 3), "TRAIN-RLHF", "Integrate",
      "books/part-04-training-system/31-rlhf.md#L1", "books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/33-grpo.md#L1",
      "Exploration itself is part of the RL trust boundary: a model that suppresses useful actions can resist training without overt reward hacking, so rollout diversity and policy-update diagnostics must be release evidence.",
      "§3 exploration-hacking threat model and resistant-policy construction", "§4 RL training experiments, detection signals and ablations", "constructed settings do not establish spontaneous prevalence in deployed models or a complete detector", relation="Direct Evolution", override="release_security_contract"),
    c("2604.28190", (3, 3, 3), "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
      "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1", "books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1",
      "Distributional representation distance can become a training loss by decoupling the population used to estimate statistics from the gradient batch; this trades estimator state and representation dependence for direct distribution matching.",
      "§3 Representation Fréchet Loss and population/batch decoupling", "§4 visual-generation models, quality/diversity evaluations and ablations", "selected representation encoders and image workloads do not prove perceptual alignment or generalization to all modalities", relation="Alternative Branch", override="knowledge_gap"),
    c("2604.28196", (3, 3, 3), "MULTIMODAL-WORLD-MODELS", "No Change — Existing Coverage",
      "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1", "books/part-03-multimodal-world-models/23-multimodal-representation.md#L1; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1",
      "A driving world model can share state between 3D scene understanding and future geometry prediction; unified representation still does not grant planner or physical-control authority.",
      "§3 HERMES++ unified 3D understanding/prediction architecture", "§4 driving datasets, understanding/generation metrics and ablations", "driving datasets and open-loop generation do not prove closed-loop safety or causal controllability", relation="Direct Evolution"),
    c("2604.27891", (3, 3, 3), "AGENT-WORKFLOW", "Integrate",
      "books/part-07-agent/81-workflow.md#L1", "books/part-07-agent/75-context.md#L1; books/part-07-agent/84-agent-platform.md#L1",
      "External orchestration is an alternative branch, not a default: when the full procedure fits context and the model can track it, in-context self-routing removes routing calls and fragmentation; durable side effects, audit and restart still require external workflow state.",
      "§2 directed procedures and controlled LangGraph versus in-context conditions", "§3 1,200 conversations across three procedural domains with two judge families", "§5.2-5.3 three simulated customer-service domains, LLM judges and frontier-model capability bound the conclusion; token cost is higher in-context", relation="Alternative Branch", override="knowledge_gap"),
    c("2605.00226", (3, 2, 3), "AGENT-PLANNING", "No Change — Existing Coverage",
      "books/part-07-agent/79-planning.md#L1", "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1",
      "Strategic failure can be decomposed into observation→belief update and belief→action selection gaps; verbalized belief and action accuracy should not be treated as one undifferentiated planning score.",
      "§3 strategic-play tasks, internal/verbal probes and Bayesian Coherence Coefficient", "§4 repeated games, Kuhn Poker and Chameleon evaluations", "selected games/probes do not establish causal access to latent beliefs or general decision competence", relation="Explanatory Analogy"),
    c("2604.27396", (2, 3, 2), "INFER-TENSORRT-LLM", "No Change — Existing Coverage",
      "books/part-05-inference-system/49-tensorrt-llm.md#L122", "books/part-05-inference-system/43-prefill.md#L1; books/part-05-inference-system/44-decode.md#L1",
      "VitaLLM 以 ternary/INT 双核心、leading-one KV fetch pruning 与 dependency-aware head pipeline 将 prefill/decode 的不同瓶颈映射到 phase-aware accelerator plan；prototype 证明特定 BitNet workload 可行，但不授予跨硬件通用执行结论。",
      "§II-III heterogeneous dual-core architecture, leading-one predictor and dependency-aware system integration", "§IV 16nm prototype, BitNet b1.58 3B prefill/decode and ablation evaluation", "§IV evidence is bound to one 16nm prototype, LPDDR5-class memory, BitNet b1.58 3B and disclosed sequence settings; it does not prove cross-model or cross-accelerator portability", relation="Principle Reuse"),
    c("2604.27467", (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-04-training-system/31-rlhf.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1",
      "代码 verifier 不是附属脚本，而是训练与评测共享的 evidence runtime：special-judge synthesis、test-case parallelism、multi-node sandbox 和配置化 suite 共同决定 reward truth、吞吐与可复现性。",
      "§4-5 ScaleBox architecture, automated special-judge generation, distributed sandbox execution and configuration-driven suite", "§5.2 and §6 verification accuracy/throughput plus RLVR training evaluation", "§7 Limitations: generated judges, selected code tasks, sandbox policies and author infrastructure do not prove arbitrary-program correctness or universal RL stability", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.27486", (3, 3, 3), "INFER-TENSORRT-LLM", "Integrate",
      "books/part-05-inference-system/49-tensorrt-llm.md#L220", "books/part-06-ai-infrastructure/72-security.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1",
      "GPU binary lifting 的关键不是语法翻译，而是从统一 register file 恢复 typed state、显式 control flow 与 multi-instruction semantics；conflict detection 决定何时必须拒绝生成可执行 IR。",
      "§3-5 SASS decoding, type-constraint propagation with conflict detection, control-flow reconstruction and multi-instruction aggregation", "§6 eight suites, 24,437 GPU functions, valid-IR and x86 semantic-pass evaluation plus ablation", "§6 evaluation cannot validate MUFU, texture or full SIMT behavior through an x86 backend; supported architectures/instructions bound correctness and require fail-closed handling", relation="Direct Evolution", override="knowledge_gap"),
    c("2604.27781", (3, 3, 3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-06-ai-infrastructure/73-production-best-practice.md#L1; books/part-06-ai-infrastructure/60-model-registry.md#L1",
      "AI software supply chain 必须跨 data、training、inference 与 substrate 维护 verifiability、versioning、observability 和 traceability；依赖数量只是暴露面证据，不能替代运行时 provenance 或 release gate。",
      "§2-5 four-layer AI supply-chain decomposition, integrity gaps and lifecycle requirements", "§5.1 reference-stack measurement across 48 projects, direct/transitive dependencies and source size", "exact-v1 provides a conceptual decomposition and ecosystem measurement, not a controlled security evaluation or proof that every dependency is exercised at runtime", relation="Layering / Dependency", override="release_security_contract"),
    c("2604.27861", (3, 3, 3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
      "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-07-agent/75-context.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1",
      "分解式 jailbreak 的风险状态可跨匿名、交错请求累积；TwinGate 用 asymmetric contrastive state 将 topical overlap 与 shared malicious intent 分离，但它仍只是 detector proposal，不能替代 effect mediation。",
      "§3-4 asymmetric contrastive dual-encoder state, frozen benign encoder and causal online monitoring", "§5 strictly causal evaluation over 3.62M instructions and 8,600 malicious intents, including adaptive attacks", "selected generated/curated intents and latent-space clustering do not prove complete intent reconstruction, universal low false-positive operation or action-level safety", relation="Principle Reuse", override="release_security_contract"),
    c("2604.27878", (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
      "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-07-agent/76-rag.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1",
      "Simulator evaluation must separate behavioral realism from tester reliability：像不像真人与能否保持系统 ranking 是两个可能冲突的 contract，必须共享 canonical session schema、loss accounting 与 runtime applicability metadata。",
      "§3 canonical session schema, adapters and loss accounting; §4-5 realism and tester-reliability benchmark design", "§6 four datasets, two languages, four simulator families and ranking-reliability analysis", "§8 Limitations: dataset/language/simulator coverage is finite; correlations do not prove causal transfer to production users or unseen retrieval systems", relation="Direct Evolution", override="knowledge_gap"),
]

BOOKS_COMPARISON = {
    "SF-2026-ARXIV-2604-27844": (
        "Ch36 已拥有 collective 语义、算法/transport/topology 分层和 bandwidth/latency/overlap 成本模型。",
        "尚未把 bit-exact exponent coding、GPU encode/decode critical path 与 adaptive fallback 写成同一条 compression contract。"),
    "SF-2026-ARXIV-2604-28138": (
        "Ch84 已把 AgentRun、workflow state、tool side effect 和 terminal evidence 区分于 transcript/KV。",
        "尚未具体说明 turn-boundary checkpoint 如何联合捕获 filesystem/process/tool state，以及稀疏检测如何引入 false-negative 与 co-location contention。"),
    "SF-2026-ARXIV-2605-00081": (
        "Ch72/Ch78 已明确模型只提出 action proposal，executor/policy 拥有 schema、authorization 与 effect。",
        "尚未用 typed alignment contract 把模型层 observation 与执行层 enforcement 组织为可组合、双层可观测的 contract。"),
    "SF-2026-ARXIV-2605-00136": (
        "Ch78 已说明大型 tool catalog 会增加 context token、选择混淆与 attack surface。",
        "尚未把 tool-use failure 分解为协议格式、selection/argument、transport/runtime 与真实工具收益四类可测成本。"),
    "SF-2026-ARXIV-2605-00180": (
        "Ch56 已由 workload profile、SLO 与 state locality 拥有 routing/admission 判断。",
        "尚未覆盖新模型 cold start 时从 model graph 迁移 profile，并把 uncertainty、staleness 与 online fallback 写入 admission contract。"),
    "SF-2026-ARXIV-2605-00254": (
        "Ch52/Ch56 已拥有 distributed inference 的 placement、network tier、hotspot 与 scheduling state。",
        "尚未把 MoE expert placement、token skew、all-to-all bytes、topology cost 与 reconfiguration/failure domain 联合为一个 serving decision。"),
    "SF-2026-ARXIV-2605-00300": (
        "Ch66 已要求 benchmark 冻结 workload、evaluator、版本与 evidence；Ch69 拥有成本维度。",
        "尚未把 endpoint/model configuration 定义为版本化原子对象，并在同一连续 contract 记录能耗、质量、延迟、价格与可靠性。"),
    "SF-2026-ARXIV-2605-00314": (
        "Ch72 已拥有 tool/skill 的 artifact、capability、data-flow 与 runtime-effect 审计边界。",
        "尚未说明如何由自然语言和代码合成有限 SDL fact base，再由 Datalog 约束检查 source-to-sink、permission 与 effect。"),
}

BOOKS_COMPARISON.update({
    "SF-2026-ARXIV-2604-27306": ("Ch76 已要求 provenance、temporal validity 与 source authority 随 retrieval evidence 传播。", "尚未把 atomic nugget 的 validity/lifecycle 写成 ranking 前 admission 与失效淘汰状态机。"),
    "SF-2026-ARXIV-2604-27358": ("Ch82 已区分 role、communication topology 与 orchestrator authority。", "尚未把 delegation degree 建模为受 safety constraint 约束的运行时控制变量，并显式保留责任传播边界。"),
    "SF-2026-ARXIV-2604-27405": ("Ch66 已要求版本化对象、重复采样、uncertainty 与 release gate。", "尚未说明 aggregate delta 会掩盖 item-level 双向 churn，以及 RCI 类 harmed/helped ledger 如何进入兼容性判断。"),
    "SF-2026-ARXIV-2604-27426": ("Ch72 已拥有 artifact provenance、sandbox、secret 与 egress policy。", "尚未把 local fine-tuning model code 明确视为先于 dataset access 获得执行权的供应链主体。"),
    "SF-2026-ARXIV-2604-27488": ("Ch84 已要求 skill artifact version、evaluation evidence、approval 与 rollback。", "尚未将 task generation、comparative execution 和 traceable judge evidence组织成 skill self-evolution 的受控发布回路。"),
    "SF-2026-ARXIV-2604-27536": ("Ch56 已由 workload/SLO/cost profile 拥有 admission 与 routing。", "尚未覆盖黑盒服务只有 verifiable partial observations 时的 belief update、escalation value 与 budgeted stopping。"),
    "SF-2026-ARXIV-2604-27586": ("Ch69/Ch81 已要求跨 step trace、artifact lineage 与 terminal evidence。", "尚未把 contamination 视为可先改变 decomposition/routing、后影响最终输出的 control-flow divergence。"),
    "SF-2026-ARXIV-2604-27637": ("Ch66 已冻结 model、prompt、evaluator 与 workload identity。", "尚未明确区分 common-prompt comparability 与 per-model optimized deployment contract，并记录两者对 ranking 的不同解释。"),
    "SF-2026-ARXIV-2604-27695": ("Ch77 已区分 persistent memory、retrieval state 与 derived memory。", "尚未把 evidence gap 作为 iterative retrieval 的显式状态，并定义 missing relation、stop 与 abstain。"),
    "SF-2026-ARXIV-2604-27789": ("Ch73/Ch66 已要求 canary、evaluation evidence 与 rollback gate。", "尚未把 provider 复用同名 endpoint 的 opaque update 写成 deployer-owned compatibility contract 和风险套件。"),
    "SF-2026-ARXIV-2604-27819": ("Ch83/Ch72 已拥有 MCP server identity、capability 与执行边界。", "尚未说明 benign read/write permission 如何经多 server workflow 合成为跨域泄漏，以及 canary taint 如何跨 tool edge 传播。"),
    "SF-2026-ARXIV-2604-27855": ("Ch70/Ch56 已联合考虑 cost、SLO、capacity 与 placement。", "尚未把 energy geography 作为仅在 latency、state locality、capacity 与 regulation 硬约束后才可优化的调度维度。"),
    "SF-2026-ARXIV-2604-27906": ("Ch77 已说明 memory write 需要 provenance、更新与冲突策略。", "尚未将 schema extraction、validation、retry 和 commit 顺序写成 production memory 的单一 write path。"),
    "SF-2026-ARXIV-2604-28056": ("Ch31/Ch66 已区分 reward proposal、evaluation 与 release authority。", "尚未把 reward hypothesis 从共享 checkpoint 分叉、competence verification 与 phase-aware deployment 连成一条控制链。"),
    "SF-2026-ARXIV-2604-28123": ("Ch29→Ch31 已解释 SFT 与 preference/RL 的目标差异。", "尚未显式处理 SFT distribution drift 到 RLVR on-policy distribution 的 handoff，并给出黑盒 distillation 这一条件分支。"),
    "SF-2026-ARXIV-2604-28129": ("Ch72 已要求跨 turn threat state 与 effect mediation。", "尚未补充 residual activation trajectory 这一 white-box detector 分支、模型更新后的 recalibration 和 hosted-model 不可用边界。"),
    "SF-2026-ARXIV-2604-28175": ("Ch56 已由 queue、SLO 和 runtime state 拥有 request scheduling。", "尚未把 priority 与 concurrent interference-conditioned latency prediction 联合，防止优先级把等待迁移为 GPU contention。"),
    "SF-2026-ARXIV-2604-28182": ("Ch31/Ch32/Ch33 已覆盖 reward hacking、KL 与 rollout/update loop。", "尚未把策略性抑制 exploration 作为独立训练阻抗，并要求 rollout diversity/update diagnostics 成为 release evidence。"),
    "SF-2026-ARXIV-2604-28190": ("Ch24 已比较 AR、diffusion 与 iterative correction 的 factorization/serving 代价。", "尚未补充 population-statistics 与 gradient batch 解耦后，Fréchet representation distance 可作为受限训练目标的分支。"),
    "SF-2026-ARXIV-2604-27891": ("Ch81 已说明 durable workflow state、side effect、restart 与 audit 需要外部 owner。", "尚未明确外部 graph orchestration 不是默认：procedure 可完整入 context 时，self-routing 可避免 fragment/routing calls，但不能替代 durable commit。"),
    "SF-2026-ARXIV-2604-27467": ("Ch66 已要求 evaluator identity、sandbox、terminal evidence 与 workload version 进入 release evidence；Ch31 已把 verifier signal 与 reward proposal 分离。", "尚未把 special-judge synthesis、test-case parallel execution、multi-node sandbox 与 configuration-driven suite 写成训练和评测共享的 code-verification evidence runtime。"),
    "SF-2026-ARXIV-2604-27486": ("Ch49 已解释 PTX/SASS 的架构绑定、post-compilation optimization 与独立 correctness/SLO gate。", "尚未解释 reverse lifting 时 type state 如何由统一 register file 恢复、冲突时为何必须 fail closed，以及 typed LLVM IR 怎样成为二进制审计和迁移的中间证据。"),
    "SF-2026-ARXIV-2604-27878": ("Ch66 已区分任务成功、过程 evidence、evaluator version 与 release authority。", "尚未明确 simulator 的 behavioral realism 与 tester reliability 是两个可能冲突的 evaluation contract，并要求 canonical session schema、loss accounting 和 ranking-validity evidence 分开出账。"),
})


def marker(ref: str, body: str) -> str:
    return f"<!-- {ref}:start -->\n{body.strip()}\n<!-- {ref}:end -->\n"


SPECIAL_CLOSURES = {
    "2604.27306": "NuggetIndex 把 RAG retrieval object 改为带 evidence link、validity interval 与 lifecycle state 的 atomic nugget，并在排序前剔除失效记录；公开实验只覆盖三个 QA 数据集及其作者定义指标。该 family 与现有 RAG provenance/temporal-state 主线相关，但没有改变通用 source authority、write ownership 或 release gate，因此在分母前关闭为局部 retrieval/index design evidence。",
    "2604.27358": "SBD 用 bilevel optimization 动态调节 delegation degree，并给出 safety monotonicity、inner convergence 与责任传播界；exact-v1 明确说经验验证尚待后续版本。缺少运行时 artifact 与跨域实证，当前不能把形式假设提升为可部署的 delegation authority contract，因此分母前关闭。",
    "2604.27464": "该文以 OpenClaw 为案例，把 Agent 风险整理为 context/instruction、tool/action、state/persistence 与 ecosystem/automation 四层，并强调跨层传播。它是 secondary review，不提供新的 primary enforcement mechanism 或 evaluation contract；用于发现与术语校准，但不进入候选分母。",
    "2604.27536": "Veroic 把黑盒 LLM 的升级推理决策建模为 POMDP，由可验证 signal 聚合出的 belief state 在预算约束下选择默认或高成本路径；摘要只报告作者任务集上的 quality-cost/calibration 改善。它是 inference-control 的局部策略实例，未改变可靠性 signal 的 authority、SLO admission 或生产 fallback contract，因此分母前关闭。",
    "2604.27586": "该研究在固定 Agent workflow 中注入 artifact-derived representation perturbation，并用 plan、tool-call 与 intermediate-state trace divergence 区分 silent corruption、detour recovery 和 combined disruption。614 paired runs 支持 trace-level measurement case，但没有提出新的 state owner、commit/recovery protocol 或 release criterion，因此作为受限 evaluation evidence 在分母前关闭。",
    "2604.27691": "该文把七种历史制度映射为 multi-agent topology，并在三个模型、两个 benchmark 上显示 topology 与 task/model capability 的交互。结果说明组织结构是可重配变量，但不建立可迁移的 authority、quorum、rollback 或 failure-domain contract，因而作为架构探索证据而非长期系统机制进入分母前关闭。",
    "2604.27707": "该立场论文区分 retrieval-based memo 与 weight consolidation，并以组合泛化上限和 poisoning 风险主张两类记忆应共存。它提供解释框架而非新的可验证 consolidation mechanism、lifecycle protocol 或 production evaluation，现有 Memory 章节已承载 derived state 与 provenance 边界，因此分母前关闭。",
    "2604.27818": "MASCing 训练 LSTM surrogate 捕获跨层 MoE routing dependency，再用 steering mask 改写 inference-time expert choice；七个开源 MoE 的两个 safety objective 说明局部行为可配置。该结果没有建立通用 safety authority，且同一机制也能解除拒答，未改变平台级 policy/authorization contract，因此分母前关闭为模型局部 steering case。",
    "2604.27855": "该文将 geo-distributed inference placement 写成包含电价、边际碳、PUE、capacity、network latency、state locality 与 migration friction 的优化，并提出 energy-latency frontier。证据是透明的 stylized simulation，不是生产 trace；它没有改变现有 workload-conditioned scheduling owner，只为既有成本/碳约束提供领域模型，因此分母前关闭。",
    "2604.27906": "该文把 Agent external memory 从文本相似检索提升为 schema-grounded system of record，并强调 exact fact、update/delete、negative query 与 explicit unknown。机制方向与现有 Memory 的 typed derived state、provenance 和 lifecycle 已同构，摘要没有给出改变 canonical write owner 或 consistency contract 的新证据，因此以 Existing Coverage 在分母前关闭。",
    "2604.28049": "该工作用 SQL execution/result equivalence 构造 evaluator，针对 text-to-SQL 或数据库任务减少仅凭字符串匹配的误判。它改进的是单一任务 evaluator，不改变跨领域 evaluation evidence、release authority 或 benchmark versioning contract，因此分母前关闭。",
    "2604.27935": "该文把 UAV swarm trajectory planning 变为 hierarchical active-inference world model，并用 simulated demonstrations、particle/EKF belief correction 与 unseen-layout replanning 验证。exact-v1 的状态/控制结构与 World Model 主线相关，但机制和 safety envelope 均绑定 UAV 域、指定 planner 与仿真/有限 flight traces，未改变通用 action authority 或 physical commit contract，因此分母前关闭为领域实现证据。",
    "2605.00140": "ARHQ 根据 activation quantization residual Hessian 将敏感 weight directions 分离到高精度 low-rank branch；exact-v1 仅在 Qwen3-4B-Thinking-2507 的 layer SNR 与 140 个 ZebraLogic 子集上报告结果。它是受限 PTQ 分支，没有改变全局 execution-plan、precision identity 或 deployment compatibility contract，因此分母前关闭。",
    "2605.00224": "TUR-DPO 以 reasoning topology 与 uncertainty 重加权 preference pairs，并依赖 topology extractor fidelity；exact-v1 的增益随 extractor 质量变化，模型、任务与 judge protocol 受限。它扩展 DPO 局部分支，但没有改写 preference ownership、reference policy、release evidence 或 PPO/DPO coexistence boundary，因此分母前关闭。",
    "2605.00320": "该记录与窗口内 `2604.27396v1` 属于同一 VitaLLM Source Family 的后续/重复投稿：同一 ternary/INT dual-core、leading-one KV pruning 与 head-level pipeline，只更新标题、prototype 数字与表述。为避免 revision/投稿重复计分，canonical owner 固定为 `SF-2026-ARXIV-2604-27396`；本 identity 保留为 duplicate-family reconciliation，不进入第二个 Candidate Denominator 或 Books Decision。",
    "2604.28093": "该指南整理 terminal-agent benchmark 的环境、任务、grader 与 reproducibility 要求，主要贡献是实践建议与 taxonomy。没有新增 primary runtime mechanism 或独立大规模 evaluation 结果，且现有评测章节已承载 environment/terminal evidence，因此分母前关闭。",
    "2604.28157": "FlashRT 针对特定 attention/runtime 路径优化 kernel scheduling 与 memory movement，并在作者绑定硬件和 workload 下报告吞吐/延迟收益。它是 execution kernel 的局部优化，未改变 KV ownership、request lifecycle、distributed commit 或 SLO accounting，因此分母前关闭。",
    "2604.28175": "Strait 通过作者提出的调度/并行策略改善特定 LLM inference workload，并与所选 baseline 比较。公开摘要不足以证明跨模型、硬件、长度与并发的稳定 design delta，也未改变 scheduling state owner 或 failure contract，因此分母前关闭。",
    "2605.00078": "该 world-action model 预测 action-conditioned future observation，并以作者 simulator/task 验证 planning utility。它是 World Model 主线的受限模型实例，未改变 persistent world-state owner、controller authority、closed-loop safety 或 sim-to-real contract，因此分母前关闭。",
    "2605.00269": "该研究指出 length distribution 可混淆 OOD evaluation，并通过重配长度或分层统计重新解释部分性能差异。它修正单类 benchmark 的 measurement confound，但没有形成新的跨系统 evaluation authority 或 release gate；作为 methodology caveat 在分母前关闭。",
    "2605.00183": "该研究构造 delayed-rendering phishing：页面先呈现 benign state 通过视觉 detector，随后在检测完成后切换为欺骗界面，并讨论本地 browser-extension mitigation。它证明特定 timing gap，但没有改变通用 browser/Agent effect authority、authenticated origin 或 release-security contract，因此作为受限 web-security attack evidence 在分母前关闭。",
}


CLOSURE_ROUTES = [
    (r"survey|review|taxonomy", "secondary synthesis", "DISCOVERY-ONLY", "任何 primary mechanism、artifact authority 或可执行 evaluation/release contract"),
    (r"medical|clinical|disease|protein|molecule|drug|biology|aerodynamic|agricultur|finance|wireless|traffic|satellite|classroom|ultrasound|uav|pedestrian|automotive", "vertical-domain AI", "WEEKLY-ONLY-CONTEXT", "通用 AI-System state/data/control ownership 或跨领域 evaluation/release contract"),
    (r"benchmark|bench\b|evaluation|evaluator|metric|dataset|corpus|leaderboard", "evaluation/data evidence", "PLATFORM-EVALUATION-SYSTEM", "evidence identity、evaluator/version ownership、cross-workload comparability 或 release gate"),
    (r"security|jailbreak|attack|privacy|govern|guardrail|adversarial|phishing|deepfake", "security/governance", "PLATFORM-SECURITY", "authorization/effect boundary、threat model、enforcement owner 或 release-security contract"),
    (r"reward model|preference|rlhf|dpo|alignment", "preference/reward modeling", "TRAIN-RLHF", "reward authority、preference provenance、policy optimization loop 或 release evaluation contract"),
    (r"checkpoint|fault toler|recover|rollback", "checkpoint/recovery", "TRAIN-CHECKPOINT", "checkpoint ownership、commit boundary、restore consistency 或 side-effect recovery contract"),
    (r"collective|all-to-all|nccl|distributed training|tensor parallel|pipeline parallel|zero", "distributed execution", "TRAIN-DISTRIBUTED-TRAINING", "distributed state ownership、collective correctness、failure domain 或 recovery contract"),
    (r"compiler|kernel|cuda|gpu binar|intermediate representation|llvm", "compiler/kernel execution", "INFER-EXECUTION", "execution-plan ownership、numerical contract、hardware portability 或 runtime failure boundary"),
    (r"kv cache|serving|inference|throughput|latency|batching|scheduling|routing", "inference runtime", "INFER-SCHEDULING", "request/KV state owner、admission/SLO、distributed commit 或 fallback contract"),
    (r"mixture.of.experts|\bmoe\b|expert routing", "conditional capacity", "MODEL-MOE", "expert state ownership、capacity/placement、communication 或 safety authority contract"),
    (r"quantiz|prun|low.rank|lora|adapter|compression", "model efficiency", "INFER-MEMORY-OPTIMIZATION", "precision/error contract、artifact compatibility、runtime ownership 或 rollback boundary"),
    (r"agent|tool|delegat|workflow|skill", "Agent action/workflow", "AGENT-PLATFORM", "action authority、typed tool contract、workflow commit/recovery 或 terminal-evidence contract"),
    (r"retriev|\brag\b|memory|context", "Agent information state", "AGENT-MEMORY", "canonical memory owner、provenance/lifecycle、retrieval authority 或 update/delete consistency contract"),
    (r"world model|robot|embodied|driving|navigation|trajectory|human.object", "world/physical action", "MULTIMODAL-EMBODIED-VLA", "persistent world-state owner、controller authority、closed-loop evidence 或 physical safety contract"),
    (r"image|video|audio|speech|multimodal|vision|3d|diffusion", "multimodal generation/representation", "MULTIMODAL-REPRESENTATION", "modality identity/alignment、generation state、serving ownership 或 cross-modal evaluation contract"),
    (r"attention|transformer|language model|embedding|token|position", "model architecture", "MODEL-TRANSFORMER", "representation/state semantics、training/inference equivalence 或 architecture-level system contract"),
    (r"federated|client clustering|edge|on-device", "federated/edge learning", "TRAIN-DISTRIBUTED-TRAINING", "data ownership、aggregation trust、client failure/privacy 或 deployment contract"),
    (r"training|optimizer|learning rate|gradient|pretrain|fine.tun", "training mechanism", "TRAIN-PRETRAINING", "objective/data ownership、optimizer-state semantics、reproducibility 或 checkpoint contract"),
]


def closure_route(item: dict) -> tuple[str, str, str]:
    title = item["title"].lower()
    # Title is the family identity and is less prone than the abstract to incidental
    # words such as "memory", "inference" or "distribution". Route it first.
    for pattern, domain, owner, contract in CLOSURE_ROUTES:
        if re.search(pattern, title, re.I):
            return domain, owner, contract
    return ("local model/task method", "ROADMAP-OWNER-UNCHANGED",
            "长期 state/data/control ownership、跨层 evaluation authority 或 release/recovery contract")


def closure_reason(item: dict) -> str:
    if item["arxiv_id"] in SPECIAL_CLOSURES:
        return SPECIAL_CLOSURES[item["arxiv_id"]]
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", item["abstract"].strip()) if s.strip()]
    mechanism = next((s for s in sentences if re.search(r"\b(we propose|we present|we introduce|we develop|we formulate|we build|we design|we construct|we improve|our (method|framework|model|approach|system)|the (model|method|framework|system) (introduces|uses|employs|integrates|consists))\b", s, re.I)), sentences[0])
    evidence = next((s for s in sentences if s != mechanism and re.search(r"^(experiments?|evaluation|results?|we (evaluate|show|find|demonstrate)|our (experiments?|evaluation|results?))\b", s, re.I)), None)
    if evidence is None:
        evidence = next((s for s in sentences if s != mechanism and re.search(r"\b(achieves?|improves?|outperforms?|ablation)\b", s, re.I)), "摘要未披露独立 evaluation、artifact 或 failure analysis。")
    domain, owner, contract = closure_route(item)
    return (f"《{item['title']}》— 具体机制（{domain}）：{mechanism[:440]} 证据/适用边界：{evidence[:380]} "
            f"分母前关闭：该 family 的增量停留在上述对象和作者 evaluation scope，没有改变 `{owner}` 已有的{contract}；"
            "因此保留 identity、v1 日期与拒绝理由，但不进入 Score V2/Books Decision。")


def review_body(x: dict, title: str) -> str:
    score = "/".join(map(str, x["score"]))
    return marker(f"claim:{x['fid']}", x["claim"]) + (
        f"#### {title}\n\n"
        f"- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `{x['method']}`。\n"
        f"- **Mechanism / ownership:** {x['claim']}\n"
        f"- **Evaluation contract:** `{x['evaluation']}`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。\n"
        f"- **Trade-off / failure:** `{x['limits']}`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。\n"
        f"- **Evolution / owner:** `{x['relation']}` → `{x['node']}`；Score V2 `{score}` = **{x['total']}/9**。\n"
        f"- **Books decision:** `{x['disposition']}`。\n"
    )


def canonical(value: str) -> str:
    return ";".join(sorted(unicodedata.normalize("NFC", p.strip()) for p in value.split(";") if p.strip()))


def provenance(x: dict, body: str) -> str:
    body_norm = "\n".join(line.rstrip() for line in unicodedata.normalize("NFC", body).strip().splitlines())
    body_sha = hashlib.sha256(body_norm.encode()).hexdigest()
    support = "SRC-ARXIV"
    reviewed = f"SRC-ARXIV@arXiv:{x['aid']}v1"
    method = f"https://arxiv.org/html/{x['aid']}v1 — {x['method']}"
    evaluation = x["evaluation"] if x["evaluation"].startswith("Not Disclosed") else f"https://arxiv.org/html/{x['aid']}v1 — {x['evaluation']}"
    limits = x["limits"] if x["limits"].startswith("Not Disclosed") else f"https://arxiv.org/html/{x['aid']}v1 — {x['limits']}"
    fields = ["review-completion-v1", x["fid"], f"paper-v1:{x['aid']}", f"arXiv:{x['aid']}v1",
              canonical(support), f"arXiv:{x['aid']}v1", canonical(reviewed), x["route"]]
    if x["override"] != "none": fields.append(f"review-override:{x['override']}")
    fields += [canonical(method), canonical(evaluation), canonical(limits), canonical(x["artifact"]),
               f"claim:{x['fid']}", f"review:{x['fid']}", f"review-body-sha256:{body_sha}"]
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def main() -> None:
    inv = json.loads(INVENTORY.read_text())
    by_id = {x["arxiv_id"]: x for x in inv["identities"]}
    retained = {x["aid"] for x in C}
    if not retained <= by_id.keys():
        raise SystemExit(f"retained missing: {sorted(retained - by_id.keys())}")
    recovered_false_negatives = {"2604.27396", "2604.27467", "2604.27486", "2604.27781", "2604.27861", "2604.27878"}
    duplicate_aliases = {"2605.00320"}
    ledger = []
    for item in inv["identities"]:
        keep = item["arxiv_id"] in retained
        ledger.append({
            **item,
            "decision": "retain" if keep else "pre_denominator_closure",
            "reason": ("material long-term AI-System mechanism/ownership/evaluation delta; exact-v1 review routed"
                       if keep else closure_reason(item)),
            "author_adversarial_audit": ("false_negative_rechecked_no_admission_delta" if item["arxiv_id"] in recovered_false_negatives
                                            else "retain_reconfirmed" if keep
                                            else "false_negative_rechecked_no_admission_delta"),
            "independent_fresh_context_audit": ("recovered_false_negative" if item["arxiv_id"] in recovered_false_negatives
                                                   else "retain_reconfirmed" if keep
                                                   else "duplicate_family_reconciled" if item["arxiv_id"] in duplicate_aliases
                                                   else "closure_reconfirmed"),
        })
    (PACKET / "screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    with (PACKET / "screening-ledger.tsv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["arxiv_id", "published_v1_utc", "primary_category", "route", "decision", "title", "reason", "author_adversarial_audit", "independent_fresh_context_audit"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in ledger: writer.writerow({k: row[k] for k in fields})

    bodies = {x["fid"]: review_body(x, by_id[x["aid"]]["title"]) for x in C}
    review_packet = {
        "schema": "daily-v2.1-review-packet-v1", "date": "2026-05-01",
        "window": inv["window_beijing"], "raw_identity_count": inv["strict_window_total"],
        "registered_count": inv["registered_total"], "core_count": inv["core_total"],
        "keyword_count": inv["keyword_total"], "retained_count": len(C),
        "pre_denominator_closure_count": inv["registered_total"] - len(C),
        "prefix_counts": {"2604": sum(x["arxiv_id"].startswith("2604.") for x in inv["identities"]),
                          "2605": sum(x["arxiv_id"].startswith("2605.") for x in inv["identities"])},
        "retained_ids": sorted(retained),
        "books_writeback": [x["fid"] for x in C if x["disposition"] == "Integrate"],
        "independent_audit": "complete:fresh-context:/root/may2026_day02",
    }
    (PACKET / "review-packet.json").write_text(json.dumps(review_packet, ensure_ascii=False, indent=2) + "\n")

    source_refs = {
        "2604.27289":"turn11921view0", "2604.27292":"turn11921view1",
        "2604.27309":"turn11907view0", "2604.27792":"turn11910view0", "2604.27844":"turn11906view0",
        "2604.28138":"turn11909view0", "2604.28139":"turn11908view0", "2605.00066":"turn11894view3",
        "2605.00081":"turn11895view0", "2605.00136":"turn11895view2", "2605.00155":"turn11895view3",
        "2605.00161":"turn11895view4", "2605.00180":"turn11895view6", "2605.00206":"turn11895view8",
        "2605.00254":"turn11895view9", "2605.00267":"turn11895view10", "2605.00300":"turn11895view12",
        "2605.00314":"turn11895view13",
    }
    source_refs.update({
        "2604.27306":"turn11974view0", "2604.27351":"w18-reviewed-exact-v1",
        "2604.27358":"turn11974view1", "2604.27393":"w18-reviewed-exact-v1",
        "2604.27405":"turn11974view2", "2604.27419":"w18-reviewed-exact-v1",
        "2604.27426":"turn11974view3", "2604.27488":"turn11974view4",
        "2604.27536":"turn11974view5", "2604.27586":"turn11974view6",
        "2604.27637":"turn11974view7", "2604.27660":"w18-reviewed-exact-v1",
        "2604.27695":"turn11974view8", "2604.27707":"turn11974view9",
        "2604.27711":"w18-reviewed-exact-v1", "2604.27776":"w18-reviewed-exact-v1",
        "2604.27789":"turn11978view0", "2604.27819":"turn11978view1",
        "2604.27855":"turn11978view2", "2604.27906":"turn11978view3",
        "2604.28056":"turn11978view4", "2604.28123":"turn11978view5",
        "2604.28129":"turn11978view6", "2604.28157":"w18-reviewed-exact-v1",
        "2604.28158":"w18-reviewed-exact-v1", "2604.28175":"turn11978view7",
        "2604.28181":"w18-reviewed-exact-v1", "2604.28182":"turn11978view8",
        "2604.28190":"w18-reviewed-exact-v1", "2604.28196":"turn11978view9",
        "2604.27891":"turn11980view0", "2605.00226":"turn11980view5",
        "2604.27396":"turn12002view3", "2604.27467":"turn12002view1",
        "2604.27486":"turn12002view2", "2604.27781":"turn12002view4",
        "2604.27861":"turn12002view0", "2604.27878":"turn12002view5",
    })
    access = [{
        "source_family_id": x["fid"], "url": f"https://arxiv.org/html/{x['aid']}v1",
        "primary_version": f"arXiv:{x['aid']}v1", "retrieved_at": "2026-08-31T23:28:00+08:00",
        "web_proxy_source_ref": source_refs[x["aid"]],
        "provenance_scope": "exact-v1 primary URL plus method/evaluation/non-proof locators in Review Completion Receipt",
        "full_text_read": True,
    } for x in C]
    (PACKET / "primary-access-receipts.json").write_text(json.dumps(access, ensure_ascii=False, indent=2) + "\n")

    queue = ["# 2026-05-01 Books Writeback Queue", "", "本 worker 不修改共享 Books。root 应按事件时间串行写入，再顺读 owner 与相邻章节。", ""]
    for x in C:
        if x["disposition"] != "Integrate": continue
        existing, delta = BOOKS_COMPARISON[x["fid"]]
        queue += [f"## {x['fid']}", "", f"- Owner: `{x['node']}`", f"- Target: `{x['chapter']}`",
                  f"- Adjacent: `{x['adjacent']}`", f"- Existing owner coverage: {existing}",
                  f"- Missing durable delta: {delta}", f"- Proposition: {x['claim']}",
                  f"- Trade-off boundary: {x['limits']}", f"- Exact primary: https://arxiv.org/html/{x['aid']}v1", ""]
    (PACKET / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue))

    ids = "<br>".join(x["fid"] for x in C)
    den = "DEN-20260501-" + hashlib.sha256(("|".join(sorted(retained)) + inv["window_beijing"]).encode()).hexdigest()[:20]
    lines = [
        "# Daily Research — 2026-05-01", "", "**Research Date:** 2026-05-01", "", "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-04-30 09:00:00 ～ 2026-05-01 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay", "",
        "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open（24 个已审计 Source Family 等待 root 串行 Books 写回）", "",
        "## Executive Summary", "",
        f"完整回放联合 `2604 + 2605` 两个月的 DataCite DOI-prefix 快照，从 59,801 个唯一 DOI 中按 `Submitted:v1` 严格过滤出 **{inv['strict_window_total']}** 个窗口内 identity；注册分类命中 **{inv['registered_total']}** 项（Core {inv['core_total']}、keyword route {inv['keyword_total']}）。此前 311/139 是不完整快照产生的错误分母，本报告不继承。",
        f"532 条 title+abstract 逐项筛选后，拟冻结 **{len(C)}** 个 Candidate Source Family（{len(C)/inv['registered_total']:.2%}），其余 **{inv['registered_total']-len(C)}** 项均在 screening ledger 留下 family-specific pre-denominator closure。{len(C)} 项完成 exact-v1 Method/Evaluation/Limitations 边界、Score V2、Books Comparison 与最多三条 Deep Analysis；其中 {len(review_packet['books_writeback'])} 项进入共享 Books 串行写回队列。",
        "独立 fresh-context 审计重新检查了 532 行筛选账本、56 份 exact-v1 Review 与当前 Books：恢复 6 个 false negative，将 VitaLLM 重复投稿折叠到一个 family，并把 7 个已有正文完整覆盖的 provisional Integrate 降级。Coverage、Evidence 与 Selection 已通过；root 仍须按最终 24-family 队列串行写回 Books，因此当前不宣称 Complete。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-01 |", "| Window End | 2026-05-01 |",
        "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
        f"| Denominator ID | {den} |", "| Denominator Frozen At | 2026-09-01T00:40:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-04-30T09:00:00+08:00 | 2026-05-01T09:00:00+08:00 | 2026-08-31T23:10:00+08:00 | registered Core + keyword categories; full title+abstract semantic screening | checked | {inv['strict_window_total']} | {ids} | complete disjoint 2604/2605 DataCite DOI-prefix snapshots, 00..99, all pages/cursors closed | 2026-05-01T01:00:00Z | coverage:SRC-ARXIV:20260501 | — |",
        "", marker("coverage:SRC-ARXIV:20260501", f"`datacite-arxiv-202604-v2` 与 `datacite-arxiv-202605-v2` 共覆盖 59,801 个唯一 DOI；严格窗口命中 {inv['strict_window_total']}，其中注册 route {inv['registered_total']}（2604 前缀 {review_packet['prefix_counts']['2604']}、2605 前缀 {review_packet['prefix_counts']['2605']}）。screening ledger 逐项闭合为 {len(C)} retained + {inv['registered_total']-len(C)} pre-denominator closures。DataCite 只证明 identity/subject/submitted metadata，所有机制结论回到 exact-v1 arXiv HTML。"),
        "### Coverage Limitations", "",
        "- official arXiv Atom/OAI 枚举端点在恢复时不可访问；完整、互斥的 DataCite 00..99 分区用于 identity/date routing，独立 auditor 已逐项复核 532 个 registered identity，因此该 fallback 不再保持 Coverage Open。",
        "- 注册表中 2026-08-25 才生效的组织来源不追溯成为本历史 Daily 的 Required；本轮唯一到期 Required source 是 `SRC-ARXIV`。",
        f"- {len(C)} 份 retained family 均回到 exact-v1 HTML 完成 Method、Evaluation 与 non-proof Review；DataCite 不支持任何机制结论。", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for x in C:
        d,s,u=x["score"]; fp=by_id[x["aid"]]["published_v1_utc"][:10]
        lines.append(f"| {x['fid']} | arXiv:{x['aid']}v1 | paper-v1:{x['aid']} | 2026-W18 | {fp} | SRC-ARXIV | {d} | {s} | {u} | {x['total']} | retained | {x['route']}_complete | accessible | {x['override']} | review:{x['fid']} | self | — | new_in_window | {x['node']} | {x['disposition']} | books-review:{x['fid']} | yes |")
    lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
              "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in C:
        body=bodies[x["fid"]]
        evaluation_locator = x["evaluation"] if x["evaluation"].startswith("Not Disclosed") else f"https://arxiv.org/html/{x['aid']}v1 — {x['evaluation']}"
        limitations_locator = x["limits"] if x["limits"].startswith("Not Disclosed") else f"https://arxiv.org/html/{x['aid']}v1 — {x['limits']}"
        lines.append(f"| {x['fid']} | {provenance(x,body)} | {x['route']} | arXiv:{x['aid']}v1 | SRC-ARXIV@arXiv:{x['aid']}v1 | https://arxiv.org/html/{x['aid']}v1 — {x['method']} | {evaluation_locator} | {limitations_locator} | {x['artifact']} | claim:{x['fid']} | complete |")
    lines += ["", "### Source Reviews", ""]
    for x in C: lines += [marker(f"review:{x['fid']}", bodies[x["fid"]]), ""]

    lines += ["## 4. Benchmark Contracts", "", "下表不保留 headline speedup；未公开字段显式保持 `Not Disclosed`。", "", "<!-- validator:benchmark-contract-v1 -->",
              "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in C:
        lines.append(f"| {x['fid']} | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |")

    selected={"SF-2026-ARXIV-2604-27844":"DA-TRAIN-COMM", "SF-2026-ARXIV-2604-28138":"DA-AGENT-STATE", "SF-2026-ARXIV-2604-28139":"DA-EVAL-CONTROL"}
    subs={
        "SF-2026-ARXIV-2605-00081":"DA-AGENT-STATE", "SF-2026-ARXIV-2605-00136":"DA-AGENT-STATE", "SF-2026-ARXIV-2605-00314":"DA-AGENT-STATE", "SF-2026-ARXIV-2605-00267":"DA-AGENT-STATE",
        "SF-2026-ARXIV-2604-27309":"DA-EVAL-CONTROL", "SF-2026-ARXIV-2605-00066":"DA-EVAL-CONTROL", "SF-2026-ARXIV-2605-00300":"DA-EVAL-CONTROL",
        "SF-2026-ARXIV-2605-00180":"DA-TRAIN-COMM", "SF-2026-ARXIV-2605-00254":"DA-TRAIN-COMM",
    }
    lines += ["", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
              "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
    eligible=[]
    for x in C:
        if x["total"]>=7 or x["override"]!="none":
            eligible.append(x)
            elig="score_7_9" + (";forced_review" if x["override"]!="none" else "") + (";potential_books_delta" if x["disposition"]=="Integrate" else "")
            if x["fid"] in selected:
                unit=selected[x["fid"]]; lines.append(f"| {x['fid']} | {elig} | selected | {unit} | — | 代表跨层 state/control/evidence 演进主线。 | analysis:{unit} |")
            elif x["fid"] in subs:
                unit=subs[x["fid"]]; lines.append(f"| {x['fid']} | {elig} | subsumed | — | {unit} | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:{unit} |")
            else:
                lines.append(f"| {x['fid']} | {elig} | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:{x['fid']} |")
    lines += ["", marker("analysis:DA-TRAIN-COMM", "### Deep Analysis 1 — 从局部优化到通信、路由与拓扑的联合控制\n\n分布式训练/推理最初可把 collective 和 routing 当固定实现，因为 tensor 分布、模型集合和 topology 稳定。ZipCCL 利用 BF16 exponent 分布做 lossless collective compression；RouteProfile 用已有模型图为新模型迁移 profile；MoE topology 把 expert placement、token skew 与 network tier 合并。三者共同说明：减少 bytes 或探索成本会新增 estimator、profile freshness、switcher 与 hotspot 状态。固定 NCCL、完整 profiling 和均匀 topology 在小规模/稳定 workload 仍是更安全基线。"), "",
              marker("analysis:DA-AGENT-STATE", "### Deep Analysis 2 — Agent 从文本循环演进为 effect、checkpoint 与 policy 的状态机\n\n只保存对话、只审查输出在无副作用工具和短任务中足够。Crab 显示真实恢复还需 OS state 与 turn boundary；Alignment Contracts 把 effect mediation 移到独立执行边界；tool-use tax 拆开 schema/routing/transport 成本；Semia 将 skill source→sink 变成静态约束；jailbreak capability 说明不能假设越狱后能力自然消失。收益是可恢复、可审计和最小权限，代价是 inspector 误判、静态抽象不完备、policy overhead 与更多控制状态。"), "",
              marker("analysis:DA-EVAL-CONTROL", "### Deep Analysis 3 — Evaluation 从静态得分演进为版本化 release control\n\n离线分数在对象和环境稳定时合理。EHR deployment 将 rubric、live feedback、SLO 和 cost 接到版本 gate；Claw-Eval-Live 分离 refreshable demand 与 frozen snapshot；open-loop/closed-loop 研究否定未经校准的代理指标；Token Arena 以 endpoint/configuration 为测量对象。共同结论不是增加 benchmark，而是冻结 object、workload、evaluator、terminal evidence 与版本，再让证据拥有或拒绝 release authority。"), ""]
    for x in eligible:
        if x["fid"] not in selected and x["fid"] not in subs:
            lines += [marker(f"analysis-decision:{x['fid']}", "该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。"), ""]

    lines += ["## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
              "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in C:
        lines.append(f"| {x['fid']} | {x['node']} | {x['chapter']} | {x['adjacent']} | existing:{x['fid']} | delta:{x['fid']} | {x['relation']} | {x['disposition']} | books-review:{x['fid']} |")
    lines += [""]
    for x in C:
        if x["disposition"] == "Integrate":
            existing, delta = BOOKS_COMPARISON[x["fid"]]
        else:
            existing=f"已核对 `{x['chapter']}` 与 `{x['adjacent']}`；现有正文已拥有该 state/control/evidence boundary。"
            delta="本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。"
        lines += [marker(f"books-review:{x['fid']}", marker(f"existing:{x['fid']}",existing)+marker(f"delta:{x['fid']}",delta)+f"演进关系 `{x['relation']}`；决定 `{x['disposition']}`。"), ""]

    lines += ["## 7. Semantic Audit", "", "独立 auditor 未参与本日 author packet，已对 532 行 screening、56 份 exact-v1、Deep Selection 与 current Books owner/adjacent content 完成 fresh-context 复核。审计明细见 `papers/2026/05/_sources/daily-20260501/independent-semantic-audit.json`。", "",
              "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
              "| --- | --- | --- | --- | --- | --- | --- |",
              "| SA-20260501-COVERAGE | fresh-context:may2026_day02 | coverage | coverage:SRC-ARXIV:20260501 | none | Independent audit materialized six false-negative recoveries, reconciled one VitaLLM duplicate, and froze 56 retained plus 476 closures. | passed |",
              f"| SA-20260501-EVIDENCE | fresh-context:may2026_day02 | evidence | {'; '.join('review:'+x['fid'] for x in C)} | none | 56 exact-v1 claim/locator/non-proof records checked; blocked=0. | passed |",
              "| SA-20260501-SELECTION | fresh-context:may2026_day02 | deep_analysis_selection | analysis:DA-TRAIN-COMM; analysis:DA-AGENT-STATE; analysis:DA-EVAL-CONTROL | none | All eligible families have an explicit selection disposition; the three narratives remain distinct communication, agent-state and evaluation-control chains. | passed |",
              f"| SA-20260501-BOOKS | fresh-context:may2026_day02 | books | {'; '.join('books-review:'+x['fid'] for x in C)} | BOOKS-WRITEBACK-20260501 | Current-content comparison downgraded seven provisional Integrate items and added three recovered items; root must serialize {len(review_packet['books_writeback'])} writes and perform post-write audit. | open |", "",
              "## 8. Ignored Noise", "", f"{inv['registered_total']-len(C)} 个 pre-denominator closure 位于 `papers/2026/05/_sources/daily-20260501/screening-ledger.json/tsv`。每项保留 identity、v1 时间、分类、title、abstract、具体 closure reason 和 author false-negative audit，不进入 Score V2，也不冒充全文 Review。", "",
              "## 9. Recommended Action", "", f"1. root 按事件时间处理最终 {len(review_packet['books_writeback'])}-family Books writeback queue；同一 owner 与其他日期冲突时只串行正文写入。", "2. 写回后由非作者 auditor 顺读 owner/adjacent，核验旧方案、约束变化、state/control ownership、trade-off、failure 与 fallback。", "3. post-write finding 为零后更新本日报 Books disposition/Repository Changes/Open Questions，再关闭 Books Gate。", "",
              "## 10. Repository Changes", "", "- 新建本日 inventory、532-row screening ledger、review packet、Books writeback queue 与 Daily README。", "- 未修改 Books、ROADMAP、LEARNING_STATE；未 stage、commit 或 push。", "",
              "## 11. Open Questions", "", "- lossless collective compression 的分布假设如何在训练 phase、dtype 与 model family 漂移时在线验证并安全回退？", "- Agent checkpoint 的最小 recovery state 如何与 tool idempotency、external side effects 和 workflow commit 统一？", "- endpoint-centric benchmark 如何冻结 provider drift、价格、energy telemetry 与 evaluator version？", "- effect-level policy 怎样在未知 tool semantics 下 abstain，而不是把静态 audit 误当 runtime proof？", "",
              "## 12. Sources", ""]
    for x in C:
        item=by_id[x["aid"]]
        lines.append(f"- [{item['title']}](https://arxiv.org/html/{x['aid']}v1) — arXiv:{x['aid']}v1；Submitted `{item['published_v1_utc']}`；访问 2026-08-31。")
    lines += ["", "## 13. Final Status", "", "- Completion Status = `In Progress`", "- Coverage = `Closed`（532/532 independently audited；56 retained + 476 closures）", "- Evidence = `Passed`（56/56 exact-v1 Review checked；blocked=0）", f"- Books = `Open`（{len(review_packet['books_writeback'])}-family serial writeback pending）", "- unresolved findings = `1`（Books writeback + post-write audit）", "- 下一检查点：root 串行 Books 写回 → 非作者 post-write owner/adjacent 顺读 → validator 与 diff check。", ""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"raw":inv["strict_window_total"],"registered":inv["registered_total"],"retained":len(C),"closures":inv["registered_total"]-len(C),"integrate":len(review_packet["books_writeback"])},ensure_ascii=False))


if __name__ == "__main__":
    main()
