# 2026-05-11 fresh non-author post-write review

- reviewer：未参与本轮作者返修，也未参与 root 的六项 Books 写回。
- scope：当前 V3 Daily、screening ledger、74 条 Evidence、26 条 Books queue、191 条 official basis、六项新增 Books 正文及分层 closure/retained 抽查。
- Gate：**Ongoing**。Books 写后部分通过；screening denominator 语义 Gate 未通过。

## 算术与集合

- 当前文件内算术：`826 = 74 retained + 561 pre-denominator direct closure + 191 owner-day isolation`。
- isolation 分解：`191 = 190 owner_event_recovery_closed + 1 official_withdrawal_closed`；withdrawal 为 `2605.07267`。
- 当前 Evidence：74 条、Source Family 与 retained identity 一一对应且无重复。
- 当前 Books disposition：`74 = 26 Integrate + 46 No Change — Existing Coverage + 2 仅报告`。
- 当前 Books queue：26 条、全部已写入；marker/binding 结构检查为 26/26 通过。

这些数字证明当前投影内部一致，不证明 `74/561` 的语义分类正确。closure 抽查已找到明确 false negative，因此该算术不能冻结为完成态。

## Books 写后审查

六项新增 `2605.06672`、`2605.06708`、`2605.07134`、`2605.07182`、`2605.07260`、`2605.07313` 均完成 exact-v1 采用命题与正文对读。每项 marker 成对且唯一、位于首个 `## Review notes` 前；正文不是 marker-only，而是同时承载旧方案、约束变化、state/control ownership、证据边界、trade-off、failure mode、fallback，并与相邻段自然衔接。

其余 20 个 Integrate 中，分层抽查 `2605.06733`、`2605.06919`、`2605.07063`、`2605.07490`、`2605.07686`、`2605.07701`、`2605.07769`、`2605.07881`、`2605.07937`、`2605.08060`，未发现 owner、证据边界或论证链缺失。其余 10 条沿用此前 fresh review 结论，并重新通过 26/26 marker/binding 结构检查。

机械性 Evidence 修复两项：`2605.06672` 的 exact-v1 实际声明 code/data 已发布，现改为“未取得不可变 repository URL/commit，故不采用 reproduction claim”；`2605.07260` 的 evaluation locator 收窄为 §3.2–§3.3、§5.2、Table 2–5、Figure 3，不再把 Related Work 当 evaluation。

## Retained 与 isolation 抽查

对 No Change / 仅报告按 evaluation、memory、security、training、inference、multimodal 等 owner 分层抽查，未发现 retained false positive；现有 26/46/2 是当前 74 条内部的正确处置计数。

191 条 official basis 的 identity、v1/current version、submission history、Comments 与 owner-day interpretation 均可解析。除区间样本外，逐项复核六个 later-event signal `2605.06738`、`2605.06772`、`2605.07210`、`2605.07527`、`2605.07818`、`2605.08051` 和 withdrawal `2605.07267`；它们的 isolation / 后续 owner 路由成立。前版 11 个 retained identity 因 v1 submission provenance 转为 owner-day isolation，本轮也未把它们误算成 direct false negative。

## 阻塞项：direct closure false negative

当前 direct closure 为所有排除项生成了相同结构的 generic reason。抽查发现 18 项题摘已明确给出长期机制、适用边界或评价有效性变化，仍被错误关闭；另有 10 项前版 direct retained identity 在没有命题级改判理由时回归同一模板 closure。精确集合与最小贡献理由见 `V3_FRESH_NONAUTHOR_SCREENING_REPAIR_QUEUE_20260915.md`。

因此 `826` 总 identity 数仍可使用，但 `74 retained + 561 direct closure` 不得作为终态。仅 A 组确定 false negative 重开后，retained 已至少为 92、direct closure 至多为 543；B 组 10 项还需逐项恢复或提供可审计的具体改判理由。当前不得签 Complete，也不得据此写新的 Books 语义增量。

## 结论

- Books writeback：Passed。
- Evidence/Books current-74 internal accounting：Passed。
- owner-day isolation：Passed（限当前 191 项官方依据与本轮抽查范围）。
- screening denominator：Failed。
- final Gate：**Ongoing**。

本 reviewer 仅修复状态投影与证据 locator，并写入精确有界 screening repair queue；未修改 Books，未 stage、commit 或 push。

