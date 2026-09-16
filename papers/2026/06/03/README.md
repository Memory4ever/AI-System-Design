# Daily Research — 2026-06-03

**规范：** V3
**窗口：** 2026-06-02T09:00:00+08:00 ～ 2026-06-03T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗的严格 arXiv 题摘分母已经从可读 719-row canonical packet 冻结为 87 Candidate / 632 Close；厂商源再认证另恢复 1 个 Kimi Code release Source Family，因此报告总分母为 88 Candidate。旧 44 项前沿重审后保留 39、关闭 5；675 条旧 closure 全量 title sweep 与边界 abstract 复核后恢复 48、维持关闭 627。旧报告顶部的 747/55 没有可读支撑文件，不参与当前计数。

旧报告全文和 44 项 exact-v1 Review 已保存到 [`V2_1_EVIDENCE_ARCHIVE.md`](../_sources/daily-20260603/V2_1_EVIDENCE_ARCHIVE.md)。39 个存续项复用仍匹配的 Method/Evaluation/Limitations 与 claim boundary，并已按 current Books 正文重判；48 个新恢复项也已逐项完成候选级 evidence 与 Books Decision。逐项准入、关闭 family 与 FP/FN 抽检见 [`V3_SCREENING_LEDGER.md`](../_sources/daily-20260603/V3_SCREENING_LEDGER.md)。

Books 写回已按 owner 闭合。非 Inference / Platform 批次的 6 项真实增量已写入 `TRAIN-PRETRAINING`、`TRAIN-GRPO`、`TRAIN-DISTRIBUTED-TRAINING` 与 `AGENT-PLATFORM`；本批重新顺读 13 项 Inference / Platform 决策后，KVarN、Judge Subspace 与 Overlay Governance 被现有命题级正文完整覆盖，其余 10 项归并写入 `INFER-SCHEDULING`、`PLATFORM-MODEL-REGISTRY`、`PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-SECURITY`。Kimi Code release 由现有 `AGENT-WORKFLOW` 覆盖。最终全 88 项为 71 Existing / 16 已写入正文 / 1 Only report，0 proposal、0 Deferred、exact-v1 blocker=0。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：GPT-Rosalind 属暂缓的 AI for Science，已关闭 | 已检查 | 无 |
| SRC-ANTHROPIC | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-META-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；Kimi Code 0.7.0/0.8.0 的精确 release 时刻落在本窗，见候选与判断 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-ARXIV | [`canonical-raw-identity-inventory-v2.1.json.gz`](../_sources/daily-20260603/canonical-raw-identity-inventory-v2.1.json.gz)、[`canonical-semantic-screening-checkpoint-v2.1.json.gz`](../_sources/daily-20260603/canonical-semantic-screening-checkpoint-v2.1.json.gz) 与 [`V3_SCREENING_LEDGER.md`](../_sources/daily-20260603/V3_SCREENING_LEDGER.md)；719 identities 已冻结为 87 Candidate / 632 Close，旧 747/55 空文件不作为本次依据 | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.7.0 / 0.8.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.7.0) | 2026-06-02T10:23:53+08:00 ～ 2026-06-02T22:56:13+08:00 | goal mode、background question、approval lifecycle 与 compaction todo 把长任务从 turn transcript 提升为可恢复 workflow state；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-WORKFLOW` — [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Cost-Aware Query Routing in RAG: Empirical Analysis of Retrieval Depth Tradeoffs](https://arxiv.org/abs/2606.02581v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | per-query strategy bundle 联合 token、latency、grounding 与 stop；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-RAG — [章节](../../../../books/part-07-agent/76-rag.md) |
| [ReLoRA: Knowledge-Reusing Adaptation for Fast Rollout of Evolving LLM Services](https://arxiv.org/abs/2606.02606v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | base evolution 后 adapter compatibility 与 rollout readiness 成为版本迁移合同；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-LORA — [章节](../../../../books/part-04-training-system/30-lora.md) |
| [Acceptance-Test-Driven Evaluation Protocols for Business-Centric LLM Systems](https://arxiv.org/abs/2606.02755v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | stakeholder requirement 编译为 executable acceptance/release gate；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Which Defense Closes Which Threat? Attributing OWASP-LLM-Top-10 Coverage and Its Brittleness Under Paraphrasing](https://arxiv.org/abs/2606.02822v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | defense-family/threat/operating-point attribution 取代总覆盖率；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Thinking Past the Answer: Evaluating Harmful Overthinking in Large Reasoning Models](https://arxiv.org/abs/2606.02835v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | prefix trajectory 分离首次正确、额外推理与最终退化；3+3+3=9 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks](https://arxiv.org/abs/2606.02875v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | repository partial state、handoff view 与 successor rediscovery 成为 continuation contract；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW — [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Linear Probes Detect Task Format, Not Reasoning Mode in Language Model Hidden States](https://arxiv.org/abs/2606.02907v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | format residualization 与 random control 修正 reasoning-probe 证据边界；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Fast-dLLM++: Fréchet Profile Decoding for Faster Diffusion LLM Inference](https://arxiv.org/abs/2606.02955v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | heterogeneous confidence profile 决定 diffusion LM parallel commit proposal；2+3+2=7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Predicting Inference-Time Scaling Gains from Labeled Validation-Set Output Statistics](https://arxiv.org/abs/2606.02981v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 廉价 validation statistics 预估 Best-of-N gain，改变预算 admission；3+2+2=7 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [TGV-KV: Text-Grounded KV Eviction for Vision-Language Models](https://arxiv.org/abs/2606.03075v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | text-vision relevance 驱动 multimodal KV budget 与 eviction；2+3+2=7 | 深入完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DeltaMem: Large Language Models Acting as Incremental Learners](https://arxiv.org/abs/2606.03083v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | residual tree 保存增量经验、冗余、冲突与版本化 merge；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [Learning to Solve, Forgetting to Retain: Correct-Set Turnover in RLVR](https://arxiv.org/abs/2606.03087v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | acquisition/retention turnover ledger 与 repair-window review queue；3+3+3=9 | 深入完成 | 整合：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)；正文锚点“Mastered Set 需要 Acquisition–Retention Turnover Ledger” |
| [The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs](https://arxiv.org/abs/2606.03092v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | global shadow price 按 per-query utility 分配 reasoning budget；3+3+2=8 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Experience-Driven Dynamic Exits for LLMs with Reinforcement Learning](https://arxiv.org/abs/2606.03113v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | offline RL 按 local context 选择 exit layer 与 speculation length；2+3+2=7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Uncertainty-Aware Clarification in LLM Agents with Information Gain](https://arxiv.org/abs/2606.03135v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | intent belief update 与 EIG 决定 tool action 前是否澄清；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-PLANNING — [章节](../../../../books/part-07-agent/79-planning.md) |
| [PsychoPass: Geometric Profiling of Multi-Turn Adversarial LLM Conversations](https://arxiv.org/abs/2606.03136v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | guardrail state 从单 turn 扩为长度去混淆的 adversarial trajectory sensor；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [FederatedSkill: Federated Learning for Agentic Skill Evolution](https://arxiv.org/abs/2606.03143v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | local private trajectory、semantic patch 与 personalized library 分权；3+3+3=9 | 深入完成 | 整合：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md)；正文锚点“跨用户演进时，这一边界还要求把 private episode 与 shared skill revision 分开” |
| [WebRISE: Requirement-Induced State Evaluation for MLLM-Generated Web Artifacts](https://arxiv.org/abs/2606.03220v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | requirement 编译为 observable state/transition/DOM-visual assertions；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ARBOR: Online Process Rewards via a Reusable Rubric Buffer for Search Agents](https://arxiv.org/abs/2606.03239v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | rubric candidate/admission/consolidation/retirement 形成 reward asset lifecycle；3+3+3=9 | 深入完成 | 整合：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)；正文锚点“Rubric Pool 还需要 Admission、Consolidation 与 Retirement” |
| [Multilingual Unlearning in LLMs: Transfer, Dynamics, and Reversibility](https://arxiv.org/abs/2606.03291v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | language transfer 与 reversibility 成为 unlearning release/rollback 条件；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family” |
| [Beyond Ideal Instruction: A Comprehensive Framework for Evaluating LLMs in Realistic Interactions](https://arxiv.org/abs/2606.03318v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | ambiguity、uncooperative behavior 与 shifting intent 进入 tool-use 验收；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Calibration Data Trade-offs Across Capability Dimensions: Why Multi-Source Mixing Matters for High-Sparsity LLM Pruning](https://arxiv.org/abs/2606.03328v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | capability slices 揭示 averaged pruning score 掩盖 opposite-sign retention；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FLIPS: Instance-Fingerprinting for LLMs via Pseudo-random Sequences](https://arxiv.org/abs/2606.03330v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | model identity 扩为 weights、prompt、sampling、quantization 的 instance identity；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-MODEL-REGISTRY — [章节](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [RogueMerge: Robust and Unified Attacks against LLM Model Merging](https://arxiv.org/abs/2606.03344v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 第三方 task vector 形成 model-merge supply-chain write access；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Model Merge Input 是对权重的 Supply-chain Write Access” |
| [ImageAuditor: Membership Inference Attack against Image-based Retrieval-Augmented Generation](https://arxiv.org/abs/2606.03354v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | cross-modal retrieval/extraction 与 multi-query aggregation 扩展 datastore membership audit；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When Model Merging Breaks Routing: Training-Free Calibration for MoE](https://arxiv.org/abs/2606.03391v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | merge 后 router calibration 与 expert-assignment regression 成为发布 identity；3+3+3=9 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY — [章节](../../../../books/part-06-ai-infrastructure/59-model-registry.md)；正文锚点“MoE Merge 的发布身份还要包含 Router Calibration” |
| [KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks](https://arxiv.org/abs/2606.03458v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | autoregressive timestep error accumulation 改变 KV quantization 验收；3+3+3=9 | 深入完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点“Quantization Objective 应对齐 Attention Distortion”中的 repeated state feedback |
| [What Makes Interaction Trajectories Effective for Training Terminal Agents?](https://arxiv.org/abs/2606.03461v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | teacher ability 与 environment-grounded inspect-act-verify teaching value 分离；3+3+2=8 | 深入完成 | 已有覆盖：TRAIN-DATA — [章节](../../../../books/part-04-training-system/27-data.md) |
| [DMF: A Deterministic Memory Framework for Conversational AI Agents](https://arxiv.org/abs/2606.03463v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | deterministic CPU-first write/decay/prune 与 lineage 形成可复算 memory policy；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [StepFinder: A Temporal Semantic Framework for Failure Attribution in Multi-Agent Systems](https://arxiv.org/abs/2606.03467v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | temporal dependency 定位 multi-Agent cascade 的 candidate root-cause step；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-TRACE — [章节](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [SAGE: A Quantitative Evaluation of Socialized Evolution in Agent Ecosystems](https://arxiv.org/abs/2606.03544v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | compute-matched SocialEvo/SelfEvo 分离 peer-history 增益；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Skill Is Not Document: A Query-Conditional Benchmark and Two-Stage Retriever for LLM Agent Skill Routing](https://arxiv.org/abs/2606.03565v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | top-k skill joint compatibility 取代独立 document relevance；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [DDOR: Delta Debugging for Explainable Overrefusal Testing and Repair](https://arxiv.org/abs/2606.03601v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | harmful/benign counterpart 与最小 mutation 定位 overrefusal causal feature；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs](https://arxiv.org/abs/2606.03647v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | attack profile 与 threshold-independent severity-volume 联合刻画防御边界；3+3+3=9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Attack Success Rate 不能压平 Attack Profile” |
| [Safety Measurements for Fine-tuned LLMs Should be Grounded in Capability](https://arxiv.org/abs/2606.03648v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | safety delta 必须在 capability-matched configuration 下解释；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Diagnosing Knowledge Gaps in LLM Tool Use: An Agentic Benchmark for Novel API Acquisition](https://arxiv.org/abs/2606.03657v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | API discovery、schema acquisition、environment execution 与 effect verification 分层诊断；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING — [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [SkillPyramid: A Hierarchical Skill Consolidation Framework for Self-Evolving Agents](https://arxiv.org/abs/2606.03692v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | skill candidate、dependency、conflict、validation 与 promotion/revoke lifecycle；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Entropy Gate: Entropy Quenching for Near-Lossless Token Compression in LLM Pipelines](https://arxiv.org/abs/2606.03739v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | entropy gate 压缩 pipeline token，但 task-correctness 证据不足；2+2+2=6 | 标准完成 | 仅报告：embedding similarity 不能替代任务正确性，且压缩问题仅 6/9 保持 |
| [Tool-Aware Optimization with Entropy Guidance for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03762v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | tool outcome、trajectory admission 与 entropy/delayed consequence 联合优化；3+3+2=8 | 深入完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Backdoor Unlearning Generalization: A Path Toward the Removal of Unknown Triggers in LLMs](https://arxiv.org/abs/2606.03785v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | known-trigger removal 扩为 held-out unknown-family 与 retain-behavior release gate；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family” |
| [Trading Human Curation for Synthetic Augmentation in RLVR](https://arxiv.org/abs/2606.03800v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | synthetic/human task substitution 同时冻结 sandbox、quality gate、held-out utility 与 cost；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-DATA — [章节](../../../../books/part-04-training-system/27-data.md) |
| [Consistency Training Can Entrench Misalignment](https://arxiv.org/abs/2606.03810v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | consistency/self-generated-label training 需重新打开 alignment behavior gate；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Synthesize and Reward -- Reinforcement Learning for Multi-Step Tool Use in Live Environments](https://arxiv.org/abs/2606.03892v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | stateful MCP、live-state synthesis、session isolation 与 programmatic reward 绑定训练 row；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-DATA — [章节](../../../../books/part-04-training-system/27-data.md) |
| [Value-Aware Stochastic KV Cache Eviction for Reasoning Models](https://arxiv.org/abs/2606.03928v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | value outlier pinning 与 stochastic survivor diversity 共同约束 reasoning eviction；3+3+3=9 | 深入完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [q0: Primitives for Hyper-Epoch Pretraining](https://arxiv.org/abs/2606.03938v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | multi-epoch state 从单 checkpoint 扩为 population、chain distillation 与 budgeted member set；3+3+3=9 | 深入完成 | 整合：TRAIN-PRETRAINING — [章节](../../../../books/part-04-training-system/28-pretraining.md)；正文锚点“超多 Epoch 训练会把单一 Checkpoint 演进为模型群体状态” |
| [Quantifying Faithful Confidence Expression in Large Reasoning Models](https://arxiv.org/abs/2606.03969v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | intrinsic estimator 与 linguistic decisiveness 分权，避免单一 confidence truth；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories](https://arxiv.org/abs/2606.03979v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | short-term context 向 parameter consolidation 迁移并分离 self-improvement phase；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill](https://arxiv.org/abs/2606.03980v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | rule/reference/checklist/rubric 外置为 versioned reward-evaluation skill；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Inference Cost Attacks for Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2606.02643v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；RAG poisoning 放大检索与生成资源；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size](https://arxiv.org/abs/2606.02646v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；effective evidence 取代 nominal agent count；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents](https://arxiv.org/abs/2606.02668v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；approval 必须从真实 action/effect 渲染；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Approval Summary 必须由待执行 Effect 反向渲染” |
| [Echelon: Auditable Aggregate-Only Language-Model Adaptation Across Privacy Boundaries](https://arxiv.org/abs/2606.02958v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；device state non-export 与 aggregate-only adaptation；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Gate AI: LLM Security Benchmark Evaluation Methodology and Results](https://arxiv.org/abs/2606.02959v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；threshold/group split/operating point disclosure；2+3+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators](https://arxiv.org/abs/2606.02963v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；kernel proposal、backend 与 validation 分权；2+3+2=7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM — [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving](https://arxiv.org/abs/2606.02964v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；按 execution cost 管理 lossless KV segment；3+3+2=8 | 深入完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference](https://arxiv.org/abs/2606.02982v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；admission estimate 与 runtime drift 持续 reconciliation；3+3+2=8 | 深入完成 | 整合：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Token Drift 改变剩余工作时，要重算队列承诺” |
| [FOLD: Fuzzy Online Deduplication for Very Large Evolving Datasets via Approximate Nearest Neighbor Search](https://arxiv.org/abs/2606.03001v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；在线 fuzzy dedup state 与 admission；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-DATA — [章节](../../../../books/part-04-training-system/27-data.md) |
| [Perplexity Can Miss SAE Feature Damage Under Quantization](https://arxiv.org/abs/2606.03002v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；perplexity parity 不保证 feature fidelity；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MUSE: A Unified Agentic Harness for MLLMs](https://arxiv.org/abs/2606.03005v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；tool/parser/harness/deterministic verification 分权；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [MOSAIC: Efficient Mixture-of-Agent Scheduling via Adaptive Aggregation and Inference Concurrency](https://arxiv.org/abs/2606.03014v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；routing skew、generation variance 与 concurrency 联合调度；3+3+2=8 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [SkillGuard: A Permission-Centric Framework for Agent Skill Security](https://arxiv.org/abs/2606.03024v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；skill principal 连接 intent、permission 与 runtime effect；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Deliberative Illusion: Diagnosing Factual Attrition and Stance Homogenization in Multi-Agent LLM Deliberation](https://arxiv.org/abs/2606.03032v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；factual attrition 修正“共识即可靠”；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Capability Advertisement as a Market for Lemons: A Trust Layer for Heterogeneous Agent Networks](https://arxiv.org/abs/2606.03034v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；capability identity、drift、evidence 与 freshness；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MCP — [章节](../../../../books/part-07-agent/83-mcp.md) |
| [The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not Human Alignment](https://arxiv.org/abs/2606.03043v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；judge subspace consensus 不取得 human authority；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点“Judge Agreement 不是单一数字” |
| [ToolGate: Token-Efficient Pre-Call Control for Tool-Augmented Vision-Language Agents](https://arxiv.org/abs/2606.03054v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；tool issue 前 execute/skip gate；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING — [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [SkillDAG: Self-Evolving Typed Skill Graphs for LLM Skill Selection at Scale](https://arxiv.org/abs/2606.03056v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；typed dependency/conflict graph 改变 skill routing；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [ASymPO: Asymmetric-Scale Policy Optimization for Asynchronous LLM Post-Training Without Behavior Information](https://arxiv.org/abs/2606.03070v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；无 behavior logprob 的 stale-policy 更新边界；3+3+2=8 | 深入完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)；命题锚点“正负 Advantage 不必共享同一 Clipping Contract”“Asynchronous RL 必须把 Policy Staleness 写进 Advantage” |
| [Libra: Efficient Resource Management for Agentic RL Post-Training](https://arxiv.org/abs/2606.03077v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；rollout/learner 异构资源与 long-tail makespan；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../books/part-04-training-system/36-distributed-training.md)；命题锚点“RL Phase 资源可以成为弹性函数，但训练语义不能随实例伸缩”“Agent RL 从 Trainer 中心演进为版本化 Dataflow” |
| [EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03108v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；policy 与 harness 共同版本化、诊断与 backtest；3+3+2=8 | 深入完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [SPOQ: Specialist Orchestrated Queuing for Multi-Agent Software Engineering](https://arxiv.org/abs/2606.03115v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；dependency waves、pre/post validation 与 human gate；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW — [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Cost-Aware Optimization for Agentic Query Execution](https://arxiv.org/abs/2606.03152v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；dollar cost/quality 使 planning 与 execution 在线交织；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW — [章节](../../../../books/part-07-agent/81-workflow.md) |
| [OpenAgenet / OAN White Paper: Open Infrastructure for Trusted Agent Interconnection](https://arxiv.org/abs/2606.03161v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；interconnection 前 identity/governance/freshness/authorization；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-MCP — [章节](../../../../books/part-07-agent/83-mcp.md) |
| [DECA: Decentralizing Block-Wise Adam for Efficient LLM Full-Parameter Fine-Tuning on Non-IID Data](https://arxiv.org/abs/2606.03209v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；decentralized FPFT state/communication/convergence；3+3+2=8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点“去中心化全参数微调必须显式切分 Optimizer Ownership” |
| [The Reliability Gap in Benchmark Auditing: Distribution Shift and Scale as Failure Modes of Contamination Detection](https://arxiv.org/abs/2606.03305v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；contamination detector 的 scale/drift FP/FN 边界；3+3+2=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Contamination Detector 必须随 Scale 与 Distribution 重新校准” |
| [The Security Budget of Code-LLM Prompt Hardening: Provable Limits Under Pass-Only Acceptance](https://arxiv.org/abs/2606.03308v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；pass-only filter 存在不可消除安全 floor；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Implement Kubernetes Pod-Level Remote Attestation for Confidential Workloads on dstack](https://arxiv.org/abs/2606.03323v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；LLMaaS confidential workload 绑定 Pod identity；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AI Model Extraction Attacks: Bypassing Single-Client Assumptions in Defenses](https://arxiv.org/abs/2606.03381v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；跨身份 aggregation 击穿 per-client 防护；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Extraction Budget 必须跨身份聚合” |
| [Demystifying Pipeline Parallelism: First Theory for PipeDream](https://arxiv.org/abs/2606.03498v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；pipeline stale block-SGD 的可核验边界；3+3+2=8 | 深入完成 | 已有覆盖：TRAIN-PIPELINE-PARALLEL — [章节](../../../../books/part-04-training-system/38-pipeline-parallel.md) |
| [Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI](https://arxiv.org/abs/2606.03518v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；delegation graph、scope 与 revoke 的组合授权；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点“多跳 Delegation 必须保留 Human Principal” |
| [CoEval: Ranking Language Models for Custom Tasks Without Labeled Data or Trustworthy Benchmarks](https://arxiv.org/abs/2606.03650v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；无可信标签时分离 model-selection authority 与 judge role；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Same Weights, Different Robot: A Deployment Safety View of VLA Policies](https://arxiv.org/abs/2606.03724v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；checkpoint 与 unnormalizer/controller 共同构成 executable policy；3+3+2=8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA — [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [E2LLM: Towards Efficient LLM Serving in Heterogeneous Edge/Fog Environments](https://arxiv.org/abs/2606.03770v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；heterogeneous edge/fog 的 split、placement 与 resource control；2+2+2=6 | 标准完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [AI Agents Enable Adaptive Computer Worms](https://arxiv.org/abs/2606.03811v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；Agent 使 worm 按目标生成 exploit strategy；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [TreeFlash: Parallel AR-Approximation for Faster Speculative Decoding](https://arxiv.org/abs/2606.03819v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；parallel tree draft 与 target verification；3+3+2=8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [RealClawBench: Live OpenClaw Benchmarks from Real Developer-Agent Sessions](https://arxiv.org/abs/2606.03889v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；真实 session 的 environment reconstruction 与 verification；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Agent libOS: A Runtime Substrate for Capability-Controlled Self-Evolving LLM Agents](https://arxiv.org/abs/2606.03895v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；operation/capability/resource/information-flow 三平面分权；3+3+3=9 | 深入完成 | 整合：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md)；正文锚点“快速演进的 Skill / Tool Layer 不能拥有 Primitive Effect Authority” |
| [NetKV: Network-Aware Decode Instance Selection for Disaggregated LLM Inference](https://arxiv.org/abs/2606.03910v1) | 2026-06-03T08:00:00+08:00 ～ 2026-06-03T09:00:00+08:00 | 不重复评分：V2.1 已处理；network cost oracle 进入 KV placement 与 TTFT SLO；3+3+2=8 | 深入完成 | 整合：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Network Cost Oracle 只提交 Placement Score” |

候选分母冻结为 88：87 个 arXiv Candidate 加 1 个厂商 release Candidate。39 项 surviving prior 为 32 Existing / 7 已写入正文；48 项恢复候选为 38 Existing / 9 已写入正文 / 1 Only report；Kimi Code release 为 Existing。全 88 项合计 71 Existing / 16 已写入正文 / 1 Only report / 0 proposal / 0 Deferred，exact-v1 blocker=0。五个旧 false-positive 与 627 个维持关闭项不进入 Evidence Gate。

## 4. 证据与知识整合

### [Kimi Code 0.7.0 / 0.8.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.7.0)

官方 GitHub Release 的不可变 `published_at` 分别为 `2026-06-02T02:23:53Z` 与 `2026-06-02T14:56:13Z`。release notes 把 goal 的 pause/resume/cancel/replace、后台提问、approval lifecycle hook 与 compaction todo 暴露为显式状态，证明的是当时公开的 interface/version fact；它没有证明跨崩溃恢复、exactly-once、长任务成功率或生产 SLO。`AGENT-WORKFLOW` 已把 workflow state、审批、checkpoint、恢复与 handoff 作为长期 owner，因此不重复写 Books。

旧 44 项的 exact-v1 evidence bodies 可读，并涵盖 RAG inference cost attack、Agent coordination、consent integrity、omnimodal world model、aggregate-only distributed adaptation、kernel portability、multi-segment KV、token-drift scheduling、online dedup、Agent harness/security、RL runtime、distributed training、evaluation 与 deployment safety。它们不是当前准入结论，但重冻后无需因排版重复全文阅读。

675 项 closure proposal 已全量 title sweep；边界项读取完整 abstract。旧模板被反例击穿后恢复 48 项，其他 627 项分别落入 embodied/local、incremental、benchmark、theory 或 vertical family。恢复项包括 acceptance-test release gate、coding-Agent handoff state、RAG/LLM inference control、Agent memory/skill、RLVR reward/data、KV、security 与评测结论修正；仅有架构名、局部 benchmark 或垂直任务者没有恢复。

Books trace-to-body 结果见 [`V3_RECOVERY_BLOCKERS.md`](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md)。39 个 prior 的 current body rejudgment 见 [`V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md`](../_sources/daily-20260603/V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md)：32 Existing / 7 已写入正文。恢复候选中 9 项已写入正文、38 项由现有命题级正文覆盖，另有 1 项仅保留日报；没有开放 Books proposal。

恢复候选第一批 8 项的 exact-v1 Evidence 与当前 Books comparison 见 [`V3_EVIDENCE_BATCH_01.md`](../_sources/daily-20260603/V3_EVIDENCE_BATCH_01.md)。

### [Cost-Aware Query Routing in RAG: Empirical Analysis of Retrieval Depth Tradeoffs](https://arxiv.org/abs/2606.02581v1)

手工 priors 与小 corpus 只支持受限 routing 实例；当前 RAG 已把 retrieval、compression、verification、stop 与成本组成联合 policy，故已有覆盖。

### [ReLoRA: Knowledge-Reusing Adaptation for Fast Rollout of Evolving LLM Services](https://arxiv.org/abs/2606.02606v1)

Re-adaptation 不能取消 base/adapter identity 与兼容性验收；当前 LoRA 与 Model Registry 已有版本迁移、隔离和重训 fallback。

### [Acceptance-Test-Driven Evaluation Protocols for Business-Centric LLM Systems](https://arxiv.org/abs/2606.02755v1)

Requirement compiler 只提交 evaluator proposal；当前 Evaluation 已有 EvalSpec、non-vacuous/meta-evaluation admission 与独立 release authority。

### [Which Defense Closes Which Threat? Attributing OWASP-LLM-Top-10 Coverage and Its Brittleness Under Paraphrasing](https://arxiv.org/abs/2606.02822v1)

四容器与 17 probes 不证明完整防御；当前 Security/Evaluation 已按 threat family、operating point 与 mutation slice 归因，故已有覆盖。

### [Thinking Past the Answer: Evaluating Harmful Overthinking in Large Reasoning Models](https://arxiv.org/abs/2606.02835v1)

Oracle prefix 揭示首次正确后的反向退化，但不能直接部署；当前 Scheduling/Evaluation 已分离 budget、stop sensor 与 answer commit。

### [Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks](https://arxiv.org/abs/2606.02875v1)

Structured note 的 changed files、validation、uncertainty 与 rollback risk 是当前 Workflow handoff acceptance contract 的字段化实例。

### [Linear Probes Detect Task Format, Not Reasoning Mode in Language Model Hidden States](https://arxiv.org/abs/2606.02907v1)

结果只击穿该实验的 reasoning-mode 解释；当前 Evaluation 已将 probe 限定为需 format control、random baseline 与 causal intervention 的 diagnostic sensor。

### [Fast-dLLM++: Fréchet Profile Decoding for Faster Diffusion LLM Inference](https://arxiv.org/abs/2606.02955v1)

Fréchet profile 仍只是 proposal selector；当前 Speculative Decoding 已明确 authoritative verification、token/KV commit 与 calibration/factorization fallback。

恢复候选第二批 8 项的 exact-v1 Evidence 与 Books comparison 见 [`V3_EVIDENCE_BATCH_02.md`](../_sources/daily-20260603/V3_EVIDENCE_BATCH_02.md)。

### [Predicting Inference-Time Scaling Gains from Labeled Validation-Set Output Statistics](https://arxiv.org/abs/2606.02981v1)

廉价 predictor 只能是 admission sensor；当前 Scheduling 已有 reasoning/sample budget、calibration 与 fixed-budget fallback。

### [TGV-KV: Text-Grounded KV Eviction for Vision-Language Models](https://arxiv.org/abs/2606.03075v1)

Text grounding 是 multimodal KV importance sensor；当前 KV owner 已有 modality/role、结构保护、revision identity 与 FullKV fallback。

### [DeltaMem: Large Language Models Acting as Incremental Learners](https://arxiv.org/abs/2606.03083v1)

Residual tree 不取得 truth authority；当前 Memory 已分离 raw evidence、derived state、conflict/freshness、versioned merge 与 rollback。

### [Learning to Solve, Forgetting to Retain: Correct-Set Turnover in RLVR](https://arxiv.org/abs/2606.03087v1)

GRPO 已在正文锚点“Mastered Set 需要 Acquisition–Retention Turnover Ledger”吸收 `mastered-set turnover ledger → review delay/repair window → pre-rollout replacement queue`，并保留固定 replay/canary 与预算不扩张边界。

### [The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs](https://arxiv.org/abs/2606.03092v1)

当前 Scheduling 已有 resource shadow price、reasoning allocation、future-recovery opportunity 与 hard reservation；本篇是受限 utility 实例。

### [Experience-Driven Dynamic Exits for LLMs with Reinforcement Learning](https://arxiv.org/abs/2606.03113v1)

Learned exit policy 只拥有 proposal；target verification 与 state commit 仍由当前 Speculative Decoding contract 承载。

### [Uncertainty-Aware Clarification in LLM Agents with Information Gain](https://arxiv.org/abs/2606.03135v1)

当前 Planning 已有 belief、information gain、action/delay/failure cost、hard override 与 user-confirmation fallback，故已有覆盖。

### [PsychoPass: Geometric Profiling of Multi-Turn Adversarial LLM Conversations](https://arxiv.org/abs/2606.03136v1)

长度去混淆后的 geometry 仍只是校准 sensor；Security 的 policy/tool authorization/effect mediation 保持最终 authority。

恢复候选第三批 8 项的 exact-v1 Evidence 与 Books comparison 见 [`V3_EVIDENCE_BATCH_03.md`](../_sources/daily-20260603/V3_EVIDENCE_BATCH_03.md)。

### [FederatedSkill: Federated Learning for Agentic Skill Evolution](https://arxiv.org/abs/2606.03143v1)

Agent Platform 已在“跨用户演进时，这一边界还要求把 private episode 与 shared skill revision 分开”吸收 local private trajectory→semantic patch→shared plan→personalized library commit，并保留 privacy/conflict gate 与 local-only fallback。

### [WebRISE: Requirement-Induced State Evaluation for MLLM-Generated Web Artifacts](https://arxiv.org/abs/2606.03220v1)

Interaction Contract Graph 是当前 EvalSpec 的 UI 实例；simulator 与 implicit requirement extraction 不能拥有 truth authority。

### [ARBOR: Online Process Rewards via a Reusable Rubric Buffer for Search Agents](https://arxiv.org/abs/2606.03239v1)

GRPO 已在正文锚点“Rubric Pool 还需要 Admission、Consolidation 与 Retirement”吸收可复用 rubric 的 lifecycle，并保留 terminal-verifier authority、drift quarantine 与静态 rubric fallback。

### [Multilingual Unlearning in LLMs: Transfer, Dynamics, and Reversibility](https://arxiv.org/abs/2606.03291v1)

Security 已在正文锚点“Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family”吸收 language/script transfer matrix、cross-language regain、reversibility 与受限删除结论。

### [Beyond Ideal Instruction: A Comprehensive Framework for Evaluating LLMs in Realistic Interactions](https://arxiv.org/abs/2606.03318v1)

当前 Evaluation 已分离 user state、bounded clarification、environment revision、outcome 与 user-experience diagnostics，故已有覆盖。

### [Calibration Data Trade-offs Across Capability Dimensions: Why Multi-Source Mixing Matters for High-Sparsity LLM Pruning](https://arxiv.org/abs/2606.03328v1)

当前 Evaluation 已要求 dense/pruned item transition、capability/calibration slices、真实 sparse runtime 与 rollback，平均分不承担 release gate。

### [FLIPS: Instance-Fingerprinting for LLMs via Pseudo-random Sequences](https://arxiv.org/abs/2606.03330v1)

当前 Model Registry 已将 prompt/template、sampler、quantization/runtime 纳入 instance identity，并把 fingerprint 限定为辅助证据。

### [RogueMerge: Robust and Unified Attacks against LLM Model Merging](https://arxiv.org/abs/2606.03344v1)

Security 已在正文锚点“Model Merge Input 是对权重的 Supply-chain Write Access”吸收第三方 merge input、隔离 composition 与 merged-artifact behavior gate。

恢复候选第四批 8 项的 exact-v1 Evidence 与 Books comparison 见 [`V3_EVIDENCE_BATCH_04.md`](../_sources/daily-20260603/V3_EVIDENCE_BATCH_04.md)。

### [ImageAuditor: Membership Inference Attack against Image-based Retrieval-Augmented Generation](https://arxiv.org/abs/2606.03354v1)

当前 Security 已把 membership、query identity、多查询相关性、false positive 与 isolation fallback 写入合同；图像是 modality-specific probe。

### [When Model Merging Breaks Routing: Training-Free Calibration for MoE](https://arxiv.org/abs/2606.03391v1)

Model Registry 已在正文锚点“MoE Merge 的发布身份还要包含 Router Calibration”吸收 merged weights、router calibration revision、expert-assignment regression 与 source-model fallback。

### [KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks](https://arxiv.org/abs/2606.03458v1)

KV owner 的“Quantization Objective 应对齐 Attention Distortion”已明确 repeated state feedback，并直接以 KVarN 的 pseudo-decode 证据约束 autoregressive accumulation；无需重复写入。

### [What Makes Interaction Trajectories Effective for Training Terminal Agents?](https://arxiv.org/abs/2606.03461v1)

当前 Data 已要求 trajectory 绑定 environment、harness、verifier、observation/action lineage 与 outcome canary，故已有覆盖。

### [DMF: A Deterministic Memory Framework for Conversational AI Agents](https://arxiv.org/abs/2606.03463v1)

当前 Memory 已分离 raw event、deterministic/derived state、lineage、decay/prune、conflict/freshness 与 full-history fallback。

### [StepFinder: A Temporal Semantic Framework for Failure Attribution in Multi-Agent Systems](https://arxiv.org/abs/2606.03467v1)

当前 Trace 已有 earliest evidence-backed failure span、responsibility、propagation 与 outcome binding，learned scorer 不能成为因果真值。

### [SAGE: A Quantitative Evaluation of Socialized Evolution in Agent Ecosystems](https://arxiv.org/abs/2606.03544v1)

当前 Evaluation/Multi-Agent 已要求 compute-matched counterfactual、history-channel identity、coordination tax 与 outcome，故已有覆盖。

### [Skill Is Not Document: A Query-Conditional Benchmark and Two-Stage Retriever for LLM Agent Skill Routing](https://arxiv.org/abs/2606.03565v1)

当前 Agent Platform 已要求 task/skill compatibility、dependency/conflict、permission hard gate 与 executable-set validation。

恢复候选第五批 8 项的 exact-v1 Evidence 与 Books comparison 见 [`V3_EVIDENCE_BATCH_05.md`](../_sources/daily-20260603/V3_EVIDENCE_BATCH_05.md)。

### [DDOR: Delta Debugging for Explainable Overrefusal Testing and Repair](https://arxiv.org/abs/2606.03601v1)

当前 Evaluation 已有 overrefusal/harmful counterpart、最小 mutation、oracle/meta-evaluation 与 repair regression；本篇提供受限实例，故已有覆盖。

### [Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs](https://arxiv.org/abs/2606.03647v1)

Evaluation 已在正文锚点“Attack Success Rate 不能压平 Attack Profile”吸收 attacker knowledge/access、适用性、自适应性、迁移性、危害、样本效率与指标 non-authority 边界。

### [Safety Measurements for Fine-tuned LLMs Should be Grounded in Capability](https://arxiv.org/abs/2606.03648v1)

当前 Evaluation 已要求 model/runtime/prompt/tool capability-matched configuration 与 paired canary，避免把能力变化误判为安全变化，故已有覆盖。

### [Diagnosing Knowledge Gaps in LLM Tool Use: An Agentic Benchmark for Novel API Acquisition](https://arxiv.org/abs/2606.03657v1)

当前 Tool Calling 已分离 tool discovery、schema acquisition、environment execution、argument/effect verifier 与 fallback，故已有覆盖。

### [SkillPyramid: A Hierarchical Skill Consolidation Framework for Self-Evolving Agents](https://arxiv.org/abs/2606.03692v1)

当前 Agent Platform 已有 skill candidate、dependency/conflict、validation、promotion、revoke 与 versioned library commit；层级归并不改变 owner，故已有覆盖。

### [Entropy Gate: Entropy Quenching for Near-Lossless Token Compression in LLM Pipelines](https://arxiv.org/abs/2606.03739v1)

只保留日报：embedding similarity 不能替代 downstream task correctness，且摘要报告的压缩问题仅 6/9 保持，不足以改变长期压缩或发布合同。

### [Tool-Aware Optimization with Entropy Guidance for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03762v1)

当前 GRPO 已要求 tool/environment outcome、trajectory admission、entropy/credit assignment 与 delayed consequence regression；本篇为具体优化实例，故已有覆盖。

### [Backdoor Unlearning Generalization: A Path Toward the Removal of Unknown Triggers in LLMs](https://arxiv.org/abs/2606.03785v1)

Security 已在正文锚点“Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family”吸收 `known trigger → held-out unknown family → activation-shift sensor → independent behavior/retain gate`。

恢复候选第六批 8 项的 exact-v1 Evidence 与 Books comparison 见 [`V3_EVIDENCE_BATCH_06.md`](../_sources/daily-20260603/V3_EVIDENCE_BATCH_06.md)。

### [Trading Human Curation for Synthetic Augmentation in RLVR](https://arxiv.org/abs/2606.03800v1)

当前 Data/GRPO 已将 sandbox、task、verifier、quality/learnable-zone gate、human/synthetic mix、held-out evaluation、lineage 与成本纳入同一训练数据合同；单 seed 的受限 substitution rate 不成为通用汇率。

### [Consistency Training Can Entrench Misalignment](https://arxiv.org/abs/2606.03810v1)

当前 Evaluation/Security 已要求任何 post-training artifact 重新运行 matched capability/safety behavior slices 与 distribution-shift canary；consistency objective 或 self-generated label 不能继承旧 verdict。

### [Synthesize and Reward -- Reinforcement Learning for Multi-Step Tool Use in Live Environments](https://arxiv.org/abs/2606.03892v1)

当前 Data 已有 executable environment、initial/final state、tool schema、task、verifier 与 row lineage；GRPO 已有 environment-owned transition、MCP candidate admission、programmatic reward 与 outcome authority，故已有覆盖。

### [Value-Aware Stochastic KV Cache Eviction for Reasoning Models](https://arxiv.org/abs/2606.03928v1)

当前 KV owner 已把 attention、value norm、entropy、position 与随机 reservoir 当作 eviction proposal，并要求 error-budget calibration、真实 packed/kernel 路径与 FullKV fallback；VaSE 是受限组合实例。

### [q0: Primitives for Hyper-Epoch Pretraining](https://arxiv.org/abs/2606.03938v1)

Pretraining 已在正文锚点“超多 Epoch 训练会把单一 Checkpoint 演进为模型群体状态”吸收 `single-model multi-epoch → population snapshot identity → chain-distillation lineage → held-out prior selection → inference-budget-specific member set`，并保留单模型和 distill-to-one fallback。

### [Quantifying Faithful Confidence Expression in Large Reasoning Models](https://arxiv.org/abs/2606.03969v1)

当前 Evaluation 已分离 white-box probe、token probability、自报 confidence 与 sample agreement，并要求 estimator-specific calibration、prompt variants、risk-coverage decision 与 independent outcome gate。

### [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories](https://arxiv.org/abs/2606.03979v1)

当前 Memory 已明确 external evidence 到 parameter consolidation 的条件分支，冻结 episodes、teacher/student、objective、checkpoint lineage、held-out evaluator、删除与 rollback；Sleep 是其中一种实现。

### [Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill](https://arxiv.org/abs/2606.03980v1)

当前 GRPO 已要求 reward/verifier identity、rubric/evidence provenance 与 independent outcome gate；Agent Platform 已把 skill definition、resources、permission、version、validation 与 revoke 作为可执行资产合同，故已有覆盖。

## 5. 缺口与下一步

无

## 6. 复核

复核者：独立 fresh-context 语义复核

结论：通过

严格题摘分母复核通过：719 个 arXiv identity = 87 Candidate + 632 Close，厂商源另有 1 个 release Candidate；旧前沿 44 = 39 + 5，旧 closure 675 = 48 + 627。10+10+10 fresh-context FP/FN 抽检没有发现新共享错误 family。88/88 Candidate 的 Evidence 与 Books Decision 已闭合，最终 disposition 为 71 Existing / 16 已写入正文 / 1 Only report，proposal=0、Deferred=0、exact-v1 blocker=0。逐项 anchor 均存在于 owner 章节顶层 `## Review notes` 之前；新增正文保留旧方案、约束变化、状态或控制 owner、trade-off、failure、fallback 与证据边界。
