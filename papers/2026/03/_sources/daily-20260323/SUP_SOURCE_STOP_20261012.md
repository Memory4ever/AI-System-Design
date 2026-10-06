# 2026-03-23 来源遗漏补充：03-22 自然日

作者：supp_mar23。执行时间：2026-10-12T05:53～06:01+08:00。仅补北京时间2026-03-22完整自然日；原报告[03-22T09,03-23T09)窗口、Sora候选/4分/03-23日期与原§4连续正文冻结。旧完成声明不替代本次验收。未读Weekly，未启动Live/其他日期，未改共享Books/LS/索引，未stage/commit/push。

本轮实际重读AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、RESEARCH_SOURCES使用说明/Daily14/arxiv范围及ROADMAP；LS只作路由。不以旧Submitted检索池扩队列，不把机构当前宽目录的窗外文章送入正文审阅。

## 1. 实际入口与有限停止

下面都是本轮独立公开GET/POST或网页读取；日期只用于自然日定位。网页提取失效的RSS/API均用公开原始响应恢复，不以空提取授阴性。引用旧原件时限定身份/日期metadata，而非继承旧小时门/完成声明。

| 来源 | 本轮实际读取与停止 | 当日判断及未恢复部分 |
| --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)公开GET784414B，1287 items；03-21～23原日期筛查仅Sora `Mon, 23 Mar 2026 00:00:00 GMT` | BJT03-23，非补充窗；原候选保持，不重复审阅/计数。RSS有限存留，不证明被删除历史 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)GET282283B，177个publishedOn；9个March日期/相邻slug完整读 | 无03-22；三Science `2026-03-23T23:00:00.000Z`=BJT24日，最近前文03-13。只核日期，不拿窗外core入本日 |
| SRC-GOOGLE-AI | [March archive](https://research.google/blog/2026/03/)完整12卡；[page2](https://research.google/blog/2026/03/?page=2)网页不可提取后GET163717B恢复，03-06/03-04两卡，2/2；[DeepMind page3](https://deepmind.google/blog/page/3/)完整24卡，March六身份与旧SOURCE原值一致，复用其17/26/25/10/03日期而非重审全文。[Pubs2026](https://research.google/pubs/?year=2026)GET336107B，无datePublished/datetime字段 | 可见Blog无03-22；Pubs本日foundation/训练/推理/多模态dated历史切片仍缺，S1 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)网页0行，但GET278821B无datePublished/publishedOn/datetime。Engineering [首页](https://engineering.fb.com/)、[page2](https://engineering.fb.com/page/2/)、[page3](https://engineering.fb.com/page/3/)完整可见卡，停止March13/17/18→30/31邻界；不是沿旧2页号 | Research本日dated切片仍S2；Engineering有限三页无03-22，不授全机构历史 |
| SRC-QWEN | [公共API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)GET4781799B，40 articles，只有articles数据键无total/paging；全部title/path与extra.date独立读，对应[旧metadata](V3_QWEN_METADATA.md)身份/原值一致 | March只有MaxPreview19与Omni30，无22；不把40篇全文计已审 |
| SRC-DEEPSEEK | [News/Research](https://www.deepseek.com/en/news/)39行，当前News5/Research10；已观察[公开脚本](https://www.deepseek.com/_next/static/chunks/app/%5Blocale%5D/news/page-bd765c90dd4eb584.js)本轮9467B，g最新Jun24→Feb25，News完整16原日期与[V3_SOURCE_STOP](V3_SOURCE_STOP.md)同身份字段有效复用 | 有限当前目录无March22，不保留假隐藏目录故障；不授全历史 |
| SRC-MOONSHOT | [Kimi官方Blog](https://www.kimi.com/en/blog/)156行19卡，全部日期/标题可见；July16→April20→Feb09→2025/2024止 | 可见无March22；不扩GitHub、不把旧platform截止2025当故障 |
| SRC-TENCENT-HUNYUAN | [公开列表API](https://api.hunyuan.tencent.com/api/blog/publicList)POST pageNum1/pageSize20/renderType0，accept-language zh、Content-Type JSON、Origin官网；442610B，totalNum11/list11，全部id/title/publishedAt独立读；原display字段按同身份旧SOURCE复用。一次不带zh仅9 EN项不认证CN | Feb03/13→April23/30邻界，无22；publishedAt不替换display firstpublic |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)175行15完整可见卡，Aug→Apr01→Mar15→Feb21/11→2025；停当前可见 | 无22，不扩GitHub，不授全部历史 |
| SRC-BYTEDANCE-SEED | [论文相邻页](https://seed.bytedance.com/api/get_article_list_v2?publish_year=2026&count=100&order_desc=false&article_type=1&page_token=20)及[Blog](https://seed.bytedance.com/api/get_article_list_v2?publish_year=2026&count=100&order_desc=false&article_type=2&page_token=0)，明确header `x-tt-locale: US`：18/82,next40,true；14/19,next空,false，所有ID/PublishDate独立读。默认实际14/82、Blog9/23 next20＋下一3/23，只作locale差异，不冒认US | US论文20→21→23→24日，无22；1337 UTC22T16=BJT23，非补窗不重开其AIforScience。US Blog缺5身份/本日切片S3，不沿next40扩库存 |
| SRC-BAIDU-ERNIE | [zh Blog](https://ernie.baidu.com/blog/zh/)68行10卡May09/Apr30/15→Feb06/Jan29/15→2025，下一页指示2/2；本轮停止第一页跨本日邻界，不沿旧分页完整断言 | 可见无March22；有限目录非删除历史证明 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)338行/GET58220B，8 dated Paper/15 undated Blog；全部可见metadata实际读；Pro/Omni同身份旧原页明确March18有效复用，不重审正文；TTS仅标题/资源图，不猜route | dated Paper Mar13→Jun29无22；Blog/TTS本日dated历史切片与身份/公开日期S4，不能以undated标题判无事件 |
| SRC-MINIMAX | [EN Blog](https://www.minimax.io/blog)76行12卡/[CN](https://www.minimaxi.com/blog)68行13卡，March18→Feb12/14、后April/May；[AgentTech](https://agent.minimax.io/docs/techblog)当前66行3项Oct08/Sep22/Sep19，不沿旧May13单entry完成声明 | 当前可见均非22；目录有限，未扩guide/GitHub或把当前删除/换版证明历史零条 |
| SRC-ARXIV | [官方availability](https://info.arxiv.org/help/availability.html)实际170–189：public Sun–Thu，EDT Sunday20=UTC03-23T00=BJT03-23T08；March22 BJT通常无scheduled batch，但不据此授全历史零。[cs.CL March show25](https://arxiv.org/list/cs.CL/2026-03?show=25)读月header2138/1–25而无分日，首尾是March早段，不扩月队列；[cs.DC March250](https://arxiv.org/list/cs.DC/2026-03?show=250)当前cache miss，旧有效月header不能恢复日证 | 本日相关announcement/重要revision/延迟旧Submitted公开历史切片S5仍缺。旧27 earliest scheduled23不转成新22候选，也不移动旧归属 |

补检仅发现线索，不是新固定源：搜索 `site:arxiv.org "22 Mar 2026"` 和 `"2026-03-22"` 分别配(language model / Transformer / MoE)、(multimodal / world model / VLA)、(agent / GPU / inference)。六有限查询未返回命中，不把搜索空响应当Coverage或零论文证明；原始入口无可确认当日新身份，未建立题摘/全文数量目标。

## 2. 决定性原值与身份边界

Seed US paper18（ID=PublishDate epoch ms，独立实际响应）：

```text
1992=1772020800000;1412=1772121600000;1420=1772121600000;1411=1772294400000;
1607=1772294400000;1644=1772380800000;1664=1772380800000;1424=1773244800000;
1414=1773504000000;1426=1773590400000;1661=1773936000000;1407=1774022400000;
1337=1774195200000;1334=1774281600000;1428=1774281600000;1606=1774368000000;
1335=1774454400000;1336=1774454400000.
```

US Blog14：

```text
1939=1770825600000;1806=1770912000000;1801=1770998400000;2155=1771171200000;
1202=1774972800000;1798=1775664000000;2132=1776873600000;2152=1781798400000;
1949=1782172962000;1950=1783353600000;2159=1783440000000;1788=1784476800000;
1970=1785427200000;2186=1785859200000.
```

nearest paper1407 BJT21日00，1337 BJT23日00；本轮不以UTC22日误记BJT22。OpenAI Sora UTC23日00=BJT23日08，原候选保留，不为匹配新自然日而搬移。Anthropic三文UTC23日23=BJT24日07。同identity原日期/有效研究可以复用，不继承旧hour-gate结论。

补充确定候选0，新增评分0，新增证据采用0，Books新写0。未发现值得展开的新当日身份，也未把旧27日期保留当新全文队列；不存在“潜力明确但深审费时而排除”。旧27请求与19469中心predicate冲突继续原样保留，不清除或用新增0覆盖。

## 3. 本次安全终态及独立验收入口

五类补充窗保留项S1 GooglePubs dated主题切片、S2 Meta Research dated主题切片、S3 SeedUS Blog未返回5身份/本日metadata、S4 MiMo datedBlog/TTS身份公开日、S5 arXiv相关announcement与重要revision历史切片。仅接受官方dated原始目录/分页、原公告或具有公开语义的metadata；不以当前首页、submitted/updated、月header或搜索0代替。它们不支持正面Coverage、Evidence、Books或无遗漏断言；外部材料以后出现只重开对应来源/identity/03-22时段。

普通作者工作已到有限停止；没有新单篇需要PRE/Books锁/POST，但非作者完整六部分DAY仍待root。原§4不改，所有新增过程依据只在本文件，正式六部分保留关键判断。

root独立DAY反馈（2026-10-12，本轮后续）：实际完整读正式126行六部分与本文件全本，核14入口/有限停止、US/default原值差额、BJT22及Sora/Seed/Science窗外分责、0新增与五限制隔离；旧28题摘/27门不作为新队列，不授历史全覆盖。root独立冻结比较均True，当前V3与限定diff通过，判本轮增量DAY PASS；作者据此更新正式完成态，未自签。完成只限本日有限来源及0新增，不表示全互联网无遗漏，未启动下一日。

作者静态检查：本日V3实际通过；原窗口、原1候选完整行/日期/评分、原§4连续全文逐字相同，六标题正好1～6；11个正式本地引用存在；本日限定cached/unstaged diff-check通过。补查前原V3全文在[baseline-before-supplement-20261012.md](baseline-before-supplement-20261012.md)，仅冻结兼容不授语义完成。机器通过不是DAY；本轮非作者结论未自签。
