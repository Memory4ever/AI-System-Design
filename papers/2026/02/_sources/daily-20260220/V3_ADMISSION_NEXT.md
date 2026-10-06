# 02/20 第二批准入请求：实际完整题摘语义切片

阅读依据：本日inventory的完整题摘；它们保留旧公开字段用于定点恢复，不继承旧评分/逐项队列。四组当前官方Atom query成功（system12/language127/multi37/agent48，start0/max200，均total小于200）；current revision和Submitted只作发现与下界，不当当窗版本。旧宽表相关标题作补检，未逐篇强制处理435条。

以下潜力连到具体选择，尚未授日期/必要证据/Books。标准默认仅新增命题评分，不以主题关联、已有owner或成熟原则加分。

## B1 模型、训练、推理与表示潜力

| ID | 新增命题与改变的选择 | 拟评分 |
| --- | --- | --- |
| 15950 | 同视觉encoder的text-symbol比filled-square定位优→空间能力评价须拆文字识别媒介混杂，不把图像输入一律当native geometry | 2+1+2=5，反侧深入 |
| 15997 | exact-v1粗difficulty相关不等fine timing预测，within-class/swap失效与原Pythia外部probe无一致前兆→几何monitor须绑定probe人口与checkpoint窗口；不借later新增hard-task证明 | 2+1+2=5 |
| 16008 | acoustic/linguistic encoder评价排序分裂且关联audioLM→选择audio encoder须按信息类型而非总榜 | 2+2+2=6 |
| 16054 | answer-informed oracle暴露token-ranking层间方差→prefill token选择应比较跨层聚合且oracle仅事后评价 | 2+1+2=5 |
| 16065 | recursive contaminated training收敛由内在率和fresh data比例较慢者控制→synthetic数据占比应和轮次/估计误差联合定界 | 2+2+2=6，必要理论 |
| 16066 | information-asymmetry多turn可验证任务训练feedback ICL并跨域迁移→交互反馈利用不应默认靠singleturn能力涌现 | 2+2+2=6 |
| 16069 | perfect retrieval下64k patch仍失败、agent成功主要短context→nominal容量不可直接推codebase usable reasoning | 2+2+2=6，反侧深入 |
| 16075 | analog MVM+Boolean PUM完整非MVM计算驻留memory→LLM加速可否避免CPU往返须检验混合外围成本 | 2+2+2=6 |
| 16086 | learnable codebook配diversity+peakedness soft-hard退火保持utilization→固定geometry并非避免collapse唯一选项 | 2+1+2=5 |
| 16092 | DecoupledRoPE控制position/content后仍长序列退化→two-stream优势需解释semantic/structural排序冲突 | 2+1+2=5，设计反侧深入 |
| 16093 | teacher/student split-context shared-token KL无需生成→持续知识适配可比较知识学习与posttraining保留的资源折中 | 2+2+2=6 |
| 16100 | 原abs标题/摘要不一致（官方也如此）但给出动态pipeline migration机制→一次core核正文identity与<50ms迁移状态条件 | 暂不评分 |
| 16132 | cross-inference cache attention使用语义相关prompt旧视频latent→生成cache从单request步复用拓展跨request，须保质量/污染边界 | 2+2+2=6 |
| 16144 | 请求特定modality deletion并输出certificate→是否有实际可撤销参数保证而非缺模态鲁棒性，一次core定界 | 暂不评分，安全 |
| 16154 | truncated speaker trace由listener执行给reward+masked SFT regularization→CoT可执行性训练与faithfulness/accuracy取舍 | 2+2+2=6 |
| 16165 | planner/executor层级returns与HAE无偏/降方差→长轨迹credit需时间抽象而非flat GAE | 2+2+2=6，必要理论 |
| 16189 | activation-selected localized module移植无需训练→task-localized capacity可否transfer而不整网merge | 2+1+2=5 |
| 16197 | target modality collapse+curvature masking+hypergradient认证→鲁棒性是否真有新学习机制或只有术语，一次core | 暂不评分 |
| 16198 | Doob correction模拟实现non-differentiable reward transport→guidance不必训练或reward梯度但须近似误差界 | 2+2+2=6，必要理论 |
| 16229 | multi-entity factor各自latent-action和nextstate→单一scene动作接口不足时可选factored dynamics | 2+1+2=5 |
| 16284 | perKVhead attention-output/mass匹配，部分闭式→context latent compaction不必昂贵end2end优化但query泛化需验证 | 2+1+2=5 |
| 16299 | 去除crossencoder冗余interaction保OOD质量→RAG reranker质量/计算取舍不只是减少候选数 | 2+1+2=5 |
| 16301 | sequence learner通过co-player diversity隐式学习aware而无规则/快慢分离→协作机制是否适用于model-agent而非泛MARL，一次core | 暂不评分 |
| 16305 | frozen全层convex-gated probing缩小fine-tune差异并暴露representation质量→encoder选择避免readout优化混杂 | 2+1+2=5 |
| 16334 | no mask/AGM/oracle mask比较与thinking交互→audio推理收益取决于source separation质量 | 2+1+2=5 |
| 16340 | decaying LR同质模型下momentum steepest descent margin KKT及Adam无epsilon→优化器选择改变隐式norm而非只speed | 2+1+2=5，必要理论 |
| 16343 | codec resynthesis作bonafide/spoof标签改变检测评价→codec表示与合成来源不可用一个标签混淆 | 2+1+2=5 |
| 16412 | 稀疏RGB+compressedmotion去噪且features线性压缩→longvideo表示预算不必full decode全RGB | 2+2+2=6 |
| 16438 | targeted gender DPO在ambiguous context造成其他属性bias spillover→alignment公平不能用aggregate单属性验收 | 2+1+2=5，反侧深入 |
| 16449 | embedding hubness使distance-metric错判，multiscale GICDM校邻域→generation质量度量需检查表征几何失真 | 2+1+2=5 |
| 16455 | pixel localization可视化后re-input refine再decode→visual错误反馈可以回到pixels而不只text自纠 | 2+1+2=5 |
| 16456 | LoRSum proximalALS=implicit blockpower，scaled diagonal KFAC避免fullSVD→LoRA优化器可逼近投影full step但memory/compute成本需比较 | 2+1+2=5，必要理论 |
| 16469 | source-language translationese lexical diversity/typology分别关联perplexity/grammar→syntheticmultilingual数据不能只用翻译quality选 | 2+1+2=5 |
| 16473 | C-RASP→Lustre/SMT验证与localsearch合成→Transformer program可检验形式语义但不是trainedLM等价保证 | 2+1+2=5，必要理论 |
| 16488 | solicitation+feedback学习的SML跨域与underspecified对话→区别回答能力与主动收集缺失信息的trainable skill | 2+2+2=6；与16066家族关系待核 |
| 16490 | depthgrowing和looping共享depthsignature且可组合、mathcooldown影响→两种compute扩展不必视互斥机制 | 2+1+2=5 |
| 16498 | analyticaldiffusion后验support随SNR收缩、动态goldsubset及近似界→无需每步full-data scan | 2+1+2=5，必要理论 |
| 16500 | persistenthomology紧致/稳定softprompt对应收益，TSLoss约束训练→小参数适配可否由结构regularizer改变收敛，一次core | 暂不评分 |
| 16511 | 完整AB为独立humanoid fall reactive RL teacher/student，没有foundation/VLA或LLM训练推理接口；不能仅凭可映射Ch26准入 | 范围排除，不评分；root完整AB独校 |
| 16570 | quadratictilt rank/sign决定采样tractability，rank1 negative也可难→rewardguidance不是任意lowrank都高效 | 2+1+2=5，必要理论 |
| 16587 | textCoT在SID预测削弱history使用并随长度加剧→混合text/discrete模型的thinking可能伤条件信息 | 2+1+2=5，反侧深入 |
| 16596 | controlledcanary插入前后多checkpoint审计比finalsnapshot更强→privacy审计须覆盖版本sequence | 2+2+2=6，安全深入 |
| 16601 | freshdata比例与scoreerror控制多轮diffusiondivergence上下界→syntheticretraining drift应看累计而非单轮loss | 2+1+2=5，必要理论 |
| 16608 | 一次core/root独校：IG×gradient成熟融合与插删AUC局部，无独立fusion控制或新成立条件；不能由估计器名称/美观或局部指标授因果faithfulness增量。原拟准入已具体纠正，证据保留于V3_CORE_DECISIONS。 | 贡献排除，不评分 |
| 16609 | multi-vectorfullpretrain较smallKD强；supervisedfirst省unsupervisedbudget→RAGencoder训练recipe不能默认single-vector转KD足够 | 2+1+2=5 |
| 16642 | adaptive decoupledWD破坏NC0必要条件，momentum效应→neuralcollapse不可外推optimizer-independent | 2+1+2=5，必要理论/反侧 |
| 16660 | multilingualpromptvariants collinearity loss无需targetresponse监督→跨语安全对齐可选representationconsistency而不只pairlanguage训练 | 2+2+2=6，安全深入 |
| 16675 | surface-normalobservations/replay/augment改worldmodelclothsim2real→具体收益是否可归因表示与适用条件，一次core | 暂不评分 |
| 16682 | observer-centriccamera pose/motion任务发现partialgeometriccues不能coherentgeometry→VLM spatial评价需要egocentricframe控制 | 2+1+2=5 |
| 16687 | 64modelIsoFLOP discreteaudio data/modeloptima与semantic/acoustic/textrecipe→audio缩放与text-firstbackbone不同预算选择 | 2+2+2=6 |
| 16689 | 控制data/sample/representation/downstreamcompute后OC难compositional优势、dense充足资源追平→选择objectbias依约束不绝对优 | 2+1+2=5 |
| 16697 | perfectretraining删除序列可重建undeleteddata→unlearning定义应保护保留集不只模拟删后重训 | 2+2+2=6，安全理论深入 |
| 16698 | causalhierarchy/CRL把observational/interventional/counterfactualclaims按identifiability界定→interpretability必须匹配assumption和claim，一次core确定不是纯taxonomy | 暂不评分 |
| 16702 | highlevelprinciple SAP多route允许renewedvisualconsult comparabletokenbudget→VLMtesttime scaling不应只更长textCoT | 2+1+2=5 |
| 16704 | fastweightNSP selfsupervisedreward+entropypositions/GRPO→fixedstatememory训练应优化seqcoherence而不只NTP | 2+2+2=6 |
| 16705 | IK residualreference+neuralforwardmodel+replan减少EEerror→modularVLM理解/EEcontrol之间具体error接口 | 2+2+2=6 |
| 16710 | egohumanaction数据scale与robot结果关联、humanrobotalignedmidtraining→embodimenttransfer瓶颈在alignment而不只更多humanvideo | 2+2+2=6 |
| 16712 | canonicalURDF/parameterizedmorphology同时统一representation/actionspace→crosshandpolicy应有形态接口而非单fixedhand | 2+2+2=6 |

## B2 Agent与评价潜力

| ID | 新增命题与改变的选择 | 拟评分 |
| --- | --- | --- |
| 15983 | solverfeasible不等semanticallycorrect；parameterperturbationbehavior无需groundtruth→verification要扰动semanticexpectation而不只execution | 2+1+2=5，设计反侧 |
| 16106 | neutralalgorithm中间spec的pairedtranslation改变compile/runtimefailure分布→在语言迁移选择先spec后code而非direct | 2+1+2=5 |
| 16138 | nearverbalquestiontimegazefixation最能消ambiguity→multimodalinteraction应对齐signal时间而非只更多图像 | 2+1+2=5 |
| 16149 | controlledportraitediting发现soft-erasure/stereotypereplacement随sourceidentity异质→identitypreservation评价不能平均promptcompliance | 2+1+2=5，反侧 |
| 16173 | preactionclarify+postactionfeedbackdualchannel针对userdrift比singlechannel→personalizationmemory更新需pre/post证据不同责任 | 2+2+2=6 |
| 16179 | traininghighfidelityenterpriseenv跨benchtransfer，但未分离environmentproperties→一次core查controlled新增训练/奖励choice，不自动收新benchmark | 暂不评分 |
| 16192 | storethenextract概念有simpleexperiment→一次core查新增retrieval/retention边界而非已知完整日志原则 | 暂不评分 |
| 16200 | coreference测量定义分歧和ranking冲突/上下文扰动→是否只是传统NLPvalidity泛论还是LM评价具体反例，一次core | 暂不评分 |
| 16241 | 原完整题摘潜力记录保留；当前官方明确complete withdrawal，重大方法差异影响有效性/复现，root实际独核排除 | 原准入评分失效；不评分/候选/Books，原证据与撤回依据见V3_EVIDENCE_SEVENTEENTH |
| 16304 | maliciouspackage判别好但line-indicator差/hallucination，复杂度主因→code安全judge只能triage不能直接归因机制 | 2+1+2=5，安全深入 |
| 16346 | sequentialmisuse time-to-firstjailbreak/RMJD与attacklanguage不单调→agentmisuse测量需turn exposure和taskcompletion | 2+2+2=6，安全深入 |
| 16424 | observableevents术语认证+coreguard保证disagreement/recert→semantic一致需要经验支持集而不等协议格式正确 | 2+1+2=5，必要理论 |
| 16429 | executiontrace schema/state/dependencytrainedclassifier替closedsethead→agentshortlist不必每次generativecall但coverage/drift须核 | 2+2+2=6 |
| 16485 | orchestratorcalibration/selfassessment profiles异构toolmodel选择→一次core查selection校准改变而非异构committee均值 | 暂不评分 |
| 16493 | credibility/decay/conflictnetwork reweight+abstain，controlledtextvisioncontradiction视觉placebo→memory检索要按可靠性非相似性，须查具体新score条件 | 2+2+2=6 |
| 16610 | BTsigma jointinferranking/judgereliability无需humansupervision→juryaggregation不能默认equaltrust或rawprobability一致 | 2+1+2=5 |
| 16639 | persuasion/resistance弱相关和asymmetric，commitment/verification行为→一次core检查不是只新gametask排名 | 暂不评分 |
| 16653 | Skill selection随modelcapacity和thinkingGPUcost失效→resourceconstrainedagent不能默认proprietaryskill效用外推smallLM | 2+1+2=5 |
| 16662 | naturalstrategy→code隔离parsing，hundreds/selfplay/imitation坏collectiveequilibrium→agent评估不能只单agent胜率 | 2+2+2=6 |
| 16666 | 12metrics拆consistent/robust/predictable/severity，15models能力提高可靠性只小涨→performancegate须拆accuracy/reliability | 2+2+2=6，设计反侧 |
| 16671 | CFG/operationmap validatedhelpers pathtargettests→一次core查减少invalidsignature的具体grounding机制/消融，不以TDD+CI改名收 | 暂不评分 |
| 16699 | environmentstateprior显式costuncertainty tradeoff→agent探索停止需要可校准环境prior而非固定RLpolicy | 2+1+2=5 |

## B3 代表性明确排除（实际完整题摘）

- 16038：贡献为把heuristicdesign已有evaluation/feedback/update模块化，并给出CO四域均值；摘要未给新模块机制、新的可控适用条件或失效边界，不能因叫forward/backward而收。
- 16085：语言统计/falsebelief输出用于人类社会认知理论，未新增LM学习/系统设计mechanism或可改变能力评价解释的控制；不因模型41个收。
- 16105：GPS任务数与地域/geometry排名及fine-tune已知tradeoff，未给会改变当前model/system解释的新混杂机制；新task/domain本身不收。
- 16111：Pinterest business prevalence共享calibration系统，不是foundationmodel能力/训练/推理/平台/Agent机制；LLM只做标签供业务统计，不借Evaluationowner引入。
- 16131：ECDF cosine-reference分布与kmedoid QA显示不同temperature/persona分群，未指出原能力或design结论被误判，换summarymetric本身不收。
- 16201：完整摘要明确synthesizes prior taxonomy四轴，未新证据修正longtail机制；不收综述收纳。
- 16238：foundationimage模型fine-tune边缘检测及densityguidance只改善下游edge任务，未给生成模型本身新mechanism或通用适用条件。
- 16467：English/Hindi真实exam新题和CoT/language排行，未发现evaluation混杂或新设计选择，不因bilingual现实重要收。
- 16512：FoT把ToT/GoT/ProbTree+HPO/parallel/cache组合成framework，未给新执行正确性/效用条件，只speed/cost/taskscore；不因orchestration术语收。
- 16640：完整题摘明确提供领域训练GPT2与GGUF8bit消融，报告模型大小约下降74%/accuracy下降约3.5%，不能称没有任何precision对照。贡献排除仍成立：既有GGUF8bit用于领域模型的有限质量/容量取舍，未新增执行/量化机制或改变已有设计判断的成立条件；不因small model或法律领域拒绝，不扩大到全文队列。root完整题摘分层负侧独核后本条理由已纠偏，保留原AB。

## 早Submitted潜力日期保留

15843/15846/15847/15855/15858/15863/15864/15868/15870/15872/15873/15875/15889/15892/15894/15895/15896/15897/15914/15919/15927：均实际读完整题摘，存在capacity、tokencompression、steering、runtime、state、diffusionlatent、embodiedgrounding、privacy或evaluation潜力，但Submitted下界早于本窗，登记上界不能唯一确定firstpublic。待精确abs/公告证据只定点恢复，不正面采用，不把延迟登记当窗证。

新官方Atom另发现16080/16113/16136/16177/16612与16736/16740/16741/16742/16745/16746/16760/16763及若干3月ID：只作新线索，尚未完整exact-v1题摘/日期，不因querySubmitted落窗纳确定候选。按最小identity/date恢复，不扩他日任务。
