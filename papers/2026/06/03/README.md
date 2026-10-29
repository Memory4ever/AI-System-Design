# Daily Research — 2026-06-03

**规范：** V3
**窗口：** 2026-06-02T09:00:00+08:00 ～ 2026-06-03T09:00:00+08:00
**窗口说明：** 用户授权保留已有候选日期、评分、原窗口与有效证据，只补遗漏来源；原完整§4保持连续，不按新窗口搬移旧候选。
**补充窗口：** 2026-06-02 ～ 2026-06-02
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-25T18:56:21+08:00

## 1. 结论

本次只补Jun02北京时间自然日，保留原小时窗口、两旧候选日期/分数及有效证据。当前已处理146个唯一家族：115项实际整合并通过非writer真实写后复核、23项具体已有覆盖、4项仅报告（含2旧项）、1项四分关闭、3项中心争议暂缓。00251经R175/R177实际Ch66写后、01629经R176具体已有覆盖已同步；本轮末22具名全部必要/Books处置生效：16实际整合、5具体已有覆盖、1仅报告；00567旧漏交接又经R191–193准入/日证、必要/actualowner及唯一实际POST完成。此前27家族及有效证据保护。00130旧N因具体参数化贡献反例撤回，R196有限日期恢复后跨Jun01–02，列具名日期保留，不入146、不评分/续Methods或Books。**本次有限补查已完成，R197非writer日级独立复核通过；所有隔离项不作正面证据或无遗漏保证。**

新增长期机制包括外部trace比较与无reference生成的资格差异、冻结soft接口的监督权重时间路径、多agent改答的操作归因、双时域memory信用、无指令feed选择干预、父子约束传播、持续学习流/冻结读出资格、skill/tool联动版本、时间隔离评价、共同subchecks、选择性skill调用，以及训练-only与部署预测两类world-model消费。均融入现有owner论证，保留反退、混杂、成本与回退；不把作者实验当生产保证、已核代码或复现。

机构13源有限补查、模型/Agent/多模态末22具名与00567均已处理；00130潜在贡献保留，但可限定的公开区间跨日，必要层未作本窗采用。宽导航不是几百篇贡献；R197已验该新增终态差额并恢复日级通过，146既成层不重审。原87/MetaPoint旧日期及Google Research、Meta、Qwen、MiMo历史目录限制不支持零发布或无遗漏。

## 2. 来源覆盖

本轮机构执行与有限原件见[机构记录](../_sources/daily-20260603/SUP_ORG_20261023.md)，root已独立核RSS六事件与新增政策核心、Anthropic真实分页和旧事件复用边界。arXiv两切片有限发现及所有具名材料已处理，[有限停止](../_sources/daily-20260603/SUP_FINITE_STOP_20261025.md)经R197通过，不称全球无遗漏；不扫描Weekly组。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml)：web 不支持 XML，直接公开 GET 成功，1315 items。仅按 Jun02 BJT 日期过滤；前邻 Jun01 12Z，后邻 Jun03 10Z。6 事件见下表。 | 已检查 | 旧5事件复用；多出的 Jun01 17Z policy 已读完整核心后排除。RSS 当前保留不能证明删除项不存在。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)当前198 articles；首屏与 hydration 不是完整历史列表。由当前公开 chunk `04_9peblvyok2.js` 的 `listingPagesPath`/`fetch` 实际恢复 [page2](https://www.anthropic.com/listing/research/default/2)：`posts`24、`hasNextPage=true`，08/10→04/29；目标相邻06/03 `attack-navigator`→05/27 `coding-agents-social-sciences`。到低于目标日停止。 | 已检查 | 无目标日 metadata。初次把返回键误当 articles/rows，另外下载 page3/4 后才解析 posts，元数据已明显早于目标；未读其正文、未展开筛选队列，明确停止。不能沿用旧173 publication数量。 |
| SRC-GOOGLE-AI | [DeepMind page2](https://deepmind.google/blog/page/2/)当前7月→6月→5月，底部 Gemma4 12B→Singapore；[page3](https://deepmind.google/blog/page/3/)5月→4月，确认跨界停止。Gemma4 12B 的旧精确06/03 16Z日期证据未受影响，只作窗外边界，不重读。另实际打开 [Research pubs](https://research.google/pubs/)及[Blog](https://research.google/blog/)。只做目标日期官方域查询。 | 受阻 | DeepMind 当前有限边界无 Jun02条目；Google Research 仍无可恢复的目标日目录，pubs年度/当前首屏不能作日证。第一次搜索误写 `site.research.google` 而回传宽泛SEO结果，全部未采用；随后正确 domains 限官方域目标日无结果，也不作零命中。历史目录保留项继续隔离。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)解析空；[publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1) web两次timeout，直接公开GET成功285196字符，但实际可读条目出现2019/2018旧年月杂序，不再呈现旧06/05→05/27窗口边界。 | 受阻 | 未据空页/杂序宣称Jun02零命中。旧SA-3DAO核心negative及有限独核未失效，可复用而不重读；当前publication列表不足以新增历史覆盖断言。需目标日期排序目录/原始事件恢复，停止无差别翻页。 |
| SRC-QWEN | [旧站](https://qwenlm.github.io/)明示redirect→[qwen.ai](https://qwen.ai/research)，动态壳；实际公开前端 `0.0.85/js/969.js` 给出 `/api/page_config?code=`。只读 [news.news-list](https://qwen.ai/api/page_config?code=news.news-list)17项、日期2024/08/28～2025/04/28；[research.research-list](https://qwen.ai/api/page_config?code=research.research-list)60项、2022/11/14～2025/12/23。目标日期官方域补检无结果。 | 受阻 | 真实旧列表恢复，非当前2026完整目录；无可确认本窗新事件，2026历史缺口继续隔离。不以空搜索作0、不遍历全站。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)研究导航→[研究与动态](https://www.deepseek.com/news/)；研究06/24→02/25、动态09/10→04/24跨窗。 | 已检查 | 可见目标相邻范围无当日事件；到低于目标边界停止，不读其他日期正文；保留“查看全部”与当前目录留存局限。 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)26条Overview最晚2025/11/07。公开 GitHub releases API `kimi-code?per_page=100&page=1`83条，`kimi-cli?per_page=100&page=1`100条，均实际达到低于目标；Code0.9=06/03 14:01:42Z→0.8=06/02 14:56:13Z→0.7=06/02 02:23:53Z→0.6=05/29 14:24:54Z；CLI1.47=06/05 10:35:01Z→1.46=05/29 05:56:52Z。 | 已检查 | Code两事件旧家族去重，既有必要代码/正确性审阅和Only判断复用。未重读无关release、未把0.9记已审重复候选。 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)web壳；按来源要求尝试真实浏览器，创建tab超时并reset，未假称UI已读。公开HTML当前bundle `index-Uh_m57w8.js`定位 `/blog` chunk `index-Bnu48NkA.js`→`index-CeX5xNqy.js`，实际只读POST `https://api.hunyuan.tencent.com/api/blog/publicList`，参数 pageNum1/pageSize100/renderType0。zh totalNum11/list11，en9。见下面字段摘录。 | 已检查 | 全部公开 metadata 无Jun02；zh publicAt目标相邻07/06→05/21→04/30；Hy3preview内容date04/23但publicAt07/05，不混用。当前返回没有displayDate字段，不能复抄旧字段名。未读窗外正文；只检查cover日期。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)实际08/26→08/14→06/16 GLM5.2→05/20 ZCube；[官方发布说明](https://docs.z.ai/release-notes/new-released)06/16→04/07。 | 已检查 | 两官方可见相邻段均无Jun02，低于窗口停止。未把不同页面8月日期差异当本窗变化，也未读窗外正文；“查看更多”及当前目录留存局限仍在。 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)当前首20/246（旧242已变化），目标相邻06/04→06/03 MetaPoint→05/29。实际Blog公开bundle `main.6ec6cb71.js`给出只读GET `/api/get_article_list_v2`。article_type2/count20/order_desctrue，按research_area_id100～104五主线组各首批返回均has_more=false/next_page_token空，数量12/14/5/3/9。 | 已检查 | 无Jun02。Foundation06/23→02/14；Visual07/08→04/23（顶部另07/31）；Audio07/20→04/09（顶部另08/05）；Infra最晚2025；Frontier07/07→2025。Infra total4而返回3的差异只记录、不虚构第4条。论文接口article_type1单独GET只返总数/游标、无文章，未把它算正文清单；HTML目标边界已实际读。MetaPoint旧日期保留不改判、不转Jun02候选。 |
| SRC-BAIDU-ERNIE | [Blog zh](https://ernie.baidu.com/blog/zh/)page1/2：05/09→04/30→04/15→更早；低于目标即可停止，不请求page2正文。 | 已检查 | 当前保留目录无Jun02项；未扩成整站/历史正文审阅。 |
| SRC-XIAOMI-MIMO | [主页Paper/Blog](https://mimo.xiaomi.com/)原有限检查为Paper8条、Blog15无日期及公开静态route frontmatter，历史限制保留；新增定点实读[官方Model Release](https://mimo.mi.com/docs/en-US/updates/model)的09/22→**2026-06-02 mimo-v2.5-asr Released**→04/23相邻段。Jun02核心仅列双语/方言、歌词/复杂音频、知识密集识别能力。root原件阅读作非writer校准，作者独立读同段采用，见机构记录追加差额。 | 已检查 | 该具名事件日期已恢复，不是零事件或待全文；核心未披露新架构、训练目标、运行机制或受控设计取舍，按贡献前具体排除，不评分/候选/Books。Paper/Blog其余custom routes/CSR历史日期仍不能恢复，不由此声称目录完整或无遗漏；不扩读窗外正文。 |
| SRC-MINIMAX | [English Blog](https://www.minimax.io/blog)与[中文（redirect至minimax.cn）](https://www.minimaxi.com/blog)相邻06/09 MaxProof→06/01 M3；英文下一05/27，中文下一05/25。打开[当前Agent llms索引](https://agent.minimax.io/docs/llms.txt)72行，techblog区当前5项，见下段有限日期核。 | 已检查 | Blog无Jun02条目；索引不作当天发布证据。当前techblog已非旧1项，但具体文本指向9～10月，不反填6月；undated docs不支持本窗完整覆盖断言。 |
| SRC-ARXIV | Jun02 registered窗口仅导航；模型5页274及infra27/25，官方submitted主题35，Agent248/Multi214各一页。精确v1+同DOI arxiv.content/findable/registered+适用日程逐批联合日证；真实官方月列表有限语义差额见[标题补检](../_sources/daily-20260603/SUP_OFFICIAL_TITLE_DELTA_20261025.md)，不是公告或全分类检查。R196另只核LG六月页头/00130第6条，不浏览其余5233标题或翻页 | 受阻 | 有界发现、末22具名与00567均处理；[有限停止](../_sources/daily-20260603/SUP_FINITE_STOP_20261025.md)及00130终态差额经R197确认。目标日完整历史目录/API未恢复，已查范围/候选日证有效；00130潜贡献不再N但日期跨Jun01–02，不评分/当窗采用。辅助空检索非零发布，旧429不扩全源失败；日期/首发保留不支持候选、Books或无遗漏 |
| SRC-OPENREVIEW | 实际由02494同题五作者触发，只核[forum cMZ4Z7u5B5](https://openreview.net/forum?id=cMZ4Z7u5B5)、[PDF原入口](https://openreview.net/pdf?id=cMZ4Z7u5B5)与具名作者/venue渠道；复用R160及[有限原证](../_sources/daily-20260603/SUP_MONITORING_EARLY_SIGNAL_20261025.md)，不扩全venue | 受阻 | 会期/接受May26非正文公开日；forum验证页、API1/2均403，作者下载无历史日期。既有root所见PDF保留，不冒本次重新可读；它不证当期public release，不用于候选/Books/覆盖。重开需原始public release、pdate/odate/readers连同字段语义/公开历史组合、可靠历史快照或作者/venue首发公告，非单字段足证；只证forum未public不关闭作者渠道 |
| 表外：[FLAIRS出版方](https://journals.flvc.org/FLAIRS/article/view/141843) | 实际由00334同题三作者/VoR触发，只核article141843及[PDF147188](https://journals.flvc.org/FLAIRS/article/download/141843/147188)，复用R167与[精确登记原件](../_sources/daily-20260603/SUP_MODEL_00334_FLAIRS_CROSSREF_20261025.json) | 受阻 | online May06/created及VoR标签不等首次可读正文，两具名正常入口403；不扩issue/venue或用提交补first-public。重开限可读VoR与对应官方历史公开界/发布日期，或明确窗内重要revision依据；已读必要保留但不作本窗正面采用 |

## 3. 候选与判断

原两行日期/分数不动；其后144个新增家族已通过独立准入/联合日证并作必要证据及Books处置，其中00376/00674证明与01451测量三项中心争议隔离，不代表全部主张已证实或全球无遗漏。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.7.0 / 0.8.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.7.0) | 2026-06-02T10:23:53+08:00 ～ 2026-06-02T22:56:14+08:00 | 独立goal/TODO与typed undo/replay、审批observer具体改变长会话状态恢复边界；2+2+2=6 | 深入完成 | 仅报告：版本实现新增，不宣称现有Ch81泛主题全部覆盖；长期context/worldeffect/resume分账由实际正文承载 |
| [Codex roles / ChatGPT Sites](https://openai.com/index/codex-for-every-role-tool-workflow) | 2026-06-02T17:00:00+08:00 ～ 2026-06-02T18:00:01+08:00 | artifact局部context与受管理hosted输出、独立automation刷新→review→redeploy改变交付边界；1+2+2=5 | 标准完成 | 仅报告：公开publication/refresh接口事实，无新运行实现/因果评价，成熟review/permission原则不加高分 |
| [Schedule-Level Shared-Prefix Reuse for LLM RL Training](https://arxiv.org/html/2606.01143v1) | 2026-06-02 | schedule级prefix VJP复用与逻辑token计数；3+3+2=8 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；独立R1/R7已通过，具体范围见§4 |
| [SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving](https://arxiv.org/html/2606.01751v1) | 2026-06-02 | Sparse-Q跨层修正与命中physical copy费用；2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；独立R3/R7已通过，具体范围见§4 |
| [Confidence-Adaptive SwiGLU for Mixture-of-Experts](https://arxiv.org/html/2606.00761v1) | 2026-06-02 | router affinity参与expert内部激活与真实吞吐取舍；2+1+2=5 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)；独立R4/R7已通过，具体范围见§4 |
| [A Pre-Training Analogue of Grokking in Language Models: Tracing Delayed Grammatical Generalization](https://arxiv.org/html/2606.00230v1) | 2026-06-02 | 关键短语曝光代理/选择条件下延迟语法泛化；2+1+2=5 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；独立R5/R10已通过，具体范围见§4 |
| [Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools](https://arxiv.org/html/2606.02483v1) | 2026-06-02 | issue-time逐observer披露、三假设与弱labeler边界；3+2+3=8 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)；独立R2/R7已通过，具体范围见§4 |
| [Retrieve What's Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation](https://arxiv.org/html/2606.02479v1) | 2026-06-02 | target-pixel残余覆盖的联合选择，不授depth单独必胜；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；独立R6/R10已通过，具体范围见§4 |
| [Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains](https://arxiv.org/html/2606.02357v1) | 2026-06-02 | tool trace与answer-critical信息贡献分责；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)；独立R8已通过，具体范围见§4 |
| [Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution](https://arxiv.org/html/2606.01435v1) | 2026-06-02 | 候选抽取与确定性版本策略分责，whole-pipeline非resolver因果；3+2+2=7 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)；独立R9/R11已通过，具体范围见§4 |
| [SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision](https://arxiv.org/html/2606.01139v1) | 2026-06-02 | skill缺陷门控/保持与锚定编辑、search-base与best-return分责；2+1+2=5 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)；独立必要Source/PRE与真实POST通过，范围见§4 |
| [TVIR: Building Deep Research Agents Towards Text–Visual Interleaved Report Generation](https://arxiv.org/html/2606.02320v1) | 2026-06-02 | figure/caption/context/source分项及原件/修订测量视图区分；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；非临时Ch81路由，独立Source/PRE/真实POST通过 |
| [Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate](https://arxiv.org/html/2606.00820v1) | 2026-06-02 | 同题改答的自反思、stance与reasoning条件归因，并将个体与聚合分账；3+2+2=7 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)；本轮独立必要证据/owner及实际POST通过 |
| [CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems](https://arxiv.org/html/2606.00756v1) | 2026-06-02 | local episode与cloud subgoal guidance分离；云聚合不取得原始事实所有权；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)；本轮独立必要证据/owner及具体覆盖通过 |
| [Enhancing LLM Metacognition via Cognitive Pairwise Training](https://arxiv.org/html/2606.00869v1) | 2026-06-02 | 含reference四类trace比较监督与无reference生成的迁移边界；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)；本轮独立必要证据/owner及实际POST通过 |
| [Towards Lightweight Reliability: Using Soft Prompts for Hallucination Mitigation in Large Language Models](https://arxiv.org/html/2606.00919v1) | 2026-06-02 | 冻结输入接口中目标混合的时间路径，而非仅参数量；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)；本轮独立必要证据/owner及实际POST通过 |
| [Learning to Retrieve: Dual-Level Long-Term Memory for Text-to-SQL Agents](https://arxiv.org/html/2606.00547v1) | 2026-06-02 | episode结果信用与turn PRM代理分责；2+1+2=5 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)；独立Source/PRE与真实POST通过 |
| [Adversarial Feeds Steer LLM Agent Decisions Against Their Defaults](https://arxiv.org/pdf/2606.00914v1) | 2026-06-02 | 无显式指令的多轮feed选择也可改变决策；3+2+2=7 | 深入完成 | 整合：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md)；独立Source/PRE与真实POST通过 |
| [Discovering Agents for Discovery: The Case for DNS](https://arxiv.org/html/2606.02314v1) | 2026-06-02 | 跨registry发现依赖与完整wire预算；2+2+1=5 | 深入完成 | 整合：`AGENT-MCP`，[Ch83](../../../../books/part-07-agent/83-mcp.md)；独立Source/PRE与真实POST通过 |
| [ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use](https://arxiv.org/html/2606.00341v1) | 2026-06-02 | benign任务中的纠正控制反证及父子约束传播；3+2+2=7 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md)；独立Source/PRE与真实POST通过 |
| [AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents](https://arxiv.org/html/2606.02461v1) | 2026-06-02 | 受控可复用流、naive干扰流与冻结读出/heldout分验；2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)；独立Source/PRE与真实POST通过 |
| [SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems](https://arxiv.org/html/2606.01314v1) | 2026-06-02 | 依赖skill/tool原子bundle与分级验证/失败存档；2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)；独立Source/PRE与真实POST通过 |
| [ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment](https://arxiv.org/html/2606.00644v1) | 2026-06-02 | visible cutoff/hidden future与引用/决策对象分验；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；独立Source/PRE与真实POST通过 |
| [FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification for Agentic Search](https://arxiv.org/html/2606.00660v1) | 2026-06-02 | 固定跨候选requirements，缺证不得计支持；2+1+2=5 | 深入完成 | 整合：`AGENT-REFLECTION`，[Ch80](../../../../books/part-07-agent/80-reflection.md)；独立Source/PRE与真实POST通过 |
| [Skill or Skip? Learning Selective Skill Invocation in Agentic Tasks via Dual-Granularity Preference Learning](https://arxiv.org/html/2606.00510v1) | 2026-06-02 | shared-prefix invoke/skip偏好区分相关skill与此刻调用效用；2+2+2=6 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)；独立Source/PRE与真实POST通过 |
| [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/html/2606.02388v1) | 2026-06-02 | on-policy next-observation训练辅助与部署想象环分开；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；独立Source/PRE与真实POST通过 |
| [COMAP: Co-Evolving World Models and Agent Policies for LLM Agents](https://arxiv.org/html/2606.02372v1) | 2026-06-02 | 实际executed transition与EMA特权训练/部署student分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；独立Source/PRE与真实POST通过 |
| [Beyond Visual Memory: Mechanistic Diagnostics of Latent Visual Reasoning](https://arxiv.org/html/2606.01287v1) | 2026-06-02 | latent内容、marker和格式的拆分诊断；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces](https://arxiv.org/html/2606.01317v1) | 2026-06-02 | workspace副作用与终态拒答分验；2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Same Payload, Different Channel: Measuring Trust Asymmetry in Tool-Using Language Models](https://arxiv.org/html/2606.00566v1) | 2026-06-02 | metadata/output渠道的相反风险及测量混杂；3+2+2=7 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary](https://arxiv.org/html/2606.00376v1) | 2026-06-02 | reasoning状态容量与训练上限强主张的证明边界；3+2+2=7 | 争议 | 暂缓：中心证明桥未闭，见§4/§5 |
| [AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations](https://arxiv.org/html/2606.02240v1) | 2026-06-02 | integration-disjoint检测与真实防御收益分验；2+2+2=6 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence](https://arxiv.org/html/2606.02380v1) | 2026-06-02 | 压力配对下plan、action与自述的独立判定；2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability](https://arxiv.org/html/2606.01365v1) | 2026-06-02 | loop/output/grounding分层而非终答代进展；2+1+2=5 | 深入完成 | 整合：`PLATFORM-TRACE`，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Reducing Token Usage of State-in-Context Agents using Minification](https://arxiv.org/html/2606.01326v1) | 2026-06-02 | 程序语义保持不等于LLM消费者信息保持；2+1+2=5 | 深入完成 | 整合：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL](https://arxiv.org/html/2606.01619v1) | 2026-06-02 | 旧/新skill在演化policy内的组内信用；2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [When Hard Negatives Hurt: Bridging the Generative-Discriminative Gap in Hard Negative Synthesis for Retrieval](https://arxiv.org/html/2606.01304v1) | 2026-06-02 | 生成负例的来源shortcut与监督正则分责；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG`，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning](https://arxiv.org/html/2606.02132v1) | 2026-06-02 | tool-free对照与difficulty shaping学习调用必要性；2+2+2=6 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression](https://arxiv.org/html/2606.02559v1) | 2026-06-02 | Attention/FFN分别选取与replacement可拟合性；2+1+2=5 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER`，[Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [ResMerge: Residual-based Spectral Merging of Large Language Models](https://arxiv.org/html/2606.02252v1) | 2026-06-02 | 完整RL task-vector head/residual与agreement门控；2+1+2=5 | 深入完成 | 整合：`TRAIN-LORA`，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [An Algebraic View of the Expressivity of Recurrent Language Models](https://arxiv.org/html/2606.01765v1) | 2026-06-02 | 算术语义改变受限递推parity能力；3+1+3=7 | 深入完成 | 整合：`MODEL-LONG-CONTEXT`，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [A Finite-Calibration Regime Map for LLM Judge Panels](https://arxiv.org/html/2606.01034v1) | 2026-06-02 | 有限人标下judge-panel联合cell的估计压力；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [On the Generalization Gap in Self-Evolving Language Model Reasoning](https://arxiv.org/html/2606.01075v1) | 2026-06-02 | 自反馈标签闭环与oracle/scale边界；2+1+2=5 | 深入完成 | 整合：`TRAIN-DPO`，[Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [ProjQ: Project-and-Quantize for Adapter-Aware LLM Compression](https://arxiv.org/html/2606.00494v1) | 2026-06-02 | PTQ误差塑形与adapter有限rank容量耦合；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA`，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning](https://arxiv.org/html/2606.00395v1) | 2026-06-02 | 未来route预测、current replay与density身份分责；2+2+2=6 | 深入完成 | 整合：`TRAIN-PPO`，[Ch32](../../../../books/part-04-training-system/32-ppo.md) |
| [Massive Spikes in LLMs are Bias Vectors: Mechanistic Uncovering and Spike-Free Quantization](https://arxiv.org/html/2606.02288v1) | 2026-06-02 | 去spike后显式恢复sink的K/V与末端功能；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Geometric Latent Reasoning Induces Shorter Generations in LLMs](https://arxiv.org/html/2606.02248v1) | 2026-06-02 | 冻结embedding位移latent及两pass预算接口；2+1+2=5 | 深入完成 | 整合：`MODEL-DECODER-ONLY`，[Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Extreme Low-Bit Inference in Reasoning Models: Failure Modes and Targeted Recovery](https://arxiv.org/html/2606.02011v1) | 2026-06-02 | 低bit轨迹膨胀与commit/fallback全路径费用；3+2+2=7 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads](https://arxiv.org/html/2606.01927v1) | 2026-06-02 | 单node一轮准备与sequence分片采样的一致性；2+2+2=6 | 深入完成 | 整合：`INFER-VLLM`，[Ch50](../../../../books/part-05-inference-system/50-vllm.md) |
| [Resonant Context Anchoring: Decoupling Attention Routing and Signal Gain at Inference Time](https://arxiv.org/html/2606.01923v1) | 2026-06-02 | 固定routing概率下query-specific Value gain；2+1+2=5 | 深入完成 | 整合：`MODEL-SELF-ATTENTION`，[Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [Move the Query, Not the Cache: Characterizing Cross-Instance Latent and Sparse Attention Redistribution Across GPU Fabrics](https://arxiv.org/html/2606.01502v1) | 2026-06-02 | route/fetch/local跨实例attention的全成本反转；2+2+2=6 | 深入完成 | 整合：`INFER-DYNAMO`，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [ScanWeaver: Compiler-Driven Parallelization of Affine Recurrences via Associative Scan Lowering](https://arxiv.org/html/2606.00601v1) | 2026-06-02 | affine recurrence编译IR与matched-forward比较；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction](https://arxiv.org/html/2606.01850v1) | 2026-06-02 | 压缩后accuracy、预测集覆盖与大小不能互相代签；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ProbeScale: Probing Analysis to Optimize Neural Scaling Laws for Efficient Small Language Model Inference](https://arxiv.org/html/2606.01806v1) | 2026-06-02 | task-weighted probe作budgeted contiguous layer选择；1+1+2=4 | 已关闭 | 仅报告：局部probe加权裁层方案，未提供需进一步采用的长期机制差额 |
| [Off-the-Shelf LLMs as Process Scorers: Training-Free Alternative to PRMs for Mathematical Reasoning](https://arxiv.org/html/2606.01682v1) | 2026-06-02 | 大模型likelihood用于生成中chunk选择的长度/时点边界；2+1+2=5 | 深入完成 | 整合：`MODEL-SAMPLING`，[Ch20](../../../../books/part-02-model/20-sampling.md) |
| [CANARY: Zero-Label Detection of Fine-Tuning Contamination in Language Models](https://arxiv.org/html/2606.01695v1) | 2026-06-02 | 可信base差分与clean参考下的whitebox候选审计信号；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；独核R30–33实际Source/owner/POST通过 |
| [TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment](https://arxiv.org/html/2606.01755v1) | 2026-06-02 | 同题多persona离线未来反馈与客观真值/风格分责；2+1+2=5 | 深入完成 | 整合：`TRAIN-RLHF`，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)；独核R30–33实际Source/owner/POST通过 |
| [DOT-MoE: Differentiable Optimal Transport for MoEfication](https://arxiv.org/html/2606.01666v1) | 2026-06-02 | 联合neuron分组与token routing、dense-mask到物化expert转换；2+2+2=6 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)；独核R30–33实际Source/owner/POST通过 |
| [Don't Let a Few Network Failures Slow the Entire AllReduce](https://arxiv.org/html/2606.01680v1) | 2026-06-02 | 健康局部归约/慢rank合并回送/健康allgather流水；2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；同alias具体机制refine，旧Books trace归属不搬 |
| [AlphaToken: Decoupling Adaptation and Stability for Path-Aware Response Token Valuation in LLM Post-Training](https://arxiv.org/html/2606.01635v1) | 2026-06-02 | 目标验证/参考Fisher漂移与有限Value路径共同选择监督；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)；独立R38/R41实际Source/owner/POST通过 |
| [ProbMoE: Differentiable Probabilistic Routing for Mixture-of-Experts](https://arxiv.org/html/2606.01509v1) | 2026-06-02 | 固定基数subset采样与精确条件边际STE、部署MAP分责；2+1+2=5 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)；独立R37/R41实际Source/owner/POST通过 |
| [TwinQuant: Learnable Subspace Decomposition for 4-Bit LLM Quantization](https://arxiv.org/html/2606.01556v1) | 2026-06-02 | 共同postquant目标与INT32中间片上scale/requant/pack消费接口；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；独立R40/R42实际Source/owner/POST通过 |
| [Cross-lingual Self-Consistency for Multilingual Reasoningwith Language Models](https://arxiv.org/html/2606.01464v1) | 2026-06-02 | canonical答案频率的语言目标人口/参考分布及强弱语言取舍；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)；R43/45必要/actual-owner及唯一实际POST通过 |
| [AMP / memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations](https://arxiv.org/html/2606.01138v1) | 2026-06-02 | 同schema/capability-qualified测试不保证后端scope/id/空policy操作语义可迁移；2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)；R47–50纠正原N、必要/actual-owner与实际POST通过 |
| [Before and After Temperature: A Distributional View of Creative LLM Generation](https://arxiv.org/html/2606.01451v1) | 2026-06-02 | 同步观测温度变换前后分布的测量资格与捕获失配；2+1+2=5 | 争议 | 暂缓：中心采集/概率分母冲突，不能由高相关授予创造力诊断，见§4/§5 |
| [Learning from Saturated Data: Signals Beyond Correctness for LLM Training](https://arxiv.org/html/2606.01436v1) | 2026-06-02 | 经验饱和正确样本的质量排序及离线目标/迁移反退；2+1+2=5 | 深入完成 | 整合：`TRAIN-DPO`，[Ch34](../../../../books/part-04-training-system/34-dpo.md)；R54必要/owner/PRE、R55唯一实际POST通过，见§4 |
| [Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents](https://arxiv.org/html/2606.00476v1) | 2026-06-02 | 前提/结论/动作与结论读出噪声分层测量；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R56必要/owner/PRE与R58唯一实际POST通过，见§4 |
| [OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents](https://arxiv.org/html/2606.02031v1) | 2026-06-02 | 多轮RL中horizon与managed context支持及同基准消融边界；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)；R59必要/owner/PRE与R61唯一实际POST通过，见§4 |
| [Consistent and Distinctive: LLM Benchmark Efficiency via Maximum Independent Set Prompt Selection on Similarity Graphs](https://arxiv.org/pdf/2606.01400v1) | 2026-06-02 | 子集selection种子间排名一致与对全量排名保真两参照分账；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R63必要/owner/PRE、R65唯一实际POST通过，见§4 |
| [Fail-Closed Lowering of Resident KV Claims onto LLM Serving Runtimes](https://arxiv.org/html/2606.01387v1) | 2026-06-02 | 观察adapter与scheduler/allocator/storage执行义务分责；同claim恢复/失败顺序限定；2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；R66必要/owner/PRE、R68唯一实际POST通过，见§4 |
| [RLVR without Ineffective Samples: Group Prioritized Off-Policy Optimization for LLM Reasoning](https://arxiv.org/html/2606.01281v1) | 2026-06-02 | 完整有效组补空槽与behavior/proximal双参照分责；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)；R69必要/PRE、R72唯一实际POST通过，见§4 |
| [Real2SAM2Real: Generative 3D Caches as Complementary Context for Video Diffusion](https://arxiv.org/html/2606.00299v1) | 2026-06-02 | 完整前景cache/normal软条件与外观分责，非已辨识物理transition；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；R70必要/PRE、R73唯一实际POST通过，见§4 |
| [Thinking Economically: A Hierarchical Framework for Adaptive-Complexity Reasoning in LLMs](https://arxiv.org/html/2606.01168v1) | 2026-06-02 | 题目预算标签与训练期步骤压缩两级监督，代理/过滤人口分责；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)；R74必要/PRE、R77唯一实际POST通过，见§4 |
| [When Data Is Scarce: Scaling Sparse Language Models with Repeated Training](https://arxiv.org/html/2606.01155v1) | 2026-06-02 | unique数据/重复与稀疏容量共同饱和、预算与硬件成本分账；2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING`，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)“数据受限的Scaling”完整两段；R78必要/具体NC通过，无新书段，见§4 |
| [StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement](https://arxiv.org/html/2606.00267v1) | 2026-06-02 | 局部noise压力提案与独立随机风险频率分账，非物理或全局最坏保证；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；R79必要/PRE、R81唯一实际POST通过，见§4 |
| [DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts](https://arxiv.org/html/2606.01062v1) | 2026-06-02 | 选后expert输出的成对非线性组合与顺序深度，非额外稀疏执行；2+1+2=5 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)；R84必要/PRE、R87唯一实际POST通过，见§4 |
| [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](https://arxiv.org/html/2606.02486v1) | 2026-06-02 | 运动patch预测供冻结动作decoder消费，以方差限制视野而非认证安全；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；R85必要/PRE、R88唯一实际POST通过，见§4 |
| [SafeVLA-Bench: A Benchmark for the Success–Safety Gap in Vision-Language-Action Models](https://arxiv.org/html/2606.00773v1) | 2026-06-02 | task-valid适用集、成功违例联合人口与最坏深度分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；R89必要/PRE、R90唯一实际POST通过，见§4 |
| [Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference](https://arxiv.org/html/2606.01007v1) | 2026-06-02 | task条件共激活软重权与placement/负载取舍，代理不等时延；2+2+2=6 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)；R92必要/PRE、R94唯一实际POST通过，见§4 |
| [Detect Before You Leap: Mirage Detection in Vision–Language Models](https://arxiv.org/html/2606.00435v1) | 2026-06-02 | 固定readout跨层相关性sensor与候选答案release分责；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；R95必要/PRE、R96唯一实际POST通过，见§4 |
| [Decoding in Order-Agnostic Language Models: Chain-Rule Deviation and Uniform Spreading](https://arxiv.org/html/2606.00997v1) | 2026-06-02 | 固定目标跨揭示顺序的条件相容性诊断，自产confidence与可靠性分责；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R97必要/PRE、R99唯一实际POST通过，见§4 |
| [Lodestar: An Online-Learning LLM Inference Router](https://arxiv.org/html/2606.00946v1) | 2026-06-02 | 路由改变训练人口，决策快照/所选TTFT反馈与近期及多样回放分责；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；R100必要/PRE、R102唯一实际POST通过，见§4 |
| [Training-Free Image Inversion for One-Step Diffusion Models](https://arxiv.org/html/2606.01380v1) | 2026-06-02 | 冻结生成器的逐图噪声/条件两阶段适配与重复消费成本；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R101必要/PRE、R104唯一实际POST通过，见§4 |
| [Memory-Efficient LLM Training with Dynamic Sparsity: From Stability to Practical Scaling](https://arxiv.org/html/2606.00888v1) | 2026-06-02 | regrowth后的局部optimizer时钟、warm-up与active-only状态边界；2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING`，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)动态稀疏三完整段，R105通过，不造diff |
| [Knowledge-Intensive Video Generation](https://arxiv.org/html/2606.01285v1) | 2026-06-02 | 视频事实精度、用途完成、原片grounding与偏好agreement分账；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)视频目标/claim支持/三轴/Agreement具体组，R107通过 |
| [CUPID in the Model Zoo: Online Matchmaking for Selecting Your Dream LLM](https://arxiv.org/html/2606.00846v1) | 2026-06-02 | 个人目标belief与目标条件utility共同提出比较pair，偏好/预算/部署资格分账；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，R108必要/PRE及R111唯一实际POST通过 |
| [PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation](https://arxiv.org/html/2606.00515v1) | 2026-06-02 | VLA语义proposal与sampled diagonal-admittance端口证书/任务安全分责；2+2+2=6 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)Passivity Shield三完整段，R109具体NC通过 |
| [Mitigating Hallucinations in Large Language Models Via Decoder Layer Skipping](https://arxiv.org/html/2606.00819v1) | 2026-06-02 | 仅词表readout方向提出已算residual插值候选，公式/传播语义未闭不授完整路径收益；2+1+2=5 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER`，[Ch17](../../../../books/part-02-model/17-transformer-layer.md)，只R112修后单段与R114唯一实际POST通过，非完整算法验收 |
| [Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs](https://arxiv.org/html/2606.00813v1) | 2026-06-02 | 冻结source攻击归档再跨target重放，分开搜索适应与迁移分母；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，R115必要/PRE与R117唯一实际POST通过 |
| [Mechanistic Diagnostics of Spatial Lexical Bias in Multimodal Large Language Model Spatial Reasoning](https://arxiv.org/html/2606.01914v1) | 2026-06-02 | 同图选项语义对照、局部state杠杆与冻结视觉适配的归因边界；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，R116必要/PRE与R118唯一实际POST通过 |
| [Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety](https://arxiv.org/html/2606.00801v1) | 2026-06-02 | 按描述符保留局部最强攻击，但cell覆盖、judge与迁移权限分账；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)Adversarial Coverage完整段及00813归档/分母段，R120具体NC通过，非duplicate |
| [RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation](https://arxiv.org/html/2606.01600v1) | 2026-06-02 | 指令可行性改变completion评价方向，分开有害/不可行与拒绝分母；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，R119必要/PRE与R121唯一实际POST通过 |
| [ViBE: Co-Optimizing Workload Skew and Hardware Variability for MoE Serving](https://arxiv.org/html/2606.00735v1) | 2026-06-02 | 按负载条件逐卡耗时与expert需求共同放置，分开静态收益和动态recipe；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，R124必要/PRE与R126唯一实际POST通过 |
| [TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation](https://arxiv.org/html/2606.00232v1) | 2026-06-02 | 固定观察图/每轮claim图隔离与确定性局部修补预算，risk不是事实概率；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，R125修后PRE与R127唯一实际POST通过 |
| [The Paradox of Outcome Optimization: A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs](https://arxiv.org/html/2606.00674v1) | 2026-06-02 | reward screening与过程监督能否改变shortcut可行解，而非仅增加密集credit；3+1+2=6 | 争议 | 暂缓：中心理论的商空间/OOD人口、loss下界和MI/实际process目标桥未闭；R128必要审阅及隔离通过，不进入Books，精确重开见§4 |
| [τ0-WM: A Unified Video-Action World Model for Robotic Manipulation](https://arxiv.org/html/2606.01027v1) | 2026-06-02 | 两级重去噪/模拟预算与LAR重新提案后的证据身份，旧动作评价不可继承；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，R129必要/原PRE与R130唯一实际POST通过 |
| [The Invitation Trap: Proactive Availability Backdoor in LLMs via Conversational Induction](https://arxiv.org/html/2606.00654v1) | 2026-06-02 | 被污染assistant主动建议塑造后续trigger暴露，建议/接受与执行权须分责；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)“模型建议也可能塑造未来 Trigger”完整两段，R131具体NC通过，撤原重复PRE，不降分/不搬日期 |
| [Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition](https://arxiv.org/html/2606.00959v1) | 2026-06-02 | 条件决策分解区分模态unique/redundant/synergistic贡献，训练重权与真实质量分验；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，R132必要/原两段PRE与R133唯一实际POST通过 |
| [Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems](https://arxiv.org/html/2606.00804v1) | 2026-06-02 | 固定任务类映射不保证最佳协调，负证据与后验容差须分账；2+1+2=5 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)具体task-slice/equal-budget/协调税与router误判回退组，R135通过 |
| [MESA: Improving MoE Safety Alignment via Decentralized Expertise](https://arxiv.org/html/2606.00651v1) | 2026-06-02 | 专家更新域选择与安全/一般双流router目标配对，使用频率不等安全语义；2+2+2=6 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)，R134必要/原单段PRE与R136唯一实际POST通过 |
| [Understanding the Self-Reflection Mechanisms of LLMs through Biased Attitude Associations](https://arxiv.org/html/2606.00600v1) | 2026-06-02 | 总投影离散度与组标准化effect在尺度变化下不同，表示平滑不授行为公平；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，R137必要/原单PRE与R139唯一实际POST通过 |
| [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/html/2606.01770v1) | 2026-06-02 | 分支构造/当时选用两个状态，有限oracle headroom不等真实路由收益；2+2+2=6 | 深入完成 | 整合：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md)，R138必要/原两段PRE与R140唯一实际POST通过 |
| [Hierarchical Online Prompt Mutation with Dual-Loop Feedback for Guardrailed Evidence Document Generation: A Production-Evaluation Case Study](https://arxiv.org/html/2606.01472v1) | 2026-06-02 | family/version选择与失败后局部编辑的责任分离；2+1+2=5 | 深入完成 | 已有覆盖：`AGENT-PROMPT`，[Ch74](../../../../books/part-07-agent/74-prompt.md)；R141核版本池/constraint-residual/SkillOpt具体正文，见§4 |
| [Revisiting Parameter-Based Knowledge Editing in Large Language Models: Theoretical Limits and Empirical Evidence](https://arxiv.org/html/2606.00570v1) | 2026-06-02 | 参数改动绝对大小与相对表示尺度/行为保留分责；2+2+2=6 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；R142修句PRE/R143唯一actualPOST，见§4 |
| [Self-Conditioned Positional HNSW for Overlap-Aware Retrieval in Chunked-Document RAG Systems: Method and Industrial Evidence-Quality Audit](https://arxiv.org/html/2606.01542v1) | 2026-06-02 | 首检条件的位置先验改变索引/查询度量，再独立gap选集；2+1+2=5 | 深入完成 | 整合：`AGENT-RAG`，[Ch76](../../../../books/part-07-agent/76-rag.md)；R144修后PRE/R145唯一actualPOST，只待验证接口，见§4 |
| [DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation](https://arxiv.org/html/2606.01212v1) | 2026-06-02 | 固定相关query群上直接话题防护的审计人口边界；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG`，[Ch76](../../../../books/part-07-agent/76-rag.md)；R146修句PRE/R147唯一actualPOST，见§4 |
| [Escaping the Mode Lottery: Multi-Response Training Improves Language Model Generalization](https://arxiv.org/html/2606.00544v1) | 2026-06-02 | prompt覆盖与conditional response采样的方差/目标及成本分责；2+1+3=6 | 深入完成 | 整合：`TRAIN-DATA`，[Ch27](../../../../books/part-04-training-system/27-data.md)；R148修后PRE/R149唯一actualPOST，见§4 |
| [GNMR: Runtime Stability Control for Low-Precision Large Language Model Training](https://arxiv.org/html/2606.00539v1) | 2026-06-02 | 双时域历史归一风险与受预算可恢复执行分责；2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING`，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)；R150核同family实际完整三段，非旧trace判重，见§4 |
| [Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories](https://arxiv.org/html/2606.02060v1) | 2026-06-02 | 有害承诺/支持/传播与普通探索的过程测量；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R151核同family完整两段及Ch69依赖分责，见§4 |
| [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/html/2606.00516v1) | 2026-06-02 | phase干扰/launch摊销与idle-slot、KV容量的切换选择；3+2+2=7 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；R152核同family完整三段，保模型/硬件/队列与SLO边界，见§4 |
| [BraveGuard: From Open-World Threats to Safer Computer-Use Agents](https://arxiv.org/html/2606.01166v1) | 2026-06-02 | 外部威胁到执行监督、内部数据更新与独立外部验收分责；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；R153原两段PRE/R154唯一actualPOST，见§4 |
| [Canonicalized Stable-List Replay for Private Federated Continual Learning over Language-Model Embeddings](https://arxiv.org/html/2606.00426v1) | 2026-06-02 | 无序回放候选先建立条件canonical身份再merge；2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；R155原两段PRE/R156唯一actualPOST，见§4 |
| [LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation](https://arxiv.org/html/2606.02553v1) | 2026-06-02 | 固定生成器外的retrieval-key几何与真实context分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；R157原两段PRE/R158唯一actualPOST，见§4 |
| [Detector-Evasive LLM Paraphrasing via Constrained Policy Optimization](https://arxiv.org/html/2606.00392v1) | 2026-06-02 | 期望语义proxy阈值反馈与分项组归一的约束单位分责；2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)；R159核FGRPO/GDPO/CGRPO完整具体正文，见§4 |
| [CRMA: A Spectrally-Bounded Backbone for Modular Continual Fine-Tuning of LLMs](https://arxiv.org/html/2606.00382v1) | 2026-06-02 | 共享可训练基底与逐任务参数隔离的局部取舍；2+1+2=5 | 标准完成 | 仅报告：关键机制未披露；中心桥未证、测量对象及FROZEN漂移冲突保持隔离，R161见§4 |
| [SPARQLe: Sub-Precision Activation Representation for Quantized LLM Inference](https://arxiv.org/html/2606.00365v1) | 2026-06-02 | activation位平面联合执行与bitmap成本、无损分解/有损增强分责；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；R162 PRE、R164落位失败已定点修复、R165实际POST通过，见§4 |
| [Active Exploring like a Pigeon: Reinforcing Spatial Reasoning via Agentic Vision-Language Models](https://arxiv.org/html/2606.02459v1) | 2026-06-02 | 按需视图消费、估计map更新与空间谓词检查的监督接口；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；R163原两段PRE与R166唯一actualPOST，见§4 |
| [HLL: Can Agents Cross Humanity's Last Line of Verification?](https://arxiv.org/html/2606.02449v1) | 2026-06-02 | 终态命中与家族专用过程规则接受集合的测量分责；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R168核过程指令/AuditKIT/Procedure-Aware具体正文，见§4 |
| [Geometry-Aware Implicit Memory for Video World Models](https://arxiv.org/html/2606.02436v1) | 2026-06-02 | 非frame-indexed记忆的camera-query训练监督与推理辅助consumer移除；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；R169原两段PRE与R170唯一actualPOST，见§4 |
| [Rethinking the Role of Temperature in Large Language Model Distillation](https://arxiv.org/html/2606.00306v1) | 2026-06-02 | 蒸馏温度与KL方向共同定义目标/梯度及局部排名；3+1+2=6 | 深入完成 | 整合：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)；R171原单PRE与R173唯一actualPOST，见§4 |
| [Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference](https://arxiv.org/html/2606.02430v1) | 2026-06-02 | 自回归stage/operator/dtype保护预算与无fault质量/共享KV盲区；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；R172原单PRE与R174唯一actualPOST，见§4 |
| [Teaching LLMs to Know Their Limits](https://arxiv.org/html/2606.00251v1) | 2026-06-02 | 同model自评更新改变可解性标签，重探测与原solver保持双参照；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R175必要与R177实际POST，见§4 |
| [Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation](https://arxiv.org/html/2606.01629v1) | 2026-06-02 | 长文多协议judge的构念、输入失败与长度切片边界；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R176实际完整论点比较，见§4 |
| [On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on Annotation Task Performance](https://arxiv.org/html/2606.00467v1) | 2026-06-02 | 定义匹配配对sensor与文本熟悉、原错救回/原对损坏分别验证；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R178必要/具体差额、R179唯一实际POST，见§4 |
| [DECK: A Consistency × Confidence Taxonomy of LLM Hallucinations](https://arxiv.org/html/2606.02289v1) | 2026-06-02 | scorer族可观察面与外部切片，构造分歧不证独立盲区定理；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R178具体正文比较，见§4 |
| [The Shape of Wisdom: Decision Trajectories in Language Models](https://arxiv.org/html/2606.01202v1) | 2026-06-02 | depthwise读出、标量记账replay与真实输入干预区分；2+1+2=5 | 标准完成 | 仅报告：tail稳定操作定义及干预资格未闭；R178通过，见§4 |
| [Accuracy, Stability, and Repeated-Run Reliability of Large Language Models on Deterministic Programming Tasks](https://arxiv.org/html/2606.00920v1) | 2026-06-02 | 同题run均值与全R通过分母，中心PSR数字不相容隔离；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R178具体正文比较，见§4 |
| [Training Prompt Matters: State-Adaptive Optimization for Robust Fine-Tuning](https://arxiv.org/html/2606.01967v1) | 2026-06-02 | 同task当前checkpoint target CE选择并固定训练指令；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)；R180/R184，见§4 |
| [HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity](https://arxiv.org/html/2606.00271v1) | 2026-06-02 | arrival人口权重与stale方向的独立校正；2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；R180，见§4 |
| [GPTQ-intrinsic LoRA: A Near-optimal Algorithm for Low-precision Quantization with Low-rank Adaptation](https://arxiv.org/html/2606.01412v1) | 2026-06-02 | 同GPTQ sweep全精度吸收坐标与fixed-grid交替条件；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；R180/R184，见§4 |
| [Finer Parameter Steps for Low-Rank PEFT: A Controlled Study with CP Tensor Adapters](https://arxiv.org/html/2606.00428v1) | 2026-06-02 | CP预算grid步长与受限方向表达能力分账；2+1+2=5 | 深入完成 | 整合：`TRAIN-LORA`，[Ch30](../../../../books/part-04-training-system/30-lora.md)；R180/R184，见§4 |
| [DSL-LLaDA: Scaling Continuous Denoising to 8B Masked Diffusion LMs](https://arxiv.org/html/2606.01024v1) | 2026-06-02 | 已有MDLM到Gaussian embedding/converter的续训桥；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R181/R184，见§4 |
| [Revise, Don’t Freeze: Sampler-Matched Training for Self-Correcting Masked Diffusion Language Models](https://arxiv.org/html/2606.01026v1) | 2026-06-02 | clean-slate候选重选与selfcommit错误人口监督配对；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R181/R184，见§4 |
| [WaveFilter: Enhancing the Long-Context Capability of Diffusion LLMs via Wavelet-Guided KV Cache Filtering](https://arxiv.org/html/2606.00724v1) | 2026-06-02 | 当前query由多尺度旧prompt K粗选后读原KV细筛；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R181/R184，见§4 |
| [EPIC: Efficient and Parallel Inference under CFG Constraints for Diffusion Language Models](https://arxiv.org/html/2606.00722v1) | 2026-06-02 | CFG超集只预筛候选batch，exact witness仍批准提交；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R182/R186，见§4 |
| [FLARE: Diffusion for Hybrid Language Model](https://arxiv.org/html/2606.01774v1) | 2026-06-02 | visibility落实为recurrent boundary/reset与分mode commit；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R182/R186，见§4 |
| [SimSD: Simple Speculative Decoding in Diffusion Language Models](https://arxiv.org/html/2606.02544v1) | 2026-06-02 | SimSD temporal-causal data/prediction布局与非lossless边界；2+2+2=6 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；R182，见§4 |
| [BlockGen: Flexible Blockwise Sequence Modeling with Hybrid Samplers](https://arxiv.org/html/2606.02241v1) | 2026-06-02 | mixed-block训练与额外AR评分corrector改变corruption排名；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R182/R186，见§4 |
| [Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving](https://arxiv.org/html/2606.01839v1) | 2026-06-02 | 首prefill相位、两观测量与一次KV交接的放置分工；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；R183/R186/R187，见§4 |
| [Leyline: KV Cache Directives for Agentic Inference](https://arxiv.org/html/2606.01065v1) | 2026-06-02 | amortize保旧hidden影响与forget重prefill两合同；2+2+2=6 | 标准完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；R183，见§4 |
| [Idleness is Relative: Exploiting Tool-Call Idle Windows for Offloading in Agentic Systems with MORI](https://arxiv.org/html/2606.00866v1) | 2026-06-02 | 剔除gating自造等待与GPU/CPU反向保留标签；2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；R183/R187，见§4 |
| [CHIMERA: A Flexible and Scalable 3.1 TOPS/W AI-MCU with Transformer Accelerator and 563 Gb/s Shared-L2 Memory Subsystem with QoS Guarantees](https://arxiv.org/html/2606.02358v1) | 2026-06-02 | 同shared L2 bank交错与窄control/宽bulk联合仲裁；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；R185/R188，见§4 |
| [Inner Product Aware Quantization: Provably Fast, Accurate, and Adaptive Algorithms](https://arxiv.org/html/2606.00289v1) | 2026-06-02 | 独立无偏舍入类中worst单位方向与分布平均两码本目标；2+1+3=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；R185/R188，见§4 |
| [Cram: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning](https://arxiv.org/html/2606.02502v1) | 2026-06-02 | warmup增量谱与历史A子空间筛rank，独立校centroid竞争；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA`，[Ch30](../../../../books/part-04-training-system/30-lora.md)；R189/R190，见§4 |
| [ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning](https://arxiv.org/html/2606.02576v1) | 2026-06-02 | 训练target格式teacher与部署输入预测码分别校准；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA`，[Ch30](../../../../books/part-04-training-system/30-lora.md)；R189/R190，见§4 |
| [Regular-Activation Concentration: Characterizing Column-Level Output Sparsity Across Diffusion Model Architectures](https://arxiv.org/html/2606.00567v1) | 2026-06-02 | 跨M token列OR粒度、denoise hotset与τ/r两校准量的布局资格；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；R191准入/日证、R192必要/收窄及R193唯一实际POST，见§4 |


## 4. 证据与知识整合

### [Kimi Code 0.7.0 / 0.8.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.7.0)

官方release API `published_at` 分别2026-06-02T02:23:53Z与2026-06-02T14:56:13Z，两核心release及PR319/336/277/270/315必要实现/说明实际读，详见[精确packet](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md#kimi-code-070--080发布正确性差额待非作者有限核)。PR319把独立tool store的TODO确定性附在compaction summary before history write，不能证明其他摘要忠实或任务完成。PR336 PermissionRequest/Result仅真实approval RPC成对异步通知，return ignored，不是authorization gate。PR277撤销real-user-prompt suffix并同步修剪replay、保injection/不穿compaction_summary；达到边界超额undo可先删suffix再throw，非全无修改；测试只支持受控context/replay一致，不是worldeffect undo。PR270 persisted active/paused/blocked、complete transient announce-clear，restart active→paused需resume；模型markComplete没有独立执行completionCriterion验证，完成消息/statistics非成功证明。

发布正确性差额按研究合同深入受影响部分；未读/未采用无关release项，也没有运行厂商测试或宣称复现。当前实际[AGENT-WORKFLOW Ch81](../../../../books/part-07-agent/81-workflow.md)“Context与Environment必须在同一恢复点对齐”约579–615及“Resume语义”约1142–1148已承载context/environment/effectledger与durable state分账；[AGENT-CONTEXT Ch75](../../../../books/part-07-agent/75-context.md)约282–300已有control-state最低fidelity与原文authority。它们支持长期边界，但不使特定新接口变成旧正文已有实现。因此最终处置仅报告，非作者必要证据与实际owner定点核通过，不另写版本手册段或新的Books。

### [Codex roles / ChatGPT Sites](https://openai.com/index/codex-for-every-role-tool-workflow)

官方RSS `pubDate`分别2026-06-02T09:00:00Z与[Academy](https://openai.com/academy/chatgpt-sites)10:00:00Z。原文核心：role plugins捆apps/skills/instructions/workflows；annotations把artifact局部选中span带入context；Sites生成/预览→review→deploy/shareURL，admin与connected app权限继续独立。Academy说当时不能直接连接live data，另automation gather更新后reviewrefresh/redeploy；没有承诺生成、保存、部署、共享、刷新自动成为一个成功事务。具体可改变选择：静态发布产物需要显式freshness/republication路径，不能把一次创建当作持续最新资料。

采用限发布接口/边界，无运行实现、matched comparison、heldout或端到端质量成本证据；评分只给这一局部机制，不给成熟approval原则或机构声望。当前[PLATFORM-PRODUCTION Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)与Ch81负责review/release与状态交付，公告未形成必须新增的长期机制，仅报告处置已通过有限非作者准入/证据核。10/01额外读当前Learn Sites save/deploy说明用于避免现在功能倒填6月，**当前文档不是历史发布证据**，不将其viewer connector、APIkey等新细节用于本窗判断。

### 机构事件的贡献前关闭与风险边界

[Codex productivity](https://openai.com/index/codex-for-knowledge-work)RSS06/02 02Z：知识工作者用户群增长速度超过开发者用户群3倍，非任务效率提升；采用数据没有新的评价协议或机制；[Youth leadership](https://openai.com/index/advancing-youth-safety-and-opportunity-through-global-leadership)07Z：9原则是政策提案，旧ageprediction/parentalcontrols回顾，不当作新部署；[Travelers](https://openai.com/index/travelers)12Z：Realtime应用85–90%completion缺cohort/denom/CI/E2E与新架构，不因应用成功数字准入。[Meta SA-3DAO](https://ai.meta.com/datasets/sa-3dao-sam-3d-artist-objects/)沿用2025 benchmark的100公开/900heldout，无新evaluation盲区/protocol。四项读核心后pre-denominator关闭，具体证据边界保留，不把日期未核明的SA再追时刻。四项有限negative校准已由apr29_close通过。

原旧raw所列2606.24369当前原站v2 withdrawn、v3重新提交，并非全家族永远撤回；v1=06/23且v3=09/22，都窗外，只纠正材料身份，不评分/不采用任何版本、不扩另一日。87 DateHold不是证据失败；其已有方法/反证留在[旧必要笔记](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md#旧readme必要证据留存非本轮87-evidencebooks验收)，没有在本轮声称逐篇全文已读。


### 本次增量证据的适用范围

以上连续原块为旧小时窗口的有效证据，其“无新Books”只属于旧轮；以下为本次Jun02补查实际新增，后续版本与旧DateHold标签不替当前原证。

### [Schedule-Level Shared-Prefix Reuse for LLM RL Training](https://arxiv.org/html/2606.01143v1)

精确v1采用范围：schedule级prefix VJP复用与逻辑token计数。原分3+3+2=8，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_MODEL_20261023.md)，独立必要原证/owner与实际采用见[独核R1/R7](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。已按逐字最小拟稿融入[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)的相关论证，非writer实际完整新增/直接两侧/本人注写后通过；反退/成本与旧路回退近文。未核代码或复现，未将当前版本的新实验替代v1。

### [SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving](https://arxiv.org/html/2606.01751v1)

精确v1采用范围：Sparse-Q跨层修正与命中physical copy费用。原分2+2+2=6，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_MODEL_20261023.md)，独立必要原证/owner与实际采用见[独核R3/R7](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。已按逐字最小拟稿融入[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)的相关论证，非writer实际完整新增/直接两侧/本人注写后通过；反退/成本与旧路回退近文。未核代码或复现，未将当前版本的新实验替代v1。

### [Confidence-Adaptive SwiGLU for Mixture-of-Experts](https://arxiv.org/html/2606.00761v1)

精确v1采用范围：router affinity参与expert内部激活与真实吞吐取舍。原分2+1+2=5，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_MODEL_20261023.md)，独立必要原证/owner与实际采用见[独核R4/R7](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。已按逐字最小拟稿融入[Ch21](../../../../books/part-02-model/21-moe.md)的相关论证，非writer实际完整新增/直接两侧/本人注写后通过；反退/成本与旧路回退近文。未核代码或复现，未将当前版本的新实验替代v1。

### [A Pre-Training Analogue of Grokking in Language Models: Tracing Delayed Grammatical Generalization](https://arxiv.org/html/2606.00230v1)

精确v1采用范围：关键短语曝光代理/选择条件下延迟语法泛化。原分2+1+2=5，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_MODEL_20261023.md)，独立必要原证/owner与实际采用见[独核R5/R10](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。已按逐字最小拟稿融入[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)的相关论证，非writer实际完整新增/直接两侧/本人注写后通过；反退/成本与旧路回退近文。未核代码或复现，未将当前版本的新实验替代v1。

### [Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools](https://arxiv.org/html/2606.02483v1)

精确v1采用范围：issue-time逐observer披露、三假设与弱labeler边界。原分3+2+3=8，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_AGENT_MULTI_20261023.md)，独立必要原证/owner与实际采用见[独核R2/R7](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。已按逐字最小拟稿融入[Ch78](../../../../books/part-07-agent/78-tool-calling.md)的相关论证，非writer实际完整新增/直接两侧/本人注写后通过；反退/成本与旧路回退近文。未核代码或复现，未将当前版本的新实验替代v1。

### [Retrieve What's Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation](https://arxiv.org/html/2606.02479v1)

精确v1采用范围：target-pixel残余覆盖的联合选择，不授depth单独必胜。原分2+2+2=6，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_AGENT_MULTI_20261023.md)，独立必要原证/owner与实际采用见[独核R6/R10](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。已按逐字最小拟稿融入[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)的相关论证，非writer实际完整新增/直接两侧/本人注写后通过；反退/成本与旧路回退近文。未核代码或复现，未将当前版本的新实验替代v1。

### [Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains](https://arxiv.org/html/2606.02357v1)

精确v1采用范围：tool trace与answer-critical信息贡献分责。原分3+2+2=7，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_AGENT_MULTI_20261023.md)，独立必要原证/owner与实际采用见[独核R8](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。Ch78 no-tool/call-shell/result及非严格因果/额外成本正文已具体覆盖；OOD与训练不匹配/小样本留作本报告边界，不再添段。未核代码或复现，未将当前版本的新实验替代v1。

### [Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution](https://arxiv.org/html/2606.01435v1)

精确v1采用范围：候选抽取与确定性版本策略分责，whole-pipeline非resolver因果。原分3+2+2=7，具体长期差额深入；必要方法、关键对照与反侧、实际owner及完整拟稿见[作者记录](../_sources/daily-20260603/SUP_AGENT_MULTI_20261023.md)，独立必要原证/owner与实际采用见[独核R9/R11](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)。已按逐字最小拟稿融入[Ch77](../../../../books/part-07-agent/77-memory.md)的相关论证，非writer实际完整新增/直接两侧/本人注写后通过；反退/成本与旧路回退近文。未核代码或复现，未将当前版本的新实验替代v1。

### [SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision](https://arxiv.org/html/2606.01139v1)

精确v1 §3/式1–9、§4/T1、§5.1–5.3/T2–4及Limitations/A.C–E必要域支持：先证执行失败属于skill缺陷再准修改，保存已过行为，以证据/迁移条件绑定原则及可检查动作锚；搜索沿新候选前进与最终返回best-observed是不同状态。5分按实际Ch77更新接口差额深入，并未因处置上调评分。T4自由修订52/86接近完整53/86，不证明结构化普遍更强；不同任务分母、source-success条件迁移、可见verifier过拟合和额外candidate执行费用均保留。原实现无no-skill fallback，“保旧skill”不等至少胜无skill。日期/准入复用独立R13的有效Jun02组合依据，不用后版本补v1。

已融入唯一`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)的Ctx2Skill历史回选完整段后、Memory policy前，补本地修订资格与search/return分责，不重述已有跨版本probe选择或授执行权。[必要证据及完整差额](../_sources/daily-20260603/SUP_SKILLREVISE_20261024.md)经[本轮独核R2/R4](../_sources/daily-20260603/SUP_CHECKPOINT_REVIEW_20261024.md)确认；实际新增/完整两侧/本人源注真实POST通过，未核实现或复现实验。

### [TVIR: Building Deep Research Agents Towards Text–Visual Interleaved Report Generation](https://arxiv.org/html/2606.02320v1)

精确v1 §3.4/4/5.1/5.3–5.5与B/C/D必要域支持将figure、caption、周边论证与source分项验收，而不由文字流畅或URL存在代签。6分按具体测量差额加深。CSC是矛盾计数传感器，零矛盾不证明支持完整；Appendix C的IA/MC消费清除失效路径、由judge修订caption后的文字视图，不能把修订后分数授给原产物。有限抽取/人类对齐、system均分相关与逐图真值分开，D.2三次是evaluation而非已确认生成重跑；预算挤占为作者解释，未采榜差因果或完整Agent可靠性。日期/准入同样复用R13，不比较后版本。

实际比较Ch81既有chart-first writer顺序与Ch66 claim-level契约后，唯一owner定为`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，而非继承初筛临时workflow路由。在claim-level provenance尾段后、Raw Score到Claim Sensor前新增视觉绑定/原件与测量视图分责，保judge/来源失败及全计费。[必要证据/PRE](../_sources/daily-20260603/SUP_TVIR_20261024.md)经[独核R3/R4](../_sources/daily-20260603/SUP_CHECKPOINT_REVIEW_20261024.md)及实际完整新增/直接两侧/本人注POST通过；未核全部prompt、图像素、代码或复现，不授事实或部署安全。

### [Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate](https://arxiv.org/html/2606.00820v1)

精确v1 §3–6把无同伴自反思、只见立场、见完整推理分开，在SR-stable population中作操作归因，不声称读出内在心理过程。GPT-4o五agent、MMLU-Pro受限设置中，个体变化不等最终多数票改善；无标签减少peer adoption也未增accuracy，reasoning条件另改变文字长度与格式。3+2+2=7，设计反证必要深入；控制分组、全对话/重跑/聚合费用与无label部署资格均保留。已融入Ch82 Peer/Debate的原多agent候选段后、同题独立采样前，解释“改答”并非从众同义词；未核实现或复现。

必要证据及完整采用边界见[Agent batch2记录](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)，[独立复核R5–8](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)确认日期/准入/Source、实际owner及完整真实写后。未变化的先前成果不重审，不据本批通过授完整DAY。

### [CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems](https://arxiv.org/html/2606.00756v1)

精确v1 §3.2–3.4、§4.1–4.3/T1–2、§5支持以semantic subgoal聚组、critic派生与异步分发，而非参数同步。Mistral7B/RTX4090与deepseek-chat critic等有限文本任务；cloud context大于local的混杂、Gripper/Jericho零或负结果及68.68s云均延迟保留，不签低延迟SLO。2+2+2=6，标准必要证据完成。Ch77“Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权”的完整正文已承载local raw authority、派生guidance、dispatch receipt、stale风险与local-only fallback，故不为收益数字改书；其中tenant/TTL等是本项目设计要求，不冒论文已实现。

必要证据及完整采用边界见[Agent batch2记录](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)，[独立复核R5–8](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)确认日期/准入/Source、实际owner的具体已有覆盖。未变化的先前成果不重审，不据本批通过授完整DAY。

### [Enhancing LLM Metacognition via Cognitive Pairwise Training](https://arxiv.org/html/2606.00869v1)

精确v1 §3–5/T1–3及§5.3、§4.4支持普通NTP学习problem/reference/two-trace到四类相对标签，再在无reference生成中验迁移，不是DPO，也不证明内部事实verifier。2+1+2=5，针对实际知识缺口深入：SUM较高F1与过拒、3B/4B及32B未RL反侧、teacher/rollout/token预算差异保留，摘要与正文不齐headline未采用。已融入Ch29恢复监督的single-trace yes/no段后、少量高质量数据节前，区分外部比较资格与内部生成校准；未复现。

必要证据及完整采用边界见[MODEL R3记录](../_sources/daily-20260603/SUP_MODEL_R3_RESUME_20261024.md)，[独立复核R5–8](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)确认日期/准入/Source、实际owner及完整真实写后。未变化的先前成果不重审，不据本批通过授完整DAY。

### [Towards Lightweight Reliability: Using Soft Prompts for Hallucination Mitigation in Large Language Models](https://arxiv.org/html/2606.00919v1)

精确v1 §4/Eq1–4、§6/T2–4、§7及A.0.A/T5支持冻结基座、输入soft prompt的abstain/fact CE、负hallucination CE与KL，以及μ的时间schedule。2+1+2=5，按Ch29具体缺口深入；单Gemma12B/TruthfulQA配置、固定μ与多seed未齐，不作普遍最优归因。Llama部分域反退、judge与输出截断条件保留；KL不认证能力无损，冻结仍需反传。已在Ch29 Concept Tokens后、离散chunk-code前融入“更新哪些参数”和“沿什么监督路径更新”分责；未核代码或复现。

必要证据及完整采用边界见[MODEL R3记录](../_sources/daily-20260603/SUP_MODEL_R3_RESUME_20261024.md)，[独立复核R5–8](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)确认日期/准入/Source、实际owner及完整真实写后。未变化的先前成果不重审，不据本批通过授完整DAY。

### [Learning to Retrieve: Dual-Level Long-Term Memory for Text-to-SQL Agents](https://arxiv.org/html/2606.00547v1)

精确v1 §5.1–5.3、§6/T1–5与Limitations支持按episode结果和turn局部teacher-PRM分别训练选择器，不把PRM标签一致率当真实因果效用。2+1+2=5，实际Ch77信用接口缺口深入；无RL第一层接近、去episode少token却伤success、Spider2迁移仍可增加turn，限制双层RL必需性。GPT5/GPT4o模拟用户、BIRD去重增强与teacher共同偏差、训练/检索/额外prefill费用保留；硬件、精度、并发及统一SLO未披露，不复现。已在Ch77 proxy identity完整段后、terminal utility前融入双时域选择，事实与行动授权不交给utility。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R9–10/R12](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)确认Source、唯一owner与完整实际新增/直接两侧/本人注写后通过；这不是日级候选冻结或完整DAY。

### [Adversarial Feeds Steer LLM Agent Decisions Against Their Defaults](https://arxiv.org/pdf/2606.00914v1)

精确v1 PDF §3–6（持久原件首页June2）支持固定模型/persona/最终问题，只干预此前feed构成/顺序后测forced-choice。相同版本HTML URL自标Aug24且题摘总数有差异，不声称格式历史逐字一致、不采用2785总量。3+2+2=7，设计反证深入：Qwen null、Gemma平衡/披露未恢复、generator swap同时换内容池、建议非实际动作、run分组probe与全部暴露/防御费用保留。已融入Ch75最终答案分账段后、抽取视图代理段前，补上游选择器审计；不从逐帖无显式恶意推出任意filter失效或全链安全。未复现实验。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R9–10/R12](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)确认Source、唯一owner与完整实际新增/直接两侧/本人注写后通过；这不是日级候选冻结或完整DAY。

### [Discovering Agents for Discovery: The Case for DNS](https://arxiv.org/html/2606.02314v1)

精确v1 §3–5提供metadata条件字节预算，而非部署benchmark。2+2+1=5，针对Ch83跨组织发现差额深入；API endpoint与静态MCP名称为proxy，只有21.7%条目可解析tool，独立P90相乘不是联合分位或上界。部分签名/证书字段不等完整wire、chain或后续registry费用，未实测发现时延、可靠性、安全或业务授权。已在Ch83 selective discovery全量fallback后、Tool Description前融入名字解析之后的依赖；协议/格式改变须重算，保显式registry/HTTPS与批准端点回退，未核实现或复现。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R9–10/R12](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)确认Source、唯一owner与完整实际新增/直接两侧/本人注写后通过；这不是日级候选冻结或完整DAY。

### [ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use](https://arxiv.org/html/2606.00341v1)

精确v1 §3–6必要域把82个受控computer-use任务中的task success、违规意图与真实违规分开；截图/a11y、API reasoning配置、VM与人工抽查条件见原件。3+2+2=7，普通任务控制反证深入；子代理只接subtask未继承原约束、部分restricted场景无法测success，不能外推任意部署违规率或能力因果。已在Ch81 durable control-plane核心判断后融入无攻击场景控制边界，派发/effect强制与显式约束传播为本项目设计要求，不称三种prompt mitigation已实现可靠防御。全部子轨迹/VM/审计成本保留，未复现。

[必要证据/完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R11/R14](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核Source、actual owner及实际完整新增/直接两侧/本人注写后通过；不是完整DAY。

### [AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents](https://arxiv.org/html/2606.02461v1)

精确v1 §3–5/式1–3/T2–4及Limitations将可读写第一遍F、无memory B、冻结后同题第二遍S及独立H分开。2+2+2=6，实际评价缺口深入；SG=S−F还含当前题写入、后续维护与检索，不是纯遗忘率，同题重读不能认证泛化。controlled人为复用结构、naive及heldout反退、三run与判分限制保留。已在Ch77评估Memory标题后、Neuromem前融入任务流与读出资格，而非只增加benchmark名称；所有两遍/维护/holdout计费，未运行。

[必要证据/完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R11/R14](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核Source、actual owner及实际完整新增/直接两侧/本人注写后通过；不是完整DAY。

### [SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems](https://arxiv.org/html/2606.01314v1)

精确v1 §2–4、D.3–6/E必要域支持把tool变化与依赖skill作为共同候选，unit→integration→原强项回归，并留失败signature与retirement理由。2+2+2=6，Ch77跨依赖修订接口缺口深入；共激活/语义veto是搜索启发非因果或安全证明，FreeTool异常增、完整法仍有2.1%回归、人工no-op损坏及同源judge限制保留。已在Ch77 COSPLAY后、policy与bank联动维护前融入bundle验收，不覆盖已有SkillRevise局部修订资格。全候选/失败重提/回归/存档费用保留，未核代码或复现。

[必要证据/完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R11/R14](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核Source、actual owner及实际完整新增/直接两侧/本人注写后通过；不是完整DAY。

### [ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment](https://arxiv.org/html/2606.00644v1)

精确v1 §3–5及人工/系统适配域，以500个AI研究判断任务冻结cutoff语料、关闭web，未来材料只用于验证，并分报Fact、FTA、Trace及Pers代理。2+2+2=6，实际测量缺口深入；声明模型cutoff不证明参数无未来污染，taxonomy/human–LLM构造target不等唯一真实研究路线，八专家检查不是现实未来决策验证。高Trace可伴粒度、因果角色、干预或时间尺度偏移，相关性不当因果。唯一owner从初筛RAG校正为Ch66评价，在Paper-to-code后、frontier lag前融入时间隔离与决策对象分验；全KB/任务/agent/judge/人审费用保留，未复现，不扩AI for Science。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R13/R15–16](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核必要Source、actual owner和实际完整新增/直接两侧/本人注写后通过；不授完整DAY。

### [FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification for Agentic Search](https://arxiv.org/html/2606.00660v1)

精确v1 §2–4/T1–3为每个候选使用相同显式subchecks，将contradicted/not_found/supported映射为0/0/1后聚合/早停。2+1+2=5，Ch80比较规则缺口深入；分解可能漏要求，最高分不等真值。四轨迹并不等验证token/web预算，Gemini平均与aggregation近持平、局部最优及手审仅判分样本均保留，不把cache/早停泛化成更便宜。已在Ch80 traceback反馈段后、blind checker前融入共同清单与缺证处理；全部检索/验证/judge与失败重查计费，未复现。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R13/R15–16](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核必要Source、actual owner和实际完整新增/直接两侧/本人注写后通过；不授完整DAY。

### [Skill or Skip? Learning Selective Skill Invocation in Agentic Tasks via Dual-Granularity Preference Learning](https://arxiv.org/html/2606.00510v1)

精确v1 §3–5.4从同一prefix强制invoke/skip，成功优先、双成功按环境步数、双失败丢弃，再合episode及local偏好训练。2+2+2=6，实际调用接口缺口深入；entropy是分支heuristic不是必要性概率，续采样/过滤不签无偏因果。ALFWorld Qwen3 4/8B、BFCL14B，后者改善伴更多调用，不能写少调用总更好；invoked人口precision与总体success分开，steps非总费用。已在Ch78 Toolformer/ReAct能力路径后、Tool Contract前融入调用分责；库/双续跑/训练/注入全计费，未核实现或复现。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R13/R15–16](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核必要Source、actual owner和实际完整新增/直接两侧/本人注写后通过；不授完整DAY。

### [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/html/2606.02388v1)

精确v1 §2–4.7/Alg1/T1–4、§7及A.1支持同policy轨迹的动作reward与next-observation辅助监督：因果attention阻止action位置forward看未来，但辅助loss仍更新共享参数，不是stop-gradient。2+2+2=6，Ch25训练-only消费缺口深入；qlogq不是完整词表熵，reward归一不自动适用于负奖励域。Qwen2.5受限文本环境/searchQA、三seed，直接CE可低于原RL，GIGPO子任务可退步；1.5B ALFWorld局部step/显存profile非通用零开销。已在Ch25 action schema后、AIM前融入训练辅助分支，与上线worldmodel调用区别；一步/重复轨迹限制及全训练/真实transition费用保留，未核实现或复现。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R13/R15–16](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核必要Source、actual owner和实际完整新增/直接两侧/本人注写后通过；不授完整DAY。

### [COMAP: Co-Evolving World Models and Agent Policies for LLM Agents](https://arxiv.org/html/2606.02372v1)

精确v1 §3.1–3.3/式1–8、§4.1–4.4及C.2–3支持draft→student future→修订→action gate→真实执行；训练必须绑定真正执行的动作，不用被拒draft配真实后果。EMA teacher能读真实future仅是训练特权，上线无teacher/future，保draft不授真实安全。2+2+2=6，Ch25共同更新接口缺口深入；专家warm-up、canonicalized变化F1非full state及同源feedback反侧保留。Qwen3 4/8B、4×A10080GB/LoRA r8，37.68GPUh仅8B AW局部成本，不等全域同费用。已在Ch25演进说明后、symbolic branch前融入，与PaW是替代消费分支而非直接谱系；未核实现或复现。

[必要证据及完整差额](../_sources/daily-20260603/SUP_AGENT_B2_RESUME_20261024.md)经[独核R13/R15–16](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)核必要Source、actual owner和实际完整新增/直接两侧/本人注写后通过；不授完整DAY。

### [Beyond Visual Memory: Mechanistic Diagnostics of Latent Visual Reasoning](https://arxiv.org/html/2606.01287v1)

slot干预、marker-only和跨样本交换分验；保Monet-RL例外、RL数据未全匹配、小分母与attention非因果，不由提分认证视觉记忆。Ch23 Connector shortcut后、视频反事实前新增受限诊断。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分3+2+2=7，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces](https://arxiv.org/html/2606.01317v1)

exact-v1 §4–5/T3的716 sandbox任务/13模型；HSR排除incapable且含recommendation，不是全人口真实damage。Ch81将持久workspace与有用完成分验。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Same Payload, Different Channel: Measuring Trust Asymmetry in Tool-Using Language Models](https://arxiv.org/html/2606.00566v1)

exact-v1 §3–8的98英语静态cases/6模型；同payload但chat无tool、trigger及judge不同，不能当纯渠道因果或普遍检测配方。Ch78按实际渠道和成功条件分验。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分3+2+2=7，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary](https://arxiv.org/html/2606.00376v1)

exact-v1 §3–6/B3–B6的有限attention/decorrelation假设、survival上界与实际最大深度不等价；hazard-horizon到state capacity及baseline索引桥未证明。中心主张争议，未进入Books；需精确版本补齐状态人口/分布/精度/通信与训练差异证明，或可核纠正版本明确撤除一般上限。 暂缓，不写Books；精确重开条件见本段。评分3+2+2=7，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations](https://arxiv.org/html/2606.02240v1)

exact-v1 §3–5/Limitations；69.9→2.4为固定trace any-step旗标而非在线阻断、重执行或任务完成；预筛与分母矛盾保留。Ch78新增检测人口/干预效用分界。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence](https://arxiv.org/html/2606.02380v1)

exact-v1 §3–4的300选择任务、mock工具、Pass5与有效人口；judge82.5并非自然失效率或主观intent证据。Ch81新增报告与执行分验。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability](https://arxiv.org/html/2606.01365v1)

exact-v1 III–VIII/TI–II：165 GAIA、8步/8调用/30s/25K软限；10/30选择审计、warning后可恢复，相似度proxy不证明在线干预节费。Ch69进展信号与干预效用分责。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Reducing Token Usage of State-in-Context Agents using Minification](https://arxiv.org/html/2606.01326v1)

exact-v1 §3–4/T1–4与dedent分析；代理token90535→52776但质量50→38，fullrun未含dedent，局部分母冲突/不同tokenizer限制保留。Ch75压缩目标后新增consumer及patch格式边界。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL](https://arxiv.org/html/2606.01619v1)

exact-v1 §3–4.3/T1–2/A，版本对照、discounted Thompson/reservoir与自动接纳；不同policy不直接合历史胜率，autoaccept可损害，不采用科学领域应用主张。Ch77有无skill组之后补版本收益。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [When Hard Negatives Hurt: Bridging the Generative-Discriminative Gap in Hard Negative Synthesis for Retrieval](https://arxiv.org/html/2606.01304v1)

exact-v1 §2–4/Alg1，来源诊断与entropy/mass balance辅助，query/mined只在辅助域detach；不授互信息归零或retrieval真值。Ch76表示首段后补负例构造边界。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning](https://arxiv.org/html/2606.02132v1)

exact-v1 §3–4/T1–3；组内对照与token重权不等授权，局部调用可增，少调用不等质量。Ch78 necessity论证中新增训练效用边界。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_AGENT_B3_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression](https://arxiv.org/html/2606.02559v1)

exact-v1 §3–5/T1–7/D；mask排序不等替换后质量，Qwen instruct反退，bypass有额外参数/MAC，不是等净压缩或无损。Ch17冗余论证中新增子模块替换条件。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [ResMerge: Residual-based Spectral Merging of Large Language Models](https://arxiv.org/html/2606.02252v1)

exact-v1 §4–5/Eq6–16；naive residual-only弱于head、ungated反退，微小均分差无重复CI，几何不是功能真值。Ch30多个Adapter相加处新增完整矩阵分工。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [An Algebraic View of the Expressivity of Recurrent Language Models](https://arxiv.org/html/2606.01765v1)

exact-v1 §4/AppendixJ必要构造；固定求值非负float与uint wraparound条件分开，负数及非2幂分支另有限制，存在性不证明训练可达。Ch22状态表达边界保旧合理条件。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分3+1+3=7，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [A Finite-Calibration Regime Map for LLM Judge Panels](https://arxiv.org/html/2606.01034v1)

exact-v1 §3–5/A；scalar偏差与交互表方差/未见cell回退分责，support entropy不是风险界，选择/校准/验证/test隔离。Ch66 checker-set费用后补校准人口。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [On the Generalization Gap in Self-Evolving Language Model Reasoning](https://arxiv.org/html/2606.01075v1)

exact-v1 §2–6/T1–4，4B仍受oracle改善、12B接近oracle但不授一般ceiling；完整生成/验证费用计入。Ch34 multi-round lineage中融入标签来源分验。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [ProjQ: Project-and-Quantize for Adapter-Aware LLM Compression](https://arxiv.org/html/2606.00494v1)

exact-v1 §3–6/Eq8–16；只在abundant-rank等假设下给separable上界，不证明严格plasticity或任意迭代更好；局部反退与全费保留。Ch30 QLoRA处补误差子空间。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning](https://arxiv.org/html/2606.00395v1)

exact-v1 §3–5/Eq1–8/T1–2；rollout固定路由、训练重放索引，bounded soft-route稳定界非hard top-k无偏PPO或完整prefix/KV一致。Ch32 rho身份后新增条件边界。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Massive Spikes in LLMs are Bias Vectors: Mechanistic Uncovering and Spike-Free Quantization](https://arxiv.org/html/2606.02288v1)

exact-v1 §3–5/T1–2，clamp/templates与terminal residual；原精度和低bit都有反退，RoPE稳定近似，PPL正文印误不作收益。Ch49量化分布诊断开头融入功能保持资格。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Geometric Latent Reasoning Induces Shorter Generations in LLMs](https://arxiv.org/html/2606.02248v1)

exact-v1 §3–4，answerCE与transitionMSE，K+text计步骤；大K漂移、大预算CoT反超，successful-only与异decoder不签wallclock或faithfulness。Ch18 latent费用后补连续输入接口。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Extreme Low-Bit Inference in Reasoning Models: Failure Modes and Targeted Recovery](https://arxiv.org/html/2606.02011v1)

exact-v1 §3–8/T1–5/A：Qwen/GPTQ W2/W4受模型任务、cap与解析条件限制；TTFA是token位置、tokens/s乘轨迹估算非服务实测。Ch49已有“Reasoning Quantization要验收Commitment”完整两段及同family marker，实际拥有precision×预算×parser、first-answer/commit gap、loop/hitlimit、phase fallback/plan与双路径费用；独核撤回重复新增PRE，保持7分深入，不造diff。 具体已有覆盖，不重复写入。评分3+2+2=7，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads](https://arxiv.org/html/2606.01927v1)

exact-v1 §4–9/T1，iteration长度、早反馈、padding/回收及RNG消费；8×H100/A100、FP16、PPoff、batch32，TTFT基本不变，完整生产SLO未齐。Ch42旧alias承载通用host瓶颈，Ch50仅补实现差额并链接该owner，不另复写主解释。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Resonant Context Anchoring: Decoupling Attention Routing and Signal Gain at Inference Time](https://arxiv.org/html/2606.01923v1)

exact-v1 §3–5/Eq1–8/T1–3；gain不能静态折KV，SNR近似要求对齐/近常量噪声，NQSwap反事实context不是世界真值，70B ROUGE-L与较大gain反退。Ch14 routing不等贡献后新增信号幅度分支，不授消除幻觉。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_MODEL_B4_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Move the Query, Not the Cache: Characterizing Cross-Instance Latent and Sparse Attention Redistribution Across GPU Fabrics](https://arxiv.org/html/2606.01502v1)

exact-v1 §2.1–2.3/§3–4/§5.1–5.4/Fig4；MLA/稀疏粒度，host小batch反侧、holder容量/位置与语义fetch资格。H100/NDR200微基准非全模型/SLO，未采通用倍率。Ch52 Hetis完整组后新增块级执行选择。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+2+2=6，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_INFRA_NEXT_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [ScanWeaver: Compiler-Driven Parallelization of Affine Recurrences via Associative Scan Lowering](https://arxiv.org/html/2606.00601v1)

exact-v1 §3–6/§9，Blelloch lowering不是新scan数学；浮点重排、稳态排编译加载、完整Mamba融合不是matchedkernel、无全reset/backward/分布式。Ch49 attention monoid费用后补编译兼容子集并链接Ch22。 必要机制已实际融入上述owner正文并通过唯一非writer实际POST。评分2+1+2=5，完整题摘、联合日期、实际必要Source及反证见[本项原始记录](../_sources/daily-20260603/SUP_INFRA_NEXT_20261024.md)；准入/owner及实际保存独核见[独核R1–20](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。未核代码、未复现实验，不授生产保证。

### [Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction](https://arxiv.org/html/2606.01850v1)

actual Ch66“Compression Release必须同时验收Accuracy与Calibrated Uncertainty”完整首两段及同family alias SF-COMPRESSION-UNCERTAINTY，已具体拥有同样本accuracy/coverage/set size、calibration failure、artifact/score/target、交换性/shift及回退，旧06-02归属不搬。exact-v1 §3.1/§4/§5必要域的退化SS1/CR约12只是评价失败，不认证小集合可靠或一般安全位宽。独核R23具体NC通过，撤回Ch49新增PRE。 完整题摘/联合日证见[B5](../_sources/daily-20260603/SUP_MODEL_B5_20261024.md)，实际必要范围及原未采用提案见[本项原证记录](../_sources/daily-20260603/SUP_MODEL_B5_TWO_SOURCE_20261024.md)，最终采用见[独核R22–28](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。当前官方abs所见无withdrawn/removed/erratum，只是该页有限notice核，非全网保证；未核代码或复现。

### [ProbeScale: Probing Analysis to Optimize Neural Scaling Laws for Efficient Small Language Model Inference](https://arxiv.org/html/2606.01806v1)

exact-v1 §3只是任务probe成绩加权、预算内contiguous block枚举与可选task finetune，scaling laws是初始模型训练良好的假定，不是新scaling定律。独核R22据实际增量计1+1+2=4，身份/联合日期与关闭判断完成，不借成熟proxy原则补分。未采用headline压缩/任务百分比为通用效率，也未假称全文评价完成或新增Books。 完整题摘/联合日证见[B5](../_sources/daily-20260603/SUP_MODEL_B5_20261024.md)，最终采用见[独核R22–28](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。当前官方abs所见无withdrawn/removed/erratum，只是该页有限notice核，非全网保证；未核代码或复现。

### [Off-the-Shelf LLMs as Process Scorers: Training-Free Alternative to PRMs for Mathematical Reasoning](https://arxiv.org/html/2606.01682v1)

exact-v1 §3/Eq1–4、§4.1–4.8/Table1–5/Limitations；固定chunk上限仍有EOS短段，likelihood不等真值，matched干预不等FLOPs/时间。math/同family、PRM与small-greedy反侧、废弃候选/双模型驻留/串行费用保留。Ch20 LTM完整marker后/链-答案likelihood完整组前已实际融入受限选择机制，非exact speculative；独核R24必要/owner/PRE、R25唯一真实POST通过，窄位生效释放。 完整题摘/联合日证见[B5](../_sources/daily-20260603/SUP_MODEL_B5_20261024.md)，实际必要范围及原未采用提案见[本项原证记录](../_sources/daily-20260603/SUP_MODEL_B5_TWO_SOURCE_20261024.md)，最终采用见[独核R22–28](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。当前官方abs所见无withdrawn/removed/erratum，只是该页有限notice核，非全网保证；未核代码或复现。


### [CANARY: Zero-Label Detection of Fine-Tuning Contamination in Language Models](https://arxiv.org/html/2606.01695v1)

精确v1采用范围：可信base差分与clean参考下的whitebox候选审计信号。§3–6/Eq2/5.2/5.6–8；跨架构与低rank反退、LogitKL逐prompt同分、未知shift阈值不保证保留，不采用α0放大或手术链。完整必要范围、评价条件与不采用链见[本批Source及精确owner提案](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)，[独核R30–32](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核准贡献、分数、必要原域与实际owner；root已将原单段融入[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)原论证及本人章末注，R33唯一非writer实际完整新增/完整直接两侧/本人注POST通过，指定窄位生效释放。未核实现或复现，有限结果不授通用安全、公平或生产性能。

### [TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment](https://arxiv.org/html/2606.01755v1)

精确v1采用范围：同题多persona离线未来反馈与客观真值/风格分责。§3–6/A.1；truth参考与judge资格分开，return正域/标准化/轨迹目标桥未闭，不采用完整NSW最优或普遍公平。完整必要范围、评价条件与不采用链见[本批Source及精确owner提案](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)，[独核R30–32](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核准贡献、分数、必要原域与实际owner；root已将原单段融入[Ch31](../../../../books/part-04-training-system/31-rlhf.md)原论证及本人章末注，R33唯一非writer实际完整新增/完整直接两侧/本人注POST通过，指定窄位生效释放。未核实现或复现，有限结果不授通用安全、公平或生产性能。

### [DOT-MoE: Differentiable Optimal Transport for MoEfication](https://arxiv.org/html/2606.01666v1)

精确v1采用范围：联合neuron分组与token routing、dense-mask到物化expert转换。§3–4/D/E/H/J；结构capacity非token负载，STE非无偏、dense-mask非训练提速，质量差额与alignment/rounding费用保留。完整必要范围、评价条件与不采用链见[本批Source及精确owner提案](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)，[独核R30–32](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核准贡献、分数、必要原域与实际owner；root已将原单段融入[Ch21](../../../../books/part-02-model/21-moe.md)原论证及本人章末注，R33唯一非writer实际完整新增/完整直接两侧/本人注POST通过，指定窄位生效释放。未核实现或复现，有限结果不授通用安全、公平或生产性能。

### [Don't Let a Few Network Failures Slow the Entire AllReduce](https://arxiv.org/html/2606.01680v1)

精确v1 §2–6必要域支持带宽退化但rank仍在线时的四阶段数据流与受约束segment流水；不采用完整formalproof/任意拓扑最优。完整机制、联合日证、SimAI确定性模拟而非实机、多个straggler额外开销反侧及旧alias差额见[本项原证](../_sources/daily-20260603/SUP_OPTCC_SOURCE_20261024.md)。独核R34必要Source/actual-owner/精确单段PRE通过，root已在Ch36原两完整段之间补具体流程，R35唯一实际完整新增/直接两侧/binding/本人注POST通过；旧SF-OPTCC-ASYMMETRIC-ALLREDUCE及旧Jun02trace保持，不重复建立owner。未核代码、全证明或复现，慢链路模拟结果不授端到端训练/SLO保证。

### [AlphaToken: Decoupling Adaptation and Stability for Path-Aware Response Token Valuation in LLM Post-Training](https://arxiv.org/html/2606.01635v1)

采用命题：目标验证/参考Fisher漂移与有限Value路径共同选择监督。不是完整因果或无遗忘保证；验证样本参与选择、代理匹配条件、目标/retain反退与更慢全费保留。精确必要证据/实际owner差额见[原证及提案](../_sources/daily-20260603/SUP_ALPHATOKEN_SOURCE_20261024.md)，[独核R38/R41](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)分别核必要原域/新PRE与实际写后。原单段及章末本人注已融入[Ch29](../../../../books/part-04-training-system/29-sft.md)，唯一非writer完整新增/直接完整两侧/本人注POST通过生效，窄位释放。未核实现或复现，不用局部实验签发普遍质量、训练/服务加速或生产SLO。

### [ProbMoE: Differentiable Probabilistic Routing for Mixture-of-Experts](https://arxiv.org/html/2606.01509v1)

采用命题：固定基数subset采样与精确条件边际STE、部署MAP分责。精确边际不等非线性taskloss真实无偏梯度；动态k少expert可损质量，未核Eq8完整实施不补recipe。精确必要证据/实际owner差额见[原证及提案](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)，[独核R37/R41](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)分别核必要原域/新PRE与实际写后。原单段及章末本人注已融入[Ch21](../../../../books/part-02-model/21-moe.md)，唯一非writer完整新增/直接完整两侧/本人注POST通过生效，窄位释放。未核实现或复现，不用局部实验签发普遍质量、训练/服务加速或生产SLO。

### [TwinQuant: Learnable Subspace Decomposition for 4-Bit LLM Quantization](https://arxiv.org/html/2606.01556v1)

采用命题：共同postquant目标与INT32中间片上scale/requant/pack消费接口。量化前线性恒等不授量化后无损/全网consumer等价；质量/速度rank不拼同预算、反侧及全部准备/运行费保留。精确必要证据/实际owner差额见[原证及提案](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)，[独核R40/R42](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)分别核必要原域/新PRE与实际写后。原单段及章末本人注已融入[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，唯一非writer完整新增/直接完整两侧/本人注POST通过生效，窄位释放。未核实现或复现，不用局部实验签发普遍质量、训练/服务加速或生产SLO。

### [Cross-lingual Self-Consistency for Multilingual Reasoningwith Language Models](https://arxiv.org/html/2606.01464v1)

精确v1 §3–6必要域/Limitations：平行语言答案须canonical可比，按各语言频率构造均权或参考语言log reward，不增加独立真值；强语言目标可优于均权池，单语言仍退步。自翻译、共错/parser、全部L×N生成与训练成本保留。必要原证、评价合同和Ch33具体差额见[B5末节01464](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)，[独核R43/45](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)分别通过必要Source/实际owner/原单段PRE及唯一实际POST；root已将原单段及本人H2注融TTVS完整组后、安全表示读出前。未核代码或复现，不由一致性授正确性、通用迁移或净省。

### [AMP / memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations](https://arxiv.org/html/2606.01138v1)

精确v1采用限适配快照的三项兼容反侧：user scope丢失、稳定record id缺失造成逐记录操作失效、空ExpirePolicy变全选；68PASS/12SKIP/0FAIL不能解读为全部语义已通过。root原N提案被独核R47依据精确PDF原反侧纠正，随后必要原域实际采用与R48 score/actual-owner/单段PRE、R50唯一actualPOST完成，原单段及本人注已融Ch77 HyMemory迁移完整段后/poisoning更新可信前。完整证据、改判原因与版本/联合日证见[决定性补读及必要采用](../_sources/daily-20260603/SUP_AGENT_DEFINITION_DELTA_20261024.md)，[独核R46–50](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)。不采用后版PurgeBench/recover，不断言当前所有框架仍有同问题；未核实现/复现，小规模conformance不签通用隔离、删除或SLO。


### [Before and After Temperature: A Distributional View of Creative LLM Generation](https://arxiv.org/html/2606.01451v1)

精确v1 §3–7必要审阅与actual Ch20经[独核R52](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)通过争议判断，保2+1+2=5而非降分排除。作者以T1.5 top200捕获至少.95质量为充分性依据，但Table1中88.41%的实际采样token需追加到头外；在同一分布/支持假设下强烈失配，原文未给足实际sampler与完整归一分母解释。保存头重归一、采样后append、跨温度不同K与已分歧prefix不能冒完整同条件概率；alpha前缀的离散overshoot与censor分母也待消歧。不是声称有限随机偏差逻辑不可能，亦不是网络故障。

[必要证据与完整边界](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)保留模型/硬件/采样与judge人口、coherent两区间feature相同的反侧、特征选择与全部测量费用。Ch20已有排名不变、条件头非全分布与AR闭环，不重复写成熟原则；新增的经验诊断优势尚未成立，故中心争议/Books暂缓，不以已有覆盖隐藏冲突、不采用精确相关或净性能保证。只在取得同一步raw/post分母、capture/append支持、实际processors的原始记录或明确纠错，解释mass/append及alpha/censor后定点重开；恢复经验优势还需同条件或明确分账prefix及独立coherent人口验证。不要求整库复现，也不因此停止其他普通待办。

### [Learning from Saturated Data: Signals Beyond Correctness for LLM Training](https://arxiv.org/html/2606.01436v1)

精确v1 §3–6/A.1/B.1–3必要域：当前8次全对仅经验饱和，正确性组内无排序不等SFT无学习信号。用pair judge胜率或平均完整词表token熵倒数在正确回答内构造DPO极值pair，另一σRRHF为长度归一rank hinge、sigmoid gap权重及最高分SFT anchor，需同题候选在device比较组内相遇；不是已实现GRPO。GSM8K自judge训练与instruct/entropy两类反退直接限定优势，强judge亦非真值，同generation pool不等总预算。

[必要原件/评价与最小差额](../_sources/daily-20260603/SUP_MODEL_B5_SOURCE_20261024.md)保held-out测试/validation选点、LoRA/sweep和全部采样/判分/训练成本；未核代码、复现或普遍迁移。独核R54核必要证据/5分/actual Ch34原单段PRE，root已真实保存单段及本人注，在SilentForks完整段+marker后、OSCAR完整段前；[R55唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核真实新增、完整直接两侧与本人注通过生效。只新增经验饱和人口的训练接口，原行为规则pair与视觉grounding分支均保，不把低熵签为正确推理。

### [Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents](https://arxiv.org/html/2606.00476v1)

精确v1 §3–5/Table1–2必要：用显式DECISION对JSON检查结论/动作，另核EQUITY/POT_ODDS/RULE到结论，避免把free-text parser噪声当行为不忠实。500次Monte-Carlo加阈值只是固定heuristic reference，不是精确GTO；显式elicitation、缺失/可解析人口、固定seat与同手decision相关均限制因果与外推，低不一致率不认证隐藏推理忠实。root定点核v1 PDF第一页/页脚与v1 HTML一致，未用后来摘要回填；没有复现/实现或通用规则无用结论。

[必要证据/评价与owner差额](../_sources/daily-20260603/SUP_AGENT_DEFINITION_DELTA_20261024.md)保局部人口、所有调用/参考求值/判分成本和反侧。独核R56通过5分、actual Ch66原单段PRE，root已真实保存于promptparser完整段13287后、语义scorer完整段09497前及本人注；[R58唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核完整新增/直接两侧/本人注通过生效。Ch80不复制该测量owner，原输出合同与语义scorer论证保持。

### [OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents](https://arxiv.org/html/2606.02031v1)

精确v1 §4/5.4–5.5/Table4及A相关配置必要：rollout与优化重建同一managed context，保历史reasoning/tool calls与逐call text feedback、仅留最近截图。Context消融以15-step-only为基准，不是full15→30课程；增加第二截图有增有退。更多SFT还改变数据分布，不构成可塑性单因果，文本反馈不等真实状态/原子commit，终奖广播不等逐步真实credit。

[必要原证/评价与actual owner差额](../_sources/daily-20260603/SUP_AGENT_DEFINITION_DELTA_20261024.md)保训练阶段计费歧义、judge代理与去abort/official不同协议、有限模型/站点人口及所有采样/浏览器/训练费用；未核实现或复现、不采SOTA因果/普遍最优。R59通过5分与Ch33原单段PRE，root真实保存于AgentGym-RL完整horizon段及独立08755 marker后、稀有轨迹完整段前及本人注，[R61唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)通过生效；不复制旧cap课程或另建Ch75/81 owner。

### [Consistent and Distinctive: LLM Benchmark Efficiency via Maximum Independent Set Prompt Selection on Similarity Graphs](https://arxiv.org/pdf/2606.01400v1)

精确v1 PDF §3–7/T1–6/Limitations必要（HTML后段乱码未冒可读全文）：subset-selection不同种子的Kendall W，与各子集相对完整benchmark的Spearman rho测不同参照；内部稳定可以与偏离全量排名并存。原distance连边d≥theta所成MIS与每theta/2区域最多一点的覆盖论证冲突，不能静默反转边方向后采用均匀去重、纠偏或净省费。完整benchmark排名也不是独立领域真值，低相关不等子集更公平。

[B6必要证据与actual Ch66差额](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)保四英文基准/固定model-panel、离线anchor、缺失配置与所有embedding/建图/求解/选参费用；未核实现或复现。独核R63通过5分/原单段PRE，root已真实融入compression artifact完整段及12475 marker后、下一压缩分支完整两段前和本人注，[R65唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核真实新增/完整两侧/本人注通过生效。只采用两种rank参照边界，不将原方法冲突包装成正面图算法保证；01387后续已R66/68实际闭合；MODEL其余普通项继续。

### [Fail-Closed Lowering of Resident KV Claims onto LLM Serving Runtimes](https://arxiv.org/html/2606.01387v1)

精确v1 §3–10/12只采用runtime lowering的责任界限：预登记registry/稳定KV身份和有序事件允许外部adapter重建观察，却不凭telemetry创造scheduler、allocator或storage的执行义务；同一claim须先restore再reuse，失败结果须先于terminal处理，wrong-claim故障或重算不是restore成功。local patched vLLM的invalid-load witness不是upstream用户接口或initial admission拒绝；curated descriptor和有限mutation控制不证明所有未审路径正确，131/30/30/41还是不同gate人口而非整齐的成功分类。

[B6必要证据及actualowner](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)保单GPU/受控注入、配置未披露、registry/joins/hooks/失败回退完整费用，未核代码或复现。原Ch45 ResidentClaim已有字段与显式降级，新增只补上述lowering深度与顺序，不重复字段或扩为生产保证。R66独立必要/原单段PRE、root真实保存及[R68唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/直接两侧/本人注通过，融于24259原组之后、双向prefix刷新组之前。其余普通研究仍继续。

### [RLVR without Ineffective Samples: Group Prioritized Off-Policy Optimization for LLM Reasoning](https://arxiv.org/html/2606.01281v1)

精确v1 §4–6/T1–2/C/D2的受限接口是用近期FIFO中reward有差异的完整组补更新空槽，分开old/behavior外权与current/old proximal clipping；同policy组身份不取消筛选人口/年龄偏差。原Alg1空buffer库存缺口不能补造已验实现，PPO clipping也不强制理论全域ratio界；过陈旧池collapse、部分任务弱于DAPO与7B比GRPO更慢的反侧均保。训练/采样配置与完整费用见[B6必要包](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)，不将更满batch当无偏、全纠偏或免费训练。

R69独立必要/actual Ch33/原单段PRE后，root真实融入FIFO/reuse论证与成功轨迹正则分支之间；[R72唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核完整新增/直接两侧/本人注通过。只采该具体接口，不重复已有replay原则，不授实现核验或复现。

### [Real2SAM2Real: Generative 3D Caches as Complementary Context for Video Diffusion](https://arxiv.org/html/2606.00299v1)

精确v1 §3/4.1–4.4/T1–2/5：生成的完整前景mesh通过给定轨迹渲染normal条件，外观reference与几何软注入分路；视频估计normal的训练人口和推理时粗mesh渲染人口仍有差异，实例扰动/LoRA是适配手段，不是完全保留prior证明。v1为300训练clips，不采用当前后版2000；相机/对象测试分母分账，RPE-R和消融smoothness有反侧。闭合隐面不是新观测，给定对象运动不是学得物理transition。

[单篇必要及actual Ch25差额](../_sources/daily-20260603/SUP_MULTI_NEXT_SOURCE_20261024.md)保主文配置未披露与资产/伪标/适配/渲染/采样费用，未核图像素、代码或复现。R70原单段PRE、root真实保存后，[R73唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/直接两侧/本人注通过，融于VerseCrafter载荷评价与E³C静态空间/人体条件之间，不授无歧义、真实状态或动作提交。

### [Thinking Economically: A Hierarchical Framework for Adaptive-Complexity Reasoning in LLMs](https://arxiv.org/html/2606.01168v1)

精确v1 §3/4 T1–3/6采用两级预算监督：从教师有限候选中最短成功链构造题目step-range标签，训练期再以PPL排序、局部NLL probe与embedding梯度提出步骤压缩。它们不是最少必要步骤、真实难度或Fisher真值；hard选择反传/对齐未闭处不补完整recipe，部署不在线执行该Fisher剪枝。MATH500先过滤后split为233/77/78，不能称原500全人口测试；固定depth或整体组合对照也不隔离所有组件，候选、验证、router、probe/梯度与全部适配均计费。

[B6必要/actualowner](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)与R74确认Ch29已有删条件历史和loss选位不等该两级接口；root原单段真实融入XS-CoT之后、trajectory repetition之前，[R77唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/直接两侧/本人注通过，不授逻辑保真、Pareto最优、净加速或复现。

### [When Data Is Scarce: Scaling Sparse Language Models with Repeated Training](https://arxiv.org/html/2606.01155v1)

精确v1 §3–5/F的最小长期命题，是在同一数据饱和边界内联合冻结unique数据、重复暴露、active/总容量与稀疏度，再依实际预算问题比较边际收益。经验拟合、partial grid和外推最优点不是通用系数，loss-optimal与compute-optimal也不具有相同约束；理论稀疏FLOPs不认证墙钟，完整条件及反侧见[B6必要记录](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。

[R78独立必要/具体NC](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)确认actual Ch28“数据受限的Scaling必须把Unique Data与Repetition分账”两完整段已承载上述联合比较、拟合边界/重校准、实际硬件与dense回退，精确旧primary alias为SF-SPARSE-REPEATED-TRAINING；没有以主题近似替代比较，也不为经验常数制造新书段。旧Books trace标Daily06-02不单独证明该事件已经在旧Report有效审阅，未据此迁旧候选日期或排本窗候选；当前仅作实际已有覆盖，不计新I、不授复现。

### [StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement](https://arxiv.org/html/2606.00267v1)

精确v1 §3–4/6/B.6/D.4–5/F支持定向调整diffusion初始noise、以VLM语义目标和prior统计限制提出失败样本。局部搜索不认证全局最坏、物理正确或base未支持的真实分支；定向命中率也不是环境风险概率。相同候选或iteration数不等相同生成/验证/反向费用，VLM存在reward hacking，有限策略改善仍依赖选定数据与真实闭环验收。

[必要记录及最小差额](../_sources/daily-20260603/SUP_MULTI_NEXT_SOURCE_20261024.md)保留直接反侧和未核实现/复现边界；R79首次必要/六分/actual owner/PRE通过后，root原单段融入Ch25随机分布验收之后、动作结构probe之前，[R81唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/完整两侧/本人注通过。新增的是压力提案接口，不替代原随机频率、参考分布或实际动作安全验收。

### [DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts](https://arxiv.org/html/2606.01062v1)

精确v1 §3–4/6/B.1在选定experts之后，构造固定K节点的逐深度成对非线性消息，再聚合输出；不重新顺序执行experts，向量gate也不自动省去pairwise计算。DP构造要求给定图和足够深度，不能证明语言训练已学得推理算法；近似同FLOPs的有限对照仍有吞吐下降与下游退步，配置相同不等训练权重被冻结。

[B6必要记录](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)保共享配方歧义、规模外与未核实现边界。R84必要/五分/actual Ch21/PRE通过，root原单段实际融入Dispatch–Aggregation与检索Router之间，[R87唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/直接完整两侧/本人注通过；只补输出组合轴，不改原dispatch、通信与容量解释。

### [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](https://arxiv.org/html/2606.02486v1)

精确v1 §3–6/B.3/B.5–8/C.5–6/D.1/E.2–5支持从短序列估计运动、仅预测选中patch并对齐给冻结action decoder，样本方差限制展开视野。首次越阈不是最后安全步，预测未来不等新观察或已匹配执行时点；共享运动估计/启发噪声不是完整校准。固定视野、简单运动模型和全patch仍有较好切片，chaotic场景的adaptive对固定消融未完成，更多样本亦非零费。

[必要证据与actualowner](../_sources/daily-20260603/SUP_MULTI_NEXT_SOURCE_20261024.md)保受限本体实验、训练/对齐与控制总预算；R85必要/六分/原两段PRE通过后root真实融入Ch26 Latency开篇，[R88唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/完整两侧/本人注通过。未核图像素、代码或复现，不由局部抓取率签普遍实时或物理安全。

### [SafeVLA-Bench: A Benchmark for the Success–Safety Gap in Vision-Language-Action Models](https://arxiv.org/html/2606.00773v1)

精确v1 §3–5/T2–5/C.2–6/D/E先由信号、任务机制和对象属性确定适用谓词，再分开全部轨迹的满足率、成功且违例联合比例与成功条件违例率；最坏归一深度不等累计伤害或真实风险。全episode排除、阈值/严重锚选择及固定规范量的统计区间都影响解释；两个MuJoCo host的有限结果不能认证真实硬件或在线shield，不混v3的样本或后训练。

[必要证据/actualowner](../_sources/daily-20260603/SUP_MULTI_NEXT_SOURCE_20261024.md)与R89核实原success非安全原则已有，不重复计为Design3；正式2+2+2=6只给具体测量接口。root按R89将“柜体”精确修为“抽屉等关节部件”，其余原两段实际融入Ch26 Evaluation开篇，[R90唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/完整两侧/本人注通过。未核图像素、代码或复现；保原日志/动力学分责及控制权限。

### [Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference](https://arxiv.org/html/2606.01007v1)

精确v1 §3–5/A/D/H以已知task family软偏好重权原共激活边，离线分组并修复primary容量，再与副本/近期负载guard分责。偏好不是expert语义，原无边不凭标签新造；primary容量不覆盖副本内存，guard空可行集回全候选也不提供硬负载保证。通信hop代理/dispatch Jain不能替带宽、排队或E2E时延，去guard的有限对照还以更差热点负载换更低通信代理。

[B6必要及actualowner](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)保指标分母/完整调度和规模外未证边界；R92必要/六分/原稿通过后root单段真实融入Ch21输入浓集风险与跨层affinity之间，[R94唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/完整两侧/本人注通过。未核代码或实机复现，不按局部代理批准鲁棒部署。

### [Detect Before You Leap: Mirage Detection in Vision–Language Models](https://arxiv.org/html/2606.00435v1)

精确v1 §3–6、§7 T3/错误及答案质量、§9/A.2–4/B.1/K/L支持以固定CLIP读出探测跨层patch-question轨迹，再与pixel/domain/structured class融合放行候选答案。中间层投影只是近似；完整路径先生成候选再release，不采用before-generation免调用解释。MR分母是全部三类input，不是条件FPR或事实confidence；Related仍可答错，T3较低MR和较高分类准确不总同得，混入拒答的答案均值不认证相关样本质量无损。

[必要证据与actualowner](../_sources/daily-20260603/SUP_MULTI_NEXT_SOURCE_20261024.md)保训练/开发与校准人口、直接反侧和全部执行费。R95必要/五分/原两段PRE通过后root真实融入Ch23样本可靠性之后，[R96唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)完整新增/完整两侧/本人注通过；不倒填v5结果，不授临床、普遍正确性或代码复现。

### [Decoding in Order-Agnostic Language Models: Chain-Rule Deviation and Uniform Spreading](https://arxiv.org/html/2606.00997v1)

精确v1 §3–4/6/B的必要证据区分固定target的跨路径条件概率与自由生成自产token confidence；所测mask条件不自动来自同一相容joint。均匀极值有固定乘积等假设，不把低方差变成任务可靠性定律；Table2及IFEval低均值桶反例、弱相关与全部min-Var候选轨迹成本均保留。

[必要证据与实际owner](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)经R97独核后，root将原单段融入Ch24 Objective/Commit与训练bound测量之间；[R99唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核完整新增、完整邻接及本人注通过。只采用单checkpoint/block内单位置的诊断接口，不认证并行提交、精确分布保持、在线最佳策略或SLO，未核代码/复现。

### [Lodestar: An Online-Learning LLM Inference Router](https://arxiv.org/html/2606.00946v1)

精确v1 §4–5/B支持按决策快照与所选endpoint的负TTFT训练共享预测器，再以近期FIFO和多样回放持续更新。未选endpoint没有反事实标签，路由又改变后续cache与负载，不能授无偏或长期全局最优；逐特征range guard非完整OOD检测，贪心TTFT可能驱逐未来共享KV。V100禁用prefix功能的混杂、专用A30与数据库/采集/训练/推断费用均保留，未采用未闭tie配方或生产SLO保证。

[必要证据与actualowner](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)经R100通过，root将原单段融Ch56全局延迟模型之后；[R102唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核实际新增、完整两侧及本人注。支持和直接反侧足即停止，未核代码或复现实验。

### [Training-Free Image Inversion for One-Step Diffusion Models](https://arxiv.org/html/2606.01380v1)

精确v1 §3.1–3.3/4.1–4.6/T1–5区分noise先优化冻结、suffix后学与同源图重复使用；免重训不是免逐图准备，单步编辑也不是完整请求成本。30步DDIM及600更新的费用和单次较慢反例、结构/感知/语义取舍、U-Net有限范围保留；不采用未闭KL估计recipe、严格语义解耦或背景无损。

[必要证据与actualowner](../_sources/daily-20260603/SUP_TFINV_SOURCE_OWNER_20261025.md)经R101通过，root将原单段融入Ch24训练期编辑适配与离散编辑分支之间；[R104唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)实际核完整新增、完整邻接及本人注。未核图像像素、代码或复现，不用后版结果倒填。

### [Memory-Efficient LLM Training with Dynamic Sparsity: From Stability to Practical Scaling](https://arxiv.org/html/2606.00888v1)

精确v1 §3–5/C/G支持regrow新连接的局部时钟重置、warm-up及density/active-only optimizer状态分账；局部smoothness界不证明全局收敛、稀疏kernel加速或故障恢复已验。主表外引/预算不全同、SMETgrad及单LR反退、estimated memory与硬件未披露边界保留。

[首次必要证据及实际三段比较](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)经[R105](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)独核：Ch28动态稀疏组已具体承载cold-start压力、local timestep/warm-up/density及active-state身份、代价和dense/static退路，不只主题相同。六分具体已有覆盖，无新增正文或POST；不据同family标记冒称旧事件已审重复，不搬原归属，未核代码/复现。

### [Knowledge-Intensive Video Generation](https://arxiv.org/html/2606.01285v1)

精确v1 §3–5/A.1/A.4/A.5将视频画质、文本claim事实精度、用途完成和原片grounding分开。1080是题库而实际仅54题，参考人类视频另选题；全部规划/判分同源judge，108对偏好每对仅一人且人机tie政策不同。较高text-only agreement可能漏视觉grounding，不能删除原视频支持；HelpS尺度/百分比显示式未齐，不采用完整公式或安全保证。

[必要证据与actualowner具体比较](../_sources/daily-20260603/SUP_KIVI_SOURCE_NC_20261025.md)经[R107](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)独核：实际owner修为Ch66而非初筛Ch24路由，视频目标/过程、caption逐claim原片支持与Unknown、MuRGAt支持/coverage/正确性及Judge Agreement身份已完整承载长期分账。五分具体已有覆盖，不追加benchmark摘要或重复正文；全部生成/提取/判断及人审计费，未核图像素、代码或复现。

### [CUPID in the Model Zoo: Online Matchmaking for Selecting Your Dream LLM](https://arxiv.org/html/2606.00846v1)

精确v1 §3–5/B.2–3支持同时维护个人目标belief与目标条件utility，联合提出下一对比较。metadata/judge模拟、有限真人偏好与任务正确性不是同一证据；目标明确时机制可冗余，花费后调price penalty不是事前硬预算准入。辅助调用/GP选择及用户时间全计，不采用完整后验/regret recipe、普遍最低费或部署正确保证。

[必要证据与actualowner](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)经R108通过，root将原单段融入Ch66固定目标主动比较之后、比较图估计校正之前；[R111唯一实际POST](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)核完整新增/完整两侧与本人注通过，未核代码/复现。

### [PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation](https://arxiv.org/html/2606.00515v1)

精确v1 §3–5/7、A全部假设/证明、B.1/B.3区分低频VLA提案与高频gate/projection/tank的唯一admittance提交。证明有对角采样、合法状态/envelope、damping credit及数值残差等前提，零sampled margin violation不能替峰值力或任务安全；T1规则controller更高safe、T2 stale/random与独立EV分母等直接反侧保留。

[首次必要证据与具体三段比较](../_sources/daily-20260603/SUP_PACO_SOURCE_NC_20261025.md)经[R109](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)独核，正式6分而非题摘暂拟8：经典passivity不是本研究新增基础定理，评分不借成熟原理，安全影响仍深入必要证明。Ch26已完整承载cold/stale压力、提交链、残差/非全物理保证和代价/退路，具体已有覆盖；不新写Books或计I，不据marker冒旧事件已审duplicate，未核代码或真机复现。

### [Mitigating Hallucinations in Large Language Models Via Decoder Layer Skipping](https://arxiv.org/html/2606.00819v1)

精确v1 §2–4/Eqs1–7/Alg1/T1–3只能给readout差向量方向触发局部residual插值候选：非真实gradient/幻觉标签，已算当前层也不物理省算。α方向文字与公式相反、分布制备/改后传播/cache/零范数未闭，会直接限制所报质量表的执行路径归因，不是仅部署优化；部分任务/配置反退与全部额外投影/重传播/校准费保留，不私补hook或完整recipe。

[必要原证](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)经[R112](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)独核收窄，作者原稿未获批准；root只采用reader完整修后单段，融入Ch17 Residual主干与有条件势函数之间。R114唯一实际POST核完整新段/完整邻接/本人注通过。Books保留候选性质和未闭边界，不将性能表写为完整机制已证、原分布无损或已复现。

### [Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs](https://arxiv.org/html/2606.00813v1)

exact-v1 §3–6必要证据及直接反侧见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。仅采独立生产并冻结source归档、同一归档跨target重放的评价身份；不同source的对角线并非同一难度人口。三seed/单模型家族，参数量与架构共变，类别网格与空类分母未闭，52响应第二judge的refusal一致不等harm真值；固定raw-seed本已观察非单调，不采“静态必漏”、普遍安全排序或alignment因果。完整搜索、重放和分歧审计计费，未复现/执行攻击。5分；实际Ch66攻击预算完整段后、Red-TTT完整段前融入一段及本人注，经R115首次必要/PRE、R117唯一实际POST通过。

### [Mechanistic Diagnostics of Spatial Lexical Bias in Multimodal Large Language Model Spatial Reasoning](https://arxiv.org/html/2606.01914v1)

exact-v1 §3–6/D/J/K1–2/K6–7/L1的支持与直接反侧见[必要包](../_sources/daily-20260603/SUP_SPATIAL_LEXICAL_SOURCE_20261025.md)。同图同题的选项语义负控、probe和双向state干预分开信息可读与消费错误；55个高脆弱case为选后人口，blank单独重训、同批选层/选通道与非能量匹配randomK不授唯一因果。冻结视觉的语言LoRA修复不证明视觉充分或未学新知识，公共binary切片仍反退；全排列robust不是普通准确率，完整对照/适配/质量回归计费。6分；实际Ch23完整2610-29241诊断段后、文本局部性段前融一段及本人注，R116首次必要/PRE、R118唯一实际POST通过。未采用后版或宣称代码/复现。

### [Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety](https://arxiv.org/html/2606.00801v1)

exact-v1 §2–4/Alg1/T1、A/T2与C必要证据及两实际承载段见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。语义genome与archive描述符不同，按cell保留局部最优不认证威胁全覆盖；单generic seed、单次query不支持真实多轮或跨模型迁移。三值fitness与结果/附录四值及.8定义冲突、类别排序矛盾保留，不补造ASR或安全排名。5分，R120首次必要及具体已有覆盖通过：Ch66现有Adversarial Coverage段明确cell数量/局部质量/未覆盖与archive成本，00813段明确冻结重放、有效类别分母及judge/Unknown，已承载可采用长期分支。不是同事件重复，不降分、不新增Books/注/PRE/POST；未运行攻击或复现。

### [RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation](https://arxiv.org/html/2606.01600v1)

exact-v1 §3–5/Limitations/B–E支持与直接反侧见[必要包](../_sources/daily-20260603/SUP_ROBOTRUST_SOURCE_20261025.md)。只初图+语言的离线视频，不是action-conditioned闭环。1207对含77编辑图，人审180对分层子集而非全量，自动judge抽20帧，细物理/图像agreement仍弱；NA及三次门禁无返回从部分评价排除，不能由返回子集宣布服务安全。可行性会改变completion分数的解释，有害可行不等不可行；5分，此具体命题融actual Ch25三结论/WorldReason完整段后、环境动态H3前，R119必要/PRE与R121唯一实际POST通过。不同片长/采样预算及生成/人审/校准费用保持，不授真实执行、安全、无遗漏或净性能保证。

### [ViBE: Co-Optimizing Workload Skew and Hardware Variability for MoE Serving](https://arxiv.org/html/2606.00735v1)

exact-v1 §3–5/T2与必要A2/Alg1–2见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。同型号设备的token负载→耗时曲线与expert demand共同决定最慢卡，单点greedy不保证非线性目标全局最优；低QPS/Decode争用可反退，cosine向量漂移看不到纯量级变化。主静态8×MI325X/FP8/TP8EP8、ShareGPT/Sonnet固定人口与SLO代理，不把phase模拟当PD网络实测；动态增量路径前后表述未闭、rack为profile投影，不补完整recipe/服务普效。6分；Ch56现设备速度完整段后、MoE并行切换H3前融一段，R124必要/PRE、R126唯一实际POST通过。采样、校准、迁移及完整回归费用保留，未核像素/代码或复现。

### [TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation](https://arxiv.org/html/2606.00232v1)

exact-v1 §2–4.5/C/D/E2–6/F2–4的机制、条件递推与直接反侧见[必要包](../_sources/daily-20260603/SUP_TIGER_SOURCE_20261025.md)。输入图在输出前固定、claim图每轮另抽，局部risk只排序修补，raw input仍可回读；同模型误差不因conditioning隔离变统计独立，共指传播/embedding差异不成为逻辑蕴含或事实概率。R125把原稿“risk递减”收窄成测得总risk的条件期望上界，非单调实际路径或现实幻觉保证；非零残余、删组件仍赢Frozen、图派生GT/三seed口径张力及detector漏关系均保留。实际Ch23 caption双路径成本段后融R125修后单段，R127唯一实际POST通过，6分。全部图抽取/重复生成/质量核验计费，F3单GPU199s对38s缺精确GPU分配不作通用性能基线；未用后版、代码或复现实验。

### [The Paradox of Outcome Optimization: A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs](https://arxiv.org/html/2606.00674v1)

exact-v1 §3–5/三定理直属proof、Remark1/T1/probe及必要A.1–2/B见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)，R128首次必要/正式6分与隔离通过。给定Z=h(S)的条件MI为零不等绝对无C，更不证明真实optimizer必然坍塌；商空间measure μ未与OOD人口对齐，通用loss不能直接代熵/KL正下界，过程MI与正确标签似然也未给等价桥。三模型472筛后问题/5run的有限表不能补这些中心证明；训练标签/曝光预算、反事实gold及单run probe不足授等预算RL因果。actual Ch31终值/trace和目标兼容段不等已承载新定理，故不是主题NC，也不为造diff添加警告。原分数、有限正侧与反侧都保留，中心bound/filter不用于Books、Coverage/Evidence或普效保证。重开需明确μ为OOD pushforward、loss/统一δ及η随N条件，MI人口/实际目标/验证器与全部最优解的有效证明；若改采经验则需训练/标签/等曝光、472gold/audit与probe原证。材料当前可读，争议不是访问故障，不无限追附件。

### [τ0-WM: A Unified Video-Action World Model for Robotic Manipulation](https://arxiv.org/html/2606.01027v1)

exact-v1 III–VII/Alg1–2/T1–2及直接A/B必要域见[必要包](../_sources/daily-20260603/SUP_TAU0_SOURCE_20261025.md)。VAM提出动作与ACVS按给定动作预测未来/进度是两个消费接口；RCS重去噪一致性非成功概率，低分才触发模拟，以最大预测进度选future后LAR重新query动作，不是执行原被评估候选。旧评价不能继承是项目接口推论，不冒作者已有安全门。两task各20单次、四proposal、CFG/ACG反退及人视频/UMI与预算混杂保留，220/180ms局部query未绑定全部候选/K次评分/模拟/再生成/感知控制的完整TTC。正式6分只实际两接口/证据身份增量；R129必要/actual Ch26及原单段PRE、R130真实POST通过。正文融三接口code后/共享mask完整段前，训练、候选/评分/rollout、生成和控制验收均计费，未核代码/实机或复现，不授deadline与安全。

### [The Invitation Trap: Proactive Availability Backdoor in LLMs via Conversational Induction](https://arxiv.org/html/2606.00654v1)

exact-v1 §3–6/主表及必要D.2/T7见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。R131独立必要/6分通过并发现actual Ch72“模型建议也可能塑造未来Trigger”完整两段已具体承载建议→接受回流→trigger/action、lineage、独立policy/显式确认/最小权限及模拟非真实发生率，故撤新PRE、具体已有覆盖，不是凭marker判duplicate。主实证需上游few-shot污染能力，合成persona/有限轮次不能外推自然用户攻击；AIR×ASR的两阶段乘积未证真实joint，WildChat只接受代理，GPT5.1与其他切片反侧保留。改写防御未排隐含/自适应触发或正常任务损伤，不授永久安全。合成、对话、判分、人审及全部回归成本保留；未读恶意payload/全prompt、未执行攻击/代码或复现。

### [Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition](https://arxiv.org/html/2606.00959v1)

exact-v1 §2–5/C/D/H.1–2/4–6见[必要包](../_sources/daily-20260603/SUP_PID_SOURCE_20261025.md)。Y是模型候选分布非gold，统计分解与文字条件化感官增量不授因果电路或真值；mean pooling、近似Gauss mask、选项mass门与人口共同限定量。跨模型相关和shuffle仅对应功能验证，换题意不作保义因果。训练local clipping/熵gap与先shortcut后gap的非重叠权重，经匹配数量/3seed局部对照支持有限收益，Gemma/知识题和更高synergy而质量更低的反侧全保。正式6分；R132必要/actual Ch23与原两段PRE、R133唯一实际POST通过，融reliability完整段后/TC-LIA前。多条件推理/估计器/50contexts/选样/LoRA及回归计费，GPU/precision/总训练与服务SLO未披露不补，未核代码/像素或复现，不倒填Aug08 v2。

### [Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems](https://arxiv.org/html/2606.00804v1)

exact-v1 §3–8及必要A/B/C定义见[必要包](../_sources/daily-20260603/SUP_DYNAMIC_COORD_SOURCE_20261025.md)。30任务/3重复/4策略/4模型不是1440独立任务；预注册strict最佳假说失败，后验.10容差不等线上非劣或等费router实测。第二judge13/15与结论all冲突、aux排序翻转和固定judge/行业语言混杂保留，不采通用路由表/法规正确性或相关低只是offset的免责。5分；R135必要与actual Ch82四组具体已有覆盖通过，保单Agent/独立验证/equal-budget和协调损伤的边界，不新增正文/注，不为NC省必要层。

### [MESA: Improving MoE Safety Alignment via Decentralized Expertise](https://arxiv.org/html/2606.00651v1)

exact-v1 §2.2–5/T1–4及必要B/E/T5见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。经验activation prior约束选择更新expert，安全流追重分配软router目标、一般流回冻结reference；不是部署实时OT/原频率即真实功能。启发式cost和未核曲率/OT证明不作安全担保，Qwen代码/知识题反退、纯router退步、跨方法LR/曝光预算不同及full/selected-mask实现资格未闭都保。正式6分；R134必要/actual Ch21与原单PRE、R136唯一POST通过，融CNN-MoE反侧后/频率诊断前。Top-k不变不授负载/通信/时延不变，全部统计/求解/训练/安全与效用回归计费；不读无关证明/全部附件、不执行攻击或复现实验。

### [Understanding the Self-Reflection Mechanisms of LLMs through Biased Attitude Associations](https://arxiv.org/html/2606.00600v1)

exact-v1 §3–4/Eq1–4/T1–2、Limitations与必要B见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。Global是均方离散度，Local是组均值差/联合标准差；共同正scale可降低Global但不改Local为项目代数推论，非作者已测干预。一维valence probe、Western二分类、单run/RTX3080/temp0与额外prompt/局部层消融不能签公平真值或唯一反思机制，拒答/中性/真实行为分账。正式5分，R137必要/actual Ch66原单PRE与R139真实POST通过；正文融跨语scorer完整段后、本地考试完整段前，全部采集/投影/提示/行为回归计费。未读F精确prompt图、不据此授treatment因果，未核代码或复现。

### [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/html/2606.01770v1)

exact-v1 §3–6/B/G完整必要域见[必要包](../_sources/daily-20260603/SUP_ADAPTIVE_HARNESS_SOURCE_20261025.md)。演化workspace构造branch集合，solver/router只按当前任务与当时可用版本选用，延迟outcome不能倒灌；Git不自动保证权限/并发隔离。Oracle加减为会计非建设性最优，有限replay的nav/完整子集与branch可用时间不同，FutureX路由低于main、配置fallback却未使用、variants各胜不拼普胜皆保。B仅solver tokens/逐任务elapsed和，不是完整演化费或并发makespan。正式6分，R138必要/actual Ch84原两段PRE与R140真实POST通过，融版本化controller段/marker后，完整保下一demonstration binding组；未核全部prompt/logs/代码或复现，不搬旧06-02NC trace或授未来流稳定。

### [Hierarchical Online Prompt Mutation with Dual-Loop Feedback for Guardrailed Evidence Document Generation: A Production-Evaluation Case Study](https://arxiv.org/html/2606.01472v1)

exact-v1 §3–8/A1–4见[必要包](../_sources/daily-20260603/SUP_HOPM_SOURCE_20261025.md)。请求中选择family/version、生成及校验，与请求外反馈后局部修改分责；CTAM只是操作归因，不是因果根因。7×600同case比较非随机流量/完整factorial，Full guardrail低于human-only和mutation-only、Full-human金额CI跨0；770/318投影与70×5 OCR是不同人口，与01542共享材料不算独立验证。正式5分，R141首次必要/actual Ch74版本池、constraint-residual与SkillOpt三组具体已有覆盖通过，不新增Book或末注；未披露bandit/mutation recipe不能补成实现，全部探索、生成、人审、修订与回归计费，未核代码或复现。

### [Revisiting Parameter-Based Knowledge Editing in Large Language Models: Theoretical Limits and Empirical Evidence](https://arxiv.org/html/2606.00570v1)

exact-v1 §3–6/Th4.5/T1–3与必要C.1/C.5/C.6/T33–34/D/E见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。相同绝对变化除较小方向RMS给较大ratio，不证绝对放大、语义重要或必然行为崩溃；线性累积需coherent，局部近似不可外推长期定律。AlphaEdit推理韧性、GT-locality与before/after保持两人口、event/triples信息差及检索预算混杂均保。R142确认原7仅未冻结准备初分，原JSON不变，按窄证据命题正式6分并深入实际gap；R143唯一actualPOST通过，原单段融Ch5规则编辑与Bregman约束之间。表示/SVD、编辑、检索/生成与双侧回归全计费，未核全B/图像/代码或复现，不采参数编辑普遍失败/检索全轴最优。

### [Self-Conditioned Positional HNSW for Overlap-Aware Retrieval in Chunked-Document RAG Systems: Method and Industrial Evidence-Quality Audit](https://arxiv.org/html/2606.01542v1)

exact-v1 PDF§2–3/6/8与HTML核心有限比对见[必要包](../_sources/daily-20260603/SUP_SCP_HNSW_SOURCE_20261025.md)。HTML封面Aug24与PDFJun2不同，精确v1身份与拟采用核心相合，不改已核Jun02公告日或冒历史逐字证明。位置进入索引向量度量，首检估中心再二检，独立gap选择不等联合效用最优或support独立；原HNSW实现未改不授旧图无条件兼容。多区域/相邻必要证据反侧保留，工业770/318与OCR共用评审不是检索效果，表4仅建议控制实验。正式5分，R144必要/actual Ch76修后单段PRE及R145唯一POST通过，只保待验证设计，不授优于semantic/MMR、真实SLO或实现验证。正文在top-k冗余问题与reader双视图之间，绑定文档/参数/两池身份与重建/双ANN/重排/独立核验全费。

### [DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation](https://arxiv.org/html/2606.01212v1)

exact-v1§3–6/A4必要见[单篇原件](../_sources/daily-20260603/SUP_DISCOURSE_SOURCE_20261025.md)。检索暴露、立场代理和用户前后问卷分开，固定query群不同于连续搜索trajectory；graph关系/judge不是因果或truth，部分COV高于RASR而逐query路径未闭，不据集合指标授因果。选定防护确降低受测指标，不能称所有防御无效；81学生两topic不授泛人群说服、四域构建corpus不等自然互联网发生率。正式6分，R146必要/actualCh76修后单段PRE与R147唯一POST通过，融ecosystem完整组后/长文生成前。全部构建、搜索/生成、判分与独立核验计费，未读操作payload/全部prompt或执行攻击/核代码/复现，不把v2倒填本日。

### [Escaping the Mode Lottery: Multi-Response Training Improves Language Model Generalization](https://arxiv.org/html/2606.00544v1)

exact-v1§2–3/5–6/B1–3/C2必要见[原件与采用边界](../_sources/daily-20260603/SUP_MRT_SOURCE_20261025.md)。固定theta/finitevariance/条件iid下prompt方差地板与response项分开，随机保留只在候选与选择条件下保q目标，q不等真实P；连续成本极值不等整数/全流程最优。匹配steps非全部token/FLOPs，Table2 Similar仍有coverage高于Diverse的反侧，reference CE/cos与正确性分账。正式六分字段2+1+3经R148确认，旧未冻结初分原JSON保持；R149唯一actualPOST通过，两段融Ch27重复曝光与网页问句人口之间。生成、审核、selector、训练和独立回归全计费，未采用广泛uniform bound/全网格或核代码/复现。

### [GNMR: Runtime Stability Control for Low-Precision Large Language Model Training](https://arxiv.org/html/2606.00539v1)

exact-v1§2–5/7/Alg1–2及必要C/D/E关键反侧见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。自历史norm双ratio只是风险代理，maxO为active数量非总bytes/time、lock可被预算排名挤出；4/6bit模拟不授原生速度，matched-trigger比较混合填满cap与稀疏duty，token/LR口径及质量/资源反退保留。正式6分，R150首次必要/actual Ch28同family三段具体已有覆盖通过；正文已实际承载sensor/backend两路径、hardbudget/lock、checkpoint/trace、成本与失败退路，不新增正文/注。旧Jun02恢复DateHold标签不授本轮验收或事件duplicate，旧8分/日期未迁；未核代码、全证明或复现。

### [Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories](https://arxiv.org/html/2606.02060v1)

exact-v1§3–6/B/D必要见[原件与具体覆盖](../_sources/daily-20260603/SUP_TELBENCH_SOURCE_20261025.md)。完整已结束轨迹上的claim/support/dependency审计不是在线修复；弱支持本身非错，465任务重复与有错pool筛选不能补all-clean run误报校准，hard首错定位仍低，版本/工具差异与多调用token费保留。正式6分，R151发现并核Ch66同family `SF-DRIFT-TELBENCH`真实两段已承载span/first-harmful-commitment/claim-lineage传播及localizer非根因，Ch69另拥有immutable trace到派生依赖与原始证据分责。故具体已有覆盖，实际owner由临时Reflection路由纠正为Evaluation，不新增Book/注、不迁旧日期或冒事件已审重复；未核全部prompt/代码或复现。

### [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/html/2606.00516v1)

旧有效crossover核心复用，精确v1§3–4/A4/D6/F3必要补查及actual Ch56具体覆盖见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。EB保未完成KV、累计idle slots后refill；解析阈值依饱和、hazard/fluid等模型，近期profile与延迟更新不授任意流量最优，实际KV gate另担容量可行性。各scheduler各自grid最优不等固定配置净因果；MoE反退、TTFT/TPOT取舍与严格SLO低attainment均保，所有profile/估计/调优/排队计费。正式7分，R152首次核新补必要层与Ch56同family三整段，已具体承载k、状态/容量、crossover、漂移与tail风险及MB/固定阈值/PD退路，故已有覆盖，无新Book/注/POST待办；不以旧计划/marker授重复、不迁旧日期/分数，未核全证明/代码或复现。

### [BraveGuard: From Open-World Threats to Safer Computer-Use Agents](https://arxiv.org/html/2606.01166v1)

精确v1§3–4/T1–3/A及实际Ch72差额见[必要证据](../_sources/daily-20260603/SUP_BRAVEGUARD_SOURCE_20261025.md)。外部威胁结构变为可执行任务与完整轨迹监督，内部validation回拨下一批数据、外部benchmark不参与反馈；实际Jan01文献cutoff不等部署持续适应，binary监督不等rationale训练，事后分类不证明effect前拦截。集合均值headline、动态组件与数据预算混合、跨格式F1反退、完整合成/再训/验收费均保。正式6分，R153 actual owner/原两段PRE与R154唯一真实POST通过；已融Ch72现有安全data-augmentation段后/Policy-as-Data前，区分训练数据更新与运行时规则输入，保原guard、人工和确定性effect gate。未读攻击payload、核代码或复现，不授通用安全。

### [Canonicalized Stable-List Replay for Private Federated Continual Learning over Language-Model Embeddings](https://arxiv.org/html/2606.00426v1)

精确v1§3–7/E/F/G必要域与actual Ch36差额见[必要证据](../_sources/daily-20260603/SUP_CSLR_SOURCE_20261025.md)。公开anchor对已释放回放分布生成签名，先识别canonical mode再按组聚合；可见性/噪声与同模式归组均有条件，oracle不可识别不排除共享坐标OT/Hungarian。仅replay-release预算不覆盖head更新、frozen head非full LLM、不同隐私scope的epsilon不等预算，完整拟合/匹配/交换/训练费保留。正式6分，R155原两段PRE与R156唯一actualPOST通过；已融Ch36 Federated Type完整组后/GradsSharding前，连接可表达性、身份与分块，Ch72仍拥有隐私会计。不授端到端隐私、全FCL收敛、实现核验或复现。

### [LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation](https://arxiv.org/html/2606.02553v1)

精确v1§3–4/Alg1/Eq1–9/T1–3/A/E必要与actual Ch25差额见[必要证据](../_sources/daily-20260603/SUP_LONGLIVE_RAG_SOURCE_20261025.md)。冻结generator，独立key以reconstruction/局部反冗余/二阶smooth形成检索几何，上一完成latent提出query，实际消费成对context；固定12槽意味着近期/非局部预算竞争。delta单项及部分视觉指标反退、共享WAN坐标非跨任意family、自产历史污染和bank增长保留；约0.49秒只是120秒rollout的局部编码/搜索，不免造数/encoder训练/真实context读取等完整费用。正式6分，R157原两段PRE与R158唯一实际POST通过，已融Ch25 depth-residual组后/motion-aware组前；不授真实world state、恒定总内存、无漂移或控制安全，未核图像素/代码或复现。

### [Detector-Evasive LLM Paraphrasing via Constrained Policy Optimization](https://arxiv.org/html/2606.00392v1)

exact-v1§2–3/4.1–4.5/A5/T14标准必要与actual Ch33具体覆盖见[必要证据](../_sources/daily-20260603/SUP_DEPO_SOURCE_20261025.md)。两reward分别组标准化后按lambda混合，dual另读原单位mean语义proxy；期望BERTScore≥阈值不等每条真实保义，也不从CMDP援引给非凸LoRA/clip训练授零dualitygap或严格可行保证。有限主对照、reward-detector与训练域同时改变的转移反退、单seed/完整预算与费用均保。正式5分，R159实际核Ch33 FGRPO多signal/dual、GDPO与CGRPO单位/violation完整正文已经具体承载该可复用判断，故已有覆盖，不新增Book/注。未执行规避改写、核全部样例/代码或复现。

### [CRMA: A Spectrally-Bounded Backbone for Modular Continual Fine-Tuning of LLMs](https://arxiv.org/html/2606.00382v1)

exact-v1 §3–5/6.1.2–6.1.3/T4/6/7/8.1的标准必要审阅见[原证及边界](../_sources/daily-20260603/SUP_CRMA_SOURCE_20261025.md)，独核R161通过，正式2+1+2=5。理想双随机线性M非扩张只限制输入扰动，不证明跨训练时间保持旧任务；固定readout下I与permutation可不同。readout/gate、残差blend、初始化及训练组合主动省略，有限Sinkhorn误差也未闭，不能补造成完整可执行机制。§3.4的完整adapter口径与§5.2每五步instrumented mixing-layer均值不是同一测量对象，T7 FROZEN非零漂移又与zero-by-construction文字冲突；这些中心桥和反证保持隔离，不由“仅报告”变正面验收。

有限Mistral三seed和Gemma旧域loss结果只属于隐藏bundle及正确router条件，不能掩盖Medical/Finance、MMLU/GSM8K反退，也没有matched published-CL对照。实际Ch17/Ch30已承载局部M界与完整计算图、冻结参数/路由的验收分责，不能补出本文未披露组合。故仅报告——关键机制未披露，无新增Books/注。恢复须实际公开完整readout/blend/init/训练配置、解释漂移与测量对象，并给匹配组件及旧新能力对照；不支持严格无遗忘、完整pipeline界、生产可用或全日Coverage。多adapter驻留、路由/Sinkhorn、探索训练与独立回归全计费，未核代码或复现。


### [SPARQLe: Sub-Precision Activation Representation for Quantized LLM Inference](https://arxiv.org/html/2606.00365v1)

exact-v1 §3–5/Eq1–3/Alg1/T1–2的必要支持、反侧和actual Ch49差额见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)，R162正式6分/原单段PRE通过。dense低位与稀疏高位的同码分解不同于整值跳算；含bitmap为9−4s bits/value，需s>25%才省payload，不是同比延迟。保原码与正确符号/位权/累加只是分解等价条件，不补原文未闭signed datapath；clip增强改变函数。isoarea与isoMAC不同、7nm综合/成本模型排DRAM、Llama ARC与BitNet PPL反退及全部校准/codec/两pass/buffer费用保留。已融Ch49 metadata容量段后/StagQ前；首次实际POST R164发现正文误落注区，已仅搬原literal至授权正文位置，R165修后实际POST通过，未重复Source/PRE。无原生GPU支持、完整服务加速/无损A8、代码核验或复现保证。

### [Active Exploring like a Pigeon: Reinforcing Spatial Reasoning via Agentic Vision-Language Models](https://arxiv.org/html/2606.02459v1)

exact-v1 §3–6/Eq1–10/T1–5/F4/F6文字的必要证据见[本项包](../_sources/daily-20260603/SUP_ACTIVE_SPATIAL_SOURCE_20261025.md)。给定视图中按query选择下一图、更新同一估计map、将空间关系变为map上的bool谓词；不是机器人移动，执行True不认证视觉事实、翻译忠实或真实几何。GT map/Y及最终正确门控参与训练，不能授无reward hacking；Among/细网格反退、答对仍坐标错、模拟Common/Complex归零与完整造数/读图/检查/训练费保留。既有可检查地图原则不重复计新，实际小gap是按需视觉消费—共同map更新—关系消费者的监督接口；R163正式6分/原两段PRE与R166唯一actualPOST通过，已融Ch23房间对齐文本完整成本段后/离线多视图分组前。未核图像素/代码/实机或复现，不授真实世界状态、行动或控制安全。


### [HLL: Can Agents Cross Humanity's Last Line of Verification?](https://arxiv.org/html/2606.02449v1)

exact-v1 §3–4/T1–4/A4/B1/B5标准必要见[原证及实际owner](../_sources/daily-20260603/SUP_HLL_SOURCE_OWNER_20261025.md)，R168正式2+1+2=5与具体已有覆盖通过。八类动态检查将终态答案与family-specific可见动作/状态规则分账，不证真人、授权或真实服务防护；过程规则自身仍有false-reject及外部效度义务。T4按同八类静态人口比较，Qwen动态反升及分批完整预算未披露均保，不采所有模型/干扰必退，也不把不同运行变同trace重评分因果。实际Ch66过程指令完整binding、AuditKIT和Procedure-Aware三组已具体承载真实过程/effect与outcome、接受集合/替代合法路径及oracle冲突；非泛Tool主题NC，不重复写benchmark摘要。全部模拟、遥测、规则校准与真实任务回归计费；未操作真实CAPTCHA、核代码/图像素或复现。


### [Geometry-Aware Implicit Memory for Video World Models](https://arxiv.org/html/2606.02436v1)

exact-v1 §3–4/Eq1–20/T1–4必要与actual Ch25差额见[原证及限制](../_sources/daily-20260603/SUP_GIM_WORLD_SOURCE_OWNER_20261025.md)，R169正式6分/原两段PRE和R170唯一actualPOST通过。固定slots不逐一对应frame，训练用历史camera的ray查询memory，辅助head重建冻结teacher特征；推理去teacher/head不免历史读取、筛选或原件存储，不授真实几何/transition。MI来自pose/time代理，submodular字样不补全局greedy保证；translation与强压缩反退、估计器/Sim3评价、三/四重训口径及0.26%局部计时边界均保。已融Ch25 ZipMap完整组后/Mem3R完整组前，不重复已有camera查询原则，只补非frame-indexed生成memory的训练监督接口。Teacher造标、联合训练、所有历史管理/查询/生成/独立回归全付费，未核像素/代码或复现，不授长期无漂移、恒定总成本或物理行动。


### [Rethinking the Role of Temperature in Large Language Model Distillation](https://arxiv.org/html/2606.00306v1)

exact-v1 §2/式2–4/Prop2.1–2.2/§3–4/T1/A的必要支持、反侧与actual Ch29差额见[B6本项](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。同prefix/词表的蒸馏温度同时改变teacher/student分布；RKL也有随温度改变的q权重，不能只称统一scale。高温共同logit-gradient首项不证明有限温度/参数轨迹或下游等价，数学式未乘tau²而实现惯例未核，不补配方。离线固定teacher回答、验证checkpoint/未另明的tau选点人口、三/五benchmark均值与五seed ROUGE-L边界、较高tau反退及全teacher/搜索/训练费均保。正式3+1+2=6，R171原单段PRE与R173唯一actualPOST通过，已融Ch29 Distillation标题后/gold局部修正前；不授on-policy、teacher tail真值、全域目标最优、代码核验或复现。

### [Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference](https://arxiv.org/html/2606.02430v1)

exact-v1 §3/4.1–2/T1–3/5.1–2/5.4/6必要与actual Ch49差额见[本项包](../_sources/daily-20260603/SUP_LLMFI_SOURCE_OWNER_20261025.md)。单bit/特定wrapper阶段下按stage/site/dtype观察差异，再选择保护预算；不以扩维关联证明自纠或给dtype普遍可靠性排序。局部INT8提高fault下质量却损无fault质量，checksum保护FLOPs比例非实际延迟，恢复accuracy损失与重复首token的trial检出coverage不同；共享坏KV可令两次一致，不能补为已验cache/独立冗余recipe。正式6分，R172原单段PRE/R174唯一actualPOST通过，已融Ch49 DRIFT完整组后/Attention统计分工前。全部profile、转换、校验、重复forward/重试及回归计费，未核图像素/代码或复现，不授真实故障率、完整服务无错或SLO。


### [Teaching LLMs to Know Their Limits](https://arxiv.org/html/2606.00251v1)

精确v1 §3–4/式1–4/T1–3/D.1–6/T6–8/F见[B6必要原证](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)。自评训练改变同一solver后，旧可解性标签一致性可能提高而新标签一致性及solver能力下降；K5 any-correct/多数正确标签不是单次可靠率。CDS为带人口分母的z统计量非概率，CR为生成run均值比非逐题无损；RL/SFT训练预算不同、.6B塌缩和跨域反侧保留。正式6分，R175必要/actual Ch66差额与R177唯一实际POST通过，已融Continual Update的exchangeability与推理配置变更两段之间。不倒填v2改题/新实验，不授真正自知、普遍RL优越或自报routing权；所有probe/训练/重标/独立solver回归计费，未核代码或复现。

### [Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation](https://arxiv.org/html/2606.01629v1)

精确v1 §3–5/T2–3/§7/B/C.6见[必要原证及具体覆盖](../_sources/daily-20260603/SUP_LONGJUDGE_SOURCE_NC_20261025.md)。不同point/pair/list协议与参照不能混作同一chance；长度分箱有下降、非单调或上升，未有matched length-edit干预，不授长度因果。Reference/rubric可改善也可损任务，overflow与policy拒绝合并错误应另保无有效判断人口，DOCX存储不证judge完整消费原生图表。正式5分，R176核Ch66 EvalSpec、artifact可见性、reference/rubric受控比较、construct sensitivity/invariance及criterion/ranking分层的真实正文，已具体承载可支持的长期选择；不为新bench或排行制造书稿diff，不倒填当前v4。全部准备/两顺序及辅助输入调用/独立核验计费，未核实现或复现。

### [On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on Annotation Task Performance](https://arxiv.org/html/2606.00467v1)

精确v1 §3–5/T1–8/C/D.1/E.1与actual Ch66差额见[本批必要原证](../_sources/daily-20260603/SUP_CLOSE_BATCH1_20261025.md)。DSF为概念解释与目标定义的embedding匹配代理，不是内部概念直接读出；54个model–dataset cell不是54独立模型，相关不证因果或无污染。定义交换改变政策，不同于保义改写，原错rescue与原对corruption分别验；T3均值与文字增量不齐，未采其差值，多轮拒绝drop人口不授普遍纠错上限。正式5分，R178必要/具体配对sensor差额及R179唯一实际POST通过，已融Ch66四层首解释完整段后/rubric传播完整段前，未拆双侧。全部概念引出、embedding、优化、独立gold/人审与回归计费，保原政策/gold回退，未核代码或复现，不授自报confidence与代理门禁权限。

### [DECK: A Consistency × Confidence Taxonomy of LLM Hallucinations](https://arxiv.org/html/2606.02289v1)

精确v1 §3–5/T2–4/A/B见[本批必要原证与具体覆盖](../_sources/daily-20260603/SUP_CLOSE_BATCH1_20261025.md)。同target500选best-AUROC代表及阈值非独立held-out；反对角分歧由两轴构造，不证明知识独立。高confidence/可重复不普遍推出AUROC0.5，regex拒答与substring命中不授完整truth；当前v2 cross-fit不倒填。正式5分，R178核Ch66 supervised-ensemble完整段及同源modal错误/外部verifier完整组，具体承担scorer误差面、domain shift、相关性与独立校准，故已有覆盖；不为2×2名称或未成立universal桥造书稿diff。采样/scorer、标签/外证及全部校准计费，未核代码或复现。

### [The Shape of Wisdom: Decision Trajectories in Language Models](https://arxiv.org/html/2606.01202v1)

精确v1 §2–8/T1–4见[本批必要原证](../_sources/daily-20260603/SUP_CLOSE_BATCH1_20261025.md)。9000轨迹与600/model平衡traced子集读出人口不同，gold-dependent margin非无标签confidence。Tail stable缺窗口/阈值，比例不授runtime早退；§7 subtraction/substitution为标量记账replay，不是真activation替换，§6删span虽实际重跑但选span独立规则未闭。当前v2明说全新研究替代v1，记录变更而不倒填新centroid实验。正式5分、R178仅报告：新观察保留准入，稳定控制机制与因果桥未立，Ch5既有readout→intervention不为本文未闭定义增加正面主张。重开条件限v1明确操作定义/实际activation证据，不无限追附件；所有读出/干预/独立回归计费，未核代码或复现。

### [Accuracy, Stability, and Repeated-Run Reliability of Large Language Models on Deterministic Programming Tasks](https://arxiv.org/html/2606.00920v1)

精确v1 §3–5/T1–2/Limitations见[本批必要原证与具体覆盖](../_sources/daily-20260603/SUP_CLOSE_BATCH1_20261025.md)。同N100题/R5的PSR应为binary全通过指示均值，T2的47.5%与声明人口不相容且未说明加权，中心排名/精确gap隔离；pooled Wilson不处理题内相关，reasoning预算/温度控制不匹配不授思考单因果。v2已大幅修订为新人口，不修复v1数字。正式5分，R178核Ch66 Pass@k→Pass^k完整code/解释/边界、Evaluation Identity与不确定性组已承担outcome vector、conjunction、paired transition及隔离重置，具体已有覆盖。逐题Y/明确权重与版本依据才定点重开数字；全部生成/执行/重复/人口核对计费，未核API行为或复现。

### [Training Prompt Matters: State-Adaptive Optimization for Robust Fine-Tuning](https://arxiv.org/html/2606.01967v1)

精确v1 §4/Alg1、§5/T1–3及必要gradient/设置；同任务选表述不是逐step prompt学习，训练和评价共同换prompt仍有混杂，BWT/FWT反退及局部梯度非完整因果。 正式2+1+2=5，R180/R184必要/actualowner与唯一实际POST通过；已融forgetting缓解整段后/已知分类repair整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH2_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity](https://arxiv.org/html/2606.00271v1)

精确v1 §3/Eq1–19、§4/T1/A相关数值；当前momentum仅方向参考，per-tensor几何校正不补全异步收敛；模拟worker pace不是真WAN，高staleness同步更优/对MLA反退保留。 正式2+2+2=6，R180必要/actualowner具体已有覆盖通过；actual Arrival Bias与Stale Direction完整两段已承担arrival权重/方向reference、身份与错误reference压新域风险。不为新术语、细配置或marker制造书稿diff。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH2_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [GPTQ-intrinsic LoRA: A Near-optimal Algorithm for Low-precision Quantization with Low-rank Adaptation](https://arxiv.org/html/2606.01412v1)

精确v1 §4.2/Alg3、§4.3投影假设、§5/Alg4、§6/T1–3/C；增广H奇异需数值处理，fixed-grid/精确coordinate/同surrogate最优低秩才约束目标不增；infinite-grid谱界不授低bit或下游质量，DeiT反退保留。 正式2+1+2=5，R180/R184必要/actualowner与唯一实际POST通过；已融FLRQ完整第二段后/LoRaQ完整首段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH2_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Finer Parameter Steps for Low-Rank PEFT: A Controlled Study with CP Tensor Adapters](https://arxiv.org/html/2606.00428v1)

精确v1 §3–6/Eq1–7、raw与best-under-cap直接反侧；2048²的一步193是stored scalars非intrinsic DOF，CP方向受限；更多grid的事后max非独立选型，SST2饱和/BoolQ稍弱/RTE差距不删。 正式2+1+2=5，R180/R184必要/actualowner与唯一实际POST通过；已融完整参数比例段后/零初始化解释与代码整组前，初次锚误放已自修并由实际POST核当前正确位置。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH2_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [DSL-LLaDA: Scaling Continuous Denoising to 8B Masked Diffusion LMs](https://arxiv.org/html/2606.01024v1)

精确v1 §3–5/Alg1–2及必要训练/采样反侧；不是直接替换sampler，clean CE续训与converter/solver成套，Top词表/Heun/末端额外求值不授原联合分布；长参考、高NFE与开放创作可退步。 正式2+1+2=5，R181/R184必要/actualowner与唯一实际POST通过；已融RePlaid完整第二段后/球面endpoint完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH3_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Revise, Don’t Freeze: Sampler-Matched Training for Self-Correcting Masked Diffusion Language Models](https://arxiv.org/html/2606.01026v1)

精确v1 §3–5/Alg与A.4必要；每步重提block所有候选、不继承旧visible，selfcommit/mask用gold而非所有clean位置等权。未适配直接换sampler退步，sampler不匹配/更多步code反侧、末步强接收与EOS身份保留，不授corrector精确joint。 正式2+1+2=5，R181/R184必要/actualowner与唯一实际POST通过；已融DMax完整末成本段后/随机remask完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH3_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [WaveFilter: Enhancing the Long-Context Capability of Diffusion LLMs via Wavelet-Guided KV Cache Filtering](https://arxiv.org/html/2606.00724v1)

精确v1 §3–5/Eq与Alg B直接反侧；低频代理不是真语义或exactprefix，索引/伪码不闭不补recipe。Fast cache组合有明显TPS降低、任务质量退与层次/保留量非单调，不能拿相对dense倍数当继续加速。 正式2+1+2=5，R181/R184必要/actualowner与唯一实际POST通过；已融08086完整近似组及独立marker后/credit预测分布完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH3_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [EPIC: Efficient and Parallel Inference under CFG Constraints for Diffusion Language Models](https://arxiv.org/html/2606.00722v1)

精确v1 §3–5/必要算法及直接对照；local lexing复用/直接completion图parser降低检查成本，regular超集不授exact可完成。预算witness补全不保模型分布，近满syntax不是程序功能，简单grammar可慢/提前EOS与纯checker成本分账。 正式2+2+2=6，R182/R186必要/actualowner与唯一实际POST通过；已融00612完整可完成性组与独立marker后/DConstrain路径目标完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH4_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [FLARE: Diffusion for Hybrid Language Model](https://arxiv.org/html/2606.01774v1)

精确v1 §3–5/必要Eq、A.5/B/D设置与反侧；noisy block不能污染其它block/packed文档，diffusion暂态与AR accepted-prefix不共用错误live state。不同mix/任务仍退，held-draft概率strict条件不授便宜近似；A.5约4×per-input-token attention work非2×总work，source原笔误已定点纠正。 正式2+2+2=6，R182/R186必要/actualowner与唯一实际POST通过；已融04185双可见性完整marker后/CARD单流完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH4_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [SimSD: Simple Speculative Decoding in Diffusion Language Models](https://arxiv.org/html/2606.02544v1)

精确v1 §3–4/Eq1–5/T1–4必要；同时hidden间接影响使近似非lossless，接受/拒绝分布未由所写recipe证明，不补residual采样。高agreement非joint，CG基线/双卡FP32/batch1及decode排prefill分账，GSM/MBPP质量反退保留。 正式2+2+2=6，R182必要/actualowner具体已有覆盖通过；actual Temporal-causal Verification Layout同family两完整段已承担data/prediction、order/RoPE、额外KV和非精确fallback。不为新术语、细配置或marker制造书稿diff。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH4_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [BlockGen: Flexible Blockwise Sequence Modeling with Hybrid Samplers](https://arxiv.org/html/2606.02241v1)

精确v1 §3–5/必要训练与反侧；平均ELBO与mixture logsumexp bound非同成本/精确likelihood；ARPC额外size1前向评分不是真值verifier。D3只归masked/uniform在不同corrector/NFE的具体排名反转，不借数学标题；ARgreedy/高NFE整段更好与文本17.5/16.7算术错误隔离。 正式3+1+2=6，R182/R186必要/actualowner与唯一实际POST通过；已融完整fixed-blocksize段后/跨块overlap完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH4_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving](https://arxiv.org/html/2606.01839v1)

精确v1 §3–5/容量式及全部设置/反侧；0.6B四A40回放非30B真实Agent，decoder故意过配、AMPD模拟10%错误，0%等价及FullPD末turn TBT更好不删。容量仍依decode/驻留profile，原绑定/transfer先后不齐不补协议；R186撤无独立纠错对象的D3，正式6非原拟7，不因工作量/Books改分。 正式2+2+2=6，R183/R186/R187必要/actualowner与唯一实际POST通过；按R183明确收窄已融Conversation Placement首完整段后/pinning成本整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH5_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Leyline: KV Cache Directives for Agentic Inference](https://arxiv.org/html/2606.01065v1)

精确v1 §3–8/Limitations/T2及配置必要；amortize仅旋转Kpe、保后继Knope/V，不等删减文本re-prefill或完整旧prompt分布。policy gain用re-prefill而splice另微基准，未完成组成ablation；bf16不能替全部分歧免责，warmstart/tenant失败与峰内存不降保留。 正式2+2+2=6，R183必要/actualowner具体已有覆盖通过；actual Token Replay Identity三完整段与local repair/非prefix组已承担append/drop/repos历史、保旧影响/非隐私删除、分段恢复和引用生命周期。不为新术语、细配置或marker制造书稿diff。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH5_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Idleness is Relative: Exploiting Tool-Call Idle Windows for Offloading in Agentic Systems with MORI](https://arxiv.org/html/2606.00866v1)

精确v1 §3–7/Eq1/T1–2及全部设置；k5 phase比例非瞬时status，标签落KV节点后两tier相反优先，同类LRU；无容量压力不必然驱逐。186/200 trace闭环非真实生成成功，cap-H200非H100，平均TTFT/局部CPU开销非tail免费，未来tier不冒实现。 正式2+2+2=6，R183/R187必要/actualowner与唯一实际POST通过；按R183可能驱逐的收窄已融Idle Window首residency段后/成本段前，旧独立marker保留。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH5_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [CHIMERA: A Flexible and Scalable 3.1 TOPS/W AI-MCU with Transformer Accelerator and 563 Gb/s Shared-L2 Memory Subsystem with QoS Guarantees](https://arxiv.org/html/2606.02358v1)

精确v1 完整短稿I–III/T1–2/captions必要；多cluster扩展仿真与20k窄读实测分账，34cycle缺仲裁额度/流量条件不授WCET。3.19子系统/12mm²die、不同频压峰值及silicon-derived子模型执行不可拼全系统优势/质量，INT8无损未证。 正式2+2+2=6，R185/R188必要/actualowner与唯一实际POST通过；已融专用workload contract完整首段后/非线性专用单元完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH6_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Inner Product Aware Quantization: Provably Fast, Accurate, and Adaptive Algorithms](https://arxiv.org/html/2606.00289v1)

精确v1 §1–5、B/C证明、D.3/Table1/F.8必要；印相邻概率反写、Def3.1漏单位球不照recipe，B明确无偏和单位球支持窄数学对象。固定Q的worst=max坐标方差、average=输入二阶矩加权，仅独立类；minimizer非唯一，最坏1%事件可反弱，窄窗失效回全域、M4预处理不授GPU/LLM加速。 正式2+1+3=6，R185/R188必要/actualowner与唯一实际POST通过；已融完整INT4 outlier手算段后/PoT完整段前，原Q/DQ代码未拆。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH6_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Cram: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning](https://arxiv.org/html/2606.02502v1)

精确v1 §3–6/T1–6、A–H必要；几何新方向非未掌握能力，冻结旧centroid不冻结新expert加入后的归一竞争，soft penalty不保hard正交。gamma全组和/tildeV/冷启动未闭不补recipe；格式变换信息和预算/插入模块混杂、任务/OOD反退与全部pool成本保留。 正式2+2+2=6，R189/R190必要/actualowner与唯一实际POST通过；已融07494完整end后、ProtoAda前及原无taskdata子空间完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH7_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning](https://arxiv.org/html/2606.02576v1)

精确v1 §3–6/T1–3/A投影证明/B–D必要；task均值与单query、oracle/预测/group/协议人口分开，tokenid统计非tokenizer独立。投影最近点非语义兼容/保旧，T1实均46.928不采印47.23，预算混杂/顺序反退/periodic合并删残余及全部global/group/residual费保留。 正式2+2+2=6，R189/R190必要/actualowner与唯一实际POST通过；已融CRAM后/原无taskdata子空间完整段前。 细证与原提案见[本项必要包](../_sources/daily-20260603/SUP_CLOSE_BATCH7_20261025.md)；全部准备、选择/调用/执行与独立回归计费，未核实现或复现，不授普遍收益/生产SLO。

### [Regular-Activation Concentration: Characterizing Column-Level Output Sparsity Across Diffusion Model Architectures](https://arxiv.org/html/2606.00567v1)

精确v1 §2–6/T1–4必要及actual Ch49差额见[本项原证](../_sources/daily-20260603/SUP_CLOSE_00567_SOURCE_OWNER_20261025.md)。同column消费者跨M token作OR，跨denoise hotset身份另验；τ幅度与r目标hotfraction同数不同约束，阈值膨胀不等天然稀疏。跨架构形状关联非匹配因果；Jaccard恰1与hotset增长冲突，不采永久cold保证；reuse Y(t−1)与质量臂cold-zeroed非同operator，不合成联合quality-cycle点/固定安全τ。单GDDR/代表UNet block周期为模拟，N100 paired输出差异不是自然质量与真实安全。正式2+1+2=5，R191准入/联合日证、R192必要/actualowner及唯一收窄、R193唯一实际POST通过，已融Ch49共享representation两kernel完整费用段后/双稀疏SpMspV完整段前。Profile、threshold、逐步mask/重排/旧状态与真实生成回归全计费，保刷新mask/原布局/dense退路，未核像素/实现或复现；不倒填v2改题/提交记录。

## 5. 缺口与下一步

**无未处理的普通发现、必要证据或Books写入，R197最终日级独立验收通过。** 已处理144个新增家族：115真实整合与POST、23具体已有覆盖、2仅报告、1四分关闭、3中心争议；原2仅报告保持。末22具名与00567已闭，146既成层不第三Methods/行政PRE。00130原贡献N已更正为潜在参数化/压缩机制，R196确认公开区间跨日，有限日期层终态保留，不再普通续全文/Books。[有限停止原证](../_sources/daily-20260603/SUP_FINITE_STOP_20261025.md)与下列精确保留项不支撑正面证据或无遗漏保证。

- [00130 exact-v1](https://arxiv.org/abs/2606.00130v1)：root具体反例及reader决定性定义确认，层级小cores经非线性/侧向混合生成权重是直接参数化/压缩潜贡献，小模型/AlexNet/VGG不能作范围关闭。旧N撤回，非评分下降或已有覆盖。日期[精确原件](../_sources/daily-20260603/SUP_MODEL_EXTRA_NAV_20261023.json)同DOI/client=`arxiv.content`/state=`findable`/registered=`2026-06-02T03:44:18.000Z`，官方v1=`2026-05-28T19:43:10Z`，与适用EDT公告规则给可能公开区间Jun01 08:00～Jun02 11:44:18 BJT，跨Jun01–02，不能截取Jun02或以PDF封面补日证。R196只核官方LG六月页头/精确第6条（无日组）及一次题名+作者日期搜索，无可用primary receipt；不扩其余5233标题/假想渠道。HTML Aug24/PDF Jun02差异保留，不冒历史逐字；核心定点非完整必要层，不正式计146/评分/续Methods或Books，不用于正面保证。重开限该ID当批官方日公告、真实日组历史记录或作者可靠public release/快照以限定整个区间；若证Jun02只续该项必要/actualowner，若证更早留真实归属日恢复线索，不迁旧候选。

- [MODEL历史路由](../_sources/daily-20260603/SUP_MODEL_20261023.md)保原初提案与已读依据，当前以§3–4及R178–193为准：原余18与02358/00289/CRAM/ProtoAda全部已处置，00251/01629既成层复用。00567漏交接已R191–193必要/实际Ch49闭合，不再是待办。三中心争议及00382/01202未闭主张不作正面证据；七MODEL日期和AIMC另列保留。旧API/advanced失败不冒所有官方入口失效，真实月列表有限差额和停止复用，不扩全分类。
- [Agent/多模态历史路由](../_sources/daily-20260603/SUP_AGENT_MULTI_20261023.md)：所有已准入具名必要、具体NC或实际Books/POST已成，不重开原批次；01138实际整合、02536贡献前关闭有效，02494首发资格及五日期另列隔离。462主题导航不是全文分母；有限官方标题差额及相关六线索沿[已执行原证](../_sources/daily-20260603/SUP_OFFICIAL_TITLE_DELTA_20261025.md)和当前收束，不再将其写成未执行发现队列。
- 跨日资格保留的确切身份：MODEL 00024/00079/00093/00160/00003/00132/00091，Agent/Multi 00189/00135/00152/00094/00096，另02672 AIMC。其v1最早公开界至findable注册的可能区间跨BJT日期，不能只取Jun02注册或后版提交入窗。已执行的作者publication/project/代码README/官方abs有限恢复见[具名原入口](../_sources/daily-20260603/SUP_INFRA_NEXT_20261024.md)，00079还有作者May月份信号须消歧；当前均不评分/正式候选/Books，不证明必不在Jun02。只以当期官方ID公告、具可靠首发日的作者正文/历史快照或明确修订/纠错重开各自日期层，不扩全年或全部commit。

- [00334 Lexical Bias / Triangulated Preference Shift](../_sources/daily-20260603/SUP_MODEL_B6_SOURCE_20261024.md)：R167核当前arXiv相关FLAIRS DOI与同题作者/VoR入口，出版方登记online May06但官方article141843/galley147188正常入口403。它构成具名早正文渠道，登记/created不能冒首次可读正文，Jun02 arXiv日证亦不自动成为全文first-public。当前不评分/正式候选/Books，不迁已有日期；已读必要保留。只在取得该article/galley历史公开界、可读VoR或可核首发/窗内重要revision依据时重开，不扩全venue或用不可访问冒零命中。
- [02494 Monitoring Agentic Systems](../_sources/daily-20260603/SUP_MONITORING_EARLY_SIGNAL_20261025.md)：R160核实同题五作者的OpenReview cMZ4Z7u5B5及作者原站当前PDF渠道。May26会期/接受说明不证明正文当日公开；API403、验证页与作者下载无历史日期，无法确定是否早于Jun02。R62的Jun02 arXiv组合日证保留，但不自动证明全文first-public，也未证窗内重要revision。仅首次公开资格隔离，不正式计候选、评分/Methods或Books，不支撑Coverage/已审重复。定点恢复需这些具名正文渠道的原始public release、公开历史或作者/venue首发公告；只证明OpenReview当时非public不能自动关闭作者正文渠道。
- 00382仅报告中的中心桥、测量对象及FROZEN漂移冲突仍按§4隔离，不用于正面证据或整pipeline保证；与00376/00674/01451原争议分开保存。

- 原87/MetaPoint日期保留仍只旧隔离记录。当前合同允许有效联合日证；root已具名验证02643仍跨Jun02/03，不外推全部旧家族。只在具体新证据改变身份/日期或采用时重开，旧16I不直接计本轮成果。
- Google Research、Qwen与当前Meta历史目录：机构有限原始入口已执行，但无法恢复目标日可靠目录/日期。不能作零发布或正面Coverage；重开需目标官方日期目录、具名原始发布或可核历史快照。不因此扩全站/全年，不把当前壳或空搜索当无发布。MiMo官方Model Release已恢复Jun02的mimo-v2.5-asr具名事件及日期；该短核心只有识别能力宣传，缺新机制/受控设计取舍，具体贡献前排除，不评分/候选/Books、非待全文。MiMo其余Paper/Blog custom routes/CSR历史日期缺口仍保留，只以相应原始日期记录/可靠历史快照重开；已恢复一事件不作全源无遗漏保证。

00376/00674证明争议与01451测量争议仅按各自§4列示的原证/纠正条件重开，不用于正面Books或保证。官方advanced两次400及旧月列表路径404/cache miss见[原始执行范围](../_sources/daily-20260603/SUP_INFRA_NEXT_20261024.md)；新路径月列表已有真实有限恢复，二者不互相覆盖，更不证明目标日零发布，不循环相同失败。

窗外事件只作边界/真实归属恢复，不搬入Jun02；本日不新增其他Daily或Weekly，不恢复2025任务。年度其余未验日由各自独立上下文推进。

## 6. 复核

复核者：前批`jun03_org_supp`、`jun03_checkpoint_reader`、`jun03_resume_reader`、`jun03_next_reader`及root有效层分别复用；末22由root/R178–179及非writer `jun03_remaining_review`/R180–190完成必要、actualowner、具体NC/Only及所有真实POST，00567经R191–193完成。R194整日通过已由R195撤回，但其146全表/来源范围/有效链检查继续有效。R196更正00130贡献N并作有限跨日保留，R197已对真潜贡献更正与有限日期终态的实存差额一次读核，恢复日级验收；不复用R194的00130错误N，也不重146 Methods或行政PRE。

结论：通过

当前保存态：146已处理＝115实际整合、23具体已有覆盖、4仅报告（含2旧）、1四分关闭、3中心争议；00130不是贡献N，亦非确定本窗候选；R197已确认其跨日终态不支持正面采用。V3/本地引用及限定空白机械检查已通过，终存后再核不构成新研究轮；本轮直接核原两候选行及2994字符旧§4连续不变，旧27行/18098字符保护明确沿R21已有root快照实测，不冒重新全量字节比较。年度计数由root据本日实际完成另记，本日不维护跨日报数；格式不替语义完成或无遗漏保证。

最终依据为[独核R197](../_sources/daily-20260603/SUP_NEXT_REVIEW_20261024.md)：R194整体通过曾由R195撤回，R196更正00130潜贡献并完成有限跨日恢复，R197只核该真实保存差额后恢复本日日级完成。Coverage、Evidence、Books分别处理到安全终态；所有跨日/首发/目录/中心争议保留不取得正面保证。原146全表、必要/actualowner/唯一POST及已有效的来源范围核验复用，未重Methods或扩池。

### 历史复核与过程停点

以下保留当时范围与计数，不作当前待办或当前年度进度；最新状态只取本节开头、§1–5及当前canonical独核。

首8有效层见[独核R1–11](../_sources/daily-20260603/SUP_INDEPENDENT_20261023.md)，机构范围及RSS/pagination见[root R1–3](../_sources/daily-20260603/SUP_REVIEW_20261023.md)；01139/02320必要Source/真实POST和旧保存态见[checkpoint独核R2–5](../_sources/daily-20260603/SUP_CHECKPOINT_REVIEW_20261024.md)。本次[独核R1–16](../_sources/daily-20260603/SUP_RESUME_REVIEW_20261024.md)校准全部17个身份（15候选/2排除）、逐项核必要证据和owner，并在root真实保存后完整读14新增段/直接完整两侧/本人注。FineVerify映射、BFCL模型与PaW forward/梯度边界已据原文修正，00914采用精确PDF并保HTML日期差异，ForeSci从初筛RAG路由改实际Ch66。00756具体覆盖不造diff。没有借小批通过授整个来源/全池DAY。

原两候选字段与本轮恢复前12家族有效证据保留；本次新增已融入六部分与实际Books，未仅补引用。独立R17已通过当前27家族、真实Books状态及Report/2026 State/两源路由的窄保存态检查；V3、Report96个本地引用、State本2026任务块15个本地引用及限定working空白检查通过。root另按恢复前快照核原12行及连续旧§4前缀8705字符逐字保持；reader直接核HEAD两旧行/原窗口及旧§4子串，其余快照比较明确复用root实测。格式通过不证明全日完成、全仓清洁或实验复现。后批发现、筛选和研究仍普通待办，年度153/279不变。保护已有及2025并发修改/index，不stage、commit、push。

本次续跑25项由`jun03_next_reader`逐项校准准入/联合日期、必要Source与actualowner，并对23实际新增完成唯一POST（R20完成最后01927/01923）；R16以真实同family正文撤回02011重复PRE，R19据Ch42 alias收窄Ch50差额。当时52家族计数仅本批保存态，不是完整DAY；年度153/279不变。

本批R21已核前52家族保存态；此后B5三项01850/01806/01682已依R22–28落实，CANARY/TriAlign/DOT三项经R30–33完成必要证据及实际Books/POST，此后三项AlphaToken/ProbMoE/TwinQuant经R37–42实际闭合；余51仅准入/日期通过，不把题摘读完计为Evidence/Books完成，日报仍进行中、年度153/279不变。

OptCC R34–35首次必要及实际POST通过，当时59家族/51I；原alias与旧trace保持，年度153/279不变，本日仍普通推进未DAY。

AlphaToken/ProbMoE/TwinQuant分别经R41/R42唯一实际POST生效，当前62家族/54I已同步；普通发现/必要/Books仍在，不授DAY或增加年度计数。

01464 R43/45必要及真实Books/POST已闭，当时63唯一家族/55I，余50 MODEL必要层和其他普通待办继续；本日未DAY，153/279不变。

01138原N由R47具名反侧纠正，经R50实际POST已融当前64家族/56I；02536 R46具体贡献前关闭，仅原始筛选记录保留，不评分/候选/Books。本日仍未DAY，153/279不变。

01451经R52必要/owner争议判断融为65家族/56I；R51只完成00476/02031准入/date，01436必要包已交首次独核，均不预记Source完成或Books。R53核64保存态的旧63时态已改“当时”，未重审有效正文；本日仍未DAY，年度153/279不变。

01436经R54必要/owner/原PRE与R55唯一实际POST融为66家族/57I；01451中心测量争议按R52隔离，MODEL普通必要余48。00476必要包已交首次独核、02031仅准入/date通过，仍有普通发现/研究，未DAY，153/279不变。

R57只核66/57I保存态与01451精确题名及01436注同步；随后00476 R56/58真实闭合融当前67/58I，Agent普通余24，02031必要包待首次独核，MODEL余48及其他普通继续。未DAY，153/279不变。

02031经R59/61实际闭合融当前68家族/59I；R62只完成Agent/Multi余23的具体贡献/Jun02联合日证，不是评分、当前notice、必要Source/owner或Books完成。MODEL余48及发现/资格仍普通，年度153/279不增，本日未DAY。

01400经R63/65、01387经R66/68实际闭合，01281 R69/72与00299 R70/73亦已实际闭合，01168经R74/77实际闭合，01155 R78具体已有覆盖后，当前81家族/71I/5具体NC，原MODEL必要余40、Agent/Multi余18；四定义新准入/日证已在MODEL路由末节校准，尚未必要Source，不与该40混计。R64确认七日期项有界原入口补查与资格隔离、00079早稿信号保留，未确认Jun02、不授全部恢复穷尽或DAY；原件与定点重开见有限恢复末节。

00997经R97必要/六分/原单PRE与R99唯一实际POST闭合；81唯一家族/71I，MODEL必要余40、下一00946首次独核中，Agent/Multi余18、下一01380首次必要独核中。原有效层及153/279日级计数保持，本日未DAY。

00946经R100/102、01380经R101/104实际闭合后当前83唯一家族/73I/5具体NC；MODEL余39下一00888，Agent/Multi余17下一01285首次必要中。此前计数是分批快照，不授DAY或增加153/279年度计数。

00888 R105与01285 R107必要及actual-owner具体已有覆盖通过后，当前85唯一家族＝73实际I/7具体NC/2旧Only/1四分关闭/2中心争议；MODEL余38下一00846，Agent/Multi余16下一00515。没有新增Books或POST待办，普通发现/必要层仍在，未DAY、153/279不增。

00846 R108/111实际Ch66与00515 R109具体已有覆盖通过后，当前87唯一＝74实际I/8具体NC/2旧Only/1四分关闭/2争议。MODEL余37下一00819、Agent/Multi余15下一01914仍普通必要；年度153/279不变，未DAY。

00819仅R112批准的限界修后单段经R114真实POST生效，当前88唯一/75I/8具体NC；MODEL余36含00813 R115必要/五分/原单PRE，待root实际保存；Agent/Multi余15含01914首次必要提案待独核，日级153/279不变，未DAY。

00813 R115/117与01914 R116/118的必要/PRE及唯一实际POST已成，当前90唯一＝77实际I/8具体NC/2旧Only/1四分关闭/2中心争议。MODEL原余35下一00801，Agent/Multi余14下一01600；普通发现与必要层继续，年度153/279不变，未DAY。

00801 R120具体已有覆盖与01600 R119/121实际Ch25成链后，当前92唯一＝78实际I/9具体NC/2旧Only/1四分关闭/2争议。MODEL原余34下一00735，Agent/Multi余13下一00232；有界官方标题差额及首次准入/date校准见[当日补检](../_sources/daily-20260603/SUP_OFFICIAL_TITLE_DELTA_20261025.md)，未预确定两拟项或扩整类队列。年度153/279不变，未DAY。

00735 R124/126与00232 R125修后稿/R127真实POST后，当前94唯一＝80实际I/9具体NC/2旧Only/1四分关闭/2中心争议。MODEL原余33下一00674，Agent/Multi余12下一01027；R122–123已通过新增01472/01542完整题摘与Jun02联合日证，仅必要/评分/owner仍普通，未计本94。外部有限保留与原字段不变，年度当前154/279（06-04另日已真实验收），本日未DAY。
00674经R128首次必要/正式6分/actual Ch31与中心争议隔离通过，当前95唯一＝80实际I/9具体NC/2旧Only/1四分关闭/3中心争议。MODEL原余32下一00654；01027 R129必要/PRE已通过且root原单段已实际保存，唯一POST普通待办，未预I。年度154/279不变，本日未DAY。

01027经R129必要/正式六分/原单段PRE及R130唯一实际POST生效，当前96唯一＝81实际I/9具体NC/2旧Only/1四分关闭/3中心争议。Agent/Multi原余11下一00959；MODEL原余32下一00654。日级年度154/279不增，普通发现/必要/Books继续，本日未DAY。

00654经R131必要/六分与actual Ch72同family具体已有覆盖生效，当前97唯一＝81实际I/10具体NC/2旧Only/1四分关闭/3争议。MODEL原余31下一00651，Agent/Multi原余11下一00959首次必要中；154/279不变，本日未DAY。

00959经R132必要/六分/原两段PRE与R133唯一实际POST生效，当前98唯一＝82实际I/10具体NC/2旧Only/1四分关闭/3争议。Agent/Multi原余10下一00804；MODEL原余31下一00651。原27行/连续18098字符旧§4本轮复算均保持，300本地引用路径存在（新增00959链接另验），V3仅机械；154/279不增，本日未DAY。

00651 R134/136实际Ch21与00804 R135具体NC生效，当前100唯一＝83实际I/11具体NC/2旧Only/1四分关闭/3争议。MODEL原余30下一00600，Agent/Multi原余9下一01770；其他具名准入/发现普通缺层保留，年度154/279不增，本日未DAY。

00600 R137/139实际Ch66与01770 R138/140实际Ch84生效，当前102唯一＝85实际I/11具体NC/2旧Only/1四分关闭/3争议。MODEL原余29下一00570，Agent/Multi原余8下一01212；新01472必要/拟5与actual Ch74具体NC已交首次独核、01542仍普通必要，未计102。年度154/279不变，本日未DAY。

01472经R141首次必要/正式五分/actual Ch74三组具体已有覆盖通过，当前103唯一＝85实际I/12具体NC/2旧Only/1四分关闭/3中心争议。01542必要层仍普通；MODEL原余29下一00570、Agent/Multi原余8下一01212未变，年度154/279不增，本日未DAY。

00570经R142正式六分/原单段唯一修句PRE与R143唯一actualPOST生效，当前104唯一＝86实际I/12具体NC/2旧Only/1四分关闭/3中心争议。MODEL原余28下一00544，Agent/Multi原余8下一01212必要准备；01542必要/五分/actualCh76原单PRE交首次独核。年度154/279不增，本日未DAY。

01542经R144五分/修后单段PRE与R145唯一actualPOST生效，当前105唯一＝87实际I/12具体NC/2旧Only/1四分关闭/3中心争议。01212必要/拟六分/actual Ch76原单PRE已交首次独核；MODEL原余28下一00544未开始。年度154/279不增，本日未DAY。

01212经R146六分/修后单段PRE与R147唯一actualPOST生效，当前106唯一＝88实际I/12具体NC/2旧Only/1四分关闭/3中心争议。Agent/Multi原余7下一02060；MODEL原余28中的00544必要/拟六分/actualCh27原两PRE已交首次独核。年度154/279不增，本日未DAY。

00544经R148六分/两条件修后PRE与R149唯一actualPOST生效，当前107唯一＝89实际I/12具体NC/2旧Only/1四分关闭/3中心争议。MODEL原余27下一00539、Agent/Multi原余7下一02060均已准备首次必要/具体NC，交独核；其后00516尚未开始。年度154/279不增，本日未DAY。

00539 R150与02060 R151分别经首次必要/正式六分/实际同family正文具体NC，当前109唯一＝89实际I/14具体NC/2旧Only/1四分关闭/3中心争议。MODEL原余26下一00516、Agent/Multi原余6下一01166尚未必要，其他具名普通层仍在；年度154/279不增，本日未DAY。

00516经R152正式七分/必要补层与actual Ch56同family三段具体NC通过，当前110唯一＝89实际I/15具体NC/2旧Only/1四分关闭/3中心争议。MODEL原余25下一00426；Agent/Multi原余6中的01166必要/PRE待首次独核。年度154/279不增，普通未完，本日未DAY。

01166经R153正式六分/原两段PRE与R154唯一actualPOST生效，当前111唯一＝90实际I/15具体NC/2旧Only/1四分关闭/3争议。Agent/Multi原余5下一02553；MODEL原余25中的00426必要/拟六分/actual Ch36两段PRE交首次独核。年度154/279不增，本日未DAY。

00426经R155正式六分/原两段PRE与R156唯一actualPOST生效，当前112唯一＝91实际I/15具体NC/2旧Only/1四分关闭/3争议。MODEL原余24下一00392；Agent/Multi原余5中02553必要/拟六分/actual Ch25两段PRE交首次独核。年度154/279不增，本日未DAY。

02553经R157正式六分/原两段PRE与R158唯一actualPOST生效，当前113唯一＝92实际I/15具体NC/2旧Only/1四分关闭/3争议。Agent/Multi原余4下一02494；MODEL原余24中00392首次必要/拟五分/actual Ch33具体NC交独核。年度154/279不增，本日未DAY。

00392经R159首次标准必要/正式五分与actual Ch33具体已有覆盖通过，当前114唯一＝92实际I/16具体NC/2旧Only/1四分关闭/3争议。MODEL原余23下一00382；02494因新具名更早OpenReview正文渠道仅重开first-public资格，尚未Methods/评分，不搬旧候选；Agent其后02459等尚未必要。年度154/279不增，本日未DAY。


00382经R161标准必要/正式五分及仅报告采用，中心桥和测量冲突明确保留；02494经R160仅first-public缺口隔离，不进正式候选。当前115唯一＝92实际I/16具体NC/3Only（含2旧）/1四分关闭/3争议；MODEL余22下一00365，Agent余3下一02459。两项R162/R163只是必要与PRE，尚无实际SAVE/POST，不计I。年度154/279不变，本日未DAY。

00365 R162必要/PRE、R164落位失败定点修复后R165实际POST，以及02459 R163/R166实际POST均已采用。当前117唯一＝94实际I/16具体NC/3Only（含2旧）/1四分关闭/3中心争议；MODEL余21下一00334，Agent余2下一02449。原27行/连续旧证据保持，不把保存落位修复当新机制审阅或重跑依据，年度154/279不变，本日未DAY。

02449经R168正式五分/actualCh66具体NC采用，当前118唯一＝94实际I/17具体NC/3Only（含旧2）/1四分关闭/3中心争议。00334 R167仅具名FLAIRS首正文资格隔离，非正式候选/评分；MODEL余20下一00306，Agent余1下一02436必要/PRE待首独核。年度154/279不变，未DAY。

02436经R169正式六分/原两段PRE与R170唯一actualPOST采用，当前119唯一＝95实际I/17具体NC/3Only（含2旧）/1四分关闭/3中心争议。Agent/Multi原具名必要余0，有限发现/整体清单尚需收束；MODEL余20含00306必要/拟六分/actualCh29单段PRE交独核，四定义/CRAM/ProtoAda仍普通。年度154/279不变，未DAY。

00306经R171/R173实际Ch29、02430经R172/R174实际Ch49采用，当前121唯一＝97实际I/17具体NC/3Only（含旧2）/1四分关闭/3争议。MODEL原余19下一00251，三定义01629/02358/00289与CRAM/ProtoAda仍普通；Agent具名必要余0但有限发现收束未日级验。V3机械与原旧证据保护另核，年度154/279不增。
