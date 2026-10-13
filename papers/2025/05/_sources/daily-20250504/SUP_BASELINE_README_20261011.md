# Daily Research — 2025-05-04

**Research Date:** 2025-05-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2025-05-03 09:00:00 ～ 2025-05-04 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。fresh-context reviewer 已完成全量语义复核、exact-v1 证据验收与 post-write Books audit。

## Executive Summary

官方 announcement owner 分母为 0；全量逐行读取 title+abstract 后保留 0 个 family，关闭 0 条，withdrawn/removed exact-v1 为 0，blocked evidence 为 0。未使用 Weekly 作 discovery、筛选、评分、Review 或 Books 证据。7 个初始 closure false negative 已纠正；所有 current-content comparison 与 Gate 已由 fresh-context reviewer 验收。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2025-05-04 |
| Window End | 2025-05-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20250504-5803914305a5d8f5585f |
| Denominator Frozen At | 2026-09-03T21:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2025-05-03T09:00:00+08:00 | 2025-05-04T09:00:00+08:00 | 2026-09-03T21:15:00+08:00 | official announcement owner recovery; owner_report_date=2025-05-04 | no_hit | 0 | — | pages=1; final_cursor=end; rows=0 | 2025-05-04T09:00:00+08:00 | coverage:SRC-ARXIV:20250504 | — |

<!-- coverage:SRC-ARXIV:20250504:start -->owner inventory SHA prefix `5803914305a5d8f5585f`；semantic ledger SHA prefix `7b32fdff142c1914eaa7`；算术 `0 = 0 retained + 0 closures`。<!-- coverage:SRC-ARXIV:20250504:end -->

### Coverage Limitations

注册表晚于历史窗口；本次只对可复现的官方 announcement owner inventory 作完整论文 recall。组织来源若无历史枚举证据，不伪造 retroactive no-hit。

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

只有 Candidate Ledger 明确标为 `yes` 的数字主张进入下表；其余论文数字不被提升为日报结论。

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

Books Gate 已通过：5 项既有语义绑定经 exact-v1 与目标/相邻正文复核后记为 `verified_existing_writeback`，不重复插入。

## 7. Semantic Audit

fresh-context audit 独立于作者重建；author recheck 不作为 Gate 证据。

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20250504-COVERAGE | fresh-context:daily_2025may_fresh_audit | coverage | coverage:SRC-ARXIV:20250504 | — | 696 title+abstract identities re-read without sampling; seven false negatives moved to their owner-day retained sets and zero-hit owner ledgers were rehashed | passed |
| SA-20250504-EVIDENCE | fresh-context:daily_2025may_fresh_audit | evidence | validator:review-completion-v1 | — | all retained routes were checked against primary packets for method, evaluation, limitation, artifact and withdrawal facets | passed |
| SA-20250504-SELECTION | fresh-context:daily_2025may_fresh_audit | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | every eligible family has a day-specific selected or non-selected disposition within the three-item narrative budget | passed |
| SA-20250504-BOOKS | fresh-context:daily_2025may_fresh_audit | books | validator:books-comparison-v1 | — | five exact-v1 sources and current target/adjacent flows were rechecked in date order; existing bindings were marked verified_existing_writeback and line-one placeholders removed | passed |

## 8. Ignored Noise

0 条 pre-denominator closure 均在 `semantic-screening-ledger-v2.1.json.gz` 中保留完整 identity、title、abstract evidence、closure class 与 family-specific reason；没有评分，也没有冒充全文 Review。

## 9. Recommended Action

保持当前 owner 与 Books 语义绑定；后续只在新 primary evidence 改变长期机制边界时重新打开 Books Decision。

## 10. Repository Changes

重建 05/01–04 Daily、owner-day ledger、exact-v1 manifests、no-hit receipts、Books queue 与 fresh-context audit receipt；既有 Books 正文经验证合格，未重复修改。未 stage/commit/push。

## 11. Open Questions

- None.

## 12. Sources

## 13. Final Status

- Completion Status = `Complete`
- Coverage = `Closed`
- Evidence = `Passed`
- Books = `Passed`
- unresolved findings = 0
