# 2025-12-01 增量来源补查

最新恢复（2026-10-07 17:00前后）：Sartre16:24修后定点确认已经返回，仅通过DeepMind修正，不授全日完成。用户最新禁止catchup；下文15～16时的catchup请求只保留历史执行事实，不能继续用90天限制阻止查漏。新增Advanced/API/月表实际请求、身份差额、停止范围及待非作者校准见[本日续跑记录](./history-discovery-20261007.md)。本记录旧“未返回”“当前边界”均按当时停点理解，最新状态以该续跑记录与README为准；未覆盖旧原件。

作者执行：2026-10-07T15:10:25+08:00 起；本记录包含15:38～15:44的官方动态目录继续恢复与实际校验，及16:02的首校准响应。Sartre首校准已收到，修后非作者确认与日级最终验收未返回。

## 范围与保留边界

只拥有本日 README 与本目录原件；补充窗 **2025-11-30 ～ 2025-11-30**。用户授权只补遗漏，原窗 Nov30 09:00～Dec1 09:00、原候选/保留项、公开时间、归属和有效审阅全部保留。没有把 SCONE、DeepSeek 或原 arXiv 保留项按新日期规则重新归属；原日程推导不授新材料公告日。

已重读主工作区 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES 每日组及 arXiv 使用说明、Prompt、ROADMAP，LEARNING_STATE 只定位本轮授权与本日 ownership。已读本日旧 README 全部材料和旧七份来源/筛选/复核记录。旧完成不是本轮完成；旧来源观察仅用于定点恢复入口，不充当本轮扫描。

原件位于 [supplement-20261007](./supplement-20261007/)。以下请求均实际执行；curl 保存响应正文，HTTP 200 仍检查内容、日期口径、错误与分页。网络失败没有原件时在此明记。执行过程中未 stage/commit/push，未写合同、脚本、月索引、State 或 Books。

## 14 源实际范围与停止点

| 来源 | 实际入口、查询/分页、原件与停止位置 | 作者结果及边界 |
| --- | --- | --- |
| SRC-OPENAI | `https://openai.com/news/rss.xml` → `openai-rss.xml`；XML parser 实际 1251 items，只提取目标日期与相邻段。相邻 Nov26 Mixpanel / Dec1 五条；另执行 `site:openai.com/index "November 30, 2025"` 首轮 | 该 RSS 的 Nov30 切片没有 item；不是全机构无论文。搜索返回后来的 Cyber Special Operations 文中观察日期以及 community 用户帖；日期字符串不是发布日期，community 不作研究来源。Mixpanel 为 Nov26 已知安全事件，不移入本窗。 |
| SRC-ANTHROPIC | Research HTML → `anthropic-research.html`；读取内嵌 publicationList 的 Nov25、Dec1、Dec2 连续段；`site:anthropic.com/research "November 30, 2025"` 首轮 | SCONE `publishedOn=2025-12-01T00:00:00.000Z` 仍是旧保留项，未改其日期或结论。当前保存的相邻目录没有 Nov30；不等于全机构召回。 |
| SRC-GOOGLE-AI | DeepMind `?page=3`原件实际首页30卡，16:12前web默认页再核Nov21/Dec3邻接；Google Blog curl失败后web实际1/9页至Nov12；pubs早次年入口失败，后默认web恢复1–15/11597、2025选项678，年参数仍Internal Error；默认curl25秒timeout，CUA无可用浏览器；两个官方域主题日期首轮补检 | 伪分页未生效；默认pubs已恢复，不再称全目录不可达。678是年份选项数，不授本次过滤成功或日公开。目标日历史切片/具名首公开仍缺，错误/成功分开保存。没有遍历9页/265/678条，详见16:12恢复记录。 |
| SRC-META-AI | Publications `?content_types%5B0%5D=publication&page=4` curl 先 connection reset、后30秒 timeout；web 原站实际恢复第4页，读取 Dec16/Dec12/Dec1 AdvancedIF/Nov19～Nov10 连续段；`site:ai.meta.com "November 30, 2025"` 首轮 | 具体段没有 Nov30 条目。AdvancedIF 是旧目录收录/去重证据，不改原归属；未读2021等被混排旧项，不把第4页等同全站完整历史。 |
| SRC-QWEN | 旧站、新站 `/blog`、`/research` → `qwen-old.html` / `qwen-new.html` / `qwen-research.html`；旧站第一页止 Sep23；官方域收窄搜索两轮仅辅助。15:38以后继续按真实部署恢复两条前端数据流：`qwen-articles.json` 40条、`qwen-research-list.json` 60条，路径/id重合7，合并93身份；日期元数据全部可解析，无missing，Nov13/Dec5邻接 | 撤销此前“目录未恢复”阻碍；只检查这两响应的目标日期切片及相邻段，未见Nov30，不声称全机构无论文。接口返回正文不等于已读93篇题摘/正文；查询与版本原件见下面恢复详情。 |
| SRC-DEEPSEEK | 官网与 API Docs `/news/news251201` → `deepseek.html` / `deepseek-dec1.html`。15:38以后 `/news/` → `deepseek-news.html`，实际Research10条，Dec2 V3.2/Nov27 Math-V2相邻；News嵌入10条，Dec1/Sep29相邻；具名 `/news/deepseek-v3-2/` → `deepseek-release-web.html`，metadata/正文Dec1 | 撤销此前“当前官网不提供历史目录”描述；已读当前News/Research相邻段，未见Nov30。不把Research列署日改作arXiv官方首公告，不把具名Dec1日期强加给原DeepSeek保留项。只认证这个有界目录，非全机构历史。 |
| SRC-MOONSHOT | `/blog` 全 Overview 26条 → `kimi-blog.html`；链接 `/blog/posts/changelog` 全页 → `kimi-changelog.html`；`site:platform.kimi.com "2025年11月30日"` 首轮 | Overview 最新 Nov7、最末 May29 2024；changelog 最新 Nov6、最末 Apr30 2024。两者本窗无条目，不外推机构论文。误试 `/docs/pricing/chat` → `kimi-recovery.html` 是非研究恢复路线，不计来源覆盖。 |
| SRC-TENCENT-HUNYUAN | 首查 Research → `hunyuan.html` skeleton；隐藏浏览器创建实际30秒 timeout。部署 `index-I3I3bCf9.js` → `hunyuan-app.js`，恢复官方 `/api/blog/publicList`；POST `{"pageNum":1,"pageSize":20,"renderType":0}` → `hunyuan-list.json`，code0、totalNum9、实际list9、全为2026，最早 Feb3。官方域 Nov30及 November2025 首轮搜索；OCR原页探测 → `hunyuan-ocr.html`（当前只有壳），另 GameCraft-2 项目具名恢复 | 当前响应9条并非旧记录11条，保留本轮真实分母；没有把变少当历史覆盖完成。2025 Research 目录缺失，需历史All段/原公告。搜索恢复的 HunyuanOCR Nov25 只作窗外线索，不借它填 Nov30；GameCraft-2见下方题摘筛选，未因本源缺旧目录省略它。 |
| SRC-ZAI | 首查 Research 及 `?page=2` → `zai.html` / `zai-page2.html`；第一页15、第二页18并显示“没有更多”，最早 Dec7；release原页 → `zai-release.html`，Sep30/Dec8；`site:zhipuai.cn/zh/research "2025" "11" "30"` 首轮 | 当前目录未保留 November；release相邻段未见本窗事件，但不证明旧Research零事件。搜索被投资者/新闻与当前应用命中污染，未拿企业新闻替代研究页，历史目录仍受阻。 |
| SRC-BYTEDANCE-SEED | `/en/public_papers` 1/13页 → `seed-papers.html`；从部署 `main.897993d4.js` → `seed-main.js` 核 GET `/api/get_article_list_v2` 调用。参数 `article_type=1,publish_year=2025,count=20,page_token=0,order_desc=true` 初响应 `seed-paper2025.json` 有total94但无list，不能当空；实际按前端调用加 `x-tt-locale: US` → `seed-paper2025-us.json`，返回18条、total94、has_more true、next token20，Dec15/Dec2/Oct22。type2同参数 → `seed-blog2025.json`，15条、total49、next20、Dec2/Nov27/Oct23。辅助 `site:seed.bytedance.com "Nov 30, 2025" OR "2025-11-30"` 首轮 | 只读至跨窗邻接段，停止于token0，不展开剩余94/49条。两个类型均跨过本窗；不能把无 locale 的缺失list或成功状态当零论文。按前端日期编码解释自然日，没有时分秒门限。 |
| SRC-BAIDU-ERNIE | Blog `/blog/zh/` 第1页及其 `/page/2/` 第2/2页 → `ernie-page1.html` / `ernie-page2.html`，Dec9/Nov21相邻、第二页最早Jun30；`site:ernie.baidu.com "2025年11月30日"` 首轮 | 两页 Blog 已核，本窗没有条目；第二页还含Nov11，不仅旧记录所述Nov7。未扩扫普通提交或机构全论文。 |
| SRC-XIAOMI-MIMO | 首页Paper8、Blog15（More只展开已在HTML中的7条）→ `mimo.html`；部署4752 → `mimo-routes.js`，route自有日期HSS Dec19、Safety Dec18，Flash无date。15:38官方 `/blog/` → `mimo-blog.html` HTTP200，Flash正文明确Dec16 2025；另当前部署入口 → `mimo-index.js` | 撤销“More下一页未恢复”隐含判断；本轮15条身份已包括折叠内容。Paper Oct21/Jan8邻接已核，Flash具名日期已恢复，无须借HSS日期。仍有无date路由，当前目录不证明2025 November历史完整；未泛读2026工具纠错或全部iframe附件。 |
| SRC-MINIMAX | 英文 `/blog` 全13项 → `minimax.html`；中文 `/blog` 跳转至当前中文目录，全13项 → `minimax-zh.html`；`site:minimax.io/blog "November 30, 2025" OR "2025-11-30"` 首轮 | 两目录均见Oct27/Dec23相邻段，中文另有Jan15；当前Blog本窗无条目。未触发Agent Tech Blog具名事件，不扫描周级或全仓库提交。 |
| SRC-ARXIV | 详见下一节：四主题辅助查询、实际表单错误/粒度核验、日列表/catchup、Atom API、月列表有界探测、八份精确v1题摘及必要具名原件 | 必要历史公告日批次仍受阻。未把参数、HTTP200、submitted、DataCite、Updated:v1、月份、公告日程或模型仓库创建时间转成公开日。 |

## web 原站恢复观察与辅助搜索边界

2026-10-07 15:16～15:18 +08:00，Meta [第4页](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=4) web 原站恢复的日期/题名段为：Dec16 Audiovisual Perception → Dec12 Text-Guided Semantic Image Encoder → Dec1 AdvancedIF → Nov19 SAM 3D/Body/SAM3 → Nov18 Souper-Model → Nov11 CATransformers → Nov10 Omnilingual ASR。Google [2025 Blog第1页](https://research.google/blog/2025/)恢复的邻接为 Dec3 auditory benchmark → Nov21 EV port availability → Nov19 speech translation → Nov18 Generative UI；本页末 Nov12 JAX-Privacy，显示1/9。这些是本轮实际原站结果，不是复用旧notes；curl失败与web成功权限分开。

上述13源的检索分4批，执行约15:13～15:17。每个查询只一轮，未分页；搜索引擎没有提供有效原站日期过滤保证。只作漏项恢复，空响应/无相关命中不授原源覆盖。第一批 OpenAI 返回社区用户帖及后来文章中的观察日期，第二批 Qwen 混入用户分享，第三批 Z.ai 混入企业新闻，均不采为官方研究事件。没有为搜索首页建立零事件断言。

### 校准等待期间的明确局部恢复（15:38～15:44 +08:00）

- Qwen：web打开`https://qwen.ai/research`与`/blog`均0行，没有以此结束。实际从已保存HTML的部署基址`https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/`请求`p_home-index.js`、`main.js`、`p_layout.js`、`p_research-index.js`、`5fb222f6.js`、`2766.js`、`969.js`，全部HTTP200。保存对应`qwen-*.js`，最后969模块44467明确`cy=/api/v2/article/retrieval`、`fA=/api/page_config?code=research.research-list`；Research页面GET传`type=qwen_ai,language=en-US`，不是自行猜分页/日期参数。
- 实际GET `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`，按部署加`X-Request-Id: 86cf08be-53e4-4c41-8967-f67490f18bc2`：HTTP200、`success=true`、`data.articles`40条、4781799字节，保存`qwen-articles.json`。另GET `https://qwen.ai/api/page_config?code=research.research-list`，请求id`1f280811-e3e5-4076-b6d2-47246f0d91ba`：HTTP200、根数组60条、57428字节，保存`qwen-research-list.json`。后者不是success/data对象；首次parser误假定对象而报TypeError，已按实际数组重解析，不以异常当空。两流按path/id重合7、合并93个身份，仅做日期切片，不建立93篇贡献队列。
- Qwen文章流日期范围2025-11-13～2026-09-20；配置流2022-11-14～2025-12-23，全部日期可解析。原始ISO字段按北京时间自然日解释，仅用日期不核时分秒，Nov13 DeepResearch → Dec5 SAPO/TTS update相邻，未见Nov30。题名`Qwen3-Omni-Flash-2025-12-01`的自身字段为Dec9，`qwen3-tts-1128`为Dec5，不从型号/slug造发布日期。合并之外未声称存在全面召回保障，也未读接口自带的全部正文。
- DeepSeek：GET `https://www.deepseek.com/news/` HTTP200、113863字节，保存`deepseek-news.html`，真实News页面chunk与内嵌posts10条；Research实际展示10条，Dec2 V3.2 → Nov27 Math-V2 → Nov1 LPLB邻接。具名GET`https://www.deepseek.com/news/deepseek-v3-2/` HTTP200、125627字节，保存`deepseek-release-web.html`，可见正文、`article:published_time`和frontmatter均Dec1。只恢复日期/身份，不采用其性能宣传或改旧日期。另猜测`/research/`404、45549字节→`deepseek-research.html`，不是成功空目录，不把这个无效路由当新增必要外部阻碍。
- MiMo：web原站`https://mimo.xiaomi.com/blog/`恢复具名Flash正文，随后curl同URL HTTP200、29415字节→`mimo-blog.html`。h1是Introducing MiMo-V2-Flash，可见time文本明确December16,2025，而dateTime属性仅`2025-12`，日证据取可见官方正文，不取月字段。当前部署`index.c5195ace.js` HTTP200、22556字节→`mimo-index.js`。已有`mimo.html`的`blog-more`内确实包含编号09～15七条，More按钮`aria-controls=blog-more`/`aria-expanded=false`是展开已有内容；撤销未翻下一页的描述。仍不把其他无date的route强行按相邻项归日。
- Hunyuan：实际部署Blog chunk `index-CUQAWQeM.js`（10220字节）与API chunk `index-cEoitnb7.js`（429字节），两者HTTP200，保存`hunyuan-blog.js`/`hunyuan-api.js`。后者核POST`/api/blog/publicList`；前者明确`renderType0=allTab,1=paperTab,2=modelTab`、列表传`pageNum/pageSize/renderType`。因此原已执行renderType0确实是All，不再用猜测参数当生效过滤。当前All响应total9/list9只剩2026，2025历史恢复仍无证据；不扩全组织仓库。
- Google pubs的web原站恢复`https://research.google/pubs/?year=2025`也返回不可访问，与本轮curl timeout分别记录；不因DeepMind/Blog已成功而给pubs授覆盖通过。本次本机缺bs4，结构检查改用标准HTMLParser/JSON parser，不安装依赖、不改项目脚本。

## arXiv 查询有效性与停止位置

1. `language model` Advanced，`from_date=2025-11-30,to_date=2025-12-01,date_type=announced_date_first,size=50,order=-announced_date_first` 实际 HTTP200，`arxiv-advanced.html` 显示 **1–50/3481**，首项2511.23478，v1 Nov28提交、originally announced November2025。这不是日级过滤：只把首屏作为有界线索，发现实际放宽后不翻其后3431项；只恢复下表八份精确v1。页面上的后续版本摘要不能代替v1（Video-R2、Price of Progress、GameCraft-2均存在后来版本）。
2. 同一查询改 `from_date=to_date=2025-11-30`，实际 HTTP200，`arxiv-sameday.html` 有 **End date must be later than start date**，不是成功的零结果。帮助明确 announcement date 只有 year/month，排序用原v1公告年月。已按root告知定点实核；不能靠另换order名称授日。
3. `/catchup/cs.CL/2025-11-30` 和 `/list/cs.CL/2025-11-30` 均 HTTP400，保存 `arxiv-catchup.html` / `arxiv-daylist.html`，**错误路径的400本身不证明历史恢复不可行**。因此继续实际取 `/catchup` → `arxiv-catchup-form.html` HTTP200，读官方form：GET `/catchup`、字段subject/date/include_abs、date为YYYY-MM-DD；实际正确请求 `/catchup?subject=cs.CL&date=2025-11-30&include_abs=True` → `arxiv-catchup-correct.html` HTTP400，原文明确 **Catchup only allowed for past 90 days**。邻接Dec1正确请求同样400 → `arxiv-catchup-adjacent.html`。这才是当前必要2025日批次的具体外部恢复边界，不是参数未核或日期缺秒。Atom `export.arxiv.org/api/query` 本轮 HTTP500，保存 `arxiv-api.xml`，不是旧轮429。请求为 `all:"large language model" AND submittedDate:[202511290000 TO 202512010000]`, start0,max25,sort submittedDate descending。即使取得该提交切片，也仍需首公开证据；错误响应不授零命中。
4. 四主题辅助查询均一轮、无结果：`site:arxiv.org "30 Nov 2025" (transformer OR "language model" OR MoE OR pretraining OR optimization)`；同日期 `(GPU OR kernel OR distributed OR inference OR cache)`；同日期 `(multimodal OR "world model" OR "vision language action" OR diffusion)`；同日期 `(agent OR retrieval OR evaluation OR reinforcement)`。仅说明辅助索引受限，未把摘要没有精确日期字符串等同无公告。
5. `/list/cs.CL/2025-11?skip=0&show=25` → `arxiv-cl-nov.html` 实际1–25/1527，**从2511.00010开始，是月初，不是月末或11-30日批次**。后续只定点末25 `skip=1502&show=25` → `arxiv-cl-nov-end.html`，实际1503–1527/1527从2511.21398至2511.23473，全部cross-list（末项ThetaEvolve），亦不是11-30日批次或原生分类日列表。只核目录顺序/边界，不翻中间页，不把两个探测页50题名作当日逐项关闭队列。月初页面具名撤回2511.00115已打开当前abs → `withdrawn-personality.html`，确认为撤回，排除采用链路；未给其月份或提交字段造日。不是对这些题名完成贡献筛选或对12分类完成覆盖。
6. 原已有 CourseTimeQA 2512.00360 当前abs再次实核 → `coursetime-current.html`，仍明确检索测量错误导致表格及中心数字失效、v2撤回。保留原排除理由，不当访问故障；本次不评分或Books。旧A-CC/Threshold/QA47等有效安全/反证理由未变，只复用旧原件，不谎称本轮重读全部附件。

当前缺的是目标日期相关的官方历史 **new/announced日批次** 或可核实作者首次正文发布，不是更精确的提交时分秒。没有DataCite/日程推导替代。若root取得真实批次，只重开受影响身份与主题；不要按这次失败查询制造全月任务。

## 八份新恢复题摘及首批校准材料

以下八份均实读完整精确v1题摘/当前abs状态字段。只是在放宽的检索首页恢复的身份；尚不能确认为补充窗材料，不进入确定候选、评分、性能证据或Books。定点查 Nov28/29/30 与本日README未见这八ID；不是全仓库去重完成。潜在理由明确即停止；不得因日期受阻或Books有主题而删除。

| 身份/原件 | 约束 → 原文具体增量 → 待核设计选择 | 作者初筛/校准问题 |
| --- | --- | --- |
| [Video-R2 2511.23478v1](https://arxiv.org/abs/2511.23478v1)，`arxiv-2511.23478v1.html` | 视频推理答案正确不保证过程依赖视觉 → TAC/VAS分开诊断答案一致与视觉依赖，时间戳SFT与Temporal Alignment Reward → 评价和训练是否应显式约束时间grounding | 潜在准入，不能把11个benchmark的局部反证排除。需独立校准后才能审指标可识别性、奖励/预算对照；v1说将开源，不借v2已开源反填。 |
| [Video-CoM 2511.23477v1](https://arxiv.org/abs/2511.23477v1)，`arxiv-2511.23477v1.html` | 一次编码后纯文本推理不能重新取视觉证据 → 可重看/聚焦的视频操作序列和step-level reward → 视觉证据获取能否成为可学习执行动作 | 潜在准入，不按Agent流程组合直接关闭。需操作/奖励消融及总取证成本；官方README API原件无发布日，不能由当前release文字授11-30公开。 |
| [WMAct 2511.23476v1](https://arxiv.org/abs/2511.23476v1)，`arxiv-2511.23476v1.html` | 依赖多轮环境反馈的策略未必能内化动力学 → 按行动有效性重标奖励、退火可用交互次数 → 减少外部观察是否训练出可迁移的状态推理 | 潜在准入。只保留Sokoban/Maze/Taxi局部机制检验，不把一轮任务成功直接当真实world model或物理安全。 |
| [ThetaEvolve 2511.23473v1](https://arxiv.org/abs/2511.23473v1)，`arxiv-2511.23473v1.html` | 纯推理演化只在数据库保存策略 → test-time RL与程序库探索并行，训练checkpoint在目标/未见任务比较 → 参数更新能否内化而不只是增加搜索预算 | 潜在准入对象是训练/搜索机制，不因数学任务或小8B模型关闭。代码README API原件无first-public日；新bound不是机制归因证明。 |
| [VGT 2511.23469v1](https://arxiv.org/abs/2511.23469v1)，`arxiv-2511.23469v1.html` | 为理解训练的VLM表示与生成codec各自优化 → 语义编码器与像素decoder对齐后AR连续空间生成 → 可复用表示是否改变codec训练/收敛取舍 | 潜在准入。未采用20x等数字。官方README News为Nov19结果、Dec1 inference scripts、Dec26训练代码；这些不同事件不证明论文11-30首公开，也不搬旧材料。 |
| [Price of Progress 2511.23455v1](https://arxiv.org/abs/2511.23455v1)，`arxiv-2511.23455v1.html` | benchmark进步掩盖每单位质量的成本 → 作者将质量目标、价格、开放模型/硬件调整分开估计 → 评价结论是否必须同时绑定质量目标和资源成本 | 潜在准入，效率估算是分析性质，不是kernel实测；不采用5～10x/3x年率。v1题名为Algorithmic Efficiency and the Falling Cost，不能用v2 Price Performance/推理价格上涨段反填。 |
| [Hunyuan-GameCraft-2 2511.23429v1](https://arxiv.org/abs/2511.23429v1)，`arxiv-2511.23429v1.html` | 固定键盘动作schema与人工标注限制交互 → 指令/键盘/鼠标注入、从文本视频构建因果对齐交互数据、InterBench → 语言条件视频控制和action语义边界 | 潜在准入。项目页 `gamecraft-project.html` 无具名first-public日，不用copyright2025或Nov28 submission归日；视觉响应不等真实动力学可识别。 |
| [SuperIntelliAgent 2511.23436v1](https://arxiv.org/abs/2511.23436v1)，`arxiv-2511.23436v1.html`；定点core `superintelliagent-v1.html` | 静态偏好集不能持续吸收推理反馈 → verifier按条件向量构造No→Yes前后配对，成功轨迹入replay，异步更新受lag K约束 → 训练数据筛选与陈旧反馈的边界 | 原题摘组合增量含糊，**只定点读§2.1～2.2/Algorithms1–2**决定准入，现保留窄潜在准入，不以“成熟组合”或可能负面结果关闭。还发现Eq7含log-sigmoid而Eq9写denoise-loss差的简化，是否等价与参考策略/实际实现需校准后深入受影响部分；当前不声称数学已证错、训练稳定或生产能力。未读§3结果或附录。 |

七项明确理由与一项定点core补正已向root报告；Sartre独立首校准已返回，八项窄潜在准入通过，不授目标日公开或方法收益。没有扩大深读其余七篇、没有评分快慢倒置或因日期受阻缩池。轻量当前abs未见这八项withdrawn标记，只陈述本次页面观察，不证明全版本史没有纠错。

## Books 与证据权限

当前没有新增可采用命题，**Books实际改动0、可执行整合建议0**；不是宣称主题已覆盖。旧SIMPLE/AVWM/VLASH/Catch/Academic/SCONE及QA47等具体差额/反证按旧有效记录保留。当前实际对读Ch66“为什么选一个分数不是评估系统”及成功层次、Ch25行动条件transition/真实控制权限相邻段；不把原则段自动当新论文方法已有覆盖。

若日期与证据恢复，Video-R2/Price of Progress的评价条件主owner可比较 `PLATFORM-EVALUATION-SYSTEM`；Video-CoM视觉取证主owner比较 `AGENT-TOOL-CALLING` 与 `MULTIMODAL-REPRESENTATION` 交接；WMAct/ThetaEvolve/SuperIntelliAgent需先区分训练objective与环境状态owner（`TRAIN-GRPO` / `TRAIN-DPO`），不是把“memory”命名直接交给AGENT-MEMORY；VGT比较 `MULTIMODAL-REPRESENTATION` 的codec/共享表示，GameCraft-2比较 `MULTIMODAL-WORLD-MODELS` 的typed action接口。这只是恢复路由，**没有形成精确书稿差额或整合验收**；不提交空泛Books补丁给root。

## 精确停点与未审范围

确定补充窗新增候选0；新增恢复身份8（均外部日期保留，题摘理由完成，Sartre首校准通过）；新明确撤回关闭身份1（2511.00115）；既有CourseTimeQA排除复核1，不计新增候选，两项撤回已获独立确认。原日21个潜在贡献身份及DeepSeek旧日期保留全部保留，未移动日期或重算评分；复用的是旧七份实际记录，不称21篇本轮深审。

外部材料请求：arXiv具名v1官方日批次/作者首正文公开；Hunyuan/Z.ai历史November目录、MiMo缺日期路由的独立日期或历史目录；Google pubs目标日历史切片/具名原件公开日期（16:12前默认页已恢复，年参数/可操作筛选入口仍未取得）。Qwen与DeepSeek相邻段恢复后撤销此前目录受阻请求，只保留实际查询范围限制；原DeepSeek/SCONE日期限制不因新窗规则改处置。外部保留项不支持“零事件”“无遗漏”、Coverage/Evidence通过、正面性能/安全或Books采用。

未审：Advanced其余结果/所有月目录题摘、arXiv12分类完整日批次、七项普通潜力方法/评价、Super实验/实现/附录、未知历史动态目录、普通held全部附件、全仓库版本史；没有扫描每周源。Super必要公式反侧已独立处理，不授等价或部署保证；未查实现只在未来采用相应结论时定点重开。当前普通来源必修已落实，修后非作者确认与日级验收是root待处理gate，不可写本轮完成，也不因未知日期展开全部普通方法。

## 实际校验（仅作者机械检查）

`python3 scripts/validate_research.py --report papers/2025/12/01/README.md` 本轮退出0，1份V3接口/一致性通过；`git diff --check -- papers/2025/12/01/README.md papers/2025/12/01/_sources` 退出0。本日README与本记录的相对文件链接实际检查缺失0；已读本日完整diff，原窗口/旧材料段落保留，变化限本日README和新_sources。`git diff --cached --stat` 本轮输出为空；没有执行stage/commit/push。

这些结果不验收真实覆盖、方法、日期或Books。原轮Mill复核不授本轮通过；Sartre实际首校准另见下节，当前仍等待修后非作者确认与日级验收，外部保留项也不获得Coverage/Evidence通过。

## 作者交接停点

2026-10-07 15:47 +08:00，Avicenna保存`12authorREADY`：仅表示本日作者补查记录、原件与明确局部校正可供Sartre独立校准，不是本轮完成/复核通过。最新V3校验、diff空白检查、相对文件链接检查再次实际通过，cached diff为空。新增确定落窗0、日期隔离潜力8、新撤回关闭1、旧CourseTimeQA撤回复用1；14每日源均实际请求，其中9个当前有界段已检查、5项具体外部受阻。剩余方法/评价/公式反证未深审且已列明，待校准与必要日期恢复后只重开对应项。没有隐藏普通阅读完成断言，没有写Books/共享State/合同或Git。

按root最新授权，本作者保存此停点后转为08-01非作者校准；12-01等待Sartre结果，由root协调后续恢复，不自签验收、不自切另一作者日。

## 首校准响应与局部修正（16:02 +08:00）

完成08-01非作者Review后，按root新授权回12-01，重新读取主AGENTS/当前合同/每日来源/Prompt/ROADMAP及本日材料。实际读取[Sartre首校准](./supplement-first-review-20261007.md)：八份v1窄准入、两种撤回排除及Super必要公式隔离通过，唯一普通必修是DeepMind伪分页。

16:02标准HTMLParser实际解析原`deepmind-page3.html`：两个canonical均`https://deepmind.google/research/publications/`；Previous链接为`#`且class含`pagination__arrow--hidden`；Next链接为`/research/publications/page/2/`。正文为265 publications总数、首页30张日期卡，Sep16 2026至Nov4 2025，其中Dec3 Capturing Human Preferences → Nov21 Imitation Learning → Nov4下界。原`?page=3`请求返回的是首页，不是成功翻页；HTTP响应成功与参数生效明确分开。原文件名保留为请求历史，未改原件。

本次选择删除非必要的“第3页”覆盖声明、保留首页内Nov30两侧的实际有界观察；没有再次请求真`/research/publications/page/3/`，也不将旧26个月标签题名或其他旧题名重新认证为第3页。Sartre独立实际真第3页观察为Mar24 2025至Sep21 2024，引用的是其复核记录，不冒称作者新curl原件；该段不涉及本补充窗，无须扩扫。Google pubs访问失败与其他来源外部边界不因此消失。

同步首校准事实与Super反侧：即使接受Eq8且const消去，Eq7代入仍是`E softplus(beta*Delta)`，不等Eq9的`E Delta`；因此展示公式链不能授直接等价，不推实际代码错误或全部实验无效。无正面采用，保留必要公式/可靠性/稳定性隔离即可；未来采用objective/实现时再定点核实际loss、reference与采样条件。本次未读新实验/代码/附件、未更改八项潜力或日期。

作者保存修后`12authorREADY`供非作者定点确认；首校准不是日级最终通过，状态仍进行中。没有Books/State/合同/脚本/索引/Git写入。

修后实际机械检查：V3校验1份退出0，限定本日README/_sources的`git diff --check`退出0，本日README/本记录相对文件链接缺失0、行尾空白0；实际parser复核首页日期卡30张及首尾日期一致。只作只读Git检查，没有stage/commit/push；这些结果不替代非作者修后确认。

## root新回源提示后的本日定点核查（16:12前完成）

root提供其他日的page2/3/9、Meta和Hunyuan访问结果，只作路由，不跨日授本窗覆盖。本作者实际web回DeepMind首页，再次核到Nov30两侧Dec3/Nov21与Nov4下界，无须打开本窗之外Mar/Apr页。实际web打开Google pubs默认页成功，年参数入口仍Internal Error；本机默认curl实际25秒timeout/0B，CUA iab不可用且浏览器列表空，没有UI阅读或筛选成功。两次官方pubs主题/目标日补检返回空，仅索引受限，不作no-hit来源验收。

实际URL、工具结果摘录、执行停止与权限边界存[Google目录恢复观察](./supplement-20261007/google-directory-recovery-1612.md)。撤销“默认pubs不可达”当前判断，保留早次实际失败历史；2025选项678不等生效年过滤或日公开。新恢复确定候选仍0，8潜力/撤回/旧日期处置不变。尚需相关历史切片/具名日公开；未创建678逐项队列、未扩其他日、未把他人Hunyuan timeout/kernelreset冒称本次UI检查。
