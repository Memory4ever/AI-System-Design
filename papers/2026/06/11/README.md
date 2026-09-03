# Daily Research — 2026-06-11

**Research Date:** 2026-06-11

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-10 09:00:00 ～ 2026-06-11 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；559/559 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
> Strict V2.1 reconstruction for `DEN-20260611-559031`. Books writeback was serialized through root; this lane performed the independent post-write audit.

The Beijing window contains 559 registered arXiv identities. Full 559/559 title+abstract semantic screening freezes 31 durable AI-system families and 528 row-specific closures. All 31 exact-v1 Reviews, benchmark contracts and full-frontier selection decisions pass fresh semantic audit. Root merged 26 Integrate families into 12 unique owners; five No Change families were rechecked against existing owner/adjacent coverage. The 31/31 post-write fresh-context audit resolved one Daily-only owner finding for 2606.12370 and closed Books Gate.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-11 |
| Window End | 2026-06-11 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260611-559031 |
| Denominator Frozen At | 2026-08-29T23:15:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-10T09:00:00+08:00 | 2026-06-11T09:00:00+08:00 | 2026-08-29T23:15:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 562 | SF-2026-ARXIV-2606-11257;SF-2026-ARXIV-2606-11265;SF-2026-ARXIV-2606-11270;SF-2026-ARXIV-2606-11290;SF-2026-ARXIV-2606-11349;SF-2026-ARXIV-2606-11357;SF-2026-ARXIV-2606-11375;SF-2026-ARXIV-2606-11387;SF-2026-ARXIV-2606-11409;SF-2026-ARXIV-2606-11445;SF-2026-ARXIV-2606-11520;SF-2026-ARXIV-2606-11522;SF-2026-ARXIV-2606-11543;SF-2026-ARXIV-2606-11632;SF-2026-ARXIV-2606-11671;SF-2026-ARXIV-2606-11686;SF-2026-ARXIV-2606-11688;SF-2026-ARXIV-2606-11690;SF-2026-ARXIV-2606-11718;SF-2026-ARXIV-2606-11806;SF-2026-ARXIV-2606-11871;SF-2026-ARXIV-2606-11878;SF-2026-ARXIV-2606-11916;SF-2026-ARXIV-2606-11949;SF-2026-ARXIV-2606-11998;SF-2026-ARXIV-2606-12243;SF-2026-ARXIV-2606-12320;SF-2026-ARXIV-2606-12329;SF-2026-ARXIV-2606-12370 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260611/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260611; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260611 |
<!-- coverage:SRC-ARXIV:20260611:start -->
All 559 identities were read at title+abstract level. Full-retain and full-closure surfaces were audited; keyword routes were not used as admission decisions. Frozen result: 31 retained, 528 closures.
<!-- coverage:SRC-ARXIV:20260611:end -->


<!-- latest-contract-reopen:2026-06-11:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-11:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **562** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **29** 条是旧报告 retained provenance，**533** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11257 | arXiv:2606.11257v1 | paper-v1:2606.11257 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11257 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-11257 | yes |
| SF-2026-ARXIV-2606-11265 | arXiv:2606.11265v1 | paper-v1:2606.11265 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11265 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11265 | yes |
| SF-2026-ARXIV-2606-11270 | arXiv:2606.11270v1 | paper-v1:2606.11270 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11270 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11270 | yes |
| SF-2026-ARXIV-2606-11290 | arXiv:2606.11290v1 | paper-v1:2606.11290 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11290 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11290 | yes |
| SF-2026-ARXIV-2606-11349 | arXiv:2606.11349v1 | paper-v1:2606.11349 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11349 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11349 | yes |
| SF-2026-ARXIV-2606-11357 | arXiv:2606.11357v1 | paper-v1:2606.11357 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11357 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11357 | yes |
| SF-2026-ARXIV-2606-11375 | arXiv:2606.11375v1 | paper-v1:2606.11375 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11375 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11375 | yes |
| SF-2026-ARXIV-2606-11387 | arXiv:2606.11387v1 | paper-v1:2606.11387 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11387 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2606-11387 | yes |
| SF-2026-ARXIV-2606-11409 | arXiv:2606.11409v1 | paper-v1:2606.11409 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11409 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11409 | yes |
| SF-2026-ARXIV-2606-11445 | arXiv:2606.11445v1 | paper-v1:2606.11445 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11445 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11445 | yes |
| SF-2026-ARXIV-2606-11520 | arXiv:2606.11520v1 | paper-v1:2606.11520 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11520 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11520 | yes |
| SF-2026-ARXIV-2606-11522 | arXiv:2606.11522v1 | paper-v1:2606.11522 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11522 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-11522 | yes |
| SF-2026-ARXIV-2606-11543 | arXiv:2606.11543v1 | paper-v1:2606.11543 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11543 | self | — | new_in_window | AGENT-REFLECTION | Integrate | books-review:SF-2026-ARXIV-2606-11543 | yes |
| SF-2026-ARXIV-2606-11632 | arXiv:2606.11632v1 | paper-v1:2606.11632 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11632 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11632 | yes |
| SF-2026-ARXIV-2606-11671 | arXiv:2606.11671v1 | paper-v1:2606.11671 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11671 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11671 | yes |
| SF-2026-ARXIV-2606-11686 | arXiv:2606.11686v1 | paper-v1:2606.11686 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11686 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-11686 | yes |
| SF-2026-ARXIV-2606-11688 | arXiv:2606.11688v1 | paper-v1:2606.11688 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11688 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-11688 | yes |
| SF-2026-ARXIV-2606-11690 | arXiv:2606.11690v1 | paper-v1:2606.11690 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11690 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2606-11690 | yes |
| SF-2026-ARXIV-2606-11718 | arXiv:2606.11718v1 | paper-v1:2606.11718 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11718 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-11718 | yes |
| SF-2026-ARXIV-2606-11806 | arXiv:2606.11806v1 | paper-v1:2606.11806 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11806 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-11806 | yes |
| SF-2026-ARXIV-2606-11871 | arXiv:2606.11871v1 | paper-v1:2606.11871 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11871 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11871 | yes |
| SF-2026-ARXIV-2606-11878 | arXiv:2606.11878v1 | paper-v1:2606.11878 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11878 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11878 | yes |
| SF-2026-ARXIV-2606-11916 | arXiv:2606.11916v1 | paper-v1:2606.11916 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11916 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-11916 | yes |
| SF-2026-ARXIV-2606-11949 | arXiv:2606.11949v1 | paper-v1:2606.11949 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11949 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-11949 | yes |
| SF-2026-ARXIV-2606-11998 | arXiv:2606.11998v1 | paper-v1:2606.11998 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-11998 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-11998 | yes |
| SF-2026-ARXIV-2606-12243 | arXiv:2606.12243v1 | paper-v1:2606.12243 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12243 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12243 | yes |
| SF-2026-ARXIV-2606-12320 | arXiv:2606.12320v1 | paper-v1:2606.12320 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12320 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-12320 | yes |
| SF-2026-ARXIV-2606-12329 | arXiv:2606.12329v1 | paper-v1:2606.12329 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12329 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-12329 | yes |
| SF-2026-ARXIV-2606-12370 | arXiv:2606.12370v1 | paper-v1:2606.12370 | 2026-W24 | 2026-06-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-12370 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12370 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11257 | RP-7416a312efaa02aa | deep | arXiv:2606.11257v1 | SRC-ARXIV@arXiv:2606.11257v1 | https://arxiv.org/html/2606.11257v1 — §III System Design | https://arxiv.org/html/2606.11257v1 — §IV–V Experimental Setup and Results | https://arxiv.org/html/2606.11257v1 — §VI-B Limitations and Future Work | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11257 | complete |
| SF-2026-ARXIV-2606-11265 | RP-bc343613f8fe9dc3 | deep | arXiv:2606.11265v1 | SRC-ARXIV@arXiv:2606.11265v1 | https://arxiv.org/html/2606.11265v1 — §IV Methodology | https://arxiv.org/html/2606.11265v1 — §V Experiment | https://arxiv.org/html/2606.11265v1 — §III Threat Model and §VI Conclusion | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11265 | complete |
| SF-2026-ARXIV-2606-11270 | RP-cd7e36580346407e | deep | arXiv:2606.11270v1 | SRC-ARXIV@arXiv:2606.11270v1 | https://arxiv.org/html/2606.11270v1 — §3 Methodology | https://arxiv.org/html/2606.11270v1 — §4 Experiments and Results | https://arxiv.org/html/2606.11270v1 — §5 Analysis and §6 Conclusion | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11270 | complete |
| SF-2026-ARXIV-2606-11290 | RP-01f6fb11a7cb6692 | deep | arXiv:2606.11290v1 | SRC-ARXIV@arXiv:2606.11290v1 | https://arxiv.org/html/2606.11290v1 — §3 Methodology | https://arxiv.org/html/2606.11290v1 — §4 Experiments | https://arxiv.org/html/2606.11290v1 — Appendix F.1 Limitations | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11290 | complete |
| SF-2026-ARXIV-2606-11349 | RP-8636496ad0fd6ed1 | deep | arXiv:2606.11349v1 | SRC-ARXIV@arXiv:2606.11349v1 | https://arxiv.org/html/2606.11349v1 — §3 Framework | https://arxiv.org/html/2606.11349v1 — §§4–5 Experiments and Results | https://arxiv.org/html/2606.11349v1 — §6 Discussion | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11349 | complete |
| SF-2026-ARXIV-2606-11357 | RP-b026917f348215a6 | deep | arXiv:2606.11357v1 | SRC-ARXIV@arXiv:2606.11357v1 | https://arxiv.org/html/2606.11357v1 — §4 TileFuse Overview | https://arxiv.org/html/2606.11357v1 — §5 Evaluation | https://arxiv.org/html/2606.11357v1 — §6 Discussion and Limitations | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11357 | complete |
| SF-2026-ARXIV-2606-11375 | RP-5a798bc0d88d8216 | deep | arXiv:2606.11375v1 | SRC-ARXIV@arXiv:2606.11375v1 | https://arxiv.org/html/2606.11375v1 — §3 Methodology | https://arxiv.org/html/2606.11375v1 — §4 Results | https://arxiv.org/html/2606.11375v1 — §5.3 Limitations | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11375 | complete |
| SF-2026-ARXIV-2606-11387 | RP-1c6b49bf807718bb | deep | arXiv:2606.11387v1 | SRC-ARXIV@arXiv:2606.11387v1 | https://arxiv.org/html/2606.11387v1 — §4.3–4.4 Promotion Schedule and Frozen Rules | https://arxiv.org/html/2606.11387v1 — §5 Results | https://arxiv.org/html/2606.11387v1 — §7 Limitations | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11387 | complete |
| SF-2026-ARXIV-2606-11409 | RP-d51c0fe5f3e7d971 | deep | arXiv:2606.11409v1 | SRC-ARXIV@arXiv:2606.11409v1 | https://arxiv.org/html/2606.11409v1 — §2 Framework | https://arxiv.org/html/2606.11409v1 — §3–4 Experimental Setup and Results | https://arxiv.org/html/2606.11409v1 — §7 Future Work & Limitations | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11409 | complete |
| SF-2026-ARXIV-2606-11445 | RP-52dc37bbb44d5674 | deep | arXiv:2606.11445v1 | SRC-ARXIV@arXiv:2606.11445v1 | https://arxiv.org/html/2606.11445v1 — §3 Method | https://arxiv.org/html/2606.11445v1 — §§4–5 evaluation and ablation | https://arxiv.org/html/2606.11445v1 — §7 Limitations | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11445 | complete |
| SF-2026-ARXIV-2606-11520 | RP-557ed1728ca241f5 | deep | arXiv:2606.11520v1 | SRC-ARXIV@arXiv:2606.11520v1 | https://arxiv.org/html/2606.11520v1 — §4 ISE Synthesis Paradigm | https://arxiv.org/html/2606.11520v1 — §5 Experiments | https://arxiv.org/html/2606.11520v1 — §6 Limitations | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11520 | complete |
| SF-2026-ARXIV-2606-11522 | RP-e60ea4b6c8f2900b | deep | arXiv:2606.11522v1 | SRC-ARXIV@arXiv:2606.11522v1 | https://arxiv.org/html/2606.11522v1 — §3 Search discipline and control loop | https://arxiv.org/html/2606.11522v1 — §4 Evaluation | https://arxiv.org/html/2606.11522v1 — §5 Discussion | Not Disclosed — immutable event-time artifact commit not required for manuscript claim | claim:SF-2026-ARXIV-2606-11522 | complete |
| SF-2026-ARXIV-2606-11543 | RP-996ddbe635b42759 | deep | arXiv:2606.11543v1 | SRC-ARXIV@arXiv:2606.11543v1 | arXiv:2606.11543v1 §3 Method; §§3.2–3.4 controlled variants/runtime evidence | arXiv:2606.11543v1 §4 Experiments; §4.1 setup; §§4.2–4.5 | arXiv:2606.11543v1 §6 Limitations; Appendix E layout sensitivity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11543 | complete |
| SF-2026-ARXIV-2606-11632 | RP-4e9fd9e26590524b | deep | arXiv:2606.11632v1 | SRC-ARXIV@arXiv:2606.11632v1 | arXiv:2606.11632v1 §§3–5 SAB model, airlock and broker | arXiv:2606.11632v1 §7 Evaluation Methodology and Targets; §7.3 setup | arXiv:2606.11632v1 §9 Discussion and Limitations; §9.2 | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11632 | complete |
| SF-2026-ARXIV-2606-11671 | RP-cb041cc73e0cfe1f | deep | arXiv:2606.11671v1 | SRC-ARXIV@arXiv:2606.11671v1 | arXiv:2606.11671v1 §3 Runtime Skill Audit; §4 implementation | arXiv:2606.11671v1 §5 Evaluation | arXiv:2606.11671v1 §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11671 | complete |
| SF-2026-ARXIV-2606-11686 | RP-0ce3f06f8207f473 | deep | arXiv:2606.11686v1 | SRC-ARXIV@arXiv:2606.11686v1 | arXiv:2606.11686v1 §3 Layer-Isolated Evaluation; taxonomy and pure mode | arXiv:2606.11686v1 §4 Evaluation; controlled regression injection | arXiv:2606.11686v1 §5 Discussion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11686 | complete |
| SF-2026-ARXIV-2606-11688 | RP-4a4a6c0c5ab9aedf | deep | arXiv:2606.11688v1 | SRC-ARXIV@arXiv:2606.11688v1 | arXiv:2606.11688v1 §3 Method; §4 theorem; §5 System | arXiv:2606.11688v1 §6 Empirical evaluation; §6.5 scaled corpus | arXiv:2606.11688v1 §7 Limitations; Appendix A auditor boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11688 | complete |
| SF-2026-ARXIV-2606-11690 | RP-0181f38c7f1189ab | deep | arXiv:2606.11690v1 | SRC-ARXIV@arXiv:2606.11690v1 | arXiv:2606.11690v1 §3 Concurrency-Aware Cost Framework | arXiv:2606.11690v1 §4 Experimental Setup; §5 Results | arXiv:2606.11690v1 §6.8 Scope; §6.9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11690 | complete |
| SF-2026-ARXIV-2606-11718 | RP-69008b395e54945b | deep | arXiv:2606.11718v1 | SRC-ARXIV@arXiv:2606.11718v1 | arXiv:2606.11718v1 §III Chiplet-Contiguous Layout | arXiv:2606.11718v1 §IV Evaluation; §IV-A methodology | arXiv:2606.11718v1 §V Conclusion; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11718 | complete |
| SF-2026-ARXIV-2606-11806 | RP-e59717310c0c9142 | deep | arXiv:2606.11806v1 | SRC-ARXIV@arXiv:2606.11806v1 | arXiv:2606.11806v1 §3 Experience Serving in Production | arXiv:2606.11806v1 §4 setup; §5 Results; Appendices E–G | arXiv:2606.11806v1 §4.4 claim boundary; Appendix H interpretation scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11806 | complete |
| SF-2026-ARXIV-2606-11871 | RP-ef1e562ab221a22b | deep | arXiv:2606.11871v1 | SRC-ARXIV@arXiv:2606.11871v1 | arXiv:2606.11871v1 §III threat model; §§IV–V design/implementation | arXiv:2606.11871v1 §VI Evaluation; §VII backend cost | arXiv:2606.11871v1 §VI-H portability boundaries; §VIII Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11871 | complete |
| SF-2026-ARXIV-2606-11878 | RP-32f0c5e2c40380f3 | deep | arXiv:2606.11878v1 | SRC-ARXIV@arXiv:2606.11878v1 | arXiv:2606.11878v1 §§III–V participation authority and CSC | arXiv:2606.11878v1 §VI evidence; §VII-D mitigation results | arXiv:2606.11878v1 §VII-E Cost and Limits; §VIII Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11878 | complete |
| SF-2026-ARXIV-2606-11916 | RP-4c1dd32fa7aadd61 | deep | arXiv:2606.11916v1 | SRC-ARXIV@arXiv:2606.11916v1 | arXiv:2606.11916v1 §III Methodology | arXiv:2606.11916v1 §IV Results; §§IV-A–IV-E | arXiv:2606.11916v1 §V Threats to Validity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11916 | complete |
| SF-2026-ARXIV-2606-11949 | RP-cbb84c907331e88b | deep | arXiv:2606.11949v1 | SRC-ARXIV@arXiv:2606.11949v1 | arXiv:2606.11949v1 §3 Methods; §§3.1–3.10 | arXiv:2606.11949v1 §4 setup; §5 Results | arXiv:2606.11949v1 §6.5 Limitations; §5.4 ground-truth regimes | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11949 | complete |
| SF-2026-ARXIV-2606-11998 | RP-a0357c5c1450f9fc | deep | arXiv:2606.11998v1 | SRC-ARXIV@arXiv:2606.11998v1 | arXiv:2606.11998v1 §3 Methods; §3.1 threat model/protocol | arXiv:2606.11998v1 §4 Results; Appendix C red/blue teaming | arXiv:2606.11998v1 §5 Discussion, Transparent CoT assumption and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-11998 | complete |
| SF-2026-ARXIV-2606-12243 | RP-e1d58c24fbbef53e | deep | arXiv:2606.12243v1 | SRC-ARXIV@arXiv:2606.12243v1 | arXiv:2606.12243v1 §3 Methodology; §§3.2–3.5 | arXiv:2606.12243v1 §4 Experiments | arXiv:2606.12243v1 §4.4 additional analysis; §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12243 | complete |
| SF-2026-ARXIV-2606-12320 | RP-c7a9413d6eff0ccb | deep | arXiv:2606.12320v1 | SRC-ARXIV@arXiv:2606.12320v1 | arXiv:2606.12320v1 §§3–8 threat model, five planes and composed architecture | arXiv:2606.12320v1 §9 case studies; §10 validation roadmap | arXiv:2606.12320v1 §11 Limitations and Open Questions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12320 | complete |
| SF-2026-ARXIV-2606-12329 | RP-6a541eae325447a5 | deep | arXiv:2606.12329v1 | SRC-ARXIV@arXiv:2606.12329v1 | arXiv:2606.12329v1 §3 System Design; §§4–6 architecture/implementation | arXiv:2606.12329v1 §7 Evaluation | arXiv:2606.12329v1 §8 Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12329 | complete |
| SF-2026-ARXIV-2606-12370 | RP-71b997b43c07d9de | deep | arXiv:2606.12370v1 | SRC-ARXIV@arXiv:2606.12370v1 | arXiv:2606.12370v1 §§3–5 entropy bound, TV loss and adaptation | arXiv:2606.12370v1 §6 Experiments | arXiv:2606.12370v1 §7.8 top-k instability; §9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-12370 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-11257:start -->
<!-- claim:SF-2026-ARXIV-2606-11257:start -->
`Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11257v1`：Retrieval-Augmented Generation (RAG) pipelines are compute-intensive, combining embedding, retrieval, reranking, and large language model (LLM) generation.

机制与 owner：Keep embedding, reranking and generation on the Snapdragon Hexagon NPU and measure the entire RAG energy/latency path rather than one isolated operator. 状态/数据/控制 owner 固定为 `INFER-GPU-MEMORY`；Method 锚点是 `§III System Design`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§IV–V Experimental Setup and Results` 只证明 `End-to-end indexing plus 120 Wikipedia-passage queries; embedding, retrieval, reranking and generation` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Dell XPS 13, Snapdragon X Elite Hexagon NPU; CPU and Adreno/OpenCL GPU baselines`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Latency and energy are measured outcomes, not acceptance SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Results are one Dell XPS 13 / Snapdragon X Elite stack and a 120-query corpus; extrapolation to Apple, Intel or MediaTek NPUs is explicitly unproven. 反证/外推边界在 `§VI-B Limitations and Future Work`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11257:end -->
<!-- review:SF-2026-ARXIV-2606-11257:end -->

<!-- review:SF-2026-ARXIV-2606-11265:start -->
<!-- claim:SF-2026-ARXIV-2606-11265:start -->
`When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11265v1`：Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection.

机制与 owner：Evaluate corpus poisoning after the real chunking and reranking pipeline, distinguishing retrieval exposure from whether the generator follows a poisoned chunk. 状态/数据/控制 owner 固定为 `AGENT-RAG`；Method 锚点是 `§IV Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§V Experiment` 只证明 `Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Attack success depends on retriever, chunk and generator settings; a failed poison under one pipeline does not certify the corpus or other retrieval depths. 反证/外推边界在 `§III Threat Model and §VI Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11265:end -->
<!-- review:SF-2026-ARXIV-2606-11265:end -->

<!-- review:SF-2026-ARXIV-2606-11270:start -->
<!-- claim:SF-2026-ARXIV-2606-11270:start -->
`Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11270v1`：Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning.

机制与 owner：Measure subliminal behavior transfer through distillation as a ratio conditioned on teacher behavior and student response rather than treating matching outputs as benign data. 状态/数据/控制 owner 固定为 `TRAIN-DATA`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments and Results` 只证明 `Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning.` 上、`Llama-2-7B-Chat and Qwen2.5-7B-Instruct teachers/students; GPT-4.1 evaluator` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Observed transfer ratios are model/task specific and do not identify every causal feature; data lineage and behavioral canaries must coexist with aggregate metrics. 反证/外推边界在 `§5 Analysis and §6 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11270:end -->
<!-- review:SF-2026-ARXIV-2606-11270:end -->

<!-- review:SF-2026-ARXIV-2606-11290:start -->
<!-- claim:SF-2026-ARXIV-2606-11290:start -->
`FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11290v1`：Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off.

机制与 owner：Precompute reusable workflow fragments into a bank and choose them per query, separating expensive workflow search from repeated online execution. 状态/数据/控制 owner 固定为 `AGENT-WORKFLOW`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off.` 上、`Qwen3-8B FlowBank optimizer; GPT-4o and Qwen3-8B optimizer baselines` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A stale bank can reuse the wrong flow and query adaptation still needs validation; unconstrained online search remains the fallback for novel tasks. 反证/外推边界在 `Appendix F.1 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11290:end -->
<!-- review:SF-2026-ARXIV-2606-11290:end -->

<!-- review:SF-2026-ARXIV-2606-11349:start -->
<!-- claim:SF-2026-ARXIV-2606-11349:start -->
`Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11349v1`：In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information.

机制与 owner：Make clarification a self-gated action competing with navigation on the same ordinal scale so information-seeking becomes an observable policy decision. 状态/数据/控制 owner 固定为 `AGENT-PLANNING`；Method 锚点是 `§3 Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–5 Experiments and Results` 只证明 `In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The measured shift depends on benchmark information gaps and answer-channel quality; asking more questions is not itself evidence of better deployment behavior. 反证/外推边界在 `§6 Discussion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11349:end -->
<!-- review:SF-2026-ARXIV-2606-11349:end -->

<!-- review:SF-2026-ARXIV-2606-11357:start -->
<!-- claim:SF-2026-ARXIV-2606-11357:start -->
`TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11357v1`：With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets.

机制与 owner：Fuse mixed-precision quantized LLM operators around AMD NPU tile/dataflow constraints instead of composing generic kernels with repeated layout conversion. 状态/数据/控制 owner 固定为 `INFER-DECODE`；Method 锚点是 `§4 TileFuse Overview`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Evaluation` 只证明 `With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets.` 上、`Gemma 2B and Qwen2.5 3B end-to-end LLM workloads` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Kernel gains are bound to the evaluated AMD NPU and quantization formats; unsupported shapes and quality effects require fallback kernels and model-level checks. 反证/外推边界在 `§6 Discussion and Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11357:end -->
<!-- review:SF-2026-ARXIV-2606-11357:end -->

<!-- review:SF-2026-ARXIV-2606-11375:start -->
<!-- claim:SF-2026-ARXIV-2606-11375:start -->
`When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11375v1`：Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy.

机制与 owner：Add perturbation fragility after linear-probe accuracy saturates, so pretraining checkpoints with equal separability can still be distinguished by representation stability. 状态/数据/控制 owner 固定为 `TRAIN-PRETRAINING`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Results` 只证明 `Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy.` 上、`OLMo-2 1B and OLMo-3 7B checkpoints` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Fragility depends on probe, perturbation and layer choice and is not a training objective by itself; downstream evaluation still owns usefulness. 反证/外推边界在 `§5.3 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11375:end -->
<!-- review:SF-2026-ARXIV-2606-11375:end -->

<!-- review:SF-2026-ARXIV-2606-11387:start -->
<!-- claim:SF-2026-ARXIV-2606-11387:start -->
`Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11387v1`：Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets.

机制与 owner：Use small controlled pretraining experiments as promotion receipts before expensive runs, with explicit continuation/stop decisions instead of scaling every hypothesis. 状态/数据/控制 owner 固定为 `TRAIN-PRETRAINING`；Method 锚点是 `§4.3–4.4 Promotion Schedule and Frozen Rules`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Results` 只证明 `Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Micro-scale rank order can invert at scale and cheap experiments omit distributed effects; staged promotion reduces decision cost but cannot guarantee final-model quality. 反证/外推边界在 `§7 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11387:end -->
<!-- review:SF-2026-ARXIV-2606-11387:end -->

<!-- review:SF-2026-ARXIV-2606-11409:start -->
<!-- claim:SF-2026-ARXIV-2606-11409:start -->
`Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11409v1`：Adversarial robustness evaluations of large language models (LLMs) typically report attack success rate (ASR) under fixed query budgets, implicitly treating all attacks as equally costly.

机制与 owner：Parameterize adversarial risk by cumulative attack FLOPs and report risk-compute curves, not only success at an equal query count. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§2 Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§3–4 Experimental Setup and Results` 只证明 `Three attack strategies on two jailbreak benchmarks, re-parameterized by cumulative FLOPs` 上、`Ten models across three families and four training/alignment stages` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Risk-compute curves are evaluation objects, not service SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：FLOPs omit hardware, latency and monetary factors and attacker strategies can transfer; it is a comparable pressure proxy, not a production security SLO. 反证/外推边界在 `§7 Future Work & Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11409:end -->
<!-- review:SF-2026-ARXIV-2606-11409:end -->

<!-- review:SF-2026-ARXIV-2606-11445:start -->
<!-- claim:SF-2026-ARXIV-2606-11445:start -->
`Forecasting Future Behavior as a Learning Task` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11445v1`：Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs.

机制与 owner：Train a single-pass behavior forecaster directly on reasoning trajectories to predict rerun stability and response changes without pretending the trace is a faithful explanation. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§3 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–5 evaluation and ablation` 只证明 `Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs.` 上、`OLMo-3-7B-Think and Qwen3.5-2B target LRMs; GPT-5.4 and Claude Opus 4.6 naive readers` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Forecast accuracy is limited to trained behavior questions and model distributions; a forecaster predicts outcomes but does not explain causes or authorize actions. 反证/外推边界在 `§7 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11445:end -->
<!-- review:SF-2026-ARXIV-2606-11445:end -->

<!-- review:SF-2026-ARXIV-2606-11520:start -->
<!-- claim:SF-2026-ARXIV-2606-11520:start -->
`ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11520v1`：Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets.

机制与 owner：Synthesize OS-agent data through structured intent, role-locked multi-turn simulation and execution of every tool call in an isolated live workspace. 状态/数据/控制 owner 固定为 `TRAIN-DATA`；Method 锚点是 `§4 ISE Synthesis Paradigm`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Experiments` 只证明 `Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets.` 上、`Qwen3-8B fine-tuned model; Qwen3-8B, Qwen3-32B, and GPT-4o references` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A generated intent distribution and one workspace image can miss real-user states; execution grounding proves tool effects in that sandbox, not external safety. 反证/外推边界在 `§6 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11520:end -->
<!-- review:SF-2026-ARXIV-2606-11520:end -->

<!-- review:SF-2026-ARXIV-2606-11522:start -->
<!-- claim:SF-2026-ARXIV-2606-11522:start -->
`Search Discipline for Long-Horizon Research Agents` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11522v1`：Autoresearch agents now propose, evaluate, and select scientific candidates against a metric, and that metric is usually an aggregate reduced over a heterogeneous space of regions, slices, or cohorts.

机制与 owner：Move candidate acceptance out of the metric-optimizing research agent into an external controller that audits disaggregated regions/slices before commit. 状态/数据/控制 owner 固定为 `AGENT-PLATFORM`；Method 锚点是 `§3 Search discipline and control loop`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Evaluation` 只证明 `Autoresearch agents now propose, evaluate, and select scientific candidates against a metric, and that metric is usually an aggregate reduced over a heterogeneous space of regions, slices, or cohorts.` 上、`Not applicable: fire-model research-control case, no evaluated LM checkpoint asserted` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The fire-model case demonstrates aggregate inversion but not every science domain; protected slices and noise tolerances remain domain-owned policy. 反证/外推边界在 `§5 Discussion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11522:end -->
<!-- review:SF-2026-ARXIV-2606-11522:end -->

<!-- review:SF-2026-ARXIV-2606-11543:start -->
### 2606.11543 — SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。

**State / data / control owner。** `AGENT-REFLECTION` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11543v1 §4 Experiments; §4.1 setup; §§4.2–4.5` 支持 `82 SkillsBench tasks × 3 conditions × 5 trials`；模型 `GPT-5.4 high reasoning`；硬件 `Not Disclosed — hosted runtime hardware is not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11543v1 §3 Method; §§3.2–3.4 controlled variants/runtime evidence`；counterevidence locator：`arXiv:2606.11543v1 §6 Limitations; Appendix E layout sensitivity`。

**Trade-off / failure / coexistence / evolution。** 按需资源降低入口负担但可能产生 fanout tax；精确格式、阈值或长 artifact pipeline 仍适合 flat/local instructions。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11543:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11543v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11543:end -->
<!-- review:SF-2026-ARXIV-2606-11543:end -->

<!-- review:SF-2026-ARXIV-2606-11632:start -->
### 2606.11632 — Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11632v1 §7 Evaluation Methodology and Targets; §7.3 setup` 支持 `500 contracts × five trials; 2,500 admissions`；模型 `Go SAB prototype, OPA, PostgreSQL ledger, three-validator SQA`；硬件 `Single-node local workstation; exact CPU/GPU not disclosed`；精度 `Not applicable — control-plane prototype`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11632v1 §§3–5 SAB model, airlock and broker`；counterevidence locator：`arXiv:2606.11632v1 §9 Discussion and Limitations; §9.2`。

**Trade-off / failure / coexistence / evolution。** 证书化增加 admission latency 和 TCB；证据陈旧、policy/validator 漂移或 emergency bypass 会破坏保证，IAM 仍保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11632:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11632v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11632:end -->
<!-- review:SF-2026-ARXIV-2606-11632:end -->

<!-- review:SF-2026-ARXIV-2606-11671:start -->
### 2606.11671 — Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11671v1 §5 Evaluation` 支持 `100 OpenClaw skills with static baselines and evolving attacks`；模型 `LLM-assisted profiler/task generator/trace judge; exact models not fully disclosed`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11671v1 §3 Runtime Skill Audit; §4 implementation`；counterevidence locator：`arXiv:2606.11671v1 §7 Limitations`。

**Trade-off / failure / coexistence / evolution。** 动态探测覆盖 context-dependent behavior，却不穷尽 trigger；模型化 task/judge 会漂移，静态扫描仍是廉价第一层。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11671:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11671v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11671:end -->
<!-- review:SF-2026-ARXIV-2606-11671:end -->

<!-- review:SF-2026-ARXIV-2606-11686:start -->
### 2606.11686 — Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11686v1 §4 Evaluation; controlled regression injection` 支持 `238 cases across 23 slices; seven injected regressions; two tenants`；模型 `No-LLM deterministic ordering-agent scaffold`；硬件 `Not Disclosed`；精度 `Not applicable — deterministic harness`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11686v1 §3 Layer-Isolated Evaluation; taxonomy and pure mode`；counterevidence locator：`arXiv:2606.11686v1 §5 Discussion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 分层 gate 定位快但只覆盖显式 scaffold；端到端 stochastic behavior 与未被 exercise 的 layer 仍需独立评测。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11686:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11686v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11686:end -->
<!-- review:SF-2026-ARXIV-2606-11686:end -->

<!-- review:SF-2026-ARXIV-2606-11688:start -->
### 2606.11688 — Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。

**State / data / control owner。** `AGENT-WORKFLOW` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11688v1 §6 Empirical evaluation; §6.5 scaled corpus` 支持 `3,150 paired cells; 70 tasks including 50 SWE-bench Lite`；模型 `Three systems × three models; model identities partly withheld`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11688v1 §3 Method; §4 theorem; §5 System`；counterevidence locator：`arXiv:2606.11688v1 §7 Limitations; Appendix A auditor boundary`。

**Trade-off / failure / coexistence / evolution。** hard floor 用 coverage 换 honesty；定理依赖 gate soundness、floor enforcement 与 plan coverage，不能证明任务本身正确。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11688:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11688v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11688:end -->
<!-- review:SF-2026-ARXIV-2606-11688:end -->

<!-- review:SF-2026-ARXIV-2606-11690:start -->
### 2606.11690 — Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。

**State / data / control owner。** `PLATFORM-COST` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11690v1 §4 Experimental Setup; §5 Results` 支持 `42 H100 benchmarks plus 56 A100 cross-hardware runs, 1–10 rps and saturation sweeps`；模型 `Dense, ultra-sparse MoE and sparse MoE models`；硬件 `NVIDIA H100 and A100 80GB PCIe`；精度 `FP16 and FP8 where supported`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11690v1 §3 Concurrency-Aware Cost Framework`；counterevidence locator：`arXiv:2606.11690v1 §6.8 Scope; §6.9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 真实 meter 提高归因但需要 workload replay；burst、prefix cache、I/O shape 与硬件 FP8 支持会改变 crossover。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11690:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11690v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11690:end -->
<!-- review:SF-2026-ARXIV-2606-11690:end -->

<!-- review:SF-2026-ARXIV-2606-11718:start -->
### 2606.11718 — Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11718v1 §IV Evaluation; §IV-A methodology` 支持 `Qwen3-30B and Llama-3.1-70B inference/training GEMM shapes`；模型 `Qwen3-30B; Llama-3.1-70B`；硬件 `Modeled multi-chiplet GPU; exact product not claimed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11718v1 §III Chiplet-Contiguous Layout`；counterevidence locator：`arXiv:2606.11718v1 §V Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 布局变换减少 remote HBM traffic，却要求 runtime/compiler 重排；对非 GEMM、动态 shape 或不同 interleave policy 不构成普遍收益。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11718:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11718v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11718:end -->
<!-- review:SF-2026-ARXIV-2606-11718:end -->

<!-- review:SF-2026-ARXIV-2606-11806:start -->
### 2606.11806 — External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11806v1 §4 setup; §5 Results; Appendices E–G` 支持 `Production moderation plus tool-use and GPQA contrast tasks`；模型 `Reasoning/instruct model variants disclosed in Appendix A.4`；硬件 `Not Disclosed — hosted serving hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11806v1 §3 Experience Serving in Production`；counterevidence locator：`arXiv:2606.11806v1 §4.4 claim boundary; Appendix H interpretation scope`。

**Trade-off / failure / coexistence / evolution。** selective retrieval 控制 prompt burden，但 miss/over-trigger 与 selector overhead 会伤害质量；规则少或高度共享时 global compact 仍成立。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11806:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11806v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11806:end -->
<!-- review:SF-2026-ARXIV-2606-11806:end -->

<!-- review:SF-2026-ARXIV-2606-11871:start -->
### 2606.11871 — WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11871v1 §VI Evaluation; §VII backend cost` 支持 `77 CUDA artifacts; 51,621 sites; 52.2M dynamic checks`；模型 `CUDA SASS binaries`；硬件 `NVIDIA CUDA testbed; exact GPU bound in §VI-A`；精度 `Not applicable — binary instrumentation`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11871v1 §III threat model; §§IV–V design/implementation`；counterevidence locator：`arXiv:2606.11871v1 §VI-H portability boundaries; §VIII Discussion`。

**Trade-off / failure / coexistence / evolution。** SASS-level enforcement覆盖真实执行面但增加 instrumentation/callback cost；未恢复 site 必须 fail closed 或留在 denominator 外。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11871:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11871v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11871:end -->
<!-- review:SF-2026-ARXIV-2606-11871:end -->

<!-- review:SF-2026-ARXIV-2606-11878:start -->
### 2606.11878 — Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decisions

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11878v1 §VI evidence; §VII-D mitigation results` 支持 `CUDA contract-conformance suite across four authority dimensions`；模型 `CUDA collective primitives and CIC wrapper`；硬件 `NVIDIA CUDA testbed; exact GPU in evidence appendix`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11878v1 §§III–V participation authority and CSC`；counterevidence locator：`arXiv:2606.11878v1 §VII-E Cost and Limits; §VIII Discussion and Limitations`。

**Trade-off / failure / coexistence / evolution。** CIC 防止 range-valid metadata 扭曲授权，却需保存 reference membership/epoch；普通 CFI 不覆盖此语义面。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11878:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11878v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11878:end -->
<!-- review:SF-2026-ARXIV-2606-11878:end -->

<!-- review:SF-2026-ARXIV-2606-11916:start -->
### 2606.11916 — Characterizing Software Aging in GPU-Based LLM Serving Systems

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11916v1 §IV Results; §§IV-A–IV-E` 支持 `216-hour campaign; six co-located deployments; Poisson stress`；模型 `Qwen2.5-7B-Instruct on vLLM, Triton-vLLM and PyTorch/HF`；硬件 `One host with 3× NVIDIA L40S`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11916v1 §III Methodology`；counterevidence locator：`arXiv:2606.11916v1 §V Threats to Validity`。

**Trade-off / failure / coexistence / evolution。** 长时 campaign 昂贵且 co-location 可能混入 contention；短基准仍适合 kernel 回归，但不能替代 rejuvenation evidence。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11916:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11916v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11916:end -->
<!-- review:SF-2026-ARXIV-2606-11916:end -->

<!-- review:SF-2026-ARXIV-2606-11949:start -->
### 2606.11949 — Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11949v1 §4 setup; §5 Results` 支持 `4 classifiers × 5 shifts × 20 seeds × 2 windows; 800 cells`；模型 `Four deployed safety classifiers`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11949v1 §3 Methods; §§3.1–3.10`；counterevidence locator：`arXiv:2606.11949v1 §6.5 Limitations; §5.4 ground-truth regimes`。

**Trade-off / failure / coexistence / evolution。** 检测可能对 target attack 无信号，density ratio 也会退化；abstention 恢复 coverage 不等于阻止攻击。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11949:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11949v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11949:end -->
<!-- review:SF-2026-ARXIV-2606-11949:end -->

<!-- review:SF-2026-ARXIV-2606-11998:start -->
### 2606.11998 — Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11998v1 §4 Results; Appendix C red/blue teaming` 支持 `Multi-turn BashArena software-engineering tasks`；模型 `Trusted, untrusted-agent and intermediate-monitor model configurations`；硬件 `Not Disclosed — API/runtime hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11998v1 §3 Methods; §3.1 threat model/protocol`；counterevidence locator：`arXiv:2606.11998v1 §5 Discussion, Transparent CoT assumption and Limitations`。

**Trade-off / failure / coexistence / evolution。** bootstrapping 延长弱 monitor 生命周期，却依赖 transparent CoT；隐藏推理、steganography 或共同盲点会失效。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11998:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11998v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11998:end -->
<!-- review:SF-2026-ARXIV-2606-11998:end -->

<!-- review:SF-2026-ARXIV-2606-12243:start -->
### 2606.12243 — VIA-SD: Verification via Intra-Model Routing for Speculative Decoding

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12243v1 §4 Experiments` 支持 `Four tasks across T5/Gemma model families`；模型 `T5 and Gemma families`；硬件 `Disclosed in §4.1; no cross-paper normalization`；精度 `Disclosed in §4.1 where applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12243v1 §3 Methodology; §§3.2–3.5`；counterevidence locator：`arXiv:2606.12243v1 §4.4 additional analysis; §5 Conclusion`。

**Trade-off / failure / coexistence / evolution。** slim verifier 节约 full-model calls 但引入 routing error/threshold；exact rejection contract 与 full verifier fallback 必须保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12243:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12243v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12243:end -->
<!-- review:SF-2026-ARXIV-2606-12243:end -->

<!-- review:SF-2026-ARXIV-2606-12320:start -->
### 2606.12320 — A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12320v1 §9 case studies; §10 validation roadmap` 支持 `Seven canonical workflow threats plus production case studies`；模型 `Reference architecture; not a model benchmark`；硬件 `Not applicable`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12320v1 §§3–8 threat model, five planes and composed architecture`；counterevidence locator：`arXiv:2606.12320v1 §11 Limitations and Open Questions`。

**Trade-off / failure / coexistence / evolution。** 多平面提高可中断性与归因，却增加 latency/state consistency/TCB；reference architecture 不证明生产效果。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12320:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12320v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12320:end -->
<!-- review:SF-2026-ARXIV-2606-12320:end -->

<!-- review:SF-2026-ARXIV-2606-12329:start -->
### 2606.12329 — PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12329v1 §7 Evaluation` 支持 `Two-month self-study, 10 projects, 207 events`；模型 `Local-first projectmem with MCP/CLI`；硬件 `Local developer environment; hardware not disclosed`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12329v1 §3 System Design; §§4–6 architecture/implementation`；counterevidence locator：`arXiv:2606.12329v1 §8 Limitations and Future Work`。

**Trade-off / failure / coexistence / evolution。** event sourcing 提供 provenance/rollback，但 self-study 不能证明跨团队收益；错误 judgment 仍需 supersession 与关闭开关。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12329:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12329v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12329:end -->
<!-- review:SF-2026-ARXIV-2606-12329:end -->

<!-- review:SF-2026-ARXIV-2606-12370:start -->
### 2606.12370 — Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12370v1 §6 Experiments` 支持 `RL math/reasoning workloads and MTP acceptance/throughput sweeps`；模型 `Multiple MTP-enabled LLM scales`；硬件 `Disclosed in experimental appendix`；精度 `Disclosed in experimental appendix`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12370v1 §§3–5 entropy bound, TV loss and adaptation`；counterevidence locator：`arXiv:2606.12370v1 §7.8 top-k instability; §9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 更新 MTP 提升 rollout throughput 却增加训练耦合；top-k TV 不稳，完整 rejection sampling 是 correctness fallback；TRAIN-RLHF 只消费 rollout throughput 与 policy-update handoff。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12370:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12370v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12370:end -->
<!-- review:SF-2026-ARXIV-2606-12370:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11257 | End-to-end indexing plus 120 Wikipedia-passage queries; embedding, retrieval, reranking and generation | Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity | Dell XPS 13, Snapdragon X Elite Hexagon NPU; CPU and Adreno/OpenCL GPU baselines | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Latency and energy are measured outcomes, not acceptance SLOs | Exact-v1 §IV–V Experimental Setup and Results; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §VI-B Limitations and Future Work |
| SF-2026-ARXIV-2606-11265 | Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection. | Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §V Experiment; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §III Threat Model and §VI Conclusion |
| SF-2026-ARXIV-2606-11270 | Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning. | Llama-2-7B-Chat and Qwen2.5-7B-Instruct teachers/students; GPT-4.1 evaluator | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §4 Experiments and Results; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §5 Analysis and §6 Conclusion |
| SF-2026-ARXIV-2606-11290 | Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off. | Qwen3-8B FlowBank optimizer; GPT-4o and Qwen3-8B optimizer baselines | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §4 Experiments; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in Appendix F.1 Limitations |
| SF-2026-ARXIV-2606-11349 | In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information. | Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §§4–5 Experiments and Results; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §6 Discussion |
| SF-2026-ARXIV-2606-11357 | With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets. | Gemma 2B and Qwen2.5 3B end-to-end LLM workloads | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §5 Evaluation; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §6 Discussion and Limitations |
| SF-2026-ARXIV-2606-11375 | Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy. | OLMo-2 1B and OLMo-3 7B checkpoints | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §4 Results; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §5.3 Limitations |
| SF-2026-ARXIV-2606-11387 | Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets. | Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §5 Results; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §7 Limitations |
| SF-2026-ARXIV-2606-11409 | Three attack strategies on two jailbreak benchmarks, re-parameterized by cumulative FLOPs | Ten models across three families and four training/alignment stages | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Risk-compute curves are evaluation objects, not service SLOs | Exact-v1 §3–4 Experimental Setup and Results; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §7 Future Work & Limitations |
| SF-2026-ARXIV-2606-11445 | Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs. | OLMo-3-7B-Think and Qwen3.5-2B target LRMs; GPT-5.4 and Claude Opus 4.6 naive readers | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §§4–5 evaluation and ablation; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §7 Limitations |
| SF-2026-ARXIV-2606-11520 | Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets. | Qwen3-8B fine-tuned model; Qwen3-8B, Qwen3-32B, and GPT-4o references | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §5 Experiments; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §6 Limitations |
| SF-2026-ARXIV-2606-11522 | Autoresearch agents now propose, evaluate, and select scientific candidates against a metric, and that metric is usually an aggregate reduced over a heterogeneous space of regions, slices, or cohorts. | Not applicable: fire-model research-control case, no evaluated LM checkpoint asserted | Not Disclosed | Not Disclosed | Dataset/task-defined; no universal fixed input length disclosed | Task-defined; no universal fixed output length disclosed | Not Disclosed | Not Disclosed | Not Disclosed — measured outcomes and experimental thresholds are not production SLOs | Exact-v1 §4 Evaluation; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in §5 Discussion |
| SF-2026-ARXIV-2606-11543 | Disclosed — 82 SkillsBench tasks × 3 conditions × 5 trials | Disclosed — GPT-5.4 high reasoning | Not Disclosed — hosted runtime hardware is not identified | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11632 | Disclosed — 500 contracts × five trials; 2,500 admissions | Disclosed — Go SAB prototype, OPA, PostgreSQL ledger, three-validator SQA | Single-node local workstation; exact CPU/GPU not disclosed | Not applicable — control-plane prototype | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11671 | Disclosed — 100 OpenClaw skills with static baselines and evolving attacks | Disclosed — LLM-assisted profiler/task generator/trace judge; exact models not fully disclosed | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11686 | Disclosed — 238 cases across 23 slices; seven injected regressions; two tenants | Disclosed — No-LLM deterministic ordering-agent scaffold | Not Disclosed | Not applicable — deterministic harness | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11688 | Disclosed — 3,150 paired cells; 70 tasks including 50 SWE-bench Lite | Disclosed — Three systems × three models; model identities partly withheld | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11690 | Disclosed — 42 H100 benchmarks plus 56 A100 cross-hardware runs, 1–10 rps and saturation sweeps | Disclosed — Dense, ultra-sparse MoE and sparse MoE models | NVIDIA H100 and A100 80GB PCIe | FP16 and FP8 where supported | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11718 | Disclosed — Qwen3-30B and Llama-3.1-70B inference/training GEMM shapes | Disclosed — Qwen3-30B; Llama-3.1-70B | Modeled multi-chiplet GPU; exact product not claimed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11806 | Disclosed — Production moderation plus tool-use and GPQA contrast tasks | Disclosed — Reasoning/instruct model variants disclosed in Appendix A.4 | Not Disclosed — hosted serving hardware not identified | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11871 | Disclosed — 77 CUDA artifacts; 51,621 sites; 52.2M dynamic checks | Disclosed — CUDA SASS binaries | NVIDIA CUDA testbed; exact GPU bound in §VI-A | Not applicable — binary instrumentation | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11878 | Disclosed — CUDA contract-conformance suite across four authority dimensions | Disclosed — CUDA collective primitives and CIC wrapper | NVIDIA CUDA testbed; exact GPU in evidence appendix | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11916 | Disclosed — 216-hour campaign; six co-located deployments; Poisson stress | Disclosed — Qwen2.5-7B-Instruct on vLLM, Triton-vLLM and PyTorch/HF | One host with 3× NVIDIA L40S | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11949 | Disclosed — 4 classifiers × 5 shifts × 20 seeds × 2 windows; 800 cells | Disclosed — Four deployed safety classifiers | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-11998 | Disclosed — Multi-turn BashArena software-engineering tasks | Disclosed — Trusted, untrusted-agent and intermediate-monitor model configurations | Not Disclosed — API/runtime hardware not identified | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12243 | Disclosed — Four tasks across T5/Gemma model families | Disclosed — T5 and Gemma families | Disclosed in §4.1; no cross-paper normalization | Disclosed in §4.1 where applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12320 | Disclosed — Seven canonical workflow threats plus production case studies | Disclosed — Reference architecture; not a model benchmark | Not applicable | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12329 | Disclosed — Two-month self-study, 10 projects, 207 events | Disclosed — Local-first projectmem with MCP/CLI | Local developer environment; hardware not disclosed | Not applicable | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-12370 | Disclosed — RL math/reasoning workloads and MTP acceptance/throughput sweeps | Disclosed — Multiple MTP-enabled LLM scales | Disclosed in experimental appendix | Disclosed in experimental appendix | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11257 | score_7_9; potential_books_delta | not_selected | — | — | Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11257 |
| SF-2026-ARXIV-2606-11265 | score_7_9 | not_selected | — | — | When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11265 |
| SF-2026-ARXIV-2606-11270 | score_7_9 | not_selected | — | — | Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11270 |
| SF-2026-ARXIV-2606-11290 | score_7_9 | not_selected | — | — | FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11290 |
| SF-2026-ARXIV-2606-11349 | score_7_9 | not_selected | — | — | Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11349 |
| SF-2026-ARXIV-2606-11357 | score_7_9 | not_selected | — | — | TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11357 |
| SF-2026-ARXIV-2606-11375 | score_7_9 | not_selected | — | — | When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11375 |
| SF-2026-ARXIV-2606-11387 | score_7_9; potential_books_delta | not_selected | — | — | Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11387 |
| SF-2026-ARXIV-2606-11409 | score_7_9 | not_selected | — | — | Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11409 |
| SF-2026-ARXIV-2606-11445 | score_7_9 | not_selected | — | — | Forecasting Future Behavior as a Learning Task remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11445 |
| SF-2026-ARXIV-2606-11520 | score_7_9 | not_selected | — | — | ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11520 |
| SF-2026-ARXIV-2606-11522 | score_7_9; potential_books_delta | selected | DA-20260610-AGENT-CONTROL | — | The agent-control unit was fixed before prose drafting: it moves commit authority away from the metric-optimizing research agent and demonstrates why disaggregated protected slices can reverse the aggregate winner. | analysis:DA-20260610-AGENT-CONTROL |
| SF-2026-ARXIV-2606-11543 | score_7_9; potential_books_delta | not_selected | — | — | SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11543 |
| SF-2026-ARXIV-2606-11632 | score_7_9; potential_books_delta | selected | DA-20260611-ADMISSION | — | Selected after 31/31 frontier comparison for non-overlapping control-plane, reliability, or serving-abstraction novelty. | analysis:DA-20260611-ADMISSION |
| SF-2026-ARXIV-2606-11671 | score_7_9; potential_books_delta | not_selected | — | — | Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11671 |
| SF-2026-ARXIV-2606-11686 | score_7_9; potential_books_delta | not_selected | — | — | Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11686 |
| SF-2026-ARXIV-2606-11688 | score_7_9; potential_books_delta | not_selected | — | — | Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11688 |
| SF-2026-ARXIV-2606-11690 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11690 |
| SF-2026-ARXIV-2606-11718 | score_7_9; potential_books_delta | not_selected | — | — | Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11718 |
| SF-2026-ARXIV-2606-11806 | score_7_9; potential_books_delta | not_selected | — | — | External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11806 |
| SF-2026-ARXIV-2606-11871 | score_7_9; potential_books_delta | not_selected | — | — | WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11871 |
| SF-2026-ARXIV-2606-11878 | score_7_9; potential_books_delta | not_selected | — | — | Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11878 |
| SF-2026-ARXIV-2606-11916 | score_7_9; potential_books_delta | selected | DA-20260611-AGING | — | Selected after 31/31 frontier comparison for non-overlapping control-plane, reliability, or serving-abstraction novelty. | analysis:DA-20260611-AGING |
| SF-2026-ARXIV-2606-11949 | score_7_9; potential_books_delta | not_selected | — | — | Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11949 |
| SF-2026-ARXIV-2606-11998 | score_7_9; potential_books_delta | not_selected | — | — | Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-11998 |
| SF-2026-ARXIV-2606-12243 | score_7_9 | not_selected | — | — | VIA-SD: Verification via Intra-Model Routing for Speculative Decoding remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-12243 |
| SF-2026-ARXIV-2606-12320 | score_7_9; potential_books_delta | not_selected | — | — | A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-12320 |
| SF-2026-ARXIV-2606-12329 | score_7_9; potential_books_delta | not_selected | — | — | PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-12329 |
| SF-2026-ARXIV-2606-12370 | score_7_9 | not_selected | — | — | Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-12370 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-2026-ARXIV-2606-11257:start -->
Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11257:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11265:start -->
When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11265:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11270:start -->
Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11270:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11290:start -->
FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11290:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11349:start -->
Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11349:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11357:start -->
TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11357:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11375:start -->
When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11375:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11387:start -->
Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11387:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11409:start -->
Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11409:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11445:start -->
Forecasting Future Behavior as a Learning Task remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11445:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11520:start -->
ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11520:end -->

<!-- analysis:DA-20260610-AGENT-CONTROL:start -->
Search Discipline is selected because it changes commit authority. An autoresearch agent optimizes an aggregate metric and is structurally conflicted when that metric hides a protected-region regression. The external controller owns the disaggregated slice contract, noise tolerance and acceptance decision. The fire-model example proves an aggregate inversion in one domain; it does not prove universal slice definitions. The durable rule is narrower: the proposer must not be the only party allowed to define and accept its evidence.
<!-- analysis:DA-20260610-AGENT-CONTROL:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11543:start -->
SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11543:end -->

<!-- analysis:DA-20260611-ADMISSION:start -->
### DA-20260611-ADMISSION
Proposal is not authority: typed contract, evidence digest, policy/revocation version and broker identity must all bind before a model proposal mutates production state.
<!-- analysis:DA-20260611-ADMISSION:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11671:start -->
Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11671:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11686:start -->
Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11688:start -->
Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11688:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11690:start -->
Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11690:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11718:start -->
Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11718:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11806:start -->
External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11806:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11871:start -->
WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11871:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11878:start -->
Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11878:end -->

<!-- analysis:DA-20260611-AGING:start -->
### DA-20260611-AGING
Serving reliability is time-dependent: host/device/client signals and autocorrelation-aware long campaigns are required before rejuvenation or release decisions.
<!-- analysis:DA-20260611-AGING:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11949:start -->
Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11949:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-11998:start -->
Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-11998:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12243:start -->
VIA-SD: Verification via Intra-Model Routing for Speculative Decoding remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-12243:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12320:start -->
A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-12320:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12329:start -->
PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-12329:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-12370:start -->
Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-12370:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-11257 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L213 | ROADMAP.md#L80; books/part-05-inference-system/54-gpu-memory.md#L10 | existing:SF-2026-ARXIV-2606-11257 | delta:SF-2026-ARXIV-2606-11257 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11257 |
| SF-2026-ARXIV-2606-11265 | AGENT-RAG | books/part-07-agent/76-rag.md#L10 | ROADMAP.md#L80; books/part-07-agent/76-rag.md#L10 | existing:SF-2026-ARXIV-2606-11265 | delta:SF-2026-ARXIV-2606-11265 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11265 |
| SF-2026-ARXIV-2606-11270 | TRAIN-DATA | books/part-04-training-system/27-data.md#L514 | ROADMAP.md#L80; books/part-04-training-system/27-data.md#L10 | existing:SF-2026-ARXIV-2606-11270 | delta:SF-2026-ARXIV-2606-11270 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11270 |
| SF-2026-ARXIV-2606-11290 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L628 | ROADMAP.md#L80; books/part-07-agent/81-workflow.md#L10 | existing:SF-2026-ARXIV-2606-11290 | delta:SF-2026-ARXIV-2606-11290 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11290 |
| SF-2026-ARXIV-2606-11349 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L10 | ROADMAP.md#L80; books/part-07-agent/79-planning.md#L10 | existing:SF-2026-ARXIV-2606-11349 | delta:SF-2026-ARXIV-2606-11349 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11349 |
| SF-2026-ARXIV-2606-11357 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L126 | ROADMAP.md#L80; books/part-05-inference-system/44-decode.md#L10 | existing:SF-2026-ARXIV-2606-11357 | delta:SF-2026-ARXIV-2606-11357 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11357 |
| SF-2026-ARXIV-2606-11375 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L653 | ROADMAP.md#L80; books/part-04-training-system/28-pretraining.md#L10 | existing:SF-2026-ARXIV-2606-11375 | delta:SF-2026-ARXIV-2606-11375 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11375 |
| SF-2026-ARXIV-2606-11387 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L653 | ROADMAP.md#L80; books/part-04-training-system/28-pretraining.md#L10 | existing:SF-2026-ARXIV-2606-11387 | delta:SF-2026-ARXIV-2606-11387 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11387 |
| SF-2026-ARXIV-2606-11409 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | ROADMAP.md#L80; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-11409 | delta:SF-2026-ARXIV-2606-11409 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11409 |
| SF-2026-ARXIV-2606-11445 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | ROADMAP.md#L80; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-11445 | delta:SF-2026-ARXIV-2606-11445 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11445 |
| SF-2026-ARXIV-2606-11520 | TRAIN-DATA | books/part-04-training-system/27-data.md#L514 | ROADMAP.md#L80; books/part-04-training-system/27-data.md#L10 | existing:SF-2026-ARXIV-2606-11520 | delta:SF-2026-ARXIV-2606-11520 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-11520 |
| SF-2026-ARXIV-2606-11522 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L549 | ROADMAP.md#L80; books/part-07-agent/84-agent-platform.md#L10 | existing:SF-2026-ARXIV-2606-11522 | delta:SF-2026-ARXIV-2606-11522 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11522 |
| SF-2026-ARXIV-2606-11543 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-11543 | delta:SF-2026-ARXIV-2606-11543 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11543 |
| SF-2026-ARXIV-2606-11632 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11632 | delta:SF-2026-ARXIV-2606-11632 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11632 |
| SF-2026-ARXIV-2606-11671 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11671 | delta:SF-2026-ARXIV-2606-11671 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11671 |
| SF-2026-ARXIV-2606-11686 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-11686 | delta:SF-2026-ARXIV-2606-11686 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11686 |
| SF-2026-ARXIV-2606-11688 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L1; books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-11688 | delta:SF-2026-ARXIV-2606-11688 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11688 |
| SF-2026-ARXIV-2606-11690 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-11690 | delta:SF-2026-ARXIV-2606-11690 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11690 |
| SF-2026-ARXIV-2606-11718 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1; books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-11718 | delta:SF-2026-ARXIV-2606-11718 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11718 |
| SF-2026-ARXIV-2606-11806 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-11806 | delta:SF-2026-ARXIV-2606-11806 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11806 |
| SF-2026-ARXIV-2606-11871 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11871 | delta:SF-2026-ARXIV-2606-11871 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11871 |
| SF-2026-ARXIV-2606-11878 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11878 | delta:SF-2026-ARXIV-2606-11878 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11878 |
| SF-2026-ARXIV-2606-11916 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-11916 | delta:SF-2026-ARXIV-2606-11916 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11916 |
| SF-2026-ARXIV-2606-11949 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-11949 | delta:SF-2026-ARXIV-2606-11949 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11949 |
| SF-2026-ARXIV-2606-11998 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-11998 | delta:SF-2026-ARXIV-2606-11998 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-11998 |
| SF-2026-ARXIV-2606-12243 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/44-decode.md#L1; books/part-04-training-system/31-rlhf.md#L1; books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-12243 | delta:SF-2026-ARXIV-2606-12243 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12243 |
| SF-2026-ARXIV-2606-12320 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-12320 | delta:SF-2026-ARXIV-2606-12320 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12320 |
| SF-2026-ARXIV-2606-12329 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-12329 | delta:SF-2026-ARXIV-2606-12329 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-12329 |
| SF-2026-ARXIV-2606-12370 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/44-decode.md#L1; books/part-04-training-system/31-rlhf.md#L1; books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-12370 | delta:SF-2026-ARXIV-2606-12370 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-12370 |

<!-- books-review:SF-2026-ARXIV-2606-11257:start -->
Compared `Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite` against `books/part-05-inference-system/54-gpu-memory.md#L213` and ROADMAP owner `INFER-GPU-MEMORY`.

<!-- existing:SF-2026-ARXIV-2606-11257:start -->
`INFER-GPU-MEMORY` already owns the underlying mechanism/evaluation boundary in `books/part-05-inference-system/54-gpu-memory.md#L213`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11257:end -->

<!-- delta:SF-2026-ARXIV-2606-11257:start -->
在 GPU Memory 章节补一个端侧 NPU 的全链 RAG memory/energy 分支，限定 Snapdragon X Elite、120-query 与单机测量，禁止外推其他 NPU。
<!-- delta:SF-2026-ARXIV-2606-11257:end -->

Decision: `Integrate`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11257:end -->

<!-- books-review:SF-2026-ARXIV-2606-11265:start -->
Compared `When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines` against `books/part-07-agent/76-rag.md#L10` and ROADMAP owner `AGENT-RAG`.

<!-- existing:SF-2026-ARXIV-2606-11265:start -->
`AGENT-RAG` already owns the underlying mechanism/evaluation boundary in `books/part-07-agent/76-rag.md#L10`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11265:end -->

<!-- delta:SF-2026-ARXIV-2606-11265:start -->
Exact-v1 adds the bounded alternative `Evaluate corpus poisoning after the real chunking and reranking pipeline, distinguishing retrieval exposure from whether the generator follows a poisoned chunk.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11265:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11265:end -->

<!-- books-review:SF-2026-ARXIV-2606-11270:start -->
Compared `Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation` against `books/part-04-training-system/27-data.md#L514` and ROADMAP owner `TRAIN-DATA`.

<!-- existing:SF-2026-ARXIV-2606-11270:start -->
`TRAIN-DATA` already owns the underlying mechanism/evaluation boundary in `books/part-04-training-system/27-data.md#L514`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11270:end -->

<!-- delta:SF-2026-ARXIV-2606-11270:start -->
Exact-v1 adds the bounded alternative `Measure subliminal behavior transfer through distillation as a ratio conditioned on teacher behavior and student response rather than treating matching outputs as benign data.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11270:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11270:end -->

<!-- books-review:SF-2026-ARXIV-2606-11290:start -->
Compared `FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse` against `books/part-07-agent/81-workflow.md#L628` and ROADMAP owner `AGENT-WORKFLOW`.

<!-- existing:SF-2026-ARXIV-2606-11290:start -->
`AGENT-WORKFLOW` already owns the underlying mechanism/evaluation boundary in `books/part-07-agent/81-workflow.md#L628`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11290:end -->

<!-- delta:SF-2026-ARXIV-2606-11290:start -->
Exact-v1 adds the bounded alternative `Precompute reusable workflow fragments into a bank and choose them per query, separating expensive workflow search from repeated online execution.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11290:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11290:end -->

<!-- books-review:SF-2026-ARXIV-2606-11349:start -->
Compared `Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents` against `books/part-07-agent/79-planning.md#L10` and ROADMAP owner `AGENT-PLANNING`.

<!-- existing:SF-2026-ARXIV-2606-11349:start -->
`AGENT-PLANNING` already owns the underlying mechanism/evaluation boundary in `books/part-07-agent/79-planning.md#L10`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11349:end -->

<!-- delta:SF-2026-ARXIV-2606-11349:start -->
Exact-v1 adds the bounded alternative `Make clarification a self-gated action competing with navigation on the same ordinal scale so information-seeking becomes an observable policy decision.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11349:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11349:end -->

<!-- books-review:SF-2026-ARXIV-2606-11357:start -->
Compared `TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs` against `books/part-05-inference-system/44-decode.md#L126` and ROADMAP owner `INFER-DECODE`.

<!-- existing:SF-2026-ARXIV-2606-11357:start -->
`INFER-DECODE` already owns the underlying mechanism/evaluation boundary in `books/part-05-inference-system/44-decode.md#L126`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11357:end -->

<!-- delta:SF-2026-ARXIV-2606-11357:start -->
Exact-v1 adds the bounded alternative `Fuse mixed-precision quantized LLM operators around AMD NPU tile/dataflow constraints instead of composing generic kernels with repeated layout conversion.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11357:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11357:end -->

<!-- books-review:SF-2026-ARXIV-2606-11375:start -->
Compared `When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis` against `books/part-04-training-system/28-pretraining.md#L653` and ROADMAP owner `TRAIN-PRETRAINING`.

<!-- existing:SF-2026-ARXIV-2606-11375:start -->
`TRAIN-PRETRAINING` already owns the underlying mechanism/evaluation boundary in `books/part-04-training-system/28-pretraining.md#L653`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11375:end -->

<!-- delta:SF-2026-ARXIV-2606-11375:start -->
Exact-v1 adds the bounded alternative `Add perturbation fragility after linear-probe accuracy saturates, so pretraining checkpoints with equal separability can still be distinguished by representation stability.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11375:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11375:end -->

<!-- books-review:SF-2026-ARXIV-2606-11387:start -->
Compared `Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining` against `books/part-04-training-system/28-pretraining.md#L653` and ROADMAP owner `TRAIN-PRETRAINING`.

<!-- existing:SF-2026-ARXIV-2606-11387:start -->
`TRAIN-PRETRAINING` already owns the underlying mechanism/evaluation boundary in `books/part-04-training-system/28-pretraining.md#L653`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11387:end -->

<!-- delta:SF-2026-ARXIV-2606-11387:start -->
在 Pretraining 章节补一段 staged promotion：小实验是扩容决策 receipt，不是大规模结果的缩小版证明；保留 scale inversion 与 distributed-effects failure。
<!-- delta:SF-2026-ARXIV-2606-11387:end -->

Decision: `Integrate`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11387:end -->

<!-- books-review:SF-2026-ARXIV-2606-11409:start -->
Compared `Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` and ROADMAP owner `PLATFORM-EVALUATION-SYSTEM`.

<!-- existing:SF-2026-ARXIV-2606-11409:start -->
`PLATFORM-EVALUATION-SYSTEM` already owns the underlying mechanism/evaluation boundary in `books/part-06-ai-infrastructure/66-evaluation-system.md#L10`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11409:end -->

<!-- delta:SF-2026-ARXIV-2606-11409:start -->
Exact-v1 adds the bounded alternative `Parameterize adversarial risk by cumulative attack FLOPs and report risk-compute curves, not only success at an equal query count.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11409:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11409:end -->

<!-- books-review:SF-2026-ARXIV-2606-11445:start -->
Compared `Forecasting Future Behavior as a Learning Task` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` and ROADMAP owner `PLATFORM-EVALUATION-SYSTEM`.

<!-- existing:SF-2026-ARXIV-2606-11445:start -->
`PLATFORM-EVALUATION-SYSTEM` already owns the underlying mechanism/evaluation boundary in `books/part-06-ai-infrastructure/66-evaluation-system.md#L10`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11445:end -->

<!-- delta:SF-2026-ARXIV-2606-11445:start -->
Exact-v1 adds the bounded alternative `Train a single-pass behavior forecaster directly on reasoning trajectories to predict rerun stability and response changes without pretending the trace is a faithful explanation.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11445:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11445:end -->

<!-- books-review:SF-2026-ARXIV-2606-11520:start -->
Compared `ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories` against `books/part-04-training-system/27-data.md#L514` and ROADMAP owner `TRAIN-DATA`.

<!-- existing:SF-2026-ARXIV-2606-11520:start -->
`TRAIN-DATA` already owns the underlying mechanism/evaluation boundary in `books/part-04-training-system/27-data.md#L514`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11520:end -->

<!-- delta:SF-2026-ARXIV-2606-11520:start -->
Exact-v1 adds the bounded alternative `Synthesize OS-agent data through structured intent, role-locked multi-turn simulation and execution of every tool call in an isolated live workspace.` but its trade/failure boundary does not require a durable manuscript change.
<!-- delta:SF-2026-ARXIV-2606-11520:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11520:end -->

<!-- books-review:SF-2026-ARXIV-2606-11522:start -->
Compared `Search Discipline for Long-Horizon Research Agents` against `books/part-07-agent/84-agent-platform.md#L549` and ROADMAP owner `AGENT-PLATFORM`.

<!-- existing:SF-2026-ARXIV-2606-11522:start -->
`AGENT-PLATFORM` already owns the underlying mechanism/evaluation boundary in `books/part-07-agent/84-agent-platform.md#L549`; the paper cannot silently transfer that owner.
<!-- existing:SF-2026-ARXIV-2606-11522:end -->

<!-- delta:SF-2026-ARXIV-2606-11522:start -->
在 Agent Platform 章节补 external acceptance loop：优化 aggregate metric 的 agent 不拥有 commit；controller 必须审计 protected slices 与 noise tolerance。
<!-- delta:SF-2026-ARXIV-2606-11522:end -->

Decision: `Integrate`. Exact-v1 evaluation conditions and non-proof boundary remain attached.
<!-- books-review:SF-2026-ARXIV-2606-11522:end -->

<!-- existing:SF-2026-ARXIV-2606-11543:start -->
Owner `AGENT-REFLECTION` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11543:end -->

<!-- delta:SF-2026-ARXIV-2606-11543:start -->
Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。
<!-- delta:SF-2026-ARXIV-2606-11543:end -->

<!-- books-review:SF-2026-ARXIV-2606-11543:start -->
Owner `AGENT-REFLECTION`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/81-workflow.md; books/part-07-agent/84-agent-platform.md`.
<!-- books-review:SF-2026-ARXIV-2606-11543:end -->

<!-- existing:SF-2026-ARXIV-2606-11632:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11632:end -->

<!-- delta:SF-2026-ARXIV-2606-11632:start -->
Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。
<!-- delta:SF-2026-ARXIV-2606-11632:end -->

<!-- books-review:SF-2026-ARXIV-2606-11632:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11632:end -->

<!-- existing:SF-2026-ARXIV-2606-11671:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11671:end -->

<!-- delta:SF-2026-ARXIV-2606-11671:start -->
Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。
<!-- delta:SF-2026-ARXIV-2606-11671:end -->

<!-- books-review:SF-2026-ARXIV-2606-11671:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11671:end -->

<!-- existing:SF-2026-ARXIV-2606-11686:start -->
Owner `PLATFORM-EVALUATION-SYSTEM` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11686:end -->

<!-- delta:SF-2026-ARXIV-2606-11686:start -->
生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。
<!-- delta:SF-2026-ARXIV-2606-11686:end -->

<!-- books-review:SF-2026-ARXIV-2606-11686:start -->
Owner `PLATFORM-EVALUATION-SYSTEM`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/67-monitoring.md; books/part-07-agent/81-workflow.md`.
<!-- books-review:SF-2026-ARXIV-2606-11686:end -->

<!-- existing:SF-2026-ARXIV-2606-11688:start -->
Owner `AGENT-WORKFLOW` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11688:end -->

<!-- delta:SF-2026-ARXIV-2606-11688:start -->
长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。
<!-- delta:SF-2026-ARXIV-2606-11688:end -->

<!-- books-review:SF-2026-ARXIV-2606-11688:start -->
Owner `AGENT-WORKFLOW`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/80-reflection.md; books/part-07-agent/82-multi-agent.md`.
<!-- books-review:SF-2026-ARXIV-2606-11688:end -->

<!-- existing:SF-2026-ARXIV-2606-11690:start -->
Owner `PLATFORM-COST` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11690:end -->

<!-- delta:SF-2026-ARXIV-2606-11690:start -->
LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。
<!-- delta:SF-2026-ARXIV-2606-11690:end -->

<!-- books-review:SF-2026-ARXIV-2606-11690:start -->
Owner `PLATFORM-COST`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/56-inference-scheduling.md; books/part-06-ai-infrastructure/67-monitoring.md`.
<!-- books-review:SF-2026-ARXIV-2606-11690:end -->

<!-- existing:SF-2026-ARXIV-2606-11718:start -->
Owner `INFER-GPU-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11718:end -->

<!-- delta:SF-2026-ARXIV-2606-11718:start -->
Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。
<!-- delta:SF-2026-ARXIV-2606-11718:end -->

<!-- books-review:SF-2026-ARXIV-2606-11718:start -->
Owner `INFER-GPU-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-05-inference-system/45-why-kv-cache-speeds-up.md; books/part-05-inference-system/55-pd-disaggregation.md`.
<!-- books-review:SF-2026-ARXIV-2606-11718:end -->

<!-- existing:SF-2026-ARXIV-2606-11806:start -->
Owner `AGENT-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11806:end -->

<!-- delta:SF-2026-ARXIV-2606-11806:start -->
生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。
<!-- delta:SF-2026-ARXIV-2606-11806:end -->

<!-- books-review:SF-2026-ARXIV-2606-11806:start -->
Owner `AGENT-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/75-context.md; books/part-07-agent/76-rag.md`.
<!-- books-review:SF-2026-ARXIV-2606-11806:end -->

<!-- existing:SF-2026-ARXIV-2606-11871:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11871:end -->

<!-- delta:SF-2026-ARXIV-2606-11871:start -->
CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。
<!-- delta:SF-2026-ARXIV-2606-11871:end -->

<!-- books-review:SF-2026-ARXIV-2606-11871:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11871:end -->

<!-- existing:SF-2026-ARXIV-2606-11878:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11878:end -->

<!-- delta:SF-2026-ARXIV-2606-11878:start -->
GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。
<!-- delta:SF-2026-ARXIV-2606-11878:end -->

<!-- books-review:SF-2026-ARXIV-2606-11878:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11878:end -->

<!-- existing:SF-2026-ARXIV-2606-11916:start -->
Owner `PLATFORM-MONITORING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11916:end -->

<!-- delta:SF-2026-ARXIV-2606-11916:start -->
LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。
<!-- delta:SF-2026-ARXIV-2606-11916:end -->

<!-- books-review:SF-2026-ARXIV-2606-11916:start -->
Owner `PLATFORM-MONITORING`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-06-ai-infrastructure/69-trace.md`.
<!-- books-review:SF-2026-ARXIV-2606-11916:end -->

<!-- existing:SF-2026-ARXIV-2606-11949:start -->
Owner `PLATFORM-MONITORING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11949:end -->

<!-- delta:SF-2026-ARXIV-2606-11949:start -->
deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。
<!-- delta:SF-2026-ARXIV-2606-11949:end -->

<!-- books-review:SF-2026-ARXIV-2606-11949:start -->
Owner `PLATFORM-MONITORING`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-06-ai-infrastructure/69-trace.md`.
<!-- books-review:SF-2026-ARXIV-2606-11949:end -->

<!-- existing:SF-2026-ARXIV-2606-11998:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-11998:end -->

<!-- delta:SF-2026-ARXIV-2606-11998:start -->
trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。
<!-- delta:SF-2026-ARXIV-2606-11998:end -->

<!-- books-review:SF-2026-ARXIV-2606-11998:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-11998:end -->

<!-- existing:SF-2026-ARXIV-2606-12243:start -->
Owner `INFER-SPECULATIVE-DECODING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12243:end -->

<!-- delta:SF-2026-ARXIV-2606-12243:start -->
把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。
<!-- delta:SF-2026-ARXIV-2606-12243:end -->

<!-- books-review:SF-2026-ARXIV-2606-12243:start -->
Owner `INFER-SPECULATIVE-DECODING`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `books/part-05-inference-system/44-decode.md; books/part-04-training-system/31-rlhf.md; books/part-05-inference-system/49-tensorrt-llm.md`.
<!-- books-review:SF-2026-ARXIV-2606-12243:end -->

<!-- existing:SF-2026-ARXIV-2606-12320:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12320:end -->

<!-- delta:SF-2026-ARXIV-2606-12320:start -->
生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。
<!-- delta:SF-2026-ARXIV-2606-12320:end -->

<!-- books-review:SF-2026-ARXIV-2606-12320:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-06-ai-infrastructure/71-multi-tenant.md; books/part-06-ai-infrastructure/73-production-best-practice.md`.
<!-- books-review:SF-2026-ARXIV-2606-12320:end -->

<!-- existing:SF-2026-ARXIV-2606-12329:start -->
Owner `AGENT-MEMORY` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12329:end -->

<!-- delta:SF-2026-ARXIV-2606-12329:start -->
Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。
<!-- delta:SF-2026-ARXIV-2606-12329:end -->

<!-- books-review:SF-2026-ARXIV-2606-12329:start -->
Owner `AGENT-MEMORY`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-07-agent/75-context.md; books/part-07-agent/76-rag.md`.
<!-- books-review:SF-2026-ARXIV-2606-12329:end -->

<!-- existing:SF-2026-ARXIV-2606-12370:start -->
Owner `INFER-SPECULATIVE-DECODING` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-12370:end -->

<!-- delta:SF-2026-ARXIV-2606-12370:start -->
RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。
<!-- delta:SF-2026-ARXIV-2606-12370:end -->

<!-- books-review:SF-2026-ARXIV-2606-12370:start -->
Owner `INFER-SPECULATIVE-DECODING`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`; adjacent handoff `books/part-05-inference-system/44-decode.md; books/part-04-training-system/31-rlhf.md; books/part-05-inference-system/49-tensorrt-llm.md`.
<!-- books-review:SF-2026-ARXIV-2606-12370:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260611-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260611 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260611: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260611-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-11257; review:SF-2026-ARXIV-2606-11265; review:SF-2026-ARXIV-2606-11270; review:SF-2026-ARXIV-2606-11290; review:SF-2026-ARXIV-2606-11349; review:SF-2026-ARXIV-2606-11357; review:SF-2026-ARXIV-2606-11375; review:SF-2026-ARXIV-2606-11387; review:SF-2026-ARXIV-2606-11409; review:SF-2026-ARXIV-2606-11445; review:SF-2026-ARXIV-2606-11520; review:SF-2026-ARXIV-2606-11522; review:SF-2026-ARXIV-2606-11543; review:SF-2026-ARXIV-2606-11632; review:SF-2026-ARXIV-2606-11671; review:SF-2026-ARXIV-2606-11686; review:SF-2026-ARXIV-2606-11688; review:SF-2026-ARXIV-2606-11690; review:SF-2026-ARXIV-2606-11718; review:SF-2026-ARXIV-2606-11806; review:SF-2026-ARXIV-2606-11871; review:SF-2026-ARXIV-2606-11878; review:SF-2026-ARXIV-2606-11916; review:SF-2026-ARXIV-2606-11949; review:SF-2026-ARXIV-2606-11998; review:SF-2026-ARXIV-2606-12243; review:SF-2026-ARXIV-2606-12320; review:SF-2026-ARXIV-2606-12329; review:SF-2026-ARXIV-2606-12370 | EVIDENCE-OWNER-REBUILD-20260611: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260611-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-11257; analysis-decision:SF-2026-ARXIV-2606-11265; analysis-decision:SF-2026-ARXIV-2606-11270; analysis-decision:SF-2026-ARXIV-2606-11290; analysis-decision:SF-2026-ARXIV-2606-11349; analysis-decision:SF-2026-ARXIV-2606-11357; analysis-decision:SF-2026-ARXIV-2606-11375; analysis-decision:SF-2026-ARXIV-2606-11387; analysis-decision:SF-2026-ARXIV-2606-11409; analysis-decision:SF-2026-ARXIV-2606-11445; analysis-decision:SF-2026-ARXIV-2606-11520; analysis:DA-20260610-AGENT-CONTROL; analysis-decision:SF-2026-ARXIV-2606-11543; analysis:DA-20260611-ADMISSION; analysis-decision:SF-2026-ARXIV-2606-11671; analysis-decision:SF-2026-ARXIV-2606-11686; analysis-decision:SF-2026-ARXIV-2606-11688; analysis-decision:SF-2026-ARXIV-2606-11690; analysis-decision:SF-2026-ARXIV-2606-11718; analysis-decision:SF-2026-ARXIV-2606-11806; analysis-decision:SF-2026-ARXIV-2606-11871; analysis-decision:SF-2026-ARXIV-2606-11878; analysis:DA-20260611-AGING; analysis-decision:SF-2026-ARXIV-2606-11949; analysis-decision:SF-2026-ARXIV-2606-11998; analysis-decision:SF-2026-ARXIV-2606-12243; analysis-decision:SF-2026-ARXIV-2606-12320; analysis-decision:SF-2026-ARXIV-2606-12329; analysis-decision:SF-2026-ARXIV-2606-12370 | SELECTION-OWNER-REBUILD-20260611: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260611-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-11257; books-review:SF-2026-ARXIV-2606-11265; books-review:SF-2026-ARXIV-2606-11270; books-review:SF-2026-ARXIV-2606-11290; books-review:SF-2026-ARXIV-2606-11349; books-review:SF-2026-ARXIV-2606-11357; books-review:SF-2026-ARXIV-2606-11375; books-review:SF-2026-ARXIV-2606-11387; books-review:SF-2026-ARXIV-2606-11409; books-review:SF-2026-ARXIV-2606-11445; books-review:SF-2026-ARXIV-2606-11520; books-review:SF-2026-ARXIV-2606-11522; books-review:SF-2026-ARXIV-2606-11543; books-review:SF-2026-ARXIV-2606-11632; books-review:SF-2026-ARXIV-2606-11671; books-review:SF-2026-ARXIV-2606-11686; books-review:SF-2026-ARXIV-2606-11688; books-review:SF-2026-ARXIV-2606-11690; books-review:SF-2026-ARXIV-2606-11718; books-review:SF-2026-ARXIV-2606-11806; books-review:SF-2026-ARXIV-2606-11871; books-review:SF-2026-ARXIV-2606-11878; books-review:SF-2026-ARXIV-2606-11916; books-review:SF-2026-ARXIV-2606-11949; books-review:SF-2026-ARXIV-2606-11998; books-review:SF-2026-ARXIV-2606-12243; books-review:SF-2026-ARXIV-2606-12320; books-review:SF-2026-ARXIV-2606-12329; books-review:SF-2026-ARXIV-2606-12370 | BOOKS-OWNER-REBUILD-20260611: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

- 528 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit instead of being promoted into the Candidate Ledger.

## 9. Recommended Action

- `Integrate`: 26 families were merged by root into 12 unique ROADMAP owners; each exact-v1 family ID occurs once in its target Books file.
- `No Change — Existing Coverage`: 5 families remain Daily evidence only because the durable mechanism and fallback boundary already exist in the owner or explicit adjacent chapter.
- Finding `F-0611-OWNER-12370` was confined to Daily routing: MTP acceptance/TV/rejection correctness belongs to `INFER-SPECULATIVE-DECODING`; `TRAIN-RLHF` consumes rollout throughput and policy-update consequences as an adjacent handoff.

## 10. Repository Changes

- Root performed the serialized Books writeback across the 12 files listed in `BOOKS_INTEGRATION_QUEUE_V1.md`.
- This lane updated the 2026-06-11 Daily, source receipts, finalizer and post-write audit only; it did not stage, commit, push or modify Books.

## 11. Open Questions

- How should runtime-skill probes, policy epochs and certificate revocation be recalibrated when evidence or threat distributions drift?
- Which aging signals can safely trigger rejuvenation without turning a deployment-specific campaign into a universal threshold?
- How should graph-serving placement, tiered memory and PD handoff share backpressure and failure semantics under mixed workloads?
- How should event-sourced experience and persistent-memory certificates expire or supersede incorrect historical judgments?
- These are research continuations, not unresolved Gate findings.

## 12. Sources

- [Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite](https://arxiv.org/abs/2606.11257v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines](https://arxiv.org/abs/2606.11265v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation](https://arxiv.org/abs/2606.11270v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse](https://arxiv.org/abs/2606.11290v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents](https://arxiv.org/abs/2606.11349v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs](https://arxiv.org/abs/2606.11357v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis](https://arxiv.org/abs/2606.11375v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining](https://arxiv.org/abs/2606.11387v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models](https://arxiv.org/abs/2606.11409v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Forecasting Future Behavior as a Learning Task](https://arxiv.org/abs/2606.11445v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/abs/2606.11520v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Search Discipline for Long-Horizon Research Agents](https://arxiv.org/abs/2606.11522v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/abs/2606.11543v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure](https://arxiv.org/abs/2606.11632v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security](https://arxiv.org/abs/2606.11671v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/abs/2606.11686v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents](https://arxiv.org/abs/2606.11688v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation](https://arxiv.org/abs/2606.11690v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs](https://arxiv.org/abs/2606.11718v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs](https://arxiv.org/abs/2606.11806v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries](https://arxiv.org/abs/2606.11871v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision](https://arxiv.org/abs/2606.11878v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Characterizing Software Aging in GPU-Based LLM Serving Systems](https://arxiv.org/abs/2606.11916v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers](https://arxiv.org/abs/2606.11949v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/abs/2606.11998v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/abs/2606.12243v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/abs/2606.12320v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/abs/2606.12329v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
- [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/abs/2606.12370v1) — first-public（Asia/Shanghai）：2026-06-11；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

- Status: Complete.
- Coverage Gate: Closed.
- Evidence Gate: Passed.
- Books Gate: Passed.
- Fresh-context Semantic Audit: Passed；unresolved findings = 0.

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
