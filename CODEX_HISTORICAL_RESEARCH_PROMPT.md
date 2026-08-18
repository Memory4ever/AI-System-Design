# AI-System-Design Historical Weekly Adapter

版本：V2.1
适用范围：完整历史 ISO Weekly、Source Delta Audit、材料恢复

## 1. 任务

Historical Research 用于恢复完整 ISO week 的可复算证据链，不把后来看到的摘要反写成历史事实，也不补造历史 Daily。

所有通用规则只由以下文件定义：

1. `docs/RESEARCH_CONTRACT.md`
2. `docs/RESEARCH_SOURCES.md`
3. `docs/REPORT_CONTRACTS.md`

本 Adapter 只保留历史模式特有的日期归属、并行边界、spillback、材料恢复与增量重开规则。

## 2. 运行前加载

读取：

- `AGENTS.md`
- 上述三个统一合同
- `ROADMAP.md`
- `papers/<year>/weekly/README.md`
- 当前待处理 Weekly 与前后相邻周
- `docs/LEARNING_STATE.md` 中最新历史 cursor / checkpoint

只处理当前 checkpoint 尚未闭合的来源或候选。旧 Source Review 是否可复用，必须按
[Research 合同 §11](./docs/RESEARCH_CONTRACT.md#11-历史兼容review-复用与-source-delta-audit) 验证完整 provenance；
不得仅凭旧状态、标题或 URL 略过审阅。

## 3. 历史归属

- Weekly 必须覆盖完整 Monday～Sunday，不按月末、季度末、年末或批次截断。
- 论文按 arXiv v1 或其他可核验 first-public date 归周。
- revision、正式发表、release、代码和项目页是同一 Source Family 的演进节点，不重复成为论文 owner。
- discovery feed、索引收录、后续 Weekly 或人工发现日不能替代 event date。
- 跨年周按 ISO-week-year 归档。

任何日期、身份或 revision 冲突都按公共合同保留对读和不可判定边界；不能用标题或最新版本
猜测事件时事实。

## 4. Source Delta Audit

新来源注册表不会触发全年机械重跑。只安排后续检查时，使用
[Report 合同 §6](./docs/REPORT_CONTRACTS.md#delta-audit-queue-notification-与-true-reopen) 的
`Delta Audit Queued`，不要提前声明当前 Gate、Completion 或 V2.1 packet。真正开始审计后，才使用
`Coverage Mode = Delta Audit`：

```text
读取注册表 Effective Date
→ 比较旧 owner-family ledger 与新增来源命中
→ 核对相邻周 spillback / delayed listing
→ 核对 identity、first-public 与重要 revision
→ 只重开真实受影响 owner week
```

重开条件只有：

- 新发现 in-window Source Family；
- first-public owner 冲突；
- 重要 revision 改变机制或实验结论；
- 原报告没有足够的 receipt / pagination / ledger 证据证明 denominator。

完成审计且没有上述差异时，记录 `Source Delta Audit — No Reopen`；它不是 queue notification。baseline、
changed sources、effective coverage / denominator、earlier-owner reconciliation 与 Review provenance 直接使用
[Report 合同 §3](./docs/REPORT_CONTRACTS.md#3-v21-最小可审计接口)；不能把“新合同生效”偷换成
“所有历史 Weekly 重新全文研究”。

## 5. 完整周发现与分母

未生成的历史 Weekly 使用 `Coverage Mode = Full Replay`，直接执行当前注册表的完整周合同：

```text
Required Daily
+ Required Weekly
+ 当周 Event / Periodic
+ bounded Backstop
```

按公共合同的固定来源组织。每个到期 Source ID 使用
[Source Coverage Receipt §3.2](./docs/REPORT_CONTRACTS.md#32-source-coverage-receipt) 保存收据并按该节闭合；
本 Adapter 不复制 Receipt 状态或 Gate 语义。

Google Scholar、Semantic Scholar 等不可冻结 Backstop 直接使用 Report 合同 §3.2，不在本 Adapter
另定义 Gate 算术或“全网无遗漏”结论。

## 6. 并行研究与单一写入者

多个完整 Week 可以并行执行 discovery、全文阅读和 read-only Source Packet：

```text
Week N discovery / review   ─┐
Week N+1 discovery / review ─┼→ 单一 reconciliation owner
Week N+2 discovery / review ─┘  → owner Weekly → 年度索引 → per-week Review
```

并行执行者不得同时修改 Weekly、年度索引或 Learning State。单一 reconciliation owner 负责：

- first-public / revision / spillback；
- Source Family 与评分 owner 唯一性；
- Weekly 写回与年度索引一致性；
- per-week Coverage / Evidence Gate。

每个子任务只有负责周的 Source Packet 和所有未决项都已显式交给 reconciliation owner 后才能结束。
“已发现候选”或“已写草稿”不算完成；只有串行写入者能声明负责周通过 Gate。

## 7. 证据、叙事选择与语义审阅

使用 [Research 合同 §7](./docs/RESEARCH_CONTRACT.md#7-review-合同) 与
[Report 合同 §3.4～3.7](./docs/REPORT_CONTRACTS.md#34-review-completion-receipt)。Historical 模式的唯一额外约束是：
后续 revision 不能替代事件时版本；如果只能取得后来版本，必须在 evidence version 与
claim boundary 中限定可支持范围。

## 8. Blocked 恢复与 Materials Request

材料恢复和状态组合直接使用 [Report 合同 §8.1](./docs/REPORT_CONTRACTS.md#81-唯一状态与-gate-真值表)
与 [Materials Request §7](./docs/REPORT_CONTRACTS.md#7-materials-request-ledger)。本 Adapter 只规定历史 forward 行为：

用户允许 blocked-skip 时也不改变 Report 合同的状态真值表；只有 §8.1 已允许闭合、且授权与 forward
policy 已记录时，forward cursor 才能继续。其他状态从同一 checkpoint 恢复。

## 9. Books 边界

Historical Weekly 默认只修复证据体系。未明确授权历史 Books Integration 时，冻结 Books 修改，并使用
[Report 合同 §8.1](./docs/REPORT_CONTRACTS.md#81-唯一状态与-gate-真值表) 的 Historical Books 例外；
本 Adapter 不另定义对应 Gate 或 disposition。

若用户另行授权，使用 [Research 合同 §9](./docs/RESEARCH_CONTRACT.md#9-books-gate-与目录外内容)
和 [Books Comparison §3.6](./docs/REPORT_CONTRACTS.md#36-books-comparison)。Weekly 摘要与评分本身不能直接写进 Books。

## 10. 每周验收

每完成一个 Week，使用 [Report 合同 §8.2](./docs/REPORT_CONTRACTS.md#82-完成条件) 进行 per-week 结构验收，
并完成四个 scope 的 Semantic Audit；scope applicability 直接使用 Report 合同 §3.7。只有该合同允许
当前状态移动 forward cursor 时才进入下一周，否则下次从同一 checkpoint 继续。

## 11. 校验与 Git Safety

执行 [Report 合同 §10](./docs/REPORT_CONTRACTS.md#10-校验命令)。命令成功只是结构校验；不得代替每周
Semantic Audit。

不 stage、commit、push，不清理、覆盖或回滚既有 Daily、Weekly、Books 或其他未提交修改。

最终报告必须给出：owner-family 总数、各 Review 路由完成数、ordinary pending、blocked / disputed、材料请求、
变更文件、三个 Gate、校验结果与下一 continuation point；状态含义只引用 Report 合同 §8，不在 Adapter 重述。
