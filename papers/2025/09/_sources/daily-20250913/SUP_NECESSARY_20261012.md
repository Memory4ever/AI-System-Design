# Sep13 增量必要决定门与理论采用边界

作者Schrodinger实际读取本日精确v1原件，HTTP/bytes/SHA与执行时间在同名SUP request。以下不等全部全文/附录、公开日、实现核验或复现；日期未证不评分、不列为正式新候选、不进入Books。旧12风险/理论及3评价必要核心有效层仍保留，不由新标签推翻。

## MOAT 2509.09629v1

实际methods paragraphs18–34及§5证明35–48：planner每次K subgoal由grounder PPL择优DPO，grounder自生成action经更强critic过滤/纠正，coldstart SFT后交替。机制窄P成立。Lemma把PPL与实际奖励负相关当等价目标，再由DPO和CE likelihood改善推实际R不降；相关不推出逐点等价/实际奖励单调，有限SGD/有噪critic也未满足理想更新假设。即使有界单调标量奖励成立，也只得其值收敛，不认证整个参数/多agent训练收敛。保留中心保证争议；恢复需要对应奖励代理条件、实际更新保证的可信证明/勘误，而非更多无关benchmark。

## CDE 2509.09675v1

实际method24–61（52–55截断后单独补读），AppendixD100–111/E112–143。actor bonus主式`r + omega_t min(|r|/kappa, alpha B_actor)`的负奖励符号保持需要有效omega/kappa边界；AppD吸收omega后改用κ|r|且κ<1，不能忽略参数化条件。AppD精确KL-prox分布更新仅给同correctness组内相对likelihood排序，不等所有正确答案绝对增加/概率校准；normalizer下两者都可能下降。AppE finite-horizon linear MDP、已知有界features、iid centered subGaussian MC noise、Gram/n→正定、无放回head子样本和asymptotic n/K的ridge结果不升级为有限神经critic/PPO countbonus保证；ζ=1相同head无分歧也不证明通用探索能力。此处只保条件理论/奖励设计P，不照采全部calibration或样本效率headline。

## Graph Alignment 2509.09597v1

实际methods36–71、AppB107–128证明，§4.3 83–87及AppC.4 148–155。lowpass1−λ/2与highpassλ/2在λ=1同为.5：响应相反方向不推出正交/独立或MI≤ε，常数/退化features也不能保证严格margin提升。soft orthogonal/bijective penalty不认证exact isometry/bijection；concatenation不同坐标块距离本来可分，不需要用未证互信息补归因。P是双通谱表示与geometry-aware对齐机制，不采用中心普遍保证。vision/language评价是按class平均image embedding/多textprompt平均后kNN图，不等任意instance-level语义映射；模型/数据条件不同不可将一个榜当通用泛化证书。未核所有表/图/实现，日期回归还需证明假设/具体修正与可比协议。

## 七个最小贡献决定门

- RFSeek10216：实际intro4–19/方法20–36，source-linked edge及显式/推荐/推断分账、ASCII图遗漏与prompt遗漏集合变化，保窄P；不授citation即语义truth或complete FSM。
- XAgents10054：实际§3 paragraphs22–53，discrete membership低于ML后reprocess，再remove无关节点/decompose过复杂节点，保局部路径重建P；LLM membership/vote不是独立truth、并发安全或终止保证。
- Style10179：实际intro5–16/results61–101。human前后style本身不稳、语言/genre/base-chat/prompt分项影响比较，窄P；不采RLHF唯一因果或所有Czech base失效普遍结论，未核figure像素。
- DOCUEVAL2511.05496：实际intro/六层方法/演示paragraphs4–34（16–28另补避免截断），人先独评再看AI，版本化criteria/config/source/trace与workflow比较P；只有peer-review演示不认证human truth、deployment quality或guardrails防御效果。
- CARENLI10222：实际13–33及71–94。typed-schema routing与oraclefamily上界/局部misrouting反侧P，不是临床应用指标即机制。80条由模板扩展非80独立真实人口；verifier accuracy按solver最后label正误定义，不等独立reasoning-validity标注；compositional高route准确仍低task结果不支持唯一routing因果瓶颈。
- SIRBench16226：实际27–43/77–91。只保随机codon counterfactual及固定总context few-long对many-short的LLM归纳测量P；不引入molecule/clinical discovery研究。Anscombe实际27–55/72–91独读校准通过，不授唯一memorization因果或全部LLM无归纳保证，非读全部科学任务队列。
- SME10594：旧NECESSARY_CORE§2.3–3.2有效核心只支持概念four-pillar治理，无可执行威胁模型/安全保证；作者本轮另实际读精确v1 paragraphs14–50的风险/四柱/阶段/讨论，保留旧已校准最低组织约束P，不升级安全实现或Book新机制。不由耗时或日期缺失改EX。

## 排除项安全门与改判

Anscombe实际独读Rosacea09844 necessary14–51/SUP_REVIEW raw，见独核§11：固定红色ROI及诊断指标无身份真值/re-ID威胁人口/DP评价，Fig5遮脸未作为证据；领域诊断EX但隐私保证未证，不把它留作未读普通门。Chile09871修正为synthetic-persona人口代表性/分项失配窄P；LongText10199原有效Longformer未胜/support-substance confound窄P保持，不能因成熟分类关掉。HGEN只heterogeneous-node/meta-path ensemble未建立主线直接贡献，范围EX而非所有GNN/理论排。

## 具名独核当前层

Anscombe已实际独读MOAT/CDE/Graph本文具名必要段并通过采用限制；RFSeek20–54/62–65、XAgents22–53、DOCUEVAL4–34、CARENLI13–96、Style61–97、SIRBench上述必要段逐项窄P校准实际通过。source及完整六部分仍普通；不将这些局部签名当DAY/FINAL。
