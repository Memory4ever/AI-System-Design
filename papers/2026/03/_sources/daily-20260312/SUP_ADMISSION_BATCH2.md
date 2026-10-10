# 03-12 题摘语义第2包

作者实际逐项完整exact-v1题摘/当前comment/history读完24项，原件SUP_EXACT_BATCH2.json；metadata取回不作Evidence。root随后实际完整24题摘/当前信号独立校准，原19窄潜力保留、09938/09161具体EX通过、10098/10068日期跨日保留；09452根据必要core撤销原EX。因此本包20窄潜力、2具体EX、2必要日期保留；准入不是日期或Evidence通过，尚未完成必要Source/Books的均普通待办。

日期：以下19潜力的arxiv.content owning/findable DOI registered均03-11UTC，exact-v1 Submitted Mar10 before18UTC配官方availability noadvance+最早Tue20EDT下界，同一BJT03-11日夹证；不是registered单独公开。09452 accepted TMLR、09200 ICLRworkshop等先稿信号须定点核；后续acceptedICML/ACL/SLT等不能单独证明早于arxiv。原报告候选不重算。

| exact-v1 ID | 原约束 → 实际增量 → 如果成立改变选择 | 状态 |
| --- | --- | --- |
|2603.09884|旧政治劝说结论/信息型prompt收益未跨新模型验证 → 两surveyN19145/七模型有信息prompt模型依赖及方向反转 → 不跨模型继承persuasion风险/策略有效性|potential；PLATFORM-EVALUATION-SYSTEM，作者风险实验非社会通用保证|
|2603.09865|独立选层或选数据忽略二者交互 → gradient aligned逐层选数据与稀疏更新 → 比较layer-data联合PEFT而非统一过滤|potential；TRAIN-LORA|
|2603.09815|Transformer隐表示受label-irrelevant噪声 → learnable restriction/prolongation pseudo-projector非严格orthogonal → 可核验噪声抑制分支，不授MG到LLM通用性质|potential；MODEL-TRANSFORMER-LAYER|
|2603.09803|binary RLVR奖励把偶然正确trace同等处理 → 自身ICL demonstration utility/EvidenceGain隐式重权 → 比较自监督推理质量proxy与externaljudge|potential；TRAIN-GRPO|
|2603.09714|单audio评价掩盖多input scaling/顺序脆弱性 → multi-audio控制及audio permutation selfconsistency → 按输入数量/排列验收audio aggregation|potential；MULTIMODAL-REPRESENTATION|
|2603.09678|常规code高分可能依赖语言曝光 → 五esolang文档+interpreter任务与主流code差距 → 不凭稀有repo数量直接断言genuine reasoning，但值得核混杂后修评价|potential；PLATFORM-EVALUATION-SYSTEM|
|2603.09453|Bayesian全参数开销大 → 只把MoE expert routing logits/temperature随机化 → 对比routing uncertainty与确定性router，不外推全模型Bayes|potential；MODEL-MOE|
|2603.09331|环境reward稀疏 → taskdescription与interaction embedding completion dense signal → 可核验具身rewardshaping/真实success与semantic proxy分账|potential；MULTIMODAL-EMBODIED-VLA|
|2603.09232|CD平均收益未识别错误族 → transition matrix区分absence/guessing可修vsreason/confident错难修 → 按baseline error profile选择CD|potential；MULTIMODAL-REPRESENTATION|
|2603.09215|交错speech都full-depth昂贵/confidenceexit未必有效 → fixedintermediate speech＋periodic full-depth refresh → 比较modality-aware exit schedule与text confidence heuristic|potential；MULTIMODAL-GENERATIVE-PARADIGMS|
|2603.09206|VLMselfevolution仍需seedimages → proposer/coder-renderer/solver三角色GRPO闭环 → 比较执行反馈生成视觉数据与双角色seed路径|potential；TRAIN-GRPO|
|2603.09160|open-endedcaption不可用确定verifier → 候选committee→sample-specificrubric→LLMjudge多维reward → 比较rubricidentity与holisticreward，不把judge当真值|potential；TRAIN-RLHF|
|2603.09117|RLVRaccuracy与confidence calibration混合可能冲突 → 理论gradient conflict＋decoupled DCPO → 比较reasoning与calibration分离目标|potential；TRAIN-GRPO|
|2603.09222|context pruning按孤立相关性易失answerclue → leaveoneout clue decrease＋composite margin encoder → 比较queryconditioned必要句压缩；v1LooComp不混currentEnComp|potential；AGENT-CONTEXT|
|2603.09216|prefill/decode cacheability与weightlayout不一致 → DDB小cacheablebuf＋OWR swizzledcopy → 比较一份PIMweight资产与phase转换成本|potential；INFER-GPU-MEMORY|
|2603.09205|emotion作为label未验LLMreasoning表示漂移 → controlled humancontextattentiongeometry＋emotionalregularizer → 核proxy/correlation与条件泛化，不把emotiontruth化|potential；MODEL-SELF-ATTENTION|
|2603.09200|reasoning改进的风险不能靠任务分数自证 → RAISE情境识别风险/配对探针命题 → 保留可检验风险切片，不把参数共享推出跨域单调改进|potential；root已实际精确v1§6完整boxed命题/AppC.2–C.4/F，中心proof的共享参数→跨域性能单调、C.3由≥0转>0且预设旧结论不丢均不成立；MirrorTest亦混泛化知识，行为差异不独证内部SA。中心Disputed隔离，不采推理必然增加SA/RLHF普遍不可能有效；作者仅剩必要先公开去重/评分，不重复整篇|
|2603.09185|negation/exclusionquery无法靠普通similarity → 分positive/negative优化queryembedding contrastiveobjective → 比较不改encoder的negationretrieval路径|potential；AGENT-RAG|
|2603.09046|TrustZone保护LLMinference隔离过死 → flexibleprotectedpage/NPU＋securepipeline/multimodelscheduler → 比较资源交接与trustboundary成本|potential；PLATFORM-PRODUCTION；安全必要深入，currentv3无明确withdraw/纠错note|

## 具体EX

- 2603.09938：FUSE四维综述分类与工具/挑战总结，完整题摘未给新增可核的merge机制、混杂反证或适用边界，不能以modelmerge主题映射入选。日期03-11线索不影响EX，无必要日期请求。
- 2603.09452（原EX理由保留，已撤销）：原判断只看CTI领域triage/search/draftingbenchmark＋analystmetrics及nuancedexpertise不足，未识别具体评价排序反例。root实际exact-v1§1/AppE.1发现稀疏summary的ROUGE/BERTScore较高但analyst偏好详细contextual summary，故改为窄potential：lexical/embedding proxy与用途评价排序可能相反，若成立改变评价目标与人工对照选择，而非将CTI workflow当Agent贡献。首公开另有TMLR11/2025官方PDF首页线索，本日归属尚不授；定点恢复见SUP_FIRST_PUBLIC_RECOVERY.md。
- 2603.09161：用不完美LLM生成RTL学习netlist表示，新增有效性条件属于电路representation/边界识别/组件分类，不改变LLM生成机制或为大模型服务的kernel/编译执行；不通过TRAIN-DATA/PLATFORM-EVALUATION映射绕范围。领域价值不否认，日期不影响EX。

## 必要日期保留

- 2603.10098 CSRO：LLM生成code policy替RLoracle具有potential，但owning/findable upper03-12与03-11lower跨日，AAMASextendedabstract接受另有先稿线索。必要实际announcementday/公开authorpaper未得，不评分，不采用。不是只因Submitted17:37落机会区间就确认03-11。
- 2603.10068 ADVERSA：continuousroundguardrailtrajectory/triplejudgereliability与attackerrefusalconfound有potential，v1完整AB保留；owningfindable upper03-12跨日，必要announcementday缺，不评分。currentSERA接受本身非先公开证据；不将15conversation结果推广安全保证。
