# 2026-06-05 V3 recovery blockers

> **2026-09-11 update：** 下方 Books trace-to-body 队列已被非作者 final fresh audit 覆盖。最终分母为 71 Candidate / 635 Close；旧 8 项 Integrate 全部为 `已有覆盖`，new Integrate = 0，正文缺口 = 0。当前唯一报告侧 blocker 是最终 71 项 Candidate 的 Evidence 与逐项 Books Decision。

## Denominator

可读基线为 706 raw / 68 prior / 638 closure proposals。502 项共用 incremental closure 理由被反例击穿后已逐题重审，其余 136 项也完成 title-first、边界项完整摘要复核。权威分母冻结为 Candidate 76 / Close 630：old prior 保留 52、关闭 16；old closure 恢复 24、维持关闭 614。AppAgent-Claw（2606.05171）、LANTERN（2606.05182）、state commitment learning（2606.05201）与 DeployBench（2606.05238）恢复；long-horizon credit（2606.05263）因仍是局部 RL credit 方法而关闭。逐项依据与 FP/FN 抽查见 V3_SCREENING_LEDGER.md。当前 blocker 转为 24 个新恢复 Candidate 的评分/Evidence/Books Decision，以及下列 surviving Integrate 的 Books trace-to-body。

## Books write queue

当前八项旧 Integrate 均只找到 trace，没有独立 semantic-body-binding：

| Source Family ID | Target file | Trace anchor | 正文队列 |
| --- | --- | --- | --- |
| SF-2026-ARXIV-2606-05304 | books/part-07-agent/82-multi-agent.md | daily-books-trace:SF-2026-ARXIV-2606-05304（约 870 行） | 补写 action-state communication 的消息语义/拓扑边界 |
| SF-2026-ARXIV-2606-05679 | books/part-06-ai-infrastructure/72-security.md | daily-books-trace:SF-2026-ARXIV-2606-05679（约 2164 行） | 补写 agent data-flow policy 的控制点与执行边界 |
| SF-2026-ARXIV-2606-05933 | books/part-05-inference-system/56-inference-scheduling.md | daily-books-trace:SF-2026-ARXIV-2606-05933（约 1267 行） | 补写 sliding-window/SLO 调度机制与适用边界 |
| SF-2026-ARXIV-2606-05951 | books/part-04-training-system/36-distributed-training.md | daily-books-trace:SF-2026-ARXIV-2606-05951（约 1535 行） | 补写 symmetric memory/device-initiated communication 的系统边界 |
| SF-2026-ARXIV-2606-06090 | books/part-07-agent/77-memory.md | daily-books-trace:SF-2026-ARXIV-2606-06090（约 1547 行） | 补写 memory-as-execution-state 的 owner 与恢复边界 |
| SF-2026-ARXIV-2606-06240 | books/part-07-agent/77-memory.md | daily-books-trace:SF-2026-ARXIV-2606-06240（约 1553 行） | 补写 bitemporal contradiction resolution 的时态语义 |
| SF-2026-ARXIV-2606-06256 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md | daily-books-trace:SF-2026-ARXIV-2606-06256（约 1488 行） | 补写 head-aware reuse/SegPagedAttention 的命中与失效边界 |
| SF-2026-ARXIV-2606-06453 | books/part-05-inference-system/47-pagedattention.md | daily-books-trace:SF-2026-ARXIV-2606-06453（约 247 行） | 补写 programmable sparse-attention serving 的块管理与回退边界 |

单独 trace 修正队列：SF-2026-ARXIV-2606-05304 的 Daily 2026-06-04 改为 2026-06-05；其余七项日期正确。正文队列只在候选 survives 当前分母后消费。
