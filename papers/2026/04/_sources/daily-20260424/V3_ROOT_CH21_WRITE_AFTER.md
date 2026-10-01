# 04/24 Ch21 21330 实际写后有限复核

复核者 root，非 04/24 报告与 Ch21 本次改动的作者。已重读官方 [2604.21330v1](https://arxiv.org/html/2604.21330v1) §3 的 teacher/router 分工，与 `V3_APR02_FOUR_21327_21343_INDEPENDENT.md` 的写前边界对照，并顺读 Ch21 当前负载辅助代理、计算价值 teacher、此次两段以及后续 global/local balance。

**结论：通过这两段的实际写后复核。** 正文区分 frozen dense feature backbone 与仍训练的辅助 router；student 接受停止梯度的分布监督，不把 load/entropy proxy 写成语义真值。与前文未来策略价值 teacher 和后文 step/microbatch 负载约束是不同责任。保留末层指导、仅模仿、指导时长的反向结果及视觉实验/teacher 成本边界；没有把所测视觉模型外推为任意 LLM MoE 或生产吞吐。Review note 已改为真实写后状态，`git diff --check` 对本章通过。

本复核不验收 04/24 其他候选、来源日期、报告分母或日级 Gate；未复现实验。
