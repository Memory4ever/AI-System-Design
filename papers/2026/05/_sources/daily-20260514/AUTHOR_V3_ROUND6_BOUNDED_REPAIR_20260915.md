# 2026-05-14 V3 Round6 Bounded Repair

**返修者：** `/root/may14_round6_bounded_repair`

**身份：** author repair；不能替代 fresh non-author final review

**状态：** Ongoing — denominator/evidence/comparison repaired; root writeback and fresh review pending

## 边界

- 时间窗保持 `[2026-05-13T09:00:00+08:00, 2026-05-14T09:00:00+08:00)`。
- 未扩来源、未重新抓取或重扫 714 条 active inventory。
- 只处理终审指定的 7 个 challenged family；额外只修复同一审计已举例的 `2605.12729` closure reason 截断。
- 作者 lane 未编辑 Books；新的 4 个 Integrate 已随后由 root 写入对应章节，等待 fresh non-author review。

## 重裁结果

| family | 结论 | 核心依据 |
| --- | --- | --- |
| `2605.12652` | Retain；7；Deep；`TRAIN-GRPO`；Integrate pending | 同组成功/失败 rollout 共同构造 teacher context，改变 group evidence→token supervision 的控制流 |
| `2605.12667` | Retain；8；Deep；`TRAIN-GRPO`；Integrate pending | ordinal threshold decomposition 改变 noisy discrete reward 的 advantage estimator |
| `2605.12714` | Pre-denominator closure | 选择/剪枝只在有限 embedder/base-LLM/task/budget 上显示相关性，未形成长期 execution/release contract |
| `2605.12718` | Retain；6；Standard；`AGENT-MEMORY`；No Change | typed graph belief 与 adjudication 有长期价值，但 Ch77 已具体承载 competing hypotheses/evidence/falsification/manual fallback |
| `2605.12741` | Retain；7；Deep；`TRAIN-SFT`；Integrate pending | failure trace→reflection→persistent playbook→token target 与 rare-success→GRPO handoff |
| `2605.12908` | Retain；7；Deep；`TRAIN-RLHF`；Integrate pending | feature elicitation/off-target preservation 修正 W2S 的单一 capacity-mismatch 解释 |
| `2605.13695` | Demote to pre-denominator closure | 单 judge、单 prompt、350 pair benchmark、单 seed、未校准、关键 ablation 缺失且约 47× output-token cost |

`2605.12729` 仍关闭，但理由已恢复为完整 family-specific 结论：它是 NetOps/AIOps survey，无新机制、artifact 或 evaluation result，观点与现有 workflow/security/monitoring contract 重复。

`screening-outcomes-v3.json` 中其余被 240 字符切断的 closure reason 没有重新审论文或改变 admission，而是从同一 714-ID active owner receipt 机械恢复已有完整 title+abstract decision：564 条恢复原文，另有 3 条使用本轮新裁决。恢复后 586 条 current closure 不再存在截断尾部；这项记录修复不等于新增 Full Source Review。

## 当前唯一总账

```text
714 raw identities
= 128 retained
+ 586 pre-denominator closures
+   0 withdrawn

128 arXiv + 2 official = 130 Candidate Denominator
128 exact-v1 reviews = 124 deep + 4 standard
Books = 83 Applied + 4 Pending + 41 No Change
```

`round6-current-reconciliation.json` 是当前唯一 reconciliation；`v3-author-recert.json` 的 79 与 `v3-bounded-semantic-repair.json` 的 120 已标记 superseded，不能作为并行总账。

## Books 比较

- `2605.12718` 对读的是 Ch77 首个 `Review notes` 前的具体命题 “Belief State：先保存竞争假设，再决定事实”，不是主题相似；因此 No Change。
- 其余四项都指出现有正文仍缺少的命题级 delta，位于 `root-books-writeback-queue-round6.json`。写入建议与证据边界见 `ROOT_BOOKS_SYNTHESIS_ROUND6_20260915.md`。

## 未完成 Gate

1. Root 尚未按 owner/date 顺序写回四项 Books 增量。
2. 写回后需要另一 fresh non-author reviewer 只复核 7 个 challenged family、总账、binding 与 Final Status。
3. 因此作者只能登记 `Ongoing`，不得签署 Complete。
