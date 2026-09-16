# 2026-05-23 Root Books Writeback：VeOmni 事件

**状态：** 两项共享 Books 写回已由 root 串行完成，并通过 fresh non-author 写后语义复核。

## 写回范围

- `SF-2026-BYTEDANCE-VEOMNI-PR-779` → `TRAIN-MEGATRON`：把 variable-length/window-attention metadata 从 device forward 前移到 host producer，明确 versioned producer/consumer contract、exact-logit Gate 与 device-side fallback。
- `SF-2026-BYTEDANCE-VEOMNI-PR-781` → `TRAIN-ZERO`：区分 HSDP shard-dimension reduce-scatter 与 replica-dimension all-reduce，明确 gradient-accumulation final boundary、group/reduction identity 和完整同步 fallback。

两项均只采用相应 PR、merge commit 和披露测试能够支持的机制命题。正文没有采用通用性能提升结论；未披露的端到端时间、CPU 成本、多节点规模、硬件、重复方差与收敛质量均保留为 evidence boundary。

## 验收结果

fresh non-author 已确认两项事件落在严格窗口，准入不是普通修复扩池；正文机制、代价、failure/fallback、ROADMAP owner、相邻衔接、唯一成对 marker 及日报 Candidate/Evidence/Books 对账均通过。完整收据见 [`V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260916.md`](./V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260916.md)。
