# 2025-07-04 机构每日源有限补查

执行日期：2026-10-11。责任：机构来源补查与贡献初筛作者；非本日最终独立复核人。
状态：13/13 个机构每日源已实际尝试，达到下述有界停止点，可交来源/潜力独核；历史来源缺口保留。
这不是机构完整覆盖、全源零命中证明、Evidence完成、Books完成或DAY签名。

## 1. 范围与冻结

- 旧Strict Window保持北京时间2025-07-03 09:00 → 2025-07-04 09:00，旧正式0 / 潜力7与旧正文不改。
- 新增材料只按北京时间2025-07-03完整自然日筛选。机构官方日期仅需日级，不将旧精确时刻要求传播给新增；portal日期不自动等于论文家族首公开日。
- 本文件唯一手工写入；同目录同前缀raw/headers是实际取得的网络响应。未写README、INSTITUTIONS、DAY-RECOVERY、State、Books、合同、索引、代码或任何2026报告，未stage/commit/push。
- root负责arXiv发现池、报告、State、评分与Books，并复核机构来源与具名判断；本轮只为Seed邻项定点核一个版本身份，不扫arXiv列表。Ptolemy作为非本日报告作者负责最终DAY独立复核，人类用户不承担独核职责。
- 已重读AGENTS、Research/Report合同、Sources使用说明及每日组、Prompt、ROADMAP、本日README/INSTITUTIONS/DAY-RECOVERY；State2025只作本日路由。未加载其他日源包、Weekly或全年待审队列。
- 旧包入口及候选冻结可复用；下表日期导航、数组和失败均是本轮实际观察，没有把旧跨日缓存或旧作者浏览器失败当成本轮读取证据。

## 2. 13源实际边界

Google DeepMind/Research依注册表合为SRC-GOOGLE-AI一源，以下共13源，不含SRC-ARXIV。“未见”仅指实际得到的有限页段、数组或feed。

| 来源ID | 查哪里、到哪里 | 结果、停止与限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) → [index](https://openai.com/research/index/)；[RSS](https://openai.com/news/rss.xml) XML1287个item，逐项过滤日期元数据。 | RSS本日未见，邻项07-01 Genspark、07-08 AFT。Research/index当前卡片未到2025-07；止于当前index与有限feed，不声称旧Research全部在RSS。旧1247不是当前数量。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) HTML；HTMLParser取Next script，JSON解码self.__next_f.push字符串，177次publishedOn、168个不同时间值。 | 07-15 Claude4 cyber与06-27 companionship/Project Vend之间未见07-03，ISO元数据按北京时间取日。168不是去重论文数。止于本Research响应，不扩新闻或全年题摘。 |
| SRC-GOOGLE-AI | Google [七月博客](https://research.google/blog/2025/07/)9条；[Publications](https://research.google/pubs/)首页；DeepMind [Research](https://deepmind.google/research/) → [Publications](https://deepmind.google/research/publications/) → 真实[page/2](https://deepmind.google/research/publications/page/2/)；[Blog page/6](https://deepmind.google/blog/page/6/)。 | Google博客07-02 Sound Localization → 07-09 MedGemma无本日项。DeepMind publication page2为07-13三项 → 07-01 Rethinking Example Selection → 06-26，实际跨本日，但目录自称selection。Google Publications首页1–15/11612、2025 facet680只是当前表单，未得到有效2025日级历史切片；curl超时不能写零命中。博客不能代替论文。止于这些页与本日搜索，不遍历680或265项。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)实际curl connection reset；web open0行；官方域名本日搜索。 | 必要Research内容未恢复；搜索未给相关官方研究结果，不是机构无发布证明。保留外部缺口，停止重复请求，不写零命中。 |
| SRC-QWEN | [首页](https://qwenlm.github.io/)实际Next → [page/2](https://qwenlm.github.io/page/2/)，第二页另存HTTP200。 | 日期跨本日：07-22 Qwen3-Coder → 06-27 TTS → 06-26 VLo。两页未见07-03，止于跨越，不扩新站全年历史。 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/) → API docs；实际取得[Change Log](https://api-docs.deepseek.com/updates/)。 | 本日相邻08-21 V3.1 → 05-28 R1-0528无07-03。止于日志日期段与首页，不遍历仓库/全年论文；日志不等于所有研究历史。 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)，本轮web读到26个带日级日期目录项。 | 07-17 Playground → 07-11 K2 → 05-06 Thinking API，未见07-03。止于该页，不扫组织仓库，未用旧跨日缓存冒充本轮原件。 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) skeleton；本轮动态浏览器不可用；读其直接引用的主JS、/blog列表与API模块，核/research与/blog共用列表；POST[publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，pageNum1/pageSize20/renderType0。 | JS明确0为“全部”、1论文、2模型。响应code0,totalNum9,list9，日级2026-02-03至09-22，全为2026。确认当前All返回9条，不证明2025历史Research不存在。止于该接口、本日搜索，保留历史目录缺口；不再误称仅普通博客，也不伪装成功浏览器观察。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)HTTP200；客户端“查看更多”确实写page参数，本轮取[page=2](https://www.zhipuai.cn/zh/research?page=2)；[release notes](https://docs.z.ai/release-notes/new-released)。 | 首页15卡片止2025-12-09；page2可见18卡片与“没有更多”，增12-21 GLM-4.7、12-08 AutoGLM、12-07 GLM-4.6V，不是完全相同页；仍未恢复07-03，release notes止09-30。纠正旧“page2完全相同”的当前描述，不以“没有更多”证明无旧发布。止于两页和本日搜索，保留旧目录缺口。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)、[Public papers](https://seed.bytedance.com/en/public_papers)首查；官网主JS给GET /api/get_article_list_v2。2025、count20、order_desc=true、x-tt-locale:US，type1/2各token0/20，共4请求。 | type1真数组18+20=38,total94；type2真数组18+18=36,total45；四响应has_more=true。type1邻项07-04 ByteDexter → 06-27 Hessian；type2 07-14 ICML → 06-28 Embedding，均跨本日。止token20，不翻40，不做94/45全池队列。实返不足20不补造。portal日期不证明家族首公开。邻项见§4。 |
| SRC-BAIDU-ERNIE | [博客首页](https://ernie.baidu.com/blog/zh/) → 实际Next [page/2](https://ernie.baidu.com/blog/zh/page/2/)，末页2/2。 | 08-14 FastDeploy2 → 06-30 ERNIE4.5，无07-03；止博客末页，不扫仓库/全历史论文。 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)8Paper/15Blog；主JS真实chunk映射恢复8557首页模块、6159列表/Paper模块。 | Paper是date数组slice().reverse()，8项含4条2025/4条2026，09-19 MiMo-Audio → 06-04 MiMo-VL。Blog当前本地固定15项，initialVisibleCount8；slice(0,c)/slice(c)与More只切本地展示，不是网络历史分页。不能全写2026：[HSS末项](https://mimo.xiaomi.com/blog/mimo-v2-flash-hss)官方日期2025-12-22。未逐条取得15博客日期，不声称全博客日级排除/全历史无遗漏。止本地列表及本日搜索，保留旧Blog历史缺口。最初漏async/的两个JS404，修正后200才用于判断。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)、[中文Blog](https://www.minimaxi.com/blog)转到minimax.cn；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)；本日搜索定位官方News。 | 英文目录止10-27 M2，中文还列01-15 MiniMax-01，日期跨本日；Agent目录3条均2026，不读全文。News找到07-03 Hailuo-02/Envato，完整核心已核，C见§4。止两个博客首页、Agent目录、一篇本日News，当前Research列表不能替代全站历史。 |

## 3. 可重现方法与工具观察

### 实际数组/分页

- Seed接口为 `https://seed.bytedance.com/api/get_article_list_v2?article_type={1|2}&publish_year=2025&count=20&page_token={0|20}&order_desc=true`，请求头 `x-tt-locale: US`。JSON parser读取sub_article_list、ArticleMeta.ID/PublishDate、ArticleSubContentEn.Title；毫秒时间戳按北京时间取日。type1=Publication，type2=Blog，来自官网主JS而非猜测year路由。
- Publication两页日期范围12-15→06-26、06-20→05-20；Blog两页12-24→06-25、06-18→02-12。四响应next_page_token为20/40且has_more=true。38/36是实际返回数，不按count20宣称40/40，不由导航跨越升级到全池穷尽；本日外只核目录日期/身份，不转入题摘队列。
- 混元主JS实际route `/research` 的index组件为Blog；列表模块renderType0=All、1=Papers、2=Models，API模块原文POST `/api/blog/publicList`。列表页默认大pageSize不要求照搬；本轮20已大于total9，没有继续分页。本轮浏览器结果是 `Browser is not available: iab`，后续 `listBrowsers=[]`；无截图/成功DOM读取，不继承旧协调者30秒超时。
- 混元9项日级范围为2026-02-03 Learning from context、02-13 RLVR、04-23 Hy3 preview、04-30 context、07-08 Hy3、07-21 Hyra、08-06 ELR、08-28 Hy4 preview、09-22 larger batches。仅元数据定位，不研究2026全文，也不据此消灭2025历史缺口。
- 智谱page2确实增加卡片，不能永久继承旧“假分页”结论；18卡片止12月仍不够本日历史。MiMo8557/6159源码核本地显示逻辑，不是浏览器执行证明；其15博客包括2025-12-22 HSS，不能概括全2026。
- DeepMind publication page2来自真实href `/research/publications/page/2/`，不是错用 `?page=2`。Google Research `?category=2025&search=language%20model` 与DeepMind `?year=2025` 曾被web报不可访问，未证明参数有效，不计为2025查询零命中。Google Research历史论文切片未恢复。

### 有限日期搜索

本轮13个查询只用于本日定位，不作为完整覆盖或全池待审列表：

| 组 | 实际查询字符串 |
| --- | --- |
| 1 | `site:openai.com "July 3, 2025"`；`site:anthropic.com "July 3, 2025"`；`site:ai.meta.com "July 3, 2025"`；`site:research.google "July 3, 2025"` |
| 2 | `site:seed.bytedance.com "2025-07-03"`；`site:minimax.io "July 3" "2025"`；`site:hunyuan.tencent.com "2025" "07-03"` |
| 3 | `site:mimo.xiaomi.com "2025" "July" "3"`；`site:zhipuai.cn "2025" "7月3日"`；`site:ai.meta.com "July 3, 2025" research` |
| 4 | `site:research.google "July 3, 2025" "language"`；`site:deepmind.google "July 3, 2025"`；`site:ai.meta.com "July 3" "2025" LLM` |

组1主要出现OpenAI Community，不作为OpenAI官方研究。组2恢复MiniMax官方News；*.space.minimax.io用户托管页不是机构发布，未继续打开。组3/4未返相关结果，不据此消灭缺口。

web可读内容是本次工具返回，不伪称curl原件或2025历史快照：Google七月博客9项、DeepMind Blog page6/publication page2、Kimi与ERNIE目录、MiniMax Agent目录均实际看到§2页段。web不给HTTP状态时不虚构状态。没有执行浏览器复现；独核可用本地原件重算JSON/SSR元数据，只有web观察的段落只能继承本作者本次tool observations或自行复现。

## 4. 新具名材料与贡献筛选

### C1. Hailuo-02 is Now Integrated into Envato's VideoGen

- 主源：[MiniMax官方News](https://www.minimax.io/news/hailuo-02-is-now-integrated-into-envatos-videogen)，官方日级日期 **2025-07-03**；[完整原响应](./institutions-supplement-20261011-minimax-envato.raw)。web核日期、标题和全部短正文，不只搜索片段。
- 完整核心：已有Hailuo-02接入Envato VideoGen，创作者以文本/图片提示生成短视频；宣传质量、可控性、成本效率，但未披露新训练、结构、推理/数据机制或新的可核验对比实验。
- 准入句：**C，既有模型的渠道/产品集成，没有新增模型或系统研究贡献。**“extreme physics”无配套机制/实验，不能采用为物理因果理解或控制保证。不是因评分低、收费、日期未知或Books已有覆盖而排除。
- 不新增正式/潜力，不要求评分/Deep Review，不声明Books Existing Coverage。若另有本日首公开技术报告带新机制/实验，按该新身份重开，不由营销措辞自动触发。

### 邻项N1. Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting

- Seed type1 token0 ID294，portal日级 **2025-07-04**；仅定点核[2507.03227v1](https://arxiv.org/abs/2507.03227v1)并完整读取AB，[版本原件](./institutions-supplement-20261011-bytedexter-identity.raw)。
- 完整AB核心：高自由度手的示教质量约束模仿学习；提出20-DoF连杆驱动仿人手、实时优化式人体动作重定向与手臂协调；以手内操作及九物体杂乱化妆桌整理验证遥操作和示教生成。
- 贡献预判：**窄P型系统/表示控制材料**，硬件加运动重定向不是成熟模型简单下游拼装。可关注人体手势到机器人关节映射、实时保真和手臂协调；“高质量示教”不等于已验证训练后策略泛化。未评分/读PDF，不是Evidence完成或Books采用。
- 版本页日级Submitted on 4 Jul 2025，与portal07-04一致；不以原小时窗口union迁入07-03补充。未证明更早项目页家族首公开，也不声称全家族不存在更早公开。**本轮新增潜力仍0**；这是本日外邻项身份核对，交root避免日期混入，不扩项目/仓库历史，不要求为此审全篇。

## 5. 可结束边界与未决

- 本轮新增本日正式 **0**、本日潜力 **0**、本日具名C **1**、本日外邻项AB/版本核对 **1**。原正式0/潜力7及既存审阅不在本轮改判；本轮0不意味着旧7已关闭。
- 13/13是已实际尝试，不是13/13正面Coverage。Google Research必要历史论文切片、Meta Research、混元2025历史Research、智谱旧Research、MiMo旧Blog等缺口保留；RSS、DeepMind selection和其他博客也不证明机构全量完整覆盖。
- 可执行的有限入口、真实分页/数组/接口、日级定位已尝试并到上述停止点，不编造“必须作者澄清才能读原文”的受阻。没有留下已定位且符合本日日期的新P核心未读任务。未用全年待审队列补缺，不按可达性预先降分。
- 若实际恢复到明确2025-07-03官方旧目录段、遗漏相关题摘或本日首公开家族身份，按该页段/身份定点重开；混元浏览器恢复时也仅核本日与邻接日期段，不追全站。
- 包可交来源/潜力独核。arXiv新增、Evidence、Books、六部分与最终DAY由root及非本日报作者独核完成；本文件不授正面Coverage/Evidence，不签DAY。

## 6. 实际请求收据

日期2026-10-11；时间为请求调用记录的UTC起点，不是文章公开时刻。exit/HTTP为实际curl退出码/响应状态；HTTP000表示没取得HTTP响应，非网站状态码000。只有headers且0字节的失败没有raw正文。HTTP404原件保留，正确async路径200才用于逻辑判断。其余web观察见§2/3。

| 名称 | 起点UTC | exit/HTTP | 字节 | 本地证据 |
| --- | --- | --- | --- | --- |
| openai-rss | 04:09:06 UTC | 0 / 200 | 784414 | [headers](./institutions-supplement-20261011-openai-rss.headers) / [原响应](./institutions-supplement-20261011-openai-rss.raw) |
| anthropic | 04:09:07 UTC | 0 / 200 | 282283 | [headers](./institutions-supplement-20261011-anthropic.headers) / [原响应](./institutions-supplement-20261011-anthropic.raw) |
| google-july | 04:09:08 UTC | 28 / 000 | 0 | [headers](./institutions-supplement-20261011-google-july.headers); 无正文 |
| meta | 04:09:09 UTC | 35 / 000 | 0 | [headers](./institutions-supplement-20261011-meta.headers); 无正文 |
| qwen-page2 | 04:09:09 UTC | 0 / 200 | 17379 | [headers](./institutions-supplement-20261011-qwen-page2.headers) / [原响应](./institutions-supplement-20261011-qwen-page2.raw) |
| ernie-page2 | 04:09:10 UTC | 0 / 200 | 20533 | [headers](./institutions-supplement-20261011-ernie-page2.headers) / [原响应](./institutions-supplement-20261011-ernie-page2.raw) |
| mimo | 04:09:10 UTC | 0 / 200 | 58220 | [headers](./institutions-supplement-20261011-mimo.headers) / [原响应](./institutions-supplement-20261011-mimo.raw) |
| seed-research | 04:12:08 UTC | 0 / 200 | 114100 | [headers](./institutions-supplement-20261011-seed-research.headers) / [原响应](./institutions-supplement-20261011-seed-research.raw) |
| hunyuan | 04:12:09 UTC | 0 / 200 | 6893 | [headers](./institutions-supplement-20261011-hunyuan.headers) / [原响应](./institutions-supplement-20261011-hunyuan.raw) |
| hunyuan-api | 04:12:09 UTC | 0 / 200 | 315236 | [headers](./institutions-supplement-20261011-hunyuan-api.headers) / [原响应](./institutions-supplement-20261011-hunyuan-api.raw) |
| zai | 04:12:09 UTC | 0 / 200 | 1276424 | [headers](./institutions-supplement-20261011-zai.headers) / [原响应](./institutions-supplement-20261011-zai.raw) |
| seed-main | 04:15:57 UTC | 0 / 200 | 1857907 | [headers](./institutions-supplement-20261011-seed-main.headers) / [原响应](./institutions-supplement-20261011-seed-main.raw) |
| deepseek-updates | 04:15:57 UTC | 0 / 200 | 48079 | [headers](./institutions-supplement-20261011-deepseek-updates.headers) / [原响应](./institutions-supplement-20261011-deepseek-updates.raw) |
| minimax-envato | 04:15:58 UTC | 0 / 200 | 64760 | [headers](./institutions-supplement-20261011-minimax-envato.headers) / [原响应](./institutions-supplement-20261011-minimax-envato.raw) |
| deepmind-pubs | 04:15:58 UTC | 0 / 200 | 142513 | [headers](./institutions-supplement-20261011-deepmind-pubs.headers) / [原响应](./institutions-supplement-20261011-deepmind-pubs.raw) |
| google-pubs | 04:16:00 UTC | 28 / 000 | 0 | [headers](./institutions-supplement-20261011-google-pubs.headers); 无正文 |
| seed-type1-token0 | 04:17:15 UTC | 0 / 200 | 49455 | [headers](./institutions-supplement-20261011-seed-type1-token0.headers) / [原响应](./institutions-supplement-20261011-seed-type1-token0.raw) |
| seed-type2-token0 | 04:17:16 UTC | 0 / 200 | 41802 | [headers](./institutions-supplement-20261011-seed-type2-token0.headers) / [原响应](./institutions-supplement-20261011-seed-type2-token0.raw) |
| mimo-main | 04:17:16 UTC | 0 / 200 | 22556 | [headers](./institutions-supplement-20261011-mimo-main.headers) / [原响应](./institutions-supplement-20261011-mimo-main.raw) |
| zai-main | 04:17:16 UTC | 0 / 200 | 18362 | [headers](./institutions-supplement-20261011-zai-main.headers) / [原响应](./institutions-supplement-20261011-zai-main.raw) |
| deepmind-pubs2 | 04:17:16 UTC | 0 / 200 | 143342 | [headers](./institutions-supplement-20261011-deepmind-pubs2.headers) / [原响应](./institutions-supplement-20261011-deepmind-pubs2.raw) |
| seed-type1-token20 | 04:18:28 UTC | 0 / 200 | 53526 | [headers](./institutions-supplement-20261011-seed-type1-token20.headers) / [原响应](./institutions-supplement-20261011-seed-type1-token20.raw) |
| seed-type2-token20 | 04:18:29 UTC | 0 / 200 | 38756 | [headers](./institutions-supplement-20261011-seed-type2-token20.headers) / [原响应](./institutions-supplement-20261011-seed-type2-token20.raw) |
| zai-page2 | 04:18:29 UTC | 0 / 200 | 1397497 | [headers](./institutions-supplement-20261011-zai-page2.headers) / [原响应](./institutions-supplement-20261011-zai-page2.raw) |
| mimo-8557 | 04:18:30 UTC | 0 / 404 | 190 | [headers](./institutions-supplement-20261011-mimo-8557.headers) / [原响应](./institutions-supplement-20261011-mimo-8557.raw) |
| mimo-6159 | 04:18:31 UTC | 0 / 404 | 190 | [headers](./institutions-supplement-20261011-mimo-6159.headers) / [原响应](./institutions-supplement-20261011-mimo-6159.raw) |
| bytedexter-identity | 04:18:32 UTC | 0 / 200 | 42775 | [headers](./institutions-supplement-20261011-bytedexter-identity.headers) / [原响应](./institutions-supplement-20261011-bytedexter-identity.raw) |
| mimo-8557-async | 04:18:53 UTC | 0 / 200 | 7920 | [headers](./institutions-supplement-20261011-mimo-8557-async.headers) / [原响应](./institutions-supplement-20261011-mimo-8557-async.raw) |
| mimo-6159-async | 04:18:53 UTC | 0 / 200 | 25477 | [headers](./institutions-supplement-20261011-mimo-6159-async.headers) / [原响应](./institutions-supplement-20261011-mimo-6159-async.raw) |
| minimax-blog-cn | 04:18:53 UTC | 0 / 200 | 144114 | [headers](./institutions-supplement-20261011-minimax-blog-cn.headers) / [原响应](./institutions-supplement-20261011-minimax-blog-cn.raw) |
| minimax-blog-en | 04:18:54 UTC | 0 / 200 | 134698 | [headers](./institutions-supplement-20261011-minimax-blog-en.headers) / [原响应](./institutions-supplement-20261011-minimax-blog-en.raw) |
| hunyuan-main | 04:19:57 UTC | 0 / 200 | 542746 | [headers](./institutions-supplement-20261011-hunyuan-main.headers) / [原响应](./institutions-supplement-20261011-hunyuan-main.raw) |
| mimo-hss-date | 04:19:57 UTC | 0 / 200 | 64692 | [headers](./institutions-supplement-20261011-mimo-hss-date.headers) / [原响应](./institutions-supplement-20261011-mimo-hss-date.raw) |
| zai-releases | 04:19:58 UTC | 0 / 200 | 254035 | [headers](./institutions-supplement-20261011-zai-releases.headers) / [原响应](./institutions-supplement-20261011-zai-releases.raw) |
| hunyuan-list-js | 04:20:58 UTC | 0 / 200 | 10220 | [headers](./institutions-supplement-20261011-hunyuan-list-js.headers) / [原响应](./institutions-supplement-20261011-hunyuan-list-js.raw) |
| hunyuan-api-js | 04:20:59 UTC | 0 / 200 | 429 | [headers](./institutions-supplement-20261011-hunyuan-api-js.headers) / [原响应](./institutions-supplement-20261011-hunyuan-api-js.raw) |

## 7. 本地检查

- 已用本地结构化解析重算：RSS1287、Anthropic177次publishedOn/168个不同时间值，两者按北京时间2025-07-03过滤均无该日项；Seed四数组18/20/18/18、total94/45与has_more/next符合§2/3；混元total/list为9/9。
- 本文件71次本地引用均存在，来源表13行/13个唯一ID；请求收据36行，全部有正文的原件字节数与收据一致。0字节失败的headers只证明实际请求留存，不证明正文恢复。
- 首次新文件限定空白检查报EOF多一空行（退出3），已仅在本文件修复。no-index diff复查退出1、无空白诊断（新增文件有diff，不误报退出0）；另用本地检查确认无行尾空白及EOF多空行。本日限定git diff --check退出0，但它不覆盖未跟踪新文件；本地引用复查无缺项、表格列数无错误。没有运行本日报告V3，不能由来源文件格式检查宣称报告或DAY通过。
