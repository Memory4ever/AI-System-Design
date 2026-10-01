# FG²-GDN `2604.19021v1` Books 实际写后非作者复核

复核者 root，2026-09-28。依据[官方 exact-v1](https://arxiv.org/html/2604.19021v1) §3.2–3.5、§4/Tables1–4 对读 Ch22 约 244–246 行、前后 GDN/混合预算/在线 ridge/GDN-2 的过渡和章末 Review note；`git diff --check -- books/part-02-model/22-long-context.md` 通过。未复现实验，不代替 04/22 整日 Gate。

**PASS。** 正文没有把非对称左乘 rank-one 错写为失去低秩，而明确指出失去原对称 `uuᵀ` generalized-Householder/WY lowering；双边 `sqrt(β)` 后仍保持受限 chunk 形式，`β^k/β^v` 的独立擦除/写入是条件扩展。训练内状态修改与 Adam 二阶 optimizer 未混同。现有 scalar GDN、KDA 和需要逐字回看的 Attention 继续共存；Table4 单独向量 β LongBench 16.0 低于 KDA 16.4，H800 BF16/固定 token 的 prefill 结果未扩写为任意 SLO。Ch22 的前后交接通畅。

本裁决只允许该 Source Family 的实际 Books 决策计入 04/22；其他候选、日期、分母及日级独立复核仍须继续。
