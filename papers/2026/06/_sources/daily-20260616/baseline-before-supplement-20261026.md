# Daily Research — 2026-06-16

**规范：** V3
**窗口：** 2026-06-15T09:00:00+08:00 ～ 2026-06-16T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-11T14:55:01+08:00

## 1. 结论

canonical raw inventory 共 1186 个身份；独立复核确认 title + 完整 abstract 筛选后的 100 个候选仍满足本项目贡献门槛，1086 项在分母前关闭。候选中 23 项已在 Review notes 前形成完整正文机制链，77 项由既有命题级正文承载；相较复核前，将 29 项从 Integrate 降级为 Existing Coverage。ordinary pending、材料请求与 Books body writeback queue 均为 0；5 项新增正文已通过独立 post-write 终审，本日报 Complete。

当前合同评分已由非作者重新校准，不以已经深读或已经写入 Books 倒推高分。100 项现在分布为 `6 分 × 77、8 分 × 23`；既有 exact-v1 深审仍可复用，最低审阅等级按新分数表述。逐项旧分、新分和三维依据见 [current score recalibration](../_sources/daily-20260616/CURRENT_SCORE_RECALIBRATION_20260914.json)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ANTHROPIC | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-GOOGLE-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-META-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-QWEN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-DEEPSEEK | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MOONSHOT | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ZAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MINIMAX | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260616/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ARXIV | official first-public owner、canonical raw inventory 与全量题摘账本；逐项语义复核 1186 个 raw identities，冻结 100 个候选、关闭 1086 项 | 已检查 | 无 |

分母前关闭项均保留 identity、完整摘要 hash 与 family-specific reason；两轮 fresh-context 反向审计共恢复 29 个 false negatives。准入不使用关键词、章节可映射性或候选数量；本窗无 withdrawn retained family。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Unified KV Pooling to Accelerate Long-Context LLM Serving](https://arxiv.org/html/2606.14779v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-GPU-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-GPU-MEMORY，[owner](../../../../books/part-05-inference-system/54-gpu-memory.md)；命题锚点：Long-context State 可以形成多级 Byte-addressable Tier |
| [The Vision Encoder as a Privacy Boundary: Visual-Token Side Channels in Encoder-Free Vision-Language Models](https://arxiv.org/html/2606.14783v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Privacy Boundary 必须覆盖全部 Observable Channels |
| [XFlow: An Executable Protocol Programming System for Reliable Multi-Agent Workflows](https://arxiv.org/html/2606.14790v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：State Machine 是基本模型 |
| [Knowledge-Based Zero-Replay Debugging of Multi-Agent LLM Traces](https://arxiv.org/html/2606.14805v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-TRACE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-TRACE，[owner](../../../../books/part-06-ai-infrastructure/69-trace.md)；正文锚点：预测器只能分配 Replay Budget，不能确认因果 |
| [PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions](https://arxiv.org/html/2606.14832v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 恢复准入：AGENT-TOOL-CALLING 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Computer-use Action 与完成判断应优先读取程序真实状态 |
| [Semantic Integrity Failures in Document-to-LLM Supply Chains](https://arxiv.org/html/2606.15020v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：Document Ingestion 必须比较 Rendered 与 Extracted View |
| [NEURON-Fabric: CXL-Side Low-Bit Gradient Aggregation for Distributed Training](https://arxiv.org/html/2606.15045v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DISTRIBUTED-TRAINING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：通信压缩必须把编解码写进 Critical Path |
| [Solyx AI Grid: Hardware-Telemetry-Aware Routing Across Geographically Distributed GPU Clusters](https://arxiv.org/html/2606.15050v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-GATEWAY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-GATEWAY，[owner](../../../../books/part-06-ai-infrastructure/62-gateway.md)；命题锚点：Gateway、EPP 与 Engine Scheduler |
| [Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models](https://arxiv.org/html/2606.15070v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-DECODE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-DECODE，[owner](../../../../books/part-05-inference-system/44-decode.md)；正文锚点：Request-local Stop Sensor 不能取得最终停止权 |
| [PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression](https://arxiv.org/html/2606.15157v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：从统一跨层共享到 Token × Depth 自适应残差 |
| [Coordinated Scheduling for MoE LLM Serving](https://arxiv.org/html/2606.15177v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：Request、Engine 与 Expert 决策需要共享一份调度状态 |
| [CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation](https://arxiv.org/html/2606.15179v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：分布式证据汇聚应按 Sufficiency 收敛，而不是等待所有节点 |
| [Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems](https://arxiv.org/html/2606.15242v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Skill Poisoning 的真值是 Side Effect，而不是是否被调用 |
| [Acting While Understanding: Asynchronous Semantic-Action Decoupling for Real-Time Vision-Language-Action Models](https://arxiv.org/html/2606.15285v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-EMBODIED-VLA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：Fast-Slow VLA：把慢语义状态与快控制拆成有界陈旧的异步闭环 |
| [Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades](https://arxiv.org/html/2606.15308v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：跨模态 Availability 先攻击决策状态，而不一定生成恶意内容 |
| [Adaptive Resource Management and Quality Control for Streaming Video Generation](https://arxiv.org/html/2606.15319v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：迭代生成与流式会话需要显式 Progress State |
| [CausalDrive: Real-time Causal World Models for Autonomous Driving](https://arxiv.org/html/2606.15341v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：Goal 属于 Planner Cost，不能成为 Transition 的答案通道 |
| [CoAgent: Concurrency Control for Multi-Agent Systems](https://arxiv.org/html/2606.15376v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；命题锚点：声明式协议约束 Transition，而不是相信参与者会协调 |
| [Rethinking the Role of Efficient Attention in Hybrid Architectures](https://arxiv.org/html/2606.15378v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 MODEL-LONG-CONTEXT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；正文锚点：Hybrid Attention 还需要按层分配精确访问预算 |
| [Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment](https://arxiv.org/html/2606.15441v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Pre-execution Guardrail：检测 Off-task 不能等到副作用发生后 |
| [A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference](https://arxiv.org/html/2606.15453v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-GPU-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-GPU-MEMORY，[owner](../../../../books/part-05-inference-system/54-gpu-memory.md)；命题锚点：MoE Expert Staging 可以消费时序与跨层激活相关性 |
| [Understanding Diversity Collapse in RLVR via the Lens of Overtraining](https://arxiv.org/html/2606.15455v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 TRAIN-GRPO 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；正文锚点：Exploration 必须与 Verified Progress 对齐 |
| [Who Drifted: the System or the Judge? Anytime-Valid Attribution in LLM Evaluation Pipelines](https://arxiv.org/html/2606.15474v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Attribution 是 Versioned Evaluation Contract |
| [One Goal, Many Commands: Characterizing Denylist Fragility in AI Agents](https://arxiv.org/html/2606.15549v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Canonical Action 与 Effect-time Authorization |
| [Service-Induced Congestion in Memory-Constrained LLM Serving](https://arxiv.org/html/2606.15555v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：不确定输出长度下的 Future-state Reservation |
| [Pixels to Proofs: Probabilistically-Safe Latent World Model Control via Parallel Conformal Robust MPC](https://arxiv.org/html/2606.15594v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：从平均预测误差到分层的 Rollout Admission |
| [FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion](https://arxiv.org/html/2606.15609v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：跨会话分解会绕过 Prompt-local Guard |
| [MosaicQuant: Inlier-Outlier Disaggregation for Unified 4-Bit LLM Quantization](https://arxiv.org/html/2606.15652v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：Distribution-conditioned Quantization：共享权重不等于共享 Scale |
| [ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training](https://arxiv.org/html/2606.15682v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 恢复准入：INFER-TENSORRT-LLM 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点：W/A/KV 联合量化必须保护关键 Reasoning Commitment |
| [Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift](https://arxiv.org/html/2606.15734v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 TRAIN-LORA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-LORA，[owner](../../../../books/part-04-training-system/30-lora.md)；正文已落实：从持续改写共享权重到可检索的临时参数更新 |
| [Approaching Shannon Bound with Lossless LLM Weight Compression](https://arxiv.org/html/2606.15789v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-GPU-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-GPU-MEMORY，[owner](../../../../books/part-05-inference-system/54-gpu-memory.md)；命题锚点：Lossless Weight Compression 需要与 GEMM Tiling 联合调度 |
| [Mean-Field Parallel Decoding for Discrete Diffusion Language Models](https://arxiv.org/html/2606.15805v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-GENERATIVE-PARADIGMS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：Early convergence 与 high confidence 不是同一个 Commit 证据 |
| [TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI](https://arxiv.org/html/2606.15822v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-GATEWAY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-GATEWAY，[owner](../../../../books/part-06-ai-infrastructure/62-gateway.md)；命题锚点：Gateway、EPP 与 Engine Scheduler |
| [Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations](https://arxiv.org/html/2606.15903v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：先分开 Construction 与 Retrieval Failure，再选择 Memory 结构 |
| [PromptShift-CRC: Drift-Aware Conformal Risk Control for Foundation Models Under Prompt and Domain Shift](https://arxiv.org/html/2606.15964v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Continual Update 需要同步推进 Calibration State |
| [Do Activation Monitors Survive Model Updates? Benchmarking, Predicting, and Repairing Activation-Monitor Staleness](https://arxiv.org/html/2606.15980v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-MONITORING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点：Model Revision 必须触发 Activation Monitor 复验 |
| [Fearless Concurrency on the GPU](https://arxiv.org/html/2606.15991v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：异步工作不必永久绑定固定 Physical Core |
| [Auditing Reward Hackability in Code RL Training Environments](https://arxiv.org/html/2606.16062v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Reward Hacking 监测要分开 Reference 与可部署观测面 |
| [Your "Pro" LLM Subscription May Actually Be "Free": Exposing Fingerprint Spoofing Risks in LLM Inference Services](https://arxiv.org/html/2606.16100v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Referential Security：身份声明必须可持续验证 |
| [Edge-Inference Governors Need Memory-Clock State](https://arxiv.org/html/2606.16106v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：Power Envelope 也要按推理阶段分配 |
| [SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing](https://arxiv.org/html/2606.16135v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：流式输入把 Cache 变成可续租的 Session State |
| [Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing](https://arxiv.org/html/2606.16264v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-PD-DISAGGREGATION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-PD-DISAGGREGATION，[owner](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；正文锚点：从静态 Pool Ratio 到耦合的 SLO Control State |
| [Dynamic Malicious Skills in Agentic AI](https://arxiv.org/html/2606.16287v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Skill Poisoning 的真值是 Side Effect，而不是是否被调用 |
| [QK-Normed MLA: QK normalization without full key caching](https://arxiv.org/html/2606.16310v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 MODEL-LONG-CONTEXT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；命题锚点：条件化机制分支与共存边界 |
| [Filtered ANN as a Phase Transition: When Selectivity-Estimation Error Causes Plan Regret](https://arxiv.org/html/2606.16341v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 恢复准入：AGENT-RAG 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；命题锚点：从固定 Retriever 演进到可提交的 Logical / Physical Plan |
| [Communication-Efficient Verifiable Attention for LLM Inference](https://arxiv.org/html/2606.16352v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Proof of Equation Satisfaction 不等于 Proof of Expended Work |
| [The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs](https://arxiv.org/html/2606.16358v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-GATEWAY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-GATEWAY，[owner](../../../../books/part-06-ai-infrastructure/62-gateway.md)；正文锚点：TEE Router 只收缩 Plaintext Authority，不提供端到端正确性 |
| [Mixtures of Subspaces for Bandwidth Efficient Context Parallel Training](https://arxiv.org/html/2606.16384v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DISTRIBUTED-TRAINING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：Context Parallel 的 buffer 也有容量上限 |
| [BadWorld: Adversarial Attacks on World Models](https://arxiv.org/html/2606.16519v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：VLA 威胁模型必须延伸到物理反馈 |
| [Multimodal Evaluator Preference Collapse: Cross-Modal Coupling in Self-Evolving Agents](https://arxiv.org/html/2606.16682v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：组件分数不能在相关错误下直接合成系统可靠性 |
| [PATCH: Action-Chunk-Conditioned Latent Patch Innovation Monitoring for Robot Manipulation](https://arxiv.org/html/2606.16690v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 恢复准入：MULTIMODAL-EMBODIED-VLA 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：闭环检测必须读取动作产生时的控制状态 |
| [GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents](https://arxiv.org/html/2606.16813v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 AGENT-TOOL-CALLING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Disclosure Minimization 不能替代 Authorization |
| [How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation](https://arxiv.org/html/2606.16821v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Search Query 本身也是 Public Egress Action |
| [CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents](https://arxiv.org/html/2606.16824v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：从统一保留到 workload-aware eviction |
| [Tangram: Hiding GPU Heterogeneity for Efficient LLM Parallelization](https://arxiv.org/html/2606.16907v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DISTRIBUTED-TRAINING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；命题锚点：从手写 Plan 到可校准的并行规划器 |
| [Greed Is Learned: Visible Incentives as Reward-Hacking Triggers](https://arxiv.org/html/2606.16914v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：从 Model Capability Gate 到 Deployment-context Residual Risk Loop |
| [Agent trajectories as programs: fingerprinting and programming coding-agent behavior](https://arxiv.org/html/2606.16988v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：从 Agent Trace 编译 Workflow 需要可归因的数据依赖 |
| [KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing](https://arxiv.org/html/2606.17034v1) | 2026-06-16T08:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点：KV Steering 是可回滚的派生状态变换 |

| [Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/html/2606.15007v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MODEL-MOE 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-MOE，[owner](../../../../books/part-02-model/21-moe.md)；命题锚点：Total / Active Parameters 只是约束坐标，不是架构答案 |
| [How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position](https://arxiv.org/html/2606.15032v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：World Model 评价分离 transition fidelity、decision utility 与真实闭环 outcome |
| [A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability](https://arxiv.org/html/2606.15551v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：WORLDVIEW-WHY-MODELS-LEARN 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN，[owner](../../../../books/part-01-worldview/04-why-models-learn.md)；正文锚点：Edge of Stability 是离散动力学分岔，不是“学习率越大越好” |
| [Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking](https://arxiv.org/html/2606.15673v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Agent Evaluation 保存 semantic state transition 与 first-loss attribution |
| [Google's Training Supercomputers from TPU v2 to Ironwood: Architectural Stability, Scale, Resilience, Power Efficiency, and Sustainability Across Five Generations](https://arxiv.org/pdf/2606.15870v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-DISTRIBUTED-TRAINING 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；命题锚点：先定义 collective semantics，再选择可替换的数据流与实现 |
| [From Tokens to Regions: CUDA-Sensitive Instruction Tuning for GPU Kernel Generation](https://arxiv.org/html/2606.16231v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-SFT 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-SFT，[owner](../../../../books/part-04-training-system/29-sft.md)；命题锚点：SFT 的 supervision allocation 必须服从可执行 artifact 与能力回归 |
| [daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization](https://arxiv.org/html/2606.16497v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-GRPO 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：Skill 更新必须经过执行回执、独立 outcome 对照与版本提交 |
| [Incentives and Evidence in Learned Service Orchestration](https://arxiv.org/html/2606.16555v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Matched Counterfactual 必须保持任务界面 |
| [Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning](https://arxiv.org/html/2606.16576v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Look Again Before You Abstain:Budgeted Conformal Evidence Acquisition for Reliable Vision-Language Model](https://arxiv.org/html/2606.16667v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy |
| [A First-Principles Derivation of LLM Policy Optimization: From Expected Reward to GRPO and Its Structural Extensions](https://arxiv.org/html/2606.16733v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-GRPO 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：从 REINFORCE 到 PPO，再到 GRPO |
| [SoK: Security and Privacy of Foundation-Model-Powered Robots](https://arxiv.org/html/2606.16788v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-SECURITY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：从 Model Capability Gate 到 Deployment-context Residual Risk Loop |
| [Follow the Latent Roadmap: Navigating Revocable Decoding for Diffusion LLMs with Anchor Tokens](https://arxiv.org/html/2606.16847v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-GENERATIVE-PARADIGMS 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；命题锚点：Editable tokens 在 Commit 前保持可撤销 |
| [Human-on-the-Bridge: Scalable Evaluation for AI Agents](https://arxiv.org/html/2606.16871v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Human–Agent Team 必须成为独立 Evaluation Object |
| [DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/html/2606.16993v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-WORLD-MODELS 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：Persistent World State 需要流式更新与观测校正 |
| [Exploding and vanishing gradients in deep neural networks: the effect of residual connections](https://arxiv.org/html/2606.17013v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：WORLDVIEW-WHY-MODELS-LEARN 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：WORLDVIEW-WHY-MODELS-LEARN，[owner](../../../../books/part-01-worldview/04-why-models-learn.md)；命题锚点：Residual connection 使深层 Jacobian product 保留 identity path |
| [ExpRL: Exploratory RL for LLM Mid-Training](https://arxiv.org/html/2606.17024v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-GRPO 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：RL mid-training 的训练奖励不等于部署期 environment authority |
| [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/html/2606.17030v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-WORLD-MODELS 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：language-conditioned video forecast 不拥有 physical action authority |

| [SWARM-LLM: Collaborative Inference for Edge-based Small Language Models](https://arxiv.org/html/2606.14711v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-GATEWAY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-GATEWAY，[owner](../../../../books/part-06-ai-infrastructure/62-gateway.md)；命题锚点：Gateway 先按 privacy、安全与 data residency 建立 eligible set，再优化成本与延迟 |
| [Context Compression Is Not One Thing: Readable Symbolic Re-expression vs. Coherent Summary at Matched Budget](https://arxiv.org/html/2606.14875v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-CONTEXT 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[owner](../../../../books/part-07-agent/75-context.md)；命题锚点：Context Compression 以未来决策充分性、provenance 与可回源性为合同 |
| [Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations](https://arxiv.org/html/2606.15008v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-SECURITY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Multi-Agent 聚合不能把最弱成员升级为系统 authority |
| [Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/html/2606.15017v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Agent 组件收益必须采用 token/compute-matched counterfactual |
| [Resilient Consensus in Agentic AI](https://arxiv.org/html/2606.15024v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-MULTI-AGENT 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；命题锚点：Multi-Agent 共识需要外部协议约束 |
| [OSGuard: A Benchmark for Safety in Computer-Use Agents](https://arxiv.org/html/2606.15034v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Computer-use evaluation 同时保存局部 action checks 与端到端 invariant |
| [AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents](https://arxiv.org/html/2606.15057v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-SECURITY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：IPI 防御必须在 adaptive attack 与 effect-time authorization 下验收 |
| [Is Code Better Than Language for Algorithmic Reasoning](https://arxiv.org/html/2606.15589v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-TOOL-CALLING 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Tool output 是 observation，外部 executor 才拥有执行结果 |
| [PathRouter: Aligning Rewards with Retrieval Quality in Agentic Graph Retrieval-Augmented Generation](https://arxiv.org/html/2606.16409v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-GRPO 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：RAG 评估分离 retrieval/path evidence 与最终 answer outcome |
| [Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/html/2606.16420v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-PLATFORM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLATFORM，[owner](../../../../books/part-07-agent/84-agent-platform.md)；命题锚点：Skill 更新必须经过执行回执与版本提交 |
| [Privacy from Symmetry: Orthogonally Equivariant Transformers for LLM Inference](https://arxiv.org/html/2606.16461v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-SECURITY 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：Split Inference 的表示保护可以写进模型对称性 |
| [BRICKS-WM: Building Reusability via Interface Composition Kinetics for Structured World Models](https://arxiv.org/html/2606.16489v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-WORLD-MODELS 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：World Model 可按动力学责任拆成可复用模块 |
| [Tail-Shape Estimation in LLM Evaluation Is Fragile: A Protocol for Diagnosing False Positives](https://arxiv.org/html/2606.16511v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Tail Metric 也必须先通过可识别性与稳定性 Gate |
| [SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents](https://arxiv.org/html/2606.16591v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-TOOL-CALLING 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Tool discovery 是 query-conditioned proposal，不能替代逐工具授权 |
| [VeriGraph: Towards Verifiable Data-Analytic Agents](https://arxiv.org/html/2606.16603v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-WORKFLOW 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Workflow 的 canonical DAG 与 evidence graph 由平台拥有 |
| [ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control](https://arxiv.org/html/2606.16605v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：PLATFORM-EVALUATION-SYSTEM 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：World Model evaluation 分离 dynamics、policy、value 与闭环 outcome |
| [User as Code: Executable Memory for Personalized Agents](https://arxiv.org/html/2606.16707v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-MEMORY 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：Append-only evidence 与可执行 derived memory state 分离 |
| [Taming Curvature: Architecture Warm-Up for Stable Transformer Training](https://arxiv.org/html/2606.16768v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-PRETRAINING 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；正文锚点：Architecture Warm-up 只能作为受测曲率压力的 Actuator |
| [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled Policy Optimization](https://arxiv.org/html/2606.16771v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-GRPO 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：多 Reward 聚合不能掩盖 Channel Collapse 与梯度冲突 |
| [Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models](https://arxiv.org/html/2606.16825v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MODEL-MOE 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-MOE，[owner](../../../../books/part-02-model/21-moe.md)；正文锚点：MoE 可以共享 Expert Parameters，同时保留逐层 Routing State |
| [Directory-Aware Query and Maintenance in Vector Databases](https://arxiv.org/html/2606.16903v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-RAG 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；命题锚点：Retrieval Index 必须保留原生 Hierarchy |
| [LESS Is More: Mutual-Stability Sampling for Diffusion Language Models](https://arxiv.org/html/2606.16908v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：MULTIMODAL-GENERATIVE-PARADIGMS 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；命题锚点：Diffusion token 的稳定性只支持 proposal，runtime 独占 commit/rollback |
| [TokenPilot: Cache-Efficient Context Management for LLM Agents](https://arxiv.org/html/2606.17016v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：AGENT-CONTEXT 的长期机制边界；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-CONTEXT，[owner](../../../../books/part-07-agent/75-context.md)；正文锚点：canonical prefix 与 segment lifecycle |
| [DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents](https://arxiv.org/html/2606.17029v1) | 2026-06-16T00:00:00+08:00 ～ 2026-06-16T09:00:00+08:00 | fresh audit 从全量 raw 恢复：TRAIN-GRPO 的长期机制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：Evidence-derived Rubric 是版本化 Reward State |

## 4. 证据与知识整合

### [Unified KV Pooling to Accelerate Long-Context LLM Serving](https://arxiv.org/html/2606.14779v1)

**2606.14779 — Unified KV Pooling to Accelerate Long-Context LLM Serving**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：KV offload 不应串行穿过单 host/SSD；应把多 DRAM/SSD 汇成 bandwidth-weighted pool，并以 user-space SPDK bypass filesystem。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.14779v1 §V Evaluation` 支持 `Long-context KV offload and TTFT/I/O sweeps`；模型 `Llama-3.1-8B, GPT-OSS-20B, Qwen3-30B-A3B`；硬件 `Multi-host-memory and SSD testbed disclosed in §V-A`；精度 `Model/KV precision disclosed in §V-A`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.14779v1 §IV Design; KV orchestrator and passthrough`；counterevidence locator：`arXiv:2606.14779v1 §VI Discussion`。

**Trade-off / failure / coexistence / evolution。** pooling 降低 blocked I/O，却引入 allocator metadata、failure recovery 与 SPDK 运维成本；短 context/HBM-resident path 仍更简单。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.14779v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `INFER-GPU-MEMORY` owner 为 [books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md)。Review notes 前命题级锚点为 `Long-context State 可以形成多级 Byte-addressable Tier`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [The Vision Encoder as a Privacy Boundary: Visual-Token Side Channels in Encoder-Free Vision-Language Models](https://arxiv.org/html/2606.14783v1)

**2606.14783 — The Vision Encoder as a Privacy Boundary: Visual-Token Side Channels in Encoder-Free Vision-Language Models**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Encoder-free VLM 的 visual tokens 与 layer-0 KV 可能成为 output filter 之前的可逆 privacy side channel；architecture 与 cache access 必须进入 threat model。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.14783v1 §3 setup; §§4–7 experiments` 支持 `Held-out access-code inversion, clutter/degradation/transfer and defense ablations`；模型 `Gemma4/Fuyu vs Qwen3-VL/InternVL/LLaVA controls`；硬件 `Not Disclosed`；精度 `Token/value quantization tested as ineffective value-level defense`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.14783v1 §2 Threat Model; §§4–8 mechanism/defense`；counterevidence locator：`arXiv:2606.14783v1 §8 Defense Boundary; §9 deployment implications`。

**Trade-off / failure / coexistence / evolution。** 降低 spatial sampling 可减泄漏但可能损失 OCR/细节能力；value noise/quantization 不构成通用缓解。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.14783v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Privacy Boundary 必须覆盖全部 Observable Channels`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [XFlow: An Executable Protocol Programming System for Reliable Multi-Agent Workflows](https://arxiv.org/html/2606.14790v1)

**2606.14790 — XFlow: An Executable Protocol Programming System for Reliable Multi-Agent Workflows**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：prompt与harness之间的承诺应以可执行protocol编译为lifecycle-governed typed symbols；actor输出须经validation/commit后才进入shared state。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.14790v1 §§3–5 XPF language, compiler and runtime symbols`；evaluation locator 为 `arXiv:2606.14790v1 §6 constrained-interaction/long-context/software-engineering evaluation`；counterevidence locator 为 `arXiv:2606.14790v1 §7 limitations and protocol/task/model scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** typed protocol提高可审计性但增加authoring/迁移与状态机僵化；informal semantic work仍在actor内，不获形式正确性。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.14790v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `State Machine 是基本模型`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Knowledge-Based Zero-Replay Debugging of Multi-Agent LLM Traces](https://arxiv.org/html/2606.14805v1)

**2606.14805 — Knowledge-Based Zero-Replay Debugging of Multi-Agent LLM Traces**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：长Multi-Agent trace应编译成event knowledge graph，并用校准predictor分配稀缺counterfactual replay budget；预测只排序证据，不替代replay oracle。

**State / data / control owner。** `PLATFORM-TRACE` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.14805v1 §§3–5 trace graph and zero-replay predictor`；evaluation locator 为 `arXiv:2606.14805v1 §6 37 trace-family held-out evaluation`；counterevidence locator 为 `arXiv:2606.14805v1 §7 limitations and deterministic-oracle/fixed-budget scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** learned ranking会随trace schema和failure分布漂移；zero replay的高recall不证明causal effect，关键事件仍需oracle replay。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.14805v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-TRACE` owner 为 [books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md)。Review notes 前正文 `预测器只能分配 Replay Budget，不能确认因果` 已形成 owner-level 机制链；本项已实际 Integrate。

### [PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions](https://arxiv.org/html/2606.14832v1)

**2606.14832 — PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions**

**问题、机制与准入。** We introduce PhoneHarness, a mixed-action benchmark and execution harness for studying phone-use agents on verifiable mobile workflows. Fresh-context 终审确认该变化触及 `AGENT-TOOL-CALLING` 的长期系统边界，而不是仅有章节映射或局部 benchmark，因此撤销旧 de-admit。

**State / data / control owner。** `AGENT-TOOL-CALLING` 是 canonical owner；跨层状态必须保留 identity、version、admission 与 fallback，论文或项目名本身不取得新 owner。

**Evidence / non-proof。** Method：`https://arxiv.org/html/2606.14832v1 — § exact-v1 anchor: PhoneHarness`；Evaluation：`https://arxiv.org/html/2606.14832v1 — § exact-v1 evaluation anchor: annotated evaluation split`；limitations/counterevidence：`https://arxiv.org/html/2606.14832v1 — § exact-v1 limitation/counterevidence anchor: mixed phone workflows`；artifact：`Not Disclosed — no later artifact used`。这些 exact-v1 位置只支持其披露 workload，不证明未披露硬件、精度、并发、SLO 或跨 workload 普遍优越性。

**Trade-off / coexistence。** 新机制提高了目标场景中的可控性或效率，但增加额外状态、估计误差或 runtime policy；原条件简单、隔离要求更强或校准证据不足时，旧路径仍是回退。

**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.14832v1` 的 exact-v1 method/evaluation/limitations。

**V3 Books 复验。** 当前 `AGENT-TOOL-CALLING` owner 为 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)。Review notes 前命题级锚点为 `Computer-use Action 与完成判断应优先读取程序真实状态`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Semantic Integrity Failures in Document-to-LLM Supply Chains](https://arxiv.org/html/2606.15020v1)

**2606.15020 — Semantic Integrity Failures in Document-to-LLM Supply Chains**

**问题与旧路径。** `Document-to-LLM applications typically read uploaded PDFs by first translating them into text through a hidden extraction layer that users cannot observe or audit.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Document ingestion 必须把 rendered view 与 extractor view作为两份可比较 evidence；PDF render/extract divergence要在进入 LLM context 前经 dual-view consistency与static screening gate。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 25 extraction gaps、16 PDF processing stacks、7 commercial LLM services；每个 service 至少暴露一种 gap。 Method locator：`https://arxiv.org/html/2606.15020v1 — § exact-v1 anchor: 25 extraction gaps`。Evaluation locator：`https://arxiv.org/html/2606.15020v1 — § exact-v1 evaluation anchor: 16 PDF processing stacks`。Benchmark identity：model=`Seven commercial LLM services evaluated as document-ingestion endpoints; base-model versions are Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Detection of 25 render/extract semantic gaps across 16 PDF-processing stacks and seven services`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** scanner规则只覆盖已知25类且可能误报；双视图一致也不证明文档真实或模型安全，动态/OCR路径仍需独立审计。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.15020v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前正文 `Document Ingestion 必须比较 Rendered 与 Extracted View` 已形成 owner-level 机制链；本项已实际 Integrate。

### [NEURON-Fabric: CXL-Side Low-Bit Gradient Aggregation for Distributed Training](https://arxiv.org/html/2606.15045v1)

**2606.15045 — NEURON-Fabric: CXL-Side Low-Bit Gradient Aggregation for Distributed Training**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：把低比特梯度聚合下沉到 CXL memory controller，并以 workload/layer/phase admission 保留 FP32 recovery path。

**State / data / control owner。** `TRAIN-DISTRIBUTED-TRAINING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15045v1 §§5–10 timing, correctness, training evidence and hardware plausibility` 支持 `CIFAR-10/100 ResNet-18, SST-2 DistilBERT; gem5/controller timing and FPGA plausibility`；模型 `ResNet-18; DistilBERT`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15045v1 §3 Architecture; §4 Methodology`；counterevidence locator：`arXiv:2606.15045v1 §7.2 harder-workload boundary; §11 Limitations`。

**Trade-off / failure / coexistence / evolution。** 低比特减少流量但 CIFAR-100 的全路径失败表明 approximation 不能无条件进入敏感层；FP32 All-Reduce 仍是 correctness fallback。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15045v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `TRAIN-DISTRIBUTED-TRAINING` owner 为 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)。Review notes 前正文 `通信压缩必须把编解码写进 Critical Path` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Solyx AI Grid: Hardware-Telemetry-Aware Routing Across Geographically Distributed GPU Clusters](https://arxiv.org/html/2606.15050v1)

**2606.15050 — Solyx AI Grid: Hardware-Telemetry-Aware Routing Across Geographically Distributed GPU Clusters**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：跨站点 LLM 路由必须联合 GPU DCGM、vLLM queue/runtime 与 WAN RTT/jitter，并把 replica lifecycle 与 capability constraint 放进 placement state。

**State / data / control owner。** `PLATFORM-GATEWAY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15050v1 §5 setup; §6 results` 支持 `three US datacenters; 15 GPUs; eight workload classes; 216-cell SLO matrix`；模型 `vLLM-served LLM workloads`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15050v1 §4 System Architecture; §§4.2–4.4 scorer and lifecycle`；counterevidence locator：`arXiv:2606.15050v1 §2.3 failure modes; §7 discussion/limitations`。

**Trade-off / failure / coexistence / evolution。** 更多信号可提前 drain，但权重、telemetry staleness 与跨站网络波动会扩大控制环；单站点/同构集群仍适合简单最少队列。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15050v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `PLATFORM-GATEWAY` owner 为 [books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md)。Review notes 前命题级锚点为 `Gateway、EPP 与 Engine Scheduler`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models](https://arxiv.org/html/2606.15070v1)

**2606.15070 — Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：用 attention-state 判断推理是否收敛，再在 exit、logit injection 与 jump intervention 之间切换，把 overthinking 从固定 token budget 演进为 request-local control。

**State / data / control owner。** `INFER-DECODE` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15070v1 §5 Experiments; Appendix D/E/F` 支持 `nine reasoning benchmarks across DeepSeek-R1-Distill and Qwen3 scales`；模型 `DeepSeek-R1-Distill; Qwen3`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15070v1 §3 motivations; §4 Methodology`；counterevidence locator：`arXiv:2606.15070v1 §5.5 discussion; Appendix H future work`。

**Trade-off / failure / coexistence / evolution。** 省 token 依赖 attention signal 的校准；误停会丢正确性、误判 trap 会增加扰动，固定 budget 与 verifier fallback 仍需共存。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15070v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `INFER-DECODE` owner 为 [books/part-05-inference-system/44-decode.md](../../../../books/part-05-inference-system/44-decode.md)。Review notes 前正文 `Request-local Stop Sensor 不能取得最终停止权` 已形成 owner-level 机制链；本项已实际 Integrate。

### [PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression](https://arxiv.org/html/2606.15157v1)

**2606.15157 — PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：KV compression 应把 eviction method 与 budget allocation 都提升为 layer-wise heterogeneous decision，而不是全层单策略同预算。

**State / data / control owner。** `INFER-KV-CACHE` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15157v1 §4 Evaluation` 支持 `long-context tasks under fixed and varied KV budgets`；模型 `multiple transformer LLMs`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15157v1 §3 Methodology`；counterevidence locator：`arXiv:2606.15157v1 §4.3–4.6 robustness and case-study boundary; §5`。

**Trade-off / failure / coexistence / evolution。** heterogeneity 提升固定预算质量却需要离线 calibration 与更多 profile metadata；短 context 或模型漂移时统一策略更稳。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15157v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `从统一跨层共享到 Token × Depth 自适应残差`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Coordinated Scheduling for MoE LLM Serving](https://arxiv.org/html/2606.15177v1)

**2606.15177 — Coordinated Scheduling for MoE LLM Serving**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：MoE serving 要协调 DP-engine request pressure 与 expert/communication pressure，并让 expert placement 消费 source-aware traffic profile。

**State / data / control owner。** `INFER-SCHEDULING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15177v1 §7 Evaluation` 支持 `MoE serving throughput, latency, ablation and overhead sweeps`；模型 `MoE LLM serving stack`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15177v1 §3 overall design; §§4–5 scheduling and placement`；counterevidence locator：`arXiv:2606.15177v1 §2.3 current-system limits; §7.5 overhead`。

**Trade-off / failure / coexistence / evolution。** 联合控制减少两级 imbalance，却引入 trace、MINLP calibration 与 online placement 开销；低偏斜或小规模部署仍适合独立调度。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15177v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `Request、Engine 与 Expert 决策需要共享一份调度状态`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation](https://arxiv.org/html/2606.15179v1)

**2606.15179 — CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：document-isolated device-cloud RAG 应用 waiting debt 与 certificate-guided minimal supplement 异步聚合证据，而不是等待所有设备或一次性上传全文。

**State / data / control owner。** `AGENT-RAG` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15179v1 §V Experiments` 支持 `device-cloud RAG experiments with waiting/communication ablations`；模型 `distributed RAG configurations`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15179v1 §III problem; §IV Methodology`；counterevidence locator：`arXiv:2606.15179v1 §IV-E theorem assumptions; §VI`。

**Trade-off / failure / coexistence / evolution。** 稀疏补充降低等待和通信，但证书/估计失真会漏证据；需要全局一致性或关键文档时同步聚合仍合理。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15179v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前正文 `分布式证据汇聚应按 Sufficiency 收敛，而不是等待所有节点` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems](https://arxiv.org/html/2606.15242v1)

**2606.15242 — Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 安全单位应从孤立 artifact 扩到 activated composition path，显式跟踪 capability flow、trust transfer 与 authorization confusion 的 state change。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15242v1 §4 Experiments` 支持 `SCR-Bench across three mechanisms and multiple LLM backends`；模型 `multiple agent backends`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15242v1 §3 Method; Appendix B`；counterevidence locator：`arXiv:2606.15242v1 Appendix A Limitations`。

**Trade-off / failure / coexistence / evolution。** path-aware sandbox 暴露组合风险但无法穷尽动态图和长链；静态 artifact vetting 与 effect-time authorization 仍是必要层。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15242v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Skill Poisoning 的真值是 Side Effect，而不是是否被调用`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Acting While Understanding: Asynchronous Semantic-Action Decoupling for Real-Time Vision-Language-Action Models](https://arxiv.org/html/2606.15285v1)

**2606.15285 — Acting While Understanding: Asynchronous Semantic-Action Decoupling for Real-Time Vision-Language-Action Models**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：把低频 semantic module 与高频 action module 异步解耦，并让 action policy 条件化历史动作以容忍 stale semantics。

**State / data / control owner。** `MULTIMODAL-EMBODIED-VLA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15285v1 §4 Experiments; Appendix B/C` 支持 `LIBERO plus real-world robot deployments and stale-semantic ablations`；模型 `asynchronous VLA variants`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15285v1 §3 Method; Appendix A`；counterevidence locator：`arXiv:2606.15285v1 §5 Limitations and Discussion`。

**Trade-off / failure / coexistence / evolution。** 提高 control rate 但引入双时钟、stale-state 与恢复边界；强耦合在低频、可停顿环境仍更简单。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15285v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `MULTIMODAL-EMBODIED-VLA` owner 为 [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Review notes 前命题级锚点为 `Fast-Slow VLA：把慢语义状态与快控制拆成有界陈旧的异步闭环`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades](https://arxiv.org/html/2606.15308v1)

**2606.15308 — Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：confidence-based model cascade 是可攻击的资源控制面：输入可被优化为强制 deferral，使昂贵模型被持续调用。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15308v1 §4 Experiments; Appendix A` 支持 `multiple datasets, MLLM families, routing metrics and preprocessing defenses`；模型 `weak/strong multimodal LLM cascades`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15308v1 §3 Method and threat model`；counterevidence locator：`arXiv:2606.15308v1 §5 Conclusion and Limitations`。

**Trade-off / failure / coexistence / evolution。** robust routing/预算 gate 抵抗成本攻击却可能拒绝真实困难输入；accuracy-only deferral 在可信流量仍可保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15308v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `跨模态 Availability 先攻击决策状态，而不一定生成恶意内容`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Adaptive Resource Management and Quality Control for Streaming Video Generation](https://arxiv.org/html/2606.15319v1)

**2606.15319 — Adaptive Resource Management and Quality Control for Streaming Video Generation**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：streaming video generation 应把 playout slack 作为动态 SLO state，用于 preemption、re-homing、elastic sequence parallelism 与 per-chunk fidelity selection。

**State / data / control owner。** `INFER-SCHEDULING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15319v1 §7 Evaluation; Appendices B/D` 支持 `streaming-video workloads, end-to-end/ablation/sensitivity and controller-overhead tests`；模型 `streaming video diffusion serving`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15319v1 §3 overview; §§4–5 slack control`；counterevidence locator：`arXiv:2606.15319v1 §7.5 sensitivity; §9 future work`。

**Trade-off / failure / coexistence / evolution。** 回收 slack 提高利用率但转移 KV/state 有开销，低保真传播与 controller lag 会伤质量；静态 reservation 在稳定负载仍合理。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15319v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前正文 `迭代生成与流式会话需要显式 Progress State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [CausalDrive: Real-time Causal World Models for Autonomous Driving](https://arxiv.org/html/2606.15341v1)

**2606.15341 — CausalDrive: Real-time Causal World Models for Autonomous Driving**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：驾驶 world model 必须由当前 observation/action 生成 reactive future，不能偷用 oracle future layout；causal text controls 与 context-forced distillation服务闭环。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15341v1 §4 benchmark; §5 Experiments` 支持 `SocioDrive-Bench and downstream closed-loop applications`；模型 `causal autoregressive teacher and distilled renderer`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15341v1 §3 Methodology`；counterevidence locator：`arXiv:2606.15341v1 §5 reliability/controllability scope; §6`。

**Trade-off / failure / coexistence / evolution。** 实时反应性用 distillation 换 fidelity，文本控制和标注 pipeline 也可能制造偏差；显式 simulator 继续拥有安全验证。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15341v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前命题级锚点为 `Goal 属于 Planner Cost，不能成为 Transition 的答案通道`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [CoAgent: Concurrency Control for Multi-Agent Systems](https://arxiv.org/html/2606.15376v1)

**2606.15376 — CoAgent: Concurrency Control for Multi-Agent Systems**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：多 Agent 共享对象可用 Monotonic Trajectory Pre-Order：固定读序、speculative write、通知与可逆三阶段 tool call，在 quiescence 达到 serializable outcome。

**State / data / control owner。** `AGENT-MULTI-AGENT` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15376v1 §7 Evaluation` 支持 `multi-agent concurrency workloads and protocol/system comparisons`；模型 `CoAgent protocol/framework`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15376v1 §§4–6 insights, MTPO and framework`；counterevidence locator：`arXiv:2606.15376v1 §5.1 correctness assumptions; §6.3 undoability and three-phase toolcalls`。

**Trade-off / failure / coexistence / evolution。** 少锁并发提高吞吐但要求 undo/saga 与 constrained tools；不可逆副作用或缺少 inverse 时必须串行或人工 gate。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15376v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前命题级锚点为 `声明式协议约束 Transition，而不是相信参与者会协调`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Rethinking the Role of Efficient Attention in Hybrid Architectures](https://arxiv.org/html/2606.15378v1)

**2606.15378 — Rethinking the Role of Efficient Attention in Hybrid Architectures**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：hybrid architecture 中 efficient attention 主要塑造 optimization，而长程 retrieval 仍主要由 full-attention layers 承担；ratio 与 positional treatment 应按该分工设计。

**State / data / control owner。** `MODEL-LONG-CONTEXT` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15378v1 §4 settings and scaling; §5 probing` 支持 `scaling-law, probing and long-context evaluations across hybrid attention variants`；模型 `multiple hybrid attention backbones`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15378v1 §§3–6 scaling/mechanism/design`；counterevidence locator：`arXiv:2606.15378v1 §6 hybrid design ablations; §7 conclusion boundary`。

**Trade-off / failure / coexistence / evolution。** 减少 full attention 降成本却会压缩长程容量；large-window 或错误 NoPE 组合会产生 lazy layers，纯 full attention 仍是质量基线。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15378v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `MODEL-LONG-CONTEXT` owner 为 [books/part-02-model/22-long-context.md](../../../../books/part-02-model/22-long-context.md)。Review notes 前正文 `Hybrid Attention 还需要按层分配精确访问预算` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment](https://arxiv.org/html/2606.15441v1)

**2606.15441 — Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：IPI defense 应在每次 tool output 上做 task-alignment reasoning，并用自适应 red-team diversity reward 构造训练分布。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15441v1 §5 Experiments` 支持 `six adaptive black-box attacks across two target models`；模型 `RETA-trained agent defenders`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15441v1 §3 failures; §4 RETA`；counterevidence locator：`arXiv:2606.15441v1 §5.5 Failure Analysis; §6 Limitations`。

**Trade-off / failure / coexistence / evolution。** 训练防御改善安全-效用取舍但依赖 threat model、reasoning faithfulness 与持续 refresh；deterministic effect gate 仍不可替代。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15441v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Pre-execution Guardrail：检测 Off-task 不能等到副作用发生后`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference](https://arxiv.org/html/2606.15453v1)

**2606.15453 — A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：MoE expert staging 可利用跨层与相邻 token 的 activation correlation 预取，并保持原 router 决策不变。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15453v1 §5 Evaluation and Analysis` 支持 `language/code MoE workloads, prediction, latency, energy and hardware sensitivity`；模型 `Qwen/DeepSeek-class MoE models`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15453v1 §3 correlations; §4 ST-MoE design`；counterevidence locator：`arXiv:2606.15453v1 §5.6–5.7 ablation/sensitivity; §7`。

**Trade-off / failure / coexistence / evolution。** prefetch 隐藏加载却占带宽/容量，误预测会挤出需要 expert；动态 routing 漂移时 on-demand loading 仍是 fallback。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15453v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `INFER-GPU-MEMORY` owner 为 [books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md)。Review notes 前命题级锚点为 `MoE Expert Staging 可以消费时序与跨层激活相关性`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Understanding Diversity Collapse in RLVR via the Lens of Overtraining](https://arxiv.org/html/2606.15455v1)

**2606.15455 — Understanding Diversity Collapse in RLVR via the Lens of Overtraining**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：RLVR 的 diversity collapse 应按 problem saturation/overtraining 解释，并用 zero-success/boundary contribution gate 决定哪些题继续更新。

**State / data / control owner。** `TRAIN-GRPO` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15455v1 §5 Experiments; Appendices A–D` 支持 `multiple reasoning benchmarks with Pass@k, gating and early-stop analyses`；模型 `RLVR base models and GRPO/REINFORCE/BBG variants`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15455v1 §3 overtraining; §4 Methodology`；counterevidence locator：`arXiv:2606.15455v1 §6 Limitations and sampling-noise appendix`。

**Trade-off / failure / coexistence / evolution。** boundary gating 保护高-k 能力但估计受少量 rollout 噪声影响；只优化 Pass@1 或资源紧张时普通 on-policy 仍更简单。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15455v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `TRAIN-GRPO` owner 为 [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。Review notes 前正文 `Exploration 必须与 Verified Progress 对齐` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Who Drifted: the System or the Judge? Anytime-Valid Attribution in LLM Evaluation Pipelines](https://arxiv.org/html/2606.15474v1)

**2606.15474 — Who Drifted: the System or the Judge? Anytime-Valid Attribution in LLM Evaluation Pipelines**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：持续评测必须用固定人标 anchor 与第二条 anytime-valid e-process 区分 system drift 和 judge drift，并让 anchor race 快于主告警。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.15474v1 §5 Experiments` 支持 `two real judge changes across two domains and repeated streaming trials`；模型 `cheap monitor plus strong LLM judge`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.15474v1 §3 cost-aware monitoring; §4 anchor construction`；counterevidence locator：`arXiv:2606.15474v1 §6 Discussion and Limitations`。

**Trade-off / failure / coexistence / evolution。** anchor 减少误归因却增加强 judge/人标成本并会陈旧；系统与 judge 同时漂移时只能按声明规则保守归类。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15474v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Attribution 是 Versioned Evaluation Contract`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [One Goal, Many Commands: Characterizing Denylist Fragility in AI Agents](https://arxiv.org/html/2606.15549v1)

**2606.15549 — CmdNeedle: Measuring the Incompleteness of Command Denylists for AI Agents**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：terminal Agent command gate不能把开放命令空间压成load-bearing denylist；应以operation/effect为policy对象并用sandbox side-effect validator验证candidate bypass。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15549v1 §§IV–VI threat model, formalization and CmdNeedle pipeline`；evaluation locator 为 `arXiv:2606.15549v1 §VII Evaluation`；counterevidence locator 为 `arXiv:2606.15549v1 §IX Limitations and Future Work`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** command枚举会持续陈旧且ask-list受approval fatigue影响；1,709-denylist结果不证明任何单个gate必然可绕过。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15549v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Canonical Action 与 Effect-time Authorization`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Service-Induced Congestion in Memory-Constrained LLM Serving](https://arxiv.org/html/2606.15555v1)

**2606.15555 — Service-Induced Congestion in Memory-Constrained LLM Serving**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：continuous batching必须把decode期间KV持续增长视为service-induced congestion state，并在admission/eviction前控制同步limit cycle。

**State / data / control owner。** `INFER-SCHEDULING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15555v1 §§2–5 dynamical model and stability analysis`；evaluation locator 为 `arXiv:2606.15555v1 §§6–7 homogeneous/heterogeneous workload results`；counterevidence locator 为 `arXiv:2606.15555v1 §8 discussion and model-assumption boundaries`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 理论依赖离散时间与workload assumptions；异质长度可去同步但不是生产调度万能规则。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15555v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `不确定输出长度下的 Future-state Reservation`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Pixels to Proofs: Probabilistically-Safe Latent World Model Control via Parallel Conformal Robust MPC](https://arxiv.org/html/2606.15594v1)

**2606.15594 — Pixels to Proofs: Probabilistically-Safe Latent World Model Control via Parallel Conformal Robust MPC**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：latent world-model control需把conformal latent-error bound、constraint checker与robust MPC绑定，模型proposal不能直接取得physical commit authority。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15594v1 §§3–5 latent world model, conformal bounds and SLS MPC`；evaluation locator 为 `arXiv:2606.15594v1 §6 vision-control evaluation`；counterevidence locator 为 `arXiv:2606.15594v1 §7 limitations and finite-task/calibration scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 概率安全依赖exchangeability、latent Markov性与constraint coverage；有限视觉控制任务不证明开放环境安全。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15594v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前正文 `从平均预测误差到分层的 Rollout Admission` 已形成 owner-level 机制链；本项已实际 Integrate。

### [FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion](https://arxiv.org/html/2606.15609v1)

**2606.15609 — FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Agent access control必须跨turn组合memory fragments并在retrieval/fusion时重建cumulative intent，不能只检查最终query。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15609v1 §§3–4 FragFuse temporal-memory attack`；evaluation locator 为 `arXiv:2606.15609v1 §5 four-setting evaluation`；counterevidence locator 为 `arXiv:2606.15609v1 §6 limitations and black-box/access-control scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 跨turntaint会增加false positive和lineage成本；86.3% bypass是三种机制/四setting结果。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15609v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `跨会话分解会绕过 Prompt-local Guard`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [MosaicQuant: Inlier-Outlier Disaggregation for Unified 4-Bit LLM Quantization](https://arxiv.org/html/2606.15652v1)

**2606.15652 — MosaicQuant: Inlier-Outlier Disaggregation for Unified 4-Bit LLM Quantization**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：4-bit runtime可把dense base与sparse 4-bit residual同时压进single fused GEMM pipeline，避免mixed-precision conversion破坏实际speedup。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15652v1 §§3–4 MosaicQuant and ZipperEngine`；evaluation locator 为 `arXiv:2606.15652v1 §5 LLaMA3/Qwen3 evaluation`；counterevidence locator 为 `arXiv:2606.15652v1 §6 limitations and disclosed model/kernel/hardware scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** sparse residual增加metadata与kernel complexity；1.24x绑定作者shape/hardware，近FP16不等于所有task等价。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15652v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前命题级锚点为 `Distribution-conditioned Quantization：共享权重不等于共享 Scale`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training](https://arxiv.org/html/2606.15682v1)

**2606.15682 — ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training**

**问题、机制与准入。** We identify that FP4 failures concentrate on low-entropy tokens--precise symbolic commitments such as digits and operators--where quantization noise inflates sampling errors that cascade through reasoning traces. Fresh-context 终审确认该变化触及 `INFER-TENSORRT-LLM` 的长期系统边界，而不是仅有章节映射或局部 benchmark，因此撤销旧 de-admit。

**State / data / control owner。** `INFER-TENSORRT-LLM` 是 canonical owner；跨层状态必须保留 identity、version、admission 与 fallback，论文或项目名本身不取得新 owner。

**Evidence / non-proof。** Method：`arXiv:2606.15682v1 §3 Empirical Analysis; §4 Methods`；Evaluation：`arXiv:2606.15682v1 §5 Experiments; §5.3 Throughput`；limitations/counterevidence：`arXiv:2606.15682v1 §6 Discussions and Appendix D scope`；artifact：`Not Disclosed — no later artifact used`。这些 exact-v1 位置只支持其披露 workload，不证明未披露硬件、精度、并发、SLO 或跨 workload 普遍优越性。

**Trade-off / coexistence。** 新机制提高了目标场景中的可控性或效率，但增加额外状态、估计误差或 runtime policy；原条件简单、隔离要求更强或校准证据不足时，旧路径仍是回退。

**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15682v1` 的 exact-v1 method/evaluation/limitations。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前正文 `W/A/KV 联合量化必须保护关键 Reasoning Commitment` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift](https://arxiv.org/html/2606.15734v1)

**2606.15734 — Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：continual post-training可把document-specific gradient变成indexed retrievable artifact，在query时临时apply并在请求后rollback，避免shared-weight cumulative drift。

**State / data / control owner。** `TRAIN-LORA` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15734v1 §§3–4 Gradient Bank and bi-level meta-learning`；evaluation locator 为 `arXiv:2606.15734v1 §5 general/domain evaluation`；counterevidence locator 为 `arXiv:2606.15734v1 §6 limitations and temporary-adaptation/model/task scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** gradient bank storage、检索误配与request isolation增加成本；临时更新不证明无安全/并发副作用。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15734v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `TRAIN-LORA` owner 为 [books/part-04-training-system/30-lora.md](../../../../books/part-04-training-system/30-lora.md)。Review notes 前正文 `从持续改写共享权重到可检索的临时参数更新` 已形成旧路径、约束变化、state/control ownership、trade-off 与 fallback 的完整机制链；本项已实际 Integrate。

### [Approaching Shannon Bound with Lossless LLM Weight Compression](https://arxiv.org/html/2606.15789v1)

**2606.15789 — Approaching Shannon Bound with Lossless LLM Weight Compression**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：lossless weight compression要让tile-level ANS decode与GEMM tiling/weight residency联合调度，bit-exact减存储但新增decode bandwidth与kernel state。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15789v1 §§3–5 entropy study and tile decompression design`；evaluation locator 为 `arXiv:2606.15789v1 §6 SGLang/multi-GPU evaluation`；counterevidence locator 为 `arXiv:2606.15789v1 §7 limitations and model/format/hardware scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 高entropy tensor收益小，decode可能成瓶颈；batch/throughput结果绑定Qwen/Mixtral与作者GPU。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15789v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-GPU-MEMORY` owner 为 [books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md)。Review notes 前命题级锚点为 `Lossless Weight Compression 需要与 GEMM Tiling 联合调度`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Mean-Field Parallel Decoding for Discrete Diffusion Language Models](https://arxiv.org/html/2606.15805v1)

**2606.15805 — Mean-Field Parallel Decoding for Discrete Diffusion Language Models**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：discrete diffusion并行commit需用pairwise compatibility修正marginal confidence，避免独立高置信token组成冲突configuration。

**State / data / control owner。** `MULTIMODAL-GENERATIVE-PARADIGMS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15805v1 §§3–4 mean-field commit scoring and fixed-point update`；evaluation locator 为 `arXiv:2606.15805v1 §5 reasoning/code evaluation`；counterevidence locator 为 `arXiv:2606.15805v1 §6 limitations and training-free/model/task scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** pairwise近似增加计算且不能表示高阶依赖；质量/延迟frontier绑定受测dLLM。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15805v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-GENERATIVE-PARADIGMS` owner 为 [books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。Review notes 前正文 `Early convergence 与 high confidence 不是同一个 Commit 证据` 已形成 owner-level 机制链；本项已实际 Integrate。

### [TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI](https://arxiv.org/html/2606.15822v1)

**2606.15822 — TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：agentic routing中gateway不能同时拥有明文与不可验证转发authority；应以三方TLS、privacy-preserving query construction和verifiable billing分拆trust。

**State / data / control owner。** `PLATFORM-GATEWAY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15822v1 PDF §§4–6 handshake, query construction and billing protocols`；evaluation locator 为 `arXiv:2606.15822v1 PDF §7 prototype evaluation`；counterevidence locator 为 `arXiv:2606.15822v1 PDF §8 limitations and cryptographic/deployment assumptions`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 2PC/ZKP扩大TCB与latency；prototype不证明provider、traffic与side-channel的生产安全。


**Claim boundary。** 仅引用 `https://arxiv.org/pdf/2606.15822v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-GATEWAY` owner 为 [books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md)。Review notes 前命题级锚点为 `Gateway、EPP 与 Engine Scheduler`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations](https://arxiv.org/html/2606.15903v1)

**2606.15903 — Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Agent memory forgetting不仅由retriever/model决定，还由extraction、storage、retrieval与injection control-plane placement共同决定，memory topology必须版本化。

**State / data / control owner。** `AGENT-MEMORY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15903v1 §§3–4 thirteen-configuration architectural study`；evaluation locator 为 `arXiv:2606.15903v1 §5 forgetting/utility evaluation`；counterevidence locator 为 `arXiv:2606.15903v1 §6 limitations and model/task/configuration scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 额外control points增加latency与inconsistency；13种配置不穷尽生产memory system。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15903v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `先分开 Construction 与 Retrieval Failure，再选择 Memory 结构`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [PromptShift-CRC: Drift-Aware Conformal Risk Control for Foundation Models Under Prompt and Domain Shift](https://arxiv.org/html/2606.15964v1)

**2606.15964 — PromptShift-CRC: Drift-Aware Conformal Risk Control for Foundation Models Under Prompt and Domain Shift**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：prompt/domain shift下conformal risk control需显式检测drift、更新calibration window并在保证失效时abstain，而不能继承旧coverage。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15964v1 §§3–4 PromptShift-CRC method`；evaluation locator 为 `arXiv:2606.15964v1 §5 prompt/domain-shift evaluation`；counterevidence locator 为 `arXiv:2606.15964v1 §6 limitations and exchangeability/drift-detection scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 窗口更新以样本效率和lag换coverage；未知shift下不能把nominal guarantee当release proof。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15964v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Continual Update 需要同步推进 Calibration State`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Do Activation Monitors Survive Model Updates? Benchmarking, Predicting, and Repairing Activation-Monitor Staleness](https://arxiv.org/html/2606.15980v1)

**2606.15980 — Do Safety Monitors Stay Reliable After an Update? Benchmarking and Predicting Activation-Monitor Staleness**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：模型更新应默认触发activation-monitor revalidation，并将staleness prediction、label-free realignment与labeled retraining分层。

**State / data / control owner。** `PLATFORM-MONITORING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15980v1 §§3–4 monitor-staleness benchmark and repair`；evaluation locator 为 `arXiv:2606.15980v1 §5 update-pair evaluation`；counterevidence locator 为 `arXiv:2606.15980v1 §6 limitations and monitor/model-update scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** realignment可能掩盖semantic drift且prediction会误排优先级；受测update pair不证明全部monitor可无标签修复。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15980v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-MONITORING` owner 为 [books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。Review notes 前正文 `Model Revision 必须触发 Activation Monitor 复验` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Fearless Concurrency on the GPU](https://arxiv.org/html/2606.15991v1)

**2606.15991 — Fearless Concurrency on the GPU**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：GPU kernel authoring可把tile-levelownership、host launch lifetime、async pipeline与CUDA graph replay纳入Rust type boundary，并保留显式unsafe escape。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.15991v1 §§3–5 cuTile Rust ownership and host execution model`；evaluation locator 为 `arXiv:2606.15991v1 §6 kernels and Grout inference evaluation`；counterevidence locator 为 `arXiv:2606.15991v1 §7 limitations and supported GPU/language/kernel surface`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** type safety不证明algorithm/numerical correctness；性能绑定B200/5090与受测kernel。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.15991v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前命题级锚点为 `异步工作不必永久绑定固定 Physical Core`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Auditing Reward Hackability in Code RL Training Environments](https://arxiv.org/html/2606.16062v1)

**2606.16062 — Auditing Reward Hackability in Code RL Training Environments**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：code RL task在进入训练前必须审计hackability，并让generated test先通过gold-sanity gate再交给LLM judge与promotion loop。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.16062v1 §§2–4 exploit audit and hardening procedure`；evaluation locator 为 `arXiv:2606.16062v1 §5 SWE-bench/R2E-Gym evaluation`；counterevidence locator 为 `arXiv:2606.16062v1 §6 limitations and sampled-task/gold-patch scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** gold patch也可能不完整，generated test diversity有限；49/20-task比例不外推全部RL环境。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.16062v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Reward Hacking 监测要分开 Reference 与可部署观测面`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Your "Pro" LLM Subscription May Actually Be "Free": Exposing Fingerprint Spoofing Risks in LLM Inference Services](https://arxiv.org/html/2606.16100v1)

**2606.16100 — Your "Pro" LLM Subscription May Actually Be "Free": Exposing Fingerprint Spoofing Risks in LLM Inference Services**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：黑盒 model fingerprint 在 provider 可自适应微调时不是身份凭证；gateway 必须把 attested model/version、计费证据与 challenge rotation 分开。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16100v1 §4 Problem Formulation (§4.1 Threat Model; §4.2 Fingerprint Spoofing); §5 Proposed Method (§5.2 GhostPrint Attack)`；`arXiv:2606.16100v1 §6 Experiments (§6.1 settings; §6.2–6.5 single/cross-model/continual spoofing); Appendix A implementation`；counterevidence `arXiv:2606.16100v1 §4.1 Threat Model; §6.5 Continual Fingerprint Spoofing; Appendix B additional results`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** GhostPrint 只证实行为指纹可被适配器伪造，不能证明任何现有 provider 正在欺诈；adapter 训练和持续轮换增加成本，检测漂移时回退到 attested model/version 与独立计费证据。


仅使用 `https://arxiv.org/html/2606.16100v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Referential Security：身份声明必须可持续验证`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Edge-Inference Governors Need Memory-Clock State](https://arxiv.org/html/2606.16106v1)

**2606.16106 — Beyond CPU–GPU Frequency: Memory-Clock and Tail Effects in Edge Inference Latency Estimation**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：edge inference governor 必须把独立 memory clock、tail latency、decode horizon 与 co-tenancy occupancy 纳入 deadline feasibility state。

**State / data / control owner。** `INFER-SCHEDULING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16106v1 §III Methodology (§III-A platform/clock control; §III-B roofline workloads; §III-C harness)`；`arXiv:2606.16106v1 §IV Memory-Clock Axis; §V Tails and Bursts; §VI Actuation Lag; §VII Trace-Driven Governor Evaluation`；counterevidence `arXiv:2606.16106v1 §IX Limitations; Appendix B What Is Ruled Out`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** EMC 轴和 burst tail 来自两类 Orin 平台，不能外推所有 edge GPU；多维 DVFS 增加 profiling/actuation 成本，未知 workload 或热状态下回退到保守 deadline headroom。


仅使用 `https://arxiv.org/html/2606.16106v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `Power Envelope 也要按推理阶段分配`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing](https://arxiv.org/html/2606.16135v1)

**2606.16135 — SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：多轮 serving 可在同机异构模型间借用 idle HBM/NVLink 保存 hot prefix，但 cache identity、donor pressure 与回收优先级必须由控制面持有。

**State / data / control owner。** `INFER-KV-CACHE` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16135v1 §3 SwiftCache Design (§3.2 Master Cache Manager; §3.3 overlap KV transfer; §3.4 worker; §3.5 coordination); §4 Implementation`；`arXiv:2606.16135v1 §5 Evaluations (§5.1 end-to-end; §5.2 interference; §5.3 context length; §5.4 latency)`；counterevidence `arXiv:2606.16135v1 §7 Conclusions and Discussions; §5.2 interference and §5.3 context-length stress`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 借用 idle HBM 能降低 P99 TTFT，但 donor pressure 或跨模型 identity 错配会引起抖动/污染；回收阈值失效时回退本地 KV 与普通 eviction，不能宣称跨机收益。


仅使用 `https://arxiv.org/html/2606.16135v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `流式输入把 Cache 变成可续租的 Session State`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing](https://arxiv.org/html/2606.16264v1)

**2606.16264 — Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：disaggregated serving 的 multiplexing 应联合 admission、prefill/decode placement 与 per-request SLO slack，避免局部利用率吞噬 tail budget。

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16264v1 §III Characterization and Motivation; §IV System Design (§IV-B SLO-Aware Multiplexing; §IV-C toggling)`；`arXiv:2606.16264v1 §V Evaluation (§V-A setup; §V-B SLO attainment; §V-C latency; §V-D queue; §V-E CDF)`；counterevidence `arXiv:2606.16264v1 §III-C resource-allocation motivation; §VII Conclusion and evaluation scope`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 联合 multiplexing 只改善论文 request mix 的 SLO，不证明不可估计突发同样可控；controller 依赖可估计 slack 与服务时间，突发或模型切换失配时应降级为隔离队列/保守 admission，而非继续过载。


仅使用 `https://arxiv.org/html/2606.16264v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-PD-DISAGGREGATION` owner 为 [books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。Review notes 前正文 `从静态 Pool Ratio 到耦合的 SLO Control State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Dynamic Malicious Skills in Agentic AI](https://arxiv.org/html/2606.16287v1)

**2606.16287 — Dynamic Malicious Skills in Agentic AI**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：Agent skill 审计必须覆盖安装后动态行为、trigger 与跨 skill composition；静态 manifest/代码扫描不能代表 runtime authority。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16287v1 §3 Problem Formulation (§3.2 Threat Model; §3.3 Dynamic Code Modification); §4 DyMalSkill`；`arXiv:2606.16287v1 §5 Attack Evaluation (§5.1 setup/results/ablation); §6 Defenses`；counterevidence `arXiv:2606.16287v1 §6 Defenses (§6.1 benign dynamic modification; §6.2 proposed defenses; §6.3 results); Appendix A verifier details`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** DyMalSkill 展示静态扫描遗漏动态修改，不证明所有动态 skill 恶意；runtime verifier 增加 syscall/权限摩擦，无法判定时回退只读 mount、签名包与拒绝执行。


仅使用 `https://arxiv.org/html/2606.16287v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Skill Poisoning 的真值是 Side Effect，而不是是否被调用`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [QK-Normed MLA: QK normalization without full key caching](https://arxiv.org/html/2606.16310v1)

**2606.16310 — QK-Normed MLA: QK normalization without full key caching**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：MLA 的 post-projection QK RMSNorm 可拆成可吸收的静态权重与每 token/group 动态标量，从而保留 latent KV decode path。

**State / data / control owner。** `MODEL-LONG-CONTEXT` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16310v1 §3 Method (§3.1 key-side RMSNorm; §3.2 query; §3.3 content/RoPE; §3.4 decode data flow); §4 Analysis`；`arXiv:2606.16310v1 §5 Experiments (training loss, downstream quality, decode overhead and stress)`；counterevidence `arXiv:2606.16310v1 §7 Limitations; Appendices B–E equivalence and diagnostics`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 分解 RMSNorm 保留论文 MLA decode path，但只对给定归一化/投影结构成立；数值误差或 fused-kernel 不兼容时回退原始归一化并保留完整 keys。


仅使用 `https://arxiv.org/html/2606.16310v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MODEL-LONG-CONTEXT` owner 为 [books/part-02-model/22-long-context.md](../../../../books/part-02-model/22-long-context.md)。Review notes 前命题级锚点为 `条件化机制分支与共存边界`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Filtered ANN as a Phase Transition: When Selectivity-Estimation Error Causes Plan Regret](https://arxiv.org/html/2606.16341v1)

**2606.16341 — Filtered ANN as a Phase Transition: When Selectivity-Estimation Error Causes Plan Regret**

**问题、机制与准入。** A filtered approximate-nearest-neighbor (ANN) query returns the k nearest vectors among those satisfying an attribute predicate P of selectivity s. Fresh-context 终审确认该变化触及 `AGENT-RAG` 的长期系统边界，而不是仅有章节映射或局部 benchmark，因此撤销旧 de-admit。

**State / data / control owner。** `AGENT-RAG` 是 canonical owner；跨层状态必须保留 identity、version、admission 与 fallback，论文或项目名本身不取得新 owner。

**Evidence / non-proof。** Method：`arXiv:2606.16341v1 §2 Problem and Model; §3 Phase Diagram; §4 Regret Is Critical`；Evaluation：`arXiv:2606.16341v1 §5 Experiments (setup and model-mismatch studies)`；limitations/counterevidence：`arXiv:2606.16341v1 §7 Limitations and Honest Findings`；artifact：`Not Disclosed — no later artifact used`。这些 exact-v1 位置只支持其披露 workload，不证明未披露硬件、精度、并发、SLO 或跨 workload 普遍优越性。

**Trade-off / coexistence。** 新机制提高了目标场景中的可控性或效率，但增加额外状态、估计误差或 runtime policy；原条件简单、隔离要求更强或校准证据不足时，旧路径仍是回退。

**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.16341v1` 的 exact-v1 method/evaluation/limitations。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前命题级锚点为 `从固定 Retriever 演进到可提交的 Logical / Physical Plan`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Communication-Efficient Verifiable Attention for LLM Inference](https://arxiv.org/html/2606.16352v1)

**2606.16352 — Communication-Efficient Verifiable Attention for LLM Inference**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：remote LLM serving 的 attention integrity 可由 TEE 验证 GPU 计算，并对 prefill pipeline 与超显存 decode KV 分区分别设计通信路径。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16352v1 §3 Motivation; §4 VeriAttn System Design (§4.1 verification; prefill; decode)`；`arXiv:2606.16352v1 §5 Evaluation (setup, prefill, decode and effectiveness)`；counterevidence `arXiv:2606.16352v1 §6 Discussion; appendices for detailed procedures and workflows`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** VeriAttn 只验证 attention 路径而非整个远端 serving stack，不证明端到端服务可信；TEE 通信、分页和 TCB 增加开销，验证失败时 fail closed 或回退本地受信执行。


仅使用 `https://arxiv.org/html/2606.16352v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Proof of Equation Satisfaction 不等于 Proof of Expended Work`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs](https://arxiv.org/html/2606.16358v1)

**2606.16358 — The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：LLM API router 的 plaintext authority 应收缩到 client-attested enclave；auth/scheduling/accounting 可留在 untrusted host，但目的地必须绑定 measured image。

**State / data / control owner。** `PLATFORM-GATEWAY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16358v1 §III System and Threat Model; §IV Aegis (§IV-A minimal TCB; measurement; fail-closed relay; destination binding); §V Formal Analysis`；`arXiv:2606.16358v1 §VI Implementation and Evaluation (setup, security, adaptive attack, auditability and workload runtime)`；counterevidence `arXiv:2606.16358v1 §VII Discussion and Limitations; protocol/proof appendices`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** Aegis 缩小 plaintext authority，但不能消除 client compromise、side channel 或 enclave 漏洞；attestation/relay 失败必须拒绝目的地绑定，不能静默回退到 host plaintext。


仅使用 `https://arxiv.org/html/2606.16358v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-GATEWAY` owner 为 [books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md)。Review notes 前正文 `TEE Router 只收缩 Plaintext Authority，不提供端到端正确性` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Mixtures of Subspaces for Bandwidth Efficient Context Parallel Training](https://arxiv.org/html/2606.16384v1)

**2606.16384 — Mixtures of Subspaces for Bandwidth Efficient Context Parallel Training**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：低带宽 context parallel 可用动态 mixture-of-subspaces 压缩 activation communication，但 subspace version 与重构误差必须随 step 传播。

**State / data / control owner。** `TRAIN-DISTRIBUTED-TRAINING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16384v1 §3 Method (§3.1 product-manifold optimization; §3.2 reparameterization; §3.3 communication; §3.4 dynamic subspaces; §3.5 unplugging)`；`arXiv:2606.16384v1 §5 Experiments (§5.1 setup; §5.2 bandwidth efficiency; §5.3 ablations; §5.5 baselines)`；counterevidence `arXiv:2606.16384v1 §7 Limitations; Appendix C ablations`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 95% 以上压缩与 300 Mbps 结果只绑定论文模型和网络，不证明任意 topology 保持收敛；动态 subspace 会引入重构误差与版本状态，误差或收敛漂移时停用 projection，回退未压缩 context parallel。


仅使用 `https://arxiv.org/html/2606.16384v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `TRAIN-DISTRIBUTED-TRAINING` owner 为 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)。Review notes 前正文 `Context Parallel 的 buffer 也有容量上限` 已形成 owner-level 机制链；本项已实际 Integrate。

### [BadWorld: Adversarial Attacks on World Models](https://arxiv.org/html/2606.16519v1)

**2606.16519 — BadWorld: Adversarial Attacks on World Models**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：world model 的安全 gate 需要对 observation/action perturbation 与 rollout compounding 做 adversarial contract，平均 prediction loss 不能替代 closed-loop robustness。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16519v1 §3 Background/problem setup; §4 Methodology (§4.1 velocity objective; §4.2 trajectory-adaptive bi-level optimization)`；`arXiv:2606.16519v1 §5 Experiments (§5.1 setup; §5.2 objectives; §5.3 ablation; §5.4 optimizer); Appendices B–E`；counterevidence `arXiv:2606.16519v1 §6 Conclusion; Appendix B robustness/transferability; Appendix C implementation details`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** BadWorld 证明可攻击特定视频 world model，不等于真实 closed-loop controller 必然崩溃；攻击优化成本高且 transfer 有界，部署回退应是安全控制器与 observation shield。


仅使用 `https://arxiv.org/html/2606.16519v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `VLA 威胁模型必须延伸到物理反馈`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Multimodal Evaluator Preference Collapse: Cross-Modal Coupling in Self-Evolving Agents](https://arxiv.org/html/2606.16682v1)

**2606.16682 — Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：self-evolving multimodal Agent 的 evaluator 会发生 cross-modal preference contagion；promotion 必须保留 modality-specific holdout 与 evaluator version。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16682v1 §3 Method (§3.1 TTRL; §3.2 MPCI; §3.3 contagion; §3.4 algorithm)`；`arXiv:2606.16682v1 §4 Experimental Setup; §5 Results; §6 Statistical Validation; §7.2 ablation`；counterevidence `arXiv:2606.16682v1 §7.4 Error Analysis and Failure Modes; §7.5 Limitations; §7.6 Threats to Validity`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** MPCI 显示所测 evaluator 的跨模态 contagion，不证明所有自演化系统同样崩塌；多 evaluator/holdout 增加成本，偏好漂移时冻结 promotion 并回滚 evaluator 版本。


仅使用 `https://arxiv.org/html/2606.16682v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `组件分数不能在相关错误下直接合成系统可靠性`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [PATCH: Action-Chunk-Conditioned Latent Patch Innovation Monitoring for Robot Manipulation](https://arxiv.org/html/2606.16690v1)

**2606.16690 — PATCH: Action-Chunk-Conditioned Latent Patch Innovation Monitoring for Robot Manipulation**

**问题、机制与准入。** We introduce PATCH, an action-chunk-conditioned latent patch innovation monitor for deployment-time intervention. Fresh-context 终审确认该变化触及 `MULTIMODAL-EMBODIED-VLA` 的长期系统边界，而不是仅有章节映射或局部 benchmark，因此撤销旧 de-admit。

**State / data / control owner。** `MULTIMODAL-EMBODIED-VLA` 是 canonical owner；跨层状态必须保留 identity、version、admission 与 fallback，论文或项目名本身不取得新 owner。

**Evidence / non-proof。** Method：`arXiv:2606.16690v1 §3 PATCH Framework (§3.1 action-corridor formulation; §3.2 monitor; §3.3 router)`；Evaluation：`arXiv:2606.16690v1 §4 Empirical Evaluations (§4.1 claims; §4.2 trigger benchmark; §4.3 assistive robots)`；limitations/counterevidence：`arXiv:2606.16690v1 §5 Conclusion and Limitations; Appendix A.9 score/threshold audit`；artifact：`Not Disclosed — no later artifact used`。这些 exact-v1 位置只支持其披露 workload，不证明未披露硬件、精度、并发、SLO 或跨 workload 普遍优越性。

**Trade-off / coexistence。** 新机制提高了目标场景中的可控性或效率，但增加额外状态、估计误差或 runtime policy；原条件简单、隔离要求更强或校准证据不足时，旧路径仍是回退。

**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.16690v1` 的 exact-v1 method/evaluation/limitations。

**V3 Books 复验。** 当前 `MULTIMODAL-EMBODIED-VLA` owner 为 [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Review notes 前命题级锚点为 `闭环检测必须读取动作产生时的控制状态`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents](https://arxiv.org/html/2606.16813v1)

**2606.16813 — GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：tool filtering 应从 goal-state 因果必要性生成最小可见集合，同时由 executor 保留完整授权；检索相似度不能成为权限。

**State / data / control owner。** `AGENT-TOOL-CALLING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16813v1 §III Problem Formulation; §IV GIST-CMTF (§IV-B–F goal generation, ambiguity, clarification, filtering and algorithm)`；`arXiv:2606.16813v1 §V Experimental Setup; §VI Results (§VI-A–F performance, wrong-goal, cost, backends and errors)`；counterevidence `arXiv:2606.16813v1 §IV-G Failure Modes; §VII-D reliability-friction tradeoff; §VIII Limitations and Threats`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** goal-aware filtering 降低所测 wrong-goal execution，但 clarification 会增加交互摩擦且不等于授权；歧义持续时回退暴露安全最小工具集并请求人工确认。


仅使用 `https://arxiv.org/html/2606.16813v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-TOOL-CALLING` owner 为 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)。Review notes 前命题级锚点为 `Disclosure Minimization 不能替代 Authorization`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation](https://arxiv.org/html/2606.16821v1)

**2606.16821 — How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：search Agent 的 source endorsement 可被网页 framing 操纵；评测应冻结操纵面并分离 retrieval exposure、citation 与最终 endorsement。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16821v1 §3 Threat Model; §4 Attack Taxonomy`；`arXiv:2606.16821v1 §5 Experimental Design; §6 Results (§6.1 main; §6.2 ablations; §6.3 skill recommendation)`；counterevidence `arXiv:2606.16821v1 §7 Discussion; unnumbered Static Proxy, Skill Probe, Self-Judging and Dual-Use limitations`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 静态 proxy 只证明 source framing 能操纵 endorsement，不证明开放 Web 的真实发生率；防御 prompt 或 backend 切换有成本，来源冲突时回退多源验证和拒绝背书。


仅使用 `https://arxiv.org/html/2606.16821v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Search Query 本身也是 Public Egress Action`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents](https://arxiv.org/html/2606.16824v1)

**2606.16824 — CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：coding-Agent KV workload 的 prefix reuse、branching 与长 idle gap 不同于聊天；cache manager 应按 repository/session lineage 与 reuse horizon 调度。

**State / data / control owner。** `INFER-KV-CACHE` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16824v1 §3 Coding Agent Workloads; §4 Serving Implications; §5 CacheWise Design (§5.1 scheduling; §5.2 eviction; §5.3 implementation)`；`arXiv:2606.16824v1 §6 Evaluation (§6.1 setup; §6.2 end-to-end; §6.3 ablations; §6.4 movement; §6.5 predictor; §6.6 overhead)`；counterevidence `arXiv:2606.16824v1 §3 workload scope; §6.5 predictor accuracy and §6.6 scheduling overhead`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** CacheWise 的收益只绑定采集到的 coding traces 和 vLLM 实现，不证明其他 Agent workload 同样获益；metadata predictor 漂移会错误保留 KV，压力或命中率恶化时回退 LRU/标准 prefix caching。


仅使用 `https://arxiv.org/html/2606.16824v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `从统一保留到 workload-aware eviction`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Tangram: Hiding GPU Heterogeneity for Efficient LLM Parallelization](https://arxiv.org/html/2606.16907v1)

**2606.16907 — Tangram: Hiding GPU Heterogeneity for Efficient LLM Parallelization**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：异构 GPU 并行化需要把 compute/communication capability 映射为逻辑同构 stage，并用 runtime remapping 隐藏设备差异而不掩盖 straggler。

**State / data / control owner。** `TRAIN-DISTRIBUTED-TRAINING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16907v1 §3 Tangram Design; §4 Resource and Model Decomposition; §5 Model-Slice Composition`；`arXiv:2606.16907v1 §6 Evaluation (§6.1 setup; §6.2–6.6 heterogeneity, scaling, pruning and planning)`；counterevidence `arXiv:2606.16907v1 §2.2 heterogeneous-cluster challenges; §6.6 planner scalability boundary`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** Tangram 扩展异构 plan 搜索但不能消除真实设备 straggler/故障；decomposition/planning 有编译开销，profile 不可信时回退同构 island 或保守 pipeline。


仅使用 `https://arxiv.org/html/2606.16907v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `TRAIN-DISTRIBUTED-TRAINING` owner 为 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)。Review notes 前命题级锚点为 `从手写 Plan 到可校准的并行规划器`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Greed Is Learned: Visible Incentives as Reward-Hacking Triggers](https://arxiv.org/html/2606.16914v1)

**2606.16914 — Greed Is Learned: Visible Incentives as Reward-Hacking Triggers**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：reward hacking 可由可见 incentive wording 触发；training/evaluation 必须把任务效用与可见奖励线索做 counterfactual 分离。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16914v1 §3 MoneyWorld; §§4–5 redundant versus decision-relevant channels`；`arXiv:2606.16914v1 §6 Controls/Scaling/Robustness; §7 safety-prior flip; Appendix E evaluation`；counterevidence `arXiv:2606.16914v1 §8 Discussion (§8.4 limitations and methodology); Appendix A criterion scope`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** MoneyWorld 证明决策相关 incentive channel 可诱发 hacking，不证明自然语言奖励线索普遍致因；channel blinding 可能损失有效反馈，安全 probe 失败时冻结 adaptation。


仅使用 `https://arxiv.org/html/2606.16914v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `从 Model Capability Gate 到 Deployment-context Residual Risk Loop`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Agent trajectories as programs: fingerprinting and programming coding-agent behavior](https://arxiv.org/html/2606.16988v1)

**2606.16988 — Agent trajectories as programs: fingerprinting and programming coding-agent behavior**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：coding-Agent trajectory 可规范化为 program/control-flow fingerprint，用于行为比较与约束注入；trace 相似不等于 semantic correctness。

**State / data / control owner。** `AGENT-WORKFLOW` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.16988v1 §2 Theory of Procedural Understanding (§2.1 action vocabulary; §2.2 information theory); §3 significance`；`arXiv:2606.16988v1 §4 Natural Studies; §5 Controlled Evaluations; §6 distilled-model case study`；counterevidence `arXiv:2606.16988v1 §7 Conclusion; Appendix A vocabulary algorithms and reward specifications`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** procedural fingerprint 区分十个 Agent 的行为习惯，不证明轨迹相似就是语义正确；压缩 vocabulary 可遗漏关键动作，约束导致成功率下降时回退结果级验收。


仅使用 `https://arxiv.org/html/2606.16988v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `从 Agent Trace 编译 Workflow 需要可归因的数据依赖`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing](https://arxiv.org/html/2606.17034v1)

**2606.17034 — KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：localized context erasing 应在 KV state 上学习受控 steering，并以旁观 token drift 与下游行为验证删除范围。

**State / data / control owner。** `INFER-KV-CACHE` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17034v1 §4 KVEraser (§4.1 surrogate cache; §4.2 inference complexity)`；`arXiv:2606.17034v1 §5 Experiments (§5.1–5.6 two-stage training, setup, scaling, unseen QA and ablations)`；counterevidence `arXiv:2606.17034v1 §6 Conclusion and Future Work; Appendix E failure-case breakdown; Appendix G compute`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** KVEraser 在所测 QA 上局部擦除，不证明敏感信息从参数或所有后续 state 删除；steering 会伤及旁观 token，drift 超阈值时回退重新 prefill 或清空 session。


仅使用 `https://arxiv.org/html/2606.17034v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前正文 `KV Steering 是可回滚的派生状态变换` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/html/2606.15007v1)

**2606.15007 — Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning**

**问题、旧路径与约束变化。** 只比较总参数或 active 参数便于粗略估算 capacity 与单 token compute。 长上下文、agentic reasoning 和低精度部署让 state size、kernel support、training objective 与 decode path 共同决定成本。

**机制、State / data / control owner。** Hybrid Mamba-Attention backbone、LatentMoE、MTP、NVFP4 pretraining 与多阶段 post-training 被作为同一 model-system contract 设计，而不是用单一 active-parameter 数解释效率。 model artifact 持有 architecture/precision/context/training lineage；runtime 独立验证实际吞吐和 SLO。

**Evidence：proof / non-proof。** exact-v1 technical report：550B/55B active、20T tokens、1M context、LatentMoE/MTP/NVFP4/RLVR/MOPD；厂商约 6× 吞吐只绑定其披露配置，不能外推。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 多机制协同提高效率却扩大训练与部署耦合；任一 kernel/precision 路径不满足时回退受支持精度或较简单 dense/attention 配置。

**V3 Books 复验。** 当前 [MODEL-MOE](../../../../books/part-02-model/21-moe.md) 在 Review notes 前已有命题级正文 `Total / Active Parameters 只是约束坐标，不是架构答案`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position](https://arxiv.org/html/2606.15032v1)

**2606.15032 — How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position**

**问题、旧路径与约束变化。** 视频质量与感知相似度适合筛除明显失败，成本也最低。 world model 被用于决策后，漂亮视频不能证明 action-conditioned transition 对 policy 有用。

**机制、State / data / control owner。** 把 world-model evidence 从视觉 plausibility 分成 L0–L7：预测/物理/交互一致性，直到可执行 planning、policy ranking 和 policy improvement；每一级只支撑更窄的 claim。 evaluation spec 持有 level、environment、policy 与 success criterion；模型输出不能自行声明 decision utility。

**Evidence：proof / non-proof。** exact-v1 position paper 的 taxonomy、decision-making examples 与 limitations；是证据合同而非新的 benchmark 结果。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 高层级评估更接近部署但昂贵、受 policy/environment 绑定；早期研究仍可保留低层指标，但不得越级陈述。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `World Model 评价分离 transition fidelity、decision utility 与真实闭环 outcome`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability](https://arxiv.org/html/2606.15551v1)

**2606.15551 — A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability**

**问题、旧路径与约束变化。** 局部二次近似给出简单学习率稳定条件，在曲率近似固定时足够。 现代训练常在 sharpness 超过经典阈值后仍长期降 loss，静态 Hessian 阈值无法解释。

**机制、State / data / control owner。** 将 sharpness 穿越经典稳定阈值解释为离散 gradient map 的 flip bifurcation，并用 normal/tangent decomposition 与 Lyapunov coefficient 区分局部振荡和沿低损失流形的慢运动。 optimizer state 持有 step size/momentum，loss geometry 决定局部 map；监控 sharpness 只是 sensor，不是自动调参 authority。

**Evidence：proof / non-proof。** exact-v1 theorem framework 与受限数值验证；严格结论依赖光滑性、局部分岔和结构假设，不构成所有深网训练 recipe。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 理论解释提高诊断力但计算曲率昂贵，越界也可能真正发散；假设不成立时回退 loss/gradient/step-norm 联合监控与保守 schedule。

**V3 Books Decision。** 已写入 [WORLDVIEW-WHY-MODELS-LEARN](../../../../books/part-01-worldview/04-why-models-learn.md) 正文 `Edge of Stability 是离散动力学分岔，不是“学习率越大越好”`，并通过独立 post-write 终审。

### [Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking](https://arxiv.org/html/2606.15673v1)

**2606.15673 — Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking**

**问题、旧路径与约束变化。** terminal success 易计算、可横向比较，在短单步任务中足够。 长链 Web Agent 可能找到正确页面却执行失败，也可能偶然成功但过程不合规。

**机制、State / data / control owner。** WebStep 为 GUI 旁路维护 deterministic semantic MDP，逐步记录 exploration、execution 与 recovery state，使同一失败终点可归因到不同过程错误。 environment 拥有 semantic state truth，harness 持有 action/transition receipt，scorer 才能聚合过程指标。

**Evidence：proof / non-proof。** exact-v1 1,800 tasks、五类 agents、controlled difficulty 与 semantic tracking；网站为受控本地环境，不证明开放 Web 表现。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 过程标注提高诊断力但环境建模昂贵，可能约束合法替代路径；无法建模时回退 outcome + raw trajectory +人工审计。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `Agent Evaluation 保存 semantic state transition 与 first-loss attribution`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Google's Training Supercomputers from TPU v2 to Ironwood: Architectural Stability, Scale, Resilience, Power Efficiency, and Sustainability Across Five Generations](https://arxiv.org/pdf/2606.15870v1)

**2606.15870 — Google's Training Supercomputers from TPU v2 to Ironwood: Architectural Stability, Scale, Resilience, Power Efficiency, and Sustainability Across Five Generations**

**问题、旧路径与约束变化。** 固定拓扑和连续 pod allocation 在规模小、故障少时最简单。 HBM、节点数和 pod 规模跨数量级增长后，碎片、故障域、SDC 和功耗成为训练 goodput 的一等约束。

**机制、State / data / control owner。** 五代 TPU 保持双 TensorCore、compiler-controlled memory 与 XLA 编程契约，同时把互连从 2D 扩到 3D torus、引入 OCS 做非连续 cube allocation/故障隔离，并用 FBIST 与 VPU hardware replay 发现静默错误。 compiler/runtime 持有逻辑 program/partition，fabric scheduler 持有 topology/allocation，hardware reliability plane 持有 replay/error receipt。

**Evidence：proof / non-proof。** exact-v1 PDF（TPU v2→Ironwood architecture/network/scaling/resilience/power sections）：HBM 16→192 GiB、pod 256→9216 chips、peak pod compute 约 3600×；perf/W 图为 peak/TDP，不是生产 workload。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 稳定 ISA/编译接口降低迁移成本却限制架构自由；OCS/replay 增加控制复杂度，故障或 profile 不可信时回退同构 island、重试和 checkpoint。

**V3 Books 复验。** 当前 [TRAIN-DISTRIBUTED-TRAINING](../../../../books/part-04-training-system/36-distributed-training.md) 在 Review notes 前已有命题级正文 `先定义 collective semantics，再选择可替换的数据流与实现`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [From Tokens to Regions: CUDA-Sensitive Instruction Tuning for GPU Kernel Generation](https://arxiv.org/html/2606.16231v1)

**2606.16231 — From Tokens to Regions: CUDA-Sensitive Instruction Tuning for GPU Kernel Generation**

**问题、旧路径与约束变化。** 普通 next-token SFT 数据便宜、稳定，适合语义均匀的代码任务。 kernel correctness/性能由少数同步、索引、内存和 launch 区域主导，均匀 loss 会稀释关键约束。

**机制、State / data / control owner。** 先识别与 CUDA execution constraint 强耦合的 token/region，再用 adaptive token masking 与 region-level sample weighting 分配监督，而不是平均训练整段代码。 training data 持有 region annotation，SFT objective 持有权重；compile/test harness 独立拥有 correctness receipt。

**Evidence：proof / non-proof。** exact-v1 method、compile/pass@k 与 kernel benchmarks；结论绑定受测模型、CUDA tasks 和标注过程，不证明生产 kernel 性能。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 区域标注和 masking 可能过拟合已知 pattern；编译或执行失败时回退完整 SFT、execution feedback 或人工 kernel。

**V3 Books 复验。** 当前 [TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md) 在 Review notes 前已有命题级正文 `SFT 的 supervision allocation 必须服从可执行 artifact 与能力回归`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization](https://arxiv.org/html/2606.16497v1)

**2606.16497 — daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization**

**问题、旧路径与约束变化。** 静态技巧库适合稳定硬件和常见算子，检索成本低。 新 kernel/硬件持续出现，旧技巧会失效或互相冲突，而纯 rollout 又反复探索。

**机制、State / data / control owner。** selection、policy 与 summarizer agents 共享 backbone；候选 CUDA/Triton 优化必须先通过 correctness 与 measured speedup，summarizer 才能把经验提交到动态 skill library。 execution harness 持有正确性/性能真值，skill registry 持有 provenance/version，policy 只提出候选实现。

**Evidence：proof / non-proof。** exact-v1 multi-agent/RL method、kernel benchmark 与 ablation；证据绑定受测任务、compiler/hardware，不证明跨 GPU 或 production workload。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 动态库会积累重复/错误技能并增加检索开销；验证失败或 library drift 时回退空库 baseline、静态规则或人工 tuning。

**V3 Books 复验。** 当前 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前已有命题级正文 `Skill 更新必须经过执行回执、独立 outcome 对照与版本提交`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Incentives and Evidence in Learned Service Orchestration](https://arxiv.org/html/2606.16555v1)

**2606.16555 — Incentives and Evidence in Learned Service Orchestration**

**问题、旧路径与约束变化。** 复用论文自带 baseline 能快速复现相对收益。 历史 artifact、依赖和 evaluator 漂移会让 comparator 先失效，制造虚假优势或虚假脆弱性。

**机制、State / data / control owner。** 以预注册 perturbation 重放三类 RL orchestration system，并把 artifact/runtime breakage、baseline collapse 与算法行为分开；只有 production comparator 仍有效时，learned-policy delta 才可解释。 evaluation owner 持有 runnable artifact、comparator health、perturbation 与 operational metrics；policy 不拥有自身有效性判断。

**Evidence：proof / non-proof。** exact-v1 预注册复现实验覆盖 resource allocation、DAG scheduling、autoscaling；负结果说明许多预测 reversal 未出现，不证明 RL orchestration 永远无效。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 严格重建昂贵且可能无法恢复原部署；artifact 不可复现时应降级结论并回退当前生产 baseline，而不是沿用旧分数。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `Matched Counterfactual 必须保持任务界面`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning](https://arxiv.org/html/2606.16576v1)

**2606.16576 — Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning**

**问题、旧路径与约束变化。** 开放环境 benchmark 更自然，但难知道 agent 是规划失败还是环境歧义。 要测 agent 是否构建 world model，需要可判定 hypothesis 和 interaction efficiency。

**机制、State / data / control owner。** 用 DFA membership/equivalence query 将 hidden-world discovery 变成可控、可扩展且有 oracle 的交互评估。 oracle/environment 持有 DFA truth，agent 持有 hypothesis，harness 持有 query trace。

**Evidence：proof / non-proof。** exact-v1 automata-learning testbed 与 classic algorithm comparators；只证明抽象 DFA 环境，不证明物理世界建模。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 形式环境诊断清晰但生态有效性有限；真实任务仍需可执行环境和 outcome evidence。

**V3 Books Decision。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Evaluation Identity 必须包含 Harness 与 Environment` 已覆盖该长期命题；本项为 `No Change — Existing Coverage`。

### [Look Again Before You Abstain:Budgeted Conformal Evidence Acquisition for Reliable Vision-Language Model](https://arxiv.org/html/2606.16667v1)

**2606.16667 — Look Again Before You Abstain:Budgeted Conformal Evidence Acquisition for Reliable Vision-Language Model**

**问题、旧路径与约束变化。** selective prediction 直接拒答最容易给出风险界。 把 hallucination 压到低水平可能导致超过 80% abstention，系统虽安全却不可用。

**机制、State / data / control owner。** 将 VLM 输出决策拆成 answer、abstain、acquire-evidence，并用 conformal calibration 约束 asserted claims 的 hallucination rate；预算分配器只在额外观察可降低 abstention 时请求证据。 calibration set 持有 coverage evidence，acquisition policy 持有预算，最终 answer gate 只在证据充分时 commit。

**Evidence：proof / non-proof。** exact-v1 balanced object-existence benchmark 中 5% hallucination 目标对应高拒答，并评估 budgeted acquisition；exchangeability、数据与 VLM 范围限制外不可保证。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 额外观测增加 latency/cost，错误检索还会强化幻觉；coverage 失效时回退 abstain、人工核验或更窄任务。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [A First-Principles Derivation of LLM Policy Optimization: From Expected Reward to GRPO and Its Structural Extensions](https://arxiv.org/html/2606.16733v1)

**2606.16733 — A First-Principles Derivation of LLM Policy Optimization: From Expected Reward to GRPO and Its Structural Extensions**

**问题、旧路径与约束变化。** 按算法时间线罗列易查阅。 相似名字掩盖每个方法究竟修复 variance、off-policy drift 还是 baseline 成本。

**机制、State / data / control owner。** 按 trajectory probability 与 reward 两个可改变因子解释 REINFORCE→PPO→GRPO 的结构分支。 已有 Ch33 以 objective/estimator/constraint 为 owner。

**Evidence：proof / non-proof。** exact-v1 为推导型综述，支持框架解释，不提供独立生产效果。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 统一坐标可读性高但会忽略实现细节；具体采用仍回到 workload 与训练 contract。

**V3 Books Decision。** 当前 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前的 `从 REINFORCE 到 PPO，再到 GRPO` 已覆盖该长期命题；本项为 `No Change — Existing Coverage`。

### [SoK: Security and Privacy of Foundation-Model-Powered Robots](https://arxiv.org/html/2606.16788v1)

**2606.16788 — SoK: Security and Privacy of Foundation-Model-Powered Robots**

**问题、旧路径与约束变化。** 按 jailbreak/backdoor 类别总结便于按攻击名检索。 物理 action 将同一漏洞沿感知、world state、controller 和 fleet communication 放大。

**机制、State / data / control owner。** 按 foundation model、embodied pipeline、ecosystem 与 governance 四层组织机器人 security/privacy trust boundary。 已有 Security owner 按 first-compromised trust boundary 组织风险。

**Evidence：proof / non-proof。** exact-v1 SoK 的 96-paper taxonomy；是二级证据与研究密度地图，不证明现实事故概率。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** taxonomy 提供覆盖地图但编码含判断；控制仍需各 state owner 的实证。

**V3 Books Decision。** 当前 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前的 `从 Model Capability Gate 到 Deployment-context Residual Risk Loop` 已覆盖该长期命题；本项为 `No Change — Existing Coverage`。

### [Follow the Latent Roadmap: Navigating Revocable Decoding for Diffusion LLMs with Anchor Tokens](https://arxiv.org/html/2606.16847v1)

**2606.16847 — Follow the Latent Roadmap: Navigating Revocable Decoding for Diffusion LLMs with Anchor Tokens**

**问题、旧路径与约束变化。** 全量 remask/refine 简单且保留并行生成优势。 错误 token 互相强化时，局部验证不能区分可信上下文与待修正状态。

**机制、State / data / control owner。** 从时间一致性选择 anchor tokens，并把 anchor cache 与可撤销生成/扰动验证分离，避免新 token 在 mixed-quality context 中吸收错误。 decoder 持有 editable/anchor masks 与 cache lineage；只有验证通过的 anchor 可参与后续条件。

**Evidence：proof / non-proof。** exact-v1 LLaDA-8B、Dream-7B 的 math/code experiments；不证明所有 diffusion LM 或任务具备相同 temporal consistency。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** anchor 选择错误会冻结错误，双路径验证增加计算；置信不足时回退更保守 remasking 或 autoregressive decode。

**V3 Books 复验。** 当前 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 在 Review notes 前已有命题级正文 `Editable tokens 在 Commit 前保持可撤销`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Human-on-the-Bridge: Scalable Evaluation for AI Agents](https://arxiv.org/html/2606.16871v1)

**2606.16871 — Human-on-the-Bridge: Scalable Evaluation for AI Agents**

**问题、旧路径与约束变化。** Human-in-the-loop 对少量高风险样本最可信。 长时 Agent 的 phantom tool calls、漏调 mandatory tools 与 policy drift 需要规模化、多轮复验。

**机制、State / data / control owner。** 专家先构造 traps、jurors、rules 与 fallback，再由 harness 在大量 turns 上重复执行，把 human judgment 从逐请求审批变成版本化 evaluation policy。 human owner 定义规则/fallback，harness 持有 versioned cases/trace，LLM judge 只作 sensor。

**Evidence：proof / non-proof。** exact-v1 约 23,500 turns 的多轮评估；结论绑定作者任务、judge 和规则，不证明完全替代人工审查。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 预编译规则提高规模但会陈旧并遗漏未知 failure；分布变化时回退人工复核、red-team 与规则 revision。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `Human–Agent Team 必须成为独立 Evaluation Object`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/html/2606.16993v1)

**2606.16993 — DreamX-World 1.0: A General-Purpose Interactive World Model**

**问题、旧路径与约束变化。** 短片段 video generation 适合视觉预训练与局部 future prediction。 interactive environment 要支持导航、回访和事件修改，独立 clip 会遗忘空间状态。

**机制、State / data / control owner。** E-PRoPE 编码相机轨迹，causal forcing/DMD distillation 与 memory-conditioned residual recycling 延长可交互视频状态，使重访区域受到历史约束。 world-model runtime 持有 camera/event/memory lineage；生成帧仍是预测，不拥有真实环境提交权。

**Evidence：proof / non-proof。** exact-v1 data engine、method、long-horizon evaluation 与 8×RTX5090 上 16 FPS 的作者结果；不证明 action-conditioned causal dynamics 或 policy utility。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 持久 memory 增加漂移和计算，错误历史会自我强化；控制任务回退真实 observation、simulator state 与 closed-loop verifier。

**V3 Books 复验。** 当前 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 在 Review notes 前已有命题级正文 `Persistent World State 需要流式更新与观测校正`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Exploding and vanishing gradients in deep neural networks: the effect of residual connections](https://arxiv.org/html/2606.17013v1)

**2606.17013 — Exploding and vanishing gradients in deep neural networks: the effect of residual connections**

**问题、旧路径与约束变化。** 逐层链式法则已能直观解释梯度乘积。 仅说梯度相乘无法精确区分深度极限中的典型增长率与 residual 的作用。

**机制、State / data / control owner。** 用 multiplicative ergodic theory 描述深层 Jacobian product 的 Lyapunov exponents，并说明 identity residual term 如何改变梯度指数增长/衰减率。 这是模型/优化动力学解释，不是运行时控制器；训练系统仍以观测到的 gradient/loss 负责决策。

**Evidence：proof / non-proof。** exact-v1 理论命题；未提供覆盖现代 Transformer 全部非线性、归一化与 optimizer 的经验结论。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 理论提高因果理解但假设抽象；实践仍需 initialization、normalization、clipping 和 schedule 联合验证。

**V3 Books 复验。** 当前 [WORLDVIEW-WHY-MODELS-LEARN](../../../../books/part-01-worldview/04-why-models-learn.md) 在 Review notes 前已有命题级正文 `Residual connection 使深层 Jacobian product 保留 identity path`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [ExpRL: Exploratory RL for LLM Mid-Training](https://arxiv.org/html/2606.17024v1)

**2606.17024 — ExpRL: Exploratory RL for LLM Mid-Training**

**问题、旧路径与约束变化。** SFT 直接注入 curated reasoning trace 稳定，sparse GRPO 则目标最干净。 base model 没有探索 coverage 时，sparse reward 无法发现有效轨迹，而人工 SFT 预设了策略形状。

**机制、State / data / control owner。** 用隐藏 reference solution 生成 decomposition/verification/self-correction 等稠密探索信号，在 mid-training 扩展 base-policy coverage，再切回真实任务 outcome RL。 training pipeline 持有 private scaffold/reference 与 phase boundary；部署模型不得访问或声称这些隐藏真值。

**Evidence：proof / non-proof。** exact-v1 math-centered experiments，对比 SFT、sparse GRPO 与 self-distillation；依赖 reference/judge，不证明开放任务同样有效。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 稠密 signal 可能 reward hack、泄漏答案或过拟合 verifier；reference 不可靠时回退 SFT、可验证 outcome 或不执行该阶段。

**V3 Books 复验。** 当前 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前已有命题级正文 `RL mid-training 的训练奖励不等于部署期 environment authority`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/html/2606.17030v1)

**2606.17030 — Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation**

**问题、旧路径与约束变化。** 为每个 embodiment 训练 action-specific model，接口清楚且可直接控制。 action schema 不统一限制跨域数据复用，语言可作为共享条件接口。

**机制、State / data / control owner。** Double-stream MMDiT 结合冻结 Qwen2.5-VL，以 8.6M 视频和 general→expert curriculum 学习跨 manipulation/driving/navigation 的语言条件视觉 transition。 world model 持有预测视频/条件 lineage，controller 与真实环境仍持有 action schema、safety envelope 和 effect receipt。

**Evidence：proof / non-proof。** exact-v1 technical report 的 architecture/data/curriculum 与 benchmark；零样本视频质量不证明真实物理闭环或 controller success。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 语言统一接口提高数据规模却丢失低层控制精度和因果保证；执行时回退 embodiment-specific controller、real observation 和 safety monitor。

**V3 Books 复验。** 当前 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 在 Review notes 前已有命题级正文 `language-conditioned video forecast 不拥有 physical action authority`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [SWARM-LLM: Collaborative Inference for Edge-based Small Language Models](https://arxiv.org/html/2606.14711v1)

**2606.14711 — SWARM-LLM: Collaborative Inference for Edge-based Small Language Models**

**问题、旧路径与约束变化。** edge-only 在简单请求和隐私优先时低延迟，cloud-only 在高难任务中能力稳定。 异构小模型既可能协作补能力，也可能把敏感或危险请求错误升级到云。

**机制、State / data / control owner。** 按请求使用 uncertainty 与 safety signal 在 local、peer collaboration 和 cloud escalation 间选择。 gateway 持有路由与 disclosure policy；各模型只返回 proposal，不能自行升级权限。

**Evidence：proof / non-proof。** exact-v1 system/evaluation 覆盖三种 SLM、一个 70B cloud API 与受控 easy/hard/safety workload；约四分之一云调用不是生产比例。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 估计器漂移会误路由，peer 协作增加延迟；信号不可信时回退本地拒答或固定受审云路径。

**V3 Books 复验。** 当前 [PLATFORM-GATEWAY](../../../../books/part-06-ai-infrastructure/62-gateway.md) 在 Review notes 前已有命题级正文 `Gateway 先按 privacy、安全与 data residency 建立 eligible set，再优化成本与延迟`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Context Compression Is Not One Thing: Readable Symbolic Re-expression vs. Coherent Summary at Matched Budget](https://arxiv.org/html/2606.14875v1)

**2606.14875 — Context Compression Is Not One Thing: Readable Symbolic Re-expression vs. Coherent Summary at Matched Budget**

**问题、旧路径与约束变化。** 连贯 prose summary 对人可读，在单跳问答中足够。 相同 token budget 下，摘要可能删除实体关系，压缩率不能代表 evidence preservation。

**机制、State / data / control owner。** 将 passage 重写为可读 entity–relation statements，并与删除、截断和同编码器摘要做 matched-budget 比较。 context layer 持有压缩 lineage 与原证据 locator；压缩文本不取得事实 authority。

**Evidence：proof / non-proof。** exact-v1 method/evaluation 覆盖 MuSiQue、TwoWiki、HotpotQA；深度交互假设为 null，结果不支持随 reasoning depth 普遍扩大优势。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 符号重写可能损失语气、否定和出处；高风险 claim 回退原文片段与引用。

**V3 Books 复验。** 当前 [AGENT-CONTEXT](../../../../books/part-07-agent/75-context.md) 在 Review notes 前已有命题级正文 `Context Compression 以未来决策充分性、provenance 与可回源性为合同`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations](https://arxiv.org/html/2606.15008v1)

**2606.15008 — Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations**

**问题、旧路径与约束变化。** 多 agent 投票或并行提案可以提高覆盖率。 any-one-can-trigger 的 effect aggregation 让单个脆弱 agent 取得整体执行权。

**机制、State / data / control owner。** 把 aggregation rule、privilege drift、boundary failure 和 attacker capability curve 纳入安全对象，并在执行前 policy gate。 全局 authorizer 持有 effect commit；agent 数量不能扩大 principal authority。

**Evidence：proof / non-proof。** exact-v1 threat model/evaluation 报告 1→7 agents 的 compromise 增长及 mitigation；数字绑定 OpenClaw 构型和受测模型。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 门控降低 utility 并增加 latency；高风险 effect 回退 quorum、least privilege 与人工批准。

**V3 Books 复验。** 当前 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前已有命题级正文 `Multi-Agent 聚合不能把最弱成员升级为系统 authority`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/html/2606.15017v1)

**2606.15017 — Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents**

**问题、旧路径与约束变化。** 增加 skill/memory module 常能改善单次任务成功率。 模块自身每次消耗 token；若不计总预算，会把更多 compute 误认成更好记忆。

**机制、State / data / control owner。** 固定 actor+module 总 token budget，与把同预算给 vanilla actor 的 baseline 比较，并报告 run variance。 evaluation run 持有全链 token ledger 与 seed distribution；模块不能只报告自身局部成本。

**Evidence：proof / non-proof。** exact-v1 覆盖 WebArena/WorkArena、三模型和三种 augmentation；只证明 online setting，不否定离线摊销或特定领域技能。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** matched budget 可能改变探索深度；可复用离线资产仍需按 amortized cost 单独评估。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `Agent 组件收益必须采用 token/compute-matched counterfactual`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Resilient Consensus in Agentic AI](https://arxiv.org/html/2606.15024v1)

**2606.15024 — Resilient Consensus in Agentic AI**

**问题、旧路径与约束变化。** 自然语言协商灵活，适合低风险意见汇总。 LLM agent 在理论可达的 Byzantine consensus 条件下仍可能不收敛。

**机制、State / data / control owner。** 在 agent 外包裹 classical resilient filter，并将 topology robustness 与模型行为分开。 协议层持有 membership、round 与 commit rule；模型消息只是输入。

**Evidence：proof / non-proof。** exact-v1 controlled complete/general graph experiment 支持所测 agents 与 horizon；不证明所有模型或真实网络。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 过滤器降低表达自由且依赖 fault bound；假设不成立时回退中心化 coordinator 或人工裁决。

**V3 Books Decision。** `[AGENT-MULTI-AGENT](../../../../books/part-07-agent/82-multi-agent.md)` 在 Review notes 前已有 `Multi-Agent 共识需要外部协议约束` 的长期命题；本项为 `No Change — Existing Coverage`。

### [OSGuard: A Benchmark for Safety in Computer-Use Agents](https://arxiv.org/html/2606.15034v1)

**2606.15034 — OSGuard: A Benchmark for Safety in Computer-Use Agents**

**问题、旧路径与约束变化。** 逐 action 分类便于诊断 guardrail。 局部判断正确不保证整个任务不会以危险捷径完成。

**机制、State / data / control owner。** 同一用户目标下同时维护 action-level label 与 OSWorld-derived state invariant，区分 nominal success 与 safe completion。 environment evaluator 持有真实系统状态与 safety invariant；guardrail 只提供局部判定。

**Evidence：proof / non-proof。** exact-v1 benchmark/method/evaluation 支持人工构造的风险变体；不证明开放桌面 hazard 覆盖完备。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 状态 invariant 维护昂贵且可能拒绝合法替代路径；覆盖不足时保留轨迹与人工复核。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `Computer-use evaluation 同时保存局部 action checks 与端到端 invariant`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents](https://arxiv.org/html/2606.15057v1)

**2606.15057 — AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents**

**问题、旧路径与约束变化。** 静态注入集适合可重复回归。 攻击者会针对 defense 迭代，且 action-open request 把关键参数合法地委托给不可信内容。

**机制、State / data / control owner。** 用黑盒 attack optimizer 重放 defense，并按任务 specification 是否封闭 action space 分层报告 ASR。 security harness 持有攻击预算、task spec 与 effect receipt；detector 分数不能独自宣告安全。

**Evidence：proof / non-proof。** exact-v1 覆盖三套任务、五模型和多类 defense；28%/64% 是其自适应预算与 action-open slice。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 自适应评测成本高且仍非最坏情况；高风险任务回退精确参数、capability restriction 与 effect authorization。

**V3 Books 复验。** 当前 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前已有命题级正文 `IPI 防御必须在 adaptive attack 与 effect-time authorization 下验收`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Is Code Better Than Language for Algorithmic Reasoning](https://arxiv.org/html/2606.15589v1)

**2606.15589 — Is Code Better Than Language for Algorithmic Reasoning**

**问题、旧路径与约束变化。** 自然语言或代码都可作为中间表征。 把代码格式与真实解释器执行同时改变，会混淆工具收益来源。

**机制、State / data / control owner。** 增加 model-simulated-code intervention，保持表示改变但移除 deterministic executor，再与真实执行比较。 agent 生成 trace，解释器拥有计算真值与 receipt；模型模拟不得冒充执行。

**Evidence：proof / non-proof。** exact-v1 40-task verifiable benchmark 支持 +31.6pp execution 与 +0.15pp representation 对比；范围只限所测算法任务。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 外部执行扩大 sandbox 与供应链风险；不可安全执行时回退验证器、形式约束或人工计算。

**V3 Books 复验。** 当前 [AGENT-TOOL-CALLING](../../../../books/part-07-agent/78-tool-calling.md) 在 Review notes 前已有命题级正文 `Tool output 是 observation，外部 executor 才拥有执行结果`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [PathRouter: Aligning Rewards with Retrieval Quality in Agentic Graph Retrieval-Augmented Generation](https://arxiv.org/html/2606.16409v1)

**2606.16409 — PathRouter: Aligning Rewards with Retrieval Quality in Agentic Graph Retrieval-Augmented Generation**

**问题、旧路径与约束变化。** outcome-only reward 在答案可验证时简单。 正确答案可能来自捷径，trajectory scalar 也无法定位错误 retrieval action。

**机制、State / data / control owner。** 按 answer correctness × path overlap 分组缩放 GRPO advantage；evidence-poor rollout 只在 reasoning/query token 接受 frozen teacher KL。 reward pipeline 持有 gold evidence path 与 token mask；teacher 不监督 answer token。

**Evidence：proof / non-proof。** exact-v1 六 QA benchmark、三模型规模与 ablation 支持其提升；path overlap 依赖 gold path，不代表唯一合法证据。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 路径奖励可能压制替代证据；无可靠 gold path 时回退 outcome reward 加可审计 retrieval trace。

**V3 Books 复验。** 当前 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前已有命题级正文 `RAG 评估分离 retrieval/path evidence 与最终 answer outcome`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/html/2606.16420v1)

**2606.16420 — Transferable Self-Evolving Playbooks for Agentic Security Auditing**

**问题、旧路径与约束变化。** 人工 playbook 在任务稳定时最可控。 漏洞和工具变化使静态 skill 过期，而未经验证的自动总结会污染后续 run。

**机制、State / data / control owner。** audit agent rollout、ground-truth evaluator 打分，reviser 仅根据失败分析提交 playbook revision，并测跨模型/harness transfer。 skill registry 持有 provenance/version；evaluator receipt 决定 commit，agent 不能自证成功。

**Evidence：proof / non-proof。** exact-v1 open-source advisory experiment 支持受测 agent/harness 的 acquisition/transfer；不证明一般安全审计或无双用途风险。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 演化可能过拟合已知 advisory；无可信 oracle 时回退人工维护和隔离 sandbox。

**V3 Books Decision。** `[AGENT-PLATFORM](../../../../books/part-07-agent/84-agent-platform.md)` 在 Review notes 前已有 `Skill 更新必须经过执行回执与版本提交` 的长期命题；本项为 `No Change — Existing Coverage`。

### [Privacy from Symmetry: Orthogonally Equivariant Transformers for LLM Inference](https://arxiv.org/html/2606.16461v1)

**2606.16461 — Privacy from Symmetry: Orthogonally Equivariant Transformers for LLM Inference**

**问题、旧路径与约束变化。** 普通 split inference 隐藏 token 但会暴露可逆 embedding。 对 activation 加噪会损害 utility，重型密码协议成本高。

**机制、State / data / control owner。** client 用秘密正交矩阵旋转 embedding，server 的 ConjFormer 通过 scalar RMSNorm 与 conjugated weights 在旋转基底执行。 client 持有 secret basis；server 只能观察 rotated state，模型 artifact 必须绑定转换。

**Evidence：proof / non-proof。** exact-v1 GPT-2/Llama3.2-1B PubMed experiment 支持 direct nearest-neighbor inversion 降低；不是密码学保密证明。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 需要专门架构与 fine-tuning，侧信道/组合攻击仍未知；不满足时回退本地/TEE/cryptography。

**V3 Books Decision。** 已写入 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 正文 `Split Inference 的表示保护可以写进模型对称性`，并通过独立 post-write 终审。

### [BRICKS-WM: Building Reusability via Interface Composition Kinetics for Structured World Models](https://arxiv.org/html/2606.16489v1)

**2606.16489 — BRICKS-WM: Building Reusability via Interface Composition Kinetics for Structured World Models**

**问题、旧路径与约束变化。** monolithic latent dynamics 在单 agent/environment 配对下最简单。 替换 agent 会迫使不变的背景动力学一起重训。

**机制、State / data / control owner。** 将 actuated agent 与 background dynamics 分开，通过 learned latent interface 组合 transition，并冻结复用背景模块。 各模块持有自己的 transition state/version；interface 定义交互，不把视觉分割当功能边界。

**Evidence：proof / non-proof。** exact-v1 MBRL experiments 支持从头训练可比和跨 agent 背景复用；只覆盖受测连续控制环境。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 错误分解会漏掉强耦合接触；不可分环境回退 monolithic model。

**V3 Books Decision。** 已写入 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 正文 `World Model 可按动力学责任拆成可复用模块`，并通过独立 post-write 终审。

### [Tail-Shape Estimation in LLM Evaluation Is Fragile: A Protocol for Diagnosing False Positives](https://arxiv.org/html/2606.16511v1)

**2606.16511 — Tail-Shape Estimation in LLM Evaluation Is Fragile: A Protocol for Diagnosing False Positives**

**问题、旧路径与约束变化。** 均值与普通 tail magnitude 易解释，适合样本有限的 release comparison。 极值 tail-index 容易把 threshold 选择和 scorer 结构误认成新风险信号。

**机制、State / data / control owner。** 预注册 admissibility、fit、threshold stability 与 effect-size gates，再允许 tail-shape claim。 evaluation spec 持有 estimator、threshold 与 rejection rule；漂亮 tail fit 不取得 release authority。

**Evidence：proof / non-proof。** exact-v1 在两个 scorer family 的 toxicity setup 捕获三类 false positive，并拒绝 headline claim；不是所有 tail risk 的否定。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 严格 gate 会降低检出力；数据不足时回退区间、CVaR/quantile 或不发布 tail-index。

**V3 Books Decision。** `[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)` 在 Review notes 前已有 `Tail Metric 也必须先通过可识别性与稳定性 Gate` 的长期命题；本项为 `No Change — Existing Coverage`。

### [SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents](https://arxiv.org/html/2606.16591v1)

**2606.16591 — SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents**

**问题、旧路径与约束变化。** 小工具集可全部放进 prompt。 工具扩到数千项且子目标在执行中出现时，静态注入昂贵，一次检索又看不见后续 intention。

**机制、State / data / control owner。** 维护 intention–tool–collaboration graph，随 observation/subgoal 主动检索局部 schema。 harness 持有 current intention 与 admitted tool set；模型只能从可见集合提案。

**Evidence：proof / non-proof。** exact-v1 7,471 tools、三 benchmark 支持 recall/success 与 schema exposure；不证明开放工具描述可信。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 意图图会陈旧或误连；检索置信不足时回退关键词/人工目录并限制 capability。

**V3 Books 复验。** 当前 [AGENT-TOOL-CALLING](../../../../books/part-07-agent/78-tool-calling.md) 在 Review notes 前已有命题级正文 `Tool discovery 是 query-conditioned proposal，不能替代逐工具授权`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [VeriGraph: Towards Verifiable Data-Analytic Agents](https://arxiv.org/html/2606.16603v1)

**2606.16603 — VeriGraph: Towards Verifiable Data-Analytic Agents**

**问题、旧路径与约束变化。** 线性 trace 易生成、便于阅读。 数值计算、grounding 与语义推导混在文本中后，终结论无法回溯到原数据。

**机制、State / data / control owner。** 用 computational、grounding、derivational 三类 expansion 构建异构 DAG，以 reachability 检查结构 traceability，再单独评估 semantic support。 原始数据与 interpreter receipt 持有数值真值；claim node 保存 derivation/provenance，不自证语义。

**Evidence：proof / non-proof。** exact-v1 四 benchmark 与 claim-level grounding evaluator 支持受测系统；87.61% 是作者 evaluator 下的结果。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 图构建增加 token/存储，semantic judge 仍会错；低风险任务可回退线性 trace，高风险 claim 必须保留原始 receipt。

**V3 Books 复验。** 当前 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md) 在 Review notes 前已有命题级正文 `Workflow 的 canonical DAG 与 evidence graph 由平台拥有`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control](https://arxiv.org/html/2606.16605v1)

**2606.16605 — ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control**

**问题、旧路径与约束变化。** 只攻击 observation 或 action output 易执行。 world-model agent 的 value、RSSM state 与 transition 也可能成为更早的脆弱点。

**机制、State / data / control owner。** 按 component loss × step budget × temporal exposure 构造攻击矩阵，并比较 input defense recovery。 evaluation harness 持有攻击位置、时序和 component identity；terminal reward 不能独自定位 owner。

**Evidence：proof / non-proof。** exact-v1 四 Dreamer-style agents、20 tasks 与五 white-box objective 支持该矩阵；不证明真实攻击频率。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 白盒 attack 偏强且 benchmark 昂贵；生产中回退 threat-tiered subset、在线 sensor 与 safe controller。

**V3 Books 复验。** 当前 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已有命题级正文 `World Model evaluation 分离 dynamics、policy、value 与闭环 outcome`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [User as Code: Executable Memory for Personalized Agents](https://arxiv.org/html/2606.16707v1)

**2606.16707 — User as Code: Executable Memory for Personalized Agents**

**问题、旧路径与约束变化。** 检索式 bag-of-facts 在事实回忆中简单有效。 矛盾消解、跨记录聚合和主动规则触发需要确定性状态转换，而相似度检索不会自动执行。

**机制、State / data / control owner。** 保留 append-only log，周期性编译为 typed objects/functions checkpoint；查询在代码状态上执行。 log 是原始事实账本，typed code 是可重建派生状态；解释器只执行有版本规则。

**Evidence：proof / non-proof。** exact-v1 LOCOMO 与 aggregate/alert tasks 支持受测 memory system；近 99% 聚合结果依赖其 schema、compiler 和 benchmark。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 生成代码有注入、bug 与 schema migration 风险；无法安全编译时回退检索、人工确认与只读规则。

**V3 Books 复验。** 当前 [AGENT-MEMORY](../../../../books/part-07-agent/77-memory.md) 在 Review notes 前已有命题级正文 `Append-only evidence 与可执行 derived memory state 分离`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Taming Curvature: Architecture Warm-Up for Stable Transformer Training](https://arxiv.org/html/2606.16768v1)

**2606.16768 — Taming Curvature: Architecture Warm-Up for Stable Transformer Training**

**问题、旧路径与约束变化。** 固定深度配合 LR warm-up 是主流且实现简单。 preconditioned curvature 随深度突增时，loss spike 与 divergence 不能仅靠统一 LR 解释。

**机制、State / data / control owner。** 用 warm-started power iteration 在线估计最大预条件 Hessian eigenvalue，并逐步增加网络深度限制 curvature surge。 trainer 持有 active depth、optimizer/preconditioner 与 curvature sensor；sensor 不自动拥有调度 authority。

**Evidence：proof / non-proof。** exact-v1 theory与 billion-parameter experiments 支持在线 estimator 和稳定性改善；不构成所有 architecture/optimizer 的 recipe。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** HVP 与拓扑扩展增加复杂度，深度切换改变训练状态；小模型或稳定配置仍回退普通 LR warm-up。

**V3 Books Decision。** 已写入 [TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md) 正文 `Architecture Warm-up 只能作为受测曲率压力的 Actuator`，并通过独立 post-write 终审。

### [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled Policy Optimization](https://arxiv.org/html/2606.16771v1)

**2606.16771 — GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled Policy Optimization**

**问题、旧路径与约束变化。** 将各 reward 独立归一化再相加能保持实现清晰。 同 rollout 在不同目标上正负相反时，聚合会抵消有效更新。

**机制、State / data / control owner。** 按 reward disagreement 过滤严重冲突 rollout，并以 query-level consensus 动态重加权更新。 reward pipeline 保存每维 advantage 与 mask；最终 policy update 不能丢失冲突 provenance。

**Evidence：proof / non-proof。** exact-v1 tool-calling/preference scenarios 与 ablation 支持其训练效率；过滤后的 Pareto trade-off 和长期偏差仍未充分证明。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 过滤会删除困难但重要样本并偏向一致目标；冲突无法消解时回退 Pareto/约束优化或分阶段训练。

**V3 Books 复验。** 当前 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前已有命题级正文 `多 Reward 聚合不能掩盖 Channel Collapse 与梯度冲突`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models](https://arxiv.org/html/2606.16825v1)

**2606.16825 — Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models**

**问题、旧路径与约束变化。** 每层独立 expert 最大化表达自由，但模型/optimizer memory 随层数线性增长。 许多层级 expert 路径存在参数冗余，active compute 不变却必须驻留全量权重。

**机制、State / data / control owner。** 跨连续层 tying expert weights，保留各层 attention 与独立 router。 shared expert artifact 有统一版本；每层 router 仍拥有 token dispatch，不得合并统计。

**Evidence：proof / non-proof。** exact-v1 OLMoE/Qwen3/DeepSeek-style pretraining 支持近 2x expert-memory reduction 与受测质量；未证明所有规模和 serving kernel。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 共享会削弱层特化并产生更新耦合；质量下降或并行布局不利时回退独立 expert。

**V3 Books Decision。** 已写入 [MODEL-MOE](../../../../books/part-02-model/21-moe.md) 正文 `MoE 可以共享 Expert Parameters，同时保留逐层 Routing State`，并通过独立 post-write 终审。

### [Directory-Aware Query and Maintenance in Vector Databases](https://arxiv.org/html/2606.16903v1)

**2606.16903 — Directory-Aware Query and Maintenance in Vector Databases**

**问题、旧路径与约束变化。** flat scalar metadata 与 path expansion 在小目录中足够。 递归查询和目录移动使在线 expansion 变慢、离线 expansion 产生写放大与一致性问题。

**机制、State / data / control owner。** 把目录拓扑作为 trie index，分别定义 directory-semantic query 与 maintenance。 vector store 持有 path/tree identity 和原子结构更新；应用层不再复制展开结果。

**Evidence：proof / non-proof。** exact-v1 ByteDance Viking implementation、WIKI-Dir/ARXIV-Dir benchmark 支持三策略比较；结果绑定其 workload。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** trie 增加索引和迁移成本；层级浅且更新少时 flat metadata 仍更简单。

**V3 Books Decision。** `[AGENT-RAG](../../../../books/part-07-agent/76-rag.md)` 在 Review notes 前已有 `Retrieval Index 必须保留原生 Hierarchy` 的长期命题；本项为 `No Change — Existing Coverage`。

### [LESS Is More: Mutual-Stability Sampling for Diffusion Language Models](https://arxiv.org/html/2606.16908v1)

**2606.16908 — LESS Is More: Mutual-Stability Sampling for Diffusion Language Models**

**问题、旧路径与约束变化。** 固定 denoising step 易实现并保持可预测计算。 稳定位置被反复计算，而单步高置信也可能过早提交不稳定 token。

**机制、State / data / control owner。** 只有 top-1 confidence、token persistence 与 top-K distribution JSD 同时稳定才 unmask。 sampler 持有跨 step distribution history 与 commit mask；单步 logit 不拥有 final commit。

**Evidence：proof / non-proof。** exact-v1 三个 dLLM、七 benchmark 与 wall-clock/step evaluation 支持减少 72.1% steps；阈值仍绑定受测模型。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 保守联合 gate 可能延迟困难 token；历史不足或校准漂移时回退固定预算。

**V3 Books 复验。** 当前 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 在 Review notes 前已有命题级正文 `Diffusion token 的稳定性只支持 proposal，runtime 独占 commit/rollback`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### [TokenPilot: Cache-Efficient Context Management for LLM Agents](https://arxiv.org/html/2606.17016v1)

**2606.17016 — TokenPilot: Cache-Efficient Context Management for LLM Agents**

**问题、旧路径与约束变化。** 随时剪掉低相关文本能直接减少 token。 任意序列变更会破坏稳定 prefix，节省的 token 可能换来 cache invalidation。

**机制、State / data / control owner。** ingestion-aware compaction 固定全局 prefix，lifecycle-aware eviction 只在 segment relevance 到期的批次边界移除。 context manager 持有 segment lifecycle 与 cache lineage；模型 relevance 只作为 eviction sensor。

**Evidence：proof / non-proof。** exact-v1 PinchBench/Claw-Eval isolated/continuous mode 支持成本下降；数字绑定其 harness 和 cache implementation。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 延迟 eviction 保留无用 token，误判会删关键状态；不支持 prefix cache 时回退普通 compaction。

**V3 Books 复验。** 当前 [AGENT-CONTEXT](../../../../books/part-07-agent/75-context.md) 在 Review notes 前正文 `canonical prefix 与 segment lifecycle` 已形成 owner-level 机制链；本项已实际 Integrate。

### [DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents](https://arxiv.org/html/2606.17029v1)

**2606.17029 — DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents**

**问题、旧路径与约束变化。** 直接让 LLM 根据 query 写 rubric 成本低。 模型若未识别信息需求，reward 会遗漏关键证据并训练出表面完整报告。

**机制、State / data / control owner。** 先递归构建 evidence-backed subquestion tree，以叶子形成 atomic target，再从 target 合成 query 与 rubric pair。 dataset pipeline 持有 evidence tree/provenance；rubric scorer 只评价被显式绑定的 target。

**Evidence：proof / non-proof。** exact-v1 9K pairs、三 benchmark 与 GPU-hour comparison 支持其训练效率；evidence tree 质量仍受检索与生成误差影响。 本报告只采用 exact-v1，不用 later revision 扩张结论。

**Trade-off / failure / coexistence / fallback。** 构树昂贵且可能固化单一路径；开放问题回退人工 rubric、multiple evidence trees 与 post-hoc audit。

**V3 Books 复验。** 当前 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前已有命题级正文 `Evidence-derived Rubric 是版本化 Reward State`；它已承载本项可长期保留的机制与边界，exact-v1 仅作为受限证据，不再形成新的 owner-level 增量。本项为 `No Change — Existing Coverage`。

### Books / semantic audit

Fresh-context 独立复核以 level-2 `Review notes` 为正文边界。100 个冻结候选中，23 项已有完整正文机制链，77 项有不依赖 source trace 的命题级覆盖。此次将 29 项仅能复述现有机制或局部 operating point 的提案降级；新增 5 项逐条核对唯一 canonical marker、正文边界、完整机制链和章节衔接，章末 trace、source marker 和 proposal artifact 均未被用作正文落地证明。

## 5. 缺口与下一步

无

ordinary pending、材料请求与 Books body writeback queue 均为 0。1086 项已完成分母前关闭，不构成待办。

### Repository Changes

- 完成 1186 个 raw identities 的逐项 title + 完整 abstract 语义复核，冻结 100 个 Candidate、关闭 1086 项。
- 独立复核将 29 项 proposal 降级为 Existing Coverage；剩余 5 个 Integrate family 已写入 owner 正文并通过 post-write 终审。

## 6. 复核

当前来源再认证复核者：\`june_11_20_recert\`（独立于原报告作者）。当前合同来源再认证补齐十三个官方 Daily 源；未发现需恢复的独立候选，原 Candidate/Evidence/Books 结论保持不变。

复核者：june_15_16_independent_books_gate_reaudit（fresh context）
复核范围：1186 个 raw identities 的 title + full abstract 准入、100 个 retained 的 evidence boundary、77 个 Existing anchor 与 23 个 Integration Decision；重点逐项复核原 52 个 Integrate。
复核结论：Candidate/Evidence 通过；Books 为 23 Integrated / 0 queued / 77 Existing；相较复核前降级 29 项；ordinary pending=0。
写后复核者：june_15_16_postwrite（fresh context）；5/5 新增正文通过唯一锚点、正文边界、机制链、证据边界与相邻语义检查。记录：`../_sources/daily-20260616/v3-independent-post-write-audit-20260911.json`。
结论：通过
