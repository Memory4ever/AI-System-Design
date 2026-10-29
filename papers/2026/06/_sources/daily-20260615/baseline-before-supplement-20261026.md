# Daily Research — 2026-06-15

**规范：** V3
**窗口：** 2026-06-14T09:00:00+08:00 ～ 2026-06-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-11T14:55:01+08:00

## 1. 结论

canonical raw inventory 共 471 个身份；独立复核确认 title + 完整 abstract 筛选后的 44 个候选仍满足本项目贡献门槛，427 项在分母前关闭。候选中 13 项已在 Review notes 前形成完整正文机制链，31 项由既有命题级正文承载；相较复核前，将 10 项从 Integrate 降级为 Existing Coverage。ordinary pending、材料请求与 Books body writeback queue 均为 0；6 项新增正文已通过独立 post-write 终审，本日报 Complete。

当前合同评分已由非作者重新校准，不以已经深读或已经写入 Books 倒推高分。44 项现在分布为 `6 分 × 31、8 分 × 13`；既有 exact-v1 深审仍可复用，最低审阅等级按新分数表述。逐项旧分、新分和三维依据见 [current score recalibration](../_sources/daily-20260615/CURRENT_SCORE_RECALIBRATION_20260914.json)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ANTHROPIC | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-GOOGLE-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-META-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-QWEN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-DEEPSEEK | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MOONSHOT | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ZAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MINIMAX | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260615/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ARXIV | official first-public owner、canonical raw inventory 与全量题摘账本；逐项语义复核 471 个 raw identities，冻结 44 个候选、关闭 427 项 | 已检查 | 无 |

分母前关闭项均保留 identity、完整摘要 hash 与 family-specific reason；两轮 fresh-context 反向审计共恢复 17 个 false negatives。准入不使用关键词、章节可映射性或候选数量；本窗无 withdrawn retained family。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Tiara: A Programmable Line-Rate ISA for Remote Memory Access](https://arxiv.org/html/2606.13708v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 INFER-PD-DISAGGREGATION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-PD-DISAGGREGATION，[owner](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；正文锚点：Remote-memory 依赖链可以下沉，但只能执行受限程序 |
| [How Task Structure Limits Multi-Agent Success: An Information-Theoretic Analysis](https://arxiv.org/html/2606.13733v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；命题锚点：Topology 从部署前选择演进到运行时有界修复 |
| [Natively Unlearnable Large Language Models](https://arxiv.org/html/2606.13873v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DATA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：训练完成后再从共享 backbone 中精确移除某个来源 |
| [Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization](https://arxiv.org/html/2606.13949v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：从独立 Span 到关系感知的本地 Sanitization |
| [STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming](https://arxiv.org/html/2606.13968v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-GATEWAY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-GATEWAY，[owner](../../../../books/part-06-ai-infrastructure/62-gateway.md)；正文锚点：跨域推理必须分离 Control Channel 与 Token Stream |
| [Same-Origin Policy for Agentic Browsers](https://arxiv.org/html/2606.14027v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Prompt Injection 与 Tool Boundary |
| [Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents](https://arxiv.org/html/2606.14106v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：长期视觉流需要把 Entity Identity 从 Perception 中分离 |
| [SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills](https://arxiv.org/html/2606.14154v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Skill Poisoning 的真值是 Side Effect，而不是是否被调用 |
| [CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward](https://arxiv.org/html/2606.14179v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 TRAIN-GRPO 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；正文锚点：Tool Feedback 只能密化已有接口信息 |
| [SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing](https://arxiv.org/html/2606.14239v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Trial Evidence 不能直接提交为 Workflow Revision |
| [WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation](https://arxiv.org/html/2606.14275v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：Logical Memory Identity 与 Physical Locality 必须分层 |
| [PLAIground: SLO-Driven Runtime Model Selection for Compound AI Systems in the Edge-Cloud-Space Continuum](https://arxiv.org/html/2606.14356v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：Admission 也可以联合选择 Model、Quantization 与 Placement |
| [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](https://arxiv.org/html/2606.14470v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：从原始轨迹到派生策略：Memory 的演进不是无限追加 |
| [Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results](https://arxiv.org/html/2606.14516v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Evaluation Run 的平台对象模型 |
| [From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails](https://arxiv.org/html/2606.14517v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Availability 攻击从单模型开销扩展到动态路径 |
| [Behavioral Audit of Machine Unlearning Has a Privacy Cost](https://arxiv.org/html/2606.14518v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Unlearning 必须分开参数擦除与推理拒答 |
| [StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance](https://arxiv.org/html/2606.14571v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Longitudinal State：事实必须先于对话，读写路径必须分开审计 |
| [SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model](https://arxiv.org/html/2606.14574v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 AGENT-PLANNING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；命题锚点：学习到的 Transition 只能验证候选，不能提交环境事实 |
| [When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime](https://arxiv.org/html/2606.14589v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-MONITORING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点：Silent Failure 必须保留可行动的外部回执 |
| [Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens](https://arxiv.org/html/2606.14620v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-GENERATIVE-PARADIGMS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：Editable tokens 与 commit boundary |
| [When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks](https://arxiv.org/html/2606.14629v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 AGENT-REFLECTION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-REFLECTION，[owner](../../../../books/part-07-agent/80-reflection.md)；命题锚点：Critic Accuracy 不等于 Intervention Value |
| [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](https://arxiv.org/html/2606.14674v1) | 2026-06-15T08:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Component Priority 只能是 Action Evidence |

| [The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/html/2606.13685v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：从 Pass@k 到 Pass^k：能力覆盖与重复可靠性不是同一问题 |
| [Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces](https://arxiv.org/html/2606.13686v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-SECURITY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Safety Evaluation 的单位是 Run，不只是 Prompt |
| [$μ_0$: A Scalable 3D Interaction-Trace World Model](https://arxiv.org/html/2606.13769v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-WORLD-MODELS 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：从 RGB Rollout 到 Projective 4D Predictive State |
| [TASR: Training-Free Adaptive Stopping for Iterative Retrieval](https://arxiv.org/html/2606.13814v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-RAG 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；命题锚点：Query、Compression 与 Stopping 是联合 Policy |
| [Beyond Perplexity: UTF-8 Validity in Byte-aware Language Models](https://arxiv.org/html/2606.14122v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MODEL-TOKENIZER 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-TOKENIZER，[owner](../../../../books/part-02-model/11-tokenizer.md)；正文锚点：Byte-level generation 不能把 Protocol Validity 交给概率模型 |
| [Small LLMs: Pruning vs. Training from Scratch](https://arxiv.org/html/2606.14150v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-PRETRAINING 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；正文锚点：模型压缩的 Baseline 必须同时绑定训练预算与可执行粒度 |
| [Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL](https://arxiv.org/html/2606.14211v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-GRPO 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：outcome verifier 拥有 reward 方向，reflection/self-report 只提供传感信号 |
| [Selective Agentic Recovery for UAV Autonomy with a Persistent Mission Runtime](https://arxiv.org/html/2606.14219v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-PLATFORM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLATFORM，[owner](../../../../books/part-07-agent/84-agent-platform.md)；命题锚点：Agent Recovery State 超出 Transcript |
| [Decoupled Mixture-of-Experts for Parametric Knowledge Injection](https://arxiv.org/html/2606.14243v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MODEL-MOE 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-MOE，[owner](../../../../books/part-02-model/21-moe.md)；正文锚点：Parametric Knowledge Injection 需要隔离 Expert State 与 Backbone State |
| [AgentCyberRange: Benchmarking Frontier AI Systems in Realistic Cyber Ranges](https://arxiv.org/html/2606.14295v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Evaluation Identity 必须包含 Harness 与 Environment |

| [Efficient On-Device Diffusion LLM Inference with Mobile NPU](https://arxiv.org/html/2606.13740v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：INFER-TENSORRT-LLM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：专用加速器首先是一份 Workload Contract |
| [FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift](https://arxiv.org/html/2606.13817v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-WORLD-MODELS 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：已知 ego transition 与 residual scene dynamics 分离 |
| [Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning](https://arxiv.org/html/2606.13856v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-SFT 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-SFT，[owner](../../../../books/part-04-training-system/29-sft.md)；正文锚点：Fine-tuning 稳定性要监控 Output Collapse，而不只监控 Weight Distance |
| [Temporal Backtracking Search for Test-time Generative Video Reasoning](https://arxiv.org/html/2606.13861v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-GENERATIVE-PARADIGMS 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：视频推理搜索应回滚时间前缀，而不是重采样整条轨迹 |
| [PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation](https://arxiv.org/html/2606.13886v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-EMBODIED-VLA 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：模型只提出 action proposal，controller 与 safety envelope 拥有物理提交权 |
| [Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH](https://arxiv.org/html/2606.13994v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-SECURITY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：安全 Gate 沿跨步骤 cumulative intent 与 effect-time authorization 聚合 |
| [When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms](https://arxiv.org/html/2606.14200v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-MULTI-AGENT 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Agent reputation 必须按 skill 条件化并记录 zero-evidence state |
| [From Prompts to Responses: Dual-Sided Data Leakage and Defense in Split Large Language Models](https://arxiv.org/html/2606.14210v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-SECURITY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Split inference 的 activation 与训练梯度均属于可观察隐私面 |
| [When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs](https://arxiv.org/html/2606.14238v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-EMBODIED-VLA 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：Physical Safety 需要显式 Safety Envelope |
| [When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More](https://arxiv.org/html/2606.14476v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-TOOL-CALLING 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Tool Output 是 Observation，不是 Authority |
| [Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0](https://arxiv.org/html/2606.14598v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：INFER-TENSORRT-LLM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：Quantization 的收益必须来自真实 Low-bit Kernel Path |
| [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://arxiv.org/html/2606.14672v1) | 2026-06-15T00:00:00+08:00 ～ 2026-06-15T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-WORKFLOW 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：Parallel Agent 分支可以交付 KV State，但必须显式校准 |

## 4. 证据与知识整合

### [Tiara: A Programmable Line-Rate ISA for Remote Memory Access](https://arxiv.org/html/2606.13708v1)

**2606.13708 — Tiara: A Programmable Line-Rate ISA for Remote Memory Access**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Remote-memory indirection 可用 memory-side NIC 上预注册、静态可验证的 compact ISA 执行，把依赖链从多 RTT 收敛为一次 request。

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.13708v1 §4 Evaluation; §§4.5–4.6 AI workloads` 支持 `Graph, page-table, lock, MoE gather and disaggregated PagedAttention`；模型 `PagedAttention 8KB blocks; MoE 32 experts`；硬件 `FPGA-based memory-side NIC prototype`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.13708v1 §3 Tiara Design; compiler/verifier`；counterevidence locator：`arXiv:2606.13708v1 §6 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** line-rate operator 降低 RTT，却限制程序表达力并扩大 NIC TCB；复杂/动态逻辑仍需 CPU/RPC fallback。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13708v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `INFER-PD-DISAGGREGATION` owner 为 [books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。Review notes 前正文 `Remote-memory 依赖链可以下沉，但只能执行受限程序` 已形成 owner-level 机制链；本项已实际 Integrate。

### [How Task Structure Limits Multi-Agent Success: An Information-Theoretic Analysis](https://arxiv.org/html/2606.13733v1)

**2606.13733 — How Task Structure Limits Multi-Agent Success: An Information-Theoretic Analysis**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：MAS topology必须服从任务constraint graph；bounded communication下 minimum-cut information bottleneck 可决定应重构任务而非增加 agents/messages。

**State / data / control owner。** `AGENT-MULTI-AGENT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13733v1 §§2–4 constraint-graph model and information-theoretic bound`；evaluation locator 为 `arXiv:2606.13733v1 §5 synthetic and SWE-bench evidence`；counterevidence locator 为 `arXiv:2606.13733v1 No dedicated limitations section — typicality/capacity assumptions and empirical-scope boundary in §§2–5`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 理论边界依赖典型性与容量假设，不能当 runtime predictor；构图成本高，低耦合任务仍可用简单并行。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13733v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前命题级锚点为 `Topology 从部署前选择演进到运行时有界修复`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Natively Unlearnable Large Language Models](https://arxiv.org/html/2606.13873v1)

**2606.13873 — Natively Unlearnable Large Language Models**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：source-level unlearning若是硬需求，应在训练时把shared backbone与source-addressable sparse sinks分离，并把disable-sink作为部署revoke动作。

**State / data / control owner。** `TRAIN-DATA` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13873v1 §§3–4 NULL architecture and source-to-sink training`；evaluation locator 为 `arXiv:2606.13873v1 §5 Wikipedia/downstream/adversarial evaluations`；counterevidence locator 为 `arXiv:2606.13873v1 §6 limitations and source-label/model-scale/retraining comparison scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** source isolation增加参数/路由/lineage成本，source overlap或错误标签会破坏边界；有限规模接近retraining不证明法定删除或所有泄漏消失。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13873v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `TRAIN-DATA` owner 为 [books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)。Review notes 前正文 `训练完成后再从共享 backbone 中精确移除某个来源` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization](https://arxiv.org/html/2606.13949v1)

**2606.13949 — Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：UI Agent 的 observation 在离开设备前应由trusted local broker按sensitivity与task necessity执行keep/abstract/remove三态最小披露。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13949v1 §§3–4 MINIM local broker and contextual-integrity objective`；evaluation locator 为 `arXiv:2606.13949v1 §5 WebArena-derived UI evaluation`；counterevidence locator 为 `arXiv:2606.13949v1 §6 limitations and UI/task-distribution boundary`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 本地minimizer本身成为TCB且会误删任务关键元素；WebArena-derived结果不证明真实桌面隐私或任务成功。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13949v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `从独立 Span 到关系感知的本地 Sanitization`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming](https://arxiv.org/html/2606.13968v1)

**2606.13968 — STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：跨local/HPC/cloud推理要分离auth/job-dispatch control channel与encrypted token-stream data channel，并让tier routing/context summarization成为显式policy。

**State / data / control owner。** `PLATFORM-GATEWAY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13968v1 §§3–5 three-tier routing, dual-channel HPC streaming and proxy`；evaluation locator 为 `arXiv:2606.13968v1 §6 1,200-query and TTFT evaluation`；counterevidence locator 为 `arXiv:2606.13968v1 §7 limitations and institutional-HPC/network/model scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 多tier减少成本或数据外发却增加judge误路由、relay availability与上下文摘要损失；0.54s TTFT绑定作者网络/HPC。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13968v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-GATEWAY` owner 为 [books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md)。Review notes 前正文 `跨域推理必须分离 Control Channel 与 Token Stream` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Same-Origin Policy for Agentic Browsers](https://arxiv.org/html/2606.14027v1)

**2606.14027 — Same-Origin Policy for Agentic Browsers**

**问题与旧路径。** `Agentic browsers integrate autonomous AI agents into web browsers, enabling users to accomplish web tasks through natural-language instructions.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Agentic browser 的 origin policy 必须追踪 agent 读入数据的 origin label，在跨 origin 写入前由浏览器侧 detector 与 user confirmation gate 授权；传统 script-only SOP 不覆盖 agent 自身形成的数据通道。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** SOPBench 覆盖 50 个 source-sink 类别组合、5 个 agentic browsers 与 6 个 backbone LLM；BrowserOS-SOPGuard 报告 0.00 violation rate 与 2.07%–5.79% runtime overhead。 Method locator：`https://arxiv.org/html/2606.14027v1 — § exact-v1 anchor: SOPGuard`。Evaluation locator：`https://arxiv.org/html/2606.14027v1 — § exact-v1 evaluation anchor: SOPBench`。Benchmark identity：model=`Six backbone LLMs in the exact-v1 SOPBench matrix; no single-model aggregate`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`SOP violation rate, paired utility tests, and runtime overhead on SOPBench, Mind2Web, WebArena-Infinity, and REAL`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 合成页面与 BrowserOS 实现不证明任意浏览器、隐式推断数据或用户确认都安全；label propagation 与用户疲劳仍会失效。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14027v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Prompt Injection 与 Tool Boundary`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents](https://arxiv.org/html/2606.14106v1)

**2606.14106 — Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents**

**问题与旧路径。** `Graphical User Interface (GUI) agents are increasingly used to automate complex computer tasks across applications, websites, and operating systems.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** GUI memory 不应保存整屏即视为更多证据；应把成功动作压缩成 action-relevant crop，并把正常 retrieval 与错误恢复 memory 分开，以避免视觉上下文把 state error 转成 grounding/hidden-operation error。 Authoritative owner 是 `AGENT-MEMORY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** OSWorld、WebForge、AgentNetBench 的四类 failure audit；OSWorld/GPT-5.4-mini 上 AGMem 由 full-image memory 的 20.4% 提升到 27.2% accuracy。 Method locator：`https://arxiv.org/html/2606.14106v1 — § exact-v1 anchor: 3 AGMem: mitigating the side effects of visual memory`。Evaluation locator：`https://arxiv.org/html/2606.14106v1 — § exact-v1 evaluation anchor: 4 AGMem experiments`。Benchmark identity：model=`GPT-5.4-mini for the reported OSWorld AGMem result; additional GUI-agent settings remain bound to the exact-v1 matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task accuracy plus state, grounding, hidden-operation, and recovery-failure audit on OSWorld, WebForge, and AgentNetBench`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 裁剪和 recovery detector 都可能遗漏不可见 affordance；三套 GUI benchmark 不证明长期真实桌面 memory 的正确性。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14106v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `长期视觉流需要把 Entity Identity 从 Perception 中分离`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills](https://arxiv.org/html/2606.14154v1)

**2606.14154 — SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills**

**问题与旧路径。** `Large language model (LLM) agents increasingly extend their capabilities at runtime by loading Agent Skills, which pair natural-language specifications (SKILL.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Skill supply-chain audit 必须联合读取自然语言 SKILL.md 与可执行 code，因为两种模态可以分别无害、组合后才形成 payload；admission 需覆盖 13 类 cross-modal mutation 与 runtime effect。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 76 个 strongest-attack 样本与跨 Qwen2.5-Coder-7B-Instruct、GPT-4o-mini、GPT-5.4-mini/5.4 的 attack/defense comparison。 Method locator：`https://arxiv.org/html/2606.14154v1 — § exact-v1 anchor: SkillMutator`。Evaluation locator：`https://arxiv.org/html/2606.14154v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark identity：model=`Qwen2.5-Coder-7B-Instruct, GPT-4o-mini, GPT-5.4-mini, and GPT-5.4`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Attack success and defense comparison over 13 cross-modal attack categories and 76 strongest-attack samples`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 自动 mutation 与蒸馏轨迹只覆盖作者 taxonomy；静态 paired reading 仍不能证明运行时无动态依赖或 latent trigger。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14154v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Skill Poisoning 的真值是 Side Effect，而不是是否被调用`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward](https://arxiv.org/html/2606.14179v1)

**2606.14179 — CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward**

**问题与旧路径。** `We present CacheRL, a system for training small agent foundation models that achieves 92 percent process accuracy on multi-step tool-calling tasks, approaching GPT-5's 94 percent while requiring 100 times less compute.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 离线 tool-agent RL 可把 rollout 缓存分为精确/模糊/缺失层级，以 token mask 避免把 cache artifact 当 policy action，并让 reward 权重随 cache tier 改变。 Authoritative owner 是 `TRAIN-GRPO`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen3-4B-Thinking 迭代 SFT+GRPO；validation reward 0.43→0.78，process accuracy 92%，并以 GPT-5 的 94% 作受限比较。 Method locator：`https://arxiv.org/html/2606.14179v1 — § exact-v1 anchor: CacheAgentLoop`。Evaluation locator：`https://arxiv.org/html/2606.14179v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark identity：model=`Qwen3-4B-Thinking trained with SFT plus GRPO; GPT-5 used only as a bounded process-accuracy comparison`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Validation reward and process accuracy under exact, fuzzy, and missing cache tiers`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 摘要明确报告强 SFT 后 RL 增益有限；fuzzy cache 改变环境反馈，不能替代 live tool execution 或跨 policy probability correction。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14179v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `TRAIN-GRPO` owner 为 [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。Review notes 前正文 `Tool Feedback 只能密化已有接口信息` 已形成 owner-level 机制链；本项已实际 Integrate。

### [SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing](https://arxiv.org/html/2606.14239v1)

**2606.14239 — SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing**

**问题与旧路径。** `Agent skills are structured procedural packages that guide frozen LLM agents in specialized workflows.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Skill evolution 可用同一 task 的 with/without-skill paired trajectory 隔离行为 delta，再让固定 structural verifier gate Refine/Repair 与 rollback。 Authoritative owner 是 `AGENT-WORKFLOW`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 89 个 containerized tasks、8 个 professional domains；不访问 hidden tests、reference solutions 或 external rewards，平均 reward 73.9%。 Method locator：`https://arxiv.org/html/2606.14239v1 — § exact-v1 anchor: paired trajectory auditing`。Evaluation locator：`https://arxiv.org/html/2606.14239v1 — § exact-v1 evaluation anchor: 89 containerized tasks`。Benchmark identity：model=`Skill-evolving coding agents in the exact-v1 paired-run matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Fixed structural verifier and task reward over 89 containerized tasks in eight domains; no hidden tests, reference solutions, or external rewards exposed to the auditor`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 只可观察到的结构约束才能被 verifier 发现；paired runs 仍受模型随机性与 evaluator 共偏影响，不能证明 unobservable correctness。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14239v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Trial Evidence 不能直接提交为 Workflow Revision`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation](https://arxiv.org/html/2606.14275v1)

**2606.14275 — WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation**

**问题与旧路径。** `LLM-curated hierarchical knowledge bases, namely a tree-structured wiki whose nodes summarize an underlying corpus, have become a dominant substrate for retrieval-augmented applications, yet their storage layer is still treated as an implementation detail.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 层级知识库需要 path-indexed KV 原生持有 schema evolution：offline rewrite 以无 read-path lock 的一致性协议提交，budgeted navigation 在同一树上提供 anytime refinement。 Authoritative owner 是 `AGENT-MEMORY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** WeChat Official Account AI Assistant 部署与 AuthTrace；四类 query operator 对 relational/graph/filesystem backends，end-to-end correctness 63.2%。 Method locator：`https://arxiv.org/html/2606.14275v1 — § exact-v1 anchor: path-indexed key-value storage`。Evaluation locator：`https://arxiv.org/html/2606.14275v1 — § exact-v1 evaluation anchor: AuthTrace`。Benchmark identity：model=`Not Disclosed — no single model identity governs the storage/backend comparison`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`AuthTrace and four query operators over relational, graph, and filesystem backends; end-to-end answer correctness`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 单一产品 workload 与 schema induction 不能证明任意 corpus 的一致性或答案真实性；offline rewrite、path churn 与导航预算仍可能制造 stale read。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14275v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `Logical Memory Identity 与 Physical Locality 必须分层`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [PLAIground: SLO-Driven Runtime Model Selection for Compound AI Systems in the Edge-Cloud-Space Continuum](https://arxiv.org/html/2606.14356v1)

**2606.14356 — PLAIground: SLO-Driven Runtime Model Selection for Compound AI Systems in the Edge-Cloud-Space Continuum**

**问题与旧路径。** `Applications in the 3D Computing Continuum, which unifies edge, cloud, and space, require combining multiple AI tasks such as object detection, time-series analytics, and natural language processing into Compound AI systems.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** SLO-driven compound runtime 应把 task/data contract、可用 edge/cloud/space model profile 与 cooldown/threshold 状态交给在线 selector，而非固定一个最强模型。 Authoritative owner 是 `INFER-SCHEDULING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 两个 workflows；固定模型策略被报告最高 21× budget violation 或 4pp accuracy miss。 Method locator：`https://arxiv.org/html/2606.14356v1 — § exact-v1 anchor: CAIM Task and Data Contracts`。Evaluation locator：`https://arxiv.org/html/2606.14356v1 — § exact-v1 evaluation anchor: two workflows`。Benchmark identity：model=`Candidate edge, cloud, and space models enumerated in the two exact-v1 workflows`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Workflow-specific accuracy, latency, and resource-budget constraints; not a universal production SLO`；evaluator=`Constraint satisfaction, accuracy miss, and budget violation for runtime selection versus fixed-model policies`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 两条 workflow 与作者 profile 不能给通用 SLO；profiling drift、switching delay 与不可用 region 必须触发 fallback。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14356v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `Admission 也可以联合选择 Model、Quantization 与 Placement`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](https://arxiv.org/html/2606.14470v1)

**2606.14470 — GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge**

**问题与旧路径。** `Large language model reasoning leaves no trace once it is done.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Reasoning/memory 若以 commit、note 与 tag 保存可获得 replay/diff/merge，但准确率收益主要来自近重复检索；当 copyability 低于约 0.8 时，版本化 substrate 本身不产生方法迁移。 Authoritative owner 是 `AGENT-MEMORY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 跨多类 reasoning tasks 的 retrieval/copyability probes；作者保留并解释被撤回/反驳的早期结论。 Method locator：`https://arxiv.org/html/2606.14470v1 — § exact-v1 anchor: every scored thought is a commit`。Evaluation locator：`https://arxiv.org/html/2606.14470v1 — § exact-v1 evaluation anchor: 7 All Experiments at a Glance`。Benchmark identity：model=`Reasoning agents in the exact-v1 retrieval and copyability probes`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task score, retrieval reuse, and copyability across five substrates, two benchmarks, and two scales`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 负结果绑定模型、任务和 sampling budget；git lineage 提供可审计性，不证明记忆内容正确或新问题迁移。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14470v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `从原始轨迹到派生策略：Memory 的演进不是无限追加`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results](https://arxiv.org/html/2606.14516v1)

**2606.14516 — Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results**

**问题与旧路径。** `AI evaluations are widely used for testing and understanding progress.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Evaluation result 需要 source-agnostic result schema 与 instance-level output，把 model/benchmark/harness 元数据从分散 leaderboard 转成可复用 artifact。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 社区仓库快照含 22,235 models、2,273 benchmarks、31 formats，并提供 converters。 Method locator：`https://arxiv.org/html/2606.14516v1 — § exact-v1 anchor: 3 The Every Eval Ever Schema`。Evaluation locator：`https://arxiv.org/html/2606.14516v1 — § exact-v1 evaluation anchor: 7 Case Studies`。Benchmark identity：model=`Not Disclosed — repository records 22,235 models but does not evaluate one canonical model`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Schema conversion coverage and three case studies over 2,273 benchmarks and 31 source formats`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 统一字段不保证 score 语义可比、数据新鲜或 provenance 完整；community ingestion 仍需 validation。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14516v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Evaluation Run 的平台对象模型`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails](https://arxiv.org/html/2606.14517v1)

**2606.14517 — From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails**

**问题与旧路径。** `LLM-based guardrails have emerged as a highly effective defense against prompt injection and jailbreak attacks in autonomous agents.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Reasoning guardrail 也必须有 token/time/concurrency budget 与 fail-closed/fail-open policy；否则攻击者可让安全模型陷入长推理并通过共享 guardrail queue 放大为租户级 DoS。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 8 个 model backbones 上 13–63× token amplification；web/desktop/code/multi-agent deployments 中最高 148× latency amplification。 Method locator：`https://arxiv.org/html/2606.14517v1 — § exact-v1 anchor: beam-search optimization framework`。Evaluation locator：`https://arxiv.org/html/2606.14517v1 — § exact-v1 evaluation anchor: end-to-end real-world agent deployments`。Benchmark identity：model=`Eight guardrail backbones spanning Claude, GPT, Gemini, DeepSeek, and Qwen families as enumerated in exact-v1`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Guardrail token amplification and end-to-end agent latency amplification under optimized and structural payloads`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** beam-search payload 与作者部署不提供真实流量发生率；硬 cap 会产生安全 false negative，独立容量池也增加成本。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14517v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Availability 攻击从单模型开销扩展到动态路径`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Behavioral Audit of Machine Unlearning Has a Privacy Cost](https://arxiv.org/html/2606.14518v1)

**2606.14518 — Behavioral Audit of Machine Unlearning Has a Privacy Cost**

**问题与旧路径。** `The removal of learned data from Machine Learning models through Machine Unlearning (MU) has been widely studied; however, there has yet to be an agreed-upon scheme for auditing MU.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Machine-unlearning audit 在互不信任 owner/auditor 下必须显式记录 audit leakage budget；只查询模型行为的通用 audit 对 convex models 无法同时识别 insufficient unlearning 且不泄露 retained-set membership。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** convex model 的 information-theoretic result与实验，并在 non-convex models 上观察同类 privacy-audit tension。 Method locator：`https://arxiv.org/html/2606.14518v1 — § exact-v1 anchor: information-theoretic proof`。Evaluation locator：`https://arxiv.org/html/2606.14518v1 — § exact-v1 evaluation anchor: empirical results on convex models`。Benchmark identity：model=`Convex models for the theorem-backed experiments plus non-convex models for empirical scope testing`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Insufficient-unlearning detectability versus retained-set membership leakage under mutually distrustful owner and auditor`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 定理前提不覆盖所有深网、side information 或 cryptographic proof；行为审计失败也不证明某次 unlearning 合规。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14518v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Unlearning 必须分开参数擦除与推理拒答`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance](https://arxiv.org/html/2606.14571v1)

**2606.14571 — StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance**

**问题与旧路径。** `A central role of personal-agent memory is to turn stored information and prior interactions into future-oriented assistance.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Memory evaluation 要把 streaming observation→首次 evidence use→feedback incorporation→future reuse 拆成四个时序指标，不能用 stored 或单次 recall 代替未来辅助。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** EgoLife evidence anchors；8 个 memory systems、2 个 backbones 的两步 task sequences。 Method locator：`https://arxiv.org/html/2606.14571v1 — § exact-v1 anchor: two-step task sequence`。Evaluation locator：`https://arxiv.org/html/2606.14571v1 — § exact-v1 evaluation anchor: eight memory systems across two backbones`。Benchmark identity：model=`Eight memory systems across two backbone models in the exact-v1 StreamMemBench matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`First evidence use, storage, feedback incorporation, and future reuse over two-step task sequences with EgoLife evidence anchors`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 两步序列和 egocentric stream 不能证明长期 identity/tenure；成功储存、局部 feedback incorporation 都不等于后续行为可靠。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14571v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Longitudinal State：事实必须先于对话，读写路径必须分开审计`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model](https://arxiv.org/html/2606.14574v1)

**2606.14574 — SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model**

**问题与旧路径。** `Large language models (LLMs) are increasingly deployed as planners for autonomous agents in household environments.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Executable planning evaluator 必须让 symbolic world model 区分 immediate precondition failure、latent hazard 与 irreversible failure，并在 action commit 前运行 counterfactual foresight。 Authoritative owner 是 `AGENT-PLANNING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** kitchen world model含 77 actions、262 objects、约46,800 interactions；6 个 LLM，最佳 error-free plan 17%，latent failure最高56%。 Method locator：`https://arxiv.org/html/2606.14574v1 — § exact-v1 anchor: state machine executor`。Evaluation locator：`https://arxiv.org/html/2606.14574v1 — § exact-v1 evaluation anchor: six LLMs`。Benchmark identity：model=`Six LLMs in the exact-v1 Simmer matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Error-free plan rate plus immediate, latent, and irreversible failure classification in the symbolic kitchen world`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 人工符号世界只覆盖可编码 kitchen semantics；counterfactual simulator 不证明真实环境 fidelity，漏建 hazard 会形成假安全。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14574v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `AGENT-PLANNING` owner 为 [books/part-07-agent/79-planning.md](../../../../books/part-07-agent/79-planning.md)。Review notes 前命题级锚点为 `学习到的 Transition 只能验证候选，不能提交环境事实`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime](https://arxiv.org/html/2606.14589v1)

**2606.14589 — When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime**

**问题与旧路径。** `LLM agent systems increasingly run as long-lived autonomous runtimes: scheduling jobs, calling tools, maintaining memory, and pushing results to humans.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Long-lived Agent 的 silent failure 应按 environment quirk、assumption mismatch、error swallowing、fail-plausible narrative、operational omission 分类，并要求错误跨组件边界后仍以可行动 evidence 到达人。 Authoritative owner 是 `PLATFORM-MONITORING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 8 周、约40 scheduled jobs、8 providers；22 incidents/至少28 manifestations，4,286 unit tests 与827 governance checks。 Method locator：`https://arxiv.org/html/2606.14589v1 — § exact-v1 anchor: five-class mechanism-oriented taxonomy`。Evaluation locator：`https://arxiv.org/html/2606.14589v1 — § exact-v1 evaluation anchor: 22 incidents`。Benchmark identity：model=`Production runtime spanning eight model providers; individual incident-model mapping is not disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Manual incident reconstruction and five-class taxonomy over 22 incidents, backed by 4,286 tests and 827 governance checks`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 单一私人 production runtime、人工 postmortem 与小样本不提供事故率；audit 擅长回归阻断而非 ex-ante 预防。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14589v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-MONITORING` owner 为 [books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。Review notes 前正文 `Silent Failure 必须保留可行动的外部回执` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens](https://arxiv.org/html/2606.14620v1)

**2606.14620 — Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens**

**问题与旧路径。** `Open diffusion language models are marketed as parallel, non-autoregressive decoders, yet the order in which a shipped checkpoint actually commits its tokens is almost never measured.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Masked diffusion LM 的 token commit order 必须从 sampler accept events 测量；大批 simultaneous commit 使 token-level order 部分未定义，所谓 block size 可能只是观测粒度。 Authoritative owner 是 `MULTIMODAL-GENERATIVE-PARADIGMS`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** DiffusionGemma 26B、686 prompts、6 regimes；比较 commit granularity、confidence 与 task correctness。 Method locator：`https://arxiv.org/html/2606.14620v1 — § exact-v1 anchor: sampler accept step`。Evaluation locator：`https://arxiv.org/html/2606.14620v1 — § exact-v1 evaluation anchor: 686-prompt`。Benchmark identity：model=`DiffusionGemma 26B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Commit granularity, commit order, confidence, and task correctness over 686 prompts in six regimes`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 单一 checkpoint/sampler 的行为不定义整个 diffusion LM family；JSON、数学、事实任务间关系不可外推生产 latency。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14620v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-GENERATIVE-PARADIGMS` owner 为 [books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。Review notes 前正文 `Editable tokens 与 commit boundary` 已形成 owner-level 机制链；本项已实际 Integrate。

### [When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks](https://arxiv.org/html/2606.14629v1)

**2606.14629 — When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks**

**问题与旧路径。** `Verifier-driven self-DPO is a common recipe for self-improving production visual-language models.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Self-improving VLM 的 verifier 更新必须与 policy update 分离，并用 held-out new-task slice 与 rollback gate 防止 verifier在旧任务提升时对新任务回退。 Authoritative owner 是 `AGENT-REFLECTION`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 多任务 self-improvement experiments 与 verifier/policy ablations；指标只绑定作者 task/model matrix。 Method locator：`https://arxiv.org/html/2606.14629v1 — § exact-v1 anchor: 2 Production setup`。Evaluation locator：`https://arxiv.org/html/2606.14629v1 — § exact-v1 evaluation anchor: 3 Headline finding: silent failure on MMMU`。Benchmark identity：model=`Qwen-3-VL-2B and Qwen-2.5-VL-3B students with Qwen2.5-VL/Qwen3-VL verifier ladder from 3B to 8B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Held-out old-task and new-task performance on MathVista, MMMU, and BLINK with verifier/policy ablations`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 同源 verifier、policy 与 synthetic data 会共偏；held-out task 仍可能与部署分布不同，改善旧任务不能授权 promotion。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14629v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `AGENT-REFLECTION` owner 为 [books/part-07-agent/80-reflection.md](../../../../books/part-07-agent/80-reflection.md)。Review notes 前命题级锚点为 `Critic Accuracy 不等于 Intervention Value`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](https://arxiv.org/html/2606.14674v1)

**2606.14674 — AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition**

**问题与旧路径。** `LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Embodied scaffold evaluation 应把 perception、memory、reasoning、reflection、action 与 learning 表示为 typed components，在固定接口下做 controlled composition。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** DeliveryBench、ALFRED、MiniGrid、RoboTHOR 与多 backbone，测 component interaction 和 scaffold compatibility。 Method locator：`https://arxiv.org/html/2606.14674v1 — § exact-v1 anchor: AgentSpec`。Evaluation locator：`https://arxiv.org/html/2606.14674v1 — § exact-v1 evaluation anchor: DeliveryBench`。Benchmark identity：model=`Multiple backbone models composed with typed AgentSpec scaffold components`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task success and component-interaction ablations on DeliveryBench, ALFRED, MiniGrid, and RoboTHOR`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 四个环境与标准接口会屏蔽真实 integration cost；模块 swap 的相对收益不等于生产系统可组合性。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.14674v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Component Priority 只能是 Action Evidence`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/html/2606.13685v1)

**2606.13685 — The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation**

**问题、旧路径与约束变化。** 单次 LLM-as-a-Judge 标签在低风险筛选中成本最低，也便于快速比较。 judge 开始承担排行榜、reward-model 数据与 release gate 时，单次标签的不稳定性会被误当成模型差异。

**机制、State / data / control owner。** 同一 judge、prompt 与输入重复执行仍会产生判决翻转；评估系统应保存 trial distribution、position order 与 reliability curve，再决定需要多少次复测才能得到稳定 verdict。 EvalRun 持有 judge/version/prompt/order/trial seeds；评估 owner 才能把重复判决聚合为 release evidence。

**Evidence：proof / non-proof。** exact-v1 的 Method、Reliability Curves、Bias and Sensitivity、Limitations；实验只含 29 个任务、两个 OpenAI judge、pairwise/pointwise 各 50 次，不证明所有 judge 或任务需要相同复测次数。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 重复试验提高成本且无法消除系统性偏差；预算不足时回退确定性 scorer、人工仲裁或报告区间而非伪造单点真值。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `从 Pass@k 到 Pass^k：能力覆盖与重复可靠性不是同一问题`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces](https://arxiv.org/html/2606.13686v1)

**2606.13686 — Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces**

**问题、旧路径与约束变化。** 仅在 prompt 中声明约束能覆盖简单、显式的禁止条件。 Web Agent 的不可信指令来自可操作 UI，而不是只来自用户文本。

**机制、State / data / control owner。** 将七类 deceptive UI 注入可执行电商环境，分离页面诱导、agent observation 与最终 action receipt。 browser/environment 拥有页面状态，policy owner 拥有 effect authorization；模型输出只是 proposal。

**Evidence：proof / non-proof。** exact-v1 WebDecept method、VisualWebArena shopping evaluation 与 limitations；只证明受测电商 deceptive pattern，不证明开放 Web 的发生率。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 环境级注入提高真实性但覆盖有限；未知界面仍回退浏览器隔离、effect-time authorization 与人工确认。

**V3 Books Decision。** 当前 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前的 `Safety Evaluation 的单位是 Run，不只是 Prompt` 已覆盖该长期命题；本项为 `No Change — Existing Coverage`。

### [$μ_0$: A Scalable 3D Interaction-Trace World Model](https://arxiv.org/html/2606.13769v1)

**2606.13769 — $μ_0$: A Scalable 3D Interaction-Trace World Model**

**问题、旧路径与约束变化。** pixel-space video prediction 保留外观最完整，直接 action model 则最贴近具体 embodiment。 跨 embodiment 扩展时，稠密像素浪费容量，而 action label 又不可共享。

**机制、State / data / control owner。** 先从视频恢复语义关键点和全局对齐的 3D interaction trace，再由 permutation-equivariant Trace Expert 以 flow matching 预测轨迹；action expert 消费该可迁移 prior。 world-model owner 持有可版本化 3D trace 与事件条件；下游 controller 只消费预测轨迹，不反向把预测提交为环境事实。

**Evidence：proof / non-proof。** exact-v1 TraceExtract、Trace Expert、pretraining/adaptation experiments 与 limitations；证据覆盖 tabletop manipulation，不含 force/tactile/contact，也受感知栈误差影响。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 3D trace 提高迁移性但丢失接触动力学和外观细节；感知置信不足时回退 pixel model、真实 observation 与 embodiment-specific controller。

**V3 Books 复验。** 当前 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 在 Review notes 前已有命题级正文 `从 RGB Rollout 到 Projective 4D Predictive State`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [TASR: Training-Free Adaptive Stopping for Iterative Retrieval](https://arxiv.org/html/2606.13814v1)

**2606.13814 — TASR: Training-Free Adaptive Stopping for Iterative Retrieval**

**问题、旧路径与约束变化。** 固定 top-k 或最大轮数简单、可预测，在检索成本低且问题难度接近时仍合理。 迭代 RAG 中大量后续调用既不改变答案也不增加证据，却持续消耗 latency 与 token budget。

**机制、State / data / control owner。** 当连续轮答案规范化后一致且当前答案 logit margin 通过校准阈值时停止检索，把 stopping 从固定轮数改成 request-local sensor。 retrieval loop 持有 answer lineage、evidence set 与 stop sensor；最终回答/拒答 authority 仍由 evidence policy 决定。

**Evidence：proof / non-proof。** exact-v1 stopping predicate、BM25/dense retrieval extensions、3×2 distractor evaluation 与 limitations；固定阈值来自受测单元，不证明跨模型免校准。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 过早稳定可能锁定共同错误，margin 也不是事实置信度；分布漂移时回退最大轮数、证据覆盖 gate 或人工核验。

**V3 Books 复验。** 当前 [AGENT-RAG](../../../../books/part-07-agent/76-rag.md) 在 Review notes 前已有命题级正文 `Query、Compression 与 Stopping 是联合 Policy`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Beyond Perplexity: UTF-8 Validity in Byte-aware Language Models](https://arxiv.org/html/2606.14122v1)

**2606.14122 — Beyond Perplexity: UTF-8 Validity in Byte-aware Language Models**

**问题、旧路径与约束变化。** byte tokenization 能覆盖任意字节，避免 OOV，并让词表保持简单。 稀有或未见字符下，局部高概率 byte 组合仍可能形成非法 UTF-8。

**机制、State / data / control owner。** 对 byte-aware LM 单独测量 UTF-8 structural validity，而不是从 token loss/perplexity 推断输出一定可解码。 tokenizer/runtime 持有 decoder validity state；模型概率只提出 byte，不拥有协议合法性。

**Evidence：proof / non-proof。** exact-v1 355M 模型、80B 多语 token、四种语言与结构有效性协议；不证明所有 tokenizer/规模具有相同失效率。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 增量 validity gate 会限制采样并增加状态；纯 ASCII 或上层协议已强校验时旧路径仍可保留。

**V3 Books Decision。** 已写入 [MODEL-TOKENIZER](../../../../books/part-02-model/11-tokenizer.md) 正文 `Byte-level generation 不能把 Protocol Validity 交给概率模型`，并通过独立 post-write 终审。

### [Small LLMs: Pruning vs. Training from Scratch](https://arxiv.org/html/2606.14150v1)

**2606.14150 — Small LLMs: Pruning vs. Training from Scratch**

**问题、旧路径与约束变化。** 从大模型剪枝能复用已有能力，直接训练小模型则部署形态最简单。 只比较最终精度会把继承初始化、追加训练 token 与不可加速稀疏度混为一谈。

**机制、State / data / control owner。** 在 token-matched 预算下比较 pruned initialization 与 scratch，并区分 depth、width、fine-grained sparsity；压缩质量与硬件可执行收益是两个独立 Gate。 training run 持有 parent lineage、mask/granularity 与 token budget；runtime owner 独立证明目标硬件 speedup。

**Evidence：proof / non-proof。** exact-v1 Llama-3.1-8B、六类剪枝、0.5–0.8 ratio 与两种 token-matched setting；不证明所有架构或 sparse kernel 都获益。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 细粒度剪枝可能保留质量却没有硬件加速，粗粒度可执行但损失能力；无稳定 sparse runtime 时回退 dense small model。

**V3 Books Decision。** 已写入 [TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md) 正文 `模型压缩的 Baseline 必须同时绑定训练预算与可执行粒度`，并通过独立 post-write 终审。

### [Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL](https://arxiv.org/html/2606.14211v1)

**2606.14211 — Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL**

**问题、旧路径与约束变化。** 只按任务成败做 RL 最直接，也避免单独训练 critic。 Agent 即使看到错误回执仍可能错误判断自身成功，普通 outcome RL 不会稳定修正该 reflection gap。

**机制、State / data / control owner。** RefGRPO 将 agent 的反思判断与已观察到的 execution outcome 比较，增加 calibration bonus，修复 outcome reward 对自我评估状态缺少 credit assignment 的问题。 environment receipt 拥有结果真值；reflection 是可训练 sensor，reward pipeline 只按两者一致性更新 policy。

**Evidence：proof / non-proof。** exact-v1 RefGRPO、text-to-SQL experiments/ablations 与 limitations；只证明受测任务和反馈形式，不证明 self-report 成为事实 authority。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** bonus 依赖可判定 outcome，错误 verifier 会训练出错误自信；真值不可得时回退独立 evaluator 或不奖励反思。

**V3 Books 复验。** 当前 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前已有命题级正文 `outcome verifier 拥有 reward 方向，reflection/self-report 只提供传感信号`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Selective Agentic Recovery for UAV Autonomy with a Persistent Mission Runtime](https://arxiv.org/html/2606.14219v1)

**2606.14219 — Selective Agentic Recovery for UAV Autonomy with a Persistent Mission Runtime**

**问题、旧路径与约束变化。** 本地 waypoint/setpoint controller 在环境稳定时延迟最低、故障边界最清楚。 开放环境需要语义恢复，但每次远端推理都引入 latency、backend uncertainty 与不可验证建议。

**机制、State / data / control owner。** Persistent Mission Runtime 在本地持续掌握 flight/safety state，CVI gate 只在 no-progress 或任务歧义时请求远端 reasoner，并验证返回的恢复动作后再恢复原 policy。 local runtime 持有 mission state 与最终 actuator authority；远端 Agent 只拥有 bounded recovery proposal。

**Evidence：proof / non-proof。** exact-v1 architecture、400 次 Gazebo/PX4 runs 与单次 real demo；不证明复杂真实空域、通信故障或广泛 sim-to-real。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 选择性调用降低成本但 gate 可能漏报/误报；验证失败或链路中断时回退本地 safety controller、hover/land 或人工接管。

**V3 Books 复验。** 当前 [AGENT-PLATFORM](../../../../books/part-07-agent/84-agent-platform.md) 在 Review notes 前已有命题级正文 `Agent Recovery State 超出 Transcript`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Decoupled Mixture-of-Experts for Parametric Knowledge Injection](https://arxiv.org/html/2606.14243v1)

**2606.14243 — Decoupled Mixture-of-Experts for Parametric Knowledge Injection**

**问题、旧路径与约束变化。** RAG 易更新但只做 prompt-level 注入；普通 post-training 融合紧密却会修改共享参数。 高频领域知识更新要求减少 catastrophic forgetting、冲突与整模型重算。

**机制、State / data / control owner。** 将知识 expert 与 router 同 backbone 解耦，只在末端 FFN 组合输出，使知识版本可独立加载/撤销，并保留 backbone KV cache 复用。 knowledge registry 持有 expert/version，router 持有选择策略，backbone state 保持独立；末层组合才产生派生输出。

**Evidence：proof / non-proof。** exact-v1 Decoupled MoE method、约 300 corpus/small-base experiments 与 limitations；不证明大规模模型、所有知识冲突或通用优于 RAG。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 末层注入限制表达深度并增加 expert/router 生命周期；需要深层推理或可靠出处时回退 RAG/专门微调。

**V3 Books Decision。** 已写入 [MODEL-MOE](../../../../books/part-02-model/21-moe.md) 正文 `Parametric Knowledge Injection 需要隔离 Expert State 与 Backbone State`，并通过独立 post-write 终审。

### [AgentCyberRange: Benchmarking Frontier AI Systems in Realistic Cyber Ranges](https://arxiv.org/html/2606.14295v1)

**2606.14295 — AgentCyberRange: Benchmarking Frontier AI Systems in Realistic Cyber Ranges**

**问题、旧路径与约束变化。** CTF/单漏洞任务适合快速测量孤立技能。 frontier agent 的真实攻击链跨主机和多阶段，终点分数无法定位能力来源。

**机制、State / data / control owner。** 开放 cyber range 将服务发现、立足点、横向移动和验证 receipt 放进同一可复现实验环境。 harness/environment 持有可执行状态与 verifier，agent 只提交动作。

**Evidence：proof / non-proof。** exact-v1 110 vulnerabilities、15 applications、8 ranges、156 hosts 与 matched prompt/budget；不证明真实生产网络攻击成功率。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 真实环境提高诊断力但维护成本与双用途风险更高；高风险场景回退隔离 sandbox 与人工审批。

**V3 Books Decision。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Evaluation Identity 必须包含 Harness 与 Environment` 已覆盖该长期命题；本项为 `No Change — Existing Coverage`。

### [Efficient On-Device Diffusion LLM Inference with Mobile NPU](https://arxiv.org/html/2606.13740v1)

**2606.13740 — Efficient On-Device Diffusion LLM Inference with Mobile NPU**

**问题、旧路径与约束变化。** CPU-only dLLM 保留动态提交语义但移动端计算过慢；普通 NPU 图执行适合固定 shape。 token 逐步提交、允许 revision 与有限 NPU address space 同时出现。

**机制、State / data / control owner。** 以多 block speculative fill 保持 NPU dense work，以 CPU revision path 修正未稳定 token，并压缩/重映射 NPU-visible buffers。 runtime 持有 committed/revisable token state 与 buffer map；CPU correction 不能绕过最终 token commit。

**Evidence：proof / non-proof。** §§3–5 给出三项设计、端到端与分解实验；17–42x 只相对其 CPU baseline，且绑定受测手机、LLaDA-8B 与 prefix-cache 配置。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 双路径和 remap overlap 增加同步及内存管理复杂度；输出短或 NPU 图不支持时回退 CPU/GPU 或普通 block decoding。

**V3 Books 复验。** 当前 [INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 在 Review notes 前已有命题级正文 `专用加速器首先是一份 Workload Contract`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift](https://arxiv.org/html/2606.13817v1)

**2606.13817 — FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift**

**问题、旧路径与约束变化。** 只用短历史预测 action-conditioned transition，在惯性与风流很弱时合理。 长时隐变量会持续改变相同 action 的后果。

**机制、State / data / control owner。** 把短历史 object motion state 与长历史 ambient context 分解，并以 zero-context residual 隔离 base dynamics 和 drift。 模型维护两类 latent state；真实环境 observation 始终拥有纠错 authority。

**Evidence：proof / non-proof。** §§4–6 与 context zero/shuffle ablation 支持模拟水面载具中的分解作用，不证明真实流场或跨 embodiment 普适性。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 分解增强长 rollout，却依赖 latent identifiability；context 失真时回退短时模型和频繁真实观测。

**V3 Books 复验。** 当前 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 在 Review notes 前已有命题级正文 `已知 ego transition 与 residual scene dynamics 分离`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning](https://arxiv.org/html/2606.13856v1)

**2606.13856 — Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning**

**问题、旧路径与约束变化。** 固定初始化与权重级正则通常足以限制小规模 fine-tuning 漂移。 同配置仅改变 seed 仍可能出现 action-output collapse，且权重距离看不见 Jacobian null-space 内的退化。

**机制、State / data / control owner。** 用 patch-level output variance/covariance regularization、dropout 或更低 LR 约束预测表征。 trainer 持有 seed/run lineage 与 output-collapse sensor；机器人 success receipt 仍由环境给出。

**Evidence：proof / non-proof。** §§3–6 覆盖 7 methods、最多 13 seeds、3 LIBERO benchmark；0/21 对 1/13 是小样本诊断，不证明通用消除随机性。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 输出正则可能抑制必要的低方差动作；分布变化时仍需多 seed、held-out rollout 与更保守 LR。

**V3 Books Decision。** 已写入 [TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md) 正文 `Fine-tuning 稳定性要监控 Output Collapse，而不只监控 Weight Distance`，并通过独立 post-write 终审。

### [Temporal Backtracking Search for Test-time Generative Video Reasoning](https://arxiv.org/html/2606.13861v1)

**2606.13861 — Temporal Backtracking Search for Test-time Generative Video Reasoning**

**问题、旧路径与约束变化。** root-level best-of-N 简单且互相独立，在错误均匀分布时合理。 视频轨迹在扩散早期形成，后续 denoising 无法修复早期时序分支。

**机制、State / data / control owner。** 定位首个失败时间点，保留已验证 clean prefix，从该 anchor 继续 variable-K generation。 search controller 持有 prefix lineage、verifier receipt 与 restart budget；生成模型只提出后缀。

**Evidence：proof / non-proof。** §§3–5 与 matched-budget experiment/ablation 支持算法、导航、机器人任务；22.7% 对 0.7% 是严格 OOD 子集，不是通用视频质量结论。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** prefix verifier 错误会固化坏状态，且任意前缀恢复需要额外训练；定位不可靠时回退 root sampling。

**V3 Books Decision。** 已写入 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 `视频推理搜索应回滚时间前缀，而不是重采样整条轨迹`，并通过独立 post-write 终审。

### [PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation](https://arxiv.org/html/2606.13886v1)

**2606.13886 — PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation**

**问题、旧路径与约束变化。** temporal smoothing 在动作噪声小、接触简单时成本最低。 接触与动力学约束使平滑动作仍可能物理不一致。

**机制、State / data / control owner。** 在冻结 VLA 后增加 phase FSM 和 selective Euler–Lagrange gate，只修正被 dynamics oracle 判为不一致的 action。 VLA 拥有 proposal，physics gate 与低层 controller 拥有 effect-time commit。

**Evidence：proof / non-proof。** §§3–5 覆盖 LIBERO/Robosuite 与单个真实机械臂任务；不足 1ms 和最高提升值绑定其 oracle、平台与任务。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** oracle/FSM 误判会覆盖有效动作；模型不匹配时回退原 controller、safety envelope 或人工接管。

**V3 Books 复验。** 当前 [MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 在 Review notes 前已有命题级正文 `模型只提出 action proposal，controller 与 safety envelope 拥有物理提交权`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH](https://arxiv.org/html/2606.13994v1)

**2606.13994 — Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH**

**问题、旧路径与约束变化。** 逐 prompt 拒绝可阻断显式、单步的有害请求。 恶意目标可被拆成各自无害但累计有害的可执行子任务。

**机制、State / data / control owner。** benchmark 用图结构保存全局有害目标、分解路径与每步 effect receipt，测量组合后而非局部文本风险。 security monitor 持有跨 run causal/effect graph；单个 agent step 无权重置风险状态。

**Evidence：proof / non-proof。** §§3–5 与附录给出 DeCompBench 构造和受测 agents；只证明该生成与执行分布，不证明真实攻击发生率。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 跨步追踪增加误报和状态成本；低风险无副作用任务可保留局部 guard，但 action 链必须回退确定性 authorizer。

**V3 Books 复验。** 当前 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前已有命题级正文 `安全 Gate 沿跨步骤 cumulative intent 与 effect-time authorization 聚合`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms](https://arxiv.org/html/2606.14200v1)

**2606.14200 — When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms**

**问题、旧路径与约束变化。** 全局声誉在任务同质、行为平稳时是廉价协作信号。 skill 与情境异质后，历史平均会把无关成功转成过度信任，并可被低成本操纵。

**机制、State / data / control owner。** 用 conditional information value 检查当前证据是否足以减少 verification，再决定路由或复核。 协作层持有 task-conditioned trust state；执行者不能用自报信誉取得 commit authority。

**Evidence：proof / non-proof。** §§3–7 给出模型、真实数据 placement 与 adversarial analysis；理论依赖其观测与耦合假设。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 条件建模需要更多样本且会估错稀有技能；证据不足时回退独立验证，不做传递信任。

**V3 Books 复验。** 当前 [AGENT-MULTI-AGENT](../../../../books/part-07-agent/82-multi-agent.md) 在 Review notes 前正文 `Agent reputation 必须按 skill 条件化并记录 zero-evidence state` 已形成 owner-level 机制链；本项已实际 Integrate。

### [From Prompts to Responses: Dual-Sided Data Leakage and Defense in Split Large Language Models](https://arxiv.org/html/2606.14210v1)

**2606.14210 — From Prompts to Responses: Dual-Sided Data Leakage and Defense in Split Large Language Models**

**问题、旧路径与约束变化。** 把 token 留在 client 可避免直接上传原文。 server 仍能从 smashed representation 或反向更新恢复敏感数据。

**机制、State / data / control owner。** 攻击联合两端初始化与模型反演；防御则对 forward representation 和 backward signal 分别正则并分阶段训练。 client/server 边界必须记录可观察 tensor 与训练阶段；privacy owner 独立评估双向泄漏。

**Evidence：proof / non-proof。** §§4–8 覆盖攻击、防御与多项实验；只支持受测 split point、模型与数据，未构成密码学保证。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 双向正则会损害 utility 并增加训练耦合；高敏感数据仍回退本地执行、TEE/cryptography 或不共享。

**V3 Books 复验。** 当前 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前已有命题级正文 `Split inference 的 activation 与训练梯度均属于可观察隐私面`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs](https://arxiv.org/html/2606.14238v1)

**2606.14238 — When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs**

**问题、旧路径与约束变化。** 统一噪声阈值便于部署，在 ODD 单一时可用。 不同驾驶场景和决策复杂度会产生不同失效阈值与严重度。

**机制、State / data / control owner。** 以 scenario × perturbation severity 构造二维 safety envelope，而不是全局平均鲁棒性。 deployment policy 持有 ODD entry 与 fallback；VLA 分数只作为 sensor。

**Evidence：proof / non-proof。** §§3–7 支持其 driving VLA、扰动与 GMM bands；不证明真实道路频率或 envelope 跨模型稳定。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 细粒度 envelope 需要持续校准；未覆盖场景回退保守 controller 或拒绝自动驾驶。

**V3 Books Decision。** `[MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)` 在 Review notes 前已有 `Physical Safety 需要显式 Safety Envelope` 的长期命题；本项为 `No Change — Existing Coverage`。

### [When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More](https://arxiv.org/html/2606.14476v1)

**2606.14476 — When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More**

**问题、旧路径与约束变化。** 直接采用专用工具输出在工具可靠且问题匹配时最省 token。 更强 backbone 也可能近乎无条件服从冻结工具，能力提升不会自然产生选择判断。

**机制、State / data / control owner。** 用 tool/no-tool/alternative arms 与 held-out oracle headroom 区分调用能力和选择能力。 tool 返回 observation；agent policy 提案，verifier/authorizer 决定是否提交。

**Evidence：proof / non-proof。** §§3–6 覆盖 ogbn-arxiv/WikiCS、Qwen2.5 0.5B–7B 与多 seed；选择 gate 只恢复部分 headroom。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 额外 routing 也会无净收益；特征不足时回退强制交叉验证或禁用高风险工具。

**V3 Books Decision。** `[AGENT-TOOL-CALLING](../../../../books/part-07-agent/78-tool-calling.md)` 在 Review notes 前已有 `Tool Output 是 Observation，不是 Authority` 的长期命题；本项为 `No Change — Existing Coverage`。

### [Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0](https://arxiv.org/html/2606.14598v1)

**2606.14598 — Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0**

**问题、旧路径与约束变化。** W8A8 存储压缩在缺少 native kernel 时仍可减少容量。 若运行时立刻反量化到 bf16，标称 INT8 不会获得 tensor-core compute。

**机制、State / data / control owner。** 融合 int8×int8→int32 GEMM、按 token/channel dequant 与 bias epilogue，并按 shape autotune。 execution plan 持有实际 kernel/accumulator/scale identity；quantized artifact 名称不等于低比特执行。

**Evidence：proof / non-proof。** §§3–6 在 RTX3090/Ideogram4.0 给出 bit-exact、per-GEMM 与端到端结果；A100/B200 反例说明收益不普适。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 专用 kernel 增加维护与数值风险；非 Ampere 或 shape 不匹配时回退 bf16/FP8/NF4。

**V3 Books Decision。** `[INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)` 在 Review notes 前已有 `Quantization 的收益必须来自真实 Low-bit Kernel Path` 的长期命题；本项为 `No Change — Existing Coverage`。

### [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://arxiv.org/html/2606.14672v1)

**2606.14672 — Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows**

**问题、旧路径与约束变化。** 文本串接是最兼容的合并接口，也天然保留可读证据。 并行分支被串成单序列会丢失结构并重复 prefill。

**机制、State / data / control owner。** cache mapper 对独立 branch KV 做坐标校准，专门训练的 synthesizer adapter 从非顺序 cache 接口生成。 每个 worker 持有 branch cache identity；synthesizer 只消费已版本化映射，不把 cache 当共享可变真值。

**Evidence：proof / non-proof。** §§2–4 覆盖九个数据集及 ablation；2.5–11x TTFT 只绑定其模型、branch 数和 serving setup。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 隐藏 state handoff 降低可解释性且模型更新会破坏映射；不兼容时回退文本/结构化 artifact 合并。

**V3 Books Decision。** 已写入 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md) 正文 `Parallel Agent 分支可以交付 KV State，但必须显式校准`，并通过独立 post-write 终审。

### Books / semantic audit

Fresh-context 独立复核以 level-2 `Review notes` 为正文边界。44 个冻结候选中，13 项已有完整正文机制链，31 项有不依赖 source trace 的命题级覆盖。此次将 10 项仅能复述现有机制或局部 operating point 的提案降级；新增 6 项逐条核对唯一 canonical marker、正文边界、完整机制链和章节衔接，章末 trace、source marker 和 proposal artifact 均未被用作正文落地证明。

## 5. 缺口与下一步

无

ordinary pending、材料请求与 Books body writeback queue 均为 0。427 项已完成分母前关闭，不构成待办。

### Repository Changes

- 完成 471 个 raw identities 的逐项 title + 完整 abstract 语义复核，冻结 44 个 Candidate、关闭 427 项。
- 独立复核将 10 项 proposal 降级为 Existing Coverage；剩余 6 个 Integrate family 已写入 owner 正文并通过 post-write 终审。

## 6. 复核

当前来源再认证复核者：\`june_11_20_recert\`（独立于原报告作者）。当前合同来源再认证补齐十三个官方 Daily 源；未发现需恢复的独立候选，原 Candidate/Evidence/Books 结论保持不变。

复核者：june_15_16_independent_books_gate_reaudit（fresh context）
复核范围：471 个 raw identities 的 title + full abstract 准入、44 个 retained 的 evidence boundary、31 个 Existing anchor 与 13 个 Integration Decision；重点逐项复核原 23 个 Integrate。
复核结论：Candidate/Evidence 通过；Books 为 13 Integrated / 0 queued / 31 Existing；相较复核前降级 10 项；ordinary pending=0。
写后复核者：june_15_16_postwrite（fresh context）；6/6 新增正文通过唯一锚点、正文边界、机制链、证据边界与相邻语义检查。记录：`../_sources/daily-20260615/v3-independent-post-write-audit-20260911.json`。
结论：通过
