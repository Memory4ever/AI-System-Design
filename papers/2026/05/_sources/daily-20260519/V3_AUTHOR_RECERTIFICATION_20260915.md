# 2026-05-19 V3 作者侧有界再认证

- 窗口：`[2026-05-18T09:00:00+08:00, 2026-05-19T09:00:00+08:00)`。
- owner：arXiv official 2026-05-18 20:00 EDT announcement batch，即 2026-05-19 08:00 北京；`2605.16259`–`2605.18754` 共 1348 identities。DataCite 只作 identity/DOI 佐证。
- 受影响集合：36/36；`26 restored + 10 proposition-level closures`。
- FP 校准：19/19 已重读题名与完整摘要，0 项移出。
- 冻结算术：`1348 = 172 retained + 1176 closures + 0 withdrawn`；closure 包含 1175 个语义关闭与 1 个 Charon earlier-owner duplicate。
- Evidence：26 个恢复项全部完成 exact-v1 locator、evaluation、counterevidence 与 claim-boundary 复核；既有 146 项保留既有可重放 Evidence，不在本轮重扫。
- Books：`172 = 57 Integrate + 115 No Change`；本轮 delta 为 9 Integrate + 17 No Change。9 项仅进入 root queue，作者未写共享 Books。
- Daily 来源：14/14 有界处理；13 个机构来源没有新增达到门槛的窗内事件。Meta GIM 由 arXiv official batch 归属后在题名+摘要层关闭。
- blocker：当前 Atom/OAI 对 1348 项 withdrawal/status 全页 refresh 返回 HTTP 429/connection reset；保存的 2026-09-03 official receipt 记录 withdrawn=0，但不能冒充 2026-09-15 状态刷新。
- 作者检查点状态：当时为 Ongoing，作者没有自签 Complete。其后 root Books 写回和 fresh non-author review 已完成，当前终态由 `V3_FRESH_NONAUTHOR_FINAL_GATE_REVIEW_20260915.md` 记录为 Complete。

结构化真值见 `author-v3-recertification-20260915.json`；root 只执行了 `root-books-writeback-queue-v3-20260915.json` 的 9 项，最终独立验收见 `V3_FRESH_NONAUTHOR_FINAL_GATE_REVIEW_20260915.md`。
