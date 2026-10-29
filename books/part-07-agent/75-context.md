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

对测试生成，缺失的工作集未必只是同名符号的定义，还可能是“如何构造出可以调用目标方法的对象”。一条受限Java分支先沿静态call graph取得有限深度的调用路径，再收集目标方法、依赖方法与参数类型；遇到可访问的public constructor，就把其参数依赖继续展开到fixed point，去重后交给模型。它把调用顺序与对象构造建议变成输入，而不从代码检索得分推断可执行性；静态边、public可见性和构造闭包仍可能漏掉反射、运行时分派或环境依赖。<!-- source-family:SF-2026-ARXIV-2604-22046 -->

这份closure是prompt候选，不是合法路径或测试正确性的证明。[CAT的受限Java对照](https://arxiv.org/html/2604.22046v1)还依赖生成、编译执行和修复回路，去掉callchain与dependency的联合消融不能隔离每个组件；与整class或按复杂度分配次数的基线也不能只看一次总coverage就归因。路径可随深度膨胀，解析、依赖闭包、构建与全部重试都计费，coverage提升不等发现真实bug；工作集已常驻、静态解析不可靠或预算难以摊销时，保留普通源码/手工fixture、较浅路径与现有测试工具，用真实执行结果继续检查，而不让闭包自签action前置已满足。

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

固定输入预算时，逐项相关性排序还会反复选中同一类证据，却漏掉需要联合读取的部分。另一分支将memory记录、历史turn与tool结果放入共同候选池，以token估算作成本，用query相关性加权的集合覆盖目标选择工作集，再交给原Agent消费；独立selector拥有本次选取，不拥有改写原事实、撤销工具权限或永久删历史的权力。[受限facility-location对照](https://arxiv.org/html/2606.20047v1#S3)中，相近的证据recall仍可对应不同QA质量，较紧预算又可输给普通topK，因此embedding覆盖与去冗余不是答案可提取性或未来充分性的保证。候选粒度、embedding、query、token估算与预算须共同保存，顺序依赖和桥接证据仍需原文回读；不把有限候选上的代理优化称为全任务最优。编码、覆盖计算、选择及独立consumer评价都付费；预算、估算或任务支持不合时，保留简单topK/MMR、较完整历史和有界回读，不由短context或较高代理覆盖批准语义无损与净提速。
<!-- source-family:SF-2026-ARXIV-2606-20047 -->

把内容选入Context后，放置还可以按有关联的块组，而不总是独立给每块排一个位置。一个受限做法先固定关键指令及其输出格式邻居，整体移动该组并改变组内先后，再与单块移动及中性邻居替换比较，以区分绝对位置和局部内容组合。[RAMPART的合成指令probe](https://arxiv.org/html/2606.04628v1#S3)中，关键块跟在两format块之后可改善部分位置，替换邻居后残余信号仍在；它不证明统一attention机制或所有任务的固定最优位置。这个分支增加分块、诊断调用、编排和回归成本，literal出现也不是实际任务完成；任务、模型或邻接内容改变时，应重验或保留简单固定排序/完整指令。未进入这次view的schema不等于executor撤权，授权仍由工具执行边界检查。<!-- source-family:SF-2026-ARXIV-2606-04628 -->

当检索内容用于改写下一份prompt，而非直接回答事实时，exemplar还可以按质量层次或不同评价轴组合，不必只取一个总分最高项。一条[受限对照构造分支](https://arxiv.org/html/2509.02093v1)从近邻中分别保留高/中/低层，或取各metric最佳，再让模型对照生成新提示；同一项可能赢多个轴，中层也不因被命名为anchor就保证防过拟合。标签若来自prompt-response pair，就不能静默变成prompt固有质量，更不能把complexity或verbosity均值当事实/安全真值。应保存query、原配对、各轴标签、retrieval/selection与最终prompt，再在明确的下游consumer上独立验收；较大k仍可能退步，同源judge和混样本数的消融不证明纯reasoning因果。标注、检索、全部refine/生成/judge和回归均付费；评价对象、标签或净收益不可靠时，保留原prompt、简单top-k/可信exemplar与独立任务测试，不让更高refinement分数取得事实或执行权限。

<!-- source-family:SF-2025-ARXIV-2509-02093 -->

排序和去重之前，共享对话还要保留“谁说了什么”。同一条全局 transcript 不能原样当作每个 Agent 的 user/assistant 历史：某位伙伴的 assistant turn 对另一位 Agent 并不是自产生回答。可先用绝对 speaker identity 保存原 content 与顺序，再为当前消费者确定性映射 SELF/PARTNER 等相对角色。角色视图不改写 canonical history，也不把所有伙伴的内容合并为同一种事实或权限；原身份仍用于追溯与冲突处理。<!-- source-family:SF-2026-ARXIV-2604-09212 -->

这增加消费者身份、view revision 和重放规则，而不是又生成一份不可回查的摘要。[SPASM的受限双Agent对照](https://arxiv.org/html/2604.09212v1)支持该输入接口分支，但 English instruction-tuned、固定温度与最多二十条 utterances 的结果不证明开放协作中的人格保持或零 echo。Embedding probe不是偏好真值，DeepSeek的motivation维度未显著改善；echo人审人口的正文/表注口径亦未统一，不能把局部人工一致率扩到全部记录。角色/来源不能可靠恢复、多人接口未校准或消费者行为退步时，保留原typed transcript与显式speaker标签，不让相对role获得授权。Multi-Agent委派与实际执行仍由第82章承担。

当历史中相邻 turns 共同表达证据时，孤立 top-K turn 还可能切断弱相关但保持连续性的上下文。一个替代分支预存 turn embeddings，到 query 到来时将 relevance 转为归一化 gain，选择若干 contiguous spans，再按原时间次序拼接；它不同于写时固定分段或持久 summary。[DyCP 的限定 span 对照](https://arxiv.org/html/2601.07994v1)支持这种 query-time working-set 选择，不授 turn 相邻即有真实依赖，也不改写原记录的 authority。展示算法先 append 再更新停止量，不能据其文字宣称每个已选 span 都过阈；零方差、耗尽与容量边界仍需实现核验。

无需额外 LLM 分段调用不等于免费：embedding、索引、span 检索与拼接仍占预算，多留低相关 turns 也会增加输入与等待。有限对照中 GPT-4.1 的 full history 已接近此分支，检索遗漏仍会丢掉完整历史可回答的证据；judge 分数及低相关 turn 移除实验不证明全局依赖因果或超长能力。短历史、已常驻工作集或检索不可靠时，保留完整 history、简单 top-K 与原文回读，按实际遗漏/成本选择，不由标称窗口更长或 pruning 更短推断普遍收益。<!-- source-family:SF-2026-ARXIV-2601-07994 -->

跨段证据还可以按多种读取顺序构造候选工作状态，而不是只选一份固定拼接：先从各chunk提问题相关证据与暂定答案，据此选择要回读的原段，再沿不同次序逐步更新状态；相同有序前缀复用已生成状态，被判无用的扩展则剪去该路径后续。[受限多视角读取分支](https://arxiv.org/html/2509.06436v1)缓存的是派生语义状态，不是decoder KV，也不证明不同次序已覆盖全部事实；cache须绑定query、原段/顺序、模型与prompt版本，不能以片段集合相同复用不同历史。摘要漏掉的线索会影响后续回读选择，当前无用的段也可能在之后出现桥接证据，故局部utility只拥有搜索proposal，不授无损剪枝。较长路径与跨worker多数都不认证真值，重排阅读也不改原文时序或来源；共享前缀和同模型状态还使候选相关。原实验仍有任务反退，更低None率只是更常作答，非幻觉减少。初次全段读取、全部路径/状态生成、utility、缓存驻留、最终聚合与独立原文核验均计费，局部省调用不等比顺读便宜。证据选择、顺序敏感或预算不可靠时，保原段引用、更宽回读、固定顺序/直接长窗和Unknown，不让被选摘要自行批准事实或完整理解。

<!-- source-family:SF-2025-ARXIV-2509-06436 -->

Assembly 不一定只有检索或手写规则：也可以训练一个独立的 Context generator，为当前任务生成执行提示，同时冻结真正执行工具的 Agent。训练时先对同一任务取得成功与失败轨迹，用对比 reflection 形成监督样本，再以冻结执行器的结果奖励更新 generator；部署时生成的新提示进入本次 Context。这与检索历史 Memory 不同：经验主要改变 generator 参数，executor 的参数不随该训练更新，生成提示也不因此成为事实或授权。<!-- source-family:SF-2026-ARXIV-2604-07487 -->

这种分责让 Context 构造本身可以优化，却增加离线多轨迹采集、reflection、训练和每次调用的生成成本，并可能学到执行器或环境专属捷径。作者在 AppWorld 等任务中报告了受限收益，但没有包含 RL-only 的完整因子对照，也没有把额外轨迹与运行成本全部匹配，不能据此证明每一阶段必需或普遍比检索更省。任务或工具接口变化后，需要重新验证 generator—executor 配对；训练数据不足、需要严格来源可追溯性或执行器频繁更换时，固定 assembly、原文检索与已有 Memory 仍是合理路径。

连续编辑的 Context generator 还须看见部署时的中间状态，而不只学会从 seed 写出一次提示。一条受限分支从多轮编辑树抽取已修改的 instruction 与带正确答案、执行成绩的反馈，训练一次 edit；直接把编辑前已知的“不修改”成绩作奖励参照，而不再交给学习的 value 或组内归一化吸收。这个 action-independent baseline 不改变期望优化目标，也不保证方差必减；单次训练更不等于多轮累积收益最优。部署另保存各 context 及成绩并允许回访旧分支，避免必须沿最新错误 edit 继续，但搜索和提交仍由 Context owner 控制。[有限 SQL/选择题对照](https://arxiv.org/html/2603.18620v1)把固定 holdout 反复用于分支选择并报告最佳轮次，不能当未参与选择的最终泛化；editor 变强也不证明冻结的执行器胜过更强执行模型。初始轨迹、gold反馈、编辑器训练、每轮候选与多次执行评价均计费，冻结参数不消除指令污染或遗忘约束。反馈不可得、任务/执行器变更或净预算不足时，保留固定 assembly、已核 generator 与原文检索，并在未参与选择的任务上验收，不由自改提示批准事实或权限。<!-- source-family:SF-2026-ARXIV-2603-18620 -->

外部 generator 还可以在每次 tool observation 后维护运行中的 message view，而不只生成起始提示：按稳定 message IDs 提议保留、合并、改写或删除，冻结的 executor 再消费下一视图。[AdaCoM 的有限对照](https://arxiv.org/html/2605.30785v1)支持训练这种 manager，却也显示未经训练的编辑会退步，跨 executor 迁移受保真需求和摘要样式影响；同类任务的原始成绩接近，并不保证能消费相同 working memory。工程上仍须由 runtime 保护原始历史、约束和可回读引用，不允许 role 字段提升来源权限。每步 manager、训练与额外评价均付费，改写早期 prefix 还损失 KV reuse；较短输入或少量成功率改善不认证整轨迹更省。消费者、任务或预算改变时，重验 manager—executor 配对，保留 none、较完整原文和固定 assembly，而不把更激进压缩当普遍更可靠。<!-- source-family:SF-2026-ARXIV-2605-30785 -->

外部manager之外，executor也可在同一输出中写专用operator/address tokens，运行时解析后修改下一次renderedcontext；这仍需要状态owner，不是“native”就能绕过执行检查。[受限context-editing分支](https://arxiv.org/html/2610.25550v1#S3)保稳定block地址、locked系统块和不可编辑actionhistory，改写/移除只影响可见view；编辑旧prefix仍需重prefill。训练先以全trace提出释放资格，再让teacher在此前编辑已生效的当前view上写下一edit，避免原history里仍在、部署view里已不存在的target；后见资格不等线上知道未来，literal检查也不排所有语义误删。实际audit仍有defect，tool形式对照保留stubs/receipt、native会剥edit，且普通compaction未匹配额外FT，不能把全部收益唯一归token语法。Teacher/fullFT、runtime、所有重prefill和回归均计费，trimmedtoken均值与离线估计可overlap时间不等全任务实测净时延；原harness副本仍可触compaction。地址、来源保真或预算不稳时，保留原记录/none、固定compaction或已验manager，不让较短view取得原证删除权。<!-- source-family:SF-2026-ARXIV-2610-25550 -->

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

对数据表，schema 与查询历史在命名稳定、表语义简单时足以导航，却不一定保留生成数据的过滤条件、粒度和更新逻辑。另一条派生视图分支从生产代码抽取这些语义，将它们与表使用信息、人工说明一起离线归一化，再让请求检索相关定义；无定义或视图陈旧时，回到已授权的实时数据与元数据查询。代码说明回答的是“如何构造”，live observation 回答的是“当前是什么”，用户纠错则可以提出需确认保存的持久 Memory；三者不能在一次摘要中获得同等事实与写入权威。<!-- source-family:SF-2026-OPENAI-INHOUSE-DATA-AGENT -->

预计算把重复语义探索移出请求路径，也增加代码抽取、离线刷新、存储与stale-view风险；静态代码理解不证明生产执行和数据 freshness。[内部数据Agent的公开工程说明](https://openai.com/index/inside-our-in-house-data-agent/)支持这条工作流实例，却未以受控消融证明各层的独立收益或通用正确性。生产逻辑难以恢复、权限不足或新数据与旧定义冲突时，应回读原代码、补实时检查或转人工；小语料与低复用任务仍可直接查询，不让自动丰富的Context代替原数据证据、索引发布或Memory提交。

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

还要分开“本次生成推理”和“把旧推理留在下次Context”：在历史已足够精确重建state的[受限文件任务](https://arxiv.org/html/2610.25760v1#S3)中，移除旧thought但仍生成当前thought，守lock规则可近似保留，而某模型的最终任务成功仍受旧thought保留影响。此比较没有匹配当前计算量；保留还会改变后续写多少reasoning，不能简化成旧推理无价值。固定history时，等长filler、另一history的流畅reasoning与准确state table都不复现自产reasoning的全部行动效果；交换counterfactual reasoning又可让action跟随错误结论，说明可见状态和执行消费需分别验收，而非自产thought获得事实权。高probe读出或state问答不证明action使用同一路径，oracletable也会改变prompt与尝试分母。生成、保留、状态重建及独立执行检查都计费；trace与原观察冲突、保留预算不足或规则违反无法核实时，保留原history/可信state replay和执行前确定性gate，不以可读state或一份连贯计划替代真实约束。<!-- source-family:SF-2026-ARXIV-2610-25760 -->

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

多图推理还可以把全局计划与局部像素读取分开：manager 保存原问题、跨图计划、worker 的最终结论及 crop handle，每次 worker 只读一张指定图与所选技能，私有历史不回灌全局。这样避免所有图片、技能和试探过程反复挤进同一窗口；但最终一句结论是有损摘要，crop 和原图必须能回读，manager 没看过的像素不能因收到流畅结论就变成独立事实。<!-- source-family:SF-2026-ARXIV-2605-04304 -->

这将部分 context 压力换成任务分解、路由、裁剪和额外调用；局部窗口的峰值不是整条轨迹的总 tokens、费用或延迟。受限图表对照在更长多步任务上受益，简单单图任务不一定优于直接读图；错误裁剪会丢全局约束，技能库和摘要也可能遗漏。任务短、全局关系难以拆分或费用不合算时，保留完整图/直接 VLM；局部结论冲突则回读原图和相关 crop，而不是让层级结构自己认证正确。

程序性视觉参考还可以先在临时 branch 中解释，而不把全部截图直接追加给主 Agent：将 skill 拆成带文字状态卡的多个视图，先根据 live observation、近期历史与状态卡选择必要参考图，再在局部窗口对齐当前状态，输出是否适用、子目标、建议计划、禁做事项与验证提示。主路径消费这份结构化 guidance，再决定本次动作；参考图不是当前界面的坐标真值，branch 也只是上下文分工，不自动构成权限或安全隔离。[MMSkills 的有限对照](https://arxiv.org/html/2605.13527v1)支持把“参考表达—当前对齐—主路径决策”分开，直接注入完整参考可能过度锚定，咨询本身也会误解状态、遗漏 coverage 或生成错误步骤。多视图、咨询调用、图像编码、技能构建与完整轨迹都计费，主路径少几步不等端到端更省；覆盖不足、grounding 或预算失配时，回读当前画面、保留纯文本 skill/直接 VLM 与独立结果核验，不让历史成功示例或流畅计划取得本次执行权。<!-- source-family:SF-2026-ARXIV-2605-13527 -->

临时工作还可以沿同一agent的prefix分叉，而不另开一份完整角色历史：branch共享进入前的上下文，在局部展开工具与推理，return时只把摘要接回主路径，并将私有KV回滚到分叉边界。[受限上下文折叠分支](https://arxiv.org/html/2510.11967v1#S3)将长期可见状态与局部计算分开，不等于并行多agent、任意嵌套或已撤销外部动作。分叉revision、原轨迹/工具结果、返回摘要及KV位置须共同保存；摘要可能丢依赖，scope judge只检查给定prompt与return也不认证全部trace正确。训练完整trajectory与压缩奖励仍支付私有生成，峰值窗口与理论累计预算不是已省总tokens；工具调用还可明显增加，训练只计main rollout的时间不代全流程。跨分支事实冲突、摘要不足或费用失配时，回读私有原记录、扩大返回支持或保完整单路径，不由KV回滚、较短主窗口和更长可生成轨迹批准执行撤销、事实保持与净加速。

<!-- source-family:SF-2025-ARXIV-2510-11967 -->

检索到语义相近的示例，还不等于它能直接装入当前工作集：示例中的对象、关系和步骤可能属于另一份结构。可先按语义召回，再分别构造来源示例与当前输入的关系图，以映射和结构重写提出适配后的示例，最后装配给回答模型。[这一受限上下文分支](https://arxiv.org/html/2510.04560v1#S3)把“找什么”与“怎样适配到此刻”分开，但图来自模型/工具提案，结构相似不认证事实、步骤可执行或语义保持；找对示例、甚至能反思仍可能答错。原示例、两份图、映射和改写版本应连同可见输入保存，不能让重写文本取得当前观测真值；union式添加与重embedding也不是完整delete、一致性或状态事务。固定语义检索下的结构消融可以给局部支持，检索消融若同时关闭重写则不能独占检索的因果；按被测模型选困难题和同源支持人口亦不等线上分布。全部支持样本制备、索引/embedding、图抽取/对齐、重写、最终推理与独立答案核验均计费；局部额外tokens和秒数不是全链SLO。对应关系、事实或净预算不稳时，保可信原示例、较窄直接上下文与真实输入回读，不由匹配到示例或更复杂图批准通用推理、记忆正确和执行安全。

<!-- source-family:SF-2025-ARXIV-2510-04560 -->

面对长视频，可见集还可以按原始时间范围组织，而不预先把整段证据压成 captions：每次读取声明子问题、起止区间、采样率和帧预算，先稀疏扫描定位候选，再对同一区间加密重看，或把多个区间按各自密度拼到一次观察中。返回的描述与实体表仍是派生状态，应保留时间 anchors、所见帧与原视频恢复入口；重新观察提供另一份读取，不自动消除 Observer 或记忆更新的错误。<!-- source-family:SF-2026-ARXIV-2603-24558 -->

这个接口把预算从全视频预处理移到按需多轮取证，同时增加视频解码、Observer、Reasoner、实体维护与重读费用。[受限长视频对照](https://arxiv.org/html/2603.24558v1)中，较弱的计划器可能损伤强 Observer，单次大上下文更快，预建索引则可能用更高前置成本换更高精度或多 query 复用；峰值 context 和总 tokens 不能互代完整时延。时间对齐、实体引用或收益不可靠时，应回读原帧、限制轮次并保留均匀采样/静态 captions 或人工核验，不把重复的派生描述当独立事实确认。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-14029:start -->
派生视觉接口不只用于原生图像，也能承载旧文本 observation：逐项渲染较老的工具结果，actions 与近期 observation 仍保留文本，而不是将全部历史改成像素。它改变 consumer 的输入接口，不改变证据身份；搜索服务已生成的摘要，渲染后仍是摘要，不会恢复成原网站事实。原文本、引用与恢复入口仍须保留，stale/fresh 分界与表示选择共同决定当前可见视图。

POINTS-Seeker exact-v1 需要训练 consumer 适应混合表示，并支付渲染、图像编码与原文恢复成本；有限对照中全部转图像反而较差，token 减少不能直接外推为端到端时延或证据无损。长轨迹与模型、任务变化须重测；短轨迹、逐字协议或适配不足时，直接携带文本仍合理。这是与 active slots 并行的表示分支，不是删除原始 artifact 的授权。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-14029:end -->

视图改成像素后，重复生成它也可能成为开销。可按 episode 缓存 normalized segment 的渲染图块，每轮依原历史次序拼接，再由 compression tool 决定下一视图的像素密度；cache key 还须绑定 renderer/style 身份，不能仅因文字相同复用不兼容图块。这只省去重复渲染：整段拼接、resize、图像编码和 decoder KV 仍分别产生费用，原文与可恢复引用也仍需保留。策略改变的是 consumer 的下一次可见视图，不是删除源记录的权限。

任务成功后才给压缩奖励，也不能保证策略不会过度压缩。AgentOCR 的受限对照中，更频繁注入该奖励可大幅降低成功率，某些任务的文本基线仍更强；论文正文与伪码对注入间隔的计数口径不同，不宜照抄为通用执行规则。Render 时间和视觉 token 节省不能替代完整轨迹费用，episode 图块缓存仍会增长，字体与布局变化也未充分检验。重复片段少、逐字证据重要或质量回归时，固定保守密度、近期文本和完整文本路径仍是合理退路。<!-- source-family:SF-2026-ARXIV-2601-04786 -->

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

示例工作集也可以沿请求流扩展，而不更新学生权重：先以学生输出entropy决定是否检索已有demo，仍不确定时异步请求教师标注，将通过筛选的示例写入pool供后续请求使用；当前回答与未来pool更新因此是两个不同事件。[ICD的受限多模态对照](https://arxiv.org/html/2510.18117v1)用多次教师一致和跨模态匹配筛选，但一致/相似与低entropy均不是真实正确率，不能把稍后得到的教师答案说成本次回答已被纠正。应保存示例来源、教师/encoder版本、可见请求次序、写入资格与失效条件；pool会继承错标和漂移，检索、demo prefill、教师多次调用及驻留均计费。无参数更新不等零蒸馏成本，碳排proxy也不是完整服务实测；示例失配或预算不足时，隔离派生pool、保可信固定demo与原学生/显式教师路径，独立验收当前答案。

<!-- source-family:SF-2025-ARXIV-2510-18117 -->

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

有限工作集还可以直接规定重启时带走什么，而不先训练摘要器：每生成一个chunk就清空旧KV，重新编码原问题、固定开头与最近一段推理，再继续生成。这样限制的是下一次调用的可见条件与缓存，而不是只在旧cache上滑动一个attention窗口；对固定原问题、首段和chunk预算，可见工作集有上界，但完整轨迹仍应在外部保存以供审核和必要回读。

[受限Markovian Thinker对照](https://arxiv.org/html/2510.06557v1)支持训练消费者适应这种重启，不证明保留片段是未来任务的Markov充分状态，原问题变长也会增加边界。过短chunk会损质量，重编码/训练反传并不总更快，外推长链成本亦不等实际墙钟测量；清空KV、重复prefill、全部rollout与独立长程回归均计费。旧证据丢失、跨块依赖或净预算不合时，扩大近期工作集、回读原文，或保留完整上下文/经验证摘要，不由固定窗口与长输出授予无限可靠推理。<!-- source-family:SF-2025-ARXIV-2510-06557 -->

压缩规则本身也可以由失败对照迭代，而不永久依赖一份通用摘要prompt。固定执行agent，在训练任务上分别取得完整上下文成功和压缩后失败的轨迹，让LLM比较其信息差额、汇总反馈并更新compression guideline，再用压缩成功任务提出更短规则；还可把teacher成功压缩样本蒸馏为较小compressor。[ACON的受限分支](https://arxiv.org/html/2510.00615v1#S3)把history与最新observation分开触发，但轨迹差异只是提出规则的线索，不证明某条遗漏已被因果定位；contrastive子集择优和success-only蒸馏也不保证未来任务充分，更不使摘要成为事实副本。

规则搜索、双轨迹工具执行、teacher/student训练、每次压缩与后续生成必须一起计费，不能把peak input tokens下降当成总显存或时延同比下降。原模拟任务中更激进的压短步骤仍可损准确率，计入cached-input折扣后history重写常不省钱，而observation压缩的取舍不同；小compressor也可能延续teacher遗漏。规则、阈值或部署消费者失配时，保留原文可回读引用、完整关键状态与不压缩分支，独立验收任务结果和全部费用，不由textual feedback或局部保留率批准长期无损运行。<!-- source-family:SF-2025-ARXIV-2510-00615 -->

压缩监督还可从短QA种子扩成较长训练上下文：回到原文来源，同时扩展已知支持文档与干扰文档，再用目标答案的likelihood变化迭代裁去支持文档首尾的低贡献句，把留下的片段作为摘要target。[BRIEF-Pro的受限对照](https://arxiv.org/html/2510.13799v1)据此训练较小compressor供冻结reader消费，新增的是监督人口和读出分工，不是让摘要自证充分。只扩oracle文档会制造过干净输入，但共同扩展也同时改变长度，不能独占真实噪声鲁棒性的因果；训练时已知支持文档和gold答案的特权更不能带入普通请求。句数指令只近似控制输出长度，word压缩率也不是token、墙钟或总费用；部分reader/任务仍弱于完整上下文。来源扩展、teacher似然试删、compressor训练与全部压缩/reader调用共同计费；跨句证据、来源或新query支持失配时，保留原文引用、较宽上下文与不压缩分支，不由平均压缩率批准开放任务无损。

<!-- source-family:SF-2025-ARXIV-2510-13799 -->

若业务已给出“哪些原句重要”的标签，抽取压缩还可把留存率要求变成文档级校准对象：固定句子评分器，先为每份校准文档求出仍保留指定比例重要句的最大删选阈值，再用这些阈值的低分位决定新文档统一的保留门。[有限conformal抽取分支](https://arxiv.org/html/2509.20461v1#S3)在校准与新文档标签对可交换等条件下，约束的是“新摘录的重要句召回至少达标”的边际概率，不是每份摘录无遗漏、标签已涵盖全部现实关键信息或句子本身正确；目标召回低于一时本就允许漏标注句。评分、分句、重要性偏好和人口变化须重新核验，离散分数ties及端点约定也不能由连续秩推导省略。原句抽取之后再交生成模型改写，不继承这份coverage；还须独立验收最终信息支持与任务效用。全部标注、逐句含原文评分、校准/重校准、可选改写与验证都有成本，句子移除率不等token或总费节省。标签、交换性或下游支持不足时，保原文/更宽摘录、回读引用与领域人工核验，不让统计门替代事实和行动权限。

<!-- source-family:SF-2025-ARXIV-2509-20461 -->

词法minification也有同一边界：删除注释、改名或缩进即使保留部分程序运行语义，也可能丢掉修复线索，或让模型按压缩格式输出而无法匹配原文件。[受限SWE修复对照](https://arxiv.org/html/2606.01326v1#S4)出现输入减少而解决率下降，dedent另有补丁缩进失败；全bench主结果却排除了dedent，不能把全部退步归它。统一tokenizer计数只是代理，小样本变换消融也不等全人口因果。变换、原文映射、所有重试与测试都计费；格式或质量回归时保留原源码/注释、较轻删减与独立测试，不由parser语义或更少token自签消费者无损。<!-- source-family:SF-2026-ARXIV-2606-01326 -->

摘要后的继续执行还可成为单独的训练对象，验收也不能只看压缩器读起来是否完整：一条[分段训练分支](https://arxiv.org/html/2509.13313v1#S3)在预算触发处把历史改成问题加摘要，从该状态重新生成，并把整条rollout的终局相对advantage广播给各segment。它让消费者见到部署时的重启状态，却不给摘要或每段步骤独立真值；按总segment数平均还会使更长轨迹拥有更多项，不能默认为每轨迹等权。摘要生成、分段训练、全部工具/失败轨迹与后续长度都计费，成功query费用不能替全人口预算；同时增加工具步数的对照也不识别广播的单独收益。摘要遗漏未决项、状态保真或净质量失配时，保留原文引用、较完整近期历史与无摘要分支，不把有限窗口重启当作无限可靠探索或完整证据账。
<!-- source-family:SF-2025-ARXIV-2509-13313 -->

当轨迹主要被冗长工具返回撑大时，先降低远期observation的可见粒度，是比每次生成语义摘要更简单的基线：保留system/user约束、完整reasoning/action记录和最近若干轮的原observation，只把更早返回换成带原文引用的占位视图。它不把旧action重新执行，也不让被保留的reasoning取得事实权；原始工具结果仍须可回读，这是项目的证据合同。此法只减缓增长，reasoning/action本身仍会累积；递归摘要也须独立限制长度，不能默认任何一支恒定内存。[SWE-agent中的有限对照](https://arxiv.org/html/2508.21433v1#S3)表明，view选择还可能改变后续尝试长度，所以应共同验任务质量、完整轨迹与所有调用费，而不只比较当前输入tokens；部分thinking配置的删减/摘要都反退，未显著差异也不是质量等价。摘要调用、cache重用条件、被延长的后续推理与全部工具执行都计价，按API单价估本地token费用不等真实GPU成本；不能把“摘要掩盖失败信号”的解释当已证内部因果。近期窗口遗漏关键旧证据、状态已变或预算无收益时，应回读原文、保留较完整history或经独立验收的摘要，短任务仍可直接传全轨迹，不把更复杂或更短的view自行升级为可靠策略。
<!-- source-family:SF-2025-ARXIV-2508-21433 -->

对已知问题，extractive 分支可以不改写句子，而用一个学习到的标量衡量段落是否包含答题线索：分别编码完整段落和删去每一句后的变体，以两者分数差提议该句的条件贡献。这里比较的是“其余上下文仍在时删掉这一句”的模型读数，不是句子与 query 的相似度，更不是最终答案正确性的证明。训练标签、分句和 chunk 合并、encoder 与阈值共同决定这份派生视图；逐字保留被选句子也不能保证保住指代、否定或跨句组合证据。尤其两句互为冗余时，各自删除的损失可能很小，同时删去却会移走唯一证据，因此单句低分不能直接签发集合充分性。

这种选择以额外编码换取更细的删除信号：[受限 leave-one-out 对照](https://arxiv.org/html/2603.09222v1)的原始路径需要完整段落加各删句变体的多次 encoder passes，并行只改变执行安排，不消除工作量。整段低分门与句分数间隙阈值也需要独立质量检查；阈值退路未完整披露时，不补成保真 recipe。所测 QA 中部分 reader/任务仍低于未压缩输入，表内 compression time 更不等于包含目标 reader 的全链时延。训练、所有变体、分句、阈值校准、reader 与回归费用一起计入下面的 break-even；联合删句失真、阈值失配或总预算不合算时，保留原文、扩大保留集合或回读未压缩段落，而不是让线索分数代替 evidence gate。<!-- source-family:SF-2026-ARXIV-2603-09222 -->

如果任务与评分器已冻结，输入删减还可以从完整可行视图出发，逐步检验每次删除，而不是先对原文每项打分再一次删完。保留完整输入H作基线，在当前子集I中逐项试删并重跑同一consumer，只有声明的质量保留比仍过阈值才接受一次删除，随后在更新后的集合上重评；提前停止保住的只是这份proxy约束，并非全局最小或真实任务无损。[推荐模型的受限可行性研究](https://arxiv.org/html/2508.21547v1#S5)提供了这种backward选择实例，不能当作LLM Context已测收益，更不定义法律上的必要数据。可删多少依模型、metric、阈值与输入人口而变，用原模型完整输入输出估计reference又可能只保其原有偏差；平均NDCG保留不保证其他指标或每个用户同样保留。完整基线、proxy版本、候选删除顺序和独立holdout应分开保存，全部试删调用/原文访问与回归都计费，调用数不等wall-clock；约束不可靠、分母退化、未来任务未知或成本不足时，保留原文/高风险字段与已验固定选择，拒绝继续删除，不由更小子集自签充分证据或隐私授权。
<!-- source-family:SF-2025-ARXIV-2508-21547 -->

Context 是否修改也可由独立 router 先决定，再让具名操作处理派生视图：保留 raw history，以 LoRA 分支执行纠错或压缩，也允许 none，solver 消费修改后的 view 而不是覆盖原证据。训练 router 的数据可先让 teacher 执行候选 operator，比较 base solver 在 raw/refactored history 下的 paired outcome，只保留有改善的提案，再混合 corrective/compressive/none；这让结果条件决定是否重构，却不把 teacher 改写升为事实真值。<!-- source-family:SF-2026-ARXIV-2601-05589 -->

[受限重构对照](https://arxiv.org/html/2601.05589v1)使用 Qwen2.5-7B、E5检索与GPT5.2 teacher，Table1多项仍低于SearchR1或RECOMP；压缩token减少不能抹去router、operator、teacher生成/筛选与solver总费用。选择人口只含受测outcome改善，也不保证新任务保真；raw/derived identity、operator及结果版本须分开保存。Router错选、重构失真或净预算不合算时，保留raw history、none分支和原有压缩/回读，不让派生视图改写权限或提交事实。

在线 Context 选择还可以把判断延后到压缩后的短程反馈，而不只由原历史或训练好的 router 决定。预算触发时，从同一 raw history 构造保留近期、摘要和重置等候选 views，各自继续少量工具交互，再让 router 同时读取原历史与候选 continuations，选择一条后续路径。它改变的是 view 的验证时点：先看某种信息取舍怎样影响下一步查证，再决定是否继续；不是让压缩摘要取得事实 authority，也不是证明所有候选拥有相同状态或语义。

`arXiv:2603.27490v1` §3/§4.3 的有限消融中，看三轮后续反馈优于只看views或随机选择，但五轮反而退步，更多lookahead不自动更可靠。额外分支、原历史复读、summary/router和全部toolcalls均须计入成本，较少主轨迹turns或仅完成任务的token图不代表全人口省费；self-router也共享原agent的盲区。写工具或外部sideeffect不能随弃branch撤销，必要时只做可隔离/read-only试探并由可信执行器独立commit。预算、候选view或反馈不可靠时，保留固定近期/摘要策略、原文回读或none分支，不让在线选择越过Context和Tool的验证边界。<!-- source-family:SF-2026-ARXIV-2603-27490 -->

压缩之外，还可以把长原文留在外部环境，由模型用程序选择、变换并回读片段。但“能访问超过窗口的输入”和“值得递归调用子模型”是两个不同判断：前者来自外置原文与选择接口，后者要看任务是否需要子调用完成局部语义处理，还是根模型用代码就能筛选、聚合。应对照同样可访问原文的 no-subcall 分支，而不只对照被窗口截断的普通调用；局部新证据中，某一模型在代码问答和文档查找上去掉子调用反而更好，在信息密集的分类/成对聚合任务上却从子调用受益，因此不能把 external access 的收益统一归因于 recursion。<!-- source-family:SF-2026-ARXIV-2512-24601 -->

这一选择还要绑定根/子模型、任务样本和 evaluator：不同 child 配置不是相同推理预算，API 费用均值也不能代替硬件成本或尾时延；同步子调用、返回失败与少数长轨迹会改变端到端代价。原文、代码、片段范围和调用 provenance 应保留为可重放依据，在子调用无增益、成本失控或验证失败时回退程序化读取与有限 Context，而不是默认继续递归。外部执行是否允许访问文件、联网或产生副作用，仍由 Tool 层的权限与执行器决定，长上下文接口不授予这些能力。

固定周期压缩在 observation 短且预算宽松时易于重放；但若一条长工具结果即将进入窗口，先追加再裁剪可能已经溢出，盲目提前全量压缩又会丢掉仍有余量时可保留的证据。更精细的 admission 顺序是先知道待载入 observation 的长度和当前 headroom，再决定不压缩、只聚合部分旧片段，或在预算紧张时聚合更多历史，最后才载入正文。Context runtime 必须拥有容量检查与最终 commit，模型的聚合选择不能越过原文保留、policy pinning 和可回读引用。<!-- source-family:SF-2026-ARXIV-2604-01664 -->

这种延迟载入以额外的计数、决策和压缩工作换取更少的无谓信息损失，也把长度估计错误、片段级摘要失真与压缩耗时带进关键路径。作者仅在组合问答与长程网页搜索设置中测试了预算条件化、分段聚合及渐紧预算训练；它不证明训练出的策略在任意工具输出、长窗口或生产 SLO 下最优。短轨迹、原文可完整驻留、长度未知或高风险证据不宜压缩时，固定保留余量、拒绝过长 observation 或外置原文并按需回读仍是合理分支。

压缩准入还要算总时间，而不只是比较压缩前后的 token 数：同一请求上，`T_compressor + T_target(compressed) < T_target(original)` 才有时延收益；还要同时验实际压缩率、答案质量和压缩器的显存占用。短输入、便宜的目标模型或较慢的压缩器会使前处理吞掉 prefill 节省；长输入、可摊销的压缩结果或受限显存则可能改变选择。这个 break-even 随目标模型、硬件、长度、批量与并发重算，不能用单一压缩比例作为通用策略。现有作者实验只覆盖所测 LLMLingua 分支、模型/设备与任务，未建立生产尾延迟或任意证据保真保证。<!-- source-family:SF-2026-ARXIV-2604-02985 -->

若同一原文会被多个问题反复读取，压缩也可先于问题完成：将原文切成独立小段，让可训练的压缩器输出少量 soft embeddings，再按原顺序交给冻结的 reader，问题仍以原始 token 输入。一个[受限问答分支](https://arxiv.org/html/2509.19228v1#S3.SS2)用原文加训练问题生成 teacher 答案，只在同一答案的位置匹配各层 hidden states，从而学习压缩器而不更新 reader；它不是逐字重建，也不证明未见问题所需的区别都已保留。分段独立使表示可在问题到达前制备和复用，却仍须绑定 tokenizer、分段边界、压缩器与 reader 身份；缓存这种表示不等于任意位置的 KV 都能复用。这条路径在短输入仍可能变慢，字符计数、拼写等结构任务也可能失真，离线生成只把费用移出请求路径，teacher、训练、缓存维护和实际 reader 消费仍须结算。结构细节、未来问题或净预算不合格时，保留原文回读、不压缩的冻结 reader 与按当前问题选择内容的分支，不由较少 embeddings 推出普遍保真或端到端加速。

<!-- source-family:SF-2025-ARXIV-2509-19228 -->

软压缩的载体还可以来自原文中的位置，而非另加一组从零学习的slots：将原文分段，按覆盖规则选anchor token并叠加可训练标记，让双向encoder把整段信息汇到这些位置，再取各层anchor K/V交给因果reader。[SAC的有限问答对照](https://arxiv.org/html/2510.08907v1)用LM预训与QA目标训练这条接口，说明逐字重构并非所有压缩器都必需的中间任务；它不证明AE普遍有害、原token天然拥有充分语义或未见问题的信息无损。双向预编码、分段边界、anchor选择/位置、LoRA和reader的层KV布局须绑定，不能把它当在线因果cache任意删行，或给另一模型直接续读；较高平均QA仍有任务反退。全部预编码/训练、KV存储与reader消费及独立质量回归都计费，少量anchors不认证完整端到端省时；未来任务、格式兼容或净预算不合时，保原文回读、更大表示或未压缩reader，不让压缩状态替证据签发充分性。

<!-- source-family:SF-2025-ARXIV-2510-08907 -->

若程序性skill会被反复选中，也可在发布前制备绑定目标模型的多分辨率soft-prefix artifact：同一较长slots表示取前缀供较小预算，配合一份共享adapter教消费者读取，query仍保原文本。预算不必由长度单独决定；可以从原skill生成诊断题，以同消费者的full-text答案作银参考，选通过比较的最小分辨率，否则回原文。这只检验相对参考的行为一致性，skill、target与适配版本改变后不能沿旧资格通用分发。

[SKIM的有限对照](https://arxiv.org/html/2606.12203v1)中，弱full-text参考会误导选择，更高预算/更强teacher也不总改善；golden skill与模拟tool训练不证明真实检索、外部工具或权限正确。压缩器/adapter训练、诊断题与judge、每目标artifact存储/更新、读取及全部行为回归均计费，离线制备不签零开销或全链SLO。银参考、执行依赖或净预算失配时，扩大表示并回可审阅原skill/原base与独立工具结果核验，不让较少tokens批准动作完成。
<!-- source-family:SF-2026-ARXIV-2606-12203 -->

压缩容量也不必只依赖原文长度。一个受限分支让 query-aware encoder 读取分块 Context，由其末端 hidden-state probe 估计相关内容长度 `L_hat`，再以 `k=min(L_hat/r,k_max)` 决定 soft-token slots，并把兼容 K/V 交给目标 reader。它把固定 slot 数变成 query-adaptive capacity，但相关长度不是充分证据，也不证明压缩结果可供任意 reader 使用。Teacher 相关标注、encoder/probe 与 ratio/max policy 都须保存身份，额外 encoding、probe 和质量回归也要计入 break-even；[局部压缩对照](https://arxiv.org/html/2602.03226v1)显示短输入可能因 slots 过少而退步，不支持“压得越短越好”。长度估计失配、必要细节被丢掉或总成本不合算时，应扩大 slots、回读原文或退回固定容量/未压缩输入。
<!-- source-family:SF-2026-ARXIV-2602-03226 -->

重复日志还可以走另一条分支：不概括含义，而把重复子串替换为短标记并附字典。此时应把字典、标记和说明一并计入目标 tokenizer 的输入预算，并区分两个接口：软件按规则还原原文，以及模型直接在编码态完成任务。前者可以是确定性的 codec 合同，后者仍依赖模型是否正确查表、保持跨行关系并执行目标分析；可逆编码本身不会把这种能力一并交付。<!-- source-family:SF-2026-ARXIV-2604-13066 -->

因此，解压 exact match、字符相似度与目标任务正确性要分开验收，不能把较高的字符串重建分数当作日志诊断或跨记录推理的保证。作者的重复日志实验支持字典表示具有压缩空间、所测模型能够在部分协议下重建文本，但没有验证目标 analytics，也没有证明解压是所有语义任务的能力下界。重复度低、字典开销大、目标任务依赖未验证的编码态操作时，原文或先由软件解码再调用模型仍合理；高风险记录的原始 artifact 和逐字约束不能因 codec 可逆而移交给模型猜测。

不另带显式字典时，压缩视图也可以仍是原词表的离散text：只提示producer用多语词汇/符号保留关系，再让冻结reader直接消费，而不先还原可读自然语言。[受限文本分支](https://arxiv.org/html/2606.19857v1#S3)把人可读性、目标tokenizer长度与指定reader的任务可恢复性分开；低可读或高surprisal不等无信息，局部QA保持也不证明全语义无损或任意模型能读。Producer/reader、prompt、压缩强度、源范围及最终任务须共同绑定，跨pair的质量可能明显回退；强压增加reader thought时，短输入也未必总费更低。全部源读取/分块、压缩与搜索、检索/reader生成、人工审计和原文回读均付费，先读全源再压不能和直接截窗称同信息预算。保留原始artifact与逐字约束，高风险仍用typed字段；消费者、审计或净质量失配时，回可读summary/显式字典、较大原文窗口与有界回读，不由更短符号串或同模型自读的高分批准通用编码、安全通道和删除源记录。 <!-- source-family:SF-2026-ARXIV-2606-19857 -->

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

抽取与提交还可以使用不同的预算时点：由独立writer在窗口尚有余量时多次增量整理任务、约束、未决动作和原文引用，到真正换窗时再组装这些状态，而不是等满窗才同时做理解、压缩与恢复。[一份长任务coding runtime说明](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)给出这种前移分支；每文件single-writer可减少写竞争，却不证明后台视图覆盖最新tail，更不能代替上文的base revision与提交检查。提前writer、持久文件与回读原文增加后台计算、存储和失效维护，抽取不完整时仍需同步补齐或保留原历史。作者同模型harness A/B没有隔离writer，固定触发比例也未经独立最优性验证，不能从长任务组合胜率推出该机制净收益或任意长会话无损。<!-- source-family:SF-2026-MIMO-CODE-LONG-HORIZON -->

并行化能隐藏一部分压缩延迟，却增加双份 Context、取消/重做、版本冲突和 fidelity evaluator 成本；错误 commit 会丢 observation，过于保守则持续浪费后台计算。短会话、高风险逐字记录、剩余 token 很少或无法可靠合并 tail 时，应回退同步压缩、外置原文引用或不压缩。`arXiv:2605.23296v1` 的 §3 与 §5 支持作者 parallel compaction runtime 及 HotpotQA/LoCoMo 等受测合同，§6 不证明任意 Agent、压缩器、并发修改或生产 tail-SLO 都能安全隐藏 stall。

<!-- source-family:SF-2026-ARXIV-2605-23296 -->

可恢复 compaction 还必须区别摘要候选、Hook 执行和 canonical history 的提交。先持久化候选，才能在中断后沿原 operation 继续后续 Hook 与提交；未知 Hook 结果要查询原证据，不能像纯摘要一样重新生成后再执行。[Qwen Code 的固定合同](https://github.com/QwenLM/qwen-code/blob/d03b3116dae52589210a50f84ac099876f75326c/docs/design/2026-10-22-managed-context-compression.md)将 compaction 与 terminal maintenance outcome 原子登记，保留原 audit transcript；纯摘要可能重复计费，但不能因此重复提交历史。窗口边界也不能只沿旧 writer watermark 放置：[MiMo 的 rebuild 修复](https://github.com/XiaomiMiMo/MiMo-Code/pull/2702)把 boundary 放在最新消息之后，并将已接受但未投递的输入另列 deferred state，避免 tail 反复进入窗口或用户输入被摘要截断。这增加候选持久化、revision、tail 与恢复配对成本；原件可低成本完整驻留时，简单同步压缩仍合理。公开合同与局部回归不证明摘要语义无损、任意 Hook 可重试或所有并发部署安全；输入配对或 operation 证据缺失时保持 blocked、回读原文，不把一次压缩完成签成下一任务正确。<!-- source-family:SF-2026-QWEN-CODE-DURABLE-COMPACTION;SF-2026-MIMO-CODE-2702 -->

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

代码的选择粒度还可以分成两级：先按函数或class提出候选，以当前instruction的条件perplexity变化排序，再把保留函数的预算分给内部完整代码块，按块的代理分数与token成本作受限背包选择。[LongCodeZip的有限对照](https://arxiv.org/html/2510.00446v1#S3)给出这条coarse-to-fine分支，不把PPL差当真实互信息，也不因函数/行边界就认定依赖闭包、语法或运行语义完整。函数身份、原位置、保护集合、block边界、评分模型与实际tokenizer须共同保存；最低保护项放不下、预算重缩放或分数退化时，应扩大预算/回读原文，而非强行删关键依赖。块价值可相互依赖，预算内代理最优不等最终代码正确；EM/相似度、摘要judge或needle命中也不代编译执行。所有评分前向、切分/分配/DP、压缩与目标生成及回归均付费，部分模型仍会退步；短输入、廉价consumer或净收益不足时，保留整函数、只做coarse筛选、原源码与独立测试，不从更短输入签无损或通用加速。<!-- source-family:SF-2025-ARXIV-2510-00446 -->

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

预算内可接受与值得裁剪也不能共用同一个阈值：若自动摘要在较高水位触发，却先按更低的安全目标删除最旧历史，正常压缩请求也会主动打断可复用前缀。[一个固定实现的纠错](https://github.com/MoonshotAI/kimi-code/pull/4456)先判断完整请求是否真的超过“窗口减输出预留”，只有超出才裁到安全目标，并把摘要输出上限约束到剩余空间。媒体回退同样应固定当次拒绝时的降级范围，不能每加一张新图就滚动改写旧前缀；新请求再被拒绝时才重新评估。它增加估算、快照和前缀诊断成本；估算失准仍需缩减重试，字节前缀保持也不证明服务端命中。无缓存、真超窗或高保真输入场景继续保留原压缩/回读路径，不把较短请求当成更低总费用。<!-- source-family:SF-2026-KIMI-CODE-OCT27 -->

功能回答正确还不能验收缓存集成，连用来确认命中的计数器也可能解析错。应把请求侧的provider/model能力、marker形状与prefix稳定条件，和响应侧cache-read/creation字段的缺省、聚合、计价分别核对；[一种集成检测分支](https://arxiv.org/html/2610.34817v1)将调用点的条件与带核验日期的外部能力表绑定，而不让模型凭记忆判断当前API合同。局部静态检查不能覆盖跨轮prefix重组或mutation，LLM guard也会误报漏报，因此仍须保留多请求投影与真实request/usage对照。能力表维护、静态分析、人工核警和运行探针都计费；已知语法与计数检查可继续作廉价基线，provider语义或meter不可信时保留Unknown/原始usage并回源，不以零cached-token或普通测试通过单独宣告缓存失效或费用已降低。<!-- source-family:SF-2026-ARXIV-2610-34817 -->

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

运行中的可信控制更新，也不必通过改写既有system prefix或伪装成user turn传入。[Opus 4.8公开的Messages API合同](https://www.anthropic.com/news/claude-opus-4-8)允许在messages数组中追加system entry，以更新任务权限、token预算或环境信息并保留旧prefix cache；这里的append不等于修改先前bytes，更不使物理cache拥有当前权限。Context owner仍应校验更新的可信来源、scope与policy revision，把当前有效约束绑定到本次request，并由executor在动作边界执行；web、tool或memory内容不能自行升格为system指令。该发布只确认消息接口，不证明所有SDK/backend兼容、任意cache布局无失效或安全性提高，额外context与重处理仍计费；接口不支持或当前约束不能完整兑现时，重建合法request、接受保守cache miss或停止敏感动作，不以缓存命中为授权证书。<!-- source-family:SF-2026-ANTHROPIC-OPUS-4-8 -->

## Observability 与 Evaluation

Context evaluation 应分解：

- selection recall：所需信息是否入选；
- precision：无关/冲突内容比例；
- placement/use：模型是否使用正确 evidence；
- faithfulness：结论是否由 evidence 支持；
- cost/latency：assembly、Prefill 和 storage read；
- privacy：是否越权读取或记录敏感内容。

只评最终答案会无法区分 retrieval miss、bad ranking、compression loss 与 model misuse。

固定目标、进度可从文件重新读出的任务，仍可用最终产物分数验收结果；但它可能对历史替换不敏感，因为遗漏的信息能够从工作产物补回，而用户后来追加的工作方式与禁止范围未必存在于文件中。评价应先区分这两种可恢复性，再分别检查产物、约束留存与实际遵从，不能以任务分近似不变推断交互约束完整。[受限压缩对照](https://arxiv.org/html/2610.31778v1)支持这一测量边界，不证明压缩导致作弊：所测作弊早于首次压缩，真实会话的约束留存又依赖judge，未测其最终任务伤害；少量任务、模型与触发区间也不能签发通用阈值。额外约束标注、分层检查和重跑都有成本；交互约束未知或评价不可靠时，保留原始指令、独立执行检查与可回读历史，而不由基准分数批准删除。
<!-- source-family:SF-2026-ARXIV-2610-31778 -->

在同一状态重放之外，配对统计还要保留变化方向：固定代码工作树、继续执行的模型、工具和预算，分别从完整历史与摘要续做，把原本成功而摘要后失败计为损害，把反向变化另列为挽救，不能只用总成功率让两者相抵。标识符或修复词串仍在，也不保证消费者能把证据转成正确编辑；[配对修复对照](https://arxiv.org/html/2610.31710v1)中，这两种验收给出了不同的配置排序。字面细节留存集与修复集应各报分母，连续production压缩的后续可评价子群缩小也不能直接当作同一人口的纵向衰减。配对重放、环境还原、重复确认、摘要与全部后续工具执行均计费；私有轨迹及缓存状态未公开时，结果表可重算不等原实验可精确复跑。任务、消费者或预算改变后应重新验收，分歧时保留原历史、更完整状态或回读入口，不把较高保留率当成续做保证。
<!-- source-family:SF-2026-ARXIV-2610-31710 -->

即使每条外部内容都没有显式指令，选择哪些内容、按什么比例和顺序让模型连续阅读，也可能改变下一次决策。可固定模型、persona与最终问题，仅干预此前的暴露轨迹，再分别测原默认方向、反方向与无变化条件；[有限feed对照](https://arxiv.org/pdf/2606.00914v1)支持把上游选择器纳入Context审计，而不把下游prompt单测当全链安全。效应依模型与任务而变，平衡或披露并非普遍防御，forced-choice建议也不等真实动作；逐帖无恶意标记不认证整体暴露无偏。数据池制备、全部暴露轮次、重跑和防御均计费，轨迹内probe须按run分组并比较可见history基线。选择器或默认方向改变时重验；影响不可控时保留固定可信源、显式来源与人工批准，不由filter未报警批准执行。<!-- source-family:SF-2026-ARXIV-2606-00914 -->

反过来，只用抽取视图与reference的词面重叠来调selector，也不能保证下游reader排序相同。可固定文档、token预算与generator，分别比较所选context自身的coverage proxy、生成答案/摘要及full-context；再以Lead与shuffled位置对照、同unitization换selector，判断收益来自文档前置结构还是减少冗余。[必要有限对照](https://arxiv.org/html/2605.00336v1)出现低预算抽取偏好Lead而生成更偏好MMR的条件差异，不能把extractive dev上调好的阈值直接当生成router。RCD等覆盖/多样性目标仍是代理，ROUGE与BERTScore都不认证事实正确，单个罕见关键约束也可能被删。编码、pairwise相似度、选择/调参、generator与回读一起计费；任务、文档顺序或指标迁移时重校准，收益或充分性不稳则保留full context、简单选择与原文回读，不由更小输入预算签发全链提速或安全。<!-- source-family:SF-2026-ARXIV-2605-00336 -->

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

不编辑 trace 时，也要把“前轮推理是否继续进入输入”与“本轮是否生成新推理”分开：只保留回答和工具结果在短任务中便宜透明，跨轮任务则可以继续携带模型已经生成的推理块，同时按当前请求选择是否再付推理计算。这不是扩大模型窗口、写入长期 Memory 或让旧推理成为事实。运行时需保留原序列、来源轮次与模型/模板身份，并分别验收 retention 与 compute 开关；错误推理会持续条件化后续回答，完整保留也增加窗口、KV 和敏感派生内容的占用。GLM-4.7 的公开说明支持这种接口分责，但整模型成绩与不同评测配置不能证明单独保留推理的收益，也不保证净省费或 cache 命中。接口不兼容、任务短或继承错误时，回到普通对话历史、原文回读与独立验收，不让关闭新推理被误当成清除旧状态。

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

压缩可发现的skill还须分开路由与功能消费者：先让一个只含描述的shadow skill模拟与原文的竞争，提出更短的触发描述，再用真实router在指定query子集核是否仍会调用；失败时有限恢复原描述或直接回退原文。只有路由资格通过，才分别压正文/引用并验证实际任务。[SkillReducer的受限协议](https://arxiv.org/html/2603.29919v1)把这两个消费者分开，却不证明模拟judge与真实router等价或任意query触发不变；536/536包含39次原文fallback且排除了原失败人口，任务与同预算切片仍有反退。压缩、模拟候选、真实调用、恢复、引用读取和任务验证全部付费，Stage2保留当前best也不能认证无损。Router版本/query支持、正文功能或净预算失配时，恢复原skill和完整引用、保留人工/真实任务回归，不以描述相似或触发一次批准全部能力保留。<!-- source-family:SF-2026-ARXIV-2603-29919 -->

有界执行视图还要区分任务阶段：某动作在当前阶段已尝试，不代表环境改变后永远不可重试。[PABU 的一个分支](https://arxiv.org/html/2602.09138v1)保留 goal 与最新 observation，用 learned progress 更新阶段，并仅在同一阶段积累 attempted actions；阶段推进时重置该集合，同时学习保留哪些旧 observation。它把“防重复”改为 stage-conditioned 状态维护，而不是无条件删除旧动作或堆积全部历史；available actions 从观察解析，不由此认证真实环境可执行。<!-- source-family:SF-2026-ARXIV-2602-09138 -->

progress 文本仍是 learned observation，不是可信 authority、Bayesian belief 或严格 Markov state；误判阶段、漏保留前提与未见失败都可能导致错误重试或丢失恢复线索。受测 context masking 同时改变训练与评价，不能归因于单独上线删历史；输入 token 减少时输出 token 反而增加，也不授所有任务成本更低。阶段识别或保留策略失配时，回读原始观察、恢复更完整历史，并以真实环境反馈复核 frontier；“不重复”不应凌驾于必要重试及后续状态验收。<!-- source-family:SF-2026-ARXIV-2602-09138 -->

长期有效的约束还应从自由文本摘要中分离成 versioned state，记录 scope、expiry、来源与当前执行 frontier。side channel 增加 schema 和迁移成本，但避免多轮 compaction 把强约束降成背景事实。低风险问答仍可使用普通摘要，外部 effect 越大，越需要 paired-state regression。

压缩时机同样不是固定 token 阈值就能决定：如果任务还在搜证或等待工具结果，删除早期观察可能使下一步无法修正；当环境状态、未决约束与后续行动已达到可检查的 READY 条件，才允许提交一个更短的执行视图。触发器只提出压缩时机，Context owner 必须检验 pinned constraints、raw handles 和恢复路径；误报比延迟压缩更危险。StateComp 的作者受控任务显示 token 节省与平均回报接近的受限权衡，但若原始历史不可回读、跨模型/任务状态识别漂移，固定阈值、保留更多近期记录或暂不压缩仍更稳妥。<!-- source-family:SF-2026-ARXIV-2609-27298 -->

即使删除时机合适，也不能把每段历史的“可删性”独立相加：两段分别可删的记录可能互为唯一备份，同时删除就会丢掉约束。更稳妥的对象是**实际提交的删除集合与保留下来的内容**。一个受限实现先在已完成轨迹上联合删除 protocol-valid 的 tool exchange/assistant blocks，以同一已记录下一步输出的 teacher-forced likelihood 差作离线风险标签；线上只用当前可见状态预测候选集合风险，保护近邻与固定约束，并在没有低风险集合时 abstain。它把单项排序改为集合级提交，但 learned risk 不是安全保证：teacher-forced 下一步与真实继续执行不同，误判、额外特征计算及不可恢复的原文删除仍需 raw fallback 和任务级回归。短会话或完整历史可负担时，保留原文仍是简单基线。<!-- source-family:SF-2026-ARXIV-2609-27276 -->

<!-- source-family: arxiv:2608.06503v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: context-compression-paired-state-regression -->

### 持久 Instruction 更新应先修改 Typed State，再重建文本 View

直接编辑长 prompt 最接近人类写作，却容易在局部修改时破坏相邻约束、引用或优先级。更稳健的分支把持久 instruction 表示为 typed dependency graph：模型只提出 scoped patch，validator 检查目标节点、依赖与不变量，commit 后再生成带版本的文本 checkpoint。图是 authority state，文本是派生 view；无法无损解析的自由文本仍保留人工编辑路径。

外部规则热更新还要区分当前磁盘内容、已渲染进上下文的描述和 runtime 实际允许的能力。一个[公开实现案例](https://github.com/MoonshotAI/kimi-code/commit/18c6d64272952503baccf706bff455bb6a2c488e)为渲染快照维护可重放、可撤销的比较基线，让 watch 与 reload 共用去重，并在 clear/compaction 后重建；逐文件身份也避免尾删或清空被旧片段匹配漏掉。这比每次读盘直接提醒更易恢复，却增加基线、订阅和恢复状态。实现先记录基线再通知，工具不可用时还可只推进基线，因此它不是模型已消费的确认，更不保证 exactly-once delivery 或遵从新规则。通知、上下文容量和恢复均有成本；状态资格或提醒能力不足时，保留显式 checkpoint、重新渲染与 runtime 原权限，而非把 reload 完成当上下文已经生效。
<!-- source-family:SF-2026-MOONSHOT-KIMI-CODE-20261016 -->

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

推测用户愿意执行哪一个动作，还须与“这个已选动作做得怎样”分开。一个纵向研究分别收集 action-selection 意图与仅对已选动作给出的 execution 判断，再比较用户自己的历史、等量其他用户历史和全部历史；只有保留两个分母，才不会把未选择误当执行失败。[受限个人历史对照](https://arxiv.org/html/2604.23815v1)支持个人上下文可能有用，却不证明生成动作内在比执行更难，也不使几个月后的意图保持不变。小型研究者人口、解释过滤的 test 子集与重叠置信区间限制自动个性化结论。历史收集、隐私治理、标签/检索与新调用均付费；偏好漂移、来源不足或涉及新副作用时，保留当前明确指令、请求澄清或静默，不让预测的选择意图取代用户授权。<!-- source-family:SF-2026-ARXIV-2604-23815 -->

### Context Compression 要保留未来更新所需的区别

只以“压缩后仍能回答当前问题”作为目标，在一次性问答中合理；长期 Agent 还会收到新 observation、纠错和目标变化，当前不重要的区别可能成为下一步更新的必要条件。压缩器因此要同时提交 current-answer sufficiency 与 future-update preservation：保留可恢复引用、未决分支和会改变后续 belief/action 的 distinctions，而不是把所有当下未使用的信息合并。<!-- source-family:SF-2026-ARXIV-2609-20045 -->

保留未来可用性会降低压缩率，也无法穷举未知问题。作者结果只支持其任务和 future-query construction；高风险或未来需求不可建模时，应保留原始 archive、可逆摘要和按需回读，压缩视图不能取得事实 owner。

未来可用性还需要单独的评价人口：把压缩时已知的问题与未展示的后续问题分开，在实际保留 token 数相同下加入 random deletion 基线，再按是否共享证据和后续 consumer 所需内容分组。保当前问题所需整句，可能漏掉别的问题；保散布的 content words 能改善某些阅读题，却可能丢掉工具调用需要的完整 identifier 与结构，因此没有由一个平均分决定的通用压缩顺序。Label 恢复也不等被保留文本支持，应另报 evidence/原始 handle 保留与 support 核验。[现有对照](https://arxiv.org/html/2610.27301v1)只覆盖公开文本和录制轨迹的 ID 问题，不是 live agent 后继成功；保 archive 也不保证重取命中，构建、检查和回读可能超过 full state 成本。未知需求、证据缺失或净收益不足时，保留更完整历史/可恢复引用与独立后续任务回归，而非以当前题或更少 tokens 批准不可逆删除。<!-- source-family:SF-2026-ARXIV-2610-27301 -->

### Context Selection 应从 Claim/Action Obligation 反推最小证据包络

按相似度追加更多 token，可能仍漏掉决定能否行动的关键前提。更严格的路径先定义 claim 或 action obligation，再沿 derivation graph 选择覆盖其 closure 的最小 sufficient evidence envelope；包络不充分时状态保持 unresolved，不能用 context 更长冒充 assurance。<!-- source-family:SF-2026-ARXIV-2609-16302 -->

该方法降低 context/cost，却引入 obligation discovery、schema/type 与 solver complexity。图不完整、obligation 不可信或行动风险高时，应回退更宽 evidence set、deterministic checks 或人工审阅；少量 preserved artifacts 与 synthetic 数据不证明自动发现义务。

## Review notes

- `SF-2026-ARXIV-2606-19857`，Jun20补Jun19；消费sole§108唯一exact-v1必要，2+1+2=5，actualCh75 softcompression/字典codec两完整前肩、未来充分性两后肩及Ch22/82交接已读，仅原词表text低可读-v-pair-specific恢复/额外thought差额深入。保跨pair负侧/强度混杂、LoCoMo低原/CodeRepo全源权限与Kimi行身份未闭/全部费ND；不授通用lossless/安全，未核实现/复现，PRE/SAVE/selfread/actualPOST仅本日实际层。

本人注：`SF-2025-ARXIV-2510-18117` — Locke，Daily2025-10-23补Oct22；exact-v1 §4–5/A.4.1必要，2+1+2=5，当前回答/未来异步教师demo写入差额深入。保三次一致/entropy/相似非truth、SigLIP替换基线、派生pool漂移与教师/检索/prefill全费；不采实测全碳或服务SLO，未核实现/复现。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。

- `SF-2026-ARXIV-2606-20047` — Daily2026-06-20补Jun19；复用sole唯一必要[exact-v1](https://arxiv.org/html/2606.20047v1)§3/5，作者actualCh75 Assembly/Compression/旧trace核，2+1+2=5。只跨类型集合覆盖与token预算/consumer可提取性分责，保tightbudget输topK、有限100题/tworeader+judge、代理/顺序/全部费用，不采未闭常数近似、fullcontext优越或净速。旧trace非正文采用证据；未核artifact/复现。唯一reader A9实际owner/完整稿PRE已通过，作者按原稿SAVE；完整selfread与sole actualPOST按本日真实后到层，不由本注预签。

- `SF-2025-ARXIV-2510-13799` — Daily2025-10-17补Oct16；exact-v1§3/式1、§4/T1–3必要，2+2+2=6，仅short-to-long共同扩展/答案条件剪裁的训练消费差额。保oracle/gold权限、长度混杂、LongSeal及reader反退、近似句数/word非token和全费，不采完整保真/净速或新任务充分性；未核代码/复现。PRE/真实SAVE/完整自读/solePOST只据canonical实际后到。

- `SF-2026-ARXIV-2610-34817` — `live1028_china`，Daily2026-10-28/Oct27首次公告，只采用[exact-v1](https://arxiv.org/html/2610.34817v1)§V–VIII/Alg1/TIII必要域，2+2+2=6；v2提交不另计重要修订。request条件/readmeter与May10 dated oracle、single-site guard差额经唯一reader必要/actual owner/整段PRE独核；A recall是rule来源同集，B precision-only，27silent request/usage验证不是省费实测，多快照prefix问题不在检测范围。未核artifact或复现；实际SAVE/POST见本日ARXIV_AGENT/REVIEW，不由本注预签。

- `SF-2026-KIMI-CODE-OCT27` — `live1028_china`，Daily2026-10-28，kimi-code同家族4个Oct27实施事件中的[#4456](https://github.com/MoonshotAI/kimi-code/pull/4456)，精确`68a283894163204e93b072cef20db164015a5cad`；2+2+2=6。仅触发/裁剪目标分责及媒体投影快照差额；必要fullCompaction/llmRequester代码与局部regression定义已读，非真实provider命中率/费用测量，未运行或复现。唯一reader必要/实际owner/整体PRE已通过；实际SAVE与写后复核按[本日CHINA](../../papers/2026/10/_sources/daily-20261028/CHINA.md)及REVIEW后到记录，不由本注预签。

- `SF-2026-ARXIV-2610-31778` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31778v1)§3–5核心方法、metrics/Q1–Q4与limits首次必要按§9复用，2+1+2=5，实际AGENT-CONTEXT Ch75单段差额。仅文件可恢复/历史独有约束的评价人口边界，不重复既有rulepin/snapshotfork/enforcement；保validsubmission/触发区间、Gemini少compaction、异judge与作弊先于压缩反侧及全标注/重跑成本，不采压缩导致违规/普遍无损或阈值。未核代码/全部附件或复现；PRE/真实SAVE/selfread/solePOST以本日实际记录为准，本注不预签。
- `SF-2026-ARXIV-2610-31710` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31710v1)§3–5与G可得性/工具/预算首次必要按§9复用，2+1+2=5，实际AGENT-CONTEXT Ch75单段差额。仅同代码状态配对damage/rescue分向分母及literal/production异人口，不重复一般replay；保固定Kimi-K3/预算、选PRE成功、后续小子群、输入截断/输出长度与privatecache限制，全部还原/确认/工具费；不采保留率即续做保证、总体损害频率或精确复现，未核代码/运行。PRE/真实SAVE/selfread/solePOST仅本日实际记录，本注不预签。

- `SF-2025-ARXIV-2510-04560` — Arendt，Daily2025-10-08补Oct07；原6，采用R25决定/root R383余必要§4.1–4.2/T1/C/T5/E/F/G2与R433独占actualowner，不第二Methods/owner。仅semantic retrieval→当前对象关系graph结构重写→context装配差额；保source/current/mapping身份、union/重embedding非delete事务、retrieval消融同时关AR、模型选难度3:7/同源8shot人口、局部TextOCR反退和找对/反思仍答错。22.5K/3.26s非全SLO，全部制样/embedding/图/改写/推理/核验费保；不采完整recipe、图即truth/实际导航或通用净速，未核失败像素/全prompt/实现与复现，PRE/SAVE/fullselfread/solePOST仅本日canonical真实后到层，不以本注预签。

- `SF-2025-ARXIV-2510-06557` — Daily2025-10-10补Oct09BJT；[exact-v1](https://arxiv.org/html/2510.06557v1)，2+2+2=6，Jason R12唯一首次必要直接复用。仅清KV/原query+固定首块与近期chunk重编码的context重启差额；保相对原query的界、非Markov充分、过短质量与24k反传反慢/96k成本估算非实测，AIME24选checkpoint非独立holdout及全prefill/训练费。不采无限可靠推理/生产SLO，无代码复现；PRE/SAVE/完整自读/solePOST仅本日canonical真实后到，不预签。 Jason R24整体PRE/窄授后真实SAVE与完整自读/QA已成，R26唯一actualPOST通过，指定窄位释放；仅同步既成态，不授DAY。

- `SF-2025-ARXIV-2510-00446`：Daily2025-10-03补Oct02；[LongCodeZip exact-v1](https://arxiv.org/html/2510.00446v1#S3)，2+1+2=5/函数与块两级预算gap深入。仅PPL代理→coarse→函数预算→块选择；保非MI/依赖闭包、clamp后重缩放/保护集可行性、Seed/Claude/crossmodel反侧、指标资格及2.58+6.59全费，不授语法/执行无损、完整allocator或普遍提速。未核全T4/5/图曲线、代码或复现。R25原分/日门复用；root R95必要/actualowner/整体PRE及窄授通过，真实SAVE/fullselfread后root R98唯一actualPOST通过、指定窄位释放；仅行政同步既成，不授DAY。

- `SF-2025-ARXIV-2510-00615`：Daily2025-10-03补Oct02；[ACON exact-v1](https://arxiv.org/html/2510.00615v1#S3)，2+2+3=7。只采离线full-success/compressed-fail更新guideline、success-only压短/蒸馏及history/observation独立触发/计费；保轨迹分叉非因果、同集择优/teacher筛选、阈值反退、peak-token非HBM/时延与缓存折扣后history不必省费。原文/none退路与训练/工具/压缩/完整生成全费近文，不授无损/事实authority/SLO；未核代码/复现。Kuhn R8日期/R23必要、actualowner与整体PRE通过，真实SAVE/fullselfread，Kuhn R26唯一actualPOST通过，窄位释放，不预DAY。

- `SF-2026-ARXIV-2606-12203` — Daily2026-06-12补Jun11，supp_jun12；[exact-v1](https://arxiv.org/html/2606.12203v1)，2+2+2=6，actual gap深入。§3–5/7/A/C/E必要；只per-skill/target多分辨率artifact与银参考离线校准/原文回退，保模拟tool/弱参考/兼容与全费；完整费用与原路径/独立核验保正文，不授普遍质量/安全或SLO，未核代码/复现。唯一reader jun12_review_finish canonical§43实际必要/actual owner/原两段PRE通过并窄授，作者按原稿真实SAVE，jun12_review_finish唯一§44实际POST已通过，指定窄位已释放，仅同步既成状态，不预DAY。

- `SF-2026-MIMO-CODE-LONG-HORIZON` — Daily2026-06-11补Jun10；[官方工程说明](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)§3.1–3.5/§5及§2 NOTE，2+2+2=6。只补提前多次writer抽取与后续rebuild提交的预算分工，不采固定比例最优、single-writer即原子最新或harness组合收益唯一归因；语法迁移仍计划态、全费用/原文回退保留。未核代码/复现。root SUP_REVIEW_20261026 §2实际必要Source/现owner/逐字PRE通过并窄授，作者真实保存及完整自读后，root已实际完整新增/直接两侧/本人注唯一非writer POST通过，本句只行政同步既成结果，不预签日级。

- `SF-2026-ARXIV-2606-04628` — [RAMPART exact-v1](https://arxiv.org/html/2606.04628v1)，§2–4/F1–2文字图注及§6，5分；只采固定邻居组合/组内顺序与位置分离的受限诊断分支。31-block firmware/literal probe不证完整任务或通用attention因果，schema移除不证executor撤权，零prompt-token方法调用不等零总费；未核代码或复现。

- `SF-2025-ARXIV-2509-20461` — Socrates，Daily2025-09-27补Sep26；[Conformal Importance exact-v1](https://arxiv.org/html/2509.20461v1) S2–6/E4–15/A1.1–2/C5有限必要，2+1+2=5。只按document重要句召回校准抽取view；保marginal非逐件/标签非truth、ties与alpha端点/空标签、abstractive不继承、400split与同源proxy/局部反退及全费，不授临床/法律安全。R14首次准备→作者18唯一actual采用通过；作者24原三项/完整侧组经R23整体纯PRE通过，root本轮fresh独立新窄授后作者27原技术稿真实保存并完整自读，Helmholtz R26唯一actualPOST通过，I5生效且指定窄位即时释放；本句只行政同步既成，不第三POST。未核全部图像素/代码或复现。

- `SF-2025-ARXIV-2509-19228` — Singer，Daily2025-09-25补Sep24；exact-v1 §3.1–3.3/Eq1–3、§4.1–4.6/T1–2/F2–6必要，2+2+2=6。Sartre R12有限Source通过；只采独立segment的query前CE制备/冻结reader与answer位置hidden监督分责，不采任意未来问题充分、字符结构保真、通用4x/总KV50%或净费。保短输入反慢/短context质量反退、OEjudge与MCregex/拼接及LOFT人口、teacherStd退化、所有teacher/训练/缓存/reader费用与原文退路，未核代码/图像素/复现。Sartre R14完整原三项纯PRE通过，root本轮fresh独立新窄授；A26已按原稿真保存/完整自读，Sartre R20唯一非writer actualPOST通过，新I2生效且本指定窄位释放；仅行政同步既成结果，不第三POST或授日级。

- `SF-2026-ARXIV-2606-01326`：2+1+2=5；exact-v1 §3–4/T1–4与dedent分析；保全bench无dedent、tokenizer代理、样本/分母限制与patch格式反例，不采任意程序无损或全部退步因果。 未核实现或复现。独立Source/owner/逐字PRE通过，root实际保存；非writer `jun03_next_reader` 已真实读取完整新增、完整直接两侧与本人注，唯一actualPOST通过（本日SUP_NEXT_REVIEW_20261024，末项R20）；本句只同步既成结果，不授完整DAY。

- `SF-2026-ARXIV-2606-00914`：精确v1 PDF §3–6；3+2+2=7。仅feed选择干预与默认方向，保null、防御失败、建议非动作；HTML同版本URL日期/摘要差异保留，不采2785总量或格式历史逐字一致；未复现。 Source/逐字PRE经独立复核通过，root已实际保存；非writer真实完整写后复核已通过（SUP_RESUME_REVIEW_20261024 R12）。

- `SF-2025-ARXIV-2509-13313` — author18，Daily2025-09-18补Sep17；[ReSum exact-v1](https://arxiv.org/html/2509.13313v1)§2–4/T1–2/A–D.2必要，2+2+3=7，summary-conditioned continuation/segment消费差额深入。保segment非独立真值/非轨迹等权、format门、§3与B gap合同冲突、GRPO40/ReSum60及query预算混杂、summary模型与分项反退、D成功人口非总费；未授无限成功/可靠gap或完整原证账，未核图全部点/实现或复现。

- `SF-2026-QWEN-CODE-DURABLE-COMPACTION` / `SF-2026-MIMO-CODE-2702` — Daily2026-10-23，各家族2+2+2=6；固定Qwen合同Admission/Execution/Recovery及MiMo rebuild spec S2.6必要。候选/hook/terminal与newest boundary/deferred分责；旧已清原文不可恢复，不授无损并发。独立reader Source/actualowner/联合逐字PRE通过，root已存本段，独立reader实际POST已通过，未运行代码。

- `SF-2026-ARXIV-2610-25760` — Daily2026-10-21窗Oct20；exact-v1 §3–7，2+1+2=5。保当前生成/旧thought保留/compute分账、attempt与strictsuccess分母、secondpass/oracle与probe/action限制；未核代码/复现。reader R135必要Source/actualowner/完整PRE原样通过，root已授Trace-as-State完整成本段后/state tools前单段及本人注；作者真实保存，唯一reader R140 actualPOST通过并生效释放；只行政同步，不第三核、不授DAY。

- `SF-2026-ARXIV-2610-27301` — Daily2026-10-22，[exact-v1](https://arxiv.org/html/2610.27301v1)§2–6/8与C/G/L/N必要域，3+2+2=7。仅同token random基线/known-hidden/evidence-ID消费者使排序反转的验收差额；保EI反转非token-matched、FEVER label非support、recorded ID非live、ECov known损失与恢复高费，不授通用最优压缩或archive无损。作者G3/reader R66必要Source/具体owner/PRE通过，actualPOST另见本日REVIEW；未核实现或复现。

- `SF-2026-ARXIV-2605-30785` — Daily2026-06-02补Jun01；[exact-v1](https://arxiv.org/html/2605.30785v1)，6分，必要域见作者SUP及独立原件。root R10日证/准入、R19必要Source/实际owner/完整PRE通过并授本单段+本人注；root R20实际完整新增/直接完整两侧/本人note及两层限定diff-check POST通过，第6/7真实整合生效、两位释放；仅行政同步，不第三Source/PRE/POST，未核代码/复现。保manager/consumer样式兼容、32K/native条件不匹配、破KV与全费；runtime保护是工程要求非论文已实现。

- `SF-2026-MOONSHOT-KIMI-CODE-20261016` — [Daily 2026-10-17](../../papers/2026/10/17/README.md)，PR4019精确commit `18c6d642`；ORG_A事件A。仅持久比较基线/生命周期，保record-before-notify及无工具仍推进基线，不采消费ACK/exactly-once/遵从保证。仅读代码/测试源，未运行；同家族guard事件B仅报告不写书，实际非作者写后复核已通过（本日REVIEW/ORG_A及root接纳）。

- `SF-2026-ARXIV-2605-00336` — Daily2026-05-05补May04；[exact-v1](https://arxiv.org/html/2605.00336v1)，2+1+2=5，具体owner差额深入。必要Source/date/直接反侧见唯一SUP R33；root C15实际owner完整邻接/逐字PRE通过，授单段及本人注。费用、反侧和旧分支近正文，不授普遍性能/安全/完整理论；作者已保存，root C19非writer实际正文/完整局部邻接及本人注POST通过、窄lease释放，不预签DAY；未核实现/复现。

- `SF-2026-ARXIV-2604-23815` — Daily2026-04-29补Apr28自然日；[exact-v1](https://arxiv.org/html/2604.23815v1)§2/3.1/4.1–4.4/5必要层；2+1+2=5，selection意图与selected-only execution人口分责具体差额深入。不授生成内在更难/静态意图或history代授权，受限人口、重叠CI/标签过滤与全部费用近正文。root必要Source/actual owner/逐字PRE通过并授本单段+本人注窄lease；root非writer实际新增正文、完整上下邻接与本人注POST通过，窄lease释放，作者仅同步已发生行政状态，未核实现/复现，不授DAY。

- `SF-2026-ARXIV-2603-09222` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09222v1) 必要§3–5/A1–2与相关评价反侧，2+1+2=5，条件删句proxy/集合充分性与多次encoding差额深入。root作者与supplement_20260312非作者必要Source/date/逐字PRE通过；v1多encoder不回填current单encoding，真实反退、阈值退路未闭合与全链费用近文。作者及非writer均已实际顺读损失→删句→router→break-even完整邻接与本注、回对有效必要原证，POST通过；不授全图、代码/复现或DAY。

- `SF-2026-ARXIV-2601-05589` — Daily `2026-01-13` 增量；[exact-v1](https://arxiv.org/html/2601.05589v1) §4.1/4.3/5.1/Table1；router/LoRA derived view、paired outcome筛选；raw保留/多基线反侧/费用近文；2+2+2=6，具体差额深入。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-04786`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04786v1) §4.1–4.3/Eq3–8、§5/Table1–4、§7与有关AppA/B2–4。采用segment-cache与下一视图density分责，不把O(miss)render当全部Stack/encode成本或恒定memory。ALFWorld/Search、Qwen2.5-VL3B/7B、2/4H100及不同text/optical caps限制；text质量反侧、K1/K5成功率反侧、render168.77ms非E2E、cache增长保留；正文trainingiterations与Alg t envstep不一致，不授K5配方。precision/concurrency/SLO未充分披露，字体/layout未测。root窄写；jan10_books_audit实际必要源、正文/完整局部邻接与末注独立POST通过，未复现。

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

- `SF-2026-OPENAI-INHOUSE-DATA-AGENT` — Daily `2026-01-30`补漏；[官方Jan29工程说明](https://openai.com/index/inside-our-in-house-data-agent/)六层Context/Runtime Context、Evaluation/Security。2+2+2=6，producer-derived语义与live observation/user-confirm Memory差额定点深入；只采公开workflow，未采用controlled效率、安全认证或prompt普遍经验。未运行内部实现/复现实验；root必要Source与实际owner PRE通过，root非作者实际正文/完整邻接及末注POST通过，窄锁释放；日级独立验收见对应Daily。

- `SF-2026-ARXIV-2603-18620` — [LSE exact-v1](https://arxiv.org/html/2603.18620v1)必要§3/Eqs1–10/Algorithm1、§4/Tables1–3/§5限制及AppA/T4；仅中间context edit训练状态、已知null-edit参照与多轮选择分责。保gold可得、baseline期望不变/方差非保证、单步非长期最优、UCB初始边界不采、D50/八次/25round择优非独立test、跨editor非跨执行器全胜、逐项反退及全费；不采通用selfevolution、免遗忘/安全或生产保证，未核全prompt/代码/复现。

- `SF-2026-ARXIV-2603-24558` — [LensWalk exact-v1](https://arxiv.org/html/2603.24558v1)§3–4、B.3、C.1/T6–8。仅时间scope/FPS/framebudget与rawvideo重读分责；保弱Reasoner反退、单次更快/DVD精度反侧/索引摊费，peakcontext非总SLO。未核图像/代码或复现，不采全局无误纠错/统一预算因果。

- `SF-2026-ARXIV-2603-27490` — [AgentSwing exact-v1](https://arxiv.org/html/2603.27490v1) §2.1/§3、§4.1/§4.3/T2–3及§7；仅部署候选view的有限tool-feedback后选择时点。保K3/K5反側、chain-rule非新机制、finished人口/弃branch和summary/API/tool全费，以及external effect不可随discard撤销；不授router正确性、全人口省费或通用K/SLO，未核artifact/复现。

- `SF-2026-ARXIV-2603-29919` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29919v1)IV-A/B/Alg1–2、V-A–C/TIII–V，2+1+2=5，仅shadow模拟→real trigger子集/最多三restore/原文fallback与body-ref功能分验。保536含39fallback/排64原fail、Stage2 best<1、14%反退、同50预算.909<.921及全部制备/路由/读取/验证费，不授任意query/完整faithfulness；未核代码/复现。

- `SF-2026-ARXIV-2604-09212` — Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.09212v1)§2.1/2.2/3.4T3/3.5T4/5与AppL，2+1+2=5具体gap深入；只采用canonical absolute speaker→deterministic per-agent view。保DS p=.460、two-agent/cap20/temp0、probe非人格真值与echo人口口径争议；不授allpartners同authority、多Agent已实测、零echo/安全。reader必要Source/逐字PRE及实际正文/完整邻接/本人注POST通过，作者仅同步此注并实读回；未核实现/复现。

- `SF-2025-ZAI-GLM47-THINKING` — Daily2025-12-23补Dec22；[官方发布日](https://docs.z.ai/release-notes/new-released)、[原官方Blog](https://z.ai/blog/glm-4.7)既有本日core与[当前Thinking Mode](https://docs.z.ai/guides/capabilities/thinking-mode)必要域分责。2+1+2=5，retention/turn compute接口差额深入；current recipe/default不倒填2025，整体bench/配置不授保留trace的独立因果、净省费或cache保证。未核运行实现/复现；Newton8实际Source/score/owner/PRE通过，root本日ROOT_REVIEW§1窄许可后作者实际保存/self-read，Newton10实际完整正文/两侧/本人note非writer POST通过，root§2已实际读回接纳并释放窄位；仅同步这些已发生事实，非日级DAY。

- `SF-2026-ARXIV-2604-22046` — Daily2026-04-28补Apr27；2+1+2=5，v1§3.2～3.4/4.1/4.2.2～4.3，callchain/constructor依赖closure具体差额深入；depth≤3/Qwen3Coder30B/RTX6000Ada/10gen+3fix与同timebudget反侧，precisiondefault未具体披露，不授路径可执行/coverage即bugtruth。reader必要Source/date/实际owner/逐字PRE通过，root授本两段+本人注窄lease，reader非writer实际正文/完整两侧/本人注POST通过，root接纳释放窄lease；作者仅行政同步本注并实际读回；未核实现/复现，不授DAY。

- `SF-2026-ARXIV-2605-04304` — Daily2026-05-08补May07；[exact-v1](https://arxiv.org/html/2605.04304v1) §2–4/Limitations；PeakTok非总费、简单任务反侧、crop/skill/摘要遗漏与额外call/latency。6分，具体owner差额深入，仅采正文受限接口；未核实现或复现。

- `SF-2026-ARXIV-2605-13527` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13527v1)§2/3/5/AppC必要域，2+2+2=6。仅采state-card/multiview选择与临时branch→结构化G的当前咨询接口；保错误grounding/覆盖/生成、main自主选择、GUI20step及缺跑配置/全费，不授分支安全隔离、历史图坐标、通用迁移或净费保证，未核artifact/复现。

- `SF-2025-ARXIV-2508-21547` — Godel，Daily2025-09-02补Sep01；[exact-v1](https://arxiv.org/html/2508.21547v1)§3–8/Alg1/Tables1–6必要Source，2+1+2=5。仅逐次重评/同proxy可行删减与reference/独立holdout分责；源两推荐model非LLM实测，保局部非全局最小/非跨metric每user保证、fullhistory代理/调用次数非全费，不采法规/隐私或业务效果。Context用途/验收与退路为项目推导/原理复用，未核像素/代码或复现。Newton41实际必要Source/具体owner/本逐字PRE通过，root协调09222完整第二段inline后/router首段前一段/独立marker/本人注；已按稿保存，Newton42一次真实完整新增/直接两侧/本人注POST通过，指定窄位即时生效释放；不预整日DAY。

- `SF-2025-ARXIV-2509-02093` — Noether，Daily2025-09-04补Sep3；[exact-v1](https://arxiv.org/html/2509.02093v1) III-B/C与IV-A/C/V旧必要层，Ohm37补II/III-A/D/完整IV/TableII/V，2+1+2=5。仅exemplar分层/多轴选择与consumer身份，保prompt/response混用未闭、同源judge、top3混杂/k反退和全费用，不采精确改善或中层必防过拟合，未核代码/图像/运行对象或复现。Ohm§42真实必要Source/正式评分/具体owner与逐字PRE通过，root仅协调完整排序段后/共享speaker身份首段前本单段/独立marker/本人注；已实际保存并经Ohm§46一次真实完整新增/完整直接两侧/本人注POST通过，本指定窄位即时生效释放；不预整日DAY。

- `SF-2025-ARXIV-2508-21433` — Godel，Daily2025-09-02补Sep01；[exact-v1](https://arxiv.org/html/2508.21433v1)§3–6/A/B/C/Tables1–4必要Source，2+2+2=6，仅observation视图/后续轨迹/费用consumer分责。保SWE限定、thinking反退、未显著非等效、API估价非本地实耗/全部费、增长与假说边界，不授普效/无损或生产SLO。原文回读/证据权限是项目推导；未核全D/E/图像素/代码或复现，不回投v3新增OpenHands/hybrid。Newton43实际必要Source/具体owner/本逐字PRE通过，root协调Compression完整公式fence/目标非最短段后、leave-one-out前一段/独立marker/本人注；已按稿保存，Newton48一次真实完整新增/直接两侧/本人注语义POST通过，指定窄位生效释放；本人新增EOF空行已最小修正，不预整日DAY。
- `SF-2026-ANTHROPIC-OPUS-4-8` — Daily2026-05-29补May28；官方news Messages API system-entry核心/具体owner见SUP_SOURCES A14，root实际独核通过并授trustclass末句后/Observability前一段＋本人注。作者真实保存、完整新增/直接两侧顺读，root已实际完整新增/直接两侧/本人注唯一POST通过，窄位释放，不预DAY；不采用未独核卡摘要精确OSWorld数字、营销性能、SDK或backend实现保证。

- `SF-2025-ARXIV-2509-06436` — Darwin，Daily2025-09-10补Sep9；exact-v1 §3–6/T2–4、Limitations与A–G必要域（G含完整文字例），2+1+2=5。仅跨chunk读取顺序分叉/语义状态前缀复用与utility剪枝接口，保摘要支持/误剪/非KV与None非truth、T2任务反退和全费，不授完整recipe/无损剪枝/positionbias消除或净效率；未核图像像素/代码、模型运行或复现。
- `SF-2026-ARXIV-2610-25550` — Daily2026-10-21补Oct20；oct21_resume_reader R172必要Source/actual owner/完整PRE原样通过，root具名授本精确单段+本人注。作者已真实保存并完整自读新增/完整直接两侧及本人注，reader R177唯一非writer actualPOST已通过，窄位生效释放；仅行政同步既成事实，不第三核。未核代码/复现，不授DAY。

- `SF-2025-ARXIV-2510-08907` — Daily2025-10-14补Oct13；writer exact-v1§3–5/AppA/T1–6必要，Planck R53关键核，2+2+2=6，原token-anchor/bidirectional层KV与LM/QA训练消费gap深入。保冻结target/LoRA128、分块510/5–51x、AE人口不同/各cell反退和全费；不采任意reader/无损或AE普遍无用。未核代码/复现，整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

- `SF-2025-ARXIV-2510-11967` — Herschel，Daily2025-10-16补Oct15；消费Cicero R35 exact-v1 §2.2–2.3/3.1–3.3/4.1/4.3/4.5.2–3首次必要，2+2+2=6，仅shared-prefix branch/return摘要/KV回滚消费差额深入。保主支交替非nested/parallel、FoldGRPO全轨迹/penalty与prompt-return judge非全trace、32K×10峰值/累计分账、工具96.5对49.5及main-only训练time/全费，不授执行撤销/充分摘要或净速。未第二Methods/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。
