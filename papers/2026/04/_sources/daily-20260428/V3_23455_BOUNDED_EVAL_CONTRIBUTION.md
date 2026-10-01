# 2604.23455v1 CUJBench：跨浏览器—后台诊断的有界贡献复核（作者侧）

此处只在完整题摘准入后读决定贡献的 exact-v1 方法与关键反证、对读实际 owner；不把本文或 87 个场景自动记为正式候选/Books 整合。旧题摘与初筛在 `V3_ARXIV_ADMISSION_BATCH2.md`，先前 Ch66 对读线索在 `V3_THREE_ABSTRACT_OWNER_RESCREEN.md`。

| 核项 | 原文证据与条件 |
| --- | --- |
| 评价对象 | [官方 v1 §II-A/C/D](https://arxiv.org/html/2604.23455v1) 把一次已失败的 critical user journey 定义为冻结 incident snapshot，拆 `E_frontend`（截图/HAR/DOM/console）、`E_backend`（日志/trace/metric）与 operational context；Agent 通过固定缓存工具查询，提交 component、layer、fault type、解释和 evidence IDs，实际 trajectory 另记。Fault injection spec→独立 reviewer evidence chain→抽样人类验证给出三层标签。这不是浏览器 Agent 的正常任务完成率，也不是纯后台 RCA。 |
| 窄评价反证 | [§III-A–E](https://arxiv.org/html/2604.23455v1#S3) 的完整 corpus 是 87 个场景，但六模型×三条件实际只在挑选的 25 个场景跑 446/450 次；四次 GLM full 超时排除。B1 是文本检索、没有 tool loop/截图，不能同 B2/B3 当纯工具增减对照；B2/B3 同 15-turn cap，但 7 vs 12 工具，实际 calls/token/提交率不等。browser-only aggregate A@1 28.0% vs full 19.9%，full SR 56.8%，部分小模型反向受益，故不是“后台证据有害”的因果定律。A@1 要 component∧type 同时对，Evidence Recall 与 tool coverage 不能替代正确归因。 |
| 实际 owner 对读 | [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已有 outcome/trace/evidence、探索错误 vs 已得证据后的决策错误、deterministic first-loss 和 evaluator identity，但未在同一诊断任务中明确冻结 **用户可见症状→后台原因** 的两侧证据身份与合成验收。若长期设计要从 GUI 故障到 backend RCA，最窄增量是：先固定同一失败事件的前端/后台 snapshot、fault oracle 与工具可见集，再分别记 evidence discovery、跨层 attribution、submission 和总工具成本；不能用单一最终答案或‘工具越多越好’推断。Ch81 拥有实际执行/重试，不是 benchmark truth owner。 |
| 边界与作者侧处置 | 建议保留为**潜在评价合同增量**，仅待非作者贡献校准和有据本窗日期后进入必要 Source Review/Books Decision；不因为新 benchmark 名称直接入书。两个开源 app、controlled injection、人工只抽样校验、单 frozen snapshot、25 场景实验及单一 reference investigation path 限制外推；19.7% 是该实验总体 A@1，不是生产 RCA 失败率。若非作者指出 Ch66 现段已经逐项承载 browser/backend 同事件证据身份与归因分母，则改具名 Existing 或前分母关闭，而非重复写跨模态口号。 |

日期：receipt 中 v1 Updated `2026-04-28T00:41:55Z` 可辅助官方公告槽＋连续 ID 的有界归属，但不是首次公开的单点日志；本文不因该字段直接冻结候选。
