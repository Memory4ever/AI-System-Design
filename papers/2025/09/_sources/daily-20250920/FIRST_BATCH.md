# 20日 首批准入交接

2026-10-06T20:26:28+08最新非作者裁决：本日DAY通过；原53完整v1题摘恢复15839局部终答/推理反例后51潜力/2关闭，同段cross-list实际新增12完整v1题摘＝11潜力/1关闭，合计65＝62潜力/3贡献关闭。另11标题范围关闭及MiMo潜力1，正式/证据完成/Books0。[独立验收与12项准入边界](./INDEPENDENT_DAY_REVIEW.md)为最新差额；旧49/4、50/3与原范围关闭保留历史，不再作为终态。

14:35:53+08差额：16241 REAMS据Algorithm1的oracle失败选择、人工执行与未统一重试预算恢复最小评价边界潜力，53题摘现50潜力/3关闭。15478/16107必要core及15896安全关闭受影响段已读；精确位置与源码分页见[NARROW_SOURCE_SAFETY_HANDOFF.md](./NARROW_SOURCE_SAFETY_HANDOFF.md)。下面原49/4及REAMS关闭为历史记录，不覆盖本差额。

作者Tesla；2026-10-06。本日独立月列表有界标题查漏52身份，47相关/含糊身份实际读精确v1完整题摘（15478/15560 HTML404后abs/v1恢复）。以下43潜力、4关闭，另5明确领域标题不进入正文队列。仍缺真实first-public，不以submitted/API published/ID顺序授落窗或评分。请root按研究合同§3校准首批机制/负面及代表性排除；没有自授Evidence/Books。

原题摘在对应`2509.IDv1.raw`，两abs替代有独立原文件；部分完整正文下载超时但题摘结构完整，只声称题摘。作者未把下载全文算全文阅读。

## 潜力：既有约束 → 实际增量 → 待核设计选择

| ID(v1) | 具体潜力与限制 |
| --- | --- |
| 15403 | explanation无不确定保证→posthoc/抗噪校准→解释置信输出；不等于faithfulness |
| 15430 | 外部label encoder成本或随机label弱→内部增强label加raw anchor/bilevel→SSL训练/坍塌取舍 |
| 15447 | persona自由文本不可控→量化schema与hybrid比较→一致性/多样性取舍，不因25persona关闭 |
| 15476 | 模态越多未必越好→TA/AV优于trimodal局部反证→模态选择 |
| 15478 | 多模态攻击被假定更强→文本稍强反证→输入模态安全评价；26人726prompt不授生产ASR |
| 15485 | ordinal单标签高罚错误→conformal集合内加权解码→有限标签替代输出设计，非语言通用加速 |
| 15515 | uniform query cache→knapsack/累计更新与regret→异质query缓存，理论假设及总成本待核 |
| 15518 | 合成slang可代人类样本→生成结构偏差/蒸馏informativeness→synthetic数据可替代边界 |
| 15549 | 英语数据选择外推→multilingual质量/多样性及SAH比较→跨语言SFT选择 |
| 15550 | 文本检测分布重合→迭代repair effort统计→检测替代信号，额外修复成本待核 |
| 15556 | 语言占比独立调参→cross-language effective ratio与两步优化→预训练数据分配 |
| 15568 | 相关聚合成本高→BISAC/topic debate+BM25拼接→cheap synthesis替代路线；不是仅因应用关闭 |
| 15577 | retrieval relevance非generation utility→process监督rewrite/distillation→RAG桥接目标 |
| 15579 | 全utterance SSL不适streaming→chunk上下文/大FSQ/group loss→流式codec训练内存取舍 |
| 15587 | reasoning技能混杂→counterintuitive句子及抗偏metric→逻辑评价混杂，需核metric不能只是更难题库 |
| 15621 | 指定句子unlearn不覆盖概念→自构triplets/解释→概念删除；KG不等真实内部知识 |
| 15631 | 输出抑制不等忘记→SAE向unknown激活对齐→删除目标/utility；不能采genuine forgetting宣传 |
| 15655 | 语音层越深未必更语义→minimalpair中层峰/末层退步→encoder层/目标选择 |
| 15667 | rawaudio与text直接alignment→Whisper decoder hidden连续融合→audio-conditioned text空间替代 |
| 15701 | PCC高不等rank稳定→.9 PCC/.6 SCC及phoneme失效→细粒度评价盲区，不因发音应用排除 |
| 15714 | nextword语料预算→teacher高层反馈→互动学习数据预算；teacher计算不由word数抵消 |
| 15723 | opinion少数覆盖偏差→frequency framed prompting→提示表达/汇总公平性 |
| 15739 | linear judge外推辩论→QuAD非线性/顺序长度失效→judge表示与输入次序 |
| 15763 | KV sequence删除信息损失→gist shift kernel/实际驱逐→压缩质量与物理收益 |
| 15789 | UN corpus不可复现/对齐→Graph-Aided Paragraph Alignment→训练数据构建替代，不将规模数当机制 |
| 15793 | linguistic cues难辨可核claim→retrieval+source credibility→verifiability检测；组合收益归因待核 |
| 15811 | 单语言bestof预算→crosslingual reward/rank→采样分配，匹配总预算待核 |
| 15837 | visualgrounding等于semantic提升→speech词身份增强但语义未改善→encoder表示反证 |
| 15888 | weightadaptation成本→warmstart KL-gradient steering→decode适配；firstorder不是完整训练等价 |
| 15901 | summary整体生成遗漏→fact骨架/reader九问+P-MESA→faithfulness与reader-fit评价 |
| 15926 | 单essay分数无信心→conformal set/UAcc→ordinal输出校准；coverage不等逐题正确 |
| 15958 | hardmax收敛描述外推→alignment敏感localmax/quiescent sets→attention动力学适用条件 |
| 15974 | allbias效率但选哪些不明→bias-selection→低数据参数选择，非LoRA普遍替代 |
| 16025 | cascaded/shortwindow漏discourse→session全局/多目标/frozenprior→speech评分窗口与校准取舍 |
| 16028 | speechfriendly损reasoning→reason/verbalize分责+异步ReVerT→输出接口/latency |
| 16093 | 单judge分数混覆盖与正确→gold-derived precision/recall→评价维度与criteria人工成本 |
| 16105 | 各层uniformpruning→连续化非均匀expert搜索→MoE压缩/质量预算 |
| 16107 | simplification被当无害→clarification减少/ambiguitycommit→可理解性与澄清失效 |
| 16112 | relevantcode非必要code→logprob query/multipath/BestFit→repository RAG目标 |
| 16188 | 多语言数据等于文化能力→culture维度与未必改善反证→data/eval边界，不只新增140标签 |
| 16198 | 自由文本longrepo计划漂移→persistent capability/file/dataflow graph→规划表示与test验证 |
| 16264 | aggregate bias掩盖群体→demo可检视counterfactual/negativeLoRA结果→局部公平性盲区；尚待去重原EuroParlVote事件 |
| 16278 | longdependency不足→pretrainmeta-token/meta-attn→状态landmark与lengthgeneralization；synthetic不授通用长上下文 |

## 代表性关闭

- 15560 `How important is language for human-like intelligence?`完整v1题摘提出语言压缩/文化抽象的观点；没有给出本次可核的新学习机制、定理条件或修正具体系统选择的比较证据。不是因非工程论文关闭。
- 15896 `The Psychology of Falsehood`是人类心理/误信息分类综述与未来方向，题摘未提供新模型/系统机制或盲区实证；不是所有survey一律排除。
- 16241 `REAMS`题摘仅zero-shot+program synthesis在数学任务提高准确率，未给新增执行机制、适用边界或可比预算事实；不由90.15%倒推贡献。
- 15839 `Multi-Physics`明确专门物理科学领域benchmark，按ROADMAP暂缓AI for Science，不绕到Evaluation引入。它的模态/CoT切片保留原记录，若root认为实际属于通用表示反证而非该暂缓范围，可定点重开，不重扫47项。

5标题关闭：15419 radiology、15620 scientific event、15640 medical translation、16226 scientific induction、16256 Hausa sentiment dataset，只作明确领域应用/科学范围判断，不称读了摘要。

## 官方Blog当前事件

Google [TTD-DR Blog](https://research.google/blog/leveraging-test-time-compute-to-scale-deep-research/)本轮完整相关核心及2507.16075v1题摘已读：draft引导search、revision/judge路径与July原稿是同一贡献；当前Agentspace可用说明未给新执行/兼容/可靠性约束。不以“旧论文无价值”关闭，仅提案关闭这次再阐述事件，也不冒称July原事件已有本项目审阅。请root核该差额。

MiMo-Audio官方Paper页Sep19及本轮GitHub/Demo核心是25Hz/8RVQ/patch4→6.25Hz LLM→25Hz delay decoder的具体替代设计，潜力保留。但Sep19整天相交本窗；初commit `9bc65b003c18` Sep19T00:48:29Z在下界前，后一01:05:50Z在窗内，也不证明仓库当时public或首次公开。缺原公告/历史public artifact上界，暂不评分/采用。December论文版本不搬到九月。

系统主题API真实200共7条，最新版本仅发现，另6具名精确v1完整题摘已恢复实际读完；第7条15844明确medical multi-view clustering，不纳入LLM训练/系统主线。后续不按全年系统库存扩池。合计53完整v1题摘，49潜力/4关闭，非53本窗事件。

| ID(v1) | 新增系统潜力与边界 |
| --- | --- |
| 15450 PCCL | 网络拥塞/dilation使collective算法理论收益失效→按通信pattern改光路并计reconfig成本→算法/网络共同选择；128GPU局部不授anytopology保证 |
| 15674 H2T2 | 单阈offload难兼顾非对称错误成本→calibrated闭式/uncalibrated双阈在线策略→cost-sensitive routing；不是foundation实测，理论适用条件待核 |
| 15861 ToFU | posthoc难消记忆→训练时transform composition限制instance信息→learn-to-unlearn；小模型理论/实验不因非LLM自动排除，不能授法规符合或完全遗忘 |
| 15940 Arnold | topology错配通信group→按pattern/network调placement→大集群训练调度；仿真spread与生产endtoend数字分开 |
| 15965 RLinf | heterogeneous RL流水利用低→M2Flow时空拆分/recompose、contextswitch/elasticpipe→训练流程物理计划；v1为1.1–2.13倍，不用最新v2 1.07–2.43倍 |
| 16293 ByteRobust | 大训练故障routine恢复→按parallelism demarcate/localize→诊断/容错路径；97% ETTR不等故障零/生产保证，200k平台与9600GPUjob分开 |
