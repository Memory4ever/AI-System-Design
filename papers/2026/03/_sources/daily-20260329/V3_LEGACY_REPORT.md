# Daily Research — 2026-03-29

**Research Date:** 2026-03-29

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-28 09:00:00 ～ 2026-03-29 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=0/0/0；denominator=0、pre-denominator closures=0。exact-v1 Review complete=0、blocked=0；Integrate 建议=0。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-29 |
| Window End | 2026-03-29 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260329-AUTHOR-0 |
| Denominator Frozen At | 2026-09-02T16:07:11.473626+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-28T09:00:00+08:00 | 2026-03-29T09:00:00+08:00 | 2026-09-02T16:07:11.473626+08:00 | official-schedule recovery receipt + 0/0 title/abstract replay + official abs/HTML/PDF exact-v1 | no_hit | 0 | — | pages=100; prefixes=00..99; final_cursor=end; registered=0; screened=0; retained=0; closure=0 | 2026-03-29T01:00:00+00:00 | screening-ledger-final.json#sha256=298ef2b0a8cd350a27e476e86a9fccdb378304b21595b3d4a08c3c9c537b1324; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260329:start -->作者侧已逐项筛选全部 0 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260329:end -->

### Fresh-context Audit

<!-- fresh-context-audit:lane-c:start -->
非作者审计已重放 0/0 条 title+abstract：作者 retained 0 项均保留，0 个 false-negative family 已完成 exact-v1 Source Review，0 个 recall challenge 被逐项驳回，0 个 withdrawn 只保留 identity/status；reconciled denominator 为 0；Books queue 中 0 个 `Integrate` 被降为 `No Change — Existing Coverage`，0 个 owner 已重绑。本审计已重建分母、Review 与 Books comparison，但不写 Books；Coverage/Evidence/Books Gate 继续保持 Open，等待 root final reconciliation。收据：`papers/2026/03/_sources/daily-20260329/fresh-context-audit-receipt.json`、`fresh-context-retained-evidence-audit.json`、`fresh-context-books-audit.json`。
<!-- fresh-context-audit:lane-c:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


### Source Reviews



## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |




## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |




## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260329-COVERAGE | fresh-context:march-lane-c-reviewer | coverage | fresh-context-audit:lane-c | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260329-EVIDENCE | fresh-context:march-lane-c-reviewer | evidence | fresh-context-audit:lane-c;validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260329-SELECTION | fresh-context:march-lane-c-reviewer | deep_analysis_selection | fresh-context-audit:lane-c;validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260329-BOOKS | fresh-context:march-lane-c-reviewer | books | fresh-context-audit:lane-c;validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260329/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

当前 retained Review 可复用，但 denominator 的 full-row fresh-context 反证发现 false-negative；按 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 重做全量语义复核后，再重算 Selection 与 Books disposition。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- Books Decision 已闭合，本日无需修改 Books。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 未解决语义 finding=4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）；blocked / unverified / disputed 仍为 0。
- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；它们不是本次流程 pending。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Open`
- Evidence: `Open`
- Books: `Open`
- unresolved findings: 4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）
