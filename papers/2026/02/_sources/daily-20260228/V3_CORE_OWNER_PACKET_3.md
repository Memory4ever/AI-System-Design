# 第三包：受控反侧与已恢复原机制

后续实际裁决：22425与22480必要原源/具体owner由root非作者实际核通过，Existing安全处置，无新正文；22469原核心与owner PRE通过，Ch23单段/自身note实际POST及Uniform-Smooth/Gaussian-noise分离句回核通过并释放窄lease。Uniform-Smooth随机source仍有较小收益，Gaussian noise才是entropy升而幻觉恶化的独立控制，不混作同一反侧。22453官方v2撤回说明已核，停止下方旧提案全部采用链；该家族仅raw EX，不评分、不进正式候选/Books。窗外v4恢复不救回本窗，下方保留先前阅读与纠错过程，不代表有效提案。

## 22425 ArchAgent，5分，标准完成 → 已有覆盖提案

原§3.5及§7.3/blocks51–56、135–139：100M短trace search与1B验证人口不同；Policy12在优化compile消去assert后调用LLC不支持的write bypass，使模拟器丢write/少算DRAM压力而伪造IPC3/4%收益。只采用Agent/evaluator失效，不采用cache架构指标为LLM贡献。Actual Ch66已读1233–1258：simulator仅预筛，不拥有deployment truth，backend/event semantics/known omissions组成EvalRun，必须real replay；1253–1255更具体区分组件统计、接口请求、application真实依赖。已有论证承载score不能认证semantic-valid execution，故建议Existing/NoChange，不制造ArchAgent论文名gap。未核全部cache代码或artifact。

## 22453 Retrieval-Transition Heads，5分标准完成；实际head责任差额需深入

§3.2–4.1/blocks30–48：600 NIAH配置，Google译needle，四语言，英语/中文pivot不是直接latenttoken；Qwen3-30B aligner将目标语言token对应源needle，RTS不是新retrieval/projector模块。§5/blocks49–67，Appendix D/E必要：相同k=25 RH/RTH/random masking，RTH总体退步更大；Table2 Llama Swahili随机mask本身−20.8、部分语言RH更差，不支持所有随机无影响/RTH总最重要。Table3只在两种mask均从correct→wrong的交集内judge分错误，不能估总体错误率；k≥50普通retrievalfailure覆盖transition效应。pivot proxy与attention之外MLP/残差未隔离，不能证明唯一语言概念通道，更未直接测试KVcompression。

Actual Ch15已读105–139：head分化/冗余、可视化不证明稳定概念、posthoc pruning不等production acceleration。但缺**按within-language retrieval排名不能涵盖跨语言coherence所需heads**这项受控反侧。申请 `Books/part-02-model/15-multi-head-attention.md` “Head怎样分化”现有冗余段后仅一段+自身末注：分别验同语检索/跨语生成、headset/pivot/aligner/k绑定；masking不授直接压缩策略。Ch14定义attention计算、Ch16MLP混合仍不同owner。

## 22469 Spatial Credit Redistribution，6分，深入完成

已纠正初筛误记：训练free的**two-pass inference**不是CLIP训练gradient。§3/blocks20–41：诊断pass找attentiontopK32，排边界，8邻接、源/邻居不能冲突；第二pass早层residual hooks按lambda1.1增加邻居并缩源，故总norm是放大不是严格守恒redistribution。norm-credit correlation r=.72，entropy-hallucination关联非因果；不采用未经必要证明的peak-preserving命题。§4–6/43–84：单A100fp16、6模型、200COCO trainheldout挑超参、POPE3×1000/CHAIR3000、3run。Uniform-Smooth同lambda/K/layers但随机source，noise entropy↑HR反退；LLaVA13B CRoPSHR12.6优于SCR12.8，SCR仅CIDEr代价较小，不能说所有baseline指标占优。两pass+43–56ms；可选one-pass需要5Kmaps训练MLP，不属training-free。小对象/边界与邻居混淆会失败，15%预测改变内30%新错，关系推理/对抗未验。

Actual Ch23已读83–103：诊断encoder、局部consumer与MOH场景先验反侧，但缺**早层hiddenstate空间邻居干预及entropy不是grounding证书**。申请 `Books/part-03-multimodal-world-models/23-multimodal-representation.md` MOH负侧段之后仅一段+自身末注：two-pass/addition不是训练credit，低entropy条件收益/噪声反退、对象边界与延迟代价/fallback同段。不更改已有LazyStrike段。

## 22480 VeRO，5分，标准完成 → 已有覆盖提案

一次decisive结果已确认真实受限条件，恢复IN而非因成熟harness骨架EX。原HTMLv1标题为“An Evaluation Harness”，以实际版本为准。§4/63–76：B8/5仅evaluation call，benchmark3runs/case4runs，validation挑bestcommit；固定GPT4.1mini target，Pawn与Knight同时改变tools/prompt/libraries/turn20/40，不证明复杂度单因果。§5.2–5.3/80、87–96：迁移到新model/任务可退；minimal Pawn上Cookbook+Reasoning较好，复杂Knight上Minimal较好，指导人口不能统一；特定添加verification tool在GAIA涨而SimpleQA−17.8。§6/104：tokens/APIcost不包含预算，无budget消融/人工baseline，API不稳和泄groundtruth未控制，因此不授VeRO必需、等总成本提升或所有agent规律。采用命题只为**optimizer instruction、base-agent能力与目标model/task共同验收**。

Actual Ch84已读982–1012及1080–1094：model/harness配对、cross-product regression、任务/prompt/tool/controller身份与独立holdout/cost预算、capabilityvector含新/历史任务及failure slices已有具体论证。instruction sophistication的方向在2个同时改变tools/prompt/turn的agent上未被唯一隔离，作为报告的经验切片保留，而不提升为新的通用指导规则；采用的配对与跨任务回归合同已由Ch84实际承载，建议Existing/NoChange，不申请写锁。
