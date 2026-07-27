# Codex Historical Research Prompt

## 目标

Historical Research 用于恢复完整 ISO Weekly 的证据链，而不是把后来看到的新闻摘要反写成
历史事实。Weekly 必须尽可能接近 Live Daily 的候选覆盖度，同时保留 first-public date、revision、
primary evidence、技术演进与 Books 决策边界。

Historical Backfill 不创建历史 Daily。所有事件、评分、Source Review、spillback 与缺口直接写入
对应的 `papers/<ISO-week-year>/weekly/<ISO-week-year>-W<week>/README.md`；年度索引只维护
可复算汇总账本。

## 归档时钟与事件归属

1. Weekly 覆盖完整 Monday～Sunday，不按月末、季度末或回填批次截断。
2. 论文以 arXiv v1 或其他可核验 first-public date 归周；revision 是同一 Source Family 的演进节点，
   不重复计为新论文。
3. 官方发布、technical report、model/system card、代码或 artifact 可形成不同 event node，但必须共享
   Source Family，并分别记录日期和证据角色。
4. discovery feed、Blog 或后续 Weekly 发现更早事件时，写回真实 owner week；推荐日期不能替代事件日期。
5. 跨年 ISO week 以 ISO-week-year 归档，不能重复进入两个年度。

## 固定来源顺序

候选必须按以下顺序检索和组织：

1. 模型与研究机构；
2. arXiv 与学术来源；
3. AI Infra 与工程项目。

机构和工程项目的固定顺序沿用 `CODEX_DAILY_RESEARCH_PROMPT.md`。学术发现每日/每周使用 arXiv、
Google Scholar、OpenAlex、DBLP；Semantic Scholar 与 Hugging Face 用于补充发现和去重；Crossref
用于 Weekly metadata 交叉检验。聚合索引只能发现候选，机制结论必须回到 primary source。

## 唯一标识与去重

每个候选以以下组合建立唯一身份：

```text
Source Family ID
+ primary identifier（arXiv / DOI / release tag / PR / RFC）
+ first-public date
```

标题大小写、版本号、Blog 标题或推荐日期不能单独作为唯一键。同一论文的 v1、后续 revision、代码发布和
机构解读应通过 Source Family 连接，并明确属于 `Direct Evolution`、`Layering / Dependency`、
`Principle Reuse` 或 `Explanatory Analogy`。

## 状态词汇表

- `Review Pending`：primary material 已可访问，但尚未完成要求的阅读范围。
- `Unverified / Blocked`：正文、唯一身份、指定版本或决定机制是否成立的 artifact 无法取得。
- `Discovery Gap`：存在可能遗漏的线索，但尚不能建立候选身份、评分或机制结论。
- `Disputed`：来源可读，但日期、revision、实验条件、复现结果或不同 primary sources 相互冲突。
- `Books Pending`：Weekly evidence 已完成，但该 Source Family 尚未完成 Books 判断；它不是 Weekly 缺失。
- `Version Fact / Mechanism Not Disclosed`：只有官方版本或产品事实，没有公开内部机制。

`Blocked` 可以按用户确认的 blocked-skip 规则不阻止 forward cursor，但必须保留在 Backlog Ledger，
不能计入 Full Source Review，也不能支持 Books。`Review Pending` 不得与 `Completed` 同时出现。

## 评分与阅读门槛

六维评分均为 0～5：Technical Novelty、System Impact、Practical Value、Source Reliability、
Project Relevance、Longevity。

- 所有 `20+` 候选必须完成非模板化 Full Source Review。
- 低于 20 分的候选至少核验 primary identity、日期、评分和拒绝理由。
- 无法访问正文时不得根据标题或摘要沿用旧评分；旧分数只能标记 provisional discovery priority。
- Must Read 不等于必须修改 Books。

Full Source Review 至少包含：

```text
Candidate / Week / Score
Source Family ID / Source Type
Event Date / First-public Date / Revision History
Direct and Related Primary Sources
Access and Verification Status / Full-read Coverage
Original Problem / Why Previous Design Was Reasonable / Changed Constraint
Mechanism / State Ownership / Control Flow / Data Flow / Implementation
Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead
Hardware / Model / Precision / Length / Batch / Concurrency / SLO
What the Evidence Proves / Does Not Prove
Limitations / Threats to Validity
Trade-offs / New Failure Modes / Where Previous Design Still Applies
Evolution Relationship
Stable Knowledge Node ID / Current Chapter / Legacy Chapter
Target and Adjacent Chapters Read / Existing Coverage
Integration Decision / Rejection Reason / Open Questions
```

公开材料未披露的字段写 `Not Disclosed`，不得从产品能力反推内部模型、训练或 runtime。

## Blocked Source Recovery

对所有 blocked 项按以下顺序重试：

```text
arXiv HTML
→ 对应事件版本 PDF
→ 作者项目页 / repository / artifact
→ 官方 Blog / technical report / model card / system card / RFC / Release
→ OpenAlex / Crossref / DBLP metadata 交叉确认
```

恢复全文后必须真正补齐 Method、公式/算法、实现、完整 Evaluation、ablation、相关 Appendix、
limitations 与 artifact，不得只删除 `Blocked` 标签。若仍无法恢复，在年度 Materials Request Ledger
中记录 Priority、Week、Source Family、已知 identifier、具体缺失材料、不足原因、可接受替代材料、
建议文件名与补回后的审计范围。

## 技术演进与 Books Gate

Weekly 必须保留：

```text
原始约束
→ 旧方案为什么合理
→ 旧方案暴露的边界
→ workload / scale / hardware / SLO 变化
→ 新机制改变什么
→ 证据证明与未证明什么
→ 新增状态、成本和 failure mode
→ 新旧方案各自成立的条件
→ 下一阶段压力
```

Books 使用两道独立 Gate：

- `Source-Family Books Gate`：identity、event-time revision、全文、claim/evidence boundary、artifact、Stable Node owner 与相邻章节均完成后，可逐 family 进入 Books；`Blocked`、`Disputed` 与 `Version Fact / Mechanism Not Disclosed` 不得进入长期机制正文。
- `Archive Completion Gate`：年度 discovery replay、revision 去重、blocked recovery 与材料账本全部闭合后，才可宣称历史归档完整。

Archive Completion Gate 仍 Open 不必冻结已通过 Source-Family Gate 的可靠机制，但不得把局部完成写成年度无遗漏。Weekly 摘要本身不能进入 Books，也不得为制造 Git Diff 强行修改章节。

## 每周与年度验收

每完成一周或一个小批次，立即检查：

- ISO window、first-public date、revision 与跨周归属；
- 来源真实性、Source Family 唯一性、评分 Total 和 Evidence Level；
- Full Source Review 是否非模板化，事实、作者结论和推断是否分开；
- ROADMAP owner 与相邻章节是否实际核对；
- `Review Pending`、`Blocked`、`Discovery Gap`、`Disputed` 和 `Books Pending` 是否一致；
- Markdown 标题、围栏、URL、相对路径和行尾空白。

年度完成还要求：所有 Weekly 有最终 discovery disposition；`Review Pending = 0`；每个仍 blocked 项都有
明确材料请求；spillback 与 revision 可回溯；年度索引、Weekly、Live Daily 和 Learning State 一致；
`git diff --check` 与工作树范围检查通过。

不得执行 git stage、commit、push、reset、checkout、clean 或其他破坏性操作。
