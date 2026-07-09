![img.png](img.png)
AI System Design

From First Principles to AI Infrastructure

一套持续演进的 AI System 学习体系。

不是从框架开始，也不是从 API 开始。

而是从一个更根本的问题开始：

为什么今天的 AI System 会设计成这样？

它解决了什么问题？经历了哪些失败？做出了哪些权衡？

如果未来模型、硬件和业务约束改变，它还会是最优解吗？

⸻

Why This Repository?

学习 AI 最容易陷入一种状态：

今天学习 Transformer。

明天学习 LoRA。

后天学习 vLLM。

然后又出现：

* SGLang
* KServe
* Dynamo
* DeepSpeed
* Megatron
* RLHF
* GRPO
* RAG
* Agent
* MCP

知识越来越多，框架越来越多。

但脑海中依然缺少一张稳定的地图。

问题往往不是：

学得不够多。

而是：

没有形成自己的知识系统。

这个项目因此而生。

它试图建立一棵完整的 AI System Knowledge Tree：

Worldview
    ↓
Model
    ↓
Training
    ↓
Inference
    ↓
AI Infrastructure
    ↓
Agent

以后遇到任何新的：

* 模型
* 论文
* 框架
* Runtime
* 优化方法
* Agent 技术

都应该首先回答：

它在整棵知识树中的位置是什么？

⸻

The Core Philosophy

这个项目不满足于回答：

What is Attention?

而希望继续追问：

Why Attention?

不是直接告诉你：

Q = XWq
K = XWk
V = XWv

而是从问题开始：

一个 Token 如何根据上下文重新理解自己？
        ↓
为什么 MLP 不够？
        ↓
为什么 RNN 不够？
        ↓
能否让信息路由依赖当前输入？
        ↓
Attention
        ↓
为什么又需要 Q、K、V？

我们希望尽可能重新走一遍技术诞生的道路。

不是站在答案面前背答案。

而是假设：

如果今天我们不知道 Transformer，我们能否重新把它发明出来？

⸻

What Makes This Project Different?

1. First Principles

每一个重要概念都从问题出发。

Problem
    ↓
Naive Solution
    ↓
Failure
    ↓
Better Solution
    ↓
New Trade-off
    ↓
Modern Design

我们关心的不只是：

它是什么？

更关心：

为什么它必须出现？

⸻

2. System Thinking

单独理解一个技术通常并不困难。

真正困难的是理解它们之间的关系。

例如：

Tokenizer
    ↓
Embedding
    ↓
Attention
    ↓
KV Cache
    ↓
PagedAttention
    ↓
Continuous Batching
    ↓
vLLM
    ↓
PD Disaggregation
    ↓
LLM Runtime
    ↓
AI Infrastructure

这里没有任何一个概念是孤立的。

它们共同构成了一条完整的系统演化链。

⸻

3. Design Trade-offs

现实世界里几乎没有免费的优化。

例如：

KV Cache
减少重复计算
        ↓
降低 Decode 计算量
        ↓
但增加显存占用
        ↓
长上下文进一步放大显存压力
        ↓
于是出现 PagedAttention
        ↓
进一步推动 KV Cache 调度与 PD 分离

因此，每一章都会重点讨论：

* 得到了什么？
* 失去了什么？
* 为什么这个 Trade-off 在今天仍然值得？
* 哪些约束改变后，当前设计可能失效？

⸻

4. Engineering Reality

AI 并不只发生在论文里。

最终所有算法都会撞上真实世界：

* GPU Memory
* Compute
* Communication
* Network
* Scheduling
* Throughput
* Latency
* Cost
* Reliability

因此本项目会持续连接：

Algorithm
    ↓
GPU
    ↓
Runtime
    ↓
Distributed System
    ↓
Production Infrastructure

重点关注的真实系统包括：

* PyTorch
* Megatron
* DeepSpeed
* vLLM
* SGLang
* TensorRT-LLM
* KServe
* Kubeflow
* Kubernetes
* GPU Scheduler
* Agent Runtime

但本项目不会围绕某个框架组织知识。

因为：

框架会变化，问题长期存在。

⸻

Knowledge Tree

整个项目目前分为六个部分。

Part I · Worldview

AI 为什么会发展成今天这样？

理解：

* AI 的技术演化
* 模型为什么能够学习
* 表示学习
* Scaling Law
* 涌现能力
* AI System 的长期演化路线

目标不是学习某个模型。

而是建立一张完整的 AI 世界地图。

⸻

Part II · Model

一个 Token 如何最终变成答案？

从：

Text
    ↓
Tokenizer
    ↓
Embedding
    ↓
Position
    ↓
Attention
    ↓
MLP
    ↓
Transformer
    ↓
Sampling
    ↓
Output

逐层理解：

* Tokenizer
* Embedding
* Position Encoding
* Self Attention
* Multi-Head Attention
* MLP
* Transformer Layer
* Decoder Only
* KV Cache
* Sampling
* MoE
* Long Context

目标不是背 Transformer。

而是理解：

为什么整个模型最终收敛到今天这套设计。

⸻

Part III · Training System

模型能力是如何生产出来的？

研究：

Data
    ↓
Pretraining
    ↓
Checkpoint
    ↓
SFT
    ↓
Preference Learning
    ↓
RL / DPO / GRPO

以及：

Single GPU
    ↓
Data Parallel
    ↓
Tensor Parallel
    ↓
Pipeline Parallel
    ↓
ZeRO
    ↓
Large-Scale Training System

主要内容：

* Data
* Pretraining
* SFT
* LoRA
* RLHF
* PPO
* GRPO
* DPO
* Checkpoint
* Distributed Training
* Tensor Parallel
* Pipeline Parallel
* ZeRO
* Megatron
* DeepSpeed

⸻

Part IV · Inference System

为什么推理正在成为 AI Infra 的核心战场？

一个请求进入系统之后：

Request
    ↓
Tokenization
    ↓
Scheduling
    ↓
Prefill
    ↓
KV Cache
    ↓
Decode
    ↓
Sampling
    ↓
Streaming Response

背后涉及：

* Prefill
* Decode
* KV Cache
* Continuous Batching
* PagedAttention
* Speculative Decoding
* TensorRT-LLM
* vLLM
* SGLang
* Dynamo
* KServe LLM
* GPU Memory
* PD Disaggregation
* Inference Scheduling

这一部分将重点连接：

Model Architecture
        ↓
GPU Architecture
        ↓
Runtime Design
        ↓
Distributed Serving

⸻

Part V · AI Infrastructure

如何从工具走向平台？

一个真正的 AI Platform 不只是：

训练页面
+
模型部署页面

而是围绕整个模型生命周期构建：

Data
    ↓
Training
    ↓
Model
    ↓
Deployment
    ↓
Serving
    ↓
Observability
    ↓
Evaluation
    ↓
Feedback

核心内容包括：

* AI Platform
* Kubeflow
* Model Registry
* Training Operator
* KServe
* Gateway
* GPU Scheduler
* Volcano
* Kai Scheduler
* MLflow
* Monitoring
* Logging
* Trace
* Cost
* Multi-Tenancy
* Security
* Production Best Practices

目标是理解：

如何设计一个真正可以长期运行的 AI System。

⸻

Part VI · Agent

如何让模型从回答问题，走向执行任务？

模型本身只会生成 Token。

但真实系统需要：

Prompt
    ↓
Context
    ↓
RAG
    ↓
Memory
    ↓
Tool Calling
    ↓
Planning
    ↓
Workflow
    ↓
Agent

主要内容：

* Prompt
* Context
* RAG
* Memory
* Tool Calling
* Planning
* Reflection
* Workflow
* Multi-Agent
* MCP
* Agent Platform

最终关注的问题是：

如何构建可治理、可观测、可控、可复用的 Agent System。

⸻

Chapter Design

每一个重要章节原则上遵循同一套结构。

1. Chapter Question

这一章真正需要回答的问题是什么？

⸻

2. Problem

如果没有这项技术，系统会遇到什么根本问题？

⸻

3. Thought Experiment

假设我们不知道标准答案。

我们会如何尝试自己设计一个方案？

⸻

4. History / Evolution

技术是如何一步步演化到今天的？

⸻

5. First Principles

从最基本的约束重新推导设计。

⸻

6. Math

数学究竟解决了什么问题？

不为了公式而讲公式。

⸻

7. Engineering

算法如何真正运行在：

* GPU
* Memory
* Network
* Distributed Systems

之上？

⸻

8. Design Trade-offs

设计获得了什么，又付出了什么？

⸻

9. Alternatives & Dead Ends

还有哪些方案？

为什么没有成为主流？

⸻

10. Engineering Practice

如何连接真实工业系统和生产问题？

⸻

11. AI System Position

这个概念位于整棵知识树的哪里？

⸻

12. Interview Questions

真正能够检验理解深度的问题。

⸻

13. Research Outlook

未来可能如何演化？

⸻

14. Reflection

哪些问题仍然没有答案？

⸻

Learning Method

这个项目遵循一个长期原则：

先建立主干，再补充叶子。

不要试图第一次就把每一个章节学到极致。

推荐顺序：

Stage 1
建立 AI System 世界观
        ↓
Stage 2
理解模型内部机制
        ↓
Stage 3
理解模型能力如何产生
        ↓
Stage 4
深入推理系统
        ↓
Stage 5
构建 AI Infrastructure
        ↓
Stage 6
进入 Agent System

学习不是线性的。

它更像不断回到同一棵树上：

第一次
知道它在哪里
第二次
理解它是什么
第三次
理解为什么这样设计
第四次
理解工程实现
第五次
阅读源码
第六次
理解论文和未来演化

⸻

Current Focus

当前最优先的学习路线：

为什么模型能够学习
        ↓
Tokenizer
        ↓
Embedding
        ↓
Position Encoding
        ↓
Attention
        ↓
Transformer
        ↓
KV Cache
        ↓
Inference
        ↓
PD Disaggregation
        ↓
LLM Runtime
        ↓
AI Infrastructure

重点不是追求速度。

而是逐步形成：

可以迁移到未来技术的底层判断力。

⸻

Repository Structure

计划中的目录结构：

.
├── README.md
├── ROADMAP.md
├── AGENTS.md
│
├── docs/
│   ├── PROJECT_CONTEXT.md
│   ├── LEARNING_PHILOSOPHY.md
│   ├── WRITING_GUIDE.md
│   ├── LEARNING_STATE.md
│   └── DECISIONS.md
│
├── books/
│   ├── 01-worldview/
│   ├── 02-model/
│   ├── 03-training-system/
│   ├── 04-inference-system/
│   ├── 05-ai-infrastructure/
│   └── 06-agent/
│
├── labs/
├── examples/
├── papers/
└── assets/

其中：

* ROADMAP.md：整个项目的 Single Source of Truth
* AGENTS.md：AI Coding Agent 的项目规则
* PROJECT_CONTEXT.md：项目背景和长期目标
* LEARNING_PHILOSOPHY.md：学习方法
* LEARNING_STATE.md：当前学习位置
* DECISIONS.md：重要设计决策和知识体系演化记录

⸻

Living Book

这不是一本写完之后就结束的书。

它是一个持续演进的知识系统。

未来会不断加入：

* 新模型架构
* 新训练方法
* 新推理系统
* 新论文
* 新源码分析
* 新工程实践
* 新的失败案例
* 新的设计权衡

但所有新内容都应该首先回答：

它应该位于知识树中的哪里？

而不是不断制造新的碎片。

⸻

Long-Term Vision

这个项目最终希望同时成为：

📚 一套系统教材
🗺️ 一张知识地图
🧠 一套思考框架
⚙️ 一本工程手册
💻 一份源码索引
📄 一条论文阅读路径
🧪 一个实验系统

最终目标并不是：

成为最会使用某个 AI 框架的人。

而是：

建立设计下一代 AI System 所需要的判断力。

⸻

Who Is This For?

这个项目更适合已经拥有一定工程背景，并希望进入以下方向的人：

* AI Infrastructure
* LLM Runtime
* ML Systems
* Distributed Training
* Model Serving
* LLMOps
* Agent Platform
* AI System Architecture

尤其适合来自：

* Backend Engineering
* Distributed Systems
* Kubernetes
* Data Infrastructure
* MLOps
* Platform Engineering

背景的工程师。

它并不试图成为最简单的大模型入门教程。

它希望做的是：

帮助有工程经验的人，建立一套真正完整的 AI System 世界模型。

⸻

Roadmap

完整知识树：

👉 See ROADMAP.md⁠￼

⸻

Contributing

这个项目仍处于持续建设中。

欢迎：

* 讨论设计问题
* 指出技术错误
* 补充经典论文
* 提供工程案例
* 讨论不同技术路线
* 提出更好的第一性原理解释

但这个项目不追求：

内容越多越好。

更重要的是：

结构是否一致，推导是否严谨，知识是否真正连接起来。

⸻

License

计划采用双许可证模式。

Educational Content

原创教材、文章、RoadMap 和图表：

CC BY-NC-SA 4.0

允许非商业学习、分享和修改，但需署名，并以相同方式共享。

Source Code

原创代码、Labs 和 Examples：

Apache License 2.0

第三方内容保留其原始版权和许可证。

⸻

Final Thought

AI 领域变化很快。

模型会变化。

框架会变化。

今天的最佳实践也会变化。

但真正长期存在的是那些底层问题：

知识如何被表示？
能力如何被训练出来？
GPU 如何被高效利用？
推理如何平衡吞吐和延迟？
系统如何持续迭代？
Agent 如何安全地执行任务？

这个项目希望做的事情很简单：

不追着每一个答案跑。

而是建立一套能够持续寻找答案的方法。