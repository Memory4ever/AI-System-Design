# 项目决策记录

## ADR-001：使用 GitHub 作为唯一事实来源

决策：

本项目不再使用 Word 作为主要内容源。

原因：

Markdown 和 Git 能够提供：

- 差异比较
- 历史记录
- 审阅
- 分支
- 协作

Word 可以作为发布产物生成。

---

## ADR-002：围绕问题而不是框架组织内容

决策：

vLLM、KServe 等框架不用于定义顶层知识架构。

原因：

框架会变化。

底层系统问题会持续存在。

例如，应采用：

推理调度（Inference Scheduling）
    ├── vLLM
    ├── SGLang
    └── 未来的系统

而不是：

vLLM
SGLang
KServe

---

## ADR-003：将书稿内容存放在 `books/` 下

后续状态：

`books/` 作为正文目录的决策继续有效；下文的六 Part 目录快照已被 ADR-008 的七 Part / 84 章结构取代。

决策：

所有生成的书稿内容都存放在 `books/` 下。

该目录按照路线图中的六个 Part 组织：

- `books/part-01-worldview`
- `books/part-02-model`
- `books/part-03-training-system`
- `books/part-04-inference-system`
- `books/part-05-ai-infrastructure`
- `books/part-06-agent`

每一章都作为独立的 Markdown 文件，存放在对应的 Part 目录中。

原因：

`ROADMAP.md` 应继续作为知识树、章节顺序和学习路线的唯一事实来源。

章节内容需要一个独立且稳定的位置，这样仓库才能从路线图逐步成长为书稿，同时避免把规划、状态和长篇正文混在同一个文件中。

---

## ADR-004：由第 62 章负责 Evaluation System

状态：

已接受

日期：

2026-07-27

后续状态：

Evaluation System 的稳定 owner 继续有效；ADR-008 迁移后，当前 owner 为 `PLATFORM-EVALUATION-SYSTEM` / Ch66，Ch62 是 legacy chapter。

背景：

全局知识树已经把 Evaluation 同时定义为能力产出的信号和在线控制环的信号。Data、Training、Model Registry、Observability、Production 与 Agent 相关章节各自包含局部评估问题，但没有任何章节负责稳定的端到端框架。

这导致以下问题在知识树中没有唯一 owner：

- 一项评估结论适用于什么对象和部署分布；
- evaluation dataset、scorer、environment 与系统版本如何共同形成可复现证据；
- offline、shadow、canary、online 与 human evaluation 如何相互补充；
- evaluator error、contamination、uncertainty、slice 与 feedback bias 如何约束结论；
- 证据如何转化为 promotion、rollback 或 investigation 决策。

决策：

第 62 章改为通用的 `Evaluation System` 章节。它负责第一性原理评估模型，以及连接 specification、dataset、execution、scoring、aggregation、decision 与 feedback 的平台契约。

MLflow 继续保留在第 62 章中，作为 experiment、model、dataset、trace、metric 与 artifact 证据的一种实现映射。它不定义质量的含义，也不被视为 Evaluation System 本身。

第 62 章具有以下明确边界：

- 各领域章节保留自身的局部指标和 failure mode；
- Model Registry 索引不可变身份、证据引用和 promotion state，但不定义评估语义；
- Observability 记录发生了什么，而 Evaluation 判断观察到的行为是否满足指定目标；
- release controller 把策略应用于评估证据，但不能在发布决策之后反向编造证据；
- Agent 章节保留组件级与 trajectory 级评估机制，同时复用第 62 章的证据与决策契约。

考虑过的备选方案：

1. 新增一个专门章节，并对第 63～80 章重新编号。拒绝：这会产生大范围机械变动，却不能改善概念边界。
2. 保留第 62 章作为 MLflow 产品章节，并把 Evaluation 分散在各领域章节中。拒绝：产品无法负责稳定的跨系统问题，反馈环也仍然不完整。
3. 把 Evaluation 附加到 Monitoring。拒绝：Monitoring 描述观察到的状态，而 Evaluation 将行为与目标进行比较，二者具有不同的 dataset、scorer、uncertainty 与 decision 语义。

影响：

- `ROADMAP.md` 将第 62 章命名为 `Evaluation System`。
- `books/part-05-ai-infrastructure/62-mlflow.md` 被 `62-evaluation-system.md` 取代。
- 跨章节引用统一指向第 62 章中的公共评估契约，同时保留各领域的局部评估细节。
- 全书继续保持 80 章，避免无关的重新编号。

---

## ADR-005：采用双轴知识树

状态：

已接受

日期：

2026-07-30

后续状态：

五条横轴、Memory/State 区分与关系分类继续有效；六 Part / 80 章以及拒绝第七 Part 的结构结论已被 ADR-008 取代。后续写作还将 `Alternative Branch` 作为第五种关系，用于表达不同约束下并存的设计分支。

背景：

现有六个 Part 按阅读顺序和主要问题的归属组织全书：

```text
Part I：
  世界观 / 坐标系

Part II～VI 生命周期：
  Model
  -> Training
  -> Inference
  -> Infrastructure
  -> Agent
```

这一顺序提供了一条连贯的端到端学习路线，但也可能遮蔽跨多个 Part 反复出现的约束。Compute、Memory、Communication、Scheduling 与 State 会以不同对象和时间尺度，出现在 Training、Inference、Platform 与 Agent 系统中。

曾考虑过一种完全围绕这些系统原语组织的替代目录。它可以让历史联系更加明显，却会把资源机制、生命周期阶段、runtime 层与产品案例放在同一层级；也会让 KV Cache、分布式通信和调度等主题在多个 Part 中重复出现。

决策：

保留六个 Part，继续作为唯一的顶层目录与章节顺序架构；新增五条横贯系统的观察轴：

- 计算（Compute）
- 内存（Memory）
- 通信（Communication）
- 调度（Scheduling）
- 状态（State）

`ROADMAP.md` 同时负责两个轴：

- 纵向阅读与归属轴为每一章分配一个主要问题 owner；Part I 是元层级坐标系，而不是生命周期中的执行阶段；
- 横向系统观察轴提供跨 Part 的主题阅读路线。

第 3 章中的生产、交付、控制和行动闭环四个视角，是系统职责视角，不构成第三套相互竞争的章节层级。

横向章节序列是主题阅读路线，不是在声称它们之间存在直接技术谱系。每一次跨 Part 交接都应明确属于演进、分层 / 依赖、原理复用还是类比。

即使 Memory 与 State 指向同一个章节，也仍然保留为两条独立观察轴：

- Memory 关注字节存放在哪里、占用多少容量，以及何时移动、保留或被驱逐。
- State 关注这些字节表示什么、由谁拥有、哪个版本有效，以及何时提交或恢复。

本书还区分四种历史联系：

1. 直接演进；
2. 分层或依赖；
3. 原理复用；
4. 解释性类比。

这样可以避免把相似约束误写成没有证据支持的直接谱系。例如，KV Cache 可以复用 cache 与 paging 原理，但不是 CPU Cache 的直接后代；NIXL 可以与 collective library 共存，但不是后者的下一版本。

以框架为重点的章节仍然可以作为有效的实现研究，但其标题与中心命题应先指出稳定的系统问题，再指出作为实现案例的框架。

考虑过的备选方案：

1. 用 Compute、Memory、Communication、Scheduling、Inference、Training 与 AI Runtime 取代现有六个 Part。拒绝：这些类别不处于同一抽象层，会割裂能力生命周期。
2. 新增第七个基础 Part，并对第 23～80 章重新编号。拒绝：稳定机制可以由现有章节负责，而重新编号会引发大范围机械变动，使引用变得脆弱。
3. 保留当前目录，但不提供横向导航。拒绝：这会让重要的系统演进路线继续隐含在各章之中，并鼓励逐框架阅读。

影响：

- 仓库继续保留六个 Part 目录和第 1～80 章。
- 第 3 章负责双轴全局地图。
- 第 9 章负责系统演进方法和关系分类。
- 第 32 章负责 Training 的分布式通信基础，并向后衔接 Inference 的状态传输。
- State 路线从第 19 章中 KV state 的起源开始，先经过第 71 章的单次调用 Context，再到第 73 章的持久化 Memory。
- Runtime 与 Infrastructure 产品章节以稳定问题命名，并把当前框架作为实现案例。
- 不会仅仅为了复制一份横向主题而新增章节；横向观察轴应指向现有的主要 owner。

---

## ADR-006：将面试证据与书稿、研究归档分离

状态：

已接受

日期：

2026-08-03

后续状态：

证据分层决策继续有效；下文“不构成第七个 Part”是当时的编号语境，当前含义是 `interview/` 不构成新的 Books Part。

背景：

仓库六个 Part 的书稿已经形成完整 Draft，`papers/` 负责按时间归档 primary-source
研究证据。面试准备会产生另一类材料，包括岗位矩阵、压缩答案、限时练习、项目故事、
Mock 反馈和投递就绪记录。这些材料的变化速度快于稳定章节，不应重新定义知识树。

决策：

- 稳定的解释性内容继续放在 `books/`，研究证据继续放在 `papers/`。
- 可执行 benchmark、profiling、故障注入和一体化 AI Platform Capstone 放在
  `labs/`。
- 16 周计划、逐周 Checklist、岗位矩阵、问题库、设计练习、项目故事和 Mock 记录
  放在 `interview/`。
- 只有当面试发现暴露了长期有效的知识缺口，并通过仓库正常的来源与写作门禁时，
  才将其沉淀到 `books/`。

影响：

- 面试准备可以针对知识提取速度和可测量的就绪程度优化，同时不会把 Book 变成题库。
- 性能和项目结论必须指向 `labs/` 中的可复现证据，或明确标注的既有生产证据。
- `ROADMAP.md` 继续作为知识树的唯一事实来源；`interview/` 不构成
  第七个 Part。

---

## ADR-007：分离 Source-Family Books Gate 与 Archive Completion Gate

状态：

已接受

日期：

2026-08-13

背景：

历史 Weekly 回填同时面对两类不同完成条件。第一类是某个 Source Family 的身份、版本、正文、方法、实验、limitations、artifact 与章节边界已经完成审计，足以判断长期机制。第二类是一个完整年度的 discovery replay、blocked source 恢复、revision 去重和材料清单全部闭合。若把两者绑成一个 Gate，少数不可访问材料会长期冻结已经可靠的知识；若完全取消 Archive Gate，又会把局部完成误写成年度无遗漏。

决策：

- Source Family 按候选级 Books eligibility 独立判断。只有 identity、first-public/revision、full-read coverage、claim boundary、owner 与相邻章节均完成，且状态不是 `Blocked`、`Disputed` 或仅有 `Version Fact`，才能进入 Books。
- `Archive Completion` 判断一个 Daily/Weekly/年度归档是否已经完成 discovery、去重、缺口恢复和材料账本。它是 Report-level Coverage / Evidence Gate 与 Materials reconciliation 的派生状态，不是第四个平行 Gate；保持 Open 不阻塞已经满足 eligibility 的 Source Family。
- Weekly 摘要和评分本身不构成 Books Gate；正文必须能回溯到 primary source review。
- 进入 Books 后，同步对应研究记录的 owner、current/legacy chapter、integration decision、changed files 与 open questions。
- Archive 仍 Open 时，任何状态汇总必须准确写明剩余 Blocked/Discovery Gap，不得宣称年度审计全部完成。

影响：

- 可靠机制能及时沉淀，而材料缺口继续可见。
- Books 的完成度不再等同 papers archive 的召回完备度。
- 需要维护 Source Family identity，避免同一论文、release 和后续 artifact 被重复吸收。

---

## ADR-008：新增 Part III、扩展至 84 章并引入 Stable Knowledge Node ID

状态：

已接受

日期：

2026-08-13

背景：

2026 研究审计表明，多模态表示、跨模态生成、World Model 与 Embodied/VLA 已形成连续知识链。继续把这些机制分散寄居在 Ch10、Data、Inference execution 或 Agent 章节，会混淆 representation、generation、environment state 与 action authority。另一方面，章节号已被大量 Weekly 引用；直接把编号当永久身份会让未来结构调整产生语义歧义。

决策：

- 在 Model 与 Training 之间新增 Part III：多模态、生成与世界模型。
- 新增 Ch23～26：多模态表示、生成范式、World Models、Embodied AI/VLA。
- 原 Ch23～80 顺延为 Ch27～84，形成七 Part / 84 章结构。
- 为全部章节引入 Stable Knowledge Node ID；ID 按长期问题域与冻结语义 slug 生成，不随阅读顺序变化。
- `ROADMAP.md` 同时维护 Node ID、current chapter、current path 与 legacy chapter。
- 历史 Weekly 的旧章节号不机械重写；年度索引提供 legacy mapping。以后研究记录优先写 Stable Node ID，并附 current/legacy chapter。
- AI for Science 保持 Data → Evaluation → Workflow → Security 的领域路线；compiler/kernel/hardware co-design 保持 Model/Training → inference execution → resource scheduling 路线，不新增独立 Part。

备选方案：

1. 保持 80 章，只在 Ch10 增写 World Model。拒绝：会让趋势章成为机制杂物篮子，无法承载 representation→action 的连续推导。
2. 使用 Ch22A～22D，避免重编号。拒绝：阅读顺序与文件路径会长期保留例外，难以形成清晰 Part 边界。
3. 为 AI for Science 或 hardware 单独建 Part。暂缓：目前证据显示它们是跨章节领域路线和横轴，而不是同一抽象层的纵向知识主干。

影响：

- ADR-005 中“保持六 Part / 80 章”和“拒绝第七 Part”的结构结论被本 ADR 取代；其五条横轴、Memory/State 区分与四种演进关系继续有效。
- Ch10 收缩为未来情景与 handoff；原 Training、Inference、Infrastructure、Agent 章节内容保留并顺延。
- 新研究首先定位 Stable Node ID，只有现有 owner 无法承载时才提出 Structural Candidate。

---

## ADR-009：统一 Research、Report 与 Books 合同

状态：

已接受

后续状态：

三份唯一合同、Score V2 三维量纲和三个 Gate 继续有效；V2 marker 只做小型结构校验、
validator 不读自由叙事的边界，由 ADR-010 进一步细化为 V2.1 可审计接口和独立语义验收。
当前 owner 边界也由 ADR-010 收紧：Research 合同维护 Coverage discovery / identity、Score、Review / Access
语义与 Books eligibility；Report 合同维护机器 schema、Semantic Audit 到 Gate 的映射和唯一完成状态真值表。
本 ADR 原有“身份、证据与 claim boundary 未变化即可复用 Full Review”的简写也由 ADR-010 的完整
Review provenance 条件取代；缺任一 provenance 字段时不得迁移完成状态。

日期：

2026-08-25

背景：

Daily 与 Historical Prompt 曾同时维护来源名单、六维评分、Evidence 术语、候选分母、Report 模板、Books Gate 与质量检查。相同规则在多处逐步漂移：来源入口被重复计数，`Evidence Level` 同时表达来源类型和阅读状态，六维分数混入来源可靠性与项目相关性，Historical Weekly 也出现多组含义重叠的 Gate。结果是 Prompt 越来越长，却仍可能因为分页或候选分母没有闭合而在重跑时出现大幅差异。

决策：

- `docs/RESEARCH_CONTRACT.md` 唯一定义 Source Family、Coverage、Score V2、Review 路由、Supporting Evidence / Access 状态和 Books eligibility。
- `docs/RESEARCH_SOURCES.md` 作为来源注册表，使用稳定 Source ID、Authority Role、Cadence、Claim Scope 与 Effective Date；机构名、URL 和 venue 不再充当来源身份。
- `docs/REPORT_CONTRACTS.md` 在本决策时唯一定义 Daily、Sunday Weekly 与 Historical Weekly 的归档时钟、
  必填字段和 V2 机器账本；其当前 V2.1 owner 范围以上述后续状态和 ADR-010 为准。
- Daily 与 Historical Prompt 降为轻量 Adapter，只保留各自的时间窗口、执行顺序和模式差异。
- Score V2 只包含 `Design Delta`、`System Reach`、`Durability` 三项，每项 0～3。分数只决定审阅深度，不决定来源可信度、完成状态或是否进入 Books。
- Source Reliability 不进入分数；候选通过 Supporting Source IDs 关联 Authority Role 与 Claim Scope。是否读完由 Review Status 表达；材料受阻由 Access Status 表达；是否进入 Books 由 Integration Disposition 表达。
- 公共流程只保留 Coverage、Evidence 与 Books 三个 Gate。旧名称在历史记录中可保留，但新记录必须映射到这三个 Gate。
- V2 Markdown 使用版本 marker 限定小型可判定表，validator 不解析自由叙事，也不猜测旧报告语义。

历史兼容：

- 旧六维 `/30` 作为 `Score V1 Legacy` 原样保留，不机械重算。
- 来源注册表以 `Effective Date` 生效；新增来源不会自动证明更早 Weekly 有遗漏。
- 已完成周先执行 Source Delta Audit。只有出现新的 in-window Source Family、first-public owner 冲突、重要 revision 或 denominator 证据不足时，才重开真实 owner week。
- 已完成且身份、证据和 claim boundary 未变化的 Full Source Review 继续有效。

影响：

- Prompt 不再复制来源、评分、状态机或 Report schema；后续变更只修改唯一 owner。
- Daily 必须先保存 Coverage Receipt 并冻结候选分母，避免初次扫描与重跑出现无法解释的候选差异。
- Historical Weekly 可以并行发现和阅读，但日期与 Source Family reconciliation 仍由单一写入者串行完成。
- 不属于当前 Books 结构但具有长期价值的候选进入 `Structural Candidate`；上下文事实进入 `Weekly Only — Context`，均不会静默丢失或被强行写入杂物章节。
- 本决策不触发历史 Weekly 全量重跑，也不授权历史 Books Integration。

---

## ADR-010：将结构合规与研究语义验收分离

状态：

已接受

日期：

2026-08-25

背景：

ADR-009 建立了统一来源、分母、三维评分和三个 Gate，但 V2 初版仍允许一个 Report
只凭 `deep_complete`、一段非空文本或“validator 通过”声明研究已完成。这会让以下不同
问题被压缩成相同的形式状态：

- 来源扫描已运行，但缺 cursor、watermark 或 snapshot；
- 候选已打分，但 Method、evaluation、limitations 和 artifact 没有可定位证据；
- 高价值 family 已完成 Source Review，但 Deep Analysis 的选择没有比较依据；
- Books Decision 已填写，但没有与现有章节命题及相邻章的真实比较；
- 旧 Historical Review 因为标题相同就被复用，却缺身份、版本、locator 或 claim boundary provenance。

决策：

- 公共合同升级为 V2.1；Score Schema 仍为 V2，`Design Delta / System Reach / Durability`
  的定义和 0～9 量纲不变。
- Source Coverage Receipt 增加实际窗口、Executed At、watermark 与 closure evidence，并增加
  `incomplete`，专门表达“已执行但普通闭合工作未完成”。它必然使 Coverage Gate
  保持 Open，不得伪装成 `checked` 或 external `failed`。
- Candidate Ledger 增加 Owner Report Ref、Prior Review Ref 与 Reconciliation。earlier-owner 使用
  `earlier_owner_pending → earlier_owner_written_back` 两阶段：pending 强制 Report 保持 In Progress、
  Evidence / Books Open；terminal 只有在 owner Report 能解析同一 family 与非 pending RP 后成立。
  `Prior Review Ref` 只有 `reused_unchanged` 强制填写，owner writeback 本身不伪装成旧 Review 复用。
- 重要 revision 使用独立 `revision` candidate state：不重复成为同层评分 owner，
  但 `important_revision` 强制重跑 Deep Review、Selection 和 Books Decision。`duplicate` 只保留给无重要变化的重复命中。
- 引入四个最小可审计接口：Review Completion Receipt、Deep Analysis Selection、Books
  Comparison 与 Semantic Audit。它们只固定证据引用和状态关系，不强迫所有候选使用相同长度
  或同一套叙事模板。
- Review Completion Receipt 增加全部 Reviewed Evidence Versions；Review Provenance ID 同时绑定
  evidence version 集合、四类 locator、claim ref 与规范化有界 Review 正文 digest。只冻结字段名或
  anchor、却允许证据正文静默变化，不构成 provenance。
- Deep Analysis eligibility 以 Source Family 为分母，每个 eligible family 恰好一行；selected unit
  最多三个，`subsumed` 必须结构化指向 selected unit。Books 相关 eligibility 使用 Selection 前的
  `potential_books_delta / potential_structural_gap`，不能由最终 disposition 反向构造。
- `Review Status = blocked` 表示路由已确定、可达工作已做完，但精确外部材料不可取；
  它不是 ordinary `pending` 的别名。`Conditional Pass` 只能由这类 external blocker 或已完成
  对读却无法唯一判定的 `disputed` 支持，且 ordinary pending 必须为零。
- validator 只验证 marker、字段、引用、枚举、唯一性和状态一致性，不得把命令通过解释为
  语义验收。Semantic Audit 必须由没有参与 Report 主要写作的 fresh-context reviewer 完成。
- Semantic Audit scope 到 Gate 的映射固定为：coverage → Coverage；evidence 与
  deep_analysis_selection → Evidence，并在 open 时连带 Books Open；books → Books。Books 的 final、
  conditional、Not Assessed disposition 由 Report 合同真值表聚合，不再依赖 prose 猜测。
- 历史 Review 只有在 family identity、primary identifier、evidence version、route-specific locators、
  claim boundary、Review Provenance ID、Prior Review Ref 和重要 revision 检查完整时才可复用；否则必须重新审阅或保持
  pending。
- Historical Full Replay 才直接执行全部 Required sources；Delta Audit 当前只保存 Changed Source IDs，
  effective coverage / denominator 由 baseline effective state 加本轮 delta 复算。Score V1 Legacy 与
  earlier Score V2 Report 都可只读 audit，但不会自动获得 V2.1 semantic-complete 身份。
- `Delta Audit Queued` 只是待办通知，不修改旧 contract、denominator、Gate、Completion 或任何 V2.1
  machine interface；旧 Gate 仅是 legacy denominator 的历史结果。写入 V2.1 packet、执行 changed-source
  reconciliation、改变当前状态或对扩大分母作 completeness claim 中的任一项，才构成 true reopen，并立即
  要求完整 V2.1 delta packet 与 strict `--report`。已执行并证明无影响的 `No Reopen` 也不是 queue notification。
- Daily 与 Historical Adapter 只保留模式差异和对稳定合同章节的引用，不复制评分、状态、
  Receipt 列或 Books Gate 规则。

备选方案：

1. 使用 Review 字数阈值或长模板保证质量。拒绝：长度可被模板化文本游戏，不能代替证据定位与 claim boundary。
2. 让 validator 直接判断自然语言真伪。拒绝：这会隐藏审阅主体和不可复算假设，也会把工具能力误写成证据。
3. 只修正当日 Report。拒绝：同一漏洞会在 Daily、Sunday Weekly 和 Historical Weekly 反复出现。

影响：

- 新生成或真实重开的 Report 使用 V2.1 最小接口，同时保持 `Score Schema = V2`。
- 旧 V1 / V2 Report 不机械重写；它们的 Review 完成状态也不会因旧文字存在而被默认迁移。
- 最终交付必须分别报告结构校验、Semantic Audit、未解决 findings 和工作树状态。
