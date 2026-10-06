# 04 独立有限主题筛选与校准

作者sept12_15_author，窗口UTC2025-09-03 01→09-04 01。启动完整重读当前AGENTS/Prompt/合同/ROADMAP与路由checkpoint；当日路径与原件定点查无旧材料，不从README缺失单独推断。四查询model44、systems8、multimodal13、agents26；submittedSep2 18Z→Sep3 18Z仅宽发现，91去重75家族，75题名全部实际浏览。选52相关/含糊家族取得[精确v1完整题摘](exact-v1.raw)全部实际分4批读完，未读其余23摘要，不把库存变逐项关闭/全文队列。URL/实际检查时间/sha见raw旁request。

## 首次作者冻结45潜力（DAY纠正后的当前结果见末节）

不评分、不做Books，不授FullEvidence。此为原52题摘的45pot/7close历史停点，不是当前最终分母；10518曾按中心争议保留，现已由官方撤回证据取消潜力，原准入解释仅为追溯错误判断保留。

| ID v1 | 原约束→实际增量→局部选择 |
| --- | --- |
| 02718 | offline routing不适高volume预算→ANNS历史特征+初期小query集一次dualLP→在线routing；randomorder/相似性与大opt前提 |
| 02751 | semantic operator迭代贵/DeepResearch无queryplan优化→agent写可优化operator程序→数据runtime，2基本query不是通用提升 |
| 02753 | expert pruning省容量不必省GPU执行→weight-only layer activeexpert分配→MoE资源选择；不能吞memory/throughput反侧 |
| 02754 | LLM模块直接移植motion不必成立→五模块controlledtransfer/失败适配→VLA表示、目标与TTS边界 |
| 02761 | planner去噪可能误删humanrecovery→judge/planner迭代验证并保留recovery轨迹→模仿训练数据可靠性 |
| 02805 | modality冲突检测与决策混同→linearprobe信号/attention阶段分离→多模态解释接口，相关性不即causal |
| 02820 | 单format/ROUGE忘记有假阳性→JS目标、semanticjudge/worstparaphrase+ICR与utility分账→unlearning评价；不授irreversible |
| 02830 | speech PEFT domain-shift缺适配条件→右singularvector选择旋转/左固定→语义映射与训练参数分配 |
| 02910 | personalized agent不等更保多样性→Facebook匹配选择generic/personal两维反向结果→代理选择目标；非真实人longitudinal变化 |
| 02915 | audio全解冻不必更好→同数据四epoch LoRA vs LoRA+encoder/projector受控指标分叉→组件/质量/资源选择；非整个LLM fullfinetune |
| 02966 | VLA场景动态/knowledge grounding缺→temporal-frequency/spatialencoder与retrievedprior三段alignment→动作表示；仅openloop |
| 02981 | orthogonalupdate步长缺依据→clampednorm accumulator+spectraldirection→Muongradient适应，不采任意神经网最优 |
| 03018 | collective黑箱难定位可靠性→内部control/data dependency trace→分布式训练故障归因 |
| 03020 | EOS未训练全context语义→双向query/document reconstruction→embedding训练目标 |
| 03025 | text无visualevidence仍被当图内→FFN VisualAbsentneurons/detection改写→跨模态grounding接口 |
| 03047 | checkpoint恢复慢/异步step不一致→DP存活replica+optimizer barrier/step tag→恢复一致性；全DP失败仍需checkpoint |
| 03054 | 固定group量化→sorting/adaptivegroup优化→权重误差与量化成本；v3明确纠正v1 bit长度，1.007bit不可采 |
| 03057 | fixedadapter冗余/rigid→可微gate稀疏插入path搜索→多task PEFT结构 |
| 03059 | RLVR verifier domains少→question-answer-code执行合成接口→训练数据验证；不是chemistry科学应用指标回流 |
| 03113 | visual/text bias逐例变→gradientnorm influence与contrastivedecode→解码可靠性/预算，whitebox最多5倍成本 |
| 03131 | language-centric recommendation缺item动态→统一hierarchicalitemtoken与recommendation-oriented AR→模型表示/预训练替代，不只推荐成绩 |
| 03136 | fixedKVbudget不同workload失配→MonteCarlo futurequery attention投票→自适应cache预算 |
| 03234 | highrank与vectorPEFT效率冲突→随机共享Tuckernetwork小scalevectors→rank/参数分账 |
| 03263 | GPU数量与time-to-train/efficiency混同→MLPerf4.1四workload再分析和heterogeneoushw限制→测量条件；无同硬件因果scale证明 |
| 03310 | validator全开启不等可靠→30prompt删unit/UI/lint消融misreject/quality取舍→Agent验收环境，不吞反侧 |
| 03312 | failuretracer同语言模型低正确→counterfactualreplay/faultinjection标注+多grainRL→失败归因 |
| 03329 | 英文bias测量不可直接转文化→matchedtranslation与SESGO两层/不同方向→评价语种边界，不证全部mitigation因果 |
| 03345 | deductive分数掩盖inductive/abductive→programmableworld+hypothesisparsimony度量→推理评价盲区 |
| 03377 | CXLbyte读取隐藏bit规律→bitplanecompression/precisionfetch+KVcluster→near-data bandwidth；losslesscodec非低precision无损 |
| 03380 | groupchat秘密原文仍可访问→局部aspect数据视图/事件更新→代理信息可见性；p/a-agent policy仍LLM，不授noninterference |
| 03383 | 分类attack不等物理危害→动态actionleader帧目标/安全距离taxonomy→VLA危害评价；ACT/Bakuseen任务而非所有foundationVLA |
| 03405 | factfrequency不完全解释knowledge形成→entityretrieval+checkpoint因果data干预资源→表示学习验证接口 |
| 03407 | token平均accuracy不等labelconfidence→BERT6strong-matchclustering与层间变化→表征形成局部反侧，非普遍定律 |
| 03501 | coarsevideo缺事件/gesture锚点→temporallydensemasklet/meta合成→spacetime表示训练 |
| 03505 | fixedtargettabular不统一missingness→contextconditional多mask联合变量query接口→主线外新foundation路径，非仅tabular应用 |
| 03518 | refusal不等没有战略deception→zeroablation+contrastiveactivation steer与sale/honesty取舍→安全行为控制；非所有有意欺骗证明 |
| 04508 | smallagent longtrajectory难学全subtasks→逐epoch新增subtaskcurriculum→多agent训练/效率Pareto |
| 04512 | average scaling掩盖category/data量→1Bfinetune高data分类vslargerzero/few-shot局部可行→评价与部署预算，不授therapy/privacy安全 |
| 06990 | weights-only foundation小domain缺继续训练信息→简单SSL continuedobjective少hyperparams→预训练迁移预算 |
| 06992 | federatedlocal标签不覆盖global攻击→GlobalLabelEmbedding beacon+crosslayerpromptgenerator→distributedVLM robustness条件 |
| 06994 | 多选题不等OCR/enterprise输出协议→BlockWeaver variable/unorderedOCR比对及描述faithfulness→多模态评价接口 |
| 10513 | heterogeneous instruction specialization缺→sequencegroup→tokenexpert两stage→MoE routing语义粒度 |
| 10515 | BTpairwise/rationality假设→uncertaintyutilityanchor支持unpaired→preference数据/目标替代 |
| 10518（已撤回关闭） | 原HKM准入解释被当前官方paper withdrawn/v2 history标记否决；原v1内容仅保留必要排除与争议依据，不评分、不采用、不在当前潜力集合 |
| 2510.01197 | chartcode质量掩盖数据检索/visual规范→三层评价与guidance/selfevaluate差异→Agent结果评价；Oct编号与Submitted不能倒授Sept首公开 |

## 7明确关闭与FIRST

02864 Arabic多agent生成/evaluator/swarm再生组合，摘要无新增通用控制成立边界；03161 已有PEFT直接processlogs领域预测；03335 已有程序search+traffic simulator的领域算法成绩；03479 一般textgame deepRL而非foundation/LLM机制；03394 普通VM干扰预测借Transformer，不构成本项目大模型runtime桥；04518 已有GRPO用于SLMtool的效果数字，无新目标/执行机制；04515 BAME更强within-each-ethnicity prompt+人工解释迭代未控制，只有领域representation改进，未建立独立新机制/成立条件。关闭不等无学术价值，不因域、survey、模型大小或原来已有主题一刀切；风险与混杂笔记保留。

root非作者FIRST已实际完整读取12代表题摘，认可上述六明确关闭；要求02915/03310/04515/10518普通核心继续执行。作者实际补读后root基于定位笔记校准：02915组件/指标分账与03310validatormisreject恢复，04515混杂关闭（非声称解释机制无效）；当时10518争议保留/非withdraw的判断已被末节官方标记纠正。03505两入口准入认可，新模型contextconditionaljoint/missingness可潜力，不是只映射章节。root没有声称五项原核心已独立实读；全部拟项与必要原文已由sept22_25_author本次DAY实际读取，不借局部FIRST授完整日报。

当前事件页轻量风险检查：03054currentv4 comment承认v3 bit-length error，历史v2撤回、随后v3/v4有效正文；10518currentv2则首部明确paper withdrawn、history v2 (withdrawn)、无PDF且comment significant errors。原“没有withdraw标签”断言撤销，见[官方当前原件](status-10518.raw)与[03054不同版本范围](status-03054.raw)。必要核的精准版本和受影响位置见[核心](NECESSARY_CORE.md)。DateHold≠贡献关闭或FullEvidence；普通核心18已处理，不假装外部受阻。

## DAY限定恢复、官方撤回与最终分母

sept22_25_author从原75题名浏览库存只重开03116/04516两含糊项，实际完整读官方精确v1题摘；[原件](reopen-v1.raw)/[访问记录](reopen-v1.request.json)不以Submitted作为公开。root另逐一实际打开官方精确v1完整题摘，非作者FIRST通过；原作者接受这两项有限修正，不把delegated读取改写成自己亲读。

| ID v1 | 原约束→实际增量→最小准入范围 |
| --- | --- |
| 03116 | 直出数值评分有任意数bunching/不连续→直接pointwise、pairwise、token-probability-weighted pointwise及小模型finetune四路线比较→标量construct的scorer选择潜力；不采用摘要数字作通用可靠性结论，公开日期仍hold |
| 04516 | 翻译后任务分数不等本地训练评价→两单语BERT、原Swahili新闻分类与Swahili转英文路径局部比较→跨语种评价反侧潜力；不证明LLM内部translation、isolated language causality或所有原语训练更好，公开日期仍hold |

10518原v1题摘/§3–6/A反证已保留，但[官方当前页](status-10518.raw)首部paper withdrawn与v2 history精确撤回标记是新的必要排除依据。root本次实际打开官方原页确认范围，原作者接受纠正；清除该家族当前候选、评分和采用链，不留日期潜力/erratum复活请求。未来须官方明确恢复且独立重新审阅，才可能作新的处理；并非仅因争议、访问难或省审而缩池。

最终54完整精确v1题摘=46日期/原家族终态潜力+8关闭（原7贡献关闭+1官方撤回）；75浏览题名中其余21摘要未读，非逐项关闭或全文队列。正式当窗候选0、采用0、Books0。18必要原文全部按NECESSARY_CORE限域独核，其余潜力不授FullEvidence。全部8关闭题摘均实际读，六明确组合/领域桥接/既有目标理由分层、04515强prompt与人工budget风险深入、10518撤回全核；14来源有限入口/数组/分页/停止已独核，外部日期与六历史源保留不授Coverage/Evidence或无遗漏。
