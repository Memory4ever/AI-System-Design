# Daily Research — 2026-08-29

**规范：** V3
**窗口：** 2026-08-28T09:00:00+08:00 ～ 2026-08-29T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T17:55:00+08:00

## 1. 结论

本窗从 14 个每日来源中确认四个材料家族：Anthropic 的自动化对齐研究闭环与主观研究评估方法、腾讯混元 Hy4 preview 模型/运行时 artifact，以及 OpenAI 对 Cursor 的供应合同变更。相邻日报的来源水位与官方日期将三个仅有日级日期的发布收窄到本窗内；Hy4 以初始 commit 的精确时间归属。arXiv 在本窗没有新的公告批次。

四项均已读到足以支撑采用命题的原始正文。前三项强化现有 Evaluation、MoE、长上下文与推理执行主线，Books 已有具体论点承载；OpenAI 事件只证明供应关系与未来可用性变化，不披露模型机制，故仅报告。独立复核确认来源归属、证据边界与 Books 处置一致，本日闭环。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 列表与 2026-08-28 官方说明；8 月 28 日 09:20 水位尚未出现该页，官方日期将公开范围收窄到本窗 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 与 Alignment Science Blog；8 月 28 日 09:20 水位无命中，两个官方页面均标 8 月 28 日，范围收窄到本窗 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind/Research Blog 日期列表越过 8 月 28 日；年度 Publications 增量已按原始发布日期去重 | 已检查 | 无 |
| SRC-META-AI | 官方 Research/Results 日期列表越过窗口，最近项目早于 8 月 28 日 | 已检查 | 无 |
| SRC-QWEN | 官方论文与模型列表检查至窗口前条目 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究入口与官方仓库发布面检查至窗口水位 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 仓库/Release 检查至窗口水位 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”列表、官方仓库与 Hy4 初始 commit；确认一个本窗模型 artifact | 已检查 | 无 |
| SRC-ZAI | Research、官方发布说明与仓库检查至窗口水位 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research/论文目录检查至窗口前条目 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与 ERNIE 仓库检查至窗口前条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo 论文/博客与官方仓库检查至窗口前条目 | 已检查 | 无 |
| SRC-MINIMAX | 中英文 Research/Blog 与官方仓库检查至窗口前条目 | 已检查 | 无 |
| SRC-ARXIV | 官方公告日程与相邻已闭合批次核对；北京时间周五 09:00 后至周六 09:00 无新公告批次 | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Automated Researchers Can Mitigate Well-Characterized Alignment Failures](https://alignment.anthropic.com/2026/automated-alignment-researchers/) | 2026-08-28T09:20:00+08:00 ～ 2026-08-29T00:00:00+08:00 | 自动研究 Agent 的 proposal、experiment、evaluation 与 commit 权限分离；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的独立 evaluator、hidden evidence 与发布 Gate |
| [TASTE: Can AI Models Judge AI Safety Research Proposals?](https://alignment.anthropic.com/2026/taste/) | 2026-08-28T09:20:00+08:00 ～ 2026-08-29T00:00:00+08:00 | 无客观 oracle 时以专家讨论、置信与分歧构造可审计 evaluator；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的多证据 adjudication 与 abstention |
| [Hy4 preview](https://github.com/Tencent-Hunyuan/Hy4-preview/tree/72c695e1d35f031d6a1c6cc19b748b1c46222bf3) | 2026-08-28T14:58:08+08:00 | 770B/49B-active MoE、稀疏 attention、跨层索引复用与原生 MTP 的共同部署 artifact；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md)；INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) | 2026-08-28T09:20:00+08:00 ～ 2026-08-29T00:00:00+08:00 | 模型供应终止改变 provider dependency 与迁移合同，但不披露技术机制；1 + 2 + 2 = 5 | 标准完成 | 仅报告：只保留版本/供应事实，不把未披露原因写入 PLATFORM-PRODUCTION |

## 4. 证据与知识整合

### [Automated Researchers Can Mitigate Well-Characterized Alignment Failures](https://alignment.anthropic.com/2026/automated-alignment-researchers/)

原始报告把研究循环拆为问题提出、实验执行、结果评估与研究方向选择，并通过受限工具、独立验证与人工/外部评价降低自证闭环。它证明在作者给定环境中，自动研究者能发现并缓解一组对齐失败；不能证明 evaluator 不会与 generator 共偏、hidden set 永不泄漏，或系统可以无人监管地提交长期结论。长期设计含义是 proposal authority 与 acceptance/commit authority 必须分离，这已由 Ch66 的 evidence object、独立 evaluator 与 release gate 承载。

### [TASTE: Can AI Models Judge AI Safety Research Proposals?](https://alignment.anthropic.com/2026/taste/)

TASTE 面对没有单一 ground truth 的研究问题，不把一次模型评分当作置信度，而是保留多位专家的理由、置信区间与分歧，再据此筛选可继续研究的命题。其证据支持“主观任务也需要显式评价合同与 abstention”，不支持把专家共识当作事实证明。Ch66 已区分 metric、judge、human adjudication 与 decision owner，因此无需重复追加。

### [Hy4 preview](https://github.com/Tencent-Hunyuan/Hy4-preview/tree/72c695e1d35f031d6a1c6cc19b748b1c46222bf3)

初始 commit 固定了模型卡、权重入口、部署与微调说明：backbone 为 770B 总参数、49B token-active 的 MoE，77 个 MoE 层各含 256 routed experts 与一个 shared expert；attention 采用 Gated DSA 与跨层 IndexCache，并提供一层原生 MTP 及 vLLM/SGLang 启动方式。模型卡只证明公开配置和作者 benchmark，未披露完整训练数据、算力、并发、SLO 或独立复现；这些数字不能外推为通用 MoE 或 speculative decoding 性能常数。现有 Ch21、Ch22 与 Ch48 已拥有条件计算、长上下文索引与 MTP 的机制和 trade-off，本项作为组合 artifact 不改变结论。

### [Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)

官方说明只证明供应关系将终止、未来模型不再继续提供这一合同事实。它没有公开内部安全判断、模型行为变化或基础设施机制，因此不能反推技术原因，也不足以修改长期章节；只作为 provider concentration、迁移与退出计划的窗口事实保留。

## 5. 缺口与下一步

无

## 6. 复核

复核者：`/root/aug01_08`
结论：通过

14 个每日来源均有本窗检查结论，四个候选与本节标题一一对应。当前官方页面确认两篇 Anthropic 材料的日期、标题与采用命题；Hy4 使用固定初始 commit，OpenAI 事件只保留供应合同事实，没有反推内部机制。评分与审阅深度相符，未见 withdrawn 或漏掉的 Structural Candidate。Ch21、Ch48、Ch66 的具体机制可定位；OpenAI 项保持仅报告是安全边界。报告、Evidence 与 Books Decision 均已完成。
