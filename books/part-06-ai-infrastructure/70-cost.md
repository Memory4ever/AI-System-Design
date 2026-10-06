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

长度成本实验还必须记录输出上限：设潜在完成长度为 L、cap 为 C，实际统计通常只见到 min(L,C)。大量回答触及 cap，说明该配置下的资源压力，却不能识别 cap 以外的完整尾分布或未截断分位数；这是对测量条件的工程解释，不是由固定 5k-token 实验取得的无限尾部结论。Native token accounting、开放模型采样温度与闭源默认配置也要分别保留，不能把不同 decoder 的计数直接合成统一长度策略。<!-- source-family:SF-2026-ARXIV-2601-08490 -->

提醒模型简短可以减少输出，却同时改变任务效用，不能只据 token 下降签发无损 mitigation。受限对照中某些模型的正常任务完整正确率明显下降，另一些没有同样退步；应共同验收 length/cap-hit、正常任务质量与实际资源时间。论文未测真实服务 latency、跨租户排队或生产 DoS，故这些仍需独立 workload 验收；效用退步或尾部不可见时，应保留硬预算、准入与原 decoder 配置，而不是把文字提醒当作资源隔离。

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

分母明确后还需防止**只量 GPU、漏掉整机**。Agent 的工具等待和低并发阶段可能让 CPU、内存、主板与空闲基线占更大份额；把 GPU 遥测的 joules/token 直接当成完整服务能耗，会随工作流 phase 和批处理状态改变误差。测量应同步标记 load、prefill、decode、tool/idle 与成功/失败，分别保留 device 与 host 边界，再汇总到 goal lineage。整机计量增加时钟对齐和功率仪表成本，不能把 IPMI/NVML/RAPL 的估计视为外部电表真值；只比较同机 GPU kernel 时 device-only 仍可作局部指标。[单服务器实验](https://arxiv.org/html/2609.29707v1)展示这两种口径的差异，不支持跨硬件固定倍率。
<!-- source-family:SF-2026-ARXIV-2609-29707 -->

测量边界明确后，缩短输出也不能直接等同于节能。按代码边界暂停、编译并运行测试的早停器，会新增validation时间、CPU工作和等待期间的GPU驻留能耗；只有被省去的decode成本超过这些开销，且任务质量仍满足合同，才达到break-even。校验频率因此是决策量，失败、超时和没有可截断尾部的请求也必须计入。短而正确的基线继续生成可能比频繁检查更便宜。[代码早停实验](https://arxiv.org/html/2604.06755v1)确有少量token减少而GPU总能量增加的配置；其A10、10Hz NVML仅测device，CPU验证能耗未实测，不能把该局部反证换成全服务节能保证。<!-- source-family:SF-2026-ARXIV-2604-06755 -->

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

### 执行中闲置与 Deep Idle 不能合并核算

资源时间账本能说明 GPU 被谁占用，却不能单凭平均 SM 利用率推算能耗。程序仍驻留、计算/显存/通信活动很低的 execution-idle，可能比没有驻留程序的 deep idle 消耗更多功率；同样的池级平均利用率，若工作集中在少数设备、其余设备退出驻留状态，能耗也可能不同。监控负责对齐驻留状态、活动、功率和持续时间，成本账本再积分这些状态的能量；缺失计数器不能当成零活动。

识别这种差别后，才有两个不同的优化分支：集中负载以减少高功耗闲置暴露，或在持续低活动期降频、活动恢复时升频并设置 cooldown。两者都可能增加排队或恢复延迟，不能把节电视为免费收益；是否允许动作仍由请求的尾延迟与质量合同决定。突发负载、计数器不可用或延迟余量不足时，保留均衡调度与默认频率更稳妥。

这一分账得到[756 GPU、31 天遥测及 L40S/Llama-13B/vLLM 回放](https://arxiv.org/html/2604.04745v1#S2)的受限支持：作者的秒级观测不能诊断短 kernel，遥测前序相关也不证明等待原因；其负载集中和降频原型均有尾延迟损失，未建立通用 SLO 保证。板级功率仍不是整机能量，不能替代前述 host/goal 核算。
<!-- source-family:SF-2026-ARXIV-2604-04745 -->

有持久 Context 的 Agent 还会把降频反馈到状态压力：执行更慢使 Agent 活得更久，更多轮 Context 同时驻留，继而增加 eviction/recompute，重算又让执行进一步变慢。频率不能只由瞬时活动决定，而须同驻留量、可用 headroom 与 admission 联动；可以按 Context 量选频，用最慢 Agent 的累计进度提出 boost，再以独立阈值限制新接纳。这里 progress proxy 只触发控制候选，实际 KV 可用性和请求提交仍归第56章调度，成本 owner 要核频率、存活时长与重算的完整回路。<!-- source-family:SF-2026-ARXIV-2604-16682 -->

联动控制增加状态观测、阈值校准、router 与频率切换成本，也可能为降低驻留压力牺牲功率或接纳率。原文 H100/vLLM、有限模型及三小时录制请求回放中，最慢5% Agent 的累计 token/s 不是 request-tail、真实任务重新执行成功率或整机 goal 能量，饱和与 PD 边界也未完整测量。预算不稳、状态计数失准或重算反弹时，应保留默认频率、保守 admission 与必要容量余量；节电只能在同质量和任务完成合同下验收，不能以设备瞬时功率降低自签收益。<!-- source-family:SF-2026-ARXIV-2604-16682 -->

## Unit Economics 与总需求反弹

<!-- source-family:SF-2026-ARXIV-2605-27480 -->

只用每 token 的能耗、碳排或水耗衡量 serving，在主要目标是账单与机房资源时合理；但它们不能代理供应链、土地使用与生物多样性等不同生命周期外部性。若平台需要比较这些影响，必须先冻结 functional unit：同一质量门槛下的一次请求、一个有效 token 或一个完成任务，并把硬件制造、运行地点、时间窗口、基础设施分摊和质量退化绑定到同一 identity。

扩展核算能避免用一个环境指标冒充全部影响，却会增加数据缺口、模型假设和不可比性；缺少 site-specific 与 lifecycle 数据时只能报告范围与 uncertainty，不能生成虚假的精确 chargeback。碳/水指标在日常容量优化中仍更可执行，而生物多样性等账本适合采购、选址与长期组合决策。当前单一方法研究只能证明这种 accounting boundary 有必要，不能给出所有部署的通用影响系数。

环境维度不能互相代理，并不意味着每次选择计算配置都需要不同排名。若 workload、质量/延迟可行集合及 functional unit 固定，同一地点和时段下的 operational impact 都写成 IT energy 乘各自相同的正 intensity，能耗更低的配置在这些维度中也更低；这是比例模型的条件结论。改变地点或时段后，各 intensity 的次序可以不同，能耗最优地域不再自然是碳、水或生态影响最优地域。应把计算配置排序和部署排序分开，不将固定部署的经验一致性扩大成跨地域代理权限。

加入配置相关的 embodied impact 后，设配置 i 的 IT energy 低于 j；只有 i 相对 j 的 embodied 劣势大于 `intensity × (energy_j − energy_i)`，对应维度才会偏好更高能耗的 j。关键是差额方向与 crossover，而不是 embodied 总占比大；pairwise 翻转也未必改变全候选最优项。[PRISM v1 §2/§6/A.5.1](https://arxiv.org/html/2609.35569v1) 支持这条条件边界，结论仍依赖相同地域执行 profile、硬件寿命/利用率分摊与环境系数。新增核算与优化不确定性不能变成真实站点合规或生产收益；既有 fleet 的制造负担已发生，运行路由与采购决策还须分账。条件失配、迁移/网络代价未知或数据不足时保留原部署与范围估算，由调度 owner 在硬约束内另行验收。<!-- source-family:SF-2026-ARXIV-2609-35569 -->

低 intensity 时间窗很短且不同站点不同步时，迁移训练不能只换一个碳系数：冷启动、完整参数同步、local-step/FedAvg 与暂停改变了有效训练进度和优化路径，同功能单位应包含这些切换工作与独立质量要求。[有限 curtailment-aware 原型](https://arxiv.org/html/2602.22760v1)用低 marginal-intensity trace 作被弃电力的 proxy，在短窗口中同步/部署可吞掉有效计算时间；较低估算碳排仍伴随更高总能耗。Near-IID 分配和动态参与是其条件，train EMA/best perplexity 不能替代 held-out 能力，地理 trace replay 也不等站点实际弃电或物理排放测量。Provisioning、hysteresis、同步、失败未回报人口与进度恢复须计费，但不在成本章节重写训练状态协议；窗口不足、非IID或质量退化时，保留固定站点连续训练、保守暂停与原同步路径，不由低碳估算自签训练品质、zero-carbon 或账单收益。<!-- source-family:SF-2026-ARXIV-2602-22760 -->

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

可部署功率还不能只用峰值或总 energy 描述。同步训练、checkpoint 与启停会使机架瞬时功率迅速变化；设施侧的 ramp-rate 和频谱预算可能先于平均功率触限。一个替代分支不改变训练步骤，而在机架电源边界分开处理时间尺度：被动滤波吸收较快变化，双向辅助储能吸收或释放较慢的功率差，慢速 controller 再纠正损耗与偏置造成的 state-of-charge 漂移。储能需要的容量由功率差对时间的积分决定，波形平滑不是能量免费，也不等于平均功耗减少。

这条分支用额外硬件、转换损耗、热与寿命管理换取训练控制和设施瞬态之间的解耦；过滤只在额定功率、电流、SoC 与可用 headroom 内成立，软件离线后也不能无期限忽略漂移。受限 [EasyRider v1](https://arxiv.org/html/2604.15522v1) 的400VDC、10kW原型及两TitanX/125M训练trace对照支持局部波形与能量取舍，不证明完整MW级电网合规或电池寿命；低电压受25A上限限制，慢controller实验只核inner-loop恢复而非长期aging。Headroom不足、设施接口不相容或额外损耗无法摊销时，原有power cap、负载协调和保守容量预算仍共存，成本账本应同时记录波形条件、buffer损耗与训练完成成本。<!-- source-family:SF-2026-ARXIV-2604-15522 -->

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

组件与阶段的可控性成立后，频率选择还可以从“每个 kernel 都不能变慢”放宽为“整段执行不能超出允许时长”。对指定调用及 shape 分别测量频率配置的时间与能量，再最小化总能量、约束全部 kernel 的总时长，便允许一个调用局部变慢、由其他调用的时间收益补偿；固定频率或逐 kernel 非变慢规则则保留了更简单的预算边界。[Kernel-level DVFS exact-v1 §4–6](https://arxiv.org/html/2601.08539v1) 使用这种全局分配，但其顺序 kernel 时间总和不等于并发、通信或完整多 GPU 训练的 critical path。

搜索出的频率组合只是待执行 proposal：逐 kernel 切频的延迟可能超过短 kernel，热状态、测量噪声与搜索选择正向异常值也会破坏预算。作者 RTX3080Ti 的重测已从最初零慢化变为约0.6%慢化，§9 明示当前频率不能全部成功逐次应用；因此平台必须把实际切换、overlap/通信和独立重复测量加入端到端验收，不能承诺零损失节能。不能稳定执行或满足热/SLO 约束时，退回阶段级、固定频率或已验证整卡 cap，并保留原 profile 与失败证据。
<!-- source-family:SF-2026-ARXIV-2601-08539 -->

在目标设备尚未可用的设计阶段，实测组件活动与功率曲线也可能拿不到；只按 FLOPs、总 bytes 或 kernel latency 估算，则会抹掉 L2 与 DRAM 访问、SM 间负载分布的能耗差异。一条有条件的预测分支从 tile、threadblock 排布与 pipeline 推导各层流量和 busy/lazy SM 时间线，用已有硬件的离线测量校准相位时延及模块功率系数，再把规则、顺序 kernel 的估计合成待选架构和频率的功率 proposal。它把“先运行每个目标配置再决定”改为“先筛设计点，再在目标设备上测量”，不是免去所有 profiling。<!-- source-family:SF-2026-ARXIV-2604-20105 -->

这种代理提高预选速度，却把 kernel layout 识别、离线校准集和跨架构能效假设引入成本合同。目标平台的内存技术改变、并发 kernel/通信与不规则稀疏出现时，旧模型可能失准；单 GPU 的平均功率误差也不能签多租户尾延迟、整机能量或正式 power cap。相同设备与稳定 workload 已有实测时，直接 profile 更可信；尚未具备目标设备时才用结构预测缩小试验空间，并在取得设备后以真实功率、热与 SLO 测量验收或回退保守预算。作者在 A100/A10 离线训练、H100/L40S 有限外推下的结果仅支持这个受限分支，不是通用功率传感器。<!-- source-family:SF-2026-ARXIV-2604-20105 -->

频率选择还可以减少 profiling，而不是直接发明更强 actuator。完整扫过每个新模型、输入和频率最可信，却支付大量试跑；一个替代分支只在默认频率观察新 workload，再分别用 normalized power 分布与 duration-weighted SM/DRAM 活动寻找参考近邻，借用对应的频率缩放曲线。功率与性能瓶颈不同，两个近邻不必相同；离线聚类用于组织和解释参考库，不等于运行时直接按簇名称控制设备。<!-- source-family:SF-2026-ARXIV-2604-03591 -->

借曲线减少探索成本，却引入 phase、输入、模型和计数器语义失配。功率目标与允许性能退化须分别验收，平均预测或受测 p90 也不是严格 power/SLO bound；作者 QwenMoE 的预测存在约5%超目标反例。平台采用时应保存 profile identity、验证 actuator 权限并在失配时回退实测频率扫描或已验证 power cap，这是采用规则，不是作者已建立的通用保证。MI300X上的 cap 实验不能被 A100 仅 utilization 分析补成跨厂商控制验证；厂商计数器含义、测量噪声和整机账目仍需独立处理。

参考曲线还可能遗漏主机与设备的时间耦合。固定 CPU 频率或同步执行时，按 GPU operating point 估计时延往往足够；异步 kernel launch 与 GPU execution 重叠后，调整任一频率都可能把原来的重叠变成等待，反之亦然。此时应分别拟合主机提交与设备执行，再估计频率依赖的间隙/重叠，按跨层依赖重建整段 timeline；不能把两侧各自按频率比缩放，也不能简单相加逐层时延。稀疏采样可以减少 profiling，却仍支付离线校准、硬件计数器和层类型识别成本。<!-- source-family:SF-2026-ARXIV-2604-15357 -->

这种联合估计是成本与频率选择的 proxy，不是 deadline 或全局能耗最优保证。运行时、上下文或并发改变后，原有耦合关系可能失配，应重新校准，并在误差或热/SLO 风险越界时回退实测扫描或已验证 power cap。现有证据只覆盖受测 Jetson、DNN 与语言模型 decode：平均预测误差和吞吐目标比例不能升级为尾延迟成功概率，先选 GPU 再降 CPU 的 greedy 也不证明全局最优。Kernel 执行实现仍由第49章解释，实际 SLO 调度仍由第56章负责。

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

- `SF-2026-ARXIV-2604-20105`（Experimental）：[exact-v1](https://arxiv.org/html/2604.20105v1) §III-B、IV-A～C、V、VI-A/C/E；Daily 2026-04-23。只吸收目标设备尚不可测时 kernel 结构→模块活动→离线校准的设计阶段 proposal 与实测回退；A100/A10 训练、H100/L40S 外推、顺序规则单 GPU 限定，不能证明并发通信、整机能量或 SLO。apr02 非作者 source→实际 Ch70 采用核通过；root 已顺读写后正文与相邻段落，未复现实验。

- `SF-2026-ARXIV-2604-15522`（EasyRider；Experimental）：[exact-v1](https://arxiv.org/html/2604.15522v1) §3–4/§5.3–5.4/§6/§7.1–7.4/§8及B.2。只采用设施瞬态波形、被动/储能快滤波与慢SoC纠偏的条件分支；400VDC/25A/10kW原型、两TitanX/125M训练trace与normalized示范分开。inner-loop恢复不是outer aging、电池寿命或MW级电网合规；§8的$66k/$3.7M≈1.78%与文中<1.25%不一致，该成本比率不采用，B.2全局QP保证不采用。root必要源→实际owner与literal有限独立采用通过；root 实际顺读新正文与 Installed Power、水耗相邻交接后，非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-15357`（FLAME；Experimental）：[exact-v1](https://arxiv.org/html/2604.15357v1) §III-A/B、IV、V、VI-A–D，Eq2/4 拟合、Fig16 消融及 Eq13/14 greedy 支持有限联合 timeline 分支。Jetson AGX Orin/Orin NX、PyTorch/Transformers、三类DNN与GPT2-large/Qwen2-1.5B/7B decode，context≤1024、INA3221；平均MAPE8.14%与rate-ratio QoS不当tail/deadline保证。precision、并发和生产SLO未披露；Eq10–11自引用EWMA未自行修补或采用。apr02必要source→owner独立核验通过；root实际顺读正文与相邻交接后，非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-16682`：[exact-v1](https://arxiv.org/html/2604.16682v1)，Daily 2026-04-21；§3.3–3.4/6.2–6.3/7–8。采用降频→Agent 寿命→Context→evict/recompute 反馈与 admission 联动；H100/vLLM 和录制回放限制保留，P5 累计 token/s 非请求 tail/task success。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-06755`，Experimental：[exact-v1](https://arxiv.org/html/2604.06755v1) §4、§5.1–5.3、§6.1–6.2、§7。采用在线stop验证必须结算净成本的反证，不采用普遍节能、完整程序正确或未测CPU能耗。HumanEval/MBPP及Java协议、temperature0.1/top-p0.95、输出上限1000token、单A10/10Hz NVML限定结果；精度、batch/concurrency/SLO未披露。不把§5.3无干扰与§7无法独占GPU的冲突消除；apr01非作者写后核对通过，未复现实验。
- `SF-2026-ARXIV-2604-03591`（Minos；Experimental）：[exact-v1](https://arxiv.org/html/2604.03591v1) §4.1–4.3/5.1–5.3/7.1/7.4/8 支持默认频率单profile、power/performance双近邻与参考频率曲线；MI300X8卡192GB/1300～2100MHz cap，A100PCIe40GB无cap权限。vLLM batch1/8/32、torchtune32/64、QwenMoE32受限，1～2msenergy-counter/EMA与边界idle截断不是整机能耗；Qwen约5%超功率预测不等hard保证，未复现实验。

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

- `SF-2026-ARXIV-2601-08539` — Daily `2026-01-15`；[Kernel-level DVFS exact-v1](https://arxiv.org/html/2601.08539v1) §4–9/Tables1–2。2+2+2=6，调用级全局时间预算 owner 缺口深入；采用局部慢化补偿、profile 选择偏差与实际切频不可行反侧，不采用生产逐 kernel 实施或零慢化保证。单 GPU 隔离调用估计不是完整训练实测，未核代码或复现；root 必要原源/owner 写前核通过，root 实际正文/前后衔接及末注非作者 POST 通过，日级 Gate 未授。

- `SF-2026-ARXIV-2601-08490` — Daily `2026-01-15`；[BenchOverflow exact-v1](https://arxiv.org/html/2601.08490v1) §4.1固定5k cap/模型native统计、Table3正常任务反侧与限制。2+1+2=5，具体cap-censor/length≠utility gap深入；尾部不可见是工程推断，不授真实latency、cross-tenant DoS或无损提醒。open T1/closed default、质量下降与未披露硬件/runtime保留；未运行代码或复现。root必要原源/现owner写前通过并授窄锁，root已实际核两段正文、前后交接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-22760` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22760v1)，必要原段/对照与局部反侧见当日core/owner packet。fresh非旧packet作者独核具体原证与actual owner差额，获root该owner窄ownership后写一段；作者正文及完整邻接实际顺读，root非写入者实际正文、完整邻接与自身末注POST通过，窄锁释放。采用正文窄命题，局部错误不授理论/全系统保证，未核实现或复现，不授日级Gate。
