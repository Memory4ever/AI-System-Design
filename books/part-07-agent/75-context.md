# 第75章 Context

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-CONTEXT`
**Legacy Chapter:** Ch71
**Status:** Draft

**Roadmap Intent:** 上下文是 LLM 的运行时状态。

## 本章要回答的问题

Context 为什么不是“把所有已知信息塞进窗口”？模型支持更长 token length 后，检索、摘要和状态管理是否会消失？Agent context 与持久 Memory 有什么区别？

本章的核心判断是：**Context 是本次模型调用可见的、经过选择和序列化的工作状态。它受 token budget、信息相关性、位置、信任和隐私共同约束；accepted length 不等于 effective utilization。**

## Context 是一次调用的可见状态

一次调用可抽象为：

```text
C_t = assemble(
  instructions,
  user input,
  conversation,
  retrieved evidence,
  memory reads,
  tool schemas/results,
  workflow state
)

y_t ~ p(. | C_t, theta)
```

`C_t` 会随每一步 tool observation 和 workflow transition 改变。模型参数 `theta` 相对稳定，Context 则是 Agent runtime 的高频状态。

Memory 可以跨调用持久化；Context 是从各存储和当前事件中选择出的 working set。二者关系类似 storage 与 working set，而不是同义词。

## Token Budget 是容量约束

设：

```text
T_max     model/runtime accepted context length
T_sys     instructions and policies
T_hist    conversation history
T_ret     retrieved or memory content
T_tool    tool schemas and observations
T_out     reserved output budget
```

必须满足：

```text
T_sys + T_hist + T_ret + T_tool + T_out <= T_max
```

但满足不等式只证明请求可被接受，不证明模型能找到、理解或正确使用其中的信息。第 22 章已区分 accepted length、position generalization、effective utilization 和 system capacity；本章负责 runtime selection。

## 为什么“全塞进去”会失败

更多 token 会增加：

- Prefill compute、TTFT 与成本；
- KV Cache 占用和并发压力；
- irrelevant evidence 与指令冲突；
- lost-in-the-middle 风险；
- sensitive data 暴露面；
- cache identity 和 invalidation 复杂度。

`Lost in the Middle` 的实验说明相关信息位置会显著影响表现。这个结论不能外推为固定排序口诀，却足以否定“只要窗口够长就无需 context engineering”。

### Coding Agent 的工作集目标是 Action 前事实充分，而不是 Token 更多

为 coding task 持续扩张 Context，在依赖事实完整且检索准确时可以减少回看；缺少版本、调用关系或 repository convention 时，多模型可能一致编造，额外无关 token 也不能修复缺失变量，甚至会强化旧约定。Assembly 应在 action 前检查 dependency facts、current code state 与约束是否可用，并让测试/工具结果验证输出；缺失时定点检索或 abstain，而不是无差别加长窗口。该策略增加检索和 precondition checks；小仓库、完整工作集已常驻时直接拼接仍简单。`arXiv:2608.16630v1` 只支持作者 coding-agent tasks 中的 working-set failure，不证明所有错误都由 Context 缺失造成。

<!-- source-family:SF-2026-ARXIV-2608-16630 -->

## Context Assembly Pipeline

可靠 assembly 需要显式阶段：

```text
collect candidates
→ authorize and filter
→ rank by relevance/recency/authority
→ deduplicate and resolve conflicts
→ compress or summarize
→ place with source/trust metadata
→ reserve output and tool budget
```

排序不能只看 embedding similarity。Authoritative policy、current workflow state 与 user intent 可能优先于语义相近文本。冲突内容应保留来源和时间，不应由摘要器静默合并成一个“事实”。

当历史中相邻 turns 共同表达证据时，孤立 top-K turn 还可能切断弱相关但保持连续性的上下文。一个替代分支预存 turn embeddings，到 query 到来时将 relevance 转为归一化 gain，选择若干 contiguous spans，再按原时间次序拼接；它不同于写时固定分段或持久 summary。[DyCP 的限定 span 对照](https://arxiv.org/html/2601.07994v1)支持这种 query-time working-set 选择，不授 turn 相邻即有真实依赖，也不改写原记录的 authority。展示算法先 append 再更新停止量，不能据其文字宣称每个已选 span 都过阈；零方差、耗尽与容量边界仍需实现核验。

无需额外 LLM 分段调用不等于免费：embedding、索引、span 检索与拼接仍占预算，多留低相关 turns 也会增加输入与等待。有限对照中 GPT-4.1 的 full history 已接近此分支，检索遗漏仍会丢掉完整历史可回答的证据；judge 分数及低相关 turn 移除实验不证明全局依赖因果或超长能力。短历史、已常驻工作集或检索不可靠时，保留完整 history、简单 top-K 与原文回读，按实际遗漏/成本选择，不由标称窗口更长或 pruning 更短推断普遍收益。<!-- source-family:SF-2026-ARXIV-2601-07994 -->

Assembly 不一定只有检索或手写规则：也可以训练一个独立的 Context generator，为当前任务生成执行提示，同时冻结真正执行工具的 Agent。训练时先对同一任务取得成功与失败轨迹，用对比 reflection 形成监督样本，再以冻结执行器的结果奖励更新 generator；部署时生成的新提示进入本次 Context。这与检索历史 Memory 不同：经验主要改变 generator 参数，executor 的参数不随该训练更新，生成提示也不因此成为事实或授权。<!-- source-family:SF-2026-ARXIV-2604-07487 -->

这种分责让 Context 构造本身可以优化，却增加离线多轨迹采集、reflection、训练和每次调用的生成成本，并可能学到执行器或环境专属捷径。作者在 AppWorld 等任务中报告了受限收益，但没有包含 RL-only 的完整因子对照，也没有把额外轨迹与运行成本全部匹配，不能据此证明每一阶段必需或普遍比检索更省。任务或工具接口变化后，需要重新验证 generator—executor 配对；训练数据不足、需要严格来源可追溯性或执行器频繁更换时，固定 assembly、原文检索与已有 Memory 仍是合理路径。

## Context Serving 是派生视图生命周期

复杂 Agent 不一定从原文临时组装每次 Context。以代码仓库为例，同一 commit 可以派生
lexical index、dense embeddings、symbol graph 与历史摘要；它们共享 source identity，
却有不同的物理布局、更新路径和查询语义。更一般地，可以把 Context production 写成：

```text
authoritative source version
→ build heterogeneous derived views
→ maintain each view under its own validity rule
→ route a request to compatible views
→ deliver bounded, source-linked context
```

关键不是把所有派生状态包装成一个“统一索引”，而是保留
**operation-specific validity boundary**。Lexical hit、semantic candidate、symbol location 与
prompt history 不是可互换结果；一次 edit 对它们造成的失效范围也不同。只有当 view
identity、source range、freshness status 和 supported operation 都可见时，runtime 才能安全
选择增量维护、复用或完整重建。

CodeNib 预印本把 repository context 作为 multi-view data system 来测量，支持了这一工程
方向；但其结果来自受控、静止 repository snapshots，尚未证明 concurrent publication、
multi-tenant recovery 或 learned online scheduling。因此这里沉淀的是派生视图与有效性边界，
不是对某个实现或性能数字的通用背书。

仓库视图还可以以实际构建与测试产物为依据，而不是让模型仅从文件名推断架构：将 buildable components、只编排其他目标的 aggregators、runners 与 tests 分成不同节点，依赖引用绑定来源文件或构建 call stack，并与 repository revision、build configuration 一起生成可追溯的结构图。缺失来源、断引用或不允许的循环应显式失败，无法可靠恢复的字段保留 Unknown，而不是由模型补成事实。它提供的是 build/test 层的派生地图，不替代代码内部语义、真实构建执行或完整测试验收。<!-- source-family:SF-2026-ARXIV-2601-10112 -->

这种视图用 extractor、schema 校验和更新维护成本减少重复结构探索，但“图中已有事实”仍不保证 Agent 完成正确遍历。[SPADE 的受限评价](https://arxiv.org/html/2601.10112v1)中，少数原本答对的依赖问题反而因浅层读取退步；CMake 自动提取与其他构建系统的手工图不能合成全自动覆盖，七个合成仓库加一个真实仓库的结构 QA 也不是修 bug 的生产提效。预构图成本未计入 QA 时延，重复次数又不足精确估计整体收益。配置漂移、未知边或多跳依赖遗漏时，应重新取构建证据并用显式 closure 查询，必要时回到源文件与工具探索，不能让短 JSON 视图自签完整性。

派生 Context 也不一定等 query 到达后才生产。连续视频、日志或长会话可以在后台将 recent native evidence
压成带时间范围的 provisional summaries，让前台请求只消费当前 buffer 与已生成视图：

```text
continuous observations
-> bounded native-evidence buffer
-> proactive derived context updates
-> query arrives
-> foreground assembly and answer
```

这会把 response-path latency 前移成 always-on compute，而不是减少总工作。无 query 时的浪费、background/
foreground interference、buffer backpressure、summary hallucination 与 FIFO error accumulation 都进入资源合同；
`query-to-answer latency` 必须与 total tokens、compute、energy 和 capacity 分开报告。Video Streaming Thinking 的
实验只支持在其视频问答设置中可以这样隐藏 query 后工作，不证明 textual memory 能替代原始 frames，也不证明
通用 serving 更省。Query 稀疏、需要回看全局证据或 compute-sensitive 时，post-query global reasoning 仍合理；
proactive path 只有在 source time range、derived-state revision、correction/replay 和 scheduler priority 明确时成立。

Derived state 是否存在还不够；对 causal model，**它进入 Context 的顺序**决定能否改变原文的表示。若第一遍读取
长上下文后才得到 task state 或 reasoning trace，把它追加成 `[x,T,q]` 只能影响后续 token，不能重写已经形成的
`x` 表示；在一次 fresh pass 中改成 `[T,x,q]`，则可让 `T` 作为不完美的条件状态指导模型重新读取 `x`。这里
query `q` 在两条路径中都位于末尾，比较的是 state 相对 long context 的前后次序，不是把历史计算放到 query 之后。

Fresh reread 用额外完整 pass、trace tokens 与 latency 换取 order-aware contextualization，也会失去普通多轮场景的
prefix KV reuse。`T` 仍是 model-generated derived claim，必须绑定来源 pass、模型与截断规则，错误 trace 不能覆盖
原始证据；接口不暴露可复用 state、任务很短或 cache reuse 更重要时，单次 `[x,q]`、普通 retrieval 或局部回读仍
更合理。[Trace-as-State 的 matched order evidence](https://arxiv.org/html/2609.02702v1)只覆盖三类长上下文任务和
一次 fresh second pass，未验证 multi-round Agent，不能外推成任意 Transformer 或交互任务的复杂度保证。

当模型可以主动 `writeContext`、`readContext` 或 `deleteContext` 时，Context 从一次性 prompt 又演进成
显式受控的 working state。模型可以把长 observation 压成 notes、暂时移出当前窗口并按需回读，从而让
attention budget 与 durable source 分离：

```text
authoritative observation
→ model proposes context write / read / hide
→ runtime validates operation and records source links
→ assemble a bounded visible view
→ restore raw evidence on demand or audit
```

这里 `deleteContext` 默认只能改变当前可见视图，不等于删除原始 artifact、Memory 或审计记录；model note 也是
derived claim，不是新的 authoritative fact。它以额外 tool calls、state machine、summary drift 和 provenance
管理换取更细的 attention control。短任务和高保真要求下，直接保留原文仍合理；显式 state tools 只有在 source
link、visibility scope、lease、rollback 与 durable-delete policy 分开时才不会把“忘记看见”误写成“已经遗忘”。

### 视觉 Artifact：持久存在不等于进入本次可见上下文

文本工具结果通常还能以摘要和引用表示；crop、mask、overlay 等中间视觉证据却不能把像素完整线性化为文字。
将每张生成图像自动追加到后续请求，在短轨迹里最简单，也让模型始终看得到它；轨迹变长后则重复支付视觉 token，
旧图还可能淹没当前需要比较的细节。相反，只把图像存成文件而不提供可寻址入口，模型又无法主动找回它。
可把这两种状态分开：工具生成的图像进入带稳定 ID、来源与父子关系的 artifact ledger；Context renderer 只把
被显式选入有界 active slots 的像素载荷编入下一次请求。生成图像退出 slot 后可驱逐其 inline payload；
原始输入和文件按各自保留策略继续可回读，因而“看不见”不等于“证据不存在”。这将视觉证据生产交给工具、可见性选择交给
Agent policy、身份和恢复交给 runtime，而不是让一次 tool observation 自动决定永久上下文占用。

有界可见集主要控制重复注入成本，不保证模型会选对或正确解释图像；选择错误可让原本答对的请求退化，
工具和多轮调用也可能比单次 VLM 回答更贵。短任务、图像很少或不信任模型选择时，append-only 仍是合理基线。
一项 static-image sandbox 实验的 compiler-matched 对照支持“有界保留”降低 token 用量，但同为两个可见槽时，
显式选择相对自动保留最近两图的准确率差异未达显著；其本地延迟只限论文披露的单并发推理设置，
不能推广到视频或生产 SLO。<!-- source-family:SF-2026-ARXIV-2609-24362 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-14029:start -->
派生视觉接口不只用于原生图像，也能承载旧文本 observation：逐项渲染较老的工具结果，actions 与近期 observation 仍保留文本，而不是将全部历史改成像素。它改变 consumer 的输入接口，不改变证据身份；搜索服务已生成的摘要，渲染后仍是摘要，不会恢复成原网站事实。原文本、引用与恢复入口仍须保留，stale/fresh 分界与表示选择共同决定当前可见视图。

POINTS-Seeker exact-v1 需要训练 consumer 适应混合表示，并支付渲染、图像编码与原文恢复成本；有限对照中全部转图像反而较差，token 减少不能直接外推为端到端时延或证据无损。长轨迹与模型、任务变化须重测；短轨迹、逐字协议或适配不足时，直接携带文本仍合理。这是与 active slots 并行的表示分支，不是删除原始 artifact 的授权。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-14029:end -->

旧tool observation也可压成soft tokens而不是图像，保留native tool envelope、assistant actions与近期原文本；这只是读取接口，逐字工具参数仍应回读原source。训练同一个adapted decoder读compressed view时，还需另在full-text view对原base分布作anchor：前一项教新表示读取，后一项限制旧接口行为漂移，不能由重建loss好推出工具策略没变。两个view按assistant-token身份而非压缩后的绝对位置对齐；若只缓存top logits与一个tail bucket，约束的是粗化分布，不是全部tail行为。

[受限latent-observation对照](https://arxiv.org/html/2609.31430v1)中，更好literal recall或更强teacher仍可能降低任务成功，默认近期窗口也比uncompressed base退步。扩大硬文本窗口改变quality、encoder驻留和KV预算；observation由text移成soft时还会使旧prefix从变更点失效，encoder缓存与decoder prefix复用要分别计账。受限窗口/并发优势相对同adapted fulltext，且排去最后长任务tail，不能叫全轨迹总成本或可靠性保证。Anchor是软约束而非task certificate；无足够behavior回归、原文可完整驻留或必须逐字时，保留原base/fulltext、较大近期窗口和可恢复source，再按实际task/latency预算选择。<!-- source-family:SF-2026-ARXIV-2609-31430 -->

Context 也可能成为可迭代的 derived state，而不是一次 assembly 的只读结果。多模态 in-context
classification 的一个实验性分支，固定未标注 demonstrations，维护一组 pseudo-label，并用 leave-one-out
方式反复重标：

```text
source-linked demonstrations
→ initialize derived labels
→ hide one label and infer it from the others
→ update a versioned label vector
→ stop by bounded iterations / stability check
```

它把上下文选择推进到 self-conditioned refinement，却会放大早期错标，可能收敛到语义一致但任务错误的
fixed point，并以 `O(iterations × demonstrations)` 的 model calls 换取修正机会。原始 demonstrations 仍是
authority，pseudo-label vector 只是可丢弃视图；真实 label、Memory 或 source artifact 不能被它覆盖。CIRCLE
只在其 open-world multimodal ICL 设置中支持该机制，不证明 LMM 普遍优于 VLM 或迭代一定提高真实 taxonomy。

### Semantic Policy 与 Recoverable Bookkeeping 应分 Owner

短 research loop 把 candidate、已读证据、importance、verification 和 budget 全留在 transcript 中，透明但会随
horizon 溢出。更长 search 可以让 policy 只决定 search/read/curate/verify/stop，把候选池、全文 store、证据图、
verification cache 与 renderer degradation 交给 harness：

```text
policy-owned semantic action
→ harness updates versioned working state
→ bounded renderer builds the next Context
→ raw evidence remains dereferenceable
→ crash/replay restores bookkeeping without inventing decisions
```

这降低模型做 bookkeeping 的负担，却使 schema、renderer、eviction、cache freshness 和 train/eval/serve interface
成为行为合同。Full transcript 在短任务和最高透明度要求下仍合理；deterministic top-k 在单跳与紧 SLO 下更稳。
Harness-1 的作者实验支持固定模型会因 interface 改变而改变可用能力，但 component ablation 未重训、verifier/
compression 也会错，因此不能把 harness gain 归因成模型能力提升。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07134:start -->
Web Agent 若把完整 DOM/AXTree 平铺进 Context，短页面上最透明；页面变长后，逐元素截断会切断导航、表单、内容区等功能关系，使 token 仍在却失去可操作结构。一个有界分支先按功能区域组织可交互元素，再增量维护 PageDigest：policy 根据当前目标请求区域，renderer 生成下一轮 view，原始 AXTree/DOM 继续作为可回读 authority，而摘要不能自行发明控件状态。

这减少无关元素占用，却新增 region segmentation、digest freshness、跨页 identity 与隐藏元素遗漏。作者证据只支持其网页任务、浏览器表示和 evaluator，不证明功能区域在所有站点稳定。页面短、结构异常、无障碍树缺失或关键控件无法定位时，应回退 `view_all`、完整重新观察或直接读取原始树；任何外部副作用仍需 Tool/Workflow 层单独批准。<!-- source-family:SF-2026-ARXIV-2605-07134 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07134:end -->

## Context Compression 的损失

Summary、extractive compression 和 structured state 都可减少 token。压缩函数可写为：

```text
C'_t = compress(C_t, task, budget)
```

目标不是最短，而是保留对未来决策充分的信息。摘要可能丢失 exception、否定、数字和 provenance；递归摘要还会累积漂移。

压缩之外，还可以把长原文留在外部环境，由模型用程序选择、变换并回读片段。但“能访问超过窗口的输入”和“值得递归调用子模型”是两个不同判断：前者来自外置原文与选择接口，后者要看任务是否需要子调用完成局部语义处理，还是根模型用代码就能筛选、聚合。应对照同样可访问原文的 no-subcall 分支，而不只对照被窗口截断的普通调用；局部新证据中，某一模型在代码问答和文档查找上去掉子调用反而更好，在信息密集的分类/成对聚合任务上却从子调用受益，因此不能把 external access 的收益统一归因于 recursion。<!-- source-family:SF-2026-ARXIV-2512-24601 -->

这一选择还要绑定根/子模型、任务样本和 evaluator：不同 child 配置不是相同推理预算，API 费用均值也不能代替硬件成本或尾时延；同步子调用、返回失败与少数长轨迹会改变端到端代价。原文、代码、片段范围和调用 provenance 应保留为可重放依据，在子调用无增益、成本失控或验证失败时回退程序化读取与有限 Context，而不是默认继续递归。外部执行是否允许访问文件、联网或产生副作用，仍由 Tool 层的权限与执行器决定，长上下文接口不授予这些能力。

固定周期压缩在 observation 短且预算宽松时易于重放；但若一条长工具结果即将进入窗口，先追加再裁剪可能已经溢出，盲目提前全量压缩又会丢掉仍有余量时可保留的证据。更精细的 admission 顺序是先知道待载入 observation 的长度和当前 headroom，再决定不压缩、只聚合部分旧片段，或在预算紧张时聚合更多历史，最后才载入正文。Context runtime 必须拥有容量检查与最终 commit，模型的聚合选择不能越过原文保留、policy pinning 和可回读引用。<!-- source-family:SF-2026-ARXIV-2604-01664 -->

这种延迟载入以额外的计数、决策和压缩工作换取更少的无谓信息损失，也把长度估计错误、片段级摘要失真与压缩耗时带进关键路径。作者仅在组合问答与长程网页搜索设置中测试了预算条件化、分段聚合及渐紧预算训练；它不证明训练出的策略在任意工具输出、长窗口或生产 SLO 下最优。短轨迹、原文可完整驻留、长度未知或高风险证据不宜压缩时，固定保留余量、拒绝过长 observation 或外置原文并按需回读仍是合理分支。

压缩准入还要算总时间，而不只是比较压缩前后的 token 数：同一请求上，`T_compressor + T_target(compressed) < T_target(original)` 才有时延收益；还要同时验实际压缩率、答案质量和压缩器的显存占用。短输入、便宜的目标模型或较慢的压缩器会使前处理吞掉 prefill 节省；长输入、可摊销的压缩结果或受限显存则可能改变选择。这个 break-even 随目标模型、硬件、长度、批量与并发重算，不能用单一压缩比例作为通用策略。现有作者实验只覆盖所测 LLMLingua 分支、模型/设备与任务，未建立生产尾延迟或任意证据保真保证。<!-- source-family:SF-2026-ARXIV-2604-02985 -->

压缩容量也不必只依赖原文长度。一个受限分支让 query-aware encoder 读取分块 Context，由其末端 hidden-state probe 估计相关内容长度 `L_hat`，再以 `k=min(L_hat/r,k_max)` 决定 soft-token slots，并把兼容 K/V 交给目标 reader。它把固定 slot 数变成 query-adaptive capacity，但相关长度不是充分证据，也不证明压缩结果可供任意 reader 使用。Teacher 相关标注、encoder/probe 与 ratio/max policy 都须保存身份，额外 encoding、probe 和质量回归也要计入 break-even；[局部压缩对照](https://arxiv.org/html/2602.03226v1)显示短输入可能因 slots 过少而退步，不支持“压得越短越好”。长度估计失配、必要细节被丢掉或总成本不合算时，应扩大 slots、回读原文或退回固定容量/未压缩输入。
<!-- source-family:SF-2026-ARXIV-2602-03226 -->

重复日志还可以走另一条分支：不概括含义，而把重复子串替换为短标记并附字典。此时应把字典、标记和说明一并计入目标 tokenizer 的输入预算，并区分两个接口：软件按规则还原原文，以及模型直接在编码态完成任务。前者可以是确定性的 codec 合同，后者仍依赖模型是否正确查表、保持跨行关系并执行目标分析；可逆编码本身不会把这种能力一并交付。<!-- source-family:SF-2026-ARXIV-2604-13066 -->

因此，解压 exact match、字符相似度与目标任务正确性要分开验收，不能把较高的字符串重建分数当作日志诊断或跨记录推理的保证。作者的重复日志实验支持字典表示具有压缩空间、所测模型能够在部分协议下重建文本，但没有验证目标 analytics，也没有证明解压是所有语义任务的能力下界。重复度低、字典开销大、目标任务依赖未验证的编码态操作时，原文或先由软件解码再调用模型仍合理；高风险记录的原始 artifact 和逐字约束不能因 codec 可逆而移交给模型猜测。

"充分"必须相对于未来任务定义，而不是压缩器自认为语义相似。跨 session handover 可以按三层保存：必须逐字保真的决策、约束与授权；对已知 future-query family 足够的统计量；以及无法安全归约、可供以后回读的原始 observation。理论上最小状态只需保持未来 target distribution，但开放 Agent 通常不知道未来 query，也无法证明自动摘要已经达到 predictive equivalence，所以高风险或任务未知时不能删除原文。

这种分层用较小 handover state 换 writer bias、任务分布假设和错误归约风险；短会话、存储便宜或证据不可约时，完整 transcript 仍更透明。`arXiv:2608.14528v1` 在 exogeneity 等假设下给出 deterministic sufficient handover 的理论刻画及 Gaussian/nonparametric regression 上下界，不证明开放 Agent 能自动知道未来问题、可靠抽取最小状态或忠实保留决策。

<!-- source-family:SF-2026-ARXIV-2608-14528 -->

关键状态应使用 typed workflow fields 或原始 artifact reference，不只存在自然语言摘要。必要时保留摘要到原文的 links，允许按需回读。

“保留重要内容”仍然过于模糊，因为不同 query type 依赖不同 evidence shape。通用 gist 可能很好地保存人物、事件和关系，却系统性删掉 date、duration、ordering 与 valid-time；aggregate accuracy 又可能被 multi-hop 或 factual gains 掩盖这一 slice failure。因而 compression policy 应声明可测试的 preservation contract：

```text
task / future-query distribution
+ protected evidence types
+ source time range and temporal anchors
+ exception / negation / identifier fields
+ compression and evaluator versions
→ compressed view + source links + per-slice loss evidence
```

保护 temporal anchors 不是要求所有摘要永久复制每个时间表达式。时间不参与决策、原文可低成本回读时，普通 gist 仍更省；只有 temporal query、expiry、ordering 或 event-time repair 属于 correctness contract 时，timestamp 才应成为 typed protected field。反过来，一句更明确的 compression prompt 能修复某个 benchmark slice，也不证明它迁移到其他 summarizer、语言或长期 Memory pipeline。系统仍需按 information type 做 preservation test，并保留 raw-evidence fallback。

同一 Context 中的知识也不是同质对象。Safety rule、authorization、schema 与 exception 可能要求 exact retention；
episodic log 可以有损摘要；大型 topic 可能需要分区；低频 evidence 可以移到外部存储。统一 compactor 对所有行
使用同一压缩率，在短 session 与低风险对话中便宜合理，但递归执行后会让少量必须逐字保真的 control state 与
大量可压缩历史一起衰减。更稳健的演进是先给知识分型，再把 retention operator 与类型绑定：

```text
typed knowledge registry
→ compact: 在类型允许的损失函数内就地改写
→ decompose: 主题过大时分区，并复制每个分区必须携带的规则
→ retrieve: 原文外置，查询时先 pin in-scope control state，再按相关性取 evidence
→ raw source / registry remains authoritative
```

这里的分类器只提出类型和 scope，不能拥有规则真值或授权。Registry 应保存原文 digest、knowledge type、
applicability、expiry、source、compactor / retriever version 与恢复引用；任何安全关键规则被降级、跨分区遗漏或
retrieval 未命中，都应作为 correctness failure，而不是普通 relevance loss。类型化策略提高 rule retention，却
引入 misclassification、规则复制膨胀、stale scope、重复冲突和额外存储。事实类型无法可靠判断、原文很短或
审计要求完整 replay 时，保留未压缩 Context 仍更合适。

分型之后，还需要决定有损视图在什么时候生成。每次预算告急才调用模型压缩，实现直接，却把压缩延迟、生成随机性与本轮选择耦合在一起。一个替代分支在 ingestion 或原文更新时，预生成完整、压缩、结构化和引用等多分辨率视图，全部绑定同一原文 ID、revision、scope 与最低 fidelity；组装 Context 时只选择已经存在的视图。选择器先装入所有必须保留对象的最低合格表示，再用剩余预算按增量 utility/token 升级。若最低集合本身放不下，应暴露预算压力、缩小任务或回读外部状态，不能为了让选择成功而悄悄降低安全规则的保真要求。<!-- source-family:SF-2026-ARXIV-2604-10352 -->

这把昂贵的视图生成移出压力时刻，但增加预计算、存储与更新失效成本；原文或 scope 改变后，旧视图不能继续冒充当前版本。贪心 utility 是选择代理，不证明最佳任务质量，schema 合格也不证明内容真实。受限 replay 与单 session 实验支持这一机制的可实现性，没有证明相对同样无故障的 LRU 更优的任务质量、跨 session 保真或生产 SLO。短会话、原文频繁变化或难以定义最低 fidelity 时，按需压缩与完整原文回退仍更简单；可变原文和派生视图的提交权限由下文的 registry/commit 边界负责。

一项 2026 年研究在多个公开语料与作者构造的 Agent 配置上观察到递归统一压缩会快速损失 safety rule，并以
type-specific compact / decompose / retrieve 改善 retention。该证据说明“不同 correctness contract 需要不同
retention policy”，不证明论文报告的具体 recall 能跨模型、语言与企业 policy 复现；因此正文吸收机制，不把
其数字当作生产 SLO。

### 原文是事实状态，摘要只是可替换的派生视图

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04050:start -->
只保留滚动摘要，在短会话和低风险辅助任务里最省存储；但摘要一旦覆盖原文，后续问题改变时已经无法恢复被压掉的证据。更稳健的 Context runtime 将每条 message、tool result 与文件引用先写入不可变 history，把层级 summary DAG 视为带 source pointer 的 materialized view：active Context 只装近期原文和摘要，需要审计或命中不确定时再沿稳定 ID 回读原始状态。Compaction engine 拥有阈值、版本与原子替换，模型只能请求检索或分解任务，不能宣称摘要等于原文。

这条路径以额外持久化、索引、summary lineage、回读 I/O 和重新 prefill 换取可恢复性；“所有原文可取回”也不证明模型一定会找对证据。短任务、原文可以完整驻留或存储受限时，直接 transcript 仍更简单。`arXiv:2605.04050v1` 的 §2–§3 只支持作者的 immutable store、summary DAG、三级压缩回退和 operator-level recursion；§4 的 OOLONG/Opus 4.6/Claude Code 对比不证明任意 Agent、任务或生产 SLO 更优，§5 还承认污染与基准边界。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-04050:end -->

### Compaction 从 Blocking Rewrite 演进为带 Commit 的后台状态转换

同步 compaction 在历史较短、压缩频率低时最容易保证一致性：暂停主循环，对当前 Context 生成摘要，替换成功后再继续。长时 Agent 会让这段 stall 直接进入任务 critical path；若改成后台并行，又不能让 compactor 在旧 snapshot 上完成后无条件覆盖期间新增的 observation、tool result 或 policy。需要把 compaction 拆成 `snapshot watermark → background proposal → fidelity check → compare-and-commit`：Context registry 拥有 canonical state 与 replace authority，compactor 只产生带 base revision 的派生候选，workflow 在提交前处理新增 tail 或拒绝 stale proposal。

并行化能隐藏一部分压缩延迟，却增加双份 Context、取消/重做、版本冲突和 fidelity evaluator 成本；错误 commit 会丢 observation，过于保守则持续浪费后台计算。短会话、高风险逐字记录、剩余 token 很少或无法可靠合并 tail 时，应回退同步压缩、外置原文引用或不压缩。`arXiv:2605.23296v1` 的 §3 与 §5 支持作者 parallel compaction runtime 及 HotpotQA/LoCoMo 等受测合同，§6 不证明任意 Agent、压缩器、并发修改或生产 tail-SLO 都能安全隐藏 stall。

<!-- source-family:SF-2026-ARXIV-2605-23296 -->

后台 commit 解决了状态原子性，却没有证明长期行为身份未漂移。普通问答正确率可能在 compaction 后保持，而 persona、role boundary 或 repository instruction 在多轮 coding session 中逐渐衰减。deployment evaluation 因而应从同一 snapshot fork 压缩/未压缩或不同 compactor 分支，用 versioned probes 和真实任务 continuation 分开测 role fidelity 与 task utility；evaluator 只产生 drift evidence，Context owner 才决定发布、回滚或回读原文。

Snapshot-then-probe 提高可重复性，却会引入 probe leakage、persona scorer 偏差、fork 环境不一致和额外运行成本；通过固定 probes 也不证明开放任务中无漂移。短任务、无 persona contract 或完整 transcript 可低成本保留时，直接 replay 仍更透明。`arXiv:2605.24279v1` 的 §3 至 §5 支持作者 ContextEcho harness 与长 Agent coding-session 评估，§6 不证明其 probes 覆盖所有角色约束、模型或生产 workflow。

<!-- source-family:SF-2026-ARXIV-2605-24279 -->

即使不压缩历史，只更换继续生成的模型，也会改变 Context 的行为条件。交接后的 suffix 读取的是另一模型写出的 prefix，单模型平均分不能代表有方向的 A→B 兼容性。[受限的 switch-matrix 证据](https://arxiv.org/html/2603.03111v1#S2)在同一 episode 上比较 A→B 与 B→B 的最后一轮，分别观察问答 grounding 与累积约束；有些交接变差，有些反而改善。设计验收因而应保存每轮 authoring model、模板和目标版本，并用相同历史 replay 候选 suffix；它衡量的是 continuation 是否符合任务合同，不是让旧 assistant 文字获得事实或授权真值，也不证明日志或 handoff summary 已能修复差异。<!-- source-family:SF-2026-ARXIV-2603-03111 -->

长任务还有更窄的反例：模型从自己的起点抵抗目标漂移，并不保证接手一段已漂移的弱模型轨迹后能恢复。[Inherited Goal Drift 的有限模拟](https://arxiv.org/html/2603.03258v1#S4)还显示，直接 instruction-hierarchy 测试不能可靠替代这种 continuation 评价；另一模拟环境更易恢复，说明失效与环境、前缀和目标表达共同相关。应用可以把当前目标、已完成的中间目标及真实环境状态分开保留，再从目标快照测试继承轨迹后的实际行动；这是设计验收要求，不是论文实现的自动 repair。其 binary-goal 模拟、少量 seeds 与一个特选漂移前缀，不证明所有多 Agent 交接都会失效，也不把行为偏离等同于 permission 改变；若无法确认当前目标和行动约束，应回读原始任务与可验证状态，而非只凭更强模型或更硬 prompt 继续。<!-- source-family:SF-2026-ARXIV-2603-03258 -->

Compression 之外还有一种“保留全文、只改变注意入口”的分支：Actor 在实例级选择 spans 并插入轻量 boundary
tags，Solver 仍读取完整 source。它以额外 selector pass 和 tagged-view identity 换取较低的 irreversible deletion：

```text
authoritative full context
→ query-conditioned emphasis mask
→ tagged full-context view
→ frozen Solver
→ outcome evidence and mask calibration
```

Emphasis mask 是 derived view，不拥有事实、删除或授权；source、mask/Actor、tag format、Solver 和 cache identity
必须共同版本化。HiLight 的作者实验支持这一分支在四项 benchmark 与指定 Actor/Solver 下优于 pruning/no-highlight，
不证明选中的 spans 是因果 evidence，也未验证 multi-turn cache reuse 或 production SLO。短 Context、强 deterministic
retrieval 或必须避免 prompt-position bias 时，无 selector 的完整输入仍更可靠；真正受 token hard limit 约束时，
可回读的 compression 仍不可替代。

### 从 Generic Compression 到 Goal-conditioned Structured Pruning

通用 token pruning 可以减少输入，却可能截断代码语法；按文件或 chunk 的 coarse retrieval 保留结构，
又可能丢失分散在局部行中的 dependency。Coding Agent 已知当前 goal 时，可以让 tool wrapper 把 goal 作为
focus hint，对每一完整代码行计算 task-conditioned relevance，并按 confidence 动态选择阈值：

```text
raw tool output
→ generic token / chunk compression
→ goal-conditioned line selection
→ preserve source location and full-line structure
→ raw-artifact fallback on uncertainty or audit
```

Hint 是高频、会随 plan 改变的 derived state，必须绑定 workflow step、repository revision、tool invocation
和 pruner version。错误 goal、跨 turn stale hint、false negative 或跨行 dependency 会静默删掉关键证据；
额外小模型也引入 latency、供应链和 calibration。没有 hint 时应 bypass，高不确定、debugging、security review
或需要完整 provenance 时保留 raw output。作者在特定 coding harness 和 benchmark 上的 token/latency 结果
只证明受限 feasibility，不保证跨语言、对抗代码或所有 Agent success 不回退。

长文档还可以按 page/section structure 做 learned selection，再与 lexical/semantic retrieval 组合；它比纯
token pruning 更能保留表格、标题与页面边界，但 selection 错误会整块删除证据。可逆实现应保存 source
location、选择分数和 raw-artifact fallback，并把 document revision、selector 与 task goal 绑定。短文档、
高风险审计或 multi-hop recall 尚未校准时，保留完整 Context 或 deterministic extraction 仍更可靠。

## Context Identity 与 Cache

### Context Map 是轻量导航状态，不是事实副本

把全部历史塞回 prompt 在短会话中最忠实；长任务中可维护一个小型 orientation map，只保存主题、位置、freshness 与 provenance pointer，再按需读取原文。它降低 assembly cost，却新增 map 漂移、错误指针和遗漏风险，因此 map 不能拥有事实 authority，命中后仍须回源；任务短或证据不可寻址时，直接 context 仍合理。<!-- source-family:SF-2026-ARXIV-2605-19932 --> exact-v1 §3–4 支持其 orientation cache，§5 不证明该摘要在开放长期任务中无损。

当 tool result 可按 path/hash 重新寻址时，完整保留所有消息并不是唯一的 correctness baseline。一个受限分支是在透明 Messages-API proxy 中先驱逐或压缩匿名、短寿命的输出，把完整 conversation 留在 client backing store，并在可寻址内容的位置插入 retrieval handle；后续重复读取触发 fault，再按 path/hash 取回并 pin 住该内容。Context manager 因而拥有 visible message working set、handle 与 pin state，backing store 仍拥有原始事实；这不是把 KV tensor 从 HBM page 到 host/storage。它以 fault tail、错误驱逐和 hash/path 失效风险换取 token 空间，短会话、高风险审计或工具输出不可稳定寻址时仍应完整携带。`arXiv:2603.09023v1` 的 §3 支持该 L1/L2 机制，§5 只评测 message eviction 与 fault-driven pinning；L3 只完成实现而未做规模评测，L4 仅是接口，因此不能把分层设计外推为已验证的通用 Context storage。<!-- source-family:SF-2026-ARXIV-2603-09023 -->

Context 参与模型行为身份。至少需要记录：

- segment digest/source/version；
- assembly policy version；
- model/tokenizer/chat template；
- tool schema versions；
- retrieval/memory query；
- authorization snapshot；
- compression method。

Prefix cache 可以复用相同 token prefix，但 user/tenant-specific 内容、policy version 和 adapter 都必须进入 cache identity。错误复用不仅改变回答，还可能泄漏跨租户状态。

Token reduction 与 prefix reuse 甚至可能互相冲突：任意删除、摘要或 tool-schema 抖动都可能改变后续 token
layout，让一个更短的 Context 从 cache read 退化为完整 Prefill。长 Agent session 因而需要联合管理内容效用、
canonical prefix 与 segment lifecycle，而不是只最小化 token 数：

```text
raw instruction / observation
→ deterministic stabilization and ingestion-time reduction
→ canonical visible history + hash-addressed raw artifact
→ active / completed / evictable segment state
→ batch-gated structural eviction
→ recovery tool on uncertainty or audit
```

Estimator 只能提出 completion evidence 与 residual-utility delta，registry 负责验证 state transition，artifact
store 保留 authoritative bytes，backend cache 只拥有物理 prefix blocks。延迟驱逐保住 cache identity，却扩大
短期 working set；即时驱逐节省 token，却可能触发 re-exploration 或 miss。短 session、无 prefix-cache backend、
future relevance 不可预测或 strict full-fidelity workload 中，full Context 与保守截断仍合理。TokenPilot 的作者
实验只支持其 provider-cache、benchmark ordering 与价格合同，不证明自托管 GPU 的 TTFT/goodput 收益。

驱逐 proposal 还可从主回答的生成轨迹中隔离：在相同上下文另起辅助生成分支，输出待删除的 tool-result cursor，主线程只在工具轮次边界消费已经完成的建议，不把管理 reasoning 再塞回用户回答。[SideQuest 的必要接口](https://arxiv.org/html/2602.22603v1#S3)用成功轨迹的未来最后引用训练这条分支；不再显式引用却不证明内容失效，最终 citation 还可能令暂时无用的结果重新有用。因而 proposal、主轨迹与 raw-artifact 的责任不能合并；版本/过期结果检查及原文恢复是我们的采用条件，不宣称源已实现完整协议。辅助 forward、临时 KV、训练与恢复仍付费，单 H100/SGLang 改变 concurrency 后的峰值吞吐不授同负载质量/SLO 支配。未来效用难预测、成功条件训练不适用或恢复预算不足时，继续完整历史、保守驱逐或关闭分支；并行不等免费删除。<!-- source-family:SF-2026-ARXIV-2602-22603 -->

## Context 中的信任冲突

System message、retrieved web content 与 tool result 最终都变成 token，但控制面必须保留来源差异：

| 来源 | 可作为信息 | 可直接授权动作 |
| --- | --- | --- |
| Platform policy | 是 | 仍由执行器强制 |
| User request | 是 | 受用户权限限制 |
| Retrieved content | 是 | 否 |
| Tool result | 是 | 否 |
| Model-generated memory | 需验证 | 否 |

模型可以建议如何解释内容，不能改变其 authorization class。

## Observability 与 Evaluation

Context evaluation 应分解：

- selection recall：所需信息是否入选；
- precision：无关/冲突内容比例；
- placement/use：模型是否使用正确 evidence；
- faithfulness：结论是否由 evidence 支持；
- cost/latency：assembly、Prefill 和 storage read；
- privacy：是否越权读取或记录敏感内容。

只评最终答案会无法区分 retrieval miss、bad ranking、compression loss 与 model misuse。

### Repository Retrieval 必须把 Gold Recall、可用 Span 与 No-Gold Abstention 分开

在代码仓库中，命中将被修改的文件不等于提供了足以完成修改的 Context。调用关系可能把必要证据放在 ripple
files 中；反过来，有些任务本就不需要额外仓库证据，强行检索只会增加干扰。因而 retrieval contract 至少要
分离：候选文件召回、token budget 内的有效 span、下游 edit/test outcome，以及 no-gold 场景中的选择性拒绝：

```text
task + repository revision
→ candidate files and ripple relations
→ ranked spans under token budget
→ sufficiency / abstention decision
→ edit and test evidence
```

这比单一 file-recall 分数更能定位失败，却增加 gold lineage、dependency 标注和 counterfactual evaluation 成本；
文件级 credit 也不能证明模型实际读到了正确 span。小仓库或完整 working set 可低成本常驻时，直接装载仍合理；
检索候选池不含 required API、仓库 revision 不匹配或 sufficiency 不确定时，应补检、扩大范围或拒绝行动，不能让
ranking confidence 冒充事实充分性。

<!-- source-family:SF-2026-ARXIV-2607-24882; daily-trace:papers/2026/07/29/README.md -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14885:start -->
大语料 Agent 不应让 full-corpus shell 与 retriever二选一；retriever负责把候选拉入可持久 workspace，Agent只在局部 workspace做可组合 DCI，并让 context reset 保留 workspace state。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14885:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-22906:start -->
大型代码库的 Context 恢复不应把零散命中直接塞进 Prompt；系统先重建与任务相关的跨文件 path，再对 path 做压缩、加载和有效期管理。持久 workspace 保存恢复结果，Context 只投影当前需要的部分；path 置信不足时回退更宽检索或局部代码探索。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-22906:end -->

### Scratchpad 可读不等于被后续计算忠实使用

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29522:start -->
保存 scratchpad 文本可以回放模型写过什么，却不能单凭可读性判断哪些 register 实际驱动了后续输出。因果干预结果应作为 request-local diagnostic state 保存，把可见内容与被检验的计算依赖分开；probe 只拥有观测/路由权，不能据此删除未被识别的约束。

这种诊断需要额外干预与校准，结论也受任务和模型限制：现有证据只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上支持特定 written state 被因果读取，并未证明 scratchpad 的其他 token、自然语言推理或真实 Agent memory 都忠实。干预不稳定或超出这些条件时，应保留原始 scratchpad 与外部 verifier，而不是让 probe 取代事实验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-29522:end -->

### 可编辑 Trace 仍是派生控制输入

<!-- semantic-body-binding:SF-2026-ARXIV-2604-13706:start -->
可见推理 trace 还可以作为可编辑的 control artifact，而不只是诊断记录。反馈可转为删除、修改或指导片段，抑制原 verdict/end-of-thinking 后从修改的 prefix 继续生成；它不同于追加整段旧对话再要求重答。编辑者只改变派生控制输入，原始来源与原 trace 继续保存，不能据此宣称已编辑模型真实内部思维或修复了事实；新的输出仍须独立验收。

这条执行分支引入 editor/replay 调用、反馈误译和检索不充分的风险。Co-FactChecker exact-v1 的自动反馈可见 gold/rubric，真人评测只有2专家、3研究者及14 claims/3轮，不能采用普适严格改进理论。反馈不可信或需要完整审计时，append-only、原文回读与外部 verifier 继续合理，旧 verdict 消失不是正确性证据。这里编辑的是下一步生成条件，不是上一节诊断 probe 所观测的内部因果状态。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-13706:end -->

### Context 不只选择内容，也选择何时承诺

内部推理状态可以继续修订，公开输出却会立即改变用户、工具和后续 Agent 的行动，因此“想到了什么”和“何时说出来”是两个不同的控制问题。简单做法是每一步都暴露，适合低风险协作，却会把未经验证的中间状态变成不可逆承诺；一种训练侧分支是在构造监督轨迹时，用 entailment checker 过滤与私有推理不一致的公开 disclosure，再学习何时披露。现有证据只支持这种离线数据构造与策略学习，不证明部署时存在逐次执行的 entailment gate。生产系统若要在 private state 与 public commitment 之间增加运行时检查，那是由风险与可逆性推导出的工程选择，仍需独立实现和评价；高风险场景应由确定性规则拥有最终发布权。

<!-- source-family:SF-2026-ARXIV-2605-03314 -->

同理，更多相关 Context 并不保证更好。外部知识在任务早期可能扩大探索，在约束已经收敛后却可能引入锚定、冲突和搜索分叉；Context admission 因而应评估边际决策价值、干扰风险与撤销成本，而不是按相似度无限追加。无法可靠估计 crossover point 时，旧的最小上下文、分阶段加载与可恢复引用仍是更稳健的默认。[受限证据：arXiv:2605.04361v1]

<!-- source-family:SF-2026-ARXIV-2605-04361 -->

### Policy 不是普通 Context，而是必须完整携带的执行约束

context assembly 可以为了预算裁剪历史、检索结果和示例，但 active policy set 不能被当作可选相关文本。系统应在 assembly 前验证 policy version、provenance、适用 scope 与完整性，并把结果作为 request identity 的一部分；预算不足以携带必要 policy 时应 fail closed，而不是静默截断。

由于 prompt 内规则仍可能被冲突内容覆盖，policy carriage 不能独自承担安全性。tool 与 action boundary 必须再次执行同一版本的确定性约束，并记录拒绝或降级原因。对没有外部 effect 的低风险生成，prompt-only policy 仍可作为轻量分支；一旦涉及数据、权限或物理动作，独立 enforcement 才是 canonical owner。

<!-- source-family:SF-POLICY-CARRIAGE-INTEGRITY -->

### 长上下文从被动堆积演进为 Active Information Foraging

把全部候选材料塞入 context 在容量充足时简单有效，但长任务中会同时增加噪声、成本和错误承诺。Agent 应维护显式 epistemic state：已知、未知、冲突与当前决策所需证据，再主动选择下一次读取或检索。这样 context acquisition 变成有预算的控制循环，而不是无界累积。

收益是把 token 花在决策缺口上；代价是 state estimator 可能错误地认为“已经知道”。每轮 acquisition 仍需记录遗漏风险和停止原因，低风险短文档则保留一次性加载。无法校准未知状态时，扩大检索或转人工比自信停止更安全。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07042:start -->
Context gathering 不应只把搜索历史压成摘要。Agent 要持有 predicate-based belief state，显式记录已满足条件、未解问题、证据来源和下一观察；programmatic exhaustion gate 只能根据重复查询、无新 predicate closure 与预算判断“继续搜索的边际价值耗尽”，不能把它升级为答案正确。这个状态减少重复搜索和 Context 膨胀，却依赖 extractor/schema 完整性；开放域或高风险中应扩大检索、保留 hard cap，并将 unresolved predicates 交给 verifier 或人工。`arXiv:2605.07042v1` 只支持作者框架和所测任务中的受限机制，exhaustion 不构成开放世界完备性证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07042:end -->

<!-- source-family:SF-SCOUT-ACTIVE-INFORMATION-FORAGING-FOR-LONG-TEXT-UNDERSTANDING-WITH-DECOU -->

## Context Compression 必须保留执行状态，而不只是语义

摘要与原文语义相似，仍可能丢失“下一步从哪里继续”、尚未满足的 session constraint 或时间有效期。压缩验收应在相同 environment state 下重放后续动作，检查 blocked/repeated action、constraint violation 与恢复位置；文本相似度只能作为辅助信号。

有界执行视图还要区分任务阶段：某动作在当前阶段已尝试，不代表环境改变后永远不可重试。[PABU 的一个分支](https://arxiv.org/html/2602.09138v1)保留 goal 与最新 observation，用 learned progress 更新阶段，并仅在同一阶段积累 attempted actions；阶段推进时重置该集合，同时学习保留哪些旧 observation。它把“防重复”改为 stage-conditioned 状态维护，而不是无条件删除旧动作或堆积全部历史；available actions 从观察解析，不由此认证真实环境可执行。<!-- source-family:SF-2026-ARXIV-2602-09138 -->

progress 文本仍是 learned observation，不是可信 authority、Bayesian belief 或严格 Markov state；误判阶段、漏保留前提与未见失败都可能导致错误重试或丢失恢复线索。受测 context masking 同时改变训练与评价，不能归因于单独上线删历史；输入 token 减少时输出 token 反而增加，也不授所有任务成本更低。阶段识别或保留策略失配时，回读原始观察、恢复更完整历史，并以真实环境反馈复核 frontier；“不重复”不应凌驾于必要重试及后续状态验收。<!-- source-family:SF-2026-ARXIV-2602-09138 -->

长期有效的约束还应从自由文本摘要中分离成 versioned state，记录 scope、expiry、来源与当前执行 frontier。side channel 增加 schema 和迁移成本，但避免多轮 compaction 把强约束降成背景事实。低风险问答仍可使用普通摘要，外部 effect 越大，越需要 paired-state regression。

压缩时机同样不是固定 token 阈值就能决定：如果任务还在搜证或等待工具结果，删除早期观察可能使下一步无法修正；当环境状态、未决约束与后续行动已达到可检查的 READY 条件，才允许提交一个更短的执行视图。触发器只提出压缩时机，Context owner 必须检验 pinned constraints、raw handles 和恢复路径；误报比延迟压缩更危险。StateComp 的作者受控任务显示 token 节省与平均回报接近的受限权衡，但若原始历史不可回读、跨模型/任务状态识别漂移，固定阈值、保留更多近期记录或暂不压缩仍更稳妥。<!-- source-family:SF-2026-ARXIV-2609-27298 -->

即使删除时机合适，也不能把每段历史的“可删性”独立相加：两段分别可删的记录可能互为唯一备份，同时删除就会丢掉约束。更稳妥的对象是**实际提交的删除集合与保留下来的内容**。一个受限实现先在已完成轨迹上联合删除 protocol-valid 的 tool exchange/assistant blocks，以同一已记录下一步输出的 teacher-forced likelihood 差作离线风险标签；线上只用当前可见状态预测候选集合风险，保护近邻与固定约束，并在没有低风险集合时 abstain。它把单项排序改为集合级提交，但 learned risk 不是安全保证：teacher-forced 下一步与真实继续执行不同，误判、额外特征计算及不可恢复的原文删除仍需 raw fallback 和任务级回归。短会话或完整历史可负担时，保留原文仍是简单基线。<!-- source-family:SF-2026-ARXIV-2609-27276 -->

<!-- source-family: arxiv:2608.06503v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: context-compression-paired-state-regression -->

### 持久 Instruction 更新应先修改 Typed State，再重建文本 View

直接编辑长 prompt 最接近人类写作，却容易在局部修改时破坏相邻约束、引用或优先级。更稳健的分支把持久 instruction 表示为 typed dependency graph：模型只提出 scoped patch，validator 检查目标节点、依赖与不变量，commit 后再生成带版本的文本 checkpoint。图是 authority state，文本是派生 view；无法无损解析的自由文本仍保留人工编辑路径。

### Compaction 不能把 Partial Observation 提升为已确认事实

进程被 kill、tool 超时或输出截断时，已有文本可能非常像成功结果。Compactor 若只做语义摘要，会把 partial observation 持久化成完成事实并在后续轮次放大。Context item 必须携带 process exit、observation status、source/effect receipt 与 evidence level；只有满足 commit contract 的结果才能进入 confirmed state，其他内容保留为 pending/failed observation。

Typed state 与 status metadata 提高一致性，却增加 schema 演进、validator 和重建成本。短、无持久约束的会话仍可直接拼接；关键 workflow 则宁可保留 unknown，也不能让流畅摘要改变证据等级。

<!-- source-family:SF-2026-ARXIV-2607-09175 -->
<!-- source-family:SF-2026-ARXIV-2607-13071 -->

### Context Mutation 是 Agent Proposal，State Owner 负责校验与提交

让 Agent 自主选择、压缩、恢复 Context，可以适应任务阶段并控制 token；但 context 是执行状态，模型不应直接覆盖它。每次 mutation 应声明保留目标、删除范围、source handles、预算和预期收益，由 state owner 检查 pinned constraints、provenance、tool/workflow revision 与可恢复性后原子提交。

动态管理用更多 control calls 和 metadata 换适应性，也可能因错误摘要或自我强化删除关键证据。简单短任务仍适合固定窗口；验证失败、收益不明或原文不可恢复时，应拒绝 mutation 或回退最近 checkpoint。

<!-- source-family:SF-2026-ARXIV-2607-23809 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-33672:start -->
用户撤回错误主张或追加“重新回答”只改变当前指令，若带压力的历史仍送进模型，就没有恢复到clean证据状态。恢复验收应固定question与任务约束，分别比较保history的retraction/reset、去压力内容的summary/reconstruction和无压力clean分支，测撤回后错误主张的残余影响，而不是只看最后答案或有没有reset事件。Effective context是行为条件，不能假设一个已被清零的内部记忆变量。

配对clean与history分支、保有用约束的重建增加调用与provenance成本，误删可能丢失合法任务状态。[Reset Is Not Recovery v1 §3–8/10](https://arxiv.org/html/2609.33672v1)只在有限多选题/option likelihood和templated history支持这一反例，不能分离用户压力与模型自己的旧回答坚持；aggregate恢复阈值也非逐item成功率。删除全文和gold证据是诊断上界，不是已解决的selective repair；开放生成、真实memory和retrieval需另验。低风险短会话可保简单reset，未证恢复时保留Unknown、隔离无支持主张或回可验证原始证据，不宣称更强instruction已清除污染。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-33672:end -->

### Context Optimization 可以主动取证，但不能自行改变事实权威

在同一任务族反复执行、来源单元相对稳定时，还有一条离线分支：把 source documents 和 trajectory-derived insights 作为带 provenance 的可组合单元，在开发任务上用真实 rollout fitness 选择组合、删改或重组，再冻结为可复用的 Context 版本，而不是每次 query 都重新搜索。这里优化的是单元组合，refiner 只能提出一致性修订，不能认证 insight 为真；[受限组合搜索](https://arxiv.org/html/2602.16113v1)中，不加筛选地装入全部 skills 反而退步，跨模型迁移也不等于 model-agnostic 最优。开发样本、搜索/选择历史与最终上下文必须分开记录，并用未参与选择的任务核验；开发集与测试集的去重不充分时，不能把高 fitness 当泛化。离线 population rollout、标注/反馈与 refiner 调用都是成本；固定前缀可能便于缓存，但原实验没有认证端到端缓存收益，RAG 也可以保留稳定前缀。来源变动、分布漂移或预算不足时，回退普通检索、固定组装或人工材料，不由 Context 搜索替代参数训练或事实 owner。<!-- source-family:SF-2026-ARXIV-2602-16113 -->

把 Context 当作可优化状态，最初可以只在已有材料中改写、筛选和重排；当任务需要新近或小众知识时，这条封闭路径的上限由输入材料决定。更强的分支允许 optimizer 主动调用搜索与浏览工具，把“缺什么信息”转成受预算约束的 acquisition plan，再由 Context owner 验证来源、去重并提交新版本。模型生成的是候选 Context，不是事实本身，也不能借优化目标绕过 provenance 与授权。

主动取证能补齐静态 prompt 无法包含的知识，却引入错误查询、来源污染、工具成本和对开发集的过拟合；直接给顺序优化器增加工具在受限实验中甚至可能变差。低资源、来源稳定或无法可靠验收搜索结果时，应保留被动 Context、人工材料或固定 RAG。现有证据只支持 exact-v1 的任务、工具和模型设置，不证明跨模型迁移等于事实正确，也不证明参数更新可以被 Context 更新普遍替代。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13050 -->

## 本章在知识树中的位置

Prompt 定义软接口，Context 定义本次调用的完整 working state。下一章展开 Context 的主要动态来源之一：RAG 如何从外部 corpus 检索 evidence，并为生成保留 provenance。

沿 State 横线，第 59 章的 Registry 管理可交付 artifact identity，本章把已授权的模型、Prompt、evidence、tool schema 与 workflow snapshot 组装为单次调用可见状态；第 77 章再负责跨调用持久化。Context 是高频 derived state，Memory 是受治理的 persisted state，二者不能因都包含文本而合并。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22528 -->
把 context compaction 识别为治理控制面：安全约束、授权与 provenance 在压缩后必须由 constraint pinning/typed state 继续存在，不能依赖普通 summary 自然保留。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；攻击/防护受具体 compactor 与提示结构限制；pinning 不保证约束本身正确，也不替代 effect-time reference monitor。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Context 从 token 拼接演进为带类型和生命周期的运行时 state：task contract、working evidence、tool output、safety rule 与历史草稿有不同 retention 和 correctness 要求。统一截断或摘要在内容同质时合理；长任务中则需要 type-aware compression、pinned rules、externalized state 与显式 invalidation。

更细的 Context policy降低 token 成本，却引入分类错误、compaction cliff、stale summary 和 provenance 丢失。压缩结果必须能够回到原始 evidence，规则冲突或置信度不足时回退完整 Context、检索或人工确认；Context 是当前运行状态，不等于跨任务持久 Memory。

## 自检问题

1. Context 与 Memory 的核心区别是什么？
2. `T_total <= T_max` 为什么不代表信息被有效使用？
3. 长窗口为什么没有消除检索和压缩？
4. Context assembly 为什么要先 authorization 再 ranking？
5. Summary 为什么需要链接原始 evidence？
6. 哪些字段必须进入 context/cache identity？

### Intent-conditioned Compression 会引入不可逆删除边界

面向代码或工具任务的上下文压缩，可以按当前意图优先保留 identifier、path、edit 与局部证据，而不必对所有历史使用统一摘要。它节省 token，却把 intent classifier 变成删除权限的 owner；当任务意图漂移时，被丢弃证据可能无法恢复。系统应保留 raw evidence 的回退路径、projection 版本和触发重建的条件，而不是把压缩结果当作新的唯一事实。
<!-- source-family: arxiv:2608.24188v1; semantic-body-binding: intent-conditioned-context-projection -->

### Context Compression 的身份必须包含监督语言与分词边界

压缩器在一种语言、segmenter 或 tokenizer 上达到目标预算，并不保证换到另一种组合仍保留相同事实。压缩 artifact 应绑定 supervision language、切分方式、tokenizer、实际达到的预算和 raw fallback；评价同时看信息损失与 token 节省。否则名义相同的压缩比会对应完全不同的语义删除行为。
<!-- source-family: arxiv:2608.26175v1; semantic-body-binding: multilingual-context-compression-identity -->

### 多个 Context Constraint 会发生联合可靠性坍塌

单个约束各自有较高保留率，并不保证长流程能同时保持全部约束；多次压缩、合并和交接会使联合成功率近似乘法下降。Context 管理因此要保存约束集合、逐项状态和 supersession，并在每次变换后重验，而不是只测平均语义相似度。持续维护增加 token 与检查成本，但能阻止少量局部遗漏累积成执行层违规。
<!-- source-family: arxiv:2608.12426v1; semantic-body-binding: joint-context-constraint-reliability -->

## 小结

Context 是受约束的运行时 working set，不是无限知识仓库。好的 assembly 在相关性、权威性、位置、成本和隐私之间做可追溯取舍。下一章进入 RAG 的检索链。

### Budgeted Trace State 需要保留可恢复引用

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22879:start -->
只保留最近消息或一份自由文本摘要，在短会话中简单有效；长轨迹中，graph、append-only history、reference registry 与 summary+suffix compaction 应共同定义 context identity。压缩器只产生候选视图，原始引用和已提交动作仍由 lossless trace archive 保存。

这种结构能在 token budget 内恢复较长执行链，却增加引用失效、图状态漂移和压缩器误删关键约束的风险。exact-v1 只支持作者的数据结构与评测，不证明任意 Agent 都能无损压缩；引用解析失败、关键 invariant 丢失或重放不一致时，应回退原始 trace archive。arXiv:2605.22879v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22879:end -->

### Recursive Intent Memory 只提交有界意图状态

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23668:start -->
完整重放所有对话能保留细节，却让成本随历史增长；一个受限分支把每轮状态压成有界 intent memory，并把“预测下一意图”和“压缩既有意图”作为不同训练责任。Intent state 只拥有下一步 proposal，不能静默改写原始事实、权限或用户明确约束。

更小状态改善长程交互成本，却可能丢失细节、错误主动化或把暂时偏好固化。作者实验只支持披露任务和训练流程；意图不确定、压缩回归或主动行为风险升高时，应回退 full/recent context，并采用静默或显式确认策略。arXiv:2605.23668v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23668:end -->

### Context Compression 要保留未来更新所需的区别

只以“压缩后仍能回答当前问题”作为目标，在一次性问答中合理；长期 Agent 还会收到新 observation、纠错和目标变化，当前不重要的区别可能成为下一步更新的必要条件。压缩器因此要同时提交 current-answer sufficiency 与 future-update preservation：保留可恢复引用、未决分支和会改变后续 belief/action 的 distinctions，而不是把所有当下未使用的信息合并。<!-- source-family:SF-2026-ARXIV-2609-20045 -->

保留未来可用性会降低压缩率，也无法穷举未知问题。作者结果只支持其任务和 future-query construction；高风险或未来需求不可建模时，应保留原始 archive、可逆摘要和按需回读，压缩视图不能取得事实 owner。

### Context Selection 应从 Claim/Action Obligation 反推最小证据包络

按相似度追加更多 token，可能仍漏掉决定能否行动的关键前提。更严格的路径先定义 claim 或 action obligation，再沿 derivation graph 选择覆盖其 closure 的最小 sufficient evidence envelope；包络不充分时状态保持 unresolved，不能用 context 更长冒充 assurance。<!-- source-family:SF-2026-ARXIV-2609-16302 -->

该方法降低 context/cost，却引入 obligation discovery、schema/type 与 solver complexity。图不完整、obligation 不可信或行动风险高时，应回退更宽 evidence set、deterministic checks 或人工审阅；少量 preserved artifacts 与 synthetic 数据不证明自动发现义务。

## Review notes

- `SF-2026-ARXIV-2603-03111`：[exact-v1](https://arxiv.org/html/2603.03111v1) §2–4/Appendix A；采用有方向 handoff 与 suffix no-switch 的 paired continuation 判断。9×9 模型、两 benchmark 各200 episodes，CoQA第10轮F1、Multi-IF第3轮整会话strict success（含prefix早轮表现），temperature0、2048 output tokens、可支持处 low reasoning/verbosity；paired BCa 1000 bootstrap。70%/74%为两因子 off-diagonal LOO解释率，不证明任意路由/多次或更早切换，handoff instruction等mitigation仅提出未验证。作者必要正文完成；root 已实际对读必要原文、新增段落与邻接，非作者 POST 通过，未复现实验。
- `SF-2026-ARXIV-2603-03258`：[exact-v1](https://arxiv.org/html/2603.03258v1) §3–5.2/Figures2–6、Appendix C；采用自起点稳健不等于继承轨迹稳健、hierarchy proxy 非充分与环境依赖边界。stock10 seeds/ER5 seeds，conditioning来自一个特定已漂移GPT-4o-mini轨迹，state-based drift可恢复；OpenRouter与Anthropic API默认temperature1，API模型身份和较强prompt在Appendix C。binary-goal环境、特选前缀、少量seeds及未验证的修复策略不能推生产保证；目标快照/真实行动验收是本章设计要求，不是论文实现。作者必要正文完成；root 已实际对读必要原文、新增段落与邻接，非作者 POST 通过，未复现实验。

- `SF-2026-ARXIV-2604-10352`：[ClawVM v1](https://arxiv.org/html/2604.10352v1)，Daily 2026-04-14；§3、§5.2–5.3、§7。采用预生成多分辨率与 hard-minimum fit 的责任分离，不采用任务质量优于 LRU、schema 等于事实真或跨 session 无故障保证；写前必要 source→owner 与实际正文/相邻衔接写后独立核验通过（apr01），未复现实验。

- `SF-2026-ARXIV-2604-13706`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.13706v1) §3.2、§6.3/7；trace-edit/continuation、oracle feedback 和有限真人评测边界保留。apr01 已独立核必要源→实际 owner，正文已写，root非作者实际正文与相邻衔接写后复核通过；未复现实验。
- `SF-2026-ARXIV-2604-14029`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.14029v1) §3.6/§4/Tables2–4；旧文本逐项渲染、近期文本与 consumer 适配，all-image 反例保留。apr01 已独立核必要源→实际 owner，正文已写，root非作者实际正文与相邻衔接写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-13066`（Status: Experimental）：[exact-v1 HTML](https://arxiv.org/html/2604.13066v1) §3.1–3.6 为子串/meta-token/dictionary 表示与含字典的节省条件；§4.2/§5.2–5.3、Tables1–2 区分模板解压 exact match 与算法压缩后的字符相似度，未评价目标 analytics；§7 的能力下界表述不作为保证采用。正文只吸收 codec reconstruction 与编码态目标任务的合同分离；2026-09-27 apr02 已实际重开必要官方v1、正文及相邻交接，非作者写后通过，未复现实验。

- `SF-2026-ARXIV-2604-07487`（Experimental）：[exact-v1](https://arxiv.org/html/2604.07487v1) §4.1–4.3、§5 与 PDF Appendix A。同题六条轨迹用于 contrastive reflection；Qwen3-32B generator 经 SFT/GRPO，执行器冻结。AppWorld TestN 三次运行的 TGC/SGC、平均与 oracle pass@3 分开；没有 RL-only 完整因子对照，额外采集和在线 generator 成本未完全匹配。正文只采用参数更新 owner 与构造接口分离，不证明训练免成本、跨执行器无损或任意任务优于 RAG。

- `SF-2026-ARXIV-2604-01664`（Status: Experimental）：[exact-v1 HTML](https://arxiv.org/html/2604.01664v1) §3.1–3.3 给出 observation 正文载入前的长度/headroom 状态、Null/Partial/Full 聚合及预算课程；§4.5 的 ablation 只支持作者组合问答/搜索与披露预算下的改进；Appendix A.1 承认稀疏延迟奖励和粗粒度 segment 的局限。这里吸收 admission/control 顺序，不把 GRPO 或作者性能数字写成通用部署结论。

- `SF-2026-ARXIV-2606-22528` — primary `arXiv:2606.22528v1`；Method=`arXiv:2606.22528v1 §3 Compaction-Eviction Attack; §4 Constraint Pinning`；Evaluation=`arXiv:2606.22528v1 §5 Results and Robustness`；Non-proof=`arXiv:2606.22528v1 §6 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Harness-1（policy-owned semantics / harness-owned recoverable state；Status: Experimental）:
  https://arxiv.org/abs/2606.02373

本章复用第 22、43、45、54 章的长上下文与容量约束，不重复 position/attention/KV 机制；第 76 章拥有 external retrieval，第 77 章拥有 persisted memory lifecycle。

Primary-source 入口：

- Lost in the Middle: https://arxiv.org/abs/2307.03172
- GPT-3 / in-context learning: https://arxiv.org/abs/2005.14165
- CodeNib（Status: Experimental）: https://arxiv.org/abs/2607.25431
- SWE-Pruner（goal-conditioned structured context pruning；作者实验边界）:
  https://arxiv.org/abs/2601.16746
- StateLM / The Pensieve Paradigm（model-managed visible context；Status: Experimental）:
  https://arxiv.org/abs/2602.12108
- CIRCLE（self-conditioned Context refinement；Status: Experimental）:
  https://arxiv.org/abs/2602.23229
- Long Context chapter dependency: Chapter 22 in this repository
- BEAVER（structure-aware document selection；Status: Experimental）: https://arxiv.org/abs/2603.19635
- TokenPilot（canonical prefix 与 segment-lifecycle joint objective；Status: Experimental）:
  https://arxiv.org/abs/2606.17016
- The Sleeping Agent（gist compression 的 temporal-anchor failure；Status: Experimental）:
  https://arxiv.org/abs/2608.11775

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22906` — primary `arXiv:2606.22906v1`; Method=`arXiv:2606.22906v1 — §III-B Repository Representation and Overall Framework; §III-E Metadata-First Context Construction; §IV-C Evaluation Protocol`; Evaluation=`arXiv:2606.22906v1 — §Benchmarks and evaluation scenarios.; §IV-C Evaluation Protocol; §IV-F Ablation Study: Where Do the Gains Come From?`; non-proof=`arXiv:2606.22906v1 — §Practical scope of comparison.; §IV-J Discussion of Error Modes and Scope; §V Threats to Validity`; fallback=该 family 的 failure pressure 是：Existing methods often retrieve only local fragments and fail to recover the broader task-relevant context needed for complex repository-level tasks. 披露的 evaluation signal 是：Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22953` — primary `arXiv:2606.22953v1`; Method=`arXiv:2606.22953v1 — §3 Method`; Evaluation=`arXiv:2606.22953v1 — §5.3 Lag Analysis: Early Warning; §A.2 Probe Validity Controls and Leakage Analysis; §A.8 Intervention Sweeps and Head-Level Analysis`; non-proof=`arXiv:2606.22953v1 — §9 Discussion and Limitations`; fallback=该 family 的 failure pressure 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 披露的 evaluation signal 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29522`；Method `https://arxiv.org/html/2606.29522v1 — §6 Mechanism and alignment interpretation; scratchpad intervention`；Evaluation `https://arxiv.org/html/2606.29522v1 — §5 Results`；未证明边界 `https://arxiv.org/html/2606.29522v1 — §Conclusion and intervention-identifiability scope`。

<!-- june29-owner:AGENT-CONTEXT:start -->
### 2026-06-29 来源范围补记

`SF-2026-ARXIV-2606-29522`：既有干预证据范围为 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 的特定 written registers；不覆盖显式 scratchpad 的全部 token、自然语言推理或真实 Agent memory 的忠实性。原文 §5、§6 与 Conclusion 定位见上方 source-specific Review note。

<!-- june29-owner:AGENT-CONTEXT:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-14885:start -->
- `SF-2026-ARXIV-2606-14885` — Daily `2026-06-13`；primary `arXiv:2606.14885v1`；Books review `books-review:SF-2026-ARXIV-2606-14885`。

  **已吸收的语义增量：** 大语料 Agent 不应让 full-corpus shell 与 retriever二选一；retriever负责把候选拉入可持久 workspace，Agent只在局部 workspace做可组合 DCI，并让 context reset 保留 workspace state。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14885:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20047:start -->
- `SF-2026-ARXIV-2606-20047` — Daily `2026-06-19`；primary `arXiv:2606.20047v1`；Books review `books-review:SF-2026-ARXIV-2606-20047`。

  **已吸收的语义增量：** `PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents` 路由到 `AGENT-CONTEXT`：PACMS 把 context assembly 表述为预算约束 submodular selection：独立 engine 根据 relevance、coverage 与 redundancy 选取片段，agent 消费带 provenance 的 context；不足时回落到更大窗口或检索重试。代价是 utility surrogate 可能遗漏依赖和顺序。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20047:end -->

<!-- daily-books-trace:SF-2026-COMPACTION-CLIFF:start -->
- `SF-2026-COMPACTION-CLIFF` — Daily `2026-08-25`；primary `arXiv:2608.22752v1`；Books review `books-review:SF-2026-COMPACTION-CLIFF`。

  **已吸收的语义增量：** 新增 typed compact/decompose/retrieve 演进及其 raw-source、rule pinning 与 failure boundary。
<!-- daily-books-trace:SF-2026-COMPACTION-CLIFF:end -->

- `SF-2026-ARXIV-2512-24601` — Daily `2026-01-02`；[Recursive Language Models exact-v1](https://arxiv.org/html/2512.24601v1) §2.1–2.2、§3 Table1/Observations2/4/5与§5。本窗重要新证据事件，2+2+3=7仅针对新增model/task×external-access/subcall反证，REPL/递归机制已有2025作者dated公开稿，不重计首次贡献。采用Qwen去subcall两任务更好而信息密集另两任务有收益的分账；不授10M可靠性、统一硬件总成本或同child预算。未运行实现；root必要原源/当前owner写前通过，root实际正文与邻接写后通过，日级Gate尚待。

- `SF-2026-ARXIV-2602-03226` — Daily `2026-02-05`；[ATACompressor exact-v1](https://arxiv.org/html/2602.03226v1) §3.3–3.5/AAC Eq4–5、§5.2短输入反侧。6分具体gap深入只采用query相关长度probe→ratio/max软slot容量与consumer兼容分账；length≠sufficient evidence，标注/encoder/probe/质量成本及短输入退化保留。两7B、A10040G/有限input切片不授任意longcontext/production SLO，未复现。root已实际核必要源/owner及257行正文、compression/break-even邻接与末注，POST通过；日级Gate待验。

- `SF-2026-ARXIV-2601-07994` — Daily `2026-01-15`；[DYCP exact-v1](https://arxiv.org/html/2601.07994v1) §4/Algorithm1、§6.1与Discussion。2+1+2=5，query-time contiguous span分支差额深入；append-before-test不授所有span过阈，embedding/index成本及漏检/full-history退路保留，不授超长能力。未运行代码或复现实验；root实际必要原源/现owner写前核通过，实际正文与前后邻接非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-10112` — Daily `2026-01-17`；[SPADE exact-v1](https://arxiv.org/html/2601.10112v1) IV-B–F、V必要QA/预算、VII-E及VIII。6分build/test-derived typed view gap深入；静态配置/evidence/UNKNOWN与source语义分责，CMake自动/其它手工、7synthetic/1real、部分重跑及Cursor个体退步保留，预图成本不当QA收益。未核实现或复现；root必要原源/owner写前通过，root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2602-09138` — Daily `2026-02-12`；[PABU exact-v1](https://arxiv.org/html/2602.09138v1) §3.1–3.3、4.1–4.5/Table2、5与必要B环境/训练配置。2+2+2=6，执行 state 缺口深入；只采用 stage-progress conditioned attempted-actions reset 与 learned-observation retention，不授progress可信authority/Markov/Bayes/完全防重复，训练评价联合改变与output成本增加限制邻近。root 必要 source→owner 写前通过，实际两段/完整邻接/本末注非作者 POST 通过，窄锁释放；未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16113` — Daily `2026-02-20`；[ECS exact-v1](https://arxiv.org/html/2602.16113v1) §3、§5.3–5.4 与有限任务/成本配置。2+2+2=6，离线 source-unit 组合 fitness→冻结 context 版本接口差额深入；refiner 非事实 owner，skills 反退、heldout/模型迁移权限与离线费用近正文。不采用全球最优、SFT 替代或实测 prefix-cache 加速。root 必要源/实际 owner PRE 通过；root非作者实际正文/完整邻接/自身末注 POST通过，窄锁释放；未运行 artifact 或复现。

- `SF-2026-ARXIV-2602-22603` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22603v1) §3–4必要接口，2+2+3=7；aux management trace隔离与主tool边界消费差额，成功人口/未来引用、并发与全费用及原文恢复回退近文。fresh非旧作者独核prepared原证与actual owner，root授该窄ownership；作者实际正文/完整邻接顺读，root非作者实际正文、完整邻接及自身末注POST通过，窄锁释放。未核代码/复现，非日级Gate。
