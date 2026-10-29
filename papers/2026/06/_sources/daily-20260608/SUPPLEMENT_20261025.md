# 2026-06-08 遗漏补查：2026-06-07 北京时间自然日

执行者：`supp_jun08`；执行时间：2026-10-25T18:14:40+08:00 起。本文件记录本日新增检查，不替换旧小时窗的身份、分数与有效证据。

启动时完整读取 AGENTS、当前研究合同、来源清单使用说明与 Daily 分组/arXiv 主题、Report 合同、统一 Prompt、ROADMAP；State 仅用于本日路由。只补 `[2026-06-07T00:00+08:00, 2026-06-08T00:00+08:00)`，未扫描 Weekly、Live、2025 或其他日报。无共享 Books 写入。

## 实际来源、停止范围与结果

以下为本次真实请求及必要返回字段摘录，不把非目标日期导航条目当作逐项全文队列。没有发现日期已核准的新增候选，所以没有新增评分或 Evidence/Books 正面采用。

| 来源 | 请求/实际停止点 | 本次观察及边界 |
| --- | --- | --- |
| OpenAI | [RSS](https://openai.com/news/rss.xml)，curl 成功解析全部 1318 item；按 pubDate 转换 BJT | Jun07 BJT 0。目标邻后为 Economic Research Exchange `Mon, 08 Jun 2026 00:00:00 GMT`，Built to benefit everyone `01:30:00 GMT`，S-1 `14:00:00 GMT`，均 Jun08；不重新读作补窗候选。urllib 一次 TLS EOF、web XML 不支持已由 curl 成功恢复。 |
| Anthropic | [Research page 2 JSON](https://www.anthropic.com/listing/research/default/2)，24 posts | 目标邻段 n-days/agents-in-biology `publishedOn=2026-06-08`，chemist `2026-06-05`，ATT&CK Navigator `2026-06-03`，Jun07 0。只作日期目录核查，不继承旧首屏覆盖。 |
| Google | [Research Publications](https://research.google/pubs/)；[DeepMind Publications page1](https://deepmind.google/research/publications/)，265 总数、首30条；[Google June Blog](https://research.google/blog/2026/06/) 12条全部可见 | DeepMind 邻段 Jun12/Jun04，无 Jun07，但为 selected list；Google Publications 15/11637 仅年份，HTML 无 datePublished/time；`year=2026&research_area=natural-language-processing` 实际未选中过滤、仍11637，不能冒充有效目标查询。June Blog Jun10→Jun05，无 Jun07，但不替 Publications 日级覆盖。 |
| Meta | [publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1) 原 HTML 成功294181字符；目标官方域有限搜索 | 当前前缀 Oct20→Oct14后混2019等旧库存，不构成连续 Jun07 历史切片。带 start_date/end_date 的有限恢复仍相同 October 段，未当有效日期过滤。历史目标目录受阻，不能称零发布。 |
| Qwen | GET [EN retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) / [ZH retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN)，`success`，各 `data.articles` 40条 | 读取全部 `extra.date` 与内容 HTML 的日期字段，均无 Jun07；extra.date 最近前 Qwen3.7-Plus Jun01 10:00+08，后 RobotNav/RobotManip/RobotWorld Jun16 08:00+08、RobotSuite10:00+08。HTML 与 extra 存个别日期差异，均不跨入本补窗；不将旧77条配置或空参数接口作证。 |
| DeepSeek | [研究与动态](https://www.deepseek.com/news/) 当次39行 | Research Jun24→Feb25；动态 Sep10→Apr24，到目标前停止，可见索引无 Jun07；“查看全部”保留可见范围局限。 |
| Moonshot | [Platform Blog](https://platform.kimi.com/blog) 实际HTML26个h3文章；[kimi-code releases](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=100) 85条 | Blog 最新2025Nov07，不能证明全部2026；release85首Oct25、末May26，目标前Jun05 `10:26:45Z`、后Jun09 `03:56:11Z`，Jun07 BJT无条目。未扫org commits；误试kimi-cli只作为无效替代，没有据其覆盖目标。 |
| Hunyuan | POST [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，`accept-language:zh`，body `{"pageNum":1,"pageSize":100,"renderType":0}`；code0,totalNum11,list11 | 中文全部11条均核 publicAt、displayPublishTime、publishedAt，未落 Jun07。publicAt邻前Hy-MT2 May21、邻后Hy3 preview July05（展示Apr23，不能拿展示日替实际字段）。不把英语9当中文全部。 |
| Z.ai | [Research](https://www.zhipuai.cn/zh/research)，首14日期行到2025Dec09 | Jun16 GLM5.2→May20 ZCube夹住目标，无Jun07目录项；不把目录日期当 linked-paper first-public。 |
| Seed | [Publications](https://seed.bytedance.com/en/public_papers)，page1/13，1–20/246 | Jun11→Jun04 electron dynamics→Jun03 MetaPoint→May29，已到目标前，不翻后12页；Jun04明确科学领域且窗外，不送入本日贡献池。 |
| ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)，page1/2 | 最新May09→Apr30→Apr15→旧年，到目标前停止；未翻旧page2，无本窗可见条目。 |
| MiMo | [Paper/Blog](https://mimo.xiaomi.com/) 8 papers/15 blogs；[Model Release](https://mimo.mi.com/docs/en-US/updates/model)；首页实际引用的 [route chunk](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js) | Paper Jun29→Mar13，模型更新Sep22→Jun02→Apr23。route metadata明确 inference=`2026-05-30`、UltraSpeed=`2026-06-08`、long-horizon=`2026-06-10`、tool-call-repetition=`2026-09-27`；UltraSpeed当前原页 time=`2026-06-08`。本补窗没有具名Jun07信号；不恢复旧小时窗clock hold、不采用宣传数字。 |
| MiniMax | [EN Blog](https://www.minimax.io/blog)/[中文Blog](https://www.minimaxi.com/blog)，读到Jun09→Jun01→May25；[Agent Research](https://agent.minimax.io/docs/techblog) 4个dated组 | 主Blog无Jun07；Agent已不是旧Navigation壳，实际Oct20两篇/Oct08/Sep22/Sep19（5个标题）全可见，止于Sept19，不据当前保留目录证明此前从未发布。 |
| arXiv | [官方公告规则](https://info.arxiv.org/help/availability.html)；DataCite正控与下面本窗registered查询；5条有限官方域日期/主题搜索；目标日分类列表恢复失败 | Jun07 BJT对应Jun06 12:00→Jun07 12:00 EDT，无正常公告批次；这不是全球首次公开零研究证明。没有搜索得到须读完整摘要的具名本窗论文，不以规则取消外站发现。旧498 NAV及48旧采用不是本次队列。 |

## arXiv 与 DataCite 原字段

官方日程明确周五、周六美东没有公告，new/replacement/withdrawal/crosslist均按公告过程公开；2026-06-07为北京时间周日。最后常规公告在Jun05 08:00 BJT，下次为Jun08 08:00 BJT。仅以此限定常规列表，不推断作者站点无首次公开或无更早正文。

正控：`https://api.datacite.org/dois?client-id=arxiv.content&page[size]=1&sort=-registered` 返回 `meta.total=3221843`，样例 DOI `10.48550/arxiv.math/0504088`、`relationships.client.data.id=arxiv.content`、`state=findable`。正控证明有效client过滤与存在数据；sort并未用作时间覆盖结论。

本补窗：`https://api.datacite.org/dois?client-id=arxiv.content&query=registered:[2026-06-06T16:00:00Z%20TO%202026-06-07T15:59:59Z]&page[size]=100` 返回 `data=[]`，`meta={"total":0,"totalPages":0,"page":1}`。这只报告该原字段查询的结果，不把registered零项升级为全部论文首次公开零项，不以Created替代公开日。

有限搜索实际范围（官方域、每条仅结果页，无结果后不扩年/月）：

- `site:arxiv.org "2026-06-07" "language model"`
- `site:arxiv.org "Sun, 7 Jun 2026" transformer`
- `site:arxiv.org "7 Jun 2026" "large language"`
- `site:arxiv.org "June 7 2026" (training OR inference OR agent OR multimodal)`
- `site:arxiv.org "2026-06-07" (kernel OR world OR MoE OR optimization)`

上述未返回可确认目标正文。`https://arxiv.org/list/cs.CL/260607` 返回 Cache miss，不记空批次或已完整浏览。无日公告批次时没有标题队列，不扩月度2718/旧498。

## 非候选判定与独立校准范围

本次没有先因贡献小而排除后待补日期的研究候选，也没有把80个Qwen条目、全部CVPR论文或其他宽目录送入语义关闭队列。实际代表性导航排除：

- [Google at CVPR 2026](https://research.google/conferences-and-events/google-at-cvpr-2026/) 是June03–07活动/口头报告日程，不能把会议最后一天当全部论文首次公开日；未逐篇宣称已审、也未触发整届会议重扫。
- [Heat resilience](https://sites.research.google/gr/heat-resilience/) 为屋顶albedo及城市热韧性数据应用，标题/核心明确领域应用且论文仅June月份，未发现本项目模型系统机制信号；不以通用Data/Evaluation owner重新引入AI for Science，也不为不影响排除的日期再建请求。
- OpenAI辅助官方域查询出现的是community图像画廊、账户/配额讨论，不是原始研究；不以其日期变成候选，也未据社区描述推断真实产品行为。
- Qwen3.7-Plus、MiMo UltraSpeed、Anthropic n-days 是日期导航而非贡献排除；没有为其在补窗之外的机制另作关闭或低分。

## 外部保留项与旧材料

Google Publications仅年份/动态过滤不能恢复Jun07目标主题日级目录；Meta当前混库存首屏与无效日期参数亦不能恢复该日切片。已尝试官方原页、主题参数与目标官方域查询；无进一步具名论文信号。两项隔离，不授正面Coverage或“无遗漏”；取得原始历史dated feed/list或具体具名正文再定点恢复。MiniMax Agent当前五标题不证明旧历史全文穷尽，Moonshot旧Blog也保留目录限制；不据此承诺全机构覆盖。

旧51 DateHold、旧48候选日期/评分与有效必要位置，继续保留在 [V3_RECOVERY_BLOCKERS](./V3_RECOVERY_BLOCKERS.md)。本次补Jun07不移动Jun08旧归属，不因新合同允许合法联合日证而推翻或重签旧全部日期判断；有具体原件/反例再定点恢复。

作者扫描、日期筛选与报告整理已完成；独立复核由root执行，本文件没有自签通过。
