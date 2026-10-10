# 2026-03-14 首批增量准入校准请求

作者：mar14_supplement。仅补 **2026-03-13 ～ 2026-03-13（北京时间完整自然日）**；原0候选、原窗口与原§4连续正文冻结，已保存 [baseline](SUP_BASELINE_20261009.md)。本文件不代表日期/准入独核、Evidence、Books或DAY通过；尚不评分。

已完整读取十二项精确v1题摘、Comments、Subjects与Submission history，未把当前v2～v5替代v1。原件为 `SUP_ABS_<末5位>.raw/.txt`；链接精确版本见下表。查询与实际执行原件：[四主题查询](SUP_TOPIC_MANIFEST.json)、[请求结果](SUP_TOPIC_MANIFEST_RESULT.json)、`SUP_TOPIC_MODEL/SYSTEM/MULTIMODAL/AGENT.raw`。API总量/实际返回依次78/78、4/4、35/35、62/62，start0/max150、无下一页；是有限发现停止，不是当日新论文总数、全学科召回或待逐项全文队列。发现submitted区间UTC03-11 18:00～03-12 17:59，相关语义与范围按当前合同处理。

日期原件：十二份 `SUP_DATE_<末5位>.raw`。官方 [availability](SUP_AVAILABILITY.raw) 明示ID/DOI只能在announcement分配且不能预分配；本批提交最早正常公开是Mar13BJT，十二个DOI registered均在Mar13BJT（UTC01:49～02:14）。下界与同日已公告上界合用支持本批arXiv日级公告为Mar13；registered/Submitted/Updated单独不作为first-public，Available月份和Issued年份不替代日级证据。家族早稿/会议/项目公开信号仍另核。11161恰18:00边界应由复核者核官方截止含义，不能只凭常规批次机械断言。已在线补搜四具体标题（只定位先稿，不扫描机构历史）；Cornserve存在明确2025先稿，必要定点原件恢复中。

## 首10拟潜力与2代表排除

| 精确v1材料 | 原约束/判断 → 原文实际增量 → 可能改变的解释或设计选择 | 日期/信号与最小后续核查 |
| --- | --- | --- |
| [11161 Algorithmic Capture](https://arxiv.org/abs/2603.11161v1) | 普遍表达能力不等于训练能捕获算法 → lazy/rich无限宽模型中定义任意问题规模的algorithmic capture、推得可学习函数复杂度界 → 可能收窄从有限任务拟合推断算法泛化的判断 | v2 May7不是本窗；核无限宽、训练/样本与近似误差条件，不外推有限真实LLM。WORLDVIEW-LLM-INTELLIGENCE潜在owner；18:00截止边界待独核 |
| [11243 Self-Speculative ASR](https://arxiv.org/abs/2603.11243v1) | SpeechLLM额外draft成本不一定值得 → 复用CTC encoder，低entropy直接提交、一次relaxed verify、失败后从接受前缀AR续跑 → 改变多模态speculation的资源与分布保证取舍 | 完整摘要明说4.4×点有12%relative WER increase，不能写exact-distribution或无质量代价；核entropy/relaxed接受、质量和吞吐配置。INFER-SPECULATIVE-DECODING |
| [11332 Computational Hardness](https://arxiv.org/abs/2603.11332v1) | 融合多头/多层或许降低渐近算术复杂度 → 小embedding的SETH及大embedding的Baur–Strassen direct-sum lower bound → 收窄把kernel融合解释为普遍次二次attention算法的判断 | 46页、无HTML链接；只需PDF中主定理、计算模型、approximation/precision与相关反侧，不遍历所有证明。MODEL-MULTI-HEAD-ATTENTION |
| [11388 Refusal Triggers](https://arxiv.org/abs/2603.11388v1) | safety拒绝训练可能把良性词cue也绑定refusal → 定义/分析harmful与benign refusal trigger并在对齐fine-tune显式处理 → 改变overrefusal与jailbreak防护的目标/数据取舍 | 摘要warning是内容警告不是修订/撤回；核触发归因、构造与安全/utility协议。TRAIN-RLHF潜在owner |
| [11487 Attention Sinks](https://arxiv.org/abs/2603.11487v1) | sink常被当作经验偶然 → trigger存在时prefix平均、否则零的受限任务中softmax归一化诱发sink而non-normalized ReLU可无sink → 可能改变默认null态为何占概率质量的解释 | v2～v5本窗外，不因版本号自动比较；核定理单头/多头、approximation与bias/null-token条件，不能把摘要标题外推所有softmax必有sink。MODEL-SELF-ATTENTION |
| [11504 LongFlow](https://arxiv.org/abs/2603.11504v1) | 长输出reasoning持续重估importance会昂贵 → 从当前query/attention中间量计算无辅助存储指标，并将FlashAttention/估计/eviction融合 → 改变online KV压缩的可执行成本边界 | v1标题原文截为Reasoning M，v2Apr25不能代替；核估计的具体量、周期、fusion/质量/端到端对照，11.8×不泛化。INFER-KV-CACHE |
| [11564 DapQ](https://arxiv.org/abs/2603.11564v1) | prompt侧attention未必代表未来decode → position-aware pseudo query近似未来窗口，并以position vs semantics证据设计eviction → 改变无需真实未来query的cache保留判据 | 核位置/内容干预、pseudo query位置、预算/模型/长输出边界；NIAH3%预算99.5%只作者局部结果。INFER-KV-CACHE |
| [11653 Continual VLA RL](https://arxiv.org/abs/2603.11653v1) | sequential fine-tune常被预判必然严重遗忘 → 三VLA/五lifelongRL上Seq.FT+LoRA/on-policy系统比较显示可塑/保留组合 → 可能恢复简单基线合理性并限定复杂CRL的必要条件 | v2Jun/v3Jul不迁入；项目码是可选，先核预训练、adapter/on-policy消融、task人口/预算与真实机器人范围。MULTIMODAL-EMBODIED-VLA |
| [12118 Cornserve](https://arxiv.org/abs/2603.12118v1) | any-to-any不同路径/组件伸缩不能由整模型副本统一表达 → task DAG/component disaggregation、record-and-replay、producer-to-consumer tensors → 机制有潜力但本事件是否新增仍待核 | 具体标题搜索发现 [2512.14098](https://arxiv.org/abs/2512.14098v1) 2025先稿及官方repo2025/11发布；数字和核心高度一致，定点原件恢复中，不把本窗新ID当新家族/直接准入，也不重审旧有效采用 |
| [12252 EndoCoT](https://arxiv.org/abs/2603.12252v1) | MLLM encoder一次固定指导不能渐进执行复杂指令 → iterative latent thought guidance + terminal textual grounding对接DiT denoising → 改变condition state与denoise timestep的指导契约 | v2/v3/v4窗外；核latent状态迭代、末态答案监督、任务和compute匹配，92.1%不可宣称通用视觉推理。MULTIMODAL-GENERATIVE-PARADIGMS |
| [11200 DNS-GT](https://arxiv.org/abs/2603.11200v1) | 完整题摘是DNS上下文embedding用于intrusion/botnet/domain分类，新增领域表示/任务收益；未改变当前foundation/LLM模型或系统机制 | 贡献前排除，不因Transformer/embedding/token词重收；不否认其领域价值、不评分、不另追无关先稿 |
| [11390 SliceFed](https://arxiv.org/abs/2603.11390v1) | 完整题摘为6G spectrum slicing的CMDP+primal-dual PPO+FedAvg，在通信领域QoS约束下求解；不是当前模型训练/LLM系统机制贡献 | 范围前排除，agents/PPO/latency类比不足；不把1ms无线deadline映射LLM serving，不评分 |

## 未完工作

首批准入待非作者校准，Cornserve具名先稿决定性核查仍可执行。其余四查询只已读题名供路由；尚未贡献筛选、并非被自动排除或全部全文队列。14每日入口已fresh取原件，多数必要动态/dated切片与相关标题补检未完；source获取不算覆盖/全文审阅。准备好的合格单篇可以进入必要正文，不等无关候选；未取得独核前不写共享Books/State。
