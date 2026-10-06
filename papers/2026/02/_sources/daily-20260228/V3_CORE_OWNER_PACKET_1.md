# 02/28 必要原源与具体 owner 差额：首五项

本轮作者实际阅读，不继承V2完成态；请求root非作者PRE。各HTML正文为 `V3_CORE_<id>.raw/.txt`，可定位块见 `V3_BLOCKS_<id>.md`。以下采用范围止于核心方法、对应比较与直接反侧；未遍历proof/artifact，未默认比较revision。

## 同ID公开范围依据

arXiv原 `V3_ABS_<id>.txt` 版本历史v1实际字段与DataCite同ID记录一致。官方 `V3_POLICY.txt` 声明identifier在announce时才分配、Wed14EST后至Thu14EST投稿最早Thu20EST发布；本月EST=UTC−5。五项原v1均晚于02/25 19:00Z，故原公开下界为02/27 01:00Z（09:00+08），不是Submitted时刻。DataCite registered提供已存在同ID的保守上界，秒精度上界加一秒并用半开区间；不称DataCite为首公开公告或技术证据。

| ID | 原v1 submitted UTC | registered UTC | 本窗公开范围 +08 |
| --- | --- | --- | --- |
|22394|02/25 20:42:35|02/27 02:45:23|02/27 09:00:00～10:45:24|
|22424|02/25 21:35:30|02/27 02:46:05|02/27 09:00:00～10:46:06|
|22437|02/25 21:55:43|02/27 02:46:23|02/27 09:00:00～10:46:24|
|22505|02/26 00:47:51|02/27 02:47:55|02/27 09:00:00～10:47:56|
|22593|02/26 03:55:51|02/27 02:50:01|02/27 09:00:00～10:50:02|

22437原abs显示v2 02/27 03:28:11Z；版本变化本身不授重要修订，不默认对比。22593原v1时间请root定点核原abs；未把首公开范围伪装为exact09:00。

## 22394：3+1+3=7

旧约束：dense消费者把CLS相似度当局部视觉语义，register/high-norm纠偏不足解释DINO-v1反例。增量：§4/blocks27–54，ImageNet单object的PiB与高低patch masking，训练classification↑而PiB≈.42→.44；§5/blocks55–74，channel FFT低通、过滤前后变化形成score、channel topK聚合；§6/Table3/8/9与block93，完整K反而损伤局部结果，maxpool成熟baseline不能达到同样segmentation；patch28对16同时改变分辨率，windowattention改善PiB却损accuracy，不视为唯一因果。作者把lazy aggregation作为假说，不能证明所有ViT/MLLM、register普遍无效或无成本。

Owner `MULTIMODAL-REPRESENTATION`：Ch23 §阶段二的encoder→projector链已有“可恢复/可访问/可表达”及probe成本（当前71–95），缺**全局分类目标的聚合语义与局部dense消费者分开验收**以及PiB/classification反侧。建议在那里一段窄补充，而非另建论文节；需读最终完整前后邻接及自身末注。候选lease：`Books/part-03-multimodal-world-models/23-multimodal-representation.md`，该阶段二一段+自身末注。

## 22424：3+1+3=7

§2/blocks23–65：7词关系×3格式、四Llama/Qwen，AP选择CIE/AIE heads，RSA选择concept一致heads；小K heads几乎不交，cross-format AP仍找FV不找CV。§3/blocks70–88：distinct extraction/steering prompts，FV ID增益更强，CV OOD分布更一致，FV可推French/MC括号而非Englishantonym。直接反侧§5/block99：CV zero-shot/AP不有效，需要prompt已存在concept；CV不替代FV，不证明整个通用抽象或二者训练/推理交互（102–105明确未知）。

Owner `WORLDVIEW-REPRESENTATION`：Ch5现有“decodability/intervention/fresh-probe分开”及分布边界（当前462–474）没有反向误推**因果操控有效⇒格式不变**。建议同一段后补一段，ID/OOD与zero-shot反侧相邻，非control/steering新owner。lease：`Books/part-01-worldview/05-what-neural-networks-learn.md`，机制演进段后一段+自身末注。

## 22437：2+2+3=7

§3–5/blocks34–59：RaggedShard整block原子，规划同时满足不切块、连续buffer、均衡；NP-hard排列用固定orderDP+3heuristicorders，pad在tensor间；DBuffer group-op融合、持久地址映射及inplace。§6/69–75 baseline统一ZeRO3FP32master/BF16但SGD防GPTOSS OOM；8bitAdam同32×32blocks不额外collective，Muon gather到root计算再redistribute；Table2/blocks101–109，禁planner降到65.4%、禁DBuffer92.8%、禁ragged N/A不能量化其独立吞吐；fusedGPTOSS128row块padding可18%，小perGPUbatch仍communicationbound，scaleextrapolation限定topology/protocol。

Owner `TRAIN-ZERO` Ch39当前125–141已真实覆盖block原子/ragged/planning/pointer/checkpoint与均匀fallback，不制造paper-namegap。建议**已有覆盖 NoChange**，本文必要原源限制留日报证据；若root认为“artifact不足复现production”无本轮必要依据，可改为“作者实验不证明通用production收益”，只请求当前139–141一句+自身末注窄lease，不扩章节。

## 22505：2+1+3=6 理论

§3/blocks83–110：期望L1rate误差而非全x/t有界score；TV允许all-MASK singleton初始化、Euler earlystop含初始化/score/κdSlogδ/δ项。lower仅constantstepEuler构造，不能外推all sampler。§4/blocks114–136：Assump2 integral score-entropy；Prop2需要数据无MASK，把NELBO与该积分差常数；Th4在同无MASK条件下FHS恰d次，KL≤trainingerror，无额外离散化；Th5 worstcasepair匹配，不是任意训练器实现tight。本文分析已有FHS，不声称提出新sampler；无LM质量/硬件/墙钟实测。

Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24当前1126–1142已有CTMC timing/direction与analytic-hazard τleaping(15008)但缺**已有FHS“每次揭示一个token”的无时间离散化条件与Euler误差分账**。建议在15008两段后加一段窄对照，保留d次network/词表费用、无MASK/score条件、不从step数授加速。lease：`Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，15008段后一段+自身末注。

## 22593：2+2+3=7

§4/blocks58–101：每engine仍持完整weights，TP仅slice/view（不是TP释放weights）；KV固定physicalbytes，B(p)=pBbase、head/stride变；communicators仅连续alignedgroups预初始化而非所有组合。§5/blocks104–131：同requestorder与safe point；softpreempt先DP做TP请求后需重算KV（122），hard保留pausedDPKV；单节点范围。§6/141–177：directdynamic Shift仅Llama/Nemotron，GPTOSScompatibility缺失；低load相对TP有5.19/10.45%额外，context1.9M比static8TP2.3M少17%；15ms只specific switch，不等请求总延迟/生产tail。

Owner `INFER-SCHEDULING` Ch56当前1263–1269已经同paper段。但byte-identical/generation-tagged/epoch并非原源披露，不应归因本文；现段遗漏**每engine保完整weights/soft需KV重算/连续group限制**，是具体事实纠正不是新papergap。请求窄lease `Books/part-05-inference-system/56-inference-scheduling.md` 仅该subsection两段及自身末注1590；不用改Ch45/权威索引。
