# 04/22 两项 Ch24 Books 实际写后非作者复核（2026-09-28）

复核者 root。复核对象仅为 `2604.19079v1` 与 `2604.19330v1` 的 exact-v1 来源、当前 Ch24 实际正文及相邻论证；不代替 04/22 的整日 Gate，未复现实验。

| 来源与 owner | 写后裁决 | 证据边界与衔接 |
| --- | --- | --- |
| [`2604.19079v1`](https://arxiv.org/html/2604.19079v1)，`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 | PASS | 在 CTC 重排/位置融合之后追问离线与流式使用同一 RNNT 时的监督对象，接续自然。正文明确最终 `(t,u)` 完整词表分布，而非辅助 CTC；双模式前向、现场 loss/recompute、短右视野退步、理论 `C+R` 不等于在线 tail SLO 均保留。XL 训练小时的表格/正文不一致未合并为受控收益，旧分支仍在。 |
| [`2604.19330v1`](https://arxiv.org/html/2604.19330v1)，同一 Ch24 | PASS | 正文区分同一时间位置的 RVQ residual codebook 与跨时间分辨率的降采样首 codebook 链，并接到 masked refinement；总时长仍由 G2P 和 duration predictor 估计。逐级成本、错误传播、有限英文实验和 SeedTTS 局部退步均未扩写成普适吞吐或首包结论，短音频/成本敏感的旧路径保留。 |

两项实际正文分别位于 Ch24 约 333–335、348–350 行；`Review notes` 保留 exact-v1、实验证据与未披露条件。已对 Ch24 执行 scoped `git diff --check`，无行尾/patch 格式问题。此处 PASS 仅允许对应的 Books 实际写后状态进入 04/22 Daily；其余候选、日期归属、完整分母和整日独立语义复核仍须由 04/22 owner 继续。
