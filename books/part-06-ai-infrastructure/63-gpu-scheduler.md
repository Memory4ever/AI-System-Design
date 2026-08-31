# 第63章 GPU Scheduler

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-GPU-SCHEDULER`
**Legacy Chapter:** Ch59
**Status:** Draft

**Roadmap Intent:** GPU 是稀缺资源，调度决定利用率和公平性。

## 本章要回答的问题

为什么把 GPU 注册成 `nvidia.com/gpu: 8` 仍不足以调度 AI workload？GPU scheduler 如何同时处理设备能力、拓扑、gang、队列、公平性与碎片？它与第 56 章推理调度的边界在哪里？

本章的核心判断是：**GPU scheduling 是受硬约束的多维 placement 与时间分配问题。先保证设备、拓扑和 gang 可行，再在 queue、fairness、utilization 和 SLO 之间优化；任何单一利用率指标都会丢失关键约束。**第 36 章说明 collective algorithm 必须映射到真实 topology；本章从控制面回答 scheduler 怎样为这种映射保留可行的 device、node、switch 与 failure-domain placement。

## GPU 不是同质标量

普通 CPU workload 常允许较连续的资源份额。GPU 请求背后可能包含：

- device model、HBM capacity 与 compute capability；
- full GPU、MIG slice、time-slicing 或其他 sharing mode；
- NVLink/NVSwitch、PCIe、NUMA 与 RDMA topology；
- driver、CUDA/runtime compatibility；
- ECC/Xid、thermal throttling、link degradation 与设备健康状态；
- local data/cache 与 model artifact locality；
- 多 Pod 必须同时启动的 gang。

两个节点都显示 8 GPU，不代表能运行同一个 8-way TP job。跨慢速网络拼出 8 张卡，数学上满足 count，性能上可能不可接受。

## 为什么调度会成为 AI 平台的核心问题

平台采购或接入的 GPU 数量只是 installed capacity。真正能转化为训练进度或在线 SLO 的容量，会经过多层收缩：

```text
C_installed
>= C_healthy_and_compatible
>= C_topology_feasible
>= C_policy_admitted
>= C_useful
```

`C_healthy_and_compatible` 排除了故障设备和不满足 architecture、HBM、driver/runtime 要求的资源；`C_topology_feasible` 只保留能组成目标 TP/PP/EP 或 gang shape 的设备；`C_policy_admitted` 再应用 queue、quota、priority 与 isolation；`C_useful` 最终要求 workload 真正取得训练进度或兑现 Serving SLO，而不是只显示 GPU 已分配。

这些 `C` 不是脱离 workload 的固定集群常数，而是针对某个 workload contract 和某个资源快照计算的可行容量。同一批设备对 single-GPU notebook 可能充足，对要求单 NVSwitch domain 的 8-way TP workload 却可能为零。

因此，“集群还有 64 张空卡”不等于某个 64-GPU job 可调度，“GPU utilization 很高”也不等于平台产出了有效工作。部分 gang 占卡等待、跨慢链路 collective、热降频、错误重试或在线请求大量违反 SLO，都可能让 allocated capacity 与 useful capacity 分离。

调度决策还具有放大效应。训练作业可能运行数小时或数周，一次错误拓扑会持续支付通信税；在线副本放在错误设备或 failure domain 上，会把局部放置问题转化为 tail latency 和可用性问题。抢占也不是免费回收整数张卡：训练需要保存 optimizer、RNG 和 data progress，推理需要处理已加载权重、engine、adapter cache、in-flight request 与 KV state。

多租户平台最终还必须通过调度兑现组织政策。配额、借用、公平、优先级、reservation 和 preemption 若不进入统一资源决策，只能停留在文档约定。GPU scheduler 因而不是 AI Platform 的一个边缘插件，而是把 workload contract 映射为物理执行条件的核心控制面。

## Filter、Score 与 Bind

Kubernetes scheduler 的基本过程是：

```text
unscheduled Pod
→ Filter feasible nodes
→ Score feasible nodes
→ Reserve / Permit
→ Bind
```

AI workload 在此基础上增加 job-level admission。单 Pod placement 可行，不代表整个 gang 可行；现在放下一张卡，也可能让未来 8-card job 永远无法形成连续拓扑。

可将决策写成约束优化：

```text
maximize
  w1 * useful_utilization
+ w2 * fairness
+ w3 * locality
- w4 * fragmentation
- w5 * preemption_cost

subject to
  device compatibility
  memory and topology requirements
  gang minimum
  queue quota / policy
  isolation constraints
```

权重不是普适常数。训练、interactive notebook 和 online inference 具有不同等待成本与抢占代价。

### 从 Pod Placement 到 Workload Snapshot

单 Pod 的 Filter/Score/Bind 在成员彼此独立时最简单；gang、分布式训练或有依赖的服务若逐 Pod 决策，早到成员
可能占住资源，而剩余成员永远不可行。Workload-aware scheduling 因而需要把静态 template 与一次调度尝试的
runtime snapshot 分开：

```text
versioned workload template
→ instantiate PodGroup / dependency state
→ freeze one cluster snapshot
→ evaluate whole-group feasibility and score
→ atomic commit or reject / retry
```

同一 snapshot 避免成员在不同 cluster state 上各自“可行”，atomic commit 避免 partial placement；代价是 search
space、snapshot staleness、reservation contention、rollback 与 fairness。Template owner 决定 workload intent，
scheduler 拥有 placement attempt，resource drivers 拥有 inventory，queue policy 仍决定谁先获得机会。成员独立、
资源充足或低延迟单 Pod admission 更重要时，普通 Pod scheduling 仍合理。Kubernetes 1.36 的
Workload-Aware Scheduling v1alpha2 是实验性实现证据，不证明 dependency-heavy placement 已有完整搜索或
production fairness guarantee。

## Fragmentation 为什么会发生

假设两台节点各有 8 GPU。四个 2-GPU 任务被平均铺到两台节点，每台剩 4 GPU。集群尚有 8 GPU 空闲，但一个要求单节点 8 GPU 的任务无法运行。

这就是 capacity 与 allocatable shape 的差异。调度器需要在 spread、bin-pack 与未来需求之间权衡：

- bin-pack 可释放完整节点，便于大 gang 与缩容；
- spread 可降低单节点故障和资源争用；
- topology-aware packing 可提高 collective 性能；
- 过度保留大块资源会降低短期利用率。

大规模 fabric 中，“同一节点/同一交换域”还可能不足以表达连续拓扑。调度器可以把可用 nodes 组织成
topology segments，在 gang placement 时优先选择满足规模与链路约束的 segment，再决定 pack/spread：

```text
device and failure-domain inventory
→ versioned topology segments
→ gang-size / communication-shape feasibility
→ segment selection
→ node placement and bind
```

Segment 减少跨低带宽边界的 collective traffic，却会因 nodes-down、库存变化和多作业竞争产生 stale segment、
内部碎片与 starvation。Slurm topology-aware scheduling 的大规模 simulator 只在作者 20,000-GPU、job trace、
七天与 failure contract 下支持该 policy 分支，不证明真实生产效率或所有 topology 都应采用固定 segment。

## Gang、Queue 与 Fairness

`Gang scheduling` 解决“任务最小成员能否共同运行”。Queue 解决“谁先获得机会、可借多少、何时归还”。Fairness 解决“长期共享是否符合组织政策”。

常见公平模型包括 quota、weighted fair share 与 Dominant Resource Fairness。GPU 集群中不能只看 GPU 数量；CPU、memory、network、storage bandwidth 也可能成为 dominant resource。

借用空闲 quota 能提升利用率，但需要 reclaim/preemption 规则。抢占一个训练任务的成本取决于最近 checkpoint；抢占一个 serving replica 的成本取决于剩余 capacity、KV state 和 SLO。Scheduler 必须看到 workload class，不能把 victim 只表示成“释放 8 GPU”。

## GPU Sharing 的语义不同

几种“共享”不能互换：

| 机制 | 隔离/分割 | 适合场景 | 主要风险 |
| --- | --- | --- | --- |
| MIG | 硬件级实例 | 可预测的小型 workload | profile 碎片与重配置 |
| time-slicing | 时间复用 | 开发、低占用任务 | 显存与性能隔离弱 |
| MPS | 进程并发执行 | 可配合的 CUDA workloads | fault/isolation 语义受限 |
| application batching | 应用层合并 | 在线推理 | 需要 runtime 理解请求 |

第 46 章 continuous batching 是 application scheduling，不是 cluster GPU sharing。二者都提高利用率，但作用层不同。

## 从固定 Job Shape 到 Elastic Configuration Portfolio

传统 scheduler 接收一个固定 GPU request，只决定放在哪里；但 training/inference job 可能存在多个合法配置，
例如不同 replica、memory mode、batch 或 single-GPU sharing。若 workload owner 先固定 shape，scheduler 看不到
“换一种配置便可避免碎片或共置干扰”的选择。

```text
workload-declared configuration portfolio
→ feasibility under memory / topology / SLO
→ shadow-price choice across jobs
→ interference-aware placement
→ drain / checkpoint / migrate when configuration changes
→ observe actual performance and update predictor
```

这要求严格分责：workload template 声明语义等价的可选 shape；optimizer 选择 portfolio；scheduler bind devices；
runtime 实施 memory limit、sharing 和迁移。预测器不能把“可能共置”变成安全事实，migration 也必须绑定 checkpoint、
in-flight request 与 rollback。ElastiCo 的 64×A100、single-GPU configuration scope 证明的是 joint choice 的受限可行性，
没有覆盖 multi-GPU collective、predictor drift、migration failure 或 online tail SLO。固定 shape 在 distributed
collective 强耦合、迁移昂贵或 performance isolation 优先时仍成立。

## DRA 带来的资源表达

传统 extended resource 主要表达计数。Kubernetes Dynamic Resource Allocation 允许通过 `ResourceClaim`、device attributes 和 driver 描述更丰富的设备请求与分配。

Kubernetes 1.34 的 core DRA APIs 升为 stable `resource.k8s.io/v1`，说明设备调度的基础对象已
从“Pod 消耗整数个 opaque resource”演进为：workload 声明 claim 与约束，driver 通过
`ResourceSlice` 广告设备属性，scheduler 选择 allocation，kubelet/driver 再完成 node-local
prepare。这里的核心收益是 **request 与具体 device identity 解耦**，而不是 GA 自动意味着
所有 GPU sharing 能力稳定。

同一版本的扩展恰好说明稳定级别必须拆开：

- Core DRA 已 GA，可作为设备 claim/allocation 的基础 contract。
- Consumable capacity 在 1.34 仍是 alpha；它允许多个 claims 按 memory、bandwidth 等
  capacity share 同一设备，并要求总消费不超过 driver 广告容量。
- Resource health reporting 仍是 alpha；driver 通过 kubelet 把 `Healthy`、`Unhealthy` 或
  `Unknown` 写入 Pod/container status，提供诊断事实，但不自动定义驱逐或恢复 policy。

这条演进把 GPU sharing 从预定义 partition 再推进到多维容量分配，却引入新的 owner 和
failure modes：driver 必须准确广告/执行 capacity，scheduler 的 admission state 必须与设备
实际状态一致，health 从变化到控制动作之间还可能有延迟。MIG 等硬 partition 仍适合需要强
隔离和固定 profile 的 workload；consumable capacity 更灵活，但其隔离、计量和超售语义取决
于具体 driver。

截至 2026 年，DRA API 与具体 GPU driver 能力仍需按 Kubernetes/driver 版本、feature gate
和 device class 核验。它改善资源表达与可观测性，不自动提供 queue fairness、gang、性能
隔离或 AI-specific policy。

## 与推理 Scheduler 的边界

```text
Chapter 56 inference scheduler
  request / token / KV / iteration, millisecond scale

Chapter 63 GPU scheduler
  Pod / gang / device / node / queue, seconds-to-minutes scale
```

二者通过 autoscaling、resource requests、topology 和 metrics 连接。把 token queue 直接塞进 kube-scheduler 会产生高频耦合；让 runtime 完全看不到 cluster topology 又会产生错误 placement。

## 本章在知识树中的位置

本章建立 GPU scheduling 的稳定问题模型。下一章用 Volcano 映射 batch/gang/queue 机制，再用 KAI 观察 AI-native queue 与 GPU sharing 的另一种工程组合。

## 自检问题

1. 为什么 GPU count 相同不代表节点等价？
2. Pod placement 可行为什么不代表 gang 可行？
3. capacity fragmentation 与真实空闲量有何不同？
4. Gang、queue 和 fairness 分别解决什么问题？
5. MIG、time-slicing 与 continuous batching 为什么不能混为一谈？
6. 推理 scheduler 与 GPU scheduler 的时间尺度有何不同？
7. 为什么 DRA core GA 不等于 consumable capacity 与 health policy 都已稳定？
8. 为什么 installed capacity、topology-feasible capacity 与 useful capacity 不能混为一谈？

## 小结

GPU scheduler 的任务不是简单填满设备，而是在设备/拓扑硬约束下形成可执行 workload，并维持长期公平与可接受抢占成本。下一章进入 Volcano，查看这些原则如何被表达为 PodGroup、Queue、actions 与 plugins。

<!-- recovered-daily-20260624:PLATFORM-GPU-SCHEDULER:start -->
## 2026-06-24 evidence integration — PLATFORM-GPU-SCHEDULER

相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25082**：MIG scheduler 同时拥有 configuration 内作业放置与 configuration 间 repartition；controller 以 power/performance state、partition action 与 reward 决定何时重分，而不是把 MIG 当静态 SKU。 主要是 simulation 与测得的 MIG power characteristic；repartition downtime、state migration、真实混合作业 SLO 和多节点 GPU fabric 未闭合，收益不足时保留静态 partition。
- **SF-2026-ARXIV-2606-25098**：grid signal 成为 cluster scheduler 的外部 control input，power telemetry/model 回写可用 curtailment budget；priority job 保留服务级别，elastic job 承担降载或跨地域迁移。 130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。

### Source-specific Review notes

- SF-2026-ARXIV-2606-25082: `arXiv:2606.25082v1`; exact-v1 URL=`https://arxiv.org/html/2606.25082v1`; Method=`https://arxiv.org/html/2606.25082v1 — §IV Proposed Solution; Scheduling Within Configuration; Dynamic Re-Partitioning`; Evaluation=`https://arxiv.org/html/2606.25082v1 — §V Experiments and Results`; Non-proof=`主要是 simulation 与测得的 MIG power characteristic；repartition downtime、state migration、真实混合作业 SLO 和多节点 GPU fabric 未闭合，收益不足时保留静态 partition。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25098: `arXiv:2606.25098v1`; exact-v1 URL=`https://arxiv.org/html/2606.25098v1`; Method=`https://arxiv.org/html/2606.25098v1 — §3 Architecture for Power-Flexible AI Infrastructure`; Evaluation=`https://arxiv.org/html/2606.25098v1 — §4 Experimental Demonstration; 5 Grid Services; 6 Geo-Load Shifting`; Non-proof=`130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
<!-- recovered-daily-20260624:PLATFORM-GPU-SCHEDULER:end -->

<!-- recovered-daily-20260625:PLATFORM-GPU-SCHEDULER:start -->
## 2026-06-25 evidence integration — PLATFORM-GPU-SCHEDULER

- **SF-2026-ARXIV-2606-26341**：`Many Problems One GPU batching and nonlinear-optimization execution design` 所定义的源特定机制用于把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26341**：Primary `arXiv:2606.26341v1`；Method `https://arxiv.org/html/2606.26341v1 — §Many Problems One GPU batching and nonlinear-optimization execution design`；Evaluation `https://arxiv.org/html/2606.26341v1 — §GPU scaling experiments across problem families`；未证明边界 `https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
<!-- recovered-daily-20260625:PLATFORM-GPU-SCHEDULER:end -->

## Review notes

本章只定义通用机制，不绑定具体 scheduler。自检答案回填增加了从 installed capacity 到 useful capacity 的约束收缩链，说明 GPU 调度为何是平台控制面的核心问题。它承接第 60 章的 training gang、第 56 章的 inference state，并为第 64～65 章提供统一比较坐标。

Primary-source 与官方入口：

- Kubernetes scheduler: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
- Kubernetes Scheduling Framework: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
- Dynamic Resource Allocation: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- Kubernetes v1.34 DRA GA: https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/
- DRA consumable capacity: https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/
- DRA resource health: https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/
- NVIDIA Slurm topology-aware scheduling simulation（Official Engineering Evidence）:
  https://developer.nvidia.com/blog/?p=117052
- Dominant Resource Fairness: https://www.usenix.org/conference/nsdi11/dominant-resource-fairness-fair-allocation-multiple-resource-types
- ElastiCo（elastic configuration portfolio 与 interference-aware placement；Status: Experimental）:
  https://arxiv.org/abs/2608.07971
