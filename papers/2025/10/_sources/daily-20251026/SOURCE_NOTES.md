# 2025-10-26 有限来源记录

窗口为 BJT [2025-10-25 09:00, 2025-10-26 09:00)。实际请求时间与 URL 保留于各 `*.request.json`；成功响应逐字保存在 `*.raw`。`.txt` 是 HTMLParser 文本投影，未把存在文件当作已读正文证明。

本日 startup 实读 AGENTS、研究合同、来源使用说明/每日/按需/arXiv、Report合同、Prompt、ROADMAP及 LEARNING_STATE 最新10月路由。只本日；未拿其他Daily或旧Weekly反推。

## 真实停止与恢复

- OpenAI：Research HTTP403后取官方 news/rss.xml，XML解析所有item的pubDate，只过滤本窗。当前 RSS 本窗无 item；研究页覆盖仍有限。pubDate原值为GMT，按BJT换算，不拿更新时间入窗。
- Anthropic：Research 页包含嵌入 publication 数据。只核本窗 publishedOn 范围，无命中，窗前10/14及窗后10/29字段用于边界定位；CMS `_createdAt` 不是首次公开，不采用。
- Google：Research publications 的 `?year=2025`、`?q=large%20language%20model&year=2025` 实际输出仍11583目录且2025 filter未选中，未把参数成功下载算过滤成功。DeepMind publications `?page=2` 仍同首页，从2026到2025/11/04；不伪造读完。主题/date官方域名有界补检未恢复本窗原件，原历史段隔离，不进一步遍历全年目录。
- Meta：Research200只呈现当前Muse品牌标题，没有可读历史正文。Qwen旧首页说明迁移且最晚09/23；DeepSeek首页只有当前导航。原入口检查+一次本窗域名日期补检后停，不以失败授覆盖。
- Moonshot：Blog完整当前26条，只定位09/16～11/06间；GitHub当前组织首页不作历史event ledger。
- Hunyuan：首查Research动态壳，浏览器一次初始加载后再取状态，全部11条到2026/02/03。页面JS `index-I3I3bCf9.js`给官方base URL api.hunyuan.tencent.com；chunk `index-cEoitnb7.js`给POST publicList，Blog chunk给pageNum/pageSize/renderType。第一次错误主机请求404保留；修正主机成功的英文9条、中文11条皆无2025历史段。中文请求停止page1，totalNum=11≤pageSize20，非未读分页。GitHub org与T1 README有限定位，未逐仓扫描。检索错误不授无事件。
- Z.ai：原Research/page2累积18项，终点“没有更多...”但最旧2025/12/07，没有10月历史；release notes仅补现有日期字段，不代Research覆盖。
- Seed：原网页JS `main.897993d4.js`定义Publication=1/Blog=2与 get_article_list_v2，论文请求必须加`x-tt-locale: US`。无此头的响应total94却无sub_article_list，保留异常原件，不作空结果。修正后2025升序、count20，真实tokens0/20/40/60/80，最后has_more=false；只检查PublishDate字段至10/22与12/02断档。Blog同接口type2，tokens0/20/40，最后false，10/23～11/27断档。只作本窗目录日期检查，不把年份清单的94/49当当日命中数，也不审全部正文。
- ERNIE：真实链接page2，共2页，末页至06/30，10/16后11/07；没有本窗展示项。MiMo仅当前Paper/Blog8条，10/21窗前；More不是历史pagination，未声称完整历史覆盖。
- MiniMax：英中Blog各当前11条，10/27为窗外。独立Agent Tech Blog、原生techblog.md及llms.txt，现唯一文章2026/05/13；不以主Blog代Agent历史覆盖。
- arXiv：官方availability说明所有时间Eastern，常规发布Sun～Thu20:00、Fri/Sat无公告；10/25～26 BJT没有常规批次。高级搜索明确announcement date只支持year/month，不用它造日级公开时刻。cs.CL月列表skip0/show50只定位，未遍历2666条。
- arXiv查询异常：原 `arxiv-topic` 未完整编码，返回59416及2026项目，不能用。`arxiv-topic-encoded`完整URL编码后total70、start0/max100，submitted原值全在所给提交时间范围；查询为 `(cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AI) AND (all:"language model" OR all:transformer OR all:inference OR all:agent) AND submittedDate:[202510250100 TO 202510260100]`。这些是提交线索，不是当窗首次公开事件；未将70项转成全文待办、未评分或正面采用。常规批次边界与独立官方公开缺口分开。

## 辅助查询

实际进行了Google/Meta/Hunyuan目标日期官方site查询，以及Qwen/DeepSeek/Moonshot/Z.ai/MiMo/MiniMax目标日期查询。部分仅用site文本的搜索发生域名外漂移，结果未用于证据。最终限定工具domains：deepmind.google、research.google、ai.meta.com、qwenlm.github.io、deepseek.com、platform.kimi.com、hunyuan.tencent.com、zhipuai.cn、seed.bytedance.com、ernie.baidu.com、mimo.xiaomi.com、minimax.io，query=`"2025-10-25" OR "2025-10-26" research model`，无结果，停止1轮。搜索无结果不证明原历史目录无事件。

## 校准包

确定候选0，证据0，Books差额0。独立复核重点：submitted/public区别、修正后的查询实际范围、Seed请求头/分页终点、Hunyuan真实浏览器及中文11条、Google参数未生效和Qwen迁移不当覆盖。无需以零候选制造正面Evidence；报告保持进行中。

## root 初稿反馈后的窄修

真实重开两源而非重扫日期：Google原Blog `https://www.research.google/blog/2025/10/` 成功200，首页12条由10/31至10/09，实际阅读本窗邻接10/23 Earth AI→10/27 personal health coach，未列10/25、26。按降序停止在10/23；更早页不影响本窗邻接，不将全月转为候选池。Blog补检不替代已实际访问但过滤参数失败的Google pubs。

DeepSeek从官网实际链接进入 `https://www.deepseek.com/news/` 200，研究索引10项由2026/06/24至2025/05/14，本窗邻接10/21 OCR→11/01 LPLB；动态5项邻接09/29 V3.2-Exp→12/01 V3.2。实际列表没有本窗日期，停止在相邻条目；“查看全部”没有href，未杜撰分页或日期。qwen.ai迁移入口也实际取到200但仅Qwen壳，仍隔离历史缺段。原件/真实请求google-oct、deepseek-news、qwen-new已保存。DeepSeek原“首页壳即外部hold”已纠正为此有限检查，不抹去旧过程记录。

## 2026-10-05 Google Publications 参数定点纠正

fresh实读当前AGENTS、研究合同、来源使用说明/每日/按需/arXiv、Report合同、Prompt、ROADMAP及最新10月路由，只重开本源。旧`year/query`不是有效过滤；此前称其“正确 query”不准确，旧请求/失败与root原复核记录保留，不由作者改写。

真实请求 `https://research.google/pubs/?category=2025&search=language%20model` 于UTC `2026-10-04T22:49:44.328062+00:00`执行，HTTP200，366460字节；原响应、文本投影、请求见`google-pubs-category-search.raw/.txt/.request.json`。实际核原HTML的`filter-year-2025`为checked，文本为`1 - 15 of 37 publications`及`of 3 pages`。仅定位首屏标题、年度字段和分页，不把37项扩成逐篇题摘或附件队列；停止page1。该原列表提供2025年度而非本窗首公开时刻，未读page2/3不称读完，不能授本窗零事件/完整覆盖。必要恢复条件是能连接具体相关材料到本窗的官方历史公告或完全落窗公开bounds，而非继续读取全年所有摘要。

候选/审阅/Books提案及写入仍各0；此前DAY已accepted，本次变化单独待root窄复核。其他来源、Books、索引与学习状态均未重开或修改。
