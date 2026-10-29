# Daily Research — 2026-06-17

**规范：** V3
**窗口：** 2026-06-16T09:00:00+08:00 ～ 2026-06-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T09:35:35+08:00

## 1. 结论

arXiv canonical raw inventory 共 534 个身份；本轮已逐项读取全部 title + 完整 abstract，冻结 50 个候选、以 family-specific reason 关闭 484 项。当前合同来源再认证另从 Z.ai 官方页恢复 1 个带精确发布时间的 GLM-5.2 候选，因此全日报为 51 个候选：15 个 Integrate 已在目标 Books 的首个顶层 Review notes 前形成可辨识机制链，36 个 Existing Coverage 已逐项复验。arXiv 原证据与写后终审保持有效；独立复核已确认新增官方来源候选的日期、机制边界与 Books 判断，当前没有可执行 pending。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ANTHROPIC | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-GOOGLE-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-META-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-QWEN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-DEEPSEEK | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MOONSHOT | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ZAI | 官方页给出 2026-06-16 16:00；GLM-5.2 / IndexShare 纳入候选并完成 Evidence/Books 判断；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MINIMAX | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260617/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ARXIV | 534-identity canonical raw inventory；逐项读取 title + 完整 abstract，冻结 50 Candidate / 484 Close，恢复 22 个旧宽池 false negative；owner 只在 official listing/announcement 可证明时迁移 | 已检查 | 无 |

分母前关闭项保留 identity、完整题摘 hash 与 family-specific closure。全量反向审计不以关键词、ROADMAP 可映射性或候选数量准入；本窗 22 个恢复项均已核验 official exact-v1，未发现 withdrawn retained family。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [GLM-5.2](https://www.zhipuai.cn/zh/research/161) | 2026-06-16T16:00:00+08:00 | 官方页披露跨四个稀疏层共享一个 query-aware indexer 的 `IndexShare`，具体改变 selector state 的刷新与复用边界；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；命题锚点：Sparse Attention 的两个 ownership 轴 |
| [The Price of Anarchy in Disaggregated Inference](https://arxiv.org/html/2606.17081v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-PD-DISAGGREGATION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-PD-DISAGGREGATION，[owner](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；正文锚点：从静态 Pool Ratio 到耦合的 SLO Control State |
| [Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work](https://arxiv.org/html/2606.17099v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Handoff 必须保留约束的 Action-binding Strength |
| [Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators](https://arxiv.org/html/2606.17104v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-PD-DISAGGREGATION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION，[owner](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；命题锚点：局部加速必须通过完整部署账本 |
| [Models Take Notes at Prefill: KV Cache Can Be Editable and Composable](https://arxiv.org/html/2606.17107v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：双向更新会撤销“共享 Prefix 永远不可变”的前提 |
| [Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs](https://arxiv.org/html/2606.17110v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：模型内部路由、训练数据与 Weight Repair 都进入攻击面 |
| [TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations](https://arxiv.org/html/2606.17122v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DATA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：另一分支把可撤销表示封装在带 passport 的 adapter / LoRA 中 |
| [Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems](https://arxiv.org/html/2606.17182v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；命题锚点：声明式协议约束 Transition，而不是相信参与者会协调 |
| [MemTrace: Probing What Final Accuracy Misses in Long-Term Memory](https://arxiv.org/html/2606.17328v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：用干预矩阵定位写入、检索与阅读失败 |
| [RISE: Relay Inference and Online Scheduling for Efficient Edge-Device Collaborative Diffusion Model Services](https://arxiv.org/html/2606.17378v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：迭代生成与流式会话需要显式 Progress State |
| [Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation](https://arxiv.org/html/2606.17383v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Confidence 要在 Belief、Action 与 Outcome 三层校准 |
| [Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving](https://arxiv.org/html/2606.17421v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：隐私不是一个开关，而是明文边界的重新分配 |
| [PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents](https://arxiv.org/html/2606.17467v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation](https://arxiv.org/html/2606.17518v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission |
| [Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery](https://arxiv.org/html/2606.17519v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-TOOL-CALLING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Tool Discovery 与选择 |
| [AoiZora: Topology-Aware Auto-Parallel Optimization for Inference of Diffusion Transformers](https://arxiv.org/html/2606.17566v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点：分布式 DiT Plan 必须经过编译后拓扑复排 |
| [Cordon: Semantic Transactions for Tool-Using LLM Agents](https://arxiv.org/html/2606.17573v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Durable Execution 与 Replay |
| [Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning](https://arxiv.org/html/2606.17591v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：从原始轨迹到派生策略：Memory 的演进不是无限追加 |
| [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/html/2606.17730v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：Persistent world state |
| [LUMEN: Coordinated Failure Recovery for Distributed LLM Serving](https://arxiv.org/html/2606.17787v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：MoE Failure Recovery 必须拥有 Request 与 Expert Generation |
| [AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor](https://arxiv.org/html/2606.17872v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：压缩后的答案正确不等于证据仍被保留 |
| [How Inference Compute Shapes Frontier LLM Evaluation](https://arxiv.org/html/2606.17930v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：生成迭代次数不能代替实际计算预算 |
| [RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving](https://arxiv.org/html/2606.17949v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-GATEWAY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-GATEWAY，[owner](../../../../books/part-06-ai-infrastructure/62-gateway.md)；命题锚点：Gateway、EPP 与 Engine Scheduler |
| [ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents](https://arxiv.org/html/2606.18037v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；命题锚点：视觉证据也必须有可追踪的 Claim–Evidence 生命周期 |
| [On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization](https://arxiv.org/html/2606.18121v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Coordination Failure |
| [All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code](https://arxiv.org/html/2606.18168v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Harness Optimization 的 Test Boundary 必须对优化器不可见 |
| [Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners](https://arxiv.org/html/2606.18198v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Skill Poisoning 的真值是 Side Effect，而不是是否被调用 |
| [Looped World Models](https://arxiv.org/html/2606.18208v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：Persistent world state |
| [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/html/2606.18247v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-EMBODIED-VLA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；正文锚点：Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限 |

<!-- full-raw-recovered-candidate-rows:start -->
| [Towards Distributed Inference of LLMs on a P2P Network](https://arxiv.org/html/2606.17059v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已实际写入正文；正文锚点：低带宽拓扑要联合预算 Hops、Bytes 与 Steps |
| [LineageMark: Multi-user White-box Watermarking for Contribution Tracing in Model Derivation Chains](https://arxiv.org/html/2606.17123v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[owner](../../../../books/part-06-ai-infrastructure/59-model-registry.md)；已实际写入正文；正文锚点：Producer provenance 与 consumer compatibility evidence 不能由一张 Model Card 混代 |
| [Statistical Foundations of LLM-based A/B Testing: A Surrogacy Framework for Human Causal Inference](https://arxiv.org/html/2606.17165v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已实际写入正文；正文锚点：Canary / A/B |
| [Rethinking Groups in Critic-Free RLVR](https://arxiv.org/html/2606.17250v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：Verifiable Reward 不等于每个样本都可学习 |
| [OTRO: Oblivious Tokenization Path with Square-Root ORAM](https://arxiv.org/html/2606.17358v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；已实际写入正文；正文锚点：Partial TEE 协议的秘密随机性不得跨请求复用 |
| [Dissecting model behavior through agent trajectories](https://arxiv.org/html/2606.17454v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLATFORM，[owner](../../../../books/part-07-agent/84-agent-platform.md)；命题锚点：Agent harness 必须把 model intent、实际 tool payload、environment result 与回送 context 做成双向可观测接口 |
| [Online LLM Selection via Constrained Bandits with Time-Varying Demand](https://arxiv.org/html/2606.17489v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：多轮 Routing 是带剩余预算的序列决策 |
| [MagicSim: A Unified Infrastructure for Executable Embodied Interaction](https://arxiv.org/html/2606.17511v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：Batched Environment 需要持久且可寻址的状态池 |
| [DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack](https://arxiv.org/html/2606.17574v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Cross-layer Evaluation 不允许下游成功掩盖上游故障 |
| [TivTok: Broadcasting Time-Invariant Tokens for Scalable Video Tokenization](https://arxiv.org/html/2606.17590v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已实际写入正文；正文锚点：Codec-aware tokenization：稀疏性可以在视觉 Encoder 之前暴露 |
| [The Benchmark Illusion: Pruned LLMs Can Pass Multiple Choice but Fail to Answer](https://arxiv.org/html/2606.17609v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已实际写入正文；正文锚点：压缩模型的 release gate 也不能停留在平均 perplexity |
| [Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering](https://arxiv.org/html/2606.17799v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Beyond Native Success: Auditing Deployment-Interface Exposure of CLIP Backdoors](https://arxiv.org/html/2606.17815v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Embedding 也是可执行数据供应链的一部分 |
| [Small Initialization Matters for Large Language Models](https://arxiv.org/html/2606.17945v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；命题锚点：Optimizer 不是与参数化无关的旋钮 |
| [SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs](https://arxiv.org/html/2606.17952v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-MOE，[owner](../../../../books/part-02-model/21-moe.md)；命题锚点：从固定 Top-k 到受总预算约束的 Variable-k |
| [VoidPadding: Separate Padding from Semantic Termination in Masked Diffusion Language Models](https://arxiv.org/html/2606.17999v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已实际写入正文；正文锚点：固定长度 Diffusion 把长度预测变成 Admission 决策 |
| [Recursive Scaling in Masked Diffusion Models](https://arxiv.org/html/2606.18022v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER，[owner](../../../../books/part-02-model/17-transformer-layer.md)；命题锚点：Parameter Depth 与 Execution Depth 可以分离 |
| [Latency Prediction for LLM Inference on NPU Systems](https://arxiv.org/html/2606.18042v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：从直接 Grid Search 到 Floor-first Diagnosis |
| [Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping](https://arxiv.org/html/2606.18120v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Instruction Hierarchy 必须携带 Authenticated Provenance |
| [Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers](https://arxiv.org/html/2606.18206v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER，[owner](../../../../books/part-02-model/17-transformer-layer.md)；命题锚点：Parameter Depth 与 Execution Depth 可以分离 |
| [Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification](https://arxiv.org/html/2606.18249v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已实际写入正文；正文锚点：统一架构不等于双向可用的统一语义空间 |
| [Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/html/2606.18250v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：从 RGB Rollout 到 Projective 4D Predictive State |
<!-- full-raw-recovered-candidate-rows:end -->


## 4. 证据与知识整合

### [The Price of Anarchy in Disaggregated Inference](https://arxiv.org/html/2606.17081v1)

**2606.17081 — The Price of Anarchy in Disaggregated Inference**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：PD disaggregation controller应联合感知P/D pool、hierarchical KV cache与routing congestion的externality，并在saturation knee后切换cache affinity/load balance。

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17081v1 §§3–6 coupled games, PoA estimator and adaptive controller`；evaluation locator 为 `arXiv:2606.17081v1 §§7–8 three-node B200 Dynamo evaluation`；counterevidence locator 为 `arXiv:2606.17081v1 §9.2 analytical-only P/D game; topology/model/grid-point limitations`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** controller以13% throughput换饱和期PoA/尾延迟改善；证据仅3-node B200、两模型与特定P:D topology，不是通用阈值。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17081v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-PD-DISAGGREGATION` owner 为 [books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。Review notes 前正文 `从静态 Pool Ratio 到耦合的 SLO Control State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work](https://arxiv.org/html/2606.17099v1)

**2606.17099 — Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：software delegation contract应把task、bounded authority、returned evidence bundle与acceptance context作为reviewable work package，而非只看hidden tests通过。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17099v1 §§3–4 contract conditions and review protocol`；evaluation locator 为 `arXiv:2606.17099v1 §5 64-run/192-review pilot`；counterevidence locator 为 `arXiv:2606.17099v1 §6 limitations and small TypeScript/model-reviewer scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 显式contract以13% tokens和38% wall time换reviewability；pilot不证明correctness提升。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17099v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Handoff 必须保留约束的 Action-binding Strength`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators](https://arxiv.org/html/2606.17104v1)

**2606.17104 — Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：accelerator evaluation必须拆开Prefill TTFT与Decode TPOT/throughput，并把batch/network条件带入heterogeneous PD placement决策。

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17104v1 §§3–4 phase-aware cross-accelerator methodology`；evaluation locator 为 `arXiv:2606.17104v1 §5 Llama2-7B GPU/Groq evaluation`；counterevidence locator 为 `arXiv:2606.17104v1 §6 limitations and common-model/unsupported-batching/network scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 单模型与特定accelerator不构成采购排名；decode低TPOT可在batch throughput下反转。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17104v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-PD-DISAGGREGATION` owner 为 [books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。Review notes 前命题级锚点为 `局部加速必须通过完整部署账本`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Models Take Notes at Prefill: KV Cache Can Be Editable and Composable](https://arxiv.org/html/2606.17107v1)

**2606.17107 — Models Take Notes at Prefill: KV Cache Can Be Editable and Composable**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：KV cache应被视为prefill写入的memoized downstream conclusions；edit需append erratum，compose需RoPE reposition与identity-compatible splice。

**State / data / control owner。** `INFER-KV-CACHE` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17107v1 §§3–5 causal note model, editing and composition`；evaluation locator 为 `arXiv:2606.17107v1 §6 twelve-model/vLLM evaluation`；counterevidence locator 为 `arXiv:2606.17107v1 §7 limitations and CoT/model/layout/cache-compatibility scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 无CoT edit可能被忽略，splice依赖model/layout/position identity；高hit与latency结果不证明任意context可安全改写。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17107v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `双向更新会撤销“共享 Prefix 永远不可变”的前提`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs](https://arxiv.org/html/2606.17110v1)

**2606.17110 — Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：攻击者可通过 loss-landscape poisoning 使后续 fine-tuning 提取未见训练数据；data provenance 与 update admission 必须联合审计。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17110v1 §2 Assumptions and Threat Models; §3 LLP Attack Principles`；`arXiv:2606.17110v1 §§4–7 direct-model, federated, data-poisoning and DP-evasion evaluations`；counterevidence `arXiv:2606.17110v1 Appendix C Defenses Against Poisoning Attacks in FL; threat-model scope in §2`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** LLP 展示特定 poisoning 可诱导未见数据提取，不证明任意微调都会泄漏；provenance/admission 增加训练摩擦，可疑 update 应隔离并回退可信 checkpoint。


仅使用 `https://arxiv.org/html/2606.17110v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `模型内部路由、训练数据与 Weight Repair 都进入攻击面`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations](https://arxiv.org/html/2606.17122v1)

**2606.17122 — TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：instant unlearning 可把 passport 嵌入 LoRA 表示并以 authority-mediated verification 验证配置，但 deactivate credential 不自动证明所有信息删除。

**State / data / control owner。** `TRAIN-DATA` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17122v1 §3 Method (§3.2 auditable unlearning; §3.3 passport composition; §3.4 verification/tolerance)`；`arXiv:2606.17122v1 §4 Experiments (§4.1 setup/metrics; §4.2 single/multi-class); Appendices D–H`；counterevidence `arXiv:2606.17122v1 §5 Discussion (§5.1 Scope and limitations); Appendix B.2 scaling limits; Appendix H reconstruction attack`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** passport 验证只证明配置/凭证状态，不等价于所有信息已从 backbone 删除；hypernetwork 与密钥管理增加复杂度，重构攻击或 retain gate 失败时回退重训/隔离。


仅使用 `https://arxiv.org/html/2606.17122v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `TRAIN-DATA` owner 为 [books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)。Review notes 前正文 `另一分支把可撤销表示封装在带 passport 的 adapter / LoRA 中` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems](https://arxiv.org/html/2606.17182v1)

**2606.17182 — Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：并发 MAS 需要显式 happens-before、shared-state conflict 与 side-effect serialization，并在运行前后验证 anomaly-free execution。

**State / data / control owner。** `AGENT-MULTI-AGENT` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17182v1 §II Runtime Model; §III Anomaly Catalog; §IV Consistency Lattice; verified runtime sections`；`arXiv:2606.17182v1 formal witnesses, TLAPS checks and Verus spec/runtime refinement in §§III–IV; implementation/evaluation appendices`；counterevidence `arXiv:2606.17182v1 §II-B simplifying assumptions; §III-D split-view outside single-store model; realizability frontier §IV-C`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 形式化 detector 只覆盖论文 single-store runtime 与列出的 anomaly，不证明 split-view 等外部一致性；序列化牺牲并行度，模型假设不成立时回退单写者或事务存储。


仅使用 `https://arxiv.org/html/2606.17182v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前命题级锚点为 `声明式协议约束 Transition，而不是相信参与者会协调`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [MemTrace: Probing What Final Accuracy Misses in Long-Term Memory](https://arxiv.org/html/2606.17328v1)

**2606.17328 — MemTrace: Probing What Final Accuracy Misses in Long-Term Memory**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：long-term memory 评价应在 final accuracy 之外对 construction/retrieval/injection 节点做 counterfactual attribution。

**State / data / control owner。** `AGENT-MEMORY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17328v1 §3 MemTrace (§3.1 data; §3.2 probes; §3.3 metrics; §3.4 diagnostic views)`；`arXiv:2606.17328v1 §4 Experiment and Findings (§4.1–4.5 maintenance, evidence conflict and failure attribution)`；counterevidence `arXiv:2606.17328v1 Appendix C Failure-Origin Checks; Appendix D judge reliability; Appendix E sensitivity`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** MemTrace 的 retrieval-versus-use 归因已由 Ch77 现有 memory pipeline counterfactual owner 覆盖，不证明 judge 与接口敏感性已经消失；因此回退既有 owner，本次 No Change 而非重复写入。


仅使用 `https://arxiv.org/html/2606.17328v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `用干预矩阵定位写入、检索与阅读失败`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [RISE: Relay Inference and Online Scheduling for Efficient Edge-Device Collaborative Diffusion Model Services](https://arxiv.org/html/2606.17378v1)

**2606.17378 — RISE: Relay Inference and Online Scheduling for Efficient Edge-Device Collaborative Diffusion Model Services**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：edge collaborative diffusion serving 需要 relay placement、partial denoising state 与 online queue/SLO scheduler 共同决策。

**State / data / control owner。** `INFER-SCHEDULING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17378v1 §III Proposed Methodology (§III-A motivation; §III-B relay); §IV Algorithm Design (§IV-A–C formulation, LinUCB and reward)`；`arXiv:2606.17378v1 §V Experiment (§V-A setup; §V-B relay; §V-C sensitivity; §V-D scheduling; §V-E ablation)`；counterevidence `arXiv:2606.17378v1 §V-C parameter sensitivity; §V-E ablation; §VI Conclusion`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** RISE 的 relay/scheduler 收益只绑定所测 diffusion、设备和 network，不证明其他链路同样获益；partial denoising state 迁移失败会同时伤质量和 SLO，回退本地完整推理或静态 placement。


仅使用 `https://arxiv.org/html/2606.17378v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前正文 `迭代生成与流式会话需要显式 Progress State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation](https://arxiv.org/html/2606.17383v1)

**2606.17383 — Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：Agentic AI model validation 应分别检查 belief-state filter、forecast transition 与 policy action，并以 POMDP identity 绑定三层误差。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17383v1 §2 POMDP Representation; §3 Validation Framework (§3.1 belief; §3.2 forecast; §3.3 policy; §3.4 utility)`；`arXiv:2606.17383v1 §5 Portfolio Case Study; §6 Empirical Validation (§6.1–6.12 design, calibration, drawdown, ablation and sensitivity)`；counterevidence `arXiv:2606.17383v1 §4 Model Risk (§4.1–4.7); §6.11 assumptions; §6.12 interpretation`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** POMDP 三层 validation 在单一 portfolio case 演示，不能升级为一般 Agent 合规证明；latent-state/model risk 未闭合时回退规则策略与人工风险限额。


仅使用 `https://arxiv.org/html/2606.17383v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Confidence 要在 Belief、Action 与 Outcome 三层校准`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving](https://arxiv.org/html/2606.17421v1)

**2606.17421 — Bifrost: Hybrid TEE–FHE Inference for Privacy-Preserving Transformer and LLM Serving**

**问题与机制变化。** 机密推理不能把 TEE 与 FHE 当互斥标签；应按算子泄漏面、密文代价与 PD 数据路径划分 trust boundary，并记录跨边界转换和 fallback。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17421v1 §3 Bifrost System Design; §4 Implementation`；Evaluation=`arXiv:2606.17421v1 §5 Evaluation`；Counterevidence=`arXiv:2606.17421v1 §6.2 Limitations`。Workload=`privacy-preserving transformer/LLM serving across hybrid TEE–FHE partitions`；Model=`GPT-2 (124M) and Qwen3 (0.6B)`；Hardware=`One server with 24 vCPUs, 128 GiB RAM, Intel TDX and one NVIDIA H20 96 GiB GPU`；Evaluator=`latency, communication and privacy/security analyses in §5`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 混合边界减少 FHE 覆盖却扩大 TEE TCB 与转换面；实验不证明 host I/O、side channel 或任意模型部署安全。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17421v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `隐私不是一个开关，而是明文边界的重新分配`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents](https://arxiv.org/html/2606.17467v1)

**2606.17467 — PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents**

**问题与机制变化。** 专业文档 RAG 的 ingestion 需保留 provenance-aware sanitization、可追溯 rejection 与 utility check，不能把 paraphrase 或通用文本过滤当作 indirect-instruction 清除证明。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17467v1 §3 PARSE provenance-aware sanitization pipeline`；Evaluation=`arXiv:2606.17467v1 §4–§5 122-task, five-domain evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17467v1 has no dedicated limitations section; exact-v1 counterevidence is localized at limitations discussion on real-document/domain coverage and paraphrase failure`。Workload=`122 adversarial-document tasks: financial 24, legal 25, medical 23, scientific 25, DevOps 25`；Model=`Claude Sonnet 4.5 task generator; Haiku and Sonnet Parse calls; Llama Guard 4 baseline`；Hardware=`Not Disclosed`；Evaluator=`attack success rate, task utility and ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更强 sanitization 会删除有用内容并依赖 parser/provenance quality；受测文档与攻击不证明开放语料安全。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17467v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前正文 `RAG 安全必须覆盖完整状态生命周期` 已形成 owner-level 机制链；本项已实际 Integrate。

### [SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation](https://arxiv.org/html/2606.17518v1)

**2606.17518 — SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation**

**问题与机制变化。** Agentic kernel search 可在主 reasoning 继续时 speculative 生成候选，并行执行 validation/profile；控制面还必须协调 GPU pool、候选 lineage 与远端 KV/temporary state。

**State / data / control owner。** `INFER-TENSORRT-LLM` 是唯一知识 owner；`Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17518v1 §3 SpecGen design; §4 speculative generation and resource coordination`；Evaluation=`arXiv:2606.17518v1 §5–§6 kernel-optimization evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17518v1 has no dedicated limitations section; exact-v1 counterevidence is localized at discussion of spare-GPU, remote-KV and workload/hardware dependence`。Workload=`10 KernelBench Level-1 tasks and 10 Level-2/3 tasks; 100 search iterations per task; 40 timed runs after 10 warmups`；Model=`GLM-5.1 served by vLLM; DeepSeek-V4-Pro official API in high-reasoning mode`；Hardware=`Up to 18 NVIDIA H200 GPUs with NVLink and RoCEv2; Intel Xeon Platinum 8558 host`；Evaluator=`kernel correctness, optimization time and throughput/speedup comparisons`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 投机扩大并行度也制造无效候选、额外显存和验证争用；H200 kernel-search结果不是任意 compiler/runtime 加速保证。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17518v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前命题级锚点为 `Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery](https://arxiv.org/html/2606.17519v1)

**2606.17519 — Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery**

**问题与机制变化。** 大工具目录的 routing loss 应拆成 retrieval gap 与 confusion gap；平台需分别治理 candidate recall、semantic overlap、排序偏置与 clarification fallback。

**State / data / control owner。** `AGENT-TOOL-CALLING` 是唯一知识 owner；`Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17519v1 §3 Experimental Setup; §4.1 two-component decomposition`；Evaluation=`arXiv:2606.17519v1 §5.1–5.5 shortlisting, production validation and error analysis`；Counterevidence=`arXiv:2606.17519v1 Limitations after §7; single enterprise catalog and interface differences`。Workload=`4,105 synthetic queries and 1,435 human-labelled production queries over a catalog of 110 agents and 584 tools`；Model=`GPT-5.1, GPT-5.4 and Claude Sonnet 4.5`；Hardware=`Not Disclosed`；Evaluator=`multi-label F1, retrieval/confusion oracle gaps, bootstrap CIs and annotation agreement`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** shortlisting降低 prompt 与 miss，却引入 retriever latency和约 9% shortlist miss；30-agent elbow 不是通用阈值。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17519v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-TOOL-CALLING` owner 为 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)。Review notes 前命题级锚点为 `Tool Discovery 与选择`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [AoiZora: Topology-Aware Auto-Parallel Optimization for Inference of Diffusion Transformers](https://arxiv.org/html/2606.17566v1)

**2606.17566 — AoiZora: Topology-Aware Auto-Parallel Optimization for Inference of Diffusion Transformers**

**问题与机制变化。** 分布式 DiT compiler planner 需先在 pre-compilation IR 高召回剪枝，再用 compiled HLO 与物理互连拓扑排序 sharding/placement；logical mesh 不是最终性能身份。

**State / data / control owner。** `INFER-TENSORRT-LLM` 是唯一知识 owner；`Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17566v1 §4 AoiZora, especially §§4.1–4.5; §5 implementation`；Evaluation=`arXiv:2606.17566v1 §6.1–6.6 methodology, latency, fidelity, ablation and planning cost`；Counterevidence=`arXiv:2606.17566v1 TPU v5e sub-slice, rectangular-topology and Wan 2.1 scope in §§2,6`。Workload=`Wan 2.1 one-step video-DiT denoising at 480p and 720p with 21, 41 and 81 frames`；Model=`Wan 2.1`；Hardware=`TPU v5e-4, v5e-8 and v5e-16 sub-slices`；Evaluator=`end-to-end denoising latency, search fidelity, ablations and planner cost`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 编译候选减少能省 planning cost，却可能漏掉好计划；1.42x 是指定 TPU/DiT denoising step，不是普遍加速。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17566v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前正文 `分布式 DiT Plan 必须经过编译后拓扑复排` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Cordon: Semantic Transactions for Tool-Using LLM Agents](https://arxiv.org/html/2606.17573v1)

**2606.17573 — Cordon: Semantic Transactions for Tool-Using LLM Agents**

**问题与机制变化。** 多步 tool execution 需要 task-scoped semantic transaction：shadow state、effect outbox、result lineage、delegated authority 与 recovery log 在一次 validate 后统一 commit/abort。

**State / data / control owner。** `AGENT-WORKFLOW` 是唯一知识 owner；`Books/part-07-agent/78-tool-calling.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17573v1 §3 Semantic Transaction Model; §4 Runtime Architecture; §5 Implementation`；Evaluation=`arXiv:2606.17573v1 §6.1–6.4 security, performance and benchmark correctness`；Counterevidence=`arXiv:2606.17573v1 §6.5 Limitations and Future Work`。Workload=`45 risk workflows from nine boundary categories by five risk families; five deterministic rollback trajectories; tau-bench and Terminal-Bench`；Model=`DeepSeek-V4-Pro`；Hardware=`Not Disclosed`；Evaluator=`pre-commit interception, rollback latency, task time/tokens and benign correctness`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 延迟外部 effect 提高 rollback/audit，却引入 approval latency、补偿语义与事务管理 TCB；45 个风险 workflow 不是完备安全证明。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17573v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Durable Execution 与 Replay`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning](https://arxiv.org/html/2606.17591v1)

**2606.17591 — Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning**

**问题与机制变化。** Verbal RL 的持久状态应分 rules、episode evidence 与 compositional skills，并支持置信更新、冲突处理、停用和重新激活，而非单调追加经验摘要。

**State / data / control owner。** `AGENT-MEMORY` 是唯一知识 owner；`Books/part-07-agent/81-workflow.md; Books/part-07-agent/82-multi-agent.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17591v1 §2.2 requirements; §3.1 three-layer architecture; §3.2 curation loop`；Evaluation=`arXiv:2606.17591v1 §4 financial-forecasting validation`；Counterevidence=`arXiv:2606.17591v1 §5 Limitations and non-stationary financial-case boundary`。Workload=`AAPL, AMZN, FB, GOOGL and MSFT; 2013-2016 learning period and 2017 test period`；Model=`Qwen3-VL-235B; Claude Sonnet 4.6 proposer, critic and curator`；Hardware=`Not Disclosed`；Evaluator=`accuracy and risk-adjusted return under zero-shot, partial and full curation loops`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 治理能减 stale transfer 却增加 evidence ledger、curator误判与上下文成本；金融案例不证明跨域收益。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17591v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `从原始轨迹到派生策略：Memory 的演进不是无限追加`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/html/2606.17730v1)

**2606.17730 — ActWorld: From Explorable to Interactive World Model via Action-Aware Memory**

**问题与机制变化。** 交互式 world model 的 memory 必须把 action-conditioned transition、event frame 与 object identity 跨 rollout 保存；只缓存视觉帧不足以复现可干预因果状态。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 是唯一知识 owner；`Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md; Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17730v1 §3 ActWorld action-aware hierarchical/persistent memory`；Evaluation=`arXiv:2606.17730v1 §4–§5 interactive world-model experiments and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17730v1 has no dedicated limitations section; exact-v1 counterevidence is localized at environment/action coverage and long-horizon generalization limitations`。Workload=`I-Bench: 300 prompts in 30 sequences of 10 prompts; each prompt has three action verbs and two or three camera primitives`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`interaction fidelity, long-horizon consistency and memory ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 持久 action memory减少状态遗忘却增加写入、检索与错误累积；有限环境不证明开放世界因果 fidelity。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17730v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前命题级锚点为 `Persistent world state`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [LUMEN: Coordinated Failure Recovery for Distributed LLM Serving](https://arxiv.org/html/2606.17787v1)

**2606.17787 — LUMEN: Coordinated Failure Recovery for Distributed LLM Serving**

**问题与机制变化。** Serving failure recovery 应联合决定 KV checkpoint placement、interrupted-request redistribution 与 model-reload期间的 draft capacity，而非各自局部优化。

**State / data / control owner。** `INFER-SCHEDULING` 是唯一知识 owner；`Books/part-05-inference-system/55-pd-disaggregation.md; Books/part-06-ai-infrastructure/63-gpu-scheduler.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17787v1 §4 LUMEN Design, §§4.2–4.4; §5 implementation`；Evaluation=`arXiv:2606.17787v1 §6.1–6.4 four/eight-worker prototype and up-to-64-worker simulation`；Counterevidence=`Not Disclosed — arXiv:2606.17787v1 has no dedicated limitations section; exact-v1 counterevidence is localized at worker-failure/full-reload assumptions and prototype/simulator scope`。Workload=`Splitwise-Conv traces under one to five simultaneous worker failures and request rates from 12 to 21 QPS`；Model=`Qwen3-32B and Qwen3-14B prototypes; Llama-3-70B simulation`；Hardware=`Not Disclosed`；Evaluator=`mean TTFT, TPOT and recovery time versus restart and fixed-checkpoint baselines`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 持续 checkpoint占 host memory/network，speculative recovery增加 draft state；结果不覆盖 correlated fabric failures或 production failover。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17787v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `MoE Failure Recovery 必须拥有 Request 与 Expert Generation`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor](https://arxiv.org/html/2606.17872v1)

**2606.17872 — AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor**

**问题与机制变化。** KV compression policy 要把 safety-critical refusal state 作为 offline anchor，并以 soft retention penalty约束 eviction；平均 attention/quality proxy 不能拥有安全状态。

**State / data / control owner。** `INFER-KV-CACHE` 是唯一知识 owner；`Books/part-05-inference-system/43-prefill.md; Books/part-05-inference-system/48-speculative-decoding.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17872v1 §3 AnchorKV refusal-anchor construction and soft-penalty compression`；Evaluation=`arXiv:2606.17872v1 §4–§5 safety/utility/cache evaluations and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17872v1 has no dedicated limitations section; exact-v1 counterevidence is localized at anchor/task/model/compression-ratio scope and refusal-proxy boundary`。Workload=`AdvBench harmful-behaviors split: 312 train, 104 validation and 104 test prompts; LongBench utility evaluation`；Model=`Llama-3.1-8B-Instruct target; Mistral-NeMo-Instruct-2407 attacker; DeepSeek-V3 paraphraser`；Hardware=`Not Disclosed`；Evaluator=`refusal/safety rate, task utility, memory reduction and ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 保留安全 anchor 会牺牲压缩率与普通 utility，anchor 失配还会给虚假安全感；不替代 end-to-end safety gate。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17872v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `压缩后的答案正确不等于证据仍被保留`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [How Inference Compute Shapes Frontier LLM Evaluation](https://arxiv.org/html/2606.17930v1)

**2606.17930 — How Inference Compute Shapes Frontier LLM Evaluation**

**问题与机制变化。** Frontier capability 必须报告为 inference-compute curve，并冻结 serial/parallel allocation、submission次数、feedback、compaction 与 matched budget；单点分数不能比较 generations。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17930v1 §2.1–2.5 models, scaling techniques, feedback, benchmarks and budgets`；Evaluation=`arXiv:2606.17930v1 §3.1–3.3 seven-benchmark scaling curves; Appendix A protocols`；Counterevidence=`arXiv:2606.17930v1 §4.4 Limitations; judge-noise and plateau interpretation in Appendix A.5`。Workload=`Seven benchmarks spanning software engineering, mathematics, medicine and cybersecurity; five trajectories per task`；Model=`Up to 12 frontier language models; six-model fully crossed main suite`；Hardware=`Not Disclosed`；Evaluator=`cumulative score versus tokens, serial/parallel allocation, plateau/reach/reliability analyses`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 大预算提高 elicitation也放大成本与 benchmark-specific scaffolding；tested plateau 不是模型能力上限。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17930v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `生成迭代次数不能代替实际计算预算`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving](https://arxiv.org/html/2606.17949v1)

**2606.17949 — RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving**

**问题与机制变化。** 异构 serving gateway 应联合选择 model 与具体 replica，把质量/成本约束和 queue/load state 放入同一 routing decision；先选模型再盲目 LB 会丢失耦合。

**State / data / control owner。** `PLATFORM-GATEWAY` 是唯一知识 owner；`Books/part-05-inference-system/53-kserve-llm.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17949v1 §3 RouteBalance formulation; §4 fused routing/load-balancing mechanism`；Evaluation=`arXiv:2606.17949v1 §5 evaluation on heterogeneous serving pool`；Counterevidence=`Not Disclosed — arXiv:2606.17949v1 has no dedicated limitations section; exact-v1 counterevidence is localized at model-quality estimates, arrival distribution and cluster-size limitations`。Workload=`3,534 prompts per evaluation cell over three budget-tightness mixes and request rates including 8, 12, 16 and 24`；Model=`Not Disclosed`；Hardware=`28 GPUs in a 13-instance serving pool`；Evaluator=`quality/cost constraints, load balance, latency and throughput comparisons`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 联合控制增加全局 state 与估计误差；28-GPU/13-instance结果不证明跨 provider 或 workload 优越。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17949v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-GATEWAY` owner 为 [books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md)。Review notes 前命题级锚点为 `Gateway、EPP 与 Engine Scheduler`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents](https://arxiv.org/html/2606.18037v1)

**2606.18037 — ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents**

**问题与机制变化。** MCP factuality verifier 必须把 source block identity、claim-to-source relation 与 final answer 分开评分；高 block F1 不能证明 provenance relation正确。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18037v1 §3 ProvenanceGuard source-aware verification pipeline`；Evaluation=`arXiv:2606.18037v1 §4–§5 MCP factuality experiments and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18037v1 has no dedicated limitations section; exact-v1 counterevidence is localized at source-ID stability, domain/tool and verifier-model limitations`。Workload=`281 medical MCP-agent traces; 266-trace claim subset with 2,325 labels; 40-trace held-out split with 361 claims`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`block retrieval F1, source-relation accuracy and answer factuality`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更细 provenance验证增加 calls 与 latency，source relation judge仍会漂移；不替代 authoritative source access。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18037v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前命题级锚点为 `视觉证据也必须有可追踪的 Claim–Evidence 生命周期`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization](https://arxiv.org/html/2606.18121v1)

**2606.18121 — On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization**

**问题与机制变化。** 多 Agent reliability 需把 proposer abstention、verifier abstention 与 message loss 作为不可互换的 factor-graph channels，并审计 certificate-stopping set 而非只扩 agent 数。

**State / data / control owner。** `AGENT-MULTI-AGENT` 是唯一知识 owner；`Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/66-evaluation-system.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18121v1 §IV role-typed Boolean-verifier model; §§V–X density evolution, stopping sets and optimization`；Evaluation=`arXiv:2606.18121v1 §XI calibration; §XII numerical validation; §XIII applications`；Counterevidence=`arXiv:2606.18121v1 §XIV-A limitations: correct surviving certificates, erasure-only and weak-dependence assumptions`。Workload=`Monte Carlo and deterministic-graph validation plus theorem/code/debate application mappings`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`density-evolution predictions, stopping sets and cost-constrained architecture optimization`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 理论可定位 topology瓶颈却依赖 sound verifier和局部树状假设；不覆盖 confidently-wrong/correlated failure。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18121v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前正文 `Coordination Failure` 已形成 owner-level 机制链；本项已实际 Integrate。

### [All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code](https://arxiv.org/html/2606.18168v1)

**2606.18168 — All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code**

**问题与机制变化。** Agent-authored tests 的 verifier strength 不能用“创建 test 文件”代理；release gate 应解析 assertion/oracle signal、执行路径与 failure discriminativeness。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18168v1 §3 oracle-signal taxonomy and test-code analysis method`；Evaluation=`arXiv:2606.18168v1 §4 analysis of roughly 86,000 patches/tests`；Counterevidence=`Not Disclosed — arXiv:2606.18168v1 has no dedicated limitations section; exact-v1 counterevidence is localized at repository/language/benchmark and static-analysis limitations`。Workload=`Approximately 86,000 agent-authored coding patches and associated test artifacts`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`presence and strength of explicit oracle signals, test execution and patch outcome`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更强 oracle审计增加解析与 mutation成本，仍可能漏掉语义空洞 assertion；统计比例不是所有 coding agents 的常数。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18168v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Harness Optimization 的 Test Boundary 必须对优化器不可见`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners](https://arxiv.org/html/2606.18198v1)

**2606.18198 — Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners**

**问题与机制变化。** Skill scanner 必须把 docs/code/resources/visual layers 与 execution simulation联结，因视觉隐藏指令可绕过纯文本/静态扫描后影响运行行为。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18198v1 §3 multimodal hidden-instruction threat model; §4 ExecScan pipeline`；Evaluation=`arXiv:2606.18198v1 §5–§6 attack/defense evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18198v1 has no dedicated limitations section; exact-v1 counterevidence is localized at skill formats, visual encodings, model/scanner and simulation-fidelity limits`。Workload=`multimodal agent skills containing document, code, resource and visual hidden instructions`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`attack success, scanner recall/precision and execution-grounded ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** execution-grounded扫描成本高且仍有模拟落差；受测 hidden channels 不证明未知编码被覆盖。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18198v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Skill Poisoning 的真值是 Side Effect，而不是是否被调用`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Looped World Models](https://arxiv.org/html/2606.18208v1)

**2606.18208 — Looped World Models**

**问题与机制变化。** Looped world model 以共享 recurrent block、spectral stability、adaptive early exit 与 deferred latent decoding形成 iterative-depth 分支；Ch25 已保存该 exact family 与机制边界。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 是唯一知识 owner；`Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md; Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18208v1 §3.1–3.5 looped dynamics, variable-depth training, early exit and deferred decoding`；Evaluation=`arXiv:2606.18208v1 §4.1–4.3 ScienceWorld, AlfWorld and deferred-decoding analysis`；Counterevidence=`arXiv:2606.18208v1 no dedicated limitations section; task-scale, parameter-efficiency and real-time claims bounded by §§4–6`。Workload=`ScienceWorld and ALFWorld world-model prediction and control`；Model=`LoopWM variants and exact-v1 baselines`；Hardware=`Not Disclosed`；Evaluator=`task performance, prediction quality, parameter efficiency and depth/deferral ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 已有 Ch25 已覆盖 recurrent transition、state tiering与受限 workload；100x 参数效率不等于 wall-clock、开放世界或物理 fidelity。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18208v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前命题级锚点为 `Persistent world state`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/html/2606.18247v1)

**2606.18247 — Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement**

**问题与机制变化。** Visual verifier 可在 inference 时对 policy proposal 评分/重采样，并把 verified rollouts作为下一轮 policy data；verifier只拥有 proposal/evidence，不拥有物理安全。

**State / data / control owner。** `MULTIMODAL-EMBODIED-VLA` 是唯一知识 owner；`Books/part-03-multimodal-world-models/25-multimodal-world-models.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18247v1 §3 visual-verifier training and inference-time steering; §4 autonomous improvement loop`；Evaluation=`arXiv:2606.18247v1 §5 robot-policy evaluations and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18247v1 has no dedicated limitations section; exact-v1 counterevidence is localized at verifier calibration, task/robot/camera and sim-to-real limitations`。Workload=`robot manipulation trajectories with visual verification, steering and self-training`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`task success under steering and policy improvement from verified rollouts`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 多 proposal与视觉 judge增加 actuation latency且会自强化 verifier偏差；有限任务不证明真实机器人安全。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18247v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-EMBODIED-VLA` owner 为 [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Review notes 前正文 `Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限` 已形成 owner-level 机制链；本项已实际 Integrate。

<!-- full-raw-recovered-evidence:start -->

### [Towards Distributed Inference of LLMs on a P2P Network](https://arxiv.org/html/2606.17059v1)

**问题、机制与 owner。** 去中心化 prefix-cache routing 以本地 radix tree 和周期性 anti-entropy 维护 peer cache 估计；stale metadata 只损失命中率、不破坏输出正确性，因此 weak consistency 可以成为路由正确性边界。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 System Design；§3 Safety Conditions and Failure Handling；§4–5 Experimental Setup/Results`。收益只在低通信延迟、prefix 分布偏斜的模拟 MMLU workload 中成立；affinity hotspot、高 RTT、peer failure 与估计过期会降低收益，不能外推生产 tail SLO。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 在 Review notes 前已写入 weak-consistency cache metadata、目标节点 identity 验证、anti-entropy 与普通负载均衡 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [LineageMark: Multi-user White-box Watermarking for Contribution Tracing in Model Derivation Chains](https://arxiv.org/html/2606.17123v1)

**问题、机制与 owner。** 模型派生链中的贡献追踪需要把 multi-user watermark carrier、插入顺序、检测阈值和派生 lineage 绑定到模型版本；watermark 是 provenance sensor，不是所有权或完整 lineage 的替代品。 唯一知识 owner 为 `PLATFORM-MODEL-REGISTRY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§III Problem/Threat Model；§IV LineageMark Design；§V Evaluation`。仅覆盖 white-box fine-tuning derivation 与作者攻击/模型设置；剪枝、量化、merge、共谋和未知变换可能破坏检测，误检也不能裁定法律归属。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/59-model-registry.md](../../../../books/part-06-ai-infrastructure/59-model-registry.md) 在 Review notes 前已写入 watermark provenance sensor、registry authority、变换/共谋 failure 与显式 lineage fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Statistical Foundations of LLM-based A/B Testing: A Surrogacy Framework for Human Causal Inference](https://arxiv.org/html/2606.17165v1)

**问题、机制与 owner。** 用 LLM 输出替代人类 outcome 做 A/B 推断时，必须把 surrogacy、treatment comparability、overlap 与 falsification test 写进 causal contract；模型评分相关性不等于人类 treatment effect 可识别。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Setup；§3 Surrogacy Framework；§4 Stochasticity`。作者识别结论依赖 surrogacy/comparability 假设和可观测 overlap；39% effect recovery 只属于所测数据，不能把单次 LLM 代理分数当作人类因果真值。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已写入 surrogate observation、experiment owner、识别假设与真人样本/随机实验 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Rethinking Groups in Critic-Free RLVR](https://arxiv.org/html/2606.17250v1)

**问题、机制与 owner。** critic-free RLVR 中 group 的关键作用之一是避免把所有失败 token 一起当作负证据；negative-token filtering 允许 single-rollout update，但会失去 group 内校准与探索覆盖。 唯一知识 owner 为 `TRAIN-GRPO`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2.1–2.4 grouping/negative-token analysis；§3 Methodology`。只在作者 RLVR 任务与模型上验证；single rollout 降低同步成本，却放大 verifier error、采样方差和错误正例，不能普遍替代 group sampling。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前的 `Verifiable Reward 不等于每个样本都可学习` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [OTRO: Oblivious Tokenization Path with Square-Root ORAM](https://arxiv.org/html/2606.17358v1)

**问题、机制与 owner。** CPU/GPU TEE 保护模型执行时，tokenizer 的词表访问路径仍可泄露 prompt；OTRO 用 square-root ORAM、只读表副本与 epoch rotation 隐藏访问序列，并把 KV/计算 overlap 纳入 TTFT 路径。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§III Leakage/Threat Model；§IV Reconstruction；§V–VI OTRO Design/Evaluation`。安全性依赖 TEE/ORAM threat model、访问模式实现与随机性更新；额外带宽、stash/epoch 管理和 tokenizer-specific layout 会增加 TTFT，未覆盖所有 tokenizer 与 side channel。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前已写入 tokenizer access-path threat、oblivious access、token identity owner 与普通 tokenizer/可信边界 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Dissecting model behavior through agent trajectories](https://arxiv.org/html/2606.17454v1)

**问题、机制与 owner。** 轨迹分解显示 Agent 行为由模型与 harness 共同形成；tool boundary、parser 和 feedback path 的失真会制造 intent–execution gap，因此 model/harness revision 与 component receipt 必须共同进入评估身份。 唯一知识 owner 为 `AGENT-PLATFORM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 SSA Architecture；§3 Refinements；§4–5 trajectory metric/evaluation`。作者 harness 与任务不能代表所有 Agent；轨迹差异是诊断证据，不等同模型内在能力或生产成功率。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 在 Review notes 前的 `Agent harness 必须把 model intent、实际 tool payload、environment result 与回送 context 做成双向可观测接口` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Online LLM Selection via Constrained Bandits with Time-Varying Demand](https://arxiv.org/html/2606.17489v1)

**问题、机制与 owner。** 在线模型选择在需求变化和 packing/covering 约束下应把 model pool、成本、质量估计与剩余资源作为同一 constrained-bandit state，而不是每次请求独立贪心。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§III System Model；§IV Formulation；§V Algorithm`。regret/constraint bounds依赖需求与反馈假设；partial feedback、模型版本漂移、冷启动和 tail latency 未被一般性解决，固定路由在流量稳定时仍更可审计。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 在 Review notes 前的 `多轮 Routing 是带剩余预算的序列决策` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [MagicSim: A Unified Infrastructure for Executable Embodied Interaction](https://arxiv.org/html/2606.17511v1)

**问题、机制与 owner。** 可执行 embodied interaction 应以 episode/MDP transition 为单位，由 runtime 持有 simulator、robot、planner、seed 与 record state；批处理只是共享 execution contract，不能把各 environment 状态混成 frame 流。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§1.2–1.4 Design；§3 Parallel Episode Runtime/MDP Boundary`。确定性与吞吐来自作者 simulator/runtime，不证明 sim-to-real 或硬实时控制；状态池增加 reset 泄漏、隔离和故障恢复成本。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 在 Review notes 前的 `Batched Environment 需要持久且可寻址的状态池` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack](https://arxiv.org/html/2606.17574v1)

**问题、机制与 owner。** Physical AI 评估把 task、resource、result 抽象和 episode driver 统一，令 framework、simulator、model 与 hardware outcome 可用同一 run identity 关联；统一接口不能抹平各层 truth owner。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.1–3.4 System Design；§4 Evaluation`。跨框架 alignment 只覆盖所测 physical-AI stack；adapter 语义、真实机器人故障和生产 tail 未闭合。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Cross-layer Evaluation 不允许下游成功掩盖上游故障` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [TivTok: Broadcasting Time-Invariant Tokens for Scalable Video Tokenization](https://arxiv.org/html/2606.17590v1)

**问题、机制与 owner。** 视频 tokenizer 可把 time-invariant scene content 与 time-varying motion 分成不同 token owner，并通过 attention-scope factorization 和 invariant-token broadcasting 避免重复编码；复用必须保留时间与场景 identity。 唯一知识 owner 为 `MULTIMODAL-REPRESENTATION`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3 Method；§4 Experiments；Appendix ablations`。压缩率与质量只绑定作者视频数据、codec/tokenizer 与模型；镜头切换、遮挡和快速运动会使 invariant 判断过期，广播错误会跨帧传播。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 在 Review notes 前已写入 TIV/TV scope、tokenizer/decoder ownership、过期传播 failure 与 dense-token fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [The Benchmark Illusion: Pruned LLMs Can Pass Multiple Choice but Fail to Answer](https://arxiv.org/html/2606.17609v1)

**问题、机制与 owner。** 剪枝后的模型可能保留 multiple-choice recognition 却失去 open-generation access；release gate 必须在同一知识 slice 上配对 recognition、free generation、answerability 与形式变换，区分知识存在和生成可达性。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Diagnostic Framework；§3 Demotion, Not Erasure`。作者结论来自所测 pruning/model/QA 和 multilingual stress test；恢复 prompt 或选项提示不证明部署生成能力已恢复，也不能外推所有压缩。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已写入 paired recognition/free-generation、evaluator/release authority、额外评测成本与开放生成 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering](https://arxiv.org/html/2606.17799v1)

**问题、机制与 owner。** coding-agent benchmark 若只冻结题目和单一 reference solution，会把需求不完备、harness/环境差异与模型执行混成总分；评估身份必须保存 task、harness、environment、tool budget 与 artifact verifier。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`position paper；problem analysis and proposed alignment principles`。该文是 position paper，不提供统一 benchmark 或生产因果验证；其论点只能支持 measurement contract 边界。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Evaluation Identity 必须包含 Harness 与 Environment` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Beyond Native Success: Auditing Deployment-Interface Exposure of CLIP Backdoors](https://arxiv.org/html/2606.17815v1)

**问题、机制与 owner。** CLIP backdoor 的风险要沿实际 deployment interface 审计：component readout、trigger、target label、reference set 与 downstream wrapper 共同决定可利用 exposure，而非只看 native benchmark success。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`Method/interface audit；deployment-facing evaluations`。结果绑定 CLIP、触发器与所测接口；暴露率不是真实攻击发生率，component sensor 不能替代 end-to-end policy/effect gate。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前的 `Embedding 也是可执行数据供应链的一部分` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Small Initialization Matters for Large Language Models](https://arxiv.org/html/2606.17945v1)

**问题、机制与 owner。** 初始化尺度会改变早期表示、梯度和最终 basin；训练 identity 必须绑定 parameterization、initialization、optimizer state、schedule 与 data order，不能把同一 loss 轨迹解释成同一 learned function。 唯一知识 owner 为 `TRAIN-PRETRAINING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Result；§3 Discussion`。理论和实验只覆盖论文设定；更小初始化不是跨架构通用最优，过小会削弱信号并增加 warmup/precision 风险。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-04-training-system/28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md) 在 Review notes 前的 `Optimizer 不是与参数化无关的旋钮` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs](https://arxiv.org/html/2606.17952v1)

**问题、机制与 owner。** SoftMoE 将离散 top-k 改为可微的 expert allocation，并学习 active-expert budget；router 仍拥有选择语义，runtime 必须把可变 expert 数转成 capacity/placement/communication 计划。 唯一知识 owner 为 `MODEL-MOE`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3–4 differentiable routing；§5 Experiments`。训练可微不等于部署成本可控；可变 active set 会扩大 All-to-All、容量和 kernel shape 波动，作者结果不证明普遍优于硬 top-k。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-02-model/21-moe.md](../../../../books/part-02-model/21-moe.md) 在 Review notes 前的 `从固定 Top-k 到受总预算约束的 Variable-k` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [VoidPadding: Separate Padding from Semantic Termination in Masked Diffusion Language Models](https://arxiv.org/html/2606.17999v1)

**问题、机制与 owner。** masked diffusion LM 中同一 EOS 同时承担语义终止与 padding 会让长度状态混淆；独立 VOID token 把空白 canvas 与终止语义分离，使 length/admission、denoising 与 final commit 拥有不同状态。 唯一知识 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Masked Diffusion；§3 EOS Overflow；§4 VoidPadding/Experiments`。额外 token 与 adaptive canvas 增加 tokenizer、training objective 和 sampler compatibility；作者任务不证明所有 dLLM 或 runtime 都改善，AR termination 仍是独立分支。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 在 Review notes 前已写入 VOID/EOS 状态分离、length/denoising/commit owners、runtime compatibility 代价与自回归 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Recursive Scaling in Masked Diffusion Models](https://arxiv.org/html/2606.18022v1)

**问题、机制与 owner。** masked diffusion 的 recursive depth 通过共享参数反复执行，把 parameter count 与 test-time execution depth 分离；每轮 state 必须保持可修订，停止规则不能由迭代次数冒充正确性。 唯一知识 owner 为 `MODEL-TRANSFORMER-LAYER`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`Method/recursive scaling analysis；Experiments`。收益绑定 masked-diffusion 模型与任务；更多 recursion 可能积累错误和延迟，不能等同新参数容量或普遍 scaling law。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-02-model/17-transformer-layer.md](../../../../books/part-02-model/17-transformer-layer.md) 在 Review notes 前的 `Parameter Depth 与 Execution Depth 可以分离` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Latency Prediction for LLM Inference on NPU Systems](https://arxiv.org/html/2606.18042v1)

**问题、机制与 owner。** 闭源 NPU microarchitecture、compiler rewrite 与 bucket nonlinearity使纯算子相加失效；LENS 用少量端到端测量校准分桶 latency surrogate，但 estimator 只拥有候选预测，不拥有部署 SLO。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2–3 NPU challenges；§4 LENS；Evaluation`。两次测量/分桶的准确性绑定目标 NPU、compiler、model shape 与软件版本；版本漂移、queueing 和 host overhead 要求重校准及真实 replay。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `从直接 Grid Search 到 Floor-first Diagnosis` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping](https://arxiv.org/html/2606.18120v1)

**问题、机制与 owner。** Handlebars triple-brace 等模板路径可让不可信文本越过预期 escaping，并把数据放进结构性 role；delimiter/HTML escaping 只处理字符族，不能替代 typed role、source label 与 effect-time authorization。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`attack construction and template analysis；evaluations across prompt layouts`。攻击依赖具体模板、parser 与模型；修复一个 delimiter family 不证明其他 rendering path 安全，结构化 prompt 也不能独自授予或撤销权限。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前的 `Instruction Hierarchy 必须携带 Authenticated Provenance` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers](https://arxiv.org/html/2606.18206v1)

**问题、机制与 owner。** looped Transformer 以共享 block 增加 execution depth，并用 pre-norm/residual scaling维持 fixed-point 稳定，再按收敛状态自适应停止；执行深度不等于参数深度。 唯一知识 owner 为 `MODEL-TRANSFORMER-LAYER`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.1 pre-norm；§3.2 residual scaling；experiments`。收敛阈值可能误停或拖延，稳定 fixed point 不保证任务正确；论文设置不证明所有 architecture/length 可迁移。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-02-model/17-transformer-layer.md](../../../../books/part-02-model/17-transformer-layer.md) 在 Review notes 前的 `Parameter Depth 与 Execution Depth 可以分离` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification](https://arxiv.org/html/2606.18249v1)

**问题、机制与 owner。** 理解与生成若分别使用不兼容 visual token，shared backbone 仍无法共享状态。UniAR 以 shared context–visual tokenizer、parallel bitwise prediction 与独立 decoder 建立共同 token identity，同时保留生成 artifact 边界。 唯一知识 owner 为 `MULTIMODAL-REPRESENTATION`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.1 Unified Visual Tokenizing；§3.2 AR Modeling；§4 Experiments`。统一 token 降低接口分裂却引入 rate/distortion、bitwise independence 与 decoder 版本耦合；作者结果不证明单一表示对所有理解/生成任务最优。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 在 Review notes 前已写入统一 token identity、tokenizer/decoder owner、目标竞争代价与双 tokenizer bridge fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/html/2606.18250v1)

**问题、机制与 owner。** 未来 3D state 要把 ego-motion 与 world-motion 分离，才能让相机位姿成为 action proxy、场景变化成为 environment transition；视觉重建质量不能替代可控 dynamics。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.2 Future 3D Prediction；§3.3 Ego/World Motion；§4 Evaluation`。结果绑定作者 driving/video 数据与几何假设；ego-motion proxy 不是完整 action，遮挡和动态对象仍会制造不可观测状态。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 在 Review notes 前的 `从 RGB Rollout 到 Projective 4D Predictive State` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

<!-- full-raw-recovered-evidence:end -->


### [GLM-5.2](https://www.zhipuai.cn/zh/research/161)

**问题、旧路径与约束变化。** Query-aware sparse attention 常让每个稀疏层独立维护 selector/indexer。它保留 layer-specific routing fidelity，但长上下文下 selector 计算和索引状态会随层数重复增长。GLM-5.2 的官方技术页披露 `IndexShare`：每四个稀疏注意力层复用同一 indexer，把逐层独立选择改成有边界的跨层 selector-state reuse。

**Mechanism 与 owner。** Indexer 输出只拥有候选 token selection，attention layer 仍拥有最终读写和残差更新；复用范围、刷新周期、model revision 与 fallback 必须显式绑定。唯一知识 owner 是 `MODEL-LONG-CONTEXT`，不是模型版本本身。

**Evidence 与边界。** 官方页给出精确时间 `2026/06/16 16:00`，并披露四层共享一个 indexer、1M context 与 per-token FLOPs 等作者主张。页面没有完整公开 hardware、precision、sequence composition、batch、concurrency、SLO、训练细节和实现 artifact，因此只能证明 creator-primary 所述设计，不能把 `2.9x` FLOPs 或 MTP acceptance `up to 20%` 外推为跨模型生产结论。

**Trade-off、failure 与 fallback。** 共享 indexer 减少 selector FLOPs 与状态，却假设相邻稀疏层的检索分布可复用；新增 stale selection、layer-specific recall loss、head imbalance、版本迁移和局部故障放大。分布漂移或召回审计失败时，应缩小 reuse scope 或回退逐层 indexer。

**Books Decision。** [MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md) 在 Review notes 前的 `Sparse Attention 的两个 ownership 轴` 已明确 selector refresh owner、跨层复用范围、stale-selection/head-imbalance 代价与回退边界；本项为 `No Change — Existing Coverage`。

### Books / semantic audit

原 arXiv fresh-context 审计以 level-2 `Review notes` 为正文边界。50 个 arXiv 候选中，15 项已在正文形成完整机制链，35 项有不依赖 source trace 的命题级覆盖，writeback queue=0。当前来源再认证新增的 GLM-5.2 为第 51 项，Books 判断是 Existing Coverage，未触发写回；不同 reviewer 已重新打开官方页与 Ch22 正文完成复核。

## 5. 缺口与下一步

无

## 6. 复核

复核者：独立 fresh-context reviewer（非作者侧）

结论：通过

原复核重新检查 534=50 Candidate+484 audited Close、50 项 Books disposition（15 Integrate/35 Existing）、13 项本轮新增 binding 中属于本日的 8 项，以及两套 validator 与限定 diff。8/8 marker 均位于首个顶层 Review notes 前，正文均覆盖旧约束→机制→owner→trade-off/failure→fallback。不同 reviewer 又核对了 Z.ai 官方页的 `2026/06/16 16:00`、每四个稀疏层共享一个 indexer 的公开机制与证据限制，并对读 Ch22 `Sparse Attention 的两个 ownership 轴`；确认该增量属于 Existing Coverage，Books writeback queue 仍为 0。
