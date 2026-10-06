# 2601.09236v1 — ordinal reward loss 的有限理论/实测贡献

[精确HTML](https://arxiv.org/html/2601.09236v1)。实际§3–6、A.2.2、A.4/B.1及C.4/C.5；关键原文PRIMARY_09236_CORE.md。2+1+2=5，不因控制任务排除：直接处理从人类离散rating拟合reward的监督目标，挑战固定类别数值区间使同类return收缩到midpoint的假设，不是语言系统类比。无LLM实验，不授语言模型奖励改进；root必要核心/owner及实际两段POST通过，整合TRAIN-RLHF，日期/日级Gate未授。

每类采一个trajectory，预测discounted return→differentiable rank→与ordinal class的MSE。仅约束cross-class ordering、不强迫同类相同return。主理论假设 deterministic reward、真实returns不重叠bin、hypothesis realizability、ranking exactness；结论是可行order-compatible reward解集，不恢复唯一真实reward，不证明policy最优。A.2.2为逐跨类tuple论证，有限minibatch拟合不自动授全数据pairs契约。A.4示例soft-rank为1..10，理论class/rank0..n-1；例正文又用1/2/3，偏移实现未说明。C.5实际rank regularization1，而A.4展示.01，不能把样例当训练exactness证明。软rank局部exact时可近hard ranking且梯度不保证充分；未据此否定全部经验结果。relaxed theorem未作为采用保证，不展开无关证明。

Offline三Gym任务（Reacher/DoublePendulum/HalfCheetah）静态balanced模拟GT反馈，同reward-training过程对RbRL、环境reward；未见seed上学policy，5seed，作者t-testα.05。RewardMLP1层10或100hidden、ReLU，15000/3000/1000updates，batch64，SAC batch256 lr3e-4 discount.99。Online六DMC任务，SAC；同反馈budget却rating计一条/ preference计pair两条，不是等人工看trajectory成本；不同默认schedule/sampling取各最强配置，R4dynamic schedule+50近期trajectory stratify联合，loss外有混杂。5seed、四对比Bonferroniα.0125；去两技巧在三域中两域comparable，支持但不完全隔离各选择。Online1M/2Msteps、reward500/1000updates、batchSAC1024、rewardlr3e-4、3ensemble；hardware/precision/墙钟/annotation耗时NotDisclosed。humanpilot5rater(含2authors)、100-200ratings、训练每人100trajectories，标签GTreturns明显重叠，违背理论bin假设但仍局部实测改善，不能把鲁棒实验改写理论普遍保证。

有限拟采用：ordinal feedback不指定cardinalmidpoint与同类分布约束的替代目标，以及exact/nonoverlap条件和反馈预算分账；不采用跨语言RLHF优越性或人类认知成本保证。若长期书稿已承载上述具体判断可Existing；否则另提真实差额，不为论文名更新。

root实际A.2.2/human原文与Ch31 owner写前通过，两小段写ResponseRank后/privacy前；root实际Ch31:103–111正文/前后衔接及末注POST通过，窄锁释放。5分ordinalclass监督具体gap深入完成、整合TRAIN-RLHF；不采用offset/config recipe，不授LLM-policy。日级Gate/日期冻结未授。
