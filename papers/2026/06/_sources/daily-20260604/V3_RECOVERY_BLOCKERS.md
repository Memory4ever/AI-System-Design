# 2026-06-04 V3 recovery blockers

> **2026-09-11 post-write update：** 最终分母为 64 Candidate / 511 Close：UltraEP（2606.04101）因官方 v1/v2/v3 全部 withdrawn 而去准入；2606.04071/04929 为 `已有覆盖`，2606.04145 EvalStop 已真实写入 `TRAIN-RLHF`/Ch31 并通过非作者 post-write audit。UltraEP Books residue 为 0；2606.04071 的旧 adoption trace 已精确删除；当前 blocker 为 0。

## Denominator

可读基线为 575 raw / 41 prior / 534 closure proposals。435 项共用的 incremental closure 理由被反例击穿后已全量重审，其余 99 项按 embodied / benchmark / theory / vertical 逐项复核，41 prior 也重新检查。

首轮 Candidate 210 / Close 365 被严格复核推翻：该轮仍把大模型对象或章节可映射性误当作贡献准入。作者侧二次 checkpoint 为 Candidate 73 / Close 502：旧 534 closure proposals 中只恢复 38 项，旧 41 prior 中关闭 6 项；首轮另有 137 项 Candidate 因缺少跨 workload 的长期 state/data/control、execution/evaluation/release contract 而撤回。非作者复核再关闭 9 项，最终 authority 为 Candidate 64 / Close 511；逐项和逐族理由及 10+10 FP/FN 抽查见 V3_SCREENING_LEDGER.md。

## Books write queue

当前 Books 只读快照：

| Source Family ID | Target | Body anchor | Trace anchor | 队列 |
| --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-04929 | books/part-06-ai-infrastructure/72-security.md | semantic-body-binding:SF-2026-ARXIV-2606-04929（约 1379 行） | daily-books-trace:SF-2026-ARXIV-2606-04929（约 2158 行） | 正文已存在；只复验 exact-v1 边界 |
| SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | books/part-07-agent/77-memory.md + books/part-06-ai-infrastructure/72-security.md | Ch77 `Stateless API 仍可能承载跨调用的 Implicit Memory` + Ch72 `多 Agent Cascade 需要跨 Channel 的 Influence Graph` | 无 | `已有覆盖`；旧 adoption trace 已删除，不新增正文 |
| SF-EVALSTOP | books/part-04-training-system/31-rlhf.md | `训练停止不能只看 Training Loss 或 Reward Model Score`；`semantic-body-binding:SF-EVALSTOP` | daily-books-trace:SF-EVALSTOP | 已写入并通过非作者 post-write audit |

此队列只在候选 survives 当前分母后消费；若撤回 Integrate，则清除相应采用链而非补写。
