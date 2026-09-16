# 2026-05-22 Root Books Writeback — RefusalBench

- Writer: root（serialized Books owner）
- Source Family: `SF-2026-ARXIV-2605-21545`
- Stable owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Status: Applied；等待 fresh non-author post-write semantic review

在“Response Rate、条件质量与无条件质量不能互相替代”的现有演进链中，新增 refusal evaluation 的同构边界：aggregate refusal rate 不能独自代表安全；需要 matched risk tiers、should-refuse controls、partial-compliance 内容分析，以及 access-path identity。正文同时保留专家标注、judge、adversarial coverage 的成本和 `Unknown` / deterministic policy / human review fallback。

Root 已检查 paired marker 唯一、正文位于主 `Review notes` 前，并保留 exact-v1 的 biology prompt 与 evaluation snapshot 边界。本收据不构成最终 Gate。
