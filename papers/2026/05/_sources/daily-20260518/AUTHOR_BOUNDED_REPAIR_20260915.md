# 2026-05-18 作者有界返修（2026-09-15）

**状态：Ongoing；作者不得自签 Complete。**

本次只处理 fresh non-author V3 终审列出的 owner-time、18 个 FN/signal、3 个 FP/score 与 38 个 reuse locator；未扩窗、扩源或重扫 537 条题摘。

## 冻结算术

- owner inventory：`537 = 64 retained + 473 pre-denominator closure + 0 withdrawn`。
- Evidence：`64 = 31 current exact-v1 + 33 replayable historical exact-v1`；原 38 reuse 的处置为 `33 historical replay + 3 current exact-v1 recheck + 2 removed candidates`。
- Books Decision：`64 = 31 Integrate + 33 No Change — Existing Coverage`。
- root queue：31 项，仅列真实 `Integrate`；作者侧未修改共享 Books。

## 有界重审

18 个审计指定 FN/signal 均重新读取完整题名与摘要，并以合同的贡献问题逐项判定；18 项均有题摘直接支持的机制、适用边界、评价纠错或设计分支，故进入 denominator。其 score、exact-v1 locator 与 Books 对读见本目录三个 V3 冻结 JSON。

`2605.15638` 移出分母：唯一 Books binding 为 `books/part-06-ai-infrastructure/67-monitoring.md:397`，唯一由该 source family 支撑的正文是当前第 393 与 395 段；root 必须删除或改写这两段并移除 binding，作者没有改 Books。`2605.16194` 同样移出分母。`2605.15734` 保留但降为 `2+1+2=5`，执行标准审阅并维持 Existing Coverage。

## 材料限制

无阻断本次判断的材料缺口。38 项均有可重放历史 locator/version/claim，或已完成当前 official exact-v1 定点复核；批量 current-abstract 状态探测中 `2605.15508`、`2605.15665`、`2605.15694`、`2605.16035`、`2605.16255`、`2605.15215` 曾超时，但这些探测不用于采用命题，immutable exact-v1 与历史 receipt 均可重放，因此未静默阻塞。

## 剩余外部动作

root 执行 31 项 Books queue，并删除/修订 ITHICA 唯一正文 binding；之后必须由非作者重新核对 owner-time、18 项准入、Evidence replay 和实际 Books 承载。机器校验通过不能替代该复核。
