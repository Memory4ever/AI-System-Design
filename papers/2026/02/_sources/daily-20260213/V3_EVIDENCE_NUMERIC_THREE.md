# 数学/遗忘三项必要证据（作者判断，待 root Source/Books）

## [LoRA gradient flow 2602.10212v1](https://arxiv.org/html/2602.10212v1)

5=2+1+2，标准完成，拟仅报告。§3–4 sequential/simultaneous更新收敛同gradient flow须步长趋零、uniform bounded iterates、局部gradient有界/Lipschitz，不是有限step配置等价。trace平方toy loss任何rank均可零loss，但不能由此满足任意Frobenius target；trace不看traceless部分。Frobenius目标结论使用SVD对齐初始化、B0=0与指定A0分布/diagonal保持，得到top-r截断路径；标准random init没有同闭式结论。没有LLM同预算rank质量试验，hardware/precision/batch/SLO不适用纯理论结果。

TRAIN-LORA/Ch30 35–60已有“任务更新可能低intrinsic rank”的假设，不是所有loss都需要同rank。此文给两个精确toy-loss counter而不提供真实adaptation有效rank选择条件；仅报告保留loss/init/离散化依赖，不将其写成LLM rank law或新章节。原证 INITIAL、METHOD；NUMERIC_TAIL内10212 L270–313；NUMERIC_SPECIFIC内10212 L200–251。

## [Temper-Then-Tilt 2602.10217v1](https://arxiv.org/html/2602.10217v1)

6=2+2+2，安全受影响深入。§2冻结base，classifier区分retain/forget作density-ratio tilt，先temperature flatten集中base；LLM为pooledhidden surrogate训练+nexttoken logit additive correction，不改变base weights。§3连续混合density假设base准确等于true mixture、classifier excessrisk可控、tempereddensity integrable。retain KL与forget weighted-L1不同；高peak会放大classifier有限误差，temperature降低peak因子同时改变bias/δ收敛率，不是参数删除、DP或真实攻击零恢复保证。LLM token实现不是连续globaldensity理论的完全同构。

§4/F3：TOFU200 synthetic GPT4authors，forget5/10%，Llama3.1 8B，5seed；seed1/2 grid择优FQ后报5seed，不是独立holdout调参。FQ为KS pvalue，不能认证删除；MU-ROUGE高不证明所有generation安全，原条件概率retain大幅下降且SimNPO某MU更高。单GH200、effectivebatch32，T3/ULD ZeRO0、其他micro8×acc4 ZeRO3；precision/inputlength Not Disclosed。T3 100epochs与baseline各5–20不同搜索/训练协议。预processed5.12/7.39s是缓存hidden后的classifier训练，非包含一次basefeatures成本的全pipeline；naive216/431s另列。extrahead、featuresstorage和推理classifier不可由0.03%参数忽略；不采用全端到端156x宣传。

拟PLATFORM-SECURITY/Ch72 343已有单channel suppression≠系统遗忘；新差额可仅为“classifier-guided output tilt的误差与forget-density集中度/temperature bias并列，frozenbase不会凭分布变换删除substrate”。root若认为现有observer/substrate边界已足够，有限OnlyReport，不以主题相似强行Existing。采用机制/条件边界而非正式有限样本指数定理，无需全证明附件。原证 INITIAL L98–220、METHOD；NUMERIC_SPECIFIC10217 L200–220；NUMERIC_EVAL10217 L229–267；NUMERIC_PROOF_LOC10217 L906–913；NUMERIC_MAIN_FINAL L1055–1068/1099–1105；10286_PROOF内10217 L287–291。

## [What Does Preference Learning Recover 2602.10286v1](https://arxiv.org/html/2602.10286v1)

6=2+2+2，设计假设受影响深入。§3–5 CPRD=P(x,y,y')/(P+reverse)，BT在正pair support要求odds可因式为h(x,y)/h(x,y')；PNCI对原P是充分条件。反向定理只构造另一个Q具有相同CPRD，不证明原P本身PNCI。finite/fullpositive case的A464–529已核直接log-odds代数；continuous需可积normalizer，原文construction并未证明任意r下可积，不采用无限space普遍等价。人口negative loglikelihood按comparison分布投影到Bernoulli KL；仅realizable family+global optimum才恢复observed-support CPRD，不恢复唯一true reward或未比较pair。B530–591 grouping证明支持最终CE=H+KL，但中间Eq51–53漏reverse/括号显示滑误；Eq5另缺negative sign，不按这些展示式写实现。

§6–7 connectivity依赖trainpairdistribution、hypothesis class及testQ，margin是目标pair差；不是仅增加条数或图边就保证神经reward稳定。toy finite BT-consistent targetknown实验，较高connectivity主要在其为瓶颈时有益，不能修复small margin，也不等人类偏好correctness或下游policy安全；hardware/precision/serving指标不适用采用的代数命题。不采用完整samplecomplexitybound无需AppC全读。主§6 L253–299及§7 direct反侧376–383已核。

拟TRAIN-RLHF/Ch31 76–99当前scalar/logistic/shift识别，缺“比较人口频率加权的拟合对象/不可实现时projection，而非恢复一份真实absolute reward”；可一短段承接原BT目标，写finitepositive赔率可分解条件与PNCI只充分，observed support/global optimum限制。不授原P independence必要、不照录Eq5，也不借通用likelihood成熟原理多计分。原证 INITIAL/METHOD、NUMERIC_SPECIFIC内10286 L200–251、NUMERIC_MAIN_FINAL L209–299、10286_PROOF L464–591及NUMERIC_EVAL内L376–400。

## 10217 旧 PRE 最终处置（作者）

改为仅报告，不制造整合。实际Ch72 L343已承载substrate/observer跨channel suppression边界，L2583–2620实际unlearning正文区分重训参照、局部行为、classifier/attack域与不可恢复；不是因为主题同义就称此算法已覆盖。新temperature×有限classifier-error的density集中度权衡仅在精确base mixture、可积/continuous density条件下成立，LLM pooled-token surrogate不是该理论同构；当前TOFU协议/调参人口与端到端成本不能支持一个新的普遍部署规则。保留该具体替代输出配方、原有限反侧与root必要证据复核，不授参数删除，Books为Only Report。

最终状态同步（2026-10-04）：当窗三项必要源/处置已独立复核；10212/10217仅报告，10286 Ch31实际正文/邻接/末注已root非作者POST通过。10217旧PRE未被虚构落实，具体Only理由已收束；日级另验。
