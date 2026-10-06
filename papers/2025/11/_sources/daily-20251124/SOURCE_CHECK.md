# 2025-11-24 作者有限来源检查

作者Codex / Ohm；记录时间2026-10-04T20:23:06+08:00，工具clock 12:23:06 UTC。窗口BJT `[2025-11-23T09:00:00+08:00,2025-11-24T09:00:00+08:00)`，UTC `[Nov23 01:00,Nov24 01:00)`。

本日fresh重读AGENTS、研究/Report合同、每日与arXiv来源使用说明、Prompt、ROADMAP及最新checkpoint仅路由。原请求本日20:06起实际执行，每个`raw-*`的`.request.json`保存URL、GET/POST、payload、检查时间、状态及成功响应头。不继承23候选/零结论；仅复用通用抓取/结构化解析代码与已核native入口身份。下列结果是实际返回切片，不保证全部研究或删稿历史。

## 1. 十四每日来源与有限停止

| 来源 | 实际原响应、读到哪里与停止 | 结果及限制 |
| --- | --- | --- |
| SRC-OPENAI | [RSS](raw-openai-rss.xml)1245条按UTC窗口筛，两唯一家族：Shopping Research、GPT-5数学发现。两个pubDate均`Mon, 24 Nov 2025 00:00:00 GMT`，即BJT08:00，完全落窗。[原web核心](raw-web-core.json)实际完整读正文与关键限制。 | 原公告核心已恢复；直接GET两个403文件是错误页，不作正文。RSS非删稿全集，两命中不是两确定候选。 |
| SRC-ANTHROPIC | [Research原HTML](raw-anthropic.html)Next Flight结构化解码publicationList/Research posts171项，目标相邻Nov21 14:32Z reward hacking至Nov24 15:10Z browser defenses；后一项已在窗终之后。See more数据已包含数组，无未处理分页。 | 留存数组无本窗项，不授删除/例外历史保证。无需盲扫其他publication类型或完整版本史。 |
| SRC-GOOGLE-AI | [DeepMind](raw-deepmind.html)实际216文本行当前主题/2026发布，不恢复2025；[pubs2025](raw-google-pubs.html)计676仅发现；[Blog2025 p1](raw-google-blog.html)实际Dec18至Nov12，Nov21之后Nov19/18，停止p2旧段。 | 必要pubs/DeepMind本窗历史段受阻；Blog不能替来源组。不把676变题摘或全文队列。 |
| SRC-META-AI | [Research](raw-meta.html)200但反访问壳，仅一文本行，不能当研究列表；有限辅助线索无恢复。 | 2025本窗历史段受阻，不记零研究、不反复同空入口。 |
| SRC-QWEN | [旧主页](raw-qwen.html)5保留条目，最新Sep23，越窗前停止Next；[新Research](raw-qwen-research.html)200动态壳，无可读历史列表。 | 新历史段受阻。没有逐站声称浏览器检查通过，也不继承23浏览器inventory空的结论。 |
| SRC-DEEPSEEK | [首页](raw-deepseek.html)Research More所供[本日fresh /news/](raw-deepseek-news.html)实际10个Research标题/日期，目标Nov27 DeepSeekMath-V2至Nov1 LPLB相邻，无本窗留存Research事件；止较旧研究段，不展开窗外正文。[Updates](raw-deepseek-updates.html)Dec1至Sep29只release补检，不能替Research。 | 当前10项及日期邻接支持有限停止，非全部Research或删除史；不据查看全部按钮宣称不存在更多。 |
| SRC-MOONSHOT | [Kimi Blog](raw-kimi.html)26 dated条目，Nov7/6至2024May29，停止当前尾部，无具名本窗release触发。 | 当前保留目录无本窗事件，不扩历年GitHub。 |
| SRC-TENCENT-HUNYUAN | [Research](raw-hunyuan.html)动态壳；[actual POST](raw-hunyuan-p1.json) `pageNum=1,pageSize=20,renderType=0`，total9，displayPublishTime均2026Feb3至Sept21，不足20停止p2。 | 2025历史Research受阻。IAB实际可用，但创建本源tab30秒超时并重置，随后getTab返回Tab not found；未获得浏览器渲染列表，不将这条可执行入口伪称未试/永久普通待办。 |
| SRC-ZAI | [Research p1](raw-zai.html)blogsItems15/hasMoretrue/next2；[p2](raw-zai-p2.html)18/hasMorefalse/next3；createAt非排序，最早Dec7，停止p3。[release](raw-zai-release.html)Dec22/11/10/8后Sep30，只补入口。 | November Research必要历史段受阻；两页实际检查不是全组织零研究。release不替Research，不扩GitHub。 |
| SRC-BYTEDANCE-SEED | [Research](raw-seed.html)，2025 [type2 Blog p0](raw-seed-type2-p0.json)/[type1 paper p0](raw-seed-type1-p0.json)，各18、total45/94、has_moretrue/next20；count20/order_desc/header US。逐项分离future pinned，非pinned最晚Oct22/Oct21 16Z，越窗前停止20。 | 仅两原API切片；未请求p20，不声称has_morefalse或全页读完。pinned不作时序停止边界，删除/迁移史不保证。 |
| SRC-BAIDU-ERNIE | [p1](raw-ernie.html)10项至Nov21；[p2](raw-ernie-p2.html)6项Nov11/7至June30，显示1/2、prev无next，停止p3。Nov21原UTC00字段=BJT08，在本窗前。 | 仅当前两页，无本窗留存公告。未把模型版本标签或首篇标题当完整技术报告关闭。 |
| SRC-XIAOMI-MIMO | [首页](raw-mimo.html)8 dated论文2026至Oct21/Sept19/June4/May12及15 undated Blog；本日fresh [native chunk](raw-mimo-native.js)成功25477 bytes / 25389字符，moreBlogs由h控制、按钮只本地toggle、p.map渲染已返回列表。 | 只有Blog必要日期历史段受阻；More不发分页、不恢复日期，无普通More待办。不扩读15篇无日期正文来猜公开时刻。 |
| SRC-MINIMAX | [英](raw-minimax.html)12/[中](raw-minimax-zh.html)13可见dated项，Dec23至Oct27，未观察到分页；Daily [Agent Tech原MD](raw-minimax-tech.md)与所供[llms索引](raw-minimax-index.txt)实际仅1项2026May13，止索引。 | Agent Tech2025历史段受阻，不能写未触发/不适用。两普通目录非删除史，不扫全部产品docs。 |
| SRC-ARXIV | [commit API](raw-arxiv-help-commits.json) `path=source/help/availability.md,until=2025-11-24T01:00:00Z,per_page=1`，最新Aug06 `95c71658adbaa987dc2ba1105ef9c5201ecde4ce`；[exact2025帮助](raw-arxiv-2025-help.md)亲读公告日、时间、ID分配、替换/撤回/cross-list与2025holiday。 | IANA本窗SatNov22 20EST至SunNov23 20EST，终点Sun公告排除，归25。无常规批次不是全网0；未创建submitted/整分类题摘队列。 |

八条有界Nov23辅助query真实输入已由Planck恢复本日原执行记录，见[独立notes八条辅助query段](FIRST_DAY_INDEPENDENT_REVIEW.md)：12:06:33Z Meta/Qwen/Google/DeepMind四条、12:09:13Z Hunyuan/Zai/MiMo/arXiv四条，两组各一次、无分页，返回empty。不是从empty反推输入、不证明某源历史0，不重复查询；原参数此前未存本包的历史过程不再作为不可恢复缺口。本表有限判断依上列真实原入口/切片。

## 2. 完整核心、版本与准入分层

当前作者同步（2026-10-04T21:22:58+08:00工具clock）：Planck FIRST/来源片段及21:10:55 Shopping必要Evidence与Ch31/66 OnlyReport实际差额已通过，21:13:21单项检查通过。README已落实一项确定候选、2+1+2=5、标准完成、仅报告与0 Books写入；采用范围仅厂商困难多约束内部相对质量声明，不授同预算替代。下列准入前记录保留为历史，当前普通工作仅作者变化/六部分DAY回核，不重新请求完整核心或owner。

[首批校准](FIRST_CALIBRATION_READY.md)有两实际完整官方核心。Shopping原How it works L101–104、反馈段L93–103及限制L105–110：专用mini RL后训练、研究中偏好/约束反馈更新、产品满足要求比例的内部评价。准入潜力只指这些实际披露，待非作者区分局部新验证与领域recipe，不因预算缺失或成熟组件组合直接关闭，也不以产品名字/声望直接入选。未评分、未冻结为确定候选，标准/深入Evidence未完成。

数学Blog原完整核心只是Ryu单例探索/人工判断与完成证明，提出本窗贡献关闭待分层校准；不将优化理论整体范围关闭。链接2510.23513v1只是旧身份定点恢复，[abs](raw-nag-v1-abs.html)摘要尾部截断，不冒充完整；[exact-v1 HTML](raw-nag-v1.html)实际完整题摘读至elicited，必要开头L-smooth/convex条件已见，未核全部证明。ID月规则只能支持October first announcement，不以Oct27 submitted精确赋公开时刻。当前v2 Jan19 2026不替v1，不声称旧日报已审；Blog非新理论修订证据，不强造本窗理论队列。

实际可见两个官方核心/版本身份中没有发现必须改变本处置的新撤回、勘误或安全纠错；没有遍历全历史。网页价格/库存限制与百分比评价人口必须保留，不授真实购买成功或隐私/安全保证。

## 3. 当前普通工作与隔离边界

来源切片、准入及单项必要Evidence/OnlyReport已独立处理，当前普通工作只为Planck对本次作者同步变化及六部分的最终DAY回核。本作者不得自审。共享Books由root独占，实际差额0没有写入，无月索引/state改动。

Google pubs/DeepMind、Meta、Qwen、Hunyuan、Zai Research、MiMo Blog、MiniMax Agent Tech必要本窗历史段已按可用入口有限尝试。接受本窗官方历史目录、具名原稿/精确公开范围或重要修订原源到达，只重开来源/身份；当前不作为正面Coverage/Evidence、Books或无遗漏保证。不把已失败浏览器/无可接受历史入口的项变永久普通待办；发现新真实可执行入口时不能仍叫外部保留。

没有本日具名会议新批次、评测suite或重要release/RFC触发；Daily不扫每周组，也不为证明没触发遍历按需全站。表外仅恢复数学Blog直接链接的旧精确身份。未跑artifact/模型/benchmark，未做理论全证明验算或生产隐私/安全审计。
