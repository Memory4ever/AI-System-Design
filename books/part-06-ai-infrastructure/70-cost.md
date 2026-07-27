# 第70章 Cost

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-COST`
**Legacy Chapter:** Ch66
**Status:** Draft

**Roadmap Intent:** GPU 成本、推理成本、训练成本和平台 ROI。

## 本章要回答的问题

AI 成本为什么不能只看 GPU 采购价或利用率？如何把训练、推理、闲置、失败和平台开销归因到有效结果？降低单 token 成本为什么可能让总成本上升？

本章的核心判断是：**AI cost 是资源在时间上的占用与机会成本，必须在质量、可靠性和 SLO 约束下按可归属结果计算；脱离 outcome 的利用率或单价会驱动错误优化。**

## 资源时间是共同底座

基础归因可写为：

```text
resource_cost
= Σ(resource_time_i × effective_rate_i)

effective_rate
= acquisition_or_cloud_rate
 + power/cooling/network/storage
 + operations and reserved-capacity effects
```

共享设备、预留实例和自建集群没有天然“正确单价”。平台应记录采用的 rate model 与时间窗口，避免财务口径和工程口径暗中不同。

## 训练成本

一次训练的成本不只包含成功 run：

```text
training_cost
= useful_compute
 + data preparation
 + checkpoint I/O
 + communication overhead
 + failed/retried work
 + idle gang time
 + evaluation
```

提高 checkpoint 频率增加 I/O，却减少故障后重算；更大 batch 可能提高吞吐，却改变 optimization 与模型质量。成本优化不能越过 Part IV 的训练语义。

更有意义的指标是“达到目标质量的总成本”，而非单 step 最便宜：

```text
cost_to_quality_target
= total experiment family cost until accepted evidence
```

## 推理成本

### Agent Trajectory 的 Token 数必须折算为 State-dependent Work

Tool-integrated reasoning 会在每次 tool pause 后携带更长 Context 继续执行；若 KV 不能跨 round 复用，历史 token
会重复 Prefill，之后每个 Decode token 又在更长 KV 上工作。因此“总输入+输出 token”不能表示实际计算：

```text
sum over rounds(
  newly prefetched or recomputed context work
  + decode tokens × active KV length
)
+ tool / network / idle / coordination time
```

Prefill Token Equivalents 可以作为 analytical proxy，把 Context growth、cache reuse 与 tool schedule 统一到近似
work unit；但系数依赖 model、hardware、precision、batch/concurrency、kernel、KV policy 和 lengths，不能当 latency
或账单真值。短单轮、稳定 cache hit 或直接测量完备时，普通 token/accelerator-time 指标仍合理。平台应并列保存
proxy、measured device time、wall-clock、tool cost 与 SLO，而不是用一个静态系数覆盖它们。

在线成本应绑定 workload：

```text
cost_per_request
= allocated resource-time / completed requests

cost_per_output_token
= allocated resource-time / generated output tokens

cost_per_good_request
= total serving cost / requests meeting quality and SLO
```

只看 output token 会忽略 Prefill；只看 request 会忽略长度。应同时保留 prompt/output lengths、cache hit、model/quantization、hardware、concurrency 与 SLO。

## 利用率与有效利用率

高 GPU utilization 可能来自：

- useful training/inference；
- recompute；
- rejected speculative tokens；
- padding/imbalance；
- job 无进展但 kernel busy；
- 低价值或重复请求。

因此：

```text
effective_utilization
= useful work satisfying target contract
 / allocatable resource-time
```

定义 useful work 需要业务和质量参与，不能由 GPU exporter 单独决定。

## Unit Economics 与总需求反弹

量化、batching、cache reuse 和更小模型可降低单位成本。但更便宜的调用会诱发更多调用、更长 context 或更多 Agent loops，总账单可能上升。

平台需要同时看：

- unit cost；
- demand volume；
- quality/SLO；
- marginal value；
- budget burn rate。

Cost guardrail 应支持 request/tenant/model/workload class，而不是只在月底按 namespace 分摊。

## Showback、Chargeback 与公平

Showback 提供可见性，chargeback 影响真实预算。归因键应沿平台 identity graph：

```text
tenant
→ project
→ run / service
→ model revision
→ resource allocation
→ outcome evidence
```

共享 model server、prefix cache 和 multi-tenant batch 使归因不是简单按 Pod。可以按 token work、reserved capacity 与 shared overhead 分层分摊，并明确近似误差。

## ROI 的边界

平台 ROI 不应只计算节省的 GPU：

- lead time 是否下降；
- successful change rate 是否提高；
- incident/rollback 是否更快；
- policy/security evidence 是否减少风险；
- 用户是否采用 paved road；
- 平台运营成本是否可控。

这些指标不能硬压成一个精确货币数，但需要和平台投入共同 Review。

## 本章在知识树中的位置

Cost 消费第 67～69 章 evidence，并反馈到 scheduler、autoscaling、model selection 和 lifecycle policy。下一章进入多租户：只有 identity 与 isolation 完整，成本归因和公平政策才可执行。

## 自检问题

1. 为什么 GPU 单价不是完整 AI cost？
2. `cost_to_quality_target` 比单 step 成本多考虑什么？
3. 为什么 cost per token 必须绑定 workload？
4. 高 utilization 与 effective utilization 有何差别？
5. 单位成本下降为什么可能让总成本上升？
6. 共享 serving 的成本归因为什么只能近似？

## 小结

成本是资源时间、结果与约束的关系。平台应优化满足质量和 SLO 的有效结果，而不是孤立追求 GPU busy 或最低 token 单价。下一章为这些归因和政策建立租户边界。

## Review notes

- Prefill Token Equivalents（trajectory state-cost proxy；Status: Experimental）:
  https://arxiv.org/abs/2604.05404

本章复用第 56 章 goodput、第 63 章 allocation 和第 67～69 章 evidence，不编造硬件价格或通用 ROI 数字。

Primary-source 与实践入口：

- FinOps Framework: https://www.finops.org/framework/
- Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- DistServe / goodput: https://arxiv.org/abs/2401.09670
