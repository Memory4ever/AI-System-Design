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

Fragmentation 也要区分两种 owner。Job 的 GPU 数与 node 形状天然不整除时，剩余空间是 workload-induced；调度器把本可合并的 jobs 分散到更多 partial nodes，则是 scheduler-induced。只最大化当前可行 placement 会把后者藏进“总空闲 GPU”指标。一个更可审计的策略以 anchor node 表示可复原的紧凑布局，在 arrival/departure 时显式执行 place/remove/compact，并把迁移成本和 gang feasibility 纳入决定。它用重排、状态迁移与控制面开销换取未来可用的连续拓扑；作者 trace/testbed 不能证明任意 workload 都值得 compact。迁移昂贵、作业不可抢占或空闲量主要来自不可避免形状时，应保留 best-fit/queueing，而不是为了指标强制搬迁。

失败后的 restart 也不是固定常数。只按瞬时 goodput 排序会反复延后长等待 job，并忽略 checkpoint load 已经支付的成本；age key 与分解后的 restart factor 可以分别表示等待债务、productive time 和 reload overhead，再与 goodput 一起进入每轮效用。它改善的是 starvation/restart-aware frontier，不授予某套权重跨集群通用性。OAK 的 12-GPU 仿真与 4-V100 实验只支持披露 failure/load 模型；预测漂移、不可抢占 job 或硬优先级存在时，应回退显式 reservation、FIFO/DRF 或保守 restart policy。

价格波动再把这个效用扩展到跨区域的 spot 寿命与 deadline：单区域、不迁移的策略在 checkpoint 昂贵或可选区域少时仍合理；有足够 slack 的固定 gang 才可能把整组迁移成本摊回便宜资源。[SkyNomad 的受限控制器](https://arxiv.org/html/2601.06520v1)用探测与存活时间估计剩余 spot 寿命，将 cold start、checkpoint 传输/egress 费用和剩余进度的 deadline 压力一起比较，并用迟滞避免反复切换；寿命预测不是容量预约，便宜区域也必须满足数据位置和完整 gang 的可行性。Checkpoint 的一致性与恢复语义仍由 Ch35 负责，调度器只决定何时承担迁移。其保守 on-demand 回退依赖事先已知工作量、启动时间界及 on-demand 始终可用等前提，不是无条件 deadline 保证；探测、预测漂移、大 checkpoint 或很小 slack 会吃掉节省，应保留单区域 reservation/on-demand 路径并报告其真实成本。有限云实验与 trace 模拟不能证明全局最优或任意工作负载的收益。<!-- source-family:SF-2026-ARXIV-2601-06520 -->

<!-- source-family:arxiv:2609.18519v1 -->
<!-- source-family:arxiv:2609.19024v1 -->

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

静态 quota 和借用规则容易解释，却难让租户私有的当期 SLO/迁移代价与运营方私有的供电、冷却、维护和拓扑压力持续协调。一条条件分支允许租户在运行中提出保留、放弃或重议现有 allocation 的 proposal，由运营方把物理压力折成价格或回收信号，并保留最终匹配、事务与紧急硬约束仲裁权。价格传递的是受限资源压力，不赋予租户设备所有权，也不证明报价等于真实效用或分配全局公平。<!-- source-family:SF-2026-ARXIV-2604-22509 -->

持续重议会支付 profile、控制面通信、价格波动与 checkpoint/migration 成本；重配置太贵时，原固定 quota 或先来先服务仍可能更稳妥。租户报价不可信、硬电力/故障约束需要立即执行，或作业不可安全迁移时，operator 的 quota、lease、硬安全和保守 reclaim 必须优先于软价格。作者 trace/profile 模拟覆盖所测 LLM serving、训练与 batch analytics，不是生产云 A/B，也未证明 request-tail SLO、策略真实性或隐私保证。

## GPU Sharing 的语义不同

几种“共享”不能互换：

| 机制 | 隔离/分割 | 适合场景 | 主要风险 |
| --- | --- | --- | --- |
| MIG | 硬件级实例 | 可预测的小型 workload | profile 碎片与重配置 |
| time-slicing | 时间复用 | 开发、低占用任务 | 显存与性能隔离弱 |
| MPS | 进程并发执行 | 可配合的 CUDA workloads | fault/isolation 语义受限 |
| application batching | 应用层合并 | 在线推理 | 需要 runtime 理解请求 |

第 46 章 continuous batching 是 application scheduling，不是 cluster GPU sharing。二者都提高利用率，但作用层不同。

计算分割也不自动形成时间隔离：即使按 SM 划分进程的执行范围，共享的功率上限、频率变化与其他资源压力仍可能改变共置后的完成时间。验收时因此要同时记录 SM 布局、功率与时钟状态、并发模型和到达负载，而不能把独占条件下测出的稳定提交频率当成 deadline 合同。有限样本中没有 timeout，只支持该 profile 人口下的观察，不是 worst-case execution time 证明；边缘 GPU 上六个分类模型的共置结果尤其不能直接外推到 LLM Serving。更高功率余量与更大内存带宽同时变化的设备对照，也不能只归因于其中一个因素。这条责任链增加遥测、并发对照、重新校准与保守 headroom 成本；若共置后仍不能满足时间预算，应降低并发、调整布局或退回独占，而不是从计算分区推导未测得的时序或安全保证。<!-- source-family:SF-2026-ARXIV-2601-07600 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2610-02522:start -->
短周期 latency-critical 工作与 best-effort ML 共置时，还需把 SM 选择与 HBM traffic 控制分开。预创建互补 compute contexts 可以把运行时变更缩成 slot 边界的后续 launch 选择，但已经运行的 blocks 仍留在原 context，不是任意线程抢占；经验 latency profile 与 tail reserve 也不是硬 deadline 证明。Disjoint SMs 仍共享 HBM，一条协作分支让每个高优先级 block 在需要带宽的区间独立置位共享 bitmap，最后一个 protected block 清位后才解除保护；只用 kernel-wide 单 bit 会因 blocks 不同速而提前解除。

可获得 PTX 的低优先级 kernel 再在 memory-producing threads 都会经过的安全 gate 前轮询，暂停的是新 traffic，不能撤回 in-flight requests；HBM-light 区间可以继续执行。Profile、binary rewrite、同步与 co-tenant 降速因此属于同一分享合同，而非硬件安全隔离。[Beaver 的 Aerial/vLLM 受限评价](https://arxiv.org/pdf/2610.02522)支持该组合在披露单 GPU workload 下保护 p99.9，若干全栈与跨设备切片仍只达到 miss rate低于0.1%，不授绝不超时、多租户恶意行为或任意 opaque kernel 都可改写。缺少合法 PTX/gate、profile 越界、co-tenant 不协作或严格硬隔离优先时，独占/MIG 与保守固定分区继续成立；下一段的 launch 粒度控制并不代替这条 HBM 责任链。
<!-- semantic-body-binding:SF-2026-ARXIV-2610-02522:end -->

时间复用还受正在执行的 kernel 粒度约束：高优先级请求到达，并不意味着低优先级工作可以立即停下。一条软件分支先把合法 kernel 的 block grid 切成较短子任务，以 PTX 中的 offset 保持原 blockIdx 语义，再按目标设备 profile 选择能饱和计算或带宽的最小粒度；host 只保持有限的待执行队列，以预测的 kernel tick 推进下一次 launch。这里回收的是后续 launch 的权限，等待边界仍受当前子 kernel、队列深度与预测误差约束，不是中断任意运行线程的硬件抢占。cuBLAS/cuDNN 无可提取 PTX 时须另换兼容的 CUTLASS 实现，persistent kernel、跨 block 同步等路径不能直接切分，仍需重构或保留原执行器。

细分会增加 launch 成本并降低低优先级吞吐；若观察到高优先级工作间有大 bubble，可以临时合并回较大 kernel，却同时取消了原细粒度等待边界，突发请求必须重新接受较长等待。因而 splitter、profile、tick/队列与 consolidation 策略要作为同一 sharing contract 验收，并把预测失准、库替换和低优先级减速计入成本。显存 offload 的带宽竞争又是另一条压力，不能从计算回收推出地址或故障隔离。受限 trace/SLO 下的收益不授任意 GPU、kernel 或生产尾延迟保证；无法满足合法拆分与等待预算时，原 kernel、保守时间复用或独占 GPU 仍是回退路径，故障域继续由下述独立责任链处理。

<!-- source-family:SF-2026-ARXIV-2605-26461 -->

MPS 之类的进程级共享在 workload 彼此可信、错误可通过重启整卡恢复时，能以很低的管理成本提高利用率；但当多租户进程共享 SM 与上下文后，“地址访问隔离”和“致命设备错误后的恢复”成为两条不同责任链。MMU 可以限制越界地址影响，却不能保证 fatal SM fault 后其他 client 的 runtime state 仍可继续使用。

因此 production sharing 需要显式 fault-domain contract：硬件/驱动拥有地址隔离，node runtime 负责检测 fatal fault、冻结受影响 allocation、重建 MPS client 与 context，scheduler 再依据恢复结果决定 rebind 或迁移。它以 recovery controller、重建延迟和更复杂的健康状态换取更细故障域；若驱动无法证明 client-level containment，或 workload 无 checkpoint / replay，MIG、独占 GPU 或整节点失败回退仍更可靠。单一软件栈的 fault-injection 结果不能外推为所有 GPU、driver 与 kernel 组合的隔离保证。

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

语义控制器不应直接进入 kernel hot path。一个有界分支先由人和 verifier 发布已验证策略库，运行时 Agent 只能选择 `policy_id`，内核再通过范围检查执行已有动作；reasoning plane 拥有 proposal，kernel owner 保留 execution authority。它用有限策略空间换安全与常数级切换，无法处理库外情形；策略不足或 selector 不可信时，应回退固定 scheduler，而不是允许模型生成任意 kernel 行为。

<!-- source-family:SF-2026-ARXIV-2609-12276 -->

### Power Budget 是分层资源契约

只给每张 GPU 设置独立 power cap，在单租户、固定供电域中容易实施；机架、集群与租户同时受不同
上限约束后，局部调节可能让上层预算不可行。调度器需要在每个控制周期求一个满足层级 capacity、
租户 entitlement 与设备边界的可行分配，再把 setpoint 交给节点执行；budget owner 拥有约束，
optimizer 只拥有分配 proposal，硬件 telemetry 反馈下一周期。该路径用求解与控制延迟换可组合预算，
并会引入测量漂移、不可行输入与震荡；规模小或预算独立时，静态 cap 仍更可靠。作者模拟/实验支持
其算法范围，不证明任意 GPU fleet 的功耗—性能关系或生产稳定性。
<!-- source-family:SF-2026-ARXIV-2605-01837 -->

把 GPU 数量当唯一容量会遗漏供电链的四个不同 owner：设计 provisioning 决定理论上限，rack validation 证明安装边界，operational cap 留出可靠性余量，runtime scheduler 才能消费瞬时 swing。调度器应依据可用功率而非铭牌功率 admission，并保留测量延迟与降级策略；收益是提高基础设施利用率，代价是 telemetry、控制稳定性和故障域耦合。功率波动不可测或业务不能容忍 throttle 时，静态保守 cap 仍更合理。单个大规模集群的测量不能外推为所有硬件和冷却拓扑。

<!-- source-family:SF-2026-ARXIV-2605-24461 -->

### 可回收资源需要 Lease 与 Reclaim Protocol

机会型 host/member 资源若只有“可用/不可用”标签，回收会在 checkpoint、网络迁移和流量切换之间制造竞态。更完整的契约包含 lease、成员身份、目标网络、reclaim notice 与 deadline；scheduler 负责选择目标，workload controller 负责 checkpoint，traffic owner 负责连接排空。收益是利用闲置资源，代价是恢复状态、控制面消息和尾延迟增加；短任务或不可迁移状态仍应使用保留资源。现有证据支持一种 voluntary resource protocol，不证明跨集群回收天然无损。

<!-- source-family:SF-2026-ARXIV-2605-28872 -->

```text
Chapter 56 inference scheduler
  request / token / KV / iteration, millisecond scale

Chapter 63 GPU scheduler
  Pod / gang / device / node / queue, seconds-to-minutes scale
```

二者通过 autoscaling、resource requests、topology 和 metrics 连接。把 token queue 直接塞进 kube-scheduler 会产生高频耦合；让 runtime 完全看不到 cluster topology 又会产生错误 placement。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

### Cross-API Sharing 要同时拥有 Scheduling Domain 与 Address Space

time-slicing、MPS 与 MIG 都假设 runtime 与隔离边界相对明确；当 CUDA 与 Vulkan 等不同 API 共享同一设备时，空间复用还会引入跨 API 的 allocation、同步与地址可见性问题。平台不能只把两类进程放在同一 GPU 上就宣称共享成功：scheduler 要拥有可审计的 resource partition，driver/runtime 要拥有 synchronization 与 memory-safety contract，workload identity 还必须绑定 API、context 和 device state。

这种分支可以提高碎片利用率，却把隔离证明、故障归因和 driver 兼容性变得更难。任何同步超时、越界可见性或驱动不支持都应回退为单 API、time-slicing 或硬隔离；MIG 等旧方案在强租户隔离和可预测 SLO 优先时仍然更合适。

<!-- source-family:SF-VUDA-CUDA-VULKAN-SHARING -->

### 从削峰响应到 Grid-responsive Compute

只把功率当容量上限，在电价和供电条件平稳时足够；MW 级 AI/HPC 负载接入电网后，能源可用性会在秒级到小时级变化。Scheduler owner 需要把 job deadline、checkpoint/elasticity、设施安全边界和 grid signal 分成不同时间尺度，由三层 controller 决定降频、迁移或延后，而不是让电网直接控制 workload。收益是把 compute 变成可验证的柔性负载，代价是吞吐损失、控制复杂度与 SLA 风险；信号丢失或 safety island 触发时必须回退本地安全功率。exact-v1 只支持 GridPilot 披露的 cluster/grid interface 与实测环境，不证明任意数据中心或电网均有相同收益。<!-- source-family:SF-2026-ARXIV-2605-26384 -->

### 共享 Power Cap 会把独立训练 Job 耦合成相位系统

两个训练 Job 即使没有通信，也可能在共享功率上限下相互影响：一方进入高功耗 phase 后触发 throttling，改变另一方的 step duration，长期反馈可能让 phase 锁定并放大尾部。Scheduler 不能只把平均功率相加，而应观察 phase、throttling、step-time 与 cap event 的联合 trace，再决定错峰、功率配额或隔离。

错峰可降低同步峰值，却可能延长单 Job 完成时间；动态 cap 又会增加控制振荡。负载低、功率 headroom 足或硬件隔离时，普通 bin packing 仍成立。作者的共置实验只证明特定模型、GPU 与 cap 设置下的 coupling mechanism，不是任意集群的固定现象。

<!-- source-family:SF-2026-ARXIV-2607-19638 -->

### 没有可证稳定性，就不能承诺有限等待时间

多租户 GPU admission 不能只依据当前空闲卡数。对同时消耗 GPU、显存、带宽或拓扑的 workload，应先用 vector packing 估计有效 server count，再判断到达率与服务分布是否处于稳定区；只有稳定且模型假设可接受的队列，才有资格给出等待界。unfeasible workload 应触发重配置、降级或拒绝，而不是输出看似精确的 ETA。

队列模型以可解释 bound 换来分布、独立性和服务时间假设；M/G/k 或 stochastic domination 的理论结果不等于生产 SLA。系统应持续用观测校准假设，在 burst、相关失败或资源碎片超界时撤销 bound，回退保守 admission 与实测 percentile。

<!-- source-family:SF-2026-ARXIV-2607-28223 -->

## 本章在知识树中的位置

本章建立 GPU scheduling 的稳定问题模型。下一章用 Volcano 映射 batch/gang/queue 机制，再用 KAI 观察 AI-native queue 与 GPU sharing 的另一种工程组合。

## 从机制演进到系统设计

GPU scheduler 最初按卡数和显存做 placement；异构 accelerator、MIG、拓扑与动态并行出现后，资源必须表达 capability、locality、sharing mode、health 和可重配置成本。调度器选择 placement，runtime 决定算子和通信，二者通过可验证 profile 交接，而不是互相猜测。

更精细的 typed resources 提高利用率，却增加碎片、reconfiguration latency、profile drift 和 fairness问题。capability 不可验证、拓扑快速变化或隔离要求严格时，应回退整卡、静态 pool 或保守 quota。理论可放置不等于满足训练/推理 SLO。

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

### Reclaimable Sharing 需要 Entitlement 与 Interference 的联合 Assurance

静态配额易解释却降低利用率；可回收共享允许借用空闲 GPU，但调度器必须同时追踪 entitlement deficit、reclaim latency/preemption risk 与 colocated interference。借用者拥有可撤销 lease，不取得永久容量；归还路径与受影响作业的 SLO evidence 必须先于更高 oversubscription。<!-- source-family:SF-2026-ARXIV-2609-16682 -->

预测式 reclaim 提高利用率也会放大误判、checkpoint 成本和性能干扰。模型置信不足、作业不可安全抢占或集群差异超出校准范围时，应回退硬配额、隔离 placement 或保守 headroom；作者结果不能提供通用 oversubscription 比例。

## Review notes

- `SF-2026-ARXIV-2604-22509`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.22509v1) §2.3、§4.1–4.5、§5.1/5.5、§7；Daily 2026-04-27。只吸收租户私有效用与运营方私有物理约束通过持续重议接口分权的条件分支。8–23% 属作者 trace/profile 模拟及其同租户 autoscaler/预算对照；高重配置成本可退近 FCFS，不作生产 SLO、strategy-proofness 或 privacy 保证。未复现实验，待独立写后与整日 Gate。

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

### Daily integration evidence trace

#### Source-specific Review notes

- SF-2026-ARXIV-2606-25098: `arXiv:2606.25098v1`; exact-v1 URL=`https://arxiv.org/html/2606.25098v1`; Method=`https://arxiv.org/html/2606.25098v1 — §3 Architecture for Power-Flexible AI Infrastructure`; Evaluation=`https://arxiv.org/html/2606.25098v1 — §4 Experimental Demonstration; 5 Grid Services; 6 Geo-Load Shifting`; Non-proof=`130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26341**：Primary `arXiv:2606.26341v1`；Method `https://arxiv.org/html/2606.26341v1 — §Many Problems One GPU batching and nonlinear-optimization execution design`；Evaluation `https://arxiv.org/html/2606.26341v1 — §GPU scaling experiments across problem families`；未证明边界 `https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

- `SF-2026-ARXIV-2601-04071` — Daily `2026-01-09`；[Hummingbird exact-v1](https://arxiv.org/html/2601.04071v1) §4.2–4.4、§5、§6.1–6.3。原6分因sharing合法执行粒度缺口深入受影响证据，只采用PTX/grid splitter、profile/tick有限队列、bubble consolidation与unsupported原路径分责。A10080GB/SXM4、CUDA12.6/禁DVFS、INT8 llama.cpp与BurstGPT replay/有限LP workload、exclusive P99 TTFT/TPOT合同，不授任意硬抢占、闭源库皆可拆、无条件400µs或生产SLO；LithOS为作者重建非原artifact。未运行代码或复现；root必要原源/owner写前通过，jan01_v3实际顺读正文、前后邻接与源注，非作者POST通过（此次POST不冒称重读root已核原源）。

- `SF-2026-ARXIV-2601-07600` — Daily `2026-01-14`；[Peformance Isolation exact-v1](https://arxiv.org/html/2601.07600v1) §III、§IV-A–C/Alg1、§V-B–D。原2+2+2=6，设计反证受影响内容深入；仅采用 compute partition 与 power/frequency 压力、有限 IMS profile 与 deadline 权限分账。作者以1000次中最差5次均值初估、提高直至超时、退回并检验3×1000次，是有限稳定频率测试而非 WCET。A10040GB/CUDA12.1/PyTorch2.4.1 与 Jetson Nano/AGX/JetPack6.2/TensorRT 的六个 ImageNet 分类模型配置不同，AGX同时改变功率及带宽；未测分类 accuracy、LLM/KV/Serving SLO，precision/warmup/输入分布/重复置信区间 Not Disclosed。不采用 exclusive-SM、MIG 保证或单变量功率因果外推；未运行代码/复现。root 实际必要原源与当前 owner 写前通过，并实际顺读正文、前后邻接与源注，非作者 POST 通过。

- `SF-2026-ARXIV-2601-06520` — Daily `2026-01-14`；[SkyNomad exact-v1](https://arxiv.org/html/2601.06520v1) §4.1–4.7、§5、§6.1–6.2.5。2+2+3=7，仅采用固定 gang 的 spot 寿命/迁移开销/egress/deadline 效用分账与条件回退，不承担 checkpoint correctness 或无条件 deadline/最优保证。AWS Qwen3-4B/14B，4L4/8A100/4A10G，30h工作/45h截止、100/500GB checkpoint、6min cold start；GCP H100 14day 与 AWS V100 trace 模拟20jobs不冒充生产承诺。无 slack 全回退、单 region 无选址增益、区域数收益饱和、大 checkpoint 反侧保留；headline 10% 不能覆盖部分11/12%结果，地理 eligibility 非法规合规认证。精度、训练 batch 与完整质量/成本未披露，未运行实现/复现；root 必要原源与实际 owner 写前通过，root 已实际顺读正文/前后邻接/末注，非作者 POST 通过，日级 Gate 待验。
