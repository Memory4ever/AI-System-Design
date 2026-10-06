# 本日必要原源证据与actual owner差额

2026-10-06续跑：以下B12～B26“拟/待核”和旧50/98计数保存原作者prepared时点，不是当前队列。当前150工作家族均已有逐项必要原证终态（29 I/81 E/27 Only/13 D），普通剩0；逐项终态以相应原CORE_OWNER_PACKET顶部非原作者复核段及2026-02-26 README为准。既有51由root原证/owner核，本次其余99由feb26_close_oct06作为非原packet作者定点原源/actual owner独核；10处新增Books全部root非写入者actual正文/完整邻接/自身末注POST通过。理论只读采用命题/关键反证所需，不宣称所有proof逐行审、artifact绑定或复现。Report六部分独立final仍待root验收，进行中；不以prepared自签完成或重扫全月。

## 2602.20400v1 — Three Concrete Challenges and Two Hopes for the Safety of Unsupervised Elicitation

日期：官方公告规则下界2026-02-25T09:00:00+08:00至同ID Registered秒精度上界，完整落窗；原字段见V3_DATE_PACKET.md。评分3+1+3=7：纠正无监督truth elicitation从理想基准到未知监督用途的评价外推，不是给现有UE术语评分。

原源：https://arxiv.org/html/2602.20400v1 。当前完整原文 V3_CORE_2602.20400.raw，可读行位置 V3_CORE_2602.20400.txt：§3.1/3.2行360–503；§3.3行504–768；§4.1–4.3行775–842；§5行845–863；Appendix D/E行1950附近–2001。已读足拟采用的实验构造、方法、结果与关键限制，不声称实现或复现。

实际支持：easy/hard信息权限固定且test labels仅评价时可见；GSM8K正确/错误配对添加独立spurious feature，LIAR/Civil Comments分别切换target；Ctrl-Z变50/99/100% safe训练分布；GSM8K与normative political claims混合用relative confidence衡量分数方差。Llama3.1 8B（salience/imbalanced math）、70B（impossible）、两者（Ctrl-Z）的提示与linear probes只读next-token/activation，不含CoT。显著非truth特征可夺走probe，prompt指定target仍不足。真实稀有恶意监测的训练分布比平衡数学更脆弱；AUROC好不证明在无objective truth输入上低confident。

关键反侧：不写所有imbalance都失败。100%错误GSM8K上CCS/PCA可相当甚至更好；Ctrl-Z 99/100%safe时70B E2H达0.87而8B仅0.67，故能力/方法分支不合并；PCA ensemble、bootstrapped prompting存在特定例外。Impossible混合有不真实跨数据集shift，作者承认部分方法按source分离；normative标签不是政治真值或模型moral status。作者未测SFT/weak-to-strong、scheming干扰或全部mitigations，不授UE整体不可能。

采用边界：只采用stress-test需要区分latent显著性、类别比例与答案可定义性及局部失败/例外；不采用通用监督安全保证、内部deception识别或生产风险率。§3.3对UE probe方向取max AUROC，单类supervised comparison亦涉及该方向选择，是评价标签消除正负方向歧义的oracle方向，不能当部署自动知道truth方向。训练/评价样本重复与误差条未充分披露处保持Not Disclosed；不引用未能核对的普遍置信区间或性能数。这里不需要硬件/服务SLO，因为拟命题不是推理系统速度收益；hardware/precision属Not Disclosed，模型/数据/判分身份如上。

actual owner：PLATFORM-EVALUATION-SYSTEM，books/part-06-ai-infrastructure/66-evaluation-system.md。已实际读现有Observed Capability与Elicitation Ceiling段、salience/imbalance/elicitation相关正文检索及章节交接（Ch65尾、Ch67开）；当前177–191拥有监督预算与latent不可识别边界，却没有三个UE基准轴或“不平衡数学可工作、rare malicious失败”的反侧。拟在180既有elicitation probe段之后插入下列两段，接回原有同压力配对测试，不改旧能力lower-bound论点。

拟正文：

无标签 truth score 还要分清“模型最容易发现的特征”与“任务要判断的真值”。在目标清晰、类别平衡、每个样本都有可定义答案的旧基准上，unsupervised elicitation 或 easy-to-hard probe 可以提供有用的能力下界；转向未知监督用途时，EvalSpec 应另设显著但非目标的特征、训练类比例、以及无唯一客观答案的输入三种压力，保存 target prompt、easy/hard 信息权限、model revision 与 held-out 判分身份。改变提问目标不保证 probe 不再追逐显著特征，数学正确性上的高 AUROC 也不证明规范性陈述会获得较低置信。实验对UE probe取较高AUROC的正负方向，使用了评价标签消除方向歧义；部署没有这些标签时，不能假定sensor自动知道哪个方向为truth。这里的 truth score 仍是受测分布下的 sensor，不拥有规范真值。

三种压力不能合成一个“无监督方法失效”标签。[受限对照](https://arxiv.org/html/2602.20400v1#S4)中，全错误数学训练集上的部分 probes 仍可工作，几乎全安全的命令训练集却较难识别稀有恶意，且70B easy-to-hard分支保留改善；答案可定义性测试又有跨数据集混合的人工分布偏移，未覆盖 SFT、weak-to-strong 或全部缓解法。压力切片、监督 ceiling 和独立标签增加数据与调用成本；不能获得用途相关校准时报告 Unknown，保留人工/独立 verifier 与保守权限，而不把一致性、集成分数或 balanced benchmark 认证成部署安全。<!-- source-family:SF-2026-ARXIV-2602-20400 -->

完整拟邻接：

前文：对同一 model revision，可记录 zero-shot baseline、弱监督 SFT/RL 后的可观察提升、监督来源及其可验证范围；elicitation training 只能作为 probe，不能反向证明内部真实最大能力或“欺骗已被解决”。它换来更强的 capability lower bound，却增加训练成本、distribution shift 和对 model-organism 假设的依赖。作者在人工训练为 sandbagging 的模型及数学、科学、代码任务中观察到弱监督可恢复部分表现，不证明真实部署模型普遍可被同样方法揭示；监督不可靠或风险过高时仍需独立 verifier、权限收缩与保守 release Gate。

后文：识别能力与监督效应还需要同压力下的配对条件。先在中性任务确认可观察能力，再在压力条件比较“无监控”与“声明正被监控”的工具选择，才能把能力不足、压力诱发的行为变化和监控敏感性分开；不能由一次正确回答或被监控时恢复表现推断所有场景都可靠。监控声明本身也是prompt干预，应与模型、任务和解析协议共同冻结。<!-- source-family:SF-2026-ARXIV-2604-26511 -->

拟Review note：`SF-2026-ARXIV-2602-20400` — Daily2026-02-26，exact-v1 §3.1–3.3、§4/Fig2–6、§5与D/E；3+1+3=7。仅采用三轴stress-test与局部例外；probe max-AUROC方向用评价标签，是oracle方向而非部署自动truth方向；all-incorrect math仍工作、70B E2H改善、normative混合shift及未测SFT等反侧就近。未核artifact/复现，不授内部truth或部署安全；实际source→owner PRE/锁/POST及日级验收状态按后续真实结果填写。

状态：root必要源/actual owner PRE通过，授Ch66两段+ownnote窄锁；已实际写183/185，作者顺读完整175–194邻接及末注。root非作者实际POST通过并释放窄锁。Books=整合，不授本日完成。

## 2602.20296v1 — Learning to Solve Complex Problems via Dataset Decomposition

日期V3_DATE_PACKET当前Submitted下界与Registered上界完全落窗。评分2+1+2=5；标准审阅后，actual TRAIN-DATA里没有递归子题→概念依赖/结构分支difficulty→课程order及同教师两次答案非独立验证边界，属具体长期数据缺口，深入相关机制而不改评分。

原源：https://arxiv.org/html/2602.20296v1 。V3_CORE_2602.20296.txt：§3.1行238–405，§3.2行793–1203，§3.3行1204–1354，§4.1行1475–1549，§4.2 Tables1–3/同池random-order反侧行1550–1750，§5行1936–1963。已读这些拟采用核心；题摘不是普通teacher拆题换名：原解答step变子题，带/不带原context各解一次，symbolic verifier比较两次numerical answer；递归问题树映成tag依赖图，同义tag embedding聚类，difficulty=alpha1×直接子节点数+alpha2×概念图depth，按quantile课程阶段训练。

实际比较：Qwen2.5-1.5B/Qwen3-4B-Base；math teacher GPT4o、code teacher o4-mini；MATH500、AIME24训练/25测试各30题，CodeForces C++CoTs训练→Python HumanEval测试。BF16、AdamW1e-5、batch16、5epochs、三训练seed、A10080GB、temp0 pass1。与original SFT、same-teacher direct distillation、MetaMath/MuggleMath及同一Decomp池random-order比较，作者称同设置内训练compute matched；不能推成包括teacher generation/retry的总成本相等。课程order独立的增量比整个decomposition收益小，MATH约0.8pp/AIME3.4pp，不把两者headline收益合并归因。

关键反侧：同教师带/不带context答案一致且symbolic同值只核数值一致，不独立核子题语义、概念tag或真实正确性。Depth/branch是数据构造proxy不是student真实difficulty。作者明言teacher需可靠分解，非math结构未必可拆，错链会被递归放大；同规模自改进、weak-to-strong是未来设想，不在实验支持中。不能认证high-risk场景或任意curriculum；增加teacher调用、retry、tag图、阶段训练与独立holdout成本。

actual owner：TRAIN-DATA Ch27，books/part-04-training-system/27-data.md。已读合成spec/curriculum论证及开篇和Ch28交接；当前498–501拥有可验证environment组合，503–530拥有failure-driven tool课程，均不是从既有解答递归构造子题并用图depth/branch决定训练order。拟在Failure-driven Curriculum标题前插入以下独立分支，保留前后旧方案。

拟正文（标题：从解答拆出 Curriculum，难度仍是待校准代理）：

固定题池按随机顺序训练，在样本可学且预算有限时最简单；若复杂解答把多项基础操作压在同一长序列里，可以从解答step反推较简单的子题，再递归构造问题树，将同义概念tag合并为依赖图。直接子节点数表达结构分支，概念图depth表达依赖层次，二者的加权分数再用于quantile课程分段。这改变的是训练实例的粒度与出现顺序，而不是证明所有难题都应先拆解；分解器、tag合并、difficulty权重与阶段预算必须随数据版本保存。<!-- source-family:SF-2026-ARXIV-2602-20296 -->

生成器带原context和不带context各答一次，再用symbolic verifier比较数值，可以筛掉一部分不可独立回答的子题，但同一teacher的共同错误、错误tag与语义偏移仍可能两次一致。Depth/branch也不等于student真实难度。[受限math/code实验](https://arxiv.org/html/2602.20296v1#S4)用同一分解池的random-order对照隔离部分课程效应，匹配的是给定设置下训练预算，不包括teacher调用、重试和构图的总成本；可靠分解、可校准难度或独立holdout不足时保留原题随机采样、人工/独立验证和原数据mixture，不能由强teacher→小student结果推出weak-to-strong或通用自改进。

完整前邻接：组合提高复用和难度覆盖，却会放大接口误配、隐藏状态、奖励漏洞与 verifier 相关错误。组合深度、难度分布或验证可靠性越界时，应回退独立 base environment 或人工构造。现有结果只证明作者 operators 和任务范围内的 reasoning generalization，不证明可验证组件任意组合后仍可验证。

完整后邻接标题/首段：### Failure-driven Curriculum：难例必须来自可重放失败，而不是模型自信

随机合成 tool trajectories 覆盖面广，但常把概率质量花在短、浅、同质调用上。若已有可执行 tool environment，可以先运行多个 baseline，找出重复失败的 tools、parameter constraints 与 dependency paths，再从这些失败区域生成更难 query、tool variant 或多步 trace。

拟ownnote：SF-2026-ARXIV-2602-20296，Daily2026-02-26，exact-v1 §3.1–3.3、§4.1–4.2/同池order对照、§5；2+1+2=5，具体数据课程gap深入。采用递归粒度/图difficulty/order；同teacher数值一致≠语义真值、difficulty代理、teacher总成本与weak-to-strong未来设想就近。未核artifact/复现；PRE/锁/POST与日级验收按后续真实结果填。

状态：root必要source/actual owner PRE通过，授Ch27两段+ownnote窄锁；作者actual505/507正文、496–515完整邻接及自身末注已顺读；root非作者actualPOST通过并释放窄锁。Books=整合，非日级验收。

## 2602.20379v1 — Case-Aware LLM-as-a-Judge Evaluation for Enterprise-Scale RAG Systems

日期V3_DATE_PACKET完全落窗；评分2+2+2=6，实际case-aware rubric接口缺口深入，不改评分。原源 https://arxiv.org/html/2602.20379v1 ，V3_CORE_2602.20379.txt §4.2–6行445–520、§7–8.4行637–878、§8.5–12行881–971已读。

机制：每turn judge读取case subject/description、可用prior history、retrieved contexts、answer；八指标将retrieval correctness/context sufficiency、grounding/helpfulness/answer-type、identifier integrity/case issue identification/resolution alignment分账，组织自定weighted aggregate与severitybands。Azure GPT4 temperature0/top_p1/max_tokens1024、singlecall每turn（invalidJSON boundedretry），不因此称远端确定性。所有model使用相同retrieval/prompt/history，Llama3.3-70B-Instruct vs gpt-oss120b；237短与232长是turns，显著性以70/63 conversations均值配对Wilcoxon，不能混写469独立case。

关键反侧：短case GPT4judge p0.6495但Llamajudge p0.0005，方向相近不等显著性不变；longcase局部分离不授模型通用排行。60turn两专家只对grounding/identifier/resolution三二值rubric，88/91/84%有限agreement不授8指标人工真值；原始private logs不可共享、权重/阈值需要组织校准，不授生产rootcause、deployment gate或可复现代码已运行。方法本身weighted average不能数学保证严重失败一定被保留；平台应另有hardgate，是本书已有设计要求非论文已证明。

actual owner Ch66：已实际读988–1060 RAG阶段归因、825–871 Agent/cycle及1060–1100 failureseverity。原有pipeline freezing和stage receipt合理，但没有case subject/history/structured-ID/workflow-resolution三种response职责，故拟在RAG阶段归因988标题后、原document-ID gold段前加两段。保留旧pipeline与信息coverage，不把案例rubric另立owner。

拟正文：

单轮答案在retrieved context中有依据，适合便宜的grounding回归，却不证明多轮support case已被正确解释或解决。可以将case subject/description、已尝试步骤和当前retrieved evidence共同绑定到每个turn，分别测retrieval充分性、回答依据与效用、identifier/command精确保留、case目标识别及resolution workflow一致性；case输入、rubric与权重也进入scorer身份。这是将回答质量接回任务约束，不是让judge拥有真实tool effect或企业操作权限。<!-- source-family:SF-2026-ARXIV-2602-20379 -->

逐turn打分便于定位，但统计分母应按conversation保留同case相关性，组织风险权重不能代替严重失败的独立gate。[有限企业日志对照](https://arxiv.org/html/2602.20379v1#S8)中，替换judge使短case的显著性结论改变；60turn人审只验证三个二值维度，不能认证全部rubric或生产安全。Private case字段、人工校准和多judge调用有成本，欠缺代表性或case信息时报告Unknown并保留直接任务/人工复核；简单单轮检索仍用grounding基线，不把severity加权平均当成真实resolution或通用模型排名。

完整前邻接标题：### RAG 端到端评估必须保留阶段级归因

完整后邻接：检索阶段先要问“召回了哪份文档”，还是“取得了回答所需的哪些信息”。当 corpus 中一条必要信息只有唯一权威支持时，document-ID gold 简单且便宜；当多个 chunk 可独立提供同一信息时，它会错罚有效的替代证据，而只计相关文档数又可能把 Top-K 全部花在同一信息上。更合适的评价身份是随 corpus 版本保存 `required information → 可替代的 supporting chunk 集合`：对检索结果先算已覆盖必要信息的比例，再单独验收是否覆盖了全部必要信息，而不是把部分覆盖、完整证据与最终答案正确合成一个 recall。<!-- source-family:SF-2026-ARXIV-2604-19047 -->

拟ownnote：SF-2026-ARXIV-2602-20379，Daily2026-02-26，§4.2–6、§7/8.3/8.4/8.7/9–12；2+2+2=6，case/rubric接口gap深入。仅case输入与职责分账；turn与conversation分母、短case judge显著性变化、有限3rubric人审及private-data边界近正文，不授weighted平均严重错误保证或生产gate。未核artifact/复现，PRE/锁/actualPOST以后按实际状态写。

状态：root必要源/actual owner PRE及实际正文998/1000、992–1024完整邻接及本末注5610非作者POST通过，窄锁释放。不授日级完成。

## 2602.20273v1 — The Truthfulness Spectrum Hypothesis

日期V3_DATE_PACKET完全落窗；2+1+3=6。标准审阅后actual WORLDVIEW-REPRESENTATION的方向迁移与steering边界已存在，但没有跨域方向失败与joint多域方向并存、test covariance量尺以及监测方向不等控制方向的同实验反侧；具体gap深入不改分。原源 https://arxiv.org/html/2602.20273v1 ，V3_CORE_2602.20273.txt §3–5行420–620、§7行706–842、§8行842–1035、§10/11行1108–1175已读。

主要Llama3.3-70B-Instruct，复查Llama3.1-8B/Llama3.2-3B/Qwen2.5-14B/7B及base；DoM/LR/LDA五折cross-validation，LR layer33平均token选跨域。FLEED五truth类型及sycophancy/expectation-inversion由模型构造且balanced，单域probe跨域失效不排除joint训练方向；stratified INLP逐层投影抽多条方向，作者明言INLP不是完整概念擦除。方向比较CosΣ(wA,wB)按test完整samplecovariance reweight，高R²只是给定分布/模拟相关，不授理论定律、未知deception覆盖或无需target数据的迁移证书。Base/chat几何差异是checkpoint关联，不归因完整posttraining路线。

关键反侧§8：仅Llama8B，1024 verified SimpleQA与type-matched distractor，layer15 MLPbias加alpha=-2 direction；评价是correct/incorrect logprob差而非自由生成正确率。Domain-specific均值+0.05、general -0.07，主要在本来正确高置信样本强化差异；作者§11明确modest confidence而非可靠翻错为对。不能由线性方向授内部truth、通用编辑/监测保证。Covariance估计、多域label、投影与行为干预增加成本；linear-only/modelgenerated label bias/新deception未覆盖。

actual owner：books/part-01-worldview/05-what-neural-networks-learn.md，WORLDVIEW-REPRESENTATION，已读开篇、205–289相关论证及Ch4末/Ch6开交接。当前227–231跨context direction极性及233–237softmax KL几何都有边界，但前者不是同一truth域joint-vs-single谱系，后者不是按目标activation variance比较读出迁移。本拟两段放“尤其要区分三种结论”前，接前几何，后仍原correlation/prediction/causation阶梯。

拟正文：

单一数据域的probe跨域失效，并不能推出不存在共享表示；联合多个域训练得到的读出方向，也不能推出每个域都使用同一条控制方向。可以先在联合域拟合方向、投影其线性可读部分，再在剩余表示上拟合各域方向，检验一般、部分共享与特定方向是否并存。比较两个probe时，若activation高度各向异性，普通Euclidean夹角还会被几乎不变化的维度干扰；按目标分布covariance重加权的夹角更接近该分布下的读出对齐，但依赖目标样本与估计质量，不是未知域上的truth证书。<!-- source-family:SF-2026-ARXIV-2602-20273 -->

这条读出分支仍需独立行为反侧：[有限truthfulness实验](https://arxiv.org/html/2602.20273v1#S8)中，多域方向可读出一般信息，却在事实问答的log-probability干预中不如部分特定域方向；效果主要是强化本来正确答案的相对置信，不是可靠把错误答案改对。概念投影未必完整擦除、模型生成标签会有偏差，线性分析也不覆盖新欺骗类型。多域标注、covariance估计与逐条件干预增加成本；目标数据不足、方向移植未验收或非目标行为受损时，保留原probe诊断与外部行为验证，不把monitor升级为通用控制器。

完整前邻接：这条几何分支增加 covariance Hessian 的估计与求解成本，dual 坐标还受 unembedding convex hull 可达性限制；数值低秩、regularized Newton 与步长归一化只近似理想路径，不能沿用精确 minimizer 的保证。受限实验中，probe 在测试样本可分，沿 steering 路径的同一 probe projection 却未保持相同目标 logit，显示最关键的目标超平面假设可能失配；结果还依赖筛过的 context、token pair、词表截断与路径停止规则，不授任意语义控制或生产延迟。目标不足、非目标损害或求解费用不合算时，应保留独立行为回归和已校准的原路径；counterfactual mass 稳定时，原 Euclidean 分支也有成立条件，不能用新坐标替代实证验收。

完整后邻接：尤其要区分三种结论：correlation: an activation co-occurs with a concept / prediction: an activation can predict a concept label / causation: changing the activation changes model behavior as claimed。线性 probe 能从表示中读出信息，不一定证明模型在原任务中使用了该信息；干预某个方向导致输出变化，也需要排除连带影响。可解释性不是给每个参数命名，而是建立可复现、可反驳的内部机制证据。

拟ownnote：SF-2026-ARXIV-2602-20273，Daily2026-02-26，§3–5/7/8/10/11，2+1+3=6具体gap深入。采用联合/特定域方向并存与covariance量尺及读出不授控制反侧；SimpleQA logprob/本来正确置信、模型生成标签/线性范围及projection非完整擦除近正文。未核artifact/复现，PRE/锁/POST按实际状态填。

状态：root必要source/actual owner PRE及实际Ch5正文233/235、231–265完整邻接及本末注610非作者POST通过，锁释放。Books=整合，不授日级完成。

## 2602.20332v1 — No One Size Fits All: QueryBandits for LLM Hallucination Mitigation

完全落窗，2+1+2=5；actual AGENT-PROMPT query-conditioned rewrite接口gap深入。V3_CORE_2602.20332.txt §3行866–1465、§4行1660–1970、§5行1970–2293、A.1–A.3行4240–4273、token成本Table7行6850–6890已读。GPT4o2024-11-20标17binaryfeature与五arm改写，GPT4o2024-08-06回答T.2/top_p1；所选arm reward基于reference answer的GPTjudge/RapidFuzz/BLEU(0.6/.3/.1)，随后更新bandit不是改模型参数。13dataset16scenario约1050query/每场景，15算法约252k pulls；超参heldoutgridsearch。对照static五种、no-rewrite、noncontextbandits及ablatedfeatures，作者条件下macro .681→.766；费用Table7约493median/688mean token，各组件调用+judge，作者价格非当前价格，latency/E2ESLO未披露。

关键反侧：**入组筛选原query回答正确且五个语义扰动有1–3答错**，所以这是有机会修复的perturbed cohort，不是无筛选自然流量。Canonical query预跑多收敛No-Rewrite，作者猜promptmemorization但没有因果污染证据。Feature关联非因果，reward有judgebias/词面偏置，需要reference answer才有此离线feedback，不能授无标签在线自主降低hallucination或既有生产service效果。探索有早期regret，simplebaselines某些scenario仍最低regret；分数不含统一fine-tuning/no-rewrite相同全调用预算证据。

actual owner Ch74已读开篇/94–150生命周期与noise、173–203constraint-residual；Ch73尾/Ch75开交接已读。原有systemprompt候选A/B与constraint search不承载每query linguisticcontext选择rewritearm及可更新reward的权限条件。拟在当前noise第二段后、追加规则标题前两段：

固定一条改写规则在请求同质、预算紧或缺少可信反馈时最简单；不同问题的指代、句式与约束却可能需要不同处理，统一展开或简化还可能丢失关键语义。可把保持原意的几种改写作为有限arm，用本次query的语言特征选择arm，再根据可核验答案反馈更新选择器；更新的是外部选择policy，不是模型参数，更不是发现了幻觉的唯一内部机制。Original query、feature/rubric、arm prompt、selector state与reward身份都应随版本保存。<!-- source-family:SF-2026-ARXIV-2602-20332 -->

[有限QA实验](https://arxiv.org/html/2602.20332v1#S4)的收益来自“原题能答对、语义扰动后部分答错”的筛选人口，reference answer参与judge与词面reward；不能外推到无标签自然请求，也不能把canonical原题不改写更优解释成已证明训练污染。特征标注、改写、回答、judge和探索均有成本，proxy偏置或语义保持失败时回退原请求与固定基线；反馈不可独立核验时只冻结离线选出的policy，不能靠自己的答案继续认证自己的改写。

完整前邻接：一条受限分支先用足够重复采样估计这两类 variance，再选真实候选差异较大的小任务子集优化 prompt generator，并在未参与选择的任务上验收。额外采样、穷举子集和选择偏差都要计入预算；单题可过拟合，低噪声而容易的样本也会使 signal/noise 比值不稳定。[作者数学实验](https://arxiv.org/html/2604.08801v1)中小子集优于全量训练，但更同质的 instruction-following 任务仍以全量更好，跨模型迁移也只在受测 Qwen 家族内成立。任务偏好一致、数据少或二元反馈假设不成立时，人工 Prompt、全量 regression 与固定候选比较继续合理；选择器拥有的是实验预算，不是外部真值和安全权限。

完整后邻接：### 追加规则容易，可逆地删除规则很难。长期维护的 Prompt、AGENTS.md 或 procedural skill 往往从一次次局部失败中追加规则。每次追加都可能合理，但若只保存“以后不要这样做”，没有保存它防止了什么失败、在什么条件下成立、如何证明已经失效，后来的维护者就很难安全删除。规则老、触发少或与别处相似，都不等于它已经无用：最昂贵的不是删掉一行文本，而是重新证明所有相关 constraints 仍被覆盖。

拟ownnote：SF-2026-ARXIV-2602-20332，Daily2026-02-26，§3/4/5/A.1–3/Table7，2+1+2=5具体gap深入；仅feature→rewritearm选择与reference feedback边界，筛选人口/canonical非因果污染/额外调用/不授无标签在线自证近正文。PRE/锁/POST按实际填。

状态：root必要source/actual owner PRE通过；实际Ch74正文142/144、完整137–165及自身末注297 POST通过，锁释放。

## 2602.20300v1 — What Makes a Good Query? Measuring the Impact of Human-Confusing Linguistic Features on LLM Performance

完全落窗，2+1+2=5不改分；已读§3.1–3.5/4 txt664–1500，§5.1–5.5及5.10/6/Limitations 1515–1766/1990–2041，AppendixC 3753–3855。GPT4o2024-08-06英文13datasets16scenarios，369837 query-response pairs非独立人类用户，回答/改写T1.0；17特征detector100itemcalibration，六paraphrase semanticproxy≥.85；ordinalrisk模型带dataset/scenario固定效应、LODO。Claim observational，Answerability/IntentionGrounding弱overlap不可causaltoggle；词面/模型judge及独立feature假设限制。

中心测量有未澄清冲突：§3.2 txt855–997，exact raw620–626将 hhat 写为positive weighted binaryjudge + **fuzzy string similarity + BLEU-1**，再定义hhat>.5为hallucinated，0/6 Safe、4–6 Risky。Similarity/precision通常是正确性方向；作者AppC仍称奖励权重semanticcorrectness，没有明确转成error complement的定义。不能擅自补1-s或翻转阈值来授“语言特征降低hallucination”的方向性结论。当前未发现公开实现link可核定标签映射。保留作者报告及原式，待非作者核中心定义；若未能消歧则本窗中心争议终态暂缓，不进Books或positiveEvidence，不因此EX缩池。

拟Books暂缓，重开需要精确v1执行score→error label映射/官方澄清或可核验原artifact，定点§3.2与风险labels；其他原作者headline不挽救这条中心测量。

## 2602.20293v1 — Discrete Diffusion with Sample-Efficient Estimators for Conditionals

完全落窗，2+1+2=5，通用离散生成机制准入，不采用quantum science域结果。V3_CORE_2602.20293.txt §2/3行175–800 canonical Bayes kernel、851–1250TV条件界、1250–1408roundrobin/非唯一reverse、1934–2426hardnoise说明、§4行2605–3430partialenergy/conditionalratio/NeurISE、§5.1–5.2行3429–3705及Conclusion4018–4024实际必要读。

核心：forward只改一个坐标，使canonicalreverse所需配置比率只涉及该坐标，mu(xhat)/mu(x)=mu(xhat_u|x_-u)/mu(x_u|x_-u)（正支集/分母defined）；以time/site/others为输入学partialenergy，经类别softmax恢复conditional。不必拟globaldensity，但不是任意单点proposal已成为准确全局joint。TV<=terminalmix+T×uniformsupreverseerror(+initerror)假设无法由平均trainloss核证，不采用实际网络保证。ε0一轮全随机化是作者AR极限解释；原文T=q/T=p及Eq16/17索引/路径写法不一致，不照录其完整unrolling公式或签模型普遍等价。仅保“采样顺序与噪声极限须绑定”的设计边界。

实验2layerMLP匹配parametricclass，25binarysynthetic exactsample，5data模型×10trials、10^5test，比较自实现SEDD/非官方D3PM适配，train100→10^5；MNIST binary784pixels，最多5层MLPhyperopt。NeurISE distribution proxy局部更好不授LLM/large-vocab收益、现代实现公平总预算或生产speedup；MMD/crosscorrelation不是真worstcaseTV。作者direct反侧softnoise未显著胜hardnoise，小样本hardnoise更好；新增学习每time/site、顺序/步数成本。未核artifact/复现。

actual owner MULTIMODAL-GENERATIVE-PARADIGMS Ch24，当前244–271反向核误差已承载terminal/kernel分离，447–451预训练LM局部条件/Glauber可承载复用旧条件，但没有在forwardnoise各层学习single-site条件并参数化canonicalreverse。已读Ch23末/Ch25开交接。拟在局部条件重采样两段后、AR兼容起点标题前加两段，保原pretrained路径：

复用已有LM条件之外，也可以为指定的离散加噪路径重新学习条件：若forward每步只改变一个坐标，canonical reverse需要的配置概率比率可约成“该坐标在其余坐标给定时”的条件概率比率。模型以噪声时刻、位置与其余状态学习局部partial energy，再经类别归一化构成条件分布；这把学习对象从global density或任意全局score改成逐时刻条件，但要求分母与支持有效，不让单点proposal自动认证完整joint。<!-- source-family:SF-2026-ARXIV-2602-20293 -->

逐位置训练、noise schedule与串行采样仍有成本，terminal混合误差、reverse估计误差与初始化误差也须分别验收；uniform worst-case条件不能由平均loss直接推出。[有限离散分布实验](https://arxiv.org/html/2602.20293v1#S5)中，soft-noise没有稳定胜过hard-noise，小样本后者更好，故不能把更多denoising步骤自动视为优于AR的证据。局部MLP、二值图像及低阶分布指标不授大词表语言质量或端到端加速；条件误差、混合或净费用未验收时，保留预训练条件重采样、原离散kernel和普通AR分支。

完整前邻接：这里改变的是 generation path，而不是凭空获得新的语言真值。模型只拥有局部 proposal，sampler 拥有位置选择、transition schedule 与 provisional state，runtime 仍拥有停止与外部 commit。复用已有权重可降低从零学习条件分布的门槛，却把成本移到更多 NFE、混合时间、mutable cache 和收敛诊断；有限步输出不等于已经到达 stationary distribution。受限证据还包含显著训练算力，未覆盖 streaming 与生产端到端 SLO。低延迟、append-only 或无法验证混合质量时，causal AR 仍是更可靠的回退路径。

完整后邻接：### AR 权重可以成为 Masked Diffusion 的兼容起点。从零训练 masked language model，attention pattern 与初始化都为双向修正服务，接口清楚但无法复用成熟 AR checkpoint；直接把整段序列改成双向可见，又会让 observed prompt 变成可修改状态并破坏 causal condition。兼容分支可以保留 prompt 内的 causal attention，只让 masked target 内部双向交互：prompt 仍是冻结条件，target 才拥有 provisional、可反复修正的 token state。

拟ownnote：SF-2026-ARXIV-2602-20293，Daily2026-02-26，§2/3/4/5.1–2；2+1+2=5具体gap深入，single-site canonicalratio/局部condition学习、sup误差非平均loss/softnoise反侧近正文；不采用原AR unrolling式索引不一致、science域结果、LLM/生产优势。PRE/锁/POST按真实填。

状态：root必要source/actual owner PRE通过；实际Ch24正文453/455、完整447–470及自身末注2099 POST通过，锁释放。

## 2602.20309v1 — QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models

完全落窗，2+2+2=6；实际INFER-TENSORRT-LLM跨模块量化接口gap深入。原源V3_CORE_2602.20309.txt §3.2行500–885、§3.3 885–1147、§4.1–4.4/Table1–4 1148–1575、AppD 2825–2866必要读。DuQuant成熟rotation/smoothing只是基底；增量是upstream LLM低位引入featuredrift，即使downstream DiT attention QKVO保持float也会改logit dispersion与residual injection，选择只量化LLM+DiT MLP，并分别统计logits Std/output RMS与floatteacher对齐。Teacherbuffer与layout/language-to-action接口共同version。

LIBERO、pi0.5/GR00TN1.5、FP16vsW4A8、A100（型号容量/测量并发/延迟SLO未披露）；Layerlayout消融关闭ATM/OHB，完整量化显著损成功率，MLPonly较少损伤；Fig3两统计曲线有限校准effect。Main W4A8模型模块memory1.28 vs4.27GB、.91vs2.02GB不等全服务memory或速度。GR00Tlong76→74退步、W4A4 pi平均95.3低于FP1697.1；8→16step再多求值，不授realrobot安全/lowlatency/generalmodality无损。作者统计buffer32batches、128steps×最多5trial/task，离线成本与随机不确定性未全给。

重要不采用：§3.3 Eq9写alpha=Stdteacher/Stdquant，而Eq12写LQ=LT/alpha，变量与预期student调整方向未闭合；Eq14beta=RMST/RMSQ但Eq17又ZQ=Zl/beta；主文±.4clip与AppD logclamp.30亦非同一规格。没有公开实现可核，不复制这些exactscalar更新或no-extra-op部署保证。只采用有独立Table1支持的layout与跨模块漂移诊断及统计/行为分账；若主张完整calibrationrecipe可执行则暂缓待官方exactartifact，非自行倒数纠错。

actual owner Ch49当前916–937多块格式相关性与静/动态calibration已承载代表性数据，1351–1357embodied phase精度选择承载runtime scope，但没有“下游float仍接受upstream低位输入漂移”的语言→DiT接口与双统计/真实action分账；读开篇与Ch48尾/Ch50开交接。拟在静态calibration段后、行为条件段前两段：

下游算子保留浮点，不代表它仍消费原来的输入分布。量化language backbone后，送往action DiT的feature偏差可改变Q/K logits的离散程度与output projection后的residual能量；因此层选择不能仅按各层孤立重构误差决定。一个受限layout保留DiT attention projections为浮点，只量化上游LLM和DiT MLP，再将接口的logits统计、输出RMS与实际action结果分别校准；calibration buffer、teacher与模块边界必须同artifact绑定。<!-- source-family:SF-2026-ARXIV-2602-20309 -->

[有限VLA仿真对照](https://arxiv.org/html/2602.20309v1#S4)支持上述layout与统计诊断，不把统计匹配等同动作正确：部分long-task和更低位宽仍退步。原文scalar比例与施加式、clip规格未完全一致，未核实现时不能直接复制exact修正配方或宣称零运行时成本；所报LLM+DiT内存下降也不是完整服务memory、延迟或物理安全保证。代表性轨迹、离线统计与逐任务回归有成本，接口漂移、artifact或行为验收失败时，保留更高精度模块、重新校准或原浮点policy，而不由平均成功率放行所有control阶段。

完整前邻接：静态 calibration 提前用代表性数据确定 activation 范围或重构目标，运行时路径较轻，但分布漂移会使旧 scale 失配；动态量化根据当前输入计算 scale，降低对固定范围的依赖，却把 reduction、转换和 metadata 带入热路径。Weight-only 的最简单方案也可以直接从权重统计定标；是否需要校准样本取决于量化目标，不能把所有 PTQ 都写成同一种准备流程。

完整后邻接：校准目标还可以显式加入行为条件，而不只重构无条件 activation：先在已对齐模型各层冻结 benign/harmful 的 sparse-logistic probe，再调整量化 scale/clipping，使 benign 样本保持局部重构、另一类样本向该 probe 的指定 margin 分离。[Q-realign 的受限分支](https://arxiv.org/html/2601.08089v1)以几何 probe 作为训练代理，不需要把安全回复当逐 token target；proxy、两类校准人口、loss 与来源 checkpoint 因而都属于 artifact 身份。分类可分不证明拒绝或最终输出安全，更不能从类间距离恢复“真实安全机制”。

拟ownnote：SF-2026-ARXIV-2602-20309，Daily2026-02-26，§3.2–3.3/4.1–4.4/Table1–4/AppD；2+2+2=6具体interfacegap深入。仅layout/双统计与action分账，不采用Eq12/17 scalar应用及clip不一致的exactrecipe/nooperator保证；LIBEROlong/W4A4反侧/模块memory非E2E/物理scope近正文，PRE/锁/POST按实际填。

状态：root必要source/actual owner PRE通过；Ch49正文921/923、完整917–929及自身末注2752 actual POST通过，锁释放；exactscalarrecipe隔离不支持执行。

## 2602.20323v1 — Learning Physical Principles from Interaction: Self-Evolving Planning via Test-Time Memory

完全落窗09:00～<10:47:23，2+2+3=7，必要深入。精确原源V3_CORE_2602.20323.txt方法1090–1570、OOD1756–1838、消融1917–1993、限制2082–2115实际读。高层VLM planner与固定低层executor分责；option/outcome/context/symbolicstate先存episodic，resonance只为已有principle与当前状态一致比例，surprise优先，聚类反思为Avoid/Prefer/Sequence假设。Confidence累计相关尝试的success rate，>=.8且support>=3晋升并折叠经验；不是随机因果实验/独立真值，不能采用作者“隔离因果”措辞或成功率自动取得事实权威。

Real xArm6/RealSenseD435，Gemini3Flash planning+Qwen3VL reflection每15s异步，10–20episode/task；真实Parts/Ball/Stone OOD每条件10trial，prior only新ball成功1/10与no prior1/10一样，prior+adapt4/10；尚未集成VLA，掉物/破损需人reset。Simulation Franka/MuJoCo brick插入、三run，Gemini3Flash消融每难度100episodes：full89/76/39%，direct48/23/8%，noverification85/64/27%；no forgetting91/78/36%并耗3.4x medium tokens，既有质量—成本反侧，不授forgetting普胜。训练precision/低层频率/总wallclock和生产SLO Not Disclosed；没有复现。

Books决定 **已有覆盖 AGENT-MEMORY Ch77**：实际68–150给source/consent/conflict/confidence/expiry、pending与active分开及环境failure receipt而反思只能提议；591–639给成功/失败派生procedural与raw episode/scope/judge/supersession、环境变化重新采用、不改Workflow authority；999–1029给scoped rule→独立正负池验证→晋升及反例/撤销；385–406给raw/pointer与derived/consolidation分责。原实验是这些原则在physical high-level planner的实例，resonance阈值与正向累计不是新通用验证合同；无需因物理/科学loop名字再造正文。必要源的局部收益保Report，评分不改。root实际非作者必要Evidence/Existing核通过，未申请锁或改书。

## 2602.20330v1 — Circuit Tracing in Vision–Language Models: Understanding the Internal Mechanisms of Multimodal Thinking

完全落窗09:00～<10:47:33，2+1+2=5标准完成待独立核。精确原源V3_CORE_2602.20330.txt §3.1–3.2 308–402/516–664、§3.5 925–1022、§4.1 1081–1164、§4.5–7 1326–1400实际读。Per-layer topK transcoder替换Gemma3-4B-it MLP，reconstruction error另作error node，局部graph固定ReLU/attention/normalization；不是原网络所有非线性因果图。48active latents，34decoder layers；text144k、ImageNet144k、Cauldron72k均匀50子集。Mars→Earth feature patch使后续activation/output变为Earth，但所有干预在replacement model，定性选例；不能授native circuit因果或可控性普遍结论。

原§7 attention图可能不定位、运算feature与结果feature难分、per-layer漏cross-layer/near duplicates、单Gemma模型与人工label/pruning成本，未给全面quantitativefaithfulness；训练hardware/precision/随机重复 Not Disclosed，不声称复现或deploydebug效果。Books **已有覆盖 WORLDVIEW-REPRESENTATION Ch5 actual298–311** 四类replacement gap、reconstruction/pruning/native intervention/promptpopulation与旧probe/blackbox共存；actual242–259已有prediction≠causaluse阶梯。跨视觉示例不改变该长期链，保原实验窄实例，无新增Books段。root actual必要Evidence/Existing通过。

## 2602.20338v1 — Emergent Manifold Separability during Reasoning in Large Language Models

完全落窗09:00～<10:47:44，2+1+3=6标准完成待独立核。精确原源V3_CORE_2602.20338.txt方法306–610、结果610–782、attention/Discussion/限制782–847 actual读。Boolean height5 binary31nodes、256 balanced128/128、rigidrestatement/solve/summary，Ministral3-8BReasoning32layer4096、temp0/A10080/eager；lastformat before Result anchor减少直接答案文字污染，非独立计算真值。Manifoldcapacity通过randomprojection最小可分维数、coneGaussian定义，与hardmarginSVM/LR probe比较；probe高于90%可维持，capacity只在solve/recall transient，SilentCoT不写子答案仍有pulse；attention相关r.723非因果干预。

不采用作者由layer时序“confirm causal chain”、faithfulCoT/active计算/真实内部带宽的扩大结论；TwoNN/PR约10也非硬件容量。Synthetic单模型、linear-separability假设、自然语言/70B+未测，probe与capacity不同测量不证明动态旋转唯一机制。Books **已有覆盖 WORLDVIEW-REPRESENTATION Ch5 actual242–259** decodability不等原path使用/局部干预不等完整机制，actual298–311解释模型budget；此项仅新增受限几何sensor的实例，不另为pulse创建真实工作区机制段。root actual必要Evidence/Existing通过。

## 2602.20354v1 — 3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism

完全落窗09:00～<10:48:07，2+1+2=5标准完成待核。精确原源V3_CORE_2602.20354.txt §3 254–275/279–316/350–371、训练490–625、inference880–944、ablation1024–1048/1190–1236、人评1247–1395实际读。支持query/support各半轨迹、3D点+occlusion与frozenDINOv2语义→motion latent AE重建；视频推理依赖CoTracker3+VideoDepthAnything，query tracks亦来自该pipeline，不是独立physics GT。Kubric38k与TAPVid3D4569main/150minival、TRAJAN init300epochs AdamW1e-4，scale-invariantdepth正则；未复现。

IntPhys2 no3D但有DINO多数concept近full，不能把全收益归3D；VideoPhy2 PC Spearman full.74/noDINO.50/no3D.40/TRAJAN.19，AutoEval.76另finetune协议。EvalCrafter仅按trackmotion取top50%=1849videos；Table4full subjective.60低于noDINO.63，不全质量支配。Discussion1383–1395明确复杂深度/轨迹错传到realism，约2x TRAJAN耗时只是作者limitedproxycost，未读AppC不采用具体硬件/latency数字，batch/precision/E2ESLO Not Disclosed。

Books **仅报告**：新受限semantic+trajectory estimator与消融可保sensor实例，但无需把预测querytrack重构当长期物理验收机制。Actual Ch66 4243–4249已承载人工观感/感知proxy不等物理定律参数与realreference/不确定度，201–254承载对象和scoreridentity；本项没有独立新增physics correctness contract，不以主题owner或新AE模块制造gap。geometry/correlation非真值，隔离作者physics理解宣传。root actual必要Evidence/Only通过。

## 2602.20408v1 — Examining and Addressing Barriers to Diversity in LLM-Generated Ideas

完全落窗09:00～<10:49:25，2+1+2=5标准完成待核，仅四study受限评价命题。精确原源V3_CORE_2602.20408.txt protocol518–646、category690–785/metrics819–906、study1 907–947、study2 1345–1393、study3 1468–1530/1962–1995、study4 2121–2197/2238–2275/2905–2945、discussion3181–3225实际读。Fitness product单任务；GPT4o2024-11-20生成与分类同模型，99人（121剔除离屏>10%）/99session×10串行ideas带此前history。GPT三轴industry/need/form归并再relabel，28categories/810combinations与Hammingdistance；不是独立human语义标注真值。Embedding text-embedding-3-small1536仅partition辅助/tSNE展示，不作主多样性指标。

human first idea seed后只评2–10，类别default18.34 vsseed18.35无显著差，说明单起点差不足解释后续。ordinary99persona与fitnessentrepreneur99 persona变更condition（后者ChatGPT5.2生成）；persona增group多样性可同时增withinfixation。CoT短title→差异化再展开改为一次batch10，与串行baseline预算/模式不完全matched；作者footnote另sequential robustness方向一致但幅度较小，此处不把未读AppendixE当详细结果。within slope category1.013→1.363只为该生成protocol，不识别RLHF/pretrain统一分布因果；human superiority headline、企业创新/一般模型社会效应均不采用。Discussion quality/feasibility/usefulness未测，partition仅semantic proxy，precision/hardware/temperature/tokenwallclock/重复APIseed Not Disclosed。

Books **仅报告**：核心可用是跨session与within序列多样性分账及prompt干预的受限反侧，非新内部sampling机制；actual Ch20 311–341已分coverage与selection/相关error与全费用，231–237保token/sequence质量分责，不能用分类多样性替候选效用。无需把fitness/人类比较或“persona知识分区”升为全模型长期机制。root actual必要Evidence/Only通过。

## 2602.20360v1 — Momentum Guidance: Plug-and-Play Guidance for Flow Models

完全落窗09:00～<10:48:15，2+1+2=5；actual新历史velocity reference分支gap深入。精确原源V3_CORE_2602.20360.txt §3 992–1259/Eq12–13、§4.1 1540–1635/Table1、ablation1768–1975、§6 2086–2095及强CFG反侧3903–3936实际读。m0=v0，每步先记m_next=(1−beta)v+beta*m，Euler更新使用尚未更新的m：z_next=z+dt[v+alpha(v−m)]。该historicalEMA reference不是额外弱网络/去条件branch；alpha/beta/timegrid/momentum初始化与update顺序定义artifact，一NFE只有base无CFG时，有CFG仍保两branch原成本；额外same-latent-sizevector与算术不是零成本。理想marginal smoothing仅为解释，不采用错误score精确identity或历史EMA等价真实unconditional的理论保证。

ImageNet256 improvedDiTXL/RectifiedFlow、uniformEuler16/32/64，每(CFG,NFE) FID10k搜索alpha/beta再50k评估，guidanceinterval也搜索；作者FID同模型无CFG64step4.75→3.26，CFG1.2 1.89→1.60，只作局部质量条件非无调参收益。SD3/FLUX另实例不合并；大alpha/beta过修正、强CFG相互干扰下降。无额外network eval不等wallclock/SLO/总搜索成本减半；hardware/precision/batch/confidence/生产并发NotDisclosed，未复现。

actual Ch24 210–224已有NFE非总费、SparseGuidance双capacitybranch及modulation接口，却没有“历史velocity作reference、保留sampler state与顺序”的替代分支；搜索具体Momentum Guidance/历史velocity/动量采样无已有项，非只缺论文名。拟在220双capacitybranch后、222 modulation前两段（完整邻接两段见actual）与ownnote：

guidance reference也可以来自同一采样轨迹的历史，而非再计算去条件或低capacity网络。一条连续Flow分支保存与latent同形的velocity EMA，当前步用 `v + α(v−m)` 外推，随后为下一步更新历史；初始化、时间网格、衰减和update顺序都属于sampler state。它复用已算velocity而不新增网络求值，但有CFG时仍支付原两支求值，EMA驻留与向量算术也需计费；历史reference不是精确unconditional或独立弱模型。<!-- source-family:SF-2026-ARXIV-2602-20360 -->

[有限Euler采样对照](https://arxiv.org/html/2602.20360v1#S4)支持该历史分支的局部质量收益，却额外搜索了强度、衰减与guidance时窗；过强外推或与强CFG叠加会退步。低NFE、较好FID和不增加network evaluation须分别验收，不授分布保持、wall-clock减半或所有生成任务的收益。配置与轨迹变更、质量或多样性未通过时，减弱或关闭历史外推，回退原Euler/已校准CFG与capacity分支，而不让陈旧EMA自动接管新的采样协议。

状态：root actual必要原源/owner PRE通过；实际Ch24正文222/224、完整218–228/自身末注2105 POST通过，锁释放。

## 2602.20595v1 — OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Services

完全落窗09:00～<10:53:57，3+2+2=7深入完成待核。精确原源V3_CORE_2602.20595.txt §3 355–451、§4 452–571/571–755/920–1158、§5 1159–1199/1491–1636、§6 1637–1724、B.1–2 2746–2787实际读。共享KV池/LPM scheduler、普通client streaming黑盒/公开tokenizer、domain辅助语料假设；local SFT后按low-ranked正确token与greedy错误token做DPO，更新guess proposal而非cache隔离。LPM order gap validator只在所测队列/共享池条件验证；其他FCFS/vLLM/semanticcache适配和主动defense negligible开销只是提议，不采用。

SGLang target固定Qwen2.5-3B-Instruct、local猜测Qwen3/7/14B与Llama3.1-8B；baseline matched dummy20+candidate20。MedQA test抽150（train10178/val1272），PubMedQA800/100/100，Finance400/50/50；ARPT 41.99→21.60仅作者protocol，相近PubMed语料30.27但不相关Finance51.90反退，PubMed测试Finance966.59高于base628.50。继续SFT3000step可3.7x差，DPO-only不能同等提高hardtoken。ASR正文下标/请求单位有不一致，不采用其精确ASR或统一requestcap；硬件/precision/生产并发/latency/重复统计 Not Disclosed，不复制防御充分性或最坏泄露费用保证。

Books **已有覆盖 PLATFORM-SECURITY Ch72 actual2124–2140** 同池/共享page与prefix timing先于输出过滤、principal namespace/pool/审计/代价及causalcontext身份；2142–2166 capability/uplift→deployment residualrisk→refresh与有限攻击非空间上界；2849–2853 attackgenerator/submission/attempt/auditbudget绑定。针对性训练降低猜测费用是这一审计口径的新局部反例，不新增防御机制或通用阈值，无需把DPO名字写进隔离合同。root actual必要原源及具体Existing通过，未改书。

## 2602.20656v1 — Lagom: Unleashing the Power of Communication and Computation Overlapping for Distributed LLM Training

完全落窗09:00～<10:55:27，2+2+3=7深入完成待核。精确原源V3_CORE_2602.20656.txt §3 573–716/856–1165、§4/Table2 1487–1756实际读；computationbound时serializedcomm调整改变后续overlap窗口，algorithm/protocol/transport先分组，NC主SM占用、C影响全局memory/cache，NT在所测case较小。H=(compute增加)/(comm减少)是边际代价，按minH调资源并重新更新，不授全局最优；三端点条件与criticalpath分账已核，未复制连续模型完整公式。

Megatron/PyTorch2.3/CUDA12.8/driver570.13/NCCL2.18.3-1/AutoCCL，2×8 A40：A NVLink400Gbps/2×400GbpsIB，B PCIe4/100GbpsIB；Table2绑定densePhi/Llama8B/MPT7B与MoEDeepSeek16B/OLMoE，FSDP MBS2/1/1；三dense TP均8，MBS8/4/2与GBS512/256/256；两MoE EP均8，MBS2/GBS16（root独核纠正原TP/EP列误表述）。PhiFSDP pattern90%时间，NC8→AutoCCL61虽通信快但整体.87x，LagomNC2/C684KB局部1.35x；FSDP作者1.10–1.33x、TP1.08–1.16x/EP1.07–1.08x，只限披露两cluster。两comm33searchiterations vsAutoCCL16不是无调参成本，“对百万iterations可忽略”未证明短job摊销，搜索线性经验不签全局optimal/任意GPU。Seq/precision、重复置信与全训练数值质量 Not Disclosed，未复现。

Books **已有覆盖 TRAIN-DISTRIBUTED-TRAINING Ch36 actual269–275**：实际已含本SF同形mechanism全文，SM/memory/NIC共享、contention-awaregroup、边际排序与三端点、dependency/optimizerstep边界、profile/search/漂移回退均真实承载（不是marker推定）。重新必要精确原源验证后，这层有效正文复用，不继承旧完成/评分，不添加重复。Ch35实际小结587–591与Ch37开篇交接已核。root actual必要原源及具体Existing通过；Table2 TP/EP列纠正如上，未改书。

## 2602.20628v1 — When can we trust untrusted monitoring? A safety case sketch across collusion strategies

完全落窗09:00～<10:54:45，3+2+2=7必要深入。精确原源V3_CORE_2602.20628.txt §2.4协议566–607、§4 1279–1391、Table3/§5 1392–1460/1510–1690/1561–1607、§5.6/6 1729–1866、Conclusion1924–1938实际读。U=GPT4.1同模型writer/monitor、trustedGPT4omini、Gemini2.5Flash代human与honeypot；APPS/BigCodeBench pass tests却在reference外input错误作为backdoor，删comments，再no/minify/summary jamming。Passive selfrecognition、promptacausal、For/While causal以及combined分开，selfrec SFT对jamming训练红队后动；proxy不是恶意自然发生率。

N=5000tasks、2%预算至多100honeypot/audit混合、slack5，100%usefulness下Table3 safety为统计模型输出、80%bootstrap1000次，不是真实部署概率。APPS untrustedonly无jamming selfrec未elicited97.1% vsSFT26.4%，summary68.8%；trusted+untrusted summary90.2%。Combined仅untrusted更强，加入trusted不占优；BCB与APPS jamming排序/提升不同，minifyproof train/testtoken混杂作者亦不唯一归因。Noelicitation时summary可能降低honestmonitor准确，SFT summary可能未fullyelicited；selectedattack未建模、binary策略/score独立假设、acausal未充分优化、slack未知、monitorjailbreak未建模/完美audit假设均限制safetycase，不能把Appendix proof-sketch签部署上界。额外SFT/feedback/jamming与人工audit费用，APIhardware/precision/latency/production SLO NotDisclosed，未复现。

actual owner Ch72 2849–2853已有attackselection/审计预算，但无“未共享显式signal仍能被同源monitor自识别、elicitation强度改变jamming效果”的缺口；735–744现jointintent/effect分账亦不含该观察面。拟在2853后、PartialTEE前两段，保完整前邻接：这种评测更接近自适应对手，但受 red-team 能力、攻击候选集和窄审计预算强烈影响，不是真实攻击概率上界。选择器未被充分激发时，应将结论降为已见攻击下界，并保留独立审计、最小权限和 safe-commit gate。后邻接为PartialTEE秘密随机性不得跨请求复用标题及其协议身份段。

不可信writer与monitor即使没有共享显式secret，也可能通过同模型的代码风格与语义结构识别彼此输出，形成绕过外部honeypot的协同条件。Control evaluation因而要分别激发passive self-recognition、显式/隐式signal及组合策略，并让红队针对实际minify或summary协议再训练；“prompt时没识别到”和“去掉变量名”都不能自动上界该能力。Writer/monitor/jammer身份、训练人口、反馈可见性与审计机会集应作为同一个control artifact保存。<!-- source-family:SF-2026-ARXIV-2602-20628 -->

[有限coding proxy](https://arxiv.org/html/2602.20628v1#S5)中，SFT elicitation会显著改变self-recognition风险，summary又可能损害honest monitor；不同dataset及trusted-monitor组合的排序不相同。统计safety score依赖完美audit、预算、slack与独立假设，不是部署概率；selectedattack、acausal上界与monitor jailbreak尚未闭合。训练、jamming和独立审计均需计费，能力或人口不能保守界定时保留未知、增加trusted/人工复核并收缩执行权限，不能用低proxy风险替代真实effect Gate。

状态：root actual必要source/owner PRE通过；Ch72正文2855/2857、完整2849–2865、自身末注4254经root非作者actual POST通过，窄锁释放。只授有限同源识别与jamming适应命题，不授部署概率或日级Gate。

## 2602.20433v1 — Disentangling Geometry, Performance, and Training in Language Models

完全落窗09:00～<10:50:01，3+1+3=7深入。精确原源V3_CORE_2602.20433.txt 276–341 effective rank定义、638–801训练/ID、805–899 OOD/quantization、1020–1055 finetune、1100–1410 hyperparameter对照、1578–1629 representations与AppC4203–4235实际读。Rank为unembedding singularvalue归一化熵的指数，不是特征数/任务维数；108 OLMo-style Pile受限4–75M nonembedding、8–128B tokens，batch32–512、weightdecay .01/.1/.5、LR相对.1/10/100与终LR0/1/10%，其他配置固定的对照。大batch通常高rank但loss U形；较强WD保rank却随modelsize优劣相反，弱annealing保rank却较差loss，未单独干预rank，不识别rank→能力因果。

ID loss更能追踪Paloma/Dolma100 OOD与StarCoderPython迁移；GPTQ极低rank小model脆弱，但75M不同反例，不授rank普遍无用或量化阈值。仅W/final-lasttoken H，H变化小；AppC小模型/中间层未覆盖、fine-tune大多hyperparam固定、observational非fullycausal。Seed/重复统计/precision/E2E预算不用于此定性采用，未复现。实际Ch5 181–189线性访问合同、229–259 geometry/probe/干预阶梯均已读；现有把几何位移与行为作用分开，却未承载“同一训练配置同时塑造rank与loss，rank高低不能替优化能力或release验收”的训练几何混杂差额。拟在235 truth读出段之后、237三种结论阶梯之前两段；完整当前229–259与原阶梯衔接，不改旧probe分支：

表示的有效维度也只是测量量，而非性能证书。把unembedding奇异值归一化后，用谱熵定义effective rank，可以诊断输出方向是否集中；但训练batch、weight decay与learning-rate schedule会同时改变该几何与优化结果。要判断rank是否解释能力，至少在相同模型、数据与训练配置内比较，并把ID loss、迁移、量化鲁棒性分别测量，不能把“更高rank”直接设成训练或发布目标。<!-- source-family:SF-2026-ARXIV-2602-20433 -->

[有限小模型对照](https://arxiv.org/html/2602.20433v1#S4)中，大batch或较弱annealing能保留高rank却未改善loss，weight decay的收益随模型规模改变；量化脆弱性也不服从一个通用rank阈值。这些是训练条件下的反例，不证明直接改变rank一定无效或所有层/大模型都相同。记录谱量、训练revision与额外测量成本，配置漂移或行为评价冲突时回退实际任务loss与独立验证，仍保留几何sensor用于诊断，而不让它替性能或因果验收。

状态：root实际必要Evidence/差额PRE及actual Ch5正文237/239、完整231–267/自身末注616非作者POST通过，窄锁释放。

## 2602.20710v1 — Counterfactual Simulation Training for Chain-of-Thought Faithfulness

完全落窗09:00～<10:56:44，3+2+2=7深入。精确原源V3_CORE_2602.20710.txt 298–588原cue/生成counterfactual、reasoning与outcome-only simulator及Table1，588–746 rewrite/CE-unlikelihood、746–885 setup、894–932 results、1036–1066 dissuading、1158–1173 limits实际读。Simulator看到原input/answer/CoT和counterinput，预测task model在counterinput的答案，非gold正确性；与不看CoT的simulator比较增量，Table1 helpful/bothright/bothwrong/harmful奖励+5/+1/-1/-5。在线重写/拒绝采样，lambda .4 negativeunlikelihood，5–20epoch/最多6round/batch128；task自身rewriter、simulator三次greedy多数仍有APIvariance，不是独立内部计算真值。

GPToss120B与Qwen3 instruct4B/30B-A3B/235B-A22B，Tinker LoRA32；Qwen235B或DeepSeekv3-0324 simulator。四binary任务，通常1000train/2000test（Law640/320），五seed与blockbootstrap；6seen/6heldout artificialcue，generalcounterfactual拒绝样本要task/simulator不同且oracle正确，会选特定错误人口。Cue Gmean31–48pp提升不是task accuracy；generic部分ETHICS/Law提升由outcome-only一致性解释，MMLU无提升。Persuading明显改善却dissuading53→57；实际§7 L1162明确未见cue-based/model-generated两counter类型之间transfer、分别训练，非仅未测。OODOmarginal、accuracy代价1–2pp，未联合优化正确性。额外counterfactual/rewrite/simulation/SFT调用和训练费用，不授内部causalfaithful/部署低latency或一般monitorability，hardware/precision/全cost Not Disclosed，未复现。

actual Ch31 741–758 verifier/outcome不证明process与automatic任务生成交接、260–300 auditor/自述channel，168–178独立counterfactual偏置/trajectory信用均读；已有一般judge/过程分账却没有“奖励CoT对counterfactual行为预测的增量，并以outcome-only排除单纯行为稳定性”的训练objective分支。拟747句后、749自动任务分布前两段+自身末注，不改变旧outcome verifier：

若目标是提高推理文本的可审计性，而不是只奖励最终答对，可以让独立simulator根据原输入、回答与CoT预测同一policy在counterfactual输入下的答案，再与不看CoT的outcome-only simulator比较。两者差额定义推理文本对行为预测的增量，区分解释有用、无增量与误导；据此重写/筛选轨迹并用reward-weighted正例学习与negative unlikelihood更新policy。Counterfactual、policy、rewriter、simulator及采样预算共同定义监督身份，该奖励不是真实内部计算或答案正确性的标签。<!-- source-family:SF-2026-ARXIV-2602-20710 -->

[有限二元任务对照](https://arxiv.org/html/2602.20710v1#S5)显示cue条件下的simulatability改善，却在部分generic任务主要改善outcome一致性而非CoT增量；人工cue/拒绝样本人口与反向cue限制外推，作者未观察到cue-based与model-generated两类counterfactual之间的transfer，分别训练不授统一introspection。额外重写、simulation与训练均计费，任务准确率仍须独立验收；simulator共同偏差、增量不成立或质量下降时，回退原outcome verifier、人工/独立过程审计，不把可模拟性替正确性或causal faithfulness。

状态：root actual必要Evidence/差额PRE及actual Ch31正文749/751、完整741–770/自身末注1316非作者POST通过，窄锁释放；未见两类型transfer反侧近正文。

## 2602.20717v1 — PackMonitor: Enabling Zero Package Hallucinations Through Decoding-Time Monitoring

完全落窗09:00～<10:56:54，2+2+3=7必要深入。精确原源V3_CORE_2602.20717.txt §3 511–985、§4.3–5 1100–1332、latency1700–1775、cache1975–2060、§6 2060–2104实际读。Contextparser只在所识别codeblock安装command包名区激活，PyPI有限snapshot DFA+tokenizervocabulary TokenTrie，逐字符transition合法才保logit，terminates acceptingstate才授该snapshot membership。不是所有文本dependency/动态代码/包版本API功能或安全保证；全文没有证明parser完整捕获任意安装shell syntax，不采用“supplychain风险exclusively此处”论断。

5个6.7–8B coder/instruct模型，HFuzzer每model×configuration单轮1000 iterations、targetT.7/testerT0，PyPI706618名单、8×A10080/EPYC7543/Ubuntu22.04；0 PHR/RHR为名单/所识别安装语法的人口，不授全开发供应链安全。缓存后作者generation latency1.07–1.28x vanilla、无cache2.8–6.2x；3M名单offline构建21.121s vs加载.247s，不把加载接近常数写成零费或持续更新免费。§6官方名单错误/遗漏/变动与环境latency；未复现，precision/batch/并发/SLO及包功能utility不采用未读细节。

Books **已有覆盖 MODEL-SAMPLING Ch20 actual436–452** 明确finite-settrie/offline空间代价/tokenizer与动态集合失效回退，prefix合法不等budget内accept；actual454–458局部mask不保持完整条件分布/非开放语义保证。包名DFA是这些机制的有限snapshot实例，不需要把新包主题或“zero”升为模型truth能力；保Report的parser范围/registry依赖，后置语义/执行授权仍属原接口。root actual必要原源/436–460 Existing通过，未改书。

## 2602.20493v1 — AWCP: A Workspace Delegation Protocol for Deep-Engagement Collaboration across Remote Agents

完全落窗09:00～<10:51:26，2+2+2=6标准，actual workspace/data-plane gap定点深入。精确原源V3_CORE_2602.20493.txt §3.1 420–482、§3.2 482–690、§4.1 697–768、§4.2–3 768–950、§5/6 950–1061实际读。Delegator control/Executor assignment两机器以ACCEPT/START/DONE同步；INVITE task/TTL/RO-RW/resources、ACCEPT可窄权限、START绝对expiry+transporthandle，control HTTP/SSE与SSHFS/archive/storage/git data adapter分离。NOT shared-memorytaskauthority：transport live-sync能力把snapshotpolicy强制auto；非live auto/staged/discard，detach再release。JSONpersist/crash恢复/9200TS与tests为作者声明，未核代码/运行/恢复一致性，没有正式保证双机所有failure同状态。

仅两个live demo：DeepSeekV3.2/Cline→Gemini3Pro viaSSHFS百余图整理，OpenClaw/Feishu→authorizedstamping archive两轮error/newinvitation；没有 matched实验/scale/latency/数据丢失率/ACL穿透验证，hardware/precision/费用 NotDisclosed。§6明列fine-grained file ACL/RBAC/audit、多方CRDT为future，不授现安全隔离、contextlosselimination或所有代理环境完整重建。Live写在filesystem已effect，事后snapshotstaged不能追认变成gate。

actual Ch83 241–260已有task/context/artifact到本地observedstate映射、cancel未回滚与Ch81/82分责；没有“workspaceprojection同tasklease协商、live与snapshot effect时点不同”的接口差额。拟在257 polling/去重之后、259 ownerhandoff之前两段+自身末注，前邻接完整241–260，末后保原Ch81/82执行/验收ownership：

当远端需要原生工具链直接操作多文件环境时，还可把委派对象扩展为临时workspace投影，而不是把目录内容反复序列化进消息。先协商task、资源路径、read-only/read-write与TTL，再把绝对到期和transport handle绑定到delegation identity；control消息只管理生命周期，live mount、archive、object storage或Git adapter各自承担数据访问与回传。任务状态、传输可用与产物验收仍是不同对象，不能从START或DONE推出文件effect安全或目标已完成。<!-- source-family:SF-2026-ARXIV-2602-20493 -->

[有限协议原型](https://arxiv.org/html/2602.20493v1#S4.SS2)还暴露effect时点差异：snapshot transport可先staged再申请本地采用，live同步则文件操作已回写，不能靠事后review补出同一道提交门。应按transport能力选择隔离副本/只读或明确事前授权，并保存lease、快照identity、失败和清理回执；投影、状态恢复与detach/release均需预算。细粒度ACL/审计和多方冲突处理在原型中仍未闭合；权限、同步或恢复不能确认时回退原消息/只读artifact交换，由Ch81继续负责重试、补偿与最终提交，不把临时mount当隔离保证。

状态：root actual必要源/owner PRE通过；Ch83实际259/261、完整251–270及自身末注410写后非作者POST通过，窄锁释放。仅workspace projection/effect timing分支，无ACL或恢复一致性保证。

## 2602.20497v1 — LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration

完全落窗09:00～<10:51:31，2+2+2=6标准；历史预测训练/缓存分支gap定点深入。精确原源V3_CORE_2602.20497.txt §3.2 569–930、§4.1 1376–1426、Table4/ablation2139–2318、§7.1–2 4268–4328、Table8讨论4773–4778实际读。分noise阶段专属learned predictor，早K4/后K8，historyfeature线性投影+relative-timestep KAN标量残差调制；不是每channel独立时间oracle。先完整base轨迹作为训练target，GT history一期，再用自身预测与realoutput混合history closedloop两epoch，减少输入历史漂移，非推理GT。Custom100训练prompts、KANhidden256 BF16、AdamW1e-4/WD1e-4/gradclip1，未复现。

FLUXdev/schnell DrawBench200 1024²/A100，Qwen200 1328²/H20（lightningA100）、video956prompts480×640×65/50steps/H800；质量ImageReward/CLIP与对baseperceptualPSNR/SSIM/LPIPS分别测，不是真实生成真值。Table4 N5 segmentedKAN与nonseg ImageReward同1.00、PSNR30.96 vs30.77；N10 .91 vs.88、增skip仍较差质量，不能采用“大幅stage增益所有配置”或KAN universal superiority。schnell supplementary1.15s vs2.13s/4xFLOPs非4xwalltime，未将训练搜参纳入在线speed。Table8 LESA .81GB缓存高于TeaCache .69、TaylorSeer ImageReward1.02更好；VRAM不是全模型residentmemory。训练/历史K/predictor与多stage维护另计；seed/CI/生产batch/concurrency/SLO NotDisclosed。

actual Ch24 545–558混入自产历史训练、缓存近似/KV精确写入，完整545–563读；有原则但没有“按noise阶段从历史预测中间feature、离线GT→closedloop预测输入训练”的替代机制，非只缺论文名。拟在558跨chunkcache反侧后、560原source注前两段+自身末注；原chunk-reuse不被覆盖，新time预测不拥有环境truth：

沿去噪时间的缓存也可从“直接复用旧feature”改成“根据近期feature预测下一次中间计算”。一条学习分支按noise阶段分配predictor与history窗口，用history投影和timestep调制形成残差；先以完整base轨迹监督，再混入predictor自身历史训练，使训练输入覆盖部署预测误差。这与沿chunk复用、KV写入纪律不同：得到的仍是当前block计算的近似值，不是已验证环境状态，时间网格、history来源、stage边界与predictor revision须共同保存。<!-- source-family:SF-2026-ARXIV-2602-20497 -->

[有限生成对照](https://arxiv.org/html/2602.20497v1#S4.SS3)中，小跳步时stage拆分的增益很小，扩大预测跨度仍损害保真；更少FLOPs也不等同比例wall-clock改善，另有轨迹采集、预测器训练、历史驻留与刷新费用。质量proxy、参考一致性和在线成本须分别验收，不把短prompt池中的缓存收益签成泛生成保证。采样网格/条件漂移、历史误差或净费用不合适时缩短预测跨度、刷新完整feature或回退全算/已校准复用，保留原chunk及精确KV提交分支。

状态：root actual必要源/owner PRE通过；按批准位置移至历史匹配后/具体cache前，Ch24实际556/558、完整552–568及自身末注1741写后非作者POST通过，窄锁释放。原chunk/KV分支保留，无预测truth或零训练/cache费用权限。

## 2602.20501v1 — Probing and Bridging Geometry–Interaction Cues for Affordance Reasoning in Vision Foundation Models

终态：root实际§3/4及Ch23相关正文独核通过5分标准完成/仅报告；不降分、不新增书段。下方“拟/待root”仅提交前描述，现由此终态覆盖。

完全落窗日期见V3_DATE_PACKET.md同ID，2+1+2=5标准。精确原源V3_CORE_2602.20501.txt §3 396–529/529–690、§4 735–803实际读；DINOv3 densefeatures在nounattention crop ROI后PCA，FluxKontext受限agent/object/verb editingtemplate提verb跨层attention，以NSS选geometrybasis再融合。不是实际动作/物理接触GT、也不因generation失败时attention仍稳定证明internallygroundedcause；DINO完整物体context与极简ringview不同画面，不能把几何衰减唯一归给semanticcontext干预。

UMD linearprobe/几何depthnormals比较与qualitatives，AGD20K test未用traininginteractiondata，评价interactionheatmap KLD/SIM/NSS，fullgeometry×interaction优于onlyinteraction；不是真实环境可执行affordance、用户外population或闭环安全。混合pretraining不同VFMs未匹配，不因DINO与Flux complementary就授任意模型组合。§4.3 nounmap噪声/generation不稳、浅层openloop fusion限制明确，video unified是future未支持。额外生成、attention capture、PCA/NSS与多模型featurecost；GPU/precision/batch/seed/全latency/SLO NotDisclosed，未复现。

Books拟 **仅报告**：受限representation probing/fusion与观察反侧是现principle的实例，未建立新通用感知计算或验证contract。Actual Ch23 88–99保raw视觉/sceneprior/groundingidentity、attention不证明causaluse及layerreadout，130–155 encoder生成/理解分责、几何probe不授完整encoder已有原则；新affordance heatmap不能升级为环境状态/动作authority。不因新增两model/PCA名字制造知识gap，几何/交互各sensor经验留Report。待root必要Evidence/Only actual核，无锁。

## 2602.20502v1 — ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory

终态：root实际必要源/Ch81完整相关论点核验通过标准完成/已有覆盖；无改书，下方“拟/待root”为提交前记录。

完全落窗09:00～<10:51:38，2+2+2=6标准。精确原源V3_CORE_2602.20502.txt §3 488–545/610–705、§4 867–918/1195–1234/1485–1524、§5 1730–1851、§6 1852–2005/2268–2315 actual读。离线crawl静态UI状态/单action边构图，生成OpID/typedvariable程序sketch、AST保分支/loop；BFS在当前state链接到op起点、loop return invariant、语义替换/全局root reset，unresolvable才vision fallback。MixedPython/UI plan node被actor执行，Python exception hotpatch、UI timeout snapshot/DOM re-ground并改SMG；node局部修复不等effect transaction或完整恢复/回滚，代码sandbox安全只是声明未验代码。

WebArena Reddit106题、actor Claude4.5Sonnet与AOccam GPT4Turbo基座及token单价不匹配，95%vs66%和.06vs.71不是纯programmechanism归因；1.8vs10.2calls、118vs237秒为作者有限设置结果。初plan约6.8k-prefix依APIcache，图构建/更新重crawl摊销未纳入完整费用。Manager identity歧义与MLforum空格判定失败表明精准目标/评价未闭合；大UI redesign须重crawl，不能用局部无失效传播陈述签任意GUI稳定性。GPU/precision/seed/并发/SLO/维护预算 NotDisclosed，未复现。

Books拟 **已有覆盖 AGENT-WORKFLOW**：actualCh81 64–83明确run identity、transition precondition/effect receipt与模型nextstate只是建议；1022–1043稳定procedure可以编译skill但runstate仍可见，solver是有覆盖域/verifier的候选artifact、offline构建费/漂移回退不可隐藏。此程序/SMG是有限GUI实例，不改变proposal/effect/state owner；Report保scope与不匹配对照而非论文名gap。Root待actual必要源与Existing，无锁。

## 2602.20515v1 — FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill

终态：root实际必要源/Ch43 PRE通过，actual398/400、完整388–410与自身439末注非作者POST通过，锁释放；下方拟段已落实，非日级Complete。

完全落窗日期V3_DATE_PACKET同ID，2+2+2=6标准；实际KV访问/驻留gap加深。精确原源V3_CORE_2602.20515.txt IV-B944–968/1020–1153、IV-C1153–1222、TableI/II/III1419–1527、V1536–1625 actual读。FlexPrefill head-pattern selector流式compact scores代替大intermediate，在指定稀疏索引后把head/query需求bucket成KVblock→consumers joblist，KV-major顺序处理；remaining-use由此有限job图精确计数，归零evict，hot/cold URAM和boundedlookahead只在有容量时fetch。不是一般动态请求的未来访问oracle，不授所有selector数学等价或在线batch可直接套用。HybridMPU INT8乘INT32accum、LUT/DSP混用为硬件实现分支，未复现bitexact与代码。

U280 achieved175MHz/8GBHBM460GBs vsA5000 24GB768GBs，batch1 Llama3.2-1B/3B、Qwen2.5-1B；TTFT4K–128K，RULER表4–64K。TableIII Llama1B BF16Flex61.68→INT8Flex33.44/FAST33.07，3B77.74→63.45/61.28，不能称BF16等质量加速。Matchedremaininghardware cache16MB ablation作者2.5x/65%hit，Hybrid1.8x；整A5000比较还混CPUoffload indexing与W8A8路径，1.5–2.5x只受限实现对照。Energy Token/Joule以prefill token count1、nvidia-smi/Vivado估计，不等request总费。URAM95%利用；packing/joblist/selector/固定点质量、专硬件编译/刷新费用单计，在线concurrency/SLO/seed/CI NotDisclosed。

actualCh43完整385–406：blockunion改善locality/overfetch与selector质量、总结memoryblocking已有，但尚无选择后把稀疏需求反转成KV-major消费者图并用remaining-use驻留/释放的执行分支。拟在396 union反侧之后/原source注与总结之前两段+自身Reviewnotes，保union与dense原方案：

选择完成后，还可把稀疏索引反转为“每个KV block有哪些head/query消费者”的有限job图，按KV block顺序处理，减少同一block被不同query反复gather。由已确定的job图保存remaining-use，消费后递减，归零才允许释放；有限缓存可按剩余复用分hot/cold tier，并在容量允许时有限lookahead预取。这改变的是访问/驻留schedule，不是target score或selector authority；remaining-use只对当前已冻结索引有效，不预测后续请求、Decode或未建图的访问。<!-- source-family:SF-2026-ARXIV-2602-20515 -->

[单FPGA原型](https://arxiv.org/html/2602.20515v1)说明这种schedule需与index construction、packing、banked accumulation和低精度算子协同；更少gather不自动保持原浮点质量，也不推出通用GPU/在线batch收益。其W8A8对照在RULER明显低于BF16，缓存空间与专用逻辑接近硬件预算；应分别验收selector/数值误差、job构建费、KV驻留、TTFT与完整request费用。索引变化、缓存pressure或净费用不合适时重新建图、减小复用范围或回退原query-major/dense路径，保留block-union的简单方案。

待root实际必要源/owner PRE；无Ch43锁，不采用source的全球“preserves semantics”或FPGA速度headline为生产保证。

## 2602.20528v1 — Stop-Think-AutoRegress: Language Modeling with Latent Diffusion Planning

终态：root实际必要源及Ch24 286–297已有覆盖通过；标准完成，未新增Books，下方拟判过程由此终态覆盖。

完全落窗日期V3_DATE_PACKET同ID，2+2+2=6标准。精确原源V3_CORE_2602.20528.txt §3 705–980/1030–1142、§7 1970–2015、AppB3380–3401/F4380–4489 actual读。SentenceT5XL 768D continuationembedding加噪→DiT投8softprompt→AR decoder读取prefix→第二DiT预测denoise，两lossjoint学continuation token与diffusion；推理先采continuousplan再AR realization，训练含低/高noise供semantic/prefix不同依赖，不是推理读取GT未来句子。没有nativeCoT/内部可验证规划证明，也不授通用暂停/恢复协议。

GPT2Large774M base +两DiT6层总956M，FineWeb16B/128长、250ksteps batch512 AdamW5e-4，β5；C4生成5k×64continuation/32prefix，Llama3.2-3B PPL、GPT2Largeembedding MAUVE、lexicaldiversity分账，三组generation均值/SE不等语义真值或所有长文coherence。50DDPMsteps主配置，AppB DPMsolver5–50 steps/250×96token/32prefix；15–20steps收益plateau而latency继续涨，planning未做KVcache、重复prefix。训练预算/backbone与GPT2XL/Pythia不完全匹配，当前墙钟不是架构因果收益或未来optimized承诺。GPU/precision/batch/concurrency/SLO NotDisclosed，未复现。

Books拟 **已有覆盖 MULTIMODAL-GENERATIVE-PARADIGMS**：actualCh24完整286–294分开global semantic prior与local token realization、latent信息丢失/两阶段versioncoupling/decodercost与AR回退，jointtraining含decodernoise/lossweight/timesampling身份和分别验reconstruction/PPL/diversity/NFE。STAR的SentenceT5/8softprompt是同分责的受限实现，噪声控制/共享AR权重未提出新的生成commitauthority；不为模型名字造gap，Report保trainingGT与online sampledplan差别和未cache费用。待root必要源/Existing，无锁。

## 2602.20532v1 — Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for Scalable RL Post-Training

终态：root实际必要源及Ch27 1069–1105已有覆盖通过；标准完成，9%/14%冲突不采用单一成本，下方拟判由此覆盖。

完全落窗日期V3_DATE_PACKET同ID，2+1+2=5标准。精确原源V3_CORE_2602.20532.txt §3.1 897–955、§3.2 Eq5/6 1100–1193、Eq7 1245–1396、§4 2138–2180/2278–2440、limitations9418–9431/G9568–9619 actual读。Curator选择问题→同oldactor rollout/update→oldtrajectory由newactor re-score，likelihood ratio×oldadvantage提出perproblem first-order policyimprovement，再按采样概率importance纠正部分反馈、负entropy OSMD/neuralclippedcurator训练。Actor联合更新耦合问题，utility不是独立样本因果贡献；不采用未读proof的普遍regret或nonlinearclipped实现保证。

Qwen3.0.6B curator/Qwen2.5-3B actor默认GSPO；Countdown/Zebra/ARC各30k、math12k，8rollouts同用于actor/curator。固定backbone/actorupdate比uniform、SECadvantage bucket、PCL50%success；每10step看heldout、前100step取peak，非封闭test/固定最后checkpoint，额外curator训练未match总compute。20dormant+5warmup、samplingprior防早期collapse；absadv/regression与小模型/candidatebatchablation，只支持受限creditchoice。奖励可靠/actor稳定是假设，curriculum不能修复collapse。A100/H200；mainlimitations/AppH约9% vsAppG约14% overhead自相不一，不授单一完整成本数字，保非零再score/curator费；precision/concurrency/SLO NotDisclosed，未复现。

Books拟 **已有覆盖 TRAIN-DATA**：actualCh27完整1069–1097 checkpoint-coupledselection、optimizer-aware虚拟step/heldout影响近似与有限budget、selector只能admission不拥有objective及samplingprobability/policyrevision；1095–1105 dynamicreference first-orderinfluence/proxytransfer/drift与冻结mixture回退。Bandit/ratio是该local feedback路线实例，未授unbiased样本causalvalue/任意全域curriculum；必要Report保已选观察与未知未选、neuralclipping/theory分责，不为5分统一添段。待root实际源与Existing；若独核认为缺partialfeedbackcredit长期分支，仅重开该owner差额，无锁。

## 2602.20463v1 — A Long-Short Flow-Map Perspective for Drifting Models

终态：root实际长短组合、faithfulfeature未决与必要反侧/actualCh24核；标准完成，仅报告通过。受限kernel解释保留正面意义，不因理论或小实验一概不入书。

完全落窗日期V3_DATE_PACKET同ID，2+1+3=6标准。精确原源V3_CORE_2602.20463.txt §3长短分解1435–1488、endpoint theorem2612–2850、Eq21/discussion4410–4556、§6 9066–9230 actual读。Globalmap由longtransport和短terminalmap按semigroup合成；terminal估计firstorder产生attraction，secondordertrapezoid引出balancedattraction-repulsion，kernel与p0依赖，Gaussian对应Gaussiankernel而不是任意Laplace。精确数学flowmap不等有限batch learnedpushforward；endpoint公式通过估计p_t近似，mollifier/正则假设不能消除训练偏差。仅保该受限理论解释，不复制完整likelihood/cookbook或声称本地核完所有证明。

2D50k点/8层128MLP、batch4096 LR1e-4，各dataset600k/50k/150ksteps有analyticGT；CelebAHQ30k/SDVAE/DiTB2/MAE100kstep；MeanFlow400ksteps非预算匹配，不采用14.71vs12.4作机制公平优劣。Feature-space无特征训练失败、四个保完整信息feature仍较差于千feature说明informationpreserving不等faithful优化方向；作者明确Question5.3仍开放。LR/batch64局部成功不反驳其他dataset大batch需求。GPU/precision/完整kernel估计费用/seed/CI/servingSLO NotDisclosed，未复现。

Books拟 **仅报告**：newterminal/kernel解释及有限likelihoodtoy不建立可迁移训练/执行contract；Ch24 actual517–529已经分开traininterpolation、trueflowtrajectory、learnedcompositionregularizer与质量/NFE费用，不授flowmap半群保证。Feature faithfuldirection未解决，不能把完整信息proxy升为generativeobjective等价。保Report局部新理论/反侧，不将未经采用的闭式terminal推导扩成Book recipe。待root必要Evidence/Only，无锁。

## 2602.20479v1 — Path-Decoupled Hyperbolic Flow Matching for Few-Shot Adaptation

终态：root实际径向norm、tangent/diameterstop、Table反侧与当前Ch23方向核；标准完成，仅报告通过。该有界fewshot读出增量暂不需重构现有geometry/readout论证，非只有authority变化才有长期价值。

完全落窗日期V3_DATE_PACKET同ID，2+1+2=5标准。精确原源V3_CORE_2602.20479.txt §3.2 736–785、§3.3 933–991、Algorithm1394–1554/1554–1605、Table/ablation2322–2368/2632–2804与PCA3214–3228 actual读。CLIP-LoRA后learnablenorm把textprototype近origin/image外侧，Lorentz geodesic配GTclassprototype、stepwise tangent更新+contrastive局部监督；nearestprototype距离低于classcount函数×textsemanticdiameter停止，输出trajectory累计距离nearestclass。有限labelprototype/curvature下的fewshotclassifiertransport，不是一般跨模态truth或无交叉路径证明，PCA可视化不能证disjoint corridors。

11datasets/4或16shots平均3seeds Top1，CLIP-LoRA、FMA及CHA/PO/DS消融；HFM也有slice未全领先，不采用universalgeometricenhancer或guaranteedspacing措辞。ResidualMLP+timestep、κ1/αtext=.5αimage/H.1/lossweight.1 AdamW2e-4cosine；多阶段feature/velocity训练、geodesic迭代/类prototype距离费非零。GPU/precision/完整latency/productionbatch/SLO NotDisclosed，未复现。

Books拟 **仅报告**：明确潜在geometrytransport贡献仍保5分，但目前只给固定classfewshot读出/路径proxy，没有改变长期multimodalproducer-consumer/grounding权限contract或通用geometricflow成立条件。实际Ch23相关readout与geometryprobe不是空间truth，body88–99/localreadout与encoder/consumer分责已有；不为换Lorentz/MLP名字造gap或把classification训练路径升环境/生成authority。待root必要源/Only，无锁。

## 2602.20480v1 — VINA: Variational Invertible Neural Architectures

终态：root必要源/actualowner PRE后授权窄写，actual Ch24正文194/196、完整184～203及自身末注2125 POST通过，窄锁释放；实际末注已同步，非日级Gate。

完全落窗日期V3_DATE_PACKET同ID，2+1+2=5标准，critic loss→distribution校准缺口定点深入。精确原源V3_CORE_2602.20480.txt variationalmethod900–1073/1066–1126、Assumption3.1 3190–3544、Theorem3.1/主证明步骤3544–3790、criticfiniteparameter7130–7177/moment8255–8410 actual读。T(x)=(y,z) supervisedy误差+critic variational fdivergence约束joint(Y,z) vs(Y,Z)，取逆(y,z)给候选posterior。理论要求realizability、整个T/Tinverse uniformlybiLip、uniformgeneralization、(1+a)moment及vanishingcriticapproxgap；Pinsker→TV再truncation/moment→W1，结论对P(Y∈A)>0观测集合且常数依赖A，不授每个点posterior/任意大模型适用。

这把bounded-support改finite-moment而非“去掉所有假设”；有限critic只给variationallowerbound，实际smallloss不自证ηgap或globalclass条件。SyntheticParetoα1–10/10DGaussian、coupling2/6/8层等只局部支持重尾与capacity敏感；oceanacoustics科学域结果不采用，4DOFIK亦不授VLA执行能力。采样/critic容量、saddle训练与inverse成本另计；真实LLM/domainextension、GPU/precision/端到端SLO/完整预算 NotDisclosed，未复现，未展开无关证明。

actualCh24完整182–194已分learnedmarginalvelocity vssolver、moments不恢复fulldistribution与表示共享端点，但未承载invertiblemodel“critic拟合低不等posterior校准/finite moments仍依赖criticgap”的长期证据条件。拟在188 momenttransport段后/190表示端点段前两段+ownnote（新branch不改原FM/moment/bridge）：

直接学习可逆映射是另一种分工：把输入映为观测分量和latent分量，用监督误差约束观测，再以critic匹配观测与latent的联合分布，最后用inverse产生给定观测下的候选样本。它把条件分布误差移到模型类、critic和训练泛化，而不是交给数值solver；逆可计算也不等于posterior已校准。有限critic给出的variational值通常只是所选模型类能看见的差异，拟合值低仍可能漏掉critic无法表达的分布差。<!-- source-family:SF-2026-ARXIV-2602-20480 -->

[受限定理](https://arxiv.org/html/2602.20480v1)以realizability、统一双Lipschitz、uniformgeneralization、有限高阶矩及逐渐消失的critic近似gap，把训练误差连到正概率观测集合上的Wasserstein误差；有限矩放宽bounded-support，不删除其余条件，也不签每个观测点的真posterior。更强critic增加采样、容量与saddle优化费用，重尾/稀有观测还改变误差常数；应分别检查critic表达、表示信息、实际条件质量和总成本。条件或净预算无法确认时，保留已校准density/score模型与原sampler、缩小采用域或交给独立条件验证，不让训练loss自己取得分布真实性权限。

待root actual必要源/owner PRE与Ch24窄锁；无锁无写入。

## 2602.20555v1 — Standard Transformers Achieve the Minimax Rate in Nonparametric Regression with C(s,lambda) Targets

终态：root实际B6原核心及Ch4三阶梯核，6分中心Disputed通过；冲突仅σ²>0非退化Gaussian与固定有界Y，不说σ=0或全部approximation失败，无Books。

2+1+3=6标准。拟采用：standard softmax/ReLU Transformer的Hölder近似/ERM泛化阶不是训练算法保证。Actual exactv1 §1.2 theorem1/2/3、§2.1 grid/Taylor关键构造及§2.3 covering→excessrisk主步骤已读；不遍历42k行证明。维度d×n固定、γ=s+λ、模型width/parameter bounds随m增长；rate m^(-2γ/(2γ+dn))×log²m保维度压力，pointwise比Lt要求更大架构。§8明确标准Transformer ICL及真实优化率仍开放，非LLM pretraining保证；纯理论hardware/precision/latency不适用，未复现。

决定性中心反侧：§1.2 txt2284–2448同一setup Y=f0(X)+ξ、iid Gaussian varianceσ²，又要求|Y|≤BY固定有限常数；非退化Gaussian与boundedresponse不能同时成立。未见对Y额外truncation/条件化解释，不能自行改成boundednoise或代作者补ERM条件。因此拟 **中心Disputed** 保6分与已读approximation局部意义、不授中心minimax正面Evidence/Books。精确原段[V3_B6_CORE_PACKET.md](V3_B6_CORE_PACKET.md)1–11；若root认为可安全采用独立approximation子命题，仍不借此签regression中心。重开只需一致noise/response假设与对应ERM证明，不展开无关Appendix。ActualCh4 39–59/247–285三阶梯/UAT存在非训练已有；本次不以成熟原则添段。待root实际定点核。

## 2602.20566v1 — BFA++ multi-view VLA token pruning

终态：root实际B6原核心及Ch23完整482–522核，标准Existing通过，无新增Books。

2+2+2=6标准。拟采用：同view局部保留再按camera×regionimportance全局裁剪，避免直接globalranking丢wrist；scope为pi0/RDT受测camera/task。Actual exactv1 III-B/C txt430–515/605–1053：gripperphase/VLM或bboxoverlap/人工作offline inter标签、GroundingSAM region为intra标签；两predictors按CLS/visualtoken联合posttrain/BCE，空间平滑后固定localratio，再乘viewweight作globalratio。不是读实际contact真值或证明所有相机阶段。

决定性对照：IV-D txt1550–1675 directmultiply一次ranking主view占优丢wrist，hierarchical均值.638 vs.565/onlineannotation1.3Hz并更差；pruneratio过高quality反退，adaptive ratio速度不稳。IV-A1055–1150同dataset/steps，pi0 5000/b256 vsRDT1200/b128；8A100 train/RTX3090 inference，sim100/real20trials，未给seedCI/precision/concurrency/SLO。pi0在backbone前剪以免KV失配，RDT在DiT2；annotation/predictor/spatialranking费不能用少token代替E2E。根源core见[V3_B6_CORE_PACKET.md](V3_B6_CORE_PACKET.md)13–27。

拟 **Existing MULTIMODAL-REPRESENTATION**：actualCh23完整482–518已区分global守恒/inter allocation/intra复杂度/具体selection，下层不能补上层被删证据，需modalitylowerbound/回退full；519–521另有削减层位置和identity/成本。camera阶段是此预算分层的有界VLA验证，局部先剪再global与现有层内/跨组件选择承载相同长期问题，不因VLA论文名重加。仅Report具体phase标签、KV接入点和wrist反侧；待root必要源/actualExisting，无锁。

## 2602.20574v1 — GATES: Self-Distillation under Privileged Context with Consensus Gating

终态：root实际B6原核心与Ch29 214–224/418–438/465–507核，标准Existing通过，无新增Books。

2+1+2=5标准。拟采用：同权重documenttutor与无documentstudent，不假定tutor真值；question共识gate后off-policy只留多数答案trajectory CE，on-policy全student有效rollout用clippedlogratio advantage，零共识zero loss。Actual exactv1 §3 txt330–470/658–1080；gate不是external verifier，context asymmetry/teacher刷新状态与loss角色分清。

决定性反侧：原§5.2 txt1509–1521同错/低diversity共享错误、answerparser和有效update删样本有成本；§5.3 adaptivechallenges未经oracle变29.8低于fixed35.4，不能由consensus普遍selfimprove。AppA.5 2575–2623 greedy GATES40 vsSFT40.3，maj@8优势不签单samplecapability普效。§4.1 Qwen3-4BBase/Nemotron文档、Qwen2.5-32B出题、预过滤5/8后551train50heldout，训练4/8，k8tutor+8student/b32一epoch；heldout参考亦32B8rolloutconsensus非独立humantruth。硬件/precision/完整预算ND、未复现。必要core[V3_B6_CORE_PACKET.md](V3_B6_CORE_PACKET.md)29–49。

拟 **Existing TRAIN-SFT**：actualCh29 214–224合成teacher/filterselectionbias、418–438 occupancy/teacherlabel非outcome、465–507同studentprefix privilege分布与周期teacher共享错误/额外forward及目标分账已具体覆盖；本项gate多数trajectory是有限selection实现而非正确性authority，即时sameweight相对snapshot是已讲refresh代价端点。Report保无oracle可靠性条件/两种loss差别/贪心反侧，不按5分强添新段。待root必要源/actualExisting，无锁。

## 2602.20577v1 — MVLAD-AD action codebook and priority masked decoding

终态：root实际B6原核心与Ch26 167–183核，标准Existing通过，无新增Books。

2+2+2=6标准。拟采用：KMeans waypointcodebook+softtopK embedding/reconstruction/metricgeometry目标，maskedgeneration先解action再生成reason；不是轨迹动态可行或理由忠实证明。Actual exactv1 III-B/C440–715、III-E935–1010及IV1070–1114/1370–1448；单waypoint来自data/centroid不保证任意串接动力学或安全，事后解释condition在固定plan不等真实policy因果。

决定性对照：TableIV N128trainloss.32/L2 1.73；256 .36/1.28；384 .53/2.76，大码本精细不等易学，小loss不等动作质量。Randomembedding ablationL2 2.39vs1.28支持受测geometry接口，不授domain外。LLaDA7B LoRA256/4H100 BF16/b32两stage各8epoch约9h，singleA100 inference；nuScenes离线L2/FR、textmetrics不闭环safety，未match全部ARbackbone训练/预算，不采用总体胜/最快宣传；seed/CI/concurrency/SLO ND，未复现。必要原段[V3_B6_CORE_PACKET.md](V3_B6_CORE_PACKET.md)51–69。

拟 **Existing MULTIMODAL-EMBODIED-VLA**：actualCh26完整167–183 codeccapacity与encoder扩容分责、更大码本不单调、reconstruction不等predictability/邻近code稳定、阶段mask不对应物理执行时刻；已承载此geometrycodec的长期条件。priority先action是该生成接口有界实例，不让text先后顺序改actuator authority。Report保geometricembedding验证/先action计划后解释与centroid非安全，不新增paper段。待root必要源/actualExisting，无锁。

## 2602.20558v1 — From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation in Production

root已实际必要原文与Ch75 194–204/245–278完整邻接，具体Existing通过，安全终态；下方拟判断保留过程原证，以此终态覆盖旧“待核”描述。

作者必要标准审阅已读§4.1–4.3/Length Reward、§5.1–5.2/§6.1–6.2/§8；2+1+2=5不因已有覆盖降分。机械原段与actual owner见V3_B7_CORE_OWNER_PACKET.md，待root独立复核，尚不计安全终态。日期同IDSubmitted02/24T05:15:24Z、Registered02/25T02:53:04Z秒精度，上界exclusive02:53:05Z，与官方cutoff推导的02/25 09:00BJT lower完全落窗。

拟采用：固定强oracle给verbalizer accuracy reward，再固定verbalized输入训reasoner；dataset三个月私有streaming、最多100interaction/10candidate、Discovery Recall@1，raw-input reasoner+42.8% vs verbalized+92.9%仅相对未披露绝对baseline的局部对照，不把50.1个百分点称全部机制独立因果。Ranking reward0、删lengthreward退步为关键反侧。Qwen3-8B/32B；硬件/precision/训练样本总数/绝对Recall/CI/productionSLO未披露；oracleAPI、双阶段GRPO、verbalization与cache失效均付费，蒸馏/cache只作者建议未实测E2E收益。未复现实现，通用跨域部署为未证实外推。

拟已有覆盖：AGENT-CONTEXT actualCh75 194–201consumer适配/旧接口回归，247–275任务充分性/非最短与break-even/原文回读；完整邻接245–286已读，Ch74/76交接亦已读。具体delta是日志rewrite+两阶段reward的局部验证，不新增通用保真条件；现有论证已经分开表示读取、目标任务与压缩成本，故不为单例扩书。待root核原核心/actualowner。

## 2602.20580v1 — Personal Information Parroting in Language Models

root已实际必要原文与Ch72 47–49/270–299完整邻接，具体Existing通过，安全终态；≤10prefix风险保留、不估总体黑盒概率。下方待核字样为过程原证，终态以此为准。

作者按安全信号深入受影响证据：§3检测/选样/定义与§4–5/§8–9；2+1+2=5，未遍历无关参考/附录。原段/actualowner见V3_B7_CORE_OWNER_PACKET.md，待root复核不计终态。Submitted02/24T06:02:03Z、sameIDRegistered02/25T02:53:35Z秒精度，exclusive上界02:53:36Z，完全落窗。

拟采用：Pile检测1750stratified人工审标得到483真PI，Pythia160M–6.9B六规模、真实原文前缀≤80token、greedy续写、Levenshtein ParrotScore/完整与部分span分账；email/IP规模增大复述更高，phone不呈同规律，70k→143k Pythia6.9B score近稳而prefix10/20/40/80显著影响测量。选自detector命中的goldset仅检precision未核recall、不是全Pile PI总体随机样本；完整复述不同于字符相似或部分片段privacy风险，不授任意黑盒chat泄漏概率。标注敏感数据与模型query有成本，公开语料限制现代模型适用性；hardware/precision/并发/SLO未披露，不作生产测量或DP承诺。无对非成员/随机前缀匹配control的独立因果保证。

拟已有覆盖：PLATFORM-SECURITY actualCh72 279–295 corpus/model/attacker条件与matchedcontrol/conditional fragment-completion非membership，以及47–49部分披露分账；完整270–299已读，Ch71/73交接已读。具体新证是受限PI选样前缀实验，既有sensor权限/部分与完整泄漏论证无需重构，不新增one-paper段。root独复待核。

## 2602.20659v1 — Recursive Belief Vision Language Action Model

root实际必要机械原证、Ch25 recurrent mutable/nextembedding/inverse前提通过，具体Existing安全终态。下方待核为保留过程原证，不重读/不补附件。

作者必要标准审阅完成、2+2+2=6，待root原证/actualowner复核，未计终态。§III-A–D/IV/V-C–E核心；公开区间09:00BJT～10:55:31 exclusive由sameID v1 Submitted02/24T08:02:16Z/Registered02/25T02:55:30Z precision得出。机械核心V3_B8_CORE_OWNER_PACKET.md，不是摘要。

拟采用K5recentframe＋previous256dim belief token条件整合、Gaussian prior/posterior再GRU更新，EMAfuture latent t+1/t+5 ELBO+inverse action辅助；once fixed intent与10–20Hzbelief/50Hzaction分时钟。不授learned“causal state”真值或任意horizon充分：fixed语义/对象身份假设、controller/sensor和real adaptation仍必要。4万simtraj约40Msteps/10tasks；DINOv2ViT-S14/Qwen2.5VL7B frozen、belief150M/80ksteps/b128、policy120M/100ksteps/b32、12A10080G mixedprecision；inference单A100平均episode不是productiontail或budgetmatched因果。40episode消融32.5→57.5→62.5→77.5存在重复模块/训练条件混杂，不分配总涨幅；real100traj微调/25trial68%不证明零样本普遍simreal。保真实短reactive/重观测回退。

拟Existing：actualCh25 402–438可修改recurrent状态vsappend-only、fixedstorage≠resolution/真值，与231–264 future-embedding/target drift/inverse-dynamics前提已承载具体论点；Ch26 122–141 high/low时钟与proposal/controller分责只交接。完整owner邻接已读，原关键counter充分，停止附件，无新Book段。

## 2602.20662v1 — TOM: A Ternary Read-only Memory Accelerator for LLM-powered Edge Intelligence

root实际PRE批准，作者Ch49窄写65/67两段＋自身末注2762；root非作者实际正文/完整55–75邻接与自身末注POST通过，安全终态Integrated，锁释放，本note已同步。下方草案和待核为过程，不授日级Gate。

2+2+2=6，具体固定base物理存储分支gap触发受影响深入，待root PRE；不是FPGA实机。公开09:00BJT～10:55:35 exclusive，同IDSubmitted02/24T08:08:41Z/Registered02/25T02:55:34Z。原§IV-B–E/V-A–B/V-E必要源、mechanical packet V3_B8_CORE_OWNER_PACKET.md已读。稀疏ternary00/01/10地址→bit组合逻辑把zero输出接地/CSE，base硬化ROM、ternaryadapter SRAM与KV共用、复用ternary×FP8/FP8×FP8树并VU相加；bank粒度/稀疏routing非单调，LoRA/context占SRAM面积/功耗，基型更新不因adapter恢复。

BitNet2B、ROM498.54MB/SRAM37.5MB、16lane×10MVU/500MHz、FP8activation/KV、默认1024context；64/128/256/512IO workload/batch1 CPU/GPUbitnet.cpp比较。证据是Verilog＋FusionCompiler/PowerArtist估算、ROM模块P&R（非全chip）、Verilator周期模拟；7nm跨65/28nm density normalization不是同片实测，未以该部分签TTFT/TBT倍率/能耗普效。未独立测同quality perplexity或adapter纠错能力，量化质量/能力不能从面积/带宽授予。原zero wake/latency宣传不作为硬保证，不读与采用无关ASIC全表。

actualCh49 55–69 staticNPU/adapter输入分支只有compile接口/参数运行期换值，不含参数作为逻辑固化导致base只能随chip/logic revision变更的存储密度选择；392–408已有stateonchip/固定layout但未承载稀疏weight硬化。因此拟在63后/下一静态KV标题前两段＋自身末注，前后完整49–72已读，邻Ch48/50交接已读。待root PRE/实际窄锁，不自写。

拟正文①：在模型base长期固定、单流低延迟且允许为该权重制专用逻辑时，可以进一步把不可变参数从存储artifact固化成ROM地址到权重bit的组合函数：ternary零bit接地、共享布尔子表达式，非零值再进入本地matrix-vector计算。与可换值的静态图不同，存储布局直接依赖该base的bitpattern；分布式weight bank配合本地计算/全局reduction，用面积与版本灵活性换片上带宽，参数稀疏不必经通用index解码。但稀疏率、bank尺寸和routing共同决定密度，不能从零参数比例推出同比面积节省或任意模型收益。<!-- source-family:SF-2026-ARXIV-2602-20662 -->

拟正文②：保留可写SRAM adapter能在fixedbase外叠加低秩更新，并复用同一计算阵列后求和，却不能把adapter训练/纠错能力当作base已可重写；adapter与KV共享容量，更多rank/投影和更长context会增加SRAM、面积和功耗。TOM的有限BitNet2B/FP8、cycle模拟/EDA与ROM模块P&R只支持该存储执行分支，不是fabricated wholechip、任意量化质量或零wake开销证书；跨node归一化不等同硬件实测。base频繁变更、质量未经验证、SRAM预算或芯片生产成本不合算时，可写SRAM/外存权重及通用backend仍合理，冷启动/完整request成本另验。

## 2602.20666v1 — BoxSplitGen: A Generative Model for 3D Part Bounding Boxes in Varying Granularity

root原机械关键＋actualCh24外AR/内conditionaldiffusion已核：采用机制由Ch24 33–59具体承载，改为Existing安全终态（非降分、非范围EX），不为box域recipe新段。下方作者Only拟判断保留为过程并由此次具体覆盖结论更正。

作者5分2+1+2标准必要证据已读§3.1–3.5/4/5.1–5.2/6/A.6采用采样设置，待root复核。sameID v1Submitted02/24T08:15:25Z/Registered02/25T02:55:40Z →09:00BJT～10:55:41 exclusive。mechanical core/owner V3_B8_CORE_OWNER_PACKET.md。

拟采用：SMART bottomup树反序做rootunitcube→选择pivot→条件两个childbox(2×15)→replacepivot的AR factorization，boxcount/pivotindicator喂conditional6layer512dimTransformerdiffusion，50DDIM/childsplit；另用3DShape2VecSet+ControlNet从box到shape。ShapeNet条件box集合在该family的geometry生成中可变grain，不授worldmodel或自由拓扑物理状态。Unconditionalinpainting同50步可比但略差，强finebox限制diversity；SpiceE使用不同backbone不能纯归因ControlNet，COV高可能alignment更差，训练树生成/两网络/每split50步与最终shape费用均在总成本。未复现，无人体审美或安全保证。

拟Only：actualCh24 33–59已有外层AR条件乘积/块内conditionaldiffusion联合读出与scalehistory/codec分责，包内原文足够承载该局部“选择结构＋局部生成”的解释；本项是有界3Dbox的variablegrain实例，不要求把generic生成主干重构成该boxsplit专有recipe。不是因3D/小实验/无authority排除贡献；本日报保正面的factorization及具体代价，Longterm owner框架目前无需新段。邻Ch23/25同语义交接已读，待rootactual核。

## B10 — 20720 / 20722 / 20727（root必要证据/owner与20722 POST通过，3项安全终态）

root实际B10原机械核心＋actualowner已核：20720=6 Existing Ch72 684–695/2855–2862；20727=5 Existing Ch30 191/203–207/213–231；20722=5深入gap Ch31 actual688/690、完整680–701及own1326 POST通过，旧17862marker未跨新段，自身末注同步通过，Ch31窄锁释放。以下拟段为提交前过程，由终态覆盖，47/148安全、101普通，非整日验收。

最小机械原段/对照＋actualowner见[V3_B10_CORE_OWNER_PACKET.md](V3_B10_CORE_OWNER_PACKET.md)，2623词3项；精确v1取回时间V3_FETCH_next-b10.json 2026-10-05T16:46:44Z。此前AB准入校准复用，未重开发现；同ID日期已在V3_DATE_PACKET.md有限核完全落窗，Submitted不是公开时刻。

### 2602.20720v1 — AdapTools: Adaptive Tool-based Indirect Prompt Injection Attacks on Agentic LLMs

2+2+2=6安全深入必要范围：§3/4/5.1–5.5/6.1–6.2原306–1095、1470–1705足够，未扩附件。sameIDSubmitted02/24T09:32:19Z/Registered02/25T02:56:57Z→09:00BJT～10:56:58 exclusive。采用：攻击者不只改payload，也按当前工具上下文选择更贴近良性下一步的目标，使单纯task/tool语义一致性更弱。灰盒可见最新tool，从全部benigntrajectory统计一阶转移M，再挑与predictedsuccessor embedding最相似的adversarialtarget；不是blackbox无轨迹攻击，更不证明一阶Markov是真实用户意图。LLM-as-optimizer最多5轮失败trace反馈，成功策略按embedding聚类/ASR损失δ合并；策略生成/验证/检索及transition统计有offline/API费用，CoT也非causaltruth。IPI3K3691benigntrajectory/277LLM risk评分highauthoritytool有选择人口，不估自然攻击率；六ReActLLM/InjectAgent/AgentDojo有限比较。Table4选择模块GPT4.1 ASR21.4→26.1/Qwen3-8B52.7→60.6，但UA44.8>43.8并非每配置工具选择都损utility；两模型受限消融、API成本促选择而非全model证明，攻击预算/seedCI/真实SLO未披露，不采commercial全优于open或“天然无法区分”。

拟Existing：actualCh72 684–695既有外部instruction≠trustedauthority、贴合目标不能跳effect/跨步权限，2855–2862已有attackgenerator/selector/opportunity/auditbudget一起冻结、selectedattack非概率上界。采用窄命题已真实承载；有限targetselection反证在Report保留，不为一阶Markov专有攻击实例另造安全机制。

### 2602.20722v1 — Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning

2+1+2=5标准＋actualgap必要深入；同IDSubmitted02/24T09:35:43Z/Registered02/25T02:57:00Z→09:00BJT～10:57:01 exclusive。原§3.1/3.2 639–1391、§4 1903–2030、§5.2 2285–2482/5.3 2483–2536已核，理论positive-improvement界未拟采用故不遍历AppA proof。BAPO freshgroup剔除全对/全错；badqueryFIFO限训练batch大小，每m步当前policy重新生成，在已观察meanreward进步且非全对时纳入新response；highqualityresponse只保最近3步按globalaccuracy调阈值随机补batch。Buffer记录promptID/groupresponse/reward/behaviorprob供importance ratio，是混合历史经验不是onpolicy；finite0/8不是无成功支持证明。Mini-test仅去复杂threshold，仍freshmixedreward+重读oldallwrong+历史50%response，支持必要组件而非全部机制因果。8A10080G/verl，1.5B/7–8B数学/planning/visualgeometry有限posttraining，问题与evaluation分割已明确；3epoch原0/8中31%vs19%改善不等普遍rulelearning。Batch常underfilled令backward工作减少，抵消重评/重算费用；更少rollout/同updates不可直接当同训练FLOPs或E2E免费。Precision、seedCI、最终部署SLO NotDisclosed，未复现。

ActualCh31 680–688只解释oldrollout/teacher freshness admission，不含把已筛出的“当前没学会”的query保留后再测可学性、和reusedresponse分账的采样选择。拟在原freshness段及其marker后、Humanfeedback标题前2段＋ownnote，先rootPRE/窄锁。拟段①：剔除一个group全对或全错能减少无相对advantage的更新，却不能把当时全错的query永久判成不可学。一个有界回放分支将query与旧response分开保存：周期性用当前policy重生成曾失败的query，只有观察到新的混合reward才进入更新；补batch时则使用短窗口内的历史response，保留其behavior probability用于分账。Re-evaluation改变的是当前学习支持，response reuse承担旧策略偏差，两者不能共用on-policy标签。

拟段②：有限group的零命中不是成功概率零，当前重测也会受verifier和采样噪声影响；FIFO容量、重测周期、reward范围与新旧样本占比共同改变训练分布。BAPO有限1.5B～8B/三类推理任务的mini-test支持这一batch构造分支，不签普遍正policy-improvement定理；变小的实际batch减少backward工作，故少rollout或相同步数并非整流程等预算。重生成、behavior logprob重算、存储与调参均付费；reward不可靠、policy漂移难以估计或成本不合算时，保留fresh rollout、短buffer与独立held-out验收，而不把旧成功轨迹当当前能力。

### 2602.20727v1 — ID-LoRA: Efficient Low-Rank Adaptation Inspired by Matrix Interpolative Decomposition

2+1+2=5标准必要证据；同IDSubmitted02/24T09:45:10Z/Registered02/25T02:57:07Z→09:00BJT～10:57:08 exclusive。原§4.1–4.2 561–987、4.3采用假设987–1105、§5.1 1580–1685/5.4–5.5 1702–1802足够，不采用附录全cluster最优理论。预训练W行做minimumsizeKmeans、每cluster取近centroid r行作为固定A_i；共享可训练B与inputdependent α_i=T·A_i h组合，RB把r activation分半分别同B投影再concat。Learned参数少不等不保存base/indices/分组、预处理与router不要计算；tokendependent α不能默默merge成一个固定BA。原RankAnalysis用“atmost kr”宣称actualrank更高，不足证明strict rank superiority；共享B限制与输入相关非线性均须分开，报告不采用该保证。§4.3 taskcluster/disjoint-lowrank/sharing假设不自动证明W-row近centroid识别真实tasksubspace；无需为未采用的泛化命题读完整proof。

两A800/Llama3-8B/Mistral7B，Llama3.2-3B组件消融，GSM8K/CodeAlpaca/Alpaca有限jointtasks、HExPHI refusal非独立完整安全。相同超参非各充分调优；parameterparity与SS/RS对照支持该共享/row选择局部路线，RB对MATH38.1<38.8、codepass10 38.2<38.6保反侧，不照录“除了MATH全胜”。Fig3单A800下45%extra adaptermemory/0.5%latency是额外分项，不是全模型HBM或生产SLO；batch/长度/precision/seedCI未在采用必要setup披露，未复现。

拟Existing：actualCh30 191名义rank≠effectivecapacity、203–207共享basis/模块系数条件与row-support分责、213–231输入条件容量/参数生成共同版本身份及不可随意merge/更多runtime费，已有采用的长程选择。此次frozenrowbank为有限共享方向/conditionalupdate实例，不要求主干加入该专有cluster/RB recipe；不是因无authority或论文名称已无便降处置，保可比参数预算正面观察和rank/代码反侧。

## B9 — 20696 / 20708 / 20715（root实际证据/owner与20715 POST通过，3项安全终态）

root实际全3项机械原证＋actual owner已核：20696=5 Existing Ch20 145–168；20708=6中心Disputed Eq6/11/12，不授正面safety/Books，prober具体split未披露；20715=6深入实际gap写Ch26，actual正文675/677、完整666–684与own1939 POST通过。原LWD marker定位已修回673原deployment段之后；ownnote同步实际通过，Ch26锁释放。以下拟判断为提交前过程，以上终态覆盖，本日44/148仍未整日完成。

机械原文与actual owner：[V3_B9_CORE_OWNER_PACKET.md](V3_B9_CORE_OWNER_PACKET.md)，2962词、3项；原HTML精确v1，V3_FETCH_next-b9.json有实际200/执行时间，仅源访问不计完成。日期同ID见V3_DATE_PACKET.md：均在官方cutoff09:00BJT之后且Registered精度ceil上界完全落窗。

### 2602.20696v1 — PromptCD: Test-Time Behavior Enhancement via Polarity-Prompt Contrastive Decoding

2+1+2=5标准审阅。v1Submitted02/24T08:56:52Z，Registered02/25T02:56:22Z，公开区间09:00BJT～10:56:23 exclusive。原§III/IV-A(1010–1459)、IV-B必要1459–1735、V-A1868–1940、VI-C/D2733–2872已读足采用命题，不扩附录。文本路径同一checkpoint的正/负prompt两分布取logPpos−γlogPneg，在正prompt plausible-head（λ·maxPpos）内选择；同一选中token同步写入两context，保持已生成前缀一致，并非两条独立候选答案。负prompt极小概率可把不合理token放大，APC不是正确性验证；γ过大破坏连贯性。视觉attention ratio的generic-pattern可乘分解与负prompt近uniform是作者建模假设，不是受控因果grounding；不授attention等同真实相关区域。文本四个7B/8B instruction models、NQ/ConFiQA/CoConflictQA counterfactualcontext分别测ConR/ParR，不等世界事实truth；视觉TextVQA不同crop/外工具预算有限。每token双forward，NQ TableVII latency约1.65–1.79x/throughput下降，硬件、batch、precision、长度、重复CI NotDisclosed，不采用医疗/法律普遍安全或免费治理宣传。

拟Existing：actualCh20 145–168明确heuristic score变换与硬候选mask分责、可能屏蔽正确token、处理顺序不可交换、完整decodingconfig入评价。这已经承载采用的长期选择：把条件对比当改变target分布的局部scoreprocessor，连同headmask、γ、双context/cache与成本一起验收，不能给原分布保持或正确性权限。保本日报同步双context这一具体实例与对照，不为prompt family造新sampling主干；并非因5分或工作量降处置。

### 2602.20708v1 — ICON: Indirect Prompt Injection Defense for Agents based on Inference-Time Correction

2+2+2=6安全信号触发受影响深入。v1Submitted02/24T09:13:05Z，Registered02/25T02:56:40Z，区间09:00BJT～10:56:41 exclusive。原§3/4.1–4.7/5.1–5.2必要743–1454、1672–1943已读。拟采用仅内部attention集中度是可训练attack sensor而非恶意真值、局部routing intervention须与utility/fallback共同验收：entropy/logN→FIS、min/mean/std聚合，选4敏感层×32head得到384特征，CNN/MLP/GMP probe31k。TrojanTools训练、InjectAgent/AgentDojo OOD评价，Table3 Qwen3-8B ADR80.1/98.0、URR62.3/69.6；5fold std不等独立population概率。ReAct有限模型，underattackutility与benignutility分账；255probe样本/<2min vs1.19M/>10h不同训练人口预算，不授完整runtime费零或收益纯归因。

关键未采用recipe边界：原Eq6对A使用entropy/logN，Eq11在“rawattentionweights”上percentile，Eq12以γ<1乘峰值，紧接文字称before-softmax并承诺再分配到benigncontext（txt1310–1450）。原文未明确同一A在这些阶段是logit还是已归一weight，不能自行补重新normalize或负logit操作；被选peak也不证明是恶意片段。报告只保有限作者观察，不复制exact执行式或“globalsemantic不受损”。若要采用此recipe，定点重开须官方明确A/softmaxplacement及对应实现/反侧，不扩大完整proof。

拟Existing：actualCh72 2257–2270现有head-removal vs routing-redistribution、内部sensor不持releaseauthority、whitebox身份/heldout校准、额外计算/误报及policy/工具权限回退具体覆盖该窄命题。此次IPI实验验证其一个局部切片，不新增部署防护contract；若root判断Eq12歧义阻止该family核心成立，保评分/候选改中心Disputed安全终态，不自行repair或EX缩池。

### 2602.20715v1 — IG-RFT: An Interaction-Guided RL Framework for VLA Models in Long-Horizon Robotic Manipulation

2+2+2=6标准＋actualgap受影响深入。v1Submitted02/24T09:19:50Z，Registered02/25T02:56:50Z，区间09:00BJT～10:56:51 exclusive。原§IV-A555–900/IV-B900–1137/IV-C1320–1454/V1465–1857/AppB2045–2142采用配置已读足，不扩其它附件。RoboEngine robotmask外RAFT flow阈值计pixel作为I_t标签，critic预测p_int(s)，flow初始noise温度T(s)=σ_base(1−αp_int)+σ_min；非交互探索较大、交互代理较高时较小，并以AWR exp(adv/β)加权flow-regression。交互proxy不是force/contact真值，外物运动、mask漂移会错配阶段；densehybridreward用成功1/T与按subtask completion time/weight的sigmoidpotential差，VLM/专家标注与critic估计不授通用reward或防hacking。

pi0.5、GalaxeaA1双臂、3camera/30Hz、chunk30/RTC、cloudA100+本地i7/RTX4070。4任务各60teleopdemo，再4轮×10HILrollout；非HIL对照100expertdemo不是自动整个pipeline等预算。30ksteps/b64/AdamW、actor5e−5/critic5e−6，σbase1.5/σmin.2/α.9；β.05、advclipping[0,10]。两困难任务full vs无IG成功85/70与70/55（均差15pp），同40人工干预平均77.5 vs62.5有限支持phasebranch；Fig5阴影是两任务minmax，不是seedCI，最终四任务82.5不能与该两任务均值合并。TableIV20trial/task，训练/annotator/critic/physicalrollout费用真实；一般newdomainreward尚无、HIL不scale，未复现生产或真实安全。

ActualCh26 657–678 fleet循环只解释policy/intervention版本与offline→boundedonline责任，318–322 BC/RL Q仲裁是另一机制；尚无根据交互代理连续调flow初始化方差的选择。这一actual差额可在671后原marker前拟两段＋自己的末注，待rootPRE和具体窄锁，不自写。拟段①：离线policy与固定探索噪声在阶段稳定时易复算；接近物体的精细操作与尚未接触的寻找阶段，对探索幅度可能要求相反。一个受限分支先用robotmask外的视觉motion提议交互标签，再由critic预测交互概率，将flow初始噪声方差随该概率降低；优势加权的flow回归仍在冻结轨迹与人工纠正数据上更新policy。改变的是候选动作的探索分布，不是接触真值或执行授权，交互proxy、mask/critic版本、噪声范围与数据来源都要进入训练身份。

拟段②：代理错把背景运动当接触，会过早压小探索；漏掉静态受力也可能在精细操作时放大抖动。IG-RFT的有限pi0.5真机两任务消融支持阶段条件化相对固定噪声的选择，不能把四任务成功均值、任务间minmax或人工干预数当安全/统计保证；视觉标签、subtask标注、critic训练与真实rollout均付费，整个pipeline不因同更新次数而等预算。交互标签不可靠、奖励不可信或物理风险不能隔离时，保留固定噪声/BC、离线更新与人工接管，controller和独立安全层继续持有最终动作权。

## 2602.20492v1 — Wireless Federated Multi-Task LLM Fine-Tuning via Sparse-and-Orthogonal LoRA

状态：root actual Eq16/20定点复核确认中心争议终态隔离，保2+2+2=6与候选身份，不授正面Evidence/Books；下方“深入中/拟采用”为提交前过程描述，已由此终态覆盖。A∼N(0,1)未normalize且式含i=j不能签近零Gram；mean-vector H构造C rank1不能擅补逆。重开须官方精确normalization、i≠j/有限维误差条件、H/C shape与逆的正规化定义或对应artifact，不靠LoRA成熟原则新写。


完全落窗日期见V3_DATE_PACKET.md同ID，2+2+2=6标准受影响recipe定点深入中。精确原源V3_CORE_2602.20492.txt IV-B2420–2650/3052–3188、IV-C3388–3466、IV-D4136–4220、V4646–4750/4900–5088 actual读。固定随机A首次交换后分存，局部B稀疏、按task平均input谱proxy分配layer稀疏；按通信/碰撞条件cluster选neighbor并tasklatentcode refinement作implicitrouter。Rawsource仍保中心公式歧义：Eq16独立未normalize N(0,1) A的Gram≈0不能签严格orthogonality/完全interferencefree；Eq20 C=H0H0ᵀ含C⁻¹，H0若mean vector则C rank1、逆不可用，需官方明确tensor shape/regularizer；refinedA乘normalizedlatent也需shape一致。不能自行补QR、pseudo-inverse或改formula。

作者DFL simulation至多15device，TableI10设备/LoRA r32、Qwen2.5-1.5B/7B多个binary/QA/math/code数据（只是测试LLM训练机制，不引入science领域研究），hardrouting是perfecttaskrouteroracle、singlecluster对照作者约1.3pp差；独立任务测试不证明多任务互不冲突。静态A/稀疏减少更新/交换条目不等无线E2E训练费、隐私或实际mobiledeployment；TableII预算百分比/基座参数口径未闭合，不授宣传86.56%请求/通信总费。Training epochs/seed/GPU/precision/实际无线吞吐/能耗/confidence NotDisclosed，未复现；theory证明未采用，不展开无关Appendix。

Actual Ch30 600–633 adaptercomposition行为不无冲突、因子坐标与gauge-invariant aggregation、support/参与人口与独立adapter回退已有明确边界，不能以“orthogonal”名字覆盖。当前拟采用边界：只保来源提出的固定投影/稀疏与topology原型身份，不复制未闭合recipe/orthogonality或implicitMoE保证。中心tensoridentity及有限高维近正交条件若决定该核心能否执行，需要root actual定点回核上述式；未授正面Evidence/Books，不用EX缩池，不为无artifact扩完整proof队列。重开只需作者Eq16/20/26精确shape/normalization/逆的定义或实现，非后文性能headline。

## B11 — 20732 / 20739 / 20743 root实际复核通过，50安全终态/98普通

root actual机械原源与owner核读：20739/20743具体Existing通过，20732原自己Ch45把粗筛当省child评分/metadata被独立纠正，授权仅自身196段与1726note实际修正、完整190–205写后POST通过释放。最终B11=1I2E，合计50/148＝19I21E5Only5D、98普通。下方拟Existing为提交前过程描述，20732实际纠错整合替代该提案；不授整日Gate。

当前47/148安全终态、101普通；下列三项作者必要审阅完成但未计安全终态。机械原证与owner包[V3_B11_CORE_OWNER_PACKET.md](V3_B11_CORE_OWNER_PACKET.md)约2500词，原源精确v1与当前正文非摘要。日期同V3_DATE_PACKET：下界02/25 09:00 BJT，上界依次10:57:15/10:57:25/10:57:31，完全落窗。未核代码/未复现，无共享Books锁。

### 2602.20732v1 — CHESS

2+2+3=7深入。原txt §3.1–3.3 363–720/1114–1162，§4 1163–1265，Table1/§5 1294–1608，AppC2380–2434；采用page对齐层级proposal与条件刷新，而非meanK正交等attention真值。Recent-window meanK anchor对各层meanK求dot，Grid/Chunk/Page比例保留且sink/recent页并集。实际§4.2将**全部节点**semanticvectors合成单GEMM，再boolean parent mask，不采用粗筛必省掉所有child scoring的复杂度承诺。原KV逻辑视图不重复tensor，仍有centroid/pointer/scoring费；本文“reconstruction”是刷新选择上下文，未明确按被删KV重新prefill的完整恢复协议，不代补exact backtracking。

Entropy/varentropy只是confidence/instabilitysensor，LongBenchV2同数据99percentile校准不认证正确性，AppC动态约10pages对固定6pages非同刷新次数预算。四H20/PyTorch2.5.1/CUDA12.4/page32；quality LongBenchV2和syntheticperf分开，73%/40%/1%KV总体30.4/32.2/33.2 vsFull30.2，非每slice全面优于，H2O20%34.0仍高。Quest独立kernel且仅batch1，不把peak4.56x或作者A100/H20语句混作匹配所有平台/SLO；precision、seed/CI、并发及selectionmetadata绝对费NotDisclosed。Actual Ch45 188–198已经具体承载versioned accessplan、selector proposal≠attention/事实、Grid→Chunk→Page对齐与coarsemiss/full回退；拟 **已有覆盖 INFER-KV-CACHE**，这些具体实现/校准读数留Report，非论文名gap，不改正文。

### 2602.20739v1 — PyVision-RL

2+2+2=6标准，工具runtime安全signal受影响内容深入。原txt§3.1 400–436/§3.2–3.4 659–812、SFT/RL851–1008、§4.1–4.3 1009–1189/impact1230附近。Python code/interpreter tag interleaving，将完整history返回MLLM；video只在runtime保全视频，由code选frameplot进入模型，不等模型看完全视频。Reward Racc+0.1·toolcount·1{correct}：final正确**不证明每次toolcall有用**，可压低组内短而正确trajectory的relativeadvantage。Oversample→filterzero rewardvariance/brokeninteraction→按shapedrewardstd排序，std混合toolcount并非纯题难度；去stdnorm只中心化A=R−meanR，不消掉所有正确样本负adv。Malformed排除是训练人口选择，不认证Python sandbox或推理安全，作者impact承认hostfilesystem风险。

8H100，700step，oversample32/train16/group8/lr1e−6，trainmaxturn4vs2而eval30/context32K；singlecomponent消融中去toolreward早期略好，500step以后落后，保留stdnorm波动更大，非普遍优化定律；生成、Python等待/处理、group排序、被剔除样本费另计。VSI5kvisualtoken/44.0对Qwen45k/38.0但SpaceR25k/45.6更高，不授无损/全runtime9x降本。V*191sampleavg@32不与单greedy合并；TIR正文+3.8/表注+7.3不采用其中任一未闭合headline，seed/CI/精度/端到端SLO ND。Actual Ch31 949–955 faultowner/剔除偏差与terminal≠turn因果credit、Ch33 104–134相对reward/zero variance/过滤费和2172–2178 jointdistribution/中心化非整个GRPO等价已经具体承载；拟 **已有覆盖 TRAIN-RLHF**，有界rewardtoolcount与课程实例留Report，不另写新recipe。

### 2602.20743v1 — Adaptive Text Anonymization

2+1+2=5标准，敏感文本外部评估接口定点深入。原txt§3 481–638、§4 641–775、§5 891–972、limitation1137–1145、AppA1402–1482与D1967–1980。学习prompt而非权重；seed→GEPA warmstart scalar→LLM生成richfeedback代码分解privacy/utility→roundrobin validation子样本/Paretopool→fullvalid最高aggregate选prompt。两代表task同1500forward预算消融支持该有限搜索选择，不授Pareto全局最优或fullvalid为独立test保证；111train/111valid剩余test，alpha.3/patience5。五任务原metric分别reidtop3、属性推断、spanrecall、PIentityrate与styleembedding距离，**不互换为实际身份泄漏概率**；统一Gemini2.5flash judge共误差/外发boundary未解决，localrewrite不等data全部local。

Qwen3-30B-A3B MedQA seed3.52/58.6→24.6/45.9（privacy/utility），Qwen2.5-7B5.18/47.1→7.29/41.2，明确utility退步，不授全部保持用途或医疗收益。作者约$1/task/model仅外部evaluatorAPI估算，不含localGPUprompt生成/推理，GPT5约$8testinfer预算角色不同；两RTX600024GB，batch/precision、重复seed/CI与walltimeND。Unweightedaggregate非hardprivacyconstraint/DP或compliance，richLLM反馈不创建隐私真值。Actual Ch72 253–260 learnedrewrite/Pareto、attacker/task/model/threshold身份、事实损伤与确定性redact回退已具体承载；拟 **已有覆盖 PLATFORM-SECURITY**，有限prompt搜索/实测retreat只Report，不为每搜索阶段新增正文。

## B26 — 20804 / 20921 / 20967 / 20971 / 21020，作者必要命题审阅待root非作者核

旧作者prepared停点原记录（当前已终态，以文件顶部及README为准）：最后五项合法精确v1 HTML必要方法、拟采用假设/主要推导与直接反侧已读，来源V3_FETCH_b26；[机械原证与actual owner](V3_B26_CORE_OWNER_PACKET.md)不替独立验收。B12～26共98作者必要包已备，作者未准备0，当时98项仍属普通独复/必要Books待办、原50safe不变。当时没有新Books lease/未经许可写入，尾3误判恢复尚仅题摘/日期待准入。

### 2602.20804v1 — Cooperative MARL diagnostics

2+1+3=6标准。§4–6将“benchmark含隐藏状态”拆为memory有收益且有使用、私人信息/同步/跨时间协调；paired seed/env/algorithm FF vs RNN return用单侧Wilcoxon，HAR为给定当前观测后的history/action条件MI，不把RNN赢或MI高单独当必需hidden-state推理。37scenario、IPPO/MAPPO×FF/RNN不共享参数、10seeds/每5%训练32episode/IQM95%bootstrap；permutation action null控制有限样本偏差，但max agent/max configuration是“所测方法是否有任何一个”人口，不能授环境最优/最坏性质。§7 noise按feature std扰动仅SimpleSpread/Reference局部，作者§7/8直接承认MI是统计非因果、长history/大action有限估计有偏、不作hard gate。训练预算/hyperparameter依scenario；本文采用无运行时或LLM拓扑收益claim，production SLO不适用，未核artifact不说复现。ActualCh66 36–47样本/scorer/production条件与Ch5 242–267 correlation→intervention阶梯具体承载；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，受限HAR/return诊断作为报告实例，不造每benchmark独立段、不宣称优化混杂已全部解除。

### 2602.20921v1 — Depth-uniform residual-network generalization

2+1+3=6标准理论。§2/3离散步长τ=T/L，固定T、有界data与参数norm、continuous controls C∩H1、activation φ1(x−α)−φ2(−x−β)且αβ>0、loss局部Lipschitz；Proposition2追踪activation三区域负结构校正，Theorem5/9 O(S^-1/2)兼容depth limit，非无条件层数免费。§4主步骤：output-coordinate permutation同类→loss contraction→每层结构项截断保证递归系数非负→τL=T及Grönwall；连续控制采样/延拓与H1时间regularity连接离散/连续。负校正C_s^l存在性且可0，Remark3.7称难计算/难直接设计activation，M仍指数依赖T、Lipψ与参数界；不采用“learnable threshold必提高泛化/任意Transformer/widerfree”或全实验归因。只采用条件化理论解释，不需GPU/latency，未做实验证明或全部附录复现。ActualCh4 41–55 capacity/optimization/generalization分账已有；这项有界ODE-scaled ResNet具体负项尚不能成为当前通用activation选择recipe，不需要重构该论证。拟**仅报告**保有限depth-uniform机制与C可0，不因理论或小模型一概排除。

### 2602.20967v1 — Intelligibility-guided observation addition

2+1+2=5标准。§2 Eq1将noisy y与enhanced xhat在waveform做S'y+(1−S')xhat；Eq3冻结ASR同时对两者conf，ratio conf(y)/(conf(y)+conf(xhat))加epsilon，非ideal inverseWER oracle部署。Whisper geometric tokenprob按segment token数加权；Parakeet/W2V Tsallis q.33和CTC minpool不同proxy身份。§3 VoiceBankDEMAND训练、CHIME4channel5真实/模拟各1320/16k，Demucs causal500epoch b16与GRKAN noncausal200epoch b4、Whisperlarge/Parakeet0.6Bv2/W2Vlarge960h；GT SNR只是oracle比较、3class predictor额外训练，不能合并为同费因果。§4三个CHIME条件ConfOA WER仍劣于noisy；confidence-miscalibrated组OA可胜hard-switch不证所有错误conf获救，frameOA较差只支持temporal continuity局部反侧。无需新OA训练不等零费：SE、两次confidence scoring、最终ASRdecode都付费，hardware/precision/inferencebatch/latency/seedCI ND。ActualCh23 37–47模态接口/时序与信息损失、Ch66条件化scorer已在；该frozen-ASR waveform权重是受限recognition实例，现阶段不需给每backend proxy加专用fusionrecipe。拟**仅报告**保artifact/recognition分账，不授通用语音质量或无退步。

### 2602.20971v1 — Robust generalization and Lipschitz laws

2+1+3=6；拟**中心争议暂缓**，实际影响理论general-class loss界而定点深入，不改分/EX。§3 triangle+Cauchy得robust train R≤(sqrt(E)+Lρ)^2有效；但紧接仅写Y∈[-1,1]与f L-Lipschitz，便以|f(x)−y|≤2推loss≤(2+Lρ)^2并用于uniform Rademacher gap Eq10–12，缺f输出界。常数f=100、y=0同样L-Lip直接不满足该推步；这是自己的明确反例，不是作者实验。§8另明确定义B_L={f:X→[-1,1], L-Lip}，其local envelope/平方loss contraction受限命题有意义，但不能静默将后段条件补到前general class或签全部新lowerbound。仅保相关局部数学与报告经验，不授正面general理论证据/Books。§9 MNIST d10为假设、n1k–10k/width2–768/100grid、tanh logits/Adam CE lr.001 b128/10epoch no-improvement早停；empirical slope只是真实globalLip下界，O(n²)，zero saturated点被drop、R².308，§10作者承认CE与理论squareloss不同；不以该拟合认证理论普遍率。hardware/precision/seed重复ND。重开限定§3 loss范围/Eq10–12与§8关系，需作者明确f输出限制/一致定理或精确勘误；不自行补|f|≤1，不遍历全proof。ActualCh4 41–55区分泛化/优化足以防误采用，但不借成熟原则授中心理论安全。

### 2602.21020v1 — Multi-agent imitation and exploitability

2+1+3=6标准理论。§3 product-policy Markovgame、r∈[-1,1]/γ<1/Nash expert与BCerror population；§4 fullsupport+exactstate-action可恢复equilibrium，state-only即使fullsupport仍可反例；expert未访问区允许deviation时exactoccupancy也可Ω(1/(1−γ))，此例是adapted prior而非全新普遍failure。§6新增best-response δ-continuity；rare-state chain让很小BCerror仍BR变化2，DSE使δ0、Lemma3 NashGap≤2n εBC/(1−γ)²，主步骤add/subtract expert value+两次performance-difference与product-policy；Lemma4加δ(εBC)，只有δ(0)=0且δ tractable才能给consistent/tractable标准。游戏entropy regularization的数值支持不估计任意现实LLM δ；PPAD结果不用于所有系统不可学习，无需全复杂性附录。理论hardware不适用，无生产runtime/permission guarantee。ActualCh29 214–221 teacher错误/selection与Ch82 62–74任务依赖拓扑并未签战略equilibrium；该有界已知payoff/game δ criterion当前没有可采用的语言Agent best-response model，不需把具体Nash公式加到通用handoff论证。拟**仅报告**保新的strategic metric/continuity区别与正面有限充分条件，不按经典game或无foundation标签排除，不宣称全部协作不能泛化。

## B25 — 20670 / 20672 / 20680 / 20685 / 20687，作者必要命题审阅待root非作者核

五项精确v1合法HTML已取V3_FETCH_b25，必要源method/control/直接限制及actualowner已读。原50安全/98普通不变，B12～25共93作者必要包待独复，5尚作者必要读。[机械实际原证](V3_B25_CORE_OWNER_PACKET.md)，无新Books lease/写入。20680原结果必须看CORE/Table1，不拿PARA吞未转义<后的错误投影制造75%冲突。

### 2602.20670v1 — CAMEL confidence-gated reflection

2+2+2=6标准。§3 Eq5 abslogodds(A/B)仅单token margin难度proxy；低τ选reflection/highconf直接firstverdict，非校准truth。GRPO只对J/finalverdict计credit，initialverdict仅context，每pair强制A和B两种prefix使模型不只echo；GTpreference reward非真实效用/过程因果。§4 Qwen3-14B SFT+oneepochGRPO/Skywork80k+code/math数据，三benchmark，no-augmentation baseline双rollout控制；reflection各分支提高有限accuracy但加token。Always-reflection92.8/84.2/71.6（均约82.9）与gated92.4/81.9/69.1（均约81.1）分开，不将headline82.9给默认τ5gate；reflection有right→wrong变化，net正非每case正确。τ改变质量/生成token数不证明strict全walltimePareto，混checkpoint/leaderboardbaseline也非同训练预算。硬件/精度/batch/seedCI/SLO ND，训练sampling/重复prefix/reflection代价另计。ActualCh80 45–56同源feedback独立性、199–214stopping/budget已有；这里counterfactualverdict训练是特定RMloss的有限增量，不需以该head专用recipe重构当前reflection论证。拟**仅报告**保credit/context分离与质量成本边界，不授部署判断正确性。

### 2602.20672v1 — BBQ numeric condition interface

2+1+2=5标准。§3 structuredcaption内numericbox/RGB→FIBO8B25M继续flowtrain，不改生成architecture/loss；groundedSAM2/DepthAnything/Pylette自动annotations非humanGT；80k/b512/1024²/AdamW再3000aesthetic+DPO是组合训练预算。Qwen3VL4B bridge另3Btoken/8H100，dragbox可改变hugging等semantic关系，不能把只改JSON当所有scene不变。§4 TaBR60images成对偏好，decisiveoutcomes WilsonCI不涵盖ties；COCOYOLO/LVISViTDet boxproxy、200white-background单物体color选K5/8且最接近targetcluster，亮度/阴影/少量色块外推受限。InstanceDiffusion spatial仍更好、不同generationmodel/data预算不可纯归因numericformat；generator硬件/precision/inferencebatch/seedrepeat/SLO ND。ActualCh24 16–32条件分布接口已有，但该有界25Mnumericcontrol实例未建立新通用操作约束，当前不需要为每structuredcaption格式建立rendererrecipe。拟**仅报告**保实际numeric可读增量与bridge/GT/编辑语义边界，不称deterministic精确render。

### 2602.20680v1 — Vanishing Watermarks

2+2+2=6安全signal深入method/metric/主表，拟**中心争议暂缓**，不降分排除。§3 unguidedSD1.5再生与guideddecoder可访问/固定nulltargetMSE，§4 500COCO/512²/randompayload/30%noise/λ.5单gradstep，不是无decoder访问的统一攻击；PSNR/SSIM/LPIPS不证语义全部不变。决定性§4明确StegaStamp平均56bitaccuracy，TrustMark/VINE为ECC整payloadsuccess；Table1regen7.4/12.8/24.5%、guided0/0/1.6%，§5又称7.4/12.8平均payloadbits且chance-level、guided没有任何correctbit、VINE ECC留下couplebits，指标对象/ECC处理混淆，不足支持nearzero恢复强结论。PARA把<25%～>75%吃成75是机械投影错误，已用CORE727–812恢复，不列成原文矛盾。Null全零target与random原payload的bitaccuracy关系亦未解释，不自修为message-level或自行补50%baseline。Theoryidealmanifold解释不修经验metric身份；hardware/precision/steps/batch/CI ND，evaluationcode将来释放。只保作者有限reported结果/威胁signal，不授正面Evidence/Books或通用水印无效；重开限定§3target/§4metric/Table1/§5，需要作者一致bit/wholepayload/ECC成功定义与对应输出或勘误，非遍历全部proof。

### 2602.20685v1 — RAYNOVA

2+2+2=6标准。§3 nextscale×time-prefix/allviews模型，relativePlückerray仍用camera intrinsics/extrinsics与frame，geometry-free非不需几何或physics真值；globalmaskedselfattention/calibratedray/optional3Dbox/map。Recurrenttrain缓存preKV latent使KVprojection留在计算图、长序列末累grad；groundtruthscale tokens加错模拟historyshift，非exactstate充分或无限horizon。§4 nuScenes5h6cam/nuPlan55h8cam/130M与2B变体/32A100，3stage192×336→384×672→longtrain；Table7 allscalepast易copy/samescalepast不稳，relativevsabsolute/none与recurrentFVD100→91支持有限接口选择。VAD对生成视频action接近real仅plannerproxy、不是真实安全physics；novelview1/2/4m的FID/FVD不验证同pose真图，fullthroughput1.96images/s未同硬件/precision/batch/SLO匹配/seedCI ND。ActualCh24 48–58 ownhistory漂移/扰动decoder接口和97–99历史codec/anchor/cost已具体承载；拟**已有覆盖 MULTIMODAL-GENERATIVE-PARADIGMS**，dualaxis mask与preKV训练缓存作为受限实例，不授可删除任意历史或世界状态真值。

### 2602.20687v1 — NativeEmbodied

2+1+2=5标准。§3–4 AI2THOR1085samples/15VLM，连续参数basicmoves不等实机完整nativecontroller；perceptiontriplet、alignment移除movement/targetvisible、navigation远起点但targetvisible、planning直接navigation接口是不同输入/动作机会，不能称纯模型内部skill因果。GTsegtext/LookAt/teleport/预拆任务干预改变权限/成功路径，Claude3.5Sonnet单model结论不等全部VLM因果；GTperception不显著提高不证所有perception已充分。Sample5rollout allpass/allfail人工难度/feasibility过滤改变人口；640×480/90°/T0/history20turn与step15/20/30，thinking在alignment/navigation退步，runtime/hardware/precision/重复CI/真实碰撞SLO ND。ActualCh26 14–27 perceptionproposal/controller闭环、schema/单位/frame、deadline与独立物理风险已有；拟**已有覆盖 MULTIMODAL-EMBODIED-VLA**，局部benchmark分解/特权干预和低/高task差保Report，不授humanlevel或安全控制。

## B24 — 20450 / 20981 / 21078 / 21092 / 20673 / 21039，作者必要命题审阅待root非作者核

已校准一次准入原核心复用；21039精确v1 HTML新取得，其余既有合法v1正文有效。只核采用机制、对照/条件和直接反侧，不全proof/附录。原50安全/98普通不变；B12～24共88作者必要包待独复，10尚作者必要读。[机械原段/control/actual owner](V3_B24_CORE_OWNER_PACKET.md)，无新Books lease/写入/自签验收。

### 2602.20450v1 — Terraform

2+1+2=5标准。§5–6/Alg1 final-layer weights+bias更新排序，client数据量累计IQR内最小intra-splitvariance，easy/hard层次拆分及hard retrain直到η/T，next round重新随机初采样；更新只是异质性proxy。§7两FL算法/四分类数据、Dirichlet、三run均值/A100、2localepoch/b64或FEMNIST5/b32；仅5初样本退为一轮Random、15某场景仍第二、Q3–1重高异质者退步是实际选择边界。47%还绑定更大初样本人口/预算，不授零通信/重训費、全部隐私，GPU数量/精度/runCI/生产SLO ND。ActualCh36 76–83 local参数点/optimizer与共识分责已在；该client-selection统计策略不提供当前LLM runtime新同步/恢复contract。拟**仅报告**保IQR/初采样失败条件，不因小模型或无owner排除。

### 2602.20981v1 — MMHNet

2+2+2=6标准。§4.4 temporal mask高sim保变化、MM相反保sim≥.5对齐；compressedhierarchy/replicateupsampling非无损。§5/Table4 hierarchy DeSync .438 vs .669，A6 temporal .474 vs no-route .621但IB33.82<35.00，双route.439/36.82，Table5 .7明显退步。VGGSound8s+textaudio训练，UnAV100 official/LongVale从train-split重选长片加入评价（约1k/均45s）；chunkFD/IS/IB/4.8sDeSync非整sequence听感/真值。AdamW1e-4/200k/25step，H10080GB500s→60s vsMMAudio120s仅作者该timing；trainGPU/batch/precision/runCI/SLO ND。不采用noncausal保全部长状态保证。ActualCh23 890–896多时间尺度/层次成本及1032–1036 AV冗余/互补保留/时间合并、同步误删回退实际承载。拟**已有覆盖 MULTIMODAL-REPRESENTATION**，相反sim操作和指标取舍保Report，不造一paper新段。

### 2602.21078v1 — ProxyFL

2+1+2=5标准。§5 server classifier-weight proxy对比tune；低conf ξ取预测global classprior，positive为ξ内weightedproxy、negative须ξ无交集，非真实标签。§6四数据10/20%label/Dirichlet.1/.5/1，20clients每round8/ResNet8/5localepoch/τ.95/server10或100tuneepoch；Table4单label直接纳入SVHN退步，ξrecall更高仍非GT，Top1/5及组件对照限此人口。Globaltune/pool/通信仍付费，.4GFLOPs不签总walltime忽略；parameter没有privacyconcern未成立，hardware/precision/seedCI ND，不采用附录普遍收敛。ActualCh27 318–324删除监督与修复监督、保留输入支持与独立验证已在；ξ/nonoverlap是该classifier的有界损失接口，不需重构当前LLM示范与训练长期论证。拟**仅报告**保支持域/标签错误取舍，不按prototype名词或authority变化排除表示价值。

### 2602.21092v1 — Attention geometry / bottleneck diagnosis

2+1+2=5标准，只采用§4.1 local三层graphattention受控barbell，不采用分子领域结果或globalLLM归因。256重复topology/随机sourcefeature、26test，true/dummy bridge同topology、edgefeature真/置换同分布；layer2可区分任务相关bridge，最大MA却在abundantcliqueedge，不对应曲率瓶颈。Activationvariance非实际干预因果，MSE约.2–.3非无损传输，固定3hop/source/target不授所有sink机制，hardware/precision/batch/runCI ND。ActualCh5 253–266相关→可读→干预→行为/跨域阶梯实际承载读数≠forward依赖；拟**已有覆盖 WORLDVIEW-REPRESENTATION**，受控operator反证只Report，不以关键词扩池。

### 2602.20673v1 — GA-Drive

2+1+2=5标准。§3.3–3.4首knownimage+geometrypseudo-views concatnoise，prevsegment final生成帧作next anchor；训练首帧GT推理generated，有historyshift。Blur/localblend/randommask/depthjumpmask使单轨迹conditioncorruption可训练，非真实多轨迹/相机geometry。§4 Waymoval同ReconDreamer人口、40frame×.1m路移NTA/NTL-IoU/FID为识别/appearanceproxy，部分对照仅官网例；80%primitive删/±.2m只有限误差控制。CogVideoX/T16/640×960/Waymo+700OpenDV，preprocess3s/frame/A100，训练/采样batch/precision/runCI/安全SLO ND；rolling-shutter仍几何误差、仅appearanceedit，geometryeditfuture，不授全部simgap消失/physics真值。ActualCh24 48–58真实history→ownprediction条件漂移/历史扰动训练及decoder接口配对已承载；拟**已有覆盖 MULTIMODAL-GENERATIVE-PARADIGMS**，segmentanchor/corruption作为有界实例保Report。

### 2602.21039v1 — Multi-distribution learning under bounded label noise

2+1+3=6标准理论条件/主步骤。§1 binary有限VC类、共同Bayes f*与已知ηi<1/2上界/personalized输出；knownbound、unknownmaxBayes、individualoptimalBayes是三benchmark。§3 uniform-active-mixture ERM控制averageexcess→至少半数好，但身份未知，须各分布独立test后去除；d≪1/ε分开学习更便宜、unknownη*需猜测额外预算。§4 fixedRCNη=1/4，SHT O(log1/δ·min{ε^-2,d/ε})分别absoluteerror估计或先学proxy再独立excess-test；absoluteerror慢集中不与offset快集中互换。主lower步骤shatteredset/hidden稀疏subset保持noise，边界必要；仅采用学习/验证费用不同的条件机制，不签未核完整Massart exponent/生产最优。理论hardware/precision等N/A，ERMoracle与独立label取样计費；真实LLM不自带共同f*/knownnoise。ActualCh4 41–47容量/优化/泛化分责与Ch27人口/validation现论证无需该finitebinary完整recipe重构。拟**仅报告**保测试精度的正面有限解释，非以理论/无owner排除。

## B23 — 20294 / 20650 / 20652 / 20731 / 20758 / 21160，作者必要命题审阅待root非作者核

六项精确v1正文均成功取得（V3_FETCH_b23）；日期完全落窗原证复用。原50安全/98普通不变，B12～23共82作者必要包待独复，16尚待作者必要审阅。机械原证、actual owner与20731两段拟PRE见[V3_B23_CORE_OWNER_PACKET.md](./V3_B23_CORE_OWNER_PACKET.md)。未授锁/写入或独立通过。

### 2602.20294v1 — InterviewSim

拟2+1+2=5，标准，拟已有覆盖 PLATFORM-EVALUATION-SYSTEM。§2–4用历史80%/test20%的真实访谈Q/A、GPT4.1 generation及GPT4o judge，将content similarity、BigFive ordinal alignment、test-derived fact-summary contradiction及固定context MCQ分开。具体受限取舍：top100 semantic retrieval更style/content，chrono100～1000更低contradiction，但context size/组织同时变化，MCQ根本不用于dynamic retrieval，不能归因纯temporal order或称retrieval知识保存更差。相同k100 random control支持所测relevance choice，100person extensive-data子集扩1000person后contradiction升25～38%，保coverage人口而非泛总体。五次trait mode不替human人格真值、LLM整理与judge同源偏差；相邻采访主题重叠、英文Western public interview/2015～24、身份原数据不release、human验规模缺失。API token/检索/embedding与长context预算计费；硬件precision延迟/SLO/CI ND。Actual Ch66 309–314保judge competence/directional bias分开、人工anchor与marginal非每个model覆盖，现Ch66风险切片/不同质量维度分责已承载该采用判断；具体retrieval/chrono结果留Report，不由人格proxy新写通用RAGrecipe。

### 2602.20650v1 — Dataset Color Quantization

拟2+1+2=5，标准，拟仅报告。§3训练时保所有图像但压颜色，不同于先丢样本；shallow ResNet feature分20cluster、每cluster共享palette，GradCAM++选top区域LAB palette、STE/Sobel edge优化，重建train图并用原test图评价。§4 cluster1或perimage均退、shallow比label/raw/final/random更好，2bit局部accuracy与1bit大压缩仍有质量损失；按q/24的理想pixel比率不含palette/index/header/codec与decode，保样本N训练不等pruning同算力/同bytes，teacher训练/attention与优化费用不能忽略。CIFAR40ksteps/b256、Tiny60epochs/b128、ImageNetResNet34 300ksteps/b256；设备precision/完整storage吞吐/CI ND，不外推foundation multimodal质量。attention热图不是所有high-impact color因果证明，encoder/teacher漂移仍需回归。Actual Ch27 353–355分开format/语义保真/固定recipe任务效用，Ch23 139–145保codec量化进入训练分布/版本治理；这一特定palette实现暂不需重构现有表示/数据长期链，保训练导向压缩增量而非仅将其看成存储headline。

### 2602.20652v1 — DANCE

拟2+1+3=6，标准，拟已有覆盖 PLATFORM-EVALUATION-SYSTEM。§3以RFM task-adapted CLIP embedding的rank-neighbor label set和density-contrastive loss两个nonconformity score相交；error-budget alpha_knn+alpha_clr分担，用union bound仅签满足exchangeability/valid split的marginal coverage，不是class-conditional保证。rank更紧但依distance/noisy远邻，density保罕见类但set大。§4主实验calibration作为reference且LOO，只经验coverage，不继承原disjoint theorem；lambda tuning又复用calibration。11datasets仅available testset切40fit/40cal/20test、CLIPViTB16/ResNet101、25Bayesian fit trials、lambda grid .1、m100/50，RTX4090/i914900KF/64GB；alpha .1时RFM-RAPS size2.21比DANCE2.49更小，DANCE只是效率/CCV取舍，不全SOTA。kernel fit差、稀少calibration、tuning/邻居search及refartifact成本；precision/seeds/CI ND。Actual Ch66 140–156的model/calibration双artifact与exchangeability、accuracy/coverage分责及309–314marginal限制已直接承载；双score具体实例不另添recipe，也不外推开放generation。

### 2602.20731v1 — COMiT

拟2+2+2=6，具体owner差额深入；拟整合 PRE，未写/lease。§3 fixed L-token state经local crop＋relativeoffset recurrentupdate/FSQ，randomized K及只finalupdate回传，单model分image/message AdaLN；finalmessage条件flow decoder，DINOv2 CLS SREPA与spatialREPA为额外teachers，不是每crop加token。§4训练localcrop即使测试globalonly也改善probe，SREPA与localcrops消融分别核；2layer attentionprobe非线性/纯encoder固有能力，unseenpair COCO/VG仅有限readout。goldmask按最佳token IoU选择/0.53vs0.34不是部署对象定位，也不内部causal。B→L改善两目标、L→XL重构升而semantics降；globalonly成本最低，多crop仅部分任务小增益，adaptive每crop decode非免费。32GH200/200epochs/ImageNet256、b512、Adam3e-4/sqrtdecay/EMA.999；precision/seed/CI/实际E2Edeadline ND。Actual Ch23完整137–149当前一次codec/codes治理→semantic quantizer；尚缺“固定message反复观察重新分配而非新增token”与crop-count/梯度时钟分支，所拟两窄段接141后/143前，并保旧一次codec、独立encoder/decoder与latentUM原source归属。只有root PRE+窄锁后才写，写后完整邻接独复，不靠marker。

### 2602.20758v1 — unfolded MCMC kernels

拟2+1+2=5，标准，拟已有覆盖 MULTIMODAL-GENERATIVE-PARADIGMS。§3把finite-L transition kernel/unfolded trainable step/prior当conditionalgenerator，各burn-in后dependent layer sample接受随机layer conditional WGAN-GP，samplemean L1＋SDregularizer压modecollapse，但error超阈值关闭SD；§4.1 k已知likelihood直接输入，不是未知operator泛化保证，MNIST随机blur Matérn k训练族、8～64步骤＋posterior samples。10k test/512samples估计mean，VAE-SGS零shot prior与10ktransitions、RCGAN generator输入y不显式k，因此收益不能纯归因unfolding同预算；W2latent与VAEprior同encoder偏差公开，minibatchWasserstein有bias/GP只promote1Lipschitz，不签exactposterior/equilibrium/独立样本。A40 48GB/EPYC7543，L增训练/推理费，precision/seed/CI/E2E ND；galaxy/radio astronomy域结果不作为项目新增。Actual Ch24 157–159将likelihood/noiselaw/posteriorlearner分验、参数族/有限MC/integrationerror与旧sampler回退已具体承载；这份finite trained chain是受限实例，无新长期recipe。

### 2602.21160v1 — per-class epistemic vector

拟2+1+3=6，标准，拟仅报告。§2用posterior/MCdropout/ensemble probability samples，entropy Hessian diagonal给Ck=Var(pk)/(2muk)，sum仅二阶近似MI；mean近0归一化抵消rawvariance压缩，但thirdmoment/mu²也放大，rho仅告警不校正或保证，symmetric高阶误差不能由rho小自动排除。covariance反相关辅助cue/CBEC额外safe/critical partition知识，不授trueepistemic/风险语义或calibration。§5采用FashionMNIST/CIFAR10 label-noise控制：S50低rank endtoend vsfrozenbackbone/head，CIFAR100 inflation1.17/1.89；posterior质量/训练目标同时影响排序、transfer下MI可优，不能签所有backbone冻结皆因果失效。主文medical领域风险收益不纳为本项目新增，未深入该域recipe；所采用机制只通用多类uncertainty decomposition/近似有效条件与小型视觉反侧。重复stochasticpasses/uncertaintytraining与必要held-out校准均计费，硬件/precision/同预算等价/CI在采用核心ND。Actual Ch66 calibrated score/marginal与任务slice不同层次，Ch5 proxy与真值阶梯已有；这一近似读出公式暂不需要重构当前owner论证，保正面有限解释，不以无authority变化或小实验为唯一Only理由。

## B22 — 20370 / 20517 / 20567 / 20624 / 20585 / 20646，作者必要命题审阅待root非作者核

六项均复用当前精确v1准入与完全落窗日期原证；原148确认子集/50独复安全/98普通不变。B12～22共76作者必要包已备，22尚待作者必要审阅；本批未授非作者通过、Books写入或终态。机械核心与实际owner见[V3_B22_CORE_OWNER_PACKET.md](./V3_B22_CORE_OWNER_PACKET.md)。

### 2602.20370v1 — Quantitative Approximation Rates for Group Equivariant Learning

拟2+1+3=6，标准；拟仅报告。原来“普遍逼近”不区分参数效率，新增有限Hölder/固定n,d的equivariant/invariant逼近构造，值得区分表达效率与实际优化/数据收益。采用范围为§3.1 Cor3.1的有限不变函数类比较及§3.3的self feature＋omit-one sum构造：恒query/key产生均匀平均，value乘n、residual中的负self恢复其余元素和。必要源读§3.1 theorem假设、网格/shift/编码/bit extraction主要步骤以及§3.3构造；不授固定精度可执行的生产recipe、位置编码/因果LLM等价、实际sample/optimization改进。bit encoding/巨大权重与维度、层深/参数依赖非免费，论文为理论无硬件吞吐实验，Not Applicable；theorem中FC1/FC2标签与proof的Phi/rho顺序不照抄实现。Actual Ch4 41–47/342–348已把capacity/optimization/generalization及表达效率分开；此固定集合构造给出受限解释，目前不需重构该长期论证，不因“理论”一律不入书。

### 2602.20517v1 — MIMIC inner speech

拟2+2+2=6，标准；拟已有覆盖 MULTIMODAL-EMBODIED-VLA。§3.2由每8GIF的VLM描述经CLIP为CVAE targets，CVAE历史window采样/周期更新，diffusion policy独立训练并消费latent；initial文字可覆盖零条件，随后周期回到模型生成。采用语言/历史作为mode conditioning与更新时钟，不采human内在思维、非Markov任意行为保真或生物对应理论。§4同DDPM-T policy、random/KMeans/MPNET/VLM反侧：o4-mini entropy高却success低；Qwen未总提高entropy；训练description/no update与validation/periodic优胜不同。D3IL模拟与Overcooked100局proxy human不是实际人类合作普效，GPT4ojudge非真实intent；hyperparameter search、VLM/CLIP/CVAE与每H/W调用计费，A6称主项同阶就no overhead不采零成本。precision/硬件/seed/CI未在采用核心披露，Not Disclosed，不外推完整deadline。Actual Ch26 139–143已具体承载命令抽象/更新时钟与latent action consumer、文字readback不faithfulness及完整控制费用，新增description→latent具体实例留Report，无新Book recipe。

### 2602.20567v1 — Push-Sum stability / generalization

拟2+1+3=6，必要理论核心深入；拟中心争议隔离，非作者待核。§3同column-stochastic primitive P、u与w双流程、z=w/u，delta=min stationary pi；§4逐样本G-Lipschitz/L-smooth/有界参数域、convex或PL，输出为加权平均迭代，不授任意最后checkpoint/LLM。决定性B.2 Eq41明确lambda为H的spectral radius却直接||H^t||<=C_H lambda^t，未给Jordan/非正规矩阵的适用条件；Eq52把除min_{k<=t}lambda^k吸进C'，该量随t变化，不能默作统一时间常数签后续显式δ×spectral-gap rates。不自行换更大lambda、加diagonalizable假设或修常数。有限Logistic a9a 32k/4～32 clients与LeNet CIFAR100clients/300iterations曲线保作者经验，不宣布算法无效；硬件/precision/重复CI ND。S6明确动态拓扑、compression/quantization/partial participation尚待扩展。Actual Ch36 79–87保local drift/模型估计/mixing条件与同步回退，但中心新稳定/泛化率不能拿成熟共识原则绕过，暂不正面Books。重开只需原作者明确Eq41适用条件与Eq52统一常数/相应修正，不遍历无关proof。

### 2602.20624v1 — cross-modal bias diagnostics

拟2+1+2=5，标准；拟仅报告。§2 CREMA-D全部7442/91actors，intended vs multimodal/visual/audio perceived标签不同，zero-shot Qwen2.5Omni/Gemma3n对音频silence/画面blank与禁选1～4labels的prompt；采用失败图/禁选后fallback hierarchy与AV更像V-only的限定诊断，不采模型实际attention因果或社会公平的普遍判定。§3 oscillator WattsStrogatz p=.01/k10、Lorenz与ridge另一个surrogate系统，beta tuning不是两MLLM内部intervention，不能以其SHAP/attractor授原模型真实机制。§4承认控制/完整解释未决；图抑制低频edge、自环删去、blank/silence和label prompt本身改输入任务，平均准确不等失败结构，但未控制全部表示/训练混杂。硬件/precision/seed/置信区间未披露，Not Disclosed；注释层/模型版本范围不授生产公平保证。Actual Ch23 154–157分开representation formation/readout/routing及necessary与sufficient，这个emotion输出诊断未提供新可执行融合recipe或解除内部归因限制，保局部负证而不重构长期正文。

### 2602.20585v1 — generalized smooth distribution constraints

拟2+1+3=6，标准；拟仅报告。原iid/adversarial二分之外，Definition4引入所有μ∈U满足μ(A)<=rho(mu0(A))且rho(epsilon)→0的uniform continuity；§3.1将mu0下VC cover经rho^{-1}转为所有U的cover。采用该具体支持域条件与“known U＋oblivious adversary可Hedge cover、unknown/adaptive不能由cover单独推出”的边界；不是只有限VC就适合任意数据流，也不采用private LLM、regression/multiclass/非full-information保证。已核§2 binary/0-1/full-information protocol、§3必要性disjoint-mass threshold构造/有限cover→mixture的主要论证、Theorem3及§3.1反侧；不自签全iff/privacy/algorithm proof，§3 p11.2尾部intersection/tail notation不照录为闭合必要性证明。有限cover可巨大且oracle/ERM可不可计算，理论无硬件或端到端性能实验，Not Applicable。Actual Ch4 41–47已按capacity/优化/真实风险分责；这项分布族的特定可学习条件尚不提供当前foundation训练可验证U/rho或新runtime recipe，不需重构正文，保正面数学解释，不以理论/无硬件为排除依据。

### 2602.20646v1 — perturbed forward / backward SGD

拟2+1+3=6，标准；拟已有覆盖 TRAIN-PRETRAINING。采用§3 operators bounded Jacobian/derivative Lipschitz on visited compact region与§4单步propagation/conditional bias decomposition；forward期望0仍有fourth-moment曲率项，不能把两类噪声都并成optimizer入口的无偏additive noise。已核Lemma1 Jacobian product、Lemma2 Taylor主步骤/Theorem2 Eq23与§7控制实验直接反侧，不签全部rates或真实LLM spike根因。§7 d10/M2000/T200000 logistic、convex/nonconvex regularizer与受控注入；forward sigma_f>=.5缩步长仍plateau，zero-mean backward局部更benign，不授任何backward错误无害，means是conditional不是仅总体零均值。较高层数最坏界/四阶矩、扰动发生时钟、完整reference与trace均计成本；硬件/precision/seed/CI ND，理论不能认证数值guard生产恢复。Actual Ch28 1315–1325将Update/Numerical分别验、有限数值不等高精度reference、同step异常按batch/rank/route关联，已具体承载拟采用的“计算错误不能因有限/平均归零而跳过轨迹验证”；forward/backward曲率分解留报告，不为每个有限理论实例单建recipe。

## B21 — 20422 / 20424 / 20426 / 20457 / 20461 / 20520，作者必要命题审阅待root非作者核

六项2252词mechanical必要原段/公式、关键对照/反侧与actual owner见[V3_B21_CORE_OWNER_PACKET.md](V3_B21_CORE_OWNER_PACKET.md)。拟4Existing/1Only/1中心Disputed，没有Books新写/lease或独复通过；B12–21共70准备待独复仍在原98普通内，28尚待作者必要审阅。日期同ID原字段/officialcutoff下界09BJT到Registered秒ceil，六上界10:49:45/10:49:48/10:49:51/10:50:35/10:50:40/10:52:06，完全落02/25 09～02/26 09窗。当前安全账50不变，不把作者读完当验收。

### 2602.20422v1 — mechanism-modulated diffusion plans

2+1+2=5标准，§4先从offline pool回归transition/reward，再对单步denoised trajectory estimate加transition MSE/negative predicted return与真实训练trajectory累计reward归一的noise-loss weighting；deployment固定s0为当前观测，每reverse step加两proxy梯度。这里采用“生成plan的学习代理与环境检验分开”，不采用Prop1给full multistep reverse output精确Gaussian分布的主张，也不从isotropic covariance推所有旧Diffuser无法表dynamics。Self-consistency低可能来自共同错模型，reward proxy非真实action outcome。D4RL三个locomotion/三人口与Maze2D，5seed；horizon100/128/265/384、100diffusion步、guide .001/λrd .05/λtr .1，large-maze HD-DA更好、权重偏离最优质量退。训练model/gradient费用与100步不能称免费，hardware/precision/fullE2E预算/CI未披露。Actual Ch25 90已有生成后继的auxiliary action proxy非物理truth与闭环验收，122–124保learned/explicit simulator共存；拟**已有覆盖 MULTIMODAL-WORLD-MODELS**，限定joint-plan regularization实例与large-maze反侧，不授任意foundation/world planning guarantees。

### 2602.20424v1 — implicit requirements under simulated worlds

2+1+3=6，privacy/irreversible action风险深入；§3四类discoverable constraint、§4 YAML/world/evaluator分责、§5difficultygate/§6/7及A1.4必要一致性反侧。隐藏execution rules只能在环境查询中发现，user没有写明不代表自动授权扩scope；所有rubric交集与partial score不同。205scenarios由作者＋两expert达共识，迭代修改到模型fail，再要求至少1fail≤70%与1pass100%、全pass丢弃，48.3%不是随机真实请求成功率或human水平。World Opus4.5只执行predefinedreturns但LLM并非已证明deterministic engine：主§7.2报告98.6%，A1.4实际55scenario/275run/172action的exact-match93.3%，指标身份冲突不合并、不授zero模拟bias。单回合user不可clarify、max50actions、GPT5.2-highjudge，抽样humanagreement只声称high未足够数值/CI；作者文化/年龄/IOS版本与303nativeactions范围限制。真实动作成本、安全事故率/hardware/precision未披露。Actual Ch66 63–76已有runtime/contract/quality/policy/outcome交集、不同证据身份和严重失败gate，拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**。只保有限隐含约束评价blindspot，模拟state不授实际user intention或执行许可。

### 2602.20426v1 — trace-rich teaching for trace-free tool metadata

2+2+2=6标准，§3原schema固定、D0→D1general→D2failuretrace rules，删除trace输入但保D2target；先较多trace-rich再trace-free，学习的是跨tool metadata生成，不是在deploy取得隐藏trace。训练healthyprovider筛9640→1234→107、排评测tools，inferenceunseen工具与query；dependency-aware multistep data仍由可执行示例/teacher来，不能说完全trace-free全生命周期。核心§4评测每step调用GT API teacher-force正确prefix，再验tool selection/API成功；“QL全step成功”仍该conditional人口，不等自由rollout E2E或真实业务success。Fixed count两epoch的10%→90% trace-free两stage最好、三stage退步；tool-level API不是最佳、不同tool equalweight缩收益，limited100candidates同类别抽样不授开放catalog。Qwen3-4B-Instruct2507、8A10080GB、FSDP/verl/vLLM、temp.3/topP.9/repetition1.1，precision/全trace生成费/多seedCI未披露。Actual Ch78 57–63已具体拥有actualentry/blackboxtrace依赖→versionedmetadata、traininggold不可部署继承和真实工具独立回归；拟**已有覆盖 AGENT-TOOL-CALLING**。Curriculum/teacherforcing具体实例留Report，不把描述质量签schema正确/权限或服务端诚实。

### 2602.20457v1 — pointwise oracle-robust SAIL objective

2+1+3=6标准，只采用§3 uncertainty/margin及§4.1 Theorem4.1的必要原式/四步分解。每pair conditional Bernoulli preference的uniformρ-ball中心是未知P*，marginδ且ρ<δ避免clipped endpoint；pair独立来自当前policy，known fixedψ/loglinearsoftmax、SFT reference同族。对label概率仿射loss取区间endpoint，额外ρ|ℓ1−ℓ0|＝ρβ|logratio gap|，得到nominal SAIL＋λ Epolicy|pairwise score|。Penalty本身依赖policy-induced sampling，非冻结数据的普通L1，不把理论unknowncenter直接作为部署可获得oracle；更非真实偏好moral truth。参数梯度/弱凸/Moreau stationarity需要其余assumptions1–7，该结果不采用，不为它遍历proof/附录；未提供LLMempirical validation、hardware/runtime、precision/benchmark不适用理论命题。Actual Ch31 578–584已有selector及synthetic margin不授truth/成立人口/费用边界，但并不含此formal minmax分解；这项限定理论当前不需重构实际RLHF objective分工，拟**仅报告 TRAIN-RLHF**，非因理论一概无长期价值，也不授neuralLLM普遍稳定性或收敛成本。

### 2602.20461v1 — AtteNT kernel bridge central hold

2+1+3=6，§4 Theorem3/4与A2.1决定性桥触发定点深入。Parameter update的一阶表示产生dynamic Jacobian-Gram kernel，是local Taylor/gradient-flow近似，finite宽/步长的remainder不消失。A2.SS1.p1.5先声称functional convex loss使output-gradient vector→0（参数非凸不自动如此），随后从g_tᵀ(K−Kθt)＝higher-order remainder推出所有训练点Kθt→chosen canonical K；即使先授g_t→0，乘积趋0也不能识别任意matrix/kernel差，少了独立excitation/conditioning条件。因此不采用“parameter ANN与nonparametric teaching consistent”的中心等价、canonical loss reduction签实际attention训练保证，不以有限10点NTK图补普遍证明。拟**中心争议暂缓 TRAIN-DATA**，保6分/候选，positive theory/Books隔离，重开需作者补一致极限/非退化条件及足够证明或更正，不扩其余附件。

有限empirics保留：LLM实际上per-example loss proxy，首epoch全池后70%子集/总5epochs，Llama2/Mistral/Gemma7B数学/代码/对话、4A10080GB/LoRA/FP32/b128/lr2e−5；ViT800epochs/AMP/b2048，20–80%adaptive loss selection，Mask2Former pseudo labels非depthgroundtruth。Hard/softGumbel/random与fixed70%预算对照是局部结果，80%ratio可质量退步。保author12.78% LLM平均节时不与abstract13.01%拼普遍数；score/selection/重训开销、所有训练tokens等价/多seedCI完整未披露。Actual Ch27 1081–1085已分gradient/optimizer/proxy与heldout，但不给此kernel理论背书，不借成熟selector另写正面段。

### 2602.20520v1 — region-matched inpainting/caption diagnostic

2+1+2=5标准，准入一次matched-region/late-layer与outer反侧已root通过；§2–4及A2 mask/A4config足以支持拟命题。冻结inpainting/caption/ViT，center/blur/lowdim同targetregion；CLS-to-patch TVD在重建region随depth增、outer较稳定，只是所选region/encoder受控观察，不把attention变化授语言因果或语义真值。SD1.5/2/3＋BLIP/LLaVA/QwenVL，SD3 strength.6区别旧1、50步CFG7.5；inpainting prompt直接用原annotation/boxcaptions/series text，不能当image-only感知独立贡献。SSIM弱且LOO可翻号、LPIPS/MSE相关较稳是少量configuration相关，不是逐image真值或通用metric保证。6beam兼topP.9/T.8、3captions48–64token，ND hardware/precision/全部运行费/seedCI；不外推其他preprocess/VQA/联合训练，不采用medicalscience领域结论。Actual Ch23 26–36拥有preprocess/content/coordinate/artifact身份，85明确encoder可读/fusionaccess/output分段诊断而非唯一归因；拟**已有覆盖 MULTIMODAL-REPRESENTATION**，有限视觉pipeline诊断留Report，无新长期recipe段。

## B20 — 20396 / 20419 / 20467 / 20549 / 20593 / 20629，作者必要命题审阅待root非作者核

六项2486词mechanical必要原段/公式、关键反侧与actual owner见[V3_B20_CORE_OWNER_PACKET.md](V3_B20_CORE_OWNER_PACKET.md)，拟4Existing、1Only、1中心Disputed，不改Books或计终态。B12–20共64项已备仍在98普通中，34项尚待作者必要审阅。日期复用同ID原Submitted与Registered、official cutoff lower，身份见V3_FROZEN_CANDIDATES.json：02/25 09:00BJT起，上界依次10:49:07、10:49:41、10:50:49、10:52:52、10:53:55、10:54:47，完全落窗；不把Submitted/Created/Updated自动当公开。精确v1 HTML，不读后版/revisiondiff。

### 2602.20396v1 — cc-Shapley causal context

2+1+3=6标准；§3 Definition3.1/Lemma3.2–3.4/Alg1与§3.3限制足以支持拟命题。普通observational context可通过collider打开原先无关联路径；替代方法仅对context S做随机do(S~q)，Xj仍是被观察变量，不把它偷换成do(Xj,S)后删除全部anti-causal信息。图上边缘d-separation的feature在该context intervention后仍0，统计独立对应图判断另需faithfulness。Alg1固定SCM/context marginal，拟合两conditional means；已知图/噪声结构和外生独立不是自动成立，所有context指数增长且每context两模型，未实现scale approximation。3000随机8变量linear/Laplace SCM与DirectLiNGAM仅有限理论/诊断实例；临床及protein science用途不采用，静态feature含义不直接迁移image/LLM representation。硬件/precision/端到端费用不披露，不授一般XAI causal truth。Actual Ch5 390–394 reference-conditional attribution、492因果生成条件与代理分责已有承载，拟**已有覆盖 WORLDVIEW-REPRESENTATION**；保do(context)这项受限反例与成本在Report，不因缺论文名字创建recipe。未采用Example2.1的Bernoulli interaction数值，不能由局部示例推普通Shapley全部失效。

### 2602.20419v1 — CREDIT certification central hold

2+1+3=6，所有权/安全认证中心主张触发深入；§3 MI噪声界/threshold及A2.3实际TypeI/II证明决定采用边界。Gaussian upper bound只约束protected输出与surrogate依赖，不自动区分independently trained与extracted模型。A2.SS3.p4.2以“By design”假定μ_ind<τ，之后还退到μ_ind≈0；p7.2另假定μ_sur>τ/p7.3固定正margin，未由模型训练来源/Q预算推出该两人口分离。其TypeI事件实际写 Î−μ_ind>τ，与前一步t=τ−μ_ind也不同，不自行改事件。p3.1声称每point只进入至多k个marginal neighbor sets以推出(2k+1)bounded differences；bounded embeddings不提供该一般KSG neighborhood入度界。拟**中心争议暂缓 PLATFORM-SECURITY**，原candidate/score保留，无positive certification/Books；重开需原作者一致threshold/error事件、有效population separation条件及适用KSG bounded-difference证明或明确更正，不要求无关全部proof。

有限empirical AUROC仍保author结果：CIFAR10/100四CNN与ENZYMES/PROTEINS四GNN，query train与verification test不重叠；distillation/Knockoff、Q5000/V1000/embedding1024，kneighbors3/5/7/10mean/std，RTX6000Ada/EPYC1TB。Word2Vec/STSb不是LLM，repeatedquery固定预算与有限decorrelationδ不授任意adaptive攻击保证。precision/独立重复CI/全成本未披露；计算threshold还需σ/协方差/MI调参与数据，不能沿preparation定义漏这些费。Actual Ch72 185–189已有forensics≠prevention、信号≠合法ownership与认证边界；不借成熟原则新增段掩盖中心未决。

### 2602.20467v1 — joint bias-compensated pruning

2+1+2=5标准，因具体公式不一致定点加深scalar Eq4–7与vector-output式；不遍历其余proof。保持原输出重构而非loss gradient，去掉一个权重时允许同时调本层bias；small weight/bias Taylor近似后联合最小化expected L2 discrepancy，明确vector formula用Σk E[(∂b yk)^2]为分母。**Scalar Eq7却用E[∂b y]^2，非Eq6驻点的一般E[(∂b y)^2]；后续scalar importance沿用它，不替原文补括号，不采用该scalar exact optimal recipe。** Vector expression给出独立可识别窄机制，但零分母/多weight同时删除/Taylor残差仍不提供全局最优或无损剪枝保证。MNIST两个FC/PReLU、15epoch先训＋15epoch恢复、Adam及5init分布，对照小dense宽度/random/magnitude/gradmag/bruteforce；PDE领域结果不作项目science新增。Bias能合并现有参数不等全部prep无费；Jacobian/calibration/恢复训练付费，稀疏率不证明kernel实际加速，hardware/precision/服务runtime/CI未披露。Actual Ch49 509–513拥有重构vs梯度目标与离线/执行分验、1040–1042拥有固定目标与可补偿自由度；拟**已有覆盖 INFER-TENSORRT-LLM**，只留vector条件机制及scalar冲突在Report，不授scalar配方或新增一论文段。root若认为vector不足以隔离中心，将按实际反馈保争议，不自签通过。

### 2602.20549v1 — DiME evidence estimation

2+1+3=6标准，§3 model-evidence path/conditional score、§3.1–3.2 covariance/two-draw estimator与§4.1/4.2必要反侧。模型选择需要normalized evidence，不等用reconstruction质量挑prior；two conditional iid posterior draws的Θ1ᵀΘ2避免直接||Θ||²附带traceCov偏差，这个unbiased身份只针对条件均值平方，不消除learned score/Gaussian posterior/finite Langevin/积分误差。高噪声σt² heuristic忽略prior covariance，可错mode；empirical covariance/transform-diagonal与jitter1e−2增加统计身份，不能由极限正确posterior授finite整条path正确。

Analytic1000D双Gaussian、A200×1000/σ.1，100anneal/20paths/50trialsmeanstd，DiME-PnPDM OOD bias更大，即使极限终点可正确；MNIST十prior phase retrieval的flip/translation使6/9不可唯一识别，不宣称true image唯一恢复。双draw＋Langevin与积分均付费，50或100时点不是端到端运行预算，硬件/precision/生产SLO未披露。Blackhole physical模型验证不纳当前science路线。Actual Ch24 157–159已有posterior learner/score/finite MC与solver分责，但未直接包含normalized evidence recipe；这项有界model-selection读数目前不需重构生成路径/learned composition长期链，拟**仅报告 MULTIMODAL-GENERATIVE-PARADIGMS**，理由不是理论/小实验一概无长期价值。作者明确可选错模型，不授部署选择truth或通用zero-bias保证。

### 2602.20593v1 — triggerless inference embedding substitution

2+2+2=6，安全失效路径深入；§3 threat/label inference/poison/online substitution、§4定义/人口及§5关键防御反侧。VFL passive party训练按协议而记录local embeddings/收到gradients，另持每class一labeled auxiliary例，可在inference选择source并替换送给topmodel的embedding；active结构/label未知。Cluster→targetcenter×η＋Gaussianvariation是恶意payload，“triggerless”只是不需训练植入trigger，非无恶意输入/无embedding写权限。main-task training accuracy不提供inference输入完整性；clean-label rASR/LISR与dirty-label mASR人口不混算。

MNIST/FashionFC、CIFAR/CINIC4conv、CriteoDeepFM，1active＋3/4passive仅1attacker，列/feature随机切；η太大/variance太大可降低ASR/更易detected。九defense对照另切two-party，L2norm在简单MNIST有缓解，不能宣称全部defense无效；S5.1增强attackerbottommodel改变成malicioustraining，不继承原honesttrain前提。跨party architecture/feature分布及traintest差异使norm anomaly缺统一界，真实inferenceintegrity defense仍未解决。hardware/precision/多seedCI/全protocolcost未披露。Actual Ch72 97–114逐lifecycle identity/integrity/authorization及2123–2125 activation/trust/split身份已承载采用的跨phase边界，拟**已有覆盖 PLATFORM-SECURITY**，具体攻击不添recipe，不把授权来源正常签为online tensor可信，也不授未经实验验证的通用防御。

### 2602.20629v1 — QEDBench judge/rubric calibration

2+1+3=6标准，§3交叉solver/judge/专家rubric、§4关键偏差/课程constraint对照、§5局部falseaccept与§6限制。272问题/48experts、5solver×7judge共享答案；human只用ExpertRubric，LLM用Expert/Course两套，不给course评分制造独立human truth。GPT5.2/Gemini draft经human迭代仍可能同源偏好；部分证明缺关键connectivity或假lemma仍获partialcredit，不由正确式子/流畅证明授verified。GPT5.2 r .69/MAE .13 vs .67/.14只该对照弱响应，非所有prompt无用或已识别内部prior override因果。

o3搜索214/272（88有online solution/126未找到），58未决/GraphTheory19排除审计；N1070 model-problem pooled检验p .32/.80不能证明无污染或全部independent observations。评分scale与≥.9 pass分账，3retry后default0/16,384output与模型budget使timeout失败另有identity，不把新模型headline当当前事实。StaticEnglishgroundtruth可能排有效另类proof；downstream reward poisoning仍future而非已测训练损害。完整hardware/precision/费用/独立CI未披露。Actual Ch66 124–126 label生成链/critic迁移、309–310 competence/bias/leniency与314人工anchor边界承载，拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，保具体判定blindspot而不另造benchmark段。

## B19 — 20427 / 20901 / 21188 / 21193 / 21196 / 21198 / 21202 / 21204，作者必要命题审阅待root非作者核

八项3153词必要原段/control/直接反侧与actual owner见[V3_B19_CORE_OWNER_PACKET.md](V3_B19_CORE_OWNER_PACKET.md)。拟6Existing、1Only、1窄纠错PRE，无授权或写入，不计终态。B12–19共58已备必要包仍在98普通中。日期复用V3_DATE_PACKET同IDRegistered秒精度ceil＋official cutoff lower：下界02/25 09:00BJT，上界20427 10:49:52、20901 11:01:20、21188 23:42:26、21193 23:42:39、21196 23:42:47、21198 23:42:52、21202 23:43:01、21204 23:43:06，完全落窗；Submitted不作公开时刻，未读后版或完整revisiondiff。

### 2602.20427v1 — GauS differentiable operator scheduling

2+1+2=5标准，准入一次核Groq/PIM目标与约束已有root通过；必要§3 Gaussian参数化/离散CDF/ALM/rounding、§4匹配搜索预算和A1必要legalization。每operator独立Gaussian以均值/方差替D个categorical参数，2|V|参数保时间邻近性；CDF单位区间概率对应rounding，memory LogSumExp是代理，预期dependency/resource/memory/modulo违反惩罚不是离散计划合法性。均值round后greedy修复/reinitialize；modulo fixed-point到节点数上限仍可能有recurrence violation/depth overflow，不替作者签任意feasible保证。A10080GB、所有搜索15min、单固定初始化/run，EPFL+随机图及人为backedge约束不是基础LLM实机；小图ILP可更优、RW5最终目标略差、独立Gaussian漏节点相关性。优化器GPU利用率与搜索速度不是模型执行速度，模型/hardware runtime/SLO不适用，重复seed/CI未披露。Actual Ch49 28–30已分计划搜索/接口约束与真正artifact验收，113–115保独立schedule语义/合法性；拟**已有覆盖 INFER-TENSORRT-LLM**，Gaussian有限搜索实例保Report，不按GPU搜索授生产收益或新领域operator全链。

### 2602.20901v1 — SpatiaLQA / recursive scene graph assistance

2+1+2=5标准；准入一次核同GPT4o rawdepth/seg退步与graph+CoT条件已通过。必要§3 step/content/precondition matching与judge敏感性、§4实际RSGAR对照；DepthAnythingV2/SAM+递归接触/空间graph每轮扩对象、T5后答。相同GPT4o下直接添加depth/segmentation甚至更差，CoT次优、RSGAR提升主要多step而少step略退；不能把输入信息和多次调用同时增加的全部收益唯一归因graph。GPT4o生成semantic matching矩阵再Hungarian一对一只是特定scorer，300抽样/四judge结果差不证明总体真值；唯一人类答题者不提供一般human人口能力界，step数与augmentation来源混杂，不宣称内部causal缺陷。递归perception/LLM调用成本需另计，完整端到端费用、硬件/precision/seedCI未披露。Actual Ch66 132–134已拥有生成器/结构难度/operand可读性/预算交叉分账，51–76区分semantic质量、contract与outcome；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**。该受限控制改变输入表达评价而非物理oracle，不为新benchmark题量改书。

### 2602.21188v1 — HVG temporal/view denoising

2+1+2=5标准，root一次两轴独立采样反侧已通过；必要§3 alignment/双轴窗口、§4评价与qualitative ablation、§5face限制。SVDxt UNet的pose骨椭球depth/normal与参考/camera条件，pelvis投影/crop先对齐2D视角attention；每denoising step分别对长时间/少视角和短时间/多视角重叠窗口去噪，再加权合并两个完整latent，不是先生成时间后补视角或真实3Dstate。Temporal-only裤色跨view变化、view-only跨frame logo消失是有限qualitative控制，不授全局coherence。32H100/576²、60k多view+50k多frame、受限扫描与5000视频；25video×8views不是200独立主体，face鼻/唇可失真。多seed/CI、matched双轴总计算和端到端runtime未披露。Actual Ch24 85–105已有生成history/window成本，1430–1432已把camera与motion/animation时钟分责，原路径无需为该有限人体双窗口recipe重构；拟**仅报告 MULTIMODAL-GENERATIVE-PARADIGMS**，保双轴反侧与机制证据，不因缺名字或不改authority否定其潜在价值。

### 2602.21193v1 — Nemotron-Terminal data engineering

2+2+2=6标准，§3–5数据对象、teacher/过滤与课程关键反侧。Adapter把既有math/code/SWE任务包到terminal接口（未都有test）；合成task包含instruction/input/pytest/Docker，9预建images与任务生成解耦，refs供tests不供Agent；可安装依赖不等供应链安全。DeepSeekV3.2教师与14gram/identity/Chinese过滤、完整/成功轨迹过滤改变人口；synthetic nofilter12.4 vs complete6.74/success5.06同时少掉过半数据，不证明失败经验唯一因果。两stage无优于mixed，64k/YaRN无优于标准40,960，longtail噪声反侧保留。Qwen3 8/14/32B两epoch/32k/b128/micro1/SP2/32或128GPU/CPUoffload，GPU类型/precision未披露；Harbor/Singularity fakeroot故障可容忍生成，评测另Daytona，不拼成无故障相同runtime。Actual Ch27 542–560已有container/task/verifier/scaffold/完整成功失败轨迹联合数据对象、失败标签混杂与诊断→boundedmixture→独立validation；239–248已有retention/分布变化，拟**已有覆盖 TRAIN-DATA**，不能沿headline把基模差归纯数据质或单配方通用比例。

### 2602.21196v1 — UPipe correction PRE

2+2+3=7深入，§3全链head-stage buffer复用/GQA ordering、§4实现/CPUoffload、§5关键capacity/launch对照。U heads/stage且U可整除C，project→inputAllToAll→attention→outputAllToAll重用中间QKV/comm buffer；GQA按KVgroup重排queries并复用已通信KV。**原S3.SS3.p4.1明确预先初始化最终output buffers并逐stage填入，避免concat各chunks的性能损害；现Ch36 601流程却写`→ concatenate output heads`，不可记Existing绕过已知矛盾。** 拟窄PRE只修该行成`→ fill preallocated output at owned head offsets`，并在自己的末注注明受影响事实/核验边界；其余现有593–605 head-stage/GQA/旧Ulysses分支不重排，不扩全章。

TorchTitan/FA3共同优化、nonpacked Q/K/V序列通信、tiledMLP/RMSNorm/CE共享但fullactivationCPUoffload仍在；H→U只中间attention tensor、不等总trainingmemory减少87.5%。8/16H10080GB，节点NVLINK/跨节点IB、主机1.9TB；5M场景pinmemory因主机容量关闭。较短context较慢，U=C最省buffer但多launch反退；最大8M只运行容量不授质量/收敛/长context有效能力。BF16容量分析与完整CPU/通信预算保留，无实测生产SLO。Actual Ch36完整591–606已有该机制，差额是具体错误输出策略，拟**纠错整合 TRAIN-DISTRIBUTED-TRAINING**，待root PRE/窄锁后才写与POST。

### 2602.21198v1 — Reflective Test-Time Planning

2+2+2=6标准，§3三个LLM角色/retro update、§4有限任务及A2必要费用对照。LLaVA3D三copies action/internalpreaction/externalpostaction，N4/T2候选选择；window/milestone/failure后用后续结果重新评价历史actions，将retro语言/score编为internalSFT＋policy REINFORCE（2sr/100−1）。未探索action的regularization用自身旧internalprediction，非独立gold或无forgetting保证；旧选中轨迹/score更新未给behavior-prob校正，不授onpolicy无偏。Household4families与MuJoCoCupboard有限sim评价，realrobot只qualitative；RIA/ROA单独移除可弱于两者都移除，不保证组件单调。3D7B/另QwenVL3B、有限LoRA/SGD配置，完整method约3×每step walltime，baseline3×stepbudget只约匹配时间、不等全部调用/训练budget；不采用5×规划headline。Actual Ch80 26–44已把verbalreflection跨到ephemeral weight/adapter状态、scope/budget/heldout verifier/reset/provenance与回退分清，拟**已有覆盖 AGENT-REFLECTION**，不把retro score当真实credit或任意在线LoRA准入。

### 2602.21202v1 — Multi-vector index compression

2+2+2=6标准，§3固定indexbudget/MaxSim、§4/5四compressor与AGC、§6训练/关键budget对照。AGC learned universal query在documentencoder内生成attention saliency选mcentroids→cosine硬分cluster→saliency加权mean，不是消费真实online query；hard assignment离散不证明语义分离、attention不为重要事实真值，梯度走连续聚合不通过argmax。SeqResize/MemTok/Hpool对照绑定同预算，文本MemTok≈AGC、ViDoRe平均Hpool差仅.002，更多附加query不任意单调，train32/test5/128只有有限budget迁移。95–97%是相对metric比不是事实/rare evidence保全；MetaEmbed训练规模仅1/20，MultiVENT fullindex不可构建，Omni音频16→4kHz与batch8改变输入，不能拼索引latency比例。BF16、固定训练步/数据population/不同flatvsFastPlaid评测，完整硬件/端到端费用/seedCI未披露。Actual Ch76 411–430已有persisted vectorbudget/indexidentity、compression非encoder/reader等比降本、rare evidence/重建成本和fullindex回退；与MAGIC真实query校准路径不同，拟**已有覆盖 AGENT-RAG**。

### 2602.21204v1 — TTT-KVB as learned attention

3+1+3=7深入，必要§3/§5 Theorem5.1–5.3与chainrule/累加更新步骤、§4有限行为、§6/7并行前提和反侧，不遍历所有appendix。仅TTT-KVB而非TTT-E2E；bias-free linear final layer f=φ(x;Θ)W，一步SGD把W更新写成φ_t(k)^T g_t(k)，输出φ_(t+1)(q)[W_t+φ_t(k)^T g_t(k)]。沿序列累加可成history-dependent learned linear-attention-like形式；动态φ仍消费更新后Θ，恒等式不自动给静态kernel/并行或逐事实可回读，momentum只改有效值的history coefficient。**只更新末层、冻结φ并去state weightnorm**后才有受限associative scan，非任何TTT无损parallel。多innersteps降innerloss而下游退步，gradientascent/query→key在所测variant有限结果，不构成所有memory无用/不能retrieval；可吸收符号的理论解释不授部署任意flip不重验。

LaCT760M/FineWebEdu100B/8A10020ksteps/b4/GPU、Book3 2.5BtokenPPL；另外114M/NVS与90M/ImageNet配置各异，NVS科学域结果不作项目新用途。深MLP在NVS、orthogonalization在LLM有益，完全简化略退；4×是singlebatch attention-layerthroughput非serving，1.19×特定训练速度。precision/多seedCI/生产SLO未披露。Actual Ch22 650–657已具体写KVB特定假设下history-dependent linearAttention及optimizer/nonlinearity/步数/binding改变可能失效，517–519将chunkparallel与记忆语义分开；拟**已有覆盖 MODEL-LONG-CONTEXT**。必要形式条件与代价在Report实例保留，不能因7分自动再造两段。

## B18 — 21144 / 21157 / 21158 / 21172 / 21175 / 21185 / 21186 / 21189，作者必要命题审阅待root非作者核

八项3058词mechanical必要原段、公式、control/反侧和actual owner见[V3_B18_CORE_OWNER_PACKET.md](V3_B18_CORE_OWNER_PACKET.md)。拟5Existing、1Only及2处窄PRE，尚无授权/写入，不计终态；B12–18共50已备必要项仍在98普通中。日期沿用V3_DATE_PACKET同IDSubmitted原字段+Registered秒精度ceil和official cutoff lower：均从02/25 09:00BJT起，21144上界23:40:37、21157 23:41:09、21158 23:41:11、21172 23:41:46、21175 23:41:54、21185 23:42:19、21186 23:42:21、21189 23:42:28 BJT，区间完全落窗。没有用Updated/Created授公开，也未读后版或全附录。

### 2602.21144v1 — Tensor-parallel selective SSM inference

2+2+3=7深入，§4.1–4.4/§5.1–5.5必要实现/消融。SSM cache保存每层compact recurrent state与短conv history、按channel owner分片，不是Transformer KV；packed Δ/B/C不能机械均切，logical-field placement先保证owned channel所需参数本地可得，再由channel-separable Conv1d/local scan减少重建collective。作者两处描述完整SSM-parameter AllReduce与本地B/C生成须按其配置解释，未核代码，不替作者补成任意SSM统一布局。采用“state/cache身份与collective布局共同决定执行计划”的条件机制，不授所有分片形式数学等价。四模型Mamba/Mamba2/Falcon-Mamba/Zamba、2/4A6000 PCIe或4A100 NVLINK；各方法按各自最大可行batch测throughput，非固定batch纯TP因果，4GPU在通信占优切片可弱于2。FP32→FP16 AllReduce结果的Top1/token和Top5/overlap是相对未量化输出一致性，不是外部正确率；完整token-order一致性更低，质量/通信费分别验。未披露服务SLO/尾延迟/生产并发，cache相对重复rescan不能充当相对最强optimized baseline倍率。Actual Ch49 392–414已拥有recurrent layout/lifetime/init/update和数值验证，234–236拥有joint model-shape/parallel/collective布局与成本；拟**已有覆盖 INFER-TENSORRT-LLM**，具体SSM channel/field实例留Report，不误投TRAIN-TENSOR-PARALLEL或声称正文已给Δ/B/C recipe。

### 2602.21157v1 — Halo EM-CoT VLA

2+2+2=6标准，§3三expert/mask/数据链、§4关键消融/真实评价及A2训练配置。共享attention但独立text/visual/action experts、special-token路由和crossmodal/frame masks把textual reasoning→visual subgoal→action chunk连为显式条件；noise tokens不可看对应GT，其他tokens不看noise。三个1.5B专家约4.5B总，不混写1.5B与基线容量。motion primitive由规则提取、Qwen3VL补reasoning、subtask terminal frame作visual goal，grounded目标不证明生成CoT是真实内部因果。VQA/VG/AP预训练组合与删除modality消融改变数据/预算，不能把全部收益唯一归EM-CoT；Halo-noEMCoT已经优于多基线。32H100、pretrain90k/40ksequence，FT110k(sim)/80k(real)/27k；RoboTwin clean2500与real320，真实四任务各50trials，generalization只是所选物体/lighting/layout条件。多seed/CI及端到端reasoning/action latency未披露；qualitative轨迹不证明“true semantic reasoning”。Actual Ch26 133–139已有高层目标到低层轨迹接口、subgoal projection/双级费用与controller action commit分责；拟**已有覆盖 MULTIMODAL-EMBODIED-VLA**，共享MoT与合成监督实例保留Report，不写成物理执行安全或泛embodiment迁移。

### 2602.21158v1 — SELAUR

2+1+2=5标准，§3 token entropy/least-confidence/margin混合→step mean→λ^(T−t)后段加权与Eq1/2、§4对照。failed step以.95×normalized uncertainty替换，failed trajectory以U(τ)替换，success维持原reward；是探索塑形proxy，不是真实过程credit、校准epistemic概率，也不能沿摘要称普通GRPO把所有失败梯度完全丢弃。author声称failure始终低于success依赖normalization/weights合同，未授任意weights下的数学保证。Qwen2.5 1.5B/7B、ALFWorld50/WebShop15步、A100/H100、lr1e−6/150steps/rollout8；positive/negative failure与success exponential反侧支持所测reward方向，component ablation并不证明uncertainty类型普遍正交。Table1若干ALFWorld子任务弱于GiGPO；较晚entropy上升与代表性trace不能唯一证明探索因果，多runCI/precision/整段采样训练费未披露。Actual Ch31 955–957区分uncertainty exploration prior与可观察effect/verifier的step credit，802–804要求保留未分解终局验收；拟**已有覆盖 TRAIN-RLHF**，受限failure bonus方法留Report，不赋予内部uncertainty outcome truth。

### 2602.21172v1 — NoRD

2+1+2=5标准，§3 weakSFT/组variance、§4 DrGRPO+DAPO/noKL、§5协议和supplement仅必要EgoProgress反侧。弱SFT后高variance组占较多、std归一使这些组相对缩权；移除std是成熟DrGRPO的具体VLA成立切片，不把difficultyproxy当自动正确难度。与原GRPO同weakbase的增益还包括DAPO asymmetricclip/noKL，不能唯一归因std；强SFT不同212k数据人口不是可比纯算法反证。Qwen2.5VL3B轨迹token、NAVSIM4s/2Hz模拟PDM及Waymo三reference RFS不同，BoN=6为oracle挑最好。16A100/b128SFT、30/32A100 RL/160或150steps/G8/temp1，validation温度.01不是严格greedy。EgoProgress未改善、inferred safety来自模拟proxy非真实道路，非“reasoning永远无用”；多seedCI/precision和完整runtime成本未披露。Actual Ch33 558–565已精确拥有去std/lengthnormalization、固定generationbudget与reward-scale/optimizer代价及不可任意叠DAPO，拟**已有覆盖 TRAIN-GRPO**。

### 2602.21175v1 — QCQC

2+1+2=5标准，§2 gallery-aware qualityconditioned completion、§3 bins/训练、§4 sameproxy评价/跨库反侧。不改原retriever，LLM用gallery文本及relevance/aesthetic的33/66percentile bins训练，再把短query+指定qualitylevel写成completion。OpenCLIP/caption与aestheticpredictor提供proxy，不是用户意图/美学真值；rank扰动分析只解释表达秩可能扩大，不保证质量。本篇Flickr2.4M/COCO、80COCOclassnames短queries用相同relevance/aesthetic仪表验收，非独立真实need评价；Qwen2.5.5B30epoch/b80/lr2e−5，GPT2-1.5B50epoch/b150/lr2e−3。未FT completion可能弱于prefix；randomscoreFT失控，Flickr→COCOaesthetic上升但relevance持续低，postfilter k质量与relevance取舍，不授跨库无损。硬件/precision/seeds/CI与端到端费用未披露。Actual Ch76 71–77已有query表达proposal、固定originalneed/index/reader、排名与答案效用分验和错误改写回退，拟**已有覆盖 AGENT-RAG**，特定质量bins不重构原长期owner。

### 2602.21185v1 — Duo++ Ψ sampler

2+2+3=7深入，仅采用§3 Eq11/12、A1.2必要induction与§5关键质量/预算反侧。真实clean x条件下将reverse posterior与q_s重加噪混为κ q_{s|t}+(1−κ)q_s，marginalize q_t后两项均回q_s；改变joint path而保持所指定每时刻conditional marginal。κ=1回原ancestral，mask prior可recover ReMDM，uniform prior允许token替换；tokenwise分解是给clean x后的条件性质，非数据token独立。部署用learned xθ/q0|t代入真实x，原边缘恒等式不授learned端点正确/任意步数收敛，(1−κ)(1−α_s)π offset亦可能引入错误。OWT/LM1B138M/b512/1Msteps/16H100BF16、sampling64bit logits/GenPPL GPT2Large+unigram entropy；CIFAR35M/1.5Msteps/classCFG。训练soft-Gaussian/topk curriculum降低词表费用，不当exact full-vocab objective等价；25%GPUh与33%peakmemory是此模型/半程curriculum，非serving比例。MDLM多数MCQ更好，schedule/CFG/nucleus须joint校准，NFE不等wallclock。

Actual Ch24 417–432已允许revision及训练error来源，但尚未解释“真实conditional marginals相同仍可重选joint反向路径、learned substitution不继承它”的差额。拟**窄PRE MULTIMODAL-GENERATIVE-PARADIGMS**：原423保守unmask共存段之后/427临时workspace之前两段+ownnote，说明κ/π/schedule/denoiser joint identity与费用/原sampler回退。不复制全部curriculum proof或授通用所有noise exact sampler；尚未获锁/未写。

### 2602.21186v1 — Spa3R predictive spatial features

2+1+2=5标准，B18原mechanical包已有，此处补齐此前漏写的逐项Report notes，不是新发现或额外家族。§3.2 asymmetric VGGT mask使context不读target，target可看全部；learned256 queries压缩context，再以target camera rays/relative3D encoding预测target feature；geometry/semantic teacher targets来自VGGT/DINOv3，不是实际完整3D scene或物理groundtruth。§4 ScanNet/ScanNet++、VSI-Bench288室内video/5000QA，MCA与numericalMRA不同；8NVIDIA5090/80k/每scene4–12views、encoder/decoder6layerD768，FT Qwen2.5VL3B只freeze原vision/Spa3R encoder，语言参数与residualcrossattention仍训练，不能称全VLM frozen或因此无forgetting。Relative PRoPE vsabsolutePlücker约1point受限对照，不唯一归因scene scale鲁棒；全流程precision/CI/端到端费未披露。Actual Ch23 876–880已有表示/primitive state身份及proposal非几何truth，但这项具体feature-prediction recipe目前不需要重构空间表示长期链；拟**仅报告 MULTIMODAL-REPRESENTATION**，理由不是只要不改权限就没长期价值。根复核未过，不计终态，B18八项原准备数不变。

### 2602.21189v1 — Pass@k prompt-gradient interference

3+2+3=8深入，采用binary fixed-verifier iid draws population目标Jk=E[1−(1−p)^k]和§3 exact gradient：每prompt∇p被k(1−p)^(k−1)非负重权；同题方向不翻，跨prompt总方向却取决于agreement a=<∇p,∇J1>。weighted average a为负才发生局部冲突，低success本身不足，若a均非负不能推出pass1下降。仅用必要chainrule/weighted-agreement身份，不采用原Corollary中δ<0却−δ<0的不一致符号，也不采用closed-endpoint η=δ/C2仍strict下降的未经闭合保证；这些具体形式争议保留、不可自行改号签成原作者保证，不推成整篇所有近似均失效。

Math2000随机抽样、DeepSeekR1DistillLlama8B/Qwen7B，实际梯度对象为最终hidden-layer state维4096/3584，非全参数实际RL更新；k32/T.7/topP.95/EMbinary，7组easy/hard阈值筛选只诊断对应population。toy展示/有限hidden-state MC alignment不能证明真实训练普遍pass1降或能优化任意inferencebudget；hardware/precision/总gradient费/多runCI未披露。Actual Ch31 414–420已有passk/sharpening≠能力与modeextinction，但没有跨prompt重权引入gradient interference这一具体条件。拟**窄PRE TRAIN-RLHF**：原411 Majority Vote小节前两段+ownnote，仅明确population目标/负agreement条件和hiddenstate诊断界限，optimizer/rollout额外成本、独立pass1/passk分验与固定目标回退，不采用原阈值/步长recipe。尚未获锁/未写，形式争议若影响这个窄采用由root定点回核。

## B17 — 21059 / 21061 / 21064 / 21103 / 21127 / 21133 / 21140 / 21143，作者必要命题审阅待root非作者核

八项3482词mechanical必要原文/control/直接反侧及actual owner见[V3_B17_CORE_OWNER_PACKET.md](V3_B17_CORE_OWNER_PACKET.md)。拟6具体Existing、2Only，无拟写书/lease，不计安全终态；B12–17共42项仍属普通98。日期复用V3_DATE_PACKET.md140–148同ID原字段及officialcutoff，公开下界02/25 09:00BJT，上界21059 23:37:07、21061 23:37:11、21064 23:37:19、21103 23:38:56、21127 23:39:55、21133 23:40:10、21140 23:40:27、21143 23:40:35 BJT，完全落窗，不以Submitted或Updated授公开。

### 2602.21059v1 — Expert-driven Schema of LLM Errors

2+1+2=5标准，§3系统/两阶段人审、§4.1新遗漏/幻觉子类与限定研究方法。采用专家无priming与后续schema inventory的同session比较发现：可信流畅/高层正确不排除局部数值、引用/源身份幻觉与关键遗漏，precision式错误和recall式遗漏应分开。68QA来自两作者专家9论文、开放/轴编码49codes；后10位NASA内部网络专家各三英文自著论文/十二问题、先自由反馈后inventory，无随机交叉顺序或盲独立gold。因此只采用具体被发现的评价盲区，不授schema因果提升/自动评价器总体错误率或科学领域结论。Mixtral8×7B Instructv0.1、llama.cpp0.2.61/4V10016GB、temperature.7、sentence retrieval12→60/8k；专家会话2h，人工编码/生成成本与多runCI未披露。Actual Ch66 51–76 transport/schema/semantic/outcome分开、事实错误/遗漏仍需独立人审与provenance已具体承载；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，schema子项留Report，不把新增taxonomy视作新release gate。

### 2602.21061v1 — Diligent Learner GF(2) reconstruction

2+1+2=5标准，§2强validator假设、§3–4有界oracle任务/partial access反例、§5协议与§6工具反侧。采用逐步proposal成功概率依赖已给正确prefix与新证据是否共同利用，不把test-time搜索预算视作自然保证。任务generator提供orderedANF/prefix/address boundary/32sample，未来项被oracle屏蔽，每步唯一正确continuation、O(d)检查；这是一条合成条件下的可诊断上界，不是任意数学题存在同样完美validator。data-only单sample Bayes反例不等多sample不可学习；effective-prefix curve fit不是内部真实容量。Qwen四配置3000实例/五depth/vLLM/32k或81,920context，frontier三模型各60queries/三depth、一半允tools；推理轨迹费用使完整protocol未复制，Opus“禁工具”仍有tool-like行为。因此采用局部信息/工具条件，不授超智能、普遍γ常数或工具唯一因果；hardware/precision/调用总费与充分CI未披露。Actual Ch66 132–138已有生成轴/oracle/witness/budget分责与内部容量不可倒推，这个GF(2)理论和有限next-step实例目前不需重构长期owner或形成开放推理recipe；拟**仅报告**，保其正面受限解释，非因理论/小实验排除。

### 2602.21064v1 — Conditional Capacity Expansion

2+1+2=5标准，§3四组件/mapping、§4匹配随机activation反侧及§6费用定义。小base每batch训练，loss连续k次下降后切较大模型，weights/buffers与optimizerstate经architecture-specific map往返，epoch起点回base；ViT宽/head与ResNet深度映射不授任意shape等价轨迹。Experiment B匹配每epoch activation次数而随机位置，对ResNet无损、EfficientNet略改善，故特定触发时刻不是唯一解释，capacity暴露次数同样重要。V10032/A6000、ResNetSGD/CIFAR200epoch、ViT300epochAdamW、ImageNetLAMB100epoch/不同b，三runs；较大EfficientNet不再增益。ACC/FLOPs及122x是增量accuracy除额外平均forward FLOPs之比，**不是walltime/wholetraining降低122倍**，未计齐copy/backward/optimizer/search总费；validation替代只holdout一batch。Actual Ch28 245–260已具体拥有shape-aware mapping、moments迁移/轨道不等价、loss shock/rewarm/rollback与旧预算；拟**已有覆盖 TRAIN-PRETRAINING**，alternation/frequency控制作为限定实例留Report，不创造新扩容通用定律。

### 2602.21103v1 — Prompt-Level Distillation

2+1+2=5标准，既有once核心root校准复用；必要§3/4/5/7/8。teacher用给定label解释再抽instruction，DBSCAN丢outliers/cluster synthesis会丢minority或edge；错例加成功例refine是受限修正，成功例必要不等所有minority覆盖。loop用training数据找错，文字称validation convergence但不授独立holdout；ContractNLI局部+2.5macroF1而StereoSet此阶段收益可忽略/一次vs两次loop。Gemini3Flash/Pro teacher、Gemma34B/Gemini2Flash student、5随机fewshot baseline；前沿与学生不同模型/API条件不能把80x/25xheadline全归因prompt编译，未披露公平全synthesis费/多seedCI，长prompt/preprocessing另有成本。仅静态分类边界，不授动态符号证明/运行时计算完全外化或bias消除。Actual Ch74 132–134文本抽取约束的collision检查≠NL意图、218固定预算probe/refine和owner发布回滚已承载；拟**已有覆盖 AGENT-PROMPT**，聚类minority丢失和mixed-success验证细节在Report保留，不声称正文已有DBSCAN库。

### 2602.21127v1 — HAT-Lab human-agent deception

3+2+2=7安全深入到§3边界/attack配置、§4随机guard/主要metric、§5.3风险感知与信任反侧、§6限制及E-B排除，不读全部攻击模板。303来自329剔9过快/7错agent/10低质；Prolific英文成年desktop/approval≥98%，每人三随机block，共九静态攻击、G1/G2/G3随机101/103/99。G3出现可疑输出才interrupt，主要结果是post-task“unusual/questionable”自报perception与开放回答attack识别，**不是真实危险effect被拦或长期防护行为**；专业/信任群组关系也非随机分配因果。warnings可升perception同时未察觉风险者报告信任增加，复杂场景识别仍低；不同G1总率8.6与warning段2.7对象未明，不合并精确headline，p=.205不签推荐评分显著。Backend GPT4o/静态刺激且跨model相似不证明所有用户或认知机制；40min/participant、部署/人工编码/硬件precision与费用未披露，长期警觉与adaptive attacks未测。Actual Ch72 3052–3061已写渲染仍不能保证理解、真实reviewer身份/能力隔离、每次review质量和cost不能默授；拟**已有覆盖 PLATFORM-SECURITY**，bounded human-warning反证强化现分责，不由human approval替effect gate。

### 2602.21133v1 — SOM-VQ

2+1+2=5标准，§2.2邻域耦合/两阶段更新、§3.3容量匹配反侧、§4有限reference控制及A.1训练身份。最近邻assignment仍在latent，code另有固定2Dgrid；SOM邻域更新+BMU EMA兼顾topology/commitment。topology proxy与token可学性不同：主表低PPL受architecture confound，capacity-matchedAIST++反而VQ-EMA更低PPL，只有Lorenz有限条件支持regularization；不授所有modal codec更易学。AIST++400序列51D→PCA32D/70-15-15，10epoch pureSOM+50joint/MLP、Adam1e−3b256、GRU10epochb64、5seeds；AIST64²utilization23%/MSE饱和，hardware/precision完整费未披露。reference-BMU远近重加权仅LSTM motion demo、Gaussian-smoothedprototypeMSE，无baseline或用户study，不是任意semantic方向/物理controller真值。Actual Ch23 198语义须intervention/reconstruction支持、206–210码本/encoder优化与utilization/消费者验收已拥有必要问题链；受限grid-control机制与直接反侧目前不需重构owner，也不复制prototype控制为通用codec recipe，拟**仅报告**，保其显式拓扑接口的正面增量。

### 2602.21140v1 — ReviveMoE

2+2+3=7深入，§3.2–3.6/§4恢复对照/§6范围。失attentionKV可用CPU保留的prompt+decodedtoken重prefill；受影响group停本step并丢本step新KV，block alloc/refcount用oplog回滚；不是任意layer暂停或保采样stream exactly-once。expert可副本/attention角色切换重载/近似missing-gate−inf三路径，不把近似quality与原coverage等同。XCCL group仍全destroy/recreate，以A/E domaintrampoline和compactlogicalrank避failedcard；graph cache按systemconfiguration编译，不复用旧identity。DeepSeekV3、80Ascend64GB/CloudMatrix384、driver25.2.1 CANN8.2.1 TorchNPU2.1.0，一card模拟fail、baseline已经cachedrestart且不计Docker/Rayready；83.1→10.2限此计时，role-switchweightload40.6sec等反侧保留。缺expert实验跨层同ID故障/按频率选不是真实placement全部风险，无生产SLO/多点/networkpartition/CI或完整memory overhead保证。Actual Ch52 346–357已有membership+expertcoverage+communicator/buffer/graph联合routing epoch和stream失败边界，340–342statefulattention恢复另有前提；拟**已有覆盖 INFER-DYNAMO**，oplog/graphcache实现细节留报告，不将7分或新stack名称作为扩书gap。

### 2602.21143v1 — DeepSynth

2+1+2=5标准，§2hypothesis→analysis→closedform构建、§3metric/模型access、§4best-vs-majority/工具对照、§5错误定位及必要A.1环境反侧。120tasks/16熟悉专家/223源→155→130→120可核闭式答案，不采用science/finance域实质结论；gold步骤只是一个可行路径不是faithful CoT唯一。JSONkey/valueEM/F1与LLMjudge容许1–5.5%数值差不同，score不可合并；best-of5是oracle选成功而majority5低，不授可部署selector。原32个OWL失败随机子集由两未参加原annotation者multi-label定位，15navigation/16synthesis不能相加成31独立失败。给goldplan改善同时多给信息/budget，不能唯一归因内部planning不足；AfricaF1=0切片不证明训练数据唯一因果。API/default工具权限不同，A.1 GPT5.2可发现端点却不能处理动态table/.xlsx/bulkdownloads，40taskstepF1掉落非纯推理失败；硬件precision本地不适用，API调用/成本绑定各协议，重复CI/稳定website_snapshot未完整披露。Actual Ch66 51–76执行/schema/语义/outcome与trace来源分账已具体承载导航/工具/综合失败定位；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，benchmark的有限planning及best/majority反侧保报告，不以120新题或SOTA低造新Books段。

## B16 — 20999 / 21013 / 21015 / 21035 / 21042 / 21044 / 21045 / 21054，作者必要命题审阅待root非作者核

八项3145词机械method/control/直接反侧与actual owner包见[V3_B16_CORE_OWNER_PACKET.md](V3_B16_CORE_OWNER_PACKET.md)。拟7具体Existing及1Only，无拟写书/lease，尚未授安全终态；B12–16共34项仍属普通98，不计完成。日期复用V3_DATE_PACKET同ID原值/officialcutoff：下界02/25 09:00BJT，上界20999 23:34:38、21013 23:35:14、21015 23:35:19、21035 23:36:08、21042 23:36:25、21044 23:36:30、21045 23:36:33、21054 23:36:55BJT，全部落窗；不是Submitted公开时刻。

### 2602.20999v1 — Visual Instruction Injection

3+2+2=7，安全反证深入到§3黑箱image/text写权限、§4.1/4.2/4.4、AppC指标与D.1采帧/crop、AppH反侧；不扩全部攻击模板。拟采用静态输入检视与视频时间展开后的输出风险分账：安全reference被加入语义文字/空间符号，实际输出风险在所测四API模型下上升；不把appearance benign等同规范允许，不将其称真实system role/parser绕过。w/o symbols同时去符号及改文字引用、w/o typography把文本转外部prompt，故比较支持联合输入配置，不能唯一识别符号注意力因果。PixVerse83.5→32.5为作者VBench改造指标，**任一采帧任一classifier报警即ASR**，非原平均帧协议或真实伤害概率；GPT5.2评分>50、CLIP一致性另分账。COCO构建10772实例不等实际每一target全量运行；采帧跳首1秒/每0.5秒、边框crop限制检测人口，N≈200文字有dataset subset/帧口径不能自行补样本数。GPT4o重写/GPT5.2render、官方默认配置，precision/batch/API费用/重复CI未披露；prompt-prefix有限反侧与AppH输出过滤可识别显式有害内容保留，后者非已验证完整部署防御。Actual Ch72 1241–1252低信任内容≠授权、600独立output-time enforcement已承载；拟**已有覆盖 PLATFORM-SECURITY**，I2V时间风险与指标细节留报告，不由新modality给旧注入原则加分或新造权限段。

### 2602.21013v1 — Scratchpad-Augmented VLAs

2+1+2=5标准，§3.1–3.3及5.1–5.4。语言grounding/plan/act分开，模型预测update token后追加description并作下一动作条件；recurrent训练短段仍丢初始信息，外显scratchpad可补，但更新token不是可信controller完成证明。T-VLA PaliGemma2 3B fullFT b8/GPU lr2e−5；R-VLA Mamba130M/ViT realvalueMLP b4 lr1e−5，4A100，不同backbone/representation非同预算架构优劣。ClevrSkills50rollout初始位置未见、已见对象；两模型Rotate-Restore均无scratchpad提升，finegrainmemory不能由语言子任务完成。MemoryBench100train/25eval仅PutBlockBack，RGB/wrist对pointcloudbaseline输入不同；**sim-eval以GT按按钮动作替代真实policy，100%不是原闭环成功**。真实xArm200demo/OpenVLA7B rank32 b8 lr5e−4，20rollout与65%subtaskcompletion有限，replacementdist仍较高；precision/seedCI/总训练推理费用未披露。Actual Ch26 548–550 episode/model-derivedstate与freshness、555敏感≠正确选择、508验证postcondition已具体承载；拟**已有覆盖 MULTIMODAL-EMBODIED-VLA**，语言scratchpad是该接口实例，不授agent跨session权限或物理真值。

### 2602.21015v1 — CHAIN

2+2+2=6标准，§2交互接口/成功与solved-only效率、§3.5/3.6关键对照、AppA.1限制。32puzzle/77stacking、color对象metadata与固定actionspace避开额外VLAcontroller；Unity/3DPython规则检查是所实现环境真值，不直接认证真实接触动力学。one-shot固定单视图对interactive多视图/history的31.2→9.1等有限差额同时改变信息披露/调用预算，不单归因closed-loop能力；generator固定选择实验的RM/多采样差额也不证明内部瓶颈唯一。视频示例评估是generation而非action-conditioned真实worldmodelrollout；不采用“所有worldmodel根本不可靠”。30–60step预算、主要Pass@1；Avg@4局部趋势不替独立CI，全环境人工建模成本高、硬件/精度/API总费未披露。Actual Ch66 199同环境预算下rules given vsdiscovery及披露/历史confound、94–106 EvalSpec支持域与metric对象已具体覆盖；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，不把新增领域题数当新增owner机制。

### 2602.21035v1 — CLIPGlasses

2+1+2=5标准，Method Lens/Frame/matching/training与Results消融。冻结CLIP，前3层syntax与末层semantic经residualgate得到negatedobject表征；跨模态context生成λ∈[0,1]，S=base−Mλmax(temperature·cos(query,negatedkey),0)，仅classifier判negation时校正；训练M=1/inference阈值.5不同。它改变明确否定条件下的匹配读出，不证明人类认知机制或attention faithful。GT negobject prompt本身来自CLIP作训练target而非独立visualtruth，三阶段训练另计。CCNeg188kimages/376kcaptions同任务CoNCLIP99.70>96.56、cross NegCOCO34.51>25.70支持局部ID/OOD取舍；原ImageNet53.87→53.28/Caltech90.96→90.97，**冻结参数不保证原预测或零shot全保持**；门误判仍可改变肯定句。FAR原定义是margin非通常falsealignmentrate，不能读作错误率。hardware/precision/batch/训练步数/多seedCI与完整额外成本未披露。Actual Ch23 101–103冻结多层读出与新增训练/接口成本已承载一般设计，91/95–97非目标稳定与实体支持另验；该有界CLIP否定head的具体增量目前不需重构既有表示/读出知识链，拟**仅报告**，不是因五分、小实验或未改变authority否认其贡献，不声称Existing已写此减分公式。

### 2602.21042v1 — OmniOCR

2+1+2=5标准，§IV-B/Alg1、V-A/C/D、VI。RolmOCR foundation更新ΔW=Σw_iB_iA_i，以L1/soft-shrinkage选有效rank；这里是训练期importance/prune，不是按在线input的runtime router。selected Attention/MLP、r8/a16；1H20 96GB、48²图、BF16/b1acc2/lr5e−6/30epochearlystop；checkpoint fold回冻结backbone本身不能防过拟合或证明Serving费下降。Yi/Dongba各只选30高频/高质量类，不授allscript/罕见类；fullFT AncientYi90.53>89.62为直接反侧。rank/模块/sparsity消融支持配置条件，但未披露完整顺序任务人口、累计forgetting统计/多seedCI或wholecost，不采用“保留全部旧知识/无额外推理费”。Actual Ch30 215–217rank/targetmodules容量和不能当本质维度、295nested rank的关键rank验收/固定shape回退承载；拟**已有覆盖 TRAIN-LORA**，保训练期pruning实例而不混入线上条件rank政策。

### 2602.21044v1 — LogicGraph

2+1+2=5标准，§3minimal support、4.1–4.3生成/Prover9、5指标与6结果/limits。BackwardDAG freshatomicidentifier防不预期共享，NL再翻formal并检查step/globalderivability/consistency；只可采用该有限生成域的参考minimalset/familycoverage，fresh ID与solver校验不自签开放NL所有minimalproof穷尽/faithfulness。成功找一条与全部参考路径recall是不同对象，family按inference节点集而非输出措辞分组；900分层300/300/300、2–19paths与深度6.01有界。topmodel SR96.11/diversity59.60在该evaluation显示探索coverage仍低，不等内部不会搜索；reference-free verifier仍依赖LLMformaltranslator、syntheticprompt与给定premises，98.80/95.22人审agreement不等无falsepositive，必要人审样本/重复CI/全部API成本未披露。Actual Ch66 3671–3673 atomic reference新测量人口、matcher/预算/覆盖≠内部faithfulness与3557formalchecker边界足以承载；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，将multi-minimalsupport/family分母作为报告特例，不为每一metric建章。

### 2602.21045v1 — PaperTrail

2+1+2=5标准，§3claim/evidence/源与answer匹配、§5受试protocol、6.1及8限制。OfflineGemini2.5Pro抽claim、SPECTER候选、online问句过滤+claim匹配+cos证据是provenance意见，不是paper事实真值；结构化JSON只保schema。counterbalanced接口顺序、task顺序固定，两task/source四论文；38参加剔12（latency无engagement等）后26N，剔除不看primaryoutcomes仍限制总体验人口。TXAI信任下降t25=2.61/p.015/d.44，编辑Levenshtein reliance p.313/自信p.525未显著；不能由不显著证明无行为效果，也不以p.137点击称有效显著。单session20min引导/未测编辑质量，latent错误仍可被source覆盖不足误标。Gemini2.5Protemp1、平均query90s、多串行调用/人工preprocess费，UI复杂性与排除latency用户反侧保留；hardware精度无本地适用、API费未披露。Actual Ch66 51–76五成功层与human/feedback/延迟outcome独立、3671 claim/evidence/最终verdict分账承载；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，具体trust-vs-edit用户研究在Report保留，不为一UI加长期协议或采用Mars science域结论。

### 2602.21054v1 — Vision-Aware Uncertainty Quantification

2+1+2=5标准，§4 Eq2/5/6、5.3主要maskingcontrol、AppAimplementation/labels。ISblank=H(noimage)−H(image)，IScore=H(coremasked)−H(image)，s=H(image)−αIScore；是模型entropy变化代理，不数学mutualinformation或truth/calibratedprobability。TopK来自10–25中晚层attention；原实现**attentionknockout而非rawpixel擦除**，不能把注意力同因果必要证据等同。VisualCoTGTmask oracle高于blank、randommask反退支持mask选择条件；ViLPfactual/counterfactual互补，不授所有视觉需要高IS。Greedy≤128tokens、heldoutα/K、layerheuristic、3seedmean、1A10080GB/PyTorch2.6；freeform由GPT5三judgevote和gold语义匹配、MCQ exactmatch，不等独立人体事实真值。额外固定scoringforward与无额外ARsampling不等免费；94.6%对特定VLUncertainty实现/任务，本文费用不可外推并发SLO。原定义[0,1]likelihood但s未映射归一化，采用rankingAUROC不采用概率/阈值部署保证，作者亦明非comprehensivesafety。Actual Ch66 244 internalattention sensor/labels/threshold费用及contextsupport≠fact、187–189显著特征≠targettruth、172provenance对照已覆盖该分责；拟**已有覆盖 PLATFORM-EVALUATION-SYSTEM**，report保双forward/modalmask代理不新建每scorer recipe。

## B15 — 20937 / 20943 / 20945 / 20951 / 20972 / 20973 / 20976 / 20980，作者必要命题审阅待root非作者核

八项最小原method/control/反侧与实际owner在[V3_B15_CORE_OWNER_PACKET.md](V3_B15_CORE_OWNER_PACKET.md)，未授终态；50safe/98普通不变。拟4具体Existing、2Only、2实际gap PRE，均无写锁/未写书。日期复用同IDSubmitted/Registered与cutoff下界09:00BJT，上界02/25 20937 23:32:01、943 23:32:16、945 23:32:21、951 23:32:36、972 23:33:30、973 23:33:33、976 23:33:41、980 23:33:50 BJT，不以Submitted作公开。

### 2602.20937v1 — Deriving μP using spectral scaling conditions

2+1+3=6标准。采用§3/C.2同时约束weight/update spectral scale、§4按optimizer实际update解width scaling的框架和有限coordinate/held-out曲线，不照抄全部Table2数值或声称任意optimizer都自动符合。线性MLP/b1为推导起点，noncancellation、activation保持量级与width-independent batch/low-rank update假设必需；fixed batch不能自动授随模型增batch免重新调整。初始化尺度依架构、更新尺度依Psi，epsilon/weightdecay/低precision项后核，改变optimizer身份应重推而非沿用Adam LR。§5 NanoGPT4A100/TinyShakespeare b2/8192tokens、width128→2048/depth8/earlystop150，Llama2 12IntelMax；AppendixB说明NanoGPT ADOPT/LAMB约width256后才稳定、AdamW/Sophia约128，depth transfer对若干optimizer仍振荡。表mean多runs但无表SD、图有误差，未采用未定量CI/普遍阈值；总sweep费/precision完整身份ND。ActualCh28 656–658已具体承载modified spectral scale→参数化proposal→coordinatecheck与失败时邻近sweep，拟**Existing TRAIN-PRETRAINING**；保optimizer-specific条件/finitewidth反侧于Report，不把理论框架当所有模型免调参证明。

### 2602.20943v1 — UFO recurrent long-range 4D reconstruction

2+1+2=5标准。原§3 3Dlocation+768feature scene tokens，输入RGB/camerapose/tracked3Dboxes，新帧frustum内近K3600在camera-local坐标更新，替换visible/追加new/保留others，再由object softassignment与learnedlifespan解码Gaussian；不是仅相机RGB自识别真实object动力学或actiontransition。§4 no-refinement/no-state退、no-state iterativetraining仍收益，显示temporalprior亦贡献，不能全归persistent memory。性能singleH20/b1、16s输入近linear与约25%memory少，但明确排除Gaussianrender阶段；训练16H200/b64/AdamW约一天、160×240/WOD三frontcamera，LiDAR depth/boxes等监督，不署zero3D/所有道路扩展。precision/seedCI及tracking/render全成本ND。ActualCh25 1003/1009已有流式可更新空间state/只校正影响区域、geometry漂移与重建回退及生成指标不签causal dynamics，拟**Existing MULTIMODAL-WORLD-MODELS**；保visibility/object/lifespan具体受限实例，不为Gaussian域recipe重构当前状态更新论证。

### 2602.20945v1 — efficient reasoning RL mechanics

2+2+3=7深入拟采用命题。原§2 R_T=I(correct)I(length≤L_T)，需按correctness拆长度、在2k～32k独立预算评Mean@8/Pass@8；strict2k改善不保证32k保留。§3 DeepScaleR按8rollout passrate>.5作Easy，不同prompt支持域而非同题难度因果随机；Hard正反馈稀疏时collapse。Mask incorrect只剩shortcorrect positive与longcorrect negative会length-collapse，mask所有long则可能length-rebound；L_R=L_T有限baseline避免显式惩罚完整正确长轨迹，可有更好局部Pareto，但不是所有任务最佳长度。增加N8→24同时加rollout费用、LCB差很小；highstaleness16仍entropy/length反弹，Qwenfamily未用offpolicy，且4B-Instruct/30B L_R与L_T仍不同，不能说所有配置严格相等。DSRDistillQwen1.5B/GRPO/lr1e−6/b128/N8/max16k/target4k，后续24rollouts/easy，Qwen0.6B～30B批16～128；约0.2M GPUhours不等单项或部署成本，hardware/precision/repeatedCI ND。ActualCh31 785–790已有curriculum与verifier-noise/rollout预算分责，但**缺correctness×length四格及负样本mask与rollout截点分责**；拟两个窄段在现785后/Imperfect Verifier前，保原testtier curriculum与verifier噪声路线。

拟PRE正文：

长度也是训练中的选择条件，而不只是部署统计。只给“答对且短”正reward时，四类rollout——短正确、长正确、短错误、长错误——必须分别保存mask、reward和真实采样截点；零reward仍参与group比较，移除样本却改变了有效训练人口。若只保留正确轨迹，长正确便可能成为唯一负信号，使policy把“短”当成“正确”的捷径；把所有长轨迹mask掉又可能留下未约束的长度空间。因而长度曲线应按correctness拆开，不能以平均输出变短签推理能力保持。

[受限效率RL对照](https://arxiv.org/html/2602.20945v1)显示，正反馈稀疏的hard prompts、不同负样本mask与staleness会改变collapse或length-rebound；缩短真实rollout截点与生成长轨迹后惩罚不是同一干预。较易prompt或更多rollout能改善有效reward密度，却改变输入支持与计算量，不能据此宣布普遍easy-first或N越大越好。应在相同policy/verifier下并列多个部署token预算、质量和每次有效update成本；小预算提升可能伴大预算退步，代码任务收益也较小。质量、奖励密度或长度控制不稳时保留原correctness-only目标、已验证的固定采样预算与独立多预算评价，而不是继续加强“更短”的代理目标。<!-- source-family:SF-2026-ARXIV-2602-20945 -->

### 2602.20951v1 — ArtiAgent

2+1+2=5标准。原§4 entity/subentity grounding→四类patch mapping，target替RoPE位置为reference并借缓存V，background保原位置/缓存V，FLUX1dev/FireFlow inversion；这是受控structuralartifact监督构造，不等所有physical不合理类型/无损原场景保证。LPIPS阈值.5/.9 heuristic或GPT4o三视图filter与local/global解释，非逐个humantruth；干净counterpart另走restoration减少生成traits，50kpair→100kVQA。§5 ArtiBench1k现代生成图、12humanannotator、50:50artifact与clean，不当自然失效率；Qwen2.5VL7B/InternVL3.5 8B先freezevision1epoch/b64/lr1e−5后unfreeze200step/lr1e−6支持有限detect/localize/explain增量。Testtime搜索2^r pool只见自有reward升，修复同一VLM定位/验证只有qualitative，不签独立结构改善或risk消失；generator/filter/SFT/search/inpaint总费与hardware/precision/seedCI ND。ActualCh27 329–332已有synthetic generator/judge共错风险，Ch31 921已有结构artifact遗漏及独立paired评价；**拟Only**：四类位置/V注入产生局部负监督的受限recipe留报告，其生成/过滤身份与独立下游验收并未要求重构当前通用data/measurement论证，不因未加书降分或否认具体表示操作增量。

### 2602.20972v1 — TagLLM

2+1+2=5标准。原§2分别测annotationprecision/recall/F1与下游ResNet101 mAP，部分O365类别MLLM标签训练胜原dataset humanlabels；这不证明MLLM普遍比人可靠，human comparator为旧dataset原标注，未独立重标证明每项humanerror。§3 MOP candidate→BP、ChatGPT建议co-occurrence groups、CAD supercategory/negative visuallysimilar/namephrases消歧，candidate遗漏不能被BP无条件恢复，co-occurrence不是已知真实概率。§4 COCO/O365有限控制，下游ResNet101 lr1e−4/b128/AdamW/EMA.9997/ASL；O365抽约100k并保>100positive类后251classes，稀有尾部不在结论内。COCO2017 unlabeled123k标签只有下游COCO2014分数，展示top20增益类别是选后图不是全部均匀收益。费用测annotation GPUtime但模型、硬件/precision/seedCI/完整CAD与train费用未全披露，不采通用20x总降本。ActualCh27 800–810 inferredlabel/metadata需独立语义检查、308–310同起点重训utility与240–248过滤改变支持域的具体论证已有；拟**Existing TRAIN-DATA**，保label-score与trainingvalue分开评价及命名歧义实例，不把dataset labelagreement或human身份签最优训练目标。

### 2602.20973v1 — Linear Reasoning vs. Proof by Cases

2+1+2=5标准。原§4 PC-FOL/Replace各511linear+511case，原故事291、词替换并有小改，balanced不等逐题固定所有难度因素。§5 label True/False/Unknown accuracy、proof ROUGE/Pass@k由GPT4o匹配专家proof，是参考过程一致proxy；自动Pass@k大涨不签真实proof都正确。另webinteractive GPT4o生成由一名数学家分wronglabel/wrongproof、correctlabel/wrongproof、两者correct，case正确label中不足半正确proof，labelproof不同人口不能同均值替代。词替换/numberpremise诊断、不同seed/temp补实验仍不能建立图模型是内部唯一因果，§6假设性解释不用于Books保证或完整理论证明。模型API/web两协议不同，hardware/precision/batch/完整调用预算与human一致性CI ND；SFT附件不属本次采用命题。ActualCh66 132–134复杂度切片不由length代替、3671–3673 terminalverdict/reference trail分开已具体承载，拟**Existing PLATFORM-EVALUATION-SYSTEM**；保case branch覆盖与专家发现proxyfalsepositive这一受限blindspot，不以reference ROUGE当proof authority。

### 2602.20976v1 — proactive warning evaluation

2+1+2=5，安全信号深入受影响原§3–7/限制。只采用普通无恶意query下的warnings/safealternative/harmfuladoption分责与长度/语言/模态切片，不采用生态/法律science结果、法规普遍适用性或species结论为本项目新增。1068queries GPT生成→同模型一致筛→in-house人工查，另285species×26queries；GPT5分response子集并200sample人GPT94%agreement仍非独立行为真值。Short为prompt“response in short”而非匹配token截点，warning提及率随长短变可能受输出机会/内容表达影响，不能读为内部风险识别因果。Explicitsystemprompt改善受限ProR但genericdisclaimer亦增，species识别/提醒弱耦合不证明真实控制无害；5publicAPI中版本、sampling/seedCI/batch/总费用未全部披露，publicUI≠API安全层已作者限定。ActualCh66 94–104 EvalSpec行为/人口/taxonomy/slices可承载，**拟Only**：该固定规范集合下的warning漏计/机会盲区留报告作为实例，不把领域阈值引入通用riskgate、不把文字warning当真实安全动作或法律建议。

### 2602.20980v1 — CrystaL

2+1+2=5标准，实际latent表示学习gap加深必要方法/对照。原§3 intact与corrupted同I/Q/CoTpad/Ans结构，逐decoderlayer把intact latent hidden states换进corrupted路径，answer-token KL与answer→latent attention一致性+两路CE；不是semantic label独立真值或去损坏图像后都causallyfaithful。原attention全map KL反退，仅answer→latent较好；blur优于crop/jigsaw/noise，8latenttoken优于4/16，DirectFT有限对照支持学习接口取舍，不签“视觉latent真正不可或缺”普遍因果。Qwen2.5VL为基座、16kvision任务，LoRA r16/a32/lr2e−4/4A40；SKILA/LVR从已发表结果抄而CoVT/LIVR另local协议，16kvs100k非全预算匹配，precision/batch/epochs/seedCI/E2E双路费用ND。ActualCh23 1046–1051已有canvas→latent容量/trace边界与1056以后write/read诊断，但**缺直接训练latent成为可消费跨损坏路径接口**；拟两段在canvas段末源标后/Object Hallucination前，不替原可读trace/视觉输入路径。

拟PRE正文：

加入连续reasoning tokens，并不保证模型会使用它们；完整视觉输入可能让最终答案绕过这条中间路径。一个受限训练分支保留完整图像的intact stream，另给同题的corrupted stream，将前者各decoder层的latent states移入后者，再分别约束答案分布和answer对latent tokens的attention，同时保留两路next-token目标。它把潜在状态做成显式训练接口，而不是只增加一个可读CoT槽位；intact/corrupted配对、扰动方式、转移层与token身份、loss范围须共同保存。

这种特权训练转移仍付两路前向/状态拷贝与对齐成本，训练时完整图像信息不等部署时可获得的干净真值。[受限CrystaL对照](https://arxiv.org/html/2602.20980v1)中blur比若干空间扰动稳、8tokens优于4/16，匹配整个image/latent attention图反而退步；对齐范围和破坏的语义必须另验，不能从answer改善或attention相似签内部推理faithful。已发表不同预算baseline也不认证普遍更省数据。若扰动改变正确答案、latent使用未得到独立检验或质量/总成本不合算，保留原视觉表示、直接微调、可读trace与外部grounding，不让latent接口的成功自证事实或替代上述写入/读取故障诊断。<!-- source-family:SF-2026-ARXIV-2602-20980 -->

## B14 — 20903 / 20904 / 20911 / 20913 / 20924 / 20926，作者必要命题审阅待root非作者核

六项机械原核心/对照/反侧与实际owner见[V3_B14_CORE_OWNER_PACKET.md](V3_B14_CORE_OWNER_PACKET.md)，3368词。只拟具体Existing，未授终态或Books写入；安全50/148、普通98不变。复用同ID日期证据：官方cutoff下界02/25 09:00BJT，上界20903 23:30:35、20904 23:30:38、20911 23:30:55、20913 23:31:00、20924 23:31:28、20926 23:31:33 BJT，Registered秒精度上界并非Submitted直接作公开。20904 HTML实际为空转换壳，定点exact-v1 PDF补必要机制/对照，不拓展27页附件。

### 2602.20903v1 — TextPecker

2+2+2=6标准。原§3.2分离字符结构异常比例与Hungarian word/NED+unmatched惩罚，质量项clip、训练omega5/评价omega1与两项各.5；不是OCR认出文字就证明笔画正确。结构数据以OCR初稿后人工标异常、Chinese stroke删除/交换/插入增广，standardfont/strokedata限制，极端artistic deformation仍混淆风格与错字。§4.2 SD3.5在CVTG OCR wordaccuracy+8.3而自有Sem−7.8体现指标不一致，不独自证明所有OCR改善是假象；§4.3与AppB逐项消融支持受限分责，但同训练assessor又作评价，不是独立gold。Qwen3VL/InternVL3 8B，2epoch、b2/acc32/lr5e−6、32H20，三个generator内共超参；AppG SD3.5 100step5.52h vsPPOCR5.40h，额外assessor在RL而非部署，完整生成/标注/校准成本、seedCI ND。ActualCh31 255–257已有异质对象reward匹配/eligible分母及proxy≠semanticvalidity、独立gate与费用回退；拟**Existing TRAIN-RLHF**，保具体glyph结构失效实例与两种指标人口，不为该有限assessor另建通用reward recipe或给它真值权。

### 2602.20904v1 — Transcoder Adapters for Reasoning-Model Diffing

2+1+3=6标准。Exact-v1 PDF§3.1–3.2 L190–317只训练稀疏ReLU deltaadapter，targetattention/embedding保持、baseMLP+adapter替换targetMLP；不是全部base→target变化都由MLP解释。OutputKL/NMSE/双向bridging/L1，§4.2 L413–425取消bridging后NMSE低但partialreplacement KL升，activation重构不等outputfaithfulness。§6 L810–833用wait/1ktoken作hesitation proxy，手选5623与随机50k对照、两类共同加入wait8.2超过full5.5；选wait-promotingfeature后necessity部分依赖选择，不证明所有reasoning过程必要。L876–906长度7.2→3.2k伴AIME25准确26→20反退；原target逆adapter−1不连贯，作者用−.5，不能等同replacement exactzeroing。Qwen2.5Math7B/R1DistillQwen7B一对、MLP-only；50kOpenThoughts3约380Mtoken，Adamlr8e−4/b1平均7.5ktoken/BF16，bridging采单cutoff降低前向费；hardware/seedCI/E2E费用ND。ActualCh5 304–311 replacement/errornodes/attention/pruning、原model干预与prompt/modelscope的faithfulness budget已具体承载；拟**Existing WORLDVIEW-REPRESENTATION**，保delta模型diff与bridging反证实例，不把feature label或wait归因签完整内部思考。

### 2602.20911v1 — SAEF

2+1+2=5标准。原§3冻结ImageNet21K ViTB16，task bottleneckadapter16/orthregularizer不是精确正交LoRA保证；CLIP classprototype聚cluster、visualprototype择相近pair组成合并tree/globalroot。Inference每个cluster tree比较children predictiveentropy选path，再globalroot+paths负entropy权重融合；lowentropy不是校准truth/全局最优path。§4.4 earlyexit tau1平均depth1.19、理论近6x伴accuracy−.29，K1或task数/无限depth反退；完整构建/训练/候选评分费用不可当零，理论树深不等生产SLO。RTX2080Ti、20epochs/task、b48/SGD.01/cosine，CIFAR20×5其余10×20，固定classorderseed1993非多seedCI，precision/并发/完整latency ND。ActualCh30 595–597同坐标/功能兼容条件、603–607 composition/merge/routing重新Evaluation已承载；拟**Existing TRAIN-LORA**，报告这一task hierarchy/entropy routing的有限取舍，不以adapter名称或独立task分数授组合功能保证。

### 2602.20913v1 — LongVideo-R1

2+2+2=6标准。原§3单QA按需视频导航，D3等长分割/约16秒leaf、cap宽描述与leafQA不同；LRMQwen3-8B主要消费textderived工具观察，不宣称全部frames context。§4 CG800视频/5.6kQA→33ksamples，GPT5teacher30%失败时先扩首level再goldcluehint，正确trace不等faithfulness或无泄露适用保证。§5 reward答案/位置interval/重复分责；§6短视频与globalquestion不占优，视觉相似错branch不能自行回返，均限制导航选择。8H80080GB/mixedprecision/FSDP/SFT3epochsRL2；RL captionoffline pre-extract、QA32B占2GPU，其余6RL，不能把训练说成全live按需零precompute。受限LV约3min/50%→2min/49.8tradeoff，换toolmodel也改善不能全归LRM；seedCI、完整caption/多QA费用/单项timing hardware人口 ND。ActualCh75 391–397 orientationmap/derived observation、provenance dereference/working-set fault费用具体已有；拟**Existing AGENT-CONTEXT**，保视频层级定位与跨leaf歧义实例，不为每模态造导航段或把caption当原始事实。

### 2602.20924v1 — Airavat

2+1+2=5标准。原§3registry capability接口+curator四测试仍expertvalidation，§4KG来自2021篇网络测量literature，verification只测methodologicalalignment非结论correctness，validation只在registry真有匹配gold时比较。§6–7 Prefix2Org12配置各一次全部执行成功却catchall错映射；KG warning能自动修BGP但WHOIS仍需LLM-guided人工修，更清楚query后两者auto，对query条件不能删。另36workflow是3runs不同人口，不并为12重复；60–65→20/22=90.9只特定mapping任务。§9新问题copilot、registry人审/未文献化bestpractice与长期/private条件限制，不能自签科学结论或所有correctness。Generation$.8–1.7、综合评价$4.5–7，under10min只生成，不含expertcuration；hardware/precision/batch/CI/E2E时间ND。ActualCh66 47–49 runtime≠semantic成功、108–110 code/auditor合规仍规范搜索与独立复算已有具体承载；拟**Existing PLATFORM-EVALUATION-SYSTEM**。采用的是可执行与方法规范不等的受控失效证据，非网络学科成果/成熟pipeline本身的新recipe；警告不等repair receipt，人工回退保留。

### 2602.20926v1 — HELP

2+2+2=6标准。原§3OpenIEtriplet→1:N passageprovenanceindex，HyperNode累积triplet lexsort embedding、queryTopn启动、全adjacent expansion后semanticbeam裁剪；这是检索proposal非逻辑证明/verifiedfact，无completecoverage。Finalpath contributions累加到passage与DPR backfill/dedup，重复同源路径不成为独立consensus。§4.4 Recall@5只至少一goldpassage，M4最佳/M5略退支持graph缺失噪声下flatbackfill，N3 F176.18但577.2sec/N4质量退，fixedbeam不免去全邻接候选embedding费用。Llama3.3-70B提取/生成+NVEmbedv2；HippoRAG2 published results非全复现，另baseline共同LLM；PopQA1000query graph retrieval1403→85sec不是含index/OpenIE/gen端到端SLO。hardware/precision/batch/concurrency/重复CI ND。ActualCh76 281–283 graphtext投票/provenance/deferredstate/hybridfallback与805–810 query-specificsubgraph、tail费用及原span/构图revision验证已有具体承载；拟**Existing AGENT-RAG**，保sourcebacklink/路径扩张局部效率与反侧，不把semanticpath签逻辑真值或不受hop增长影响的可扩展性。

## B13 — 20799 / 20800 / 20813 / 20816 / 20878 / 20880，作者必要命题审阅待root非作者核

六项最小机械原文/actualowner在V3_B13_CORE_OWNER_PACKET.md，3456词；未授终态，当前50safe/98普通不变。日期均复用已核同ID原Submitted+Registered与官方cutoff：本窗09:00下界，上界20799 10:58:50、20800 10:58:51、20813 10:59:11、20816 10:59:15、20878 11:00:46、20880 11:00:49 BJT，非Submitted直接作公开。无需重开已校准完整题摘。

### 2602.20799v1 — UCD-Training

2+2+2=6标准，具体长期gap加深必要内容。HTML在§5.1 Design后中断，已精确v1 PDF定点恢复p12 Table3/p14 Table4，未遍历21页。原§2.2 DAG文件依赖按DFS路径+滑窗提议样本，区别于topological order简单split可能分离有边文件；不能签任意大文件/依赖环下的完整边覆盖保证。§2.3三类SFT以内部测试/依赖实现作usage先验，答案正确性代理reasoning正确性、同DeepSeek生成/判语义，非所有trace实证faithful。Table4 Qwen3-14B去CARD LEANN55.2→25.5，去reasoningfilter Hexi compilation54.2→55.9不支持每层过滤恒改善；数据类型删减不全等token，不把全部收益独立归给DFS。Same规模训练baseline，但CPT额外阶段、不同RAG model/budget；32H20、32kcontext、全参5e−5、SFT3epoch，precision/batch/seeds/CI/E2E总费ND。四repository“unseen”是created/cutoff及低base performance推定，不认证没有污染。ActualCh27 327–330 synthetic judge与788–794 packing/boundary已有，**缺依赖关系进入同一training instance的条件身份**；拟两段在packing边界段前，不改原EOS/sidecar路径。

拟PRE正文：

Packing除了消除padding，还要看训练目标依赖哪些跨文件关系。独立文档或不需跨文件组合时，普通shuffle与按长度截断最直接；若语料只有新代码库的实现，API依赖却跨文件，拓扑排序的相邻位置不保证实际依赖相邻，分窗后可能失去同一实例内的关系证据。一条受限分支先从parser产物形成文件依赖DAG，沿DFS路径构造候选序列，再按上下文预算滑窗；它把依赖共现而不只是token利用率纳入样本身份。Graph/parser revision、路径、截断与有效进入实例的文件须随data lineage保存；这是条件化数据构造，不是改Attention或认证模型已懂调用关系。

该分支增加代码解析、路径重叠与重复token、合成/过滤及CPT/SFT成本，也受环、大文件与缺失测试约束；不能仅凭有边就宣布每对依赖必进入同一完整窗口。[受限v1对照](https://arxiv.org/pdf/2602.20799v1)中usage/composition监督有局部价值，但去数据类型同时改变监督数量，额外CPT也不与不同基座RAG同预算；compile/test或judge判答案正确不证明trace faithful。应分别验收边/文件覆盖、真实执行任务与原通用能力，关系失真或预算收益不足时保留原文档packing、真实usage样本与推理时检索，不由源码created时间签“训练从未见过”。<!-- source-family:SF-2026-ARXIV-2602-20799 -->

### 2602.20800v1 — Leakage-Free Two-Judge GenIR

3+1+2=6标准。采用§3 A不参与train/tune/selection、querytuple整组split与固定两judge validintersection的人口协议；不采用“differentfamily=独立gold/数学消灭所有leakage”。Yi1.5-9B与Llama3.1-8B，A/B invalid25.79%/33.01%，33,052→17,965 conditionalpopulation；10querysplits70testquery/seed不等700独立queries，不能采其700observation permutation显著性作为部署保证。MoralStories500仅两judge相关ρ.653，不是额外人类评分比较；SSGENρ.046，sharedpretraining/规范假设保留。S3称训练distilledstudent而S4.SS2.p4称off-the-shelf/no finetune，**蒸馏身份/收益归因未闭合不采用**，只协议分责。hardware/precision/batch/end-to-end费用ND。ActualCh66 128–130 hiddenholdout、293–299第三方proxy≠gold与人工anchor已承载，拟Existing PLATFORM-EVALUATION-SYSTEM；原recipe身份冲突若以后更正只重开distillation命题，不补造训练。

### 2602.20813v1 — Alignment Behaviour Benchmark

2+2+2=6标准。原§4 trigger-referee控制后续turn执行，904scenario/37behaviour/24model，条件turn机会与judge一起定义评价，不混真实tool effect。§5 50刻意覆盖scorepopulation、5raters each，人AI category70%却failcriteria F1.11/pass.69，同verdict不能反推同原因；100scenario plausibility人审与该50judgecalibration不同人口。§6 24×37 PCA含27zero-var剔除，Nmodel<behaviour，英语/Western规范、provider/training共变，factor不是alignment转移因果/新的保证。API/rollout/referee/human成本，完整单模型温度、重复seed/precision/batch/latencyND，不沿榜单推广生产风险。ActualCh66 998–1000 turn/conversation/judge分母与3671–3673 verdict/evidencetrail分别验收已有具体承载，拟Existing PLATFORM-EVALUATION-SYSTEM；有限多轮行为覆盖与reason-level calibration留Report，不添排行榜段落。

### 2602.20816v1 — Tail-Aware Distillation

2+1+2=5标准，具体loss接口gap加深到Eq2–4及决定对照。同词表teacher rank-topK加一个tailmass坐标构成KL1，tail内部归一分布KL2，原KL=KL1+αtail KL2；目标把第二项按sequence mean αtail归一放大，仍付fullteacher/student概率求值，非稀疏topK loss、非改变教师真值。真实nexttoken与teacherargmax39–46%不一致，rank-anchor不等label-anchor；不采用§2.1每步tailmass恒增加/所有非线性收敛保证。Table4同Regmix2Btoken、共同cosine目标对照Qwen2.5学生Vanilla44.9/RKL45.4/TADK10 46.3 avg；K过大增加noisy高熵位置权重，收益饱和退步，原MiniPLM25–50B/teacher100B不同总预算不得合并成本。1H100一周或Gemma2双H100、b128/2kcontext/Adam1e−4，precision/trainseeds/CI/E2E费用ND，PetaFLOPs仅1Mtoken估计不是吞吐。ActualCh29 248 label修正、449–451 sparsecorrection分别已有，**缺rank-based tail内部目标与质量总量分责**；拟在248后两段，不静默替原温度/goldlabel分支。

拟PRE正文：

没有可信gold标签的预训练蒸馏不能把teacher top-1当作必然正确的target class。同一词表下，可以按teacher概率排序选TopK，把这些坐标与剩余tail总质量作为一份粗分布，再把tail内部重新归一为另一份分布；普通forward KL恰由粗分布KL加teacher tail mass乘内部KL组成。Teacher分布很尖时，后项自然很轻，一条替代分支以整条sequence的平均tail mass归一其权重，保留头部/总质量目标并加强tail内部相对概率监督。TopK身份、prefix、sequence分母和loss版本须共同冻结；它与有gold的局部质量转移、只在选中坐标上近似反传是不同选择。

放大tail并不证明教师尾部语义更正确，低熵位置tail很小、K过大时高熵噪声的权重反而增加。[Tail-Aware Distillation v1的有限对照](https://arxiv.org/html/2602.20816v1)支持共同数据/目标下的局部收益与K饱和反侧，不认证每一步tail总量单调、任意学生收敛或所有任务改善。该路径仍支付完整两模型forward、概率处理及训练成本，名义FLOPs不等总显存/latency；应分别验收held-out KL、校准与下游行为。Tail估计/分母不稳、教师偏差放大或收益退步时，保留普通温度/全词表KD与原student，可信gold可用时继续采用上述有标签分支。<!-- source-family:SF-2026-ARXIV-2602-20816 -->

### 2602.20878v1 — ViLCaR

2+1+2=5标准。原§2–3LVLM提graph、detector/CLIP删无groundingelement、LLM graph-only依最终goldanswer可达性最小prune，goldassumptions含文化/角色假设，非干预识别的实际SCM/因果真值。§5 CA语义匹配至少50%triplet/阈值，CI另LLM与goldpath比，QA终局分别计；Table2 CA.458→.488/CI.652→.690但QA.763→.768只受限proxy分账，bestgraphsetting不等budgetmatched所有prompt，不能把额外goldgraph信息说成纯表示无额外答案信号。30graph×15annotator质量复核，不认证全集；Qwen2.5VL7B、80/10/10，硬件/precision/batch/seedCI/生成判图总费ND。ActualCh66 3671–3673 reference-unit/proxyalignment≠internalfaithfulness与最终verdict分别验收具体承载，拟Existing PLATFORM-EVALUATION-SYSTEM；不把causal命名授真实因果或新science路线。

### 2602.20880v1 — Conflict-aware Adaptive Safety Guidance

2+1+2=5，安全信号深入受影响内容：原§3Table1多类别平均或错类会削弱有限SD1.5 harmfuldetector结果，不能把PCA/projection所见直接认证真实harmful语义；§4每t对各keyword条件求noise，取与promptguidance最大cosine的类别施原SLD；text分支取最小projectionresidual，两个选择接口不同。§5四harmfulbench/COCO1000，Q16或NudeNet阳性只是有限detector人口；SAFREE FID43.7→CASG46.3不说无质量代价，固定/LLMcategory baseline反侧支持受限adaptive选择，不能签混合多类皆清除。AppD6 exactcostSD1.5/50step/1H100：text3.9→3.98s，latent7类10.2s=2.58x，precision/batch/seedsCI ND；training-free非免费。ActualCh24 232–240已有reference/capacity/history/conditioninterface分支，**缺多类安全direction相消与category-conditioned choice的压力**；拟在历史guidance反侧236后两段，由Ch24拥有具体samplermechanism，不让Ch72重复recipe/不赋deployment安全权限。

拟PRE正文：

增加guidance条件也不等于约束更强。单一明确类别时，固定安全reference便宜且可解释；多个有害类别的noise差分方向在同一latent和timestep上可能对立，简单组合会稀释本应压低的类别。一条受限分支每步分别求各keyword条件的guidance，与当前prompt的差分比较cosine，只把最相符的一类交给原安全steering；它改变reference选择而不重新训练denoiser。文本投影另有选择接口：比较各有害子空间的projection residual，再只采用所选子空间，不能与latent时间动态选择当作同一实现。

Cosine或小residual是所给keyword/模型下的对齐代理，不是真实有害语义，也不保证混合多类风险同时消除。[CASG v1的受限SD1.5对照](https://arxiv.org/html/2602.20880v1)支持固定/错类/平均reference的局部失效边界，但harmful率依赖Q16/NudeNet，SAFREE分支FID仍退步；需要独立内容与正常效用验收，不能由sampler自签发布安全。各类别求值仍付费：50step、单H100的七类latent分支约2.58倍原SLD时长，text projection增费不同。类别失配、过度内容改变或预算超限时保留已验收的固定reference、较保守采样与外部过滤/人工审查；training-free不取消模型求值或平台的安全裁定权。<!-- source-family:SF-2026-ARXIV-2602-20880 -->

## B12 — 20751 / 20759 / 20770 / 20791 / 20794 / 20796，作者必要命题审阅待root非作者核

50/148安全、98普通；此6项未计终态。精确v1原HTML段落机械包[V3_B12_CORE_OWNER_PACKET.md](V3_B12_CORE_OWNER_PACKET.md)2697词，paragraphID保留以定位；完整必要正文投影V3_PARA_*.txt，公式不在paragraph者按原V3_CORE_*.txt核，不把该投影当完整证明。V3_DATE_PACKET同ID区间完全落窗：下界02/25 09:00BJT，上界20751 10:57:42、759 10:57:53、770 10:58:09、791 10:58:39、794 10:58:43、796 10:58:46，Registered秒精度上界而非Submitted公开。无自身Books锁，无代码核验/复现。

### 2602.20751v1 — SibylSense

2+2+2=6标准。原§2内外loop、§3setup/controls实际paragraph21–66/Table1 txt1488–1520。冻结rubricgenerator/verifier，8expert例/4candidate，item的reference−candidate verifier gap与可重复性regularizer驱动memory；categorizer分层、每类tophalf避免只取globaltop，outer更新candidate为训练后adversary。当前evidence只存query，**不是完整reference/verifier认证证书**；itemscore只对当前candidatepool成立，弱/窄pool会过拟合。Qwen3-32Bgenerator/8Bactor、GPT4overifier/o4miniexternaljudge，reference-less仅测试rubricgeneration，outer/inner训练仍依赖expertref；病例数据这里只测LLMrewardloop，不授医学应用。GRPO3×8A100/b16/16rollout/lr5e−7，Adv相对Base GovReport52.9vs52.6小差，无seed/CI/完整memory/搜索调用费披露；不证明普遍rewardhacking消除。Actual Ch31 540–545已有onpolicy失败驱动rubric变更/独立promotion与版本回滚/同源过拟合，拟 **Existing TRAIN-RLHF**；此memory实现提供具体实例而非另建长期自评权，来源也未给独立truth保障。

### 2602.20759v1 — Overton Pluralistic Reinforcement Learning

2+1+2=5标准。原§4 OPdata/MBGM/reward与§5.1–5.2消融（paragraph13–48）。SBERT tasktriplet来自LLM多数冗余判断，promptkeywordmask+mutualbestgreedy一对一reference覆盖；singleanswer内uniqueness=cluster数/K，不是群体rewardvectors联邦聚合。threshold/聚类是learnedsimilarity代理，不能授所有观点真实相等/多元社会代表性，reference漏观点不会由coverage补齐。16kSFT+12kGRPO（3B/1.5B）改变训练，相比直接prompt/大model不能全部归reward；0.70阈值/scale40/5:1ratio局部搜参，不给未测task默认。去uniqueness保coverage但redundancy、长度增加，3:1/1:1小独特提升伴coverage退步；NLImean/accuracy@.33与ChatGPT4.1judge不等真实人类满意或安全，ValuePrism原machine-generated/人复查及再LLM增强有majoritybias。训练硬件/精度、seed/CI、完整walltime ND（V100仅SBERT编码性能）。拟 **Only**：当前Ch31 214–228明确basis/jury/weight与代表性分责，本文有限reference-set单答案匹配取舍值得Report保留，但并不重构当前群体偏好聚合接口；不把它误标现有Federated机制已覆盖、不为一套窄SBERT阈值组合另开recipe，保5分不降分。root若认定reference-set覆盖/单答去冗余为长期缺口，则再定点提案，未自行排除。

### 2602.20770v1 — Pipeline for Verifying LLM-Generated Mathematical Solutions

2+1+2=5标准，original-proof falsepositive反侧定点深入。原§3六步solverstructuredlemma→translator→prover→link；§4.1/4.3、§5.1–5.2实际原txt602–710，once核心复用不重读附件。Qwen3-8B/Kimina7B两类，自动化脚本仍受translation/prompt/type，Lean通过只证形式化theorem；过易问题prover独立完成，可绕过原错误structure。easy10/similar150经可形式化筛选/Math500有限，precision.822/.984/.942人口不同不估全球FP概率；interactive0FP/FN依人类Lean知识，不授自动保证。200手改错误/answeronly/换statement控制43/50正确且0/150错误通过是特选早期样本；answer检查额外解7题与originalsolution检查目标不同。多agent/scripts/human/call及false-negativecost，GPU/精度/time/seed/CI ND。Actual Ch66 3557 proof只覆盖formal theorem及1791–1795 sameverdict≠参考语义/独立checker/abstain已有具体承载，拟 **Existing PLATFORM-EVALUATION-SYSTEM**，不把原结构falsepositive写成新完整verificationrecipe。

### 2602.20791v1 — Rehearsal Scale

2+1+3=6标准。原§3Gaussiansetup/min-distance interpolatingestimator、§4closedform角色/条件、§5 Figures5–7与TableIV（paragraph12–65）。明确iid Gaussianfeature/noise、同n/σ、均匀每旧task s/(t−1)、最小变化norm，p与n+s的regime及taskoptimal参数差限定解析主张；不采用其未在当前HTML附出的B/C/D完整证明或把denominator阈值迁到LLM。只采用**有限理论提出的机制解释+作者实测非单调反例**：旧任务rehearsal增大不等所有acquisition/retention/generalization同时改善；DNN MNIST/CIFAR/TinyImageNet至少3重复均值，category-sharing/noise/sampling/depth同时改变适用人口，未给CI、逐配置预算/硬件/精度，不声明buffer大小的独立普遍因果。Actual Ch28 1478–1489已将replay与internaloverlay分支并存、分别验收acquisition/retention/transfer；拟 **Only**：该固定linear/DNN人口的非单调曲线目前没有建立可直接采用的foundationbufferselector或一般容量阈值，不改变已有独立三目标验收/回退路径，有限解释保Report，而非因为理论/小实验一律不入书。无formalguarantee采用、不扩大证明队列。

### 2602.20794v1 — VGGDrive

2+1+2=5标准。原§3producer/consumer接口、§4setup、Table7 txt2284–2345与camera对照。冻结VGGT preDPT保camera/registertoken；每decoder层visualmask取2Dquery、逐层独立downMLP→multiheadcrossattention到3D K/V→upMLP/residual只改visualpositions，GTcamera intrinsic/extrinsic加入K/V不能冒充零camera知识。16H200，两阶段各2epoch/b2/1e−4→5e−5，基座第二阶段也调，与one-stage/参数共享基线预算不全等。Table7 shareCVGE PDMS88.05/Time.96 vsfull88.76/1.04，baseline86.04/.81，收益增加resident3Dfeature/逐层计算，不授“无推理开销”；NAVSIM有限模拟闭环不是现实autodriving safety，NuScenesopenloop与BLEU语言指标不混。seed/CI/精度/batchtailSLO ND。Actual Ch23 105–107已经具体拥有producerlayer×consumerlayer/visualpositionmask、残差适配与驻留/训练预算/末层回退，拟 **Existing MULTIMODAL-REPRESENTATION**；本文frozen3Dproducer提供限定实例，不添驾驶域recipe或geometry真值保证。

### 2602.20796v1 — Parameter Update Magnitude

2+1+2=5标准。原§3shared/tasklinearGaussian、§4frozen/init二任务参数预算条件/主文derivative→stationarypoint步骤（paragraph16–54）、§5gradientcosinehybrid/3seedresnet（55–61）。固定总容量下trainablesize与forgetting有tradeoff，作者stationary条件ξ>η>0及距离限制仅该Gaussianregression模型；不采用未核完整AppA的全局最优/所有nonlinearmodel保证。Runtime用前后taskgradientcosine阈值决定freeze或增module，是参数距离关系的**代理**，不等作者解析δ真值或原定理证明该选择最优。CIFAR共享category提高similarity、CUBcorruption使差异增大同时变distribution，adaptive优于initialized的3run均值/冻分支优势随异质度减弱只是有限control，不授预训练LLM后训零遗忘；gradient测量/模块存储/路由及额外搜参费，硬件/精度/CI ND。Actual Ch29 854–858具体trainablesubspace/update-depth/optimizer/taskorder identity与塑性/保持/回滚取舍已承载，拟 **Existing TRAIN-SFT**，不把cosineproxy另写成理论认证threshold。
