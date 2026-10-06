# 2025-10-24 有限筛选与必要反侧

作者 Cicero；仅 BJT [2025-10-23 09:00, 2025-10-24 09:00)。本日原响应不是已读证明，以下才是实际判断范围；没有沿用他日候选池。

## 来源、查询与停止

- [FETCH](FETCH.json) 是本日真实请求，UTC 2026-10-04 22:25～22:26。四 arXiv 查询 start=0/max_results=80，按 submittedDate 降序；发现带 UTC [2025-10-23 00:00, 2025-10-24 00:59] 不作为首次公开。model_training=4、agent=3、multimodal=3、systems=3，13 唯一家族，完整题摘实际读完。
- 模型限定 CL/LG 的 MoE、mixture of experts、long context、pretraining、language-model distillation；Agent限定 AI/IR/MA 的 memory/RAG/tool use/prompt injection 且 language model/LLM；多模态限定 CV/RO 的 world model/VLA/vision-language-action/AR generative；系统限定 DC/AR/PL/OS/PF 的 LLM training/inference、KV cache。精确 URL 在 FETCH，未分页，因为每条 total <80。
- 官方 CL 月页 skip=0/show=2000 是缓存线索，不是全文队列。身份段2510.20000～2510.23000只看前15标题，止2510.20239；完整题摘补检15身份及 Seed3D=16，[原响应](arxiv_supp.raw)及[真实请求头](arxiv_supp.headers)。合计29唯一完整当前题摘；没有把ID当日期。官方 API comment 字段实际读过，未见所读响应中的撤回/纠错文字，不推断完整版本史没有变化。当前多版本只作发现，必要反侧另读精确v1。
- [RECOVERY](RECOVERY_FETCH.json)：DeepSeek /news/ 独立Research10项实际读到OCR10/21、旧5/14；Seed article_type1/2各18项，x-tt-locale:US、publish_year2025、count20、page_token0；total94/45、next20、has_more=true，目标附近论文Seed3D10/22、quantum10/21、memory10/09，Blog10/23～9/09，已越过本日目标而停止0，不说读完全库。Z.ai page2实际18条，hasMore=false/nextPage3，最老12/07，不覆盖October历史缺段。ERNIE2末页6条，11/11、11/07、10/16到6/30；不从Preview1022型号推首次发布。
- Hunyuan 首Research壳、本日CUA getTab https://hunyuan.tencent.com/research?page=1 单次15秒超时；正确 api.hunyuan.tencent.com/api/blog/publicList POST pageNum1/pageSize200/renderType0实际9项，publicAt/displayPublishTime最早2026-02-03，不能证明2025本窗无事件。
- MiMo本日HTML实际Paper8项及日期全部读完，目标邻接10/21～9/19；Blog15标题实际读完，More不作历史页。MiniMax EN12/CN13实际标题/日期读完，EN最老10/27，CN另有1/15；Agent独立HTML及md仅2026-05-13一项，不用公司Blog代替。
- Kimi25标题/日期实际读完，目标邻接11/07～9/16；Moonshot GitHub只核首页现有pinned/current repository片段，没有历史发布页。Qwen旧首页实际5条止9/23，迁移qwen.ai/blog本日HTML200但web0行；自己的main、p_blog-index、1721三bundle有限恢复只得到动态route/import，未取得文章历史；不无限爬bundle，也不证明无事件。
- Google DeepMind首Research shell SSL失败，web恢复当前Research（Latest News8项、Publications6标题），不代表October历史。Google pubs首查错误year查询原件保留；已定点纠正 https://research.google/pubs/?category=2025&search=language%20model ，本日curl18秒超时，[请求头](google_pubs_correct.headers)，web也不可达。真实October Blog page1实际12标题，止10/09；本窗附近EarthAI10/23/Quantum10/22，停止page1不扫旧page2；Blog不代pubs。
- [EXTRA](EXTRA_FETCH.json) 本日Qwen迁移/RSS/Google月页真实请求。OpenAI首Research403；ownRSS1245记录按UTC[10/23 01:00,10/24 01:00)实际2条：Consensus09:00Z、Sky10:00Z。RSS pubDate只证明feed字段，不自动等于first-public。
- 本轮实际官方日期补检各一首屏，停于所得结果：`("2025-10-23" OR "October 23, 2025") (site:openai.com/index OR site:anthropic.com/research OR site:deepmind.google OR site:ai.meta.com) (model OR training OR inference)`；`("2025-10-23" OR "2025年10月23日") (site:qwen.ai OR site:platform.kimi.com OR site:seed.bytedance.com OR site:mimo.xiaomi.com OR site:minimax.io) (模型 OR agent OR training)`。晚近安全新闻/其他年份不转为队列。没有每周/会议/版本按需扩扫。

## 具体初筛

四项明确关闭，完整AB及理由见[FIRST小包](FIRST_CALIBRATION.md)：20666 GNSS path-loss/CNN非foundation系统；20002现成Greek模型/清洗组合未给新机制；20001临床任务综述无主线机制；20239临床特征late-fusion非基础多模态表示。不是按负面、小模型或主题已有覆盖排除。

其余25项保留具体潜力，全部日期/必要版本隔离，无评分/正面Evidence：

| 身份 | 实际题摘新增的待核命题 |
| --- | --- |
| 2510.20878 | 热度决定KV精度/存储层的TTFT质量取舍。 |
| 2510.20296 | per-request RAG-IR及成本/计划探索接口。 |
| 2510.20260 | 持续微调与RAG更新的成本/时效/知识收益可比证据，不能仅因推荐领域关闭。 |
| 2510.20475 | 按模型可预测性调mask概率及sub-token表示，BabyLM小规模不是排除理由。 |
| 2510.20377 | instruction-dialogue自监督目标缓解持续预训练损害instruction following。 |
| 2510.20278 | KAN小模型协作的调用/长尾/遗忘边界。 |
| 2510.20818 | generalist路径与机体affordance解耦。 |
| 2510.20803 | AR visual tokens直接生成mask及next-scale并行，当前v2不当历史v1。 |
| 2510.21867 | temporal-tokenizer/frozenLM/MoE轨迹预测的corner-case收益及失效。 |
| 2511.01884 | hardware feedback辅助CUDA生成；submitted10/23与2511身份相冲突，先核真实首公开/版本，不能强落窗。 |
| 2510.20171 | CTran host/GPU通信定制及FTAR弹性边界。 |
| 2510.20111 | 解耦ZeRO组与异步调度的内存/通信取舍。 |
| 2510.20154 | 自动dialect/readability分层揭示stance评估盲区。 |
| 2510.20198 | textual grid扩规模下降及自称发现与坐标正确不一致。 |
| 2510.19944 | 生成几何/PBR到physics-compatible资产的边界。 |
| 2510.20168 | 同时depth/width搜索的严格表格评价盲区。 |
| 2510.20208 | 无decode采样近似tokenization marginal的运行/精度取舍。 |
| 2510.20176 | table多Agent的MCTS伪金轨迹/RL，不仅角色分工；当前v2未当v1。 |
| 2510.20033 | AR跨层双向信息流/序列标注adaptation，不能仅按传统任务排除。 |
| 2510.20151 | RLVR边界生成/重建保真及entropy-collapse控制。 |
| 2510.20098 | adaptive routing按候选信号分配昂贵reasoning的质量/调用取舍。 |
| 2510.20043 | Bengali文化知识与context收益的评价盲区；需证据判断是否仅新数据。 |
| 2510.20059 | 少量reasoning DPO相对大数据训练的可比性，不能因小Persian模型排除。 |
| 2510.20091 | 创造性质量/新颖/多样跨域不一致；当前v3不替代v1。 |
| 2510.20036 | tool-merging/检索的选择收益与错误合并边界。 |

## 必要反侧与澄清核心（非正面Evidence）

以下12份实际精确v1原件，读到相关命题即停，未遍历全部附件。源行号指原HTML，raw下载本身不计阅读。日期仍hold，因此不宣布12候选审阅完成。

- [HA-RAG](2510.20878v1.html) II-B、III-A/C/D（310、607、910、929）：混合GSE/INT8/FP8本身有损；实验仅Llama2-7B/A10040GB、MSMARCO1000文章/512token块/TriviaQA。TTFT随warmup热度变化，前2048约1.65x后2048约2.55x；输出ROUGE-1与TurboRAG比相似不是gold答案正确，60%完全相同不等于100%质量保持；没有多租户/SLO或cache失效保证。
- [RAG-Stack](2510.20296v1.html) §4.1～4.3/5（684～950）：相同retrieval recall可换出不同文档并改变生成质量；质量须重评。IR/CM/PE是blueprint，prototype尚在建设，未把性能预测接口当实测优化收益。
- [AsyncHZP](2510.20111v1.html) §3.1、5.1～5.5（202、505～742）：未具名accelerator300+BF16TFLOPS/64GB/16卡每node、8卡fullmesh400GB/s、RoCE200Gbps，Megatron dense/MoE、16Mtoken/Gbatch。recompute/offload按需但未展开。异步消融只有102.9%与100.3%相对速度；分组/并行/调度不要合并成单一25%归因。256→1024卡linearity91.12%，变长attention成本不均仍损scale；不是异步无代价或未知GPU通用保证。
- [Collective](2510.20171v1.html) §4.5/5.3/5.5/6.3（862、941、986、1187）：zero-copy测量排除handshake，只在可重用buffer时可摊销；NCCLzero-copy微基准同样快但production buffer registration限制不同。FTAR采用replica-group shrink/grow，丢部分梯度有模型研究者协作前提，不是任意单节点失效后数学等价训练。TP小GEMM有损。推理只balanced workload，k1/4、batch128/256、host4/8/16、3次平均，不能称所有100k环境收益或零故障。
- [Seed3D](2510.19944v1.html) §7/8（755～1002）：geometry1000图测ULIP/Uni3D相似，纹理/PBR视觉指标；14人43图6方法评视觉。PBR ground-truth multiview星号上界与generated-image链路分开。IsaacSim用VLM估scale、自动collision mesh和default摩擦；支持可导入资产而非识别真实质量/摩擦/接触动力学或sim-to-real安全保证。
- [VAMOS](2510.20818v1.html) III-C/D、IV-A/C/F（612、625、642、681、859）：affordance从仿真binary traversal训练，路径最小分数重排，greedy/softsample不是验证器。receding horizon依赖low-levelcontroller和感知；Spot仿真proxy与实机controller不同。跨机体N10，另采每robot50静态图/手标stair-ramp路径+噪声微调；60→90%不外推普遍跨机体/碰撞安全。
- [WM-MoE](2510.21867v1.html) §3.1/3.2、4.1/4.3/4.4/4.9/5（395、402、612、677、717、1987～）：frozenLM特征+专家输出未来轨迹，minADE/FDE/MR为best-of-G而非闭环控制。RTX409024GB；结果仍MR非零。失败分析明确急变意图、倒车/公交停靠错误及缺robust因果机制；新增LLM延迟/内存，不能从“world model”字样推出counterfactual安全规划。
- [Stance bias](2510.20154v1.html) §3.1～3.3、4.1/4.2、Limitations：AAE只linguistic proxy不代表种族；readability不是社会经济真值；样本下采样并1000balanced重采样、5旧model同样本。F1只favor/against并另有neutral输出；dialect差别总体小，结论强于正文局部结果，不能写所有群体显著偏置或因果训练归因。
- [Spatial](2510.20198v1.html) §3/4、4.4/4.5/5：四model每配置10次，400～90Ktoken textual grids；word-search自称找到与坐标准确分开，slide每步单算以去cascade但错误原因未区分读入/内部壁障表征。只能支持这些文本任务退化，不从中证明架构不可能空间推理。
- [DeepWideSearch](2510.20168v1.html) §4.1/4.2/4.4、5.1、6.3、8：两种转换、human annotation/时间字段；Avg@4/Max@4/Pass@4区别，success严格全表相等。agents同GoogleSearch/Visit，HTML摘要成本计入；无tool模型不当等预算同能力对照。合成路径与真实wide→deep不同，低strict-success不等于全部信息不可靠，方法间difficulty差异保留。
- [CreativityPrism](2510.20091v1.html) §3/4.1/4.2/5.1/5.2（598～）：v1九dataset而当前摘要八task，不能串版本。六任务用LLMjudge；TTCT没有humanannotation仅judge互相关；CS4人机相关.55、TTCW只4可靠指标。overall只是三个维度均值比较proxy，不等普遍创造性；私有data/训练归因是hypothesis。未比较无关修订附件。
- [ToolScope](2510.20036v1.html) §4.1/4.2、Limitations、H.2/J合并必要反例（3151/3516）：CSR@k是选择集合匹配而非执行成功/权限副作用。GPT4o自动合并评判与自动纠正可能错，Command-R BFCL有-1.2%回归；相似意图/可选参数对齐不证明语义等价，J的triangle noisy-doc合并不构成任意真实API安全证明。停止于这项反侧，不遍历其他附录。

## 官方 core 的贡献关闭

- [Anthropic TPU公告](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)：实际读10/23正文容量/芯片策略。up-to-millionTPU/2026容量规划，没有公开新的并行算法、训练执行机制或可比成本测量，关闭贡献，不拿“多芯片”补通用分数。
- [OpenAI Sky](https://openai.com/index/openai-acquires-software-applications-incorporated/)：实际读收购/未来macOS整合正文，没有实现接口/安全边界机制；关闭贡献。
- [Consensus](https://openai.com/index/consensus/)：实际读Planning/Search/Reading/Analysis和contextpack/API迁移core；功能编排描述，宣传tool-calling更强但无评价协议/可归因机制，不能支持新执行/可靠性知识；关闭贡献而不是伪“已有覆盖”。
- [Google Earth AI](https://research.google/blog/google-earth-ai-unlocking-geospatial-insights-with-foundation-models-and-cross-modal-reasoning/)：本日实际读BuildingBlocks、fusion、GeospatialReasoning及Eval。专用遥感/人口/气象模型与领域工具编排；QA ROUGE/数值差与Crisiscase study没有新增通用Agent执行保障机制。领域建模主线按ROADMAP暂缓，关闭本项目贡献，不只凭标题排除。Blog日名未核全网首公开，不请求无关领域全文。
- [Seed3D release](https://seed.bytedance.com/en/blog/seed3d-1-0-released-generate-high-fidelity-3d-models-from-single-images-featuring-sota-texturing)：本日实际官方历史公告2025-10-23和DataConstruction/ModelArchitecture core读过，公开技术报告已存在而未给首次正文时刻；日名整天与窗口相交且timezone不明，不能把release日自动当论文first-public。API Paper的10/22与Blog10/23字段差异保留，仍是25潜力之一。

## Books 与交接

2026-10-05T07:39:58+08:00本日fresh定点补新Qwen Research，不重复RSS/12core/正确Google查询。独立curl `https://qwen.ai/research`200/94344字节，web0行；HTML actual routePath=/home、matchedIds layout/home、CSR无历史文章。own本日已有main.js指向p_research-index，实际下载qwen_research_route.js200/16887字节，核X=44467、GET articles合并、type=qwen_ai与language=en-US，不是恢复成功的目录。止该入口及必要route，不取全部chunks/猜API、不跨日响应复用。请求时间/状态原件TARGETED_SOURCE_RECOVERY.json，web原响应TARGETED_QWEN_WEB_ORIGINAL.json。Google正确category/search本日早先独立18秒失败已有效记录，不重试凑成功。此次源变化交root窄核，报告仍进行中/§6未通过。

0确证当窗候选、0正面Evidence、0Books提案/实际写入。不作“已有覆盖/仅报告”候选决定，不以主题联想伪owner正文比较。25项只缺精确公开bounds/必要v1身份及非作者准入确认；后续若材料到达只核对应身份/命题，先通过日期与独立校准再评分、证据和具体Booksowner比较。必要反侧已保留，不因日期hold隐藏风险。
