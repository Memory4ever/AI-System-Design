# Daily Research — 2026-03-18

**规范：** V3
**窗口：** 2026-03-17T09:00:00+08:00 ～ 2026-03-18T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T02:45:13+08:00

## 1. 结论

本窗已安全终态闭合：确定候选0、证据审阅完成0、Books整合0/已有覆盖0；这不是“当日无研究”。有限主题发现中12个arXiv潜在家族的公告范围均跨过09:00右端，另Google认知评估协议和OpenAI mini安全附录的事件日期/原始版本尚未充分限定，共14个具名潜在线索隔离，不评分、不把题摘或准入校准算Evidence完成。root非作者日级Gate已通过，普通待办0；隔离不支持正面结论或无遗漏断言。

四个Submitted buffer主题实际返回125、70、17、118条元数据，跨主题重合未相加、不逐项扩成题摘或全文队列。首6潜在贡献和代表性负侧已独立校准；7项明确贡献前关闭有具体理由。OpenAI产品发布中的model/latency数字、Japan原则承诺、MiniMax自演化组合不自动成为长期机制；mini附录的实测uplift与proxy阈值调整、Google的受控人类基线/percentile协议则不能误以“安全科学应用”或“未来hackathon”排除。书稿没有本日采用或写入，不宣称无遗漏、实验复现或生产安全保证。旧V2.1稿与有效原文保留为[旧快照](../_sources/daily-20260318/V3_LEGACY_REPORT_SNAPSHOT.md)，旧660/13/9分、EffectiveDate及旧完成状态均不继承。

## 2. 来源覆盖

实际查询与停止见[有限发现记录](../_sources/daily-20260318/V3_FINITE_DISCOVERY_STOP.md)，[公开字段](../_sources/daily-20260318/V3_PUBLIC_DIRECTORY_FIELDS.json)和[混元原字段](../_sources/daily-20260318/V3_HUNYUAN_FIELDS.json)。以下只验收约定有限范围，不外推全机构历史、删除项或全学科召回。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)精选非历史；[官方RSS](https://openai.com/news/rss.xml)1242中仅UTC03/16–19的6条。03/17 10:00GMT两事件精确在窗：mini/nano产品主文31–110、JapanBlueprint31–62已核；mini安全Hub§6.3.1与addedMar17原HTML定点核 | 受阻 | 当前附录段与launch原始精确版本的对应；§5一次请求，不将主卡Mar5日期或全部当前正文反填 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)当前最新10/SeeMore同页不足历史；定点复用[17实际curl的Sanity字段](../_sources/daily-20260317/V3_WORKING_STOPPOINT.md)：March9条publishedOn/title，Mar13T10:15Z→Mar23T23Z跨本18窗，无03/17–18记录；原值见本日有限记录 | 已检查 | 仅实际Research March9条，不外推全News历史或删除项；不再把可恢复目录作为外部终态 |
| SRC-GOOGLE-AI | [DeepMindResearch](https://deepmind.google/research/)8突破/精选；[Blog page3](https://deepmind.google/blog/page/3/)24个Feb→May month-only卡；[Research March page1](https://research.google/blog/2026/03/)12标题Mar6→31，本窗相交医疗应用明确范围外；独立复用[实际page2/2两条原字段](../_sources/daily-20260305/V3_OFFICIAL_RECOVERY_12.md)，Mar6 SpeciesNet/Mar4 Bayesian均早于本18窗。认知框架Blog core255–283与原paper协议身份定点；[Pubs](https://research.google/pubs/)year filter2026=372、当前1–15/11569是年级非日历史，不扩池 | 受阻 | 认知协议事件精确日期与Pubs本窗原始发布slice；有限March2/2不替代全部Pubs，§5 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)空正文；[Blog](https://ai.meta.com/blog/)page1十项+[page2](https://ai.meta.com/blog/?page=2)十二项跨Mar11→27，可见无03/17–18。实际[Publications结果页](https://ai.meta.com/research/publications/results/?content_types%5B0%5D=publication)access error | 受阻 | Publication历史主题slice，不以有限Blog替代；§5 |
| SRC-QWEN | [旧页](https://qwenlm.github.io/)迁移、[新Blog](https://qwen.ai/blog)空；实际[公开retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40日期/path字段，邻接Feb16→Mar19跨窗、可见无本窗事件 | 已检查 | 仅当前40可见目录，不证明被删除/未返回历史 |
| SRC-DEEPSEEK | [官方/en/news](https://www.deepseek.com/en/news/)当前rendered仅Research10/News5；独立复用[17实际curl/Next props及官方脚本原值](../_sources/daily-20260317/V3_WORKING_STOPPOINT.md)，完整posts16（2026Sep10/Apr24→2025→2024Jul25）、完整Research数组Jun24→Feb25→Jan28→Jan12→2025Dec31/Dec2，跨本18窗无可见本窗行；hidden News已恢复 | 已检查 | 只实际公开数组有限范围，不外推全机构历史/删除项；不把rendered5当全News |
| SRC-MOONSHOT | [官方Kimi研究目录](https://www.kimi.com/en/blog/)19条Jun2024→Jul2026；Feb9 AgentSwarm→Apr20 K2.6跨窗，停止 | 已检查 | 不拿旧platform博客止于2025证明2026缺失 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)timeout；实际[生产publicList](https://api.hunyuan.tencent.com/api/blog/publicList)POST pageNum1/pageSize20/renderType0、zh，code0、totalNum11、11/11；display2/13→4/23跨窗，publishedAt另保原值 | 已检查 | 当前公开目录边界，不外推全机构历史；不再记动态目录不可恢复 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)可见15卡，Mar15 GLM5Turbo→Apr1跨本窗，无本窗可见条目 | 已检查 | 当前可见目录，不自动扩大GitHub活动 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)5Blog/10精选；[Pubs](https://seed.bytedance.com/en/public_papers)page1 20/242非历史。实际article_type1/year2026/token20/count100/ascending返回18/82,next40，displayMar16→20跨窗；type2/token0同参数返回14/19,next空/has_morefalse，Feb16→Apr1跨窗 | 受阻 | Blog返回14与total19不一致的5项身份/日期缺失；不授19/19或原始first-public；§5 |
| SRC-BAIDU-ERNIE | [ERNIE Blog](https://ernie.baidu.com/blog/zh/)当前10项，Feb6→Apr15跨窗、可见无03/17–18主题事件 | 已检查 | 有限可见目录，不外推全部研究 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper8有日期Mar13→Jun29；Blog15无日期，V2Pro/Omni/TTS为动态div无href。一次公开HTML限定标题/字段恢复无日期；实际iab browser unavailable停止 | 受阻 | 本窗Blog历史主题slice及原始链接/日期；不遍历脚本或全15正文，§5 |
| SRC-MINIMAX | [英文Research](https://www.minimax.io/blog)12条，M2.7 Mar18 core67–115具体关闭；[中文](https://www.minimaxi.com/blog)重定向.cn shell，原HTML恢复M2.7卡/Mar18等日期字段；[AgentTech](https://agent.minimax.io/docs/techblog)15行、一次.md InternalError | 受阻 | AgentTech本窗历史slice与中文未恢复条目日期；Forge英文2/14/中文2/12均窗外，不混同，§5 |
| SRC-ARXIV | [API](https://export.arxiv.org/api/query)四主题Submitted03/16 18Z→03/17 18Z，start0/max200/ascending，125/70/17/118分别到total。实际完整题摘12潜在+4负侧；有效monthly第一页1–25/2138仅月首标题，不能证明本日公告。12项DataCite原字段、官方schedule/no-advance-ID/DOI定点核；一次作者原发恢复 | 受阻 | 12项复合日期跨09端点；Submitted buffer未覆盖早提交延迟公告。本窗相关官方公开batch/精确原发缺口，§5 |

## 3. 候选与判断

无确定当窗候选。14项潜在线索是日期/版本隔离，不进入候选表、不评分，完整题摘与准入校准不等于证据完成。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

没有本窗正面采用命题或Books写回，不以旧NoChange结论替代当前判断。候选分母0，Evidence完成0，整合/已有覆盖/仅报告/结构候选均0；外部潜在线索不是“仅报告完成”或“已有覆盖”。已读题摘、弱侧定点core及原始日期证据保留在[原始题摘](../_sources/daily-20260318/V3_PRIMARY_ABSTRACTS.md)、[有限判断](../_sources/daily-20260318/V3_FINITE_DISCOVERY_STOP.md)、[first8日期](../_sources/daily-20260318/V3_DATACITE_FIRST_BATCH_FIELDS.json)、[tail4日期](../_sources/daily-20260318/V3_DATACITE_TAIL_FIELDS.json)。

实际7项贡献前关闭分别是OMNIFLOW科学应用、BigFive心理量表指标、SciZoom数据/写作style、ResourceThreats v1 survey，以及OpenAI产品主文、Japan承诺/既有措施、MiniMax产品/已有优化循环；不是全库存排除审计。Persona局部反证、fleet模拟sizing、VQKV codec预算仍保留potential；Google受控人类基线/percentile协议和mini治理阈值调整也没有误关。具体准入与负侧理由、已读位置、root实际抽核边界见上述有限判断；没有实现复现、生产验证或无hacking/无危害认证。

## 5. 缺口与下一步

普通可执行待办：无（0）。以下为本窗外部终态保留项，不支持正面证据、Books或无遗漏断言；以后只按具体条件重开受影响材料。

12个arXiv家族均有[官方Submitted/history](../_sources/daily-20260318/V3_PRIMARY_ABSTRACTS.md)和arxiv.content/findable的registered原值。依据官方[availability](https://info.arxiv.org/help/availability.html)、[DOI](https://info.arxiv.org/help/doi.html)、[DataCite registered](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)/[states](https://support.datacite.org/docs/doi-states)，最早可能公告下界03/18 08:00BJT，保守上界registered+1秒；均跨09右端，不能用Updated、created或排程推成精确first-public。以下每项只请求一次：取得完全落窗的官方具体公告批次/时刻、或作者原始正文可靠首公开证据后，定点恢复对应准入命题和必要审阅；若证实窗外只路由真实归属日，不扩大本窗。

| 原材料v1 | registered原值（UTC，非精确公告） | 需要恢复的具体命题与限制 |
| --- | --- | --- |
| [FlashSampling 15854](https://arxiv.org/abs/2603.15854v1) | 2026-03-18T02:18:31.000Z | sampling/LMhead精确fusion；[作者项目](https://flashsampling.github.io/FlashSampling/)及[作者Blog](https://yifzhang.com/blog/FlashSampling/)又头写February28，须同时核原正文首公开归属，不机械先补公告后采用，不考古commit |
| [HAT 15953](https://arxiv.org/abs/2603.15953v1) | 2026-03-18T02:20:51.000Z | byte/word/backbone转换兼容边界；不授全部静态tokenizer可无损移除 |
| [HIPO 16152](https://arxiv.org/abs/2603.16152v1) | 2026-03-18T02:25:34.000Z | constrained训练utility/安全保证；strict safety只是作者主张，日期恢复后必须必要deep |
| [BATQuant 16590](https://arxiv.org/abs/2603.16590v1) | 2026-03-18T02:35:56.000Z | MXFP block-affine适用条件，不授native部署吞吐 |
| [Mask 15803](https://arxiv.org/abs/2603.15803v1) | 2026-03-18T02:17:17.000Z | density/complementary mask同预算因果范围 |
| [Conformal RAG 16817](https://arxiv.org/abs/2603.16817v1) | 2026-03-18T02:41:17.000Z | vacuity/shift/distractor/scorer成本，不授生产factuality概率保证 |
| [fleet-sim 16054](https://arxiv.org/abs/2603.16054v1) | 2026-03-18T02:23:15.000Z | queue/route/length sizing反例；request-level DES、手校准GPU，不授真实硬件预测 |
| [VQKV 16435](https://arxiv.org/abs/2603.16435v1) | 2026-03-18T02:32:18.000Z | codec重构/attention预算，10Mtoken代码本非零训练，不以ratio强纳 |
| [Persona Risk 15831](https://arxiv.org/abs/2603.15831v1) | 2026-03-18T02:17:56.000Z | sequential feedback的局部反证；persona/资金/目标同时改，不授纯persona因果或自报分数等于实际belief |
| [Fast-WAM 16666](https://arxiv.org/abs/2603.16666v1) | 2026-03-18T02:37:43.000Z | video cotraining vs test-time未来想象分离，不授所有世界模型无需rollout |
| [DreamPlan 16860](https://arxiv.org/abs/2603.16860v1) | 2026-03-18T02:42:20.000Z | suboptimal探索数据的videoWM训练有效条件；若仅已有组合也可具体前关闭，不因日期受阻降分 |
| [WorldCam 16871](https://arxiv.org/abs/2603.16871v1) | 2026-03-18T02:42:35.000Z | camera pose控制/历史检索的长期一致性，不授完整真实world state |

另2个潜在事件隔离：①[Google Cognitive Taxonomy](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/) 官方Blog的JSON-LD与published_time同为2026-03-17T16:00:00+00:00，即本窗内BJT03/18零点；原paper封面Mar16仍只有日级，正文首公开与Blog是否新增机制事件未定，不能把重述重新计家族。root17实际paperAB/§3的同instruction/fewshot/format/tools、人类代表性baseline、percentile profile协议可复用，非“未来hackathon无贡献”。只请求原PDF正文首次公开/精确版本依据；不再请求已恢复的Blog时刻，确认归属后只恢复该协议命题。②[OpenAI GPT5.4 mini安全附录](https://deploymentsafety.openai.com/gpt-5-4-thinking/appendix-gpt-5.4-mini)原HTML明确addedMar17 with launch，RSS launch03/17 10:00GMT在窗；但当前§6.3.1各段与launch原始精确版本的对应未证。请求原始launch附录或该阈值调整段首公开/修订说明；不把主卡Mar5或全部当前Hub内容反填。现读“GPT5/mini非BioHigh”的作者阈值判断与rail-free/refusal-inclusive对照有潜在治理增量，但153人RCT没有测mini本身，不授“无生物危害”；更强后续模型分类未改。两项均不支持当前Books或正面结论。

另5组来源外部限制：Google缺Pubs相关日级原发slice（年级372不变日期proof）；Meta缺Publication结果历史slice（access error）；Seed缺type2未返回5条的身份/日期（需本窗过滤或可说明14/19差额的真实公开记录，不能猜语言/删除原因）；MiMo缺本窗Blog原链接/日期（动态div+browser unavailable，可接受官方dated Blog/RFC/原报告）；MiniMax缺AgentTech历史slice及中文未恢复条目原日期（HTML shell/.md失败，英文12不替代全部）。每组取得真实相关历史日期目录即可只重开本窗受影响材料，不重扫全年，不以访问失败或搜索0授无命中。arXiv此前提交延迟公开的相关本窗batch亦在SRC-ARXIV限制中，不用Submitted查询声称完整召回。

## 6. 复核

日期保留项定点补正由root实际curl官方Blog380460B核验，JSON-LD与meta同值；只修正§5当前材料请求，未把Blog重述反填原PDF首公开。候选与Books数量不变。

复核者：root（非作者）
结论：通过

首批准入校准已通过：root实际完整首6 v1题摘/history及负侧15797/15909/16131和Persona潜在边界（10份AB）；后补16666/16871/16860/16435/16054完整v1题摘/history，再实际读原HTML保存的ResourceThreats v1完整AB，合计16份具名AB（12潜在+4负侧），仅准入层校准。另实际mini主文31–110、Japan31–62、MiniMax67–96及miniHub§6.3.1/addedMar17原HTML。Google协议复用root17实际paperAB/§3校准，仅本18日期另判；不称root重读其PDF。root没有逐项重读本日四主题元数据、VQKV/fleet方法与所有实验或3多模态全文，首批校准也不授日期、Evidence或Books。root已实际读完整六部分、14源停点、12日期JSON原值及14隔离/7关闭，并实际复核修正后的Anthropic March9条、DeepSeek完整公开数组和Googlepage2/2两card及§6；本18窗独立比较准确，不继承他日候选判断。最终非作者日级Gate通过：0确定候选/0Books，14日期或版本线索与另5组来源限制均安全终态隔离，普通0，无Books写后事项，不授全量召回或Evidence证明。

机器校验：本稿V3 validator PASS；限定日报及本日_sources的git diff --check无输出。只检查格式和可判定一致性，不替代日级语义Gate。未stage、commit或push。
