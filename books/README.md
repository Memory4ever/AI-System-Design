# 《AI System：从第一性原理到 AI 基建》

这不是一组按产品或论文分类的笔记，而是一条从模型能力到生产系统的推导路线。推荐先按七个 Part 顺读，建立主干；完成顺读后，再沿 Compute、Memory、Communication、Scheduling、State 五条横轴回读。

## 全书主线

```text
为什么需要 AI System
→ 一个 token 如何变成答案
→ 表示怎样跨越模态并进入环境与行动
→ 数据和优化怎样生产能力
→ 能力怎样在延迟、显存与 SLO 下交付
→ 组织怎样复用、评估和治理能力
→ 模型怎样在状态、权限与环境反馈中完成任务
```

| Part | 核心问题 | 进入时已有认知 | 退出时获得的系统能力 |
| --- | --- | --- | --- |
| [Part I 世界观](part-01-worldview/README.md) | AI 为什么演化成今天的系统形态？ | 软件与分布式系统经验 | 用约束、状态和控制闭环分析 AI System |
| [Part II 模型基础](part-02-model/README.md) | 一个 token 如何变成答案？ | 学习、表示与 Scaling 的宏观认识 | 从离散输入推导 Transformer 输出与容量边界 |
| [Part III 多模态、生成与世界模型](part-03-multimodal-world-models/README.md) | 表示如何进入环境预测与物理行动？ | 文本模型的组件与状态 | 建立 modality、generation、world state 与 action contract |
| [Part IV Training System](part-04-training-system/README.md) | 数据、目标与分布式执行如何生产能力？ | 模型和多模态语义 | 形成从数据到可交付模型资产的生产链 |
| [Part V Inference System](part-05-inference-system/README.md) | 模型能力如何在系统约束下交付？ | 可验证模型资产 | 建立 request、token、KV、runtime 与 SLO 的交付链 |
| [Part VI AI Infrastructure](part-06-ai-infrastructure/README.md) | 多团队如何复用、评估和治理 AI 能力？ | Training 与 Inference 控制对象 | 建立统一 identity、policy、evidence 与 feedback 闭环 |
| [Part VII Agent](part-07-agent/README.md) | 模型如何在状态、权限与环境反馈中完成任务？ | 受治理的模型和平台能力 | 建立从 Context 到 Action 的可恢复执行系统 |

## 章节索引

### Part I 世界观

[Ch1 为什么学习 AI System](part-01-worldview/01-why-learn-ai-system.md) · [Ch2 AI 的发展历史](part-01-worldview/02-ai-history.md) · [Ch3 AI System 全局知识树](part-01-worldview/03-global-knowledge-tree.md) · [Ch4 模型为什么能够学习](part-01-worldview/04-why-models-learn.md) · [Ch5 神经网络到底学到了什么](part-01-worldview/05-what-neural-networks-learn.md) · [Ch6 Transformer 为什么改变世界](part-01-worldview/06-why-transformer-changed-the-world.md) · [Ch7 Scaling Law 为什么成立](part-01-worldview/07-scaling-law.md) · [Ch8 大模型为什么会产生智能](part-01-worldview/08-why-llms-show-intelligence.md) · [Ch9 AI System 的演化路线](part-01-worldview/09-ai-system-evolution.md) · [Ch10 AI 的未来](part-01-worldview/10-future-of-ai.md)

### Part II 模型基础

[Ch11 Tokenizer](part-02-model/11-tokenizer.md) · [Ch12 Embedding](part-02-model/12-embedding.md) · [Ch13 Position Encoding](part-02-model/13-position-encoding.md) · [Ch14 Self Attention](part-02-model/14-self-attention.md) · [Ch15 Multi-Head Attention](part-02-model/15-multi-head-attention.md) · [Ch16 Feed Forward / MLP](part-02-model/16-feed-forward-mlp.md) · [Ch17 Transformer Layer](part-02-model/17-transformer-layer.md) · [Ch18 Decoder Only](part-02-model/18-decoder-only.md) · [Ch19 KV Cache](part-02-model/19-kv-cache.md) · [Ch20 Sampling](part-02-model/20-sampling.md) · [Ch21 MoE](part-02-model/21-moe.md) · [Ch22 Long Context](part-02-model/22-long-context.md)

### Part III 多模态、生成与世界模型

[Ch23 多模态表示与融合](part-03-multimodal-world-models/23-multimodal-representation.md) · [Ch24 多模态生成范式](part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) · [Ch25 World Models](part-03-multimodal-world-models/25-multimodal-world-models.md) · [Ch26 Embodied AI 与 VLA](part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

### Part IV Training System

[Ch27 数据](part-04-training-system/27-data.md) · [Ch28 Pretraining](part-04-training-system/28-pretraining.md) · [Ch29 SFT](part-04-training-system/29-sft.md) · [Ch30 LoRA](part-04-training-system/30-lora.md) · [Ch31 RLHF](part-04-training-system/31-rlhf.md) · [Ch32 PPO](part-04-training-system/32-ppo.md) · [Ch33 GRPO 与 Trajectory Lifecycle](part-04-training-system/33-grpo.md) · [Ch34 DPO](part-04-training-system/34-dpo.md) · [Ch35 Checkpoint](part-04-training-system/35-checkpoint.md) · [Ch36 Distributed Training](part-04-training-system/36-distributed-training.md) · [Ch37 Tensor Parallel](part-04-training-system/37-tensor-parallel.md) · [Ch38 Pipeline Parallel](part-04-training-system/38-pipeline-parallel.md) · [Ch39 ZeRO](part-04-training-system/39-zero.md) · [Ch40 Megatron](part-04-training-system/40-megatron.md) · [Ch41 DeepSpeed](part-04-training-system/41-deepspeed.md)

### Part V Inference System

[Ch42 推理到底发生了什么](part-05-inference-system/42-what-happens-during-inference.md) · [Ch43 Prefill](part-05-inference-system/43-prefill.md) · [Ch44 Decode](part-05-inference-system/44-decode.md) · [Ch45 为什么 KV Cache 能提速](part-05-inference-system/45-why-kv-cache-speeds-up.md) · [Ch46 Continuous Batching](part-05-inference-system/46-continuous-batching.md) · [Ch47 PagedAttention](part-05-inference-system/47-pagedattention.md) · [Ch48 Speculative Decoding](part-05-inference-system/48-speculative-decoding.md) · [Ch49 高性能 GPU 推理执行](part-05-inference-system/49-tensorrt-llm.md) · [Ch50 LLM Serving Engine](part-05-inference-system/50-vllm.md) · [Ch51 结构化生成 Runtime](part-05-inference-system/51-sglang.md) · [Ch52 分布式推理 Runtime](part-05-inference-system/52-dynamo.md) · [Ch53 LLM Serving 声明式拓扑](part-05-inference-system/53-kserve-llm.md) · [Ch54 GPU Memory](part-05-inference-system/54-gpu-memory.md) · [Ch55 PD 分离](part-05-inference-system/55-pd-disaggregation.md) · [Ch56 推理调度](part-05-inference-system/56-inference-scheduling.md)

### Part VI AI Infrastructure

[Ch57 什么是 AI Platform](part-06-ai-infrastructure/57-what-is-ai-platform.md) · [Ch58 组合式 ML Platform](part-06-ai-infrastructure/58-kubeflow.md) · [Ch59 Model Registry](part-06-ai-infrastructure/59-model-registry.md) · [Ch60 Training Operator](part-06-ai-infrastructure/60-training-operator.md) · [Ch61 模型服务声明式控制面](part-06-ai-infrastructure/61-kserve.md) · [Ch62 Gateway](part-06-ai-infrastructure/62-gateway.md) · [Ch63 GPU Scheduler](part-06-ai-infrastructure/63-gpu-scheduler.md) · [Ch64 Gang 与队列调度](part-06-ai-infrastructure/64-volcano.md) · [Ch65 AI 集群公平共享与 GPU 调度](part-06-ai-infrastructure/65-kai-scheduler.md) · [Ch66 Evaluation System](part-06-ai-infrastructure/66-evaluation-system.md) · [Ch67 Monitoring](part-06-ai-infrastructure/67-monitoring.md) · [Ch68 Logging](part-06-ai-infrastructure/68-logging.md) · [Ch69 Trace](part-06-ai-infrastructure/69-trace.md) · [Ch70 Cost](part-06-ai-infrastructure/70-cost.md) · [Ch71 Multi Tenant](part-06-ai-infrastructure/71-multi-tenant.md) · [Ch72 Security](part-06-ai-infrastructure/72-security.md) · [Ch73 Production Best Practice](part-06-ai-infrastructure/73-production-best-practice.md)

### Part VII Agent

[Ch74 Prompt](part-07-agent/74-prompt.md) · [Ch75 Context](part-07-agent/75-context.md) · [Ch76 RAG](part-07-agent/76-rag.md) · [Ch77 Memory](part-07-agent/77-memory.md) · [Ch78 Tool Calling](part-07-agent/78-tool-calling.md) · [Ch79 Planning](part-07-agent/79-planning.md) · [Ch80 Reflection](part-07-agent/80-reflection.md) · [Ch81 Workflow](part-07-agent/81-workflow.md) · [Ch82 Multi-Agent](part-07-agent/82-multi-agent.md) · [Ch83 MCP](part-07-agent/83-mcp.md) · [Ch84 Agent Platform](part-07-agent/84-agent-platform.md)

## 五条横轴回读

- **Compute**：[Ch6](part-01-worldview/06-why-transformer-changed-the-world.md) → [Ch14](part-02-model/14-self-attention.md) / [Ch17](part-02-model/17-transformer-layer.md) → [Ch24](part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) → [Ch28](part-04-training-system/28-pretraining.md) / [Ch37](part-04-training-system/37-tensor-parallel.md) → [Ch49](part-05-inference-system/49-tensorrt-llm.md) → [Ch54](part-05-inference-system/54-gpu-memory.md) / [Ch63](part-06-ai-infrastructure/63-gpu-scheduler.md)，追踪模型算子如何映射到训练、推理和集群硬件。
- **Memory**：[Ch19](part-02-model/19-kv-cache.md) / [Ch22](part-02-model/22-long-context.md) → [Ch23](part-03-multimodal-world-models/23-multimodal-representation.md) / [Ch25](part-03-multimodal-world-models/25-multimodal-world-models.md) → [Ch35](part-04-training-system/35-checkpoint.md) / [Ch39](part-04-training-system/39-zero.md) → [Ch45](part-05-inference-system/45-why-kv-cache-speeds-up.md) / [Ch47](part-05-inference-system/47-pagedattention.md) / [Ch52](part-05-inference-system/52-dynamo.md) / [Ch54](part-05-inference-system/54-gpu-memory.md) / [Ch55](part-05-inference-system/55-pd-disaggregation.md) → [Ch75](part-07-agent/75-context.md) / [Ch77](part-07-agent/77-memory.md)，比较 activation、checkpoint、KV、Context 与 Agent Memory 的生命周期和 truth authority。
- **Communication**：[Ch9](part-01-worldview/09-ai-system-evolution.md) / [Ch21](part-02-model/21-moe.md) / [Ch22](part-02-model/22-long-context.md) → [Ch23](part-03-multimodal-world-models/23-multimodal-representation.md) / [Ch26](part-03-multimodal-world-models/26-multimodal-embodied-vla.md) → [Ch36～40](part-04-training-system/36-distributed-training.md) → [Ch52](part-05-inference-system/52-dynamo.md) / [Ch55](part-05-inference-system/55-pd-disaggregation.md) → [Ch63](part-06-ai-infrastructure/63-gpu-scheduler.md) → [Ch82](part-07-agent/82-multi-agent.md) / [Ch83](part-07-agent/83-mcp.md)，区分 collective、KV transfer、协议和 Agent handoff 所交换的状态。
- **Scheduling**：[Ch24](part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) / [Ch26](part-03-multimodal-world-models/26-multimodal-embodied-vla.md) → [Ch38](part-04-training-system/38-pipeline-parallel.md) → [Ch46](part-05-inference-system/46-continuous-batching.md) / [Ch52](part-05-inference-system/52-dynamo.md) / [Ch53](part-05-inference-system/53-kserve-llm.md) / [Ch56](part-05-inference-system/56-inference-scheduling.md) → [Ch63～65](part-06-ai-infrastructure/63-gpu-scheduler.md) → [Ch81](part-07-agent/81-workflow.md) / [Ch84](part-07-agent/84-agent-platform.md)，比较谁在不同时间尺度分配下一次执行机会。
- **State**：[Ch19](part-02-model/19-kv-cache.md) → [Ch23](part-03-multimodal-world-models/23-multimodal-representation.md) / [Ch25](part-03-multimodal-world-models/25-multimodal-world-models.md) / [Ch26](part-03-multimodal-world-models/26-multimodal-embodied-vla.md) → [Ch35](part-04-training-system/35-checkpoint.md) → [Ch42](part-05-inference-system/42-what-happens-during-inference.md) / [Ch45](part-05-inference-system/45-why-kv-cache-speeds-up.md) / [Ch52](part-05-inference-system/52-dynamo.md) / [Ch55](part-05-inference-system/55-pd-disaggregation.md) → [Ch59](part-06-ai-infrastructure/59-model-registry.md) → [Ch75](part-07-agent/75-context.md) / [Ch77](part-07-agent/77-memory.md) / [Ch81](part-07-agent/81-workflow.md) / [Ch84](part-07-agent/84-agent-platform.md)，追踪 identity、ownership、freshness、commit、rollback 与 evidence。

横轴表达 Principle Reuse 或 Layering 时，不应被误写为直接历史继承。具体节点映射和历史章节号以 [ROADMAP](../ROADMAP.md) 为准。

## 代表性演进链

- **Dense → Conditional Compute**：[Ch16 MLP](part-02-model/16-feed-forward-mlp.md) → [Ch21 MoE](part-02-model/21-moe.md) → [Ch36/37 Distributed Training](part-04-training-system/36-distributed-training.md) → [Ch49/54/56 Execution、Memory 与 Scheduling](part-05-inference-system/49-tensorrt-llm.md)。这是从每 token 激活全部参数到受路由约束的容量扩展，再到通信、放置和 SLO 的 `Layering / Dependency`，不是简单替代。
- **Base Capability → Post-training Branches**：[Ch28 Pretraining](part-04-training-system/28-pretraining.md) → [Ch29 SFT](part-04-training-system/29-sft.md) → [Ch31 RLHF](part-04-training-system/31-rlhf.md) → [Ch32 PPO](part-04-training-system/32-ppo.md) / [Ch33 GRPO](part-04-training-system/33-grpo.md) / [Ch34 DPO](part-04-training-system/34-dpo.md)。三条分支消费不同监督对象并承担不同 online/offline、value、trajectory 与 reference-state 成本。
- **Request → Distributed Scheduling**：[Ch42/44 Request 与 Decode](part-05-inference-system/42-what-happens-during-inference.md) → [Ch46 Continuous Batching](part-05-inference-system/46-continuous-batching.md) → [Ch47 PagedAttention](part-05-inference-system/47-pagedattention.md) → [Ch48 Speculative Decoding](part-05-inference-system/48-speculative-decoding.md) → [Ch52/56 Distributed Runtime 与 Scheduling](part-05-inference-system/52-dynamo.md)。每一步提高共享或并行机会，同时新增 fairness、block ownership、rollback、freshness 和 recovery 状态。
- **Observation → Release Gate**：[Ch66 Claim/Eval Contract](part-06-ai-infrastructure/66-evaluation-system.md) → [Ch67～69 Metrics、Logs、Traces](part-06-ai-infrastructure/67-monitoring.md) → [Ch66 Measurement/Decision](part-06-ai-infrastructure/66-evaluation-system.md) → [Ch73 Production Gate](part-06-ai-infrastructure/73-production-best-practice.md)。这是 evidence feedback loop，不是按章节号单向流动。
- **Information → Governed Action**：[Ch75 Context](part-07-agent/75-context.md) → [Ch76 RAG](part-07-agent/76-rag.md) → [Ch77 Memory](part-07-agent/77-memory.md) → [Ch78 Tool](part-07-agent/78-tool-calling.md) → [Ch81 Workflow](part-07-agent/81-workflow.md) → [Ch82 Multi-Agent](part-07-agent/82-multi-agent.md)。状态从 per-call working set 扩展到 persisted evidence、typed action、durable commit 和 bounded delegation，authority 随之收紧而不是自治单向增强。
