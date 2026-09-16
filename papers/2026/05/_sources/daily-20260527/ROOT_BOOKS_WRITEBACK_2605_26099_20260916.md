# 2026-05-27 Root Books Writeback Receipt — 2605.26099

- Source Family: `SF-2026-ARXIV-2605-26099`
- Owner: `MODEL-LONG-CONTEXT`
- Target: `books/part-02-model/22-long-context.md`
- Binding: `semantic-body-binding:SF-2026-ARXIV-2605-26099`
- Status: root writeback complete; fresh non-author post-write review pending

正文把 online fast-weight update 推进为一个有界 offline consolidation 分支：冻结 recent context 与 fast-state version，按预算执行多轮 recurrence，以质量/一致性 Gate 原子提交新 state，并把 KV clear 放在 commit 之后。正文同时保留证据只覆盖 exact-v1 的 hybrid attention/SSM 与受控任务，不外推多租户、迁移或生产 tail SLO；失败时保留旧 state 和 KV，并回退 full/sliding attention、普通 recurrent update 或外部检索。
