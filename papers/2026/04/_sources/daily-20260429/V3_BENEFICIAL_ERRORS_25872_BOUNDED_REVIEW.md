# 2604.25872v1 Imperfect Rewards：必要证据与 Ch31 owner

只读 [官方 PDF exact-v1](https://arxiv.org/pdf/2604.25872v1) 的 §3.2–3.4/Thm1、§4.1–4.2/Fig3、§5/Fig4、Appendix A.1 特征几何限定，和实际 [Ch31 RLHF](../../../../../books/part-04-training-system/31-rlhf.md) Preference data／Reward hacking／Policy-relative State、相邻 [Ch33 GRPO](../../../../../books/part-04-training-system/33-grpo.md) Verifiable Reward。HTML v1 当前 404，不以此称论文不可读；本项未展开 88 页附录或复现训练。首公开日期仍须由本日公告窄链及同家族例外核实，PDF 页眉 `28 Apr 2026`/submitted 不独证北京时间落窗。

## 贡献准入与真实机制

既有 Ch31 明确 preference pair、当前 policy 分布漂移、RM reward hacking 与 verifier 独立权威，然而“RM 排序准确率高”与“用它作 policy-gradient 后真实目标上升”之间仍缺**更新动力学的判别条件**。本文给出区别：线性 softmax policy 的 logit 更新含 `πθ(y) [rP(y)-EπrP]`，所以错排答案若仍低于当前期望代理奖励不会吸引质量，初始概率极小的错奖在受限时间窗里也弱；相反，比当前期望高的中等质量答案可能先吸走质量，使稀有最优答案概率更低。正负影响由 proxy 值、初始/当前 policy 分布、feature 几何和 PG 算法共同决定，而非只由 pairwise 标签错位决定。这是与 Ch31 当前静态 pair 准确率/泛化叙述不同的长期边界，符合 V3 贡献准入，不因理论中的线性模型或实测 1–3B 直接拒。

Thm1 只在 orthonormal output features、单个最优/中等答案加低质集合、固定奖励和**exact-gradient flow** 等假设下，证明当最优答案初始概率足够小，正确 `rG` 给中等答案中等分数会导致任意大的达标时间差；把它错误压到最低可加快到达，但不意味着实践中知道哪条“中等”应故意错奖。Appendix A.1 的正内积特征情形还可能**反过来**要求给中等答案中等奖励才能学到最优；负内积加剧停滞。因此“所有 reward errors 有益”/“binary 一定胜 partial”均不成立。

§4 的 harm-aware ranking accuracy `HAcc` 不把所有 pair 错排等罚：若 rejected 的代理 reward 低于 `max(rP(chosen), EhatπrP)`，不记有害排序错误；加权版本再用当前 policy 的 length-normalized likelihood 估计相关性。代价是必须从具体 policy 采样以估 `EhatπrP` 并计算样本 likelihood，不能当模型无关排行榜。四个 1–3B policy、13 RM、UltraFeedback/RLOO 的 Fig3 表明 HAcc 类指标通常比普通 ranking accuracy 更能预测后训表现，但相关仍低于 `0.4`、有时为负；概率加权也非稳定增益。所谓“ground truth reward increase”主实验由**另一 ArmoRM** 代理，训练集 prompt 上计算，非人类真实效用；Appendix 的另一 RM/GPT judge 对照缓解而未消除该真值身份限制。独立 held-out/human outcome 仍是 promotion authority。

§5 两约束 IFBench/Qwen3-1.7B GRPO 的 Fig4 是 reward 设计的受限示范：当一个约束初始容易而两个同时满足罕见，`0.5/约束` 部分奖励会让 policy 停在易约束，`1/两项均满足` 更快；另一个 pair 初始易度相近时两种方案都可行，脚注/App C.3 还记有高易度差时 partial 反而能快学两项、binary 失败的情形。该现象可供 Ch33 交接，但不能拿两个构造 pair 或线性理论普遍禁止 partial reward。

## 分数、Books 最小提案与停止

作者拟 `Design Delta 3 + System Reach 2 + Durability 3 = 8`，Deep。唯一知识 owner 拟 Ch31 的 Reward Model 质量/Policy-relative State；Ch33 保既有 verifiable reward 算法位置，不在两章重复叠论文名。Ch31 有真实增量：RM 选择时不只报告 pairwise accuracy，也需要在冻结的初始 policy/候选分布上区分 reward 错误的 **relative-to-current expectation 与 probability**，再同 downstream true-outcome 对照。不能把“良性错奖”提升为道德/安全许可，也不能用代理 RM 评价循环自证。

拟在 Ch31 preference candidate-distribution 段后、或 Policy-relative State 前择一窄落点：

> 排序正确率把所有偏好对等权计数，但 policy-gradient 实际消费的是相对当前策略期望的奖励优势，并被该答案的生成概率缩放。一个错排的 rejected 若仍低于当前代理奖励期望，可能不会吸引更新；更危险的是较常见、只有中等真实质量的答案获得略高于当前均值的奖励，先吸走概率，使罕见最优答案更难被探索。选择 Reward Model 时应冻结初始 policy 与候选分布，将 pairwise accuracy、按当前 policy 估计的 harm-aware 错误切片，以及真实后训效果并列，而不能用独立排行榜替代更新后的验收。
>
> 这种分账增加 on-policy 采样、likelihood 与独立 outcome 成本；少数输入或权重结构变化还会改变错误的方向。线性 softmax、正交特征下的停滞定理不是 Transformer/有限步 GRPO 的无条件定律；作者在四个小 policy 上的 HAcc 与代理“真值”后训收益相关仍弱且可反向。无法取得独立 outcome、当前 policy 不稳定或预算不足时，原 pairwise ranking 仍是廉价筛选，但只能报告当前偏好数据上的拟合，reward/verifier authority 与安全 Gate 不随这个指标转移。

待 root/另一非作者只核官方必要 §3–5 与 Ch31 实际相邻段、最小 source→owner 增量并授共享锁；当前未改 Books，未计 Integrate、未签本日 Evidence/日期/独立 Gate。本篇原属 106 潜在线索，工作账不变。
