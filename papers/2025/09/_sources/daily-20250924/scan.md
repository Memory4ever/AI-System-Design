# 2025-09-24 作者研究记录

作者：James。窗口：2025-09-23T09:00:00+08:00 ～ 2025-09-24T09:00:00+08:00。只处理本日，21已释放；不写共享文件、不授FIRST/Evidence/DAY。

本次实际请求自2026-10-06T05:20:13Z开始。原URL、状态、执行时刻、分页/请求体分别在 [fetch-results.json](fetch-results.json)、[arxiv-pages-fetch.json](arxiv-pages-fetch.json)、[deepmind-page-fetch.json](deepmind-page-fetch.json)、[source-narrow-fetch.json](source-narrow-fetch.json)、[current-core-fetch.json](current-core-fetch.json)、[arxiv-advanced-fetch.json](arxiv-advanced-fetch.json)、[month-related-fetch.json](month-related-fetch.json)。对应原响应未覆盖、未删除。解析文本不是声称全文深审。

## 来源范围与真实停止

| 来源 | 本日执行、读到哪里、停止依据 | 有限差额 |
| --- | --- | --- |
| SRC-OPENAI | Research实际403，保留error原响应；官方RSS按本窗ISO过滤得Stargate一项。实际通过web打开并读[官方核心](https://openai.com/index/five-new-stargate-sites/)全部主体。 | RSS替代发现不等于Research历史全集。 |
| SRC-ANTHROPIC | Research原HTML中`self.__next_f.push`JSON字符串还原，172个publication对象保存[原字段](ANTHROPIC_publications.json)。本窗`publishedOn`过滤无对象；2025年9月可见最近15日两项、5日biorisk，不把当前网页卡片当历史零事件。 | 172个返回对象不是全机构/全部artifact。 |
| SRC-GOOGLE-AI | DeepMind Research首查；`blog/?page=5`虽200但忽略参数，明确不授历史覆盖。实际链接恢复为`/blog/page/5/`，24卡片从Nov2025至Jul2025，跨9月。Robotics1.5原页`article:published_time`和JSON-LD均`2025-09-25T00:00:00+00:00`，窗外。FSF相邻22日事件不继承审阅；天文/流体标题按暂缓科学范围关闭；ICPC/VaultGemma邻近较早项不扩。本日Google Research `/blog/2025/09/`首12从9/30至9/11跨窗，9/23TimesFM完整核心已读，精确2410.24087v1定点核旧机制；9/24AfriMed-QA属暂缓医学应用，不深读。Publications首页1–15/11588仅年份字段，不授日窗。 | Blog有限可见夹窗；Publications缺日级历史精度。 |
| SRC-META-AI | 首查动态Research；本次results真实page4是Dec/Nov，page5实际Nov18→Sep15，停止于过窗。不能继承搜索缓存page4/5。实际读CWM、CaT、Preparedness、MetaEmbed四原页完整题摘，保留HTML和元字段抽取。 | 无ISO/带时区公开字段；Preparedness列表9/23、正文9/24冲突。 |
| SRC-QWEN | 首页可见目录及本日实际`api/page_config?code=research.research-list`60对象；严格UTC→BJT本窗过滤0。Omni/TTS属于22，ImageEdit/Guard/Travel/VL/Live属于23；Max`2025-09-24T04:00:00Z`是25窗，不扩大24。 | 官方返回60配置对象，不授全站历史完备。 |
| SRC-DEEPSEEK | 官网及准确`https://api-docs.deepseek.com/updates/`实际请求。全文相关更新段最近9/29与9/22Terminus，后者语言一致性/Agent正确性信号不因泛泛release标签关闭。 | 原`Date: 2025-09-22`无时区/时刻；不以猜测授相邻日报归属，未采用。 |
| SRC-MOONSHOT | 本日Blog完整可见25项，最近前缘9/16、9/5，后缘11/6；停止可见单页。 | 无仓库全量历史覆盖保证；无本日相关原发布线索触发全仓遍历。 |
| SRC-TENCENT-HUNYUAN | Research壳首查，实际正确POST`api.hunyuan.tencent.com/api/blog/publicList`，body`{pageNum:1,pageSize:100,renderType:0}`；9条/total9全当前返回。 | 当前9项不支持2025年9月历史覆盖，不写0。 |
| SRC-ZAI | 两次Research原JSON，首`blogsItems`15，page2累计18，`hasMore:false,nextPage:3`实际字段；最早可见Dec7，日期并非严格降序。 | 当前分页读完不是目标历史覆盖；不把featured重复卡片计为新条目。 |
| SRC-BYTEDANCE-SEED | Research/Papers首查及2025 type2 API page0 count20实际15/total49，has_moretrue,next20；非置顶已到Jul15，本日无可见对象，有限越窗停止。type1默认及Locale CN实际均total94,has_moretrue,next20，但缺`sub_article_list`。 | 置顶与年度结果不能称49项全读；Papers不是0，缺列表保留。 |
| SRC-BAIDU-ERNIE | 中文两真实页，page2标1/2回第一页；全目录读到Jun30，前缘Oct16、后缘Sep12/8月，9/24无可见项。 | 当前两页有限目录，不授历史删除/其他artifact完备。 |
| SRC-XIAOMI-MIMO | 8 Paper条目已读，近邻Sep19→Oct21；15 Blog条目已读。`More`是`aria-controls=blog-more`本页展开，6个隐藏条目已在原HTML，不是尚未执行的外链/分页。 | Blog缺发布日期，不授日窗/全仓历史。 |
| SRC-MINIMAX | 英文首12 dated items，?page2实际仍同12；中文实际13 dated items，尾Jan15，有限夹窗。Agent技术索引和llms.txt均实际首查，可见May13 2026一项。 | 中文越过Jan15不是完整历史；重复英语页不是第二历史页。 |
| SRC-ARXIV | 下节真实主题三页208、月列表有限标题101及34补题摘，官方day路径400；advanced表单实际解释announcement只支持年月。 | 提交≠首公开；月记录未公开日粒度，后续版本不得反推历史。 |

## 已读官方核心的贡献关闭与保留

### Stargate

官方2025-09-23T14:00:00GMT（RSS原值）落窗。读到计划五站/7GW、三年资金、capacity部署以及Abilene已运行OCI/GB200、6月首次交付。不能把已运行事实改成全是未来计划，也不能把10/22Wisconsin页面后加update当9月增量。原文没有新的训练/推理执行机制、可比质量/资源边界或设计失效条件；关闭其本次技术贡献，不以金额/算力规模准入。web可读原文，Research403不是这项核心缺失。

### TimesFM-ICF

本日[Google原核心](https://research.google/blog/time-series-foundation-models-can-be-few-shot-learners/)已读：learnable common separator、续预训练、跨例因果attention、23数据集结果。再实际读[2410.24087v1](https://arxiv.org/html/2410.24087v1)§4.1/§4.2、Figure3及直接相邻§4.3，separator和跨例注意已是旧版机制。Blog本次重述未指明新的release/重要修订，关闭reexposition；不以AI for Science关闭时间序列模型机制，也不重新采用宣传性能。

### Meta四项

- [CWM](https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models/)：静态代码训练限制→Python/Docker observation-action中训轨迹、stepwise execution simulation→需重考虑代码规划的环境预测监督。正文9/24，无时区。只读题摘，未读PDF、不采纳65.8%等。
- [CaT](https://ai.meta.com/research/publications/compute-as-teacher-turning-inference-compute-into-reference-free-supervision/)：无ground truth时选多rollout仍受样本候选限制→frozen anchor综合矛盾/遗漏可产出不同于多数的参考，分别programmatic equivalence/rubric reward→重考虑生成型教师而非仅选择型教师。正文9/24，无时区；题摘是恢复时当前版本，未采用数字。
- [MetaEmbed](https://ai.meta.com/research/publications/metaembed-scaling-multimodal-retrieval-at-test-time-with-flexible-late-interactions/)：单向量损细节、全token多向量索引昂贵→meta tokens+Matryoshka multi-vector training、可选索引/late-interaction token数→质量/索引成本按表示粒度调整。正文9/23；本日实际恢复2509.18095v1完整题摘，身份同家族，不重复计。
- [CWM Preparedness](https://ai.meta.com/research/publications/code-world-model-preparedness-report/)：完整题摘含风险域及misaligned propensity评估，只报告作者release判断；摘要不足证明“无额外风险”。列表9/23与正文9/24不一致，无公开时刻。安全项保留，不机械按一般模型card关闭。

四项均不得因当前无精确落窗而改判无贡献；等待原事件时区/公开区间/正式批次和相应精确版本后局部重开，不预授候选或评分，不下载所有附件。

## arXiv 有界发现与完整题摘

实际查询URL在fetch记录。12分类：cs.CL/LG/AI/DC/CV/RO/AR/PL/OS/PF/IR/MA；主题：language model/Transformer/LLM/foundation model/world model/vision language/GPU/large model。提交筛片`202509221800 TO202509231800`只是拟定位24日公告的线索。start0/100/200返回100/100/8，total208，停止于真实总数，跨分类去重208 ID；不是208篇当窗新论文。

[arxiv-query-entries.json](arxiv-query-entries.json)保留全部API原始完整title/abstract/published/updated/current-version。208标题均浏览，49明确领域标题留在[title-scope-excludes](arxiv-title-scope-excludes.json)，159相关/含糊条目的完整题摘实际全部读完（索引0–158）；[selection](arxiv-related-selection.json)。标题排除是疾病/MRI/ECG/分子/PDE等暂缓科学应用，领域预测/食品/传统语料等非foundation机制；没有以小模型/编译/理论/负面/无新通用原则作统一排除理由。标题排除49须由root分层抽检，非作者未核不称全量验证。

月份正确ISO路径已恢复first2000/2214，不重抓、也不补完剩214。月列表只为查漏浏览2509.17881–19280共101个标题（含相邻/跨分类条目，不是公告批次）；其中50已在主题查询，51新增，17明确领域/暂缓标题关闭，34相关/含糊者逐个取**v1完整题摘**，全部200且读完，保留[身份](month-related-selection.json)、[原请求](month-related-fetch.json)、[题摘](month-v1-title-abstract.json)。v1标题与当前月标题不同的Spiffy/TruthV/PiMoE按v1原值，不 silently覆盖。

### 已读159中35项的具体关闭

此处只关闭项目范围或具体贡献；日期未核不另索要不影响关闭的材料。其余124仅**潜力/待日期**，不是已准入/已证实，绝不按补集声称全文审过。

| ID（API当前版本原值见selection） | 关闭的具体依据 |
| --- | --- |
| 2509.19165 | RoSe把既有foundation先验接入立体匹配CNN、天气合成自监督；题摘给任务准确率，未提出foundation表示形成或通用执行边界。 |
| 2509.19125 | 论文分类aspect摘要+动态聚类/新taxonomy标注集；未改变模型/Agent执行或评价盲区，只提升该组织任务。 |
| 2510.01231 | summarization中Bayesian不确定性+熵/risk loss+提示的组合；题摘没有区别于既有组件的校准/风险接受机制或可靠性条件。 |
| 2509.19112 | event-sequence causal graphs用于车辆fault/disease标签推断；领域原因发现，非模型能力形成理论。 |
| 2509.19012、2509.18970 | VLA及Agent幻觉综述新增taxonomy/方向/归纳；题摘未给修正具体系统选择的新比较或反证。并非所有综述一律排除。 |
| 2509.18937 | 语言转机器人手几何/3D打印参数；形态设计应用，非动作学习/闭环控制的新机制。 |
| 2509.21380 | intra-class clustering采样只用生物医学影像评价；本次暂缓科学应用，不借Data owner引入。 |
| 2509.18864 | profiling中confidence合成标签/加权投票/蒸馏/RL加权；没有新增可信度语义或误差控制条件，只有该任务F1。 |
| 2510.01229 | synthetic query、LLM分类hard negatives、既有LCE的小reranker训练组合；未给新负例机制或可比成本边界。 |
| 2509.18826 | LoRD通用图聚类约束优化；题摘未建立模型表示学习或foundation训练的直接链路，不能仅因有收敛证明准入。 |
| 2509.18813 | MAPEX将招募/提取/topic/knowledge/postprocess按文本长度分支；只是既有Agent步骤适配keyphrase任务，无新执行/可靠性条件。 |
| 2509.18790、2509.18761 | CodeBERT/Longformer检测IaC smell、LLM协助人工校正扩taxonomy；通用软件安全应用，不等于LLM系统安全约束增量。 |
| 2509.18776 | AEC五认知等级/工程题集/专家rubric显示领域知识任务下降；未识别超出该领域的评价混杂或新增控制条件。 |
| 2509.18742 | temporal GNN加LLM近期窗口+global RNN-like prompt链；主要destination retrieval领域任务，无能力形成机制或执行增量。 |
| 2510.07325 | vulnerability co-exploitation MGNN architecture search；非LLM/foundation系统机制。 |
| 2509.18713 | MemOrb客服反思写共享库/检索，pass^k只作任务稳定性度量；未新增memory写入冲突/更新/可靠性机制，不能把既有反思原则计作delta。 |
| 2509.18710 | DataAgents位置报告列已有规划/grounding/tool及未来方向；无实际新执行机制或成立条件。 |
| 2509.18683 | LEAF-Mamba用于显著目标检测的局部模块+融合；领域方法改造，非本项目foundation状态取舍研究。 |
| 2509.18672 | NaviSense AR/LiDAR/对话/音触指引组合及12人应用体验；未改变基础模型或Agent执行边界。 |
| 2509.18661 | AutoSurvey四专门Agent流程+judge分数；没有超出既有组合的验证/可靠性机制。 |
| 2509.18636 | 编队DVS/Lloyd/Hungarian/轨迹优化；传统控制规划，无模型驱动动作机制。 |
| 2509.18571 | 视频威胁应用semantic tuple/去重/CoT组合；未提出foundation视频状态或可复用执行机制，CoT不证明可解释性。 |
| 2509.18523、2509.18520 | LLM把法律/安全资料编成weighted graph用于既有coherence推理的早期应用，非新模型或推理机制。 |
| 2509.18514 | ByT5既有denoising/curriculum应用到阿拉伯诗节奏；任务适配而非新生成factorization。 |
| 2509.18461、2509.18394 | deepfake零样本策略/AI风险建模概览；未给新增攻击、约束或有效性证据，不用overview风险标签自动准入。 |
| 2510.01226 | ClaimCheck小模型搜索/摘要/重检索/判定任务流水线，披露较高accuracy和组件消融但题摘未说明新执行机制或可比资源边界。 |
| 2509.18405 | check-field detection冻结VLM/MLLM应用及110支票数据；无新增基础表示/Agent机制。 |
| 2509.18401 | Persian文学四创造维度/设备+judge人类一致性；题摘是领域生成能力描述，未发现新的judge混杂/失效条件。 |
| 2509.18386 | GNN道路拓扑/Transformer轨迹异常；领域预测模型，不建立foundation机制关系。 |
| 2509.18383 | GPT-5求未解数学猜想，属于暂缓科学研究，不以数学benchmark名重新引入。 |
| 2509.18376 | GNN exemplar coverage+LLM编自然语言规则用于GNN解释；未形成LLM表示/可验证解释的新机制。 |

### 保留的局部/负面/理论/安全与系统潜力样本

以下均实际完整题摘读过，不采用性能、安全保证；是对日期保留项的研究方向说明，不给分。其余潜力的题摘原字段在selection，恢复时按具体命题而非159篇全文队列处理。

- 2509.19128 PipelineRL：同步/异步RL新鲜度压力→in-flight weights更新持续生成→重考虑利用率与on-policyness；2509.18521 APRIL：长尾rollout阻塞→超发、暂停未完、下步续跑→保留样本与staleness并列；2509.19086 SJA概念：MIG固定任务碎片→scheduler先公布slot、job后物化safe subjob→新协商执行边界，概念缺实验不是无贡献。
- 2509.19117 vulnerability模型受代码metric混杂；2509.18632 Planorama用户喜好不预测实际帮助；2509.18862多特征检测极小收益伴4.2x开销；2509.19088个体digital twins五类失真；2509.18762 long SFT帮助short却偏context知识；2509.19207长caption训练迁移受grounding/更新预算/位置冻结限制。全部局部/负面保留，不因未改变“通用原则”排除。
- 2509.19189 kernel intrinsic-time learning曲线；2509.19058 observable-source辅助识别；2509.18389固定Transformer存在policy-evaluation预训练minimizer实现ICRL；2509.18750受控multilingual shared vocabulary实验。理论/小模型不是范围外标签，必要假设未审，当前v2/v4不反推v1。
- 安全/设计反证潜力：2509.19212 SafeCoDe、2509.19143跨语言red-team、2509.18836 bounded-PCTL、2509.18792 model-diff安全/幻觉latent变化、2509.20393 Secret Agenda SAE标签失效、2509.18575 ranking injection、2509.18557白名单、2510.01228层级冲突、2509.18382 compute约束安全、2509.18886 CPU/GPU TEE、2509.18311 keyed robot policy隐私、2509.18874广告推断隐私。这些不作为“仅安全应用”简单关闭，也不把白名单/TEE性能宣言授保证。
- 多模态/动作潜力：19269 representation prototype alignment、19244 Lavida-O分支生成/理解、19203 LexiCLIP、19191几何位置、19018 OmniBridge、19047 FMT异频模态、19080World4RL、18953Eva-VLA反例、18816音频attention干预、18778VGGT cache、18579跨来源/层蒸馏、18570 task-selective speech fusion、18428 latent actions、18369Bengali grounding、18282PEEK中间表示。仍需日期与对应精确版，未把后续版本结论当9月事实。

### 月补34的处置

9项贡献关闭：17921（decontext内容selection/planning任务pipeline）、17946（HICode归纳labels+cluster任务）、18063（ARK既有迭代KG Agent）、18156（文本event-causality领域推断）、18008（HCI实验平台，非Agent新执行）、18122（GAUSS新技能分类/profile而非已识别评价混杂）、18174（Baseer阿拉伯OCR既有fine-tuning和数据）、18200（ASR/坐标三步CoT与curriculum任务组合）、18436（Memory-QA时间/位置多信号检索组合，没有新memory更新约束）。剩25潜力/待日期。

重要保留：17930encoder-tree共享翻译/CTC；17932 MLP truth signal；17938 D-REX最终输出/CoT不一致（可见CoT不等于真实内在意图）；17995强generator难检错/强verifier仍失效；18010 attention只解释部分saliency；18052 PIMMUR控制confound后现象不出现；18093 SEQR norm-max routing理论；18163 thinking放大误导context；18167 process-supervised检索停止；18360 speech embedding alignment；18585 rank/data质量联动；18655 edit KG一致性；18987 DTW跨模态；19020固定compute大模型较优且低资源reranking质量下降；19163主观slop labels；18083 procedural RLVR；18085 v1 Spiffy dLLM分布保留draft graphs；18091 industrial ranking block-wise latent机制；18095 MetaEmbed；18127 Safe-SAIL；18169 v1 PiMoE token路由；18173 route逆向failure；18531可验证CER reward却韵律坍缩。最后一项对TTS reward选择具有直接主线负面价值，不能当call-center应用排除。

## 日期终态隔离与重开

arXiv当日路径实际400；本日advanced原表单实际200，说明`announced_date_first`过滤**只支持年月粒度**。月份ISO页和API`published`均不能独立确认初次日级公告。208中存在2510编号、9/23提交却后续10月分配/公开的记录，且多数current v2–v5更新在2026；这直接反驳“截止提交就全落24窗”。不以submitted、DataCite、当前版本或请求成功伪造首公开。不机械要秒级时刻：若官方原公告批次/版本历史/原release能支持整个BJT公开区间落窗即可接受。

本日潜力题摘149条（124+25）仅发现记录，不是149个formal candidates；MetaEmbed和机构原页同家族，跨源不增数。首公开归属未解决的项不评分、不正面Evidence、不Books。重开条件：具体ID的官方原first-announcement批次或作者正文/release原公开区间（完全落窗）+对应精确版本，优先PipelineRL、APRIL、TEE、SJA、负侧与安全样本；其余按同样条件定点，不重扫月库存。现有主体列表、原fields、day400/advanced月粒度局限须交root独立核，不以“0formal”声称无遗漏。

## 作者handoff：24日

作者扫描/标题与必要完整题摘/本日可执行恢复普通待办0；正式候选0、评分0、证据深审0、Books拟增量0/实际0。不是Day或Coverage/Evidence通过。主报告保持进行中等待具名root DAY；根复核应先查真实范围/208vs193题摘/日期版本隔离，再分层抽检35+9贡献关闭、49+17标题关闭（重点ClaimCheck、MemOrb、RoSe、GAUSS，与TTS-prosody/Planorama等保留负侧对照），以及Meta Preparedness安全保留。Books建议为本次未采用项的No Change，不是声称现有Books已覆盖所有潜力。
