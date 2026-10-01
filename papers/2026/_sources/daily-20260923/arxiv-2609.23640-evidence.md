# `2609.23640v1` — 人类偏好不等于人类行为分布

- 身份与日期：[arXiv 摘要及版本页](https://arxiv.org/abs/2609.23640)、[exact-v1 HTML](https://arxiv.org/html/2609.23640v1)，访问 2026-09-23。官方 09-22 New 批次进入本日报；HTML 的 09-20 是投稿标记，不是首公证明。未核更早作者渠道。
- 问题与旧方案：偏好比较比逐题写唯一标准答案更容易标注，助手也不必模仿普通人的回答；但当模型被拿去模拟人群时，“人更喜欢这个回答”与“人会给出这个回答”是两个不同统计目标。旧 RLHF 用 reward+reference KL 仍适合优化助手效用。
- 机制与条件：人写回答分布为 `p_H`，人对候选的偏好奖励为 `r_P`；KL 正则的理想最优 `pi* ∝ pi_ref exp(r_P/beta)`。若 `pi_ref=p_H`，非恒定奖励会使输出分布离开 `p_H`；若 reference 原本不同，只有奖励等于 `beta log(p_H/pi_ref)+c(x)` 且支持集兼容才可精确恢复。该推导描述目标冲突，不证明所有实际训练都收敛到该最优。
- 评价与限制：作者比较同一批 human-written SHP/StackExchange responses 的等权 imitation 与偏好加权，另做 DPO；Qwen/Llama 与所列偏好数据中，提升 preference fit 通常降低 held-out human response likelihood，但从未拟合人写回答的起点训练可被 human data gain 部分抵消。Human-response likelihood 与生成分布需要单独量；估计 `p_H`、样本代表性、文化/任务切片和 impersonation 风险均未由本文消除。人类相似度不是通用助手的默认目标。
- Books Decision：`TRAIN-RLHF` Ch31 原已说明偏好优化重写分布，但未把“喜欢助手写什么”与“人自己会写什么”的两种监督目标及精确条件显式分开。正文在 KL/分布重写主线中补齐条件和应用边界。V2 Design Delta 2、System Reach 1、Durability 3，合计 6/9；独立写后复核通过。本笔记只验收单项，整日报状态以日报为准。
