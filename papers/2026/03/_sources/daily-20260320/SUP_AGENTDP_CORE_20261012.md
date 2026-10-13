# AgentDP17902：必要理论假设与中心桥接问题

root准备，2026-10-12，仅03-20补03-19。原2+2+2=6及date/准入有效裁复用；未写Books、不自签Source结论或DAY。交非准备者独核以下具体冲突，非以访问困难/工作量降分。

[exact-v1](https://arxiv.org/html/2603.17902v1)完整题摘、III-C/D、IV Definitions2/3与Lemma1/Proposition1/Corollary1、V Proposition2/3与Eq5、VI设置/指标及VII实际读够。current abs同两作者/v1可见，未见采用相关撤回说明；未读全部参考文献、代码或复现。

## 原证与root推断分开

原文IV给固定prompt/context下的一条record邻接；若对全部相邻D/D'、全部相同history及token的logit变化确实有统一Δ界，softmax归一化可得纯DP每token2Δ/T，上限L的消息可逐token合成。这是条件结论，不是已认证实际LLM的Δ；温度升高本身没有提供敏感度证明，EOS/长度/检索路径与重复会话也未在这个单消息人口内一并证明。

以下是root对原文的直接数学反侧，需非准备者独核，不能记为作者已经承认：

1. Definition3只对单token的点概率给(εk,δk)不等式，却在Lemma1直接援用所有输出集合的近似DP合成。四token的P=(.4,.4,.1,.1)、Q=(.25,.25,.25,.25)每个单token双向都满足ε=0、δ=.15，但前两个token的集合为.8与.5，差.3，已在L=1违反同δ的Definition2。δ=0的纯DP不受此反例影响；不采用一般δ加和保证。
2. III-C为逐步局部归一化AR分布，V-A把它写成全序列累计raw logits的一次Gibbs归一化；history依赖的分母不能通常删除。二token例：首步两logits=(0,0)，前缀A后=(0,0)，B后=(10,10)；实际四序列各.25，按累计raw-logit的全局Gibbs则偏向B。Proposition2显式假设Gibbs时的导数可成立，但不自动适用原AR生成，不采用其普遍效用单调或最优温度桥。
3. V给bounded utility，而Eq5在无上界的T>0上奖励λT/L。λ>0时目标趋正无穷，无有限全局最大；Proposition3写any interior optimum的必要条件不证明这样的最优存在，不采有限最优温度或可执行优化recipe。

VI只GPT-2、两相邻incident prompts、L2/5/10、T.1～2及每点250采样。输出映到有限label再Laplace平滑的经验max-log-ratio/TV/JS，不是全prompt/相邻数据/全部序列的sup证明；人工utility e^U+.1L也非enterprise任务质量。完整硬件/精度/并发/SLO及真实敏感度accountant未披露，有限趋势不修复上述理论桥。

## owner与待裁处置

实际`PLATFORM-SECURITY` Ch72完整41–61 trajectory泄漏/释放边界、375–407 rewrite/DP近文与相关adjacency/accountant段顺读；Ch71入口实际核，Ch73路径以ROADMAP为准、不写猜路径。已有具体论点不把经验ambiguity、attack失败或rewrite签成DP，已分清正式发布级数学边界和平台authorization。潜在增量是dataset-conditioned logits敏感度/temperature/length的条件组合，但当前中心近似DP/AR效用/最优设计桥未闭合。

拟`争议 / 暂缓`，保原6，不写Books、不冒整篇无价值；请求作者针对Definition3→Lemma1集合保证、AR→Gibbs所需假设及Eq5有限最优域的具体勘误/证明。纯DP条件界可说明已读且局部成立，但不把它代替整项中心结论通过。若非准备者判断这一可分离命题足以构成长期差额，再准备窄PRE，而不是直接授写。独核足以判本处置即停，不拓所有DP论文。
