# Daily Research — 2026-06-05

**Research Date:** 2026-06-05

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-04 09:00:00 ～ 2026-06-05 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
The independently audited 624-row screening surface freezes 64 retained families and 560 family-specific pre-denominator closures. All 64 retained families were independently re-opened against exact-v1 evidence. Fresh scoring yields 33 Deep and 31 Standard reviews; Score 9 fell from 46 to 13, removing the prior ceiling clustering. Evidence and Selection are closed. Root's eight Integrate proposals were then audited at nine concrete Books locations; all post-write findings were repaired and re-audited, so Books is closed.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-05 |
| Window End | 2026-06-05 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260605-66052599 |
| Denominator Frozen At | 2026-08-28T23:48:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-04T09:00:00+08:00 | 2026-06-05T09:00:00+08:00 | 2026-08-28T23:48:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 706 | SF-2026-ARXIV-2606-05241;SF-2026-ARXIV-2606-05271;SF-2026-ARXIV-2606-05304;SF-2026-ARXIV-2606-05308;SF-2026-ARXIV-2606-05339;SF-2026-ARXIV-2606-05378;SF-2026-ARXIV-2606-05384;SF-2026-ARXIV-2606-05391;SF-2026-ARXIV-2606-05395;SF-2026-ARXIV-2606-05396;SF-2026-ARXIV-2606-05403;SF-2026-ARXIV-2606-05414;SF-2026-ARXIV-2606-05415;SF-2026-ARXIV-2606-05433;SF-2026-ARXIV-2606-05495;SF-2026-ARXIV-2606-05523;SF-2026-ARXIV-2606-05548;SF-2026-ARXIV-2606-05551;SF-2026-ARXIV-2606-05558;SF-2026-ARXIV-2606-05559;SF-2026-ARXIV-2606-05568;SF-2026-ARXIV-2606-05597;SF-2026-ARXIV-2606-05606;SF-2026-ARXIV-2606-05610;SF-2026-ARXIV-2606-05646;SF-2026-ARXIV-2606-05662;SF-2026-ARXIV-2606-05679;SF-2026-ARXIV-2606-05688;SF-2026-ARXIV-2606-05711;SF-2026-ARXIV-2606-05725;SF-2026-ARXIV-2606-05742;SF-2026-ARXIV-2606-05743;SF-2026-ARXIV-2606-05787;SF-2026-ARXIV-2606-05800;SF-2026-ARXIV-2606-05805;SF-2026-ARXIV-2606-05828;SF-2026-ARXIV-2606-05868;SF-2026-ARXIV-2606-05872;SF-2026-ARXIV-2606-05875;SF-2026-ARXIV-2606-05894;SF-2026-ARXIV-2606-05933;SF-2026-ARXIV-2606-05946;SF-2026-ARXIV-2606-05951;SF-2026-ARXIV-2606-05958;SF-2026-ARXIV-2606-05976;SF-2026-ARXIV-2606-06032;SF-2026-ARXIV-2606-06036;SF-2026-ARXIV-2606-06044;SF-2026-ARXIV-2606-06054;SF-2026-ARXIV-2606-06055;SF-2026-ARXIV-2606-06063;SF-2026-ARXIV-2606-06079;SF-2026-ARXIV-2606-06087;SF-2026-ARXIV-2606-06090;SF-2026-ARXIV-2606-06178;SF-2026-ARXIV-2606-06223;SF-2026-ARXIV-2606-06240;SF-2026-ARXIV-2606-06256;SF-2026-ARXIV-2606-06284;SF-2026-ARXIV-2606-06302;SF-2026-ARXIV-2606-06324;SF-2026-ARXIV-2606-06337;SF-2026-ARXIV-2606-06387;SF-2026-ARXIV-2606-06438;SF-2026-ARXIV-2606-06448;SF-2026-ARXIV-2606-06453;SF-2026-ARXIV-2606-06460;SF-2026-ARXIV-2606-06467 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260605/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260605; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260605 |
<!-- coverage:SRC-ARXIV:20260605:start -->
624/624 identities were screened at title+abstract level. The independent audit tested all 52 proposed retains and all 572 proposed closures, yielding 64 retained and 560 pre-denominator closures. Full-screening recall does not itself imply admission; each closure remains in the canonical screening ledger with its family-specific reason.
<!-- coverage:SRC-ARXIV:20260605:end -->


<!-- latest-contract-reopen:2026-06-05:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-05:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **706** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **68** 条是旧报告 retained provenance，**638** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-05241 | arXiv:2606.05241v1 | paper-v1:2606.05241 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05241 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05241 | yes |
| SF-2026-ARXIV-2606-05271 | arXiv:2606.05271v1 | paper-v1:2606.05271 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05271 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05304 | arXiv:2606.05304v1 | paper-v1:2606.05304 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05304 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-05304 | yes |
| SF-2026-ARXIV-2606-05308 | arXiv:2606.05308v1 | paper-v1:2606.05308 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05308 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05308 | yes |
| SF-2026-ARXIV-2606-05339 | arXiv:2606.05339v1 | paper-v1:2606.05339 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05339 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05339 | yes |
| SF-2026-ARXIV-2606-05378 | arXiv:2606.05378v1 | paper-v1:2606.05378 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05378 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05378 | yes |
| SF-2026-ARXIV-2606-05384 | arXiv:2606.05384v1 | paper-v1:2606.05384 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05384 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05384 | yes |
| SF-2026-ARXIV-2606-05391 | arXiv:2606.05391v1 | paper-v1:2606.05391 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05391 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05395 | arXiv:2606.05395v1 | paper-v1:2606.05395 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05395 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05395 | yes |
| SF-2026-ARXIV-2606-05396 | arXiv:2606.05396v1 | paper-v1:2606.05396 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05396 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05403 | arXiv:2606.05403v1 | paper-v1:2606.05403 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05403 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05403 | yes |
| SF-2026-ARXIV-2606-05414 | arXiv:2606.05414v1 | paper-v1:2606.05414 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05414 | self | — | new_in_window | PLATFORM-MONITORING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05415 | arXiv:2606.05415v1 | paper-v1:2606.05415 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05415 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05415 | yes |
| SF-2026-ARXIV-2606-05433 | arXiv:2606.05433v1 | paper-v1:2606.05433 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05433 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05433 | yes |
| SF-2026-ARXIV-2606-05495 | arXiv:2606.05495v1 | paper-v1:2606.05495 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05495 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05495 | yes |
| SF-2026-ARXIV-2606-05523 | arXiv:2606.05523v1 | paper-v1:2606.05523 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05523 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05548 | arXiv:2606.05548v1 | paper-v1:2606.05548 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05548 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05548 | yes |
| SF-2026-ARXIV-2606-05551 | arXiv:2606.05551v1 | paper-v1:2606.05551 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05551 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05551 | yes |
| SF-2026-ARXIV-2606-05558 | arXiv:2606.05558v1 | paper-v1:2606.05558 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05558 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05558 | yes |
| SF-2026-ARXIV-2606-05559 | arXiv:2606.05559v1 | paper-v1:2606.05559 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05559 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05559 | yes |
| SF-2026-ARXIV-2606-05568 | arXiv:2606.05568v1 | paper-v1:2606.05568 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05568 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05568 | yes |
| SF-2026-ARXIV-2606-05597 | arXiv:2606.05597v1 | paper-v1:2606.05597 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05597 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05597 | yes |
| SF-2026-ARXIV-2606-05606 | arXiv:2606.05606v1 | paper-v1:2606.05606 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05606 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05606 | yes |
| SF-2026-ARXIV-2606-05610 | arXiv:2606.05610v1 | paper-v1:2606.05610 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05610 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05610 | yes |
| SF-2026-ARXIV-2606-05646 | arXiv:2606.05646v1 | paper-v1:2606.05646 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05646 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05646 | yes |
| SF-2026-ARXIV-2606-05662 | arXiv:2606.05662v1 | paper-v1:2606.05662 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05662 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05662 | yes |
| SF-2026-ARXIV-2606-05679 | arXiv:2606.05679v1 | paper-v1:2606.05679 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05679 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-05679 | yes |
| SF-2026-ARXIV-2606-05688 | arXiv:2606.05688v1 | paper-v1:2606.05688 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05688 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05688 | yes |
| SF-2026-ARXIV-2606-05711 | arXiv:2606.05711v1 | paper-v1:2606.05711 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05711 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05711 | yes |
| SF-2026-ARXIV-2606-05725 | arXiv:2606.05725v1 | paper-v1:2606.05725 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05725 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05725 | yes |
| SF-2026-ARXIV-2606-05742 | arXiv:2606.05742v1 | paper-v1:2606.05742 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05742 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05742 | yes |
| SF-2026-ARXIV-2606-05743 | arXiv:2606.05743v1 | paper-v1:2606.05743 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05743 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05743 | yes |
| SF-2026-ARXIV-2606-05787 | arXiv:2606.05787v1 | paper-v1:2606.05787 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05787 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05787 | yes |
| SF-2026-ARXIV-2606-05800 | arXiv:2606.05800v1 | paper-v1:2606.05800 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05800 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05800 | yes |
| SF-2026-ARXIV-2606-05805 | arXiv:2606.05805v1 | paper-v1:2606.05805 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05805 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05805 | yes |
| SF-2026-ARXIV-2606-05828 | arXiv:2606.05828v1 | paper-v1:2606.05828 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05828 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05828 | yes |
| SF-2026-ARXIV-2606-05868 | arXiv:2606.05868v1 | paper-v1:2606.05868 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05868 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05868 | yes |
| SF-2026-ARXIV-2606-05872 | arXiv:2606.05872v1 | paper-v1:2606.05872 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05872 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05872 | yes |
| SF-2026-ARXIV-2606-05875 | arXiv:2606.05875v1 | paper-v1:2606.05875 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05875 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05875 | yes |
| SF-2026-ARXIV-2606-05894 | arXiv:2606.05894v1 | paper-v1:2606.05894 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05894 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05894 | yes |
| SF-2026-ARXIV-2606-05933 | arXiv:2606.05933v1 | paper-v1:2606.05933 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05933 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-05933 | yes |
| SF-2026-ARXIV-2606-05946 | arXiv:2606.05946v1 | paper-v1:2606.05946 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05946 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05946 | no |
| SF-2026-ARXIV-2606-05951 | arXiv:2606.05951v1 | paper-v1:2606.05951 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05951 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-05951 | yes |
| SF-2026-ARXIV-2606-05958 | arXiv:2606.05958v1 | paper-v1:2606.05958 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-05958 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05958 | yes |
| SF-2026-ARXIV-2606-05976 | arXiv:2606.05976v1 | paper-v1:2606.05976 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05976 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05976 | yes |
| SF-2026-ARXIV-2606-06032 | arXiv:2606.06032v1 | paper-v1:2606.06032 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06032 | self | — | new_in_window | TRAIN-CHECKPOINT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06032 | yes |
| SF-2026-ARXIV-2606-06036 | arXiv:2606.06036v1 | paper-v1:2606.06036 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06036 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06036 | yes |
| SF-2026-ARXIV-2606-06044 | arXiv:2606.06044v1 | paper-v1:2606.06044 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06044 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06044 | yes |
| SF-2026-ARXIV-2606-06054 | arXiv:2606.06054v1 | paper-v1:2606.06054 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06054 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06054 | yes |
| SF-2026-ARXIV-2606-06055 | arXiv:2606.06055v1 | paper-v1:2606.06055 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06055 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06055 | yes |
| SF-2026-ARXIV-2606-06063 | arXiv:2606.06063v1 | paper-v1:2606.06063 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06063 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06063 | yes |
| SF-2026-ARXIV-2606-06079 | arXiv:2606.06079v1 | paper-v1:2606.06079 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06079 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06079 | yes |
| SF-2026-ARXIV-2606-06087 | arXiv:2606.06087v1 | paper-v1:2606.06087 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06087 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06087 | yes |
| SF-2026-ARXIV-2606-06090 | arXiv:2606.06090v1 | paper-v1:2606.06090 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06090 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-06090 | yes |
| SF-2026-ARXIV-2606-06178 | arXiv:2606.06178v1 | paper-v1:2606.06178 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06178 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06178 | yes |
| SF-2026-ARXIV-2606-06223 | arXiv:2606.06223v1 | paper-v1:2606.06223 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06223 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06223 | yes |
| SF-2026-ARXIV-2606-06240 | arXiv:2606.06240v1 | paper-v1:2606.06240 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06240 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-06240 | yes |
| SF-2026-ARXIV-2606-06256 | arXiv:2606.06256v1 | paper-v1:2606.06256 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06256 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-06256 | yes |
| SF-2026-ARXIV-2606-06284 | arXiv:2606.06284v1 | paper-v1:2606.06284 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06284 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06284 | yes |
| SF-2026-ARXIV-2606-06302 | arXiv:2606.06302v1 | paper-v1:2606.06302 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06302 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06302 | yes |
| SF-2026-ARXIV-2606-06324 | arXiv:2606.06324v1 | paper-v1:2606.06324 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06324 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06324 | yes |
| SF-2026-ARXIV-2606-06337 | arXiv:2606.06337v1 | paper-v1:2606.06337 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06337 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06337 | yes |
| SF-2026-ARXIV-2606-06387 | arXiv:2606.06387v1 | paper-v1:2606.06387 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06387 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06387 | yes |
| SF-2026-ARXIV-2606-06438 | arXiv:2606.06438v1 | paper-v1:2606.06438 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06438 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06438 | yes |
| SF-2026-ARXIV-2606-06448 | arXiv:2606.06448v1 | paper-v1:2606.06448 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06448 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06448 | yes |
| SF-2026-ARXIV-2606-06453 | arXiv:2606.06453v1 | paper-v1:2606.06453 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06453 | self | — | new_in_window | INFER-PAGED-ATTENTION | Integrate | books-review:SF-2026-ARXIV-2606-06453 | yes |
| SF-2026-ARXIV-2606-06460 | arXiv:2606.06460v1 | paper-v1:2606.06460 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06460 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06460 | yes |
| SF-2026-ARXIV-2606-06467 | arXiv:2606.06467v1 | paper-v1:2606.06467 | 2026-W23 | 2026-06-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-06467 | self | — | new_in_window | INFER-PAGED-ATTENTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06467 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-05241 | RP-9a9d82e94f02afbb | deep | arXiv:2606.05241v1 | SRC-ARXIV@arXiv:2606.05241v1 | https://arxiv.org/html/2606.05241v1 §3 Methodology; §§3.1–3.2 | https://arxiv.org/html/2606.05241v1 §§4–5 Evaluation and Experiment; Appendices C–E | https://arxiv.org/html/2606.05241v1 Limitations; §6 Discussion | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05241 | complete |
| SF-2026-ARXIV-2606-05271 | RP-706d0361e14a820a | deep | arXiv:2606.05271v1 | SRC-ARXIV@arXiv:2606.05271v1 | https://arxiv.org/html/2606.05271v1 §3. BIDENT Framework; §§3.4–3.5 | https://arxiv.org/html/2606.05271v1 §4. Evaluation; §4.1 Experimental Setup | https://arxiv.org/html/2606.05271v1 §3.4 Framework Overhead; §7. Conclusion | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-05271 | complete |
| SF-2026-ARXIV-2606-05304 | RP-ee35763368b2de73 | deep | arXiv:2606.05304v1 | SRC-ARXIV@arXiv:2606.05304v1 | https://arxiv.org/html/2606.05304v1 §4 PACT; §§4.1–4.3 action-state message space and protocol properties | https://arxiv.org/html/2606.05304v1 §5 Experiments; §6 Agentic Coding Harnesses | https://arxiv.org/html/2606.05304v1 §Limitations | https://github.com/iNLP-Lab/PACT — repository disclosed; exact-v1 does not pin an immutable event-time commit | claim:SF-2026-ARXIV-2606-05304 | complete |
| SF-2026-ARXIV-2606-05308 | RP-bb2d3ea71f8c23ef | deep | arXiv:2606.05308v1 | SRC-ARXIV@arXiv:2606.05308v1 | https://arxiv.org/html/2606.05308v1 §2 Method | https://arxiv.org/html/2606.05308v1 §3 Results | https://arxiv.org/html/2606.05308v1 Limitations; §4 Future Work | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05308 | complete |
| SF-2026-ARXIV-2606-05339 | RP-61f041f762a22e5a | deep | arXiv:2606.05339v1 | SRC-ARXIV@arXiv:2606.05339v1 | https://arxiv.org/html/2606.05339v1 §IV Methodology; §§IV-A–IV-G; §V Results: MCP Server Fault Taxonomy | https://arxiv.org/html/2606.05339v1 §IV-D Selection of Repositories for Manual Analysis; §IV-F Taxonomy Construction and Validation; §V-L Validation Results | https://arxiv.org/html/2606.05339v1 §VII Threats to Validity | Not Disclosed — exact-v1 cites awesome-mcp-servers as corpus provenance, not as this paper's versioned artifact | claim:SF-2026-ARXIV-2606-05339 | complete |
| SF-2026-ARXIV-2606-05378 | RP-1c607fe083e9cd34 | deep | arXiv:2606.05378v1 | SRC-ARXIV@arXiv:2606.05378v1 | https://arxiv.org/html/2606.05378v1 §§2–3 screen-and-ablate protocol and causal taxonomy | https://arxiv.org/html/2606.05378v1 §4 Setup; §4.3 Evaluation; §§5–10 | https://arxiv.org/html/2606.05378v1 §14 Limitations | https://github.com/skydancerosel/spectral-probe-circuits — repository disclosed; immutable event-time commit not pinned | claim:SF-2026-ARXIV-2606-05378 | complete |
| SF-2026-ARXIV-2606-05384 | RP-735fab18c50d72fd | deep | arXiv:2606.05384v1 | SRC-ARXIV@arXiv:2606.05384v1 | https://arxiv.org/html/2606.05384v1 §§3.2–3.7 post-decision protocol and ERS | https://arxiv.org/html/2606.05384v1 §§3.2–3.10; §4 Results | https://arxiv.org/html/2606.05384v1 §6 Limitations and Future Work | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05384 | complete |
| SF-2026-ARXIV-2606-05391 | RP-9c85cf5dbfe9d92b | deep | arXiv:2606.05391v1 | SRC-ARXIV@arXiv:2606.05391v1 | https://arxiv.org/html/2606.05391v1 §3. Research Methodology | https://arxiv.org/html/2606.05391v1 §4. Findings; §§4.1–4.2 | https://arxiv.org/html/2606.05391v1 §6. Limitations and Future Work | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-05391 | complete |
| SF-2026-ARXIV-2606-05395 | RP-eceecd6ae0d59b3a | deep | arXiv:2606.05395v1 | SRC-ARXIV@arXiv:2606.05395v1 | https://arxiv.org/html/2606.05395v1 §§3–4 VASO contract synthesis and verification loop | https://arxiv.org/html/2606.05395v1 §5 Empirical Evaluation; Appendices A–B | https://arxiv.org/html/2606.05395v1 §7 Limitations and Future Directions | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05395 | complete |
| SF-2026-ARXIV-2606-05396 | RP-36b39641d227dc06 | deep | arXiv:2606.05396v1 | SRC-ARXIV@arXiv:2606.05396v1 | https://arxiv.org/html/2606.05396v1 §3 Approach; §§3-A–3-D | https://arxiv.org/html/2606.05396v1 §§4–5 Experimental Setup and Results | https://arxiv.org/html/2606.05396v1 §7 Threats to Validity | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05396 | complete |
| SF-2026-ARXIV-2606-05403 | RP-bccf929c120eaefa | deep | arXiv:2606.05403v1 | SRC-ARXIV@arXiv:2606.05403v1 | https://arxiv.org/html/2606.05403v1 §2 Experimental design; §3 Behavioral results; §4 Internal representations; §5 Mechanistic analysis | https://arxiv.org/html/2606.05403v1 §2 Experimental design; Appendices A/D | https://arxiv.org/html/2606.05403v1 §6 Discussion | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-05403 | complete |
| SF-2026-ARXIV-2606-05414 | RP-137bafb2162dd7e4 | deep | arXiv:2606.05414v1 | SRC-ARXIV@arXiv:2606.05414v1 | https://arxiv.org/html/2606.05414v1 §3 Method; Appendix B Training Details | https://arxiv.org/html/2606.05414v1 §4 Experiments; §4.3 Evaluation Metrics; §5 Results | https://arxiv.org/html/2606.05414v1 §Limitations — exact unique heading | Not Disclosed — exact-v1 promises public artifacts but does not bind an immutable event-time revision | claim:SF-2026-ARXIV-2606-05414 | complete |
| SF-2026-ARXIV-2606-05415 | RP-413f31882082a3a5 | deep | arXiv:2606.05415v1 | SRC-ARXIV@arXiv:2606.05415v1 | https://arxiv.org/html/2606.05415v1 §3 executable schema contract and routing design | https://arxiv.org/html/2606.05415v1 §4 Experiments and Results; §§4.1–4.5 | https://arxiv.org/html/2606.05415v1 §Limitations — exact unique heading | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05415 | complete |
| SF-2026-ARXIV-2606-05433 | RP-e21d0d312a893898 | deep | arXiv:2606.05433v1 | SRC-ARXIV@arXiv:2606.05433v1 | https://arxiv.org/html/2606.05433v1 §3 Proposed solution; §3.1 proving architecture; §3.2 training-verification protocol | https://arxiv.org/html/2606.05433v1 Appendix B proof-cost/overhead estimation; Appendix G protocol formalization | https://arxiv.org/html/2606.05433v1 §2 Structural limitations; §3 Scope; Appendix A Open problems | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-05433 | complete |
| SF-2026-ARXIV-2606-05495 | RP-984d6fba088b477d | deep | arXiv:2606.05495v1 | SRC-ARXIV@arXiv:2606.05495v1 | https://arxiv.org/html/2606.05495v1 §4 Stream-Event-Triggered Scheduling; §§4.1–4.2 | https://arxiv.org/html/2606.05495v1 §5 Experimental Evaluations; §§5.1–5.3 | https://arxiv.org/html/2606.05495v1 §6 Conclusions — reviewed for scope; no dedicated limitations heading | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-05495 | complete |
| SF-2026-ARXIV-2606-05523 | RP-6c8ecc765f57537d | deep | arXiv:2606.05523v1 | SRC-ARXIV@arXiv:2606.05523v1 | https://arxiv.org/html/2606.05523v1 §§3–4 CHASE adversarial red-blue training loop | https://arxiv.org/html/2606.05523v1 §5 Results; Appendices E–F | https://arxiv.org/html/2606.05523v1 §Limitations and Ethical Considerations — exact unique heading | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05523 | complete |
| SF-2026-ARXIV-2606-05548 | RP-75a5dae83bf309e8 | deep | arXiv:2606.05548v1 | SRC-ARXIV@arXiv:2606.05548v1 | arXiv:2606.05548v1 exact heading "2 Methodology: LLM-as-a-Developer" and "3 ADK Arena" | arXiv:2606.05548v1 §4 Evaluation; §4.1 Experimental Setup | arXiv:2606.05548v1 §2.3 Assumptions and Scope; §5.6 Limitations | https://github.com/jintao-h/ADK-Arena — repository disclosed; event-time commit not pinned | claim:SF-2026-ARXIV-2606-05548 | complete |
| SF-2026-ARXIV-2606-05551 | RP-13886a6fd195a49a | deep | arXiv:2606.05551v1 | SRC-ARXIV@arXiv:2606.05551v1 | arXiv:2606.05551v1 Methodology: exact heading "5.2 Recommender Systems" | arXiv:2606.05551v1 Experiments: exact heading "5 Numerical Experiments" | arXiv:2606.05551v1 Scope and Limitations — exact heading or bounded scope route "6 Conclusion and Discussion" | Artifact URL disclosed in exact-v1: https://github.com/Telvc/AC-RAC | claim:SF-2026-ARXIV-2606-05551 | complete |
| SF-2026-ARXIV-2606-05558 | RP-01a6fcc57f42f45c | standard | arXiv:2606.05558v1 | SRC-ARXIV@arXiv:2606.05558v1 | arXiv:2606.05558v1 Methodology: exact heading "H.3 ψ \psi -adapter loss design" | arXiv:2606.05558v1 Experiments: exact heading "Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents" | arXiv:2606.05558v1 Scope and Limitations — exact heading or bounded scope route "Appendix A Limitations" | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-05558 | complete |
| SF-2026-ARXIV-2606-05559 | RP-bdfb895c4ce67f99 | standard | arXiv:2606.05559v1 | SRC-ARXIV@arXiv:2606.05559v1 | arXiv:2606.05559v1 Methodology: exact heading "3 Method" | arXiv:2606.05559v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05559v1 Scope and Limitations — exact heading or bounded scope route "5 Discussion" | Artifact URL disclosed in exact-v1: https://arxiv.org/abs/2404.11018 | claim:SF-2026-ARXIV-2606-05559 | complete |
| SF-2026-ARXIV-2606-05568 | RP-a249c251a7554085 | standard | arXiv:2606.05568v1 | SRC-ARXIV@arXiv:2606.05568v1 | arXiv:2606.05568v1 Methodology: exact heading "§3 Method / System Design" | arXiv:2606.05568v1 Experiments: exact heading "3. Experiments" | arXiv:2606.05568v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Artifact URL disclosed in exact-v1: https://github.com/hltcoe/ColBERTSaR | claim:SF-2026-ARXIV-2606-05568 | complete |
| SF-2026-ARXIV-2606-05597 | RP-d0e2ce011818217b | deep | arXiv:2606.05597v1 | SRC-ARXIV@arXiv:2606.05597v1 | arXiv:2606.05597v1 Methodology: exact heading "3.1 System" | arXiv:2606.05597v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05597v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-05597 | complete |
| SF-2026-ARXIV-2606-05606 | RP-4d86d0b488ae3ff5 | standard | arXiv:2606.05606v1 | SRC-ARXIV@arXiv:2606.05606v1 | arXiv:2606.05606v1 Methodology: exact heading "3 Informativeness and Utility Function Design" | arXiv:2606.05606v1 Experiments: exact heading "5 Numerical Experiments" | arXiv:2606.05606v1 Scope and Limitations — exact heading or bounded scope route "Limitations." | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-05606 | complete |
| SF-2026-ARXIV-2606-05610 | RP-ea1759cd95847fa7 | deep | arXiv:2606.05610v1 | SRC-ARXIV@arXiv:2606.05610v1 | arXiv:2606.05610v1 Methodology: exact heading "2 Method" | arXiv:2606.05610v1 Experiments: exact heading "3 Experiments" | arXiv:2606.05610v1 Scope and Limitations — exact heading or bounded scope route "Limitations" | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-05610 | complete |
| SF-2026-ARXIV-2606-05646 | RP-9c7bb08b18966f77 | standard | arXiv:2606.05646v1 | SRC-ARXIV@arXiv:2606.05646v1 | arXiv:2606.05646v1 Methodology: exact heading "§3 Method / System Design" | arXiv:2606.05646v1 Experiments: exact heading "3.4 Evaluation Regimes for Effective Reflection & Adaptive Evolution" | arXiv:2606.05646v1 Scope and Limitations — exact heading or bounded scope route "Appendix B Related Work: Extended Discussion" | Artifact URL disclosed in exact-v1: https://xhguo7.github.io/MemOp/ | claim:SF-2026-ARXIV-2606-05646 | complete |
| SF-2026-ARXIV-2606-05662 | RP-ffce6cb824c65298 | deep | arXiv:2606.05662v1 | SRC-ARXIV@arXiv:2606.05662v1 | arXiv:2606.05662v1 Methodology: exact heading "QDAG: Declarative Composition of Reusable Analytics Methodologies at LinkedIn" | arXiv:2606.05662v1 Experiments: exact heading "VI-A Demand-driven, memoized evaluation" | arXiv:2606.05662v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Artifact URL disclosed in exact-v1: https://bazel.build/ | claim:SF-2026-ARXIV-2606-05662 | complete |
| SF-2026-ARXIV-2606-05679 | RP-7ca6874ce5c3da13 | deep | arXiv:2606.05679v1 | SRC-ARXIV@arXiv:2606.05679v1 | arXiv:2606.05679v1 Methodology: exact section route "§3 Data Flow Control Policies; §4 Policy Enforcement" | arXiv:2606.05679v1 Experiments: exact section route "§5 Evaluation; §5.1 Setup" | arXiv:2606.05679v1 Scope and Limitations: exact bounded route "§1 stated monotonic SQL-92 scope; §2.2.3 Beyond Positive Relational Queries; §4.3/§4.5 enforcement limits" | Artifact URL disclosed in exact-v1: https://github.com/dataflowcontrol/data-flow-control | claim:SF-2026-ARXIV-2606-05679 | complete |
| SF-2026-ARXIV-2606-05688 | RP-63af8a26a4285743 | standard | arXiv:2606.05688v1 | SRC-ARXIV@arXiv:2606.05688v1 | arXiv:2606.05688v1 Methodology: exact heading "§3 Method / System Design" | arXiv:2606.05688v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05688v1 Scope and Limitations — exact heading or bounded scope route "5 Discussion" | Artifact URL disclosed in exact-v1: https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2 | claim:SF-2026-ARXIV-2606-05688 | complete |
| SF-2026-ARXIV-2606-05711 | RP-468795689d087b48 | standard | arXiv:2606.05711v1 | SRC-ARXIV@arXiv:2606.05711v1 | arXiv:2606.05711v1 Methodology: exact heading "Beyond Tokens: A Unified Framework for Latent Communication in LLM-based Multi-Agent Systems" | arXiv:2606.05711v1 Experiments: exact heading "7. Benchmark Analysis and Empirical Insights" | arXiv:2606.05711v1 Scope and Limitations — exact heading or bounded scope route "3.1 Limitations of Natural Language Communication" | Artifact URL disclosed in exact-v1: https://github.com/enochliu98/Awesome-Latent-Communication | claim:SF-2026-ARXIV-2606-05711 | complete |
| SF-2026-ARXIV-2606-05725 | RP-d0a6f2c0ae758900 | standard | arXiv:2606.05725v1 | SRC-ARXIV@arXiv:2606.05725v1 | arXiv:2606.05725v1 Methodology: exact heading "3 Methodology" | arXiv:2606.05725v1 Experiments: exact heading "4 Experimental Evaluations" | arXiv:2606.05725v1 Scope and Limitations — exact heading or bounded scope route "Appendix B Limitations" | Artifact URL disclosed in exact-v1: https://github.com/LabRAI/mmd-llm-mea-detection | claim:SF-2026-ARXIV-2606-05725 | complete |
| SF-2026-ARXIV-2606-05742 | RP-cd1696d000d60ff6 | standard | arXiv:2606.05742v1 | SRC-ARXIV@arXiv:2606.05742v1 | arXiv:2606.05742v1 Methodology: exact heading "3 Method" | arXiv:2606.05742v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05742v1 Scope and Limitations — exact heading or bounded scope route "Limitations" | Artifact URL disclosed in exact-v1: https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl_a_00276/1923288/tacl_a_00276.pdf | claim:SF-2026-ARXIV-2606-05742 | complete |
| SF-2026-ARXIV-2606-05743 | RP-9126b1d5fe7b2e82 | standard | arXiv:2606.05743v1 | SRC-ARXIV@arXiv:2606.05743v1 | arXiv:2606.05743v1 Methodology: exact heading "B.1 Design Principles" | arXiv:2606.05743v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05743v1 Scope and Limitations — exact heading or bounded scope route "Limitations" | Artifact URL disclosed in exact-v1: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Flash-Model-Card.pdf | claim:SF-2026-ARXIV-2606-05743 | complete |
| SF-2026-ARXIV-2606-05787 | RP-3ebc1245103c25fb | standard | arXiv:2606.05787v1 | SRC-ARXIV@arXiv:2606.05787v1 | arXiv:2606.05787v1 Methodology: exact heading "B.5 System-Prompt Defense" | arXiv:2606.05787v1 Experiments: exact heading "5 Experimental Setup" | arXiv:2606.05787v1 Scope and Limitations — exact heading or bounded scope route "3.1 Threat Model" | Artifact URL disclosed in exact-v1: https://platform.openai.com/docs/guides/embeddings | claim:SF-2026-ARXIV-2606-05787 | complete |
| SF-2026-ARXIV-2606-05800 | RP-3d9a2bd04b721f7a | standard | arXiv:2606.05800v1 | SRC-ARXIV@arXiv:2606.05800v1 | arXiv:2606.05800v1 Methodology: exact heading "3 Methodology" | arXiv:2606.05800v1 Experiments: exact heading "4 Experiment" | arXiv:2606.05800v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Artifact URL disclosed in exact-v1: https://huggingface.co/datasets/HuggingFaceH4/aime_2024 | claim:SF-2026-ARXIV-2606-05800 | complete |
| SF-2026-ARXIV-2606-05805 | RP-099be4a287feb35e | standard | arXiv:2606.05805v1 | SRC-ARXIV@arXiv:2606.05805v1 | arXiv:2606.05805v1 Methodology: exact heading "From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents" | arXiv:2606.05805v1 Experiments: exact heading "5 Experiments" | arXiv:2606.05805v1 Scope and Limitations — exact heading or bounded scope route "Limitations" | Artifact URL disclosed in exact-v1: https://github.com/YUHAOSUNABC/TRIAD | claim:SF-2026-ARXIV-2606-05805 | complete |
| SF-2026-ARXIV-2606-05828 | RP-6f1a66c1afad488d | standard | arXiv:2606.05828v1 | SRC-ARXIV@arXiv:2606.05828v1 | arXiv:2606.05828v1 Methodology: exact heading "3 Method" | arXiv:2606.05828v1 Experiments: exact heading "5 Experiment" | arXiv:2606.05828v1 Scope and Limitations — exact heading or bounded scope route "Limitations" | Artifact URL disclosed in exact-v1: https://github.com/ZyGan1999/Personalized-Skill-Selection | claim:SF-2026-ARXIV-2606-05828 | complete |
| SF-2026-ARXIV-2606-05868 | RP-9091ef047b721b35 | standard | arXiv:2606.05868v1 | SRC-ARXIV@arXiv:2606.05868v1 | arXiv:2606.05868v1 Methodology: exact heading "3 Method" | arXiv:2606.05868v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05868v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Artifact URL disclosed in exact-v1: https://github.com/open-compass/OpenFinData | claim:SF-2026-ARXIV-2606-05868 | complete |
| SF-2026-ARXIV-2606-05872 | RP-588b8d2ea54c1f93 | standard | arXiv:2606.05872v1 | SRC-ARXIV@arXiv:2606.05872v1 | arXiv:2606.05872v1 Methodology: exact heading "Entropy-Based Evaluation of AI Agents: A Lightweight Framework for Measuring Behavioral Patterns" | arXiv:2606.05872v1 Experiments: exact heading "Entropy-Based Evaluation of AI Agents: A Lightweight Framework for Measuring Behavioral Patterns" | arXiv:2606.05872v1 Scope and Limitations — exact heading or bounded scope route "5.4 Limitations" | Artifact URL disclosed in exact-v1: https://github.com/olahsymbo/agent-eval | claim:SF-2026-ARXIV-2606-05872 | complete |
| SF-2026-ARXIV-2606-05875 | RP-79a6921982c7abc3 | standard | arXiv:2606.05875v1 | SRC-ARXIV@arXiv:2606.05875v1 | arXiv:2606.05875v1 Methodology: exact heading "3. QCFuse System Design" | arXiv:2606.05875v1 Experiments: exact heading "4. Experiments" | arXiv:2606.05875v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Artifact URL disclosed in exact-v1: https://github.com/uYanJX/QCFuse | claim:SF-2026-ARXIV-2606-05875 | complete |
| SF-2026-ARXIV-2606-05894 | RP-f8f00b3d02829e59 | standard | arXiv:2606.05894v1 | SRC-ARXIV@arXiv:2606.05894v1 | arXiv:2606.05894v1 Methodology: exact heading "3 Method" | arXiv:2606.05894v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05894v1 Scope and Limitations — exact heading or bounded scope route "7 Limitations and Broader Impact" | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-05894 | complete |
| SF-2026-ARXIV-2606-05933 | RP-ba948193cc046aa6 | deep | arXiv:2606.05933v1 | SRC-ARXIV@arXiv:2606.05933v1 | arXiv:2606.05933v1 Methodology: exact heading "3. SlidingServe: Design and Implementation" | arXiv:2606.05933v1 Experiments: exact heading "5. Evaluation" | arXiv:2606.05933v1 Scope and Limitations — exact heading or bounded scope route "2.2. Limitations of Single-step Scheduling" | Artifact URL disclosed in exact-v1: https://huggingface.co/datasets/whu9/arxiv_summarization_postprocess | claim:SF-2026-ARXIV-2606-05933 | complete |
| SF-2026-ARXIV-2606-05946 | RP-a7b25ec985a9cc0e | deep | arXiv:2606.05946v1 | SRC-ARXIV@arXiv:2606.05946v1 | arXiv:2606.05946v1 Methodology: exact heading "§3 Method / System Design" | Not Disclosed — exact-v1 contains no empirical evaluation section; conceptual or method claim only | arXiv:2606.05946v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Artifact URL disclosed in exact-v1: https://creativecommons.org/licenses/by-nc-nd/4.0 | claim:SF-2026-ARXIV-2606-05946 | complete |
| SF-2026-ARXIV-2606-05951 | RP-d6c3dca000ccd3fd | deep | arXiv:2606.05951v1 | SRC-ARXIV@arXiv:2606.05951v1 | arXiv:2606.05951v1 Methodology: exact section route "§III NVSHMEM Overview; §§IV–VI memory, one-sided communication, and collectives" | arXiv:2606.05951v1 Experiments: exact section route "§VII Microbenchmarking; §VII-A Experimental Setup; §VIII DeepEP case study" | arXiv:2606.05951v1 Scope and Limitations: exact bounded route "§IX Related Work & Discussion; §X Conclusion and stated non-comprehensive performance scope" | Artifact URL disclosed in exact-v1: https://doi.org/10.1145/3581784.3607099 | claim:SF-2026-ARXIV-2606-05951 | complete |
| SF-2026-ARXIV-2606-05958 | RP-139e169acd38ecee | standard | arXiv:2606.05958v1 | SRC-ARXIV@arXiv:2606.05958v1 | arXiv:2606.05958v1 Methodology: exact heading "3 Methodology" | arXiv:2606.05958v1 Experiments: exact heading "4 Experiments" | arXiv:2606.05958v1 Scope and Limitations — exact heading or bounded scope route "3.1 Threat Model" | Artifact URL disclosed in exact-v1: https://github.com/unitaryai/detoxify. | claim:SF-2026-ARXIV-2606-05958 | complete |
| SF-2026-ARXIV-2606-05976 | RP-1d086f7ce3133ab0 | deep | arXiv:2606.05976v1 | SRC-ARXIV@arXiv:2606.05976v1 | arXiv:2606.05976v1 Methodology: exact heading "Appendix B Comparison with Published Self-Correction Methods" | arXiv:2606.05976v1 Experiments: exact heading "Verifiable reasoning benchmarks and complementary scaffolds." | arXiv:2606.05976v1 Scope and Limitations — exact heading or bounded scope route "5 Discussion" | Artifact URL disclosed in exact-v1: https://arxiv.org/abs/2202.03629v7 | claim:SF-2026-ARXIV-2606-05976 | complete |
| SF-2026-ARXIV-2606-06032 | RP-be6f04dac3103109 | deep | arXiv:2606.06032v1 | SRC-ARXIV@arXiv:2606.06032v1 | arXiv:2606.06032v1 Methodology: exact heading "§3 Method / System Design" | arXiv:2606.06032v1 Experiments: exact heading "§4 Experiments / Evaluation" | arXiv:2606.06032v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-06032 | complete |
| SF-2026-ARXIV-2606-06036 | RP-bfcea395c8f7308a | standard | arXiv:2606.06036v1 | SRC-ARXIV@arXiv:2606.06036v1 | arXiv:2606.06036v1 Methodology: exact heading "2.3 Motivation from Cognitive Memory Systems" | arXiv:2606.06036v1 Experiments: exact heading "5 Experiments" | arXiv:2606.06036v1 Scope and Limitations — exact heading or bounded scope route "7 Conclusion and Discussion" | Artifact URL disclosed in exact-v1: https://github.com/Ji-shuo/MRAgent | claim:SF-2026-ARXIV-2606-06036 | complete |
| SF-2026-ARXIV-2606-06044 | RP-267463e31a56fa96 | deep | arXiv:2606.06044v1 | SRC-ARXIV@arXiv:2606.06044v1 | arXiv:2606.06044v1 Methodology: exact heading "3 Method" | arXiv:2606.06044v1 Experiments: exact heading "4 Experimental Setup" | arXiv:2606.06044v1 Scope and Limitations — exact heading or bounded scope route "Limitations" | Artifact URL disclosed in exact-v1: https://github.com/xiaoAugenstern/LogicalRAG_TemporalQA | claim:SF-2026-ARXIV-2606-06044 | complete |
| SF-2026-ARXIV-2606-06054 | RP-e07bbb9bba77456a | deep | arXiv:2606.06054v1 | SRC-ARXIV@arXiv:2606.06054v1 | arXiv:2606.06054v1 Methodology: exact heading "IV Defense Methodology: MemGate" | arXiv:2606.06054v1 Experiments: exact heading "III-B Experimental Settings" | arXiv:2606.06054v1 Scope and Limitations — exact heading or bounded scope route "III-A Threat Model" | Artifact URL disclosed in exact-v1: https://github.com/Kevin-Zh-CS/MemGate | claim:SF-2026-ARXIV-2606-06054 | complete |
| SF-2026-ARXIV-2606-06055 | RP-f324d4b94cb3cd11 | deep | arXiv:2606.06055v1 | SRC-ARXIV@arXiv:2606.06055v1 | arXiv:2606.06055v1 Methodology: exact heading "E.7 Memory Features by Retrieval System" | arXiv:2606.06055v1 Experiments: exact heading "3 Experiments" | arXiv:2606.06055v1 Scope and Limitations — exact heading or bounded scope route "4 Discussion" | Artifact URL disclosed in exact-v1: https://arxiv. | claim:SF-2026-ARXIV-2606-06055 | complete |
| SF-2026-ARXIV-2606-06063 | RP-5eb84629be92adb4 | standard | arXiv:2606.06063v1 | SRC-ARXIV@arXiv:2606.06063v1 | arXiv:2606.06063v1 Methodology: exact heading "§3 Method / System Design" | arXiv:2606.06063v1 Experiments: exact heading "§4 Experiments / Evaluation" | arXiv:2606.06063v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-06063 | complete |
| SF-2026-ARXIV-2606-06079 | RP-ee21741e1294a422 | standard | arXiv:2606.06079v1 | SRC-ARXIV@arXiv:2606.06079v1 | arXiv:2606.06079v1 Methodology: exact heading "§3 Method / System Design" | arXiv:2606.06079v1 Experiments: exact heading "§4 Experiments / Evaluation" | arXiv:2606.06079v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries" | Not Disclosed — no immutable event-time artifact revision used for claims | claim:SF-2026-ARXIV-2606-06079 | complete |
| SF-2026-ARXIV-2606-06087 | RP-348f21f1d67b5c82 | standard | arXiv:2606.06087v1 | SRC-ARXIV@arXiv:2606.06087v1 | arXiv:2606.06087v1 Methodology: exact heading "§3 Method" | arXiv:2606.06087v1 Experiments: exact heading "§4 Experiments" | arXiv:2606.06087v1 Scope and Limitations — exact heading or bounded scope route "§5 Conclusion and stated scope" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06087 | complete |
| SF-2026-ARXIV-2606-06090 | RP-89ffb6fd83a672fe | deep | arXiv:2606.06090v1 | SRC-ARXIV@arXiv:2606.06090v1 | arXiv:2606.06090v1 Methodology: exact heading "§3 Method; §3.2–3.3 execution-state tree and operations" | arXiv:2606.06090v1 Experiments: exact heading "§4 Experiments; §4.1 Experimental Setup" | arXiv:2606.06090v1 Scope and Limitations — exact heading or bounded scope route "§5 Conclusion; Appendix C Bounded Context Growth" | arXiv:2606.06090v1 Appendix A Experiment Details; no immutable repository revision identified | claim:SF-2026-ARXIV-2606-06090 | complete |
| SF-2026-ARXIV-2606-06178 | RP-246e2a7b7359fec1 | standard | arXiv:2606.06178v1 | SRC-ARXIV@arXiv:2606.06178v1 | arXiv:2606.06178v1 Methodology: exact heading "§4 Methodology" | arXiv:2606.06178v1 Experiments: exact heading "§5 Experiments; §5.1 Experiment Setup" | arXiv:2606.06178v1 Scope and Limitations — exact heading or bounded scope route "§5.4 Generalization and Scalability; §6 Conclusion" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06178 | complete |
| SF-2026-ARXIV-2606-06223 | RP-4ad99ec552538a09 | standard | arXiv:2606.06223v1 | SRC-ARXIV@arXiv:2606.06223v1 | arXiv:2606.06223v1 Methodology: exact heading "§3 Method" | arXiv:2606.06223v1 Experiments: exact heading "§4 Experimental Setup and Results" | arXiv:2606.06223v1 Scope and Limitations — exact heading or bounded scope route "§5 Discussion and Limitations" | arXiv:2606.06223v1 Appendices A–C monitor details and diagnostics; no immutable repository revision identified | claim:SF-2026-ARXIV-2606-06223 | complete |
| SF-2026-ARXIV-2606-06240 | RP-b5bd60d67617df80 | deep | arXiv:2606.06240v1 | SRC-ARXIV@arXiv:2606.06240v1 | arXiv:2606.06240v1 Methodology: exact heading "§3 The Toki Operator Algebra" | arXiv:2606.06240v1 Experiments: exact heading "§4 Empirical Validation" | arXiv:2606.06240v1 Scope and Limitations — exact heading or bounded scope route "§6 Limitations and Conclusion; Appendix G Negative Results and Scope Limits" | arXiv:2606.06240v1 Appendix F Artifact Reproducibility Runbook; immutable commit not established | claim:SF-2026-ARXIV-2606-06240 | complete |
| SF-2026-ARXIV-2606-06256 | RP-474c21c2b756ff37 | deep | arXiv:2606.06256v1 | SRC-ARXIV@arXiv:2606.06256v1 | arXiv:2606.06256v1 Methodology: exact heading "§4 RedKnot Design" | arXiv:2606.06256v1 Experiments: exact heading "§5 Evaluation; §5.1 Experimental Setup" | arXiv:2606.06256v1 Scope and Limitations — exact heading or bounded scope route "§6 Future Work" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06256 | complete |
| SF-2026-ARXIV-2606-06284 | RP-16d2a47aec90ac1e | deep | arXiv:2606.06284v1 | SRC-ARXIV@arXiv:2606.06284v1 | arXiv:2606.06284v1 Methodology: exact heading "§4 Causal Minimal Tool Filtering" | arXiv:2606.06284v1 Experiments: exact heading "§5 Benchmark Design; §6 Experimental Setup; §7 Results" | arXiv:2606.06284v1 Scope and Limitations — exact heading or bounded scope route "§5.5 Scope and later limitations discussion" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06284 | complete |
| SF-2026-ARXIV-2606-06302 | RP-78f5e6d725815495 | standard | arXiv:2606.06302v1 | SRC-ARXIV@arXiv:2606.06302v1 | arXiv:2606.06302v1 Methodology: exact heading "§4 Methodology" | arXiv:2606.06302v1 Experiments: exact heading "§5 Evaluation; §5.1 Evaluation Setup" | arXiv:2606.06302v1 Scope and Limitations — exact heading or bounded scope route "§3.1 Limitations on existing system; §7 Conclusion" | https://github.com/aiha-lab/TANGRAM — repository disclosed; immutable event-time commit not pinned | claim:SF-2026-ARXIV-2606-06302 | complete |
| SF-2026-ARXIV-2606-06324 | RP-2c96029762894a15 | deep | arXiv:2606.06324v1 | SRC-ARXIV@arXiv:2606.06324v1 | arXiv:2606.06324v1 Methodology: exact heading "§III Approach" | arXiv:2606.06324v1 Experiments: exact heading "§IV Experimental Design; §V Results and Analysis" | arXiv:2606.06324v1 Scope and Limitations — exact heading or bounded scope route "§VI Discussion; §VIII Conclusion" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06324 | complete |
| SF-2026-ARXIV-2606-06337 | RP-0727af0fdad5d43e | standard | arXiv:2606.06337v1 | SRC-ARXIV@arXiv:2606.06337v1 | arXiv:2606.06337v1 Methodology: exact heading "§IV System Architecture; §§V–VIII pipelines" | arXiv:2606.06337v1 Experiments: exact heading "§X Experimental Setup; §XI Results" | arXiv:2606.06337v1 Scope and Limitations — exact heading or bounded scope route "§XIII Limitations and Future Work" | https://github.com/Shweta-Mishra-ai/tokenmizer — repository disclosed; immutable event-time commit not pinned | claim:SF-2026-ARXIV-2606-06337 | complete |
| SF-2026-ARXIV-2606-06387 | RP-d27943b76100556a | deep | arXiv:2606.06387v1 | SRC-ARXIV@arXiv:2606.06387v1 | arXiv:2606.06387v1 Methodology: exact heading "§3 Mid-Session Tool Injection" | arXiv:2606.06387v1 Experiments: exact heading "§4 Experimental Setup; §5 Results" | arXiv:2606.06387v1 Scope and Limitations — exact heading or bounded scope route "§9 Limitations" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06387 | complete |
| SF-2026-ARXIV-2606-06438 | RP-3ec166c42aea7477 | deep | arXiv:2606.06438v1 | SRC-ARXIV@arXiv:2606.06438v1 | arXiv:2606.06438v1 Methodology: exact heading "§3 CarbonSim Design" | arXiv:2606.06438v1 Experiments: exact heading "§4 Results" | arXiv:2606.06438v1 Scope and Limitations — exact heading or bounded scope route "§5 Discussion and Future Work" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06438 | complete |
| SF-2026-ARXIV-2606-06448 | RP-3bfb6957a2ed0241 | deep | arXiv:2606.06448v1 | SRC-ARXIV@arXiv:2606.06448v1 | arXiv:2606.06448v1 Methodology: exact heading "§2 Agent Memory Paradigms; §3 Workload Suite and Profiling Harness" | arXiv:2606.06448v1 Experiments: exact heading "§4 Characterizing Agent Memory Workloads" | arXiv:2606.06448v1 Scope and Limitations — exact heading or bounded scope route "§5 Discussion and Conclusion" | Not Disclosed — no immutable event-time artifact revision identified | claim:SF-2026-ARXIV-2606-06448 | complete |
| SF-2026-ARXIV-2606-06453 | RP-8e3cb69852d864dc | deep | arXiv:2606.06453v1 | SRC-ARXIV@arXiv:2606.06453v1 | arXiv:2606.06453v1 Methodology: exact heading "§3 Programming Model; §4 Interpretation; §5 Execution Optimizations" | arXiv:2606.06453v1 Experiments: exact heading "§6 Evaluation; §6.4 Efficiency Evaluations" | arXiv:2606.06453v1 Scope and Limitations — exact heading or bounded scope route "§7 Conclusion; §11 Ablation Study" | https://github.com/Infini-AI-Lab/vortex_torch — repository disclosed; immutable event-time commit not pinned | claim:SF-2026-ARXIV-2606-06453 | complete |
| SF-2026-ARXIV-2606-06460 | RP-5a8050f1672727cf | deep | arXiv:2606.06460v1 | SRC-ARXIV@arXiv:2606.06460v1 | arXiv:2606.06460v1 Methodology: exact heading "§3 Recuse Signal; §4 Adapters" | arXiv:2606.06460v1 Experiments: exact heading "§5 Experimental Design; §6 Pilot Results" | arXiv:2606.06460v1 Scope and Limitations — exact heading or bounded scope route "§9 Limitations and Future Work" | arXiv:2606.06460v1 §10 Reproducibility — standard, adapters and harness disclosed; immutable revision not pinned | claim:SF-2026-ARXIV-2606-06460 | complete |
| SF-2026-ARXIV-2606-06467 | RP-e3cf61983cdd427f | standard | arXiv:2606.06467v1 | SRC-ARXIV@arXiv:2606.06467v1 | arXiv:2606.06467v1 Methodology: exact heading "§2 Method" | arXiv:2606.06467v1 Experiments: exact heading "§3 Experiments; §3.1 Setup" | arXiv:2606.06467v1 Scope and Limitations — exact heading or bounded scope route "§5 Conclusion; Appendix D/E experimental-scope details" | arXiv:2606.06467v1 Appendices D–E experimental details; no immutable repository revision identified | claim:SF-2026-ARXIV-2606-06467 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-05241:start -->
### 2606.05241 — Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation

**问题、旧方案与约束变化。** 允许 web search 的 deep-research agent 可检索 benchmark metadata、题面甚至答案，使公开测试不再隔离训练/推理证据。

**Mechanism、state / data / control owner 与实现。** 研究定义 metadata、question-context、explicit-answer 三层 STC，并从 search traces 检测泄漏、重算去污染结果。browser trace 持有检索证据，benchmark owner 保存题目身份，contamination auditor 决定样本是否计分。

**Evaluation contract、证明与未证明。** 六个公开 benchmark 上最多约4%的 inflation 只针对所测 agents/search index/time；没有证明私有 benchmark 或未来索引同样幅度。

**Trade-off、failure mode 与旧方案共存边界。** trace-aware filtering提高有效性，却可能误删合法检索并增加评测成本；真实开放网任务仍需允许搜索，只是不能与 closed-book score 混算。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation isolation 从训练集去重扩展到 inference-time retrieval data flow。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05241v1 §3 Methodology; §§3.1–3.2`；Evaluation：`https://arxiv.org/html/2606.05241v1 §§4–5 Evaluation and Experiment; Appendices C–E`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05241v1 Limitations; §6 Discussion`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05241:start -->可引用结论只限 `arXiv:2606.05241v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05241:end -->
<!-- review:SF-2026-ARXIV-2606-05241:end -->

<!-- review:SF-2026-ARXIV-2606-05271:start -->
### 2606.05271 — BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference

**问题、旧方案与约束变化。** edge SoC 把整模型固定到 CPU/GPU/NPU 简单稳定，却忽略不同 fused operator 对各 processing unit 的 latency/energy 差异。

**Mechanism、state / data / control owner 与实现。** BIDENT 离线 profile H2D、dispatch、kernel、D2H 与能耗，将 operator-PU choice 编成 weighted execution graph 并求 shortest path。profile DB 持有 cost state，operators/tensors 是数据，mapper 掌握 placement。

**Evaluation contract、证明与未证明。** 实验只对 Intel Core Ultra 平台、所列10类模型/FP16/INT8 与 profiler cost model 证明 latency/energy mapping；未证明动态 contention 下仍最优。

**Trade-off、failure mode 与旧方案共存边界。** operator mapping提高异构利用率，却增加切分、transfer、profiling 和 recompile 成本；单一 PU 已匹配 workload 或模型很小时 model-level placement 更简单。

**演进关系与系统位置。** 这是 INFER-TENSORRT-LLM execution-plan 的 Direct Evolution：placement 粒度从 model 降到 fused operator，并把 transfer cost 纳入路径。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05271v1 §3. BIDENT Framework; §§3.4–3.5`；Evaluation：`https://arxiv.org/html/2606.05271v1 §4. Evaluation; §4.1 Experimental Setup`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05271v1 §3.4 Framework Overhead; §7. Conclusion`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-05271:start -->可引用结论只限 `arXiv:2606.05271v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05271:end -->
<!-- review:SF-2026-ARXIV-2606-05271:end -->

<!-- review:SF-2026-ARXIV-2606-05304:start -->
### 2606.05304 — What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems

**问题、旧方案与约束变化。** multi-agent 共享完整自然语言 transcript 保留信息但会膨胀 token/context；固定摘要策略又可能丢掉下游真正需要的动作状态。

**Mechanism、state / data / control owner 与实现。** PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。

**Evaluation contract、证明与未证明。** 作者在所列 MAS topologies/models/tasks 上比较五种 communication strategies，证明无固定策略普适且 PACT 的 cost/quality 权衡；不证明所有协作任务都可压缩为同一 schema。

**Trade-off、failure mode 与旧方案共存边界。** 结构化 state update 降低 token，却可能丢失解释、弱化异常协商并增加 schema evolution；小团队、短任务仍可共享完整文本。

**演进关系与系统位置。** 这是 AGENT-MULTI-AGENT 的 Direct Evolution：通信从 transcript forwarding 变成有 ownership 的状态复制协议。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05304v1 §4 PACT; §§4.1–4.3 action-state message space and protocol properties`；Evaluation：`https://arxiv.org/html/2606.05304v1 §5 Experiments; §6 Agentic Coding Harnesses`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05304v1 §Limitations`；Artifact：`https://github.com/iNLP-Lab/PACT — repository disclosed; exact-v1 does not pin an immutable event-time commit`。

<!-- claim:SF-2026-ARXIV-2606-05304:start -->可引用结论只限 `arXiv:2606.05304v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05304:end -->
<!-- review:SF-2026-ARXIV-2606-05304:end -->

<!-- review:SF-2026-ARXIV-2606-05308:start -->
### 2606.05308 — Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference

**问题、旧方案与约束变化。** 大规模 LLM judge 便宜但有系统偏差，少量 human labels 可靠却方差高；直接用任一方都难同时获得规模和统计保证。

**Mechanism、state / data / control owner 与实现。** PRECISE 用 prediction-powered inference 将大规模 judge predictions 与小规模 human residual correction 合成 bias-corrected ranking metric，并为 Precision@K 压缩 output-space computation。human labels 是校准数据，judge scores 是辅助信号，estimator 持有置信区间控制。

**Evaluation contract、证明与未证明。** ESCI 的30 human-gold/60,000 judge slice 只证明所列 ranking metrics 的校正与区间性质；不证明 judge 单样本标签正确或任意分布漂移下仍无偏。

**Trade-off、failure mode 与旧方案共存边界。** PPI 降低人工标注量，却依赖 probability sample、稳定 estimand 和正确 variance accounting；无法随机抽样时应回到更多 human evaluation。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：LLM judge 从替代真值变成可校正的低成本测量器。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05308v1 §2 Method`；Evaluation：`https://arxiv.org/html/2606.05308v1 §3 Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05308v1 Limitations; §4 Future Work`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05308:start -->可引用结论只限 `arXiv:2606.05308v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05308:end -->
<!-- review:SF-2026-ARXIV-2606-05308:end -->

<!-- review:SF-2026-ARXIV-2606-05339:start -->
### 2606.05339 — A Taxonomy of Runtime Faults in Model Context Protocol Servers

**问题、旧方案与约束变化。** MCP 的 schema 合法并不意味着 server runtime 正确；配置未生效、state、provider、timeout 等故障跨越 protocol 与实现 owner。

**Mechanism、state / data / control owner 与实现。** 研究对473 repositories中的837 fault threads做 bottom-up coding，形成11大类、27子类/73 leaf faults，并按 interaction、tool、schema、state、安全和取消路径分配故障类型。issue evidence 是数据，taxonomy 是诊断状态，maintainer/release process 掌握修复控制。

**Evaluation contract、证明与未证明。** 经验 taxonomy 只代表筛选时间窗、活跃 repositories 与 issue-reporting bias；不能当作运行时故障率或完备故障集合。

**Trade-off、failure mode 与旧方案共存边界。** 分类改善 triage/测试覆盖，却不会自动检测 silent faults，且 taxonomy 会随协议演化；单一 MCP server 仍需本地 invariants、chaos tests 和 tracing。

**演进关系与系统位置。** 这是 AGENT-MCP/PLATFORM-OBSERVABILITY 的 Layering / Dependency：wire contract 之上增加 server-runtime reliability owner。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05339v1 §IV Methodology; §§IV-A–IV-G; §V Results: MCP Server Fault Taxonomy`；Evaluation：`https://arxiv.org/html/2606.05339v1 §IV-D Selection of Repositories for Manual Analysis; §IV-F Taxonomy Construction and Validation; §V-L Validation Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05339v1 §VII Threats to Validity`；Artifact：`Not Disclosed — exact-v1 cites awesome-mcp-servers as corpus provenance, not as this paper's versioned artifact`。

<!-- claim:SF-2026-ARXIV-2606-05339:start -->可引用结论只限 `arXiv:2606.05339v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05339:end -->
<!-- review:SF-2026-ARXIV-2606-05339:end -->

<!-- review:SF-2026-ARXIV-2606-05378:start -->
### 2606.05378 — Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models

**问题、旧方案与约束变化。** attention head 对任务 pattern 有选择性并在 ablation 后影响输出，常被直接解释为稳定 task circuit；跨模型复制时这种相关到因果的跃迁未被证明。

**Mechanism、state / data / control owner 与实现。** 统一 screen-and-ablate protocol 在四任务、三种1B architecture上比较 matched-random null，并把 head 归为 primary/secondary cause、correlate、interferer 或 null。activations 是观测数据，ablation controller 施加干预，taxonomy 持有因果判定。

**Evaluation contract、证明与未证明。** 12个 task-model cells 无两项共享可比 primary screen，证明该 recipe 的具体 circuit 不可稳定移植；不证明机制完全不可解释或更大模型也无共享结构。

**Trade-off、failure mode 与旧方案共存边界。** 更严格 null/干预降低夸大结论，却提高实验成本并可能错过分布式机制；pattern screening 仍可作候选发现，但不能独立成为 causal claim。

**演进关系与系统位置。** 这是 MODEL-ATTENTION/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution（认知修正）：selectivity 被降级为 discovery evidence，causality 需要跨条件干预。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05378v1 §§2–3 screen-and-ablate protocol and causal taxonomy`；Evaluation：`https://arxiv.org/html/2606.05378v1 §4 Setup; §4.3 Evaluation; §§5–10`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05378v1 §14 Limitations`；Artifact：`https://github.com/skydancerosel/spectral-probe-circuits — repository disclosed; immutable event-time commit not pinned`。

<!-- claim:SF-2026-ARXIV-2606-05378:start -->可引用结论只限 `arXiv:2606.05378v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05378:end -->
<!-- review:SF-2026-ARXIV-2606-05378:end -->

<!-- review:SF-2026-ARXIV-2606-05384:start -->
### 2606.05384 — Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges

**问题、旧方案与约束变化。** LLM judge pipeline 默认一次评分是固定输入的稳定属性；若允许评分后对话，参与者可在不改变原答案的情况下诱导 verdict reversal。

**Mechanism、state / data / control owner 与实现。** protocol 先固定 initial decision，再施加 repeated/neutral、anti-baseline 与 counterbalanced target challenges，用 ERS 等指标分离稳定性、可逆性和定向操纵。conversation state 是新增数据，judge 持有 verdict，evaluation harness 控制挑战顺序。

**Evaluation contract、证明与未证明。** MT-Bench/AlpacaEval、GPT-4o/4o-mini judges 与100 paired instances 只证明所测 interaction 可改变判定；不证明所有 judge 或无对话 benchmark 均可操纵。

**Trade-off、failure mode 与旧方案共存边界。** 冻结 judge context 或禁止 post-decision interaction增强可复现性，却不适合需要申诉的流程；有申诉时应使用独立复审而非继续劝说同一 judge。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：judge contract 从纯函数扩展为有状态交互协议。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05384v1 §§3.2–3.7 post-decision protocol and ERS`；Evaluation：`https://arxiv.org/html/2606.05384v1 §§3.2–3.10; §4 Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05384v1 §6 Limitations and Future Work`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05384:start -->可引用结论只限 `arXiv:2606.05384v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05384:end -->
<!-- review:SF-2026-ARXIV-2606-05384:end -->

<!-- review:SF-2026-ARXIV-2606-05391:start -->
### 2606.05391 — Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents

**问题、旧方案与约束变化。** agent oversight 常被抽象成最终 review；实践中开发者必须在执行前、规划时、运行中和事后分配不同注意力与权限。

**Mechanism、state / data / control owner 与实现。** 访谈归纳 a priori control、co-planning、real-time monitoring、post-hoc review 及配套 heuristics。human 持有最终责任和 override，agent plan/action/trace 是审查数据，workflow 决定何时暂停或升级。

**Evaluation contract、证明与未证明。** 17名经验开发者的定性访谈提供早期实践锚点，不是频率估计、因果效果或行业代表样本。

**Trade-off、failure mode 与旧方案共存边界。** 多阶段 oversight 提高可控性，却带来认知负担、alert fatigue 和吞吐下降；低风险、可回滚任务可减少实时介入。

**演进关系与系统位置。** 这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Layering / Dependency：human-in-the-loop 从单一批准点演变为分阶段控制面。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05391v1 §3. Research Methodology`；Evaluation：`https://arxiv.org/html/2606.05391v1 §4. Findings; §§4.1–4.2`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05391v1 §6. Limitations and Future Work`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-05391:start -->可引用结论只限 `arXiv:2606.05391v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05391:end -->
<!-- review:SF-2026-ARXIV-2606-05391:end -->

<!-- review:SF-2026-ARXIV-2606-05395:start -->
### 2606.05395 — VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents

**问题、旧方案与约束变化。** physical-agent skill 通过 sampled rollout、unit test 或 LLM critique 演进，只证明见过的轨迹成功，不能保证未采样条件下的 temporal safety。

**Mechanism、state / data / control owner 与实现。** VASO 将 skill 表示为 planner-facing interface 与 formal state/action proposition contract，迭代生成 labeling function、model checking counterexample 和 skill refinement。contract 持有安全状态，robot plan 是数据，verifier 掌握执行前授权。

**Evaluation contract、证明与未证明。** §5 在两平台、11 specifications、400 plans及40 plans/skill 的局部合同上比较 compliance；没有证明 perception/actuator model 完整或 sim-to-real 物理安全。

**Trade-off、failure mode 与旧方案共存边界。** formal gate提高未采样路径约束，却依赖 proposition alignment，且 state-space/solver 成本可能很高；低风险 skill 仍可用 test+monitoring。

**演进关系与系统位置。** 这是 MULTIMODAL-EMBODIED-VLA/AGENT-SKILL 的 Direct Evolution：skill 从 prompt artifact 变成带形式契约和发布 gate 的执行组件。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05395v1 §§3–4 VASO contract synthesis and verification loop`；Evaluation：`https://arxiv.org/html/2606.05395v1 §5 Empirical Evaluation; Appendices A–B`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05395v1 §7 Limitations and Future Directions`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05395:start -->可引用结论只限 `arXiv:2606.05395v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05395:end -->
<!-- review:SF-2026-ARXIV-2606-05395:end -->

<!-- review:SF-2026-ARXIV-2606-05396:start -->
### 2606.05396 — Willing but Unable: Separating Refusal from Capability in Code LLMs via Abliteration

**问题、旧方案与约束变化。** 安全对齐的 code LLM 拒绝生成脆弱代码，使 benchmark 把 refusal 与缺乏 vulnerability-injection capability 混为一谈。

**Mechanism、state / data / control owner 与实现。** abliteration 估计 residual-stream refusal direction 并作低秩正交投影，再把生成结果分为 refusal、compile/correctness 与 CWE-89 injection success。权重 edit 持有 policy change，safe code/spec 是输入数据，evaluation harness 分离 willingness 与 ability。

**Evaluation contract、证明与未证明。** Python/CWE-89、Qwen2.5-Coder 3B/7B/14B、Q4_K_M/Ollama 的初步实验只证明该受限 case；不证明编辑保持其他安全性或能构造高质量通用漏洞数据。

**Trade-off、failure mode 与旧方案共存边界。** 移除 refusal 改善 capability measurement，却显著扩大滥用风险并可能损坏模型行为；只能在隔离研究环境使用，生产模型不应采用。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM 的 Alternative Branch：能力评测先控制 refusal policy，再评价任务能力，但不把 edited model 当部署方案。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05396v1 §3 Approach; §§3-A–3-D`；Evaluation：`https://arxiv.org/html/2606.05396v1 §§4–5 Experimental Setup and Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05396v1 §7 Threats to Validity`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05396:start -->可引用结论只限 `arXiv:2606.05396v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05396:end -->
<!-- review:SF-2026-ARXIV-2606-05396:end -->

<!-- review:SF-2026-ARXIV-2606-05403:start -->
### 2606.05403 — Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation

**问题、旧方案与约束变化。** multi-source synthesis 常假设模型会按统计有效性加权来源；模型可能识别单独的伪造统计，却在合成时只响应“像方法学”的表达风格。

**Mechanism、state / data / control owner 与实现。** 实验正交操纵 methodology register 与 numerical validity，比较单源识别和多源 influence。source text/number 是证据数据，synthesis model 持有权重分配，validity probe 检查是否调用已具备的识别能力。

**Evaluation contract、证明与未证明。** 五模型、三领域的行为 dissociation 只证明所构造 impossible CI 等操纵下的 epistemic blind spot；不证明所有引用审查或 tool-verified agent 都失败。

**Trade-off、failure mode 与旧方案共存边界。** 外部统计 verifier/claim decomposition提高可靠性，却增加延迟并要求可机器检查的证据；低风险摘要可保留模型合成但标注不确定性。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM/AGENT-RAG 的 Direct Evolution：source ranking 从文风/相关性扩展为可验证的 claim-level validity gate。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05403v1 §2 Experimental design; §3 Behavioral results; §4 Internal representations; §5 Mechanistic analysis`；Evaluation：`https://arxiv.org/html/2606.05403v1 §2 Experimental design; Appendices A/D`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05403v1 §6 Discussion`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-05403:start -->可引用结论只限 `arXiv:2606.05403v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05403:end -->
<!-- review:SF-2026-ARXIV-2606-05403:end -->

<!-- review:SF-2026-ARXIV-2606-05414:start -->
### 2606.05414 — When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories

**问题、旧方案与约束变化。** early failure classifier 只有 trajectory-level label，传统做法把终局失败复制给每个 prefix；多轮对话中失败证据稀疏且延迟，这会制造错误的 turn-level supervision。

**Mechanism、state / data / control owner 与实现。** attention-based predictor 从整体 label 学稀疏 turn evidence，再以 risk estimate 驱动可调 alert/stop policy。partial trajectory 是数据状态，risk model 更新 failure belief，threshold controller 掌握中止/升级。

**Evaluation contract、证明与未证明。** §§4–5 只在指定 dialog/agent datasets 与 metrics 上证明比 prefix-label baselines 更好的 early-warning tradeoff；不证明 production threshold 或 causal root cause。

**Trade-off、failure mode 与旧方案共存边界。** 弱监督减少 turn labels，却可能把相关语句误作早期因果信号；风险低或误停代价高时应延后 alert 并保留完整执行。

**演进关系与系统位置。** 这是 AGENT-WORKFLOW/PLATFORM-OBSERVABILITY 的 Direct Evolution：监控从事后 outcome 变成随 trajectory 更新的在线控制信号。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05414v1 §3 Method; Appendix B Training Details`；Evaluation：`https://arxiv.org/html/2606.05414v1 §4 Experiments; §4.3 Evaluation Metrics; §5 Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05414v1 §Limitations — exact unique heading`；Artifact：`Not Disclosed — exact-v1 promises public artifacts but does not bind an immutable event-time revision`。

<!-- claim:SF-2026-ARXIV-2606-05414:start -->可引用结论只限 `arXiv:2606.05414v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05414:end -->
<!-- review:SF-2026-ARXIV-2606-05414:end -->

<!-- review:SF-2026-ARXIV-2606-05415:start -->
### 2606.05415 — Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval

**问题、旧方案与约束变化。** 多源 tables/documents/files 的语义隐含且 schema 不一；直接 vector search 绕过结构，手工 schema 又昂贵且难随来源演进。

**Mechanism、state / data / control owner 与实现。** 系统用 closed-world field catalog 约束 schema discovery，确定性推断 keys/hierarchy，并以同一 executable schema 驱动 extraction、dedup、KG linking 与多工具 retrieval。schema/version 持有契约，provenance graph 是状态，router 控制查询路径。

**Evaluation contract、证明与未证明。** §4 只在作者数据与 query workload 上证明 ingestion/retrieval traceability；没有证明任意隐含语义可自动恢复或 schema extension 无冲突。

**Trade-off、failure mode 与旧方案共存边界。** 共享契约提高一致性，却增加 catalog governance、identity resolution 和 migration；同质单源可直接使用原生 schema/search。

**演进关系与系统位置。** 这是 TRAIN-DATA→AGENT-RAG 的 Direct Evolution：schema 从摄取产物变成贯穿构建与查询的可执行、带 provenance 控制面。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05415v1 §3 executable schema contract and routing design`；Evaluation：`https://arxiv.org/html/2606.05415v1 §4 Experiments and Results; §§4.1–4.5`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05415v1 §Limitations — exact unique heading`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05415:start -->可引用结论只限 `arXiv:2606.05415v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05415:end -->
<!-- review:SF-2026-ARXIV-2606-05415:end -->

<!-- review:SF-2026-ARXIV-2606-05433:start -->
### 2606.05433 — Zero knowledge verification for frontier AI training is possible

**问题、旧方案与约束变化。** frontier training regulation以累计 compute 为阈值却依赖厂商自报；传统完整重放或逐算子证明在该规模不可行。

**Mechanism、state / data / control owner 与实现。** 方案预提交 training specification，采集 inter-node network observations，并在线生成 intermediate-computation Merkle commitments，使用具 native tensor primitives 的 zkVM 抽查/证明。trainer 持有执行状态，commitments/telemetry 是审计数据，verifier 掌握合规判定。

**Evaluation contract、证明与未证明。** Appendix B/G 给出 proof-cost估算与协议论证，而非 frontier-scale end-to-end deployment；没有证明硬件 telemetry 完整、spec 与真实训练语义完全一致。

**Trade-off、failure mode 与旧方案共存边界。** 零知识审计保护模型/数据机密，却增加 commitment、proof、trusted instrumentation 与 protocol complexity；低风险训练可继续使用日志和第三方 audit。

**演进关系与系统位置。** 这是 PLATFORM-SECURITY/GOVERNANCE 的 Layering / Dependency：在既有发布审计与 provenance owner 上增加可验证计算记录；现有安全章节能够承载，无需 Structural Candidate。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05433v1 §3 Proposed solution; §3.1 proving architecture; §3.2 training-verification protocol`；Evaluation：`https://arxiv.org/html/2606.05433v1 Appendix B proof-cost/overhead estimation; Appendix G protocol formalization`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05433v1 §2 Structural limitations; §3 Scope; Appendix A Open problems`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-05433:start -->可引用结论只限 `arXiv:2606.05433v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05433:end -->
<!-- review:SF-2026-ARXIV-2606-05433:end -->

<!-- review:SF-2026-ARXIV-2606-05495:start -->
### 2606.05495 — SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines

**问题、旧方案与约束变化。** CUDA Graph 降低单图 launch overhead，但 static batching/global polling 仍产生 inter-batch gap、延迟和 active-buffer 冲突。

**Mechanism、state / data / control owner 与实现。** SET 为每 worker 绑定 stream、pre-instantiated graph 和独立 buffers，用 event chaining/work stealing 在完成时派发下一 job。per-stream buffer 持有 in-flight state，CUDA events 是控制信号，scheduler 掌握 worker/slot 所有权。

**Evaluation contract、证明与未证明。** §5 在 RTX3090/5090 两平台、六 workloads 和 workload-specific batch sweep 上报告 throughput/overhead；不证明 LLM serving、跨 GPU 或生产 tail SLO。

**Trade-off、failure mode 与旧方案共存边界。** 事件触发减少 host gap，却增加 buffer memory、event dependency 与 scheduler complexity；低并发、单 graph workload 仍可用同步 replay。

**演进关系与系统位置。** 这是 INFER-EXECUTION 的 Principle Reuse：continuous scheduling 的状态所有权下沉到 CUDA graph pipeline，但不能直接外推成 LLM runtime 结论。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05495v1 §4 Stream-Event-Triggered Scheduling; §§4.1–4.2`；Evaluation：`https://arxiv.org/html/2606.05495v1 §5 Experimental Evaluations; §§5.1–5.3`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05495v1 §6 Conclusions — reviewed for scope; no dedicated limitations heading`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-05495:start -->可引用结论只限 `arXiv:2606.05495v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05495:end -->
<!-- review:SF-2026-ARXIV-2606-05495:end -->

<!-- review:SF-2026-ARXIV-2606-05523:start -->
### 2606.05523 — CHASE: Adversarial Red-Blue Teaming for Improving LLM Safety using Reinforcement Learning

**问题、旧方案与约束变化。** 静态 safety data 或 white-box attack 优化难覆盖部署中的自适应 black-box prompt rewriting；固定 red-team corpus 很快失去压力。

**Mechanism、state / data / control owner 与实现。** CHASE 让 attacker 用 GRPO 优化 bypass×intent fidelity，defender 用 harvested rewrites 经 GRPO 与 rejection-sampled SFT 强化，并混入 benign data。attacker/defender checkpoints 持有对抗状态，rewrites/rewards 是数据，co-evolution loop 控制迭代。

**Evaluation contract、证明与未证明。** §5/appendices 只在 Llama-3.1-8B-Instruct、指定 attacks/evaluators 上证明所测 robustness 变化；未证明对 frontier models、长期自博弈或未知攻击无 reward hacking。

**Trade-off、failure mode 与旧方案共存边界。** 在线生成 hard negatives提高适应性，却增加训练成本、评价器依赖和 catastrophic alignment drift；稳定威胁下 curated SFT 仍更可控。

**演进关系与系统位置。** 这是 TRAIN-RLHF/PLATFORM-SECURITY 的 Direct Evolution：red teaming 从发布前数据集变成闭环 attacker–defender control process。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05523v1 §§3–4 CHASE adversarial red-blue training loop`；Evaluation：`https://arxiv.org/html/2606.05523v1 §5 Results; Appendices E–F`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05523v1 §Limitations and Ethical Considerations — exact unique heading`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05523:start -->可引用结论只限 `arXiv:2606.05523v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05523:end -->
<!-- review:SF-2026-ARXIV-2606-05523:end -->

<!-- review:SF-2026-ARXIV-2606-05548:start -->
### 2606.05548 — ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer

**问题、旧方案与约束变化。** Freezing the developer, ADK API/documentation surface, isolated runner, generation effort and downstream agent outcomes changes how Agent frameworks are compared rather than merely adding one task score. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-EVALUATION-SYSTEM`。

**机制、实现与 ownership。** The manuscript holds the coding developer model fixed, gives every framework an isolated Docker environment, validates that generated code actually imports the target framework, and runs uniform adapters over four benchmark families. This turns documentation usability, repair effort and resulting agent behavior into separate observables. The experiment covers 51 Python frameworks and 204 framework–benchmark pairs, but the reported generation cost and success are conditional on the frozen documentation, prompts, GPT-5.4 Nano, adapter implementation and test suites. They do not measure intrinsic API complexity or prove that a framework will rank the same under a different developer model or production workload. The durable delta is an evaluation contract—framework identity, docs, generator, validation, task runner and outcome must all be versioned—not a product ranking. 在本次复核中，`PLATFORM-EVALUATION-SYSTEM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — We implement this in \textbf{ADK Arena}, a fully automated pipeline with per-framework Docker isolation, a three-level validation pipeline, and benchmark adapters for SWE-bench, $τ^2$-bench, Terminal-Bench, and MCP-Atlas Model: Disclosed — Execution uses GPT-5.4 Nano via the token proxy. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05548v1 exact heading "2 Methodology: LLM-as-a-Developer" and "3 ADK Arena"`；Evaluation: `arXiv:2606.05548v1 §4 Evaluation; §4.1 Experimental Setup`；Limitations: `arXiv:2606.05548v1 §2.3 Assumptions and Scope; §5.6 Limitations`；Artifact: `https://github.com/jintao-h/ADK-Arena — repository disclosed; event-time commit not pinned`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05548:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.05548v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05548:end -->
<!-- review:SF-2026-ARXIV-2606-05548:end -->

<!-- review:SF-2026-ARXIV-2606-05551:start -->
### 2606.05551 — Conformal Risk-Averse Decision Making with Action Conditional Guarantee

**问题、旧方案与约束变化。** Action-conditional rather than marginal conformal coverage changes the safety guarantee attached to each released decision and therefore the evaluation/release contract. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-EVALUATION-SYSTEM`。

**机制、实现与 ownership。** The paper derives prediction sets and risk-averse policies whose guarantee is conditioned on the action selected, then supplies a finite-sample pinball-loss calibration algorithm and proofs. Two tabular decision workloads show that the action-conditional procedure improves the corresponding conditional metric over marginal conformal baselines. What is proved depends on the stated exchangeability/calibration setting, finite action space and defined loss; it is not a causal intervention guarantee, a distribution-shift guarantee, or permission for the learned policy to bypass an external safety authority. Computation and sample demand increase as action conditioning fragments calibration support, so marginal methods remain reasonable where only population-level coverage is required. 在本次复核中，`PLATFORM-EVALUATION-SYSTEM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Experiments on two real-world datasets confirm that our approach significantly improves action-conditional performance over conformal baselines. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05551v1 Methodology: exact heading "5.2 Recommender Systems"`；Evaluation: `arXiv:2606.05551v1 Experiments: exact heading "5 Numerical Experiments"`；Limitations: `arXiv:2606.05551v1 Scope and Limitations — exact heading or bounded scope route "6 Conclusion and Discussion"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/Telvc/AC-RAC`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05551:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.05551v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05551:end -->
<!-- review:SF-2026-ARXIV-2606-05551:end -->

<!-- review:SF-2026-ARXIV-2606-05558:start -->
### 2606.05558 — Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents

**问题、旧方案与约束变化。** Off-policy Agent evaluation from logged trajectories introduces an explicit surrogate-environment boundary and policy-conditioned transition contract instead of requiring live execution. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-EVALUATION-SYSTEM`。

**机制、实现与 ownership。** ADWM factors a policy-guided trajectory distribution into action-conditioned one-step transitions and alternates an evaluation LLM with latent diffusion denoising. Four agent benchmarks span dense, shaped, continuous and sparse reward; evaluation policies differ from behavior policies, and ranking correlation plus component ablations test the world-model estimator. The manuscript itself notes ground-truth episode uncertainty and an embedding adapter tied to the evaluation model family. Logged-support gaps, model error and rollout compounding remain; the result cannot replace live evaluation or certify causal environment response. 在本次复核中，`PLATFORM-EVALUATION-SYSTEM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Empirically, ADWM achieves accurate value estimates and evaluation reliability across diverse multi-turn agent tasks, demonstrating its promise as a practical framework for offline LLM agent evaluation. Model: Disclosed — Behavior π b \pi_{b} Evaluation π e \pi_{e} Reward HotpotQA ( Yang et al., 2018 ) ReAct-HotpotQA-SFT ReAct-HotpotQA {DPO, PRM} ( Xiong et al., 2025 ) dense F1 ScienceWorld ( Wang et al., 2022 ) sw-llama-sft sw-llama-eto  Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05558v1 Methodology: exact heading "H.3 ψ \psi -adapter loss design"`；Evaluation: `arXiv:2606.05558v1 Experiments: exact heading "Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents"`；Limitations: `arXiv:2606.05558v1 Scope and Limitations — exact heading or bounded scope route "Appendix A Limitations"`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05558:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05558v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05558:end -->
<!-- review:SF-2026-ARXIV-2606-05558:end -->

<!-- review:SF-2026-ARXIV-2606-05559:start -->
### 2606.05559 — CLaaS: Continual learning as a service for sample efficient online learning

**问题、旧方案与约束变化。** CLaaS assigns rollout storage, replay, asynchronous parameter updates and serving-time model refresh to a deployment service, changing state and control ownership. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-PLATFORM`。

**机制、实现与 ownership。** CLaaS wraps collection, replay, asynchronous parameter updates and checkpoint exposure behind a chat-compatible service. The experiment uses 100 adversarial instruction-hierarchy scenarios split into five non-stationary stages; an adaptive attacker changes as the defender learns, and the paper compares forward/backward transfer across update methods. This demonstrates a prototype adaptation loop, not production safety under broad workloads or model families. Asynchrony makes policy version, sample provenance, reward/verifier drift and rollback first-class states; a one-line client integration does not remove those obligations. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Ideally, adaptation can be performed from accumulated agent experiences and retain prior capabilities while transferring to future tasks. Model: Disclosed — Our infrastructure uses Qwen3-8B ( Yang et al., 2025 ) with 2xH100 Nvidia GPUs, one for asynchronous training and one for inference. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05559v1 Methodology: exact heading "3 Method"`；Evaluation: `arXiv:2606.05559v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05559v1 Scope and Limitations — exact heading or bounded scope route "5 Discussion"`；Artifact: `Artifact URL disclosed in exact-v1: https://arxiv.org/abs/2404.11018`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05559:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05559v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05559:end -->
<!-- review:SF-2026-ARXIV-2606-05559:end -->

<!-- review:SF-2026-ARXIV-2606-05568:start -->
### 2606.05568 — ColBERTSaR: Sparsified ColBERT Index via Product Quantization

**问题、旧方案与约束变化。** Turning ColBERT token storage into a quantized inverted index changes persistent index layout, gather/decompression work and MaxSim data flow, not only retrieval accuracy. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-RAG`。

**机制、实现与 ownership。** ColBERTSaR interprets product-quantized document-token representations as learned sparse terms and retains MaxSim as the scoring distinction. Cross-language retrieval experiments report competitive effectiveness and index sizes roughly 53–77% of a one-bit PLAID index, with a larger gap on technical terminology. This is a proof-of-concept index representation result: it does not disclose production query latency, update cost, cache behavior, end-to-end RAG quality or generalize beyond the tested multilingual collections. 在本次复核中，`AGENT-RAG` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — As baselines, we compare with BM25 (machine-translated documents, i.e., DT, on NeuCLIRBench and NeuCLIRTech provided by the benchmark to perform lexical matching on English tokens) as the lexical sparse retrieval alterna Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Disclosed — We use eight NVIDIA V100 GPUs and a learning rate of 10 − 4 10^{-4} with a per-device batch size of 2048 vectors for 100k training steps using fp16. 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05568v1 Methodology: exact heading "§3 Method / System Design"`；Evaluation: `arXiv:2606.05568v1 Experiments: exact heading "3. Experiments"`；Limitations: `arXiv:2606.05568v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/hltcoe/ColBERTSaR`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05568:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05568v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05568:end -->
<!-- review:SF-2026-ARXIV-2606-05568:end -->

<!-- review:SF-2026-ARXIV-2606-05597:start -->
### 2606.05597 — AsyncWebRL: Efficient Asynchronous Reinforcement Learning for Multi-Step Visual Web Agents

**问题、旧方案与约束变化。** Overlapping rollout, update and policy refresh with an everlasting rollout pool changes distributed RL execution and freshness ownership; the trajectory normalizer finding also changes token-budget accounting. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `TRAIN-DISTRIBUTED-TRAINING`。

**机制、实现与 ownership。** AsyncWebRL overlaps rollout, update and policy refresh with an everlasting pool, moves screenshots behind lightweight references, and corrects mixed policy versions during training. It also replaces a per-trajectory `1/|τ|` normalizer whose interaction with longer failed trajectories weakened negative token gradients. The authors report 2.4–2.9× pipeline speedup and shorter trajectories under their web-agent/browser/GPU configuration, but hardware, concurrency, precision and service SLO are not fully disclosed for general comparison. Staleness, shared-store pressure and trajectory weighting are new failure modes; synchronous training remains simpler where rollout cost is small. 在本次复核中，`TRAIN-DISTRIBUTED-TRAINING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — We picked WebGym because it is the largest open multi-step visual web-agent training environment to date: roughly 290k training tasks across 128k real-world websites in three difficulty levels (Easy, Medium, Hard), evalu Model: Disclosed — Rewards are binary, produced by WebGym’s GPT-4o rubric evaluator. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05597v1 Methodology: exact heading "3.1 System"`；Evaluation: `arXiv:2606.05597v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05597v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05597:start -->
**Claim boundary。** Fresh Score V2 = `2/3/2=7`；review route = `deep`；primary evidence = `arXiv:2606.05597v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05597:end -->
<!-- review:SF-2026-ARXIV-2606-05597:end -->

<!-- review:SF-2026-ARXIV-2606-05606:start -->
### 2606.05606 — Cross-Epoch Adaptive Rollout Optimization for RL Post-Training

**问题、旧方案与约束变化。** A posterior over prompt success and a global cross-epoch budget make rollout allocation durable training-resource state rather than a fixed per-prompt hyperparameter. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `TRAIN-GRPO`。

**机制、实现与 ownership。** The proposed controller allocates a fixed global rollout budget across epochs using observed difficulty/learning signals rather than fixing equal samples per epoch; the manuscript supplies a guarantee under its assumptions and numerical comparisons plus ablations. The result supports closed-loop budget allocation, not arbitrary reduction of on-policy coverage: stale difficulty estimates can starve rare modes, so minimum coverage and audit receipts remain necessary. 在本次复核中，`TRAIN-GRPO` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Under fixed prompt utilities, we prove an $O(\sqrt{K})$ regret bound against the offline allocation benchmark. Model: Disclosed — We evaluate their performance on four open-weight language models: DeepSeek-R1-Distill-Qwen-1.5B ( Guo et al. Hardware: Disclosed — We use H800 GPUs for all runs: the 1.5B and 4B models are trained on 4 4 GPUs, while the 7B model is trained on 8 8 GPUs. 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05606v1 Methodology: exact heading "3 Informativeness and Utility Function Design"`；Evaluation: `arXiv:2606.05606v1 Experiments: exact heading "5 Numerical Experiments"`；Limitations: `arXiv:2606.05606v1 Scope and Limitations — exact heading or bounded scope route "Limitations."`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05606:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05606v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05606:end -->
<!-- review:SF-2026-ARXIV-2606-05606:end -->

<!-- review:SF-2026-ARXIV-2606-05610:start -->
### 2606.05610 — Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training

**问题、旧方案与约束变化。** Checkpoint-equivalent compute and proxy-derived learning-rate/batch laws change continued-pretraining resource planning and stability judgment rather than reporting one optimum. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `TRAIN-PRETRAINING`。

**机制、实现与 ownership。** The study fits predictive relationships for optimal learning rate and batch size as model/data scale changes in continued pretraining, validates them across held-out configurations and includes ablations. The equations are empirical workload models, not universal laws: corpus shift, optimizer, initialization, token budget and loss surface define the fitted regime. The durable delta is to treat CPT hyperparameters as jointly scaled and revalidated rather than copied from pretraining. 在本次复核中，`TRAIN-PRETRAINING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — To discover these laws, we utilize small-scale proxy models ( N ∈ { 100 ​ M , 500 ​ M } N\in\{100\text{M},500\text{M}\} ) trained on the target CPT dataset. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05610v1 Methodology: exact heading "2 Method"`；Evaluation: `arXiv:2606.05610v1 Experiments: exact heading "3 Experiments"`；Limitations: `arXiv:2606.05610v1 Scope and Limitations — exact heading or bounded scope route "Limitations"`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05610:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.05610v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05610:end -->
<!-- review:SF-2026-ARXIV-2606-05610:end -->

<!-- review:SF-2026-ARXIV-2606-05646:start -->
### 2606.05646 — Enhancing Software Engineering Through Closed-Loop Memory Optimization

**问题、旧方案与约束变化。** Validated downstream impact is used both as a task-agnostic memory evaluation contract and as the closed-loop optimization signal across episodes. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** The system observes task outcomes, reflects on reusable experience, updates memory and tests the revised memory over subsequent software tasks. Its multiple evaluation regimes distinguish immediate task gain from adaptive evolution, but memory contamination, benchmark leakage and evaluator-driven self-confirmation remain. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — However, these agents remain fundamentally episodic: they fail to retain, refine, and reuse experiences across tasks, repeatedly reconstructing context from scratch and reproducing similar mistakes. Model: Disclosed — M θ \mathbf{\textit{M}}_{\theta} Accuracy (%) Efficiency (%) LA file ( 𝟏 ) \bm{\textbf{{LA}}_{\textit{file}}^{(1)}} LA func ( 𝟏 ) \bm{\textbf{{LA}}_{\textit{func}}^{(1)}} LA file ( − 𝟏 ) \bm{\textbf{{LA}}_{\textit{file}} Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05646v1 Methodology: exact heading "§3 Method / System Design"`；Evaluation: `arXiv:2606.05646v1 Experiments: exact heading "3.4 Evaluation Regimes for Effective Reflection & Adaptive Evolution"`；Limitations: `arXiv:2606.05646v1 Scope and Limitations — exact heading or bounded scope route "Appendix B Related Work: Extended Discussion"`；Artifact: `Artifact URL disclosed in exact-v1: https://xhguo7.github.io/MemOp/`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05646:start -->
**Claim boundary。** Fresh Score V2 = `1/2/2=5`；review route = `standard`；primary evidence = `arXiv:2606.05646v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05646:end -->
<!-- review:SF-2026-ARXIV-2606-05646:end -->

<!-- review:SF-2026-ARXIV-2606-05662:start -->
### 2606.05662 — QDAG: Declarative Composition of Reusable Analytics Methodologies at LinkedIn

**问题、旧方案与约束变化。** QDAG moves production analytics methodology from drifting imperative glue into typed, composable, demand-driven DAG state deployed across 500 hosts and 100 use cases. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-FOUNDATIONS`。

**机制、实现与 ownership。** QDAG represents production analytics methodology as a declarative DAG with reusable nodes, demand-driven memoized evaluation and incremental recomputation. LinkedIn cases show how definition, execution and cached result identities can be separated, but they do not prove portability or performance outside the disclosed stack. 在本次复核中，`PLATFORM-FOUNDATIONS` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Not Disclosed — exact-v1 does not identify workload/evaluation slice Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05662v1 Methodology: exact heading "QDAG: Declarative Composition of Reusable Analytics Methodologies at LinkedIn"`；Evaluation: `arXiv:2606.05662v1 Experiments: exact heading "VI-A Demand-driven, memoized evaluation"`；Limitations: `arXiv:2606.05662v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Artifact URL disclosed in exact-v1: https://bazel.build/`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05662:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；primary evidence = `arXiv:2606.05662v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05662:end -->
<!-- review:SF-2026-ARXIV-2606-05662:end -->

<!-- review:SF-2026-ARXIV-2606-05679:start -->
### 2606.05679 — Data Flow Control: Data Safety Policies for AI Agents

**问题、旧方案与约束变化。** Optimizer-invariant tuple-level provenance predicates move Agent data-release safety from prompts into the DBMS, giving the data plane enforcement ownership. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-SECURITY`。

**机制、实现与 ownership。** The paper separates a data-use/release policy from SQL or tool-call correctness and compares logical provenance with physical enforcement paths. This makes combination, derivation and disclosure effects explicit at action time; the prototype assumes trusted mediation and cannot undo disclosure after data leave the boundary. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — §5 evaluates TPC-H across scaling, five DBMS engines, policy/source/self-join sweeps, plus an application workload Model: Not Disclosed — not applicable to this DBMS policy-enforcement workload; no learned model is evaluated Hardware: Disclosed — §5.1 uses an 8-core Apple M3 with 16GB RAM for DuckDB/Umbra/PostgreSQL/DataFusion and AWS RDS with 4 vCPUs/16GB RAM for SQL Server 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05679v1 Methodology: exact section route "§3 Data Flow Control Policies; §4 Policy Enforcement"`；Evaluation: `arXiv:2606.05679v1 Experiments: exact section route "§5 Evaluation; §5.1 Setup"`；Limitations: `arXiv:2606.05679v1 Scope and Limitations: exact bounded route "§1 stated monotonic SQL-92 scope; §2.2.3 Beyond Positive Relational Queries; §4.3/§4.5 enforcement limits"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/dataflowcontrol/data-flow-control`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05679:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.05679v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05679:end -->
<!-- review:SF-2026-ARXIV-2606-05679:end -->

<!-- review:SF-2026-ARXIV-2606-05688:start -->
### 2606.05688 — Value-and-Structure Alignment for Routing-Consistent Quantization of Mixture-of-Experts Models

**问题、旧方案与约束变化。** Quantization can change top-k expert identity; preserving router value and ordering therefore becomes part of MoE quantization correctness, not an optional quality metric. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `MODEL-MOE`。

**机制、实现与 ownership。** The method aligns both expert values and router structure during quantization, recognizing that small routing changes alter which parameters execute. Model/task experiments support lower routing divergence alongside quality retention, but kernel cost and expert-placement communication are not established. 在本次复核中，`MODEL-MOE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — AutoRound optimizes quantization parameters by minimizing a block-wise reconstruction loss on a small calibration dataset. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05688v1 Methodology: exact heading "§3 Method / System Design"`；Evaluation: `arXiv:2606.05688v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05688v1 Scope and Limitations — exact heading or bounded scope route "5 Discussion"`；Artifact: `Artifact URL disclosed in exact-v1: https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05688:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05688v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05688:end -->
<!-- review:SF-2026-ARXIV-2606-05688:end -->

<!-- review:SF-2026-ARXIV-2606-05711:start -->
### 2606.05711 — Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems

**问题、旧方案与约束变化。** The text-versus-latent communication framework exposes what state crosses Agent boundaries, how sender/receiver spaces align and how the receiver fuses it; this corrects the durable protocol model even though the paper is a synthesis. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MULTI-AGENT`。

**机制、实现与 ownership。** The paper unifies embedding-, hidden-state-, KV- and hybrid communication paths and demonstrates a training-free implementation branch. Latent channels can reduce tokens and preserve richer state, but weaken portability, interoperability, observability and policy enforcement; surveyed benchmark results are not one controlled comparison. 在本次复核中，`AGENT-MULTI-AGENT` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05711v1 Methodology: exact heading "Beyond Tokens: A Unified Framework for Latent Communication in LLM-based Multi-Agent Systems"`；Evaluation: `arXiv:2606.05711v1 Experiments: exact heading "7. Benchmark Analysis and Empirical Insights"`；Limitations: `arXiv:2606.05711v1 Scope and Limitations — exact heading or bounded scope route "3.1 Limitations of Natural Language Communication"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/enochliu98/Awesome-Latent-Communication`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05711:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05711v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05711:end -->
<!-- review:SF-2026-ARXIV-2606-05711:end -->

<!-- review:SF-2026-ARXIV-2606-05725:start -->
### 2606.05725 — An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic

**问题、旧方案与约束变化。** Model-extraction detection is defined over benign-calibrated traffic windows, making cross-request distribution state and service-level thresholds explicit security state. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-SECURITY`。

**机制、实现与 ownership。** The detector aggregates statistical discrepancy over sequences of API queries instead of judging each request in isolation, with per-dataset results and implementation details. Detection depends on window, benign traffic, attacker adaptation and model endpoint; it does not prove attribution or justify automatic punishment without policy review. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Dataset family Attacker query source Normal query source Query-Efficient-Med Self-generated medical domain stealing queries Medicine-related WildChat queries Model-Leeching Template-wrapped SQuAD extraction prompts Origi Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05725v1 Methodology: exact heading "3 Methodology"`；Evaluation: `arXiv:2606.05725v1 Experiments: exact heading "4 Experimental Evaluations"`；Limitations: `arXiv:2606.05725v1 Scope and Limitations — exact heading or bounded scope route "Appendix B Limitations"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/LabRAI/mmd-llm-mea-detection`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05725:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05725v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05725:end -->
<!-- review:SF-2026-ARXIV-2606-05725:end -->

<!-- review:SF-2026-ARXIV-2606-05742:start -->
### 2606.05742 — AdaPLD: Adaptive Retrieval and Reuse for Efficient Model-Free Speculative Decoding

**问题、旧方案与约束变化。** Adaptive retrieval and reuse of prior draft candidates changes model-free speculative proposal state and the acceptance/control loop. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-SPECULATIVE-DECODING`。

**机制、实现与 ownership。** AdaPLD retrieves and reuses prior continuation patterns without a trained draft model and adapts proposal length/ reuse based on acceptance. Main, component and stochastic-decoding tests support the selected LMs/benchmarks; cache lookup overhead, stale patterns and target verification remain. 在本次复核中，`INFER-SPECULATIVE-DECODING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Across diverse benchmarks, AdaPLD reduces target-model forward passes and achieves up to $3.10\times$ decoding speedup. Model: Disclosed — Model Layer Vicuna-7B 9 Vicuna-13B 13 Vicuna-33B 11 Qwen3-8B 29 Table 6: Transformer layer indices used for hidden-state reranking in each model. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05742v1 Methodology: exact heading "3 Method"`；Evaluation: `arXiv:2606.05742v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05742v1 Scope and Limitations — exact heading or bounded scope route "Limitations"`；Artifact: `Artifact URL disclosed in exact-v1: https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl_a_00276/1923288/tacl_a_00276.pdf`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05742:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05742v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05742:end -->
<!-- review:SF-2026-ARXIV-2606-05742:end -->

<!-- review:SF-2026-ARXIV-2606-05743:start -->
### 2606.05743 — Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense

**问题、旧方案与约束变化。** Contrastive safety-memory cells jointly store block and permit conditions and evolve without retraining, changing guardrail state, poisoning risk and cross-attack reuse. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-SECURITY`。

**机制、实现与 ownership。** Membrane stores contrastive attack/benign experience and updates retrieval/decision state as new attacks arrive, measuring both jailbreak blocking and over-refusal. Online safety memory can adapt faster than weights but can also be poisoned or authorize false positives; the retrieved signal must not own the final action. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — On AgentHarm we keep the same refusal-based definitions, with ASR the fraction of harmful tasks not refused and FRR the refusal rate on benign tasks. Model: Disclosed — In the main experiments, the target model and all LLM-based components of Membrane are instantiated with Qwen3-8B, served through a self-hosted vLLM endpoint. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05743v1 Methodology: exact heading "B.1 Design Principles"`；Evaluation: `arXiv:2606.05743v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05743v1 Scope and Limitations — exact heading or bounded scope route "Limitations"`；Artifact: `Artifact URL disclosed in exact-v1: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Flash-Model-Card.pdf`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05743:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05743v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05743:end -->
<!-- review:SF-2026-ARXIV-2606-05743:end -->

<!-- review:SF-2026-ARXIV-2606-05787:start -->
### 2606.05787 — SentinelRAG: Synthetic Sentinel Knowledge for RAG Database Copyright Protection

**问题、旧方案与约束变化。** Owner-only sentinel probes and synthetic database entries introduce a provenance/detection contract for unauthorized RAG datastore redistribution. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-SECURITY`。

**机制、实现与 ownership。** SentinelRAG injects synthetic, detectable knowledge into a retrieval database so suspicious reproduction can provide a provenance signal while ordinary query utility is monitored. The attack/utility experiments support the chosen retrievers and sentinel construction, but adaptive attackers, false positives and database transformation define the boundary; the watermark is evidence, not automatic enforcement authority. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Experiments on four datasets ranging from 2.9k to 8.8M documents demonstrate that SentinelRAG achieves statistically significant detection $p < 10^{-5}$ across all tested configurations at only a 0.1% injection rate. Model: Disclosed — Dataset GPT-5-mini Qwen-3-8B Gemini-3-Flash GPT-OSS-20B SentinelRAG (Ours) NFCorpus 1.0% 1.0% 0.5% 1.0% FiQA 0.0% 0.0% 0.0% 0.0% MS-MARCO 1.0% 1.0% 1.0% 1.0% HotpotQA 0.0% 0.0% 0.0% 0.0% RAG-WM (Baseline) NFCorpus 7.0% 1 Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05787v1 Methodology: exact heading "B.5 System-Prompt Defense"`；Evaluation: `arXiv:2606.05787v1 Experiments: exact heading "5 Experimental Setup"`；Limitations: `arXiv:2606.05787v1 Scope and Limitations — exact heading or bounded scope route "3.1 Threat Model"`；Artifact: `Artifact URL disclosed in exact-v1: https://platform.openai.com/docs/guides/embeddings`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05787:start -->
**Claim boundary。** Fresh Score V2 = `1/2/2=5`；review route = `standard`；primary evidence = `arXiv:2606.05787v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05787:end -->
<!-- review:SF-2026-ARXIV-2606-05787:end -->

<!-- review:SF-2026-ARXIV-2606-05800:start -->
### 2606.05800 — SALT: When More Rollouts Don't Help in Group-Based Policy Optimization and How to Make Them Matter

**问题、旧方案与约束变化。** The feature-concentration diagnosis shows why more group rollouts can stop adding training signal and changes the design judgment for allocating rollout compute. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `TRAIN-GRPO`。

**机制、实现与 ownership。** SALT attributes the weak return from additional group rollouts to feature concentration: nominally more samples may fail to add distinct learning signal. Its mechanism changes selection/weighting so added sampling creates useful variation, with experiments and ablations supporting the selected models, rewards and tasks. Extra rollout compute, reward bias and distributed synchronization remain costs; more samples are not intrinsically better. 在本次复核中，`TRAIN-GRPO` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Across diverse reasoning-oriented RLVR benchmarks and model scales, SALT improves effective update geometry and performance without modifying the reward model or the rollout sampling procedure Signed low-rank gradient re Model: Disclosed — Dataset Method AIME24 AIME25 GSM8K MATH-500 GPQA ACC Pass@8 ACC Pass@8 ACC Pass@8 ACC Pass@8 ACC Pass@8 Deepseek-Distill-Qwen-1.5B ∼ \sim Vanilla 29.1 59.3 22.0 42.6 80.3 95.0 85.5 96.4 34.5 82.4 MATH-TRAIN GRPO 29.3 59. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05800v1 Methodology: exact heading "3 Methodology"`；Evaluation: `arXiv:2606.05800v1 Experiments: exact heading "4 Experiment"`；Limitations: `arXiv:2606.05800v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Artifact URL disclosed in exact-v1: https://huggingface.co/datasets/HuggingFaceH4/aime_2024`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05800:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05800v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05800:end -->
<!-- review:SF-2026-ARXIV-2606-05800:end -->

<!-- review:SF-2026-ARXIV-2606-05805:start -->
### 2606.05805 — From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents

**问题、旧方案与约束变化。** Returning a constrained remediation plan rather than only allow/deny changes the guardrail-to-agent action interface and the authority boundary for recovery. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-SECURITY`。

**机制、实现与 ownership。** The framework turns a risk classification into a structured remediation plan for an agent workflow. This can make a guardrail response more actionable than allow/deny alone, but a generated plan is a proposal: policy, authorization, human escalation and post-action verification must remain external owners. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — However, agent risks often arise when otherwise benign tasks are contaminated by untrusted external content, unsafe instructions, or risky tool use. Model: Disclosed — Method ASB-DPI ASB-IPI AgentHarm ASR ( ↓ \downarrow ) TSR ( ↑ \uparrow ) RR ASR ( ↓ \downarrow ) TSR ( ↑ \uparrow ) RR HS ( ↑ \uparrow ) Harm ( ↓ \downarrow ) No defense ReAct 86.96 0.00 7.35 99.49 1.57 0.34 36.28 77.04  Hardware: Disclosed — In our implementation, Tri-Guard is served with vLLM on a single NVIDIA A100 80GB GPU. 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05805v1 Methodology: exact heading "From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents"`；Evaluation: `arXiv:2606.05805v1 Experiments: exact heading "5 Experiments"`；Limitations: `arXiv:2606.05805v1 Scope and Limitations — exact heading or bounded scope route "Limitations"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/YUHAOSUNABC/TRIAD`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05805:start -->
**Claim boundary。** Fresh Score V2 = `1/2/2=5`；review route = `standard`；primary evidence = `arXiv:2606.05805v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05805:end -->
<!-- review:SF-2026-ARXIV-2606-05805:end -->

<!-- review:SF-2026-ARXIV-2606-05828:start -->
### 2606.05828 — Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents

**问题、旧方案与约束变化。** Strictly separating local statistical preference state from remote semantic intent parsing changes selection authority and privacy/cost ownership in personal Agent harnesses. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-PLATFORM`。

**机制、实现与 ownership。** The proposed personal-agent harness keeps a local statistical prior over user skill preferences and separates skill selection from remote language interpretation. This improves privacy and latency boundaries when preferences are stable, while sparse observations, drift and incorrect local priors can route the wrong action. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — These empirical results reinforce the core conclusion: delegating probabilistic credit assignment to a local statistical prior while reserving the remote LLM strictly for complex intent parsing avoids the systemic failur Model: Disclosed — To ensure architectural robustness across varying model capabilities, we evaluate all agents using 3 diverse LLM backbones: GPT-5.2 ( OpenAI, 2025b ) , DeepSeek-V4-Flash ( DeepSeek-AI, 2026 ) , and Qwen3-30B-Instruct ( Y Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05828v1 Methodology: exact heading "3 Method"`；Evaluation: `arXiv:2606.05828v1 Experiments: exact heading "5 Experiment"`；Limitations: `arXiv:2606.05828v1 Scope and Limitations — exact heading or bounded scope route "Limitations"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/ZyGan1999/Personalized-Skill-Selection`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05828:start -->
**Claim boundary。** Fresh Score V2 = `1/2/2=5`；review route = `standard`；primary evidence = `arXiv:2606.05828v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05828:end -->
<!-- review:SF-2026-ARXIV-2606-05828:end -->

<!-- review:SF-2026-ARXIV-2606-05868:start -->
### 2606.05868 — YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition

**问题、旧方案与约束变化。** Adaptive GQA-to-MLA transition changes KV representation and concurrency memory layout; the financial workload is evidence, not the owner of the mechanism. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-KV-CACHE`。

**机制、实现与 ownership。** YouZhi measures layer-specific degradation while converting GQA layers to MLA, applies a staged recovery pipeline and evaluates language, financial-task and high-concurrency behavior on Ascend A3 with vLLM-Ascend. The result supports this converted-model/hardware stack; reported concurrency cannot be transferred to other models, precisions, lengths, batches or SLOs without the same contract. 在本次复核中，`INFER-KV-CACHE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Compared to their respective base models, YouZhi-7B yields a 12.3% improvement in average financial benchmark score alongside a 2.69$\times$ increase in maximum concurrency; similarly, YouZhi-14B achieves a 7.0% accuracy Model: Disclosed — Specifically, our resulting models, YouZhi-7B and YouZhi-14B, are converted from the GQA models OpenPangu-7B and Qwen2.5-14B-Instruct, respectively. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05868v1 Methodology: exact heading "3 Method"`；Evaluation: `arXiv:2606.05868v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05868v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/open-compass/OpenFinData`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05868:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05868v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05868:end -->
<!-- review:SF-2026-ARXIV-2606-05868:end -->

<!-- review:SF-2026-ARXIV-2606-05872:start -->
### 2606.05872 — Entropy-Based Observability for AI Agent Behavior

**问题、旧方案与约束变化。** Deriving exploration, rigidity, tool concentration and uncertainty-reduction telemetry from traces adds an Agent-behavior observability plane beyond outcome metrics. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-MONITORING`。

**机制、实现与 ownership。** The framework defines action, trajectory and tool entropy, information gain, exploration efficiency and robustness entropy, then demonstrates them on controlled and learning-roadmap agents. These lightweight signals can reveal behavioral collapse or churn but are descriptive proxies: high entropy is not quality and low entropy is not failure. 在本次复核中，`PLATFORM-MONITORING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — AI agents are typically instrumented through outcome-oriented indicators such as task success, reward, latency, and cost.Although these indicators are operationally important, they provide limited visibility into the int Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05872v1 Methodology: exact heading "Entropy-Based Evaluation of AI Agents: A Lightweight Framework for Measuring Behavioral Patterns"`；Evaluation: `arXiv:2606.05872v1 Experiments: exact heading "Entropy-Based Evaluation of AI Agents: A Lightweight Framework for Measuring Behavioral Patterns"`；Limitations: `arXiv:2606.05872v1 Scope and Limitations — exact heading or bounded scope route "5.4 Limitations"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/olahsymbo/agent-eval`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05872:start -->
**Claim boundary。** Fresh Score V2 = `1/2/2=5`；review route = `standard`；primary evidence = `arXiv:2606.05872v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05872:end -->
<!-- review:SF-2026-ARXIV-2606-05872:end -->

<!-- review:SF-2026-ARXIV-2606-05875:start -->
### 2606.05875 — QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving

**问题、旧方案与约束变化。** Query-aware compressed cache fusion changes the identity, granularity and quality boundary of reusable RAG prefill state. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-KV-CACHE`。

**机制、实现与 ownership。** QCFuse uses chunk-anchor probing and critical-layer localization to select which cached tokens need recomputation, avoiding a full-context/all-layer selection pass that would stall pipelined cache fusion. SGLang experiments cover TTFT, context scaling, bandwidth, request load, quality and ablations, but results remain model, dataset, cache-link, recompute-budget and SLO specific. 在本次复核中，`INFER-KV-CACHE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — We implement QCFuse in SGLang and evaluate it on four open-weight LLMs across six datasets. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05875v1 Methodology: exact heading "3. QCFuse System Design"`；Evaluation: `arXiv:2606.05875v1 Experiments: exact heading "4. Experiments"`；Limitations: `arXiv:2606.05875v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/uYanJX/QCFuse`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05875:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05875v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05875:end -->
<!-- review:SF-2026-ARXIV-2606-05875:end -->

<!-- review:SF-2026-ARXIV-2606-05894:start -->
### 2606.05894 — EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents

**问题、旧方案与约束变化。** Budgeted evidence retention makes provenance, eviction and future retrieval cost explicit long-horizon memory state rather than flat context trimming. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** EMBER turns streaming episodes into source-backed evidence capsules, retains a budgeted cover before the future query is known and selects a chain at read time. Experiments test retention and answerability, but probe errors can discard future-critical evidence and generated capsules remain derived state that must preserve source identity and rebuild. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — • LongMemEval-RR is our LongMemEval-derived Budgeted Pre-Query Retention protocol ( Wu et al., 2025 ) , not an official LongMemEval benchmark name. Model: Disclosed — We fine-tune Qwen2.5-7B and Qwen2.5-14B ( Yang and others, 2024 ) memory-policy backbones on external pre-query episodes, keeping the retriever fixed during rollouts. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05894v1 Methodology: exact heading "3 Method"`；Evaluation: `arXiv:2606.05894v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05894v1 Scope and Limitations — exact heading or bounded scope route "7 Limitations and Broader Impact"`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05894:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05894v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05894:end -->
<!-- review:SF-2026-ARXIV-2606-05894:end -->

<!-- review:SF-2026-ARXIV-2606-05933:start -->
### 2606.05933 — Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference

**问题、旧方案与约束变化。** SLO-aware sliding-window chunking changes batch construction, latency prediction and fairness state under shared inference contention. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-SCHEDULING`。

**机制、实现与 ownership。** SlidingServe predicts batch latency, assigns multi-level priority and constructs chunks over a scheduling window rather than greedily optimizing one iteration. Goodput, overload, transient-load, ablation and predictor-fidelity experiments support the tested serving stack; prediction error, workload drift and starvation remain failure modes, and results are bound to the reported model/hardware/load/SLO contract. 在本次复核中，`INFER-SCHEDULING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — §5 evaluates ShareGPT and arXiv-summarization traces under maximum-goodput, overload, transient-load, ablation, and predictor-fidelity slices Model: Disclosed — §5 uses Llama3-8B and Qwen2.5-7B Hardware: Disclosed — §5 deploys both evaluated models on RTX 3090 GPUs with tensor parallelism TP=2 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05933v1 Methodology: exact heading "3. SlidingServe: Design and Implementation"`；Evaluation: `arXiv:2606.05933v1 Experiments: exact heading "5. Evaluation"`；Limitations: `arXiv:2606.05933v1 Scope and Limitations — exact heading or bounded scope route "2.2. Limitations of Single-step Scheduling"`；Artifact: `Artifact URL disclosed in exact-v1: https://huggingface.co/datasets/whu9/arxiv_summarization_postprocess`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05933:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.05933v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05933:end -->
<!-- review:SF-2026-ARXIV-2606-05933:end -->

<!-- review:SF-2026-ARXIV-2606-05946:start -->
### 2606.05946 — Short paper: Models in the dark -- Rectification and erasure under GDPR in ML supply chains

**问题、旧方案与约束变化。** The models-in-the-dark finding shows rectification/erasure cannot be enforced without lineage across derived models and supply-chain actors, correcting model-registry lifecycle ownership. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-MODEL-REGISTRY`。

**机制、实现与 ownership。** The paper argues that data-subject rights cannot be implemented solely by editing an upstream dataset: organizations must locate model/controller copies, assess model-level effects and propagate rectification or erasure across opaque supply chains and continually learned descendants. It is a legal/technical scope analysis, not proof that current unlearning methods satisfy GDPR. 在本次复核中，`PLATFORM-MODEL-REGISTRY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: No empirical benchmark is claimed Model: No empirical model slice is claimed Hardware: No empirical hardware slice is claimed 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05946v1 Methodology: exact heading "§3 Method / System Design"`；Evaluation: `Not Disclosed — exact-v1 contains no empirical evaluation section; conceptual or method claim only`；Limitations: `arXiv:2606.05946v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Artifact URL disclosed in exact-v1: https://creativecommons.org/licenses/by-nc-nd/4.0`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05946:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；primary evidence = `arXiv:2606.05946v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05946:end -->
<!-- review:SF-2026-ARXIV-2606-05946:end -->

<!-- review:SF-2026-ARXIV-2606-05951:start -->
### 2606.05951 — Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication

**问题、旧方案与约束变化。** Symmetric memory and device-initiated one-sided communication change ownership and initiation of sparse AI communication, a runtime mechanism rather than an application benchmark. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `TRAIN-DISTRIBUTED-TRAINING`。

**机制、实现与 ownership。** The source traces symmetric-memory allocation/registration, remote address computation, device-initiated RMA, proxy or IBGDA paths, ordering, collectives and protocol selection. System experiments can explain when device-side one-sided communication avoids host orchestration, but conclusions are version/topology/interconnect specific and must not be turned into generic bandwidth claims. 在本次复核中，`TRAIN-DISTRIBUTED-TRAINING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — We also examine DeepEP as a case study of NVSHMEM in performance-critical sparse deep learning workloads. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Disclosed — All measurements in this section were collected on a CoreWeave H200 cluster. 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05951v1 Methodology: exact section route "§III NVSHMEM Overview; §§IV–VI memory, one-sided communication, and collectives"`；Evaluation: `arXiv:2606.05951v1 Experiments: exact section route "§VII Microbenchmarking; §VII-A Experimental Setup; §VIII DeepEP case study"`；Limitations: `arXiv:2606.05951v1 Scope and Limitations: exact bounded route "§IX Related Work & Discussion; §X Conclusion and stated non-comprehensive performance scope"`；Artifact: `Artifact URL disclosed in exact-v1: https://doi.org/10.1145/3581784.3607099`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05951:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.05951v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05951:end -->
<!-- review:SF-2026-ARXIV-2606-05951:end -->

<!-- review:SF-2026-ARXIV-2606-05958:start -->
### 2606.05958 — Steering Vectors are an Adversarial Attack Surface

**问题、旧方案与约束变化。** Activation-steering artifacts become a model-control supply-chain input that can be poisoned, requiring admission, provenance and mitigation boundaries. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-SECURITY`。

**机制、实现与 ownership。** The attack optimizes benign-looking contrast pairs so their derived steering vector preserves a named attribute on benign prompts while increasing jailbreak behavior. Threat-model, multi-model and internal-analysis results support the tested steering pipeline; access assumptions and evaluator coverage bound the claim. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Since the technique is plug-and-play, users share datasets and precomputed vectors to steer model activations. Model: Disclosed — ASR (attack success rate) is the fraction of harmful -prompt responses that a three-judge ensemble ( Claude-Sonnet-4.5 , GPT-4.1 , and Llama-3.3-70B-Instruct , all prompted with the same rubric and instructed to mark loo Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05958v1 Methodology: exact heading "3 Methodology"`；Evaluation: `arXiv:2606.05958v1 Experiments: exact heading "4 Experiments"`；Limitations: `arXiv:2606.05958v1 Scope and Limitations — exact heading or bounded scope route "3.1 Threat Model"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/unitaryai/detoxify.`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05958:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.05958v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05958:end -->
<!-- review:SF-2026-ARXIV-2606-05958:end -->

<!-- review:SF-2026-ARXIV-2606-05976:start -->
### 2606.05976 — The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models

**问题、旧方案与约束变化。** Byte-identical errors become correctable when their chat role changes, correcting the durable belief that self-correction failure is purely a reasoning-capability deficit. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-REFLECTION`。

**机制、实现与 ownership。** The intervention keeps answer bytes fixed but changes whether the chat template labels them as the model's own or another actor's output. Verification and adversarial-mirror experiments support role-conditioned error flagging, showing that failure can be an access/policy gate rather than absent error knowledge. It does not prove faithful internal reasoning or universal correction across templates. 在本次复核中，`AGENT-REFLECTION` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Recent works show that LLM agents struggle to correct errors in their own reasoning traces, despite their ability to correct errors from external sources. Model: Disclosed — The open-weight set is served via Ollama and comprises three 70B-class models, Qwen2.5-72B-Instruct ( Qwen 2025 ) , Llama-3.3-70B-Instruct ( Dubey et al. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.05976v1 Methodology: exact heading "Appendix B Comparison with Published Self-Correction Methods"`；Evaluation: `arXiv:2606.05976v1 Experiments: exact heading "Verifiable reasoning benchmarks and complementary scaffolds."`；Limitations: `arXiv:2606.05976v1 Scope and Limitations — exact heading or bounded scope route "5 Discussion"`；Artifact: `Artifact URL disclosed in exact-v1: https://arxiv.org/abs/2202.03629v7`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-05976:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.05976v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-05976:end -->
<!-- review:SF-2026-ARXIV-2606-05976:end -->

<!-- review:SF-2026-ARXIV-2606-06032:start -->
### 2606.06032 — Catastrophic Forgetting as Accessibility Collapse: A Three-Level Framework for Knowledge Persistence in Continual Learning

**问题、旧方案与约束变化。** Separating storage, representation and accessibility shows behavioral forgetting can coexist with recoverable checkpoint knowledge, changing what forgetting and recovery checks must measure. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `TRAIN-CHECKPOINT`。

**机制、实现与 ownership。** On Split CIFAR-100 with ResNet-18, the final task-0 classifier reaches zero accuracy while frozen-feature probes and a reset linear head recover substantial performance; earlier layers retain more than the final layer/readout. This supports separating storage, representation and access for that controlled setup, not the universal claim that forgetting never destroys representations. Projection recovery also reports a negative result. 在本次复核中，`TRAIN-CHECKPOINT` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — In this work, we investigate an alternative perspective: that forgetting may arise not from complete destruction of task representations but from a loss of accessibility to preserved information. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06032v1 Methodology: exact heading "§3 Method / System Design"`；Evaluation: `arXiv:2606.06032v1 Experiments: exact heading "§4 Experiments / Evaluation"`；Limitations: `arXiv:2606.06032v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06032:start -->
**Claim boundary。** Fresh Score V2 = `3/2/3=8`；review route = `deep`；primary evidence = `arXiv:2606.06032v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06032:end -->
<!-- review:SF-2026-ARXIV-2606-06032:end -->

<!-- review:SF-2026-ARXIV-2606-06036:start -->
### 2606.06036 — Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents

**问题、旧方案与约束变化。** Reconstructing graph memory at query time changes what is authoritative stored state versus derived retrieval state for long-horizon agents. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** MRAgent traverses and reconstructs a graph of memory units across multiple steps, allowing relations absent from any single retrieved item to be assembled into an answer. LongMemEval-style results, cost analysis and ablations support the tested budgets, but graph extraction, judge quality and traversal cost can manufacture or miss relations. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Experiments on the LoCoMo benchmark and LongMemEval benchmark demonstrate significant improvements over strong baselines (up to 23%), while substantially reducing token and runtime cost, highlighting the effectiveness of Model: Disclosed — Following prior work, we report F 1 and LLM-Judge (J) scores using GPT-4o-mini, and additionally report evidence recall (Recall) for analysis. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06036v1 Methodology: exact heading "2.3 Motivation from Cognitive Memory Systems"`；Evaluation: `arXiv:2606.06036v1 Experiments: exact heading "5 Experiments"`；Limitations: `arXiv:2606.06036v1 Scope and Limitations — exact heading or bounded scope route "7 Conclusion and Discussion"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/Ji-shuo/MRAgent`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06036:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06036v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06036:end -->
<!-- review:SF-2026-ARXIV-2606-06036:end -->

<!-- review:SF-2026-ARXIV-2606-06044:start -->
### 2606.06044 — IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval

**问题、旧方案与约束变化。** Interval entities, Allen relations and fuzzy-bound tightening give dynamic knowledge explicit validity semantics rather than treating time as flat metadata. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-RAG`。

**机制、实现与 ownership。** IA-RAG represents events as intervals and applies interval algebra when decomposing and retrieving temporal queries. The evaluation supports the covered temporal query types; extraction mistakes, incomplete event boundaries and the cost of relation expansion remain failure modes. 在本次复核中，`AGENT-RAG` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Experiments on multiple temporal question answering benchmarks, including TimeQA, TempReason, and ComplexTR, demonstrate that IA-RAG achieves strong temporal retrieval and reasoning performance, particularly on complex c Model: Disclosed — We employ Qwen2.5-14B-Instruct Qwen et al. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06044v1 Methodology: exact heading "3 Method"`；Evaluation: `arXiv:2606.06044v1 Experiments: exact heading "4 Experimental Setup"`；Limitations: `arXiv:2606.06044v1 Scope and Limitations — exact heading or bounded scope route "Limitations"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/xiaoAugenstern/LogicalRAG_TemporalQA`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06044:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.06044v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06044:end -->
<!-- review:SF-2026-ARXIV-2606-06044:end -->

<!-- review:SF-2026-ARXIV-2606-06054:start -->
### 2606.06054 — Beyond Similarity: Trustworthy Memory Search for Personal AI Agents

**问题、旧方案与约束变化。** Separating similarity from authority, recency and user control changes the admission and ranking contract for personal memory. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** MemGate evaluates memory records before retrieval/use, treating privacy and harmful personalization as an admission decision rather than a prompt-only instruction. The threat model and experiments support the tested memories and attacks; classifier error, distribution drift and bypass through derived memories remain. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Our results show that long-term memory is not merely a utility layer, but a durable control channel that can reshape how agents interpret tasks and execute actions, leaving them highly susceptible to the aforementioned t Model: Disclosed — The evaluated models include Qwen-3-8B [ 26 ] , Llama-3.3-70B-Instruct [ 27 ] , GPT-4o-mini [ 28 ] , GPT-5.1 [ 29 ] , Gemini-3-Pro [ 30 ] , and Claude-Sonnet-4.6 [ 31 ] . Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06054v1 Methodology: exact heading "IV Defense Methodology: MemGate"`；Evaluation: `arXiv:2606.06054v1 Experiments: exact heading "III-B Experimental Settings"`；Limitations: `arXiv:2606.06054v1 Scope and Limitations — exact heading or bounded scope route "III-A Threat Model"`；Artifact: `Artifact URL disclosed in exact-v1: https://github.com/Kevin-Zh-CS/MemGate`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06054:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.06054v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06054:end -->
<!-- review:SF-2026-ARXIV-2606-06054:end -->

<!-- review:SF-2026-ARXIV-2606-06055:start -->
### 2606.06055 — HUSH-Bench: Measuring Memory-Use Boundaries for Sensitive History in Conversational Agents

**问题、旧方案与约束变化。** The relevant-versus-warranted distinction changes the evaluation boundary for using sensitive history, not merely memory retrieval accuracy. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** RBI-Eval varies sensitive, benign and irrelevant histories to measure whether memory shifts a response when that use is warranted. The benchmark distinguishes access from justified use; it does not establish user intent, universal privacy norms or production policy correctness. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — We introduce HUSH-Bench, a controlled benchmark of 2,400 benign prompts paired with histories containing one marked sensitive disclosure and matched no-memory references. Model: Disclosed — We evaluate 4 generation models: Claude-Sonnet-4.6 ( Anthropic, 2026 ) , GPT-5.4-mini ( OpenAI, 2026 ) , DeepSeek-V4-Flash ( DeepSeek-AI, 2026 ) , and Qwen3.5-9B ( Qwen Team, 2026 ) . Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06055v1 Methodology: exact heading "E.7 Memory Features by Retrieval System"`；Evaluation: `arXiv:2606.06055v1 Experiments: exact heading "3 Experiments"`；Limitations: `arXiv:2606.06055v1 Scope and Limitations — exact heading or bounded scope route "4 Discussion"`；Artifact: `Artifact URL disclosed in exact-v1: https://arxiv.`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06055:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.06055v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06055:end -->
<!-- review:SF-2026-ARXIV-2606-06055:end -->

<!-- review:SF-2026-ARXIV-2606-06063:start -->
### 2606.06063 — LLM-Based Porting of Optimized C++ to CUDA Through Deoptimization and Reoptimization

**问题、旧方案与约束变化。** The controlled Direct/Deopt-Reopt comparison shows source architecture must be an explicit state in Agentic CPU-to-GPU porting and that success-conditioned speed cannot stand in for end-to-end correctness. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-PLATFORM`。

**机制、实现与 ownership。** The pipeline first deoptimizes specialized C++ into a representation where intent is recoverable, then re-optimizes it for CUDA and checks generated kernels. Tests and benchmarks support covered programs; passing a finite oracle does not prove semantic equivalence, and unsupported idioms can be silently mistranslated. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Not Disclosed — exact-v1 does not identify workload/evaluation slice Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06063v1 Methodology: exact heading "§3 Method / System Design"`；Evaluation: `arXiv:2606.06063v1 Experiments: exact heading "§4 Experiments / Evaluation"`；Limitations: `arXiv:2606.06063v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06063:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06063v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06063:end -->
<!-- review:SF-2026-ARXIV-2606-06063:end -->

<!-- review:SF-2026-ARXIV-2606-06079:start -->
### 2606.06079 — SkillComposer: Learning to Evolve Agent Skills for Specification and Generalization

**问题、旧方案与约束变化。** Create/improve/merge operations and offline/online/hybrid modes make Agent skills evolvable lifecycle objects instead of one-shot prompt snippets. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-PLATFORM`。

**机制、实现与 ownership。** SkillComposer replaces one-shot extraction with three operations and supports offline libraries, online refinement and hybrid use. Agent/code results show complementary improvement/merge effects; rejection sampling, verifier quality and the executor still define the skill's validity. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — However, current skill construction methods treat the problem as one-shot extraction, overlooking a fundamental tension: a skill tailored to the specific task fails to transfer, while the abstracted skill often provides  Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06079v1 Methodology: exact heading "§3 Method / System Design"`；Evaluation: `arXiv:2606.06079v1 Experiments: exact heading "§4 Experiments / Evaluation"`；Limitations: `arXiv:2606.06079v1 Scope and Limitations — exact heading or bounded scope route "Scope and Limitations — conclusion and stated scope boundaries"`；Artifact: `Not Disclosed — no immutable event-time artifact revision used for claims`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06079:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06079v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06079:end -->
<!-- review:SF-2026-ARXIV-2606-06079:end -->

<!-- review:SF-2026-ARXIV-2606-06087:start -->
### 2606.06087 — LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents

**问题、旧方案与约束变化。** Moving skills from plaintext context into modular LoRA state changes updateability, composition, disclosure and provenance ownership even though the reported gains are task-bounded. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-PLATFORM`。

**机制、实现与 ownership。** LatentSkill uses a hypernetwork to compile textual skills into loadable LoRA adapters, reducing repeated prefill and plaintext exposure while retaining scaling/composition. ALFWorld and Search-QA support the tested adapters; weight-space storage is not secrecy, and composition can interfere when parameter directions are misaligned. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — §4 evaluates ALFWorld and Search-QA workloads Model: Disclosed — §4 evaluation uses Qwen3-8B Hardware: Not Disclosed — §4 does not identify evaluation hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06087v1 Methodology: exact heading "§3 Method"`；Evaluation: `arXiv:2606.06087v1 Experiments: exact heading "§4 Experiments"`；Limitations: `arXiv:2606.06087v1 Scope and Limitations — exact heading or bounded scope route "§5 Conclusion and stated scope"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06087:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06087v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06087:end -->
<!-- review:SF-2026-ARXIV-2606-06087:end -->

<!-- review:SF-2026-ARXIV-2606-06090:start -->
### 2606.06090 — Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents

**问题、旧方案与约束变化。** Treating memory as workflow execution state assigns durable status, decisions and handoff ownership separately from semantic document organization. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** MAGE stores branches in a hierarchical state tree and derives active context only from the current valid path. Grow, Compress, Maintain and Revise bound context and isolate invalid traces. MemoryArena evidence supports the tested agents; bad validation or summary can still corrupt a whole subtree. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — §4.1 uses MemoryArena across shopping, travel planning, progressive web search, and formal reasoning Model: Disclosed — §4.1 uses Qwen3.6-27B, with Qwen3-8B-Embedding for embedding-dependent baselines Hardware: Disclosed — §4.1 runs inference on NVIDIA A100 GPUs; count/topology is not stated 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06090v1 Methodology: exact heading "§3 Method; §3.2–3.3 execution-state tree and operations"`；Evaluation: `arXiv:2606.06090v1 Experiments: exact heading "§4 Experiments; §4.1 Experimental Setup"`；Limitations: `arXiv:2606.06090v1 Scope and Limitations — exact heading or bounded scope route "§5 Conclusion; Appendix C Bounded Context Growth"`；Artifact: `arXiv:2606.06090v1 Appendix A Experiment Details; no immutable repository revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06090:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.06090v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06090:end -->
<!-- review:SF-2026-ARXIV-2606-06090:end -->

<!-- review:SF-2026-ARXIV-2606-06178:start -->
### 2606.06178 — Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning

**问题、旧方案与约束变化。** User cost-performance preference becomes learned routing state that must adapt when the routable model set changes, altering model-selection control rather than adding one router score. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-SCHEDULING`。

**机制、实现与 ownership。** MetaRouter treats preference profiles as contextual-bandit tasks and meta-learns fast adaptation to limited feedback. In/out-of-distribution tests support the tested model pools; preference drift and feedback/reward bias remain. 在本次复核中，`INFER-SCHEDULING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — To handle the challenge of heterogeneous user needs, we formulate preference profiles as a set of distinct tasks in contextual bandit and propose MetaRouter, a meta-learning framework designed for preference-aware LLM ro Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06178v1 Methodology: exact heading "§4 Methodology"`；Evaluation: `arXiv:2606.06178v1 Experiments: exact heading "§5 Experiments; §5.1 Experiment Setup"`；Limitations: `arXiv:2606.06178v1 Scope and Limitations — exact heading or bounded scope route "§5.4 Generalization and Scalability; §6 Conclusion"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06178:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06178v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06178:end -->
<!-- review:SF-2026-ARXIV-2606-06178:end -->

<!-- review:SF-2026-ARXIV-2606-06223:start -->
### 2606.06223 — From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents

**问题、旧方案与约束变化。** Reward-hack activation is only latent policy state; combining it with entropy and decision context changes the monitor-to-risk-state contract and prevents activation from being treated as an action verdict. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-MONITORING`。

**机制、实现与 ownership。** Activation scores identify a policy tendency; entropy and decision context determine when it is likely to become an unsafe next action. Gameable environments and steering experiments support layered monitoring, but transfer and causal specificity remain weak. 在本次复核中，`PLATFORM-MONITORING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — We find that adapters fine-tuned on \textit{School-of-Reward-Hacks} dataset can transfer reward-hack tendencies into agentic action selection, especially when the environment exposes proxy-reward affordances. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06223v1 Methodology: exact heading "§3 Method"`；Evaluation: `arXiv:2606.06223v1 Experiments: exact heading "§4 Experimental Setup and Results"`；Limitations: `arXiv:2606.06223v1 Scope and Limitations — exact heading or bounded scope route "§5 Discussion and Limitations"`；Artifact: `arXiv:2606.06223v1 Appendices A–C monitor details and diagnostics; no immutable repository revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06223:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06223v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06223:end -->
<!-- review:SF-2026-ARXIV-2606-06223:end -->

<!-- review:SF-2026-ARXIV-2606-06240:start -->
### 2606.06240 — TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory

**问题、旧方案与约束变化。** Bitemporal valid-time and transaction-time operators define contradiction resolution and history semantics for persistent Agent memory. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** TOKI types common merge heuristics as bitemporal operators with isolation preconditions, dual rows and keyed judge provenance. Proofs define replay consistency and audit preservation; the limited workload comparison claims no system superiority. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — On its one natural-workload slice the audit-row defence moves LoCoMo by 0.86, and ablating the typed memory layer removes 0.49 accuracy on 1,444 answerable LoCoMo questions; the cross-system comparison stays underpowered Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06240v1 Methodology: exact heading "§3 The Toki Operator Algebra"`；Evaluation: `arXiv:2606.06240v1 Experiments: exact heading "§4 Empirical Validation"`；Limitations: `arXiv:2606.06240v1 Scope and Limitations — exact heading or bounded scope route "§6 Limitations and Conclusion; Appendix G Negative Results and Scope Limits"`；Artifact: `arXiv:2606.06240v1 Appendix F Artifact Reproducibility Runbook; immutable commit not established`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06240:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.06240v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06240:end -->
<!-- review:SF-2026-ARXIV-2606-06240:end -->

<!-- review:SF-2026-ARXIV-2606-06256:start -->
### 2606.06256 — RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention

**问题、旧方案与约束变化。** Head-aware reuse plus segmented paging changes long-context KV identity, page layout and execution rather than only model quality. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-KV-CACHE`。

**机制、实现与 ownership。** RedKnot reuses cached context selectively across attention heads and introduces segmented paged attention to serve non-contiguous reused state. Long-context results support reported models/configurations; reuse identity, precision, prefix overlap, concurrency and SLO must remain explicit. 在本次复核中，`INFER-KV-CACHE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — §5.1 uses six long-context QA datasets (HotpotQA, MuSiQue, 2WikiMQA, TriviaQA, MultiFieldQA, Qasper) with 7.9K–65K-token RAG contexts and PD serving slices Model: Disclosed — §5.1 evaluates Llama-3.3-70B, Qwen3-32B, and Mistral-7B Hardware: Disclosed — §5.1 uses one server with 8×NVIDIA H800 80GB, 2×Intel Xeon 8468V, 2TB DDR, and four RoCE v2 interfaces at about 200Gbps unidirectional 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06256v1 Methodology: exact heading "§4 RedKnot Design"`；Evaluation: `arXiv:2606.06256v1 Experiments: exact heading "§5 Evaluation; §5.1 Experimental Setup"`；Limitations: `arXiv:2606.06256v1 Scope and Limitations — exact heading or bounded scope route "§6 Future Work"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06256:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.06256v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06256:end -->
<!-- review:SF-2026-ARXIV-2606-06256:end -->

<!-- review:SF-2026-ARXIV-2606-06284:start -->
### 2606.06284 — ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents

**问题、旧方案与约束变化。** Precondition-effect contracts expose only the causally sufficient next-step tool frontier, making tool-menu state a controlled runtime surface. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-TOOL-CALLING`。

**机制、实现与 ownership。** CMTF uses precondition/effect contracts to compute a minimal next-step tool frontier, reducing menus and token cost without relying only on semantic similarity. Its success depends on complete/correct contracts and state tracking. 在本次复核中，`AGENT-TOOL-CALLING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — §§5–7 use 102 synthetic tasks, 100 tools, six filters, and 2448 task-method-model runs Model: Disclosed — §6.1 uses Amazon Nova 2 Lite, Nova 2 Pro Preview, Claude 3.5 Haiku, and Claude Sonnet 4 Hardware: Not Disclosed — §6 does not identify execution hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06284v1 Methodology: exact heading "§4 Causal Minimal Tool Filtering"`；Evaluation: `arXiv:2606.06284v1 Experiments: exact heading "§5 Benchmark Design; §6 Experimental Setup; §7 Results"`；Limitations: `arXiv:2606.06284v1 Scope and Limitations — exact heading or bounded scope route "§5.5 Scope and later limitations discussion"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06284:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.06284v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06284:end -->
<!-- review:SF-2026-ARXIV-2606-06284:end -->

<!-- review:SF-2026-ARXIV-2606-06302:start -->
### 2606.06302 — Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving

**问题、旧方案与约束变化。** Non-uniform layer/head KV compression changes multi-turn cache allocation and quality accounting at serving time. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-KV-CACHE`。

**机制、实现与 ownership。** Tangram calibrates stable head budgets offline, reserves them at scheduling, uses ragged page tables and precomputes load balance. vLLM evidence supports reported workloads; head stability, quality, GPU, turns, concurrency and SLO are required conditions. 在本次复核中，`INFER-KV-CACHE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Non-uniform KV compression, which allocates heterogeneous budgets across attention heads, preserves accuracy far better than uniform schemes, yet remains impractical: modern serving stacks assume identical KV lengths acr Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06302v1 Methodology: exact heading "§4 Methodology"`；Evaluation: `arXiv:2606.06302v1 Experiments: exact heading "§5 Evaluation; §5.1 Evaluation Setup"`；Limitations: `arXiv:2606.06302v1 Scope and Limitations — exact heading or bounded scope route "§3.1 Limitations on existing system; §7 Conclusion"`；Artifact: `https://github.com/aiha-lab/TANGRAM — repository disclosed; immutable event-time commit not pinned`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06302:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06302v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06302:end -->
<!-- review:SF-2026-ARXIV-2606-06302:end -->

<!-- review:SF-2026-ARXIV-2606-06324:start -->
### 2606.06324 — From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws

**问题、旧方案与约束变化。** Separating harness flaws from model failures changes diagnosis, lifecycle and repair ownership in Agent runtimes. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-PLATFORM`。

**机制、实现与 ownership。** HTIR binds failed trajectory spans to provenance, control-flow and artifact-effect edges before a scoped harness patch is admitted; its held-out gains do not establish causal correctness outside the four benchmark harnesses. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — This paper proposes HarnessFix, a trace-grounded and diagnosis-driven framework for repairing agent harnesses. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06324v1 Methodology: exact heading "§III Approach"`；Evaluation: `arXiv:2606.06324v1 Experiments: exact heading "§IV Experimental Design; §V Results and Analysis"`；Limitations: `arXiv:2606.06324v1 Scope and Limitations — exact heading or bounded scope route "§VI Discussion; §VIII Conclusion"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06324:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.06324v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06324:end -->
<!-- review:SF-2026-ARXIV-2606-06324:end -->

<!-- review:SF-2026-ARXIV-2606-06337:start -->
### 2606.06337 — TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management

**问题、旧方案与约束变化。** A typed graph with supersession, invalidation, bitemporal validity and decision-transition evidence defines resumable session state beyond flat transcript summarization. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** TokenMizer turns session history into a graph whose summaries and links are mutable derived state; graph maintenance buys bounded context but adds stale-edge, summary-loss and rebuild failure modes. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Long-horizon LLM sessions outlive their context windows, and the standard mitigations - truncation, summarization, retrieval - share a structural flaw: they treat history as flat text, discarding precisely the content th Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06337v1 Methodology: exact heading "§IV System Architecture; §§V–VIII pipelines"`；Evaluation: `arXiv:2606.06337v1 Experiments: exact heading "§X Experimental Setup; §XI Results"`；Limitations: `arXiv:2606.06337v1 Scope and Limitations — exact heading or bounded scope route "§XIII Limitations and Future Work"`；Artifact: `https://github.com/Shweta-Mishra-ai/tokenmizer — repository disclosed; immutable event-time commit not pinned`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06337:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06337v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06337:end -->
<!-- review:SF-2026-ARXIV-2606-06337:end -->

<!-- review:SF-2026-ARXIV-2606-06387:start -->
### 2606.06387 — WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents

**问题、旧方案与约束变化。** Tool-surface poisoning at WebMCP discovery time changes protocol trust, runtime authorization and tool metadata admission. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MCP`。

**机制、实现与 ownership。** The attack changes an MCP tool surface during an active session, so tool identity and authorization cannot be checked only at discovery time; the experiments bound exploitability, not all MCP clients or transports. 在本次复核中，`AGENT-MCP` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Based on these results, we outline potential mitigation directions and provide security design recommendations for WebMCP, including binding tool identity to its origin, ensuring lifecycle consistency, enforcing data bou Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06387v1 Methodology: exact heading "§3 Mid-Session Tool Injection"`；Evaluation: `arXiv:2606.06387v1 Experiments: exact heading "§4 Experimental Setup; §5 Results"`；Limitations: `arXiv:2606.06387v1 Scope and Limitations — exact heading or bounded scope route "§9 Limitations"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06387:start -->
**Claim boundary。** Fresh Score V2 = `2/3/3=8`；review route = `deep`；primary evidence = `arXiv:2606.06387v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06387:end -->
<!-- review:SF-2026-ARXIV-2606-06387:end -->

<!-- review:SF-2026-ARXIV-2606-06438:start -->
### 2606.06438 — CarbonSim: A Lifecycle-Aware Framework for Evaluating Carbon Tradeoffs in Hardware Upgrade Decisions

**问题、旧方案与约束变化。** Combining workload, power, embodied carbon, scheduling and time-varying grid intensity changes hardware-refresh evaluation from operational efficiency to lifecycle cost. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-COST`。

**机制、实现与 ownership。** CarbonSim separates embodied upgrade cost from operational savings over an explicit lifecycle horizon; conclusions move with utilization, grid mix, lifetime and performance assumptions rather than defining a universal upgrade rule. 在本次复核中，`PLATFORM-COST` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Although newer hardware often improves performance and energy efficiency, these gains do not always offset the carbon cost of premature replacement, particularly under low-utilization workloads or low-carbon electricity  Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06438v1 Methodology: exact heading "§3 CarbonSim Design"`；Evaluation: `arXiv:2606.06438v1 Experiments: exact heading "§4 Results"`；Limitations: `arXiv:2606.06438v1 Scope and Limitations — exact heading or bounded scope route "§5 Discussion and Future Work"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06438:start -->
**Claim boundary。** Fresh Score V2 = `2/2/3=7`；review route = `deep`；primary evidence = `arXiv:2606.06438v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06438:end -->
<!-- review:SF-2026-ARXIV-2606-06438:end -->

<!-- review:SF-2026-ARXIV-2606-06448:start -->
### 2606.06448 — Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads

**问题、旧方案与约束变化。** Workload characterization ties long-lived Agent state to serving locality, memory pressure and request execution, changing platform capacity assumptions. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `AGENT-MEMORY`。

**机制、实现与 ownership。** The profiling harness separates memory construction, retrieval and answer generation, exposing a write-path/read-path cost frontier; ten systems and two suites characterize workloads but do not rank every production memory architecture. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06448v1 Methodology: exact heading "§2 Agent Memory Paradigms; §3 Workload Suite and Profiling Harness"`；Evaluation: `arXiv:2606.06448v1 Experiments: exact heading "§4 Characterizing Agent Memory Workloads"`；Limitations: `arXiv:2606.06448v1 Scope and Limitations — exact heading or bounded scope route "§5 Discussion and Conclusion"`；Artifact: `Not Disclosed — no immutable event-time artifact revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06448:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.06448v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06448:end -->
<!-- review:SF-2026-ARXIV-2606-06448:end -->

<!-- review:SF-2026-ARXIV-2606-06453:start -->
### 2606.06453 — Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents

**问题、旧方案与约束变化。** Programmable sparse-attention indexes and kernels change request-level serving state and execution for Agent workloads. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-PAGED-ATTENTION`。

**机制、实现与 ownership。** Vortex moves sparse-attention interpretation into a programmable runtime and lowers it into kernels and scheduling state; reported speed/accuracy slices remain model, GPU, precision and length conditional. 在本次复核中，`INFER-PAGED-ATTENTION` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — §6 uses RULER, AMC23, AIME24/AIME26 and synthetic 16K-prompt load tests Model: Disclosed — §6 evaluates Qwen3 0.6B–8B, GLM-4.7-Flash, and MiniMax-M2.7 229B Hardware: Disclosed — §6.2/§6.4 use one H200, one B200, and four B200 GPUs with TP=4 for specified slices 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06453v1 Methodology: exact heading "§3 Programming Model; §4 Interpretation; §5 Execution Optimizations"`；Evaluation: `arXiv:2606.06453v1 Experiments: exact heading "§6 Evaluation; §6.4 Efficiency Evaluations"`；Limitations: `arXiv:2606.06453v1 Scope and Limitations — exact heading or bounded scope route "§7 Conclusion; §11 Ablation Study"`；Artifact: `https://github.com/Infini-AI-Lab/vortex_torch — repository disclosed; immutable event-time commit not pinned`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06453:start -->
**Claim boundary。** Fresh Score V2 = `3/3/2=8`；review route = `deep`；primary evidence = `arXiv:2606.06453v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06453:end -->
<!-- review:SF-2026-ARXIV-2606-06453:end -->

<!-- review:SF-2026-ARXIV-2606-06460:start -->
### 2606.06460 — Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight

**问题、旧方案与约束变化。** Recusal at admission and stop mid-flight are distinct in-band governance events, changing credentialed Agent control semantics. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `PLATFORM-SECURITY`。

**机制、实现与 ownership。** In-band deny and stop signals are evaluated as two different control points, showing that recognition does not imply mid-flight termination; the pilot does not prove enforceable governance without an external reference monitor. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — We define an open mini-standard (access-time deny/throttle/warn and mid-task halt), implement three live adapters (SSH, PostgreSQL, Kubernetes), and measure compliance over SSH across five agents. Model: Disclosed — Agents honor directive granularity (no over-recusal on throttle/warn, 0/176), but throttle showed no measurable self-limiting and no agent surfaced a warn (0/100); an authorization framing flips GPT-4o to proceed. Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06460v1 Methodology: exact heading "§3 Recuse Signal; §4 Adapters"`；Evaluation: `arXiv:2606.06460v1 Experiments: exact heading "§5 Experimental Design; §6 Pilot Results"`；Limitations: `arXiv:2606.06460v1 Scope and Limitations — exact heading or bounded scope route "§9 Limitations and Future Work"`；Artifact: `arXiv:2606.06460v1 §10 Reproducibility — standard, adapters and harness disclosed; immutable revision not pinned`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06460:start -->
**Claim boundary。** Fresh Score V2 = `3/3/3=9`；review route = `deep`；primary evidence = `arXiv:2606.06460v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06460:end -->
<!-- review:SF-2026-ARXIV-2606-06460:end -->

<!-- review:SF-2026-ARXIV-2606-06467:start -->
### 2606.06467 — You Only Index Once: Cross-Layer Sparse Attention with Shared Routing

**问题、旧方案与约束变化。** Sharing sparse-attention routing across layers removes repeated index construction and changes cross-layer access-state ownership. 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `INFER-PAGED-ATTENTION`。

**机制、实现与 ownership。** Shared routing reuses one sparse index across layers to reduce indexing work, trading layer-specific selectivity for reuse; its accuracy and efficiency evidence is architecture- and workload-bound. 在本次复核中，`INFER-PAGED-ATTENTION` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: Disclosed — Experiments across short-context and long-context benchmarks show that CLSA is both accurate and efficient, achieving up to 7.6x decoding speedup and 17.1x overall throughput improvement at 128K context. Model: Not Disclosed — exact-v1 does not identify model/version Hardware: Not Disclosed — exact-v1 does not identify hardware/topology 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `arXiv:2606.06467v1 Methodology: exact heading "§2 Method"`；Evaluation: `arXiv:2606.06467v1 Experiments: exact heading "§3 Experiments; §3.1 Setup"`；Limitations: `arXiv:2606.06467v1 Scope and Limitations — exact heading or bounded scope route "§5 Conclusion; Appendix D/E experimental-scope details"`；Artifact: `arXiv:2606.06467v1 Appendices D–E experimental details; no immutable repository revision identified`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:SF-2026-ARXIV-2606-06467:start -->
**Claim boundary。** Fresh Score V2 = `2/2/2=6`；review route = `standard`；primary evidence = `arXiv:2606.06467v1`。本段不授权 Books 写入。
<!-- claim:SF-2026-ARXIV-2606-06467:end -->
<!-- review:SF-2026-ARXIV-2606-06467:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-05241 | Disclosed — 六个公开 benchmark 上最多约4%的 inflation 只针对所测 agents/search index/time；没有证明私有 benchmark 或未来索引同样幅度。 Locator: https://arxiv.org/html/2606.05241v1 §§4–5 Evaluation and Experiment; Appendices C–E | Disclosed — Appendix C names deep-research agents; detector/base slice uses Qwen3-30B-A3B | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §§4–5 and Appendix D report question/turn detection, inflation and human–automatic agreement |
| SF-2026-ARXIV-2606-05271 | Disclosed — 实验只对 Intel Core Ultra 平台、所列10类模型/FP16/INT8 与 profiler cost model 证明 latency/energy mapping；未证明动态 contention 下仍最优。 Locator: https://arxiv.org/html/2606.05271v1 §4. Evaluation; §4.1 Experimental Setup | Disclosed — ten CNN/Transformer/SSM/KAN/spiking/VLA families | Disclosed — Intel Core Ultra Lunar Lake Series 2 CPU/iGPU/NPU | Disclosed — FP16 and INT8 | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — latency, energy and placement trade-offs across ten pipelines |
| SF-2026-ARXIV-2606-05304 | Disclosed — 作者在所列 MAS topologies/models/tasks 上比较五种 communication strategies，证明无固定策略普适且 PACT 的 cost/quality 权衡；不证明所有协作任务都可压缩为同一 schema。 Locator: https://arxiv.org/html/2606.05304v1 §5 Experiments; §6 Agentic Coding Harnesses | Disclosed — Qwen3-8B/14B/32B plus named Claude/GPT harness models | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Disclosed — The split-evidence interaction uses 4 4 alternating turns, max_new_tokens = 4,096 =4{,}096 per turn, 5–5 split. | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — We report token-overlap F1 for the interaction setting and exact-match accuracy for the pipeline, alongside the average total tokens per problem. |
| SF-2026-ARXIV-2606-05308 | Disclosed — ESCI 的30 human-gold/60,000 judge slice 只证明所列 ranking metrics 的校正与区间性质；不证明 judge 单样本标签正确或任意分布漂移下仍无偏。 Locator: https://arxiv.org/html/2606.05308v1 §3 Results | Disclosed — Claude 3 Sonnet and Haiku judges | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — bias-corrected ranking estimates versus human-gold metrics on a 30-item sample |
| SF-2026-ARXIV-2606-05339 | Disclosed — 经验 taxonomy 只代表筛选时间窗、活跃 repositories 与 issue-reporting bias；不能当作运行时故障率或完备故障集合。 Locator: https://arxiv.org/html/2606.05339v1 §IV-D Selection of Repositories for Manual Analysis; §IV-F Taxonomy Construction and Validation; §V-L Validation Results | Not Applicable — software-ecosystem study | Not Applicable — repository/thread analysis and interviews | Not Applicable — no precision claim | Not Applicable — corpora are not model contexts | Not Applicable — coded observations are not generated outputs | Not Applicable — no runtime batch | Not Applicable — no request concurrency | Not Applicable — no SLO | Disclosed — manual coding of 837 threads and 473 repositories plus validation with 55 practitioners |
| SF-2026-ARXIV-2606-05378 | Disclosed — 12个 task-model cells 无两项共享可比 primary screen，证明该 recipe 的具体 circuit 不可稳定移植；不证明机制完全不可解释或更大模型也无共享结构。 Locator: https://arxiv.org/html/2606.05378v1 §4 Setup; §4.3 Evaluation; §§5–10 | Disclosed — Pythia 1B, OLMo 1B and OLMoE 1B-7B | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — For each task, at the final (target) position we measure top-1 accuracy (does the argmax equal the correct answer?), logit ​ _ ​ diff = logit ⁡ ( correct ) − logit ⁡ ( distractor ) \mathrm{logit\_diff}=\mathrm{logit}(\text{correct})-\mathrm{logit}(\text{distractor}) , and frac ⁡ ( correct > distractor ) \mathrm{frac}(\ |
| SF-2026-ARXIV-2606-05384 | Disclosed — MT-Bench/AlpacaEval、GPT-4o/4o-mini judges 与100 paired instances 只证明所测 interaction 可改变判定；不证明所有 judge 或无对话 benchmark 均可操纵。 Locator: https://arxiv.org/html/2606.05384v1 §§3.2–3.10; §4 Results | Disclosed — GPT-4o and GPT-4o-mini judges | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Applicable — API judge study | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — 100 paired instances are dataset size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §§3–4 define ERS and post-decision consistency metrics |
| SF-2026-ARXIV-2606-05391 | Disclosed — 17名经验开发者的定性访谈提供早期实践锚点，不是频率估计、因果效果或行业代表样本。 Locator: https://arxiv.org/html/2606.05391v1 §4. Findings; §§4.1–4.2 | Not Applicable — qualitative study of 17 developers | Not Applicable — interviews | Not Applicable — no model execution | Not Applicable — interviews are study units | Not Applicable — transcripts/codes are qualitative artifacts | Not Applicable — criterion/snowball sample | Not Applicable — one-to-one interviews | Not Applicable — no SLO | Disclosed — reflexive thematic analysis with the stated recruitment/coding procedure |
| SF-2026-ARXIV-2606-05395 | Disclosed — §5 在两平台、11 specifications、400 plans及40 plans/skill 的局部合同上比较 compliance；没有证明 perception/actuator model 完整或 sim-to-real 物理安全。 Locator: https://arxiv.org/html/2606.05395v1 §5 Empirical Evaluation; Appendices A–B | Disclosed — GPT-5-nano skill generator and GPT-4o-mini plan generator | Not Disclosed — robotic platforms are named but compute is not bound | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — compliance across 400 generated plans |
| SF-2026-ARXIV-2606-05396 | Disclosed — Python/CWE-89、Qwen2.5-Coder 3B/7B/14B、Q4_K_M/Ollama 的初步实验只证明该受限 case；不证明编辑保持其他安全性或能构造高质量通用漏洞数据。 Locator: https://arxiv.org/html/2606.05396v1 §§4–5 Experimental Setup and Results | Disclosed — Qwen2.5-Coder-Instruct 3B/7B/14B, Base and Abliterated | Disclosed — Core Ultra 7 155H, 32 GB RAM, no dedicated GPU | Disclosed — Q4_K_M 4-bit GGUF | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — 600-second timeout is an experiment budget | Disclosed — multiple static/dynamic vulnerability tools with concordance and manual adjudication |
| SF-2026-ARXIV-2606-05403 | Disclosed — 五模型、三领域的行为 dissociation 只证明所构造 impossible CI 等操纵下的 epistemic blind spot；不证明所有引用审查或 tool-verified agent 都失败。 Locator: https://arxiv.org/html/2606.05403v1 §2 Experimental design; Appendices A/D | Disclosed — Claude, Qwen and OLMo; exact identities in Appendix C.8 | Disclosed — EC2 p4de.24xlarge with 8x A100 80 GB | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — We report the correct identification rate (CIR): the fraction of reviews that identify the specific flaw, not just raise generic concerns (Table 3 ; judge validation in Appendix F.2 ). |
| SF-2026-ARXIV-2606-05414 | Disclosed — §§4–5 只在指定 dialog/agent datasets 与 metrics 上证明比 prefix-label baselines 更好的 early-warning tradeoff；不证明 production threshold 或 causal root cause。 Locator: https://arxiv.org/html/2606.05414v1 §4 Experiments; §4.3 Evaluation Metrics; §5 Results | Disclosed — Qwen3-Embedding-0.6B (32K, 1,024 dimensions) plus two-layer MLP predictors | Disclosed — Appendix C reports A100 run costs | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Disclosed — frozen encoder supports 32K; experiments use trajectory prefixes | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Disclosed — Appendix B uses batch 256 | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §4.3 evaluates accuracy–earliness and stopping utility |
| SF-2026-ARXIV-2606-05415 | Disclosed — §4 只在作者数据与 query workload 上证明 ingestion/retrieval traceability；没有证明任意隐含语义可自动恢复或 schema extension 无冲突。 Locator: https://arxiv.org/html/2606.05415v1 §4 Experiments and Results; §§4.1–4.5 | Disclosed — GPT-4.1; cross-model slice adds Claude Haiku 4.5 and Llama 3.3 70B | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — We evaluate end-to-end QA accuracy across four benchmarks (Table 1 ), intrinsic schema/KG quality, and online serving efficiency. |
| SF-2026-ARXIV-2606-05433 | Disclosed — Appendix B/G 给出 proof-cost估算与协议论证，而非 frontier-scale end-to-end deployment；没有证明硬件 telemetry 完整、spec 与真实训练语义完全一致。 Locator: https://arxiv.org/html/2606.05433v1 Appendix B proof-cost/overhead estimation; Appendix G protocol formalization | Disclosed — estimates name Llama 3.1 405B; determinism check uses Llama 7B | Disclosed — determinism measurement uses 8x H100 | Disclosed — BF16 and FP32 are separately analyzed | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — bounded determinism measurement plus analytical cost estimates; no frontier end-to-end deployment benchmark |
| SF-2026-ARXIV-2606-05495 | Disclosed — §5 在 RTX3090/5090 两平台、六 workloads 和 workload-specific batch sweep 上报告 throughput/overhead；不证明 LLM serving、跨 GPU 或生产 tail SLO。 Locator: https://arxiv.org/html/2606.05495v1 §5 Experimental Evaluations; §§5.1–5.3 | Not Applicable — CUDA scheduling workloads | Disclosed — RTX 3090/Xeon 6330 and RTX 5090/i7-11700 | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Disclosed — §5.2 sweeps workload-specific batch values (including 4, 8, 32 and up to 4,096); no universal fixed batch applies | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — throughput/overhead with Nsight Systems across six workloads |
| SF-2026-ARXIV-2606-05523 | Disclosed — §5/appendices 只在 Llama-3.1-8B-Instruct、指定 attacks/evaluators 上证明所测 robustness 变化；未证明对 frontier models、长期自博弈或未知攻击无 reward hacking。 Locator: https://arxiv.org/html/2606.05523v1 §5 Results; Appendices E–F | Disclosed — Llama-3.1-8B-Instruct with LoRA | Disclosed — Appendix H.3 uses one RTX PRO 6000 48 GB | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Disclosed — Appendix H gives stage-specific batches | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §5/Appendices E–F measure attack success, safety/refusal and utility across red-blue rounds |
| SF-2026-ARXIV-2606-05548 | Disclosed — We implement this in \textbf{ADK Arena}, a fully automated pipeline with per-framework Docker isolation, a three-level validation pipeline, and benchmark adapters for SWE-bench, $τ^2$-bench, Terminal-Bench, and MCP-Atlas | Disclosed — Execution uses GPT-5.4 Nano via the token proxy. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05551 | Disclosed — Experiments on two real-world datasets confirm that our approach significantly improves action-conditional performance over conformal baselines. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05558 | Disclosed — Empirically, ADWM achieves accurate value estimates and evaluation reliability across diverse multi-turn agent tasks, demonstrating its promise as a practical framework for offline LLM agent evaluation. | Disclosed — Behavior π b \pi_{b} Evaluation π e \pi_{e} Reward HotpotQA ( Yang et al., 2018 ) ReAct-HotpotQA-SFT ReAct-HotpotQA {DPO, PRM} ( Xiong et al., 2025 ) dense F1 ScienceWorld ( Wang et al., 2022 ) sw-llama-sft sw-llama-eto | Not Disclosed — exact-v1 does not identify hardware/topology | Disclosed — LLM-side π b \pi_{b} / π e \pi_{e} inference is served by vLLM 0.5.4 with bf16 weights and a tensor-parallel size of 1 (one GPU per LLM job). | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Disclosed — Random seeds s ∈ { 0 , 1 , 2 , 3 , 4 } s\in\{0,1,2,3,4\} control: (i) the ε \varepsilon -greedy admissible-action draw, (ii) the imagined-rollout DDPM noise sequence, (iii) the π b \pi_{b} trajectory shuffling at world-m | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05559 | Disclosed — Ideally, adaptation can be performed from accumulated agent experiences and retain prior capabilities while transferring to future tasks. | Disclosed — Our infrastructure uses Qwen3-8B ( Yang et al., 2025 ) with 2xH100 Nvidia GPUs, one for asynchronous training and one for inference. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05568 | Disclosed — As baselines, we compare with BM25 (machine-translated documents, i.e., DT, on NeuCLIRBench and NeuCLIRTech provided by the benchmark to perform lexical matching on English tokens) as the lexical sparse retrieval alterna | Not Disclosed — exact-v1 does not identify model/version | Disclosed — We use eight NVIDIA V100 GPUs and a learning rate of 10 − 4 10^{-4} with a per-device batch size of 2048 vectors for 100k training steps using fp16. | Disclosed — In this work, we propose an embedding quantization approach that turns a ColBERT index into a true inverted index. | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Disclosed — We use eight NVIDIA V100 GPUs and a learning rate of 10 − 4 10^{-4} with a per-device batch size of 2048 vectors for 100k training steps using fp16. | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05597 | Disclosed — We picked WebGym because it is the largest open multi-step visual web-agent training environment to date: roughly 290k training tasks across 128k real-world websites in three difficulty levels (Easy, Medium, Hard), evalu | Disclosed — Rewards are binary, produced by WebGym’s GPT-4o rubric evaluator. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — On the system side, an asynchronous design overlaps rollout, gradient update, and policy refresh across iterations, paired with two web-agent-specific adaptations, namely an everlasting rollout pool and lightweight scree |
| SF-2026-ARXIV-2606-05606 | Disclosed — Under fixed prompt utilities, we prove an $O(\sqrt{K})$ regret bound against the offline allocation benchmark. | Disclosed — We evaluate their performance on four open-weight language models: DeepSeek-R1-Distill-Qwen-1.5B ( Guo et al. | Disclosed — We use H800 GPUs for all runs: the 1.5B and 4B models are trained on 4 4 GPUs, while the 7B model is trained on 8 8 GPUs. | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05610 | Disclosed — To discover these laws, we utilize small-scale proxy models ( N ∈ { 100 ​ M , 500 ​ M } N\in\{100\text{M},500\text{M}\} ) trained on the target CPT dataset. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Disclosed — The efficacy of continued pre-training for Large Language Models (LLMs) hinges upon hyperparameter configurations, such as learning rate and batch size. | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — RQ2 (Accuracy): Can the Equivalent Compute C pre C_{\text{pre}} accurately quantify the initial state of a given checkpoint under domain shift? |
| SF-2026-ARXIV-2606-05646 | Disclosed — However, these agents remain fundamentally episodic: they fail to retain, refine, and reuse experiences across tasks, repeatedly reconstructing context from scratch and reproducing similar mistakes. | Disclosed — M θ \mathbf{\textit{M}}_{\theta} Accuracy (%) Efficiency (%) LA file ( 𝟏 ) \bm{\textbf{{LA}}_{\textit{file}}^{(1)}} LA func ( 𝟏 ) \bm{\textbf{{LA}}_{\textit{func}}^{(1)}} LA file ( − 𝟏 ) \bm{\textbf{{LA}}_{\textit{file}} | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Disclosed — During RL, n rollout n_{\textit{rollout}} denotes the number of rollouts, and c c denotes the batch size of preference rollout in 𝒟 RL \mathcal{D}_{\textit{RL}} (§ 3.3 ). | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Through complementary evaluation on \textit{single-episode} and \textit{cross-episode} memory augmentation, results demonstrate that \ours consistently improves SE agents across settings, achieving absolute gains of up t |
| SF-2026-ARXIV-2606-05662 | Not Disclosed — exact-v1 does not identify workload/evaluation slice | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Disclosed — Laziness is implemented with a double-checked, lock-guarded holder so that, under concurrent forcing from independent branches, the underlying supplier runs exactly once. | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Our experience shows that making methodologies declarative improves reuse, testability, and cross-product consistency while preserving interactive latency. |
| SF-2026-ARXIV-2606-05679 | Disclosed — §5 evaluates TPC-H across scaling, five DBMS engines, policy/source/self-join sweeps, plus an application workload | Not Disclosed — not applicable to this DBMS policy-enforcement workload; no learned model is evaluated | Disclosed — §5.1 uses an 8-core Apple M3 with 16GB RAM for DuckDB/Umbra/PostgreSQL/DataFusion and AWS RDS with 4 vCPUs/16GB RAM for SQL Server | Not Disclosed — not applicable; no numerical model precision or quantization is part of the DBMS benchmark | Not Disclosed — not applicable; the workload is relational queries and database scale, not token input length | Not Disclosed — not applicable; the workload is relational queries and database scale, not token output length | Disclosed — §5.1 reports one warmup followed by five measured runs per configuration | Not Disclosed — §5 does not identify a concurrent-query level | Not Disclosed — §5 reports latency/overhead but defines no acceptance SLO | Disclosed — §5 reports runtime/overhead and scaling against logical/physical provenance baselines |
| SF-2026-ARXIV-2606-05688 | Disclosed — AutoRound optimizes quantization parameters by minimizing a block-wise reconstruction loss on a small calibration dataset. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Disclosed — Mixture-of-Experts (MoE) models scale foundation models efficiently by activating only a subset of experts for each token, but their large number of expert parameters still makes quantization essential for practical depl | Disclosed — We use a maximum calibration sequence length of 2,048 tokens for Solar-Open-100B and 1,024 tokens for Nemotron-3-Nano-30B-A3B. | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Consequently, except for differences in generation quality, VSRAQ has the same memory footprint and inference latency as the corresponding AutoRound-quantized model at the same precision. |
| SF-2026-ARXIV-2606-05711 | Disclosed — Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05725 | Disclosed — Dataset family Attacker query source Normal query source Query-Efficient-Med Self-generated medical domain stealing queries Medicine-related WildChat queries Model-Leeching Template-wrapped SQuAD extraction prompts Origi | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Disclosed — RQ5: How sensitive are results to batch size, threshold, and decision direction? | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Across three random seeds, MMD achieves 0.3% benign FPR, 100.0% pure-attacker TPR, 90.5% average TPR over attacker fractions, and 95.1% balanced accuracy. |
| SF-2026-ARXIV-2606-05742 | Disclosed — Across diverse benchmarks, AdaPLD reduces target-model forward passes and achieves up to $3.10\times$ decoding speedup. | Disclosed — Model Layer Vicuna-7B 9 Vicuna-13B 13 Vicuna-33B 11 Qwen3-8B 29 Table 6: Transformer layer indices used for hidden-state reranking in each model. | Not Disclosed — exact-v1 does not identify hardware/topology | Disclosed — AdaPLD preserves high-precision lexical reuse while using semantic similarity to recover additional reuse opportunities when lexical matching fails. | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05743 | Disclosed — On AgentHarm we keep the same refusal-based definitions, with ASR the fraction of harmful tasks not refused and FRR the refusal rate on benign tasks. | Disclosed — In the main experiments, the target model and all LLM-based components of Membrane are instantiated with Qwen3-8B, served through a self-hosted vLLM endpoint. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — We report Attack Success Rate (ASR), False Refusal Rate (FRR), and their F1, the harmonic mean of the harmful-refusal rate ( 1 − ASR ) (1-\mathrm{ASR}) and benign-admission rate ( 1 − FRR ) (1-\mathrm{FRR}) , F1 = 2 ​ ( |
| SF-2026-ARXIV-2606-05787 | Disclosed — Experiments on four datasets ranging from 2.9k to 8.8M documents demonstrate that SentinelRAG achieves statistically significant detection $p < 10^{-5}$ across all tested configurations at only a 0.1% injection rate. | Disclosed — Dataset GPT-5-mini Qwen-3-8B Gemini-3-Flash GPT-OSS-20B SentinelRAG (Ours) NFCorpus 1.0% 1.0% 0.5% 1.0% FiQA 0.0% 0.0% 0.0% 0.0% MS-MARCO 1.0% 1.0% 1.0% 1.0% HotpotQA 0.0% 0.0% 0.0% 0.0% RAG-WM (Baseline) NFCorpus 7.0% 1 | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — We employed an LLM judge (GPT-5) to evaluate watermark payloads on two metrics: Implausibility Rate (IR) , quantifying contradictions with common knowledge, and Actionability Risk Rate (ARR) , measuring the creation of m |
| SF-2026-ARXIV-2606-05800 | Disclosed — Across diverse reasoning-oriented RLVR benchmarks and model scales, SALT improves effective update geometry and performance without modifying the reward model or the rollout sampling procedure Signed low-rank gradient re | Disclosed — Dataset Method AIME24 AIME25 GSM8K MATH-500 GPQA ACC Pass@8 ACC Pass@8 ACC Pass@8 ACC Pass@8 ACC Pass@8 Deepseek-Distill-Qwen-1.5B ∼ \sim Vanilla 29.1 59.3 22.0 42.6 80.3 95.0 85.5 96.4 34.5 82.4 MATH-TRAIN GRPO 29.3 59. | Not Disclosed — exact-v1 does not identify hardware/topology | Disclosed — This setting serves as an orthogonal, non-math RLVR domain with a high-precision verifier, enabling us to examine whether the signed low-rank geometry and the effectiveness of SALT generalize beyond mathematical reasonin | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Disclosed — SALT estimates a dominant shared subspace from the mini-batch Gram geometry, decomposes group-relative coefficients into shared and residual channels, and adaptively amplifies the residual channel when signed cancellatio | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — To ensure the stability of experiments, we run each experiment five times and report the average results with Accuracy and Pass@8. |
| SF-2026-ARXIV-2606-05805 | Disclosed — However, agent risks often arise when otherwise benign tasks are contaminated by untrusted external content, unsafe instructions, or risky tool use. | Disclosed — Method ASB-DPI ASB-IPI AgentHarm ASR ( ↓ \downarrow ) TSR ( ↑ \uparrow ) RR ASR ( ↓ \downarrow ) TSR ( ↑ \uparrow ) RR HS ( ↑ \uparrow ) Harm ( ↓ \downarrow ) No defense ReAct 86.96 0.00 7.35 99.49 1.57 0.34 36.28 77.04 | Disclosed — In our implementation, Tri-Guard is served with vLLM on a single NVIDIA A100 80GB GPU. | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Extensive experiments on ASB and AgentHarm show that TRIAD reduces the average attack success rate to 10.42%, while achieving the best safety-utility trade-off among guardrail-integrated baselines. |
| SF-2026-ARXIV-2606-05828 | Disclosed — These empirical results reinforce the core conclusion: delegating probabilistic credit assignment to a local statistical prior while reserving the remote LLM strictly for complex intent parsing avoids the systemic failur | Disclosed — To ensure architectural robustness across varying model capabilities, we evaluate all agents using 3 diverse LLM backbones: GPT-5.2 ( OpenAI, 2025b ) , DeepSeek-V4-Flash ( DeepSeek-AI, 2026 ) , and Qwen3-30B-Instruct ( Y | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Extensive evaluations demonstrate that our decoupled approach achieves the lowest cumulative regret and highest test accuracy, significantly outperforming traditional memory-augmented agents. |
| SF-2026-ARXIV-2606-05868 | Disclosed — Compared to their respective base models, YouZhi-7B yields a 12.3% improvement in average financial benchmark score alongside a 2.69$\times$ increase in maximum concurrency; similarly, YouZhi-14B achieves a 7.0% accuracy | Disclosed — Specifically, our resulting models, YouZhi-7B and YouZhi-14B, are converted from the GQA models OpenPangu-7B and Qwen2.5-14B-Instruct, respectively. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Disclosed — Large language models (LLMs) drive significant financial innovations, yet their high-concurrency deployment is severely bottlenecked by KV cache memory overhead, which inflates infrastructure costs and throttles scalabil | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Compared to their respective base models, YouZhi-7B yields a 12.3% improvement in average financial benchmark score alongside a 2.69$\times$ increase in maximum concurrency; similarly, YouZhi-14B achieves a 7.0% accuracy |
| SF-2026-ARXIV-2606-05872 | Disclosed — AI agents are typically instrumented through outcome-oriented indicators such as task success, reward, latency, and cost.Although these indicators are operationally important, they provide limited visibility into the int | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — AI agents are typically instrumented through outcome-oriented indicators such as task success, reward, latency, and cost.Although these indicators are operationally important, they provide limited visibility into the int |
| SF-2026-ARXIV-2606-05875 | Disclosed — We implement QCFuse in SGLang and evaluate it on four open-weight LLMs across six datasets. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Disclosed — All evaluated serving strategies run in the same SGLang-based BF16 serving stack ( Zheng et al., 2023 ; Kwon et al., 2023 ) . | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — 4.4 ) • Serving Throughput. |
| SF-2026-ARXIV-2606-05894 | Disclosed — • LongMemEval-RR is our LongMemEval-derived Budgeted Pre-Query Retention protocol ( Wu et al., 2025 ) , not an official LongMemEval benchmark name. | Disclosed — We fine-tune Qwen2.5-7B and Qwen2.5-14B ( Yang and others, 2024 ) memory-policy backbones on external pre-query episodes, keeping the retriever fixed during rollouts. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05933 | Disclosed — §5 evaluates ShareGPT and arXiv-summarization traces under maximum-goodput, overload, transient-load, ablation, and predictor-fidelity slices | Disclosed — §5 uses Llama3-8B and Qwen2.5-7B | Disclosed — §5 deploys both evaluated models on RTX 3090 GPUs with tensor parallelism TP=2 | Not Disclosed — §5 does not identify numerical precision | Disclosed — §5 compares trace-specific prompt-length distributions, but does not publish one fixed input length | Not Disclosed — §5 does not identify one fixed output-token length | Not Disclosed — §5 does not identify one fixed batch size | Not Disclosed — offered load is reported without a fixed in-flight concurrency contract | Disclosed — §5 evaluates TTFT/TPOT SLO attainment under the paper's stated per-request thresholds; the thresholds are workload-specific, not a universal serving SLO | Disclosed — §5 reports maximum goodput, SLO violations, latency, overload response, ablations, and predictor fidelity |
| SF-2026-ARXIV-2606-05951 | Disclosed — We also examine DeepEP as a case study of NVSHMEM in performance-critical sparse deep learning workloads. | Not Disclosed — exact-v1 does not identify model/version | Disclosed — All measurements in this section were collected on a CoreWeave H200 cluster. | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Disclosed — For inter-node scalar p / g , we additionally use a tuned IBGDA configuration with NVSHMEM_IBGDA_NUM_RC_PER_PE=64 , 64 CTAs, 1024 threads per CTA, to expose the benefit of higher GPU-initiated RDMA concurrency. | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-05958 | Disclosed — Since the technique is plug-and-play, users share datasets and precomputed vectors to steer model activations. | Disclosed — ASR (attack success rate) is the fraction of harmful -prompt responses that a three-judge ensemble ( Claude-Sonnet-4.5 , GPT-4.1 , and Llama-3.3-70B-Instruct , all prompted with the same rubric and instructed to mark loo | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — We test the attack on two open-weight model families and eight model-attribute combinations, observing that poisoned vectors reach an absolute attack success rate (ASR) of $20{-}55\%$, $+19\%$ to $+51\%$ over a clean ref |
| SF-2026-ARXIV-2606-05976 | Disclosed — Recent works show that LLM agents struggle to correct errors in their own reasoning traces, despite their ability to correct errors from external sources. | Disclosed — The open-weight set is served via Ollama and comprises three 70B-class models, Qwen2.5-72B-Instruct ( Qwen 2025 ) , Llama-3.3-70B-Instruct ( Dubey et al. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Scoring uses a locked Qwen-72B judge ( T = 0 T=0 ) that returns YES / NO on whether the continuation explicitly identifies c ⋆ c_{\star} as wrong, following the calibration guidance of Kim and Khashabi (2025) ; the expli |
| SF-2026-ARXIV-2606-06032 | Disclosed — In this work, we investigate an alternative perspective: that forgetting may arise not from complete destruction of task representations but from a loss of accessibility to preserved information. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — We observe complete behavioral forgetting of earlier tasks, with task accuracy collapsing from 54.8% to 0%, while linear probe performance retains approximately 76% of the original representational information. |
| SF-2026-ARXIV-2606-06036 | Disclosed — Experiments on the LoCoMo benchmark and LongMemEval benchmark demonstrate significant improvements over strong baselines (up to 23%), while substantially reducing token and runtime cost, highlighting the effectiveness of | Disclosed — Following prior work, we report F 1 and LLM-Judge (J) scores using GPT-4o-mini, and additionally report evidence recall (Recall) for analysis. | Not Disclosed — exact-v1 does not identify hardware/topology | Disclosed — Aggregating over the dataset, precision and recall are computed as: Precision = ∑ i J ⁡ ( y ^ i , y i ) ∑ i 𝕀 [ y ^ i ≠ ∅ ] , Recall = ∑ i J ⁡ ( y ^ i , y i ) N , \mathrm{Precision}=\frac{\sum_{i}J(\hat{y}_{i},y_{i})}{\s | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Evaluation metrics include F1 score (F1), and LLM-Judge score (J). |
| SF-2026-ARXIV-2606-06044 | Disclosed — Experiments on multiple temporal question answering benchmarks, including TimeQA, TempReason, and ComplexTR, demonstrate that IA-RAG achieves strong temporal retrieval and reasoning performance, particularly on complex c | Disclosed — We employ Qwen2.5-14B-Instruct Qwen et al. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — (2025) , reporting both Accuracy and Recall, computed based on the overlap between the predicted answers and the gold-standard answer. |
| SF-2026-ARXIV-2606-06054 | Disclosed — Our results show that long-term memory is not merely a utility layer, but a durable control channel that can reshape how agents interpret tasks and execute actions, leaving them highly susceptible to the aforementioned t | Disclosed — The evaluated models include Qwen-3-8B [ 26 ] , Llama-3.3-70B-Instruct [ 27 ] , GPT-4o-mini [ 28 ] , GPT-5.1 [ 29 ] , Gemini-3-Pro [ 30 ] , and Claude-Sonnet-4.6 [ 31 ] . | Not Disclosed — exact-v1 does not identify hardware/topology | Disclosed — This suggests that MemGate does not block memory globally; instead, it improves the precision of memory usage. | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Disclosed — We use AdamW with learning rate 1.5 × 10 − 4 1.5\times 10^{-4} , batch size 256, and train for 20 epochs. | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — MemGate is inserted between the vector memory store and the backbone LLM, requiring no LLM modification, memory-database rewriting, or inference-time LLM judge. |
| SF-2026-ARXIV-2606-06055 | Disclosed — We introduce HUSH-Bench, a controlled benchmark of 2,400 benign prompts paired with histories containing one marked sensitive disclosure and matched no-memory references. | Disclosed — We evaluate 4 generation models: Claude-Sonnet-4.6 ( Anthropic, 2026 ) , GPT-5.4-mini ( OpenAI, 2026 ) , DeepSeek-V4-Flash ( DeepSeek-AI, 2026 ) , and Qwen3.5-9B ( Qwen Team, 2026 ) . | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — The scoring pass uses a condition-blind judge that hides model identity, memory condition, and retrieval method and assigns continuous 0–1 scores for the four dimensions, following rubric-based LLM evaluation practice ( |
| SF-2026-ARXIV-2606-06063 | Not Disclosed — exact-v1 does not identify workload/evaluation slice | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Overall, Deopt-Reopt is an effective but non-universal technique for LLM-based GPU porting, with gains that depend on the kernel, the model, the search budget, and the success rate. |
| SF-2026-ARXIV-2606-06079 | Disclosed — However, current skill construction methods treat the problem as one-shot extraction, overlooking a fundamental tension: a skill tailored to the specific task fails to transfer, while the abstracted skill often provides | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06087 | Disclosed — §4 evaluates ALFWorld and Search-QA workloads | Disclosed — §4 evaluation uses Qwen3-8B | Not Disclosed — §4 does not identify evaluation hardware/topology | Not Disclosed — §4 does not identify evaluation precision | Disclosed — Table 1 reports average prefill-token counts by workload | Disclosed — Table 1 reports average decode-token counts by workload | Not Disclosed — §4 does not identify batch size | Not Disclosed — §4 does not identify in-flight concurrency | Not Disclosed — §4 reports outcomes but no acceptance SLO threshold | Disclosed — §4 reports ALFWorld success, Search-QA exact match, and token counts |
| SF-2026-ARXIV-2606-06090 | Disclosed — §4.1 uses MemoryArena across shopping, travel planning, progressive web search, and formal reasoning | Disclosed — §4.1 uses Qwen3.6-27B, with Qwen3-8B-Embedding for embedding-dependent baselines | Disclosed — §4.1 runs inference on NVIDIA A100 GPUs; count/topology is not stated | Not Disclosed — §4.1 does not identify numerical precision | Not Disclosed — tasks run up to hundreds of steps but no fixed input-token length is disclosed | Not Disclosed — §4.1 does not identify output-token limits | Not Disclosed — §4.1 does not identify batch size | Not Disclosed — §4.1 does not identify in-flight concurrency | Not Disclosed — §4 defines no serving acceptance SLO | Disclosed — §4.1 binds task success rate, progress score, and total prompt-plus-generation token consumption |
| SF-2026-ARXIV-2606-06178 | Disclosed — To handle the challenge of heterogeneous user needs, we formulate preference profiles as a set of distinct tasks in contextual bandit and propose MetaRouter, a meta-learning framework designed for preference-aware LLM ro | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06223 | Disclosed — We find that adapters fine-tuned on \textit{School-of-Reward-Hacks} dataset can transfer reward-hack tendencies into agentic action selection, especially when the environment exposes proxy-reward affordances. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06240 | Disclosed — On its one natural-workload slice the audit-row defence moves LoCoMo by 0.86, and ablating the typed memory layer removes 0.49 accuracy on 1,444 answerable LoCoMo questions; the cross-system comparison stays underpowered | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Disclosed — We show that contradiction resolution is write-time concurrency control and make the missing contract explicit. | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — A tightness companion proves that, within the relational schedule model, keyed logging of the adjudicating judge is necessary for replay consistency, which every audited baseline omits. |
| SF-2026-ARXIV-2606-06256 | Disclosed — §5.1 uses six long-context QA datasets (HotpotQA, MuSiQue, 2WikiMQA, TriviaQA, MultiFieldQA, Qasper) with 7.9K–65K-token RAG contexts and PD serving slices | Disclosed — §5.1 evaluates Llama-3.3-70B, Qwen3-32B, and Mistral-7B | Disclosed — §5.1 uses one server with 8×NVIDIA H800 80GB, 2×Intel Xeon 8468V, 2TB DDR, and four RoCE v2 interfaces at about 200Gbps unidirectional | Not Disclosed — §5.1 does not identify one numerical precision contract for all measurements | Disclosed — §5.1 reports 7.9K–65K-token contexts across the six datasets | Not Disclosed — §5.1 does not identify one fixed output-token length | Not Disclosed — §5.1 does not identify one fixed batch size | Disclosed — §5.5 reports sessions-per-GPU and burst-mode throughput slices, but not one universal in-flight concurrency setting | Not Disclosed — §5 reports TTFT and throughput but defines no production acceptance SLO | Disclosed — §5 binds F1/EM and logit fidelity to TTFT, FLOPs, KV bandwidth, throughput, PD-transfer bytes, and sessions-per-GPU |
| SF-2026-ARXIV-2606-06284 | Disclosed — §§5–7 use 102 synthetic tasks, 100 tools, six filters, and 2448 task-method-model runs | Disclosed — §6.1 uses Amazon Nova 2 Lite, Nova 2 Pro Preview, Claude 3.5 Haiku, and Claude Sonnet 4 | Not Disclosed — §6 does not identify execution hardware/topology | Not Disclosed — §6 does not identify numerical precision | Not Disclosed — §6 fixes task context but gives no input-token length | Not Disclosed — §6 says fixed maximum output length without publishing its value | Not Disclosed — §6 does not identify batch size | Not Disclosed — §6 does not identify concurrent execution | Not Disclosed — the controlled benchmark defines no serving SLO | Disclosed — §6.4 defines task success, wrong-tool, premature-action, tools/step, trajectory length, and token cost |
| SF-2026-ARXIV-2606-06302 | Disclosed — Non-uniform KV compression, which allocates heterogeneous budgets across attention heads, preserves accuracy far better than uniform schemes, yet remains impractical: modern serving stacks assume identical KV lengths acr | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Multi-turn LLM serving accumulates dialogue history whose Key-Value (KV) cache grows with every turn and every user, quickly exceeding the model weights themselves and making memory -- not compute -- the binding constrai |
| SF-2026-ARXIV-2606-06324 | Disclosed — This paper proposes HarnessFix, a trace-grounded and diagnosis-driven framework for repairing agent harnesses. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06337 | Disclosed — Long-horizon LLM sessions outlive their context windows, and the standard mitigations - truncation, summarization, retrieval - share a structural flaw: they treat history as flat text, discarding precisely the content th | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06387 | Disclosed — Based on these results, we outline potential mitigation directions and provide security design recommendations for WebMCP, including binding tool identity to its origin, ensuring lifecycle consistency, enforcing data bou | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06438 | Disclosed — Although newer hardware often improves performance and energy efficiency, these gains do not always offset the carbon cost of premature replacement, particularly under low-utilization workloads or low-carbon electricity | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06448 | Disclosed — LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Finally, we derive 10 system recommendations covering construction scheduling, capability floors, amortization via query volume, freshness-latency tradeoffs, and fleet-scale management. |
| SF-2026-ARXIV-2606-06453 | Disclosed — §6 uses RULER, AMC23, AIME24/AIME26 and synthetic 16K-prompt load tests | Disclosed — §6 evaluates Qwen3 0.6B–8B, GLM-4.7-Flash, and MiniMax-M2.7 229B | Disclosed — §6.2/§6.4 use one H200, one B200, and four B200 GPUs with TP=4 for specified slices | Disclosed — §6.4 discloses FP8 for MiniMax scaling runs; other slice precision is not stated | Disclosed — §6.4 uses up to 4K inputs and synthetic 16K-token prompts for the named slices | Disclosed — §6.2/§6.4 use 16K or 32K generation budgets and 512-token load-test outputs | Not Disclosed — §6 does not state a batch size for the serving measurements | Not Disclosed — §6.4 reports 1–8 req/s, not in-flight concurrency | Not Disclosed — §6.4 reports P95 TPOT but defines no acceptance threshold | Disclosed — §6 binds throughput to mean@16/pass@k accuracy and reports P95 TPOT for latency slices |
| SF-2026-ARXIV-2606-06460 | Disclosed — We define an open mini-standard (access-time deny/throttle/warn and mid-task halt), implement three live adapters (SSH, PostgreSQL, Kubernetes), and measure compliance over SSH across five agents. | Disclosed — Agents honor directive granularity (no over-recusal on throttle/warn, 0/176), but throttle showed no measurable self-limiting and no agent surfaced a warn (0/100); an authorization framing flips GPT-4o to proceed. | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Not Disclosed — exact-v1 does not identify evaluator/metric version |
| SF-2026-ARXIV-2606-06467 | Disclosed — Experiments across short-context and long-context benchmarks show that CLSA is both accurate and efficient, achieving up to 7.6x decoding speedup and 17.1x overall throughput improvement at 128K context. | Not Disclosed — exact-v1 does not identify model/version | Not Disclosed — exact-v1 does not identify hardware/topology | Not Disclosed — exact-v1 does not identify precision/quantization | Not Disclosed — exact-v1 does not identify input length | Not Disclosed — exact-v1 does not identify output length | Not Disclosed — exact-v1 does not identify batch | Not Disclosed — exact-v1 does not identify concurrency | Not Disclosed — exact-v1 does not identify an acceptance SLO; reported percentile/TTFT alone is not an SLO | Disclosed — Experiments across short-context and long-context benchmarks show that CLSA is both accurate and efficient, achieving up to 7.6x decoding speedup and 17.1x overall throughput improvement at 128K context. |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-05241 | score_7_9 | not_selected | — | — | Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05241 |
| SF-2026-ARXIV-2606-05271 | forced_review | not_selected | — | — | BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05271 |
| SF-2026-ARXIV-2606-05304 | score_7_9; potential_books_delta | selected | DA-20260604-ACTION-STATE-COMMUNICATION | — | 这是 AGENT-MULTI-AGENT 的 Direct Evolution：通信从 transcript forwarding 变成有 ownership 的状态复制协议。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that replaces transcript forwarding with an explicit public action-state projection while preserving private reasoning ownership; current Message-not-State prose lacks that projection mechanism. It is non-overlapping with NPU resource rebinding and cross-stage poisoning. Mechanism owner: PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。 | analysis:DA-20260604-ACTION-STATE-COMMUNICATION |
| SF-2026-ARXIV-2606-05308 | score_7_9 | not_selected | — | — | Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05308 |
| SF-2026-ARXIV-2606-05339 | score_7_9 | not_selected | — | — | A Taxonomy of Runtime Faults in Model Context Protocol Servers remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05339 |
| SF-2026-ARXIV-2606-05378 | score_7_9 | not_selected | — | — | Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner WORLDVIEW-REPRESENTATION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05378 |
| SF-2026-ARXIV-2606-05384 | score_7_9 | not_selected | — | — | Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05384 |
| SF-2026-ARXIV-2606-05391 | forced_review | not_selected | — | — | Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05391 |
| SF-2026-ARXIV-2606-05395 | score_7_9 | not_selected | — | — | VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05395 |
| SF-2026-ARXIV-2606-05396 | forced_review | not_selected | — | — | Willing but Unable: Separating Refusal from Capability in Code LLMs via Abliteration remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05396 |
| SF-2026-ARXIV-2606-05403 | score_7_9 | not_selected | — | — | Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05403 |
| SF-2026-ARXIV-2606-05414 | forced_review | not_selected | — | — | When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05414 |
| SF-2026-ARXIV-2606-05415 | score_7_9 | not_selected | — | — | Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05415 |
| SF-2026-ARXIV-2606-05433 | score_7_9 | not_selected | — | — | Zero knowledge verification for frontier AI training is possible remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05433 |
| SF-2026-ARXIV-2606-05495 | score_7_9 | not_selected | — | — | SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05495 |
| SF-2026-ARXIV-2606-05523 | forced_review | not_selected | — | — | CHASE: Adversarial Red-Blue Teaming for Improving LLM Safety using Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 6 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05523 |
| SF-2026-ARXIV-2606-05548 | score_7_9 | not_selected | — | — | ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05548 |
| SF-2026-ARXIV-2606-05551 | score_7_9 | not_selected | — | — | Conformal Risk-Averse Decision Making with Action Conditional Guarantee remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05551 |
| SF-2026-ARXIV-2606-05597 | score_7_9 | not_selected | — | — | AsyncWebRL: Efficient Asynchronous Reinforcement Learning for Multi-Step Visual Web Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05597 |
| SF-2026-ARXIV-2606-05610 | score_7_9 | not_selected | — | — | Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05610 |
| SF-2026-ARXIV-2606-05662 | score_7_9 | not_selected | — | — | QDAG: Declarative Composition of Reusable Analytics Methodologies at LinkedIn remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05662 |
| SF-2026-ARXIV-2606-05679 | score_7_9; potential_books_delta | selected | DA-20260605-AUTHORITY | — | Data Flow Control: Data Safety Policies for AI Agents 以 跨工具与数据路径的 authority/provenance enforcement 改变 `PLATFORM-SECURITY` 的长期设计判断；在完整 33-family eligible pool 中，它代表一个不与另两项重复的系统轴，且 exact-v1 同时给出机制、实现与受限证据。 | analysis:DA-20260605-AUTHORITY |
| SF-2026-ARXIV-2606-05933 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05933 |
| SF-2026-ARXIV-2606-05946 | score_7_9 | not_selected | — | — | Short paper: Models in the dark -- Rectification and erasure under GDPR in ML supply chains remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MODEL-REGISTRY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05946 |
| SF-2026-ARXIV-2606-05951 | score_7_9; potential_books_delta | not_selected | — | — | Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05951 |
| SF-2026-ARXIV-2606-05976 | score_7_9 | not_selected | — | — | The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05976 |
| SF-2026-ARXIV-2606-06032 | score_7_9 | not_selected | — | — | Catastrophic Forgetting as Accessibility Collapse: A Three-Level Framework for Knowledge Persistence in Continual Learning remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-CHECKPOINT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06032 |
| SF-2026-ARXIV-2606-06044 | score_7_9 | not_selected | — | — | IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06044 |
| SF-2026-ARXIV-2606-06054 | score_7_9 | not_selected | — | — | Beyond Similarity: Trustworthy Memory Search for Personal AI Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06054 |
| SF-2026-ARXIV-2606-06055 | score_7_9 | not_selected | — | — | HUSH-Bench: Measuring Memory-Use Boundaries for Sensitive History in Conversational Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06055 |
| SF-2026-ARXIV-2606-06090 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06090 |
| SF-2026-ARXIV-2606-06240 | score_7_9; potential_books_delta | selected | DA-20260605-STATE | — | TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory 以 持久记忆写路径的 bitemporal/isolation contract 改变 `AGENT-MEMORY` 的长期设计判断；在完整 33-family eligible pool 中，它代表一个不与另两项重复的系统轴，且 exact-v1 同时给出机制、实现与受限证据。 | analysis:DA-20260605-STATE |
| SF-2026-ARXIV-2606-06256 | score_7_9; potential_books_delta | not_selected | — | — | RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06256 |
| SF-2026-ARXIV-2606-06284 | score_7_9 | not_selected | — | — | ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06284 |
| SF-2026-ARXIV-2606-06324 | score_7_9 | not_selected | — | — | From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06324 |
| SF-2026-ARXIV-2606-06387 | score_7_9 | not_selected | — | — | WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06387 |
| SF-2026-ARXIV-2606-06438 | score_7_9 | not_selected | — | — | CarbonSim: A Lifecycle-Aware Framework for Evaluating Carbon Tradeoffs in Hardware Upgrade Decisions remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06438 |
| SF-2026-ARXIV-2606-06448 | score_7_9 | not_selected | — | — | Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06448 |
| SF-2026-ARXIV-2606-06453 | score_7_9; potential_books_delta | not_selected | — | — | Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-PAGED-ATTENTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06453 |
| SF-2026-ARXIV-2606-06460 | score_7_9 | not_selected | — | — | Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-06460 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-2026-ARXIV-2606-05241:start -->
Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05241:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05271:start -->
BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05271:end -->

<!-- analysis:DA-20260604-ACTION-STATE-COMMUNICATION:start -->
这是 AGENT-MULTI-AGENT 的 Direct Evolution：通信从 transcript forwarding 变成有 ownership 的状态复制协议。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that replaces transcript forwarding with an explicit public action-state projection while preserving private reasoning ownership; current Message-not-State prose lacks that projection mechanism. It is non-overlapping with NPU resource rebinding and cross-stage poisoning. Mechanism owner: PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。
<!-- analysis:DA-20260604-ACTION-STATE-COMMUNICATION:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05308:start -->
Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05308:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05339:start -->
A Taxonomy of Runtime Faults in Model Context Protocol Servers remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05339:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05378:start -->
Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner WORLDVIEW-REPRESENTATION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05378:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05384:start -->
Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05384:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05391:start -->
Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents remains evidence-complete after canonical owner transfer with V2 score 5 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05391:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05395:start -->
VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05395:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05396:start -->
Willing but Unable: Separating Refusal from Capability in Code LLMs via Abliteration remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05396:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05403:start -->
Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05403:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05414:start -->
When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05414:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05415:start -->
Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05415:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05433:start -->
Zero knowledge verification for frontier AI training is possible remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05433:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05495:start -->
SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05495:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05523:start -->
CHASE: Adversarial Red-Blue Teaming for Improving LLM Safety using Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 6 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05523:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05548:start -->
ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05548:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05551:start -->
Conformal Risk-Averse Decision Making with Action Conditional Guarantee remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05551:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05597:start -->
AsyncWebRL: Efficient Asynchronous Reinforcement Learning for Multi-Step Visual Web Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05597:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05610:start -->
Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05610:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05662:start -->
QDAG: Declarative Composition of Reusable Analytics Methodologies at LinkedIn remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05662:end -->

<!-- analysis:DA-20260605-AUTHORITY:start -->
Data Flow Control: Data Safety Policies for AI Agents 以 跨工具与数据路径的 authority/provenance enforcement 改变 `PLATFORM-SECURITY` 的长期设计判断；在完整 33-family eligible pool 中，它代表一个不与另两项重复的系统轴，且 exact-v1 同时给出机制、实现与受限证据。 该 family 进入 selected analysis unit；Full Source Review 与 Books Decision 均保留。
<!-- analysis:DA-20260605-AUTHORITY:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05933:start -->
Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05933:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05946:start -->
Short paper: Models in the dark -- Rectification and erasure under GDPR in ML supply chains remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MODEL-REGISTRY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05946:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05951:start -->
Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05951:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05976:start -->
The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05976:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06032:start -->
Catastrophic Forgetting as Accessibility Collapse: A Three-Level Framework for Knowledge Persistence in Continual Learning remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-CHECKPOINT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06032:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06044:start -->
IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06044:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06054:start -->
Beyond Similarity: Trustworthy Memory Search for Personal AI Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06054:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06055:start -->
HUSH-Bench: Measuring Memory-Use Boundaries for Sensitive History in Conversational Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06055:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06090:start -->
Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06090:end -->

<!-- analysis:DA-20260605-STATE:start -->
TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory 以 持久记忆写路径的 bitemporal/isolation contract 改变 `AGENT-MEMORY` 的长期设计判断；在完整 33-family eligible pool 中，它代表一个不与另两项重复的系统轴，且 exact-v1 同时给出机制、实现与受限证据。 该 family 进入 selected analysis unit；Full Source Review 与 Books Decision 均保留。
<!-- analysis:DA-20260605-STATE:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06256:start -->
RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06256:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06284:start -->
ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06284:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06324:start -->
From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06324:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06387:start -->
WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06387:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06438:start -->
CarbonSim: A Lifecycle-Aware Framework for Evaluating Carbon Tradeoffs in Hardware Upgrade Decisions remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-COST. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06438:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06448:start -->
Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06448:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06453:start -->
Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-PAGED-ATTENTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06453:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-06460:start -->
Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-06460:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-05241 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1654 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L393 | existing:SF-2026-ARXIV-2606-05241 | delta:SF-2026-ARXIV-2606-05241 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05241 |
| SF-2026-ARXIV-2606-05304 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L253 | books/part-07-agent/81-workflow.md#L951; books/part-07-agent/83-mcp.md#L273 | existing:SF-2026-ARXIV-2606-05304 | delta:SF-2026-ARXIV-2606-05304 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-05304 |
| SF-2026-ARXIV-2606-05308 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1158 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L354 | existing:SF-2026-ARXIV-2606-05308 | delta:SF-2026-ARXIV-2606-05308 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05308 |
| SF-2026-ARXIV-2606-05339 | AGENT-MCP | books/part-07-agent/83-mcp.md#L14 | books/part-07-agent/82-multi-agent.md#L539; books/part-07-agent/84-agent-platform.md#L639 | existing:SF-2026-ARXIV-2606-05339 | delta:SF-2026-ARXIV-2606-05339 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05339 |
| SF-2026-ARXIV-2606-05378 | WORLDVIEW-REPRESENTATION | books/part-01-worldview/05-what-neural-networks-learn.md#L178 | books/part-01-worldview/04-why-models-learn.md#L4; books/part-01-worldview/06-why-transformer-changed-the-world.md#L99 | existing:SF-2026-ARXIV-2606-05378 | delta:SF-2026-ARXIV-2606-05378 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05378 |
| SF-2026-ARXIV-2606-05384 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1267 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L334 | existing:SF-2026-ARXIV-2606-05384 | delta:SF-2026-ARXIV-2606-05384 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05384 |
| SF-2026-ARXIV-2606-05395 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L78 | books/part-07-agent/80-reflection.md#L288; books/part-07-agent/82-multi-agent.md#L335 | existing:SF-2026-ARXIV-2606-05395 | delta:SF-2026-ARXIV-2606-05395 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05395 |
| SF-2026-ARXIV-2606-05403 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L429 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L273 | existing:SF-2026-ARXIV-2606-05403 | delta:SF-2026-ARXIV-2606-05403 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05403 |
| SF-2026-ARXIV-2606-05415 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L59 | books/part-05-inference-system/56-inference-scheduling.md#L803; books/part-06-ai-infrastructure/58-kubeflow.md#L126 | existing:SF-2026-ARXIV-2606-05415 | delta:SF-2026-ARXIV-2606-05415 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05415 |
| SF-2026-ARXIV-2606-05433 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L875 | books/part-06-ai-infrastructure/71-multi-tenant.md#L146; books/part-06-ai-infrastructure/73-production-best-practice.md#L76 | existing:SF-2026-ARXIV-2606-05433 | delta:SF-2026-ARXIV-2606-05433 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05433 |
| SF-2026-ARXIV-2606-05495 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L414 | books/part-05-inference-system/55-pd-disaggregation.md#L448; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L190 | existing:SF-2026-ARXIV-2606-05495 | delta:SF-2026-ARXIV-2606-05495 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05495 |
| SF-2026-ARXIV-2606-05548 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1840 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L113; books/part-06-ai-infrastructure/67-monitoring.md#L16 | existing:SF-2026-ARXIV-2606-05548 | delta:SF-2026-ARXIV-2606-05548 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05548 |
| SF-2026-ARXIV-2606-05551 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1840 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L113; books/part-06-ai-infrastructure/67-monitoring.md#L16 | existing:SF-2026-ARXIV-2606-05551 | delta:SF-2026-ARXIV-2606-05551 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05551 |
| SF-2026-ARXIV-2606-05558 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1840 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L113; books/part-06-ai-infrastructure/67-monitoring.md#L16 | existing:SF-2026-ARXIV-2606-05558 | delta:SF-2026-ARXIV-2606-05558 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05558 |
| SF-2026-ARXIV-2606-05559 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L639 | books/part-07-agent/83-mcp.md#L231 | existing:SF-2026-ARXIV-2606-05559 | delta:SF-2026-ARXIV-2606-05559 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05559 |
| SF-2026-ARXIV-2606-05568 | AGENT-RAG | books/part-07-agent/76-rag.md#L99 | books/part-07-agent/75-context.md#L337; books/part-07-agent/77-memory.md#L1116 | existing:SF-2026-ARXIV-2606-05568 | delta:SF-2026-ARXIV-2606-05568 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05568 |
| SF-2026-ARXIV-2606-05597 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L270 | books/part-04-training-system/35-checkpoint.md#L478; books/part-04-training-system/37-tensor-parallel.md#L301 | existing:SF-2026-ARXIV-2606-05597 | delta:SF-2026-ARXIV-2606-05597 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05597 |
| SF-2026-ARXIV-2606-05606 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1320 | books/part-04-training-system/32-ppo.md#L370; books/part-04-training-system/34-dpo.md#L291 | existing:SF-2026-ARXIV-2606-05606 | delta:SF-2026-ARXIV-2606-05606 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05606 |
| SF-2026-ARXIV-2606-05610 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L12 | books/part-04-training-system/27-data.md#L712; books/part-04-training-system/29-sft.md#L444 | existing:SF-2026-ARXIV-2606-05610 | delta:SF-2026-ARXIV-2606-05610 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05610 |
| SF-2026-ARXIV-2606-05646 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-05646 | delta:SF-2026-ARXIV-2606-05646 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05646 |
| SF-2026-ARXIV-2606-05662 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L168 | books/part-05-inference-system/56-inference-scheduling.md#L776; books/part-06-ai-infrastructure/58-kubeflow.md#L57 | existing:SF-2026-ARXIV-2606-05662 | delta:SF-2026-ARXIV-2606-05662 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05662 |
| SF-2026-ARXIV-2606-05679 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1020 | books/part-06-ai-infrastructure/71-multi-tenant.md#L80; books/part-06-ai-infrastructure/73-production-best-practice.md#L174 | existing:SF-2026-ARXIV-2606-05679 | delta:SF-2026-ARXIV-2606-05679 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-05679 |
| SF-2026-ARXIV-2606-05688 | MODEL-MOE | books/part-02-model/21-moe.md#L446 | books/part-02-model/20-sampling.md#L221; books/part-02-model/22-long-context.md#L592 | existing:SF-2026-ARXIV-2606-05688 | delta:SF-2026-ARXIV-2606-05688 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05688 |
| SF-2026-ARXIV-2606-05711 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L273 | books/part-07-agent/81-workflow.md#L796; books/part-07-agent/83-mcp.md#L209 | existing:SF-2026-ARXIV-2606-05711 | delta:SF-2026-ARXIV-2606-05711 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05711 |
| SF-2026-ARXIV-2606-05725 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1020 | books/part-06-ai-infrastructure/71-multi-tenant.md#L80; books/part-06-ai-infrastructure/73-production-best-practice.md#L174 | existing:SF-2026-ARXIV-2606-05725 | delta:SF-2026-ARXIV-2606-05725 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05725 |
| SF-2026-ARXIV-2606-05742 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L248 | books/part-05-inference-system/47-pagedattention.md#L245; books/part-05-inference-system/49-tensorrt-llm.md#L1161 | existing:SF-2026-ARXIV-2606-05742 | delta:SF-2026-ARXIV-2606-05742 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05742 |
| SF-2026-ARXIV-2606-05743 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1020 | books/part-06-ai-infrastructure/71-multi-tenant.md#L80; books/part-06-ai-infrastructure/73-production-best-practice.md#L174 | existing:SF-2026-ARXIV-2606-05743 | delta:SF-2026-ARXIV-2606-05743 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05743 |
| SF-2026-ARXIV-2606-05787 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1020 | books/part-06-ai-infrastructure/71-multi-tenant.md#L80; books/part-06-ai-infrastructure/73-production-best-practice.md#L174 | existing:SF-2026-ARXIV-2606-05787 | delta:SF-2026-ARXIV-2606-05787 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05787 |
| SF-2026-ARXIV-2606-05800 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1320 | books/part-04-training-system/32-ppo.md#L370; books/part-04-training-system/34-dpo.md#L291 | existing:SF-2026-ARXIV-2606-05800 | delta:SF-2026-ARXIV-2606-05800 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05800 |
| SF-2026-ARXIV-2606-05805 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1020 | books/part-06-ai-infrastructure/71-multi-tenant.md#L80; books/part-06-ai-infrastructure/73-production-best-practice.md#L174 | existing:SF-2026-ARXIV-2606-05805 | delta:SF-2026-ARXIV-2606-05805 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05805 |
| SF-2026-ARXIV-2606-05828 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L639 | books/part-07-agent/83-mcp.md#L231 | existing:SF-2026-ARXIV-2606-05828 | delta:SF-2026-ARXIV-2606-05828 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05828 |
| SF-2026-ARXIV-2606-05868 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889 | books/part-05-inference-system/44-decode.md#L273; books/part-05-inference-system/46-continuous-batching.md#L251 | existing:SF-2026-ARXIV-2606-05868 | delta:SF-2026-ARXIV-2606-05868 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05868 |
| SF-2026-ARXIV-2606-05872 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L268 | books/part-06-ai-infrastructure/66-evaluation-system.md#L2159; books/part-06-ai-infrastructure/68-logging.md#L70 | existing:SF-2026-ARXIV-2606-05872 | delta:SF-2026-ARXIV-2606-05872 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05872 |
| SF-2026-ARXIV-2606-05875 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889 | books/part-05-inference-system/44-decode.md#L273; books/part-05-inference-system/46-continuous-batching.md#L251 | existing:SF-2026-ARXIV-2606-05875 | delta:SF-2026-ARXIV-2606-05875 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05875 |
| SF-2026-ARXIV-2606-05894 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-05894 | delta:SF-2026-ARXIV-2606-05894 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05894 |
| SF-2026-ARXIV-2606-05933 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L776 | books/part-05-inference-system/55-pd-disaggregation.md#L150; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L76 | existing:SF-2026-ARXIV-2606-05933 | delta:SF-2026-ARXIV-2606-05933 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-05933 |
| SF-2026-ARXIV-2606-05946 | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#L205 | books/part-06-ai-infrastructure/58-kubeflow.md#L84; books/part-06-ai-infrastructure/60-training-operator.md#L126 | existing:SF-2026-ARXIV-2606-05946 | delta:SF-2026-ARXIV-2606-05946 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05946 |
| SF-2026-ARXIV-2606-05951 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L270 | books/part-04-training-system/35-checkpoint.md#L478; books/part-04-training-system/37-tensor-parallel.md#L301 | existing:SF-2026-ARXIV-2606-05951 | delta:SF-2026-ARXIV-2606-05951 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-05951 |
| SF-2026-ARXIV-2606-05958 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1020 | books/part-06-ai-infrastructure/71-multi-tenant.md#L80; books/part-06-ai-infrastructure/73-production-best-practice.md#L174 | existing:SF-2026-ARXIV-2606-05958 | delta:SF-2026-ARXIV-2606-05958 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05958 |
| SF-2026-ARXIV-2606-05976 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L89 | books/part-07-agent/79-planning.md#L273; books/part-07-agent/81-workflow.md#L698 | existing:SF-2026-ARXIV-2606-05976 | delta:SF-2026-ARXIV-2606-05976 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05976 |
| SF-2026-ARXIV-2606-06032 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#L478 | books/part-04-training-system/34-dpo.md#L151; books/part-04-training-system/36-distributed-training.md#L517 | existing:SF-2026-ARXIV-2606-06032 | delta:SF-2026-ARXIV-2606-06032 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06032 |
| SF-2026-ARXIV-2606-06036 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-06036 | delta:SF-2026-ARXIV-2606-06036 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06036 |
| SF-2026-ARXIV-2606-06044 | AGENT-RAG | books/part-07-agent/76-rag.md#L99 | books/part-07-agent/75-context.md#L337; books/part-07-agent/77-memory.md#L1116 | existing:SF-2026-ARXIV-2606-06044 | delta:SF-2026-ARXIV-2606-06044 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06044 |
| SF-2026-ARXIV-2606-06054 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-06054 | delta:SF-2026-ARXIV-2606-06054 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06054 |
| SF-2026-ARXIV-2606-06055 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-06055 | delta:SF-2026-ARXIV-2606-06055 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06055 |
| SF-2026-ARXIV-2606-06063 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L639 | books/part-07-agent/83-mcp.md#L231 | existing:SF-2026-ARXIV-2606-06063 | delta:SF-2026-ARXIV-2606-06063 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06063 |
| SF-2026-ARXIV-2606-06079 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L639 | books/part-07-agent/83-mcp.md#L231 | existing:SF-2026-ARXIV-2606-06079 | delta:SF-2026-ARXIV-2606-06079 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06079 |
| SF-2026-ARXIV-2606-06087 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L639 | books/part-07-agent/83-mcp.md#L231 | existing:SF-2026-ARXIV-2606-06087 | delta:SF-2026-ARXIV-2606-06087 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06087 |
| SF-2026-ARXIV-2606-06090 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-06090 | delta:SF-2026-ARXIV-2606-06090 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-06090 |
| SF-2026-ARXIV-2606-06178 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L776 | books/part-05-inference-system/55-pd-disaggregation.md#L150; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L76 | existing:SF-2026-ARXIV-2606-06178 | delta:SF-2026-ARXIV-2606-06178 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06178 |
| SF-2026-ARXIV-2606-06223 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L268 | books/part-06-ai-infrastructure/66-evaluation-system.md#L2159; books/part-06-ai-infrastructure/68-logging.md#L70 | existing:SF-2026-ARXIV-2606-06223 | delta:SF-2026-ARXIV-2606-06223 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06223 |
| SF-2026-ARXIV-2606-06240 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-06240 | delta:SF-2026-ARXIV-2606-06240 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-06240 |
| SF-2026-ARXIV-2606-06256 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889 | books/part-05-inference-system/44-decode.md#L273; books/part-05-inference-system/46-continuous-batching.md#L251 | existing:SF-2026-ARXIV-2606-06256 | delta:SF-2026-ARXIV-2606-06256 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-06256 |
| SF-2026-ARXIV-2606-06284 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L423 | books/part-07-agent/77-memory.md#L476; books/part-07-agent/79-planning.md#L163 | existing:SF-2026-ARXIV-2606-06284 | delta:SF-2026-ARXIV-2606-06284 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06284 |
| SF-2026-ARXIV-2606-06302 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889 | books/part-05-inference-system/44-decode.md#L273; books/part-05-inference-system/46-continuous-batching.md#L251 | existing:SF-2026-ARXIV-2606-06302 | delta:SF-2026-ARXIV-2606-06302 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06302 |
| SF-2026-ARXIV-2606-06324 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L639 | books/part-07-agent/83-mcp.md#L231 | existing:SF-2026-ARXIV-2606-06324 | delta:SF-2026-ARXIV-2606-06324 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06324 |
| SF-2026-ARXIV-2606-06337 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-06337 | delta:SF-2026-ARXIV-2606-06337 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06337 |
| SF-2026-ARXIV-2606-06387 | AGENT-MCP | books/part-07-agent/83-mcp.md#L227 | books/part-07-agent/82-multi-agent.md#L487; books/part-07-agent/84-agent-platform.md#L639 | existing:SF-2026-ARXIV-2606-06387 | delta:SF-2026-ARXIV-2606-06387 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06387 |
| SF-2026-ARXIV-2606-06438 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L172 | books/part-06-ai-infrastructure/69-trace.md#L103; books/part-06-ai-infrastructure/71-multi-tenant.md#L67 | existing:SF-2026-ARXIV-2606-06438 | delta:SF-2026-ARXIV-2606-06438 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06438 |
| SF-2026-ARXIV-2606-06448 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1116 | books/part-07-agent/76-rag.md#L407; books/part-07-agent/78-tool-calling.md#L344 | existing:SF-2026-ARXIV-2606-06448 | delta:SF-2026-ARXIV-2606-06448 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06448 |
| SF-2026-ARXIV-2606-06453 | INFER-PAGED-ATTENTION | books/part-05-inference-system/47-pagedattention.md#L253 | books/part-05-inference-system/46-continuous-batching.md#L73; books/part-05-inference-system/48-speculative-decoding.md#L675 | existing:SF-2026-ARXIV-2606-06453 | delta:SF-2026-ARXIV-2606-06453 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-06453 |
| SF-2026-ARXIV-2606-06460 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1020 | books/part-06-ai-infrastructure/71-multi-tenant.md#L80; books/part-06-ai-infrastructure/73-production-best-practice.md#L174 | existing:SF-2026-ARXIV-2606-06460 | delta:SF-2026-ARXIV-2606-06460 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06460 |
| SF-2026-ARXIV-2606-06467 | INFER-PAGED-ATTENTION | books/part-05-inference-system/47-pagedattention.md#L253 | books/part-05-inference-system/46-continuous-batching.md#L73; books/part-05-inference-system/48-speculative-decoding.md#L675 | existing:SF-2026-ARXIV-2606-06467 | delta:SF-2026-ARXIV-2606-06467 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06467 |

<!-- books-review:SF-2026-ARXIV-2606-05241:start -->
<!-- existing:SF-2026-ARXIV-2606-05241:start -->Slice suites**：验证特定语言、风险、长度或 tenant。<!-- existing:SF-2026-ARXIV-2606-05241:end -->

<!-- delta:SF-2026-ARXIV-2606-05241:start -->研究定义 metadata、question-context、explicit-answer 三层 STC，并从 search traces 检测泄漏、重算去污染结果。browser trace 持有检索证据，benchmark owner 保存题目身份，contamination auditor 决定样本是否计分。<!-- delta:SF-2026-ARXIV-2606-05241:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1654`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L393. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05241:end -->

<!-- books-review:SF-2026-ARXIV-2606-05304:start -->
<!-- existing:SF-2026-ARXIV-2606-05304:start -->Message 作为 event 保留，authoritative state 由 workflow transition 更新。一个 agent 说“B 已完成”不能替代 B 的 signed/verified output。<!-- existing:SF-2026-ARXIV-2606-05304:end -->

<!-- delta:SF-2026-ARXIV-2606-05304:start -->PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。<!-- delta:SF-2026-ARXIV-2606-05304:end -->

Target `AGENT-MULTI-AGENT` at `books/part-07-agent/82-multi-agent.md#L253`; adjacent refs: books/part-07-agent/81-workflow.md#L951; books/part-07-agent/83-mcp.md#L273. Decision: `Integrate`. Post-write verified at `books/part-07-agent/82-multi-agent.md#L255` with SHA-256 `7021f12173a5a3bdc2578440316780c67325ceee5077319d11a06372794eeef2`.
<!-- books-review:SF-2026-ARXIV-2606-05304:end -->

<!-- books-review:SF-2026-ARXIV-2606-05308:start -->
<!-- existing:SF-2026-ARXIV-2606-05308:start -->这份偏差。Prediction-powered inference 一类方法因此改变的是 estimator，而不是把 metric 升级为 ground truth：<!-- existing:SF-2026-ARXIV-2606-05308:end -->

<!-- delta:SF-2026-ARXIV-2606-05308:start -->PRECISE 用 prediction-powered inference 将大规模 judge predictions 与小规模 human residual correction 合成 bias-corrected ranking metric，并为 Precision@K 压缩 output-space computation。human labels 是校准数据，judge scores 是辅助信号，estimator 持有置信区间控制。<!-- delta:SF-2026-ARXIV-2606-05308:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1158`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L354. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05308:end -->

<!-- books-review:SF-2026-ARXIV-2606-05339:start -->
<!-- existing:SF-2026-ARXIV-2606-05339:start -->本章的核心判断是：**MCP 标准化 AI host 与能力提供方之间的发现、消息、生命周期和协商接口；它降低 M×N 集成成本，但不替代 tool semantics、authorization policy、workflow reliability 或 server trust assessment。**<!-- existing:SF-2026-ARXIV-2606-05339:end -->

<!-- delta:SF-2026-ARXIV-2606-05339:start -->研究对473 repositories中的837 fault threads做 bottom-up coding，形成11大类、27子类/73 leaf faults，并按 interaction、tool、schema、state、安全和取消路径分配故障类型。issue evidence 是数据，taxonomy 是诊断状态，maintainer/release process 掌握修复控制。<!-- delta:SF-2026-ARXIV-2606-05339:end -->

Target `AGENT-MCP` at `books/part-07-agent/83-mcp.md#L14`; adjacent refs: books/part-07-agent/82-multi-agent.md#L539; books/part-07-agent/84-agent-platform.md#L639. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05339:end -->

<!-- books-review:SF-2026-ARXIV-2606-05378:start -->
<!-- existing:SF-2026-ARXIV-2606-05378:start -->更强的 contract 是用外部 ground-truth target 约束 decodability，并由与训练 reader 独立的 fresh probe 审计。它减少训练 reader 与表示共同作弊的循环性，却仍受 probe drift、目标遗漏和 correlation≠causation 限制；因果使用仍必须回到 intervention 与 downstream behavior。<!-- existing:SF-2026-ARXIV-2606-05378:end -->

<!-- delta:SF-2026-ARXIV-2606-05378:start -->统一 screen-and-ablate protocol 在四任务、三种1B architecture上比较 matched-random null，并把 head 归为 primary/secondary cause、correlate、interferer 或 null。activations 是观测数据，ablation controller 施加干预，taxonomy 持有因果判定。<!-- delta:SF-2026-ARXIV-2606-05378:end -->

Target `WORLDVIEW-REPRESENTATION` at `books/part-01-worldview/05-what-neural-networks-learn.md#L178`; adjacent refs: books/part-01-worldview/04-why-models-learn.md#L4; books/part-01-worldview/06-why-transformer-changed-the-world.md#L99. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05378:end -->

<!-- books-review:SF-2026-ARXIV-2606-05384:start -->
<!-- existing:SF-2026-ARXIV-2606-05384:start -->Evaluator 的 aggregate accuracy 可能同时掩盖两种相反失败：目标事实已经改变，judge 却保持原 verdict；无关表达被改写，judge 又错误地改变 verdict。因而 construct validity 不应压成一个标量，而应至少有两条受控 intervention arm：<!-- existing:SF-2026-ARXIV-2606-05384:end -->

<!-- delta:SF-2026-ARXIV-2606-05384:start -->protocol 先固定 initial decision，再施加 repeated/neutral、anti-baseline 与 counterbalanced target challenges，用 ERS 等指标分离稳定性、可逆性和定向操纵。conversation state 是新增数据，judge 持有 verdict，evaluation harness 控制挑战顺序。<!-- delta:SF-2026-ARXIV-2606-05384:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1267`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L334. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05384:end -->

<!-- books-review:SF-2026-ARXIV-2606-05395:start -->
<!-- existing:SF-2026-ARXIV-2606-05395:start -->这种 activation contract 不取代数据库、object manifest 或 consensus log，只规定它们必须原子绑定哪些 agent-state 语义。有限状态空间验证可以证明抽象 protocol 在已编码 transitions 下没有违反 invariant，却不覆盖 WAL crash、network partition、storage bug、真实签名持久化、外部 side-effect atomicity 或高并发延迟。因此低并发、single writer、无持久副作用的短任务仍可使用更简单的 version/CAS；multi-writer、跨恢复和高权限 workflow 才需要完整的 branch head、writer fencing、receipt 与 lifecycle contract。<!-- existing:SF-2026-ARXIV-2606-05395:end -->

<!-- delta:SF-2026-ARXIV-2606-05395:start -->VASO 将 skill 表示为 planner-facing interface 与 formal state/action proposition contract，迭代生成 labeling function、model checking counterexample 和 skill refinement。contract 持有安全状态，robot plan 是数据，verifier 掌握执行前授权。<!-- delta:SF-2026-ARXIV-2606-05395:end -->

Target `AGENT-WORKFLOW` at `books/part-07-agent/81-workflow.md#L78`; adjacent refs: books/part-07-agent/80-reflection.md#L288; books/part-07-agent/82-multi-agent.md#L335. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05395:end -->

<!-- books-review:SF-2026-ARXIV-2606-05403:start -->
<!-- existing:SF-2026-ARXIV-2606-05403:start -->outcome 会掩盖 epistemic failure，不证明 scaffold 普遍无效，也未验证把该 taxonomy 作为训练目标就能修复。<!-- existing:SF-2026-ARXIV-2606-05403:end -->

<!-- delta:SF-2026-ARXIV-2606-05403:start -->实验正交操纵 methodology register 与 numerical validity，比较单源识别和多源 influence。source text/number 是证据数据，synthesis model 持有权重分配，validity probe 检查是否调用已具备的识别能力。<!-- delta:SF-2026-ARXIV-2606-05403:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L429`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L273. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05403:end -->

<!-- books-review:SF-2026-ARXIV-2606-05415:start -->
<!-- existing:SF-2026-ARXIV-2606-05415:start -->这解释了为什么 Kubernetes 常成为底座：它提供声明式 API、controller 和资源模型。但 Kubernetes 不认识 checkpoint 是否通过评估、Tokenizer 是否匹配、KV Cache 是否属于某个模型身份。这些是 AI Platform 必须增加的 domain contracts。<!-- existing:SF-2026-ARXIV-2606-05415:end -->

<!-- delta:SF-2026-ARXIV-2606-05415:start -->系统用 closed-world field catalog 约束 schema discovery，确定性推断 keys/hierarchy，并以同一 executable schema 驱动 extraction、dedup、KG linking 与多工具 retrieval。schema/version 持有契约，provenance graph 是状态，router 控制查询路径。<!-- delta:SF-2026-ARXIV-2606-05415:end -->

Target `PLATFORM-FOUNDATIONS` at `books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L59`; adjacent refs: books/part-05-inference-system/56-inference-scheduling.md#L803; books/part-06-ai-infrastructure/58-kubeflow.md#L126. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05415:end -->

<!-- books-review:SF-2026-ARXIV-2606-05433:start -->
<!-- existing:SF-2026-ARXIV-2606-05433:start -->→ effect-time authorization<!-- existing:SF-2026-ARXIV-2606-05433:end -->

<!-- delta:SF-2026-ARXIV-2606-05433:start -->方案预提交 training specification，采集 inter-node network observations，并在线生成 intermediate-computation Merkle commitments，使用具 native tensor primitives 的 zkVM 抽查/证明。trainer 持有执行状态，commitments/telemetry 是审计数据，verifier 掌握合规判定。<!-- delta:SF-2026-ARXIV-2606-05433:end -->

Target `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L875`; adjacent refs: books/part-06-ai-infrastructure/71-multi-tenant.md#L146; books/part-06-ai-infrastructure/73-production-best-practice.md#L76. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05433:end -->

<!-- books-review:SF-2026-ARXIV-2606-05495:start -->
<!-- existing:SF-2026-ARXIV-2606-05495:start -->短 horizon 可预见 capacity release，长 horizon 却更依赖未知 output、future arrivals 与尚未做出的决策。<!-- existing:SF-2026-ARXIV-2606-05495:end -->

<!-- delta:SF-2026-ARXIV-2606-05495:start -->SET 为每 worker 绑定 stream、pre-instantiated graph 和独立 buffers，用 event chaining/work stealing 在完成时派发下一 job。per-stream buffer 持有 in-flight state，CUDA events 是控制信号，scheduler 掌握 worker/slot 所有权。<!-- delta:SF-2026-ARXIV-2606-05495:end -->

Target `INFER-SCHEDULING` at `books/part-05-inference-system/56-inference-scheduling.md#L414`; adjacent refs: books/part-05-inference-system/55-pd-disaggregation.md#L448; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L190. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05495:end -->

<!-- books-review:SF-2026-ARXIV-2606-05548:start -->
<!-- existing:SF-2026-ARXIV-2606-05548:start -->Store-results-without-contract。** 保存一堆 metrics，却没有 dataset、scorer、environment 和 subject identity。替代方案是把 Evaluation Run 作为不可变证据对象。<!-- existing:SF-2026-ARXIV-2606-05548:end -->

<!-- delta:SF-2026-ARXIV-2606-05548:start -->Freezing the developer, ADK API/documentation surface, isolated runner, generation effort and downstream agent outcomes changes how Agent frameworks are compared rather than merely adding one task score.<!-- delta:SF-2026-ARXIV-2606-05548:end -->

实际读取 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L1840` 与相邻章节 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L113 ; books/part-06-ai-infrastructure/67-monitoring.md#L16`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05548:end -->

<!-- books-review:SF-2026-ARXIV-2606-05551:start -->
<!-- existing:SF-2026-ARXIV-2606-05551:start -->Store-results-without-contract。** 保存一堆 metrics，却没有 dataset、scorer、environment 和 subject identity。替代方案是把 Evaluation Run 作为不可变证据对象。<!-- existing:SF-2026-ARXIV-2606-05551:end -->

<!-- delta:SF-2026-ARXIV-2606-05551:start -->Action-conditional rather than marginal conformal coverage changes the safety guarantee attached to each released decision and therefore the evaluation/release contract.<!-- delta:SF-2026-ARXIV-2606-05551:end -->

实际读取 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L1840` 与相邻章节 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L113 ; books/part-06-ai-infrastructure/67-monitoring.md#L16`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05551:end -->

<!-- books-review:SF-2026-ARXIV-2606-05558:start -->
<!-- existing:SF-2026-ARXIV-2606-05558:start -->Store-results-without-contract。** 保存一堆 metrics，却没有 dataset、scorer、environment 和 subject identity。替代方案是把 Evaluation Run 作为不可变证据对象。<!-- existing:SF-2026-ARXIV-2606-05558:end -->

<!-- delta:SF-2026-ARXIV-2606-05558:start -->Off-policy Agent evaluation from logged trajectories introduces an explicit surrogate-environment boundary and policy-conditioned transition contract instead of requiring live execution.<!-- delta:SF-2026-ARXIV-2606-05558:end -->

实际读取 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L1840` 与相邻章节 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L113 ; books/part-06-ai-infrastructure/67-monitoring.md#L16`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05558:end -->

<!-- books-review:SF-2026-ARXIV-2606-05559:start -->
<!-- existing:SF-2026-ARXIV-2606-05559:start -->Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。<!-- existing:SF-2026-ARXIV-2606-05559:end -->

<!-- delta:SF-2026-ARXIV-2606-05559:start -->CLaaS assigns rollout storage, replay, asynchronous parameter updates and serving-time model refresh to a deployment service, changing state and control ownership.<!-- delta:SF-2026-ARXIV-2606-05559:end -->

实际读取 owner `books/part-07-agent/84-agent-platform.md#L639` 与相邻章节 `books/part-07-agent/83-mcp.md#L231`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05559:end -->

<!-- books-review:SF-2026-ARXIV-2606-05568:start -->
<!-- existing:SF-2026-ARXIV-2606-05568:start -->Retrieval metric 必须与 Agent 实际 query distribution 对齐。面向自然问题训练的 dense retriever，未必适合 deep-research Agent 生成的短 entity、keyword 或逐步 subquery；更强 encoder 在接口分布错位时也可能输给 lexical baseline。评估应联合版本化 query generator、corpus/index、retriever/reranker、packing policy 与 context use，并分开报告 source recall、duplicate eviden<!-- existing:SF-2026-ARXIV-2606-05568:end -->

<!-- delta:SF-2026-ARXIV-2606-05568:start -->Turning ColBERT token storage into a quantized inverted index changes persistent index layout, gather/decompression work and MaxSim data flow, not only retrieval accuracy.<!-- delta:SF-2026-ARXIV-2606-05568:end -->

实际读取 owner `books/part-07-agent/76-rag.md#L99` 与相邻章节 `books/part-07-agent/75-context.md#L337 ; books/part-07-agent/77-memory.md#L1116`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05568:end -->

<!-- books-review:SF-2026-ARXIV-2606-05597:start -->
<!-- existing:SF-2026-ARXIV-2606-05597:start -->两者共享 latency、bandwidth、topology、copy avoidance 与 completion 等第一性问题，却不应被写成 `Collective -> NIXL` 的直接替代史。第 52 章从分布式推理 runtime 解释数据移动与编排边界，第 55 章进一步讨论 Prefill/Decode 分离中的 KV ownership 与 transfer。<!-- existing:SF-2026-ARXIV-2606-05597:end -->

<!-- delta:SF-2026-ARXIV-2606-05597:start -->Overlapping rollout, update and policy refresh with an everlasting rollout pool changes distributed RL execution and freshness ownership; the trajectory normalizer finding also changes token-budget accounting.<!-- delta:SF-2026-ARXIV-2606-05597:end -->

实际读取 owner `books/part-04-training-system/36-distributed-training.md#L270` 与相邻章节 `books/part-04-training-system/35-checkpoint.md#L478 ; books/part-04-training-system/37-tensor-parallel.md#L301`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05597:end -->

<!-- books-review:SF-2026-ARXIV-2606-05606:start -->
<!-- existing:SF-2026-ARXIV-2606-05606:start -->它没有让 RL 变简单到只剩一个公式。Group variance、rollout generation、reward specification、token credit、policy synchronization 和 implementation variants 共同决定训练是否有效。<!-- existing:SF-2026-ARXIV-2606-05606:end -->

<!-- delta:SF-2026-ARXIV-2606-05606:start -->A posterior over prompt success and a global cross-epoch budget make rollout allocation durable training-resource state rather than a fixed per-prompt hyperparameter.<!-- delta:SF-2026-ARXIV-2606-05606:end -->

实际读取 owner `books/part-04-training-system/33-grpo.md#L1320` 与相邻章节 `books/part-04-training-system/32-ppo.md#L370 ; books/part-04-training-system/34-dpo.md#L291`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05606:end -->

<!-- books-review:SF-2026-ARXIV-2606-05610:start -->
<!-- existing:SF-2026-ARXIV-2606-05610:start -->第 27 章已经把数据构造成 token sequences，Part II 也已经给出 Decoder-only 模型。模型怎样仅通过预测下一个 token 改变数十亿参数？Loss 下降、perplexity、训练 token 数、optimizer step 与能力增长分别是什么关系？梯度异常时，warmup、clipping、adaptive optimizer 与逐层 learning rate 分别能解决什么？为什么一次成功的 Pretraining run 不只是反复调用 `backward()`？<!-- existing:SF-2026-ARXIV-2606-05610:end -->

<!-- delta:SF-2026-ARXIV-2606-05610:start -->Checkpoint-equivalent compute and proxy-derived learning-rate/batch laws change continued-pretraining resource planning and stability judgment rather than reporting one optimum.<!-- delta:SF-2026-ARXIV-2606-05610:end -->

实际读取 owner `books/part-04-training-system/28-pretraining.md#L12` 与相邻章节 `books/part-04-training-system/27-data.md#L712 ; books/part-04-training-system/29-sft.md#L444`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05610:end -->

<!-- books-review:SF-2026-ARXIV-2606-05646:start -->
<!-- existing:SF-2026-ARXIV-2606-05646:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-05646:end -->

<!-- delta:SF-2026-ARXIV-2606-05646:start -->Validated downstream impact is used both as a task-agnostic memory evaluation contract and as the closed-loop optimization signal across episodes.<!-- delta:SF-2026-ARXIV-2606-05646:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05646:end -->

<!-- books-review:SF-2026-ARXIV-2606-05662:start -->
<!-- existing:SF-2026-ARXIV-2606-05662:start -->AI Platform 的本质是统一 identity、state、policy 和 feedback，使模型生命周期从个人操作变成组织能力。下一章以 Kubeflow 为例，观察这组抽象如何建立在 Kubernetes reconciliation 之上，以及为什么一个生态不能自动等同于一个完整平台。<!-- existing:SF-2026-ARXIV-2606-05662:end -->

<!-- delta:SF-2026-ARXIV-2606-05662:start -->QDAG moves production analytics methodology from drifting imperative glue into typed, composable, demand-driven DAG state deployed across 500 hosts and 100 use cases.<!-- delta:SF-2026-ARXIV-2606-05662:end -->

实际读取 owner `books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L168` 与相邻章节 `books/part-05-inference-system/56-inference-scheduling.md#L776 ; books/part-06-ai-infrastructure/58-kubeflow.md#L57`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05662:end -->

<!-- books-review:SF-2026-ARXIV-2606-05679:start -->
<!-- existing:SF-2026-ARXIV-2606-05679:start -->模型生成的计划、代码或工具调用只是一份 proposal。要成为执行 authority，必须先编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity；airlock 负责验证 schema 和证据，broker 只授予完成该动作所需的短期能力。证书化增加 admission latency 与 TCB，证据陈旧、policy/validator drift 或 emergency bypass 都会破坏保证，因此既有 IAM、sandbox 和 effect-time au<!-- existing:SF-2026-ARXIV-2606-05679:end -->

<!-- delta:SF-2026-ARXIV-2606-05679:start -->Optimizer-invariant tuple-level provenance predicates move Agent data-release safety from prompts into the DBMS, giving the data plane enforcement ownership.<!-- delta:SF-2026-ARXIV-2606-05679:end -->

实际读取 owner `books/part-06-ai-infrastructure/72-security.md#L1020` 与相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md#L80 ; books/part-06-ai-infrastructure/73-production-best-practice.md#L174`。Decision: `Integrate`。该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05679:end -->

<!-- books-review:SF-2026-ARXIV-2606-05688:start -->
<!-- existing:SF-2026-ARXIV-2606-05688:start -->标准 MoE 也不是先把数据按“数学、代码、语言”拆开，再逐个训练独立 experts。通常 shared layers、router 与 experts 在同一个端到端 objective 下 joint optimization：一个 token 的主任务梯度只进入它实际选择的 expert paths，shared layers 接收跨 routes 的信号，router 同时受到主任务信号与 load-balancing/capacity 约束。于是每个 expert 看到的是 router 动态形成的条件样本分布，而不是人工声明且永久不变的领域 dataset。<!-- existing:SF-2026-ARXIV-2606-05688:end -->

<!-- delta:SF-2026-ARXIV-2606-05688:start -->Quantization can change top-k expert identity; preserving router value and ordering therefore becomes part of MoE quantization correctness, not an optional quality metric.<!-- delta:SF-2026-ARXIV-2606-05688:end -->

实际读取 owner `books/part-02-model/21-moe.md#L446` 与相邻章节 `books/part-02-model/20-sampling.md#L221 ; books/part-02-model/22-long-context.md#L592`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05688:end -->

<!-- books-review:SF-2026-ARXIV-2606-05711:start -->
<!-- existing:SF-2026-ARXIV-2606-05711:start -->Gate 只管理 communication，不拥有 shared state 或 action authority。它会新增 false reject、correlated judge、<!-- existing:SF-2026-ARXIV-2606-05711:end -->

<!-- delta:SF-2026-ARXIV-2606-05711:start -->The text-versus-latent communication framework exposes what state crosses Agent boundaries, how sender/receiver spaces align and how the receiver fuses it; this corrects the durable protocol model even though the paper is a synthesis.<!-- delta:SF-2026-ARXIV-2606-05711:end -->

实际读取 owner `books/part-07-agent/82-multi-agent.md#L273` 与相邻章节 `books/part-07-agent/81-workflow.md#L796 ; books/part-07-agent/83-mcp.md#L209`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05711:end -->

<!-- books-review:SF-2026-ARXIV-2606-05725:start -->
<!-- existing:SF-2026-ARXIV-2606-05725:start -->模型生成的计划、代码或工具调用只是一份 proposal。要成为执行 authority，必须先编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity；airlock 负责验证 schema 和证据，broker 只授予完成该动作所需的短期能力。证书化增加 admission latency 与 TCB，证据陈旧、policy/validator drift 或 emergency bypass 都会破坏保证，因此既有 IAM、sandbox 和 effect-time au<!-- existing:SF-2026-ARXIV-2606-05725:end -->

<!-- delta:SF-2026-ARXIV-2606-05725:start -->Model-extraction detection is defined over benign-calibrated traffic windows, making cross-request distribution state and service-level thresholds explicit security state.<!-- delta:SF-2026-ARXIV-2606-05725:end -->

实际读取 owner `books/part-06-ai-infrastructure/72-security.md#L1020` 与相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md#L80 ; books/part-06-ai-infrastructure/73-production-best-practice.md#L174`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05725:end -->

<!-- books-review:SF-2026-ARXIV-2606-05742:start -->
<!-- existing:SF-2026-ARXIV-2606-05742:start -->这里 predictor 只拥有 proposal budget，不拥有 correctness。Target 的 verification、sampling policy 和 rollback<!-- existing:SF-2026-ARXIV-2606-05742:end -->

<!-- delta:SF-2026-ARXIV-2606-05742:start -->Adaptive retrieval and reuse of prior draft candidates changes model-free speculative proposal state and the acceptance/control loop.<!-- delta:SF-2026-ARXIV-2606-05742:end -->

实际读取 owner `books/part-05-inference-system/48-speculative-decoding.md#L248` 与相邻章节 `books/part-05-inference-system/47-pagedattention.md#L245 ; books/part-05-inference-system/49-tensorrt-llm.md#L1161`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05742:end -->

<!-- books-review:SF-2026-ARXIV-2606-05743:start -->
<!-- existing:SF-2026-ARXIV-2606-05743:start -->模型生成的计划、代码或工具调用只是一份 proposal。要成为执行 authority，必须先编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity；airlock 负责验证 schema 和证据，broker 只授予完成该动作所需的短期能力。证书化增加 admission latency 与 TCB，证据陈旧、policy/validator drift 或 emergency bypass 都会破坏保证，因此既有 IAM、sandbox 和 effect-time au<!-- existing:SF-2026-ARXIV-2606-05743:end -->

<!-- delta:SF-2026-ARXIV-2606-05743:start -->Contrastive safety-memory cells jointly store block and permit conditions and evolve without retraining, changing guardrail state, poisoning risk and cross-attack reuse.<!-- delta:SF-2026-ARXIV-2606-05743:end -->

实际读取 owner `books/part-06-ai-infrastructure/72-security.md#L1020` 与相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md#L80 ; books/part-06-ai-infrastructure/73-production-best-practice.md#L174`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05743:end -->

<!-- books-review:SF-2026-ARXIV-2606-05787:start -->
<!-- existing:SF-2026-ARXIV-2606-05787:start -->模型生成的计划、代码或工具调用只是一份 proposal。要成为执行 authority，必须先编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity；airlock 负责验证 schema 和证据，broker 只授予完成该动作所需的短期能力。证书化增加 admission latency 与 TCB，证据陈旧、policy/validator drift 或 emergency bypass 都会破坏保证，因此既有 IAM、sandbox 和 effect-time au<!-- existing:SF-2026-ARXIV-2606-05787:end -->

<!-- delta:SF-2026-ARXIV-2606-05787:start -->Owner-only sentinel probes and synthetic database entries introduce a provenance/detection contract for unauthorized RAG datastore redistribution.<!-- delta:SF-2026-ARXIV-2606-05787:end -->

实际读取 owner `books/part-06-ai-infrastructure/72-security.md#L1020` 与相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md#L80 ; books/part-06-ai-infrastructure/73-production-best-practice.md#L174`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05787:end -->

<!-- books-review:SF-2026-ARXIV-2606-05800:start -->
<!-- existing:SF-2026-ARXIV-2606-05800:start -->它没有让 RL 变简单到只剩一个公式。Group variance、rollout generation、reward specification、token credit、policy synchronization 和 implementation variants 共同决定训练是否有效。<!-- existing:SF-2026-ARXIV-2606-05800:end -->

<!-- delta:SF-2026-ARXIV-2606-05800:start -->The feature-concentration diagnosis shows why more group rollouts can stop adding training signal and changes the design judgment for allocating rollout compute.<!-- delta:SF-2026-ARXIV-2606-05800:end -->

实际读取 owner `books/part-04-training-system/33-grpo.md#L1320` 与相邻章节 `books/part-04-training-system/32-ppo.md#L370 ; books/part-04-training-system/34-dpo.md#L291`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05800:end -->

<!-- books-review:SF-2026-ARXIV-2606-05805:start -->
<!-- existing:SF-2026-ARXIV-2606-05805:start -->模型生成的计划、代码或工具调用只是一份 proposal。要成为执行 authority，必须先编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity；airlock 负责验证 schema 和证据，broker 只授予完成该动作所需的短期能力。证书化增加 admission latency 与 TCB，证据陈旧、policy/validator drift 或 emergency bypass 都会破坏保证，因此既有 IAM、sandbox 和 effect-time au<!-- existing:SF-2026-ARXIV-2606-05805:end -->

<!-- delta:SF-2026-ARXIV-2606-05805:start -->Returning a constrained remediation plan rather than only allow/deny changes the guardrail-to-agent action interface and the authority boundary for recovery.<!-- delta:SF-2026-ARXIV-2606-05805:end -->

实际读取 owner `books/part-06-ai-infrastructure/72-security.md#L1020` 与相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md#L80 ; books/part-06-ai-infrastructure/73-production-best-practice.md#L174`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05805:end -->

<!-- books-review:SF-2026-ARXIV-2606-05828:start -->
<!-- existing:SF-2026-ARXIV-2606-05828:start -->Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。<!-- existing:SF-2026-ARXIV-2606-05828:end -->

<!-- delta:SF-2026-ARXIV-2606-05828:start -->Strictly separating local statistical preference state from remote semantic intent parsing changes selection authority and privacy/cost ownership in personal Agent harnesses.<!-- delta:SF-2026-ARXIV-2606-05828:end -->

实际读取 owner `books/part-07-agent/84-agent-platform.md#L639` 与相邻章节 `books/part-07-agent/83-mcp.md#L231`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05828:end -->

<!-- books-review:SF-2026-ARXIV-2606-05868:start -->
<!-- existing:SF-2026-ARXIV-2606-05868:start -->多轮 serving 可在同机异构模型间借用 idle HBM/NVLink 保存 hot prefix，但 cache identity、donor pressure 与回收优先级必须由控制面持有。借用 idle HBM 能降低 P99 TTFT，但 donor pressure 或跨模型 identity 错配会引起抖动/污染；回收阈值失效时回退本地 KV 与普通 eviction，不能宣称跨机收益。 coding-Agent KV workload 的 prefix reuse、branching 与长 idle gap 不同于聊天；cache manager 应按 repository<!-- existing:SF-2026-ARXIV-2606-05868:end -->

<!-- delta:SF-2026-ARXIV-2606-05868:start -->Adaptive GQA-to-MLA transition changes KV representation and concurrency memory layout; the financial workload is evidence, not the owner of the mechanism.<!-- delta:SF-2026-ARXIV-2606-05868:end -->

实际读取 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889` 与相邻章节 `books/part-05-inference-system/44-decode.md#L273 ; books/part-05-inference-system/46-continuous-batching.md#L251`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05868:end -->

<!-- books-review:SF-2026-ARXIV-2606-05872:start -->
<!-- existing:SF-2026-ARXIV-2606-05872:start -->Monitoring 承接第 66 章对 Evaluation/Observability 的边界，为第 57 章 Evidence Plane 提供聚合 observed state，并向 evaluation sampling、autoscaling、admission、cost 与 incident response 提供输入。下一章转向离散事件：当指标告诉我们“出问题了”，Logging 如何留下可查询证据。<!-- existing:SF-2026-ARXIV-2606-05872:end -->

<!-- delta:SF-2026-ARXIV-2606-05872:start -->Deriving exploration, rigidity, tool concentration and uncertainty-reduction telemetry from traces adds an Agent-behavior observability plane beyond outcome metrics.<!-- delta:SF-2026-ARXIV-2606-05872:end -->

实际读取 owner `books/part-06-ai-infrastructure/67-monitoring.md#L268` 与相邻章节 `books/part-06-ai-infrastructure/66-evaluation-system.md#L2159 ; books/part-06-ai-infrastructure/68-logging.md#L70`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05872:end -->

<!-- books-review:SF-2026-ARXIV-2606-05875:start -->
<!-- existing:SF-2026-ARXIV-2606-05875:start -->多轮 serving 可在同机异构模型间借用 idle HBM/NVLink 保存 hot prefix，但 cache identity、donor pressure 与回收优先级必须由控制面持有。借用 idle HBM 能降低 P99 TTFT，但 donor pressure 或跨模型 identity 错配会引起抖动/污染；回收阈值失效时回退本地 KV 与普通 eviction，不能宣称跨机收益。 coding-Agent KV workload 的 prefix reuse、branching 与长 idle gap 不同于聊天；cache manager 应按 repository<!-- existing:SF-2026-ARXIV-2606-05875:end -->

<!-- delta:SF-2026-ARXIV-2606-05875:start -->Query-aware compressed cache fusion changes the identity, granularity and quality boundary of reusable RAG prefill state.<!-- delta:SF-2026-ARXIV-2606-05875:end -->

实际读取 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889` 与相邻章节 `books/part-05-inference-system/44-decode.md#L273 ; books/part-05-inference-system/46-continuous-batching.md#L251`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05875:end -->

<!-- books-review:SF-2026-ARXIV-2606-05894:start -->
<!-- existing:SF-2026-ARXIV-2606-05894:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-05894:end -->

<!-- delta:SF-2026-ARXIV-2606-05894:start -->Budgeted evidence retention makes provenance, eviction and future retrieval cost explicit long-horizon memory state rather than flat context trimming.<!-- delta:SF-2026-ARXIV-2606-05894:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05894:end -->

<!-- books-review:SF-2026-ARXIV-2606-05933:start -->
<!-- existing:SF-2026-ARXIV-2606-05933:start -->Decode 期间每个请求的 KV 持续增长，scheduler 的 admission 与 eviction 会反过来改变未来可用容量。若大量相似请求同步进入同一阶段，系统可能形成 admission、memory pressure、eviction、再 admission 的 limit cycle；因此 capacity controller 需要把 KV growth 作为动态 state，而不是只看当前 queue length。<!-- existing:SF-2026-ARXIV-2606-05933:end -->

<!-- delta:SF-2026-ARXIV-2606-05933:start -->SLO-aware sliding-window chunking changes batch construction, latency prediction and fairness state under shared inference contention.<!-- delta:SF-2026-ARXIV-2606-05933:end -->

实际读取 owner `books/part-05-inference-system/56-inference-scheduling.md#L776` 与相邻章节 `books/part-05-inference-system/55-pd-disaggregation.md#L150 ; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L76`。Decision: `Integrate`。该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05933:end -->

<!-- books-review:SF-2026-ARXIV-2606-05946:start -->
<!-- existing:SF-2026-ARXIV-2606-05946:start -->SF-2026-ARXIV-2606-22875**：FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs 的 exact-v1 机制为：In this paper, we propose FedOT, the first framework for ownership verification and leakage tracing in federated LDMs. 因此 把 ownership/provenance 证据与 artifact hash、client iden<!-- existing:SF-2026-ARXIV-2606-05946:end -->

<!-- delta:SF-2026-ARXIV-2606-05946:start -->The models-in-the-dark finding shows rectification/erasure cannot be enforced without lineage across derived models and supply-chain actors, correcting model-registry lifecycle ownership.<!-- delta:SF-2026-ARXIV-2606-05946:end -->

实际读取 owner `books/part-06-ai-infrastructure/59-model-registry.md#L205` 与相邻章节 `books/part-06-ai-infrastructure/58-kubeflow.md#L84 ; books/part-06-ai-infrastructure/60-training-operator.md#L126`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05946:end -->

<!-- books-review:SF-2026-ARXIV-2606-05951:start -->
<!-- existing:SF-2026-ARXIV-2606-05951:start -->两者共享 latency、bandwidth、topology、copy avoidance 与 completion 等第一性问题，却不应被写成 `Collective -> NIXL` 的直接替代史。第 52 章从分布式推理 runtime 解释数据移动与编排边界，第 55 章进一步讨论 Prefill/Decode 分离中的 KV ownership 与 transfer。<!-- existing:SF-2026-ARXIV-2606-05951:end -->

<!-- delta:SF-2026-ARXIV-2606-05951:start -->Symmetric memory and device-initiated one-sided communication change ownership and initiation of sparse AI communication, a runtime mechanism rather than an application benchmark.<!-- delta:SF-2026-ARXIV-2606-05951:end -->

实际读取 owner `books/part-04-training-system/36-distributed-training.md#L270` 与相邻章节 `books/part-04-training-system/35-checkpoint.md#L478 ; books/part-04-training-system/37-tensor-parallel.md#L301`。Decision: `Integrate`。该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05951:end -->

<!-- books-review:SF-2026-ARXIV-2606-05958:start -->
<!-- existing:SF-2026-ARXIV-2606-05958:start -->模型生成的计划、代码或工具调用只是一份 proposal。要成为执行 authority，必须先编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity；airlock 负责验证 schema 和证据，broker 只授予完成该动作所需的短期能力。证书化增加 admission latency 与 TCB，证据陈旧、policy/validator drift 或 emergency bypass 都会破坏保证，因此既有 IAM、sandbox 和 effect-time au<!-- existing:SF-2026-ARXIV-2606-05958:end -->

<!-- delta:SF-2026-ARXIV-2606-05958:start -->Activation-steering artifacts become a model-control supply-chain input that can be poisoned, requiring admission, provenance and mitigation boundaries.<!-- delta:SF-2026-ARXIV-2606-05958:end -->

实际读取 owner `books/part-06-ai-infrastructure/72-security.md#L1020` 与相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md#L80 ; books/part-06-ai-infrastructure/73-production-best-practice.md#L174`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05958:end -->

<!-- books-review:SF-2026-ARXIV-2606-05976:start -->
<!-- existing:SF-2026-ARXIV-2606-05976:start -->episode evidence 编译成下一 episode 的 actor prompt/state update。Workflow owner 必须持有 environment reset、<!-- existing:SF-2026-ARXIV-2606-05976:end -->

<!-- delta:SF-2026-ARXIV-2606-05976:start -->Byte-identical errors become correctable when their chat role changes, correcting the durable belief that self-correction failure is purely a reasoning-capability deficit.<!-- delta:SF-2026-ARXIV-2606-05976:end -->

实际读取 owner `books/part-07-agent/80-reflection.md#L89` 与相邻章节 `books/part-07-agent/79-planning.md#L273 ; books/part-07-agent/81-workflow.md#L698`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-05976:end -->

<!-- books-review:SF-2026-ARXIV-2606-06032:start -->
<!-- existing:SF-2026-ARXIV-2606-06032:start -->沿 State 横线，本章把第 19 章已经出现的运行时模型状态问题扩展为带 logical step、version 与 commit boundary 的训练事务；第 42 章随后把同样的 identity、ownership 与 completion 问题应用到在线 request lifecycle。两者是状态原则复用，不共享 checkpoint 格式或提交协议。<!-- existing:SF-2026-ARXIV-2606-06032:end -->

<!-- delta:SF-2026-ARXIV-2606-06032:start -->Separating storage, representation and accessibility shows behavioral forgetting can coexist with recoverable checkpoint knowledge, changing what forgetting and recovery checks must measure.<!-- delta:SF-2026-ARXIV-2606-06032:end -->

实际读取 owner `books/part-04-training-system/35-checkpoint.md#L478` 与相邻章节 `books/part-04-training-system/34-dpo.md#L151 ; books/part-04-training-system/36-distributed-training.md#L517`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06032:end -->

<!-- books-review:SF-2026-ARXIV-2606-06036:start -->
<!-- existing:SF-2026-ARXIV-2606-06036:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-06036:end -->

<!-- delta:SF-2026-ARXIV-2606-06036:start -->Reconstructing graph memory at query time changes what is authoritative stored state versus derived retrieval state for long-horizon agents.<!-- delta:SF-2026-ARXIV-2606-06036:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06036:end -->

<!-- books-review:SF-2026-ARXIV-2606-06044:start -->
<!-- existing:SF-2026-ARXIV-2606-06044:start -->Retrieval metric 必须与 Agent 实际 query distribution 对齐。面向自然问题训练的 dense retriever，未必适合 deep-research Agent 生成的短 entity、keyword 或逐步 subquery；更强 encoder 在接口分布错位时也可能输给 lexical baseline。评估应联合版本化 query generator、corpus/index、retriever/reranker、packing policy 与 context use，并分开报告 source recall、duplicate eviden<!-- existing:SF-2026-ARXIV-2606-06044:end -->

<!-- delta:SF-2026-ARXIV-2606-06044:start -->Interval entities, Allen relations and fuzzy-bound tightening give dynamic knowledge explicit validity semantics rather than treating time as flat metadata.<!-- delta:SF-2026-ARXIV-2606-06044:end -->

实际读取 owner `books/part-07-agent/76-rag.md#L99` 与相邻章节 `books/part-07-agent/75-context.md#L337 ; books/part-07-agent/77-memory.md#L1116`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06044:end -->

<!-- books-review:SF-2026-ARXIV-2606-06054:start -->
<!-- existing:SF-2026-ARXIV-2606-06054:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-06054:end -->

<!-- delta:SF-2026-ARXIV-2606-06054:start -->Separating similarity from authority, recency and user control changes the admission and ranking contract for personal memory.<!-- delta:SF-2026-ARXIV-2606-06054:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06054:end -->

<!-- books-review:SF-2026-ARXIV-2606-06055:start -->
<!-- existing:SF-2026-ARXIV-2606-06055:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-06055:end -->

<!-- delta:SF-2026-ARXIV-2606-06055:start -->The relevant-versus-warranted distinction changes the evaluation boundary for using sensitive history, not merely memory retrieval accuracy.<!-- delta:SF-2026-ARXIV-2606-06055:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06055:end -->

<!-- books-review:SF-2026-ARXIV-2606-06063:start -->
<!-- existing:SF-2026-ARXIV-2606-06063:start -->Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。<!-- existing:SF-2026-ARXIV-2606-06063:end -->

<!-- delta:SF-2026-ARXIV-2606-06063:start -->The controlled Direct/Deopt-Reopt comparison shows source architecture must be an explicit state in Agentic CPU-to-GPU porting and that success-conditioned speed cannot stand in for end-to-end correctness.<!-- delta:SF-2026-ARXIV-2606-06063:end -->

实际读取 owner `books/part-07-agent/84-agent-platform.md#L639` 与相邻章节 `books/part-07-agent/83-mcp.md#L231`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06063:end -->

<!-- books-review:SF-2026-ARXIV-2606-06079:start -->
<!-- existing:SF-2026-ARXIV-2606-06079:start -->Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。<!-- existing:SF-2026-ARXIV-2606-06079:end -->

<!-- delta:SF-2026-ARXIV-2606-06079:start -->Create/improve/merge operations and offline/online/hybrid modes make Agent skills evolvable lifecycle objects instead of one-shot prompt snippets.<!-- delta:SF-2026-ARXIV-2606-06079:end -->

实际读取 owner `books/part-07-agent/84-agent-platform.md#L639` 与相邻章节 `books/part-07-agent/83-mcp.md#L231`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06079:end -->

<!-- books-review:SF-2026-ARXIV-2606-06087:start -->
<!-- existing:SF-2026-ARXIV-2606-06087:start -->Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。<!-- existing:SF-2026-ARXIV-2606-06087:end -->

<!-- delta:SF-2026-ARXIV-2606-06087:start -->Moving skills from plaintext context into modular LoRA state changes updateability, composition, disclosure and provenance ownership even though the reported gains are task-bounded.<!-- delta:SF-2026-ARXIV-2606-06087:end -->

实际读取 owner `books/part-07-agent/84-agent-platform.md#L639` 与相邻章节 `books/part-07-agent/83-mcp.md#L231`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06087:end -->

<!-- books-review:SF-2026-ARXIV-2606-06090:start -->
<!-- existing:SF-2026-ARXIV-2606-06090:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-06090:end -->

<!-- delta:SF-2026-ARXIV-2606-06090:start -->Treating memory as workflow execution state assigns durable status, decisions and handoff ownership separately from semantic document organization.<!-- delta:SF-2026-ARXIV-2606-06090:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `Integrate`。该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06090:end -->

<!-- books-review:SF-2026-ARXIV-2606-06178:start -->
<!-- existing:SF-2026-ARXIV-2606-06178:start -->Decode 期间每个请求的 KV 持续增长，scheduler 的 admission 与 eviction 会反过来改变未来可用容量。若大量相似请求同步进入同一阶段，系统可能形成 admission、memory pressure、eviction、再 admission 的 limit cycle；因此 capacity controller 需要把 KV growth 作为动态 state，而不是只看当前 queue length。<!-- existing:SF-2026-ARXIV-2606-06178:end -->

<!-- delta:SF-2026-ARXIV-2606-06178:start -->User cost-performance preference becomes learned routing state that must adapt when the routable model set changes, altering model-selection control rather than adding one router score.<!-- delta:SF-2026-ARXIV-2606-06178:end -->

实际读取 owner `books/part-05-inference-system/56-inference-scheduling.md#L776` 与相邻章节 `books/part-05-inference-system/55-pd-disaggregation.md#L150 ; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L76`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06178:end -->

<!-- books-review:SF-2026-ARXIV-2606-06223:start -->
<!-- existing:SF-2026-ARXIV-2606-06223:start -->Monitoring 承接第 66 章对 Evaluation/Observability 的边界，为第 57 章 Evidence Plane 提供聚合 observed state，并向 evaluation sampling、autoscaling、admission、cost 与 incident response 提供输入。下一章转向离散事件：当指标告诉我们“出问题了”，Logging 如何留下可查询证据。<!-- existing:SF-2026-ARXIV-2606-06223:end -->

<!-- delta:SF-2026-ARXIV-2606-06223:start -->Reward-hack activation is only latent policy state; combining it with entropy and decision context changes the monitor-to-risk-state contract and prevents activation from being treated as an action verdict.<!-- delta:SF-2026-ARXIV-2606-06223:end -->

实际读取 owner `books/part-06-ai-infrastructure/67-monitoring.md#L268` 与相邻章节 `books/part-06-ai-infrastructure/66-evaluation-system.md#L2159 ; books/part-06-ai-infrastructure/68-logging.md#L70`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06223:end -->

<!-- books-review:SF-2026-ARXIV-2606-06240:start -->
<!-- existing:SF-2026-ARXIV-2606-06240:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-06240:end -->

<!-- delta:SF-2026-ARXIV-2606-06240:start -->Bitemporal valid-time and transaction-time operators define contradiction resolution and history semantics for persistent Agent memory.<!-- delta:SF-2026-ARXIV-2606-06240:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `Integrate`。该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06240:end -->

<!-- books-review:SF-2026-ARXIV-2606-06256:start -->
<!-- existing:SF-2026-ARXIV-2606-06256:start -->多轮 serving 可在同机异构模型间借用 idle HBM/NVLink 保存 hot prefix，但 cache identity、donor pressure 与回收优先级必须由控制面持有。借用 idle HBM 能降低 P99 TTFT，但 donor pressure 或跨模型 identity 错配会引起抖动/污染；回收阈值失效时回退本地 KV 与普通 eviction，不能宣称跨机收益。 coding-Agent KV workload 的 prefix reuse、branching 与长 idle gap 不同于聊天；cache manager 应按 repository<!-- existing:SF-2026-ARXIV-2606-06256:end -->

<!-- delta:SF-2026-ARXIV-2606-06256:start -->Head-aware reuse plus segmented paging changes long-context KV identity, page layout and execution rather than only model quality.<!-- delta:SF-2026-ARXIV-2606-06256:end -->

实际读取 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889` 与相邻章节 `books/part-05-inference-system/44-decode.md#L273 ; books/part-05-inference-system/46-continuous-batching.md#L251`。Decision: `Integrate`。该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06256:end -->

<!-- books-review:SF-2026-ARXIV-2606-06284:start -->
<!-- existing:SF-2026-ARXIV-2606-06284:start -->SF-2026-ARXIV-2606-23112**：Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning 的 exact-v1 机制为：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerab<!-- existing:SF-2026-ARXIV-2606-06284:end -->

<!-- delta:SF-2026-ARXIV-2606-06284:start -->Precondition-effect contracts expose only the causally sufficient next-step tool frontier, making tool-menu state a controlled runtime surface.<!-- delta:SF-2026-ARXIV-2606-06284:end -->

实际读取 owner `books/part-07-agent/78-tool-calling.md#L423` 与相邻章节 `books/part-07-agent/77-memory.md#L476 ; books/part-07-agent/79-planning.md#L163`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06284:end -->

<!-- books-review:SF-2026-ARXIV-2606-06302:start -->
<!-- existing:SF-2026-ARXIV-2606-06302:start -->多轮 serving 可在同机异构模型间借用 idle HBM/NVLink 保存 hot prefix，但 cache identity、donor pressure 与回收优先级必须由控制面持有。借用 idle HBM 能降低 P99 TTFT，但 donor pressure 或跨模型 identity 错配会引起抖动/污染；回收阈值失效时回退本地 KV 与普通 eviction，不能宣称跨机收益。 coding-Agent KV workload 的 prefix reuse、branching 与长 idle gap 不同于聊天；cache manager 应按 repository<!-- existing:SF-2026-ARXIV-2606-06302:end -->

<!-- delta:SF-2026-ARXIV-2606-06302:start -->Non-uniform layer/head KV compression changes multi-turn cache allocation and quality accounting at serving time.<!-- delta:SF-2026-ARXIV-2606-06302:end -->

实际读取 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L889` 与相邻章节 `books/part-05-inference-system/44-decode.md#L273 ; books/part-05-inference-system/46-continuous-batching.md#L251`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06302:end -->

<!-- books-review:SF-2026-ARXIV-2606-06324:start -->
<!-- existing:SF-2026-ARXIV-2606-06324:start -->Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。<!-- existing:SF-2026-ARXIV-2606-06324:end -->

<!-- delta:SF-2026-ARXIV-2606-06324:start -->Separating harness flaws from model failures changes diagnosis, lifecycle and repair ownership in Agent runtimes.<!-- delta:SF-2026-ARXIV-2606-06324:end -->

实际读取 owner `books/part-07-agent/84-agent-platform.md#L639` 与相邻章节 `books/part-07-agent/83-mcp.md#L231`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06324:end -->

<!-- books-review:SF-2026-ARXIV-2606-06337:start -->
<!-- existing:SF-2026-ARXIV-2606-06337:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-06337:end -->

<!-- delta:SF-2026-ARXIV-2606-06337:start -->A typed graph with supersession, invalidation, bitemporal validity and decision-transition evidence defines resumable session state beyond flat transcript summarization.<!-- delta:SF-2026-ARXIV-2606-06337:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06337:end -->

<!-- books-review:SF-2026-ARXIV-2606-06387:start -->
<!-- existing:SF-2026-ARXIV-2606-06387:start -->记录 server/tool/resource identity、latency、result size、policy decision、error/cancel，同时默认排除 credentials 和敏感 content。MCP 版本、capabilities 和 server trust level 也应进入 evidence。<!-- existing:SF-2026-ARXIV-2606-06387:end -->

<!-- delta:SF-2026-ARXIV-2606-06387:start -->Tool-surface poisoning at WebMCP discovery time changes protocol trust, runtime authorization and tool metadata admission.<!-- delta:SF-2026-ARXIV-2606-06387:end -->

实际读取 owner `books/part-07-agent/83-mcp.md#L227` 与相邻章节 `books/part-07-agent/82-multi-agent.md#L487 ; books/part-07-agent/84-agent-platform.md#L639`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06387:end -->

<!-- books-review:SF-2026-ARXIV-2606-06438:start -->
<!-- existing:SF-2026-ARXIV-2606-06438:start -->Cost 消费第 67～69 章 evidence，并反馈到 scheduler、autoscaling、model selection 和 lifecycle policy。下一章进入多租户：只有 identity 与 isolation 完整，成本归因和公平政策才可执行。<!-- existing:SF-2026-ARXIV-2606-06438:end -->

<!-- delta:SF-2026-ARXIV-2606-06438:start -->Combining workload, power, embodied carbon, scheduling and time-varying grid intensity changes hardware-refresh evaluation from operational efficiency to lifecycle cost.<!-- delta:SF-2026-ARXIV-2606-06438:end -->

实际读取 owner `books/part-06-ai-infrastructure/70-cost.md#L172` 与相邻章节 `books/part-06-ai-infrastructure/69-trace.md#L103 ; books/part-06-ai-infrastructure/71-multi-tenant.md#L67`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06438:end -->

<!-- books-review:SF-2026-ARXIV-2606-06448:start -->
<!-- existing:SF-2026-ARXIV-2606-06448:start -->只保存事实文本并在读取时做通用 embedding search，写入便宜、检索逻辑统一，但未来 query 可能使用与原文不同的描述或关联线索。更主动的 write path 在保存事实/fragment 时同时生成若干 descriptive 与 associative retrieval triggers，并将它们绑定到同一 provenance、version 和 supersession state；读取时 trigger 只负责扩大 proposal set，原始事实仍是权威内容。<!-- existing:SF-2026-ARXIV-2606-06448:end -->

<!-- delta:SF-2026-ARXIV-2606-06448:start -->Workload characterization ties long-lived Agent state to serving locality, memory pressure and request execution, changing platform capacity assumptions.<!-- delta:SF-2026-ARXIV-2606-06448:end -->

实际读取 owner `books/part-07-agent/77-memory.md#L1116` 与相邻章节 `books/part-07-agent/76-rag.md#L407 ; books/part-07-agent/78-tool-calling.md#L344`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06448:end -->

<!-- books-review:SF-2026-ARXIV-2606-06453:start -->
<!-- existing:SF-2026-ARXIV-2606-06453:start -->本轮 Review 补充了 internal/external fragmentation 的边界，并明确 PagedAttention 通过 KV capacity 间接影响吞吐。论文中的设计与当前 vLLM 实现不能视为完全同一版本；本章保留机制不变量，具体 block manager 与 kernel 行为应以目标版本文档和代码为准。<!-- existing:SF-2026-ARXIV-2606-06453:end -->

<!-- delta:SF-2026-ARXIV-2606-06453:start -->Programmable sparse-attention indexes and kernels change request-level serving state and execution for Agent workloads.<!-- delta:SF-2026-ARXIV-2606-06453:end -->

实际读取 owner `books/part-05-inference-system/47-pagedattention.md#L253` 与相邻章节 `books/part-05-inference-system/46-continuous-batching.md#L73 ; books/part-05-inference-system/48-speculative-decoding.md#L675`。Decision: `Integrate`。该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06453:end -->

<!-- books-review:SF-2026-ARXIV-2606-06460:start -->
<!-- existing:SF-2026-ARXIV-2606-06460:start -->模型生成的计划、代码或工具调用只是一份 proposal。要成为执行 authority，必须先编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity；airlock 负责验证 schema 和证据，broker 只授予完成该动作所需的短期能力。证书化增加 admission latency 与 TCB，证据陈旧、policy/validator drift 或 emergency bypass 都会破坏保证，因此既有 IAM、sandbox 和 effect-time au<!-- existing:SF-2026-ARXIV-2606-06460:end -->

<!-- delta:SF-2026-ARXIV-2606-06460:start -->Recusal at admission and stop mid-flight are distinct in-band governance events, changing credentialed Agent control semantics.<!-- delta:SF-2026-ARXIV-2606-06460:end -->

实际读取 owner `books/part-06-ai-infrastructure/72-security.md#L1020` 与相邻章节 `books/part-06-ai-infrastructure/71-multi-tenant.md#L80 ; books/part-06-ai-infrastructure/73-production-best-practice.md#L174`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06460:end -->

<!-- books-review:SF-2026-ARXIV-2606-06467:start -->
<!-- existing:SF-2026-ARXIV-2606-06467:start -->本轮 Review 补充了 internal/external fragmentation 的边界，并明确 PagedAttention 通过 KV capacity 间接影响吞吐。论文中的设计与当前 vLLM 实现不能视为完全同一版本；本章保留机制不变量，具体 block manager 与 kernel 行为应以目标版本文档和代码为准。<!-- existing:SF-2026-ARXIV-2606-06467:end -->

<!-- delta:SF-2026-ARXIV-2606-06467:start -->Sharing sparse-attention routing across layers removes repeated index construction and changes cross-layer access-state ownership.<!-- delta:SF-2026-ARXIV-2606-06467:end -->

实际读取 owner `books/part-05-inference-system/47-pagedattention.md#L253` 与相邻章节 `books/part-05-inference-system/46-continuous-batching.md#L73 ; books/part-05-inference-system/48-speculative-decoding.md#L675`。Decision: `No Change — Existing Coverage`。目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。 本 lane 不写 Books。
<!-- books-review:SF-2026-ARXIV-2606-06467:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260605-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260605 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260605: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260605-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-05241; review:SF-2026-ARXIV-2606-05271; review:SF-2026-ARXIV-2606-05304; review:SF-2026-ARXIV-2606-05308; review:SF-2026-ARXIV-2606-05339; review:SF-2026-ARXIV-2606-05378; review:SF-2026-ARXIV-2606-05384; review:SF-2026-ARXIV-2606-05391; review:SF-2026-ARXIV-2606-05395; review:SF-2026-ARXIV-2606-05396; review:SF-2026-ARXIV-2606-05403; review:SF-2026-ARXIV-2606-05414; review:SF-2026-ARXIV-2606-05415; review:SF-2026-ARXIV-2606-05433; review:SF-2026-ARXIV-2606-05495; review:SF-2026-ARXIV-2606-05523; review:SF-2026-ARXIV-2606-05548; review:SF-2026-ARXIV-2606-05551; review:SF-2026-ARXIV-2606-05558; review:SF-2026-ARXIV-2606-05559; review:SF-2026-ARXIV-2606-05568; review:SF-2026-ARXIV-2606-05597; review:SF-2026-ARXIV-2606-05606; review:SF-2026-ARXIV-2606-05610; review:SF-2026-ARXIV-2606-05646; review:SF-2026-ARXIV-2606-05662; review:SF-2026-ARXIV-2606-05679; review:SF-2026-ARXIV-2606-05688; review:SF-2026-ARXIV-2606-05711; review:SF-2026-ARXIV-2606-05725; review:SF-2026-ARXIV-2606-05742; review:SF-2026-ARXIV-2606-05743; review:SF-2026-ARXIV-2606-05787; review:SF-2026-ARXIV-2606-05800; review:SF-2026-ARXIV-2606-05805; review:SF-2026-ARXIV-2606-05828; review:SF-2026-ARXIV-2606-05868; review:SF-2026-ARXIV-2606-05872; review:SF-2026-ARXIV-2606-05875; review:SF-2026-ARXIV-2606-05894; review:SF-2026-ARXIV-2606-05933; review:SF-2026-ARXIV-2606-05946; review:SF-2026-ARXIV-2606-05951; review:SF-2026-ARXIV-2606-05958; review:SF-2026-ARXIV-2606-05976; review:SF-2026-ARXIV-2606-06032; review:SF-2026-ARXIV-2606-06036; review:SF-2026-ARXIV-2606-06044; review:SF-2026-ARXIV-2606-06054; review:SF-2026-ARXIV-2606-06055; review:SF-2026-ARXIV-2606-06063; review:SF-2026-ARXIV-2606-06079; review:SF-2026-ARXIV-2606-06087; review:SF-2026-ARXIV-2606-06090; review:SF-2026-ARXIV-2606-06178; review:SF-2026-ARXIV-2606-06223; review:SF-2026-ARXIV-2606-06240; review:SF-2026-ARXIV-2606-06256; review:SF-2026-ARXIV-2606-06284; review:SF-2026-ARXIV-2606-06302; review:SF-2026-ARXIV-2606-06324; review:SF-2026-ARXIV-2606-06337; review:SF-2026-ARXIV-2606-06387; review:SF-2026-ARXIV-2606-06438; review:SF-2026-ARXIV-2606-06448; review:SF-2026-ARXIV-2606-06453; review:SF-2026-ARXIV-2606-06460; review:SF-2026-ARXIV-2606-06467 | EVIDENCE-OWNER-REBUILD-20260605: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260605-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-05241; analysis-decision:SF-2026-ARXIV-2606-05271; analysis:DA-20260604-ACTION-STATE-COMMUNICATION; analysis-decision:SF-2026-ARXIV-2606-05308; analysis-decision:SF-2026-ARXIV-2606-05339; analysis-decision:SF-2026-ARXIV-2606-05378; analysis-decision:SF-2026-ARXIV-2606-05384; analysis-decision:SF-2026-ARXIV-2606-05391; analysis-decision:SF-2026-ARXIV-2606-05395; analysis-decision:SF-2026-ARXIV-2606-05396; analysis-decision:SF-2026-ARXIV-2606-05403; analysis-decision:SF-2026-ARXIV-2606-05414; analysis-decision:SF-2026-ARXIV-2606-05415; analysis-decision:SF-2026-ARXIV-2606-05433; analysis-decision:SF-2026-ARXIV-2606-05495; analysis-decision:SF-2026-ARXIV-2606-05523; analysis-decision:SF-2026-ARXIV-2606-05548; analysis-decision:SF-2026-ARXIV-2606-05551; analysis-decision:SF-2026-ARXIV-2606-05597; analysis-decision:SF-2026-ARXIV-2606-05610; analysis-decision:SF-2026-ARXIV-2606-05662; analysis:DA-20260605-AUTHORITY; analysis-decision:SF-2026-ARXIV-2606-05933; analysis-decision:SF-2026-ARXIV-2606-05946; analysis-decision:SF-2026-ARXIV-2606-05951; analysis-decision:SF-2026-ARXIV-2606-05976; analysis-decision:SF-2026-ARXIV-2606-06032; analysis-decision:SF-2026-ARXIV-2606-06044; analysis-decision:SF-2026-ARXIV-2606-06054; analysis-decision:SF-2026-ARXIV-2606-06055; analysis-decision:SF-2026-ARXIV-2606-06090; analysis:DA-20260605-STATE; analysis-decision:SF-2026-ARXIV-2606-06256; analysis-decision:SF-2026-ARXIV-2606-06284; analysis-decision:SF-2026-ARXIV-2606-06324; analysis-decision:SF-2026-ARXIV-2606-06387; analysis-decision:SF-2026-ARXIV-2606-06438; analysis-decision:SF-2026-ARXIV-2606-06448; analysis-decision:SF-2026-ARXIV-2606-06453; analysis-decision:SF-2026-ARXIV-2606-06460 | SELECTION-OWNER-REBUILD-20260605: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260605-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-05241; books-review:SF-2026-ARXIV-2606-05304; books-review:SF-2026-ARXIV-2606-05308; books-review:SF-2026-ARXIV-2606-05339; books-review:SF-2026-ARXIV-2606-05378; books-review:SF-2026-ARXIV-2606-05384; books-review:SF-2026-ARXIV-2606-05395; books-review:SF-2026-ARXIV-2606-05403; books-review:SF-2026-ARXIV-2606-05415; books-review:SF-2026-ARXIV-2606-05433; books-review:SF-2026-ARXIV-2606-05495; books-review:SF-2026-ARXIV-2606-05548; books-review:SF-2026-ARXIV-2606-05551; books-review:SF-2026-ARXIV-2606-05558; books-review:SF-2026-ARXIV-2606-05559; books-review:SF-2026-ARXIV-2606-05568; books-review:SF-2026-ARXIV-2606-05597; books-review:SF-2026-ARXIV-2606-05606; books-review:SF-2026-ARXIV-2606-05610; books-review:SF-2026-ARXIV-2606-05646; books-review:SF-2026-ARXIV-2606-05662; books-review:SF-2026-ARXIV-2606-05679; books-review:SF-2026-ARXIV-2606-05688; books-review:SF-2026-ARXIV-2606-05711; books-review:SF-2026-ARXIV-2606-05725; books-review:SF-2026-ARXIV-2606-05742; books-review:SF-2026-ARXIV-2606-05743; books-review:SF-2026-ARXIV-2606-05787; books-review:SF-2026-ARXIV-2606-05800; books-review:SF-2026-ARXIV-2606-05805; books-review:SF-2026-ARXIV-2606-05828; books-review:SF-2026-ARXIV-2606-05868; books-review:SF-2026-ARXIV-2606-05872; books-review:SF-2026-ARXIV-2606-05875; books-review:SF-2026-ARXIV-2606-05894; books-review:SF-2026-ARXIV-2606-05933; books-review:SF-2026-ARXIV-2606-05946; books-review:SF-2026-ARXIV-2606-05951; books-review:SF-2026-ARXIV-2606-05958; books-review:SF-2026-ARXIV-2606-05976; books-review:SF-2026-ARXIV-2606-06032; books-review:SF-2026-ARXIV-2606-06036; books-review:SF-2026-ARXIV-2606-06044; books-review:SF-2026-ARXIV-2606-06054; books-review:SF-2026-ARXIV-2606-06055; books-review:SF-2026-ARXIV-2606-06063; books-review:SF-2026-ARXIV-2606-06079; books-review:SF-2026-ARXIV-2606-06087; books-review:SF-2026-ARXIV-2606-06090; books-review:SF-2026-ARXIV-2606-06178; books-review:SF-2026-ARXIV-2606-06223; books-review:SF-2026-ARXIV-2606-06240; books-review:SF-2026-ARXIV-2606-06256; books-review:SF-2026-ARXIV-2606-06284; books-review:SF-2026-ARXIV-2606-06302; books-review:SF-2026-ARXIV-2606-06324; books-review:SF-2026-ARXIV-2606-06337; books-review:SF-2026-ARXIV-2606-06387; books-review:SF-2026-ARXIV-2606-06438; books-review:SF-2026-ARXIV-2606-06448; books-review:SF-2026-ARXIV-2606-06453; books-review:SF-2026-ARXIV-2606-06460; books-review:SF-2026-ARXIV-2606-06467 | BOOKS-OWNER-REBUILD-20260605: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

Ordinary review pending: `0`. Exact-v1 body re-opened: `64/64` (`38` local hash-verified bodies, `26` official arXiv exact-v1 HTML reads). Benchmark contracts: `60/60` reviewed field by field; `4` papers make no empirical benchmark claim. No blocked or unverified retained family remains.

## 9. Recommended Action

本日 Completion Status=Complete；没有独立的 legacy action section。后续动作只保留在已冻结的 Gate、Materials 和 source packet 中，不从展示迁移推导新的研究结论。

## 10. Repository Changes

 and Continuation

Root serialized eight `Integrate` proposals across Ch36, Ch45, Ch47, Ch56, Ch72 and Ch77. This fresh lane repaired the 2606.05679/05933/06256 benchmark false negatives, corrected the 2606.05679/05951 method locators, and re-audited all nine concrete Books locations without modifying Books. Coverage, Evidence, Selection and Books Gates are closed; unresolved findings are zero. Post-write receipt: `../_sources/daily-20260605/POST_WRITE_FRESH_AUDIT_V1.md`.

## 11. Open Questions

本日没有未解决的 ordinary pending；精确状态以 Gate metadata 与 Semantic Audit 为准。

## 12. Sources

- [Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation](https://arxiv.org/abs/2606.05241v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference](https://arxiv.org/abs/2606.05271v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference](https://arxiv.org/abs/2606.05308v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [A Taxonomy of Runtime Faults in Model Context Protocol Servers](https://arxiv.org/abs/2606.05339v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models](https://arxiv.org/abs/2606.05378v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges](https://arxiv.org/abs/2606.05384v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents](https://arxiv.org/abs/2606.05391v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents](https://arxiv.org/abs/2606.05395v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Willing but Unable: Separating Refusal from Capability in Code LLMs via Abliteration](https://arxiv.org/abs/2606.05396v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation](https://arxiv.org/abs/2606.05403v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories](https://arxiv.org/abs/2606.05414v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval](https://arxiv.org/abs/2606.05415v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Zero knowledge verification for frontier AI training is possible](https://arxiv.org/abs/2606.05433v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines](https://arxiv.org/abs/2606.05495v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [CHASE: Adversarial Red-Blue Teaming for Improving LLM Safety using Reinforcement Learning](https://arxiv.org/abs/2606.05523v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer](https://arxiv.org/abs/2606.05548v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Conformal Risk-Averse Decision Making with Action Conditional Guarantee](https://arxiv.org/abs/2606.05551v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](https://arxiv.org/abs/2606.05558v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [CLaaS: Continual learning as a service for sample efficient online learning](https://arxiv.org/abs/2606.05559v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [AsyncWebRL: Efficient Asynchronous Reinforcement Learning for Multi-Step Visual Web Agents](https://arxiv.org/abs/2606.05597v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Cross-Epoch Adaptive Rollout Optimization for RL Post-Training](https://arxiv.org/abs/2606.05606v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training](https://arxiv.org/abs/2606.05610v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Enhancing Software Engineering Through Closed-Loop Memory Optimization](https://arxiv.org/abs/2606.05646v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [QDAG: Declarative Composition of Reusable Analytics Methodologies at LinkedIn](https://arxiv.org/abs/2606.05662v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Data Flow Control: Data Safety Policies for AI Agents](https://arxiv.org/abs/2606.05679v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Value-and-Structure Alignment for Routing-Consistent Quantization of Mixture-of-Experts Models](https://arxiv.org/abs/2606.05688v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems](https://arxiv.org/abs/2606.05711v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic](https://arxiv.org/abs/2606.05725v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [AdaPLD: Adaptive Retrieval and Reuse for Efficient Model-Free Speculative Decoding](https://arxiv.org/abs/2606.05742v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense](https://arxiv.org/abs/2606.05743v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [SentinelRAG: Synthetic Sentinel Knowledge for RAG Database Copyright Protection](https://arxiv.org/abs/2606.05787v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [SALT: When More Rollouts Don't Help in Group-Based Policy Optimization and How to Make Them Matter](https://arxiv.org/abs/2606.05800v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents](https://arxiv.org/abs/2606.05805v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](https://arxiv.org/abs/2606.05828v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](https://arxiv.org/abs/2606.05868v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Entropy-Based Observability for AI Agent Behavior](https://arxiv.org/abs/2606.05872v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents](https://arxiv.org/abs/2606.05894v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference](https://arxiv.org/abs/2606.05933v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Short paper: Models in the dark -- Rectification and erasure under GDPR in ML supply chains](https://arxiv.org/abs/2606.05946v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication](https://arxiv.org/abs/2606.05951v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models](https://arxiv.org/abs/2606.05976v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Catastrophic Forgetting as Accessibility Collapse: A Three-Level Framework for Knowledge Persistence in Continual Learning](https://arxiv.org/abs/2606.06032v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents](https://arxiv.org/abs/2606.06036v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval](https://arxiv.org/abs/2606.06044v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Beyond Similarity: Trustworthy Memory Search for Personal AI Agents](https://arxiv.org/abs/2606.06054v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [HUSH-Bench: Measuring Memory-Use Boundaries for Sensitive History in Conversational Agents](https://arxiv.org/abs/2606.06055v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [LLM-Based Porting of Optimized C++ to CUDA Through Deoptimization and Reoptimization](https://arxiv.org/abs/2606.06063v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [SkillComposer: Learning to Evolve Agent Skills for Specification and Generalization](https://arxiv.org/abs/2606.06079v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents](https://arxiv.org/abs/2606.06087v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents](https://arxiv.org/abs/2606.06090v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning](https://arxiv.org/abs/2606.06178v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents](https://arxiv.org/abs/2606.06223v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory](https://arxiv.org/abs/2606.06240v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention](https://arxiv.org/abs/2606.06256v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents](https://arxiv.org/abs/2606.06284v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving](https://arxiv.org/abs/2606.06302v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management](https://arxiv.org/abs/2606.06337v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents](https://arxiv.org/abs/2606.06387v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [CarbonSim: A Lifecycle-Aware Framework for Evaluating Carbon Tradeoffs in Hardware Upgrade Decisions](https://arxiv.org/abs/2606.06438v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight](https://arxiv.org/abs/2606.06460v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
- [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467v1) — first-public（Asia/Shanghai）：2026-06-05；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
