# Daily Research — 2026-06-19

**Research Date:** 2026-06-19

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-18 09:00:00 ～ 2026-06-19 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
Beijing window `[2026-06-18 09:00, 2026-06-19 09:00)` contains 556 registered identities. Full 556/556 title+abstract screening freezes 68 durable families and 488 family-specific closures. All 68 exact-v1 full texts have source-specific Method/Evaluation/limitation/artifact receipts and exact ten-field benchmark contracts; the complete selection frontier was rerun after Evidence passed. Root wrote all 56 net deltas into 23 unique owners, and this lane independently verified 56 exact owner-body/Review-note pairs plus 12 absent No Change markers with zero unresolved finding.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-19 |
| Window End | 2026-06-19 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-19:c24d08496777b43b |
| Denominator Frozen At | 2026-08-30T00:35:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-18T09:00:00+08:00 | 2026-06-19T09:00:00+08:00 | 2026-08-30T00:35:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 590 | SF-2026-ARXIV-2606-19376;SF-2026-ARXIV-2606-19380;SF-2026-ARXIV-2606-19382;SF-2026-ARXIV-2606-19386;SF-2026-ARXIV-2606-19390;SF-2026-ARXIV-2606-19409;SF-2026-ARXIV-2606-19464;SF-2026-ARXIV-2606-19535;SF-2026-ARXIV-2606-19544;SF-2026-ARXIV-2606-19559;SF-2026-ARXIV-2606-19595;SF-2026-ARXIV-2606-19613;SF-2026-ARXIV-2606-19667;SF-2026-ARXIV-2606-19692;SF-2026-ARXIV-2606-19704;SF-2026-ARXIV-2606-19714;SF-2026-ARXIV-2606-19719;SF-2026-ARXIV-2606-19746;SF-2026-ARXIV-2606-19753;SF-2026-ARXIV-2606-19755;SF-2026-ARXIV-2606-19758;SF-2026-ARXIV-2606-19769;SF-2026-ARXIV-2606-19795;SF-2026-ARXIV-2606-19803;SF-2026-ARXIV-2606-19808;SF-2026-ARXIV-2606-19847;SF-2026-ARXIV-2606-19849;SF-2026-ARXIV-2606-19868;SF-2026-ARXIV-2606-19887;SF-2026-ARXIV-2606-19898;SF-2026-ARXIV-2606-19899;SF-2026-ARXIV-2606-19911;SF-2026-ARXIV-2606-19989;SF-2026-ARXIV-2606-19992;SF-2026-ARXIV-2606-19998;SF-2026-ARXIV-2606-20002;SF-2026-ARXIV-2606-20005;SF-2026-ARXIV-2606-20023;SF-2026-ARXIV-2606-20047;SF-2026-ARXIV-2606-20113;SF-2026-ARXIV-2606-20122;SF-2026-ARXIV-2606-20128;SF-2026-ARXIV-2606-20158;SF-2026-ARXIV-2606-20235;SF-2026-ARXIV-2606-20243;SF-2026-ARXIV-2606-20245;SF-2026-ARXIV-2606-20254;SF-2026-ARXIV-2606-20318;SF-2026-ARXIV-2606-20363;SF-2026-ARXIV-2606-20374;SF-2026-ARXIV-2606-20381;SF-2026-ARXIV-2606-20408;SF-2026-ARXIV-2606-20470;SF-2026-ARXIV-2606-20474;SF-2026-ARXIV-2606-20475;SF-2026-ARXIV-2606-20487;SF-2026-ARXIV-2606-20493;SF-2026-ARXIV-2606-20502;SF-2026-ARXIV-2606-20510;SF-2026-ARXIV-2606-20512;SF-2026-ARXIV-2606-20520;SF-2026-ARXIV-2606-20529;SF-2026-ARXIV-2606-20536;SF-2026-ARXIV-2606-20537;SF-2026-ARXIV-2606-20545;SF-2026-ARXIV-2606-20553;SF-2026-ARXIV-2606-20562 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260619/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260619; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260619 |
<!-- coverage:SRC-ARXIV:20260619:start -->
All 377 Core, 69 keyword-routed and 110 route-negative identities were screened. Frozen arithmetic: `556 = 68 retained + 488 closures`; keyword routing was recall-only.
<!-- coverage:SRC-ARXIV:20260619:end -->


<!-- latest-contract-reopen:2026-06-19:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-19:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **590** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **67** 条是旧报告 retained provenance，**523** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-19376 | arXiv:2606.19376v1 | paper-v1:2606.19376 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19376 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19376 | yes |
| SF-2026-ARXIV-2606-19380 | arXiv:2606.19380v1 | paper-v1:2606.19380 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19380 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-19380 | yes |
| SF-2026-ARXIV-2606-19382 | arXiv:2606.19382v1 | paper-v1:2606.19382 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19382 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19382 | yes |
| SF-2026-ARXIV-2606-19386 | arXiv:2606.19386v1 | paper-v1:2606.19386 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19386 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-19386 | yes |
| SF-2026-ARXIV-2606-19390 | arXiv:2606.19390v1 | paper-v1:2606.19390 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19390 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-19390 | yes |
| SF-2026-ARXIV-2606-19409 | arXiv:2606.19409v1 | paper-v1:2606.19409 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19409 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19409 | yes |
| SF-2026-ARXIV-2606-19464 | arXiv:2606.19464v1 | paper-v1:2606.19464 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19464 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19464 | yes |
| SF-2026-ARXIV-2606-19535 | arXiv:2606.19535v1 | paper-v1:2606.19535 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19535 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-19535 | yes |
| SF-2026-ARXIV-2606-19544 | arXiv:2606.19544v1 | paper-v1:2606.19544 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19544 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19544 | yes |
| SF-2026-ARXIV-2606-19559 | arXiv:2606.19559v1 | paper-v1:2606.19559 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19559 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19559 | yes |
| SF-2026-ARXIV-2606-19595 | arXiv:2606.19595v1 | paper-v1:2606.19595 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19595 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19595 | yes |
| SF-2026-ARXIV-2606-19613 | arXiv:2606.19613v1 | paper-v1:2606.19613 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19613 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-19613 | yes |
| SF-2026-ARXIV-2606-19667 | arXiv:2606.19667v1 | paper-v1:2606.19667 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19667 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-19667 | yes |
| SF-2026-ARXIV-2606-19692 | arXiv:2606.19692v1 | paper-v1:2606.19692 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19692 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-19692 | yes |
| SF-2026-ARXIV-2606-19704 | arXiv:2606.19704v1 | paper-v1:2606.19704 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19704 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-19704 | yes |
| SF-2026-ARXIV-2606-19714 | arXiv:2606.19714v1 | paper-v1:2606.19714 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19714 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-19714 | yes |
| SF-2026-ARXIV-2606-19719 | arXiv:2606.19719v1 | paper-v1:2606.19719 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19719 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-19719 | yes |
| SF-2026-ARXIV-2606-19746 | arXiv:2606.19746v1 | paper-v1:2606.19746 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19746 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-19746 | yes |
| SF-2026-ARXIV-2606-19753 | arXiv:2606.19753v1 | paper-v1:2606.19753 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19753 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19753 | yes |
| SF-2026-ARXIV-2606-19755 | arXiv:2606.19755v1 | paper-v1:2606.19755 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19755 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-19755 | yes |
| SF-2026-ARXIV-2606-19758 | arXiv:2606.19758v1 | paper-v1:2606.19758 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19758 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-19758 | yes |
| SF-2026-ARXIV-2606-19769 | arXiv:2606.19769v1 | paper-v1:2606.19769 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19769 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-19769 | yes |
| SF-2026-ARXIV-2606-19795 | arXiv:2606.19795v1 | paper-v1:2606.19795 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19795 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-19795 | yes |
| SF-2026-ARXIV-2606-19803 | arXiv:2606.19803v1 | paper-v1:2606.19803 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19803 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-19803 | yes |
| SF-2026-ARXIV-2606-19808 | arXiv:2606.19808v1 | paper-v1:2606.19808 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19808 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-19808 | yes |
| SF-2026-ARXIV-2606-19847 | arXiv:2606.19847v1 | paper-v1:2606.19847 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19847 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-19847 | yes |
| SF-2026-ARXIV-2606-19849 | arXiv:2606.19849v1 | paper-v1:2606.19849 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19849 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-19849 | yes |
| SF-2026-ARXIV-2606-19868 | arXiv:2606.19868v1 | paper-v1:2606.19868 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19868 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19868 | yes |
| SF-2026-ARXIV-2606-19887 | arXiv:2606.19887v1 | paper-v1:2606.19887 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19887 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19887 | yes |
| SF-2026-ARXIV-2606-19898 | arXiv:2606.19898v1 | paper-v1:2606.19898 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19898 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-19898 | yes |
| SF-2026-ARXIV-2606-19899 | arXiv:2606.19899v1 | paper-v1:2606.19899 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19899 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19899 | yes |
| SF-2026-ARXIV-2606-19911 | arXiv:2606.19911v1 | paper-v1:2606.19911 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19911 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-19911 | yes |
| SF-2026-ARXIV-2606-19989 | arXiv:2606.19989v1 | paper-v1:2606.19989 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19989 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-19989 | yes |
| SF-2026-ARXIV-2606-19992 | arXiv:2606.19992v1 | paper-v1:2606.19992 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19992 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2606-19992 | yes |
| SF-2026-ARXIV-2606-19998 | arXiv:2606.19998v1 | paper-v1:2606.19998 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19998 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-19998 | yes |
| SF-2026-ARXIV-2606-20002 | arXiv:2606.20002v1 | paper-v1:2606.20002 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20002 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-20002 | yes |
| SF-2026-ARXIV-2606-20005 | arXiv:2606.20005v1 | paper-v1:2606.20005 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20005 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-20005 | yes |
| SF-2026-ARXIV-2606-20023 | arXiv:2606.20023v1 | paper-v1:2606.20023 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20023 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-20023 | yes |
| SF-2026-ARXIV-2606-20047 | arXiv:2606.20047v1 | paper-v1:2606.20047 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20047 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-20047 | yes |
| SF-2026-ARXIV-2606-20113 | arXiv:2606.20113v1 | paper-v1:2606.20113 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20113 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-20113 | yes |
| SF-2026-ARXIV-2606-20122 | arXiv:2606.20122v1 | paper-v1:2606.20122 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20122 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-20122 | yes |
| SF-2026-ARXIV-2606-20128 | arXiv:2606.20128v1 | paper-v1:2606.20128 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20128 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-20128 | yes |
| SF-2026-ARXIV-2606-20158 | arXiv:2606.20158v1 | paper-v1:2606.20158 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20158 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-20158 | yes |
| SF-2026-ARXIV-2606-20235 | arXiv:2606.20235v1 | paper-v1:2606.20235 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20235 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20235 | yes |
| SF-2026-ARXIV-2606-20243 | arXiv:2606.20243v1 | paper-v1:2606.20243 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20243 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20243 | yes |
| SF-2026-ARXIV-2606-20245 | arXiv:2606.20245v1 | paper-v1:2606.20245 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20245 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20245 | yes |
| SF-2026-ARXIV-2606-20254 | arXiv:2606.20254v1 | paper-v1:2606.20254 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20254 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-20254 | yes |
| SF-2026-ARXIV-2606-20318 | arXiv:2606.20318v1 | paper-v1:2606.20318 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20318 | self | — | new_in_window | PLATFORM-PRODUCTION | Integrate | books-review:SF-2026-ARXIV-2606-20318 | yes |
| SF-2026-ARXIV-2606-20363 | arXiv:2606.20363v1 | paper-v1:2606.20363 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20363 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-20363 | yes |
| SF-2026-ARXIV-2606-20374 | arXiv:2606.20374v1 | paper-v1:2606.20374 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20374 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2606-20374 | yes |
| SF-2026-ARXIV-2606-20381 | arXiv:2606.20381v1 | paper-v1:2606.20381 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20381 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-20381 | yes |
| SF-2026-ARXIV-2606-20408 | arXiv:2606.20408v1 | paper-v1:2606.20408 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20408 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20408 | yes |
| SF-2026-ARXIV-2606-20470 | arXiv:2606.20470v1 | paper-v1:2606.20470 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20470 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-20470 | yes |
| SF-2026-ARXIV-2606-20474 | arXiv:2606.20474v1 | paper-v1:2606.20474 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20474 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-20474 | yes |
| SF-2026-ARXIV-2606-20475 | arXiv:2606.20475v1 | paper-v1:2606.20475 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20475 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-20475 | yes |
| SF-2026-ARXIV-2606-20487 | arXiv:2606.20487v1 | paper-v1:2606.20487 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20487 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-20487 | yes |
| SF-2026-ARXIV-2606-20493 | arXiv:2606.20493v1 | paper-v1:2606.20493 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20493 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-20493 | yes |
| SF-2026-ARXIV-2606-20502 | arXiv:2606.20502v1 | paper-v1:2606.20502 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20502 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20502 | yes |
| SF-2026-ARXIV-2606-20510 | arXiv:2606.20510v1 | paper-v1:2606.20510 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20510 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-20510 | yes |
| SF-2026-ARXIV-2606-20512 | arXiv:2606.20512v1 | paper-v1:2606.20512 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20512 | self | — | new_in_window | AGENT-PROMPT | Integrate | books-review:SF-2026-ARXIV-2606-20512 | yes |
| SF-2026-ARXIV-2606-20520 | arXiv:2606.20520v1 | paper-v1:2606.20520 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20520 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-20520 | yes |
| SF-2026-ARXIV-2606-20529 | arXiv:2606.20529v1 | paper-v1:2606.20529 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20529 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-20529 | yes |
| SF-2026-ARXIV-2606-20536 | arXiv:2606.20536v1 | paper-v1:2606.20536 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20536 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-20536 | yes |
| SF-2026-ARXIV-2606-20537 | arXiv:2606.20537v1 | paper-v1:2606.20537 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20537 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-20537 | yes |
| SF-2026-ARXIV-2606-20545 | arXiv:2606.20545v1 | paper-v1:2606.20545 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20545 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-20545 | yes |
| SF-2026-ARXIV-2606-20553 | arXiv:2606.20553v1 | paper-v1:2606.20553 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20553 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-20553 | yes |
| SF-2026-ARXIV-2606-20562 | arXiv:2606.20562v1 | paper-v1:2606.20562 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20562 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-20562 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-19376 | RP-07d8cc158ffc095c | deep | arXiv:2606.19376v1 | SRC-ARXIV@arXiv:2606.19376v1 | https://arxiv.org/html/2606.19376v1 — § exact-v1 anchor: SLARouter | https://arxiv.org/html/2606.19376v1 — § exact-v1 evaluation anchor: wide range of LLM benchmarks | https://arxiv.org/html/2606.19376v1 — § exact-v1 limitation/counterevidence anchor: sparse one-sided user feedback | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19376 | complete |
| SF-2026-ARXIV-2606-19380 | RP-c1321d3e370915d9 | deep | arXiv:2606.19380v1 | SRC-ARXIV@arXiv:2606.19380v1 | arXiv:2606.19380v1 §3 setup; §4 scenarios; §5 design | arXiv:2606.19380v1 §6 Implementation and Results; Appendices | arXiv:2606.19380v1 §7 future directions; Appendix C.17 validity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19380 | complete |
| SF-2026-ARXIV-2606-19382 | RP-7cd3882895d2caf9 | deep | arXiv:2606.19382v1 | SRC-ARXIV@arXiv:2606.19382v1 | arXiv:2606.19382v1 §§3–4 DynAMO plan-then-execute scheduler | arXiv:2606.19382v1 §5 six AssetOpsBench experiments | arXiv:2606.19382v1 §6 limitations and industrial-benchmark/tool-latency scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19382 | complete |
| SF-2026-ARXIV-2606-19386 | RP-102a459d1f668462 | deep | arXiv:2606.19386v1 | SRC-ARXIV@arXiv:2606.19386v1 | arXiv:2606.19386v1 §2 Setup; §3 Δt=0 Audit and Erratum; §§4–9 cadence sweeps, scaling and transition triggers | arXiv:2606.19386v1 §4 Uniform-Cadence Sweep; §5 Measured Real Cadence; §6 burst structure; Appendix A replay/instrumentation | arXiv:2606.19386v1 §8 scaling-rule limits; §9 transition-trigger timing problem; §11 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19386 | complete |
| SF-2026-ARXIV-2606-19390 | RP-3c319344d784506a | deep | arXiv:2606.19390v1 | SRC-ARXIV@arXiv:2606.19390v1 | arXiv:2606.19390v1 PDF §§3–5 AIBOM-driven CSAF-VEX workflow and execution binding | arXiv:2606.19390v1 PDF §§6–7 reproducibility/case-study evaluation | Not Disclosed — arXiv:2606.19390v1 has no dedicated limitations section; exact-v1 counterevidence is localized at PDF limitations on dependency inventory, activation observability and advisory authority | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19390 | complete |
| SF-2026-ARXIV-2606-19409 | RP-7d7150c18958b701 | deep | arXiv:2606.19409v1 | SRC-ARXIV@arXiv:2606.19409v1 | https://arxiv.org/html/2606.19409v1 — § exact-v1 anchor: Session-Centered Runtime State | https://arxiv.org/html/2606.19409v1 — § exact-v1 evaluation anchor: audited milestones | https://arxiv.org/html/2606.19409v1 — § exact-v1 limitation/counterevidence anchor: claims are limited | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19409 | complete |
| SF-2026-ARXIV-2606-19464 | RP-9c9808c620abad7c | deep | arXiv:2606.19464v1 | SRC-ARXIV@arXiv:2606.19464v1 | https://arxiv.org/html/2606.19464v1 — § exact-v1 anchor: obligations, dispensations | https://arxiv.org/html/2606.19464v1 — § exact-v1 evaluation anchor: examples | https://arxiv.org/html/2606.19464v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19464 | complete |
| SF-2026-ARXIV-2606-19535 | RP-c928538e16521982 | deep | arXiv:2606.19535v1 | SRC-ARXIV@arXiv:2606.19535v1 | https://arxiv.org/html/2606.19535v1 — § exact-v1 anchor: platform-triggered backdoor | https://arxiv.org/html/2606.19535v1 — § exact-v1 evaluation anchor: broad range of deployment targets | https://arxiv.org/html/2606.19535v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19535 | complete |
| SF-2026-ARXIV-2606-19544 | RP-c5005845d92e5630 | deep | arXiv:2606.19544v1 | SRC-ARXIV@arXiv:2606.19544v1 | https://arxiv.org/html/2606.19544v1 — § exact-v1 anchor: Minimum Viable Validation Protocol | https://arxiv.org/html/2606.19544v1 — § exact-v1 evaluation anchor: 118 runs | https://arxiv.org/html/2606.19544v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19544 | complete |
| SF-2026-ARXIV-2606-19559 | RP-2946b51270383016 | deep | arXiv:2606.19559v1 | SRC-ARXIV@arXiv:2606.19559v1 | https://arxiv.org/html/2606.19559v1 — § exact-v1 anchor: action confidence from request uncertainty | https://arxiv.org/html/2606.19559v1 — § exact-v1 evaluation anchor: five LLM backbones | https://arxiv.org/html/2606.19559v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19559 | complete |
| SF-2026-ARXIV-2606-19595 | RP-0d67b5370a61594a | deep | arXiv:2606.19595v1 | SRC-ARXIV@arXiv:2606.19595v1 | https://arxiv.org/html/2606.19595v1 — § exact-v1 anchor: Post-Interruption Recovery | https://arxiv.org/html/2606.19595v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19595v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19595 | complete |
| SF-2026-ARXIV-2606-19613 | RP-25646df540d73ac2 | deep | arXiv:2606.19613v1 | SRC-ARXIV@arXiv:2606.19613v1 | https://arxiv.org/html/2606.19613v1 — § exact-v1 anchor: 100 Interaction Turns | https://arxiv.org/html/2606.19613v1 — § exact-v1 evaluation anchor: 20 scenarios | https://arxiv.org/html/2606.19613v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19613 | complete |
| SF-2026-ARXIV-2606-19667 | RP-5baa9c06caf84ed7 | deep | arXiv:2606.19667v1 | SRC-ARXIV@arXiv:2606.19667v1 | https://arxiv.org/html/2606.19667v1 — § exact-v1 anchor: prefix tree over recently served evidence sequences | https://arxiv.org/html/2606.19667v1 — § exact-v1 evaluation anchor: three vLLM configurations | https://arxiv.org/html/2606.19667v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19667 | complete |
| SF-2026-ARXIV-2606-19692 | RP-c13c9c459b44e695 | deep | arXiv:2606.19692v1 | SRC-ARXIV@arXiv:2606.19692v1 | https://arxiv.org/html/2606.19692v1#S5 — §5 Incremental Systems Architecture | https://arxiv.org/html/2606.19692v1#S9 — §9 Systems Evaluation | https://arxiv.org/html/2606.19692v1#S13 — §13 Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19692 | complete |
| SF-2026-ARXIV-2606-19704 | RP-ded7d6e10d00311a | deep | arXiv:2606.19704v1 | SRC-ARXIV@arXiv:2606.19704v1 | https://arxiv.org/html/2606.19704v1#S4 — §4 Predictive Validity as the Ranking Criterion | https://arxiv.org/html/2606.19704v1#S6 — §6 Implications for Benchmark Design | https://arxiv.org/html/2606.19704v1#S8 — §Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19704 | complete |
| SF-2026-ARXIV-2606-19714 | RP-062a8e997f6b95cc | deep | arXiv:2606.19714v1 | SRC-ARXIV@arXiv:2606.19714v1 | https://arxiv.org/html/2606.19714v1#S4 — §4 Methodology | https://arxiv.org/html/2606.19714v1#S6 — §6 Experiments | https://arxiv.org/html/2606.19714v1#A5 — §Appendix E Experimental Details | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19714 | complete |
| SF-2026-ARXIV-2606-19719 | RP-691ee5e1c14e2cbc | deep | arXiv:2606.19719v1 | SRC-ARXIV@arXiv:2606.19719v1 | https://arxiv.org/html/2606.19719v1#S3 — §3 Cache-Aware Metrics | https://arxiv.org/html/2606.19719v1#S4 — §4 Experimental Setup and §5 Results | https://arxiv.org/html/2606.19719v1#A2.SS4 — §Appendix B.4 Quality Considerations and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19719 | complete |
| SF-2026-ARXIV-2606-19746 | RP-61fd57fa75893e4e | deep | arXiv:2606.19746v1 | SRC-ARXIV@arXiv:2606.19746v1 | https://arxiv.org/html/2606.19746v1#S4 — §4 System Design | https://arxiv.org/html/2606.19746v1#S5 — §5 Evaluation | https://arxiv.org/html/2606.19746v1#S6 — §6 Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19746 | complete |
| SF-2026-ARXIV-2606-19753 | RP-c972392ec2ec3f66 | deep | arXiv:2606.19753v1 | SRC-ARXIV@arXiv:2606.19753v1 | https://arxiv.org/html/2606.19753v1#S2 — §2 Grounded Inference Primitives | https://arxiv.org/html/2606.19753v1#S5 — §5 Reference Architecture | https://arxiv.org/html/2606.19753v1#S7 — §7 Generative Model Risks | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19753 | complete |
| SF-2026-ARXIV-2606-19755 | RP-27409fe63680c354 | deep | arXiv:2606.19755v1 | SRC-ARXIV@arXiv:2606.19755v1 | https://arxiv.org/html/2606.19755v1#S3 — §3 Methodology | https://arxiv.org/html/2606.19755v1#S4 — §4 Experiments and §5 Ablation | https://arxiv.org/html/2606.19755v1#A1 — §Appendix A Experimental Setup and Safety Head | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19755 | complete |
| SF-2026-ARXIV-2606-19758 | RP-726feb59653f0bfd | deep | arXiv:2606.19758v1 | SRC-ARXIV@arXiv:2606.19758v1 | https://arxiv.org/html/2606.19758v1#S4 — §4 Methodology | https://arxiv.org/html/2606.19758v1#S5 — §5 Experiments | https://arxiv.org/html/2606.19758v1#A3 — §Appendix C Fallback Routing | https://anonymous.4open.science/r/SIGMA-2338/ — code artifact disclosed by arXiv:2606.19758v1 | claim:SF-2026-ARXIV-2606-19758 | complete |
| SF-2026-ARXIV-2606-19769 | RP-76ebce1b4564d3ce | deep | arXiv:2606.19769v1 | SRC-ARXIV@arXiv:2606.19769v1 | https://arxiv.org/html/2606.19769v1#S5 — §V Data Standards as Infrastructure | https://arxiv.org/html/2606.19769v1#S6 — §VI Implementation Priorities | https://arxiv.org/html/2606.19769v1#S4 — §IV Why More Data Is Not Enough | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19769 | complete |
| SF-2026-ARXIV-2606-19795 | RP-322a480b058b9997 | deep | arXiv:2606.19795v1 | SRC-ARXIV@arXiv:2606.19795v1 | https://arxiv.org/html/2606.19795v1#S3 — §3 Handoff Contracts, Objects, and Coordination | https://arxiv.org/html/2606.19795v1#S6 — §6 Unified Handoff Protocol | https://arxiv.org/html/2606.19795v1#S1.SS2 — §1.2 Limitations of Existing Surveys and §1.3 Scope | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19795 | complete |
| SF-2026-ARXIV-2606-19803 | RP-aeaf792b78e8e2bd | deep | arXiv:2606.19803v1 | SRC-ARXIV@arXiv:2606.19803v1 | https://arxiv.org/html/2606.19803v1#S2 — §2 FGAC Policy Model | https://arxiv.org/html/2606.19803v1#S4 — §4 Preliminary Experiments | https://arxiv.org/html/2606.19803v1#S5 — §5 Discussion and §6 Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19803 | complete |
| SF-2026-ARXIV-2606-19808 | RP-0c555a3d9a53ebe1 | deep | arXiv:2606.19808v1 | SRC-ARXIV@arXiv:2606.19808v1 | https://arxiv.org/html/2606.19808v1#S4 — §4 Selective Verification Method | https://arxiv.org/html/2606.19808v1#S5 — §5 Experimental Setup and §6 Results | https://arxiv.org/html/2606.19808v1#A10 — §Appendix J Limitations and Deployment Considerations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19808 | complete |
| SF-2026-ARXIV-2606-19847 | RP-1199ba0db5407a9a | deep | arXiv:2606.19847v1 | SRC-ARXIV@arXiv:2606.19847v1 | https://arxiv.org/html/2606.19847v1#S3 — §3 AtomMem Methods | https://arxiv.org/html/2606.19847v1#S4 — §4 Experiments | https://arxiv.org/html/2606.19847v1#S5 — §5 Conclusion and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19847 | complete |
| SF-2026-ARXIV-2606-19849 | RP-c7ef0298826dbad5 | deep | arXiv:2606.19849v1 | SRC-ARXIV@arXiv:2606.19849v1 | https://arxiv.org/html/2606.19849v1#S3 — §3 Stage-Wise Coordinated Streaming | https://arxiv.org/html/2606.19849v1#S4 — §4 Experiments | https://arxiv.org/html/2606.19849v1#S5 — §5 Accuracy-Latency and Resource-Constrained Parallelism | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19849 | complete |
| SF-2026-ARXIV-2606-19868 | RP-9a14dd683ba0cdbc | deep | arXiv:2606.19868v1 | SRC-ARXIV@arXiv:2606.19868v1 | https://arxiv.org/html/2606.19868v1#S3 — §III Uncertainty-Estimation Taxonomy | https://arxiv.org/html/2606.19868v1#S4 — §IV Experimental Setup | https://arxiv.org/html/2606.19868v1#S6 — §VI Conclusion and Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19868 | complete |
| SF-2026-ARXIV-2606-19887 | RP-4180b67bff117050 | deep | arXiv:2606.19887v1 | SRC-ARXIV@arXiv:2606.19887v1 | https://arxiv.org/html/2606.19887v1#S3 — §III FinRED Framework | https://arxiv.org/html/2606.19887v1#S4 — §IV Experiments and §V Expert Validation | https://arxiv.org/html/2606.19887v1#S6 — §VI Reliability and Limitations | https://github.com/selectstar-ai/FinRED-paper; https://huggingface.co/datasets/datumo/FinRED — code and dataset artifacts disclosed by arXiv:2606.19887v1 | claim:SF-2026-ARXIV-2606-19887 | complete |
| SF-2026-ARXIV-2606-19898 | RP-a051e671356d2188 | deep | arXiv:2606.19898v1 | SRC-ARXIV@arXiv:2606.19898v1 | https://arxiv.org/html/2606.19898v1#S3 — §3 Rule-Based Router and §4 ML Router | https://arxiv.org/html/2606.19898v1#S6 — §6 Experiments | https://arxiv.org/html/2606.19898v1#S7 — §7 Conclusion and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19898 | complete |
| SF-2026-ARXIV-2606-19899 | RP-582a009d8f6e71f7 | deep | arXiv:2606.19899v1 | SRC-ARXIV@arXiv:2606.19899v1 | https://arxiv.org/pdf/2606.19899v1#page=9 — §PDF pp.9–15 Capability-Evaluation Methods | https://arxiv.org/pdf/2606.19899v1#page=16 — §PDF pp.16–26 Evaluation Results | https://arxiv.org/pdf/2606.19899v1#page=28 — §PDF pp.28–30 Limitations and Risk Interpretation | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19899 | complete |
| SF-2026-ARXIV-2606-19911 | RP-20744799a9ebab1e | deep | arXiv:2606.19911v1 | SRC-ARXIV@arXiv:2606.19911v1 | https://arxiv.org/html/2606.19911v1#S3 — §3 Multi-Agent Transactive Memory | https://arxiv.org/html/2606.19911v1#S4 — §4 Experimental Setup and §5 Results | https://arxiv.org/html/2606.19911v1#S6 — §6 Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19911 | complete |
| SF-2026-ARXIV-2606-19989 | RP-b38d576c58041147 | deep | arXiv:2606.19989v1 | SRC-ARXIV@arXiv:2606.19989v1 | https://arxiv.org/html/2606.19989v1#S2 — §2 Online Dynamic Batching System Design | https://arxiv.org/html/2606.19989v1#S4 — §4 Experimental Evaluation | https://arxiv.org/html/2606.19989v1#S5 — §5 Scope and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19989 | complete |
| SF-2026-ARXIV-2606-19992 | RP-7adfc2821bbff09d | deep | arXiv:2606.19992v1 | SRC-ARXIV@arXiv:2606.19992v1 | https://arxiv.org/html/2606.19992v1#S3 — §3 ToolPro Design | https://arxiv.org/html/2606.19992v1#S4 — §4 Experiments | https://arxiv.org/html/2606.19992v1#S5 — §5 Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19992 | complete |
| SF-2026-ARXIV-2606-19998 | RP-694e1b3d6952190b | deep | arXiv:2606.19998v1 | SRC-ARXIV@arXiv:2606.19998v1 | https://arxiv.org/html/2606.19998v1#S3 — §3 Tri-Info Method | https://arxiv.org/html/2606.19998v1#S4 — §4 Experimental Setup and §5 Results | https://arxiv.org/html/2606.19998v1#S5.SS4 — §5.4 Conclusion and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-19998 | complete |
| SF-2026-ARXIV-2606-20002 | RP-f7e3232b7bd95940 | deep | arXiv:2606.20002v1 | SRC-ARXIV@arXiv:2606.20002v1 | https://arxiv.org/html/2606.20002v1#S2 — §2 Connect-the-Dots Framework | https://arxiv.org/html/2606.20002v1#S3 — §3 Implementations and Experiments | https://arxiv.org/html/2606.20002v1#S4 — §4 Analysis and Limitations | https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod/examples/research_cod — implementation disclosed by arXiv:2606.20002v1 | claim:SF-2026-ARXIV-2606-20002 | complete |
| SF-2026-ARXIV-2606-20005 | RP-a29aec0ec277fe4d | deep | arXiv:2606.20005v1 | SRC-ARXIV@arXiv:2606.20005v1 | https://arxiv.org/html/2606.20005v1#S3 — §3 StreamKL Forward/Backward Pass | https://arxiv.org/html/2606.20005v1#S5 — §5 Experiments | https://arxiv.org/html/2606.20005v1#S6 — §6 Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20005 | complete |
| SF-2026-ARXIV-2606-20023 | RP-50e668003ea41e9f | deep | arXiv:2606.20023v1 | SRC-ARXIV@arXiv:2606.20023v1 | https://arxiv.org/html/2606.20023v1#S2 — §2 Privilege Model and Selection Analysis | https://arxiv.org/html/2606.20023v1#S3 — §3 Evaluation Setup and §4 Empirical Analysis | https://arxiv.org/html/2606.20023v1#S5 — §5 Mitigation and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20023 | complete |
| SF-2026-ARXIV-2606-20047 | RP-90c7ab390f612f9b | deep | arXiv:2606.20047v1 | SRC-ARXIV@arXiv:2606.20047v1 | https://arxiv.org/html/2606.20047v1#S3 — §3 PACMS System Design | https://arxiv.org/html/2606.20047v1#S5 — §5 Evaluation | https://arxiv.org/html/2606.20047v1#S5.SS2 — §5.2 Scope and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20047 | complete |
| SF-2026-ARXIV-2606-20113 | RP-fb409fa4b9c158a3 | deep | arXiv:2606.20113v1 | SRC-ARXIV@arXiv:2606.20113v1 | https://arxiv.org/html/2606.20113v1#S3 — §3 Problem Formalization and Stabilization Controller | https://arxiv.org/html/2606.20113v1#S5 — §5 Experiments | https://arxiv.org/html/2606.20113v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20113 | complete |
| SF-2026-ARXIV-2606-20122 | RP-f249957d58c3af3d | deep | arXiv:2606.20122v1 | SRC-ARXIV@arXiv:2606.20122v1 | https://arxiv.org/html/2606.20122v1#S4 — §4 Utility-Guided Dynamic Outline Optimization | https://arxiv.org/html/2606.20122v1#S5 — §5 Experiments | https://arxiv.org/html/2606.20122v1#S6 — §6 Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20122 | complete |
| SF-2026-ARXIV-2606-20128 | RP-84687f4f8b364f54 | deep | arXiv:2606.20128v1 | SRC-ARXIV@arXiv:2606.20128v1 | https://arxiv.org/html/2606.20128v1#S3 — §3 Differential Correctness Method | https://arxiv.org/html/2606.20128v1#S4 — §4 Evaluation | https://arxiv.org/html/2606.20128v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20128 | complete |
| SF-2026-ARXIV-2606-20158 | RP-4d50659e52912c89 | deep | arXiv:2606.20158v1 | SRC-ARXIV@arXiv:2606.20158v1 | https://arxiv.org/html/2606.20158v1#S2 — §II N-Version Coding-Agent Architecture | https://arxiv.org/html/2606.20158v1#S3 — §III Experimental Methodology and §IV Results | https://arxiv.org/html/2606.20158v1#S5 — §V Threats to Validity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20158 | complete |
| SF-2026-ARXIV-2606-20235 | RP-392f4bfb8706ca2d | deep | arXiv:2606.20235v1 | SRC-ARXIV@arXiv:2606.20235v1 | https://arxiv.org/html/2606.20235v1#S3 — §3 ScholarQuest Construction | https://arxiv.org/html/2606.20235v1#S5 — §5 Evaluation | https://arxiv.org/html/2606.20235v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20235 | complete |
| SF-2026-ARXIV-2606-20243 | RP-8f285092e2b9544f | deep | arXiv:2606.20243v1 | SRC-ARXIV@arXiv:2606.20243v1 | https://arxiv.org/html/2606.20243v1#S3 — §III Phoenix System Architecture | https://arxiv.org/html/2606.20243v1#S4 — §IV Evaluation | https://arxiv.org/html/2606.20243v1#S5 — §V Discussion and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20243 | complete |
| SF-2026-ARXIV-2606-20245 | RP-f5a1a2f002544540 | deep | arXiv:2606.20245v1 | SRC-ARXIV@arXiv:2606.20245v1 | https://arxiv.org/html/2606.20245v1#S3 — §III Explicit Knowledge-Conflict Methodology | https://arxiv.org/html/2606.20245v1#S4 — §IV Experiments | https://arxiv.org/html/2606.20245v1#S5 — §V Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20245 | complete |
| SF-2026-ARXIV-2606-20254 | RP-38a22ee7bfc0c6e3 | deep | arXiv:2606.20254v1 | SRC-ARXIV@arXiv:2606.20254v1 | https://arxiv.org/html/2606.20254v1#S4 — §4 Threat Model and §5 Task-Arithmetic Removal | https://arxiv.org/html/2606.20254v1#S6 — §6 Evaluation | https://arxiv.org/html/2606.20254v1#S7 — §7 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20254 | complete |
| SF-2026-ARXIV-2606-20318 | RP-212218bf18adb6bb | deep | arXiv:2606.20318v1 | SRC-ARXIV@arXiv:2606.20318v1 | https://arxiv.org/html/2606.20318v1#S4 — §4 AgenticDB Design | https://arxiv.org/html/2606.20318v1#S5 — §5 Evaluation Methodology and §6 Results | https://arxiv.org/html/2606.20318v1#S7 — §7 Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20318 | complete |
| SF-2026-ARXIV-2606-20363 | RP-391bf36a70f6b126 | deep | arXiv:2606.20363v1 | SRC-ARXIV@arXiv:2606.20363v1 | https://arxiv.org/html/2606.20363v1#S4 — §4 Automated SKILL.md Generation | https://arxiv.org/html/2606.20363v1#S5 — §5 Experiments | https://arxiv.org/html/2606.20363v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20363 | complete |
| SF-2026-ARXIV-2606-20374 | RP-f3090f909a736e29 | deep | arXiv:2606.20374v1 | SRC-ARXIV@arXiv:2606.20374v1 | https://arxiv.org/html/2606.20374v1#S3 — §3 ARGUS System Overview | https://arxiv.org/html/2606.20374v1#S4 — §4 Runtime Monitoring and Diagnosis Evaluation | https://arxiv.org/html/2606.20374v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20374 | complete |
| SF-2026-ARXIV-2606-20381 | RP-67a9d16b459379d4 | deep | arXiv:2606.20381v1 | SRC-ARXIV@arXiv:2606.20381v1 | https://arxiv.org/html/2606.20381v1#S4 — §4 UFP4 Recipe | https://arxiv.org/html/2606.20381v1#S5 — §5 Experiments | https://arxiv.org/html/2606.20381v1#S6 — §6 Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20381 | complete |
| SF-2026-ARXIV-2606-20408 | RP-7ef903cba4a59e56 | deep | arXiv:2606.20408v1 | SRC-ARXIV@arXiv:2606.20408v1 | https://arxiv.org/html/2606.20408v1#S3 — §3 NRT-Bench Design | https://arxiv.org/html/2606.20408v1#S4 — §4 Experimental Setup and Evaluation | https://arxiv.org/html/2606.20408v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20408 | complete |
| SF-2026-ARXIV-2606-20470 | RP-cdb915d6b69bd787 | deep | arXiv:2606.20470v1 | SRC-ARXIV@arXiv:2606.20470v1 | https://arxiv.org/html/2606.20470v1#S3 — §III Defense and §IV Misdirection | https://arxiv.org/html/2606.20470v1#S5 — §V Simulation Evaluation | https://arxiv.org/html/2606.20470v1#S6 — §VI Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20470 | complete |
| SF-2026-ARXIV-2606-20474 | RP-ac4c4262fb3008bb | deep | arXiv:2606.20474v1 | SRC-ARXIV@arXiv:2606.20474v1 | https://arxiv.org/html/2606.20474v1#S4 — §4 Ultra-TurboQuant and §5 UltraQuant | https://arxiv.org/html/2606.20474v1#S6 — §6 Accuracy and §7 Systems Evaluation | https://arxiv.org/html/2606.20474v1#S8 — §8 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20474 | complete |
| SF-2026-ARXIV-2606-20475 | RP-9de8a5bbb7075a21 | deep | arXiv:2606.20475v1 | SRC-ARXIV@arXiv:2606.20475v1 | https://arxiv.org/html/2606.20475v1#S3 — §3 Marginal-Advantage Accumulation | https://arxiv.org/html/2606.20475v1#S4 — §4 Experiments | https://arxiv.org/html/2606.20475v1#S5 — §5 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20475 | complete |
| SF-2026-ARXIV-2606-20487 | RP-b940f941cca68b76 | deep | arXiv:2606.20487v1 | SRC-ARXIV@arXiv:2606.20487v1 | https://arxiv.org/html/2606.20487v1#S3 — §3 Hierarchical Recovery Methodology | https://arxiv.org/html/2606.20487v1#S4 — §4 Experiments | https://arxiv.org/html/2606.20487v1#S5 — §5 Failure Analysis and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20487 | complete |
| SF-2026-ARXIV-2606-20493 | RP-77a86b6f29e4212c | deep | arXiv:2606.20493v1 | SRC-ARXIV@arXiv:2606.20493v1 | https://arxiv.org/html/2606.20493v1#S3 — §3 Contagion Network Model | https://arxiv.org/html/2606.20493v1#S4 — §4 Experiments | https://arxiv.org/html/2606.20493v1#S5 — §5 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20493 | complete |
| SF-2026-ARXIV-2606-20502 | RP-0bf6eff9a456738b | deep | arXiv:2606.20502v1 | SRC-ARXIV@arXiv:2606.20502v1 | https://arxiv.org/html/2606.20502v1#S3 — §III Methodological Framework | https://arxiv.org/html/2606.20502v1#S4 — §IV Results | https://arxiv.org/html/2606.20502v1#S6 — §VI Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20502 | complete |
| SF-2026-ARXIV-2606-20510 | RP-67600c27d15826a2 | deep | arXiv:2606.20510v1 | SRC-ARXIV@arXiv:2606.20510v1 | https://arxiv.org/html/2606.20510v1#S3 — §3 Verification Optimization and §4 Relaxation | https://arxiv.org/html/2606.20510v1#S5 — §5 Evaluation | https://arxiv.org/html/2606.20510v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20510 | complete |
| SF-2026-ARXIV-2606-20512 | RP-d8a742aecaafc237 | deep | arXiv:2606.20512v1 | SRC-ARXIV@arXiv:2606.20512v1 | https://arxiv.org/html/2606.20512v1#S3 — §3 Probe-and-Refine Design | https://arxiv.org/html/2606.20512v1#S4 — §4 Evaluation through §7 Cross-Model Analysis | https://arxiv.org/html/2606.20512v1#S9 — §9 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20512 | complete |
| SF-2026-ARXIV-2606-20520 | RP-6c72032bcaba9641 | deep | arXiv:2606.20520v1 | SRC-ARXIV@arXiv:2606.20520v1 | https://arxiv.org/html/2606.20520v1#S4 — §4 Broker Execution and §5 Scoped Identity | https://arxiv.org/html/2606.20520v1#S8 — §8 Evaluation and §9 Security Analysis | https://arxiv.org/html/2606.20520v1#S10 — §10 Discussion and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20520 | complete |
| SF-2026-ARXIV-2606-20529 | RP-c8d78f7ab01e108b | deep | arXiv:2606.20529v1 | SRC-ARXIV@arXiv:2606.20529v1 | https://arxiv.org/html/2606.20529v1#S3 — §3 LedgerAgent Method | https://arxiv.org/html/2606.20529v1#S4 — §4 Experiments | https://arxiv.org/html/2606.20529v1#S5 — §5 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20529 | complete |
| SF-2026-ARXIV-2606-20536 | RP-6a6d900fef2a17af | deep | arXiv:2606.20536v1 | SRC-ARXIV@arXiv:2606.20536v1 | https://arxiv.org/html/2606.20536v1#S3 — §3 Experimental Setup | https://arxiv.org/html/2606.20536v1#S4 — §4 Experiments | https://arxiv.org/html/2606.20536v1#S5 — §5 Limitations and Recommendations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20536 | complete |
| SF-2026-ARXIV-2606-20537 | RP-d0d0e2cb26d1b959 | deep | arXiv:2606.20537v1 | SRC-ARXIV@arXiv:2606.20537v1 | https://arxiv.org/html/2606.20537v1#S2 — §2 FlashRT Runtime Substrate and Execution-State Capsules | https://arxiv.org/html/2606.20537v1#S4 — §4 Evaluation | https://arxiv.org/html/2606.20537v1#S5 — §5 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20537 | complete |
| SF-2026-ARXIV-2606-20545 | RP-33157592a04e39d5 | deep | arXiv:2606.20545v1 | SRC-ARXIV@arXiv:2606.20545v1 | https://arxiv.org/html/2606.20545v1#S3 — §3 WRBench Suite and Persistent-State Diagnostics | https://arxiv.org/html/2606.20545v1#S4 — §4 Evaluation | https://arxiv.org/html/2606.20545v1#S5 — §5 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20545 | complete |
| SF-2026-ARXIV-2606-20553 | RP-7e0df945a420c1f9 | deep | arXiv:2606.20553v1 | SRC-ARXIV@arXiv:2606.20553v1 | https://arxiv.org/html/2606.20553v1#S3 — §3 Threat Model and §4 Privacy-Backdoor Attack | https://arxiv.org/html/2606.20553v1#S5 — §5 Evaluation | https://arxiv.org/html/2606.20553v1#S6 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20553 | complete |
| SF-2026-ARXIV-2606-20562 | RP-ec769ff78729d332 | deep | arXiv:2606.20562v1 | SRC-ARXIV@arXiv:2606.20562v1 | https://arxiv.org/html/2606.20562v1#S3 — §3 MemoryWAM Method | https://arxiv.org/html/2606.20562v1#S4 — §4 Experiments | https://arxiv.org/html/2606.20562v1#A1 — §Appendix A Additional Results and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-20562 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-19376:start -->
### 2606.19376 — Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees

**问题与旧路径。** `Inference costs for large language model (LLM) applications are rapidly growing, driven by surging demand and rising infrastructure cost.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** LLM router 可在稀疏、单侧 user feedback下在线学习cost policy，同时把满意度SLA作为约束而非平均reward。 Authoritative owner 是 `INFER-SCHEDULING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 多类LLM benchmarks；SLARouter报告保持SLA并最高降成本2.2×，无需per-benchmark tuning。 Method locator：`https://arxiv.org/html/2606.19376v1 — § exact-v1 anchor: SLARouter`。Evaluation locator：`https://arxiv.org/html/2606.19376v1 — § exact-v1 evaluation anchor: wide range of LLM benchmarks`。Benchmark identity：model=`Candidate LLMs in the exact-v1 SLARouter benchmark matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Per-user satisfaction guarantee used by SLARouter; no universal deployment SLO`；evaluator=`Cost subject to user-satisfaction guarantee over multiple LLM benchmarks with sparse one-sided feedback`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 理论保证依赖反馈与可行性假设；offline benchmark satisfaction不是生产SLA，delayed/strategic feedback会破坏校准。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-19376:start -->
Claim boundary：只使用 `arXiv:2606.19376v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-19376:end -->
<!-- review:SF-2026-ARXIV-2606-19376:end -->

<!-- review:SF-2026-ARXIV-2606-19380:start -->
### 2606.19380 — AgentArmor: A Framework, Evaluation, & Mitigation of Coding Agent Failures

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：coding-agent safety failure 应拆成 underspecification、capability error 与 harness error，并分别用 policy、classifier/immutability 与 context/tool control修复。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.19380v1 §6 Implementation and Results; Appendices` 支持 `eight coding-agent safety evaluations plus mitigation tests`；模型 `frontier coding agents and AgentArmor`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.19380v1 §3 setup; §4 scenarios; §5 design`；counterevidence locator：`arXiv:2606.19380v1 §7 future directions; Appendix C.17 validity`。

**Trade-off / failure / coexistence / evolution。** 分解支持定向缓解但有限场景不能证明安全 guarantee；自修改 harness 还需外部 immutable authority。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-19380:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.19380v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-19380:end -->
<!-- review:SF-2026-ARXIV-2606-19380:end -->

<!-- review:SF-2026-ARXIV-2606-19382:start -->
### 2606.19382 — DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Multi-Agent workflow scheduler应从dependency DAG释放ready tasks、并行independent work且在fault时保持topological correctness。

**State / data / control owner。** `AGENT-MULTI-AGENT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.19382v1 §§3–4 DynAMO plan-then-execute scheduler`；evaluation locator 为 `arXiv:2606.19382v1 §5 six AssetOpsBench experiments`；counterevidence locator 为 `arXiv:2606.19382v1 §6 limitations and industrial-benchmark/tool-latency scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Ch82/81已拥有dependency DAG、ready-node release、独立workspace与coordinator bottleneck/fallback，不机械追加。

<!-- claim:SF-2026-ARXIV-2606-19382:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.19382v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-19382:end -->
<!-- review:SF-2026-ARXIV-2606-19382:end -->

<!-- review:SF-2026-ARXIV-2606-19386:start -->
### 2606.19386 — Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：wall-clock moment detector 在 Agent cadence 下可能结构性双稳态；monitor 必须以可观测 transition window 校准而非宣称瞬时状态真值。

**State / data / control owner。** `PLATFORM-MONITORING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.19386v1 §2 Setup; §3 Δt=0 Audit and Erratum; §§4–9 cadence sweeps, scaling and transition triggers`；`arXiv:2606.19386v1 §4 Uniform-Cadence Sweep; §5 Measured Real Cadence; §6 burst structure; Appendix A replay/instrumentation`；counterevidence `arXiv:2606.19386v1 §8 scaling-rule limits; §9 transition-trigger timing problem; §11 Limitations`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 论文首先纠正自身 Δt=0 错误，后续 bistability 只覆盖所测 cadence/monitor class；时钟或 burst 分布漂移时回退 transition-window 告警而非 moment truth。

<!-- claim:SF-2026-ARXIV-2606-19386:start -->
仅使用 `https://arxiv.org/html/2606.19386v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-19386:end -->
<!-- review:SF-2026-ARXIV-2606-19386:end -->

<!-- review:SF-2026-ARXIV-2606-19390:start -->
### 2606.19390 — Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework

**问题与机制变化。** Agentic advisory automation需把 AIBOM/SBOM、runtime activation evidence、signed CSAF-VEX与replay bundle连成同一漏洞处置链，不能仅按静态依赖宣告 affected/not affected。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.19390v1 PDF §§3–5 AIBOM-driven CSAF-VEX workflow and execution binding`；Evaluation=`arXiv:2606.19390v1 PDF §§6–7 reproducibility/case-study evaluation`；Counterevidence=`Not Disclosed — arXiv:2606.19390v1 has no dedicated limitations section; exact-v1 counterevidence is localized at PDF limitations on dependency inventory, activation observability and advisory authority`。Workload=`Approximately 10,000 SBOM entries plus synthetic dependency graphs of 50, 500 and 5,000 components; five-fold cross-validation`；Model=`Random forest with 200 estimators and maximum depth 12; XGBoost with 300 trees, learning rate 0.05, maximum depth 6 and subsampling 0.8`；Hardware=`Not Disclosed`；Evaluator=`advisory consistency, activation evidence, signed artifact and replay reproducibility`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 运行证据可减少误报却可能漏掉潜在路径；自动VEX不能替代产品安全 owner签署与补丁验证。

<!-- claim:SF-2026-ARXIV-2606-19390:start -->
**Claim boundary。** 只使用 `https://arxiv.org/pdf/2606.19390v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-19390:end -->
<!-- review:SF-2026-ARXIV-2606-19390:end -->

<!-- review:SF-2026-ARXIV-2606-19409:start -->
### 2606.19409 — OpenRath: Session-Centered Runtime State for Agent Systems

**问题与旧路径。** Modern agent systems often suffer from fragmented runtime state: transcripts, tool effects, memory events, workspace placement, branch provenance, and replay evidence are recorded separately and become difficult to inspect or reproduce. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Session 应成为执行路径携带的一等 runtime value，统一 transcript、tool effect、sandbox、branch lineage、token usage、pending work 与 memory event；fork/merge/replay 是显式操作。 唯一知识 owner 为 `AGENT-PLATFORM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 报告只验证 controlled runtime properties 与 audited milestones，没有 broad quantitative comparison。 Method=`https://arxiv.org/html/2606.19409v1 — § exact-v1 anchor: Session-Centered Runtime State`；Evaluation=`https://arxiv.org/html/2606.19409v1 — § exact-v1 evaluation anchor: audited milestones`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`audited runtime invariants and controlled replay properties; no broad quality benchmark`。

**Trade-off、failure、共存与演进。** live-provider quality、optional backend availability 与 memory quality明确未证明；central Session 也可能扩大故障域。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19409v1 — § exact-v1 limitation/counterevidence anchor: claims are limited`。

<!-- claim:SF-2026-ARXIV-2606-19409:start -->
Claim boundary：仅 `arXiv:2606.19409v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19409:end -->
<!-- review:SF-2026-ARXIV-2606-19409:end -->

<!-- review:SF-2026-ARXIV-2606-19464:start -->
### 2606.19464 — Deontic Policies for Runtime Governance of Agentic AI Systems

**问题与旧路径。** Autonomous agentic AI systems driven by Large Language Models (LLMs) introduce a new class of security, privacy, and compliance challenges: an agent that can invoke tools, manipulate data, install software, and coordinate with peer agents across organizational boundaries must be constrained not just by authentication and access control, but by the full structure of enterprise governance. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** runtime governance 除 permit/prohibit 外还需 obligation lifecycle、dispensation、meta-policy precedence 与 ontology reasoning，并在 LLM 外执行。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 以 AgenticRei examples 展示 tool calls 与 A2A messages 的 policy expression/evaluation。 Method=`https://arxiv.org/html/2606.19464v1 — § exact-v1 anchor: obligations, dispensations`；Evaluation=`https://arxiv.org/html/2606.19464v1 — § exact-v1 evaluation anchor: examples`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`expressibility and runtime policy-evaluation examples`。

**Trade-off、failure、共存与演进。** 示例不构成吞吐、安全或完备性证明；ontology/policy conflict 仍需可信 owner 与版本治理。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19464v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19464:start -->
Claim boundary：仅 `arXiv:2606.19464v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19464:end -->
<!-- review:SF-2026-ARXIV-2606-19464:end -->

<!-- review:SF-2026-ARXIV-2606-19535:start -->
### 2606.19535 — FloatDoor: Platform-Triggered Backdoors in LLMs

**问题与旧路径。** Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** model artifact identity 必须绑定 serving platform/kernel；FloatDoor 通过两个 LoRA 放大 floating-point divergence 并把 platform signature 绑定恶意 task，暴露 audit/serve TOCTOU。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen3-4B 跨 NVIDIA GPU、Google TPU、AWS Graviton、Alibaba Yitian-710，并展示目标平台 code vulnerability。 Method=`https://arxiv.org/html/2606.19535v1 — § exact-v1 anchor: platform-triggered backdoor`；Evaluation=`https://arxiv.org/html/2606.19535v1 — § exact-v1 evaluation anchor: broad range of deployment targets`。Benchmark contract：model=`Qwen3-4B and Qwen3-8B with two LoRA adapters`；hardware=`NVIDIA H200, NVIDIA A100, NVIDIA H100, NVIDIA DGX Spark, Google TPU, AWS Graviton and Alibaba Yitian-710`；precision=`Not Disclosed`；batch=`1`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`target-platform activation, aggregate utility and vulnerable-code generation`。

**Trade-off、failure、共存与演进。** 攻击依赖作者平台集合与 LoRA；跨平台不一致不等于任意模型都可植入，可信构建仍需独立证明。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19535v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19535:start -->
Claim boundary：仅 `arXiv:2606.19535v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19535:end -->
<!-- review:SF-2026-ARXIV-2606-19535:end -->

<!-- review:SF-2026-ARXIV-2606-19544:start -->
### 2606.19544 — Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias

**问题与旧路径。** LLM-as-a-Judge has become the dominant evaluation paradigm for language models, but judge validation in practice relies on exact-match agreement, a metric that does not correct for chance and systematically overstates discriminative ability. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Judge validation 要同时报告 chance-corrected agreement、test-retest consistency 与 position/verbosity bias；高 consistency 不能替代 validity。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 21 judges、9 providers、3 benchmarks、118 runs、约 541k judgments；报告 kappa deflation 与 ranking shifts。 Method=`https://arxiv.org/html/2606.19544v1 — § exact-v1 anchor: Minimum Viable Validation Protocol`；Evaluation=`https://arxiv.org/html/2606.19544v1 — § exact-v1 evaluation anchor: 118 runs`。Benchmark contract：model=`Gemini 3.1 Pro, Claude Opus 4.6, DeepSeek V3.2, Claude Sonnet 4.6, Llama 3.3 70B, Kimi K2.5, GPT-5.4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, GLM-5, GPT-oss 120B, Claude Sonnet 4, Gemini 2.5 Flash, Claude Haiku 4.5, GPT-4.1-mini, Minimax M2.7, Qwen 3 8B, GPT-4o-mini, Mixtral 8x22B and GPT-5.4-mini`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`agreement, Cohen's kappa, test-retest consistency, position bias and verbosity bias`。

**Trade-off、failure、共存与演进。** 三个 benchmark 与单一 pairwise rubric 不证明所有 judge 场景；Cohen kappa 也依赖 prevalence。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19544v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-19544:start -->
Claim boundary：仅 `arXiv:2606.19544v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19544:end -->
<!-- review:SF-2026-ARXIV-2606-19544:end -->

<!-- review:SF-2026-ARXIV-2606-19559:start -->
### 2606.19559 — Uncertainty Decomposition for Clarification Seeking in LLM Agents

**问题与旧路径。** Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 黑盒 Agent 可把 action confidence 与 request uncertainty 分开；只有后者高时触发 clarification，避免把执行不确定与需求欠规范混成 abstention。 唯一知识 owner 为 `AGENT-PLANNING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 五个 backbones，在 WebShop/ALFWorld clarification variants 与 REAL 上比较 clarification F1/fault detection。 Method=`https://arxiv.org/html/2606.19559v1 — § exact-v1 anchor: action confidence from request uncertainty`；Evaluation=`https://arxiv.org/html/2606.19559v1 — § exact-v1 evaluation anchor: five LLM backbones`。Benchmark contract：model=`GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B and GPT-OSS-120B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`clarification F1 and fault detection across clarification and standard benchmarks`。

**Trade-off、failure、共存与演进。** prompt-based uncertainty 未校准成概率；benchmark 人工制造 50% 欠规范，澄清成本和用户响应质量未被完整建模。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19559v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19559:start -->
Claim boundary：仅 `arXiv:2606.19559v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19559:end -->
<!-- review:SF-2026-ARXIV-2606-19559:end -->

<!-- review:SF-2026-ARXIV-2606-19595:start -->
### 2606.19595 — IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows

**问题与旧路径。** Voice agents deployed in structured workflows (customer service, healthcare scheduling, account management) must handle frequent user interruptions while maintaining progress through multi-step procedures. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** voice-agent interruption recovery 必须保存 workflow node、已提交 side effects 与待确认槽位，恢复时区分 resume、repair、restart。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** IHBench 在 structured workflows 上测 interruption 后 task completion 与 recovery error。 Method=`https://arxiv.org/html/2606.19595v1 — § exact-v1 anchor: Post-Interruption Recovery`；Evaluation=`https://arxiv.org/html/2606.19595v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`GPT-4o Audio, GPT-4o Mini Audio, GPT Audio, GPT Audio Mini, GPT Realtime, GPT Realtime 1.5, GPT Realtime Mini, GPT Realtime 2, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash Live, Gemma 4 12B Instruct, Qwen3-Omni-30B-A3B-Instruct, Qwen2.5-Omni-7B, Phi-4-Multimodal-Instruct, Voxtral-Small-24B-2507, Qwen2-Audio-7B-Instruct, MiMo-Audio-7B-Instruct and Kimi-Audio-7B-Instruct across 27 mode/configuration combinations`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`post-interruption task completion and structured recovery error`。

**Trade-off、failure、共存与演进。** 模拟中断与语音管线不覆盖真实网络/ASR drift；恢复成功也不证明重复 effect 被阻止。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19595v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19595:start -->
Claim boundary：仅 `arXiv:2606.19595v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19595:end -->
<!-- review:SF-2026-ARXIV-2606-19595:end -->

<!-- review:SF-2026-ARXIV-2606-19613:start -->
### 2606.19613 — StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns

**问题与旧路径。** We introduce StaminaBench, a benchmark that measures the stamina of coding agents: how many consecutive interaction turns (change requests) they can handle before failing. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 6 harnesses×7 open LLMs、20 scenarios×100 turns；所有模型 5–6 turns 内失败，test feedback/retry 最多提升 12×。 Method=`https://arxiv.org/html/2606.19613v1 — § exact-v1 anchor: 100 Interaction Turns`；Evaluation=`https://arxiv.org/html/2606.19613v1 — § exact-v1 evaluation anchor: 20 scenarios`。Benchmark contract：model=`Devstral 2, Devstral Small 2, GLM-5, Kimi K2.5, Nemotron Super, Qwen3-Coder-Next and Qwen3.5-122B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`consecutive passed turns, test feedback/retry effect and harness sensitivity over 20x100-turn scenarios`。

**Trade-off、failure、共存与演进。** 程序生成 REST workload 不能代表全部软件演化；turn-to-failure 对变更难度和 harness 强敏感。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19613v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19613:start -->
Claim boundary：仅 `arXiv:2606.19613v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19613:end -->
<!-- review:SF-2026-ARXIV-2606-19613:end -->

<!-- review:SF-2026-ARXIV-2606-19667:start -->
### 2606.19667 — CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference

**问题与旧路径。** Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** RAG evidence set 不变时，可用近期 evidence-sequence prefix tree 重排证据，让集合重叠转成 token-prefix 重用；retriever 仍拥有 relevance，scheduler 只拥有顺序。 唯一知识 owner 为 `INFER-KV-CACHE`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 三个 vLLM configurations，median TTFT 降约 20–33%，QA quality 未下降；greedy 达 oracle TTFT gain 的 97.5%。 Method=`https://arxiv.org/html/2606.19667v1 — § exact-v1 anchor: prefix tree over recently served evidence sequences`；Evaluation=`https://arxiv.org/html/2606.19667v1 — § exact-v1 evaluation anchor: three vLLM configurations`。Benchmark contract：model=`Qwen2.5-1.5B and Qwen2.5-7B`；hardware=`RTX 4060 Ti 8 GB, RTX 4090 24 GB and RTX 4090D 24 GB`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`median TTFT, prefix reuse and QA answer quality`。

**Trade-off、failure、共存与演进。** 重排可能改变 positional bias 与答案；局部 query locality 不保证生产 cache hit，且不减少 decode cost。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19667v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19667:start -->
Claim boundary：仅 `arXiv:2606.19667v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19667:end -->
<!-- review:SF-2026-ARXIV-2606-19667:end -->

<!-- review:SF-2026-ARXIV-2606-19692:start -->
### 2606.19692 — When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems

**问题与旧路径。** Vector hubness, where a few points become nearest neighbors of many queries, creates a poisoning risk in retrieval-augmented generation (RAG): one injected document can influence unrelated requests.

**机制、状态与控制流。** `When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems` 路由到 `AGENT-RAG`：旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。 唯一知识 owner 为 `AGENT-RAG`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19692v1#S5 — §5 Incremental Systems Architecture`；Evaluation=`https://arxiv.org/html/2606.19692v1#S9 — §9 Systems Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结论限于单向量 cosine 检索、固定 encoder、两个 10 万文档语料和给定攻击；organic hubs 在冻结阈值下大量被标记，targeted single-query、late-interaction、multi-vector 与模型内部投毒未验证。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19692:start -->
Claim boundary：仅 `arXiv:2606.19692v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19692v1#S13 — §13 Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-19692:end -->
<!-- review:SF-2026-ARXIV-2606-19692:end -->

<!-- review:SF-2026-ARXIV-2606-19704:start -->
### 2606.19704 — Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents

**问题与旧路径。** Agent benchmarks are growing fast, but no single benchmark touches more than four or five of the dimensions that deployment exposes.

**机制、状态与控制流。** `Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents` 路由到 `PLATFORM-EVALUATION-SYSTEM`：它不再用单次 aggregate mean 排名决定发布，而要求 evaluation owner 保存 configuration identity，并以 in-sample/OOD rank correlation、judge-independent trajectory verifier 和持久 benchmark transport 判断配置能否外推；旧 leaderboard 可保留为观测列，不能继续拥有 release 决策。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19704v1#S4 — §4 Predictive Validity as the Ranking Criterion`；Evaluation=`https://arxiv.org/html/2606.19704v1#S6 — §6 Implications for Benchmark Design`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 这是基于 AssetOpsBench 与 14 份未同行评审 implementation reports 的 position paper；作者未运行大规模 predictive-validity trial，也未证明十二层正交或排名与真实 incident/override 指标相关。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19704:start -->
Claim boundary：仅 `arXiv:2606.19704v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19704v1#S8 — §Limitations`。
<!-- claim:SF-2026-ARXIV-2606-19704:end -->
<!-- review:SF-2026-ARXIV-2606-19704:end -->

<!-- review:SF-2026-ARXIV-2606-19714:start -->
### 2606.19714 — AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing

**问题与旧路径。** Large language models (LLMs) are increasingly used as judges for open-ended generation, as large-scale human evaluation is often expensive and difficult to scale, yet their preferences remain imperfect proxies for human judgment.

**机制、状态与控制流。** `AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing` 路由到 `PLATFORM-EVALUATION-SYSTEM`：AURA 把 judge trust 作为可更新隐状态：人类只验证 uncertainty 高的 pair，refinement 将已验证的一致性信号传播到其余比较，再更新下一轮采样；evaluation owner 而非 judge 独占抽样、停止和审计轨迹。其代价是传播错误会放大初始偏差，需保留随机抽检和预算耗尽时的原始 judge/human fallback。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19714v1#S4 — §4 Methodology`；Evaluation=`https://arxiv.org/html/2606.19714v1#S6 — §6 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 证据来自 5×640 合成比较与一组真实 pairwise judge 数据；未证明在开放域、judge 分布漂移、非 pairwise 评价或极低 human budget 下仍校准。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19714:start -->
Claim boundary：仅 `arXiv:2606.19714v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19714v1#A5 — §Appendix E Experimental Details`。
<!-- claim:SF-2026-ARXIV-2606-19714:end -->
<!-- review:SF-2026-ARXIV-2606-19714:end -->

<!-- review:SF-2026-ARXIV-2606-19719:start -->
### 2606.19719 — Closing the Calibration Gap in Semantic Caching

**问题与旧路径。** Semantic caching cuts LLM inference costs by serving a cached response to semantically similar queries.

**机制、状态与控制流。** `Closing the Calibration Gap in Semantic Caching` 路由到 `AGENT-RAG`：语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。 唯一知识 owner 为 `AGENT-RAG`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19719v1#S3 — §3 Cache-Aware Metrics`；Evaluation=`https://arxiv.org/html/2606.19719v1#S4 — §4 Experimental Setup and §5 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 74,265 个英文 pair、45% 正例、9 个 bi-encoder/reranker 的结果受 ParaBank2 与合成数据占比、标签噪声及部署先验约束；固定 test mix 不证明低重复率生产流量。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19719:start -->
Claim boundary：仅 `arXiv:2606.19719v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19719v1#A2.SS4 — §Appendix B.4 Quality Considerations and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-19719:end -->
<!-- review:SF-2026-ARXIV-2606-19719:end -->

<!-- review:SF-2026-ARXIV-2606-19746:start -->
### 2606.19746 — SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL

**问题与旧路径。** The scaling of LLMs toward long-context inference has shifted the primary serving system bottleneck from computation to memory capacity.

**机制、状态与控制流。** `SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL` 路由到 `INFER-KV-CACHE`：dense-attention 时代的 RDMA 全 prefix 搬运被改为 CXL cache-line top-k 按需读取：prefill 把 KV 写入共享池，scheduler 按设备分配请求，decode GPU 只取 sparse attention 选中的条目；KV owner 从单 GPU/整块传输变成 CXL pool 与调度器协同。失败时仍需本地 DRAM/RDMA 路径，代价是 CXL 拓扑、细粒度访问和设备争用。 唯一知识 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19746v1#S4 — §4 System Design`；Evaluation=`https://arxiv.org/html/2606.19746v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证 DeepSeek-V3.2 AWQ4、SGLang/HiSparse、8×H20、2TB CXL、16K–128K/1K 输出；RDMA 是本机 loopback 的理想化基线，不能证明跨机、dense attention 或其它 CXL 设备收益。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19746:start -->
Claim boundary：仅 `arXiv:2606.19746v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19746v1#S6 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-19746:end -->
<!-- review:SF-2026-ARXIV-2606-19746:end -->

<!-- review:SF-2026-ARXIV-2606-19753:start -->
### 2606.19753 — Grounded Inference: Principles for Deterministically Encapsulated Generative Models

**问题与旧路径。** The incorporation of generative models into traditional computational systems presents both enormous opportunity and tremendous peril.

**机制、状态与控制流。** `Grounded Inference: Principles for Deterministically Encapsulated Generative Models` 路由到 `PLATFORM-PRODUCTION`：该文把概率模型封装为受类型化输入、可验证输出、超时/失败状态和确定性 orchestration 约束的组件，主程序保留状态与最终 authority；但它是架构原则而非新的可复算实现，作为现有 grounded-inference 原则的补充而不追加 Books 机制。 唯一知识 owner 为 `PLATFORM-PRODUCTION`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19753v1#S2 — §2 Grounded Inference Primitives`；Evaluation=`https://arxiv.org/html/2606.19753v1#S5 — §5 Reference Architecture`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 没有公开 workload、实现 artifact 或对照实验；四个 primitive 与两个 anti-pattern 未被量化验证，不能据此声称确定性、可靠性或生产风险已经闭合。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19753:start -->
Claim boundary：仅 `arXiv:2606.19753v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19753v1#S7 — §7 Generative Model Risks`。
<!-- claim:SF-2026-ARXIV-2606-19753:end -->
<!-- review:SF-2026-ARXIV-2606-19753:end -->

<!-- review:SF-2026-ARXIV-2606-19755:start -->
### 2606.19755 — SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling

**问题与旧路径。** Speculative inference accelerates large language model (LLM) decoding but provides no inherent safety guarantees.

**机制、状态与控制流。** `SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling` 路由到 `INFER-SPECULATIVE-DECODING`：SafeSpec 将安全 head 并入 target verification 的同一次前向：draft token 通过语义与风险联合门，风险触发 rollback 和 safety-guided multi-sampling，而非在 speculative path 外串联 guard。target verifier 持有 accept/rollback 控制；外部 guard 仍作为未知攻击与 head 故障 fallback。 唯一知识 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19755v1#S3 — §3 Methodology`；Evaluation=`https://arxiv.org/html/2606.19755v1#S4 — §4 Experiments and §5 Ablation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 15% ASR 降幅与 2.06× benign speedup 绑定 Qwen3-32B、论文所列攻击集和 6×A800；latent head 不能证明新型 jailbreak、跨语言或 target/draft 变更后仍校准。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19755:start -->
Claim boundary：仅 `arXiv:2606.19755v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19755v1#A1 — §Appendix A Experimental Setup and Safety Head`。
<!-- claim:SF-2026-ARXIV-2606-19755:end -->
<!-- review:SF-2026-ARXIV-2606-19755:end -->

<!-- review:SF-2026-ARXIV-2606-19758:start -->
### 2606.19758 — SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design

**问题与旧路径。** Existing graph-based multi-agent system (MAS) designers mainly improve collaboration by optimizing communication topologies over predefined agents, roles, or groups.

**机制、状态与控制流。** `SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design` 路由到 `AGENT-MULTI-AGENT`：SIGMA 不把 agent node 当封闭角色，而由任务到 skill-agent incidence matrix 组合节点，再解码通信图；skill mailbox 拥有消息路由，缺 skill 或组合退化时回落到预定义 agent/topology。代价是库质量、组合搜索和 mailbox 隔离成为新的控制面。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19758v1#S4 — §4 Methodology`；Evaluation=`https://arxiv.org/html/2606.19758v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果仅覆盖六个 reasoning/coding benchmark、三个 base LLM 和论文 skill libraries；0.96-point unseen-library drop 不证明开放技能供应链、权限隔离或长任务稳定性。 Artifact=`https://anonymous.4open.science/r/SIGMA-2338/ — code artifact disclosed by arXiv:2606.19758v1`。

<!-- claim:SF-2026-ARXIV-2606-19758:start -->
Claim boundary：仅 `arXiv:2606.19758v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19758v1#A3 — §Appendix C Fallback Routing`。
<!-- claim:SF-2026-ARXIV-2606-19758:end -->
<!-- review:SF-2026-ARXIV-2606-19758:end -->

<!-- review:SF-2026-ARXIV-2606-19769:start -->
### 2606.19769 — Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI

**问题与旧路径。** The scalability of humanoid robots will depend not only on models and hardware, but also on whether physical experience can accumulate across robots, tasks, organizations, and time.

**机制、状态与控制流。** `Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI` 路由到 `MULTIMODAL-EMBODIED-VLA`：它把 humanoid 数据 owner 从孤立样本仓库提升为 lifecycle contract：每条经验绑定 body/action/task/scene/trace/outcome，并保留时间、坐标系、标定、运动学、单位、版本和 provenance；capability-specific schema 在水平标准之上扩展，旧数据只能经显式兼容层进入训练。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19769v1#S5 — §V Data Standards as Infrastructure`；Evaluation=`https://arxiv.org/html/2606.19769v1#S6 — §VI Implementation Priorities`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 材料源于 ISO/WD 26264-1 制定经验而非完成标准或跨厂商 benchmark；未证明提议字段足以消除硬件差异、隐私/IP 限制和 sim-to-real 偏移。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19769:start -->
Claim boundary：仅 `arXiv:2606.19769v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19769v1#S4 — §IV Why More Data Is Not Enough`。
<!-- claim:SF-2026-ARXIV-2606-19769:end -->
<!-- review:SF-2026-ARXIV-2606-19769:end -->

<!-- review:SF-2026-ARXIV-2606-19795:start -->
### 2606.19795 — Agentic Electronic Design Automation: A Handoff Perspective

**问题与旧路径。** Electronic design automation (EDA) is inherently multi-stage and handoff-heavy.

**机制、状态与控制流。** `Agentic Electronic Design Automation: A Handoff Perspective` 路由到 `AGENT-WORKFLOW`：EDA agent handoff 从传文件/自然语言升级为 consumer-defined acceptance contract：artifact 连同 scope、evidence、provenance、authority 和 workflow state 传递，下一 stage 显式 accept/reject；EACP 分离 discovery、message、tool、workflow 与 security/IP 层。旧 stage-local check 共存，但不能替代跨边界交付证据。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19795v1#S3 — §3 Handoff Contracts, Objects, and Coordination`；Evaluation=`https://arxiv.org/html/2606.19795v1#S6 — §6 Unified Handoff Protocol`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 这是 82 个系统的 survey/protocol proposal，没有端到端 EACP 实现或 signoff benchmark；五层协议未证明能覆盖供应链 IP、工具副作用和组织级授权。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19795:start -->
Claim boundary：仅 `arXiv:2606.19795v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19795v1#S1.SS2 — §1.2 Limitations of Existing Surveys and §1.3 Scope`。
<!-- claim:SF-2026-ARXIV-2606-19795:end -->
<!-- review:SF-2026-ARXIV-2606-19795:end -->

<!-- review:SF-2026-ARXIV-2606-19803:start -->
### 2606.19803 — Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases

**问题与旧路径。** Vector databases are increasingly used in security sensitive contexts with Retrieval Augmented Generation and organizational AI pipelines; however, their security capabilities remain limited.

**机制、状态与控制流。** `Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases` 路由到 `PLATFORM-SECURITY`：向量检索不再先 ANN 后应用层过滤，而把 subject/object/policy 与 approximate candidate generation 共同求解；policy engine 拥有可见集合，ANN 只在授权候选内优化 recall/latency。pre/post-filter 可作为规模与索引能力不同的共存路径，但必须分别报告漏检和越权风险。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19803v1#S2 — §2 FGAC Policy Model`；Evaluation=`https://arxiv.org/html/2606.19803v1#S4 — §4 Preliminary Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 论文仅给 formal model 与 preliminary experiments；未覆盖动态 policy、跨租户缓存、删除一致性或所有向量数据库实现，不能宣称 FGAC 与 ANN recall 已同时普适最优。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19803:start -->
Claim boundary：仅 `arXiv:2606.19803v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19803v1#S5 — §5 Discussion and §6 Future Work`。
<!-- claim:SF-2026-ARXIV-2606-19803:end -->
<!-- review:SF-2026-ARXIV-2606-19803:end -->

<!-- review:SF-2026-ARXIV-2606-19808:start -->
### 2606.19808 — Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning

**问题与旧路径。** Test-time reasoning is increasingly used as a serving-time control knob, but extra reasoning is not uniformly valuable: it can repair failed attempts, waste compute on already-correct answers, or introduce harmful answer changes.

**机制、状态与控制流。** `Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning` 路由到 `INFER-SCHEDULING`：SEVRA 把额外推理视为 serving allocation：冻结 solver 先产出 attempt，recoverability gate 决定保留、验证或 bounded retry；scheduler 拥有 token budget 和 harmful-flip 审计。较长 initial budget 在部分任务更优，因此 controller 必须与 no-verify/longer-solve 路径共存。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19808v1#S4 — §4 Selective Verification Method`；Evaluation=`https://arxiv.org/html/2606.19808v1#S5 — §5 Experimental Setup and §6 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 76.3%/26.8% 与 transfer 数字限于 Qwen3-4B、MATH500/GSM8K/CommonsenseQA 和给定 token budgets；不证明 gate 在新模型、开放题或负载漂移下优于先增加初始预算。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19808:start -->
Claim boundary：仅 `arXiv:2606.19808v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19808v1#A10 — §Appendix J Limitations and Deployment Considerations`。
<!-- claim:SF-2026-ARXIV-2606-19808:end -->
<!-- review:SF-2026-ARXIV-2606-19808:end -->

<!-- review:SF-2026-ARXIV-2606-19847:start -->
### 2606.19847 — AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts

**问题与旧路径。** Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions.

**机制、状态与控制流。** `AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts` 路由到 `AGENT-MEMORY`：AtomMem 以 Fact Executor 将长对话压成高价值 atomic facts，按事件层次与 temporal profile 演化，并由 associative graph 在查询时联结；memory owner 控制 extract/update/retrieve，原始对话保留为冲突校验 fallback。代价是事实抽取错误、属性覆盖和图扩散会造成不可逆记忆漂移。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19847v1#S3 — §3 AtomMem Methods`；Evaluation=`https://arxiv.org/html/2606.19847v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只在 LoCoMo 的多类 reasoning 指标上比较；未证明真实多会话隐私、删除、冲突事实、跨语言或长期 profile 更新正确。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19847:start -->
Claim boundary：仅 `arXiv:2606.19847v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19847v1#S5 — §5 Conclusion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-19847:end -->
<!-- review:SF-2026-ARXIV-2606-19847:end -->

<!-- review:SF-2026-ARXIV-2606-19849:start -->
### 2606.19849 — ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference

**问题与旧路径。** Streaming VideoLLMs must continuously process incoming video while maintaining low query latency, making both video-ingestion throughput and query-time responsiveness critical for real-time deployment.

**机制、状态与控制流。** `ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference` 路由到 `INFER-SCHEDULING`：ViCoStream 将 video preprocessing、encoder、token drop、prefill/decode 统一到 chunk scheduler，以 CUDA-stream overlap、bounded visual attention 和 query retrieval 控制每 chunk 计算/内存；调度器拥有 stage backpressure，降载时通过 token retention/attention scope 回退，而非让单模块各自最大化。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19849v1#S3 — §3 Stage-Wise Coordinated Streaming`；Evaluation=`https://arxiv.org/html/2606.19849v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 134 FPS 与 <50 ms TTFT 仅对应 Qwen2.5-VL-3B/7B、单 A100 和论文 streaming benchmarks；精度接近 full-history 不证明长时依赖、并发请求或其它 GPU。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19849:start -->
Claim boundary：仅 `arXiv:2606.19849v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19849v1#S5 — §5 Accuracy-Latency and Resource-Constrained Parallelism`。
<!-- claim:SF-2026-ARXIV-2606-19849:end -->
<!-- review:SF-2026-ARXIV-2606-19849:end -->

<!-- review:SF-2026-ARXIV-2606-19868:start -->
### 2606.19868 — A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models

**问题与旧路径。** Although large language models (LLMs) have shown strong capabilities across a wide range of tasks, their outputs often remain unreliable and may contain hallucinations, making uncertainty estimation (UE) essential for building trustworthy LLMs.

**机制、状态与控制流。** `A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models` 路由到 `PLATFORM-EVALUATION-SYSTEM`：统一框架把 black-box UE 的 verbalization、sampling、explanation、multi-agent 与 hybrid 信号放到同一 evaluator contract；但 24 方法无单一 winner，现有评测章已包含按 task/calibration 选择 UE 的原则，因此记为 No Change。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19868v1#S3 — §III Uncertainty-Estimation Taxonomy`；Evaluation=`https://arxiv.org/html/2606.19868v1#S4 — §IV Experimental Setup`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 24 方法×4 模型×4 数据设置不能证明跨 API 版本、开放生成或成本约束下的统一最优；answer-space/hybrid 优势是设置相关观察。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19868:start -->
Claim boundary：仅 `arXiv:2606.19868v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19868v1#S6 — §VI Conclusion and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-19868:end -->
<!-- review:SF-2026-ARXIV-2606-19868:end -->

<!-- review:SF-2026-ARXIV-2606-19887:start -->
### 2606.19887 — FinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming

**问题与旧路径。** Existing safety benchmarks target general adversarial scenarios but miss finance-specific risks.

**机制、状态与控制流。** `FinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming` 路由到 `PLATFORM-EVALUATION-SYSTEM`：FinRED 用专家 taxonomy 生成金融 red-team 样例并由专家复核标签/可靠性，属于现有 domain-specific evaluation pipeline 的实例；它未改变通用 release owner，故只作 No Change handoff。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19887v1#S3 — §III FinRED Framework`；Evaluation=`https://arxiv.org/html/2606.19887v1#S4 — §IV Experiments and §V Expert Validation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 专家一致性和覆盖只适用于论文金融风险 taxonomy、模型与样本；未证明其它司法辖区、实时市场或非金融安全域。 Artifact=`https://github.com/selectstar-ai/FinRED-paper; https://huggingface.co/datasets/datumo/FinRED — code and dataset artifacts disclosed by arXiv:2606.19887v1`。

<!-- claim:SF-2026-ARXIV-2606-19887:start -->
Claim boundary：仅 `arXiv:2606.19887v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19887v1#S6 — §VI Reliability and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-19887:end -->
<!-- review:SF-2026-ARXIV-2606-19887:end -->

<!-- review:SF-2026-ARXIV-2606-19898:start -->
### 2606.19898 — Query-aware Routing for Filtered Approximate Nearest Neighbors Search

**问题与旧路径。** Filtered ANN search, which combines vector similarity with attribute predicates, is a core primitive in modern vector databases and retrieval-augmented generation.

**机制、状态与控制流。** `Query-aware Routing for Filtered Approximate Nearest Neighbors Search` 路由到 `AGENT-RAG`：filtered ANN 从静态单索引选择变为 query-aware router：规则或 learned policy 依据 filter selectivity/shape 将查询送往不同索引路径；router 拥有 plan choice，监测失配时回落到精确过滤或保守规则。代价是训练分布漂移会把 latency 优化变成 recall 回归。 唯一知识 owner 为 `AGENT-RAG`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19898v1#S3 — §3 Rule-Based Router and §4 ML Router`；Evaluation=`https://arxiv.org/html/2606.19898v1#S6 — §6 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验绑定论文数据分布、filter 模式、索引实现和 recall/latency 指标；未证明动态更新、复杂布尔 policy 或跨 tenant workload。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19898:start -->
Claim boundary：仅 `arXiv:2606.19898v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19898v1#S7 — §7 Conclusion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-19898:end -->
<!-- review:SF-2026-ARXIV-2606-19898:end -->

<!-- review:SF-2026-ARXIV-2606-19899:start -->
### 2606.19899 — Measuring Biological Capabilities and Risks of AI Agents

**问题与旧路径。** This paper addresses a rapidly emerging policy challenge: how to generate and interpret credible evidence about the biological capabilities and risks of AI scientists, or agentic AI systems capable of autonomously or collaboratively performing multi-step scientific tasks.

**机制、状态与控制流。** `Measuring Biological Capabilities and Risks of AI Agents` 路由到 `PLATFORM-EVALUATION-SYSTEM`：该工作把生物能力/风险拆为可操作 task suites、agent scaffold 与分级 risk interpretation，但仍属于垂直 benchmark；现有 evaluation 章节已要求 domain expert、capability 与 misuse 分离，故不新增机制。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/pdf/2606.19899v1#page=9 — §PDF pp.9–15 Capability-Evaluation Methods`；Evaluation=`https://arxiv.org/pdf/2606.19899v1#page=16 — §PDF pp.16–26 Evaluation Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** PDF 评测不能把受测 agent 的实验室能力直接外推为现实生物危害；任务覆盖、工具 access、专家评分和风险阈值均是特定设计。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19899:start -->
Claim boundary：仅 `arXiv:2606.19899v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/pdf/2606.19899v1#page=28 — §PDF pp.28–30 Limitations and Risk Interpretation`。
<!-- claim:SF-2026-ARXIV-2606-19899:end -->
<!-- review:SF-2026-ARXIV-2606-19899:end -->

<!-- review:SF-2026-ARXIV-2606-19911:start -->
### 2606.19911 — Multi-Agent Transactive Memory

**问题与旧路径。** The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations.

**机制、状态与控制流。** `Multi-Agent Transactive Memory` 路由到 `AGENT-MEMORY`：多 agent 记忆从各自 transcript 变为 transactive directory：agent 保存谁知道什么与证据位置，查询先路由到 memory owner 再取内容；目录过期时回落到广播/共享检索。其收益以额外索引维护、错误 expertise attribution 和隐私边界为代价。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19911v1#S3 — §3 Multi-Agent Transactive Memory`；Evaluation=`https://arxiv.org/html/2606.19911v1#S4 — §4 Experimental Setup and §5 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只在论文 multi-agent tasks、拓扑和模型上验证；未证明目录在 agent churn、对抗写入、跨组织权限或长期知识漂移下可靠。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19911:start -->
Claim boundary：仅 `arXiv:2606.19911v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19911v1#S6 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-19911:end -->
<!-- review:SF-2026-ARXIV-2606-19911:end -->

<!-- review:SF-2026-ARXIV-2606-19989:start -->
### 2606.19989 — Online Dynamic Batching with Formal Guarantees for LLM Training

**问题与旧路径。** Modern LLM training breaks a core assumption behind offline batch samplers: the true training cost of a sample is only observable after preprocessing, augmentation, templating, tokenization, and multimodal visual-token expansion.

**机制、状态与控制流。** `Online Dynamic Batching with Formal Guarantees for LLM Training` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：训练 batching 从离线固定 batch 改为 online queue policy，在到达、长度与资源状态变化时决定组合，同时以形式化界约束等待/效率；scheduler 拥有 batch formation，超出假设时退回静态 bucket。代价是在线估计误差与公平性。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19989v1#S2 — §2 Online Dynamic Batching System Design`；Evaluation=`https://arxiv.org/html/2606.19989v1#S4 — §4 Experimental Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 形式保证依赖论文到达与成本模型；未证明真实多租户数据 loader、straggler、网络/optimizer 状态或非平稳长度分布满足假设。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19989:start -->
Claim boundary：仅 `arXiv:2606.19989v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19989v1#S5 — §5 Scope and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-19989:end -->
<!-- review:SF-2026-ARXIV-2606-19989:end -->

<!-- review:SF-2026-ARXIV-2606-19992:start -->
### 2606.19992 — Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services

**问题与旧路径。** In the agentic web era, LLM-based agents increasingly invoke web services as tools, yet most interfaces remain \emph{static endpoints} that poorly express long-horizon workflows with loops, conditionals, joins, and retries.

**机制、状态与控制流。** `Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services` 路由到 `AGENT-MCP`：Tool Programs 将静态 endpoint 列表变成可组合、带类型与执行语义的服务接口；服务端拥有 program validation/sandbox，agent 只提交受限程序，失败时回落到单步 endpoint。灵活性以验证复杂度、资源上界和更大的代码注入面为代价。 唯一知识 owner 为 `AGENT-MCP`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19992v1#S3 — §3 ToolPro Design`；Evaluation=`https://arxiv.org/html/2606.19992v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验只覆盖作者 web-service/tool tasks；未证明任意第三方 API、副作用事务、认证轮换或不可信程序可安全执行。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19992:start -->
Claim boundary：仅 `arXiv:2606.19992v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19992v1#S5 — §5 Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-19992:end -->
<!-- review:SF-2026-ARXIV-2606-19992:end -->

<!-- review:SF-2026-ARXIV-2606-19998:start -->
### 2606.19998 — Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory

**问题与旧路径。** Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet they remain black boxes whose physical interactions can cause irreversible harm, making generalizable and interpretable failure detection essential.

**机制、状态与控制流。** `Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory` 路由到 `MULTIMODAL-EMBODIED-VLA`：Tri-Info 用 VLA 内部 information signals 预测 action failure，并把 abstain/fallback 交给执行控制器；旧做法只看 action likelihood 或单一 uncertainty。代价是 probe 与阈值需随 policy/environment 校准，未知 shift 时回落到人工/安全 controller。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19998v1#S3 — §3 Tri-Info Method`；Evaluation=`https://arxiv.org/html/2606.19998v1#S4 — §4 Experimental Setup and §5 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只在论文 VLA 模型、任务与 failure labels 上验证；离线 AUROC/检测率不证明真实机器人动作安全、因果故障或跨 embodiment 泛化。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-19998:start -->
Claim boundary：仅 `arXiv:2606.19998v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19998v1#S5.SS4 — §5.4 Conclusion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-19998:end -->
<!-- review:SF-2026-ARXIV-2606-19998:end -->

<!-- review:SF-2026-ARXIV-2606-20002:start -->
### 2606.20002 — Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning

**问题与旧路径。** This work presents a general framework for training large language models (LLMs) to "Connect the Dots" (CoD), a meta-capability required by long-lifecycle agents: as an LLM-based AI agent gets deployed in an environment, it solves a long sequence of tasks while continuously exploring the environment, learning from its own experiences, and iteratively self-updating its context about the environment, thereby achieving progressively better performance on future tasks conditioned on the updated context.

**机制、状态与控制流。** `Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning` 路由到 `TRAIN-RLHF`：Connect-the-Dots 用跨 domain、跨 lifecycle 的 RL trajectory 把短任务 reward 改为长期 agent state transition 信号；trainer 拥有 curriculum、reward 与 checkpoint selection，旧单域 SFT/RL 作为稳定初始化。代价是跨域 reward leakage 和 credit assignment，失败时需回退到分域训练/验证。 唯一知识 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20002v1#S2 — §2 Connect-the-Dots Framework`；Evaluation=`https://arxiv.org/html/2606.20002v1#S3 — §3 Implementations and Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果限于 exact-v1 domains、模型、reward verifier 和 rollout budget；未证明开放世界长期记忆、真实工具副作用或跨生命周期泛化。 Artifact=`https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod/examples/research_cod — implementation disclosed by arXiv:2606.20002v1`。

<!-- claim:SF-2026-ARXIV-2606-20002:start -->
Claim boundary：仅 `arXiv:2606.20002v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20002v1#S4 — §4 Analysis and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20002:end -->
<!-- review:SF-2026-ARXIV-2606-20002:end -->

<!-- review:SF-2026-ARXIV-2606-20005:start -->
### 2606.20005 — StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation

**问题与旧路径。** Attention distillation, which trains one attention distribution to match another by minimizing their Kullback-Leibler (KL) divergence, is widely used in knowledge distillation, model compression, continual learning, and sparse-attention LLM training.

**机制、状态与控制流。** `StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：StreamKL 将 attention distillation 的 KL 计算分块流式执行，避免物化完整概率张量；kernel/trainer 共同拥有 block state 与数值归约，OOM 或不支持 shape 时回退到标准 KL。速度/显存换来额外 kernel、归约误差和硬件依赖。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20005v1#S3 — §3 StreamKL Forward/Backward Pass`；Evaluation=`https://arxiv.org/html/2606.20005v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证论文 attention shapes、精度、模型与 GPU；未证明所有 vocab/sequence 规模、分布式并行或低精度下保持相同数值和收敛。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20005:start -->
Claim boundary：仅 `arXiv:2606.20005v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20005v1#S6 — §6 Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-20005:end -->
<!-- review:SF-2026-ARXIV-2606-20005:end -->

<!-- review:SF-2026-ARXIV-2606-20023:start -->
### 2606.20023 — When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents

**问题与旧路径。** As LLM agents increasingly select tools autonomously, their choices among tools with different privileges become safety-relevant.

**机制、状态与控制流。** `When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents` 路由到 `AGENT-TOOL-CALLING`：工具选择不再只优化成功率，而先求满足任务的最小 capability set；planner 提议工具，policy layer 比较 privilege lattice 后降权/拒绝 over-privileged choice，并保留必要时显式 escalation。代价是 capability annotation 不全会误拒绝或低估组合权限。 唯一知识 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20023v1#S2 — §2 Privilege Model and Selection Analysis`；Evaluation=`https://arxiv.org/html/2606.20023v1#S3 — §3 Evaluation Setup and §4 Empirical Analysis`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 测量与 mitigation 绑定论文 agent/tool suites 和 privilege labels；未证明动态 OAuth scope、跨工具权限合成或恶意 metadata。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20023:start -->
Claim boundary：仅 `arXiv:2606.20023v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20023v1#S5 — §5 Mitigation and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20023:end -->
<!-- review:SF-2026-ARXIV-2606-20023:end -->

<!-- review:SF-2026-ARXIV-2606-20047:start -->
### 2606.20047 — PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents

**问题与旧路径。** Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously.

**机制、状态与控制流。** `PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents` 路由到 `AGENT-CONTEXT`：PACMS 把 context assembly 表述为预算约束 submodular selection：独立 engine 根据 relevance、coverage 与 redundancy 选取片段，agent 消费带 provenance 的 context；不足时回落到更大窗口或检索重试。代价是 utility surrogate 可能遗漏依赖和顺序。 唯一知识 owner 为 `AGENT-CONTEXT`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20047v1#S3 — §3 PACMS System Design`；Evaluation=`https://arxiv.org/html/2606.20047v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 评测限于论文任务、预算、retriever 与 utility 定义；submodular 近似不证明长依赖、冲突证据或对抗 context 下答案正确。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20047:start -->
Claim boundary：仅 `arXiv:2606.20047v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20047v1#S5.SS2 — §5.2 Scope and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20047:end -->
<!-- review:SF-2026-ARXIV-2606-20047:end -->

<!-- review:SF-2026-ARXIV-2606-20113:start -->
### 2606.20113 — When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation

**问题与旧路径。** Streaming Retrieval-Augmented Generation (Streaming RAG) hides tool latency by issuing retrieval queries in parallel with the user's still-arriving input, before the utterance is complete.

**机制、状态与控制流。** `When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation` 路由到 `AGENT-TOOL-CALLING`：streaming tool use 不应在第一个 token 触发；controller 追踪 tool-intent 随解码的稳定度，在置信轨迹达到阈值后才 dispatch，未稳定则继续生成或回落到完整 query。它用 latency 换误调用率，并要求 cancellation/duplicate suppression。 唯一知识 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20113v1#S3 — §3 Problem Formalization and Stabilization Controller`；Evaluation=`https://arxiv.org/html/2606.20113v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 稳定阈值与收益只在论文 retrieval tasks、模型、网络延迟和工具集上测得；未证明有副作用工具、长参数或分布漂移。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20113:start -->
Claim boundary：仅 `arXiv:2606.20113v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20113v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20113:end -->
<!-- review:SF-2026-ARXIV-2606-20113:end -->

<!-- review:SF-2026-ARXIV-2606-20122:start -->
### 2606.20122 — ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research

**问题与旧路径。** Open-ended deep research (OEDR) requires systems to acquire knowledge through multi-round retrieval and generate coherent long-form reports.

**机制、状态与控制流。** `ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research` 路由到 `AGENT-PLANNING`：ScaffoldAgent 将 deep-research outline 变成可迭代控制状态：每轮按预期 utility 增删/重排子目标，再据证据覆盖继续搜索；planner 拥有 outline version，budget 用尽则冻结当前结构并交给 verifier。代价是 utility 估计会偏向易检索证据。 唯一知识 owner 为 `AGENT-PLANNING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20122v1#S4 — §4 Utility-Guided Dynamic Outline Optimization`；Evaluation=`https://arxiv.org/html/2606.20122v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验仅覆盖论文开放研究任务、搜索后端和 judge；未证明 factuality、source authority、长时间网页漂移或真实研究验收。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20122:start -->
Claim boundary：仅 `arXiv:2606.20122v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20122v1#S6 — §6 Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-20122:end -->
<!-- review:SF-2026-ARXIV-2606-20122:end -->

<!-- review:SF-2026-ARXIV-2606-20128:start -->
### 2606.20128 — The Correctness Illusion in LLM-Generated GPU Kernels

**问题与旧路径。** Benchmarks for LLM-generated GPU kernels (KernelBench, TritonBench, GEAK) score correctness through fixed-shape, small-sample allclose-style checks.

**机制、状态与控制流。** `The Correctness Illusion in LLM-Generated GPU Kernels` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：GPU kernel 验收从单设备单输入通过改为 CPU oracle、跨 shape/dtype/GPU differential testing 与 clean controls；release owner 保存失败 witness，并在 verdict 不一致时拒绝上线或回退原 kernel。代价是 oracle/设备矩阵成本和未覆盖输入。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20128v1#S3 — §3 Differential Correctness Method`；Evaluation=`https://arxiv.org/html/2606.20128v1#S4 — §4 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 24/26 ops 与 RTX3060/A10/L40S/A100/H100 的测试仍不穷尽未定义行为、驱动版本、并发或大模型端到端性能。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20128:start -->
Claim boundary：仅 `arXiv:2606.20128v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20128v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20128:end -->
<!-- review:SF-2026-ARXIV-2606-20128:end -->

<!-- review:SF-2026-ARXIV-2606-20158:start -->
### 2606.20158 — N-Version Programming with Coding Agents

**问题与旧路径。** This paper revisits the classical concept on N-version programming in the setting of contemporary AI coding agents.

**机制、状态与控制流。** `N-Version Programming with Coding Agents` 路由到 `AGENT-WORKFLOW`：N-version coding agents 并行产出独立实现，由测试/静态检查和 adjudicator 汇合，而非信任单次生成；workflow owner 管理 diversity、quorum 与 fallback 到人工。额外 token/latency 的收益依赖故障独立性，相关 hallucination 会击穿多数表决。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20158v1#S2 — §II N-Version Coding-Agent Architecture`；Evaluation=`https://arxiv.org/html/2606.20158v1#S3 — §III Experimental Methodology and §IV Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果只覆盖论文 coding tasks、agent versions 与 test suites；未证明安全漏洞、缺失 oracle、共享训练数据导致的相关错误。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20158:start -->
Claim boundary：仅 `arXiv:2606.20158v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20158v1#S5 — §V Threats to Validity`。
<!-- claim:SF-2026-ARXIV-2606-20158:end -->
<!-- review:SF-2026-ARXIV-2606-20158:end -->

<!-- review:SF-2026-ARXIV-2606-20235:start -->
### 2606.20235 — ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments

**问题与旧路径。** Academic paper search is a core step in scientific research, and LLM-based search agents are emerging as a promising paradigm for iterative, intent-driven literature exploration.

**机制、状态与控制流。** `ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments` 路由到 `PLATFORM-EVALUATION-SYSTEM`：ScholarQuest 提供 taxonomy-guided academic-search benchmark，但没有改变 evaluation/release 控制权或现有 paper-search owner，因此不追加 Books。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20235v1#S3 — §3 ScholarQuest Construction`；Evaluation=`https://arxiv.org/html/2606.20235v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** benchmark 覆盖开放文献环境与既定 taxonomy；分数不证明封闭数据库、未来索引、全文权限或科研结论正确。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20235:start -->
Claim boundary：仅 `arXiv:2606.20235v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20235v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20235:end -->
<!-- review:SF-2026-ARXIV-2606-20235:end -->

<!-- review:SF-2026-ARXIV-2606-20243:start -->
### 2606.20243 — Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs

**问题与旧路径。** We present Phoenix, a multi-agent LLM system that resolves GitHub issues from triage through pull-request creation, combining seven layered safety controls with a baseline-aware test evaluation strategy.

**机制、状态与控制流。** `Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs` 路由到 `AGENT-WORKFLOW`：Phoenix 的 multi-agent issue-resolution safety pipeline 已被 workflow 章的隔离执行、review gate 与 rollback 原则覆盖；本日只保留实现 handoff，不重复 owner。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20243v1#S3 — §III Phoenix System Architecture`；Evaluation=`https://arxiv.org/html/2606.20243v1#S4 — §IV Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** GitHub issues、repositories、tests 与 agent 配置是特定实验；测试通过不证明 supply-chain、secret、部署或未测试行为安全。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20243:start -->
Claim boundary：仅 `arXiv:2606.20243v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20243v1#S5 — §V Discussion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20243:end -->
<!-- review:SF-2026-ARXIV-2606-20243:end -->

<!-- review:SF-2026-ARXIV-2606-20245:start -->
### 2606.20245 — Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference

**问题与旧路径。** Large language models (LLMs) have achieved strong performance across a wide range of language-based tasks by leveraging both extensive parametric knowledge and in-context learning ability, enabling them to incorporate external information provided in the input prompt.

**机制、状态与控制流。** `Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference` 路由到 `AGENT-CONTEXT`：显式 parametric/context knowledge conflict resolution 属于现有 context provenance 与冲突裁决路径；该研究没有新增跨系统 state owner，故 No Change。 唯一知识 owner 为 `AGENT-CONTEXT`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20245v1#S3 — §III Explicit Knowledge-Conflict Methodology`；Evaluation=`https://arxiv.org/html/2606.20245v1#S4 — §IV Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验只验证给定冲突构造、模型和问答集；显式选择不能证明来源真实性、时效性或隐式冲突被发现。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20245:start -->
Claim boundary：仅 `arXiv:2606.20245v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20245v1#S5 — §V Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20245:end -->
<!-- review:SF-2026-ARXIV-2606-20245:end -->

<!-- review:SF-2026-ARXIV-2606-20254:start -->
### 2606.20254 — Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic

**问题与旧路径。** Model quantization is widely adopted to reduce memory usage and inference cost when deploying deep neural networks on resource-constrained devices.

**机制、状态与控制流。** `Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic` 路由到 `PLATFORM-SECURITY`：量化不再被当作纯压缩步骤：security owner 将 quantization-conditioned backdoor 视作可分离 task vector，在发布前比较全精度/量化行为并用 task arithmetic 移除，再做 clean/attack 双验收。无法分离时回退到拒绝量化模型。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20254v1#S4 — §4 Threat Model and §5 Task-Arithmetic Removal`；Evaluation=`https://arxiv.org/html/2606.20254v1#S6 — §6 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 移除效果限于论文 backdoor construction、模型、bit-width 与 calibration data；未证明未知触发器、其它量化器或 task-vector subtraction 不损害能力。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20254:start -->
Claim boundary：仅 `arXiv:2606.20254v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20254v1#S7 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20254:end -->
<!-- review:SF-2026-ARXIV-2606-20254:end -->

<!-- review:SF-2026-ARXIV-2606-20318:start -->
### 2606.20318 — AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads

**问题与旧路径。** Configuration tuning is critical to database performance but remains difficult in real deployments.

**机制、状态与控制流。** `AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads` 路由到 `PLATFORM-PRODUCTION`：AgenticDB 将数据库 reconfiguration 变成 telemetry→proposal→sandbox evaluation→guarded apply→rollback 的闭环；DB control plane 而非 LLM 持有变更权限和状态版本。代价是试验流量与错误 cost model，fallback 为上一配置和人工 approval。 唯一知识 owner 为 `PLATFORM-PRODUCTION`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20318v1#S4 — §4 AgenticDB Design`；Evaluation=`https://arxiv.org/html/2606.20318v1#S5 — §5 Evaluation Methodology and §6 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果绑定论文 workloads、DBMS、动作空间和离线/沙箱指标；未证明生产突发流量、数据迁移、锁竞争或跨版本自动演进安全。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20318:start -->
Claim boundary：仅 `arXiv:2606.20318v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20318v1#S7 — §7 Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-20318:end -->
<!-- review:SF-2026-ARXIV-2606-20318:end -->

<!-- review:SF-2026-ARXIV-2606-20363:start -->
### 2606.20363 — Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining

**问题与旧路径。** Explicit skill libraries make computer-using agents easier to inspect, but it remains unclear whether such libraries can be mined from interaction data in a way that improves downstream policies.

**机制、状态与控制流。** `Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining` 路由到 `AGENT-PLATFORM`：SKILL.md 不再完全手写，而从 computer-use trajectory 中抽取可复用步骤、前置条件和 recovery，经过评测后发布；skill registry 拥有版本/验证，agent 只消费已批准 artifact。错误归纳时回退原 trajectory 或人工 skill。 唯一知识 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20363v1#S4 — §4 Automated SKILL.md Generation`；Evaluation=`https://arxiv.org/html/2606.20363v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验覆盖论文应用、轨迹质量和 computer-use agent；未证明 UI 漂移、敏感动作、跨 OS 或生成 skill 的供应链安全。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20363:start -->
Claim boundary：仅 `arXiv:2606.20363v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20363v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20363:end -->
<!-- review:SF-2026-ARXIV-2606-20363:end -->

<!-- review:SF-2026-ARXIV-2606-20374:start -->
### 2606.20374 — ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters

**问题与旧路径。** Large-scale LLM training requires always-on, fine-grained observability for effective performance diagnosis at scale.

**机制、状态与控制流。** `ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters` 路由到 `PLATFORM-TRACE`：ARGUS 将万卡训练诊断从节点日志提升为跨 rank/collective/network/storage 的统一 trace identity；collector 控制采样与时钟映射，diagnoser 只在证据图上定位瓶颈，超预算时降采样并保留关键 span。代价是 telemetry overhead 与相关性误判。 唯一知识 owner 为 `PLATFORM-TRACE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20374v1#S3 — §3 ARGUS System Overview`；Evaluation=`https://arxiv.org/html/2606.20374v1#S4 — §4 Runtime Monitoring and Diagnosis Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 生产观察来自特定 >10,000-GPU 集群、训练栈和故障集；trace 覆盖与诊断时延不证明因果根因、其它 fabric 或故障自动修复。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20374:start -->
Claim boundary：仅 `arXiv:2606.20374v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20374v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20374:end -->
<!-- review:SF-2026-ARXIV-2606-20374:end -->

<!-- review:SF-2026-ARXIV-2606-20381:start -->
### 2606.20381 — Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe

**问题与旧路径。** FP4 training promises substantial reductions in memory and computation cost for LLM pretraining, yet current FP4 hardware paths and recipes, including NVIDIA Blackwell/Rubin-class systems and AMD MI350-series GPUs, remain centered on E2M1 data elements.

**机制、状态与控制流。** `Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：UFP4 针对 FP4 pretraining 的 shrinkage bias 重新分配量化几何与 scaling，使 optimizer/quantizer 共同拥有低精度状态；异常 loss 时回退 BF16/更高精度。显存/吞吐收益以 recipe、kernel 和收敛敏感性为代价。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20381v1#S4 — §4 UFP4 Recipe`；Evaluation=`https://arxiv.org/html/2606.20381v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只在 exact-v1 模型规模、token budget、FP4 hardware/simulation 与下游评测验证；未证明更长预训练、其它 optimizer 或最终能力无回归。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20381:start -->
Claim boundary：仅 `arXiv:2606.20381v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20381v1#S6 — §6 Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-20381:end -->
<!-- review:SF-2026-ARXIV-2606-20381:end -->

<!-- review:SF-2026-ARXIV-2606-20408:start -->
### 2606.20408 — NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms

**问题与旧路径。** Large language model (LLM) agents are increasingly proposed as supervisory components for safety-critical systems, yet their robustness under sustained, adaptive adversarial pressure remains poorly characterized.

**机制、状态与控制流。** `NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms` 路由到 `PLATFORM-EVALUATION-SYSTEM`：NRT-Bench 将 operator-agent red teaming 组织成多轮控制室状态、攻击轨迹和 safety-critical acceptance，但作为垂直 benchmark 已被通用多轮安全评测契约覆盖，故 No Change。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20408v1#S3 — §3 NRT-Bench Design`；Evaluation=`https://arxiv.org/html/2606.20408v1#S4 — §4 Experimental Setup and Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 任务、模拟控制室、attackers 与 judges 不等同真实基础设施；benchmark 成功/失败不能外推为生产控制权限或事故风险。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20408:start -->
Claim boundary：仅 `arXiv:2606.20408v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20408v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20408:end -->
<!-- review:SF-2026-ARXIV-2606-20408:end -->

<!-- review:SF-2026-ARXIV-2606-20470:start -->
### 2606.20470 — Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems

**问题与旧路径。** Agentic AI systems increasingly rely on language-model components to interpret instructions, process external data, invoke tools, and coordinate with other agents.

**机制、状态与控制流。** `Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems` 路由到 `PLATFORM-SECURITY`：防御不只阻断 model-guided attacker，还可发布受控假信号改变攻击者 belief/update path；defender 拥有 decoy 状态与撤销，真实 agent state 不暴露。代价是误导污染 observability 与合法调试，故必须与直接拒绝、隔离和审计共存。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20470v1#S3 — §III Defense and §IV Misdirection`；Evaluation=`https://arxiv.org/html/2606.20470v1#S5 — §V Simulation Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果来自论文 attack/defense simulation；未证明真实攻击者适应、法律/伦理约束、side channel 或 decoy 不伤害正常 agent。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20470:start -->
Claim boundary：仅 `arXiv:2606.20470v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20470v1#S6 — §VI Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20470:end -->
<!-- review:SF-2026-ARXIV-2606-20470:end -->

<!-- review:SF-2026-ARXIV-2606-20474:start -->
### 2606.20474 — UltraQuant: 4-bit KV Caching for Context-Heavy Agents

**问题与旧路径。** Context-heavy agents place unusual pressure on the key-value (KV) cache: long prefixes are reused across many short turns, while concurrency determines whether the serving system can keep GPUs utilized.

**机制、状态与控制流。** `UltraQuant: 4-bit KV Caching for Context-Heavy Agents` 路由到 `INFER-KV-CACHE`：UltraQuant 将 agent 长上下文 KV 压到 4-bit，并分别控制 token/channel quantization 与 runtime dequant；cache manager 持有 format metadata，质量回归时按 layer/request 回退高精度。收益以 kernel 复杂度、误差累积和 workload sensitivity 为代价。 唯一知识 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20474v1#S4 — §4 Ultra-TurboQuant and §5 UltraQuant`；Evaluation=`https://arxiv.org/html/2606.20474v1#S6 — §6 Accuracy and §7 Systems Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 质量与系统数字限于论文 models、context-heavy agent workloads、长度和 hardware；未证明极长上下文、不同 attention、并发 tail latency 或所有任务无损。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20474:start -->
Claim boundary：仅 `arXiv:2606.20474v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20474v1#S8 — §8 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20474:end -->
<!-- review:SF-2026-ARXIV-2606-20474:end -->

<!-- review:SF-2026-ARXIV-2606-20475:start -->
### 2606.20475 — Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution

**问题与旧路径。** In batch-style trace distillation, the same memory operation may receive contradictory feedback across different batches.

**机制、状态与控制流。** `Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution` 路由到 `AGENT-MEMORY`：memory self-evolution 不按单轮 reward 覆盖旧记忆，而累计候选记忆相对基线的 marginal advantage，再由 memory owner 决定 promote/retain/evict；低置信时保留旧版本。代价是 delayed credit 与 evaluator bias 会固化错误。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20475v1#S3 — §3 Marginal-Advantage Accumulation`；Evaluation=`https://arxiv.org/html/2606.20475v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验仅覆盖论文 agents、tasks、judge 与 memory budget；未证明非平稳长期用户、对抗记忆或跨任务 advantage 可比较。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20475:start -->
Claim boundary：仅 `arXiv:2606.20475v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20475v1#S5 — §5 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20475:end -->
<!-- review:SF-2026-ARXIV-2606-20475:end -->

<!-- review:SF-2026-ARXIV-2606-20487:start -->
### 2606.20487 — Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems

**问题与旧路径。** Real-world computer-use tasks often span multiple applications and devices, requiring agents to coordinate heterogeneous environments under dynamic runtime failures.

**机制、状态与控制流。** `Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems` 路由到 `AGENT-WORKFLOW`：跨设备 agent 从全局 replanning 改为层级 recovery：设备局部 controller 先修复可逆错误，跨设备依赖破坏才升级 workflow planner；handoff state 保存 checkpoint/compensation。代价是故障分类错误，fallback 为全局重规划或人工。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20487v1#S3 — §3 Hierarchical Recovery Methodology`；Evaluation=`https://arxiv.org/html/2606.20487v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证论文 devices、tasks、failure injection 与 latency；未证明真实设备副作用、网络 partition、并发用户或补偿完整。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20487:start -->
Claim boundary：仅 `arXiv:2606.20487v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20487v1#S5 — §5 Failure Analysis and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20487:end -->
<!-- review:SF-2026-ARXIV-2606-20487:end -->

<!-- review:SF-2026-ARXIV-2606-20493:start -->
### 2606.20493 — Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems

**问题与旧路径。** When large language models serve as evaluators in multi-agent systems, their strategy preferences -- whether induced by explicit prompts or by shared architectural priors -- propagate through the agent network.

**机制、状态与控制流。** `Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems` 路由到 `AGENT-MULTI-AGENT`：它把 evaluator preference 看作多-agent 图上的传播状态，要求 evaluation owner 跟踪 judge influence/依赖，而非把 agent votes 当独立样本；检测到 contagion 时使用隔离 judge 或独立 anchor。代价是图估计与额外评审成本。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20493v1#S3 — §3 Contagion Network Model`；Evaluation=`https://arxiv.org/html/2606.20493v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果来自论文 contagion model、拓扑和 LLM judges；未证明真实组织评审、隐藏共享训练或动态 agent 网络中的因果传播。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20493:start -->
Claim boundary：仅 `arXiv:2606.20493v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20493v1#S5 — §5 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20493:end -->
<!-- review:SF-2026-ARXIV-2606-20493:end -->

<!-- review:SF-2026-ARXIV-2606-20502:start -->
### 2606.20502 — Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software

**问题与旧路径。** Whether LLMs scoring well on vulnerability benchmarks genuinely reason about security or merely pattern-match on contaminated data remains unresolved.

**机制、状态与控制流。** `Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software` 路由到 `PLATFORM-EVALUATION-SYSTEM`：该研究表明 vulnerability detector 可校准却不理解漏洞，支持现有 evaluation 章分离 confidence calibration 与 semantic correctness 的原则；没有新的长期 owner，故 No Change。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20502v1#S3 — §III Methodological Framework`；Evaluation=`https://arxiv.org/html/2606.20502v1#S4 — §IV Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果绑定 systems-software 数据集、fine-tuning recipe、模型与漏洞标签；校准曲线不能证明新代码、组合漏洞或真实 exploitability。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20502:start -->
Claim boundary：仅 `arXiv:2606.20502v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20502v1#S6 — §VI Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20502:end -->
<!-- review:SF-2026-ARXIV-2606-20502:end -->

<!-- review:SF-2026-ARXIV-2606-20510:start -->
### 2606.20510 — Efficient and Sound Probabilistic Verification for AI Agents

**问题与旧路径。** Securing AI agents that operate in complex digital environments has become a critical need, and runtime monitoring approaches that formulate and enforce policies expressed in a formal language like Datalog offer a promising solution.

**机制、状态与控制流。** `Efficient and Sound Probabilistic Verification for AI Agents` 路由到 `AGENT-WORKFLOW`：概率 verification 将 agent policy 的不确定转移纳入可计算验收，通过 relaxation 在 sound bound 与成本间调节；verifier 拥有 accept/reject，超时或 bound 过松时回退 conservative rule/human review。代价是状态抽象与概率模型误设。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20510v1#S3 — §3 Verification Optimization and §4 Relaxation`；Evaluation=`https://arxiv.org/html/2606.20510v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** soundness 只对论文形式假设、抽象与概率界成立；实验不证明开放工具环境、非平稳 policy 或未建模副作用。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20510:start -->
Claim boundary：仅 `arXiv:2606.20510v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20510v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20510:end -->
<!-- review:SF-2026-ARXIV-2606-20510:end -->

<!-- review:SF-2026-ARXIV-2606-20512:start -->
### 2606.20512 — Probe-and-Refine Tuning of Repository Guidance for Coding Agents

**问题与旧路径。** LLM-based coding agents need higher-level operational knowledge about a repository (which files house which subsystems, how to run the test suite, which workflows have historically led to wrong fixes) that does not exist in the code itself.

**机制、状态与控制流。** `Probe-and-Refine Tuning of Repository Guidance for Coding Agents` 路由到 `AGENT-PROMPT`：repository guidance 从静态 README/AGENTS 文本变为 probe-and-refine：运行 coding agent，定位失败 step，再在固定 step budget 内修改 guidance 并跨模型验证；repo owner 持有发布/回滚，过拟合时保留旧指导。代价是 probe 成本和 benchmark leakage。 唯一知识 owner 为 `AGENT-PROMPT`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20512v1#S3 — §3 Probe-and-Refine Design`；Evaluation=`https://arxiv.org/html/2606.20512v1#S4 — §4 Evaluation through §7 Cross-Model Analysis`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果限于论文 repositories、tasks、agents 和 step budget；未证明未来代码变化、隐藏测试、安全规范或跨模型长期泛化。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20512:start -->
Claim boundary：仅 `arXiv:2606.20512v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20512v1#S9 — §9 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20512:end -->
<!-- review:SF-2026-ARXIV-2606-20512:end -->

<!-- review:SF-2026-ARXIV-2606-20520:start -->
### 2606.20520 — Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes

**问题与旧路径。** Autonomous agents are increasingly connected to cloud, deployment, and data-control workflows, but production mutation authority should not reside inside non-deterministic reasoning processes.

**机制、状态与控制流。** `Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes` 路由到 `PLATFORM-SECURITY`：Sovereign Execution Broker 将 prompt 声明的权限替换为 certificate-bound authority：principal 提交带 scope/expiry 的证书，broker 在工具执行前验证、记录并可 revoke；agent 不持有最终执行权。证书/身份漂移时 fail closed，并与人工 break-glass 共存。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20520v1#S4 — §4 Broker Execution and §5 Scoped Identity`；Evaluation=`https://arxiv.org/html/2606.20520v1#S8 — §8 Evaluation and §9 Security Analysis`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** evaluation 只覆盖论文 broker、capability 和 attack scenarios；未证明所有第三方工具、密钥轮换、跨域 trust root 或 broker compromise。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20520:start -->
Claim boundary：仅 `arXiv:2606.20520v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20520v1#S10 — §10 Discussion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20520:end -->
<!-- review:SF-2026-ARXIV-2606-20520:end -->

<!-- review:SF-2026-ARXIV-2606-20529:start -->
### 2606.20529 — LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents

**问题与旧路径。** Policy-adherent tool-calling agents in customer-service domains must maintain task states across turns while calling tools and obeying domain policies.

**机制、状态与控制流。** `LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents` 路由到 `AGENT-MEMORY`：LedgerAgent 将 policy-relevant state 记录为结构化 append-only ledger，planner 每次工具调用前读取约束并提交可审计 transition；ledger/policy engine 拥有状态，LLM 不能静默改写。解析冲突时拒绝或转人工。代价是 schema 覆盖与写放大。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20529v1#S3 — §3 LedgerAgent Method`；Evaluation=`https://arxiv.org/html/2606.20529v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验限于论文 tool tasks、policy set 与 ledger parser；未证明并发事务、隐式状态、恶意工具返回或长期 ledger 压缩。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20529:start -->
Claim boundary：仅 `arXiv:2606.20529v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20529v1#S5 — §5 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20529:end -->
<!-- review:SF-2026-ARXIV-2606-20529:end -->

<!-- review:SF-2026-ARXIV-2606-20536:start -->
### 2606.20536 — The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation

**问题与旧路径。** The Frechet Inception Distance (FID) is the de facto arbiter of image generation, yet most papers report just a single number from a single trained model using a single sampling seed.

**机制、状态与控制流。** `The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation` 路由到 `PLATFORM-EVALUATION-SYSTEM`：FID 验收从单次 seed 分数改为显式训练 seed×生成 seed 分布与置信区间；evaluation owner 保存随机性来源，release 依据分布而非最好一次。增加重复成本，预算不足时至少报告 seed sensitivity 而非隐藏。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20536v1#S3 — §3 Experimental Setup`；Evaluation=`https://arxiv.org/html/2606.20536v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 数百个 SiT 网络和 ImageNet-256 的方差结论不证明其它生成架构、数据、采样器或人类质量；FID 本身仍不是完整质量/安全指标。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20536:start -->
Claim boundary：仅 `arXiv:2606.20536v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20536v1#S5 — §5 Limitations and Recommendations`。
<!-- claim:SF-2026-ARXIV-2606-20536:end -->
<!-- review:SF-2026-ARXIV-2606-20536:end -->

<!-- review:SF-2026-ARXIV-2606-20537:start -->
### 2606.20537 — Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving

**问题与旧路径。** Mainstream LLM serving systems reuse prefix work mainly through paged or radix key-value (KV) caches.

**机制、状态与控制流。** `Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving` 路由到 `INFER-REQUEST-LIFECYCLE`：Execution-State Capsule 在 graph-boundary 捕获可恢复的静态 buffer/执行状态，使 on-device small-batch serving 可 checkpoint/restore，而非重建整个 runtime；FlashRT 拥有 capsule schema 与兼容性，失配时冷启动。代价是图绑定、静态内存和 backend 特化。 唯一知识 owner 为 `INFER-REQUEST-LIFECYCLE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20537v1#S2 — §2 FlashRT Runtime Substrate and Execution-State Capsules`；Evaluation=`https://arxiv.org/html/2606.20537v1#S4 — §4 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证 NVIDIA CUDA backend、论文 graph/model/batch 和设备；未证明跨 driver/backend、故障一致性、并发恢复或生产 tail latency。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20537:start -->
Claim boundary：仅 `arXiv:2606.20537v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20537v1#S5 — §5 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20537:end -->
<!-- review:SF-2026-ARXIV-2606-20537:end -->

<!-- review:SF-2026-ARXIV-2606-20545:start -->
### 2606.20545 — Current World Models Lack a Persistent State Core

**问题与旧路径。** World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires an internal world state that keeps evolving over time, decoupled from observation, so that objects endure and events run to their conclusions whether or not a camera is watching, much as the moon holds to its orbit when no one is looking.

**机制、状态与控制流。** `Current World Models Lack a Persistent State Core` 路由到 `MULTIMODAL-WORLD-MODELS`：WRBench 把 camera motion 当 observability intervention，依次验证相机执行、在视场内连续性、离开视场后的状态演化和重新观察一致性；world-model evaluator 拥有 persistent-state verdict，普通 fidelity 指标仅并列。失败时回到显式 state memory/受限 camera。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20545v1#S3 — §3 WRBench Suite and Persistent-State Diagnostics`；Evaluation=`https://arxiv.org/html/2606.20545v1#S4 — §4 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** benchmark 只诊断论文 world models、camera paths 与 human calibration；未证明真实物理状态、因果动力学、长期遮挡或安全控制。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20545:start -->
Claim boundary：仅 `arXiv:2606.20545v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20545v1#S5 — §5 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20545:end -->
<!-- review:SF-2026-ARXIV-2606-20545:end -->

<!-- review:SF-2026-ARXIV-2606-20553:start -->
### 2606.20553 — From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning

**问题与旧路径。** Federated learning (FL) enables multiple parties to collaboratively fine-tune language models for domain-specific tasks without sharing raw data.

**机制、状态与控制流。** `From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning` 路由到 `PLATFORM-SECURITY`：联邦微调的效率路径被证明可承载 privacy backdoor；release contract 因此要在 client update 聚合前后检测泄漏触发与 utility，并由 server 持有 quarantine/rollback。安全聚合与效率优化需和隐私 red-team 共存。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20553v1#S3 — §3 Threat Model and §4 Privacy-Backdoor Attack`；Evaluation=`https://arxiv.org/html/2606.20553v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 攻击与防御只在论文 FL topology、语言模型、clients 和 triggers 上验证；未证明 secure aggregation、异构数据或未知 covert channel。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20553:start -->
Claim boundary：仅 `arXiv:2606.20553v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20553v1#S6 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20553:end -->
<!-- review:SF-2026-ARXIV-2606-20553:end -->

<!-- review:SF-2026-ARXIV-2606-20562:start -->
### 2606.20562 — MemoryWAM: Efficient World Action Modeling with Persistent Memory

**问题与旧路径。** Robust robotic manipulation in the real world requires not only an understanding of the current observation, but also memory and dynamics modeling.

**机制、状态与控制流。** `MemoryWAM: Efficient World Action Modeling with Persistent Memory` 路由到 `MULTIMODAL-EMBODIED-VLA`：MemoryWAM 将 world-action model 的历史压入 persistent memory，在新 observation/action 时选择性读取和更新，使状态不完全依赖当前窗口；memory controller 拥有写入/遗忘，漂移时清空或回退无记忆 model。代价是错误状态累积和额外带宽。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20562v1#S3 — §3 MemoryWAM Method`；Evaluation=`https://arxiv.org/html/2606.20562v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验限于论文 environments、horizons、models 和 memory sizes；未证明真实机器人、不可逆动作、长期漂移或 memory poisoning。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

<!-- claim:SF-2026-ARXIV-2606-20562:start -->
Claim boundary：仅 `arXiv:2606.20562v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20562v1#A1 — §Appendix A Additional Results and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-20562:end -->
<!-- review:SF-2026-ARXIV-2606-20562:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-19376 | 多类LLM benchmarks；SLARouter报告保持SLA并最高降成本2.2×，无需per-benchmark tuning。 | Candidate LLMs in the exact-v1 SLARouter benchmark matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Per-user satisfaction guarantee used by SLARouter; no universal deployment SLO | Cost subject to user-satisfaction guarantee over multiple LLM benchmarks with sparse one-sided feedback |
| SF-2026-ARXIV-2606-19380 | Disclosed — eight coding-agent safety evaluations plus mitigation tests | Disclosed — frontier coding agents and AgentArmor | Disclosed only in the exact-v1 setup; no cross-paper normalization | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-19382 | Disclosed — exact-v1 evaluation workload for DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling | Disclosed where applicable in exact-v1 evaluation; no cross-paper normalization | Disclosed where applicable in exact-v1 setup; otherwise Not Disclosed | Not Disclosed as a universal contract — paper-specific precision is not generalized | Not Disclosed as one universal contract — workload-specific sizes remain bound to v1 | Not Disclosed as one universal contract — task-specific limits are not generalized | Not Disclosed as one universal contract — dataset/trial count is not relabeled batch | Not Disclosed as one universal contract — parallel trials/workers are not relabeled serving concurrency | Not Disclosed — paper metrics are not a production acceptance SLO | Disclosed — exact-v1 paper metrics, baselines and ablations; no later artifact used |
| SF-2026-ARXIV-2606-19386 | SWE-bench Agent trajectories replayed at uniform and measured wall-clock cadence | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | non-uniform Agent action cadence | Not Disclosed | alarm regime, cadence sweep, burst stability, scaling rule and transition-trigger audit |
| SF-2026-ARXIV-2606-19390 | Approximately 10,000 SBOM entries plus synthetic dependency graphs of 50, 500 and 5,000 components; five-fold cross-validation | Random forest with 200 estimators and maximum depth 12; XGBoost with 300 trees, learning rate 0.05, maximum depth 6 and subsampling 0.8 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | advisory consistency, activation evidence, signed artifact and replay reproducibility |
| SF-2026-ARXIV-2606-19409 | audited runtime invariants and controlled replay properties; no broad quality benchmark | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | audited runtime invariants and controlled replay properties; no broad quality benchmark |
| SF-2026-ARXIV-2606-19464 | expressibility and runtime policy-evaluation examples | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | expressibility and runtime policy-evaluation examples |
| SF-2026-ARXIV-2606-19535 | target-platform activation | Qwen3-4B and Qwen3-8B with two LoRA adapters | NVIDIA H200, NVIDIA A100, NVIDIA H100, NVIDIA DGX Spark, Google TPU, AWS Graviton and Alibaba Yitian-710 | Not Disclosed | Not Disclosed | Not Disclosed | 1 | Not Disclosed | Not Disclosed | target-platform activation, aggregate utility and vulnerable-code generation |
| SF-2026-ARXIV-2606-19544 | agreement | Gemini 3.1 Pro, Claude Opus 4.6, DeepSeek V3.2, Claude Sonnet 4.6, Llama 3.3 70B, Kimi K2.5, GPT-5.4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, GLM-5, GPT-oss 120B, Claude Sonnet 4, Gemini 2.5 Flash, Claude Haiku 4.5, GPT-4.1-mini, Minimax M2.7, Qwen 3 8B, GPT-4o-mini, Mixtral 8x22B and GPT-5.4-mini | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | agreement, Cohen's kappa, test-retest consistency, position bias and verbosity bias |
| SF-2026-ARXIV-2606-19559 | clarification F1 and fault detection across clarification and standard benchmarks | GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B and GPT-OSS-120B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | clarification F1 and fault detection across clarification and standard benchmarks |
| SF-2026-ARXIV-2606-19595 | post-interruption task completion and structured recovery error | GPT-4o Audio, GPT-4o Mini Audio, GPT Audio, GPT Audio Mini, GPT Realtime, GPT Realtime 1.5, GPT Realtime Mini, GPT Realtime 2, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash Live, Gemma 4 12B Instruct, Qwen3-Omni-30B-A3B-Instruct, Qwen2.5-Omni-7B, Phi-4-Multimodal-Instruct, Voxtral-Small-24B-2507, Qwen2-Audio-7B-Instruct, MiMo-Audio-7B-Instruct and Kimi-Audio-7B-Instruct across 27 mode/configuration combinations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | post-interruption task completion and structured recovery error |
| SF-2026-ARXIV-2606-19613 | consecutive passed turns | Devstral 2, Devstral Small 2, GLM-5, Kimi K2.5, Nemotron Super, Qwen3-Coder-Next and Qwen3.5-122B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | consecutive passed turns, test feedback/retry effect and harness sensitivity over 20x100-turn scenarios |
| SF-2026-ARXIV-2606-19667 | median TTFT | Qwen2.5-1.5B and Qwen2.5-7B | RTX 4060 Ti 8 GB, RTX 4090 24 GB and RTX 4090D 24 GB | Not Disclosed | max_model_len 2048 or 4096 by configuration | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | median TTFT, prefix reuse and QA answer quality |
| SF-2026-ARXIV-2606-19692 | Two 100,000-document BEIR-composed corpora; 5,571/8,000 sentinels; embedding-space and HotFlip hub attacks | BAAI/bge-large-en-v1.5 plus MiniLM, BGE-base, GTE-large, E5-large-v2 sweep | Apple-silicon arm64 with MPS | float32 embeddings | max sequence length 256; HotFlip length 32 | Not Disclosed | Not Disclosed | 1–8 ingestion threads | Not Disclosed | attack recall/AUROC at frozen 1% benign FPR; HNSW decision flips; ingestion latency/scaling |
| SF-2026-ARXIV-2606-19704 | AssetOpsBench synthesis across 14 implementation studies and seven prior agent benchmarks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Proposed in-sample/OOD rank correlation under three pre-registered criteria; experiment not run |
| SF-2026-ARXIV-2606-19714 | Synthetic pairwise data: 5 runs × 640 comparisons; real pairwise LLM-answer judge data | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | human-consistency recovery, uncertainty-directed label efficiency, ranking agreement and ablations |
| SF-2026-ARXIV-2606-19719 | 74,265-pair English test set with 45% positive labels | Nine retriever/reranker variants including MiniLM, GTE, ColBERT-family and LangCache models | Not Disclosed | BF16 for disclosed LangCache training | 128 tokens for LangCache-Embed-v3 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | PR-AUC, P-CHR AUC, CRR, deployment precision, calibration/structural-gap decomposition |
| SF-2026-ARXIV-2606-19746 | 512 ShareGPT requests; cache-populate and cache-hit rounds | DeepSeek-V3.2 AWQ 4-bit on SGLang/HiSparse | 8×NVIDIA H20 96GB; 2×Xeon Platinum 8575C; 2TB DRAM; 2TB CXL pool | AWQ 4-bit weights; BF16 SGLang runtime | 16K–128K tokens | 1K tokens | Not Disclosed | 8 cache-populate; 64 cache-hit | Not Disclosed | output-token throughput, TTFT, TBT versus RDMA loopback, host-DRAM and GPU-only baselines |
| SF-2026-ARXIV-2606-19753 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-19755 | Multiple adversarial/jailbreak and benign workloads listed in exact-v1 | Qwen3-32B target; Qwen3Guard-Gen-0.6B guard baseline; latent safety head | 6×NVIDIA A800 80GB | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | attack success rate, over-refusal, capability and speculative-decoding speedup |
| SF-2026-ARXIV-2606-19758 | Six reasoning and coding benchmarks; unseen-skill-library transfer | Three base LLMs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task score versus CARD and topology baselines; unseen-library performance drop |
| SF-2026-ARXIV-2606-19769 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-19795 | Survey of 82 agentic EDA systems | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | handoff-contract taxonomy; no empirical EACP benchmark disclosed |
| SF-2026-ARXIV-2606-19803 | Preliminary policy-aware vector-search experiments disclosed in §4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | policy correctness, ANN recall and query latency |
| SF-2026-ARXIV-2606-19808 | MATH500, GSM8K and CommonsenseQA reasoning tasks | Frozen Qwen3-4B solver | Not Disclosed | Not Disclosed | Initial solve budgets include 8,192 tokens | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | accuracy, verification/post-generation tokens, harmful flips and realized total tokens |
| SF-2026-ARXIV-2606-19847 | LoCoMo multi-session memory benchmark | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reasoning-task accuracy, memory size/cost and ablations |
| SF-2026-ARXIV-2606-19849 | Multiple streaming-video benchmarks listed in exact-v1 | Qwen2.5-VL-3B/7B-Instruct | Single NVIDIA A100 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Reported TTFT below 50 ms in tested configuration | video FPS, TTFT, accuracy and stage-wise bottleneck/ablation curves |
| SF-2026-ARXIV-2606-19868 | Four dataset settings | Four black-box LLMs; 24 uncertainty-estimation methods | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | unified uncertainty quality/calibration comparison across method categories |
| SF-2026-ARXIV-2606-19887 | FinRED expert-guided financial red-team benchmark | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | red-team coverage/performance, expert validation and inter-rater reliability |
| SF-2026-ARXIV-2606-19898 | Filtered-ANN query workloads and filter-selectivity regimes in §6 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | recall/latency and routing accuracy against fixed rule/index paths |
| SF-2026-ARXIV-2606-19899 | Biological capability and risk task suites in exact-v1 PDF | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task capability scores and expert risk interpretation |
| SF-2026-ARXIV-2606-19911 | Multi-agent tasks and memory ablations in §4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success, retrieval/communication cost and transactive-directory ablations |
| SF-2026-ARXIV-2606-19989 | Online LLM-training arrival/length traces in §4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | batching efficiency, waiting time/utilization and formal competitive guarantees |
| SF-2026-ARXIV-2606-19992 | Agentic web-service tasks in §4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task completion, tool-program flexibility and execution overhead |
| SF-2026-ARXIV-2606-19998 | VLA failure-prediction tasks in exact-v1 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | failure-detection discrimination/calibration and cross-setting generalization |
| SF-2026-ARXIV-2606-20002 | Cross-domain long-lifecycle agent rollouts in §3 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | cross-domain task success/generalization and RL ablations |
| SF-2026-ARXIV-2606-20005 | Attention-distillation KL workloads in §5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | peak memory, runtime/throughput, numerical error and downstream distillation quality |
| SF-2026-ARXIV-2606-20023 | Agent tool-selection tasks with privilege annotations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success, selected privilege excess and mitigation utility |
| SF-2026-ARXIV-2606-20047 | Context-selection tasks and budgets in §5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | answer/task quality versus context tokens, latency and selection ablations |
| SF-2026-ARXIV-2606-20113 | Streaming retrieval/tool-intent tasks in §5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success, tool-call timing, false dispatch and latency |
| SF-2026-ARXIV-2606-20122 | Open-ended deep-research tasks in §5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | research-task quality, evidence coverage, cost and outline-optimization ablations |
| SF-2026-ARXIV-2606-20128 | 24-kernel corpus extended to 26 operations including flash attention | Not Disclosed | RTX 3060, A10, L40S, A100 SXM4 and H100 NVL | FP64 CPU oracle; FP32/FP16/BF16 target cases | Operation-schema shape domains | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | bug recall, clean-control precision and cross-GPU verdict consistency |
| SF-2026-ARXIV-2606-20158 | Coding-agent tasks under N-version configurations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | functional correctness, failure correlation, adjudication accuracy and agent cost |
| SF-2026-ARXIV-2606-20235 | ScholarQuest taxonomy-guided open-literature search tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | academic-search task success and taxonomy-specific retrieval/reasoning metrics |
| SF-2026-ARXIV-2606-20243 | GitHub issue-resolution repositories and injected failure/safety cases | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | issue resolution, test outcomes, unsafe-action rate and multi-agent ablations |
| SF-2026-ARXIV-2606-20245 | Parametric-versus-contextual knowledge-conflict tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | conflict detection/resolution accuracy across knowledge conditions |
| SF-2026-ARXIV-2606-20254 | Quantization-conditioned backdoor clean/attack suites | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | attack success, clean utility and post-removal quantized-model quality |
| SF-2026-ARXIV-2606-20318 | Database workloads and reconfiguration action space in §5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | workload performance, adaptation speed, unsafe/regressive changes and rollback |
| SF-2026-ARXIV-2606-20363 | Computer-use interaction trajectories and held-out skill tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | skill execution success, generation quality and trajectory-mining ablations |
| SF-2026-ARXIV-2606-20374 | Production distributed-training workloads and diagnosed incidents | Not Disclosed | >10,000-GPU cluster | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | trace coverage, diagnosis latency/accuracy and production overhead |
| SF-2026-ARXIV-2606-20381 | LLM FP4 pretraining configurations in §5 | Not Disclosed | Not Disclosed | FP4/UFP4 with higher-precision comparisons | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | pretraining loss, downstream quality and shrinkage-bias diagnostics |
| SF-2026-ARXIV-2606-20408 | NRT-Bench multi-turn operator-agent red-team scenarios in simulated control rooms | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | attack success, safe task utility and multi-turn recovery |
| SF-2026-ARXIV-2606-20470 | Model-guided attack/defensive-misdirection simulations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | attacker success/time/cost under defense and decoy strategies |
| SF-2026-ARXIV-2606-20474 | Context-heavy agent workloads and long-context KV-cache traces | Not Disclosed | Not Disclosed | 4-bit KV cache with higher-precision baselines | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task quality, KV footprint, throughput and latency |
| SF-2026-ARXIV-2606-20475 | Memory-driven agent self-evolution tasks in §4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success, memory utility, marginal-advantage accuracy and ablations |
| SF-2026-ARXIV-2606-20487 | Cross-device agent tasks with injected local/cross-device failures | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | recovery success, latency/cost and unnecessary global replans |
| SF-2026-ARXIV-2606-20493 | Multi-agent evaluator networks/topologies in §4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | preference propagation, independence loss and intervention effectiveness |
| SF-2026-ARXIV-2606-20502 | Systems-software vulnerability-detection datasets in §III–IV | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | detection quality, calibration and comprehension/semantic probes |
| SF-2026-ARXIV-2606-20510 | Probabilistic agent-verification cases in §5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | soundness/coverage, verification cost and relaxation tightness |
| SF-2026-ARXIV-2606-20512 | Repository coding tasks under probe-and-refine guidance | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success, localization, step budget, cross-model transfer and guidance ablations |
| SF-2026-ARXIV-2606-20520 | Agent-control-plane authority and attack scenarios in §8–9 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | authorized task utility, unauthorized execution, revoke/drift behavior and broker overhead |
| SF-2026-ARXIV-2606-20529 | Policy-constrained tool-calling tasks in §4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success, policy violations, state consistency and ledger overhead |
| SF-2026-ARXIV-2606-20536 | Several hundred SiT networks on ImageNet 256×256 | Not Disclosed | Not Disclosed | Not Disclosed | 256×256 images | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | FID distributions across training and generation seeds |
| SF-2026-ARXIV-2606-20537 | Low-latency small-batch on-device Physical-AI serving graphs | Not Disclosed | NVIDIA CUDA backend | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | checkpoint/restore latency, throughput, memory and correctness across graph boundaries |
| SF-2026-ARXIV-2606-20545 | WRBench camera-motion interventions on generated-world models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | human-calibrated camera execution, in-view continuity, off-view evolution and re-observation consistency |
| SF-2026-ARXIV-2606-20553 | Federated language-model fine-tuning with privacy-backdoor attacks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | leakage/attack success, clean utility and defense behavior |
| SF-2026-ARXIV-2606-20562 | World-action-model environments and persistent-memory ablations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | action/world prediction, task success, memory/latency and horizon scaling |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-19376 | score_7_9 | not_selected | — | — | Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19376 |
| SF-2026-ARXIV-2606-19380 | score_7_9; potential_books_delta | not_selected | — | — | ClayBuddy: A Framework, Evaluation, & Mitigation of Coding Agent Failures remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19380 |
| SF-2026-ARXIV-2606-19382 | score_7_9 | not_selected | — | — | DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19382 |
| SF-2026-ARXIV-2606-19386 | score_7_9; potential_books_delta | not_selected | — | — | Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19386 |
| SF-2026-ARXIV-2606-19390 | score_7_9; potential_books_delta | not_selected | — | — | Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19390 |
| SF-2026-ARXIV-2606-19409 | score_7_9 | not_selected | — | — | OpenRath: Session-Centered Runtime State for Agent Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19409 |
| SF-2026-ARXIV-2606-19464 | score_7_9 | not_selected | — | — | Deontic Policies for Runtime Governance of Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19464 |
| SF-2026-ARXIV-2606-19535 | score_7_9; potential_books_delta | selected | DA-20260618-PLATFORM-BOUND-ARTIFACT | — | 它把 platform/kernel 纳入模型供应链的可执行 identity，而非仅记录权重 hash。 | analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT |
| SF-2026-ARXIV-2606-19544 | score_7_9 | not_selected | — | — | Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19544 |
| SF-2026-ARXIV-2606-19559 | score_7_9 | not_selected | — | — | Uncertainty Decomposition for Clarification Seeking in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19559 |
| SF-2026-ARXIV-2606-19595 | score_7_9 | not_selected | — | — | IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19595 |
| SF-2026-ARXIV-2606-19613 | score_7_9; potential_books_delta | not_selected | — | — | StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19613 |
| SF-2026-ARXIV-2606-19667 | score_7_9; potential_books_delta | not_selected | — | — | CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19667 |
| SF-2026-ARXIV-2606-19692 | score_7_9; potential_books_delta | not_selected | — | — | When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19692 |
| SF-2026-ARXIV-2606-19704 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19704 |
| SF-2026-ARXIV-2606-19714 | score_7_9; potential_books_delta | not_selected | — | — | AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19714 |
| SF-2026-ARXIV-2606-19719 | score_7_9; potential_books_delta | not_selected | — | — | Closing the Operational Gap in Semantic Caching remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19719 |
| SF-2026-ARXIV-2606-19746 | score_7_9; potential_books_delta | not_selected | — | — | SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19746 |
| SF-2026-ARXIV-2606-19753 | score_7_9 | not_selected | — | — | Grounded Inference: Principles for Deterministically Encapsulated Generative Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19753 |
| SF-2026-ARXIV-2606-19755 | score_7_9; potential_books_delta | not_selected | — | — | SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19755 |
| SF-2026-ARXIV-2606-19758 | score_7_9; potential_books_delta | not_selected | — | — | SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19758 |
| SF-2026-ARXIV-2606-19769 | score_7_9; potential_books_delta | not_selected | — | — | Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19769 |
| SF-2026-ARXIV-2606-19795 | score_7_9; potential_books_delta | not_selected | — | — | Agentic Electronic Design Automation: A Handoff Perspective remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19795 |
| SF-2026-ARXIV-2606-19803 | score_7_9; potential_books_delta | not_selected | — | — | Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19803 |
| SF-2026-ARXIV-2606-19808 | score_7_9; potential_books_delta | not_selected | — | — | Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19808 |
| SF-2026-ARXIV-2606-19847 | score_7_9; potential_books_delta | not_selected | — | — | AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19847 |
| SF-2026-ARXIV-2606-19849 | score_7_9; potential_books_delta | not_selected | — | — | ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19849 |
| SF-2026-ARXIV-2606-19868 | score_7_9 | not_selected | — | — | A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19868 |
| SF-2026-ARXIV-2606-19887 | score_7_9 | not_selected | — | — | FinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19887 |
| SF-2026-ARXIV-2606-19898 | score_7_9; potential_books_delta | not_selected | — | — | Query-aware Routing for Filtered Approximate Nearest Neighbors Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19898 |
| SF-2026-ARXIV-2606-19899 | score_7_9 | not_selected | — | — | Measuring Biological Capabilities and Risks of AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19899 |
| SF-2026-ARXIV-2606-19911 | score_7_9; potential_books_delta | not_selected | — | — | Multi-Agent Transactive Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19911 |
| SF-2026-ARXIV-2606-19989 | score_7_9; potential_books_delta | not_selected | — | — | Online Dynamic Batching with Formal Guarantees for LLM Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19989 |
| SF-2026-ARXIV-2606-19992 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19992 |
| SF-2026-ARXIV-2606-19998 | score_7_9; potential_books_delta | not_selected | — | — | Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19998 |
| SF-2026-ARXIV-2606-20002 | score_7_9; potential_books_delta | not_selected | — | — | Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20002 |
| SF-2026-ARXIV-2606-20005 | score_7_9; potential_books_delta | not_selected | — | — | StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20005 |
| SF-2026-ARXIV-2606-20023 | score_7_9; potential_books_delta | not_selected | — | — | When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20023 |
| SF-2026-ARXIV-2606-20047 | score_7_9; potential_books_delta | not_selected | — | — | PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20047 |
| SF-2026-ARXIV-2606-20113 | score_7_9; potential_books_delta | not_selected | — | — | When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20113 |
| SF-2026-ARXIV-2606-20122 | score_7_9; potential_books_delta | not_selected | — | — | ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20122 |
| SF-2026-ARXIV-2606-20128 | score_7_9; potential_books_delta | not_selected | — | — | The Correctness Illusion in LLM-Generated GPU Kernels remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20128 |
| SF-2026-ARXIV-2606-20158 | score_7_9; potential_books_delta | not_selected | — | — | N-Version Programming with Coding Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20158 |
| SF-2026-ARXIV-2606-20235 | score_7_9 | not_selected | — | — | ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20235 |
| SF-2026-ARXIV-2606-20243 | score_7_9 | not_selected | — | — | Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20243 |
| SF-2026-ARXIV-2606-20245 | score_7_9 | not_selected | — | — | Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20245 |
| SF-2026-ARXIV-2606-20254 | score_7_9; potential_books_delta | not_selected | — | — | Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20254 |
| SF-2026-ARXIV-2606-20318 | score_7_9; potential_books_delta | not_selected | — | — | AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20318 |
| SF-2026-ARXIV-2606-20363 | score_7_9; potential_books_delta | not_selected | — | — | Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20363 |
| SF-2026-ARXIV-2606-20374 | score_7_9; potential_books_delta | selected | DA-20260619-TRACE-10K-GPU | — | 入选：把万卡训练诊断从节点日志提升为跨层 trace contract。 | analysis:DA-20260619-TRACE-10K-GPU |
| SF-2026-ARXIV-2606-20381 | score_7_9; potential_books_delta | not_selected | — | — | Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20381 |
| SF-2026-ARXIV-2606-20408 | score_7_9 | not_selected | — | — | NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20408 |
| SF-2026-ARXIV-2606-20470 | score_7_9; potential_books_delta | not_selected | — | — | Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20470 |
| SF-2026-ARXIV-2606-20474 | score_7_9; potential_books_delta | not_selected | — | — | UltraQuant: 4-bit KV Caching for Context-Heavy Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20474 |
| SF-2026-ARXIV-2606-20475 | score_7_9; potential_books_delta | not_selected | — | — | Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20475 |
| SF-2026-ARXIV-2606-20487 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20487 |
| SF-2026-ARXIV-2606-20493 | score_7_9; potential_books_delta | not_selected | — | — | Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20493 |
| SF-2026-ARXIV-2606-20502 | score_7_9 | not_selected | — | — | Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20502 |
| SF-2026-ARXIV-2606-20510 | score_7_9; potential_books_delta | not_selected | — | — | Efficient and Sound Probabilistic Verification for AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20510 |
| SF-2026-ARXIV-2606-20512 | score_7_9; potential_books_delta | not_selected | — | — | Probe-and-Refine Tuning of Repository Guidance for Coding Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PROMPT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20512 |
| SF-2026-ARXIV-2606-20520 | score_7_9; potential_books_delta | selected | DA-20260619-CERTIFICATE-AUTHORITY | — | 入选：把 agent control-plane authority 固化为可验证 certificate 与 broker enforcement。 | analysis:DA-20260619-CERTIFICATE-AUTHORITY |
| SF-2026-ARXIV-2606-20529 | score_7_9; potential_books_delta | not_selected | — | — | LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20529 |
| SF-2026-ARXIV-2606-20536 | score_7_9; potential_books_delta | not_selected | — | — | The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20536 |
| SF-2026-ARXIV-2606-20537 | score_7_9; potential_books_delta | not_selected | — | — | Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-REQUEST-LIFECYCLE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20537 |
| SF-2026-ARXIV-2606-20545 | score_7_9; potential_books_delta | not_selected | — | — | Current World Models Lack a Persistent State Core remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20545 |
| SF-2026-ARXIV-2606-20553 | score_7_9; potential_books_delta | not_selected | — | — | From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20553 |
| SF-2026-ARXIV-2606-20562 | score_7_9; potential_books_delta | not_selected | — | — | MemoryWAM: Efficient World Action Modeling with Persistent Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-20562 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-2026-ARXIV-2606-19376:start -->
Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19376:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19380:start -->
ClayBuddy: A Framework, Evaluation, & Mitigation of Coding Agent Failures remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19380:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19382:start -->
DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19382:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19386:start -->
Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19386:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19390:start -->
Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19390:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19409:start -->
OpenRath: Session-Centered Runtime State for Agent Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19409:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19464:start -->
Deontic Policies for Runtime Governance of Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19464:end -->

<!-- analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT:start -->
### DA-20260618-PLATFORM-BOUND-ARTIFACT
权重 hash 不能单独定义可执行模型身份。FloatDoor 表明同一权重和 LoRA 组合可利用 platform/kernel 浮点差异触发不同任务，因此 audit artifact 必须绑定目标硬件、kernel 和 serving build；跨平台差异本身仍不证明后门存在。
<!-- analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19544:start -->
Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19544:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19559:start -->
Uncertainty Decomposition for Clarification Seeking in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19559:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19595:start -->
IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19595:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19613:start -->
StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19613:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19667:start -->
CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19667:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19692:start -->
When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19692:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19704:start -->
Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19714:start -->
AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19714:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19719:start -->
Closing the Operational Gap in Semantic Caching remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19719:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19746:start -->
SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19746:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19753:start -->
Grounded Inference: Principles for Deterministically Encapsulated Generative Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19753:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19755:start -->
SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19755:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19758:start -->
SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19758:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19769:start -->
Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19769:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19795:start -->
Agentic Electronic Design Automation: A Handoff Perspective remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19795:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19803:start -->
Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19803:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19808:start -->
Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19808:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19847:start -->
AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19849:start -->
ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19849:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19868:start -->
A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19868:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19887:start -->
FinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19887:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19898:start -->
Query-aware Routing for Filtered Approximate Nearest Neighbors Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19898:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19899:start -->
Measuring Biological Capabilities and Risks of AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19899:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19911:start -->
Multi-Agent Transactive Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19911:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19989:start -->
Online Dynamic Batching with Formal Guarantees for LLM Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19989:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19992:start -->
Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19992:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19998:start -->
Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19998:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20002:start -->
Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20002:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20005:start -->
StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20023:start -->
When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20023:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20047:start -->
PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20047:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20113:start -->
When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20113:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20122:start -->
ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20122:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20128:start -->
The Correctness Illusion in LLM-Generated GPU Kernels remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20128:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20158:start -->
N-Version Programming with Coding Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20158:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20235:start -->
ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20235:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20243:start -->
Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20243:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20245:start -->
Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20245:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20254:start -->
Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20254:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20318:start -->
AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20318:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20363:start -->
Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20363:end -->

<!-- analysis:DA-20260619-TRACE-10K-GPU:start -->
### 万卡训练的 trace contract
规模扩大后，单节点日志不能重建跨 rank、collective、network 和 storage 的因果链；ARGUS 把 trace identity 与诊断路径提升为平台契约，仍不能把相关序列自动当作根因。
<!-- analysis:DA-20260619-TRACE-10K-GPU:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20381:start -->
Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20381:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20408:start -->
NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20408:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20470:start -->
Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20470:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20474:start -->
UltraQuant: 4-bit KV Caching for Context-Heavy Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20474:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20475:start -->
Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20475:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20487:start -->
Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20487:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20493:start -->
Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20493:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20502:start -->
Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20502:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20510:start -->
Efficient and Sound Probabilistic Verification for AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20510:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20512:start -->
Probe-and-Refine Tuning of Repository Guidance for Coding Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PROMPT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20512:end -->

<!-- analysis:DA-20260619-CERTIFICATE-AUTHORITY:start -->
### Agent 权限的可验证执行
仅在 prompt 中声明权限不足以形成控制边界；certificate-bound broker 把 principal、capability 与执行授权绑定，并要求 revoke/audit 路径与工具调用分离。其评测不证明所有外部工具或密钥生命周期已覆盖。
<!-- analysis:DA-20260619-CERTIFICATE-AUTHORITY:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20529:start -->
LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20529:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20536:start -->
The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20536:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20537:start -->
Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-REQUEST-LIFECYCLE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20537:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20545:start -->
Current World Models Lack a Persistent State Core remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20545:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20553:start -->
From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20553:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20562:start -->
MemoryWAM: Efficient World Action Modeling with Persistent Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-20562:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-19376 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L1 | Books/part-05-inference-system/52-dynamo.md#L1; Books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2606-19376 | delta:SF-2026-ARXIV-2606-19376 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19376 |
| SF-2026-ARXIV-2606-19380 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-19380 | delta:SF-2026-ARXIV-2606-19380 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19380 |
| SF-2026-ARXIV-2606-19382 | AGENT-MULTI-AGENT | Books/part-07-agent/82-multi-agent.md#L1 | Books/part-07-agent/81-workflow.md#L1; Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-19382 | delta:SF-2026-ARXIV-2606-19382 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19382 |
| SF-2026-ARXIV-2606-19386 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/68-logging.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-19386 | delta:SF-2026-ARXIV-2606-19386 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19386 |
| SF-2026-ARXIV-2606-19390 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/69-trace.md#L1; Books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-19390 | delta:SF-2026-ARXIV-2606-19390 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19390 |
| SF-2026-ARXIV-2606-19409 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-19409 | delta:SF-2026-ARXIV-2606-19409 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19409 |
| SF-2026-ARXIV-2606-19464 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19464 | delta:SF-2026-ARXIV-2606-19464 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19464 |
| SF-2026-ARXIV-2606-19535 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19535 | delta:SF-2026-ARXIV-2606-19535 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19535 |
| SF-2026-ARXIV-2606-19544 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19544 | delta:SF-2026-ARXIV-2606-19544 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19544 |
| SF-2026-ARXIV-2606-19559 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-19559 | delta:SF-2026-ARXIV-2606-19559 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19559 |
| SF-2026-ARXIV-2606-19595 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-19595 | delta:SF-2026-ARXIV-2606-19595 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19595 |
| SF-2026-ARXIV-2606-19613 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19613 | delta:SF-2026-ARXIV-2606-19613 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19613 |
| SF-2026-ARXIV-2606-19667 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-19667 | delta:SF-2026-ARXIV-2606-19667 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19667 |
| SF-2026-ARXIV-2606-19692 | AGENT-RAG | Books/part-07-agent/76-rag.md#L1 | Books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-19692 | delta:SF-2026-ARXIV-2606-19692 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19692 |
| SF-2026-ARXIV-2606-19704 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19704 | delta:SF-2026-ARXIV-2606-19704 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19704 |
| SF-2026-ARXIV-2606-19714 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19714 | delta:SF-2026-ARXIV-2606-19714 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19714 |
| SF-2026-ARXIV-2606-19719 | AGENT-RAG | Books/part-07-agent/76-rag.md#L1 | Books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-19719 | delta:SF-2026-ARXIV-2606-19719 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19719 |
| SF-2026-ARXIV-2606-19746 | INFER-KV-CACHE | Books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | Books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-19746 | delta:SF-2026-ARXIV-2606-19746 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19746 |
| SF-2026-ARXIV-2606-19753 | PLATFORM-PRODUCTION | Books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-19753 | delta:SF-2026-ARXIV-2606-19753 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19753 |
| SF-2026-ARXIV-2606-19755 | INFER-SPECULATIVE-DECODING | Books/part-05-inference-system/48-speculative-decoding.md#L1 | Books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-19755 | delta:SF-2026-ARXIV-2606-19755 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19755 |
| SF-2026-ARXIV-2606-19758 | AGENT-MULTI-AGENT | Books/part-07-agent/82-multi-agent.md#L1 | Books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-19758 | delta:SF-2026-ARXIV-2606-19758 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19758 |
| SF-2026-ARXIV-2606-19769 | MULTIMODAL-EMBODIED-VLA | Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-19769 | delta:SF-2026-ARXIV-2606-19769 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19769 |
| SF-2026-ARXIV-2606-19795 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-19795 | delta:SF-2026-ARXIV-2606-19795 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19795 |
| SF-2026-ARXIV-2606-19803 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-19803 | delta:SF-2026-ARXIV-2606-19803 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19803 |
| SF-2026-ARXIV-2606-19808 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L1 | Books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-19808 | delta:SF-2026-ARXIV-2606-19808 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19808 |
| SF-2026-ARXIV-2606-19847 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-19847 | delta:SF-2026-ARXIV-2606-19847 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19847 |
| SF-2026-ARXIV-2606-19849 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L1 | Books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-19849 | delta:SF-2026-ARXIV-2606-19849 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19849 |
| SF-2026-ARXIV-2606-19868 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19868 | delta:SF-2026-ARXIV-2606-19868 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19868 |
| SF-2026-ARXIV-2606-19887 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19887 | delta:SF-2026-ARXIV-2606-19887 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19887 |
| SF-2026-ARXIV-2606-19898 | AGENT-RAG | Books/part-07-agent/76-rag.md#L1 | Books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-19898 | delta:SF-2026-ARXIV-2606-19898 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19898 |
| SF-2026-ARXIV-2606-19899 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19899 | delta:SF-2026-ARXIV-2606-19899 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19899 |
| SF-2026-ARXIV-2606-19911 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-19911 | delta:SF-2026-ARXIV-2606-19911 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19911 |
| SF-2026-ARXIV-2606-19989 | TRAIN-DISTRIBUTED-TRAINING | Books/part-04-training-system/36-distributed-training.md#L1 | Books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-19989 | delta:SF-2026-ARXIV-2606-19989 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19989 |
| SF-2026-ARXIV-2606-19992 | AGENT-MCP | Books/part-07-agent/83-mcp.md#L1 | Books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-19992 | delta:SF-2026-ARXIV-2606-19992 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19992 |
| SF-2026-ARXIV-2606-19998 | MULTIMODAL-EMBODIED-VLA | Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-19998 | delta:SF-2026-ARXIV-2606-19998 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19998 |
| SF-2026-ARXIV-2606-20002 | TRAIN-RLHF | Books/part-04-training-system/31-rlhf.md#L1 | Books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-20002 | delta:SF-2026-ARXIV-2606-20002 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20002 |
| SF-2026-ARXIV-2606-20005 | TRAIN-DISTRIBUTED-TRAINING | Books/part-04-training-system/36-distributed-training.md#L1 | Books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-20005 | delta:SF-2026-ARXIV-2606-20005 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20005 |
| SF-2026-ARXIV-2606-20023 | AGENT-TOOL-CALLING | Books/part-07-agent/78-tool-calling.md#L1 | Books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-20023 | delta:SF-2026-ARXIV-2606-20023 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20023 |
| SF-2026-ARXIV-2606-20047 | AGENT-CONTEXT | Books/part-07-agent/75-context.md#L1 | Books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-20047 | delta:SF-2026-ARXIV-2606-20047 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20047 |
| SF-2026-ARXIV-2606-20113 | AGENT-TOOL-CALLING | Books/part-07-agent/78-tool-calling.md#L1 | Books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-20113 | delta:SF-2026-ARXIV-2606-20113 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20113 |
| SF-2026-ARXIV-2606-20122 | AGENT-PLANNING | Books/part-07-agent/79-planning.md#L1 | Books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-20122 | delta:SF-2026-ARXIV-2606-20122 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20122 |
| SF-2026-ARXIV-2606-20128 | TRAIN-DISTRIBUTED-TRAINING | Books/part-04-training-system/36-distributed-training.md#L1 | Books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-20128 | delta:SF-2026-ARXIV-2606-20128 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20128 |
| SF-2026-ARXIV-2606-20158 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-20158 | delta:SF-2026-ARXIV-2606-20158 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20158 |
| SF-2026-ARXIV-2606-20235 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-20235 | delta:SF-2026-ARXIV-2606-20235 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20235 |
| SF-2026-ARXIV-2606-20243 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-20243 | delta:SF-2026-ARXIV-2606-20243 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20243 |
| SF-2026-ARXIV-2606-20245 | AGENT-CONTEXT | Books/part-07-agent/75-context.md#L1 | Books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-20245 | delta:SF-2026-ARXIV-2606-20245 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20245 |
| SF-2026-ARXIV-2606-20254 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-20254 | delta:SF-2026-ARXIV-2606-20254 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20254 |
| SF-2026-ARXIV-2606-20318 | PLATFORM-PRODUCTION | Books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-20318 | delta:SF-2026-ARXIV-2606-20318 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20318 |
| SF-2026-ARXIV-2606-20363 | AGENT-PLATFORM | Books/part-07-agent/84-agent-platform.md#L1 | Books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-20363 | delta:SF-2026-ARXIV-2606-20363 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20363 |
| SF-2026-ARXIV-2606-20374 | PLATFORM-TRACE | Books/part-06-ai-infrastructure/69-trace.md#L1 | Books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2606-20374 | delta:SF-2026-ARXIV-2606-20374 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20374 |
| SF-2026-ARXIV-2606-20381 | TRAIN-DISTRIBUTED-TRAINING | Books/part-04-training-system/36-distributed-training.md#L1 | Books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-20381 | delta:SF-2026-ARXIV-2606-20381 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20381 |
| SF-2026-ARXIV-2606-20408 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-20408 | delta:SF-2026-ARXIV-2606-20408 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20408 |
| SF-2026-ARXIV-2606-20470 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-20470 | delta:SF-2026-ARXIV-2606-20470 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20470 |
| SF-2026-ARXIV-2606-20474 | INFER-KV-CACHE | Books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | Books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-20474 | delta:SF-2026-ARXIV-2606-20474 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20474 |
| SF-2026-ARXIV-2606-20475 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-20475 | delta:SF-2026-ARXIV-2606-20475 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20475 |
| SF-2026-ARXIV-2606-20487 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-20487 | delta:SF-2026-ARXIV-2606-20487 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20487 |
| SF-2026-ARXIV-2606-20493 | AGENT-MULTI-AGENT | Books/part-07-agent/82-multi-agent.md#L1 | Books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-20493 | delta:SF-2026-ARXIV-2606-20493 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20493 |
| SF-2026-ARXIV-2606-20502 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-20502 | delta:SF-2026-ARXIV-2606-20502 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20502 |
| SF-2026-ARXIV-2606-20510 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-20510 | delta:SF-2026-ARXIV-2606-20510 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20510 |
| SF-2026-ARXIV-2606-20512 | AGENT-PROMPT | Books/part-07-agent/74-prompt.md#L1 | Books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2606-20512 | delta:SF-2026-ARXIV-2606-20512 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20512 |
| SF-2026-ARXIV-2606-20520 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-20520 | delta:SF-2026-ARXIV-2606-20520 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20520 |
| SF-2026-ARXIV-2606-20529 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-20529 | delta:SF-2026-ARXIV-2606-20529 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20529 |
| SF-2026-ARXIV-2606-20536 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-20536 | delta:SF-2026-ARXIV-2606-20536 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20536 |
| SF-2026-ARXIV-2606-20537 | INFER-REQUEST-LIFECYCLE | Books/part-05-inference-system/42-what-happens-during-inference.md#L1 | Books/part-05-inference-system/43-prefill.md#L1 | existing:SF-2026-ARXIV-2606-20537 | delta:SF-2026-ARXIV-2606-20537 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20537 |
| SF-2026-ARXIV-2606-20545 | MULTIMODAL-WORLD-MODELS | Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-20545 | delta:SF-2026-ARXIV-2606-20545 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20545 |
| SF-2026-ARXIV-2606-20553 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-20553 | delta:SF-2026-ARXIV-2606-20553 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20553 |
| SF-2026-ARXIV-2606-20562 | MULTIMODAL-EMBODIED-VLA | Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-20562 | delta:SF-2026-ARXIV-2606-20562 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20562 |

<!-- existing:SF-2026-ARXIV-2606-19376:start -->
Read owner `INFER-SCHEDULING` at `Books/part-05-inference-system/56-inference-scheduling.md` and adjacent chapters `Books/part-05-inference-system/52-dynamo.md; Books/part-06-ai-infrastructure/70-cost.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-19376:end -->

<!-- delta:SF-2026-ARXIV-2606-19376:start -->
LLM router 可在稀疏、单侧 user feedback下在线学习cost policy，同时把满意度SLA作为约束而非平均reward。
<!-- delta:SF-2026-ARXIV-2606-19376:end -->

<!-- books-review:SF-2026-ARXIV-2606-19376:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 理论保证依赖反馈与可行性假设；offline benchmark satisfaction不是生产SLA，delayed/strategic feedback会破坏校准。
<!-- books-review:SF-2026-ARXIV-2606-19376:end -->

<!-- existing:SF-2026-ARXIV-2606-19380:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-19380:end -->

<!-- delta:SF-2026-ARXIV-2606-19380:start -->
coding-agent safety failure 应拆成 underspecification、capability error 与 harness error，并分别用 policy、classifier/immutability 与 context/tool control修复。
<!-- delta:SF-2026-ARXIV-2606-19380:end -->

<!-- books-review:SF-2026-ARXIV-2606-19380:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-19380:end -->

<!-- existing:SF-2026-ARXIV-2606-19382:start -->
Owner `AGENT-MULTI-AGENT` and explicit adjacent chapters were read; existing mechanism, fallback and failure boundary were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-19382:end -->

<!-- delta:SF-2026-ARXIV-2606-19382:start -->
Multi-Agent workflow scheduler应从dependency DAG释放ready tasks、并行independent work且在fault时保持topological correctness
<!-- delta:SF-2026-ARXIV-2606-19382:end -->

<!-- books-review:SF-2026-ARXIV-2606-19382:start -->
Owner `AGENT-MULTI-AGENT`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/66-evaluation-system.md`. Ch82/81已拥有dependency DAG、ready-node release、独立workspace与coordinator bottleneck/fallback，不机械追加。
<!-- books-review:SF-2026-ARXIV-2606-19382:end -->

<!-- existing:SF-2026-ARXIV-2606-19386:start -->
Ch67 已持有 signal identity、sampling/time semantics、threshold 与 alert lifecycle；Ch68/Ch69 持有日志和 trace 证据。 For this family the compared adjacent handoff is `books/part-06-ai-infrastructure/68-logging.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1`.
<!-- existing:SF-2026-ARXIV-2606-19386:end -->

<!-- delta:SF-2026-ARXIV-2606-19386:start -->
wall-clock moment detector 在 Agent cadence 下可能结构性双稳态；monitor 必须以可观测 transition window 校准而非宣称瞬时状态真值
<!-- delta:SF-2026-ARXIV-2606-19386:end -->

<!-- books-review:SF-2026-ARXIV-2606-19386:start -->
Unique owner `PLATFORM-MONITORING`; adjacent consumer `books/part-06-ai-infrastructure/68-logging.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 论文首先纠正自身 Δt=0 错误，后续 bistability 只覆盖所测 cadence/monitor class；时钟或 burst 分布漂移时回退 transition-window 告警而非 moment truth。
<!-- books-review:SF-2026-ARXIV-2606-19386:end -->

<!-- existing:SF-2026-ARXIV-2606-19390:start -->
`PLATFORM-SECURITY` 已有 trust boundary、provenance、least privilege、containment 与 effect-time authority; adjacent handoff was checked in `Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md`.
<!-- existing:SF-2026-ARXIV-2606-19390:end -->

<!-- delta:SF-2026-ARXIV-2606-19390:start -->
Agentic advisory automation需把 AIBOM/SBOM、runtime activation evidence、signed CSAF-VEX与replay bundle连成同一漏洞处置链，不能仅按静态依赖宣告 affected/not affected。
<!-- delta:SF-2026-ARXIV-2606-19390:end -->

<!-- books-review:SF-2026-ARXIV-2606-19390:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`PLATFORM-SECURITY`. 运行证据可减少误报却可能漏掉潜在路径；自动VEX不能替代产品安全 owner签署与补丁验证。
<!-- books-review:SF-2026-ARXIV-2606-19390:end -->

<!-- existing:SF-2026-ARXIV-2606-19409:start -->
现有 owner 已拥有 typed Session、branch/merge/replay、runtime identity 与 controlled release；相邻 MCP 章只拥有协议交接。 Comparative result for arXiv:2606.19409v1: Ch84 已含同一 exact family 的 Session runtime value、fork/merge/replay 和 controlled-property boundary。
<!-- existing:SF-2026-ARXIV-2606-19409:end -->

<!-- delta:SF-2026-ARXIV-2606-19409:start -->
Session 应成为执行路径携带的一等 runtime value，统一 transcript、tool effect、sandbox、branch lineage、token usage、pending work 与 memory event；fork/merge/replay 是显式操作。
<!-- delta:SF-2026-ARXIV-2606-19409:end -->

<!-- books-review:SF-2026-ARXIV-2606-19409:start -->
Principle Reuse; No Change — Existing Coverage. live-provider quality、optional backend availability 与 memory quality明确未证明；central Session 也可能扩大故障域。
<!-- books-review:SF-2026-ARXIV-2606-19409:end -->

<!-- existing:SF-2026-ARXIV-2606-19464:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19464v1: Ch72 已有 policy version、obligation 与外部 reference monitor；无需复制 DSL。
<!-- existing:SF-2026-ARXIV-2606-19464:end -->

<!-- delta:SF-2026-ARXIV-2606-19464:start -->
runtime governance 除 permit/prohibit 外还需 obligation lifecycle、dispensation、meta-policy precedence 与 ontology reasoning，并在 LLM 外执行。
<!-- delta:SF-2026-ARXIV-2606-19464:end -->

<!-- books-review:SF-2026-ARXIV-2606-19464:start -->
Principle Reuse; No Change — Existing Coverage. 示例不构成吞吐、安全或完备性证明；ontology/policy conflict 仍需可信 owner 与版本治理。
<!-- books-review:SF-2026-ARXIV-2606-19464:end -->

<!-- existing:SF-2026-ARXIV-2606-19535:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19535v1: 它把 platform/kernel 纳入模型供应链的可执行 identity，而非仅记录权重 hash。
<!-- existing:SF-2026-ARXIV-2606-19535:end -->

<!-- delta:SF-2026-ARXIV-2606-19535:start -->
model artifact identity 必须绑定 serving platform/kernel；FloatDoor 通过两个 LoRA 放大 floating-point divergence 并把 platform signature 绑定恶意 task，暴露 audit/serve TOCTOU。
<!-- delta:SF-2026-ARXIV-2606-19535:end -->

<!-- books-review:SF-2026-ARXIV-2606-19535:start -->
Direct Evolution; Integrate. 攻击依赖作者平台集合与 LoRA；跨平台不一致不等于任意模型都可植入，可信构建仍需独立证明。
<!-- books-review:SF-2026-ARXIV-2606-19535:end -->

<!-- existing:SF-2026-ARXIV-2606-19544:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.19544v1: Ch66 已把 reliability、validity、bias 分离；本大样本是强验证而非新机制。
<!-- existing:SF-2026-ARXIV-2606-19544:end -->

<!-- delta:SF-2026-ARXIV-2606-19544:start -->
Judge validation 要同时报告 chance-corrected agreement、test-retest consistency 与 position/verbosity bias；高 consistency 不能替代 validity。
<!-- delta:SF-2026-ARXIV-2606-19544:end -->

<!-- books-review:SF-2026-ARXIV-2606-19544:start -->
Principle Reuse; No Change — Existing Coverage. 三个 benchmark 与单一 pairwise rubric 不证明所有 judge 场景；Cohen kappa 也依赖 prevalence。
<!-- books-review:SF-2026-ARXIV-2606-19544:end -->

<!-- existing:SF-2026-ARXIV-2606-19559:start -->
现有 owner 已拥有 ask/act gate、uncertainty decomposition、依赖图与预算；相邻 reflection 章只拥有复核。 Comparative result for arXiv:2606.19559v1: Ch79 已拥有 ask/act gate 与 uncertainty decomposition；保留跨 backbone 证据。
<!-- existing:SF-2026-ARXIV-2606-19559:end -->

<!-- delta:SF-2026-ARXIV-2606-19559:start -->
黑盒 Agent 可把 action confidence 与 request uncertainty 分开；只有后者高时触发 clarification，避免把执行不确定与需求欠规范混成 abstention。
<!-- delta:SF-2026-ARXIV-2606-19559:end -->

<!-- books-review:SF-2026-ARXIV-2606-19559:start -->
Principle Reuse; No Change — Existing Coverage. prompt-based uncertainty 未校准成概率；benchmark 人工制造 50% 欠规范，澄清成本和用户响应质量未被完整建模。
<!-- books-review:SF-2026-ARXIV-2606-19559:end -->

<!-- existing:SF-2026-ARXIV-2606-19595:start -->
现有 owner 已拥有 durable checkpoint、claim-evidence lineage、idempotent resume 与人工接管；相邻 reflection 章只提出修正信号。 Comparative result for arXiv:2606.19595v1: Ch81 已有 durable checkpoints 与 idempotent resume；IHBench补充 voice workload。
<!-- existing:SF-2026-ARXIV-2606-19595:end -->

<!-- delta:SF-2026-ARXIV-2606-19595:start -->
voice-agent interruption recovery 必须保存 workflow node、已提交 side effects 与待确认槽位，恢复时区分 resume、repair、restart。
<!-- delta:SF-2026-ARXIV-2606-19595:end -->

<!-- books-review:SF-2026-ARXIV-2606-19595:start -->
Principle Reuse; No Change — Existing Coverage. 模拟中断与语音管线不覆盖真实网络/ASR drift；恢复成功也不证明重复 effect 被阻止。
<!-- books-review:SF-2026-ARXIV-2606-19595:end -->

<!-- existing:SF-2026-ARXIV-2606-19613:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.19613v1: 它给长期 session 的 degradation/first-failure 一个不同于独立 pass@1 的 evaluation contract。
<!-- existing:SF-2026-ARXIV-2606-19613:end -->

<!-- delta:SF-2026-ARXIV-2606-19613:start -->
coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。
<!-- delta:SF-2026-ARXIV-2606-19613:end -->

<!-- books-review:SF-2026-ARXIV-2606-19613:start -->
Direct Evolution; Integrate. 程序生成 REST workload 不能代表全部软件演化；turn-to-failure 对变更难度和 harness 强敏感。
<!-- books-review:SF-2026-ARXIV-2606-19613:end -->

<!-- existing:SF-2026-ARXIV-2606-19667:start -->
现有 owner 已拥有 prefix identity、cache reuse、失效与跨请求共享边界；相邻 continuous batching 章只拥有批次调度。 Comparative result for arXiv:2606.19667v1: 它连接 RAG evidence ordering 与 prefix-cache locality，同时保持 relevance owner 不变。
<!-- existing:SF-2026-ARXIV-2606-19667:end -->

<!-- delta:SF-2026-ARXIV-2606-19667:start -->
RAG evidence set 不变时，可用近期 evidence-sequence prefix tree 重排证据，让集合重叠转成 token-prefix 重用；retriever 仍拥有 relevance，scheduler 只拥有顺序。
<!-- delta:SF-2026-ARXIV-2606-19667:end -->

<!-- books-review:SF-2026-ARXIV-2606-19667:start -->
Direct Evolution; Integrate. 重排可能改变 positional bias 与答案；局部 query locality 不保证生产 cache hit，且不减少 decode cost。
<!-- books-review:SF-2026-ARXIV-2606-19667:end -->

<!-- existing:SF-2026-ARXIV-2606-19692:start -->
Re-read `Books/part-07-agent/76-rag.md#L1` with adjacent handoff `Books/part-07-agent/77-memory.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19692:end -->

<!-- delta:SF-2026-ARXIV-2606-19692:start -->
`When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems` 路由到 `AGENT-RAG`：旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。
<!-- delta:SF-2026-ARXIV-2606-19692:end -->

<!-- books-review:SF-2026-ARXIV-2606-19692:start -->
Direct Evolution; Integrate. 结论限于单向量 cosine 检索、固定 encoder、两个 10 万文档语料和给定攻击；organic hubs 在冻结阈值下大量被标记，targeted single-query、late-interaction、multi-vector 与模型内部投毒未验证。
<!-- books-review:SF-2026-ARXIV-2606-19692:end -->

<!-- existing:SF-2026-ARXIV-2606-19704:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19704:end -->

<!-- delta:SF-2026-ARXIV-2606-19704:start -->
`Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents` 路由到 `PLATFORM-EVALUATION-SYSTEM`：它不再用单次 aggregate mean 排名决定发布，而要求 evaluation owner 保存 configuration identity，并以 in-sample/OOD rank correlation、judge-independent trajectory verifier 和持久 benchmark transport 判断配置能否外推；旧 leaderboard 可保留为观测列，不能继续拥有 release 决策。
<!-- delta:SF-2026-ARXIV-2606-19704:end -->

<!-- books-review:SF-2026-ARXIV-2606-19704:start -->
Direct Evolution; Integrate. 这是基于 AssetOpsBench 与 14 份未同行评审 implementation reports 的 position paper；作者未运行大规模 predictive-validity trial，也未证明十二层正交或排名与真实 incident/override 指标相关。
<!-- books-review:SF-2026-ARXIV-2606-19704:end -->

<!-- existing:SF-2026-ARXIV-2606-19714:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19714:end -->

<!-- delta:SF-2026-ARXIV-2606-19714:start -->
`AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing` 路由到 `PLATFORM-EVALUATION-SYSTEM`：AURA 把 judge trust 作为可更新隐状态：人类只验证 uncertainty 高的 pair，refinement 将已验证的一致性信号传播到其余比较，再更新下一轮采样；evaluation owner 而非 judge 独占抽样、停止和审计轨迹。其代价是传播错误会放大初始偏差，需保留随机抽检和预算耗尽时的原始 judge/human fallback。
<!-- delta:SF-2026-ARXIV-2606-19714:end -->

<!-- books-review:SF-2026-ARXIV-2606-19714:start -->
Direct Evolution; Integrate. 证据来自 5×640 合成比较与一组真实 pairwise judge 数据；未证明在开放域、judge 分布漂移、非 pairwise 评价或极低 human budget 下仍校准。
<!-- books-review:SF-2026-ARXIV-2606-19714:end -->

<!-- existing:SF-2026-ARXIV-2606-19719:start -->
Re-read `Books/part-07-agent/76-rag.md#L1` with adjacent handoff `Books/part-07-agent/77-memory.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19719:end -->

<!-- delta:SF-2026-ARXIV-2606-19719:start -->
`Closing the Calibration Gap in Semantic Caching` 路由到 `AGENT-RAG`：语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。
<!-- delta:SF-2026-ARXIV-2606-19719:end -->

<!-- books-review:SF-2026-ARXIV-2606-19719:start -->
Direct Evolution; Integrate. 74,265 个英文 pair、45% 正例、9 个 bi-encoder/reranker 的结果受 ParaBank2 与合成数据占比、标签噪声及部署先验约束；固定 test mix 不证明低重复率生产流量。
<!-- books-review:SF-2026-ARXIV-2606-19719:end -->

<!-- existing:SF-2026-ARXIV-2606-19746:start -->
Re-read `Books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` with adjacent handoff `Books/part-05-inference-system/46-continuous-batching.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19746:end -->

<!-- delta:SF-2026-ARXIV-2606-19746:start -->
`SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL` 路由到 `INFER-KV-CACHE`：dense-attention 时代的 RDMA 全 prefix 搬运被改为 CXL cache-line top-k 按需读取：prefill 把 KV 写入共享池，scheduler 按设备分配请求，decode GPU 只取 sparse attention 选中的条目；KV owner 从单 GPU/整块传输变成 CXL pool 与调度器协同。失败时仍需本地 DRAM/RDMA 路径，代价是 CXL 拓扑、细粒度访问和设备争用。
<!-- delta:SF-2026-ARXIV-2606-19746:end -->

<!-- books-review:SF-2026-ARXIV-2606-19746:start -->
Direct Evolution; Integrate. 只验证 DeepSeek-V3.2 AWQ4、SGLang/HiSparse、8×H20、2TB CXL、16K–128K/1K 输出；RDMA 是本机 loopback 的理想化基线，不能证明跨机、dense attention 或其它 CXL 设备收益。
<!-- books-review:SF-2026-ARXIV-2606-19746:end -->

<!-- existing:SF-2026-ARXIV-2606-19753:start -->
Re-read `Books/part-06-ai-infrastructure/73-production-best-practice.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/72-security.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19753:end -->

<!-- delta:SF-2026-ARXIV-2606-19753:start -->
`Grounded Inference: Principles for Deterministically Encapsulated Generative Models` 路由到 `PLATFORM-PRODUCTION`：该文把概率模型封装为受类型化输入、可验证输出、超时/失败状态和确定性 orchestration 约束的组件，主程序保留状态与最终 authority；但它是架构原则而非新的可复算实现，作为现有 grounded-inference 原则的补充而不追加 Books 机制。
<!-- delta:SF-2026-ARXIV-2606-19753:end -->

<!-- books-review:SF-2026-ARXIV-2606-19753:start -->
Principle Reuse; No Change — Existing Coverage. 没有公开 workload、实现 artifact 或对照实验；四个 primitive 与两个 anti-pattern 未被量化验证，不能据此声称确定性、可靠性或生产风险已经闭合。
<!-- books-review:SF-2026-ARXIV-2606-19753:end -->

<!-- existing:SF-2026-ARXIV-2606-19755:start -->
Re-read `Books/part-05-inference-system/48-speculative-decoding.md#L1` with adjacent handoff `Books/part-05-inference-system/49-tensorrt-llm.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19755:end -->

<!-- delta:SF-2026-ARXIV-2606-19755:start -->
`SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling` 路由到 `INFER-SPECULATIVE-DECODING`：SafeSpec 将安全 head 并入 target verification 的同一次前向：draft token 通过语义与风险联合门，风险触发 rollback 和 safety-guided multi-sampling，而非在 speculative path 外串联 guard。target verifier 持有 accept/rollback 控制；外部 guard 仍作为未知攻击与 head 故障 fallback。
<!-- delta:SF-2026-ARXIV-2606-19755:end -->

<!-- books-review:SF-2026-ARXIV-2606-19755:start -->
Direct Evolution; Integrate. 15% ASR 降幅与 2.06× benign speedup 绑定 Qwen3-32B、论文所列攻击集和 6×A800；latent head 不能证明新型 jailbreak、跨语言或 target/draft 变更后仍校准。
<!-- books-review:SF-2026-ARXIV-2606-19755:end -->

<!-- existing:SF-2026-ARXIV-2606-19758:start -->
Re-read `Books/part-07-agent/82-multi-agent.md#L1` with adjacent handoff `Books/part-07-agent/83-mcp.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19758:end -->

<!-- delta:SF-2026-ARXIV-2606-19758:start -->
`SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design` 路由到 `AGENT-MULTI-AGENT`：SIGMA 不把 agent node 当封闭角色，而由任务到 skill-agent incidence matrix 组合节点，再解码通信图；skill mailbox 拥有消息路由，缺 skill 或组合退化时回落到预定义 agent/topology。代价是库质量、组合搜索和 mailbox 隔离成为新的控制面。
<!-- delta:SF-2026-ARXIV-2606-19758:end -->

<!-- books-review:SF-2026-ARXIV-2606-19758:start -->
Direct Evolution; Integrate. 结果仅覆盖六个 reasoning/coding benchmark、三个 base LLM 和论文 skill libraries；0.96-point unseen-library drop 不证明开放技能供应链、权限隔离或长任务稳定性。
<!-- books-review:SF-2026-ARXIV-2606-19758:end -->

<!-- existing:SF-2026-ARXIV-2606-19769:start -->
Re-read `Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` with adjacent handoff `Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19769:end -->

<!-- delta:SF-2026-ARXIV-2606-19769:start -->
`Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI` 路由到 `MULTIMODAL-EMBODIED-VLA`：它把 humanoid 数据 owner 从孤立样本仓库提升为 lifecycle contract：每条经验绑定 body/action/task/scene/trace/outcome，并保留时间、坐标系、标定、运动学、单位、版本和 provenance；capability-specific schema 在水平标准之上扩展，旧数据只能经显式兼容层进入训练。
<!-- delta:SF-2026-ARXIV-2606-19769:end -->

<!-- books-review:SF-2026-ARXIV-2606-19769:start -->
Direct Evolution; Integrate. 材料源于 ISO/WD 26264-1 制定经验而非完成标准或跨厂商 benchmark；未证明提议字段足以消除硬件差异、隐私/IP 限制和 sim-to-real 偏移。
<!-- books-review:SF-2026-ARXIV-2606-19769:end -->

<!-- existing:SF-2026-ARXIV-2606-19795:start -->
Re-read `Books/part-07-agent/81-workflow.md#L1` with adjacent handoff `Books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19795:end -->

<!-- delta:SF-2026-ARXIV-2606-19795:start -->
`Agentic Electronic Design Automation: A Handoff Perspective` 路由到 `AGENT-WORKFLOW`：EDA agent handoff 从传文件/自然语言升级为 consumer-defined acceptance contract：artifact 连同 scope、evidence、provenance、authority 和 workflow state 传递，下一 stage 显式 accept/reject；EACP 分离 discovery、message、tool、workflow 与 security/IP 层。旧 stage-local check 共存，但不能替代跨边界交付证据。
<!-- delta:SF-2026-ARXIV-2606-19795:end -->

<!-- books-review:SF-2026-ARXIV-2606-19795:start -->
Direct Evolution; Integrate. 这是 82 个系统的 survey/protocol proposal，没有端到端 EACP 实现或 signoff benchmark；五层协议未证明能覆盖供应链 IP、工具副作用和组织级授权。
<!-- books-review:SF-2026-ARXIV-2606-19795:end -->

<!-- existing:SF-2026-ARXIV-2606-19803:start -->
Re-read `Books/part-06-ai-infrastructure/72-security.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19803:end -->

<!-- delta:SF-2026-ARXIV-2606-19803:start -->
`Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases` 路由到 `PLATFORM-SECURITY`：向量检索不再先 ANN 后应用层过滤，而把 subject/object/policy 与 approximate candidate generation 共同求解；policy engine 拥有可见集合，ANN 只在授权候选内优化 recall/latency。pre/post-filter 可作为规模与索引能力不同的共存路径，但必须分别报告漏检和越权风险。
<!-- delta:SF-2026-ARXIV-2606-19803:end -->

<!-- books-review:SF-2026-ARXIV-2606-19803:start -->
Direct Evolution; Integrate. 论文仅给 formal model 与 preliminary experiments；未覆盖动态 policy、跨租户缓存、删除一致性或所有向量数据库实现，不能宣称 FGAC 与 ANN recall 已同时普适最优。
<!-- books-review:SF-2026-ARXIV-2606-19803:end -->

<!-- existing:SF-2026-ARXIV-2606-19808:start -->
Re-read `Books/part-05-inference-system/56-inference-scheduling.md#L1` with adjacent handoff `Books/part-05-inference-system/55-pd-disaggregation.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19808:end -->

<!-- delta:SF-2026-ARXIV-2606-19808:start -->
`Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning` 路由到 `INFER-SCHEDULING`：SEVRA 把额外推理视为 serving allocation：冻结 solver 先产出 attempt，recoverability gate 决定保留、验证或 bounded retry；scheduler 拥有 token budget 和 harmful-flip 审计。较长 initial budget 在部分任务更优，因此 controller 必须与 no-verify/longer-solve 路径共存。
<!-- delta:SF-2026-ARXIV-2606-19808:end -->

<!-- books-review:SF-2026-ARXIV-2606-19808:start -->
Direct Evolution; Integrate. 76.3%/26.8% 与 transfer 数字限于 Qwen3-4B、MATH500/GSM8K/CommonsenseQA 和给定 token budgets；不证明 gate 在新模型、开放题或负载漂移下优于先增加初始预算。
<!-- books-review:SF-2026-ARXIV-2606-19808:end -->

<!-- existing:SF-2026-ARXIV-2606-19847:start -->
Re-read `Books/part-07-agent/77-memory.md#L1` with adjacent handoff `Books/part-07-agent/78-tool-calling.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19847:end -->

<!-- delta:SF-2026-ARXIV-2606-19847:start -->
`AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts` 路由到 `AGENT-MEMORY`：AtomMem 以 Fact Executor 将长对话压成高价值 atomic facts，按事件层次与 temporal profile 演化，并由 associative graph 在查询时联结；memory owner 控制 extract/update/retrieve，原始对话保留为冲突校验 fallback。代价是事实抽取错误、属性覆盖和图扩散会造成不可逆记忆漂移。
<!-- delta:SF-2026-ARXIV-2606-19847:end -->

<!-- books-review:SF-2026-ARXIV-2606-19847:start -->
Direct Evolution; Integrate. 只在 LoCoMo 的多类 reasoning 指标上比较；未证明真实多会话隐私、删除、冲突事实、跨语言或长期 profile 更新正确。
<!-- books-review:SF-2026-ARXIV-2606-19847:end -->

<!-- existing:SF-2026-ARXIV-2606-19849:start -->
Re-read `Books/part-05-inference-system/56-inference-scheduling.md#L1` with adjacent handoff `Books/part-05-inference-system/55-pd-disaggregation.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19849:end -->

<!-- delta:SF-2026-ARXIV-2606-19849:start -->
`ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference` 路由到 `INFER-SCHEDULING`：ViCoStream 将 video preprocessing、encoder、token drop、prefill/decode 统一到 chunk scheduler，以 CUDA-stream overlap、bounded visual attention 和 query retrieval 控制每 chunk 计算/内存；调度器拥有 stage backpressure，降载时通过 token retention/attention scope 回退，而非让单模块各自最大化。
<!-- delta:SF-2026-ARXIV-2606-19849:end -->

<!-- books-review:SF-2026-ARXIV-2606-19849:start -->
Direct Evolution; Integrate. 134 FPS 与 <50 ms TTFT 仅对应 Qwen2.5-VL-3B/7B、单 A100 和论文 streaming benchmarks；精度接近 full-history 不证明长时依赖、并发请求或其它 GPU。
<!-- books-review:SF-2026-ARXIV-2606-19849:end -->

<!-- existing:SF-2026-ARXIV-2606-19868:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19868:end -->

<!-- delta:SF-2026-ARXIV-2606-19868:start -->
`A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models` 路由到 `PLATFORM-EVALUATION-SYSTEM`：统一框架把 black-box UE 的 verbalization、sampling、explanation、multi-agent 与 hybrid 信号放到同一 evaluator contract；但 24 方法无单一 winner，现有评测章已包含按 task/calibration 选择 UE 的原则，因此记为 No Change。
<!-- delta:SF-2026-ARXIV-2606-19868:end -->

<!-- books-review:SF-2026-ARXIV-2606-19868:start -->
Principle Reuse; No Change — Existing Coverage. 24 方法×4 模型×4 数据设置不能证明跨 API 版本、开放生成或成本约束下的统一最优；answer-space/hybrid 优势是设置相关观察。
<!-- books-review:SF-2026-ARXIV-2606-19868:end -->

<!-- existing:SF-2026-ARXIV-2606-19887:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19887:end -->

<!-- delta:SF-2026-ARXIV-2606-19887:start -->
`FinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming` 路由到 `PLATFORM-EVALUATION-SYSTEM`：FinRED 用专家 taxonomy 生成金融 red-team 样例并由专家复核标签/可靠性，属于现有 domain-specific evaluation pipeline 的实例；它未改变通用 release owner，故只作 No Change handoff。
<!-- delta:SF-2026-ARXIV-2606-19887:end -->

<!-- books-review:SF-2026-ARXIV-2606-19887:start -->
Principle Reuse; No Change — Existing Coverage. 专家一致性和覆盖只适用于论文金融风险 taxonomy、模型与样本；未证明其它司法辖区、实时市场或非金融安全域。
<!-- books-review:SF-2026-ARXIV-2606-19887:end -->

<!-- existing:SF-2026-ARXIV-2606-19898:start -->
Re-read `Books/part-07-agent/76-rag.md#L1` with adjacent handoff `Books/part-07-agent/77-memory.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19898:end -->

<!-- delta:SF-2026-ARXIV-2606-19898:start -->
`Query-aware Routing for Filtered Approximate Nearest Neighbors Search` 路由到 `AGENT-RAG`：filtered ANN 从静态单索引选择变为 query-aware router：规则或 learned policy 依据 filter selectivity/shape 将查询送往不同索引路径；router 拥有 plan choice，监测失配时回落到精确过滤或保守规则。代价是训练分布漂移会把 latency 优化变成 recall 回归。
<!-- delta:SF-2026-ARXIV-2606-19898:end -->

<!-- books-review:SF-2026-ARXIV-2606-19898:start -->
Direct Evolution; Integrate. 实验绑定论文数据分布、filter 模式、索引实现和 recall/latency 指标；未证明动态更新、复杂布尔 policy 或跨 tenant workload。
<!-- books-review:SF-2026-ARXIV-2606-19898:end -->

<!-- existing:SF-2026-ARXIV-2606-19899:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19899:end -->

<!-- delta:SF-2026-ARXIV-2606-19899:start -->
`Measuring Biological Capabilities and Risks of AI Agents` 路由到 `PLATFORM-EVALUATION-SYSTEM`：该工作把生物能力/风险拆为可操作 task suites、agent scaffold 与分级 risk interpretation，但仍属于垂直 benchmark；现有 evaluation 章节已要求 domain expert、capability 与 misuse 分离，故不新增机制。
<!-- delta:SF-2026-ARXIV-2606-19899:end -->

<!-- books-review:SF-2026-ARXIV-2606-19899:start -->
Principle Reuse; No Change — Existing Coverage. PDF 评测不能把受测 agent 的实验室能力直接外推为现实生物危害；任务覆盖、工具 access、专家评分和风险阈值均是特定设计。
<!-- books-review:SF-2026-ARXIV-2606-19899:end -->

<!-- existing:SF-2026-ARXIV-2606-19911:start -->
Re-read `Books/part-07-agent/77-memory.md#L1` with adjacent handoff `Books/part-07-agent/78-tool-calling.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19911:end -->

<!-- delta:SF-2026-ARXIV-2606-19911:start -->
`Multi-Agent Transactive Memory` 路由到 `AGENT-MEMORY`：多 agent 记忆从各自 transcript 变为 transactive directory：agent 保存谁知道什么与证据位置，查询先路由到 memory owner 再取内容；目录过期时回落到广播/共享检索。其收益以额外索引维护、错误 expertise attribution 和隐私边界为代价。
<!-- delta:SF-2026-ARXIV-2606-19911:end -->

<!-- books-review:SF-2026-ARXIV-2606-19911:start -->
Direct Evolution; Integrate. 只在论文 multi-agent tasks、拓扑和模型上验证；未证明目录在 agent churn、对抗写入、跨组织权限或长期知识漂移下可靠。
<!-- books-review:SF-2026-ARXIV-2606-19911:end -->

<!-- existing:SF-2026-ARXIV-2606-19989:start -->
Re-read `Books/part-04-training-system/36-distributed-training.md#L1` with adjacent handoff `Books/part-04-training-system/37-tensor-parallel.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19989:end -->

<!-- delta:SF-2026-ARXIV-2606-19989:start -->
`Online Dynamic Batching with Formal Guarantees for LLM Training` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：训练 batching 从离线固定 batch 改为 online queue policy，在到达、长度与资源状态变化时决定组合，同时以形式化界约束等待/效率；scheduler 拥有 batch formation，超出假设时退回静态 bucket。代价是在线估计误差与公平性。
<!-- delta:SF-2026-ARXIV-2606-19989:end -->

<!-- books-review:SF-2026-ARXIV-2606-19989:start -->
Direct Evolution; Integrate. 形式保证依赖论文到达与成本模型；未证明真实多租户数据 loader、straggler、网络/optimizer 状态或非平稳长度分布满足假设。
<!-- books-review:SF-2026-ARXIV-2606-19989:end -->

<!-- existing:SF-2026-ARXIV-2606-19992:start -->
Re-read `Books/part-07-agent/83-mcp.md#L1` with adjacent handoff `Books/part-07-agent/84-agent-platform.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19992:end -->

<!-- delta:SF-2026-ARXIV-2606-19992:start -->
`Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services` 路由到 `AGENT-MCP`：Tool Programs 将静态 endpoint 列表变成可组合、带类型与执行语义的服务接口；服务端拥有 program validation/sandbox，agent 只提交受限程序，失败时回落到单步 endpoint。灵活性以验证复杂度、资源上界和更大的代码注入面为代价。
<!-- delta:SF-2026-ARXIV-2606-19992:end -->

<!-- books-review:SF-2026-ARXIV-2606-19992:start -->
Direct Evolution; Integrate. 实验只覆盖作者 web-service/tool tasks；未证明任意第三方 API、副作用事务、认证轮换或不可信程序可安全执行。
<!-- books-review:SF-2026-ARXIV-2606-19992:end -->

<!-- existing:SF-2026-ARXIV-2606-19998:start -->
Re-read `Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` with adjacent handoff `Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-19998:end -->

<!-- delta:SF-2026-ARXIV-2606-19998:start -->
`Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory` 路由到 `MULTIMODAL-EMBODIED-VLA`：Tri-Info 用 VLA 内部 information signals 预测 action failure，并把 abstain/fallback 交给执行控制器；旧做法只看 action likelihood 或单一 uncertainty。代价是 probe 与阈值需随 policy/environment 校准，未知 shift 时回落到人工/安全 controller。
<!-- delta:SF-2026-ARXIV-2606-19998:end -->

<!-- books-review:SF-2026-ARXIV-2606-19998:start -->
Direct Evolution; Integrate. 只在论文 VLA 模型、任务与 failure labels 上验证；离线 AUROC/检测率不证明真实机器人动作安全、因果故障或跨 embodiment 泛化。
<!-- books-review:SF-2026-ARXIV-2606-19998:end -->

<!-- existing:SF-2026-ARXIV-2606-20002:start -->
Re-read `Books/part-04-training-system/31-rlhf.md#L1` with adjacent handoff `Books/part-04-training-system/32-ppo.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20002:end -->

<!-- delta:SF-2026-ARXIV-2606-20002:start -->
`Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning` 路由到 `TRAIN-RLHF`：Connect-the-Dots 用跨 domain、跨 lifecycle 的 RL trajectory 把短任务 reward 改为长期 agent state transition 信号；trainer 拥有 curriculum、reward 与 checkpoint selection，旧单域 SFT/RL 作为稳定初始化。代价是跨域 reward leakage 和 credit assignment，失败时需回退到分域训练/验证。
<!-- delta:SF-2026-ARXIV-2606-20002:end -->

<!-- books-review:SF-2026-ARXIV-2606-20002:start -->
Direct Evolution; Integrate. 结果限于 exact-v1 domains、模型、reward verifier 和 rollout budget；未证明开放世界长期记忆、真实工具副作用或跨生命周期泛化。
<!-- books-review:SF-2026-ARXIV-2606-20002:end -->

<!-- existing:SF-2026-ARXIV-2606-20005:start -->
Re-read `Books/part-04-training-system/36-distributed-training.md#L1` with adjacent handoff `Books/part-04-training-system/37-tensor-parallel.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20005:end -->

<!-- delta:SF-2026-ARXIV-2606-20005:start -->
`StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：StreamKL 将 attention distillation 的 KL 计算分块流式执行，避免物化完整概率张量；kernel/trainer 共同拥有 block state 与数值归约，OOM 或不支持 shape 时回退到标准 KL。速度/显存换来额外 kernel、归约误差和硬件依赖。
<!-- delta:SF-2026-ARXIV-2606-20005:end -->

<!-- books-review:SF-2026-ARXIV-2606-20005:start -->
Direct Evolution; Integrate. 只验证论文 attention shapes、精度、模型与 GPU；未证明所有 vocab/sequence 规模、分布式并行或低精度下保持相同数值和收敛。
<!-- books-review:SF-2026-ARXIV-2606-20005:end -->

<!-- existing:SF-2026-ARXIV-2606-20023:start -->
Re-read `Books/part-07-agent/78-tool-calling.md#L1` with adjacent handoff `Books/part-07-agent/79-planning.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20023:end -->

<!-- delta:SF-2026-ARXIV-2606-20023:start -->
`When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents` 路由到 `AGENT-TOOL-CALLING`：工具选择不再只优化成功率，而先求满足任务的最小 capability set；planner 提议工具，policy layer 比较 privilege lattice 后降权/拒绝 over-privileged choice，并保留必要时显式 escalation。代价是 capability annotation 不全会误拒绝或低估组合权限。
<!-- delta:SF-2026-ARXIV-2606-20023:end -->

<!-- books-review:SF-2026-ARXIV-2606-20023:start -->
Direct Evolution; Integrate. 测量与 mitigation 绑定论文 agent/tool suites 和 privilege labels；未证明动态 OAuth scope、跨工具权限合成或恶意 metadata。
<!-- books-review:SF-2026-ARXIV-2606-20023:end -->

<!-- existing:SF-2026-ARXIV-2606-20047:start -->
Re-read `Books/part-07-agent/75-context.md#L1` with adjacent handoff `Books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20047:end -->

<!-- delta:SF-2026-ARXIV-2606-20047:start -->
`PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents` 路由到 `AGENT-CONTEXT`：PACMS 把 context assembly 表述为预算约束 submodular selection：独立 engine 根据 relevance、coverage 与 redundancy 选取片段，agent 消费带 provenance 的 context；不足时回落到更大窗口或检索重试。代价是 utility surrogate 可能遗漏依赖和顺序。
<!-- delta:SF-2026-ARXIV-2606-20047:end -->

<!-- books-review:SF-2026-ARXIV-2606-20047:start -->
Direct Evolution; Integrate. 评测限于论文任务、预算、retriever 与 utility 定义；submodular 近似不证明长依赖、冲突证据或对抗 context 下答案正确。
<!-- books-review:SF-2026-ARXIV-2606-20047:end -->

<!-- existing:SF-2026-ARXIV-2606-20113:start -->
Re-read `Books/part-07-agent/78-tool-calling.md#L1` with adjacent handoff `Books/part-07-agent/79-planning.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20113:end -->

<!-- delta:SF-2026-ARXIV-2606-20113:start -->
`When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation` 路由到 `AGENT-TOOL-CALLING`：streaming tool use 不应在第一个 token 触发；controller 追踪 tool-intent 随解码的稳定度，在置信轨迹达到阈值后才 dispatch，未稳定则继续生成或回落到完整 query。它用 latency 换误调用率，并要求 cancellation/duplicate suppression。
<!-- delta:SF-2026-ARXIV-2606-20113:end -->

<!-- books-review:SF-2026-ARXIV-2606-20113:start -->
Direct Evolution; Integrate. 稳定阈值与收益只在论文 retrieval tasks、模型、网络延迟和工具集上测得；未证明有副作用工具、长参数或分布漂移。
<!-- books-review:SF-2026-ARXIV-2606-20113:end -->

<!-- existing:SF-2026-ARXIV-2606-20122:start -->
Re-read `Books/part-07-agent/79-planning.md#L1` with adjacent handoff `Books/part-07-agent/80-reflection.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20122:end -->

<!-- delta:SF-2026-ARXIV-2606-20122:start -->
`ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research` 路由到 `AGENT-PLANNING`：ScaffoldAgent 将 deep-research outline 变成可迭代控制状态：每轮按预期 utility 增删/重排子目标，再据证据覆盖继续搜索；planner 拥有 outline version，budget 用尽则冻结当前结构并交给 verifier。代价是 utility 估计会偏向易检索证据。
<!-- delta:SF-2026-ARXIV-2606-20122:end -->

<!-- books-review:SF-2026-ARXIV-2606-20122:start -->
Direct Evolution; Integrate. 实验仅覆盖论文开放研究任务、搜索后端和 judge；未证明 factuality、source authority、长时间网页漂移或真实研究验收。
<!-- books-review:SF-2026-ARXIV-2606-20122:end -->

<!-- existing:SF-2026-ARXIV-2606-20128:start -->
Re-read `Books/part-04-training-system/36-distributed-training.md#L1` with adjacent handoff `Books/part-04-training-system/37-tensor-parallel.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20128:end -->

<!-- delta:SF-2026-ARXIV-2606-20128:start -->
`The Correctness Illusion in LLM-Generated GPU Kernels` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：GPU kernel 验收从单设备单输入通过改为 CPU oracle、跨 shape/dtype/GPU differential testing 与 clean controls；release owner 保存失败 witness，并在 verdict 不一致时拒绝上线或回退原 kernel。代价是 oracle/设备矩阵成本和未覆盖输入。
<!-- delta:SF-2026-ARXIV-2606-20128:end -->

<!-- books-review:SF-2026-ARXIV-2606-20128:start -->
Direct Evolution; Integrate. 24/26 ops 与 RTX3060/A10/L40S/A100/H100 的测试仍不穷尽未定义行为、驱动版本、并发或大模型端到端性能。
<!-- books-review:SF-2026-ARXIV-2606-20128:end -->

<!-- existing:SF-2026-ARXIV-2606-20158:start -->
Re-read `Books/part-07-agent/81-workflow.md#L1` with adjacent handoff `Books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20158:end -->

<!-- delta:SF-2026-ARXIV-2606-20158:start -->
`N-Version Programming with Coding Agents` 路由到 `AGENT-WORKFLOW`：N-version coding agents 并行产出独立实现，由测试/静态检查和 adjudicator 汇合，而非信任单次生成；workflow owner 管理 diversity、quorum 与 fallback 到人工。额外 token/latency 的收益依赖故障独立性，相关 hallucination 会击穿多数表决。
<!-- delta:SF-2026-ARXIV-2606-20158:end -->

<!-- books-review:SF-2026-ARXIV-2606-20158:start -->
Direct Evolution; Integrate. 结果只覆盖论文 coding tasks、agent versions 与 test suites；未证明安全漏洞、缺失 oracle、共享训练数据导致的相关错误。
<!-- books-review:SF-2026-ARXIV-2606-20158:end -->

<!-- existing:SF-2026-ARXIV-2606-20235:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20235:end -->

<!-- delta:SF-2026-ARXIV-2606-20235:start -->
`ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments` 路由到 `PLATFORM-EVALUATION-SYSTEM`：ScholarQuest 提供 taxonomy-guided academic-search benchmark，但没有改变 evaluation/release 控制权或现有 paper-search owner，因此不追加 Books。
<!-- delta:SF-2026-ARXIV-2606-20235:end -->

<!-- books-review:SF-2026-ARXIV-2606-20235:start -->
Principle Reuse; No Change — Existing Coverage. benchmark 覆盖开放文献环境与既定 taxonomy；分数不证明封闭数据库、未来索引、全文权限或科研结论正确。
<!-- books-review:SF-2026-ARXIV-2606-20235:end -->

<!-- existing:SF-2026-ARXIV-2606-20243:start -->
Re-read `Books/part-07-agent/81-workflow.md#L1` with adjacent handoff `Books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20243:end -->

<!-- delta:SF-2026-ARXIV-2606-20243:start -->
`Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs` 路由到 `AGENT-WORKFLOW`：Phoenix 的 multi-agent issue-resolution safety pipeline 已被 workflow 章的隔离执行、review gate 与 rollback 原则覆盖；本日只保留实现 handoff，不重复 owner。
<!-- delta:SF-2026-ARXIV-2606-20243:end -->

<!-- books-review:SF-2026-ARXIV-2606-20243:start -->
Principle Reuse; No Change — Existing Coverage. GitHub issues、repositories、tests 与 agent 配置是特定实验；测试通过不证明 supply-chain、secret、部署或未测试行为安全。
<!-- books-review:SF-2026-ARXIV-2606-20243:end -->

<!-- existing:SF-2026-ARXIV-2606-20245:start -->
Re-read `Books/part-07-agent/75-context.md#L1` with adjacent handoff `Books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20245:end -->

<!-- delta:SF-2026-ARXIV-2606-20245:start -->
`Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference` 路由到 `AGENT-CONTEXT`：显式 parametric/context knowledge conflict resolution 属于现有 context provenance 与冲突裁决路径；该研究没有新增跨系统 state owner，故 No Change。
<!-- delta:SF-2026-ARXIV-2606-20245:end -->

<!-- books-review:SF-2026-ARXIV-2606-20245:start -->
Principle Reuse; No Change — Existing Coverage. 实验只验证给定冲突构造、模型和问答集；显式选择不能证明来源真实性、时效性或隐式冲突被发现。
<!-- books-review:SF-2026-ARXIV-2606-20245:end -->

<!-- existing:SF-2026-ARXIV-2606-20254:start -->
Re-read `Books/part-06-ai-infrastructure/72-security.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20254:end -->

<!-- delta:SF-2026-ARXIV-2606-20254:start -->
`Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic` 路由到 `PLATFORM-SECURITY`：量化不再被当作纯压缩步骤：security owner 将 quantization-conditioned backdoor 视作可分离 task vector，在发布前比较全精度/量化行为并用 task arithmetic 移除，再做 clean/attack 双验收。无法分离时回退到拒绝量化模型。
<!-- delta:SF-2026-ARXIV-2606-20254:end -->

<!-- books-review:SF-2026-ARXIV-2606-20254:start -->
Direct Evolution; Integrate. 移除效果限于论文 backdoor construction、模型、bit-width 与 calibration data；未证明未知触发器、其它量化器或 task-vector subtraction 不损害能力。
<!-- books-review:SF-2026-ARXIV-2606-20254:end -->

<!-- existing:SF-2026-ARXIV-2606-20318:start -->
Re-read `Books/part-06-ai-infrastructure/73-production-best-practice.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/72-security.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20318:end -->

<!-- delta:SF-2026-ARXIV-2606-20318:start -->
`AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads` 路由到 `PLATFORM-PRODUCTION`：AgenticDB 将数据库 reconfiguration 变成 telemetry→proposal→sandbox evaluation→guarded apply→rollback 的闭环；DB control plane 而非 LLM 持有变更权限和状态版本。代价是试验流量与错误 cost model，fallback 为上一配置和人工 approval。
<!-- delta:SF-2026-ARXIV-2606-20318:end -->

<!-- books-review:SF-2026-ARXIV-2606-20318:start -->
Direct Evolution; Integrate. 结果绑定论文 workloads、DBMS、动作空间和离线/沙箱指标；未证明生产突发流量、数据迁移、锁竞争或跨版本自动演进安全。
<!-- books-review:SF-2026-ARXIV-2606-20318:end -->

<!-- existing:SF-2026-ARXIV-2606-20363:start -->
Re-read `Books/part-07-agent/84-agent-platform.md#L1` with adjacent handoff `Books/part-07-agent/83-mcp.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20363:end -->

<!-- delta:SF-2026-ARXIV-2606-20363:start -->
`Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining` 路由到 `AGENT-PLATFORM`：SKILL.md 不再完全手写，而从 computer-use trajectory 中抽取可复用步骤、前置条件和 recovery，经过评测后发布；skill registry 拥有版本/验证，agent 只消费已批准 artifact。错误归纳时回退原 trajectory 或人工 skill。
<!-- delta:SF-2026-ARXIV-2606-20363:end -->

<!-- books-review:SF-2026-ARXIV-2606-20363:start -->
Direct Evolution; Integrate. 实验覆盖论文应用、轨迹质量和 computer-use agent；未证明 UI 漂移、敏感动作、跨 OS 或生成 skill 的供应链安全。
<!-- books-review:SF-2026-ARXIV-2606-20363:end -->

<!-- existing:SF-2026-ARXIV-2606-20374:start -->
Re-read `Books/part-06-ai-infrastructure/69-trace.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/70-cost.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20374:end -->

<!-- delta:SF-2026-ARXIV-2606-20374:start -->
`ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters` 路由到 `PLATFORM-TRACE`：ARGUS 将万卡训练诊断从节点日志提升为跨 rank/collective/network/storage 的统一 trace identity；collector 控制采样与时钟映射，diagnoser 只在证据图上定位瓶颈，超预算时降采样并保留关键 span。代价是 telemetry overhead 与相关性误判。
<!-- delta:SF-2026-ARXIV-2606-20374:end -->

<!-- books-review:SF-2026-ARXIV-2606-20374:start -->
Direct Evolution; Integrate. 生产观察来自特定 >10,000-GPU 集群、训练栈和故障集；trace 覆盖与诊断时延不证明因果根因、其它 fabric 或故障自动修复。
<!-- books-review:SF-2026-ARXIV-2606-20374:end -->

<!-- existing:SF-2026-ARXIV-2606-20381:start -->
Re-read `Books/part-04-training-system/36-distributed-training.md#L1` with adjacent handoff `Books/part-04-training-system/37-tensor-parallel.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20381:end -->

<!-- delta:SF-2026-ARXIV-2606-20381:start -->
`Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：UFP4 针对 FP4 pretraining 的 shrinkage bias 重新分配量化几何与 scaling，使 optimizer/quantizer 共同拥有低精度状态；异常 loss 时回退 BF16/更高精度。显存/吞吐收益以 recipe、kernel 和收敛敏感性为代价。
<!-- delta:SF-2026-ARXIV-2606-20381:end -->

<!-- books-review:SF-2026-ARXIV-2606-20381:start -->
Direct Evolution; Integrate. 只在 exact-v1 模型规模、token budget、FP4 hardware/simulation 与下游评测验证；未证明更长预训练、其它 optimizer 或最终能力无回归。
<!-- books-review:SF-2026-ARXIV-2606-20381:end -->

<!-- existing:SF-2026-ARXIV-2606-20408:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20408:end -->

<!-- delta:SF-2026-ARXIV-2606-20408:start -->
`NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms` 路由到 `PLATFORM-EVALUATION-SYSTEM`：NRT-Bench 将 operator-agent red teaming 组织成多轮控制室状态、攻击轨迹和 safety-critical acceptance，但作为垂直 benchmark 已被通用多轮安全评测契约覆盖，故 No Change。
<!-- delta:SF-2026-ARXIV-2606-20408:end -->

<!-- books-review:SF-2026-ARXIV-2606-20408:start -->
Principle Reuse; No Change — Existing Coverage. 任务、模拟控制室、attackers 与 judges 不等同真实基础设施；benchmark 成功/失败不能外推为生产控制权限或事故风险。
<!-- books-review:SF-2026-ARXIV-2606-20408:end -->

<!-- existing:SF-2026-ARXIV-2606-20470:start -->
Re-read `Books/part-06-ai-infrastructure/72-security.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20470:end -->

<!-- delta:SF-2026-ARXIV-2606-20470:start -->
`Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems` 路由到 `PLATFORM-SECURITY`：防御不只阻断 model-guided attacker，还可发布受控假信号改变攻击者 belief/update path；defender 拥有 decoy 状态与撤销，真实 agent state 不暴露。代价是误导污染 observability 与合法调试，故必须与直接拒绝、隔离和审计共存。
<!-- delta:SF-2026-ARXIV-2606-20470:end -->

<!-- books-review:SF-2026-ARXIV-2606-20470:start -->
Direct Evolution; Integrate. 结果来自论文 attack/defense simulation；未证明真实攻击者适应、法律/伦理约束、side channel 或 decoy 不伤害正常 agent。
<!-- books-review:SF-2026-ARXIV-2606-20470:end -->

<!-- existing:SF-2026-ARXIV-2606-20474:start -->
Re-read `Books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` with adjacent handoff `Books/part-05-inference-system/46-continuous-batching.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20474:end -->

<!-- delta:SF-2026-ARXIV-2606-20474:start -->
`UltraQuant: 4-bit KV Caching for Context-Heavy Agents` 路由到 `INFER-KV-CACHE`：UltraQuant 将 agent 长上下文 KV 压到 4-bit，并分别控制 token/channel quantization 与 runtime dequant；cache manager 持有 format metadata，质量回归时按 layer/request 回退高精度。收益以 kernel 复杂度、误差累积和 workload sensitivity 为代价。
<!-- delta:SF-2026-ARXIV-2606-20474:end -->

<!-- books-review:SF-2026-ARXIV-2606-20474:start -->
Direct Evolution; Integrate. 质量与系统数字限于论文 models、context-heavy agent workloads、长度和 hardware；未证明极长上下文、不同 attention、并发 tail latency 或所有任务无损。
<!-- books-review:SF-2026-ARXIV-2606-20474:end -->

<!-- existing:SF-2026-ARXIV-2606-20475:start -->
Re-read `Books/part-07-agent/77-memory.md#L1` with adjacent handoff `Books/part-07-agent/78-tool-calling.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20475:end -->

<!-- delta:SF-2026-ARXIV-2606-20475:start -->
`Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution` 路由到 `AGENT-MEMORY`：memory self-evolution 不按单轮 reward 覆盖旧记忆，而累计候选记忆相对基线的 marginal advantage，再由 memory owner 决定 promote/retain/evict；低置信时保留旧版本。代价是 delayed credit 与 evaluator bias 会固化错误。
<!-- delta:SF-2026-ARXIV-2606-20475:end -->

<!-- books-review:SF-2026-ARXIV-2606-20475:start -->
Direct Evolution; Integrate. 实验仅覆盖论文 agents、tasks、judge 与 memory budget；未证明非平稳长期用户、对抗记忆或跨任务 advantage 可比较。
<!-- books-review:SF-2026-ARXIV-2606-20475:end -->

<!-- existing:SF-2026-ARXIV-2606-20487:start -->
Re-read `Books/part-07-agent/81-workflow.md#L1` with adjacent handoff `Books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20487:end -->

<!-- delta:SF-2026-ARXIV-2606-20487:start -->
`Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems` 路由到 `AGENT-WORKFLOW`：跨设备 agent 从全局 replanning 改为层级 recovery：设备局部 controller 先修复可逆错误，跨设备依赖破坏才升级 workflow planner；handoff state 保存 checkpoint/compensation。代价是故障分类错误，fallback 为全局重规划或人工。
<!-- delta:SF-2026-ARXIV-2606-20487:end -->

<!-- books-review:SF-2026-ARXIV-2606-20487:start -->
Direct Evolution; Integrate. 只验证论文 devices、tasks、failure injection 与 latency；未证明真实设备副作用、网络 partition、并发用户或补偿完整。
<!-- books-review:SF-2026-ARXIV-2606-20487:end -->

<!-- existing:SF-2026-ARXIV-2606-20493:start -->
Re-read `Books/part-07-agent/82-multi-agent.md#L1` with adjacent handoff `Books/part-07-agent/83-mcp.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20493:end -->

<!-- delta:SF-2026-ARXIV-2606-20493:start -->
`Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems` 路由到 `AGENT-MULTI-AGENT`：它把 evaluator preference 看作多-agent 图上的传播状态，要求 evaluation owner 跟踪 judge influence/依赖，而非把 agent votes 当独立样本；检测到 contagion 时使用隔离 judge 或独立 anchor。代价是图估计与额外评审成本。
<!-- delta:SF-2026-ARXIV-2606-20493:end -->

<!-- books-review:SF-2026-ARXIV-2606-20493:start -->
Direct Evolution; Integrate. 结果来自论文 contagion model、拓扑和 LLM judges；未证明真实组织评审、隐藏共享训练或动态 agent 网络中的因果传播。
<!-- books-review:SF-2026-ARXIV-2606-20493:end -->

<!-- existing:SF-2026-ARXIV-2606-20502:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20502:end -->

<!-- delta:SF-2026-ARXIV-2606-20502:start -->
`Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software` 路由到 `PLATFORM-EVALUATION-SYSTEM`：该研究表明 vulnerability detector 可校准却不理解漏洞，支持现有 evaluation 章分离 confidence calibration 与 semantic correctness 的原则；没有新的长期 owner，故 No Change。
<!-- delta:SF-2026-ARXIV-2606-20502:end -->

<!-- books-review:SF-2026-ARXIV-2606-20502:start -->
Principle Reuse; No Change — Existing Coverage. 结果绑定 systems-software 数据集、fine-tuning recipe、模型与漏洞标签；校准曲线不能证明新代码、组合漏洞或真实 exploitability。
<!-- books-review:SF-2026-ARXIV-2606-20502:end -->

<!-- existing:SF-2026-ARXIV-2606-20510:start -->
Re-read `Books/part-07-agent/81-workflow.md#L1` with adjacent handoff `Books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20510:end -->

<!-- delta:SF-2026-ARXIV-2606-20510:start -->
`Efficient and Sound Probabilistic Verification for AI Agents` 路由到 `AGENT-WORKFLOW`：概率 verification 将 agent policy 的不确定转移纳入可计算验收，通过 relaxation 在 sound bound 与成本间调节；verifier 拥有 accept/reject，超时或 bound 过松时回退 conservative rule/human review。代价是状态抽象与概率模型误设。
<!-- delta:SF-2026-ARXIV-2606-20510:end -->

<!-- books-review:SF-2026-ARXIV-2606-20510:start -->
Direct Evolution; Integrate. soundness 只对论文形式假设、抽象与概率界成立；实验不证明开放工具环境、非平稳 policy 或未建模副作用。
<!-- books-review:SF-2026-ARXIV-2606-20510:end -->

<!-- existing:SF-2026-ARXIV-2606-20512:start -->
Re-read `Books/part-07-agent/74-prompt.md#L1` with adjacent handoff `Books/part-07-agent/75-context.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20512:end -->

<!-- delta:SF-2026-ARXIV-2606-20512:start -->
`Probe-and-Refine Tuning of Repository Guidance for Coding Agents` 路由到 `AGENT-PROMPT`：repository guidance 从静态 README/AGENTS 文本变为 probe-and-refine：运行 coding agent，定位失败 step，再在固定 step budget 内修改 guidance 并跨模型验证；repo owner 持有发布/回滚，过拟合时保留旧指导。代价是 probe 成本和 benchmark leakage。
<!-- delta:SF-2026-ARXIV-2606-20512:end -->

<!-- books-review:SF-2026-ARXIV-2606-20512:start -->
Direct Evolution; Integrate. 结果限于论文 repositories、tasks、agents 和 step budget；未证明未来代码变化、隐藏测试、安全规范或跨模型长期泛化。
<!-- books-review:SF-2026-ARXIV-2606-20512:end -->

<!-- existing:SF-2026-ARXIV-2606-20520:start -->
Re-read `Books/part-06-ai-infrastructure/72-security.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20520:end -->

<!-- delta:SF-2026-ARXIV-2606-20520:start -->
`Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes` 路由到 `PLATFORM-SECURITY`：Sovereign Execution Broker 将 prompt 声明的权限替换为 certificate-bound authority：principal 提交带 scope/expiry 的证书，broker 在工具执行前验证、记录并可 revoke；agent 不持有最终执行权。证书/身份漂移时 fail closed，并与人工 break-glass 共存。
<!-- delta:SF-2026-ARXIV-2606-20520:end -->

<!-- books-review:SF-2026-ARXIV-2606-20520:start -->
Direct Evolution; Integrate. evaluation 只覆盖论文 broker、capability 和 attack scenarios；未证明所有第三方工具、密钥轮换、跨域 trust root 或 broker compromise。
<!-- books-review:SF-2026-ARXIV-2606-20520:end -->

<!-- existing:SF-2026-ARXIV-2606-20529:start -->
Re-read `Books/part-07-agent/77-memory.md#L1` with adjacent handoff `Books/part-07-agent/78-tool-calling.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20529:end -->

<!-- delta:SF-2026-ARXIV-2606-20529:start -->
`LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents` 路由到 `AGENT-MEMORY`：LedgerAgent 将 policy-relevant state 记录为结构化 append-only ledger，planner 每次工具调用前读取约束并提交可审计 transition；ledger/policy engine 拥有状态，LLM 不能静默改写。解析冲突时拒绝或转人工。代价是 schema 覆盖与写放大。
<!-- delta:SF-2026-ARXIV-2606-20529:end -->

<!-- books-review:SF-2026-ARXIV-2606-20529:start -->
Direct Evolution; Integrate. 实验限于论文 tool tasks、policy set 与 ledger parser；未证明并发事务、隐式状态、恶意工具返回或长期 ledger 压缩。
<!-- books-review:SF-2026-ARXIV-2606-20529:end -->

<!-- existing:SF-2026-ARXIV-2606-20536:start -->
Re-read `Books/part-06-ai-infrastructure/66-evaluation-system.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20536:end -->

<!-- delta:SF-2026-ARXIV-2606-20536:start -->
`The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation` 路由到 `PLATFORM-EVALUATION-SYSTEM`：FID 验收从单次 seed 分数改为显式训练 seed×生成 seed 分布与置信区间；evaluation owner 保存随机性来源，release 依据分布而非最好一次。增加重复成本，预算不足时至少报告 seed sensitivity 而非隐藏。
<!-- delta:SF-2026-ARXIV-2606-20536:end -->

<!-- books-review:SF-2026-ARXIV-2606-20536:start -->
Direct Evolution; Integrate. 数百个 SiT 网络和 ImageNet-256 的方差结论不证明其它生成架构、数据、采样器或人类质量；FID 本身仍不是完整质量/安全指标。
<!-- books-review:SF-2026-ARXIV-2606-20536:end -->

<!-- existing:SF-2026-ARXIV-2606-20537:start -->
Re-read `Books/part-05-inference-system/42-what-happens-during-inference.md#L1` with adjacent handoff `Books/part-05-inference-system/43-prefill.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20537:end -->

<!-- delta:SF-2026-ARXIV-2606-20537:start -->
`Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving` 路由到 `INFER-REQUEST-LIFECYCLE`：Execution-State Capsule 在 graph-boundary 捕获可恢复的静态 buffer/执行状态，使 on-device small-batch serving 可 checkpoint/restore，而非重建整个 runtime；FlashRT 拥有 capsule schema 与兼容性，失配时冷启动。代价是图绑定、静态内存和 backend 特化。
<!-- delta:SF-2026-ARXIV-2606-20537:end -->

<!-- books-review:SF-2026-ARXIV-2606-20537:start -->
Direct Evolution; Integrate. 只验证 NVIDIA CUDA backend、论文 graph/model/batch 和设备；未证明跨 driver/backend、故障一致性、并发恢复或生产 tail latency。
<!-- books-review:SF-2026-ARXIV-2606-20537:end -->

<!-- existing:SF-2026-ARXIV-2606-20545:start -->
Re-read `Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` with adjacent handoff `Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20545:end -->

<!-- delta:SF-2026-ARXIV-2606-20545:start -->
`Current World Models Lack a Persistent State Core` 路由到 `MULTIMODAL-WORLD-MODELS`：WRBench 把 camera motion 当 observability intervention，依次验证相机执行、在视场内连续性、离开视场后的状态演化和重新观察一致性；world-model evaluator 拥有 persistent-state verdict，普通 fidelity 指标仅并列。失败时回到显式 state memory/受限 camera。
<!-- delta:SF-2026-ARXIV-2606-20545:end -->

<!-- books-review:SF-2026-ARXIV-2606-20545:start -->
Direct Evolution; Integrate. benchmark 只诊断论文 world models、camera paths 与 human calibration；未证明真实物理状态、因果动力学、长期遮挡或安全控制。
<!-- books-review:SF-2026-ARXIV-2606-20545:end -->

<!-- existing:SF-2026-ARXIV-2606-20553:start -->
Re-read `Books/part-06-ai-infrastructure/72-security.md#L1` with adjacent handoff `Books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20553:end -->

<!-- delta:SF-2026-ARXIV-2606-20553:start -->
`From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning` 路由到 `PLATFORM-SECURITY`：联邦微调的效率路径被证明可承载 privacy backdoor；release contract 因此要在 client update 聚合前后检测泄漏触发与 utility，并由 server 持有 quarantine/rollback。安全聚合与效率优化需和隐私 red-team 共存。
<!-- delta:SF-2026-ARXIV-2606-20553:end -->

<!-- books-review:SF-2026-ARXIV-2606-20553:start -->
Direct Evolution; Integrate. 攻击与防御只在论文 FL topology、语言模型、clients 和 triggers 上验证；未证明 secure aggregation、异构数据或未知 covert channel。
<!-- books-review:SF-2026-ARXIV-2606-20553:end -->

<!-- existing:SF-2026-ARXIV-2606-20562:start -->
Re-read `Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` with adjacent handoff `Books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-20562:end -->

<!-- delta:SF-2026-ARXIV-2606-20562:start -->
`MemoryWAM: Efficient World Action Modeling with Persistent Memory` 路由到 `MULTIMODAL-EMBODIED-VLA`：MemoryWAM 将 world-action model 的历史压入 persistent memory，在新 observation/action 时选择性读取和更新，使状态不完全依赖当前窗口；memory controller 拥有写入/遗忘，漂移时清空或回退无记忆 model。代价是错误状态累积和额外带宽。
<!-- delta:SF-2026-ARXIV-2606-20562:end -->

<!-- books-review:SF-2026-ARXIV-2606-20562:start -->
Direct Evolution; Integrate. 实验限于论文 environments、horizons、models 和 memory sizes；未证明真实机器人、不可逆动作、长期漂移或 memory poisoning。
<!-- books-review:SF-2026-ARXIV-2606-20562:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260619-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260619 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260619: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260619-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-19376; review:SF-2026-ARXIV-2606-19380; review:SF-2026-ARXIV-2606-19382; review:SF-2026-ARXIV-2606-19386; review:SF-2026-ARXIV-2606-19390; review:SF-2026-ARXIV-2606-19409; review:SF-2026-ARXIV-2606-19464; review:SF-2026-ARXIV-2606-19535; review:SF-2026-ARXIV-2606-19544; review:SF-2026-ARXIV-2606-19559; review:SF-2026-ARXIV-2606-19595; review:SF-2026-ARXIV-2606-19613; review:SF-2026-ARXIV-2606-19667; review:SF-2026-ARXIV-2606-19692; review:SF-2026-ARXIV-2606-19704; review:SF-2026-ARXIV-2606-19714; review:SF-2026-ARXIV-2606-19719; review:SF-2026-ARXIV-2606-19746; review:SF-2026-ARXIV-2606-19753; review:SF-2026-ARXIV-2606-19755; review:SF-2026-ARXIV-2606-19758; review:SF-2026-ARXIV-2606-19769; review:SF-2026-ARXIV-2606-19795; review:SF-2026-ARXIV-2606-19803; review:SF-2026-ARXIV-2606-19808; review:SF-2026-ARXIV-2606-19847; review:SF-2026-ARXIV-2606-19849; review:SF-2026-ARXIV-2606-19868; review:SF-2026-ARXIV-2606-19887; review:SF-2026-ARXIV-2606-19898; review:SF-2026-ARXIV-2606-19899; review:SF-2026-ARXIV-2606-19911; review:SF-2026-ARXIV-2606-19989; review:SF-2026-ARXIV-2606-19992; review:SF-2026-ARXIV-2606-19998; review:SF-2026-ARXIV-2606-20002; review:SF-2026-ARXIV-2606-20005; review:SF-2026-ARXIV-2606-20023; review:SF-2026-ARXIV-2606-20047; review:SF-2026-ARXIV-2606-20113; review:SF-2026-ARXIV-2606-20122; review:SF-2026-ARXIV-2606-20128; review:SF-2026-ARXIV-2606-20158; review:SF-2026-ARXIV-2606-20235; review:SF-2026-ARXIV-2606-20243; review:SF-2026-ARXIV-2606-20245; review:SF-2026-ARXIV-2606-20254; review:SF-2026-ARXIV-2606-20318; review:SF-2026-ARXIV-2606-20363; review:SF-2026-ARXIV-2606-20374; review:SF-2026-ARXIV-2606-20381; review:SF-2026-ARXIV-2606-20408; review:SF-2026-ARXIV-2606-20470; review:SF-2026-ARXIV-2606-20474; review:SF-2026-ARXIV-2606-20475; review:SF-2026-ARXIV-2606-20487; review:SF-2026-ARXIV-2606-20493; review:SF-2026-ARXIV-2606-20502; review:SF-2026-ARXIV-2606-20510; review:SF-2026-ARXIV-2606-20512; review:SF-2026-ARXIV-2606-20520; review:SF-2026-ARXIV-2606-20529; review:SF-2026-ARXIV-2606-20536; review:SF-2026-ARXIV-2606-20537; review:SF-2026-ARXIV-2606-20545; review:SF-2026-ARXIV-2606-20553; review:SF-2026-ARXIV-2606-20562 | EVIDENCE-OWNER-REBUILD-20260619: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260619-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-19376; analysis-decision:SF-2026-ARXIV-2606-19380; analysis-decision:SF-2026-ARXIV-2606-19382; analysis-decision:SF-2026-ARXIV-2606-19386; analysis-decision:SF-2026-ARXIV-2606-19390; analysis-decision:SF-2026-ARXIV-2606-19409; analysis-decision:SF-2026-ARXIV-2606-19464; analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT; analysis-decision:SF-2026-ARXIV-2606-19544; analysis-decision:SF-2026-ARXIV-2606-19559; analysis-decision:SF-2026-ARXIV-2606-19595; analysis-decision:SF-2026-ARXIV-2606-19613; analysis-decision:SF-2026-ARXIV-2606-19667; analysis-decision:SF-2026-ARXIV-2606-19692; analysis-decision:SF-2026-ARXIV-2606-19704; analysis-decision:SF-2026-ARXIV-2606-19714; analysis-decision:SF-2026-ARXIV-2606-19719; analysis-decision:SF-2026-ARXIV-2606-19746; analysis-decision:SF-2026-ARXIV-2606-19753; analysis-decision:SF-2026-ARXIV-2606-19755; analysis-decision:SF-2026-ARXIV-2606-19758; analysis-decision:SF-2026-ARXIV-2606-19769; analysis-decision:SF-2026-ARXIV-2606-19795; analysis-decision:SF-2026-ARXIV-2606-19803; analysis-decision:SF-2026-ARXIV-2606-19808; analysis-decision:SF-2026-ARXIV-2606-19847; analysis-decision:SF-2026-ARXIV-2606-19849; analysis-decision:SF-2026-ARXIV-2606-19868; analysis-decision:SF-2026-ARXIV-2606-19887; analysis-decision:SF-2026-ARXIV-2606-19898; analysis-decision:SF-2026-ARXIV-2606-19899; analysis-decision:SF-2026-ARXIV-2606-19911; analysis-decision:SF-2026-ARXIV-2606-19989; analysis-decision:SF-2026-ARXIV-2606-19992; analysis-decision:SF-2026-ARXIV-2606-19998; analysis-decision:SF-2026-ARXIV-2606-20002; analysis-decision:SF-2026-ARXIV-2606-20005; analysis-decision:SF-2026-ARXIV-2606-20023; analysis-decision:SF-2026-ARXIV-2606-20047; analysis-decision:SF-2026-ARXIV-2606-20113; analysis-decision:SF-2026-ARXIV-2606-20122; analysis-decision:SF-2026-ARXIV-2606-20128; analysis-decision:SF-2026-ARXIV-2606-20158; analysis-decision:SF-2026-ARXIV-2606-20235; analysis-decision:SF-2026-ARXIV-2606-20243; analysis-decision:SF-2026-ARXIV-2606-20245; analysis-decision:SF-2026-ARXIV-2606-20254; analysis-decision:SF-2026-ARXIV-2606-20318; analysis-decision:SF-2026-ARXIV-2606-20363; analysis:DA-20260619-TRACE-10K-GPU; analysis-decision:SF-2026-ARXIV-2606-20381; analysis-decision:SF-2026-ARXIV-2606-20408; analysis-decision:SF-2026-ARXIV-2606-20470; analysis-decision:SF-2026-ARXIV-2606-20474; analysis-decision:SF-2026-ARXIV-2606-20475; analysis-decision:SF-2026-ARXIV-2606-20487; analysis-decision:SF-2026-ARXIV-2606-20493; analysis-decision:SF-2026-ARXIV-2606-20502; analysis-decision:SF-2026-ARXIV-2606-20510; analysis-decision:SF-2026-ARXIV-2606-20512; analysis:DA-20260619-CERTIFICATE-AUTHORITY; analysis-decision:SF-2026-ARXIV-2606-20529; analysis-decision:SF-2026-ARXIV-2606-20536; analysis-decision:SF-2026-ARXIV-2606-20537; analysis-decision:SF-2026-ARXIV-2606-20545; analysis-decision:SF-2026-ARXIV-2606-20553; analysis-decision:SF-2026-ARXIV-2606-20562 | SELECTION-OWNER-REBUILD-20260619: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260619-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-19376; books-review:SF-2026-ARXIV-2606-19380; books-review:SF-2026-ARXIV-2606-19382; books-review:SF-2026-ARXIV-2606-19386; books-review:SF-2026-ARXIV-2606-19390; books-review:SF-2026-ARXIV-2606-19409; books-review:SF-2026-ARXIV-2606-19464; books-review:SF-2026-ARXIV-2606-19535; books-review:SF-2026-ARXIV-2606-19544; books-review:SF-2026-ARXIV-2606-19559; books-review:SF-2026-ARXIV-2606-19595; books-review:SF-2026-ARXIV-2606-19613; books-review:SF-2026-ARXIV-2606-19667; books-review:SF-2026-ARXIV-2606-19692; books-review:SF-2026-ARXIV-2606-19704; books-review:SF-2026-ARXIV-2606-19714; books-review:SF-2026-ARXIV-2606-19719; books-review:SF-2026-ARXIV-2606-19746; books-review:SF-2026-ARXIV-2606-19753; books-review:SF-2026-ARXIV-2606-19755; books-review:SF-2026-ARXIV-2606-19758; books-review:SF-2026-ARXIV-2606-19769; books-review:SF-2026-ARXIV-2606-19795; books-review:SF-2026-ARXIV-2606-19803; books-review:SF-2026-ARXIV-2606-19808; books-review:SF-2026-ARXIV-2606-19847; books-review:SF-2026-ARXIV-2606-19849; books-review:SF-2026-ARXIV-2606-19868; books-review:SF-2026-ARXIV-2606-19887; books-review:SF-2026-ARXIV-2606-19898; books-review:SF-2026-ARXIV-2606-19899; books-review:SF-2026-ARXIV-2606-19911; books-review:SF-2026-ARXIV-2606-19989; books-review:SF-2026-ARXIV-2606-19992; books-review:SF-2026-ARXIV-2606-19998; books-review:SF-2026-ARXIV-2606-20002; books-review:SF-2026-ARXIV-2606-20005; books-review:SF-2026-ARXIV-2606-20023; books-review:SF-2026-ARXIV-2606-20047; books-review:SF-2026-ARXIV-2606-20113; books-review:SF-2026-ARXIV-2606-20122; books-review:SF-2026-ARXIV-2606-20128; books-review:SF-2026-ARXIV-2606-20158; books-review:SF-2026-ARXIV-2606-20235; books-review:SF-2026-ARXIV-2606-20243; books-review:SF-2026-ARXIV-2606-20245; books-review:SF-2026-ARXIV-2606-20254; books-review:SF-2026-ARXIV-2606-20318; books-review:SF-2026-ARXIV-2606-20363; books-review:SF-2026-ARXIV-2606-20374; books-review:SF-2026-ARXIV-2606-20381; books-review:SF-2026-ARXIV-2606-20408; books-review:SF-2026-ARXIV-2606-20470; books-review:SF-2026-ARXIV-2606-20474; books-review:SF-2026-ARXIV-2606-20475; books-review:SF-2026-ARXIV-2606-20487; books-review:SF-2026-ARXIV-2606-20493; books-review:SF-2026-ARXIV-2606-20502; books-review:SF-2026-ARXIV-2606-20510; books-review:SF-2026-ARXIV-2606-20512; books-review:SF-2026-ARXIV-2606-20520; books-review:SF-2026-ARXIV-2606-20529; books-review:SF-2026-ARXIV-2606-20536; books-review:SF-2026-ARXIV-2606-20537; books-review:SF-2026-ARXIV-2606-20545; books-review:SF-2026-ARXIV-2606-20553; books-review:SF-2026-ARXIV-2606-20562 | BOOKS-OWNER-REBUILD-20260619: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

The 488 family-specific closures remain row-addressable in `denominator-full-semantic-audit-v1.tsv`; keyword routing was recall-only and all 110 route-negative identities were audited.

### Materials and Access

- 68/68 exact-v1 identities completed full-text review. 66 used official arXiv HTML, `2606.19899v1` used the official PDF, and `2606.20820v1` used the official arXiv v1 identity plus an explicitly recorded exact-v1 full-text fallback because the official body reader returned a cache miss/404.

## 9. Recommended Action

- Final Books disposition: 56 Integrate across 23 unique owner files; 12 No Change handoffs.
- Books Gate Passed after the 68/68 post-write fresh audit.
- Preserve the frozen denominator and reopen only when versioned primary evidence changes a recorded mechanism, owner, evaluation contract or non-proof boundary.

## 10. Repository Changes

- Root wrote 56 source-family deltas into 23 shared Books owners; this presentation migration changed only the 2026-06-19 Daily, its source packet, and date-specific finalizer/audit files.

## 11. Open Questions

- How should cache-line sparse-KV transport adapt when CXL topology or attention sparsity differs from the evaluated 8×H20 setup?
- Which trace identities remain stable enough to support causal diagnosis across 10,000-GPU training retries?
- How should certificate-bound agent authority compose with external tools whose revoke and key-lifecycle semantics are weaker?
- These are research continuations, not unresolved Gate blockers.

## 12. Sources

- [Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees](https://arxiv.org/abs/2606.19376v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [ClayBuddy: A Framework, Evaluation, & Mitigation of Coding Agent Failures](https://arxiv.org/abs/2606.19380v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling](https://arxiv.org/abs/2606.19382v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence](https://arxiv.org/abs/2606.19386v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework](https://arxiv.org/abs/2606.19390v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [OpenRath: Session-Centered Runtime State for Agent Systems](https://arxiv.org/abs/2606.19409v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Deontic Policies for Runtime Governance of Agentic AI Systems](https://arxiv.org/abs/2606.19464v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [FloatDoor: Platform-Triggered Backdoors in LLMs](https://arxiv.org/abs/2606.19535v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](https://arxiv.org/abs/2606.19544v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Uncertainty Decomposition for Clarification Seeking in LLM Agents](https://arxiv.org/abs/2606.19559v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows](https://arxiv.org/abs/2606.19595v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns](https://arxiv.org/abs/2606.19613v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference](https://arxiv.org/abs/2606.19667v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems](https://arxiv.org/abs/2606.19692v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents](https://arxiv.org/abs/2606.19704v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing](https://arxiv.org/abs/2606.19714v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Closing the Operational Gap in Semantic Caching](https://arxiv.org/abs/2606.19719v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL](https://arxiv.org/abs/2606.19746v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Grounded Inference: Principles for Deterministically Encapsulated Generative Models](https://arxiv.org/abs/2606.19753v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling](https://arxiv.org/abs/2606.19755v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design](https://arxiv.org/abs/2606.19758v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI](https://arxiv.org/abs/2606.19769v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Agentic Electronic Design Automation: A Handoff Perspective](https://arxiv.org/abs/2606.19795v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases](https://arxiv.org/abs/2606.19803v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning](https://arxiv.org/abs/2606.19808v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](https://arxiv.org/abs/2606.19847v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference](https://arxiv.org/abs/2606.19849v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models](https://arxiv.org/abs/2606.19868v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [FinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming](https://arxiv.org/abs/2606.19887v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Query-aware Routing for Filtered Approximate Nearest Neighbors Search](https://arxiv.org/abs/2606.19898v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Measuring Biological Capabilities and Risks of AI Agents](https://arxiv.org/abs/2606.19899v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Multi-Agent Transactive Memory](https://arxiv.org/abs/2606.19911v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Online Dynamic Batching with Formal Guarantees for LLM Training](https://arxiv.org/abs/2606.19989v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services](https://arxiv.org/abs/2606.19992v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory](https://arxiv.org/abs/2606.19998v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning](https://arxiv.org/abs/2606.20002v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation](https://arxiv.org/abs/2606.20005v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents](https://arxiv.org/abs/2606.20023v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents](https://arxiv.org/abs/2606.20047v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation](https://arxiv.org/abs/2606.20113v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research](https://arxiv.org/abs/2606.20122v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [The Correctness Illusion in LLM-Generated GPU Kernels](https://arxiv.org/abs/2606.20128v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [N-Version Programming with Coding Agents](https://arxiv.org/abs/2606.20158v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments](https://arxiv.org/abs/2606.20235v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs](https://arxiv.org/abs/2606.20243v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference](https://arxiv.org/abs/2606.20245v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic](https://arxiv.org/abs/2606.20254v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads](https://arxiv.org/abs/2606.20318v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining](https://arxiv.org/abs/2606.20363v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters](https://arxiv.org/abs/2606.20374v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe](https://arxiv.org/abs/2606.20381v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms](https://arxiv.org/abs/2606.20408v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems](https://arxiv.org/abs/2606.20470v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/abs/2606.20474v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution](https://arxiv.org/abs/2606.20475v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems](https://arxiv.org/abs/2606.20487v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.20493v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software](https://arxiv.org/abs/2606.20502v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Efficient and Sound Probabilistic Verification for AI Agents](https://arxiv.org/abs/2606.20510v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Probe-and-Refine Tuning of Repository Guidance for Coding Agents](https://arxiv.org/abs/2606.20512v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes](https://arxiv.org/abs/2606.20520v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents](https://arxiv.org/abs/2606.20529v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation](https://arxiv.org/abs/2606.20536v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving](https://arxiv.org/abs/2606.20537v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [Current World Models Lack a Persistent State Core](https://arxiv.org/abs/2606.20545v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning](https://arxiv.org/abs/2606.20553v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
- [MemoryWAM: Efficient World Action Modeling with Persistent Memory](https://arxiv.org/abs/2606.20562v1) — first-public（Asia/Shanghai）：2026-06-19；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`Passed`；Completion Status=`Complete`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
