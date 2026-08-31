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

<!-- daily-20260621:platform-monitoring:start -->
### Context generator 是 pre-failure sensor identity 的一部分

agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。

**Trade-off、failure、共存与回退。** 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-21843` — primary `arXiv:2606.21843v1`；exact-v1 URL=`https://arxiv.org/html/2606.21843v1`；Method=`https://arxiv.org/html/2606.21843v1 — §3.1 Ada: a persistent AI agent; §3.4 The probe battery`；Evaluation=`https://arxiv.org/html/2606.21843v1 — §4 Magnitude Baseline; §5.6 Drift experiment`；Non-proof=`https://arxiv.org/html/2606.21843v1 — §6.3 Limitations — Drift trajectory is a padding artifact`。
<!-- daily-20260621:platform-monitoring:end -->

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

### 从 GPU Busy 到 Counter-derived Progress Sensor

GPU busy 适合回答设备是否在执行，却无法区分有用训练、recompute、padding 或失控 kernel。硬件 counter 可以构造 precision-agnostic 的 FLOP-progress sensor，但 metric owner 必须版本化 counter mapping、clock、kernel coverage 与 calibration revision，避免换架构或 kernel 后沿用同一数值含义。

它提高对执行进度的可见性，却增加采样开销、跨设备校准和未覆盖 kernel 的盲区；counter 不完整时应回退到 device time、step/token progress 与端到端 SLO 的联合判断。`arXiv:2605.20799v1` 的 §III 与 §IV 只支持作者计数器映射和实验；§VI 不证明该指标等于 useful work、模型质量或 SLO 达成。

<!-- source-family:SF-2026-ARXIV-2605-20799 -->

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

这里的 `Errors` 必须声明语义。`transport_error_rate` 可以由状态码、timeout、OOM 和 dependency failure 直接聚合；`contract_failure_rate` 可以来自 schema validator 或 tool protocol；但 hallucination、instruction failure 与 business outcome 通常需要第 66 章定义的 scorer、抽样和延迟标签。一个请求可以同时是 `runtime_success = true` 和 `quality_success = false`。

Monitoring 可以把已经校准的 evaluation results 聚合为时间序列，用于观察 slice drift、burn rate 和触发调查；它不能从 `HTTP 200`、低 latency 或 token 正常结束自动推导内容正确。否则 dashboard 会把“系统稳定地产生错误答案”显示成健康。

### 从 Error Counter 到 Layer × Detectability Failure Coordinate

按 transport status、timeout、OOM 和 dependency error 统计失败，在请求语义与 transport outcome 高度一致时最直接；但多 provider gateway、流式协议、tool call 和 session failover 把“成功返回”与“状态连续”拆开了。一个请求可能得到 `2xx`、完整结束 SSE stream，却已经发生 tool index collision、跨 provider state 丢失或 retry storm。此时继续把 Errors 定义成单个 counter，会让系统只看见容易检测的症状，看不见 silent contract failure。

更可维护的做法不是不断追加 error code，而是给每个 failure evidence 同时记录两个坐标：

```text
origin layer: client / gateway / provider adapter / model runtime / dependency / session state
detectability: explicit signal / invariant violation / cross-signal correlation / silent semantic failure
```

一次 incident 随后沿同一 evidence object 连接 `symptom → suspected root cause → detection signal → reproduction → recovery`。origin layer 决定谁拥有修复，detectability 决定需要 metrics、trace、schema validator、fault injection 还是第 66 章的 quality evaluator。这样 `runtime_success = true` 与 `contract_success = false` 可以同时成立，也不会把质量失败伪装成 transport error。

这条路线的代价是 failure schema、跨层 correlation 和复现 harness 都需要版本化维护；taxonomy 也永远可能漏掉未知组合。因此它不能替代 SLO、trace sampling、canary 与 incident investigation。系统规模小、协议单一时，RED 指标仍是合理起点；只有 silent failure 已影响恢复责任或 error budget 时，才值得承担二维分类与复现成本。

### 从 Thread State 下钻到带资源身份的依赖图

线程在 runnable、blocked 或 I/O wait 中的时间占比只能说明“停在哪里”，不能说明“被谁阻塞”。诊断可以从 request entry thread 反向追踪 futex、pipe、socket、VFS 与 block-I/O，并把每条边绑定实际 backing resource，形成 contention propagation graph。收益是把症状连接到锁、磁盘或远端服务，代价是 eBPF/内核版本依赖、图开销和 entry propagation 假设；无法稳定识别入口或 GPU collective 时，传统 profile 仍是 fallback。作者结果只覆盖单机 Linux 与披露应用，不能外推到所有容器、kernel 或训练拓扑。

<!-- source-family:SF-2026-ARXIV-2605-25298 -->

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

### Differential Privacy 必须覆盖事件发布与告警语义

只对存储后的 dashboard 数值加噪，在离线报表、固定查询和单次发布时容易理解；runtime monitor 会持续观察事件、
维护 temporal state，并在条件满足时选择是否发出 alert。事件何时被释放、规则被评估多少次、哪些窗口共享个体数据，
都会共同消耗 privacy budget。若 instrumentation、budget accountant 和 alert engine 各自计算，单次输出看似合规，
组合后的时序发布仍可能泄露信息。

因此 DP monitoring 的最小合同需要把 output-stream 依赖与发布串成同一状态机：specification analysis 根据时间依赖
识别 event-level adjacency 与 sensitivity，privacy barrier 决定在哪里注入噪声，tree-based aggregation 与 composition
记录跨时间预算。告警若消费这些输出，只能作为后处理，并另行校准噪声下的 false positive、false negative 与
abstention；论文并未证明任意 alert policy 的正确性。

```text
protected event identity + temporal specification
→ event-level adjacency and sensitivity
→ privacy barrier + calibrated noisy output stream
→ tree aggregation / composition accounting
→ downstream alert or analysis as post-processing
```

它获得持续监控下可审计的隐私边界，却会降低稀有故障可见性并增加预算枯竭、时间相关性假设、噪声累积和告警校准
成本。需要逐事件 debugging、低频安全事故调查或 threat model 不允许聚合时，应在受控权限下保留原始证据通道，
而不是把 DP 告警当作唯一真值。现有 exact-v1 只证明其声明的 stream-based monitoring specifications，不证明任意
telemetry、攻击模型或生产 SLO 下均可用。

<!-- source-family:SF-DP-RUNTIME-MONITORING -->

## SLO 与 Error Budget

<!-- source-family:SF-2026-ARXIV-2605-27599 -->

GPU utilization、瞬时 board power 或进程运行时间都容易取得，因此常被用来估算每个进程的能耗；但这些 proxy 没有共同的可观测能量 denominator，也没有回答共享 CPU、memory、fan 与电源损耗如何归属。要让 process-level energy 成为可审计 metric，monitoring contract 至少需要设备/系统边界上的能量计数、同一时间窗内的进程活动 identity，以及明确的 attribution rule 与 residual/unattributed bucket。没有 denominator 时只能标为 estimate，不能把利用率比例包装成直接测量。

外部功率计可以补充设备未暴露的接口，却把采样频率、时钟对齐、共享部件拆分和运维成本引入证据链；它适合校准或实验审计，不必成为每个在线请求的常驻路径。现有 exact-v1 审计只覆盖一台 GX10 的标准接口，支持“该栈当时无法直接提供进程级能量归因”这一边界，不证明所有 NVIDIA 设备或后续固件都如此。若硬件计数器不可用，平台应保留 coarse node/job accounting 与 uncertainty，而不是伪造细粒度精度。

SLO 应说明事件、有效请求、目标和窗口。例如：

```text
SLI = requests meeting success, TTFT and TPOT conditions
      / eligible requests

error_budget = 1 - SLO_target
```

Goodput 可表示单位资源内满足 SLO 的有效工作。它不替代质量、安全和成本指标，而是防止通过牺牲 tail latency 制造高 throughput。

Alert 应指向可执行动作。单个瞬时阈值容易抖动；多窗口 burn-rate 更适合判断 error budget 是否快速消耗。

## Monitoring 也会改变系统

### 输出 Watermark 与 Hidden State 都只是受限 Sensor

<!-- semantic-body-binding:SF-WATERMARKING-SHOULD-BE-TREATED-AS-A-MONITORING-PRIMITIVE:start -->
Watermark 不只回答单条输出是否命中；观察者可以跨输出、key 和时间聚合信号，形成 entity-level attribution。因此
watermark identity、key scope、observer capability、aggregation window 与 false-positive budget 必须进入 monitoring
contract，并接受隐私与滥用审查。它提供来源线索，不证明内容真实性或唯一作者；高隐私场景可能选择更短窗口、轮换
key 或不部署。多 key 实验只支持该观察面存在，不给出任意部署的识别率。
<!-- semantic-body-binding:SF-WATERMARKING-SHOULD-BE-TREATED-AS-A-MONITORING-PRIMITIVE:end -->

<!-- semantic-body-binding:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start -->
只在文本生成后分类会错过逐步形成的隐式危害；same-pass monitor 可以读取普通 decode 已产生的 hidden state，利用
时间聚合提前产生 hazard signal，而不再调用 base model。它降低额外 forward cost，却依赖 white-box access、layer/
model revision 和阈值校准，也可能在 domain shift 下误报。EMA 或 probe 只触发 defer、review 或 stop proposal，最终
authority 仍属于独立 policy；无法取得内部状态时回退 output/trajectory monitor。
<!-- semantic-body-binding:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:end -->

高频 scrape、过细 histogram、昂贵 GPU exporter 和大量 labels 都有成本。控制环消费 metrics 时还要考虑：

- freshness 与 scrape delay；
- aggregation window；
- missing data；
- counter reset；
- autoscaling feedback oscillation。

缺指标与“指标为零”必须区分，否则 exporter 故障会被解释成负载消失。

### Model-internal Sensor 必须从 Inference Hot Path 解耦

只采集请求级 metrics 成本最低，却看不到 activation、attention、router 或 hidden-state 异常；在每个 kernel 上同步
复制完整 tensor 最直接，又会让诊断本身改变 latency、显存与调度。内部可观测性因此需要从“是否插桩”演进为一条
受 policy 控制的数据路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11093:start -->
runtime 在选定 graph point 生成带 model/request/layer/tensor revision 的 capture descriptor，将 bounded tensor slice
或派生 statistic 先写入 GPU staging buffer，再异步搬到 CPU queue 供 probe 消费；admission policy 限制采样率、
bytes、保留期与敏感字段。Inference owner 只负责安全 capture point 和 buffer lifetime，Monitoring owner 负责 sensor
policy，probe 负责派生判断，Logging/Trace 保存 provenance；probe 不能回写执行状态或冒充模型 truth。

异步 staging 把多数分析移出 hot path，却仍会争用 GPU memory、copy engine、PCIe 与 host queue，并引入 dropped
sample、时序错位和敏感 activation 泄漏。队列过载、descriptor/version 不匹配或开销预算被突破时，应先降低采样、
退化为 aggregate，再关闭内部 capture，回到请求级 metrics 与按 incident 的离线 profiler。作者实验只覆盖公开的
模型、runtime 与 probes，不证明所有 tensor 或生产 tail 都能低开销采集。[受限证据：arXiv:2605.11093v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11093:end -->

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

### 无法插桩时，网络流只能充当旁路传感器

显式 framework instrumentation 能直接携带 job、rank、phase 与 operation identity，因果边界最清楚；但托管框架、封闭镜像或遗留训练任务可能无法修改代码。此时交换机与 host 已有的 flow sequence 可以作为退化观测面：用时间、大小、方向和通信周期提出 job、parallelism 与 phase 的候选解释，再由 workload registry、拓扑和少量显式证据交叉确认。

<!-- semantic-body-binding:SF-2025-LLMPRISM:start -->
旁路 sensor 只拥有 observation proposal，不拥有 workload truth。共享流量、加密/聚合、拓扑变化、框架版本和数据并行规模都会改变 signature；分类结果必须携带 sensor revision、训练分布、置信区间与 unknown 状态。它以零代码侵入换取间接性和 drift 风险，适合发现隐藏任务或触发进一步诊断；需要精确 root cause、计费或发布判断时应回退显式 instrumentation。LLMPrism 的生产部署描述只证明其平台合同内的可行性，不能把作者识别率或时间误差外推到任意集群。
<!-- semantic-body-binding:SF-2025-LLMPRISM:end -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-11916:start -->
LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-11916:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-11949:start -->
deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-11949:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14589:start -->
Long-lived Agent 的 silent failure 应按 environment quirk、assumption mismatch、error swallowing、fail-plausible narrative、operational omission 分类，并要求错误跨组件边界后仍以可行动 evidence 到达人。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14589:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15980:start -->
模型更新应默认触发activation-monitor revalidation，并将staleness prediction、label-free realignment与labeled retraining分层。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15980:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19386:start -->
wall-clock moment detector 在 Agent cadence 下可能结构性双稳态；monitor 必须以可观测 transition window 校准而非宣称瞬时状态真值。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19386:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24119:start -->
撤销把 denoising top-1 concentration 当 PEFT collapse alarm 的旧路径；monitor 改读 max LoRA gradient norm，并由每个 DLM family 的 held-out calibration 拥有告警阈值。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24119:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-26383:start -->
性能监控可用 speed-of-light model 将硬件峰值、数据移动和 workload 参数分解成可校准上界，再用 observed gap 定位瓶颈。上界是诊断基线，不是生产承诺；模型参数或运行条件未披露、校准失效时回到直接 profile 与端到端 SLO。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-26383:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28116:start -->
从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-28116:end -->

### Silent Data Corruption 需要真实 Fault Model

训练系统常用随机 bit flip 验证容错，因为它便宜且可重复；但真实 GPU silent corruption 与 operation type、数值位置和传播拓扑相关，均匀随机模型可能高估或低估保护效果。Monitoring 应把硬件错误指纹、受影响算子、跨 rank 传播和最终模型偏差连接起来，再据此设计校验、冗余与重算策略。更真实的 fault injection 提升证据质量，也增加硬件依赖与实验成本；无法取得现场故障分布时，应把随机注入明确标成 stress test，而非生产故障率或恢复能力的证明。[受限证据：arXiv:2605.04213v1]

<!-- source-family:SF-2026-ARXIV-2605-04213 -->

对永久或稳定复现的 CPU defect，另一条受限分支在同一 thread 内复制关键 instruction 并比较输出，把原 workload 变成主动 functional test。它比只依赖 machine-check exception 覆盖更多 silent mismatch，却增加指令、寄存器和时间开销；同源复制也可能共同受到设计 bug、瞬态相关故障或 compiler transformation 影响。

这种 checker 只拥有检测信号，不拥有根因和恢复权。部署前应绑定被改写程序、instruction 类型、compiler、硬件代际与 false-positive/coverage 测量；开销过高或 fault model 不匹配时，回退离线诊断、ECC/checksum、冗余执行或 checkpoint recovery。作者 hyperscaler 测试不能外推为任意 AI accelerator 或生产故障率。

<!-- source-family:SF-2026-ARXIV-2605-15638 -->

### 跨管理域网络需要可校验的 Ground Truth Loop

当校园、机房或合作方网络由不同管理域维护时，拓扑 inventory 很快失真，黑盒二层段也无法靠应用指标反推。监控面应先通过确定性的 L2 探测建立受版本控制的 ground truth，再用 integrity loop 比对观测与期望，只有通过 human-in-the-loop admission 的变更才进入正式拓扑。收益是让告警有可追责的资产身份，代价是探测权限、变更延迟和人工审核成本；单域且拓扑由控制器独占时，声明式 inventory 仍更简单。该案例证明闭环结构的价值，不保证某组探针适用于所有网络。

<!-- source-family:SF-2026-ARXIV-2605-24683 -->

## 本章在知识树中的位置

Monitoring 承接第 66 章对 Evaluation/Observability 的边界，为第 57 章 Evidence Plane 提供聚合 observed state，并向 evaluation sampling、autoscaling、admission、cost 与 incident response 提供输入。下一章转向离散事件：当指标告诉我们“出问题了”，Logging 如何留下可查询证据。

在隐私数据流上，职责还要再分一次：第 72 章的 policy-bound detector 决定原始内容中哪些
字段应在入口被最小化；本章决定剩余 telemetry 以何种 aggregation、attestation 和 retention
contract 被观察；第 66 章再判断这些受限观测是否足以支持能力、安全或发布结论。入口过滤、
zero-trust aggregation 与 Evaluation 是 `Layering / Dependency`，任何一层都不能用“看不到原文”
推导出匿名、合规或证据充分。

## 从机制演进到系统设计

Monitoring 从被动收集 metrics 演进到能解释 workload 和 failure onset 的 sensor system。Metric、log、trace、probe 与 context generator 都有自己的版本、采样和成本；主动 probe 可以制造可诊断信号，但必须与真实用户流量分开标记。

更丰富的传感器提高定位能力，却增加 overhead、privacy 风险、cardinality 和 observer effect。Monitoring 只拥有 observed state，不拥有“系统是否足够好”的最终判断；采样缺失或 sensor identity 漂移时，应保留 unknown，而不是以低错误率推断质量。Evaluation 和 release policy消费这些证据但保持独立。

## 自检问题

1. 为什么应从 SLO 反推 metrics？
2. GPU utilization 高为什么不证明有用工作多？
3. Histogram 与 Summary 的聚合语义有何差异？
4. 为什么 request ID 不应作为 metric label？
5. Goodput 约束了 throughput 的什么缺陷？
6. Missing metric 与 zero value 为什么要区分？
7. 入口 redaction、zero-trust aggregation 与 Evaluation 为什么不能互相替代？
8. 为什么 `runtime_success = true` 与 `quality_success = false` 可以同时成立？

## 从随机 Fault Injection 到可定位的 Accelerator Sensor

随机 bit flip 能快速验证“系统是否会坏”，却不保存 processing element 的结构身份，也不能区分错误发生在何处。对规则矩阵阵列，可用带代数结构的测试向量让输出 syndrome 保留 PE 行/列线索；单轮概率定位不确定时，再升级为比值型两轮检查，而不是把猜测直接交给 recovery controller。

这种 sensor 以额外测试执行、带宽和诊断延迟换更细 fault localization；它依赖算子、阵列映射与数值误差模型，不能把受控注错成功外推成现场故障覆盖率。结构不匹配、性能预算不足或 syndrome 不稳定时，仍需 checksum、冗余执行、checkpoint rollback 与人工硬件诊断。[受限证据：arXiv:2605.08594v1]

<!-- source-family:SF-2026-ARXIV-2605-08594 -->

### Fail-slow Detection 需要在线信号与离线资格复验分权

训练 job 内的 step time、collective latency 和 peer comparison 能低成本发现正在拖慢同步边界的节点，却容易把 workload phase、数据倾斜或短暂抖动误判为硬件故障。在线 monitor 应只拥有“提出 suspect”的权限；离线 node sweep 在隔离环境中复测计算、通信和设备健康，再由 cluster controller 决定 quarantine、return-to-service 或 replacement。

这条双路径缩短发现时间并降低无依据驱逐，但增加基线维护、复测容量和状态交接；在线漏报与离线环境不一致仍会造成错误结论。小规模或无同步放大的 workload 可继续使用简单阈值，证据冲突时保持节点隔离并升级人工诊断。exact-v1 只覆盖其披露训练集群、fail-slow 注入、false-positive 与监控开销，不证明所有硬件退化或生产故障分布都可被捕获。

<!-- source-family:SF-2026-ARXIV-2605-17879 -->

## Monitor 也需要独立的 Red-team Loop

### 被观测者会适应 Monitor，固定暴露策略会产生共同盲区

直接把完整推理轨迹暴露给单一 monitor，在开发期容易定位问题；一旦生成模型知道告警边界，可能通过压缩、改写或把危险意图分散到多步来规避检测。防御需要把 exposure policy、monitor identity 与外部行为信号显式版本化，并用异构监测器检查共同失败：

```text
trajectory + tool/environment signals
→ versioned exposure views
→ heterogeneous monitors
→ correlation and disagreement audit
→ independent stop / escalation policy
```

多 monitor 可以降低单点盲区，却不能把相关模型的同源偏差当作独立证据；更多暴露还会增加隐私、计算和攻击面。低风险、行为可由确定性规则完全约束的流程仍应优先规则与最小日志；对高风险 Agent，monitor 也只能提供告警证据，最终停止权应由独立 policy owner 持有。

<!-- source-family:SF-2026-ARXIV-2605-15257 -->
<!-- source-family:SF-2026-ARXIV-2605-15377 -->

在固定已知攻击集上测 monitor，适合比较版本并建立最低回归线；当攻击者会观察告警边界并调整轨迹时，静态集合会系统性低估最难发现的 failure。更完整的 pressure test 让 red-team generator 在受控预算内搜索能完成有害目标、同时绕过当前 monitor 的 trajectory，再由独立 environment verifier 和 judge 确认目标、可执行性与告警结果。Monitor 只拥有 observation，red-team 只产生挑战，两者都不能自行宣布安全结论。

<!-- source-family:SF-MONITORINGBENCH-SEMI-AUTOMATED-RED-TEAMING-FOR-AGENT-MONITORING -->
每轮结果必须绑定 attack generator、target agent、tool/environment、monitor revision、judge 与 search budget；否则更强搜索产生的低分会被误读为 monitor 回归，较弱搜索产生的高分又会成为虚假安全感。半自动 red-team 能提高 hard-negative recall，却增加攻击生成成本、judge 偏差和 benchmark overfitting；固定回归集、人工设计攻击与生产 incident replay 仍应共存。公开结果只支持其 coding-agent monitor、模型和攻击分布，不证明未知攻击覆盖率。[受限证据：arXiv:2605.09684v1]

### Router Telemetry 是旁路安全传感器，不是裁决器

MoE 路由原本是执行状态，若不同输入在 expert 选择与 GPU 活动上形成稳定差异，它也可作为不读取正文的旁路安全传感器。监控面应以 request identity 关联 routing-induced telemetry，经校准 detector 产生风险 proposal，再交给独立 policy gate；这样减少原始内容暴露，却会引入硬件映射漂移、tenant 干扰和模型升级后的失准。可疑路由不等于有害语义，检测器失配时必须回到内容受控审计或人工复核。现有证据绑定特定 MoE、遥测和攻击分布，不证明跨模型、跨硬件的通用安全可分性。

<!-- source-family:SF-2026-ARXIV-2605-24817 -->

## 小结

Monitoring 用受控成本提供系统健康的统计视图。它适合发现趋势、提出 fail-slow suspect 并驱动分层控制环，却不能独自判定节点故障，也不能解释某一次失败的完整上下文。下一章用 structured logs 保存事件证据。

## Review notes

本章复用 Part V 已冻结的 TTFT、TPOT、SLO attainment 与 goodput，不重新定义推理机制；自检答案回填明确了 transport、contract 与 semantic errors 的不同证据来源。第 68 章拥有事件，第 69 章拥有因果链，第 66 章继续拥有质量口径和发布判断。

Primary-source 与官方入口：

- Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- Prometheus histograms and summaries: https://prometheus.io/docs/practices/histograms/
- OpenTelemetry Metrics: https://opentelemetry.io/docs/concepts/signals/metrics/
- NVIDIA NCCL Inspector Prometheus mode:
  https://developer.nvidia.com/blog/real-time-performance-monitoring-and-faster-debugging-with-nccl-inspector-and-prometheus/
- Kubernetes Pressure Stall Information metrics:
  https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/
- Anthropic, "Measuring agent autonomy": https://www.anthropic.com/research/measuring-agent-autonomy
- LLMPrism（网络流序列作为不可插桩训练任务的旁路 sensor；Status: Experimental）：https://arxiv.org/html/2505.00342v1
  - 证据边界：作者结果绑定其平台、流量和部署合同；共享流量、加密、拓扑与框架漂移会使识别失效，不能替代显式 instrumentation。
- Google Research, "Private analytics via zero-trust aggregation":
  https://research.google/blog/private-analytics-via-zero-trust-aggregation/
- Agentic Search in the Wild（session trajectory 与 evidence-traceability proxy；作者观测边界）:
  https://arxiv.org/abs/2601.17617
- FailureAtlas（arXiv:2607.17525v1；Status: Experimental）：Method/Taxonomy `#S3/#S4`，case studies `#S6`，limitations `#S8`，完整 catalog `#A1`。作者 catalog 与复现证明分类方法可执行，不证明 failure space 完备，也不提供生产发生率。Repository: https://github.com/Vishal-sys-code/failure-atlas；事件时 commit 未固定。

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28116 — primary arXiv:2606.28116v1; exact-v1 URL=https://arxiv.org/html/2606.28116v1; Method=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; Training-stability monitors.; 5 Designing Module-Specific Monitors from First Principles; Evaluation=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; 1 Introduction; Non-proof=https://arxiv.org/html/2606.28116v1 — §6 Limitations; 7 Conclusion。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24119: `arXiv:2606.24119v1`; exact-v1 URL=`https://arxiv.org/html/2606.24119v1`; Method=`https://arxiv.org/html/2606.24119v1 — §3 Methodology; 3.2 Experimental Setup`; Evaluation=`https://arxiv.org/html/2606.24119v1 — §4 Experiments and Results; 4.1 Calibrated Triage`; Non-proof=`816 个配置、3 个 DLM family 与 200-step horizon 只支持短程 DLM-LoRA triage；跨 family 阈值失败，不能外推为通用 collapse detector。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26383**：Primary `arXiv:2606.26383v1`；Method `https://arxiv.org/html/2606.26383v1 — §SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation`；Evaluation `https://arxiv.org/html/2606.26383v1 — §Predicted-vs-observed latency and throughput analysis`；未证明边界 `https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- daily-20260627:PLATFORM-MONITORING:start -->
### Owner-merged minimal durable delta

Training-instability monitoring 应在 aggregate loss 发散前读取 mechanism-adjacent state：attention spectrum、router/load state 与 update statistic 是分别校准、绑定 checkpoint 的 sensor。它们可以触发暂停、诊断或 rollback，但不能自动拥有 root-cause truth；sensor 漂移或相互冲突时必须 abstain，并保留最近已验证 checkpoint 作为 fallback。

### Trade-off、failure、fallback 与 coexistence

Pre-loss signal 可能噪声大且依赖 family；它们保持 observe-first，缺失校准时 abstain，不能自动干预训练。

<!-- daily-20260627:PLATFORM-MONITORING:end -->

<!-- recovered-daily-20260624:PLATFORM-MONITORING:start -->
### 2026-06-24 evidence integration — PLATFORM-MONITORING

相邻章 `books/part-06-ai-infrastructure/66-evaluation-system.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24119**：撤销把 denoising top-1 concentration 当 PEFT collapse alarm 的旧路径；monitor 改读 max LoRA gradient norm，并由每个 DLM family 的 held-out calibration 拥有告警阈值。 816 个配置、3 个 DLM family 与 200-step horizon 只支持短程 DLM-LoRA triage；跨 family 阈值失败，不能外推为通用 collapse detector。

<!-- recovered-daily-20260624:PLATFORM-MONITORING:end -->

<!-- recovered-daily-20260625:PLATFORM-MONITORING:start -->
### 2026-06-25 evidence integration — PLATFORM-MONITORING

- **SF-2026-ARXIV-2606-26383**：`SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation` 所定义的源特定机制用于以校准后的硬件与 workload 参数分解性能上界和瓶颈；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:PLATFORM-MONITORING:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-DP-RUNTIME-MONITORING:start -->
- `SF-DP-RUNTIME-MONITORING` — Daily `2026-05-05`；primary `arXiv:2605.02391v1`；Books review `books-review:SF-DP-RUNTIME-MONITORING`。

  **已吸收的语义增量：** continuous monitoring 的 DP contract 必须共同拥有 event-level adjacency、temporal dependency、privacy-barrier placement、output release 与 composition accounting；下游告警只是 post-processing，不能把论文扩写成通用 alert guarantee。
<!-- daily-books-trace:SF-DP-RUNTIME-MONITORING:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07889:start -->
- `SF-2026-ARXIV-2606-07889` — Daily `2026-06-06`；primary `arXiv:2606.07889v1`；Books review `books-review:SF-2026-ARXIV-2606-07889`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07889:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11916:start -->
- `SF-2026-ARXIV-2606-11916` — Daily `2026-06-11`；primary `arXiv:2606.11916v1`；Books review `books-review:SF-2026-ARXIV-2606-11916`。

  **已吸收的语义增量：** LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11916:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11949:start -->
- `SF-2026-ARXIV-2606-11949` — Daily `2026-06-11`；primary `arXiv:2606.11949v1`；Books review `books-review:SF-2026-ARXIV-2606-11949`。

  **已吸收的语义增量：** deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11949:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14589:start -->
- `SF-2026-ARXIV-2606-14589` — Daily `2026-06-13`；primary `arXiv:2606.14589v1`；Books review `books-review:SF-2026-ARXIV-2606-14589`。

  **已吸收的语义增量：** Long-lived Agent 的 silent failure 应按 environment quirk、assumption mismatch、error swallowing、fail-plausible narrative、operational omission 分类，并要求错误跨组件边界后仍以可行动 evidence 到达人。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14589:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15980:start -->
- `SF-2026-ARXIV-2606-15980` — Daily `2026-06-15`；primary `arXiv:2606.15980v1`；Books review `books-review:SF-2026-ARXIV-2606-15980`。

  **已吸收的语义增量：** 模型更新应默认触发activation-monitor revalidation，并将staleness prediction、label-free realignment与labeled retraining分层
<!-- daily-books-trace:SF-2026-ARXIV-2606-15980:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19386:start -->
- `SF-2026-ARXIV-2606-19386` — Daily `2026-06-16`；primary `arXiv:2606.19386v1`；Books review `books-review:SF-2026-ARXIV-2606-19386`。

  **已吸收的语义增量：** wall-clock moment detector 在 Agent cadence 下可能结构性双稳态；monitor 必须以可观测 transition window 校准而非宣称瞬时状态真值
<!-- daily-books-trace:SF-2026-ARXIV-2606-19386:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19262:start -->
- `SF-2026-ARXIV-2606-19262` — Daily `2026-06-18`；primary `arXiv:2606.19262v1`；Books review `books-review:SF-2026-ARXIV-2606-19262`。

  **已吸收的语义增量：** hidden training detection 可读取已有 accelerator telemetry 的 phase、memory/compute 与 collective signatures，保持 observe-only，不向 workload 注入探针。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19262:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20758:start -->
- `SF-2026-ARXIV-2606-20758` — Daily `2026-06-19`；primary `arXiv:2606.20758v1`；Books review `books-review:SF-2026-ARXIV-2606-20758`。

  **已吸收的语义增量：** `A Topology-Aware, Memory-Centric Architecture that Separates Root-Cause Derivation from Root-Cause Explanation` 路由到 `PLATFORM-MONITORING`：OPS CORTEX 用四层 operational memory 保存拓扑、正常模式、事件与历史故障；deterministic graph/threshold engine 先派生 root-cause candidate，LLM 只解释、确认和建议，不拥有因果判定或修复权限。图证据不足时回退人工 investigation。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20758:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21130:start -->
- `SF-2026-ARXIV-2606-21130` — Daily `2026-06-20`；primary `arXiv:2606.21130v1`；Books review `books-review:SF-2026-ARXIV-2606-21130`。

  **已吸收的语义增量：** GPU/AI 服务的异常浪涌要由多窗口 telemetry 与显式阈值选择检测，并把 recall、false alarm 与 detection delay 一起交给 operator
<!-- daily-books-trace:SF-2026-ARXIV-2606-21130:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21843:start -->
- `SF-2026-ARXIV-2606-21843` — Daily `2026-06-21`；primary `arXiv:2606.21843v1`；Books review `books-review:SF-2026-ARXIV-2606-21843`。

  **已吸收的语义增量：** agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21843:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-17525:start -->
- `SF-2026-ARXIV-2607-17525` — Daily `2026-07-21`；primary `arXiv:2607.17525v1`；Books review `books-review:SF-2026-ARXIV-2607-17525`。

  **已吸收的语义增量：** 新增证据边界：把多 provider serving 的 failure 以 origin layer 与 detectability 两轴建模，再由 issue evidence、独立复现与完整 case study 连接现象、根因、检测信号和恢复动作。关键 delta 不是新增错误名单，而是把 runtime_success 与 semantic/continuity failure 分开。 该 delta 已进入 `books/part-06-ai-infrastructure/67-monitoring.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-17525:end -->
