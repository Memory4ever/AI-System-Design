# Oct24 C6：实际owner与窄PRE

oct24_org仅本文件，root唯一Books/Report/State writer，reader独立核。当前Books方法/指南重读，Source只消费本日ARXIV证据批C六项必要域，不第三读全文；前文Source作者不是本文件作者。精确版本/评分/公开日仍按ARXIV，以下不是Source/Books/DAY自签。实际读四owner开篇、目标正文与完整邻段，未以Review notes的完成标签替正文覆盖。

## 三项具体NC提案

### 31446 AMV-Guard → AGENT-MEMORY / Ch77

已读`Recall 与 Commitment 必须分开授权`整个本节：检索→activation→validation→bounded realization/ask/abstain，Memory owner不拥有外部副作用提交；该节最后2609.29545完整段已有“验证将改变后续选择的价值大于探测成本才recheck”，置信很高/很低不一定值得验证，刷新新版本、不用旧confidence授关键副作用。另`Verifier 输出必须带着校准边界进入Memory生命周期`整节明确verifier identity/domain/expiry与不可靠时保守不写；`Provenance必须进入read/action/repair`明确按action-risk threshold、依赖闭包execute/abstain/request evidence。

因此本次采用的action-conditioned verification VOI、校准verifier与abstain分责已被实际论点承载；论文固定p/r/κ的special-case阈值与depth2实用近似没有提供普适生产门，不复制该数值recipe。NC不声称书里已有原论文全部算法，只保本次可长期采用的选择原则；ToolSandbox/AppWorld harm及覆盖反侧留Report，不加Book/note。

### 30769 Herding → AGENT-MULTI-AGENT / Ch82

已读开篇/`什么时候分解有意义`，明确同错误文档/同模型互述不创造新证据；`Verification与Aggregation`要求生成评价隔离、独立evidence与保留disagreement；`同根报告可以帮助读懂证据，却不能按独立观察累加`整节以root与提取误差分解说明重复报告不提高source truth；`Memory拓扑不必等于Agent拓扑`两段明确共享池导致过早收敛/污染，局部pool＋受限摘要留多样性及代价。

本次可采用的“前人可见流量/累积推荐不是独立证据，可能产生自强化路径依赖”属于这些已有机制的局部受控反例。MusicLab歌词/推荐人口不是生产协作、也没有新去herd执行机制；不把有限13同质population和人类不匹配协议变普遍MAS规律。具体NC，不新建社会模拟小节或加机制同义段。

### 31355 Muffin → AGENT-MULTI-AGENT / Ch82

实际正文`Memory拓扑不必等于Agent拓扑`说明local pool owner、只交换受限摘要/反馈而非复制raw memory；`条件化机制分支`中2606.24437正文已有“不平铺全部history reasoning，按quality/diversity投影少量references”；`Coordination Tax`内MiroFlow两完整段要求冻结外围output rewriter/分开主体和完整pipeline，摘要加工不能独占协作因果，完整token/critical-path计费；`Agent数量应由边际信息价值分配`已有按任务难度分配与估计失准回equal-budget。

这些组合覆盖本次只采用的selective findings sharing、私有原始状态不自动广播与orchestrator/summarizer分账。Muffin异步共享摘要buffer是局部实现选择；其固定step不等固定token/latency、QA无tool反馈证据不足以产生新的durable执行/可靠并发合同，故不把“async”再造执行小节。不用Review notes的PACT声明冒充实际正文；确切buffer算法/41.9K结果仍在Report，NC不宣称书里已有该实现。

## 其余三项差额准备

31019/30612 Ch76与30635 Ch66实际承载段已读；只有更新切分边界写放大、per-query融合伤害/aggregate分离、spec与test隐藏依赖未由现有泛化声明具体表达，准备窄PRE。未写Book。


## 31019：更新边界写放大 → Ch76 窄PRE

Owner：AGENT-RAG / `books/part-07-agent/76-rag.md`，`Chunking 是信息边界设计`。实际已读该节完整上下邻段，以及Offline ingestion中revision/segment lineage、写放大和训练中模型更新的局部刷新段。已有“写放大”只给通用ingestion压力，局部刷新针对encoder训练漂移；二者没有解释冻结encoder下小内容编辑如何经chunk边界移动扩大新payload，因此不是同一差额。采用命题限于该边界压力与质量—重算联合验收，非推荐具体chunker。

操作：只在下列完整上锚与完整下锚之间插入一段，其他内容/marker不改。PRE待reader独核、root实际保存；本文件不是POST。

上锚（完整段）：

> 更合理的策略结合 document structure、semantic boundaries、overlap 与 parent-child retrieval。没有对所有语料通用的 chunk size。

拟插入完整正文：

切分还决定知识更新时的重算放大，而不只是一次查询的证据范围：即使encoder冻结，文档前部的小段插入也会移动固定长度边界，使未改文字落入不同payload而必须重编码。可在新旧revision间只复用严格相同的chunk输入，并将source/segment身份、chunker参数与encoder版本共同保存；评价同时测重编码输入token比例和相同检索预算下的质量，而不从原文编辑比例推算embedding费用。[相邻修订的受限对照](https://arxiv.org/html/2610.31019v1)支持这种边界漂移压力，不证明内容感知切分普遍最优：recursive与content-defined边界的成本排序随长度/语言翻转，失败项不能从分母静默删除，小recall差额的区间触零也不是等价证明。边界检测、比对、重编码、索引发布及质量回归全要付费，输入token重算率不等金钱或服务延迟；更新少时简单固定切分仍合理，复用身份或质量不稳时保留完整重编码和原始证据检查，不以少重算批准支持完备。<!-- source-family:SF-2026-ARXIV-2610-31019 -->

下锚（完整段；其后原有HiChunk source-family marker保持不动）：

> 固定小块适合局部问题，却可能把同一问题所需的多条证据拆散。文档内层级可靠时，可以先用小叶子匹配，再根据已命中的兄弟覆盖和剩余token预算，决定是否改向reader交付完整父段；这改变的是最终消费的原文范围，而不是让树节点获得事实权威。[HiChunk的受限分支](https://arxiv.org/html/2509.11552v1#S4)支持把检索粒度与交付粒度分开，但过粗的父层也会降低召回，末尾截断仍可能切掉合并后所需的证据，不能从层级完整或预算检查推导支持完备。评价应同时保留少量句子即可回答的问题与需要分散证据的问题，在相同context预算下分别看证据召回和最终答案；合成问题的长度、来源和模型筛选也在改变，不能把差额唯一归于证据密度。结构标注、边界模型训练、索引、原文展开与reader生成都付费，较低分块耗时不等全链更快。层级、证据支持或净预算不稳时，保留原文小块/hybrid与独立支持核验，不靠更大的父段补造缺失事实。

采用/反侧：严格payload复用、长度/encoder/检索预算匹配；保失败NA及recall不等价，成本仅token重算。完整来源机制/评价条件见ARXIV批C，不额外再读附件或扩日。


## 30612：融合平均增益与逐query伤害 → Ch76 窄PRE

Owner：AGENT-RAG / `books/part-07-agent/76-rag.md`，Query Pipeline。实际已读hybrid开篇及IRAKE邻段、两跳question/bridge连续路由迁移反退段、Exact Adaptive Fusion整段。后者的exactness是完整融合top-k身份，不是融合优于component；两跳路由说明特定权重迁移但没有区分全体aggregate gain与query-level强单路tax、排名/coverage两类失败。新增仅这条质量验收差额，不再引入一个“智能融合算法”。

操作：只在下列完整上锚与完整下锚之间插入一段，其他正文不改。

上锚（完整段）：

> Dense retrieval 擅长语义相似，lexical retrieval 对 rare identifiers、code symbols 和精确词更稳。Hybrid retrieval 常更鲁棒，但增加融合和调参复杂度。

拟插入完整正文：

Hybrid的平均收益不构成逐query的质量下限：融合改变相对排名，即使两路各自保留了相关文档，也可能把当前query较强一路的结果挤出前列；少量相关文档若已离开交付候选池，后续reranker更无法凭空恢复。应在相同输出k下分别报告融合相对各单路的收益/伤害、排名变化与coverage损失，再按目标语料和风险约束选权重，而不只比较全体均值。[受限多语料对照](https://arxiv.org/html/2610.30612v1)支持这一区分，逐query事后取较强单路只是诊断oracle，并非线上可用router；廉价特征路由跨语料未稳定胜过静态插值，cross-encoder也会修复部分同时新伤害另一些query。双路执行、融合调参、router/重排及独立答案支持核验均计费，较高平均检索分不批准每次回答。目标语料留出验证、相关性标注或路由净收益不足时，保留已验的固定融合或适合该workload的单路，不由平均增益强制所有query融合，也不由局部tax否定hybrid。<!-- source-family:SF-2026-ARXIV-2610-30612 -->

下锚（完整段；随后原有IRAKE marker不改）：

> 当外部库保存的是模型应消费的事实编辑时，先按参数知识把问题拆细，可能已经绕过了编辑对应的提问粒度。另一条受限路径先用原问题或后续改写粗召回编辑候选，让模型选择可用于引导的atomic question，再据此分解并做细粒度检索；事实级引导使用对应问题而非编辑答案，成功案例库则另提供完整解题记录作为分解参照。[IRAKE的受限对照](https://arxiv.org/html/2509.07555v1)支持这条检索先影响query producer的顺序分支，不等于改写参数或证明编辑必被正确使用：案例成功、检到编辑乃至清除回溯stack都只是控制信号，后续改写仍会传播前答错误。应保留原问题、编辑及案例来源/版本、引导选择、分解与实际使用支持，分别验收召回、答案正确及编辑消费；更多候选可能同时损害引导判断与最终答案，counterfactual集合的任一问成功率也不是开放知识真值。案例制备/索引、额外预检索、判断/重写/分解、精检索、回溯与独立回归全部计费，少输出token不保证净省费或完备终止。引导失配、来源不可信或预算不合时，保留原query、非引导分解与普通检索及独立答案核验，不由命中过编辑批准事实正确。

采用/反侧：七BEIR/五encoder等有限对照，oracle相对与always-dense相对的tax不能混称；冻结LOCO/5fold调参与测试隔离，不能把ground-truth最强component当部署输入。Source不用hardware/SLO作该质量论据；无可靠廉价router/无reranker全修复保证，保hybrid合理性。


## 30635：可见规范与oracle隐藏依赖 → Ch66 窄PRE

Owner：PLATFORM-EVALUATION-SYSTEM / `books/part-06-ai-infrastructure/66-evaluation-system.md`，`Evaluation Identity 必须包含 Harness 与 Environment`。实际已读该节完整起始状态/协议权限邻段及规范强度/测试覆盖相关段：现有identity解释model/harness/environment/scorer变化，NL2VC/Verus等规格强度不证明oracle额外名称/路径/literal能否由原spec/base推出。差额是task—test依赖可推导性的上游合同，不是新judge或又一句“测试不等真值”。

操作：在通用identity段之后、environment起始状态分支之前插入一段。完整上下锚如下；其他内容不改。

上锚（完整段）：

> 可复现的评估身份至少应写成 `model × benchmark × harness × environment × scorer`。Harness 负责适配与控制流，Environment 负责可执行状态，Scorer 只拥有从轨迹到判断的映射；聚合分数之前必须保存原始 trajectory 与 component-level receipt，才能区分模型退化、adapter drift、工具故障和评分变化。统一协议可以复用执行与观测设施，但每个 adapter 仍需证明语义等价。

拟插入完整正文：

评估身份中的task specification与test oracle还必须对齐：隐藏test本身合理，但若test要求的名称、路径或literal既未在可见规范披露，也不能由起始代码/环境推出，失败就混入了对隐藏约束的猜测，而不只测实现所声明需求的能力。可逐项追踪oracle依赖到可见来源，并用reference依赖的单名遮盖等有界干预辅助定位缺口；静态scanner只提出候选，仍需独立人工核对可推导性。[一项五语言受限审计](https://arxiv.org/html/2610.30635v1)支持这种specification–oracle gap确实存在，但检测precision/recall并非完美、召回样本小，受影响case失败较多也不把全部失败唯一归于缺口；剔除后的总体排行基本稳定，更不能宣称所有benchmark失效。应共同保留原spec、base、reference/test与审计版本，分别报告缺口切片及完整人口；依赖提取、干预运行、人审和重新评分全付费。缺口确认时优先公开必要约束或隔离该切片并重验，不为提高分数擅删有效test；可推导性未闭时保留Unknown与原分数上下文，不让一次pass或fail独占通用代码能力结论。<!-- source-family:SF-2026-ARXIV-2610-30635 -->

下锚（完整段）：

> Environment身份还须包含起始状态，而不只声明同一container或request。可保持原任务、隐藏verifier、harness与预算不变，另从前任已宣完成却未过验收的持久改动重建环境，再作无前任trace/失败提示的blind continuation；[受限残留起点评价](https://arxiv.org/html/2610.25899v1#S3)表明，干净起点能完成并不保继承后仍能完成，排名也可能改变。该人口按前任提交失败筛选，不是自然handoff频率；多个残留先在task内平均，不能将state数当独立任务数。高比例已过tests、读过diff或保留更多旧代码都不认证原需求已满足，留下同failedtests也只支持acceptancebias候选解释，未证明重启一定更好。前任尝试、patch/process重建、重验、续跑与完整终验都计费；无法确认残留身份/可用性或独立验收不足时，保留clean-start参照、原快照与独立需求核对，把未完成留作未决，不由前任completion声明批准继续发布。<!-- source-family:SF-2026-ARXIV-2610-25899 -->

采用/反侧：static五语言审计；reference单名遮盖126/128编译失败是依赖干预，不将其等同所有Agent失败原因。heldout独立blind核验precision58/65与recall13/14、小样本区间宽；35public runs matched比较保混杂，删受影响test不推翻总leaderboard。上述数字只供核对采用边界，不拟堆Book；本文只采用上游spec完整性与独立核验原则。

## C6作者边界结语

本批六项完毕：31446/30769/31355为具体NC，31019/30612/30635为三项窄PRE。仅AUTHOR_C追加，没有修改Books/Report/State/REVIEW，未stage/commit/push/index；PRE都仍待reader独立核和root实际读锚/保存，不自签POST或DAY。已核Source复用本日批C，不第三读、不扩大候选或日期。



