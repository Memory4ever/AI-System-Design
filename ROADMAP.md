<!--
This file is the Single Source of Truth for the AI System knowledge tree.
Stable Knowledge Node ID is the durable identity. Chapter number is reading order.
-->

# AI System：从第一性原理到 AI 基建

**版本：** v0.2（七 Part / 84 章）

**目标读者：** 已具备软件工程、分布式系统、Kubernetes 或平台工程经验，正在建设 Data / Training → Model → Deployment → Serving → Observability 全链路的工程师。

**写作原则：** 先解释问题为何存在、旧方案为何合理、约束如何变化，再解释机制、证据边界、trade-off、共存条件和下一阶段压力。框架、论文和版本只用于验证长期机制。

## 核心学习路径

```text
世界观
→ 模型基础
→ 多模态表示、生成、世界模型与物理行动
→ Training System
→ Inference System
→ AI Infrastructure
→ Agent
```

## 全书结构总览

| Part | 章节 | 核心问题 |
| --- | --- | --- |
| Part I 世界观 | Ch1～10 | AI 为什么演化成今天的系统形态？ |
| Part II 模型基础 | Ch11～22 | 一个 token 如何变成答案？ |
| Part III 多模态、生成与世界模型 | Ch23～26 | 表示如何跨越模态，并最终进入可修正的环境预测与物理行动？ |
| Part IV Training System | Ch27～41 | 数据、目标与分布式执行如何生产可交付能力？ |
| Part V Inference System | Ch42～56 | 模型能力如何在 memory、latency、throughput 与 SLO 下交付？ |
| Part VI AI Infrastructure | Ch57～73 | 多团队如何复用、评估和治理 AI 能力？ |
| Part VII Agent | Ch74～84 | 模型如何在状态、权限与环境反馈中完成任务？ |

## Stable Knowledge Node ID

章节号表达当前阅读顺序；Stable Knowledge Node ID 表达长期知识所有权。章节插入、移动或重编号时，Node ID 不变。历史 Weekly 中的旧章节号仍按当时语义解释，不进行机械重写。

新研究记录统一写：

```text
Owner: INFER-SPECULATIVE-DECODING
Current chapter: Ch48
Legacy chapter: Ch44
```

### 节点映射表

| Stable Node ID | Current | Current path | Legacy |
| --- | ---: | --- | ---: |
| `WORLDVIEW-WHY-AI-SYSTEM` | Ch1 | `books/part-01-worldview/01-why-learn-ai-system.md` | Ch1 |
| `WORLDVIEW-AI-HISTORY` | Ch2 | `books/part-01-worldview/02-ai-history.md` | Ch2 |
| `WORLDVIEW-KNOWLEDGE-TREE` | Ch3 | `books/part-01-worldview/03-global-knowledge-tree.md` | Ch3 |
| `WORLDVIEW-WHY-MODELS-LEARN` | Ch4 | `books/part-01-worldview/04-why-models-learn.md` | Ch4 |
| `WORLDVIEW-REPRESENTATION` | Ch5 | `books/part-01-worldview/05-what-neural-networks-learn.md` | Ch5 |
| `WORLDVIEW-TRANSFORMER` | Ch6 | `books/part-01-worldview/06-why-transformer-changed-the-world.md` | Ch6 |
| `WORLDVIEW-SCALING-LAW` | Ch7 | `books/part-01-worldview/07-scaling-law.md` | Ch7 |
| `WORLDVIEW-LLM-INTELLIGENCE` | Ch8 | `books/part-01-worldview/08-why-llms-show-intelligence.md` | Ch8 |
| `WORLDVIEW-SYSTEM-EVOLUTION` | Ch9 | `books/part-01-worldview/09-ai-system-evolution.md` | Ch9 |
| `WORLDVIEW-FUTURE` | Ch10 | `books/part-01-worldview/10-future-of-ai.md` | Ch10 |
| `MODEL-TOKENIZER` | Ch11 | `books/part-02-model/11-tokenizer.md` | Ch11 |
| `MODEL-EMBEDDING` | Ch12 | `books/part-02-model/12-embedding.md` | Ch12 |
| `MODEL-POSITION-ENCODING` | Ch13 | `books/part-02-model/13-position-encoding.md` | Ch13 |
| `MODEL-SELF-ATTENTION` | Ch14 | `books/part-02-model/14-self-attention.md` | Ch14 |
| `MODEL-MULTI-HEAD-ATTENTION` | Ch15 | `books/part-02-model/15-multi-head-attention.md` | Ch15 |
| `MODEL-FFN` | Ch16 | `books/part-02-model/16-feed-forward-mlp.md` | Ch16 |
| `MODEL-TRANSFORMER-LAYER` | Ch17 | `books/part-02-model/17-transformer-layer.md` | Ch17 |
| `MODEL-DECODER-ONLY` | Ch18 | `books/part-02-model/18-decoder-only.md` | Ch18 |
| `MODEL-KV-CACHE` | Ch19 | `books/part-02-model/19-kv-cache.md` | Ch19 |
| `MODEL-SAMPLING` | Ch20 | `books/part-02-model/20-sampling.md` | Ch20 |
| `MODEL-MOE` | Ch21 | `books/part-02-model/21-moe.md` | Ch21 |
| `MODEL-LONG-CONTEXT` | Ch22 | `books/part-02-model/22-long-context.md` | Ch22 |
| `MULTIMODAL-REPRESENTATION` | Ch23 | `books/part-03-multimodal-world-models/23-multimodal-representation.md` | N/A |
| `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 | `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` | N/A |
| `MULTIMODAL-WORLD-MODELS` | Ch25 | `books/part-03-multimodal-world-models/25-multimodal-world-models.md` | N/A |
| `MULTIMODAL-EMBODIED-VLA` | Ch26 | `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` | N/A |
| `TRAIN-DATA` | Ch27 | `books/part-04-training-system/27-data.md` | Ch23 |
| `TRAIN-PRETRAINING` | Ch28 | `books/part-04-training-system/28-pretraining.md` | Ch24 |
| `TRAIN-SFT` | Ch29 | `books/part-04-training-system/29-sft.md` | Ch25 |
| `TRAIN-LORA` | Ch30 | `books/part-04-training-system/30-lora.md` | Ch26 |
| `TRAIN-RLHF` | Ch31 | `books/part-04-training-system/31-rlhf.md` | Ch27 |
| `TRAIN-PPO` | Ch32 | `books/part-04-training-system/32-ppo.md` | Ch28 |
| `TRAIN-GRPO` | Ch33 | `books/part-04-training-system/33-grpo.md` | Ch29 |
| `TRAIN-DPO` | Ch34 | `books/part-04-training-system/34-dpo.md` | Ch30 |
| `TRAIN-CHECKPOINT` | Ch35 | `books/part-04-training-system/35-checkpoint.md` | Ch31 |
| `TRAIN-DISTRIBUTED-TRAINING` | Ch36 | `books/part-04-training-system/36-distributed-training.md` | Ch32 |
| `TRAIN-TENSOR-PARALLEL` | Ch37 | `books/part-04-training-system/37-tensor-parallel.md` | Ch33 |
| `TRAIN-PIPELINE-PARALLEL` | Ch38 | `books/part-04-training-system/38-pipeline-parallel.md` | Ch34 |
| `TRAIN-ZERO` | Ch39 | `books/part-04-training-system/39-zero.md` | Ch35 |
| `TRAIN-MEGATRON` | Ch40 | `books/part-04-training-system/40-megatron.md` | Ch36 |
| `TRAIN-DEEPSPEED` | Ch41 | `books/part-04-training-system/41-deepspeed.md` | Ch37 |
| `INFER-REQUEST-LIFECYCLE` | Ch42 | `books/part-05-inference-system/42-what-happens-during-inference.md` | Ch38 |
| `INFER-PREFILL` | Ch43 | `books/part-05-inference-system/43-prefill.md` | Ch39 |
| `INFER-DECODE` | Ch44 | `books/part-05-inference-system/44-decode.md` | Ch40 |
| `INFER-KV-CACHE` | Ch45 | `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` | Ch41 |
| `INFER-CONTINUOUS-BATCHING` | Ch46 | `books/part-05-inference-system/46-continuous-batching.md` | Ch42 |
| `INFER-PAGED-ATTENTION` | Ch47 | `books/part-05-inference-system/47-pagedattention.md` | Ch43 |
| `INFER-SPECULATIVE-DECODING` | Ch48 | `books/part-05-inference-system/48-speculative-decoding.md` | Ch44 |
| `INFER-TENSORRT-LLM` | Ch49 | `books/part-05-inference-system/49-tensorrt-llm.md` | Ch45 |
| `INFER-VLLM` | Ch50 | `books/part-05-inference-system/50-vllm.md` | Ch46 |
| `INFER-SGLANG` | Ch51 | `books/part-05-inference-system/51-sglang.md` | Ch47 |
| `INFER-DYNAMO` | Ch52 | `books/part-05-inference-system/52-dynamo.md` | Ch48 |
| `INFER-KSERVE-TOPOLOGY` | Ch53 | `books/part-05-inference-system/53-kserve-llm.md` | Ch49 |
| `INFER-GPU-MEMORY` | Ch54 | `books/part-05-inference-system/54-gpu-memory.md` | Ch50 |
| `INFER-PD-DISAGGREGATION` | Ch55 | `books/part-05-inference-system/55-pd-disaggregation.md` | Ch51 |
| `INFER-SCHEDULING` | Ch56 | `books/part-05-inference-system/56-inference-scheduling.md` | Ch52 |
| `PLATFORM-FOUNDATIONS` | Ch57 | `books/part-06-ai-infrastructure/57-what-is-ai-platform.md` | Ch53 |
| `PLATFORM-KUBEFLOW` | Ch58 | `books/part-06-ai-infrastructure/58-kubeflow.md` | Ch54 |
| `PLATFORM-MODEL-REGISTRY` | Ch59 | `books/part-06-ai-infrastructure/59-model-registry.md` | Ch55 |
| `PLATFORM-TRAINING-OPERATOR` | Ch60 | `books/part-06-ai-infrastructure/60-training-operator.md` | Ch56 |
| `PLATFORM-KSERVE` | Ch61 | `books/part-06-ai-infrastructure/61-kserve.md` | Ch57 |
| `PLATFORM-GATEWAY` | Ch62 | `books/part-06-ai-infrastructure/62-gateway.md` | Ch58 |
| `PLATFORM-GPU-SCHEDULER` | Ch63 | `books/part-06-ai-infrastructure/63-gpu-scheduler.md` | Ch59 |
| `PLATFORM-VOLCANO` | Ch64 | `books/part-06-ai-infrastructure/64-volcano.md` | Ch60 |
| `PLATFORM-KAI-SCHEDULER` | Ch65 | `books/part-06-ai-infrastructure/65-kai-scheduler.md` | Ch61 |
| `PLATFORM-EVALUATION-SYSTEM` | Ch66 | `books/part-06-ai-infrastructure/66-evaluation-system.md` | Ch62 |
| `PLATFORM-MONITORING` | Ch67 | `books/part-06-ai-infrastructure/67-monitoring.md` | Ch63 |
| `PLATFORM-LOGGING` | Ch68 | `books/part-06-ai-infrastructure/68-logging.md` | Ch64 |
| `PLATFORM-TRACE` | Ch69 | `books/part-06-ai-infrastructure/69-trace.md` | Ch65 |
| `PLATFORM-COST` | Ch70 | `books/part-06-ai-infrastructure/70-cost.md` | Ch66 |
| `PLATFORM-MULTI-TENANT` | Ch71 | `books/part-06-ai-infrastructure/71-multi-tenant.md` | Ch67 |
| `PLATFORM-SECURITY` | Ch72 | `books/part-06-ai-infrastructure/72-security.md` | Ch68 |
| `PLATFORM-PRODUCTION` | Ch73 | `books/part-06-ai-infrastructure/73-production-best-practice.md` | Ch69 |
| `AGENT-PROMPT` | Ch74 | `books/part-07-agent/74-prompt.md` | Ch70 |
| `AGENT-CONTEXT` | Ch75 | `books/part-07-agent/75-context.md` | Ch71 |
| `AGENT-RAG` | Ch76 | `books/part-07-agent/76-rag.md` | Ch72 |
| `AGENT-MEMORY` | Ch77 | `books/part-07-agent/77-memory.md` | Ch73 |
| `AGENT-TOOL-CALLING` | Ch78 | `books/part-07-agent/78-tool-calling.md` | Ch74 |
| `AGENT-PLANNING` | Ch79 | `books/part-07-agent/79-planning.md` | Ch75 |
| `AGENT-REFLECTION` | Ch80 | `books/part-07-agent/80-reflection.md` | Ch76 |
| `AGENT-WORKFLOW` | Ch81 | `books/part-07-agent/81-workflow.md` | Ch77 |
| `AGENT-MULTI-AGENT` | Ch82 | `books/part-07-agent/82-multi-agent.md` | Ch78 |
| `AGENT-MCP` | Ch83 | `books/part-07-agent/83-mcp.md` | Ch79 |
| `AGENT-PLATFORM` | Ch84 | `books/part-07-agent/84-agent-platform.md` | Ch80 |

## 七个 Part 的章节规划

### Part I 世界观（Ch1～10）

建立学习问题、历史、知识树、学习与表示、Transformer、Scaling、能力、系统演化和未来约束。Ch10 只做情景入口；多模态、World Model 与 Embodied 的机制归 Part III。

### Part II 模型基础（Ch11～22）

沿 Tokenizer → Embedding → Position → Attention → MLP → Layer → Decoder Only → KV Cache → Sampling 展开，再以 MoE 和 Long Context 描述参数容量与序列容量。这里拥有通用模型组件，不拥有跨模态 codec、生成范式或物理控制。

### Part III 多模态、生成与世界模型（Ch23～26）

- **Ch23 多模态表示与融合**：raw signal 如何变成带 modality、time 和 provenance identity 的可学习表示。
- **Ch24 多模态生成范式**：AR、Diffusion、Masked/Block Diffusion 如何在 factorization、并行、cache、修正与 commit 之间取舍。
- **Ch25 World Models**：从 observation generation 演进到 action-conditioned transition、latent dynamics、imagined rollout 与 persistent world state。
- **Ch26 Embodied AI 与 VLA**：感知、语言条件动作、trajectory/action chunk、low-level controller、真实环境反馈和 safety envelope 如何闭环。

### Part IV Training System（Ch27～41）

Ch27～34 拥有数据、pretraining、SFT/LoRA 与 preference optimization；Ch35～41 拥有 checkpoint、collective、TP、PP、ZeRO 与训练 runtime。多模态数据配比和训练 objective 在这里实现，但表示/生成/world/action 语义仍由 Part III 定义。

### Part V Inference System（Ch42～56）

Ch42～48 从 request lifecycle、Prefill/Decode、KV、batching、paging、speculation 建立单 engine 机制；Ch49～53 映射 execution plan、serving engine、structured runtime、distributed state 与 topology；Ch54～56收束 HBM、PD 和 SLO scheduling。

### Part VI AI Infrastructure（Ch57～73）

平台以 control/data/evidence planes 统一 asset、workload、serving、gateway、typed resources、evaluation、observability、cost、tenancy、security 与 production readiness。AI for Science 是跨 Data → Evaluation → Workflow → Security 的领域路线，不建立独立 Part。

### Part VII Agent（Ch74～84）

从 Prompt、Context、RAG、derived Memory 到 Tool、Planning、Reflection、Workflow、Multi-Agent、MCP 和 Agent Platform。Agent memory 不拥有 environment dynamics；Agent planning 可以消费 World Model，但不把预测状态当作事实状态。

## 双轴知识树

七个 Part 是阅读和 owner 主干；五条横轴用于复核跨层系统原语，而不替代 owner：

| 横轴 | 主要路径 |
| --- | --- |
| Compute | Ch6 → Ch14/17 → Ch24 → Ch28/37 → Ch49 → Ch54/63 |
| Memory | Ch19/22 → Ch23/25 → Ch35/39 → Ch45/47/52/54/55 → Ch75/77 |
| Communication | Ch9/21/22 → Ch23/26 → Ch36～40 → Ch52/55 → Ch63 → Ch82/83 |
| Scheduling | Ch24/26 → Ch38 → Ch46/52/53/56 → Ch63～65 → Ch81/84 |
| State | Ch19 → Ch23/25/26 → Ch35 → Ch42/45/52/55 → Ch59 → Ch75/77/81/84 |

历史关系必须标记为 `Direct Evolution`、`Layering / Dependency`、`Principle Reuse` 或 `Explanatory Analogy`。后发技术不得静默覆盖旧方案。

## 跨领域阅读路线

### Compiler / Kernel / Hardware Co-design

```text
MODEL-FFN / MODEL-MOE
→ TRAIN-DISTRIBUTED-TRAINING
→ INFER-TENSORRT-LLM
→ INFER-GPU-MEMORY
→ PLATFORM-GPU-SCHEDULER
```

### AI for Science

```text
TRAIN-DATA
→ PLATFORM-EVALUATION-SYSTEM
→ AGENT-WORKFLOW
→ PLATFORM-SECURITY
```

### Edge / On-device AI

```text
WORLDVIEW-FUTURE
→ MULTIMODAL-REPRESENTATION / MULTIMODAL-EMBODIED-VLA
→ INFER-TENSORRT-LLM
→ PLATFORM-GPU-SCHEDULER
```

## 建议学习顺序

先顺读七个 Part 建立主干，再沿五条横轴回读。框架章节不是产品手册：先读相邻机制章，再把框架放回 owner 边界。遇到新论文，先定位 Stable Node ID；若现有节点无法承载，再提出 Structural Candidate，而不是把 Ch10、Ch49、Ch66 或 Ch84 当作杂物篮子。
