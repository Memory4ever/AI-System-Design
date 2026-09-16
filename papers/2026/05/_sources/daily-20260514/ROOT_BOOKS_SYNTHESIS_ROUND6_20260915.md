# 2026-05-14 Round6 Root Books Synthesis

**状态：** Root writeback pending

**边界：** 本文件只给出 owner、命题增量与写回约束；作者 lane 未编辑 Books。Root 必须先重读目标位置与相邻段落，并按章节现有论证重写，不能直接把本文件追加为论文摘要。

## 1. `2605.12652` → `TRAIN-GRPO` / Ch33

现有 OPD 主线已经把可达状态归 Student、token guidance 归 Teacher、outcome admission 归 verifier，但仍把每条 rollout 当作独立 teacher query。待写增量应位于 “OPD 是探索催化剂” 附近：同一 prompt 的多条 on-policy attempts 已经形成一个局部 trial-and-error state；成功 peer 提供可行路径，失败 peer 提供结构化负证据，二者可以共同构造 teacher context，再为当前 trajectory 产生 token distribution。

这不是让 Teacher 获得 reward authority。Group membership、policy revision 与 verifier result 必须冻结；Teacher 只据这些 evidence 提 supervision proposal。收益是 instance-adaptive guidance，代价是多 rollout、额外 teacher context/query、同组错误相关和 verifier label contamination。没有可靠 outcome、成本过高或开放任务无法验证时，保留独立 OPD、离线蒸馏或普通 outcome RL。

证据边界：exact-v1 的 Qwen3-4B/8B、8 rollouts、verl/异步 vLLM/FSDP/BF16 与披露任务；不外推任意 teacher、开放任务或生产 SLO。建议 binding：`SF-2026-ARXIV-2605-12652`。

## 2. `2605.12667` → `TRAIN-GRPO` / Ch33

现有 reward contract 已包含 binary reward、proximity zones 与 multi-channel aggregation，但缺少多级离散 auto-rater noise 如何进入 advantage estimator。待写增量应说明：直接归一化一次 1..K rating 时，单个离群 judgment 会改变整组均值/方差；把等级分解为 K-1 个有序 binary thresholds、逐阈值独立归一化后累积，可把一次 rating error 限制在部分 threshold，而不是污染全部 update。

该机制以 noise isolation 与 implicit curriculum 换取新的 objective state：rating scale、threshold ordering、每阈值 coverage 和 rater revision 都必须进入 run identity。它不消除 judge bias、threshold bias 或 reward hacking；等级不稳定、阈值样本退化或任务只有 hard correctness 时，回退 binary verifier、重复 judging 或保守 GRPO。

证据边界：exact-v1 的 Qwen2.5-7B/Qwen3-4B、UltraFeedback/RLAIF、8×H100 训练、4×A100 评测和披露 judge/benchmark；不把作者相对增益外推不同 reward scale。建议 binding：`SF-2026-ARXIV-2605-12667`。

## 3. `2605.12741` → `TRAIN-SFT` / Ch29

Ch29 已分别讨论 deployment episode 派生策略、same-prefix distillation 与 failure-conditioned demonstration，但缺少 rare-success 下的完整闭环。待写增量应将其串成：失败 trajectory 保留 raw provenance；局部 reflection 诊断 failure；跨 step playbook 保存可复用 lesson，并以 helpful/harmful evidence、staleness 与 pruning 管理；self-teacher 读取这些 derived state 产生 token-level target；当真实成功样本增多或派生策略失真时，切换到 GRPO/verified SFT，而不是继续让 playbook 自我强化。

Playbook 不是环境事实，也不拥有 admission。它降低等待成功 rollout 的交互成本，却引入 reflection hallucination、持久 poisoning、过时 lesson 与参数化后难删除。无法验证 lesson、需用户级删除或高风险任务时，保留 raw trace、外部 memory 或人工 review。

证据边界：exact-v1 的 Qwen3-4B/30B 与四个 continual-learning tasks；作者只证明 early rare-success regime，GRPO 比较不是等 rollout budget，后期表现非单调。建议 binding：`SF-2026-ARXIV-2605-12741`。

## 4. `2605.12908` → `TRAIN-RLHF` / Ch31

Ch31 已通过受限 logistic-regression 结果反驳“W2S 必须来自 capacity mismatch”，但还缺少 feature-level 正机制。待写增量应作为并列理论分支：在两层 reward model、pretraining task subspace 与 localization 等假设下，weak-label fine-tuning 的多步 SGD 可以逐步 elicitate latent target feature，同时近似保留 off-target pretrained features。它说明弱监督有时是在改变可读出的方向，而不是从零创造能力。

该理论不能升级 weak supervisor 的 truth authority。它未分析 second-layer learning，只证明 feature alignment 而非完整 function approximation，且结论依赖 algorithm、even link 与合成 geometry。假设不能确认时，仍必须用真实模型、held-out capability、teacher-error slices 和 policy-relative evaluation；不得以理论可能性降低反馈质量 Gate。

证据边界：exact-v1 的合成设置 `d=1024, s=128, K=2` 与披露 learning-rate sweeps；不是 frontier LLM 经验结果。建议 binding：`SF-2026-ARXIV-2605-12908`。

## 顺序与验收

1. 先在 Ch29 写 `2605.12741`，再在 Ch31 写 `2605.12908`，最后在 Ch33 按 `2605.12652 → 2605.12667` 顺序写入。
2. 每个 binding 在 canonical owner 的首个 `Review notes` 之前恰好一次。
3. 正文必须同时保留旧方案成立条件、changed constraint、state/control ownership、trade-off、failure、fallback 与 exact-v1 non-proof。
4. 写回后同步 queue/comparison/report 为 Applied，再交 fresh non-author reviewer；root 写回与格式校验都不能替代语义终审。
