# 2026-05-17 V3 Fresh Non-author Final Review

## 审核结论

通过。严格窗口为 `[2026-05-16T09:00:00+08:00, 2026-05-17T09:00:00+08:00)`；本终审没有扩展来源、窗口或候选，也没有编辑 Books。

本窗终态为：14 个 Daily 来源已处理，0 个可确认落窗的独立事件，Candidate Denominator=0，Evidence Review=0，withdrawn=0，Books 写回=0。Meta GIM 的日期冲突被隔离为终态保留项，不支持本窗候选、Books 或“互联网无遗漏”断言。

## 1. 来源与窗口

- 当前 `docs/RESEARCH_SOURCES.md` 的 Daily 清单恰好包含 14 个唯一 Source ID；README 逐行覆盖相同 14 项。
- `non-arxiv-source-coverage-v3.json` 的 13 个 boundary key 与清单中除 `SRC-ARXIV` 外的 13 项完全一致，记录的相邻事件均未形成可确认落窗事件。
- `arxiv-owner-replay-20260903/20260517/arxiv-owner-receipt.json` 记录 `raw_identity_count=0`、`official_oai_direct_count=0`、`revision_recovery_count=0`、`semantic_review_pending_count=0`。旧 submission/DataCite 混合窗口的 identity 不是本窗新增公告。
- README 的来源表给出实际入口、相邻记录或零命中边界；“已检查”只限注册入口和严格窗口，不被解释为互联网全量保证。

## 2. 旧 279 项与 31 个候选

`screening-ledger-independent-final.json` 中存在 279 个互异 identity，其中旧 `retained` 为 31、旧 closure 为 248。终审以 ID 集合独立重算，而不是接受作者汇总：

| 后续记录 | 279 项交集 | 其中旧候选 | 核验边界 |
| --- | ---: | ---: | --- |
| 2026-05-19 owner replay | 252 | 28 | receipt 逐 ID 相交 |
| 2026-05-20 owner replay | 11 | 1 | receipt 逐 ID 相交 |
| 2026-05-21 owner replay | 3 | 0 | receipt 逐 ID 相交 |
| 2026-05-25 owner replay | 1 | 1 | receipt 逐 ID 相交 |
| 2026-05-26 owner replay | 1 | 1 | receipt 逐 ID 相交 |
| 2026-05-29 owner replay | 6 | 0 | receipt 逐 ID 相交 |
| `2606.00053` | 1 | 0 | 06-02 DataCite boundary-created 记录；不冒充官方公开日 |
| `2606.12435`～`2606.12438` | 4 | 0 | 06-12 provisional raw bucket；official listing receipt 未捕获 |
| **合计** | **279** | **31** | **无重复、无未调和的 05-17 identity** |

前六个 May receipt 的交集互不重复，合计 274；剩余恰好为上述 5 个 `2606.*` identity。后 5 项的 identifier month 与后续恢复记录足以将其排除出 05-17，但不足以宣称 06-02/06-12 是已确认的官方首次公开日。README 与 owner reconciliation 已据此收窄表述。

旧 31 个候选全部包含在前六个 May receipt 中，分布为 28+1+1+1=31；没有旧候选落入 5 个六月边界项。因此旧评分、Evidence 或 Books 结论均不属于 05-17。

## 3. Charon 与 GIM 的日期挑战

### Charon

05-16 的 V3 原始记录保存 ByteDance Seed `ArticleMeta.PublishDate=1778860800000`，换算为 2026-05-16T00:00:00+08:00，落入 05-16 日报窗口且早于 05-17 窗口起点。`arXiv:2605.17164v1` 的提交时间为 2026-05-17T05:28:22+08:00，只是同 family 的后续论文证据。05-17 不重复拥有、评分或执行 Books Decision。

### Meta GIM

Meta publication listing 显示 2026-05-17，当前官方详情页显示 2026-05-18；arXiv submission history 给出 v1 为 2026-05-18T17:09:50Z，即 2026-05-19T01:09:50+08:00。仅有日期的 05-17 listing 无法证明其首次公开落在当日 00:00～09:00，后两项证据又在窗后，因此不能把 GIM 作为 05-17 的确定候选。

该冲突已经按合同隔离：不用于正面证据、不进入 Books、不支持零遗漏或评价结论；定点重开条件是 Meta 提供可验证且落入本窗的首次公开时刻。现有不确定性不是仍可由本次执行解决的待办。

## 4. Books 与工作树边界

`root-books-writeback-queue-v3.json` 的 `candidate_count=0` 且 `items=[]`，与 README 的零候选、零 Books 写回一致。本终审未编辑 Books，也未复用旧 V2.1 的 31 项 Books 处置。

旧 `candidate-ids.txt` 是 V2.1 作者阶段的非规范辅助文件，只有 30 行；后续独立恢复使 canonical 旧 ledger 的 retained 变为 31。V3 终态计数以 279 项 canonical ledger 和本次集合调和为准，不把该旧辅助文件当成当前候选清单。

## 5. 对抗复核与修正

终审主动挑战了“279 项都已经获得官方 owner 日”这一可能过度声明。结果确认 274 项具有后续 May replay 记录，5 个六月 identity 只有后续恢复桶，其中 06-12 audit 还明确写着 official listing receipt 未捕获。因此修正 README 与 owner reconciliation：本日报只断言 279/279 不属于 05-17；不替六月报告宣称精确 owner 已闭合。

修正后没有发现仍会改变本窗零事件、零候选或空 Books 队列的反例。由于当前任务本身是 root 指派的独立 fresh-context 终审，未再启动嵌套或跨模型复核。

## 6. 最终 Gate

- Coverage：安全终态。14/14 到期来源有明确结果；GIM 冲突隔离。
- Candidate：通过。0 个可确认落窗 family；旧 279/31 不属于本窗。
- Evidence：通过。候选为 0，无待审阅项。
- Books：通过。队列为空，无写回需求。
- Semantic：通过。过度 owner 表述已修正；无剩余可执行工作。

