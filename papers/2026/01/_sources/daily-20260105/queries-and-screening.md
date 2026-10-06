# Jan05 原始查询与筛选停点

窗口：[2026-01-04T09:00:00+08:00, 2026-01-05T09:00:00+08:00)，UTC [Jan4T01,Jan5T01)。执行2026-10-02T03:03～03:07Z。仅本日README与月级_sources owned；不读取旧Report/Weekly候选、评分、摘要。跨日只接两Kimi release身份及日期线索，本日重新取得具体原文决定贡献。

## 机构来源：实际入口与停止

五批原入口响应保存在official-entry-0～4.txt，补充入口在supplemental-official.txt；不是把宽目录变成候选队列。每批只是当前官方首屏/有限日期定位，不读窗外全部摘要。

1. OpenAI Research首屏当前2026年7～9月。进一步GET https://openai.com/news/rss.xml，仅1243项title/link/pubDate元数据筛本窗与两侧：hits=[]，Jan2T10Z Grove / Jan7T00Z Health，原字符串见official-date-slices。止这一日期段，不读全年正文；不重审窗外Grove。
2. Anthropic Research首屏Oct1～Sep4；进一步GET原HTML解析174个publishedOn，本窗hits=[]，最近之前Bloom 2025-12-19T19:45:00.000Z，之后本次返回Title为Next-generation Constitutional Classifiers 2026-01-08T00:00:00.000Z。保留实际原字段，不借另一日报目录标题。止metadata，不全读174篇。
3. Google DeepMind Research current news止May2026，进一步Publications page1 30 dated rows/265 total/9pages，Jan9 TRecViT→Dec3 Capturing Human Preferences桥接窗口，停止page1。GoogleResearch pubs当前首屏只有年过滤2026=372/2025=676等，缺本日first-public/revision目录；官方域日期补检首组后仍受阻，不能沿科研全站扩搜。
4. Meta Research原入口0行；官方域日期query首组空。不是“无发布”，必要历史日期目录缺失。
5. Qwen旧Blog止Sep23 2025→July2025，明确新Blog https://qwen.ai/blog fresh0行；官方域Jan4/5主题日期query空。缺Jan05历史dated入口，不根据版本号判公开。
6. DeepSeek /news/ 当前研究10项Jan12→Dec31桥接，本窗无行，动态5/查看全部有限。date-label不是首次公开时刻，不据此重新吸收mHC或推全机构零。
7. Kimi Platform26 dated entries Nov7 2025→May2024；fresh exact-tag https://raw.githubusercontent.com/MoonshotAI/kimi-cli/0.72/CHANGELOG.md 完整0.71/0.72核心，GET两官方release tags API获得published_at。日期确定；完整模型研究/重要revision历史不由平台与单项目提供。止这两个版本，不普通PR扫描。
8. Hunyuan首查Research超时；本日fresh POST https://api.hunyuan.tencent.com/api/blog/publicList，Content-Type application/json，body {"pageNum":1,"pageSize":1000,"renderType":0}。成功code0,totalNum9,list9，各publishedAt/publicAt/displayPublishTime/updatedAt原字段保留。本次已成功提取官方前端数据，无须以浏览器重复同一目录；最早display/published 1770090898=Feb3T03:54:58Z，当前九条无法恢复Jan05历史，被删除/隐去记录未知。止page1 metadata，未读这些窗外正文。
9. Z.ai首查Research本次15日期行，止Dec9 2025/查看更多；release-notes Jan14→Dec22桥接无本窗dated行。有限release不是全部研究，日期query首组空后缺完整历史目录。
10. Seed官方Research/public_papers首屏后GET已知官方API，只窗口邻接切片。article_type=1/2分别论文/博客；publish_year=2026 ASC、2025 DESC，count20/page_token0，header x-tt-locale:US。2026首页19/14行，最早PublishDate=1768838400000（Jan19T16Z/Jan20 BJT）与1770825600000（Feb11T16Z/Feb12 BJT）；2025首页18/18，最新1765728000000（Dec14T16Z/Dec15 BJT）与1766505600000（Dec23T16Z/Dec24 BJT）。按实际PublishDate而非遇旧pinned即停，本窗无行；next_page_token/has_more/total原值保存。不读全年AB，有限当前API的locale/status不保历史完整。
11. ERNIE Blogpage1 Jan8→Dec23桥接，下一页2/2更旧，止page1无本窗行及query首组。不把全部论文出版状态当日首次公开。
12. MiMo八个Paper日期Jan8→Oct21桥接，15个当前Blog/More多无日期，止首入口+日期query首组。缺历史Blog日期，不把标题重命名当研究增量。
13. MiniMax English12 dated项Jan27→Dec23桥接无本窗行；中文minimaxi重定向minimax.cn/blog仅68行壳，AgentTechBlog仅15行导航。止三有限入口+官方域日期query首组，CN/Agent历史受阻。

辅助机构查询四组原文及domains见date-search.txt；Jan4/Jan5日期表达+model/research/agent，均首组Empty search results即止。不把空索引视为14源全覆盖、不新增Weekly源。

## arXiv 本日边界和查询

本日重开availability：L172说明常规公开公告Sun～Thu、Fri/Sat无公告；L175/176首次公告才分ID、不能提前获得或backdate。另实际读holiday全文L17/21/29/32：只延迟新submission公开，Dec31ET14～Jan2ET14 accepted批次计划Jan4ET20公告。该计划=Jan5 BJT09，恰好本窗不含右端；没有把Submitted或计划时间伪装具体论文的实际首次公开证明，也未扩日吸收下一批。常规计划公告本窗无，不保证作者镜像/非标准公开变化不存在。

补检API针对可能旧提交更新，而非将所有Submitted扩成新论文池：
lastUpdatedDate:[202601040100 TO 202601050059] AND submittedDate:[199001010000 TO 202601040059] AND (<theme>)
start=0,max_results=20,sortBy=lastUpdatedDate,sortOrder=ascending。四主题完整编码URL/执行时间/total/entries见arxiv-and-kimi.jsonl：
- 模型：(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:MoE OR all:"foundation model")
- 系统：(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:kernel OR all:"model inference" OR all:"distributed training")
- 多模态：(cat:cs.CV OR cat:cs.RO OR cat:cs.LG) AND (all:"foundation model" OR all:"world model" OR all:VLA OR all:multimodal OR all:"diffusion model")
- Agent：(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:LLM OR all:"language model") AND (all:agent OR all:RAG OR all:memory OR all:reasoning OR all:planning)

实际四组total0/rows[]，stop首组，不逐分类清库存。latestUpdated索引与Submitted过滤不是全部公开修订目录。官网catchup?subject=cs.CL&date=2026-01-05&include_abs=False web cache miss、实际HTTP400；/list/cs.CL/2026-01?skip=0&show=25 cache miss。为本窗标题查漏尝试但目录未恢复，止此不扩全月。

## 两个已确认本窗事件的独立初筛

本日重新取得完整release body及exact-tag changelog窄核心，原文在arxiv-and-kimi.jsonl。两事件同一kimi-cli家族，不是两个论文候选。
- 0.71：published_at=2026-01-04T05:08:41Z，created_at=2026-01-04T04:59:46Z；前者支持本日release公开，后者不替代公开。ACP把file reads/writes/shell通过client同步，另/model默认切换与reload、/skill按需加载、info版本协议json、Toad UI、CI Python3.14。实际变化是功能/兼容接入，但核心未提出可改变长期执行/可靠性选择的新控制机制、失效边界或验证条件；并非仅因是框架发布排除。拟贡献前关闭，不评分，不读普通PR，也不声称当前代码已核/实验复现。
- 0.72：published_at=2026-01-04T06:01:07Z，created_at=2026-01-04T05:55:57Z；完整核心只有Python3.14 installation fix。具体修复是此版本安装兼容，无模型/训练/推理/Agent机制的长期增量，也无核心可见纠错/安全或本书设计反证信号；fix标签本身不触发全PR深入阅读。拟贡献前关闭，不评分。

首批两负侧及0拟入选已发root独立校准，不继承Jan04处置。其余来源无确认窗内相关材料不做形式化题摘数量。root实际读取本日两个精确release完整核心、日期与查询停止及限制，确认负侧与0正式候选/No Change的有限依据，非作者日级验收通过；实际范围见README§6，作者未自复核。

## 精确限制及重开

GoogleResearch日级公开目录、Meta、Qwen、Moonshot完整研究/重要revision、Hunyuan历史、Z.ai完整历史、MiMo Blog日期、MiniMax CN/Agent，以及arXiv非标准公开revision/作者镜像，隔离且不算正面Evidence/Coverage无缺口。所需替代是同一本窗官方dated历史目录/公告批次/指定版本公告或可核author-first-public，取得后只恢复该源/事件，不扩月份；不能进入Books或支撑无遗漏/性能/安全保证。
