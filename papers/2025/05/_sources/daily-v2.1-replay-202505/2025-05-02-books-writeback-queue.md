# 2025-05-02 Books Writeback Queue

本文件保留五项写回要求与完成收据。root 已按事件时间串行写回；独立 fresh-context reviewer 已重读 owner 与相邻章节，五项均通过，无待写回条目。

## SF-2025-AVA

- Owner: `AGENT-RAG`
- Target: `books/part-07-agent/76-rag.md`
- Adjacent: `books/part-07-agent/75-context.md; books/part-07-agent/77-memory.md`
- Suggested anchor: RAG 已有 chunk/index/provenance，但缺少持续视频流如何变成可修订事件图的完整路径。
- Long-term proposition: 长视频 RAG 要先把连续观察压缩为带时间和来源的可修订事件图，再让 agent 在不同视图间检索；短视频直接 VLM 仍是低复杂度分支。
- Evidence boundary: 作者以 3 秒片段生成描述并做语义合并，构造事件/实体/时间图，再用多视图检索、MCTS 与 self-consistency 回答。AVA-100 只覆盖八段长视频和 120 个问题；描述误差、图陈旧与搜索成本会累积，不能外推为通用实时视频理解。
- Exact primary: https://arxiv.org/html/2505.00254v1

## SF-2025-LLMPRISM

- Owner: `PLATFORM-MONITORING`
- Target: `books/part-06-ai-infrastructure/67-monitoring.md`
- Adjacent: `books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-06-ai-infrastructure/68-logging.md`
- Suggested anchor: Monitoring 已有 metrics/logs/traces 与 collective telemetry，但缺少无法植入代码时的网络流序列诊断分支。
- Long-term proposition: 当训练框架不可插桩时，网络流序列可提供 job/parallelism/phase 的旁路传感；共享流量、加密、拓扑和框架漂移会使它失效，必须回退显式 instrumentation。
- Evidence boundary: 论文从交换机/host 网络流推断训练任务、并行策略与阶段，并报告自 2024-10 的生产部署经验。作者的识别率和时间线误差只属于其平台与流量合同；旁路传感无法证明模型正确，也可能被共享流量或版本漂移混淆。
- Exact primary: https://arxiv.org/html/2505.00342v1

## SF-2025-SOLO

- Owner: `TRAIN-PRETRAINING`
- Target: `books/part-04-training-system/28-pretraining.md`
- Adjacent: `books/part-04-training-system/27-data.md; books/part-04-training-system/29-sft.md`
- Suggested anchor: Pretraining 已有 low-precision update、error feedback 与 role-aware optimizer state，但没有解释 EMA dynamics 的两种量化失真。
- Long-term proposition: 低比特 optimizer 的风险不只是静态误差：unsigned EMA 会淹没新信号，signed state 会放大方差或方向错误；状态演化决定是否还能学习。
- Evidence boundary: 作者用 log quantization 与 precision-specific momentum 处理 2-bit 级 Adam state，并在受限模型/训练设置比较。证据不覆盖所有 optimizer、分布式 checkpoint、故障恢复或数值格式；高精度 state 在小规模或不稳定训练中仍是基线。
- Exact primary: https://arxiv.org/html/2505.00347v1

## SF-2025-DISTRIBUTED-RAG

- Owner: `AGENT-RAG`
- Target: `books/part-07-agent/76-rag.md`
- Adjacent: `books/part-07-agent/75-context.md; books/part-07-agent/77-memory.md`
- Suggested anchor: RAG 主要以中央索引为默认，已讨论 partition 和 federation，但缺少 peer-owned knowledge 的完整控制边界。
- Long-term proposition: 分布式 RAG 将 corpus ownership 留在 peer，并以 topic-aware discovery 代替中央索引；它减少集中收集，却不会自动提供 query privacy、信任或一致性。
- Evidence boundary: 作者在仿真网络比较 topic-aware random walk 与 flooding/centralized baselines，并报告接近中央检索、消息更少。证据不覆盖对抗 peer、真实网络故障、隐私证明或生产尾延迟；稳定可审计 corpus 仍适合中央 RAG。
- Exact primary: https://arxiv.org/html/2505.00443v1

## SF-2025-SPILL-BEANS

- Owner: `PLATFORM-SECURITY`
- Target: `books/part-06-ai-infrastructure/72-security.md`
- Adjacent: `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`
- Suggested anchor: Security 已覆盖 tenant isolation、model/data side channels，但缺少 token embedding access 可经共享 CPU cache 泄露的明确 control boundary。
- Long-term proposition: 即便 API 不返回 logits，共享 CPU cache 与 embedding access 仍可能泄露 token；防御必须进入 co-location、page sharing 和 cache isolation，而不只是输出过滤。
- Evidence boundary: 作者在特定 co-location 与监控 token set 下恢复 API key/英文 token，headline rate 受可监控集合、CPU/cache 与部署布局约束。它不证明任意云、多租户或模型都可被同样攻击，但足以扩展平台 threat model。
- Exact primary: https://arxiv.org/html/2505.00817v1
