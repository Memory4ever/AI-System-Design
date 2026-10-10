# 第69章 Trace

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-TRACE`
**Legacy Chapter:** Ch65
**Status:** Draft

**Roadmap Intent:** 链路追踪如何定位请求在复杂系统中的耗时。

## 本章要回答的问题

为什么有 Metrics 和 Logs 仍难以解释一次慢请求？Trace 如何表达并行、排队、重试、异步 handoff 和 token streaming？采集更多 spans 为什么不一定获得更好因果证据？

本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**

## 从总延迟到 Critical Path

Gateway 看到 request latency 10 秒，可能包含：

```text
auth
→ gateway queue
→ endpoint selection
→ backend queue
→ prefill
→ first token
→ repeated decode
→ stream close
```

各组件日志都正常，仍无法知道哪些步骤串行、哪些并行，以及真正阻塞在哪里。Trace 用 span 的 start/end 与关系表达这条路径。

## Span 的最小语义

一个 span 通常包含：

- trace/span identity；
- parent 或 links；
- operation name/kind；
- start/end；
- status；
- attributes；
- events；
- resource/service identity。

Span 不应等于每一行函数调用。边界应落在网络调用、queue wait、scheduler decision、model phase、artifact load、tool call 等能解释系统行为的节点。

## LLM Trace 的阶段设计

一次在线生成可拆成：

```text
inference.request
├─ gateway.auth
├─ route.select
├─ runtime.queue
├─ model.prefill
├─ model.decode
│  ├─ first_token event
│  └─ token progress events or aggregates
└─ stream.write
```

不应为每个 token 固定创建 span：长输出会造成海量数据。可使用 span events、分段聚合或仅记录关键 token milestones，并用 metrics 保存整体分布。

但统一 span schema 只规定字段如何表达，不保证字段真的穿过了调用栈。Provider 可能以不同 response metadata 返回 usage，streaming 与 non-streaming 的交付路径不同，generation 与 embedding 调用也可能经过不同 framework hooks；某层内部消费了 metadata 后，应用层即使使用同一套 telemetry wrapper，仍可能只看到部分信息。因此采集合同还要绑定 backend/API、transport、调用类型与 framework revision，明确哪些 usage、termination reason 和 payload-size 字段应被保留、转换与转发，并用对应路径的测试确认 exposure，而不能由“接入统一 schema”推定观测等价。

字段缺失应记为 unknown 及缺失位置，不能补成零 usage 或据此判定低成本。必要时增加 backend-aware hook，或回退 provider 原始 accounting evidence；这会增加适配、版本回归与采集开销，无法恢复的部分仍需保留缺口。Trace owner 负责字段身份与传递证据，实际计价和结果成本归因交给[下一章 Cost](./70-cost.md#资源时间是共同底座)。这些要求不把 call graph 的相似度升级为因果证据，也不保证任意 framework 或生产 SLO。

<!-- source-family: arxiv:2601.00481v1; semantic-body-binding: telemetry-field-exposure-contract -->

当业务代码不能改动、阶段标签又未显式暴露时，可把采集对象从 wrapper 扩展到正在运行的解释器 frame 生命周期：一条[受限实现报告](https://arxiv.org/html/2601.09258v1)在可附着的 CPython 进程上读取函数与调用上下文，再发出 semantic range 关联 GPU API/kernel；分布式通信还需保存 logical communicator/rank 到 node/device 的映射，不能仅靠一张 call graph 推定慢通信在哪两张卡之间。这增加运行时 hook、参考计数与内容暴露、拓扑映射维护的压力，工程支持域必须绑定解释器、framework/backend 和权限；未覆盖的 native/non-Python 路径应保留 unknown 或退回显式 range。时钟与关联边仍按下节独立校验，纳秒字段不是精度保证，trace/residual 只提供定位线索，不认证因果瓶颈或请求 SLO。<!-- source-family:SF-2026-ARXIV-2601-09258 -->

字段可见后，资源轨迹的形状仍不能代替容量和失败验收。把内存曲线减去baseline、取累计最大值、再按峰值归一化，便于比较相对分配阶段，却会隐藏释放与绝对bytes；用DTW对齐还能比较阶段形状，却不保留原wall-clock间隔。因此normalized profile必须与raw bytes、实际peak、runtime和测量scope并列保存，OOM、timeout、instrumentation error也要留在原运行人口，不能从成功运行的形状相近推断容量风险降低。仅覆盖Python对象或按filename归属的instrument不能默认为native/device全部内存；少量重复的平均形状也不能认证tail安全。采集、重复执行及对齐增加开销，scope或clock不可恢复时应退回带unknown的原测量证据，再由资源与Cost owner判断容量和代价，而非由单位峰值曲线宣称优化成功。<!-- source-family:SF-2026-ARXIV-2601-01215 -->

## Context Propagation 与异步边界

HTTP headers 可传播 trace context；queue、batch、PD handoff 和 tool workflow 需要显式复制 context。Continuous batching 中多个 requests 共享一次 GPU iteration，无法简单用一个 parent-child tree 表达。

可以让 runtime iteration span 通过 links 关联多个 request spans，同时把 request-level queue/phase durations记录在各自 span。Links 表达相关性，不应伪装成唯一父子因果。

共享 batch 的总 latency 还不能直接复制给每个 request。可按 compute-bound 与 memory-bound regime 建模请求对 iteration 的边际资源份额，再把 attribution model 与 model、hardware、TP、kernel/execution-plan revision 一起版本化；它提供可校准的 causal cost share，不是跨 backend 的常数。模型失配、量化或 PD 路径变化时，应回退 batch-level 观测并重新校准，而不能由分摊值反推单请求独占 latency。

<!-- source-family: arxiv:2608.08382v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: dynamic-batch-request-level-causal-latency-share -->

### 跨节点时间戳不是天然的因果顺序

单机或时钟误差远小于阶段间隔时，按 wall-clock timestamp 排序最简单，也足以定位大多数延迟问题。流水线跨越多个节点后，系统可以在吞吐与输出都正常的同时，让 clock skew 把后发生的事件排到前面；此时 trace 仍“看起来完整”，因果解释却已经错误。

同一原则也适用于跨 profiler 归因：framework operator、compiler fusion、kernel invocation 与 hardware counter 应由稳定 semantic region 和 invocation order 连接，而不是事后按近似 timestamp 拼接。互相干扰的 sensors 可以分轮采集，但必须保存 measurement-plan provenance；无法归属的 library 区间是一等证据，不能平均摊给附近算子。收益是可解释 join，代价是多轮执行与 instrumentation drift，必须保留 reference run。

<!-- source-family:SF-2026-ARXIV-2609-11938 -->
<!-- source-family:SF-2026-ARXIV-2609-12299 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-21361:start -->
因此 span 不能只保存时间值，还要保存 clock domain、同步方式、误差/新鲜度界限以及可验证的依赖边。能够携带 request sequence、message ID、queue handoff 或逻辑时钟时，应优先用这些关系重建 happens-before；无法证明顺序的事件要明确标为不可排序，而不是强制拼成时间线。这样把可观测状态从“一个 timestamp”扩展为“时间读数 + 因果约束”，代价是更多 metadata、同步开销与不完全排序。受控多节点实验只显示作者流水线在数毫秒级偏移下出现因果违例，不提供生产通用阈值；在单机、已验证同步或只关心聚合吞吐时，普通 timestamp trace 仍是合理旧路径。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-21361:end -->

## Sampling 的偏差

Head sampling 在请求开始时决定，成本低，却可能错过后来变慢或出错的 trace；tail sampling 在看到完整结果后选择，更能保留错误和 tail，但 collector 需要暂存更多状态。

采样策略可结合：

- errors 与 policy denies；
- high TTFT/TPOT；
- rare model/adapter revision；
- tenant debug window；
- random baseline；
- cost/privacy limits。

只保留慢请求会失去正常基线；只随机采样又可能错过稀有安全事件。

从公开仓库恢复 Agent 轨迹时，采样之前还存在观察资格：配置文件、commit coauthor、branch 名称与 PR label 是不同通道，出现标记不等于已执行，没有标记也不等于未使用。配置可能被忽略，coauthor 取决工具设置，完整交互可能需要认证；共享约定文件更不能唯一识别某个模型。因此 trace population 必须同时保存通道、可见权限、缺失状态和提取规则，区分执行事实与身份推断，不把跨通道缺失补成零活动。<!-- source-family:SF-2026-ARXIV-2601-18345 -->

观察资格改变后，结果排名也可能变化。[一项 coding-trace 方法报告](https://arxiv.org/html/2601.18345v1)引用的 PR 切片在排除 draft 后出现排名逆转，只支持该过滤人口下的证据警示，不能冒充本文重新复现的完整 Agent 能力或人类监督因果。跨通道恢复、权限审计和失败/draft 样本保留都增加采集成本；公开记录不足时应标 Unknown，保留原观测和不同分母，而非用可见成功比例给真实部署签发可靠性。短且显式 instrumentation 完整的流程仍可用普通 trace，仓库标记只作恢复线索。

## Metrics、Logs 与 Traces 的互补

```text
Metrics: aggregate health and alert
Logs: discrete event evidence
Traces: per-operation causal path
```

Exemplar 可从 histogram bucket 跳转到代表性 trace；TraceId/SpanId 可把 logs 挂到 span。三者共享 resource identity 与 semantic conventions 才能关联。

OpenTelemetry GenAI semantic conventions 当前仍在演进。平台应固定内部 schema/version，通过 translation layer 对接标准，避免 dashboard 直接依赖实验字段。

## 安全与成本

Span attributes 同样不能默认包含 prompt/context/output。Trace backend 常被广泛访问，高基数和敏感字段还会同时造成成本与泄露。

Instrumentation overhead 应被度量：serialization、context propagation、collector queue、export failures 与 storage cost。Trace 系统故障不应阻塞普通请求，但高风险 action 的 audit 要另有可靠路径。

当所需证据只是每个 kernel 访问过哪些 memory objects，而不是每个访问地址的因果序列时，collector 还可把分析位置移到 device：在 GPU 上按对象计数，kernel 结束只回传聚合 map，避免 raw trace buffer 满后反复传 CPU、停顿和逐事件分析。这个 summary 能回答特定 working-set 问题，却已丢掉原事件次序，不能冒充完整 trace、并发 live-memory peak 或根因证明。[受限 device-summary 对照](https://arxiv.org/html/2602.22103v1)在 A100/RTX3060 与若干 DNN/语言模型上比较完整 profiling 过程，但 CPU 对照常单线程，NVBit 还包含 SASS 解析；倍数不能只归因 placement 或当作原任务吞吐。额外 helper、计数、驻留和 instrumentation 仍会扰动执行，开销随事件类型/数量改变，4MB 示例也不是通用上界。应绑定 capture scope、object identity、丢弃字段，并按相同事件/evaluator计收集、传输、分析及原 workload 的费用；需要完整时序、范围未覆盖或扰动不可接受时保留 raw trace/CPU分析、较粗采样与明确 unknown，不因 passive 未改程序数据就宣称零干扰。<!-- source-family:SF-2026-ARXIV-2602-22103 -->

## 从 Linear Trace 到 Root-cause Graph

### 从单一 Monitor Score 到多维、分权的运行证据

单一安全分数在 observer 可信、风险维度相关且只需粗粒度 gate 时便于部署；monitor 与 Agent 同源、可能共享盲点甚至串谋后，一个 scalar 会隐藏“目标一致但违反约束”或“推理看似连贯但 action trace 不一致”的结构。Trace owner 应保留 goal alignment、constraint adherence、reasoning coherence、safety awareness 与 action-trace consistency 等分维 observation，以及每个 observer 的身份和分歧。

这些 signal 可以由不同模型与 deterministic heuristic 分权产生，最终 gate 只组合有 provenance 的证据。分权降低单一 observer 控制全部判断的风险，却增加调用、阈值校准和相关失败；维度也不是安全真值。观察者意见不一致、输入超出校准域或高副作用 action 到来时，应回退最小权限、隔离执行和人工升级。

该结构为后续 root-cause graph 提供可追溯 observation，而不是直接宣称因果。作者 519 样本只属于 heuristic、intent analyzer 与多维评分组合的 attack/honest 实验；separation-of-duties 的结果来自另一次小样本运行，两个阈值仅有 20 和 7 个样本，不能合并成同一规模的分权安全证据。这些结果不证明开放生产环境的安全率，也不能证明模型调用彼此不存在共同盲点。

<!-- source-family:SF-2026-ARXIV-2604-03968 -->

### 验证状态必须是带授权者的单调 Promotion

在单一可信 reviewer、低风险 artifact 中，给 claim 维护一个可覆写的 `verified=true/false` 足够直接；当作者、AI auditor、工具和人工共同参与时，同一个布尔值会抹掉“谁依据什么把状态提高到哪里”，也允许后来的低权限动作静默覆盖更严格的判断。Trace 因而不只记录 claim 与 source，还应把每次验证提升保存为不可变事件：

```text
claim + generating activity
→ evidence/access state
→ promotion event(grantor, authority, policy revision, evidence pointer)
→ current verification level
```

Promotion 必须单调并受 authority ceiling 约束。例如，AI 可以完成结构检查、来源定位或给出待审判断，却不能自行授予 human-confirmed 状态；vendor/source 被保存、artifact hash 匹配，也只证明字节身份和可访问性，不证明内容真的支持 claim。Validator 应拒绝没有生成 activity 的 claim、越权 promotion 和缺少 evidence pointer 的高等级状态，而不是在 dashboard 上补一个看似完整的标签。

这种状态机提高了 provenance 的可追责性，却增加 schema、身份/密钥、CI、存储和人工 promotion 成本；它仍依赖 producer 如实记录，无法从图结构本身得到真值。缺少独立 reviewer、provider-signed witness 或可复核 source 时，应保留未验证 gap，并回退人工审阅或更低验证等级。单人、短生命周期且不触发发布决策的草稿可以继续使用简单状态，但不能把它复用于高风险 release gate。Exact-v1 的单仓库自举案例只证明其 schema/validator 能执行这些结构与权限不变量，不证明遥测诚实、跨团队适用或 claim 为真。

<!-- source-family:SF-2026-ARXIV-2607-25637 -->

分布式请求与 Agent workflow 往往包含并行 branch、共享 tool、retry 和异步回调。按时间读取完整 trace 能恢复
“发生过什么”，却容易把靠近失败的 span 误认成原因；只让 LLM 总结所有日志又会把噪声、Prompt 长度和不可
复算判断一起扩大。诊断层可以在 immutable trace 上构建一个派生 dependency graph：

```text
versioned spans, logs and artifacts
+ harness / code / tool / prompt dependency priors
→ failure-node identification
→ backward causal slice over corrupted data/control flow
→ candidate responsible module and evidence subgraph
→ reproduce, patch, regression-test or abstain
```

Graph owner 只拥有诊断 view，不得改写原 trace；candidate root cause 也不能直接授权自动 patch。Dependency prior
错误会漏掉真实边或制造伪因果，并行 branch 的时间相关不等于控制依赖，black-box tool 还可能没有足够结构。
因此输出必须保留被排除/保留 span、规则/模型版本、置信与复现实验。Full-trace manual review 在高风险事故、
依赖图不完整或低频新故障中仍是正确旧方案；结构化 slicing 适合重复 pipeline 和可见度足够的系统。STRACE
提供了 structure-guided attribution 的实验性证据，不证明 observational trace 本身已经识别真实因果。

Root-cause graph 之外还有一类更直接的审计问题：Agent 是否明知 system instruction 或 task rule，却在后续决策中
违背它。只检查最终 outcome 会把“偶然成功但过程越权”和“合规执行但环境失败”混在一起；只对单个 span 打分又
看不到 rule 如何跨对话、规划与 tool event 传播。一个受限的 trace auditor 可以先从版本化 instruction 中抽取
可检查规则，再以整条 trace 为 evidence 对每条规则作判断：

```text
versioned prompt / system policy
→ extracted behavioral rules with provenance
→ dialogue + decision + tool-event trace
→ rule-conditioned process judgment
→ deterministic effect receipt / human review for consequential actions
```

这样 outcome 与 process evidence 被分离，规则违反可以定位到具体 transition；代价是 rule extraction、judge
一致性、trace 隐私和存储成本。模型 judge 只能作为 sensor，不能替代确定性 authorizer 或真实 side-effect receipt；
规则抽错、instruction 冲突或 trace 缺失时必须输出 Unknown，而不是“未发现违规”。短且确定性的 workflow 仍应
优先使用状态机断言；语义 trace auditor 适合规则难以完全形式化、但所有关键事件均可见的路径。作者评估只支持
所测 Agent traces 的检测能力，不构成生产合规率。<!-- source-family:SF-2026-ARXIV-2603-23806 -->

### 从 Root-cause Hypothesis 到受限 Repair

Root-cause graph 缩小调查范围后，还不能把诊断直接提升为修改生产行为的权威。多轮 Agent 的下游症状可能由上游 tool error、环境漂移或模型判断共同造成，因此应把四类状态分开版本化：trace evidence 记录实际发生的 span 与 artifact；diagnoser 只提交带依据的 causal hypothesis；repair controller 根据 side-effect class、权限和回滚条件决定是否允许 patch/rerun；rerun result 再成为新的 evidence。

一次 rerun 成功会提高该修复路径的实用置信度，却可能来自随机采样或环境恢复，不能反向证明原 attribution 必然正确。这个分层获得可审计的 recovery loop，也新增 trace 隐私、schema coupling、诊断误归因和 repair authority 风险。短、确定、规则清晰的 workflow 仍适合人工或固定规则诊断；高副作用动作必须要求人工批准、独立 regression evidence 或 abstain。

因此，归因实验不能把独立重试当作对原 trace 的检验。应保存候选错误点之前的执行 prefix，只在其附近施加 diagnosis-specific intervention，再验证新的 outcome。Faithfulness gate 检查第一步重生成是否遵守修复计划：soft 模式仅记录判断，hard 模式拒绝偏离并有界重试。即使任务恢复，若靠无关改动绕开失败，也不能据此支持原诊断。

通过这种受控重放，outcome 从错到对只说明该 intervention 足以恢复结果，不证明它是唯一、最小的原因或最早因果起点。它增加重执行、判断器和环境恢复成本；oracle answer 不可得时，proxy verifier 的证据更弱。不可逆副作用、环境缺失或多处共同错误，应保留多个假设、人工审计或停止，而非强行产出单一归因。`arXiv:2606.09071v1` 的 §3–4、Appendix R 支持这一受限机制，不提供生产因果保证。

<!-- source-family:SF-2026-ARXIV-2606-09071 -->

随机 policy 还留下另一层归因问题：即使不修复任何内容，只重新采样一个 action，也会重滚全部下游决策。因而单次“重跑成功”没有稳定比较基线。可以固定 factual prefix，以同一 policy 的重采样作为 null intervention，再分别改变 action、observation、context 或 policy，执行有界的多次 continuation，比较 outcome 分布及其不确定性；provider 在 temperature=0 时仍可能变化，应记录 replay action-match，而非声明精确重放。诊断层拥有比较与假设，不取得外部 effect 的重执行权限。

这一比较估计的是随机续跑中的总效应，不是当前步骤的直接效应：早期无关步骤也可能因重新采样后面的关键决定而显得有效。选择最后一个仍具有可辨效应的重决策点，或用有预算的 coalition/Shapley 估计拆分交互，是不同归因分支，不能宣称已找到普遍唯一原因。[Causal Agent Replay 的受控 SCM 验证](https://arxiv.org/html/2606.08275v1)只覆盖 planted cause 与 mocked tools；有限样本区间、judge 噪声、多个步骤及额外 rollout 成本都会限制判断，matched continuation randomness 仍未被其实现解决。真实不可逆动作、环境无法重建或预算不足时，应保留多个原因与 unknown，回退人工调查；确定性的短流程仍先用状态机断言和固定重放。<!-- source-family:SF-2026-ARXIV-2606-08275 -->

当系统尚未拥有可靠 dependency graph 时，还可以先从 raw trace 中检索相似成功/失败记录，由 judge 生成受限
标签，再学习“当前执行偏离成功轨迹分布的哪里”。这形成另一条诊断演进：

```text
raw trace search
→ versioned judge labels
→ success-manifold / deviation model
→ suspicious span or transition
→ reproduction and root-cause confirmation
```

它比固定阈值能利用跨 span 模式，却把 retrieval corpus、judge、embedding、成功定义和 distribution drift 都
写入诊断状态。Deviation 只定位异常，不证明因果；新版本产生的合法路径也可能被旧 manifold 误报。因而结果
只能缩小调查范围，必须回到日志、artifact、复现和 regression test。低频新故障或 judge 无法校准时，规则与
人工 full-trace review 仍是正确基线。

### Trace Optimization 必须把成本与规则决策写入同一证据对象

### 动态模型路由需要独立 Route Receipt

只记录最终模型名，在静态单模型服务中足够；动态路由会让候选集、策略版本、预算、租户约束和健康状态共同决定选择。每次路由应生成 receipt，保存候选快照、约束、策略 revision、选择结果、fallback 与可披露 provenance。Router 拥有选择动作，receipt 只记录事实，release/cost owner 决定是否接受该路径。

完整 receipt 增加存储、隐私与延迟，并不能证明被选模型最好；低风险固定路由可保留简化日志。字段缺失或策略不可重放时，只能诊断最终调用，不能声称重构了决策。现有 exact-v1 只支持作者的动态路由设定。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01710 -->

当结论会驱动真实 action 时，线性 trace 还要升级为 claim-centered evidence graph：每个 claim 指向所用 observation、变换和 policy revision，再连接 action proposal、实际 artifact 与独立 validation。Trace owner 保存“发生了什么”，graph view 表达“哪个证据支持哪个决定”，validator 只确认声明的后置条件；任一边缺失都不能由最终成功反推补齐。它增加 lineage 与 join 成本，却使局部证据撤销可以精确失效下游决定。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18398 -->

完整保存原始 trajectory 在规则少、成本低或审计风险高时最可靠；当 Agent run 变长后，仅凭最终成功与总成本去删除步骤，会混淆“补回缺失依赖的必要 repair”和“对结果无影响的昂贵绕路”。一种受限演进是把 child trace、逐步 billed cost 与 rule type 固化为同一 TraceCard，再让 preserve、prune 与 repair rule 对这个版本化对象提出变换：

```text
immutable parent trajectory
-> child trace + per-step cost + rule type
-> preserve | prune | repair proposal
-> replayed task outcome and cost receipt
-> accept rule revision or retain parent
```

这让成本优化拥有可回滚 lineage，但 rule 命中不是因果证明。现有实验只有 30+30 tasks、单一 model/seed；在 17 个 baseline-success held-out tasks 中，只有 2 个匹配两条 learned prune rules，preserve rules 还出现 3 个跨 benchmark 回归，部分 heuristics 没有得到验证。没有稳定 child trace 或 cost attribution 时，不应自动蒸馏、剪枝或把失败归因给某一步，而应回退原 trajectory 与人工 rule review。低成本 preserve path 与 cost-aware prune 因此是并存分支，不是后者对前者的替代。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23853:start -->
TraceCard 只有在变换前后同时保存行为与成本 receipt 时，才足以承载可审计的 trajectory optimization。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23853:end -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-09692:start -->
agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-09692:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-10937:start -->
在 Trace 章节补一段 compiler rewrite provenance：non-injective transform 后由 observable behavior 重建 lineage；显式 ID 仍与其共存。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-10937:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14805:start -->
#### 预测器只能分配 Replay Budget，不能确认因果

长 Multi-Agent trace 中，逐条重放所有 branch 最可靠，却会让 counterfactual replay 成本随参与者和分支数增长。诊断层可以先把 immutable events 编译成保留数据/控制依赖、agent/tool identity 与 commit boundary 的 knowledge graph，再用经过校准的 predictor 为最可能改变归因的节点分配 replay budget。Graph 与 predictor 只拥有证据排序权，真实 replay、环境回执或人工调查仍拥有因果确认权。

这种两阶段路径降低平均重放成本，却可能因图缺边、训练分布漂移或 predictor 过度自信错过根因；“预测 replay 会失败”不是零重放证明。作者结果只覆盖其 trace 与 oracle 设置，关键安全事故、低置信候选或依赖不可见时应回退 full replay/人工审计，并保留未检查 branch，而不能把预算优化写成因果结论。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14805:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-26449:start -->
让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-26449:end -->

### Contamination 先表现为 Control-flow Divergence

不确定或被污染的 evidence 未必直接出现在最终答案，它可能先改变 decomposition、routing、tool choice 或 retry path。因而 provenance 不能只跟随文本片段，还要穿过 artifact transformation 与 workflow edge，记录相同输入下控制流何处首次分叉。该图能定位传播链，却受 synthetic corruption model 与 trace completeness 限制；缺少因果 intervention 时只能报告关联，不能把 divergence 自动解释成根因。

<!-- source-family:SF-2026-ARXIV-2604-27586 -->

### Failure Attribution 必须从阶段定位升级到可证伪的因果候选

终局 task failure 只说明某处出错，不能指出是 perception、planning、tool、environment 还是 recovery。先把 trajectory 分解为带输入、状态、动作、observation 与 commit 的 stages，可以定位最早异常阶段；但“与失败同时出现”仍只是相关。

当失败标签稀缺时，可以只用成功轨迹拟合连续时间 reference flow，再以失败轨迹偏离该流的位置生成 anomaly candidates。这个 one-class 路径避免先编造失败 taxonomy，却依赖成功样本覆盖、表征与时间对齐；conformal threshold 只校准检测率，不证明偏离步骤是根因。高风险诊断必须用 replay、干预或 counterfactual 验证，证据不足时保留 multiple candidates。

CLI coding-agent 与受控 benchmark 的结果只支持各自轨迹和模型，不能外推为通用 failure prevalence。低成本 final-only metric 仍适合回归总览，但不能承担修复归因。

<!-- source-family:SF-2026-ARXIV-2607-09510 -->
<!-- source-family:SF-2026-ARXIV-2607-12747 -->

## 本章在知识树中的位置

本章完成 Evidence Plane 的三种信号。下一章使用这些 evidence 回答经济问题：资源时间如何转成一次训练、一次成功请求和一个满足 SLO 的 token 的真实成本。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22698 -->
black-box agent forensics 需要固定 probe transcript、system-prompt/topic 条件与 attribution threshold，把模型/配置 fingerprint 当 evidence 而非身份真值。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；synthetic transcript 与 threshold/config scope 限制外推；provider 更新、sampling 和 prompt drift 会使 fingerprint 失效。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Trace 从请求 spans 演进到跨 model、tool、workflow 和 environment 的语义因果链后，必须同时记录执行顺序、数据/状态依赖、版本与外部 effect。只有这样，终局 failure 才能回溯到首次有害 commitment，而不是把相关步骤误当原因。

更细 trace 提高 replay 和 attribution，却带来数据量、隐私、采样偏差和跨系统 clock/identity 问题。关键 action 与 state transition 需要不可丢的 receipt，普通高频 span 可以采样；trace 缺口存在时只能缩小 claim，不能由流畅 narrative 补全不存在的事件。

## 自检问题

1. Trace 比分散日志多提供了什么信息？
2. 为什么不应给每个 token 创建 span？
3. Continuous batching 为什么需要 span links？
4. Head 与 tail sampling 的偏差分别是什么？
5. Metrics、Logs、Traces 如何通过 identity 关联？
6. 为什么 GenAI semantic conventions 需要版本边界？

## 跨层 Trace 只能提出因果候选，不能自动证明根因

大模型服务的请求会依次穿过 host queue、runtime、CUDA launch、Kernel 与通信层；任何单层 trace 都可能把上游等待误判为本层瓶颈。系统应让同一 request identity 贯穿 NVTX/CUPTI/日志事件，先重建 call-chain tree 和时间有向关系，再通过重放、配置干预或受控对照验证 causal slice。这样用更高采集成本与时钟同步复杂度换取可操作根因；层间关联缺失、采样过稀或没有干预时，只能报告 correlation。`arXiv:2608.01975v1` 仅在作者环境中支持该诊断流程，不证明自动搜索得到的路径就是生产事故唯一根因。<!-- source-family:SF-2026-ARXIV-2608-01975 -->

## 小结

Trace 让请求经过多个控制面和数据面时仍保留 causal context。好的 tracing 记录关键边界与决策，而不是最大化 span 数量。下一章将可观测事实转换为成本归因与优化约束。

### Trace 需要行为 Taxonomy，不能只有自由文本摘要

运行时日志若只保存 tool call 和自然语言说明，很难跨任务比较 Agent 如何探索、恢复和提交。Grounded behavior taxonomy 可以把行动分类、上下文、前后依赖和结果编码成可聚合 trace，使 evaluation 与 incident analysis 共享同一行为坐标。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13625 -->

Taxonomy 会压平边界行为，自动分类器也可能错标；现有大规模描述分析不能证明分类完备。未覆盖行为应保留原始事件并允许 taxonomy 演进，分类不确定时回退 raw trace 而非强行归类。

## Review notes

- `SF-2026-ARXIV-2601-18345` — Daily `2026-01-28` 增量；[exact-v1](https://arxiv.org/html/2601.18345v1) §4/5.2–5.3，repo 观察 channels 与 draft population 的测量差额，3+1+2=6；本文引用切片不是独立重现，标记不唯一识别 model/human oversight。jan28_review 实际必要原源/owner/PRE通过，root先授窄锁；jan28_review 实际完整局部邻接、新两段与自身末注POST通过，不授DAY；未核artifact或复现实验。

- `SF-2026-ARXIV-2601-01215` — Daily `2026-01-07`；[MemoryDynamics exact-v1](https://arxiv.org/html/2601.01215v1) §3.2/3.3/3.5、4.1–4.3、5.3–5.5及必要language/budget/aggregate补段。3+1+2=6，shape-normalization/DTW与capacity风险的测量反证缺口深入；保baseline/cummax/unit-peak/clock损失、tracemalloc scope和已排除的OOM/timeout/instrument错误，不授N5/r10的tail保障。root实际必要源与Ch69 owner写前及实际一段、邻接与末注非作者POST通过；未运行代码或复现。

- MAESTRO（`arXiv:2601.00481v1`）：实际审阅 §3.1.1/3.1.2、§4.1/4.3、§5.1 与 A.2.2，采用统一 schema 与 provider/transport/framework 字段 exposure 的区别；12 个 predefined instances 的有限运行与 Jaccard/LCS 不证明生产可移植性或因果归因，hardware/precision 为 Not Disclosed。root 非作者必要源→owner 及实际写后复核通过。https://arxiv.org/html/2601.00481v1

- `SF-2026-ARXIV-2604-21361`（Status: Experimental）：exact-v1 支持“功能与吞吐正常而 timestamp 因果顺序已错误”的受控多节点案例；作者观察到的具体 skew 转折绑定其 pipeline、同步与 instrumentation，不是生产告警常数。https://arxiv.org/abs/2604.21361v1

- `SF-2026-ARXIV-2604-23853`（Status: Experimental）：exact-v1 支持 child trace、逐步成本与 rule type 组成 TraceCard，并在作者 30+30 task contract 中评估 preserve/prune/repair；不证明启发式规则具有跨模型、跨 benchmark 的稳定因果有效性。https://arxiv.org/abs/2604.23853v1

- **TraceGuard（arXiv:2604.03968v1；Status: Experimental）**：exact-v1 Table 2 的 519 样本属于组合 detector；Table 5 的 separation-of-duties 来自 earlier run，两阈值样本量分别为 20/7，不能混作同一规模证据；不证明 observer 独立、攻击覆盖完备或生产安全率。https://arxiv.org/abs/2604.03968v1

- `SF-2026-ARXIV-2606-22698` — primary `arXiv:2606.22698v1`；Method=`arXiv:2606.22698v1 §3 Approach`；Evaluation=`arXiv:2606.22698v1 §4 Experiments; §4.3 Evaluation`；Non-proof=`arXiv:2606.22698v1 §7 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Trace success-manifold deviation diagnosis（Status: Experimental）:
  https://arxiv.org/abs/2607.12747v1

本章承接 Part V 请求状态机，并为 Part VII tool/workflow trace 留出扩展：Agent trace 会增加 context retrieval、planning、tool side effects 与 human approval，但沿用相同 propagation 原理。

官方入口：

- OpenTelemetry signals: https://opentelemetry.io/docs/concepts/signals/
- OpenTelemetry tracing: https://opentelemetry.io/docs/concepts/signals/traces/
- OpenTelemetry semantic conventions: https://opentelemetry.io/docs/specs/semconv/
- STRACE / From Noisy Traces to Root Causes（structure-guided root-cause attribution；Status: Experimental）:
  https://arxiv.org/abs/2607.07702
- AgentDebugX（exact v1 + event-time commit；Status: Experimental）：https://arxiv.org/html/2607.18754v1
  - 证据边界：184 localization traces、73 个 initially failed GAIA tasks；strict exact-step attribution 仍低，一次 rerun 不能证明因果归因或跨框架安全性。

### Daily integration evidence trace

<!-- daily-books-trace:SF-2026-ARXIV-2607-25637:start -->
- `SF-2026-ARXIV-2607-25637` — Daily [2026-07-29](../../papers/2026/07/29/README.md)；primary `arXiv:2607.25637v1`；正文锚点“验证状态必须是带授权者的单调 Promotion”。本章吸收 grantor、authority ceiling、单调 promotion event 与“artifact 可访问性不等于 claim truth”的边界；单仓库自举案例不证明跨组织 truth verification。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25637:end -->

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24626: `arXiv:2606.24626v1`; exact-v1 URL=`https://arxiv.org/html/2606.24626v1`; Method=`https://arxiv.org/html/2606.24626v1 — §2 Methodology: SAFARI`; Evaluation=`https://arxiv.org/html/2606.24626v1 — §3 Experimental Setup; 4 Results; A/B/C appendices`; Non-proof=`Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26449**：Primary `arXiv:2606.26449v1`；Method `https://arxiv.org/html/2606.26449v1 — §ProvenAI provenance-native trace schema and evidence links`；Evaluation `https://arxiv.org/html/2606.26449v1 — §Generated-answer trace/evidence evaluation`；未证明边界 `https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-09692:start -->
- `SF-2026-ARXIV-2606-09692` — Daily `2026-06-09`；primary `arXiv:2606.09692v1`；Books review `books-review:SF-2026-ARXIV-2606-09692`。

  **已吸收的语义增量：** agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09692:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-10937:start -->
- `SF-2026-ARXIV-2606-10937` — Daily `2026-06-10`；primary `arXiv:2606.10937v1`；Books review `books-review:SF-2026-ARXIV-2606-10937`。

  **已吸收的语义增量：** 在 Trace 章节补一段 compiler rewrite provenance：non-injective transform 后由 observable behavior 重建 lineage；显式 ID 仍与其共存。
<!-- daily-books-trace:SF-2026-ARXIV-2606-10937:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14805:start -->
- `SF-2026-ARXIV-2606-14805` — Daily `2026-06-12`；primary `arXiv:2606.14805v1`；Books review `books-review:SF-2026-ARXIV-2606-14805`。

  **已吸收的语义增量：** 长Multi-Agent trace应编译成event knowledge graph，并用校准predictor分配稀缺counterfactual replay budget；预测只排序证据，不替代replay oracle
<!-- daily-books-trace:SF-2026-ARXIV-2606-14805:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20374:start -->
- `SF-2026-ARXIV-2606-20374` — Daily `2026-06-19`；primary `arXiv:2606.20374v1`；Books review `books-review:SF-2026-ARXIV-2606-20374`。

  **已吸收的语义增量：** `ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters` 路由到 `PLATFORM-TRACE`：ARGUS 将万卡训练诊断从节点日志提升为跨 rank/collective/network/storage 的统一 trace identity；collector 控制采样与时钟映射，diagnoser 只在证据图上定位瓶颈，超预算时降采样并保留关键 span。代价是 telemetry overhead 与相关性误判。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20374:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-12747:start -->
- `SF-2026-ARXIV-2607-12747` — Daily `2026-07-15`；primary `arXiv:2607.12747v1`；Books review `books-review:SF-2026-ARXIV-2607-12747`。

  **已吸收的语义增量：** 新增证据边界：A latent continuous-time trajectory model learns normal flow from successful traces; deviations on failed traces yield step attribution, with conformal detection controlling thresholds. 该 delta 已进入 `books/part-06-ai-infrastructure/69-trace.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-12747:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-18754:start -->
- `SF-2026-ARXIV-2607-18754` — Daily `2026-07-22`；primary `arXiv:2607.18754v1`；Books review `books-review:SF-2026-ARXIV-2607-18754`。

  **已吸收的语义增量：** 新增证据边界：Typed trace capture feeds a multi-turn debugger that narrows agent, step and failure class; the diagnosis is converted into a bounded repair and evaluated by a single rerun. Failure taxonomy and framework integrations are extensible surfaces rather than model truth. 该 delta 已进入 `books/part-06-ai-infrastructure/69-trace.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-18754:end -->

- `SF-2026-ARXIV-2601-09258` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09258v1) §4.1.1–4.1.3、§4.2/5–6/8。6分具体采集接口gap深入，采用 CPython frame→semantic GPU range/API 及 logical rank→physical device 关联；支持域/隐私维护与 unknown fallback 是工程推导，不冒称全解释器、framework、权限或 native 路径实测。scheduler 未进 predictor，normal-baseline warmup/阈值及 suspicion 非 cause；不采用零开销、request SLO 或生产诊断保证。root 已实际必要源/目标 owner 写前核通过，实际新增一段、前后衔接及末注非作者 POST通过；未运行 artifact 或复现实验。

- `SF-2026-ARXIV-2602-22103` — Daily `2026-02-27`；[PASTA exact-v1](https://arxiv.org/html/2602.22103v1) §3/§5.3/§7，blocks34–35/102–104/127。2+2+2=6，device-summary collector位置差额深入；仅kernel访问对象聚合，非完整时序/live峰值/causaltruth；CPU单线程与SASS解析混杂、capture scope/扰动/全profile费用及rawtrace回退近文。root必要源/actual owner PRE通过并授单段窄锁；作者正文/完整邻接/自身末注已实际顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放；未核实现或复现，非日级Gate。
