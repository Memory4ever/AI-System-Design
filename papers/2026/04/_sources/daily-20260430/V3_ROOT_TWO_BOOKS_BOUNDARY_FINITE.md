# 2026-04-30：26340 / 26505 非作者 Books 边界复核

复核者：root；2026-09-29。仅核官方 exact-v1 的必要机制与真实目标章节，不替代日期、来源或整日日级 Gate。

## 2604.26340v1 — DMEP：现有章节仍有窄缺口

[原文 §III-C–E/Algorithm 1、§IV](https://arxiv.org/html/2604.26340v1) 的三阶段是：均匀 LoRA-MoE 探索时累计实际 Top-k 路由；在逐 module 利用率和最小存活数约束下，一次性**物理删除** expert、optimizer moments 并重索引 gate；随后将 balancing loss 系数置零，仅用任务目标继续训练。正文说路由稳定，印刷 Algorithm 1 则在固定 warm-up epoch 后裁剪，不提供经验证的在线 drift stop rule。Table I 的吞吐属于后阶段，不是包括探索/裁剪在内的端到端成本。

[Ch30 原 adapter 条件容量段](../../../../../books/part-04-training-system/30-lora.md)已经讨论逐 module evidence、可回滚 mask、最小 expert floor 与质量 replay，所以不用另起一章或重复背景。但它没有清楚交代论文与可回滚 mask 不同的**训练状态迁移**：physical slicing 不仅改 forward，还改变 optimizer-state identity；关闭 balancing loss 是另一个独立的更新目标选择。其原先仅一句 `semantic-body-binding` 也不能代替这个机制。故 `Existing Coverage` 不充分，应为窄 `Integrate`。作者现已在 Ch30 主线中补出两分支的条件、代价和回退边界；非作者写后复核见[独立记录](V3_ROOT_26340_CH30_WRITE_AFTER.md)。不得写成论文证明可无损恢复被删除 expert；可回滚 mask 是工程上另一条旧路。

## 2604.26505v1 — 动态量化侧信道：已有具体正文

[原文 §3–6](https://arxiv.org/html/2604.26505v1) 的机制是同一 batch 的 per-tensor 动态 scale 由多条请求共同决定，victim 输入因此改变 attacker 的量化误差和可观察 logits。实验需要 co-location、模型/量化配置、top-1 log probability 观察；batch=2 的小模型结果不外推生产利用率或现实可攻击性。

[Ch72「Runtime 优化统计也可能成为跨租户共享状态」](../../../../../books/part-06-ai-infrastructure/72-security.md)已明确共享 scale→输出 side channel、scale granularity/batch composition/tenant boundary 身份、per-token/static 或 batch 隔离、logit access 前提以及单租户旧 fast path。这个可迁移判断和成本/回退已经在正文，不需再写相同机制。`Existing Coverage` 只指此长期命题，不称论文所有攻击设置都被书稿复现。

以上是两项 Books Decision 的有限复核；26340 的真实正文和非作者写后核已通过，26505 的已有覆盖可直接用于本日处置。两项均不能据此宣称 04/30 Daily Complete。
