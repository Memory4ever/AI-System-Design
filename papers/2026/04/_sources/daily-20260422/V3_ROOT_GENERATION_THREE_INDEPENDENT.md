# Apr22 生成目标三项有限非作者核

复核者root，非报告/提案作者。实际读官方exact-v1必要方法/评价及Ch24对应CTMC目标、masked revision与ELT有限loop正文；未验全日报来源/日期，未复现实验，未遍历无关附件。

## 18738：5分标准，仅报告通过

[v1](https://arxiv.org/html/2604.18738v1) §4.2～4.3/Alg1、§6实际核：保持detector而把替换动作改成MASK，另有当前低概率和跨步下降信号；每位置次数/每步比例cap约束振荡。v1主表仅LLaDA2.1-mini、greedy、block32，BBH75.50→75.38、AIME30→30，pilot的100题选择不能与全测试主表合成一致端到端成本。mask无方向偏差及错误token必是adversarial不是一般定理。Ch24:195～216已经将允许重写、训练噪声/软状态、span proposal与commit分开；新局部action消融值得报告，但不足以新增长期机制owner。不称三detector算法整体已有覆盖。Only通过，生产配置缺失仍保留。

## 18739：6分具体缺口深入，窄采用通过

[v1](https://arxiv.org/html/2604.18739v1) §3.1～3.3/Eq11～19、§4.3～4.4实际核。共同mask条件律下，terminal reward的指数倾斜可转为base样本上的加权条件矩，再用局部unmask posterior匹配；CTMC hazard权重把局部目标连接到受条件的terminal KL。Ch24一般masked CE/CTMC及Ch31 reward/KL、Ch33 policy gradient并未解释这条无需精确sequence marginal的matching分支，可以放在Ch24相应目标之后，不命名为GRPO升级。

应保留base条件律、mask schedule、reward和buffer身份；有限神经训练、近似base posterior、confidence-based reveal和旧buffer不自动满足理论期望。control variate的条件无偏性不等于任意参数下每个sample target都是概率simplex：Eq17若r允许负值、c=1，w=exp(hr)<1且实际类别base概率很小时该分量可能负；不在Books写任意reward/c皆为合法概率或唯一全局最优保证。采用终点重加权→局部目标的有条件机制即可。

§4.3～4.4保留LLaDA8B、LoRA128/64、32块/256训练输出/T128与8H100 Sudoku比较；MATH/GSM弱于SPG，大h风险和额外rollout/mask/优化成本真实存在，不外推稳定收敛/生产SLO。可以按两段窄写，写后仍须实际非作者验收。

## 18839：6分具体缺口深入，窄采用通过

[v1](https://arxiv.org/html/2604.18839v1) §3.1～3.3/Eq6～7、§4.4～4.5/§5 Table1实际核。DRM从腐化target初始化，对共享转移展开有限k步后监督末端并整窗反传；它与ELT的同图full-depth teacher/prefix student目标不同，可以接Ch24:250～252有限loop论证后。该目标不是unknown inference state全覆盖或实际规划的证明。

SPRM对自身轨迹的扰动是另一分支，§4.4明确inference不加噪且加噪略降；Table1中7M reARC SPRM11.8低于TRM12.4。7M→14M同时改embedding、heads及k4→6，不能单归递归深度；pass@2、数据/示例微调和candidate选择须一起评价。正文保短窗activation成本、窗口外漂移、长TBPTT/单步denoising/固定深度共存；不采用小模型普遍超过4B或全成本更低。两段采用通过，不代表日级Gate。

## root 实际写后复核

实际顺读 Ch24 的 ELT 段、18839 两段与后接 commit boundary，以及 CTMC 段、18739 两段与后接监督粒度。两项已真实进入机制正文而非只写 Review notes：18839区分 prefix 蒸馏、窗口末端监督与长程状态覆盖，保留 SPRM 退步和候选/配置混杂；18739区分条件匹配与轨迹 RL，保留 buffer/条件律、sample-target 合法性与 rollout 成本。前后主线通顺，未采用全局最优、普遍质量收益或生产 SLO；非作者实际写后通过，未复现，仍非整日完成。
