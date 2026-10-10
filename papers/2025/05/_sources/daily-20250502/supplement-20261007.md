# 2025-05-02 来源遗漏补查 checkpoint

作者：Boole；继承模型，不调整模型。仅本日，补充窗口 `2025-05-01 ～ 2025-05-01`。原窗口 `2025-05-01 09:00:00 ～ 2025-05-02 09:00:00` 和原26家族公开日/评分/有效审阅冻结；[完整原报告](baseline-before-supplement-20261007.md)保留。2026-10-07启动/压缩恢复均重读AGENTS及当前Research/每日Source/arXiv说明/Report/Prompt/ROADMAP和State本日路由，不继承05-01或其他日验收。

## 当前停点与真实漏斗

14个每日来源均实际重新访问，历史限制逐源隔离，没有catchup/全类月份/机构历年队列。4主题134次出现→110唯一完整当前题摘：初判75P/35C，root全部首读后四重开79P/31C，再实际读18具名exact-v1 core及AMIE §2.1/C.3/C.4并通过五P→C，当前校准74P/36C，非formal日候选。机构另计：Anthropic贡献前关闭；AMIE May1官方事件准入5分已通过，本轮受限标准完成1、Ch81受限标准及具体已有覆盖已获root第三批通过；Meta/OpenAI反侧保持。LIFT按R1保留P/中心梯度实现争议，不采用GNN监督直接更新LLM，不改C/降分绕过。Google Pubs本轮真实2025+language model返回首页15/37目录身份、May1日期文本0条，两请求200、停page1，不成年度全文队列。root第三批内容差额已通过，作者写回READY；仅冻结旧值校验兼容未通过，不签整日、不计验收。原26不迁日/改分；Books写入0，不授全Coverage/Evidence。

## 14来源实际检查

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/release直接请求403；网页检索恢复研究首页并定点May1 Monday GPT退休说明和Responses/Files事故页；事故短更新读到末尾，不跨历史队列。 | 受阻 | 历史Research条目目录未恢复；搜索没有命中不证明无研究。事故无cause/机制复盘；不由resolved推出安全。 |
| SRC-ANTHROPIC | Research/news当前页；定点/news/integrations官方跳转claude.com，核心全文标May1，June3扩可用plan分离；root核后产品可用性贡献前关闭，不评分/不签Books已有覆盖。 | 已检查 | 仅恢复此具名发布，不保证全站无遗漏；版本为当前官方迁移页，不伪称May1网页快照。 |
| SRC-GOOGLE-AI | DeepMind year无效page1/9止；Blog /2025/05九行日期目录及AMIE核心/评价/限制已读。Pubs本轮category=2025&search=language model实际200、year选中、首页15/37；同category搜索May 1, 2025实际200、0条。仅读目录身份/年份及分页状态，不开正文、不取page2/3。 | 受阻 | 有限主题年度入口已恢复，但目录年不是具体首公开日，日期搜索0条不授无遗漏；DeepMind/Pubs May1历史日期缺口保留。AMIE准入5已通过、受限标准/owner差额已获root第三批通过，May6 paper及当前Blog2026-10-06发表更新不回投May1。 |
| SRC-META-AI | Research当前页和具名May1 Cutouts核心全文；读SAM2.1此前fall2024训练、Torch Inductor及H100吞吐/首帧延迟；root已读短文，关闭维持。 | 受阻 | 无法由当前Research恢复May1完整历史目录；本文未披露新compiler/执行机制归因，不计无遗漏。 |
| SRC-QWEN | 官方首页及/page/2/的日期/标题，May1位置相邻Qwen3 Apr29与Qwen3Embedding Jun5；在第2页日期包围停止。 | 已检查 | 只支持此两页博客日期切片无May1行，不证明论文或GitHub全部渠道无事件。 |
| SRC-DEEPSEEK | 官方首页当前模型与具名日期搜索；/news实际转到First API Call当前文档，不是News历史目录，读到文档页末即止。 | 受阻 | 错误目录/无搜索结果不能授无命中；需要May1官方研究/发布列表快照。 |
| SRC-MOONSHOT | Kimi Platform Blog可见列表按日期核到May6长思考、Apr7价格调整及Mar3Muon/Feb19MoBA；May1处无行；不扫GitHub全历史。 | 已检查 | 只支持该官方博客当前保留列表的日期切片，不声称所有repository版本无事件。 |
| SRC-TENCENT-HUNYUAN | Research动态shell；已尝试IAB，超时/子agent不支持隐藏visibility，未取得浏览器证据。由官方JS恢复api.hunyuan.tencent.com/api/blog/publicList，POST pageNum1/pageSize20/renderType0，total9/list9全为2026，停page1。 | 受阻 | 当前研究目录不提供2025；错误host404保留但不作阴性。需May1全部列表或当期具名条目快照，不据访问失败写不适用。 |
| SRC-ZAI | 首查官方Research，当前展示2026至Dec2025；?year=2025&month=5无效返回同页；具名日期搜索未恢复May1，停止当前页。 | 受阻 | 缺历史Research目录，不扫描嵌入全机构论文历年数据；需May1条目快照。 |
| SRC-BYTEDANCE-SEED | 官方JS恢复get_article_list_v2，publish_year2025/order_desctrue/count20；blog type2 token0→20日期跨Jul14/May12→Apr23，stop20；已并发取到40只保留日期导航，不建筛选队列。papers type1且x-tt-localeUS token0→20→40，page40 May17→Mar22，May2→Apr25包围，stop40（不取60）。 | 已检查 | 无May1门户发布行仅限该日期切片；门户publishDate不是原论文首公开，不能替代arXiv日期。错误type0/缺locale空response明确无阴性权限。 |
| SRC-BAIDU-ERNIE | 技术博客首页和page2日期导航读到最早Jun30 2025，停止page2；没有恢复May1，不扫repo全历史。 | 受阻 | 最早当前保留条目不是源成立日；需要May1官方论文/技术博客列表，不写不适用。 |
| SRC-XIAOMI-MIMO | 官方首页current首newsMay12及官方MiMo README当前HEAD，用于身份/日期导航，未冻结代码版本；停止首页+README。 | 受阻 | 未恢复May1历史发布，不将Apr30已知身份静默搬入本日。需要May1官方变更/发布快照；不能用HEAD日期证明v1。 |
| SRC-MINIMAX | 英文/中文blog（中文官方redirect minimax.cn）可见日期段至Jan15 2025；技术blog官方页当前仅May13 2026，止本页。 | 受阻 | 当前保留博客日期片段没有May1行，不代表全部研究release无事件；无零命中/不适用推断。 |
| SRC-ARXIV | 4具名Advanced主题：language model；LLM AND inference；vision language OR world model OR video generation；agent AND LLM。CS含crosslist，first-submitted Apr29～30仅发现，size100，announced_date_first；model101按start0/100读完，systems10/multi11/agent12单页读完；134出现→110唯一完整题摘，root校准74日期隔离潜力+36关闭，非formal；LIFT另保留中心机制争议。官方月表cs.DC May skip0/show25只浏览标题到#8；cs.CL Apr skip1500/show100只浏览到#1506，不扫全分类。 | 受阻 | 公告年月/提交不是May1公开日期。API模型total187首100未筛选不分页；错误400/404/越界空列表均不作阴性；宽May2提交query已收窄而非转待办队列。CaGR-RAG从月表定点读题摘，v1提交May2只作窗外线索，不计本窗候选。 |

## 查询、分页与停止

[实际请求索引](supplement-20261007/request-index.md)的70个请求逐个链接参数/UTC时刻/状态/redirect；额外[CaGR-RAG请求](supplement-20261007/arxiv-cagrrag.request.json)定点补原始题摘，不扩月表。真实HTTP请求从2026-10-07T09:56:56.011718Z至10:25:23.156095Z，即北京时间17:56:56至18:25:23；精确时刻以各收据为准。UTC与北京时间只作运行记录，不作论文时刻筛选。

Advanced共同实际参数：`advanced=1`, `classification-computer_science=y`, `classification-include_cross_list=include`, `date-filter_by=date_range`, `date-from_date=2025-04-29`, `date-to_date=2025-04-30`, `date-date_type=submitted_date_first`, `abstracts=show`, `size=100`, `order=announced_date_first`。`terms-N-operator/term/field=all`分别是上表4组词，model只分页start=100补最后1条。初始`order=-submitted_date_first`4组400；修正后Apr29～May2 model251过宽（只读首几个身份）及其他50条页面没变成筛选队列，随后收窄至Apr29～30；原始错误/宽页保存，不能用它们的数量计算完成。最终110完整题摘分段读完，#13～15因输出截断定点补读。全文json保留搜索回传的当前版本，不声称历史exact-v1。

API辅助实际`search_query=(all:"language model") AND submittedDate:[202504290000 TO 202504302359]`、`start=0/max_results=100/sortBy=submittedDate/sortOrder=ascending`（以[原请求](supplement-20261007/arxiv-api-model.request.json)编码为准）；total187，首100仅作辅助恢复，不全筛、不请求剩余87。该API没有CS分类约束，不与Advanced110混算。

官方月表cs.DC `https://arxiv.org/list/cs.DC/2025-05?skip=0&show=25`总302，只读标题到#8，不分页，不将302送入队列。#3 Distributed RAG只核身份对本日旧候选2505.00443去重；#7 CaGR-RAG定点[abstract当前页](supplement-20261007/arxiv-cagrrag.txt)读完，原文cluster query grouping/opportunistic prefetch有潜力，但[v1]提交May2，不冒充May1首公开，作为窗外线索暂不扩查。cs.CL `.../2025-04?skip=1500&show=100`总1613，header和前6标题到#1506，仅月目录线索，不读100完整题摘；早期skip2200/1800越界空响应不证明无命中。月编号/announcement year-month一律不当具体日。

Seed实际GET `/api/get_article_list_v2?article_type=1&publish_year=2025&order_desc=true&count=20&page_token=0/20/40`，header `x-tt-locale:US`；papers total94，页18/20/19条（localization使列表数与count不同），停止token40不取60。Blog type2 total49，token0/20/40回15/18/8条；token20已经穿过May1，token40为检查前已经并发发送的多取页，只有日期导航读到末尾，无正文队列，`has_more=false`。此前type0或type1无locale返回空列表无历史阴性权限。门户的publishDate和原论文首公开分开。

Hunyuan由Research官方asset链恢复POST `https://api.hunyuan.tencent.com/api/blog/publicList` body `{"pageNum":1,"pageSize":20,"renderType":0}`；totalNum9，9行全部2026，停page1，不假装恢复2025。最初同path错host `hunyuan.tencent.com`404保留。浏览器三次尝试有timeout与子agentvisibility不支持，没有成功截图，不替代恢复缺口。

Google原`?year/month`与猜archive路径不生效/404均保存。随后从实际页面链接`/blog/2025`再到`/blog/2025/05`，已读9条日期+标题及May1 AMIE核心；May2 Amplify和其余月条目只日期导航，不进入本窗。

### 本轮Google Pubs具名有限恢复

按用户指定实际试`category=2025`，而不是继续无效year参数。GET [2025+language model](https://research.google/pubs/?category=2025&search=language%20model)，UTC2026-10-07T11:40:42.931943+00:00，200，最终URL保留相同category/search；HTML的filter-year-2025确为checked，结果`1 - 15 of 37 publications`。GET [2025+May1日期文本](https://research.google/pubs/?category=2025&search=May%201%2C%202025)，UTC11:40:46.540046+00:00，200，`0 - 0 of 0 publications`/No Results Found。真实参数、状态、最终URL与page1停止见[LM收据](supplement-20261007/google-pubs-category-lm.request.json)、[May1收据](supplement-20261007/google-pubs-category-may1.request.json)；对应raw/txt原件保留。

实际只读过滤是否生效、结果数、首页15个题名/身份与年级元数据，停首页最后RADAR，不读目录内嵌完整摘要/论文正文，不请求page2/3剩余22。首页身份依次为：Toward expert-level medical question answering；Towards accurate differential diagnosis；Gemini & Physical World；SSDTrain；A Scalable Framework for Evaluating Health Language Models；Astute RAG；Synthetic Text Generation via Gradient Matching；personal health LLM for sleep/fitness；Crosslingual Capabilities；Synthesizing/Adapting Error Correction Data；Outgoing Connection Heterogeneity；Similarity Metrics for Data Selection；HEART；PLAN-TUNING；RADAR。它们只是2025主题目录恢复，不是15当日候选、不是新潜力分母，也不变成全部年度逐项待办；获得具名May1首公开依据才定点重开相应身份。未确认日期的目录身份不因没有深审而作贡献关闭。

辅助web检索实际两q：`site:research.google/pubs/ "May 1, 2025" "language model"`、`site:research.google/pubs/ "2025-05-01" "language model"`，domain research.google。工具返回AMIE Blog与Google at CHI 2025的日期片段，均非pubs内May1首公开证明；只看发现结果，不打开CHI正文/扩会议队列。网页工具对category+LM open显示not accessible，随后直接HTTP200已恢复，前者不当源不可达/无命中。试图取官方JS的curl返回空白未得诊断，不作为过滤证据；过滤有效性依据实际HTML checked与37结果。年度目录与文本零结果都不足授May1历史覆盖，缺口维持，只接受当期官方日期列表/具名首发定点恢复。

## 撤回/纠错、安全与反证

Anthropic页June3更新仅可用plan扩展，不是May1机制；Google/Meta当前core可见处未发现正式撤回/勘误说明，但不能证明完整版本史无变更。arXiv当前搜索注释未找到正式withdrawn/retracted/erratum，关键词`correction`命中Antidote/one-shot正文，不当勘误。原75及当前74潜力中prompt injection、ReCIT梯度泄漏、code安全、supply-chain、NeuRel、CachePrune、persuasion、base/aligned反证都保留，root已全读题摘；必要精确事件注释仍待按采用命题检查；不把安全负侧从池里减掉。机构代表排除含AMIE的OSCE模拟边界、Meta收益归因缺口及OpenAI事件无root-cause详情，全部交非作者。

## Books只交root的具体比较预备

Anthropic贡献前关闭不是已有覆盖：原稿实际只有Claude产品可用性变化，主题能映射Ch83不能替代新增机制。不继续为该篇制造Books差额；此前Ch83正文定点读取仅是预备，不作本包Books通过。

AMIE准入5分已获root通过，本轮受限标准Evidence及actual-owner实际正文比较完成，已有覆盖/No Change已获root第三批通过，具体Ch81位置、采用边界及重开条件见[差额](core-revisions-20261007.md#actual-owner差额提交root)。没有新长期句或共享Books写入提案，不凭主题覆盖撤销准入。

## 下一次只从此处恢复

1. root首读110题摘及第二批18 core/AMIE准入校准复用；[第三批](review-supplement-20261007.md#第三批本轮内容闭合冻结日期校验仍未通过)已实际通过LIFT隔离、AMIE受限标准/Ch81具体已有覆盖和Pubs有限恢复。当前74P/36C非formal，无这些项的窄核/论文待办，不重抓110/18。
2. 唯一当前停点为冻结旧值的V3校验兼容：exit1，仅26条旧日期范围错误，无其他错误。root暂不签整日、不计验收；作者保留原窗口/日期/评分/52块与进行中，不改checker或共享规则，不静默跳过旧行或扩窗迁日。后续仅由root确认不改变冻结旧值的兼容校验办法。
3. 74P日期、LIFT中心机制争议及历史来源缺口已独核隔离，非当前普通未读/必要外部材料阻塞；材料以后到达时按既有具名条件重开对应身份，不正面采用、不进Books、不扩检索。LIFT单独恢复日期不能解除梯度争议。
4. 前轮19具名HTML/两PDF及Pubs两限定GET/两日期web search的实际请求和停止原件保留。本次仅裁决同步与机械验证，没有新网络/扩池、无Books新句或共享写入。内容写回READY，不授DAY。

限定仅README和同日_sources；保护运行前与并发修改，无stage/commit/push，未写Books/State/合同/index或独立原件。本轮内容差额已获root第三批通过，当前唯一停点为26条冻结旧日期/原09:00窗口的V3兼容报错，不改旧值。实际写后重跑V3：exit1，仅26条冻结日期错误、无其他错误；26日期/评分/owner/审阅无差额、52原review/Books块逐字保持，原窗口和完整档案SHA256不变，独立review原件hash写前后相同。四份维护文档91处本地引用/54目标均存在，限定diff检查通过、cached差额为空。作者实际写回READY，报告进行中、校验未通过、整日不计验收。历史日期/来源/争议隔离不重新列为当前普通待办。
