# 第59章 GPU Scheduler

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** GPU 是稀缺资源，调度决定利用率和公平性。

## 本章要回答的问题

为什么把 GPU 注册成 `nvidia.com/gpu: 8` 仍不足以调度 AI workload？GPU scheduler 如何同时处理设备能力、拓扑、gang、队列、公平性与碎片？它与第 52 章推理调度的边界在哪里？

本章的核心判断是：**GPU scheduling 是受硬约束的多维 placement 与时间分配问题。先保证设备、拓扑和 gang 可行，再在 queue、fairness、utilization 和 SLO 之间优化；任何单一利用率指标都会丢失关键约束。**

## GPU 不是同质标量

普通 CPU workload 常允许较连续的资源份额。GPU 请求背后可能包含：

- device model、HBM capacity 与 compute capability；
- full GPU、MIG slice、time-slicing 或其他 sharing mode；
- NVLink/NVSwitch、PCIe、NUMA 与 RDMA topology；
- driver、CUDA/runtime compatibility；
- local data/cache 与 model artifact locality；
- 多 Pod 必须同时启动的 gang。

两个节点都显示 8 GPU，不代表能运行同一个 8-way TP job。跨慢速网络拼出 8 张卡，数学上满足 count，性能上可能不可接受。

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

## Fragmentation 为什么会发生

假设两台节点各有 8 GPU。四个 2-GPU 任务被平均铺到两台节点，每台剩 4 GPU。集群尚有 8 GPU 空闲，但一个要求单节点 8 GPU 的任务无法运行。

这就是 capacity 与 allocatable shape 的差异。调度器需要在 spread、bin-pack 与未来需求之间权衡：

- bin-pack 可释放完整节点，便于大 gang 与缩容；
- spread 可降低单节点故障和资源争用；
- topology-aware packing 可提高 collective 性能；
- 过度保留大块资源会降低短期利用率。

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

第 42 章 continuous batching 是 application scheduling，不是 cluster GPU sharing。二者都提高利用率，但作用层不同。

## DRA 带来的资源表达

传统 extended resource 主要表达计数。Kubernetes Dynamic Resource Allocation 允许通过 `ResourceClaim`、device attributes 和 driver 描述更丰富的设备请求与分配。

截至 2026 年，DRA API 与具体 GPU driver 能力仍需按 Kubernetes/driver 版本核验。它改善资源表达，不自动提供 queue fairness、gang 或 AI-specific policy。

## 与推理 Scheduler 的边界

```text
Chapter 52 inference scheduler
  request / token / KV / iteration, millisecond scale

Chapter 59 GPU scheduler
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

## 小结

GPU scheduler 的任务不是简单填满设备，而是在设备/拓扑硬约束下形成可执行 workload，并维持长期公平与可接受抢占成本。下一章进入 Volcano，查看这些原则如何被表达为 PodGroup、Queue、actions 与 plugins。

## Review notes

本章只定义通用机制，不绑定具体 scheduler。它承接第 56 章的 training gang、第 52 章的 inference state，并为第 60～61 章提供统一比较坐标。

Primary-source 与官方入口：

- Kubernetes scheduler: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
- Kubernetes Scheduling Framework: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
- Dynamic Resource Allocation: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- Dominant Resource Fairness: https://www.usenix.org/conference/nsdi11/dominant-resource-fairness-fair-allocation-multiple-resource-types
