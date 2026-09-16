# 2026-05-25 root Books writeback receipt

- 状态：root 串行写回已完成；等待未参与作者修复与本次写回的 fresh non-author 终审。
- 队列：31/31 actions applied。
- 新增长期命题：27 项，均使用唯一 `semantic-body-binding` 成对 marker，位于目标章节首个 `## Review notes` 之前。
- binding-only 修复：2 项（`2605.22949`、`2605.23893`），只校正来源与既有命题的绑定范围，不改变正文结论。
- evidence quarantine：2 项（`2605.22834`、`2605.23857`），因 exact-v1 正文无法独立回放，已从稳定机制正文移除正面命题与 marker；材料恢复前不作 Books 证据。
- 作者侧校验：31 项目标均存在预期 marker 状态；新增/修复 marker 唯一且顺序正确；隔离 marker 不存在；scoped `git diff --check` 通过。

本收据只证明物理写回及作者侧结构校验，不替代 fresh-context 对来源边界、章节语义、trade-off、failure/fallback 与相邻交接的独立复核，也不签署 Daily Complete。
