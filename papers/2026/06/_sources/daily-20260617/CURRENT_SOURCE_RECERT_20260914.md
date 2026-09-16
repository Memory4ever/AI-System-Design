# Current-contract source recertification — 2026-06-17

- Window: `2026-06-16T09:00:00+08:00`–`2026-06-17T09:00:00+08:00`
- Accessed: `2026-09-14`

All thirteen official Daily sources were rechecked. Anthropic's June 16 coding-usage study is closed before the denominator because it is observational adoption/labor evidence, not a durable AI-system mechanism. Z.ai's official [GLM-5.2 research page](https://www.zhipuai.cn/zh/research/161) provides the exact timestamp `2026/06/16 16:00`, so it belongs to this window and is admitted as a distinct official-source candidate.

GLM-5.2 discloses an `IndexShare` design that reuses one query-aware indexer across four sparse-attention layers, plus improved MTP and long-context claims. The durable contribution is the selector-state reuse boundary; vendor performance claims remain bound to its model/configuration because complete hardware, precision, length, batch, concurrency, and SLO conditions are not disclosed. Candidate score: Design Delta `3`, System Reach `3`, Durability `2`, Total `8`. Evidence level: creator-primary technical page; mechanism disclosed, implementation and benchmark contract incomplete. Books decision: `No Change — Existing Coverage`, owner `MODEL-LONG-CONTEXT`; the Ch22 body section “Sparse Attention 的两个 ownership 轴” already defines selector refresh ownership, cross-layer reuse scope, stale-selection/head-imbalance failure modes, and fallback to a narrower reuse boundary.

Result: official-source delta `1 Candidate`; no Books write is required. The old candidate-table labels saying “待 root 串行写回” were separately reconciled against actual Review-notes-before body anchors and must not be treated as a new Books queue.
