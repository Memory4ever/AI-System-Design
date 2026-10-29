# 2026-02-19 增量首批准入校准（作者提案，待非作者）

补充窗口 BJT 2026-02-18完整自然日，原67候选/评分/日期/旧09:00窗口/有效Source与Books冻结。完整原版baseline94359bytes与只读index逐字相同（初次多一空行已纠正，未截断）。当前四窄主题32/4/15/8命中，均start0,max100,total=rows；跨主题并旧身份去重后31个新完整题摘（见arxiv-narrow JSON），其中摘要来自当前API的身份线索，不授权v1采用；拟采用前查精确v1。已有同身份实际有效筛选复用，不将旧宽364库存变队列。

## 拟继续（潜在贡献；除EVMbench外必要公开日尚未成立）

|身份|原约束 → 原文新增 → 重新考虑的判断|
|---|---|
|[EVMbench](https://openai.com/index/introducing-evmbench/)|审计judge/编译通过不等实际安全 → detect/patch/exploit分别采用审计标签、functional+exploit测试、隔离链状态交易重放 → 不能以报告中的漏洞命中授现实可利用性，时序/链范围单独交代。Feb18官方正文，旧RSS00Z为08BJT，现补充自然日内。|
|[15136 Universal priors](https://arxiv.org/abs/2602.15136v1)|预训练分布固定似乎不能未知分布适应 → Poisson EB universal prior与posterior contraction/长度泛化界 → 有条件推断适应不等训练动力学或任意Transformer保证。|
|[Thin Keys 2603.04427](https://arxiv.org/abs/2603.04427v1)|Q/K selection与V transfer共维未必必要 → low-rank key并吸收到Q的分工 → cache降维质量与函数逼近须核精确v1、必要日期；current v4不冒充本窗版本。root指出首包漏路由已补，不扩旧库存。|
|[15283 Complex-Valued Unitary](https://arxiv.org/abs/2602.15283v1)|规范保持几何不自动校准 → 同backbone分类head+Born读出反侧/OOD与sentiment负侧 → 分开表示几何、readout与有效校准；小模型不误排。|
|[15353 NeuroSymActive](https://arxiv.org/abs/2602.15353v1)|prompt整图/纯符号搜索各有成本 → differentiable软统一/path评价+value-guided探索 → 可保的模块贡献/lookup成本需核，不因 KG 场景直接关闭。|
|[15368 GMAIL](https://arxiv.org/abs/2602.15368v1)|generated images直接替real会混shift → 先作为独立modality做latent alignment再训VLM → generated数据收益的条件含domain接口，不只增加样本。|
|[15514 DependencyAI](https://arxiv.org/abs/2602.15514v1)|AI文本检测跨域失真 → dependency-only基线与generator-specific过预测 → 新检测信号可核，不能把可解释性当跨域有效。|
|[15552 Latent Regularization](https://arxiv.org/abs/2602.15552v1)|boundary-test输入未必有效/多样 → mixing+binary search与random truncation三轴对照 → validity/diversity/fault detection不同，局部负载也能改具体评价选择。|
|[15586 Uniform error bounds](https://arxiv.org/abs/2602.15586v1)|dependent-data quantized动态模型泛化不能借iid → slow block/fast spaced-point界由encoding bits控制 → 若证明成立可改worldmodel/learning quantization的统计条件，但不直接外推LLM执行精度。|
|[15336 Digital Logic](https://arxiv.org/abs/2602.15336v1)|学生感知有用不等技术正确 → 10题24学生与独立答案judge对照，顺序问题template失配 → 教育场景的局部评价反证不按领域泛泛关闭，但不授一般能力因果。|
|[15388 CoverAssert](https://arxiv.org/abs/2602.15388v1)|单passassertion/一般feedback没定位功能漏点 → AST signal+semantic聚类回映规格，驱动uncovered-point feedback → 覆盖代理与semantic/assertion正确性分开，待核模块收益。|
|[DART 2603.12269](https://arxiv.org/abs/2603.12269v1)|固定exit阈值不看输入难度/联合策略 → difficulty估计+DP阈值联合，ViT准确率损失17%反侧 → early-exit质量成本须模型/workload限定；不因旧CNN或局部反侧关闭。|
|[DreamZero 2602.15922](https://arxiv.org/abs/2602.15922v1)|semantic VLA不足新motion → pretrained视频diffusion联合future/action与closed-loop优化 → world/action耦合与实时控制预算需核；Submitted不授Feb18公开。|
|[VideoSketcher 2602.15819](https://arxiv.org/abs/2602.15819v1)|静态生成无stroke时间结构 → 合成几何学习ordering、七例手绘学习style两阶段 → temporal/appearance训练信号解耦，不能只称现有video模型新应用。|
|[Alignment Iatrogenesis 2603.08723](https://arxiv.org/abs/2603.08723v1)|English-only安全测量可能漏语言×约束模式 → visible/invisible censorship与multi-agent语言对照 → 潜在局部评价反证可核，心理学标签不能先当安全真值。|
|[EarthSpatialBench 2602.15918](https://arxiv.org/abs/2602.15918v1)|spatial视觉QA混表示 → textual/overlay/coordinate与拓扑/距离任务对照 → 若确有表示控制反侧可改评价，不只因为地理场景/benchmark名排除。|
|[15724 Navigable retrieval](https://arxiv.org/abs/2602.15724v1)|候选过多增加navigation歧义 → episode exemplar+step imitation候选pruning，各自消融 → 候选召回/剪枝上限与LLM推理分责，待核实际机制。|
|[Solidity 2603.13239](https://arxiv.org/abs/2603.13239v1)|reasoning提示提高recall未必质量 → CoT/ToT recall↑precision↓ → 有限400个contract的decision-regime反侧可改prompt评价，领域不独自决定排除。|

## 具名代表排除（贡献前关闭，不为其追日期）

- 15159 AID-MAE：inherent+augmented masking不进encoder是MAE成熟masked-input训练迁EHR，仅临床结构/任务指标，未给通用模型机制失效或新条件；不是见EHR就排。
- 15259 Generative Proactivity：哲学ignorance/proactivity设计position，题摘无可验证干预机制或新可靠性条件，不因Agent关键词准入。
- 15236 BindCLIP、15451 Molecular：科学virtual-screening/药物优化是暂缓AIforScience，不经representation owner绕回。
- 15553 RUVA：vector删除“ghosts”的前提不成立，graph可编辑不自动right-to-forgotten；题摘仅图curation架构/demo宣称，未给删除依赖闭包或新验证机制。若root认为该负向争议信号需定点core，将重开本项。
- 2603.10006 TOBA-LM：GPT2+现有Engram ngram组合与训练步数宣传未指出新机制/分账条件；不是因为区域语言关闭。
- 2603.10007 GATech：E5 pooler现有选项shared-task比较和长度混杂观察，无改变当前具体机制选择的新增识别；不是负结果一律关闭。
- 15578 Depression、15740 MRC-GAT：clinical symptom/AD诊断，现有crossattention/copula/metarelation组合，领域指标未构成通用机制。
- 15750 UrbanVerse：区域图random-walk序列与task条件diffusion城市预测组合，未改变当前基础模型的具体解释/设计。
- 15820 Simulation TTA：D-optimal存统计用于高维物理仿真/设计优化，题摘贡献仍是暂缓科学应用，无通用基础模型独立机制证据。
- 15650 CEMRAG/2603.16876 MARL-Rad：医疗影像/临床报告的concept/RAG、region-agent RL组合只支持领域指标，暂缓科学应用。
- 2603.04425 Cellular：通信网络部署分类，不是大模型训练/推理资源机制。

## 停点

续跑差额：ThinKeys漏路由已补exact v1，集合现在为31arXiv=17潜在贡献日期保留+14EX，另EVMbench1确定机构家族。root已实际校准31完整题摘、RUVA必要安全core、EVM日期准入及必要Source/actual owner已有覆盖PRE。NeuroSymActive只补决定准入事实的§3.1–3.4/Algorithm1，看到frozen-LLM soft prompt接口与inner搜索/outer人审/human cost分工，仍因必要公开日隔离，不采用性能或理论保证。本提案的首包遗漏与后续纠正保留，不扩库存；以下是当时停点，不代表当前待办。

当前是准入校准提案，尚无全部日期/必要source/Books/DAY通过。原老EX分层结果复用不重复请求。日期采用原公告/作者dated材料，Submitted/Atom/DOI/Updated/邻ID均不直接认定；一次必要恢复仍缺即精确隔离。EVMbench可先进入必要Source，不等全源。
