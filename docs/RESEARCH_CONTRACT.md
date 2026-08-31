# 研究合同

版本：V2.1
生效日期：2026-08-25

## 1. 目的

本合同定义 Daily、Sunday Weekly 与 Historical Weekly 共用的研究生命周期。目标不是扩大新闻数量，而是让每个长期结论都能回答：候选从哪里来、为何归入这个时间窗口、读到了什么证据、证据没有证明什么，以及它是否改变现有知识树。

统一流程只有一条：

```text
确定窗口
→ 执行到期来源并保存 Coverage Receipt
→ 冻结 Source Family 候选分母
→ 校正日期、revision、spillback 与重复关系
→ 按路由完成 Source Review
→ 记录可审计的 Review Completion Receipt
→ 写入 Report
→ 执行 Deep Analysis Selection
→ 作出 Books Comparison 与 Decision
→ 由 fresh-context reviewer 完成 Semantic Audit
```

来源入口由 [RESEARCH_SOURCES.md](./RESEARCH_SOURCES.md) 维护；三类 Report 的归档时钟、表结构和完成条件由 [REPORT_CONTRACTS.md](./REPORT_CONTRACTS.md) 维护。本文件不重复维护具体机构名单或 Report 模板。

## 2. 五个正交对象

研究系统必须把下列对象分开。任何一个字段都不能代替另一个字段。

1. **Source Family Identity**：同一论文、release、artifact 与后续 revision 的稳定身份。
2. **Score V2**：候选值得投入多深的审阅成本。
3. **Supporting Evidence / Review / Access State**：哪些 Source ID 支撑结论、读到什么程度、材料是否可取得。
4. **Claim Scope**：证据允许支持哪些事实，禁止外推哪些事实。
5. **Integration Disposition**：结论是否进入长期 Books，以及由哪个 Stable Knowledge Node 拥有。

“高分”“来源权威”“全文已读”“可以进入 Books”是四个不同判断。不得把它们压缩成一个单值 `Evidence Level` 或总分。候选通过 `Supporting Source IDs` 关联注册表，再由各 Source ID 的 Authority Role 和 Allowed Claim Scope 派生证据边界。

## 3. Source Family 与事件归属

稳定 family 身份使用：

```text
Source Family ID
+ canonical primary identifier set
```

单次事件身份使用：

```text
Source Family ID
+ event kind / version
+ first-public date
```

- 同一论文的 v1、revision、正式发表、作者项目页和代码发布共享一个 Source Family，但可以形成不同 event node。
- 论文通常以 arXiv v1 或可核验的首次公开正文日期归周；正式发表日不会覆盖更早的公开日期。
- release、RFC、model/system card 和代码 artifact 按各自首次公开日期记录，并声明它们在 family 中承担的证据角色。
- discovery feed 的推荐日、索引收录日和搜索发现日不能代替事件日期。
- 同一 Source Family 在一份 Report 的候选分母中只能出现一次。Daily 先跨历史记录去重，再以 canonical primary
  event 的 first-public time 判断是否进入本轮窗口；HF、搜索索引或其他 discovery feed 的推荐日不能改变归属。
- feed 在本轮首次暴露、但 primary event 属于更早窗口的 family，只建立 delayed-discovery recovery 通知，不进入
  当前 Daily 候选分母，也不阻塞当前 Daily Gate。它不是零分或静默忽略：恢复任务必须重开真实 owner Report，并在
  owner 中完成 Score V2、Source Review、Books Decision 与必要的 Weekly reconciliation。
- 后续 Daily 再次命中同一 family 且没有重要 revision 时只记录 duplicate/reconciliation，不重复评分；Sunday Weekly
  可以基于七日证据重新评分，Historical Weekly 仍只在真实 owner week 建立周级评分。
- 后续 Daily 遇到重要 revision 时，使用 `Candidate State = revision` 和
  `Reconciliation = same_window_revision`：不成为第二个评分 owner，但必须以
  `important_revision` 重跑 Deep Review、Selection 和 Books Decision，并指向原 owner Report。
- 标题、品牌名和 URL 可以变化，不能单独作为身份键。
- 日期校正只改变 event identity 与 owner week，不创建新的 Source Family。

跨事件关系只使用以下五类：

- `Direct Evolution`
- `Layering / Dependency`
- `Principle Reuse`
- `Explanatory Analogy`
- `Alternative Branch`

关系的语义以 [LEARNING_PHILOSOPHY.md](./LEARNING_PHILOSOPHY.md) 为准。

## 4. Coverage 与候选分母

### 4.1 Coverage Receipt

每个到期来源都必须留下 Coverage Receipt，至少包含：

```text
Source ID
覆盖窗口
使用的 endpoint、venue 或 topic filter
pagination / cursor / query closure
命中数量
候选 Source Family
不可访问项或限制 ID
完成状态
```

Coverage Receipt 还必须保存带时区的实际执行时间、真实检索窗口、listing / release
watermark 与可复算的 closure evidence。状态只表示以下含义：

- `checked`：窗口已闭合且存在命中；
- `no_hit`：窗口已闭合但没有命中；
- `incomplete`：已执行普通扫描，但 cursor、watermark、snapshot 或分页证据未闭合；这是
  ordinary pending，不是 `checked`，也不是 external failure；
- `failed`：已精确识别外部访问失败，并绑定 Gap / Limitation 与材料请求；
- `not_due`：当前窗口未到期的 Periodic / Event / Backstop 来源。

`incomplete` 与 `failed` 不得互换，也不得用口头“已检查”代替 closure evidence。它们对
Report-level Gate 的影响只由 [REPORT_CONTRACTS.md §8](./REPORT_CONTRACTS.md#8-gate-与完成条件)
维护。

非确定排序的 Google Scholar、Semantic Scholar 等 Backstop 不参与确定性 Coverage closure 的算术；
它们不可访问时仍必须记录限制。

### 4.2 Candidate Denominator

候选分母先于审阅冻结。`已完成 Review 数 = 当前候选数` 只能说明“已入池候选处理完”，不能证明“扫描没有遗漏”。冻结前必须完成：

```text
到期来源逐项闭合
→ endpoint / filter / pagination 收据完整
→ 同一来源内去重
→ 相邻分类与触发源补检
→ first-public / revision / spillback reconciliation
→ 生成当前 Report 唯一 family ledger
```

Coverage recall 与 Candidate admission 是两个不同阶段。全量枚举、Core Daily 逐项 title + abstract
语义筛选、关键词路由和相邻分类补检，只负责证明“看见并判断过”，不自动把命中项送入候选分母。只有至少
满足下列一项，family 才能进入 Candidate Ledger 并接受 Score V2：

- 明确改变或补全长期 AI System 机制；
- 改变 state、data 或 control ownership；
- 改变可复算的 evaluation / release contract；
- 改变 Platform、Training 或 Inference 的设计判断与成立边界；
- 用 primary evidence 修正 Books 的既有认知。

仅仅能映射 ROADMAP、属于 AI 研究、提供单领域方法或 benchmark、改善局部表示/模型指标、或出现
`agent / memory / world model / inference` 等术语，均不足以入池。此类 family 留在 Coverage screening
ledger，以 `pre-denominator closure` 逐项记录 identity、日期和 family-specific 理由；不接受 Score V2，
也不进入 Source Review。Score V2 只决定已经入池候选的审阅深度，绝不能反向承担候选筛选。

冻结前必须由 fresh-context reviewer 同时检查 proposed retained 的 false positive 和 pre-denominator
closures 的 false negative。审计不得只抽样，也不得以预设保留比例代替逐项判断。

Daily 冻结后若发现 canonical event time 仍落在本轮窗口的新 Source Family，重开当日分母并完成评分和对应
Review。若 primary first-public 属于更早窗口，只更新独立 delayed-discovery recovery ledger；当前 Daily 保留
发现来源、primary identity、真实 owner 与恢复状态，但候选分母和三个 Gate 不随之扩张。恢复执行时重开真实 owner
Report；不存在可复用旧 Review 时必须重新评分和审阅，存在可复用 provenance 时按 §11 校验后复用。
`earlier_owner_pending / earlier_owner_written_back` 仅为已有 V2.1 Report 的兼容解析值，新 Daily 不再生成。
Historical Weekly 的新增候选仍只重开真实 owner week。

## 5. Authority Role 与 Claim Scope

来源注册表为每个 Source ID 指定一个主要 Authority Role：

- `Creator Primary`：证明该机构公开的模型、机制、版本和 artifact；不能把未披露内容反推成内部事实。
- `Primary Manuscript`：承载作者公开的论文正文、版本与实验主张；作者实验仍受其 workload 与方法边界约束。
- `Review Authority`：证明 submission、review、decision、withdrawal 与公开审稿状态；评审意见本身不是已证实机制。
- `Independent Evaluator`：证明其 evaluation contract 与结果；不能证明被测模型内部机制。
- `Formal Publisher`：证明正式版本、venue、DOI 与 publication status。
- `Benchmark / Standard Owner`：证明规则、提交配置、标准文本和对应结果。
- `Artifact Provenance`：证明 commit、release、RFC、spec、代码路径和公开实现。
- `Analytical Dataset`：证明其数据方法与估算；估算必须保留 uncertainty，不能冒充厂商披露。
- `Discovery / Metadata`：只用于发现、身份、去重、引用和恢复；不能支持技术机制结论。

一个 Source Family 可以组合多个角色，例如作者论文提供机制、正式 proceedings 提供发表状态、repository 提供实现、独立机构提供 evaluation。组合证据不会自动扩大任何单一来源的允许范围。`Formal Publisher` 托管的作者 PDF 可以承载作者主张，但 publisher role 本身只证明正式版本与发表状态。

Report 中的每个重要 claim 必须明确归因：

- `官方事实`：creator、standard owner 或 artifact owner 明确公开的事实；
- `作者实验主张`：论文在特定 evaluation contract 下报告的结果；
- `独立评估`：Independent Evaluator 在其协议下得到的结果；
- `社区观点`：只作线索或争议背景，不能单独通过 Evidence Gate；
- `Agent 推断`：必须显式写为推断，并列出从哪些已核验事实推导而来。

## 6. Score V2：只决定审阅路由

当前 Report 去重后需要处理的每个有效候选使用三个维度，每项 `0～3`：

### 6.1 Design Delta

- `0`：没有可辨识的设计变化，或只是营销包装。
- `1`：局部实现变化，不改变现有设计判断。
- `2`：给出重要机制、边界或替代方案。
- `3`：改变既有设计结论、修正错误或建立新的演进节点。

### 6.2 System Reach

- `0`：与 AI System 无直接关系。
- `1`：影响单一组件或局部 workload。
- `2`：跨一个系统边界，影响 state、data flow、control flow 或 SLO。
- `3`：影响多个层级、生命周期阶段或平台 contract。

### 6.3 Durability

- `0`：短期产品、营销或无法复用的孤立事实。
- `1`：版本敏感，但对当前工程有记录价值。
- `2`：在一类稳定约束下可复用。
- `3`：揭示长期问题、第一性原理或清晰演进关系。

```text
Total = Design Delta + System Reach + Durability
范围 = 0～9
```

处置路由：

- `7～9`：Deep Source Review + Books Decision。
- `5～6`：保留候选并完成 Standard Source Review。
- `0～4`：完成 identity、日期、重复关系和最终 disposition 闭合；必要时可做更深审阅。

以下情况无论分数如何都强制 Deep Source Review：

- 修正现有错误；
- 改变 release 或 security contract；
- 与 Books 现有结论冲突；
- 全文证据确认补全一个可定位的长期知识缺口；
- 属于会改变机制解释或实验结论的重要 revision。

`Source Reliability` 不再参与分数，由 Supporting Source IDs、Authority Role 与 Claim Scope 表达；`Review Status`、`Access Status` 和 Books disposition 也不参与分数。

## 7. Review 合同

### 7.1 Closure Review（通常对应 0～4）

至少核验：

- 唯一身份与 primary identifier；
- first-public date 与 owner week；
- revision / duplicate / spillback；
- 三维评分；
- 最终 disposition 及其原因。

### 7.2 Standard Source Review（通常对应 5～6）

在 Closure Review 之上，至少核验：

- 原始问题与主要机制；
- 旧方案为何合理、发生了什么约束变化；
- evaluation contract 与关键 baseline；
- 证据证明什么、没有证明什么；
- trade-off、failure mode 与适用边界；
- 对应的系统问题与可能的 Stable Node owner；此时只定位知识树，不读取 Books 正文。

### 7.3 Deep Source Review（通常对应 7～9或强制路由）

在 Standard Review 之上，按来源实际公开范围阅读：

- Method、公式、状态所有权、control flow、data flow 与实现；
- 实验、ablation、sensitivity、overhead、Appendix 与 limitations；
- artifact、代码路径、release / RFC / commit；
- workload、model、hardware、precision、input/output length、batch、concurrency、SLO 与 evaluator；
- 相邻技术、旧方案共存边界和下一重压力；
- claim attribution、公开范围与未披露字段。

公开材料未披露的字段写 `Not Disclosed`。作者 benchmark 只能证明其绑定的实验合同，不能外推为普遍结论。

`Deep Source Review` 是所有被路由候选的证据包，不限制数量；`Deep Analysis` 是 Report 正文中用于重建技术演进的叙事单元。叙事容量由 Report 合同维护，不能拿它偷换成“只全文审入选项”。每个已完成 Review 都必须有可定位的 `Review Ref`。

### 7.4 Review Completion Receipt

`Review Status = *_complete` 不是作者自由声明。每个候选必须在 Report 的 Review Completion
Receipt 中占据唯一一行，并记录：

- 本次审阅使用的精确 primary evidence 版本；
- 本次实际用于 claim 的全部 evidence versions，按 Source ID 与精确 version / tag / DOI / commit 绑定；
- 由 review schema、family/event identity、实际审阅的 evidence versions、route、全部 locator、
  claim boundary 与有界 Review 正文内容共同冻结的 Review Provenance ID；
- 与路由相符的 Method / Identity、Evaluation、Limitations / Counterevidence 与 Artifact locator；
- 可回溯的 Claim Boundary Ref；
- 完成、外部受阻或确实无需审阅的结果。

locator 可以是章节、公式、图表、Appendix、commit、RFC 段落或 Report 中的稳定引用。
不适用或未公开字段必须写带原因的 `Not Required — ...` 或 `Not Disclosed — ...`。
“已读”“已检查”“见原文”或一段无 locator 的摘要都不是完成证据。合同不使用字数阈值：
验收对象是可追溯的证据位置和 claim boundary，不是文本长度。

### 7.5 Deep Analysis Selection

Deep Analysis Selection 分配的是长叙事容量，不是研究完成度。eligibility 的最小可复算单位是
Source Family，而不是作者事后命名的 analysis unit。以下 family 进入显式 eligibility pool：

- Score V2 `7～9`；
- 强制 Deep Review override；
- Evidence 阶段根据 `ROADMAP.md` 与候选 claim boundary 判断为 `potential_books_delta`；
- Evidence 阶段尚找不到稳定 owner、需要在 Books Comparison 中验证的 `potential_structural_gap`；
- 参与跨 family 日期、安全、release、证据或技术演进修正的 family。

`potential_books_delta / potential_structural_gap` 是读取 Books 正文前的候选信号，不是最终 Books
Disposition。若后续 Books Comparison 得到 `Integrate` 或 `Structural Candidate`，但该 family 没有对应的
pre-Books eligibility，必须重开 Selection，而不能用最终 disposition 反向伪造当时的选择依据。

Report 必须为每个 eligible family 恰好记录一行 `selected`、`subsumed` 或 `not_selected`，并给出可审计理由。
多个 family 只有在共享同一非重复演进链时才能使用同一 selected Analysis Unit ID；selected unit 最多三个。
“因为只能选三项”不是理由。选择优先级依次考虑：

1. 正确性、security / release contract、Books conflict 和重要 revision；
2. 是否改变长期系统设计或暴露结构缺口；
3. Design Delta、System Reach 和 Durability；
4. 是否能构成非重复的跨候选演进链；
5. 证据是否足以支持稳定叙事。

`subsumed` 必须通过结构字段指向一个实际 `selected` 的 Analysis Unit ID；`not_selected` 只表示没有进入
长叙事，不降低其 Source Review 或 Books Decision 责任。选择发生在 Books Comparison 之前，避免由最终
disposition 倒推 eligibility。

### 7.6 Review 与 Access 状态含义

`Review Status`：

- `deep_complete`
- `standard_complete`
- `closure_complete`
- `pending`
- `blocked`
- `not_required`

`Access Status`：

- `accessible`
- `partial`
- `blocked`
- `unverified`
- `disputed`

`blocked` 是 Review 的最终受阻状态，不是 ordinary `pending` 的别名。`partial` 也不会因为已读到摘要
就自动变成完成。但如果公开来源确认某字段未披露，在可追溯的 `Not Disclosed — reason`
界定下，`accessible + *_complete` 仍然成立。

`partial / blocked / unverified` 使用 `blocked` 时必须有精确 Materials Request。`disputed + *_complete`
必须在 Review Ref 与 Claim Boundary Ref 中并列冲突来源和不可判定边界；只在解决冲突需要外部材料时才进入
Materials Request。`blocked / unverified / disputed` 不能支持 `Integrate` 或
`No Change — Existing Coverage`。

Review / Access 组合如何限制 Evidence Gate、Coverage 收据如何限制 Coverage Gate，只由
[REPORT_CONTRACTS.md §8.1](./REPORT_CONTRACTS.md#81-唯一状态与-gate-真值表) 维护。不在 Research 合同
复制第二份映射。

## 8. Benchmark 合同

任何 vendor、作者或第三方性能数字都必须绑定：

```text
workload
model
hardware
precision / quantization
input length
output length
batch
concurrency
SLO
evaluator
```

缺少的字段写 `Not Disclosed`，而不是猜测。MLPerf、Arena、HELM、METR 或论文实验各自只在其 evaluation contract 内成立；不同 suite、版本、system、division 或 evaluator 的数字不得直接合并。

## 9. Books Gate 与目录外内容

Evidence Gate 只验收来源、身份、claim boundary 与 Review 完成度，不读取 Books 正文。候选通过 Evidence Gate 且可能改变长期知识后，Books Decision 才读取目标与相邻章节，检查现有覆盖、owner 冲突和叙事位置。

`Integrate`、`No Change — Existing Coverage` 与 `Structural Candidate` 必须进入 Books Comparison
Receipt。该收据必须并列目标 Stable Node、目标及相邻章节、现有中心命题、新证据的真实
delta、演进关系、证据边界和最终 Decision。它不是把评分或 Weekly 摘要复制到 Books，而是证明
新结论与现有知识之间的相同、冲突、补全或结构缺口。

`Integrate` 必须同时满足：

- `Review Status = deep_complete`；
- `Access Status = accessible`；
- `Review Ref` 可定位；
- Stable Node ID 可在 `ROADMAP.md` 解析；
- 目标及相邻章节已审阅，并留下 `Books Review Ref`；
- 结论达到长期知识门槛。

分数只负责初始审阅路由，不直接决定 Books。低分 correction、Books conflict 或已由全文证据确认的
long-term knowledge gap 若要进入 Books，必须通过 override 升级为 Deep Review。

每个 Source Family 必须获得一个最终 disposition：

- `Integrate`
- `No Change — Existing Coverage`
- `Structural Candidate`
- `Weekly Only — Context`
- `Version Fact / Mechanism Not Disclosed`
- `Blocked / Unverified`
- `Disputed`
- `Rejected — Low Durability / Out of Scope`

`Structural Candidate` 进入季度结构复核。它表示当前知识树确实缺少稳定 owner，因此 Candidate Ledger 的 `Stable Node ID` 必须写 `—`，并在叙事区记录建议的结构范围；它不表示应立即新建“前沿技术”章节。经济、社会、行业和产品事实如果不改变 AI System 设计 contract，使用 `Weekly Only — Context`；不能因为不在 Books 范围内而静默丢失，也不能强行写入不相关章节。

Source-Family Books eligibility 与 Report-level Books Gate 相互区分。年度 `Archive Completion` 是 Coverage、Evidence 与 Materials reconciliation 的派生状态，不是第四个平行 Gate。具体决策见 [DECISIONS.md](./DECISIONS.md) 的 ADR-007。

## 10. Semantic Audit 与 Gate

### 10.1 结构校验不等于语义验收

validator 只能确认 marker、字段、引用、枚举、唯一性和状态约束是否满足；它不能证明
来源已被正确理解、claim 与 locator 相符、Deep Analysis 选得最有价值，或 Books 比较没有曲解
现有结论。因此，“validator 通过”只能报告为“结构校验通过”，不得简写为
“研究已验收”或“证据全部通过”。

Report 必须另外保存 Semantic Audit Receipt，由没有参与该 Report 主要写作的
fresh-context reviewer 对以下 scope 给出可追溯的 reviewed refs、findings、resolution 和 status：

- `coverage`；
- `evidence`；
- `deep_analysis_selection`；
- `books`。

Semantic Audit 不用来追求绝对无误，而是强制区分“报告作者声明”与“独立复核后可接受”。
存在未解决 finding 时对应 scope 为 `open`；Historical Weekly 未获授权 Books Integration 时，
books scope 才可为 `not_applicable`。作者不得同时充当该 Report 的 semantic reviewer。

### 10.2 Gate

本系统只保留三个 Gate：

1. **Coverage Gate**：到期来源、收据、候选分母与日期去重是否闭合。
2. **Evidence Gate**：冻结分母中每个候选是否拥有与路由相符的 Review 或精确 unresolved disposition。
3. **Books Gate**：已完成证据的候选是否获得最终 integration disposition，并在需要时同步 Books。

三个 Gate 的允许值、Review / Access / Coverage 组合、Semantic Audit 上限、Books N/A 边界与
`Complete / Conditional / In Progress` 完成条件，只由
[REPORT_CONTRACTS.md §8](./REPORT_CONTRACTS.md#8-gate-与完成条件) 的唯一真值表维护。本合同不再保存第二份
状态映射；结构 validator 通过也不会自动改变任何 Gate。

不能再引入含义重叠的 `Discovery Denominator Gate`、`Discovery Recall Gate`、`Candidate Evidence Gate` 等平行名称。历史文字可以保留，但新记录统一映射到上述三个 Gate。

## 11. 历史兼容、Review 复用与 Source Delta Audit

- 旧 Weekly 的六维 `/30` 保留为 `Score V1 Legacy`，不机械重算。
- V2.1 contract 约束所有新生成或真实重开的 Report，并继续使用 `Score Schema: V2`。命令行对
  `--report` 使用 strict 模式：缺少 `Contract Version: V2.1` 或 `Score Schema: V2` 都必须失败。
  `--audit` 才允许 Score V1 Legacy 或缺少 V2.1 contract marker 的 earlier Score V2 Report 保持只读兼容；
  后者不因此获得 V2.1 semantic-complete 身份。
- 注册表的 `Effective Date` 表示该来源从何时进入固定合同，不反推此前所有周必然遗漏。
- 已完成周先做 Source Delta Audit：比较新增来源、现有 owner ledger、相邻周 spillback 与 revision/identity 变化。
- 只有出现新的 in-window Source Family、日期归属冲突、重要 revision 或无法证明原 denominator 时，才重开真实 owner week。
- 仅登记待检查 baseline、changed sources 与 continuation point 时，使用
  [Report 合同 §6](./REPORT_CONTRACTS.md#delta-audit-queue-notification-与-true-reopen) 的非权威
  `Delta Audit Queued`；它不改变旧 Report 的分母、Gate 或 Completion，也不构成 true reopen。真实重开
  的触发边界与 strict 要求只由该节维护。
- 历史 Review 只有在 provenance 完整时才可复用：Source Family identity、primary identifier、精确
  evidence version、路由所需 locator、claim boundary、Review Provenance ID、Prior Review Ref 和无重要 revision
  都必须可验证。
- “旧报告写过 Full Source Review”、相同标题、相同 URL 或一段旧摘要都不构成复用证据。
  任一 provenance 缺失时，重新审阅或保持 `Review Status = pending`；不得直接迁移完成状态。

Historical V2.1 contract 明确区分：

- `Coverage Mode = Full Replay`：未生成的历史周使用当前注册表完整执行；
- `Coverage Mode = Delta Audit`：已完成周只检查相对 baseline 的 Changed Source IDs 与受影响 families，
  当前 Receipt 不复制未变化来源；effective coverage / denominator 由 baseline effective state 加本轮 delta
  复算。保留旧 V1 或 earlier Score V2 正文和分数，不把整周隐式升级为当前 V2.1 完整来源集。

Delta Audit 必须记录 baseline report、previous denominator 或显式 legacy identity、changed Source IDs、
新 effective denominator 与冻结时间；没有真实差异时记录 `No Reopen`。

因此，来源补全不等于推倒历史全年重跑。

## 12. 质量与 Git Safety

每次运行至少检查：

- Source ID、Source Family、first-public date、owner week 与 revision 唯一性；
- Score V2 三项及 Total；
- Supporting Source IDs、Review、Access 与 Books 状态是否冲突；
- benchmark 合同是否完整；
- Report 与 Books owner/disposition 是否一致；
- Markdown 标题、表格、链接、代码围栏、日期与行尾空白；
- `git diff --check`、staged/unstaged diff 和工作树范围。

研究自动化不得 stage、commit、push、清理或回滚既有修改，除非用户明确授权。
