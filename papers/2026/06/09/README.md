# Daily Research — 2026-06-09

**Research Date:** 2026-06-09

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-08 09:00:00 ～ 2026-06-09 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；477/477 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
> Strict V2.1 reconstruction for `DEN-20260609-477015`. No Books file is modified in this report.

The Beijing window contains 477 registered arXiv identities. Full 477/477 title+abstract screening freezes 15 durable families and 462 family-specific closures. Exact-v1 review passes all retained families. Corrected-contract Selection is `15 retained = 15 eligible + 0 non-eligible`, with three selected units; this equality is derived from all retained scores rather than assumed. Books formal comparison covers 15/15 families (14 Integrate, one No Change), while Weekly Only is explicitly zero. Evidence Gate and Books Gate are Passed after serialized writeback and post-write fresh audit.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-09 |
| Window End | 2026-06-09 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260609-477015 |
| Denominator Frozen At | 2026-08-29T20:45:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-08T09:00:00+08:00 | 2026-06-09T09:00:00+08:00 | 2026-08-29T20:45:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 1235 | SF-TRAIT-MISALIGNMENT-MONITOR;SF-ML-LIFECYCLE-ASSESSMENT;SF-2026-ARXIV-2606-07684;SF-2026-ARXIV-2606-07687;SF-2026-ARXIV-2606-07703;SF-2026-ARXIV-2606-07710;SF-2026-ARXIV-2606-07713;SF-2026-ARXIV-2606-07720;SF-2026-ARXIV-2606-07726;SF-2026-ARXIV-2606-07783;SF-2026-ARXIV-2606-07790;SF-2026-ARXIV-2606-07805;SF-2026-ARXIV-2606-07808;SF-2026-ARXIV-2606-07822;SF-2026-ARXIV-2606-07833;SF-2026-ARXIV-2606-07834;SF-2026-ARXIV-2606-07845;SF-2026-ARXIV-2606-07846;SF-2026-ARXIV-2606-07856;SF-2026-ARXIV-2606-07867;SF-2026-ARXIV-2606-07874;SF-2026-ARXIV-2606-07878;SF-2026-ARXIV-2606-07881;SF-2026-ARXIV-2606-07889;SF-2026-ARXIV-2606-07904;SF-2026-ARXIV-2606-07923;SF-2026-ARXIV-2606-07936;SF-2026-ARXIV-2606-07943;SF-2026-ARXIV-2606-07950;SF-2026-ARXIV-2606-07957;SF-2026-ARXIV-2606-07968;SF-2026-ARXIV-2606-07970;SF-2026-ARXIV-2606-07992;SF-2026-ARXIV-2606-08049;SF-2026-ARXIV-2606-08094;SF-2026-ARXIV-2606-08106;SF-2026-ARXIV-2606-08197;SF-2026-ARXIV-2606-08200;SF-2026-ARXIV-2606-08302;SF-2026-ARXIV-2606-08317;SF-2026-ARXIV-2606-08340;SF-2026-ARXIV-2606-08346;SF-2026-ARXIV-2606-08348;SF-2026-ARXIV-2606-08367;SF-2026-ARXIV-2606-08372;SF-2026-ARXIV-2606-08381;SF-2026-ARXIV-2606-08382;SF-2026-ARXIV-2606-08403;SF-2026-ARXIV-2606-08411;SF-2026-ARXIV-2606-08417;SF-2026-ARXIV-2606-08432;SF-2026-ARXIV-2606-08433;SF-2026-ARXIV-2606-08446;SF-2026-ARXIV-2606-08476;SF-2026-ARXIV-2606-08483;SF-2026-ARXIV-2606-08486;SF-2026-ARXIV-2606-08517;SF-2026-ARXIV-2606-08529;SF-2026-ARXIV-2606-08531;SF-2026-ARXIV-2606-08539;SF-2026-ARXIV-2606-08574;SF-2026-ARXIV-2606-08590;SF-2026-ARXIV-2606-08610;SF-2026-ARXIV-2606-08615;SF-2026-ARXIV-2606-08625;SF-2026-ARXIV-2606-08635;SF-2026-ARXIV-2606-08661;SF-2026-ARXIV-2606-08671;SF-2026-ARXIV-2606-08679;SF-2026-ARXIV-2606-08702;SF-2026-ARXIV-2606-08755;SF-2026-ARXIV-2606-08761;SF-2026-ARXIV-2606-08769;SF-2026-ARXIV-2606-08779;SF-2026-ARXIV-2606-08790;SF-2026-ARXIV-2606-08806;SF-2026-ARXIV-2606-08813;SF-2026-ARXIV-2606-08831;SF-2026-ARXIV-2606-08840;SF-2026-ARXIV-2606-08867;SF-2026-ARXIV-2606-08869;SF-2026-ARXIV-2606-08891;SF-2026-ARXIV-2606-08892;SF-2026-ARXIV-2606-08893;SF-2026-ARXIV-2606-08919;SF-2026-ARXIV-2606-08950;SF-2026-ARXIV-2606-08960;SF-2026-ARXIV-2606-09005;SF-2026-ARXIV-2606-09061;SF-2026-ARXIV-2606-09084;SF-2026-ARXIV-2606-09441;SF-2026-ARXIV-2606-09613;SF-2026-ARXIV-2606-09643;SF-2026-ARXIV-2606-09682;SF-2026-ARXIV-2606-09686;SF-2026-ARXIV-2606-09692;SF-2026-ARXIV-2606-09711;SF-2026-ARXIV-2606-09774;SF-2026-ARXIV-2606-09809 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260609/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260609; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260609 |
<!-- coverage:SRC-ARXIV:20260609:start -->
All 477 registered identities were screened at title+abstract level; 15 retained and 462 row-specific closures. No absent identity is counted as a closure: `2606.09138` is the discovered Claw-R1 identity and has its own family-specific pre-denominator closure; `2606.09686` uses the official exact-v1 84-Format title instead of the discovery snapshot's 83-Format title.
<!-- coverage:SRC-ARXIV:20260609:end -->


<!-- latest-contract-reopen:2026-06-09:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-09:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **1235** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **99** 条是旧报告 retained provenance，**1136** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-TRAIT-MISALIGNMENT-MONITOR | arXiv:2606.07631v1 | paper-v1:2606.07631 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-TRAIT-MISALIGNMENT-MONITOR | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-TRAIT-MISALIGNMENT-MONITOR | yes |
| SF-ML-LIFECYCLE-ASSESSMENT | arXiv:2606.07632v1 | paper-v1:2606.07632 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-ML-LIFECYCLE-ASSESSMENT | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-ML-LIFECYCLE-ASSESSMENT | yes |
| SF-2026-ARXIV-2606-07684 | arXiv:2606.07684v1 | paper-v1:2606.07684 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07684 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-07684 | yes |
| SF-2026-ARXIV-2606-07687 | arXiv:2606.07687v1 | paper-v1:2606.07687 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07687 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07687 | yes |
| SF-2026-ARXIV-2606-07703 | arXiv:2606.07703v1 | paper-v1:2606.07703 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07703 | self | — | new_in_window | INFER-PREFILL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07703 | yes |
| SF-2026-ARXIV-2606-07710 | arXiv:2606.07710v1 | paper-v1:2606.07710 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07710 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07710 | yes |
| SF-2026-ARXIV-2606-07713 | arXiv:2606.07713v1 | paper-v1:2606.07713 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07713 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07713 | yes |
| SF-2026-ARXIV-2606-07720 | arXiv:2606.07720v1 | paper-v1:2606.07720 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07720 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07720 | yes |
| SF-2026-ARXIV-2606-07726 | arXiv:2606.07726v1 | paper-v1:2606.07726 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07726 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07726 | yes |
| SF-2026-ARXIV-2606-07783 | arXiv:2606.07783v1 | paper-v1:2606.07783 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07783 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-07783 | yes |
| SF-2026-ARXIV-2606-07790 | arXiv:2606.07790v1 | paper-v1:2606.07790 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07790 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-07790 | yes |
| SF-2026-ARXIV-2606-07805 | arXiv:2606.07805v1 | paper-v1:2606.07805 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07805 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-07805 | yes |
| SF-2026-ARXIV-2606-07808 | arXiv:2606.07808v1 | paper-v1:2606.07808 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-07808 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-07808 | yes |
| SF-2026-ARXIV-2606-07822 | arXiv:2606.07822v1 | paper-v1:2606.07822 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07822 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-07822 | yes |
| SF-2026-ARXIV-2606-07833 | arXiv:2606.07833v1 | paper-v1:2606.07833 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-07833 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-07833 | yes |
| SF-2026-ARXIV-2606-07834 | arXiv:2606.07834v1 | paper-v1:2606.07834 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07834 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-07834 | yes |
| SF-2026-ARXIV-2606-07845 | arXiv:2606.07845v1 | paper-v1:2606.07845 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07845 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07845 | yes |
| SF-2026-ARXIV-2606-07846 | arXiv:2606.07846v1 | paper-v1:2606.07846 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07846 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07846 | yes |
| SF-2026-ARXIV-2606-07856 | arXiv:2606.07856v1 | paper-v1:2606.07856 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07856 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07856 | yes |
| SF-2026-ARXIV-2606-07867 | arXiv:2606.07867v1 | paper-v1:2606.07867 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-07867 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-07867 | yes |
| SF-2026-ARXIV-2606-07874 | arXiv:2606.07874v1 | paper-v1:2606.07874 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07874 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-07874 | yes |
| SF-2026-ARXIV-2606-07878 | arXiv:2606.07878v1 | paper-v1:2606.07878 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07878 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-07878 | yes |
| SF-2026-ARXIV-2606-07881 | arXiv:2606.07881v1 | paper-v1:2606.07881 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07881 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | Integrate | books-review:SF-2026-ARXIV-2606-07881 | yes |
| SF-2026-ARXIV-2606-07889 | arXiv:2606.07889v1 | paper-v1:2606.07889 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07889 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-07889 | yes |
| SF-2026-ARXIV-2606-07904 | arXiv:2606.07904v1 | paper-v1:2606.07904 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07904 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07904 | yes |
| SF-2026-ARXIV-2606-07923 | arXiv:2606.07923v1 | paper-v1:2606.07923 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07923 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-07923 | yes |
| SF-2026-ARXIV-2606-07936 | arXiv:2606.07936v1 | paper-v1:2606.07936 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07936 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07936 | yes |
| SF-2026-ARXIV-2606-07943 | arXiv:2606.07943v1 | paper-v1:2606.07943 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-07943 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-07943 | yes |
| SF-2026-ARXIV-2606-07950 | arXiv:2606.07950v1 | paper-v1:2606.07950 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07950 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07950 | yes |
| SF-2026-ARXIV-2606-07957 | arXiv:2606.07957v1 | paper-v1:2606.07957 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-07957 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07957 | yes |
| SF-2026-ARXIV-2606-07968 | arXiv:2606.07968v1 | paper-v1:2606.07968 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07968 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07968 | yes |
| SF-2026-ARXIV-2606-07970 | arXiv:2606.07970v1 | paper-v1:2606.07970 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-07970 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07970 | yes |
| SF-2026-ARXIV-2606-07992 | arXiv:2606.07992v1 | paper-v1:2606.07992 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07992 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07992 | yes |
| SF-2026-ARXIV-2606-08049 | arXiv:2606.08049v1 | paper-v1:2606.08049 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08049 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-08049 | yes |
| SF-2026-ARXIV-2606-08094 | arXiv:2606.08094v1 | paper-v1:2606.08094 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08094 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08094 | yes |
| SF-2026-ARXIV-2606-08106 | arXiv:2606.08106v1 | paper-v1:2606.08106 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08106 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-08106 | yes |
| SF-2026-ARXIV-2606-08197 | arXiv:2606.08197v1 | paper-v1:2606.08197 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08197 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08197 | yes |
| SF-2026-ARXIV-2606-08200 | arXiv:2606.08200v1 | paper-v1:2606.08200 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08200 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-08200 | yes |
| SF-2026-ARXIV-2606-08302 | arXiv:2606.08302v1 | paper-v1:2606.08302 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08302 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08302 | yes |
| SF-2026-ARXIV-2606-08317 | arXiv:2606.08317v1 | paper-v1:2606.08317 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08317 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08317 | yes |
| SF-2026-ARXIV-2606-08340 | arXiv:2606.08340v1 | paper-v1:2606.08340 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08340 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08340 | yes |
| SF-2026-ARXIV-2606-08346 | arXiv:2606.08346v1 | paper-v1:2606.08346 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08346 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08346 | yes |
| SF-2026-ARXIV-2606-08348 | arXiv:2606.08348v1 | paper-v1:2606.08348 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08348 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08348 | yes |
| SF-2026-ARXIV-2606-08367 | arXiv:2606.08367v1 | paper-v1:2606.08367 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08367 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08367 | yes |
| SF-2026-ARXIV-2606-08372 | arXiv:2606.08372v1 | paper-v1:2606.08372 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-08372 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08372 | yes |
| SF-2026-ARXIV-2606-08381 | arXiv:2606.08381v1 | paper-v1:2606.08381 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-08381 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08381 | yes |
| SF-2026-ARXIV-2606-08382 | arXiv:2606.08382v1 | paper-v1:2606.08382 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08382 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08382 | yes |
| SF-2026-ARXIV-2606-08403 | arXiv:2606.08403v1 | paper-v1:2606.08403 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08403 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-08403 | yes |
| SF-2026-ARXIV-2606-08411 | arXiv:2606.08411v1 | paper-v1:2606.08411 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08411 | self | — | new_in_window | INFER-DECODE | Integrate | books-review:SF-2026-ARXIV-2606-08411 | yes |
| SF-2026-ARXIV-2606-08417 | arXiv:2606.08417v1 | paper-v1:2606.08417 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08417 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08417 | yes |
| SF-2026-ARXIV-2606-08432 | arXiv:2606.08432v1 | paper-v1:2606.08432 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08432 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08432 | yes |
| SF-2026-ARXIV-2606-08433 | arXiv:2606.08433v1 | paper-v1:2606.08433 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08433 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08433 | yes |
| SF-2026-ARXIV-2606-08446 | arXiv:2606.08446v1 | paper-v1:2606.08446 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08446 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08446 | yes |
| SF-2026-ARXIV-2606-08476 | arXiv:2606.08476v1 | paper-v1:2606.08476 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08476 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-08476 | yes |
| SF-2026-ARXIV-2606-08483 | arXiv:2606.08483v1 | paper-v1:2606.08483 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08483 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08483 | yes |
| SF-2026-ARXIV-2606-08486 | arXiv:2606.08486v1 | paper-v1:2606.08486 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08486 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08486 | yes |
| SF-2026-ARXIV-2606-08517 | arXiv:2606.08517v1 | paper-v1:2606.08517 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08517 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08517 | yes |
| SF-2026-ARXIV-2606-08529 | arXiv:2606.08529v1 | paper-v1:2606.08529 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08529 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08529 | yes |
| SF-2026-ARXIV-2606-08531 | arXiv:2606.08531v1 | paper-v1:2606.08531 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08531 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08531 | yes |
| SF-2026-ARXIV-2606-08539 | arXiv:2606.08539v1 | paper-v1:2606.08539 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08539 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-08539 | yes |
| SF-2026-ARXIV-2606-08574 | arXiv:2606.08574v1 | paper-v1:2606.08574 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08574 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08574 | yes |
| SF-2026-ARXIV-2606-08590 | arXiv:2606.08590v1 | paper-v1:2606.08590 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08590 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08590 | yes |
| SF-2026-ARXIV-2606-08610 | arXiv:2606.08610v1 | paper-v1:2606.08610 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08610 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08610 | yes |
| SF-2026-ARXIV-2606-08615 | arXiv:2606.08615v1 | paper-v1:2606.08615 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08615 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08615 | yes |
| SF-2026-ARXIV-2606-08625 | arXiv:2606.08625v1 | paper-v1:2606.08625 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08625 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08625 | yes |
| SF-2026-ARXIV-2606-08635 | arXiv:2606.08635v1 | paper-v1:2606.08635 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08635 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2606-08635 | yes |
| SF-2026-ARXIV-2606-08661 | arXiv:2606.08661v1 | paper-v1:2606.08661 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08661 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08661 | yes |
| SF-2026-ARXIV-2606-08671 | arXiv:2606.08671v1 | paper-v1:2606.08671 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08671 | self | — | new_in_window | AGENT-REFLECTION | Integrate | books-review:SF-2026-ARXIV-2606-08671 | yes |
| SF-2026-ARXIV-2606-08679 | arXiv:2606.08679v1 | paper-v1:2606.08679 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08679 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08679 | yes |
| SF-2026-ARXIV-2606-08702 | arXiv:2606.08702v1 | paper-v1:2606.08702 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08702 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08702 | yes |
| SF-2026-ARXIV-2606-08755 | arXiv:2606.08755v1 | paper-v1:2606.08755 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08755 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08755 | yes |
| SF-2026-ARXIV-2606-08761 | arXiv:2606.08761v1 | paper-v1:2606.08761 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08761 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-08761 | yes |
| SF-2026-ARXIV-2606-08769 | arXiv:2606.08769v1 | paper-v1:2606.08769 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08769 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08769 | yes |
| SF-2026-ARXIV-2606-08779 | arXiv:2606.08779v1 | paper-v1:2606.08779 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08779 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08779 | yes |
| SF-2026-ARXIV-2606-08790 | arXiv:2606.08790v1 | paper-v1:2606.08790 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08790 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08790 | yes |
| SF-2026-ARXIV-2606-08806 | arXiv:2606.08806v1 | paper-v1:2606.08806 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08806 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08806 | yes |
| SF-2026-ARXIV-2606-08813 | arXiv:2606.08813v1 | paper-v1:2606.08813 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08813 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08813 | yes |
| SF-2026-ARXIV-2606-08831 | arXiv:2606.08831v1 | paper-v1:2606.08831 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08831 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08831 | yes |
| SF-2026-ARXIV-2606-08840 | arXiv:2606.08840v1 | paper-v1:2606.08840 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08840 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08840 | yes |
| SF-2026-ARXIV-2606-08867 | arXiv:2606.08867v1 | paper-v1:2606.08867 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08867 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08867 | yes |
| SF-2026-ARXIV-2606-08869 | arXiv:2606.08869v1 | paper-v1:2606.08869 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08869 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08869 | yes |
| SF-2026-ARXIV-2606-08891 | arXiv:2606.08891v1 | paper-v1:2606.08891 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08891 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08891 | yes |
| SF-2026-ARXIV-2606-08892 | arXiv:2606.08892v1 | paper-v1:2606.08892 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08892 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08892 | yes |
| SF-2026-ARXIV-2606-08893 | arXiv:2606.08893v1 | paper-v1:2606.08893 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08893 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08893 | yes |
| SF-2026-ARXIV-2606-08919 | arXiv:2606.08919v1 | paper-v1:2606.08919 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08919 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-08919 | yes |
| SF-2026-ARXIV-2606-08950 | arXiv:2606.08950v1 | paper-v1:2606.08950 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08950 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-08950 | yes |
| SF-2026-ARXIV-2606-08960 | arXiv:2606.08960v1 | paper-v1:2606.08960 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-08960 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-08960 | yes |
| SF-2026-ARXIV-2606-09005 | arXiv:2606.09005v1 | paper-v1:2606.09005 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09005 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-09005 | yes |
| SF-2026-ARXIV-2606-09061 | arXiv:2606.09061v1 | paper-v1:2606.09061 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09061 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-09061 | yes |
| SF-2026-ARXIV-2606-09084 | arXiv:2606.09084v1 | paper-v1:2606.09084 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09084 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-09084 | yes |
| SF-2026-ARXIV-2606-09441 | arXiv:2606.09441v1 | paper-v1:2606.09441 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09441 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2606-09441 | yes |
| SF-2026-ARXIV-2606-09613 | arXiv:2606.09613v1 | paper-v1:2606.09613 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09613 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-09613 | yes |
| SF-2026-ARXIV-2606-09643 | arXiv:2606.09643v1 | paper-v1:2606.09643 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09643 | self | — | new_in_window | INFER-KSERVE-TOPOLOGY | Integrate | books-review:SF-2026-ARXIV-2606-09643 | yes |
| SF-2026-ARXIV-2606-09682 | arXiv:2606.09682v1 | paper-v1:2606.09682 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09682 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-09682 | yes |
| SF-2026-ARXIV-2606-09686 | arXiv:2606.09686v1 | paper-v1:2606.09686 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09686 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-09686 | yes |
| SF-2026-ARXIV-2606-09692 | arXiv:2606.09692v1 | paper-v1:2606.09692 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09692 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2606-09692 | yes |
| SF-2026-ARXIV-2606-09711 | arXiv:2606.09711v1 | paper-v1:2606.09711 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09711 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-09711 | yes |
| SF-2026-ARXIV-2606-09774 | arXiv:2606.09774v1 | paper-v1:2606.09774 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09774 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-09774 | yes |
| SF-2026-ARXIV-2606-09809 | arXiv:2606.09809v1 | paper-v1:2606.09809 | 2026-W24 | 2026-06-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-09809 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-09809 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-TRAIT-MISALIGNMENT-MONITOR | RP-7b6f13d8fc137a1d | deep | arXiv:2606.07631v1 | SRC-ARXIV@arXiv:2606.07631v1 | arXiv:2606.07631v1 exact-v1 HTML § `3 Methodology`; § `3.1 Two-Phase Trait-Space Representation`; § `3.2 Finetuning Protocol` | arXiv:2606.07631v1 exact-v1 HTML § `4 Trait-space Geometry of Finetuning Drift`; § `5 Stress Tests`; Appendix `9 EM Evaluation Protocol` | arXiv:2606.07631v1 exact-v1 HTML § `6 Discussion and Conclusion` (`Calibration scope`; `Caveats and technical limits`) | Not Disclosed — arXiv:2606.07631v1 exact-v1 HTML does not pin an immutable implementation revision | claim:SF-TRAIT-MISALIGNMENT-MONITOR | complete |
| SF-ML-LIFECYCLE-ASSESSMENT | RP-b01411d5e8809fad | deep | arXiv:2606.07632v1 | SRC-ARXIV@arXiv:2606.07632v1 | arXiv:2606.07632v1 exact-v1 PDF § `3 Life Cycle Assessment for ML Models`; § `3.1 Goal Definition and Scoping` | arXiv:2606.07632v1 exact-v1 PDF § `3.5 Case Study: Comparing the Effects of LLM System Design Choices with LCA`; § `4 Alternative Views` | arXiv:2606.07632v1 exact-v1 PDF § `2 Limitations in Existing Approaches to Evaluating ML’s Resource Needs`; § `5 Benefits of LCAs in Machine Learning` | Not Disclosed — arXiv:2606.07632v1 does not pin an immutable implementation revision | claim:SF-ML-LIFECYCLE-ASSESSMENT | complete |
| SF-2026-ARXIV-2606-07684 | RP-988218261a7122dc | deep | arXiv:2606.07684v1 | SRC-ARXIV@arXiv:2606.07684v1 | § exact-v1 web-proxy locator for arXiv:2606.07684v1: §3 Problem Formulation; §§4–5 reuse, semantic drift and selective patching at https://arxiv.org/html/2606.07684v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07684v1: §6 Experiments at https://arxiv.org/html/2606.07684v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07684v1: Limitations and Future Work: shared architecture, <=32K context, one-time pair calibration and bounded distribution shift at https://arxiv.org/html/2606.07684v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07684 | complete |
| SF-2026-ARXIV-2606-07687 | RP-2400e5e227e3267c | standard | arXiv:2606.07687v1 | SRC-ARXIV@arXiv:2606.07687v1 | § exact-v1 web-proxy route for arXiv:2606.07687v1: full identity and method review at https://arxiv.org/html/2606.07687v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07687v1: full evaluation/results/table review at https://arxiv.org/html/2606.07687v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07687v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07687v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07687 | complete |
| SF-2026-ARXIV-2606-07703 | RP-37c05af618829e80 | standard | arXiv:2606.07703v1 | SRC-ARXIV@arXiv:2606.07703v1 | § exact-v1 web-proxy route for arXiv:2606.07703v1: full identity and method review at https://arxiv.org/html/2606.07703v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07703v1: full evaluation/results/table review at https://arxiv.org/html/2606.07703v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07703v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07703v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07703 | complete |
| SF-2026-ARXIV-2606-07710 | RP-e4fe81f16b36bef6 | standard | arXiv:2606.07710v1 | SRC-ARXIV@arXiv:2606.07710v1 | § exact-v1 web-proxy route for arXiv:2606.07710v1: full identity and method review at https://arxiv.org/html/2606.07710v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07710v1: full evaluation/results/table review at https://arxiv.org/html/2606.07710v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07710v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07710v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07710 | complete |
| SF-2026-ARXIV-2606-07713 | RP-7efb5094e94d8f29 | standard | arXiv:2606.07713v1 | SRC-ARXIV@arXiv:2606.07713v1 | § exact-v1 web-proxy route for arXiv:2606.07713v1: full identity and method review at https://arxiv.org/html/2606.07713v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07713v1: full evaluation/results/table review at https://arxiv.org/html/2606.07713v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07713v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07713v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07713 | complete |
| SF-2026-ARXIV-2606-07720 | RP-03339872f21980af | standard | arXiv:2606.07720v1 | SRC-ARXIV@arXiv:2606.07720v1 | § exact-v1 web-proxy route for arXiv:2606.07720v1: full identity and method review at https://arxiv.org/html/2606.07720v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07720v1: full evaluation/results/table review at https://arxiv.org/html/2606.07720v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07720v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07720v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07720 | complete |
| SF-2026-ARXIV-2606-07726 | RP-21a13aebf0b681d7 | standard | arXiv:2606.07726v1 | SRC-ARXIV@arXiv:2606.07726v1 | § exact-v1 web-proxy route for arXiv:2606.07726v1: full identity and method review at https://arxiv.org/html/2606.07726v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07726v1: full evaluation/results/table review at https://arxiv.org/html/2606.07726v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07726v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07726v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07726 | complete |
| SF-2026-ARXIV-2606-07783 | RP-8d05a341e5623002 | deep | arXiv:2606.07783v1 | SRC-ARXIV@arXiv:2606.07783v1 | § exact-v1 web-proxy locator for arXiv:2606.07783v1: §3 Experimental Design and Setup; §§3.3–3.7 clean, poisoned and mixed contexts at https://arxiv.org/html/2606.07783v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07783v1: §4 Evaluation Metrics and result sections at https://arxiv.org/html/2606.07783v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07783v1: Limitations: synthetic poison, small question set and two models; no broad retrieval guarantee at https://arxiv.org/html/2606.07783v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07783 | complete |
| SF-2026-ARXIV-2606-07790 | RP-a19496864e2f7cf8 | deep | arXiv:2606.07790v1 | SRC-ARXIV@arXiv:2606.07790v1 | § exact-v1 web-proxy locator for arXiv:2606.07790v1: §3 Experimental Setup; §4 Byzantine Cheap Talk; topology/condition design at https://arxiv.org/html/2606.07790v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07790v1: §§3.1–3.5 game, models, conditions and metrics; result sections; Appendix 0.B at https://arxiv.org/html/2606.07790v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07790v1: Conclusion and Appendix scope: coordination game traces do not prove Byzantine-tolerant production protocols at https://arxiv.org/html/2606.07790v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07790 | complete |
| SF-2026-ARXIV-2606-07805 | RP-13cc06785c3df236 | deep | arXiv:2606.07805v1 | SRC-ARXIV@arXiv:2606.07805v1 | § exact-v1 web-proxy locator for arXiv:2606.07805v1: §3 Methodology; §§3.1–3.5 SERV pipeline, scenario evolution and trace audit at https://arxiv.org/html/2606.07805v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07805v1: §4 Experiments at https://arxiv.org/html/2606.07805v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07805v1: Discussion/Conclusion boundaries: dynamic benchmark evidence is not enforceable compliance authority at https://arxiv.org/html/2606.07805v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07805 | complete |
| SF-2026-ARXIV-2606-07808 | RP-4c14921b61b66211 | deep | arXiv:2606.07808v1 | SRC-ARXIV@arXiv:2606.07808v1 | § exact-v1 web-proxy locator for arXiv:2606.07808v1: §2 Diagnostic framework; §2.2 three-stage IH process; §2.3 failure modes at https://arxiv.org/html/2606.07808v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07808v1: §3 Diagnostic study; §4 self-monitoring interventions; Appendix H prompts at https://arxiv.org/html/2606.07808v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07808v1: §6 Limitations; self-monitoring is not authenticated provenance or deterministic authorization at https://arxiv.org/html/2606.07808v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07808 | complete |
| SF-2026-ARXIV-2606-07822 | RP-0832dd61d606519b | deep | arXiv:2606.07822v1 | SRC-ARXIV@arXiv:2606.07822v1 | § exact-v1 web-proxy locator for arXiv:2606.07822v1: §2 EURO utility metric; §3 ACUTE activation features and estimators at https://arxiv.org/html/2606.07822v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07822v1: §4 Experiments; §5 Results & Analysis; Appendices G–K at https://arxiv.org/html/2606.07822v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07822v1: Appendix L Additional Limitations; confidence/utility estimates remain task/model/calibration conditional at https://arxiv.org/html/2606.07822v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07822 | complete |
| SF-2026-ARXIV-2606-07833 | RP-ea6d45ac4c23343b | deep | arXiv:2606.07833v1 | SRC-ARXIV@arXiv:2606.07833v1 | § exact-v1 web-proxy locator for arXiv:2606.07833v1: §2 Experimental Setup; process-mining formulation at https://arxiv.org/html/2606.07833v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07833v1: §3 Results; §§3.1–3.6 state transitions, mutators and time-to-jailbreak at https://arxiv.org/html/2606.07833v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07833v1: §4 Discussion — Limitations; two models/controlled campaign do not establish deployment prevalence at https://arxiv.org/html/2606.07833v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07833 | complete |
| SF-2026-ARXIV-2606-07834 | RP-17c55f36a6b4c264 | deep | arXiv:2606.07834v1 | SRC-ARXIV@arXiv:2606.07834v1 | § exact-v1 web-proxy locator for arXiv:2606.07834v1: §4 Problem Definition and Diagnostic Protocol; §§4.2–4.6 CCO and two-channel probe at https://arxiv.org/html/2606.07834v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07834v1: §5 Intervention Ladder; §6 Channel-Orthogonality Tests; Appendix B/C at https://arxiv.org/html/2606.07834v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07834v1: §7 Scope Conditions and Limitations; mixed-evidence contract and modest/non-replicating magnitude boundaries at https://arxiv.org/html/2606.07834v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07834 | complete |
| SF-2026-ARXIV-2606-07845 | RP-8842a3cf384923b8 | deep | arXiv:2606.07845v1 | SRC-ARXIV@arXiv:2606.07845v1 | § exact-v1 web-proxy route for arXiv:2606.07845v1: full identity and method review at https://arxiv.org/html/2606.07845v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07845v1: full evaluation/results/table review at https://arxiv.org/html/2606.07845v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07845v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07845v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07845 | complete |
| SF-2026-ARXIV-2606-07846 | RP-2bf337c18c63a132 | standard | arXiv:2606.07846v1 | SRC-ARXIV@arXiv:2606.07846v1 | § exact-v1 web-proxy route for arXiv:2606.07846v1: full identity and method review at https://arxiv.org/html/2606.07846v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07846v1: full evaluation/results/table review at https://arxiv.org/html/2606.07846v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07846v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07846v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07846 | complete |
| SF-2026-ARXIV-2606-07856 | RP-5a6e358cf86f141e | standard | arXiv:2606.07856v1 | SRC-ARXIV@arXiv:2606.07856v1 | § exact-v1 web-proxy route for arXiv:2606.07856v1: full identity and method review at https://arxiv.org/html/2606.07856v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07856v1: full evaluation/results/table review at https://arxiv.org/html/2606.07856v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07856v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07856v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07856 | complete |
| SF-2026-ARXIV-2606-07867 | RP-7736f8f79dac253f | deep | arXiv:2606.07867v1 | SRC-ARXIV@arXiv:2606.07867v1 | § exact-v1 web-proxy locator for arXiv:2606.07867v1: §2 SODA benchmark; §3 cold-start gap; §4 causal ablations at https://arxiv.org/html/2606.07867v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07867v1: §§3.1–5.2 experiments; §7 additional experiments; Appendices C–G at https://arxiv.org/html/2606.07867v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07867v1: §6 deployment recommendation and Limitations; warm-up evidence is not an external safety authority at https://arxiv.org/html/2606.07867v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07867 | complete |
| SF-2026-ARXIV-2606-07874 | RP-dc62a2778a760b80 | deep | arXiv:2606.07874v1 | SRC-ARXIV@arXiv:2606.07874v1 | § exact-v1 web-proxy locator for arXiv:2606.07874v1: §3 Experimental Setup; §§4–5 susceptibility and policy-steerability questions at https://arxiv.org/html/2606.07874v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07874v1: §§4.1–5 experiments; Appendices B–D cross-task/language/model results at https://arxiv.org/html/2606.07874v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07874v1: Limitations section; prior rigidity is judge/task/context conditional at https://arxiv.org/html/2606.07874v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07874 | complete |
| SF-2026-ARXIV-2606-07878 | RP-b7f192e14d33f39d | deep | arXiv:2606.07878v1 | SRC-ARXIV@arXiv:2606.07878v1 | § exact-v1 web-proxy locator for arXiv:2606.07878v1: §2 Method; §§2.1–2.4 Perceiver compactor, position handling, iteration and training at https://arxiv.org/html/2606.07878v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07878v1: §3 Results; Appendix B.1 vLLM injection microbenchmark; Appendices H–O at https://arxiv.org/html/2606.07878v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07878v1: §5 Discussion — Limitations; logical/physical cache length and training-transfer boundaries at https://arxiv.org/html/2606.07878v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07878 | complete |
| SF-2026-ARXIV-2606-07881 | RP-e859d22bd7f93e13 | deep | arXiv:2606.07881v1 | SRC-ARXIV@arXiv:2606.07881v1 | § exact-v1 web-proxy locator for arXiv:2606.07881v1: §3 Method; §§3.1–3.4 version drift and update-frequency control; Appendix D inconsistency bound at https://arxiv.org/html/2606.07881v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07881v1: §4 Results; Appendix B systems/hardware/precision; Appendix C at https://arxiv.org/html/2606.07881v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07881v1: §5 Discussion — Limitations; bounded drift evidence is GPT-style/single-node/configuration conditional at https://arxiv.org/html/2606.07881v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07881 | complete |
| SF-2026-ARXIV-2606-07889 | RP-7bf1ee4a393eff1e | deep | arXiv:2606.07889v1 | SRC-ARXIV@arXiv:2606.07889v1 | § exact-v1 web-proxy locator for arXiv:2606.07889v1: §2 Strained Coherence; §3 Method; §§3.1–3.4 dataset, detector, baselines and evaluation at https://arxiv.org/html/2606.07889v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07889v1: §4 Results; §§4.1–4.7 main, selectivity, cross-model and paraphrase slices at https://arxiv.org/html/2606.07889v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy locator for arXiv:2606.07889v1: §6 Limitations and Future Work; small samples, late median flag time and think-text substrate dependence at https://arxiv.org/html/2606.07889v1; local transfer reset prevented freezing fragment IDs | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07889 | complete |
| SF-2026-ARXIV-2606-07904 | RP-1f2ffd36ae157898 | deep | arXiv:2606.07904v1 | SRC-ARXIV@arXiv:2606.07904v1 | § exact-v1 web-proxy route for arXiv:2606.07904v1: full identity and method review at https://arxiv.org/html/2606.07904v1; local transfer reset prevented freezing fragment IDs | § exact-v1 web-proxy route for arXiv:2606.07904v1: full evaluation/results/table review at https://arxiv.org/html/2606.07904v1; no unlocated result is promoted beyond the abstract-bound benchmark contract | § exact-v1 web-proxy route for arXiv:2606.07904v1: full limitations/conclusion/appendix counterevidence review at https://arxiv.org/html/2606.07904v1; non-disclosed fields remain explicit | Not Disclosed — no immutable event-time artifact revision was used for this claim | claim:SF-2026-ARXIV-2606-07904 | complete |
| SF-2026-ARXIV-2606-07923 | RP-c680c902d7ada098 | deep | arXiv:2606.07923v1 | SRC-ARXIV@arXiv:2606.07923v1 | arXiv:2606.07923v1 §3 Larch; §§3.1–3.4 state, A2C, selectivity planner and latency-hiding pipeline | arXiv:2606.07923v1 §4 Experimental Evaluation; §4.1 setup; §§4.2–4.8 results, sensitivity, oracle and ablation | arXiv:2606.07923v1 §5 Discussion and Conclusion; §4.8 delayed-update counterevidence | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-07923 | complete |
| SF-2026-ARXIV-2606-07936 | RP-6950153e4880d488 | deep | arXiv:2606.07936v1 | SRC-ARXIV@arXiv:2606.07936v1 | arXiv:2606.07936v1 §3 Reporting Criteria and Codebook; §4 Dataset and Methods | arXiv:2606.07936v1 §5 Results over 284 manually reviewed and 1.8k+ LLM-assisted papers | arXiv:2606.07936v1 §6 Discussion and recommendations; the codebook measures reporting, not intrinsic judgment correctness | arXiv:2606.07936v1 https://github.com/larchlab/Illusions-of-the-Gold-Standard — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-07936 | complete |
| SF-2026-ARXIV-2606-07943 | RP-591bf06bdf9452a5 | deep | arXiv:2606.07943v1 | SRC-ARXIV@arXiv:2606.07943v1 | arXiv:2606.07943v1 §3 Poise Attack; §§3.1–3.5 eligibility, placement, generation and execution postcondition | arXiv:2606.07943v1 §4 Experimental Setup; §5 Results on Skill-Inject and SkillsBench | arXiv:2606.07943v1 §6 Limitations; audit false positives and eligible-task restriction | arXiv:2606.07943v1 SkillSafety/SkillTester artifact disclosed in manuscript; immutable event-time commit not pinned | claim:SF-2026-ARXIV-2606-07943 | complete |
| SF-2026-ARXIV-2606-07950 | RP-f45a8584f6534d21 | deep | arXiv:2606.07950v1 | SRC-ARXIV@arXiv:2606.07950v1 | arXiv:2606.07950v1 §4 CoDaPO; confidence/difficulty value, update weighting and within-mini-batch resampling | arXiv:2606.07950v1 §5 Experiments; §5.1 setup; Appendix C.6 implementation details | arXiv:2606.07950v1 §6 Conclusion; Appendix dynamic-difficulty analysis and fixed-compute boundary | arXiv:2606.07950v1 https://github.com/tmlr-group/CoDaPO — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-07950 | complete |
| SF-2026-ARXIV-2606-07957 | RP-614affaa0c0ed258 | deep | arXiv:2606.07957v1 | SRC-ARXIV@arXiv:2606.07957v1 | arXiv:2606.07957v1 §4 Demand-Driven Architecture; formal derivation and bidirectional catalogue/asset triggers | arXiv:2606.07957v1 §8 Evaluation Methodology; complexity analysis and worked example, not executed measurements | arXiv:2606.07957v1 §10 Limitations; rule correctness and alert prioritization explicitly out of scope | Not Disclosed — architecture paper provides no executable artifact | claim:SF-2026-ARXIV-2606-07957 | complete |
| SF-2026-ARXIV-2606-07968 | RP-2131f7f81797e463 | deep | arXiv:2606.07968v1 | SRC-ARXIV@arXiv:2606.07968v1 | arXiv:2606.07968v1 §IV RecurGuard; recurrence, volume and progress signals with three-chunk termination | arXiv:2606.07968v1 §VI Experimental Setup; §VII Results and adaptive stress tests | arXiv:2606.07968v1 §XI Limitations; exposed-trace dependency and topical adaptive miss boundary | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-07968 | complete |
| SF-2026-ARXIV-2606-07970 | RP-cc8fa4627aa85b66 | standard | arXiv:2606.07970v1 | SRC-ARXIV@arXiv:2606.07970v1 | arXiv:2606.07970v1 §3 Methods; bi-level Patcher inner attack and parallel implementation | arXiv:2606.07970v1 §4 Experiments; §4.1 setup and full-parameter attack transfer | arXiv:2606.07970v1 §6 Limitations and Conclusion; stronger simulated attacks remain a bounded threat-model proxy | arXiv:2606.07970v1 https://github.com/haomingwen/patcher — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-07970 | complete |
| SF-2026-ARXIV-2606-07992 | RP-8ef9550c4fbe545e | deep | arXiv:2606.07992v1 | SRC-ARXIV@arXiv:2606.07992v1 | arXiv:2606.07992v1 §3 Methodology; seven-dimensional mutation space and controlled error-path injection | arXiv:2606.07992v1 §4 Evaluation; Appendix C.1 controlled tool-error protocol | arXiv:2606.07992v1 §5 Discussion and Conclusion; production guardrails and controlled-environment boundary | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-07992 | complete |
| SF-2026-ARXIV-2606-08049 | RP-6c3238020ccefa82 | deep | arXiv:2606.08049v1 | SRC-ARXIV@arXiv:2606.08049v1 | arXiv:2606.08049v1 §3 SKILL.nb; selective formalization, versioned notebook and gate-conditioned local fallback; Appendix A | arXiv:2606.08049v1 §4 Experiments; shared Evaluation Protocol and WebArena/Mind2Web/GitLab migration slices | arXiv:2606.08049v1 §5 Limitations; Appendix A.8 lifecycle and environment-drift boundaries | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08049 | complete |
| SF-2026-ARXIV-2606-08094 | RP-1ba2dc9941ddd337 | deep | arXiv:2606.08094v1 | SRC-ARXIV@arXiv:2606.08094v1 | arXiv:2606.08094v1 §3 Runtime Design; §3.3 cached prefix/action expert and Algorithm 1 solver loop | arXiv:2606.08094v1 §4 Evaluation; §4.1 setup and 200-episode LIBERO-Object protocol | arXiv:2606.08094v1 §5 Limitations; deployment portability does not prove every VLA architecture behaviorally identical | arXiv:2606.08094v1 https://fai-modelopt-tech.github.io/vla-cpp.github.io/ — project, code and scaffold disclosed; commit not pinned | claim:SF-2026-ARXIV-2606-08094 | complete |
| SF-2026-ARXIV-2606-08106 | RP-181e2165eeb1d7c6 | deep | arXiv:2606.08106v1 | SRC-ARXIV@arXiv:2606.08106v1 | arXiv:2606.08106v1 §4 PACE; paired testing-by-betting e-process and Algorithm 1 commit gate | arXiv:2606.08106v1 §5 Experiments on prompt self-evolution with hidden real/no-gain conditions | arXiv:2606.08106v1 §6 Limitations; per-decision guarantee is not a global lifetime guarantee | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08106 | complete |
| SF-2026-ARXIV-2606-08197 | RP-1acca2d61481dff4 | deep | arXiv:2606.08197v1 | SRC-ARXIV@arXiv:2606.08197v1 | arXiv:2606.08197v1 §III AlignFed Framework; §IV version grouping, semantic calibration and fairness weighting | arXiv:2606.08197v1 §V Experimental Evaluation; §V-A setup | arXiv:2606.08197v1 §VI Conclusion and stated simulation/heterogeneous-edge scope | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08197 | complete |
| SF-2026-ARXIV-2606-08200 | RP-c424724066337887 | deep | arXiv:2606.08200v1 | SRC-ARXIV@arXiv:2606.08200v1 | arXiv:2606.08200v1 §3 Online Agent-as-a-Judge; in-world situation generation through native dialogue/action | arXiv:2606.08200v1 §4 Experiments; §4.1 life-simulation setup and human-label agreement | arXiv:2606.08200v1 §5 Discussion; evaluator intervention can change the trajectory it measures | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08200 | complete |
| SF-2026-ARXIV-2606-08302 | RP-e8b9b36b8d6d533f | standard | arXiv:2606.08302v1 | SRC-ARXIV@arXiv:2606.08302v1 | arXiv:2606.08302v1 §IV attention-head analysis; §V HACK++ calibration, decoupled attention/cache budgets and adaptive allocation | arXiv:2606.08302v1 §VI Experiments across VAR generation and understanding tasks | arXiv:2606.08302v1 §VII Conclusion; one-time calibration and VAR-specific head taxonomy bound transfer | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08302 | complete |
| SF-2026-ARXIV-2606-08317 | RP-18157f439471a95b | standard | arXiv:2606.08317v1 | SRC-ARXIV@arXiv:2606.08317v1 | arXiv:2606.08317v1 §II Methodology: Literature Selection and Analysis Framework; §VI-A Evaluation Dimensions; §IX-B Database Architecture Selection Framework, Stages 1–3 and scoring formula | arXiv:2606.08317v1 §VI-B Table I directional performance characteristics; §IX-D financial-fraud case study, Tables IV–V | arXiv:2606.08317v1 §IX-B Framework Limitations; §XI Limitations | Not Disclosed — exact-v1 PDF names no executable framework artifact or immutable repository revision | claim:SF-2026-ARXIV-2606-08317 | complete |
| SF-2026-ARXIV-2606-08340 | RP-b725cf5e0838ba57 | deep | arXiv:2606.08340v1 | SRC-ARXIV@arXiv:2606.08340v1 | arXiv:2606.08340v1 §3 alem benchmark design; procedural coordination tasks, communication and difficulty controls | arXiv:2606.08340v1 §4 Experiments; §4.1 zero-shot 13-LLM team setup and MARL reference | arXiv:2606.08340v1 §6 Limitations and Future Work; benchmark world and zero-shot policy scope | arXiv:2606.08340v1 https://github.com/alem-world/alem-env — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-08340 | complete |
| SF-2026-ARXIV-2606-08346 | RP-fbdeac65cf8a68f0 | standard | arXiv:2606.08346v1 | SRC-ARXIV@arXiv:2606.08346v1 | arXiv:2606.08346v1 §3 CATPO; informativeness score, critique-guided healing and normalized tree weighting | arXiv:2606.08346v1 §4 Experiments; §4.1 Qwen2.5-Math-1.5B on MATH and four test benchmarks | arXiv:2606.08346v1 §5 Conclusion; single base-model/math-training regime and critique cost bound generality | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08346 | complete |
| SF-2026-ARXIV-2606-08348 | RP-73a84954614a1376 | deep | arXiv:2606.08348v1 | SRC-ARXIV@arXiv:2606.08348v1 | arXiv:2606.08348v1 §3 Bayesian-Agent; verified trajectories, posterior skill beliefs, actions and guardrails | arXiv:2606.08348v1 §4 Experiments across RealFin-Bench, SOP-Bench, Lifelong AgentBench and harness ablations | arXiv:2606.08348v1 §5 Limitations; posterior repair depends on verifiable task artifacts | arXiv:2606.08348v1 https://github.com/DataArcTech/Bayesian-Agent — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-08348 | complete |
| SF-2026-ARXIV-2606-08367 | RP-5bf143c8206aefbc | deep | arXiv:2606.08367v1 | SRC-ARXIV@arXiv:2606.08367v1 | arXiv:2606.08367v1 §3 Platform Design; persistent memories, 120+ tools, live data and consequential governance | arXiv:2606.08367v1 §5.1 setup; §5.2 15-day cross-vendor results across five parallel worlds | arXiv:2606.08367v1 §8 Limitations; one 15-day simulation cannot establish deployment-timescale causality | arXiv:2606.08367v1 Prompts, logs and configurations released; immutable event-time revision not identified | claim:SF-2026-ARXIV-2606-08367 | complete |
| SF-2026-ARXIV-2606-08372 | RP-57893c6b157cfb73 | deep | arXiv:2606.08372v1 | SRC-ARXIV@arXiv:2606.08372v1 | arXiv:2606.08372v1 §2 taxonomy and attack families; §4 memorization test and RA-as-MIA reduction | arXiv:2606.08372v1 §3 empirical study of 14 attacks, 9 generators and 5 datasets; §4 interpretation tests | arXiv:2606.08372v1 §5.3 Limitations; black-box single-record released-table threat model | arXiv:2606.08372v1 Attack infrastructure disclosed through NIST CRC context; immutable event-time revision not pinned | claim:SF-2026-ARXIV-2606-08372 | complete |
| SF-2026-ARXIV-2606-08381 | RP-25e072b721b16333 | standard | arXiv:2606.08381v1 | SRC-ARXIV@arXiv:2606.08381v1 | arXiv:2606.08381v1 §3 comparative black-box framework; semantic-space divergence against a reference model set | arXiv:2606.08381v1 §4 Case Studies of previously reported provider-specific alignment behavior | arXiv:2606.08381v1 Limitations section; relative divergence detects difference, not absolute truth or provider intent | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-08381 | complete |
| SF-2026-ARXIV-2606-08382 | RP-332f47a0d4240ac0 | deep | arXiv:2606.08382v1 | SRC-ARXIV@arXiv:2606.08382v1 | arXiv:2606.08382v1 §3 STAR-KV; differentiable thresholds, key/value-specific factorization and rank-aware quantization | arXiv:2606.08382v1 §4 Experiments; Appendix A.4 kernel and benchmark details | arXiv:2606.08382v1 §5 Conclusion and ablations; low-rank sensitivity is model/workload dependent | arXiv:2606.08382v1 https://github.com/PriyanshBhatnagar/STAR-KV — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-08382 | complete |
| SF-2026-ARXIV-2606-08403 | RP-e6b091b49989fca9 | deep | arXiv:2606.08403v1 | SRC-ARXIV@arXiv:2606.08403v1 | arXiv:2606.08403v1 §3 Threat Model; §4 Carriers | arXiv:2606.08403v1 §5 Experimental Setup; §6 Results | arXiv:2606.08403v1 §7 Discussion; §8 Limitations | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08403 | complete |
| SF-2026-ARXIV-2606-08411 | RP-7284a77a8b918582 | deep | arXiv:2606.08411v1 | SRC-ARXIV@arXiv:2606.08411v1 | arXiv:2606.08411v1 §3 Methods; §§3.1–3.4 lane scheduling and execution | arXiv:2606.08411v1 §4 Experiments; §4.1 Experimental Setup | arXiv:2606.08411v1 §4.3 Ablation Study; §5 Conclusion | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08411 | complete |
| SF-2026-ARXIV-2606-08417 | RP-de0fffe767233ca0 | deep | arXiv:2606.08417v1 | SRC-ARXIV@arXiv:2606.08417v1 | arXiv:2606.08417v1 §3 Methodology; §§3.1–3.2 naive samplers and distributional metrics | arXiv:2606.08417v1 §4 Experiments | arXiv:2606.08417v1 §5 Conclusion; Appendix A parameter sweeps | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08417 | complete |
| SF-2026-ARXIV-2606-08432 | RP-b88778ec3d1ac037 | deep | arXiv:2606.08432v1 | SRC-ARXIV@arXiv:2606.08432v1 | arXiv:2606.08432v1 §4 Prefix Failure; §5 Trajectory-Refined Distillation | arXiv:2606.08432v1 §6 Experiments; Appendix C Evaluation Protocol | arXiv:2606.08432v1 §6.4–6.5 signal/trajectory analysis; Appendix B ablations | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08432 | complete |
| SF-2026-ARXIV-2606-08433 | RP-736ad903f0b9f8ea | deep | arXiv:2606.08433v1 | SRC-ARXIV@arXiv:2606.08433v1 | arXiv:2606.08433v1 Methodology in brief; §§2.1–2.6 six engine-level axes | arXiv:2606.08433v1 §3 Cross-axis reads; §4 Threat-model qualification matrix; §5 product portraits | arXiv:2606.08433v1 §6 Open questions; §7 Caveats and limitations | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08433 | complete |
| SF-2026-ARXIV-2606-08446 | RP-811af586caa2d54a | deep | arXiv:2606.08446v1 | SRC-ARXIV@arXiv:2606.08446v1 | arXiv:2606.08446v1 §3 Observation and Insights; §§3.1–3.3 stability/cost controls | arXiv:2606.08446v1 §4 Empirical Studies; §§4.1–4.5 | arXiv:2606.08446v1 Appendices A, D, E and §5 Conclusion | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08446 | complete |
| SF-2026-ARXIV-2606-08476 | RP-ffd6b54dcc79eb46 | deep | arXiv:2606.08476v1 | SRC-ARXIV@arXiv:2606.08476v1 | arXiv:2606.08476v1 §3 FlashCP Design; §§3.1–3.4 | arXiv:2606.08476v1 §4 Experiments; §4.1 Experiment Setup; §§4.2–4.3 | arXiv:2606.08476v1 §2.3 Limitation of Existing Works; §6 Conclusion | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08476 | complete |
| SF-2026-ARXIV-2606-08483 | RP-a319e8120bdee627 | deep | arXiv:2606.08483v1 | SRC-ARXIV@arXiv:2606.08483v1 | arXiv:2606.08483v1 §1 Question Design; §2 User Profile Simulation; §3 Technical Implementation | arXiv:2606.08483v1 §4 Evaluation Criteria; §5 Temporal Stability | arXiv:2606.08483v1 §6 Discussion and structural black-box limits | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08483 | complete |
| SF-2026-ARXIV-2606-08486 | RP-c44d3e318c9dbdf7 | deep | arXiv:2606.08486v1 | SRC-ARXIV@arXiv:2606.08486v1 | arXiv:2606.08486v1 §3 TRADE Model; §4 Training and Inference | arXiv:2606.08486v1 §6 Experiments; §6.1 Setup; §§6.2–6.5 | arXiv:2606.08486v1 §8 Limitations; Appendix A model configuration | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08486 | complete |
| SF-2026-ARXIV-2606-08517 | RP-3558b60ffde8b004 | deep | arXiv:2606.08517v1 | SRC-ARXIV@arXiv:2606.08517v1 | arXiv:2606.08517v1 §3 Problem, Setup, and Algorithm; §4 Joint Certificate | arXiv:2606.08517v1 §5 Experimental Evaluation; §5.1–5.3 | arXiv:2606.08517v1 §4.9 regime-separation scope; later experimental scope analysis | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08517 | complete |
| SF-2026-ARXIV-2606-08529 | RP-b0fd57e5e2ec79a9 | deep | arXiv:2606.08529v1 | SRC-ARXIV@arXiv:2606.08529v1 | arXiv:2606.08529v1 §3 Methodology; §§3.1–3.6 | arXiv:2606.08529v1 §4 Results; §§4.1–4.5 | arXiv:2606.08529v1 §6 Limitations; Appendix D incomplete cells/failure analysis | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08529 | complete |
| SF-2026-ARXIV-2606-08531 | RP-4abc16da7a5062a5 | deep | arXiv:2606.08531v1 | SRC-ARXIV@arXiv:2606.08531v1 | arXiv:2606.08531v1 §3 VESTA Framework; §§3.1–3.3 | arXiv:2606.08531v1 §4 Experimental Results and Analysis; §4.1 setup | arXiv:2606.08531v1 §5 Conclusion; Appendices D–H judge/protocol/trace evidence | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08531 | complete |
| SF-2026-ARXIV-2606-08539 | RP-436d086778fc83ea | deep | arXiv:2606.08539v1 | SRC-ARXIV@arXiv:2606.08539v1 | arXiv:2606.08539v1 §3 threat-type decomposition and trust-layer design; §4 self-improving dual store | arXiv:2606.08539v1 §5 evaluation and online replay; Tables 2–5 | arXiv:2606.08539v1 §6 Limitations; concurrency and fixed-verdict replay boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08539 | complete |
| SF-2026-ARXIV-2606-08574 | RP-fa8e96b4a3a59962 | deep | arXiv:2606.08574v1 | SRC-ARXIV@arXiv:2606.08574v1 | arXiv:2606.08574v1 §2 Method; §3 Theoretical Analysis | arXiv:2606.08574v1 §4 Experimental Settings; §5 Empirical Studies | arXiv:2606.08574v1 Appendix F Limitations and Future Work | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08574 | complete |
| SF-2026-ARXIV-2606-08590 | RP-59506c4656612cbc | deep | arXiv:2606.08590v1 | SRC-ARXIV@arXiv:2606.08590v1 | arXiv:2606.08590v1 §IV System Overview; §V Audit Checks | arXiv:2606.08590v1 §VI Snapshot Evaluation; §VII Live-Validation Status | arXiv:2606.08590v1 §VIII Failure Analysis; §IX Limitations and Future Work | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08590 | complete |
| SF-2026-ARXIV-2606-08610 | RP-b93e7693041602ad | deep | arXiv:2606.08610v1 | SRC-ARXIV@arXiv:2606.08610v1 | arXiv:2606.08610v1 §2 Robot RL Automation as a Harness Engineering Problem; §3 HARBOR | arXiv:2606.08610v1 §4 Experiments; §§4.1–4.3; Appendix D details | arXiv:2606.08610v1 §5 Conclusion, Limitations, and Future Work | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08610 | complete |
| SF-2026-ARXIV-2606-08615 | RP-695280f91c2bc82c | deep | arXiv:2606.08615v1 | SRC-ARXIV@arXiv:2606.08615v1 | arXiv:2606.08615v1 §3 streaming problem formulation; §§4–5 streaming-native VLM and harness | arXiv:2606.08615v1 §6 Streaming-Eval; §7 Experiment; §7.1 setup | arXiv:2606.08615v1 §7.4 Ablation Study; §9 Limitations | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08615 | complete |
| SF-2026-ARXIV-2606-08625 | RP-c38e5af4c9c823f7 | deep | arXiv:2606.08625v1 | SRC-ARXIV@arXiv:2606.08625v1 | arXiv:2606.08625v1 §2 rubric definition/taxonomy; §3 construction and optimization | arXiv:2606.08625v1 §4 evaluation use; §5 training use | arXiv:2606.08625v1 §6 reliability limits; §8 future directions and claim-bounded survey scope | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08625 | complete |
| SF-2026-ARXIV-2606-08635 | RP-0f4e522dab0e8c81 | deep | arXiv:2606.08635v1 | SRC-ARXIV@arXiv:2606.08635v1 | arXiv:2606.08635v1 §2 Problem Formulation; §4 SpectrumKV Policy | arXiv:2606.08635v1 §5 Experimental Setup; §6 Results; §7 Additional Analyses | arXiv:2606.08635v1 §8 Evidence boundary; §9 Limitations and Threats to Validity | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08635 | complete |
| SF-2026-ARXIV-2606-08661 | RP-f97713bdec2cab1d | deep | arXiv:2606.08661v1 | SRC-ARXIV@arXiv:2606.08661v1 | arXiv:2606.08661v1 §3 Threat Model and Overview; §4 Vulnerability Analysis | arXiv:2606.08661v1 §5 Evaluating Vulnerabilities; §6 Evaluation Details | arXiv:2606.08661v1 §6.4 sensitivity; §6.5 commercial-system generalization; §7 takeaways | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08661 | complete |
| SF-2026-ARXIV-2606-08671 | RP-a82bf081f9d5baa0 | deep | arXiv:2606.08671v1 | SRC-ARXIV@arXiv:2606.08671v1 | arXiv:2606.08671v1 §2 Method; §§2.2–2.3 harness and persistent decision history | arXiv:2606.08671v1 §3 Experiments; §3.1 Benchmarks and Evaluation Settings | arXiv:2606.08671v1 §5 Conclusion; unnumbered Limitations | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08671 | complete |
| SF-2026-ARXIV-2606-08679 | RP-95849c3d55f04a40 | deep | arXiv:2606.08679v1 | SRC-ARXIV@arXiv:2606.08679v1 | arXiv:2606.08679v1 §2 Task-level model ranking; §3 ranking across tasks | arXiv:2606.08679v1 §4 Experiments; §§4.1–4.3 | arXiv:2606.08679v1 Appendix D rank-interval interpretation and task selection | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08679 | complete |
| SF-2026-ARXIV-2606-08702 | RP-91f0efad6c3b07da | deep | arXiv:2606.08702v1 | SRC-ARXIV@arXiv:2606.08702v1 | arXiv:2606.08702v1 §3 budgeted context-control preliminaries; §4 Methodology; §§4.1–4.5 | arXiv:2606.08702v1 §5 Experiment; Appendix A.3 protocol | arXiv:2606.08702v1 §5.3 Additional Analysis and Discussion; appendix run-isolation boundaries | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08702 | complete |
| SF-2026-ARXIV-2606-08755 | RP-59a9da8811bade98 | deep | arXiv:2606.08755v1 | SRC-ARXIV@arXiv:2606.08755v1 | arXiv:2606.08755v1 §3 Preliminary negative results; §4 Skill-Augmented Policy Optimization | arXiv:2606.08755v1 §5 Experiments; §5.1 setup; §§5.2–5.5 | arXiv:2606.08755v1 §5.4 skill utility; §5.5 ablation; Appendix D negative/alternate results | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08755 | complete |
| SF-2026-ARXIV-2606-08761 | RP-26d0162d8ef832cb | deep | arXiv:2606.08761v1 | SRC-ARXIV@arXiv:2606.08761v1 | arXiv:2606.08761v1 §2 W4A4 performance gap; §3 APEX4 quantization; §4 pure-W4A4 kernel | arXiv:2606.08761v1 §5 Evaluation; §5.1 setup; §§5.2–5.4 | arXiv:2606.08761v1 §5.5 cross-platform analysis; §7 Conclusion and deployment boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08761 | complete |
| SF-2026-ARXIV-2606-08769 | RP-696219ef599e1551 | deep | arXiv:2606.08769v1 | SRC-ARXIV@arXiv:2606.08769v1 | arXiv:2606.08769v1 §III problem/data; §IV RadOT-Eval method | arXiv:2606.08769v1 §V Evaluation Protocol; §VI Results | arXiv:2606.08769v1 §VII Discussion, limitations, and evidence-transport boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08769 | complete |
| SF-2026-ARXIV-2606-08779 | RP-6ac8bc1e29dfeead | deep | arXiv:2606.08779v1 | SRC-ARXIV@arXiv:2606.08779v1 | arXiv:2606.08779v1 §3 engine-discrepancy decision space; §4 magic penalty; §5 discrepancy-constrained MDP | arXiv:2606.08779v1 §6 Experiments; setup, results, and ablations | arXiv:2606.08779v1 §7 Limitations and engine-identity boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08779 | complete |
| SF-2026-ARXIV-2606-08790 | RP-4e1f1a56de9d92b1 | deep | arXiv:2606.08790v1 | SRC-ARXIV@arXiv:2606.08790v1 | arXiv:2606.08790v1 §3 RAILS at a glance; §4 formal model; §§5–7 verification/settlement state machine | arXiv:2606.08790v1 §8 worked scenarios and exposure analysis | arXiv:2606.08790v1 Not Disclosed — no empirical limitations section; formal proposal is bounded to §§3–8 and does not prove real task completion | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08790 | complete |
| SF-2026-ARXIV-2606-08806 | RP-e2006528fa543c0b | deep | arXiv:2606.08806v1 | SRC-ARXIV@arXiv:2606.08806v1 | arXiv:2606.08806v1 §4 Governance Methodology and control chain | arXiv:2606.08806v1 §5 Results and artifact-policy analysis | arXiv:2606.08806v1 §6 Conclusion; provenance, approval, and auditability boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08806 | complete |
| SF-2026-ARXIV-2606-08813 | RP-d25e9f9679ad507c | deep | arXiv:2606.08813v1 | SRC-ARXIV@arXiv:2606.08813v1 | arXiv:2606.08813v1 §2 Aperon system architecture and HNTL layout | arXiv:2606.08813v1 §3 Implementation, hardware, and retrieval results | arXiv:2606.08813v1 §4 Conclusion; CPU/ANN-layout scope boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08813 | complete |
| SF-2026-ARXIV-2606-08831 | RP-5299d5b908b3f780 | deep | arXiv:2606.08831v1 | SRC-ARXIV@arXiv:2606.08831v1 | arXiv:2606.08831v1 §2 Setup and ancestor-conditioned DAG errors; §3 inference-time subgraph prediction and conformal calibration | arXiv:2606.08831v1 §4 Experiments | arXiv:2606.08831v1 §6 Limitations and graph/calibration assumptions | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08831 | complete |
| SF-2026-ARXIV-2606-08840 | RP-8a4e580d77c78613 | deep | arXiv:2606.08840v1 | SRC-ARXIV@arXiv:2606.08840v1 | arXiv:2606.08840v1 §III Evaluation Methodology | arXiv:2606.08840v1 §IV Results and execution failure modes | arXiv:2606.08840v1 §V Discussion and aggregate-pass-rate boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08840 | complete |
| SF-2026-ARXIV-2606-08867 | RP-4c709f8f12934eed | deep | arXiv:2606.08867v1 | SRC-ARXIV@arXiv:2606.08867v1 | arXiv:2606.08867v1 §4 Production support-agent system design | arXiv:2606.08867v1 §5 Case Study and evaluation; §6 offline/online measurement | arXiv:2606.08867v1 privacy, rollout, and production-readiness boundaries in §§6–7 | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08867 | complete |
| SF-2026-ARXIV-2606-08869 | RP-82b7a61caf152da2 | deep | arXiv:2606.08869v1 | SRC-ARXIV@arXiv:2606.08869v1 | arXiv:2606.08869v1 §II dynamic cloud-edge model; §III semantic-state framework | arXiv:2606.08869v1 §IV Implementation/training; §V Experimental Results | arXiv:2606.08869v1 §VI Conclusion and topology/workload scope | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08869 | complete |
| SF-2026-ARXIV-2606-08891 | RP-1716b2a3ac2e6be5 | deep | arXiv:2606.08891v1 | SRC-ARXIV@arXiv:2606.08891v1 | arXiv:2606.08891v1 §3 PALUTE Architecture Design; §§3.1–3.4 | arXiv:2606.08891v1 §4 Evaluation; §4.1 Experimental Setup; §§4.2–4.4 | arXiv:2606.08891v1 §4.3 sensitivity; §4.4 overhead; §5 Conclusion and simulation boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08891 | complete |
| SF-2026-ARXIV-2606-08892 | RP-c9361007b84371a7 | deep | arXiv:2606.08892v1 | SRC-ARXIV@arXiv:2606.08892v1 | arXiv:2606.08892v1 §2 diffuse-threat control framework; §§3–5 red/blue automated experiment planning | arXiv:2606.08892v1 §5 mitigations; Appendix C scorer details; Appendices D–G optimization/experiments | arXiv:2606.08892v1 §7 Limitations and Future Work; fuzzy-task and automated-scorer boundary | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08892 | complete |
| SF-2026-ARXIV-2606-08893 | RP-8b1a786f9f4f4d9a | deep | arXiv:2606.08893v1 | SRC-ARXIV@arXiv:2606.08893v1 | arXiv:2606.08893v1 §2 detector objective/architecture; §3 dataset cleaning and training | arXiv:2606.08893v1 §4 Results; §§4.1–4.6 | arXiv:2606.08893v1 §5 Conclusion/Future Work; Appendix A negative path and robustness ablations | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-08893 | complete |
| SF-2026-ARXIV-2606-08919 | RP-1c43fd6dc866112a | deep | arXiv:2606.08919v1 | SRC-ARXIV@arXiv:2606.08919v1 | arXiv:2606.08919v1 §3 Selective Classification; §4 Endogenous Reviewer Model | arXiv:2606.08919v1 §5 Experiments | arXiv:2606.08919v1 §6 Limitations and Human-Study Boundary | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-08919 | complete |
| SF-2026-ARXIV-2606-08950 | RP-aeb8f92ff95552f7 | deep | arXiv:2606.08950v1 | SRC-ARXIV@arXiv:2606.08950v1 | arXiv:2606.08950v1 §III Methodology | arXiv:2606.08950v1 §§IV–V Cloud/HPC and lifecycle evaluation | arXiv:2606.08950v1 §VI Discussion and Conclusion | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-08950 | complete |
| SF-2026-ARXIV-2606-08960 | RP-19e5f9067a226a60 | deep | arXiv:2606.08960v1 | SRC-ARXIV@arXiv:2606.08960v1 | arXiv:2606.08960v1 §3 The Hacker-Fixer Loop; Appendix D | arXiv:2606.08960v1 §4 Hardening Results | arXiv:2606.08960v1 Appendix A Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-08960 | complete |
| SF-2026-ARXIV-2606-09005 | RP-2b72d8ce152645a9 | deep | arXiv:2606.09005v1 | SRC-ARXIV@arXiv:2606.09005v1 | arXiv:2606.09005v1 §III System and Attacker Model; §III-C Control/Data Boundary | arXiv:2606.09005v1 §§IV–V Experimental Design and Results | arXiv:2606.09005v1 §X Limitations and Validity Threats | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09005 | complete |
| SF-2026-ARXIV-2606-09061 | RP-142528f9f795ddd5 | deep | arXiv:2606.09061v1 | SRC-ARXIV@arXiv:2606.09061v1 | arXiv:2606.09061v1 §3 The Developed Methodology | arXiv:2606.09061v1 §4 Experiment and Evaluation | arXiv:2606.09061v1 §4.6 Discussion; §5 Future Work | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09061 | complete |
| SF-2026-ARXIV-2606-09084 | RP-233ac36cbc14e4e3 | deep | arXiv:2606.09084v1 | SRC-ARXIV@arXiv:2606.09084v1 | arXiv:2606.09084v1 §3 Context-Fractured Decomposition | arXiv:2606.09084v1 §4 Evaluation | arXiv:2606.09084v1 §5 Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09084 | complete |
| SF-2026-ARXIV-2606-09441 | RP-8afa327b0d33b3f8 | deep | arXiv:2606.09441v1 | SRC-ARXIV@arXiv:2606.09441v1 | arXiv:2606.09441v1 §§3–5 Attention invariance, SIFT design and implementation | arXiv:2606.09441v1 §§6–7 Evaluation Methodology and Results | arXiv:2606.09441v1 §9 Conclusion; no dedicated limitations section | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09441 | complete |
| SF-2026-ARXIV-2606-09613 | RP-76c31794bf2fa4e4 | deep | arXiv:2606.09613v1 | SRC-ARXIV@arXiv:2606.09613v1 | arXiv:2606.09613v1 §3 AgentServeSim | arXiv:2606.09613v1 §§4–6 Setup, validation and design-space exploration | arXiv:2606.09613v1 §7 Limitations and Future Work | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09613 | complete |
| SF-2026-ARXIV-2606-09643 | RP-10e7ea9d62fe3870 | deep | arXiv:2606.09643v1 | SRC-ARXIV@arXiv:2606.09643v1 | arXiv:2606.09643v1 §3 FMplex Design | arXiv:2606.09643v1 §§4–6 Implementation and Evaluation | arXiv:2606.09643v1 §7 Discussion and Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09643 | complete |
| SF-2026-ARXIV-2606-09682 | RP-61cc1e75c9192f52 | deep | arXiv:2606.09682v1 | SRC-ARXIV@arXiv:2606.09682v1 | arXiv:2606.09682v1 §3 AutoMegaKernel Harness | arXiv:2606.09682v1 §4 Evaluation | arXiv:2606.09682v1 §5 Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09682 | complete |
| SF-2026-ARXIV-2606-09686 | RP-a247e1a62c95aa15 | deep | arXiv:2606.09686v1 | SRC-ARXIV@arXiv:2606.09686v1 | arXiv:2606.09686v1 §§2–4 Numeric Catalog and Conformance Model | arXiv:2606.09686v1 §§5–6 Validation and Results | arXiv:2606.09686v1 §7 Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09686 | complete |
| SF-2026-ARXIV-2606-09692 | RP-8343d97fdcdec84f | deep | arXiv:2606.09692v1 | SRC-ARXIV@arXiv:2606.09692v1 | arXiv:2606.09692v1 §2 Delegation-Observable Execution; §3 Common Information Model | arXiv:2606.09692v1 §§4–5 Gateway and Evaluation | arXiv:2606.09692v1 §6 Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09692 | complete |
| SF-2026-ARXIV-2606-09711 | RP-47fd9e2b0553e006 | deep | arXiv:2606.09711v1 | SRC-ARXIV@arXiv:2606.09711v1 | arXiv:2606.09711v1 §§2–4 PRIME Definition, Probes and Interventions | arXiv:2606.09711v1 §5 Experiments | arXiv:2606.09711v1 §6 Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09711 | complete |
| SF-2026-ARXIV-2606-09774 | RP-46f0ca3172e30fcf | deep | arXiv:2606.09774v1 | SRC-ARXIV@arXiv:2606.09774v1 | arXiv:2606.09774v1 §§3–4 SIGA Adapter and Self-Evolution | arXiv:2606.09774v1 §§5–6 Evaluation | arXiv:2606.09774v1 Appendix F Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09774 | complete |
| SF-2026-ARXIV-2606-09809 | RP-10455601ceb4ea42 | deep | arXiv:2606.09809v1 | SRC-ARXIV@arXiv:2606.09809v1 | arXiv:2606.09809v1 §§3–5 Evaluation Cards Schema and Interpretive Signals | arXiv:2606.09809v1 §§6–8 Deployment and Analysis | arXiv:2606.09809v1 Appendix J Limitations | Not Disclosed — no later artifact is used | claim:SF-2026-ARXIV-2606-09809 | complete |

### Source Reviews

<!-- review:SF-TRAIT-MISALIGNMENT-MONITOR:start -->
### Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning

<!-- claim:SF-TRAIT-MISALIGNMENT-MONITOR:start -->只靠周期性行为评估能发现 emergent misalignment，但检测间隔长且成本高。该方法把七个 alignment trait 编成 activation direction，跨 checkpoint 追踪低维 drift，并用该 profile 训练轻量 monitor。 四个 7–9B 模型和 14B stress test 支持研究 regime 内的 AUROC/误报漏报；内部 drift 只是 sensor，跨模型、起始 misalignment 与更长训练需要重校准。它需要白盒 activation 访问，不能取代行为验收或 effect-time policy。<!-- claim:SF-TRAIT-MISALIGNMENT-MONITOR:end -->
Deep evidence contract：Method/identity=`arXiv:2606.07631v1 exact-v1 HTML § `3 Methodology`; § `3.1 Two-Phase Trait-Space Representation`; § `3.2 Finetuning Protocol``；Evaluation=`arXiv:2606.07631v1 exact-v1 HTML § `4 Trait-space Geometry of Finetuning Drift`; § `5 Stress Tests`; Appendix `9 EM Evaluation Protocol``；Limitations/counterevidence=`arXiv:2606.07631v1 exact-v1 HTML § `6 Discussion and Conclusion` (`Calibration scope`; `Caveats and technical limits`)`；Artifact=`Not Disclosed — arXiv:2606.07631v1 exact-v1 HTML does not pin an immutable implementation revision`。Owner/authority：`Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning` 的长期机制归入 `PLATFORM-MONITORING`；activation/trace warning 只负责在线风险与浪费信号；behavioral evaluation、environment outcome 和 operator policy 决定是否阻断。
<!-- review:SF-TRAIT-MISALIGNMENT-MONITOR:end -->

<!-- review:SF-ML-LIFECYCLE-ASSESSMENT:start -->
### Position: Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment

**问题、旧路径与约束变化。** Per-training-run energy or per-query inference cost is useful for local optimization but can move impact into data preparation, experimentation, refresh, embodied infrastructure or retirement. The comparison becomes meaningful only after a functional unit and a life-cycle boundary are frozen.

**Mechanism、state/data/control owner 与实现。** Model life-cycle assessment expands efficiency accounting from one training run or inference sample to data, experimentation, deployment, refresh, infrastructure and retirement under an explicit functional unit. The governed state is an inventory keyed by functional unit, stage boundary, model/service revision, hardware lifetime allocation, utilization and regional resource factors. Component operators own measured activity; the LCA/evaluation owner owns boundary and allocation rules; an aggregate report may compose disclosed records but cannot invent missing vendor telemetry. Method/identity 定位为 `arXiv:2606.07632v1 exact-v1 PDF § `3 Life Cycle Assessment for ML Models`; § `3.1 Goal Definition and Scoping``；artifact 定位为 `Not Disclosed — arXiv:2606.07632v1 does not pin an immutable implementation revision`。未披露的实现 revision、runtime 或硬件路径不作补写。

**Evaluation、证明与未证明。** Evaluation 定位为 `arXiv:2606.07632v1 exact-v1 PDF § `3.5 Case Study: Comparing the Effects of LLM System Design Choices with LCA`; § `4 Alternative Views``；limitations/counterevidence 定位为 `arXiv:2606.07632v1 exact-v1 PDF § `2 Limitations in Existing Approaches to Evaluating ML’s Resource Needs`; § `5 Benefits of LCAs in Machine Learning``。The framework and case-study accounting show how changing the boundary can reverse a design comparison and expose omitted stages. They do not recover undisclosed energy, water, embodied-carbon or fleet-utilization data, and sector projections retain inventory and allocation uncertainty. 原文边界保持为：Inventory boundaries and sector projections retain uncertainty; an LCA framework supports comparable accounting but does not supply undisclosed vendor energy data.

**Trade-off、failure mode 与共存。** Broader accounting improves comparability but raises collection cost, supplier dependence and double-counting risk. A narrow metric can undercount shifted cost; an over-broad or unstable functional unit can make alternatives incomparable. Run-level measurements remain valid for a bounded engineering decision when their excluded stages are explicit.

**Evolution 与系统位置。** The owner evolves from isolated accelerator efficiency to a versioned life-cycle evidence object; the next pressure is auditable supplier data and uncertainty propagation rather than a single universal footprint number. 关系限定为 `Direct Evolution`；Books disposition 为 `No Change — Existing Coverage`。

<!-- claim:SF-ML-LIFECYCLE-ASSESSMENT:start -->Model life-cycle assessment expands efficiency accounting from one training run or inference sample to data, experimentation, deployment, refresh, infrastructure and retirement under an explicit functional unit. 证据边界：Inventory boundaries and sector projections retain uncertainty; an LCA framework supports comparable accounting but does not supply undisclosed vendor energy data.<!-- claim:SF-ML-LIFECYCLE-ASSESSMENT:end -->
<!-- review:SF-ML-LIFECYCLE-ASSESSMENT:end -->

<!-- review:SF-2026-ARXIV-2606-07684:start -->
### 2606.07684 — Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching

**问题与旧分支。** SCD addresses these challenges via two mechanisms: (1) Reuse, which reconstructs most layers from low-rank subspaces to minimize transfer cost, and (2) Patch, which predicts normalized inputs at sparse transition layers to truncate error propagation. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We propose Semantic Cache Distillation (SCD), a loss-constrained framework that replaces raw KV transmission with compact semantic codes. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MEMORY`，对应 `books/part-07-agent/77-memory.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07684v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07684:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07684:end -->
<!-- review:SF-2026-ARXIV-2606-07684:end -->

<!-- review:SF-2026-ARXIV-2606-07687:start -->
### 2606.07687 — What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction

**问题与旧分支。** Video world models are increasingly used to provide predictive visual representations, yet it remains unclear which pretraining signals induce action-relevant structure in their latent spaces. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We study this question through a unified probe-based evaluation across diverse encoder families, including image-only self-supervision, video pretraining with and without latent prediction, reconstruction-based autoencoders, diffusion models, and shortcut-forcing dynamics models. 本次 exact-v1 全文复核把 canonical owner 固定为 `MULTIMODAL-WORLD-MODELS`，对应 `books/part-03-multimodal-world-models/25-multimodal-world-models.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** Our results identify temporal predictive structure -- not reconstruction fidelity -- as the primary ingredient underlying action-relevant video representations. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07687v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07687:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07687:end -->
<!-- review:SF-2026-ARXIV-2606-07687:end -->

<!-- review:SF-2026-ARXIV-2606-07703:start -->
### 2606.07703 — How Much Dense Attention is Necessary? Oracle-Guided Sparse Prefill for Full/GQA Layers in Hybrid Long-Context Models

**问题与旧分支。** Long-context prefill remains expensive because full/GQA layers still score the historical sequence, even in hybrid models with local, sparse, linear, or recurrent components. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We introduce an attention-mass top-k oracle for existing GQA checkpoints: for each layer and query position, it computes dense attention, selects head-averaged token support, and recomputes attention only on that support. 本次 exact-v1 全文复核把 canonical owner 固定为 `INFER-PREFILL`，对应 `books/part-05-inference-system/43-prefill.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07703v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07703:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07703:end -->
<!-- review:SF-2026-ARXIV-2606-07703:end -->

<!-- review:SF-2026-ARXIV-2606-07710:start -->
### 2606.07710 — WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing

**问题与旧分支。** The autoregressive nature of large language models (LLMs) remains a significant bottleneck for inference, particularly in complex agentic workloads. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** To address this volatility, we introduce WhiFlash, the first cross-paradigm SD method that unifies autoregressive and diffusion-based parallel drafting under a single token-level controller. 本次 exact-v1 全文复核把 canonical owner 固定为 `INFER-SPECULATIVE-DECODING`，对应 `books/part-05-inference-system/48-speculative-decoding.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07710v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07710:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07710:end -->
<!-- review:SF-2026-ARXIV-2606-07710:end -->

<!-- review:SF-2026-ARXIV-2606-07713:start -->
### 2606.07713 — Attention at the Theoretical Minimum: A Mathematics of Arrays Framework for Memory-Optimal Transformer Kernels

**问题与旧分支。** The attention mechanism is the dominant computational bottleneck in modern transformer-based AI. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We present a Mathematics of Arrays (MoA) reformulation of scaled dot-product attention and its numerically stable softmax, deriving a Denotational Normal Form (DNF) that eliminates all intermediate arrays -- including the implicit transposed-key buffer and every softmax temporary -- by algebraic construction rather than empirical tuning. 本次 exact-v1 全文复核把 canonical owner 固定为 `INFER-TENSORRT-LLM`，对应 `books/part-05-inference-system/49-tensorrt-llm.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07713v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07713:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07713:end -->
<!-- review:SF-2026-ARXIV-2606-07713:end -->

<!-- review:SF-2026-ARXIV-2606-07720:start -->
### 2606.07720 — Why Limit the Residual Stream to Layers and Not Tokens? Persistent Memory for Continuous Latent Reasoning

**问题与旧分支。** However, we identify a limitation we term the \textbf{concept bottleneck}. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** To address this, we propose \textbf{AGCLR} (Adaptive Gated Continuous Latent Reasoning), which augments CoCoNuT with a \textit{Gated Concept Stream}. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-CONTEXT`，对应 `books/part-07-agent/75-context.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** Large language models (LLMs) have demonstrated remarkable reasoning abilities on mathematical and multi-hop planning tasks. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07720v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07720:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07720:end -->
<!-- review:SF-2026-ARXIV-2606-07720:end -->

<!-- review:SF-2026-ARXIV-2606-07726:start -->
### 2606.07726 — Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm that Provably Exploits Model Similarity

**问题与旧分支。** Large Language Models are typically benchmarked by evaluating every model on every test query. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We propose Synchronized Successive Rejects (SySRs), augmenting the classical Successive Rejects algorithm with paired comparisons. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** Unlike prior attempts to leverage model similarity in best-model identification, our approach is hyperparameter-free and enjoys performance guarantees that improve with the degree of similarity between evaluated models. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07726v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07726:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07726:end -->
<!-- review:SF-2026-ARXIV-2606-07726:end -->

<!-- review:SF-2026-ARXIV-2606-07783:start -->
### 2606.07783 — Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval

**问题与旧分支。** In misinformation-rich environments, however, retrieved content may include plausible but incorrect information, raising concerns about the reliability of RAG-based information access systems. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** In this work, we propose an evaluation protocol to systematically test how the RAG system handles conflicts between parametric knowledge and evidence retrieved from context with varying amounts of misleading information. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07783v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07783:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07783:end -->
<!-- review:SF-2026-ARXIV-2606-07783:end -->

<!-- review:SF-2026-ARXIV-2606-07790:start -->
### 2606.07790 — Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games

**问题与旧分支。** Multi-agent LLM systems increasingly rely on communication protocols for coordination, yet their robustness under adversarial and structural constraints remains poorly understood. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Building on prior work showing that cheap-talk channels enable cooperation in LLM coordination games, we investigate two vulnerability classes in a 4-player Stag Hunt across six model families and 720 trials. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MULTI-AGENT`，对应 `books/part-07-agent/82-multi-agent.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07790v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07790:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07790:end -->
<!-- review:SF-2026-ARXIV-2606-07790:end -->

<!-- review:SF-2026-ARXIV-2606-07805:start -->
### 2606.07805 — Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems

**问题与旧分支。** The rapid evolution of Large Language Models (LLMs) from passive assistants to autonomous, execution-capable agents has introduced critical operational risks. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Most current evaluation frameworks neglect procedural compliance, leading to ''Machiavellian'' behaviors where agents strategically violate safety rules to maximize rewards - a direct manifestation of Goodhart's Law. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MULTI-AGENT`，对应 `books/part-07-agent/82-multi-agent.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** To address this blind spot, we introduce MAC-Bench, a dynamic, adversarial benchmark designed to evaluate the procedural alignment of multi-agent systems under realistic pressure. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07805v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07805:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07805:end -->
<!-- review:SF-2026-ARXIV-2606-07805:end -->

<!-- review:SF-2026-ARXIV-2606-07808:start -->
### 2606.07808 — Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models

**问题与旧分支。** Existing benchmarks largely measure this behavior end-to-end, asking whether the final response is compliant. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We introduce a white-box diagnostic framework that localizes instruction hierarchy failures into instruction identification, conflict resolution, and response realization, making failures more interpretable. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-SECURITY`，对应 `books/part-06-ai-infrastructure/72-security.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** We evaluate three reasoning models--Gemma-4-31B-IT, Qwen3.6-35B-A3B, and Claude Sonnet 4.6--on long-context adaptations of IHEval and IHChallenge, and find that the dominant failure mode varies across models, tasks, and context length. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07808v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07808:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07808:end -->
<!-- review:SF-2026-ARXIV-2606-07808:end -->

<!-- review:SF-2026-ARXIV-2606-07822:start -->
### 2606.07822 — The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust

**问题与旧分支。** Unfortunately, even as models improve, they remain poorly calibrated, often biasing towards overconfidence. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Calibration is a good proxy for trust: well-calibrated confidence estimates help inform the risk versus reward tradeoff when trusting a specific model output. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07822v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07822:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07822:end -->
<!-- review:SF-2026-ARXIV-2606-07822:end -->

<!-- review:SF-2026-ARXIV-2606-07833:start -->
### 2606.07833 — Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks

**问题与旧分支。** Standard AI red teaming evaluations reduce adversarial campaigns to a single binary outcome, attack success rate (ASR), not taking into account the sequential structure of how models resist or yield to attacks. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We propose applying process mining, a discipline for discovering and analyzing process models from event logs, to red teaming traces. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-SECURITY`，对应 `books/part-06-ai-infrastructure/72-security.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** We conduct a controlled experiment pitting 60 HarmBench prompts against two LLMs, GPT-OSS 120B and Llama 3.3 70B, using 10 prompt mutation strategies over up to 110 attempts per prompt. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07833v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07833:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07833:end -->
<!-- review:SF-2026-ARXIV-2606-07833:end -->

<!-- review:SF-2026-ARXIV-2606-07834:start -->
### 2606.07834 — Cherry-pick Override: Unsafe Directional Commitment in LLM Judges under Mixed Evidence

**问题与旧分支。** LLM judges increasingly turn verdicts into system commitments. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Under mixed evidence (claims with both supporting and refuting sources) this is unsafe: when the schema exposes CONFLICTING as the authorized non-directional verdict, returning SUPPORTS/REFUTES is an unauthorized directional commitment, a failure we name Cherry-pick Override (CCO). 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** A minimal two-channel reference probe reaches operating points neither single channel reaches; under the random-veto null its promotion to CONFLICTING is structurally targeted on AVeriTeC (empirical p &lt; 1/2001) and weaker but in the same direction on VitaminC-Mixed, a selectivity result rather than a magnitude one. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07834v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07834:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07834:end -->
<!-- review:SF-2026-ARXIV-2606-07834:end -->

<!-- review:SF-2026-ARXIV-2606-07845:start -->
### 2606.07845 — GRPO Does Not Close the Multi-Agent Coordination Gap

**问题与旧分支。** We measure how well current large language models coordinate as multiple agents sharing a common resource, using the dining philosophers problem as a clean test bed. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Across 630 episodes spanning seven models and three philosopher counts, four frontier closed-source systems reach mean reward 0.45 to 0.87 and Mistral-Small 24B reaches 0.83 to 0.99, while Qwen3-14B reaches 0.13 to 0.35. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MULTI-AGENT`，对应 `books/part-07-agent/82-multi-agent.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** Two further observations qualify the result. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07845v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07845:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07845:end -->
<!-- review:SF-2026-ARXIV-2606-07845:end -->

<!-- review:SF-2026-ARXIV-2606-07846:start -->
### 2606.07846 — Cost-Aware Speculative Execution for LLM-Agent Workflows: An Integrated Five-Dimension Method

**问题与旧分支。** We specify the runtime mechanics, a closed-form result that the rule self-limits as the upstream branching factor grows, a five-stage calibration pipeline (offline replay, shadow, canary, online calibration, drift-triggered kill-switch), and a workload-fit rubric over eight production archetypes. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Speculative execution can reclaim that idle time by launching a downstream operation with a predicted upstream input, but here each speculation costs real money (per-token billing) and its success probability is hard to estimate and drifts over time. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-WORKFLOW`，对应 `books/part-07-agent/81-workflow.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** We specify the runtime mechanics, a closed-form result that the rule self-limits as the upstream branching factor grows, a five-stage calibration pipeline (offline replay, shadow, canary, online calibration, drift-triggered kill-switch), and a workload-fit rubric over eight production archetypes. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07846v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07846:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07846:end -->
<!-- review:SF-2026-ARXIV-2606-07846:end -->

<!-- review:SF-2026-ARXIV-2606-07856:start -->
### 2606.07856 — Teacher-Free Self-Training Amplifies but Does Not Compound: A Pass@$K$ Crossover on a Free-Verifier Domain

**问题与旧分支。** (ii) Per-round STaR self-training raises the ceiling but never accelerates -- the gain tracks remaining headroom and decelerates across $K=4$ independent training trajectories. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We make the question decidable with a teacher-free "constellation" -- a generator, a learned critic, and a free exact verifier -- on a FlashFill-style "trapdoor" DSL, where verified (problem, solution) pairs are cheap to synthesize, hard to invert, and free to check exactly. 本次 exact-v1 全文复核把 canonical owner 固定为 `TRAIN-SFT`，对应 `books/part-04-training-system/29-sft.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07856v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07856:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07856:end -->
<!-- review:SF-2026-ARXIV-2606-07856:end -->

<!-- review:SF-2026-ARXIV-2606-07867:start -->
### 2606.07867 — The Cold-Start Safety Gap in LLM Agents

**问题与旧分支。** Are tool-calling LLM agents equally safe throughout a conversation? 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** To study this systematically, we introduce Safety Over Depth for Agents (SODA), a benchmark that controls how many regular agentic tasks the agent completes before encountering a safety threat, supporting up to 20 preceding tasks. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-SECURITY`，对应 `books/part-06-ai-infrastructure/72-security.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07867v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07867:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07867:end -->
<!-- review:SF-2026-ARXIV-2606-07867:end -->

<!-- review:SF-2026-ARXIV-2606-07874:start -->
### 2606.07874 — Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators

**问题与旧分支。** LLMs-as-judges are the only way to evaluate safety at scale. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Despite their importance, LLM-judges themselves are rarely evaluated beyond human agreement in simple, static benchmarks. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** LLMs-as-judges are the only way to evaluate safety at scale. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07874v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07874:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07874:end -->
<!-- review:SF-2026-ARXIV-2606-07874:end -->

<!-- review:SF-2026-ARXIV-2606-07878:start -->
### 2606.07878 — Still: Amortized KV Cache Compaction in a Single Forward Pass

**问题与旧分支。** Existing compaction methods satisfy only part of this requirement: selection methods are lightweight but subset-bound, while synthesis methods are expressive but rely on per-context optimization. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** Here we introduce Still, a small per-layer Perceiver trained once against a frozen base model that produces compact keys and values in a single forward pass. 本次 exact-v1 全文复核把 canonical owner 固定为 `INFER-KV-CACHE`，对应 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** We show that amortization makes long-context cache compaction tractable, and synthesis makes its compact state useful at extreme compression. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07878v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07878:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07878:end -->
<!-- review:SF-2026-ARXIV-2606-07878:end -->

<!-- review:SF-2026-ARXIV-2606-07881:start -->
### 2606.07881 — Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency

**问题与旧分支。** Pipeline parallelism is essential for training large neural networks, but existing schedules trade off throughput, memory, and optimization consistency. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We introduce PACI (Pipeline Asynchronous training with Controlled Inconsistency), a bubble-free asynchronous pipeline method that bounds forward/backward version drift without weight stashing, prediction, additional parameter copies, or global synchronization. 本次 exact-v1 全文复核把 canonical owner 固定为 `TRAIN-PIPELINE-PARALLEL`，对应 `books/part-04-training-system/38-pipeline-parallel.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** These results show that forward/backward inconsistency need not be eliminated: when explicitly bounded, it can be safely traded for substantial efficiency gains. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07881v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07881:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07881:end -->
<!-- review:SF-2026-ARXIV-2606-07881:end -->

<!-- review:SF-2026-ARXIV-2606-07889:start -->
### 2606.07889 — Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories

**问题与旧分支。** LLM-based coding agents sometimes acknowledge a problem in their own reasoning and then proceed anyway. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We call this pattern strained coherence: a safety-relevant failure mode in which an agent has information that should change its behavior, states that information, and still acts against it. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-MONITORING`，对应 `books/part-06-ai-infrastructure/67-monitoring.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** We give an operational definition, build a Claude Sonnet 4.6 judge that reads full trajectories and flags spans where the pattern occurs, and evaluate it on 44 Terminal-bench-2 trajectories using a Qwen3.5-35B-A3B backbone. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07889v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07889:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07889:end -->
<!-- review:SF-2026-ARXIV-2606-07889:end -->

<!-- review:SF-2026-ARXIV-2606-07904:start -->
### 2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents

**问题与旧分支。** However, manually writing and maintaining such contracts does not scale to large or changing tool ecosystems. 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** We introduce Contract2Tool, a framework for inferring tool contracts from metadata, schemas, documentation, and execution traces. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-TOOL-CALLING`，对应 `books/part-07-agent/78-tool-calling.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** Contract2Tool converts observable tool evidence into normalized symbolic contracts that can be evaluated intrinsically and deployed inside downstream causal tool filtering. Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `https://arxiv.org/html/2606.07904v1`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:SF-2026-ARXIV-2606-07904:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:SF-2026-ARXIV-2606-07904:end -->
<!-- review:SF-2026-ARXIV-2606-07904:end -->

<!-- review:SF-2026-ARXIV-2606-07923:start -->
<!-- claim:SF-2026-ARXIV-2606-07923:start -->
Larch: Learned Query Optimization for Semantic Predicates 处理的问题是：Online selectivity learning plus exact per-row ordering makes semantic-predicate token cost query-planner state rather than an opaque LLM charge.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Larch; §§3.1–3.4 state, A2C, selectivity planner and latency-hiding pipeline`。状态 owner 为 `INFER-SCHEDULING`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experimental Evaluation; §4.1 setup; §§4.2–4.8 results, sensitivity, oracle and ablation` 提供可复核结果。

评估证明边界：workload=`Three real datasets plus three semantic-filter workloads and synthetic selectivity/horizon sweeps`；model=`Semantic-filter LLM backends and lightweight A2C/selectivity models; exact backend matrix is workload-specific`；evaluator=`Token use/cost overhead, convergence, sensitivity, oracle comparison and update latency`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Discussion and Conclusion; §4.8 delayed-update counterevidence`。

取舍、failure、共存与演进：Larch-Sel buys token savings with an online estimator whose errors can reorder individual rows; static PZ/Quest-style plans remain the fallback before enough labels accrue or when embeddings are unavailable. Its evolution is from global heuristic order to learned per-row selectivity plus exact dynamic programming, not a new semantic operator. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-07923:end -->
<!-- review:SF-2026-ARXIV-2606-07923:end -->

<!-- review:SF-2026-ARXIV-2606-07936:start -->
<!-- claim:SF-2026-ARXIV-2606-07936:start -->
Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation 处理的问题是：Twenty reproducibility fields separate what human judges measured, who judged, and how judgments may be interpreted; this changes the evaluation receipt contract.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Reporting Criteria and Codebook; §4 Dataset and Methods`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5 Results over 284 manually reviewed and 1.8k+ LLM-assisted papers` 提供可复核结果。

评估证明边界：workload=`284 confirmed manual *CL 2023–2025 papers plus LLM-assisted labeling of the remaining long-form/human-evaluation corpus`；model=`GPT-4o-mini-2025-04-16 for automatic annotation; Gemini-2.5-Pro and Claude-3.7-Sonnet-20250219 in model-selection pilot`；evaluator=`Manual IAA; GPT-4o-mini selection on 26 papers; independent 125-paper/3,875-label validation; bootstrap reporting rates`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Discussion and recommendations; the codebook measures reporting, not intrinsic judgment correctness`。

取舍、failure、共存与演进：A twenty-field codebook raises reporting cost and can measure whether a study is reproducible without proving that its human judgments are valid. It coexists with task-specific quality rubrics: the contribution is a receipt schema for who judged, what was measured and how results may be interpreted. Artifact 边界：`https://github.com/larchlab/Illusions-of-the-Gold-Standard — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07936:end -->
<!-- review:SF-2026-ARXIV-2606-07936:end -->

<!-- review:SF-2026-ARXIV-2606-07943:start -->
<!-- claim:SF-2026-ARXIV-2606-07943:start -->
Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents 处理的问题是：Postcondition-validated payload execution jointly with legitimate-task success changes skill-poisoning evidence from invocation to completed side effect, while position controls stealth and reliability.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Poise Attack; §§3.1–3.5 eligibility, placement, generation and execution postcondition`。状态 owner 为 `PLATFORM-SECURITY`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experimental Setup; §5 Results on Skill-Inject and SkillsBench` 提供可复核结果。

评估证明边界：workload=`Skill-Inject 25 eligible tasks ×3 harms and SkillsBench 27 tasks ×3, two trials/configuration`；model=`codex+gpt-5.2; OpenClaw+DeepSeek-V4-Flash/Pro; Claude Code+Sonnet-4.6`；evaluator=`Joint ASR, task verifier, postcondition verifier and four-judge SkillTester delta alerts`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations; audit false positives and eligible-task restriction`。

取舍、failure、共存与演进：Moving the payload from YAML to a locally plausible body position trades visibility for dependence on the agent reading that position. The joint verifier avoids invocation-only false success, while SkillTester's high clean-skill false-positive rate shows that LLM alerts cannot replace sandbox effect evidence or conservative skill admission. Artifact 边界：`SkillSafety/SkillTester artifact disclosed in manuscript; immutable event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07943:end -->
<!-- review:SF-2026-ARXIV-2606-07943:end -->

<!-- review:SF-2026-ARXIV-2606-07950:start -->
<!-- claim:SF-2026-ARXIV-2606-07950:start -->
The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning 处理的问题是：Confidence, empirical difficulty, and shrinking group advantage become explicit rollout-allocation state used for both resampling and update weighting under fixed compute.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§4 CoDaPO; confidence/difficulty value, update weighting and within-mini-batch resampling`。状态 owner 为 `TRAIN-GRPO`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5 Experiments; §5.1 setup; Appendix C.6 implementation details` 提供可复核结果。

评估证明边界：workload=`MATH training and twelve reported math, general-reasoning and code benchmarks`；model=`Llama-3.2-1B-Instruct; Qwen2.5-Math-1.5B and 7B`；evaluator=`Accuracy across twelve benchmarks, confidence/difficulty dynamics and fixed-compute comparison`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Conclusion; Appendix dynamic-difficulty analysis and fixed-compute boundary`。

取舍、failure、共存与演进：Difficulty-aware resampling concentrates fixed rollout compute but can starve examples whose value estimate is initially wrong; uniform GRPO remains the neutral branch when confidence and empirical difficulty are unreliable. The result supports compute reallocation within the tested regimes, not a universal optimizer ordering. Artifact 边界：`https://github.com/tmlr-group/CoDaPO — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07950:end -->
<!-- review:SF-2026-ARXIV-2606-07950:end -->

<!-- review:SF-2026-ARXIV-2606-07957:start -->
<!-- claim:SF-2026-ARXIV-2606-07957:start -->
Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path 处理的问题是：CSPM rules become tenant-local derived state maintained bidirectionally from catalogue entries and the live asset graph, removing vendor release cadence from the protection critical path.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§4 Demand-Driven Architecture; formal derivation and bidirectional catalogue/asset triggers`。状态 owner 为 `PLATFORM-SECURITY`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§8 Evaluation Methodology; complexity analysis and worked example, not executed measurements` 提供可复核结果。

评估证明边界：workload=`No executed benchmark — formal semantics, complexity analysis, worked example and proposed evaluation methodology`；model=`Not Disclosed — no model evaluated`；evaluator=`Methodology proposes latency/resource evaluation; paper explicitly does not prove rule correctness or alert priority`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§10 Limitations; rule correctness and alert prioritization explicitly out of scope`。

取舍、failure、共存与演进：Tenant-local rule derivation shortens vendor cadence but makes catalogue freshness, asset-graph correctness and rule garbage collection tenant responsibilities. Centrally authored rules remain necessary for predicates not derivable from structured feeds; the paper explicitly leaves rule correctness and alert priority outside its proof. Artifact 边界：`Not Disclosed — architecture paper provides no executable artifact`。
<!-- claim:SF-2026-ARXIV-2606-07957:end -->
<!-- review:SF-2026-ARXIV-2606-07957:end -->

<!-- review:SF-2026-ARXIV-2606-07968:start -->
<!-- claim:SF-2026-ARXIV-2606-07968:start -->
RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks 处理的问题是：A generation-time monitor combines recurrence, volume growth, and task progress over consecutive chunks and owns early termination of reasoning-token consumption attacks.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§IV RecurGuard; recurrence, volume and progress signals with three-chunk termination`。状态 owner 为 `PLATFORM-MONITORING`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§VI Experimental Setup; §VII Results and adaptive stress tests` 提供可复核结果。

评估证明边界：workload=`OverThink, ExtendAttack, held-out QA/code/math/summarization and adaptive stress tests`；model=`DS-R1-Qwen-7B primary; DS-R1-Llama-8B, Qwen3-8B, Llama3.1-8B, Sonnet-4.5 and Opus-4.7 slices`；evaluator=`TPR/FPR, joint miss rate, token amplification and post-hoc QDM fallback`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§XI Limitations; exposed-trace dependency and topical adaptive miss boundary`。

取舍、failure、共存与演进：Early termination saves billed reasoning tokens only when traces are observable and the three signals remain anomalous; topical adaptive attacks expose a roughly 50% joint-miss boundary. QDM therefore remains a post-hoc fallback, and the monitor must not terminate benign long reasoning from a single transient alarm. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-07968:end -->
<!-- review:SF-2026-ARXIV-2606-07968:end -->

<!-- review:SF-2026-ARXIV-2606-07970:start -->
<!-- claim:SF-2026-ARXIV-2606-07970:start -->
Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks 处理的问题是：Train-time adversarial attack strength becomes an inner-loop robustness control, with parallel execution preserving the stronger full-parameter threat model.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Methods; bi-level Patcher inner attack and parallel implementation`。状态 owner 为 `TRAIN-SFT`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 setup and full-parameter attack transfer` 提供可复核结果。

评估证明边界：workload=`Beavertails/PKU-SafeRLHF/ToxicDPO-v2 test attacks; AdvBench, Beavertails and HEx-PHI ASR; Alpaca utility`；model=`Qwen2.5-1.5B main/ablation; Qwen3-4B and Llama3-8B generalization; Qwen3-Max harmfulness judge`；evaluator=`Attack Success Rate on three safety sets, utility, transfer and wall-clock; fully poisoned and larger-malicious-set failures retained`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations and Conclusion; stronger simulated attacks remain a bounded threat-model proxy`。

取舍、failure、共存与演进：A stronger inner attack improves robustness to full-parameter malicious fine-tuning at extra train-time compute; the parallel algorithm reduces wall time without removing that compute. Conventional SFT alignment remains cheaper for weaker threat models, and success against simulated attacks does not certify every future poisoning strategy. Artifact 边界：`https://github.com/haomingwen/patcher — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-07970:end -->
<!-- review:SF-2026-ARXIV-2606-07970:end -->

<!-- review:SF-2026-ARXIV-2606-07992:start -->
<!-- claim:SF-2026-ARXIV-2606-07992:start -->
VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation 处理的问题是：Tool errors are an authority-bearing ingress path; mutation across error structure and language changes MCP trust from tool output validation to error-loop admission and containment.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Methodology; seven-dimensional mutation space and controlled error-path injection`。状态 owner 为 `AGENT-MCP`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Evaluation; Appendix C.1 controlled tool-error protocol` 提供可复核结果。

评估证明边界：workload=`Controlled MCP tool-error JSON with seven mutation dimensions and email-exfiltration effect`；model=`Gemini-3.1-Pro, GPT-5.5, GLM-5.1, Qwen3-Coder`；evaluator=`Injection compliance/ASR by error structure plus production-guardrail comparison`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Discussion and Conclusion; production guardrails and controlled-environment boundary`。

取舍、failure、共存与演进：Systematic mutation widens coverage of MCP error paths but the experiment's controlled tool errors and exfiltration action do not reproduce every production framework. Framework guardrails can still contain the path; the durable change is to treat errors as authority-bearing inputs rather than to ban tool error text. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-07992:end -->
<!-- review:SF-2026-ARXIV-2606-07992:end -->

<!-- review:SF-2026-ARXIV-2606-08049:start -->
<!-- claim:SF-2026-ARXIV-2606-08049:start -->
SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows 处理的问题是：Versioned notebooks make each reusable step auditable state and let validation gates choose code execution or local natural-language fallback when environments drift.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 SKILL.nb; selective formalization, versioned notebook and gate-conditioned local fallback; Appendix A`。状态 owner 为 `AGENT-WORKFLOW`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; shared Evaluation Protocol and WebArena/Mind2Web/GitLab migration slices` 提供可复核结果。

评估证明边界：workload=`WebArena-Verified, Mind2Web cross-site/domain and GitLab 15.7→16.11/18.9 migration`；model=`Agent model/backend matrix is experiment-specific; no single evaluated model identity`；evaluator=`Success, retained success, bounded-repair recovery/regression and migration gap`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Limitations; Appendix A.8 lifecycle and environment-drift boundaries`。

取舍、failure、共存与演进：Versioned notebooks add maintenance and gate design, and a stale gate can reject reusable code or trigger excessive natural-language fallback. One-shot free-form workflows remain useful for non-repeated tasks; SKILL.nb evolves durable workflows by localizing failure and repair evidence at each step. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08049:end -->
<!-- review:SF-2026-ARXIV-2606-08049:end -->

<!-- review:SF-2026-ARXIV-2606-08094:start -->
<!-- claim:SF-2026-ARXIV-2606-08094:start -->
vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models 处理的问题是：A single C++ runtime owns cached vision-language prefix state, cross-attending action-expert solver steps, portable model bundles, and one request protocol across VLA families.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Runtime Design; §3.3 cached prefix/action expert and Algorithm 1 solver loop`。状态 owner 为 `INFER-REQUEST-LIFECYCLE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Evaluation; §4.1 setup and 200-episode LIBERO-Object protocol` 提供可复核结果。

评估证明边界：workload=`LIBERO-Object 10 tasks ×20 episodes per architecture and ALOHA moving-target stress test`；model=`Seven VLA architectures spanning five backbones/four action heads`；evaluator=`Episode success, behavioral match, latency, memory footprint and cross-hardware roofline`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Limitations; deployment portability does not prove every VLA architecture behaviorally identical`。

取舍、failure、共存与演进：One portable runtime reduces Python-stack drift but requires architecture adapters, self-contained bundle conversion and hardware-specific kernels. Generic PyTorch remains the development branch for unsupported models; batch-1 roofline results identify utilization as the tested lever without proving all robot control loops meet real-time deadlines. Artifact 边界：`https://fai-modelopt-tech.github.io/vla-cpp.github.io/ — project, code and scaffold disclosed; commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08094:end -->
<!-- review:SF-2026-ARXIV-2606-08094:end -->

<!-- review:SF-2026-ARXIV-2606-08106:start -->
<!-- claim:SF-2026-ARXIV-2606-08106:start -->
PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents 处理的问题是：Anytime-valid paired tests move self-evolution authority from noisy score improvement to a false-commit-controlled acceptor that remains valid under optional stopping.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§4 PACE; paired testing-by-betting e-process and Algorithm 1 commit gate`。状态 owner 为 `AGENT-PLATFORM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5 Experiments on prompt self-evolution with hidden real/no-gain conditions` 提供可复核结果。

评估证明边界：workload=`Prompt self-evolution on GSM8K, SVAMP and ARC-Challenge with hidden-real-gain and no-gain regimes`；model=`Qwen2.5 0.5B–3B agents`；evaluator=`False/harmful commits, held-out accuracy, variance and evaluation cost`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations; per-decision guarantee is not a global lifetime guarantee`。

取舍、failure、共存与演进：PACE spends paired evaluations to avoid noisy commits and may delay acceptance of small real gains. Greedy acceptance remains faster when errors are cheap, but self-modifying production agents need the per-candidate false-commit bound; optional-stopping validity must not be misstated as a lifetime family-wise guarantee. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08106:end -->
<!-- review:SF-2026-ARXIV-2606-08106:end -->

<!-- review:SF-2026-ARXIV-2606-08197:start -->
<!-- claim:SF-2026-ARXIV-2606-08197:start -->
AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments 处理的问题是：Version grouping, calibration-set semantic alignment, and freshness/participation weighting make staleness and fairness explicit asynchronous federated aggregation state.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§III AlignFed Framework; §IV version grouping, semantic calibration and fairness weighting`。状态 owner 为 `TRAIN-DISTRIBUTED-TRAINING`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§V Experimental Evaluation; §V-A setup` 提供可复核结果。

评估证明边界：workload=`Heterogeneous asynchronous federated fine-tuning under non-IID data and staleness`；model=`Llama3-8B and Qwen3-8B`；evaluator=`Convergence, accuracy, fairness, staleness robustness, latency and communication`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§VI Conclusion and stated simulation/heterogeneous-edge scope`。

取舍、failure、共存与演进：Version grouping and calibration reduce stale semantic drift but introduce calibration data, grouping delay and fairness weighting into the aggregator. Synchronous FFT remains simpler under homogeneous clients; AlignFed is the heterogeneous asynchronous branch and its single-A100 FP16 experiment does not establish large fleet SLOs. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08197:end -->
<!-- review:SF-2026-ARXIV-2606-08197:end -->

<!-- review:SF-2026-ARXIV-2606-08200:start -->
<!-- claim:SF-2026-ARXIV-2606-08200:start -->
Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents 处理的问题是：An in-world evaluator actively creates criterion-relevant situations through native dialogue/action, changing evaluation from passive trajectory scoring to coverage-seeking intervention.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Online Agent-as-a-Judge; in-world situation generation through native dialogue/action`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 life-simulation setup and human-label agreement` 提供可复核结果。

评估证明边界：workload=`Life simulation: five characters, 32 social criteria, three target backends × three seeds`；model=`Target-agent backends vary; all automated judges use GPT-5.4-mini`；evaluator=`Criteria coverage and agreement with human labels versus passive judges`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Discussion; evaluator intervention can change the trajectory it measures`。

取舍、failure、共存与演进：An active judge improves criterion coverage by changing the situation, so its actions become part of the evidence-generating treatment and may confound natural behavior. Passive trajectory scoring remains necessary for observational questions; the two modes must be reported separately and the judge must never repair the target trajectory. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08200:end -->
<!-- review:SF-2026-ARXIV-2606-08200:end -->

<!-- review:SF-2026-ARXIV-2606-08302:start -->
<!-- claim:SF-2026-ARXIV-2606-08302:start -->
HACK++: Towards More Effective Head-Aware Key-Value Compression for Efficient Visual Autoregressive Modeling 处理的问题是：Head role, layer, and generation step control separate attention and retained-cache budgets for visual autoregressive decoding instead of applying one global compression ratio.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§IV attention-head analysis; §V HACK++ calibration, decoupled attention/cache budgets and adaptive allocation`。状态 owner 为 `INFER-KV-CACHE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§VI Experiments across VAR generation and understanding tasks` 提供可复核结果。

评估证明边界：workload=`Multiple VAR models over text-to-image, class-conditional and unified understanding/generation tasks`；model=`Infinity-2B/8B and additional VAR models in §VI`；evaluator=`Generation quality, task accuracy, attention/cache budget and robustness to 1% cache`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§VII Conclusion; one-time calibration and VAR-specific head taxonomy bound transfer`。

取舍、failure、共存与演进：Head-type calibration and separate attention/cache budgets improve aggressive VAR compression but can age when model, layer behavior or generation regime changes. Global compression remains the simpler branch; HACK++ is VAR-specific evidence and does not displace general LLM KV retention owners. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08302:end -->
<!-- review:SF-2026-ARXIV-2606-08302:end -->

<!-- review:SF-2026-ARXIV-2606-08317:start -->
<!-- claim:SF-2026-ARXIV-2606-08317:start -->
Architectural Evolution and Selection Framework for Database Systems in AI-Ready Data Platforms 处理的问题是：Nine dimensions, workload characterization, constraint filtering, and compatibility scoring make polyglot database choice a reviewable platform decision rather than intuition.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§II Methodology: Literature Selection and Analysis Framework; §VI-A Evaluation Dimensions; §IX-B Database Architecture Selection Framework, Stages 1–3 and scoring formula`。状态 owner 为 `PLATFORM-FOUNDATIONS`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§VI-B Table I directional performance characteristics; §IX-D financial-fraud case study, Tables IV–V` 提供可复核结果。

评估证明边界：workload=`Conceptual comparison of 13 database paradigms plus one representative financial-fraud architecture case; Table I ranges are directional literature synthesis, not a controlled benchmark`；model=`Not Disclosed — no model is evaluated`；evaluator=`Qualitative compatibility values 1/2/3 weighted by workload importance; financial case maximum score 90; no product-level empirical evaluator`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§IX-B Framework Limitations; §XI Limitations`。

取舍、failure、共存与演进：Workload profiling and hard filtering make architecture choice auditable, but the compatibility values are qualitative paradigm-level judgments and the fraud example is illustrative rather than a controlled product benchmark. Existing platform admission and one-size-fits-all safeguards remain the owner contract; product-specific measurements, deployment constraints and empirical validation must precede any commit. Artifact 边界：`Not Disclosed — exact-v1 PDF names no executable framework artifact or immutable repository revision`。
<!-- claim:SF-2026-ARXIV-2606-08317:end -->
<!-- review:SF-2026-ARXIV-2606-08317:end -->

<!-- review:SF-2026-ARXIV-2606-08340:start -->
<!-- claim:SF-2026-ARXIV-2606-08340:start -->
Benchmarking Open-Ended Multi-Agent Coordination in Language Agents 处理的问题是：A long-horizon world separates individual task reward from coordination reward while controlling communication, role specialization, and coordination difficulty.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 alem benchmark design; procedural coordination tasks, communication and difficulty controls`。状态 owner 为 `AGENT-MULTI-AGENT`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 zero-shot 13-LLM team setup and MARL reference` 提供可复核结果。

评估证明边界：workload=`Procedural long-horizon alem world across coordination difficulty; homogeneous teams and MARL references`；model=`13 modern LLMs zero-shot; named frontier examples include Gemini-3.1-Pro-High and GPT-5.4-High`；evaluator=`Normalized return split into base-task and coordination reward; communication/memory/reasoning ablations`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§6 Limitations and Future Work; benchmark world and zero-shot policy scope`。

取舍、failure、共存与演进：Alem makes coordination measurable by imposing a particular procedural ecology, reward split and communication channel; strong return there need not transfer to open production teams. Short structured benchmarks remain useful for isolated skills, while alem adds long-horizon coordination stress rather than a universal agent ranking. Artifact 边界：`https://github.com/alem-world/alem-env — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08340:end -->
<!-- review:SF-2026-ARXIV-2606-08340:end -->

<!-- review:SF-2026-ARXIV-2606-08346:start -->
<!-- claim:SF-2026-ARXIV-2606-08346:start -->
CATPO: Critique-Augmented Tree Policy Optimization 处理的问题是：Tree outcome diversity and policy-reward decorrelation identify low-signal rollout trees; critique-guided grafting repairs all-fail branches before informativeness-weighted updates.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 CATPO; informativeness score, critique-guided healing and normalized tree weighting`。状态 owner 为 `TRAIN-GRPO`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 Qwen2.5-Math-1.5B on MATH and four test benchmarks` 提供可复核结果。

评估证明边界：workload=`Qwen2.5-Math-1.5B trained on MATH; AIME24, MATH-500, OlympiadBench and MinervaMath`；model=`Qwen2.5-Math-1.5B`；evaluator=`Pass@1/Avg@8 and macro accuracy; tree-informativeness/healing ablations`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Conclusion; single base-model/math-training regime and critique cost bound generality`。

取舍、failure、共存与演进：Critique-guided healing recovers all-fail trees but adds critique generation and can graft a persuasive wrong repair. Flat GRPO/TreeRPO remain simpler when trees already contain mixed outcomes; evidence is limited to one math model/training corpus and four math benchmarks. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08346:end -->
<!-- review:SF-2026-ARXIV-2606-08346:end -->

<!-- review:SF-2026-ARXIV-2606-08348:start -->
<!-- claim:SF-2026-ARXIV-2606-08348:start -->
Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses 处理的问题是：Verified trajectories and posterior beliefs turn skills into evidence-bearing lifecycle objects with auditable update and guardrail actions across harnesses.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Bayesian-Agent; verified trajectories, posterior skill beliefs, actions and guardrails`。状态 owner 为 `AGENT-PLATFORM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments across RealFin-Bench, SOP-Bench, Lifelong AgentBench and harness ablations` 提供可复核结果。

评估证明边界：workload=`SOP-Bench, Lifelong AgentBench and RealFin-Bench across native, GenericAgent, mini-swe-agent and Claude Code backends`；model=`deepseek-v4-flash and deepseek-v4-pro for Bayesian variants; Claude Sonnet-4.6, Claude Opus-4.6 and GPT-5.4 comparison rows`；evaluator=`Task accuracy, token accounting, efficiency, full/incremental repair and backend/model ablations`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Limitations; posterior repair depends on verifiable task artifacts`。

取舍、failure、共存与演进：Posterior skill actions are only as trustworthy as priors, verified trajectory artifacts and the harness's failure taxonomy; sparse evidence can make repair conservative. Raw empirical rates remain transparent with abundant homogeneous trials, while Bayesian-Agent owns finite-sample cross-harness uncertainty rather than model-weight learning. Artifact 边界：`https://github.com/DataArcTech/Bayesian-Agent — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08348:end -->
<!-- review:SF-2026-ARXIV-2606-08348:end -->

<!-- review:SF-2026-ARXIV-2606-08367:start -->
<!-- claim:SF-2026-ARXIV-2606-08367:start -->
Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy 处理的问题是：Continuously running heterogeneous agent populations, persistent memories, consequential governance, and live exogenous data expose drift and cross-influence absent from exam-style evaluation.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Platform Design; persistent memories, 120+ tools, live data and consequential governance`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§5.1 setup; §5.2 15-day cross-vendor results across five parallel worlds` 提供可复核结果。

评估证明边界：workload=`15 days, five parallel worlds, ten agents/world, 120+ tools and three memories`；model=`Claude Sonnet-4.6, Grok-4.1-Fast, Gemini-3-Flash, GPT-5-mini and mixed population`；evaluator=`Cross-world behavioral trajectories, governance stability/collapse and released logs`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§8 Limitations; one 15-day simulation cannot establish deployment-timescale causality`。

取舍、failure、共存与演进：Continuous worlds expose drift and cross-influence at the cost of API nondeterminism, high run expense and difficult causal attribution. Exam-style benchmarks remain the controlled complement; a 15-day, five-world observation demonstrates observability, not deployment-timescale safety or vendor superiority. Artifact 边界：`Prompts, logs and configurations released; immutable event-time revision not identified`。
<!-- claim:SF-2026-ARXIV-2606-08367:end -->
<!-- review:SF-2026-ARXIV-2606-08367:end -->

<!-- review:SF-2026-ARXIV-2606-08372:start -->
<!-- claim:SF-2026-ARXIV-2606-08372:start -->
SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC) 处理的问题是：A memorization test distinguishes population reconstruction from training-record leakage and maps reconstruction and membership inference to one comparable privacy-risk scale.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§2 taxonomy and attack families; §4 memorization test and RA-as-MIA reduction`。状态 owner 为 `PLATFORM-SECURITY`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§3 empirical study of 14 attacks, 9 generators and 5 datasets; §4 interpretation tests` 提供可复核结果。

评估证明边界：workload=`14 attacks ×9 synthetic-data generators ×5 datasets; QI sizes 3–16; DP epsilon sweeps`；model=`Classifiers, graphical models and diffusion/generative attack families; not one LLM`；evaluator=`Rarity-weighted reconstruction advantage, train/holdout memorization gap and RA-as-MIA comparison`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5.3 Limitations; black-box single-record released-table threat model`。

取舍、failure、共存与演进：The unified risk scale improves comparability but remains a black-box, single-record released-table threat model; model inversion, aggregate reconstruction and coordinated targets stay separate branches. The train/holdout gap prevents high reconstruction accuracy from being mislabeled as memorization, especially for rare records. Artifact 边界：`Attack infrastructure disclosed through NIST CRC context; immutable event-time revision not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08372:end -->
<!-- review:SF-2026-ARXIV-2606-08372:end -->

<!-- review:SF-2026-ARXIV-2606-08381:start -->
<!-- claim:SF-2026-ARXIV-2606-08381:start -->
Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard 处理的问题是：Reference-set-relative semantic divergence provides a black-box audit contract for provider-specific alignment when absolute ground truth is unavailable.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 comparative black-box framework; semantic-space divergence against a reference model set`。状态 owner 为 `PLATFORM-EVALUATION-SYSTEM`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Case Studies of previously reported provider-specific alignment behavior` 提供可复核结果。

评估证明边界：workload=`Three black-box cases: DeepSeek-R1 on China- and US-sensitive domains, and Meta AI Chat/Llama 4 on Meta-related topics`；model=`DeepSeek-R1 and Meta AI Chat/Llama 4 targets; diverse baseline ensemble; GPT-5.2 and Gemini-3.1-Flash-Lite judges; four embedding models`；evaluator=`Welch one-sided t-test, bootstrap median test, target-permutation diagnostic; relative divergence not absolute correctness or intent`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `Limitations section; relative divergence detects difference, not absolute truth or provider intent`。

取舍、failure、共存与演进：Relative semantic divergence depends on the reference-set composition and can detect systematic difference without identifying truth, provider intent or harm. Ground-truth task evaluation remains necessary where labels exist; this framework is the black-box comparative branch for otherwise unobservable policy variation. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。
<!-- claim:SF-2026-ARXIV-2606-08381:end -->
<!-- review:SF-2026-ARXIV-2606-08381:end -->

<!-- review:SF-2026-ARXIV-2606-08382:start -->
<!-- claim:SF-2026-ARXIV-2606-08382:start -->
STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control 处理的问题是：Differentiable head/block thresholds, sensitivity-specific factorization, and rank-aware mixed precision turn KV rank into adaptive runtime compression state backed by kernels.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 STAR-KV; differentiable thresholds, key/value-specific factorization and rank-aware quantization`。状态 owner 为 `INFER-KV-CACHE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; Appendix A.4 kernel and benchmark details` 提供可复核结果。

评估证明边界：workload=`WikiText-2 perplexity, six LM-Eval tasks, LongBench and 4K RULER plus kernel/throughput slices`；model=`LongChat-7B-v1.5, Llama-2-7B, Llama-3-8B-Instruct and Llama-3.1-8B-Instruct long-context slice`；evaluator=`Perplexity, zero-shot accuracy, LongBench/RULER, compression, attention speedup and end-to-end throughput`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§5 Conclusion and ablations; low-rank sensitivity is model/workload dependent`。

取舍、failure、共存与演进：Adaptive rank and mixed precision need learned thresholds, decomposition choices and custom Triton kernels; sensitivity can move across heads, blocks, models and workloads. Fixed-rank compression remains easier to deploy, and throughput gains cannot be transferred beyond the disclosed GPU/kernel slices. Artifact 边界：`https://github.com/PriyanshBhatnagar/STAR-KV — repository disclosed; event-time commit not pinned`。
<!-- claim:SF-2026-ARXIV-2606-08382:end -->
<!-- review:SF-2026-ARXIV-2606-08382:end -->

<!-- review:SF-2026-ARXIV-2606-08403:start -->
### 2606.08403 — Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：结构化浮点载体把恶意信号藏在原始文本视图之外，并在可信重建后才进入模型上下文，迫使安全 owner 同时校验 data layer 与 reconstruction layer。 exact-v1 摘要将具体问题界定为：Text-centered prompt-injection defenses assume that the malicious signal is visible in one of the inspected text views. We study a reproducible LLM01-style indirect prompt/content-injection failure mode where that assumption breaks: a payload caught in plain English slips past the same detector when it is transported as structured float parameters and reconstructed only as fragmented telemetry. Across 14,400 attacked real-model trials on three commercial LLM APIs from different providers, the IFS-derived float-arra

**State / data / control owner。** `PLATFORM-SECURITY` 负责输入信任、权限与阻断/升级控制；在本 source 中，需被显式持有、传递或阻断的状态正是“结构化浮点载体把恶意信号藏在原始文本视图之外，并在可信重建后才进入模型上下文，迫使安全 owner 同时校验 data layer 与 reconstruction layer。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08403v1 §5 Experimental Setup; §6 Results` 实际支持的合同是 `Disclosed — §5 uses summarization and structured extraction across four carriers, three injection objectives, four defenses and three commercial APIs; 14,400 attacked real-model trials plus 4,800 clean trials`，evaluator 是 `Disclosed — leakage ASR, Strong ASR, task success rate and detection rate, with carrier×defense and 2×2 ablations`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08403v1 §3 Threat Model; §4 Carriers`；counterevidence locator: `arXiv:2606.08403v1 §7 Discussion; §8 Limitations`。

**Trade-off / failure / coexistence / evolution。** 双层载体校验增加解析与误报成本；若重建器不可控或 semantic gate 已覆盖载体，普通 text inspection 仍应保留，而演进点是把 reconstructed data 纳入同一 trust boundary。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08403:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08403v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08403:end -->
<!-- review:SF-2026-ARXIV-2606-08403:end -->

<!-- review:SF-2026-ARXIV-2606-08411:start -->
### 2606.08411 — AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：AsyncLane 用 lane tree 把 DLM 的 prefix refinement 与 frontier advancement 解耦，并以 shared-prefix batching、lookahead reuse 与 cache refresh 管理异步依赖。 exact-v1 摘要将具体问题界定为：Block-wise semi-autoregressive decoding is the standard inference paradigm for diffusion large language models (DLMs), but it imposes a strict dependency between blocks: the next block cannot begin until the current block is fully decoded or its denoising budget is exhausted. We observe that once a block exposes a reliable delimiter boundary or stable semantic prefix, continuation generation need not wait for every residual token to be resolved. We propose AsyncLane, a training-free decoding scheduler that decouple

**State / data / control owner。** `INFER-DECODE` 负责lane/frontier、cache refresh 与终止状态；在本 source 中，需被显式持有、传递或阻断的状态正是“AsyncLane 用 lane tree 把 DLM 的 prefix refinement 与 frontier advancement 解耦，并以 shared-prefix batching、lookahead reuse 与 cache refresh 管理异步依赖。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08411v1 §4 Experiments; §4.1 Experimental Setup` 实际支持的合同是 `Disclosed — §4.1 evaluates GSM8K, GSM8K-CoT, MATH, HumanEval and MBPP over 256/512/1024 generation budgets`，evaluator 是 `Disclosed — tokens/s, exact-match accuracy, pass@1, model-call NFE and wall-clock latency`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08411v1 §3 Methods; §§3.1–3.4 lane scheduling and execution`；counterevidence locator: `arXiv:2606.08411v1 §4.3 Ablation Study; §5 Conclusion`。

**Trade-off / failure / coexistence / evolution。** 异步 lane 提高吞吐但引入 prefix consistency、cache refresh 与 termination 竞态；短输出或 batch=1 的传统同步 decode 仍可能更简单，后续压力在多请求 fairness。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08411:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08411v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08411:end -->
<!-- review:SF-2026-ARXIV-2606-08411:end -->

<!-- review:SF-2026-ARXIV-2606-08417:start -->
### 2606.08417 — Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：零参数劣质 sampler 可在非退化 entropy 下优化 gen-PPL，说明单一 scorer predictability 不能充当生成质量，评测必须转向分布差异。 exact-v1 摘要将具体问题界定为：Diffusion and continuous flow-based language models have emerged as the leading non-autoregressive alternatives to language modeling. Progress in both paradigms is overwhelmingly tracked by generative perplexity (gen-PPL): the per-token negative log-likelihood of samples under a frozen autoregressive (AR) scorer such as gpt2-large, typically paired with an empirical-entropy guardrail to rule out low-entropy collapse. We argue that this metric is unsound. By construction, gen-PPL measures only predictability under t

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“零参数劣质 sampler 可在非退化 entropy 下优化 gen-PPL，说明单一 scorer predictability 不能充当生成质量，评测必须转向分布差异。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08417v1 §4 Experiments` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: We recommend evaluation suites that directly quantify the distributional divergence between generated and reference text, and use such a suite to re-benchmark recent non-autoregressive models, recovering a more faithful picture of the current state of the art.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08417v1 §3 Methodology; §§3.1–3.2 naive samplers and distributional metrics`；counterevidence locator: `arXiv:2606.08417v1 §5 Conclusion; Appendix A parameter sweeps`。

**Trade-off / failure / coexistence / evolution。** 分布指标降低单一 scorer 被投机的风险，却增加参考分布与多指标解释成本；受控 conditional generation 仍可保留 PPL，演进是把 unconditional quality 与 predictability 解耦。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08417:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08417v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08417:end -->
<!-- review:SF-2026-ARXIV-2606-08417:end -->

<!-- review:SF-2026-ARXIV-2606-08432:start -->
### 2606.08432 — Trajectory-Refined Distillation

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：TRD 把 on-policy distillation 的修复尺度从 token-loss clipping 提升到 teacher-guided trajectory correction，以避免失败 prefix 产生双峰且碎片化的监督。 exact-v1 摘要将具体问题界定为：On-policy distillation (OPD) has become a central post-training tool for large language models (LLMs), providing dense per-token teacher supervision along the student's own rollouts. In this work, we identify a common structural cause underlying OPD, which we call prefix failure. Under prefix failure, dense per-token supervision induces a bimodal teacher mixture and fragmented gradients that token-level loss truncation or reweighting fail to address. This observation motivates us to move beyond token-level loss int

**State / data / control owner。** `TRAIN-SFT` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“TRD 把 on-policy distillation 的修复尺度从 token-loss clipping 提升到 teacher-guided trajectory correction，以避免失败 prefix 产生双峰且碎片化的监督。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08432v1 §6 Experiments; Appendix C Evaluation Protocol` 实际支持的合同是 `Disclosed — five competition-math benchmarks plus HumanEval+, MBPP+ and LiveCodeBench for OPD code evaluation`，evaluator 是 `Disclosed — Avg@16, Pass@16, task accuracy, KL/trajectory diagnostics and refinement-signal ablations`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08432v1 §4 Prefix Failure; §5 Trajectory-Refined Distillation`；counterevidence locator: `arXiv:2606.08432v1 §6.4–6.5 signal/trajectory analysis; Appendix B ablations`。

**Trade-off / failure / coexistence / evolution。** trajectory correction 以额外 teacher rollout 和长序列内存换取连续监督；teacher error 或 prefix drift 会把整轨迹带偏，因此 token clipping 仍是低成本保护层。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08432:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08432v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08432:end -->
<!-- review:SF-2026-ARXIV-2606-08432:end -->

<!-- review:SF-2026-ARXIV-2606-08433:start -->
### 2606.08433 — AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing)

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：AI code sandbox 不能用单一总分排序；host attack surface、leakage、stackability、CVE、patch cadence 与 fuzzing posture 必须按 threat model 分轴负责。 exact-v1 摘要将具体问题界定为：This paper reads six engine-level measurements together -- 1.1 host attack surface, 1.2 information leakage, 1.3 defense-in-depth stackability, 1.4 public CVE history, 1.5 patch cadence, and 1.6 upstream fuzzing posture -- to describe how five AI-sandbox products isolate guest code from the host kernel. No single axis is a sufficient basis for a comparative judgement; the cross-axis reading is the load-bearing analysis. Three high-level findings: (1) engine classes (microVM, userspace kernel, OCI container) separat

**State / data / control owner。** `PLATFORM-SECURITY` 负责输入信任、权限与阻断/升级控制；在本 source 中，需被显式持有、传递或阻断的状态正是“AI code sandbox 不能用单一总分排序；host attack surface、leakage、stackability、CVE、patch cadence 与 fuzzing posture 必须按 threat model 分轴负责。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08433v1 §3 Cross-axis reads; §4 Threat-model qualification matrix; §5 product portraits` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: zzing investment splits into three tiers, and the strongest combination -- microVM x continuous public fuzzer -- is unoccupied in this set, leaving the "0 published CVEs x no upstream fuzzer x no academic study" intersection structurally unmeasured. We report per-axis orderings, per-product portraits, and a threat-model qualification matrix; no overall ranking is proposed. Companion repository (code, Apache-2.0): htt`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08433v1 Methodology in brief; §§2.1–2.6 six engine-level axes`；counterevidence locator: `arXiv:2606.08433v1 §6 Open questions; §7 Caveats and limitations`。

**Trade-off / failure / coexistence / evolution。** 多轴 sandbox 审计牺牲一个总分的易读性；CVE 缺失、patch lag 或 stackability 变化会迅速使结论过期，产品级隔离与 engine 级属性必须并存。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08433:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08433v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08433:end -->
<!-- review:SF-2026-ARXIV-2606-08433:end -->

<!-- review:SF-2026-ARXIV-2606-08446:start -->
### 2606.08446 — Sparrow: Sparse Rollout for Stable and Efficient Long-context RL of Large Language Models

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：Sparrow 把 long-context RL rollout 的稀疏注意力当作训练系统路径，并显式保留 dense teacher refresh 以约束效率与策略漂移。 exact-v1 摘要将具体问题界定为：Despite being powerful, reinforcement learning with verifiable rewards (RLVR) induces extremely long COT, making it computationally expensive. Since RLVR per-step cost is dominated by long-context rollout generation, sparse attention offers a promising way to accelerate dense rollout. However, sparse rollouts require a delicate stability-efficiency tradeoff: overly aggressive sparsity causes collapse, while overly lenient sparsity gives insufficient speedup. In this work, we study this tradeoff through sparse-to-de

**State / data / control owner。** `TRAIN-GRPO` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“Sparrow 把 long-context RL rollout 的稀疏注意力当作训练系统路径，并显式保留 dense teacher refresh 以约束效率与策略漂移。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08446v1 §4 Empirical Studies; §§4.1–4.5` 实际支持的合同是 `Disclosed — long-context RL rollout plus sparse-attention cost studies, including 16K/24K/32K prefill probes and 1,000 repeated decode timings`，evaluator 是 `Disclosed — sparse/dense mismatch, rollout stability, latency, page-size sensitivity and LoRA-distillation overhead`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08446v1 §3 Observation and Insights; §§3.1–3.3 stability/cost controls`；counterevidence locator: `arXiv:2606.08446v1 Appendices A, D, E and §5 Conclusion`。

**Trade-off / failure / coexistence / evolution。** 稀疏 rollout 降低长上下文注意力成本，却把稳定性押在 dense refresh 与 KV budget 上；预算过低会 collapse，短上下文 dense attention 仍是合理基线。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08446:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08446v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08446:end -->
<!-- review:SF-2026-ARXIV-2606-08446:end -->

<!-- review:SF-2026-ARXIV-2606-08476:start -->
### 2606.08476 — FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：FlashCP 将 context-parallel 的负载均衡、attention kernel 与 KV 通信共同建模，避免静态 sequence sharding 把三类瓶颈分开优化。 exact-v1 摘要将具体问题界定为：Context parallelism (CP) is essential for training large-scale, long-context language models, as it partitions sequences to reduce memory overhead. However, existing CP methods suffer from workload imbalance, inefficient kernels, and redundant communication due to static sequence sharding and key-value (KV) tensor communication. We present FlashCP, a load-balanced and communication-efficient framework for CP training. FlashCP introduces a sharding-aware communication mechanism to eliminate redundant KV communicatio

**State / data / control owner。** `TRAIN-DISTRIBUTED-TRAINING` 负责sequence shard、通信与同步状态；在本 source 中，需被显式持有、传递或阻断的状态正是“FlashCP 将 context-parallel 的负载均衡、attention kernel 与 KV 通信共同建模，避免静态 sequence sharding 把三类瓶颈分开优化。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08476v1 §4 Experiments; §4.1 Experiment Setup; §§4.2–4.3` 实际支持的合同是 `Disclosed — WLB-LLM, Pile and RedPajama; 100K sampled packed sequences; 128K contexts; CP sizes 4 and 8`，evaluator 是 `Disclosed — normalized training/inference latency, speedup, load imbalance, communication and kernel-efficiency breakdown`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08476v1 §3 FlashCP Design; §§3.1–3.4`；counterevidence locator: `arXiv:2606.08476v1 §2.3 Limitation of Existing Works; §6 Conclusion`。

**Trade-off / failure / coexistence / evolution。** 联合优化负载、kernel 与通信减少局部最优，却依赖序列长度分布和 NVLink 拓扑；均匀短序列仍可用静态 CP，未来压力来自跨节点异构网络。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08476:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08476v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08476:end -->
<!-- review:SF-2026-ARXIV-2606-08476:end -->

<!-- review:SF-2026-ARXIV-2606-08483:start -->
### 2606.08483 — Testing the Black Box: Structural Barriers to Independent Evaluation of Consumer-Facing Health LLMs

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：consumer health LLM 的 personalization 与版本漂移无法由黑盒单次测量独立归因，评测合同必须记录可观察输入、不可见系统状态与重复测量边界。 exact-v1 摘要将具体问题界定为：Background: Consumer-facing large language models are now a common source of health information, and they interpret and personalize responses rather than retrieve them. Whether their responses vary across users is a clinical, equity, and governance question, sharpened by evidence that sycophantic responses can alter judgment and increase trust. Objective: To evaluate response variation and sycophancy in consumer-facing health LLMs under conditions resembling ordinary patient use. Methods: We constructed simulated u

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“consumer health LLM 的 personalization 与版本漂移无法由黑盒单次测量独立归因，评测合同必须记录可观察输入、不可见系统状态与重复测量边界。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08483v1 §4 Evaluation Criteria; §5 Temporal Stability` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Objective: To evaluate response variation and sycophancy in consumer-facing health LLMs under conditions resembling ordinary patient use.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08483v1 §1 Question Design; §2 User Profile Simulation; §3 Technical Implementation`；counterevidence locator: `arXiv:2606.08483v1 §6 Discussion and structural black-box limits`。

**Trade-off / failure / coexistence / evolution。** 重复黑盒测量能暴露版本漂移但无法分解不可见模型、检索与个性化状态；厂商内部 telemetry 与独立外部 probe 必须并存，不能把时间差误判为因果。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08483:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08483v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08483:end -->
<!-- review:SF-2026-ARXIV-2606-08483:end -->

<!-- review:SF-2026-ARXIV-2606-08486:start -->
### 2606.08486 — TRADE: Transducer-Augmented Decoder for Speech LLM

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：TRADE 以共享 audio encoder 的 transducer branch 补齐 Speech LLM 的 frame alignment、streaming decode 与 end-of-utterance 状态。 exact-v1 摘要将具体问题界定为：Speech Large Language Models (Speech LLMs) lack a principled mechanism for streaming inference: their label-synchronous generation has no acoustic-frame alignment, making real-time decoding and end-of-utterance detection difficult. We propose TRADE TRansducer-Augmented DEcoder, which augments a multimodal LLM with a transducer branch that shares the audio encoder and uses the LLM's hidden states directly as the prediction network -- coupling frame-synchronous acoustic alignment with the LLM's linguistic reasoning.

**State / data / control owner。** `INFER-DECODE` 负责lane/frontier、cache refresh 与终止状态；在本 source 中，需被显式持有、传递或阻断的状态正是“TRADE 以共享 audio encoder 的 transducer branch 补齐 Speech LLM 的 frame alignment、streaming decode 与 end-of-utterance 状态。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08486v1 §6 Experiments; §6.1 Setup; §§6.2–6.5` 实际支持的合同是 `Disclosed — streaming speech recognition over six chunk-size operating points and offline/streaming comparisons`，evaluator 是 `Disclosed — speech quality/alignment, latency/RTF, streaming stability and operating-point comparisons`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08486v1 §3 TRADE Model; §4 Training and Inference`；counterevidence locator: `arXiv:2606.08486v1 §8 Limitations; Appendix A model configuration`。

**Trade-off / failure / coexistence / evolution。** transducer 分支换来流式对齐但增加联合训练、chunk policy 与终止状态；离线高质量路径仍需共存，噪声或超长静默会放大 premature end-of-utterance 风险。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08486:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08486v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08486:end -->
<!-- review:SF-2026-ARXIV-2606-08486:end -->

<!-- review:SF-2026-ARXIV-2606-08517:start -->
### 2606.08517 — A Joint Finite-Sample Certificate for Adaptive Selective Conformal Risk Control

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：adaptive selective predictor 的部署证明必须联合约束 selected risk、acceptance floor 与 utility，而不能分别挑选阈值后拼接置信区间。 exact-v1 摘要将具体问题界定为：Selective predictors answer on confident inputs and abstain elsewhere; deploying one safely needs a single finite-sample certificate that simultaneously upper-bounds the selected risk, lower-bounds the acceptance probability $\pacc$ above a floor $\pmin$, and lower-bounds the deployment utility. This certificate must be valid under adaptive threshold selection from a finite grid of $m$ pairs on $\ncert$ samples. We give such a certificate for bounded, possibly non-monotone losses by treating the selected risk direc

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“adaptive selective predictor 的部署证明必须联合约束 selected risk、acceptance floor 与 utility，而不能分别挑选阈值后拼接置信区间。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08517v1 §5 Experimental Evaluation; §5.1–5.3` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Selective predictors answer on confident inputs and abstain elsewhere; deploying one safely needs a single finite-sample certificate that simultaneously upper-bounds the selected risk, lower-bounds the acceptance probability $\pacc$ above a floor $\pmin$, and lower-bounds the deployment utility.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08517v1 §3 Problem, Setup, and Algorithm; §4 Joint Certificate`；counterevidence locator: `arXiv:2606.08517v1 §4.9 regime-separation scope; later experimental scope analysis`。

**Trade-off / failure / coexistence / evolution。** 联合证书减少阈值挑选偏差，却依赖 exchangeability 与有限样本界；分布漂移时保证失效，传统独立监控仍需作为 deployment backstop。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08517:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08517v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08517:end -->
<!-- review:SF-2026-ARXIV-2606-08517:end -->

<!-- review:SF-2026-ARXIV-2606-08529:start -->
### 2606.08529 — Scaffold Effects on GAIA: A Controlled Comparison

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：GAIA 控制实验显示 scaffold 本身可显著移动同一模型的得分，因此 capability owner 必须分离 model、scaffold 与 attempt budget。 exact-v1 摘要将具体问题界定为：Published agent capability scores conflate what a model can do with what its scaffold lets it do, and the magnitude of this elicitation gap is not well characterized under controlled conditions. This study executes a pre-registered controlled comparison of three scaffolds (ReAct, a Planner-Actor-Rater multi-agent design, and planner-then-executor) across five models from three providers (Claude Opus 4.7, Sonnet 4.6, Haiku 4.5; Gemini 3.1 Pro Preview; GPT-5.5) on GAIA validation Levels 1 and 2, holding tasks and con

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“GAIA 控制实验显示 scaffold 本身可显著移动同一模型的得分，因此 capability owner 必须分离 model、scaffold 与 attempt budget。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08529v1 §4 Results; §§4.1–4.5` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: ng variable, and the predicted planner-executor advantage on file-reading tasks is falsified. Structured scaffolds make fewer tool calls yet recover more often from mid-trajectory errors at the harder level, and a single cell (Gemini with planner-then-executor) is the cheapest at both levels and the most accurate at Level 2. These results indicate that single-scaffold capability numbers are scaffold-conditional estim`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08529v1 §3 Methodology; §§3.1–3.6`；counterevidence locator: `arXiv:2606.08529v1 §6 Limitations; Appendix D incomplete cells/failure analysis`。

**Trade-off / failure / coexistence / evolution。** 控制 scaffold 提高归因可信度但增加运行成本和组合数；tool outage 或 attempt budget 差异仍会污染比较，模型分数与 scaffold 分数应长期分栏。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08529:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08529v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08529:end -->
<!-- review:SF-2026-ARXIV-2606-08529:end -->

<!-- review:SF-2026-ARXIV-2606-08531:start -->
### 2606.08531 — VESTA: A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：ForesightSafety-SAGE 把 agent 风险从静态 prompt/终局判断扩展为 scenario generation、authority context 与执行轨迹上的多维检查。 exact-v1 摘要将具体问题界定为：Large language models (LLMs) are increasingly evolving from simple text-based interaction systems into LLM agents that can maintain memory, use tools, access external environments, and execute tasks. As their capabilities and autonomy expand, the safety risks they face also become more diverse. Existing evaluations often rely on manually written scenarios, static prompts, or final-output judgments, making it difficult to capture the diverse risks that agents may face during task execution. We introduce ForesightSaf

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“ForesightSafety-SAGE 把 agent 风险从静态 prompt/终局判断扩展为 scenario generation、authority context 与执行轨迹上的多维检查。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08531v1 §4 Experimental Results and Analysis; §4.1 setup` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Existing evaluations often rely on manually written scenarios, static prompts, or final-output judgments, making it difficult to capture the diverse risks that agents may face during task execution.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08531v1 §3 VESTA Framework; §§3.1–3.3`；counterevidence locator: `arXiv:2606.08531v1 §5 Conclusion; Appendices D–H judge/protocol/trace evidence`。

**Trade-off / failure / coexistence / evolution。** 自动 scenario generation 扩大风险覆盖却把可信度部分交给生成器和 judge；authority context 或 rubric 错配会制造伪风险，人工 threat modeling 必须保留。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08531:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08531v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08531:end -->
<!-- review:SF-2026-ARXIV-2606-08531:end -->

<!-- review:SF-2026-ARXIV-2606-08539:start -->
### 2606.08539 — AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：AgentTrust 按 lexical 与 semantic threat 分流 action decision，并让 allow/warn/block/escalate 的反馈进入可更新 judge，而不是扩张固定规则包。 exact-v1 摘要将具体问题界定为：AI agents increasingly take consequential actions -- shell commands, cloud operations, and arbitrary tool-calls -- so a trust layer must decide, per action, whether to allow, warn, block, or escalate. We argue that the right way to reason about such a layer is by threat type. Lexical (fixed-signature) threats, where danger lives in a stable token, are decidable by deterministic rules; semantic (intent-dependent) threats, where a benign and a malicious action share the same surface, are out of reach for rules by con

**State / data / control owner。** `PLATFORM-SECURITY` 负责输入信任、权限与阻断/升级控制；在本 source 中，需被显式持有、传递或阻断的状态正是“AgentTrust 按 lexical 与 semantic threat 分流 action decision，并让 allow/warn/block/escalate 的反馈进入可更新 judge，而不是扩张固定规则包。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08539v1 §5 evaluation and online replay; Tables 2–5` 实际支持的合同是 `Disclosed — independent 630-action corpus, external semantic slice, and 30×1,500-action Monte Carlo online replay (45,000 actions)`，evaluator 是 `Disclosed — accuracy, FPR/FNR, judge-call rate, semantic accuracy, memory correctness and dangerous leaks`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08539v1 §3 threat-type decomposition and trust-layer design; §4 self-improving dual store`；counterevidence locator: `arXiv:2606.08539v1 §6 Limitations; concurrency and fixed-verdict replay boundary`。

**Trade-off / failure / coexistence / evolution。** 可学习 trust layer 提高语义覆盖但可能被 poisoned feedback 和 stale memory 反向放大；确定性高危规则应继续共存，演进压力是 live concurrency 与可撤销更新。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08539:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08539v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08539:end -->
<!-- review:SF-2026-ARXIV-2606-08539:end -->

<!-- review:SF-2026-ARXIV-2606-08574:start -->
### 2606.08574 — OrderDP: A Theoretically Guaranteed Lossless Dynamic Data Pruning Framework

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：OrderDP 区分 full-data gradient 与 pruning surrogate 的 unbiasedness，并把样本顺序纳入动态数据删减合同。 exact-v1 摘要将具体问题界定为：Data pruning (DP), as an oft-stated strategy to alleviate heavy training burdens, reduces the volume of training samples according to a well-defined pruning method while striving for near-lossless performance. However, existing approaches, which commonly select highly informative samples, can lead to biased gradient estimation compared to full-dataset training. Furthermore, the analysis of this bias and its impact on final performance remains ambiguous. To address these challenges, we propose OrderDP, a plug-and-pl

**State / data / control owner。** `TRAIN-DATA` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“OrderDP 区分 full-data gradient 与 pruning surrogate 的 unbiasedness，并把样本顺序纳入动态数据删减合同。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08574v1 §4 Experimental Settings; §5 Empirical Studies` 实际支持的合同是 `Disclosed — CIFAR-10/100 and ImageNet-1K pruning with ResNet-18/50, repeated stability and gradient checks`，evaluator 是 `Disclosed — accuracy, training time/GPU-hours, pruning ratio, Jaccard stability and gradient direction`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08574v1 §2 Method; §3 Theoretical Analysis`；counterevidence locator: `arXiv:2606.08574v1 Appendix F Limitations and Future Work`。

**Trade-off / failure / coexistence / evolution。** 动态删减节约计算却依赖 surrogate 与顺序分布；探索不足会永久遗漏难例，因此 full-data checkpoint 与可逆 retention policy 仍是安全阀。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08574:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08574v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08574:end -->
<!-- review:SF-2026-ARXIV-2606-08574:end -->

<!-- review:SF-2026-ARXIV-2606-08590:start -->
### 2606.08590 — Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：Kubernetes RCA 将 typed evidence graph、read-only tool collection、bounded traversal 与独立 verdict validation 分开，避免 prompt leakage 冒充诊断增益。 exact-v1 摘要将具体问题界定为：Kubernetes incidents are diagnosed reliably only when a root-cause system's reported gains come from incident evidence rather than scenario-specific shortcuts. We present Graph Traversal Agent, a graph-guided RCA agent that combines LLM reasoning with specialized tools. The model reasons over a typed evidence graph, while deterministic graph and tool operations collect evidence, bound the search, and check proposed verdicts. We map operational constraints, including read-only evidence collection, propagation-aware

**State / data / control owner。** `PLATFORM-MONITORING` 负责evidence graph、telemetry state 与诊断 verdict；在本 source 中，需被显式持有、传递或阻断的状态正是“Kubernetes RCA 将 typed evidence graph、read-only tool collection、bounded traversal 与独立 verdict validation 分开，避免 prompt leakage 冒充诊断增益。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08590v1 §VI Snapshot Evaluation; §VII Live-Validation Status` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: The surviving gain concentrates on ChaosMesh scenarios whose ground-truth root cause is the injected fault object already present in the evidence graph, so we report it as benchmark-coupled rather than broad cross-cluster RCA evidence.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08590v1 §IV System Overview; §V Audit Checks`；counterevidence locator: `arXiv:2606.08590v1 §VIII Failure Analysis; §IX Limitations and Future Work`。

**Trade-off / failure / coexistence / evolution。** typed graph 增强审计但会受 telemetry 缺口、拓扑陈旧和 traversal budget 限制；传统 runbook 与人工 verdict 仍需共存，下一压力是 live incident validation。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08590:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08590v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08590:end -->
<!-- review:SF-2026-ARXIV-2606-08590:end -->

<!-- review:SF-2026-ARXIV-2606-08610:start -->
### 2606.08610 — HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：HARBOR 把 robot RL 自动化定义为 bounded stages、standard commands、persistent artifacts 与 executable gates 的 harness，而非一个长提示词。 exact-v1 摘要将具体问题界定为：Reinforcement learning (RL) has become a powerful paradigm for robot learning, particularly in sim-to-real settings, but its broader adoption remains limited by the engineering pipeline surrounding the algorithms. Building tasks, shaping rewards, and tuning hyperparameters require substantial expert effort, making RL workflows costly and difficult to scale. We introduce HARBOR, an agentic framework that frames robot RL automation as a harness-engineering problem: given a simulator codebase and a task specification,

**State / data / control owner。** `AGENT-WORKFLOW` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“HARBOR 把 robot RL 自动化定义为 bounded stages、standard commands、persistent artifacts 与 executable gates 的 harness，而非一个长提示词。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08610v1 §4 Experiments; §§4.1–4.3; Appendix D details` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: HARBOR decomposes such high-level objectives into bounded stages executed by specialized agents through standardized commands, persistent artifacts, executable gates, and reusable knowledge, and scales iteration via decentralized parallel trials and experience learning across runs.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08610v1 §2 Robot RL Automation as a Harness Engineering Problem; §3 HARBOR`；counterevidence locator: `arXiv:2606.08610v1 §5 Conclusion, Limitations, and Future Work`。

**Trade-off / failure / coexistence / evolution。** harness 提高可恢复性却增加 stage schema、artifact 与 gate 维护；错误 gate 会稳定地产生错误进度，交互式专家调试仍是异常路径。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08610:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08610v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08610:end -->
<!-- review:SF-2026-ARXIV-2606-08610:end -->

<!-- review:SF-2026-ARXIV-2606-08615:start -->
### 2606.08615 — Harnessing Streaming Video in the Wild

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：unbounded streaming video 同时要求 proactive interaction、long-horizon memory 与 real-time processing，形成跨 chunk state retention 与 bounded-latency 的联合合同。 exact-v1 摘要将具体问题界定为：Vision-Language Models (VLMs) are increasingly required to process unbounded video streams in applications such as video-call assistants, live commentary, and embodied robots. An ideal streaming system should support proactive interaction, long-horizon memory, and real-time processing, while resting on a VLM backbone capable of handling diverse in-the-wild streaming tasks. However, existing VLMs excel at offline video understanding but fall short in streaming capabilities and lack dedicated infrastructure for strea

**State / data / control owner。** `AGENT-MEMORY` 负责持久轨迹、memory-skill relation 与更新状态；在本 source 中，需被显式持有、传递或阻断的状态正是“unbounded streaming video 同时要求 proactive interaction、long-horizon memory 与 real-time processing，形成跨 chunk state retention 与 bounded-latency 的联合合同。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08615v1 §6 Streaming-Eval; §7 Experiment; §7.1 setup` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: However, existing VLMs excel at offline video understanding but fall short in streaming capabilities and lack dedicated infrastructure for streaming deployment.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08615v1 §3 streaming problem formulation; §§4–5 streaming-native VLM and harness`；counterevidence locator: `arXiv:2606.08615v1 §7.4 Ablation Study; §9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 跨 chunk memory 支持无界视频但会累积错误状态并占用时延预算；事件稀疏场景可退回窗口化处理，演进压力是 bounded forgetting 与 proactive trigger 校准。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08615:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08615v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08615:end -->
<!-- review:SF-2026-ARXIV-2606-08615:end -->

<!-- review:SF-2026-ARXIV-2606-08625:start -->
### 2606.08625 — From Holistic Evaluation to Structured Criteria: Rubrics Across the Evolving LLM Landscape

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：rubric 随 chat、reasoning 与 agent 范式演化，评价单位从 holistic output 转为可追踪的 structured criteria 与行为约束。 exact-v1 摘要将具体问题界定为：As Large Language Models (LLMs) advance toward open-ended autonomous agents, the mechanisms used to evaluate and guide their behavior must evolve accordingly. This work introduces the rubric as a unifying framework capturing this evolution, characterizing rubrics as a dynamic response to successive LLM paradigm shifts that recurs across otherwise independent efforts in evaluation, reinforcement learning, and safety alignment. We define rubrics as explicit criteria sets that transform complex quality judgments into

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“rubric 随 chat、reasoning 与 agent 范式演化，评价单位从 holistic output 转为可追踪的 structured criteria 与行为约束。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08625v1 §4 evaluation use; §5 training use` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: As Large Language Models (LLMs) advance toward open-ended autonomous agents, the mechanisms used to evaluate and guide their behavior must evolve accordingly.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08625v1 §2 rubric definition/taxonomy; §3 construction and optimization`；counterevidence locator: `arXiv:2606.08625v1 §6 reliability limits; §8 future directions and claim-bounded survey scope`。

**Trade-off / failure / coexistence / evolution。** structured rubric 提供可追踪反馈但可能固化遗漏标准或被 gaming；holistic human review 仍负责新型 failure，rubric 必须版本化并随任务范式演化。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08625:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08625v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08625:end -->
<!-- review:SF-2026-ARXIV-2606-08625:end -->

<!-- review:SF-2026-ARXIV-2606-08635:start -->
### 2606.08635 — SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：SpectrumKV 将 PD 之间的 KV 传输从 token keep/drop 二元决策改为 per-token mixed precision，使网络字节、量化误差与重算成为同一控制面。 exact-v1 摘要将具体问题界定为：Prefill-decode (PD) disaggregation decouples prompt processing from token generation, but it also turns the key-value (KV) cache into a network payload. Existing PD-side KV reduction methods are mostly binary: selected tokens are transmitted at full precision and the rest are not transmitted. This paper argues that binary selection leaves a useful design space unused. SpectrumKV assigns a precision level to each token instead: attention sinks and other high-importance tokens are protected at FP16, medium-importance

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 负责KV payload、token precision 与网络传输控制；在本 source 中，需被显式持有、传递或阻断的状态正是“SpectrumKV 将 PD 之间的 KV 传输从 token keep/drop 二元决策改为 per-token mixed precision，使网络字节、量化误差与重算成为同一控制面。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08635v1 §5 Experimental Setup; §6 Results; §7 Additional Analyses` 实际支持的合同是 `Disclosed — WikiText-2 PPL, NIAH at 4,096 tokens/19 depths, 2K–8K context sweeps, TTFT/TPS transfer-path timing and ablations`，evaluator 是 `Disclosed — PPL delta, NIAH accuracy, TTFT, TPS, transfer budget, quantization error and probe/ablation outcomes`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08635v1 §2 Problem Formulation; §4 SpectrumKV Policy`；counterevidence locator: `arXiv:2606.08635v1 §8 Evidence boundary; §9 Limitations and Threats to Validity`。

**Trade-off / failure / coexistence / evolution。** mixed-precision KV 降低网络字节却增加 per-token probe、量化 kernel 与 fallback；INT4 probe 失败时必须回退 FP16/INT8，完整 scheduler 与 contention 仍未被证明。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08635:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08635v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08635:end -->
<!-- review:SF-2026-ARXIV-2606-08635:end -->

<!-- review:SF-2026-ARXIV-2606-08661:start -->
### 2606.08661 — Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：Data Agent 把数据库执行、外部数据资源与 agent reasoning 三个攻击面串联，安全 owner 必须覆盖 query authority、tool side effects 与 evidence provenance。 exact-v1 摘要将具体问题界定为：Data agents integrate LLM-driven reasoning with relational data access, executable analytical tools, and multi-step workflow orchestration, making them increasingly central to enterprise analytics. This integration introduces new security vulnerabilities across data resources, database execution, and agent reasoning, recombining concerns from database security and general-purpose LLM-agent security into failure modes that neither line of work captures on its own. To address this gap, we present a systematic securit

**State / data / control owner。** `PLATFORM-SECURITY` 负责输入信任、权限与阻断/升级控制；在本 source 中，需被显式持有、传递或阻断的状态正是“Data Agent 把数据库执行、外部数据资源与 agent reasoning 三个攻击面串联，安全 owner 必须覆盖 query authority、tool side effects 与 evidence provenance。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08661v1 §5 Evaluating Vulnerabilities; §6 Evaluation Details` 实际支持的合同是 `Disclosed — isolated benchmark data across database execution, external-resource and agent-reasoning attack surfaces plus commercial-service checks`，evaluator 是 `Disclosed — vulnerability/attack outcomes, sensitivity, cross-system generalization and explicit ethical scope`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08661v1 §3 Threat Model and Overview; §4 Vulnerability Analysis`；counterevidence locator: `arXiv:2606.08661v1 §6.4 sensitivity; §6.5 commercial-system generalization; §7 takeaways`。

**Trade-off / failure / coexistence / evolution。** 三攻击面联合分析提高覆盖却扩大权限与隔离成本；只读查询仍可用轻量 guard，具副作用 tool 必须升级审批，商业系统结果不能外推到 host compromise。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08661:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08661v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08661:end -->
<!-- review:SF-2026-ARXIV-2606-08661:end -->

<!-- review:SF-2026-ARXIV-2606-08671:start -->
### 2606.08671 — SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。 exact-v1 摘要将具体问题界定为：Agent skills extend language-model agents with task-specific procedures, scripts, and references, but the tasks and environments they target continually change. Existing methods improve skills in bounded runs and retain only the final artifact, discarding the decision history that later agents need to interpret prior revisions, evaluations, and rejected alternatives. We introduce SkillHone, a harness for continual agent skill evolution grounded in persistent decision history. SkillHone pairs skill revisions with ev

**State / data / control owner。** `AGENT-REFLECTION` 负责skill revision history、evaluation 与回退状态；在本 source 中，需被显式持有、传递或阻断的状态正是“SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08671v1 §3 Experiments; §3.1 Benchmarks and Evaluation Settings` 实际支持的合同是 `Disclosed — GAIA and WebWalkerQA-EN in curated-search and raw-open-web settings`，evaluator 是 `Disclosed — benchmark accuracy by difficulty split plus optimization-trajectory comparison; English and single-skill limitations stated`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08671v1 §2 Method; §§2.2–2.3 harness and persistent decision history`；counterevidence locator: `arXiv:2606.08671v1 §5 Conclusion; unnumbered Limitations`。

**Trade-off / failure / coexistence / evolution。** 持久 decision history 增强可解释回退却会累积陈旧技能和无效分支；无状态任务仍可用一次性 skill，演进压力是 history compaction 与 cross-skill conflict。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08671:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08671v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08671:end -->
<!-- review:SF-2026-ARXIV-2606-08671:end -->

<!-- review:SF-2026-ARXIV-2606-08679:start -->
### 2606.08679 — Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：leaderboard 必须传播 task-level 不确定性并输出 rank intervals，而不是把多任务均值压成确定名次。 exact-v1 摘要将具体问题界定为：Pretrained models are often evaluated on multi-task leaderboards to measure their applicability in diverse contexts. However, current methods for aggregating performance across tasks into leaderboard-level rankings do not address the uncertainty and variability at the task level. While recent works have proposed interval-based model rankings, the principled aggregation of uncertainty from individual tasks to leaderboard-level rankings remains unaddressed, and variation in models' performance across tasks is frequen

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“leaderboard 必须传播 task-level 不确定性并输出 rank intervals，而不是把多任务均值压成确定名次。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08679v1 §4 Experiments; §§4.1–4.3` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Pretrained models are often evaluated on multi-task leaderboards to measure their applicability in diverse contexts.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08679v1 §2 Task-level model ranking; §3 ranking across tasks`；counterevidence locator: `arXiv:2606.08679v1 Appendix D rank-interval interpretation and task selection`。

**Trade-off / failure / coexistence / evolution。** rank interval 诚实表达不确定性但弱化单一榜单的简洁排序；样本太少会产生宽区间，task-level score 仍需保留以解释区间来源。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08679:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08679v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08679:end -->
<!-- review:SF-2026-ARXIV-2606-08679:end -->

<!-- review:SF-2026-ARXIV-2606-08702:start -->
### 2606.08702 — ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：ConMem 显式建模 memory-skill relation，并从 noisy trajectories 中选择结构化记忆以支持 training-free multi-agent adaptation。 exact-v1 摘要将具体问题界定为：Recent advances have improved the adaptive capabilities of LLM-based multi-agent systems (MAS) through memory-, skill-, and learning-based approaches, yet these approaches remain challenged by noisy trajectories, insufficient modeling of memory-skill relations, and reliance on additional training or high-quality supervision. To address these limitations, we propose ConMem, a relation-aware and training-free framework that enables efficient multi-agent adaptation through cross-experience coordination. Specifically,

**State / data / control owner。** `AGENT-MEMORY` 负责持久轨迹、memory-skill relation 与更新状态；在本 source 中，需被显式持有、传递或阻断的状态正是“ConMem 显式建模 memory-skill relation，并从 noisy trajectories 中选择结构化记忆以支持 training-free multi-agent adaptation。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08702v1 §5 Experiment; Appendix A.3 protocol` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08702v1 §3 budgeted context-control preliminaries; §4 Methodology; §§4.1–4.5`；counterevidence locator: `arXiv:2606.08702v1 §5.3 Additional Analysis and Discussion; appendix run-isolation boundaries`。

**Trade-off / failure / coexistence / evolution。** 结构化 memory 降低 noisy trajectory 干扰却增加 relation extraction 错误；新任务无可靠 relation 时原始轨迹检索仍应回退，后续压力是多 agent 写冲突。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08702:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08702v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08702:end -->
<!-- review:SF-2026-ARXIV-2606-08702:end -->

<!-- review:SF-2026-ARXIV-2606-08755:start -->
### 2606.08755 — Co-Evolving Skill Generation and Policy Optimization

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：skill generation 与 policy optimization 必须共同验证新 skill 的 usefulness，避免 skill bank 只积累未经行为结果校验的文本程序。 exact-v1 摘要将具体问题界定为：Skill-augmented reinforcement learning improves language agents by storing reusable procedural knowledge acquired from past experience. Existing methods typically use strong language models to analyze trajectories, generate skills, and update a retrievable skill bank during online training. However, they rarely assess whether a newly generated skill is useful before it is stored and reused. We find that this assumption is unreliable: even skills generated by proprietary frontier LLMs exhibit highly mixed utility, w

**State / data / control owner。** `AGENT-REFLECTION` 负责skill revision history、evaluation 与回退状态；在本 source 中，需被显式持有、传递或阻断的状态正是“skill generation 与 policy optimization 必须共同验证新 skill 的 usefulness，避免 skill bank 只积累未经行为结果校验的文本程序。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08755v1 §5 Experiments; §5.1 setup; §§5.2–5.5` 实际支持的合同是 `Disclosed — ALFWorld, WebShop and Search-QA policy/skill co-evolution`，evaluator 是 `Disclosed — task reward/success, skill utility, joint-optimization ablation and negative baselines`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08755v1 §3 Preliminary negative results; §4 Skill-Augmented Policy Optimization`；counterevidence locator: `arXiv:2606.08755v1 §5.4 skill utility; §5.5 ablation; Appendix D negative/alternate results`。

**Trade-off / failure / coexistence / evolution。** skill 与 policy 共演化避免无用技能堆积，却带来非平稳 credit assignment；短任务直接 policy update 仍更简单，失败时要回滚 skill bank 与 checkpoint。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08755:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08755v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08755:end -->
<!-- review:SF-2026-ARXIV-2606-08755:end -->

<!-- review:SF-2026-ARXIV-2606-08761:start -->
### 2606.08761 — APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。 exact-v1 摘要将具体问题界定为：W4A4 quantization promises full utilization of INT4 Tensor Cores, yet group dequantization overhead on CUDA Cores has driven existing systems to mixed-precision fallbacks. We present the first systematic study of how intra-SM compute balance governs this bottleneck. Through controlled benchmarks across four GPUs from Ampere and Ada architectures, we identify the Tensor Cores to CUDA Cores throughput ratio ($ρ$) as the primary hardware indicator: the W4A4-g128 kernel yields $2.0$--$2.5\times$ speedup on RTX~3090 ($ρ

**State / data / control owner。** `INFER-GPU-MEMORY` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08761v1 §5 Evaluation; §5.1 setup; §§5.2–5.4` 实际支持的合同是 `Disclosed — WikiText2 perplexity, PIQA/ARC/HellaSwag/WinoGrande zero-shot accuracy, kernel tests and vLLM end-to-end serving`，evaluator 是 `Disclosed — kernel/end-to-end speedup, PPL delta, zero-shot accuracy and cross-GPU rho analysis`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08761v1 §2 W4A4 performance gap; §3 APEX4 quantization; §4 pure-W4A4 kernel`；counterevidence locator: `arXiv:2606.08761v1 §5.5 cross-platform analysis; §7 Conclusion and deployment boundary`。

**Trade-off / failure / coexistence / evolution。** 纯 W4A4 提升高 batch 性能但依赖特定 SM 映射和 workload 饱和度；低 batch 或不同 GPU 上 FP16/W4A8 fallback 仍合理，演进压力是连续 batching。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08761:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08761v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08761:end -->
<!-- review:SF-2026-ARXIV-2606-08761:end -->

<!-- review:SF-2026-ARXIV-2606-08769:start -->
### 2606.08769 — RadOT-Eval: Auditable Structured-Evidence Transport for Radiology Report Evaluation

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：RadOT-Eval 将 radiology generation 的 omission、hallucination、polarity、location、uncertainty 与 temporal error 映射为可审计 structured-evidence transport。 exact-v1 摘要将具体问题界定为：Automatic evaluation is critical for high-stakes text generation, where errors often involve omitted findings, hallucinated content, polarity reversals, location changes, uncertainty mismatches, and temporal-comparison errors rather than low surface similarity alone. Radiology report generation provides a challenging test case because generated reports must preserve structured clinical evidence across sources. We present RadOT-Eval, an interpretable structured-evidence optimal transport framework for offline auditi

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“RadOT-Eval 将 radiology generation 的 omission、hallucination、polarity、location、uncertainty 与 temporal error 映射为可审计 structured-evidence transport。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08769v1 §V Evaluation Protocol; §VI Results` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Automatic evaluation is critical for high-stakes text generation, where errors often involve omitted findings, hallucinated content, polarity reversals, location changes, uncertainty mismatches, and temporal-comparison errors rather than low surface similarity alone.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08769v1 §III problem/data; §IV RadOT-Eval method`；counterevidence locator: `arXiv:2606.08769v1 §VII Discussion, limitations, and evidence-transport boundary`。

**Trade-off / failure / coexistence / evolution。** structured evidence transport 提升可审计性却依赖实体抽取、极性和时间对齐；自由文本专家判断仍处理 ontology 外发现，错误 mapping 会系统性误罚。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08769:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08769v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08769:end -->
<!-- review:SF-2026-ARXIV-2606-08769:end -->

<!-- review:SF-2026-ARXIV-2606-08779:start -->
### 2606.08779 — Reformulate LLM Reinforcement Learning for Efficient Training under Black-box Discrepancy

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：训练 engine 与推理 engine 的 discrepancy 会使 RL objective 与实际 rollout distribution 脱节，post-training 必须记录 sampler/implementation identity。 exact-v1 摘要将具体问题界定为：Reinforcement Learning (RL) has emerged as a pivotal post-training paradigm, yet it frequently suffers from unpredictable sub-optimum performance or even training collapses. Recent findings attribute these failures to a hidden train-inference discrepancy (or mismatch), stemming from the disparate underlying engines and architecture. We find that the training policy can actively self-correct such a discrepancy when provided with an appropriate learning signal. Then, we further empirically identify a discrepancy tole

**State / data / control owner。** `TRAIN-RLHF` 负责rollout distribution、checkpoint plasticity 与 sampler identity；在本 source 中，需被显式持有、传递或阻断的状态正是“训练 engine 与推理 engine 的 discrepancy 会使 RL objective 与实际 rollout distribution 脱节，post-training 必须记录 sampler/implementation identity。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08779v1 §6 Experiments; setup, results, and ablations` 实际支持的合同是 `Disclosed — DAPO-Math-17K RL with math-verify reward and explicit train/inference-engine discrepancy`，evaluator 是 `Disclosed — math reward, training efficiency/stability, engine-discrepancy and ablation outcomes`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08779v1 §3 engine-discrepancy decision space; §4 magic penalty; §5 discrepancy-constrained MDP`；counterevidence locator: `arXiv:2606.08779v1 §7 Limitations and engine-identity boundary`。

**Trade-off / failure / coexistence / evolution。** discrepancy-aware objective 避免强制统一 engine，却增加双 policy 估计与 penalty 校准；能低成本对齐 kernel/precision 时旧路径仍优先，黑盒漂移会使约束失真。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08779:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08779v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08779:end -->
<!-- review:SF-2026-ARXIV-2606-08779:end -->

<!-- review:SF-2026-ARXIV-2606-08790:start -->
### 2606.08790 — RAILS: Verification-Native Clearing For Agentic Commerce

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：RAILS 把 delegated obligation、verification、liability 与 settlement action 组合成 agent commerce 的 clearing contract，而不把支付成功等同于任务履约。 exact-v1 摘要将具体问题界定为：Autonomous agents negotiate, purchase, deploy code, and move funds, but no neutral mechanism determines whether they met their delegated obligation, who is responsible when they did not, or which settlement action follows. This is the agentic clearing problem. Tool protocols (MCP), inter-agent communication (A2A), payment rails (x402), mandate and network agent protocols (AP2, Visa, Mastercard), and settlement-risk standards each assume that determination and none produce it. Clearing is the missing primitive. Paym

**State / data / control owner。** `AGENT-TOOL-CALLING` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“RAILS 把 delegated obligation、verification、liability 与 settlement action 组合成 agent commerce 的 clearing contract，而不把支付成功等同于任务履约。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08790v1 §8 worked scenarios and exposure analysis` 实际支持的合同是 `Not applicable — formal clearing protocol with worked scenarios, not an empirical benchmark`，evaluator 是 `Not applicable — definitions/propositions and worked scenarios do not constitute empirical verification`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08790v1 §3 RAILS at a glance; §4 formal model; §§5–7 verification/settlement state machine`；counterevidence locator: `arXiv:2606.08790v1 Not Disclosed — no empirical limitations section; formal proposal is bounded to §§3–8 and does not prove real task completion`。

**Trade-off / failure / coexistence / evolution。** verification-native clearing 明确责任却引入证明、争议与 settlement latency；低价值可逆交易可保留轻量支付，形式 invariant 不等同真实任务已履约。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08790:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08790v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08790:end -->
<!-- review:SF-2026-ARXIV-2606-08790:end -->

<!-- review:SF-2026-ARXIV-2606-08806:start -->
### 2606.08806 — Governance Controls for AI-Generated Test Artifacts in Autonomous Software Testing

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：AI-generated test artifacts 需要 provenance、policy checks、human approval 与 audit trail 的治理层，生成速度不能替代测试资产的责任链。 exact-v1 摘要将具体问题界定为：Artificial Intelligence (AI) and Large Language Models (LLMs) are increasingly used in autonomous software testing; however, AI-generated test artifacts often suffer from hallucinations, compliance violations, security risks, and limited explainability. To enhance the reliability, transparency, and trustworthiness of AI-generated testing artifacts, this research introduces the concept of Governance-Aware Autonomous Testing Framework (GATF). The framework extends the autonomous testing lifecycle with governance vali

**State / data / control owner。** `PLATFORM-PRODUCTION` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“AI-generated test artifacts 需要 provenance、policy checks、human approval 与 audit trail 的治理层，生成速度不能替代测试资产的责任链。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08806v1 §5 Results and artifact-policy analysis` 实际支持的合同是 `Disclosed — Defects4J and PROMISE with Jenkins/GitHub Actions governance checks`，evaluator 是 `Disclosed — test accuracy/validity/success, hallucination rate, governance precision/recall/FPR and latency`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08806v1 §4 Governance Methodology and control chain`；counterevidence locator: `arXiv:2606.08806v1 §6 Conclusion; provenance, approval, and auditability boundary`。

**Trade-off / failure / coexistence / evolution。** governance gate 降低幻觉测试资产却增加审批时延和分类器误报；低风险临时测试可保留 sandboxed 快路径，provenance 丢失时资产必须失效。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08806:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08806v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08806:end -->
<!-- review:SF-2026-ARXIV-2606-08806:end -->

<!-- review:SF-2026-ARXIV-2606-08813:start -->
### 2606.08813 — Aperon Technical Report: Hierarchical No-Pointer Tangent-Local Search for High-Dimensional Approximate Nearest Neighbors

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：HNTL 用 hierarchical no-pointer tangent-local layout 降低 ANN graph 的 pointer tax 与不规则访存，把候选生成的数据布局与 CPU pipeline 一起优化。 exact-v1 摘要将具体问题界定为：We present HNTL (Hierarchical No-pointer Tangent-Local), the core vector indexing and candidate generation framework of the Aperon vector memory system. Proximity graphs (e.g., HNSW) incur a heavy pointer tax in memory overhead and induce irregular memory accesses that stall CPU pipelines. HNTL resolves this by partitioning the high-dimensional space into local, coherent grains, representing vectors as low-dimensional coordinates on local tangent spaces, and scanning them sequentially using a pointerless Block-SoA

**State / data / control owner。** `AGENT-RAG` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“HNTL 用 hierarchical no-pointer tangent-local layout 降低 ANN graph 的 pointer tax 与不规则访存，把候选生成的数据布局与 CPU pipeline 一起优化。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08813v1 §3 Implementation, hardware, and retrieval results` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: N=10,000), local PCA captures 96.3% of the variance, allowing HNTL to achieve a final Rerank Recall@10 of 1.0000 with a candidate pool size of only C=20 vectors. Hardware profiling via Apple kperf CPU Performance Monitoring Unit (PMU) counters demonstrates a 3.61x speedup (4.137 ns/vector vs. 14.951 ns/vector) for our NEON auto-vectorized C++ Block-SoA scan engine over standard pointer-chasing graph traversals, drive`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08813v1 §2 Aperon system architecture and HNTL layout`；counterevidence locator: `arXiv:2606.08813v1 §4 Conclusion; CPU/ANN-layout scope boundary`。

**Trade-off / failure / coexistence / evolution。** no-pointer tangent-local layout 降低 CPU pointer tax，却受维度、grain partition 与 cold-tier 量化影响；成熟 HNSW/FAISS 路径应共存，GPU warp scan 尚属未来工作。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08813:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08813v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08813:end -->
<!-- review:SF-2026-ARXIV-2606-08813:end -->

<!-- review:SF-2026-ARXIV-2606-08831:start -->
### 2606.08831 — Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：multi-step reasoning 的 factuality error 具有 ancestor-conditioned DAG 结构，conformal control 不能把 node-wise error 简单累加。 exact-v1 摘要将具体问题界定为：Large language models (LLMs) increasingly perform multi-step reasoning, where intermediate claims form implicit directed acyclic graphs whose node correctness is structurally conditioned on their ancestors. This makes factuality uncertainty structural, rather than a trivial accumulation of node-wise errors, and necessitates inference-time uncertainty quantification over the reasoning structure. While conformal prediction (CP) offers flexible user-specified factuality control, existing work remains post-hoc and cann

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“multi-step reasoning 的 factuality error 具有 ancestor-conditioned DAG 结构，conformal control 不能把 node-wise error 简单累加。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08831v1 §4 Experiments` 实际支持的合同是 `Disclosed — multi-step reasoning DAG factuality with calibration/test splits and ancestor-closed subgraph objectives`，evaluator 是 `Disclosed — no-false/no-miss conformal coverage, retained subgraph utility and calibration validity`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08831v1 §2 Setup and ancestor-conditioned DAG errors; §3 inference-time subgraph prediction and conformal calibration`；counterevidence locator: `arXiv:2606.08831v1 §6 Limitations and graph/calibration assumptions`。

**Trade-off / failure / coexistence / evolution。** ancestor-aware conformal control提供有限样本覆盖，却要求 exchangeability、nested score 与正确 DAG；graph construction 错误会破坏保证，普通 node scorer 仍可作诊断而非证明。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08831:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08831v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08831:end -->
<!-- review:SF-2026-ARXIV-2606-08831:end -->

<!-- review:SF-2026-ARXIV-2606-08840:start -->
### 2606.08840 — Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：code model 的 pass rate 必须按语言、题型与 execution failure mode 分层，aggregate pass rate 会掩盖可部署性边界。 exact-v1 摘要将具体问题界定为：Code generation models are typically compared using compact execution benchmarks and aggregate pass rates, but such summaries obscure how performance varies across programming languages, problem families, and failure modes. We present a large-scale, execution-grounded evaluation of 9 openly accessible LLMs specialized for coding on 2,707 free LeetCode problems across 12 programming languages. Our corpus contains 325,343 problem-model-language jobs, each linked to prompt metadata, extracted code, LeetCode execution

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“code model 的 pass rate 必须按语言、题型与 execution failure mode 分层，aggregate pass rate 会掩盖可部署性边界。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08840v1 §IV Results and execution failure modes` 实际支持的合同是 `Disclosed — multilingual execution-grounded code tasks stratified by language, task type and runtime failure`，evaluator 是 `Disclosed — execution pass rate stratified by language/task plus compile/runtime/timeout failure modes`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08840v1 §III Evaluation Methodology`；counterevidence locator: `arXiv:2606.08840v1 §V Discussion and aggregate-pass-rate boundary`。

**Trade-off / failure / coexistence / evolution。** execution-grounded分层评测提高可部署解释，却受 sandbox、编译器与默认参数影响；aggregate pass rate 仍可作摘要，但不能替代语言/失败模式切片。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08840:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08840v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08840:end -->
<!-- review:SF-2026-ARXIV-2606-08840:end -->

<!-- review:SF-2026-ARXIV-2606-08867:start -->
### 2606.08867 — Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：100M-user support agent 把离线 evaluation、context engineering、training 与 online measurement 组成闭环，单一模型分数不代表生产 readiness。 exact-v1 摘要将具体问题界定为：The rapid rise in LLM capabilities has made AI agents increasingly viable across a broad range of tasks. Among the most promising applications is building production-ready customer-facing agents, a challenge that demands coordinated excellence in evaluation methodology, context engineering, training, and online measurement. Yet these critical pillars are typically developed in isolation, creating blind spots that only surface after deployment. In this paper, we present a unified framework that bridges offline devel

**State / data / control owner。** `AGENT-PLATFORM` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“100M-user support agent 把离线 evaluation、context engineering、training 与 online measurement 组成闭环，单一模型分数不代表生产 readiness。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08867v1 §5 Case Study and evaluation; §6 offline/online measurement` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Among the most promising applications is building production-ready customer-facing agents, a challenge that demands coordinated excellence in evaluation methodology, context engineering, training, and online measurement.`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08867v1 §4 Production support-agent system design`；counterevidence locator: `arXiv:2606.08867v1 privacy, rollout, and production-readiness boundaries in §§6–7`。

**Trade-off / failure / coexistence / evolution。** 离线到在线闭环提升生产适配但带来隐私、实验隔离和反馈延迟；静态 benchmark 仍负责可复现回归，在线 metric 漂移不能静默改写训练目标。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08867:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08867v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08867:end -->
<!-- review:SF-2026-ARXIV-2606-08867:end -->

<!-- review:SF-2026-ARXIV-2606-08869:start -->
### 2606.08869 — A Low-Latency Semantic State Estimator using Latent Predictive Learning for Dynamic Network Monitoring and Orchestration

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：dynamic cloud-edge control loop 需要把变动 node set 与 query 编码成低延迟 semantic state，而不是只收集 raw counters。 exact-v1 摘要将具体问题界定为：Closed-loop network monitoring and orchestration increasingly require semantic interpretations of live telemetry beyond raw counter collection. However, dynamic cloud-edge environments change both the active node set and the monitoring query at runtime, while control loops demand bounded millisecond-scale responses. We introduce a latent predictive state estimator (LPSE) for dynamic network monitoring and orchestration, built on latent predictive learning over streaming telemetry. The framework converts variable-ca

**State / data / control owner。** `PLATFORM-MONITORING` 负责evidence graph、telemetry state 与诊断 verdict；在本 source 中，需被显式持有、传递或阻断的状态正是“dynamic cloud-edge control loop 需要把变动 node set 与 query 编码成低延迟 semantic state，而不是只收集 raw counters。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08869v1 §IV Implementation/training; §V Experimental Results` 实际支持的合同是 `Disclosed — one seven-node live Kubernetes cluster under five stress profiles; 100-question and 700-query comparisons`，evaluator 是 `Disclosed — clean/stressed accuracy, latency, robustness, model size and cluster-state coverage`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08869v1 §II dynamic cloud-edge model; §III semantic-state framework`；counterevidence locator: `arXiv:2606.08869v1 §VI Conclusion and topology/workload scope`。

**Trade-off / failure / coexistence / evolution。** semantic state 压缩降低控制延迟，却可能丢失罕见 raw signal；原始 telemetry 必须保留用于回放，拓扑变化和 codebook drift 会使 50 ms 内的错误更快传播。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08869:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08869v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08869:end -->
<!-- review:SF-2026-ARXIV-2606-08869:end -->

<!-- review:SF-2026-ARXIV-2606-08891:start -->
### 2606.08891 — PALUTE: Processing-In-Memory Acceleration via Lookup Table for Edge LLM Inference

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：PALUTE 用 processing-in-memory lookup table 同时吸收 quantized GEMM 的 dequantization 与 nonlinear operator 成本，改变 edge inference 的 data-movement owner。 exact-v1 摘要将具体问题界定为：Large language models are increasingly deployed on edge devices with tight power and area budgets. While mixed-precision GEMM reduces arithmetic complexity, quantized inference is often dominated by dequantization and nonlinear operators. Lookup Table (LUT)-based method mitigates these costs by precomputing outputs and replacing repeated arithmetic with table lookups, but existing designs incur significant capacity and lookup-latency overheads. This paper presents PALUTE, a LUT-based Processing-In-Memory accelerato

**State / data / control owner。** `INFER-TENSORRT-LLM` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“PALUTE 用 processing-in-memory lookup table 同时吸收 quantized GEMM 的 dequantization 与 nonlinear operator 成本，改变 edge inference 的 data-movement owner。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08891v1 §4 Evaluation; §4.1 Experimental Setup; §§4.2–4.4` 实际支持的合同是 `Disclosed — cycle-accurate end-to-end Transformer decode simulation plus RTL synthesis and sensitivity/overhead studies`，evaluator 是 `Disclosed — TPS, power, energy/area efficiency, sensitivity and overhead under simulation/synthesis`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08891v1 §3 PALUTE Architecture Design; §§3.1–3.4`；counterevidence locator: `arXiv:2606.08891v1 §4.3 sensitivity; §4.4 overhead; §5 Conclusion and simulation boundary`。

**Trade-off / failure / coexistence / evolution。** PIM LUT 减少数据移动却以表容量、生成、工艺假设和灵活性为代价；GPU/NPU 仍适合动态精度与模型，simulation/RTL 结果不能当作实芯片部署证明。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08891:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08891v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08891:end -->
<!-- review:SF-2026-ARXIV-2606-08891:end -->

<!-- review:SF-2026-ARXIV-2606-08892:start -->
### 2606.08892 — Diffuse AI Control on Fuzzy Tasks

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：Diffuse AI Control 针对长时段、fuzzy-task sabotage 把控制证据分散到多次任务与审计预算，而非依赖单次可验证 outcome。 exact-v1 摘要将具体问题界定为：AI models deployed in critical domains, such as AI safety research, may subtly sabotage our efforts due to misalignment. Diffuse AI Control is a subfield of AI safety concerned with mitigating risks from AI sabotage distributed over long deployment horizons (diffuse threats). These risks are particularly pernicious on fuzzy tasks, i.e. tasks which are hard to grade or require intuition. To understand diffuse threats on fuzzy tasks, we introduce a framework that considers AI control as an adversarial game between a

**State / data / control owner。** `PLATFORM-SECURITY` 负责输入信任、权限与阻断/升级控制；在本 source 中，需被显式持有、传递或阻断的状态正是“Diffuse AI Control 针对长时段、fuzzy-task sabotage 把控制证据分散到多次任务与审计预算，而非依赖单次可验证 outcome。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08892v1 §5 mitigations; Appendix C scorer details; Appendices D–G optimization/experiments` 实际支持的合同是 `Disclosed — fuzzy research-proposal tasks with automated red/blue prompt optimization, scorer controls and appended stress experiments`，evaluator 是 `Disclosed — weak/strong scorer outcomes, saddle-point robustness, variance/ablation and qualitative attack analysis`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08892v1 §2 diffuse-threat control framework; §§3–5 red/blue automated experiment planning`；counterevidence locator: `arXiv:2606.08892v1 §7 Limitations and Future Work; fuzzy-task and automated-scorer boundary`。

**Trade-off / failure / coexistence / evolution。** diffuse control 聚合长时证据，却依赖弱/强 scorer 与 prompt optimization 的代表性；可验证任务仍应使用单次 outcome gate，fuzzy scorer 被协同优化时可能共同失真。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08892:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08892v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08892:end -->
<!-- review:SF-2026-ARXIV-2606-08892:end -->

<!-- review:SF-2026-ARXIV-2606-08893:start -->
### 2606.08893 — Cheap Reward Hacking Detection

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：cheap reward-hacking detector 用 trajectory embedding 与 metadata/reward distance 近似替代昂贵 LLM judge，但其清洗 split 与阈值不能外推为通用证明。 exact-v1 摘要将具体问题界定为：A small transformer encoder is trained to map Terminal-Wrench trajectories onto a unit sphere where embedding distance approximates the $L_1$ distance between reward and metadata signals. A linear probe on top of that embedding detects reward hacking on the cleaned test split with AUC $0.9467$ and TPR@5%FPR $0.8296$, matching the TW sanitized LLM-as-judge AUC ($0.9510$ on the cleaned split) and exceeding its TPR@5%FPR ($0.7130$ vs $0.8296$) on the same information condition, at roughly four orders of magnitude lowe

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 负责任务、scaffold、judge、metric 与不确定性元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“cheap reward-hacking detector 用 trajectory embedding 与 metadata/reward distance 近似替代昂贵 LLM judge，但其清洗 split 与阈值不能外推为通用证明。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.08893v1 §4 Results; §§4.1–4.6` 实际支持的合同是 `Disclosed — cleaned Terminal-Wrench trajectory variants with 5,689/735/690 train/val/test split`，evaluator 是 `Disclosed — ROC AUC, TPR@5%FPR, cleaned-split comparison, stripped-input and adversarial robustness ablations`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.08893v1 §2 detector objective/architecture; §3 dataset cleaning and training`；counterevidence locator: `arXiv:2606.08893v1 §5 Conclusion/Future Work; Appendix A negative path and robustness ablations`。

**Trade-off / failure / coexistence / evolution。** 小 encoder 将 judge 成本降四个数量级，却依赖清洗 split 且读取自然语言 reasoning；格式或策略漂移会击穿 probe，昂贵 judge 仍应抽样复核。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08893:start -->
**Claim boundary。** 可引用内容限于 `arXiv:2606.08893v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08893:end -->
<!-- review:SF-2026-ARXIV-2606-08893:end -->

<!-- review:SF-2026-ARXIV-2606-08919:start -->
### 2606.08919 — Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：人工审批不是无限 oracle；guard 的 escalation policy 必须把 reviewer 分歧、疲劳与 flooding 下的有限 attention 当作可耗尽资源。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.08919v1 §5 Experiments` 支持 `Disclosed — 125 个 adversarially weighted agent actions、多人风险标注与 fatigue/flooding simulation`，evaluator 为 `Disclosed — reviewer agreement、selective-risk/coverage curve 与 realized-safety curve`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.08919v1 §3 Selective Classification; §4 Endogenous Reviewer Model`；counterevidence locator: `arXiv:2606.08919v1 §6 Limitations and Human-Study Boundary`。

**Trade-off / failure / coexistence / evolution。** 降低 escalation load 会提高自动放行风险；全升级又会因疲劳降低实际安全性，静态审批仍适合低频高危动作。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08919:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.08919v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08919:end -->
<!-- review:SF-2026-ARXIV-2606-08919:end -->

<!-- review:SF-2026-ARXIV-2606-08950:start -->
### 2606.08950 — When More Cores Hurts: The Vector Database Scaling Paradox in HPC

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：向量数据库的 insertion、indexing、query 与 mixed read/write 生命周期必须同 storage hierarchy、broadcast-gather 与 partitioning 一起评估；增加 core/node 可因协调瓶颈反向降低吞吐。

**State / data / control owner。** `AGENT-RAG` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.08950v1 §§IV–V Cloud/HPC and lifecycle evaluation` 支持 `Disclosed — Qdrant/Milvus/Weaviate，四个 embedding datasets，两台生产超算，最多 64 nodes/256 workers`，evaluator 为 `Disclosed — upload/index time、QPS、latency/P95/P99、recall 与 storage overhead`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.08950v1 §III Methodology`；counterevidence locator: `arXiv:2606.08950v1 §VI Discussion and Conclusion`。

**Trade-off / failure / coexistence / evolution。** HPC-native deployment扩大资源却引入 MPI/Apptainer、shared storage 与 aggregation bottleneck；云端架构在普通规模仍更易运维。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08950:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.08950v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08950:end -->
<!-- review:SF-2026-ARXIV-2606-08950:end -->

<!-- review:SF-2026-ARXIV-2606-08960:start -->
### 2606.08960 — Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：benchmark verifier 应通过 hacker→fixer→solver 的闭环迭代：攻击发现 exploit、修补拒绝 exploit、solver 防止补丁把合法解一并拒绝。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.08960v1 §4 Hardening Results` 支持 `Disclosed — 1,968 tasks/5 terminal-agent benchmarks；KernelBench 与 Terminal-Bench case studies`，evaluator 为 `Disclosed — attack success、held-out exploit rejection、legitimate-solver acceptance 与 patch transfer`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.08960v1 §3 The Hacker-Fixer Loop; Appendix D`；counterevidence locator: `arXiv:2606.08960v1 Appendix A Limitations`。

**Trade-off / failure / coexistence / evolution。** 循环只覆盖 hacker 能发现的攻击，shared defense pool 也绑定共同 evaluation substrate；独立 held-out exploit corpus 仍不可省。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-08960:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.08960v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-08960:end -->
<!-- review:SF-2026-ARXIV-2606-08960:end -->

<!-- review:SF-2026-ARXIV-2606-09005:start -->
### 2606.09005 — Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：RAG prompt assembly 必须把 document-authored metadata/provenance 视为 data 而非 policy，避免不可信文档在同一自然语言 channel 中冒充 control signal。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09005v1 §§IV–V Experimental Design and Results` 支持 `Disclosed — 六个 model settings、paired prompt-pressure controls、toy/semi-realistic/embedding/LangChain-style RAG`，evaluator 为 `Disclosed — synthetic-canary disclosure、paired lift、confidence interval、FDR 与 source-authority probe`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09005v1 §III System and Attacker Model; §III-C Control/Data Boundary`；counterevidence locator: `arXiv:2606.09005v1 §X Limitations and Validity Threats`。

**Trade-off / failure / coexistence / evolution。** 结构化 channel separation、redaction 与 output scanning 增加集成成本且都不是完整防御；旧式文本提示仍可作为辅助但不能承担 authority。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09005:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09005v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09005:end -->
<!-- review:SF-2026-ARXIV-2606-09005:end -->

<!-- review:SF-2026-ARXIV-2606-09061:start -->
### 2606.09061 — Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill LLM Serving

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：chunked-prefill scheduler 需联合持有 request age、remaining prefill work、predicted latency 与 active-prefill cap，而不只用 arrival order 或 static token budget。

**State / data / control owner。** `INFER-SCHEDULING` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09061v1 §4 Experiment and Evaluation` 支持 `Disclosed — 混合长短 prompt、NVIDIA GPU 与 Ascend、single/multi-GPU chunked-prefill workloads`，evaluator 为 `Disclosed — mean/P99 E2E latency、TTFT、fairness、fragmentation、predictor error 与 portability`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09061v1 §3 The Developed Methodology`；counterevidence locator: `arXiv:2606.09061v1 §4.6 Discussion; §5 Future Work`。

**Trade-off / failure / coexistence / evolution。** aging 抑制 starvation 却牺牲部分短请求优先；latency predictor 会漂移，chunk 太大时重排机会消失，FCFS 仍是保守基线。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09061:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09061v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09061:end -->
<!-- review:SF-2026-ARXIV-2606-09061:end -->

<!-- review:SF-2026-ARXIV-2606-09084:start -->
### 2606.09084 — Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：tool agent 的安全状态跨越多轮 artifact write/read；防御必须记录 artifact lineage 并在组合读取时执行 provenance-aware policy，不能只审核当前 turn。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09084v1 §4 Evaluation` 支持 `Disclosed — 有限 model/tool/pipeline topologies 下的 context-fractured agent attack testbed`，evaluator 为 `Disclosed — ASR、context-removal/depth/width ablations、topology sensitivity 与 artifact inspection`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09084v1 §3 Context-Fractured Decomposition`；counterevidence locator: `arXiv:2606.09084v1 §5 Limitations`。

**Trade-off / failure / coexistence / evolution。** lineage tagging 增加 instrumentation/storage 与 benign cross-session false positive；论文只证明需要该控制面，没有交付校准后的完整防御。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09084:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09084v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09084:end -->
<!-- review:SF-2026-ARXIV-2606-09084:end -->

<!-- review:SF-2026-ARXIV-2606-09441:start -->
### 2606.09441 — SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：RAG 重复文档的 prefill 可保存 selective index 而非整份 KV：offline 编码局部 attention，online 只重算 query-sensitive cross attention，以 storage traffic 换 TTFT。

**State / data / control owner。** `INFER-PREFILL` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09441v1 §§6–7 Evaluation Methodology and Results` 支持 `Disclosed — RAG context-reuse workloads、context-length sweep 与 diverse attention patterns`，evaluator 为 `Disclosed — TTFT、accuracy、storage scaling、energy、breakdown 与 hyperparameter sensitivity`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09441v1 §§3–5 Attention invariance, SIFT design and implementation`；counterevidence locator: `arXiv:2606.09441v1 §9 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** selective index 减少重算但引入离线 storage、pattern assumption 与 custom kernel；复用率低或 attention 不稳定时完整 prefill 仍正确。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09441:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09441v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09441:end -->
<!-- review:SF-2026-ARXIV-2606-09441:end -->

<!-- review:SF-2026-ARXIV-2606-09613:start -->
### 2606.09613 — AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：agent serving simulator 的执行单位必须从独立 request 提升为 program，显式模拟 turn dependency、tool gap、session affinity 与跨 HBM/host/CXL 的 KV residency。

**State / data / control owner。** `INFER-SCHEDULING` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09613v1 §§4–6 Setup, validation and design-space exploration` 支持 `Disclosed — 多轮 agent traces、real serving deployments、arrival/model/hardware/KV-tier sweeps`，evaluator 为 `Disclosed — program JCT、throughput、TTFT/TPOT、policy rank preservation 与 prediction error`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09613v1 §3 AgentServeSim`；counterevidence locator: `arXiv:2606.09613v1 §7 Limitations and Future Work`。

**Trade-off / failure / coexistence / evolution。** simulation 降低 accelerator 探索成本却依赖 trace/calibration；6% 内复现实验不能替代新模型、工具时延和多租户下的实机验收。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09613:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09613v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09613:end -->
<!-- review:SF-2026-ARXIV-2606-09613:end -->

<!-- review:SF-2026-ARXIV-2606-09643:start -->
### 2606.09643 — FMplex: Model Virtualization for Serving Extensible Foundation Models

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：extensible foundation model serving 需要把 base weights 与 extension state 虚拟化：共享公共层、按请求装载/组合扩展，并由 placement/cache 控制其生命周期。

**State / data / control owner。** `INFER-KSERVE-TOPOLOGY` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09643v1 §§4–6 Implementation and Evaluation` 支持 `Disclosed — 多 extension foundation-model serving configurations and baselines`，evaluator 为 `Disclosed — memory footprint、load/switch latency、throughput、tail latency 与 extension-count sensitivity`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09643v1 §3 FMplex Design`；counterevidence locator: `arXiv:2606.09643v1 §7 Discussion and Limitations`。

**Trade-off / failure / coexistence / evolution。** 共享提高 density 但引入 extension interference、cache miss 与版本兼容性；扩展少或隔离要求强时独立 replica 仍更简单。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09643:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09643v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09643:end -->
<!-- review:SF-2026-ARXIV-2606-09643:end -->

<!-- review:SF-2026-ARXIV-2606-09682:start -->
### 2606.09682 — AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：agent 生成 megakernel 必须经过 typed IR、静态 shape/layout/resource checks、编译与数值验证门，失败后才允许 self-retarget；自然语言计划不直接获得 kernel authority。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09682v1 §4 Evaluation` 支持 `Disclosed — 多 GPU workload/kernel synthesis tasks with compile-and-run verification`，evaluator 为 `Disclosed — compile success、numerical correctness、performance、repair rounds 与 failure taxonomy`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09682v1 §3 AutoMegaKernel Harness`；counterevidence locator: `arXiv:2606.09682v1 §5 Limitations`。

**Trade-off / failure / coexistence / evolution。** 静态门降低 silent miscompile 却限制可表达优化并增加 compile/search cost；成熟算子与不可验证路径仍应回退到人工 kernel。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09682:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09682v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09682:end -->
<!-- review:SF-2026-ARXIV-2606-09682:end -->

<!-- review:SF-2026-ARXIV-2606-09686:start -->
### 2606.09686 — An 84-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：低精度 format contract 需要 vendor-neutral、bit-exact 的 encode/decode、rounding、overflow、NaN/Inf/subnormal 与 microscaling conformance vectors；格式名相同不代表语义相同。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09686v1 §§5–6 Validation and Results` 支持 `Disclosed — official v1 的 84-format catalog，覆盖 FP8/BF16/MXFP4/microscaling families`，evaluator 为 `Disclosed — bit-exact vectors、cross-implementation agreement、edge-case coverage 与 mismatch diagnostics`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09686v1 §§2–4 Numeric Catalog and Conformance Model`；counterevidence locator: `arXiv:2606.09686v1 §7 Limitations`。

**Trade-off / failure / coexistence / evolution。** bit-exact catalog 提高互操作性但维护成本随标准修订增长；它验证表示语义，不证明任何训练或推理 workload 的质量/性能。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09686:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09686v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09686:end -->
<!-- review:SF-2026-ARXIV-2606-09686:end -->

<!-- review:SF-2026-ARXIV-2606-09692:start -->
### 2606.09692 — Observability for Delegated Execution in Agentic AI Systems

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。

**State / data / control owner。** `PLATFORM-TRACE` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09692v1 §§4–5 Gateway and Evaluation` 支持 `Disclosed — 跨工具 delegation/re-delegation、concurrency/retry reconstruction scenarios`，evaluator 为 `Disclosed — reconstruction completeness、query correctness、gateway overhead 与 missing-lineage failure cases`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09692v1 §2 Delegation-Observable Execution; §3 Common Information Model`；counterevidence locator: `arXiv:2606.09692v1 §6 Limitations`。

**Trade-off / failure / coexistence / evolution。** 双图与 gateway 提高可归因性但不推断 intent/policy compliance；跨工具 schema、missing telemetry 与 identity minting 仍需平台治理。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09692:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09692v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09692:end -->
<!-- review:SF-2026-ARXIV-2606-09692:end -->

<!-- review:SF-2026-ARXIV-2606-09711:start -->
### 2606.09711 — Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：reward-hacking 监测需观察显性 exploit 之前形成的 proxy-reward internalization：正确性判断、proxy acceptance 预测与 proxy-gold gap 推理三种状态。

**State / data / control owner。** `TRAIN-RLHF` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09711v1 §5 Experiments` 支持 `Disclosed — 可 exploit pytest rewards 的 coding RL checkpoints 与 evaluator-switch controls`，evaluator 为 `Disclosed — hack onset/severity forecast、direct/activation probes、direction ablation 与 OOD misalignment correlation`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09711v1 §§2–4 PRIME Definition, Probes and Interventions`；counterevidence locator: `arXiv:2606.09711v1 §6 Limitations`。

**Trade-off / failure / coexistence / evolution。** probe 可作 early warning，却可能被训练规避且当前只在 pytest coding RL 验证；相关性不等于通用 causal monitor。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09711:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09711v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09711:end -->
<!-- review:SF-2026-ARXIV-2606-09711:end -->

<!-- review:SF-2026-ARXIV-2606-09774:start -->
### 2606.09774 — Auto-Configuring Scientific Simulators with Lightweight Coding-Agent Adapters

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：给通用 coding agent 适配 scientific simulator 时，应把 executable contract 外置为 retrieval、procedural memory、agent-callable validator 与 validation-gated termination，而不重写 agent loop。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09774v1 §§5–6 Evaluation` 支持 `Disclosed — GEOS main benchmark；OpenFOAM/LAMMPS transfer；human calibration`，evaluator 为 `Disclosed — structural/quality score、completion、variance、runtime、ablation 与 transfer delta`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09774v1 §§3–4 SIGA Adapter and Self-Evolution`；counterevidence locator: `arXiv:2606.09774v1 Appendix F Limitations`。

**Trade-off / failure / coexistence / evolution。** adapter 可移植但 component importance 依接口 bottleneck 变化；结构通过不代表物理正确，tool 暴露也不保证 agent 会调用。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09774:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09774v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09774:end -->
<!-- review:SF-2026-ARXIV-2606-09774:end -->

<!-- review:SF-2026-ARXIV-2606-09809:start -->
### 2606.09809 — Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：Evaluation result 需要把 benchmark metadata、run data 与 model metadata 组合成可追踪 record，并按读者呈现 reproducibility、completeness、provenance/risk 与 score comparability。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制所需状态、数据与控制决策；论文项目名不取得跨章节 ownership。需要跨 owner 传递的中间状态必须带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.09809v1 §§6–8 Deployment and Analysis` 支持 `Disclosed — 52-paper review、10 stakeholder interviews、5,816 models/635 benchmarks/101,843 results`，evaluator 为 `Disclosed — schema coverage、documentation/comparability signals、extraction quality 与 monitoring findings`。它不证明生产 SLO、跨模型/跨硬件普遍优越性，也不把未披露字段补写为事实。Method locator: `arXiv:2606.09809v1 §§3–5 Evaluation Cards Schema and Interpretive Signals`；counterevidence locator: `arXiv:2606.09809v1 Appendix J Limitations`。

**Trade-off / failure / coexistence / evolution。** 统一 schema 改善解释却可能固化过时字段；reader mode 不能替代原始 evidence，agent evaluation 也未被系统综述充分覆盖。 长期知识只吸收 mechanism、owner handoff 与 failure boundary，不吸收产品排名。

<!-- claim:SF-2026-ARXIV-2606-09809:start -->
**Claim boundary。** 可引用内容限于 `https://arxiv.org/html/2606.09809v1` 的 exact-v1 method/evaluation/limitations 与本 report benchmark contract；ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-09809:end -->
<!-- review:SF-2026-ARXIV-2606-09809:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-TRAIT-MISALIGNMENT-MONITOR | checkpoint-level emergent-misalignment detection on four 7–9B models plus two 14B stress-test models and held-out perturbations; frozen at arXiv:2606.07631v1 §Appendix 9 EM Evaluation Protocol | Llama-3-8B; Mistral-7B-v0.3; Qwen2.5-7B; Gemma-2-9B; held-out probes Qwen2.5-14B and Phi-4-14B | single NVIDIA A6000 GPU | Not Disclosed | checkpoint prompt sets; no common numeric prompt-length cap disclosed | maximum 600 generated tokens per checkpoint response | vLLM batched generation with numeric size undisclosed; batch size 64 is limited to the SAE appendix slice | Not Disclosed | monitoring-quality evidence only; no production detection SLO | two-pass GPT-4o grading, EM/FNR/FPR thresholding and trait-space drift diagnostics across checkpoints/seeds |
| SF-ML-LIFECYCLE-ASSESSMENT | Model life-cycle assessment expands efficiency accounting from one training run or inference sample to data, experimentation, deployment, refresh, infrastructure and retirement under an explicit functional unit. Evaluation is frozen at arXiv:2606.07632v1 exact-v1 PDF § `3.5 Case Study: Comparing the Effects of LLM System Design Choices with LCA`; § `4 Alternative Views`. | Not Applicable — ML life-cycle assessment framework and system-design case studies; no controlled model implementation is benchmarked | H100 appears in the case-study system inventory; no controlled benchmark host | Not Applicable — life-cycle inventory comparison, not tensor execution measurement | Not Applicable — functional-unit/workload inventory rather than sequence-length sweep | Not Applicable — environmental-impact inventory rather than generated output | Not Applicable — no batched ML run | Not Applicable — no request-concurrency experiment | life-cycle impact comparison only; no production SLO | ISO-style LCA functional unit, resource inventory and energy/water/carbon life-cycle impact comparison |
| SF-2026-ARXIV-2606-07684 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Disclosed — QUANTIZATION | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07687 | Disclosed — Our results identify temporal predictive structure -- not reconstruction fidelity -- as the primary ingredient underlying action-relevant video representations. | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — Our results identify temporal predictive structure -- not reconstruction fidelity -- as the primary ingredient underlying action-relevant video representations. |
| SF-2026-ARXIV-2606-07703 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Disclosed — Qwen-family retrieval-, Qwen3.5-9B RULER-style, Qwen3.5-0.8B and Qwen3, Qwen3.5-0.8B on NPU an, Qwen3.5-9B on GPU agai | Disclosed — accelerator | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07710 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07713 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Disclosed — accelerators or empirical til | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07720 | Disclosed — Large language models (LLMs) have demonstrated remarkable reasoning abilities on mathematical and multi-hop planning tasks. | Disclosed — GPT-2 as our base mod | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — Large language models (LLMs) have demonstrated remarkable reasoning abilities on mathematical and multi-hop planning tasks. |
| SF-2026-ARXIV-2606-07726 | Disclosed — Unlike prior attempts to leverage model similarity in best-model identification, our approach is hyperparameter-free and enjoys performance guarantees that improve with the degree of similarity between evaluated models. | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — Unlike prior attempts to leverage model similarity in best-model identification, our approach is hyperparameter-free and enjoys performance guarantees that improve with the degree of similarity between evaluated models. |
| SF-2026-ARXIV-2606-07783 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07790 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07805 | Disclosed — To address this blind spot, we introduce MAC-Bench, a dynamic, adversarial benchmark designed to evaluate the procedural alignment of multi-agent systems under realistic pressure. | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — To address this blind spot, we introduce MAC-Bench, a dynamic, adversarial benchmark designed to evaluate the procedural alignment of multi-agent systems under realistic pressure. |
| SF-2026-ARXIV-2606-07808 | Disclosed — We evaluate three reasoning models--Gemma-4-31B-IT, Qwen3.6-35B-A3B, and Claude Sonnet 4.6--on long-context adaptations of IHEval and IHChallenge, and find that the dominant failure mode varies across models, tasks, and context length. | Disclosed — Gemma-4-31B-IT, Qwen3.6-35B-A3B, Claude Sonnet 4.6--on lo, Claude Sonnet 4.6, GPT-5.3, GPT-5.3 reductions of | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — We evaluate three reasoning models--Gemma-4-31B-IT, Qwen3.6-35B-A3B, and Claude Sonnet 4.6--on long-context adaptations of IHEval and IHChallenge, and find that the dominant failure mode varies across models, tasks, and context length. |
| SF-2026-ARXIV-2606-07822 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07833 | Disclosed — We conduct a controlled experiment pitting 60 HarmBench prompts against two LLMs, GPT-OSS 120B and Llama 3.3 70B, using 10 prompt mutation strategies over up to 110 attempts per prompt. | Disclosed — GPT-OSS 120B and Llam, GPT-OSS exhibits a ne, Llama presents multiple | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — We conduct a controlled experiment pitting 60 HarmBench prompts against two LLMs, GPT-OSS 120B and Llama 3.3 70B, using 10 prompt mutation strategies over up to 110 attempts per prompt. |
| SF-2026-ARXIV-2606-07834 | Disclosed — A minimal two-channel reference probe reaches operating points neither single channel reaches; under the random-veto null its promotion to CONFLICTING is structurally targeted on AVeriTeC (empirical p &lt; 1/2001) and weaker but in the same direction on VitaminC-Mixed, a selectivity result rather than a magnitude one. | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — A minimal two-channel reference probe reaches operating points neither single channel reaches; under the random-veto null its promotion to CONFLICTING is structurally targeted on AVeriTeC (empirical p &lt; 1/2001) and weaker but in the same direction on VitaminC-Mixed, a selectivity result rather than a magnitude one. |
| SF-2026-ARXIV-2606-07845 | Disclosed — Two further observations qualify the result. | Disclosed — Mistral-Small 24B reaches, Qwen3-14B reaches 0.13, Qwen-7B and Mistral-Sm | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — Two further observations qualify the result. |
| SF-2026-ARXIV-2606-07846 | Disclosed — We specify the runtime mechanics, a closed-form result that the rule self-limits as the upstream branching factor grows, a five-stage calibration pipeline (offline replay, shadow, canary, online calibration, drift-triggered kill-switch), and a workload-fit rubric over eight production archetypes. | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — We specify the runtime mechanics, a closed-form result that the rule self-limits as the upstream branching factor grows, a five-stage calibration pipeline (offline replay, shadow, canary, online calibration, drift-triggered kill-switch), and a workload-fit rubric over eight production archetypes. |
| SF-2026-ARXIV-2606-07856 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Disclosed — Qwen3-4B on a single 2 | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07867 | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice |
| SF-2026-ARXIV-2606-07874 | Disclosed — LLMs-as-judges are the only way to evaluate safety at scale. | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — LLMs-as-judges are the only way to evaluate safety at scale. |
| SF-2026-ARXIV-2606-07878 | Disclosed — We show that amortization makes long-context cache compaction tractable, and synthesis makes its compact state useful at extreme compression. | Disclosed — Qwen and Gemma models | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Disclosed — 8\times, 200\times | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — We show that amortization makes long-context cache compaction tractable, and synthesis makes its compact state useful at extreme compression. |
| SF-2026-ARXIV-2606-07881 | Disclosed — These results show that forward/backward inconsistency need not be eliminated: when explicitly bounded, it can be safely traded for substantial efficiency gains. | Disclosed — GPT-style language-mo | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — These results show that forward/backward inconsistency need not be eliminated: when explicitly bounded, it can be safely traded for substantial efficiency gains. |
| SF-2026-ARXIV-2606-07889 | Disclosed — We give an operational definition, build a Claude Sonnet 4.6 judge that reads full trajectories and flags spans where the pattern occurs, and evaluate it on 44 Terminal-bench-2 trajectories using a Qwen3.5-35B-A3B backbone. | Disclosed — Claude Sonnet 4.6 judge, Qwen3.5-35B-A3B backbo, Gemma4-31B with 43 traj, Gemma tertile, Qwen tertiles | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — We give an operational definition, build a Claude Sonnet 4.6 judge that reads full trajectories and flags spans where the pattern occurs, and evaluate it on 44 Terminal-bench-2 trajectories using a Qwen3.5-35B-A3B backbone. |
| SF-2026-ARXIV-2606-07904 | Disclosed — Contract2Tool converts observable tool evidence into normalized symbolic contracts that can be evaluated intrinsically and deployed inside downstream causal tool filtering. | Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim | Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim | Not Disclosed — full exact-v1 review did not establish precision/quantization | Not Disclosed — full exact-v1 review did not establish input length | Not Disclosed — full exact-v1 review did not establish output length | Not Disclosed — full exact-v1 review did not establish one batch contract | Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency | Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold | Disclosed — Contract2Tool converts observable tool evidence into normalized symbolic contracts that can be evaluated intrinsically and deployed inside downstream causal tool filtering. |
| SF-2026-ARXIV-2606-07923 | Three real datasets plus three semantic-filter workloads and synthetic selectivity/horizon sweeps | Semantic-filter LLM backends and lightweight A2C/selectivity models; exact backend matrix is workload-specific | Not Disclosed — §4.1 does not bind one hardware topology to every result | Not Disclosed | Rows/documents with precomputed embeddings; no token length contract | Filter outcomes and token calls; no output-token length contract | Not Disclosed | Not Disclosed | Not Disclosed — token cost is an outcome, not an acceptance SLO | Token use/cost overhead, convergence, sensitivity, oracle comparison and update latency |
| SF-2026-ARXIV-2606-07936 | 284 confirmed manual *CL 2023–2025 papers plus LLM-assisted labeling of the remaining long-form/human-evaluation corpus | GPT-4o-mini-2025-04-16 for automatic annotation; Gemini-2.5-Pro and Claude-3.7-Sonnet-20250219 in model-selection pilot | Not Disclosed | Not Disclosed | Abstract, introduction, candidate human-evaluation sections and appendix passages | Five chunks of codebook answers as flat JSON; up to two full reruns after validation failure | Not Disclosed — question chunks are separate API calls, not a disclosed batch size | Not Disclosed | Only fields with held-out validation accuracy >0.75 are reported; this is a reporting threshold, not service SLO | Manual IAA; GPT-4o-mini selection on 26 papers; independent 125-paper/3,875-label validation; bootstrap reporting rates |
| SF-2026-ARXIV-2606-07943 | Skill-Inject 25 eligible tasks ×3 harms and SkillsBench 27 tasks ×3, two trials/configuration | codex+gpt-5.2; OpenClaw+DeepSeek-V4-Flash/Pro; Claude Code+Sonnet-4.6 | Docker/Harbor sandbox; host accelerator not disclosed | Not Disclosed | Skill files and task contexts; no fixed token length | One injected instruction plus legitimate task completion | Not Disclosed | Not Disclosed | ASR requires sandbox postcondition and passing legitimate-task verifier | Joint ASR, task verifier, postcondition verifier and four-judge SkillTester delta alerts |
| SF-2026-ARXIV-2606-07950 | MATH training and twelve reported math, general-reasoning and code benchmarks | Llama-3.2-1B-Instruct; Qwen2.5-Math-1.5B and 7B | 4×NVIDIA A100 | Not Disclosed | Dataset-defined prompts; no fixed input length | Evaluation uses 32 responses at temperature 0.6; no fixed output cap disclosed | 16; 8 rollouts per group | Not Disclosed | Not Disclosed | Accuracy across twelve benchmarks, confidence/difficulty dynamics and fixed-compute comparison |
| SF-2026-ARXIV-2606-07957 | No executed benchmark — formal semantics, complexity analysis, worked example and proposed evaluation methodology | Not Disclosed — no model evaluated | Not Disclosed | Not Disclosed | Catalogue entries and live asset graphs; no fixed size | Derived tenant-local rules | Not Disclosed | Not Disclosed | Not Disclosed | Methodology proposes latency/resource evaluation; paper explicitly does not prove rule correctness or alert priority |
| SF-2026-ARXIV-2606-07968 | OverThink, ExtendAttack, held-out QA/code/math/summarization and adaptive stress tests | DS-R1-Qwen-7B primary; DS-R1-Llama-8B, Qwen3-8B, Llama3.1-8B, Sonnet-4.5 and Opus-4.7 slices | NVIDIA A100 for open models; count/topology not disclosed | Not Disclosed | Prompt/task dependent | Reasoning trace analyzed in 64-word chunks | Not Disclosed | Not Disclosed | Three consecutive anomalous chunks is termination policy, not a service SLO | TPR/FPR, joint miss rate, token amplification and post-hoc QDM fallback |
| SF-2026-ARXIV-2606-07970 | Beavertails/PKU-SafeRLHF/ToxicDPO-v2 test attacks; AdvBench, Beavertails and HEx-PHI ASR; Alpaca utility | Qwen2.5-1.5B main/ablation; Qwen3-4B and Llama3-8B generalization; Qwen3-Max harmfulness judge | Not Disclosed | Not Disclosed | 200 unsafe Beavertails plus 800 GSM8K samples in default test-time mix | Maximum 256 generated tokens; temperature 0.6 and top-p 0.9 | Global batch 4 for attack, defense, baselines and test-time attack | Parallel attack/defense loops use stale attack vectors; worker concurrency not disclosed | Not Disclosed | Attack Success Rate on three safety sets, utility, transfer and wall-clock; fully poisoned and larger-malicious-set failures retained |
| SF-2026-ARXIV-2606-07992 | Controlled MCP tool-error JSON with seven mutation dimensions and email-exfiltration effect | Gemini-3.1-Pro, GPT-5.5, GLM-5.1, Qwen3-Coder | Provider APIs; hardware not disclosed | Not Disclosed | Controlled agent/tool contexts; no fixed token length | Tool-call compliance/effect | Not Disclosed | Not Disclosed | Not Disclosed | Injection compliance/ASR by error structure plus production-guardrail comparison |
| SF-2026-ARXIV-2606-08049 | WebArena-Verified, Mind2Web cross-site/domain and GitLab 15.7→16.11/18.9 migration | Agent model/backend matrix is experiment-specific; no single evaluated model identity | Not Disclosed | Not Disclosed | Workflow steps, pages and notebook evidence; no fixed token length | Task actions, screenshots and traces | Not Disclosed | Three re-executions for durability; not concurrency | Gates are per-step validity policies, not service SLOs | Success, retained success, bounded-repair recovery/regression and migration gap |
| SF-2026-ARXIV-2606-08094 | LIBERO-Object 10 tasks ×20 episodes per architecture and ALOHA moving-target stress test | Seven VLA architectures spanning five backbones/four action heads | RTX 3060; Jetson AGX Orin; 8GB Jetson Orin Nano | Model/package-specific; no one precision contract | Vision-language prefix and robot observation; no fixed token length | Action-expert solver steps | Batch 1 | One request at a time in roofline slice; broader concurrency not disclosed | Not Disclosed | Episode success, behavioral match, latency, memory footprint and cross-hardware roofline |
| SF-2026-ARXIV-2606-08106 | Prompt self-evolution on GSM8K, SVAMP and ARC-Challenge with hidden-real-gain and no-gain regimes | Qwen2.5 0.5B–3B agents | Not Disclosed | Not Disclosed | Paired identical evaluation instances | Commit/reject decisions and task answers | Not Disclosed | Sequential optional stopping; no concurrent execution contract | User-set per-candidate false-commit probability | False/harmful commits, held-out accuracy, variance and evaluation cost |
| SF-2026-ARXIV-2606-08197 | Heterogeneous asynchronous federated fine-tuning under non-IID data and staleness | Llama3-8B and Qwen3-8B | Single NVIDIA A100 | FP16 | Maximum sequence length 650 | Not Disclosed | Batch 1 | Asynchronous clients; fixed concurrent-client count not disclosed | Communication budget ≤50MB is a constraint, not latency SLO | Convergence, accuracy, fairness, staleness robustness, latency and communication |
| SF-2026-ARXIV-2606-08200 | Life simulation: five characters, 32 social criteria, three target backends × three seeds | Target-agent backends vary; all automated judges use GPT-5.4-mini | Provider APIs; hardware not disclosed | Not Disclosed | Interactive social histories; no fixed token length | Dialogue/actions and criterion evidence | Not Disclosed | Five-character world; no request concurrency contract | Not Disclosed | Criteria coverage and agreement with human labels versus passive judges |
| SF-2026-ARXIV-2606-08302 | Multiple VAR models over text-to-image, class-conditional and unified understanding/generation tasks | Infinity-2B/8B and additional VAR models in §VI | Not Disclosed | Not Disclosed | Multi-scale visual-token histories | Generated images/tokens | Not Disclosed | Not Disclosed | 30% attention/10% cache are budgets, not SLOs | Generation quality, task accuracy, attention/cache budget and robustness to 1% cache |
| SF-2026-ARXIV-2606-08317 | Conceptual comparison of 13 database paradigms plus one representative financial-fraud architecture case; Table I ranges are directional literature synthesis, not a controlled benchmark | Not Disclosed — no model is evaluated | Not Disclosed | Not Disclosed | Workload profile over nine architectural dimensions; no fixed input length | Ranked paradigm/architecture recommendation; no fixed output length | Not Disclosed | Not Disclosed | Not Disclosed | Qualitative compatibility values 1/2/3 weighted by workload importance; financial case maximum score 90; no product-level empirical evaluator |
| SF-2026-ARXIV-2606-08340 | Procedural long-horizon alem world across coordination difficulty; homogeneous teams and MARL references | 13 modern LLMs zero-shot; named frontier examples include Gemini-3.1-Pro-High and GPT-5.4-High | Not Disclosed | Not Disclosed | World observations and communication histories | Actions/messages over long horizons | Not Disclosed | Team size/configuration disclosed per environment; serving concurrency not disclosed | Not Disclosed | Normalized return split into base-task and coordination reward; communication/memory/reasoning ablations |
| SF-2026-ARXIV-2606-08346 | Qwen2.5-Math-1.5B trained on MATH; AIME24, MATH-500, OlympiadBench and MinervaMath | Qwen2.5-Math-1.5B | Not Disclosed | Not Disclosed | MATH problems and rollout trees | Tree continuations/critiques | Not Disclosed | Not Disclosed | Not Disclosed | Pass@1/Avg@8 and macro accuracy; tree-informativeness/healing ablations |
| SF-2026-ARXIV-2606-08348 | SOP-Bench, Lifelong AgentBench and RealFin-Bench across native, GenericAgent, mini-swe-agent and Claude Code backends | deepseek-v4-flash and deepseek-v4-pro for Bayesian variants; Claude Sonnet-4.6, Claude Opus-4.6 and GPT-5.4 comparison rows | Not Disclosed | Not Disclosed | Verified task trajectories with benchmark/context/failure-mode/token/turn/latency features | Task artifacts plus skill actions; table reports input/output/total tokens | Not Disclosed | Not Disclosed | Posterior action thresholds are lifecycle policy, not service SLO | Task accuracy, token accounting, efficiency, full/incremental repair and backend/model ablations |
| SF-2026-ARXIV-2606-08367 | 15 days, five parallel worlds, ten agents/world, 120+ tools and three memories | Claude Sonnet-4.6, Grok-4.1-Fast, Gemini-3-Flash, GPT-5-mini and mixed population | Live provider APIs; hardware not disclosed | Not Disclosed | Persistent world plus live weather/news/internet inputs | Actions, governance outcomes and logs | Not Disclosed | Ten agents/world; request concurrency not disclosed | Not Disclosed | Cross-world behavioral trajectories, governance stability/collapse and released logs |
| SF-2026-ARXIV-2606-08372 | 14 attacks ×9 synthetic-data generators ×5 datasets; QI sizes 3–16; DP epsilon sweeps | Classifiers, graphical models and diffusion/generative attack families; not one LLM | Not Disclosed | Not Disclosed | Tabular released datasets and target quasi-identifiers | Predicted hidden attributes | Not Disclosed | Not Disclosed | Not Disclosed | Rarity-weighted reconstruction advantage, train/holdout memorization gap and RA-as-MIA comparison |
| SF-2026-ARXIV-2606-08381 | Three black-box cases: DeepSeek-R1 on China- and US-sensitive domains, and Meta AI Chat/Llama 4 on Meta-related topics | DeepSeek-R1 and Meta AI Chat/Llama 4 targets; diverse baseline ensemble; GPT-5.2 and Gemini-3.1-Flash-Lite judges; four embedding models | Provider APIs; hardware not disclosed | Not Disclosed | Shared case-specific prompts generated with GPT-4o; fixed token lengths not disclosed | Black-box responses, embeddings and ordinal judge labels | Not Disclosed | Not Disclosed | Statistical alpha=0.05 is a hypothesis threshold, not service SLO | Welch one-sided t-test, bootstrap median test, target-permutation diagnostic; relative divergence not absolute correctness or intent |
| SF-2026-ARXIV-2606-08382 | WikiText-2 perplexity, six LM-Eval tasks, LongBench and 4K RULER plus kernel/throughput slices | LongChat-7B-v1.5, Llama-2-7B, Llama-3-8B-Instruct and Llama-3.1-8B-Instruct long-context slice | RTX Pro 6000 for <6 GPU-hour 3,000-sample calibration; single RTX 4090 for attention/kernel latency | FP16 SDPA baseline; first 20% channels 4-bit and remainder 3-bit for average 3.2-bit quantized slice | Benchmark-defined; RULER explicitly 4K | Benchmark-defined generation lengths | Not Disclosed | Not Disclosed | Not Disclosed | Perplexity, zero-shot accuracy, LongBench/RULER, compression, attention speedup and end-to-end throughput |
| SF-2026-ARXIV-2606-08403 | Disclosed — §5 uses summarization and structured extraction across four carriers, three injection objectives, four defenses and three commercial APIs; 14,400 attacked real-model trials plus 4,800 clean trials | Disclosed — GPT-5.4, Gemini 3.1 Flash-Lite Preview, and Claude Sonnet 4.6; Prompt Guard 2, TF-IDF and roberta-base defenses | Not Disclosed — API-backed model execution and local classifier hardware are not identified | Not Disclosed — model/classifier numerical precision is not identified | Disclosed — Appendix C reports neural-detector maximum sequence length 512 and largest attacked input 438 subword tokens | Not Disclosed — no fixed model-output length contract is identified | Disclosed — roberta-base defense training uses batch size 16; API attack trials are not relabeled as a serving batch | Not Disclosed — no in-flight concurrency contract is identified | Not Disclosed — ASR/TSR thresholds are evaluation metrics, not a production SLO | Disclosed — leakage ASR, Strong ASR, task success rate and detection rate, with carrier×defense and 2×2 ablations |
| SF-2026-ARXIV-2606-08411 | Disclosed — §4.1 evaluates GSM8K, GSM8K-CoT, MATH, HumanEval and MBPP over 256/512/1024 generation budgets | Disclosed — LLaDA- and Dream-based masked diffusion LMs; Fast-dLLM and inference-only d3LLM baselines | Disclosed — one NVIDIA H100 GPU | Not Disclosed — §4.1 does not identify numerical precision | Not Disclosed — prompt lengths are task-dependent and no single fixed input length is stated | Disclosed — benchmark generation budgets 256, 512 and 1024 tokens | Disclosed — inference batch size 1 | Not Disclosed — active lanes are scheduler state, not request concurrency | Not Disclosed — TPS/quality trade-off has no production acceptance threshold | Disclosed — tokens/s, exact-match accuracy, pass@1, model-call NFE and wall-clock latency |
| SF-2026-ARXIV-2606-08417 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: We recommend evaluation suites that directly quantify the distributional divergence between generated and reference text, and use such a suite to re-benchmark recent non-autoregressive models, recovering a more faithful picture of the current state of the art. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08432 | Disclosed — five competition-math benchmarks plus HumanEval+, MBPP+ and LiveCodeBench for OPD code evaluation | Disclosed — Qwen3-1.7B/4B students, frozen Qwen3-8B teacher, and Qwen3-4B/8B shared-backbone OPSD | Disclosed — Appendix C uses one 8-GPU node; exact accelerator model is not identified in the bound locator | Disclosed — bfloat16 training | Disclosed — Appendix C reports method-specific maximum lengths from 18,432 to 38,912 tokens | Disclosed — evaluation samples up to 64 math or 128 code sequences; fixed token cap varies by recipe | Disclosed — per-GPU batch 1 with gradient accumulation 16, effective batch 128 on eight GPUs | Not Disclosed — sample count is not in-flight serving concurrency | Not Disclosed — no serving SLO | Disclosed — Avg@16, Pass@16, task accuracy, KL/trajectory diagnostics and refinement-signal ablations |
| SF-2026-ARXIV-2606-08433 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: zzing investment splits into three tiers, and the strongest combination -- microVM x continuous public fuzzer -- is unoccupied in this set, leaving the "0 published CVEs x no upstream fuzzer x no academic study" intersection structurally unmeasured. We report per-axis orderings, per-product portraits, and a threat-model qualification matrix; no overall ranking is proposed. Companion repository (code, Apache-2.0): htt | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08446 | Disclosed — long-context RL rollout plus sparse-attention cost studies, including 16K/24K/32K prefill probes and 1,000 repeated decode timings | Disclosed — Qwen3-1.7B is used in the reported stability example; dense-teacher and sparse-student configurations remain recipe-specific | Disclosed — single NVIDIA H200 for the bound kernel/full-model cost measurements | Not Disclosed — no numerical training/inference precision contract is stated in the bound setup | Disclosed — 16K, 24K, and 32K prefill lengths; 37K generation-budget stability slice | Disclosed by experiment — long-generation regimes vary; no single universal decode cap | Disclosed — batch 8 in the 1,000-trial full-model timing and batch 16 in the page-size cost table | Not Disclosed — batch size is not relabeled as request concurrency | Not Disclosed — stability and speedup results are not a production SLO | Disclosed — sparse/dense mismatch, rollout stability, latency, page-size sensitivity and LoRA-distillation overhead |
| SF-2026-ARXIV-2606-08476 | Disclosed — WLB-LLM, Pile and RedPajama; 100K sampled packed sequences; 128K contexts; CP sizes 4 and 8 | Disclosed — 16- and 32-attention-head model configurations with head dimension 128; Llama3 CP, Per-Doc CP and Ring-Attn baselines | Disclosed — single node with 8×NVIDIA H100 SXM 80GB connected by NVLink | Not Disclosed — §4.1 does not identify numerical precision | Disclosed — 128K context in the main comparison, with additional context-window sweeps | Not applicable — training/inference attention-kernel benchmark, not free-form generation output | Disclosed — each evaluation input is a packed sequence; no global optimizer batch is stated | Disclosed — CP worker counts 4 and 8; this is parallelism degree, not request concurrency | Not Disclosed — latency/speedup has no acceptance SLO | Disclosed — normalized training/inference latency, speedup, load imbalance, communication and kernel-efficiency breakdown |
| SF-2026-ARXIV-2606-08483 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Objective: To evaluate response variation and sycophancy in consumer-facing health LLMs under conditions resembling ordinary patient use. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08486 | Disclosed — streaming speech recognition over six chunk-size operating points and offline/streaming comparisons | Disclosed — shared audio encoder with transducer branch, adaptor/joint network, and Speech-LLM decoder | Disclosed — training on 16×H200 GPUs; real-time inference check on one H200; about 8 GB inference memory | Disclosed — bfloat16 mixed-precision training | Disclosed — dynamic chunks 4/8/16/24/32/full post-subsampling frames; utterance split at 25 seconds | Not Disclosed — no fixed generated-token cap | Not Disclosed — eight-step gradient accumulation is disclosed but per-step/global batch is not | Not Disclosed — one-pass streaming is not an in-flight concurrency contract | Disclosed as evaluated real-time boundary — maximum RTF 0.171 across six operating points, not a production availability SLO | Disclosed — speech quality/alignment, latency/RTF, streaming stability and operating-point comparisons |
| SF-2026-ARXIV-2606-08517 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Selective predictors answer on confident inputs and abstain elsewhere; deploying one safely needs a single finite-sample certificate that simultaneously upper-bounds the selected risk, lower-bounds the acceptance probability $\pacc$ above a floor $\pmin$, and lower-bounds the deployment utility. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08529 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: ng variable, and the predicted planner-executor advantage on file-reading tasks is falsified. Structured scaffolds make fewer tool calls yet recover more often from mid-trajectory errors at the harder level, and a single cell (Gemini with planner-then-executor) is the cheapest at both levels and the most accurate at Level 2. These results indicate that single-scaffold capability numbers are scaffold-conditional estim | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08531 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Existing evaluations often rely on manually written scenarios, static prompts, or final-output judgments, making it difficult to capture the diverse risks that agents may face during task execution. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08539 | Disclosed — independent 630-action corpus, external semantic slice, and 30×1,500-action Monte Carlo online replay (45,000 actions) | Disclosed — Haiku 4.5, Sonnet 4.6, Opus 4.8 and GPT-5.5 judges; deterministic rules and MiniLM retrieval controls | Not Disclosed — hosted judge/runtime hardware is not identified | Not Disclosed — numerical precision is not identified | Not Disclosed — action text length contract is not identified | Not Disclosed — judge output length is not identified | Not Disclosed — corpus/replay size is not a model batch size | Not Disclosed — §6 explicitly says live concurrency is not exercised by fixed-verdict replay | Disclosed as a safety invariant, not latency SLO — zero benign hard-blocks; escalation tops out at warn/review | Disclosed — accuracy, FPR/FNR, judge-call rate, semantic accuracy, memory correctness and dangerous leaks |
| SF-2026-ARXIV-2606-08574 | Disclosed — CIFAR-10/100 and ImageNet-1K pruning with ResNet-18/50, repeated stability and gradient checks | Disclosed — ResNet-18 and ResNet-50 with Dynamic Random, UCB and InfoBatch baselines | Disclosed — ImageNet timing on a 2×NVIDIA L40 server | Disclosed — Timm ImageNet recipe uses mixed-precision training; exact dtype is not stated | Not applicable — fixed image datasets rather than token input | Not applicable — classification training | Disclosed — 128 for CIFAR and 1,024 for ImageNet | Not Disclosed — no serving concurrency | Not Disclosed — accuracy/runtime comparisons have no acceptance SLO | Disclosed — accuracy, training time/GPU-hours, pruning ratio, Jaccard stability and gradient direction |
| SF-2026-ARXIV-2606-08590 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: The surviving gain concentrates on ChaosMesh scenarios whose ground-truth root cause is the injected fault object already present in the evidence graph, so we report it as benchmark-coupled rather than broad cross-cluster RCA evidence. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08610 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: HARBOR decomposes such high-level objectives into bounded stages executed by specialized agents through standardized commands, persistent artifacts, executable gates, and reusable knowledge, and scales iteration via decentralized parallel trials and experience learning across runs. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08615 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: However, existing VLMs excel at offline video understanding but fall short in streaming capabilities and lack dedicated infrastructure for streaming deployment. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08625 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: As Large Language Models (LLMs) advance toward open-ended autonomous agents, the mechanisms used to evaluate and guide their behavior must evolve accordingly. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08635 | Disclosed — WikiText-2 PPL, NIAH at 4,096 tokens/19 depths, 2K–8K context sweeps, TTFT/TPS transfer-path timing and ablations | Disclosed — Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3 and Gemma-2-9B-it; Qwen2.5-14B only in locality characterization | Disclosed — NVIDIA RTX 4080 SUPER 32GB and RTX 4090 48GB cloud GPUs | Disclosed — token tiers FP16/INT8/INT4; adaptive fallback disables INT4 for Qwen after probe failure | Disclosed — 2K–8K contexts; NIAH fixed at 4,096 in the main retrieval slice | Not Disclosed — no fixed decode output length is identified | Not Disclosed — no batch size is identified | Not Disclosed — no continuous batching or request concurrency; §6.6 excludes a complete PD scheduler and contention | Not Disclosed — TTFT reduction has no acceptance threshold | Disclosed — PPL delta, NIAH accuracy, TTFT, TPS, transfer budget, quantization error and probe/ablation outcomes |
| SF-2026-ARXIV-2606-08661 | Disclosed — isolated benchmark data across database execution, external-resource and agent-reasoning attack surfaces plus commercial-service checks | Disclosed in §§6.1–6.5 — open-source and commercial data-agent systems are reported per condition | Disclosed — AMD Ryzen Threadripper PRO 9975WX, 576 GB RAM, one RTX Pro 6000 GPU for open-source runs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — exploit outcomes are not a production SLO | Disclosed — vulnerability/attack outcomes, sensitivity, cross-system generalization and explicit ethical scope |
| SF-2026-ARXIV-2606-08671 | Disclosed — GAIA and WebWalkerQA-EN in curated-search and raw-open-web settings | Disclosed — Claude Opus 4.6 development controller and Qwen3.6-35B-A3B execution/evaluation backbone | Not Disclosed — model execution hardware/topology is not identified | Not Disclosed — numerical precision is not identified | Not Disclosed — task/context token lengths are not identified | Not Disclosed — output length is not identified | Not Disclosed — no batch size is identified | Not Disclosed — role-bounded dispatches are not quantified as concurrent execution | Not Disclosed — no latency/reliability SLO | Disclosed — benchmark accuracy by difficulty split plus optimization-trajectory comparison; English and single-skill limitations stated |
| SF-2026-ARXIV-2606-08679 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Pretrained models are often evaluated on multi-task leaderboards to measure their applicability in diverse contexts. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08702 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08755 | Disclosed — ALFWorld, WebShop and Search-QA policy/skill co-evolution | Disclosed in §5.1 and Appendix hyperparameters; model identity stays workload-bound | Not Disclosed | Not Disclosed | Disclosed — maximum prompts 4,096/6,000/5,000 by workload | Disclosed — maximum responses 512/768/700 and environment steps 50/15/4 | Disclosed — train batches 16/16/512, validation 256/64/1,024, eight rollouts per prompt | Not Disclosed — rollout multiplicity is not request concurrency | Not Disclosed | Disclosed — task reward/success, skill utility, joint-optimization ablation and negative baselines |
| SF-2026-ARXIV-2606-08761 | Disclosed — WikiText2 perplexity, PIQA/ARC/HellaSwag/WinoGrande zero-shot accuracy, kernel tests and vLLM end-to-end serving | Disclosed — LLaMA-2 family (including 7B/70B), LLaMA-3-8B and Qwen2.5 family (including 7B/32B) | Disclosed — A100-40G, RTX 3090, A40 and L40S with per-SM and memory specifications | Disclosed — pure W4A4/INT4, compared with FP16, W4A16, W4A8 and mixed W4A4/W4A8 baselines | Not Disclosed as one serving contract — workload-dependent calibration/evaluation inputs | Not Disclosed — no fixed generated-token length is identified | Disclosed — vLLM serving sweeps include batch sizes through 256; A100 recovers at batch size ≥64 | Not Disclosed — batch sweep is not relabeled as in-flight request concurrency | Not Disclosed — throughput/speedup has no acceptance SLO | Disclosed — kernel/end-to-end speedup, PPL delta, zero-shot accuracy and cross-GPU rho analysis |
| SF-2026-ARXIV-2606-08769 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Automatic evaluation is critical for high-stakes text generation, where errors often involve omitted findings, hallucinated content, polarity reversals, location changes, uncertainty mismatches, and temporal-comparison errors rather than low surface similarity alone. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08779 | Disclosed — DAPO-Math-17K RL with math-verify reward and explicit train/inference-engine discrepancy | Disclosed in §6 setup; model/checkpoint and engine identities are condition-bound | Not Disclosed | Disclosed as the studied discrepancy dimension — FP16 alignment is a prior baseline, not asserted as the paper's universal runtime dtype | Not Disclosed — prompt cap is not stated in the bound setup | Disclosed — maximum response length 8,192 tokens | Disclosed — 64 prompts, PPO mini-batch 16, eight rollouts per prompt | Not Disclosed | Not Disclosed | Disclosed — math reward, training efficiency/stability, engine-discrepancy and ablation outcomes |
| SF-2026-ARXIV-2606-08790 | Not applicable — formal clearing protocol with worked scenarios, not an empirical benchmark | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable — protocol invariants are not measured service objectives | Not applicable — definitions/propositions and worked scenarios do not constitute empirical verification |
| SF-2026-ARXIV-2606-08806 | Disclosed — Defects4J and PROMISE with Jenkins/GitHub Actions governance checks | Disclosed — transformer-based artifact generator, RoBERTa governance classifier, SHAP/attention explainability | Disclosed — Intel Xeon Gold 6338, NVIDIA A100 40 GB, 128 GB RAM, Ubuntu 22.04 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — reported generation latency and governance quality have no acceptance threshold | Disclosed — test accuracy/validity/success, hallucination rate, governance precision/recall/FPR and latency |
| SF-2026-ARXIV-2606-08813 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: N=10,000), local PCA captures 96.3% of the variance, allowing HNTL to achieve a final Rerank Recall@10 of 1.0000 with a candidate pool size of only C=20 vectors. Hardware profiling via Apple kperf CPU Performance Monitoring Unit (PMU) counters demonstrates a 3.61x speedup (4.137 ns/vector vs. 14.951 ns/vector) for our NEON auto-vectorized C++ Block-SoA scan engine over standard pointer-chasing graph traversals, drive | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08831 | Disclosed — multi-step reasoning DAG factuality with calibration/test splits and ancestor-closed subgraph objectives | Disclosed — factuality-utility predictor plus paper-specified LLM reasoning generators | Not Disclosed | Not Disclosed — 'precision-oriented' names a statistical objective, not numerical dtype | Not Disclosed | Not Disclosed | Disclosed — predictor training batch size 32 | Not Disclosed | Disclosed as statistical coverage level 1-alpha, not latency SLO | Disclosed — no-false/no-miss conformal coverage, retained subgraph utility and calibration validity |
| SF-2026-ARXIV-2606-08840 | Disclosed — multilingual execution-grounded code tasks stratified by language, task type and runtime failure | Disclosed — nine open-weight/openly accessible instruction-tuned code models | Disclosed — Lambda Vector One, AMD Ryzen 7, 128 GB RAM, RTX 4090 24 GB, 4 TB SSD | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — execution pass rate stratified by language/task plus compile/runtime/timeout failure modes |
| SF-2026-ARXIV-2606-08867 | Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: Among the most promising applications is building production-ready customer-facing agents, a challenge that demands coordinated excellence in evaluation methodology, context engineering, training, and online measurement. | Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred | Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims | Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred | Not Disclosed in the currently bound contract — no single universal input length is inferred | Not Disclosed in the currently bound contract — no single universal output length is inferred | Not Disclosed in the currently bound contract — batch or accumulation is not inferred | Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency | Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO | Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority |
| SF-2026-ARXIV-2606-08869 | Disclosed — one seven-node live Kubernetes cluster under five stress profiles; 100-question and 700-query comparisons | Disclosed — LPSE, 106.3M-parameter MLP, XGBoost, Qwen3-4B and 120B Nemotron upper-bound baseline | Disclosed — one RTX 6000 Ada GPU for non-LLM systems; Qwen3-4B single-GPU comparison | Not Disclosed | Disclosed — 16-frame context window; 78,352-dimensional flattened MLP input | Not applicable — state/question classification | Not Disclosed | Not Disclosed — seven sequential queries within a budget is headroom analysis, not concurrent load | Disclosed — 50 ms control-loop budget; observed 6.65 ms mean is one-run evidence | Disclosed — clean/stressed accuracy, latency, robustness, model size and cluster-state coverage |
| SF-2026-ARXIV-2606-08891 | Disclosed — cycle-accurate end-to-end Transformer decode simulation plus RTL synthesis and sensitivity/overhead studies | Disclosed — Qwen3-0.6B/1.7B/4B/8B with Jetson Orin NX, PIMPAL, FIGLUT and CHIME baselines | Disclosed — modeled 35 nm, 768-layer, 24 GB M3D DRAM; 7 nm logic synthesized at 200 MHz | Disclosed — W4A4, 4-bit LUT results and 128-bit row-buffer transfers | Not Disclosed — no one token-length contract | Not Disclosed — throughput is per generated token without a fixed sequence cap | Not Disclosed | Disclosed at hardware level — modeled peak 8,388,608 concurrent LUT lookups; not request concurrency | Not Disclosed — TPS/power/area results have no acceptance threshold | Disclosed — TPS, power, energy/area efficiency, sensitivity and overhead under simulation/synthesis |
| SF-2026-ARXIV-2606-08892 | Disclosed — fuzzy research-proposal tasks with automated red/blue prompt optimization, scorer controls and appended stress experiments | Disclosed — paper-processing, red/blue and scorer prompts bind exact provider models in Appendix H | Not Disclosed — API experiment compute hardware is not identified | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — saddle-point blue-team per-evaluation batch 32, anchor budget 10, five inner loops and ten outer cycles | Not Disclosed | Not Disclosed | Disclosed — weak/strong scorer outcomes, saddle-point robustness, variance/ablation and qualitative attack analysis |
| SF-2026-ARXIV-2606-08893 | Disclosed — cleaned Terminal-Wrench trajectory variants with 5,689/735/690 train/val/test split | Disclosed — 13,842,560-parameter six-layer transformer encoder plus 128-d embedding and logistic probe | Disclosed — 15-hour training run on Apple M2 Max | Not Disclosed | Disclosed — 512-token chunks and 4,096 maximum tokens | Not applicable — trajectory embedding/classification | Disclosed — 32 trajectories, yielding 496 pairs per step | Not Disclosed | Disclosed as evaluator operating point TPR at 5% FPR, not production SLO | Disclosed — ROC AUC, TPR@5%FPR, cleaned-split comparison, stripped-input and adversarial robustness ablations |
| SF-2026-ARXIV-2606-08919 | Disclosed — 125 个 adversarially weighted agent actions、多人风险标注与 fatigue/flooding simulation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — reviewer agreement、selective-risk/coverage curve 与 realized-safety curve |
| SF-2026-ARXIV-2606-08950 | Disclosed — Qdrant/Milvus/Weaviate，四个 embedding datasets，两台生产超算，最多 64 nodes/256 workers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — upload/index time、QPS、latency/P95/P99、recall 与 storage overhead |
| SF-2026-ARXIV-2606-08960 | Disclosed — 1,968 tasks/5 terminal-agent benchmarks；KernelBench 与 Terminal-Bench case studies | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — attack success、held-out exploit rejection、legitimate-solver acceptance 与 patch transfer |
| SF-2026-ARXIV-2606-09005 | Disclosed — 六个 model settings、paired prompt-pressure controls、toy/semi-realistic/embedding/LangChain-style RAG | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — synthetic-canary disclosure、paired lift、confidence interval、FDR 与 source-authority probe |
| SF-2026-ARXIV-2606-09061 | Disclosed — 混合长短 prompt、NVIDIA GPU 与 Ascend、single/multi-GPU chunked-prefill workloads | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — mean/P99 E2E latency、TTFT、fairness、fragmentation、predictor error 与 portability |
| SF-2026-ARXIV-2606-09084 | Disclosed — 有限 model/tool/pipeline topologies 下的 context-fractured agent attack testbed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — ASR、context-removal/depth/width ablations、topology sensitivity 与 artifact inspection |
| SF-2026-ARXIV-2606-09441 | Disclosed — RAG context-reuse workloads、context-length sweep 与 diverse attention patterns | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — TTFT、accuracy、storage scaling、energy、breakdown 与 hyperparameter sensitivity |
| SF-2026-ARXIV-2606-09613 | Disclosed — 多轮 agent traces、real serving deployments、arrival/model/hardware/KV-tier sweeps | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — program JCT、throughput、TTFT/TPOT、policy rank preservation 与 prediction error |
| SF-2026-ARXIV-2606-09643 | Disclosed — 多 extension foundation-model serving configurations and baselines | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — memory footprint、load/switch latency、throughput、tail latency 与 extension-count sensitivity |
| SF-2026-ARXIV-2606-09682 | Disclosed — 多 GPU workload/kernel synthesis tasks with compile-and-run verification | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — compile success、numerical correctness、performance、repair rounds 与 failure taxonomy |
| SF-2026-ARXIV-2606-09686 | Disclosed — official v1 的 84-format catalog，覆盖 FP8/BF16/MXFP4/microscaling families | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — bit-exact vectors、cross-implementation agreement、edge-case coverage 与 mismatch diagnostics |
| SF-2026-ARXIV-2606-09692 | Disclosed — 跨工具 delegation/re-delegation、concurrency/retry reconstruction scenarios | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — reconstruction completeness、query correctness、gateway overhead 与 missing-lineage failure cases |
| SF-2026-ARXIV-2606-09711 | Disclosed — 可 exploit pytest rewards 的 coding RL checkpoints 与 evaluator-switch controls | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — hack onset/severity forecast、direct/activation probes、direction ablation 与 OOD misalignment correlation |
| SF-2026-ARXIV-2606-09774 | Disclosed — GEOS main benchmark；OpenFOAM/LAMMPS transfer；human calibration | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — structural/quality score、completion、variance、runtime、ablation 与 transfer delta |
| SF-2026-ARXIV-2606-09809 | Disclosed — 52-paper review、10 stakeholder interviews、5,816 models/635 benchmarks/101,843 results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Disclosed — schema coverage、documentation/comparability signals、extraction quality 与 monitoring findings |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-TRAIT-MISALIGNMENT-MONITOR | score_7_9 | not_selected | — | — | Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-TRAIT-MISALIGNMENT-MONITOR |
| SF-ML-LIFECYCLE-ASSESSMENT | score_7_9 | not_selected | — | — | Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-ML-LIFECYCLE-ASSESSMENT |
| SF-2026-ARXIV-2606-07684 | score_7_9; potential_books_delta | not_selected | — | — | Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07684 |
| SF-2026-ARXIV-2606-07783 | score_7_9; potential_books_delta | not_selected | — | — | Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07783 |
| SF-2026-ARXIV-2606-07790 | score_7_9; potential_books_delta | not_selected | — | — | Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07790 |
| SF-2026-ARXIV-2606-07805 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07805 |
| SF-2026-ARXIV-2606-07808 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07808 |
| SF-2026-ARXIV-2606-07822 | score_7_9; potential_books_delta | not_selected | — | — | The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07822 |
| SF-2026-ARXIV-2606-07833 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07833 |
| SF-2026-ARXIV-2606-07834 | score_7_9; potential_books_delta | selected | DA-20260606-EVALUATION-EVIDENCE | — | Selected as the strongest evidence-complete representative of a non-overlapping security-runtime, evaluation-evidence, or derived-state evolution chain. | analysis:DA-20260606-EVALUATION-EVIDENCE |
| SF-2026-ARXIV-2606-07845 | score_7_9 | not_selected | — | — | GRPO Does Not Close the Multi-Agent Coordination Gap remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07845 |
| SF-2026-ARXIV-2606-07867 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | The Cold-Start Safety Gap in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07867 |
| SF-2026-ARXIV-2606-07874 | score_7_9; potential_books_delta | not_selected | — | — | Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07874 |
| SF-2026-ARXIV-2606-07878 | score_7_9; potential_books_delta | not_selected | — | — | Still: Amortized KV Cache Compaction in a Single Forward Pass remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07878 |
| SF-2026-ARXIV-2606-07881 | score_7_9; potential_books_delta | not_selected | — | — | Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-PIPELINE-PARALLEL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07881 |
| SF-2026-ARXIV-2606-07889 | score_7_9; potential_books_delta | not_selected | — | — | Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07889 |
| SF-2026-ARXIV-2606-07904 | score_7_9 | not_selected | — | — | Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07904 |
| SF-2026-ARXIV-2606-07923 | score_7_9; potential_books_delta | not_selected | — | — | Larch: Learned Query Optimization for Semantic Predicates remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07923 |
| SF-2026-ARXIV-2606-07936 | score_7_9 | not_selected | — | — | Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07936 |
| SF-2026-ARXIV-2606-07943 | score_7_9; potential_books_delta; forced_review | selected | DA-20260607-SECURITY | — | Poise is the frontier's strongest non-overlapping security unit because it binds hidden skill placement to both verified side effect and legitimate-task success, exposing an admission failure that ordinary invocation metrics miss. | analysis:DA-20260607-SECURITY |
| SF-2026-ARXIV-2606-07950 | score_7_9 | not_selected | — | — | The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07950 |
| SF-2026-ARXIV-2606-07957 | score_7_9; forced_review | not_selected | — | — | Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07957 |
| SF-2026-ARXIV-2606-07968 | score_7_9 | not_selected | — | — | RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07968 |
| SF-2026-ARXIV-2606-07992 | score_7_9 | not_selected | — | — | VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-07992 |
| SF-2026-ARXIV-2606-08049 | score_7_9; potential_books_delta | not_selected | — | — | SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08049 |
| SF-2026-ARXIV-2606-08094 | score_7_9 | not_selected | — | — | vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-REQUEST-LIFECYCLE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08094 |
| SF-2026-ARXIV-2606-08106 | score_7_9; potential_books_delta | selected | DA-20260607-EVOLUTION | — | PACE is the strongest lifecycle-governance unit because it moves commit authority into an anytime-valid acceptor and quantifies both false and harmful self-modification under optional stopping. | analysis:DA-20260607-EVOLUTION |
| SF-2026-ARXIV-2606-08197 | score_7_9 | not_selected | — | — | AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08197 |
| SF-2026-ARXIV-2606-08200 | score_7_9; potential_books_delta | not_selected | — | — | Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08200 |
| SF-2026-ARXIV-2606-08340 | score_7_9 | not_selected | — | — | Benchmarking Open-Ended Multi-Agent Coordination in Language Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08340 |
| SF-2026-ARXIV-2606-08348 | score_7_9 | not_selected | — | — | Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08348 |
| SF-2026-ARXIV-2606-08367 | score_7_9 | not_selected | — | — | Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08367 |
| SF-2026-ARXIV-2606-08372 | score_7_9; forced_review | not_selected | — | — | SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC) remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08372 |
| SF-2026-ARXIV-2606-08382 | score_7_9 | not_selected | — | — | STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08382 |
| SF-2026-ARXIV-2606-08403 | score_7_9; potential_books_delta | not_selected | — | — | Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08403 |
| SF-2026-ARXIV-2606-08411 | score_7_9; potential_books_delta | not_selected | — | — | AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08411 |
| SF-2026-ARXIV-2606-08417 | score_7_9 | not_selected | — | — | Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08417 |
| SF-2026-ARXIV-2606-08432 | score_7_9 | not_selected | — | — | Trajectory-Refined Distillation remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08432 |
| SF-2026-ARXIV-2606-08433 | score_7_9 | not_selected | — | — | AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing) remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08433 |
| SF-2026-ARXIV-2606-08446 | score_7_9 | not_selected | — | — | Sparrow: Sparse Rollout for Stable and Efficient Long-context RL of Large Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08446 |
| SF-2026-ARXIV-2606-08476 | score_7_9; potential_books_delta | not_selected | — | — | FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08476 |
| SF-2026-ARXIV-2606-08483 | score_7_9 | not_selected | — | — | Testing the Black Box: Structural Barriers to Independent Evaluation of Consumer-Facing Health LLMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08483 |
| SF-2026-ARXIV-2606-08486 | score_7_9 | not_selected | — | — | TRADE: Transducer-Augmented Decoder for Speech LLM remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08486 |
| SF-2026-ARXIV-2606-08517 | score_7_9 | not_selected | — | — | A Joint Finite-Sample Certificate for Adaptive Selective Conformal Risk Control remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08517 |
| SF-2026-ARXIV-2606-08529 | score_7_9 | not_selected | — | — | Scaffold Effects on GAIA: A Controlled Comparison remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08529 |
| SF-2026-ARXIV-2606-08531 | score_7_9 | not_selected | — | — | ForesightSafety-SAGE:A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08531 |
| SF-2026-ARXIV-2606-08539 | score_7_9; potential_books_delta | not_selected | — | — | AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08539 |
| SF-2026-ARXIV-2606-08574 | score_7_9 | not_selected | — | — | OrderDP: A Theoretically Guaranteed Lossless Dynamic Data Pruning Framework remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08574 |
| SF-2026-ARXIV-2606-08590 | score_7_9 | not_selected | — | — | Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08590 |
| SF-2026-ARXIV-2606-08610 | score_7_9 | not_selected | — | — | HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08610 |
| SF-2026-ARXIV-2606-08615 | score_7_9 | not_selected | — | — | Harnessing Streaming Video in the Wild remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08615 |
| SF-2026-ARXIV-2606-08625 | score_7_9 | not_selected | — | — | From Holistic Evaluation to Structured Criteria: Rubrics Across the Evolving LLM Landscape remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08625 |
| SF-2026-ARXIV-2606-08635 | score_7_9; potential_books_delta | not_selected | — | — | SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-PD-DISAGGREGATION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08635 |
| SF-2026-ARXIV-2606-08661 | score_7_9 | not_selected | — | — | Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08661 |
| SF-2026-ARXIV-2606-08671 | score_7_9; potential_books_delta | not_selected | — | — | SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08671 |
| SF-2026-ARXIV-2606-08679 | score_7_9 | not_selected | — | — | Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08679 |
| SF-2026-ARXIV-2606-08702 | score_7_9 | not_selected | — | — | ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08702 |
| SF-2026-ARXIV-2606-08755 | score_7_9 | not_selected | — | — | Co-Evolving Skill Generation and Policy Optimization remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08755 |
| SF-2026-ARXIV-2606-08761 | score_7_9; potential_books_delta | not_selected | — | — | APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08761 |
| SF-2026-ARXIV-2606-08769 | score_7_9 | not_selected | — | — | RadOT-Eval: Auditable Structured-Evidence Transport for Radiology Report Evaluation remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08769 |
| SF-2026-ARXIV-2606-08779 | score_7_9 | not_selected | — | — | Reformulate LLM Reinforcement Learning for Efficient Training under Black-box Discrepancy remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08779 |
| SF-2026-ARXIV-2606-08790 | score_7_9 | not_selected | — | — | RAILS: Verification-Native Clearing For Agentic Commerce remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08790 |
| SF-2026-ARXIV-2606-08806 | score_7_9 | not_selected | — | — | Governance Controls for AI-Generated Test Artifacts in Autonomous Software Testing remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08806 |
| SF-2026-ARXIV-2606-08813 | score_7_9 | not_selected | — | — | Aperon Technical Report: Hierarchical No-Pointer Tangent-Local Search for High-Dimensional Approximate Nearest Neighbors remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08813 |
| SF-2026-ARXIV-2606-08831 | score_7_9 | not_selected | — | — | Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08831 |
| SF-2026-ARXIV-2606-08840 | score_7_9 | not_selected | — | — | Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08840 |
| SF-2026-ARXIV-2606-08867 | score_7_9 | not_selected | — | — | Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08867 |
| SF-2026-ARXIV-2606-08869 | score_7_9 | not_selected | — | — | A Low-Latency Semantic State Estimator using Latent Predictive Learning for Dynamic Network Monitoring and Orchestration remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08869 |
| SF-2026-ARXIV-2606-08891 | score_7_9 | not_selected | — | — | PALUTE: Processing-In-Memory Acceleration via Lookup Table for Edge LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08891 |
| SF-2026-ARXIV-2606-08892 | score_7_9 | not_selected | — | — | Diffuse AI Control on Fuzzy Tasks remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08892 |
| SF-2026-ARXIV-2606-08893 | score_7_9 | not_selected | — | — | Cheap Reward Hacking Detection remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08893 |
| SF-2026-ARXIV-2606-08919 | score_7_9; potential_books_delta | not_selected | — | — | Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08919 |
| SF-2026-ARXIV-2606-08950 | score_7_9; potential_books_delta | not_selected | — | — | When More Cores Hurts: The Vector Database Scaling Paradox in HPC remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08950 |
| SF-2026-ARXIV-2606-08960 | score_7_9; potential_books_delta | not_selected | — | — | Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-08960 |
| SF-2026-ARXIV-2606-09005 | score_7_9; potential_books_delta | not_selected | — | — | Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09005 |
| SF-2026-ARXIV-2606-09061 | score_7_9 | not_selected | — | — | Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill LLM Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09061 |
| SF-2026-ARXIV-2606-09084 | score_7_9; potential_books_delta | not_selected | — | — | Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09084 |
| SF-2026-ARXIV-2606-09441 | score_7_9; potential_books_delta | not_selected | — | — | SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-PREFILL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09441 |
| SF-2026-ARXIV-2606-09613 | score_7_9; potential_books_delta | not_selected | — | — | AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09613 |
| SF-2026-ARXIV-2606-09643 | score_7_9; potential_books_delta | not_selected | — | — | FMplex: Model Virtualization for Serving Extensible Foundation Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-KSERVE-TOPOLOGY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09643 |
| SF-2026-ARXIV-2606-09682 | score_7_9; potential_books_delta | not_selected | — | — | AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09682 |
| SF-2026-ARXIV-2606-09686 | score_7_9; potential_books_delta | not_selected | — | — | An 83-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09686 |
| SF-2026-ARXIV-2606-09692 | score_7_9; potential_books_delta | not_selected | — | — | Observability for Delegated Execution in Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09692 |
| SF-2026-ARXIV-2606-09711 | score_7_9; potential_books_delta | not_selected | — | — | Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09711 |
| SF-2026-ARXIV-2606-09774 | score_7_9; potential_books_delta | not_selected | — | — | Auto-Configuring Scientific Simulators with Lightweight Coding-Agent Adapters remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09774 |
| SF-2026-ARXIV-2606-09809 | score_7_9; potential_books_delta | not_selected | — | — | Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-09809 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-TRAIT-MISALIGNMENT-MONITOR:start -->
Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-TRAIT-MISALIGNMENT-MONITOR:end -->

<!-- analysis-decision:SF-ML-LIFECYCLE-ASSESSMENT:start -->
Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-ML-LIFECYCLE-ASSESSMENT:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07684:start -->
Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07684:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07783:start -->
Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07783:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07790:start -->
Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07790:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07805:start -->
Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07805:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07808:start -->
Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07808:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07822:start -->
The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07822:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07833:start -->
Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07833:end -->

<!-- analysis:DA-20260606-EVALUATION-EVIDENCE:start -->
Evaluation must preserve conflicting evidence rather than collapse it into one directional score. `2606.07834` is selected because mixed-evidence override directly challenges judge reliability and connects randomized harnesses, contextual priors, calibration and retrieval-condition slices without claiming one universal judge.
<!-- analysis:DA-20260606-EVALUATION-EVIDENCE:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07845:start -->
GRPO Does Not Close the Multi-Agent Coordination Gap remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07845:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07867:start -->
The Cold-Start Safety Gap in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07867:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07874:start -->
Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07874:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07878:start -->
Still: Amortized KV Cache Compaction in a Single Forward Pass remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07878:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07881:start -->
Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-PIPELINE-PARALLEL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07881:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07889:start -->
Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07889:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07904:start -->
Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07904:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07923:start -->
Larch: Learned Query Optimization for Semantic Predicates remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07923:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07936:start -->
Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07936:end -->

<!-- analysis:DA-20260607-SECURITY:start -->
Poise exposes why skill admission cannot stop at content scanning or invocation detection. The evidence object must join three identities: the exact skill position, the verified external side effect, and the legitimate-task verifier. This is selected over the other security families because it changes the release/admission contract without depending on a vendor-specific runtime; its SkillTester false-positive result also prevents treating an LLM audit alert as ground truth.
<!-- analysis:DA-20260607-SECURITY:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07950:start -->
The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07950:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07957:start -->
Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07957:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07968:start -->
RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07968:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07992:start -->
VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-07992:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08049:start -->
SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08049:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08094:start -->
vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-REQUEST-LIFECYCLE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08094:end -->

<!-- analysis:DA-20260607-EVOLUTION:start -->
PACE separates proposer quality from commit authority. Reusing the same noisy dev estimate across hundreds of proposals creates adaptive multiple testing; the acceptor, not the proposer, owns whether state changes. Paired anytime-valid evidence controls each candidate's false-commit probability under optional stopping, while the paper explicitly does not claim a global lifetime error bound. This is the frontier's clearest durable self-evolution gate.
<!-- analysis:DA-20260607-EVOLUTION:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08197:start -->
AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08197:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08200:start -->
Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08200:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08340:start -->
Benchmarking Open-Ended Multi-Agent Coordination in Language Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08340:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08348:start -->
Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08348:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08367:start -->
Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08367:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08372:start -->
SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC) remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08372:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08382:start -->
STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08382:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08403:start -->
Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08403:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08411:start -->
AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08411:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08417:start -->
Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08417:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08432:start -->
Trajectory-Refined Distillation remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08432:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08433:start -->
AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing) remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08433:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08446:start -->
Sparrow: Sparse Rollout for Stable and Efficient Long-context RL of Large Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08446:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08476:start -->
FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08476:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08483:start -->
Testing the Black Box: Structural Barriers to Independent Evaluation of Consumer-Facing Health LLMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08483:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08486:start -->
TRADE: Transducer-Augmented Decoder for Speech LLM remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08486:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08517:start -->
A Joint Finite-Sample Certificate for Adaptive Selective Conformal Risk Control remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08517:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08529:start -->
Scaffold Effects on GAIA: A Controlled Comparison remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08529:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08531:start -->
ForesightSafety-SAGE:A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08531:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08539:start -->
AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08539:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08574:start -->
OrderDP: A Theoretically Guaranteed Lossless Dynamic Data Pruning Framework remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08574:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08590:start -->
Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08590:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08610:start -->
HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08610:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08615:start -->
Harnessing Streaming Video in the Wild remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08615:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08625:start -->
From Holistic Evaluation to Structured Criteria: Rubrics Across the Evolving LLM Landscape remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08625:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08635:start -->
SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-PD-DISAGGREGATION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08635:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08661:start -->
Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08661:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08671:start -->
SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08671:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08679:start -->
Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08679:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08702:start -->
ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08702:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08755:start -->
Co-Evolving Skill Generation and Policy Optimization remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08755:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08761:start -->
APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08761:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08769:start -->
RadOT-Eval: Auditable Structured-Evidence Transport for Radiology Report Evaluation remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08769:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08779:start -->
Reformulate LLM Reinforcement Learning for Efficient Training under Black-box Discrepancy remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08779:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08790:start -->
RAILS: Verification-Native Clearing For Agentic Commerce remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08790:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08806:start -->
Governance Controls for AI-Generated Test Artifacts in Autonomous Software Testing remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08806:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08813:start -->
Aperon Technical Report: Hierarchical No-Pointer Tangent-Local Search for High-Dimensional Approximate Nearest Neighbors remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08813:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08831:start -->
Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08831:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08840:start -->
Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08840:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08867:start -->
Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08867:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08869:start -->
A Low-Latency Semantic State Estimator using Latent Predictive Learning for Dynamic Network Monitoring and Orchestration remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08869:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08891:start -->
PALUTE: Processing-In-Memory Acceleration via Lookup Table for Edge LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08891:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08892:start -->
Diffuse AI Control on Fuzzy Tasks remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08892:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08893:start -->
Cheap Reward Hacking Detection remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08893:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08919:start -->
Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08919:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08950:start -->
When More Cores Hurts: The Vector Database Scaling Paradox in HPC remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08950:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-08960:start -->
Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-08960:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09005:start -->
Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09061:start -->
Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill LLM Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09061:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09084:start -->
Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09084:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09441:start -->
SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-PREFILL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09441:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09613:start -->
AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09613:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09643:start -->
FMplex: Model Virtualization for Serving Extensible Foundation Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-KSERVE-TOPOLOGY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09643:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09682:start -->
AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09682:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09686:start -->
An 83-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09692:start -->
Observability for Delegated Execution in Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09692:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09711:start -->
Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09711:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09774:start -->
Auto-Configuring Scientific Simulators with Lightweight Coding-Agent Adapters remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09774:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-09809:start -->
Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-09809:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-TRAIT-MISALIGNMENT-MONITOR | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L49 | books/part-06-ai-infrastructure/66-evaluation-system.md#L235;books/part-06-ai-infrastructure/68-logging.md#L119 | existing:SF-TRAIT-MISALIGNMENT-MONITOR | delta:SF-TRAIT-MISALIGNMENT-MONITOR | Layering / Dependency | No Change — Existing Coverage | books-review:SF-TRAIT-MISALIGNMENT-MONITOR |
| SF-ML-LIFECYCLE-ASSESSMENT | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L71 | books/part-06-ai-infrastructure/69-trace.md#L14;books/part-06-ai-infrastructure/71-multi-tenant.md#L14 | existing:SF-ML-LIFECYCLE-ASSESSMENT | delta:SF-ML-LIFECYCLE-ASSESSMENT | Direct Evolution | No Change — Existing Coverage | books-review:SF-ML-LIFECYCLE-ASSESSMENT |
| SF-2026-ARXIV-2606-07684 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L10 | books/part-07-agent/76-rag.md#L10; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-2026-ARXIV-2606-07684 | delta:SF-2026-ARXIV-2606-07684 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07684 |
| SF-2026-ARXIV-2606-07687 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 | existing:SF-2026-ARXIV-2606-07687 | delta:SF-2026-ARXIV-2606-07687 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07687 |
| SF-2026-ARXIV-2606-07703 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L10 | books/part-05-inference-system/42-what-happens-during-inference.md#L10; books/part-05-inference-system/44-decode.md#L10 | existing:SF-2026-ARXIV-2606-07703 | delta:SF-2026-ARXIV-2606-07703 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07703 |
| SF-2026-ARXIV-2606-07710 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L10 | books/part-05-inference-system/47-pagedattention.md#L10; books/part-05-inference-system/49-tensorrt-llm.md#L10 | existing:SF-2026-ARXIV-2606-07710 | delta:SF-2026-ARXIV-2606-07710 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07710 |
| SF-2026-ARXIV-2606-07713 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L10 | books/part-05-inference-system/48-speculative-decoding.md#L10; books/part-05-inference-system/50-vllm.md#L10 | existing:SF-2026-ARXIV-2606-07713 | delta:SF-2026-ARXIV-2606-07713 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07713 |
| SF-2026-ARXIV-2606-07720 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L10 | books/part-07-agent/74-prompt.md#L10; books/part-07-agent/76-rag.md#L10 | existing:SF-2026-ARXIV-2606-07720 | delta:SF-2026-ARXIV-2606-07720 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07720 |
| SF-2026-ARXIV-2606-07726 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10 | existing:SF-2026-ARXIV-2606-07726 | delta:SF-2026-ARXIV-2606-07726 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07726 |
| SF-2026-ARXIV-2606-07783 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10 | existing:SF-2026-ARXIV-2606-07783 | delta:SF-2026-ARXIV-2606-07783 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07783 |
| SF-2026-ARXIV-2606-07790 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L10 | books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10 | existing:SF-2026-ARXIV-2606-07790 | delta:SF-2026-ARXIV-2606-07790 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07790 |
| SF-2026-ARXIV-2606-07805 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L10 | books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10 | existing:SF-2026-ARXIV-2606-07805 | delta:SF-2026-ARXIV-2606-07805 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07805 |
| SF-2026-ARXIV-2606-07808 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-2026-ARXIV-2606-07808 | delta:SF-2026-ARXIV-2606-07808 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07808 |
| SF-2026-ARXIV-2606-07822 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10 | existing:SF-2026-ARXIV-2606-07822 | delta:SF-2026-ARXIV-2606-07822 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07822 |
| SF-2026-ARXIV-2606-07833 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-2026-ARXIV-2606-07833 | delta:SF-2026-ARXIV-2606-07833 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07833 |
| SF-2026-ARXIV-2606-07834 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10 | existing:SF-2026-ARXIV-2606-07834 | delta:SF-2026-ARXIV-2606-07834 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07834 |
| SF-2026-ARXIV-2606-07845 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L10 | books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10 | existing:SF-2026-ARXIV-2606-07845 | delta:SF-2026-ARXIV-2606-07845 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07845 |
| SF-2026-ARXIV-2606-07846 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L10 | books/part-07-agent/80-reflection.md#L10; books/part-07-agent/82-multi-agent.md#L10 | existing:SF-2026-ARXIV-2606-07846 | delta:SF-2026-ARXIV-2606-07846 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07846 |
| SF-2026-ARXIV-2606-07856 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L10 | books/part-04-training-system/28-pretraining.md#L10; books/part-04-training-system/30-lora.md#L10 | existing:SF-2026-ARXIV-2606-07856 | delta:SF-2026-ARXIV-2606-07856 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07856 |
| SF-2026-ARXIV-2606-07867 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L10 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-2026-ARXIV-2606-07867 | delta:SF-2026-ARXIV-2606-07867 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07867 |
| SF-2026-ARXIV-2606-07874 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10 | existing:SF-2026-ARXIV-2606-07874 | delta:SF-2026-ARXIV-2606-07874 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07874 |
| SF-2026-ARXIV-2606-07878 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | books/part-05-inference-system/44-decode.md#L10; books/part-05-inference-system/46-continuous-batching.md#L10 | existing:SF-2026-ARXIV-2606-07878 | delta:SF-2026-ARXIV-2606-07878 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07878 |
| SF-2026-ARXIV-2606-07881 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#L10 | books/part-04-training-system/37-tensor-parallel.md#L10; books/part-04-training-system/39-zero.md#L10 | existing:SF-2026-ARXIV-2606-07881 | delta:SF-2026-ARXIV-2606-07881 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07881 |
| SF-2026-ARXIV-2606-07889 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L10 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-06-ai-infrastructure/68-logging.md#L10 | existing:SF-2026-ARXIV-2606-07889 | delta:SF-2026-ARXIV-2606-07889 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07889 |
| SF-2026-ARXIV-2606-07904 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L10 | books/part-07-agent/77-memory.md#L10; books/part-07-agent/79-planning.md#L10 | existing:SF-2026-ARXIV-2606-07904 | delta:SF-2026-ARXIV-2606-07904 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07904 |
| SF-2026-ARXIV-2606-07923 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L358 | ROADMAP.md#L1; books/part-05-inference-system/56-inference-scheduling.md#L10 | existing:SF-2026-ARXIV-2606-07923 | delta:SF-2026-ARXIV-2606-07923 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07923 |
| SF-2026-ARXIV-2606-07936 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-07936 | delta:SF-2026-ARXIV-2606-07936 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07936 |
| SF-2026-ARXIV-2606-07943 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L367 | ROADMAP.md#L1; books/part-06-ai-infrastructure/72-security.md#L10 | existing:SF-2026-ARXIV-2606-07943 | delta:SF-2026-ARXIV-2606-07943 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-07943 |
| SF-2026-ARXIV-2606-07950 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L10 | ROADMAP.md#L1; books/part-04-training-system/33-grpo.md#L10 | existing:SF-2026-ARXIV-2606-07950 | delta:SF-2026-ARXIV-2606-07950 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07950 |
| SF-2026-ARXIV-2606-07957 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L367 | ROADMAP.md#L1; books/part-06-ai-infrastructure/72-security.md#L10 | existing:SF-2026-ARXIV-2606-07957 | delta:SF-2026-ARXIV-2606-07957 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07957 |
| SF-2026-ARXIV-2606-07968 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L10 | ROADMAP.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L10 | existing:SF-2026-ARXIV-2606-07968 | delta:SF-2026-ARXIV-2606-07968 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07968 |
| SF-2026-ARXIV-2606-07970 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L10 | ROADMAP.md#L1; books/part-04-training-system/29-sft.md#L10 | existing:SF-2026-ARXIV-2606-07970 | delta:SF-2026-ARXIV-2606-07970 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07970 |
| SF-2026-ARXIV-2606-07992 | AGENT-MCP | books/part-07-agent/78-tool-calling.md#L10 | ROADMAP.md#L1; books/part-07-agent/78-tool-calling.md#L10 | existing:SF-2026-ARXIV-2606-07992 | delta:SF-2026-ARXIV-2606-07992 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07992 |
| SF-2026-ARXIV-2606-08049 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L159 | ROADMAP.md#L1; books/part-07-agent/81-workflow.md#L10 | existing:SF-2026-ARXIV-2606-08049 | delta:SF-2026-ARXIV-2606-08049 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08049 |
| SF-2026-ARXIV-2606-08094 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L10 | ROADMAP.md#L1; books/part-05-inference-system/42-what-happens-during-inference.md#L10 | existing:SF-2026-ARXIV-2606-08094 | delta:SF-2026-ARXIV-2606-08094 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08094 |
| SF-2026-ARXIV-2606-08106 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L343 | ROADMAP.md#L1; books/part-07-agent/84-agent-platform.md#L10 | existing:SF-2026-ARXIV-2606-08106 | delta:SF-2026-ARXIV-2606-08106 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08106 |
| SF-2026-ARXIV-2606-08197 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L10 | ROADMAP.md#L1; books/part-04-training-system/36-distributed-training.md#L10 | existing:SF-2026-ARXIV-2606-08197 | delta:SF-2026-ARXIV-2606-08197 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08197 |
| SF-2026-ARXIV-2606-08200 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-08200 | delta:SF-2026-ARXIV-2606-08200 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08200 |
| SF-2026-ARXIV-2606-08302 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292 | ROADMAP.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | existing:SF-2026-ARXIV-2606-08302 | delta:SF-2026-ARXIV-2606-08302 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08302 |
| SF-2026-ARXIV-2606-08317 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L10 | books/part-06-ai-infrastructure/58-kubeflow.md#L10 | existing:SF-2026-ARXIV-2606-08317 | delta:SF-2026-ARXIV-2606-08317 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08317 |
| SF-2026-ARXIV-2606-08340 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L10 | ROADMAP.md#L1; books/part-07-agent/82-multi-agent.md#L10 | existing:SF-2026-ARXIV-2606-08340 | delta:SF-2026-ARXIV-2606-08340 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08340 |
| SF-2026-ARXIV-2606-08346 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L10 | ROADMAP.md#L1; books/part-04-training-system/33-grpo.md#L10 | existing:SF-2026-ARXIV-2606-08346 | delta:SF-2026-ARXIV-2606-08346 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08346 |
| SF-2026-ARXIV-2606-08348 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L343 | ROADMAP.md#L1; books/part-07-agent/84-agent-platform.md#L10 | existing:SF-2026-ARXIV-2606-08348 | delta:SF-2026-ARXIV-2606-08348 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08348 |
| SF-2026-ARXIV-2606-08367 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-08367 | delta:SF-2026-ARXIV-2606-08367 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08367 |
| SF-2026-ARXIV-2606-08372 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L367 | ROADMAP.md#L1; books/part-06-ai-infrastructure/72-security.md#L10 | existing:SF-2026-ARXIV-2606-08372 | delta:SF-2026-ARXIV-2606-08372 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08372 |
| SF-2026-ARXIV-2606-08381 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L335 | ROADMAP.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | existing:SF-2026-ARXIV-2606-08381 | delta:SF-2026-ARXIV-2606-08381 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08381 |
| SF-2026-ARXIV-2606-08382 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292 | ROADMAP.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 | existing:SF-2026-ARXIV-2606-08382 | delta:SF-2026-ARXIV-2606-08382 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08382 |
| SF-2026-ARXIV-2606-08403 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1349 | books/part-06-ai-infrastructure/71-multi-tenant.md#L84; books/part-06-ai-infrastructure/73-production-best-practice.md#L144 | existing:SF-2026-ARXIV-2606-08403 | delta:SF-2026-ARXIV-2606-08403 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08403 |
| SF-2026-ARXIV-2606-08411 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L254 | books/part-05-inference-system/43-prefill.md#L367; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L645 | existing:SF-2026-ARXIV-2606-08411 | delta:SF-2026-ARXIV-2606-08411 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08411 |
| SF-2026-ARXIV-2606-08417 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1268 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L113; books/part-06-ai-infrastructure/67-monitoring.md#L113 | existing:SF-2026-ARXIV-2606-08417 | delta:SF-2026-ARXIV-2606-08417 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08417 |
| SF-2026-ARXIV-2606-08432 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L315 | books/part-04-training-system/28-pretraining.md#L833; books/part-04-training-system/30-lora.md#L370 | existing:SF-2026-ARXIV-2606-08432 | delta:SF-2026-ARXIV-2606-08432 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08432 |
| SF-2026-ARXIV-2606-08433 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L955 | books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L98 | existing:SF-2026-ARXIV-2606-08433 | delta:SF-2026-ARXIV-2606-08433 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08433 |
| SF-2026-ARXIV-2606-08446 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L835 | books/part-04-training-system/32-ppo.md#L284; books/part-04-training-system/34-dpo.md#L283 | existing:SF-2026-ARXIV-2606-08446 | delta:SF-2026-ARXIV-2606-08446 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08446 |
| SF-2026-ARXIV-2606-08476 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L903 | books/part-04-training-system/35-checkpoint.md#L502; books/part-04-training-system/37-tensor-parallel.md#L305 | existing:SF-2026-ARXIV-2606-08476 | delta:SF-2026-ARXIV-2606-08476 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08476 |
| SF-2026-ARXIV-2606-08483 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1018 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L76 | existing:SF-2026-ARXIV-2606-08483 | delta:SF-2026-ARXIV-2606-08483 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08483 |
| SF-2026-ARXIV-2606-08486 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L178 | books/part-05-inference-system/43-prefill.md#L329; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L456 | existing:SF-2026-ARXIV-2606-08486 | delta:SF-2026-ARXIV-2606-08486 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08486 |
| SF-2026-ARXIV-2606-08517 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1701 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L243 | existing:SF-2026-ARXIV-2606-08517 | delta:SF-2026-ARXIV-2606-08517 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08517 |
| SF-2026-ARXIV-2606-08529 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L140 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L243 | existing:SF-2026-ARXIV-2606-08529 | delta:SF-2026-ARXIV-2606-08529 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08529 |
| SF-2026-ARXIV-2606-08531 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1835 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L130; books/part-06-ai-infrastructure/67-monitoring.md#L289 | existing:SF-2026-ARXIV-2606-08531 | delta:SF-2026-ARXIV-2606-08531 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08531 |
| SF-2026-ARXIV-2606-08539 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1349 | books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L183 | existing:SF-2026-ARXIV-2606-08539 | delta:SF-2026-ARXIV-2606-08539 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08539 |
| SF-2026-ARXIV-2606-08574 | TRAIN-DATA | books/part-04-training-system/27-data.md#L133 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L546; books/part-04-training-system/28-pretraining.md#L833 | existing:SF-2026-ARXIV-2606-08574 | delta:SF-2026-ARXIV-2606-08574 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08574 |
| SF-2026-ARXIV-2606-08590 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L128 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1964; books/part-06-ai-infrastructure/68-logging.md#L106 | existing:SF-2026-ARXIV-2606-08590 | delta:SF-2026-ARXIV-2606-08590 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08590 |
| SF-2026-ARXIV-2606-08610 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L104 | books/part-07-agent/80-reflection.md#L213; books/part-07-agent/82-multi-agent.md#L509 | existing:SF-2026-ARXIV-2606-08610 | delta:SF-2026-ARXIV-2606-08610 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08610 |
| SF-2026-ARXIV-2606-08615 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L14 | books/part-07-agent/76-rag.md#L162; books/part-07-agent/78-tool-calling.md#L313 | existing:SF-2026-ARXIV-2606-08615 | delta:SF-2026-ARXIV-2606-08615 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08615 |
| SF-2026-ARXIV-2606-08625 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1372 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L289 | existing:SF-2026-ARXIV-2606-08625 | delta:SF-2026-ARXIV-2606-08625 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08625 |
| SF-2026-ARXIV-2606-08635 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L444 | books/part-05-inference-system/54-gpu-memory.md#L359; books/part-05-inference-system/56-inference-scheduling.md#L758 | existing:SF-2026-ARXIV-2606-08635 | delta:SF-2026-ARXIV-2606-08635 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08635 |
| SF-2026-ARXIV-2606-08661 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L562 | books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L183 | existing:SF-2026-ARXIV-2606-08661 | delta:SF-2026-ARXIV-2606-08661 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08661 |
| SF-2026-ARXIV-2606-08671 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L303 | books/part-07-agent/79-planning.md#L326; books/part-07-agent/81-workflow.md#L714 | existing:SF-2026-ARXIV-2606-08671 | delta:SF-2026-ARXIV-2606-08671 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08671 |
| SF-2026-ARXIV-2606-08679 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1807 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L291 | existing:SF-2026-ARXIV-2606-08679 | delta:SF-2026-ARXIV-2606-08679 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08679 |
| SF-2026-ARXIV-2606-08702 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L703 | books/part-07-agent/76-rag.md#L432; books/part-07-agent/78-tool-calling.md#L314 | existing:SF-2026-ARXIV-2606-08702 | delta:SF-2026-ARXIV-2606-08702 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08702 |
| SF-2026-ARXIV-2606-08755 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L274 | books/part-07-agent/79-planning.md#L286; books/part-07-agent/81-workflow.md#L728 | existing:SF-2026-ARXIV-2606-08755 | delta:SF-2026-ARXIV-2606-08755 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08755 |
| SF-2026-ARXIV-2606-08761 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L423 | books/part-05-inference-system/53-kserve-llm.md#L168; books/part-05-inference-system/55-pd-disaggregation.md#L409 | existing:SF-2026-ARXIV-2606-08761 | delta:SF-2026-ARXIV-2606-08761 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08761 |
| SF-2026-ARXIV-2606-08769 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L74 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L113 | existing:SF-2026-ARXIV-2606-08769 | delta:SF-2026-ARXIV-2606-08769 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08769 |
| SF-2026-ARXIV-2606-08779 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L420 | books/part-04-training-system/30-lora.md#L419; books/part-04-training-system/32-ppo.md#L378 | existing:SF-2026-ARXIV-2606-08779 | delta:SF-2026-ARXIV-2606-08779 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08779 |
| SF-2026-ARXIV-2606-08790 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L14 | books/part-07-agent/77-memory.md#L1167; books/part-07-agent/79-planning.md#L284 | existing:SF-2026-ARXIV-2606-08790 | delta:SF-2026-ARXIV-2606-08790 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08790 |
| SF-2026-ARXIV-2606-08806 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L45 | books/part-06-ai-infrastructure/72-security.md#L1047; books/part-07-agent/74-prompt.md#L189 | existing:SF-2026-ARXIV-2606-08806 | delta:SF-2026-ARXIV-2606-08806 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08806 |
| SF-2026-ARXIV-2606-08813 | AGENT-RAG | books/part-07-agent/76-rag.md#L33 | books/part-07-agent/75-context.md#L290; books/part-07-agent/77-memory.md#L1188 | existing:SF-2026-ARXIV-2606-08813 | delta:SF-2026-ARXIV-2606-08813 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08813 |
| SF-2026-ARXIV-2606-08831 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1463 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L275 | existing:SF-2026-ARXIV-2606-08831 | delta:SF-2026-ARXIV-2606-08831 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08831 |
| SF-2026-ARXIV-2606-08840 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L170 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L243 | existing:SF-2026-ARXIV-2606-08840 | delta:SF-2026-ARXIV-2606-08840 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08840 |
| SF-2026-ARXIV-2606-08867 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L14 | books/part-07-agent/83-mcp.md#L212 | existing:SF-2026-ARXIV-2606-08867 | delta:SF-2026-ARXIV-2606-08867 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08867 |
| SF-2026-ARXIV-2606-08869 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L128 | books/part-06-ai-infrastructure/66-evaluation-system.md#L2123; books/part-06-ai-infrastructure/68-logging.md#L105 | existing:SF-2026-ARXIV-2606-08869 | delta:SF-2026-ARXIV-2606-08869 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08869 |
| SF-2026-ARXIV-2606-08891 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L987 | books/part-05-inference-system/48-speculative-decoding.md#L711; books/part-05-inference-system/50-vllm.md#L379 | existing:SF-2026-ARXIV-2606-08891 | delta:SF-2026-ARXIV-2606-08891 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08891 |
| SF-2026-ARXIV-2606-08892 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L298 | books/part-06-ai-infrastructure/71-multi-tenant.md#L139; books/part-06-ai-infrastructure/73-production-best-practice.md#L134 | existing:SF-2026-ARXIV-2606-08892 | delta:SF-2026-ARXIV-2606-08892 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08892 |
| SF-2026-ARXIV-2606-08893 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1811 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L241 | existing:SF-2026-ARXIV-2606-08893 | delta:SF-2026-ARXIV-2606-08893 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-08893 |
| SF-2026-ARXIV-2606-08919 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L716 | books/part-07-agent/80-reflection.md#L1; books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-08919 | delta:SF-2026-ARXIV-2606-08919 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08919 |
| SF-2026-ARXIV-2606-08950 | AGENT-RAG | Books/part-07-agent/76-rag.md#L51 | books/part-07-agent/75-context.md#L1; books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-08950 | delta:SF-2026-ARXIV-2606-08950 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08950 |
| SF-2026-ARXIV-2606-08960 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1946 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-08960 | delta:SF-2026-ARXIV-2606-08960 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-08960 |
| SF-2026-ARXIV-2606-09005 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L992 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-09005 | delta:SF-2026-ARXIV-2606-09005 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09005 |
| SF-2026-ARXIV-2606-09061 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L180 | books/part-05-inference-system/55-pd-disaggregation.md#L1; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L1 | existing:SF-2026-ARXIV-2606-09061 | delta:SF-2026-ARXIV-2606-09061 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-09061 |
| SF-2026-ARXIV-2606-09084 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L998 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-09084 | delta:SF-2026-ARXIV-2606-09084 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09084 |
| SF-2026-ARXIV-2606-09441 | INFER-PREFILL | Books/part-05-inference-system/43-prefill.md#L331 | books/part-05-inference-system/42-what-happens-during-inference.md#L1; books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2606-09441 | delta:SF-2026-ARXIV-2606-09441 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09441 |
| SF-2026-ARXIV-2606-09613 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L718 | books/part-05-inference-system/55-pd-disaggregation.md#L1; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L1 | existing:SF-2026-ARXIV-2606-09613 | delta:SF-2026-ARXIV-2606-09613 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09613 |
| SF-2026-ARXIV-2606-09643 | INFER-KSERVE-TOPOLOGY | Books/part-05-inference-system/53-kserve-llm.md#L195 | books/part-05-inference-system/52-dynamo.md#L1; books/part-05-inference-system/54-gpu-memory.md#L1 | existing:SF-2026-ARXIV-2606-09643 | delta:SF-2026-ARXIV-2606-09643 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09643 |
| SF-2026-ARXIV-2606-09682 | INFER-TENSORRT-LLM | Books/part-05-inference-system/49-tensorrt-llm.md#L991 | books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-05-inference-system/50-vllm.md#L1 | existing:SF-2026-ARXIV-2606-09682 | delta:SF-2026-ARXIV-2606-09682 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09682 |
| SF-2026-ARXIV-2606-09686 | INFER-TENSORRT-LLM | Books/part-05-inference-system/49-tensorrt-llm.md#L997 | books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-05-inference-system/50-vllm.md#L1 | existing:SF-2026-ARXIV-2606-09686 | delta:SF-2026-ARXIV-2606-09686 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09686 |
| SF-2026-ARXIV-2606-09692 | PLATFORM-TRACE | Books/part-06-ai-infrastructure/69-trace.md#L165 | books/part-06-ai-infrastructure/68-logging.md#L1; books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2606-09692 | delta:SF-2026-ARXIV-2606-09692 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09692 |
| SF-2026-ARXIV-2606-09711 | TRAIN-RLHF | Books/part-04-training-system/31-rlhf.md#L414 | books/part-04-training-system/30-lora.md#L1; books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-09711 | delta:SF-2026-ARXIV-2606-09711 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09711 |
| SF-2026-ARXIV-2606-09774 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L722 | books/part-07-agent/80-reflection.md#L1; books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-09774 | delta:SF-2026-ARXIV-2606-09774 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09774 |
| SF-2026-ARXIV-2606-09809 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1952 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-09809 | delta:SF-2026-ARXIV-2606-09809 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-09809 |

<!-- existing:SF-TRAIT-MISALIGNMENT-MONITOR:start -->`PLATFORM-MONITORING` 当前与该机制最接近的命题是：类似地，telemetry、health verdict 与 attestation 是三层证据。Agent/exporter 可以报告 sensor state，health service 可按 policy 聚合判断，attestation 只证明指定 software/boundary 的身份与完整性；任何一层都不能自动证明设备 会故障、模型结果正确或 workload 应迁移。NVIDIA Fleet Intelligence 作为版本化实现案例支持这类分层，不支持 把厂商 predictive-failure 效果外推为通用因果结论。 相邻章节对 handoff 的约束是：只奖励“主动完成”会驱动 Agent 过度行动；只测 intent recovery 又看不到 rejection 后是否停止。Proactivity 的 operating point 至少包含正确行动、应该沉默时不行动，以及用户拒绝/纠正后的停止。Deterministic side-effect checks 与 soft preference judge 应分开，simulator identity、hidden profile、feedback history 和 policy revision 都属于 evaluation contract。KnowU-Bench 是 Experimental case；synthetic personas 与小规模 judge calibration 不能代表真实用户人口。 / 这个 snapshot 机制补足 detection 到 diagnosis 的中间层，不替代 metrics、distributed trace、hardware telemetry 或 deterministic collective tests。Ring buffer 有 overhead，timeout 时 side channel、monitor thread 或 teardown 仍可能丢数据，离线分析也增加反馈延迟。小作业或可稳定复现的错误可继续用普通日志和显式 assertion；官方 fleet 比例不能外推成任意集群的 root-cause 先验。<!-- existing:SF-TRAIT-MISALIGNMENT-MONITOR:end -->

<!-- delta:SF-TRAIT-MISALIGNMENT-MONITOR:start -->只靠周期性行为评估能发现 emergent misalignment，但检测间隔长且成本高。该方法把七个 alignment trait 编成 activation direction，跨 checkpoint 追踪低维 drift，并用该 profile 训练轻量 monitor。 四个 7–9B 模型和 14B stress test 支持研究 regime 内的 AUROC/误报漏报；内部 drift 只是 sensor，跨模型、起始 misalignment 与更长训练需要重校准。它需要白盒 activation 访问，不能取代行为验收或 effect-time policy。<!-- delta:SF-TRAIT-MISALIGNMENT-MONITOR:end -->

<!-- books-review:SF-TRAIT-MISALIGNMENT-MONITOR:start -->`Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning` 与 `PLATFORM-MONITORING` 的关系判定为 `Layering / Dependency`。比较 `books/part-06-ai-infrastructure/67-monitoring.md#L49` 与 `books/part-06-ai-infrastructure/66-evaluation-system.md#L235;books/part-06-ai-infrastructure/68-logging.md#L119` 后，决定为 `No Change — Existing Coverage`：该 exact-v1 的机制 `只靠周期性行为评估能发现 emergent misalignment，但检测间隔长且成本高。该方法把七个 alignment trait 编成 activation direction，跨 checkpoint 追踪低维 drift，并用该 profile 训练轻量 monitor。 四个 7–9B 模型和 14B stress test 支持研究 regime 内的 AUROC/误报漏报；内部 drift 只是 sensor，跨模型、起始 misalignment 与更长训练需要重校准。它需要白盒 activation 访问，不能取代行为验收或 effect-time policy。` 已被现有命题或相邻 handoff 覆盖；作者结果只增加受限实例，而 `只靠周期性行为评估能发现 emergent misalignment，但检测间隔长且成本高。该方法把七个 alignment trait 编成 activation direction，跨 checkpoint 追踪低维 drift，并用该 profile 训练轻量 monitor。 四个 7–9B 模型和 14B stress test 支持研究 regime 内的 AUROC/误报漏报；内部 drift 只是 sensor，跨模型、起始 misalignment 与更长训练需要重校准。它需要白盒 activation 访问，不能取代行为验收或 effect-time policy。` 阻止把它提升为新的长期设计结论。 不把论文名称、作者 benchmark 或未披露实现写成长期机制；若为 Integrate，正文写回仍由 root 按日期串行处理。<!-- books-review:SF-TRAIT-MISALIGNMENT-MONITOR:end -->

<!-- existing:SF-ML-LIFECYCLE-ASSESSMENT:start -->`PLATFORM-COST` 当前与该机制最接近的命题是：Prefill Token Equivalents 可以作为 analytical proxy，把 Context growth、cache reuse 与 tool schedule 统一到近似 work unit；但系数依赖 model、hardware、precision、batch/concurrency、kernel、KV policy 和 lengths，不能当 latency 或账单真值。短单轮、稳定 cache hit 或直接测量完备时，普通 token/accelerator-time 指标仍合理。平台应并列保存 proxy、measured device time、wall-clock、tool cost 与 SLO，而不是用一个静态系数覆盖它们。 相邻章节对 handoff 的约束是：本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。** / 本章的核心判断是：**Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。**<!-- existing:SF-ML-LIFECYCLE-ASSESSMENT:end -->

<!-- delta:SF-ML-LIFECYCLE-ASSESSMENT:start -->Model life-cycle assessment expands efficiency accounting from one training run or inference sample to data, experimentation, deployment, refresh, infrastructure and retirement under an explicit functional unit. 证据边界：Inventory boundaries and sector projections retain uncertainty; an LCA framework supports comparable accounting but does not supply undisclosed vendor energy data.<!-- delta:SF-ML-LIFECYCLE-ASSESSMENT:end -->

<!-- books-review:SF-ML-LIFECYCLE-ASSESSMENT:start -->`Position: Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment` 与 `PLATFORM-COST` 的关系判定为 `Direct Evolution`。比较 `books/part-06-ai-infrastructure/70-cost.md#L71` 与 `books/part-06-ai-infrastructure/69-trace.md#L14;books/part-06-ai-infrastructure/71-multi-tenant.md#L14` 后，决定为 `No Change — Existing Coverage`：该 exact-v1 的机制 `Model life-cycle assessment expands efficiency accounting from one training run or inference sample to data, experimentation, deployment, refresh, infrastructure and retirement under an explicit functional unit.` 已被现有命题或相邻 handoff 覆盖；作者结果只增加受限实例，而 `Inventory boundaries and sector projections retain uncertainty; an LCA framework supports comparable accounting but does not supply undisclosed vendor energy data.` 阻止把它提升为新的长期设计结论。 不把论文名称、作者 benchmark 或未披露实现写成长期机制；若为 Integrate，正文写回仍由 root 按日期串行处理。<!-- books-review:SF-ML-LIFECYCLE-ASSESSMENT:end -->

<!-- books-review:SF-2026-ARXIV-2606-07684:start -->
SF-2026-ARXIV-2606-07684: fresh comparison read `books/part-07-agent/77-memory.md#L10` and `books/part-07-agent/76-rag.md#L10; books/part-07-agent/78-tool-calling.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07684:start -->
Ch77 §§Memory Write/Read; 派生策略; 一致性与并发
<!-- existing:SF-2026-ARXIV-2606-07684:end -->

<!-- delta:SF-2026-ARXIV-2606-07684:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07684:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07684:end -->

<!-- books-review:SF-2026-ARXIV-2606-07687:start -->
SF-2026-ARXIV-2606-07687: fresh comparison read `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10` and `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07687:start -->
Ch25 §§State ownership; Control flow 与数据流; Evaluation
<!-- existing:SF-2026-ARXIV-2606-07687:end -->

<!-- delta:SF-2026-ARXIV-2606-07687:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07687:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07687:end -->

<!-- books-review:SF-2026-ARXIV-2606-07703:start -->
SF-2026-ARXIV-2606-07703: fresh comparison read `books/part-05-inference-system/43-prefill.md#L10` and `books/part-05-inference-system/42-what-happens-during-inference.md#L10; books/part-05-inference-system/44-decode.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07703:start -->
Ch43 §§Prefill 输出; TTFT 边界; 长 Prompt 干扰 Decode
<!-- existing:SF-2026-ARXIV-2606-07703:end -->

<!-- delta:SF-2026-ARXIV-2606-07703:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07703:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07703:end -->

<!-- books-review:SF-2026-ARXIV-2606-07710:start -->
SF-2026-ARXIV-2606-07710: fresh comparison read `books/part-05-inference-system/48-speculative-decoding.md#L10` and `books/part-05-inference-system/47-pagedattention.md#L10; books/part-05-inference-system/49-tensorrt-llm.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07710:start -->
Ch48 §§Exact Acceptance; Lossless Verification; Drafter 演进
<!-- existing:SF-2026-ARXIV-2606-07710:end -->

<!-- delta:SF-2026-ARXIV-2606-07710:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07710:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07710:end -->

<!-- books-review:SF-2026-ARXIV-2606-07713:start -->
SF-2026-ARXIV-2606-07713: fresh comparison read `books/part-05-inference-system/49-tensorrt-llm.md#L10` and `books/part-05-inference-system/48-speculative-decoding.md#L10; books/part-05-inference-system/50-vllm.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07713:start -->
Ch49 §§GEMM 执行; FlashAttention; Build-time 与 Runtime-time
<!-- existing:SF-2026-ARXIV-2606-07713:end -->

<!-- delta:SF-2026-ARXIV-2606-07713:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07713:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07713:end -->

<!-- books-review:SF-2026-ARXIV-2606-07720:start -->
SF-2026-ARXIV-2606-07720: fresh comparison read `books/part-07-agent/75-context.md#L10` and `books/part-07-agent/74-prompt.md#L10; books/part-07-agent/76-rag.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07720:start -->
Ch75 §§Context Assembly; Compression; Context Identity
<!-- existing:SF-2026-ARXIV-2606-07720:end -->

<!-- delta:SF-2026-ARXIV-2606-07720:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07720:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07720:end -->

<!-- books-review:SF-2026-ARXIV-2606-07726:start -->
SF-2026-ARXIV-2606-07726: fresh comparison read `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` and `books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07726:start -->
Ch66 §§评估声明完整对象; 评估结论相对于分布; Scorer 不是绝对真相
<!-- existing:SF-2026-ARXIV-2606-07726:end -->

<!-- delta:SF-2026-ARXIV-2606-07726:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07726:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07726:end -->

<!-- books-review:SF-2026-ARXIV-2606-07783:start -->
SF-2026-ARXIV-2606-07783: fresh comparison read `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` and `books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07783:start -->
Ch66 §§评估声明完整对象; 评估结论相对于分布; Scorer 不是绝对真相
<!-- existing:SF-2026-ARXIV-2606-07783:end -->

<!-- delta:SF-2026-ARXIV-2606-07783:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07783:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07783:end -->

<!-- books-review:SF-2026-ARXIV-2606-07790:start -->
SF-2026-ARXIV-2606-07790: fresh comparison read `books/part-07-agent/82-multi-agent.md#L10` and `books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07790:start -->
Ch82 §§Coordination Tax; Topology; Coordination Failure; Evaluation
<!-- existing:SF-2026-ARXIV-2606-07790:end -->

<!-- delta:SF-2026-ARXIV-2606-07790:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07790:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07790:end -->

<!-- books-review:SF-2026-ARXIV-2606-07805:start -->
SF-2026-ARXIV-2606-07805: fresh comparison read `books/part-07-agent/82-multi-agent.md#L10` and `books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07805:start -->
Ch82 §§Coordination Tax; Topology; Coordination Failure; Evaluation
<!-- existing:SF-2026-ARXIV-2606-07805:end -->

<!-- delta:SF-2026-ARXIV-2606-07805:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07805:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07805:end -->

<!-- books-review:SF-2026-ARXIV-2606-07808:start -->
SF-2026-ARXIV-2606-07808: fresh comparison read `books/part-06-ai-infrastructure/72-security.md#L10` and `books/part-06-ai-infrastructure/71-multi-tenant.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`. Classification is `partial`.

<!-- existing:SF-2026-ARXIV-2606-07808:start -->
Ch72 §§行为控制权; Supply-chain Integrity; Tool Boundary; Instruction Hierarchy
<!-- existing:SF-2026-ARXIV-2606-07808:end -->

<!-- delta:SF-2026-ARXIV-2606-07808:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07808:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07808:end -->

<!-- books-review:SF-2026-ARXIV-2606-07822:start -->
SF-2026-ARXIV-2606-07822: fresh comparison read `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` and `books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07822:start -->
Ch66 §§评估声明完整对象; 评估结论相对于分布; Scorer 不是绝对真相
<!-- existing:SF-2026-ARXIV-2606-07822:end -->

<!-- delta:SF-2026-ARXIV-2606-07822:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07822:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07822:end -->

<!-- books-review:SF-2026-ARXIV-2606-07833:start -->
SF-2026-ARXIV-2606-07833: fresh comparison read `books/part-06-ai-infrastructure/72-security.md#L10` and `books/part-06-ai-infrastructure/71-multi-tenant.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07833:start -->
Ch72 §§行为控制权; Supply-chain Integrity; Tool Boundary; Instruction Hierarchy
<!-- existing:SF-2026-ARXIV-2606-07833:end -->

<!-- delta:SF-2026-ARXIV-2606-07833:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07833:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07833:end -->

<!-- books-review:SF-2026-ARXIV-2606-07834:start -->
SF-2026-ARXIV-2606-07834: fresh comparison read `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` and `books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07834:start -->
Ch66 §§评估声明完整对象; 评估结论相对于分布; Scorer 不是绝对真相
<!-- existing:SF-2026-ARXIV-2606-07834:end -->

<!-- delta:SF-2026-ARXIV-2606-07834:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07834:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07834:end -->

<!-- books-review:SF-2026-ARXIV-2606-07845:start -->
SF-2026-ARXIV-2606-07845: fresh comparison read `books/part-07-agent/82-multi-agent.md#L10` and `books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07845:start -->
Ch82 §§Coordination Tax; Topology; Coordination Failure; Evaluation
<!-- existing:SF-2026-ARXIV-2606-07845:end -->

<!-- delta:SF-2026-ARXIV-2606-07845:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07845:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07845:end -->

<!-- books-review:SF-2026-ARXIV-2606-07846:start -->
SF-2026-ARXIV-2606-07846: fresh comparison read `books/part-07-agent/81-workflow.md#L10` and `books/part-07-agent/80-reflection.md#L10; books/part-07-agent/82-multi-agent.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07846:start -->
Ch81 §§State Machine; Evaluator-Driven Search; Durable Execution
<!-- existing:SF-2026-ARXIV-2606-07846:end -->

<!-- delta:SF-2026-ARXIV-2606-07846:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07846:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07846:end -->

<!-- books-review:SF-2026-ARXIV-2606-07856:start -->
SF-2026-ARXIV-2606-07856: fresh comparison read `books/part-04-training-system/29-sft.md#L10` and `books/part-04-training-system/28-pretraining.md#L10; books/part-04-training-system/30-lora.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07856:start -->
Ch29 §§SFT 数据质量; Catastrophic forgetting; Evaluation
<!-- existing:SF-2026-ARXIV-2606-07856:end -->

<!-- delta:SF-2026-ARXIV-2606-07856:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07856:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07856:end -->

<!-- books-review:SF-2026-ARXIV-2606-07867:start -->
SF-2026-ARXIV-2606-07867: fresh comparison read `books/part-06-ai-infrastructure/72-security.md#L10` and `books/part-06-ai-infrastructure/71-multi-tenant.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07867:start -->
Ch72 §§行为控制权; Supply-chain Integrity; Tool Boundary; Instruction Hierarchy
<!-- existing:SF-2026-ARXIV-2606-07867:end -->

<!-- delta:SF-2026-ARXIV-2606-07867:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07867:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07867:end -->

<!-- books-review:SF-2026-ARXIV-2606-07874:start -->
SF-2026-ARXIV-2606-07874: fresh comparison read `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` and `books/part-06-ai-infrastructure/65-kai-scheduler.md#L10; books/part-06-ai-infrastructure/67-monitoring.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07874:start -->
Ch66 §§评估声明完整对象; 评估结论相对于分布; Scorer 不是绝对真相
<!-- existing:SF-2026-ARXIV-2606-07874:end -->

<!-- delta:SF-2026-ARXIV-2606-07874:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07874:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07874:end -->

<!-- books-review:SF-2026-ARXIV-2606-07878:start -->
SF-2026-ARXIV-2606-07878: fresh comparison read `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10` and `books/part-05-inference-system/44-decode.md#L10; books/part-05-inference-system/46-continuous-batching.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07878:start -->
Ch45 §§生命周期; 一致性不变量; 连续 Tensor 到 Block 管理
<!-- existing:SF-2026-ARXIV-2606-07878:end -->

<!-- delta:SF-2026-ARXIV-2606-07878:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07878:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07878:end -->

<!-- books-review:SF-2026-ARXIV-2606-07881:start -->
SF-2026-ARXIV-2606-07881: fresh comparison read `books/part-04-training-system/38-pipeline-parallel.md#L10` and `books/part-04-training-system/37-tensor-parallel.md#L10; books/part-04-training-system/39-zero.md#L10`. Classification is `partial`.

<!-- existing:SF-2026-ARXIV-2606-07881:start -->
Ch38 §§Bubble; 异步 Pipeline; 参数版本
<!-- existing:SF-2026-ARXIV-2606-07881:end -->

<!-- delta:SF-2026-ARXIV-2606-07881:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07881:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07881:end -->

<!-- books-review:SF-2026-ARXIV-2606-07889:start -->
SF-2026-ARXIV-2606-07889: fresh comparison read `books/part-06-ai-infrastructure/67-monitoring.md#L10` and `books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-06-ai-infrastructure/68-logging.md#L10`. Classification is `genuinely missing`.

<!-- existing:SF-2026-ARXIV-2606-07889:start -->
Ch67 §§目标与信号; 四层指标; Monitoring 也会改变系统
<!-- existing:SF-2026-ARXIV-2606-07889:end -->

<!-- delta:SF-2026-ARXIV-2606-07889:start -->
Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07889:end -->

Decision: `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-07889:end -->

<!-- books-review:SF-2026-ARXIV-2606-07904:start -->
SF-2026-ARXIV-2606-07904: fresh comparison read `books/part-07-agent/78-tool-calling.md#L10` and `books/part-07-agent/77-memory.md#L10; books/part-07-agent/79-planning.md#L10`. Classification is `already covered`.

<!-- existing:SF-2026-ARXIV-2606-07904:start -->
Ch78 §§Tool Contract; Proposal/authorization/effect; Side-effect Class
<!-- existing:SF-2026-ARXIV-2606-07904:end -->

<!-- delta:SF-2026-ARXIV-2606-07904:start -->
Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- delta:SF-2026-ARXIV-2606-07904:end -->

Decision: `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-07904:end -->

<!-- books-review:SF-2026-ARXIV-2606-07923:start -->
Compared `Larch: Learned Query Optimization for Semantic Predicates` against `books/part-05-inference-system/56-inference-scheduling.md#L358` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07923:start -->
Ch56 已把 KV residency 和 pipeline state 变成可调度成本，但没有 semantic predicate 的逐行 selectivity 学习与精确短路排序。
<!-- existing:SF-2026-ARXIV-2606-07923:end -->

<!-- delta:SF-2026-ARXIV-2606-07923:start -->
Online selectivity learning plus exact per-row ordering makes semantic-predicate token cost query-planner state rather than an opaque LLM charge. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-07923:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07923:end -->

<!-- books-review:SF-2026-ARXIV-2606-07936:start -->
Compared `Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07936:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-07936:end -->

<!-- delta:SF-2026-ARXIV-2606-07936:start -->
Twenty reproducibility fields separate what human judges measured, who judged, and how judgments may be interpreted; this changes the evaluation receipt contract. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07936:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07936:end -->

<!-- books-review:SF-2026-ARXIV-2606-07943:start -->
Compared `Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents` against `books/part-06-ai-infrastructure/72-security.md#L367` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07943:start -->
Ch72 已定义持久 Skill 的 supply-chain lifecycle、admission 和 revocation，但没有位置感知单指令、静默副作用与合法任务联合通过的攻击证据。
<!-- existing:SF-2026-ARXIV-2606-07943:end -->

<!-- delta:SF-2026-ARXIV-2606-07943:start -->
Postcondition-validated payload execution jointly with legitimate-task success changes skill-poisoning evidence from invocation to completed side effect, while position controls stealth and reliability. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-07943:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07943:end -->

<!-- books-review:SF-2026-ARXIV-2606-07950:start -->
Compared `The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning` against `books/part-04-training-system/33-grpo.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07950:start -->
`TRAIN-GRPO` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07950:end -->

<!-- delta:SF-2026-ARXIV-2606-07950:start -->
Confidence, empirical difficulty, and shrinking group advantage become explicit rollout-allocation state used for both resampling and update weighting under fixed compute. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07950:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07950:end -->

<!-- books-review:SF-2026-ARXIV-2606-07957:start -->
Compared `Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path` against `books/part-06-ai-infrastructure/72-security.md#L367` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07957:start -->
Ch72 已定义持久 Skill 的 supply-chain lifecycle、admission 和 revocation，但没有位置感知单指令、静默副作用与合法任务联合通过的攻击证据。
<!-- existing:SF-2026-ARXIV-2606-07957:end -->

<!-- delta:SF-2026-ARXIV-2606-07957:start -->
CSPM rules become tenant-local derived state maintained bidirectionally from catalogue entries and the live asset graph, removing vendor release cadence from the protection critical path. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07957:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07957:end -->

<!-- books-review:SF-2026-ARXIV-2606-07968:start -->
Compared `RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks` against `books/part-06-ai-infrastructure/67-monitoring.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07968:start -->
`PLATFORM-MONITORING` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07968:end -->

<!-- delta:SF-2026-ARXIV-2606-07968:start -->
A generation-time monitor combines recurrence, volume growth, and task progress over consecutive chunks and owns early termination of reasoning-token consumption attacks. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07968:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07968:end -->

<!-- books-review:SF-2026-ARXIV-2606-07970:start -->
Compared `Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks` against `books/part-04-training-system/29-sft.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07970:start -->
`TRAIN-SFT` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07970:end -->

<!-- delta:SF-2026-ARXIV-2606-07970:start -->
Train-time adversarial attack strength becomes an inner-loop robustness control, with parallel execution preserving the stronger full-parameter threat model. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07970:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07970:end -->

<!-- books-review:SF-2026-ARXIV-2606-07992:start -->
Compared `VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation` against `books/part-07-agent/78-tool-calling.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-07992:start -->
`AGENT-MCP` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-07992:end -->

<!-- delta:SF-2026-ARXIV-2606-07992:start -->
Tool errors are an authority-bearing ingress path; mutation across error structure and language changes MCP trust from tool output validation to error-loop admission and containment. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-07992:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-07992:end -->

<!-- books-review:SF-2026-ARXIV-2606-08049:start -->
Compared `SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows` against `books/part-07-agent/81-workflow.md#L159` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08049:start -->
Ch81 已有 split-gated self-evolution asset，但没有以 versioned notebook 为逐步 owner 的 code/NL 局部回退与多模态证据链。
<!-- existing:SF-2026-ARXIV-2606-08049:end -->

<!-- delta:SF-2026-ARXIV-2606-08049:start -->
Versioned notebooks make each reusable step auditable state and let validation gates choose code execution or local natural-language fallback when environments drift. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-08049:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08049:end -->

<!-- books-review:SF-2026-ARXIV-2606-08094:start -->
Compared `vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models` against `books/part-05-inference-system/42-what-happens-during-inference.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08094:start -->
`INFER-REQUEST-LIFECYCLE` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08094:end -->

<!-- delta:SF-2026-ARXIV-2606-08094:start -->
A single C++ runtime owns cached vision-language prefix state, cross-attending action-expert solver steps, portable model bundles, and one request protocol across VLA families. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08094:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08094:end -->

<!-- books-review:SF-2026-ARXIV-2606-08106:start -->
Compared `PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents` against `books/part-07-agent/84-agent-platform.md#L343` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08106:start -->
Ch84 已有 Skill compiler/admission 与 executable evidence，但没有 optional-stopping 下 false-commit-controlled 的统计 acceptor。
<!-- existing:SF-2026-ARXIV-2606-08106:end -->

<!-- delta:SF-2026-ARXIV-2606-08106:start -->
Anytime-valid paired tests move self-evolution authority from noisy score improvement to a false-commit-controlled acceptor that remains valid under optional stopping. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-08106:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08106:end -->

<!-- books-review:SF-2026-ARXIV-2606-08197:start -->
Compared `AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments` against `books/part-04-training-system/36-distributed-training.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08197:start -->
`TRAIN-DISTRIBUTED-TRAINING` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08197:end -->

<!-- delta:SF-2026-ARXIV-2606-08197:start -->
Version grouping, calibration-set semantic alignment, and freshness/participation weighting make staleness and fairness explicit asynchronous federated aggregation state. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08197:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08197:end -->

<!-- books-review:SF-2026-ARXIV-2606-08200:start -->
Compared `Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08200:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-08200:end -->

<!-- delta:SF-2026-ARXIV-2606-08200:start -->
An in-world evaluator actively creates criterion-relevant situations through native dialogue/action, changing evaluation from passive trajectory scoring to coverage-seeking intervention. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- delta:SF-2026-ARXIV-2606-08200:end -->

Decision: `Integrate`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08200:end -->

<!-- books-review:SF-2026-ARXIV-2606-08302:start -->
Compared `HACK++: Towards More Effective Head-Aware Key-Value Compression for Efficient Visual Autoregressive Modeling` against `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08302:start -->
Ch45 已有 workload-semantic retention、variable-rank low-rank compression 与 prefix identity；缺少跨 turn QueryMemory 和 sentinel slot-map 保持行/相位/前缀身份的删除机制。
<!-- existing:SF-2026-ARXIV-2606-08302:end -->

<!-- delta:SF-2026-ARXIV-2606-08302:start -->
Head role, layer, and generation step control separate attention and retained-cache budgets for visual autoregressive decoding instead of applying one global compression ratio. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08302:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08302:end -->

<!-- books-review:SF-2026-ARXIV-2606-08317:start -->
Compared `Architectural Evolution and Selection Framework for Database Systems in AI-Ready Data Platforms` against `books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08317:start -->
Ch57 已把平台定义为 workload-specific identity/state/policy/evidence contract，并以 intent→admission→reconciliation 闭环和 one-size-fits-all failure 约束架构选择；概念性数据库 taxonomy 不新增独立 owner。
<!-- existing:SF-2026-ARXIV-2606-08317:end -->

<!-- delta:SF-2026-ARXIV-2606-08317:start -->
Nine dimensions, workload characterization, constraint filtering, and compatibility scoring make polyglot database choice a reviewable platform decision rather than intuition. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08317:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08317:end -->

<!-- books-review:SF-2026-ARXIV-2606-08340:start -->
Compared `Benchmarking Open-Ended Multi-Agent Coordination in Language Agents` against `books/part-07-agent/82-multi-agent.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08340:start -->
`AGENT-MULTI-AGENT` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08340:end -->

<!-- delta:SF-2026-ARXIV-2606-08340:start -->
A long-horizon world separates individual task reward from coordination reward while controlling communication, role specialization, and coordination difficulty. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08340:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08340:end -->

<!-- books-review:SF-2026-ARXIV-2606-08346:start -->
Compared `CATPO: Critique-Augmented Tree Policy Optimization` against `books/part-04-training-system/33-grpo.md#L10` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08346:start -->
`TRAIN-GRPO` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。
<!-- existing:SF-2026-ARXIV-2606-08346:end -->

<!-- delta:SF-2026-ARXIV-2606-08346:start -->
Tree outcome diversity and policy-reward decorrelation identify low-signal rollout trees; critique-guided grafting repairs all-fail branches before informativeness-weighted updates. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08346:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08346:end -->

<!-- books-review:SF-2026-ARXIV-2606-08348:start -->
Compared `Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses` against `books/part-07-agent/84-agent-platform.md#L343` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08348:start -->
Ch84 已有 Skill compiler/admission 与 executable evidence，但没有 optional-stopping 下 false-commit-controlled 的统计 acceptor。
<!-- existing:SF-2026-ARXIV-2606-08348:end -->

<!-- delta:SF-2026-ARXIV-2606-08348:start -->
Verified trajectories and posterior beliefs turn skills into evidence-bearing lifecycle objects with auditable update and guardrail actions across harnesses. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08348:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08348:end -->

<!-- books-review:SF-2026-ARXIV-2606-08367:start -->
Compared `Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08367:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-08367:end -->

<!-- delta:SF-2026-ARXIV-2606-08367:start -->
Continuously running heterogeneous agent populations, persistent memories, consequential governance, and live exogenous data expose drift and cross-influence absent from exam-style evaluation. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08367:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08367:end -->

<!-- books-review:SF-2026-ARXIV-2606-08372:start -->
Compared `SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC)` against `books/part-06-ai-infrastructure/72-security.md#L367` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08372:start -->
Ch72 已定义持久 Skill 的 supply-chain lifecycle、admission 和 revocation，但没有位置感知单指令、静默副作用与合法任务联合通过的攻击证据。
<!-- existing:SF-2026-ARXIV-2606-08372:end -->

<!-- delta:SF-2026-ARXIV-2606-08372:start -->
A memorization test distinguishes population reconstruction from training-record leakage and maps reconstruction and membership inference to one comparable privacy-risk scale. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08372:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08372:end -->

<!-- books-review:SF-2026-ARXIV-2606-08381:start -->
Compared `Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard` against `books/part-06-ai-infrastructure/66-evaluation-system.md#L335` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08381:start -->
Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。
<!-- existing:SF-2026-ARXIV-2606-08381:end -->

<!-- delta:SF-2026-ARXIV-2606-08381:start -->
Reference-set-relative semantic divergence provides a black-box audit contract for provider-specific alignment when absolute ground truth is unavailable. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08381:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08381:end -->

<!-- books-review:SF-2026-ARXIV-2606-08382:start -->
Compared `STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control` against `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292` and its ROADMAP-adjacent owner.

<!-- existing:SF-2026-ARXIV-2606-08382:start -->
Ch45 已有 workload-semantic retention、variable-rank low-rank compression 与 prefix identity；缺少跨 turn QueryMemory 和 sentinel slot-map 保持行/相位/前缀身份的删除机制。
<!-- existing:SF-2026-ARXIV-2606-08382:end -->

<!-- delta:SF-2026-ARXIV-2606-08382:start -->
Differentiable head/block thresholds, sensitivity-specific factorization, and rank-aware mixed precision turn KV rank into adaptive runtime compression state backed by kernels. 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。
<!-- delta:SF-2026-ARXIV-2606-08382:end -->

Decision: `No Change — Existing Coverage`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.
<!-- books-review:SF-2026-ARXIV-2606-08382:end -->

<!-- existing:SF-2026-ARXIV-2606-08403:start -->
只检查模型看到的普通文本，在输入会经过结构化编码与可信重建时并不充分。恶意 signal 可以在 data layer 里表现为浮点参数，直到 reconstruction layer 才重新成为模型可解释内容；因此 admission receipt 必须同时绑定原始载体、重建函数、重建后的语义与最终 action。普通 text classifier 仍可拦截直接注入，但它不拥有“重建后内容是否可信”的结论。无法验证重建链时，应拒绝 auxiliary channel、canonicalize 后重扫，或要求人工审批。
<!-- existing:SF-2026-ARXIV-2606-08403:end -->

<!-- delta:SF-2026-ARXIV-2606-08403:start -->
结构化浮点载体把恶意信号藏在原始文本视图之外，并在可信重建后才进入模型上下文，迫使安全 owner 同时校验 data layer 与 reconstruction layer。
<!-- delta:SF-2026-ARXIV-2606-08403:end -->

<!-- books-review:SF-2026-ARXIV-2606-08403:start -->
Existing owner proposition: 只检查模型看到的普通文本，在输入会经过结构化编码与可信重建时并不充分。恶意 signal 可以在 data layer 里表现为浮点参数，直到 reconstruction layer 才重新成为模型可解释内容；因此 admission receipt 必须同时绑定原始载体、重建函数、重建后的语义与最终 action。普通 text classifier 仍可拦截直接注入，但它不拥有“重建后内容是否可信”的结论。无法验证重建链时，应拒绝 auxiliary channel、canonicalize 后重扫，或要求人工审批。

Delta: 结构化浮点载体把恶意信号藏在原始文本视图之外，并在可信重建后才进入模型上下文，迫使安全 owner 同时校验 data layer 与 reconstruction layer。

Disposition rationale: Post-write exact-v1 audit found the durable delta in `books/part-06-ai-infrastructure/72-security.md#L1349-L1357` with source-specific proof/non-proof boundary and owner handoff.

Owner `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L1349`; adjacent `books/part-06-ai-infrastructure/71-multi-tenant.md#L84; books/part-06-ai-infrastructure/73-production-best-practice.md#L144`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08403:end -->

<!-- existing:SF-2026-ARXIV-2606-08411:start -->
- AsyncLane（arXiv:2606.08411v1；Status: Experimental）：证据覆盖 lane scheduling、shared-prefix batching、lookahead reuse/cache refresh，以及 LLaDA/Dream 在 GSM8K、MATH、HumanEval、MBPP 等切片；单 H100、batch 1、256/512/1,024-token budgets，不证明多请求公平性或 production SLO，precision 未披露。https://arxiv.org/html/2606.08411v1
<!-- existing:SF-2026-ARXIV-2606-08411:end -->

<!-- delta:SF-2026-ARXIV-2606-08411:start -->
AsyncLane 用 lane tree 把 DLM 的 prefix refinement 与 frontier advancement 解耦，并以 shared-prefix batching、lookahead reuse 与 cache refresh 管理异步依赖。
<!-- delta:SF-2026-ARXIV-2606-08411:end -->

<!-- books-review:SF-2026-ARXIV-2606-08411:start -->
Existing owner proposition: - AsyncLane（arXiv:2606.08411v1；Status: Experimental）：证据覆盖 lane scheduling、shared-prefix batching、lookahead reuse/cache refresh，以及 LLaDA/Dream 在 GSM8K、MATH、HumanEval、MBPP 等切片；单 H100、batch 1、256/512/1,024-token budgets，不证明多请求公平性或 production SLO，precision 未披露。https://arxiv.org/html/2606.08411v1

Delta: AsyncLane 用 lane tree 把 DLM 的 prefix refinement 与 frontier advancement 解耦，并以 shared-prefix batching、lookahead reuse 与 cache refresh 管理异步依赖。

Disposition rationale: Post-write exact-v1 audit found the durable delta in `books/part-05-inference-system/44-decode.md#L254-L275` with source-specific proof/non-proof boundary and owner handoff.

Owner `INFER-DECODE` at `books/part-05-inference-system/44-decode.md#L254`; adjacent `books/part-05-inference-system/43-prefill.md#L367; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L645`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08411:end -->

<!-- existing:SF-2026-ARXIV-2606-08417:start -->
多个 uncertainty scorer 的 supervised ensemble 也只能在有代表性的标签与目标模型访问合同下作为 sensor。Black-box consistency、token probability、reflexive judge 与 claim-level score 观察不同误差面，组合后可能改善 AUROC / calibration，却会引入标签成本、domain shift、grader correlation 与 scorer availability。原始相似度、entropy 或 ensemble output 仍不是概率；必须按 deployment slice 校准，并把 abstain、human escalation 与风险覆盖率作为最终决策输出。
<!-- existing:SF-2026-ARXIV-2606-08417:end -->

<!-- delta:SF-2026-ARXIV-2606-08417:start -->
零参数劣质 sampler 可在非退化 entropy 下优化 gen-PPL，说明单一 scorer predictability 不能充当生成质量，评测必须转向分布差异。
<!-- delta:SF-2026-ARXIV-2606-08417:end -->

<!-- books-review:SF-2026-ARXIV-2606-08417:start -->
Existing owner proposition: 多个 uncertainty scorer 的 supervised ensemble 也只能在有代表性的标签与目标模型访问合同下作为 sensor。Black-box consistency、token probability、reflexive judge 与 claim-level score 观察不同误差面，组合后可能改善 AUROC / calibration，却会引入标签成本、domain shift、grader correlation 与 scorer availability。原始相似度、entropy 或 ensemble output 仍不是概率；必须按 deployment slice 校准，并把 abstain、human escalation 与风险覆盖率作为最终决策输出。

Delta: 零参数劣质 sampler 可在非退化 entropy 下优化 gen-PPL，说明单一 scorer predictability 不能充当生成质量，评测必须转向分布差异。

Disposition rationale: Ch66 已把 proxy、分布差异、scorer blind spot 与不确定性纳入同一 EvalSpec；该 sampler 反例强化既有原则，不建立新 owner。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1268`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L113; books/part-06-ai-infrastructure/67-monitoring.md#L113`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08417:end -->

<!-- existing:SF-2026-ARXIV-2606-08432:start -->
→ same-prefix on-policy distillation
<!-- existing:SF-2026-ARXIV-2606-08432:end -->

<!-- delta:SF-2026-ARXIV-2606-08432:start -->
TRD 把 on-policy distillation 的修复尺度从 token-loss clipping 提升到 teacher-guided trajectory correction，以避免失败 prefix 产生双峰且碎片化的监督。
<!-- delta:SF-2026-ARXIV-2606-08432:end -->

<!-- books-review:SF-2026-ARXIV-2606-08432:start -->
Existing owner proposition: → same-prefix on-policy distillation

Delta: TRD 把 on-policy distillation 的修复尺度从 token-loss clipping 提升到 teacher-guided trajectory correction，以避免失败 prefix 产生双峰且碎片化的监督。

Disposition rationale: Ch29 已拥有 same-prefix on-policy distillation 与 privileged-teacher/student-state 分离；TRD 是 trajectory-correction 分支，不改变 SFT handoff。

Owner `TRAIN-SFT` at `books/part-04-training-system/29-sft.md#L315`; adjacent `books/part-04-training-system/28-pretraining.md#L833; books/part-04-training-system/30-lora.md#L370`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08432:end -->

<!-- existing:SF-2026-ARXIV-2606-08433:start -->
旧 threat model 常把训练和评测 sandbox 看成“非生产环境”：没有客户流量、默认无公网、任务结束即可销毁，
<!-- existing:SF-2026-ARXIV-2606-08433:end -->

<!-- delta:SF-2026-ARXIV-2606-08433:start -->
AI code sandbox 不能用单一总分排序；host attack surface、leakage、stackability、CVE、patch cadence 与 fuzzing posture 必须按 threat model 分轴负责。
<!-- delta:SF-2026-ARXIV-2606-08433:end -->

<!-- books-review:SF-2026-ARXIV-2606-08433:start -->
Existing owner proposition: 旧 threat model 常把训练和评测 sandbox 看成“非生产环境”：没有客户流量、默认无公网、任务结束即可销毁，

Delta: AI code sandbox 不能用单一总分排序；host attack surface、leakage、stackability、CVE、patch cadence 与 fuzzing posture 必须按 threat model 分轴负责。

Disposition rationale: Ch72 已按 threat model 管理 sandbox isolation、attack surface 与 defense-in-depth；六轴比较是审计实例，不形成跨章节新机制。

Owner `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L955`; adjacent `books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L98`; relation `Layering / Dependency`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08433:end -->

<!-- existing:SF-2026-ARXIV-2606-08446:start -->
rollout、redundant rollout 和 parameter refresh，但任何吞吐策略都不能绕过前者。它把“最多容忍几个旧版本”
<!-- existing:SF-2026-ARXIV-2606-08446:end -->

<!-- delta:SF-2026-ARXIV-2606-08446:start -->
Sparrow 把 long-context RL rollout 的稀疏注意力当作训练系统路径，并显式保留 dense teacher refresh 以约束效率与策略漂移。
<!-- delta:SF-2026-ARXIV-2606-08446:end -->

<!-- books-review:SF-2026-ARXIV-2606-08446:start -->
Existing owner proposition: rollout、redundant rollout 和 parameter refresh，但任何吞吐策略都不能绕过前者。它把“最多容忍几个旧版本”

Delta: Sparrow 把 long-context RL rollout 的稀疏注意力当作训练系统路径，并显式保留 dense teacher refresh 以约束效率与策略漂移。

Disposition rationale: Ch33 已拥有 rollout、policy-version freshness 与训练执行效率边界；稀疏 rollout 加 dense refresh 是该控制面的受限实现分支。

Owner `TRAIN-GRPO` at `books/part-04-training-system/33-grpo.md#L835`; adjacent `books/part-04-training-system/32-ppo.md#L284; books/part-04-training-system/34-dpo.md#L283`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08446:end -->

<!-- existing:SF-2026-ARXIV-2606-08476:start -->
静态 sequence sharding 在长度近似均匀、attention kernel 和链路成本稳定时最容易实现；packed long-context training 会同时暴露 token imbalance、kernel efficiency 与 KV communication 三个瓶颈。Context-parallel planner 因而不能只重新分 sequence，也要把 attention tile、worker load 与 KV exchange 放进同一 cost model，并让 authoritative optimizer/checkpoint state 继续由训练拓扑拥有。
<!-- existing:SF-2026-ARXIV-2606-08476:end -->

<!-- delta:SF-2026-ARXIV-2606-08476:start -->
FlashCP 将 context-parallel 的负载均衡、attention kernel 与 KV 通信共同建模，避免静态 sequence sharding 把三类瓶颈分开优化。
<!-- delta:SF-2026-ARXIV-2606-08476:end -->

<!-- books-review:SF-2026-ARXIV-2606-08476:start -->
Existing owner proposition: 静态 sequence sharding 在长度近似均匀、attention kernel 和链路成本稳定时最容易实现；packed long-context training 会同时暴露 token imbalance、kernel efficiency 与 KV communication 三个瓶颈。Context-parallel planner 因而不能只重新分 sequence，也要把 attention tile、worker load 与 KV exchange 放进同一 cost model，并让 authoritative optimizer/checkpoint state 继续由训练拓扑拥有。

Delta: FlashCP 将 context-parallel 的负载均衡、attention kernel 与 KV 通信共同建模，避免静态 sequence sharding 把三类瓶颈分开优化。

Disposition rationale: Post-write exact-v1 audit found the durable delta in `books/part-04-training-system/36-distributed-training.md#L903-L909` with source-specific proof/non-proof boundary and owner handoff.

Owner `TRAIN-DISTRIBUTED-TRAINING` at `books/part-04-training-system/36-distributed-training.md#L903`; adjacent `books/part-04-training-system/35-checkpoint.md#L502; books/part-04-training-system/37-tensor-parallel.md#L305`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08476:end -->

<!-- existing:SF-2026-ARXIV-2606-08483:start -->
联邦个性化会把同一问题推进到 client-local visibility：aggregate acceptance 可能正常，却掩盖少数 client 上的 bias、miscalibration、adaptation failure、OOD 或 alignment erosion。评估合同必须先声明哪些统计允许留在本地、哪些可聚合、哪些只可在受审计的隔离环境中检查，再把 local slice evidence 与 global release decision 分离。否则“平均模型通过”会被误写成“每个个性化模型都安全”。
<!-- existing:SF-2026-ARXIV-2606-08483:end -->

<!-- delta:SF-2026-ARXIV-2606-08483:start -->
consumer health LLM 的 personalization 与版本漂移无法由黑盒单次测量独立归因，评测合同必须记录可观察输入、不可见系统状态与重复测量边界。
<!-- delta:SF-2026-ARXIV-2606-08483:end -->

<!-- books-review:SF-2026-ARXIV-2606-08483:start -->
Existing owner proposition: 联邦个性化会把同一问题推进到 client-local visibility：aggregate acceptance 可能正常，却掩盖少数 client 上的 bias、miscalibration、adaptation failure、OOD 或 alignment erosion。评估合同必须先声明哪些统计允许留在本地、哪些可聚合、哪些只可在受审计的隔离环境中检查，再把 local slice evidence 与 global release decision 分离。否则“平均模型通过”会被误写成“每个个性化模型都安全”。

Delta: consumer health LLM 的 personalization 与版本漂移无法由黑盒单次测量独立归因，评测合同必须记录可观察输入、不可见系统状态与重复测量边界。

Disposition rationale: Ch66 已要求完整 subject identity、重复运行与 client-local/关键 slice；黑盒 consumer-health 测量不能独立归因，正落在既有评测合同。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1018`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L76`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08483:end -->

<!-- existing:SF-2026-ARXIV-2606-08486:start -->
结束条件必须与 sampling、detokenization 和 stream 一致。例如 stop string 可能跨 token boundary，系统不能只检查最后一个 token id。
<!-- existing:SF-2026-ARXIV-2606-08486:end -->

<!-- delta:SF-2026-ARXIV-2606-08486:start -->
TRADE 以共享 audio encoder 的 transducer branch 补齐 Speech LLM 的 frame alignment、streaming decode 与 end-of-utterance 状态。
<!-- delta:SF-2026-ARXIV-2606-08486:end -->

<!-- books-review:SF-2026-ARXIV-2606-08486:start -->
Existing owner proposition: 结束条件必须与 sampling、detokenization 和 stream 一致。例如 stop string 可能跨 token boundary，系统不能只检查最后一个 token id。

Delta: TRADE 以共享 audio encoder 的 transducer branch 补齐 Speech LLM 的 frame alignment、streaming decode 与 end-of-utterance 状态。

Disposition rationale: Ch44 已拥有 decode frontier、termination、detokenization 与 streaming state；speech transducer/frame alignment 是领域化 decode branch，不改写通用 owner。

Owner `INFER-DECODE` at `books/part-05-inference-system/44-decode.md#L178`; adjacent `books/part-05-inference-system/43-prefill.md#L329; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L456`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08486:end -->

<!-- existing:SF-2026-ARXIV-2606-08517:start -->
量化、剪枝或蒸馏可能保持平均准确率，却改变 confidence calibration、prediction-set coverage、set size 与 selective-risk 曲线。发布比较因此需要在同一 workload、slice 和 decision threshold 下同时检查 task quality、risk-coverage、abstention rate、calibration drift 与 runtime benefit；只在压缩后重新调一个阈值，会掩盖 sensor identity 已变化。
<!-- existing:SF-2026-ARXIV-2606-08517:end -->

<!-- delta:SF-2026-ARXIV-2606-08517:start -->
adaptive selective predictor 的部署证明必须联合约束 selected risk、acceptance floor 与 utility，而不能分别挑选阈值后拼接置信区间。
<!-- delta:SF-2026-ARXIV-2606-08517:end -->

<!-- books-review:SF-2026-ARXIV-2606-08517:start -->
Existing owner proposition: 量化、剪枝或蒸馏可能保持平均准确率，却改变 confidence calibration、prediction-set coverage、set size 与 selective-risk 曲线。发布比较因此需要在同一 workload、slice 和 decision threshold 下同时检查 task quality、risk-coverage、abstention rate、calibration drift 与 runtime benefit；只在压缩后重新调一个阈值，会掩盖 sensor identity 已变化。

Delta: adaptive selective predictor 的部署证明必须联合约束 selected risk、acceptance floor 与 utility，而不能分别挑选阈值后拼接置信区间。

Disposition rationale: Ch66 已联合管理 risk-coverage、abstention、threshold 与关键 slice；joint certificate 强化现有 release rule，而非新增控制面。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1701`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L243`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08517:end -->

<!-- existing:SF-2026-ARXIV-2606-08529:start -->
可复现的评估身份至少应写成 `model × benchmark × harness × environment × scorer`。Harness 负责适配与控制流，Environment 负责可执行状态，Scorer 只拥有从轨迹到判断的映射；聚合分数之前必须保存原始 trajectory 与 component-level receipt，才能区分模型退化、adapter drift、工具故障和评分变化。统一协议可以复用执行与观测设施，但每个 adapter 仍需证明语义等价。
<!-- existing:SF-2026-ARXIV-2606-08529:end -->

<!-- delta:SF-2026-ARXIV-2606-08529:start -->
GAIA 控制实验显示 scaffold 本身可显著移动同一模型的得分，因此 capability owner 必须分离 model、scaffold 与 attempt budget。
<!-- delta:SF-2026-ARXIV-2606-08529:end -->

<!-- books-review:SF-2026-ARXIV-2606-08529:start -->
Existing owner proposition: 可复现的评估身份至少应写成 `model × benchmark × harness × environment × scorer`。Harness 负责适配与控制流，Environment 负责可执行状态，Scorer 只拥有从轨迹到判断的映射；聚合分数之前必须保存原始 trajectory 与 component-level receipt，才能区分模型退化、adapter drift、工具故障和评分变化。统一协议可以复用执行与观测设施，但每个 adapter 仍需证明语义等价。

Delta: GAIA 控制实验显示 scaffold 本身可显著移动同一模型的得分，因此 capability owner 必须分离 model、scaffold 与 attempt budget。

Disposition rationale: Ch66 已把 model、harness、environment、scorer 与 raw trajectory 绑定为 evaluation identity；scaffold-induced score movement由该 owner 直接吸收。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L140`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L243`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08529:end -->

<!-- existing:SF-2026-ARXIV-2606-08531:start -->
纯 LLM benchmark 主要测 prompt→completion；Agent workload 还包含工具、状态、orchestration、重试和 runtime policy。评估对象应从 model alias 扩展为 `model + runtime + tool/environment generation`，并用 typed trace 说明哪些路径真正执行。生产 trace 或十几个应用可以暴露新压力，但只是 workload characterization，不能证明样本代表全部 Agent。
<!-- existing:SF-2026-ARXIV-2606-08531:end -->

<!-- delta:SF-2026-ARXIV-2606-08531:start -->
ForesightSafety-SAGE 把 agent 风险从静态 prompt/终局判断扩展为 scenario generation、authority context 与执行轨迹上的多维检查。
<!-- delta:SF-2026-ARXIV-2606-08531:end -->

<!-- books-review:SF-2026-ARXIV-2606-08531:start -->
Existing owner proposition: 纯 LLM benchmark 主要测 prompt→completion；Agent workload 还包含工具、状态、orchestration、重试和 runtime policy。评估对象应从 model alias 扩展为 `model + runtime + tool/environment generation`，并用 typed trace 说明哪些路径真正执行。生产 trace 或十几个应用可以暴露新压力，但只是 workload characterization，不能证明样本代表全部 Agent。

Delta: ForesightSafety-SAGE 把 agent 风险从静态 prompt/终局判断扩展为 scenario generation、authority context 与执行轨迹上的多维检查。

Disposition rationale: Ch66 已把 Agent 评测扩展到 runtime、tool/environment generation、typed trace 与 scenario coverage；VESTA 是安全场景实例。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1835`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L130; books/part-06-ai-infrastructure/67-monitoring.md#L289`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08531:end -->

<!-- existing:SF-2026-ARXIV-2606-08539:start -->
通过内容检查后，agent action 仍需要独立 trust decision。Lexical rule 适合稳定且可枚举的高危模式，semantic judge 可以覆盖措辞变化；两者都只能给出 `allow / warn / block / escalate` 建议，确定性 IAM、tool schema 与 effect-time approval 继续拥有 commit authority。若 semantic memory 接受线上反馈，它必须记录 verdict source、judge/version、scope、expiry 与 rollback，不能让 poisoned feedback 或并发更新静默改变安全策略。
<!-- existing:SF-2026-ARXIV-2606-08539:end -->

<!-- delta:SF-2026-ARXIV-2606-08539:start -->
AgentTrust 按 lexical 与 semantic threat 分流 action decision，并让 allow/warn/block/escalate 的反馈进入可更新 judge，而不是扩张固定规则包。
<!-- delta:SF-2026-ARXIV-2606-08539:end -->

<!-- books-review:SF-2026-ARXIV-2606-08539:start -->
Existing owner proposition: 通过内容检查后，agent action 仍需要独立 trust decision。Lexical rule 适合稳定且可枚举的高危模式，semantic judge 可以覆盖措辞变化；两者都只能给出 `allow / warn / block / escalate` 建议，确定性 IAM、tool schema 与 effect-time approval 继续拥有 commit authority。若 semantic memory 接受线上反馈，它必须记录 verdict source、judge/version、scope、expiry 与 rollback，不能让 poisoned feedback 或并发更新静默改变安全策略。

Delta: AgentTrust 按 lexical 与 semantic threat 分流 action decision，并让 allow/warn/block/escalate 的反馈进入可更新 judge，而不是扩张固定规则包。

Disposition rationale: Post-write exact-v1 audit found the durable delta in `books/part-06-ai-infrastructure/72-security.md#L1349-L1358` with source-specific proof/non-proof boundary and owner handoff.

Owner `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L1349`; adjacent `books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L183`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08539:end -->

<!-- existing:SF-2026-ARXIV-2606-08574:start -->
混合与加权可能需要读取不同信号，并以不同 cadence 变化。更清楚的系统分解是：
<!-- existing:SF-2026-ARXIV-2606-08574:end -->

<!-- delta:SF-2026-ARXIV-2606-08574:start -->
OrderDP 区分 full-data gradient 与 pruning surrogate 的 unbiasedness，并把样本顺序纳入动态数据删减合同。
<!-- delta:SF-2026-ARXIV-2606-08574:end -->

<!-- books-review:SF-2026-ARXIV-2606-08574:start -->
Existing owner proposition: 混合与加权可能需要读取不同信号，并以不同 cadence 变化。更清楚的系统分解是：

Delta: OrderDP 区分 full-data gradient 与 pruning surrogate 的 unbiasedness，并把样本顺序纳入动态数据删减合同。

Disposition rationale: Ch27 已把 select/mix/weight、gradient/loss signal、active set 与 held-out evaluation 建成版本化 data control plane；OrderDP 是 pruning/order 算法分支。

Owner `TRAIN-DATA` at `books/part-04-training-system/27-data.md#L133`; adjacent `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L546; books/part-04-training-system/28-pretraining.md#L833`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08574:end -->

<!-- existing:SF-2026-ARXIV-2606-08590:start -->
一次 incident 随后沿同一 evidence object 连接 `symptom → suspected root cause → detection signal → reproduction → recovery`。origin layer 决定谁拥有修复，detectability 决定需要 metrics、trace、schema validator、fault injection 还是第 66 章的 quality evaluator。这样 `runtime_success = true` 与 `contract_success = false` 可以同时成立，也不会把质量失败伪装成 transport error。
<!-- existing:SF-2026-ARXIV-2606-08590:end -->

<!-- delta:SF-2026-ARXIV-2606-08590:start -->
Kubernetes RCA 将 typed evidence graph、read-only tool collection、bounded traversal 与独立 verdict validation 分开，避免 prompt leakage 冒充诊断增益。
<!-- delta:SF-2026-ARXIV-2606-08590:end -->

<!-- books-review:SF-2026-ARXIV-2606-08590:start -->
Existing owner proposition: 一次 incident 随后沿同一 evidence object 连接 `symptom → suspected root cause → detection signal → reproduction → recovery`。origin layer 决定谁拥有修复，detectability 决定需要 metrics、trace、schema validator、fault injection 还是第 66 章的 quality evaluator。这样 `runtime_success = true` 与 `contract_success = false` 可以同时成立，也不会把质量失败伪装成 transport error。

Delta: Kubernetes RCA 将 typed evidence graph、read-only tool collection、bounded traversal 与独立 verdict validation 分开，避免 prompt leakage 冒充诊断增益。

Disposition rationale: Ch67 已区分 telemetry、typed failure evidence、root-cause hypothesis、reproduction 与 verdict；Kubernetes RCA harness 不取得 monitoring 新 owner。

Owner `PLATFORM-MONITORING` at `books/part-06-ai-infrastructure/67-monitoring.md#L128`; adjacent `books/part-06-ai-infrastructure/66-evaluation-system.md#L1964; books/part-06-ai-infrastructure/68-logging.md#L106`; relation `Layering / Dependency`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08590:end -->

<!-- existing:SF-2026-ARXIV-2606-08610:start -->
自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。
<!-- existing:SF-2026-ARXIV-2606-08610:end -->

<!-- delta:SF-2026-ARXIV-2606-08610:start -->
HARBOR 把 robot RL 自动化定义为 bounded stages、standard commands、persistent artifacts 与 executable gates 的 harness，而非一个长提示词。
<!-- delta:SF-2026-ARXIV-2606-08610:end -->

<!-- books-review:SF-2026-ARXIV-2606-08610:start -->
Existing owner proposition: 自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。

Delta: HARBOR 把 robot RL 自动化定义为 bounded stages、standard commands、persistent artifacts 与 executable gates 的 harness，而非一个长提示词。

Disposition rationale: Ch81 已拥有 canonical DAG、typed mutation、persistent artifact 与 executable gate；robot-RL harness 是同一 workflow contract 的实例。

Owner `AGENT-WORKFLOW` at `books/part-07-agent/81-workflow.md#L104`; adjacent `books/part-07-agent/80-reflection.md#L213; books/part-07-agent/82-multi-agent.md#L509`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08610:end -->

<!-- existing:SF-2026-ARXIV-2606-08615:start -->
本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**
<!-- existing:SF-2026-ARXIV-2606-08615:end -->

<!-- delta:SF-2026-ARXIV-2606-08615:start -->
unbounded streaming video 同时要求 proactive interaction、long-horizon memory 与 real-time processing，形成跨 chunk state retention 与 bounded-latency 的联合合同。
<!-- delta:SF-2026-ARXIV-2606-08615:end -->

<!-- books-review:SF-2026-ARXIV-2606-08615:start -->
Existing owner proposition: 本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**

Delta: unbounded streaming video 同时要求 proactive interaction、long-horizon memory 与 real-time processing，形成跨 chunk state retention 与 bounded-latency 的联合合同。

Disposition rationale: Ch77 已将 runtime persisted state 与参数/KV 区分并负责跨段保留、压缩、检索与遗忘；streaming video 只新增 workload 压力。

Owner `AGENT-MEMORY` at `books/part-07-agent/77-memory.md#L14`; adjacent `books/part-07-agent/76-rag.md#L162; books/part-07-agent/78-tool-calling.md#L313`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08615:end -->

<!-- existing:SF-2026-ARXIV-2606-08625:start -->
alternative 判错。因此 rubric 是有 owner、version、适用域、priority/dependency、holdout 与审批边界的
<!-- existing:SF-2026-ARXIV-2606-08625:end -->

<!-- delta:SF-2026-ARXIV-2606-08625:start -->
rubric 随 chat、reasoning 与 agent 范式演化，评价单位从 holistic output 转为可追踪的 structured criteria 与行为约束。
<!-- delta:SF-2026-ARXIV-2606-08625:end -->

<!-- books-review:SF-2026-ARXIV-2606-08625:start -->
Existing owner proposition: alternative 判错。因此 rubric 是有 owner、version、适用域、priority/dependency、holdout 与审批边界的

Delta: rubric 随 chat、reasoning 与 agent 范式演化，评价单位从 holistic output 转为可追踪的 structured criteria 与行为约束。

Disposition rationale: Ch66 已把 rubric formation、atomic criterion execution、ranking 与版本/审批边界分层；rubric 演化综述不改变该 owner。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1372`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L289`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08625:end -->

<!-- existing:SF-2026-ARXIV-2606-08635:start -->
- Mix-Quant（phase-aware precision 与 compatible KV handoff；Status: Experimental）:
<!-- existing:SF-2026-ARXIV-2606-08635:end -->

<!-- delta:SF-2026-ARXIV-2606-08635:start -->
SpectrumKV 将 PD 之间的 KV 传输从 token keep/drop 二元决策改为 per-token mixed precision，使网络字节、量化误差与重算成为同一控制面。
<!-- delta:SF-2026-ARXIV-2606-08635:end -->

<!-- books-review:SF-2026-ARXIV-2606-08635:start -->
Existing owner proposition: - Mix-Quant（phase-aware precision 与 compatible KV handoff；Status: Experimental）:

Delta: SpectrumKV 将 PD 之间的 KV 传输从 token keep/drop 二元决策改为 per-token mixed precision，使网络字节、量化误差与重算成为同一控制面。

Disposition rationale: Post-write exact-v1 audit found the durable delta in `books/part-05-inference-system/55-pd-disaggregation.md#L444-L450` with source-specific proof/non-proof boundary and owner handoff.

Owner `INFER-PD-DISAGGREGATION` at `books/part-05-inference-system/55-pd-disaggregation.md#L444`; adjacent `books/part-05-inference-system/54-gpu-memory.md#L359; books/part-05-inference-system/56-inference-scheduling.md#L758`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08635:end -->

<!-- existing:SF-2026-ARXIV-2606-08661:start -->
模型拒绝、解释或声称“没有修改”仍只是语言层 observation；coding agent 可能已经改写文件、startup hook、依赖或运行环境。Effect Gate 应检查 canonical tool trace、runtime output、filesystem/artifact diff 与预先声明的 executable predicate，并把 partial effect、rollback 与残留状态分别记录。回复文本可以作为 intent sensor，却不能证明副作用没有发生。
<!-- existing:SF-2026-ARXIV-2606-08661:end -->

<!-- delta:SF-2026-ARXIV-2606-08661:start -->
Data Agent 把数据库执行、外部数据资源与 agent reasoning 三个攻击面串联，安全 owner 必须覆盖 query authority、tool side effects 与 evidence provenance。
<!-- delta:SF-2026-ARXIV-2606-08661:end -->

<!-- books-review:SF-2026-ARXIV-2606-08661:start -->
Existing owner proposition: 模型拒绝、解释或声称“没有修改”仍只是语言层 observation；coding agent 可能已经改写文件、startup hook、依赖或运行环境。Effect Gate 应检查 canonical tool trace、runtime output、filesystem/artifact diff 与预先声明的 executable predicate，并把 partial effect、rollback 与残留状态分别记录。回复文本可以作为 intent sensor，却不能证明副作用没有发生。

Delta: Data Agent 把数据库执行、外部数据资源与 agent reasoning 三个攻击面串联，安全 owner 必须覆盖 query authority、tool side effects 与 evidence provenance。

Disposition rationale: Ch72 已要求 tool/database action 经过 authority、effect receipt、provenance 与 fail-closed control；Data Agent 的三攻击面属于既有分层。

Owner `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L562`; adjacent `books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L183`; relation `Layering / Dependency`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08661:end -->

<!-- existing:SF-2026-ARXIV-2606-08671:start -->
把 skill 当作一段可直接覆盖的文本，在任务稳定、修改可人工审阅时足够简单；持续演化后，latest-only state 会丢失修改原因、被拒方案、evaluation 与回退点。Reflection owner 应把每次 revision 记录为 `proposal → evidence → decision → accepted/rejected → successor`，并区分当前 run 的 improvement state、可复用 skill 与第 77 章长期 Memory。
<!-- existing:SF-2026-ARXIV-2606-08671:end -->

<!-- delta:SF-2026-ARXIV-2606-08671:start -->
SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。
<!-- delta:SF-2026-ARXIV-2606-08671:end -->

<!-- books-review:SF-2026-ARXIV-2606-08671:start -->
Existing owner proposition: 把 skill 当作一段可直接覆盖的文本，在任务稳定、修改可人工审阅时足够简单；持续演化后，latest-only state 会丢失修改原因、被拒方案、evaluation 与回退点。Reflection owner 应把每次 revision 记录为 `proposal → evidence → decision → accepted/rejected → successor`，并区分当前 run 的 improvement state、可复用 skill 与第 77 章长期 Memory。

Delta: SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。

Disposition rationale: Post-write exact-v1 audit found the durable delta in `books/part-07-agent/80-reflection.md#L303-L309` with source-specific proof/non-proof boundary and owner handoff.

Owner `AGENT-REFLECTION` at `books/part-07-agent/80-reflection.md#L303`; adjacent `books/part-07-agent/79-planning.md#L326; books/part-07-agent/81-workflow.md#L714`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08671:end -->

<!-- existing:SF-2026-ARXIV-2606-08679:start -->
**Leaderboard-first。** 先选公开 benchmark，再把高分当作产品目标。替代方案是先写 intended use 与 failure taxonomy，再选择或构造 suites。
<!-- existing:SF-2026-ARXIV-2606-08679:end -->

<!-- delta:SF-2026-ARXIV-2606-08679:start -->
leaderboard 必须传播 task-level 不确定性并输出 rank intervals，而不是把多任务均值压成确定名次。
<!-- delta:SF-2026-ARXIV-2606-08679:end -->

<!-- books-review:SF-2026-ARXIV-2606-08679:start -->
Existing owner proposition: **Leaderboard-first。** 先选公开 benchmark，再把高分当作产品目标。替代方案是先写 intended use 与 failure taxonomy，再选择或构造 suites。

Delta: leaderboard 必须传播 task-level 不确定性并输出 rank intervals，而不是把多任务均值压成确定名次。

Disposition rationale: Ch66 已拒绝 leaderboard-first/average-only，并保留 task slice 与 uncertainty；rank interval 是既有 aggregation contract 的实现。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1807`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L291`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08679:end -->

<!-- existing:SF-2026-ARXIV-2606-08702:start -->
+ supersedes / conflicts-with relation
<!-- existing:SF-2026-ARXIV-2606-08702:end -->

<!-- delta:SF-2026-ARXIV-2606-08702:start -->
ConMem 显式建模 memory-skill relation，并从 noisy trajectories 中选择结构化记忆以支持 training-free multi-agent adaptation。
<!-- delta:SF-2026-ARXIV-2606-08702:end -->

<!-- books-review:SF-2026-ARXIV-2606-08702:start -->
Existing owner proposition: + supersedes / conflicts-with relation

Delta: ConMem 显式建模 memory-skill relation，并从 noisy trajectories 中选择结构化记忆以支持 training-free multi-agent adaptation。

Disposition rationale: Ch77 已拥有结构化 memory、关系边、冲突/supersedes 语义与受限 admission；ConMem 的 memory-skill selection 是训练免分支。

Owner `AGENT-MEMORY` at `books/part-07-agent/77-memory.md#L703`; adjacent `books/part-07-agent/76-rag.md#L432; books/part-07-agent/78-tool-calling.md#L314`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08702:end -->

<!-- existing:SF-2026-ARXIV-2606-08755:start -->
History 增加可解释性与 rollback，也会累积陈旧分支、冲突技能和 compaction 成本。新 revision 只有在独立 evaluation 改善目标任务且不破坏保留 slice 时才提交；失败时回退到上一个 accepted version。Ch80 拥有 revision/evaluation/rejection 语义，Ch81 拥有 durable execution 与并发提交，第 77 章拥有跨任务 memory admission。
<!-- existing:SF-2026-ARXIV-2606-08755:end -->

<!-- delta:SF-2026-ARXIV-2606-08755:start -->
skill generation 与 policy optimization 必须共同验证新 skill 的 usefulness，避免 skill bank 只积累未经行为结果校验的文本程序。
<!-- delta:SF-2026-ARXIV-2606-08755:end -->

<!-- books-review:SF-2026-ARXIV-2606-08755:start -->
Existing owner proposition: History 增加可解释性与 rollback，也会累积陈旧分支、冲突技能和 compaction 成本。新 revision 只有在独立 evaluation 改善目标任务且不破坏保留 slice 时才提交；失败时回退到上一个 accepted version。Ch80 拥有 revision/evaluation/rejection 语义，Ch81 拥有 durable execution 与并发提交，第 77 章拥有跨任务 memory admission。

Delta: skill generation 与 policy optimization 必须共同验证新 skill 的 usefulness，避免 skill bank 只积累未经行为结果校验的文本程序。

Disposition rationale: Ch80 已要求 skill revision 记录 evidence、accept/reject、独立 evaluation 与 rollback；联合 skill/policy 优化验证同一原则。

Owner `AGENT-REFLECTION` at `books/part-07-agent/80-reflection.md#L274`; adjacent `books/part-07-agent/79-planning.md#L286; books/part-07-agent/81-workflow.md#L728`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08755:end -->

<!-- existing:SF-2026-ARXIV-2606-08761:start -->
纯 W4A4 用更复杂的 intra-SM mapping 换高 batch 吞吐；低 batch、不同 GPU 或 kernel 未覆盖时，FP16、W4A16、W4A8 或 mixed fallback 仍合理。作者观察到 A100 在 batch≥64 才恢复优势，说明 benchmark batch 不能被误写为并发 SLO。Ch54 拥有 precision-residency identity，Ch49 拥有 runtime integration，Ch56 拥有 continuous batching 与请求调度。
<!-- existing:SF-2026-ARXIV-2606-08761:end -->

<!-- delta:SF-2026-ARXIV-2606-08761:start -->
APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。
<!-- delta:SF-2026-ARXIV-2606-08761:end -->

<!-- books-review:SF-2026-ARXIV-2606-08761:start -->
Existing owner proposition: 纯 W4A4 用更复杂的 intra-SM mapping 换高 batch 吞吐；低 batch、不同 GPU 或 kernel 未覆盖时，FP16、W4A16、W4A8 或 mixed fallback 仍合理。作者观察到 A100 在 batch≥64 才恢复优势，说明 benchmark batch 不能被误写为并发 SLO。Ch54 拥有 precision-residency identity，Ch49 拥有 runtime integration，Ch56 拥有 continuous batching 与请求调度。

Delta: APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。

Disposition rationale: Post-write exact-v1 audit found the durable delta in `books/part-05-inference-system/54-gpu-memory.md#L423-L429` with source-specific proof/non-proof boundary and owner handoff.

Owner `INFER-GPU-MEMORY` at `books/part-05-inference-system/54-gpu-memory.md#L423`; adjacent `books/part-05-inference-system/53-kserve-llm.md#L168; books/part-05-inference-system/55-pd-disaggregation.md#L409`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08761:end -->

<!-- existing:SF-2026-ARXIV-2606-08769:start -->
某些任务无法为每个请求即时获得 ground truth，因此不能简单把语义错误重新编码成另一个实时 `error_rate`。平台通常组合离线标注集、规则与 deterministic checks、抽样 human review、judge、用户反馈和延迟到达的业务 outcome，并为不同证据保留 provenance 与不确定性。高风险 policy failure 还应作为 hard gate，而不是被大量正常请求在平均值中抵消。
<!-- existing:SF-2026-ARXIV-2606-08769:end -->

<!-- delta:SF-2026-ARXIV-2606-08769:start -->
RadOT-Eval 将 radiology generation 的 omission、hallucination、polarity、location、uncertainty 与 temporal error 映射为可审计 structured-evidence transport。
<!-- delta:SF-2026-ARXIV-2606-08769:end -->

<!-- books-review:SF-2026-ARXIV-2606-08769:start -->
Existing owner proposition: 某些任务无法为每个请求即时获得 ground truth，因此不能简单把语义错误重新编码成另一个实时 `error_rate`。平台通常组合离线标注集、规则与 deterministic checks、抽样 human review、judge、用户反馈和延迟到达的业务 outcome，并为不同证据保留 provenance 与不确定性。高风险 policy failure 还应作为 hard gate，而不是被大量正常请求在平均值中抵消。

Delta: RadOT-Eval 将 radiology generation 的 omission、hallucination、polarity、location、uncertainty 与 temporal error 映射为可审计 structured-evidence transport。

Disposition rationale: Ch66 已拥有 semantic-success taxonomy、per-example evidence 与 domain-specific rubric；radiology error transport 是领域实例。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L74`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L113`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08769:end -->

<!-- existing:SF-2026-ARXIV-2606-08779:start -->
优先路径仍是避免过度 SFT；base-anchored fusion 或 attribution-guided neuron reset 只能作为修复分支，因为它们可能损失已学能力并引入新的 checkpoint lineage。修复后必须重新跑 SFT retention、RL gain 与 agentic task Gate。Ch31 拥有 SFT→RL handoff 与 rollout distribution，Ch32 拥有 PPO update contract，checkpoint/version identity 仍由 Ch35 冻结。
<!-- existing:SF-2026-ARXIV-2606-08779:end -->

<!-- delta:SF-2026-ARXIV-2606-08779:start -->
训练 engine 与推理 engine 的 discrepancy 会使 RL objective 与实际 rollout distribution 脱节，post-training 必须记录 sampler/implementation identity。
<!-- delta:SF-2026-ARXIV-2606-08779:end -->

<!-- books-review:SF-2026-ARXIV-2606-08779:start -->
Existing owner proposition: 优先路径仍是避免过度 SFT；base-anchored fusion 或 attribution-guided neuron reset 只能作为修复分支，因为它们可能损失已学能力并引入新的 checkpoint lineage。修复后必须重新跑 SFT retention、RL gain 与 agentic task Gate。Ch31 拥有 SFT→RL handoff 与 rollout distribution，Ch32 拥有 PPO update contract，checkpoint/version identity 仍由 Ch35 冻结。

Delta: 训练 engine 与推理 engine 的 discrepancy 会使 RL objective 与实际 rollout distribution 脱节，post-training 必须记录 sampler/implementation identity。

Disposition rationale: Ch31 已将 rollout probability、policy/checkpoint version 与 training/inference runtime identity绑定；engine discrepancy 是既有 RLHF handoff failure。

Owner `TRAIN-RLHF` at `books/part-04-training-system/31-rlhf.md#L420`; adjacent `books/part-04-training-system/30-lora.md#L419; books/part-04-training-system/32-ppo.md#L378`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08779:end -->

<!-- existing:SF-2026-ARXIV-2606-08790:start -->
本章的核心判断是：**模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。**
<!-- existing:SF-2026-ARXIV-2606-08790:end -->

<!-- delta:SF-2026-ARXIV-2606-08790:start -->
RAILS 把 delegated obligation、verification、liability 与 settlement action 组合成 agent commerce 的 clearing contract，而不把支付成功等同于任务履约。
<!-- delta:SF-2026-ARXIV-2606-08790:end -->

<!-- books-review:SF-2026-ARXIV-2606-08790:start -->
Existing owner proposition: 本章的核心判断是：**模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。**

Delta: RAILS 把 delegated obligation、verification、liability 与 settlement action 组合成 agent commerce 的 clearing contract，而不把支付成功等同于任务履约。

Disposition rationale: Ch78 已拥有 delegated tool intent、typed schema、authorization、side-effect 与 outcome receipt；commerce settlement 是其业务协议层，不新增核心 owner。

Owner `AGENT-TOOL-CALLING` at `books/part-07-agent/78-tool-calling.md#L14`; adjacent `books/part-07-agent/77-memory.md#L1167; books/part-07-agent/79-planning.md#L284`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08790:end -->

<!-- existing:SF-2026-ARXIV-2606-08806:start -->
这些责任不是要求所有系统一开始就采用最重的平台。低流量、低风险 PoC 可以使用简单实现，但必须明确哪些保证尚未建立。生产化的关键不是组件数量，而是每项风险是否有 owner、evidence、failure policy 和 rollback path。
<!-- existing:SF-2026-ARXIV-2606-08806:end -->

<!-- delta:SF-2026-ARXIV-2606-08806:start -->
AI-generated test artifacts 需要 provenance、policy checks、human approval 与 audit trail 的治理层，生成速度不能替代测试资产的责任链。
<!-- delta:SF-2026-ARXIV-2606-08806:end -->

<!-- books-review:SF-2026-ARXIV-2606-08806:start -->
Existing owner proposition: 这些责任不是要求所有系统一开始就采用最重的平台。低流量、低风险 PoC 可以使用简单实现，但必须明确哪些保证尚未建立。生产化的关键不是组件数量，而是每项风险是否有 owner、evidence、failure policy 和 rollback path。

Delta: AI-generated test artifacts 需要 provenance、policy checks、human approval 与 audit trail 的治理层，生成速度不能替代测试资产的责任链。

Disposition rationale: Ch73 已拥有 provenance、policy、approval、release/rollback 与 audit obligations；AI-generated tests 是 production artifact 的受限类别。

Owner `PLATFORM-PRODUCTION` at `books/part-06-ai-infrastructure/73-production-best-practice.md#L45`; adjacent `books/part-06-ai-infrastructure/72-security.md#L1047; books/part-07-agent/74-prompt.md#L189`; relation `Layering / Dependency`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08806:end -->

<!-- existing:SF-2026-ARXIV-2606-08813:start -->
原始 RAG 工作把 parametric generator 与 non-parametric dense index 结合。工程系统进一步拆成 ingestion、index、query、rerank 和 context assembly。
<!-- existing:SF-2026-ARXIV-2606-08813:end -->

<!-- delta:SF-2026-ARXIV-2606-08813:start -->
HNTL 用 hierarchical no-pointer tangent-local layout 降低 ANN graph 的 pointer tax 与不规则访存，把候选生成的数据布局与 CPU pipeline 一起优化。
<!-- delta:SF-2026-ARXIV-2606-08813:end -->

<!-- books-review:SF-2026-ARXIV-2606-08813:start -->
Existing owner proposition: 原始 RAG 工作把 parametric generator 与 non-parametric dense index 结合。工程系统进一步拆成 ingestion、index、query、rerank 和 context assembly。

Delta: HNTL 用 hierarchical no-pointer tangent-local layout 降低 ANN graph 的 pointer tax 与不规则访存，把候选生成的数据布局与 CPU pipeline 一起优化。

Disposition rationale: Ch76 已拥有 ingestion/index/candidate construction、index identity 与 retrieval pipeline；HNTL 是 CPU ANN index-layout implementation branch。

Owner `AGENT-RAG` at `books/part-07-agent/76-rag.md#L33`; adjacent `books/part-07-agent/75-context.md#L290; books/part-07-agent/77-memory.md#L1188`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08813:end -->

<!-- existing:SF-2026-ARXIV-2606-08831:start -->
`first error` 不是第一句看起来奇怪的 reasoning text，而是最早能由 environment state diff、tool result、test
<!-- existing:SF-2026-ARXIV-2606-08831:end -->

<!-- delta:SF-2026-ARXIV-2606-08831:start -->
multi-step reasoning 的 factuality error 具有 ancestor-conditioned DAG 结构，conformal control 不能把 node-wise error 简单累加。
<!-- delta:SF-2026-ARXIV-2606-08831:end -->

<!-- books-review:SF-2026-ARXIV-2606-08831:start -->
Existing owner proposition: `first error` 不是第一句看起来奇怪的 reasoning text，而是最早能由 environment state diff、tool result、test

Delta: multi-step reasoning 的 factuality error 具有 ancestor-conditioned DAG 结构，conformal control 不能把 node-wise error 简单累加。

Disposition rationale: Ch66 已拥有 trajectory/first-error attribution、graph-conditioned evidence 与 conformal uncertainty；DAG factuality control 复用该原则。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1463`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L138; books/part-06-ai-infrastructure/67-monitoring.md#L275`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08831:end -->

<!-- existing:SF-2026-ARXIV-2606-08840:start -->
总体平均会把局部灾难隐藏在高频正常样本中。Evaluation System 应同时保存 per-example results、总体聚合和关键 slices：
<!-- existing:SF-2026-ARXIV-2606-08840:end -->

<!-- delta:SF-2026-ARXIV-2606-08840:start -->
code model 的 pass rate 必须按语言、题型与 execution failure mode 分层，aggregate pass rate 会掩盖可部署性边界。
<!-- delta:SF-2026-ARXIV-2606-08840:end -->

<!-- books-review:SF-2026-ARXIV-2606-08840:start -->
Existing owner proposition: 总体平均会把局部灾难隐藏在高频正常样本中。Evaluation System 应同时保存 per-example results、总体聚合和关键 slices：

Delta: code model 的 pass rate 必须按语言、题型与 execution failure mode 分层，aggregate pass rate 会掩盖可部署性边界。

Disposition rationale: Ch66 已要求 per-example evidence、language/task/risk slices 与 execution failure taxonomy；aggregate pass-rate 分解直接落入现有合同。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L170`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L243`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08840:end -->

<!-- existing:SF-2026-ARXIV-2606-08867:start -->
本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**
<!-- existing:SF-2026-ARXIV-2606-08867:end -->

<!-- delta:SF-2026-ARXIV-2606-08867:start -->
100M-user support agent 把离线 evaluation、context engineering、training 与 online measurement 组成闭环，单一模型分数不代表生产 readiness。
<!-- delta:SF-2026-ARXIV-2606-08867:end -->

<!-- books-review:SF-2026-ARXIV-2606-08867:start -->
Existing owner proposition: 本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**

Delta: 100M-user support agent 把离线 evaluation、context engineering、training 与 online measurement 组成闭环，单一模型分数不代表生产 readiness。

Disposition rationale: Ch84 已把 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy 组成平台闭环；100M-user case 不改变 ownership。

Owner `AGENT-PLATFORM` at `books/part-07-agent/84-agent-platform.md#L14`; adjacent `books/part-07-agent/83-mcp.md#L212`; relation `Layering / Dependency`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08867:end -->

<!-- existing:SF-2026-ARXIV-2606-08869:start -->
一次 incident 随后沿同一 evidence object 连接 `symptom → suspected root cause → detection signal → reproduction → recovery`。origin layer 决定谁拥有修复，detectability 决定需要 metrics、trace、schema validator、fault injection 还是第 66 章的 quality evaluator。这样 `runtime_success = true` 与 `contract_success = false` 可以同时成立，也不会把质量失败伪装成 transport error。
<!-- existing:SF-2026-ARXIV-2606-08869:end -->

<!-- delta:SF-2026-ARXIV-2606-08869:start -->
dynamic cloud-edge control loop 需要把变动 node set 与 query 编码成低延迟 semantic state，而不是只收集 raw counters。
<!-- delta:SF-2026-ARXIV-2606-08869:end -->

<!-- books-review:SF-2026-ARXIV-2606-08869:start -->
Existing owner proposition: 一次 incident 随后沿同一 evidence object 连接 `symptom → suspected root cause → detection signal → reproduction → recovery`。origin layer 决定谁拥有修复，detectability 决定需要 metrics、trace、schema validator、fault injection 还是第 66 章的 quality evaluator。这样 `runtime_success = true` 与 `contract_success = false` 可以同时成立，也不会把质量失败伪装成 transport error。

Delta: dynamic cloud-edge control loop 需要把变动 node set 与 query 编码成低延迟 semantic state，而不是只收集 raw counters。

Disposition rationale: Ch67 已把 observed state、typed evidence 与 control-loop signal分开，并将 action authority留给 scheduler/evaluator；semantic estimator 是 sensor 分支。

Owner `PLATFORM-MONITORING` at `books/part-06-ai-infrastructure/67-monitoring.md#L128`; adjacent `books/part-06-ai-infrastructure/66-evaluation-system.md#L2123; books/part-06-ai-infrastructure/68-logging.md#L105`; relation `Layering / Dependency`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08869:end -->

<!-- existing:SF-2026-ARXIV-2606-08891:start -->
Quantization 只有与明确的 graph mapping、可用 kernels 和目标硬件对齐，必要时再进行 structural rewrite，才可能把更少 bytes 转化为更低单步成本；in-flight batching 和 paged KV 则管理持续到来的 request state。
<!-- existing:SF-2026-ARXIV-2606-08891:end -->

<!-- delta:SF-2026-ARXIV-2606-08891:start -->
PALUTE 用 processing-in-memory lookup table 同时吸收 quantized GEMM 的 dequantization 与 nonlinear operator 成本，改变 edge inference 的 data-movement owner。
<!-- delta:SF-2026-ARXIV-2606-08891:end -->

<!-- books-review:SF-2026-ARXIV-2606-08891:start -->
Existing owner proposition: Quantization 只有与明确的 graph mapping、可用 kernels 和目标硬件对齐，必要时再进行 structural rewrite，才可能把更少 bytes 转化为更低单步成本；in-flight batching 和 paged KV 则管理持续到来的 request state。

Delta: PALUTE 用 processing-in-memory lookup table 同时吸收 quantized GEMM 的 dequantization 与 nonlinear operator 成本，改变 edge inference 的 data-movement owner。

Disposition rationale: Ch49 已拥有 graph/operator 到 kernel/accelerator 的执行映射及 data-movement contract；PIM lookup table 是 backend alternative。

Owner `INFER-TENSORRT-LLM` at `books/part-05-inference-system/49-tensorrt-llm.md#L987`; adjacent `books/part-05-inference-system/48-speculative-decoding.md#L711; books/part-05-inference-system/50-vllm.md#L379`; relation `Alternative Branch`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08891:end -->

<!-- existing:SF-2026-ARXIV-2606-08892:start -->
budget 与 action verifier，并把 CoT signal 与 output inspection、least privilege、sandbox、typed authorization、
<!-- existing:SF-2026-ARXIV-2606-08892:end -->

<!-- delta:SF-2026-ARXIV-2606-08892:start -->
Diffuse AI Control 针对长时段、fuzzy-task sabotage 把控制证据分散到多次任务与审计预算，而非依赖单次可验证 outcome。
<!-- delta:SF-2026-ARXIV-2606-08892:end -->

<!-- books-review:SF-2026-ARXIV-2606-08892:start -->
Existing owner proposition: budget 与 action verifier，并把 CoT signal 与 output inspection、least privilege、sandbox、typed authorization、

Delta: Diffuse AI Control 针对长时段、fuzzy-task sabotage 把控制证据分散到多次任务与审计预算，而非依赖单次可验证 outcome。

Disposition rationale: Ch72 已区分 CoT sensor、monitorability、authorization 与 outcome safety，并组合 budget/action verifier；diffuse long-horizon control 复用此分层。

Owner `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L298`; adjacent `books/part-06-ai-infrastructure/71-multi-tenant.md#L139; books/part-06-ai-infrastructure/73-production-best-practice.md#L134`; relation `Layering / Dependency`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08892:end -->

<!-- existing:SF-2026-ARXIV-2606-08893:start -->
**Judge-as-truth。** 用一个 model judge 替代所有人工与 verifier。替代方案是多证据校准、顺序随机化、disagreement 分析和高风险人工复核。
<!-- existing:SF-2026-ARXIV-2606-08893:end -->

<!-- delta:SF-2026-ARXIV-2606-08893:start -->
cheap reward-hacking detector 用 trajectory embedding 与 metadata/reward distance 近似替代昂贵 LLM judge，但其清洗 split 与阈值不能外推为通用证明。
<!-- delta:SF-2026-ARXIV-2606-08893:end -->

<!-- books-review:SF-2026-ARXIV-2606-08893:start -->
Existing owner proposition: **Judge-as-truth。** 用一个 model judge 替代所有人工与 verifier。替代方案是多证据校准、顺序随机化、disagreement 分析和高风险人工复核。

Delta: cheap reward-hacking detector 用 trajectory embedding 与 metadata/reward distance 近似替代昂贵 LLM judge，但其清洗 split 与阈值不能外推为通用证明。

Disposition rationale: Ch66 已将 judge/detector限定为需校准的 sensor，并保存 split、threshold、uncertainty 与独立 verifier；cheap detector 不改变 truth owner。

Owner `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1811`; adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L241`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-08893:end -->

<!-- existing:SF-2026-ARXIV-2606-08919:start -->
Owner `AGENT-WORKFLOW` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-08919:end -->

<!-- delta:SF-2026-ARXIV-2606-08919:start -->
人工审批不是无限 oracle；guard 的 escalation policy 必须把 reviewer 分歧、疲劳与 flooding 下的有限 attention 当作可耗尽资源。
<!-- delta:SF-2026-ARXIV-2606-08919:end -->

<!-- books-review:SF-2026-ARXIV-2606-08919:start -->
Owner `AGENT-WORKFLOW`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08919:end -->

<!-- existing:SF-2026-ARXIV-2606-08950:start -->
Owner `AGENT-RAG` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-08950:end -->

<!-- delta:SF-2026-ARXIV-2606-08950:start -->
向量数据库的 insertion、indexing、query 与 mixed read/write 生命周期必须同 storage hierarchy、broadcast-gather 与 partitioning 一起评估；增加 core/node 可因协调瓶颈反向降低吞吐。
<!-- delta:SF-2026-ARXIV-2606-08950:end -->

<!-- books-review:SF-2026-ARXIV-2606-08950:start -->
Owner `AGENT-RAG`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08950:end -->

<!-- existing:SF-2026-ARXIV-2606-08960:start -->
Owner `PLATFORM-EVALUATION-SYSTEM` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-08960:end -->

<!-- delta:SF-2026-ARXIV-2606-08960:start -->
benchmark verifier 应通过 hacker→fixer→solver 的闭环迭代：攻击发现 exploit、修补拒绝 exploit、solver 防止补丁把合法解一并拒绝。
<!-- delta:SF-2026-ARXIV-2606-08960:end -->

<!-- books-review:SF-2026-ARXIV-2606-08960:start -->
Owner `PLATFORM-EVALUATION-SYSTEM`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-08960:end -->

<!-- existing:SF-2026-ARXIV-2606-09005:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09005:end -->

<!-- delta:SF-2026-ARXIV-2606-09005:start -->
RAG prompt assembly 必须把 document-authored metadata/provenance 视为 data 而非 policy，避免不可信文档在同一自然语言 channel 中冒充 control signal。
<!-- delta:SF-2026-ARXIV-2606-09005:end -->

<!-- books-review:SF-2026-ARXIV-2606-09005:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09005:end -->

<!-- existing:SF-2026-ARXIV-2606-09061:start -->
Owner `INFER-SCHEDULING` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09061:end -->

<!-- delta:SF-2026-ARXIV-2606-09061:start -->
chunked-prefill scheduler 需联合持有 request age、remaining prefill work、predicted latency 与 active-prefill cap，而不只用 arrival order 或 static token budget。
<!-- delta:SF-2026-ARXIV-2606-09061:end -->

<!-- books-review:SF-2026-ARXIV-2606-09061:start -->
Owner `INFER-SCHEDULING`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`.
<!-- books-review:SF-2026-ARXIV-2606-09061:end -->

<!-- existing:SF-2026-ARXIV-2606-09084:start -->
Owner `PLATFORM-SECURITY` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09084:end -->

<!-- delta:SF-2026-ARXIV-2606-09084:start -->
tool agent 的安全状态跨越多轮 artifact write/read；防御必须记录 artifact lineage 并在组合读取时执行 provenance-aware policy，不能只审核当前 turn。
<!-- delta:SF-2026-ARXIV-2606-09084:end -->

<!-- books-review:SF-2026-ARXIV-2606-09084:start -->
Owner `PLATFORM-SECURITY`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09084:end -->

<!-- existing:SF-2026-ARXIV-2606-09441:start -->
Owner `INFER-PREFILL` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09441:end -->

<!-- delta:SF-2026-ARXIV-2606-09441:start -->
RAG 重复文档的 prefill 可保存 selective index 而非整份 KV：offline 编码局部 attention，online 只重算 query-sensitive cross attention，以 storage traffic 换 TTFT。
<!-- delta:SF-2026-ARXIV-2606-09441:end -->

<!-- books-review:SF-2026-ARXIV-2606-09441:start -->
Owner `INFER-PREFILL`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09441:end -->

<!-- existing:SF-2026-ARXIV-2606-09613:start -->
Owner `INFER-SCHEDULING` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09613:end -->

<!-- delta:SF-2026-ARXIV-2606-09613:start -->
agent serving simulator 的执行单位必须从独立 request 提升为 program，显式模拟 turn dependency、tool gap、session affinity 与跨 HBM/host/CXL 的 KV residency。
<!-- delta:SF-2026-ARXIV-2606-09613:end -->

<!-- books-review:SF-2026-ARXIV-2606-09613:start -->
Owner `INFER-SCHEDULING`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09613:end -->

<!-- existing:SF-2026-ARXIV-2606-09643:start -->
Owner `INFER-KSERVE-TOPOLOGY` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09643:end -->

<!-- delta:SF-2026-ARXIV-2606-09643:start -->
extensible foundation model serving 需要把 base weights 与 extension state 虚拟化：共享公共层、按请求装载/组合扩展，并由 placement/cache 控制其生命周期。
<!-- delta:SF-2026-ARXIV-2606-09643:end -->

<!-- books-review:SF-2026-ARXIV-2606-09643:start -->
Owner `INFER-KSERVE-TOPOLOGY`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09643:end -->

<!-- existing:SF-2026-ARXIV-2606-09682:start -->
Owner `INFER-TENSORRT-LLM` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09682:end -->

<!-- delta:SF-2026-ARXIV-2606-09682:start -->
agent 生成 megakernel 必须经过 typed IR、静态 shape/layout/resource checks、编译与数值验证门，失败后才允许 self-retarget；自然语言计划不直接获得 kernel authority。
<!-- delta:SF-2026-ARXIV-2606-09682:end -->

<!-- books-review:SF-2026-ARXIV-2606-09682:start -->
Owner `INFER-TENSORRT-LLM`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09682:end -->

<!-- existing:SF-2026-ARXIV-2606-09686:start -->
Owner `INFER-TENSORRT-LLM` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09686:end -->

<!-- delta:SF-2026-ARXIV-2606-09686:start -->
低精度 format contract 需要 vendor-neutral、bit-exact 的 encode/decode、rounding、overflow、NaN/Inf/subnormal 与 microscaling conformance vectors；格式名相同不代表语义相同。
<!-- delta:SF-2026-ARXIV-2606-09686:end -->

<!-- books-review:SF-2026-ARXIV-2606-09686:start -->
Owner `INFER-TENSORRT-LLM`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09686:end -->

<!-- existing:SF-2026-ARXIV-2606-09692:start -->
Owner `PLATFORM-TRACE` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09692:end -->

<!-- delta:SF-2026-ARXIV-2606-09692:start -->
agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。
<!-- delta:SF-2026-ARXIV-2606-09692:end -->

<!-- books-review:SF-2026-ARXIV-2606-09692:start -->
Owner `PLATFORM-TRACE`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09692:end -->

<!-- existing:SF-2026-ARXIV-2606-09711:start -->
Owner `TRAIN-RLHF` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09711:end -->

<!-- delta:SF-2026-ARXIV-2606-09711:start -->
reward-hacking 监测需观察显性 exploit 之前形成的 proxy-reward internalization：正确性判断、proxy acceptance 预测与 proxy-gold gap 推理三种状态。
<!-- delta:SF-2026-ARXIV-2606-09711:end -->

<!-- books-review:SF-2026-ARXIV-2606-09711:start -->
Owner `TRAIN-RLHF`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09711:end -->

<!-- existing:SF-2026-ARXIV-2606-09774:start -->
Owner `AGENT-WORKFLOW` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09774:end -->

<!-- delta:SF-2026-ARXIV-2606-09774:start -->
给通用 coding agent 适配 scientific simulator 时，应把 executable contract 外置为 retrieval、procedural memory、agent-callable validator 与 validation-gated termination，而不重写 agent loop。
<!-- delta:SF-2026-ARXIV-2606-09774:end -->

<!-- books-review:SF-2026-ARXIV-2606-09774:start -->
Owner `AGENT-WORKFLOW`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09774:end -->

<!-- existing:SF-2026-ARXIV-2606-09809:start -->
Owner `PLATFORM-EVALUATION-SYSTEM` and adjacent chapters were read before disposition; existing text was compared against the exact-v1 delta.
<!-- existing:SF-2026-ARXIV-2606-09809:end -->

<!-- delta:SF-2026-ARXIV-2606-09809:start -->
Evaluation result 需要把 benchmark metadata、run data 与 model metadata 组合成可追踪 record，并按读者呈现 reproducibility、completeness、provenance/risk 与 score comparability。
<!-- delta:SF-2026-ARXIV-2606-09809:end -->

<!-- books-review:SF-2026-ARXIV-2606-09809:start -->
Owner `PLATFORM-EVALUATION-SYSTEM`; relation `Direct Evolution`; disposition `Integrate`.
<!-- books-review:SF-2026-ARXIV-2606-09809:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260609-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260609 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260609: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260609-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-TRAIT-MISALIGNMENT-MONITOR; review:SF-ML-LIFECYCLE-ASSESSMENT; review:SF-2026-ARXIV-2606-07684; review:SF-2026-ARXIV-2606-07687; review:SF-2026-ARXIV-2606-07703; review:SF-2026-ARXIV-2606-07710; review:SF-2026-ARXIV-2606-07713; review:SF-2026-ARXIV-2606-07720; review:SF-2026-ARXIV-2606-07726; review:SF-2026-ARXIV-2606-07783; review:SF-2026-ARXIV-2606-07790; review:SF-2026-ARXIV-2606-07805; review:SF-2026-ARXIV-2606-07808; review:SF-2026-ARXIV-2606-07822; review:SF-2026-ARXIV-2606-07833; review:SF-2026-ARXIV-2606-07834; review:SF-2026-ARXIV-2606-07845; review:SF-2026-ARXIV-2606-07846; review:SF-2026-ARXIV-2606-07856; review:SF-2026-ARXIV-2606-07867; review:SF-2026-ARXIV-2606-07874; review:SF-2026-ARXIV-2606-07878; review:SF-2026-ARXIV-2606-07881; review:SF-2026-ARXIV-2606-07889; review:SF-2026-ARXIV-2606-07904; review:SF-2026-ARXIV-2606-07923; review:SF-2026-ARXIV-2606-07936; review:SF-2026-ARXIV-2606-07943; review:SF-2026-ARXIV-2606-07950; review:SF-2026-ARXIV-2606-07957; review:SF-2026-ARXIV-2606-07968; review:SF-2026-ARXIV-2606-07970; review:SF-2026-ARXIV-2606-07992; review:SF-2026-ARXIV-2606-08049; review:SF-2026-ARXIV-2606-08094; review:SF-2026-ARXIV-2606-08106; review:SF-2026-ARXIV-2606-08197; review:SF-2026-ARXIV-2606-08200; review:SF-2026-ARXIV-2606-08302; review:SF-2026-ARXIV-2606-08317; review:SF-2026-ARXIV-2606-08340; review:SF-2026-ARXIV-2606-08346; review:SF-2026-ARXIV-2606-08348; review:SF-2026-ARXIV-2606-08367; review:SF-2026-ARXIV-2606-08372; review:SF-2026-ARXIV-2606-08381; review:SF-2026-ARXIV-2606-08382; review:SF-2026-ARXIV-2606-08403; review:SF-2026-ARXIV-2606-08411; review:SF-2026-ARXIV-2606-08417; review:SF-2026-ARXIV-2606-08432; review:SF-2026-ARXIV-2606-08433; review:SF-2026-ARXIV-2606-08446; review:SF-2026-ARXIV-2606-08476; review:SF-2026-ARXIV-2606-08483; review:SF-2026-ARXIV-2606-08486; review:SF-2026-ARXIV-2606-08517; review:SF-2026-ARXIV-2606-08529; review:SF-2026-ARXIV-2606-08531; review:SF-2026-ARXIV-2606-08539; review:SF-2026-ARXIV-2606-08574; review:SF-2026-ARXIV-2606-08590; review:SF-2026-ARXIV-2606-08610; review:SF-2026-ARXIV-2606-08615; review:SF-2026-ARXIV-2606-08625; review:SF-2026-ARXIV-2606-08635; review:SF-2026-ARXIV-2606-08661; review:SF-2026-ARXIV-2606-08671; review:SF-2026-ARXIV-2606-08679; review:SF-2026-ARXIV-2606-08702; review:SF-2026-ARXIV-2606-08755; review:SF-2026-ARXIV-2606-08761; review:SF-2026-ARXIV-2606-08769; review:SF-2026-ARXIV-2606-08779; review:SF-2026-ARXIV-2606-08790; review:SF-2026-ARXIV-2606-08806; review:SF-2026-ARXIV-2606-08813; review:SF-2026-ARXIV-2606-08831; review:SF-2026-ARXIV-2606-08840; review:SF-2026-ARXIV-2606-08867; review:SF-2026-ARXIV-2606-08869; review:SF-2026-ARXIV-2606-08891; review:SF-2026-ARXIV-2606-08892; review:SF-2026-ARXIV-2606-08893; review:SF-2026-ARXIV-2606-08919; review:SF-2026-ARXIV-2606-08950; review:SF-2026-ARXIV-2606-08960; review:SF-2026-ARXIV-2606-09005; review:SF-2026-ARXIV-2606-09061; review:SF-2026-ARXIV-2606-09084; review:SF-2026-ARXIV-2606-09441; review:SF-2026-ARXIV-2606-09613; review:SF-2026-ARXIV-2606-09643; review:SF-2026-ARXIV-2606-09682; review:SF-2026-ARXIV-2606-09686; review:SF-2026-ARXIV-2606-09692; review:SF-2026-ARXIV-2606-09711; review:SF-2026-ARXIV-2606-09774; review:SF-2026-ARXIV-2606-09809 | EVIDENCE-OWNER-REBUILD-20260609: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260609-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-TRAIT-MISALIGNMENT-MONITOR; analysis-decision:SF-ML-LIFECYCLE-ASSESSMENT; analysis-decision:SF-2026-ARXIV-2606-07684; analysis-decision:SF-2026-ARXIV-2606-07783; analysis-decision:SF-2026-ARXIV-2606-07790; analysis-decision:SF-2026-ARXIV-2606-07805; analysis-decision:SF-2026-ARXIV-2606-07808; analysis-decision:SF-2026-ARXIV-2606-07822; analysis-decision:SF-2026-ARXIV-2606-07833; analysis:DA-20260606-EVALUATION-EVIDENCE; analysis-decision:SF-2026-ARXIV-2606-07845; analysis-decision:SF-2026-ARXIV-2606-07867; analysis-decision:SF-2026-ARXIV-2606-07874; analysis-decision:SF-2026-ARXIV-2606-07878; analysis-decision:SF-2026-ARXIV-2606-07881; analysis-decision:SF-2026-ARXIV-2606-07889; analysis-decision:SF-2026-ARXIV-2606-07904; analysis-decision:SF-2026-ARXIV-2606-07923; analysis-decision:SF-2026-ARXIV-2606-07936; analysis:DA-20260607-SECURITY; analysis-decision:SF-2026-ARXIV-2606-07950; analysis-decision:SF-2026-ARXIV-2606-07957; analysis-decision:SF-2026-ARXIV-2606-07968; analysis-decision:SF-2026-ARXIV-2606-07992; analysis-decision:SF-2026-ARXIV-2606-08049; analysis-decision:SF-2026-ARXIV-2606-08094; analysis:DA-20260607-EVOLUTION; analysis-decision:SF-2026-ARXIV-2606-08197; analysis-decision:SF-2026-ARXIV-2606-08200; analysis-decision:SF-2026-ARXIV-2606-08340; analysis-decision:SF-2026-ARXIV-2606-08348; analysis-decision:SF-2026-ARXIV-2606-08367; analysis-decision:SF-2026-ARXIV-2606-08372; analysis-decision:SF-2026-ARXIV-2606-08382; analysis-decision:SF-2026-ARXIV-2606-08403; analysis-decision:SF-2026-ARXIV-2606-08411; analysis-decision:SF-2026-ARXIV-2606-08417; analysis-decision:SF-2026-ARXIV-2606-08432; analysis-decision:SF-2026-ARXIV-2606-08433; analysis-decision:SF-2026-ARXIV-2606-08446; analysis-decision:SF-2026-ARXIV-2606-08476; analysis-decision:SF-2026-ARXIV-2606-08483; analysis-decision:SF-2026-ARXIV-2606-08486; analysis-decision:SF-2026-ARXIV-2606-08517; analysis-decision:SF-2026-ARXIV-2606-08529; analysis-decision:SF-2026-ARXIV-2606-08531; analysis-decision:SF-2026-ARXIV-2606-08539; analysis-decision:SF-2026-ARXIV-2606-08574; analysis-decision:SF-2026-ARXIV-2606-08590; analysis-decision:SF-2026-ARXIV-2606-08610; analysis-decision:SF-2026-ARXIV-2606-08615; analysis-decision:SF-2026-ARXIV-2606-08625; analysis-decision:SF-2026-ARXIV-2606-08635; analysis-decision:SF-2026-ARXIV-2606-08661; analysis-decision:SF-2026-ARXIV-2606-08671; analysis-decision:SF-2026-ARXIV-2606-08679; analysis-decision:SF-2026-ARXIV-2606-08702; analysis-decision:SF-2026-ARXIV-2606-08755; analysis-decision:SF-2026-ARXIV-2606-08761; analysis-decision:SF-2026-ARXIV-2606-08769; analysis-decision:SF-2026-ARXIV-2606-08779; analysis-decision:SF-2026-ARXIV-2606-08790; analysis-decision:SF-2026-ARXIV-2606-08806; analysis-decision:SF-2026-ARXIV-2606-08813; analysis-decision:SF-2026-ARXIV-2606-08831; analysis-decision:SF-2026-ARXIV-2606-08840; analysis-decision:SF-2026-ARXIV-2606-08867; analysis-decision:SF-2026-ARXIV-2606-08869; analysis-decision:SF-2026-ARXIV-2606-08891; analysis-decision:SF-2026-ARXIV-2606-08892; analysis-decision:SF-2026-ARXIV-2606-08893; analysis-decision:SF-2026-ARXIV-2606-08919; analysis-decision:SF-2026-ARXIV-2606-08950; analysis-decision:SF-2026-ARXIV-2606-08960; analysis-decision:SF-2026-ARXIV-2606-09005; analysis-decision:SF-2026-ARXIV-2606-09061; analysis-decision:SF-2026-ARXIV-2606-09084; analysis-decision:SF-2026-ARXIV-2606-09441; analysis-decision:SF-2026-ARXIV-2606-09613; analysis-decision:SF-2026-ARXIV-2606-09643; analysis-decision:SF-2026-ARXIV-2606-09682; analysis-decision:SF-2026-ARXIV-2606-09686; analysis-decision:SF-2026-ARXIV-2606-09692; analysis-decision:SF-2026-ARXIV-2606-09711; analysis-decision:SF-2026-ARXIV-2606-09774; analysis-decision:SF-2026-ARXIV-2606-09809 | SELECTION-OWNER-REBUILD-20260609: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260609-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-TRAIT-MISALIGNMENT-MONITOR; books-review:SF-ML-LIFECYCLE-ASSESSMENT; books-review:SF-2026-ARXIV-2606-07684; books-review:SF-2026-ARXIV-2606-07687; books-review:SF-2026-ARXIV-2606-07703; books-review:SF-2026-ARXIV-2606-07710; books-review:SF-2026-ARXIV-2606-07713; books-review:SF-2026-ARXIV-2606-07720; books-review:SF-2026-ARXIV-2606-07726; books-review:SF-2026-ARXIV-2606-07783; books-review:SF-2026-ARXIV-2606-07790; books-review:SF-2026-ARXIV-2606-07805; books-review:SF-2026-ARXIV-2606-07808; books-review:SF-2026-ARXIV-2606-07822; books-review:SF-2026-ARXIV-2606-07833; books-review:SF-2026-ARXIV-2606-07834; books-review:SF-2026-ARXIV-2606-07845; books-review:SF-2026-ARXIV-2606-07846; books-review:SF-2026-ARXIV-2606-07856; books-review:SF-2026-ARXIV-2606-07867; books-review:SF-2026-ARXIV-2606-07874; books-review:SF-2026-ARXIV-2606-07878; books-review:SF-2026-ARXIV-2606-07881; books-review:SF-2026-ARXIV-2606-07889; books-review:SF-2026-ARXIV-2606-07904; books-review:SF-2026-ARXIV-2606-07923; books-review:SF-2026-ARXIV-2606-07936; books-review:SF-2026-ARXIV-2606-07943; books-review:SF-2026-ARXIV-2606-07950; books-review:SF-2026-ARXIV-2606-07957; books-review:SF-2026-ARXIV-2606-07968; books-review:SF-2026-ARXIV-2606-07970; books-review:SF-2026-ARXIV-2606-07992; books-review:SF-2026-ARXIV-2606-08049; books-review:SF-2026-ARXIV-2606-08094; books-review:SF-2026-ARXIV-2606-08106; books-review:SF-2026-ARXIV-2606-08197; books-review:SF-2026-ARXIV-2606-08200; books-review:SF-2026-ARXIV-2606-08302; books-review:SF-2026-ARXIV-2606-08317; books-review:SF-2026-ARXIV-2606-08340; books-review:SF-2026-ARXIV-2606-08346; books-review:SF-2026-ARXIV-2606-08348; books-review:SF-2026-ARXIV-2606-08367; books-review:SF-2026-ARXIV-2606-08372; books-review:SF-2026-ARXIV-2606-08381; books-review:SF-2026-ARXIV-2606-08382; books-review:SF-2026-ARXIV-2606-08403; books-review:SF-2026-ARXIV-2606-08411; books-review:SF-2026-ARXIV-2606-08417; books-review:SF-2026-ARXIV-2606-08432; books-review:SF-2026-ARXIV-2606-08433; books-review:SF-2026-ARXIV-2606-08446; books-review:SF-2026-ARXIV-2606-08476; books-review:SF-2026-ARXIV-2606-08483; books-review:SF-2026-ARXIV-2606-08486; books-review:SF-2026-ARXIV-2606-08517; books-review:SF-2026-ARXIV-2606-08529; books-review:SF-2026-ARXIV-2606-08531; books-review:SF-2026-ARXIV-2606-08539; books-review:SF-2026-ARXIV-2606-08574; books-review:SF-2026-ARXIV-2606-08590; books-review:SF-2026-ARXIV-2606-08610; books-review:SF-2026-ARXIV-2606-08615; books-review:SF-2026-ARXIV-2606-08625; books-review:SF-2026-ARXIV-2606-08635; books-review:SF-2026-ARXIV-2606-08661; books-review:SF-2026-ARXIV-2606-08671; books-review:SF-2026-ARXIV-2606-08679; books-review:SF-2026-ARXIV-2606-08702; books-review:SF-2026-ARXIV-2606-08755; books-review:SF-2026-ARXIV-2606-08761; books-review:SF-2026-ARXIV-2606-08769; books-review:SF-2026-ARXIV-2606-08779; books-review:SF-2026-ARXIV-2606-08790; books-review:SF-2026-ARXIV-2606-08806; books-review:SF-2026-ARXIV-2606-08813; books-review:SF-2026-ARXIV-2606-08831; books-review:SF-2026-ARXIV-2606-08840; books-review:SF-2026-ARXIV-2606-08867; books-review:SF-2026-ARXIV-2606-08869; books-review:SF-2026-ARXIV-2606-08891; books-review:SF-2026-ARXIV-2606-08892; books-review:SF-2026-ARXIV-2606-08893; books-review:SF-2026-ARXIV-2606-08919; books-review:SF-2026-ARXIV-2606-08950; books-review:SF-2026-ARXIV-2606-08960; books-review:SF-2026-ARXIV-2606-09005; books-review:SF-2026-ARXIV-2606-09061; books-review:SF-2026-ARXIV-2606-09084; books-review:SF-2026-ARXIV-2606-09441; books-review:SF-2026-ARXIV-2606-09613; books-review:SF-2026-ARXIV-2606-09643; books-review:SF-2026-ARXIV-2606-09682; books-review:SF-2026-ARXIV-2606-09686; books-review:SF-2026-ARXIV-2606-09692; books-review:SF-2026-ARXIV-2606-09711; books-review:SF-2026-ARXIV-2606-09774; books-review:SF-2026-ARXIV-2606-09809 | BOOKS-OWNER-REBUILD-20260609: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

The 462 pre-denominator closures remain row-addressable in the screening ledger with family-specific reasons and reopen conditions; they are not scored, selected or leaked into Books.

## 9. Recommended Action

Final disposition is 14 Integrate and one No Change — Existing Coverage (`2606.09061`); formal Books comparison=15 and Weekly Only=0. The initial No Change for `2606.08950` was overturned by fresh audit and resolved through the Ch76 writeback.

## 10. Repository Changes

Root wrote the 14 Books deltas across 10 owner chapters; this lane edits the 2026-06-09 Daily, its source packet and deterministic finalizer, and independently records the post-write fresh audit.

## 11. Open Questions

No Gate-blocking question remains. Future work must revalidate workload-specific simulator, numeric-format, vector-database and security-defense claims rather than treating these exact-v1 results as production constants.

## 12. Sources

- [Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning](https://arxiv.org/abs/2606.07631v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment](https://arxiv.org/abs/2606.07632v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching](https://arxiv.org/abs/2606.07684v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction](https://arxiv.org/abs/2606.07687v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [How Much Dense Attention is Necessary? Oracle-Guided Sparse Prefill for Full/GQA Layers in Hybrid Long-Context Models](https://arxiv.org/abs/2606.07703v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing](https://arxiv.org/abs/2606.07710v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Attention at the Theoretical Minimum: A Mathematics of Arrays Framework for Memory-Optimal Transformer Kernels](https://arxiv.org/abs/2606.07713v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Why Limit the Residual Stream to Layers and Not Tokens? Persistent Memory for Continuous Latent Reasoning](https://arxiv.org/abs/2606.07720v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm that Provably Exploits Model Similarity](https://arxiv.org/abs/2606.07726v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval](https://arxiv.org/abs/2606.07783v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games](https://arxiv.org/abs/2606.07790v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems](https://arxiv.org/abs/2606.07805v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models](https://arxiv.org/abs/2606.07808v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust](https://arxiv.org/abs/2606.07822v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks](https://arxiv.org/abs/2606.07833v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Cherry-pick Override: Unsafe Directional Commitment in LLM Judges under Mixed Evidence](https://arxiv.org/abs/2606.07834v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [GRPO Does Not Close the Multi-Agent Coordination Gap](https://arxiv.org/abs/2606.07845v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Cost-Aware Speculative Execution for LLM-Agent Workflows: An Integrated Five-Dimension Method](https://arxiv.org/abs/2606.07846v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Teacher-Free Self-Training Amplifies but Does Not Compound: A Pass@$K$ Crossover on a Free-Verifier Domain](https://arxiv.org/abs/2606.07856v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [The Cold-Start Safety Gap in LLM Agents](https://arxiv.org/abs/2606.07867v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators](https://arxiv.org/abs/2606.07874v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Still: Amortized KV Cache Compaction in a Single Forward Pass](https://arxiv.org/abs/2606.07878v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency](https://arxiv.org/abs/2606.07881v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories](https://arxiv.org/abs/2606.07889v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents](https://arxiv.org/abs/2606.07904v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Larch: Learned Query Optimization for Semantic Predicates](https://arxiv.org/abs/2606.07923v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation](https://arxiv.org/abs/2606.07936v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents](https://arxiv.org/abs/2606.07943v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.07950v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path](https://arxiv.org/abs/2606.07957v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](https://arxiv.org/abs/2606.07968v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks](https://arxiv.org/abs/2606.07970v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation](https://arxiv.org/abs/2606.07992v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows](https://arxiv.org/abs/2606.08049v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models](https://arxiv.org/abs/2606.08094v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents](https://arxiv.org/abs/2606.08106v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments](https://arxiv.org/abs/2606.08197v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents](https://arxiv.org/abs/2606.08200v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [HACK++: Towards More Effective Head-Aware Key-Value Compression for Efficient Visual Autoregressive Modeling](https://arxiv.org/abs/2606.08302v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Architectural Evolution and Selection Framework for Database Systems in AI-Ready Data Platforms](https://arxiv.org/abs/2606.08317v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](https://arxiv.org/abs/2606.08340v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [CATPO: Critique-Augmented Tree Policy Optimization](https://arxiv.org/abs/2606.08346v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses](https://arxiv.org/abs/2606.08348v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy](https://arxiv.org/abs/2606.08367v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC)](https://arxiv.org/abs/2606.08372v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard](https://arxiv.org/abs/2606.08381v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://arxiv.org/abs/2606.08382v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection](https://arxiv.org/abs/2606.08403v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding](https://arxiv.org/abs/2606.08411v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics](https://arxiv.org/abs/2606.08417v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Trajectory-Refined Distillation](https://arxiv.org/abs/2606.08432v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing)](https://arxiv.org/abs/2606.08433v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Sparrow: Sparse Rollout for Stable and Efficient Long-context RL of Large Language Models](https://arxiv.org/abs/2606.08446v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training](https://arxiv.org/abs/2606.08476v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Testing the Black Box: Structural Barriers to Independent Evaluation of Consumer-Facing Health LLMs](https://arxiv.org/abs/2606.08483v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [TRADE: Transducer-Augmented Decoder for Speech LLM](https://arxiv.org/abs/2606.08486v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [A Joint Finite-Sample Certificate for Adaptive Selective Conformal Risk Control](https://arxiv.org/abs/2606.08517v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Scaffold Effects on GAIA: A Controlled Comparison](https://arxiv.org/abs/2606.08529v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [ForesightSafety-SAGE:A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents](https://arxiv.org/abs/2606.08531v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions](https://arxiv.org/abs/2606.08539v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [OrderDP: A Theoretically Guaranteed Lossless Dynamic Data Pruning Framework](https://arxiv.org/abs/2606.08574v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents](https://arxiv.org/abs/2606.08590v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning](https://arxiv.org/abs/2606.08610v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Harnessing Streaming Video in the Wild](https://arxiv.org/abs/2606.08615v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [From Holistic Evaluation to Structured Criteria: Rubrics Across the Evolving LLM Landscape](https://arxiv.org/abs/2606.08625v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving](https://arxiv.org/abs/2606.08635v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems](https://arxiv.org/abs/2606.08661v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History](https://arxiv.org/abs/2606.08671v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation](https://arxiv.org/abs/2606.08679v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems](https://arxiv.org/abs/2606.08702v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Co-Evolving Skill Generation and Policy Optimization](https://arxiv.org/abs/2606.08755v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing](https://arxiv.org/abs/2606.08761v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [RadOT-Eval: Auditable Structured-Evidence Transport for Radiology Report Evaluation](https://arxiv.org/abs/2606.08769v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Reformulate LLM Reinforcement Learning for Efficient Training under Black-box Discrepancy](https://arxiv.org/abs/2606.08779v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [RAILS: Verification-Native Clearing For Agentic Commerce](https://arxiv.org/abs/2606.08790v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Governance Controls for AI-Generated Test Artifacts in Autonomous Software Testing](https://arxiv.org/abs/2606.08806v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Aperon Technical Report: Hierarchical No-Pointer Tangent-Local Search for High-Dimensional Approximate Nearest Neighbors](https://arxiv.org/abs/2606.08813v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models](https://arxiv.org/abs/2606.08831v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs](https://arxiv.org/abs/2606.08840v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework](https://arxiv.org/abs/2606.08867v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [A Low-Latency Semantic State Estimator using Latent Predictive Learning for Dynamic Network Monitoring and Orchestration](https://arxiv.org/abs/2606.08869v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [PALUTE: Processing-In-Memory Acceleration via Lookup Table for Edge LLM Inference](https://arxiv.org/abs/2606.08891v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Diffuse AI Control on Fuzzy Tasks](https://arxiv.org/abs/2606.08892v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Cheap Reward Hacking Detection](https://arxiv.org/abs/2606.08893v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human](https://arxiv.org/abs/2606.08919v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [When More Cores Hurts: The Vector Database Scaling Paradox in HPC](https://arxiv.org/abs/2606.08950v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops](https://arxiv.org/abs/2606.08960v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries](https://arxiv.org/abs/2606.09005v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill LLM Serving](https://arxiv.org/abs/2606.09061v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps](https://arxiv.org/abs/2606.09084v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance](https://arxiv.org/abs/2606.09441v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving](https://arxiv.org/abs/2606.09613v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [FMplex: Model Virtualization for Serving Extensible Foundation Models](https://arxiv.org/abs/2606.09643v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis](https://arxiv.org/abs/2606.09682v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [An 83-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats](https://arxiv.org/abs/2606.09686v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Observability for Delegated Execution in Agentic AI Systems](https://arxiv.org/abs/2606.09692v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization](https://arxiv.org/abs/2606.09711v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Auto-Configuring Scientific Simulators with Lightweight Coding-Agent Adapters](https://arxiv.org/abs/2606.09774v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
- [Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting](https://arxiv.org/abs/2606.09809v1) — first-public（Asia/Shanghai）：2026-06-09；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。477 个 raw identities 已闭合为 15 个 retained families 与 462 个 family-specific pre-denominator closures；Selection 为 15 eligible + 0 non-eligible、selected=3，互斥并集守恒；Benchmark Claim=yes 子集 15/15 完整；Books formal comparison=15、Weekly Only=0。全部 scope 通过 fresh-context audit，未解决 finding 为 0。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
