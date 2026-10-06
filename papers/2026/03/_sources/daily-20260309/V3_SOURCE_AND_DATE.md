# 03/09 V3 来源、准入线索与日期隔离

作者 mar02_v3；检查 2026-10-01T23:43:17+08:00。窗口固定 2026-03-08T09:00:00+08:00～2026-03-09T09:00:00+08:00。本记录是实际有限获取的停点，不是旧54/527库存的筛选账本。当前确定当窗候选0、必要证据审阅0、Books整合/已有覆盖0；不把题摘审阅称作Evidence完成。

## 1. 14来源实际停点

1. **SRC-OPENAI**：[Research](https://openai.com/research/)当前精选不是历史覆盖。web不能解析text/xml后，实际curl解析[官方RSS](https://openai.com/news/rss.xml)的03/07～10 pubDate；仅03/09 `OpenAI to acquire Promptfoo`（Company）`Mon, 09 Mar 2026 10:00:00 GMT`=BJT18，03/10两项分别11/10GMT，均窗外；没有返回03/07～08项。此RSS切片已检查，不外推全机构发布无遗漏。
2. **SRC-ANTHROPIC**：[Research](https://www.anthropic.com/research)首页10项09/30～08/28无历史证明。实际读HTML嵌入PublicResearch `publishedOn`：`mozilla-firefox-security=2026-03-06T10:30:00.000Z`、`exploit=2026-03-06T00:00:00.000Z`、`labor-market-impacts=2026-03-05T19:59:21.508Z`、`diff-tool=2026-03-13T10:15:00.000Z`。有限相邻段跨窗无当窗行；不是全机构保证。
3. **SRC-GOOGLE-AI**：DeepMind Research当前精选；实际由HTML分页href恢复[Blog page3](https://deepmind.google/blog/page/3/)，24条May→Feb2026。相邻链接原文[10 years AlphaGo](https://deepmind.google/blog/10-years-of-alphago/) `March 10, 2026`、[Flash-Lite](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) `Mar 03, 2026`均窗外。Google Research [March archive](https://research.google/blog/2026/03/)当前page1实际12条March31→March6WAXAL（相邻March11诊断）；page2 web失败，定点读[实际已保存page2元数据](../daily-20260305/V3_OFFICIAL_RECOVERY_12.md)：163230bytes、2/2、仅March6SpeciesNet/March4Bayesian，全部日期与09窗口对读，均窗外，不继承05正文/处置判断。Blog历史两页有限已检查；[Google Research pubs](https://research.google/pubs/)2026年372条、当前页1～15/11569不能证明本窗历史覆盖，仍受阻。官方域名03/08～09搜索仅辅助无结果，不能替代目录。
4. **SRC-META-AI**：[Research](https://ai.meta.com/research/)web0行/curl空body，官方域名日期搜索无结果。必要历史目录受阻，不记零命中。
5. **SRC-QWEN**：[原入口](https://qwenlm.github.io/)实际指向[qwen.ai/research](https://qwen.ai/research)，web0行/curl空body。root指出已恢复公共只读入口后，作者先定点读[恢复机制/原值记录](../daily-20260305/V3_OFFICIAL_RECOVERY_12.md)，再自己实际GET `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`。返回data仅articles、40条，没有total或分页键；40/40 title/path、extra.date及正文article:published_time metadata全读并独立与09窗口对照，不审窗外正文。相邻Qwen3.5 display=`2026-02-16T04:00:00+08:00`/published=`2026-02-14T04:00:00+08:00`→Qwen3.5-Max-Preview两字段=`2026-03-19T04:00:00+08:00`；Omni displayMarch30/publishedJan7、TTS displayJan22/embeddedMarch24 2025等矛盾都窗外，不猜改。40条无字段落窗，仅当前返回切片已检查，不再保留动态目录普通gap，不外推所有删除/隐藏历史。
6. **SRC-DEEPSEEK**：实际[Research/News](https://www.deepseek.com/en/news/)Research可见10条，最近`2026/02/25 DualPath`→`2026/06/24 V4`跨窗无行。News可见5条Sep10→Apr24→Dec2025，ViewAll未展开。有限Research段已检查，不授News全部历史/全机构无遗漏。
7. **SRC-MOONSHOT**：platform blog26可见条目止2025/11/07，不能代表2026；已恢复[实际Kimi Blog](https://www.kimi.com/en/blog/)19完整可见条目，最近`2026/02/09 Agent Swarm`→`2026/04/20 K2.6`跨窗无行。当前目录有限已检查，旧platform限制不冒充必要永久gap。
8. **SRC-TENCENT-HUNYUAN**：[Research](https://hunyuan.tencent.com/research)实际脚本发现只读 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，JSON `{"pageNum":1,"pageSize":20,"renderType":0}`。返回totalNum11、list11/11。原字段`displayPublishTime`/`publishedAt`均保留语义，不能互当首公开；跨窗相邻display `1770971794`（Feb13）→`1776873600`（Apr23）；Apr23行publishedAt=`1782308557`（Jun24）。无March字段。完整可见11行有限检查，不外推机构全部历史；不保存无关signed图片URL。
9. **SRC-ZAI**：[Research](https://www.zhipuai.cn/zh/research)实际15可见条目Aug26→Dec9，SeeMore未展开；相邻`2026/02/21 GLM5 Technical Report`→`2026/03/15 GLM5 Turbo`跨窗。有限可见段已检查，不全站保证。
10. **SRC-BYTEDANCE-SEED**：[Research](https://seed.bytedance.com/en/research)/[papers](https://seed.bytedance.com/en/public_papers)实际HTML脚本 `https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/deploy/flow/ai_official_website/88329/static/js/main.897993d4.js`发现GET `/api/get_article_list_v2`。只读`article_type=1,publish_year=2026,order_desc=false,count=20,page_token=0`及20，两页从Jan20穿过Mar26，总82/has_more=true；实际可见翻译/公开过滤后非每页20。相邻paper日期原毫秒`1772380800000`（UTC03/01T16=03/02BJT00，ids1644/1664）→`1773244800000`（UTC03/11T16=03/12BJT00，id1424），无本窗日期，越右端停止。Blog `article_type=2`同年升序offset0，总23/has_more=true、9可见，最近Feb14 (`1770998400000`)→Apr1 (`1774972800000`)。没有全扫82/242。浏览器创建失败BrowserNotAvailable、可用浏览器列表[]；脚本只读恢复成功，因此不能仍报普通browser待办。
11. **SRC-BAIDU-ERNIE**：[Blog](https://ernie.baidu.com/blog/zh/)page1/2十可见条目May9→Nov21 2025；最近Feb06ERNIE5.0→Apr15ERNIEImage跨窗。有限段已检查，未扫更老page2。
12. **SRC-XIAOMI-MIMO**：[官网](https://mimo.xiaomi.com/)Paper8条，最近Feb03HySparse→Mar13ARL-Tangram跨窗。Blog15可见无日期；实际脚本`https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js`恢复部分ENfrontmatter日期（12/18～19 2025、05/30、06/08、06/10、09/27 2026），多项V2.5/Pro/TTS/V2.6等仍无date。Paper有限已检查；Blog当窗发布日期映射受阻，不从系列名填日期，未扩大未来正文审阅。
13. **SRC-MINIMAX**：minimax.io/blog错误；中文入口实际redirect[www.minimax.cn/blog](https://www.minimax.cn/blog)，13可见条目Aug13→Jan15 2025；最近Feb12Forge/M2.5→Mar18M2.7跨窗无行。[Agent Tech Blog](https://agent.minimax.io/docs/techblog)当前索引及[llms.txt](https://agent.minimax.io/docs/llms.txt)只揭示techblog/agent-team；CN目录AgentTeam Apr27窗外。有限可见段已检查，不全机构无遗漏。
14. **SRC-ARXIV**：下面的主题线索和一次官方month-list已查；必要具体首公开批次受阻。不记Coverage通过/当窗零论文。

## 2. arXiv有界发现，不是库存队列

实际API入口[export query](https://export.arxiv.org/api/query)，发现使用`submittedDate:[202603051900 TO202603082359]`（UTC）+sortBy=submittedDate、sortOrder=ascending、start=0。这是针对普通Sunday公告机会的提交检索，不将Submitted当首公开。迟延条目含后续月份ID，不能因此全收入03/09。

| 主题与分类 | 实际读取边界 | 未读/不宣称 |
| --- | --- | --- |
| cs.DC/CL/LG/AI，LLM serving、memory、agent、training、Transformer等主线 | 初次宽查询76前12，收窄后391前40标题，相关完整题摘如下 | 391不是逐项题摘/全文队列 |
| cs.CV/RO，标题multimodal/world model/VLA/diffusion/vision-language | 87前20标题，05623～06054 | 未全读87 |
| cs.AR/PL/OS/PF，LLM/Transformer/language model/GPU | 13/13标题：05646/06710/05692/06728/06731/24595/05904/05931/2604.03245/07006/08755/18030/07850 | 标题浏览不等于13篇完整题摘 |
| cs.IR/MA，LLM/language model/Agent及retrieval/memory/coordination/agent标题 | 15/15标题：05621/05789/23516/2604.22756/06007/06025/06065/06217/2604.09596/06394/06397/06856/07233/07379/15658 | 通用推荐/博弈不自动纳入 |
| cs.CL/LG/AI，Transformer/MoE/model merging/distillation/policy optimization/language model标题 | 107前20标题，相关05727/05768/05772/05773/05805/05806/05828/05878等 | 未全读107，无后续全量队列 |

补检实际[cs.DC March月表](https://arxiv.org/list/cs.DC/2026-03?show=2000)，Total346；标题页与目标邻接含05800[54]、06350[59]。页面只有March标题/编号，没有`Mon, 9`日标题；membership不能证明某日batch。一次skip=50/show=50恢复cachemiss/429停止，不扩大日期探针。旧`inventory.json`及旧scheduled_match仅查漏/raw，54/527及DataCite+日程归属均不继承。

## 3. 日期证明为什么没有过Gate

实际[arXiv availability](https://info.arxiv.org/help/availability.html)：Sun～Thu20Eastern公告；QA可延迟1～4天，ID首次公告分配不预分配。[NIST](https://www.nist.gov/pml/time-and-frequency-division/local-time-faqs)：DST第二个MarchSunday02提前1h、EDT UTC−4。03/08是该Sunday，所以最早普通Sunday公告03/09BJT08，在本窗最后1h；这只是机会，不是具体batch证明。

实际DataCite `Updated`原值虽在08～09，却按[官方dateType定义](https://datacite-metadata-schema.readthedocs.io/en/4.6/appendices/appendix-1/dateType/)表示resource最后更新，非Available；Available仅`2026-03`。created/registered均在本窗09右端后，不足以形成完全落窗的公开正文范围。`citation_online_date`05800实际等Submitted03/06，也不是公告时间。[arxiv-canonical](https://github.com/arXiv/arxiv-canonical) README明确As of2023-03-17 nothing in repo in use at arxiv.org，不能把其规划S3路径当真实生产公告接口。

| v1 | Submitted UTC | DataCite v1 Updated UTC | created/registered UTC |
| --- | --- | --- | --- |
| 05553 | 03/05T04:58:38 | 03/09T00:01:20 | 03/09T01:38:40/01:38:40 |
| 05578 | 03/05T17:44:29 | 03/09T00:02:08 | 03/09T01:39:16/01:39:17 |
| 05786 | 03/06T00:34:14 | 03/09T00:14:34 | 03/09T01:44:10/01:44:11 |
| 05800 | 03/06T01:22:16 | 03/09T00:15:37 | 03/09T01:44:30/01:44:31 |
| 06003 | 03/06T08:02:58 | 03/09T00:30:16 | 03/09T01:49:19/01:49:20 |
| 06350 | 03/06T14:58:16 | 03/09T00:49:56 | 03/09T01:57:27/01:57:28 |
| 05697 | 03/05T21:43:02 | 03/09T00:09:32 | 03/09T01:42:06/01:42:06 |
| 06001 | 03/06T08:01:36 | 03/09T00:30:12 | 03/09T01:49:16/01:49:17 |
| 05931 | 03/06T06:03:38 | 03/09T00:26:10 | 03/09T01:47:37/01:47:37 |

所有日期年为2026。05553/05578在Thu14EST之前，最早普通公告可能Mar06BJT09，不能把两者直接称本窗。其他具体条目同样未恢复真实Sunday批次/<=09公开正文上界。停止有限恢复，不继续靠更多metadata拼伪exactslot。

## 4. 完整题摘的潜在贡献（仅日期保留，未评分/深审/Books）

以下15个精确v1已实际读完整题摘和当前v1history；身份链接只负责可恢复，不能证明本窗。root实际读首6题摘/hist并通过具体机制校准；后9待独立抽核日期隔离/准入。它们**不进正式候选表**。

| v1链接/材料 | 具体潜在增量与不能采用的外推 |
| --- | --- |
| [05800 StreamWise](https://arxiv.org/abs/2603.05800v1) | 异构LLM/TTS/video DAG按质量、parallelism、earlier scene与资源/SLO联合权衡；非45美元/实时宣传准入 |
| [06350 MoEless](https://arxiv.org/abs/2603.06350v1) | layer-aware expert load predictor触发proactive function scaling/placement并平衡locality/load；不采普遍43/84收益 |
| [06003 EvoESAP](https://arxiv.org/abs/2603.06003v1) | 固定global expert budget与layer内排序，以teacher-forced ESAP proxy做进化式跨层非均匀分配；不把proxy当部署质量 |
| [05553 EigenData](https://arxiv.org/abs/2603.05553v1) | BFCLv3 schema/implementation/reference bug及DB outcome而非turn-match，可能修正评价排名与人类有效性判断；早提交下界未清 |
| [05578 Tool-Genesis](https://arxiv.org/abs/2603.05578v1) | 可归因interface/function/downstream与早错放大诊断可能改变接口验证；若只是分桶常识不能强准入，早提交下界未清 |
| [05786 Proof-of-Guardrail](https://arxiv.org/abs/2603.05786v1) | TEE attestation证明实际执行公开guardrail而非相信私有agent厂商；执行真实性≠guardrail有效性/防jailbreak。当前v2为Jun26窗外，不冒称v1安全已证 |
| [05697 MultiHaystack](https://arxiv.org/abs/2603.05697v1) | givenevidence/full异构pool对照揭示端到端retrieval bottleneck；不是单凭46k/747规模 |
| [06001 IGAR](https://arxiv.org/abs/2603.06001v1) | 固定视觉下矛盾OOD语言检查VLA依赖视觉先验而忽视指令，并train-free attention recalibration；LIBERO/Franka局部不是全安全；当前Jul2v2窗外 |
| [05931 Persistent-State Dataflow GDN Accelerator](https://arxiv.org/abs/2603.05931v1) | 2MB persistent BRAM/five-phase dataflow/一次读写state矩阵/grouped value heads；四U55C设计点不证明所有subquadratic算子<1FLOP/B或对H100普遍4.5x |
| [05727 Structured Multidimensional Representation](https://arxiv.org/abs/2603.05727v1) | L-product三阶tensor频谱slice attention/FFN，固定宽度p-parallel参数约1/p和DCT归纳偏置；小型IMDB/AGNews不自动排除，也不授普遍等价 |
| [05805 Sparse Crosscoders](https://arxiv.org/abs/2603.05805v1) | shared-feature BatchTopK crosscoder联合activations比较MoE/dense表示，matched active params的5层/1Btokens条件；total capacity confound不能忽略 |
| [05806 MoELens](https://arxiv.org/abs/2603.05806v1) | DeepSeekMoE64/active6 routing集中/top-expert表示及三域perplexity可修正局部稀疏判断；不采普遍单expert等价。Comments ICLR2025 SLLM workshop提示较早家族身份，尚无primary先公开证明，不伪称已审duplicate |
| [05772 DepthCharge](https://arxiv.org/abs/2603.05772v1) | head AblationImpactRanking+boundary perturbation的安全绕过机制信号；不照抄ASR14或无条件安全；Mar13v2窗外 |
| [05773 Knowing Without Acting](https://arxiv.org/abs/2603.05773v1) | harmfulness recognition/refusal双轴、double difference/causal steering双重分离反证；不采universal保证；Mar13v2窗外 |
| [06397 R4T](https://arxiv.org/abs/2603.06397v1) | set-level不可分解reward训练fan-out LLM再编译teacher pairs到diffusion embedding，目标一致性可改变retrieval选择；fashion/music局部非纯领域指标、也非普遍10x |

另3个实际完整题摘但准入事实仍含糊，只保存线索不默认retain： [05692 dense deployment](https://arxiv.org/abs/2603.05692v1) Llama3.1 70/405B intranodeTP/PP，摘要尚不能区分既有latency/throughput权衡与新matched资源边界；[05831 mobile reasoning](https://arxiv.org/abs/2603.05831v1) knowledge-pack/exposure非单调与3B UAV intermittent-link局部SWAP-C条件，不能泛称可靠；[06007 MASFactory](https://arxiv.org/abs/2603.06007v1) intent→editable workflow→DAG+reuse/context/trace七bench可能既有组合，不能仅框架/数字准入。因三者本窗身份同样无法确认，未展开core队列；恢复日期后只窄读决定准入的内容。

## 5. 具名分层负侧与独立范围

- **贡献关闭，完整题摘**：[05839 Evaluating LLM Alignment with Human Trust Models](https://arxiv.org/abs/2603.05839v1)，单GPT-J activation cosine对既有人类trust taxonomy/60 emotion concepts，未提供新的有效性条件或评价设计；不因模型旧/实验小关闭。root实际完整题摘负侧校准通过。
- **安全提案负侧，完整题摘**：[06025 Sensitivity-Aware Retrieval-Augmented Intent Clarification](https://arxiv.org/abs/2603.06025v1)，是attack model/retrieval defense/eval utility三项研究agenda，非已实现的新防御或有效性证据；摘要不支持既有安全保证改变。未读核心/未宣称安全反证全部复核，root必要时仅窄核这个安全家族。
- **项目范围关闭，exact-v1 API完整题摘**：[05789 The Coordination Gap: Alternation Metrics for Temporal Dynamics in Multi-Agent Battle of the Exes](https://arxiv.org/abs/2603.05789v1)。Markov game Q-learning/random null的PA/ALT公平性诊断有局部价值，但不属于本项目模型驱动LLM协作机制；不因新metrics存在而通过系统类比引入Ch82。当前v5标题不同，未用当前题名替换v1。
- **标题明确范围外（未冒称完整摘要）**：[05917 Stock market Node Transformer/BERT sentiment](https://arxiv.org/abs/2603.05917v1)、[05646 functional programming course assessment](https://arxiv.org/abs/2603.05646v1)：分别领域预测/教育中的LLM应用，未见直接新模型或系统机制线索。
- **暂缓范围标题样本**：[05900 molecular policy optimization](https://arxiv.org/abs/2603.05900v1)为AI for Science线索，仅记录范围，未借RL/evaluation owner引回本日。

明确负项无需另追不影响处置的日期。05772/05773/05786/06001安全或反证潜在贡献保留而非负侧；不能为了零候选忽略信号。没有声明全部13/15/20标题或旧527条已完整题摘/独立复核。

## 6. 精确一次材料请求与停止条件

**D1：上述15潜在贡献+3含糊线索的v1本窗身份**。需要实际带时间的03/08EDT20公告列表及具体ID membership，或原始作者/项目/正文公开记录支持完全在本窗的首公开范围；05553/05578等更早提交须额外排除更早公开，05806须解ICLR2025家族首公开。DataCite Updated/created、月表membership、提交时间和日程不接受单独替代。当前原始批次不可恢复，有限month-list失败后停止；不支持候选、证据、Books或无遗漏。恢复时只重开具体身份→决定准入必要core→证据/owner，不补全391/527库存。

**H1：历史目录切片**。准确剩余：Meta `https://ai.meta.com/research/` 本窗研究目录（空响应）；Google Research `https://research.google/pubs/` 本窗日级论文目录（当前year/count不含日期切片）；MiMo `https://mimo.xiaomi.com/` Blog15卡无date的本窗映射；DeepSeek `https://www.deepseek.com/en/news/` News首5之外ViewAll隐藏段（当前可见相邻2025/12/01→2026/04/24，未证明隐藏本窗无项）。需这些入口对应本窗原始归档/日期目录或可访问公开API/browser同段记录，精选/搜索无结果不接受替代。ZAI SeeMore只限定实际可见段，不把没有具体相关新信号的未知loadmore建永久请求。Qwen公共40/40 metadata与GoogleResearch Blog2/2已恢复，不再保留其动态/Blog历史gap。当前可用浏览器[]、剩余原始动态空响应/缺历史，受影响来源隔离，不授正面完整覆盖。

当前没有Books差额提案或写锁。2026-10-02T00:01:03+08:00正式同步root非作者最终日Gate通过，普通待办0。root实际全读正式六部分/本记录/18隔离条件；完整题摘核首6及05697/06001/05931/05772/05773/06397共12潜在、05839/06025两负项。其余05727/05805/05806与3含糊只核隔离身份/重开条件，05789访问失败不声称读到，范围负侧不称全量。缺日期而非实验可信度使上述项不进入必要正文/Books队列。root于本次有限恢复后指示终态隔离，不继续广泛补检/全文。无Weekly、LS、索引或stage/commit/push修改；下一独立分配03/12不继承本日分母。
