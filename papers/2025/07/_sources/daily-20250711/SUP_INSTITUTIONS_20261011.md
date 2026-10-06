# July11 机构 Daily 来源有限补查

检查日：2026-10-11
报告归属：2025-07-11
本轮新材料窗口：2025-07-10 完整 BJT 自然日
范围：Daily 组 13 个机构来源，不含 arXiv 发现扫描
性质：机构来源补查作者交包；不是独立复核签名或 DAY 验收

## 1. Ownership、冻结与复用

- 本 agent 只写本文件及同目录 `SUP_I11_*` 网络原件。root 负责 arXiv、日报、State、Books，并复核机构来源与具名贡献判断；Ptolemy 是非报告作者最终 DAY 复核者。人类不承担独立复核。
- 启动已重读当前 AGENTS、Research 合同、Report 合同、Sources 使用说明与 Daily 组、Prompt、ROADMAP、本日 README 及本日旧 BOUNDARIES / RECOVERIES / SUPPLEMENT、相关机构原件。最新 checkpoint 仅作 July11 路由；不加载其他日期研究包。
- 原报告窗口 `2025-07-10T09:00:00+08:00 ～ 2025-07-11T09:00:00+08:00`、原正式候选 0、原 65 项保留身份及日期、连续 §4 均冻结。本文件不改这些原值，不重做既存有效机制审阅。新材料按 7 月 10 日自然日归属，不传播原小时级缺口。
- 本轮重新请求机构入口及必要有限页段；旧同日原件只用于明确标出的复用。当前在线目录不是 2025 年网页快照；页面日期、版本提交日、当前抓取时间和首次公开日不得混用。
- 源切片中的后续年份元数据仅为判断目录是否到达历史窗口，没有阅读这些材料的题摘、方法或扩展其他日期队列。没有 Weekly / 全年 catchup、Git 写入或共享文件写入。

## 2. 13 来源的实际切片与停止点

下表“未发现目标项”只限实际切片，不表示全站零事件或无遗漏。Google Research 与 DeepMind 合并为一个注册 ID。

| ID | 本轮实际入口 / 原件 | 页段、结果与停止 | 限制 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 网页工具读取；[RSS raw](./SUP_I11_openai-rss.raw) | RSS 解析 1287 个 item，仅筛 BJT 7/10 日期；相邻记录为 7/11 EU 公告与 7/8 教师合作，无 7/10 item；停止该 feed，不逐篇审阅窗外新闻 | 当前 Research / RSS 切片不保证研究全历史或重要修订完整 |
| SRC-ANTHROPIC | [Research raw](./SUP_I11_anthropic.raw) | 解码页面内序列化数据，177 次 publishedOn 出现、168 个唯一时间戳；2025/7 仅 7/15，无 7/10；不继续论文历史队列 | 此为时间戳粒度，不等于 177 篇论文；旧 174 条记录 / 172 slug 的分母不同，不据此宣布旧计数错误或全站覆盖 |
| SRC-GOOGLE-AI | [Research July2025](https://research.google/blog/2025/07/)、[GFM](https://research.google/blog/graph-foundation-models-for-relational-data/)、[Google publications](https://research.google/pubs/)；[DeepMind Research](https://deepmind.google/research/)、[publications raw](./SUP_I11_deepmind-pubs1.raw)、[真正 page/2](https://deepmind.google/research/publications/page/2/)、[blog page/6](https://deepmind.google/blog/page/6/) | 网页工具取得 Research 月页 9 条及 GFM 7/10 原文。Google publications 仅当前初始表单 / 1–15 of 11612，没有恢复目标日筛选。DeepMind publications 按真实路径到 page/2，目录从 7/13 三条跨到 7/1、6/26，无 7/10 目录项；在此停止，不遍历 265 项选择列表。blog page/6 的 July 五条复用同日已有效定点日期记录，不重复机制审阅；GFM 见 §3 | 月博客不是全部论文；DeepMind 目录日期不是论文 first-public 证明。Google / DeepMind 若干本地请求超时，但网页工具有可读正文，见 §5。未使用错误的 query page2 冒充翻页 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)；[本轮 headers](./SUP_I11_meta.headers) | 本地请求约 12 秒超时，网页工具返回 0 行；作一次目标日官方域名搜索后停止 | 无历史正文，搜索未建立目标事件，不能写为 0 命中、Coverage 通过；本轮是 timeout，不冒称旧 reset 错误复现 |
| SRC-QWEN | [首页 raw](./SUP_I11_qwen.raw)、[真实 page/2 raw](./SUP_I11_qwen-page2.raw)、[官方 research-list API raw](./SUP_I11_qwen-research.raw) | 首页 Next 到 page/2，7/22 → 6/27 → 6/26 跨过目标日；API 实际 60 条本地数组，BJT 7/10 项 0，2025/7 为 7/27、7/24、7/22；停止两页 + 一个数组，不沿全年历史 | 仅当前站点迁移目录和当前 research-list，不保证官方全部历史/修订 |
| SRC-DEEPSEEK | [主页 raw](./SUP_I11_deepseek.raw)、[官方 updates raw](./SUP_I11_deepseek-updates.raw) | 发布说明目标邻接段 8/21 → 5/28，没有 7/10 日期条；停止 changelog 目标邻接段 | 主页与产品发布说明不等于完整 Research 历史 |
| SRC-MOONSHOT | [Kimi Blog raw](./SUP_I11_kimi.raw) | 实际页面 26 个 time 元素，邻接 7/17 → Kimi K2 7/11 → 5/6；K2 在新窗外，不读正文、不找小时 | 只对该列表归属判断；不改原候选/§4，也不凭当前目录保证所有旧论文 |
| SRC-TENCENT-HUNYUAN | [Research 壳 raw](./SUP_I11_hunyuan.raw)、[All API raw](./SUP_I11_hunyuan-all.raw) | 浏览器可列出 IAB，但打开 Research 调用 71.0844 秒后执行超时、内核重置，未取得 DOM/截图。POST publicList，pageNum=1/pageSize=20/renderType=0，实际 totalNum=9/list=9，displayPublishTime 按 BJT 均 2026/2/3～9/22；停止 All 当前返回，不逐条读研究 | “全部”只表示此 API 当前 All 模式，不证明 2025 历史完备。2025 目录未恢复，诚实隔离；不写目标窗零事件 |
| SRC-ZAI | [Research raw](./SUP_I11_zai.raw)、[page2 raw](./SUP_I11_zai-page2.raw) | 首页可见 15 卡片到 2025/12/9；?page=2 实际 SSR 18 卡片、包含前页重复，仅延伸到 12/7并显示没有更多；到该停止点为止。目标日官方域搜索未建立目标事件 | 没有到达 7/10；“没有更多”不能解释成历史完整或目标日 0。搜索出现旧 2024 news 队列，未展开 |
| SRC-BYTEDANCE-SEED | [Research raw](./SUP_I11_seed.raw)、[当前 JS raw](./SUP_I11_seed-main.raw)、四个 2025 API 数组（§4）、[CoT 原文](./SUP_I11_seed-cot.raw) | 当前 public_papers 初始 20/242 不是历史补查；改用 publish_year=2025、type1/2、tokens0/20、count20、order_desc=true 与 x-tt-locale: US。实际 papers 38 / blogs 36；论文切片内唯一 7/10 具名项为 CoT，博客切片无 7/10；停止 token20，不请求 token40 | 两类均 has_more=true，38/36 不是 94/45 全池。纠正旧稀疏 payload，不宣称新目录全站完备。CoT 是旧家族事件，见 §3 |
| SRC-BAIDU-ERNIE | [首页 raw](./SUP_I11_ernie.raw)、[真实 page/2 raw](./SUP_I11_ernie-page2.raw) | Next 到 /blog/zh/page/2/，第二页 6 条，目标邻接 8/14 FastDeploy → 6/30 ERNIE4.5；第二页末为上一页 1/2，没有进一步页；停止两页 | 列表没有 7/10 项，不等于历史网页无删除或所有官方论文 |
| SRC-XIAOMI-MIMO | [首页 raw](./SUP_I11_mimo.raw)、[main](./SUP_I11_mimo-main.raw)、[8557](./SUP_I11_mimo-8557.raw)、[6159](./SUP_I11_mimo-6159.raw) | Paper 是 l.G.slice().reverse() 的本地 8 项：4 条 2025、4 条 2026，目标邻接 9/19 → 6/4，无 7/10。Blog 实际本地 15 项，initialVisibleCount=8；More 只是 slice(0,c) / slice(c) 的本地显隐，不是另一个历史请求；在此停止 | Blog 列表没有统一日期，不能错误写“15 篇全是 2026”，也不能从按钮推出历史全量或目标日零事件 |
| SRC-MINIMAX | [英文 Blog raw](./SUP_I11_minimax-en.raw)、[中文 Blog raw](./SUP_I11_minimax-cn.raw)、[目标日官方 News raw](./SUP_I11_minimax-news.raw) | 英文可见 12 条到 2025/10/27；中文 13 条包含 2025/1/15，目标邻接仍不提供 7/10 技术条。一次官方域目标日搜索找到 7/10 教育 News，完整核心已读，判 C；在此停止 | 当前 Blog 不是全部历史；*.space.minimax.io 用户托管 newsletter 排除，不当官方研究。具名 C 不把其他外部缺口归零 |

## 3. 具名材料与准入判断

### 3.1 GFM：恢复 7/10 官方日期，窄 P，交 root 读证据

- 主身份：[Graph foundation models for relational data](https://research.google/blog/graph-foundation-models-for-relational-data/)，作者 Michael Galkin / Pramod Doguparty，官方页面明示 July 10, 2025。本轮网页工具实际读到日期与核心，日级已足够归新补充窗；不再要求精确小时。
- 本轮 curl 该页超时，没有新 raw。可复用同日原 [google-gfm.raw](./google-gfm.raw) / [google-gfm.txt](./google-gfm.txt)：本轮已定点核旧原件包含标题、July10 日期及核心，未改原件。网页工具读取不是浏览器 DOM 自证，也不是 2025 时点快照。
- 完整核心：单表模型丢失跨表连通，传统 GNN 又绑定训练图的节点/边类型与特征空间。官方提出表类型→节点类型、行→节点、外键→边、其他列→特征，并要求编码器跨数据库 schema/特征空间迁移；硬编码类型表或特定特征投影不能直接复用，作者主张学习不同任务中属性之间的交互可改善迁移。目标是同一模型在未见图上推理，不仅是把成熟 GNN 拼进某个应用。
- 准入句：多表关系预测受 schema 变化和模型重训约束 → 图化关系及可迁移编码改变跨 schema 模型复用选择 → 有具体机制增量线索，保留窄 P，日期门恢复。它是旧已知线索的日期恢复，不是新发现一篇论文。
- 官方内部分类结果、基线公平性、平均精度增益与 zero/few-shot 外推仍由 root 读必要证据。这里不授 Evidence 完成、不评分、不宣布 Books 已覆盖，也不改旧 §4。若原文不足以支撑一般迁移或实现细节，应精确限制采用命题，不以日期/费用降分关闭。

### 3.2 Seed CoT：7/10 目录事件，不冒充新论文或重要修订

- 主身份：[Understanding Chain-of-Thought in LLMs through Information Theory](https://seed.bytedance.com/en/public_papers/understanding-chain-of-thought-in-llms-through-information-theory)，Jean-Francois Ton / Muhammad Faaiz Taufiq / Yang Liu，目录日期 2025-07-10、ICML2025。
- 实际完整题摘：CoT 标注昂贵、只看最终答案会漏掉中间步骤错误；框架用每一步信息增益评估推理轨迹、定位 failure mode，尽量避免额外 CoT 标注；作者报告 toy arithmetic / GSM8K / PRM800k 结果。机制可影响“结果正确是否代表过程有效”的评估选择，不能仅因为是评估论文降成 C。
- 但下载链接指向 [2411.11984](https://arxiv.org/abs/2411.11984)，本轮只定点核该身份，没有 arXiv 发现扫描。[本轮身份 raw](./SUP_I11_seed-cot-identity.raw) 显示 v1 submitted 2024-11-18，v2 revised 2025-07-10。提交/修订历史不是首公开证据；家族显然不是 2025/7 新论文。
- 准入句：7/10 官网页/ICML 事件承载旧 CoT 信息论评估机制 → 未识别改变方法、兼容性、正确性或安全结论的官方重要修订说明 → 本窗不新增 P、不重复计分。未做全篇版本 diff，不声称 v1/v2 全文相同；也不把普通 v2 标签自动认定为重要修订。
- 沿用本日旧有效家族/事件隔离判断。重开须具体重要修订命题及相应官方原文，不要求小时，不要求无差别通读全部版本。

### 3.3 MiniMax：新增具名 C，核心已核

- 主身份：[Empowering the Next Generation: MiniMax Supports AI Education for Underprivileged Youth in Hong Kong](https://www.minimax.io/news/ai-education-for-underprivileged-youth-in-hk)，官方页面日期 July 10, 2025；[本轮原件](./SUP_I11_minimax-news.raw)。
- 完整核心：MiniMax 为香港青年 mentorship 的 GenAI workshop 提供服务合作，给予学生/教育者两个月免费不限量 Hailuo Video 访问；介绍 7/5 首场视频创作活动及后续两场计划。7/5 是活动发生日，不替代 7/10 公告日。
- 准入句：教育使用和访问成本约束 → 提供现成视频工具与使用机会 → 没有新增模型、训练、架构、推理或评估机制，属范围/贡献 C。不是因为日期未知、费用、低分或 Books 已有覆盖而排除。
- 不把访问优惠或参与活动当作模型技术证据，不投入全文论文审阅。

### 3.4 Kimi K2：窗外，不延续旧小时待办

本轮 Kimi 列表官方日期 2025-07-11，链接 /blog/posts/k2-report。对新 7/10 自然日不适用，因此无需恢复时刻或读核心；保留原报告记录不动，不在本窗新增 P/C 贡献排除。

## 4. Seed 实际分页与 locale 校正

当前 JS 明示 get_article_list_v2 参数映射，以及论文 article_type=1 请求的 `x-tt-locale: US` 覆盖。四次本轮请求均显式发送该 header；不把旧空数组当作正常终点。

| 类型 / token | actual array | total | next_page_token | has_more | 实际 BJT 日期切片 | 原件 |
| --- | --- | --- | --- | --- | --- | --- |
| paper type1 / 0 | 18 | 94 | 20 | true | 2025-12-15 → 2025-06-26 | [raw](./SUP_I11_seed-type1-p0.raw) |
| paper type1 / 20 | 20 | 94 | 40 | true | 2025-06-20 → 2025-05-20 | [raw](./SUP_I11_seed-type1-p20.raw) |
| blog type2 / 0 | 18 | 45 | 20 | true | 2025-12-24 → 2025-06-25 | [raw](./SUP_I11_seed-type2-p0.raw) |
| blog type2 / 20 | 18 | 45 | 40 | true | 2025-06-18 → 2025-02-12 | [raw](./SUP_I11_seed-type2-p20.raw) |

paper ID 去重 38 / blog ID 去重 36；count=20 是请求上限，不是实际条数。paper token0 中 ID276 是 7/10 CoT；blog 这两页没有 7/10。切片已跨过目标日，停止 token20，尚有更多页但不作为本批全年队列。该有限范围不能保证没有列表过滤/遗漏/后续重要版本，也不能授全站正面 Coverage。

## 5. 本轮获取记录与网页观察权限

### 5.1 获取方式

35 次本地网络请求，30 次 HTTP200 获得 raw，5 次 curl exit28 / HTTP000 / bytes0。下表时间为 **2026-10-11 UTC 请求起始时间**，仅记录抓取，不用来推导历史发布时间。GET 除 Hunyuan 为 POST：

`https://api.hunyuan.tencent.com/api/blog/publicList`
body：`{"pageNum":1,"pageSize":20,"renderType":0}`

Seed 四个 API 的统一查询：`publish_year=2025&count=20&order_desc=true`，article_type 和 page_token 如 §4，header `x-tt-locale: US`。
Qwen API：`https://qwen.ai/api/page_config?code=research.research-list`。
其他请求 URL 为 §2 链接及网页原件中的当前静态资源引用；MiniMax 中文入口从 minimaxi.com 跳转 minimax.cn。静态 JS 只解析当前目录/分页行为，不执行或扩大研究范围。

| 请求名 | 开始 UTC | HTTP / curl exit | bytes | 秒 | 请求 URL | 本地记录 |
| --- | --- | --- | --- | --- | --- | --- |
| openai-rss | 07:54:51 UTC | 200 / 0 | 784414 | 0.361 | https://openai.com/news/rss.xml | [headers](./SUP_I11_openai-rss.headers) / [raw](./SUP_I11_openai-rss.raw) |
| anthropic | 07:54:52 UTC | 200 / 0 | 282283 | 1.823 | https://www.anthropic.com/research | [headers](./SUP_I11_anthropic.headers) / [raw](./SUP_I11_anthropic.raw) |
| google-month | 07:54:54 UTC | 000 / 28 | 0 | 12.006 | https://research.google/blog/2025/07/ | [headers](./SUP_I11_google-month.headers)；未获得 raw |
| google-gfm | 07:55:06 UTC | 000 / 28 | 0 | 12.006 | https://research.google/blog/graph-foundation-models-for-relational-data/ | [headers](./SUP_I11_google-gfm.headers)；未获得 raw |
| deepmind | 07:55:18 UTC | 000 / 28 | 0 | 12.007 | https://deepmind.google/research/ | [headers](./SUP_I11_deepmind.headers)；未获得 raw |
| meta | 07:55:30 UTC | 000 / 28 | 0 | 12.005 | https://ai.meta.com/research/ | [headers](./SUP_I11_meta.headers)；未获得 raw |
| qwen | 07:55:42 UTC | 200 / 0 | 17307 | 0.738 | https://qwenlm.github.io/ | [headers](./SUP_I11_qwen.headers) / [raw](./SUP_I11_qwen.raw) |
| deepseek | 07:55:43 UTC | 200 / 0 | 115583 | 0.054 | https://www.deepseek.com/ | [headers](./SUP_I11_deepseek.headers) / [raw](./SUP_I11_deepseek.raw) |
| deepseek-updates | 07:55:43 UTC | 200 / 0 | 48079 | 0.121 | https://api-docs.deepseek.com/updates/ | [headers](./SUP_I11_deepseek-updates.headers) / [raw](./SUP_I11_deepseek-updates.raw) |
| kimi | 07:55:43 UTC | 200 / 0 | 13388 | 0.183 | https://platform.kimi.com/blog | [headers](./SUP_I11_kimi.headers) / [raw](./SUP_I11_kimi.raw) |
| hunyuan | 07:55:43 UTC | 200 / 0 | 6893 | 0.162 | https://hunyuan.tencent.com/research | [headers](./SUP_I11_hunyuan.headers) / [raw](./SUP_I11_hunyuan.raw) |
| zai | 07:55:43 UTC | 200 / 0 | 1276468 | 0.687 | https://www.zhipuai.cn/zh/research | [headers](./SUP_I11_zai.headers) / [raw](./SUP_I11_zai.raw) |
| seed | 07:55:44 UTC | 200 / 0 | 114243 | 0.328 | https://seed.bytedance.com/en/research | [headers](./SUP_I11_seed.headers) / [raw](./SUP_I11_seed.raw) |
| ernie | 07:55:45 UTC | 200 / 0 | 28100 | 0.288 | https://ernie.baidu.com/blog/zh/ | [headers](./SUP_I11_ernie.headers) / [raw](./SUP_I11_ernie.raw) |
| mimo | 07:55:45 UTC | 200 / 0 | 58220 | 0.173 | https://mimo.xiaomi.com/ | [headers](./SUP_I11_mimo.headers) / [raw](./SUP_I11_mimo.raw) |
| minimax-en | 07:55:45 UTC | 200 / 0 | 134698 | 1.788 | https://www.minimax.io/blog | [headers](./SUP_I11_minimax-en.headers) / [raw](./SUP_I11_minimax-en.raw) |
| minimax-cn | 07:55:47 UTC | 200 / 0 | 144114 | 0.966 | https://www.minimaxi.com/blog | [headers](./SUP_I11_minimax-cn.headers) / [raw](./SUP_I11_minimax-cn.raw) |
| qwen-page2 | 07:57:08 UTC | 200 / 0 | 17379 | 0.658 | https://qwenlm.github.io/page/2/ | [headers](./SUP_I11_qwen-page2.headers) / [raw](./SUP_I11_qwen-page2.raw) |
| ernie-page2 | 07:57:08 UTC | 200 / 0 | 20533 | 0.236 | https://ernie.baidu.com/blog/zh/page/2/ | [headers](./SUP_I11_ernie-page2.headers) / [raw](./SUP_I11_ernie-page2.raw) |
| zai-page2 | 07:57:09 UTC | 200 / 0 | 1397453 | 0.710 | https://www.zhipuai.cn/zh/research?page=2 | [headers](./SUP_I11_zai-page2.headers) / [raw](./SUP_I11_zai-page2.raw) |
| seed-main | 07:57:09 UTC | 200 / 0 | 1857907 | 0.138 | https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/deploy/flow/ai_official_website/88329/static/js/main.c981da25.js | [headers](./SUP_I11_seed-main.headers) / [raw](./SUP_I11_seed-main.raw) |
| seed-type1-p0 | 07:57:10 UTC | 200 / 0 | 49455 | 0.183 | https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=0&order_desc=true | [headers](./SUP_I11_seed-type1-p0.headers) / [raw](./SUP_I11_seed-type1-p0.raw) |
| seed-type1-p20 | 07:57:10 UTC | 200 / 0 | 53526 | 0.261 | https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=20&order_desc=true | [headers](./SUP_I11_seed-type1-p20.headers) / [raw](./SUP_I11_seed-type1-p20.raw) |
| seed-type2-p0 | 07:57:10 UTC | 200 / 0 | 41802 | 0.256 | https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=0&order_desc=true | [headers](./SUP_I11_seed-type2-p0.headers) / [raw](./SUP_I11_seed-type2-p0.raw) |
| seed-type2-p20 | 07:57:11 UTC | 200 / 0 | 38756 | 0.322 | https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=20&order_desc=true | [headers](./SUP_I11_seed-type2-p20.headers) / [raw](./SUP_I11_seed-type2-p20.raw) |
| seed-cot | 07:57:11 UTC | 200 / 0 | 102823 | 0.582 | https://seed.bytedance.com/en/public_papers/understanding-chain-of-thought-in-llms-through-information-theory | [headers](./SUP_I11_seed-cot.headers) / [raw](./SUP_I11_seed-cot.raw) |
| seed-cot-identity | 07:57:12 UTC | 200 / 0 | 40561 | 0.347 | https://arxiv.org/abs/2411.11984 | [headers](./SUP_I11_seed-cot-identity.headers) / [raw](./SUP_I11_seed-cot-identity.raw) |
| hunyuan-all | 08:00:23 UTC | 200 / 0 | 315236 | 0.397 | https://api.hunyuan.tencent.com/api/blog/publicList | [headers](./SUP_I11_hunyuan-all.headers) / [raw](./SUP_I11_hunyuan-all.raw) |
| qwen-research | 08:01:09 UTC | 200 / 0 | 57428 | 0.267 | https://qwen.ai/api/page_config?code=research.research-list | [headers](./SUP_I11_qwen-research.headers) / [raw](./SUP_I11_qwen-research.raw) |
| mimo-main | 08:01:09 UTC | 200 / 0 | 22556 | 0.052 | https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.c5195ace.js | [headers](./SUP_I11_mimo-main.headers) / [raw](./SUP_I11_mimo-main.raw) |
| mimo-8557 | 08:01:09 UTC | 200 / 0 | 7920 | 0.044 | https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js | [headers](./SUP_I11_mimo-8557.headers) / [raw](./SUP_I11_mimo-8557.raw) |
| mimo-6159 | 08:01:10 UTC | 200 / 0 | 25477 | 0.035 | https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js | [headers](./SUP_I11_mimo-6159.headers) / [raw](./SUP_I11_mimo-6159.raw) |
| minimax-news | 08:01:10 UTC | 200 / 0 | 78973 | 1.150 | https://www.minimax.io/news/ai-education-for-underprivileged-youth-in-hk | [headers](./SUP_I11_minimax-news.headers) / [raw](./SUP_I11_minimax-news.raw) |
| deepmind-pubs1 | 08:01:11 UTC | 200 / 0 | 142513 | 7.173 | https://deepmind.google/research/publications/ | [headers](./SUP_I11_deepmind-pubs1.headers) / [raw](./SUP_I11_deepmind-pubs1.raw) |
| deepmind-pubs2 | 08:01:18 UTC | 000 / 28 | 0 | 12.003 | https://deepmind.google/research/publications/page/2/ | [headers](./SUP_I11_deepmind-pubs2.headers)；未获得 raw |

### 5.2 网页工具观测与本地原件分开

本轮网页读取工具（非浏览器自动化）实际读取了 OpenAI Research、Anthropic Research、Google July2025 / GFM / publications、DeepMind Research / publications / publications/page/2 / blog/page/6、Seed public_papers / CoT、MiniMax 具名 News。Google / DeepMind 上述本地 timeout 不代表网页读取也失败；反之，不把工具返回正文虚报为新本地 raw 或浏览器成功。Meta 页面返回 0 行。工具的当前/缓存页面不代表目标日快照，未提供 HTTP 状态的网页结果不伪造状态。

四个有限官方域搜索同时提交：

- `site:ai.meta.com/research "July 10, 2025"`
- `site:minimax.io "July 10" "2025"`
- `site:hunyuan.tencent.com "2025-07-10"`
- `site:zhipuai.cn "2025" "7月10日"`

MiniMax 仅把官方 News 当具名原始来源，用户托管 newsletter 排除；ZAI 搜索旧 2024 新闻不展开。没有由索引建立其他目标日具名研究，不能据此宣布任何机构无遗漏。

DeepMind blog/page/6 只有月级五条 July 标记；日期判断复用本日旧 [SUPPLEMENT](./SUPPLEMENT.md) 及 dm-flashlite / dm-backstory / dm-imo / dm-t5gemma / dm-medgemma 既有定点原件，未重复旧有效机制审阅。T5Gemma 原页 7/9，仍在新窗外。仅 GFM 的原日级日期恢复需要 root 继续必要证据审阅，不制造旧月目录的全新外部未读队列。

## 6. 交付边界与下一步

- 本批 13 个机构已完成实际有界首查/必要有限补查并保留停止点。新增发现的本窗 P 为 0；另有 **旧 GFM 的 7/10 日期恢复窄 P 1 条**，及 **新具名 MiniMax C 1 条**。Seed 7/10 CoT 为旧家族事件，未确立重要修订；K2 7/11 窗外。
- root 的具体普通事项是核本包来源/metadata、读 GFM 必要证据并在报告表达采用范围。尚有可执行工作，不把本日虚构为受阻终态；本 agent 不负责完成日报六节或授 DAY。
- Meta 历史正文、Hunyuan 2025 目录、ZAI 目标日前目录及各当前目录的全历史完整性仍有限制；Seed 只检查 38/36 数组、MiMo 15 个无统一日期博客也不声称全站完备。这些缺口不得写为零命中、正面 Coverage、Evidence 或 Books 完整覆盖。
- 机构包是后续 root / Ptolemy 验收输入，不是“全 2025 补查完成”。整体历史恢复由 root 继续推进。本轮不添加全年待扫队列、不重写旧连续 §4。

## 7. 本包本地检查

- 13 个来源 ID 唯一且不含 SRC-ARXIV；100 个本地 Markdown 引用均存在，表格列数一致。Seed 两类跨页实际去重仍为 38 / 36。
- 35 个 headers 与 30 个 raw 已核；raw 字节数逐项等于请求记录，5 个 timeout 没有虚构正文文件。
- 首轮本包检查发现 EOF 多一个空行，已修正；首轮辅助表格检查错误地未允许 4 列表格，修正检查后通过。最终本包 git diff --no-index --check 无警告，exit1 仅表示新增文件有 diff；限定同日 git diff --check exit0。
- 唯一手工写入为本文件；SUP_I11_* 是网络获取原件。README 的既有 / 并行修改及 SUP_A11_*、其他独核文件均未改动。未运行 root 尚在写的全日报 V3，不将本包格式/链接检查当作研究语义或 DAY 通过；未 stage / commit / push。
