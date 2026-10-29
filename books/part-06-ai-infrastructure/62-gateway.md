# 第62章 Gateway

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-GATEWAY`
**Legacy Chapter:** Ch58
**Status:** Draft

**Roadmap Intent:** 统一入口、认证、限流、路由、协议转换和观测。

## 本章要回答的问题

为什么模型服务前还需要 Gateway？它与 Kubernetes Service、KServe controller、EPP 和推理 scheduler 的职责如何分开？重试、限流和路由为什么可能破坏 LLM 请求语义？

本章的核心判断是：**Gateway 是外部请求进入 AI data plane 的策略边界。它把身份、协议、流量策略和服务目标转成可执行路由，但不拥有模型内部 token state。**

## Kubernetes Service 不足以表达入口策略

Service 提供 endpoint discovery 和基础负载均衡，但生产 AI API 还要处理：

- TLS、authentication 与 authorization；
- tenant/model/API version 路由；
- rate、concurrency 与 token budget；
- timeout、retry、circuit breaking；
- streaming、request size 与 protocol translation；
- request identity、audit 与 telemetry propagation。

若这些逻辑分散在每个 model server，策略会漂移，runtime 也被迫承担与模型执行无关的职责。

## Gateway API 的角色分离

Kubernetes Gateway API 用不同资源表达不同 owner 的意图：

| Resource | 典型 owner | 职责 |
| --- | --- | --- |
| `GatewayClass` | infrastructure provider | 某类 Gateway 实现 |
| `Gateway` | cluster operator | listener、地址、TLS 与可附着边界 |
| `HTTPRoute` / `GRPCRoute` | application owner | match、filter 与 backend |
| `Service` / `InferencePool` | workload/platform owner | backend endpoints |

这种分工比一个巨大 Ingress annotation 集合更容易做权限隔离。Route 能否跨 namespace 附着必须由双方 reference policy 明确允许。

## LLM 请求改变传统代理假设

LLM 请求通常长连接、流式返回、service time 高且输出长度未知。传统默认策略可能有害：

- 自动 retry 可能重复计费或重复工具副作用；
- 固定短 timeout 会中断正常长生成；
- 只按 requests/sec 限流忽略 token cost；
- round-robin 忽略 KV/prefix locality；
- buffering 会破坏 streaming 与 TPOT 观测。

因此入口策略至少要识别 request class：

```text
estimated_work
= prompt_tokens
 + expected_output_tokens
 + model/adapter cost
```

估计不精确，但仍优于把一个 50-token 请求和一个 100k-token 请求视作同样成本。Admission 的最终 memory/SLO 判断仍由第 56 章的 serving control loop完成。

对可变 reasoning depth 的请求，`expected_output_tokens` 还不够：admission 应估计额外计算能带来的边际质量，并把最大 amplification、deadline 与 tenant budget 一起冻结。模型或 router 可以请求更多计算，但只有 Gateway/control plane 能批准新的预算 epoch；收益证据不足、队列拥塞或高分位延迟接近上限时回退固定 effort。这样避免“更会思考”变成无界资源占用，也承认在高价值难题上额外计算可能合理。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18921 -->

### 推理更快以后，API 前处理也需要增量状态

GPU变快后，入口的重复工作会反而成为主瓶颈。工具循环每轮只新增少量结果，却重新校验和渲染完整历史时，延迟随会话累积；一个条件分支用持久连接保存先前response、工具描述和已渲染token，后续引用明确的前序identity，只为新输入执行相应前处理。这改变的是API/CPU状态复用，而不是engine的KV分页或Agent的长期记忆；仅换传输协议，不能自动消除完整历史工作。<!-- source-family:SF-2026-OPENAI-WEBSOCKET-API-INCREMENTAL -->

连接局部缓存增加内存、状态归属和失效处理责任。从系统设计上，只有旧状态身份、模型/工具配置与策略仍合资格，才能复用旧处理结果；把部分校验改成delta处理，不代表新旧内容组合的约束被自动证明。官方工程披露支持这种增量分支，但未给断线恢复、跨连接迁移或所有安全规则的完整保证。若旧状态不可取、资格变化或增量验证不能建立，就显式重建/重新验证；短请求和无会话场景仍可使用stateless入口。收益应分解API前处理、工具时间与模型推理，不能把更快模型或up-to结果全归给WebSockets。

### 入口状态的归属与协议兼容

单会话直连能少一跳，多方通话使用SFU也便于集中媒体策略；当主要负载变为用户与模型的一对一实时交互，Kubernetes弹性扩缩却会放大每会话公开UDP端口和有状态协议终结的矛盾。可把小而固定的公开媒体入口交给薄relay，由transceiver独占ICE、DTLS、SRTP密钥与session lifecycle；首个STUN包中的server ICE ufrag携带cluster和owner提示，relay据此转发，再以client地址到owner的soft mapping处理后续包。这里的入口只决定包送往哪里，不解密媒体、不取得模型token/KV或Agent任务完成权。<!-- source-family:SF-2026-OPENAI-WEBRTC-RELAY -->

这以额外转发hop、映射协调及过期清理换取较小公开端口面和稳定的hard-state归属。relay重启后的mapping可由后续STUN重建，Redis缓存可加快恢复，但路由重建不等于transceiver的ICE/密钥状态可迁移或已恢复；相应保证仍需另行验证。官方工程披露没有量化可比端到端延迟、并发或尾部SLO，不能从“thin relay足够”推出通用低延迟、零丢包或无需kernel bypass。小规模直连、多方媒体SFU仍各有适用域；无法维持owner映射时，应显式重新协商连接，不把流量改投新进程当成原会话连续性。

协议normalize还要区分“回到同一provider格式”与“换到另一provider”。可用中立typed IR保存message/content、tool call和generation controls，并在preserve模式另存provider-specific metadata，使同格式往返可检查结构保持；strip模式或目标不支持的字段却会丢失cache、sampling等能力。这不是所有provider语义本来相同，warnings也不认证丢字段无影响。Gateway应显式判断本请求哪些字段可转、哪些是不可降级合同，不兼容时拒绝或固定原provider，而非用JSON成功替代会话语义验收。<!-- source-family:SF-2026-ARXIV-2604-09360 -->

流式转换另需request-scoped状态：current block、tool-call identity/name、未完整的argument buffers，以及提前到达的finish/usage事件。累计part与delta、隐式与显式block边界不是可直接拼接的同一对象；转译只交付格式与顺序，不执行tool或批准effect。[LLM-Rosetta的有限测试](https://arxiv.org/html/2604.09360v1)支持四schema下的接口分支，255条stream测试与10条cross-provider案例不授所有API演进或transitive保真，自写测试与六个外部compliance案例亦有限。映射维护、buffer、校验、serialization和额外proxy hop都计费；字段新变、stream重建失败或总成本不成立时，重核adapter或保留provider-native客户端/原直连，不从converter微时延推出生产SLO。

## Gateway、EPP 与 Engine Scheduler

三者处于不同时间尺度：

```text
Gateway
  authenticate, normalize, apply coarse policy

EPP / smart router
  choose endpoint using queue, KV, adapter and model-server signals

Engine scheduler
  choose token work for the next iteration
```

Gateway API Inference Extension 的 `InferencePool` 在当前 v1 API 中表示一组同配置 model server Pods，并引用 Endpoint Picker。EPP 根据 KV utilization、queue length、active adapters 等信号选择 endpoint。

EPP 失败时的 fail-open/fail-close 是显式可用性与策略 trade-off。Fail-open 保持流量，却可能丢失 locality/SLO；fail-close 保护策略，却扩大控制面故障影响。

### MCP Gateway：把协议、身份、目录与会话归属收束到共享控制点

当每个 Agent 只直连少量、无状态且协议一致的 Tool Server 时，client-side connection 与完整 schema 装载最简单：没有共享控制面，也容易定位失败。约束变化来自数千工具、legacy OpenAPI、多个 MCP 变体、细粒度授权和有状态 session。此时仅做 endpoint load balancing 不够，因为协议翻译、调用者可见的授权目录、候选工具检索与 session-owner routing 必须读取同一 identity。

更稳健的演进是让 Gateway 拥有外部身份、协议适配、authorized catalog view 与 session-to-backend mapping；Agent 仍拥有 task intent 和最终 tool choice，EPP/engine scheduler 仍拥有模型执行。混合 lexical/semantic retrieval 只是缩小候选集，不应绕过授权，也不证明所选工具能正确完成任务。

共享控制点新增了 coordination state：跨 Gateway 的 session miss、集中式 metadata store、Pub/Sub 与长连接恢复可能成为新的 tail-latency 和可用性瓶颈。因而 session identity 需要 owner、lease、expiry、failover 与可观测证据；工具规模小、session 无状态或组织不愿承担共享协调面时，direct connection 仍更合理。当前证据来自单一云厂商部署和作者 microbenchmark，不构成可移植 MCP 标准实现的证明。

## 认证、授权与模型身份

认证回答调用者是谁，授权回答其能调用哪个模型、数据域和操作。Route 到 endpoint 之前，应把外部 identity 转成内部可信 principal，而不是继续信任可伪造 header。

对于 multi-adapter 或多模型服务，授权不能只停在 URL：

```text
principal
→ tenant
→ allowed model version / adapter
→ quota and data policy
→ backend identity
```

Gateway 日志与 trace 需要记录解析后的 immutable model/service revision，同时避免记录敏感 prompt 全文。

可信 principal 解决调用者身份，却不让模型推定的用户属性自动变成已验证事实。若响应策略依赖年龄等不确定属性，应把推定值、可信证明与缺失信息分开，由版本化 policy 决定保守路由及纠正路径；收集证明又增加隐私成本，误判也可能限制合规用户，不能把保守默认当作分类器正确性。[公开年龄策略计划](https://openai.com/index/building-towards-age-prediction/)说明这种约束已出现，但没有证明预测系统已部署或其误差可接受。属性依据不足时保留明确受限路径，而不是静默升级为可信授权；这是一条从公开政策约束推导出的系统设计边界，不是厂商内部实现披露。<!-- source-family:SF-2025-OPENAI-AGE-POLICY -->

## 重试与幂等性

安全 retry 需要同时满足：

- 请求尚未产生对外可见 token 或副作用；
- backend 可以识别 idempotency key；
- deadline 仍有预算；
- retry 不会突破 tenant quota；
- 新 endpoint 不依赖丢失的 local KV state。

一旦流式输出已开始，透明 retry 通常无法保持同一 token trajectory。Agent tool call 更可能产生外部副作用，第 78～81 章还会扩展这一边界。

若请求确实允许复用同一完整回答，Gateway 还可在固定空间里缓存 response，而不是复用 engine KV 或透明重做已交付请求。响应大小不同时，命中次数不足以表达价值：一个受限在线分支估计 query 频率与 miss 的期望生成费用，再按 byte 预算求推荐集合；但推荐的新回答尚未存在，实体 cache 只能保留已有交集，等真实 miss 取得结果后再填充，不能把离线最优集合当作已经物化的状态。[Cache Bandit 的有限模型](https://arxiv.org/html/2509.15515v1)假定有限 query、固定问答大小和稳定到达分布，hit 成本为零，miss 才观测费用，并以 miss 数或时间触发再求解；其累计 inference-cost 对照没有支付完整求解、存取和校验开销，不证明净服务 SLO 改善。从系统设计上，复用还应先满足 caller/data、model/adapter、生成与 policy 的响应身份资格，不能让较高缓存价值越过授权或内容时效。在线估计、推荐集合、真实填充和失效处理都付费；分布、回答资格或净收益不合时，回到固定/简单替换策略或直接调用，保留原幂等与独立质量检查，不从命中率批准语义等价。
<!-- source-family:SF-2025-ARXIV-2509-15515 -->

### Response Trace Watermark 是受限序列化通道

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21865:start -->
传统水印往往改写字段值或侵入业务 handler；如果某类 JSON/XML response 的 member order 在 client contract 中明确不承载语义，而且整个序列化链保序，Gateway 可以把 grouped-key permutation 用作受限 trace channel。此时 watermark artifact 必须联合绑定 schema、grouping 与排序规则、key material、serializer path 和 extraction receipt；Gateway 只拥有编码与提取，client compatibility、signature/cache canonicalization 和 authorization 仍由各自 owner 验收。

“字段顺序在规范中无语义”不等于真实 client、签名、缓存或 canonicalizer 不观察字节顺序。该分支还增加重序列化、容量阈值、密钥管理和删除/规范化后的恢复损失，容量不足时插入 fake key 甚至会改变可见结构。只要 compatibility、完整性或 key secrecy Gate 失败，就应禁用 permutation embedding，回退显式 signed provenance、sidecar audit receipt 或应用层水印；可提取 watermark 不能被解释为内容完整性或授权证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21865:end -->

## 观测与容量反馈

Gateway 是 client-perceived latency 的最佳观测点之一，应分解：

```text
request_latency
= gateway_queue
 + routing
 + backend_queue
 + TTFT
 + streaming_duration
```

它还应传播 trace context 与 request identity，让后端 metrics/logs/traces 可关联。高层路由不能只消费瞬时 GPU utilization，应使用经过聚合、带 freshness 和 fallback 的 signals，避免控制环振荡。

当 Gateway 同时做 provider evaluation 与 routing 时，直接为每种模型、任务和故障各加一列指标，短期可读，长期
却会产生名称漂移、不可比较的 evaluator 和丢失 lineage 的临时规则。一个 typed schema 可以把 Context、intent、
response issue、quality evidence 与 operational measurements 分开建模，再用显式 relation 将一次 route decision
连接到输入版本、候选 provider、evaluator revision 和最终 outcome：

```text
request identity + typed context
→ candidate route set
→ versioned quality / operational evidence
→ policy decision
→ response and outcome receipt
→ evaluator / routing recalibration
```

Schema 只提供可查询、可追溯的控制面语言，不保证自动 evaluator 已校准，也不应取代 Engine 对 token/KV 的实时
调度权。它获得跨 provider 对照与事后解释，代价是字段治理、迟到数据、join consistency 和 evaluator coupling；
schema 过宽会把未知值误当作可比较事实。单 provider、单指标服务仍可使用薄 telemetry；异构 provider 和持续
策略学习场景才值得支付关系化成本。事件时论文只展示其 schema population 与 routing case，不证明固定字段集合
适用于所有业务。<!-- source-family:SF-2026-ARXIV-2603-26728 -->

缺少本域带标签请求时，路由训练还可先从domain描述构造受限task taxonomy，按profile生成QA、去重，再实际调用冻结的全部候选模型取得quality与token-cost标签。Query先提出task-type分布，各model的type-conditioned预测再按该分布混合，最后按声明的quality/cost权重排序；这里训练的支持域来自synthetic generator与taxonomy，不是对真实请求已经观测到的能力，也不能让高utility越过硬资格。<!-- source-family:SF-2026-ARXIV-2604-09377 -->

[TRouter的有限冷启动对照](https://arxiv.org/html/2604.09377v1)只支持该经验预测接口，类型单标签不是真实posterior，task/model条件独立也须按人口检验。正文reverse-KL与one-hot CE方向、marginal-mean MSE与期望conditional likelihood未闭，不采用“实际训练已实现同ELBO/校准保证”；更细taxonomy也非处处更优。合成QA、全部候选回答/判分、训练与真实holdout回归全计费，造数报价不是总预算，LR五runs不能推广到主表。Domain、candidate价格/身份或质量代理漂移时，补真实calibration、退回静态/已核router或保留Unknown，不从synthetic低费推出通用路由收益、latency或安全。

路由训练的标签也可能只是一次随机回答，而非该query/model的稳定能力。可在离线对保义改写和重复解码采样，分别估计质量、费用及整体波动，再按声明的risk权重形成回归/分类监督；线上仍只用原query选择一个合资格模型，不获得test-time oracle。[受限同router对照](https://arxiv.org/html/2606.06924v1)支持这种替换，但更多观测与risk项并非处处改善，改写的结构相同也不保证语义同一。全部改写、候选回答、评分与重训都计费，token-price效用不等延迟或尾部SLO；语义、候选版本、价格或收益失配时，保留单shot原始分布、已验固定route与独立回归，不把更稳label签成正确性或权限。<!-- source-family:SF-2026-ARXIV-2606-06924 -->

路由训练还要说明费用在哪个人口进入目标，而不能只看reward里出现了cost：若目标写为success乘以“固定收益减费用”，期望优化的是成功率与成功样本内费用的组合，失败调用虽真实花钱，却不进入该费用项。[受限语言router分支](https://arxiv.org/html/2510.08439v1#S4)还允许自答、外调后合成或直接采用某返回，这些只是选择动作，engine仍负责实际调用、重试、资格与完整记账。两次失败不论费用都可同reward，成功过贵甚至可比失败更低，故权重不是硬预算，也不是正确性严格优先；必须另存失败/重试、router本身和外调/合成的全账，并以独立质量底线验收。候选描述、价格与pool变化属于训练输入和人口，不把路由模式变化认证为自知能力；扩池也可同时增质增费，部分任务弱于强单模型。全部制样/难度调用、训练rollout、catalog扰动与真实请求回归均付费。成功判据、费用或候选资格失配时，保已核固定route、较小合资格池与外层cap，不由高accuracy/cost比或success gate批准失败免费、全域净省费和生产SLO。

<!-- source-family:SF-2025-ARXIV-2510-08439 -->

Learned router 只能在**已满足硬资格**的候选中提供 utility 排序：Context 容量、tool/modality 支持、region、
privacy、safety 与 data-residency 先形成 eligible set，预测质量、成本、延迟与 cache reuse 再参与选择；高 utility
不能补偿不合资格。多轮分类还可把 request history 的 decoder KV 作为 session-owned persistent state，只将当前
candidate-label roster 作为 transient suffix 计算并丢弃其 KV，避免 endpoint 增删污染对话状态。代价是 label suffix
仍要关注全部 retained history，延迟同时受 cache length 与 roster size 影响；session/model/tokenizer identity、TTL、
truncation 与 position handling 任一不可靠时，应回到 stateless classification 或固定 route。

[SCX Router](https://arxiv.org/html/2609.02292v1)只为 direct endpoint path 提供 released/evaluated evidence；profile、
posterior、hybrid、cascade、portfolio 与 planner-worker 都仍是未完成的组件或提案。其 task taxonomy 的
problem-solving F1 只有 `.127`，端到端比较又使用预先筛出存在正 routing gain 的 1,000/1,500 tasks，缺少 CI、
重复 seeds 与冻结 endpoint revision。因此这里只吸收状态归属与 hard-filter-first 边界，不把它写成生产路由收益、
streaming latency 或 agentic routing 已成立。

若请求目标只是有限标签分类，路由还可从一次选模型变成顺序购买测量：先由带标签请求和各候选的历史输出拟合标签及测量概率，再按当前已问结果比较“停止并预测”与“再付费问哪个候选”，用有限池动态规划提出下一步。最优仅相对所给概率模型、独立性口径和费用，不证明学到的 posterior 正确；跨请求共同犯错与同一请求下的采样依赖也不能混为一谈。Pool 扩大同时增加联合估计压力与指数求解成本，零查询仍支付 embedding、预测器和规划，不是零计算。受限分类对照的 token-price 费用及无限独立重复下的渐近律，都不能替代真实延迟、共错与分布漂移验收。应保标签/候选版本、观测 state、校准人口和全部离线调用费用；概率失准、候选不合硬资格或净收益不足时，保固定 route、较小可信池与独立最终判据，不由 DP 最优签发一般生成或动作安全。 [受限机制与证据](https://arxiv.org/html/2610.30076v1)。<!-- source-family:SF-2026-ARXIV-2610-30076 -->

对一般生成候选，查询API常只取得output和cost，并未取得该候选的真实reward；只有被选部署的输出才有后续反馈。因此可把“还要付费问谁”的reservation index与“已有哪个输出更值”的reward evaluator分开学习，前者消费queried样本，后者只消费selected反馈，不能把未选候选补作已观察奖励。在独立请求、条件独立候选、同request–output共享效用及可识别参数模型下，乐观估计可据当前最好输出与剩余index决定继续或停止；理论还要求特征/阈值有足够支持，不由一个拟合分数自动满足。累计期望regret相对所给oracle，不授每请求正确或严格latency；每API每期一次也不覆盖多次采样、并行ensemble与合成。所有查询、探索、拟合和独立outcome计费，反馈迟缺、来源效应或支持漂移时保固定合资格cascade、原router与Unknown，不让learned utility越过硬资格和最终验收。 [受限原件](https://arxiv.org/html/2606.07392v1)。<!-- source-family:SF-2026-ARXIV-2606-07392 -->

一个请求的 utility 还可能定义在有限输出集合，而不是单条回答上：先固定 generation budget、语义去重规则和质量 evaluator，再让 router 选择预期能产生更多高质量 unique answers 的候选模型。通过 suite 内的 offline sampling 得到每个 query 的集合分数及 route label，只提供该预算和 evaluator 下的训练目标；贪心去重的顺序、阈值和 judge revision 都会改变 label，不能把“多样”当真值、无限覆盖或绕过前述 hard eligibility 的理由。<!-- source-family:SF-2026-ARXIV-2604-02319 -->

[有限十八模型 suite 的路由对照](https://arxiv.org/html/2604.02319v1)在固定 sampling 配置中支持这个目标，却不保证 OOD 或改 prompt 后的收益；speculative router 在域外与低频切片没有一致优势，全模型混合也可降低平均质量和后序回答质量。候选 prefill、日志、offline generation/judging、route training 与完整输出预算都付费，所测 speculative 路径比 top-one 分支更慢，不能用更高集合分数承诺更低 SLO 成本。label/预算迁移不可靠、请求只需一个可靠答案或时限紧时，保留固定 route 与单答案质量/延迟目标，不把较多 unique 输出升级为用户任务成功。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13968:start -->
#### 跨域推理必须分离 Control Channel 与 Token Stream

跨 local、HPC 与 cloud 的推理最初可以沿同一代理通道传递认证、作业控制和 token stream；当管理域、网络成本和数据驻留不同，这会让控制面拥有不必要的明文，也让慢控制操作阻塞长连接数据流。Gateway 应把 auth/job-dispatch control channel 与加密 token-stream data channel 分离，并把 tier selection、Context 摘要、会话归属和 fallback 写成版本化 policy。Router 选择合资格路径，传输层持有流式连接，模型 runtime 仍持有 token/KV state。

通道分离降低信任与故障耦合，却增加密钥、会话一致性、跨通道 trace 和 partial-failure 处理；摘要还可能丢失任务关键语义。身份、路由 receipt 或 state handoff 不完整时，应回退同域直连或显式重建 Context，不能从 token 已到达反推控制决策正确。作者结果仅覆盖其 tier、网络与 workload，不构成通用跨域 SLO。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13968:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16358:start -->
#### TEE Router 只收缩 Plaintext Authority，不提供端到端正确性

普通 API router 在单一可信运营域中同时读取 prompt、鉴权和目标 endpoint 最直接；跨组织或第三方 gateway 出现后，同一组件同时持有 plaintext 与转发 authority 会形成集中泄露面。可将解密和目的地绑定收缩到 client-attested enclave：untrusted host 继续执行可公开的认证前置、排队、scheduling 与 accounting，enclave 只接受绑定 measured image、policy revision 和目标身份的请求，再释放最小必要明文。

TEE 把信任边界缩小，却没有消除 side channel、rollback、证明新鲜度和运营可用性问题；attestation 也不证明上游 policy 或下游模型正确。测量身份不可验证、enclave 容量不足或 streaming 恢复无法保持会话语义时，应 fail closed 或回退到用户明确授权的直连路径，而不是把“运行在 TEE”当作端到端隐私证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16358:end -->

### Stateful Failover 的验收对象是会话连续性，不是 Endpoint 可达

无状态路由只要新 provider 返回 200 即可判定 failover 成功；多轮 LLM 会话还携带 system policy、tool state、prefix/KV 与 provider-specific serialization，目标端可达却可能语义断裂。Gateway 因而需要在切换前识别可迁移状态、兼容转换和不可转移字段，切换后用会话级 invariants 验证连续性，并在不兼容时拒绝透明切换、显式重建 Context 或要求用户确认。

多 provider 提高可用性，也增加状态映射、隐私边界和语义漂移。短、无工具、无持久状态的请求仍适合普通重试；复杂 Agent session 不能用单一 uptime 或一次回答相似度证明连续。公开 benchmark 只支持其 provider/harness/failure matrix，不给出生产通用 failover 成功率。

<!-- source-family:SF-2026-ARXIV-2607-15899 -->

## 本章在知识树中的位置

本章连接 KServe service desired state 与实际请求流量，并把租户、SLO 和观测信号送往 Serving data plane。下一章继续向下进入 cluster resource plane：GPU Scheduler 如何为 training 与 inference Pods 分配真正稀缺且具有拓扑的设备。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22560 -->
第三方 LLM gateway 不能仅返回 provider name；每次路径选择要生成 evidence-bound provenance，绑定 policy、provider endpoint、fallback、请求版本与可验证 receipt。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只覆盖受测 gateway/provider；receipt 证明公开路径与策略执行，不证明 provider 内部模型或隐藏处理。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Gateway 从认证与负载均衡入口演进到跨站点、跨 provider 和 Agent protocol 的策略控制点后，routing decision 必须绑定 model/provider identity、capability、queue/runtime、WAN state、privacy policy、session 与 receipt。Gateway 可以选择路径，却不能同时拥有不可验证的明文和执行 authority。

集中策略提高复用与治理，却增加 session stickiness、transport translation、enclave attestation 和单点 blast radius。receipt、身份或重试幂等性无法证明时，应回到直连、固定 provider 或人工批准；engine scheduler 继续拥有 token work，GPU scheduler 继续拥有 Pod placement。

## 自检问题

1. Gateway API 为什么拆分 `GatewayClass`、`Gateway` 与 Route？
2. LLM 流式请求为什么使透明 retry 危险？
3. requests/sec 为什么不是充分的 LLM rate limit？
4. Gateway、EPP、engine scheduler 分别调度什么？
5. EPP fail-open 与 fail-close 的代价是什么？
6. 为什么授权需要绑定实际 model/adapter identity？

## 小结

Gateway 将外部流量转化为带身份、协议、配额和可观测上下文的内部请求。它可以借助 EPP 做 inference-aware endpoint selection，但不进入 token iteration。下一章转向更慢、更稀缺的资源决策：GPU placement。

## Review notes

- `SF-2026-ARXIV-2606-07392` — supp_jun09，Daily2026-06-09补Jun08；[exact-v1](https://arxiv.org/html/2606.07392v1)必要核心/直接反侧及actual owner见本日SUPPLEMENT“后六必要/actual owner”，6分。root独立§40已实际核必要域、完整目标邻接与唯一稿并授此单段窄位；仅按该稿保存，保近文适用条件、代价和反证，不授未测因果/隐私/安全/线上保证，未核完整artifact或复现。root§42唯一非writer实际POST已通过，窄位释放；本注仅同步既成、不授DAY。

- `SF-2026-ARXIV-2606-06924` — Daily2026-06-09补Jun08；[exact-v1](https://arxiv.org/html/2606.06924v1) §3.3/4/5.1–5.3及rewrite validity/单shot方差；只重复观测形成质量/费/整体risk监督，保同结构/100single-shot-v-1DARS、语义sanity非保证、局部反退和全采样费。2+2+2=6、具体gap深入，未核实现/复现；root SUP_REVIEW §16实际必要/actual owner/完整两侧与literal已核并授本单段+注，作者已真实保存并完整自读新增、直接完整两侧及自身H2注；root SUP_REVIEW §17唯一非writer实际POST已通过，指定窄位已释放，不预DAY。

- `SF-2025-ARXIV-2509-15515` — Singer，Daily2025-09-23补Sep22；Cache Bandit exact-v1§3–7必要域，2+1+2=5。只异大小完整response推荐/实体填充分离与有限miss-feedback条件，非engine KV/语义近似命中；保稳定分布/固定问答、offline更强权限和求解/存取/校验未全计净SLO的限制。R8日门/5分、R10必要Source有效；caller/model/policy资格是系统推断，不称作者已实现。未核代码/复现；R22具体owner/原稿纯PRE通过，root本轮fresh窄授后原单段/独立marker及本人注已保存，Sartre R26 sole actual POST通过，指定窄位生效释放，不授DAY。

- `SF-2026-ARXIV-2610-30076` — Daily2026-10-23，Oct22公开；SOURCE_MODEL5.md Q7必要exact-v1/actual owner及逐字PRE经独立oct23_live_org通过，沿原6分。root仅按准许窄位保存，保关键反侧/适用边界/全部费用和原有效正文；未核完整artifact或复现，独立oct23_live_org已完整核新增、直接两侧及本人注，实际写后通过，不授DAY。

- `SF-2026-ARXIV-2604-02319` — Daily2026-04-04补Apr3；[diversity router exact-v1](https://arxiv.org/html/2604.02319v1)必要§2–6/C/D/E/F/G/H1，2+1+3=6。reader actualSource/Ch62逐字PRE/61–63交接通过，root授两body/本人注窄锁，作者实写顺读；只quality-weighted unique集合utility与offline label身份，保OOD/prompt/平均质量反退和prefill/judging/慢路径费用，不授truth/无限覆盖或净SLO。supp_apr04_reader实际正文/完整局部邻接/本人注nonwriterPOST通过，本人注同步后作者实际读回；未核代码/复现，不授DAY。

- `SF-2025-OPENAI-AGE-POLICY`：[Building towards age prediction](https://openai.com/index/building-towards-age-prediction/) 与 [Teen safety, freedom, and privacy](https://openai.com/index/teen-safety-freedom-and-privacy/)，2025-09-16 官方计划。采用年龄推定与可信身份分离的政策约束及隐私/误判代价；预测算法、阈值、误差与部署成效未披露，不作安全保证。正文 policy 分离是明确的系统推断。

- `SF-2026-OPENAI-WEBSOCKET-API-INCREMENTAL`：[OpenAI工程披露](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/)，原RSS事件04/22T10:00Z；核心When API became bottleneck / Building persistent connection / Keeping API familiar / Setting new bar。只采用connection-local API渲染与增量前处理分支，上线`response.create`+`previous_response_id`不是弃用原型`response.append`。up-to40%为作者alpha/client观察，model/hardware并非matched对照，完整precision/length/batch/concurrency/SLO未披露；未复现。资格检查和显式重建是系统设计推断，不是厂商全validator/恢复保证。apr20_resume已完成source→实际owner及literal独立采用，并实际顺读正文57～78及本证据条目，写后复核通过。

- `SF-2026-ARXIV-2606-22560` — primary `arXiv:2606.22560v1`；Method=`arXiv:2606.22560v1 §3 Provenance Model; §4 Gateway-Path Binding; §5 Implementation`；Evaluation=`arXiv:2606.22560v1 §7 Evaluation`；Non-proof=`arXiv:2606.22560v1 §9 Limitations and Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

本章与第 53、56 章形成三层契约：KServe LLM/EPP 管理 endpoint path，第 56 章管理 runtime token state，本章管理外部流量策略。当前 `InferencePool` v1 状态按 2026 年官方文档记录。

官方入口：

- Gateway API overview: https://gateway-api.sigs.k8s.io/docs/concepts/api-overview/
- Gateway API Inference Extension: https://gateway-api-inference-extension.sigs.k8s.io/
- InferencePool v1: https://gateway-api-inference-extension.sigs.k8s.io/api-types/inferencepool/
- KServe control plane: https://kserve.github.io/website/docs/concepts/architecture/control-plane
- Scalable LLM Agent Tool Access in the Cloud（MCP gateway、authorized discovery 与 session-owner routing；Status: Experimental）:
  https://arxiv.org/abs/2607.15593v1

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-13968:start -->
- `SF-2026-ARXIV-2606-13968` — Daily `2026-06-12`；primary `arXiv:2606.13968v1`；Books review `books-review:SF-2026-ARXIV-2606-13968`。

  **已吸收的语义增量：** 跨local/HPC/cloud推理要分离auth/job-dispatch control channel与encrypted token-stream data channel，并让tier routing/context summarization成为显式policy
<!-- daily-books-trace:SF-2026-ARXIV-2606-13968:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15050:start -->
- `SF-2026-ARXIV-2606-15050` — Daily `2026-06-14`；primary `arXiv:2606.15050v1`；Books review `books-review:SF-2026-ARXIV-2606-15050`。

  **已吸收的语义增量：** 跨站点 LLM 路由必须联合 GPU DCGM、vLLM queue/runtime 与 WAN RTT/jitter，并把 replica lifecycle 与 capability constraint 放进 placement state。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15050:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15822:start -->
- `SF-2026-ARXIV-2606-15822` — Daily `2026-06-15`；primary `arXiv:2606.15822v1`；Books review `books-review:SF-2026-ARXIV-2606-15822`。

  **已吸收的语义增量：** agentic routing中gateway不能同时拥有明文与不可验证转发authority；应以三方TLS、privacy-preserving query construction和verifiable billing分拆trust
<!-- daily-books-trace:SF-2026-ARXIV-2606-15822:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16358:start -->
- `SF-2026-ARXIV-2606-16358` — Daily `2026-06-16`；primary `arXiv:2606.16358v1`；Books review `books-review:SF-2026-ARXIV-2606-16358`。

  **已吸收的语义增量：** LLM API router 的 plaintext authority 应收缩到 client-attested enclave；auth/scheduling/accounting 可留在 untrusted host，但目的地必须绑定 measured image
<!-- daily-books-trace:SF-2026-ARXIV-2606-16358:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17949:start -->
- `SF-2026-ARXIV-2606-17949` — Daily `2026-06-17`；primary `arXiv:2606.17949v1`；Books review `books-review:SF-2026-ARXIV-2606-17949`。

  **已吸收的语义增量：** 异构 serving gateway 应联合选择 model 与具体 replica，把质量/成本约束和 queue/load state 放入同一 routing decision；先选模型再盲目 LB 会丢失耦合。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17949:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-15593:start -->
- `SF-2026-ARXIV-2607-15593` — Daily `2026-07-18`；primary `arXiv:2607.15593v1`；Books review `books-review:SF-2026-ARXIV-2607-15593`。

  **已吸收的语义增量：** 新增证据边界：Direct MCP client-to-server connectivity does not scale to heterogeneous transports, large tool catalogs, centralized policy and stateful failover. A gateway can own protocol translation, identity-bound visibility, deterministic retrieval and session placement, but the session identifier and routing state become correctness-critical distributed state. 该 delta 已进入 `books/part-06-ai-infrastructure/62-gateway.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-15593:end -->

- `SF-2026-ARXIV-2604-09360` — Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.09360v1)§3.1–3.2/4.3/5.2–5.4/5.6/6.1–6.3，2+2+2=6协议边界深入；只采preserve同provider/strip跨provider分责和request-scopedtypedstream，不采普适semantic/transitive保持、無损或serviceSLO。保unsupported/topk/cachecontrol丢失与warnings、255/10/6测试人口、自写test循环风险、CPython3.10单硬件与proxy额外hop；未核artifact/实际API部署。reader必要Source/逐字PRE及实际正文/完整邻接/本人注POST通过，作者仅同步此注并实读回。

- `SF-2026-ARXIV-2604-09377` — Apr14补Apr13，exact-v1§3–4及必要synthesis-cost/假设反侧，2+2+2=6具体cold-start支持域gap深入；仅taxonomy synth→allcandidate quality/cost标签与type-mixture预测分责，不采Eq6→7/9实际ELBO或trueposterior/校准。保4×2000/7:1:2、17880/15200 QA与不同judge协议、domain .5402优于difficulty .5274、LR五runs非全主表、造数14.34/10.03非总费及hardware/runtime/SLO ND。reader必要Source有效，有限date/light与reader finalPRE实际通过；supp_apr14_reader实际正文/完整上下邻及本人末注POST通过，作者已实读回；未核实现/复现。

- `SF-2026-OPENAI-WEBRTC-RELAY` — May05补May04，[官方工程披露](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)Architecture/Routing/Global Relay/Implementation/Results，2+2+2=6具体入口分责gap深入；仅采用ufrag首包路由、薄relay soft map与transceiver hard-state分责。未核公开artifact、真实部署、负载/尾部性能或hard-session无损恢复；不以SO_REUSEPORT/thread pinning推任意flow亲和保证。root必要Source、逐字PRE及实际正文/完整邻接/本人note POST已在May05唯一SUP R2通过，作者行政同步并实读回。

- `SF-2025-ARXIV-2510-08439` — Aquinas，Daily2025-10-11补Oct10；Godel R116 exact-v1 §3–7/T1–2/全部5.3首次必要完整消费，HTML333865B；reader PDF2981412/9753722B partial不冒完整。2+2+2=6，仅success-gated成本目标的实际人口与语言router选择/engine全账分责差额深入；保Y(K−λC)非总费用/硬质量优先、候选/失败与重试全费、task/pool反侧及未闭配置，不采80%统一省费或SLO。未核全像素/code/训练线上复现；整体PRE/真实SAVE/完整自读/solePOST只本日canonical后到真实层。
