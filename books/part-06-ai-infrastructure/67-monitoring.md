# 第67章 Monitoring

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-MONITORING`
**Legacy Chapter:** Ch63
**Status:** Draft

**Roadmap Intent:** Metrics 如何回答系统是否健康。

## 本章要回答的问题

Metrics 能回答哪些平台问题，又会丢失什么？为什么“GPU utilization 很高”不能证明系统健康？如何把 Part V 的 TTFT、TPOT、goodput 与平台 SLO 连接起来？

本章的核心判断是：**Monitoring 用低成本聚合 measurements 描述系统在时间窗口内的 observed health 与 SLI/SLO state。它适合趋势、告警和控制环，不负责定义业务质量，也不负责还原单次请求的完整因果链。**

第 66 章已经区分了“记录事实”与“判断是否满足用途”：Evaluation 定义 subject、distribution、scorer 与 decision；Monitoring 持续采集低成本 observed state，并可承载 evaluation result 的聚合趋势，但不重新定义质量标准。

## 先定义目标，再选择可测信号

容易采集的指标不一定重要。应从用户与平台契约反推：

```text
user objective
→ SLI definition
→ measurement and aggregation
→ SLO target and window
→ alert / control action
```

例如聊天服务的 SLI 可包含成功率、TTFT、TPOT 和正确 model revision；batch training 则更关心 queue time、job completion、checkpoint progress 与有效 GPU time。两者不能共享一个“平均 latency”解释。

## 四层指标

| 层次 | 示例 | 回答的问题 |
| --- | --- | --- |
| Model/quality | evaluation score、fallback、safety violation | 能力是否仍符合用途 |
| Service/runtime | TTFT、TPOT、queue、KV、tokens/s | 请求执行是否达标 |
| Resource | GPU/CPU/HBM/network/storage | 资源哪里饱和 |
| Platform/business | lead time、goodput、cost、SLO attainment | 系统是否产生有效结果 |

只观察最底层会产生错觉：GPU busy 可能在 recompute、部分 gang 等待或无效请求上消耗。

Resource utilization 还不能表达“有多少时间在等资源”。CPU、memory 与 I/O 的 Pressure Stall Information
把 runnable work 因 contention 无法推进的时间暴露为 pressure evidence，使平台能区分 idle、busy-but-progressing
与 busy-and-stalled。Unsupported platform 必须省略该 signal，不能报告零；`missing` 与 `no pressure` 是不同状态。
Pressure 仍不等于 root cause，也不能单独触发 eviction：sampling window、cgroup/node scope、workload phase、
throttling 与 application goodput 必须联合解释。

类似地，telemetry、health verdict 与 attestation 是三层证据。Agent/exporter 可以报告 sensor state，health service
可按 policy 聚合判断，attestation 只证明指定 software/boundary 的身份与完整性；任何一层都不能自动证明设备
会故障、模型结果正确或 workload 应迁移。NVIDIA Fleet Intelligence 作为版本化实现案例支持这类分层，不支持
把厂商 predictive-failure 效果外推为通用因果结论。

### Autonomy 不是一个纯模型指标

生产 Agent 的连续运行时长、tool-call 数、用户中断率和任务完成率可以形成 autonomy telemetry，
但这些观测共同受到模型能力、产品 UX、用户信任、任务分布、权限和 timeout policy 影响：

```text
observed autonomy
= model behavior
× task opportunity
× tool and permission surface
× user intervention policy
× product/runtime limits
```

因此，Anthropic 2026 年基于大规模产品交互的 autonomy measurement 更适合作为
`deployment-system observation`，不能被解释为模型固有的单一 autonomy level。session
长度和 tool calls 是 proxy；采样、单厂商流量、classifier 误差和产品变化都必须进入版本与
不确定性说明。若要用于 release decision，还需由第 66 章把这些在线观测与受控 task
evaluation、风险 slice 和业务 outcome 联合起来。

### 从单次 Query 指标到 Session-level Search Trajectory Sensor

单次 retrieval latency、document count 与 hit rate 适合观察 backend health，却看不见 Agent 是否反复查询、
持续缩窄、切换 facet，或把先前 evidence 带入下一步。Multi-step search 因此需要一个绑定 sessionization
规则的 trajectory view：

```text
timestamped query and retrieval parameters
→ versioned sessionization / continuity classifier
→ intent and reformulation labels
→ repetition / exploration / specialization distributions
→ evidence-traceability proxy across steps
→ budget, stop or investigation signal
```

例如可以统计新 query terms 有多少能在累计 retrieved evidence 中做 lexical trace。这个指标可解释、便宜，
却只说明字符串来源可能相关，不证明 Agent 理解、正确使用或引用了证据；repetition 也可能是合理 retry，
不是自动失败。Session cutoff、classifier/judge、retrieval replay corpus 和 tokenization 都必须版本化，原始
query/evidence 属于高敏高基数 trace，不能塞入 metrics labels。

这类 sensor 可为 repetition-aware stop、intent-adaptive retrieval budget 和 evaluation sampling 提供输入，
但不得独立驱动高风险终止或发布结论。单一 API/provider population、缺失 underlying agent identity、LLM
taxonomy 与 lexical proxy 都构成 selection/measurement boundary；日志去标识也不自动消除 sequence-level
隐私风险。固定 retrieval budget 在短任务、缺少可靠 classifier 或可预测性优先时仍是合理基线。

## Rate、Errors、Duration 与 Saturation

服务侧可用 RED：Rate、Errors、Duration；资源侧可用 USE：Utilization、Saturation、Errors。LLM 需要再加状态信号：

- request/token rate 与 workload distribution；
- TTFT/TPOT 的 p50/p95/p99；
- active/pending requests；
- KV allocation、reuse、eviction、offload；
- Prefill/Decode work 与 batch occupancy；
- admission reject/preemption；
- model/adapter/revision identity。

指标必须带单位、类型和 workload conditions。`tokens/s` 未说明 input/output mix、模型、硬件与 SLO 时没有可比性。

## 平均值为什么危险

对于延迟分布：

```text
mean = sum(x_i) / N
```

均值可以被大量短请求掩盖，无法描述少量严重超时。分位数更接近 tail，但不能对不同实例的预计算 quantiles 直接求平均。

Histogram 记录 bucket/count/sum，可在聚合后估计 quantile；Summary 通常在 client 端计算 quantiles，跨实例不易聚合。具体选择要结合精度、成本和 backend 支持。

## Cardinality 是资源预算

Metric system 为每组 label values 维护 time series。若把 `request_id`、`user_id` 或原始 prompt 放入 labels：

```text
series_count
≈ product(cardinality of each label dimension)
```

存储、内存和 query cost 会迅速失控。高基数字段应进入 logs/traces，metrics 只保留可聚合维度，如 tenant class、model revision、status/reason。OpenTelemetry 当前 metrics SDK 还定义 cardinality limit 与 overflow behavior，说明该约束已进入 instrumentation contract。

## 隐私约束会改变可观测性的数据平面

传统 telemetry 默认后端能看见每条原始事件，再在查询时聚合。对跨设备或高敏数据，这个
前提本身可能不可接受。演进路径可以写成：

```text
central raw-event collection
→ client-side minimization / redaction
→ secure aggregation
→ attested zero-trust aggregation
→ only policy-approved aggregates leave the boundary
```

这不是给现有 dashboard 增加一个加密开关，而是改变 **谁拥有原始状态**。在 secure
aggregation 与受 attestation 约束的执行环境中，单条输入不应被后端重建，查询者只得到满足
阈值和策略的聚合结果。收益是降低平台对中央服务和运维人员的信任；代价是 ad-hoc query、
单请求 debugging、低频 slice 和数据纠错能力受限，密钥、证明、dropout 与查询预算又成为
新的控制面状态。

这类机制与 redaction 是 `Layering / Dependency`，不是替代关系：入口过滤减少敏感字段，
聚合协议限制后端能恢复什么，retention 与 access policy 再约束聚合物。Google 2026 年
Zero-Trust Aggregation 是这一设计分支的官方案例，但其安全结论只在声明的密码学协议、
TEE/attestation、客户端和查询威胁模型下成立。

## SLO 与 Error Budget

SLO 应说明事件、有效请求、目标和窗口。例如：

```text
SLI = requests meeting success, TTFT and TPOT conditions
      / eligible requests

error_budget = 1 - SLO_target
```

Goodput 可表示单位资源内满足 SLO 的有效工作。它不替代质量、安全和成本指标，而是防止通过牺牲 tail latency 制造高 throughput。

Alert 应指向可执行动作。单个瞬时阈值容易抖动；多窗口 burn-rate 更适合判断 error budget 是否快速消耗。

## Monitoring 也会改变系统

高频 scrape、过细 histogram、昂贵 GPU exporter 和大量 labels 都有成本。控制环消费 metrics 时还要考虑：

- freshness 与 scrape delay；
- aggregation window；
- missing data；
- counter reset；
- autoscaling feedback oscillation。

缺指标与“指标为零”必须区分，否则 exporter 故障会被解释成负载消失。

### Collective Telemetry：先聚合定位，再短时展开

训练 collective 的单次 event trace 最适合 forensic analysis，却会随 communicator、rank 和 operation 快速增长；
只观察 application throughput 又无法判断问题位于 compute、collective algorithm、protocol 还是 network path。
更可操作的演进是把两种证据分层：

```text
participant-local collective events
→ per-GPU / rank periodic aggregates by op, size bucket, algorithm and protocol
→ fleet dashboard and anomaly trigger
→ temporary verbose trace for the affected slice
```

Metrics owner 只保存低基数 aggregate；communicator/rank identity、GPU UUID、NCCL/plugin revision、dump interval
与 exporter freshness 必须可追溯到 Logging/Trace 的细粒度证据。聚合能降低存储和 dashboard 成本，却丢失单次
operation lineage；verbose 模式会迅速放大 cardinality 与 profiler overhead，只应按 incident window 开启。
Collective bandwidth 与网络异常同期出现只提供相关性，仍需结合 participant-local logs、network counters、
topology 和 application goodput 才能定位 root cause。NCCL Inspector 的 Prometheus mode 是这条机制的官方案例，
其“低开销”主张不能脱离 profiler-on/off、模型、拓扑、并发和 tail SLO contract 外推。

## 本章在知识树中的位置

Monitoring 承接第 66 章对 Evaluation/Observability 的边界，为第 57 章 Evidence Plane 提供聚合 observed state，并向 evaluation sampling、autoscaling、admission、cost 与 incident response 提供输入。下一章转向离散事件：当指标告诉我们“出问题了”，Logging 如何留下可查询证据。

在隐私数据流上，职责还要再分一次：第 72 章的 policy-bound detector 决定原始内容中哪些
字段应在入口被最小化；本章决定剩余 telemetry 以何种 aggregation、attestation 和 retention
contract 被观察；第 66 章再判断这些受限观测是否足以支持能力、安全或发布结论。入口过滤、
zero-trust aggregation 与 Evaluation 是 `Layering / Dependency`，任何一层都不能用“看不到原文”
推导出匿名、合规或证据充分。

## 自检问题

1. 为什么应从 SLO 反推 metrics？
2. GPU utilization 高为什么不证明有用工作多？
3. Histogram 与 Summary 的聚合语义有何差异？
4. 为什么 request ID 不应作为 metric label？
5. Goodput 约束了 throughput 的什么缺陷？
6. Missing metric 与 zero value 为什么要区分？
7. 入口 redaction、zero-trust aggregation 与 Evaluation 为什么不能互相替代？

## 小结

Monitoring 用受控成本提供系统健康的统计视图。它适合发现趋势和驱动控制环，却不能解释某一次失败的完整上下文。下一章用 structured logs 保存事件证据。

## Review notes

本章复用 Part V 已冻结的 TTFT、TPOT、SLO attainment 与 goodput，不重新定义推理机制；第 68 章拥有事件，第 69 章拥有因果链。

Primary-source 与官方入口：

- Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- Prometheus histograms and summaries: https://prometheus.io/docs/practices/histograms/
- OpenTelemetry Metrics: https://opentelemetry.io/docs/concepts/signals/metrics/
- NVIDIA NCCL Inspector Prometheus mode:
  https://developer.nvidia.com/blog/real-time-performance-monitoring-and-faster-debugging-with-nccl-inspector-and-prometheus/
- Kubernetes Pressure Stall Information metrics:
  https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/
- Anthropic, "Measuring agent autonomy": https://www.anthropic.com/research/measuring-agent-autonomy
- Google Research, "Private analytics via zero-trust aggregation":
  https://research.google/blog/private-analytics-via-zero-trust-aggregation/
- Agentic Search in the Wild（session trajectory 与 evidence-traceability proxy；作者观测边界）:
  https://arxiv.org/abs/2601.17617
