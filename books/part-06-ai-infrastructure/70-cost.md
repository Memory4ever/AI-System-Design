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

### Adaptation 不是单一路径，而是受预算约束的组合决策

当一个任务只允许 full fine-tuning，先选方法再核算成本是合理的；随着 SFT、PEFT、retrieval-augmented
in-context learning 与组合策略同时可用，训练开销、在线检索开销和可达到质量已经不能用同一单位直接比较。
更稳健的顺序是先冻结决策合同，再让预测模型提出候选：

```text
task and quality target
+ data access / freshness boundary
+ model and hardware revision
+ training, retrieval and serving price model
+ evaluation contract
→ propose an adaptation portfolio
→ measure candidate quality and realized resource use
→ select, reject or fall back
```

<!-- semantic-body-binding:SF-2025-COSMOS-ADAPTATION:start -->
Quality/cost predictor 只拥有 proposal，不拥有最终选择真值。真实 Evaluation 与已经发生的资源账本仍是
decision owner：预测超出校准分布、价格或 workload 发生漂移、失败 run 无法归因时，应回退直接 measurement，
而不是把预测节省写成生产事实。
<!-- semantic-body-binding:SF-2025-COSMOS-ADAPTATION:end -->

联合预测可以减少无效 sweep，却新增 predictor calibration、价格漂移、failed-run attribution 与比较口径
不一致。任务稳定、可选路径少或 measurement 很便宜时，直接执行一个已验证方法仍更简单。作者在 11 个 NLP
classification tasks、给定模型 roster 与 A100 条件下的结果只证明该 proposal path 可行，不证明生产 workload
或未来价格下仍能选中最优策略。

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

### Utilization 应由实际负载推出，而不是由计算器假定

用满载吞吐除以 GPU 单价，可以得到清晰的理论下界；在容量规划早期、持续满载或批处理可任意排队时，这个旧口径仍有用。在线服务的 offered load 较低或到达呈 burst 时，固定填写 `100% utilization` 会把空闲资源时间从账本里消失，使同一硬件看起来拥有并不存在的低 token 成本。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-11690:start -->
成本模型应从到达率 `lambda`、服务时间分布和请求长度推导 in-flight concurrency，再用实测 batching、queue 与 device busy time 得到有效利用率。稳定区间可用 Little's Law 的 `L = lambda * W` 作为一致性检查，但它不是容量真值：接近饱和时，排队会抬高 `W`，不同 Prefill/Decode mix、cache hit 和 SLO admission 也会改变一次请求消耗的资源。于是 `hardware + model + precision + lambda + length/SLO distribution` 共同定义 cost point，而 utilization 是被观测和校准的结果，不是随意输入。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-11690:end -->

这会让自托管与 API 成本比较更诚实，却需要真实流量、尾延迟和 idle allocation 数据；用短 benchmark 外推全天流量仍可能误判。负载不稳定时应报告多档 arrival-rate curve、goodput 与置信区间，并保留 on-demand、共享池或批处理作为低利用率 fallback。任何特定模型、量化或硬件上的饱和收益都只是该 workload 的测量结果，不能取代重新校准。

### Agent 能耗的分母应是 Successful Goal

Per-token/per-request 适合单轮、边界明确的调用；Agent 为同一目标触发多次模型、tool、retry、idle 与失败 run 时，它们必须进入同一 goal lineage。Cost owner 记录所有资源事件，evaluation owner 版本化 success predicate，只有满足该谓词的 goal 才进入 `energy_per_successful_goal` 分母；失败成本不能被静默丢弃。

该口径更接近业务结果，却依赖有争议的成功定义、长尾 attribution 和跨系统计量；goal 无法稳定判定时，应并列报告 per-request、device time 与 failed-run cost。`arXiv:2605.22883v1` 的 §4 与 §8 只支持作者测量合同；§10.1 不证明该 evaluator 适用于所有 Agent、硬件或真实电力边界。

<!-- source-family:SF-2026-ARXIV-2605-22883 -->

### Agent 的持久化 Footprint 也是成本

Agent memory、trajectory、tool artifact 与中间摘要把在线计算变成持续增长的存储状态。只计逻辑 bytes 会遗漏
重复 embedding、索引、版本副本和原文回显；只追求压缩率又可能删除 provenance、schema 或重建所需的边界。
因此成本账本至少要同时保存两组量：

```text
footprint = logical bytes + growth + duplication / echo + index overhead
safety    = reconstructability + schema preservation + provenance coverage
```

第一组回答“留下多少、为何增长”，第二组回答“压缩或清理后能否恢复 authoritative state”。可重建的 derived
artifact 可以用更激进的 TTL、压缩或重算策略；不可重建的用户输入、审批与外部 evidence 则要优先保留语义和
审计契约。代价是 storage accounting 必须理解 artifact type，而不再只是统计 bucket bytes。具体 memory merge、
遗忘与 provenance 语义由第 77 章拥有；本章只拥有资源成本与重建成本的联合核算。

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

<!-- source-family:SF-2026-ARXIV-2605-27480 -->

只用每 token 的能耗、碳排或水耗衡量 serving，在主要目标是账单与机房资源时合理；但它们不能代理供应链、土地使用与生物多样性等不同生命周期外部性。若平台需要比较这些影响，必须先冻结 functional unit：同一质量门槛下的一次请求、一个有效 token 或一个完成任务，并把硬件制造、运行地点、时间窗口、基础设施分摊和质量退化绑定到同一 identity。

扩展核算能避免用一个环境指标冒充全部影响，却会增加数据缺口、模型假设和不可比性；缺少 site-specific 与 lifecycle 数据时只能报告范围与 uncertainty，不能生成虚假的精确 chargeback。碳/水指标在日常容量优化中仍更可执行，而生物多样性等账本适合采购、选址与长期组合决策。当前单一方法研究只能证明这种 accounting boundary 有必要，不能给出所有部署的通用影响系数。

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

当 provider 同时隐藏 model、tokenizer 与 reasoning trace 时，按其自报 token 数计费虽然便宜，却让 evidence producer
与受益方成为同一主体。可审计 meter 应把一次用量绑定为 versioned receipt，由 usage meter 记录请求生命周期和计量
证据，billing plane 做聚合，tenant 或独立 auditor 通过 attestation、proof 或抽样 replay 验证；provider 不能同时
独占原始计量、账单聚合和最终裁决三种权力。

这种分权可降低 token inflation 与争议，却会引入 TEE/证明、重执行、隐私、tokenizer disclosure，以及 streaming
生命周期对账成本；attestation 只能证明某段计量路径运行过，不能证明模型质量、公平或业务价值。低风险且 tokenizer
透明时，公开规则加抽样 replay 仍是更便宜的基线；无法验证的 provider bill 应附 dispute、预算上限或降级条款。
exact-v1 中的攻击幅度只绑定论文使用的三种 audit framework、模型与数据，不应外推所有 hosted reasoning 服务。

<!-- source-family:SF-2026-ARXIV-2605-30040 -->

## ROI 的边界

平台 ROI 不应只计算节省的 GPU：

- lead time 是否下降；
- successful change rate 是否提高；
- incident/rollback 是否更快；
- policy/security evidence 是否减少风险；
- 用户是否采用 paved road；
- 平台运营成本是否可控。

这些指标不能硬压成一个精确货币数，但需要和平台投入共同 Review。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-23546:start -->
训练能耗不能只按参数量或 GPU-hours 估算；roofline 风格模型应把 model size、parallelism、hardware operating point、利用率与 wall-clock 联合到同一 measurement contract，并与质量边界一起报告。解析模型适合做规划 proxy，真实发布仍需设备功耗与端到端测量校准。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-23546:end -->

### Installed Power 不是可部署 AI Capacity

只用 datacenter 总兆瓦规划容量，在机架功率密度单一、网络和冗余结构稳定时足够粗略；多代 accelerator 共存后，rack limit、busway/UPS hierarchy、网络拓扑、冷却和冗余会让一部分电力无法分配给目标 workload。成本模型应从 installed power 进一步计算可部署容量和 stranded capacity：

```text
facility power and redundancy
+ rack generations / cooling / topology
→ feasible placement set
→ deployable accelerator capacity
→ stranded power and capacity cost
```

这把 power delivery 变成 placement 的硬约束，却增加设施模型、故障域和代际迁移复杂度。规划模型只能支持 what-if，不等于真实 facility measurement；同质小集群或机架约束宽松时，简单功率预算仍合理。任何设计比较都需绑定拓扑、冗余、负载和演进周期，不能从单一 MW 数推断可服务 token。

<!-- source-family:SF-2026-ARXIV-2605.16255 -->

### 水耗从事后 Accounting 演进为受约束 Dispatch

按区域电力水强度汇总月度水耗，适合 showback，却无法指导“何时、在哪里执行”这一控制问题。Cost owner 可以把电网 dispatch、计算负载与虚拟水强度放进同一约束优化层，在满足容量与服务边界后调整 placement。它把环境成本变成可执行目标，但依赖水归因模型、固定点收敛和及时 grid signal；模型错误可能把负担转移到未计量区域。数据不足时应保留静态 accounting 与硬预算，而不是启用自动调度。exact-v1 仅支持 IEEE 30/118-bus 仿真及其水模型，不证明真实数据中心已实现节水或跨区域外部性消失。<!-- source-family:SF-2026-ARXIV-2605-25854 -->

### Energy Geography 只能在硬约束之后优化

电价或碳强度使跨地域 placement 看似直接，但 state locality、capacity、latency、regulation 与 failure domain 通常先限制可行集合。调度器应先冻结这些硬约束，再把 energy geography 作为候选集合内的优化信号；便宜电力不能单独拥有 routing authority。分析模型可以支持 what-if，不等于生产 trace；请求不可迁移或状态搬迁成本超过收益时，原地域固定 placement 仍更合理。

<!-- source-family:SF-2026-ARXIV-2604-27855 -->

## Memory Cost 由内部维护行为决定

两段同样长度的对话，在不同 memory system 中可能触发完全不同的 summary、retrieval、rewrite 和 model-call 次数。只按输入 token 估算会遗漏 write amplification、周期 consolidation、查询 fan-out 与额外 judge。成本模型应逐层记录 archive write、derived view、retrieval、injection 和 rebuild，并与 rolling/full-context baseline 比较 break-even。

break-even 依赖模型价格、对话分布和正确率目标，不能把某个轮数当普遍阈值。会话短或记忆命中低时，保留更多原始 context 可能更便宜；长期、高复用场景才值得承担 memory control plane。

## 共享 Batch 的成本必须按边际贡献归因

多个请求共享一次 batch 时，总能耗不是各请求 token 数的线性和：最长序列、padding、KV traffic 与同步会让一个请求改变其他请求的执行成本。按 token 比例分摊虽然便宜，却可能系统性低估长请求或高外部性请求。

更可审计的路线是先离线重放请求子集，建立边际能耗或 Shapley-style reference，再用可在线取得的长度、phase 与资源特征拟合估计器。reference 负责校准，不等于唯一公平政策；在线 estimator 还要携带误差预算，误差过大时只用于容量规划而不用于 chargeback。该方法增加重放成本，但把测量模型与业务定价规则分开。
<!-- source-family: arxiv:2608.00026v1; daily: 2026-08-04; semantic-body-binding: request-marginal-energy-attribution -->

### RAG 成本必须沿 Request 与 Tenant 穿过整条 Pipeline

只按生成 token 计费最简单，却把 indexing、embedding、retrieval、rerank、shared cache 与 failed retry 的资源藏在平台总账。更完整的 cost identity 让一次请求在各阶段携带同一 tenant/request tag，并把共享索引、缓存和后台更新按公开规则分摊；chargeback owner 保存原始 usage、allocation policy 与可争议回执。

精细归因增加 instrumentation、标签基数与 shared-cost policy 争议，也不保证云账单与内部计量完全一致。单租户或索引成本可忽略时粗粒度 showback 仍够用；多租户 RAG 的 quota、SLO 与价格决策则不能只看 generation cost。作者原型只支持其 pipeline 与计量设置。

<!-- source-family:SF-2026-ARXIV-2607-12188 -->

### GPU Power Budget 应按组件与阶段分配

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21847:start -->
整卡 power cap 容易部署，也在缺少细粒度 actuator 时保持最清楚的安全边界；但它把 core、memory 与 workload phase 的瓶颈压成一个总数。只有 telemetry 和 actuator 能分别观测并控制这些 owner 时，平台才应按组件与阶段分配 power budget，并把 policy revision、阶段分类、热约束与 SLO 一起记录。

细粒度控制可能把压力从 core 移到 memory，或因阶段误判恶化尾延迟，还会增加传感、控制与稳定性成本。现有 exact-v1 的效率数字只属于受测 GPU 和操作，不能外推为通用节能比例。组件可观测性、actuator isolation 或阶段识别不足时，应回退经过验证的整卡 power cap，并保留 thermal/SLO guard。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21847:end -->

## 本章在知识树中的位置

Cost 消费第 67～69 章 evidence，并反馈到 scheduler、autoscaling、model selection 和 lifecycle policy。下一章进入多租户：只有 identity 与 isolation 完整，成本归因和公平政策才可执行。

## 从机制演进到系统设计

成本核算从 GPU-hour 扩展到一次可交付结果的完整资源图：训练 token、checkpoint、Serving bytes、KV transfer、tool/API、evaluation、失败重试、人工复核和 idle capacity 都应归属明确 workload。局部加速只有减少了端到端关键路径或容量成本，才构成系统收益。

更精细的 activity-based accounting 提高决策质量，却增加归因和采集开销。数据缺失时应报告区间和未分配成本，而不是伪造单一精确数字；小规模实验仍可使用简化核算，但不能把 vendor headline 或 kernel speedup 直接升级为 TCO 结论。

## 自检问题

1. 为什么 GPU 单价不是完整 AI cost？
2. `cost_to_quality_target` 比单 step 成本多考虑什么？
3. 为什么 cost per token 必须绑定 workload？
4. 高 utilization 与 effective utilization 有何差别？
5. 单位成本下降为什么可能让总成本上升？
6. 共享 serving 的成本归因为什么只能近似？

### Generation Energy 不是 Token 数的线性函数

按 `input_tokens + output_tokens` 估算能耗在窄长度区间容易复算，却隐藏了 prefill 与 autoregressive decode 对计算、内存访存和固定启动成本的不同叠加。更精确的模型应保留 input/output length 二维曲面与 model/runtime/hardware identity，先找到单位有效 token 的局部 operating point，再评估截断、摘要或 generation budget 是否真正降低 `energy_per_successful_goal`。

On-device 与 server 也不能只按一次推理能耗比较。本地路径还要结算 prefill、量化 operating point、电池循环和设备 embodied cost；server 路径则依赖 batching、利用率与网络。Local-first 可能改善隐私或离线可用性，却不天然更绿色；任何结论都应绑定设备、模型、precision、batch、长度、生命周期假设和成功任务分母，条件改变时重新选择 placement。

<!-- source-family:SF-2026-ARXIV-2609-11940 -->

所谓 sweet spot 会随 batch、KV cache、quantization、clock/power cap 和硬件改变，摘要还可能增加额外请求并降低质量。因而分析式模型只用于 proposal/what-if，必须用当前 runtime 能耗与质量/SLO 回执校准；稳定窄负载仍可使用线性模型。公开结果只支持披露的 H100、TensorRT-LLM、模型和长度网格，不可外推跨硬件节能倍数。<!-- source-family:SF-2026-ARXIV-2602-05695 -->

### 节能控制前先证明 Actuator Authority

训练系统观测到功率变化，不代表当前 controller 真能通过 group size、并行度或调度动作稳定改变能耗；sharding 与运行时可能覆盖这些设置。闭合节能控制环前，应在明确 measurement window 内做干预，确认 actuator 对 power、step time 与质量的因果影响，并把控制权归属写入运行配置。否则 RL 或自动调参只是在追逐相关性。
<!-- source-family: arxiv:2608.11226v1; semantic-body-binding: energy-control-actuator-authority -->

## 小结

成本是资源时间、结果与约束的关系。平台应优化满足质量和 SLO 的有效结果，而不是孤立追求 GPU busy 或最低 token 单价。下一章为这些归因和政策建立租户边界。

### 成本分母要覆盖优化链，而不只看最终服务

蒸馏后的 student serving 可能更省电，但 teacher generation、logit/materialization、student training 与 evaluation 已在
上线前支付资源。如果只比较 student 单次请求，就会把成本转移误写成节能。Cost owner 应以同一 workload 和寿命假设记录
完整 distillation lifecycle，并分别报告一次性与随请求增长的成本。它增加计量与摊销假设；teacher 产物可跨多个 student
复用时必须声明分摊方式。lifetime、allocation 或 reuse 假设失效，或 upstream cost 无法取得时，lifecycle total 应标为
Unknown 并分项报告，不能用缺失项补成一个精确总数；若问题明确限定为已经部署、上游投入已成为 sunk cost 的 student，
marginal per-request serving cost 仍是合法的共存基线。现有证据限作者模型、任务和能耗仪器，不能外推为所有蒸馏都节能。

<!-- source-family:SF-2026-ARXIV-2605-13981 -->

## Review notes

- Prefill Token Equivalents（trajectory state-cost proxy；Status: Experimental）:
  https://arxiv.org/abs/2604.05404
- Persistent Agent Memory footprint / reconstructability audit（Status: Experimental）:
  https://arxiv.org/abs/2607.11149v1

本章复用第 56 章 goodput、第 63 章 allocation 和第 67～69 章 evidence，不编造硬件价格或通用 ROI 数字。

Primary-source 与实践入口：

- FinOps Framework: https://www.finops.org/framework/
- Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- DistServe / goodput: https://arxiv.org/abs/2401.09670

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-23546` — primary `arXiv:2606.23546v1`; Method=`arXiv:2606.23546v1 — §2.2 Scale, Architecture, and Efficiency; §3.1 Tasks, Models and Training Protocol; §3.2 Compute, Parameter and Memory Proxies`; Evaluation=`arXiv:2606.23546v1 — §3.5 Hardware Efficiency via Empirical Speedup Models; §Appendix A Pre-Modeling Exploratory Data Analysis`; non-proof=`arXiv:2606.23546v1 — §7 Discussion; §8 Conclusion`; fallback=该 family 的 failure pressure 是：Transformer-based models underpin modern natural language processing but incur rapidly growing computational and energy costs. 披露的 evaluation signal 是：We derive a scaling law model that accurately predicts training energy across heterogeneous configurations. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-11690:start -->
- `SF-2026-ARXIV-2606-11690` — Daily `2026-06-11`；primary `arXiv:2606.11690v1`；Books review `books-review:SF-2026-ARXIV-2606-11690`。

  **已吸收的语义增量：** LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11690:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11149:start -->
- `SF-2026-ARXIV-2607-11149` — Daily `2026-07-14`；primary `arXiv:2607.11149v1`；Books review `books-review:SF-2026-ARXIV-2607-11149`。

  **已吸收的语义增量：** 新增证据边界：AgentFootprint diffs fresh per-run sandboxes, classifies retained artifacts, measures logical bytes/composition/duplication/echo/compressibility/growth and separately tests reconstructability. 该 delta 已进入 `books/part-06-ai-infrastructure/70-cost.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11149:end -->
