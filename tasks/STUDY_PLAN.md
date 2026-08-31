# AI System 24 周双轨学习计划

## 目标

本计划面向每周 10～12 小时的长期学习，同时服务 AI Infra 面试，但不被面试题库驱动。

24 周结束时：

- 84 章全部通过 L2，能闭卷解释问题、机制、trade-off 和知识树连接；
- 核心机制达到 L3～L5，有推导、源码或实验依据；
- GPU/CUDA、Distributed AI、RL Infrastructure、Inference Runtime 各有一个 L6 Anchor；
- 至少完成一个跨 Training → Serving → Platform → Agent 的可复现 Capstone；
- 每个“掌握”声明都能回到 `tasks/progress.yaml` 中的证据，而不是 Books 篇幅。

## 双轨结构

### Track A：章节主干

第 1～18 周按知识依赖完成 84 章第一轮。每章至少完成 L1～L2，表中更高目标分阶段推进。

### Track B：问题纵深

第 19～22 周不再顺章阅读，而是用四个问题串联多个章节：

1. Tensor shape 为什么决定 GPU kernel 和模型架构的效率边界？
2. 模型、状态和通信怎样跨设备分工并在失败后恢复？
3. 偏好优化怎样改变分布，rollout/runtime 怎样保证训练证据可信？
4. 请求、KV、scheduler 和 workers 怎样共同决定 Serving SLO？

## 每周执行协议

每周只选择一个中心问题，按下面顺序执行：

```text
闭卷基线
→ Books / primary source
→ 推导或源码追踪
→ 写下实验预测
→ 受控实验 / scenario challenge
→ 解释 prediction gap
→ 压缩为原则与决策表
→ 更新 progress.yaml
```

默认时间预算：

| 工作 | 时间 |
| --- | ---: |
| Books 与 primary sources | 3h |
| 推导或源码 hot path | 2h |
| 实验、profiling 或 failure injection | 3～4h |
| 压缩、图示与证据整理 | 1～2h |
| 中英文闭卷讲解 | 1h |

如果实验超过预算，只完成最小可证伪路径并记录 blocker；不得用没有 control group 的长时间运行换取虚假 L5。

## 24 周路线

| Week | 中心主题 | 章节 | 实验 / 任务 | 本周交付 |
| ---: | --- | --- | --- | --- |
| 1 | 学习合同与 AI System 地图 | Ch1～3 | Lab 00；审计已有成果，不自动计分 | 基线 Level、知识树定位测试、第一份周复盘 |
| 2 | 学习、表示、Scaling 与能力 | Ch4～8 | Lab 01；训练/测试反例 | 最小训练循环、表示边界和 scaling 外推反例 |
| 3 | 系统演化与输入表示 | Ch9～13 | BPE、embedding、RoPE 数值练习 | Text→embedding+position 的 shape/identity contract |
| 4 | Transformer 主体 | Ch14～18 | Lab 02 | 可逐层对齐的 Decoder-only checkpoint |
| 5 | 自回归状态、MoE 与长上下文 | Ch19～22 | Lab 03/04 的 CPU baseline | Cache parity、sampling replay、router imbalance 证据 |
| 6 | 多模态到环境行动 | Ch23～26 | Lab 05/06 最小路径 | modality/state identity 与 action feedback trace |
| 7 | Data、Pretraining、SFT、LoRA | Ch27～30 | Lab 07；审计现有 LoRA run | data/objective/adapter/checkpoint lineage |
| 8 | RLHF、PPO、GRPO、DPO | Ch31～34 | Lab 08 toy branch | 五类监督对象、状态成本和 proxy failure 对照 |
| 9 | Checkpoint、collective 与 TP | Ch35～37 | Lab 09 第一阶段 | recovery parity、collective trace、TP shape 预算 |
| 10 | PP、ZeRO 与训练 runtime | Ch38～41 | Lab 09 第二阶段 | 并行状态账本和组合选择表 |
| 11 | 请求、Prefill、Decode 与 KV | Ch42～45 | 完成 Lab 03 | 单请求 runtime state machine 与 phase metrics |
| 12 | Batching、paging、speculation 与 engines | Ch46～50 | Lab 10；vLLM/TensorRT-LLM 源码入口 | 单 engine controlled benchmark 与 commit invariants |
| 13 | 分布式推理与 SLO 调度 | Ch51～56 | Lab 11 | routing/KV transfer/PD/scheduling break-even |
| 14 | AI Platform control plane | Ch57～62 | Lab 12 第一阶段 | artifact/workload/service/traffic desired-state trace |
| 15 | GPU 调度、Evaluation 与观测 | Ch63～68 | Lab 12/13 第一阶段 | queue/fairness/evaluation Gate 和 metrics/log boundary |
| 16 | Trace、Cost、Tenancy 与 Production | Ch69～73 | 完成 Lab 13 | 可追溯发布、成本模型、threat model 与 rollback |
| 17 | Agent information state 与 tools | Ch74～78 | Lab 14 | context/RAG/memory/tool authority 对照 |
| 18 | Planning 到 Agent Platform | Ch79～84 | Lab 15 | durable workflow、multi-agent 成本和协议边界 |
| 19 | GPU / CUDA 纵深 | 回读 Ch14、16～17、21、37、43～44、49、54 | GEMM/Attention shape、profiler、kernel path | Ch49 L6 challenge；GPU bottleneck decision tree |
| 20 | Distributed AI 纵深 | 回读 Ch21、35～41、52～56、63～65 | collective/EP/TP/PD/topology/failure | Ch36 L6 challenge；跨训练与推理通信预算 |
| 21 | RL Infrastructure 纵深 | 回读 Ch27～35、66 | dataset→rollout→reward→update→checkpoint | Ch33 L6 challenge；算法与 runtime failure tree |
| 22 | Inference Runtime 纵深 | 回读 Ch19～22、42～56 | vLLM/SGLang request trace 和 SLO diagnosis | Ch50 L6 challenge；未知 workload 诊断 |
| 23 | End-to-End Capstone | 横跨 Ch27、35、42、56、59、61、66、73、81、84 | Lab 16 | 可复现 lifecycle、五类 failure 和 evidence chain |
| 24 | Compression 与最终验收 | 全部 | 闭卷抽检、双语讲解、System Design Mock | Level 审计、知识债务、下一轮 12 周计划 |

## 阶段门禁

### Week 6 Gate：模型机制主干

- Ch1～26 全部至少 L2。
- Token→Transformer→Decode 的 shape/state 连续。
- 至少两个 prediction 与 observation 不一致，并形成更新后的 mental model。

### Week 10 Gate：能力生产

- Ch27～41 全部至少 L2。
- 能区分 data/objective/optimizer/system/evaluation signal。
- checkpoint 和并行策略均有 state ownership，而不是框架功能描述。

### Week 18 Gate：能力交付、治理与 Agent

- Ch42～84 全部至少 L2。
- Training artifact 能连续追踪到 Serving、Platform evidence 和 Agent action。
- Labs 10～15 至少各完成一条 correctness baseline；未到 E2 的不计 L5。

### Week 22 Gate：四柱纵深

- 四个 L6 Anchor 均通过 fresh-context challenge。
- 每个方向至少有一个 profiler/trace、一个 failure injection 和一个替代设计。
- 能解释什么时候不选择当前最熟悉的框架或优化。

### Week 24 Gate：计划完成

- `progress.yaml` 有 84 个唯一 Stable Node，全部 `current_level >= 2`。
- 所有达到 L5/L6 的章节都有实验或 challenge 证据链接。
- Lab 16 可从干净环境复现；失败和 toy-workload 边界没有被隐藏。
- 随机抽取 12 章闭卷讲解，其中四柱各至少两章。

## Paper、Books 与学习状态的关系

- Paper 只有在解决当前 question、挑战 prediction 或修正 mental model 时计入学习证据。
- Daily/Weekly 的 `Must Read`、Source Review 或 Books Integration 不自动提升个人 Level。
- 学习后发现 Books 缺口，可以单独进入 Research→Books 流程；本周 Checklist 不以产生 Books diff 为完成条件。
- 每四周执行一次 Compression Pass：`5 principles + 10 trade-offs + 3 formulas/state machines + 1 design map`。

## 中断与恢复

- 一周投入不足 6 小时时，不把未完成项压缩到下一周并行堆叠；下一周先关闭前一周 Gate。
- 硬件不可用时，先完成 CPU/reference、trace simulation 或 quantitative model，并将 GPU 结论标记 `blocked`。
- 上游框架 major version 改变时，相关 L4～L6 设为 `refresh_due`，L1～L3 的长期机制不自动失效。
- 连续两周未通过 Gate 时，减少目标 Level，不减少 correctness 和 evidence 要求。
