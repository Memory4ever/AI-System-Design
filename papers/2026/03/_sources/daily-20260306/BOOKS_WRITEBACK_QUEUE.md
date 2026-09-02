# Books Writeback Queue — 2026-03-06

Status: applied; root final reconciliation and post-write Books audit remain open.

## SF-2026-ARXIV-2603-03491

- Writeback: applied to `PLATFORM-PRODUCTION`; marker `source-family:SF-2026-ARXIV-2603-03491`; post-write audit pending.

- Primary: `arXiv:2603.03491v1`
- Exact source: https://arxiv.org/html/2603.03491v1
- Stable Node: `PLATFORM-PRODUCTION`
- Target: `books/part-06-ai-infrastructure/73-production-best-practice.md#硬件 Variation 要跨 Device、Runtime 与 Training 共同闭环 (line 127)`
- Adjacent: `books/part-06-ai-infrastructure/72-security.md#本章要回答的问题 (line 10); books/part-07-agent/74-prompt.md#本章要回答的问题 (line 10)`
- Existing proposition: Demo 只证明受控条件下的可能性；生产发布必须把 identity、quality、capacity、reliability、governance、economics 与 evolution 的隐含假设转成有 owner、evidence、failure policy 和 rollback path 的证明责任。
- Proposed mechanism: 论文结合 selective write-verify 与 right-censored noise learning，在硬件写入和训练层分别控制变异传播。
- Evidence boundary: 只接受 arXiv:2603.03491v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
