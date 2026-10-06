# 2025-11-23 有限原源检查

作者Codex / Ohm，实际clock 2026-10-04T19:58:35+08:00。窗口BJT [Nov22 09:00,Nov23 09:00)。全部下列raw与request是本日fresh执行保存；只复用历史规程/API/native路径身份，不复用别日报候选、覆盖计数或完成标签。请求时间UTC、URL/方法/参数/状态/响应头见各`.request.json`。HTML只解析正文与Next Flight，不执行第三方脚本，不进入训练/artifact。

## 十四每日源

| ID | 实际入口、范围及有限停止 | 权限/缺口 |
| --- | --- | --- |
| SRC-OPENAI | 官方Research实际web打开、[RSS](raw-openai-rss.xml)1245条原XML逐日期筛UTC [Nov22 01,Nov23 01)，本窗0。邻近Nov20 14:50Z Foxconn与Nov24 00Z购物/数学研究均在窗外，不移窗。 | 当前保留RSS/首页非删除史保证；无具名本窗材料，未扩大旧公告核心队列。 |
| SRC-ANTHROPIC | [Research](raw-anthropic.html)真实publicationList/Research posts171全数组解析，目标相邻Nov21 14:32Z reward hacking与Nov24 15:10Z browser defenses，后者窗外；无本窗retained post。 | 可执行See more数据已在原Flight返回，不当未完普通分页；不保证删稿/例外，未读邻日前沿附件。 |
| SRC-GOOGLE-AI | [DeepMind](raw-deepmind.html)当前Research主题/近期2026入口、[pubs2025](raw-google-pubs.html)676计数仅发现、[Google Blog2025 p1](raw-google-blog.html)Dec18至Nov12，Nov21后Nov19/18，已越目标窗口，止p2。EV原核心分层范围关闭。 | 必要pubs/DeepMind本窗历史段未恢复，Blog不能替全部来源；未把676变题摘队列。 |
| SRC-META-AI | [Research](raw-meta.html)200反自动化壳，web文本0；精确官方域Nov22 model/training query实际无相关结果，止空入口。 | 历史切片缺失，不记无研究；不反复空检索。 |
| SRC-QWEN | [旧主页](raw-qwen.html)5项最新Sep23至July24，越窗前停止旧Next；[新Research](raw-qwen-research.html)200壳无列表，精确官方域2025-11-22检索未得相关原文。 | 新动态历史列表缺失；本日CUA实际browsers=[]，不假称浏览器已读列表。 |
| SRC-DEEPSEEK | [主页](raw-deepseek.html)Research More所供[本日fresh /news/](raw-deepseek-news.html)实际10个Research标题/日期，目标Nov27 DeepSeekMath-V2至Nov1 LPLB相邻，无本窗留存Research事件；止较旧研究段，不展开窗外正文。[API Updates](raw-deepseek-updates.html)Dec1至Sep29仅release补检，不能替Research。 | 当前10项及相邻日期支持有限停止，非全研究/删除史；查看全部按钮仍不据此宣称不存在更多。无具名本窗事件不扩GitHub。 |
| SRC-MOONSHOT | [Kimi Blog](raw-kimi.html)26个dated条目，Nov7/6至2024 May29，无Next，止尾部；无具名release触发。 | 当前保留目录不保证删稿；不扩组织全部项目。 |
| SRC-TENCENT-HUNYUAN | [Research首页](raw-hunyuan.html)动态壳；浏览器inventory空；实际[POST publicList](raw-hunyuan-p1.json)pageNum1/pageSize20/renderType0，total9，全部displayPublishTime为2026，少于20止p2。精确2025-11-22 Research检索无结果。 | 不能以2026 API数据证明2025无事件；必要2025段终态隔离。 |
| SRC-ZAI | [Research p1](raw-zai.html)blogsItems15/next2/hasMoretrue；实际[p2](raw-zai-p2.html)18/next3/hasMorefalse，非排序createAt最早Dec7，止p3。[release](raw-zai-release.html)Dec22/11/10/8后Sep30。 | 当前Research无November历史，release不替Research；精确中文Nov22 GLM检索空，不扩组织仓库。 |
| SRC-BYTEDANCE-SEED | [官方Research](raw-seed.html)及实际2025 API [blog type2 p0](raw-seed-type2-p0.json)、[paper type1 p0](raw-seed-type1-p0.json)，各18项，total45/94，next20/has_moretrue。分别逐项看PublishDate+IsPinned：未来pinned隔离，最晚非pinned Oct22/21 16Z，已过窗前边界，止20不声称全页读完。 | 有限year切片，pinned不当时序上界；无本窗保留项但不授删除/迁移史无遗漏。 |
| SRC-BAIDU-ERNIE | [p1](raw-ernie.html)10项最低Nov21；实际[p2](raw-ernie-p2.html)6项Nov11/7至June30，1/2 prev无next，止p3。1120原核心关闭，UTC目录字段窗前。 | 不以榜单公告无机制推断整个ERNIE模型无贡献。 |
| SRC-XIAOMI-MIMO | [首页](raw-mimo.html)8dated论文2026至Oct21/Sept19/June4/May12、15undated Blog全返回。[fresh native](raw-mimo-native.js)moreBlogs/p.map与onClick toggle实际核，More非分页，不另猜路由。 | Blog必要日期段缺失；已执行More核查不是普通待办；不全读15窗外/无日期正文。 |
| SRC-MINIMAX | [英文](raw-minimax.html)12/[中文](raw-minimax-zh.html)13dated可见项，Dec23至Oct27边界，中文另Jan15，无观察到分页入口。实际[Agent Tech MD](raw-minimax-tech.md)与[llms索引](raw-minimax-index.txt)52行仅1 Tech条2026-05-13，止当前索引。 | Agent Tech已检查不是未触发/不适用；2025历史段缺失不记零。未将product docs全部扫成Tech。 |
| SRC-ARXIV | [历史commits API](raw-arxiv-help-commits.json)截至窗终最新Aug06 commit95c716…、[exact2025帮助](raw-arxiv-2025-help.md)及[2025存档](raw-arxiv-2025-availability.html)实际读取；IANA换算Fri21 20:00至Sat22 20:00EST，无常规批次。只做官方域Nov22 language-model announcement例外线索检索，空后止。 | 无例外公告线索；不授所有预发/全网0，不造submitted题摘队列。规则涵盖新稿/替换/撤回/cross-list，2025Nov27 holiday窗外。 |

## 本日辅助检索与浏览器

实际web两组四query：`site:ai.meta.com "November 22, 2025" model training`、`site:qwen.ai "2025-11-22" research model`、`site:research.google "November 22, 2025" language model`、`site:deepmind.google "22 November 2025" research`；以及`site:hunyuan.tencent.com/research "2025-11-22"`、`site:zhipuai.cn "2025年11月22日" GLM`、`site:mimo.xiaomi.com "2025-11-22"`、`site:arxiv.org "2025-11-22" "language model" announcement`。第一组只返回Google标签页中2023/其他日期，非Nov22 2025新增；第二组空。精确query只补线索，不替官方目录或证明零研究。此记录保存实际query与结果限度，不从unlabelled empty结果反推输入。

本日CUA getState实际browsers=[]，native app可见但没有可用浏览器控制；未把inventory当Research正文已读。不重试空browser或无限猜API。恢复只接受官方可读本窗历史目录、具名原稿/精确公开范围、重要修订身份等新原源；到达后只开受影响来源/项。

## 筛选、触发与未检查范围

当前确定候选0、采用0、Books No Change建议0写入，尚待非作者实际准入/日级。两目录邻近负侧EV领域应用/ERNIE榜单核心已完整必要读，见[FIRST](FIRST_CALIBRATION_READY.md)，不算本窗两新增。不扫描所有676 pubs、全部arXiv分类/月表/所有submitted题摘、所有组织GitHub或全站删除史。没有具名本窗conference批次、评测suite或重要release/RFC触发，按需未触发；Daily不扫Weekly，周日也不自动扩本次为Weekly。

必要历史缺段：Google pubs/DeepMind、Meta、Qwen、Hunyuan、Zai Research、MiMo Blog、MiniMax Agent Tech；当前可用入口有限处理结束，明确不支持正面证据、Books、性能/安全或无遗漏保证，不列永久普通重试待办。
