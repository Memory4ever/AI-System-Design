# 2025-09-23 独立研究停点（James，进行中）

窗口：2025-09-22T09:00:00+08:00 ～ 2025-09-23T09:00:00+08:00。启动/恢复按AGENTS及当前研究、Report合同、来源清单Daily/arXiv组执行。仅本日重新请求和材料，不继承其他日期候选。

## 实际源请求与停止

`fetch-results.json`保存本日各机构首查与可执行目录请求，`targeted-fetch.json`保存具名核心及首次arXiv主题请求。原响应原样保留。

- OpenAI Research403，官方RSS本窗3项：CNA newsroom、SchoolAI及NVIDIA systems partnership。前两项题义为业务应用，没有模型/系统机制或纠错信号，范围前关闭。第三项原官方核心已通过web实际读取：意向合作、逐步投入及未来部署规划，不披露新的执行机制或已实现性能/可行性边界，贡献前关闭；不把计划10GW或投资额度当已建容量。原URL `https://openai.com/index/openai-nvidia-systems-partnership/`；RSS pubDate为2025-09-22 08:45 GMT，在本窗。RSS不等同完整Research历史。
- Anthropic本日Research的Next.js字符串JSON实际解析172个publication对象，保留publishedOn原值；9月可见09-05/15及后续09-26，本窗没有对象，不称全网无事件。
- Google Research本日September Blog首12项09-30→09-11有限跨窗；Publications仅年级日期，隔离。TimesFM本日核心及精确2410.24087v1完整题摘已读，待定点核separator机制是否已在原文，不因时间序列foundation model将其误列AI for Science。DeepMind本日page5六个9月标题，FSF自身原HTML datePublished=2025-09-22T00:00:00+00:00，属于前一Daily窗口，不扩23；当前正文2026更新不能作2025政策。原gzip响应及解压副本均保留。
- Meta首查后实际page5，publication可见11月→09-15跨窗，但不同type分别排序，不授全站连续覆盖。ARE完整题摘、MetaEmbed及CWM Preparedness官方完整题摘已通过web实际读取；后两项本日原响应补取中。MetaEmbed compact多向量及Matryoshka多粒度训练改变质量/索引/查询成本选择，潜在贡献保留；date-only09-23未给时区。Preparedness列表09-23而正文09-24，日期冲突保留；安全评价主张不能只据摘要采用。ARE date-only09-22也不能确定落本窗。
- Qwen首页可见09-23→08-19；Qwen3Guard具名官方页实际200，核心/示例已读，见下段拟入选。
- DeepSeek官网与实际 `https://api-docs.deepseek.com/updates/`、Terminus原说明实际新取；09-22 date-only仍缺落窗区间，语言混合/random characters与Code/Search Agent正确性信号保留，不按未披露架构排除。
- Kimi Blog可见09-16/05，ERNIE实际两页09-12均窗前；MiMo可见09-19早于本窗，不授first-public。只关闭本日有限可见切片，不声称未列事件不存在。
- Hunyuan正确publicList本日返回9/total9当前项，不恢复2025历史；没有沿用别日11计数。
- Z.ai首 `blogsItems` 数组15，实际page2累计18、hasMore=false、最早12-07；目录不恢复9月。递归JSON另有featured对象，初始20对象/16ID派生输出保留但不作首列表计数；正确列表见 `ZAI_blogsItems.json`、`ZAI_P2_blogsItems.json`。
- Seed2025 type2实际15/49、has_more=true，非置顶跨09-09至07-15，停第一页；type1 total94缺sub_article_list不是0论文。
- MiniMax本日英文首页与page2相同12dated items，不是真分页；中文实际13项10-27→01-15有限夹窗；Agent与llms索引当前1篇2026-05-13，没有可执行历史分页，完整性未知。

## 首批准入：Qwen3Guard（待root）

官方事件 `https://qwenlm.github.io/blog/qwen3guard/`。`QWEN_GUARD.raw`原meta article:published_time/modified_time及JSON-LD datePublished同为 `2025-09-23T04:00:00+08:00`，完全落本窗。核心全文及使用示例见原响应和 `QWEN_GUARD.txt`。不伪造秒级或从显示日期补时区。

准入链：完整响应后置审查无法及时干预流式输出，二元标签也难兼容不同安全严格度→Stream在Transformer最后层加两个分类头、逐token接收并保持stream_state；Gen提供Safe/Controversial/Unsafe三档，可按策略映射中档→需要区分检测粒度、策略阈值与输出提交/拦截时序，而非将安全分类分数等同安全交付保证。

拟入选1家族，待root FIRST-QWEN-GUARD-23；未自授准入、未评分、未授深入审阅。安全约束变化将按研究合同§4深入受影响内容。119语言及0.6B/4B/8B是作者发布事实，benchmark优势、响应延迟及不损helpfulness需要原协议；不从标题SOTA采纳。

历史版本恢复：Blog指向GitHub main技术报告，当前PDF真实下载见 `qwen-report-fetch.json` / `Qwen3Guard_Technical_Report.pdf`；未称其是当时版本、未声称全文读完。截止2025-09-23T01:00:00Z的该路径commits和全repo commits API分别实际200返回`[]`，保存 `QWEN_REPORT_HISTORY.raw`、`QWEN_ALL_HISTORY.raw`与请求日志。不据此断言当时未在其他路径公开。后来arXiv2510.14276不是9月首次公开证据。必要性能/训练证据若只能取得后版，应明确隔离；Blog可独立支持已披露的机制描述。

## arXiv实际失败与有界补检

按十二分类ROADMAP主题及同义词，submittedDate202509191800～202509221800仅作计划周一20EDT公告的发现线索，不是ID公开日期。原查询完整URL保存在 `targeted-fetch.json`；04:23:21Z第一次429，04:27:47Z第二次429，见 `arxiv-retry-fetch.json`，不是空事件。

本日官方day路径 `/list/cs.CL/2025-09-23`实际400；ISO月目录 `/list/cs.CL/2025-09?show=2000`实际200，首2000/2214原响应保存。辅助web三条 `site:arxiv.org/abs "Submitted on 22 Sep 2025"` 加LLM/vision language/GPU首返回页未命中，不授召回或零事件。后来main arxiv.org替代API相同主题请求04:46:10Z仍实际429，见 `arxiv-main-fetch.json`，至此三次失败，不无限重试。

已实际补检月目录2509.16204～2509.17880的171标题（`month-title-slice.json`），按相关或含糊语义选126读取精确v1完整题摘（`month-related-selection.json`、`month-related-fetch.json`、各 `2509.*v1.abs.raw`）；没有取126全文。原始月号/ID相邻不是日级公开证据。题摘派生合集 `month-v1-title-abstract.json` 126项全部实际读取，网页可见撤回/纠错关键词轻查没有恢复到需处理的撤回字段；不因此宣称遍历完整版本史或不存在勘误。

保留潜在机制、局部/负面证据举例：16278 meta-token attention/长度外推；16400控制SES档案下解释放大偏差；16462去偏与下游公平不一致；16487同evaluator相关度和SFT收益饱和；16596更多SFT数据可能损伤知识；16660检测toxicity的neuron不等于生成expert；17317机器翻译简化语料的负迁移及native适配；17349流式翻译latency指标的segmentation混杂；17418视觉拼写检测不等于纠错；17481缺失/矛盾chart信息的hallucination盲区；17570等预算相关采样的diversity/quality取舍；17879Wasserstein分布变化评价上下文persuasion，而非只看greedy回答。16686 EG-MLA、17238 RoE、17396 EpiCache、17737 compositional token压缩分别保留实际架构/资源取舍；16866 seqBench和16941 SWE-Bench Pro保留受控任务复杂度/统一scaffold的评价失效边界。16411层级retrieval维度假设与long-distance失败、16442合成增强规模收益递减/小生成器与pretraining依赖、16548 MC step标签噪声的自去噪、17393测试输入主动排除有限程序假设也是可核贡献。以上都缺必要日级公开证据，不入当窗确定候选、不采用数字、不开全文队列；取得官方日级公告或可支持完全落窗区间才定点重开相应ID。

贡献前关闭代表：16241仅程序求解流程/准确率增益，未给新机制或条件；16264偏差展示平台未给新增模型机制/受控反证；16325 agent overhearing taxonomy/建议未给新增执行或可靠性证据；16597用MCP与control术语改写模块组合，无具体新控制约束；16679生命周期RL综述未指认新增分析/修正；16713 interactive drama工具组合无新适用条件；16990已有GRPO作用于speech及BLEU收益，未识别新机制/质量资源可比边界；17829滑窗/摘要/entity context模块与总体指标不足以证明新状态机制；17834工业FMEA应用已有foundation model，不建立当前模型/系统机制链。16226科学归纳任务、17552只以分子任务证明non-text in-context representation按当前AI for Science边界关闭，不借通用owner绕回；17047是人类语言处理read-time研究，非模型能力形成证据；17844是人类argument appraisal语料研究，非LM安全/系统新机制。日期未核实不影响这些具体处置，不继续追日期。其他题摘存在潜在增量或决定事实含糊的均保留，不因局部、survey、未披露实验细节或没有普适规律机械关闭；全文审阅仅在日期和独立准入后围绕命题开展。

本源终态限制只是当前可用主题API/日列表不能恢复公开归属及月标题有限补检，不授正面Coverage、零事件或无遗漏。未来官方历史日列表/announcement原记录恢复时，只重开本窗和具名ID，提交时间/DataCite注册不作为替代。

## 已完成定点核验

TimesFM：`GOOGLE_TIMES_V1_HTML.raw/.txt` 为2410.24087v1真实正文，§4.1/§4.2/Figure3已提出共用learnable separator、跨example causal attention，并解释多线性trend拼接为triangle-wave的混淆。2024-10-31v1已公开的机制在本次Blog再次说明，没有发现新重要修订/设计增量，贡献前关闭；不是因其时间序列任务机械排除。原core与题摘此前已读，后来正文实际定点读取日志见 `initial-narrow-fetch.json`。

Meta：本日MetaEmbed及Code World Model Preparedness原HTML均成功200，见 `initial-narrow-fetch.json` 与 `META_EMBED.raw/.txt`、`META_PREPAREDNESS.raw/.txt`。完整摘要实际读到MetaTokens紧凑多向量、MatryoshkaMultiVectorRetrieval的查询/索引粒度；保留质量-资源选择，不据MMEB/ViDoRe32B宣传采用。Preparedness正文09-24而page5列表09-23，安全/误对齐propensity主张不据摘要授无新增风险。对两个原HTML的meta、time/datetime及datePublished/publication_date/publish_time/ISO日期定点提取未恢复带时区发布字段。ARE原题摘09-22 date-only同样隔离，不推造时区。

Qwen3Guard repo：`QWEN_REPO.raw` 本日官方API created_at=2025-09-23T08:13:20Z，晚于截点2025-09-23T01:00:00Z；能解释截点前GitHub历史空数组，但不能否认本日04:00北京Blog原发布日期，也不能证明当时其他渠道报告未存在。性能/训练/有效性命题必要当时版本未取得，保持不采用后版；Blog明示架构/标签/使用时序可独立审阅。仍待root FIRST-QWEN-GUARD-23，未先评分。

## 窗外Qwen3-Omni恢复（只交22 owner/root）

本日有界题摘发现2509.17765v1潜在Thinker/Talker MoE及multi-codebook AR/causal ConvNet首frame speech机制，随后实际请求官方README、Blog和截点前路径commits。当前hash Blog只应用壳，没有正文；官方脚本 `p_blog-index.js`/`969.js` 恢复原 `/api/page_config?...code=research.research-list`。此接口实际返60目录对象，未扫描全60正文，定点提取id=qwen3-omni：原date=`2025-09-21T21:00:00.000Z`，北京22日05:00，落22窗。`tokenLinks=https://docs.qwenlm.ai/research/qwen3-omni/index.json` 实际200并读Architecture/Performance核心；当前hash `/api/v2/article/` 返回Article does not exist，保留原记录，不称0事件。请求分别见 `qwen-omni-fetch.json`、`qwen-omni-recovery-fetch.json`、`qwen-blog-js-fetch.json`、`qwen-config-recovery-fetch.json`、`qwen-omni-config-fetch.json`、`qwen-omni-article-fetch.json`。4467.js一次404系实际CSS-only chunk ID错误，随后真实脚本路由恢复，不掩盖失败。

原JSON `QWEN_OMNI_CONFIG.raw`、原tokens `QWEN_OMNI_TOKENS.raw` 与 `QWEN_OMNI_CORE.txt` 供root核日期/准入；官方历史README `QWEN_OMNI_INITIAL.raw` 精确ae5dbf9e734b7c72c1a70805cfb321b5fa3e9615，author/committer date=2025-09-22T16:05:18Z，不直接等于公开。核心说明Talker每步主codebook/MTP残余codebooks/Code2Wav增量waveform，潜在增量清楚；211ms/507ms是Blog宣传，v1摘要234ms是theoretical cold-start first-packet，不能合并为实测收益。历史PDF可从同commit assets/Qwen3_Omni.pdf定点取得，不用main反推版本。此材料不列23候选、不在23评分/Books；已经交root仅重开22 Qwen家族的FIRST及必要审阅。

剩余普通工作：23 root准入后Qwen具名家族必要审阅和实际owner/邻接Books比较、独立DAY；来源普通补检已执行。22 FSF已有作者ready材料，但新Omni/TTS恢复需22局部重开准入，不再宣称22全日普通待办0。每项作者日级工作ready及时交接；共享Books/月README/LEARNING_STATE未写，不stage/commit/push。

## FIRST-QWEN-23：新恢复入口五项核心及局部准入包

`QWEN_OMNI_CONFIG.raw`实际目录60对象；按本日窗口筛出5项，原对象另存 `qwen-window-config.json`。每项tokenLinks均实际200，原记录 `qwen-window-core-fetch.json`，原tokens `*.tokens.raw` 和派生 `*.core.txt`。只读取本窗5核心，不把60对象当全文队列。所有日期是官方原ISO，非由显示日期/提交时间推造。没有继承root11 Next的准入。

1. Qwen3Guard：date=`2025-09-22T20:00:00.000Z`，北京23日04:00，与原Blog meta一致。完整Key Features、workflow及原使用示例已读。完整响应后置/binary阈值约束→最后层双分类头逐token/state审查，Safe/Controversial/Unsafe中档可动态policy映射→重新考虑检测粒度、政策严格度与提交时序的分离。拟准入；安全变化需深入受影响内容。原报告历史缺口、RL有效性/性能未采用边界如前。
2. Qwen3-VL：date=`2025-09-22T22:00:00.000Z`，北京23日06:00。实际读Introduction/Key Highlights/Model Performance/Model Updates核心，未称读取每个demo附件。原MRoPE按t/h/w分块使时间集中高频、视觉只单层注入、T-RoPE承载视频时序→interleaved-MRoPE让三轴覆盖全频、DeepStack跨LLM层注入不同ViT层特征、交错文本timestamp/frame→改变多模态位置/融合/可表达时间的选择。拟准入，owner候选MULTIMODAL-REPRESENTATION；不是因长context宣传或benchmark冠军准入。100%/99.5% needle与32语言OCR有效性未按宣传采用，训练预算/对照及实现精确版仍须针对采用命题审阅。这里的timestamp语义不能外推真实world-state或行动可靠性。
3. Qwen-Image-Edit-2509：date=`2025-09-22T16:08:30.000Z`，北京23日00:08:30。实际读发布核心/变更理由及文字说明（未声称看完图片）。原单图编辑条件→在原架构上image-concatenation继续训练以支持多图reference，keypoint/depth/edge作为图条件→输入参考身份与结构控制进入同一编辑条件通道，改变多reference条件组织。拟局部准入，owner候选MULTIMODAL-REPRESENTATION/生成接口交接；脸/商品/文字一致性的未受控挑选示例不能证明普遍identity preservation或收益归因。新revision实际多图训练/条件支持而非版本号本身触发；必要训练/条件机制可再定点读model card，不遍历图例。
4. Qwen3-LiveTranslate：date=`2025-09-22T23:00:26.000Z`，北京23日07:00:26。实际读Key Features/Performance/Examples文字与输出语言表。跨语言词序要求等待未来context、噪声/歧义仅靠audio欠定→semantic unit prediction与视觉context辅助、轻MoE+dynamic sampling服务实时译流→需要核翻译commit粒度与多模态补证的质量/延迟边界。潜在增量清楚但算法机制披露浅，交root局部准入校准；不因未给实验细节排除，也不把semantic unit标签当已验证新调度。3s和实时保留94%准确率缺完整workload/model/hardware/protocol，不采用定量/普适鲁棒性；示例只支持作者展示事实，不证明无损。可接受原技术说明/当时service协议支撑必要机制；若关键机制始终未披露可收窄为仅报告或暂缓，不编造实现。
5. Travel Planner：date=`2025-09-22T21:00:59.000Z`，北京23日05:00:59。官方Introduction/Key Features/反思与查询核心实际读完。多Agent对接Amap/Fliggy/search、根据开门时间/到站时间修订计划，是已有规划/工具/反思的任务组合；70+工具调用不是新执行机制，也没有披露一致性、失败恢复或可靠性成立条件。拟贡献前关闭，不把app产品更新当系统方法突破，不据“every piece traceable”授保证。

请root FIRST-QWEN-23独核5项原字段和上述受影响准入/排除，代表性另核TimesFM旧v1 separator、OpenAI意向合作关闭以及安全/局部负侧保留。当前正式候选0、未评分、作者未自授FIRST。之后才围绕通过项展开最低必要审阅与精确Books差额，不能在此授日级ready。23无候选进行中V3和限定diff-check曾通过，新增包后还需再校验；机器不验语义。
