# JitRL — Source / PRE（待独立确认，非写后验收）

材料：[2601.18510v1](https://arxiv.org/html/2601.18510v1)。公开日联合核验为2026-01-27：精确v1周一截止前提交，已赋最终ID与官方公告规则给首次announcement下界；arxiv.content当日deposit created给可用上界，不用Submitted/created单值替代公开日。原始见 supplement-abs-18510-20261008.json 与 supplement-date-identities-20261008.json。分数2+2+2=6；具体owner缺口深入，不因Books处置改分。

实际必要原源：§3–4.4的状态/动作/回报triplet、局部kNN的V/Q与unseen-action optimistic bonus、KL惩罚求解；§5.1/5.6 Table8/5.7 Table9与Appendix C。给定Ahat的closed form有效，Ahat不是真实advantage。C.1 asymptotic条件与C.2证明的cross-entry noise条件未充分说明；仅每条conditional-zero-mean/variance不能推出无covariance的σ²/k，隔离理论一致性/实训最优保证。实际固定k不等于k随N增长。Blackbox verbalized confidence→logits另分支不是base真实probability接口。Table8同memory prompt对照支持所测Gemini/WebArena/Jericho的窄增量；异硬件/训练费与API价不支持统一34倍端到端成本。

Owner：AGENT-MEMORY，Ch77。实际已读Fact State/Retrieval-policy State到U-Mem、后续read-time complexity与unit×presentation交接；Ch76收尾与Ch78开篇。现有learned proxy与U-Mem把反馈用于选memory/其呈现，未承载“已取回经验直接估计当前action advantage并在冻结模型logit重加权”的分支。新增不重复事实治理、Thompson memory探索或Ch33权重训练。

拟插入：U-Mem段之后、`这条演进把部分复杂度`之前。保留所有原文，以下两段，删论文名称仍沿问题推进：

记忆还可以影响“当前该选哪个动作”，而不只决定把哪些记录送入 Context。若历史经验保存状态、动作与回报，可在当前状态的语义邻域估计各动作的 Q 与整体 V，得到局部优势估计 Ahat；对未见动作的乐观奖励则显式承担探索假设。在能取得动作 logits 的冻结模型接口上，用 z′(a)=z(a)+βAhat(a) 重加权生成，等价于对给定 Ahat 求解预期优势减去相对原策略 KL 惩罚的单步目标。这是经验驱动的推理期 action-policy state，不是参数训练，也不把取回的记录变成事实权威；β、邻域、动作解析和奖励模型均进入其身份，错误相似度或奖励会把行为推向错误方向。

这一闭式解只优化所给的优势估计，不能认证它等于当前真实动作价值。[JitRL 的同记忆对照](https://arxiv.org/html/2601.18510v1#S5)在所测 Gemini/WebArena 与 Jericho 条件下比较了仅提示记忆与 logit 重加权；black-box 分支把 verbalized confidence 转成代理 logits，并不是读取 base 的真实概率。固定 k、LLM 步奖励、不断变化的策略也不能自动满足渐近估计所需的局部平滑、条件无偏、动作充分访问、邻域增长及漂移消失条件，噪声间相关还影响其方差论证。检索、评估与logit接口带来额外调用及维护成本，异硬件训练费用与API价格的比较不授生产降本倍数；支持不足、接口不可得或reward漂移时，保留记忆提示、静态检索与原策略，并继续由授权和结果验证限制动作。<!-- source-family:SF-2026-ARXIV-2601-18510 -->

Root已授本日该两段+自身note窄锁，作者尚未写入。需peer实际PRE确认后落正文，再actual POST。当前Ch66/33未获写锁。
