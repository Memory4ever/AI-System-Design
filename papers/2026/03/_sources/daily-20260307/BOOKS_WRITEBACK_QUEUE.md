# Books Writeback Queue — 2026-03-07

Status: partially applied; root final reconciliation and post-write Books audit remain open.

## SF-2026-ARXIV-2603-04851

- Writeback: applied to `TRAIN-RLHF`; marker `source-family:SF-2026-ARXIV-2603-04851`; post-write audit pending.

- Primary: `arXiv:2603.04851v1`
- Exact source: https://arxiv.org/html/2603.04851v1
- Stable Node: `TRAIN-RLHF`
- Target: `books/part-04-training-system/31-rlhf.md#Harm Horizon：Sequence Reward 的 Gradient 可能天然局部 (line 244)`
- Adjacent: `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`
- Existing proposition: Reward Model 通常在完整 response 后给出 scalar，而 policy 逐 token 生成；sequence outcome 本身不能指出哪个 token 导致好坏，长序列、稀疏 reward 与延迟反馈会放大 credit-assignment 方差。
- Proposed mechanism: 论文以序列 harm 的 martingale/协方差分解刻画 gradient，使 alignment locality 成为可分析的 objective property。
- Evidence boundary: 只接受 arXiv:2603.04851v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。

## SF-2026-ARXIV-2603-05353

- Writeback: applied to `INFER-KV-CACHE`; marker `source-family:SF-2026-ARXIV-2603-05353`; post-write audit pending.

- Primary: `arXiv:2603.05353v1`
- Exact source: https://arxiv.org/html/2603.05353v1
- Stable Node: `INFER-KV-CACHE`
- Target: `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#Structured knowledge 只有进入 physical access plan 才改变 KV 成本 (line 152)`
- Adjacent: `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`
- Existing proposition: 逻辑 prompt 保持不变时，physical-read optimization 可以只读取计划区域，但 access plan 必须绑定模型、tokenization、KV layout 与 knowledge revision；依赖不确定或验证失败时应回退 full context。
- Proposed mechanism: InfoFlow KV 根据跨 token 信息流选择需要重算的局部状态，使缓存复用和因果修复共享一个选择 contract。
- Evidence boundary: 只接受 arXiv:2603.05353v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
