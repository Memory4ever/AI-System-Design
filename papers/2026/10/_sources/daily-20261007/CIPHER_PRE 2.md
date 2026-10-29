# CIPHER-MoE — exact Books PRE request

Author oct07_missing; independent necessary Source/date/score6 and concrete owner by oct11_missing in READER_REVIEW.md. Actual Ch21 routing/load-balance/capacity/All-to-All handoff and Ch20/22 handoffs read. Unique owner MODEL-MOE. Insert after paragraph `当 token 超出 capacity...` and before `## Expert Parallelism 为什么需要 All-to-All`. Current four overflow choices stay intact. Not yet written.

Exact proposed single paragraph:

Capacity admission 也可以放在 token-side Top-K 之后：先保留 router 的候选选择，再由每个 expert 按 token affinity、阈值和 microbatch 容量筛选 assignments；strict 分支清零被拒贡献，reroute 分支则尝试仍有容量且满足阈值的其他 expert，shared experts 与 token 本身的序列/loss 位置不随之删除。因而“Top-K 不变”不能解释为实际 expert 贡献集合或梯度不变。[CIPHER-MoE 的受限训练对照](https://arxiv.org/html/2610.05744v1#S3)支持这一执行分支，但其条件保留定理及固定 expert-output 的局部界不保证整个训练无损；strict 有任务与平均质量反退，V4-Pro 原 baseline OOM 也不能生成有限加速倍数。Affinity 排序、过滤/重路由、辅助 loss 和通信都需计费，capacity、训练人口及 quality regression 随模型绑定；失败时保留原路由、更宽容量或经核的固定分支，不由负载变平签发质量保持。<!-- source-family:SF-2026-ARXIV-2610-05744 -->

Proposed own source note: Daily2026-10-07 Oct6; exact-v1 §3–4/T1–3/A4.4/A5T8 necessary;2+2+2=6; strict/reroute and executed-contribution boundary only; preserve theorem assumptions, quality regressions, Pro OOM/no finite speedup and hardware/precision Not Disclosed; no artifact/reproduction. Non-author Source passed; PRE/actual POST separate.

