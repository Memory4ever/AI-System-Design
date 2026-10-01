# 2026-09-27 机构 A：有界发现核查

- 本日窗口：`[2026-09-26T09:00:00+08:00, 2026-09-27T09:00:00+08:00)`。
- 检查时间：2026-09-27 09:35（Asia/Shanghai）。
- 范围：七个 Daily 机构来源；仅发现、日期与贡献准入核查，不是整日日报 Gate，也不是 Books Integration。
- 执行依据：本轮实际完整读取 AGENTS、统一 Prompt、研究与 Report 合同、来源 Daily 组及 arXiv 路由、ROADMAP。历史扩池已暂停；没有沿用旧日报完成标签。
- 结果：在下述实际可读列表中，没有确认本窗的新贡献候选。Meta 目录不可访问、Google Research Publications 缺日级信息等限制仍存在，不能把这一结果解释成所有机构在互联网上均无新论文。

## 1. 实际来源与停止范围

| Source ID | 实际入口与读取范围 | 本窗结果与边界 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)、其 [Research Index](https://openai.com/research/index/)、[News RSS](https://openai.com/news/rss.xml)。Index 当前首组从 09/23 MentalHealthBench、09/22 GPT-6 Sol/Luna向更早日期排列。RSS 网页 XML 解析失败后，实际读取官方 XML；文件含 1,230 items，仅检查最新八条的日期/身份，不是读了 1,230 篇。 | 可读研究索引及 RSS 最新事件均在窗口之前。RSS 最新 `pubDate=Fri, 25 Sep 2026 19:00:00 GMT`，对应北京时间 09/26 03:00 的 Proaction，归缺失的 09/26，不归 09/27。结论仅限定这两个公开列表，不把 Research 落地页当全站完备性证明。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 可读；实际抽取其原始 `publishedOn` 与 slug，168 个不同日期/身份组合。只检查窗口邻域 metadata；最近两条为 Nine Loops `2026-09-25T16:58:00.000Z`、Project Swap `2026-09-24T18:37:00.000Z`，未读历年全文。 | 公开研究列表本窗无已确认条目。Nine Loops 为北京时间 09/26 00:58，单独归缺日恢复；Project Swap 为 09/25 02:37，早于两个窗口。没有用 lastmod 代替公开日期。 |
| SRC-GOOGLE-AI | [DeepMind Blog](https://deepmind.google/blog/) 本页九个 September 卡片逐个打开日期，再到 August 停止；[DeepMind Publications](https://deepmind.google/research/publications/) 首列表最新为 09/01；[Google Research Blog](https://research.google/blog/) 可见最新 09/24 长视频文章；[Google Research Publications](https://research.google/pubs/) 当前只给 Year/Title 排序，第一页 15/11,553 条。 | DeepMind 九卡均为 09/24 或更早，不因非时间排序只看首卡：Flash 09/02、Live Avatar 09/24、Private AI Compute 09/23、TTS 09/23、Live Extended Thinking 09/15、AlphaGenome 09/08、WeatherNext 09/03、Fairwind 09/02、Agentic Video 09/01。只读日期，不采用窗外正文。本窗未确认新条目；Google Research Blog 完整列表/RSS回溯及 Publications 日级公开时刻未恢复，见 §3。日期只有 calendar day 时不虚构时区精度。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)、[Blog](https://ai.meta.com/blog/)、[Publications](https://ai.meta.com/research/publications/) 有界尝试。Research 网页返回空有效内容，其余网页失败；只读 HTTP fallback 实际 `Connection reset by peer`、HTTP 000、0 bytes。 | 访问隔离；未知有无窗口事件，绝不记零。没有扩扫历年或用第三方转载替代官方目录。 |
| SRC-QWEN | [Research](https://qwen.ai/research) 动态页无可读列表后，恢复官网研究页所用 [静态接口](https://qwen.ai/api/page_config?code=research.research-list)（60 条）与 [动态接口](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)（`data.articles` 40 条）。仅提取 title/path/date，不把接口正文数量当已全文审阅。 | 动态最新 `extra.date=2026-09-20T20:00:00+08:00`，Qwen-Image-2.1；邻近为 09/18 Live Translate/Omni Flash、09/03 E-CommerceBench/QwenDrive。静态项全部更早。因此官网合并的 60+40 公开研究列表在两窗均未见新项；不能代替作者 arXiv 的独立覆盖。 |
| SRC-DEEPSEEK | [首页](https://www.deepseek.com/)、其 [News](https://www.deepseek.com/news/)、[V4.1 Flash 官方公告](https://www.deepseek.com/news/deepseek-v4-1-flash/)。News 当前最新 09/10→04/24，研究索引当前可见十项最新 06/24→02/25。另尝试 [API Docs News](https://api-docs.deepseek.com/news)，失败/超时。 | 可见 News/研究索引没有本窗条目；范围限定当前公开列表。研究索引“查看全部”未获得可验证分页，不声称已穷尽全部论文；首页无日期横幅经公告核为 09/10，不能归本窗。 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog) 可见 26 条，最新 2025-11-07；[官方组织](https://github.com/MoonshotAI) 当前 43 repos 的前十 updated 条目。官方 API [按 created 降序前十仓库](https://api.github.com/orgs/MoonshotAI/repos?type=public&sort=created&direction=desc&per_page=10) 最新创建为 07/27 Kimi-K3；针对唯一窗口 push 信号 kimi-code 读取 [最近五个 Releases](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=5)。 | kimi-code `pushed_at=2026-09-26T03:38:19Z` 是仓库活动，不是新研究/release。最新 release 2.1.1 `published_at=2026-09-24T07:24:08Z`，早于两窗；default-branch commits 的本窗查询返回 `[]`，不推断所有分支无活动。平台博客陈旧、没有全组织每仓 release 穷举，限定实际检查范围；当前未形成可确认的重要事件候选。 |

## 2. 09/27 准入结果

没有确认本窗内且满足项目贡献门槛的新 Source Family；没有评分行，没有 Books 提案。这个结论来自上表实际入口/停点，并不以机构名、AI 关键词或目录数量制造候选。目录不可访问或只有不够精确的日期者进入限制，不当作已排除的论文。

## 3. 精确覆盖限制

1. **META-DIRECTORY-ACCESS**：三个官方入口没有返回可检索、可定窗列表；恢复材料是同一窗口的官方研究/博客/publication 清单或对应正式原文，不能用第三方“没有新闻”补零。
2. **GOOGLE-RESEARCH-DAY-DATE**：Publications 只给年份，无法从第一页年度条目确定两窗归属；未批量阅读全年。Research Blog 可见最新日期为 09/24，但完整 RSS 网页解析失败，直接读取 RSS 及 blog HTML 时间字段均超时。已读 DeepMind 九卡不能替代 Google Research 全目录。
3. **GOOGLE-CALENDAR-PRECISION**：DeepMind 卡片原文给日历日而非精确公开时间；九项均不提供已确认的 09/27 事件。对缺日 09/26，只能说没有确认条目，不对 Sep24 条目凭未披露时区造精确首发。需要时定点恢复该条官方时间字段，不扫年度论文。
4. **DEEPSEEK-INDEX-SCOPE**：News 与当前十项研究索引可读，但“查看全部”分页与 API Docs News 未恢复；可见目录停点有效，不等于完整组织论文清单。其作者 arXiv 由另一路独立发现去重。
5. **MOONSHOT-PLATFORM-SCOPE**：Platform Blog 当前停在 2025；组织新仓及 kimi-code release 有界核查有效，不冒充所有仓库每个 PR/branch/release 检索。本窗 push 仅活动信号，没有确认重要公告；无需把普通 commit 扩成全文队列。

以上是本子任务精确终态限制；并非整日日报 Complete 或整日受阻判定。

## 4. 复用停点补查缺失的 09/26（与本日分开）

缺日窗口：`[2026-09-25T09:00:00+08:00, 2026-09-26T09:00:00+08:00)`。仅复用上述目录日期邻域并定点打开两篇原文，没有重新扫描历史机构列表。

| Source Family / 原文 | 日期证据与归属 | 原文内容与准入关闭 |
| --- | --- | --- |
| SF-OPENAI-PROACTION-CODEX：[Proaction boosts sales 60% and saves 75+ hours with Codex](https://openai.com/index/proaction/) | 官方 News RSS `Fri, 25 Sep 2026 19:00:00 GMT` → `2026-09-26T03:00:00+08:00`，在 09/26 窗内，不是 09/27。 | 已读实际客户案例核心：把电话、邮件和表格上下文用于演示页面、插件与业务语音 Agent。效果数字是客户估计，不是受控实验；没有披露新模型机制、平台状态责任或训练/推理设计合同。**前分母关闭：业务应用/客户估算，无可迁移系统设计增量**。不评分、不 selected、不写 Books。 |
| SF-ANTHROPIC-NINE-LOOPS：[Yes, Claude can do Nine Loops](https://www.anthropic.com/research/yes-claude-can-do-nine-loops) | 官方 Research 元数据 `publishedOn=2026-09-25T16:58:00.000Z` → `2026-09-26T00:58:00+08:00`，在 09/26 窗内。 | 已读原文研究核心及验证边界：在已知高阶散射振幅计算方法上用科学 harness、Python/SymPy 与物理学家验证。文章明确不是发现新物理原则；重复继续提示与单一任务成功没有构成通用 Agent 正确性合同、训练或推理机制创新。**前分母关闭：当前暂停的 AI for Science 应用，且未披露对现有 LLM/Infra/Agent 设计的独立长期增量**。不是仅凭领域标签排除，也不把案例成功泛化为可靠 Agent 保证；不评分、不 selected、不写 Books。 |

其余机构仅复用 §1 相同实际停点：Qwen 合并公开列表、DeepSeek 可见目录及 Moonshot 所核发布均早于缺日；Google/Meta 的精确限制仍适用。没有用 09/27 无确认候选替代 09/26 的覆盖结论。

## 5. 交付边界

只创建本文件；未改 Daily README、Books、LEARNING_STATE、月度 checkpoint、Weekly 或共享索引。本文件是机构发现与精确限制材料，后续候选去重、整体来源覆盖、独立语义 Gate 及日报验收仍由主任务执行。
