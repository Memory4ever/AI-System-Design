# Jun03 续跑：准入校准与首批必要证据 / 待 root 独核

仅补2026-06-02 BJT自然日，作者 `supp_jun03_close`。已完整重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt与ROADMAP；仅读State2026块、本日最新停点。使用using-agent-skills约束范围与验证，documentation-and-adrs要求保留判断理由；不新增公共合同/ADR或软件实现。Books比较前已读PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE及下列实际owner/邻章职责。只写本日Report/sources，不持Books写锁，不stage/commit/push。

## 本次真实校准

不是用是否有owner、能补限定或整合比例决定准入。原文实际新证据/替代设计若可能改变主线判断即继续；只是把成熟原则改名不能算新增机制。四项完整v1题摘/联合Jun02日证已由R26/R28完成，本批原件与日期字段复用，不第三恢复日期。四精确DOI均arxiv.content/findable，registered依次00467 `2026-06-02T03:52:12Z`、02289 `04:35:48Z`、01202 `04:09:49Z`、00920 `04:02:59Z`；v1提交均在本次适用周一公告截点前且此前一公告后。联合界仍全在Jun02 BJT，字段不是实际公开时刻。

已实际重读四完整题摘：

- 00467可审的是DSF与文本续写memorization分离、提示纠错/损坏人口及错误定义下confidence的实际对照，不是“confidence不是真值”这一成熟原则。拟2+1+2=5；旧JSON初提D3基于“纠错”字样不足，本次不把未识别的因果纠错算3。
- 02289可审的是具体scorer族盲区/外部切片验证，不是2×2新名称。拟2+1+2=5；必要证据后再决定理论“universal”是否成立。
- 01202可审的是depthwise margin/组件记账/真正输入删除的区别及观察人口，不是“稳定不等于正确”口号。拟2+1+2=5。
- 00920可审的是同问题run均值与全R通过的排名/幅度反证。必要层揭示该数字人口矛盾，不能以一般多次评价原则造I；拟2+1+2=5，旧JSON D3反转证据未成立，不按Books处置或工作量改分。

代表性排除复用00947：taxonomic整理与federated隐私议程没有具体检测器/新失效条件，不因能映Ch66准入；01693通用GPU队列没有基础模型consumer，不因GPU关键词准入。两项原完整题摘/明确排除理由沿已成独核，不第三全文。局部/负面结果不被这两个排除模板一并删除。

## 00467 — 必要完成，唯一Ch66小差额提案

[exact-v1](https://arxiv.org/html/2606.00467v1) / [保存HTML](SUP_CLOSE_2606.00467v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.00467)为Oct02 v2/camera-ready，无所见withdrawn/removed/erratum；不倒填v2。实际读v1 §3–5、T1–8、C四回归定义、D.1多轮及E.1/§5限制；未读全提示/样例、代码或复现。

DSF不是直接读出internal concept：让模型解释目标概念，以六sentence encoders的解释—完整任务定义cosine均值作为外部测量。9模型×6数据集54个model–dataset cell，控制dataset后正相关；不能把cell数当54独立模型、embedding一致当因果或无标签选型已部署验证。文本续写ROUGE/BERTScore/cosine代理不正相关也不证明没有训练污染。九模型/五主toxicity数据集各抽1000，API T0；mixed-effects只六核心模型、message随机截距，DSF聚合相关与逐message回归分母不同。推理硬件、precision、完整调用费/时延/SLO未披露，不补闭源参数估计。

Rescue只在原错人口，corruption另在原对人口；定义交换改变任务构念，不是保义paraphrase。T3均值aligned82.0 vszero80.3与§4.2“+2.2”不齐，故不采用该数；“错定义”Fox82.6可高于aligned82.0也禁止单调优越。DSF+0.41仅关联，aligned条件+0.25/p.085亦不能包成全部条件显著；高confidence与错误固着相关不证明原因。D.1每model–dataset100原错、三轮带旧答案/confidence，78.8% Llama8B拒绝drop须另保无有效判断人口，不把18.7% pooled或8.5%高信心恢复授普遍上限、原错不可恢复或任意多轮无效。数据/标签、六embedding、全部定义/示例/DSPy调用和独立gold回归付费；原标签政策、独立人审/可执行检查仍拥有真值。

实际完整读Ch66“Judge先证明看见目标变化”双臂组、“Rubric Formation、Criterion Execution与Ranking”四层/首解释组及后DPO-rubric传播完整组；另读Ch66高信心错误sensor组、Ch65/67开篇职责。现文已承担rubric会错、target敏感/保义不变和confidence非正确性，不能把这些再写一遍。真正尚未承担的是**在标签/政策定义本身固定时，模型被引出的概念定义与目标定义的匹配可作为候选配对sensor，须与文本熟悉、实际救错/损坏两个人口分验**。这不是赋DSF内部知识权限或给出无需gold的可靠门禁。

唯一`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。拟在四层首解释完整段（结束“不能直接同时成为训练 reward 和公开 release gate。”）之后、现“即使改写没有明显改变 criterion 描述”完整段之前补以下单段；现两侧不拆，不新建标题。该处仅提案，未写Books/未独核通过：

> 即使目标定义本身已经核准，还须区分模型对这份定义的匹配与对数据文字的熟悉。可先让模型独立解释待标概念，以解释和目标定义的语义相似提出model–definition配对，再用有gold样本分别检查原错被救回及原对被损坏的人口；[受限annotation对照](https://arxiv.org/html/2606.00467v1#S3)发现定义匹配代理与准确率相关，而文本续写相似未有同向关联，但这不证明内部概念已被直接读出、没有污染或代理导致性能。定义交换会改变标注政策，不同于保义改写；高自报confidence也不能认证定义与预期政策一致。少量任务、聚合相关、拒绝/解析失败和有时更好的错配定义限制外推，全部概念引出、embedding、提示优化与独立标签验收都计费。配对或参考定义不可靠时保留经核原政策、gold抽核和人工裁定，不由DSF或更多纠错提示自行批准批量标注。<!-- source-family:SF-2026-ARXIV-2606-00467 -->

## 02289 DECK — 必要完成，具体NC提案

[exact-v1](https://arxiv.org/html/2606.02289v1) / [保存HTML](SUP_CLOSE_2606.02289v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.02289)Oct01 v2，无所见撤回/纠错；只用v1，不倒填v2 cross-fit阈值。实际读§3–5/T2–4与A/B完整定义，未核代码/全15评分表或复现。三个generator、四短QA数据集/每条件500、五samples T1、top-k15；同target split选best-AUROC族代表且在全500上选YJ阈值，不是独立held-out部署收益。BB/WB不同可观察量不自动统计独立；两轴定义的反对角分歧是构造必然，作者也已承认，不能再当独立验证。

Judge/provider不同不证明训练知识独立。外部label切片有限且有不显著行，SelfAware只unanswerable，regex含“unknown”等即算正确拒答，不认证无矛盾或无伪造；substring reference也不是完整truth审查。§5.3 exact_match常零被解释成“response不匹配unanswerable question”，其与peer-response consistency接口未闭，不能从退化scorer推出所有output检测器必失败。概率很高也仍可在高分范围内排序，不存在由high-confidence/repeatability自动推出AUROC0.5的普遍定理。单NF4末层probe与finite ensemble的近chance不排其它层/读出/有外部知识的judge。API/本地硬件全费用不齐，不补SLO。

actual Ch66在“Judge先证明看见目标变化”后的**完整supervised-ensemble段**已明确BB consistency/tokenprob/reflexive judge/claim信号各有误差面、label/domain-shift/grader-correlation/availability及deployment校准；“相关采样抬Coverage/压Selection”完整binding已承担同源modal错误/多样proposal与外部verifier；“高信心错误几何sensor”及claim-probe组明确probe非truth/外证authority。故保留的可支持长期选择已具体覆盖，不为2×2术语或尚未成立universal桥造I。拟5分标准完成、已有覆盖，不另写Books。全部采样/scorer/标签/校准/外证验收费。

## 01202 Shape of Wisdom — 必要完成，仅报告提案

[exact-v1](https://arxiv.org/html/2606.01202v1) / [保存HTML](SUP_CLOSE_2606.01202v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.01202)Oct20 v2明说以全新研究替代v1 decision-trajectory分析，不是撤回；记录此实质变化，不倒填后版centroid实验。实际读v1 §2–8/T1–4，未核图像素/代码或重建artifacts。

3000四选MMLU×三7/8B=9000轨迹；全panel按decode同letter的token组计分，600/model且四regime各150的traced子集另用单token分数，两个读出人口不合并。Margin=gold−最强错误、drift相邻层差、distance=abs(margin)是依已知gold的诊断，不是部署无标签confidence。正文说tail stable但未给tail窗/阈值，故42.1%“未settled”只保作者操作分组，不能复算稳定定义或借为runtime早退。Attention/MLP scalars线性held-out drift R²不证组件干预；§7 subtraction/substitution是**记账replay**，不是替换实际hidden再run模型，source配对改变结果且长程误差增长。§6删span并重run是真输入干预，但span如何标记/与effect独立的完整规则未闭，不用shuffle证明全语义因果。硬件/precision/推理采样与全费未齐。

actual Ch5从readout→intervention阶梯、Jacobian lens/后续计算读出组、“信息存在/可读/被使用”完整组已具体承担读出与真实干预、最终输出非truth及协议资格。本文新观察值得记录，故不反向撤销准入；但未完整定义的稳定regime与conditional accounting不提供目前可纳入Books的独立稳定控制或计算机制。拟5分标准完成、仅报告；隔离regime比例、attention正向/MLP负向、模拟transplant为内部因果/通用控制的外推。重开需v1明确tail/scalar/span定义及与实际activation干预相符的新证据，后版新研究按其真归属处理，不为它无限追附件。

## 00920 repeated-run — 必要完成，具体NC提案；中心数字不采用

[exact-v1](https://arxiv.org/html/2606.00920v1) / [保存HTML](SUP_CLOSE_2606.00920v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.00920)Oct10 v2明确大幅修订/改题，99题/15,840与v1的100题/16,000不同；只记录对原数必要影响，不读后版全文或倒填其variance结论。实际读v1 §3–5/T1–2与Limitations。

同100新近LeetCode题、16API模型、2prompt、各R5；T.3/p.9但o4-mini不支持该控制，output4096而两reasoning更高budget，不能将思考效应单独识别。执行deterministic不使生成deterministic，新近不证无污染；API刷新、code提取、timeout/无效分母都属identity。公式RLPR=sumY/(NR)、PSR=mean_i[all5pass]、AV按题samplevariance；PSR是观测五次全通过比例，不是单次retry-free概率或无限次稳定。T2 GPT4.1 Detailed PSR47.5%不可能来自N100个binary指示器，未明平均/权重；与其排名反转和精确gap不当已核正面证据。RLPR按500次pooled Wilson还忽略题内相关，不据此授跨题precision。v2新人口说明存在改变而不自动修复v1；完整model版本/CI/逐题Y或明确加权才可定点重开这些数。

actual Ch66“从Pass@k到Pass^k”完整解释/code/边界组已经明确同task隔离重置、outcome vector、conjunction与paired transition；“平均值/切片/不确定性”、Evaluation Identity与harness组拥有重复单位/配置身份，不是泛标题。故最小可支持长期指标选择已具体覆盖，拟5分标准完成、已有覆盖，原定量矛盾明确隔离，不以现象已有数学预期排除实测潜在价值，也不以新测量名造书稿。所有生成/执行/重复与population校核全计费，未复现/核API行为。

## 交付与余项

本包四项ready交root第一次必要/具体owner独核，00467仅请求上述具体Ch66位置，未写Books；其余三无Book写请求。不预正式候选/计数/I/DAY或行政PASS。已成01629 R176与00251 R177另已真实同步报告为123/98I/18NC，不第三必要层。

MODEL原18的本批4之外仍14：01967/00271/01412/00428/00722/00724/01026/01024/01774/02544/02241/01839/01065/00866。02358/00289/CRAM02502/ProtoAda02576另四项普通必要，有限发现收束仍普通；日期/中心争议保留不支持正面保证。下一小批只继续具名材料，不扩NAV或换日。
