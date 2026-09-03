# 2026-06 / 2026-07 Daily 最新合同复核

本账本只接受非空 evidence file。它不会因为旧报告写有 `Complete`、validator 通过或文件名存在，就把证据视为已经闭合。

## 结论

| Month | Reports | Candidates | Review rows | Integrate dispositions | Ready for fresh-context audit |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2026-06 | 30 | 1484 | 1484 | 724 | 10 |
| 2026-07 | 31 | 474 | 474 | 178 | 9 |

当前两个月都不能沿用旧 `Complete`：官方 arXiv availability、exact-v1 Atom 与 DataCite DOI `created` 已恢复 1,960 个未撤稿候选的 first-public owner，其中 1,060 个可确认需要跨日报移动，2 个 identifier-month / DOI-created 冲突仍需 exact announcement 材料；部分报告还缺失 raw inventory、逐 identity closure 或 exact-version primary material。6 月的零字节恢复空壳不计入任何 Gate。2026-08-25 才生效的新增来源不倒推为 6～7 月 Required Daily receipt；它们只按 Source Delta Audit 规则检查是否发现真实 in-window family。

## Findings

- `per_identity_closure_missing`: 42 reports
- `zero_byte_files_ignored`: 19 reports

## Recovery boundary

- `ledger.json` 保存逐日报告、来源缺口、每日报告可引用的非空/空文件计数和候选/Review 算术。共享月级 packet 可被多个日期引用，因此 README 不汇总文件计数，以免重复计数。
- `materials-request.tsv` 仅列 2 个 identifier month 与 DOI-created Eastern month 冲突的 exact announcement 证明；普通 owner move、分母重放和零字节恢复都不得转嫁给用户。
- 已有候选、Review 与 Integrate 判断暂时保留为 provenance，不作为最新合同已通过结论；owner 修复后必须重新运行 denominator、fresh-context false-positive/false-negative audit 与 Books comparison。
- 本任务不直接修改 Books；旧 `Integrate` 已进入月内 `BOOKS_WRITEBACK_QUEUE_latest-contract.json`，但全部冻结为 `frozen_pending_upstream_reconciliation`，只能由单一 owner 在上游 Gate 与 fresh-context Books comparison 通过后按日期合并。
