# 2025-11-12 关键反侧与纠错校准包

作者：Noether。准备：2026-10-04T20:24:00+08:00。Ohm21:02:19已实际有限复核，两个窄限定作者同步见末段，整体回核尚待。
只授下述实际读取范围；不是整日 Evidence/日期/Books 完成。首批见 [FIRST](./FIRST_CALIBRATION.md)，第二批16项方向见 [SECOND](./SECOND_CALIBRATION.md)。本轮 native 请求及完整/部分响应边界见 [执行](./12-critical-native2.json)。

## 已准备的受影响核心

| 身份/原始材料 | 实际已读及裁决 | 仍不支持的命题 |
| --- | --- | --- |
| [2511.07482v1 AAPP](https://arxiv.org/html/2511.07482v1) / [raw](./safety-aapp-v1.html) | alignment-critical channel保护、risk gate、历史状态/评价集、Table1及紧邻解释实际读。C4与WildJailbreak校准；测试held-out WildJailbreak，Llama2-7B-chat/Qwen2.5-14B/Gemma3-12B，300输入/120输出、batch20、20轮刷新；FLOPs是2/MAC估算，不是实测TPS。Llama r=.3 Table1 PP F1/.Acc/.FAR=.645/.624/.313，AAPP=.760/.741/.254；紧邻prose给另一组PP .585/.575、FAR .353→.216，**表文冲突保留**，不择优照录。作者承认大比例剪枝毒性下降可能来自语言能力退化。准入潜力保留，安全保证关闭。 | refusal分类器/toxicity proxy不等于真实有害性、全面过度拒答与production安全；不将FLOP降本视作实测加速。日期未核，不正面采用、不请求Books。 |
| [2511.05797v1 Plugins](https://arxiv.org/html/2511.05797v1) / [部分raw](./safety-plugin-v1.html) | §VII-C/§VIII-C、responsible disclosure及讨论实际读；原响应468481/552628bytes，不能写完整附件已读。历史伪造漏洞Oct2024披露、P1 Dec服务端修补/加固prompt后tool-instruction攻击仍有效；P2提醒不等于修复。增量是具体第三方role序列/信任边界的失效，不是把通用prompt注入原则当新机制。 | 不授所有插件/模型都失效、hardened prompt完全无效；不同supplier与不同攻击不合并。当前v1提交仅发现字段。 |
| [2511.05804v1 Spectral](https://arxiv.org/html/2511.05804v1) / [raw](./safety-spectral-v1.html) | 实际§7完整限制：118 controlled context-statement样本，Llama/Qwen/Phi3，中文/法文仅初步；自然NQ/Hotpot/SelfCheck/semantic-entropy、长上下文>=512、多轮自由生成与对抗redteam仍future。Bayes最优依赖two-regime mixture/MLR条件。保留小样本检测方向。 | 不授通用agent kill-switch/生产恢复/audit/HITL已实现。前面较广长上下文措辞不消掉§7未来工作边界。 |
| [2511.05852v2 Edits withdrawal](https://arxiv.org/abs/2511.05852v2) / [原v2](./edits-v2.html)、[current](./edits-current.html) | 本轮实际读取v2撤回说明和current history。原声明因author order、status错误、article尚未published请求retracted；history明确v2 withdrawn，submitted `2025-11-12T09:17:35Z`。本次不采用该撤回版本，也**不回用v1的232配置作正面证据**。v3 Dec7/v4 Jun2026再公开不是本窗替代；当前254配置及新题名不倒灌v1。 | 不称全部版本永久无效，不把行政记录错误误写成实验造假；submitted不是撤回公开时刻，v2时间字段已经在本窗终点之后。v1潜在编辑/适配交互方向只保留恢复线索。 |
| [2511.06852v1 DBDI](https://arxiv.org/html/2511.06852v1) / [raw](./safety-dbdi-v1.html) | threat model、Eq8–10、关键评价、Table2–6及实现成本原说明实际读。白盒weights/hidden states/实时steering权限，跨benchmark校准/测试、greedy T=0，AdvBench/HarmBench用LlamaGuard3，StrongREJECT用其harmfulness score。Llama2-7B的97.88%是**simplified prompt**，official template 95.96%；两向/顺序/层选择是具体机制。Table5 TwinBreak来自原论文而非统一重跑，HarmBench 91% vs94%并非全赢；ASR表有95.46/95.96差异，保留局部冲突。 | 不外推黑盒部署/所有安全alignment只有两维。未干预时weights不改不证明干预时一般能力不受损；15–25秒/层offline与online线性操作不同成本，不合并为端到端速度保证。 |
| [2511.06125v1 QUEST-LOFT](https://arxiv.org/html/2511.06125v1) / [部分raw](./correction-quest-v1.html) | 原gold纠错流程、§3模型/检索/Justified QA与verification、§4新旧评价、§7限制实际读。100test/10dev/328entities，作者合并gold和各方法答案后人工查snippet/full-doc/web，MATCH/NO_MATCH/DEBATABLE；从双方移除DEBATABLE。Gecko embedding、top40 RaR vs全部128K CiC，Gemini1.5Pro/Flash。Pro RAG .67→Justified .81→verification .83 F1，但CoT版.76/+.verification .74，不能称每组件都增益。 | 小集、test迭代可能overfit；作者人工curation不是盲独立ground truth。基线fewshot与Justified零样例/结构改变，不归因单一reasoning能力；不授全部RAG胜long-context。部分242143/650219bytes不是全附件已读。 |
| [2511.06668v1 Contradictory evidence](https://arxiv.org/html/2511.06668v1) / [raw](./negative-contradiction-v1.html) | §3.2–3.5/§4、Table2、§5.4实际读。1476 TGA medicine/8856queries，1074有证据；PubMed1975–2025、up-to20 temporal/citation pool、固定K=5，bge-small/FAISS。SPECTER句pair相似>=.75后PubMedBERT-MNLI/MedNLI peak contradiction；most-similar/most/least-contradictory使用不同选择条件。五模型T=0/max256，ROUGE及同embedding语义指标。保留“语义相关与证据一致并非同一轴”的局部负证据。 | 选择条件同时改变relevance，不能把全部下降纯因果归于contradiction；Table2各模型R1下降不一致，不照录18.2%为普遍率。句级NLI≠临床truth/安全评价，不引入医学机制/诊疗建议；只English且可能漏文档级矛盾。 |
| [2511.05682v1 VMDT](https://arxiv.org/html/2511.05682v1) / [部分raw](./negative-vmdt-v1.html) | safety数据/§2.2/§2.3、C.1.3评价及human agreement实际读。T2V780、V2T990，两种模态不同risk集合；BR refusal vs HGR harmful output不能合并。短于10秒video均匀10frame、GPT4o-2024-08-06 judge；两researcher435样本平均85.5%agreement、interrater .830 **仅T2V验证人口**，不是跨模态统一验证。V2T另有自己的验证人口，提供细视频描述辅助judge，非纯video直接判定。转写/变换场景HGR更低可能是能力不足而非安全。 | 不授所有视频模型整体安全随scale增减；不同模态/模型家族/场景不混成同一因果量。原599400/1675175bytes部分；完整§K和所有风险附件未读，不冒称全套核验。 |
| [2511.07112v1 More Agents](https://arxiv.org/html/2511.07112v1) / [部分raw](./negative-math-multiagent-v1.html) | §4模型/benchmark、§5主要方向/§7完整限制实际读。六open模型、GSM8K/MATH/MMLU-math/MultiArith；same-model独立sampling+majority，1→5主要收益、>=10饱和，punctuation/WikiTypo/R2ATA不同。§3.3文字条件翻错率与公式分子缺clean正确mask冲突，不自动有[0,1]界；不直接采用该ASR条件定义/数值或定量稳健性保证，也不只以task分层消解。未核代码，不断言实现必错，潜力保留。 | English math/字符扰动不代表agent safety；无adaptive adversary、debate/verifier/cost-aware策略。regex答案抽取与shared-model相关错误可混杂。部分347301/672133bytes，不授all appendix。 |
| [2511.06448v1 Fraud](https://arxiv.org/html/2511.06448v1) / [raw](./negative-fraud-v1.html) | §4.1–4.3与Limitations实际读。110 simulated agents（100benign Qwen2.5-32B/10malicious）140posts；conversation conversion≠population impact。R1开collusion17→41%population、35→60.2%conversation，malicious V3的benign model容量对照32B/72B/DeepSeekV3效果不同；1000/100scale轨迹不授现实普遍率。 | 模拟LLM行为不等于真人被骗率/真实转账证据，模型能力与风险相关不授因果；不同benign模型/场景与双指标不拼接。 |

## Oracle精确复用边界

2511.06073v1完整AB本日已读。为同一原v1的SHACL采用边界，定点实际读取11保存的 [PDF身份原响应](../daily-20251111/nov11-critical-identity.txt) 与 [PDF §6.2–6.3](../daily-20251111/nov11-source-final-details.txt)，不是继承11候选/来源覆盖。原PDF题头是Licensing Oracle；错误索引标题只隔离那条索引，不授论文通篇无效。PDF明确complete formal KG假设；incomplete/out-of-scope需abstain、imprecise predicates、ambiguity/time-dependent尚未实现、多跳单triples有效不证明复合答案。保留这条限制；没有把needed&sufficient措辞当通用真实性定理。本日未声称重新完整审读其全部方法，root11已核的同一v1反侧只复用相同命题。

## 最小日期恢复与未核范围

上述arXiv v1 Atom published仍是submitted发现字段，公开落窗未获得；有限恢复见 [SECOND](./SECOND_CALIBRATION.md)。本包只为重要纠错/安全/中心反侧保留必要证据，不继续展开全部实验。正面采用、评分、Books均未授予。原始有日期版本/重要公告到达时只重开该ID及依赖命题；不要求全owner/所有附件。

请root/Ohm/Carver独立核本包范围及处置，特别是Edits撤回不得回用v1、AAPP/DBDI表文冲突、QUEST revised-gold/CoT反侧、VMDT judge与frame抽样边界、Fraud simulation两指标。其余普通题摘理由正在落盘；这是小包ready，不等日级完成。

## 独立发现的两项公式边界窄修

2026-10-04T21:00:17+08:00，作者实际回读本日原HTML受影响段，保留[Ohm FIRST最新§5](FIRST_INDEPENDENT_REVIEW.md)/[SECOND§3](SECOND_INDEPENDENT_REVIEW.md)发现，不推倒其余有效核心：

- More Agents §3.3文字称ASR是clean正确样本被扰动翻错的条件比例；印出的分子却只有 `sum 1[f_n(A(x_i)) != y_i]`，没有clean正确mask，分母为clean正确数。因此公式不等于该条件翻错率，亦不自动落在[0,1]。未核代码，不能断言实现必错；保留局部ensemble/噪声潜力，不正面采用该ASR条件定义、数值或定量稳健性保证。日期仍隔离，最小重开是同版本勘误或该metric配对mask的实际实现/原计数，不为未采用项全读代码/实验。
- AAPP Fig2称更接近harmful时门控触发，正文Eq2的KL距离后却以 `KL_harm-KL_safe >= tau_margin` 保护harmful历史活跃channel。距离小才更近，本核心没有阈值符号/实现解释让两者可直接等同。门控正确性未验证，保护机制潜力与既有Table1/prose冲突保留；只在拟采用时补同版阈值/勘误/实现，不无条件称已验证risk detector。

作者普通理由已收束；THIRD及其余118完整AB/17标题关闭的必要独立范围仍待实际结论，不将SECOND16通过扩大为全134通过。

## THIRD最新两处同步及新增公式边界

2026-10-04T21:07:47+08:00实际读[Ohm THIRD](THIRD_INDEPENDENT_REVIEW.md)21:02:19后，More Agents行已保留条件定义/公式冲突，VMDT行已补435/85.5%/.830仅属于T2V；作者定点回读本日原§3.3与C.1.3/C.2.3验证段，不混合模态人口。请Ohm仅回核这两处与README对应限定，不重读其余有效反侧。

另实际回读DBDI原Eq4–6：harm方向文字先定义 `u_raw` 来自harm差矩阵、mask为 `m_harm`，Eq6却用 `v_raw` 与 `m_harm` 归一化。保留raw向量符号/提取文字不一致，不正面采用该式为实现正确性；原式mask确为harm，不能误写成refusal mask。未核实现/勘误，不全代码审计。既有两向机制潜力与表文冲突不因此关闭。

Ohm THIRD §3已实际对照Books必要owner及交接，支持GPT两个方向仅报告、拟共享差额0；作者具体正文对照一致，最终采用该处置，没有Books写入/POST对象。其余普通分层、十四来源/六部分DAY仍待实际非作者，不自授完成。
