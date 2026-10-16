# Daily Research — 2026-05-03

**规范：** V3

**窗口：** 2026-05-02T09:00:00+08:00 ～ 2026-05-03T09:00:00+08:00

**状态：** 完成

**阶段：** Coverage、Evidence 与 Books 已处理到安全终态；独立复核通过

**Books：** 纳入本次

**检查时间：** 2026-09-14T15:35:00+08:00

## 1. 结论

本次按当前合同重新检查十四个每日来源，在可核验的官方入口中没有确认落入本窗、同时能够改变大模型或 AI Infrastructure 长期设计判断的新材料。已确认的窗内原始材料身份为 0，贡献候选为 0，因而没有评分、Evidence Review 或 Books 写回；Books Decision 为 `No Change`。

旧过程材料曾把 2026-05-02/03 的 arXiv `submitted_v1_utc` 命中记成 512 个原始条目、274 个注册分类条目和 36 个候选。这个口径不符合当前以首次公开公告决定 owner day 的规则：arXiv 官方说明 Friday、Saturday 不发布公告，且提交时间不等于公开时间。本窗在北京时间 Sunday 09:00 截止，未跨过下一次公开公告；因此这些提交记录不属于 05-03，不能用于本日报的候选、评分或 Books 判断。旧账本保留为来源恢复过程证据，但被本报告的日期归属结论取代。

三个入口存在日级历史发现限制：Google Research 的部分目录只给年份或月份、Qwen 注册入口已重定向且新站未提供可提取的历史日级列表、MiMo Blog 卡片未披露日期。它们被隔离为不支持“绝对无遗漏”断言的保留项；其余可核验来源也只证明列明官方入口的公开记录。作者完成来源与日期审计后，非作者重新核对公告节奏、旧提交时间错配、十四源范围与零候选的 Books 判断，未发现需要重开本日的材料。

## 2. 来源覆盖

本轮只检查每日来源。表中的“已检查”只表示列明入口及停止点已经核对，不表示该机构所有公开渠道绝无遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 的模型、视觉与音频研究目录；可见相邻模型条目为 04-23 与 07-09，未见窗内事件 | 已检查 | Research 首页是精选目录；不把 sitemap 的修改时间当首次公开时间 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 的带日期出版目录；相邻公开记录为 04-30 与 05-07 | 已检查 | 限官方公开目录 |
| SRC-GOOGLE-AI | [Google DeepMind News](https://deepmind.google/blog/)与[Publications](https://deepmind.google/research/publications/)，并核对 [Google Research Publications](https://research.google/pubs/) | 受阻 | DeepMind 可见出版记录在 04-25 后跳至 05-06；Google Research 部分索引只给年份或月份，不能据此作日级全站无遗漏断言 |
| SRC-META-AI | [Meta AI Results](https://ai.meta.com/results/)及下一页；跨页核对到 04-16、05-04、05-06 等相邻记录 | 已检查 | 只覆盖官方 Results 目录；没有把人物页或领域应用当作窗内研究事件 |
| SRC-QWEN | [注册入口](https://qwenlm.github.io/)及其官方 sitemap；旧站最新公开目录止于 2025，另核对 QwenLM 官方仓库的创建日期，没有窗内新仓库身份 | 受阻 | 注册入口已重定向到新站；新站未提供可提取的历史日级研究列表，不能证明窗内绝对为零 |
| SRC-DEEPSEEK | [官网研究入口](https://www.deepseek.com/)与[官方更新日志](https://api-docs.deepseek.com/zh-cn/updates/)；相邻可核验更新为 04-24，官方仓库无窗内新项目身份 | 已检查 | 限官网、更新日志与官方组织公开记录 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)完整可见目录及 [MoonshotAI GitHub](https://github.com/MoonshotAI) 项目创建记录；窗口附近没有新身份 | 已检查 | Blog 目录止于 2025；仓库检查只用于发现公开项目，不把普通提交活动当研究事件 |
| SRC-TENCENT-HUNYUAN | [Research“全部”列表](https://hunyuan.tencent.com/research)的公开接口返回 8/8 条记录；相邻记录为 04-30 与 05-06 后的仓库项目 | 已检查 | 限 Research 列表和官方组织的公开项目身份 |
| SRC-ZAI | [智谱 Research](https://www.zhipuai.cn/zh/research)完整可见目录及 zai-org 项目创建记录；相邻研究条目为 04-29 与 05-20 | 已检查 | 限官方目录和公开项目身份 |
| SRC-BYTEDANCE-SEED | [Seed Research](https://seed.bytedance.com/en/research)及出版目录；相邻项目相关条目为 04-26 与 05-16，官方组织无窗内新项目身份 | 已检查 | AI for Science 按当前 ROADMAP 暂缓，且本窗也无相关日级命中 |
| SRC-BAIDU-ERNIE | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/)完整首页；相邻条目为 04-30 与 05-09，ERNIE Releases 无窗内发布 | 已检查 | 限官方博客与公开 Release；排行榜条目本身也不自动构成机制候选 |
| SRC-XIAOMI-MIMO | [MiMo Paper / Blog](https://mimo.xiaomi.com/)与 XiaomiMiMo 项目创建记录；Paper 的相邻可验证日期为 03-13 与 06-29，仓库无窗内新项目身份 | 受阻 | Blog 卡片不披露稳定日级时间，不能据此证明窗内绝对为零 |
| SRC-MINIMAX | [英文 Research](https://www.minimax.io/blog)、[中文技术入口](https://www.minimaxi.com/blog)和 [Agent Tech Blog](https://agent.minimax.io/docs/techblog)；相邻带日期条目晚于 05-13 或 05-25/26 | 已检查 | 中英文目录对部分条目的日期口径不同，但均不与本窗相交 |
| SRC-ARXIV | [官方公告日程](https://info.arxiv.org/help/availability.html#announcement-schedule)及既有 DataCite/OAI owner replay；本窗覆盖 Friday/Saturday 的非公告区间，确认公开身份 0 | 已检查 | 提交时间、DOI ingestion 和 current OAI datestamp 不拥有 first-public day |

## 3. 候选与判断

日期归属、跨来源去重、项目范围和贡献判断后没有留下候选。候选为零时不生成空评分，也不把受限入口或窗外提交记成零分候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

本窗没有候选进入 Evidence Review，因此没有需要与 Books 命题比较的机制增量，也没有 Stable Knowledge Node owner。Books Decision 为 `No Change`，没有修改 `books/`。

这一判断只表示“本窗没有确认的贡献候选”，不是说旧过程材料中的论文都没有价值。旧 36 个候选若在后续 owner day 按当前贡献标准仍然成立，应由真实首次公开窗口承担证据审阅与 Books 处置；05-03 不沿用其旧评分、旧 Books 结论或已完成状态，也不删除其他日期已经有合法证据支持的 Books 正文。

## 5. 缺口与下一步

本窗没有仍可由作者继续执行的候选、Evidence Review 或 Books 写回。以下是已经隔离的外部发现限制，不支持正面证据、Books 或“本窗绝对无遗漏”断言：

**终态保留项：** 下列限制均不支持正面证据、Books 或无遗漏断言；每项只在对应的官方日级时间或唯一材料身份恢复时定点重开。

- `SRC-GOOGLE-AI`：Google Research 日级历史发布时间不可从当前索引完整恢复。若官方目录补充日级时间，或出现可唯一定位到本窗的重要模型/系统事件，只重开该材料。
- `SRC-QWEN`：注册入口迁移后缺少可提取的 2026 日级历史研究列表。若新站公开可查询归档，或官方项目提供可唯一定位到本窗的发布记录，只重开对应 Source Family。
- `SRC-XIAOMI-MIMO`：Paper 列表有日期而 Blog 卡片无日期。若官方 Blog 披露日级时间，或材料自身 metadata 能唯一定位本窗，只重开该条目。

窗外恢复项：旧 `screening-ledger-v2.1` 的 512 个提交时间命中不归 05-03；它们需要在实际公开公告所属日期执行去重、撤回检查和贡献判断，不能整体搬成下一日候选，也不阻塞本窗作者侧结束。

## 6. 复核

复核者：`/root`（非作者 fresh-context 复核）

结论：通过

独立复核者重新检查了固定窗口、十四个每日来源、arXiv 官方公告日程与旧提交时间错配。官方规则确认 Friday、Saturday 不发布公告，本窗在下一次 Sunday 20:00 ET 公告前结束；旧 512/274/36 只反映提交时间分组，不能拥有 05-03。报告没有把受限入口用于正面证据或无遗漏断言，零候选与 `No Change` Books 决定相称，未发现明显假阴性或未处理的可执行工作。机器校验和 Markdown 检查只作为格式证据，不替代本次语义复核。
