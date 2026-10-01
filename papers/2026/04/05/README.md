# Daily Research — 2026-04-05

**规范：** V3
**窗口：** 2026-04-04T09:00:00+08:00 ～ 2026-04-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T04:30:22+08:00

## 1. 结论

本窗尚未确认会改变 AI System 长期知识或 Books 既有判断的独立研究事件；这不是所有原始来源已证实零命中。14 个到期 Daily 来源中，11 个已取得与本窗相邻的官网目录或有界仓库停点，OpenAI Research、Meta Research/Publications 和 Google Research Publications 的历史精确日目录仍不可完整回溯，保留为彼此独立的外部限制。可核来源的候选分母为 **0**，无需为了制造 Books diff 修改章节；作者外的日期、来源、准入与 Books 独立语义复核已完成。

日期归属是本日的关键纠错。旧 [4 月 5 日原始筛选材料](../_sources/daily-20260405/)按 arXiv v1 提交/版本字段读出 `423` 条窗内 identity、`221` 条注册项、`17` 个旧候选；后来 [旧版日报存档](../_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-04-05.md)则按 DataCite DOI `created` 代理得出 `0`。两套时间字段都不是首次公开公告。arXiv [官方公告规则](https://info.arxiv.org/help/availability.html)写明通常仅美东 Sunday～Thursday 公告，新稿、替换和撤回通知也随公告发布；本窗对应美东 Friday 21:00 至 Saturday 21:00，下一次正常 Sunday 20:00 ET 公告是北京时间 **2026-04-06 08:00**，不在本窗。因此旧 `423/221/17` 不可继承为本日候选，旧 DOI-created `0` 也不是本日完成的独立证据。若有可核的特殊公告或机构首次公开正文，须按该事件定点重开。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | [Research](https://openai.com/research/)、[Research Index](https://openai.com/research/index/)及可回溯的[官方 News RSS](https://openai.com/news/rss.xml)；RSS 邻近条目是 04-02T10:30Z 和 04-06T10:00Z，本窗无 News 条目。 | 受阻 | News 不等于完整 Research；历史 Research 列表未取得本窗精确日分页停点。需官方历史目录、可核官网存档或当窗原始公告；不作 Research 零命中断言。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) 页面嵌入 `publishedOn` 的相邻项为 04-02T10:56Z 和 04-07T09:35Z；本窗无该官网目录条目。 | 已检查 | 只限定官网当前公开研究索引，不代替未列出的作者论文。 |
| `SRC-GOOGLE-AI` | [Google Research 4 月博客归档](https://research.google/blog/2026/04/)相邻文章为 04-03 [behavioral dispositions](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/) 与 04-09 后续文章；[DeepMind Publications](https://deepmind.google/research/publications/)精选目录从 04-25 跳至 03-22。 | 受阻 | [Google Research Publications](https://research.google/pubs/)只有年份/主题过滤，未取得精确日停点；博客日期无时刻，且 04-03 文章链接 02-11 已公开的 [2602.11328v1](https://arxiv.org/abs/2602.11328v1)，不能按再说明重复计分。恢复条件：官方日级目录或当窗原始论文。 |
| `SRC-META-AI` | [Meta AI Blog](https://ai.meta.com/blog/)可见邻近 04-08 与 03-26；[Research](https://ai.meta.com/research/)文本不可取，[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)请求超时。 | 受阻 | Blog 不能替代 Research；需官方历史研究目录、可核存档或当窗原始公告，不作该源零命中断言。 |
| `SRC-QWEN` | [官网动态接口](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 返回 40 条，其中 04-02T04:00+08 后至 04-15 无 04-04/05 项；[研究静态目录](https://qwen.ai/api/page_config?code=research.research-list) 60 条，均为更早项目。 [QwenLM](https://github.com/QwenLM) 组织公开仓库按创建时间 58/58 条触底，未见本窗新仓库。 | 已检查 | 限上述官网列表与新仓库；不把高频 CLI release 或普通提交当作未经触发的模型研究。 |
| `SRC-DEEPSEEK` | [官方研究与动态](https://www.deepseek.com/news/)可见动态 04-24 前接 2025-12，研究目录 06-24 前接 02-25。 | 已检查 | 限官网可见目录；未公开的作者工作不作零命中证明。 |
| `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog)目前最新 2025-11-07；[kimi-cli Releases](https://github.com/MoonshotAI/kimi-cli/releases)邻近 1.30.0 于 04-02T14:40:52Z、1.31.0 于 04-10；[MoonshotAI](https://github.com/MoonshotAI)按创建时间列出 43/43 个公开仓库，末项 2023-03-28。 | 已检查 | 有界官网、定点正式 release 与组织新仓库无本窗事件；不遍历全部日常 commit。 |
| `SRC-TENCENT-HUNYUAN` | [Research 全部列表](https://hunyuan.tencent.com/research)的官网 `publicList` 接口以 `renderType=0,pageNum=1,pageSize=100` 返回 9/9 条，历史日期由 04-23 跳至 02-13；[Tencent-Hunyuan](https://github.com/Tencent-Hunyuan)按创建时间列出 83/83 个公开仓库，末项 2024-05-10。 | 已检查 | 限官网公开列表和组织新仓库；不把无触发的旧仓库提交当研究事件。 |
| `SRC-ZAI` | [官方 Research](https://www.zhipuai.cn/zh/research)公开日期由 04-01 跳至 04-07；[发布说明](https://docs.z.ai/release-notes/new-released)由 02-12 跳至 04-07；[zai-org](https://github.com/zai-org)按创建时间列出 53/53 个公开仓库，末项 2021-05-25。 | 已检查 | CMS `createdAt` 不是公开日期；结论限上述官方目录与新仓库。 |
| `SRC-BYTEDANCE-SEED` | [官方论文目录](https://seed.bytedance.com/en/public_papers)通过官网列表 API `article_type=1,count=20,page_token=40`（总 242）跨 04-08 至 03-31；[研究博客](https://seed.bytedance.com/en/research)的 `article_type=2` 首页由 04-09 跳至 04-01；[ByteDance-Seed](https://github.com/ByteDance-Seed)按创建时间列出 63/63 个公开仓库，末项 2024-04-19。 | 已检查 | 论文目录含暂缓的 AI for Science，不能把站内总量当本项目候选；本窗可见目录没有独立条目。 |
| `SRC-BAIDU-ERNIE` | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/)相邻公开日期为 02-06 与 04-15；[ERNIE 正式 Releases](https://github.com/PaddlePaddle/ERNIE/releases)无本窗版本。 | 已检查 | 限技术博客和指定仓库正式 release。 |
| `SRC-XIAOMI-MIMO` | [MiMo 官网](https://mimo.xiaomi.com/) Paper 目录从 06-29 跳至 03-13；[XiaomiMiMo](https://github.com/XiaomiMiMo)按创建时间列出 18/18 个公开仓库，末项 2025-04-26。 | 已检查 | 无日期的卡片不能证明本窗发布；不把一般仓库提交当候选。 |
| `SRC-MINIMAX` | [英文博客](https://www.minimax.io/blog)、[中文博客](https://www.minimaxi.com/blog)的相邻日期为 03-18 与 04-27；[Agent Tech Blog 索引](https://agent.minimax.io/docs/llms.txt)只见 04-27 文章；[MiniMax-AI](https://github.com/MiniMax-AI)按创建时间列出 35/35 个公开仓库，末项 2025-01-14。 | 已检查 | 限官网目录及组织新仓库；不遍历所有旧仓库普通提交。 |
| `SRC-ARXIV` | [官方 Availability / Announcement Schedule](https://info.arxiv.org/help/availability.html)明确正常公告是美东 Sun–Thu 20:00；本窗落在 Sat 时段，下一正常批次为北京时间 04-06 08:00。 | 已检查 | 限正常公告；旧 v1 提交/版本时间与 DOI-created 均不可作为本窗首次公开。若发现特殊延期公告或独立机构首次公开，按具体事件核验。 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

可核来源的本窗唯一候选分母为 **0**；三个外部目录限制不参加“零命中”算术。旧 `_sources/daily-20260405/` 的 17 个按 v1 字段形成的候选保留在原始材料，不机械转成当窗评分行；其中 `2604.03588v1`、`2604.03679v1` 的保存全文也只证明当时读过正文，不证明本窗口公开。

## 4. 证据与知识整合

没有经本窗事件日期与贡献筛选共同确认的候选，Books Decision 为 **No Change**，无书稿改动。旧 V2.1 中的 `Complete`、`Passed` 和 Books 决定不能代替本窗 V3 证据；若外部目录恢复出真正的当窗材料，先核其 Source Family 与贡献，再依三维评分决定审阅深度和章节判断。

## 5. 缺口与下一步

- 尚可执行：无。14 个到期来源已完成有界检查，或将不可回溯目录精确隔离；可核来源没有需要 Source Review 或 Books 写入的本窗候选。
- **终态保留项：** OpenAI Research 历史分页、Meta Research/Publications、Google Research Publications 的精确日目录当前不可完整读取。三项分别隔离，**不用于正面证据、Books 或无遗漏断言**，不支持“全源零命中”。定点重开条件：获得官方历史目录、可核官网存档或明确落窗的原始公告后，仅重开受影响来源与对应日报，不重跑其它已核来源。
- 窗外原始库存：旧 423/221/17 基于 v1 提交/版本字段而非公告；无需为了本日零常规公告逐篇全文复审。以后发现其真正公告日时，只在真实归属窗口定点处理。

## 6. 复核

复核者：主任务（非本日报作者）
结论：通过

独立按北京时间左闭右开窗口复算其对应美东 Friday 21:00～Saturday 21:00，重核 [arXiv 官方公告规则](https://info.arxiv.org/help/availability.html)所列常规 Sun–Thu 20:00 ET，以及下一个 Sun 20:00 ET 位于 04-06 08:00 北京时间。逐行复看 14 来源的官网、列表或定点 artifact 停点：旧 v1 提交字段 `423/221/17` 与 DOI-created `0` 都不是首次公开公告，三份不可完整回溯的官方目录不能算零命中。可核来源没有独立候选，故 Books No Change；这项语义判断与后续格式校验分开记录。
