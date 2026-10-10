# Aligning Large Language Models with Searcher Preferences 2603.10473v1：必要Source/actual owner受限裁决ready

仅2026-03-12 BJT补充自然日，原日期/候选/§4冻结。准备者mar13_supplement，不自行授非准备者Source/DAY，不写Books。

## 身份、准入及实际阅读

精确主源 https://arxiv.org/html/2603.10473v1 ，SUP_CORE_10473.raw/txt、MANIFEST/RESULT实际GET200，337972bytes，UTC2026-10-10T02:12:34.802326。既有SUP_ABS3_10473完整v1题摘、第三准入独核及SUP_DATE3_10473/独核§23的Mar12日级arxiv夹证有效复用。Current abstract未见撤回/纠错；HTML顶部KDD August2026和ACM DOI XXXX/template不是已证早公开，不用更晚会议模板重开先稿或遍历所有venue。

原窄准入是底线与行为reward的不同聚合责任，不借GRPO/检索或RedNote名声抬分。实际读§3.1–3.3完整必要机制（txt390–1128）、§4.1–4.5及Table1–4（1129–1537）、§5结论；Appendix B人评界面、C/Table5完整定义、D数据集、E完整指标、F说明（2240–2530、2708–2796）。未复现、未核代码，不认证图曲线的精确像素数或所有case真值。必要公式/直接反侧已足，不扩全部references/不相关案例。

## 决定反证：soft-AND reward不是hard admission

§3.3 Eq1 B_delta=exp(mean(log((s_i+delta)/(1+delta))))，Eq2行为utility U为weighted mean，Eq3 R=B_delta U。§4.1.4 delta=.01；正delta确避免log0并给log-sensitivity界，但任何s_i=0时B仍严格正。§4.3.1称“only within the safe region”、§4.4称utility“never compromises”底线；这不是该公式可授的hard-constraint保证。

具体数学反例（本作者推断，不说实际线上已出现）：Table5九底线的m=9示例，一项0、另八项1，U=1，则R=(.01/1.01)^(1/9)约.599；所有底线1但U=.1的合法对照R=.1。两类进入Eq6同组时违规类可高于均值、有正advantage。KL/clipping可以限制更新，并不把该candidate从可行域逐项拒绝；不宣称每次optimizer必提升违规概率，也不否认有限训练改善。这一断点已有公式足够，不以可选代码未读伪造外部blocked。

## 评价、反侧与费用

Human dual-track/blind/assisted + senior escalation是标签制备与校准，不认证全部事实/安全；Table5多底线LLM-based，仅format/length rule-based。Appendix B界面展示policy intent+reference notes，不能从上下文存在直接授accuracy；blind路径和assisted路径人口/最终标签独立性未明确。

同SFT起点，GRPO-Gated vs Linear是有意义的受限对照。Table4本稿同reward system自动评价：Basic .9875低于Linear .9906/RFT .9930，Rich .9832低于GenRM .9840；Hallucination .9836、Evidence .7089等局部改善保留，不复制“全维最优”。T1/2 reward与expert agreement非所有开放安全事件准确；D维度800–3600、holistic2800与RMtrain40000/无标签RL500000不同人口不合并。1000query blind side-by-side人评有独立结果渠道，但未披露本文足够逐维hard safety分母/CI，不能用总winrate认证must-have全部满足。

线上§4.5 user-ID hash modulo同期间各10%traffic，作者声明两侧p<.05、VCR典型CI±.1percentage point；具体运行日期/样本M/按user聚类方法/heldout域明细、BCR audit抽样数与CI Not Disclosed。E的VCR dwell>5s、SR<1.5s、RR reformulation是参与proxy，不等事实真值；BCR日常人审存在局部安全监测而非0风险。保留线上改善方向与原AB数字口径，不从未视觉核的图补造分项值。

§4.1.4 Qwen3-30B-A3B-Instruct-2507 policy、DeepSeek-R1 reward、18H800nodes其中16reward服务，globalbatch128/每prompt16completion/temp1/AdamW/lr1e-6/KL.01。precision、每node GPU数、prompt/output长度、trainingsteps、walltime、线上latency/concurrency/SLO及人工全部费用Not Disclosed。所有标签校准/LLMjudge/16rollout/训练/线上audit付费，150millionPV不是本实验样本。No Supply Reject维度和已有refusal路径不能授执行授权。

## 实际owner、评分与最小处置

ROADMAP唯一TRAIN-RLHF Ch31：本次实际完整顺读230–271聚合邻接，尤其“多目标Reward的Bottleneck聚合不能冒充HardConstraint”两段已具体写算术可补偿/SoftMin分项压力、deterministic must-have gate、归一化/调度/噪声失败及原固定回退；相邻DARC和rubric分支也不把soft selector当安全过滤。584–615消费reward的objective/独立promotion责任已对回。Ch66只owner evaluator资格，Ch72只effect safety，不建第二owner。

本稿新增delta-smoothed geometric bottom-line×behavior arithmetic的有限训练接口与直接反证值得保留，拟2+1+2=5；不是借成熟GRPO原则加分。安全强主张触发必要局部深入，已读完对应方法/评价/直接反侧。拟中心保证争议/暂缓Books0，不把本稿新实验叫已有覆盖，不为了抽象安全原则造两段。可采用有限soft shaping/局部改善事实，不采用strict safe-region/no-compromise guarantee。

精确重开条件：本ID给可执行hard admissibility/threshold策略和reward/advantage的关系，独立分项安全人口与failure/CI、校准身份及等预算评价，才核受影响采用链路；不请求全站历史/无关附件。root非准备者实际Eq1–6/δ=.01、完整Table4与严格主张、Ch31完整局部已核，5分必要深入/中心安全保证争议暂缓Books0通过，正式受限处置，不否定局部收益或全部部署。无PRE/POST写需求、未授DAY。
