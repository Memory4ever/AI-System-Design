# 第63章 Monitoring

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** Metrics 如何回答系统是否健康。

## 本章要回答的问题

Metrics 能回答哪些平台问题，又会丢失什么？为什么“GPU utilization 很高”不能证明系统健康？如何把 Part IV 的 TTFT、TPOT、goodput 与平台 SLO 连接起来？

本章的核心判断是：**Monitoring 用低成本聚合 measurements 描述系统在时间窗口内是否满足目标。它适合趋势、告警和控制环，不负责还原单次请求的完整因果链。**

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

## 本章在知识树中的位置

Monitoring 为第 53 章 Evidence Plane 提供聚合 observed state，并向 autoscaling、admission、cost 与 incident response 提供输入。下一章转向离散事件：当指标告诉我们“出问题了”，Logging 如何留下可查询证据。

## 自检问题

1. 为什么应从 SLO 反推 metrics？
2. GPU utilization 高为什么不证明有用工作多？
3. Histogram 与 Summary 的聚合语义有何差异？
4. 为什么 request ID 不应作为 metric label？
5. Goodput 约束了 throughput 的什么缺陷？
6. Missing metric 与 zero value 为什么要区分？

## 小结

Monitoring 用受控成本提供系统健康的统计视图。它适合发现趋势和驱动控制环，却不能解释某一次失败的完整上下文。下一章用 structured logs 保存事件证据。

## Review notes

本章复用 Part IV 已冻结的 TTFT、TPOT、SLO attainment 与 goodput，不重新定义推理机制；第 64 章拥有事件，第 65 章拥有因果链。

Primary-source 与官方入口：

- Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- Prometheus histograms and summaries: https://prometheus.io/docs/practices/histograms/
- OpenTelemetry Metrics: https://opentelemetry.io/docs/concepts/signals/metrics/
