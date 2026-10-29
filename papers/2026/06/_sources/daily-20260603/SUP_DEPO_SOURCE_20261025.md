# 00392 DEPO：标准必要审阅 / 五分 / Ch33具体已有覆盖提案

仅Jun03补Jun02 BJT；当前AGENTS/Research/Report/Sources适用分组/统一入口/ROADMAP和本日停点已恢复。旧R26/28完整题摘/准入与联合日期有效复用：唯一v1 May29 22:19:28Z提交，精确DOI `10.48550/arxiv.2606.00392` arxiv.content/findable/registered Jun02 03:50:27Z，按适用公告规则最早Jun02 00Z至登记上界同Jun02 BJT。不是提交日直接归窗。[当前官方abs](https://arxiv.org/abs/2606.00392)唯一v1、所见无withdrawn/erratum，不作完整版本史遍历。

## 实读、机制和直接限制

实际读[exact-v1](https://arxiv.org/html/2606.00392v1)§2–3完整目标/式1–8/dual更新、§4.1–4.5主要比较及反向转移、A.5阈值解释与T14训练/推断/评价设置；未读完整改写攻击样例/payload、全部实验附件、代码或复现。这里只审约束优化与测量，不生成/执行规避检测的改写。首次大段输出的跨域表有截断，不宣称完整核所有数字；本文采用的主对照和方向性反侧实际可见，足以停止。

主reward为detector读出的AI分数反向，constraint为BERTScoreF1的**期望**≥阈值，非每篇严格保义。一次同prompt G候选里两reward各自中心/标准化后以当前lambda合成advantage，再做ratio/clip/KL更新；dual却读未标准化mean BERTScore与原阈值差额，lambda非负且配置上限10。故反馈单位和相对更新尺度不同，不能自动继承原CMDP原始reward的严格可行域或逐样本约束。§2援引零dualitygap也不构成参数化LoRA、有限样本/clip更新的收敛或每轮满足证书；这里是自己的采用边界，不声称论文已证明该非等价修复。缺少zero-std处理的公式不补成通用recipe。

BERTScore用DeBERTa上下文token匹配，不是原子事实、逻辑蕴含或全部细粒度语义真值。T1 direct rewrite均值.854、DEPO .857跨.85，说明受测平均proxy可行；detector-only更高规避但proxy.798未过，固定权重的若干有限配置未过，不能推出所有scalarization不可能可行或DEPO普遍唯一最优。一个均值checkmark不显示低尾/每样本都≥.85。跨detector/域有限转移不授未见检测器可靠性；§4.5更换训练域与reward detector后对原MAGE转移反弱，混合域/奖励变化不能唯一归一个因素。所有原始分数与评价阈值须各自保留，不能把ASR和AUC方向混为统一更好。

T14：Qwen3-4B-Instruct-2507、LoRA32/alpha64/dropout.05、AdamW2e-4、4prompt batch/accum4/G8/3epochs/1000train、KL.04、train temp1、seed42；推断temp.9/top-p.95/max512，一样本一candidate，1600 AI测试/100–500token、human10k在1%FPR校准、eval seed2026。硬件表仅“A6000 Ada/H100”、卡数/完整wallclock/全配置匹配与重复CI未闭，precision/生产并发/SLO未披露或不适用，不自行补。阈值.85按普通改写heldout分布的解释不是跨域概率校准。模型/奖励调用、rollout、BERTScore/全部检测器、训练/调参和独立保义检查都付费，少一value model不等总成本已验证更低。

## 正式评分与actual Ch33具体覆盖

Design Delta2 + System Reach1 + Durability2 = 5，与旧未冻结初分一致，不因NC/费用降分。具体贡献是受限任务中以外部语义proxy目标/阈值反馈替代固定reward权重，并暴露组相对归一与原单位约束的分责；不把一般CMDP/GRPO或“能检测规避”本身当新基础定律。

唯一 `TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)。实际完整读原组mean/std+delta解释与直接代价、FGRPO完整段及相邻效率资格组、GDPO多criterion组归一→batch尺度段、**Lagrange multiplier/CGRPO完整段**与直接后turn-normalization完整组；Ch32/34开篇及ROADMAP边界已读。它们已分别具体承载：多signal独立归一与显式dual feedback；judge/proxy非行为真值、期望不等每样本gate；标准化改变约束控制单位，保原violation/threshold/乘子及advantage，不能继承原cost guarantee；所有费用与outcome-only/独立gate回退。

这些实际机制正文已承担本项可复用结论，不只是“本章讲GRPO”的主题映射。DEPO的检测器任务与有限.85配方不新增长期owner或改变现有设计结论，拟具体**已有覆盖**，无新PRE/Book/本人注/POST要求。当前正文未签零dualitygap、严格语义可行或普遍支配，故无需为反对论文宣传强造纠错diff。首次必要/五分/具体NC尚待独立复核，不预行政采用或DAY；下一项按真实原路由，不从本处猜ID。

## 后续采用

R159首次必要/正式五分/actual Ch33具体NC通过，root已融Report候选与证据段。无Book/本人注/PRE/POST待办，不执行检测规避或预DAY。
