# 2026-03-18 V3 有限发现、筛选与停止

作者mar01_v3；检查2026-10-02，窗口2026-03-17T09:00:00+08:00→2026-03-18T09:00:00+08:00。当前规则独立重读，不继承旧660库存、13候选、9分、EffectiveDate、旧Evidence/NoChange或Weekly。旧稿单独保存，旧原文保留未删除。本文件是实际有限入口与筛选记录，不是宽目录逐项审计。

## arXiv主题查询

API入口https://export.arxiv.org/api/query；四查询均start=0、max_results=200、sortBy=submittedDate、sortOrder=ascending。实际返回与total分别125/125、70/70、17/17、118/118；同篇交叉重合，不加为当天论文数、不使整份列表成为题摘/全文队列。原始身份字段见[V3_ARXIV_THEME_METADATA.json](./V3_ARXIV_THEME_METADATA.json)。

- systems：`submittedDate:[202603161800 TO 202603171800] AND (cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"large language model" OR all:"distributed training" OR all:"speculative decoding" OR all:"kernel" OR all:"inference")`。
- learning：同Submitted范围，`(cat:cs.CL OR cat:cs.LG) AND (all:"Transformer" OR all:"mixture of experts" OR all:"language model") AND (all:"optimization" OR all:"scaling" OR all:"representation" OR all:"attention")`。
- multimodal：同Submitted范围，`(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"world model" OR all:"vision language action" OR all:"video generation" OR all:"multimodal foundation")`。
- agent_eval：同Submitted范围，`(cat:cs.AI OR cat:cs.MA OR cat:cs.IR OR cat:cs.CL) AND (all:"language model" OR all:"LLM") AND (all:"agent" OR all:"retrieval" OR all:"evaluation")`。

以上是围绕预期下一公开slot的Submitted buffer，不是首次公开窗口，也不能覆盖此前Submitted而延迟moderation的全部事件。API现有版本/后续updated不触发revision深审。实际有界补检请求 `/list/cs.CL/2603?skip=0&show=25` 返回404；有效 `/list/cs.CL/2026-03?skip=0&show=25` 返回2138中1–25，只有月首标题、没有本窗精确公告时刻；不把这页当本日公开批次，不继续抓整月。一次两条定点公告/title搜索只得HF/索引的Submitted显示和作者项目线索，不作为date proof；随后作者项目与作者Blog都显示February28且有paper链接，只用于15854首公开日期冲突隔离。没有代码commit考古。

## 有限准入与日期判断

[完整v1题摘/历史原始记录](./V3_PRIMARY_ABSTRACTS.md)中首8信号加Persona和3多模态，共12 arXiv家族，不来自旧候选池。root实际完整首6 15854/15953/16152/16590/15803/16817题摘和history的潜在贡献校准通过；不是日期或实验通过。VQKV/fleet/Persona仅定点core，三多模态完整AB；尚无必要实验深审。

| 家族v1 | 具体待核验增量与选择变化 | 停止范围 |
| --- | --- | --- |
| [15854 FlashSampling](https://arxiv.org/abs/2603.15854v1) | sampling作为LM-head tiled epilogue而非HBM logits后处理；精确分解改变采样数据路径 | fullAB/history；作者项目头February28与arXiv复合范围冲突；不采用v2/v3收益 |
| [15953 HAT](https://arxiv.org/abs/2603.15953v1) | byte→word接口保留AR backbone，使tokenizer替换的兼容/转换选择可重考 | fullAB/history；不授所有词界/语言兼容 |
| [16152 HIPO](https://arxiv.org/abs/2603.16152v1) | CMDP/primal-dual将system遵循作为约束而非等权reward；训练utility/compliance选择 | fullAB/history；strict safety只作者主张，若日期恢复须深审实际保证 |
| [16590 BATQuant](https://arxiv.org/abs/2603.16590v1) | MXFP block里rotation能迁移outlier能量；block-aligned affine使格式粒度与变换耦合 | fullAB/history；不授native低比特生产吞吐 |
| [15803 Mask](https://arxiv.org/abs/2603.15803v1) | density hub/complementary priority mask改变同样训练样本的噪声资源分配 | fullAB/history；未核同预算机制收益，ongoing work不当撤回 |
| [16817 Conformal RAG](https://arxiv.org/abs/2603.16817v1) | 高factuality可因vacuous output而无用，shift/distractor与scorer成本影响校准选择 | fullAB/history；不授实流量概率保证 |
| [16054 fleet-sim](https://arxiv.org/abs/2603.16054v1) | joint routing/queue/length budget模拟可推翻低utilization即可达P99的sizing判断 | §3.1–3.4定点；request-level两事件DES、hand-calibrated GPU常数，不是token-level硬件验证 |
| [16435 VQKV](https://arxiv.org/abs/2603.16435v1) | residual-SimVQ代码本重构对齐FlashAttention，codec执行预算不同于只压缩存量KV | §3.1–3.3定点；10Mtoken codebook训练，“training-free”仅不改backbone，不借ratio准入 |
| [15831 Persona Risk](https://arxiv.org/abs/2603.15831v1) | sequential反馈与自报risk不随round更新的局部反证，不能把prompt persona当自适应agent | §3及§4.8；persona/资金/目标同时变，selfreport相关性不证明Bayesian机制，日期隔离非心理学拒绝 |
| [16666 Fast-WAM](https://arxiv.org/abs/2603.16666v1) | 分离video co-training和test-time imagination，对在线未来生成必要性的控制反证 | fullAB/history；未核4x/190ms配置，不授全部WM无须rollout |
| [16860 DreamPlan](https://arxiv.org/abs/2603.16860v1) | suboptimal探索数据训练action-conditioned videoWM再ORPO；数据/rollout有效条件可能改变planner训练选择 | fullAB/history；只潜在条件，不把既有组合或跨physics泛化直接准入 |
| [16871 WorldCam](https://arxiv.org/abs/2603.16871v1) | 连续action→6DoF/global pose既作控制条件又作历史观测index，改变长程回访缓存检索 | fullAB/history；不把gaming镜头状态当真实完整world state |

日期实际字段见[first8](./V3_DATACITE_FIRST_BATCH_FIELDS.json)及[tail4](./V3_DATACITE_TAIL_FIELDS.json)。均arxiv.content、findable；官方[availability](https://info.arxiv.org/help/availability.html)/[DOI](https://info.arxiv.org/help/doi.html)与[registered定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)/[states](https://support.datacite.org/docs/doi-states)只给：ID/DOI不预发，Submitted/deadline最早slot为03/18 08:00BJT，registered+1秒是公告的保守上界。12项上界均03/18 10:17–10:42BJT，全部跨09终点；Updated、created、Available月级字段不是提前公开证明。因此确定候选0、不评分、不将AB算Evidence、不写Books。15854另有作者February28头，不假设该头证明原paper当日公开，重开需解决首公开归属。

## 代表性负侧（7项，不是全库存）

| 原材料 | 真实关闭依据与日期边界 |
| --- | --- |
| [15797 OMNIFLOW v1](https://arxiv.org/abs/2603.15797v1) | fullAB的冻结LLM+flow topology/physics验证服务NavierStokes/天气科学应用，ROADMAP暂缓；不借通用Agent/Eval owner重新引入。root实际AB通过。 |
| [15909 Scale Development v1](https://arxiv.org/abs/2603.15909v1) | fullAB各prompt/temp/模型影响BigFive item语义冗余和心理测量结构效度，未建立基础模型/Agent机制的有效条件；不是仅按心理学标签排除。root实际AB通过。 |
| [16131 SciZoom v1](https://arxiv.org/abs/2603.16131v1) | fullAB 44,946篇三粒度数据与前后LLM时代写作style分析，没有受控机制/可靠性偏差修正；不以科学写作误归AIforScience。root实际AB通过。 |
| [16068 Resource Consumption Threats v1](https://arxiv.org/abs/2603.16068v1) | 原HTML完整题摘为survey unified scope/诱发→理解→缓解分类，未披露新的机制、失效对照或修正具体设计判断的证据；只关本v1贡献，不断言该主题无价值。不采用API的v3来关闭v1。root已实际读本日保存的官方原HTML完整AB（PRIMARY_ABSTRACTS末478–492），再次web Cachemiss不抹去已读证据；准入层关闭通过。 |
| [GPT5.4 mini/nano产品主文](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 原core31–110比较bench/离线production latency估算及既有大模型协调/小模型subagent模式，未公开具体新训练机制或评价有效条件；不同effort不授纯因果资源收益。RSS03/17 10:00GMT精确在窗。安全附录另留潜在信号，不一并关闭。root实际core通过。 |
| [Japan Teen Safety Blueprint主文](https://openai.com/index/japan-teen-safety-blueprint/) | 原core31–62未来age estimation/controls承诺、existing break/selfharm safeguards及原则，没有新可执行contract或评估失效边界；不把隐私/安全承诺当保证。作者和root各一次PDF链接InternalError不影响主文具体关闭，无必要PDF请求。RSS03/17 10:00GMT在窗。root实际core通过。 |
| [MiniMax M2.7主文](https://www.minimax.io/blog/minimax-m27) | 原core67–115的failure→modify→eval→keep/revert与memory/skills组合和新model任务数字，无独立机制/成立条件增量；100轮内部30%不单独证明self-evolution，MLE三次24h只支持组合协议；不以缺ablation单独否准入。头Mar18日级未核时区，确定前关闭无需追精确日期。root实际67–96通过，其余作者读，不称root全主文。 |

Google Cognitive Taxonomy不列关闭：其sameinstruction/fewshot/format/tools、人类代表baseline、percentile profile协议确有潜在增量，root17实际paperAB/§3校准可定点复用；本日仅日期与event去重隔离，不继承17日报判决。OpenAI mini附录§6.3.1直接uplift vs proxy阈值调整亦不是科学应用排除。两项与12 arXiv构成14个有限潜在日期/版本请求，不是14候选或14完成审阅。

## 本日来源恢复补充

本日RSS总1242，UTC03/16–19有限6条，2条精确在窗；Qwen40条从Feb16到Mar19跨本窗；Seed type1 page_token20返回18、total82、next40/has_moretrue，显示Mar16→Mar20跨本窗，type2 token0返回14/total19/has_morefalse/next空，Feb16→Apr1跨本窗但未返回5不可外推；保留[实际公开字段](./V3_PUBLIC_DIRECTORY_FIELDS.json)。混元网页timeout后生产zh endpoint实际11/11可见，2/13→4/23跨窗，[原字段](./V3_HUNYUAN_FIELDS.json)区分displayPublishTime与当前publishedAt。所有目录只有可见有限范围，不证明全机构历史或删除项。

Anthropic本日Research可见最新10项+SeeMore仍同页不足历史，后来按root反馈定点复用已实际恢复的March字段，详见下段，不再保留该Research目录请求。GoogleResearch年级Pubs2026=372、year-only非日历史，MarchBlog page1十二标题覆盖Mar6→31，其中Mar17医疗应用按明确范围外停，page2两条原字段已定点复用；DeepMind Blog page3二十四month-only卡跨Feb→May，Cognitive BlogMar17日级。Meta Research空正文、Blog page1十/page2十二跨Mar11→27，实际publication结果页access error；MiMo Paper8 Mar13→Jun29、Blog15无日期，公开HTML仅div标题且动态click无href，浏览器iab unavailable一次停止；MiniMax英文12、中文重定向当前shell+原HTML有Mar18的M2.7原卡，AgentTechHTML仅15行且一次.md recovery InternalError。不拿这些受限恢复当全站无命中，不继续扩全年/脚本/附件。

### 同身份原目录字段定点复用（本18窗独立对读）

只复用[17实际来源原字段记录](../daily-20260317/V3_WORKING_STOPPOINT.md)及[05实际Googlepage2响应记录](../daily-20260305/V3_OFFICIAL_RECOVERY_12.md)的身份、入口与元数据，不复用他日报告的候选或裁决。对本18窗口重新比较如下：

- Anthropic：原入口 `https://www.anthropic.com/research` 实际curl HTML Sanity March9条 `publishedOn`/title配对，保留原记录标题简记与UTC精度：Mar31T22:17Z Australia；Mar24T10:41Z Learning curves；Mar23T23Z Science Blog / Long-running / Vibe physics三条；Mar13T10:15Z diff；Mar6T10:30Z Mozilla；Mar6T00Z CVE；Mar5T19:59:21.508Z labor，年份均2026。近邻Mar13T10:15Z（BJT13日18:15）→Mar23T23Z（BJT24日07:00）跨本窗，9条无03/17–18记录。停止在实际Research March9条，不外推全News历史或删除项；保留本日latest10/SeeMore不能恢复历史的过程，但必要有限Research目录现已可核，不再终态隔离。
- DeepSeek：原入口 `https://www.deepseek.com/en/news/` 实际curl109872B的Next props完整posts16原日期为2026Sep10/Apr24；2025Dec1/Sept29/Sept22/Aug21/May28/Mar25/Jan20/Jan15；2024Dec26/Dec10/Nov20/Sept5/Aug2/Jul25。实际9467B官方脚本 `https://www.deepseek.com/_next/static/chunks/app/%5Blocale%5D/news/page-bd765c90dd4eb584.js` 显示News `N=u?w:w.slice(0,4)`、Research `d=s?g:g.slice(0,10)`；完整Research数组原邻接Jun24→Feb25→Jan28→Jan12→2025Dec31/Dec2，前四日期为2026。Feb25→Jun24跨本18窗，完整posts16无本18窗行；原值不依赖本日rendered Research10/News5。仅验收实际公开数组，不声称全机构历史。hidden News已恢复，不沿用旧目录缺口。
- Google：`https://research.google/blog/2026/03/?page=2` 已实际public urllib GET163230B，pagination2/2，仅两张原card：March6 SpeciesNet、March4 Teaching LLMs to reason like Bayesians。两原日期均在本18窗左界前，page1十二+page2两条是有限March archive2/2，不把page1当全部March，也不把它替代Pubs历史slice。这里只复用metadata，不继承05的Bayesian贡献或首公开判断，不重新展开旧论文。

root后又实际补16666/16871/16860/16435/16054完整v1AB/history及16068v1官方原HTML完整AB，总16具名AB（12潜在+4负侧）准入层校准，不授全文实验、日期或Evidence。root已实际完整读本日六部分、14源停点、12日期JSON原值、14隔离/7关闭，并实际核三修正source cells与§6，最终非作者日级Gate通过。正式日报状态完成，完成态V3 validator及限定diffcheck执行结果见§6；普通可执行项0。本窗14日期/版本线索及另5组来源外部终态保留项、具体重开位置统一见正式§5。没有Books写入、实现复现或生产验证，没有stage/commit/push。
