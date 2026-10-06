# root：两项 RAG 必要 Source 与 owner 差额

仅04-04补窗两项未处理身份，作者已把完整题摘准入与Apr3组合日门交独立reader通过；root复用这一层，不重做17个同事件。以下只核exact-v1必要证据和具体正文差额，尚非Books写后或日级验收。root已重读当前研究/Report合同、Books适用理念与指南；actual Ch76相关论证、75末交接与77开篇已读，不据大章主题相同记NC。

## 2604.02194v1 Neuro-RIT

原证：[exact-v1](https://arxiv.org/html/2604.02194v1)，[本日原件](SUP_2604.02194v1.html)。实际§3.1–3.2、§4.1–4.6/Tables1–4、A.1及A.2必要接口。IG以query-only为参照、query+document激活为终点，20步积分；按题目筛top neuron、按相关/无关组频率成集，并拆交集。先对无支持文档训练EOT目标，再以外部teacher的相关摘要训练reader，使用group gradient masks及高密度三层全参数更新。**这是训练目标与参数更新位置，不是运行时强制关闭特定neuron或保证拒答。** 389×2 HotpotQA attribution样本，Llama3-8B/H200141GB/batch4与两stage学习率/epoch披露；Mistral需重做选层，不是同mask直接移植。

必要反证：Table4去neuron更新的均值68.20对68.46差额小，去layer更新降61.77，不能把整项收益独归“独占noise neuron”；参数0.529B包含层更新，不是只改230个标量。Table1加RankCoT后均值反降，Table3的answer-absent准确率不是groundedness/abstention率。A.1以SPLADE分数选相关人口，Table5无关例仍gold=0/YES与上下文不支持的文字冲突；**不采用可复现精确归因标签配方、因果功能独占或已证noise解耦**，仅保明示的训练分支及上述反证。teacher凭prompt声明零固有知识不构成约束证明。训练/IG/teacher/重选层成本、精度/输入输出长度与完整端到端SLO Not Disclosed/未测；代码未核、未复现。

评分建议2+2+2=6，拟采用的是RAG reader训练分支与mask/层更新分责，具体反证要求深入受影响部分，不因争议降分或EX。Ch76现有GRACE已解释支持人口和learned abstention，score-conditioned attention已有版本绑定，但未解释attribution提议参数位置与全层更新共同组成artifact，以及EOT训练不等runtime硬门。唯一owner AGENT-RAG；不在Ch29/16再复制方法。

**最小拟稿**：接Ch76 GRACE两段之后、下一“补查也可以改变retriever…”之前，保全部现文：

> 支持人口确定后，还可以选择训练时改动哪些reader参数，而不只把所有参数交给同一拒答/抽取目标。一个实验分支先用相关与无关context相对query-only的activation attribution提出FFN neuron集合，拆开重叠成员，再以无支持输入的EOT目标和有支持输入的证据摘要目标分阶段训练；group gradient mask与被选整层更新共同定义新reader artifact。Attribution在这里负责提出适配位置，EOT负责学习终止行为，两者都不是在线强制拒答或neuron功能独占证明。<!-- source-family:SF-2026-ARXIV-2604-02194 -->
>
> [有限两模型QA对照](https://arxiv.org/html/2604.02194v1)的消融显示整层更新贡献大于额外neuron mask差额，部分context refinement组合还会退步；不能把全部收益或参数效率归给局部neuron。归因样本、相关标签、teacher摘要、mask、被选层与reader版本均需重新验收，IG与数据生成/适配成本不能从推理路径消失。原文归因标签示例尚有未解一致性问题，故不照录精确定位配方或因果解耦结论；标签不可靠、域转移或更新不合算时，保持原reader、普通检索重排与外置sufficiency/claim gate，而不让训练EOT替代它们。

需作者actual确认插入邻接与最小本人末注，交reader复核采用边界；root未写Books或计I。

## 2604.02091v1 RRPO

原证：[exact-v1](https://arxiv.org/html/2604.02091v1)，[本日原件](SUP_2604.02091v1.html)。实际§3.1–3.2/Eq1–15、§4.1–4.4/Tables1–5、Limitations、B.1–B.2、H/I必要成本/反证。固定pointwise reranker先对全部候选给一次分数，softmax后按剩余集合mask重归一、无放回采样有序slate；**没有每步用已选证据重新计算内容得分，不冒称真正set-conditioned scorer**。每个prefix交固定reader答题，用EM+F1+Hit目标给训练反馈；reference从同一initial pool greedy产生对应长度prefix，取其reader回答分作时间基线，省独立critic。

该reference prefix不等于当前采样路径的条件价值，且Eq8比值用固定ref、不是普通old behavior ratio；本文GAE偏差/方差解释存在过强或倒置措辞，不照录为严格PPO等价或非退化保证，只采用明示的训练反馈/参考身份。BM25 top100、DPR100words、HotpotQA k3/AmbigNQ k5、Qwen2.5-7B reader、四3090训练/两A6000 reader、AMP/batch32等协议已绑定；有限改善非通用groundedness，Qwen3 reranker RRPO后Hotpot仍低NaiveBM25。B.2没有reward-generated监督ranker对照，不能证明RL优于同反馈SFT；H为有限query配对统计，非全reader泛化证明。I的缓存/温度0 replay减少调用不是端到端训练省时测量；跨reader迁移仅受测模型，不采reader-agnostic宣传。

评分建议2+2+2=6，贡献在prefix reader反馈与固定reference身份的优化/评价边界；必要反证深入。Ch76 LURE段已有单文档utility蒸馏，Reranking段已有history K1和setwise效用；当前没有区分prefix反馈的优化slate与实际scorer conditioning、reference-time baseline与采样state value。唯一owner AGENT-RAG；通用PPO/GAE继续Ch32，不复推公式。

**最小拟稿**：接Ch76 LURE两段之后、下段“证据需要互补时…”之前，保现文：

> 单文档效用不够时，也可以在离线训练中无放回采样有序文档prefix，每加一篇就让固定reader回答，以答案任务分数训练reranker。固定reference从同一初始候选池greedy选出对应长度prefix，其答案分可作为时间相关基线，省去独立critic；但这不是当前采样路径的条件价值。训练反馈覆盖多文档并不表示scorer已经读取组合：若query–document分数只算一次、后续仅mask并重归一，它仍没有每步重估文档互补性。<!-- source-family:SF-2026-ARXIV-2604-02091 -->
>
> [RRPO的有限QA对照](https://arxiv.org/html/2604.02091v1)支持固定候选与reader下的局部排序收益，不证明RL优于同反馈监督训练，也不让reference比值取得通用PPO保证。Gold答案任务分数不是证据support，换reader、候选池、prefix预算或参考策略需重验；rollout、各prefix reader调用、训练与replay缓存都付费，局部调用节约不能代替端到端成本。召回不足、组合依赖无法由单次scorer表达或收益不合算时，保留relevance/hybrid、已有utility reranker与外置support核验。

需作者actual owner/PRE与reader采用层确认，尚无Books新写/I/POST。
