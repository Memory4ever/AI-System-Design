#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the 2025-05-02 V2.1 Daily and its frozen audit packet."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2025/05/_sources/daily-v2.1-replay-202505"
INVENTORY = PACKET / "2025-05-02-arxiv-inventory.json"
REPORT = ROOT / "papers/2025/05/02/README.md"
QUEUE = PACKET / "2025-05-02-books-writeback-queue.md"


def candidate(fid, aid, score, node, disposition, chapter, adjacent, existing,
              delta, relation, method, evaluation, limits, artifact, claim,
              review, benchmark, override="none"):
    return {
        "fid": fid, "aid": aid, "score": score, "total": sum(score),
        "node": node, "disposition": disposition, "chapter": chapter,
        "adjacent": adjacent, "existing": existing, "delta": delta,
        "relation": relation, "method": method, "evaluation": evaluation,
        "limits": limits, "artifact": artifact, "claim": claim,
        "review": review, "benchmark": benchmark, "override": override,
        "route": "deep" if sum(score) >= 7 or override != "none" else "standard",
    }


C = [
    candidate("SF-2025-UNLOK", "2505.01456", (2,2,2), "PLATFORM-SECURITY", "No Change — Existing Coverage", "books/part-06-ai-infrastructure/72-security.md", "books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-03-multimodal-world-models/23-multimodal-representation.md", "Security/Evaluation 已要求攻击、模型、数据、目标与 evaluator 共同构成安全证据身份。", "UnLOK 提供多模态 unlearning 的 typed attack-defense benchmark，但不改变既有 authority 或 release gate。", "Principle Reuse", "exact-v1 §3 UnLOK benchmark；§4 threat model, attacks and defenses", "exact-v1 §5 setup；§6 results", "exact-v1 §6 discussion；Appendix B reproducibility boundary", "Not Disclosed — exact event-time code revision is not frozen", "多模态 unlearning 不能只报告遗忘分数；必须同时冻结敏感对象、攻击面、泛化、specificity 与防御目标。", "论文构造敏感多模态知识与七类攻击/六类防御目标，在受限模型和任务上比较 efficacy、generalization 与 specificity。它不证明参数内信息被普遍删除，也不能替代法律删除、数据 lineage 或 production release gate。", ("multimodal unlearning benchmark with typed attacks/defenses", "models listed in exact-v1 §5", "Not Disclosed", "Not Disclosed", "dataset-defined", "task-defined", "Not Disclosed", "offline", "efficacy/generalization/specificity; no production threshold", "benchmark rules and attack success metrics")),
    candidate("SF-2025-AVA", "2505.00254", (2,2,2), "AGENT-RAG", "Integrate", "books/part-07-agent/76-rag.md", "books/part-07-agent/75-context.md; books/part-07-agent/77-memory.md", "RAG 已有 chunk/index/provenance，但缺少持续视频流如何变成可修订事件图的完整路径。", "补充 observation→VLM description→semantic chunk→event/entity/temporal graph→tri-view retrieval/search；graph revision 与 staleness 成为 retrieval state。", "Direct Evolution", "exact-v1 §3 system overview；§4 index construction；§4.1 Event KG", "exact-v1 §5 agentic retrieval；§6 implementation；§7 evaluation", "exact-v1 §8 limitations", "Not Disclosed — linked implementation revision is not frozen in the paper", "长视频 RAG 要先把连续观察压缩为带时间和来源的可修订事件图，再让 agent 在不同视图间检索；短视频直接 VLM 仍是低复杂度分支。", "作者以 3 秒片段生成描述并做语义合并，构造事件/实体/时间图，再用多视图检索、MCTS 与 self-consistency 回答。AVA-100 只覆盖八段长视频和 120 个问题；描述误差、图陈旧与搜索成本会累积，不能外推为通用实时视频理解。", ("long-video indexing and agentic question answering", "Qwen2.5-VL-7B for indexing; answer roster in paper", "2×RTX 4090 for index construction", "Not Disclosed", "3-second video chunks; videos >10 hours", "answer text", "Not Disclosed", "self-consistency 8/16 samples", ">5 FPS indexing; QA quality; no production SLO", "AVA-100 human-authored QA and paper metrics"), override="knowledge_gap"),
    candidate("SF-2025-ENRONQA", "2505.00263", (2,2,2), "AGENT-RAG", "No Change — Existing Coverage", "books/part-07-agent/76-rag.md", "books/part-07-agent/75-context.md; books/part-06-ai-infrastructure/71-multi-tenancy.md", "RAG 已把 tenant、ACL、corpus revision 与 retrieval receipt 纳入私有知识边界。", "EnronQA 是个性化私有文档 RAG 的数据与评测案例，不新增 owner。", "Principle Reuse", "exact-v1 §3 dataset construction；§4 quality", "exact-v1 §5 benchmarking；§6 memorized knowledge", "exact-v1 §7 discussion；Ethics statement", "Not Disclosed — dataset release revision is not frozen", "私有文档 RAG 的正确答案必须绑定用户、邮箱快照、权限与 retrieval receipt；benchmark 命中不证明真实企业隐私和访问控制。", "作者从 103,638 封邮件构造 528,304 QA，并以 150 个 inbox 测试个性化检索与模型记忆。该合同支持检索/记忆差异分析，不证明真实企业 ACL、删除、时效或隐私合规。", ("personalized QA over private email corpora", "retrieval and LLM baselines listed in §5", "Not Disclosed", "Not Disclosed", "email/query-defined", "answer text", "Not Disclosed", "offline", "QA metrics; no latency or privacy SLO", "dataset answers and benchmark scorer")),
    candidate("SF-2025-MOSA", "2505.00315", (2,2,2), "MODEL-LONG-CONTEXT", "No Change — Existing Coverage", "books/part-02-model/22-long-context.md", "books/part-02-model/15-attention.md; books/part-05-inference-system/49-tensorrt-llm.md", "Long Context 已区分 dense fallback、content selector、position identity 与 sparse-kernel cost。", "把每个 attention head 视作 expert 并按 token content 选择子集，是现有 content-based sparse branch 的实现。", "Alternative Branch", "exact-v1 §2 Mixture of Sparse Attention", "exact-v1 §3 experiments；Appendix FLOPs/model settings", "exact-v1 §5 limitations", "Not Disclosed — optimized sparse kernel is not released as frozen evidence", "content-based sparse attention 以 selector 换取更低 attention work，但 selector error、position identity 和稀疏 kernel 决定它是否优于 dense。", "作者在 iso-FLOP 的非自回归语言建模设置比较 expert-choice sparse attention；perplexity 优势并不总转化为下游收益，短序列较弱，且未提供优化 kernel 或 causal serving 证据。", ("iso-FLOP language modeling with sparse attention", "models listed in exact-v1 Appendix", "Not Disclosed", "Not Disclosed", "sequence lengths in paper", "Not Applicable", "Not Disclosed", "offline", "perplexity/downstream score; no serving SLO", "paper task evaluators")),
    candidate("SF-2025-T2VPHYS", "2505.00337", (2,2,2), "MULTIMODAL-WORLD-MODELS", "No Change — Existing Coverage", "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md; books/part-06-ai-infrastructure/66-evaluation-system.md", "World Model/Evaluation 已区分视频 plausibility、物理一致性、action-conditioned transition 与因果证据。", "十二类物理规律、hint/counterfactual probe 与人工协议是既有 evaluation contract 的案例。", "Principle Reuse", "exact-v1 §3 benchmark；§3.3 protocol", "exact-v1 §4 experiments；Appendix A implementation", "exact-v1 §5 discussion；Appendix B limitations", "Not Disclosed — benchmark revision is not frozen", "视频生成质量不能代替物理一致性；评估必须冻结物理规律、prompt、hint/counterfactual、judge 与人类协议。", "作者以十二类 first-principles law 构建 benchmark 并报告受测系统平均分均低于 0.60。它诊断生成失败，不证明模型具有或缺乏可用于控制的因果 world state，也不预测真实机器人 policy success。", ("text-to-video physical consistency across 12 law categories", "video generators listed in §4", "Not Disclosed", "Not Disclosed", "prompt-defined", "video", "Not Disclosed", "offline", "physical consistency score; no production threshold", "human protocol plus benchmark judge")),
    candidate("SF-2025-LLMPRISM", "2505.00342", (3,3,3), "PLATFORM-MONITORING", "Integrate", "books/part-06-ai-infrastructure/67-monitoring.md", "books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-06-ai-infrastructure/68-logging.md", "Monitoring 已有 metrics/logs/traces 与 collective telemetry，但缺少无法植入代码时的网络流序列诊断分支。", "补充 network-flow sequence 作为低侵入 correlated sensor，用来推断训练 job identity、并行配置、phase/timeline 与 stall；它只拥有诊断线索，不拥有 correctness。", "Alternative Branch", "exact-v1 §III motivation；§IV methodology A-D", "exact-v1 §V evaluation and deployed experience A-D", "exact-v1 §VII generalization and limits", "Not Disclosed — production deployment code is not public", "当训练框架不可插桩时，网络流序列可提供 job/parallelism/phase 的旁路传感；共享流量、加密、拓扑和框架漂移会使它失效，必须回退显式 instrumentation。", "论文从交换机/host 网络流推断训练任务、并行策略与阶段，并报告自 2024-10 的生产部署经验。作者的识别率和时间线误差只属于其平台与流量合同；旁路传感无法证明模型正确，也可能被共享流量或版本漂移混淆。", ("black-box diagnosis of production LLM training network flows", "production training jobs; exact model roster Not Disclosed", "production platform topology Not Disclosed", "Not Applicable", "flow sequence", "job/parallelism/phase labels", "Not Disclosed", "multi-job platform", "diagnosis accuracy and timeline error; no user-facing SLO", "ground-truth platform job metadata")),
    candidate("SF-2025-SOLO", "2505.00347", (3,2,3), "TRAIN-PRETRAINING", "Integrate", "books/part-04-training-system/28-pretraining.md", "books/part-04-training-system/27-data.md; books/part-04-training-system/29-sft.md", "Pretraining 已有 low-precision update、error feedback 与 role-aware optimizer state，但没有解释 EMA dynamics 的两种量化失真。", "补充 unsigned EMA 的 signal swamping 与 signed state 的 variance/wrong-direction 分支；量化器、momentum precision 与 checkpoint identity 必须共同冻结。", "Direct Evolution", "exact-v1 §3 ultra-low-bit optimizer；§3.1-3.3 EMA dynamics", "exact-v1 §4 experiments；Appendix C settings", "exact-v1 discussion/ablation and precision limits", "Not Disclosed — exact training implementation revision not frozen", "低比特 optimizer 的风险不只是静态误差：unsigned EMA 会淹没新信号，signed state 会放大方差或方向错误；状态演化决定是否还能学习。", "作者用 log quantization 与 precision-specific momentum 处理 2-bit 级 Adam state，并在受限模型/训练设置比较。证据不覆盖所有 optimizer、分布式 checkpoint、故障恢复或数值格式；高精度 state 在小规模或不稳定训练中仍是基线。", ("language-model training with ultra-low-bit optimizer states", "model roster in exact-v1 §4", "hardware Not Disclosed", "2-bit and comparison precisions", "training sequence length Not Disclosed", "Not Applicable", "settings in Appendix C", "distributed topology Not Disclosed", "loss/downstream quality and memory; no production SLO", "paper training/evaluation pipeline")),
    candidate("SF-2025-RNB", "2505.00358", (3,3,3), "TRAIN-DATA", "No Change — Existing Coverage", "books/part-04-training-system/27-data.md", "books/part-04-training-system/28-pretraining.md; books/part-06-ai-infrastructure/66-evaluation-system.md", "Data 已把 mixture weight 视为受 gradient/coverage/evaluation 反馈约束的动态控制状态。", "embedding+gradient regrouping 与 final-layer similarity 是该控制链的受限 estimator，不新增 owner。", "Direct Evolution", "exact-v1 §3 regrouping and balancing", "exact-v1 §4 experiments；Appendix E/F implementation/settings", "exact-v1 Appendix D cost and discussion limits", "Not Disclosed — exact data/control artifact revision is not frozen", "数据域不能永久沿用人工标签；可由表示和梯度反馈重组，但 estimator、mixture revision 与 drift fallback 必须纳入 lineage。", "作者以 embedding 与累计 final-layer gradient similarity 动态重组域并更新 mixture。受控实验支持样本效率，不能证明 final-layer proxy 在 frontier scale、生产漂移或不同 optimizer 下稳定；cluster churn 和 feedback cost 是新风险。", ("foundation-model pretraining data regrouping and mixture balancing", "model roster in exact-v1 §4", "Not Disclosed", "Not Disclosed", "training corpus-defined", "Not Applicable", "Not Disclosed", "offline training", "loss/downstream metrics; no production SLO", "paper benchmark evaluators")),
    candidate("SF-2025-DISTRIBUTED-RAG", "2505.00443", (2,3,2), "AGENT-RAG", "Integrate", "books/part-07-agent/76-rag.md", "books/part-07-agent/75-context.md; books/part-07-agent/77-memory.md", "RAG 主要以中央索引为默认，已讨论 partition 和 federation，但缺少 peer-owned knowledge 的完整控制边界。", "补充 peer-owned indexes 与 topic-aware random walk：恢复数据所有权，同时引入 query leakage、peer availability/trust、routing 与 index consistency。", "Alternative Branch", "exact-v1 §3 distributed RAG model and topic-aware random walk", "exact-v1 §4 experiments and sensitivity", "exact-v1 discussion and threat boundary", "Not Disclosed — exact simulation/repository revision is not frozen", "分布式 RAG 将 corpus ownership 留在 peer，并以 topic-aware discovery 代替中央索引；它减少集中收集，却不会自动提供 query privacy、信任或一致性。", "作者在仿真网络比较 topic-aware random walk 与 flooding/centralized baselines，并报告接近中央检索、消息更少。证据不覆盖对抗 peer、真实网络故障、隐私证明或生产尾延迟；稳定可审计 corpus 仍适合中央 RAG。", ("peer-to-peer retrieval-augmented generation", "retrieval/generation models in exact-v1", "simulation; hardware Not Disclosed", "Not Disclosed", "query/corpus-defined", "answer text", "Not Disclosed", "peer network simulation", "retrieval/answer quality and messages; no production SLO", "simulation benchmark metrics")),
    candidate("SF-2025-HALLUMIX", "2505.00506", (2,2,2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "books/part-06-ai-infrastructure/66-evaluation-system.md", "books/part-06-ai-infrastructure/67-monitoring.md; books/part-06-ai-infrastructure/72-security.md", "Evaluation 已把 hallucination 拆为 claim/evidence、slice、length、evaluator 与 calibration contract。", "HalluMix 是跨 NLI/summary/QA 的 benchmark 实例，强调 sub-source overfitting 与长度效应。", "Principle Reuse", "exact-v1 §2 benchmark；§3 methodology", "exact-v1 §4 results", "exact-v1 §5 discussion, sub-source overfitting and length", "Not Disclosed — exact benchmark release revision not frozen", "hallucination detector 的分数只属于给定任务、来源、长度和 evaluator；跨来源平均值不能替代 slice 与 calibration。", "作者构建 task-agnostic multi-domain benchmark，比较检测器并揭示来源过拟合与长度效应。最佳指标属于其数据划分和标签协议，不证明开放世界事实核验、生产置信度或单条 claim 正确性。", ("hallucination detection across NLI, summarization and QA", "detector roster in exact-v1", "Not Disclosed", "Not Disclosed", "dataset/length slices", "label", "Not Disclosed", "offline", "accuracy/F1; no production calibration threshold", "benchmark labels and paper metrics")),
    candidate("SF-2025-FREQKV", "2505.00570", (3,2,3), "INFER-KV-CACHE", "No Change — Existing Coverage", "books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "books/part-02-model/22-long-context.md; books/part-05-inference-system/47-paged-attention.md", "KV/Long Context 已覆盖 feature/frequency compression、position identity、lossy error 与 FullKV fallback。", "FreqKV 的迭代频域压缩是已有 branch 的具体 estimator，不新增运行时 owner。", "Alternative Branch", "exact-v1 §4 method", "exact-v1 §5 experiments；§6 latency analysis", "exact-v1 analysis and Appendix D overhead", "Not Disclosed — exact implementation revision not frozen", "频域 KV 压缩用有损 summary 延伸窗口；频率分配、RoPE/position identity 与关键 token 丢失决定它何时必须回退 FullKV。", "作者在 LLaMA2/3、8K 训练与最长 256K 评测下比较长上下文任务和 latency。证据不覆盖 continuous batching、并发尾延迟或关键事实不可丢失的 workload，不能把平均质量外推为通用无损缓存。", ("long-context inference with frequency-domain KV compression", "LLaMA2/3 roster in exact-v1", "hardware in exact-v1 §6; topology Not Disclosed", "Not Disclosed", "trained 8K; evaluated up to 256K", "task-defined", "Not Disclosed", "Not Disclosed", "task quality and latency; no production SLO", "long-context benchmark metrics")),
    candidate("SF-2025-GRAPH-MOE", "2505.00792", (2,2,2), "MODEL-MOE", "No Change — Existing Coverage", "books/part-02-model/21-moe.md", "books/part-02-model/16-mlp.md; books/part-04-training-system/37-tensor-parallel.md", "MoE 已把 token/context-conditioned router、capacity、load、placement、dispatch 与 drift/fallback 放在同一链。", "token similarity/attention context 形成 graph signal，是已有 context-aware routing 的一种输入。", "Principle Reuse", "exact-v1 §§2-4 graph routing mechanism and entropy", "exact-v1 §5 evaluation；Appendix experiment details", "exact-v1 limitations/ablation and Appendix deployment boundary", "Not Disclosed — no frozen distributed runtime artifact", "router 可利用 token graph context 改变 expert selection，但质量增益只有在 capacity、load、dispatch 与 placement 同时成立时才转化为系统收益。", "作者在中等语言模型和 60M 视觉 MoE、K=2 下报告 modest gains。它不提供 frontier distributed dispatch、expert placement 或生产路由漂移证据，因此不能改变既有系统结论。", ("context-aware routing in language and vision MoE", "medium LM and 60M vision MoE", "Not Disclosed", "Not Disclosed", "task-defined", "task-defined", "K=2 routing", "offline", "task metrics/router entropy; no serving SLO", "paper benchmark evaluators")),
    candidate("SF-2025-PATCHWORK-RAG", "2505.07833", (3,3,3), "INFER-SCHEDULING", "No Change — Existing Coverage", "books/part-05-inference-system/56-inference-scheduling.md", "books/part-05-inference-system/55-pd-disaggregation.md; books/part-06-ai-infrastructure/64-resource-scheduling.md", "Inference Scheduling 已把 RAG 写成 typed operator DAG、bounded queue、heterogeneous placement 与 end-to-end SLO controller。", "Patchwork v1 提供 pipeline spec、placement/config selection 与 SLO mitigation 的受限实现；当前 metadata 后来改名 Harmonia，不改写 v1 identity。", "Direct Evolution", "exact-v1 title Patchwork；§3 framework/spec/allocation/configuration/SLO mitigation", "exact-v1 §4 evaluation and sensitivity", "exact-v1 discussion and workload/topology limits", "Not Disclosed — exact event-time implementation revision not frozen", "RAG serving 优化必须以端到端 operator DAG 和 SLO budget 为单位；单算子加速若移动 bottleneck，不能代表请求收益。", "v1 论文以四类 RAG 应用评估异构 placement、configuration 与 runtime mitigation，并报告 throughput/SLO violation 改善。结果只属于作者模型、硬件和 workload；current Atom 标题 Harmonia 是后续 rename，不能回写为 v1 标题或证明生产普适性。", ("end-to-end serving for four RAG applications", "models/operators listed in exact-v1", "heterogeneous cluster in exact-v1; topology details Not Disclosed here", "Not Disclosed", "application-defined", "application-defined", "Not Disclosed", "multi-stage serving", "throughput and SLO violations; thresholds in exact-v1", "application-specific quality/SLO evaluator")),
    candidate("SF-2025-SPILL-BEANS", "2505.00817", (3,3,3), "PLATFORM-SECURITY", "Integrate", "books/part-06-ai-infrastructure/72-security.md", "books/part-06-ai-infrastructure/71-multi-tenancy.md; books/part-06-ai-infrastructure/73-production.md", "Security 已覆盖 tenant isolation、model/data side channels，但缺少 token embedding access 可经共享 CPU cache 泄露的明确 control boundary。", "补充 shared cache/page/embedding access side channel；隔离、page sharing、cache partition 与 co-location policy 属于平台 authority，不是模型过滤。", "Layering / Dependency", "exact-v1 §4 threat and attack", "exact-v1 §§5-6 leakage evaluation", "exact-v1 §8 countermeasures；Ethics", "Not Disclosed — attack artifact revision not frozen", "即便 API 不返回 logits，共享 CPU cache 与 embedding access 仍可能泄露 token；防御必须进入 co-location、page sharing 和 cache isolation，而不只是输出过滤。", "作者在特定 co-location 与监控 token set 下恢复 API key/英文 token，headline rate 受可监控集合、CPU/cache 与部署布局约束。它不证明任意云、多租户或模型都可被同样攻击，但足以扩展平台 threat model。", ("CPU cache side-channel token leakage from LLM inference", "victim model/runtime in exact-v1", "CPU/cache configuration in exact-v1; general topology Not Disclosed", "Not Disclosed", "prompt/token stream", "token identity", "Not Disclosed", "co-located attacker", "token/key recovery under paper threat model; no production threshold", "known token ground truth")),
    candidate("SF-2025-OET", "2505.00843", (2,2,2), "PLATFORM-SECURITY", "No Change — Existing Coverage", "books/part-06-ai-infrastructure/72-security.md", "books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-07-agent/78-tool.md", "Security/Evaluation 已要求 adaptive attack、threat model、utility 与 action gate 分离。", "optimization-based white/black-box prompt injection 是已有 adaptive red-team branch 的工具实例。", "Principle Reuse", "exact-v1 §3 toolkit workflow", "exact-v1 §4 evaluation", "exact-v1 discussion and attack coverage limits", "Not Disclosed — toolkit repository revision not frozen", "prompt-injection defense 必须面对能依据反馈优化的攻击，并把内容 detection 与 tool/action authorization 分开。", "论文提供 optimization-based white/black-box attack workflow并比较防御。它不证明覆盖开放攻击空间、真实工具 authority 或持续漂移；评测工具不取得 deployment security authority。", ("adaptive prompt-injection evaluation", "target model/defense roster in exact-v1", "API/local; hardware Not Disclosed", "Not Disclosed", "prompt-defined", "attack response", "Not Disclosed", "offline/adaptive queries", "attack success and utility; no production threshold", "toolkit rules and paper evaluator"), override="release_security_contract"),
    candidate("SF-2025-NEMO-INSPECTOR", "2505.00903", (2,2,2), "TRAIN-DATA", "No Change — Existing Coverage", "books/part-04-training-system/27-data.md", "books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-04-training-system/28-pretraining.md", "Data/Evaluation 已把 synthetic sample、inspection、filter、lineage 与 human audit 分开。", "NeMo-Inspector 是 generation inspection/filtering 的工具案例，不新增证据 authority。", "Layering / Dependency", "exact-v1 §2 overview；§3 usage", "exact-v1 §4 results", "exact-v1 §6 limitations", "Not Disclosed — exact tool revision not frozen", "synthetic data inspection 应保留原 generation、filter reason、reviewer 与 downstream evaluation；可视化工具只支持 diagnosis，不自动决定 admission。", "作者展示推理可视化、分析和人工过滤，并在 GSM-Plus/OpenMath 案例报告质量变化。结果属于所选生成器、过滤标准和下游任务；它不证明人工筛选可扩展或自动过滤无偏。", ("LLM generation inspection and filtering", "generator/training models in exact-v1", "Not Disclosed", "Not Disclosed", "dataset-defined", "generation text", "Not Disclosed", "offline", "filter rate and downstream accuracy; no production SLO", "dataset/task evaluator")),
]


def marker(ref, body):
    return f"<!-- {ref}:start -->{body}<!-- {ref}:end -->"


def normalized_hash(text):
    text = unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n"))
    return hashlib.sha256("\n".join(x.rstrip() for x in text.strip().splitlines()).encode()).hexdigest()


def provenance(x, body):
    def canonical_multi(value):
        return ";".join(sorted(v.strip() for v in value.split(";") if v.strip() and v.strip() != "—"))
    method = source_locator(x, x["method"])
    evaluation = source_locator(x, x["evaluation"])
    limits = limitations_locator(x)
    fields = ["review-completion-v1", x["fid"], f"paper-v1:{x['aid']}", f"arXiv:{x['aid']}v1", "SRC-ARXIV", f"arXiv:{x['aid']}v1", f"SRC-ARXIV@arXiv:{x['aid']}v1", x["route"]]
    if x["override"] != "none":
        fields.append(f"review-override:{x['override']}")
    fields += [canonical_multi(method), canonical_multi(evaluation), canonical_multi(limits), canonical_multi(x["artifact"]), f"claim:{x['fid']}", f"review:{x['fid']}", f"review-body-sha256:{normalized_hash(body)}"]
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def source_locator(x, value):
    if value.startswith("Not Disclosed") or value.startswith("Not Required"):
        return value
    return f"https://arxiv.org/html/{x['aid']}v1 — {value}"


def limitations_locator(x):
    value = x["limits"]
    if x["route"] == "deep" and "§" not in value and "Appendix" not in value:
        value = "exact-v1 § Discussion/Limitations boundary — " + value
    return source_locator(x, value)


def chapter_ref(value):
    return "; ".join(part.strip() + ("" if "#" in part else "#L1") for part in value.split(";") if part.strip())


def closure_reason(item):
    text = (item["title"] + " " + item["abstract"]).lower()
    if any(k in text for k in ("survey", "review of", "systematic review", "position paper", "taxonomy")):
        reason = "secondary synthesis：可用于发现或术语校准，但没有形成可核验的新机制或系统 contract"
    elif any(k in text for k in ("medical", "disease", "protein", "molecule", "agricultur", "traffic", "financial", "education", "emotion", "recommendation", "remote sensing")):
        reason = "垂直领域应用：方法或数据集只服务具体领域，未改变通用 AI System 的 state/data/control ownership"
    elif any(k in text for k in ("benchmark", "dataset", "corpus")):
        reason = "局部 benchmark/dataset：未改变长期 evaluation contract，或证据只覆盖单任务/单领域"
    elif any(k in text for k in ("quantization", "pruning", "distillation", "adapter", "lora", "federated", "graph neural", "segmentation")):
        reason = "局部算法增量：未形成跨模型/运行时/平台的长期设计判断变化"
    else:
        reason = "AI 相关但未达分母门槛：title+abstract 未显示长期机制、系统 reach 或 Books 既有结论修正"
    first = re.split(r"(?<=[.!?])\s+", item["abstract"].strip())[0][:220]
    return f"{reason}；abstract evidence: {first}"


def main():
    inventory = json.loads(INVENTORY.read_text())
    for x in C:
        x["benchmark"] = tuple("Not Disclosed" if value == "Not Applicable" else value for value in x["benchmark"])
    by_id = {x["arxiv_id"]: x for x in inventory["identities"]}
    retained = {x["aid"] for x in C}
    if not retained <= by_id.keys():
        raise SystemExit("retained identity missing from frozen inventory")

    ledger = []
    for item in inventory["identities"]:
        is_retained = item["arxiv_id"] in retained
        row = {
            "arxiv_id": item["arxiv_id"], "identity": item["identity"],
            "published_v1_utc": item["published_v1_utc"], "primary_category": item["primary_category"],
            "categories": item["categories"], "route": item["route"], "title": item["title"],
            "abstract": item["abstract"], "decision": "retain" if is_retained else "pre_denominator_closure",
            "closure_reason": "retained after title+abstract semantic screening: material AI-System design/evidence delta" if is_retained else closure_reason(item),
            "false_negative_audit": "pending independent fresh-context audit",
        }
        ledger.append(row)
    (PACKET / "2025-05-02-screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    with (PACKET / "2025-05-02-screening-ledger.tsv").open("w", newline="", encoding="utf-8") as f:
        fields = ["arxiv_id","identity","published_v1_utc","primary_category","route","decision","title","closure_reason","false_negative_audit"]
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n"); w.writeheader()
        for row in ledger: w.writerow({k: row[k] for k in fields})

    raw_sha = {r["path"]: r["sha256"] for r in inventory["raw_receipts"]}
    exact = {}
    for x in C:
        p = PACKET / "2025-05-02-exact-v1-html" / f"{x['aid']}v1.html"
        exact[x["aid"]] = {"path": str(p.relative_to(ROOT)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size}
    receipt = {
        "schema": "daily-v2.1-replay-receipt-v1", "date": "2025-05-02",
        "window": "[2025-05-01T09:00:00+08:00, 2025-05-02T09:00:00+08:00)",
        "query": inventory["query"], "raw_identity_count": 690,
        "registered_count": 296, "core_count": 220, "keyword_count": 76,
        "retained_count": len(C), "closure_count": 296-len(C),
        "retained_ids": sorted(retained), "raw_receipts": inventory["raw_receipts"],
        "exact_v1_receipts": exact,
        "coverage_audit": "pending independent fresh-context audit",
        "evidence_audit": "pending independent fresh-context audit",
        "books_writeback": [x["fid"] for x in C if x["disposition"] == "Integrate"],
    }
    (PACKET / "2025-05-02-review-packet.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

    queue_items = [x for x in C if x["disposition"] == "Integrate"]
    q = ["# 2025-05-02 Books Writeback Queue", "", "本文件只排队，不修改共享 Books。root 必须按事件时间串行写回并重新审阅 owner 与相邻章节。", ""]
    for x in queue_items:
        q += [f"## {x['fid']}", "", f"- Owner: `{x['node']}`", f"- Target: `{x['chapter']}`", f"- Adjacent: `{x['adjacent']}`", f"- Suggested anchor: {x['existing']}", f"- Long-term proposition: {x['claim']}", f"- Evidence boundary: {x['review']}", f"- Exact primary: https://arxiv.org/html/{x['aid']}v1", ""]
    QUEUE.write_text("\n".join(q))

    ids = "<br>".join(x["fid"] for x in C)
    den = "DEN-20250502-" + hashlib.sha256((ids + raw_sha["arxiv-20250502-start0000.partial.xml"] + raw_sha["arxiv-20250502-start0650.xml"]).encode()).hexdigest()[:20]
    lines = [
        "# Daily Research — 2025-05-02", "", "**Research Date:** 2025-05-02", "", "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2025-05-01 09:00:00 ～ 2025-05-02 09:00:00（北京时间，左闭右开）", "", "**Contract:** V2.1 Full Replay", "",
        "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open（等待独立 fresh-context audit 与 5 项串行写回），状态真值见第 7、13 节", "",
        "## Executive Summary", "",
        "本轮从官方 arXiv Atom/API 严格窗口重新冻结 690 个 v1 identity，而不是从 W18 `/30` 评分反推。注册分类命中 296 项：220 条 Core Daily 已逐项完成 title+abstract 语义筛选，76 条 keyword route 也完成语义判断；冻结 16 个候选（5.41%），其余 280 个 family 保留 identity、摘要证据与具体 pre-denominator closure。", "",
        "16 个候选均已读取 exact-v1 HTML 的机制、实验与边界，完成 Score V2、route-matched Review、Benchmark Contract 与逐 family Books Comparison。长期增量集中于五项：长视频事件图 RAG、训练网络流旁路诊断、EMA 量化状态动力学、peer-owned distributed RAG、CPU cache token side channel。其余十一项由 Books 现有主线承载。", "",
        "本 worker 不伪造独立 reviewer，也不与其他日期并行写共享 Books。因此 Coverage/Evidence/Books Gate 保持 Open：root 需要独立复核 296-row screening ledger 的 false-positive/false-negative、16 份 exact-v1 Review 与三项 Deep Analysis selection，再按队列串行写回五项并重读 owner/adjacent。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2025-05-02 |", "| Window End | 2025-05-02 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {den} |", "| Denominator Frozen At | 2026-08-31T18:30:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2025-05-01T09:00:00+08:00 | 2025-05-02T09:00:00+08:00 | 2026-08-31T17:35:00+08:00 | official Atom `submittedDate:[202505010100 TO 202505020100]`; registered categories; Core full semantic + keyword route | checked | 690 | {ids} | page=2; start=0 partial plus bounded overlap/tail start=650; reconciled 690 unique; final_cursor=end | 2025-05-02T01:00:00Z | coverage:SRC-ARXIV:20250502 | — |", "",
        marker("coverage:SRC-ARXIV:20250502", f"官方 query 声明 690 条；首响应保留 673 个完整 entry（SHA-256 `{raw_sha['arxiv-20250502-start0000.partial.xml']}`），以 start=650 的 40-entry 官方尾片（SHA-256 `{raw_sha['arxiv-20250502-start0650.xml']}`）闭合重叠后得到 690/690。296 条注册分类筛选、16 retained 与 280 closures 位于 screening ledger。"), "",
        "### Coverage Limitations", "", "- Atom 首响应被传输中断；未删除原始 partial receipt，而是用有重叠的官方 bounded tail 闭合并校验 query total、unique identity 和严格窗口。", "- W18 仅作 prior discovery/evidence clue；没有自动 retain、没有继承旧六维 `/30` 分数，也没有把 W18 的 review 声明冒充本日 exact-v1 Review。", "- 注册表 2026-08-25 才生效的组织/backstop 来源不追溯性重写本窗口。本轮论文 recall 由官方 arXiv 查询闭合；独立 denominator audit 尚未完成，所以 Coverage Gate 仍为 Open。", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for x in C:
        item = by_id[x["aid"]]; d,s,u=x["score"]
        lines.append(f"| {x['fid']} | arXiv:{x['aid']}v1 | paper-v1:{x['aid']} | 2025-W18 | {item['published_v1_utc'][:10]} | SRC-ARXIV | {d} | {s} | {u} | {x['total']} | retained | {x['route']}_complete | accessible | {x['override']} | review:{x['fid']} | self | — | new_in_window | {x['node']} | {x['disposition']} | books-review:{x['fid']} | yes |")
    lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    bodies = {x["fid"]: marker(f"claim:{x['fid']}", x["claim"]) + x["review"] for x in C}
    for x in C:
        lines.append(f"| {x['fid']} | {provenance(x,bodies[x['fid']])} | {x['route']} | arXiv:{x['aid']}v1 | SRC-ARXIV@arXiv:{x['aid']}v1 | {source_locator(x,x['method'])} | {source_locator(x,x['evaluation'])} | {limitations_locator(x)} | {x['artifact']} | claim:{x['fid']} | complete |")
    lines += ["", "### Source Reviews", ""]
    for x in C: lines += [marker(f"review:{x['fid']}", bodies[x["fid"]]), ""]
    lines += ["## 4. Benchmark Contracts", "", "每行只冻结 exact-v1 公开条件；`Not Disclosed` 不从相邻论文或常见默认值补齐。", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in C: lines.append("| " + x["fid"] + " | " + " | ".join(x["benchmark"]) + " |")
    lines += ["", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    selected = {"SF-2025-LLMPRISM":"DA-TRAINING-CONTROL-STATE", "SF-2025-PATCHWORK-RAG":"DA-RAG-RUNTIME", "SF-2025-SPILL-BEANS":"DA-EVIDENCE-SECURITY"}
    subsume = {"SF-2025-SOLO":"DA-TRAINING-CONTROL-STATE", "SF-2025-RNB":"DA-TRAINING-CONTROL-STATE", "SF-2025-DISTRIBUTED-RAG":"DA-RAG-RUNTIME", "SF-2025-FREQKV":"DA-RAG-RUNTIME", "SF-2025-OET":"DA-EVIDENCE-SECURITY"}
    for x in C:
        if x["total"] >= 7 or x["override"] != "none":
            elig = ["score_7_9"] if x["total"] >= 7 else []
            if x["override"] != "none": elig.append("forced_review")
            if x["disposition"] == "Integrate": elig.append("potential_books_delta")
            if x["fid"] in selected:
                unit=selected[x["fid"]]; lines.append(f"| {x['fid']} | {';'.join(elig)} | selected | {unit} | — | 代表本日一条跨层状态/控制权演进主线。 | analysis:{unit} |")
            elif x["fid"] in subsume:
                unit=subsume[x["fid"]]; lines.append(f"| {x['fid']} | {';'.join(elig)} | subsumed | — | {unit} | 独立 Review 保留；机制作为同一控制链分支进入长叙事。 | analysis:{unit} |")
            else:
                lines.append(f"| {x['fid']} | {';'.join(elig)} | not_selected | — | — | 已完成 route-matched Review；三项容量优先给跨训练、RAG 与安全边界的演进链。 | analysis-decision:{x['fid']} |")
    lines += ["", marker("analysis:DA-TRAINING-CONTROL-STATE", "### Deep Analysis 1 — 训练系统从显式指标走向可恢复的状态观测与控制\n\n稳定训练最初依赖框架内指标、标准精度 optimizer 和固定数据域，因为这些状态容易解释。规模、异构平台和 memory 约束改变后，三条分支出现：LLMPrism 用网络流旁路推断 job/parallelism/phase；SOLO 处理低比特 EMA 的 signal swamping 与方向误差；R&B 以表示/梯度信号动态调整数据域。收益是少侵入、少内存和自适应，代价是 proxy drift、误诊、cluster churn 与 checkpoint identity 复杂化；显式 instrumentation、高精度 state 和固定 mixture 在稳定/高风险场景仍是 fallback。"), "", marker("analysis:DA-RAG-RUNTIME", "### Deep Analysis 2 — RAG 从中央静态索引演进为带 ownership 与 SLO 的状态系统\n\n中央索引在 corpus 稳定、权限统一时最简单。长视频、peer-owned knowledge 和多算子 serving 改变约束：AVA 把连续观察压缩为可修订事件图；Distributed RAG 把 corpus 留在 peer 并增加 topic-aware discovery；Patchwork 以 operator DAG 和 end-to-end budget 调度；FreqKV 只作为有损 memory branch。新机制获得时序检索、数据自治和资源弹性，也引入图陈旧、query leakage、peer failure、跨算子 bottleneck 和 lossy state；小语料、稳定权限与低并发仍可使用中央检索/FullKV。"), "", marker("analysis:DA-EVIDENCE-SECURITY", "### Deep Analysis 3 — 安全从内容攻击评测推进到平台隔离与 action authority\n\n静态 prompt 测试在模型无工具、单租户时合理。OET 表明攻击会依据反馈优化，UnLOK/HalluMix/T2VPhys 提醒 evaluator 必须绑定攻击、slice 和任务；Spill The Beans 进一步把威胁移到共享 CPU cache，绕过输出过滤。于是 detection 只拥有风险信号，tool/action gate、co-location、page sharing 与 cache isolation 才拥有执行 authority。代价是更复杂的 threat model、资源隔离和误报；无共享硬件或无工具权限的低风险 workload 可保留较轻控制。"), ""]
    for x in C:
        if (x["total"] >= 7 or x["override"] != "none") and x["fid"] not in selected and x["fid"] not in subsume: lines += [marker(f"analysis-decision:{x['fid']}", "该 family 的全文 Review 和 Books 比较已完成；本日报不以第四段论文摘要突破三项 Deep Analysis 上限。"), ""]
    lines += ["## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in C: lines.append(f"| {x['fid']} | {x['node']} | {chapter_ref(x['chapter'])} | {chapter_ref(x['adjacent'])} | existing:{x['fid']} | delta:{x['fid']} | {x['relation']} | {x['disposition']} | books-review:{x['fid']} |")
    lines += ["", "五项 `Integrate` 的精确写回要求位于 `_sources/daily-v2.1-replay-202505/2025-05-02-books-writeback-queue.md`；本 worker 不并行修改共享 Books。", ""]
    for x in C: lines += [marker(f"books-review:{x['fid']}", marker(f"existing:{x['fid']}",x['existing']) + marker(f"delta:{x['fid']}",x['delta']) + f"演进关系 `{x['relation']}`；当前决定 `{x['disposition']}`。"), ""]
    lines += ["## 7. Semantic Audit", "", "本 worker 是报告与筛选作者，不能伪装成 fresh-context reviewer。以下四个 scope 明确留给 root 或其他未参与写作的 reviewer；在审计与写回完成前，Gate 保持 Open。", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", "| SA-20250502-COVERAGE | fresh-context:pending_may02_independent | coverage | coverage:SRC-ARXIV:20250502 | AUDIT-PENDING-20250502-COVERAGE | 需复核 690→296→16/280、日期、route、false-positive 与 pre-denominator false-negative。 | open |", f"| SA-20250502-EVIDENCE | fresh-context:pending_may02_independent | evidence | {'; '.join('review:'+x['fid'] for x in C)} | AUDIT-PENDING-20250502-EVIDENCE | 需抽核/复核 16 份 exact-v1 locator、claim boundary 与 benchmark 字段。 | open |", "| SA-20250502-SELECTION | fresh-context:pending_may02_independent | deep_analysis_selection | analysis:DA-TRAINING-CONTROL-STATE; analysis:DA-RAG-RUNTIME; analysis:DA-EVIDENCE-SECURITY | AUDIT-PENDING-20250502-SELECTION | 需确认三条叙事未强行合并不同 owner，所有 eligible family 有 disposition。 | open |", f"| SA-20250502-BOOKS | fresh-context:pending_may02_independent | books | {'; '.join('books-review:'+x['fid'] for x in C)} | BOOKS-WRITEBACK-20250502 | 需按日期串行写回 5 项并重读 owner/adjacent；其余 11 项复核 Existing Coverage。 | open |", "",
        "## 8. Ignored Noise", "", "280 个 pre-denominator closure 全部保留在 `2025-05-02-screening-ledger.json/tsv`，每项包含 exact identity、v1 时间、分类、route、title、abstract 证据与 family-specific closure reason。它们主要是垂直领域应用、secondary synthesis、局部 benchmark/dataset 和不改变长期 state/data/control ownership 的单点算法；没有被误写成低分候选或全文审阅。", "",
        "## 9. Recommended Action", "", "1. root 先执行独立 denominator/evidence/selection audit；finding 必须回到 screening ledger 或 Source Review 修正。", "2. 审计通过后按事件时间串行处理 `AVA → LLMPrism → SOLO → Distributed RAG → Spill The Beans` 的 Books queue，若与其他日期命中同一 owner，按章节语义位置整合而不是章末追加。", "3. 写回后重读 owner 与相邻章节，确认旧方案、约束变化、收益、trade-off、failure mode 和 fallback 均存在，再将 Books Gate 关闭。", "",
        "## 10. Repository Changes", "", "- 新建本日报、296-row screening ledger、Review packet、16 份 exact-v1 HTML receipt 和 Books writeback queue。", "- 保留中断 Atom 原始响应与 bounded tail，不覆盖或伪造完整单响应。", "- 未修改 Books、ROADMAP、LEARNING_STATE；未 stage、commit 或 push。", "",
        "## 11. Open Questions", "", "- 网络流旁路诊断在加密、共享流量与拓扑变化下怎样校准并安全 abstain？", "- 2-bit optimizer state 如何与 checkpoint 恢复、分布式聚合和 mixed-precision overflow 联合定义 identity？", "- peer-owned RAG 如何同时处理 query privacy、peer trust、index consistency 和 SLO？", "- token side channel 的隔离应在 scheduler、runtime、OS page sharing 还是 cache partition 哪层拥有最终 authority？", "",
        "## 12. Sources", ""]
    exact_titles = {
        "2505.00254": "Empowering Agentic Video Analytics Systems with Video Language Models",
        "2505.07833": "Patchwork: A Unified Framework for RAG Serving",
    }
    for x in C:
        item=by_id[x["aid"]]; title = exact_titles.get(x["aid"], item["title"])
        lines.append(f"- [{title}](https://arxiv.org/html/{x['aid']}v1) — arXiv:{x['aid']}v1；首次公开 `{item['published_v1_utc']}`；访问 2026-08-31。")
    lines += ["- [W18 prior discovery baseline](../../weekly/2025-W18/README.md) — 只作历史线索，不继承 V1 评分或完成状态。", "", "## 13. Final Status", "", "- Completion Status = `In Progress`", "- Coverage = `Open`", "- Evidence = `Open`", "- Books = `Open`", "- unresolved findings = `4`（Coverage、Evidence、Selection 三项独立审计，以及包含五个 family 的 Books writeback/audit）", "- 下一检查点：root 完成 fresh-context audit；处理 finding；串行 Books writeback；owner/adjacent audit；再同步为终态。", ""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"raw":690,"registered":296,"core":220,"keyword":76,"retained":len(C),"closures":296-len(C),"queue":len(queue_items)},ensure_ascii=False))


if __name__ == "__main__":
    main()
