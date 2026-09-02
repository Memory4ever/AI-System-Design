# Books Writeback Queue — 2026-03-24

**Status:** Pending root serial writeback and fresh-context prewrite audit. 本文件不证明 Books 已修改。

| Source Family | Exact Source | Stable Node | Target | Adjacent | Existing Proposition | Proposed Durable Mechanism | Evidence Boundary | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-21177 | arXiv:2603.21177v1 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md | books/part-04-training-system/32-ppo.md; books/part-04-training-system/34-dpo.md | 本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。 | 方法只重放近期产生高方差/高信号 group outcome 的 prompt，再用当前 policy 重新 rollout，而不是复用旧 trajectory。 | 只支持 arXiv:2603.21177v1 §Appendix B Algorithm 的机制与 §5.1 Main Results 的公开 workload；§6.2 Limitations & Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 | applied_postwrite_verified |
