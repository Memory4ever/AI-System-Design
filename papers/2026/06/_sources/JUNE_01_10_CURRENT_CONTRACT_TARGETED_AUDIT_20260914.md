# 2026-06-01～10 当前合同定点复核

## 目的与复用边界

本轮不把已有可核实的 title+abstract 语义筛选、exact-v1 Evidence 和 Books 正文锚点从零重做。只有三类项目重开：每日厂商源的历史覆盖误判、日期归属/撤回变化，以及足以击穿既有准入的 false-positive / false-negative 反例。原有 identity、版本和 claim 未变化的 Source Review 按 `docs/RESEARCH_CONTRACT.md` 复用。

## 厂商源增量

逐源回放见 [`daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md`](daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md)，各日报来源行显式引用该共享证据。新增或恢复的 owner candidate 为：06-01 MiniMax M3；06-03～06-06 和 06-10 的 Kimi Code release families；06-10 MaxProof。OpenAI Dreaming 只披露 2026-06-04 日期，无法跨 09:00 截点唯一归属，作为隔离日期缺口同时记录于 06-04、06-05，但不进入任何一天的候选分母。

## 定点 false-positive 审计

对每个非空 arXiv 日期抽取低/中/高位置或边界类型，重新读取现有 title+abstract 判断、exact-v1 机制摘要和 Books disposition，而不是只检查关键词。抽样覆盖如下：

| 日期 | 复核家族 | 反例问题 | 结论 |
| --- | --- | --- | --- |
| 06-02 | 2606.00005、2606.02304、2606.02540 | 是否只是多 Agent/skill 名称，未改变协作证据或 skill lifecycle | 保留；分别明确 claim/evidence、typed evolution unit、reuse/revoke/sandbox contract |
| 06-03 | Kimi Code 0.7/0.8、2606.03928、2606.03910 | release 是否越权成可靠性证据；KV 工作是否只是局部 benchmark | Kimi 仅作 interface evidence；两项 KV 均改变 eviction/placement control，保留 |
| 06-04 | Kimi Code 0.9、2606.05037、2606.04874 | 协议/benchmark 是否仅产品或排行榜信息 | Kimi 限于 ACP/side-channel 接口；其余两项给出 recovery/evaluation contract，保留 |
| 06-05 | Kimi Code 0.10、2606.05679、2606.06399 | goal queue 是否只是版本噪声；CollabSim 是否足以进入 Books | Kimi 5 分标准审阅；data-flow policy 保留；CollabSim 仅报告，不进入长期正文 |
| 06-08 | 2606.06515、2606.06529、2606.07404 | 专用 photonic accelerator 或安全实验是否缺跨系统意义 | 前者形成 execution-plan co-design 边界，后二者改变 control evaluation / training-state migration，保留 |
| 06-09 | 2606.07632、2606.08381、2606.09411 | 生命周期成本、无 ground-truth audit、steganography 是否只是单项评测 | 三项均改变 cost/evaluation/security contract；边界已限制在披露 workload，保留 |
| 06-10 | Kimi Code 0.12、2606.10487、2606.10062 | swarm 名称或 probe/memory benchmark 是否被过度准入 | Kimi 只作 interface evidence；后二者分别改变 learned sensor/reference monitor 与 deployment-memory lineage，保留 |

未发现上述样本中需要从 Candidate 降回 pre-denominator closure 的项目。该结论不能替代已有全表 ledger；它只验证本次合同变更未使旧分母出现共享型准入漂移。

## false-negative 与日期对账

旧 closure 的共享型反例已由各日现有非作者审计完成；本轮只检查新线索。厂商页恢复 7 个 Source Family，均由当前 Books 命题覆盖；MaxProof 精确对应 `TRAIN-GRPO` 的 verifier specification、independent oracle 与 authority separation。06-07 历史 submission-date packet 的 23 项由 first-public receipt 全部迁往 06-09，不在 06-07 重复计数。withdrawn family 2606.04101 与 2606.24369 保持排除，无正向 Books 采用链。

## 当前状态

- 06-01～09：报告侧 Coverage、Evidence 与 Books Decision 闭合；06-04/05 仅保留同一 Dreaming 日期缺口。
- 06-10：报告、Evidence 与 Books Decision 闭合；Kimi Code 和 MaxProof 均为 Existing，不需要共享 Books 写回。
- 本轮没有重算未受影响的旧分数，也没有把 release notes 外推为机制可靠性或性能结论。
