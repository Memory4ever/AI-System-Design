# AI Infra 面试：16 周成长计划

- **状态：**执行中
- **目标级别：**Senior IC 到 Staff
- **目标岗位：**AI Platform、LLM Serving / Inference、Distributed Training
- **公司配比：**外企 70%，国内大厂 30%
- **主要语言：**Python 和 Go，同时培养 C++ / CUDA 阅读与 profiling 能力
- **可用环境：**单机多卡
- **投递策略：**第 16 周完成后开始正式投递

## 1. 计划目标

这份计划要把仓库中已有的知识树转化为面试能力和工程证据，而不是重新通读全部 80 章。第 16 周结束时，学习者应当能够：

1. 推导模型、训练、推理和平台的核心机制；
2. 实现并测量具有代表性的多 GPU workload；
3. 从 Compute、Memory、Communication、Scheduling 和 State 五个角度诊断故障；
4. 在明确的 SLO、容量、成本、租户和恢复约束下设计端到端 AI Platform；
5. 以 Senior IC 到 Staff 的深度，用中英文解释项目决策。

整个成长闭环是：

```text
知识
-> 可执行实验
-> 测量与证据
-> 设计决策
-> 面试表达
-> 对抗性 Review
```

## 2. 资料职责

| 来源 | 职责 | 使用规则 |
| --- | --- | --- |
| `books/` | 稳定的心智模型与跨系统推导 | 阅读 owner 章节和相邻章节，不把书稿改成面试速记 |
| `papers/` | Primary-source 证据与最新研究 | 只使用会改变设计决策或适用边界的材料 |
| `labs/` | 可复现代码、benchmark、profiling 和故障证据 | 每项性能结论必须记录 workload 与环境 |
| `interview/` | 岗位矩阵、问题、设计答案、项目故事和 Mock 记录 | 面试压缩材料不进入 Book |
| AI-fundamentals | GPU、集群、CUDA、Kubernetes 和 Runtime 实践入口 | 版本敏感结论必须回到官方来源核验 |
| AI-Infra-from-Zero-to-Hero | MLSys 与会议论文发现入口 | 只作为索引，不作为最终技术证据 |

资料使用顺序固定为：

```text
仓库知识树
-> 官方文档或原始论文
-> 外部实现笔记
-> 本地实验
-> 面试答案
```

## 3. 每周执行模型

每周投入 10～12 小时：

| 活动 | 时间 | 必须产出 |
| --- | ---: | --- |
| Coding 与计算机基础 | 3 小时 | 4 道精选题，其中包含 1 次限时练习 |
| Labs 与 Capstone | 4 小时 | 代码、配置、原始数据和结论 |
| Books 与 primary sources | 2 小时 | 1 份主题图和未解决问题 |
| System Design 与表达 | 2 小时 | 1 次设计练习，以及中英文讲解 |
| 每周复盘 | 1 小时 | Checklist、证据链接、错误和下周修正项 |

不能因为阅读完成就进入下一周，必须先形成当周的验收证据。所有性能结果至少要绑定：

```text
硬件 + 软件版本 + 模型 + precision
+ 输入/输出分布 + 并发 + 测量方法 + SLO
```

## 4. 十六周路线

| 周次 | 核心问题 | 知识输入 | 工程产出 | 面试产出 | Exit Gate |
| ---: | --- | --- | --- | --- | --- |
| 1 | 目标岗位真正要求什么能力 | `ROADMAP.md`、Part III～V、30 个代表性 JD | 环境清单和可复现模板 | 岗位矩阵、基线 Mock、差距排序 | 三类岗位画像和十大差距均有证据支持 |
| 2 | GPU workload 的时间消耗在哪里 | 第6、14、32、50章；GPU 架构与 CUDA 来源 | Device、显存带宽、传输和计算 microbenchmark | 中英文解释 memory hierarchy 与 Roofline | 能区分 compute、memory、launch 和 transfer bound |
| 3 | 一个 token 如何变成 Runtime 工作与状态 | Part II，重点为第14～22章 | Attention / KV shape 与显存计算器及测试 | 推导 Attention、GQA/MQA、KV 容量、MoE 和 Long Context 权衡 | 不看笔记也能推导符号、shape、bytes 和复杂度 |
| 4 | 多 GPU 扩展为什么会失败 | 第32～35章；NCCL 与 collective 来源 | 不同消息大小和 GPU 组合下的单机 NCCL benchmark | 根据 tensor shape 与拓扑选择 collective | 能解释 latency/bandwidth 区间并识别误导性扩展结论 |
| 5 | 训练模型应怎样切分 | 第23～35章 | 小模型 DDP，加至少一种状态切分或模型并行实验 | 从显存和通信预算选择 DP/TP/PP/ZeRO/EP | 并行方案覆盖 global batch、显存、通信和故障影响 |
| 6 | 什么让训练能够恢复和复现 | 第31、36、37章 | Checkpoint 保存与恢复、data cursor/RNG 检查、worker 故障注入 | 训练事故深挖和恢复设计 | 恢复语义覆盖声明的训练轨迹状态，而不只是权重 |
| 7 | 请求进入后如何变成流式 token | 第38～42章 | vLLM 或 SGLang 基线服务与 workload generator | 推导 TTFT、TPOT、request/token throughput 和 goodput | 指标包含 workload distribution 和 percentile |
| 8 | 每种推理优化修改了哪个瓶颈 | 第41～44、50～52章 | Batching、KV 压力、speculative 或 prefix reuse 对照实验 | 比较 paging、batching、speculation 和 scheduling | 每项优化都有实测收益、适用边界和新增技术债 |
| 9 | Serving engine 如何持有 request 与 KV state | 第45～47章 | Profile 一条请求经过 scheduler、KV manager 和 worker 的路径 | Runtime 源码路径讲解和首次 AI Systems Mock | 能追踪完整请求，而不是把 Engine 简化成单一算法 |
| 10 | 何时需要分布式推理或 PD 分离 | 第48～52章 | 单机 PD 模拟或双进程原型，并计算 KV transfer | 设计 aggregated 与 disaggregated Serving | 明确单机证据边界，不宣称验证了多节点 RDMA |
| 11 | Kubernetes 如何把模型变成可治理服务 | 第53～58章 | Registry identity、KServe topology、Gateway routing、canary 和 rollback | AI Platform control plane System Design | Desired state、artifact identity、发布证据和 data path 相互分离 |
| 12 | 稀缺 GPU 应如何准入和调度 | 第59～61、67章 | 使用 Go 实现 scheduler policy 或 controller，并测试 queue 与 fairness | 设计包含 quota、gang、locality、fairness、preemption 的 GPU 平台 | 策略决策确定、可观测，并通过资源争用测试 |
| 13 | 平台如何判断发布健康且值得上线 | 第62～69章 | Evaluation gate、metrics/log/trace 关联、容量和成本模型 | Production readiness Review 和安全威胁模型 | 发布决策可追溯到证据、策略、owner 和 rollback action |
| 14 | 完整平台能否承受负载与故障 | 联查 Part III～V | 集成 Capstone、压测、故障注入并修复一个瓶颈 | RFC、ADR、benchmark、incident report 和架构讲解 | 其他工程师能够复现系统并挑战结论 |
| 15 | 已学知识能否承受对抗性面试 | 错误记录和薄弱章节 | 只修复 Mock 暴露的缺口 | 4 次 Mock：Coding、AI 深度、System Design、英文 Behavioral | 重复失败项均有书面修正和重新测试 |
| 16 | 所有证据是否达到 Staff 级评估要求 | 全部 Portfolio Review | 从干净环境跑通 setup 到 benchmark 并冻结结果 | 双语简历、8 个故事、项目讲稿、问题库和公司清单 | 简历中的每项结论都有代码、数据、设计或生产证据 |

## 5. Capstone 契约

在 `labs/ai-platform-capstone/` 下建设一个一体化项目：

```text
Training Job
-> Checkpoint / Adapter
-> Evaluation Gate
-> Model Registry
-> KServe / Gateway
-> vLLM or SGLang
-> GPU Admission and Scheduling
-> Metrics / Logs / Trace / Cost
-> Canary / Rollback
```

实现职责如下：

- Python 负责 workload generation、训练实验、Evaluation、benchmark、容量计算和故障注入。
- Go 负责一个有实际意义的 control plane 组件：admission、queueing、scheduling policy 或 Kubernetes reconciliation。
- 模型执行和编排机制继续由现有框架负责。项目只集成和测量，不编写没有工程价值的玩具替代品。
- 所有单机多卡结果必须明确标注。除非以后在真实集群测量，否则多节点 RDMA、InfiniBand 和 failure domain 相关结论均视为尚未验证。

必须形成以下 Staff 级材料：

1. Architecture 与 request/state flow 图；
2. 包含替代方案、拒绝方案和演化路线的 RFC；
3. SLO 与容量模型；
4. 包含原始结果的可复现 benchmark report；
5. 一份故障注入 incident report；
6. Security、tenancy、cost、rollout 和 rollback 分析。

## 6. 面试策略

70% 的外企准备重点包括：

- 在 16 周内持续进行限时 Coding 和计算机基础训练；
- 在 System Design 中先澄清需求，再进行定量推导；
- 从第 9 周开始进行英文项目讲解与 Behavioral 训练；
- 重点表达量化影响、owner 边界、分歧处理和跨团队技术领导力。

30% 的国内大厂准备重点包括：

- 快速完成机制推导并承受连续追问；
- 熟悉框架源码路径、GPU / Runtime 内部机制和生产排障；
- 能准确说明项目细节、性能适用条件和故障分析。

正式投递从第 16 周完成后开始。第 9～16 周使用不熟悉的面试官或全新题目进行 Mock，以弥补没有真实面试反馈的问题。

## 7. 最终就绪标准

- 完成一个可复现的端到端 Capstone，以及 GPU/CUDA、Distributed Training、Inference、Platform Control 四类独立 Labs。
- 完成 64 道精选 Coding 题和至少 16 次限时练习。
- 完成 12 道完整 AI System Design，覆盖容量、SLO、State、故障、安全、成本和演化。
- 完成 8 个 Senior-to-Staff 项目或 Behavioral 故事，且都有中英文版本。
- 完成 8 次 Mock Interview，其中至少 4 次全英文。
- 能在 45 分钟内完成 Training Platform、LLM Serving 或 Multi-tenant GPU Platform 设计，不隐藏关键假设。
- 简历中的每项性能或业务影响都能指向代码、测量、运行证据，或明确标注的既有生产结果。
