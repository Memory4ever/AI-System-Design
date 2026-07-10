# 第9章 AI System 的演化路线

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Status:** Draft

**Roadmap Intent:** 从单机训练到分布式训练，从离线模型到在线 Serving，从 MLOps 到 LLMOps。

## 本章要回答的问题

为什么一个能在 notebook 中训练和预测的模型，最终会需要 Pipeline、分布式训练、Serving、LLM runtime、平台控制面乃至 Agent runtime？这些系统形态是在解决什么逐步迁移的瓶颈？

第 2 章从规则系统、机器学习、深度学习、LLM 到 Agent 讨论**能力范式**迁移。本章只追踪另一条线：**支撑能力生产与交付的系统形态，如何从单人实验演化为可复现 Pipeline、计算集群、在线服务、状态化 runtime 和治理平台。**

中心命题是：AI System 的演化由主瓶颈迁移推动。早期瓶颈是“能否做出有效实验”，随后依次变成“能否复现”“能否扩大计算”“能否在线交付”“能否管理运行时状态”，最后变成“能否跨团队控制质量、成本、风险与行动”。

## 第一阶段：单机实验解决可行性

最初的目标通常很简单：准备一份数据，训练一个模型，在 validation set 上看到指标改善。代码、数据路径、超参数和环境可能都由同一个人管理。

```text
local data -> training script -> model file -> offline metric
```

这种形态的优势是反馈快。研究者可以自由修改特征、架构和 loss，不必先设计稳定接口。对于探索未知问题，过早平台化反而会增加摩擦。

但单机实验把大量状态藏在人的工作目录和记忆里：究竟用了哪版数据，哪些 preprocessing，什么依赖，哪个 seed，哪个 checkpoint 对应哪组指标。只要另一个人尝试复现，或者数周后需要继续实验，隐式状态就会变成主要故障源。

第一个系统瓶颈因此不是 GPU 数量，而是**实验无法成为可追踪资产**。

## 第二阶段：Pipeline 解决可复现生产

朴素修复是写一个更长的 shell script，把数据处理、训练和评估串起来。这在步骤较少时有效，随着数据校验、特征生成、训练、评估、审批和发布增多，脚本会积累路径耦合、重复计算、隐式依赖和人工恢复逻辑。

Pipeline 把过程显式表示为有输入、输出和依赖的步骤：

```text
ingest -> validate -> transform -> train -> evaluate -> register
```

关键收益不是画出 DAG，而是让 artifact、metadata 和 execution 关联起来。某个 checkpoint 可以追溯到数据版本、代码、配置和评估；失败步骤可以有边界地重试；相同组件可以在不同实验中复用。

TFX 等生产 ML 平台工作说明，训练只是持续 ML Pipeline 的一个组件，数据验证、模型验证和 Serving 连接同样重要。Sculley 等人对 hidden technical debt 的分析则提醒：ML 系统的复杂性常来自数据依赖、配置、反馈回路、胶水代码和外部世界变化，而不只是模型代码。

Pipeline 也有代价。组件接口降低自由度，metadata 和 artifact 管理增加系统复杂性，错误地缓存或复用还可能制造静默数据问题。只有当复现、协作和持续运行成为真实需求时，这层抽象才产生净收益。

## 第三阶段：分布式训练解决规模约束

当模型、数据或期限超过单设备能力，Pipeline 能复现实验，却不能让一次训练装得下或按时完成。系统瓶颈转向 compute、memory 和 communication。

分布式训练把原本单设备中的对象切分到多个 worker：

- Data Parallel 切分 batch，并聚合梯度；
- Tensor Parallel 切分单层矩阵计算；
- Pipeline Parallel 切分模型层与 micro-batch；
- ZeRO 类方法切分参数、梯度或 optimizer state。

这不是纯加速问题。worker 必须在 collective communication、拓扑、同步语义和 failure recovery 下维持正确优化过程。集群越大，单卡性能越不能代表 job completion time；straggler、网络拥塞、checkpoint I/O 和节点故障都会放大。

此时 Scheduler 也从“找空闲机器”演化为表达 gang、拓扑、优先级、配额和抢占策略的控制系统。训练任务需要一组资源同时可用，跨机互联位置可能直接影响吞吐，失败重启还需要重建分布式状态。

规模化训练解决了能力生产上限，却制造了资源治理与组织公平性问题：谁能使用多少 GPU，紧急任务是否可抢占，实验吞吐与集群利用率如何平衡，成本归属怎样计算。

## 第四阶段：在线 Serving 解决能力交付

离线 batch prediction 可以等待任务完成，在线业务要求请求在 SLO 内返回，并能处理流量变化、故障和版本切换。系统形态从 job 转向 service：

```text
model artifact -> deployment -> replica -> endpoint -> traffic
```

Serving 需要管理模型加载、健康检查、扩缩容、版本发布、回滚、流量路由、认证和观测。模型成功启动不等于服务可用：输入 schema、preprocessing、依赖版本和训练/Serving skew 都可能让线上行为偏离离线评估。

传统预测服务常把一次请求近似看作独立前向计算。平台可以按 QPS、CPU/GPU utilization 和 latency 做容量管理。随着模型变大，加载时间、显存占用和硬件异构性增加，模型生命周期逐渐不同于普通微服务。

在线化还让质量反馈进入系统。HTTP 200 只证明链路完成，不能证明预测正确。服务指标、业务结果、数据 drift 和模型 Evaluation 必须关联，才能形成从部署回到能力生产的闭环。

## 第五阶段：LLM Runtime 管理 token 与状态

LLM Serving 保留了在线服务的生命周期问题，又改变了请求内部结构。一次生成包含 Prefill 和逐 token Decode；请求长度不齐；KV Cache 随上下文和输出增长；streaming 让首 token 和后续 token 具有不同 SLO。

朴素方案是一个请求占用一个 worker 直到生成结束。短期容易实现，但不同长度请求会造成 GPU 空洞，KV Cache 容量限制并发，长请求还可能阻塞短请求。

LLM runtime 因而引入 token-level 或 iteration-level scheduling、continuous batching、paged KV memory、prefix reuse、speculative decoding、parallelism 和 admission control。系统负载单位不再只是 request，而包含 prompt token、generated token、active sequence 和 KV block。

```text
request lifecycle
  -> Prefill compute
  -> KV Cache state
  -> iterative Decode
  -> streamed output
```

这使 Runtime 与 Serving 的边界更重要。Runtime 决定模型怎样在 GPU 上执行和共享状态；Serving 决定副本、发布、流量和生命周期；Gateway 决定入口策略。把三者全部称为“模型服务”会让性能和治理问题无法定位。

LLM 也让 prompt、context、retrieval、sampling 和 safety policy 进入可版本化配置。即使 checkpoint 不变，运行时行为也可能改变。传统只围绕 model artifact 的 MLOps 资产模型不再足够。

## 第六阶段：平台治理解决跨团队控制

当多个团队共享训练、模型、Serving 和 GPU，局部最优开始互相冲突。业务希望快速上线，平台希望统一接口，基础设施希望提高利用率，安全与合规要求审批和审计，财务要求成本可归因。

把更多工具放进一个 Portal 不是平台化。真正的平台控制面至少要建立稳定对象与策略：

```text
identity / tenant / quota
data / experiment / model / deployment
runtime / resource / policy
metric / evaluation / trace / cost
```

控制面声明期望状态，data plane 执行训练、推理和流量处理，observability 提供实际状态，controller 根据偏差采取动作。这个闭环与 Kubernetes control loop 有相似性，但 AI 对象还包含概率质量、数据血缘和模型版本，不能只看资源状态。

平台抽象过薄，团队会重复搭建胶水代码；抽象过厚，则可能隐藏 runtime 关键参数、阻碍新模型接入并造成最低公分母。成熟平台需要分层：稳定治理契约放在上层，性能敏感与快速变化能力通过可扩展 runtime interface 暴露。

## 第七阶段：Agent Runtime 管理行动闭环

LLM 返回文本时，失败影响主要停留在答案。Agent 调用数据库、代码环境、工单、支付或基础设施后，输出会改变外部状态。

运行过程也从单次生成变成多步状态机：

```text
goal -> plan -> tool call -> observation -> state update -> next action
```

朴素实现让模型在循环里自由决定下一步。它缺少可靠终止、权限边界、幂等、补偿、人工确认和 durable state，因而很难用于高风险任务。

Agent runtime 需要把模型决策放入受控执行环境：工具 schema 与身份、最小权限、预算、超时、重试、checkpoint、审计 trace、评估和 human-in-the-loop。模型提供开放式判断，workflow 与 policy 提供硬约束。

这一步把 AI System 从“交付预测能力”推进到“治理行动能力”。平台不再只管理 model deployment，也要管理任务状态、工具连接、用户上下文和外部副作用。

## MLOps、LLMOps 与 AgentOps 的边界

这些词更适合描述运维对象扩展，而不是三代互相替代的产品类别。

| 范围 | 核心资产与状态 | 主要运行问题 |
| --- | --- | --- |
| MLOps | data、feature、experiment、model、deployment | 可复现、训练/Serving skew、持续评估与发布 |
| LLMOps | 上述对象 + prompt、context、retrieval、token runtime、KV state | 生成质量、长上下文、成本、token 调度与安全 |
| AgentOps | 上述对象 + tool、memory、workflow、action、environment state | 权限、持久状态、多步恢复、副作用与审计 |

LLMOps 没有让数据血缘、模型版本和部署治理失效；AgentOps 也没有让 LLM runtime 消失。每一层继承前一层问题，再增加新的运行时对象。

所以引入新术语前应先问：系统新增了什么必须管理的状态、控制环和失败模式？如果只是更换产品名，没有新增对象或责任边界，就没有必要建立新的知识树分支。

## 一条统一的演化逻辑

七个阶段可以压缩为瓶颈迁移表：

| 阶段 | 首要目标 | 暴露的新瓶颈 |
| --- | --- | --- |
| 单机实验 | 证明任务可行 | 隐式状态、不可复现 |
| 可复现 Pipeline | 让能力生产可追踪 | 组件契约、持续数据变化 |
| 分布式训练 | 突破单设备规模与时间 | 通信、容错、集群调度、成本 |
| 在线 Serving | 在 SLO 内交付模型 | 生命周期、流量、线上质量 |
| LLM Runtime | 高效生成并管理 KV 状态 | token 调度、长尾、显存与长上下文 |
| 平台治理 | 跨团队复用与控制 | 抽象边界、策略冲突、组织复杂性 |
| Agent Runtime | 在环境反馈中执行任务 | 权限、持久状态、副作用与责任 |

演化不是所有团队都必须走完的成熟度阶梯。一个小规模离线模型没有必要复制大型 Agent 平台；一个高风险工具 Agent 即使流量很小，也可能从第一天就需要严格权限和审计。阶段描述的是问题何时出现，不是采购清单。

## 控制闭环是系统成熟的共同标志

无论处于哪个阶段，系统从脚本走向平台的关键不是组件数量，而是能否形成闭环：

```text
declare objective
-> execute
-> observe
-> evaluate
-> decide
-> change with rollback
```

训练 Pipeline 的闭环比较新 checkpoint 与基线；Serving 的闭环比较实际 SLO 与期望；LLM 系统还比较输出质量与成本；Agent 系统还要评估动作结果和副作用。

自动化不等于闭环。没有 Evaluation 的自动重训，可能更快发布退化模型；没有权限的自动 Agent，可能更快执行错误动作；没有回滚和血缘的控制器，也无法安全纠偏。

## 本章在知识树中的位置

本章把第 3 章的能力生产、能力交付、控制治理和 Agent 闭环放到时间轴上。它解释了为什么后续 Part III、IV、V、VI 分别会形成 Training System、Inference Runtime、AI Platform 与 Agent Platform。

本章不重复第 2 章：第 2 章问“模型和任务能力为何从规则演化到 LLM 与 Agent”，本章问“工程系统为何从 notebook 演化到 Pipeline、Runtime 和治理控制面”。能力突破会触发系统变化，系统成熟又会让能力规模化，二者相互推动但不是同一叙事。

## 自检问题

1. 单机实验的第一个系统瓶颈为什么常常不是算力？
2. Pipeline 相比长脚本新增了哪些可追踪对象？
3. 分布式训练为什么同时是优化语义、通信和调度问题？
4. 在线 Serving 与离线 prediction 的控制目标有什么不同？
5. LLM runtime 为什么需要 token-level 状态与调度？
6. Runtime、Serving 与 Gateway 应怎样分工？
7. 平台 Portal 与平台 control plane 有什么区别？
8. MLOps、LLMOps、AgentOps 各自新增了哪些状态？
9. 为什么演化阶段不是每个团队都要照搬的成熟度清单？
10. 自动化为什么不能替代 Evaluation、权限和回滚闭环？

## 小结

AI System 从单机脚本演化到平台，不是因为系统天然喜欢复杂，而是能力规模与交付责任不断暴露隐式状态。可行性之后需要复现，复现之后需要扩展计算，模型生产之后需要在线交付，LLM 又引入 token 与 KV 状态，Agent 最终把权限和外部行动带入运行时。

MLOps、LLMOps 和 AgentOps 描述的是被管理对象逐步扩展。系统设计应从当前瓶颈出发，引入足够的 Pipeline、Runtime 和治理能力，同时警惕没有真实复用或控制收益的平台抽象。

## Review notes

本章保持“系统形态演化”主线，不按年份罗列框架，也不重述第 2 章的模型范式。后续 Review 应重点检查各阶段是否由明确瓶颈触发，以及 MLOps、LLMOps、AgentOps 是否仍以状态和控制责任区分，而不是变成市场术语。

优先核验入口：

- D. Sculley et al., "Hidden Technical Debt in Machine Learning Systems", 2015: https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
- Denis Baylor et al., "TFX: A TensorFlow-Based Production-Scale Machine Learning Platform", 2017: https://research.google/pubs/tfx-a-tensorflow-based-production-scale-machine-learning-platform/
- Martin Abadi et al., "TensorFlow: A System for Large-Scale Machine Learning", 2016: https://research.google/pubs/tensorflow-a-system-for-large-scale-machine-learning/
- Eric Breck et al., "What's your ML test score? A rubric for ML production systems", 2016: https://research.google/pubs/whats-your-ml-test-score-a-rubric-for-ml-production-systems/
- Woosuk Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", 2023: https://arxiv.org/abs/2309.06180
- Shunyu Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", 2022: https://arxiv.org/abs/2210.03629
