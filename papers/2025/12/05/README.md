# Daily Research — 2025-12-05

**规范：** V3
**窗口：** 2025-12-04T09:00:00+08:00 ～ 2025-12-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T19:52:26+08:00

## 1. 结论

1个确定落窗家族作者侧标准审阅：Anthropic Interviewer提供访谈自报与聊天轨迹口径不等同的局部证据，不证明自治或生产率因果变化。5分；Books测量对象/人口/标签边界已有具体覆盖，无改书。14源独立有限检查，普通待办0；四个具名arXiv潜在贡献和旧目录仍外部隔离，不是Coverage通过或零事件；Mill已完成非作者独立核验，具体范围及日级结果见§6。

## 2. 来源覆盖

每源原始邻接、查询/停止及筛选见[本日记录](../_sources/daily-20251205/WINDOW_REVIEW.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮RSS Dec4/5仅Dec4 19Z Australia，政策合作核心非新机制 | 已检查 | 仅入口主题切片，不是全机构保证 |
| SRC-ANTHROPIC | Interviewer原生HTML datePublished Dec4 17Z，Method/口径/Limitations | 已检查 | 当前页维护时间不授新研究事件 |
| SRC-GOOGLE-AI | Blog2025第1页Dec3/Dec4/Dec10，Titans/MIRAS核心与两份旧v1；DeepMind第3页Dec3/Jan9 | 已检查 | MSEB旧必要日期隔离，不把目录或Blog介绍作首次论文 |
| SRC-META-AI | 原始第4页Dec1/Dec12连续邻接 | 已检查 | 不外推全站零事件 |
| SRC-QWEN | 原始旧Sep23/新动态与部署/仓库有限替代按本窗重核 | 受阻 | 2025历史目录缺失隔离 |
| SRC-DEEPSEEK | 正确API Docs Dec1/下一2026邻接，已恢复card身份 | 已检查 | 不用现页全部版本反填历史 |
| SRC-MOONSHOT | 全Overview26项最近Nov7、changelog Nov6邻接 | 已检查 | 本窗未见该入口新条目 |
| SRC-TENCENT-HUNYUAN | All11项2026及旧Research失败原始观察 | 受阻 | 2025历史Research缺失隔离 |
| SRC-ZAI | 原始All第2页18条到Dec7、release Dec8 | 受阻 | 更旧目录未保留，不能零命中 |
| SRC-BYTEDANCE-SEED | 2025Paper首段Dec15/Dec2/Oct22、Blog Dec16/Dec2/Nov27 | 已检查 | 日编码不补精度，不重授GR-RL日期 |
| SRC-BAIDU-ERNIE | 原始Blog2/2页至Nov7，Nov21/Dec9边界 | 已检查 | 无全机构召回保证 |
| SRC-XIAOMI-MIMO | Paper8项与route HSS Dec19/Safety Dec18；Blog15项原始观察 | 受阻 | 无date/旧More历史完整性隔离 |
| SRC-MINIMAX | 英文13项和中文Oct27/Dec23原始邻接 | 已检查 | 未触发具名AgentTech新事件 |
| SRC-ARXIV | 四主题Dec4查询；官方cs.PL首1–25标题，相关完整精确v1题摘 | 受阻 | 查询越日期、月身份/提交不授first-public |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI](https://www.anthropic.com/research/anthropic-interviewer) | 2025-12-05T01:00:00+08:00 | 访谈与聊天日志的自动化口径差异揭示下游使用/人口边界不能混合；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)目标→EvalSpec及标签粒度段 |

## 4. 证据与知识整合

### [Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI](https://www.anthropic.com/research/anthropic-interviewer)

原字段`article:published_time`与`datePublished=2025-12-04T17:00:00.000Z`完全落窗。Method及Limitations支持crowdworker样本、AI访谈demand effects、静态/自报限制；访谈与既有日志不是配对同任务对照，不采用差值为因果测量或能力增益。三阶段instrument披露不等于新Agent执行机制，准入仅为可复查的评价边界。

Ch66实际约79–110定义eligible population、slice、scorers和标签生成链/轨迹粒度/缺失，不从能采集的proxy倒推目标；相邻Ch65资源政策、Ch67observed health不授质量判断。本窄命题已有覆盖，不新增正文。完整必要证据、未披露条件和采用边界见[作者记录](../_sources/daily-20251205/WINDOW_REVIEW.md#anthropic-interviewer准入证据与books)。未核代码/复现实验，无Books写入。

## 5. 缺口与下一步

作者普通待办0，准入/证据/已有覆盖及来源复核以Mill维护的§6为准，作者不覆盖该结论。以下为本窗终态保留项：[Tensor accelerators 2512.02371v1](https://arxiv.org/abs/2512.02371v1)、[Lumos 2512.02966v1](https://arxiv.org/abs/2512.02966v1)、[Beyond Code Pairs 2512.03086v1](https://arxiv.org/abs/2512.03086v1)、[SpatialReasoner 2512.03284v1](https://arxiv.org/abs/2512.03284v1)完整题摘有具体潜在机制，缺个体首公开；不评分、不用于正面证据、不进入 Books、不支撑无遗漏或性能/安全保证。隔离不计Coverage/Evidence通过或零事件。日list/catchup/API、announced年月/OAI/月列表的有限替代已明确不能提供权限，恢复需具名精确v1历史new/RSS/email或真实作者首次正文，仅重开真实归属日。

Qwen/Hunyuan/Z.ai/MiMo必要旧目录及Google MSEB已有日期请求亦为本窗终态保留项：不用于正面证据、不进入 Books、不支撑无遗漏或性能/安全保证，不授Coverage/Evidence或零事件。重开需原始2025目录邻接、具名官方历史发布/首次正文区间，只重开真实归属日，不反复同端点，不重复采为本日候选。

窗外线索：cs.PL标题补检发现reduced-precision AoS/SoA、MLIR abstract transformers、Nightjar共享状态、LOOPRAG与speculative tool calls，精确v1提交均在本窗后且无更早正文依据。只留原始身份，不扩大本窗或整月队列。本日独立验收已完成，窗外线索不扩入本窗。

## 6. 复核

复核者：Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`；非作者Gibbs。

结论：通过

实际日级复核见[本日追加记录](../_sources/daily-20251205/ROOT_ADMISSION_REVIEW.md)。核14源原始范围/有限停点；独立RSS758460 bytes和Australia正确原文，Anthropic原生HTML341440 bytes及meta/JSON发布日期Dec4 17Z，实际Method/口径/限制/Appendix标准审阅。候选分母1，窄评价命题5分通过；四个潜在精确v1完整题摘全部独立校准，包括Lumos安全信号，未知first-public不授Evidence/Books。cs.PL网页失败后原生45620 bytes实际首25标题，不扩月库存。

普通负侧分层5项：Australia核心、Titans/MIRAS Blog与两家族v1题摘、AoS/SoA05516和MLIR06442题摘；没有用“成熟组合无控制/边界”排除局部反证。其余无关题名、全版本史未全量验证；新具名窗外NeuroInv只保留真实归属线索，不把Dec17 submit授first-public。Books实际对读Ch66约79–110具体EvalSpec/标签边界及Ch65/67交接，已有覆盖成立，不改书。

作者已实际同步§5四项具名潜在贡献及旧目录/MSEB为本窗终态保留项，明确不用于正面证据/Books/无遗漏和具名恢复后真实日定点重开。本轮只定点核该补正，未重读未变来源；原范围、1确定落窗候选5分和具体已有覆盖判断维持，普通差额0，无新增Books proposal。外部终态不授Coverage/Evidence或零事件。完成态V3实际通过（exit 0），不替代语义判断；未stage/commit/push。
