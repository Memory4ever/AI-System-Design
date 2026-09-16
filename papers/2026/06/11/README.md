# Daily Research — 2026-06-11

**规范：** V3  
**窗口：** 2026-06-10T09:00:00+08:00 ～ 2026-06-11T09:00:00+08:00  
**状态：** 完成
**Books：** 纳入本次  
**检查时间：** 2026-09-11T12:45:00+08:00

## 1. 结论

对本目录 bounded canonical raw bucket 的全部 562 个 identity 已完成 title + complete abstract 准入审计；fresh-context 独立复核将 2 个误收项改为分母前关闭，最终冻结 52 个 Candidate、510 个 family-specific audited Close，满足 `562 raw = 52 Candidate + 510 audited Close`，ordinary pending=0。候选 exact-v1 Evidence Review 与 Books 比较也已独立复核：10 项确有正文增量并已写入 Books，40 项由现有章节覆盖，2 项仅报告。10 条正文均位于首个顶层 `Review notes` 前，具备机制、owner、收益、trade-off、failure、fallback 与证据边界；7 条 trace 日期修正已复验，剩余执行队列为 0。日期 owner 不由 submitted/v1 timestamp、identifier sequence、DataCite created 或 normal cutoff 推导；official historical listing receipt 到位前不执行跨日迁移，该保留限制不阻塞本日报闭环。

当前合同评分已由非作者重新校准，不以已经深读或已经写入 Books 倒推高分。52 项现在分布为 `5 分 × 2、6 分 × 40、8 分 × 10`；既有 exact-v1 深审仍可复用，最低审阅等级按新分数表述。逐项旧分、新分和三维依据见 [current score recalibration](../_sources/daily-20260611/CURRENT_SCORE_RECALIBRATION_20260914.json)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ANTHROPIC | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-GOOGLE-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-META-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-QWEN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-DEEPSEEK | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MOONSHOT | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ZAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MINIMAX | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ARXIV | [official listing owner audit](../_sources/daily-20260611/official-arxiv-announcement-owner-audit-v3.json) 记录 bounded raw bucket 562 项并撤回 schedule-derived migration；逐项 exact-v1 title + complete abstract；候选核对 exact-v1 HTML/PDF 的方法、评价与 limitations/non-proof | 已检查 | historical listing receipt 待补；未据此迁移 |

全量判定见 [`v3-reverse-admission-audit-20260910.json`](../_sources/daily-20260611/v3-reverse-admission-audit-20260910.json) 与 [`denominator-full-semantic-audit-v1.tsv`](../_sources/daily-20260611/denominator-full-semantic-audit-v1.tsv)。关闭理由绑定各自 exact-v1 题目与完整摘要中的问题/方法证据，不按关键词、学科标签、ROADMAP 映射或共享模板关闭；owner audit 明确保留 historical listing proof 缺口，不把 DataCite registration、submitted time 或正常 cutoff 推算当公开时刻。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference](https://arxiv.org/html/2606.11196v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference》关闭或降池；完整摘要显示“We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content](https://arxiv.org/html/2606.11198v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content》关闭或降池；完整摘要显示“We develop a formal framework decomposing attention scores into semantic and structural components (Eq.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文写入与独立 post-write audit 已完成 |
| [Beyond Compaction: Structured Context Eviction for Long-Horizon Agents](https://arxiv.org/html/2606.11213v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Beyond Compaction: Structured Context Eviction for Long-Horizon Agents》关闭或降池；完整摘要显示“We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon.”。该增量直接改变 AGENT-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[owner](../../../../books/part-07-agent/75-context.md)；正文锚点：Context Compression 必须保留执行状态，而不只是语义 |
| [SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving](https://arxiv.org/html/2606.11244v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving》关闭或降池；完整摘要显示“We present SPEAR, a system for post-quantization error-adaptive recovery that improves low-bit LLM serving.”。该增量直接改变 INFER-TENSORRT-LLM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文写入与独立 post-write audit 已完成 |
| [When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines](https://arxiv.org/html/2606.11265v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Based on this observation, we propose Chunk-aware and Rerank-Consistent Poisoning (CRCP), a poisoning framework that jointly optimizes retrieval relevance, reranker consistency, and chunk-boundary robustness.”，该机制在 AGENT-RAG 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation](https://arxiv.org/html/2606.11270v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“While qualitative evidence supports the existence of this effect, its magnitude has not been systematically characterized.”，该机制在 TRAIN-DATA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse](https://arxiv.org/html/2606.11290v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To this end, we present FlowBank, a three-stage framework for portfolio-based agentic workflow optimization.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents](https://arxiv.org/html/2606.11349v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Rather than treating clarification as an external uncertainty trigger, we propose ACTION-RATING, a formulation that places it inside the agent's action space on a shared ordinal scale with navigation, so that asking competes directly with acting at every decision point and help-seeking becomes observable at intermediate states.”，该机制在 AGENT-PLANNING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：从目标到状态图 |
| [When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval](https://arxiv.org/html/2606.11350v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval》关闭或降池；完整摘要显示“To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：Online Retrieval Pipeline |
| [TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs](https://arxiv.org/html/2606.11357v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this work, we present TileFuse, a close-to-metal mixed-precision kernel library for AMD XDNA2 NPUs that targets GEMM/GEMV-based operators in quantized LLM inference.”，该机制在 INFER-DECODE 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-DECODE，[owner](../../../../books/part-05-inference-system/44-decode.md)；正文锚点：端侧融合必须围绕真实 Tile / Dataflow Contract |
| [When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis](https://arxiv.org/html/2606.11375v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis》关闭或降池；完整摘要显示“We introduce fragility, a complementary per-layer metric defined as the activation-noise level at which probe accuracy collapses.”。该增量直接改变 TRAIN-PRETRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；正文写入与独立 post-write audit 已完成 |
| [Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining](https://arxiv.org/html/2606.11387v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We study an auditable staged-promotion protocol for a fixed micro-pretraining runner on two heterogeneous host blocks: Windows A100 and Linux L40S.”，该机制在 TRAIN-PRETRAINING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；正文锚点：Scaling-law Pilot 也是有预算的实验调度 |
| [Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models](https://arxiv.org/html/2606.11409v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose a compute-aware evaluation framework based on computational pressure, measured in cumulative floating-point operations (FLOPs), as a proxy for adversarial effort.”，该机制在 PLATFORM-EVALUATION-SYSTEM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Signed Compression Progress on a Sealed Audit is Goodhart-Resistant](https://arxiv.org/html/2606.11417v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Signed Compression Progress on a Sealed Audit is Goodhart-Resistant》关闭或降池；完整摘要显示“The folk claim is that this reward is "credible" because it is paid only for learning.”。该增量直接改变 TRAIN-RLHF 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-RLHF，[owner](../../../../books/part-04-training-system/31-rlhf.md)；正文写入与独立 post-write audit 已完成 |
| [INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration](https://arxiv.org/html/2606.11440v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration》关闭或降池；完整摘要显示“We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文写入与独立 post-write audit 已完成 |
| [Forecasting Future Behavior as a Learning Task](https://arxiv.org/html/2606.11445v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Forecasting Future Behavior as a Learning Task》关闭或降池；完整摘要显示“We propose an alternative that bypasses the explanation step: treat behavior forecasting as a learnable task and train Behavior Forecasters that operates on a single reasoning trajectory to make the same forecasts one would typically seek from an explanation.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/html/2606.11520v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose ISE (Intent -> Simulate -> Execute), a three-stage synthesis paradigm that addresses these gaps jointly.”，该机制在 TRAIN-DATA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/html/2606.11543v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present SkillJuror, a framework for evaluating Skill writing paradigms through semantically controlled variants, matched multi-trial evaluations, and trajectory evidence while holding task knowledge fixed.”，该机制在 AGENT-REFLECTION 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-REFLECTION，[owner](../../../../books/part-07-agent/80-reflection.md)；正文锚点：Reflection 应输出可执行诊断 |
| [Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference](https://arxiv.org/html/2606.11592v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference》关闭或降池；完整摘要显示“We propose an information-theoretic defense framework for prompt inversion in collaborative LLM inference.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure](https://arxiv.org/html/2606.11632v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“This paper introduces the Sovereign Assurance Boundary (SAB), a certificate-bound runtime admission layer for autonomous execution authority.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security](https://arxiv.org/html/2606.11671v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Runtime Skill Audit (RSA), a dynamic analysis method that audits skills by asking what the skill-mediated agent actually does under targeted runtime conditions.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents](https://arxiv.org/html/2606.11680v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents》关闭或降池；完整摘要显示“In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/html/2606.11686v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present layer-isolated evaluation: a deployed ordering agent is decomposed into a fixed taxonomy of layers (ontology, intent, routing, decomposition, escalation, safety, memory, and cross-cutting envelope/defense), each exercised by its own assertion slice in a deterministic, no-LLM "pure" mode.”，该机制在 PLATFORM-EVALUATION-SYSTEM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents](https://arxiv.org/html/2606.11688v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Autopilot, an execution model that makes silent fabricated success structurally impossible rather than merely rarer.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation](https://arxiv.org/html/2606.11690v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose a measurement methodology that parameterizes the relationship as C_eff = f(H, M, Q, lambda, L), validate it with 42 benchmarks across dense, ultra-sparse MoE, and sparse MoE models, and release vllm-cost-meter, an open-source cost meter that attaches to a live vLLM server and reports real \$/M-tokens against the operator's own traffic.”，该机制在 PLATFORM-COST 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-COST，[owner](../../../../books/part-06-ai-infrastructure/70-cost.md)；正文锚点：Utilization 应由实际负载推出，而不是由计算器假定 |
| [Substrate Asymmetry in User-Side Memory: A Diagnostic Framework](https://arxiv.org/html/2606.11712v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Substrate Asymmetry in User-Side Memory: A Diagnostic Framework》关闭或降池；完整摘要显示“We show this aggregate metric hides opposite-direction failures.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs](https://arxiv.org/html/2606.11718v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose Chiplet-Contiguous Layout, a global memory layout that stores chiplet-local data contiguously.”，该机制在 INFER-GPU-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-GPU-MEMORY，[owner](../../../../books/part-05-inference-system/54-gpu-memory.md)；正文锚点：Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页 |
| [External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs](https://arxiv.org/html/2606.11806v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“It is how different serving strategies trade off quality against online cost under realistic constraints.”，该机制在 AGENT-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code](https://arxiv.org/html/2606.11817v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code》关闭或降池；完整摘要显示“To address this vulnerability, we propose CodeShield, a safety alignment approach that robustly preserves safe behavior even under attacker-controlled grammar constraints.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning](https://arxiv.org/html/2606.11853v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning》关闭或降池；完整摘要显示“We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training](https://arxiv.org/html/2606.11867v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training》关闭或降池；完整摘要显示“We introduce ForeMoE, a micro-step-level load balancing system for MoE RL post-training.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：Expert Placement 与 Sample Packing 可以共享 Rollout Routing State |
| [WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries](https://arxiv.org/html/2606.11871v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present WarpGuard, to our knowledge the first protected-site CFI system for CUDA device binaries operating on executed SASS.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision](https://arxiv.org/html/2606.11878v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Such decisions depend not only on computed values, but also on which lanes are represented, what evidence they contribute, which lane speaks for the group, and which checked state reaches commit.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Characterizing Software Aging in GPU-Based LLM Serving Systems](https://arxiv.org/html/2606.11916v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Traditional aging studies focus on CPU-centric software with relatively regular workloads; LLM serving is different, spanning a Python host and a CUDA device, handling requests whose cost varies by orders of magnitude, and relying on rapidly evolving software stacks.”，该机制在 PLATFORM-MONITORING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点：条件化机制分支与共存边界 |
| [Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers](https://arxiv.org/html/2606.11949v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Adversarial inputs require $3.3\times$ more reasoning tokens than benign inputs to produce valid safety scores ($T_{50,\text{adv}}{=}154$ vs. $T_{50,\text{benign}}{=}46$ for o3), so low-budget deployments silently starve the monitor on exactly the inputs it must catch.”，该机制在 PLATFORM-MONITORING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点：条件化机制分支与共存边界 |
| [Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/html/2606.11998v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce \emph{bootstrapped monitoring}, a protocol that addresses this by inserting a stronger, intermediate untrusted model with transparent chain-of-thought reasoning into the oversight chain.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents](https://arxiv.org/html/2606.12087v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents》关闭或降池；完整摘要显示“We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path](https://arxiv.org/html/2606.12154v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 1 + 2 = 5；原筛选把《The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path》关闭或降池；完整摘要显示“That result solved a placement problem and immediately exposed a different one: even correctly placed, the large model needed roughly four seconds to answer, because it was still being invoked at every query.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 仅报告：INFER-PREFILL；exact-v1 尚不足以授权长期 Books 正文变化 |
| [A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs](https://arxiv.org/html/2606.12160v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs》关闭或降池；完整摘要显示“However, modern instruction-tuned LLMs already achieve substantially higher baselines (61-76%), raising the question of whether these methods remain effective in practice.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps](https://arxiv.org/html/2606.12212v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps》关闭或降池；完整摘要显示“We present the first in-depth empirical study of API key leakage in LLM-integrated apps.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study](https://arxiv.org/html/2606.12231v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study》关闭或降池；完整摘要显示“Despite their role in aligning AI behavior with developer intent, the taxonomy, evolution, and practical impact of these rules remain largely unexplored.”。该增量直接改变 AGENT-PROMPT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PROMPT，[owner](../../../../books/part-07-agent/74-prompt.md)；正文锚点：Prompt 生命周期 |
| [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/html/2606.12243v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose Verification via Intra-Model Routing for Speculative Decoding (VIA-SD), a multi-tier framework using a routed slim-verifier.”，该机制在 INFER-SPECULATIVE-DECODING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点：Correctness owner 没有改变 |
| [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/html/2606.12320v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；五平面、stop-anywhere mediation、capability attenuation 与 structured audit 属于范围内架构证据，但对 owner 章节的逐段比较表明这些原则已由 effect-time authorization、delegation-chain attenuation、跨通道 influence graph 与 evidence chain 承载。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；不把参考架构 taxonomy 重写为第二套正文 |
| [PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/html/2606.12329v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present projectmem, an open-source, local-first memory and judgment layer for AI coding agents. projectmem records development as an append-only, plain-text event log of typed events - issues, attempts, fixes, decisions, and notes - and deterministically projects that log into compact, AI-readable summaries served through the Model Context Protocol (MCP).”，该机制在 AGENT-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents](https://arxiv.org/html/2606.12341v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents》关闭或降池；完整摘要显示“We recast agent privacy as \emph{posterior-risk control} and present OCELOT, a runtime mediator that budgets how much an adversary's belief about a secret may improve across a trajectory, rather than filtering outputs.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing](https://arxiv.org/html/2606.12342v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 1 + 2 = 5；原筛选把《ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing》关闭或降池；完整摘要显示“We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 仅报告：PLATFORM-SECURITY；exact-v1 尚不足以授权长期 Books 正文变化 |
| [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/html/2606.12344v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks》关闭或降池；完整摘要显示“We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [On Subquadratic Architectures: From Applications to Principles](https://arxiv.org/html/2606.12364v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《On Subquadratic Architectures: From Applications to Principles》关闭或降池；完整摘要显示“To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics.”。该增量直接改变 MODEL-LONG-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；正文锚点：方案究竟移动了哪个瓶颈 |
| [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/html/2606.12370v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To address this bottleneck, we present Bebop, a systematic study of MTP in LLM post-training, and offer practical recipes to integrate MTP into large-scale RL pipelines.”，该机制在 INFER-SPECULATIVE-DECODING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点：Correctness owner 没有改变 |
| [Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization](https://arxiv.org/html/2606.12373v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization》关闭或降池；完整摘要显示“While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文写入与独立 post-write audit 已完成 |
| [APPO: Agentic Procedural Policy Optimization](https://arxiv.org/html/2606.12384v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《APPO: Agentic Procedural Policy Optimization》关闭或降池；完整摘要显示“Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；正文锚点：从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 |
| [Doc-to-Atom: Learning to Compile and Compose Memory Atoms](https://arxiv.org/html/2606.12400v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Doc-to-Atom: Learning to Compile and Compose Memory Atoms》关闭或降池；完整摘要显示“To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文写入与独立 post-write audit 已完成 |

## 4. 证据与知识整合

### [PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference](https://arxiv.org/html/2606.11196v1)

**问题与机制。** 原筛选把《PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference》关闭或降池；完整摘要显示“We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 PoQ-Judge: Reference-Free Evaluation Framework; 3.1 Judge Model Architectures`；可采用的最小机制命题是：We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references.

**Evaluation proof。** `2.2 The Reference-Free Evaluation Gap; 3 PoQ-Judge: Reference-Free Evaluation Framework; 3.5 Cascade Evaluation Protocol`；exact-v1 披露：Decentralized LLM inference networks need lightweight, reference-free quality evaluation for Proof of Quality (PoQ).

**Limitations / non-proof。** `6 Discussion`；We also show that online calibration identifies semantic quality as the dominant dimension and that cascade evaluation reduces cost by 72.7 percent with only modest quality loss. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content](https://arxiv.org/html/2606.11198v1)

**问题与机制。** 原筛选把《The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content》关闭或降池；完整摘要显示“We develop a formal framework decomposing attention scores into semantic and structural components (Eq.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 The Structural Attention Tax Framework; 4 Methodology`；可采用的最小机制命题是：We develop a formal framework decomposing attention scores into semantic and structural components (Eq.

**Evaluation proof。** `4.1 Experimental Design; 5 Results; Appendix A Experimental Setup and Validation`；exact-v1 披露：We derive five structure-aware mitigation strategies from the framework, ranging from zero-cost prompt modifications to training-time regularisation; format flattening (S3) is validated by both accuracy and attention-level evidence from a verbalized-triple control, while structural dispersal (S1) yields mixed results that illuminate the challenges of format-level intervention.

**Limitations / non-proof。** `7 Discussion; 8 Limitations`；We derive five structure-aware mitigation strategies from the framework, ranging from zero-cost prompt modifications to training-time regularisation; format flattening (S3) is validated by both accuracy and attention-level evidence from a verbalized-triple control, while structural dispersal (S1) yields mixed results that illuminate the challenges of format-level intervention. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-RAG` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `Retrieval Format 也是输入身份` 已完成写入并通过独立 post-write audit。

### [Beyond Compaction: Structured Context Eviction for Long-Horizon Agents](https://arxiv.org/html/2606.11213v1)

**问题与机制。** 原筛选把《Beyond Compaction: Structured Context Eviction for Long-Horizon Agents》关闭或降池；完整摘要显示“We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon.”。该增量直接改变 AGENT-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Architecture; 6.2 Evaluation Methodology`；可采用的最小机制命题是：We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon.

**Evaluation proof。** `6 Empirical Evaluation; 6.2 Evaluation Methodology; 6.3 Results`；exact-v1 披露：We describe the annotation protocol, the episode graph, the eviction policy, and the token-accounting loop, and evaluate CWL on long-horizon agentic benchmarks: a single agent session completing 89 sequential tasks across 80 million tokens with no measurable degradation in task accuracy relative to per-task isolated sessions

**Limitations / non-proof。** `7 Limitations and Open Questions`；Compared to summarization-based compaction, CWL avoids four well-known limitations: unpredictable lossiness, destruction of causal structure, blocking model cost, and compression-induced hallucination. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-CONTEXT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/75-context.md`，Review notes 前正文锚点 `Context Compression 必须保留执行状态，而不只是语义` 已承载长期命题；source 仅作受限证据。

### [SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving](https://arxiv.org/html/2606.11244v1)

**问题与机制。** 原筛选把《SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving》关闭或降池；完整摘要显示“We present SPEAR, a system for post-quantization error-adaptive recovery that improves low-bit LLM serving.”。该增量直接改变 INFER-TENSORRT-LLM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.2 SPEAR Framework; Appendix B Method Configuration`；可采用的最小机制命题是：We present SPEAR, a system for post-quantization error-adaptive recovery that improves low-bit LLM serving.

**Evaluation proof。** `5 Evaluation; 5.2 Algorithmic Quality Recovery Results; 5.3 Deployment System Results`；exact-v1 披露：Across challenging per-channel quantization settings, SPEAR recovers 56-75% of the perplexity gap between W4 and FP16 while adding less than 1% model memory overhead and maintaining latency comparable to a widely used 4-bit serving deployment.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；SPEAR introduces lightweight Error Compensators (ECs) modulated by per-token gates and places them only at the most error-sensitive layers identified through a CKA-guided entropy-aware diagnostic. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-TENSORRT-LLM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-05-inference-system/49-tensorrt-llm.md`，Review notes 前正文锚点 `Post-quantization Recovery 必须同时通过质量与执行 Gate` 已完成写入并通过独立 post-write audit。

### [When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines](https://arxiv.org/html/2606.11265v1)

<!-- claim:SF-2026-ARXIV-2606-11265:start -->
`When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11265v1`：Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection.

机制与 owner：Evaluate corpus poisoning after the real chunking and reranking pipeline, distinguishing retrieval exposure from whether the generator follows a poisoned chunk. 状态/数据/控制 owner 固定为 `AGENT-RAG`；Method 锚点是 `§IV Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§V Experiment` 只证明 `Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Attack success depends on retriever, chunk and generator settings; a failed poison under one pipeline does not certify the corpus or other retrieval depths. 反证/外推边界在 `§III Threat Model and §VI Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11265:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `RAG 安全必须覆盖完整状态生命周期` 已承载长期命题；source 仅作受限证据。

### [Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation](https://arxiv.org/html/2606.11270v1)

<!-- claim:SF-2026-ARXIV-2606-11270:start -->
`Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11270v1`：Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning.

机制与 owner：Measure subliminal behavior transfer through distillation as a ratio conditioned on teacher behavior and student response rather than treating matching outputs as benign data. 状态/数据/控制 owner 固定为 `TRAIN-DATA`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments and Results` 只证明 `Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning.` 上、`Llama-2-7B-Chat and Qwen2.5-7B-Instruct teachers/students; GPT-4.1 evaluator` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Observed transfer ratios are model/task specific and do not identify every causal feature; data lineage and behavioral canaries must coexist with aggregate metrics. 反证/外推边界在 `§5 Analysis and §6 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11270:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse](https://arxiv.org/html/2606.11290v1)

<!-- claim:SF-2026-ARXIV-2606-11290:start -->
`FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11290v1`：Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off.

机制与 owner：Precompute reusable workflow fragments into a bank and choose them per query, separating expensive workflow search from repeated online execution. 状态/数据/控制 owner 固定为 `AGENT-WORKFLOW`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off.` 上、`Qwen3-8B FlowBank optimizer; GPT-4o and Qwen3-8B optimizer baselines` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A stale bank can reuse the wrong flow and query adaptation still needs validation; unconstrained online search remains the fallback for novel tasks. 反证/外推边界在 `Appendix F.1 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11290:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents](https://arxiv.org/html/2606.11349v1)

<!-- claim:SF-2026-ARXIV-2606-11349:start -->
`Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11349v1`：In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information.

机制与 owner：Make clarification a self-gated action competing with navigation on the same ordinal scale so information-seeking becomes an observable policy decision. 状态/数据/控制 owner 固定为 `AGENT-PLANNING`；Method 锚点是 `§3 Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–5 Experiments and Results` 只证明 `In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The measured shift depends on benchmark information gaps and answer-channel quality; asking more questions is not itself evidence of better deployment behavior. 反证/外推边界在 `§6 Discussion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11349:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `从目标到状态图` 已承载长期命题；source 仅作受限证据。

### [When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval](https://arxiv.org/html/2606.11350v1)

**问题与机制。** 原筛选把《When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval》关闭或降池；完整摘要显示“To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Architecture: MASDR-RAG and Hybrid-Routed`；可采用的最小机制命题是：To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks.

**Evaluation proof。** `5 Evaluation: Proprietary Stack`；exact-v1 披露：Our results indicate that domain scoping using organizational metadata is the key fix, significantly improving P@10 from 0.77 to 0.86 ($p < 0.05$).

**Limitations / non-proof。** `11 Discussion: Scope vs. Orchestration; Limitations`；To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-RAG` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `Online Retrieval Pipeline` 已承载长期命题；source 仅作受限证据。

### [TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs](https://arxiv.org/html/2606.11357v1)

<!-- claim:SF-2026-ARXIV-2606-11357:start -->
`TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11357v1`：With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets.

机制与 owner：Fuse mixed-precision quantized LLM operators around AMD NPU tile/dataflow constraints instead of composing generic kernels with repeated layout conversion. 状态/数据/控制 owner 固定为 `INFER-DECODE`；Method 锚点是 `§4 TileFuse Overview`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Evaluation` 只证明 `With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets.` 上、`Gemma 2B and Qwen2.5 3B end-to-end LLM workloads` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Kernel gains are bound to the evaluated AMD NPU and quantization formats; unsupported shapes and quality effects require fallback kernels and model-level checks. 反证/外推边界在 `§6 Discussion and Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11357:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/44-decode.md`，Review notes 前正文锚点 `端侧融合必须围绕真实 Tile / Dataflow Contract` 已承载长期命题；source 仅作受限证据。

### [When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis](https://arxiv.org/html/2606.11375v1)

<!-- claim:SF-2026-ARXIV-2606-11375:start -->
`When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11375v1`：Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy.

机制与 owner：Add perturbation fragility after linear-probe accuracy saturates, so pretraining checkpoints with equal separability can still be distinguished by representation stability. 状态/数据/控制 owner 固定为 `TRAIN-PRETRAINING`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Results` 只证明 `Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy.` 上、`OLMo-2 1B and OLMo-3 7B checkpoints` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Fragility depends on probe, perturbation and layer choice and is not a training objective by itself; downstream evaluation still owns usefulness. 反证/外推边界在 `§5.3 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11375:end -->

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/28-pretraining.md`，Review notes 前正文锚点 `Probe 饱和后，Fragility 只能补充诊断` 已完成写入并通过独立 post-write audit。

### [Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining](https://arxiv.org/html/2606.11387v1)

<!-- claim:SF-2026-ARXIV-2606-11387:start -->
`Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11387v1`：Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets.

机制与 owner：Use small controlled pretraining experiments as promotion receipts before expensive runs, with explicit continuation/stop decisions instead of scaling every hypothesis. 状态/数据/控制 owner 固定为 `TRAIN-PRETRAINING`；Method 锚点是 `§4.3–4.4 Promotion Schedule and Frozen Rules`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Results` 只证明 `Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Micro-scale rank order can invert at scale and cheap experiments omit distributed effects; staged promotion reduces decision cost but cannot guarantee final-model quality. 反证/外推边界在 `§7 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11387:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/28-pretraining.md`，Review notes 前正文锚点 `Scaling-law Pilot 也是有预算的实验调度` 已承载长期命题；source 仅作受限证据。

### [Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models](https://arxiv.org/html/2606.11409v1)

<!-- claim:SF-2026-ARXIV-2606-11409:start -->
`Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11409v1`：Adversarial robustness evaluations of large language models (LLMs) typically report attack success rate (ASR) under fixed query budgets, implicitly treating all attacks as equally costly.

机制与 owner：Parameterize adversarial risk by cumulative attack FLOPs and report risk-compute curves, not only success at an equal query count. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§2 Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§3–4 Experimental Setup and Results` 只证明 `Three attack strategies on two jailbreak benchmarks, re-parameterized by cumulative FLOPs` 上、`Ten models across three families and four training/alignment stages` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Risk-compute curves are evaluation objects, not service SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：FLOPs omit hardware, latency and monetary factors and attacker strategies can transfer; it is a comparable pressure proxy, not a production security SLO. 反证/外推边界在 `§7 Future Work & Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11409:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Signed Compression Progress on a Sealed Audit is Goodhart-Resistant](https://arxiv.org/html/2606.11417v1)

**问题与机制。** 原筛选把《Signed Compression Progress on a Sealed Audit is Goodhart-Resistant》关闭或降池；完整摘要显示“The folk claim is that this reward is "credible" because it is paid only for learning.”。该增量直接改变 TRAIN-RLHF 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§§3–6 sealed-audit setup, telescoping guarantee and scheduler separation`；可采用的最小机制命题是：The folk claim is that this reward is "credible" because it is paid only for learning.

**Evaluation proof。** `§7 Experiments; §8 Lean 4 mechanization`；exact-v1 披露：Experiments confirm the theory: finite-audit deviation scales as n^{-0.527}; signed progress resists clip-farming, stream leakage, and noisy-TV curiosity; naive reusable audits are exploitable by black-box scalar feedback, while standard release defenses keep the attack below the 2 Delta_n threshold.

**Limitations / non-proof。** `§5 Where the theorem breaks; §10 Limitations`；The folk claim is that this reward is "credible" because it is paid only for learning. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-RLHF` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/31-rlhf.md`，Review notes 前正文锚点 `Learning Progress Reward 必须绑定 Sealed Audit` 已完成写入并通过独立 post-write audit。

### [INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration](https://arxiv.org/html/2606.11440v1)

**问题与机制。** 原筛选把《INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration》关闭或降池；完整摘要显示“We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Problem Formulation; 4 Method`；可采用的最小机制命题是：We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware.

**Evaluation proof。** `5 Experiments; 5.2 Main Results`；exact-v1 披露：Across five benchmarks, INFRAMIND delivers up to +7.6 pp accuracy over the prior baseline at low load with up to 7x lower latency, and sustains up to 99.9% SLO compliance under high load where every baseline drops below 50%.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；However, these methods do not consider the runtime state of the serving infrastructure. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-SCHEDULING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Infrastructure-aware Multi-Agent Orchestration 必须消费同一状态` 已完成写入并通过独立 post-write audit。

### [Forecasting Future Behavior as a Learning Task](https://arxiv.org/html/2606.11445v1)

<!-- claim:SF-2026-ARXIV-2606-11445:start -->
`Forecasting Future Behavior as a Learning Task` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11445v1`：Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs.

机制与 owner：Train a single-pass behavior forecaster directly on reasoning trajectories to predict rerun stability and response changes without pretending the trace is a faithful explanation. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§3 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–5 evaluation and ablation` 只证明 `Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs.` 上、`OLMo-3-7B-Think and Qwen3.5-2B target LRMs; GPT-5.4 and Claude Opus 4.6 naive readers` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Forecast accuracy is limited to trained behavior questions and model distributions; a forecaster predicts outcomes but does not explain causes or authorize actions. 反证/外推边界在 `§7 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11445:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `行为预测是独立 Evaluation Task，不是解释的副产品` 已完成写入并通过独立 post-write audit。

### [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/html/2606.11520v1)

<!-- claim:SF-2026-ARXIV-2606-11520:start -->
`ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11520v1`：Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets.

机制与 owner：Synthesize OS-agent data through structured intent, role-locked multi-turn simulation and execution of every tool call in an isolated live workspace. 状态/数据/控制 owner 固定为 `TRAIN-DATA`；Method 锚点是 `§4 ISE Synthesis Paradigm`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Experiments` 只证明 `Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets.` 上、`Qwen3-8B fine-tuned model; Qwen3-8B, Qwen3-32B, and GPT-4o references` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A generated intent distribution and one workspace image can miss real-user states; execution grounding proves tool effects in that sandbox, not external safety. 反证/外推边界在 `§6 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11520:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/html/2606.11543v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。

**State / data / control owner。** `AGENT-REFLECTION` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11543v1 §4 Experiments; §4.1 setup; §§4.2–4.5` 支持 `82 SkillsBench tasks × 3 conditions × 5 trials`；模型 `GPT-5.4 high reasoning`；硬件 `Not Disclosed — hosted runtime hardware is not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11543v1 §3 Method; §§3.2–3.4 controlled variants/runtime evidence`；counterevidence locator：`arXiv:2606.11543v1 §6 Limitations; Appendix E layout sensitivity`。

**Trade-off / failure / coexistence / evolution。** 按需资源降低入口负担但可能产生 fanout tax；精确格式、阈值或长 artifact pipeline 仍适合 flat/local instructions。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11543:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11543v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11543:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/80-reflection.md`，Review notes 前正文锚点 `Reflection 应输出可执行诊断` 已承载长期命题；source 仅作受限证据。

### [Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference](https://arxiv.org/html/2606.11592v1)

**问题与机制。** 原筛选把《Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference》关闭或降池；完整摘要显示“We propose an information-theoretic defense framework for prompt inversion in collaborative LLM inference.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method: Privacy-Preserving Collaborative Inference; 3.2 Privacy Adapter Architecture`；可采用的最小机制命题是：We propose an information-theoretic defense framework for prompt inversion in collaborative LLM inference.

**Evaluation proof。** `6 Experimental Evaluation; 6.1 Experimental Setup; 6.2 Main Results: Privacy-Utility Tradeoff and Bottleneck Ablation`；exact-v1 披露：Extensive experiments across multiple settings demonstrate that our method achieves superior privacy-utility-latency tradeoffs compared to existing defenses (up to 35% reduction in attack success), providing a principled foundation for private and efficient collaborative LLM inference.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Existing defenses rely largely on heuristic perturbations or empirical tuning, offering limited theoretical understanding of privacy leakage and its interaction with utility and latency constraints. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure](https://arxiv.org/html/2606.11632v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11632v1 §7 Evaluation Methodology and Targets; §7.3 setup` 支持 `500 contracts × five trials; 2,500 admissions`；模型 `Go SAB prototype, OPA, PostgreSQL ledger, three-validator SQA`；硬件 `Single-node local workstation; exact CPU/GPU not disclosed`；精度 `Not applicable — control-plane prototype`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11632v1 §§3–5 SAB model, airlock and broker`；counterevidence locator：`arXiv:2606.11632v1 §9 Discussion and Limitations; §9.2`。

**Trade-off / failure / coexistence / evolution。** 证书化增加 admission latency 和 TCB；证据陈旧、policy/validator 漂移或 emergency bypass 会破坏保证，IAM 仍保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11632:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11632v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11632:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security](https://arxiv.org/html/2606.11671v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11671v1 §5 Evaluation` 支持 `100 OpenClaw skills with static baselines and evolving attacks`；模型 `LLM-assisted profiler/task generator/trace judge; exact models not fully disclosed`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11671v1 §3 Runtime Skill Audit; §4 implementation`；counterevidence locator：`arXiv:2606.11671v1 §7 Limitations`。

**Trade-off / failure / coexistence / evolution。** 动态探测覆盖 context-dependent behavior，却不穷尽 trigger；模型化 task/judge 会漂移，静态扫描仍是廉价第一层。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11671:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11671v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11671:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents](https://arxiv.org/html/2606.11680v1)

**问题与机制。** 原筛选把《Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents》关闭或降池；完整摘要显示“In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information.

**Evaluation proof。** `5 Experiments; 5.1 Experimental Setup; 5.2 Main Results`；exact-v1 披露：Compared to existing methods, it consistently achieves better efficiency-performance trade-offs and generalizes effectively to unseen tasks.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Compared to existing methods, it consistently achieves better efficiency-performance trade-offs and generalizes effectively to unseen tasks. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/html/2606.11686v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11686v1 §4 Evaluation; controlled regression injection` 支持 `238 cases across 23 slices; seven injected regressions; two tenants`；模型 `No-LLM deterministic ordering-agent scaffold`；硬件 `Not Disclosed`；精度 `Not applicable — deterministic harness`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11686v1 §3 Layer-Isolated Evaluation; taxonomy and pure mode`；counterevidence locator：`arXiv:2606.11686v1 §5 Discussion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 分层 gate 定位快但只覆盖显式 scaffold；端到端 stochastic behavior 与未被 exercise 的 layer 仍需独立评测。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11686:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11686v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11686:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents](https://arxiv.org/html/2606.11688v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。

**State / data / control owner。** `AGENT-WORKFLOW` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11688v1 §6 Empirical evaluation; §6.5 scaled corpus` 支持 `3,150 paired cells; 70 tasks including 50 SWE-bench Lite`；模型 `Three systems × three models; model identities partly withheld`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11688v1 §3 Method; §4 theorem; §5 System`；counterevidence locator：`arXiv:2606.11688v1 §7 Limitations; Appendix A auditor boundary`。

**Trade-off / failure / coexistence / evolution。** hard floor 用 coverage 换 honesty；定理依赖 gate soundness、floor enforcement 与 plan coverage，不能证明任务本身正确。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11688:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11688v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11688:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation](https://arxiv.org/html/2606.11690v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。

**State / data / control owner。** `PLATFORM-COST` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11690v1 §4 Experimental Setup; §5 Results` 支持 `42 H100 benchmarks plus 56 A100 cross-hardware runs, 1–10 rps and saturation sweeps`；模型 `Dense, ultra-sparse MoE and sparse MoE models`；硬件 `NVIDIA H100 and A100 80GB PCIe`；精度 `FP16 and FP8 where supported`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11690v1 §3 Concurrency-Aware Cost Framework`；counterevidence locator：`arXiv:2606.11690v1 §6.8 Scope; §6.9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 真实 meter 提高归因但需要 workload replay；burst、prefix cache、I/O shape 与硬件 FP8 支持会改变 crossover。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11690:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11690v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11690:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/70-cost.md`，Review notes 前正文锚点 `Utilization 应由实际负载推出，而不是由计算器假定` 已承载长期命题；source 仅作受限证据。

### [Substrate Asymmetry in User-Side Memory: A Diagnostic Framework](https://arxiv.org/html/2606.11712v1)

**问题与机制。** 原筛选把《Substrate Asymmetry in User-Side Memory: A Diagnostic Framework》关闭或降池；完整摘要显示“We show this aggregate metric hides opposite-direction failures.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.2 Memory architectures; 3 Method; Appendix A Appendix A: Method (full detail)`；可采用的最小机制命题是：We show this aggregate metric hides opposite-direction failures.

**Evaluation proof。** `4 Results; Appendix B Appendix B: Results (full per-axis detail)`；exact-v1 披露：We show this aggregate metric hides opposite-direction failures.

**Limitations / non-proof。** `6 Discussion; Appendix D Appendix D: Discussion (full); D.4 Limitations (honest)`；We contribute the diagnostic framework, the diagnosed real-data negative, the alignment-tax replication, and the routing-as-classification finding. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs](https://arxiv.org/html/2606.11718v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11718v1 §IV Evaluation; §IV-A methodology` 支持 `Qwen3-30B and Llama-3.1-70B inference/training GEMM shapes`；模型 `Qwen3-30B; Llama-3.1-70B`；硬件 `Modeled multi-chiplet GPU; exact product not claimed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11718v1 §III Chiplet-Contiguous Layout`；counterevidence locator：`arXiv:2606.11718v1 §V Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 布局变换减少 remote HBM traffic，却要求 runtime/compiler 重排；对非 GEMM、动态 shape 或不同 interleave policy 不构成普遍收益。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11718:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11718v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11718:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/54-gpu-memory.md`，Review notes 前正文锚点 `Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页` 已承载长期命题；source 仅作受限证据。

### [External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs](https://arxiv.org/html/2606.11806v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11806v1 §4 setup; §5 Results; Appendices E–G` 支持 `Production moderation plus tool-use and GPQA contrast tasks`；模型 `Reasoning/instruct model variants disclosed in Appendix A.4`；硬件 `Not Disclosed — hosted serving hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11806v1 §3 Experience Serving in Production`；counterevidence locator：`arXiv:2606.11806v1 §4.4 claim boundary; Appendix H interpretation scope`。

**Trade-off / failure / coexistence / evolution。** selective retrieval 控制 prompt burden，但 miss/over-trigger 与 selector overhead 会伤害质量；规则少或高度共享时 global compact 仍成立。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11806:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11806v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11806:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code](https://arxiv.org/html/2606.11817v1)

**问题与机制。** 原筛选把《Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code》关闭或降池；完整摘要显示“To address this vulnerability, we propose CodeShield, a safety alignment approach that robustly preserves safe behavior even under attacker-controlled grammar constraints.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`IV Methodology`；可采用的最小机制命题是：To address this vulnerability, we propose CodeShield, a safety alignment approach that robustly preserves safe behavior even under attacker-controlled grammar constraints.

**Evaluation proof。** `V Experimental Setup; VI Experimental Results`；exact-v1 披露：Our experiments show that simply applying a benign code grammar constraint can effectively jailbreak LLMs.

**Limitations / non-proof。** `VII Discussion; VII-C Threats to Validity`；Such code is semantically harmless, so it does not implement the malicious request, and structurally diverse, so it is difficult to suppress through grammar tightening. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Decoding Constraint 也是不可信控制输入` 已完成写入并通过独立 post-write audit。

### [Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning](https://arxiv.org/html/2606.11853v1)

**问题与机制。** 原筛选把《Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning》关闭或降池；完整摘要显示“We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology; 3.1 Preliminaries and Problem Formulation`；可采用的最小机制命题是：We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setting; 4.2 Experimental Results`；exact-v1 披露：Evaluations confirm TASM maintains high performance under heavy compression, effectively balancing efficiency with adaptability.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Multi-modal large language models (MLLMs) depend on in-context learning (ICL) for rapid task adaptation, but their scalability is severely limited by finite context windows and the growing cost of key-value (KV) caches in long multi-modal sequences. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training](https://arxiv.org/html/2606.11867v1)

**问题与机制。** 原筛选把《Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training》关闭或降池；完整摘要显示“We introduce ForeMoE, a micro-step-level load balancing system for MoE RL post-training.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.1. MoE Architecture`；可采用的最小机制命题是：We introduce ForeMoE, a micro-step-level load balancing system for MoE RL post-training.

**Evaluation proof。** `10. Evaluation; 10.1. Experimental Setup; 10.4. Case Study`；exact-v1 披露：Evaluations on 64 GPUs demonstrate that ForeMoE achieves up to a 1.45$\times$ speedup over state-of-the-art RL post-training systems.

**Limitations / non-proof。** `3. Observations and Current Limitations`；Instead of relying on historical statistics, ForeMoE exploits the multi-stage RL pipeline (rollout, recompute, policy update) by using foreseeable routing information from the rollout stage to proactively guide load balancing in the remaining stages. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DISTRIBUTED-TRAINING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/36-distributed-training.md`，Review notes 前正文锚点 `Expert Placement 与 Sample Packing 可以共享 Rollout Routing State` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：Agents All the Way Down

独立复核结论：该 family 是单项目方法论与既有 agent building practice 的重新组织，没有提供可独立定位的新 state/control/evaluation contract；以下作者侧审阅轨迹仅用于解释误收原因，不计入 Candidate 或 Books。

**问题与机制。** 原筛选把《Agents All the Way Down; A Methodology for Building Custom AI Agents from Substrate to Production》关闭或降池；完整摘要显示“We present it as a transferable practice, independent of any language or framework.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 PDF；方法链由摘要中的 P1–P5 生命周期定义定位`；可采用的最小机制命题是：We present it as a transferable practice, independent of any language or framework.

**Evaluation proof。** `exact-v1 PDF；生产案例与边界说明`；exact-v1 披露：We present it as a transferable practice, independent of any language or framework.

**Limitations / non-proof。** `exact-v1 PDF；摘要未披露独立 limitations 标题`；We present it as a transferable practice, independent of any language or framework. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries](https://arxiv.org/html/2606.11871v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11871v1 §VI Evaluation; §VII backend cost` 支持 `77 CUDA artifacts; 51,621 sites; 52.2M dynamic checks`；模型 `CUDA SASS binaries`；硬件 `NVIDIA CUDA testbed; exact GPU bound in §VI-A`；精度 `Not applicable — binary instrumentation`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11871v1 §III threat model; §§IV–V design/implementation`；counterevidence locator：`arXiv:2606.11871v1 §VI-H portability boundaries; §VIII Discussion`。

**Trade-off / failure / coexistence / evolution。** SASS-level enforcement覆盖真实执行面但增加 instrumentation/callback cost；未恢复 site 必须 fail closed 或留在 denominator 外。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11871:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11871v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11871:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision](https://arxiv.org/html/2606.11878v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11878v1 §VI evidence; §VII-D mitigation results` 支持 `CUDA contract-conformance suite across four authority dimensions`；模型 `CUDA collective primitives and CIC wrapper`；硬件 `NVIDIA CUDA testbed; exact GPU in evidence appendix`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11878v1 §§III–V participation authority and CSC`；counterevidence locator：`arXiv:2606.11878v1 §VII-E Cost and Limits; §VIII Discussion and Limitations`。

**Trade-off / failure / coexistence / evolution。** CIC 防止 range-valid metadata 扭曲授权，却需保存 reference membership/epoch；普通 CFI 不覆盖此语义面。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11878:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11878v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11878:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Characterizing Software Aging in GPU-Based LLM Serving Systems](https://arxiv.org/html/2606.11916v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11916v1 §IV Results; §§IV-A–IV-E` 支持 `216-hour campaign; six co-located deployments; Poisson stress`；模型 `Qwen2.5-7B-Instruct on vLLM, Triton-vLLM and PyTorch/HF`；硬件 `One host with 3× NVIDIA L40S`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11916v1 §III Methodology`；counterevidence locator：`arXiv:2606.11916v1 §V Threats to Validity`。

**Trade-off / failure / coexistence / evolution。** 长时 campaign 昂贵且 co-location 可能混入 contention；短基准仍适合 kernel 回归，但不能替代 rejuvenation evidence。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11916:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11916v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11916:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/67-monitoring.md`，Review notes 前正文锚点 `条件化机制分支与共存边界` 已承载长期命题；source 仅作受限证据。

### [Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers](https://arxiv.org/html/2606.11949v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11949v1 §4 setup; §5 Results` 支持 `4 classifiers × 5 shifts × 20 seeds × 2 windows; 800 cells`；模型 `Four deployed safety classifiers`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11949v1 §3 Methods; §§3.1–3.10`；counterevidence locator：`arXiv:2606.11949v1 §6.5 Limitations; §5.4 ground-truth regimes`。

**Trade-off / failure / coexistence / evolution。** 检测可能对 target attack 无信号，density ratio 也会退化；abstention 恢复 coverage 不等于阻止攻击。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11949:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11949v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11949:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/67-monitoring.md`，Review notes 前正文锚点 `条件化机制分支与共存边界` 已承载长期命题；source 仅作受限证据。

### [Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/html/2606.11998v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11998v1 §4 Results; Appendix C red/blue teaming` 支持 `Multi-turn BashArena software-engineering tasks`；模型 `Trusted, untrusted-agent and intermediate-monitor model configurations`；硬件 `Not Disclosed — API/runtime hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11998v1 §3 Methods; §3.1 threat model/protocol`；counterevidence locator：`arXiv:2606.11998v1 §5 Discussion, Transparent CoT assumption and Limitations`。

**Trade-off / failure / coexistence / evolution。** bootstrapping 延长弱 monitor 生命周期，却依赖 transparent CoT；隐藏推理、steganography 或共同盲点会失效。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11998:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11998v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11998:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：Scientific Novelty Assessment

独立复核结论：该 family 的对象是 AI for Science 中的 scientific novelty judgment；当前范围明确暂缓该阶段，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题与机制。** 原筛选把《On the Limits of LLM-as-Judge for Scientific Novelty Assessment》关闭或降池；完整摘要显示“We introduce RQ-Bench, a benchmark built from recent arXiv papers.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We introduce RQ-Bench, a benchmark built from recent arXiv papers.

**Evaluation proof。** `5 Evaluation Setup; 6 Experiments; 6.1 Experimental Setup`；exact-v1 披露：This makes novelty evaluation a central problem.

**Limitations / non-proof。** `6.2 Results and Discussions; Limitations`；These RQs are not the only valid questions for the same background. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents](https://arxiv.org/html/2606.12087v1)

**问题与机制。** 原筛选把《FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents》关闭或降池；完整摘要显示“We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2 Difficulty Framework; 2.1 Problem Formulation; 3 Methodology`；可采用的最小机制命题是：We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding.

**Evaluation proof。** `4 Experiment; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：Experiments show that FORT induces longer pre-answer search and fewer shortcut patterns than existing open-source deep search datasets.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Existing synthesis methods often increase apparent difficulty by enriching graph structures, but structural complexity alone does not guarantee realized search difficulty: the intended search process can collapse through a cheaper identifying route. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DATA` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path](https://arxiv.org/html/2606.12154v1)

**问题与机制。** 原筛选把《The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path》关闭或降池；完整摘要显示“That result solved a placement problem and immediately exposed a different one: even correctly placed, the large model needed roughly four seconds to answer, because it was still being invoked at every query.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 The Horsehair Architecture`；可采用的最小机制命题是：That result solved a placement problem and immediately exposed a different one: even correctly placed, the large model needed roughly four seconds to answer, because it was still being invoked at every query.

**Evaluation proof。** `5 Experimental Setup; 6 Results`；exact-v1 披露：A 16-case verification gate blocked all ten corrupted entries while admitting all six supported ones.

**Limitations / non-proof。** `8 Limitations`；During an offline phase, the large model reads source documents and writes verified answer entries into a structured knowledge store; at runtime, only a lightweight router, a deterministic renderer, and a 1B-class model are active. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-PREFILL` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Only report`；该 exact-v1 仅支持受限案例，尚不足以改变长期 Books 机制链，不创建正文或 trace 采用链。

### [A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs](https://arxiv.org/html/2606.12160v1)

**问题与机制。** 原筛选把《A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs》关闭或降池；完整摘要显示“However, modern instruction-tuned LLMs already achieve substantially higher baselines (61-76%), raising the question of whether these methods remain effective in practice.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Evaluation Framework; 4.5 Deliberative Methods`；可采用的最小机制命题是：However, modern instruction-tuned LLMs already achieve substantially higher baselines (61-76%), raising the question of whether these methods remain effective in practice.

**Evaluation proof。** `3 Evaluation Framework; 4 Experiments; 4.1 Main Results`；exact-v1 披露：We design a six-control evaluation framework -- out-of-distribution training, multi-judge validation, simple decoding baselines, confound controls, bootstrap confidence intervals, and seed variance -- and apply it across 5 models (1B-70B), 3 benchmarks, and 15 methods.

**Limitations / non-proof。** `5 Discussion and Conclusion`；We release a seven-point evaluation checklist and discuss implications for future truthfulness research. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps](https://arxiv.org/html/2606.12212v1)

**问题与机制。** 原筛选把《Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps》关闭或降池；完整摘要显示“We present the first in-depth empirical study of API key leakage in LLM-integrated apps.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3. Methodology`；可采用的最小机制命题是：We present the first in-depth empirical study of API key leakage in LLM-integrated apps.

**Evaluation proof。** `exact-v1 evaluation/results section`；exact-v1 披露：Our findings show that LLM API key leakage is both prevalent and persistent in the iOS ecosystem, exposing a systemic gap between developer practice and secure integration principles, and suggest that secure LLM integration requires not only developer awareness but also explicit security guidance from providers and platform-level enforcement.

**Limitations / non-proof。** `6. Threats to Validity`；To assess remediation, we re-analyzed the same 282 vulnerable applications three months after responsible disclosure; only 28% had remediated the reported vulnerability, while 72% remained exploitable, with persistent issues stemming from unauthenticated backends and broken JWT implementations. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study](https://arxiv.org/html/2606.12231v1)

**问题与机制。** 原筛选把《Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study》关闭或降池；完整摘要显示“Despite their role in aligning AI behavior with developer intent, the taxonomy, evolution, and practical impact of these rules remain largely unexplored.”。该增量直接改变 AGENT-PROMPT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4. Research Methodology`；可采用的最小机制命题是：Despite their role in aligning AI behavior with developer intent, the taxonomy, evolution, and practical impact of these rules remain largely unexplored.

**Evaluation proof。** `3.1. Evaluation and Impact of AI IDEs; 5. Study Results; 6.1. Interpretation of Study Results`；exact-v1 披露：Our study provides empirical insights that can help developers optimize prompting strategies and guide tool builders in designing automated conflict-detection and context-management mechanisms for AI IDEs.

**Limitations / non-proof。** `6. Discussion; 7. Threats to Validity`；Our study provides empirical insights that can help developers optimize prompting strategies and guide tool builders in designing automated conflict-detection and context-management mechanisms for AI IDEs. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PROMPT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/74-prompt.md`，Review notes 前正文锚点 `Prompt 生命周期` 已承载长期命题；source 仅作受限证据。

### [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/html/2606.12243v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12243v1 §4 Experiments` 支持 `Four tasks across T5/Gemma model families`；模型 `T5 and Gemma families`；硬件 `Disclosed in §4.1; no cross-paper normalization`；精度 `Disclosed in §4.1 where applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12243v1 §3 Methodology; §§3.2–3.5`；counterevidence locator：`arXiv:2606.12243v1 §4.4 additional analysis; §5 Conclusion`。

**Trade-off / failure / coexistence / evolution。** slim verifier 节约 full-model calls 但引入 routing error/threshold；exact rejection contract 与 full verifier fallback 必须保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12243:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12243v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12243:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/48-speculative-decoding.md`，Review notes 前正文锚点 `Correctness owner 没有改变` 已承载长期命题；source 仅作受限证据。

### [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/html/2606.12320v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12320v1 §9 case studies; §10 validation roadmap` 支持 `Seven canonical workflow threats plus production case studies`；模型 `Reference architecture; not a model benchmark`；硬件 `Not applicable`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12320v1 §§3–8 threat model, five planes and composed architecture`；counterevidence locator：`arXiv:2606.12320v1 §11 Limitations and Open Questions`。

**Trade-off / failure / coexistence / evolution。** 多平面提高可中断性与归因，却增加 latency/state consistency/TCB；reference architecture 不证明生产效果。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12320:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12320v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12320:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`。五平面是实现 taxonomy；现有正文已经拥有 delegation/effect-time authorization、capability attenuation、跨通道 influence graph 与 evidence chain，不追加平行架构清单。

### [PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/html/2606.12329v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12329v1 §7 Evaluation` 支持 `Two-month self-study, 10 projects, 207 events`；模型 `Local-first projectmem with MCP/CLI`；硬件 `Local developer environment; hardware not disclosed`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12329v1 §3 System Design; §§4–6 architecture/implementation`；counterevidence locator：`arXiv:2606.12329v1 §8 Limitations and Future Work`。

**Trade-off / failure / coexistence / evolution。** event sourcing 提供 provenance/rollback，但 self-study 不能证明跨团队收益；错误 judgment 仍需 supersession 与关闭开关。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12329:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12329v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12329:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents](https://arxiv.org/html/2606.12341v1)

**问题与机制。** 原筛选把《OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents》关闭或降池；完整摘要显示“We recast agent privacy as \emph{posterior-risk control} and present OCELOT, a runtime mediator that budgets how much an adversary's belief about a secret may improve across a trajectory, rather than filtering outputs.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`III Problem Formulation; IV-A Architecture and Rubrics`；可采用的最小机制命题是：We recast agent privacy as \emph{posterior-risk control} and present OCELOT, a runtime mediator that budgets how much an adversary's belief about a secret may improve across a trajectory, rather than filtering outputs.

**Evaluation proof。** `V Experiments; V-A Experimental Setup; V-B Privacy–Utility Evaluation`；exact-v1 披露：Across diverse agent benchmarks and recent defenses, OCELOT attains significantly lower leakage at higher task utility, resists adaptive injection, jailbreak, cumulative inference, and sink collusion, and adds only modest overhead.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Across diverse agent benchmarks and recent defenses, OCELOT attains significantly lower leakage at higher task utility, resists adaptive injection, jailbreak, cumulative inference, and sink collusion, and adds only modest overhead. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Agent Privacy 必须对整条 Trajectory 记账` 已完成写入并通过独立 post-write audit。

### [ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing](https://arxiv.org/html/2606.12342v1)

**问题与机制。** 原筛选把《ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing》关闭或降池；完整摘要显示“We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; J.5 Qwen2.5-7B-Base: Same-Family Anchor Size and Method Ablation`；可采用的最小机制命题是：We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations.

**Evaluation proof。** `4 Experiments; 5 Results; 5.1 Headline Results`；exact-v1 披露：Across both cross-vocabulary and same-vocabulary evaluation pairs, ALIGNBEAM substantially raises refusal on adversarial benchmarks while keeping task accuracy and inference overhead within practical bounds.

**Limitations / non-proof。** `Limitations; Appendix L Extended Limitations`；The results show that safety alignment can be transferred between model families at inference time, without touching either model's weights. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Only report`；该 exact-v1 仅支持受限案例，尚不足以改变长期 Books 机制链，不创建正文或 trace 采用链。

### [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/html/2606.12344v1)

**问题与机制。** 原筛选把《Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks》关闭或降池；完整摘要显示“We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator.

**Evaluation proof。** `3.3 Validation Results and the 80-Instance Scale; 4 Experimental Setup; 5 Results`；exact-v1 披露：Claw-SWE-Bench therefore treats harness and cost accounting as first-class axes of SWE-style coding-agent evaluation, providing both a full benchmark and a low-cost reference set for reproducible comparison.

**Limitations / non-proof。** `7 Conclusion and Discussion`；General-purpose agents such as OpenClaw are increasingly used as autonomous tool users, but their coding ability is difficult to measure under SWE-bench: a generic agent does not by itself satisfy the clean Docker workspace, patch, and prediction contract required for scoring. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [On Subquadratic Architectures: From Applications to Principles](https://arxiv.org/html/2606.12364v1)

**问题与机制。** 原筛选把《On Subquadratic Architectures: From Applications to Principles》关闭或降池；完整摘要显示“To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics.”。该增量直接改变 MODEL-LONG-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Analysis of Leading Subquadratic Attention Architectures`；可采用的最小机制命题是：To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics.

**Evaluation proof。** `2 Experiments with Complex Dependencies; 4 Experiments on Accumulation and State Tracking; Appendix B Code-focused Language Model Pre-training Results`；exact-v1 披露：We evaluate these models on tasks with complex dependencies: (1) code-model pre-training, (2) distillation of code models from large language models, and (3) pre-training of time-series foundation models.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Overall, our findings indicate that xLSTM's gains on complex tasks stem from robust state tracking and accumulation. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `MODEL-LONG-CONTEXT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-02-model/22-long-context.md`，Review notes 前正文锚点 `方案究竟移动了哪个瓶颈` 已承载长期命题；source 仅作受限证据。

### [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/html/2606.12370v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12370v1 §6 Experiments` 支持 `RL math/reasoning workloads and MTP acceptance/throughput sweeps`；模型 `Multiple MTP-enabled LLM scales`；硬件 `Disclosed in experimental appendix`；精度 `Disclosed in experimental appendix`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12370v1 §§3–5 entropy bound, TV loss and adaptation`；counterevidence locator：`arXiv:2606.12370v1 §7.8 top-k instability; §9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 更新 MTP 提升 rollout throughput 却增加训练耦合；top-k TV 不稳，完整 rejection sampling 是 correctness fallback；TRAIN-RLHF 只消费 rollout throughput 与 policy-update handoff。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12370:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12370v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12370:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/48-speculative-decoding.md`，Review notes 前正文锚点 `Correctness owner 没有改变` 已承载长期命题；source 仅作受限证据。

### [Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization](https://arxiv.org/html/2606.12373v1)

**问题与机制。** 原筛选把《Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization》关闭或降池；完整摘要显示“While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method`；可采用的最小机制命题是：While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：Extensive experiments show that RL training on these composite environments consistently enhances reasoning generalization.

**Limitations / non-proof。** `Appendix A Limitations`；Moreover, RACES achieves performance comparable to training on 300 individual environments using only 50 base environments, demonstrating significant efficiency in environment utilization. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DATA` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `可验证环境可以组合，但组合器不拥有正确性` 已完成写入并通过独立 post-write audit。

### [APPO: Agentic Procedural Policy Optimization](https://arxiv.org/html/2606.12384v1)

**问题与机制。** 原筛选把《APPO: Agentic Procedural Policy Optimization》关闭或降池；完整摘要显示“Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence.

**Evaluation proof。** `4 Experiments; 4.1 Experiment Setup; 4.2 Main Results`；exact-v1 披露：Experiments on 13 benchmarks show that APPO consistently improves strong agentic RL baselines by nearly 4 points, while keeping efficient tool-calls and maintaining behavior interpretability.

**Limitations / non-proof。** `Appendix G Limitations`；Our pilot analysis shows that influential decision points are broadly distributed throughout the generated sequence rather than concentrated at tool calls, while token entropy alone does not reliably reflect their impact on final outcomes. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-GRPO` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/33-grpo.md`，Review notes 前正文锚点 `从一个终局标量到 Typed Credit：Reward 必须匹配决策边界` 已承载长期命题；source 仅作受限证据。

### [Doc-to-Atom: Learning to Compile and Compose Memory Atoms](https://arxiv.org/html/2606.12400v1)

**问题与机制。** 原筛选把《Doc-to-Atom: Learning to Compile and Compose Memory Atoms》关闭或降池；完整摘要显示“To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; 3.2 Compositional Memory Framework`；可采用的最小机制命题是：To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：Experiments on six diverse QA benchmarks demonstrate that Doc2Atom outperforms Doc-to-LoRA baselines while reducing the memory cost of document internalization.

**Limitations / non-proof。** `Limitations`；However, producing a single monolithic adapter for all queries leads to irrelevant-query interference, limited compositional recall, and poor scalability to long-document reasoning. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `个性化更新与事实可靠性是两套策略` 已完成写入并通过独立 post-write audit。

### Books / semantic audit

`Integrate=10`，`No Change — Existing Coverage=40`，`Only report=2`，另有 2 项经独立准入复核改为分母前关闭。作者侧 proposal 与独立 Gate 的最终覆盖清单见 [`v3-independent-candidate-books-gate-20260911.json`](../_sources/daily-20260611/v3-independent-candidate-books-gate-20260911.json)；独立写后结果见 [`v3-independent-post-write-audit-20260911.json`](../_sources/daily-20260611/v3-independent-post-write-audit-20260911.json)。`books_removal_queue=0`，7 条 trace 日期修正均已完成并复验，remaining queue=`0`。

## 5. 缺口与下一步

终态保留项：official historical arXiv listing/announcement receipt 尚未取得；定点重开条件：未来取得可改变公开日期 owner 的官方 listing evidence；该缺口不用于正面证据、Books 或无遗漏断言。

1. 10 条 Books body writeback 与 7 条 trace 日期修正均已完成；正文 marker、章节位置、长期机制链和报告映射已由非写作者独立复验，执行队列为 0。
2. official historical arXiv listing/announcement receipt 仍是保留的来源边界；在其到位前不执行跨日迁移，也不把该外部证明缺口伪装成当前日期的执行 pending。
3. 若未来取得相反的 official listing evidence，只重开受影响的日期 owner reconciliation，不推翻本次冻结的 Candidate denominator。

### Repository Changes

- 更新 2026-06-11 Daily 与 `_sources/daily-20260611` 下的 V3 Gate、proposal、reconciliation 和独立写后审计 artifact。
- 复验并最小重排 `27-data.md`、`28-pretraining.md`、`31-rlhf.md`、`49-tensorrt-llm.md`、`56-inference-scheduling.md`、`66-evaluation-system.md`、`72-security.md`、`76-rag.md`；`77-memory.md` 的现有落点无需重排。
- 未修改 Candidate denominator、`docs/LEARNING_STATE.md`、其他日期或月级 audit。

## 6. 复核

当前来源再认证复核者：\`june_11_20_recert\`（独立于原报告作者）。当前合同来源再认证补齐十三个官方 Daily 源；未发现需恢复的独立候选，原 Candidate/Evidence/Books 结论保持不变。

复核者：Candidate/Books Gate `/root/june_11_12_independent_gate`；独立 post-write audit `/root/june_11_12_postwrite`
结论：通过

- 2 项误收已关闭、1 项伪增量已改为 Existing Coverage；10 条 Books 正文与 7 条 trace correction 已逐条复验。独立审计发现并修复了案例先于通用基线的章节顺序问题，未改变 Candidate denominator 或长期结论。
- 机器校验：`validate_research.py`、`check_report_v3.validate`、JSON/算术/URL 与身份去重、marker 唯一性、Review notes 边界和 `git diff --check` 均通过。机器结果不替代上述语义复核。
