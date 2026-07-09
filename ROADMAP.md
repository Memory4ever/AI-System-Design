<!--
This file is the Single Source of Truth for the AI System knowledge tree.
Keep the overall structure stable. Add new topics by locating them in the existing tree first.
-->

# AI System：从大模型原理到 AI 基建

**版本：**v0.1 初版

**目标读者：**已经具备软件工程、后端系统、Kubernetes 或平台工程经验，正在进入大模型 / AI Infra / LLMOps 的工程师。

**写作原则：**每一章先讲 Why，再讲 What，最后讲 How；先建立稳定的知识树，再逐步补充框架、论文、代码和工程案例。

## 前言：为什么要写这套课程

学习大模型和 AI 基建，最容易掉进一个陷阱：每天都在追新工具，却没有一张稳定的地图。今天看 vLLM，明天看 KServe，后天看 Ray、SGLang、Dynamo、TensorRT-LLM、DeepSpeed、Megatron，知识越来越多，但内在结构并没有建立起来。

这套课程的目标不是把所有工具罗列一遍，而是帮助你建立一棵 AI System 的知识树。以后每遇到一个新框架，你都能判断它位于哪一层，解决什么长期问题，带来什么新的权衡。

对做 AI Infra 的工程师来说，真正有价值的能力不是“会用某个框架”，而是能理解模型、训练、推理、Serving、调度、可观测性、成本治理和 Agent 之间的系统关系，并能把这些能力组织成可复用的平台。

> **核心学习路径：世界观 → 模型原理 → 训练系统 → 推理系统 → AI 平台 → Agent。**

## 全书结构总览

| 部分 | 核心目标 |
| --- | --- |
| Part I 世界观：AI 为什么会发展成今天这样 | 建立底层问题意识，理解 AI System 的演化路线。 |
| Part II 模型：一个 Token 如何变成答案 | 理解 Tokenizer、Embedding、Attention、Transformer、KV Cache、Sampling 等模型内部机制。 |
| Part III Training System：模型能力如何产生 | 理解数据、预训练、SFT、LoRA、RLHF、GRPO、分布式训练等能力生产过程。 |
| Part IV Inference System：为什么推理是 AI Infra 的核心战场 | 理解 Prefill、Decode、Continuous Batching、PagedAttention、PD 分离、vLLM、SGLang、Dynamo 等。 |
| Part V AI Infrastructure：从工具到平台 | 理解 Kubeflow、KServe、Model Registry、Gateway、GPU Scheduler、监控、日志、Trace、多租户和生产治理。 |
| Part VI Agent：从回答问题到执行任务 | 理解 Prompt、Context、RAG、Memory、Tool Calling、Planning、Workflow、Multi-Agent、MCP。 |

## 六大部分章节规划

### Part I 世界观：AI 为什么会发展成今天这样

- **第1章 为什么学习 AI System**：AI System 不是模型部署，而是让模型稳定、高效、可控、可迭代地产生业务价值的一组系统。
- **第2章 AI 的发展历史**：从规则系统到机器学习、深度学习、Transformer、LLM、Agent，理解每次范式变化背后的瓶颈。
- **第3章 AI System 全局知识树**：建立 Data、Training、Model、Inference、Serving、Scheduling、Observability、Evaluation、Agent 的全局地图。
- **第4章 模型为什么能够学习**：从函数近似、损失函数、梯度下降、表示学习理解“学习”的本质。
- **第5章 神经网络到底学到了什么**：理解特征、表示空间、分布、泛化和归纳偏置。
- **第6章 Transformer 为什么改变世界**：理解注意力机制如何统一建模序列依赖、上下文关系和可扩展训练。
- **第7章 Scaling Law 为什么成立**：理解参数、数据、算力之间的经验规律，以及为什么规模会带来能力跃迁。
- **第8章 大模型为什么会产生智能**：从预测下一个 token 到涌现能力、上下文学习和工具使用。
- **第9章 AI System 的演化路线**：从单机训练到分布式训练，从离线模型到在线 Serving，从 MLOps 到 LLMOps。
- **第10章 AI 的未来**：Agent、个性化模型、世界模型、端侧智能与 AI 平台化。
### Part II 模型：一个 Token 如何变成答案

- **第11章 Tokenizer**：文本如何被切成 token，为什么 tokenizer 会影响知识表示、上下文长度和多语言能力。
- **第12章 Embedding**：离散 token 如何进入连续向量空间，模型如何在向量空间里表达语义关系。
- **第13章 Position Encoding**：为什么 Transformer 需要位置信息，以及绝对位置、相对位置、RoPE 的差异。
- **第14章 Self Attention**：每个 token 如何根据上下文重新理解自己。
- **第15章 Multi-Head Attention**：为什么需要多个注意力头，从不同子空间捕捉关系。
- **第16章 Feed Forward / MLP**：Attention 负责信息混合，MLP 负责非线性变换与知识存储。
- **第17章 Transformer Layer**：Residual、Normalization、Attention、MLP 如何组成可堆叠模块。
- **第18章 Decoder Only 架构**：为什么主流 LLM 采用自回归 Decoder Only。
- **第19章 KV Cache**：为什么生成时要缓存历史 Key/Value，它如何改变推理系统设计。
- **第20章 Sampling**：温度、top-k、top-p、贪心解码如何影响输出风格和稳定性。
- **第21章 MoE**：稀疏专家模型如何扩大容量，同时控制计算成本。
- **第22章 Long Context**：长上下文为什么困难，位置编码、显存、注意力复杂度和检索增强如何互相影响。
### Part III Training System：模型能力如何产生

- **第23章 数据**：数据质量、分布、清洗、去重、配比决定模型上限。
- **第24章 Pretraining**：大规模预训练如何形成通用语言和世界知识。
- **第25章 SFT**：监督微调如何把通用模型对齐到指令、任务和业务风格。
- **第26章 LoRA**：为什么低秩适配可以高效改变模型行为，而不必全量更新参数。
- **第27章 RLHF**：人类偏好如何通过奖励模型影响模型输出。
- **第28章 PPO**：从策略优化角度理解传统 RLHF 的训练过程。
- **第29章 GRPO**：为什么 GRPO 适合大模型推理增强，如何用组内相对优势降低训练复杂度。
- **第30章 DPO**：直接偏好优化如何绕过显式奖励模型。
- **第31章 Checkpoint**：模型权重、优化器状态、训练恢复与版本管理。
- **第32章 分布式训练**：为什么单机训练不够，通信、显存、吞吐如何成为核心瓶颈。
- **第33章 Tensor Parallel**：把矩阵计算切到多张卡上。
- **第34章 Pipeline Parallel**：把模型层切到多张卡上，流水线执行。
- **第35章 ZeRO**：切分优化器状态、梯度和参数，降低显存占用。
- **第36章 Megatron**：大模型训练框架中的并行策略组合。
- **第37章 DeepSpeed**：训练优化、ZeRO、推理优化和工程化封装。
### Part IV Inference System：为什么推理是 AI Infra 的核心战场

- **第38章 推理到底发生了什么**：一个请求从 API 进入，到 token 流式返回，经历哪些阶段。
- **第39章 Prefill**：Prompt 阶段一次性处理上下文，计算密集、可并行度高。
- **第40章 Decode**：逐 token 生成阶段串行性强，延迟敏感。
- **第41章 为什么 KV Cache 能提速**：避免重复计算历史上下文，是 LLM 推理系统的核心状态。
- **第42章 Continuous Batching**：动态合并请求，提高 GPU 利用率。
- **第43章 PagedAttention**：像操作系统管理内存一样管理 KV Cache。
- **第44章 Speculative Decoding**：用小模型猜测，大模型验证，缓解自回归串行瓶颈。
- **第45章 TensorRT-LLM**：面向 NVIDIA GPU 的高性能推理优化。
- **第46章 vLLM**：以 PagedAttention 和调度为核心的大模型 Serving 引擎。
- **第47章 SGLang**：面向结构化生成、复杂推理和高效 Serving 的运行时。
- **第48章 Dynamo**：面向大规模推理的服务编排与 PD 分离方案。
- **第49章 KServe LLM**：在 Kubernetes 上标准化管理大模型推理服务。
- **第50章 GPU Memory**：权重、激活、KV Cache、临时 buffer 如何争夺显存。
- **第51章 PD 分离**：Prefill 和 Decode 计算特征不同，为什么要拆分部署。
- **第52章 推理调度**：如何在吞吐、延迟、公平性、成本之间取舍。
### Part V AI Infrastructure：从工具到平台

- **第53章 什么是 AI Platform**：平台不是工具集合，而是统一资源、任务、模型、服务和治理能力。
- **第54章 Kubeflow**：基于 Kubernetes 的 ML 平台底座。
- **第55章 Model Registry**：模型资产、版本、元数据和血缘管理。
- **第56章 Training Operator**：标准化训练任务提交、分布式训练和生命周期管理。
- **第57章 KServe**：模型 Serving 的声明式管理、Runtime 抽象和流量治理。
- **第58章 Gateway**：统一入口、认证、限流、路由、协议转换和观测。
- **第59章 GPU Scheduler**：GPU 是稀缺资源，调度决定利用率和公平性。
- **第60章 Volcano**：面向批任务和 AI 训练的 Gang Scheduling。
- **第61章 Kai Scheduler**：面向 AI 工作负载的资源编排与队列治理。
- **第62章 MLflow**：实验追踪、模型管理和模型生命周期工具。
- **第63章 Monitoring**：Metrics 如何回答系统是否健康。
- **第64章 Logging**：日志如何支持排障、审计和行为分析。
- **第65章 Trace**：链路追踪如何定位请求在复杂系统中的耗时。
- **第66章 Cost**：GPU 成本、推理成本、训练成本和平台 ROI。
- **第67章 Multi Tenant**：多团队共享平台时的隔离、配额和权限。
- **第68章 Security**：模型、数据、API、Prompt、工具调用的安全边界。
- **第69章 Production Best Practice**：从 PoC 到生产环境需要补齐哪些非功能能力。
### Part VI Agent：从回答问题到执行任务

- **第70章 Prompt**：Prompt 是 LLM 时代的新接口，也是软程序。
- **第71章 Context**：上下文是 LLM 的运行时状态。
- **第72章 RAG**：用检索把外部知识动态注入上下文。
- **第73章 Memory**：短期记忆、长期记忆和用户状态管理。
- **第74章 Tool Calling**：模型如何调用外部系统，把语言能力变成行动能力。
- **第75章 Planning**：复杂任务如何被拆解、排序和执行。
- **第76章 Reflection**：模型如何基于反馈修正自己的中间结果。
- **第77章 Workflow**：把模型能力嵌入稳定、可控的业务流程。
- **第78章 Multi-Agent**：多个智能体之间如何分工、协作和互相校验。
- **第79章 MCP**：模型与工具、数据源、上下文之间的标准连接层。
- **第80章 Agent Platform**：从单个 Agent 到可治理、可观测、可复用的 Agent 平台。

## 第1章 为什么学习 AI System

大模型的出现让很多工程师误以为“AI 的核心就是模型”。但真正进入生产环境之后会发现，模型只是核心资产之一。一个模型能否稳定服务用户，取决于训练、推理、部署、监控、调度、评估、数据反馈等一整套系统。

传统软件工程中，代码是主要资产；AI 工程中，数据、模型权重、训练过程、评估结果和线上反馈共同构成资产。因此 AI System 的任务不是简单把模型跑起来，而是让模型在真实业务环境中稳定、高效、可控、可迭代地创造价值。

对平台工程师来说，学习 AI System 的意义在于获得长期稳定的判断力。框架会更新，最佳实践会变化，但底层问题长期存在：数据如何生产能力？GPU 如何被高效使用？推理如何兼顾延迟和吞吐？多团队如何共享平台？模型上线后如何持续评估和迭代？

所以这门课程的第一原则是：先理解长期问题，再学习具体工具。vLLM、KServe、Dynamo、Kubeflow、Ray、DeepSpeed 都不是孤立名词，它们分别是某些长期问题在特定阶段的工程解法。

## 第2章 AI 的发展与演化

AI 的发展不是线性堆功能，而是不断突破旧系统瓶颈的过程。早期规则系统依赖人工编码知识，优势是可解释，缺点是扩展性差。机器学习把规则从手写变成从数据中学习，但强依赖特征工程。深度学习进一步把特征也交给模型学习，但对算力和数据提出更高要求。

Transformer 的出现改变了序列建模方式。Attention 机制让模型可以直接建模 token 之间的关系，并且比传统 RNN 更适合并行训练。随着数据、参数和算力扩大，LLM 通过自回归预测下一个 token，逐步获得语言、知识、推理和上下文学习能力。

LLM 之后，AI 不再只是“输入特征，输出预测”。Prompt、Context、RAG、Tool Calling、Memory、Agent 进入系统边界。模型开始与外部知识库、工具系统、业务流程连接，AI System 的复杂度从模型训练扩展到运行时编排和平台治理。

理解这条演化路线的关键，不是记住技术名词，而是看到每一代技术试图解决的瓶颈：规则系统解决可解释性，机器学习解决规则泛化，深度学习解决特征学习，Transformer 解决长程依赖和并行扩展，LLM 解决通用能力，Agent 解决行动能力。

## 第3章 AI System 的全局知识树

AI System 不是一个系统，而是一组围绕模型生命周期构建的系统能力。它至少包含 Data System、Training System、Model System、Inference System、Serving System、Scheduling System、Observability、Evaluation System 和 Agent System。

第一条主线是数据如何变成模型能力：Raw Data 经过清洗、标注、配比、训练，生成 checkpoint，再进入模型仓库和线上服务。第二条主线是模型如何变成在线服务：模型文件进入 Runtime 和推理引擎，通过 Serving 框架、Gateway、API 对外服务。

第三条主线是昂贵计算资源如何被高效使用。大模型系统的成本核心是 GPU，因此训练优化、推理优化、显存管理、批处理、调度、弹性伸缩，本质都是围绕 GPU 利用率展开。

第四条主线是从工具到平台。单个工具解决单点问题，而平台要解决多团队、多模型、多任务、多资源共享下的治理问题，包括权限、配额、资源隔离、审计、监控、成本和自动化。

第五条主线是 LLM 带来的新系统层：Prompt Layer、Context Layer、Memory Layer、Tool Layer、Agent Layer。它们让 AI System 从传统 MLOps 扩展到 LLMOps 和 AgentOps。

## 建议学习路线：先主干，后叶子

### 第一阶段：建立世界观

先读 Part I，目标不是掌握所有概念，而是理解 AI System 的问题空间。读完后应该能画出 AI System 的全局知识树。

### 第二阶段：理解模型内部机制

读 Part II，目标是能从一个 token 的生命周期理解 Transformer，而不是背公式。

### 第三阶段：理解能力生产过程

读 Part III，重点理解数据、训练、微调、强化学习和分布式训练之间的关系。

### 第四阶段：深挖推理系统

读 Part IV，这是和 AI Infra 工作最贴近的部分，要把 Prefill、Decode、KV Cache、Batching、PD 分离和推理调度学透。

### 第五阶段：搭建平台能力

读 Part V，把单点工具组织成平台：训练、模型管理、Serving、网关、调度、可观测性、多租户。

### 第六阶段：进入 Agent 平台

读 Part VI，理解 LLM 如何从回答问题变成执行任务，以及 Agent 平台需要的系统能力。

## 后续扩写方式

本初版是课程母版，后续可以按章节逐步扩写。每章建议保持统一结构：1）为什么需要它；2）它解决了什么问题；3）核心机制；4）工程实现；5）典型框架；6）常见误区；7）与整棵知识树的关系。

最适合优先扩写的路线是：第4章模型为什么能够学习 → 第6章 Transformer → 第19章 KV Cache → 第38章推理到底发生了什么 → 第51章 PD 分离 → 第57章 KServe。
