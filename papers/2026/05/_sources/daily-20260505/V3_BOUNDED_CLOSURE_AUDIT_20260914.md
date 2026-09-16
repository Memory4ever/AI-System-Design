# 2026-05-05 V3 同类 Closure 有界复核

**目的：** 检查“以局部方法/应用为由关闭，但题摘已经改变 state/data/control/evaluation choice”的同类错误；不是重新扫描 1058 项，也不扩大到其他日期。

## 范围与结果

| 分层 | 点名复核 | 结果 |
| --- | --- | --- |
| VLA runtime / embodied control | `2605.00884`、`2605.01191`、`2605.01772`、`2605.02525`、`2605.02697` | 5 项全部恢复；4 项 No Change，`2605.01772` 进入 Books 写回队列 |
| Multimodal representation / world-model data | `2605.01345`、`2605.01799`、`2605.01896`、`2605.02757` | 4 项全部恢复；3 项 No Change，`2605.01345` 进入 Books 写回队列 |
| RAG / Tool action-space state | `2605.01302`、`2605.02411` | 2 项全部恢复并进入 Books 写回队列 |
| Agent RL / generative state | `2605.02178`、`2605.02263` | 2 项全部恢复并进入 Books 写回队列 |
| VLM inference / data interface | `2605.01948`、`2605.02262` | 2 项恢复，完成 Evidence Review 后均为 No Change |
| Evaluation anti-case | `2605.02443` | 与 Ch66 显式比较后维持分母前关闭 |
| 终审确认的具体 closure 对照 | `2605.01214`、`2605.01280`、`2605.02163` | position framing 或单一文档维护组合，没有可核验、可迁移的 state/data/control/evaluation contract 增量，维持关闭 |

新分母为 `1058 raw = 138 retained + 920 closure`。相对终审前 `123 + 935`，恢复 15 项；`2605.02443` 只重写为具体 anti-case closure，没有进入分母。没有删除既有证据。

15 个恢复项均保留唯一 arXiv ID / Source Family、完整题名与摘要、北京时间 owner window、ROADMAP owner、exact-v1 审阅状态和撤回检查；截至 2026-09-14 的 exact-v1 审阅未观察到官方 withdrawal notice。该检查不承诺未来版本不会被撤回，后续出现官方撤回时仍按合同清理。

## 关闭错误的公共修复

这批错误不是“模型/机器人论文都应准入”，而是原 closure 只判断题目像不像局部方法，没有继续问方法是否重分配了状态、数据、控制或评价权。修复只采用一个判据：

```text
题名 + 完整摘要提出的可核验机制
→ 是否改变 state / data / control / evaluation choice
→ 是：进入候选分母后再做 Evidence 与 Books Review
→ 否：写出 family-specific closure 与重开条件
```

准入不等于 Books Integration。恢复后的 15 项中，6 项暴露现有 Books 命题缺口，root 已按结构化队列完成写回并由作者侧回读 marker 与相邻交接；9 项经全文和逐命题比较得到 `No Change`。这一分离避免用“书里已有类似主题”在 Evidence Review 前关闭来源，也避免为每个相关案例强行修改 Books。

本次 bounded audit 覆盖终审点名的 10 个确定漏项、5 个边界项、同理由簇的 3 个有效 closure 对照以及 1 个 Evaluation anti-case，共 19 个 family。它验证的是受影响理由簇，不代表对 920 个 closure 重新做了全量扫描；新的独立 reviewer 仍需对该分层抽样范围与修复结果作反证。

## Gate

- Candidate denominator：作者侧重新冻结；仍待独立 reviewer 反证。
- Evidence：136 个可访问候选作者侧完成，2 个 exact-v1 blocked 保持隔离。
- Books：24 个既有 Applied 保持，6 个新增项已写回并完成作者侧 marker/交接回读；共 30 个 Applied 待新非作者写后语义复核。
- Daily：进行中；新独立复核完成前不得标为 Complete。
