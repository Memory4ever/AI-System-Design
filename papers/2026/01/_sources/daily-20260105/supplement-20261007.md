# 2026-01-05 Daily 增量来源补查

执行者：supp_jan05。检查时间：2026-10-07T13:34:10+08:00。

补充窗口：2026-01-04 ～ 2026-01-04（北京时间完整自然日）。用户授权只补遗漏；原 Report 的窗口、既有日期归属、评分与有效审阅不搬移、不重算。已重新完整读取 AGENTS、统一 Prompt、研究合同、Report 合同、来源清单使用说明与 Daily 组、ROADMAP、本日 README、queries-and-screening、原日期切片及 Kimi/arXiv 记录；最新路由读取 LEARNING_STATE 本轮增量 checkpoint。使用 Daily closure 检查方法，但当前合同及用户本轮边界优先。初始只写此记录，随后按root协调授权将实际结果融入本日README原六部分并保持本轮进行中；不写Books/LEARNING_STATE，不stage、commit或push。

## 结果与可并入 Report 的结论

14 个 Daily 来源完成本轮有限入口补查；没有确认的新增窗内候选，新增候选 0、新增候选证据审阅 0、新增 Books 改动 0。原 KimiCLI 0.71/0.72 两个 Jan04 release、同一家族的有效初筛继续复用，不再评分，也不计新增候选。新增窗口早于旧 09:00 起点的时段未发现另一 release：相邻 0.70 官方公开日期为 2025-12-31，而非 Jan04。No Change 只针对已可判断材料，不宣称互联网无遗漏。

Qwen/Hunyuan、智谱、MiniMax 中文及 Agent、MiMo Blog 目录已取得可核的有限当前数据，不再把无法证明历史隐藏、删除、所有镜像不存在作为覆盖缺口。仍有具体外部限制：Google Research 年级列表缺 Jan04 日级日期切片；Meta Research 原入口无法提取历史目录。独立复核由 root 完成，本记录不自验收。

## 来源切片、入口和停止点

原始目录可复用 root 同轮获取的 [Jan04 原始目录](../daily-20260104/supplement-20261007/)；这里只复用原始响应，下面的 Jan04 窗口判断均由本作者独立执行。原始文件必须随引用保留。原本 [official-date-slices](official-date-slices.jsonl)、[arxiv-and-kimi](arxiv-and-kimi.jsonl) 只作本日有效材料复用及身份依据，不把旧 09:00 窗口检查偷换成本轮完整自然日。

| 来源 | 本轮实际范围与停点 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | `https://openai.com/news/rss.xml` 原始响应 1251 item，只按 pubDate 换算 Jan04 BJT 日期；0 行，前邻 Grove Jan02、后邻 Health Jan07，止日期 metadata；不读全年正文 | 已检查 | 无；有限官网 RSS 范围，不授全网召回 |
| SRC-ANTHROPIC | `https://www.anthropic.com/research` 原始 HTML 174 publishedOn 字段；逐日期核 Jan04 无行，邻接 Dec19 Bloom 与 Jan08 critical-infrastructure-defense，止目录日期切片 | 已检查 | 无；有限 Research 目录 |
| SRC-GOOGLE-AI | 本轮重开 DeepMind Publications page1：30 dated 行、265 总条目、9 页；Jan09 TRecViT→Dec03 Capturing Human Preferences 桥接，止 page1。Google Research pubs 首屏只有 year（2026=392、2025=677），官方域 Jan04 主题日期搜索首组无恢复线索，止首组 | 受阻 | Google Research 的 Jan04 公开日期目录未取得；不能以年字段或空搜索判零研究 |
| SRC-META-AI | 本轮重开官方 Research 入口，文本 0 行；限定 `ai.meta.com` 的 Jan04 模型/LLM/research 日期检索首组无结果，止此 | 受阻 | 官方历史日期目录未提取；空正文不支持零发布 |
| SRC-QWEN | `https://qwen.ai/api/page_config?code=research.research-list` 60 条当前目录 metadata，逐 date 检查而非数组顺序；min=2022-11-14、max=2025-12-23T05:08:30Z，Jan04=0，止完整有限响应，不逐篇读窗外题摘 | 已检查 | 无；仅当前 60 条 Research API，未声称历年隐藏条目全覆盖 |
| SRC-DEEPSEEK | 本轮重开 `/news/` 研究索引 10 条，Jan12 Engram→Dec31 mHC 桥接；动态首屏 5 条，Jan04 无行，止首屏与索引 | 已检查 | 无；有限 dated 目录，不从 mHC 版本名猜时间 |
| SRC-MOONSHOT | Platform Blog 原始 26 dated 行，最新 Nov07 2025，Jan04=0；本轮 fresh exact-tag 官方 release API 0.70/0.71/0.72；两 Jan04 事件复用原已有效初筛，止三个明确版本，不扫普通 PR | 已检查 | 无；平台与已触发 KimiCLI 的有限范围，不授全机构 revision 覆盖 |
| SRC-TENCENT-HUNYUAN | 首查官方 Research 对应 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":1000,"renderType":0}`；code0/totalNum9/list9，各 publicAt/publishedAt/displayPublishTime 分开核，不按数组次序；最早 displayed/published Feb03，Jan04=0，止完整有限列表 | 已检查 | 无；无需证明已删除/隐藏材料不存在 |
| SRC-ZAI | 首查 `https://www.zhipuai.cn/zh/research` 当前全部/时间排序 15 dated 行，Jan13→Dec10/Dec09 桥接，无 Jan04，止首屏“查看更多”之前；解析时不把后台 created/updated 时间当公开日期 | 已检查 | 无；有限 Research 当前日期切片 |
| SRC-BYTEDANCE-SEED | Research/public_papers 原入口→本轮 fresh 官方 `get_article_list_v2`，article_type1/2，2026 ASC 与 2025 DESC，count20/page_token0，x-tt-locale:US；按 PublishDate 而非 pinned 顺序核边界，4 切片 Jan04=0，止首页日期桥接 | 已检查 | 无；分页细节见下，不称全机构召回 |
| SRC-BAIDU-ERNIE | 官方 Blog `/blog/zh/` page1 十条 dated，Jan08→Dec23 桥接，无 Jan04；next2/2 更旧，止 page1，不将排行榜版本编号作事件日期 | 已检查 | 无；有限 Blog 日期切片 |
| SRC-XIAOMI-MIMO | 本轮重开官网 Paper 8 dated 行，Jan08 MiMo-V2-Flash→Oct21 MoE Router 桥接；Blog 15 行/More→官网直接引用 JS 内16个 `/blog/` route metadata，再取这些官方页面及直接声明的 iframe，仅核日期与少数无日期项核心范围。Flash正文Dec16，HSS/Safety正文Dec22，V2-Pro/Omni/TTS正文Mar18，其余dated至少Apr以后，无Jan04，止当前目录/route切片 | 已检查 | 无；两个无日期项按具体贡献/范围关闭，见下，不把正文日期和frontmatter混同 |
| SRC-MINIMAX | English Blog 12 dated 行 Jan27→Dec23，中文原入口重定向 `/blog` 13 dated 行 Jan28→Dec23，均无 Jan04；本轮重开 Agent Tech Blog 唯一 dated 入口 May13 2026，止三目录，不读窗外全文 | 已检查 | 无；CN/Agent 目录本轮已能读取，不沿用旧提取故障 |
| SRC-ARXIV | 本轮重开 Availability L170–189 与原 holiday 全文 L17/21/29/32；Jan04 BJT 没有常规 scheduled announcement。四主题 API 仅作 submitted/version-update 发现，首页停止；无确认 Jan04 公开事件，不把 API published/updated 视首次公开日期 | 已检查 | 无常规批次目录待处理；范围不包括没有具体线索的所有作者先行镜像，未宣称非标准事件绝无发生 |

### Seed 四切片原字段

API：`https://seed.bytedance.com/api/get_article_list_v2?article_type=<1|2>&publish_year=<2026|2025>&count=20&page_token=0&order_desc=<false|true>`。

- type1/2026 ASC：19 返回行，total82，has_more=true，next_page_token20；最早 PublishDate1768838400000=Jan20 BJT。
- type1/2025 DESC：18 返回行，total94，has_more=true，next_page_token20；最近 PublishDate1765728000000=Dec15 BJT。
- type2/2026 ASC：14 返回行，total19，has_more=false，next_page_token空；最早 PublishDate1770825600000=Feb12 BJT。
- type2/2025 DESC：18 返回行，total45，has_more=true，next_page_token20；最近 PublishDate1766505600000=Dec24 BJT。

按真正日期比较，不把 pinned 老文章位置当终止理由。日期边界已跨过本窗，未扩大到全年题摘队列。

### MiMo 动态 Blog 的日期恢复

官网 HTML 实际引用的 JS：`https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js`。从公开 routePath/frontmatter 恢复16个 `/blog/` 路径，直接打开每页及其显式 `<iframe src>`；这不是猜测接口，也没有加载全部页面正文作贡献审阅。当前切片恢复如下：

- `/blog/mimo-v2-flash` 的 [官方 iframe](https://mimo.xiaomi.com/mimo-v2-flash/index.html) 显式 December16,2025；原提取仅看到壳，不应继续请求已恢复日期。
- `/blog/mimo-v2-flash-hss`、`/blog/mimo-v2-flash-safety` 正文均 December22,2025；frontmatter Dec19/Dec18 与可见正文不同，但两种口径都在本窗外，不构造Jan04修订事件。
- `/blog/mimo-v2-pro`、`/blog/mimo-v2-omni`、`/blog/mimo-v2-tts` 三个直接iframe均 March18th,2026。
- `/blog/mimo-v2-5`=April22nd,2026、`/blog/mimo-v2-5-pro`=April27th,2026；ASR/TTS页面只标April2026，整个范围明确窗外，无需追具体日。
- `/blog/mimo-v2-5-inference`=May30,2026；`/blog/mimo-tilert-1000tps`=June8,2026（正文另有June23日期）；`/blog/mimo-code-long-horizon`=June10,2026；`/blog/mimo-v2-6-tool-call-repetition`=September27,2026。
- `/blog/mimo-v2-6-material-research` 未读到日期，但完整标题明确是新材料研发/PFAS捕获的领域应用，按ROADMAP暂缓AI for Science关闭，不因日期含糊额外索取材料。
- `/blog/blog1` 指向官方 `htmls/mimo_v2_flash_model_description.html`，核心为MiMo-V2-Flash示例回答及TuringTest内容展示，无新的训练/推理/评价机制或足以改变设计的证据；非仅主题映射准入。日期未核实，具体贡献已可排除后停止，不评分、不建日期请求。

这里恢复的是当前官方页面/route切片，未声称所有历史镜像或隐藏条目覆盖。全部公开日期只是窗口排除依据，未把这些窗外正文变为本日审阅队列。

### arXiv 发现查询与为何停止

统一发现条件：`lastUpdatedDate:[202601031600 TO 202601041559] AND (<theme>)`；start0/max_results20/sortBylastUpdatedDate/ascending，URL 为 `https://export.arxiv.org/api/query` 加上述参数。实际四主题保持项目切片，不逐分类扩池：

- model：`(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:MoE OR all:"foundation model")`，total43，首页20。
- system：`(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:kernel OR all:"model inference" OR all:"distributed training")`，total4，首页4。
- multimodal：`(cat:cs.CV OR cat:cs.RO OR cat:cs.LG) AND (all:"foundation model" OR all:"world model" OR all:VLA OR all:multimodal OR all:"diffusion model")`，total16，首页16。
- agent：`(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:LLM OR all:"language model") AND (all:agent OR all:RAG OR all:memory OR all:reasoning OR all:planning)`，total28，首页20。

这些数字只是当前索引的 submitted/version-update 发现命中，不是 Jan04 新论文数、不相加、不计候选。响应含 2601.01310v2（published Jan04T00:13Z、updated Jan06T04:01Z）和 2601.01500v2（published Jan04T12:03Z、updated Feb18），说明过滤命中与当前返回版本的 updated 字段不一定同窗；更不能把这些 metadata 字段升格为实际首次公开。已读 system 全部四题摘及 multimodal 返回题摘的本轮可见部分，只作线索理解，没有以摘要代替证据审阅，也未据摘要重算评分。

[Availability](https://info.arxiv.org/help/availability.html) 明确新提交、replacement、withdrawal notice、cross-list 都随公告流程；周五/六 ET 不公告，下一常规批次在 Jan05 BJT。原 [假期公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/) Jan04 ET 延迟批次同样属于 Jan05 BJT；本轮实时重开该 Blog 遇429，复用本日 [source-date-boundary](source-date-boundary.txt) 已保存完整官方正文，身份/日期/采用命题没有变化。只据此说明本日无常规 scheduled 批次，不推导所有作者网站无先行公开。止 API 首页、不追43/28的窗外提交队列，不请求精确时分秒。

## 重复事件与贡献校准材料

本轮 fresh GitHub Release API 日期：

- [0.70](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.70)：published_at=2025-12-31T13:50:27Z，窗外。这里只核相邻版本身份/日期，不为本日审其窗外增量。
- [0.71](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.71)：published_at=2026-01-04T05:08:41Z，本窗；完整 release body 与原 [exact-tag changelog 核心](arxiv-and-kimi.jsonl) 相符，ACP client file/shell同步、model切换、skill按需、info与Toad功能。原贡献前关闭有效复用；功能集成本身未提供新的可靠性保证、失效边界或对既有长期设计的验证反证，未见相关安全/撤回/纠错说明，不改成候选，也不重审所有PR。
- [0.72](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.72)：published_at=2026-01-04T06:01:07Z，本窗；release完整核心为 Python3.14 installation issue 的兼容性修复，与原材料相同；没有新增长期机制命题，不因fix标签机械深审。

两窗内事件同一已处理家族。原有效评分/审阅保持不变（两项本来不准入、不评分）；无新增需比较 Books 的单篇，未提出共享 owner 写入。

## 具体外部保留项与恢复条件

1. Google Research：取得 Jan04 官方 dated 论文/报告目录切片或已定位材料的原始发布日期，才可确认本窗论文事件。当前年目录和首组空日期检索不支持零事件，重开 `https://research.google/pubs/` 的日级入口，不扩全年。
2. Meta：取得 `https://ai.meta.com/research/` 可读取的同窗 dated 目录/官方历史列表，恢复源日期切片。当前入口0行不能作零命中证据；不要求证明被删除/隐藏材料不存在。

以上隔离项不作候选、Books正面证据或“无遗漏”保证，不要求所有先行镜像。尚可执行：root 独立复核与写入原 Report 的六部分；本作者没有遗留筛选/审阅/Books普通待办。

## root 独立复核建议范围

全部新增拟入选项为空。负侧重点：原 Kimi0.71/0.72 日期/内容有效复用与 0.70 窗外；Qwen API60条没有Jan04且不能按数组排序；Hunyuan9条全部日期字段；Seed四切片日期与分页；Z.ai15行Jan13→Dec10；MiniMaxCN13条及Agent唯一May13；MiMo正文日期与frontmatter差异均窗外、两个无日期项的具体贡献/范围关闭理由；arXiv“发现字段不等公开”与首页停止理由。抽检其余无命中目录桥接，确认只验收约定有限范围，不把 Google/Meta 保留项改为无缺口。

本轮机器检查：本日V3字段/一致性校验通过；README和本记录各14个源ID、本地引用存在、无行尾空白；限定路径git diff --check通过。不替代root独立语义验收。
