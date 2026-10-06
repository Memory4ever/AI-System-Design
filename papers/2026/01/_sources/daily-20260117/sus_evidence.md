# 10349 SuS：中心实现冲突的受限终态提案

精确源 https://arxiv.org/html/2601.10349v1 ，实际§3.2–3.6 Eq2–4/Alg1、§4.1/Table1–2及直接消融，缓存2601.10349v1-decisive.txt。5分候选准入有效，不因少样本/负面/工作量删分；本次拟中心Disputed、NoBooks，待root实际终裁。

原文§3.3定义Strategy Stability为pre/post cosine、奖励稳定；Alg1 line9写SS=1−cos。§3.4把surprise定义为预测state误差×(1−SS)，Alg1 line10却用scalar |c−P(query)|独立于SS，line12只在c=1正确trajectory上追加。它们不是同一算法，缺统一state、correctness predictor、权重与gate的明确实现；不可替作者修sign/把Alg1重写为理论配方。§3.5称meta-learned weights但更新/数值配置不足，进一步限制统一机制采用。

作者局部实测Qwen2.5-1.5B LoRA，GSM8k 200 heldout，3epochs、batch2/acc4/G8，Table1 Pass@1 14.2 vs12.1、Pass@5 46.8 vs37.1；Table2拆两个signal。此仅其未统一配置下的作者局部结果，不能凭消融判明运行的是哪个机制。硬件、precision、seed/重复、不确定性与完整新增encoder/predictor训练及E2E费用Not Disclosed；clusterentropy非真实策略独立性，缺controlled noisy-TV证明。

Ch33现reward/objective identity必须与真实estimator绑定，不授“sim一致即策略真值”或天然noisy-TV免疫。该具体冲突使统一增益归因/奖励机制不能长期采用，非主题一般覆盖的ExactExisting；无Books新写。隔离不作正面保证，重开仅需作者统一Eq2–4/Alg1、actual reward code与超参/gate，定点核受影响方法及匹配评价，不全版本diff。
