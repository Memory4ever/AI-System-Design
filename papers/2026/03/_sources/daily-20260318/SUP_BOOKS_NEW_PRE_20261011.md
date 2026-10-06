# 后批逐字 PRE（尚未写入；不授 DAY）

作者 supp_mar18；仅 BJT 2026-03-17 补充窗。各正文保持唯一 owner；以下仅申请新增段与本人末注，不改其它家族。必要原证边界见 SUP_EVIDENCE_TITLE_COMPLEMENT_20261011.md。

## 15195：TRAIN-PRETRAINING / Ch28

拟插在“不保留反向图时，更新仍须可复算”中 tPC-RTRL 段之后、零阶分支之前；现有 influence-state 说明没有区分 dense forward 与近似的历史导数传输。

保留在线 influence state 时，降低导数传播成本不一定要同时剪掉模型的前向连接。一条受限分支保持 dense 权重和前向状态演化，只在历史敏感度递推中保留部分 recurrent Jacobian 路径；本步参数对状态的直接贡献仍计算，再以稀疏 transport 近似过去影响。这改变的是 credit-assignment estimator，不是模型容量或前向可见范围；mask、路径数与恢复身份须和训练状态一起保存，也不能由少算导数直接推出梯度无偏。<!-- source-family:SF-2026-ARXIV-2603-15195 -->

这种分责在持续获得误差信号的小型循环任务中可用更少传播路径保留部分适应能力，却可能在延迟反馈、更大 hidden state 或失配选择时失效；原文的 log-gap recovery 不是 MSE 改善百分比，固定路径数也没有跨规模保证。其 ViT 实验改用每次前向重采样的 head stop-gradient，不等同循环网络的固定 mask。路径选择、近似偏差、influence state 和真实实现成本继续验收；masked dense 运算不自动获得按路径比例的实机加速，质量或完整运行费用无收益时，完整 RTRL、BPTT 与明确截断的反传仍是合理退路。<!-- source-family:SF-2026-ARXIV-2603-15195 -->

## 15590：MODEL-LONG-CONTEXT / Ch22

拟插在“从 Dense Checkpoint 迁移到 Hybrid State Model”两段之后、“可映射的中间算子”之前。现有逐层保留 attention 不等于同 head 的两记忆并行。

迁移也可以不按整层决定留下 attention：同一 head 并行维护局部精确窗口与固定大小的矩阵 recurrent state，再用 data-dependent output gate 混合两者。局部窗口保留近期寻址，递归路径累积更长历史；受限构造复用原 Q/K/V，采用 512-token sliding window 与 4 个 sink tokens 配合 mLSTM，但不是原 full attention 的精确等价。每个 head 的 gate、窗口/sink policy 和两类 state 共同定义模型身份，不能仅以固定递归状态声称所有历史都能被精确回读。<!-- source-family:SF-2026-ARXIV-2603-15590 -->

这类迁移先冻结原 embedding/MLP、用输出 MSE 拟合新增组件，再以真实 token CE 与预计算 teacher 分布的 KL 共同适配全参数；拟合接口与能力恢复分开验收。它增加双路径计算、distillation 数据和训练费用，有限 benchmark 的 tolerance recovery 不保证所有行为保持，长检索和 STEM 仍有反侧。可选的同 seed 专家权重合并仍接受第28章的共同 base、独立 holdout 与更新兼容责任，不等同推理 ensemble。编译/static-cache 的单 H100 微测也不授生产服务 SLO；迁移质量、状态接口或净成本失配时，原 dense checkpoint、逐层保留 attention 和原生 hybrid 继续成立。<!-- source-family:SF-2026-ARXIV-2603-15590 -->

## 15059：TRAIN-PRETRAINING / Ch28

拟插在 Muon/spectral geometry 的现有噪声条件论证附近（现有 Ch28 约 565–610），与15195分次窄锁写。严格更快/缺秩桥争议不采，只补 joint schedule 的长期边界。

选择 matrix-normalized 方向还不能把 batch 仅当吞吐旋钮。在 loss 有下界、Hölder-smooth、无偏且有界有限 p 阶噪声矩（p∈(1,2]）的无动量（β=0）理想 polar-update 分析中，步长须既不总和耗尽，又使高阶步长项与 batch 控制的噪声项可求和：除 ∑ηₜ=∞、∑ηₜ^(1+ν)<∞ 外，还要求 ∑ηₜ/bₜ^((p−1)/p)<∞。固定 batch 且噪声非零时，后者与不耗尽步长条件不能同时满足；扩大 batch 因而是这项理论的成立条件和付费预算，不是免费的 runtime 优化。该受限结论只给 liminf 梯度范数为零，不推出参数收敛、实际噪声必为 heavy-tail 或 LLM 墙钟更快；近似正交化、动量与缺秩实现仍须另验。条件或总成本不成立时，保留已验证的 AdamW/SGD/Muon recipe，而不以理论 headline 替换它们。<!-- source-family:SF-2026-ARXIV-2603-15059 -->

## 15377：MODEL-SAMPLING / Ch20 — 拟已有覆盖，非新写入

实际正文330–350已将 coverage 与 selection 分开，明确更多候选增加相关错误与选择费、selector 不提高则更不稳定。本文有限 k≤4 reasoning-step beam/PRM-vs-NLL 反证用于该已承载命题；本次不主张新 frontier 状态实现，故 No Change，不为 diff 添段。中心 Gaussian/GEV 近似不足以认证 safe/optimal beam width，具名隔离，不作为已有覆盖的数学证明。
