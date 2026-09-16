# 2026-05-06 非作者独立 Gate

## 审计范围

- Raw identities：493。
- Candidate Denominator：137。
- Pre-denominator closure：356。
- exact-v1 evidence：137/137（135 HTML；2 PDF）。
- 独立重评分：137/137。
- Books 命题级对读：137/137。
- Review Pending：0。
- Material Blocked：0。

## 发现与修复

### 1. Score V2 曾由处置状态机械生成

旧作者脚本用 `Integrate/APPLIED/PROPOSED` 推导 Design Delta，用 owner 前缀推导 System Reach，用 review route 推导 Durability。这违反三维分数相互独立的合同。

本轮逐项重评后：

| Total | 修复前 | 修复后 |
| --- | ---: | ---: |
| 5 | 61 | 53 |
| 6 | 0 | 25 |
| 7 | 18 | 42 |
| 8 | 50 | 15 |
| 9 | 8 | 2 |

63/137 项至少一个维度发生变化；按分数要求的 Deep 路径从 76 项收紧为 59 项。完整 before/after 位于 `NONAUTHOR_SCORE_RECALIBRATION.json`。分数只表达长期设计变化、系统触达范围和耐久性，不再表达“作者是否想写 Books”。

### 2. Evidence locator 截断过短

旧脚本只保留 heading 后 7 个词，无法证明 Method、Evaluation 与 limitation 已被真正辨认。当前活动证据包将定位片段扩展到 40 个词，并为重点写回项修正 Method/Evaluation heading override。它仍是 locator，不替代原文；最终 Books 只使用写回队列中明确的受限结论。

### 3. Books 写回建议过宽

作者初判的 24 个新写回建议，经对读 canonical owner 与相邻交接后保留 10 个，14 个降为具体命题级 Existing Coverage。最终分布为：12 项既有实体、10 项新增写回、115 项 Existing Coverage。精确 root 队列位于 `NONAUTHOR_BOOKS_RECONCILIATION.md`。

### 4. Withdrawal chain

`2605.03562` 已从活动 candidate、score 与正向 Books decision 移除，记为 withdrawal terminal closure。旧重建包中仍有 superseded 的历史正向记录，仅用于解释为何曾提出写入；它们不再是活动 evidence。当前 Books 已无该 ID、Source Family、HeadQ 名称或其特有 side-code 结论；Ch45 的通用 attention-distortion 原则由其他来源支持，不应删除。post-write 搜索已复算并关闭撤回项。为防止旧链被误运行恢复，旧 TSV 的正向行已改为 terminal closure，旧构建脚本已 fail-closed。

## Gate 判定

- Coverage Gate：Pass。
- Candidate Denominator Gate：Pass。
- Evidence Review Gate：Pass（137/137；无材料阻塞）。
- Score Gate：Pass（137/137 已独立重评；总分算术一致）。
- Pre-write Books Decision Gate：Pass（137/137 命题级对读）。
- Books Apply Gate：Pass（10 个新写回均已在 canonical owner 主干落地；12 个既有实体回读通过；withdrawal 不变量已复算）。
- Post-write Independent Gate：Pass（10/10 owner、证据边界、演进主线、相邻衔接与 marker 唯一性通过）。
- Daily Complete：**Yes**。

Post-write 复核没有发现需要再次修改共享 Books 的问题。
