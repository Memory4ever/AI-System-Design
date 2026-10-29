# Daily Research — 2026-05-17

**规范：** V3

**窗口：** 2026-05-16T09:00:00+08:00 ～ 2026-05-17T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-15T15:41:08+08:00

## 1. 结论

本次撤销旧 V2.1 报告的完成声明，重新按 14 个每日来源核验窗口。结论仍是本窗没有进入 Candidate Denominator 的 Source Family，但原因已经改变：不是“DataCite created-day 恰好为零”，而是所有到期来源都已按当前 first-public 口径检查，且没有可确认落入本窗并达到贡献门槛的事件。

旧报告的 279 个 arXiv identity 来自 submission/DataCite ingestion 混合窗口，不能作为 05-17 的原始命中。逐项调和后，279/279 均可排除出本窗：274 项分别出现在后续的 05-19（252）、05-20（11）、05-21（3）、05-25（1）、05-26（1）与 05-29（6）恢复记录；其余 5 项是 `2606.*` identity，分别出现在 06-02 的 DataCite boundary-created 记录（1）和 06-12 的 provisional raw bucket（4）。后 5 项足以证明不属于五月窗口，但当前材料不把恢复桶日期冒充已确认的官方首次公开日。旧 31 个候选全部包含在前述 274 项中，其后续记录分布为 05-19 的 28 项、05-20/05-25/05-26 各 1 项；其中 Charon 还存在更早的 ByteDance Seed 官方事件，已由 05-16 日报拥有。旧 exact-v1 阅读证据没有删除，但本日报不复用其评分、Books 决定或“完成”状态。

非 arXiv 来源的反向漏检检查发现 Meta 目录曾把 GIM 列为 05-17，但当前官方详情页写 05-18，arXiv v1 则明确为 2026-05-18T17:09:50Z（北京时间 05-19 01:09:50）。这个日期冲突不能让 GIM 成为 05-17 的确定候选；它只保留为后续真实 owner 日的调和线索，不支持本日报的证据或 Books 判断。其他机构入口的相邻事件均位于窗口外。

本窗漏斗为：14 个每日来源已检查，0 个可确认落窗的独立事件，0 个候选，0 个审阅，0 个 withdrawn，0 个 Books 写回。新的非作者终审已确认来源边界、旧记录排除和空 Books 队列，并收窄了旧 279 项的下游日期表述；本日报可以完成。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 Research](https://openai.com/research/) 与 RSS 相邻事件；Malta 合作公告为 2026-05-16T08:00:00+08:00，早于窗口起点，之后无窗内研究或系统事件 | 已检查 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)；官方时间字段由 2026-05-14 跳至 2026-05-22 | 已检查 | 无 |
| SRC-GOOGLE-AI | [Google DeepMind Publications](https://deepmind.google/research/publications/) 与 [Google Research Publications](https://research.google/pubs/)；相邻公开记录分别为 05-06/05-28 与 04-25/05-28 | 已检查 | 无 |
| SRC-META-AI | [Meta Research Publications](https://ai.meta.com/research/publications/) 及 [GIM 详情页](https://ai.meta.com/research/publications/gim-evaluating-models-via-tasks-that-integrate-multiple-cognitive-domains/)；目录的 05-17 日期与详情页 05-18 冲突，且 [arXiv:2605.18663v1](https://arxiv.org/abs/2605.18663) 为 05-19 01:09:50 北京时间，不能确认落入本窗 | 已检查 | 日期冲突已隔离为后续 owner 调和线索，不用于本窗候选或“无遗漏”断言 |
| SRC-QWEN | [Qwen 官方站点](https://qwenlm.github.io/) 的 publication/blog index；无窗内条目 | 已检查 | 无 |
| SRC-DEEPSEEK | [DeepSeek 官方入口](https://www.deepseek.com/) 的模型与研究发布索引；无窗内条目 | 已检查 | 无 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [MoonshotAI GitHub](https://github.com/MoonshotAI)；无窗内技术文章、首次公开仓库或 release，`pushed_at` 不作首次公开 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [腾讯混元 Research 全部列表](https://hunyuan.tencent.com/research)；相邻记录为 04-30 与 05-21 | 已检查 | 无 |
| SRC-ZAI | [智谱 Research](https://www.zhipuai.cn/zh/research)；相邻记录为 04-29 与 05-20 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [官方论文目录](https://seed.bytedance.com/en/public_papers)；Charon 为 2026-05-16T00:00:00+08:00，早于窗口起点，之后无窗内事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/) 与 release index；无 05-16/17 窗内条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [MiMo Paper / Blog](https://mimo.xiaomi.com/)；官方索引在 03-13 后跳至 06-29 | 已检查 | 无 |
| SRC-MINIMAX | [MiniMax Research / Blog](https://www.minimax.io/blog)；相邻技术文章为 03-18 与 05-26/27 | 已检查 | 无 |
| SRC-ARXIV | 官方 owner replay 的 05-17 receipt 为 raw identity=0、official OAI direct=0。旧 279 项中 274 项与 05-19～05-29 后续恢复记录逐项相交；5 个 `2606.*` identity 只按六月身份及 06-02/06-12 恢复桶排除出本窗，不把恢复桶写成已确认公开日 | 已检查 | 无 |

`已检查` 只证明上述注册入口及窗口的有界检查已经完成，不声称互联网中不存在任何其他材料。旧 279 项的精确去向见 [`OWNER_RECONCILIATION_V3_20260915.md`](../_sources/daily-20260517/OWNER_RECONCILIATION_V3_20260915.md)。

## 3. 候选与判断

本窗 Candidate Denominator 为 0。没有把旧 submission-window identity、窗外 GIM 或已有 exact-v1 阅读记录重新列为 05-17 候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

本窗没有候选，因此没有 V3 评分、Source Review 或 Books 修改。旧 31 个候选的 exact-v1 证据保留在原 `_sources` 中，只能由各自真实 owner 日在身份、精确版本和采用命题未变化时复用；不能为 05-17 提供 Evidence 或 Books Gate。

Books 写回队列为空，见 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260517/root-books-writeback-queue-v3.json)。

## 5. 缺口与下一步

无可执行待办。新的非作者终审已检查 14 个来源的窗口边界、279 项本窗排除、旧 31 候选的后续记录、空候选与空 Books 队列。

本窗终态保留项：Meta GIM 的目录日期 05-17 与详情页 05-18 不一致；arXiv v1 的精确时刻明确在本窗之后。该冲突不用于正面证据，不进入 Books，也不支撑“无遗漏”断言；定点重开条件是 Meta 提供可验证且落入本窗的首次公开时刻，否则不重开 05-17。

窗外调和边界：5 个 `2606.*` identity 的精确官方首次公开日仍由对应六月报告负责；05-17 只依据官方 identifier month 和后续恢复记录确认它们不属于本窗，不据此支持候选、Books 或六月 owner 完成声明。

## 6. 复核

复核者：`fresh-context:may17-nonauthor-final-20260915`

结论：通过

非作者终审重新核对了当前 14 个 Daily 来源、05-17 arXiv owner receipt、旧 279 个唯一 identity 与后续恢复记录的集合交集、旧 31 个候选、Charon 的 05-16 官方 owner、Meta GIM 的冲突日期以及空 Books 队列。终审发现并修正了把 5 个六月恢复桶日期写成已确认官方公开日的过度表述；该问题不改变 05-17 的零事件结论。完整记录见 [`V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md`](../_sources/daily-20260517/V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md)。机器校验只确认格式与可判定一致性，不替代上述语义复核。
