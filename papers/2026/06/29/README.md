# Daily Research — 2026-06-29

**Research Date:** 2026-06-29

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-28 09:00:00 ～ 2026-06-29 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
北京时间窗口 [2026-06-28 09:00, 2026-06-29 09:00) 枚举 262 个注册 identity；fresh freeze 为 86 retained + 176 family-specific closures。86/86 exact-v1 Evidence、full-frontier Selection 与 post-write Books audit 已完成。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-29 |
| Window End | 2026-06-29 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-29:3f607817d0a16d2b |
| Denominator Frozen At | 2026-08-29T22:30:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-28T09:00:00+08:00 | 2026-06-29T09:00:00+08:00 | 2026-08-29T22:30:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 380 | SF-2026-ARXIV-2606-27406;SF-2026-ARXIV-2606-27409;SF-2026-ARXIV-2606-27416;SF-2026-ARXIV-2606-27457;SF-2026-ARXIV-2606-27472;SF-2026-ARXIV-2606-27474;SF-2026-ARXIV-2606-27483;SF-2026-ARXIV-2606-27492;SF-2026-ARXIV-2606-27499;SF-2026-ARXIV-2606-27510;SF-2026-ARXIV-2606-27511;SF-2026-ARXIV-2606-27550;SF-2026-ARXIV-2606-27558;SF-2026-ARXIV-2606-27567;SF-2026-ARXIV-2606-27578;SF-2026-ARXIV-2606-27580;SF-2026-ARXIV-2606-27595;SF-2026-ARXIV-2606-27608;SF-2026-ARXIV-2606-27622;SF-2026-ARXIV-2606-27632;SF-2026-ARXIV-2606-27634;SF-2026-ARXIV-2606-27650;SF-2026-ARXIV-2606-27669;SF-2026-ARXIV-2606-27679;SF-2026-ARXIV-2606-27681;SF-2026-ARXIV-2606-27683;SF-2026-ARXIV-2606-27704;SF-2026-ARXIV-2606-27709;SF-2026-ARXIV-2606-27732;SF-2026-ARXIV-2606-27739;SF-2026-ARXIV-2606-27743;SF-2026-ARXIV-2606-27757;SF-2026-ARXIV-2606-27780;SF-2026-ARXIV-2606-27791;SF-2026-ARXIV-2606-27797;SF-2026-ARXIV-2606-27806;SF-2026-ARXIV-2606-27814;SF-2026-ARXIV-2606-27826;SF-2026-ARXIV-2606-27841;SF-2026-ARXIV-2606-27866;SF-2026-ARXIV-2606-27906;SF-2026-ARXIV-2606-27934;SF-2026-ARXIV-2606-27936;SF-2026-ARXIV-2606-27944;SF-2026-ARXIV-2606-27962;SF-2026-ARXIV-2606-27976;SF-2026-ARXIV-2606-27997;SF-2026-ARXIV-2606-28011;SF-2026-ARXIV-2606-28013;SF-2026-ARXIV-2606-28037;SF-2026-ARXIV-2606-28050;SF-2026-ARXIV-2606-28061;SF-2026-ARXIV-2606-28070;SF-2026-ARXIV-2606-28116;SF-2026-ARXIV-2606-28128;SF-2026-ARXIV-2606-28153;SF-2026-ARXIV-2606-28166;SF-2026-ARXIV-2606-28187;SF-2026-ARXIV-2606-28235;SF-2026-ARXIV-2606-28276;SF-2026-ARXIV-2606-28277;SF-2026-ARXIV-2606-28279;SF-2026-ARXIV-2606-28322 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260629/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260629; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260629 |
<!-- coverage:SRC-ARXIV:20260629:start -->
Fresh reconciliation: 262 = 86 + 176; Core 184=76+108; keyword 26=8+18; route-negative 52=2+50. Fresh-context audit checked all 85 first-freeze retained and all 177 first-freeze closures, including 52/52 route-negative identities; one false negative (2606.29328) was reinstated and the denominator re-froze at 86/176.
<!-- coverage:SRC-ARXIV:20260629:end -->


<!-- latest-contract-reopen:2026-06-29:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-29:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **380** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **63** 条是旧报告 retained provenance，**317** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27406 | arXiv:2606.27406v1 | paper-v1:2606.27406 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27406 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27409 | arXiv:2606.27409v1 | paper-v1:2606.27409 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27409 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-27409 | yes |
| SF-2026-ARXIV-2606-27416 | arXiv:2606.27416v1 | paper-v1:2606.27416 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27416 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27457 | arXiv:2606.27457v1 | paper-v1:2606.27457 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27457 | self | — | new_in_window | PLATFORM-GATEWAY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27457 | yes |
| SF-2026-ARXIV-2606-27472 | arXiv:2606.27472v1 | paper-v1:2606.27472 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27472 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27472 | yes |
| SF-2026-ARXIV-2606-27474 | arXiv:2606.27474v1 | paper-v1:2606.27474 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27474 | self | — | new_in_window | INFER-DECODE | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27483 | arXiv:2606.27483v1 | paper-v1:2606.27483 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27483 | self | — | new_in_window | AGENT-PLANNING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27492 | arXiv:2606.27492v1 | paper-v1:2606.27492 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27492 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27492 | yes |
| SF-2026-ARXIV-2606-27499 | arXiv:2606.27499v1 | paper-v1:2606.27499 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27499 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27510 | arXiv:2606.27510v1 | paper-v1:2606.27510 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27510 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27511 | arXiv:2606.27511v1 | paper-v1:2606.27511 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27511 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27550 | arXiv:2606.27550v1 | paper-v1:2606.27550 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27550 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27558 | arXiv:2606.27558v1 | paper-v1:2606.27558 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27558 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27558 | yes |
| SF-2026-ARXIV-2606-27567 | arXiv:2606.27567v1 | paper-v1:2606.27567 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27567 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27567 | yes |
| SF-2026-ARXIV-2606-27578 | arXiv:2606.27578v1 | paper-v1:2606.27578 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27578 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-27578 | yes |
| SF-2026-ARXIV-2606-27580 | arXiv:2606.27580v1 | paper-v1:2606.27580 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27580 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-27580 | yes |
| SF-2026-ARXIV-2606-27595 | arXiv:2606.27595v1 | paper-v1:2606.27595 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27595 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27608 | arXiv:2606.27608v1 | paper-v1:2606.27608 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27608 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27622 | arXiv:2606.27622v1 | paper-v1:2606.27622 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27622 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27632 | arXiv:2606.27632v1 | paper-v1:2606.27632 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27632 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27632 | yes |
| SF-2026-ARXIV-2606-27634 | arXiv:2606.27634v1 | paper-v1:2606.27634 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27634 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27634 | yes |
| SF-2026-ARXIV-2606-27650 | arXiv:2606.27650v1 | paper-v1:2606.27650 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27650 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27650 | yes |
| SF-2026-ARXIV-2606-27669 | arXiv:2606.27669v1 | paper-v1:2606.27669 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27669 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27669 | yes |
| SF-2026-ARXIV-2606-27679 | arXiv:2606.27679v1 | paper-v1:2606.27679 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27679 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27679 | yes |
| SF-2026-ARXIV-2606-27681 | arXiv:2606.27681v1 | paper-v1:2606.27681 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27681 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-27681 | yes |
| SF-2026-ARXIV-2606-27683 | arXiv:2606.27683v1 | paper-v1:2606.27683 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27683 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27683 | yes |
| SF-2026-ARXIV-2606-27704 | arXiv:2606.27704v1 | paper-v1:2606.27704 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27704 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27704 | yes |
| SF-2026-ARXIV-2606-27709 | arXiv:2606.27709v1 | paper-v1:2606.27709 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27709 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27709 | yes |
| SF-2026-ARXIV-2606-27732 | arXiv:2606.27732v1 | paper-v1:2606.27732 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27732 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2606-27732 | yes |
| SF-2026-ARXIV-2606-27739 | arXiv:2606.27739v1 | paper-v1:2606.27739 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27739 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27739 | yes |
| SF-2026-ARXIV-2606-27743 | arXiv:2606.27743v1 | paper-v1:2606.27743 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27743 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27743 | yes |
| SF-2026-ARXIV-2606-27757 | arXiv:2606.27757v1 | paper-v1:2606.27757 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27757 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27757 | yes |
| SF-2026-ARXIV-2606-27780 | arXiv:2606.27780v1 | paper-v1:2606.27780 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27780 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27780 | yes |
| SF-2026-ARXIV-2606-27791 | arXiv:2606.27791v1 | paper-v1:2606.27791 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27791 | self | — | new_in_window | MODEL-LONG-CONTEXT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27797 | arXiv:2606.27797v1 | paper-v1:2606.27797 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27797 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-27797 | yes |
| SF-2026-ARXIV-2606-27806 | arXiv:2606.27806v1 | paper-v1:2606.27806 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27806 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-27806 | yes |
| SF-2026-ARXIV-2606-27814 | arXiv:2606.27814v1 | paper-v1:2606.27814 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27814 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27814 | yes |
| SF-2026-ARXIV-2606-27826 | arXiv:2606.27826v1 | paper-v1:2606.27826 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27826 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27826 | yes |
| SF-2026-ARXIV-2606-27841 | arXiv:2606.27841v1 | paper-v1:2606.27841 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 1 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27841 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2606-27841 | yes |
| SF-2026-ARXIV-2606-27866 | arXiv:2606.27866v1 | paper-v1:2606.27866 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27866 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27866 | yes |
| SF-2026-ARXIV-2606-27906 | arXiv:2606.27906v1 | paper-v1:2606.27906 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27906 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-27906 | yes |
| SF-2026-ARXIV-2606-27934 | arXiv:2606.27934v1 | paper-v1:2606.27934 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27934 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27934 | yes |
| SF-2026-ARXIV-2606-27936 | arXiv:2606.27936v1 | paper-v1:2606.27936 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27936 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27936 | yes |
| SF-2026-ARXIV-2606-27944 | arXiv:2606.27944v1 | paper-v1:2606.27944 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27944 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27944 | yes |
| SF-2026-ARXIV-2606-27962 | arXiv:2606.27962v1 | paper-v1:2606.27962 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27962 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27962 | yes |
| SF-2026-ARXIV-2606-27976 | arXiv:2606.27976v1 | paper-v1:2606.27976 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27976 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27976 | yes |
| SF-2026-ARXIV-2606-27997 | arXiv:2606.27997v1 | paper-v1:2606.27997 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27997 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27997 | yes |
| SF-2026-ARXIV-2606-28011 | arXiv:2606.28011v1 | paper-v1:2606.28011 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28011 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28011 | yes |
| SF-2026-ARXIV-2606-28013 | arXiv:2606.28013v1 | paper-v1:2606.28013 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28013 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-28013 | yes |
| SF-2026-ARXIV-2606-28037 | arXiv:2606.28037v1 | paper-v1:2606.28037 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28037 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28037 | yes |
| SF-2026-ARXIV-2606-28050 | arXiv:2606.28050v1 | paper-v1:2606.28050 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28050 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28050 | yes |
| SF-2026-ARXIV-2606-28061 | arXiv:2606.28061v1 | paper-v1:2606.28061 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28061 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28061 | yes |
| SF-2026-ARXIV-2606-28070 | arXiv:2606.28070v1 | paper-v1:2606.28070 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28070 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28070 | yes |
| SF-2026-ARXIV-2606-28116 | arXiv:2606.28116v1 | paper-v1:2606.28116 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28116 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-28116 | yes |
| SF-2026-ARXIV-2606-28128 | arXiv:2606.28128v1 | paper-v1:2606.28128 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28128 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28128 | yes |
| SF-2026-ARXIV-2606-28153 | arXiv:2606.28153v1 | paper-v1:2606.28153 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28153 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28153 | yes |
| SF-2026-ARXIV-2606-28166 | arXiv:2606.28166v1 | paper-v1:2606.28166 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28166 | self | — | new_in_window | TRAIN-GRPO | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28187 | arXiv:2606.28187v1 | paper-v1:2606.28187 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28187 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28187 | yes |
| SF-2026-ARXIV-2606-28235 | arXiv:2606.28235v1 | paper-v1:2606.28235 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28235 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28235 | yes |
| SF-2026-ARXIV-2606-28276 | arXiv:2606.28276v1 | paper-v1:2606.28276 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28276 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-28276 | yes |
| SF-2026-ARXIV-2606-28277 | arXiv:2606.28277v1 | paper-v1:2606.28277 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28277 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28277 | yes |
| SF-2026-ARXIV-2606-28279 | arXiv:2606.28279v1 | paper-v1:2606.28279 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28279 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28279 | yes |
| SF-2026-ARXIV-2606-28322 | arXiv:2606.28322v1 | paper-v1:2606.28322 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28322 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28322 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27406 | RP-ff4d8b3c768a8d7d | deep | arXiv:2606.27406v1 | SRC-ARXIV@arXiv:2606.27406v1 | arXiv:2606.27406v1 — §2 Data; §3 Metrics; §4 Experiment Setup | arXiv:2606.27406v1 — §5 Results Discussion | arXiv:2606.27406v1 — §6 Limitations; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27406 | complete |
| SF-2026-ARXIV-2606-27409 | RP-6114a85b2caa1cdb | deep | arXiv:2606.27409v1 | SRC-ARXIV@arXiv:2606.27409v1 | arXiv:2606.27409v1 — §3 Model; §4 Stability and the verification dose; §5 Optimal corrector placement | arXiv:2606.27409v1 — §7 Empirical validation; §7.1 Onset at the predicted dose limit (RQ1) | arXiv:2606.27409v1 — §8 Discussion; §10 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27409 | complete |
| SF-2026-ARXIV-2606-27416 | RP-a2ddedc8576f9465 | deep | arXiv:2606.27416v1 | SRC-ARXIV@arXiv:2606.27416v1 | arXiv:2606.27416v1 — §3 System; §3.1 Architecture and seven principles; §5 The framework in use | arXiv:2606.27416v1 — §Evaluation regime.; §Workflow, provenance, and experiment management.; §4.3 Headline result | arXiv:2606.27416v1 — §Limitations.; §Appendix D Observed failure modes | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27416 | complete |
| SF-2026-ARXIV-2606-27457 | RP-1cfc84a115498ec9 | deep | arXiv:2606.27457v1 | SRC-ARXIV@arXiv:2606.27457v1 | arXiv:2606.27457v1 — §Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving; §3 System Overview; §Appendix B Framework Extensibility: AIME Pool Expansion | arXiv:2606.27457v1 — §4.3 Pareto Analysis and Model Selection; §7 Experiments and Results; §Appendix A Inference Setup | arXiv:2606.27457v1 — §8 Conclusion and Future Work; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27457 | complete |
| SF-2026-ARXIV-2606-27472 | RP-ae5f1ee39782ee1d | deep | arXiv:2606.27472v1 | SRC-ARXIV@arXiv:2606.27472v1 | arXiv:2606.27472v1 — §Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents; §Memory systems and RL for memory.; §Deployed memory systems. | arXiv:2606.27472v1 — §Long-term memory benchmarks.; §4 Experimental Setup; §Training setup. | arXiv:2606.27472v1 — §Failure modes.; §6 Discussion; §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27472 | complete |
| SF-2026-ARXIV-2606-27474 | RP-8913eeb813709902 | deep | arXiv:2606.27474v1 | SRC-ARXIV@arXiv:2606.27474v1 | arXiv:2606.27474v1 — §3. Multi-stage systems need component-level reporting. | arXiv:2606.27474v1 — §Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks; §3 Evaluation Setup; §3.2 Evaluation protocols | arXiv:2606.27474v1 — §5 Discussion: Lessons for Evaluating Hybrid Generation; §7 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27474 | complete |
| SF-2026-ARXIV-2606-27483 | RP-bddbd294e08b108a | deep | arXiv:2606.27483v1 | SRC-ARXIV@arXiv:2606.27483v1 | arXiv:2606.27483v1 — §Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning; §2.2 Mid-training in large language models; §3 Methodology | arXiv:2606.27483v1 — §5 Experiments; §5.1 Experiment setup; §5.2 Main results | arXiv:2606.27483v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27483 | complete |
| SF-2026-ARXIV-2606-27492 | RP-67dd5303105cdf20 | deep | arXiv:2606.27492v1 | SRC-ARXIV@arXiv:2606.27492v1 | arXiv:2606.27492v1 — §Skill routing, ecosystems, and failure modes.; §3 Method; §3.5 Skill Evolution: From Generated Evidence to Design Rules | arXiv:2606.27492v1 — §4 Experiments; §4.1 Evaluation Tasks; §4.2 Experimental Rationale | arXiv:2606.27492v1 — §Skill routing, ecosystems, and failure modes.; §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27492 | complete |
| SF-2026-ARXIV-2606-27499 | RP-0a0291fc9f98f16b | deep | arXiv:2606.27499v1 | SRC-ARXIV@arXiv:2606.27499v1 | arXiv:2606.27499v1 — §Text-side memory systems.; §Vision-side memory systems.; §DualMem is the strongest architecture. | arXiv:2606.27499v1 — §Why existing benchmarks cannot answer this.; §Agent memory benchmarks.; §3.3 Efficient evaluation: the rollout tree | arXiv:2606.27499v1 — §6 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27499 | complete |
| SF-2026-ARXIV-2606-27510 | RP-f30ba47b9ab45f95 | deep | arXiv:2606.27510v1 | SRC-ARXIV@arXiv:2606.27510v1 | arXiv:2606.27510v1 — §Counterfactual prompt design. | arXiv:2606.27510v1 — §5.2 Diagnosing Activation Patching Results | arXiv:2606.27510v1 — §6 Discussion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27510 | complete |
| SF-2026-ARXIV-2606-27511 | RP-f10610270467f5ed | deep | arXiv:2606.27511v1 | SRC-ARXIV@arXiv:2606.27511v1 | arXiv:2606.27511v1 — §When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems; §2.3 Fine-Tuning Strategies in FL Training; §5 Methodology | arXiv:2606.27511v1 — §6 Evaluations; §6.1 Experimental Setup; §Appendix C Experiment Details. | arXiv:2606.27511v1 — §2.4 Federated LLMs and Server-side Threats; §3 Threat Model; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27511 | complete |
| SF-2026-ARXIV-2606-27550 | RP-14a7c73d36065c45 | deep | arXiv:2606.27550v1 | SRC-ARXIV@arXiv:2606.27550v1 | arXiv:2606.27550v1 — §3 Optimizing Task-Specific Greedy Draft Trees; §4 Inference-Time Tree Scheduler | arXiv:2606.27550v1 — §5 Evaluation Methodology; §6 Results | arXiv:2606.27550v1 — §Appendix C More Frontiers | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27550 | complete |
| SF-2026-ARXIV-2606-27558 | RP-111f940dddbd116c | deep | arXiv:2606.27558v1 | SRC-ARXIV@arXiv:2606.27558v1 | arXiv:2606.27558v1 — §1.2. Design Principles & Evolution; §1.3. The PPRE Method; §5. PPRE Fairness Metric Algorithms | arXiv:2606.27558v1 — §7. Production Deployment and Evaluation | arXiv:2606.27558v1 — §8. Discussion; §8.1.1. Measurement Quality Discussion; §8.5. Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27558 | complete |
| SF-2026-ARXIV-2606-27567 | RP-bc95333fec80125c | deep | arXiv:2606.27567v1 | SRC-ARXIV@arXiv:2606.27567v1 | arXiv:2606.27567v1 — §2 Formal Framework; §Architectures outside scope. | arXiv:2606.27567v1 — §4.7 Main Result: Impossibility of Perfect Semantic-Faithful Control; §8 Connection to Existing Results; §Impossibility results in AI. | arXiv:2606.27567v1 — §3 Threat Model and Scope; §9 Discussion; §10 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27567 | complete |
| SF-2026-ARXIV-2606-27578 | RP-6364b961ea2df9f4 | deep | arXiv:2606.27578v1 | SRC-ARXIV@arXiv:2606.27578v1 | arXiv:2606.27578v1 — §2 Method; §Base-model training details. | arXiv:2606.27578v1 — §2.3 PRISM setup and base reward model; §3 Experiments | arXiv:2606.27578v1 — §3.9 Ablations and failure cases; §4 Discussion; §5 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27578 | complete |
| SF-2026-ARXIV-2606-27580 | RP-1f165b600801df71 | deep | arXiv:2606.27580v1 | SRC-ARXIV@arXiv:2606.27580v1 | arXiv:2606.27580v1 — §2 Method: Retroactive Advantage Correction | arXiv:2606.27580v1 — §Setup.; §K = 2 K{=}2 result and cost-quality Pareto.; §Scope of the closed-form result. | arXiv:2606.27580v1 — §4 Conclusion; §Appendix E Limitations and Discussion; §Background and discussion. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27580 | complete |
| SF-2026-ARXIV-2606-27595 | RP-11749e97f76006c9 | deep | arXiv:2606.27595v1 | SRC-ARXIV@arXiv:2606.27595v1 | arXiv:2606.27595v1 — §The Ko-WideSearch Benchmark; §Construction Pipeline; §Normalization-Aware Cell Comparison | arXiv:2606.27595v1 — §Experimental Setup; §Results; §Scoring Details | arXiv:2606.27595v1 — §Conclusion and Limitations; §Limitations. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27595 | complete |
| SF-2026-ARXIV-2606-27608 | RP-090459f56826d1d5 | deep | arXiv:2606.27608v1 | SRC-ARXIV@arXiv:2606.27608v1 | arXiv:2606.27608v1 — §3.1 Reward Model Training Paradigms; §Training; §4.1 Training Pipeline | arXiv:2606.27608v1 — §Evaluation; §Text-to-image generation results.; §Human preference evaluation. | arXiv:2606.27608v1 — §Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27608 | complete |
| SF-2026-ARXIV-2606-27622 | RP-42fab4a5e9c3867c | deep | arXiv:2606.27622v1 | SRC-ARXIV@arXiv:2606.27622v1 | arXiv:2606.27622v1 — §II-A Background on Byzantine-Robust FL Methods; §II-B FLTrust Algorithm | arXiv:2606.27622v1 — §IV Evaluation; §IV-A Experimental Setup; §IV-A 4 Extension Setup | arXiv:2606.27622v1 — §V Discussion and Limitations; §V-C Limitations for Data Poisoning Attacks; §VI Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27622 | complete |
| SF-2026-ARXIV-2606-27632 | RP-fcbc4265f52dcdfb | deep | arXiv:2606.27632v1 | SRC-ARXIV@arXiv:2606.27632v1 | https://arxiv.org/html/2606.27632v1 — §2 Content-Safety-Oriented Data System; 3 Yuvion LLM: Progressive Safety Training Paradigm; 3.2 Target Capability Design | https://arxiv.org/html/2606.27632v1 — §4 Evaluation Framework; 4.2 Level 1: Open-source General Benchmarks; 4.3 Level 2: Open-source Content Safety Benchmarks | https://arxiv.org/html/2606.27632v1 — §Discussion.; 9 Conclusion; 10 Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27632 | complete |
| SF-2026-ARXIV-2606-27634 | RP-75996c215715c982 | standard | arXiv:2606.27634v1 | SRC-ARXIV@arXiv:2606.27634v1 | https://arxiv.org/html/2606.27634v1 — §4.0.4 Training Procedure | https://arxiv.org/html/2606.27634v1 — §Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis; 2.0.1 Continual Learning and Evaluation of Language Models.; 3.2 Model Checkpoints and Evaluation | https://arxiv.org/html/2606.27634v1 — §6 Conclusion; 6.0.1 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27634 | complete |
| SF-2026-ARXIV-2606-27650 | RP-ef58e045338123ab | standard | arXiv:2606.27650v1 | SRC-ARXIV@arXiv:2606.27650v1 | https://arxiv.org/html/2606.27650v1 — §Context Design and Coverage; 6 Platform Architecture; 6.1 System Overview | https://arxiv.org/html/2606.27650v1 — §7 Evaluation Cases and Scalability; 7.1 Evaluation Cases; 7.1.5 Scalability Analysis | https://arxiv.org/html/2606.27650v1 — §8 Discussion; Limitations and Future Work; 9 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27650 | complete |
| SF-2026-ARXIV-2606-27669 | RP-ceffdfb9a0b8de47 | deep | arXiv:2606.27669v1 | SRC-ARXIV@arXiv:2606.27669v1 | https://arxiv.org/html/2606.27669v1 — §4 Methodology of Dataset Construction; Benchmark Design and Methodology.; Evaluation Framework and User Simulator. | https://arxiv.org/html/2606.27669v1 — §2.1 Web Search Benchmark; 2.2 Ambiguity Benchmark; 2.3 Interactive Clarification Benchmark | https://arxiv.org/html/2606.27669v1 — §Search-heavy guessing reveals a major failure mode.; 6 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27669 | complete |
| SF-2026-ARXIV-2606-27679 | RP-f4a08ba2915c4ee6 | standard | arXiv:2606.27679v1 | SRC-ARXIV@arXiv:2606.27679v1 | https://arxiv.org/html/2606.27679v1 — §Probe Training.; Probe Architecture and Training Size. | https://arxiv.org/html/2606.27679v1 — §Toolkits, Benchmarks, and Evaluation.; 3.1 Experimental Setup; Evaluation Metrics. | https://arxiv.org/html/2606.27679v1 — §4.2 Results and Discussion; 5 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27679 | complete |
| SF-2026-ARXIV-2606-27681 | RP-856e55a15de3a886 | deep | arXiv:2606.27681v1 | SRC-ARXIV@arXiv:2606.27681v1 | https://arxiv.org/html/2606.27681v1 — §Proposition 2 (Non-identifiability under leaky architectures) .; Proposition 3 (Training–inference consistency) .; 4.2 Model Architecture | https://arxiv.org/html/2606.27681v1 — §2 Problem Setup: Text Based POMDPs; 5 Experimental Evaluation; 5.3 Evaluation Metrics | https://arxiv.org/html/2606.27681v1 — §7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27681 | complete |
| SF-2026-ARXIV-2606-27683 | RP-9a69aabca4d4421b | deep | arXiv:2606.27683v1 | SRC-ARXIV@arXiv:2606.27683v1 | https://arxiv.org/html/2606.27683v1 — §III Preliminaries and Framework; III-A White-Box and Gray-Box Unlearning Methods; III-B API-Only Scenario and Proposed Framework | https://arxiv.org/html/2606.27683v1 — §VI Experiments; VI-A Experimental Setup; VI-B Performance Evaluation | https://arxiv.org/html/2606.27683v1 — §VII Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27683 | complete |
| SF-2026-ARXIV-2606-27704 | RP-eab38e6ee494e401 | deep | arXiv:2606.27704v1 | SRC-ARXIV@arXiv:2606.27704v1 | https://arxiv.org/html/2606.27704v1 — §IV AdvScan Algorithm; V-A 3 Adversarial Examples (AE) Generation Methodologies; V-C Evaluation of the AdvScan Algorithm | https://arxiv.org/html/2606.27704v1 — §AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis; II-D Power Analysis; II-E Side Channel Analysis for Adversarial Behavior Detection | https://arxiv.org/html/2606.27704v1 — §II-F Threat Model; IV-D Discussion of Merits and Limitations of AdvScan; VI Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27704 | complete |
| SF-2026-ARXIV-2606-27709 | RP-c82291588b7aaac8 | standard | arXiv:2606.27709v1 | SRC-ARXIV@arXiv:2606.27709v1 | https://arxiv.org/html/2606.27709v1 — §3 Methods; 3.2 Study design; 3.3 Training data and data construction | https://arxiv.org/html/2606.27709v1 — §Experiment 1.; Experiment 2.; Experiment 3. | https://arxiv.org/html/2606.27709v1 — §5 Discussion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27709 | complete |
| SF-2026-ARXIV-2606-27732 | RP-eb6d768fc8c67a93 | deep | arXiv:2606.27732v1 | SRC-ARXIV@arXiv:2606.27732v1 | https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference | https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks | https://arxiv.org/html/2606.27732v1 — §5 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27732 | complete |
| SF-2026-ARXIV-2606-27739 | RP-8b16b5a26e2e32be | standard | arXiv:2606.27739v1 | SRC-ARXIV@arXiv:2606.27739v1 | https://arxiv.org/html/2606.27739v1 — §4 Method; C.2 PRM Training Details; Model architecture. | https://arxiv.org/html/2606.27739v1 — §3 Analysis; 3.3 Theoretical Analysis; 5 Experiments | https://arxiv.org/html/2606.27739v1 — §6 Conclusion; Limitations; B.7 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27739 | complete |
| SF-2026-ARXIV-2606-27743 | RP-50afd2df11e5cd81 | standard | arXiv:2606.27743v1 | SRC-ARXIV@arXiv:2606.27743v1 | https://arxiv.org/html/2606.27743v1 — §3 Methodology; 3.5 Training and Inference | https://arxiv.org/html/2606.27743v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results | https://arxiv.org/html/2606.27743v1 — §4.6 Discussion and Limitations; 5 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27743 | complete |
| SF-2026-ARXIV-2606-27757 | RP-ccd06f48cc8dc834 | standard | arXiv:2606.27757v1 | SRC-ARXIV@arXiv:2606.27757v1 | https://arxiv.org/html/2606.27757v1 — §Towards Reliable and Robust LLM Planning: A Symbolic Feedback-Driven Iterative Self-Refinement Framework Thanks: * Corresponding author at: Institute of Automation, Chinese Academy of Sciences, Beijing, China.; III METHODOLOGY; III-B Feedback-Driven Iterative Self-Refinement Framework | https://arxiv.org/html/2606.27757v1 — §IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length | https://arxiv.org/html/2606.27757v1 — §V CONCLUSION | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27757 | complete |
| SF-2026-ARXIV-2606-27780 | RP-183a200d4042495f | standard | arXiv:2606.27780v1 | SRC-ARXIV@arXiv:2606.27780v1 | https://arxiv.org/html/2606.27780v1 — §Agent graphs and skill-graph systems.; 3 Graph World Model Framework; Framework overview. | https://arxiv.org/html/2606.27780v1 — §5 Dataset and Evaluation Protocol; Graph world model setup.; 7 Experiments | https://arxiv.org/html/2606.27780v1 — §7.2.3 Global spectral amplification differs from local hub failure; 7.5.4 OOD perturbation confirms the FE contraction boundary; 7.6.2 Role-dependent failure sensitivity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27780 | complete |
| SF-2026-ARXIV-2606-27791 | RP-5277f4acb2dfb798 | standard | arXiv:2606.27791v1 | SRC-ARXIV@arXiv:2606.27791v1 | https://arxiv.org/html/2606.27791v1 — §NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation; 3 Method | https://arxiv.org/html/2606.27791v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results | https://arxiv.org/html/2606.27791v1 — §5 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27791 | complete |
| SF-2026-ARXIV-2606-27797 | RP-4df54364f89af0a2 | deep | arXiv:2606.27797v1 | SRC-ARXIV@arXiv:2606.27797v1 | https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training | https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results | https://arxiv.org/html/2606.27797v1 — §6 Conclusions | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27797 | complete |
| SF-2026-ARXIV-2606-27806 | RP-c3ab9602bc243f16 | deep | arXiv:2606.27806v1 | SRC-ARXIV@arXiv:2606.27806v1 | https://arxiv.org/html/2606.27806v1 — §Our approach: GILP.; LLM API ecosystem.; 4 Method: Grounded Iterative Language Planning | https://arxiv.org/html/2606.27806v1 — §5 Experiments; Setup.; Cost analysis. | https://arxiv.org/html/2606.27806v1 — §6 Discussion; 7 Limitations; 8 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27806 | complete |
| SF-2026-ARXIV-2606-27814 | RP-435b3d0c09213e9a | standard | arXiv:2606.27814v1 | SRC-ARXIV@arXiv:2606.27814v1 | https://arxiv.org/html/2606.27814v1 — §4 Method; 5.4 Training Dynamics and Diagnostic Metrics; Appendix A Method and Algorithmic Details | https://arxiv.org/html/2606.27814v1 — §5 Experiments; 5.1 Experimental Setup; Datasets & Benchmarks. | https://arxiv.org/html/2606.27814v1 — §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27814 | complete |
| SF-2026-ARXIV-2606-27826 | RP-264745a51e7b122d | deep | arXiv:2606.27826v1 | SRC-ARXIV@arXiv:2606.27826v1 | https://arxiv.org/html/2606.27826v1 — §3.1 Benchmark Design; Appendix F NormPerceptor Training Data Details | https://arxiv.org/html/2606.27826v1 — §NormAct : A Benchmark for Hidden Social Norm Compliance in Embodied Planning; 2.1 Social Norm Evaluation in (M)LLMs; 3 The NormAct Benchmark | https://arxiv.org/html/2606.27826v1 — §7 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27826 | complete |
| SF-2026-ARXIV-2606-27841 | RP-274a4d92ab6f68ca | deep | arXiv:2606.27841v1 | SRC-ARXIV@arXiv:2606.27841v1 | https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.2 Layer-Wise Energy Estimation Framework | https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.1 Experimental Protocol; 4 Results | https://arxiv.org/html/2606.27841v1 — §5 Discussion; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27841 | complete |
| SF-2026-ARXIV-2606-27866 | RP-20466c85fa2228a3 | standard | arXiv:2606.27866v1 | SRC-ARXIV@arXiv:2606.27866v1 | https://arxiv.org/html/2606.27866v1 — §3 Method; Clip FFN Forward Kernel Co-Design.; Toward Co-Designed Online Budget Scheduling. | https://arxiv.org/html/2606.27866v1 — §4 Experiments; 4.1 Experimental Setup; Implementation Details and Evaluation Tasks. | https://arxiv.org/html/2606.27866v1 — §5 Conclusion; Limitations and Future Works.; A.2 Additional Discussion on Cross-Budget Transfer and Cross-Model Trends | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27866 | complete |
| SF-2026-ARXIV-2606-27906 | RP-f018813c97ac966b | deep | arXiv:2606.27906v1 | SRC-ARXIV@arXiv:2606.27906v1 | https://arxiv.org/html/2606.27906v1 — §7.2. Methodology and Outcomes on Phi-3.5-V | https://arxiv.org/html/2606.27906v1 — §2. Platform and Experimental Setup; 3.1. Phase-Level Results; 6.1. Three-Backend Benchmark | https://arxiv.org/html/2606.27906v1 — §8. Discussion; 10. Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27906 | complete |
| SF-2026-ARXIV-2606-27934 | RP-b387c14574be17ea | deep | arXiv:2606.27934v1 | SRC-ARXIV@arXiv:2606.27934v1 | https://arxiv.org/html/2606.27934v1 — §Approach. | https://arxiv.org/html/2606.27934v1 — §Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking | https://arxiv.org/html/2606.27934v1 — §10 Threat model and guarantees; 12 Physical stress and the trust boundary; 14 Scope and limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27934 | complete |
| SF-2026-ARXIV-2606-27936 | RP-45f8de32ae80c0d8 | deep | arXiv:2606.27936v1 | SRC-ARXIV@arXiv:2606.27936v1 | https://arxiv.org/html/2606.27936v1 — §3 Methodology; 3.2 Study Design and Simulated Data | https://arxiv.org/html/2606.27936v1 — §4 Results | https://arxiv.org/html/2606.27936v1 — §Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy; Threat model.; 5 Discussion and Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27936 | complete |
| SF-2026-ARXIV-2606-27944 | RP-75221d7997b0d453 | deep | arXiv:2606.27944v1 | SRC-ARXIV@arXiv:2606.27944v1 | https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework | https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework; 5 Evaluation Results | https://arxiv.org/html/2606.27944v1 — §3 Threat Model; 8 Discussion and Limitation; 9 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27944 | complete |
| SF-2026-ARXIV-2606-27962 | RP-22dc06642d188f8b | standard | arXiv:2606.27962v1 | SRC-ARXIV@arXiv:2606.27962v1 | https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 2 Overall Positioning and Design Principles; 2.3 Design Principles | https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets | https://arxiv.org/html/2606.27962v1 — §3.3 Limitations of Current Solutions; 6.5 Failure Data and Corrective Data | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27962 | complete |
| SF-2026-ARXIV-2606-27976 | RP-161e1684a0ac6eaa | standard | arXiv:2606.27976v1 | SRC-ARXIV@arXiv:2606.27976v1 | https://arxiv.org/html/2606.27976v1 — §Appendix A Reproduced baseline analyses from the global-linear system | https://arxiv.org/html/2606.27976v1 — §8 Experiments; Integral multi-encoder evaluation at 10 6 10^{6} scale. | https://arxiv.org/html/2606.27976v1 — §3 Threat Model; A measured limitation: overlap reference lookup.; 9 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27976 | complete |
| SF-2026-ARXIV-2606-27997 | RP-816d86e3849e0ca0 | deep | arXiv:2606.27997v1 | SRC-ARXIV@arXiv:2606.27997v1 | https://arxiv.org/html/2606.27997v1 — §5.1. Evaluation methodology; Recommender Systems.; Recommender Systems | https://arxiv.org/html/2606.27997v1 — §Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings; Benchmark Setting; Theoretical results summary | https://arxiv.org/html/2606.27997v1 — §7. Conclusions and discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27997 | complete |
| SF-2026-ARXIV-2606-28011 | RP-b5c754ca86619d68 | standard | arXiv:2606.28011v1 | SRC-ARXIV@arXiv:2606.28011v1 | https://arxiv.org/html/2606.28011v1 — §3 LLM-based agentic framework for fault-tolerant control | https://arxiv.org/html/2606.28011v1 — §4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results | https://arxiv.org/html/2606.28011v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28011 | complete |
| SF-2026-ARXIV-2606-28013 | RP-ff54311f4759385a | deep | arXiv:2606.28013v1 | SRC-ARXIV@arXiv:2606.28013v1 | https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant | https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis | https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28013 | complete |
| SF-2026-ARXIV-2606-28037 | RP-e4c56ec741d0b7c3 | deep | arXiv:2606.28037v1 | SRC-ARXIV@arXiv:2606.28037v1 | https://arxiv.org/html/2606.28037v1 — §Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors; 4.1.1. Tasks, Datasets, and Model Architectures | https://arxiv.org/html/2606.28037v1 — §4. Evaluation; 4.1. Experiment Setup; 4.1.5. Reproducibility and Additional Results | https://arxiv.org/html/2606.28037v1 — §5. Discussion; 5.3. Limitations; 6. Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28037 | complete |
| SF-2026-ARXIV-2606-28050 | RP-8b0774eecb4ded05 | deep | arXiv:2606.28050v1 | SRC-ARXIV@arXiv:2606.28050v1 | https://arxiv.org/html/2606.28050v1 — §3 Methodology; Hard-negative generation for evaluator training.; LoRA training budget. | https://arxiv.org/html/2606.28050v1 — §Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). | https://arxiv.org/html/2606.28050v1 — §5 Results and Discussion; 6 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28050 | complete |
| SF-2026-ARXIV-2606-28061 | RP-c941eb9693e60137 | deep | arXiv:2606.28061v1 | SRC-ARXIV@arXiv:2606.28061v1 | https://arxiv.org/html/2606.28061v1 — §4.7 System Modules | https://arxiv.org/html/2606.28061v1 — §ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents Note: This work was supported by the Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing (GJJ-25-009).; 2.1 Privacy Evaluation of Large Language Models; 2.2 Tool-Using Agents and Agent Benchmarks | https://arxiv.org/html/2606.28061v1 — §8 Representative Failure Cases; 9 Discussion and Implications; 10 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28061 | complete |
| SF-2026-ARXIV-2606-28070 | RP-4296b82eda3d243f | standard | arXiv:2606.28070v1 | SRC-ARXIV@arXiv:2606.28070v1 | https://arxiv.org/html/2606.28070v1 — §2 Architecture Overview; 3.1 Method Overview; 3.2.2 Algorithm-driven ontology growth (bottom-up) | https://arxiv.org/html/2606.28070v1 — §3.3 Results; 4.2.3 Results; Module 1: Data evaluation. | https://arxiv.org/html/2606.28070v1 — §9 Conclusion; 10 Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28070 | complete |
| SF-2026-ARXIV-2606-28116 | RP-877f1c28dc3cdce2 | deep | arXiv:2606.28116v1 | SRC-ARXIV@arXiv:2606.28116v1 | https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; Training-stability monitors.; 5 Designing Module-Specific Monitors from First Principles | https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; 1 Introduction | https://arxiv.org/html/2606.28116v1 — §6 Limitations; 7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28116 | complete |
| SF-2026-ARXIV-2606-28128 | RP-37d91892793bd718 | standard | arXiv:2606.28128v1 | SRC-ARXIV@arXiv:2606.28128v1 | https://arxiv.org/html/2606.28128v1 — §3 Method; 3.4 Training and Inference; Training data. | https://arxiv.org/html/2606.28128v1 — §4 Experiments; 4.1 Experimental Setup; Benchmarks. | https://arxiv.org/html/2606.28128v1 — §5 Conclusion; Appendix F Limitations and future work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28128 | complete |
| SF-2026-ARXIV-2606-28153 | RP-0c083d0c43178004 | deep | arXiv:2606.28153v1 | SRC-ARXIV@arXiv:2606.28153v1 | https://arxiv.org/html/2606.28153v1 — §Detection-based methods; Perturbation-based methods; Representation-based methods | https://arxiv.org/html/2606.28153v1 — §4 Experiments; 4.1 Experimental Setup; Experimental Design | https://arxiv.org/html/2606.28153v1 — §6 Conclusion; Conclusions and practical guidance.; B.3 Limitations and Future Directions | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28153 | complete |
| SF-2026-ARXIV-2606-28166 | RP-16a24106681be088 | standard | arXiv:2606.28166v1 | SRC-ARXIV@arXiv:2606.28166v1 | https://arxiv.org/html/2606.28166v1 — §3.1 Preliminaries: tandem training; 5.1 Training dynamics of TRL | https://arxiv.org/html/2606.28166v1 — §4 Results; 4.1 Experimental setup; Appendix B Additional Results | https://arxiv.org/html/2606.28166v1 — §5 Discussion; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28166 | complete |
| SF-2026-ARXIV-2606-28187 | RP-feea63dcbfbd1558 | standard | arXiv:2606.28187v1 | SRC-ARXIV@arXiv:2606.28187v1 | https://arxiv.org/html/2606.28187v1 — §GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems; 2.2 Multi-Agent System; 2.3 Multi-Agent System Optimization | https://arxiv.org/html/2606.28187v1 — §5 Experiment; Setup; Optimization Setup | https://arxiv.org/html/2606.28187v1 — §6 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28187 | complete |
| SF-2026-ARXIV-2606-28235 | RP-c88d6aafa0eb9682 | standard | arXiv:2606.28235v1 | SRC-ARXIV@arXiv:2606.28235v1 | https://arxiv.org/html/2606.28235v1 — §Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software; II-C Software ecosystems and coordination cost; II-D Emergence and complex adaptive systems | https://arxiv.org/html/2606.28235v1 — §IV-B Level of analysis and why multilevel models; V Results | https://arxiv.org/html/2606.28235v1 — §VI Discussion; VII Threats to Validity; VIII Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28235 | complete |
| SF-2026-ARXIV-2606-28276 | RP-e01698a305212ce3 | deep | arXiv:2606.28276v1 | SRC-ARXIV@arXiv:2606.28276v1 | https://arxiv.org/html/2606.28276v1 — §SimFoundry outperforms state-of-the-art simulation evaluation frameworks and makes fewer assumptions.; 5.2 Sim-to-Real Policy Training; Co-training with sim and real data further improves performance. | https://arxiv.org/html/2606.28276v1 — §SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation | https://arxiv.org/html/2606.28276v1 — §6 Limitations; 7 Conclusion; Appendix C Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28276 | complete |
| SF-2026-ARXIV-2606-28277 | RP-16cc254bac4c05d0 | deep | arXiv:2606.28277v1 | SRC-ARXIV@arXiv:2606.28277v1 | https://arxiv.org/html/2606.28277v1 — §Design Considerations. | https://arxiv.org/html/2606.28277v1 — §2.1. Case Study: Verification of Retracted Papers in the SPOT Benchmark; 3. PAT Experimental Programs at STOC and ICML; 3.1. Quantitative Author Feedback for PAT Experimental Programs | https://arxiv.org/html/2606.28277v1 — §5. Conclusion and Future Outlook | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28277 | complete |
| SF-2026-ARXIV-2606-28279 | RP-584274718264c170 | standard | arXiv:2606.28279v1 | SRC-ARXIV@arXiv:2606.28279v1 | https://arxiv.org/html/2606.28279v1 — §Agentic Hardware Design as Repository-Level Code Evolution; Benchmarks for RTL design and verification.; 3 The HORIZON Framework | https://arxiv.org/html/2606.28279v1 — §Benchmarks for RTL design and verification.; 4 Experiments; Setup and protocol. | https://arxiv.org/html/2606.28279v1 — §4.3 Detailed discussion on test-generation tasks; 5 Discussion and Limitations; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28279 | complete |
| SF-2026-ARXIV-2606-28322 | RP-50a46bd07bd079cb | deep | arXiv:2606.28322v1 | SRC-ARXIV@arXiv:2606.28322v1 | https://arxiv.org/html/2606.28322v1 — §3.1 Design Criteria | https://arxiv.org/html/2606.28322v1 — §PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. | https://arxiv.org/html/2606.28322v1 — §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28322 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-27406:start -->
### 2606.27406 — Towards Evaluation of Implicit Software World Models in Coding LLMs

**问题与旧路径。** Software engineering, whether performed by humans or by AI agents, requires reasoning about how software behaves. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Towards Evaluation of Implicit Software World Models in Coding LLMs 的 exact-v1 机制为：We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27406v1 — §2 Data; §3 Metrics; §4 Experiment Setup`；Evaluation=`arXiv:2606.27406v1 — §5 Results Discussion`；counterevidence=`arXiv:2606.27406v1 — §6 Limitations; §7 Conclusion`。exact-v1 的观测边界是：In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. 它没有证明 We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Software engineering, whether performed by humans or by AI agents, requires reasoning about how software behaves. 披露的 evaluation signal 是：In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. exact-v1 的观测边界是：In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. 它没有证明 We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27406:start -->
Primary identity `arXiv:2606.27406v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27406:end -->
<!-- review:SF-2026-ARXIV-2606-27406:end -->

<!-- review:SF-2026-ARXIV-2606-27409:start -->
### 2606.27409 — Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement

**问题与旧路径。** The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement 的 exact-v1 机制为：The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。 唯一 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27409v1 — §3 Model; §4 Stability and the verification dose; §5 Optimal corrector placement`；Evaluation=`arXiv:2606.27409v1 — §7 Empirical validation; §7.1 Onset at the predicted dose limit (RQ1)`；counterevidence=`arXiv:2606.27409v1 — §8 Discussion; §10 Limitations`。exact-v1 的观测边界是：By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing 它没有证明 The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 披露的 evaluation signal 是：By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing exact-v1 的观测边界是：By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing 它没有证明 The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27409:start -->
Primary identity `arXiv:2606.27409v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27409:end -->
<!-- review:SF-2026-ARXIV-2606-27409:end -->

<!-- review:SF-2026-ARXIV-2606-27416:start -->
### 2606.27416 — Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents

**问题与旧路径。** We call this verifier-driven research: the rules of the research process live in code that fails loudly when violated, not in prose that agents are merely asked to follow. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents 的 exact-v1 机制为：To address this problem, we present Glite ARF, an open-source Python framework for running many LLM coding agents in parallel on a research repository without sacrificing reproducibility or auditability. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27416v1 — §3 System; §3.1 Architecture and seven principles; §5 The framework in use`；Evaluation=`arXiv:2606.27416v1 — §Evaluation regime.; §Workflow, provenance, and experiment management.; §4.3 Headline result`；counterevidence=`arXiv:2606.27416v1 — §Limitations.; §Appendix D Observed failure modes`。exact-v1 的观测边界是：Framework and a public demo project accompany this paper. 它没有证明 To address this problem, we present Glite ARF, an open-source Python framework for running many LLM coding agents in parallel on a research repository without sacrificing reproducibility or auditability. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We call this verifier-driven research: the rules of the research process live in code that fails loudly when violated, not in prose that agents are merely asked to follow. 披露的 evaluation signal 是：Framework and a public demo project accompany this paper. exact-v1 的观测边界是：Framework and a public demo project accompany this paper. 它没有证明 To address this problem, we present Glite ARF, an open-source Python framework for running many LLM coding agents in parallel on a research repository without sacrificing reproducibility or auditability. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27416:start -->
Primary identity `arXiv:2606.27416v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27416:end -->
<!-- review:SF-2026-ARXIV-2606-27416:end -->

<!-- review:SF-2026-ARXIV-2606-27457:start -->
### 2606.27457 — Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving

**问题与旧路径。** Efficient deployment of large language models (LLMs) in production forces a trade-off between accuracy and cost. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving 的 exact-v1 机制为：To address this challenge, we propose a two-stage cascaded solution. 因此 把请求分类、模型路由、升级阈值、成本与 SLO 共同版本化。 唯一 owner 为 `PLATFORM-GATEWAY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27457v1 — §Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving; §3 System Overview; §Appendix B Framework Extensibility: AIME Pool Expansion`；Evaluation=`arXiv:2606.27457v1 — §4.3 Pareto Analysis and Model Selection; §7 Experiments and Results; §Appendix A Inference Setup`；counterevidence=`arXiv:2606.27457v1 — §8 Conclusion and Future Work; §Limitations`。exact-v1 的观测边界是：It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration. 它没有证明 To address this challenge, we propose a two-stage cascaded solution. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Efficient deployment of large language models (LLMs) in production forces a trade-off between accuracy and cost. 披露的 evaluation signal 是：It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration. exact-v1 的观测边界是：It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration. 它没有证明 To address this challenge, we propose a two-stage cascaded solution. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27457:start -->
Primary identity `arXiv:2606.27457v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27457:end -->
<!-- review:SF-2026-ARXIV-2606-27457:end -->

<!-- review:SF-2026-ARXIV-2606-27472:start -->
### 2606.27472 — Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents

**问题与旧路径。** We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents 的 exact-v1 机制为：Acting correctly requires using the current value of a fact and discarding values that have been superseded. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27472v1 — §Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents; §Memory systems and RL for memory.; §Deployed memory systems.`；Evaluation=`arXiv:2606.27472v1 — §Long-term memory benchmarks.; §4 Experimental Setup; §Training setup.`；counterevidence=`arXiv:2606.27472v1 — §Failure modes.; §6 Discussion; §7 Limitations`。exact-v1 的观测边界是：We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. 它没有证明 Acting correctly requires using the current value of a fact and discarding values that have been superseded. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. 披露的 evaluation signal 是：We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. exact-v1 的观测边界是：We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. 它没有证明 Acting correctly requires using the current value of a fact and discarding values that have been superseded. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27472:start -->
Primary identity `arXiv:2606.27472v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27472:end -->
<!-- review:SF-2026-ARXIV-2606-27472:end -->

<!-- review:SF-2026-ARXIV-2606-27474:start -->
### 2606.27474 — Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks

**问题与旧路径。** Evaluating SpecRef across six benchmarks (HumanEval, MBPP, GSM8K, BBH, ARC-Challenge, HellaSwag) with three distinct evaluation protocols (execution-based pass@1, exact-match, log-likelihood scoring), we surface several findings relevant beyond our specific system: (1) code benchmarks conflate structural discovery with logical correctness: providing a syntactic scaffold lifts accuracy from near zero to over 20% without changing the model, indicating that much of the baseline failure is structural; (2) a refinement tension phenomenon where multi-stage cor 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks 的 exact-v1 机制为：Evaluating SpecRef across six benchmarks (HumanEval, MBPP, GSM8K, BBH, ARC-Challenge, HellaSwag) with three distinct evaluation protocols (execution-based pass@1, exact-match, log-likelihood scoring), we surface several findings relevant beyond our specific system: (1) code benchmarks conflate structural discovery with logical correctness: providing a syntactic scaffold lifts accuracy from near zero to over 20% without changing the model, indicating that much of the baseline failure is structural; (2) a refinement tension phenomenon where multi-stage cor 因此 把 decoding objective、handoff state、quality signal 与保守 autoregressive fallback 绑定。 唯一 owner 为 `INFER-DECODE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27474v1 — §3. Multi-stage systems need component-level reporting.`；Evaluation=`arXiv:2606.27474v1 — §Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks; §3 Evaluation Setup; §3.2 Evaluation protocols`；counterevidence=`arXiv:2606.27474v1 — §5 Discussion: Lessons for Evaluating Hybrid Generation; §7 Conclusion; §Limitations`。exact-v1 的观测边界是：How should we evaluate generation systems that combine autoregressive (AR) and diffusion decoding? 它没有证明 Evaluating SpecRef across six benchmarks (HumanEval, MBPP, GSM8K, BBH, ARC-Challenge, HellaSwag) with three distinct evaluation protocols (execution-based pass@1, exact-match, log-likelihood scoring), we surface several findings relevant beyond our specific system: (1) code benchmarks conflate structural discovery with logical correctness: providing a syntactic scaffold lifts accuracy from near zero to over 20% without changing the model, indicating that much of the baseline failure is structural; (2) a refinement tension phenomenon where multi-stage cor 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Evaluating SpecRef across six benchmarks (HumanEval, MBPP, GSM8K, BBH, ARC-Challenge, HellaSwag) with three distinct evaluation protocols (execution-based pass@1, exact-match, log-likelihood scoring), we surface several findings relevant beyond our specific system: (1) code benchmarks conflate structural discovery with logical correctness: providing a syntactic scaffold lifts accuracy from near zero to over 20% without changing the model, indicating that much of the baseline failure is structural; (2) a refinement tension phenomenon where multi-stage cor 披露的 evaluation signal 是：How should we evaluate generation systems that combine autoregressive (AR) and diffusion decoding? exact-v1 的观测边界是：How should we evaluate generation systems that combine autoregressive (AR) and diffusion decoding? 它没有证明 Evaluating SpecRef across six benchmarks (HumanEval, MBPP, GSM8K, BBH, ARC-Challenge, HellaSwag) with three distinct evaluation protocols (execution-based pass@1, exact-match, log-likelihood scoring), we surface several findings relevant beyond our specific system: (1) code benchmarks conflate structural discovery with logical correctness: providing a syntactic scaffold lifts accuracy from near zero to over 20% without changing the model, indicating that much of the baseline failure is structural; (2) a refinement tension phenomenon where multi-stage cor 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27474:start -->
Primary identity `arXiv:2606.27474v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27474:end -->
<!-- review:SF-2026-ARXIV-2606-27474:end -->

<!-- review:SF-2026-ARXIV-2606-27483:start -->
### 2606.27483 — Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning

**问题与旧路径。** Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning 的 exact-v1 机制为：Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. 因此 把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state。 唯一 owner 为 `AGENT-PLANNING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27483v1 — §Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning; §2.2 Mid-training in large language models; §3 Methodology`；Evaluation=`arXiv:2606.27483v1 — §5 Experiments; §5.1 Experiment setup; §5.2 Main results`；counterevidence=`arXiv:2606.27483v1 — §6 Conclusion`。exact-v1 的观测边界是：Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. 它没有证明 Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. 披露的 evaluation signal 是：Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. exact-v1 的观测边界是：Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. 它没有证明 Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27483:start -->
Primary identity `arXiv:2606.27483v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27483:end -->
<!-- review:SF-2026-ARXIV-2606-27483:end -->

<!-- review:SF-2026-ARXIV-2606-27492:start -->
### 2606.27492 — QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems

**问题与旧路径。** In the CF fulltest setting, the best generated graph reduces RMSE from 12.53 for the strongest fixed topology to 7.87 while also reducing messages, model calls, and token cost; Silo-style results show the same direction of improvement over cold and fixed-topology baselines. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems 的 exact-v1 机制为：This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。 唯一 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27492v1 — §Skill routing, ecosystems, and failure modes.; §3 Method; §3.5 Skill Evolution: From Generated Evidence to Design Rules`；Evaluation=`arXiv:2606.27492v1 — §4 Experiments; §4.1 Evaluation Tasks; §4.2 Experimental Rationale`；counterevidence=`arXiv:2606.27492v1 — §Skill routing, ecosystems, and failure modes.; §5 Conclusion`。exact-v1 的观测边界是：This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 它没有证明 This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：In the CF fulltest setting, the best generated graph reduces RMSE from 12.53 for the strongest fixed topology to 7.87 while also reducing messages, model calls, and token cost; Silo-style results show the same direction of improvement over cold and fixed-topology baselines. 披露的 evaluation signal 是：This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. exact-v1 的观测边界是：This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 它没有证明 This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27492:start -->
Primary identity `arXiv:2606.27492v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27492:end -->
<!-- review:SF-2026-ARXIV-2606-27492:end -->

<!-- review:SF-2026-ARXIV-2606-27499:start -->
### 2606.27499 — DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection

**问题与旧路径。** Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to remember what it saw rather than what it could write down. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection 的 exact-v1 机制为：We introduce DMV-Bench (Code: https://github.com/yyyujintang/DMV-Bench), the first interactive benchmark for multimodal-agent visual memory. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27499v1 — §Text-side memory systems.; §Vision-side memory systems.; §DualMem is the strongest architecture.`；Evaluation=`arXiv:2606.27499v1 — §Why existing benchmarks cannot answer this.; §Agent memory benchmarks.; §3.3 Efficient evaluation: the rollout tree`；counterevidence=`arXiv:2606.27499v1 — §6 Conclusion; §Limitations`。exact-v1 的观测边界是：On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role. 它没有证明 We introduce DMV-Bench (Code: https://github.com/yyyujintang/DMV-Bench), the first interactive benchmark for multimodal-agent visual memory. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to remember what it saw rather than what it could write down. 披露的 evaluation signal 是：On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role. exact-v1 的观测边界是：On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role. 它没有证明 We introduce DMV-Bench (Code: https://github.com/yyyujintang/DMV-Bench), the first interactive benchmark for multimodal-agent visual memory. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27499:start -->
Primary identity `arXiv:2606.27499v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27499:end -->
<!-- review:SF-2026-ARXIV-2606-27499:end -->

<!-- review:SF-2026-ARXIV-2606-27510:start -->
### 2606.27510 — The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching

**问题与旧路径。** A natural response may be to try to eliminate INT by adjusting the estimator or unit of analysis, but each of these potential remedies has predictable failure modes. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching 的 exact-v1 机制为：It attributes causal responsibility for a model behavior to each of its individual components by estimating its natural indirect effect (NIE). 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27510v1 — §Counterfactual prompt design.`；Evaluation=`arXiv:2606.27510v1 — §5.2 Diagnosing Activation Patching Results`；counterevidence=`arXiv:2606.27510v1 — §6 Discussion and Future Work`。exact-v1 的观测边界是：Its individual and group-level magnitude and sign signal when causal conclusions are prompt-dependent, and when greedy NIE-based component ranking will miss mechanisms only discoverable through combinatorial search. 它没有证明 It attributes causal responsibility for a model behavior to each of its individual components by estimating its natural indirect effect (NIE). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A natural response may be to try to eliminate INT by adjusting the estimator or unit of analysis, but each of these potential remedies has predictable failure modes. 披露的 evaluation signal 是：Its individual and group-level magnitude and sign signal when causal conclusions are prompt-dependent, and when greedy NIE-based component ranking will miss mechanisms only discoverable through combinatorial search. exact-v1 的观测边界是：Its individual and group-level magnitude and sign signal when causal conclusions are prompt-dependent, and when greedy NIE-based component ranking will miss mechanisms only discoverable through combinatorial search. 它没有证明 It attributes causal responsibility for a model behavior to each of its individual components by estimating its natural indirect effect (NIE). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27510:start -->
Primary identity `arXiv:2606.27510v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27510:end -->
<!-- review:SF-2026-ARXIV-2606-27510:end -->

<!-- review:SF-2026-ARXIV-2606-27511:start -->
### 2606.27511 — When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems

**问题与旧路径。** In this paper, we explore the potential vulnerability where a malicious aggregator, who may collude with a third-party vendor, stealthily implants advertisement-type backdoors into federated QA models, without ever accessing client data. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems 的 exact-v1 机制为：Motivated by this, we propose to leverage clients' uploaded gradients during training, and develop a two-stage framework for data-free and stealthy poisoning: (1) recover representative training samples from client gradients, and (2) construct poisoning datasets utilizing recovered samples and trigger phrases to inject backdoors into the global model. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27511v1 — §When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems; §2.3 Fine-Tuning Strategies in FL Training; §5 Methodology`；Evaluation=`arXiv:2606.27511v1 — §6 Evaluations; §6.1 Experimental Setup; §Appendix C Experiment Details.`；counterevidence=`arXiv:2606.27511v1 — §2.4 Federated LLMs and Server-side Threats; §3 Threat Model; §8 Conclusion`。exact-v1 的观测边界是：Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. 它没有证明 Motivated by this, we propose to leverage clients' uploaded gradients during training, and develop a two-stage framework for data-free and stealthy poisoning: (1) recover representative training samples from client gradients, and (2) construct poisoning datasets utilizing recovered samples and trigger phrases to inject backdoors into the global model. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：In this paper, we explore the potential vulnerability where a malicious aggregator, who may collude with a third-party vendor, stealthily implants advertisement-type backdoors into federated QA models, without ever accessing client data. 披露的 evaluation signal 是：Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. exact-v1 的观测边界是：Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. 它没有证明 Motivated by this, we propose to leverage clients' uploaded gradients during training, and develop a two-stage framework for data-free and stealthy poisoning: (1) recover representative training samples from client gradients, and (2) construct poisoning datasets utilizing recovered samples and trigger phrases to inject backdoors into the global model. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27511:start -->
Primary identity `arXiv:2606.27511v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27511:end -->
<!-- review:SF-2026-ARXIV-2606-27511:end -->

<!-- review:SF-2026-ARXIV-2606-27550:start -->
### 2606.27550 — EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction

**问题与旧路径。** Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction 的 exact-v1 机制为：To address this, we propose Entropy-guided Multi-Token Prediction (EntMTP), a training-free scheduler that toggles between tree-based attention topologies from a set of task-specific pareto-optimal trees conditioned on a running estimate of local generation entropy. 因此 把 draft/verify/bypass 路由、质量门槛、成本和 schema-critical fallback 共同验收。 唯一 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27550v1 — §3 Optimizing Task-Specific Greedy Draft Trees; §4 Inference-Time Tree Scheduler`；Evaluation=`arXiv:2606.27550v1 — §5 Evaluation Methodology; §6 Results`；counterevidence=`arXiv:2606.27550v1 — §Appendix C More Frontiers`。exact-v1 的观测边界是：Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. 它没有证明 To address this, we propose Entropy-guided Multi-Token Prediction (EntMTP), a training-free scheduler that toggles between tree-based attention topologies from a set of task-specific pareto-optimal trees conditioned on a running estimate of local generation entropy. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. 披露的 evaluation signal 是：Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. exact-v1 的观测边界是：Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. 它没有证明 To address this, we propose Entropy-guided Multi-Token Prediction (EntMTP), a training-free scheduler that toggles between tree-based attention topologies from a set of task-specific pareto-optimal trees conditioned on a running estimate of local generation entropy. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27550:start -->
Primary identity `arXiv:2606.27550v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27550:end -->
<!-- review:SF-2026-ARXIV-2606-27550:end -->

<!-- review:SF-2026-ARXIV-2606-27558:start -->
### 2606.27558 — Productionized Fairness Measurement Under Privacy Constraints

**问题与旧路径。** Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Productionized Fairness Measurement Under Privacy Constraints 的 exact-v1 机制为：We close with a transferable framework for institutions seeking to implement similar privacy-preserving measurement infrastructure. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27558v1 — §1.2. Design Principles & Evolution; §1.3. The PPRE Method; §5. PPRE Fairness Metric Algorithms`；Evaluation=`arXiv:2606.27558v1 — §7. Production Deployment and Evaluation`；counterevidence=`arXiv:2606.27558v1 — §8. Discussion; §8.1.1. Measurement Quality Discussion; §8.5. Limitations`。exact-v1 的观测边界是：Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. 它没有证明 We close with a transferable framework for institutions seeking to implement similar privacy-preserving measurement infrastructure. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. 披露的 evaluation signal 是：Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. exact-v1 的观测边界是：Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. 它没有证明 We close with a transferable framework for institutions seeking to implement similar privacy-preserving measurement infrastructure. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27558:start -->
Primary identity `arXiv:2606.27558v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27558:end -->
<!-- review:SF-2026-ARXIV-2606-27558:end -->

<!-- review:SF-2026-ARXIV-2606-27567:start -->
### 2606.27567 — On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models

**问题与旧路径。** Prompt injection is the top security risk for LLM-integrated applications, yet every defense proposed so far has been broken. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models 的 exact-v1 机制为：It mirrors the code-data confusion in Von Neumann machines that gives rise to buffer overflows, a vulnerability class that took decades of layered defenses (DEP, Write-XOR-Execute, ASLR, stack canaries, and ultimately memory-safe languages) to contain, because no single mechanism sufficed. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27567v1 — §2 Formal Framework; §Architectures outside scope.`；Evaluation=`arXiv:2606.27567v1 — §4.7 Main Result: Impossibility of Perfect Semantic-Faithful Control; §8 Connection to Existing Results; §Impossibility results in AI.`；counterevidence=`arXiv:2606.27567v1 — §3 Threat Model and Scope; §9 Discussion; §10 Conclusion`。exact-v1 的观测边界是：We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). 它没有证明 It mirrors the code-data confusion in Von Neumann machines that gives rise to buffer overflows, a vulnerability class that took decades of layered defenses (DEP, Write-XOR-Execute, ASLR, stack canaries, and ultimately memory-safe languages) to contain, because no single mechanism sufficed. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Prompt injection is the top security risk for LLM-integrated applications, yet every defense proposed so far has been broken. 披露的 evaluation signal 是：We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). exact-v1 的观测边界是：We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). 它没有证明 It mirrors the code-data confusion in Von Neumann machines that gives rise to buffer overflows, a vulnerability class that took decades of layered defenses (DEP, Write-XOR-Execute, ASLR, stack canaries, and ultimately memory-safe languages) to contain, because no single mechanism sufficed. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27567:start -->
Primary identity `arXiv:2606.27567v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27567:end -->
<!-- review:SF-2026-ARXIV-2606-27567:end -->

<!-- review:SF-2026-ARXIV-2606-27578:start -->
### 2606.27578 — PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration

**问题与旧路径。** Reward models for Reinforcement Learning from Human Feedback (RLHF) pool preferences across thousands of annotators and fit one global affine calibrator, collapsing raters with systematically different rating-scale offsets and slopes into a single average-rater fit that does not match any individual annotator. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration 的 exact-v1 机制为：PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27578v1 — §2 Method; §Base-model training details.`；Evaluation=`arXiv:2606.27578v1 — §2.3 PRISM setup and base reward model; §3 Experiments`；counterevidence=`arXiv:2606.27578v1 — §3.9 Ablations and failure cases; §4 Discussion; §5 Limitations`。exact-v1 的观测边界是：On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. 它没有证明 PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Reward models for Reinforcement Learning from Human Feedback (RLHF) pool preferences across thousands of annotators and fit one global affine calibrator, collapsing raters with systematically different rating-scale offsets and slopes into a single average-rater fit that does not match any individual annotator. 披露的 evaluation signal 是：On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. exact-v1 的观测边界是：On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. 它没有证明 PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27578:start -->
Primary identity `arXiv:2606.27578v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27578:end -->
<!-- review:SF-2026-ARXIV-2606-27578:end -->

<!-- review:SF-2026-ARXIV-2606-27580:start -->
### 2606.27580 — Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF

**问题与旧路径。** On a tabular Markov decision process (MDP) proof-of-concept, RAC reduces the closed-form policy bias by up to 47.9x at the two-slow-channel configuration, beating wait-for-slow at lower wall-clock cost. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF 的 exact-v1 机制为：Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27580v1 — §2 Method: Retroactive Advantage Correction`；Evaluation=`arXiv:2606.27580v1 — §Setup.; §K = 2 K{=}2 result and cost-quality Pareto.; §Scope of the closed-form result.`；counterevidence=`arXiv:2606.27580v1 — §4 Conclusion; §Appendix E Limitations and Discussion; §Background and discussion.`。exact-v1 的观测边界是：We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. 它没有证明 Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：On a tabular Markov decision process (MDP) proof-of-concept, RAC reduces the closed-form policy bias by up to 47.9x at the two-slow-channel configuration, beating wait-for-slow at lower wall-clock cost. 披露的 evaluation signal 是：We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. exact-v1 的观测边界是：We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. 它没有证明 Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27580:start -->
Primary identity `arXiv:2606.27580v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27580:end -->
<!-- review:SF-2026-ARXIV-2606-27580:end -->

<!-- review:SF-2026-ARXIV-2606-27595:start -->
### 2606.27595 — Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents

**问题与旧路径。** Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents 的 exact-v1 机制为：Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27595v1 — §The Ko-WideSearch Benchmark; §Construction Pipeline; §Normalization-Aware Cell Comparison`；Evaluation=`arXiv:2606.27595v1 — §Experimental Setup; §Results; §Scoring Details`；counterevidence=`arXiv:2606.27595v1 — §Conclusion and Limitations; §Limitations.`。exact-v1 的观测边界是：Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. 它没有证明 Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. 披露的 evaluation signal 是：Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. exact-v1 的观测边界是：Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. 它没有证明 Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27595:start -->
Primary identity `arXiv:2606.27595v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27595:end -->
<!-- review:SF-2026-ARXIV-2606-27595:end -->

<!-- review:SF-2026-ARXIV-2606-27608:start -->
### 2606.27608 — Qwen-Image-2.0-RL Technical Report

**问题与旧路径。** We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Qwen-Image-2.0-RL Technical Report 的 exact-v1 机制为：We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27608v1 — §3.1 Reward Model Training Paradigms; §Training; §4.1 Training Pipeline`；Evaluation=`arXiv:2606.27608v1 — §Evaluation; §Text-to-image generation results.; §Human preference evaluation.`；counterevidence=`arXiv:2606.27608v1 — §Conclusion`。exact-v1 的观测边界是：We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. 它没有证明 We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. 披露的 evaluation signal 是：We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. exact-v1 的观测边界是：We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. 它没有证明 We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27608:start -->
Primary identity `arXiv:2606.27608v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27608:end -->
<!-- review:SF-2026-ARXIV-2606-27608:end -->

<!-- review:SF-2026-ARXIV-2606-27622:start -->
### 2606.27622 — FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks

**问题与旧路径。** FLTrust addresses this challenge by introducing a trusted server-side root dataset that assigns trust scores to client updates for more robust aggregation. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks 的 exact-v1 机制为：In this work, we propose FOGGYTRUST, a hierarchical extension of FLTrust that localizes trust computation to fog nodes, allowing the framework to better handle globally heterogeneous data while preserving robustness within locally homogeneous client groups. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27622v1 — §II-A Background on Byzantine-Robust FL Methods; §II-B FLTrust Algorithm`；Evaluation=`arXiv:2606.27622v1 — §IV Evaluation; §IV-A Experimental Setup; §IV-A 4 Extension Setup`；counterevidence=`arXiv:2606.27622v1 — §V Discussion and Limitations; §V-C Limitations for Data Poisoning Attacks; §VI Conclusion`。exact-v1 的观测边界是：We further show that this two-level architecture can simultaneously address distribution mismatch in trust estimation and client drift across groups by combining local trust-based aggregation with heterogeneity-aware global optimizers such as FedAdam and SCAFFOLD. 它没有证明 In this work, we propose FOGGYTRUST, a hierarchical extension of FLTrust that localizes trust computation to fog nodes, allowing the framework to better handle globally heterogeneous data while preserving robustness within locally homogeneous client groups. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：FLTrust addresses this challenge by introducing a trusted server-side root dataset that assigns trust scores to client updates for more robust aggregation. 披露的 evaluation signal 是：We further show that this two-level architecture can simultaneously address distribution mismatch in trust estimation and client drift across groups by combining local trust-based aggregation with heterogeneity-aware global optimizers such as FedAdam and SCAFFOLD. exact-v1 的观测边界是：We further show that this two-level architecture can simultaneously address distribution mismatch in trust estimation and client drift across groups by combining local trust-based aggregation with heterogeneity-aware global optimizers such as FedAdam and SCAFFOLD. 它没有证明 In this work, we propose FOGGYTRUST, a hierarchical extension of FLTrust that localizes trust computation to fog nodes, allowing the framework to better handle globally heterogeneous data while preserving robustness within locally homogeneous client groups. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27622:start -->
Primary identity `arXiv:2606.27622v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27622:end -->
<!-- review:SF-2026-ARXIV-2606-27622:end -->

<!-- review:SF-2026-ARXIV-2606-27632:start -->
### 2606.27632 — Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety

**问题、约束与旧路径。** As large language models are increasingly deployed in real-world systems, safety failures can still lead to harmful outputs and dangerous misuse. We argue that the essence of safety is adversarial: many failures arise not from natural inputs alone, but from strategic attempts to evade model policies and safeguards. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Notably, Yuvion-8B outperforms most state-of-the-art baselines, including substantially larger models such as GPT-5.4 and Qwen3-MAX, on several safety tasks. Method=https://arxiv.org/html/2606.27632v1 — §2 Content-Safety-Oriented Data System; 3 Yuvion LLM: Progressive Safety Training Paradigm; 3.2 Target Capability Design；Evaluation=https://arxiv.org/html/2606.27632v1 — §4 Evaluation Framework; 4.2 Level 1: Open-source General Benchmarks; 4.3 Level 2: Open-source Content Safety Benchmarks。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27632v1 — §Discussion.; 9 Conclusion; 10 Limitations and Future Work。

<!-- claim:SF-2026-ARXIV-2606-27632:start -->
Claim boundary：仅 arXiv:2606.27632v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27632:end -->
<!-- review:SF-2026-ARXIV-2606-27632:end -->

<!-- review:SF-2026-ARXIV-2606-27634:start -->
### 2606.27634 — Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis

**问题、约束与旧路径。** Small Language Models (SLMs) are increasingly being considered for deployment on edge devices such as laptops, enabling private, low-latency, and locally personalized applications. However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 sequential LoRA personalization 的 checkpoint、reference-set drift 与遗忘监控绑定为持续适配合同。 由 PLATFORM-MONITORING 持有 sensor state、calibration 与 alarm action；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We show that lightweight reference set distributional diagnostics can reveal model-specific instability patterns during sequential LoRA personalization of SLMs, including cases where task-level metrics alone hide harmful adaptation. Method=https://arxiv.org/html/2606.27634v1 — §4.0.4 Training Procedure；Evaluation=https://arxiv.org/html/2606.27634v1 — §Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis; 2.0.1 Continual Learning and Evaluation of Language Models.; 3.2 Model Checkpoints and Evaluation。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27634v1 — §6 Conclusion; 6.0.1 Limitations。

<!-- claim:SF-2026-ARXIV-2606-27634:start -->
Claim boundary：仅 arXiv:2606.27634v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27634:end -->
<!-- review:SF-2026-ARXIV-2606-27634:end -->

<!-- review:SF-2026-ARXIV-2606-27650:start -->
### 2606.27650 — GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies

**问题、约束与旧路径。** LLM-agent simulation faces a joint grounding and scaling problem: agents should act in environments that reflect real urban constraints, yet direct online LLM calls for city-scale populations are computationally prohibitive. We present GenWorld, an empirically grounded urban simulation infrastructure that combines a building-level synthetic city, a structured agent-environment interface, and offline compilation of LLM-derived decision signals into lookup policies for scalable rollout. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。 由 AGENT-PLATFORM 持有 workspace、runtime、acceptance predicate 与 replay；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We demonstrate the infrastructure through three reproducible cases: a full-city weekday rollout, a weekday-weekend behavioral contrast, and a warning-response perturbation with auditable replanning traces. Method=https://arxiv.org/html/2606.27650v1 — §Context Design and Coverage; 6 Platform Architecture; 6.1 System Overview；Evaluation=https://arxiv.org/html/2606.27650v1 — §7 Evaluation Cases and Scalability; 7.1 Evaluation Cases; 7.1.5 Scalability Analysis。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27650v1 — §8 Discussion; Limitations and Future Work; 9 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27650:start -->
Claim boundary：仅 arXiv:2606.27650v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27650:end -->
<!-- review:SF-2026-ARXIV-2606-27650:end -->

<!-- review:SF-2026-ARXIV-2606-27669:start -->
### 2606.27669 — When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search

**问题、约束与旧路径。** Search agents powered by large language models (LLMs) are increasingly used to solve complex information-seeking tasks, requiring multi-step retrieval and reasoning to fulfill user goals. However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on representative LLMs show that ambiguity detection and effective clarification are distinct capabilities, and that repeatedly searching instead of asking for clarification often performs worse than direct guessing, highlighting a critical gap between retrieval ability and interactive problem-solving in current search agents. Method=https://arxiv.org/html/2606.27669v1 — §4 Methodology of Dataset Construction; Benchmark Design and Methodology.; Evaluation Framework and User Simulator.；Evaluation=https://arxiv.org/html/2606.27669v1 — §2.1 Web Search Benchmark; 2.2 Ambiguity Benchmark; 2.3 Interactive Clarification Benchmark。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27669v1 — §Search-heavy guessing reveals a major failure mode.; 6 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27669:start -->
Claim boundary：仅 arXiv:2606.27669v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27669:end -->
<!-- review:SF-2026-ARXIV-2606-27669:end -->

<!-- review:SF-2026-ARXIV-2606-27679:start -->
### 2606.27679 — From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models

**问题、约束与旧路径。** Probe-based uncertainty estimation (UE) has emerged as a prominent approach to detect hallucinations in Large Language Models (LLMs) by learning uncertainty from internal model signals. Yet, recent methods vary simultaneously across feature design, training data construction, and evaluation setting, obscuring what actually drives performance. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。 由 PLATFORM-MONITORING 持有 sensor state、calibration 与 alarm action；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results show that raw hidden states and attention features are difficult to outperform in-domain. Method=https://arxiv.org/html/2606.27679v1 — §Probe Training.; Probe Architecture and Training Size.；Evaluation=https://arxiv.org/html/2606.27679v1 — §Toolkits, Benchmarks, and Evaluation.; 3.1 Experimental Setup; Evaluation Metrics.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, under distribution shift, structured and compressed features are more robust, suggesting that in-domain performance alone is insufficient to measure progress. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27679v1 — §4.2 Results and Discussion; 5 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27679:start -->
Claim boundary：仅 arXiv:2606.27679v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27679:end -->
<!-- review:SF-2026-ARXIV-2606-27679:end -->

<!-- review:SF-2026-ARXIV-2606-27681:start -->
### 2606.27681 — Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation

**问题、约束与旧路径。** World models in partially observed environments rely on latent representations that summarize interaction history, but in many modern LLM-based architectures predictive performance fails to reflect representation quality due to history bypass, rendering the latent state unidentifiable. Strict latent state mediation, requiring predictions to depend only on the latent state and action, is a classical principle that resolves this, but enforcing it in text-based settings is an open challenge: textual latent states are discrete and non-differentiable, precluding variational training, and expressive LLM decoders readily ignore the bottleneck. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 strict mediation 让 textual belief state 成为唯一可测试的预测状态，阻断 history bypass。 由 MULTIMODAL-WORLD-MODELS 持有 belief/latent state、transition 与 physical boundary；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on TextWorld and ScienceWorld show preserved one-step prediction accuracy alongside up to 57\% gains in representation quality and 98\% improvements in rollout performance, increasing with task complexity and horizon. Method=https://arxiv.org/html/2606.27681v1 — §Proposition 2 (Non-identifiability under leaky architectures) .; Proposition 3 (Training–inference consistency) .; 4.2 Model Architecture；Evaluation=https://arxiv.org/html/2606.27681v1 — §2 Problem Setup: Text Based POMDPs; 5 Experimental Evaluation; 5.3 Evaluation Metrics。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection. Strict mediation 增加训练成本，也可能让有损 textual state 成为瓶颈；无需可识别性时，直接 latent/history access 仍是合理旧路径。 Counterevidence/limitation=https://arxiv.org/html/2606.27681v1 — §7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27681:start -->
Claim boundary：仅 arXiv:2606.27681v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27681:end -->
<!-- review:SF-2026-ARXIV-2606-27681:end -->

<!-- review:SF-2026-ARXIV-2606-27683:start -->
### 2606.27683 — CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence

**问题、约束与旧路径。** Edge devices increasingly invoke large language models (LLMs) through API services for context aware edge intelligence, while edge generated data may be collected to improve LLMs and may introduce sensitive, copyrighted, harmful, or outdated information into model behavior. Machine unlearning offers a practical way to remove the influence of undesired data without retraining LLMs. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Compared with eleven white box and gray box unlearning baselines, CBD achieves a better unlearning utility trade off and its performance varies little across settings. Method=https://arxiv.org/html/2606.27683v1 — §III Preliminaries and Framework; III-A White-Box and Gray-Box Unlearning Methods; III-B API-Only Scenario and Proposed Framework；Evaluation=https://arxiv.org/html/2606.27683v1 — §VI Experiments; VI-A Experimental Setup; VI-B Performance Evaluation。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** On WMDP, it lowers hazardous knowledge accuracy to 25.68, near random guessing, while preserving MMLU accuracy of 52.67. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27683v1 — §VII Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27683:start -->
Claim boundary：仅 arXiv:2606.27683v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27683:end -->
<!-- review:SF-2026-ARXIV-2606-27683:end -->

<!-- review:SF-2026-ARXIV-2606-27704:start -->
### 2606.27704 — AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis

**问题、约束与旧路径。** TinyML models deployed on edge devices are increasingly adopted in safety/security-critical applications, making them a prime target for adversarial example (AE) attacks where inputs are modified to cause misclassifications. However, existing AE detection methods either require white-box model access, which is often unavailable in licensed black-box deployments, or rely on input pre-processing stages that add non-trivial latency and resource overhead, often exceeding what mission-critical applications can afford on their inference path. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results demonstrate the viability of power-based AE detection for secure, accuracy-critical TinyML deployments in black-box environments. Method=https://arxiv.org/html/2606.27704v1 — §IV AdvScan Algorithm; V-A 3 Adversarial Examples (AE) Generation Methodologies; V-C Evaluation of the AdvScan Algorithm；Evaluation=https://arxiv.org/html/2606.27704v1 — §AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis; II-D Power Analysis; II-E Side Channel Analysis for Adversarial Behavior Detection。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27704v1 — §II-F Threat Model; IV-D Discussion of Merits and Limitations of AdvScan; VI Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27704:start -->
Claim boundary：仅 arXiv:2606.27704v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27704:end -->
<!-- review:SF-2026-ARXIV-2606-27704:end -->

<!-- review:SF-2026-ARXIV-2606-27709:start -->
### 2606.27709 — Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning

**问题、约束与旧路径。** Recent work has shown that fine-tuning large language models (LLMs) for social warmth degrades factual reliability and increases sycophancy. We investigate a related but distinct failure mode: warmth fine-tuning also weakens adversarial safety, making models more susceptible to jailbreaks and harmful output generation. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。 由 TRAIN-DATA 持有 sample provenance、mixture 与 admission state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective. Method=https://arxiv.org/html/2606.27709v1 — §3 Methods; 3.2 Study design; 3.3 Training data and data construction；Evaluation=https://arxiv.org/html/2606.27709v1 — §Experiment 1.; Experiment 2.; Experiment 3.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27709v1 — §5 Discussion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27709:start -->
Claim boundary：仅 arXiv:2606.27709v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27709:end -->
<!-- review:SF-2026-ARXIV-2606-27709:end -->

<!-- review:SF-2026-ARXIV-2606-27732:start -->
### 2606.27732 — Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation

**问题、约束与旧路径。** Discrete diffusion language models (dLLMs) recover masked tokens in parallel, offering significant speedups over autoregressive (AR) generation. However, such promising frameworks face a fundamental architectural design dilemma: \ding{182} Adopting bidirectional attention achieves strong generation quality by allowing each position to access the full context, but is inherently incompatible with KV caching, limiting inference throughput in batch-serving scenarios; \ding{183} Conversely, causal attention enables efficient cached inference but loses all right-side context, substantially degrading generation quality. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 asymmetric bidirectional sidecar 重构 diffusion-LM 的右上下文、KV cache 与 parallel decode 取舍。 由 MULTIMODAL-GENERATIVE-PARADIGMS 持有 generation dependency、cache 与 commit order；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average. Method=https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference；Evaluation=https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average. Side path 增加参数、训练耦合与 cache-version 复杂度；要求 exact streaming 或 kernel 不支持时回退 causal generation。 Counterevidence/limitation=https://arxiv.org/html/2606.27732v1 — §5 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27732:start -->
Claim boundary：仅 arXiv:2606.27732v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27732:end -->
<!-- review:SF-2026-ARXIV-2606-27732:end -->

<!-- review:SF-2026-ARXIV-2606-27739:start -->
### 2606.27739 — The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment

**问题、约束与旧路径。** Process reward models (PRMs) enhance the reasoning capabilities of large language models (LLMs) by providing fine-grained feedback, yet training PRMs typically requires expensive stepwise annotations. Outcome-supervised PRMs offer a scalable alternative by learning from final-answer correctness alone, but this introduces a fundamental *credit assignment* challenge, i.e., attributing outcomes to responsible reasoning steps. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Extensive experiments demonstrate that **LCA** consistently outperforms state-of-the-art outcome-supervised PRMs across multiple tasks and backbones. Method=https://arxiv.org/html/2606.27739v1 — §4 Method; C.2 PRM Training Details; Model architecture.；Evaluation=https://arxiv.org/html/2606.27739v1 — §3 Analysis; 3.3 Theoretical Analysis; 5 Experiments。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》在 3 Analysis; 3.3 Theoretical Analysis; 5 Experiments 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27739v1 — §6 Conclusion; Limitations; B.7 Discussion。

<!-- claim:SF-2026-ARXIV-2606-27739:start -->
Claim boundary：仅 arXiv:2606.27739v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27739:end -->
<!-- review:SF-2026-ARXIV-2606-27739:end -->

<!-- review:SF-2026-ARXIV-2606-27743:start -->
### 2606.27743 — End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference

**问题、约束与旧路径。** Large Language Models (LLMs) inference is typically deployed under a static resource assumption, where models execute a fixed computational graph regardless of the runtime environment. However, real-world cloud infrastructure is inherently dynamic, characterized by fluctuating availability (e.g., spot instance preemption) and tiered Quality-of-Service requirements. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。 由 INFER-SCHEDULING 持有 request budget、compute allocation 与 fallback；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time. Method=https://arxiv.org/html/2606.27743v1 — §3 Methodology; 3.5 Training and Inference；Evaluation=https://arxiv.org/html/2606.27743v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27743v1 — §4.6 Discussion and Limitations; 5 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27743:start -->
Claim boundary：仅 arXiv:2606.27743v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27743:end -->
<!-- review:SF-2026-ARXIV-2606-27743:end -->

<!-- review:SF-2026-ARXIV-2606-27757:start -->
### 2606.27757 — Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework

**问题、约束与旧路径。** Large language models (LLMs) have attracted widespread attention from academia and industry, yet their deployment raises critical security concerns regarding robustness and reliability. Planning, a core component of intelligent behavior, remains challenging for LLMs, which often produce infeasible or incorrect solutions in long-horizon decision-making tasks due to inherent complexity. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。 由 AGENT-PLANNING 持有 world state、plan revision 与 executable commit；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Empirical results demonstrate that the proposed framework consistently improves both feasibility and correctness in long-horizon planning tasks. Method=https://arxiv.org/html/2606.27757v1 — §Towards Reliable and Robust LLM Planning: A Symbolic Feedback-Driven Iterative Self-Refinement Framework Thanks: * Corresponding author at: Institute of Automation, Chinese Academy of Sciences, Beijing, China.; III METHODOLOGY; III-B Feedback-Driven Iterative Self-Refinement Framework；Evaluation=https://arxiv.org/html/2606.27757v1 — §IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》在 IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27757v1 — §V CONCLUSION。

<!-- claim:SF-2026-ARXIV-2606-27757:start -->
Claim boundary：仅 arXiv:2606.27757v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27757:end -->
<!-- review:SF-2026-ARXIV-2606-27757:end -->

<!-- review:SF-2026-ARXIV-2606-27780:start -->
### 2606.27780 — Understanding Rollout Error in Graph World Models

**问题、约束与旧路径。** World models are increasingly used for planning, yet most analyses of rollout error assume vector-valued states and scalar error amplification. Many planning environments, however, are naturally graph-structured: agents, tools, skills, routes, and dependencies interact through evolving relations. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。 由 MULTIMODAL-WORLD-MODELS 持有 belief/latent state、transition 与 physical boundary；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail. Method=https://arxiv.org/html/2606.27780v1 — §Agent graphs and skill-graph systems.; 3 Graph World Model Framework; Framework overview.；Evaluation=https://arxiv.org/html/2606.27780v1 — §5 Dataset and Evaluation Protocol; Graph world model setup.; 7 Experiments。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27780v1 — §7.2.3 Global spectral amplification differs from local hub failure; 7.5.4 OOD perturbation confirms the FE contraction boundary; 7.6.2 Role-dependent failure sensitivity。

<!-- claim:SF-2026-ARXIV-2606-27780:start -->
Claim boundary：仅 arXiv:2606.27780v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27780:end -->
<!-- review:SF-2026-ARXIV-2606-27780:end -->

<!-- review:SF-2026-ARXIV-2606-27791:start -->
### 2606.27791 — NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation

**问题、约束与旧路径。** Hybrid attention models that mix full and sliding-window attention across layers offer a promising approach to efficient long-context inference, but the critical question of \emph{which layers} should retain full attention remains unsolved. Existing methods use either fixed periodic patterns or attention-based heuristics that may not capture what matters for downstream accuracy. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 answer-token NLL degradation 选择保留 full-attention 的层，改变 hybrid attention 的 calibration owner。 由 MODEL-LONG-CONTEXT 持有 attention reach、layer policy 与 context budget；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** De-confounding analysis shows the signal is consistent with long-range attention needs rather than generic layer sensitivity. Method=https://arxiv.org/html/2606.27791v1 — §NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation; 3 Method；Evaluation=https://arxiv.org/html/2606.27791v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** The method requires only $\sim$15 minutes of one-time calibration, advancing the efficiency-accuracy Pareto frontier for long-context LLM deployment. 该结果只保留为局部方法/实验语境；它不新增长期 owner、authority、coexistence 或 fallback 命题。 Counterevidence/limitation=https://arxiv.org/html/2606.27791v1 — §5 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27791:start -->
Claim boundary：仅 arXiv:2606.27791v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27791:end -->
<!-- review:SF-2026-ARXIV-2606-27791:end -->

<!-- review:SF-2026-ARXIV-2606-27797:start -->
### 2606.27797 — Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems

**问题、约束与旧路径。** Knowledge Distillation (KD) enables training smaller student models under the guidance of larger teacher models, and the widely adopted TRL library implements it. Yet, TRL treats both models symmetrically, missing opportunities to exploit their pronounced asymmetry in memory footprint, and communication requirements. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 按 teacher/student 不对称分别选择模型分片与拓扑通信，改变 KD runtime partition contract。 由 TRAIN-DISTRIBUTED-TRAINING 持有 partition、topology、version 与 synchronization；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results showed that exploiting teacher--student asymmetry through topology-aware parallelism notably accelerated GKD training on production HPC clusters at our company Method=https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training；Evaluation=https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》在 3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 非对称方案增加 handoff buffering 与 topology search；teacher/student footprint 相近时，共享方案仍更简单。 Counterevidence/limitation=https://arxiv.org/html/2606.27797v1 — §6 Conclusions。

<!-- claim:SF-2026-ARXIV-2606-27797:start -->
Claim boundary：仅 arXiv:2606.27797v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27797:end -->
<!-- review:SF-2026-ARXIV-2606-27797:end -->

<!-- review:SF-2026-ARXIV-2606-27806:start -->
### 2606.27806 — Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents

**问题、约束与旧路径。** Language agents plan by generating not only actions but also implicit predictions of how the world will change. These imagined state updates make agents flexible, but they also create a distinct failure mode: hallucinated state claims can be written into context and propagated across subsequent decisions. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 parametric transition model 校验 agent imagined delta，并把 disagreement 变成 targeted revision gate。 由 AGENT-PLANNING 持有 world state、plan revision 与 executable commit；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning. Method=https://arxiv.org/html/2606.27806v1 — §Our approach: GILP.; LLM API ecosystem.; 4 Method: Grounded Iterative Language Planning；Evaluation=https://arxiv.org/html/2606.27806v1 — §5 Experiments; Setup.; Cost analysis.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning. Learned transition verifier 可能与 planner 共享盲点，也不是 physics oracle；分歧或 OOD state 回退 environment validation 或人工复核。 Counterevidence/limitation=https://arxiv.org/html/2606.27806v1 — §6 Discussion; 7 Limitations; 8 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27806:start -->
Claim boundary：仅 arXiv:2606.27806v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27806:end -->
<!-- review:SF-2026-ARXIV-2606-27806:end -->

<!-- review:SF-2026-ARXIV-2606-27814:start -->
### 2606.27814 — ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks

**问题、约束与旧路径。** Training small language-model agents for long-horizon interactive tasks requires both fast imitation and reward-driven improvement. On-policy distillation (OPD) provides dense teacher guidance and typically improves rapidly in the early stage, but its gains saturate once the student approaches the teacher, limiting the final performance ceiling. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points. Method=https://arxiv.org/html/2606.27814v1 — §4 Method; 5.4 Training Dynamics and Diagnostic Metrics; Appendix A Method and Algorithmic Details；Evaluation=https://arxiv.org/html/2606.27814v1 — §5 Experiments; 5.1 Experimental Setup; Datasets & Benchmarks.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27814v1 — §6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27814:start -->
Claim boundary：仅 arXiv:2606.27814v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27814:end -->
<!-- review:SF-2026-ARXIV-2606-27814:end -->

<!-- review:SF-2026-ARXIV-2606-27826:start -->
### 2606.27826 — NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms

**问题、约束与旧路径。** Embodied agents driven by multimodal large language models (MLLMs) can often complete everyday tasks from visual observations, but goal achievement does not establish whether they proactively respect unstated social norms. Existing benchmarks assess explicit norm judgments or constrained behavior, but rarely test whether agents infer and apply scene-relevant norms during ordinary tasks. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Across three MLLM planners, goal achievement substantially exceeds norm compliance without guidance (67.4% versus 24.7%), while both broad and rule-specific guidance improve compliance, indicating that planners can often comply when prompted but not reliably on their own. Method=https://arxiv.org/html/2606.27826v1 — §3.1 Benchmark Design; Appendix F NormPerceptor Training Data Details；Evaluation=https://arxiv.org/html/2606.27826v1 — §NormAct : A Benchmark for Hidden Social Norm Compliance in Embodied Planning; 2.1 Social Norm Evaluation in (M)LLMs; 3 The NormAct Benchmark。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** NormAct therefore supports the development of embodied agents that pursue everyday goals while proactively respecting unstated social norms. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27826v1 — §7 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27826:start -->
Claim boundary：仅 arXiv:2606.27826v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27826:end -->
<!-- review:SF-2026-ARXIV-2606-27826:end -->

<!-- review:SF-2026-ARXIV-2606-27841:start -->
### 2606.27841 — WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks

**问题、约束与旧路径。** The widespread adoption of Artificial Intelligence (AI) has led to increasing concerns about energy consumption, yet there is a lack of standardized methodologies to accurately estimate AI inference energy consumption, particularly across various tasks and architectures. In this study, we propose a task independent, layer-wise energy estimation model for AI architectures. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 inference energy estimation 从整模型 proxy 拆成可跨任务/架构迁移的 layer-wise measurement contract。 由 PLATFORM-COST 持有 measurement state、resource attribution 与 cost model；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures. Method=https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.2 Layer-Wise Energy Estimation Framework；Evaluation=https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.1 Experimental Protocol; 4 Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures. Layer recomposition 可能遗漏 fusion、memory hierarchy 与 concurrency interaction；生产真值仍由 whole-run meter 持有，漂移时重校 layer model。 Counterevidence/limitation=https://arxiv.org/html/2606.27841v1 — §5 Discussion; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27841:start -->
Claim boundary：仅 arXiv:2606.27841v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27841:end -->
<!-- review:SF-2026-ARXIV-2606-27841:end -->

<!-- review:SF-2026-ARXIV-2606-27866:start -->
### 2606.27866 — FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models

**问题、约束与旧路径。** Mixture-of-Experts (MoE) language models scale model ability with sparsely activated experts, making this architecture a standard recipe for modern large models. However, sparse activation does not remove the deployment burden of storing and serving all experts, and the available deployment budget can vary substantially across devices, users, and workloads. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把一次性 MoE compression artifact 改成 nested subnet family 与可在线切换的 budget state。 由 MODEL-MOE 持有 expert capacity、nested subnet 与 routing budget；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** For deployment, our pruned subnetworks deliver real memory reduction and throughput gains, and further support realtime online budget switching with kernel-level co-design. Method=https://arxiv.org/html/2606.27866v1 — §3 Method; Clip FFN Forward Kernel Co-Design.; Toward Co-Designed Online Budget Scheduling.；Evaluation=https://arxiv.org/html/2606.27866v1 — §4 Experiments; 4.1 Experimental Setup; Implementation Details and Evaluation Tasks.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Specifically, on Qwen2-57B-A14B, our method retains ~99.8% of base performance while pruning 50% of routed expert parameters even without fine-tuning. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27866v1 — §5 Conclusion; Limitations and Future Works.; A.2 Additional Discussion on Cross-Budget Transfer and Cross-Model Trends。

<!-- claim:SF-2026-ARXIV-2606-27866:start -->
Claim boundary：仅 arXiv:2606.27866v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27866:end -->
<!-- review:SF-2026-ARXIV-2606-27866:end -->

<!-- review:SF-2026-ARXIV-2606-27906:start -->
### 2606.27906 — Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC

**问题、约束与旧路径。** Recent phone-class mobile SoCs expose practical NPU execution paths for on-device vision-language model (VLM) inference, but developers still lack phase-level guidance for mapping VLM pipelines across heterogeneous backends. We present a hardware-in-the-loop characterization of VLM inference on the Qualcomm SM8750 (Snapdragon 8 Elite), covering phase throughput, cache-state effects, 100-run thermal stability, energy, heterogeneous CPU/NPU pipeline configurations, and visual-token-budget sensitivity. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以真实 mobile SoC 证据拆开 vision encoder、prefill、decode、cache 与 thermal phase 的 backend placement。 由 INFER-REQUEST-LIFECYCLE 持有 request phase、runtime placement、queue 与 latency state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Finally, we show that a four-step graph rewrite enables previously unsupported encoders, such as Phi-3.5-V, to reach the QNN path with up to 22x speedup, providing a practical porting recipe for mobile VLM deployment. Method=https://arxiv.org/html/2606.27906v1 — §7.2. Methodology and Outcomes on Phi-3.5-V；Evaluation=https://arxiv.org/html/2606.27906v1 — §2. Platform and Experimental Setup; 3.1. Phase-Level Results; 6.1. Three-Backend Benchmark。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Using FastVLM-0.5B as an end-to-end case study, together with encoder-only measurements across four architecture families, we show that phase matters: NPU execution is highly phase-dependent, delivering 1.64x speedup for prefill but only 1.18x for decode, while vision encoders achieve 20-45x speedups over CPU. Simulation 与 component latency 不证明生产 SLO 或 embodied success；mismatch、thermal drift 或 deadline miss 时回退已实测的保守 placement/control。 Counterevidence/limitation=https://arxiv.org/html/2606.27906v1 — §8. Discussion; 10. Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27906:start -->
Claim boundary：仅 arXiv:2606.27906v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27906:end -->
<!-- review:SF-2026-ARXIV-2606-27906:end -->

<!-- review:SF-2026-ARXIV-2606-27934:start -->
### 2606.27934 — Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking

**问题、约束与旧路径。** Performance numbers reported for hardware are accepted on trust: the reader cannot recompute them, the apparatus is gone, and the silicon itself can be silently wrong, with fleet studies reporting on the order of one core in a thousand returning incorrect arithmetic with no error raised. We make a reported hardware measurement a tamper-evident, independently checkable record. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We demonstrate the construction across Blackwell and Hopper GPUs and report a residual-floor and reproducibility map by precision, size, and device. Method=https://arxiv.org/html/2606.27934v1 — §Approach.；Evaluation=https://arxiv.org/html/2606.27934v1 — §Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We then treat the check itself as a security object: a probe seed committed for offline reproducibility is an attack surface, and a probe-aware adversary can hide a corruption in the probe's null space, fooling even a quorum of bit-identical witnesses, while a Fiat-Shamir challenge derived from the claimed output closes this. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27934v1 — §10 Threat model and guarantees; 12 Physical stress and the trust boundary; 14 Scope and limitations。

<!-- claim:SF-2026-ARXIV-2606-27934:start -->
Claim boundary：仅 arXiv:2606.27934v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27934:end -->
<!-- review:SF-2026-ARXIV-2606-27934:end -->

<!-- review:SF-2026-ARXIV-2606-27936:start -->
### 2606.27936 — Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy

**问题、约束与旧路径。** The widespread collection of fine-grained location data by commercial data brokers creates a re-identification risk that is not widely recognised by the public. While prior research has established that mobility traces are highly unique and that individuals can, in principle, be identified from a handful of spatio-temporal points, such attacks have historically required significant manual effort from skilled analysts, limiting their practical scale. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified 18 of the 25 re-identifiable individuals (72%) and 18 of 43 cases overall (41.9%). Method=https://arxiv.org/html/2606.27936v1 — §3 Methodology; 3.2 Study Design and Simulated Data；Evaluation=https://arxiv.org/html/2606.27936v1 — §4 Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27936v1 — §Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy; Threat model.; 5 Discussion and Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27936:start -->
Claim boundary：仅 arXiv:2606.27936v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27936:end -->
<!-- review:SF-2026-ARXIV-2606-27936:end -->

<!-- review:SF-2026-ARXIV-2606-27944:start -->
### 2606.27944 — It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents

**问题、约束与旧路径。** Phone-use Agents can execute complex tasks end to end across real mobile applications. By operating a real device on the user's behalf, they reach far more functionalities than CLI agents, which amplifies the real-world harm they can cause when driven for malicious purposes. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved. Method=https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework；Evaluation=https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework; 5 Evaluation Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27944v1 — §3 Threat Model; 8 Discussion and Limitation; 9 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27944:start -->
Claim boundary：仅 arXiv:2606.27944v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27944:end -->
<!-- review:SF-2026-ARXIV-2606-27944:end -->

<!-- review:SF-2026-ARXIV-2606-27962:start -->
### 2606.27962 — Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence

**问题、约束与旧路径。** This paper presents a cloud-native simulation infrastructure framework for embodied intelligence that supports large-scale training, standardized evaluation, and simulation-based data collection. The framework unifies simulation environment generation, task execution, trajectory collection, model evaluation, data management, and cloud services into a scalable and reproducible platform. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。 由 PLATFORM-FOUNDATIONS 持有 environment、artifact、scheduler 与 lifecycle control；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We argue that cloud-native simulation infrastructure provides a unified foundation for data generation, model training, standardized evaluation, and real-world deployment, and will play a key role in the future development of embodied intelligence. Method=https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 2 Overall Positioning and Design Principles; 2.3 Design Principles；Evaluation=https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》在 Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27962v1 — §3.3 Limitations of Current Solutions; 6.5 Failure Data and Corrective Data。

<!-- claim:SF-2026-ARXIV-2606-27962:start -->
Claim boundary：仅 arXiv:2606.27962v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27962:end -->
<!-- review:SF-2026-ARXIV-2606-27962:end -->

<!-- review:SF-2026-ARXIV-2606-27976:start -->
### 2606.27976 — SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval

**问题、约束与旧路径。** Dense retrieval systems expose document geometry when vector stores are compromised, and a global protective transform can often be aligned from known pairs. We study SHARD, which splits PCA coordinates into a short routing prefix and a residual protected by independent cell-local orthogonal keys. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。 由 AGENT-RAG 持有 retrieval index、privacy boundary 与 evidence handoff；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** It supports CKKS ciphertext--plaintext reranking but is evaluated as a leakage trade-off, not a cryptographic document-privacy guarantee. Method=https://arxiv.org/html/2606.27976v1 — §Appendix A Reproduced baseline analyses from the global-linear system；Evaluation=https://arxiv.org/html/2606.27976v1 — §8 Experiments; Integral multi-encoder evaluation at 10 6 10^{6} scale.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** SHARD preserves retrieval and compartmentalizes alignment evidence, but does not provide DP, unlinkability, or cancellable templates. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27976v1 — §3 Threat Model; A measured limitation: overlap reference lookup.; 9 Discussion。

<!-- claim:SF-2026-ARXIV-2606-27976:start -->
Claim boundary：仅 arXiv:2606.27976v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27976:end -->
<!-- review:SF-2026-ARXIV-2606-27976:end -->

<!-- review:SF-2026-ARXIV-2606-27997:start -->
### 2606.27997 — Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings

**问题、约束与旧路径。** Benchmarks of machine learning models often include many datasets, making evaluation expensive. For efficiency, it is preferable to perform evaluations on small, representative datasets instead. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Additional experiments indicate that the effectiveness of selection approaches depends on both the quality of dataset representations and the scale of the benchmarking regime. Method=https://arxiv.org/html/2606.27997v1 — §5.1. Evaluation methodology; Recommender Systems.; Recommender Systems；Evaluation=https://arxiv.org/html/2606.27997v1 — §Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings; Benchmark Setting; Theoretical results summary。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27997v1 — §7. Conclusions and discussion。

<!-- claim:SF-2026-ARXIV-2606-27997:start -->
Claim boundary：仅 arXiv:2606.27997v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27997:end -->
<!-- review:SF-2026-ARXIV-2606-27997:end -->

<!-- review:SF-2026-ARXIV-2606-28011:start -->
### 2606.28011 — From Detection to Action: Using LLM Agents for Fault-Tolerant Control

**问题、约束与旧路径。** We propose an agentic Large Language Model (LLM) framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. The approach couples (i) a multi-agent workflow that decomposes operator duties into monitoring, planning, action synthesis, simulation, validation, and reprompting; (ii) a Digital Process Plant Twin (DPPT) that exposes plant data, models, and a simulation service for pre-execution testing; and (iii) a Graph Retrieval-Augmented Generation (Graph RAG) layer built on the CPSMod ontology, which organizes plant knowledge (structure, function, hybrid dynamics, control context, and fault semantics) into a graph that supports relation-aware, multi-hop retrieval for the agents. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。 由 AGENT-WORKFLOW 持有 artifact state、verifier/interlock 与 fallback；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Results with lightweight LLMs (GPT-4o-mini and GPT-4.1-mini) show that semantically grounded agents can derive valid recovery decisions within latency budgets compatible with the respective process dynamics, demonstrating a practical pathway from detection to validated corrective action across both discrete and continuous FTC tasks. Method=https://arxiv.org/html/2606.28011v1 — §3 LLM-based agentic framework for fault-tolerant control；Evaluation=https://arxiv.org/html/2606.28011v1 — §4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》在 4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28011v1 — §6 Discussion。

<!-- claim:SF-2026-ARXIV-2606-28011:start -->
Claim boundary：仅 arXiv:2606.28011v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28011:end -->
<!-- review:SF-2026-ARXIV-2606-28011:end -->

<!-- review:SF-2026-ARXIV-2606-28013:start -->
### 2606.28013 — The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization

**问题、约束与旧路径。** Headline type-correctness (TC\%) of LLM autoformalization has climbed from $\sim$53\% to $\sim$76\% in two years, yet this scalar conceals which errors each method resolves. We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 autoformalization 的 type correctness 与 semantic equivalence 交叉分层，防止单标量误归因。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). Method=https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant；Evaluation=https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). Semantic judge 与 selector 都可能错误或相关；uncovered/undecidable 必须保持 Unknown，高风险分歧交回独立 verification 或人工。 Counterevidence/limitation=https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28013:start -->
Claim boundary：仅 arXiv:2606.28013v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28013:end -->
<!-- review:SF-2026-ARXIV-2606-28013:end -->

<!-- review:SF-2026-ARXIV-2606-28037:start -->
### 2606.28037 — Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors

**问题、约束与旧路径。** The machine learning(ML) component of an ML-enabled system evolves through retraining, fine-tuning, and optimization, so previously valid test results may no longer hold. A single evolution step can worsen performance on some test cases while improving others, making regression test prioritization inherently directional. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results show that behavior-space ideas can be operationalized into a practical and efficient mechanism for repeated-update regression testing of evolving ML-enabled systems. Method=https://arxiv.org/html/2606.28037v1 — §Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors; 4.1.1. Tasks, Datasets, and Model Architectures；Evaluation=https://arxiv.org/html/2606.28037v1 — §4. Evaluation; 4.1. Experiment Setup; 4.1.5. Reproducibility and Additional Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** In an empirical study across classification and regression tasks, GBV-PD consistently outperformed non-directional baselines and remained competitive with a full-gradient reference, while offering better time and storage profiles for repeated updates via reusable GBV caching. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28037v1 — §5. Discussion; 5.3. Limitations; 6. Threats to Validity。

<!-- claim:SF-2026-ARXIV-2606-28037:start -->
Claim boundary：仅 arXiv:2606.28037v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28037:end -->
<!-- review:SF-2026-ARXIV-2606-28037:end -->

<!-- review:SF-2026-ARXIV-2606-28050:start -->
### 2606.28050 — Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA

**问题、约束与旧路径。** LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation is easier than generation. We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confound of open-domain comparisons. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These findings challenge core assumptions in self-evaluation pipelines. Method=https://arxiv.org/html/2606.28050v1 — §3 Methodology; Hard-negative generation for evaluator training.; LoRA training budget.；Evaluation=https://arxiv.org/html/2606.28050v1 — §Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ).。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》在 Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28050v1 — §5 Results and Discussion; 6 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-28050:start -->
Claim boundary：仅 arXiv:2606.28050v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28050:end -->
<!-- review:SF-2026-ARXIV-2606-28050:end -->

<!-- review:SF-2026-ARXIV-2606-28061:start -->
### 2606.28061 — ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents

**问题、约束与旧路径。** Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** The results show that successful tool execution does not imply appropriate privacy disclosure: an agent may complete a task while transmitting unnecessary private information through intermediate tool calls. Method=https://arxiv.org/html/2606.28061v1 — §4.7 System Modules；Evaluation=https://arxiv.org/html/2606.28061v1 — §ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents Note: This work was supported by the Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing (GJJ-25-009).; 2.1 Privacy Evaluation of Large Language Models; 2.2 Tool-Using Agents and Agent Benchmarks。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28061v1 — §8 Representative Failure Cases; 9 Discussion and Implications; 10 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28061:start -->
Claim boundary：仅 arXiv:2606.28061v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28061:end -->
<!-- review:SF-2026-ARXIV-2606-28061:end -->

<!-- review:SF-2026-ARXIV-2606-28070:start -->
### 2606.28070 — JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications

**问题、约束与旧路径。** JD$.$com, one of the world's largest e-commerce platforms, serves over 700 million active users and millions of merchants, with a catalog of tens of billions of SKUs. At this scale, high-quality, structured item knowledge underpins a better consumer experience, lower management costs, and higher operational efficiency-yet producing and serving it poses three industrial-scale challenges: fast-emerging concepts, high-quality knowledge production for massive SKUs, and diverse downstream requirements. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。 由 PLATFORM-FOUNDATIONS 持有 environment、artifact、scheduler 与 lifecycle control；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Search-traffic coverage reaches 80.4%, item-information quality issues drop by 37%, the automated fill rate of core attributes during item listing exceeds 80%. Method=https://arxiv.org/html/2606.28070v1 — §2 Architecture Overview; 3.1 Method Overview; 3.2.2 Algorithm-driven ontology growth (bottom-up)；Evaluation=https://arxiv.org/html/2606.28070v1 — §3.3 Results; 4.2.3 Results; Module 1: Data evaluation.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》在 3.3 Results; 4.2.3 Results; Module 1: Data evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28070v1 — §9 Conclusion; 10 Limitations and Future Work。

<!-- claim:SF-2026-ARXIV-2606-28070:start -->
Claim boundary：仅 arXiv:2606.28070v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28070:end -->
<!-- review:SF-2026-ARXIV-2606-28070:end -->

<!-- review:SF-2026-ARXIV-2606-28116:start -->
### 2606.28116 — Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability

**问题、约束与旧路径。** Frontier large language model training consumes massive accelerator fleets and long wall-clock computation, making stability failures costly when they occur. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。 由 PLATFORM-MONITORING 持有 sensor state、calibration 与 alarm action；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our fault-injection experiments on low-precision attention, large learning-rate, and combined faults show that these signals provide distinct signatures for different failures, triggering thousands of steps before loss divergence. Method=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; Training-stability monitors.; 5 Designing Module-Specific Monitors from First Principles；Evaluation=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; 1 Introduction。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. Pre-loss signal 可能噪声大且依赖 family；它们保持 observe-first，缺失校准时 abstain，不能自动干预训练。 Counterevidence/limitation=https://arxiv.org/html/2606.28116v1 — §6 Limitations; 7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28116:start -->
Claim boundary：仅 arXiv:2606.28116v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28116:end -->
<!-- review:SF-2026-ARXIV-2606-28116:end -->

<!-- review:SF-2026-ARXIV-2606-28128:start -->
### 2606.28128 — PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation

**问题、约束与旧路径。** Video generation models have emerged as a promising paradigm for embodied world simulation. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。 由 MULTIMODAL-WORLD-MODELS 持有 belief/latent state、transition 与 physical boundary；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Beyond generation, as a world model under the WorldArena action-planner protocol it raises the closed-loop success rate from 16.0\% to 24.0\% and further improves downstream policy success, indicating that physically aligned video models yield stronger representations for robotic manipulation. Method=https://arxiv.org/html/2606.28128v1 — §3 Method; 3.4 Training and Inference; Training data.；Evaluation=https://arxiv.org/html/2606.28128v1 — §4 Experiments; 4.1 Experimental Setup; Benchmarks.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28128v1 — §5 Conclusion; Appendix F Limitations and future work。

<!-- claim:SF-2026-ARXIV-2606-28128:start -->
Claim boundary：仅 arXiv:2606.28128v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28128:end -->
<!-- review:SF-2026-ARXIV-2606-28128:end -->

<!-- review:SF-2026-ARXIV-2606-28153:start -->
### 2606.28153 — Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models

**问题、约束与旧路径。** Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness. Method=https://arxiv.org/html/2606.28153v1 — §Detection-based methods; Perturbation-based methods; Representation-based methods；Evaluation=https://arxiv.org/html/2606.28153v1 — §4 Experiments; 4.1 Experimental Setup; Experimental Design。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28153v1 — §6 Conclusion; Conclusions and practical guidance.; B.3 Limitations and Future Directions。

<!-- claim:SF-2026-ARXIV-2606-28153:start -->
Claim boundary：仅 arXiv:2606.28153v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28153:end -->
<!-- review:SF-2026-ARXIV-2606-28153:end -->

<!-- review:SF-2026-ARXIV-2606-28166:start -->
### 2606.28166 — Tandem Reinforcement Learning with Verifiable Rewards

**问题、约束与旧路径。** Reinforcement learning with verifiable rewards (RLVR) has significantly improved the reasoning capability of large language models, reaching expert or even superhuman performance in domains such as competition math. However, whether weaker agents and humans can actually harness this capability is far less certain, with RLVR documented to drift reasoning toward idiosyncratic patterns such as poor readability and language mixing. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 让 senior/junior 交替共同生成 RLVR rollout，把 handoff compatibility 变成训练目标。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results demonstrate a promising route for RLVR with practical payoffs in multi-model communication and human compatibility. Method=https://arxiv.org/html/2606.28166v1 — §3.1 Preliminaries: tandem training; 5.1 Training dynamics of TRL；Evaluation=https://arxiv.org/html/2606.28166v1 — §4 Results; 4.1 Experimental setup; Appendix B Additional Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Training Qwen3-4B-Instruct on competition math, we find that TRL matches vanilla GRPO on solo reasoning capability while three properties emerge together from the same rollout structure: stronger handoff robustness with the junior, reduced distributional drift from the junior, and a chain-of-thought more legible to the junior. 该结果只保留为局部方法/实验语境；它不新增长期 owner、authority、coexistence 或 fallback 命题。 Counterevidence/limitation=https://arxiv.org/html/2606.28166v1 — §5 Discussion; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28166:start -->
Claim boundary：仅 arXiv:2606.28166v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28166:end -->
<!-- review:SF-2026-ARXIV-2606-28166:end -->

<!-- review:SF-2026-ARXIV-2606-28187:start -->
### 2606.28187 — GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems

**问题、约束与旧路径。** Multi-agent systems (MAS) built on large language models (LLMs) provide a promising framework for solving complex tasks through role specialization and structured interaction. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 multi-agent interaction 建成可反传 attribution graph，以 token-level influence 分配错误责任。 由 AGENT-MULTI-AGENT 持有 interaction graph、attribution 与 commit coordination；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on MultiWOZ and τ-bench show that GBC improves multi-agent performance and outperforms strong single-agent and multi-agent baselines, and higher attribution quality is associated with greater optimization effectiveness. Method=https://arxiv.org/html/2606.28187v1 — §GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems; 2.2 Multi-Agent System; 2.3 Multi-Agent System Optimization；Evaluation=https://arxiv.org/html/2606.28187v1 — §5 Experiment; Setup; Optimization Setup。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28187v1 — §6 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-28187:start -->
Claim boundary：仅 arXiv:2606.28187v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28187:end -->
<!-- review:SF-2026-ARXIV-2606-28187:end -->

<!-- review:SF-2026-ARXIV-2606-28235:start -->
### 2606.28235 — Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software

**问题、约束与旧路径。** Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Yet agents that each pass their own tests still leave repositories that accumulate problems no single contribution accounts for. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。 由 AGENT-PLATFORM 持有 workspace、runtime、acceptance predicate 与 replay；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Method=https://arxiv.org/html/2606.28235v1 — §Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software; II-C Software ecosystems and coordination cost; II-D Emergence and complex adaptive systems；Evaluation=https://arxiv.org/html/2606.28235v1 — §IV-B Level of analysis and why multilevel models; V Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》在 IV-B Level of analysis and why multilevel models; V Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28235v1 — §VI Discussion; VII Threats to Validity; VIII Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28235:start -->
Claim boundary：仅 arXiv:2606.28235v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28235:end -->
<!-- review:SF-2026-ARXIV-2606-28235:end -->

<!-- review:SF-2026-ARXIV-2606-28276:start -->
### 2606.28276 — SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation

**问题、约束与旧路径。** Training and evaluating robot policies in the real world is costly and difficult to scale. We introduce SimFoundry, a modular and automated system for zero-shot real-to-sim scene construction from a video. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 video-to-sim reconstruction、digital cousins、policy training 与 sim-to-real rank validity 绑定。 由 MULTIMODAL-EMBODIED-VLA 持有 scene state、policy evaluation 与 real-world commit；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** When evaluating sim-trained policies zero-shot in the real world, policies trained with object, scene, and task cousins in simulation show average task success rate improvements of 17%, 21%, and 40%, respectively. Method=https://arxiv.org/html/2606.28276v1 — §SimFoundry outperforms state-of-the-art simulation evaluation frameworks and makes fewer assumptions.; 5.2 Sim-to-Real Policy Training; Co-training with sim and real data further improves performance.；Evaluation=https://arxiv.org/html/2606.28276v1 — §SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》在 SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 Reconstruction quality 与 simulator ranking 不证明 contact dynamics 或 safety；rank mismatch 或未知 embodiment 会阻断物理 promotion，并保留 real-data/controller gate。 Counterevidence/limitation=https://arxiv.org/html/2606.28276v1 — §6 Limitations; 7 Conclusion; Appendix C Limitations。

<!-- claim:SF-2026-ARXIV-2606-28276:start -->
Claim boundary：仅 arXiv:2606.28276v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28276:end -->
<!-- review:SF-2026-ARXIV-2606-28276:end -->

<!-- review:SF-2026-ARXIV-2606-28277:start -->
### 2606.28277 — Towards Automating Scientific Review with Google's Paper Assistant Tool

**问题、约束与旧路径。** Artificial intelligence is driving a revolution in scientific discovery, accelerating everything from hypothesis generation to mathematical theorem proving. However, this rapid acceleration is creating a systemic challenge: traditional human peer review cannot scale to match the influx of AI-assisted science. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Pilot deployments of PAT as a pre-submission tool for authors at two major Computer Science conferences -- STOC and ICML -- demonstrate its ability to identify critical errors and suggest substantive improvements to research papers. Method=https://arxiv.org/html/2606.28277v1 — §Design Considerations.；Evaluation=https://arxiv.org/html/2606.28277v1 — §2.1. Case Study: Verification of Retracted Papers in the SPOT Benchmark; 3. PAT Experimental Programs at STOC and ICML; 3.1. Quantitative Author Feedback for PAT Experimental Programs。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** By catching errors early, PAT eases the cognitive burden placed on referees, while preserving their control over the outcomes of the review process. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28277v1 — §5. Conclusion and Future Outlook。

<!-- claim:SF-2026-ARXIV-2606-28277:start -->
Claim boundary：仅 arXiv:2606.28277v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28277:end -->
<!-- review:SF-2026-ARXIV-2606-28277:end -->

<!-- review:SF-2026-ARXIV-2606-28279:start -->
### 2606.28279 — Agentic Hardware Design as Repository-Level Code Evolution

**问题、约束与旧路径。** We present HORIZON, a self-evolving agent framework that treats hardware design as repository-level code evolution. A Markdown harness is compiled into a project pack containing domain knowledge, an executable evaluator, an acceptance predicate, and a git/runtime policy; a hands-free agent loop then evolves an isolated git worktree, using repository operations for state management, tracing, and replay. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。 由 AGENT-WORKFLOW 持有 artifact state、verifier/interlock 与 fallback；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We evaluate our approach on ChipBench, RTLLM, Verilog-Eval, and nine CVDP categories, achieving 100\% benchmark completion across all suites with a fully hands-free agentic loop. Method=https://arxiv.org/html/2606.28279v1 — §Agentic Hardware Design as Repository-Level Code Evolution; Benchmarks for RTL design and verification.; 3 The HORIZON Framework；Evaluation=https://arxiv.org/html/2606.28279v1 — §Benchmarks for RTL design and verification.; 4 Experiments; Setup and protocol.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28279v1 — §4.3 Detailed discussion on test-generation tasks; 5 Discussion and Limitations; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28279:start -->
Claim boundary：仅 arXiv:2606.28279v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28279:end -->
<!-- review:SF-2026-ARXIV-2606-28279:end -->

<!-- review:SF-2026-ARXIV-2606-28322:start -->
### 2606.28322 — PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception

**问题、约束与旧路径。** We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRubrics pairs 1,038 information-dense images with over 10,000 instance-specific rubrics. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Extensive evaluation yields critical insights: (1) The Reliability Gap: models often verify fragmented elements correctly yet fail strict conjunctive constraints, exposing brittleness in dense domains; (2) Open-Closed Stratification: contrary to reasoning trends, we reveal a persistent 8% perception deficit between open-source and proprietary frontiers; and (3) Human-Aligned Rigor: our gated metrics substantially out-align conventional benchmarks, validating that strict perceptual fidelity is the prerequisite for reliable generation. Method=https://arxiv.org/html/2606.28322v1 — §3.1 Design Criteria；Evaluation=https://arxiv.org/html/2606.28322v1 — §PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》在 PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28322v1 — §6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28322:start -->
Claim boundary：仅 arXiv:2606.28322v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28322:end -->
<!-- review:SF-2026-ARXIV-2606-28322:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27406 | Towards Evaluation of Implicit Software World Models in Coding LLMs — In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. |
| SF-2026-ARXIV-2606-27409 | Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement — By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing |
| SF-2026-ARXIV-2606-27416 | Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents — Framework and a public demo project accompany this paper. | Claude Code, Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Tasks run in parallel by living in separate git worktrees on separate branches ( task/<task_id> ). The researcher opens a coding-agent session per task; ARF supplies the worktree and branch conventions, the verifier gates, and the merge discipline that let many sessions run at once without interfering. Up to twelve sessions ran simultaneously on a single 48 GB Mac during the BEA 2026 campaign (Figure 3 ), and no merge conflict reached main . The pattern matches concurrent prior work — EvoSkill ( Alzubi et al., 2026 ) frames each agent program as a git branch; CORAL ( Qu et al., 2026 ) describes “isolated workspac | The campaign comprised 273 tracked tasks (146 experiment runs) across 129 feature sets, run by up to twelve parallel agents orchestrated from a single laptop - with some model training on rented A100s - at approximately \$450 in LLM API spend (\$498 total third-party cost), and structured per-fold provenance let us catch and strip four target-leaking feature sets, correcting an implausible 0.609 RMSE to 0.802. | Framework and a public demo project accompany this paper. |
| SF-2026-ARXIV-2606-27457 | Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving — It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration. | Gemma, Qwen, Qwen3-30B-A3B-Thinking-2507-FP8, Qwen3-4B-Thinking-2507-FP8, Qwen3.5-35B-A3B-FP8 | Not Disclosed | Pareto-superior model (Qwen3.5-35B-A3B-FP8). Figure 2: Routing regions for the AIME 2024 two-model pool. As the inference cost penalty λ \lambda increases, clusters flip from Qwen3-30B-A3B-Thinking-2507-FP8 (Q3-30B) to VibeThinker-1.5B (V) at the indicated crossover points; C1 flips first (smallest Q3-30B advantage) and C2 last (largest). The American Invitational Mathematics Examination dataset provides 921 training queries (AIME 1983–2023) and 30 test queries (AIME 2024), the full fixed competition set for this benchmark. Silhouette analysis selects 3 clusters. The primary model pool consists of VibeThinker-1.5 | Not Disclosed | Not Disclosed | Not Disclosed | Telecommunications is a demanding setting for efficient LLM inference, where domain competence and serving efficiency are both first-order. TeleQnA shows that general-purpose LLMs struggle with standards questions, motivating telecom-specialised models ( Maatouk et al., 2025 ) . The field is shifting from human-in-the-loop co-pilots toward autonomous multi-agent systems owning the full lifecycle, from detection and diagnosis to remediation and validation ( Xiao et al., 2026 ; NVIDIA, 2026 ) . These always-on agents reshape the serving problem; since they act on sensitive operational data, their models must run on | Efficient deployment of large language models (LLMs) in production forces a trade-off between accuracy and cost. | It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration. |
| SF-2026-ARXIV-2606-27472 | Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents — We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. | Claude memory, Gemini, Qwen2.5-3B, gpt-5.4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. |
| SF-2026-ARXIV-2606-27474 | Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks — How should we evaluate generation systems that combine autoregressive (AR) and diffusion decoding? | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | How should we evaluate generation systems that combine autoregressive (AR) and diffusion decoding? |
| SF-2026-ARXIV-2606-27483 | Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning — Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. | DeepSeek, Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. |
| SF-2026-ARXIV-2606-27492 | QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems — This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This paper takes that goal literally. We reframe inter-agent communication topology as a self-improving design skill. A pool of worker agents is frozen. On top of them, an LLM planner acts as an architect: for each task, it generates a temporal communication DAG specifying who sends information to whom, in which round, who receives and merges messages, and who emits the final answer. The planner is conditioned on a memory of design rules distilled from prior runs. Each rule is evidence-conditioned, tied to a structural pattern or executable scaffold, and assigned an action: Preserve , Modify , or Avoid . Learning | In the CF fulltest setting, the best generated graph reduces RMSE from 12.53 for the strongest fixed topology to 7.87 while also reducing messages, model calls, and token cost; Silo-style results show the same direction of improvement over cold and fixed-topology baselines. | This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. |
| SF-2026-ARXIV-2606-27499 | DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection — On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role. | Gemini, Qwen2.5-VL-7B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role. |
| SF-2026-ARXIV-2606-27510 | The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching — Its individual and group-level magnitude and sign signal when causal conclusions are prompt-dependent, and when greedy NIE-based component ranking will miss mechanisms only discoverable through combinatorial search. | GPT-2 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Its individual and group-level magnitude and sign signal when causal conclusions are prompt-dependent, and when greedy NIE-based component ranking will miss mechanisms only discoverable through combinatorial search. |
| SF-2026-ARXIV-2606-27511 | When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems — Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. | DeepSeek-V3, GPT-4.1, LLaMA-3.1-8B, Mistral-7B, Qwen3-8B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. |
| SF-2026-ARXIV-2606-27550 | EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction — Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. | Wang | Not Disclosed | We use Vicuna-7B v 1.3 1.3 ( Chiang et al., 2023 ) as the base LM and ankner/hydra-vicuna-7b-v1.3 ( Ankner et al., 2024 ) as the Hydra verifier, in FP16 on a single NVIDIA A100. All methods share temperature T = 0.7 T{=}0.7 , posterior threshold ϵ = 0.09 \epsilon{=}0.09 , mixing coefficient α = 0.3 \alpha{=}0.3 , max input 1400 1400 tokens, and max generation 256 256 tokens. Each benchmark is timed on 100 100 prompts (seed 123 123 ) drawn from HumanEval-val, GSM8K-val, and ShareGPT (Vicuna unfiltered split). Each run begins with one warm-up generation to amortise JIT and KV-cache allocation; timings exclude this | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | By matching speculation depth to context predictability, EntMTP maximizes expected accepted-token throughput across the full distribution of generated text without sacrificing generation quality. | Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. |
| SF-2026-ARXIV-2606-27558 | Productionized Fairness Measurement Under Privacy Constraints — Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. |
| SF-2026-ARXIV-2606-27567 | On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models — We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). |
| SF-2026-ARXIV-2606-27578 | PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration — On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. | Qwen-2.5 | Not Disclosed | The five-seed Phi-3 replication gives cross-seed mean + 42.15 % {+}42.15\% , within 1.08 1.08 pp of the single-seed reference ( + 43.23 % {+}43.23\% ), with trained-coherence across-seed variance 2.73 2.73 pp 2 (SD 1.65 1.65 pp) versus untrained mean 580.8 580.8 pp 2 . Phi-3 verbosity-only control turns trained-verbosity negative to − 32.62 % {-}32.62\% while preserving untrained-coherence at + 43.18 % {+}43.18\% (Table 2 ). Qwen2.5-7B-Instruct uses Transformer Reinforcement Learning (TRL) 0.12.2 ( von Werra et al., 2020 ) LoRA r = 32 r{=}32 , α = 16 \alpha{=}16 , lr 10 − 4 10^{-4} , bf16, 1,500 1{,}500 steps, ce | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. |
| SF-2026-ARXIV-2606-27580 | Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF — We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. | Qwen2.5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On a tabular Markov decision process (MDP) proof-of-concept, RAC reduces the closed-form policy bias by up to 47.9x at the two-slow-channel configuration, beating wait-for-slow at lower wall-clock cost. | We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. |
| SF-2026-ARXIV-2606-27595 | Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents — Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. |
| SF-2026-ARXIV-2606-27608 | Qwen-Image-2.0-RL Technical Report — We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. | Qwen-Image-2.0, Qwen-Image-2.0-RL, Qwen-Image-Bench | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On-policy distillation (OPD) consolidates heterogeneous capabilities by having students learn on self-generated trajectories under teacher supervision. GKD ( Agarwal et al., 2024 ) established this framework for LLMs, and frontier models have since adopted multi-teacher OPD to avoid the seesaw effect of multi-reward RL. Two concurrent works Flow-OPD ( Fang et al., 2026 ) and DiffusionOPD ( Li et al., 2026b ) extend OPD to flow matching models by showing that the KL divergence between Gaussian transition kernels reduces to a velocity-field MSE loss. Both of these works focus on consolidating single-reward T2I teac | Not Disclosed | We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. |
| SF-2026-ARXIV-2606-27622 | FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks — We further show that this two-level architecture can simultaneously address distribution mismatch in trust estimation and client drift across groups by combining local trust-based aggregation with heterogeneity-aware global optimizers such as FedAdam and SCAFFOLD. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We further show that this two-level architecture can simultaneously address distribution mismatch in trust estimation and client drift across groups by combining local trust-based aggregation with heterogeneity-aware global optimizers such as FedAdam and SCAFFOLD. |
| SF-2026-ARXIV-2606-27632 | The tool use benchmark suite includes API-Bank ( Li et al., 2023b ) , which assesses tool selection and execution in multi-turn dialogues over 73 API tools, and BFCL ( Patil et al., 2024 ) (Berkeley Function Calling Leaderboard), which evaluates function-calling capability across dimensions such as AST accuracy, execution accuracy, live API interactions, multi-turn conversations, and relevance detection. | We evaluate Yuvion-8B and Yuvion-32B alongside representative general-purpose baselines including GPT-5.4, Qwen3-32B, Qwen3.5-27B, Qwen3-Max, and DeepSeek-R1. | Output normalization. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The tool use benchmark suite includes API-Bank ( Li et al., 2023b ) , which assesses tool selection and execution in multi-turn dialogues over 73 API tools, and BFCL ( Patil et al., 2024 ) (Berkeley Function Calling Leaderboard), which evaluates function-calling capability across dimensions such as AST accuracy, execution accuracy, live API interactions, multi-turn conversations, and relevance detection. |
| SF-2026-ARXIV-2606-27634 | As a base for our experiments, we defined our sequential personalization setting following a continual learning setup with a sequence tasks: In order to explore both the continual learning and the stability scenarios, we leverage the TRACE benchmark ( Wang et al., 2023b ) . | Qwen 3.5 0.8B, Llama 3.2 1B Instruct and Gemma 3 1B IT | NVIDIA Titan X (11 GB), CUDA 11.8 | In order to do so, techniques such as quantization, pruning, and distillation have been employed to compress the models to a size that can fit on edge devices. | Training maximum length 512 tokens | Evaluation maximum output 256 tokens | Training batch size 2 with gradient accumulation 8; evaluation batch size 4 | Not Disclosed | Not Disclosed | Exact-match task accuracy plus ACC, BWT, FWT, KL divergence, entropy and margin over three seeds |
| SF-2026-ARXIV-2606-27650 | We evaluate GenWorld through three cases: a full-city weekday baseline, a weekday–weekend behavioral contrast, and a warning-response perturbation. | We use K = 10 K=10 – 30 30 samples per context key with a single teacher model (Gemma 3 27B); ablation of sampling count, temperature, and teacher model choice is needed. | We define a query-conditioned interface in which raw city and persona states are mapped into binned observations, actions are selected from finite candidate sets, outputs are JSON-validated, and execution traces are recorded in machine-readable form. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Against this reference, the 90,744 synthetic workers assigned to workplaces have a mean commute distance of 10.81 km, median of 10.09 km, and 90th percentile of 19.15 km. | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27669 | We conduct experiments on DiscoBench across a set of representative LLMs. | We evaluate Claude-Opus-4.7, GPT-5.4, Gemini-3.1-Pro-Preview, Doubao-Seed-2.0-Pro-High, DeepSeek-V4-Pro, Qwen-3.6-Max, MiniMax-M2.7, GLM-5.1, MiMo-v2.5-Pro, Kimi-K2.6, and Hunyuan-3.0-Preview under the same interactive retrieval framework and checkpoint-level evaluator. | 7 summarizes the total input and output tokens under the Neutral and Guided prompting settings. | Not Disclosed | 7 summarizes the total input and output tokens under the Neutral and Guided prompting settings. | Not Disclosed | Not Disclosed | (2022) focus on mapping single queries to multiple concurrent valid facts. | Not Disclosed | This section provides detailed definitions of the evaluation metrics used in our experiments. |
| SF-2026-ARXIV-2606-27679 | Our study covers a wide range of recently proposed feature representations, spanning latent embeddings, output probabilities, attention patterns, and their combinations ( Azaria and Mitchell, 2023 ; Chuang et al., 2024 ; He et al., 2024 ; Huang et al., 2025b ; Shelmanov et al., 2025 ) , evaluated with different probe architectures, supervision sizes, prompting strategies, and automated correctness labels. | We further study benchmark-to-benchmark transfer and a deployment-oriented setting in w We evaluate on seven datasets spanning three tasks: For the main experiment, we evaluate with five popular LLMs across three model families: Llama-3.1-8B ( Grattafiori et al., 2024 ) , Qwen-3-4B, Qwen-3-8B ( Yang et al., 2025 ) , Qwen-3.5-9B ( Qwen Team, 2026 ) , Gemma-3-12B ( Kamath et al., 2025 ) . | Our study covers a wide range of recently proposed feature representations, spanning latent embeddings, output probabilities, attention patterns, and their combinations ( Azaria and Mitchell, 2023 ; Chuang et al., 2024 ; He et al., 2024 ; Huang et al., 2025b ; Shelmanov et al., 2025 ) , evaluated with different probe architectures, supervision sizes, prompting strategies, and automated correctness labels. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27681 | A large body of work has focused on building better dynamics models ( Hafner et al., 2019a ; Hafner et al., 2019b ; Hafner et al., 2023 ; Schritt Our experiments evaluate whether enforcing strict mediation via fGRPO preserves predictive accuracy (Prop 1 ), yields more informative latent states (Prop 2 ), and improves rollout stability (Prop 3 ). | We additionally apply a small set of determ We experiment with three pretrained instruction-tuned language models: Qwen2.5-0.5B-Instruct (0.5B parameters), Qwen3-4B-Instruct-2507 (4B parameters) and Qwen3-32B (32B parameters). | Each instance is equipped with 8 NVIDIA A100-SXM4 GPUs (80GB memory each), for a total of 640GB GPU memory per node. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27683 | We evaluate CBD on benchmark unlearning datasets against white-box and gray-box baselines, showing an improved unlearning-utility trade-off under the API-only black-box setting. | We use the ToFU-released Llama-2-7B-Chat model 3 3 3 https://hu We first review the two mainstream unlearning paradigms and clarify why the API-only setting requires a different solution. | Second, auxiliary-model-bas layer input and output dimensions where the forget loss ℒ f wb \mathcal{L}_{f}^{\mathrm{wb}} drives the model away from the forget data, the retain loss ℒ r wb \mathcal{L}_{r}^{\mathrm{wb}} preserves behavior on retained data, and λ \lambda trades off the two. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27704 | To address these challenges, we propose AdvScan, a runtime power analysis-based methodology for AE detection that operates in a black-box We evaluate AdvScan on two MCU platforms, an STM32F303RC (Arm Cortex-M4) and an STM32L562RE (Arm Cortex-M33), running three TinyML models in the presence of AEs generated by Fast Gradient Sign Method (FGSM) [ 4 ] , Projected Gradient Descent (PGD) [ 5 ] , and the Carlini–Wagner (C&W) attack [ 6 ] under L 0 L_{0} , L 2 L_{2} , and L ∞ L_{\infty} norms. | Not Disclosed | IV-C 1 Gated-output mode An adversarial example (AE) is a maliciously crafted input designed to make NN models misclassify. | TinyML models commonly use aggressive quantization and pruning to fit within limited hardware constraints, making them more vulnerable to adversarial attacks than traditional neural networks (NNs) [ 45 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | However, existing AE detection methods either require white-box model access, which is often unavailable in licensed black-box deployments, or rely on input pre-processing stages that add non-trivial latency and resource overhead, often exceeding what mission-critical applications can afford on their inference path. |
| SF-2026-ARXIV-2606-27709 | Our experiments reveal that fine-tuning on empathetic dialogues whose user turns reflect low Agreeableness , a Big Five trait associated with skepticism, directness, and resistance to social pressure ( Costa and McCrae, 1992 ; Jensen-Campbell and Graziano, 2001 ) , paired with warm, de-escalating assistant responses, outperforms both generic empathetic data and warmth-rewritten baselines on adversarial safety measures. | We conducted three main experiments across four models: SmolLM3-3B , Llama-3.1-8B , Qwen2.5-7B-Instruct , and Mistral-7B-Instruct-v0.3 , varying only dataset composition. | 1 NVIDIA L20 GPU (48 GB VRAM) | 4-bit quantization | Maximum sequence length 1024 tokens | Not Disclosed | Batch size 8; gradient accumulation 2 | Not Disclosed | Not Disclosed | (2026) extend this to supervised fine-tuning: warm assistant responses increase sycophancy by eleven percentage points and degrade factual accuracy, with the data’s warmth identified as the causal driver. |
| SF-2026-ARXIV-2606-27732 | We evaluate R2LM through a controlled three-way comparison against the bidirectional and causal dLLM endpoints under a matched 60 60 B-token continued-pretraining protocol on Qwen3- 1.7 1.7 B. | We evaluate R2LM through a controlled three-way comparison against the bidirectional and causal dLLM endpoints under a matched 60 60 B-token continued-pretraining protocol on Qwen3- 1.7 1.7 B. | 32 NVIDIA H100 GPUs (4 nodes × 8 GPUs) | bfloat16 | Sequence length 4096 tokens | Not Disclosed | Per-device batch size 8; no gradient accumulation | Not Disclosed | Not Disclosed | However, such promising frameworks face a fundamental architectural design dilemma: ❶ Adopting bidirectional attention achieves strong generation quality by allowing each position to access the full context, but is inherently incompatible with KV caching, limiting inference throughput in batch-serving scenarios; ❷ Conversely, causal attention enables efficient cached inference but loses all right-side context, substantially degrading generation quality. |
| SF-2026-ARXIV-2606-27739 | We conduct a series of experiments to answer four research questions: Our experiments focus on math reasoning, where the correctness of intermediate steps and final answers is relatively well-defined and easy to verify. | We train PRMs on the Math-Shepherd dataset, using Qwen2.5-Math-7B-Instruct as the backbone. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For all methods except PQM, we use a global batch size (GPU count × gradient accumulation steps × per-GPU batch size) of 384 on Qwen2.5-Math-7B-Instruct and Llama3.2-3B-Instruct backbones, and 512 on Qwen3-4B. | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27743 | We design our experiments to rigorously validate two central hypotheses: (1) Our unified optimization framework with dynamic gating, achieves a superior performance-efficiency trade-off compared to static or heuristic methods. | We evaluate on two representative open-source backbones, Llama-3-8B ( Dubey et al., 2024 ) and Qwen-3-4B ( Yang et al., 2024a ) , to test whether the proposed gating-and-adaptation framework transfers across model families. | Not Disclosed | Not Disclosed | Complementary approaches learn to skip computation inside the backbone: Mixture-of-Depths routes a subset of tokens through each layer under a fixed token budget ( Raposo et al., 2024a ) , while layer-skipping To make the transition behavior explicit, we assume a structured generation format <think> ⋯ \cdots </think> <answer> ⋯ \cdots </answer> . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | w/o head gating (layer-only) underperforms the joint strategy at similar latency constraints. |
| SF-2026-ARXIV-2606-27757 | In this section, we conduct comparative experiments to evaluate the performance. | In addition, we construct a plan recogn To validate the superior planning capabilities of our framework, we conducted comparative experiments with three mainstream LLMs: GPT-4o, Claude-3-5, and DeepSeek-R1, using standard inference parameters (temperature = 0.1) for consistency. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate performance using planning coverage (success rate), defined as the proportion of problems solved relative to the total number of problems. |
| SF-2026-ARXIV-2606-27780 | We evaluate the framework on a seven-topology synthetic benchmark with existing GWM baselines, including GCN Kipf and Welling (2017) , MPNN Gilmer et al. | Not Disclosed | In an agent system, node features can encode agent status, tool outputs, skill availability, task progress, or failure signals. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27791 | We evaluate NLL-guided layer selection on Qwen3-4B-Thinking-2507 3 3 3 https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507 ( Yang et al., 2025 ) , a 36-layer model, using the LongMemEval benchmark ( Wu et al., 2025 ) . | We evaluate NLL-guided layer selection on Qwen3-4B-Thinking-2507 3 3 3 https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507 ( Yang et al., 2025 ) , a 36-layer model, using the LongMemEval benchmark ( Wu et al., 2025 ) . | We propose NLL-guided layer selection , a principled approach that directly measures what we care about: how much does each layer’s output quality degrade when we restrict its attention? | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27797 | Teacher-student generative knowledge distillation with asymmetric partition and communication plans | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | End-to-end GKD training time and topology/partition ablations |
| SF-2026-ARXIV-2606-27806 | TaskGraph, ToolChain, ResourceAlloc and RepairFlow; 100 test tasks per benchmark (60 in-distribution, 40 out-of-distribution) | Because production LLM rollouts are expensive, the agent and hybrid behaviours are reproduced by a behavioural simulator calibrated against measured GPT-4o-mini TaskGraph runs (the real-API validati We train a small parametric world model F θ : ( G t , a ) ↦ ( p ^ valid , Δ ​ G ^ , r ^ , p ^ done , ρ ^ , U ^ , J ^ K ) F_{\theta}:(G_{t},a)\mapsto(\hat{p}_{\text{valid}},\widehat{\Delta G},\hat{r},\hat{p}_{\text{done}},\hat{\rho},\hat{U},\hat{J}_{K}) on oracle transitions 𝒟 = { ( G t , a t , G t + 1 , r t , d t , m t ) } \mathcal{D}=\{(G_{t},a_{t},G_{t+1},r_{t},d_{t},m_{t})\} with the multi-task loss We use four graph-structured world-model planning benchmarks—TaskGraph … | Structured output and grounding. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Eleven agent-only, parametric-only and hybrid planners evaluated on plan validity/reward and hallucinated state transitions |
| SF-2026-ARXIV-2606-27814 | We evaluate ATOD on three long-horizon agent benchmarks: ALFWorld, WebShop, and Search-QA. | Qwen3-0.6B, Qwen3-1.7B and Qwen3-4B student models | 8 GPUs on one node | Not Disclosed | Not Disclosed | Not Disclosed | Train batch sizes ALFWorld/WebShop/Search-QA = 16/128/16; validation = 128/512/128 | Not Disclosed | Not Disclosed | However, strong agentic behavior is usually concentrated in large models, whose inference cost and deployment overhead are undesirable in latency-, privacy-, and resource-sensitive settings. |
| SF-2026-ARXIV-2606-27826 | As shown in Figure 1 , we evaluate three cue conditions of increasing explicitness to diagnose why models fail and find that models can often comply with the relevant norm when the constraint is made explicit but fail to infer it from the scene alone. | We used GPT-4o to analyze the failure causes in the action sequences generated by the models. | 5.2 Output Parsing and Error Labels E Output Parsing and Error Labels MLLM are increasingly used as embodied planners in first-person environments, where they must interpret visual observations, follow natural-language instructions, and output executable action plans ( Liu et al., 2023 ; Li et al., 2023b ; Dai et al., 2023 ; Bai et al., 2025 ; Zitkovich et al., 2023 ; Wang et al., 2023 ) . | Not Disclosed | Not Disclosed | Not Disclosed | We use 60 training epochs, a batch size of 4, and a learning rate of 1 ​ e − 4 1e^{-4} . | Not Disclosed | Not Disclosed | Each sequence is scored according to three binary rewards: We evaluate whether MLLM -based embodied planners treat social norms as implicit constraints when producing high-level action plans for ordinary embodied tasks. |
| SF-2026-ARXIV-2606-27841 | As our experiments in Section 4 show, adding new tasks to the database weakens the estimation performance of the final model. | Not Disclosed | NVIDIA H100, A100 and TITAN X measurements | Although pruning is accounted for in the model due to its impact on layer shapes, other acceleration techniques such as quantization or sparsification have not been explicitly included in the methodology. | Not Disclosed | Not Disclosed | LLM zero-shot energy evaluation uses batch size 1 | Not Disclosed | Not Disclosed | (2024) have investigated the internal mechanisms of energy measurement provided by NVIDIA-smi and found that the tool has an overall measurement error of 5%. |
| SF-2026-ARXIV-2606-27866 | We conducted comprehensive experiments on Mixtral-8x7B, Phi-3.5-MoE, and Qwen2-57B-A14B. | We conducted comprehensive experiments on Mixtral-8x7B, Phi-3.5-MoE, and Qwen2-57B-A14B. | During action training, all parameters are kept and we only use prefix mask m ⁡ ( r ) m(r) to simulate pruned expert outputs, but during deployment, parameters masked by learned actions can be dropped or excluded from forward calculations to reduce cost. | Chen Examining post-training quantization for mixture-of-experts: a benchmark . | Not Disclosed | Not Disclosed | Not Disclosed | We use the SGLang engine ( Zheng et al., 2024 ) on a single H200 GPU under a synthetic workload with 4096 prompt requests, input length = 64 =64 , output length = 256 =256 1 1 1 SGLang is a serving-oriented runtime which is designed for high-throughput structured LLM execution, and this setup is intended to approximate a realistic serving regime with substantial concurrent traffic, rather than a single-request latency test. | Not Disclosed | We further show that the shared weights recovered from single mid-budget fine-tune strategy transfers well to unseen higher and lower budgets, and that the resulting subnet family delivers real throughput gains and more flexible interfaces in deployment, especially when coupled with our explor Task Accuracy Results Analysis. |
| SF-2026-ARXIV-2606-27906 | FastVLM-0.5B FP16 CPU versus INT8 NPU on 500 COCO val2017 images and 200 VQAv2 questions | We use FastVLM-0.5B ( 1 ) as the primary model: a 0.5B-parameter VLM built on Qwen-0.5B ( 8 ) with a FastViT encoder that applies aggressive token compression for mobile execution. | Snapdragon mobile SoC CPU and Qualcomm NPU paths | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | COCO CIDEr and VQAv2 lowercase-normalized exact-match accuracy |
| SF-2026-ARXIV-2606-27934 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Throughput divergence. |
| SF-2026-ARXIV-2606-27936 | We evaluate the pipeline on a spatio-temporal dataset containing simulated location points anchored at and around true home and work addresses, focusing on a high-risk disclosure scenario. | Not Disclosed | Each stage produces structured output consumed by the next; the orchestrator enforces quality gates between transitions and halts the run early when evidence falls below a sufficiency threshold. | Zettlemoyer (2023) QLoRA: efficient finetuning of quantized LLMs . | Not Disclosed | Not Disclosed | Not Disclosed | A bash script parallelises one session per device CSV file at a concurrenc Across the 43 evaluation runs, each attempt cost on average $2.24 in API charges at list prices, produced on average 58.5K output tokens (range: 39.5K–78.9K), and took on average 17 minutes of unattended computation (range: 11.7–28.5 minutes). | Not Disclosed | Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified Re-identifying individuals at scale from spatio-temporal mobility traces has historically required sophisticated technical knowledge, including API configuration, data preprocessing, and familiarity with OSINT techniques. |
| SF-2026-ARXIV-2606-27944 | We evaluate Phone-use Agents built on four commercial models (Claude-Sonnet-4.5, GPT-5.4-medium, Gemini-3.1-Pro, and Seed-2.0-Pro) and five open-source models. | We evaluate Phone-use Agents built on four commercial models (Claude-Sonnet-4.5, GPT-5.4-medium, Gemini-3.1-Pro, and Seed-2.0-Pro) and five open-source models. | Phone-use Agents perceive the phone screen, interpret natural-language instructions, and output directly executable UI actions (tapping, typing, swiping, etc.) [ 24 , 9 , 12 , 35 , 33 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For each level, we report the success rate (SR) , defined as the fraction of samples for which the misuse task is completed, and the refusal rate (RR) , defined as the fraction of samples for which the model identifies pote Evaluation Setups . |
| SF-2026-ARXIV-2606-27962 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27976 | The client encodes the query, v q = E ⁡ ( q text ) ∈ ℝ d v_{q}=E(q_{\mathrm{text}})\in\mathbb{R}^{d} , and forms the rotated query q ′ = R ​ V k ⊤ ​ ( v q − μ ) ∈ ℝ k q^{\prime}=R\,V_{k}^{\top}(v_{q}-\mu)\in\mathbb{R}^{k} ; using the public PQ artefact and q ~ = q ′ \tilde{q}=q^{\prime} it then runs an asymmetric PQ-distance search locally and keeps the top- K cands K_{\mathrm{cands}} candidate IDs I cand I_{\mathrm{cand}} —a short-list small enough ( K cands = 40 K_{\mathrm{cands}}=40 in our experiments) that the CKKS reranking still fits the latency budget. | Not Disclosed | Five reported cells CPU-encoded; e5-large/NFCorpus omitted after exceeding CPU budget | ✓ \checkmark provided, × \times not addressed, ∼ \sim partial/approximate; “exact rerank” is full-dimensional scoring with no quantization/noise loss, “coarse-only leak” means the accessible channel exposes only coarse/topic structure. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | End-to-end query latency < 1 <1 s at 10 6 10^{6} docs The pipeline of Figure 1 processes a query in stages, of which only the last leaves the client. | The client encodes the query, v q = E ⁡ ( q text ) ∈ ℝ d v_{q}=E(q_{\mathrm{text}})\in\mathbb{R}^{d} , and forms the rotated query q ′ = R ​ V k ⊤ ​ ( v q − μ ) ∈ ℝ k q^{\prime}=R\,V_{k}^{\top}(v_{q}-\mu)\in\mathbb{R}^{k} ; using the public PQ artefact and q ~ = q ′ \tilde{q}=q^{\prime} it then runs an asymmetric PQ-distance search locally and keeps the top- K cands K_{\mathrm{cands}} candidate IDs I cand I_{\mathrm{cand}} —a short-list small enough ( K cands = 40 K_{\mathrm{cands}}=40 in our experiments) that the CKKS reranking still fits the latency budget. |
| SF-2026-ARXIV-2606-27997 | Similarly we use for the pair 𝐑 𝒮 , 𝐑 𝒟 \mathbf{R}_{\mathcal{S}},\mathbf{R}_{\mathcal{D}} Spearman’s Rank Correlation ρ ⁡ ( 𝐑 𝒮 , 𝐑 𝒟 ) \rho(\mathbf{R}_{\mathcal{S}},\mathbf{R}_{\mathcal{D}}) , Kendall’s Rank Correlation τ ⁡ ( 𝐑 𝒮 , 𝐑 𝒟 ) \tau(\mathbf{R}_{\mathcal{S}},\mathbf{R}_{\mathcal{D}}) , Normalized Discounted Cumulative Gain (NDCG@K) with K = 5 K=5 , and Mean Reciprocal Rank (MRR) used in our experiments. | Not Disclosed | Not Disclosed | Not Disclosed | These descriptions are encoded with bert-base-uncased : we tokenize each description with maximum length 256, mean-pool final-layer token embeddings over non-padding tokens, and ℓ 2 \ell_{2} -normalize the resulting 768-dimensional vector. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For these four metrics, larger values indicate better preservation of the ranking. |
| SF-2026-ARXIV-2606-28011 | Not Disclosed | Not Disclosed | We propose an agentic Large Language Model (LLM) framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28013 | Statement autoformalization stratified by Lean type-check and semantic-equivalence judgment | DeepSeek V4-Pro on ProofNet# for the full four-method dual-judging cell | We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success ( TS ), type-only ( TO ), semantic-only ( SO ), or both fail ( BF ). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Four-cell TS/TO/SO/BF signal-coverage matrix under dual semantic judging |
| SF-2026-ARXIV-2606-28037 | We evaluate GBV-PD along four dimensions: We evaluate two tasks: image classification (IC) on the CIFAR-100 ( Krizhevsky, 2009 ) and behavior cloning (BC) on the Udacity Jungle dataset ( Su, 2023 ) , released as part of Udacity’s behavior cloning project ( Udacity, 2016 ) . | Not Disclosed | Black-box testing ( Zohdinasab et al., 2023 ) , which relies only on inputs and outputs, provides limited insight into how the model has changed internally. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 3.2.3 Projection Error of Delta Loss For regression tasks, let e θ ​ ( x , y ) e_{\theta}(x,y) be a task-specific error function and τ task > 0 \tau_{\mathrm{task}}>0 a threshold for meaningful change: These definitions capture meaningful behavior changes of the model on a test case rather than small numerical fluctuations. |
| SF-2026-ARXIV-2606-28050 | We evaluate two models as ℒ \mathcal{L} : Llama-3.1-8B-Instruct ( Dubey and others, 2024 ) , a capable open-source model at modest scale, and GPT-4o-mini , a stronger proprietary model. | We evaluate two models as ℒ \mathcal{L} : Llama-3.1-8B-Instruct ( Dubey and others, 2024 ) , a capable open-source model at modest scale, and GPT-4o-mini , a stronger proprietary model. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confound of open-domain comparisons. |
| SF-2026-ARXIV-2606-28061 | Not Disclosed | Not Disclosed | 4.8 Evaluation Outputs This case design moves evaluation beyond final-output correctness and makes it possible to inspect how an agent moves information during execution. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Runtime monitoring and adversarial RAG evaluation further study how agent behavior or retrieved contexts can be scored or stre To make evaluation reproducible and diagnosable, ToolPrivacyBench separates policy definition, runtime evidence capture, disclosure identification, authorization judgment, and metric computation into independent modules. |
| SF-2026-ARXIV-2606-28070 | To assess the efficacy of 𝖲 2 ​ 𝖣 \mathsf{S}^{2}\mathsf{D} , we conducted random sampling of items across diverse categories to evaluate their knowledge recognition results. | Not Disclosed | For example, if “CPU model” already exists, “central processing unit model” is rejected. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A single platform must serve all of these highly concurrent, domain-specific demands at once, efficiently building on what the scenarios share while supporting what makes L1 cross-chunk asynchronous pipeline. | Not Disclosed | While each of the aforementioned strategies yields significant throughput gains, they are difficult to stack efficiently in practice. |
| SF-2026-ARXIV-2606-28116 | Low-precision attention, large-learning-rate and combined-fault training-instability injections | Not Disclosed | Not Disclosed | For example, flash attention (FA) exhibits substantially larger BF16 numeric deviation than baseline attention in isolated forward passes ( Golden et al., 2024 ) , and low-precision FA can corrupt weight updates through biased rounding errors and gradually derail training dynamics ( Qiu and Yao, 2026 ) . | Not Disclosed | Not Disclosed | To make the LR–GBS coupling explicit, for global batch size B B write the empirical reinforcement coefficient as The stable-winner feedback loop derived in Section 4 predicts that larger learning rates and smaller global batch sizes amplify router entropy collapse. | Not Disclosed | Not Disclosed | Pre-loss detection lead time and distinct attention/router failure signatures |
| SF-2026-ARXIV-2606-28128 | Not Disclosed | Not Disclosed | All three auxiliary models are frozen and used only to extract physics targets; they are run on the ground-truth clip on the fly during each training step, and the tracker/depth outputs are shared between the two physics losses. | Not Disclosed | Not Disclosed | Not Disclosed | For the two Wan backbones, input videos are resized to 640 × 480 640\times 480 with a maximum length of 81 frames, and both are trained for 20K steps with a global batch size of 128 using the AdamW optimizer with a learning rate of 1 × 10 − 5 1\times 10^{-5} ; for Wan2.2-I2V-A14B, we initialize from its high-noise expert and adapt it to later denoising stages during training. | Not Disclosed | Not Disclosed | In contact-rich manipulation, physical violations often appear as local dynamic errors, such as discontinuous gripper trajectories, object penetration, or anti-gravity motion, and as global relational errors, such as a pushed object remaining static or a grasped object drifting away. |
| SF-2026-ARXIV-2606-28153 | All source datasets are publicly released benchmarks intended for safety research; We evaluate on 10 datasets from the safety-eval framework ( Han et al., 2024 ; Jiang et al., 2024 ) : general intent moderation (WildGuardTest ( Han et al., 2024 ) , ToxicChat ( Lin et al., 2023 ) , OpenAI Moderation ( Markov et al., 2022 ) , Aegis ( Ghosh et al., 2024 ; Ghosh et al., 2025 ) , SimpleSafetyTests ( Vidgen et al., 2024 ) , HarmBench-Vanilla ( Mazeika et al., 2024 ) ) and adversarial-attack detection (WildJailbreak ( Jiang et al., 2024 ) , SALAD-Bench ( Li et al., 2024a ) , HarmBench-Adversarial). | We conduct our analysis on Llama-3-8B-Instruct and Llama-2-7B-Chat. | (2025) , we trace information flow by projecting the mid-layer refusal direction, under a linear framework, into the output space of attention heads across layers, thereby quantifying each head’s contribution to the refusal signal. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28166 | We evaluate on AMC 23–25, AIME 24–26, and Minerva Math ( Lewkowycz et al., 2022 ) , and report pass@ k k via an unbiased estimator following Chen et al. | We fine-tune Qwen3-4B-Instruct-2507 ( Yang et al., 2025 ) on DeepScaleR ( Tan et al., 2025 ) with a binary correctness reward on the boxed final answer. | An operational definition of compatibility, or intelligibility, is handoff robustness ( West et al., 2026 ) : a model’s output is intelligible to another agent if that agent can continue it without derailing the trajectory. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We estimate bootstrap standard errors by resampling evaluation problems, reported as ± \pm values in tables and as shaded bands in figures. |
| SF-2026-ARXIV-2606-28187 | We evaluate our approach on both task-oriented dialogue (MultiWOZ ( Ye et al., 2022 ) ) and interactive tool-use environments ( τ \tau -bench ( Yao et al., 2025 ) ), demonstrating that GBC significantly improves multi-agent performance across multiple metrics. | Backbone models are Llama-3.3-70B-It and Qwen-3-32B. | In multi-agent workflows, errors in the final output often originate from specific agents or interaction steps, yet existing methods typically rely on coarse-grained signals (e.g., overall task success or reward) to guide optimization ( Khattab et al., 2024 ; Xu et al., 2025 ; Yuksekgonul et al., 2024 ; Zhuge et al., 2024 ; Luo et al., 2025 ) . | For local model serving, we enable FP8 quantization whenever supported by the target model and serving backend. | Not Disclosed | Not Disclosed | Not Disclosed | We adopt a manager–worker architecture (Figure 2 ). | The table shows the inform score, success score, joint goal accuracy (JGA), slot recall, slot precision, and slot F1 score. | Not Disclosed |
| SF-2026-ARXIV-2606-28235 | Not Disclosed | The five agents in AIDev are OpenAI Codex, Devin, GitHub Copilot, Cursor, and Claude Code, and every row is labelled with which one wrote it. | What rules out the obvious alternative, that this traffic is merely an agent acting on its own output, is the composition of the reviewing and commenting accounts. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across more than 930,000 agent-authored pull requests, we measure how much of the variation in fr This paper locates the problem in the ecosystem, and measures it. | Not Disclosed | That understanding is a team-level asset that can be lost: projects suffer disproportionate knowledge loss when contributors leave [ 10 ] , and developers who lean on AI assistance score lower on later comprehension of the same code [ 11 ] . |
| SF-2026-ARXIV-2606-28276 | In our experiments, object cousins improve robustness to unseen object instances, scene cousins improve generalization to novel layouts, and task cousins improve both zero-shot and few-shot downstream task performance. | Not Disclosed | SimFoundry extracts per-object relevant information (segmentation masks, depth, etc.), generates 3D visual meshes via 2D-to-3D generation models, and compiles the final output scene by annotating relevant physical parameters and sanity checking the overall scene configuration in a physics simulator. | Not Disclosed | Not Disclosed | Not Disclosed | Each policy is trained with a batch size of 256, a learning rate of 1 ​ e − 5 1e-5 , and for 10k gradient steps. | Not Disclosed | Not Disclosed | The policy success rate with initial subtasks completed in sim is compared with the full end-to-end task success rate in the real world which we found improved evaluation correlations In this sub-section, we provide the scoring rubric for each task, along with the language instruction provided to the VLAs. |
| SF-2026-ARXIV-2606-28277 | Towards this end, we evaluate the real-world utility of PAT on organic, human-authored errors, using the SPOT benchmark ( Son et al., 2025 ) , which compiles manuscripts containing verified mistakes that led to subsequent errata or retractions. | Not Disclosed | However, the Scientific Method requires rigorously validating these outputs, not just generating them. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | One of the primary aims of PAT is to find technical errors in full-length scientific manuscripts. |
| SF-2026-ARXIV-2606-28279 | We evaluate our approach on ChipBench, RTLLM, Verilog-Eval, and nine CVDP categories, achieving 100% benchmark completion across all suites with a | Model: we use GPT-5.3 as the agent backbone for all experiments, fixed throughout; Benchmarks: ChipBench, RTLLM-2.0, and Verilog-Eval, together with all CVDP code- and verification-generation categories (CID 002 to 016) spanning completion, specification-to-RTL, modification, reuse, linting/QoR, and stimulus, checker, and assertion generation as well as debugging. | RTL generation differs from ordinary code completion because the output defines hardware that must satisfy temporal and bit-accurate behavior. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | AutoChip drives a generate-compile-simulate feedback loop ( Thakur et al., 2023 ) ; RTLFixer repairs syntax errors with retrieval-augmented, ReAct-style debugging ( Tsai et al., 2024 ) ; VerilogCoder plans with a task-and-circuit-relation graph and traces waveforms via an AST-based tool to localize functional bugs ( Ho et al., 2025 ) ; MAGE decomposes a design across cooperating agents with high-temperature sampling and checkpoint-based debugging ( Zhao et al., 2025 ) ; and ACE-RTL pairs an RTL-specialized generator with a frontier-model reflector and coordinator that evolves the prompting con CVDP also distinguishes non-agentic and agentic settings. |
| SF-2026-ARXIV-2606-28322 | We evaluate a diverse suite of 25 models, spanning proprietary frontier models (e.g., Gemini-3-Pro ( Team, 2025 ) , Gemini-3.5-Flash ( Gemini Team, Google DeepMind, 2026 ) , GPT-5.4 ( OpenAI, 2026b ) , GPT-4o ( OpenAI, 2024 ) , Seed-2.0 ( ByteDance-Seed, 2026c ) , Seed-1.8 ( ByteDance-Seed, 2026b ) , Seed-1.6 ( ByteDance-Seed, 2026a ) , GLM-5V-Turbo ( Hong et al., 2026 ) , Qwen3.5-Plus ( Team, 2026a ) ) and leading open-weights models (e.g.,Qwen3.5-397B ( Team, 2026a ) , Qwen3-VL ( Bai et al., 2025a ) , Qwen2.5-VL ( Bai et al., 2025b ) ,Step3-VL-10B ( Huang et al., 2026 ) , Step-3.7-Flash ( StepFun Team, 2026 ) , MiniMax-M3 ( Lai et al., 2026 ) , MiMo-V2.5 ( Team, 2026b … | We evaluate a diverse suite of 25 models, spanning proprietary frontier models (e.g., Gemini-3-Pro ( Team, 2025 ) , Gemini-3.5-Flash ( Gemini Team, Google DeepMind, 2026 ) , GPT-5.4 ( OpenAI, 2026b ) , GPT-4o ( OpenAI, 2024 ) , Seed-2.0 ( ByteDance-Seed, 2026c ) , Seed-1.8 ( ByteDance-Seed, 2026b ) , Seed-1.6 ( ByteDance-Seed, 2026a ) , GLM-5V-Turbo ( Hong et al., 2026 ) , Qwen3.5-Plus ( Team, 2026a ) ) and leading open-weights models (e.g.,Qwen3.5-397B ( Team, 2026a ) , Qwen3-VL ( Bai et al., 2025a ) , Qwen2.5-VL ( Bai et al., 2025b ) ,Step3-VL-10B ( Huang et al., 2026 ) , Step-3.7-Flash ( StepFun Team, 2026 ) , MiniMax-M3 ( Lai et al., 2026 ) , MiMo-V2.5 ( Team, 2026b … | By analyzing the discrepancies between these actual outputs 𝒫 \mathcal{P} and the reference C g ​ o ​ l ​ d C_{gold} , the rubric proposer identifies frequent hallucinations and subtle misinterpretations. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27406 | score_7_9; potential_books_delta | not_selected | — | — | Towards Evaluation of Implicit Software World Models in Coding LLMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27406 |
| SF-2026-ARXIV-2606-27409 | score_7_9; potential_books_delta | not_selected | — | — | Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27409 |
| SF-2026-ARXIV-2606-27416 | score_7_9; potential_books_delta | not_selected | — | — | Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27416 |
| SF-2026-ARXIV-2606-27457 | score_7_9; potential_books_delta | not_selected | — | — | Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GATEWAY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27457 |
| SF-2026-ARXIV-2606-27472 | score_7_9; potential_books_delta | not_selected | — | — | Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27472 |
| SF-2026-ARXIV-2606-27474 | score_7_9; potential_books_delta | not_selected | — | — | Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27474 |
| SF-2026-ARXIV-2606-27483 | score_7_9; potential_books_delta | not_selected | — | — | Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27483 |
| SF-2026-ARXIV-2606-27492 | score_7_9; potential_books_delta | not_selected | — | — | QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27492 |
| SF-2026-ARXIV-2606-27499 | score_7_9; potential_books_delta | not_selected | — | — | DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27499 |
| SF-2026-ARXIV-2606-27510 | score_7_9; potential_books_delta | not_selected | — | — | The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27510 |
| SF-2026-ARXIV-2606-27511 | score_7_9; potential_books_delta | not_selected | — | — | When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27511 |
| SF-2026-ARXIV-2606-27550 | score_7_9; potential_books_delta | not_selected | — | — | EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27550 |
| SF-2026-ARXIV-2606-27558 | score_7_9; potential_books_delta | not_selected | — | — | Productionized Fairness Measurement Under Privacy Constraints remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27558 |
| SF-2026-ARXIV-2606-27567 | score_7_9; potential_books_delta | not_selected | — | — | On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27567 |
| SF-2026-ARXIV-2606-27578 | score_7_9; potential_books_delta | not_selected | — | — | PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27578 |
| SF-2026-ARXIV-2606-27580 | score_7_9; potential_books_delta | not_selected | — | — | Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27580 |
| SF-2026-ARXIV-2606-27595 | score_7_9; potential_books_delta | not_selected | — | — | Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27595 |
| SF-2026-ARXIV-2606-27608 | score_7_9; potential_books_delta | not_selected | — | — | Qwen-Image-2.0-RL Technical Report remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27608 |
| SF-2026-ARXIV-2606-27622 | score_7_9; potential_books_delta | not_selected | — | — | FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27622 |
| SF-2026-ARXIV-2606-27632 | score_7_9; potential_books_delta | not_selected | — | — | Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27632 |
| SF-2026-ARXIV-2606-27634 | potential_books_delta | not_selected | — | — | Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27634 |
| SF-2026-ARXIV-2606-27650 | potential_books_delta | not_selected | — | — | GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies remains evidence-complete after canonical owner transfer with V2 score 6 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27650 |
| SF-2026-ARXIV-2606-27669 | score_7_9; potential_books_delta | not_selected | — | — | When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27669 |
| SF-2026-ARXIV-2606-27679 | potential_books_delta | not_selected | — | — | From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27679 |
| SF-2026-ARXIV-2606-27681 | score_7_9; potential_books_delta | selected | DA-20260627-STRICT-MEDIATED-WORLD-STATE | — | 该 family 直接改变跨层 state/control boundary：用 strict mediation 让 textual belief state 成为唯一可测试的预测状态，阻断 history bypass。 exact-v1 proof=Experiments on TextWorld and ScienceWorld show preserved one-step prediction accuracy alongside up to 57\% gains in representation quality and 98\% improvements in rollout performance, increasing with task complexity and horizon.；non-proof=We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection. | analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE |
| SF-2026-ARXIV-2606-27683 | score_7_9; potential_books_delta | not_selected | — | — | CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27683 |
| SF-2026-ARXIV-2606-27704 | score_7_9; potential_books_delta | not_selected | — | — | AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27704 |
| SF-2026-ARXIV-2606-27709 | potential_books_delta | not_selected | — | — | Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27709 |
| SF-2026-ARXIV-2606-27732 | score_7_9; potential_books_delta | not_selected | — | — | Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-GENERATIVE-PARADIGMS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27732 |
| SF-2026-ARXIV-2606-27739 | potential_books_delta | not_selected | — | — | The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27739 |
| SF-2026-ARXIV-2606-27743 | potential_books_delta | not_selected | — | — | End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference remains evidence-complete after canonical owner transfer with V2 score 5 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27743 |
| SF-2026-ARXIV-2606-27757 | potential_books_delta | not_selected | — | — | Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27757 |
| SF-2026-ARXIV-2606-27780 | potential_books_delta | not_selected | — | — | Understanding Rollout Error in Graph World Models remains evidence-complete after canonical owner transfer with V2 score 5 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27780 |
| SF-2026-ARXIV-2606-27791 | potential_books_delta | not_selected | — | — | NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation remains evidence-complete after canonical owner transfer with V2 score 5 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27791 |
| SF-2026-ARXIV-2606-27797 | score_7_9; potential_books_delta | not_selected | — | — | Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27797 |
| SF-2026-ARXIV-2606-27806 | score_7_9; potential_books_delta | not_selected | — | — | Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27806 |
| SF-2026-ARXIV-2606-27814 | potential_books_delta | not_selected | — | — | ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27814 |
| SF-2026-ARXIV-2606-27826 | score_7_9; potential_books_delta | not_selected | — | — | NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27826 |
| SF-2026-ARXIV-2606-27841 | score_7_9; potential_books_delta | not_selected | — | — | WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27841 |
| SF-2026-ARXIV-2606-27866 | potential_books_delta | not_selected | — | — | FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models remains evidence-complete after canonical owner transfer with V2 score 5 and owner MODEL-MOE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27866 |
| SF-2026-ARXIV-2606-27906 | score_7_9; potential_books_delta | selected | DA-20260627-PHASE-CLOSED-LOOP-INFERENCE | — | 该 family 直接改变跨层 state/control boundary：以真实 mobile SoC 证据拆开 vision encoder、prefill、decode、cache 与 thermal phase 的 backend placement。 exact-v1 proof=Finally, we show that a four-step graph rewrite enables previously unsupported encoders, such as Phi-3.5-V, to reach the QNN path with up to 22x speedup, providing a practical porting recipe for mobile VLM deployment.；non-proof=Using FastVLM-0.5B as an end-to-end case study, together with encoder-only measurements across four architecture families, we show that phase matters: NPU execution is highly phase-dependent, delivering 1.64x speedup for prefill but only 1.18x for decode, while vision encoders achieve 20-45x speedups over CPU. | analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE |
| SF-2026-ARXIV-2606-27934 | score_7_9; potential_books_delta | not_selected | — | — | Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27934 |
| SF-2026-ARXIV-2606-27936 | score_7_9; potential_books_delta | not_selected | — | — | Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27936 |
| SF-2026-ARXIV-2606-27944 | score_7_9; potential_books_delta | not_selected | — | — | It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27944 |
| SF-2026-ARXIV-2606-27962 | potential_books_delta | not_selected | — | — | Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27962 |
| SF-2026-ARXIV-2606-27976 | potential_books_delta | not_selected | — | — | SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27976 |
| SF-2026-ARXIV-2606-27997 | score_7_9; potential_books_delta | not_selected | — | — | Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27997 |
| SF-2026-ARXIV-2606-28011 | potential_books_delta | not_selected | — | — | From Detection to Action: Using LLM Agents for Fault-Tolerant Control remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28011 |
| SF-2026-ARXIV-2606-28013 | score_7_9; potential_books_delta | not_selected | — | — | The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28013 |
| SF-2026-ARXIV-2606-28037 | score_7_9; potential_books_delta | not_selected | — | — | Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28037 |
| SF-2026-ARXIV-2606-28050 | score_7_9; potential_books_delta | not_selected | — | — | Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28050 |
| SF-2026-ARXIV-2606-28061 | score_7_9; potential_books_delta | not_selected | — | — | ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28061 |
| SF-2026-ARXIV-2606-28070 | potential_books_delta | not_selected | — | — | JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28070 |
| SF-2026-ARXIV-2606-28116 | score_7_9; potential_books_delta | not_selected | — | — | Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28116 |
| SF-2026-ARXIV-2606-28128 | potential_books_delta | not_selected | — | — | PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation remains evidence-complete after canonical owner transfer with V2 score 5 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28128 |
| SF-2026-ARXIV-2606-28153 | score_7_9; potential_books_delta | not_selected | — | — | Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28153 |
| SF-2026-ARXIV-2606-28166 | potential_books_delta | not_selected | — | — | Tandem Reinforcement Learning with Verifiable Rewards remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28166 |
| SF-2026-ARXIV-2606-28187 | potential_books_delta | not_selected | — | — | GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 6 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28187 |
| SF-2026-ARXIV-2606-28235 | potential_books_delta | not_selected | — | — | Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software remains evidence-complete after canonical owner transfer with V2 score 6 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28235 |
| SF-2026-ARXIV-2606-28276 | score_7_9; potential_books_delta | not_selected | — | — | SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28276 |
| SF-2026-ARXIV-2606-28277 | score_7_9; potential_books_delta | not_selected | — | — | Towards Automating Scientific Review with Google's Paper Assistant Tool remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28277 |
| SF-2026-ARXIV-2606-28279 | potential_books_delta | not_selected | — | — | Agentic Hardware Design as Repository-Level Code Evolution remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28279 |
| SF-2026-ARXIV-2606-28322 | score_7_9; potential_books_delta | not_selected | — | — | PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-28322 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-2026-ARXIV-2606-27406:start -->
Towards Evaluation of Implicit Software World Models in Coding LLMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27406:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27409:start -->
Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27409:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27416:start -->
Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27416:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27457:start -->
Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GATEWAY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27457:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27472:start -->
Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27472:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27474:start -->
Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27474:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27483:start -->
Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27483:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27492:start -->
QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27492:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27499:start -->
DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27499:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27510:start -->
The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27510:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27511:start -->
When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27511:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27550:start -->
EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27550:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27558:start -->
Productionized Fairness Measurement Under Privacy Constraints remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27558:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27567:start -->
On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27567:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27578:start -->
PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27578:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27580:start -->
Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27580:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27595:start -->
Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27595:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27608:start -->
Qwen-Image-2.0-RL Technical Report remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27608:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27622:start -->
FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27622:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27632:start -->
Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27632:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27634:start -->
Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27634:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27650:start -->
GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies remains evidence-complete after canonical owner transfer with V2 score 6 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27650:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27669:start -->
When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27669:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27679:start -->
From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27679:end -->

<!-- analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE:start -->
### DA-20260627-STRICT-MEDIATED-WORLD-STATE

若 world model 可从 history bypass latent state，预测准确率无法识别 state quality。strict mediation 把 textual belief state 变成唯一读取面，训练代价和离散状态误差则成为新的 failure pressure。
<!-- analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27683:start -->
CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27683:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27704:start -->
AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27709:start -->
Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27709:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27732:start -->
Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-GENERATIVE-PARADIGMS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27732:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27739:start -->
The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27739:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27743:start -->
End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference remains evidence-complete after canonical owner transfer with V2 score 5 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27743:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27757:start -->
Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27757:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27780:start -->
Understanding Rollout Error in Graph World Models remains evidence-complete after canonical owner transfer with V2 score 5 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27780:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27791:start -->
NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation remains evidence-complete after canonical owner transfer with V2 score 5 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27791:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27797:start -->
Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27797:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27806:start -->
Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27806:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27814:start -->
ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27814:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27826:start -->
NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27826:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27841:start -->
WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27841:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27866:start -->
FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models remains evidence-complete after canonical owner transfer with V2 score 5 and owner MODEL-MOE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27866:end -->

<!-- analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE:start -->
### DA-20260627-PHASE-CLOSED-LOOP-INFERENCE

mobile phase characterization、closed-loop task time 与 kernel-level capacity simulation 共同说明：推理优化不能只发布单步 latency。backend 必须按 vision/prefill/decode/queue/kernel phase 建模，并以任务完成时间、success 与饱和边界验收。
<!-- analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27934:start -->
Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27934:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27936:start -->
Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27936:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27944:start -->
It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27944:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27962:start -->
Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27962:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27976:start -->
SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27976:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27997:start -->
Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27997:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28011:start -->
From Detection to Action: Using LLM Agents for Fault-Tolerant Control remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28011:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28013:start -->
The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28013:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28037:start -->
Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28037:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28050:start -->
Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28050:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28061:start -->
ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28061:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28070:start -->
JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28070:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28116:start -->
Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28116:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28128:start -->
PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation remains evidence-complete after canonical owner transfer with V2 score 5 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28128:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28153:start -->
Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28153:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28166:start -->
Tandem Reinforcement Learning with Verifiable Rewards remains evidence-complete after canonical owner transfer with V2 score 5 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28166:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28187:start -->
GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 6 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28187:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28235:start -->
Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software remains evidence-complete after canonical owner transfer with V2 score 6 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28235:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28276:start -->
SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28276:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28277:start -->
Towards Automating Scientific Review with Google's Paper Assistant Tool remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28277:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28279:start -->
Agentic Hardware Design as Repository-Level Code Evolution remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28279:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28322:start -->
PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-28322:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27409 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-27409 | delta:SF-2026-ARXIV-2606-27409 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27409 |
| SF-2026-ARXIV-2606-27457 | PLATFORM-GATEWAY | books/part-06-ai-infrastructure/62-gateway.md#L1 | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | existing:SF-2026-ARXIV-2606-27457 | delta:SF-2026-ARXIV-2606-27457 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27457 |
| SF-2026-ARXIV-2606-27472 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-27472 | delta:SF-2026-ARXIV-2606-27472 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27472 |
| SF-2026-ARXIV-2606-27492 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-27492 | delta:SF-2026-ARXIV-2606-27492 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27492 |
| SF-2026-ARXIV-2606-27558 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-27558 | delta:SF-2026-ARXIV-2606-27558 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27558 |
| SF-2026-ARXIV-2606-27567 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-27567 | delta:SF-2026-ARXIV-2606-27567 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27567 |
| SF-2026-ARXIV-2606-27578 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-27578 | delta:SF-2026-ARXIV-2606-27578 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27578 |
| SF-2026-ARXIV-2606-27580 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-27580 | delta:SF-2026-ARXIV-2606-27580 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27580 |
| SF-2026-ARXIV-2606-27632 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27632 | delta:SF-2026-ARXIV-2606-27632 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27632 |
| SF-2026-ARXIV-2606-27634 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L206 — ## Monitoring 也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27634 | delta:SF-2026-ARXIV-2606-27634 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27634 |
| SF-2026-ARXIV-2606-27650 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L399 — ## Agent Runtime State Machine | books/part-07-agent/83-mcp.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27650 | delta:SF-2026-ARXIV-2606-27650 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27650 |
| SF-2026-ARXIV-2606-27669 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27669 | delta:SF-2026-ARXIV-2606-27669 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27669 |
| SF-2026-ARXIV-2606-27679 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L206 — ## Monitoring 也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27679 | delta:SF-2026-ARXIV-2606-27679 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27679 |
| SF-2026-ARXIV-2606-27681 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27681 | delta:SF-2026-ARXIV-2606-27681 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27681 |
| SF-2026-ARXIV-2606-27683 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27683 | delta:SF-2026-ARXIV-2606-27683 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27683 |
| SF-2026-ARXIV-2606-27704 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27704 | delta:SF-2026-ARXIV-2606-27704 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27704 |
| SF-2026-ARXIV-2606-27709 | TRAIN-DATA | books/part-04-training-system/27-data.md#L487 — ### 从 sample provenance 到训练生命周期 lineage | books/part-04-training-system/28-pretraining.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27709 | delta:SF-2026-ARXIV-2606-27709 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27709 |
| SF-2026-ARXIV-2606-27732 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L276 — ## Cache、rollback 与 exactness | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27732 | delta:SF-2026-ARXIV-2606-27732 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27732 |
| SF-2026-ARXIV-2606-27739 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27739 | delta:SF-2026-ARXIV-2606-27739 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27739 |
| SF-2026-ARXIV-2606-27743 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L343 — ### Semantic Predicate 的 Token Cost 应成为 Query-planner State | books/part-05-inference-system/55-pd-disaggregation.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27743 | delta:SF-2026-ARXIV-2606-27743 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27743 |
| SF-2026-ARXIV-2606-27757 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L271 — ## 完成证据与 Verification | books/part-07-agent/78-tool-calling.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27757 | delta:SF-2026-ARXIV-2606-27757 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27757 |
| SF-2026-ARXIV-2606-27780 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27780 | delta:SF-2026-ARXIV-2606-27780 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27780 |
| SF-2026-ARXIV-2606-27797 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L629 — ### 从 Phase 串行到依赖驱动的跨 Phase 重排 | books/part-04-training-system/37-tensor-parallel.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27797 | delta:SF-2026-ARXIV-2606-27797 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27797 |
| SF-2026-ARXIV-2606-27806 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L271 — ## 完成证据与 Verification | books/part-07-agent/78-tool-calling.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27806 | delta:SF-2026-ARXIV-2606-27806 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27806 |
| SF-2026-ARXIV-2606-27814 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27814 | delta:SF-2026-ARXIV-2606-27814 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27814 |
| SF-2026-ARXIV-2606-27826 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27826 | delta:SF-2026-ARXIV-2606-27826 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27826 |
| SF-2026-ARXIV-2606-27841 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L107 — ## 利用率与有效利用率 | books/part-06-ai-infrastructure/69-trace.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27841 | delta:SF-2026-ARXIV-2606-27841 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27841 |
| SF-2026-ARXIV-2606-27866 | MODEL-MOE | books/part-02-model/21-moe.md#L491 — ### 从局部结果到可执行的系统边界 | books/part-02-model/20-sampling.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27866 | delta:SF-2026-ARXIV-2606-27866 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27866 |
| SF-2026-ARXIV-2606-27906 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L80 — ## 请求状态机 | books/part-05-inference-system/43-prefill.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27906 | delta:SF-2026-ARXIV-2606-27906 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27906 |
| SF-2026-ARXIV-2606-27934 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27934 | delta:SF-2026-ARXIV-2606-27934 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27934 |
| SF-2026-ARXIV-2606-27936 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27936 | delta:SF-2026-ARXIV-2606-27936 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27936 |
| SF-2026-ARXIV-2606-27944 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27944 | delta:SF-2026-ARXIV-2606-27944 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27944 |
| SF-2026-ARXIV-2606-27962 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L118 — ## Paved Road 与 Escape Hatch | books/part-06-ai-infrastructure/58-kubeflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27962 | delta:SF-2026-ARXIV-2606-27962 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27962 |
| SF-2026-ARXIV-2606-27976 | AGENT-RAG | books/part-07-agent/76-rag.md#L35 — ## Offline Ingestion 不是预处理细节 | books/part-07-agent/77-memory.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27976 | delta:SF-2026-ARXIV-2606-27976 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27976 |
| SF-2026-ARXIV-2606-27997 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27997 | delta:SF-2026-ARXIV-2606-27997 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27997 |
| SF-2026-ARXIV-2606-28011 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28011 | delta:SF-2026-ARXIV-2606-28011 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28011 |
| SF-2026-ARXIV-2606-28013 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28013 | delta:SF-2026-ARXIV-2606-28013 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28013 |
| SF-2026-ARXIV-2606-28037 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28037 | delta:SF-2026-ARXIV-2606-28037 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28037 |
| SF-2026-ARXIV-2606-28050 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28050 | delta:SF-2026-ARXIV-2606-28050 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28050 |
| SF-2026-ARXIV-2606-28061 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28061 | delta:SF-2026-ARXIV-2606-28061 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28061 |
| SF-2026-ARXIV-2606-28070 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L118 — ## Paved Road 与 Escape Hatch | books/part-06-ai-infrastructure/58-kubeflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28070 | delta:SF-2026-ARXIV-2606-28070 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28070 |
| SF-2026-ARXIV-2606-28116 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L206 — ## Monitoring 也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28116 | delta:SF-2026-ARXIV-2606-28116 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28116 |
| SF-2026-ARXIV-2606-28128 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28128 | delta:SF-2026-ARXIV-2606-28128 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28128 |
| SF-2026-ARXIV-2606-28153 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28153 | delta:SF-2026-ARXIV-2606-28153 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28153 |
| SF-2026-ARXIV-2606-28187 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L283 — ### 共享 Repository 需要 Commitment Protocol，不只是更多消息 | books/part-07-agent/81-workflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28187 | delta:SF-2026-ARXIV-2606-28187 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28187 |
| SF-2026-ARXIV-2606-28235 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L399 — ## Agent Runtime State Machine | books/part-07-agent/83-mcp.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28235 | delta:SF-2026-ARXIV-2606-28235 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28235 |
| SF-2026-ARXIV-2606-28276 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305 — ## Safety envelope | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28276 | delta:SF-2026-ARXIV-2606-28276 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28276 |
| SF-2026-ARXIV-2606-28277 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28277 | delta:SF-2026-ARXIV-2606-28277 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28277 |
| SF-2026-ARXIV-2606-28279 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28279 | delta:SF-2026-ARXIV-2606-28279 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28279 |
| SF-2026-ARXIV-2606-28322 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28322 | delta:SF-2026-ARXIV-2606-28322 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28322 |

<!-- existing:SF-2026-ARXIV-2606-27409:start -->
多智能体 owner 持有拓扑、角色、消息 provenance、独立 verifier 与 commit authority。
<!-- existing:SF-2026-ARXIV-2606-27409:end -->

<!-- delta:SF-2026-ARXIV-2606-27409:start -->
Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement 的 exact-v1 机制为：The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。
<!-- delta:SF-2026-ARXIV-2606-27409:end -->

<!-- books-review:SF-2026-ARXIV-2606-27409:start -->
Unique owner `AGENT-MULTI-AGENT`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 披露的 evaluation signal 是：By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing exact-v1 的观测边界是：By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing 它没有证明 The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27409:end -->

<!-- existing:SF-2026-ARXIV-2606-27457:start -->
Gateway 绑定认证、请求分类、route、质量/负载阈值、fallback 与 SLO。
<!-- existing:SF-2026-ARXIV-2606-27457:end -->

<!-- delta:SF-2026-ARXIV-2606-27457:start -->
Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving 的 exact-v1 机制为：To address this challenge, we propose a two-stage cascaded solution. 因此 把请求分类、模型路由、升级阈值、成本与 SLO 共同版本化。
<!-- delta:SF-2026-ARXIV-2606-27457:end -->

<!-- books-review:SF-2026-ARXIV-2606-27457:start -->
Unique owner `PLATFORM-GATEWAY`; adjacent non-owner `books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Efficient deployment of large language models (LLMs) in production forces a trade-off between accuracy and cost. 披露的 evaluation signal 是：It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration. exact-v1 的观测边界是：It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration. 它没有证明 To address this challenge, we propose a two-stage cascaded solution. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27457:end -->

<!-- existing:SF-2026-ARXIV-2606-27472:start -->
记忆写入以来源、有效时间、事务边界、supersession 与恢复回执为长期状态，未经验证的新条目不能静默覆盖旧事实。
<!-- existing:SF-2026-ARXIV-2606-27472:end -->

<!-- delta:SF-2026-ARXIV-2606-27472:start -->
Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents 的 exact-v1 机制为：Acting correctly requires using the current value of a fact and discarding values that have been superseded. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-27472:end -->

<!-- books-review:SF-2026-ARXIV-2606-27472:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. 披露的 evaluation signal 是：We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. exact-v1 的观测边界是：We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. 它没有证明 Acting correctly requires using the current value of a fact and discarding values that have been superseded. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27472:end -->

<!-- existing:SF-2026-ARXIV-2606-27492:start -->
多智能体 owner 持有拓扑、角色、消息 provenance、独立 verifier 与 commit authority。
<!-- existing:SF-2026-ARXIV-2606-27492:end -->

<!-- delta:SF-2026-ARXIV-2606-27492:start -->
QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems 的 exact-v1 机制为：This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。
<!-- delta:SF-2026-ARXIV-2606-27492:end -->

<!-- books-review:SF-2026-ARXIV-2606-27492:start -->
Unique owner `AGENT-MULTI-AGENT`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：In the CF fulltest setting, the best generated graph reduces RMSE from 12.53 for the strongest fixed topology to 7.87 while also reducing messages, model calls, and token cost; Silo-style results show the same direction of improvement over cold and fixed-topology baselines. 披露的 evaluation signal 是：This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. exact-v1 的观测边界是：This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 它没有证明 This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27492:end -->

<!-- existing:SF-2026-ARXIV-2606-27558:start -->
评估系统把样本、metric、judge、阈值、不确定性与 release authority 分离并版本化。
<!-- existing:SF-2026-ARXIV-2606-27558:end -->

<!-- delta:SF-2026-ARXIV-2606-27558:start -->
Productionized Fairness Measurement Under Privacy Constraints 的 exact-v1 机制为：We close with a transferable framework for institutions seeking to implement similar privacy-preserving measurement infrastructure. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-27558:end -->

<!-- books-review:SF-2026-ARXIV-2606-27558:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. 披露的 evaluation signal 是：Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. exact-v1 的观测边界是：Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. 它没有证明 We close with a transferable framework for institutions seeking to implement similar privacy-preserving measurement infrastructure. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27558:end -->

<!-- existing:SF-2026-ARXIV-2606-27567:start -->
安全边界由独立 reference monitor 持有，instruction/data/control 分离，并在身份、证据或 policy 不足时 fail closed。
<!-- existing:SF-2026-ARXIV-2606-27567:end -->

<!-- delta:SF-2026-ARXIV-2606-27567:start -->
On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models 的 exact-v1 机制为：It mirrors the code-data confusion in Von Neumann machines that gives rise to buffer overflows, a vulnerability class that took decades of layered defenses (DEP, Write-XOR-Execute, ASLR, stack canaries, and ultimately memory-safe languages) to contain, because no single mechanism sufficed. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-27567:end -->

<!-- books-review:SF-2026-ARXIV-2606-27567:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Prompt injection is the top security risk for LLM-integrated applications, yet every defense proposed so far has been broken. 披露的 evaluation signal 是：We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). exact-v1 的观测边界是：We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). 它没有证明 It mirrors the code-data confusion in Von Neumann machines that gives rise to buffer overflows, a vulnerability class that took decades of layered defenses (DEP, Write-XOR-Execute, ASLR, stack canaries, and ultimately memory-safe languages) to contain, because no single mechanism sufficed. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27567:end -->

<!-- existing:SF-2026-ARXIV-2606-27578:start -->
RLHF owner 持有 policy、reward、judge、rubric 与 calibration lineage，避免分数被当作无版本真值。
<!-- existing:SF-2026-ARXIV-2606-27578:end -->

<!-- delta:SF-2026-ARXIV-2606-27578:start -->
PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration 的 exact-v1 机制为：PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。
<!-- delta:SF-2026-ARXIV-2606-27578:end -->

<!-- books-review:SF-2026-ARXIV-2606-27578:start -->
Unique owner `TRAIN-RLHF`; adjacent non-owner `books/part-04-training-system/32-ppo.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Reward models for Reinforcement Learning from Human Feedback (RLHF) pool preferences across thousands of annotators and fit one global affine calibrator, collapsing raters with systematically different rating-scale offsets and slopes into a single average-rater fit that does not match any individual annotator. 披露的 evaluation signal 是：On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. exact-v1 的观测边界是：On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. 它没有证明 PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27578:end -->

<!-- existing:SF-2026-ARXIV-2606-27580:start -->
RLHF owner 持有 policy、reward、judge、rubric 与 calibration lineage，避免分数被当作无版本真值。
<!-- existing:SF-2026-ARXIV-2606-27580:end -->

<!-- delta:SF-2026-ARXIV-2606-27580:start -->
Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF 的 exact-v1 机制为：Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。
<!-- delta:SF-2026-ARXIV-2606-27580:end -->

<!-- books-review:SF-2026-ARXIV-2606-27580:start -->
Unique owner `TRAIN-RLHF`; adjacent non-owner `books/part-04-training-system/32-ppo.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：On a tabular Markov decision process (MDP) proof-of-concept, RAC reduces the closed-form policy bias by up to 47.9x at the two-slow-channel configuration, beating wait-for-slow at lower wall-clock cost. 披露的 evaluation signal 是：We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. exact-v1 的观测边界是：We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. 它没有证明 Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27580:end -->

<!-- existing:SF-2026-ARXIV-2606-27632:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27632:end -->

<!-- delta:SF-2026-ARXIV-2606-27632:start -->
把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。
<!-- delta:SF-2026-ARXIV-2606-27632:end -->

<!-- books-review:SF-2026-ARXIV-2606-27632:start -->
Principle Reuse; No Change — Existing Coverage. Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability.
<!-- books-review:SF-2026-ARXIV-2606-27632:end -->

<!-- existing:SF-2026-ARXIV-2606-27634:start -->
The monitoring owner already marks checkpoint-bound monitors stale and requires re-alignment, retraining or abstention; sequential LoRA/reference-set drift is an instance, not a new contract.
<!-- existing:SF-2026-ARXIV-2606-27634:end -->

<!-- delta:SF-2026-ARXIV-2606-27634:start -->
把 sequential LoRA personalization 的 checkpoint、reference-set drift 与遗忘监控绑定为持续适配合同。
<!-- delta:SF-2026-ARXIV-2606-27634:end -->

<!-- books-review:SF-2026-ARXIV-2606-27634:start -->
Principle Reuse; No Change — Existing Coverage. However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting.
<!-- books-review:SF-2026-ARXIV-2606-27634:end -->

<!-- existing:SF-2026-ARXIV-2606-27650:start -->
Ch84 已把 workspace/runtime、intent、acceptance predicate、trace/replay 与 promotion gate 分开。 本 family 的 source-specific delta 为：把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。 Fresh adjacent review at books/part-07-agent/83-mcp.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27650:end -->

<!-- delta:SF-2026-ARXIV-2606-27650:start -->
把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。
<!-- delta:SF-2026-ARXIV-2606-27650:end -->

<!-- books-review:SF-2026-ARXIV-2606-27650:start -->
Principle Reuse; No Change — Existing Coverage. These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work.
<!-- books-review:SF-2026-ARXIV-2606-27650:end -->

<!-- existing:SF-2026-ARXIV-2606-27669:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27669:end -->

<!-- delta:SF-2026-ARXIV-2606-27669:start -->
把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。
<!-- delta:SF-2026-ARXIV-2606-27669:end -->

<!-- books-review:SF-2026-ARXIV-2606-27669:start -->
Principle Reuse; No Change — Existing Coverage. However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect.
<!-- books-review:SF-2026-ARXIV-2606-27669:end -->

<!-- existing:SF-2026-ARXIV-2606-27679:start -->
Ch67 已把 monitor 定义为需校准的 observe/alert sensor，并要求 checkpoint 变化后 stale/abstain。 本 family 的 source-specific delta 为：给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。 Fresh adjacent review at books/part-06-ai-infrastructure/66-evaluation-system.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27679:end -->

<!-- delta:SF-2026-ARXIV-2606-27679:start -->
给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。
<!-- delta:SF-2026-ARXIV-2606-27679:end -->

<!-- books-review:SF-2026-ARXIV-2606-27679:start -->
Principle Reuse; No Change — Existing Coverage. However, under distribution shift, structured and compressed features are more robust, suggesting that in-domain performance alone is insufficient to measure progress.
<!-- books-review:SF-2026-ARXIV-2606-27679:end -->

<!-- existing:SF-2026-ARXIV-2606-27681:start -->
The world-model owner separates latent state from physical commit, but does not require state-only mediation that makes representation quality identifiable.
<!-- existing:SF-2026-ARXIV-2606-27681:end -->

<!-- delta:SF-2026-ARXIV-2606-27681:start -->
用 strict mediation 让 textual belief state 成为唯一可测试的预测状态，阻断 history bypass。
<!-- delta:SF-2026-ARXIV-2606-27681:end -->

<!-- books-review:SF-2026-ARXIV-2606-27681:start -->
Direct Evolution; Integrate. We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection.
<!-- books-review:SF-2026-ARXIV-2606-27681:end -->

<!-- existing:SF-2026-ARXIV-2606-27683:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27683:end -->

<!-- delta:SF-2026-ARXIV-2606-27683:start -->
揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。
<!-- delta:SF-2026-ARXIV-2606-27683:end -->

<!-- books-review:SF-2026-ARXIV-2606-27683:start -->
Principle Reuse; No Change — Existing Coverage. On WMDP, it lowers hazardous knowledge accuracy to 25.68, near random guessing, while preserving MMLU accuracy of 52.67.
<!-- books-review:SF-2026-ARXIV-2606-27683:end -->

<!-- existing:SF-2026-ARXIV-2606-27704:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27704:end -->

<!-- delta:SF-2026-ARXIV-2606-27704:start -->
把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。
<!-- delta:SF-2026-ARXIV-2606-27704:end -->

<!-- books-review:SF-2026-ARXIV-2606-27704:start -->
Principle Reuse; No Change — Existing Coverage. Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives.
<!-- books-review:SF-2026-ARXIV-2606-27704:end -->

<!-- existing:SF-2026-ARXIV-2606-27709:start -->
Ch27 已让 sample provenance、mixture/admission 与训练生命周期 lineage 共同决定数据能否进入训练。 本 family 的 source-specific delta 为：证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。 Fresh adjacent review at books/part-04-training-system/28-pretraining.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27709:end -->

<!-- delta:SF-2026-ARXIV-2606-27709:start -->
证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。
<!-- delta:SF-2026-ARXIV-2606-27709:end -->

<!-- books-review:SF-2026-ARXIV-2606-27709:start -->
Principle Reuse; No Change — Existing Coverage. These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective.
<!-- books-review:SF-2026-ARXIV-2606-27709:end -->

<!-- existing:SF-2026-ARXIV-2606-27732:start -->
The generation owner covers provisional commit and cache invalidation, but not an asymmetric right-context side path coexisting with a causal cache.
<!-- existing:SF-2026-ARXIV-2606-27732:end -->

<!-- delta:SF-2026-ARXIV-2606-27732:start -->
用 asymmetric bidirectional sidecar 重构 diffusion-LM 的右上下文、KV cache 与 parallel decode 取舍。
<!-- delta:SF-2026-ARXIV-2606-27732:end -->

<!-- books-review:SF-2026-ARXIV-2606-27732:start -->
Direct Evolution; Integrate. Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average.
<!-- books-review:SF-2026-ARXIV-2606-27732:end -->

<!-- existing:SF-2026-ARXIV-2606-27739:start -->
Ch33 已分离 trajectory owner、outcome verifier、teacher guidance 与 typed credit，避免 teacher 获得 reward sign authority。 本 family 的 source-specific delta 为：把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。 Fresh adjacent review at books/part-04-training-system/32-ppo.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27739:end -->

<!-- delta:SF-2026-ARXIV-2606-27739:start -->
把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。
<!-- delta:SF-2026-ARXIV-2606-27739:end -->

<!-- books-review:SF-2026-ARXIV-2606-27739:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》在 3 Analysis; 3.3 Theoretical Analysis; 5 Experiments 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27739:end -->

<!-- existing:SF-2026-ARXIV-2606-27743:start -->
Ch56 已让 request budget、queue state、goodput 与 fallback 共同约束 compute allocation。 本 family 的 source-specific delta 为：把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。 Fresh adjacent review at books/part-05-inference-system/55-pd-disaggregation.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27743:end -->

<!-- delta:SF-2026-ARXIV-2606-27743:start -->
把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。
<!-- delta:SF-2026-ARXIV-2606-27743:end -->

<!-- books-review:SF-2026-ARXIV-2606-27743:start -->
Principle Reuse; No Change — Existing Coverage. A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time.
<!-- books-review:SF-2026-ARXIV-2606-27743:end -->

<!-- existing:SF-2026-ARXIV-2606-27757:start -->
Ch79 已区分 plan proposal、pre-commit verifier、environment feedback 与 executable commit。 本 family 的 source-specific delta 为：把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。 Fresh adjacent review at books/part-07-agent/78-tool-calling.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27757:end -->

<!-- delta:SF-2026-ARXIV-2606-27757:start -->
把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。
<!-- delta:SF-2026-ARXIV-2606-27757:end -->

<!-- books-review:SF-2026-ARXIV-2606-27757:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》在 IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27757:end -->

<!-- existing:SF-2026-ARXIV-2606-27780:start -->
Ch25 已分离 belief/latent state、action-conditioned transition、physical truth 与 commit authority。 本 family 的 source-specific delta 为：给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。 Fresh adjacent review at books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27780:end -->

<!-- delta:SF-2026-ARXIV-2606-27780:start -->
给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。
<!-- delta:SF-2026-ARXIV-2606-27780:end -->

<!-- books-review:SF-2026-ARXIV-2606-27780:start -->
Principle Reuse; No Change — Existing Coverage. Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail.
<!-- books-review:SF-2026-ARXIV-2606-27780:end -->

<!-- existing:SF-2026-ARXIV-2606-27797:start -->
The distributed-training owner covers model/optimizer partitioning, but not independent teacher-inference and student-training topology plans joined by a versioned handoff.
<!-- existing:SF-2026-ARXIV-2606-27797:end -->

<!-- delta:SF-2026-ARXIV-2606-27797:start -->
按 teacher/student 不对称分别选择模型分片与拓扑通信，改变 KD runtime partition contract。
<!-- delta:SF-2026-ARXIV-2606-27797:end -->

<!-- books-review:SF-2026-ARXIV-2606-27797:start -->
Direct Evolution; Integrate. exact-v1 的结论只覆盖《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》在 3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27797:end -->

<!-- existing:SF-2026-ARXIV-2606-27806:start -->
The planning owner separates proposal, validation and commit, but lacks a learned transition-disagreement gate that requests targeted plan revision without taking action authority.
<!-- existing:SF-2026-ARXIV-2606-27806:end -->

<!-- delta:SF-2026-ARXIV-2606-27806:start -->
以 parametric transition model 校验 agent imagined delta，并把 disagreement 变成 targeted revision gate。
<!-- delta:SF-2026-ARXIV-2606-27806:end -->

<!-- books-review:SF-2026-ARXIV-2606-27806:start -->
Direct Evolution; Integrate. These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning.
<!-- books-review:SF-2026-ARXIV-2606-27806:end -->

<!-- existing:SF-2026-ARXIV-2606-27814:start -->
Ch33 已分离 trajectory owner、outcome verifier、teacher guidance 与 typed credit，避免 teacher 获得 reward sign authority。 本 family 的 source-specific delta 为：在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。 Fresh adjacent review at books/part-04-training-system/32-ppo.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27814:end -->

<!-- delta:SF-2026-ARXIV-2606-27814:start -->
在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。
<!-- delta:SF-2026-ARXIV-2606-27814:end -->

<!-- books-review:SF-2026-ARXIV-2606-27814:start -->
Principle Reuse; No Change — Existing Coverage. Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points.
<!-- books-review:SF-2026-ARXIV-2606-27814:end -->

<!-- existing:SF-2026-ARXIV-2606-27826:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27826:end -->

<!-- delta:SF-2026-ARXIV-2606-27826:start -->
把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。
<!-- delta:SF-2026-ARXIV-2606-27826:end -->

<!-- books-review:SF-2026-ARXIV-2606-27826:start -->
Principle Reuse; No Change — Existing Coverage. NormAct therefore supports the development of embodied agents that pursue everyday goals while proactively respecting unstated social norms.
<!-- books-review:SF-2026-ARXIV-2606-27826:end -->

<!-- existing:SF-2026-ARXIV-2606-27841:start -->
The cost owner models offered load and whole-run energy, but does not expose layer/operator measurement identity before architecture-level recomposition.
<!-- existing:SF-2026-ARXIV-2606-27841:end -->

<!-- delta:SF-2026-ARXIV-2606-27841:start -->
把 inference energy estimation 从整模型 proxy 拆成可跨任务/架构迁移的 layer-wise measurement contract。
<!-- delta:SF-2026-ARXIV-2606-27841:end -->

<!-- books-review:SF-2026-ARXIV-2606-27841:start -->
Direct Evolution; Integrate. We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures.
<!-- books-review:SF-2026-ARXIV-2606-27841:end -->

<!-- existing:SF-2026-ARXIV-2606-27866:start -->
The MoE owner already defines a shared checkpoint plus sampled subnet profiles, independent quality envelopes and online budget selection; nested intra-expert pruning is covered.
<!-- existing:SF-2026-ARXIV-2606-27866:end -->

<!-- delta:SF-2026-ARXIV-2606-27866:start -->
把一次性 MoE compression artifact 改成 nested subnet family 与可在线切换的 budget state。
<!-- delta:SF-2026-ARXIV-2606-27866:end -->

<!-- books-review:SF-2026-ARXIV-2606-27866:start -->
Principle Reuse; No Change — Existing Coverage. Specifically, on Qwen2-57B-A14B, our method retains ~99.8% of base performance while pruning 50% of routed expert parameters even without fine-tuning.
<!-- books-review:SF-2026-ARXIV-2606-27866:end -->

<!-- existing:SF-2026-ARXIV-2606-27906:start -->
The inference lifecycle names prefill/decode/request state, but does not bind mobile vision/prefill/decode placement and thermal phase to one hardware-specific record.
<!-- existing:SF-2026-ARXIV-2606-27906:end -->

<!-- delta:SF-2026-ARXIV-2606-27906:start -->
以真实 mobile SoC 证据拆开 vision encoder、prefill、decode、cache 与 thermal phase 的 backend placement。
<!-- delta:SF-2026-ARXIV-2606-27906:end -->

<!-- books-review:SF-2026-ARXIV-2606-27906:start -->
Direct Evolution; Integrate. Using FastVLM-0.5B as an end-to-end case study, together with encoder-only measurements across four architecture families, we show that phase matters: NPU execution is highly phase-dependent, delivering 1.64x speedup for prefill but only 1.18x for decode, while vision encoders achieve 20-45x speedups over CPU.
<!-- books-review:SF-2026-ARXIV-2606-27906:end -->

<!-- existing:SF-2026-ARXIV-2606-27934:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27934:end -->

<!-- delta:SF-2026-ARXIV-2606-27934:start -->
用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。
<!-- delta:SF-2026-ARXIV-2606-27934:end -->

<!-- books-review:SF-2026-ARXIV-2606-27934:start -->
Principle Reuse; No Change — Existing Coverage. We then treat the check itself as a security object: a probe seed committed for offline reproducibility is an attack surface, and a probe-aware adversary can hide a corruption in the probe's null space, fooling even a quorum of bit-identical witnesses, while a Fiat-Shamir challenge derived from the claimed output closes this.
<!-- books-review:SF-2026-ARXIV-2606-27934:end -->

<!-- existing:SF-2026-ARXIV-2606-27936:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27936:end -->

<!-- delta:SF-2026-ARXIV-2606-27936:start -->
证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。
<!-- delta:SF-2026-ARXIV-2606-27936:end -->

<!-- books-review:SF-2026-ARXIV-2606-27936:start -->
Principle Reuse; No Change — Existing Coverage. We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention.
<!-- books-review:SF-2026-ARXIV-2606-27936:end -->

<!-- existing:SF-2026-ARXIV-2606-27944:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27944:end -->

<!-- delta:SF-2026-ARXIV-2606-27944:start -->
以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。
<!-- delta:SF-2026-ARXIV-2606-27944:end -->

<!-- books-review:SF-2026-ARXIV-2606-27944:start -->
Principle Reuse; No Change — Existing Coverage. Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved.
<!-- books-review:SF-2026-ARXIV-2606-27944:end -->

<!-- existing:SF-2026-ARXIV-2606-27962:start -->
Ch57 已把 paved road、escape hatch、artifact/environment identity 与 lifecycle control 分开。 本 family 的 source-specific delta 为：把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。 Fresh adjacent review at books/part-06-ai-infrastructure/58-kubeflow.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27962:end -->

<!-- delta:SF-2026-ARXIV-2606-27962:start -->
把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。
<!-- delta:SF-2026-ARXIV-2606-27962:end -->

<!-- books-review:SF-2026-ARXIV-2606-27962:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》在 Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27962:end -->

<!-- existing:SF-2026-ARXIV-2606-27976:start -->
Ch76 已让 index/source provenance、retrieval evidence 与 context admission 分别持有状态和权限。 本 family 的 source-specific delta 为：把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。 Fresh adjacent review at books/part-07-agent/77-memory.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27976:end -->

<!-- delta:SF-2026-ARXIV-2606-27976:start -->
把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。
<!-- delta:SF-2026-ARXIV-2606-27976:end -->

<!-- books-review:SF-2026-ARXIV-2606-27976:start -->
Principle Reuse; No Change — Existing Coverage. SHARD preserves retrieval and compartmentalizes alignment evidence, but does not provide DP, unlinkability, or cancellable templates.
<!-- books-review:SF-2026-ARXIV-2606-27976:end -->

<!-- existing:SF-2026-ARXIV-2606-27997:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27997:end -->

<!-- delta:SF-2026-ARXIV-2606-27997:start -->
把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。
<!-- delta:SF-2026-ARXIV-2606-27997:end -->

<!-- books-review:SF-2026-ARXIV-2606-27997:start -->
Principle Reuse; No Change — Existing Coverage. For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets.
<!-- books-review:SF-2026-ARXIV-2606-27997:end -->

<!-- existing:SF-2026-ARXIV-2606-28011:start -->
Ch81 已把 artifact state、deterministic interlock、verifier 与 retry/fallback 组织为可提交状态机。 本 family 的 source-specific delta 为：把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。 Fresh adjacent review at books/part-07-agent/80-reflection.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28011:end -->

<!-- delta:SF-2026-ARXIV-2606-28011:start -->
把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。
<!-- delta:SF-2026-ARXIV-2606-28011:end -->

<!-- books-review:SF-2026-ARXIV-2606-28011:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》在 4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28011:end -->

<!-- existing:SF-2026-ARXIV-2606-28013:start -->
The evaluation owner requires semantic-equivalent adapters, but does not freeze the two-axis type-acceptance versus semantic-equivalence coverage matrix.
<!-- existing:SF-2026-ARXIV-2606-28013:end -->

<!-- delta:SF-2026-ARXIV-2606-28013:start -->
把 autoformalization 的 type correctness 与 semantic equivalence 交叉分层，防止单标量误归因。
<!-- delta:SF-2026-ARXIV-2606-28013:end -->

<!-- books-review:SF-2026-ARXIV-2606-28013:start -->
Direct Evolution; Integrate. We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF).
<!-- books-review:SF-2026-ARXIV-2606-28013:end -->

<!-- existing:SF-2026-ARXIV-2606-28037:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28037:end -->

<!-- delta:SF-2026-ARXIV-2606-28037:start -->
以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。
<!-- delta:SF-2026-ARXIV-2606-28037:end -->

<!-- books-review:SF-2026-ARXIV-2606-28037:start -->
Principle Reuse; No Change — Existing Coverage. In an empirical study across classification and regression tasks, GBV-PD consistently outperformed non-directional baselines and remained competitive with a full-gradient reference, while offering better time and storage profiles for repeated updates via reusable GBV caching.
<!-- books-review:SF-2026-ARXIV-2606-28037:end -->

<!-- existing:SF-2026-ARXIV-2606-28050:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28050:end -->

<!-- delta:SF-2026-ARXIV-2606-28050:start -->
用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。
<!-- delta:SF-2026-ARXIV-2606-28050:end -->

<!-- books-review:SF-2026-ARXIV-2606-28050:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》在 Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28050:end -->

<!-- existing:SF-2026-ARXIV-2606-28061:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28061:end -->

<!-- delta:SF-2026-ARXIV-2606-28061:start -->
把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。
<!-- delta:SF-2026-ARXIV-2606-28061:end -->

<!-- books-review:SF-2026-ARXIV-2606-28061:start -->
Principle Reuse; No Change — Existing Coverage. ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.
<!-- books-review:SF-2026-ARXIV-2606-28061:end -->

<!-- existing:SF-2026-ARXIV-2606-28070:start -->
Ch57 已把 paved road、escape hatch、artifact/environment identity 与 lifecycle control 分开。 本 family 的 source-specific delta 为：提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。 Fresh adjacent review at books/part-06-ai-infrastructure/58-kubeflow.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28070:end -->

<!-- delta:SF-2026-ARXIV-2606-28070:start -->
提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。
<!-- delta:SF-2026-ARXIV-2606-28070:end -->

<!-- books-review:SF-2026-ARXIV-2606-28070:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》在 3.3 Results; 4.2.3 Results; Module 1: Data evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28070:end -->

<!-- existing:SF-2026-ARXIV-2606-28116:start -->
The monitoring owner covers telemetry and checkpoint-stale monitors, but lacks mechanism-derived pre-loss sensors for attention/router/update failure signatures.
<!-- existing:SF-2026-ARXIV-2606-28116:end -->

<!-- delta:SF-2026-ARXIV-2606-28116:start -->
从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。
<!-- delta:SF-2026-ARXIV-2606-28116:end -->

<!-- books-review:SF-2026-ARXIV-2606-28116:start -->
Direct Evolution; Integrate. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal.
<!-- books-review:SF-2026-ARXIV-2606-28116:end -->

<!-- existing:SF-2026-ARXIV-2606-28128:start -->
Ch25 已分离 belief/latent state、action-conditioned transition、physical truth 与 commit authority。 本 family 的 source-specific delta 为：把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。 Fresh adjacent review at books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28128:end -->

<!-- delta:SF-2026-ARXIV-2606-28128:start -->
把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。
<!-- delta:SF-2026-ARXIV-2606-28128:end -->

<!-- books-review:SF-2026-ARXIV-2606-28128:start -->
Principle Reuse; No Change — Existing Coverage. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators.
<!-- books-review:SF-2026-ARXIV-2606-28128:end -->

<!-- existing:SF-2026-ARXIV-2606-28153:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28153:end -->

<!-- delta:SF-2026-ARXIV-2606-28153:start -->
区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。
<!-- delta:SF-2026-ARXIV-2606-28153:end -->

<!-- books-review:SF-2026-ARXIV-2606-28153:start -->
Principle Reuse; No Change — Existing Coverage. To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness.
<!-- books-review:SF-2026-ARXIV-2606-28153:end -->

<!-- existing:SF-2026-ARXIV-2606-28187:start -->
The multi-agent owner already represents interaction edges and attribution/noise boundaries; differentiable connection weights are a local optimizer, not a new coordination owner.
<!-- existing:SF-2026-ARXIV-2606-28187:end -->

<!-- delta:SF-2026-ARXIV-2606-28187:start -->
把 multi-agent interaction 建成可反传 attribution graph，以 token-level influence 分配错误责任。
<!-- delta:SF-2026-ARXIV-2606-28187:end -->

<!-- books-review:SF-2026-ARXIV-2606-28187:start -->
Principle Reuse; No Change — Existing Coverage. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents.
<!-- books-review:SF-2026-ARXIV-2606-28187:end -->

<!-- existing:SF-2026-ARXIV-2606-28235:start -->
Ch84 已把 workspace/runtime、intent、acceptance predicate、trace/replay 与 promotion gate 分开。 本 family 的 source-specific delta 为：用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。 Fresh adjacent review at books/part-07-agent/83-mcp.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28235:end -->

<!-- delta:SF-2026-ARXIV-2606-28235:start -->
用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。
<!-- delta:SF-2026-ARXIV-2606-28235:end -->

<!-- books-review:SF-2026-ARXIV-2606-28235:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》在 IV-B Level of analysis and why multilevel models; V Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28235:end -->

<!-- existing:SF-2026-ARXIV-2606-28276:start -->
The embodied owner warns that simulator success does not prove sim-to-real, but does not bind reconstruction artifact, editable scene variants and real-world rank-validity checks into one promotion chain.
<!-- existing:SF-2026-ARXIV-2606-28276:end -->

<!-- delta:SF-2026-ARXIV-2606-28276:start -->
把 video-to-sim reconstruction、digital cousins、policy training 与 sim-to-real rank validity 绑定。
<!-- delta:SF-2026-ARXIV-2606-28276:end -->

<!-- books-review:SF-2026-ARXIV-2606-28276:start -->
Direct Evolution; Integrate. exact-v1 的结论只覆盖《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》在 SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28276:end -->

<!-- existing:SF-2026-ARXIV-2606-28277:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28277:end -->

<!-- delta:SF-2026-ARXIV-2606-28277:start -->
把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。
<!-- delta:SF-2026-ARXIV-2606-28277:end -->

<!-- books-review:SF-2026-ARXIV-2606-28277:start -->
Principle Reuse; No Change — Existing Coverage. By catching errors early, PAT eases the cognitive burden placed on referees, while preserving their control over the outcomes of the review process.
<!-- books-review:SF-2026-ARXIV-2606-28277:end -->

<!-- existing:SF-2026-ARXIV-2606-28279:start -->
Ch81 已把 artifact state、deterministic interlock、verifier 与 retry/fallback 组织为可提交状态机。 本 family 的 source-specific delta 为：用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。 Fresh adjacent review at books/part-07-agent/80-reflection.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28279:end -->

<!-- delta:SF-2026-ARXIV-2606-28279:start -->
用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。
<!-- delta:SF-2026-ARXIV-2606-28279:end -->

<!-- books-review:SF-2026-ARXIV-2606-28279:start -->
Principle Reuse; No Change — Existing Coverage. However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design.
<!-- books-review:SF-2026-ARXIV-2606-28279:end -->

<!-- existing:SF-2026-ARXIV-2606-28322:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28322:end -->

<!-- delta:SF-2026-ARXIV-2606-28322:start -->
以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。
<!-- delta:SF-2026-ARXIV-2606-28322:end -->

<!-- books-review:SF-2026-ARXIV-2606-28322:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》在 PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28322:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260629-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260629 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260629: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260629-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-27406; review:SF-2026-ARXIV-2606-27409; review:SF-2026-ARXIV-2606-27416; review:SF-2026-ARXIV-2606-27457; review:SF-2026-ARXIV-2606-27472; review:SF-2026-ARXIV-2606-27474; review:SF-2026-ARXIV-2606-27483; review:SF-2026-ARXIV-2606-27492; review:SF-2026-ARXIV-2606-27499; review:SF-2026-ARXIV-2606-27510; review:SF-2026-ARXIV-2606-27511; review:SF-2026-ARXIV-2606-27550; review:SF-2026-ARXIV-2606-27558; review:SF-2026-ARXIV-2606-27567; review:SF-2026-ARXIV-2606-27578; review:SF-2026-ARXIV-2606-27580; review:SF-2026-ARXIV-2606-27595; review:SF-2026-ARXIV-2606-27608; review:SF-2026-ARXIV-2606-27622; review:SF-2026-ARXIV-2606-27632; review:SF-2026-ARXIV-2606-27634; review:SF-2026-ARXIV-2606-27650; review:SF-2026-ARXIV-2606-27669; review:SF-2026-ARXIV-2606-27679; review:SF-2026-ARXIV-2606-27681; review:SF-2026-ARXIV-2606-27683; review:SF-2026-ARXIV-2606-27704; review:SF-2026-ARXIV-2606-27709; review:SF-2026-ARXIV-2606-27732; review:SF-2026-ARXIV-2606-27739; review:SF-2026-ARXIV-2606-27743; review:SF-2026-ARXIV-2606-27757; review:SF-2026-ARXIV-2606-27780; review:SF-2026-ARXIV-2606-27791; review:SF-2026-ARXIV-2606-27797; review:SF-2026-ARXIV-2606-27806; review:SF-2026-ARXIV-2606-27814; review:SF-2026-ARXIV-2606-27826; review:SF-2026-ARXIV-2606-27841; review:SF-2026-ARXIV-2606-27866; review:SF-2026-ARXIV-2606-27906; review:SF-2026-ARXIV-2606-27934; review:SF-2026-ARXIV-2606-27936; review:SF-2026-ARXIV-2606-27944; review:SF-2026-ARXIV-2606-27962; review:SF-2026-ARXIV-2606-27976; review:SF-2026-ARXIV-2606-27997; review:SF-2026-ARXIV-2606-28011; review:SF-2026-ARXIV-2606-28013; review:SF-2026-ARXIV-2606-28037; review:SF-2026-ARXIV-2606-28050; review:SF-2026-ARXIV-2606-28061; review:SF-2026-ARXIV-2606-28070; review:SF-2026-ARXIV-2606-28116; review:SF-2026-ARXIV-2606-28128; review:SF-2026-ARXIV-2606-28153; review:SF-2026-ARXIV-2606-28166; review:SF-2026-ARXIV-2606-28187; review:SF-2026-ARXIV-2606-28235; review:SF-2026-ARXIV-2606-28276; review:SF-2026-ARXIV-2606-28277; review:SF-2026-ARXIV-2606-28279; review:SF-2026-ARXIV-2606-28322 | EVIDENCE-OWNER-REBUILD-20260629: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260629-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-27406; analysis-decision:SF-2026-ARXIV-2606-27409; analysis-decision:SF-2026-ARXIV-2606-27416; analysis-decision:SF-2026-ARXIV-2606-27457; analysis-decision:SF-2026-ARXIV-2606-27472; analysis-decision:SF-2026-ARXIV-2606-27474; analysis-decision:SF-2026-ARXIV-2606-27483; analysis-decision:SF-2026-ARXIV-2606-27492; analysis-decision:SF-2026-ARXIV-2606-27499; analysis-decision:SF-2026-ARXIV-2606-27510; analysis-decision:SF-2026-ARXIV-2606-27511; analysis-decision:SF-2026-ARXIV-2606-27550; analysis-decision:SF-2026-ARXIV-2606-27558; analysis-decision:SF-2026-ARXIV-2606-27567; analysis-decision:SF-2026-ARXIV-2606-27578; analysis-decision:SF-2026-ARXIV-2606-27580; analysis-decision:SF-2026-ARXIV-2606-27595; analysis-decision:SF-2026-ARXIV-2606-27608; analysis-decision:SF-2026-ARXIV-2606-27622; analysis-decision:SF-2026-ARXIV-2606-27632; analysis-decision:SF-2026-ARXIV-2606-27634; analysis-decision:SF-2026-ARXIV-2606-27650; analysis-decision:SF-2026-ARXIV-2606-27669; analysis-decision:SF-2026-ARXIV-2606-27679; analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE; analysis-decision:SF-2026-ARXIV-2606-27683; analysis-decision:SF-2026-ARXIV-2606-27704; analysis-decision:SF-2026-ARXIV-2606-27709; analysis-decision:SF-2026-ARXIV-2606-27732; analysis-decision:SF-2026-ARXIV-2606-27739; analysis-decision:SF-2026-ARXIV-2606-27743; analysis-decision:SF-2026-ARXIV-2606-27757; analysis-decision:SF-2026-ARXIV-2606-27780; analysis-decision:SF-2026-ARXIV-2606-27791; analysis-decision:SF-2026-ARXIV-2606-27797; analysis-decision:SF-2026-ARXIV-2606-27806; analysis-decision:SF-2026-ARXIV-2606-27814; analysis-decision:SF-2026-ARXIV-2606-27826; analysis-decision:SF-2026-ARXIV-2606-27841; analysis-decision:SF-2026-ARXIV-2606-27866; analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE; analysis-decision:SF-2026-ARXIV-2606-27934; analysis-decision:SF-2026-ARXIV-2606-27936; analysis-decision:SF-2026-ARXIV-2606-27944; analysis-decision:SF-2026-ARXIV-2606-27962; analysis-decision:SF-2026-ARXIV-2606-27976; analysis-decision:SF-2026-ARXIV-2606-27997; analysis-decision:SF-2026-ARXIV-2606-28011; analysis-decision:SF-2026-ARXIV-2606-28013; analysis-decision:SF-2026-ARXIV-2606-28037; analysis-decision:SF-2026-ARXIV-2606-28050; analysis-decision:SF-2026-ARXIV-2606-28061; analysis-decision:SF-2026-ARXIV-2606-28070; analysis-decision:SF-2026-ARXIV-2606-28116; analysis-decision:SF-2026-ARXIV-2606-28128; analysis-decision:SF-2026-ARXIV-2606-28153; analysis-decision:SF-2026-ARXIV-2606-28166; analysis-decision:SF-2026-ARXIV-2606-28187; analysis-decision:SF-2026-ARXIV-2606-28235; analysis-decision:SF-2026-ARXIV-2606-28276; analysis-decision:SF-2026-ARXIV-2606-28277; analysis-decision:SF-2026-ARXIV-2606-28279; analysis-decision:SF-2026-ARXIV-2606-28322 | SELECTION-OWNER-REBUILD-20260629: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260629-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-27409; books-review:SF-2026-ARXIV-2606-27457; books-review:SF-2026-ARXIV-2606-27472; books-review:SF-2026-ARXIV-2606-27492; books-review:SF-2026-ARXIV-2606-27558; books-review:SF-2026-ARXIV-2606-27567; books-review:SF-2026-ARXIV-2606-27578; books-review:SF-2026-ARXIV-2606-27580; books-review:SF-2026-ARXIV-2606-27632; books-review:SF-2026-ARXIV-2606-27634; books-review:SF-2026-ARXIV-2606-27650; books-review:SF-2026-ARXIV-2606-27669; books-review:SF-2026-ARXIV-2606-27679; books-review:SF-2026-ARXIV-2606-27681; books-review:SF-2026-ARXIV-2606-27683; books-review:SF-2026-ARXIV-2606-27704; books-review:SF-2026-ARXIV-2606-27709; books-review:SF-2026-ARXIV-2606-27732; books-review:SF-2026-ARXIV-2606-27739; books-review:SF-2026-ARXIV-2606-27743; books-review:SF-2026-ARXIV-2606-27757; books-review:SF-2026-ARXIV-2606-27780; books-review:SF-2026-ARXIV-2606-27797; books-review:SF-2026-ARXIV-2606-27806; books-review:SF-2026-ARXIV-2606-27814; books-review:SF-2026-ARXIV-2606-27826; books-review:SF-2026-ARXIV-2606-27841; books-review:SF-2026-ARXIV-2606-27866; books-review:SF-2026-ARXIV-2606-27906; books-review:SF-2026-ARXIV-2606-27934; books-review:SF-2026-ARXIV-2606-27936; books-review:SF-2026-ARXIV-2606-27944; books-review:SF-2026-ARXIV-2606-27962; books-review:SF-2026-ARXIV-2606-27976; books-review:SF-2026-ARXIV-2606-27997; books-review:SF-2026-ARXIV-2606-28011; books-review:SF-2026-ARXIV-2606-28013; books-review:SF-2026-ARXIV-2606-28037; books-review:SF-2026-ARXIV-2606-28050; books-review:SF-2026-ARXIV-2606-28061; books-review:SF-2026-ARXIV-2606-28070; books-review:SF-2026-ARXIV-2606-28116; books-review:SF-2026-ARXIV-2606-28128; books-review:SF-2026-ARXIV-2606-28153; books-review:SF-2026-ARXIV-2606-28187; books-review:SF-2026-ARXIV-2606-28235; books-review:SF-2026-ARXIV-2606-28276; books-review:SF-2026-ARXIV-2606-28277; books-review:SF-2026-ARXIV-2606-28279; books-review:SF-2026-ARXIV-2606-28322 | BOOKS-OWNER-REBUILD-20260629: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- 86/86 exact-v1 primary full texts resolved; five PDF fallbacks; later versions used=0.

## 9. Recommended Action

- Fresh prewrite disposition: 13 Integrate / 67 No Change / 6 Weekly Only across 9 write owners.
- Under the exclusive write lock, 13 Integrate families were merged into 9 owner files; 67 No Change and 6 Weekly Only families remain absent.

## 10. Repository Changes

- Updated the date-local Daily/source packet/scripts and the nine approved Books owner files; LEARNING_STATE was not changed.

## 11. Open Questions

- Coverage audit complete: 0 FP in the 85 first-freeze retained; 1 FN in the 177 closures (2606.29328) reinstated; final denominator 86/176.
- None; 86/86 post-write fresh audit found zero unresolved finding.

## 12. Sources

- [Towards Evaluation of Implicit Software World Models in Coding LLMs](https://arxiv.org/abs/2606.27406v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement](https://arxiv.org/abs/2606.27409v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents](https://arxiv.org/abs/2606.27416v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving](https://arxiv.org/abs/2606.27457v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents](https://arxiv.org/abs/2606.27472v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Speculative Refinement: A Hybrid Autoregressive Diffusion Decoding Strategy and Its Behavior Across Benchmarks](https://arxiv.org/abs/2606.27474v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning](https://arxiv.org/abs/2606.27483v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems](https://arxiv.org/abs/2606.27492v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection](https://arxiv.org/abs/2606.27499v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching](https://arxiv.org/abs/2606.27510v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems](https://arxiv.org/abs/2606.27511v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction](https://arxiv.org/abs/2606.27550v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Productionized Fairness Measurement Under Privacy Constraints](https://arxiv.org/abs/2606.27558v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/abs/2606.27567v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration](https://arxiv.org/abs/2606.27578v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF](https://arxiv.org/abs/2606.27580v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents](https://arxiv.org/abs/2606.27595v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Qwen-Image-2.0-RL Technical Report](https://arxiv.org/abs/2606.27608v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks](https://arxiv.org/abs/2606.27622v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety](https://arxiv.org/abs/2606.27632v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis](https://arxiv.org/abs/2606.27634v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies](https://arxiv.org/abs/2606.27650v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search](https://arxiv.org/abs/2606.27669v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models](https://arxiv.org/abs/2606.27679v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation](https://arxiv.org/abs/2606.27681v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence](https://arxiv.org/abs/2606.27683v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis](https://arxiv.org/abs/2606.27704v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning](https://arxiv.org/abs/2606.27709v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation](https://arxiv.org/abs/2606.27732v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment](https://arxiv.org/abs/2606.27739v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference](https://arxiv.org/abs/2606.27743v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework](https://arxiv.org/abs/2606.27757v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Understanding Rollout Error in Graph World Models](https://arxiv.org/abs/2606.27780v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation](https://arxiv.org/abs/2606.27791v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems](https://arxiv.org/abs/2606.27797v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents](https://arxiv.org/abs/2606.27806v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2606.27814v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms](https://arxiv.org/abs/2606.27826v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks](https://arxiv.org/abs/2606.27841v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models](https://arxiv.org/abs/2606.27866v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC](https://arxiv.org/abs/2606.27906v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking](https://arxiv.org/abs/2606.27934v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy](https://arxiv.org/abs/2606.27936v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents](https://arxiv.org/abs/2606.27944v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence](https://arxiv.org/abs/2606.27962v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval](https://arxiv.org/abs/2606.27976v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings](https://arxiv.org/abs/2606.27997v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [From Detection to Action: Using LLM Agents for Fault-Tolerant Control](https://arxiv.org/abs/2606.28011v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](https://arxiv.org/abs/2606.28013v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors](https://arxiv.org/abs/2606.28037v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA](https://arxiv.org/abs/2606.28050v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents](https://arxiv.org/abs/2606.28061v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications](https://arxiv.org/abs/2606.28070v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability](https://arxiv.org/abs/2606.28116v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](https://arxiv.org/abs/2606.28128v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models](https://arxiv.org/abs/2606.28153v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Tandem Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2606.28166v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems](https://arxiv.org/abs/2606.28187v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software](https://arxiv.org/abs/2606.28235v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](https://arxiv.org/abs/2606.28276v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Towards Automating Scientific Review with Google's Paper Assistant Tool](https://arxiv.org/abs/2606.28277v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [Agentic Hardware Design as Repository-Level Code Evolution](https://arxiv.org/abs/2606.28279v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
- [PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception](https://arxiv.org/abs/2606.28322v1) — first-public（Asia/Shanghai）：2026-06-29；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=1。
