# Report 合同

版本：V2.1
生效日期：2026-08-25

## 1. 共同原则

Daily、Sunday Weekly 与 Historical Weekly 使用同一 [研究合同](./RESEARCH_CONTRACT.md) 和 [来源注册表](./RESEARCH_SOURCES.md)，但承担不同的时间责任：

```text
Daily
  及时发现并完成当日证据闭环

Sunday Weekly
  聚合七天收据，补齐 Weekly 来源，并重建跨日演进

Historical Weekly
  直接重放完整历史周，不补造历史 Daily
```

三类 Report 都先保存 Coverage Receipt，再冻结候选分母。任何“Complete”声明都必须同时可复算 Coverage、Evidence 与 Books 三个 Gate。

## 2. 归档时钟

时区统一使用 `Asia/Shanghai`。

### Daily

- 每次 Live 运行都创建或幂等更新当前自然日：`papers/YYYY/MM/DD/README.md`。
- 即使没有重要候选，也写 `No Material Update Daily`，说明实际覆盖、证据边界和 Sources。
- 默认研究窗口由 Daily Adapter 明确给出，并保存实际 source/listing watermark。Daily 主候选分母与评分责任由
  canonical primary event 的 first-public time 是否落入该实际窗口决定。discovery feed 在本轮首次暴露的更早
  family 进入独立 delayed-discovery recovery ledger，不进入当前分母，也不阻塞当前 Gate；真正的评分、Review 与
  Books Decision 在真实 owner Report 的恢复任务中完成。

### Sunday Weekly

- Monday～Saturday 不生成当前周 provisional Weekly。
- Sunday 必须先完成当日 Daily 与必要的 Books Decision，再生成当前完整 ISO week：

```text
papers/<ISO-week-year>/weekly/<ISO-week-year>-W<week-number>/README.md
```

- Coverage Window 必须是 Monday～Sunday 七天，不能因月末、季度末、年末或回填批次截断。
- Daily 缺失或 primary source 无法核验时，在 Coverage Limitations 中明确列出。

### Historical Weekly

- 只生成完整 ISO Monday～Sunday Weekly，不创建历史 Daily。
- 论文按 v1 / first-public date，release、RFC、artifact 按各自首次公开日期归周。
- 允许并行 discovery 和 Source Packet 阅读，但只能由一个 reconciliation / write owner 决定 owner week 并写入 Weekly 与年度索引。

## 3. V2.1 最小可审计接口

自然语言正文可以按问题和证据需要组织；下列带版本 marker 的 Markdown 表是最小稳定接口，
不是另一套写作模板。所有新生成或真实重开的 Report 必须声明 `Contract Version: V2.1`
与 `Score Schema: V2`；合同版本升级没有改变三维评分量纲。只有通过兼容性 `--audit` 读取时，
Score V1 Legacy 与缺少 V2.1 contract marker 的 earlier Score V2 Report 才能保持只读历史身份。

这些接口使 validator 能发现缺表、缺引用和状态冲突，但不能替代 fresh-context Semantic
Audit。完成交付时必须分开报告“结构校验”与“语义验收”。

### 3.1 Report Metadata

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | `V2.1` |
| Score Schema | `V2` |
| Report Type | `Daily`、`Sunday Weekly` 或 `Historical Weekly` |
| Window Start | `YYYY-MM-DD` |
| Window End | `YYYY-MM-DD` |
| Registry Version | 来源注册表版本日期 |
| Coverage Mode | `Full Replay` 或 `Delta Audit` |
| Baseline Report | Full Replay 写 `—`；Delta Audit 写 baseline 路径 |
| Changed Source IDs | Full Replay 写 `—`；Delta Audit 写本轮来源差集 |
| Previous Denominator ID | Full Replay 写 `—`；Delta Audit 写 baseline 冻结分母 ID；无该字段的 legacy / earlier V2 baseline 使用显式 legacy identity |
| Denominator ID | 本次冻结分母的唯一 ID |
| Denominator Frozen At | 带时区的 ISO 8601 时间 |
| Completion Status | `Complete`、`Conditional` 或 `In Progress` |
| Coverage Gate | `Closed`、`Conditional Pass` 或 `Open` |
| Evidence Gate | `Passed`、`Conditional Pass` 或 `Open` |
| Books Gate | `Passed`、`Conditional Pass`、`Open` 或 `Not Applicable` |

Weekly 的窗口必须由 Monday 开始、Sunday 结束。Daily 的开始和结束表示归档自然日，必须相同；实际 24～48 小时
检索范围、listing watermark 和 cursor 写入 Coverage Receipt。Daily 与 Sunday Weekly 只能使用 Full Replay；
Historical Weekly 才能执行 Delta Audit。Delta Audit 的 `Previous Denominator ID` 必须能解析到 baseline；
若 baseline 没有冻结分母字段，使用 `legacy:<repo-relative-path>@sha256:<baseline-file-sha256>` 作为可复算身份。
本轮 `Denominator ID` 必须是应用 delta 后重新冻结的新身份，不能与 previous identity 相同。

### 3.2 Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SRC-EXAMPLE` | 带时区 ISO 8601 | 带时区 ISO 8601 | 带时区 ISO 8601 | 实际 endpoint、venue、category 或 query | `checked`、`no_hit`、`incomplete`、`failed` 或 `not_due` | 非负整数 | family ID；没有则写 `—` | page/cursor/query closure | listing / release / API watermark | 可复算 snapshot、最后页或封闭查询引用 | 没有则写 `—` |

规则：

- Daily 至少覆盖所有到期 `Required Daily` 来源。
- Sunday Weekly 与 Historical `Full Replay` 至少覆盖 `Required Daily + Required Weekly`。
- Live Daily、Sunday Weekly 与用户明确重建的历史 Daily 以 `Window End` 和来源 `Effective Date` 计算到期来源；后来加入注册表的来源不反推为更早 Daily 的 Required。新生成的 Historical Weekly 属于当前合同 Full Replay，仍执行当前注册表的 Required Daily + Required Weekly。
- Historical `Delta Audit` 的当前 Receipt 只执行 Changed Source IDs；其 effective coverage 是可解析 baseline
  的 effective receipts 加上本轮 changed-source receipts。新增到期来源必须进入 Changed Source IDs，不能仅因
  baseline 不含它而略过。
- Sunday Weekly 可以引用七份 Daily receipt，但必须在 Weekly 中形成可复算汇总，并补齐 Required Weekly。
- `incomplete` 表示已执行但缺 cursor、watermark、snapshot 或其他 closure evidence；它是 ordinary
  pending，Coverage Gate 必须为 `Open`，不得写成 `checked` 或 `failed`。
- `failed` 必须绑定 Gap / Limitation ID 与对应 Materials Request；如果该来源是可枚举或可冻结
  查询，Coverage Gate 最高为 `Conditional Pass`。明确标记为 `Non-deterministic backstop`
  的 discovery 来源仍须留下失败收据，但不参与 Closed 算术。
- Required source 不能写 `not_due`。
- Event Trigger、Periodic 与 Backstop 只有在当前窗口未触发时才能写 `not_due`；此时 `Endpoint / Filter` 必须记录本轮实际检查的 trigger、venue season、release feed 或版本条件，`Hits = 0` 且 family 写 `—`。不能用空泛的“未触发”代替触发条件检查；触发后按正常来源闭合。
- `no_hit` 必须同时满足 `Hits = 0` 且 family 为空；`checked` 必须至少有一个命中和一个 family。
- `checked / no_hit` 的 Executed At、Window Watermark 和 Closure Evidence 不得为空，也不得使用
  “已检查”、“已完成”等无法复算的占位语。
- Full Replay 中 Receipt family 并集必须与 Candidate Ledger family 集合相等。Delta Audit 中本轮
  changed-source Receipt family 并集必须与本轮受影响 Candidate Ledger family 集合相等；effective denominator
  则由 baseline denominator 应用本轮新增、替换、日期 / revision reconciliation 后得到。每个本轮候选的
  Supporting Source IDs 必须指向实际列出该 family 的当前 Receipt，或通过 baseline ref 指向继承的 receipt。

### 3.3 Candidate Ledger / Score V2

本表只承载已经通过 `RESEARCH_CONTRACT.md §4.2` admission 的候选及其同层级 closure 动作。Coverage
screening ledger 中的 `pre-denominator closure` 不得复制进本表，不打 Score V2，也不计入 Candidate
Denominator。`closure_only` 是“已入池后经评分与审阅得到关闭处置”，不是 title/abstract 阶段的拒绝项。
权威来源已标记 `withdrawn / removed` 的 revision 必须在 screening 阶段用
`withdrawn_primary_source` 闭合；Candidate Ledger、Source Review、Deep Analysis、Books Decision 与
Materials Request 中不得继续保留该 revision。撤回状态本身只出现在 Coverage receipt / screening closure，
用于解释 raw identity 为什么没有进入 denominator。

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SF-EXAMPLE` | `arXiv:2608.00001` | `paper-v1` | `2026-W35` | `YYYY-MM-DD` | `SRC-ARXIV` | `0～3` | `0～3` | `0～3` | `0～9` | `retained` | `deep_complete` | `accessible` | `none` | `review:SF-EXAMPLE` | `self` | `—` | `new_in_window` | `INFER-...` | `No Change — Existing Coverage` | `books-review:SF-EXAMPLE` | `no` |

枚举：

- `Candidate State`：`retained / closure_only / revision / duplicate / spillback / out_of_scope`。`closure_only` 描述本轮动作，
  不表示分数直接决定是否收录。Daily 中 canonical event time 落入实际窗口的新 family 使用 `retained` 或
  `closure_only`；Daily 不得使用 `spillback` 跳过窗口内评分。更早 primary event 的 delayed discovery 不进入当前
  Candidate Ledger，而进入独立 recovery ledger；`spillback` 只用于 Weekly/Historical 的跨周对账关系。
- `Review Status`：`deep_complete / standard_complete / closure_complete / pending / blocked / not_required`。
- `Access Status`：`accessible / partial / blocked / unverified / disputed`。
- `Review Override`：`none / correction / release_security_contract / books_conflict / knowledge_gap / important_revision`。
  `knowledge_gap` 只能在全文证据已经定位现有 Stable Node 中缺失的长期机制、且 Books Comparison 明确给出
  owner、相邻章和 delta 时使用；它不能由“可能值得写入”或最终 `Integrate` 反向补造。
- `Books Disposition` 使用 [RESEARCH_CONTRACT.md](./RESEARCH_CONTRACT.md) 定义的八种最终处置；未到 Books 判断时可以暂写 `Not Assessed`，但 Books Gate 不能通过。
- `Structural Candidate` 表示当前没有可解析的稳定 owner，`Stable Node ID` 必须写 `—`；建议的新结构只在叙事区描述，不能伪装成已存在节点。
- `Review Ref` 使用 `review:<Family ID>`，正文使用唯一的
  `<!-- review:<Family ID>:start --> ... <!-- review:<Family ID>:end -->` 有界区间；对应
  `Claim Boundary Ref` 必须位于该区间内部。已完成 Review 不能只改状态或只放 anchor 而没有证据包。
- `Books Review Ref` 使用 `books-review:<Family ID>`，正文使用唯一的
  `<!-- books-review:<Family ID>:start --> ... <!-- books-review:<Family ID>:end -->` 有界区间。
  `Integrate`、`No Change — Existing Coverage` 与 `Structural Candidate` 都必须留下实际审阅过的
  owner 候选、目标及相邻章节证据，不能借 disposition 跳过比较。
- `Reconciliation`：`new_in_window / earlier_owner_pending / earlier_owner_written_back /
  same_window_revision / reused_unchanged / spillback_reference / out_of_scope`。
- `Owner Report Ref` 使用 `self` 或 repo-relative Report path。`new_in_window` 使用 `self`；
  `earlier_owner_pending / earlier_owner_written_back / reused_unchanged / spillback_reference` 必须指向
  concrete owner Report。
- `earlier_owner_pending / earlier_owner_written_back` 仅用于兼容已经生成的 V2.1 Report；新 Daily 不再生成这两个值。
  新发现的更早 family 由 delayed-discovery recovery ledger 路由到真实 owner Report，不能借发现日进入当前分母。
- `reused_unchanged` 是唯一强制 `Prior Review Ref` 的状态；该值必须是 Owner Report Ref 中同一 family 的
  Review Provenance ID。`same_window_revision` 必须按 revision 重新路由 Review，不得借 prior RP 继承完成状态。
- `same_window_revision` 必须与 `Candidate State = revision` 及
  `Review Override = important_revision` 配对，指向原 owner Report，并重新生成
  绑定 revision evidence versions 的 RP。
- `spillback_reference` 只用于 Weekly / Historical 的发现周关系，Owner Report Ref 必须解析到 owner family
  与非 pending RP；它不承担本周评分 owner。
- `out_of_scope` 必须与 `Candidate State = out_of_scope` 配对。

`retained / closure_only` 必须填写三维分数。`revision / duplicate / spillback / out_of_scope` 行的四个分数字段写 `—`。
其中 `duplicate` 表示同一 Daily 序列已经处理且没有重要 revision。Daily 与 Sunday Weekly 是两个审阅层级，
可以分别评分；同层级不能重复成为评分 owner。迟到发现的历史 family 只在真实 owner Report 成为评分 owner。
`revision` 不重复评分，但因 `important_revision` 强制 Deep Review，且必须重做
Deep Analysis eligibility 与 Books Decision。
已有 `earlier_owner_pending / earlier_owner_written_back` 报告按生成时合同保持只读兼容；新报告使用 recovery ledger。

### 3.4 Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SF-EXAMPLE` | 非 pending 写 `RP-<stable-digest>`；pending 写 `—` | `deep`、`standard`、`closure` 或 `not_required` | 精确版本、tag、DOI、commit 或日期 | `SRC-...@<version / tag / DOI / commit>`；多项按 Source ID 与版本排序 | 章节、公式、图表或身份定位 | 实验、baseline 与 evaluation contract 定位 | limitations、Appendix、反证或冲突定位 | repository、release、RFC 或 artifact 定位 | Report 中的稳定 claim-boundary ref；pending 可写 `—` | `complete`、`pending`、`blocked` 或 `not_required` |

规则：

- 每个 Candidate Ledger family 必须恰好对应一行，路由、Completion Result 与 Review / Access Status
  必须遵循本合同 §8.1 的唯一真值表。
- `pending` 也必须保留一行，以明确路由、已经取得的 locator 和具体未完成范围；未完成 facet 写
  `Pending — <具体缺口>`，不能写空值、裸 `N/A` 或泛化“待审阅”。此时 Review Provenance ID、
  Claim Boundary Ref 与 Review Ref 可以写 `—`，Evidence Gate 必须为 Open，Completion 必须为 In Progress。
- `Reviewed Evidence Versions` 只列实际用于本次 claim 的 evidence，不把纯 discovery Source ID 冒充已读证据。
  每项使用 `Source ID@精确版本`，按 Source ID、再按版本字典序排序并以 `; ` 连接；Primary Evidence
  Version 必须匹配该集合中恰好一项的版本部分。pending 保留已取得版本，并对未知项写
  `Pending — <具体缺口>`。
- `complete / blocked / not_required` 的 Review Provenance ID 不是作者自报字段，而是由 validator 复算：对
  下列 canonical fields 以竖线连接、计算 SHA-256，并写成 `RP-` 加前 16 个十六进制字符：

  ```text
  review-completion-v1
  | Source Family ID
  | Event Identity
  | Primary Identifier
  | canonical Supporting Source IDs
  | Primary Evidence Version
  | canonical Reviewed Evidence Versions
  | Review Route
  | review-override:<Review Override>（仅在 `Review Override` 非 `none` 时存在）
  | canonical Method / Identity Locators
  | canonical Evaluation Locators
  | canonical Limitations / Counterevidence Locators
  | canonical Artifact Locators
  | Claim Boundary Ref
  | Review Ref
  | review-body-sha256:<完整 64 个十六进制字符的 digest>
  ```

  Supporting Source IDs、Reviewed Evidence Versions 与四个 locator cell 都先按 `;` 拆分、trim、Unicode
  NFC、字典序排序，再以 `;` 连接。Review body 从唯一
  `<!-- review:<Family ID>:start --> ... <!-- review:<Family ID>:end -->` 内部提取，不包含 markers；统一
  CRLF / CR 为 LF、Unicode NFC、删除每行尾部空白并移除首尾空行，再以 UTF-8 计算完整 SHA-256。
  `complete / blocked / not_required` 都必须有该有界 Review body 与位于其中的 Claim Boundary；pending
  没有 RP，也不计算 body digest。同一 Report 内 RP 必须唯一。历史复用必须通过 Prior Review Ref
  指向原 provenance ID / receipt，不得用标题或 URL 替代。
- `closure` 要求身份、日期和重复关系 locator；`standard` 在此之上要求 mechanism、evaluation、
  limitation 与 claim boundary；`deep` 要求按已公开范围定位 Method、Evaluation、Limitations
  与 Artifact。
- 确实不适用或未公开的字段使用带原因的 `Not Required — ...` 或 `Not Disclosed — ...`；
  裸 `N/A`、“已读”、“见原文”或空泛 URL 不是 locator。
- 非 pending 状态必须同时有可定位的 `Review Ref` 正文；Receipt 不代替叙事，叙事也不代替 Receipt。
- 本接口不使用字数阈值判定深度。

### 3.5 Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| `SF-EXAMPLE` | `score_7_9`、`forced_review`、`potential_books_delta`、`potential_structural_gap` 或 `cross_cutting_correction`；可多值 | `selected`、`subsumed` 或 `not_selected` | selected 写 `DA-...`；其他写 `—` | subsumed 写 selected Unit ID；其他写 `—` | 根据研究合同优先级给出候选间比较 | selected / subsumed 指向 `analysis:<Unit ID>`；not_selected 指向 `analysis-decision:<Family ID>` |

- eligibility pool 以 Source Family 为分母；每个 eligible family 必须恰好一行，非 eligible family 不得出现。
- eligible family 非空时至少有一个 selected unit；为空时保留空表，不伪造 Deep Analysis。
- `selected` 必须有 Analysis Unit ID 且 `Subsumed By = —`。多个 selected family 只有在共享一条不可拆分的
  演进链时才能复用同一 Unit ID；不同 selected Unit ID 最多三个。
- `subsumed` 的 `Analysis Unit ID = —`，`Subsumed By` 必须解析到当前表中至少一个 `selected` family 的
  Unit ID，Narrative Ref 指向该 selected unit 的有界分析，并在其中实际覆盖本 family。
- `not_selected` 的两个 unit 字段都写 `—`，Narrative Ref 使用
  `analysis-decision:<Family ID>` 的有界选择说明。
- Eligibility 只能由 Selection 前已经存在的 Score、Review Override、Evidence-stage knowledge-tree
  position 或跨 family correction 得出；不得由最终 Books Disposition 倒推。
- “超过三项”、“篇幅有限”或“其他类似”不是 Priority Rationale。
- selected Narrative Ref 使用 `<!-- analysis:<Unit ID>:start --> ... <!-- analysis:<Unit ID>:end -->`
  有界区间；not_selected 使用同样的 `analysis-decision:<Family ID>` start / end markers。
- 本表只选择报告长叙事，不允许将未选中 family 的 Source Review 降级或跳过。

### 3.6 Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SF-EXAMPLE` | `INFER-...`；Structural 时写 `considered:<Node IDs>` | 当前 owner 或实际审阅过的 owner 候选章节路径与定位 | 前后章或交接章定位 | `existing:<Family ID>` | `delta:<Family ID>` | 五类演进关系；确无技术关系时写 `Not Applicable — <具体原因>` | `Integrate`、`No Change — Existing Coverage` 或 `Structural Candidate` | `books-review:<Family ID>` |

`Integrate`、`No Change — Existing Coverage` 与 `Structural Candidate` 必须恰好有一行。
`Structural Candidate` 在 Candidate Ledger 中仍没有 canonical Stable Node，写 `—`；但 Books Comparison
必须以 `considered:<Node IDs>` 列出实际排查过的现有 owner，并保存对应 Target / Adjacent Chapter Ref、
现有命题、新证据差异和有界 Books Review。Evolution Relation 只能使用 `Direct Evolution`、
`Layering / Dependency`、`Principle Reuse`、`Explanatory Analogy`、`Alternative Branch`，或带具体理由的
`Not Applicable — ...`；它不能填写 Books disposition。其他 disposition 不要伪造 Books Comparison，
但仍必须在 Candidate Ledger 闭合。

Books Comparison 得到 `Integrate` 时，该 family 的 Selection 行必须已经包含 `potential_books_delta`；得到
`Structural Candidate` 时必须已经包含 `potential_structural_gap`。若 Evidence 阶段没有识别该 potential，
先重开 Deep Analysis Selection 并接受其 semantic audit，再完成 Books Decision；不得直接用最终 Decision
回填一条看似事前存在的 eligibility。

### 3.7 Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SA-EXAMPLE-COVERAGE` | 未参与本 Report 主要写作的 reviewer 身份 | `coverage`、`evidence`、`deep_analysis_selection` 或 `books` | receipt、review、analysis 或 books refs | finding ID；没有则写 `—` | 关闭 finding 的修复引用；没有则写 `—` | `passed`、`open` 或 `not_applicable` |

- 四个 scope 必须各有且只有一行。Daily 和 Sunday Weekly 的四项都适用；Historical Weekly
  未获授权 Books Integration 时，仅 books scope 可为 `not_applicable`。
- Auditor 必须是 fresh-context human 或 agent reviewer，不能是该 Report 的主要作者或空泛的
  `self / author / validator`。
- `passed` 要求未解决 finding 为零；`open` 必须保留具体 finding ID 与影响范围。
- scope 到 Gate 的映射唯一如下：`coverage → Coverage Gate`；`evidence → Evidence Gate`；
  `deep_analysis_selection → Evidence Gate`；`books → Books Gate`。coverage audit 为 `open` 时 Coverage
  Gate 为 `Open`；evidence 或 deep_analysis_selection audit 为 `open` 时 Evidence 与 Books Gate 都为
  `Open`；books audit 为 `open` 时 Books Gate 为 `Open`。`passed` 只移除该 scope 的上限，不会替其他
  receipt 抬高 Gate。
- validator 只校验本收据的存在、引用和状态一致性，不代替 reviewer 的语义判断。

### 3.8 Benchmark Contract

当任何 Candidate Ledger 行写 `Benchmark Claim = yes` 时，必须加入：

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SF-EXAMPLE` | workload | model/version | hardware/topology | precision/quantization | length | length | batch | concurrency | latency/throughput/quality SLO | evaluator/version |

未披露字段写 `Not Disclosed`，不得留空或推断。

Candidate Ledger 中每个 `Benchmark Claim = yes` 必须恰有一行合同；每行 benchmark contract 也必须反向对应一个 `yes` 候选。孤立、重复或未绑定的 benchmark 行均不能通过校验。

## 4. Daily 必填内容

### 4.1 Canonical Daily 展示结构

Daily 的机器接口与读者界面必须使用同一份状态真值。所有 `V2.1 + Report Type = Daily` 报告统一采用
下列展示结构；日期重建、恢复任务和本地生成器不得另造章节顺序或用引用块代替状态字段：

```text
# Daily Research — YYYY-MM-DD

Research Date
Timezone
Strict Window
Contract
Status

## Executive Summary
## 1. Coverage
## 2. Candidate Ledger
## 3. Review Completion Receipt
   ### Source Reviews
## 4. Benchmark Contracts
## 5. Deep Analysis Selection
## 6. Books Comparison
## 7. Semantic Audit
## 8. Ignored Noise
## 9. Recommended Action
## 10. Repository Changes
## 11. Open Questions
## 12. Sources
## 13. Final Status
```

- 标题后的 canonical preamble 必须且只能按 `Research Date → Timezone → Strict Window → Contract → Status`
  排列五个字段；字段移入正文、重复字段、窗口与报告日不一致或 Contract 降级都属于 schema failure。
- `Status` 必须概括 metadata 中的 Completion 与三个 Gate，不能用历史 checkpoint 或执行中描述覆盖最终真值。
- `Review Status`、`Access Status` 与 `Books Disposition` 保留在 Candidate Ledger；顶部 `Status` 不能替代这些逐 family 状态。
- Source Review 正文归入第 3 节；Deep Analysis 正文归入第 5 节；逐 family Books 处置归入第 6 节。
- `Materials Request`、恢复收据和其他条件性内容作为相关节的三级标题，不改变 13 节编号。
- 某节当日无项目时仍保留该节并明确写 `None` 或实际边界，不能删除章节造成 schema 漂移。
- `Final Status` 必须重述 Completion、Coverage、Evidence、Books 与明确的未解决 finding 数量；Complete 且三个
  Gate 闭合时该数量必须为 `0`。它与 metadata 不一致时，
  报告不得标记 Complete。
- 目录级审计只发现正式 Report，不递归把 `_sources/` 下的 evidence packet、审计收据或历史快照解释成
  新的 owner Report；需要检查某个证据文件时必须用显式文件路径。这样既保留历史证据，也避免旧 schema
  与重复 Source Family 污染正式报告集合。

Validator 只证明上述接口与状态自洽；它仍不能替代各 scope 的 fresh-context Semantic Audit。

Daily 必须包含：

1. `Executive Summary`：先给出当日是否存在长期重要进展。
2. `Coverage`：Metadata、Source Coverage Receipt 和 Coverage Limitations。
3. `Candidate Ledger`：按“模型与研究机构 → 学术来源 → AI Infra 与工程项目”组织。
4. `Source Review`：所有 canonical event time 落入实际窗口的候选按 Score V2 完成对应证据包，并与
   Review Completion Receipt 一一对应。
5. `Deep Analysis`：先完成 Selection Receipt，再为最多三个入选单元重建技术演进；未入选不等于未审阅。
6. `Knowledge Tree Position`：Evidence 阶段先记录可能的 Stable Node；进入 Books Decision 后才补当前及相邻章节审阅。
7. `Recommended Action / Books Decision`：逐 Source Family 给出最终处置；需要章节判断的 family 必须有 Books Comparison。
8. `Semantic Audit`：分别审阅 coverage、evidence、Deep Analysis selection 和 Books。
9. `Ignored Noise`：说明被排除的营销、转载、重复、低耐久度或越界内容。
10. `Repository Changes`：实际修改与未修改的文件。
11. `Open Questions`：待验证事实、实验边界和材料缺口。
12. `Sources`：URL、发布日期 / first-public date 与访问日期。

Daily 未完成 Required Daily receipt、候选分母冻结或 primary evidence 边界时，Evidence Gate 保持 `Open`，不能进入 Books Integration。`Must Read` 不等于必须修改 Books。

## 5. Sunday Weekly 必填内容

Sunday Weekly 在 Daily 合同之上必须包含：

- `Coverage Window`
- `Coverage Limitations`
- 七份 Daily receipt 汇总与缺失日说明
- Required Weekly、正式出版与 Periodic/event-trigger 补检
- `Cross-Week Deduplication`
- `Event-Date Daily Decision`
- `Books Integration Decision`
- Deep Analysis Selection 与跨日技术演进，入选叙事不超过三项
- 四个 scope 的 Semantic Audit

Weekly 不是七份 Daily 的摘要拼接。技术演进的推导与关系分类只由 [LEARNING_PHILOSOPHY.md](./LEARNING_PHILOSOPHY.md) 定义；Weekly 应应用该方法重建跨日变化，不在本合同复制第二份演进模板。

同一 Source Family 在一周内出现论文、revision、release 和 artifact 时，以一个 owner family 串起演进，不重复评分。

## 6. Historical Weekly 必填内容

Historical Weekly 在 Weekly 合同之上必须包含：

- 完整 ISO week 与 first-public owner 说明；
- Full Replay 直接执行的 Required Daily / Weekly receipt，或 Delta Audit 的 baseline effective coverage 与
  changed-source receipt；
- selected venue、delayed listing、revision 与相邻周 spillback reconciliation；
- Source Delta Audit 结果；
- Materials Request Ledger；
- 单一 reconciliation owner 的最终 owner-family ledger；
- 每个候选的 Review / Access / Books disposition；
- Review Completion、Deep Analysis Selection 与 Semantic Audit；
- 年度索引 writeback 与下一 continuation point。

Historical `Coverage Mode`：

- `Full Replay`：未生成的历史周，执行当前注册表的全部到期来源；
- `Delta Audit`：已完成周相对 baseline 只执行 Changed Source IDs 和受影响 family reconciliation。必须记录
  baseline path、previous denominator、差集来源、新 denominator 与冻结时间；旧 V1 账本继续保留。

### Delta Audit Queue Notification 与 True Reopen

`Delta Audit Queued` 只是非权威待办通知：它可以在 legacy Weekly 或年度索引中记录待检查的 baseline、
changed Source IDs、潜在 owner week 与 continuation point，但表示 Delta Audit 尚未开始。Queue notification：

- 不声明或修改 `Contract Version`、`Score Schema`、`Coverage Mode`、Denominator ID、Gate、Completion Status
  或 Semantic Audit status；
- 不写任何 V2.1 marker / Receipt / Candidate / Review / Selection / Books packet；
- 不把旧 Gate 外推到新增来源后的当前分母。旧 Gate 只保留为 legacy denominator 的历史结果，不构成
  当前 completeness claim。

因此，只有 queue notification 的 legacy Weekly 仍由 `--audit` 只读兼容，不构成 true reopen，也不接受
`--report` strict 成功的声明。`Source Delta Audit — No Reopen` 与 queue notification 不同：前者表示审计已经
按 V2.1 完成，并以完整 delta packet 证明没有需要重开的 owner family；后者只表示审计尚在队列中。

True reopen 从以下任一动作首次发生时开始：写入或修改任何 V2.1 machine interface；创建或改变 effective
denominator；执行 changed-source Receipt / affected-family reconciliation；改变当前 Gate、Completion 或
Semantic Audit status；或对扩大后的分母作当前 completeness claim。此时必须同时声明 V2.1 contract / V2
score，补齐当前 Delta Audit 所需的全部 V2.1 接口，并接受 `--report` strict。仅用“queued”“pending”或
“reopened”标签不能改变这个边界；如果已经改变当前状态却没有完整 packet，该 Report 是不合规的 true
reopen，而不是可绕过 strict 的 queue notification。

Delta Audit 的 Receipt 与 Candidate Ledger 只记录本轮 changed-source 命中和受影响 family，不复制 baseline
的未变化候选；因此当前两张表的 family 集合仍须双向相等。effective coverage / denominator 则等于 baseline
effective state 应用本轮 delta 后的结果，必须能沿 Baseline Report 链复算。`Denominator ID` 表示这个 effective
denominator 的新冻结身份。若 baseline 已有 V2 / V2.1 Denominator ID，必须与 `Previous Denominator ID`
一致；若 baseline 是没有 denominator 字段的 Score V1 Legacy 或 earlier Score V2 Report，使用 §3.1 定义的
legacy identity，并明确保留差分边界，不能声称已经按 V2.1 contract 全量重放。

历史回填不补造 Daily。后续周发现早期候选时，写回真实 owner week，并在发现周记录 spillback；不得在两个周重复计分。

旧 Review 仅在 Source Family identity、primary identifier、evidence version、route-specific locators、
claim boundary、Review Provenance ID、Prior Review Ref 与重要 revision 检查全部可回溯时才能写
`Reconciliation = reused_unchanged`。否则必须重新审阅或保持 `Review Status = pending`。

并行执行只允许产生 read-only Source Packet：

```text
Week N discovery / review   ─┐
Week N+1 discovery / review ─┼→ 串行日期与 family reconciliation
Week N+2 discovery / review ─┘  → owner Weekly → 年度索引 → per-week Review
```

子任务完成的条件是负责周的到期来源、候选分母、所有 Review 路由和材料清单都闭合；“找到一些论文”或“写出草稿”不是完成。

## 7. Materials Request Ledger

自动恢复顺序：

```text
arXiv HTML
→ 对应版本 PDF
→ 作者项目页 / repository / artifact
→ 官方 Blog、model/system card、RFC、release
→ OpenAlex / Crossref / DBLP / DataCite identity reconciliation
```

仍无法解决时，每项材料请求必须包含：

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `MR-SF-EXAMPLE-01` | `P1 Full Text` | `SF-EXAMPLE` | `—` | `—` | `2026-W35` | URL、arXiv ID、DOI、tag 或 commit | 缺少的具体材料 | 现有材料为何不足 | 可接受的替代材料 | 建议文件名 | 材料补回后需要完成的审阅范围 |
| `MR-SRC-EXAMPLE-01` | `P4 Discovery Export` | `—` | `SRC-EXAMPLE` | `GAP-SRC-EXAMPLE-01` | `2026-W35` | 已知 endpoint、query 或 cursor | 缺失的枚举结果或访问能力 | 为什么无法由确定性 fallback 闭合 | 可接受的导出、镜像或快照 | 建议文件名 | 恢复后需要重放的来源与分母范围 |

该表只在存在材料请求时出现。每个 `Review Status = blocked` 且 `Access Status = partial / blocked /
unverified` 的候选必须恰有一行；每行也必须反向对应这样的受阻候选。若来源在形成候选身份之前失败，则对应 `failed` receipt 必须由 `Source ID + Gap / Limitation ID` 唯一映射到一行材料请求，`Source Family ID` 写 `—`；候选级请求则填写 `Source Family ID`，来源与 gap 两列可写 `—`。`disputed` 只有在解决冲突确实需要外部材料时才进入此表，否则在 Source Review 中并列冲突证据与不可判定范围。

优先级：

- `P0 Identity`
- `P1 Full Text`
- `P2 Artifact`
- `P3 Revision`
- `P4 Discovery Export`

同一 Source Family 只请求一次，其他周引用该请求。

## 8. Gate 与完成条件

### 8.1 唯一状态与 Gate 真值表

下表是 Coverage Result、Access Status、Review Status、Semantic Audit、Books Disposition 与 Report Gate
的唯一映射。
未列出的组合均为状态冲突，strict validator 必须报错：

| Object State | Review / Closure State | Required Evidence | Gate Ceiling | Completion Consequence |
| --- | --- | --- | --- | --- |
| deterministic source `checked / no_hit` | cursor、watermark 与 closure evidence 完整 | Source Coverage Receipt | Coverage `Closed` | 可进入 denominator freeze |
| source `incomplete` | 已执行，但 ordinary closure 未完成 | 当前窗口与缺失的 closure field | Coverage `Open` | `In Progress` |
| deterministic source `failed` | 精确 external failure，ordinary work 已闭合 | Gap / Limitation、Materials Request、forward policy | Coverage `Conditional Pass` | 可为 `Conditional` |
| non-deterministic backstop `failed` | 失败已记录 | Coverage Limitation | 不降低确定性 Coverage | 不支持“全网无遗漏” |
| 合法 `not_due` | trigger / periodic 检查已记录 | trigger condition receipt | 不降低 Coverage | Required source 不得使用 |
| `accessible` | 与路由相符的 `*_complete` | Review Completion + Review Ref | Evidence `Passed` | 可进入 Books Decision |
| `accessible` | `pending` | 待完成 review scope | Evidence `Open` | `In Progress` |
| `partial` | `pending` | 仍可执行的恢复或阅读范围 | Evidence `Open` | `In Progress` |
| `partial` | `blocked` | Materials Request 与已尽可达工作 | Evidence `Conditional Pass` | 可为 `Conditional` |
| `blocked / unverified` | `blocked` | Materials Request 与精确影响范围 | Evidence `Conditional Pass` | 可为 `Conditional` |
| `disputed` | `pending` | 待对读的冲突证据 | Evidence `Open` | `In Progress` |
| `disputed` | 与路由相符的 `*_complete` | Review / Claim Boundary Ref 中的并列证据与不可判定范围 | Evidence `Conditional Pass` | 可为 `Conditional` |
| `accessible` | `not_required` | duplicate / out-of-scope 关系与历史 provenance 完整 | Evidence `Passed` | 只执行 reconciliation closure |
| `accessible` | `deep_complete` + `important_revision` | revision versions、locator、artifact delta、RP 与 owner 关系完整 | Evidence `Passed` | 不重复评分，但重做 Selection / Books Decision |
| coverage Semantic Audit `open` | 有未解决 coverage finding | finding ID、影响范围与待修复 ref | Coverage `Open` | `In Progress`；Books 由 report-level 聚合保持 `Open` |
| evidence Semantic Audit `open` | 有未解决 evidence finding | finding ID、影响范围与待修复 ref | Evidence `Open` | Books 同时保持 `Open` |
| deep_analysis_selection Semantic Audit `open` | eligibility、分组或选择 finding 未解决 | finding ID、影响 family 与待修复 ref | Evidence `Open` | Books 同时保持 `Open` |
| books Semantic Audit `open` | Books Comparison / disposition finding 未解决 | finding ID、影响范围与待修复 ref | Books `Open` | `In Progress` |
| Semantic Audit `passed` | 该 scope 未解决 finding 为零 | reviewed refs 与 resolution | 不降低对应 Gate | 仍须满足其他行 |
| Books `Integrate` | Books Comparison 已闭合，且稳定 owner 可解析 | Books Comparison + Books Review Ref + Stable Node ref + books audit passed | Books `Passed` | 仍须 Coverage Closed、Evidence Passed |
| Books `No Change — Existing Coverage` | Books Comparison 已闭合，且现有命题可定位 | Books Comparison + Books Review Ref + existing proposition ref + books audit passed | Books `Passed` | 仍须 Coverage Closed、Evidence Passed |
| Books `Structural Candidate` | Books Comparison 已闭合，且现有 owner 候选均无法承载 | Books Comparison + Books Review Ref + considered owner refs + books audit passed | Books `Passed` | 仍须 Coverage Closed、Evidence Passed |
| Books `Weekly Only — Context` | 最终 disposition 与上下文边界已闭合 | Candidate Ledger + books audit passed | Books `Passed` | 仍须 Coverage Closed、Evidence Passed |
| Books `Version Fact / Mechanism Not Disclosed` | 最终 disposition 与证据边界已闭合 | Candidate Ledger + books audit passed | Books `Passed` | 仍须 Coverage Closed、Evidence Passed |
| Books `Rejected — Low Durability / Out of Scope` | 最终 disposition 与拒绝理由已闭合 | Candidate Ledger + books audit passed | Books `Passed` | 仍须 Coverage Closed、Evidence Passed |
| Books `Blocked / Unverified` | 对应 external blocker 已精确界定 | blocked Review、Materials Request、影响范围 | Books `Conditional Pass` | 可为 `Conditional` |
| Books `Disputed` | 对读已完成但无法唯一判定 | completed disputed Review、Claim Boundary / dispute ref | Books `Conditional Pass` | 可为 `Conditional` |
| Books `Not Assessed` | Historical 未授权 Books | books audit `not_applicable` | Books `Not Applicable` | 可用于 Historical `Complete` |
| Books `Not Assessed` | Daily / Sunday 或已授权 Historical | 待 Books Decision | Books `Open` | `In Progress` |

`Conditional Pass` 不是“差不多完成”。它只能表示 ordinary work 为零，且剩余不确定性是
已精确界定的 external blocker 或已完成对读却无法唯一判定的 `disputed`。

Report-level Books Gate 按最严格状态聚合：Coverage 或 Evidence 为 `Open` 时 Books 必须为 `Open`；
两者没有 Open、但任一为 `Conditional Pass`，或任一候选使用上述 conditional Books disposition 时，
Books 必须为 `Conditional Pass`；只有 Coverage = Closed、Evidence = Passed、所有候选取得非 conditional
最终 disposition、适用 Books Comparison 完整且 books audit passed 时，Books 才能为 `Passed`。未授权
Historical Books 是唯一 `Not Applicable` 例外。

### 8.2 完成条件

Report 只有满足以下条件才能写 `Completion Status = Complete`：

- 到期来源均有唯一 Coverage Receipt；
- 实际窗口、Executed At、watermark、分页 / cursor 和 closure evidence 可复算，且没有
  `incomplete`；
- owner-family ledger 已冻结且无未解释重复；
- Score V2 Total 正确，强制 Deep Review 已执行，Review Completion Receipt 与 Candidate
  Ledger 一一对应；
- Deep Analysis eligibility pool 已全部处置，且入选单元不超过三个；
- 普通 `Review Status = pending` 为零；
- blocked / unverified / disputed 为零；这些状态即使有精确影响范围，也只能支持 `Conditional`；
- Books Gate 已通过；只有未执行 Books Integration 的 Historical Weekly 才能明确写 `Not Applicable`；
- Report、年度索引和 Books owner/disposition 一致；
- 适用的 Semantic Audit scope 全部为 `passed`，且未解决 finding 为零；
- Markdown、链接、日期、标题、围栏和 Git 范围检查通过。

`Complete` 要求 Coverage = Closed、Evidence = Passed、Books = Passed；只有未执行 Books Integration 的 Historical Weekly 才允许 Books = Not Applicable，此时所有候选必须为 `Not Assessed` 且没有 `Books Review Ref`。Daily 与 Sunday Weekly 不得使用 Books N/A。精确 external blocker 或已完成对读却无法唯一判定的 `disputed` 使 Gate 无法完全闭合时，使用 `Conditional Pass`，不能宣称 `Passed`。`Conditional` 只用于 ordinary work 已经闭合、至少一个 Gate = Conditional Pass 且没有 Gate = Open 的情况。存在普通 pending、`incomplete` 或未执行 Required source 时必须是 `In Progress`。

无论 Completion Status 为何，Books Gate 只有在 Coverage = Closed、Evidence = Passed 且没有 blocking / unresolved / pending / `Not Assessed` 时才能写 `Passed`。

Backstop 不可访问必须记录，但本身不降低确定性 Coverage Gate。`Access Status = disputed` 对应 Evidence Gate = Conditional Pass 或 Open；`Disputed` 不是 Gate 值。

## 9. Legacy 与 earlier Score V2 兼容

旧六维 `/30` 账本原样保留，并标记为 `Score V1 Legacy`。缺少 `Contract Version: V2.1`、但已有
`Score Schema: V2` 的报告称为 `earlier Score V2 Report`；它不是 Score V1 Legacy，也不会因为 audit
只读兼容而获得 V2.1 semantic-complete 身份。本合同不机械重算或重写二者。Report 真实重开并把受影响
候选迁移到 V2.1 contract / V2 score 时，必须保留旧分数与旧 contract 的历史身份，避免把 V1 `/30` 与 V2 `0～9`
混为同一量纲。

## 10. 校验命令

```text
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_research.py
python3 scripts/validate_research.py --audit papers/
git diff --check
```

`--report` 对本轮生成或重开的文件执行 strict 校验：缺少 Contract Version V2.1
或 Score Schema V2 直接失败。`--audit` 允许 Score V1 Legacy 与 earlier Score V2 Report 保持只读兼容，
同时执行其可判定的跨报告 Source Family owner reconciliation；旧报告不会被机械改写，也不会自动继承
V2.1 Review / Semantic Audit 完成状态。校验命令成功只是结构结果，语义结果以 Semantic Audit Receipt 为准。
