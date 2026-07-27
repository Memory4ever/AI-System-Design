# 第61章 KAI Scheduler

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** 面向 AI 工作负载的资源编排与队列治理。

## 本章要回答的问题

KAI Scheduler 与通用 kube-scheduler、Volcano 的差异应怎样理解？它为什么强调 queue hierarchy、fair share、GPU sharing 和 workload consolidation？选择 scheduler 时应该比较哪些不变量？

本章的核心判断是：**KAI Scheduler 是把 AI workload 的组织公平、GPU sharing 与 placement efficiency 放入一个 Kubernetes-native scheduler 的工程实现；它没有改变 gang、quota、topology 和 preemption 的基本矛盾。**

> 时效边界：KAI Scheduler 在 2026 年已由独立 `kai-scheduler` GitHub organization 维护，能力演进较快。本章按 2026 年 7 月官方仓库描述，生产使用需锁定 release、CRD 与 GPU Operator/DRA 兼容矩阵。

## 为什么 AI Cluster 需要更强的 Queue 模型

共享集群常同时运行：

- 小型 interactive jobs；
- 可 checkpoint 的长训练；
- 多节点 gang；
- 长期 inference deployments；
- 可以共享 GPU 的低利用 workload。

只按 Pod priority 会把组织级资源关系压缩成一个数字。KAI 用 hierarchical queues 表达 parent/leaf、quota、priority 和 fair sharing，让 workload 归属先成为明确输入。

## Queue Hierarchy 与 Fair Share

可以把组织结构映射为：

```text
root
├─ research
│  ├─ team-a
│  └─ team-b
└─ production
   ├─ training
   └─ inference
```

Parent queue 表达一组团队的总资源政策，leaf queue 接收 workload。空闲份额可被其他 queue 使用，提高 work conservation；当 owner 需要资源时，再按 reclaim/preemption policy 收回。

Fair share 不等于每个时刻绝对平均。它是在时间窗口内结合 guarantee、weight、demand 和 borrowing 的政策。对在线 inference，还应先满足最小可用 capacity，再讨论剩余公平。

## Placement、Consolidation 与 Fragmentation

KAI 强调 GPU workload placement 和 consolidation，其目标通常是：

- 把可放在一起的 workload 聚合，释放完整节点；
- 为大 gang 保留更可用的 topology shape；
- 减少 cloud autoscaler 无法缩容的半空节点；
- 在 sharing workload 中提高设备利用率。

但 consolidation 可能增加同节点干扰和故障 blast radius。平台应按 workload class 设置 packing policy，而不是对所有任务最大化密度。

## GPU Sharing 不是免费容量

KAI 支持 GPU sharing，但共享后的 capacity 必须按实际机制解释。逻辑 fractions 不等于物理隔离：

- 显存是否独立限制？
- kernel execution 是否互相干扰？
- 一个 workload fault 是否影响其他 workload？
- device metrics 能否归属到 tenant？
- scheduler request 是否与 runtime 可见设备一致？

对 production Serving，application batching 或 MIG 可能更可预测；对 notebook/开发任务，time-based sharing 可能更经济。选择来自 SLO 与隔离需求，而非“共享率越高越好”。

## Gang 与 Workload Signatures

多 Pod AI job 仍需要 gang/cohort semantics。KAI 的 workload signatures 等优化可以减少大批同构 Pod 的重复 scheduling work，但它是调度性能优化，不改变每个 workload 的资源与拓扑约束。

Scheduler explainability 同样重要：为什么 pending、为何选中某 node、为何被抢占，应该通过 Kubernetes Events 或其他 evidence 可查询。没有原因码，fairness 只能靠猜测。

## DRA 与设备能力

官方当前列出针对 NVIDIA ComputeResources 的 DRA 支持。DRA 可让 request 表达 device attributes 和 claim，而 scheduler 仍需解决：

- queue admission；
- gang atomicity；
- placement score；
- borrowing/reclaim；
- failure recovery。

因此 DRA 是 resource contract，不是完整 AI scheduling policy。

## 如何与 Volcano 做工程选择

不应问“哪个功能更多”，而应验证：

| 维度 | 要验证的问题 |
| --- | --- |
| API contract | 与现有 Operator/Kueue/CRD 如何集成 |
| Gang | admission、reservation、partial failure 语义 |
| Fairness | hierarchy、borrowing、reclaim 是否符合组织政策 |
| GPU modes | full/MIG/sharing/DRA 的真实隔离 |
| Topology | NVLink/RDMA/node group 是否可表达 |
| Scale | scheduler latency、throughput 与 failure behavior |
| Operations | upgrade、events、metrics、debug 与 rollback |

基准必须使用真实 workload distribution，而不是只测空集群每秒调度多少 Pods。

## 本章在知识树中的位置

第 59 章给出问题，第 60～61 章给出两种 runtime mapping。Scheduler 只负责资源 admission/placement；第 62 章回到 lifecycle evidence，讨论 MLflow 如何记录实验、模型和评估，使“用了多少 GPU”能关联“产生了什么结果”。

## 自检问题

1. 为什么 Pod priority 不能表达完整组织公平？
2. Hierarchical queue 如何支持资源借用？
3. Consolidation 的收益和风险是什么？
4. GPU sharing 为什么必须说明隔离语义？
5. DRA 改善了什么，又没有解决什么？
6. 比较 Volcano 与 KAI 时应使用哪些稳定维度？

## 小结

KAI Scheduler 将 hierarchy、fair share、GPU placement 与 sharing 组合为 AI-oriented scheduler。正确选择不来自产品名，而来自 workload、隔离、拓扑和运营契约是否匹配。

## Review notes

本章不声称 KAI 在所有维度优于 Volcano，只映射其当前官方能力，并强调版本边界。第 60、61 章共享第 59 章的比较坐标。

官方入口：

- KAI Scheduler repository: https://github.com/kai-scheduler/KAI-Scheduler
- KAI quickstart and queues: https://github.com/kai-scheduler/KAI-Scheduler/tree/main/docs
- Kubernetes DRA: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
