# 有限尾包40题摘：题摘校准与有限核心判断

原件：tail-agent-execution.raw.xml（start0/20，total100）与tail-multimodal-generation.raw.xml（start0/20，total87）；ascending submittedDate，查询各限定分类+主题+执行/表示词与202610021800–202610051800提交线索窗。提交窗不是公告证明，后续拟入选需exact-v1/日期。两页以20为有界停止点，不把余167条变队列，亦不称查全分类。本页不自动准入、评分或Source通过。

| ID | 作者贡献判断 |
| --- | --- |
|03894 Proxy Confidence|拟准入：actor logprob不可得/重复采样失效→surrogate teacherforce/PMI/verdict/toolchoice按错误类型互补，random-value反馈对照→黑盒动作可靠性sensor和反馈适用边界；非仅低价模型judge。|
|03902 Evidence Changes|拟准入：repair revision token省被当memory收益→full ingest+revision+use与source-filtered reread对照有成本排序反转→修订证据下memory投资边界；只通用memory机制，不纳医疗效果。|
|06914 DataBrain|拟关闭：schema、typed tools、persistentstate和deterministic hooks的既有组合，DataBrain任务与fault通过未披露新增执行机制或既有评价新失效条件；当前v2不作v1证据。|
|03984 Teaching Agents to Code Reliably|拟准入：自己patch自己的test可伪通过→对每patch的revertedtree判分并以gold/错误变体断言credit训练verifier→search与verification训练的新反馈分工。|
|04008 SkillScriptBench|决定事实待核：clean/doc/script/both匹配状态区分repair/preservation可能有具体负证；AST/callgraph定点修订本身成熟，若只是已知代码维护移植不准入。当前v2不可当v1。|
|04083 Self-Propagating Misalignment|拟准入/安全：外来memory poisoning假设→agent自写目标后跨aligned接班/100sessions且禁memory后filesystem传播→审计和禁单tool不能关闭持续状态威胁；prompt诱导不等自然失控。|
|04087 DUET|拟关闭：solver/grader交替prompt修订和既有tool update组合，AB无新的feedback归因机制或具体既有评价失效条件；仅四benchmark平均改善不足。|
|04109 SEER|拟关闭：时序预测中反思query+知识memory+防lookahead已有组合，未披露新增模型/训练/执行机制，领域预测改善不扩主线。|
|06923 RadOnc|拟关闭：临床schema/identity validation及跨阶段state既有机制组合；移除validation大量误派是既有合同作用，非新增机制；不以临床任务规模准入。|
|04116 CUAWright|拟关闭：bash+filesystem统一programmable harness，本身已有terminal/CLI设计；GUI/CLI数字未披露新增执行机制或受控新失效边界，不能由框架更小/多场景得分提升准入。|
|04168 Cognitive Depth|拟关闭：五维taxonomy/proxy/perturbation提案无具体机制或已验证的新评价边界。|
|04178 SHarP|决定事实待核：single-module ablation saliency再prune属成熟消融；heldout是否揭示原模块独立打分无法预测joint删除的新边界，否则是known pruning转harness。|
|04184 EvalResearchBench|拟准入：开发target最佳自制evaluator不等sealed排序最佳，时间/API预算冻结后有truncation/score集中/预算耗尽→self-evaluation元评价的具体反证；需v1核。|
|04188 RotationCoT|拟关闭：structuredCoT+坐标上下文转空间任务，三种CoT无显著差异但未改变已知prompt条件或新机制，非新领域就收。|
|04195 MemLeak|决定事实待核/安全：若只是sharedvectorstore不做ownerfilter导致泄漏、硬ownership gate修复，是既有accesscontrol缺失，不能把新名字当新机制；需core确认有无已按tenant授权仍泄漏的新路径。|
|04262 CADForge|拟关闭：componentgeometry/code-review/tool-memory组合在CAD重建应用，AB无新增通用接口或具体失效边界。|
|04313 MOIRA|拟准入：ragged per-head页数使padding/hostplanning失效→mass覆盖最小页集合+self-planning block从listlength分工且留CUDAgraph→adaptivebudget与graph执行的新兼容取舍。|
|04375 IEC/IntAct|拟准入：emit/result轨迹看不到receiverparser改变→nonexecuting逐hop观测firstdivergence、保真delivery或拒绝→行动语义与错误归因新测量/执行接口；安全相关。|
|04432 Video2World|拟关闭：video-to-simulator新benchmark，looksbetter/worksworse只重示既有视觉≠功能原则，AB无进一步具体机制或未有新边界，当前v3不作v1。|
|04438 RAGrasp|拟关闭：DINO/SAM+template+geometrygrasp已有组合，非foundation/VLA训练或表示的新机制，少量机器人成功率不扩范围。|
|03980 FADE|拟准入：clip均值漏单frame reactivation→jointKV edit+frame/time门控per-conceptLoRA+otherconcept hardneg/router→多概念视频遗忘的时空接口和质量代价；需v1。|
|03991 SkinDistillation|拟关闭：临床metadata masking+KD/gatedresidual已有方法组合，领域分类提升无新通用机制。|
|04009 SUAVE|拟准入：action/video不同输出接口→shared discrete sequence的masked生成、maskpattern切换world/policy、无actionvideo排loss→共同表示/训练接口实际变化。|
|04038 PACPrivate|拟准入：每步DPSGD clipping/noise→训练低维adapter后多次mechanismoutput协方差校准一次各向异性噪声→隐私单位/重复输出及训练composition的约束变更，核PAC/RP适用假设，不采科学应用效果。|
|04088 DualProcessDriving|拟关闭：神经planner/MPC+KG风险切换已有组合，无大模型/训练/推理主线新命题。|
|04198 ALoDLM|拟准入：每位置统一depth→unknown token保latent recurrence/commit离散context，tokenwise schedule latent+conditionalNELBO→DLM计算分配与训练目标联动接口。|
|04391 AgenticTactileVLA|拟准入：固定VLA预测不等实际接触→contact证据触发/refine/retain/release/return控制、matched close-to-stall反证→prediction与physicalrealization的受限交接。|
|04494 DreamTest|拟关闭：RSSM imagined rollout用作已有DRL测试surrogate，AB未新建worldmodel机制/适用边界，更多failure发现是领域testing效果。|
|04510 ManifoldCache|拟准入：外部constraint map下score法向/切向分解→宣称schedulemidpoint safe-cache/latepositive modeconfusion及Jacobian层stride条件→通用diffusion近似适用域的新理论命题，不采用科学任务质量；须核强断言假设。|
|04526 EmergencyCellular|拟关闭：CNN/diffusion合成压力测试网络业务监控，thresholdshift是已知校准原则的新应用，无foundation主线新机制。|
|06955 ROMA|决定事实待核：主动缺证据→交互反馈已有perception loop；若只有多模态dataset/两阶段align+interaction模仿，无新evidence-sufficiency执行/表示接口则关闭，非默认准入。|
|04540 DreamFormer|拟准入：多token高分辨率观察使imagination长链昂贵→一个输入token编码多视图且用expertlatent轨迹reward在imaginationonpolicy训练→representation/rollout成本取舍，核不是无损压缩。|
|04554 EagleDepth|拟关闭：latentfeatureguidance+预训练pixeldecoder组合用于depth，未建立通用foundation生成新机制/条件，像素更细/更快不是单独准入。|
|04585 JEPA Velocity|拟准入：single-frame target被当完整动力状态→无blur renderer无法含velocity的结构负证+pose/finitediff motion分支及matched-memory对照→worldmodel state可辨识性条件。|
|04607 ForeAct3D|拟准入：futureforecast与执行action脱节→policyactionchunk条件化future3D queries、staticity/rigidity/kinematicclosure训练期约束→VLA表示目标与行动交接，不需推理futurehead；需v1。|
|04659 PermVLA|拟准入：固定LTR chunkfactorization→CAP随机revealorder+chronologicalprefix，subsetconditional辅助训练而部署仍LTR→regularization与控制接口分责，不声称chainrule新发明。|
|04736 PhoneForecast|拟关闭：UNet行人预测+VIO/track自一致评估，无foundation表示/训练/推理新命题；统计边界已知，不能新领域应用扩主线。|
|06972 BoTFeedback|拟关闭：姿态descriptor+对齐+CoT用于教练反馈，新领域structuredinput组合无新增通用执行/训练条件。|
|04767 FlowSkillWM|拟准入：control-rate长链search→flowpolicy seed/code/label对应完整skill作为一次transition，commonplanner下applicability与label收益分离→worldmodel action抽象和search瓶颈的具体条件。|
|04778 PatientWM|拟关闭：patient时间序列predictor的split/shift/uncertainty受限审计，没有foundationWM/训练/推理新机制；已知泄漏原则用于医疗数据，不因worldmodel名称扩范围。|

## 校准后的有限终态

root实际完整读40题摘后分层校准；不把total187的其余结果转队列，不追加分页。18项进入必要Source/date：03894、03902、03984、04083、04184、04313；04375、03980、04009、04038、04198、04391；04510、04540、04585、04607、04659、04767。其中04510只采用通用几何理论，不纳科学任务效果。其余22项贡献前关闭、不评分；表中原“决定事实待核”保留初始判断，但最终结果如下。

04178原AB只支持成熟single-module saliency/prune，未给joint删除的新失效边界；06955仅主动感知loop/两阶段训练组合，均按已读完整AB关闭，非因工作量。04008已定点读exact-v1 §3/5.1（本地core-04008v1.raw.html）：Markdown→AST/CST唯一node、call context与preservation constraints、node替换/语法接口校验是既有局部程序修复组合，Clean/修复指标未建立新执行机制或超出“修复不等保留”的新有效性条件；root实际读相同核心接受关闭。04195已读exact-v1 §3核心（core-04195v1.raw.html）：pool中不执行owner后置gate，strict partition及hard postretrieval ownership恢复原边界，没有证明既有tenant授权仍被突破；root实际读接受关闭。两项均不因日期未查另建恢复请求，不作为安全正证。

03984实际拟采用已由Source收窄为oracle-rejected mutants/siblings的weighted assertion-token credit，不采用初稿“revertedtree”概括；04540实际拟采用一个time position承载64×32分类latent、训练imagined/部署真实context分责，不称无损单token。准入不等Source/Books通过，后续必要层见独立ROOT_REVIEW/READER_REVIEW/READER2_REVIEW与报告§4。
