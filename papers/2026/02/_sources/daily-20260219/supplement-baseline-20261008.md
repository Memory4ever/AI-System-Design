# Daily Research — 2026-02-19

**规范：** V3
**窗口：** 2026-02-18T09:00:00+08:00 ～ 2026-02-19T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T23:26:28.638Z

## 1. 结论

本日按当前合同独立重建，不继承旧Weekly、V2.1候选、评分或完成声明。104个唯一完整题摘线索是有界主题查询与相关题名查漏的发现材料，不是104项强制全文队列；97个同身份日期成立亦非候选数。67个具体贡献家族已分批准入校准，来源筛选已在有界查询/题名补检停点收口，不扩大宽库存。全部67项必要source/Books安全处置已root逐项通过；65项必要证据已受限完成，2项中心争议隔离；51项实际整合、14项具体已有覆盖，全部必要写入/完整邻接/末注已root POST通过。

已完成的逐项处置包括整合、具体已有覆盖及中心争议终态暂缓；所有已写正文/完整邻接和末注均实际POST通过，窄锁已释放。所有67项已逐项获得安全处置，作者侧普通扫描/筛选/审阅/Books待办为0；最终六部分、来源与日期及独立日级复核已通过。

收益均限定原版、负载与评价。Panini 写读不普遍更便宜，COMPOT 非联合 one-shot，Sparrow ESR/DSR 与 prefill 分账，鲁棒签名仅在约定编辑/密码/entropy条件下成立；Prefix47倍是 compute-to-target FLOPs 估算，不是测得时间缩短。未运行代码或复现。

## 2. 来源覆盖

以下只记录本日已实际使用入口和停止范围。历史目录不可恢复的缺口不证明零事件；没有扫描每周来源或机构历年全文。有限 API 新恢复见[本日来源恢复](../_sources/daily-20260219/V3_SOURCE_RECOVERY.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方Research与 EVMbench/RSS 的本窗定点恢复；RSS Feb18 00Z早于起点，India发布业务说明未给机制增量 | 已检查 | EVMbench初版发布时间精度与正文版本不能用当前页补造；保留归属线索，不重复深审 |
| SRC-ANTHROPIC | 官方 Research 的 Measuring Agent Autonomy 日期/原HTML与方法；DatePublished Feb18 15:10Z，当前modified Sep9；有限初版恢复已停止 | 受阻 | 初版可读快照/明确delta外部缺失，作为本窗终态保留；不能把后改数字当本窗初版，精确需求列§5 |
| SRC-GOOGLE-AI | GoogleResearch当前目录385/11583首15与DeepMind Feb18印度教育/科学说明，未扩历年论文 | 受阻 | Research本窗历史切片未恢复；教育/AIforScience应用未准入，不称零事件 |
| SRC-META-AI | 官方Research动态入口及定点辅助检索；未取得本窗可读原目录 | 受阻 | 需本窗官方event/archive；动态空响应不是无事件 |
| SRC-QWEN | 官方qwen.ai动态与原GitHub Blog可见条目止2025年9月，定点补检未恢复目标切片 | 受阻 | 需本窗原始发布目录；不遍历全repo |
| SRC-DEEPSEEK | 官方无日期主页与本窗定点补检 | 受阻 | 无可确认本窗事件目录；无命中不是不存在 |
| SRC-MOONSHOT | 平台Blog可见2025年末/更早；本日组织首页10/42repo更新时间Oct→Aug，停止当前页 | 受阻 | 未恢复Feb18–19原event/archive；Updated不当release |
| SRC-TENCENT-HUNYUAN | 官方POST publicList page1,size20,renderType0；200/code0,list9/total9，实际读所有title/publicAt/display字段 | 已检查 | 该发布目录无本窗字段；范围不等Research所有论文，无全站无遗漏保证 |
| SRC-ZAI | Research Feb11→Feb21，ReleaseNotes Feb12 GLM5/Feb3OCR的相邻发布切片；GLM5论文另按arXiv身份 | 已检查 | 仅覆盖实际目录，不借版本名准入 |
| SRC-BYTEDANCE-SEED | 官方API2026升序，type1首20至Feb24首次跨截止停止；type2九条至Mar31首次跨截止停止 | 已检查 | PublishDate索引字段不是论文first-public，未扫后续页或所有历史 |
| SRC-BAIDU-ERNIE | 官方Blog page1/2 May/Apr→Feb6/Jan29括住目标时段，实际标题筛选 | 已检查 | 仅覆盖目录切片，不授全机构召回 |
| SRC-XIAOMI-MIMO | 官方Paper目录June29/Mar13/Feb3/Jan8，Blog15可见但无公开日期 | 受阻 | Paper目录已检查；Blog本窗归属无法从无日期标题推定 |
| SRC-MINIMAX | 官方Blog当前Aug→Mar18；官方techblog.md307后200只有May13一项，停止 | 受阻 | 主Blog本窗历史切片缺失，未扫llms或repo全史 |
| SRC-ARXIV | 四主题官方API start0/max250；model训练61、runtime13、多模态20、Agent35（跨主题去重）；相关月列表前250标题只查漏，当前99完整題摘及精确v1受影响摘要、extra15题摘已读 | 已检查 | [实际查询](../_sources/daily-20260219/V3_ARXIV_TOPIC_QUERIES.json)与[题摘](../_sources/daily-20260219/V3_TITLE_ABSTRACT_SCREEN.md)不是候选关闭账；104完整题摘线索经贡献筛选保留67家族；范围外/成熟组合关闭，宽库存不是逐项队列，不宣称全学科召回 |
| 表外：[DataCite](https://api.datacite.org/) | 本日每family DOI原Created/Registered/Submitted字段；99及extra5身份独立，非相邻ID推定 | 已检查 | 与官方日程共同限定，不把Created单独等first-public |
| 表外：[arXiv公开日程](https://info.arxiv.org/help/availability.html) | identifier/DOI在announcement赋予；Mon14–Tue14 ET提交批次最早Tue20 ET | 已检查 | 仅作相同identity下界，不借其他日期候选池 |
| 表外：[GitHub Mnemis ](https://github.com/microsoft/Mnemis) | 精确repo/paper commit较早公开信号，未扩组织全史 | 受阻 | repo created/commit不证明当时public，首次公开保留§5 |
| 表外：[GitHub GLM-5](https://github.com/zai-org/GLM-5) | 精确Feb11 README ref88e136f：technical report coming soon；仅去重早release与正文事件 | 已检查 | commit不单独证明first-public，正文依arXiv同身份区间；未扩repo全史 |
| 补检：[Web 搜索](https://www.google.com/) | 仅具体机构历史入口/身份恢复，不以搜索摘要作Evidence | 检索受限 | 无命中不闭合历史目录，也不无限扩大搜索 |

## 3. 候选与判断

下表为来源筛选收口后的67个唯一候选家族。潜在准入但必要日期条件不全者只列§5，不混当窗确定候选。明确EX只保留贡献记录，不为EX追补日期。

下表区间是同身份Submitted批次官方最早公开下界与原DOI Created上界共同限定；每条原字段见[DataCite](../_sources/daily-20260219/V3_DATACITE_DATE_BOUNDS.json)。为半开区间，精度上界加1毫秒以包含原Created时刻，仍完整落窗；Created不是单独first-public。当前Updated只用作纠错/版本发现，不采用v2/v3命题。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Panini: Continual Learning in Token Space via Structured Memory](https://arxiv.org/html/2602.15156v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:00.001+00:00 | 固定weight无法连续更新→QA/entity-event workspace与无逐hopLLM的答案实体检索→迁移读写计算，保留写入成本。 2+2+2=6 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [OpaqueToolsBench: Learning Nuances of Tool Behavior Through Interaction](https://arxiv.org/html/2602.15197v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:57.001+00:00 | 静态工具schema遗漏blackbox行为→交互轨迹改docs→metadata不授执行正确性。 2+1+2=5 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression](https://arxiv.org/html/2602.15200v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:36:02.001+00:00 | 静态低秩重构→两个条件解析子问题→不把20轮交替当联合one-shot。 2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Automatically Finding Reward Model Biases](https://arxiv.org/html/2602.15222v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:36:32.001+00:00 | 已知bias清单不足→未知属性搜索后独立counterfactual验证→发现不等真实偏置召回。 2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs](https://arxiv.org/html/2602.15318v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:38:46.001+00:00 | 视觉drafter重复取证→训练visual bridge而推理text-hidden替代→长度依赖收益与prefill代价。 2+2+2=6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Unforgeable Watermarks for Language Models via Robust Signatures](https://arxiv.org/html/2602.15323v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:38:53.001+00:00 | soundness不等adaptive unforgeability→robust signatures/PPH及恢复list责任→限定编辑模型和身份归因。 3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Fast and Fusiest: An Optimal Fusion-Aware Mapper for Accelerator Design](https://arxiv.org/html/2602.15166v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:14.001+00:00 | 局部Pareto可能误剪→compatible pmapping与全lifetime reservations→限定可互换接口后裁剪。 2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [The Turbo-Charged Mapper: Fast and Optimal Mapping for Energy-efficient and Low-latency Accelerator Design](https://arxiv.org/html/2602.15172v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:22.001+00:00 | dataflow隐藏placement→显式storage/currying→保留partial-relevance顺序与模型条件。 2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Protecting Language Models Against Unauthorized Distillation through Trace Rewriting](https://arxiv.org/html/2602.15143v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:34:42.001+00:00 | 答复保持不等学生学得行为保持→trace rewrite与trigger查询→输出归因/蒸馏行为分责。 2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Weight space Detection of Backdoors in LoRA Adapters](https://arxiv.org/html/2602.15195v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:55.001+00:00 | adapter行为难验→静态五SVD sensor→制造方法/人口/holdout条件限定，与行为gate分离。 2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L215–223 |
| [ScrapeGraphAI-100k: Dataset for Schema-Constrained LLM Generation](https://arxiv.org/html/2602.15189v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:47.001+00:00 | schema高成功不等语义value→实际telemetry/population与key/value反侧→五层success分责。 2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L49–77 |
| [Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems](https://arxiv.org/html/2602.15198v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:59.001+00:00 | CoT intent不等collusion effect→nominal/reference/regret对照→task-defined效应与judge分账。 2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference](https://arxiv.org/html/2602.15206v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:36:10.001+00:00 | 多feedback不应统一scalar→共享latent reward与不同likelihood/rightcensor→观测type分责。 2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Fast and Effective On-policy Distillation from Reasoning Prefixes](https://arxiv.org/html/2602.15260v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:37:26.001+00:00 | 完整rollout昂贵→student prefix早停/渐长→省计算不授完整tail或安全。 2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [ÜberWeb: Insights from Multilingual Curation for a 20-Trillion-Token Dataset](https://arxiv.org/html/2602.15210v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:36:16.001+00:00 | 多语言比例不能独解容量损害→固定ratio改变curation双向transfer→quality与mix分开。 2+1+2=5 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [How to Train Your Long-Context Visual Document Model](https://arxiv.org/html/2602.15257v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:37:21.001+00:00 | 测试时page metadata可能无效→train/infer page-interface一致→窗口/页数/评价版本分开。 2+2+2=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [ResearchGym: Evaluating Language Model Agents on Real-World AI Research](https://arxiv.org/html/2602.15112v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:33:59.001+00:00 | 任务完成/工具成功不等研究改善→独立outcome与integrity边界→异步日志、cleanup和选择偏差不授有效研究。 2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L238–245 |
| [Seeing to Generalize: How Visual Data Corrects Binding Shortcuts](https://arxiv.org/html/2602.15183v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:38.001+00:00 | 内容可见不等绑定可泛化→paired intervention与curriculum bundle→局部binding路径不授image-only因果。 2+1+3=6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) L215/217，非作者POST通过 |
| [An Empirical Study on the Effects of System Prompts in Instruction-Tuned Models for Code Generation](https://arxiv.org/html/2602.15228v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:36:41.001+00:00 | 更rich system prompt不必提高代码通过→有限非单调对照→提示形式与模型/任务绑定。 2+1+2=5 | 标准完成 | 已有覆盖：AGENT-PROMPT，[Ch74](../../../../books/part-07-agent/74-prompt.md) L68–90/115–139 |
| [Closing the Distribution Gap in Adversarial Training for LLMs](https://arxiv.org/html/2602.15238v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:36:54.001+00:00 | jailbreak分布错配→conditional diffusion proposal+DAT→保证须harmful marginal/TV条件，不授全adaptive。 2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) L1347/1349，非作者POST通过 |

| [Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs](https://arxiv.org/html/2602.15173v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:35:24.001+00:00 | 同一风险选择受输入表示/提示改变→描述与模拟history及解释形式反侧→固定subject后评价，不把风险中性当真值。 2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [What Do Neurons Listen To? A Neuron-level Dissection of a General-purpose Audio Model](https://arxiv.org/html/2602.15307v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:38:31.001+00:00 | 低entropy神经元不是唯一语义地址→matched随机消融与共现反侧→分开相关、局部使用及跨域机制。 2+1+2=5 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Consistency-Preserving Diverse Video Generation](https://arxiv.org/html/2602.15287v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:38:03.001+00:00 | joint多样性可能损temporal一致→只移除负对齐梯度→一步代理约束不授整轨迹。 2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [On Surprising Effectiveness of Masking Updates in Adaptive Optimizers](https://arxiv.org/html/2602.15322v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:38:51.001+00:00 | 稀疏应用不等稀疏梯度与状态→dense moments后mask/damping→不把更新稀疏称省backward。 2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [The Information Geometry of Softmax: Probing and Steering](https://arxiv.org/html/2602.15293v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:38:11.001+00:00 | Euclidean steering不等输出KL预算→Bregman/expected-unembedding与hyperplane条件→条件最小off-target KL。 3+1+3=7 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Prescriptive Scaling Reveals the Evolution of Language Model Capabilities](https://arxiv.org/html/2602.15327v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:38:58.001+00:00 | loss不能直接推出后训练能力上限→条件分位人口与signed时间bins→限定生态边界和测量分配。 2+2+2=6 | 深入完成 | 整合：WORLDVIEW-SCALING-LAW，[Ch7](../../../../books/part-01-worldview/07-scaling-law.md) |
| [World-Model-Augmented Web Agents with Action Correction](https://arxiv.org/html/2602.15384v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:40:18.001+00:00 | sim选行动可能失败→失败rationale再proposal并保历史best→有限再提案不授fail-closed。 2+1+2=5 | 标准完成 | 已有覆盖：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use](https://arxiv.org/html/2602.15329v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:39:01.001+00:00 | 固定frame保留压跨event→event FIFO与当前event reservoir→分配frame retention而非语义oracle。 2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Discovering Implicit Large Language Model Alignment Objectives](https://arxiv.org/html/2602.15338v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:39:13.001+00:00 | 终点难识别训练奖励→trajectory residual提出surrogate再行为检验→拟合与真实内部目标分开。 2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models](https://arxiv.org/html/2602.15344v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:39:22.001+00:00 | memory跨时刻检索污染→已stored黑盒攻击及writer声明→写入来源治理不能由检索相关性替代。 2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MarkSweep: A No-box Removal Attack on AI-Generated Image Watermarking via Noise Intensification and Frequency-aware Denoising](https://arxiv.org/html/2602.15364v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:39:50.001+00:00 | 信息量下降不等实际decoder准确率下降→DPI/Fano责任分离与反例→三轴验收不从MI推出攻击成功。 2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations](https://arxiv.org/html/2602.15379v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:40:11.001+00:00 | fusion阻塞冷启动预取插点→weights/texture lifetime与prefetch-compute联排→冷/warm成本分账。 2+1+2=5 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems](https://arxiv.org/html/2602.15382v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:40:15.001+00:00 | 异构agent image latent不能直接互读→各codec/hub映射→span接口和版本生命周期分账。 2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching](https://arxiv.org/html/2602.15396v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:40:35.001+00:00 | 独立endpoint桥退回score→先学coupling再reverse匹配→近似coupling与成本不能省。 2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Logit Distance Bounds Representational Similarity](https://arxiv.org/html/2602.15438v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:41:33.001+00:00 | 预测KL近不保证线性readability→centered gauge/σmin/τ条件→输出与表示保留分账。 3+1+3=7 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [On the Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks](https://arxiv.org/html/2602.15460v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:42:04.001+00:00 | 更大map可能含ID小路径→控制start-goal/path支持→ID高分不授OOD算法泛化。 2+1+3=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LLM-as-Judge on a Budget](https://arxiv.org/html/2602.15481v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:42:33.001+00:00 | uniform judge预算忽略异方差→variance分配→提高固定judge均值精度非humantruth。 2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Approximation Theory for Lipschitz Continuous Transformers](https://arxiv.org/html/2602.15503v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:43:04.001+00:00 | 普通attention不保Lipschitz→tied V/负Euler/compact measure函数类→条件非扩张不授实用所有Transformer。 3+1+3=7 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/html/2602.15515v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:43:21.001+00:00 | probe信号消失可能表示漂移→旧/新probe对照和reward梯度路径→evasion不等信息移除。 2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Certified Per-Instance Unlearning Using Individual Sensitivity Bounds](https://arxiv.org/html/2602.15602v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:45:22.001+00:00 | 平均unlearning掩盖个体→per-instance sensitivity/Langevin certificate→经验distinguisher不等形式保证。 2+2+3=7 | 争议 | 暂缓：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；中心证明隔离，见§5 |
| [Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections](https://arxiv.org/html/2602.15654v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:46:36.001+00:00 | session reset未清长期状态→正常write-path持续感染→writer治理跨session责任。 2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [A Note on Non-Composability of Layerwise Approximate Verification for Neural Inference](https://arxiv.org/html/2602.15756v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:48:58.001+00:00 | 逐层容差可能放大→ReLU输出范数有界的特定扩宽反例→local检查不可自动组合端到端。 3+1+3=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [HIMM: Human-Inspired Long-Term Memory Modeling for Embodied Exploration and Question Answering](https://arxiv.org/html/2602.15513v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:43:18.001+00:00 | semantic obs过早全局融合→保留time/pose到检索投影再visual验证→semantic与几何估计分账。 2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [VLM-DEWM: Dynamic External World Model for Verifiable and Resilient Vision-Language Planning in Manufacturing](https://arxiv.org/html/2602.15549v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:44:08.001+00:00 | 计划执行不等world state生效→phase postcondition与几何反馈后DB commit→rollback不等物理回滚。 2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Directional Reasoning Trajectory Change (DRTC): Identifying Critical Trace Segments in Reasoning Models](https://arxiv.org/html/2602.15332v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:39:05.001+00:00 | trace读路径不等final outcome→receiver-only fixed continuation干预→重rollout责任另验。 2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [ActionCodec: What Makes for Good Action Tokenizers](https://arxiv.org/html/2602.15397v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:40:37.001+00:00 | 重构越好不必越易policy学→overlap稳态与token依赖结构→codec和action预测分账。 2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [TAROT: Test-driven and Capability-adaptive Curriculum Reinforcement Fine-tuning for Code Generation with Large Language Models](https://arxiv.org/html/2602.15449v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:41:48.001+00:00 | 单一testtier不适合全部capability→预选tier分配与rewardweight→不是在线hard-first课程。 2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [In Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Generations](https://arxiv.org/html/2602.15456v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:41:58.001+00:00 | 自述source偏好不等选择→固定内容交换external source label→质量与归因分别验。 2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Co-Design and Evaluation of a CPU-Free MPI GPU Communication Abstraction and Implementation](https://arxiv.org/html/2602.15356v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:39:38.001+00:00 | host progress增加开销→persistentmatch预设置/GPU stream触发→有限队列耗尽责任。 2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [The Equalizer: Introducing Shape-Gain Decomposition in Neural Audio Codecs](https://arxiv.org/html/2602.15491v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:42:47.001+00:00 | gain已缠入latent方向→preencoder norm另传scalar→重训与gain成本不能由小码本抵消。 2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs with GLU Activation Patterns](https://arxiv.org/html/2602.15521v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:43:29.001+00:00 | dense转MoE无法随意拆→profile/sharedratio与neuron对应切片→sum改softmax不保函数。 2+1+2=5 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Quantifying construct validity in large language model evaluations](https://arxiv.org/html/2602.15532v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:43:45.001+00:00 | leaderboard谱非真实能力→SEM测量误差与条件人口→统计构念不授causal。 2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling](https://arxiv.org/html/2602.15537v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:43:52.001+00:00 | 固定frame使tokenrate高→冻结表示边界层/内容层分工→temporalunit绑定任务质量。 2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs](https://arxiv.org/html/2602.15556v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:44:18.001+00:00 | 视觉attention sink不等证据使用→interlayerdelta增强和sys补偿→heuristic不授指令mass保证。 2+1+2=5 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [1-Bit Wonder: Improving QAT Performance in the Low-Bit Regime through K-Means Quantization](https://arxiv.org/html/2602.15563v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:44:27.001+00:00 | 固定weight memory下bit数/容量互换→QAT format×generative任务对照→质量不等kernel速度。 2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Beyond Static Pipelines: Learning Dynamic Workflows for Text-to-SQL](https://arxiv.org/html/2602.15564v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:44:28.001+00:00 | 异质workflow单选有边界→finite oracle与actor availability mask训练→heterogeneity不自动严格优势。 2+1+2=5 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Constraining Streaming Flow Models for Adapting Learned Robot Trajectory Distributions](https://arxiv.org/html/2602.15567v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:44:33.001+00:00 | stream flow避障不能等末端projection→SPDmetric/workspace pullback塑velocity→softshape非安全不变性。 2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [How Vision Becomes Language: A Layer-wise Information-Theoretic Analysis of Multimodal Reasoning](https://arxiv.org/html/2602.15580v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:44:51.001Z | 模态probe混合信息类别→PID估计与通道干预→但中心公式/表冲突，不能采因果份额。 2+2+2=6 | 争议 | 暂缓：中心估计公式/表一致性，见§5 |
| [A unified theory of feature learning in RNNs and DNNs](https://arxiv.org/pdf/2602.15593v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:45:10.001Z | 共享权重不自动改功能→μP posterior时间kernel条件→监督时序与归纳偏置共同决定。 3+1+3=7 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Revisiting Backdoor Threat in Federated Instruction Tuning from a Signal Aggregation Perspective](https://arxiv.org/html/2602.15671v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:46:59.001Z | benign client协议不保证数据干净→分散上游poison聚合→来源治理与update筛查分责。 2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [A Differential Fuzzing-Based Evaluation of Functional Equivalence in LLM-Generated Code Refactorings](https://arxiv.org/html/2602.15761v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:49:05.001Z | 静态tests通过不等refactor语义等价→有效输入差分反例→阴性fuzz非证明。 2+1+3=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety](https://arxiv.org/html/2602.15799v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:49:57.001Z | 首步近正交不保护整轨迹→局部曲率耦合→方向诊断与行为安全验收分责。 3+1+3=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing](https://arxiv.org/html/2602.15823v1) | 2026-02-18T01:00:00+00:00 ～ 2026-02-18T02:50:30.001Z | edit成功不等cap保留→Bregman局部GN/KFAC近似投影→artifact与能力回归分责。 2+2+2=6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Dynamic Training-Free Fusion of Subject and Style LoRAs](https://arxiv.org/html/2602.15539v1) | 2026-02-18T01:00:00Z ～ 2026-02-18T02:43:54.001Z | 静态幅度择adapter不看实际输入→layer/step feature硬择→内容与风格冲突须分账。 2+1+2=5 | 深入完成 | 整合：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation](https://arxiv.org/html/2602.15400v1) | 2026-02-18T01:00:00Z ～ 2026-02-18T02:40:40.001Z | 语言输出无metric坐标→normalized view/grid经raycast到waypoint→校准接口和controller分责。 2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [A Generative-First Neural Audio Autoencoder](https://arxiv.org/html/2602.15749v1) | 2026-02-18T01:00:00Z ～ 2026-02-18T02:48:48.001Z | encoder高rate计算昂贵→前移downsample但decoder同构CUDA fallback→两侧分别profile质量成本。 2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/html/2602.15763v1) | 2026-02-18T01:00:00Z ～ 2026-02-18T02:49:08.001Z | 异步trajectory可混version/文本重编码→TITO与staleness/env分账→采样identity不授无偏。 2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |

## 4. 证据与知识整合

### [Panini: Continual Learning in Token Space via Structured Memory](https://arxiv.org/html/2602.15156v1)

采用精确v1；固定weight无法连续更新→QA/entity-event workspace与无逐hopLLM的答案实体检索→迁移读写计算，保留写入成本。 必要方法、对照和直接反侧的可读位置见[首6证据](../_sources/daily-20260219/V3_CORE_FIRST_BATCH.md)中本family小节，未核代码或复现。整合：AGENT-RAG，Ch76；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [OpaqueToolsBench: Learning Nuances of Tool Behavior Through Interaction](https://arxiv.org/html/2602.15197v1)

采用精确v1；静态工具schema遗漏blackbox行为→交互轨迹改docs→metadata不授执行正确性。 必要方法、对照和直接反侧的可读位置见[首6证据](../_sources/daily-20260219/V3_CORE_FIRST_BATCH.md)中本family小节，未核代码或复现。整合：AGENT-TOOL-CALLING，Ch78；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression](https://arxiv.org/html/2602.15200v1)

采用精确v1；静态低秩重构→两个条件解析子问题→不把20轮交替当联合one-shot。 必要方法、对照和直接反侧的可读位置见[首6证据](../_sources/daily-20260219/V3_CORE_FIRST_BATCH.md)中本family小节，未核代码或复现。整合：INFER-TENSORRT-LLM，Ch49；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Automatically Finding Reward Model Biases](https://arxiv.org/html/2602.15222v1)

采用精确v1；已知bias清单不足→未知属性搜索后独立counterfactual验证→发现不等真实偏置召回。 必要方法、对照和直接反侧的可读位置见[首6证据](../_sources/daily-20260219/V3_CORE_FIRST_BATCH.md)中本family小节，未核代码或复现。整合：TRAIN-RLHF，Ch31；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs](https://arxiv.org/html/2602.15318v1)

采用精确v1；视觉drafter重复取证→训练visual bridge而推理text-hidden替代→长度依赖收益与prefill代价。 必要方法、对照和直接反侧的可读位置见[首6证据](../_sources/daily-20260219/V3_CORE_FIRST_BATCH.md)中本family小节，未核代码或复现。整合：INFER-SPECULATIVE-DECODING，Ch48；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Unforgeable Watermarks for Language Models via Robust Signatures](https://arxiv.org/html/2602.15323v1)

采用精确v1；soundness不等adaptive unforgeability→robust signatures/PPH及恢复list责任→限定编辑模型和身份归因。 必要方法、对照和直接反侧的可读位置见[首6证据](../_sources/daily-20260219/V3_CORE_FIRST_BATCH.md)中本family小节，未核代码或复现。整合：PLATFORM-SECURITY，Ch72；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Fast and Fusiest: An Optimal Fusion-Aware Mapper for Accelerator Design](https://arxiv.org/html/2602.15166v1)

采用精确v1；局部Pareto可能误剪→compatible pmapping与全lifetime reservations→限定可互换接口后裁剪。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：INFER-TENSORRT-LLM，Ch49；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [The Turbo-Charged Mapper: Fast and Optimal Mapping for Energy-efficient and Low-latency Accelerator Design](https://arxiv.org/html/2602.15172v1)

采用精确v1；dataflow隐藏placement→显式storage/currying→保留partial-relevance顺序与模型条件。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：INFER-TENSORRT-LLM，Ch49；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Protecting Language Models Against Unauthorized Distillation through Trace Rewriting](https://arxiv.org/html/2602.15143v1)

采用精确v1；答复保持不等学生学得行为保持→trace rewrite与trigger查询→输出归因/蒸馏行为分责。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Weight space Detection of Backdoors in LoRA Adapters](https://arxiv.org/html/2602.15195v1)

采用精确v1；adapter行为难验→静态五SVD sensor→制造方法/人口/holdout条件限定，与行为gate分离。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。已有覆盖：PLATFORM-EVALUATION-SYSTEM，Ch66 L215–223；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [ScrapeGraphAI-100k: Dataset for Schema-Constrained LLM Generation](https://arxiv.org/html/2602.15189v1)

采用精确v1；schema高成功不等语义value→实际telemetry/population与key/value反侧→五层success分责。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。已有覆盖：PLATFORM-EVALUATION-SYSTEM，Ch66 L49–77；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。审阅结果“标准完成”仅指作者已读必要块，不自动授独立验收或日级完成。

### [Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems](https://arxiv.org/html/2602.15198v1)

采用精确v1；CoT intent不等collusion effect→nominal/reference/regret对照→task-defined效应与judge分账。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference](https://arxiv.org/html/2602.15206v1)

采用精确v1；多feedback不应统一scalar→共享latent reward与不同likelihood/rightcensor→观测type分责。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：TRAIN-RLHF，Ch31；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Fast and Effective On-policy Distillation from Reasoning Prefixes](https://arxiv.org/html/2602.15260v1)

采用精确v1；完整rollout昂贵→student prefix早停/渐长→省计算不授完整tail或安全。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：TRAIN-RLHF，Ch31；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [ÜberWeb: Insights from Multilingual Curation for a 20-Trillion-Token Dataset](https://arxiv.org/html/2602.15210v1)

采用精确v1；多语言比例不能独解容量损害→固定ratio改变curation双向transfer→quality与mix分开。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：TRAIN-DATA，Ch27；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [How to Train Your Long-Context Visual Document Model](https://arxiv.org/html/2602.15257v1)

采用精确v1；测试时page metadata可能无效→train/infer page-interface一致→窗口/页数/评价版本分开。 必要方法、对照和直接反侧的可读位置见[新增10证据](../_sources/daily-20260219/V3_CORE_NEXT_BATCH.md)中本family小节，未核代码或复现。整合：MODEL-LONG-CONTEXT，Ch22；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[第二批owner](../_sources/daily-20260219/V3_BOOKS_NEXT_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [ResearchGym: Evaluating Language Model Agents on Real-World AI Research](https://arxiv.org/html/2602.15112v1)

采用精确v1；任务完成/工具成功不等研究改善→独立outcome与integrity边界→异步日志、cleanup和选择偏差不授有效研究。 必要方法、对照和直接反侧的可读位置见[第三批4项证据](../_sources/daily-20260219/V3_CORE_THIRD_BATCH.md)中本family小节，未核代码或复现。已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L238–245；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[本批实际owner及POST](../_sources/daily-20260219/V3_BOOKS_THIRD_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [Seeing to Generalize: How Visual Data Corrects Binding Shortcuts](https://arxiv.org/html/2602.15183v1)

采用精确v1；内容可见不等绑定可泛化→paired intervention与curriculum bundle→局部binding路径不授image-only因果。 必要方法、对照和直接反侧的可读位置见[第三批4项证据](../_sources/daily-20260219/V3_CORE_THIRD_BATCH.md)中本family小节，未核代码或复现。整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) L215/217，非作者POST通过；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[本批实际owner及POST](../_sources/daily-20260219/V3_BOOKS_THIRD_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

### [An Empirical Study on the Effects of System Prompts in Instruction-Tuned Models for Code Generation](https://arxiv.org/html/2602.15228v1)

采用精确v1；更rich system prompt不必提高代码通过→有限非单调对照→提示形式与模型/任务绑定。 必要方法、对照和直接反侧的可读位置见[第三批4项证据](../_sources/daily-20260219/V3_CORE_THIRD_BATCH.md)中本family小节，未核代码或复现。已有覆盖：AGENT-PROMPT，[Ch74](../../../../books/part-07-agent/74-prompt.md) L68–90/115–139；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[本批实际owner及POST](../_sources/daily-20260219/V3_BOOKS_THIRD_BATCH_PRE.md)。审阅结果“标准完成”仅指作者已读必要块，不自动授独立验收或日级完成。

### [Closing the Distribution Gap in Adversarial Training for LLMs](https://arxiv.org/html/2602.15238v1)

采用精确v1；jailbreak分布错配→conditional diffusion proposal+DAT→保证须harmful marginal/TV条件，不授全adaptive。 必要方法、对照和直接反侧的可读位置见[第三批4项证据](../_sources/daily-20260219/V3_CORE_THIRD_BATCH.md)中本family小节，未核代码或复现。整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) L1347/1349，非作者POST通过；实际差额/owner与邻接比较见[首批落实](../_sources/daily-20260219/V3_BOOKS_FIRST_BATCH_PRE.md)或[本批实际owner及POST](../_sources/daily-20260219/V3_BOOKS_THIRD_BATCH_PRE.md)。必要证据及具体Books处置已root独立复核通过。

首六源/实际Books POST、两个Ch49纠偏POST和两项Ch66 Existing可复用。后续已POST通过的实际位置：MAVRL Ch31 L690/692、Prefix L799/801，curation Ch27 L1245/1247，page接口Ch22 L201/203；源边界、相邻正文与末注已逐项经root实际核验，不以位置清单代替正文验收。WAC的actualCh79/80有限重提案/best-history条件已由root核为已有覆盖，无书改；其Kmax仍执行best，绝非fail-closed。

### [Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs](https://arxiv.org/html/2602.15173v1)

采用精确 v1：同一风险选择受输入表示/提示改变→描述与模拟history及解释形式反侧→固定subject后评价，不把风险中性当真值。有限非单调选择支持提示/人口绑定，不识别内部效用或训练因果；经济期望效用只作任务reference。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_FOURTH_BATCH.md)本 family 小节；已有覆盖归属 PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_FOURTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [What Do Neurons Listen To? A Neuron-level Dissection of a General-purpose Audio Model](https://arxiv.org/html/2602.15307v1)

采用精确 v1：低entropy神经元不是唯一语义地址→matched随机消融与共现反侧→分开相关、局部使用及跨域机制。分类taxonomy、阈值及背景共现限制低entropy解释；局部消融不能外推跨context完整音频机制。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_FOURTH_BATCH.md)本 family 小节；已有覆盖归属 WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_FOURTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Consistency-Preserving Diverse Video Generation](https://arxiv.org/html/2602.15287v1)

采用精确 v1：joint多样性可能损temporal一致→只移除负对齐梯度→一步代理约束不授整轨迹。first-order proxy 条件不保证有限轨迹；embedding训练混杂、Vendi与IID反侧及离线proxy成本保留，实际Ch24:192/194 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_FIFTH_BATCH.md)本 family 小节；整合归属 MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_FIFTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [On Surprising Effectiveness of Masking Updates in Adaptive Optimizers](https://arxiv.org/html/2602.15322v1)

采用精确 v1：稀疏应用不等稀疏梯度与状态→dense moments后mask/damping→不把更新稀疏称省backward。实际Ch28:421–438已承载dense gradient/moments→mask/damping→sparse application、bias/成本/checkpoint；No Change独立通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_FIFTH_BATCH.md)本 family 小节；已有覆盖归属 TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_FIFTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [The Information Geometry of Softmax: Probing and Steering](https://arxiv.org/html/2602.15293v1)

采用精确 v1：Euclidean steering不等输出KL预算→Bregman/expected-unembedding与hyperplane条件→条件最小off-target KL。采用强factorizability条件与近似Newton成本；完整distribution mixture/OR反例子命题隔离，不推倒旧Euclidean。实际Ch5:227/229 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_FIFTH_BATCH.md)本 family 小节；整合归属 WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_FIFTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Prescriptive Scaling Reveals the Evolution of Language Model Capabilities](https://arxiv.org/html/2602.15327v1)

采用精确 v1：loss不能直接推出后训练能力上限→条件分位人口与signed时间bins→限定生态边界和测量分配。q.98是已测人口而非物理极限，rolling overlap不是compute外推；成本proxy与近似分配非真最优。实际Ch7:164/166 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_FIFTH_BATCH.md)本 family 小节；整合归属 WORLDVIEW-SCALING-LAW，[Ch7](../../../../books/part-01-worldview/07-scaling-law.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_FIFTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [World-Model-Augmented Web Agents with Action Correction](https://arxiv.org/html/2602.15384v1)

采用精确 v1：sim选行动可能失败→失败rationale再proposal并保历史best→有限再提案不授fail-closed。Kmax仍执行best而非无条件停机；实际Ch79:217–230与Ch80:60–88已承载有限反馈再提案/best-history/unresolved，No Change独立通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CONTRIBUTION_DECISIONS.md)本 family 小节；已有覆盖归属 AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_CONTRIBUTION_DECISIONS.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use](https://arxiv.org/html/2602.15329v1)

采用精确 v1：固定frame保留压跨event→event FIFO与当前event reservoir→分配frame retention而非语义oracle。新frame与当前event平均histogram定义边界不是语义真值，frame-uniform不保证稀有关键帧；STM不等总memory。实际Ch77:581/583 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SIXTH_BATCH.md)本 family 小节；整合归属 AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SIXTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Discovering Implicit Large Language Model Alignment Objectives](https://arxiv.org/html/2602.15338v1)

采用精确 v1：终点难识别训练奖励→trajectory residual提出surrogate再行为检验→拟合与真实内部目标分开。Model-Fit为reward比值非variance/causalcoverage，human行为匹配非唯一目标；judge偏差与重训预算保留。实际Ch31:168 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SIXTH_BATCH.md)本 family 小节；整合归属 TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SIXTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models](https://arxiv.org/html/2602.15344v1)

采用精确 v1：memory跨时刻检索污染→已stored黑盒攻击及writer声明→写入来源治理不能由检索相关性替代。Ch72 memory-origin/权限与Ch77:66–104 writer状态实际承载；未测admission接受率，不授所有现实writer通路。No Change独立通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SIXTH_BATCH.md)本 family 小节；已有覆盖归属 PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SIXTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [MarkSweep: A No-box Removal Attack on AI-Generated Image Watermarking via Noise Intensification and Frequency-aware Denoising](https://arxiv.org/html/2602.15364v1)

采用精确 v1：信息量下降不等实际decoder准确率下降→DPI/Fano责任分离与反例→三轴验收不从MI推出攻击成功。反例MI2→1而固定decoder BA .75→.75，Fano下界非实际错误强制；局部移除/质量/成本非全部watermark保证。实际Ch72:1070 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SIXTH_BATCH.md)本 family 小节；整合归属 PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SIXTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations](https://arxiv.org/html/2602.15379v1)

采用精确 v1：fusion阻塞冷启动预取插点→weights/texture lifetime与prefetch-compute联排→冷/warm成本分账。profile/static schedule、150s feasible非optimal，warm3–12可反快，average非peak、persistentweights须计入；非servingSLO。实际Ch54:356 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SIXTH_BATCH.md)本 family 小节；整合归属 INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SIXTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems](https://arxiv.org/html/2602.15382v1)

采用精确 v1：异构agent image latent不能直接互读→各codec/hub映射→span接口和版本生命周期分账。Ch82:274–287实际已有同篇image-span codec/lifecycle、linearadapter非runtime、textfallback及Experimental；Perceiver/affine细节不另造长期段落，No Change独立通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SIXTH_BATCH.md)本 family 小节；已有覆盖归属 AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SIXTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching](https://arxiv.org/html/2602.15396v1)

采用精确 v1：独立endpoint桥退回score→先学coupling再reverse匹配→近似coupling与成本不能省。AM/CM仍交替，optimal只真正optimal coupling；forward NFE/coupling训练也付费，质量反侧保留。实际Ch24:172/174 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SEVENTH_BATCH.md)本 family 小节；整合归属 MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Logit Distance Bounds Representational Similarity](https://arxiv.org/html/2602.15438v1)

采用精确 v1：预测KL近不保证线性readability→centered gauge/σmin/τ条件→输出与表示保留分账。仅有限label等维/general-position/概率下界及可实现线性concept，readout不是causal使用；小σmin/τ令界空泛。实际Ch5:387/389 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SEVENTH_BATCH.md)本 family 小节；整合归属 WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [On the Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks](https://arxiv.org/html/2602.15460v1)

采用精确 v1：更大map可能含ID小路径→控制start-goal/path支持→ID高分不授OOD算法泛化。同模型局部任务的format/trace与预算混杂保留，map size不替代距离/path门槛，非无限planning。实际Ch66:264/266 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SEVENTH_BATCH.md)本 family 小节；整合归属 PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [LLM-as-Judge on a Budget](https://arxiv.org/html/2602.15481v1)

采用精确 v1：uniform judge预算忽略异方差→variance分配→提高固定judge均值精度非humantruth。Theorem5预算反例隔离：B条件不保证Kt0≤B；simulation resampling不是真实独立新调用，δ调参与uniform反侧保留。实际Ch66:317/319 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SEVENTH_BATCH.md)本 family 小节；整合归属 PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Approximation Theory for Lipschitz Continuous Transformers](https://arxiv.org/html/2602.15503v1)

采用精确 v1：普通attention不保Lipschitz→tied V/负Euler/compact measure函数类→条件非扩张不授实用所有Transformer。scalar交集函数类、compactdomain递推与sup计算条件保留，context另有C界，无token数近似保证非无限context常数成本；actualCh17:66/68 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_SEVENTH_BATCH.md)本 family 小节；整合归属 MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_SEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/html/2602.15515v1)

采用精确 v1：probe信号消失可能表示漂移→旧/新probe对照和reward梯度路径→evasion不等信息移除。同text/新probeAUC保信息，stop-gradient probe不冻结policy表示；长度/KL预算与alpha退化限制解释，root必要源/实际owner复核通过。 已窄授权写入，root实际正文/完整邻接与末注POST通过，锁已释放。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_EIGHTH_BATCH.md)本 family 小节；整合归属 TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_EIGHTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Certified Per-Instance Unlearning Using Individual Sensitivity Bounds](https://arxiv.org/html/2602.15602v1)

采用精确 v1：平均unlearning掩盖个体→per-instance sensitivity/Langevin certificate→经验distinguisher不等形式保证。C3 conditioned Gi 后未获得独立Gaussian条件，中心certificate证明隔离；保个体异质性经验不签证书，重开需修复条件化证明。root已独立核中心证明冲突与现有formal/empirical分责，本窗安全终态暂缓。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_EIGHTH_BATCH.md)本 family 小节；暂缓归属 PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_EIGHTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections](https://arxiv.org/html/2602.15654v1)

采用精确 v1：session reset未清长期状态→正常write-path持续感染→writer治理跨session责任。forced exposure/有限20trigger不等真实感染率或永久，memory utility未充分测；Ch72 provenance及Ch77 writer既有具体承载，root必要源/实际owner复核通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_EIGHTH_BATCH.md)本 family 小节；已有覆盖归属 PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_EIGHTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [A Note on Non-Composability of Layerwise Approximate Verification for Neural Inference](https://arxiv.org/html/2602.15756v1)

采用精确 v1：逐层容差可能放大→ReLU输出范数有界的特定扩宽反例→local检查不可自动组合端到端。特定g/M/δ与可选adversarialweights，不是固定base或FP16实测；不称全部verifier被破，actual身份/误差contract root必要源/实际owner复核通过。 已窄授权写入，root实际正文/完整邻接与末注POST通过，锁已释放。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_EIGHTH_BATCH.md)本 family 小节；整合归属 PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_EIGHTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [HIMM: Human-Inspired Long-Term Memory Modeling for Embodied Exploration and Question Answering](https://arxiv.org/html/2602.15513v1)

采用精确 v1：semantic obs过早全局融合→保留time/pose到检索投影再visual验证→semantic与几何估计分账。GT训练提取/受限物体导航与QA，Qwen部分SPL反侧及表值不同保留；检索投影非worldmodel动力学/全局fusion，root必要源/实际owner复核通过。 已窄授权写入，root实际正文/完整邻接与末注POST通过，锁已释放。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_EIGHTH_BATCH.md)本 family 小节；整合归属 AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_EIGHTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [VLM-DEWM: Dynamic External World Model for Verifiable and Resilient Vision-Language Planning in Manufacturing](https://arxiv.org/html/2602.15549v1)

采用精确 v1：计划执行不等world state生效→phase postcondition与几何反馈后DB commit→rollback不等物理回滚。GT/CAD/闭合类别、数据库entries非bits、真实任务计数差异/无ERT消融保留；不授碰撞安全/全动态保证，root必要源/实际owner复核通过。 已窄授权写入，root实际正文/完整邻接与末注POST通过，锁已释放。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_EIGHTH_BATCH.md)本 family 小节；整合归属 MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_EIGHTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Directional Reasoning Trajectory Change (DRTC): Identifying Critical Trace Segments in Reasoning Models](https://arxiv.org/html/2602.15332v1)

采用精确 v1：trace读路径不等final outcome→receiver-only fixed continuation干预→重rollout责任另验。固定stride spans、entropy/JS接收pivot选择与匹配随机对照；额外forward/selection效应不授正确性因果，actualCh5:258非作者POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_NINTH_BATCH.md)本 family 小节；整合归属 WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_NINTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [ActionCodec: What Makes for Good Action Tokenizers](https://arxiv.org/html/2602.15397v1)

采用精确 v1：重构越好不必越易policy学→overlap稳态与token依赖结构→codec和action预测分账。确定encoder conditional entropy不是真新定理，独立query非统计独立；RVQ额外训练、horizon预算与有限task反侧保留。actualCh26:163 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_NINTH_BATCH.md)本 family 小节；整合归属 MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_NINTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [TAROT: Test-driven and Capability-adaptive Curriculum Reinforcement Fine-tuning for Code Generation with Large Language Models](https://arxiv.org/html/2602.15449v1)

采用精确 v1：单一testtier不适合全部capability→预选tier分配与rewardweight→不是在线hard-first课程。capability不只params，easy/fulltests有限反侧、reference/生成及执行预算保留，actualCh31:767 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_NINTH_BATCH.md)本 family 小节；整合归属 TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_NINTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [In Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Generations](https://arxiv.org/html/2602.15456v1)

采用精确 v1：自述source偏好不等选择→固定内容交换external source label→质量与归因分别验。direct/indirect与现实news内容差异分账，context来源合理性不全判错、seller提示可有效反侧；actualCh66:279/末注5512非作者POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_NINTH_BATCH.md)本 family 小节；整合归属 PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_NINTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Co-Design and Evaluation of a CPU-Free MPI GPU Communication Abstraction and Implementation](https://arxiv.org/html/2602.15356v1)

采用精确 v1：host progress增加开销→persistentmatch预设置/GPU stream触发→有限队列耗尽责任。hostsetup/CTS-ready约束、~500DWQ/CPUblock与deadlock/fallback不能省；大消息pingpong反慢/halo不是同资源LLM全训练。actualCh36:361 POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_NINTH_BATCH.md)本 family 小节；整合归属 TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_NINTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [The Equalizer: Introducing Shape-Gain Decomposition in Neural Audio Codecs](https://arxiv.org/html/2602.15491v1)

采用精确 v1：gain已缠入latent方向→preencoder norm另传scalar→重训与gain成本不能由小码本抵消。400bps/双向非online、SI-SDR反侧及外部训练人口不同；actualCh23:257/末注1225非作者POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_TENTH_BATCH.md)本 family 小节；整合归属 MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_TENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs with GLU Activation Patterns](https://arxiv.org/html/2602.15521v1)

采用精确 v1：dense转MoE无法随意拆→profile/sharedratio与neuron对应切片→sum改softmax不保函数。25%sparsity掉分、全部weights保留、200B CPT/SFT费用和固定单GPU并发限制；actualCh21:285/末注1012非作者POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_TENTH_BATCH.md)本 family 小节；整合归属 MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_TENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Quantifying construct validity in large language model evaluations](https://arxiv.org/html/2602.15532v1)

采用精确 v1：leaderboard谱非真实能力→SEM测量误差与条件人口→统计构念不授causal。4395模型/19BBH，非wholemodelOOD，12/19局部win但p=.637，不以NS为等价；Ch66:508–514实际承载conditional matrix与人工构念复核，No Change独立通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_TENTH_BATCH.md)本 family 小节；已有覆盖归属 PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_TENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling](https://arxiv.org/html/2602.15537v1)

采用精确 v1：固定frame使tokenrate高→冻结表示边界层/内容层分工→temporalunit绑定任务质量。100h聚类/dev规则非零训练，52bps熵非wirecost，F1与lexical反侧/SSL预算混杂保留，actualCh23:47/末注1227非作者POST通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_TENTH_BATCH.md)本 family 小节；整合归属 MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_TENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs](https://arxiv.org/html/2602.15556v1)

采用精确 v1：视觉attention sink不等证据使用→interlayerdelta增强和sys补偿→heuristic不授指令mass保证。四logit反例表明visual+、sys−可压低其他mass，精确保证隔离；单A6000/λ退化与表值差异保留，root必要源/实际owner复核通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_ELEVENTH_BATCH.md)本 family 小节；整合归属 MODEL-SELF-ATTENTION，[Ch14](../../../../books/part-02-model/14-self-attention.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_ELEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [1-Bit Wonder: Improving QAT Performance in the Low-Bit Regime through K-Means Quantization](https://arxiv.org/html/2602.15563v1)

采用精确 v1：固定weight memory下bit数/容量互换→QAT format×generative任务对照→质量不等kernel速度。含scale及bf16emb/output、训练反传/KV非总memory；1bit若干任务与B1decode/大batch反侧，64H100和不同容量/FLOPs混杂保留，root必要源/实际owner复核通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_ELEVENTH_BATCH.md)本 family 小节；整合归属 INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_ELEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Beyond Static Pipelines: Learning Dynamic Workflows for Text-to-SQL](https://arxiv.org/html/2602.15564v1)

采用精确 v1：异质workflow单选有边界→finite oracle与actor availability mask训练→heterogeneity不自动严格优势。union可能等beststatic而非严格gap；pseudo confidence非truth，API预算/表值差异与mask比例反侧保留，root必要源/实际owner复核通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_ELEVENTH_BATCH.md)本 family 小节；整合归属 AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_ELEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [Constraining Streaming Flow Models for Adapting Learned Robot Trajectory Distributions](https://arxiv.org/html/2602.15567v1)

采用精确 v1：stream flow避障不能等末端projection→SPDmetric/workspace pullback塑velocity→softshape非安全不变性。Eq7 minimizer与M^-1v不符、有限SPD边界反例隔离硬安全；neural distance/点覆盖/finite rollout及费用未充分保证，root必要源/实际owner复核通过。 必要方法、关键对照和直接反侧的定位见[本批证据](../_sources/daily-20260219/V3_CORE_ELEVENTH_BATCH.md)本 family 小节；整合归属 MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，具体已有论点/差额与独立处置见[实际 owner 比较](../_sources/daily-20260219/V3_BOOKS_ELEVENTH_BATCH_PRE.md)。未核实现或复现；必要证据及Books处置已root独立通过。

### [How Vision Becomes Language: A Layer-wise Information-Theoretic Analysis of Multimodal Reasoning](https://arxiv.org/html/2602.15580v1)

精确v1 C.4 Eq16–17的R=min(MI)要求至少一unique为零，Tables3/8同row两正；root已独立核中心冲突并通过终态隔离。82%/2%及PID类别不当模型机制事实，局部knockout不绕过冲突；不写Books。重开需同estimand公式/实现与表一致的纠正原材料。 必要原文定位见[第十二批证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)，实际owner比较见[本批PRE](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)。未核实现或复现。

### [A unified theory of feature learning in RNNs and DNNs](https://arxiv.org/pdf/2602.15593v1)

精确PDF v1 §3.1–3.3/Figs2–5，独立噪声SGLD平稳posterior与μP条件下共享权重改变跨time covariance；弱信号/endpoint任务可能预测相同模式，顺序插值限匹配teacher。理论非普通SGD全训练或LLM工程比较，采样/解析有成本；Ch5参数共享论点有具体条件gap，实际Ch5:137及末注经root必要源/完整邻接/POST通过。 必要原文定位见[第十二批证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)，实际owner比较见[本批PRE](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)。未核实现或复现。

### [Revisiting Backdoor Threat in Federated Instruction Tuning from a Signal Aggregation Perspective](https://arxiv.org/html/2602.15671v1)

精确v1 §3–4，已知affected/clean group才能构造BSNR；client比例ρ与每client污染比例分账。Krum/FreqFed在低ρ有效，IID十client有限LoRA，不采根本无效全称。上游数据治理与malicious update筛查非同责任；实际Ch72:76及末注root POST通过。 必要原文定位见[第十二批证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)，实际owner比较见[本批PRE](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)。未核实现或复现。

### [A Differential Fuzzing-Based Evaluation of Functional Equivalence in LLM-Generated Code Refactorings](https://arxiv.org/html/2602.15761v1)

精确v1 §2–3/Tables2–4，4368输出去830编译/超时→3538，tests漏202/933个已检测不等价，而非全输出21%。有效输入分歧反驳程序对等价，不判谁正确，fuzz阴性非证明。Ch66:1741–1759的same-verdict/输入validator/执行反例与1834–1841保留性具体已有覆盖经root通过，No Change。 必要原文定位见[第十二批证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)，实际owner比较见[本批PRE](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)。未核实现或复现。

### [The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety](https://arxiv.org/html/2602.15799v1)

精确v1 Assumption1/AIC/§6局部Taylor与§7/Table1/D2–4；exact reference/Fisher谱/C²与curvature耦合均需成立，不授全局quartic或有限SGD保证。OS训练后测、未测曲率成本、LoRA/full预算不同、judge非truth与部分HS不升反側保留；实际Ch72:952及末注root POST通过。 必要原文定位见[第十二批证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)，实际owner比较见[本批PRE](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)。未核实现或复现。

### [CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing](https://arxiv.org/html/2602.15823v1)

精确v1 §3.1–3.3/Table1/Fig4/AppE，output Bregman在reference消一阶、局部GN；KFAC/block approximation与edited subset限定，不授非破坏全能力保证。五capbench每200及自由生成协议、任务退步/seq成本保留；runtime未明全部offlinecache分解口径。实际Ch5:436及末注root POST通过。 必要原文定位见[第十二批证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)，实际owner比较见[本批PRE](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)。未核实现或复现。

### [Dynamic Training-Free Fusion of Subject and Style LoRAs](https://arxiv.org/html/2602.15539v1)

采用精确v1；静态幅度择adapter不看实际输入→layer/step feature硬择→内容与风格冲突须分账。必要方法、评价反侧及配置见[本批必要证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)最后四项；与实际现有论点的差额/NoChange理由见[actual owner比较](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)开头，root必要源/actual owner PRE通过，实际Ch30:226/末注879一段已写，完整邻接作者已顺读，root非作者POST通过并释放窄锁。未核实现或复现。

### [One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation](https://arxiv.org/html/2602.15400v1)

采用精确v1；语言输出无metric坐标→normalized view/grid经raycast到waypoint→校准接口和controller分责。必要方法、评价反侧及配置见[本批必要证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)最后四项；与实际现有论点的差额/NoChange理由见[actual owner比较](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)开头，root必要源/actual owner PRE通过，实际Ch26:69/末注1882一段已写，完整邻接作者已顺读，root非作者POST通过并释放窄锁。未核实现或复现。

### [A Generative-First Neural Audio Autoencoder](https://arxiv.org/html/2602.15749v1)

采用精确v1；encoder高rate计算昂贵→前移downsample但decoder同构CUDA fallback→两侧分别profile质量成本。必要方法、评价反侧及配置见[本批必要证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)最后四项；与实际现有论点的差额/NoChange理由见[actual owner比较](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)开头，root必要源/actual owner PRE通过，实际Ch23:259/末注1231一段已写，完整邻接作者已顺读，root非作者POST通过并释放窄锁。未核实现或复现。

### [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/html/2602.15763v1)

采用精确v1；异步trajectory可混version/文本重编码→TITO与staleness/env分账→采样identity不授无偏。必要方法、评价反侧及配置见[本批必要证据](../_sources/daily-20260219/V3_CORE_TWELFTH_BATCH.md)最后四项；与实际现有论点的差额/NoChange理由见[actual owner比较](../_sources/daily-20260219/V3_BOOKS_TWELFTH_BATCH_PRE.md)开头，root已实际核Ch33:1373–1386同篇TITO/version/environment与1790–1812 sampledtoken/logprob责任，已有覆盖通过，No Change；proxy不授无偏。未核实现或复现。

## 5. 缺口与下一步

作者侧普通待办：0；67项安全处置、51处实际整合POST与14项具体已有覆盖均通过，2中心争议保留终态隔离。来源/准入已收口，不扩宽库存；最终六部分、来源停止范围/日期及代表EX分层抽检已root独立日级验收通过。

有限子命题隔离已在对应证据/正文处理：15481预算warm-start保证有数值反例；15364信息量下降不保证固定decoder bit accuracy下降；15567精确projection/不变集安全不成立。正面Books只采用另有依据的受限分支，不把这些保证隐藏成单纯实验限制。

本窗终态保留项（日期/目录缺口不支持当窗候选或覆盖断言；两中心争议候选不支持正面采用、Books或性能/安全保证）：

- [15602证书](https://arxiv.org/html/2602.15602v1)：conditioning Gi 后不可直接沿用无条件Gaussian独立B2；中心证书不采用、不写Books，root终态隔离通过。重开需同条件下正确证明/纠正原材料，不以经验ε代证书。
- [15580 PID份额](https://arxiv.org/html/2602.15580v1)：C4 Eq16–17与Tables3/8同row两unique正冲突；不采用82%/2%或类别机制、不写Books，root终态隔离通过；重开需同estimand公式/实现与表一致。
- [Mnemis 2602.15313](https://arxiv.org/abs/2602.15313)：arXiv identity日期可落窗，但较早完整PDF commit出现Jan28；repo当时public状态未知。需官方首次public时间、当时公开artifact归档或等效原证据；定点重开first-public，不用repo created/commit单独断日。
- [CircuChain 2602.15037](https://arxiv.org/abs/2602.15037)及[15091](https://arxiv.org/abs/2602.15091)：Submitted早于本announcement批次下界，原DOI上界无法排除更早公开；需同身份原公告或首次可公开全文证据，不能借邻ID/月归档。15091路由互信息理论不得外推GPUdispatch带宽；日期未成立不进入候选。
- [Anthropic autonomy](https://www.anthropic.com/research/measuring-agent-autonomy)：当前页modified Sep9，需Feb18初版可读快照或明确修订delta，才采用初版统计命题；已有当前core方法边界保留但不跨版本授原数字。
- Google/Meta/Qwen/DeepSeek/Moonshot/MiMo Blog/MiniMax的本窗官方历史切片：当前入口有限恢复已记录，缺原event/archive或等效官方区间目录。具体已知论文仍可独立处理，不据目录不可得称零事件。
- 2603.02240/2603.04428/2602.21247等晚登记材料：原上界跨截止，不能只凭较早Submitted落本窗；需明确首次公开时间。它们不是当前已确认候选，未授Evidence/Books。

窗外恢复线索：EVMbench RSS Feb18 00Z早于本窗，精度/初版仍需其真实归属日定点恢复；2603.10009 Submitted Feb17 19:00:43Z的官方最早公开下界已到下一窗。此处不搬入本日、不重复深审，不阻本窗完成。

## 6. 复核

复核者：root（非本报告作者）。
结论：通过

已分批实际独立核全部67项准入及受限必要原源/actual owner，67项安全处置通过（含2中心争议隔离）；51项实际正文/完整邻接/末注POST通过，14项具体已有覆盖通过。已纠正PPH predicate并非数值isometry、TCM原名/partial-relevance例外及reservation sum/max不是latency、Prefix47倍FLOPs非时间、344K窗口非336页。已通过的稳定范围不重复深审。

root实际复核四主题查询61/13/20/35均total=rows且max250，有界题名补检及Hunyuan9/9、Seed跨截止停止、Moonshot/MiniMax有限恢复范围；67项同身份Submitted/Created原字段已逐项核读，共同日程范围完全落窗，Updated不参与first-public判定。分层/重要信号样本为15034（教育应用/benchmark贡献）、15286/15288（成熟网络协议组合）、15391（安全headline与成熟detector组合）、15423（lexical检索scope）、15473/15488（通用optimizer/ANN范围）、15689（手工风险分类）、15543（编码后gating非省encoder compute）、15485（题库/成熟测试pipeline）。这10项有效准入/EX结果复用，剩余普通排除未被root全量独立复核，不称宽库存或全学科验证。

root已实际核最终六部分并通过日级语义Gate。104唯一发现lineage中67最终候选、2日期/更早公开保留，余35不是全量独立EX验证；104外15034贡献EX、15091日期保留、三晚登记材料日期上界保留及2603.10009窗外线索单列，不混候选分母。更宽title范围关闭未唯一归并，不估算总数。V3校验、67行与67证据小节一致性、51整合marker、38份作者Markdown本地链接及围栏检查通过（原始MiniMax抓取的站内链接按原host解释，不改原响应）；本日及27个实际owner文件限定cached/unstaged diff-check通过。未stage、commit或push，机器结果不授语义Gate；完成态校验再次执行，范围不扩张。旧[原样快照](../_sources/daily-20260219/V2.1-authoring-snapshot.md)仅保存旧线索，其Complete/364逐项关闭不继承。
