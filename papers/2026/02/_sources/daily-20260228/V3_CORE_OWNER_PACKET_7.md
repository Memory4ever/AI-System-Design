# 第七包：本窗必要证据与具体owner差额

仅本日AB5已校准潜力的八个必要材料，不把15次可读抓取算审阅完成、不扩宽标题库存。原v1 abs与HTML身份见V3_FETCH_AB5_NECESSARY；各v1 Submitted在2026-02-26 UTC，晚于官方公告政策所需2026-02-25T19Z下界，结合本窗same-ID registered恢复公开范围，非Submitted即public。共同下界2026-02-27T09:00+08，上界为下面registered加一秒后转+08（不含），均完全落窗。当前评论轻量检查不复跑版本diff。

| ID | same-ID registered UTC | 本包判断 |
| --- | --- | --- |
|22562|2026-02-27T02:49:17Z|6，Ch72窄差额待PRE|
|22570|2026-02-27T02:49:28Z|7，Ch66窄差额待PRE|
|22575|2026-02-27T02:49:35Z|6，root中心D终态已通过|
|22576|2026-02-27T02:49:37Z|5，once准入通过，Ch33窄差额待PRE|
|22579|2026-02-27T02:49:41Z|6，Ch66窄差额待PRE|
|22581|2026-02-27T02:49:44Z|5，公式子命题隔离，Ch5窄经验差额待PRE|
|22585|2026-02-27T02:49:50Z|5，跨policy排名隔离，Ch66具体Existing待PRE|
|22586|2026-02-27T02:49:51Z|5，once准入通过，Ch24窄差额待PRE|

## 22562 MUTE — 2+1+3=6，Ch72层选择差额

实际必要blocks24–62/67–98/130–153/189–193（首次截断43–59已恢复）读足。三7–8B模型先用同MMLU/MMMLU题目LoRA注入，化学QA只是可控事实遗忘proxy，不开展AIforScience应用；CKA比较各层对齐并用LRDS选中层，然后仅该层RMU/SLUG/SimNPO。优化语言EN/ES/PT外的语言未参与unlearning优化，却参与全语言CKA选择，不能称从未访问heldout语言。单模型浅层会同时毁retain，深层又不能消forget，中层依算法改变，SLUG某中层仍retain近0，其他设置仍forget残留；不保证唯一深度或无损。logit-lens小概率与低QA accuracy不授不可恢复删除，且注入/选择/评测共题不授heldout知识泛化。CKA、敏感数据消费、层搜索与微调/攻击复测都付费，硬件/完整预算Not Disclosed。

Actual Ch72 3111–3125已经承载跨语transfer/regain、retain utility、representation只诊断、refusal非erasure。具体尚缺**共同语言activation对齐选择可编辑层，并把浅层collateral与深层erase失败作为同算法受控分支**。拟在该小节一段，不重复发布安全合同；保全语言选择权限、共题控制、读出非删除与原重训/限制发布回退，请授Ch72窄lease。

## 22570 Guidance Matters — 3+1+3=7，Ch66可比基线差额

实际31–61/62–85（55–74截断补读）足够。将采样更新投影到conditional−unconditional方向定义effective CFG ratio，时间均值用于匹配baseline；ratio以norm丢符号、推导绑定DDIM类更新，匹配均值不是逐step轨迹因果等价。TDG故意用随机empty-token弱条件提高某些proxy作反例，不是新实用sampler。SDXL/2.1/3.5与DiT有限prompts/T50或32、原CFG及e-CFG对照；匹配后不少“新机制”胜率缩小，Z-Sampling/CFG++仍有局部优势。HPS/ImageReward/CLIP等随CFG改变，AES不测prompt-following，未实际人评不能认证“真实人类质量”。FID/IS与semantic属性是不同目标，不能说所有guidance无用。新增第三forward/分解/采样与多proxy评估有费，hardware/precision/生产SLO ND。

Actual Ch66 4282–4286只承载相近FID聚合掩盖不同failure，不含**sampler隐式放大guidance量与弱/无效方法也提高preference proxy，需要effective-control-matched baseline才判独立增量**。拟该处单段，保有限projection/mean matching非等价、proxy不是真值与已有固定CFG/人工独立质量回退。Ch24 1356–1361机械guidance预算已有，不在Ch24重复评价原理。请求Ch66窄lease。

## 22575 S2O — 2+1+3=6，中心D已实际独核通过，无Books

原43 Algorithm3与46/48/50明确standard online-softmax (m,ell,acc)，停止却用ell'-ell<tau*ell后break、下一行才commit。作者反例：intra初始化m0/ell1/acc0（score0,value0），新历史tile score10/value1，新m10/ell'=1+exp(-10)，tau.005使gain4.54e-5被判小而丢主导key，返回0，dense≈.999955。不同running-max gauge的差不是新mass。root已实际读最小原段并核反例，中心所写算法保证争议终态隔离；不宣称实际code同错、经验无效或全部排序思想无价值。实验必要24–81与114–120已读；retrieval O(L²/S)、HBM中间buffers/gather都有成本，prefill operator CUDAevent不是服务SLO。重开只需同gauge gain/commit修正及对应实现证据，不遍历全proof/code。

## 22576 Search-P1 — 2+1+2=5，Ch33 reward分支

once31–48/65–72/148–150已由root实际准入；必要85–89/103–110继续读足。Rpath=max(self-plan score, privileged-reference score)：self分母计执行/计划覆盖与效率，reference按语义匹配且order-agnostic，以max保替代路径；两个singletrack去除直接负侧，不是仅reward-shaping改名。reference teacher看gold并offline rejection/vote，自己的计划自一致不授truth；semantic matcher和partial-outcome judge均有偏差，8B evaluator换代有accuracy反退。90K reference avg1.91calls、训练多rollout/judge不可抹去，inference无judge不等总免费。正文与B default soft-outcome衰减参数不一致，不写精确唯一实现；max又不能保证anti-gaming或高quality定义。精确harness/失败人口和GPU配置不完整，不能授通用预算支配。

Actual Ch33 268–279已承载reference-step partial credit/teacher权限与outcome guard，尚缺**self-plan与gold-conditioned-reference两个不同分母以max形成训练credit，以及用轨迹效率而非步骤数量单独奖励**。请求其过程reward附近一段，不把self一致当环境事实，保teacher费用、matcher反侧与outcome-only/可靠process-verifier回退；planner只消费已训练policy，不在Ch79重复reward公式。

## 22579 VLA Metamorphic Testing — 2+1+3=6，Ch66关系oracle差额

实际24–46/54–89补齐截断46及54–67。TC同义/无关object/brightness要求Frechet<=delta；TV否定要求>=delta，target平移要求alpha|dp|<=d<=beta|dp|。语义不变/反向改变、可达性、多有效轨迹和随机重复才使关系有效，偏离关系不自动goal失败/physical unsafe。原象征终态成功1864source→9320followups、5VLA/2simrobot/4任务；不是所有政策同finetune recipe，所用checkpoint按作者来源分别训练。一个fixed seed、经验percentile阈值.1/.2/.3米、192两expert样本刻意分层而非simple iid危害率。GPU A6000/4080异构、EO1执行硬件ND；61h是作者测试代价非模型可比速率。某总数与分项不一致，不采统一failure率；sim关系violations不授实机安全。

Actual Ch66 2844–2849具体stage witness及safe/unsafe twins已有，3715–3717具体corpus mutation亦已有；尚缺**无完整trajectory gold时，用可证明有效的输入变换声明轨迹应保持/应变化/按比例变化，再与terminal oracle并列**。拟具身stage witness后单段，保Frechet/threshold只是关系sensor、共seed与success-conditioned人口、人工/物理oracle回退。请求Ch66同窄lease第二单段，不用机械距离签发安全。

## 22581 IBCircuit — 2+1+2=5，Ch5局部经验差额

实际28–73/82–123、153–171对应中心公式局部足够。以batch均值/方差Gaussian替代被削弱activation，联合学node/edge sigmoid gates，以原output-KL保局部行为、正则与阈值控制紧凑度；training不需corrupted-input pair不等无noise，也不等eval无corrupted：96删除未选component仍用corrupted activation patch。GPT2small IOI/GreaterThan+XL IOI限定，ACDC在GreaterThan low-node更强，更多正则增KL、hard-mask任务score可强而fidelity不同，不能取统一最优。1300/3000epoch/门选择与eval有费，hardware/precision ND，output fidelity非唯一真实因果。

公式子命题隔离：60–61 Eq9定义A=-sum(1-lambda)<0，logA未定义；153–169 Eq26逐项Gaussian KL成立，但Eq28错误把sum(log)/sum(square)合成log(负sum)/square(sum)。不采用该闭式或完整IB担保，不无差别审全部proof；保局部控制结果与可定义逐项目标，实际实现未核。重开所需是明确实际regularizer与匹配实现/控制，不照本笔记自行修paper。

Actual Ch5 304–318已承载replacement fidelity、pruning、干预/可达证书，尚缺**训练时以原output约束联合噪声门，而非手工构造corrupted input选择路径**的受限拟合分支。拟faithfulness-budget附近一段，仅Gaussian gate/output-KL经验与代理/成本；完整理论、因果minimality均不采。请求Ch5窄lease。

## 22585 Rater Bias/Rasch — 2+1+2=5，Ch66具体Existing

实际23–66/68–72/103–108足够。MFRM ordinal logits拆output/item/rater severity及threshold；需跨rater-output linkage，不是每例加3–5票就可识别。639articles/19policies/15raters/6312ratings，371double-rated组合及短4item，skew使kappa与agreement对象不同。severity诊断只是模型条件估计，unidim/依赖检查不证明构念真值、极端rater不自动错误，meta-eval/rubric仍必要。

跨policy重排子命题隔离：51各policy独立fit，jointpolicyfacet因identification不可估；59/69称跨fit rank有意义，但theta/rho共同平移可各fit独立改变单位/原点，未给共同anchor。不能采用调整后RLHF必胜human等排名，也不泛称IRT无效。

Actual Ch66 301–318已具体承载测量scale未识别、同pairgraph/anchors与Unknown/并列、共同rubric才能跨query汇总；2659–2679承载item/rater/repeat方差、同质votes不补rubric。**linked-rater severity诊断不取代共同尺度/construct校准**已实际覆盖，拟Existing，无新正文，请独核这两个实际范围。

## 22586 TabDLM — 2+1+2=5，Ch24 mixed-type路径差额

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；连续numeric codec、shared clock与双loss分责；copy反侧及schedule费用。2+1+2=5，Ch24自身末注1766；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：§2.2–2.5、blocks32–72/94–98/117–118/182/195–198；连续数值codec、共享clock与双loss接口；copy负侧、shared schedule/codec费用和AR回退。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

once32–72/94–98/117–118已root actual准入，180–199必要训练/采样接口再读足。frozen float encoder/decoder＋trainableprojection，将continuous numeric latent放placeholder，以Gaussian corruption；text/categorical仍MDLM mask，共享time clock双objective/decoder，LoRA LLaDA8B对matched LLaDA SFT。采样同一步先tokenunmask，再numericEuler update，型别/clock/schedule/placeholder身份共同绑定，而非数字文本tokenizer换名字。A10080GB bf16 fixedseed/各datasetepoch，float基座pretrain也有费；numeric/textlosswarmup与perfeature schedule为选择，不授最佳。MathExpr/ProfileBio分布/趋势优点伴deterministic copy反退，sharedclock可能非optimal；慢MDLM sampling/未来cache未implemented。训练recipe相近不等总cost/基础知识预算完全matched，不取应用质量为全模型通用保真。

Actual Ch24 274–280与334–336分别拥有异步history-noise支持及continuous/categorical严格duality，不含**同一foundation backbone中连续scalar与masked token两类corruption/readout并行耦合**。拟连续高斯→文本交接后一段，保numeric codec/双loss/有限实验与文本化数字/独立两类模型回退。请求Ch24窄lease（若与27实际同文件冲突短排队，其他项不等）。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22576：原必要blocks31–48/65–72/85–89/103–110与actual owner独核；Ch33正文283/完整273–293/own2952 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）本项落实：22581：2+1+2=5，output-KL联合Gaussian gates，错误闭式/IB保证隔离；必要原v1/直接反侧与actual owner独核，Ch5正文322/自身634及完整邻接root非写入者actual POST通过。保原有效身份/精确版/采用命题，必要原段见本项；作者已实际顺读，费用、人口、错误子保证和原路径回退近正文，窄锁释放；不授全附件/实现复现或日级。
