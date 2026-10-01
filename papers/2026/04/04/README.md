# Daily Research — 2026-04-04

**规范：** V3
**窗口：** 2026-04-03T09:00:00+08:00 ～ 2026-04-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T04:04:43+08:00

## 1. 结论

截至本次检查，尚未确认本窗有值得进入 AI System 长期知识库的独立候选；**这不是 14 个来源已全部零命中的断言**。旧 V2.1 报告把 2026-04-04 的 DataCite DOI `created` 条目当作当日 arXiv 首发，后来又以该口径得出 `0`；两个方向都不能代替官方公告时间。arXiv [公告规则](https://info.arxiv.org/help/availability.html)明确周五、周六通常不公告：本窗在美东周五晚与周六早之间，没有常规新稿批次。旧 434 条 raw identity、51 个旧候选仍作为历史线索留在[原始材料](../_sources/daily-20260404/)，不作为本日 V3 命中或候选。

机构目录已找到若干跨窗停点；Google Research 的 4 月 3 日技术博客指回 2 月已公开的同一篇论文，当前看不出独立机制或评价合同增量，不能因博客日期重复计分。官方仓库的定点 release 检查亦未发现本窗事件；这不是穷举所有仓库提交。OpenAI、Meta 的历史研究目录和 Google Research Publications 的精确日停点仍不可得，须作为不支持“全源零命中”断言的来源限制隔离。其余可执行窗口检查和独立语义复核已结束；本日完成只表示可用证据处理到安全终态，不表示受阻目录已证实无命中。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | [Research](https://openai.com/research/)、[Research Index](https://openai.com/research/index/)和可回溯的[官方 News RSS](https://openai.com/news/rss.xml)：RSS 2026-04-02 10:30 UTC 后无 04-03/04 项。 | 受阻 | News 不等于完整 Research；历史 Research 列表只见近期卡片，未取得本窗分页停点。待官方可读历史目录或当窗存档；不作零命中断言。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) 页面嵌入的 `publishedOn` 邻近项为 `2026-04-02T10:56:00Z` 的 emotion concepts，早于本窗。 | 已检查 | 仅限当前官方 Research 可见索引，不替代未列出的作者论文。 |
| `SRC-GOOGLE-AI` | [Google Research 4 月博客归档](https://research.google/blog/2026/04/)中 04-03 唯一邻近条目 [behavioral dispositions](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/)；[DeepMind Publications](https://deepmind.google/research/publications/)精选目录跨过 04-03，04-25 前接 03-22。 | 受阻 | Google Research [Publications](https://research.google/pubs/)只提供年份/主题过滤，现有入口无法取得可靠本窗停点；博客日期没有时刻，不据日期本身证明落窗。恢复条件：官方精确日目录、当窗原始论文或归档。 |
| `SRC-META-AI` | [Meta AI Blog](https://ai.meta.com/blog/)可见邻近 04-08 与 03-26；[Research](https://ai.meta.com/research/)文本为空，[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)请求超时。 | 受阻 | Blog 不能替代 Research。需官方历史研究目录/存档，否则不作该源零命中断言。 |
| `SRC-QWEN` | [官方动态接口](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 40 条与[研究静态目录](https://qwen.ai/api/page_config?code=research.research-list) 60 条，动态日期邻近 03-30、04-02 后无 04-03/04。[QwenLM 官方组织](https://github.com/QwenLM)按创建时间列出 58/58 个公开仓库，末项创建于 2023-08-03；定点查看 [Qwen3](https://github.com/QwenLM/Qwen3/releases)、[Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni/releases)、[Qwen-Image](https://github.com/QwenLM/Qwen-Image/releases)与[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent/releases)，未见本窗模型/Agent 正式 release。 | 已检查 | 结论限官网列表、组织新仓库与上述定点 release；未遍历高频 CLI 工具版本或普通提交。 |
| `SRC-DEEPSEEK` | [官方研究与动态](https://www.deepseek.com/news/)可见动态 04-24 前接 2025-12-01，研究索引 06-24 前接 02-25。 | 已检查 | 结论仅针对官网可见目录；普通仓库提交不作为研究事件。 |
| `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog)当前最新 2025-11-07；[kimi-cli 官方 Releases](https://github.com/MoonshotAI/kimi-cli/releases)邻近 `1.30.0` 为 04-02T14:40:52Z、`1.31.0` 为 04-10，不在本窗；[MoonshotAI 官方组织](https://github.com/MoonshotAI)按创建时间列出 43/43 个仓库，末项创建于 2023-03-28，未见本窗新仓库。 | 已检查 | 结论限官网博客、定点 CLI release 和组织新仓库；不把组织全部历史 commit 当作日报。 |
| `SRC-TENCENT-HUNYUAN` | [Research](https://hunyuan.tencent.com/research) 对应官方 [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，`renderType=0,pageNum=1,pageSize=100` 返回 9/9 条；日期从 04-23 直接到 02-13。[官方组织](https://github.com/Tencent-Hunyuan)按创建时间列出 83/83 个仓库，末项创建于 2024-05-10；[HunyuanVideo Releases](https://github.com/Tencent-Hunyuan/HunyuanVideo/releases)无邻近本窗 release。 | 已检查 | 限官网研究列表、组织新仓库及定点版本；不宣称未列出的作者论文绝不存在。 |
| `SRC-ZAI` | [官方 Research](https://www.zhipuai.cn/zh/research)可见发布日期 04-01 后到 04-07；[官方发布说明](https://docs.z.ai/release-notes/new-released)邻近 04-07 与 02-12；[官方组织](https://github.com/zai-org)按创建时间列出 53/53 个仓库，末项创建于 2021-05-25；[GLM-5 Releases](https://github.com/zai-org/GLM-5/releases)无本窗 release。 | 已检查 | CMS `createdAt` 不能当公开日期；检查范围限上述入口与定点仓库。 |
| `SRC-BYTEDANCE-SEED` | [官方论文目录](https://seed.bytedance.com/en/public_papers) 的公开列表 API `article_type=1,count=20,page_token=40`，总 242 条；该页日期由 04-08/07 跨至 03 月。[研究博客](https://seed.bytedance.com/en/research) 对应 `article_type=2` 首页 04-09 前接 04-01。[官方组织](https://github.com/ByteDance-Seed)按创建时间列出 63/63 个仓库，末项创建于 2024-04-19；[VeOmni Releases](https://github.com/ByteDance-Seed/VeOmni/releases)无本窗 release。 | 已检查 | 两种官网目录无本窗条目；不把日常 CI commit 计为研究，也不宣称所有历史仓库都已逐个审完。 |
| `SRC-BAIDU-ERNIE` | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/) 从 04-15 接 02-06；[ERNIE Releases](https://github.com/PaddlePaddle/ERNIE/releases)无本窗 release。 | 已检查 | 限官网博客及指定仓库的正式 release。 |
| `SRC-XIAOMI-MIMO` | [MiMo 官网](https://mimo.xiaomi.com/) Paper 列表 06-29 前接 03-13；[官方组织](https://github.com/XiaomiMiMo)按创建时间列出 18/18 个仓库，末项创建于 2025-04-26；[MiMo-V2-Flash Releases](https://github.com/XiaomiMiMo/MiMo-V2-Flash/releases)无本窗 release。 | 已检查 | 无日期的博客卡片不证明本窗事件；不把仓库普通提交当独立发布。 |
| `SRC-MINIMAX` | [英文博客](https://www.minimax.io/blog)与[中文博客](https://www.minimaxi.com/blog)的相关日期跨 03-18→04-27；[Agent Tech Blog 索引](https://agent.minimax.io/docs/llms.txt)仅可见 04-27 文章。[官方组织](https://github.com/MiniMax-AI)按创建时间列出 35/35 个仓库，末项创建于 2025-01-14；[MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1/releases)和[MiniMax-M2](https://github.com/MiniMax-AI/MiniMax-M2/releases)无本窗 release。 | 已检查 | 限官网目录、组织新仓库及定点模型 release；未遍历所有普通提交。 |
| `SRC-ARXIV` | [官方公告规则](https://info.arxiv.org/help/availability.html)：新稿、替换与撤回通常在 Sun–Thu 美东 20:00 公告，无 Fri/Sat 公告；本窗对应该常规空档。 | 已检查 | 限于常规公告；旧 DOI-created 库不用于推断本窗新稿，若有特殊 deferred mailing/单篇可核反证，定点重开。 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

本窗可核来源的独立候选分母冻结为 **0**；三个受阻目录不进入零命中算术。唯一需说明的邻近研究是 [Google Research 04-03 博客](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/)：它讨论 25 个模型的情境判断、人的共识分布与模型过度自信，但明确链接到 [arXiv:2602.11328v1](https://arxiv.org/abs/2602.11328v1)，官方版本页列出 2026-02-11 提交且无 4 月修订。博客目前未显示脱离该论文的新机制、纠错或独立评价合同，按 Source Family 只作跨来源再说明，不作为 04-04 新候选或评分；博客自身只有 04-03 日历日，没有核实到足以断言落在 09:00～09:00 窗口的时刻。

## 4. 证据与知识整合

当前没有经本窗日期、贡献与证据三层确认的候选，因此本窗 Books Decision 为 **No Change**，无书稿修改。这不是对三个受阻目录的负面证明；旧 V2.1 的 51 项 Books disposition 和 `Complete` 也未自动转为本日报结论。

## 5. 缺口与下一步

- 本窗尚可执行工作：无。已对 14 个到期来源逐项检查或精确隔离外部不可访问项；无可核入选候选需要 Source Review 或 Books 写入。
- 终态保留项（外部目录限制）：OpenAI Research 历史分页、Meta Research/Publications 与 Google Research Publications 的精确日目录当前不可完整读取。三项分别隔离，**不用于正面证据、Books 或无遗漏断言**，也不支撑“官方全源零命中”。定点重开条件：取得相应官方历史目录、可核官网存档或当窗原始公告链接后，仅重开受影响来源/材料，不重跑本窗已闭合项。
- 窗外原始数据：旧 `_sources/daily-20260404/` 的 434 条 DOI-created 身份和 51 项旧候选不能迁成本窗候选；如发现其中真正的官方公告日期属于相邻日，只在其真实归属日报处理，不要求为了本日零新稿逐篇重读其 PDF。

## 6. 复核

复核者：主任务（非本日报作者）
结论：通过

独立重开 [arXiv 公告规则](https://info.arxiv.org/help/availability.html)，核对该北京时间窗口对应的 Fri/Sat 常规空档及延期例外；重开 [Google 04-03 博客](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/) 与 [原论文版本页](https://arxiv.org/abs/2602.11328v1)，确认博客只给日历日、指向同一 Source Family，未见独立机制/纠错。逐行检查 14 来源实际入口、官方仓库定点 release 范围、旧 DOI-created 数据不继承、三个外部缺口各自的隔离和重开条件；没有把受阻项当零命中、把摘要当全文审阅，或用机器格式检查替代本次语义判断。
