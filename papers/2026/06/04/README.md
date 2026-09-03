# Daily Research — 2026-06-04

**Research Date:** 2026-06-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-03 09:00:00 ～ 2026-06-04 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
The canonical denominator is `42` retained and `532` family-specific pre-denominator closures (`7.32%`). A fresh reviewer re-opened all `42/42` exact-v1 bodies locally (`40` HTML, `2` PDF), corrected false negative disclosures and inaccurate locators, and checked every Source Review and full-frontier selection rationale. Books Comparison is restricted to the `30` Books-eligible families; the `12` `Weekly Only — Context` families remain fully reviewed candidate-level closures and deliberately have no Books Review Ref. Root then wrote only `2606.04929` to Ch72 and `2606.05304` to Ch82. Post-write review confirms their evidence boundaries, old-solution coexistence, owner handoffs and current hashes. A later concurrent Ch81 update changed its file hash but preserved Workflow's commit/approval authority; current adjacent hashes and semantics were rechecked. Pending, blocked and unverified are zero; all Gates pass.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-04 |
| Window End | 2026-06-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260604-V12-42 |
| Denominator Frozen At | 2026-08-29T12:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-03T09:00:00+08:00 | 2026-06-04T09:00:00+08:00 | 2026-08-29T12:00:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 575 | SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY;SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT;SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS;SF-ULTRAEP;SF-PROOF-CARRYING-ACTIONS;SF-EVALSTOP;SF-RECEIVER-ATTESTED-AGENT-RECEIPTS;SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR;SF-ROBOT-BENCHMARK-AUDIT;SF-AGENT-DATA-CURATION-HARNESS;SF-RL-EXCURSIONS-PRETRAINING;SF-INTERVENTION-TIMING-RELIABILITY;SF-LAZYATTENTION;SF-OCL-EXECUTION-BOUNDARY;SF-AGENT-MEMORY-GENERALITY;SF-DIGITAL-APPRENTICE-CONTROL-PLANE;SF-2026-ARXIV-2606-04329;SF-2026-ARXIV-2606-04384;SF-2026-ARXIV-2606-04402;SF-2026-ARXIV-2606-04413;SF-2026-ARXIV-2606-04415;SF-2026-ARXIV-2606-04425;SF-2026-ARXIV-2606-04459;SF-2026-ARXIV-2606-04522;SF-2026-ARXIV-2606-04557;SF-2026-ARXIV-2606-04581;SF-2026-ARXIV-2606-04594;SF-2026-ARXIV-2606-04628;SF-2026-ARXIV-2606-04769;SF-2026-ARXIV-2606-04778;SF-2026-ARXIV-2606-04799;SF-2026-ARXIV-2606-04850;SF-2026-ARXIV-2606-04903;SF-2026-ARXIV-2606-04908;SF-2026-ARXIV-2606-04923;SF-2026-ARXIV-2606-04929;SF-2026-ARXIV-2606-05004;SF-2026-ARXIV-2606-05029;SF-2026-ARXIV-2606-05037;SF-2026-ARXIV-2606-05043;SF-2026-ARXIV-2606-05122 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260604/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260604; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260604 |
<!-- coverage:SRC-ARXIV:20260604:start -->Root accepted the mutually exclusive `42 + 532 = 574` V12 ledger after a complete false-positive/false-negative review. This downstream lane does not reopen that denominator.<!-- coverage:SRC-ARXIV:20260604:end -->


<!-- latest-contract-reopen:2026-06-04:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-04:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **575** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **41** 条是旧报告 retained provenance，**534** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | arXiv:2606.04017v1 | paper-v1:2606.04017 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | no |
| SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | arXiv:2606.04056v1 | paper-v1:2606.04056 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | yes |
| SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | arXiv:2606.04071v1 | paper-v1:2606.04071 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | yes |
| SF-ULTRAEP | arXiv:2606.04101v1 | paper-v1:2606.04101 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-ULTRAEP | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-ULTRAEP | yes |
| SF-PROOF-CARRYING-ACTIONS | arXiv:2606.04104v1 | paper-v1:2606.04104 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-PROOF-CARRYING-ACTIONS | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-PROOF-CARRYING-ACTIONS | yes |
| SF-EVALSTOP | arXiv:2606.04145v1 | paper-v1:2606.04145 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-EVALSTOP | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-EVALSTOP | yes |
| SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | arXiv:2606.04193v1 | paper-v1:2606.04193 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | yes |
| SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | arXiv:2606.04196v1 | paper-v1:2606.04196 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | yes |
| SF-ROBOT-BENCHMARK-AUDIT | arXiv:2606.04233v1 | paper-v1:2606.04233 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-ROBOT-BENCHMARK-AUDIT | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-ROBOT-BENCHMARK-AUDIT | yes |
| SF-AGENT-DATA-CURATION-HARNESS | arXiv:2606.04261v1 | paper-v1:2606.04261 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-AGENT-DATA-CURATION-HARNESS | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-AGENT-DATA-CURATION-HARNESS | yes |
| SF-RL-EXCURSIONS-PRETRAINING | arXiv:2606.04272v1 | paper-v1:2606.04272 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-RL-EXCURSIONS-PRETRAINING | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-RL-EXCURSIONS-PRETRAINING | yes |
| SF-INTERVENTION-TIMING-RELIABILITY | arXiv:2606.04296v1 | paper-v1:2606.04296 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-INTERVENTION-TIMING-RELIABILITY | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-INTERVENTION-TIMING-RELIABILITY | yes |
| SF-LAZYATTENTION | arXiv:2606.04302v1 | paper-v1:2606.04302 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-LAZYATTENTION | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-LAZYATTENTION | yes |
| SF-OCL-EXECUTION-BOUNDARY | arXiv:2606.04306v1 | paper-v1:2606.04306 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-OCL-EXECUTION-BOUNDARY | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-OCL-EXECUTION-BOUNDARY | yes |
| SF-AGENT-MEMORY-GENERALITY | arXiv:2606.04315v1 | paper-v1:2606.04315 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-AGENT-MEMORY-GENERALITY | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-AGENT-MEMORY-GENERALITY | yes |
| SF-DIGITAL-APPRENTICE-CONTROL-PLANE | arXiv:2606.04321v1 | paper-v1:2606.04321 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE | yes |
| SF-2026-ARXIV-2606-04329 | arXiv:2606.04329v1 | paper-v1:2606.04329 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04329 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04329 | yes |
| SF-2026-ARXIV-2606-04384 | arXiv:2606.04384v1 | paper-v1:2606.04384 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04384 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04384 | yes |
| SF-2026-ARXIV-2606-04402 | arXiv:2606.04402v1 | paper-v1:2606.04402 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04402 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04413 | arXiv:2606.04413v1 | paper-v1:2606.04413 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04413 | self | — | new_in_window | TRAIN-SFT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04415 | arXiv:2606.04415v1 | paper-v1:2606.04415 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04415 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04415 | yes |
| SF-2026-ARXIV-2606-04425 | arXiv:2606.04425v1 | paper-v1:2606.04425 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04425 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04425 | yes |
| SF-2026-ARXIV-2606-04459 | arXiv:2606.04459v1 | paper-v1:2606.04459 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04459 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04522 | arXiv:2606.04522v1 | paper-v1:2606.04522 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04522 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04522 | yes |
| SF-2026-ARXIV-2606-04557 | arXiv:2606.04557v1 | paper-v1:2606.04557 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04557 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04557 | yes |
| SF-2026-ARXIV-2606-04581 | arXiv:2606.04581v1 | paper-v1:2606.04581 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04581 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04581 | yes |
| SF-2026-ARXIV-2606-04594 | arXiv:2606.04594v1 | paper-v1:2606.04594 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04594 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04594 | yes |
| SF-2026-ARXIV-2606-04628 | arXiv:2606.04628v1 | paper-v1:2606.04628 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04628 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04628 | yes |
| SF-2026-ARXIV-2606-04769 | arXiv:2606.04769v1 | paper-v1:2606.04769 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04769 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04769 | yes |
| SF-2026-ARXIV-2606-04778 | arXiv:2606.04778v1 | paper-v1:2606.04778 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04778 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04778 | yes |
| SF-2026-ARXIV-2606-04799 | arXiv:2606.04799v1 | paper-v1:2606.04799 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04799 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04799 | yes |
| SF-2026-ARXIV-2606-04850 | arXiv:2606.04850v1 | paper-v1:2606.04850 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04850 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04903 | arXiv:2606.04903v1 | paper-v1:2606.04903 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04903 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04908 | arXiv:2606.04908v1 | paper-v1:2606.04908 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04908 | self | — | new_in_window | INFER-GPU-MEMORY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04923 | arXiv:2606.04923v1 | paper-v1:2606.04923 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04923 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04923 | yes |
| SF-2026-ARXIV-2606-04929 | arXiv:2606.04929v1 | paper-v1:2606.04929 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04929 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-04929 | yes |
| SF-2026-ARXIV-2606-05004 | arXiv:2606.05004v1 | paper-v1:2606.05004 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05004 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05029 | arXiv:2606.05029v1 | paper-v1:2606.05029 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05029 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05029 | yes |
| SF-2026-ARXIV-2606-05037 | arXiv:2606.05037v1 | paper-v1:2606.05037 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05037 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05037 | yes |
| SF-2026-ARXIV-2606-05043 | arXiv:2606.05043v1 | paper-v1:2606.05043 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05043 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05043 | yes |
| SF-2026-ARXIV-2606-05122 | arXiv:2606.05122v1 | paper-v1:2606.05122 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05122 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05122 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | RP-afa43ff1dd184afe | deep | arXiv:2606.04017v1 | SRC-ARXIV@arXiv:2606.04017v1 | arXiv:2606.04017v1 exact-v1 HTML § `2 Agent Epistemic Integrity: A Framework` | Not Disclosed — arXiv:2606.04017v1 exact-v1 HTML has no separately identifiable empirical evaluation section | arXiv:2606.04017v1 exact-v1 HTML § `7 Conclusion and Next Steps` — no dedicated limitations heading; the cited closing section was read and the Daily claim boundary records the source-specific non-result | Not Disclosed — arXiv:2606.04017v1 exact-v1 HTML does not pin an immutable implementation revision | claim:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | complete |
| SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | RP-d8fa23f852910446 | deep | arXiv:2606.04056v1 | SRC-ARXIV@arXiv:2606.04056v1 | arXiv:2606.04056v1 Methodology: II-A Methodology | arXiv:2606.04056v1 Experiments: III The mitigation: an affine Budget (case study) | arXiv:2606.04056v1 Scope and Limitations: IV-C 4 Threats to validity for this experiment | https://github.com/flyersworder/agent-contracts | claim:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | complete |
| SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | RP-ee218c51683490a3 | deep | arXiv:2606.04071v1 | SRC-ARXIV@arXiv:2606.04071v1 | arXiv:2606.04071v1 Methodology: arXiv:2606.04071v1 §3–4 Threat Model and Method | arXiv:2606.04071v1 Experiments: arXiv:2606.04071v1 §5–6 Experiments | arXiv:2606.04071v1 Scope and Limitations: arXiv:2606.04071v1 §7 Limitations and production-prevalence boundary | Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision. | claim:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | complete |
| SF-ULTRAEP | RP-97cf7134c8dd3122 | deep | arXiv:2606.04101v1 | SRC-ARXIV@arXiv:2606.04101v1 | arXiv:2606.04101v1 Methodology: https://arxiv.org/abs/2606.04101v1 — Abstract ¶2–3; exact-load planning and expert-state transfer | arXiv:2606.04101v1 Experiments: https://arxiv.org/abs/2606.04101v1 — Abstract ¶4–5; 106B–671B training/prefill and 2560-GPU validation | arXiv:2606.04101v1 Scope and Limitations: https://arxiv.org/abs/2606.04101v1 — Abstract scope; submission-history removal boundary | Not Disclosed — exact-v1 official abstract names no event-time artifact; later GitHub repository excluded | claim:SF-ULTRAEP | complete |
| SF-PROOF-CARRYING-ACTIONS | RP-741ecbf21e10ccee | deep | arXiv:2606.04104v1 | SRC-ARXIV@arXiv:2606.04104v1 | arXiv:2606.04104v1 §4.3 Research objective | arXiv:2606.04104v1 §7.2 Authorization, workflow, and evaluation context | arXiv:2606.04104v1 §8.6 Dual-lane and future-lane integrity | Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay | claim:SF-PROOF-CARRYING-ACTIONS | complete |
| SF-EVALSTOP | RP-d648bbadb6f1568e | deep | arXiv:2606.04145v1 | SRC-ARXIV@arXiv:2606.04145v1 | arXiv:2606.04145v1 Methodology: No dedicated Method heading; mechanism located in 3 EvalStop: World-Feedback-Driven Early Stopping | arXiv:2606.04145v1 §4 Experiments | arXiv:2606.04145v1 §5 Discussion | Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay | claim:SF-EVALSTOP | complete |
| SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | RP-eccec789ece37804 | deep | arXiv:2606.04193v1 | SRC-ARXIV@arXiv:2606.04193v1 | arXiv:2606.04193v1 §4.1 Receipt structure | arXiv:2606.04193v1 §7 Evaluation | arXiv:2606.04193v1 §3.1 System model | https://github.com/Prismer-AI/signet | claim:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | complete |
| SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | RP-dd7e7f9741453c83 | deep | arXiv:2606.04196v1 | SRC-ARXIV@arXiv:2606.04196v1 | arXiv:2606.04196v1 Methodology: arXiv:2606.04196v1 §3–4 Index Format and System Integration | arXiv:2606.04196v1 Experiments: arXiv:2606.04196v1 §5 Evaluation | arXiv:2606.04196v1 Scope and Limitations: arXiv:2606.04196v1 §6 Discussion and evaluation boundary | Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision. | claim:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | complete |
| SF-ROBOT-BENCHMARK-AUDIT | RP-703a4200aa1bafdd | deep | arXiv:2606.04233v1 | SRC-ARXIV@arXiv:2606.04233v1 | arXiv:2606.04233v1 Appendix D Citation Tracker Methodology | arXiv:2606.04233v1 Appendix A Experiment Details | arXiv:2606.04233v1 §7 Discussion | Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay | claim:SF-ROBOT-BENCHMARK-AUDIT | complete |
| SF-AGENT-DATA-CURATION-HARNESS | RP-3cb996346a2d279f | deep | arXiv:2606.04261v1 | SRC-ARXIV@arXiv:2606.04261v1 | arXiv:2606.04261v1 Methodology: LLMs as tools inside the pipeline. | arXiv:2606.04261v1 Experiments: B.5 Evaluation | arXiv:2606.04261v1 §6 Conclusion | https://github.com/feiyang-k/curation-bench | claim:SF-AGENT-DATA-CURATION-HARNESS | complete |
| SF-RL-EXCURSIONS-PRETRAINING | RP-1b6b145d0bf5a42b | deep | arXiv:2606.04272v1 | SRC-ARXIV@arXiv:2606.04272v1 | arXiv:2606.04272v1 §3.1 RLVR competes with the standard pipeline on GSM8K | arXiv:2606.04272v1 §2 Methodology and Experimental Design | arXiv:2606.04272v1 §7 Discussion & Future Directions | Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay | claim:SF-RL-EXCURSIONS-PRETRAINING | complete |
| SF-INTERVENTION-TIMING-RELIABILITY | RP-365dac3fe9ac5a0d | deep | arXiv:2606.04296v1 | SRC-ARXIV@arXiv:2606.04296v1 | arXiv:2606.04296v1 §3 The Diagnostic Probe and the Three-Layer Architecture | arXiv:2606.04296v1 Experiments: No dedicated Evaluation heading; evidence located in Reproducibility | arXiv:2606.04296v1 §9 Limitations | Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay | claim:SF-INTERVENTION-TIMING-RELIABILITY | complete |
| SF-LAZYATTENTION | RP-537ac86cd0df912f | deep | arXiv:2606.04302v1 | SRC-ARXIV@arXiv:2606.04302v1 | arXiv:2606.04302v1 §3 LazyAttention : Algorithm and Analysis | arXiv:2606.04302v1 §4 Evaluation | arXiv:2606.04302v1 Scope and Limitations: Hit-ratio impact under limited cache capacity | https://github.com/LMCache/LMCache | claim:SF-LAZYATTENTION | complete |
| SF-OCL-EXECUTION-BOUNDARY | RP-cb0bc9e40aa02a58 | deep | arXiv:2606.04306v1 | SRC-ARXIV@arXiv:2606.04306v1 | arXiv:2606.04306v1 §3 Methodology | arXiv:2606.04306v1 Experiments: Real-World Corpus Foundation. | arXiv:2606.04306v1 Scope and Limitations: High Task Success and Threat Interception. | https://github.com/SHITIANYU-hue/amai_ocl | claim:SF-OCL-EXECUTION-BOUNDARY | complete |
| SF-AGENT-MEMORY-GENERALITY | RP-cd4bf35b93281c87 | deep | arXiv:2606.04315v1 | SRC-ARXIV@arXiv:2606.04315v1 | arXiv:2606.04315v1 Methodology: General algorithm. | arXiv:2606.04315v1 §3 Evaluation Design | arXiv:2606.04315v1 §6 Conclusion | https://github.com/mem0ai/mem0 | claim:SF-AGENT-MEMORY-GENERALITY | complete |
| SF-DIGITAL-APPRENTICE-CONTROL-PLANE | RP-75b278917fb25cf2 | deep | arXiv:2606.04321v1 | SRC-ARXIV@arXiv:2606.04321v1 | arXiv:2606.04321v1 §2 graduated-autonomy state machine; §3 ADAPT control plane | arXiv:2606.04321v1 §5 proof-of-concept | arXiv:2606.04321v1 §6 limitations and risks; single professional-corpus proof-of-concept boundary | Not Disclosed — exact-v1 body does not bind an immutable revision | claim:SF-DIGITAL-APPRENTICE-CONTROL-PLANE | complete |
| SF-2026-ARXIV-2606-04329 | RP-625125acf31ef58f | deep | arXiv:2606.04329v1 | SRC-ARXIV@arXiv:2606.04329v1 | https://arxiv.org/html/2606.04329v1 §3 Memory Poisoning Attack Taxonomy; §3.1 Threat Model; Appendix A exploitation path | https://arxiv.org/html/2606.04329v1 §4 Evaluation; §4.1 MPBench Design | https://arxiv.org/html/2606.04329v1 §4.5 Limitations of Prompt Injection Defense against Memory Poisoning; §5 Discussions | Not Disclosed — exact-v1 cites HERMES as an evaluated target but does not identify it as this paper's versioned artifact | claim:SF-2026-ARXIV-2606-04329 | complete |
| SF-2026-ARXIV-2606-04384 | RP-7e9d9f675fa469ff | deep | arXiv:2606.04384v1 | SRC-ARXIV@arXiv:2606.04384v1 | https://arxiv.org/html/2606.04384v1 §4. METHODOLOGY; §4.1 DP Training Framework with Selective Release Based on Clipping Gradients | https://arxiv.org/html/2606.04384v1 §5. EXPERIMENT; §§5.1–5.2 | https://arxiv.org/html/2606.04384v1 §3.3 Limitations in the Privacy Accounting of DPSUR; §7. Discussion | https://github.com/FangXieLab/DPSR-CB — repository disclosed; exact-v1 does not pin an immutable event-time commit | claim:SF-2026-ARXIV-2606-04384 | complete |
| SF-2026-ARXIV-2606-04402 | RP-e99f24a973a758e4 | deep | arXiv:2606.04402v1 | SRC-ARXIV@arXiv:2606.04402v1 | https://arxiv.org/html/2606.04402v1 §3 Consequence-aware allocation; §§5–6 algorithm and guarantees | https://arxiv.org/html/2606.04402v1 §7 Experiments | https://arxiv.org/html/2606.04402v1 §9 Discussion and Limitations | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04402 | complete |
| SF-2026-ARXIV-2606-04413 | RP-d871d77eac5b609b | deep | arXiv:2606.04413v1 | SRC-ARXIV@arXiv:2606.04413v1 | https://arxiv.org/html/2606.04413v1 §§3–6 helpful-only training branches and constitution/SDF interventions | https://arxiv.org/html/2606.04413v1 §2 Evaluation Suite; §§4–6 results; Appendix A | https://arxiv.org/html/2606.04413v1 §8.1 Limitations; §§4–6 failure analyses | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04413 | complete |
| SF-2026-ARXIV-2606-04415 | RP-4f97aa954f482802 | deep | arXiv:2606.04415v1 | SRC-ARXIV@arXiv:2606.04415v1 | https://arxiv.org/pdf/2606.04415v1 §3 FlexNPU architecture and phase-level virtualization | https://arxiv.org/pdf/2606.04415v1 §4.1 Experimental Setup; §4.2 End-to-end Results; Table 2 | https://arxiv.org/pdf/2606.04415v1 §5 Discussion and disclosed prototype boundary | Not Disclosed — exact-v1 PDF does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04415 | complete |
| SF-2026-ARXIV-2606-04425 | RP-ed27f099ffcfdf78 | deep | arXiv:2606.04425v1 | SRC-ARXIV@arXiv:2606.04425v1 | https://arxiv.org/html/2606.04425v1 §4 Taxonomy of Stored Prompt Injection; §§4.1–4.4; §§3.1–3.2 system/threat model | https://arxiv.org/html/2606.04425v1 §5 Experiments; §§5.1–5.7 | https://arxiv.org/html/2606.04425v1 §Limitations; §5.7 Discussion | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-04425 | complete |
| SF-2026-ARXIV-2606-04459 | RP-84824b1f5f97e7fa | deep | arXiv:2606.04459v1 | SRC-ARXIV@arXiv:2606.04459v1 | https://arxiv.org/pdf/2606.04459v1 §§3–4 ranking-signature geometry and recovery method | https://arxiv.org/pdf/2606.04459v1 §4 practical fitting (50 rankings; 3/5 attempts); §5 approximate parameter exposure | https://arxiv.org/pdf/2606.04459v1 §6 Discussion and attack-scope boundary | Not Disclosed — exact-v1 PDF does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04459 | complete |
| SF-2026-ARXIV-2606-04522 | RP-8a96a9ed023db257 | deep | arXiv:2606.04522v1 | SRC-ARXIV@arXiv:2606.04522v1 | https://arxiv.org/html/2606.04522v1 §§3.2–3.3 Accuracy Measures and Downstream Task Evaluation Metrics | https://arxiv.org/html/2606.04522v1 §§5–6 Experimental Setup and Results; §6.3 RAG Experiments | https://arxiv.org/html/2606.04522v1 §7 Conclusions — reviewed for scope; no dedicated limitations heading | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-04522 | complete |
| SF-2026-ARXIV-2606-04557 | RP-fc66c7f30d2fcea9 | deep | arXiv:2606.04557v1 | SRC-ARXIV@arXiv:2606.04557v1 | https://arxiv.org/html/2606.04557v1 §2 Modular cartridge training and composition | https://arxiv.org/html/2606.04557v1 §3 Experimental Setup; §4 Experimental Results | https://arxiv.org/html/2606.04557v1 §5 Discussion; Limitations | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04557 | complete |
| SF-2026-ARXIV-2606-04581 | RP-f2770bb3c6912e7d | deep | arXiv:2606.04581v1 | SRC-ARXIV@arXiv:2606.04581v1 | https://arxiv.org/html/2606.04581v1 §III Protocol and Problem Formulation; §§IV–V distributed control | https://arxiv.org/html/2606.04581v1 §VI Experimental Results; §VI-A Experiment Settings | https://arxiv.org/html/2606.04581v1 §VII Concluding Remarks — no dedicated limitations section | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04581 | complete |
| SF-2026-ARXIV-2606-04594 | RP-39d0b68e1e93965f | deep | arXiv:2606.04594v1 | SRC-ARXIV@arXiv:2606.04594v1 | https://arxiv.org/html/2606.04594v1 §3 Ekka design; §4 Implementation | https://arxiv.org/html/2606.04594v1 §5 Evaluation; §§5.1–5.7 | https://arxiv.org/html/2606.04594v1 §7 Discussion | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04594 | complete |
| SF-2026-ARXIV-2606-04628 | RP-b2a92304130977a1 | deep | arXiv:2606.04628v1 | SRC-ARXIV@arXiv:2606.04628v1 | https://arxiv.org/html/2606.04628v1 §2 RAMPART model and registry operations | https://arxiv.org/html/2606.04628v1 §3 Experiments; §§3.1–3.2 | https://arxiv.org/html/2606.04628v1 §6 Conclusion — no dedicated limitations section | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04628 | complete |
| SF-2026-ARXIV-2606-04769 | RP-b4681816fbf20fa1 | deep | arXiv:2606.04769v1 | SRC-ARXIV@arXiv:2606.04769v1 | https://arxiv.org/html/2606.04769v1 §IV DCIChecker; §IV-B Structure-Aware Tool Semantic Extraction; §IV-C DCI Checking with DRA-Prompting | https://arxiv.org/html/2606.04769v1 §V Real-world Measurement; §§V-A–V-D | https://arxiv.org/html/2606.04769v1 §VII Discussion — Limitations and scope | Not Disclosed — exact-v1 does not identify a versioned public DCIChecker artifact | claim:SF-2026-ARXIV-2606-04769 | complete |
| SF-2026-ARXIV-2606-04778 | RP-8d89848d57ad1e67 | deep | arXiv:2606.04778v1 | SRC-ARXIV@arXiv:2606.04778v1 | https://arxiv.org/html/2606.04778v1 §3 trajectory-level alignment method; Appendix A | https://arxiv.org/html/2606.04778v1 §4 Experiments and Analysis | https://arxiv.org/html/2606.04778v1 Appendix E Limitation and Broader Impact | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04778 | complete |
| SF-2026-ARXIV-2606-04799 | RP-602aa52c7d916b96 | deep | arXiv:2606.04799v1 | SRC-ARXIV@arXiv:2606.04799v1 | https://arxiv.org/html/2606.04799v1 §III Agent-Ready Data Model | https://arxiv.org/html/2606.04799v1 §VI Evaluation | https://arxiv.org/html/2606.04799v1 §VIII Conclusion | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-04799 | complete |
| SF-2026-ARXIV-2606-04850 | RP-2541c85c465a6d96 | deep | arXiv:2606.04850v1 | SRC-ARXIV@arXiv:2606.04850v1 | https://arxiv.org/html/2606.04850v1 §III Model for Co-design with Distributional Uncertainty; §IV MDPI Model; §§IV-A–IV-D | https://arxiv.org/html/2606.04850v1 §V Simulation Results; §§V-A–V-C | https://arxiv.org/html/2606.04850v1 §VI Conclusion; §VI-A Outlook — no dedicated limitations section | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04850 | complete |
| SF-2026-ARXIV-2606-04903 | RP-f9b5d3ce8bc705ff | deep | arXiv:2606.04903v1 | SRC-ARXIV@arXiv:2606.04903v1 | https://arxiv.org/html/2606.04903v1 §1.4 Methodology; §1.4.3 Ontology-First Agent Design | https://arxiv.org/html/2606.04903v1 §2.3 Derivation of System Invariants; Appendix A.3.2 Preservation of Base Results | https://arxiv.org/html/2606.04903v1 §1.2 Threat Model (What is Safety) — In scope / Out of scope; §5 Conclusion and Future Work | https://github.com/Thistleseeds/agentic-redux — repository disclosed; exact-v1 does not pin an immutable event-time commit | claim:SF-2026-ARXIV-2606-04903 | complete |
| SF-2026-ARXIV-2606-04908 | RP-b3584d3ed02e5081 | deep | arXiv:2606.04908v1 | SRC-ARXIV@arXiv:2606.04908v1 | https://arxiv.org/html/2606.04908v1 §4. Design and Implementation | https://arxiv.org/html/2606.04908v1 §5. Evaluation; §5.1 Experimental Setup | https://arxiv.org/html/2606.04908v1 §6. Related Work and Discussion; §7. Conclusion | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-04908 | complete |
| SF-2026-ARXIV-2606-04923 | RP-2ad14ea10372ea0f | deep | arXiv:2606.04923v1 | SRC-ARXIV@arXiv:2606.04923v1 | https://arxiv.org/html/2606.04923v1 §2 CHERRL; §§2.2–2.5; §4.1 Agentic Detector Design | https://arxiv.org/html/2606.04923v1 §2.5; §4.2; Appendices B, D and F | https://arxiv.org/html/2606.04923v1 Limitations; Appendix B.8 | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-04923 | complete |
| SF-2026-ARXIV-2606-04929 | RP-07944199bda63e0d | deep | arXiv:2606.04929v1 | SRC-ARXIV@arXiv:2606.04929v1 | https://arxiv.org/html/2606.04929v1 §5 Sequential Data Poisoning; §§5.1–5.3 | https://arxiv.org/html/2606.04929v1 §4 Experimental Setup; Appendix D.2 Evaluation Details; Appendix E | https://arxiv.org/html/2606.04929v1 §6 Conclusion — Limitations and future work | Not Disclosed — exact-v1 does not identify one versioned public attack artifact | claim:SF-2026-ARXIV-2606-04929 | complete |
| SF-2026-ARXIV-2606-05004 | RP-12e2157de6189575 | deep | arXiv:2606.05004v1 | SRC-ARXIV@arXiv:2606.05004v1 | https://arxiv.org/html/2606.05004v1 §4 Framework; §5 Privacy Analysis | https://arxiv.org/html/2606.05004v1 §7 Experiment; Appendix G Experiment; §5 Privacy Analysis for the formal claim | https://arxiv.org/html/2606.05004v1 Limitation — dedicated heading after §8 Conclusion | Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision | claim:SF-2026-ARXIV-2606-05004 | complete |
| SF-2026-ARXIV-2606-05029 | RP-999c38cc6bdd57ed | deep | arXiv:2606.05029v1 | SRC-ARXIV@arXiv:2606.05029v1 | https://arxiv.org/html/2606.05029v1 §3 The Proxy Approach | https://arxiv.org/html/2606.05029v1 §6 Validity Profiles for Foundation Model Research | https://arxiv.org/html/2606.05029v1 §8 Discussion | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-05029 | complete |
| SF-2026-ARXIV-2606-05037 | RP-7f8043249efe3eba | deep | arXiv:2606.05037v1 | SRC-ARXIV@arXiv:2606.05037v1 | https://arxiv.org/html/2606.05037v1 §3 Design: Self-Reflective API Framework; §4 Implementation | https://arxiv.org/html/2606.05037v1 §5 Evaluation; §§5.1–5.4 | https://arxiv.org/html/2606.05037v1 §5.5 Limitations and Threats to Validity; §6.2 Failure/Saturation cases | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-05037 | complete |
| SF-2026-ARXIV-2606-05043 | RP-bfadaf6d18000286 | deep | arXiv:2606.05043v1 | SRC-ARXIV@arXiv:2606.05043v1 | https://arxiv.org/html/2606.05043v1 §3 Modeling UCP in Langshaw | https://arxiv.org/html/2606.05043v1 §6 Evaluation | https://arxiv.org/html/2606.05043v1 §7 Discussion | https://github.com/Universal-Commerce-Protocol/samples — interoperability dependency referenced; exact-v1 does not pin a paper-specific immutable commit | claim:SF-2026-ARXIV-2606-05043 | complete |
| SF-2026-ARXIV-2606-05122 | RP-b9a023d479ef2559 | deep | arXiv:2606.05122v1 | SRC-ARXIV@arXiv:2606.05122v1 | https://arxiv.org/html/2606.05122v1 §3 Method; §§3.1–3.3 | https://arxiv.org/html/2606.05122v1 §4 Experiments; Appendix A Training Configuration | https://arxiv.org/html/2606.05122v1 Limitations; §5 Discussion | https://github.com/YiShan05/SEE_official — repository disclosed; exact-v1 does not pin an immutable event-time commit | claim:SF-2026-ARXIV-2606-05122 | complete |

### Source Reviews

<!-- review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:start -->
### Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents

<!-- claim:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:start -->把 model 与 harness 分别升级能保持模块自治，却会让 belief、capability 和 goal 在接口处语义漂移。该 position 以 interface contract 组织 goal validity、action archetype、tool instance 与 invocation failure 四级结构，要求持久状态跨 session/版本守恒。 论文提出 architecture/evaluation agenda，没有实现或 benchmark；它支持 long-running Agent 需要 joint conformance，不证明这四层已经充分。contract versioning 和兼容测试有成本，短期无持久状态任务仍可使用平面 action loop。<!-- claim:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:end -->
Deep evidence contract：Method/identity=`arXiv:2606.04017v1 exact-v1 HTML § `2 Agent Epistemic Integrity: A Framework``；Evaluation=`Not Disclosed — arXiv:2606.04017v1 exact-v1 HTML has no separately identifiable empirical evaluation section`；Limitations/counterevidence=`arXiv:2606.04017v1 exact-v1 HTML § `7 Conclusion and Next Steps` — no dedicated limitations heading; the cited closing section was read and the Daily claim boundary records the source-specific non-result`；Artifact=`Not Disclosed — arXiv:2606.04017v1 exact-v1 HTML does not pin an immutable implementation revision`。Owner/authority：`Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents` 的长期机制归入 `AGENT-PLATFORM`；skill/tool/control-plane change、recovery budget、policy 和 audit state 必须分别版本化；capability registry 与 effect executor 保留授权边界。
<!-- review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:end -->

<!-- review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:start -->
### Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study

- **Mechanism / identity:** The 21 sub-projects comprising the catalog corpus were selected from GitHub repositories tagged llm-agent , agent-framework , ai-agent , or llm-orchestration with ≥ 1,000 \geq 1{,}000 stars as of January 2026 in Python, TypeScript, or Rust, and filtered to those that either (a) expose a budget/cost/token-limit option in their public API or (b) have a GitHub issue mentioning cost overrun or runaway-spend in the title. Retained projects span the LangChain/LangGraph, AutoGPT, CrewAI, AutoGen, Pydantic AI, DSPy, LlamaIndex, and IDE-agent ecosystems among others; the full per-project mapping is in the artifact’s catalog CSV project column. Known selection biases: (i) English-language repositories only; (ii) closed-source platforms (Cursor, Replit Agent, ChatGPT plugin store) absent; (iii) the ≥ 1,000 \geq 1{,}000 -star threshold filters out early-stage projects.
- **Evaluation:** The catalog of Section II identifies eight distinct architectural mechanism clusters underlying production budget-overrun incidents. Two distinct mechanisms answer it, and we are careful not to conflate them. A runtime cap (the checked_sub reservation of § III-D , under estimator assumption A1) bounds the dollar consequence of all eight clusters once it is in place — whatever the upstream cause, in-program spend cannot exceed B 0 B_{0} .
- **Evidence boundary:** (1) Constructed reproduction : the racy code is a minimal reproduction of the M-delegation-fanout pattern, not a production extract; the catalog’s 11 such rows establish recurrence, the experiment establishes only the race rate at one parameter setting. (2) Mature runtime patterns avoid it too : actor systems and capability-secure runtimes prevent the race when correctly applied—the comparison is against the operator-error baseline most common in the catalog (shared mutable counter under asyncio.gather ), and the distinguishing claim is only that Rust turns the race into a compile-time error rather than a property the operator must remember to establish. (3) Parameter-dependence : a B 0 ∈ { 50 , 60 , 69 , 100 } B_{0}\in\{50,60,69,100\} sweep (Table VI and its companion) shows the racy condition overshoots exactly when 3 × 3\times per-child > B 0 {}>B_{0} , while the affine and locked dis
- **Artifact:** https://github.com/flyersworder/agent-contracts
<!-- claim:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:end -->
<!-- review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:end -->

<!-- review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:start -->
### Covert Influence Between Language Models

- **Mechanism / identity:** §3–4: a sender model can encode influence in apparently ordinary generated content consumed by a receiver, shifting provenance and trust ownership from human-visible text to the model-to-model channel.
- **Evaluation:** §5–6: controlled sender/receiver experiments measure transfer under the paper's carrier, model and task settings and compare monitoring/mitigation variants.
- **Evidence boundary:** The experiments demonstrate a model-to-model covert channel in tested settings; they do not establish prevalence in production or a complete detector.
- **Artifact:** Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision.
<!-- claim:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:end -->
<!-- review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:end -->

<!-- review:SF-ULTRAEP:start -->
### UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing

- **Mechanism / identity:** UltraEP reacts to post-gating exact expert load on every microbatch and layer, uses quota-driven planning for temporary replication, and transfers irregular expert state through rack-scale persistent tile streaming with relay-based fan-out mitigation. Router semantics remain unchanged; the planner owns execution placement and replication state.
- **Evaluation:** The official v1 abstract reports MoE training and serving prefill across 106B–671B models: average throughput is 94.3% of the force-balanced ideal and 1.49× the no-balancing baseline, final inter-rank imbalance falls from 1.30–4.01 to 1.01–1.04, and production training scalability/robustness is reported at 2560 GPUs.
- **Evidence boundary:** The accessible exact-v1 material is the official abstract, not the removed PDF/HTML body. It covers rack-scale MoE training and serving prefill for 106B–671B models, but does not disclose a dedicated limitations section, GPU model, topology dimensions, precision, batch size, failure recovery, optimizer/gradient correctness, decode behavior or a production latency SLO. Later v3 and the July repository are excluded.
- **Artifact:** Not Disclosed — exact-v1 official abstract names no event-time artifact; later GitHub repository excluded
<!-- claim:SF-ULTRAEP:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-ULTRAEP:end -->
<!-- review:SF-ULTRAEP:end -->

<!-- review:SF-PROOF-CARRYING-ACTIONS:start -->
### Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems

- **Mechanism / identity:** Abstractly, PCAA seeks a control mechanism M M that minimizes severe missed escalations while respecting review budgets and runtime-boundary constraints: The important point is not the specific loss function. PCAA does not treat average scoring quality as the sole endpoint. It treats selective routing, explicit review semantics, and certificate closure as the actual runtime trust problem.
- **Evaluation:** The implementation attaches more than action type and status. The authorization context names allowed systems, allowed actions, data domains, escalation mode, and whether human review is required. The workflow context preserves workflow identity, stage, business process, and connected systems.
- **Evidence boundary:** The layered integrity architecture remains useful, and the current implementation clarifies its role: Fast commitment lane : lightweight commitments or attestations that make silent drift harder. Portable trust lane : typed trust materials, attestations, or credentials that can travel across systems. Future verification lane : stronger receipts or verifiable computation artifacts that may mature later.
- **Artifact:** Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay
<!-- claim:SF-PROOF-CARRYING-ACTIONS:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-PROOF-CARRYING-ACTIONS:end -->
<!-- review:SF-PROOF-CARRYING-ACTIONS:end -->

<!-- review:SF-EVALSTOP:start -->
### EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms

- **Mechanism / identity:** Recall the architecture overview in Figure 1 . EvalStop is a composable wrapper around any base scheduling policy. It monitors eval-score trajectories (the world feedback signal) and early-stops jobs when quality is irrecoverably declining.
- **Evaluation:** We built a discrete-event simulator modelling a multi-tenant fine-tuning platform with heap-based event dispatch, slot-based GPU allocation with 2-minute preemption overhead, and Poisson arrivals. Training curves are parameterised per job type: LoRA (monotonic exponential convergence), DPO (saturating gain with small plateau), and RLHF. Our RLHF workload is a mixture : 60% of RLHF jobs exhibit classical reward hacking (eval peaks in [ 0.55 , 0.75 ] [0.55,0.75] progress and then declines, calibrated to Gao et al.
- **Evidence boundary:** World feedback as a scheduling signal. Our results show that downstream evaluation (world feedback) is a better signal for scheduling RLHF jobs than training loss (proxy 2 ) or reward model score (proxy). This aligns with the growing recognition that proxy optimization in RLHF requires external grounding ( Gao et al., 2023 ; Skalse et al., 2022 ; Moskovitz et al., 2024 ) .
- **Artifact:** Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay
<!-- claim:SF-EVALSTOP:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-EVALSTOP:end -->
<!-- review:SF-EVALSTOP:end -->

<!-- review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:start -->
### Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions

- **Mechanism / identity:** A Sello receipt is a COSE_Sign1 envelope wrapping an HPKE-encrypted payload. The structure is: p ​ k owner pk_{\text{owner}} is the owner’s X25519 public key, bound to the authorization token (Section 4.2) s ​ k service sk_{\text{service}} is the service’s Ed25519 private signing key The body is defined in CDDL [ Birkholz et al., 2019 ] notation, where ? denotes an optional field: receipt-body = { agent-identifier: tstr, ; derived from token hash action-type: tstr, ; e.g.
- **Evaluation:** We present first-party microbenchmarks of the cryptographic operations Sello performs, measured with the reference implementation against a local mock transparency log. The measurements establish steady-state per-receipt costs at the service and the owner. Network latency for submission to a hosted public log is discussed separately in §7.3 because it depends on the specific log operator’s deployment rather than on the Sello protocol itself.
- **Evidence boundary:** An owner who deploys an agent and holds a long-term HPKE key pair. The public key is bound to authorization tokens issued for the agent’s use. An agent , autonomous software acting on the owner’s behalf, which presents authorization tokens when calling services.
- **Artifact:** https://github.com/Prismer-AI/signet
<!-- claim:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:end -->
<!-- review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:end -->

<!-- review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:start -->
### Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines

- **Mechanism / identity:** §3–4: the ANN index is attached to an Apache Iceberg snapshot through Puffin metadata, making index identity and lifecycle follow immutable table snapshots rather than an external mutable service.
- **Evaluation:** §5: the paper evaluates snapshot-attached index construction and query execution in a compute-disaggregated engine against scan/baseline paths under the paper's declared datasets and index settings.
- **Evidence boundary:** The result supports snapshot-consistent vector-index ownership for the evaluated Iceberg/Puffin design; it does not establish one universal ANN format or cross-engine performance.
- **Artifact:** Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision.
<!-- claim:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:end -->
<!-- review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:end -->

<!-- review:SF-ROBOT-BENCHMARK-AUDIT:start -->
### What Are We Actually Benchmarking in Robot Manipulation?

- **Mechanism / identity:** We use a citation tracker repository to derive both the count of new arXiv papers reporting numbers on a given benchmark in a given month (the “79 new arXiv papers” figure in the introduction) and the per-benchmark cumulative counts in Figure 2 . Per-paper evidence and the full row-level audit are available through the project website: ripl.github.io/manipulation_benchmark_audit . The snapshot we report on was taken on 2026-05-21.
- **Evaluation:** Figure 5 shows example observations from the five benchmarks we audit.
- **Evidence boundary:** All four failure modes share one root cause: a benchmark score is an empirical average of success over a fixed test distribution, treated as evidence of capability over the much broader distribution of interest. Each diagnostic catches one way the score can detach from the capability it stands in for: the test instances admit a shortcut, the empirical average is too noisy to resolve the claimed gap, the test distribution is a narrow slice of the variation we care about, or the gap between training and test data drives the score more than capability does. What a future manipulation benchmark should look like.
- **Artifact:** Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay
<!-- claim:SF-ROBOT-BENCHMARK-AUDIT:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-ROBOT-BENCHMARK-AUDIT:end -->
<!-- review:SF-ROBOT-BENCHMARK-AUDIT:end -->

<!-- review:SF-AGENT-DATA-CURATION-HARNESS:start -->
### Can Generalist Agents Automate Data Curation?

- **Mechanism / identity:** Three additional LLM-driven components are part of the methodology rather than the writing process. The four trajectories labels in Table 1 (new policy, grounded, effective, shallow) are produced with LLM assistance using Claude Opus 4.7, following the rubric in Section 2.2 . We treat these labels as diagnostic annotations rather than ground-truth scientific claims, and we provide rubrics and trace examples to support auditing.
- **Evaluation:** The benchmark fixes the evaluation stage and exposes no evaluation parameter to the agent. The protocol – VLMEvalKit wrapper, the eight target benchmarks, the shared Qwen3.5-27B judge endpoint ( Table 16 ), and the aggregation rule ( Table 17 ) – is exactly the one described in Section D.3 . For the DataComp instantiation, the harness uses the standard DataComp evaluation suite ( Gadre et al., 2023 ) : 38 38 zero-shot tasks spanning ImageNet and its distribution shifts, VTAB classification tasks, retrieval (Flickr30k, MSCOCO), and additional classification benchmarks.
- **Evidence boundary:** This paper introduced Curation-Bench , a benchmark for evaluating whether generalist agents can conduct training-data curation as an iterative policy-search process. By fixing the model, training recipe, and evaluation suite, Curation-Bench isolates the curated data policy as the object of optimization and records the full trajectory of agent decisions. Our results show both promise and a limitation.
- **Artifact:** https://github.com/feiyang-k/curation-bench
<!-- claim:SF-AGENT-DATA-CURATION-HARNESS:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-AGENT-DATA-CURATION-HARNESS:end -->
<!-- review:SF-AGENT-DATA-CURATION-HARNESS:end -->

<!-- review:SF-RL-EXCURSIONS-PRETRAINING:start -->
### RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training

- **Mechanism / identity:** In Figure 2 , we report the performance of ℳ t \mathcal{M}_{t} , ℳ t RL \mathcal{M}_{t}^{\text{RL}} , ℳ t SFT \mathcal{M}_{t}^{\text{SFT}} , and ℳ t SFT → RL \mathcal{M}_{t}^{\text{SFT}\rightarrow\text{RL}} at various pre-training steps t t on GSM8K, using the GSM8K subset of OpenMathInstruct for post-training. We evaluate base checkpoints ℳ t \mathcal{M}_{t} with 8-shot prompting, as they cannot reliably follow question-answering instructions 3 3 3 In Appendix B.6 , we ablate the number of in-context examples and confirm that 8-shot yields the best performance for ℳ t \mathcal{M}_{t} . All post-trained models use 0-shot evaluation, as RL includes a formatting reward and SFT data is formatted accordingly.
- **Evaluation:** To answer foundational questions around the RL objective for LLM training, as stated above, beyond the standard training pipeline, we first establish a controlled experimental environment. Our setup centers on a custom-trained 1B model, allowing for precise control over data exposure. In this section, we detail pre-training checkpoints, define three post-training training pipelines, and describe data and evaluation.
- **Evidence boundary:** In this work, we provide a comprehensive and nuanced picture of the RL objective for LLM training beyond how it is used in the current standard pipeline. We find that RL can be effective starting early in pre-training, well before the Chinchilla-optimal regime, and often matches the full SFT → \to RL pipeline on GSM8K tokens despite never seeing a ground-truth reasoning trace. Further, the dominant lever for whether early RL succeeds is pre-training data composition, not model scale.
- **Artifact:** Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay
<!-- claim:SF-RL-EXCURSIONS-PRETRAINING:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-RL-EXCURSIONS-PRETRAINING:end -->
<!-- review:SF-RL-EXCURSIONS-PRETRAINING:end -->

<!-- review:SF-INTERVENTION-TIMING-RELIABILITY:start -->
### The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents

- **Mechanism / identity:** We separate the system into three independent layers, a structure maintained throughout development and documented in a contemporaneous design log.
- **Evaluation:** All three annotators’ label files, the inter-rater computation script (pairwise Cohen’s κ \kappa and three-rater Krippendorff’s α \alpha , implemented from scratch with an independent cross-check), the saturation replay outputs for all five trajectories, and the cross-model sweep outputs are released with this paper. Trigger thresholds and engine constants remained fixed throughout; no post-hoc tuning was applied.
- **Evidence boundary:** All F1 and firing-rate-versus-label metrics are based on a single 56-action trajectory. The saturation result spans five trajectories but uses no labels. Exact label-based metrics are noisy point estimates and should be interpreted directionally only.
- **Artifact:** Not Disclosed — exact-v1 body contains no immutable artifact URL located by this replay
<!-- claim:SF-INTERVENTION-TIMING-RELIABILITY:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-INTERVENTION-TIMING-RELIABILITY:end -->
<!-- review:SF-INTERVENTION-TIMING-RELIABILITY:end -->

<!-- review:SF-LAZYATTENTION:start -->
### LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding

- **Mechanism / identity:** In this section, we show how the positional information of reused documents can be adjusted during the attention calculation. Then we analyze the cost of deferred positional encoding for prefilling and decoding, respectively. Inspired by the analysis, we present how to integrate LazyAttention with FlashAttention ( Dao et al., 2022 ; Dao, 2024 ; Shah et al., 2024 ) seamlessly to achieve efficient computation.
- **Evaluation:** In this section, we evaluate LazyAttention along four research questions (RQs) to demonstrate its advantages, analyze its overhead, and stress-test the scope highlighted by reviewers. More experimental details and additional generalization studies can be found in Appendix B . Does LazyAttention reduce time for the first token (TTFT) under different serving loads?
- **Evidence boundary:** We now quantify why position-awareness directly lowers cache hit ratio. Assume reusable documents follow a Zipf distribution, where the i i -th most popular document has probability proportional to i − α i^{-\alpha} . If each document may appear in any of D D prompt positions and the cache stores C C physical KV entries, a position-agnostic cache stores one entry per document and caches the top C C documents: where N N is the number of reusable documents.
- **Artifact:** https://github.com/LMCache/LMCache
<!-- claim:SF-LAZYATTENTION:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-LAZYATTENTION:end -->
<!-- review:SF-LAZYATTENTION:end -->

<!-- review:SF-OCL-EXECUTION-BOUNDARY:start -->
### Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems

- **Mechanism / identity:** We study how platforms should control agent-mediated economic decisions before they affect real users, merchants, or transactions.
- **Evaluation:** To ensure our evaluation reflects authentic marketplace dynamics, we first compiled a reference corpus of real-world buyer-seller negotiation transcripts across diverse retail scenarios (e.g., street boutiques, wholesale markets, brand outlets, and cosmetics counters). This corpus captures a wide spectrum of natural human bargaining tactics, ranging from persistent haggling and demanding bundle freebies, to feigning walk-aways and leveraging budget constraints. By analyzing these authentic interactions, we identified the key edge cases and uncooperative patterns that commonly disrupt commerce workflows.
- **Evidence boundary:** Across all models, OCL maintains an exceptionally high Success Rate ( ≥ 96 % \geq 96\% ), proving that strict structural constraints do not induce conversation collapse. Concurrently, OCL robustly intercepts adversarial threats, achieving intercept rates of 94% (GPT-5.4), 82% (Gemini-3.1), and 60% (Qwen-3.5)—effectively securing inherently vulnerable baseline architectures.
- **Artifact:** https://github.com/SHITIANYU-hue/amai_ocl
<!-- claim:SF-OCL-EXECUTION-BOUNDARY:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-OCL-EXECUTION-BOUNDARY:end -->
<!-- review:SF-OCL-EXECUTION-BOUNDARY:end -->

<!-- review:SF-AGENT-MEMORY-GENERALITY:start -->
### Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline

- **Mechanism / identity:** Algorithm 1 defines the canonical AutoMEM design: a multi-step plan–execute–judge loop that can re-query memory when the judge finds the trace insufficient. This iterative form is what delivers the accuracy in Table 8 . On top of long context’s single LLM call, the loop issues three to four calls per question (planner, optional dump, judge, answerer), and the outer loop can issue further calls when the judge requests more evidence (Table 9 ).
- **Evaluation:** We measure each memory system on three axes: cross-scenario generality, token cost, and latency.
- **Evidence boundary:** We revisit memory systems for LLM agents through a cross-scenario generality and cost lens and draw: (1) no existing memory system wins across all five task families, while an off-the-shelf agent harness achieves the best generality; (2) index-based methods fail on agentic-trajectory QA in two ways: build-time schemas drop step- and action-level evidence (storage), and passive retrieval cannot surface evidence the storage retains (retrieval); (3) reaching the cost–accuracy frontier requires combining the agent harness with selective indexing, which we instantiate in AutoMEM. We see two potential future directions: (i) a memory DSL that automates schema design — a DSL over memory primitives could replace verbose Cypher and let the schema be meta-learned per workload ( Xiong et al., 2026 ) ; (ii) dedicated infrastructure for memory-bound agents — serial prefill across plan/judge/answer dom
- **Artifact:** https://github.com/mem0ai/mem0
<!-- claim:SF-AGENT-MEMORY-GENERALITY:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-AGENT-MEMORY-GENERALITY:end -->
<!-- review:SF-AGENT-MEMORY-GENERALITY:end -->

<!-- review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:start -->
### The Digital Apprentice: A Framework for Human-Directed Agentic AI Development

- **Mechanism / identity:** Per-skill autonomy tiers, explicit human graduation and runtime drift correction form an inference-time authorization/control plane.
- **Evaluation:** Agentic AI deployments face a recurring design tension: heavy human oversight limits scale, while broad autonomy outruns accountability. Neither posture provides the governance infrastructure required for responsible delegation. We present the Digital Apprentice, a framework for scalable, safe AI agency in which autonomy is earned, not assumed. The Digital Apprentice is a developmental learner that internalizes the tacit methodology of a directing human, graduating through per-skill autonomy tiers only when empirical evidence justifies it. The result is an agent that becomes genuinely useful over time while remaining aligned to a specific human's standards. Three architectural components ma…
- **Evidence boundary:** Evidence is limited to §6 limitations and risks; single professional-corpus proof-of-concept boundary; it does not establish a universal production result outside the declared models, systems, workloads or topology.
- **Artifact:** Not Disclosed — exact-v1 body does not bind an immutable revision
<!-- claim:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:end -->
<!-- review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:end -->

<!-- review:SF-2026-ARXIV-2606-04329:start -->
### 2606.04329 — From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents

**问题、旧方案与约束变化。** 会话内 prompt-injection 防护默认恶意内容随会话结束而消失；一旦 agent 能把输入写入长期 memory，这个旧假设仍便于实现，却不再覆盖跨会话复用的污染状态。

**Mechanism、state / data / control owner 与实现。** MPBench 把攻击拆为 memory write channel、结构漏洞、写入策略与后续检索触发。memory store 持有持久状态，外部 payload 是不可信数据，write/retrieve policy 掌握纳入上下文的控制权；实现以一次投毒写入和后续独立会话中的读取构成端到端事务。

**Evaluation contract、证明与未证明。** §4 只在所列 agent、memory channel 与攻击类上证明更激进的写入/检索策略与更高可利用性相关，并显示现有 prompt-injection defenses 未覆盖这些路径；它没有证明所有 memory 产品、模型或防御都会同样失败。

**Trade-off、failure mode 与旧方案共存边界。** 结构化 provenance、写权限与读取 gate 能缩小攻击面，但会牺牲自动记忆覆盖率并增加状态审计成本；不保存跨会话状态的 assistant 仍可维持较简单的会话隔离。

**演进关系与系统位置。** 这是 AGENT-MEMORY 的 Direct Evolution：从“上下文窗口内的不可信 token”扩展为“具有写权限、生命周期和再次执行机会的持久状态”。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04329v1 §3 Memory Poisoning Attack Taxonomy; §3.1 Threat Model; Appendix A exploitation path`；Evaluation：`https://arxiv.org/html/2606.04329v1 §4 Evaluation; §4.1 MPBench Design`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04329v1 §4.5 Limitations of Prompt Injection Defense against Memory Poisoning; §5 Discussions`；Artifact：`Not Disclosed — exact-v1 cites HERMES as an evaluated target but does not identify it as this paper's versioned artifact`。

<!-- claim:SF-2026-ARXIV-2606-04329:start -->可引用结论只限 `arXiv:2606.04329v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04329:end -->
<!-- review:SF-2026-ARXIV-2606-04329:end -->

<!-- review:SF-2026-ARXIV-2606-04384:start -->
### 2606.04384 — Revisiting Privacy Amplification by Subsampling in Selective Release DPSGD

**问题、旧方案与约束变化。** DPSGD 的标准 subsampling amplification 假设样本进入一次固定机制；selective release 根据中间结果决定是否发布，旧 accountant 忽略了由选择事件改变的有效采样概率。

**Mechanism、state / data / control owner 与实现。** 论文重新推导 selective-release privacy loss，并以 clipped-gradient release rule 组成 DPSR-CG。privacy accountant 持有累计预算，clipped gradient/noise 是受保护数据流，release predicate 控制一次更新是否进入外部可见模型状态。

**Evaluation contract、证明与未证明。** 实验只比较指定数据集、模型、clip/noise 和会计配置下的 privacy–utility；其贡献是修正 formal accounting contract，而不是证明任何 ε 下都优于普通 DPSGD。

**Trade-off、failure mode 与旧方案共存边界。** 选择性发布可避免部分低价值噪声更新，却增加会计复杂度并使 utility 对 release rule 敏感；无法证明选择事件独立性时，应退回保守 accountant 或标准 DPSGD。

**演进关系与系统位置。** 这是 TRAIN-PRETRAINING/PLATFORM-SECURITY 的 Direct Evolution：从每步统一记账到把 release decision 本身纳入 privacy mechanism。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04384v1 §4. METHODOLOGY; §4.1 DP Training Framework with Selective Release Based on Clipping Gradients`；Evaluation：`https://arxiv.org/html/2606.04384v1 §5. EXPERIMENT; §§5.1–5.2`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04384v1 §3.3 Limitations in the Privacy Accounting of DPSUR; §7. Discussion`；Artifact：`https://github.com/FangXieLab/DPSR-CB — repository disclosed; exact-v1 does not pin an immutable event-time commit`。

<!-- claim:SF-2026-ARXIV-2606-04384:start -->可引用结论只限 `arXiv:2606.04384v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04384:end -->
<!-- review:SF-2026-ARXIV-2606-04384:end -->

<!-- review:SF-2026-ARXIV-2606-04402:start -->
### 2606.04402 — Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation

**问题、旧方案与约束变化。** 按预测难度分配 test-time compute 把每个错误视为等价；这一目标在 benchmark accuracy 下合理，却会把生产数据库破坏与无害格式错误赋予同一损失。

**Mechanism、state / data / control owner 与实现。** 轻量 consequence predictor 从任务描述估计错误成本，scheduler 在总预算下选择模型/思考层级。request 保存 consequence estimate，候选解是数据流，budget allocator 掌握额外推理调用的控制权。

**Evaluation contract、证明与未证明。** §7 在指定 SWE-bench solver pool 与 consequence proxy 上证明预算可向高后果任务重分配；它没有证明 consequence label 无偏、也没有给出跨领域生产事故成本。

**Trade-off、failure mode 与旧方案共存边界。** 后果加权降低高代价错误，但可能因 predictor 偏差饿死低分任务并增加 tail latency；错误代价近似相同时，difficulty-only routing 仍更简单。

**演进关系与系统位置。** 这是 INFER-REQUEST-LIFECYCLE/PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：accuracy scheduler 上增加 risk-weighted objective，而非替代底层 execution engine。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04402v1 §3 Consequence-aware allocation; §§5–6 algorithm and guarantees`；Evaluation：`https://arxiv.org/html/2606.04402v1 §7 Experiments`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04402v1 §9 Discussion and Limitations`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04402:start -->可引用结论只限 `arXiv:2606.04402v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04402:end -->
<!-- review:SF-2026-ARXIV-2606-04402:end -->

<!-- review:SF-2026-ARXIV-2606-04413:start -->
### 2606.04413 — (Mis)generalization of Helpful-only Fine-tuning

**问题、旧方案与约束变化。** 只去除 refusal 的 helpful-only fine-tuning 被当作能力评测工具；旧做法能暴露危险能力，却可能同时改变 character、steerability 与 sycophancy，令“更少拒答”等同于“保持其余 alignment”这一假设失效。

**Mechanism、state / data / control owner 与实现。** 研究对 anti-refusal、synthetic-document fine-tuning、SFT/RL character questions 做分支干预。训练数据与 objective 决定权重更新，constitution/character examples 约束行为控制面，评测分别观察 refusal 与非 refusal alignment dimensions。

**Evaluation contract、证明与未证明。** §§2,4–6 证明若干 helpful-only recipes 会产生系统性 misgeneralization，且文档训练或 character 数据能缓解所测指标；没有证明存在通用 harmlessness-preserving recipe。

**Trade-off、failure mode 与旧方案共存边界。** 更少 refusal 提高危险能力可测性，却扩大部署风险且可能破坏 persona 一致性；受控 capability evaluation 可采用它，面向用户的模型仍需独立 harmlessness gate。

**演进关系与系统位置。** 这是 TRAIN-SFT 的 Alternative Branch：把“拒答率”拆成独立训练目标，不再当作整体 alignment 的代理变量。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04413v1 §§3–6 helpful-only training branches and constitution/SDF interventions`；Evaluation：`https://arxiv.org/html/2606.04413v1 §2 Evaluation Suite; §§4–6 results; Appendix A`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04413v1 §8.1 Limitations; §§4–6 failure analyses`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04413:start -->可引用结论只限 `arXiv:2606.04413v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04413:end -->
<!-- review:SF-2026-ARXIV-2606-04413:end -->

<!-- review:SF-2026-ARXIV-2606-04415:start -->
### 2606.04415 — FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location

**问题、旧方案与约束变化。** prefill 与 decode 的资源形态不同，但固定 NPU partition 无法随阶段切换；静态隔离在负载稳定时合理，在动态共置时造成碎片或相互干扰。

**Mechanism、state / data / control owner 与实现。** FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。

**Evaluation contract、证明与未证明。** §4 只对 Ascend 910C/CloudMatrix384、所列模型、W8A8、1K input 与1K/4K output及 TTFT/TPOT 门槛证明原型效果；不证明其他 NPU、精度或 SLO。

**Trade-off、failure mode 与旧方案共存边界。** 虚拟化提高阶段复用率，却引入迁移、隔离和调度开销；专用部署在单一阶段、稳定占用或硬隔离要求强时仍有效。

**演进关系与系统位置。** 这是 INFER-PD-DISAGGREGATION 与 PLATFORM-RESOURCE-SCHEDULING 的 Direct Evolution：从设备级 allocation 细化为阶段级可重绑定资源。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/pdf/2606.04415v1 §3 FlexNPU architecture and phase-level virtualization`；Evaluation：`https://arxiv.org/pdf/2606.04415v1 §4.1 Experimental Setup; §4.2 End-to-end Results; Table 2`；Limitations/Counterevidence：`https://arxiv.org/pdf/2606.04415v1 §5 Discussion and disclosed prototype boundary`；Artifact：`Not Disclosed — exact-v1 PDF does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04415:start -->可引用结论只限 `arXiv:2606.04415v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04415:end -->
<!-- review:SF-2026-ARXIV-2606-04415:end -->

<!-- review:SF-2026-ARXIV-2606-04425:start -->
### 2606.04425 — What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection

**问题、旧方案与约束变化。** 传统 prompt injection 以同一执行上下文中的输入和利用为边界；agent 把内容写入文件、memory、tool metadata 后，注入与激活可以跨会话分离。

**Mechanism、state / data / control owner 与实现。** 论文建立 write–persistence–incorporation–activation 生命周期和 sandbox。持久介质保存攻击状态，clean victim query 触发重新纳入，context constructor 掌握从存储到可执行上下文的数据控制权。

**Evaluation contract、证明与未证明。** §5 在162个跨会话 case 中分别测 WSR、IR、AR 与 E2E-ASR，证明瓶颈可出现在不同阶段；它没有评估所有持久介质或给出已验证的通用 defense。

**Trade-off、failure mode 与旧方案共存边界。** 写入审批、taint/provenance 与重新纳入 gate 增强隔离，却降低 agent 自动积累知识的能力；无持久状态系统仍可用 session-bound 防护。

**演进关系与系统位置。** 这是 AGENT-MEMORY/PLATFORM-SECURITY 的 Direct Evolution：prompt injection 从瞬时输入攻击演变为持久状态供应链攻击。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04425v1 §4 Taxonomy of Stored Prompt Injection; §§4.1–4.4; §§3.1–3.2 system/threat model`；Evaluation：`https://arxiv.org/html/2606.04425v1 §5 Experiments; §§5.1–5.7`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04425v1 §Limitations; §5.7 Discussion`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-04425:start -->可引用结论只限 `arXiv:2606.04425v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04425:end -->
<!-- review:SF-2026-ARXIV-2606-04425:end -->

<!-- review:SF-2026-ARXIV-2606-04459:start -->
### 2606.04459 — Token Rankings are Unforgeable Language Model Signatures

**问题、旧方案与约束变化。** 只返回 token ranking 常被视为比 logits 更安全；旧 API 仍保留模型对输入的相对偏好，因此可能暴露可重复的模型签名。

**Mechanism、state / data / control owner 与实现。** 方法把多次 query 的 token order 组成 ranking signature，再做识别/近似参数恢复。API response 持有排序数据，query adversary 控制采样输入，signature matcher 掌握模型归属判定。

**Evaluation contract、证明与未证明。** PDF §5 只在约50组 ranking 与指定拟合尝试下证明可区分/近似暴露；没有证明能恢复完整权重或对所有解码/API 变体都不可伪造。

**Trade-off、failure mode 与旧方案共存边界。** 限制排名深度、加噪或速率限制能减弱签名，却降低排序 API 的可用性；若客户端只需最终文本，不暴露 token rank 仍是更小接口。

**演进关系与系统位置。** 这是 PLATFORM-SECURITY 的 Principle Reuse：输出最小化从 logits 扩展到任何稳定的相对排序信号。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/pdf/2606.04459v1 §§3–4 ranking-signature geometry and recovery method`；Evaluation：`https://arxiv.org/pdf/2606.04459v1 §4 practical fitting (50 rankings; 3/5 attempts); §5 approximate parameter exposure`；Limitations/Counterevidence：`https://arxiv.org/pdf/2606.04459v1 §6 Discussion and attack-scope boundary`；Artifact：`Not Disclosed — exact-v1 PDF does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04459:start -->可引用结论只限 `arXiv:2606.04459v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04459:end -->
<!-- review:SF-2026-ARXIV-2606-04459:end -->

<!-- review:SF-2026-ARXIV-2606-04522:start -->
### 2606.04522 — ANN Search: Recall What Matters

**问题、旧方案与约束变化。** Recall@k 只衡量与 exact kNN 集合的重合，在邻居距离相近时会惩罚对下游同样有用的结果，导致 ANN 为无意义 overlap 支付计算。

**Mechanism、state / data / control owner 与实现。** 论文用 1/Ratio@k 比较返回邻居与真实邻居的距离质量，并把 metric 作为 index tuning objective。索引持有候选集合，distance 是数据证据，benchmark/tuner 决定 latency–quality operating point。

**Evaluation contract、证明与未证明。** 跨所列 ANN algorithms/datasets 的实验只证明 Recall@k 与 distance quality/下游 utility 可分离，以及替代 metric 改变效率结论；没有证明 1/Ratio@k 适合所有语义任务。

**Trade-off、failure mode 与旧方案共存边界。** distance ratio 无 judge、成本低，但仍继承 embedding metric 的偏差；业务需要离散 exact neighbors 时 Recall@k 仍是正确 contract。

**演进关系与系统位置。** 这是 AGENT-RAG/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：retrieval gate 从集合重合转向对下游有效性的可验证代理。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04522v1 §§3.2–3.3 Accuracy Measures and Downstream Task Evaluation Metrics`；Evaluation：`https://arxiv.org/html/2606.04522v1 §§5–6 Experimental Setup and Results; §6.3 RAG Experiments`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04522v1 §7 Conclusions — reviewed for scope; no dedicated limitations heading`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-04522:start -->可引用结论只限 `arXiv:2606.04522v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04522:end -->
<!-- review:SF-2026-ARXIV-2606-04522:end -->

<!-- review:SF-2026-ARXIV-2606-04557:start -->
### 2606.04557 — Cartridges at Scale: Training Modular KV Caches over Large Document Collections

**问题、旧方案与约束变化。** 单个 monolithic document cartridge 能省去重复 prefill，却无法组合大集合；独立训练的 KV blocks 直接混合又导致分布冲突。

**Mechanism、state / data / control owner 与实现。** CAS 用 dynamic distractor mixing 训练可组合 per-document cartridges，并由 budget manager 在 GPU 与持久存储间轮换。cartridge 是版本化 KV artifact，selector 决定加载集合，cache manager 掌握驻留和 token budget。

**Evaluation contract、证明与未证明。** §§3–4 在指定 Qwen3-8B、数据集和 retrieval/oracle 选择下证明百万 token 集合可扩展及 token savings；没有证明跨模型可移植或线上并发延迟。

**Trade-off、failure mode 与旧方案共存边界。** 预计算状态减少 prefill，却引入训练、artifact identity、选择错误与存储迁移成本；内容变化频繁或请求不复用时，普通 RAG/prefill 更合适。

**演进关系与系统位置。** 这是 INFER-KV-CACHE 的 Direct Evolution：KV 从单请求临时状态演变为可训练、可组合、可分层存储的文档 artifact。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04557v1 §2 Modular cartridge training and composition`；Evaluation：`https://arxiv.org/html/2606.04557v1 §3 Experimental Setup; §4 Experimental Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04557v1 §5 Discussion; Limitations`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04557:start -->可引用结论只限 `arXiv:2606.04557v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04557:end -->
<!-- review:SF-2026-ARXIV-2606-04557:end -->

<!-- review:SF-2026-ARXIV-2606-04581:start -->
### 2606.04581 — Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge

**问题、旧方案与约束变化。** 单用户 speculative decoding 假设 draft 与 verify 在固定链路；多用户 edge 中设备算力、上行带宽和 draft acceptance 同时变化，固定 draft length 会放大慢节点。

**Mechanism、state / data / control owner 与实现。** Multi-SPIN 让设备 SLM 产出 drafts、edge LLM 批量验证，并联合优化 draft length、频分带宽和计算分配。每用户 draft/acceptance 是状态，radio/compute budget 是资源数据，central optimizer 掌握分配控制。

**Evaluation contract、证明与未证明。** §VI 只在所列模型对、A100 edge server 与模拟网络条件下证明 sum token goodput；没有证明公网抖动、生产 tail SLO 或不同 tokenizer 的效果。

**Trade-off、failure mode 与旧方案共存边界。** 合作生成分摊 server compute，却增加通信、同步和 rejected-draft 浪费；链路差或本地 SLM 弱时，server-only decoding 仍可能更快。

**演进关系与系统位置。** 这是 INFER-SPECULATIVE-DECODING/INFER-DISTRIBUTED-RUNTIME 的 Direct Evolution：proposal ownership 从同机 draft model 扩展到多接入设备。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04581v1 §III Protocol and Problem Formulation; §§IV–V distributed control`；Evaluation：`https://arxiv.org/html/2606.04581v1 §VI Experimental Results; §VI-A Experiment Settings`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04581v1 §VII Concluding Remarks — no dedicated limitations section`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04581:start -->可引用结论只限 `arXiv:2606.04581v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04581:end -->
<!-- review:SF-2026-ARXIV-2606-04581:end -->

<!-- review:SF-2026-ARXIV-2606-04594:start -->
### 2606.04594 — Ekka: Automated Diagnosis of Silent Errors in LLM Inference

**问题、旧方案与约束变化。** serving optimization 的 silent error 不崩溃、只悄然降低输出质量；从最终文本反推 kernel/runtime root cause 跨越过大的语义层。

**Mechanism、state / data / control owner 与实现。** Ekka 对齐 target 与 reference implementation 的中间 execution states，逐层/逐算子做 differential diagnosis。reference trace 是正确性证据，target trace 是观测数据，alignment/search controller 定位首个 divergence。

**Evaluation contract、证明与未证明。** §5 的 pass@1/pass@5 只对作者构造的真实 silent-error benchmark 与指定 backend/模型成立；没有证明 reference 自身无错或覆盖所有 nondeterminism。

**Trade-off、failure mode 与旧方案共存边界。** 中间态比对提高可诊断性，却要求可观测点、可比 reference 与额外存储/执行；无法复现或跨硬件数值漂移大时仍需 invariant/metamorphic tests。

**演进关系与系统位置。** 这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：observability 从性能 telemetry 扩展为跨实现的语义正确性证据。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04594v1 §3 Ekka design; §4 Implementation`；Evaluation：`https://arxiv.org/html/2606.04594v1 §5 Evaluation; §§5.1–5.7`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04594v1 §7 Discussion`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04594:start -->可引用结论只限 `arXiv:2606.04594v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04594:end -->
<!-- review:SF-2026-ARXIV-2606-04594:end -->

<!-- review:SF-2026-ARXIV-2606-04628:start -->
### 2606.04628 — RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation

**问题、旧方案与约束变化。** 把 agent memory 当拼接文本会混淆内容所有权、优先级和回滚；简单截断虽便宜，却不能表达哪些 block 可被谁写入或必须保留。

**Mechanism、state / data / control owner 与实现。** RAMPART 以 named block registry 保存 provenance/priority/authorship，并在 compile context 前执行 promote、gate、write、evict、rollback。registry 持有状态，blocks 是数据，policy engine 掌握上下文编译权。

**Evaluation contract、证明与未证明。** Qwen3-8B Q4 probes 只证明特定 block 位置/分组会改变任务成功率以及这些 primitives 可调节位置；没有证明通用长期记忆质量或多租户隔离。

**Trade-off、failure mode 与旧方案共存边界。** 显式 registry 提供权限与回滚，却增加 policy 配置和 block lifecycle 复杂度；短会话、无写入的 prompt 仍可直接拼接。

**演进关系与系统位置。** 这是 AGENT-MEMORY 的 Direct Evolution：从 token budget 管理提升为有地址、权限和事务操作的状态管理。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04628v1 §2 RAMPART model and registry operations`；Evaluation：`https://arxiv.org/html/2606.04628v1 §3 Experiments; §§3.1–3.2`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04628v1 §6 Conclusion — no dedicated limitations section`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04628:start -->可引用结论只限 `arXiv:2606.04628v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04628:end -->
<!-- review:SF-2026-ARXIV-2606-04628:end -->

<!-- review:SF-2026-ARXIV-2606-04769:start -->
### 2606.04769 — Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications

**问题、旧方案与约束变化。** MCP client 按自然语言 description 选择工具，默认描述与代码行为一致；版本漂移或未声明副作用会让模型在错误权限假设下执行。

**Mechanism、state / data / control owner 与实现。** DCIChecker 联合 schema-aware static analysis 与 LLM classifier，对 description、signature、implementation effects 建立一致性检查。代码与描述是双份接口数据，server owner 维护实现，release gate 决定不一致是否阻断发布。

**Evaluation contract、证明与未证明。** measurement 只对采样的真实 MCP repositories 与分类 taxonomy 证明 DCI 存在并可被检测；没有证明 classifier 能替代 sandbox/runtime enforcement。

**Trade-off、failure mode 与旧方案共存边界。** 静态/语义检查提前发现 drift，却有解析覆盖和 LLM 误判；高风险工具仍需 capability policy 与运行时审计。

**演进关系与系统位置。** 这是 AGENT-MCP/PLATFORM-SECURITY 的 Direct Evolution：protocol conformance 从 wire schema 扩展到描述、代码和副作用的一致性。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04769v1 §IV DCIChecker; §IV-B Structure-Aware Tool Semantic Extraction; §IV-C DCI Checking with DRA-Prompting`；Evaluation：`https://arxiv.org/html/2606.04769v1 §V Real-world Measurement; §§V-A–V-D`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04769v1 §VII Discussion — Limitations and scope`；Artifact：`Not Disclosed — exact-v1 does not identify a versioned public DCIChecker artifact`。

<!-- claim:SF-2026-ARXIV-2606-04769:start -->可引用结论只限 `arXiv:2606.04769v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04769:end -->
<!-- review:SF-2026-ARXIV-2606-04769:end -->

<!-- review:SF-2026-ARXIV-2606-04778:start -->
### 2606.04778 — Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories

**问题、旧方案与约束变化。** shallow-safety 只关注开头 token 的拒答方向；生成中途注入可在任意 step 改写后续轨迹，说明最终输出或早期 hidden-state alignment 不是充分 robustness 证据。

**Mechanism、state / data / control owner 与实现。** 方法模拟 mid-sequence token perturbation，构造 trajectory-level alignment data 并直接训练扰动后的继续生成。decoder state 持有轨迹，注入 token 改变数据流，training objective 负责把恢复行为写入权重。

**Evaluation contract、证明与未证明。** §4 在三类7B/8B instruct models和指定 harmfulness suites 上证明中途脆弱性与训练增益；没有证明对所有 white-box activation intervention 或更大模型成立。

**Trade-off、failure mode 与旧方案共存边界。** 轨迹训练覆盖更多攻击位置，却增加合成扰动成本并可能压制正常纠错/用户改写；只需静态单轮拒答的系统仍可使用较轻的 output filter。

**演进关系与系统位置。** 这是 TRAIN-SFT/PLATFORM-SECURITY 的 Direct Evolution：alignment target 从首 token/final answer 延伸到整个生成状态机。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04778v1 §3 trajectory-level alignment method; Appendix A`；Evaluation：`https://arxiv.org/html/2606.04778v1 §4 Experiments and Analysis`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04778v1 Appendix E Limitation and Broader Impact`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04778:start -->可引用结论只限 `arXiv:2606.04778v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04778:end -->
<!-- review:SF-2026-ARXIV-2606-04778:end -->

<!-- review:SF-2026-ARXIV-2606-04799:start -->
### 2606.04799 — UModel: An Agent-Ready Observability Data Modeling Method at Scale

**问题、旧方案与约束变化。** metrics、logs、traces 与拓扑各自成 silo 时，人能凭经验拼接，agent RCA 却缺少可查询的实体身份和关系。

**Mechanism、state / data / control owner 与实现。** UModel 建虚拟 ontology，把 telemetry、entities 与 expert knowledge 映射为 object graph，并由 U-SPL pipeline 查询。object identity/relations 是共享状态，source adapters 供数据，query planner 掌握跨源探索控制。

**Evaluation contract、证明与未证明。** 作者案例只证明统一模型支持所测 RCA/query workflow；没有证明任意 vendor schema 自动可对齐或 ontology 长期无漂移。

**Trade-off、failure mode 与旧方案共存边界。** object-centric layer提高跨源推理，却带来 schema governance、identity resolution 和摄取成本；单一服务的小规模诊断仍可直接查原生 telemetry。

**演进关系与系统位置。** 这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：从采集信号扩展到可被 agent 消费的语义对象与关系层。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04799v1 §III Agent-Ready Data Model`；Evaluation：`https://arxiv.org/html/2606.04799v1 §VI Evaluation`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04799v1 §VIII Conclusion`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-04799:start -->可引用结论只限 `arXiv:2606.04799v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04799:end -->
<!-- review:SF-2026-ARXIV-2606-04799:end -->

<!-- review:SF-2026-ARXIV-2606-04850:start -->
### 2606.04850 — Uncertainty-Aware End-to-End Co-Design of Neural Network Processors: From Training and Mapping to Fabrication

**问题、旧方案与约束变化。** 传统 accelerator co-design 把网络训练、算子映射、硬件参数与制造偏差分阶段固定；这在每层接口稳定时合理，却会在 fabrication/latency/energy uncertainty 跨阶段传播时失去全局可比性。

**Mechanism、state / data / control owner 与实现。** 正文以 functionality-resource interface 组合 training、mapping、fabrication 与 resource-allocation blocks，并用 distributional/MDPI model 联合优化。co-design optimizer 持有决策状态，各阶段分布是数据，联合搜索掌握候选选择。

**Evaluation contract、证明与未证明。** §V 的 simulation 只证明指定 workload、processor model、uncertainty distribution 与 cost function 下的联合方案；没有证明真实 chip tape-out、跨 workload 稳健性或生产 SLO。

**Trade-off、failure mode 与旧方案共存边界。** 联合搜索减少阶段割裂，却增加模型假设、搜索成本与 distribution misspecification 风险；制造波动可忽略或 toolchain 必须独立演进时，分阶段设计仍更易验证。

**演进关系与系统位置。** 这是 INFER-TENSORRT-LLM execution-plan owner 的 Alternative Branch：从 deterministic mapping 扩展到 uncertainty-aware co-design。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04850v1 §III Model for Co-design with Distributional Uncertainty; §IV MDPI Model; §§IV-A–IV-D`；Evaluation：`https://arxiv.org/html/2606.04850v1 §V Simulation Results; §§V-A–V-C`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04850v1 §VI Conclusion; §VI-A Outlook — no dedicated limitations section`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04850:start -->可引用结论只限 `arXiv:2606.04850v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04850:end -->
<!-- review:SF-2026-ARXIV-2606-04850:end -->

<!-- review:SF-2026-ARXIV-2606-04903:start -->
### 2606.04903 — Provably Auditable and Safe LLM Agents from Human-Authored Ontologies

**问题、旧方案与约束变化。** 自由文本 planning 让 LLM 同时拥有领域解释和动作决定权，难以线性审计；在规则稳定、风险低时灵活，但高风险域无法预先证明允许行为。

**Mechanism、state / data / control owner 与实现。** Ontology-First design 由人定义 typed domain ontology/roles，Agentic Redux 用 typed lambda calculus 约束步骤并写 append-only ledger。ontology 持有规范状态，typed terms 是数据，checker/role policy 掌握执行授权。

**Evaluation contract、证明与未证明。** 论文给出 healthcare billing 与 vulnerability disclosure 两个 appropriate-domain 实现及语义论证；没有证明开放世界任务能被完整 ontologize，也未证明 LLM 感知输入正确。

**Trade-off、failure mode 与旧方案共存边界。** 可证明的 typed path 增强审计，却依赖昂贵的 ontology maintenance 并限制开放式推理；低风险探索仍可保留自由规划再加事后 review。

**演进关系与系统位置。** 这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Alternative Branch：从概率式 planner 转向人定义语义边界内的可验证执行。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04903v1 §1.4 Methodology; §1.4.3 Ontology-First Agent Design`；Evaluation：`https://arxiv.org/html/2606.04903v1 §2.3 Derivation of System Invariants; Appendix A.3.2 Preservation of Base Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04903v1 §1.2 Threat Model (What is Safety) — In scope / Out of scope; §5 Conclusion and Future Work`；Artifact：`https://github.com/Thistleseeds/agentic-redux — repository disclosed; exact-v1 does not pin an immutable event-time commit`。

<!-- claim:SF-2026-ARXIV-2606-04903:start -->可引用结论只限 `arXiv:2606.04903v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04903:end -->
<!-- review:SF-2026-ARXIV-2606-04903:end -->

<!-- review:SF-2026-ARXIV-2606-04908:start -->
### 2606.04908 — GNStor: Design of GPU-Native High-Performance Remote All-Flash Array

**问题、旧方案与约束变化。** GPU 已是计算中心，但远端 AFA I/O 仍由 CPU 编排，形成 host bounce、集中 metadata engine 与 traffic amplification。

**Mechanism、state / data / control owner 与实现。** GNStor 把 NVMe-over-RDMA request path 和部分 AFA functionality 下沉到 GPU，GPU queues 持有 I/O state，RDMA/NVMe buffers 是数据，GPU-side stack 掌握提交与完成控制。

**Evaluation contract、证明与未证明。** 实验只对 AMD EPYC 9654、768GB DDR5、A100 40GB 与指定 AFA/network configuration 的 throughput/latency 成立；不证明通用 filesystem semantics 或 failure recovery。

**Trade-off、failure mode 与旧方案共存边界。** 绕过 CPU 降低 data-path overhead，却增加 GPU runtime、metadata consistency 与隔离复杂度；控制面密集、GPU 利用低或共享 storage policy 强时 CPU-centric 路线仍合理。

**演进关系与系统位置。** 这是 PLATFORM-STORAGE/INFER-EXECUTION 的 Direct Evolution：accelerator 从数据消费者变成远端存储 I/O 的主动 owner。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04908v1 §4. Design and Implementation`；Evaluation：`https://arxiv.org/html/2606.04908v1 §5. Evaluation; §5.1 Experimental Setup`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04908v1 §6. Related Work and Discussion; §7. Conclusion`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-04908:start -->可引用结论只限 `arXiv:2606.04908v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04908:end -->
<!-- review:SF-2026-ARXIV-2606-04908:end -->

<!-- review:SF-2026-ARXIV-2606-04923:start -->
### 2606.04923 — Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning

**问题、旧方案与约束变化。** rubric RL 把 LLM judge score 当奖励，默认高分代表满足 rubric；policy 可学习 judge bias，使奖励上升而真实质量下降。

**Mechanism、state / data / control owner 与实现。** CHERRL 可控注入 judge bias，跟踪 reward divergence/hacking onset，并用 agent detector 搜索作弊行为。rubric/judge 持有评价状态，policy outputs 是数据，RL optimizer 把 judge signal 转成权重更新控制。

**Evaluation contract、证明与未证明。** §4/appendices 只证明所注入 biases 可被发现/利用以及 detector 在该环境中的表现；没有证明真实生产 judge 的全部 latent bias 被覆盖。

**Trade-off、failure mode 与旧方案共存边界。** 可控 testbed 提高可复现性，却可能过拟合人为 bias；真实 release gate 仍需独立 human/held-out evaluator 和 reward-channel monitoring。

**演进关系与系统位置。** 这是 TRAIN-RLHF/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：reward model 从可信 oracle 变成需做 adversarial validation 的系统组件。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04923v1 §2 CHERRL; §§2.2–2.5; §4.1 Agentic Detector Design`；Evaluation：`https://arxiv.org/html/2606.04923v1 §2.5; §4.2; Appendices B, D and F`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04923v1 Limitations; Appendix B.8`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-04923:start -->可引用结论只限 `arXiv:2606.04923v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04923:end -->
<!-- review:SF-2026-ARXIV-2606-04923:end -->

<!-- review:SF-2026-ARXIV-2606-04929:start -->
### 2606.04929 — Sequential Data Poisoning in LLM Post-Training

**问题、旧方案与约束变化。** 逐阶段独立审计 SFT 与 DPO poisoning 会认为每个小预算攻击都无害；post-training 顺序使前一阶段改变的表示可被后一阶段放大。

**Mechanism、state / data / control owner 与实现。** 论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。

**Evaluation contract、证明与未证明。** 实验只在列出的 Llama/Qwen、poison budgets 与 SFT→DPO/LoRA 配置上证明 additive/cross-stage interaction；没有覆盖完整 RLHF 或现实供应链攻击率。

**Trade-off、failure mode 与旧方案共存边界。** 跨阶段 provenance/audit 能发现组合风险，却增加数据 lineage 和 checkpoint 隔离成本；单一可信数据源的短 pipeline 可保持阶段内检测。

**演进关系与系统位置。** 这是 TRAIN-SFT→TRAIN-DPO 的 Direct Evolution：安全 owner 从单个 trainer 上移到整个 post-training checkpoint chain。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.04929v1 §5 Sequential Data Poisoning; §§5.1–5.3`；Evaluation：`https://arxiv.org/html/2606.04929v1 §4 Experimental Setup; Appendix D.2 Evaluation Details; Appendix E`；Limitations/Counterevidence：`https://arxiv.org/html/2606.04929v1 §6 Conclusion — Limitations and future work`；Artifact：`Not Disclosed — exact-v1 does not identify one versioned public attack artifact`。

<!-- claim:SF-2026-ARXIV-2606-04929:start -->可引用结论只限 `arXiv:2606.04929v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-04929:end -->
<!-- review:SF-2026-ARXIV-2606-04929:end -->

<!-- review:SF-2026-ARXIV-2606-05004:start -->
### 2606.05004 — SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models

**问题、旧方案与约束变化。** 现有 private inference 常修改模型或逐 prompt 加噪，分别损害兼容性、utility 与成本；公共黑盒 API 又不给调用方权重访问。

**Mechanism、state / data / control owner 与实现。** SharedRequest 生成 noisy prompt variants、按语义等价 instruction 分组并在 batch level 共享请求。client 持有敏感原文和扰动，grouping service 控制批合并，remote model 只接收混合后的请求集合。

**Evaluation contract、证明与未证明。** 作者实验只在指定 prompts/models/privacy attack 与 GPT-5.2 attribute inference slice 上报告 utility/cost；没有给出对任意 side channel 或恶意 provider 的 cryptographic secrecy。

**Trade-off、failure mode 与旧方案共存边界。** model-agnostic batching降低调用成本，却引入语义分组错误、额外 queries 与群体依赖；高敏感、强对手场景仍需 trusted execution、local model 或 cryptographic protocol。

**演进关系与系统位置。** 这是 INFER-BATCHING/PLATFORM-SECURITY 的 Principle Reuse：batch 不再只做吞吐优化，也成为 privacy mixing boundary。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05004v1 §4 Framework; §5 Privacy Analysis`；Evaluation：`https://arxiv.org/html/2606.05004v1 §7 Experiment; Appendix G Experiment; §5 Privacy Analysis for the formal claim`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05004v1 Limitation — dedicated heading after §8 Conclusion`；Artifact：`Not Disclosed — exact-v1 does not bind a public artifact to an immutable revision`。

<!-- claim:SF-2026-ARXIV-2606-05004:start -->可引用结论只限 `arXiv:2606.05004v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05004:end -->
<!-- review:SF-2026-ARXIV-2606-05004:end -->

<!-- review:SF-2026-ARXIV-2606-05029:start -->
### 2606.05029 — Validity Threats for Foundation Model Research

**问题、旧方案与约束变化。** frontier training 太贵，使研究改用 proxy model、observational comparison 或 single-run variation；省算力并未消除因果问题，只把成本换成隐藏 validity assumptions。

**Mechanism、state / data / control owner 与实现。** 框架把研究设计映射到 statistical、internal、external、construct validity，并为三类低成本 strategy 建立 characteristic threat profile。experiment design 持有 estimand，observations 是证据数据，claim gate 决定可外推范围。

**Evaluation contract、证明与未证明。** 论文提供方法论分析而非新的模型 benchmark；它证明的是各策略存在可枚举的因果威胁，不证明某一策略在所有研究问题上失效。

**Trade-off、failure mode 与旧方案共存边界。** 显式 validity contract 提高结论可审计性，却要求更多假设记录与 sensitivity analysis；资源足够时，直接 controlled replication 仍更强。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation contract 从 metric/config 扩展到 estimand、identification assumption 与外推边界。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05029v1 §3 The Proxy Approach`；Evaluation：`https://arxiv.org/html/2606.05029v1 §6 Validity Profiles for Foundation Model Research`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05029v1 §8 Discussion`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-05029:start -->可引用结论只限 `arXiv:2606.05029v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05029:end -->
<!-- review:SF-2026-ARXIV-2606-05029:end -->

<!-- review:SF-2026-ARXIV-2606-05037:start -->
### 2606.05037 — Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery

**问题、旧方案与约束变化。** API validation error 只给自然语言原因时，agent 仍需猜测可执行修复；更长 prose 未必提供字段级 actionability。

**Mechanism、state / data / control owner 与实现。** self-reflective API 返回 machine-readable recovery_feedback.suggestions[]，将失败字段、修复动作和 retry 输入结构化。server 持有 schema truth，error payload 是控制数据，agent retry loop 决定是否应用建议。

**Evaluation contract、证明与未证明。** N=30/cell、3 models、10 adversarial tasks 的 pilot 只证明 Anthropic models 上显著提升且 gpt-4o lift 不显著；不能外推为所有 API 或 agent。

**Trade-off、failure mode 与旧方案共存边界。** 结构建议提高恢复率，却扩大 API contract、可能泄露 schema/security细节；人工客户端或简单错误仍可使用普通 status/message。

**演进关系与系统位置。** 这是 AGENT-TOOL-USE/API contract 的 Direct Evolution：错误从诊断文本变成受 schema 约束的下一步控制接口。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05037v1 §3 Design: Self-Reflective API Framework; §4 Implementation`；Evaluation：`https://arxiv.org/html/2606.05037v1 §5 Evaluation; §§5.1–5.4`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05037v1 §5.5 Limitations and Threats to Validity; §6.2 Failure/Saturation cases`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-05037:start -->可引用结论只限 `arXiv:2606.05037v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05037:end -->
<!-- review:SF-2026-ARXIV-2606-05037:end -->

<!-- review:SF-2026-ARXIV-2606-05043:start -->
### 2606.05043 — Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols

**问题、旧方案与约束变化。** multi-agent protocol 由应用代码隐式实现时，消息顺序、承诺和角色约束散落在 control flow 中，难以验证或替换参与者。

**Mechanism、state / data / control owner 与实现。** Strabo 把 UCP checkout 建模为 declarative Langshaw protocol，并用 Peach agents 执行且与 Google UCP agents 互操作。protocol artifact 持有允许交互状态，messages 是数据，runtime verifier 掌握 transition control。

**Evaluation contract、证明与未证明。** 案例只证明 checkout 子协议可表达并与所测 UCP implementation 互通；没有覆盖 UCP 全部域、故障恢复或生产规模。

**Trade-off、failure mode 与旧方案共存边界。** 声明式协议增强一致性和渐进替换，却要求 schema/protocol evolution governance；局部、单进程 workflow 仍可保留直接代码。

**演进关系与系统位置。** 这是 AGENT-WORKFLOW/AGENT-MULTI-AGENT 的 Direct Evolution：interaction contract 从隐式代码提升为独立、可执行、可验证 artifact。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05043v1 §3 Modeling UCP in Langshaw`；Evaluation：`https://arxiv.org/html/2606.05043v1 §6 Evaluation`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05043v1 §7 Discussion`；Artifact：`https://github.com/Universal-Commerce-Protocol/samples — interoperability dependency referenced; exact-v1 does not pin a paper-specific immutable commit`。

<!-- claim:SF-2026-ARXIV-2606-05043:start -->可引用结论只限 `arXiv:2606.05043v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05043:end -->
<!-- review:SF-2026-ARXIV-2606-05043:end -->

<!-- review:SF-2026-ARXIV-2606-05122:start -->
### 2606.05122 — Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data

**问题、旧方案与约束变化。** 训练一个外部 judge 或让模型直接报 confidence 混合了评价能力与校准表达；base model 可能已有排序信号，只是未被稳定 elicitation。

**Mechanism、state / data / control owner 与实现。** SEE 先做 calibration-coupled RL 同时回答和预测 judge，再 masked distillation 只锐化 score prediction。模型 token distribution 持有潜在自评信号，judge labels 是校准数据，loss mask 控制哪些行为被更新。

**Evaluation contract、证明与未证明。** 三 benchmark、160 examples、Qwen3-4B-Base 结果只证明所测 judge/attributes 上校准改善且 answer quality 保持；不等于事实正确性或模型知道未知。

**Trade-off、failure mode 与旧方案共存边界。** 少数据 elicitation 降低训练成本，却继承外部 judge bias，并可能把 confidence 误当 truth；高风险 claims 仍需外部 evidence verification。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：把自评看成需校准的测量通道，而非生成概率的直接解释。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.05122v1 §3 Method; §§3.1–3.3`；Evaluation：`https://arxiv.org/html/2606.05122v1 §4 Experiments; Appendix A Training Configuration`；Limitations/Counterevidence：`https://arxiv.org/html/2606.05122v1 Limitations; §5 Discussion`；Artifact：`https://github.com/YiShan05/SEE_official — repository disclosed; exact-v1 does not pin an immutable event-time commit`。

<!-- claim:SF-2026-ARXIV-2606-05122:start -->可引用结论只限 `arXiv:2606.05122v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-05122:end -->
<!-- review:SF-2026-ARXIV-2606-05122:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | e cap (the checked_sub reservation of § III-D , under estimator assumption A1) bounds the dollar consequence of all eight clusters once it is in place — whatever the upstream cause, in-program spend cannot exceed B 0 B_{0} . | Retained projects span the LangChain/LangGraph, AutoGPT, CrewAI, AutoGen, Pydantic AI, DSPy, LlamaIndex, and IDE-agent ecosystems among others; the full per-project mapping is in the artifact’s catalog CSV project column. | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | See evaluation locator for dataset/workload and filtering. | See evaluation locator; model identities are source-specific. | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed | Not Disclosed | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed — these papers do not establish a production SLO. | See evaluation locator for metric and reference-answer contract. |
| SF-ULTRAEP | MoE training and serving prefill; exact post-gating load rebalanced every microbatch and layer | MoE models from 106B to 671B parameters | Rack-scale nodes; production training validation with 2560 GPUs; GPU model Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Per-microbatch planning; numeric microbatch size Not Disclosed | Not Disclosed | Not Disclosed | Force-balanced ideal throughput ratio; throughput versus no balancing; final inter-rank imbalance |
| SF-PROOF-CARRYING-ACTIONS | The authorization context names allowed systems, allowed actions, data domains, escalation mode, and whether human review is required. | Not Disclosed — exact-v1 replay did not locate a reproducible model field | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-EVALSTOP | Not Disclosed — exact-v1 replay did not locate a reproducible input field | We built a discrete-event simulator modelling a multi-tenant fine-tuning platform with heap-based event dispatch, slot-based GPU allocation with 2-minute preemption overhead, and Poisson arrivals. | simulator modelling a multi-tenant fine-tuning platform with heap-based event dispatch, slot-based GPU allocation with 2-minute preemption overhead, and Poisson arrivals. | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | crete-event simulator modelling a multi-tenant fine-tuning platform with heap-based event dispatch, slot-based GPU allocation with 2-minute preemption overhead, and Poisson arrivals. | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | Not Disclosed — exact-v1 replay did not locate a reproducible input field | Not Disclosed — exact-v1 replay did not locate a reproducible model field | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Network latency for submission to a hosted public log is discussed separately in §7. | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | See evaluation locator for dataset/workload and filtering. | See evaluation locator; model identities are source-specific. | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed | Not Disclosed | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed unless explicitly stated in the evaluation locator. | Not Disclosed — these papers do not establish a production SLO. | See evaluation locator for metric and reference-answer contract. |
| SF-ROBOT-BENCHMARK-AUDIT | Not Disclosed — exact-v1 replay did not locate a reproducible input field | Not Disclosed — exact-v1 replay did not locate a reproducible model field | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-AGENT-DATA-CURATION-HARNESS | Not Disclosed — exact-v1 replay did not locate a reproducible input field | The protocol – VLMEvalKit wrapper, the eight target benchmarks, the shared Qwen3. | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | 5-27B judge endpoint ( Table 16 ), and the aggregation rule ( Table 17 ) – is exactly the one described in Section D. |
| SF-RL-EXCURSIONS-PRETRAINING | We evaluate base checkpoints ℳ t \mathcal{M}_{t} with 8-shot prompting, as they cannot reliably follow question-answering instructions 3 3 3 In Appendix B. | Our setup centers on a custom-trained 1B model, allowing for precise control over data exposure. | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-INTERVENTION-TIMING-RELIABILITY | Not Disclosed — exact-v1 replay did not locate a reproducible input field | an independent cross-check), the saturation replay outputs for all five trajectories, and the cross-model sweep outputs are released with this paper. | rff’s α \alpha , implemented from scratch with an independent cross-check), the saturation replay outputs for all five trajectories, and the cross-model sweep outputs are released with this paper. | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-LAZYATTENTION | Not Disclosed — exact-v1 replay did not locate a reproducible input field | Not Disclosed — exact-v1 replay did not locate a reproducible model field | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-OCL-EXECUTION-BOUNDARY | Not Disclosed — exact-v1 replay did not locate a reproducible input field | Not Disclosed — exact-v1 replay did not locate a reproducible model field | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | Not Disclosed — exact-v1 replay did not locate a reproducible slo field | Not Disclosed — exact-v1 replay did not locate a reproducible evaluator field |
| SF-AGENT-MEMORY-GENERALITY | Not Disclosed — exact-v1 replay did not locate a reproducible input field | Not Disclosed — exact-v1 replay did not locate a reproducible model field | Not Disclosed — exact-v1 replay did not locate a reproducible hardware field | Not Disclosed — exact-v1 replay did not locate a reproducible precision field | Not Disclosed | Not Disclosed | Not Disclosed — exact-v1 replay did not locate a reproducible batch field | Not Disclosed — exact-v1 replay did not locate a reproducible concurrency field | We measure each memory system on three axes: cross-scenario generality, token cost, and latency. | Algorithm 1 defines the canonical AutoMEM design: a multi-step plan–execute–judge loop that can re-query memory when the judge finds the trace insufficient. |
| SF-DIGITAL-APPRENTICE-CONTROL-PLANE | Source-declared benchmark/workload only | See exact-v1 evaluation locator; model identities are source-bound | See exact-v1 evaluation locator; Not Disclosed where absent | Not Disclosed unless stated in exact-v1 | Not Disclosed | Not Disclosed | Not Disclosed unless stated in exact-v1 | Not Disclosed unless stated in exact-v1 | No production SLO established | §5 proof-of-concept |
| SF-2026-ARXIV-2606-04329 | Disclosed — §4 只在所列 agent、memory channel 与攻击类上证明更激进的写入/检索策略与更高可利用性相关，并显示现有 prompt-injection defenses 未覆盖这些路径；它没有证明所有 memory 产品、模型或防御都会同样失败。 Locator: https://arxiv.org/html/2606.04329v1 §4 Evaluation; §4.1 MPBench Design | Disclosed — OpenClaw and HERMES use GPT-OSS-120B | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §4.1.3 defines attack success rate and retrieval success rate; §§4.2–4.5 report both across agents, attacks and defenses |
| SF-2026-ARXIV-2606-04384 | Disclosed — 实验只比较指定数据集、模型、clip/noise 和会计配置下的 privacy–utility；其贡献是修正 formal accounting contract，而不是证明任何 ε 下都优于普通 DPSGD。 Locator: https://arxiv.org/html/2606.04384v1 §5. EXPERIMENT; §§5.1–5.2 | Disclosed — §5.1.1 uses a standard CNN for MNIST/FMNIST/CIFAR-10 and a five-layer RNN for IMDB | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Disclosed — §5.1.2/Table 2 publish dataset-specific effective batches; no universal batch applies | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §5 reports privacy-accounting validity and privacy–utility accuracy under the named datasets and release configurations |
| SF-2026-ARXIV-2606-04402 | Disclosed — §7 在指定 SWE-bench solver pool 与 consequence proxy 上证明预算可向高后果任务重分配；它没有证明 consequence label 无偏、也没有给出跨领域生产事故成本。 Locator: https://arxiv.org/html/2606.04402v1 §7 Experiments | Disclosed — §7 aggregates 16 named SWE-bench solvers from Claude 2/GPT-4 through Claude 4 Sonnet | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §7 evaluates consequence-weighted expected utility and resolve rate, with consequence labels separately audited |
| SF-2026-ARXIV-2606-04413 | Disclosed — §§2,4–6 证明若干 helpful-only recipes 会产生系统性 misgeneralization，且文档训练或 character 数据能缓解所测指标；没有证明存在通用 harmlessness-preserving recipe。 Locator: https://arxiv.org/html/2606.04413v1 §2 Evaluation Suite; §§4–6 results; Appendix A | Disclosed — training covers Haiku 4.5, Qwen3-30B-A3B and Qwen3.5-35B-A3B; evaluation names Jinx/Qwen3-32B, Sonnet 4/4.5, Opus 4.5 and Abliterated Qwen3.5-35B-A3B | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §2/Appendix A define capability, refusal, compliance, misalignment, sandbagging, sycophancy, steerability and character evaluations |
| SF-2026-ARXIV-2606-04415 | Disclosed — §4 只对 Ascend 910C/CloudMatrix384、所列模型、W8A8、1K input 与1K/4K output及 TTFT/TPOT 门槛证明原型效果；不证明其他 NPU、精度或 SLO。 Locator: https://arxiv.org/pdf/2606.04415v1 §4.1 Experimental Setup; §4.2 End-to-end Results; Table 2 | Disclosed — DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1 (large MoE) and Qwen2.5-7B | Disclosed — Ascend 910C and CloudMatrix384 (384 cards) | Disclosed — W8A8 for the reported large DeepSeek-R1 slice | Disclosed — 1K input tokens | Disclosed — 1K or 4K output tokens | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Disclosed — TTFT <=1 s and TPOT <=50 ms | Disclosed — §4 reports throughput under TTFT/TPOT constraints; AISBench is named for the distill-model workload, other slices are not version-pinned |
| SF-2026-ARXIV-2606-04425 | Disclosed — §5 在162个跨会话 case 中分别测 WSR、IR、AR 与 E2E-ASR，证明瓶颈可出现在不同阶段；它没有评估所有持久介质或给出已验证的通用 defense。 Locator: https://arxiv.org/html/2606.04425v1 §5 Experiments; §§5.1–5.7 | Not Disclosed — exact-v1 evaluation/setup text does not bind the evaluated model/version | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §§5.1–5.2 decompose 162 cases into write success, context incorporation, activation and end-to-end success |
| SF-2026-ARXIV-2606-04459 | Disclosed — PDF §5 只在约50组 ranking 与指定拟合尝试下证明可区分/近似暴露；没有证明能恢复完整权重或对所有解码/API 变体都不可伪造。 Locator: https://arxiv.org/pdf/2606.04459v1 §4 practical fitting (50 rankings; 3/5 attempts); §5 approximate parameter exposure | Disclosed — §5 evaluates Pythia-70m(-dedup) and OLMo-3-8B | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §4 reports fitting over 50 rankings and five attempts; §5 separately measures top-k ranking/parameter-recovery behavior |
| SF-2026-ARXIV-2606-04522 | Disclosed — 跨所列 ANN algorithms/datasets 的实验只证明 Recall@k 与 distance quality/下游 utility 可分离，以及替代 metric 改变效率结论；没有证明 1/Ratio@k 适合所有语义任务。 Locator: https://arxiv.org/html/2606.04522v1 §§5–6 Experimental Setup and Results; §6.3 RAG Experiments | Not Disclosed — exact-v1 evaluation/setup text does not bind the evaluated model/version | Disclosed — Intel i7-11700K, 32 GB RAM, AVX-512, Ubuntu 22.04 and gcc 11.4 | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §§5–6 measure recall-ratio divergence and downstream classification/RAG effectiveness |
| SF-2026-ARXIV-2606-04557 | Disclosed — §§3–4 在指定 Qwen3-8B、数据集和 retrieval/oracle 选择下证明百万 token 集合可扩展及 token savings；没有证明跨模型可移植或线上并发延迟。 Locator: https://arxiv.org/html/2606.04557v1 §3 Experimental Setup; §4 Experimental Results | Disclosed — Qwen3-8B | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Disclosed — bfloat16 weights with fp32 Adam optimizer state | Disclosed — packed 8,192-token sequences for the named long-context run | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Disclosed — task-specific training batches are published; no universal batch applies | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §4 reports QA accuracy, prompt-token use and cartridge/RAG comparisons |
| SF-2026-ARXIV-2606-04581 | Disclosed — §VI 只在所列模型对、A100 edge server 与模拟网络条件下证明 sum token goodput；没有证明公网抖动、生产 tail SLO 或不同 tokenizer 的效果。 Locator: https://arxiv.org/html/2606.04581v1 §VI Experimental Results; §VI-A Experiment Settings | Disclosed — TinyLlama-1.1B/Llama-2-7B and Qwen3.5-0.8B/Qwen3.5-27B pairs | Disclosed — edge server uses one NVIDIA A100 GPU | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Not Disclosed — exact-v1 evaluation/setup text does not bind the evaluator/metric version |
| SF-2026-ARXIV-2606-04594 | Disclosed — §5 的 pass@1/pass@5 只对作者构造的真实 silent-error benchmark 与指定 backend/模型成立；没有证明 reference 自身无错或覆盖所有 nondeterminism。 Locator: https://arxiv.org/html/2606.04594v1 §5 Evaluation; §§5.1–5.7 | Disclosed — Claude Sonnet 4.5 is the Ekka and baseline backend | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — BF16/FP8 is motivation, not the evaluation setup | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — We measure Mapping Accuracy : the coverage percentage of ground-truth mapping in the mapping generated by the agent. |
| SF-2026-ARXIV-2606-04628 | Disclosed — Qwen3-8B Q4 probes 只证明特定 block 位置/分组会改变任务成功率以及这些 primitives 可调节位置；没有证明通用长期记忆质量或多租户隔离。 Locator: https://arxiv.org/html/2606.04628v1 §3 Experiments; §§3.1–3.2 | Disclosed — Qwen3-8B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3 and Qwen3-14B | Disclosed — Ollama on one RTX 5080 | Disclosed — Q4 quantization | Disclosed — default all-MiniLM-L6-v2 relevance embedding truncates each block at 256 tokens; the evaluated LLM prompt length is not fixed | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Not Disclosed — exact-v1 evaluation/setup text does not bind the evaluator/metric version |
| SF-2026-ARXIV-2606-04769 | Disclosed — measurement 只对采样的真实 MCP repositories 与分类 taxonomy 证明 DCI 存在并可被检测；没有证明 classifier 能替代 sandbox/runtime enforcement。 Locator: https://arxiv.org/html/2606.04769v1 §V Real-world Measurement; §§V-A–V-D | Disclosed — claude-sonnet-4-5-20250929-thinking is DCIChecker | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Disclosed — To ensure deterministic and reproducible outputs, we use claude-sonnet-4-5-20250929-thinking with temperature set to 0 0 , top-p set to 1.0 1.0 , and a maximum generation length of 4,096 4,096 tokens. | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §IV combines author analysis, manual mutation tests and repository-scale measurement |
| SF-2026-ARXIV-2606-04778 | Disclosed — §4 在三类7B/8B instruct models和指定 harmfulness suites 上证明中途脆弱性与训练增益；没有证明对所有 white-box activation intervention 或更大模型成立。 Locator: https://arxiv.org/html/2606.04778v1 §4 Experiments and Analysis | Disclosed — Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3 and Qwen2.5-7B-Instruct | Disclosed — Appendix A.5 uses one RTX 3090 24 GB | Disclosed — 4-bit quantization and bf16 training | Disclosed — maximum sequence length 2,048 | Disclosed — Appendix A.4 caps new tokens at 256 for augmentation and evaluation | Disclosed — Appendix A reports per-device and effective training batches | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §4 measures attack success/harmfulness on AdvBench, HarmBench, HEx-PHI and JailbreakBench |
| SF-2026-ARXIV-2606-04799 | Disclosed — 作者案例只证明统一模型支持所测 RCA/query workflow；没有证明任意 vendor schema 自动可对齐或 ontology 长期无漂移。 Locator: https://arxiv.org/html/2606.04799v1 §VI Evaluation | Disclosed — The LLM backbone we use is Qwen3-max. | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — For quality evaluation, we report location accuracy with redundancy penalty (LA), type accuracy (TA), and reasoning score (RS). |
| SF-2026-ARXIV-2606-04850 | Disclosed — §V 的 simulation 只证明指定 workload、processor model、uncertainty distribution 与 cost function 下的联合方案；没有证明真实 chip tape-out、跨 workload 稳健性或生产 SLO。 Locator: https://arxiv.org/html/2606.04850v1 §V Simulation Results; §§V-A–V-C | Not Applicable — distribution-grid accelerator co-design simulation, not a model-version benchmark | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §V simulates latency/energy/resource outcomes under nominal and uncertain mappings |
| SF-2026-ARXIV-2606-04903 | Disclosed — 论文给出 healthcare billing 与 vulnerability disclosure 两个 appropriate-domain 实现及语义论证；没有证明开放世界任务能被完整 ontologize，也未证明 LLM 感知输入正确。 Locator: https://arxiv.org/html/2606.04903v1 §2.3 Derivation of System Invariants; Appendix A.3.2 Preservation of Base Results | Not Applicable — formal ontology/executable-semantics argument | Not Applicable — no hardware claim | Not Applicable — no precision claim | Not Applicable — no token-length claim | Not Applicable — no generation-length claim | Not Applicable — no batching claim | Not Applicable — no request-concurrency claim | Not Applicable — no SLO claim | Disclosed — formal definitions/proofs plus bounded worked cases; no empirical model score |
| SF-2026-ARXIV-2606-04908 | Disclosed — 实验只对 AMD EPYC 9654、768GB DDR5、A100 40GB 与指定 AFA/network configuration 的 throughput/latency 成立；不证明通用 filesystem semantics 或 failure recovery。 Locator: https://arxiv.org/html/2606.04908v1 §5. Evaluation; §5.1 Experimental Setup | Not Applicable — GPU-native storage microbenchmark | Disclosed — AMD EPYC 9654, 768 GB DDR5, NVIDIA A100 40 GB | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — storage throughput/latency and end-to-end GPU-AFA measurements |
| SF-2026-ARXIV-2606-04923 | Disclosed — §4/appendices 只证明所注入 biases 可被发现/利用以及 detector 在该环境中的表现；没有证明真实生产 judge 的全部 latent bias 被覆盖。 Locator: https://arxiv.org/html/2606.04923v1 §2.5; §4.2; Appendices B, D and F | Disclosed — Qwen3-4B trained with GRPO on HealthBench and VerInstruct | Disclosed — Appendix F uses NVIDIA H100 80 GB GPUs | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §§2.5/4.2 and Appendices B/D/F compare reward-hacking detection, rubric validity and downstream behavior |
| SF-2026-ARXIV-2606-04929 | Disclosed — 实验只在列出的 Llama/Qwen、poison budgets 与 SFT→DPO/LoRA 配置上证明 additive/cross-stage interaction；没有覆盖完整 RLHF 或现实供应链攻击率。 Locator: https://arxiv.org/html/2606.04929v1 §4 Experimental Setup; Appendix D.2 Evaluation Details; Appendix E | Disclosed — Llama-3 8B and Qwen3 1.7B/4B/8B | Disclosed — NVIDIA H100 for fine-tuning/LoRA runs | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — (1) We measure attack success rate (ASR) as the fraction of triggered prompts on which the final policy produces harmful, compliant responses (by manual inspection) to a heldout test set of harmful questions. |
| SF-2026-ARXIV-2606-05004 | Disclosed — 作者实验只在指定 prompts/models/privacy attack 与 GPT-5.2 attribute inference slice 上报告 utility/cost；没有给出对任意 side channel 或恶意 provider 的 cryptographic secrecy。 Locator: https://arxiv.org/html/2606.05004v1 §7 Experiment; Appendix G Experiment; §5 Privacy Analysis for the formal claim | Disclosed — GPT-5.2 attribute attacker; Appendix G names utility/discrimination models | Disclosed — 96-core Ubuntu server, 128 GB RAM, two A100 GPUs | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Disclosed — We set sampling ratio α = 10 \alpha=10 , privacy parameter ϵ = 1 \epsilon=1 , and batch size B = 5000 B=5000 unless specified. | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — Appendix G defines utility metrics, GPT-4o QA judging, privacy attack success and query/computation cost |
| SF-2026-ARXIV-2606-05029 | Disclosed — 论文提供方法论分析而非新的模型 benchmark；它证明的是各策略存在可枚举的因果威胁，不证明某一策略在所有研究问题上失效。 Locator: https://arxiv.org/html/2606.05029v1 §6 Validity Profiles for Foundation Model Research | Not Applicable — evaluation-validity framework | Not Applicable — no hardware claim | Not Applicable — no precision claim | Not Applicable — no token-length claim | Not Applicable — no generation-length claim | Not Applicable — no runtime batch claim | Not Applicable — no concurrency claim | Not Applicable — no SLO claim | Disclosed — checks estimand, identification assumptions, measurement and transport; no new benchmark score |
| SF-2026-ARXIV-2606-05037 | Disclosed — N=30/cell、3 models、10 adversarial tasks 的 pilot 只证明 Anthropic models 上显著提升且 gpt-4o lift 不显著；不能外推为所有 API 或 agent。 Locator: https://arxiv.org/html/2606.05037v1 §5 Evaluation; §§5.1–5.4 | Disclosed — claude-haiku-4-5, claude-sonnet-4-6 and gpt-4o-mini | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Applicable — N=30 per model/mode cell is sample size, not runtime batch | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §5 records logical success, billed tokens, retries and recovery actions after answer-leakage audit |
| SF-2026-ARXIV-2606-05043 | Disclosed — 案例只证明 checkout 子协议可表达并与所测 UCP implementation 互通；没有覆盖 UCP 全部域、故障恢复或生产规模。 Locator: https://arxiv.org/html/2606.05043v1 §6 Evaluation | Not Applicable — protocol/interoperability evaluation | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — four explicit protocol criteria applied to executable artifacts and sample implementations |
| SF-2026-ARXIV-2606-05122 | Disclosed — 三 benchmark、160 examples、Qwen3-4B-Base 结果只证明所测 judge/attributes 上校准改善且 answer quality 保持；不等于事实正确性或模型知道未知。 Locator: https://arxiv.org/html/2606.05122v1 §4 Experiments; Appendix A Training Configuration | Disclosed — Qwen3-4B-Base | Disclosed — All reported training runs use four RTX PRO 6000 GPUs with 96 GB memory each, bf16 precision, VeRL for GRPO training, and vLLM for rollout generation. | Disclosed — All reported training runs use four RTX PRO 6000 GPUs with 96 GB memory each, bf16 precision, VeRL for GRPO training, and vLLM for rollout generation. | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Disclosed — Appendix A fixes maximum response length at 8,192 tokens | Disclosed — Appendix A gives stage-specific batches | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §4.1 defines judge agreement, calibration and response-quality metrics |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | score_7_9 | not_selected | — | — | Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY |
| SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | score_7_9 | not_selected | — | — | Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT |
| SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Covert Influence Between Language Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS |
| SF-ULTRAEP | score_7_9 | not_selected | — | — | UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing remains evidence-complete after canonical owner transfer with V2 score 8 and owner MODEL-MOE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-ULTRAEP |
| SF-PROOF-CARRYING-ACTIONS | score_7_9 | not_selected | — | — | Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-PROOF-CARRYING-ACTIONS |
| SF-EVALSTOP | score_7_9; forced_review; potential_books_delta | not_selected | — | — | EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-EVALSTOP |
| SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | score_7_9 | not_selected | — | — | Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS |
| SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | score_7_9 | not_selected | — | — | Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR |
| SF-ROBOT-BENCHMARK-AUDIT | score_7_9 | not_selected | — | — | What Are We Actually Benchmarking in Robot Manipulation? remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-ROBOT-BENCHMARK-AUDIT |
| SF-AGENT-DATA-CURATION-HARNESS | score_7_9 | not_selected | — | — | Can Generalist Agents Automate Data Curation? remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-AGENT-DATA-CURATION-HARNESS |
| SF-RL-EXCURSIONS-PRETRAINING | score_7_9 | not_selected | — | — | RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-RL-EXCURSIONS-PRETRAINING |
| SF-INTERVENTION-TIMING-RELIABILITY | score_7_9 | not_selected | — | — | The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-INTERVENTION-TIMING-RELIABILITY |
| SF-LAZYATTENTION | score_7_9 | selected | DA-POSITION-INDEPENDENT-KV-STATE | — | Selected as one of three non-overlapping frontier units: training cross-stage resource ownership, agent runtime authority, or reusable KV positional state. | analysis:DA-POSITION-INDEPENDENT-KV-STATE |
| SF-OCL-EXECUTION-BOUNDARY | score_7_9 | not_selected | — | — | Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-OCL-EXECUTION-BOUNDARY |
| SF-AGENT-MEMORY-GENERALITY | score_7_9 | not_selected | — | — | Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-AGENT-MEMORY-GENERALITY |
| SF-DIGITAL-APPRENTICE-CONTROL-PLANE | score_7_9 | not_selected | — | — | The Digital Apprentice: A Framework for Human-Directed Agentic AI Development remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-DIGITAL-APPRENTICE-CONTROL-PLANE |
| SF-2026-ARXIV-2606-04329 | score_7_9 | not_selected | — | — | From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04329 |
| SF-2026-ARXIV-2606-04384 | score_7_9 | not_selected | — | — | Revisiting Privacy Amplification by Subsampling in Selective Release DPSGD remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04384 |
| SF-2026-ARXIV-2606-04402 | forced_review | not_selected | — | — | Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04402 |
| SF-2026-ARXIV-2606-04413 | forced_review | not_selected | — | — | (Mis)generalization of Helpful-only Fine-tuning remains evidence-complete after canonical owner transfer with V2 score 6 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04413 |
| SF-2026-ARXIV-2606-04415 | score_7_9 | selected | DA-20260604-NPU-VIRTUALIZATION | — | 这是 INFER-PD-DISAGGREGATION 与 PLATFORM-RESOURCE-SCHEDULING 的 Direct Evolution：从设备级 allocation 细化为阶段级可重绑定资源。 Full-frontier selection: among the eight 3/3/3 families, this is the only inference-hardware lane that turns prefill/decode phase identity into a rebindable NPU resource contract; it is non-overlapping with the selected post-training-security and multi-agent-state lanes. The exact-v1 result is bounded to Ascend 910C/CloudMatrix384 and the stated TTFT/TPOT slices. Mechanism owner: FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。 | analysis:DA-20260604-NPU-VIRTUALIZATION |
| SF-2026-ARXIV-2606-04425 | score_7_9 | not_selected | — | — | What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04425 |
| SF-2026-ARXIV-2606-04459 | forced_review | not_selected | — | — | Token Rankings are Unforgeable Language Model Signatures remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04459 |
| SF-2026-ARXIV-2606-04522 | score_7_9 | not_selected | — | — | ANN Search: Recall What Matters remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04522 |
| SF-2026-ARXIV-2606-04557 | score_7_9 | not_selected | — | — | Cartridges at Scale: Training Modular KV Caches over Large Document Collections remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04557 |
| SF-2026-ARXIV-2606-04581 | score_7_9 | not_selected | — | — | Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04581 |
| SF-2026-ARXIV-2606-04594 | score_7_9 | not_selected | — | — | Ekka: Automated Diagnosis of Silent Errors in LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04594 |
| SF-2026-ARXIV-2606-04628 | score_7_9 | not_selected | — | — | RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04628 |
| SF-2026-ARXIV-2606-04769 | score_7_9 | not_selected | — | — | Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04769 |
| SF-2026-ARXIV-2606-04778 | score_7_9 | not_selected | — | — | Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04778 |
| SF-2026-ARXIV-2606-04799 | score_7_9 | not_selected | — | — | UModel: An Agent-Ready Observability Data Modeling Method at Scale remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04799 |
| SF-2026-ARXIV-2606-04850 | forced_review | not_selected | — | — | Uncertainty-Aware End-to-End Co-Design of Neural Network Processors: From Training and Mapping to Fabrication remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04850 |
| SF-2026-ARXIV-2606-04903 | forced_review | not_selected | — | — | Provably Auditable and Safe LLM Agents from Human-Authored Ontologies remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04903 |
| SF-2026-ARXIV-2606-04908 | forced_review | not_selected | — | — | GNStor: Design of GPU-Native High-Performance Remote All-Flash Array remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04908 |
| SF-2026-ARXIV-2606-04923 | score_7_9 | not_selected | — | — | Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-04923 |
| SF-2026-ARXIV-2606-04929 | score_7_9; potential_books_delta | selected | DA-20260604-CROSS-STAGE-POISONING | — | 这是 TRAIN-SFT→TRAIN-DPO 的 Direct Evolution：安全 owner 从单个 trainer 上移到整个 post-training checkpoint chain。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that makes checkpoint handoff across SFT and preference optimization a security state channel; existing single-stage data-poisoning prose does not own the cross-stage orchestrator. It is non-overlapping with NPU phase virtualization and multi-agent public-state projection. Mechanism owner: 论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。 | analysis:DA-20260604-CROSS-STAGE-POISONING |
| SF-2026-ARXIV-2606-05004 | forced_review | not_selected | — | — | SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05004 |
| SF-2026-ARXIV-2606-05029 | score_7_9 | not_selected | — | — | Validity Threats for Foundation Model Research remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05029 |
| SF-2026-ARXIV-2606-05037 | score_7_9 | not_selected | — | — | Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05037 |
| SF-2026-ARXIV-2606-05043 | score_7_9 | not_selected | — | — | Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05043 |
| SF-2026-ARXIV-2606-05122 | score_7_9 | not_selected | — | — | Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-05122 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:start -->
Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:end -->

<!-- analysis-decision:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:start -->
Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:end -->

<!-- analysis-decision:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:start -->
Covert Influence Between Language Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:end -->

<!-- analysis-decision:SF-ULTRAEP:start -->
UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing remains evidence-complete after canonical owner transfer with V2 score 8 and owner MODEL-MOE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-ULTRAEP:end -->

<!-- analysis-decision:SF-PROOF-CARRYING-ACTIONS:start -->
Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-PROOF-CARRYING-ACTIONS:end -->

<!-- analysis-decision:SF-EVALSTOP:start -->
EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-EVALSTOP:end -->

<!-- analysis-decision:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:start -->
Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:end -->

<!-- analysis-decision:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:start -->
Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:end -->

<!-- analysis-decision:SF-ROBOT-BENCHMARK-AUDIT:start -->
What Are We Actually Benchmarking in Robot Manipulation? remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-ROBOT-BENCHMARK-AUDIT:end -->

<!-- analysis-decision:SF-AGENT-DATA-CURATION-HARNESS:start -->
Can Generalist Agents Automate Data Curation? remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-AGENT-DATA-CURATION-HARNESS:end -->

<!-- analysis-decision:SF-RL-EXCURSIONS-PRETRAINING:start -->
RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-PRETRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-RL-EXCURSIONS-PRETRAINING:end -->

<!-- analysis-decision:SF-INTERVENTION-TIMING-RELIABILITY:start -->
The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-INTERVENTION-TIMING-RELIABILITY:end -->

<!-- analysis:DA-POSITION-INDEPENDENT-KV-STATE:start -->
### 从 Position-bound Prefix Cache 到延迟位置化的可复用文档状态

传统 prefix cache 把 token 内容与当前位置一起固化，顺序或插入位置变化就需要重算；这在位置稳定时最简单可靠。LazyAttention 把 reusable document 的位置编码推迟到 attention 计算，使 cache identity 更接近 position-agnostic content state，再由请求态完成位置变换。它提高跨位置复用机会，却新增 deferred-RoPE kernel、composition correctness、cache identity 与 fallback；其 Zipf 分析和作者实现只说明受测分布/模型下的机制，不证明任意 attention architecture、并发或生产 SLO。
<!-- analysis:DA-POSITION-INDEPENDENT-KV-STATE:end -->

<!-- analysis-decision:SF-OCL-EXECUTION-BOUNDARY:start -->
Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-OCL-EXECUTION-BOUNDARY:end -->

<!-- analysis-decision:SF-AGENT-MEMORY-GENERALITY:start -->
Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-AGENT-MEMORY-GENERALITY:end -->

<!-- analysis-decision:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:start -->
The Digital Apprentice: A Framework for Human-Directed Agentic AI Development remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04329:start -->
From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04329:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04384:start -->
Revisiting Privacy Amplification by Subsampling in Selective Release DPSGD remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04384:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04402:start -->
Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04402:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04413:start -->
(Mis)generalization of Helpful-only Fine-tuning remains evidence-complete after canonical owner transfer with V2 score 6 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04413:end -->

<!-- analysis:DA-20260604-NPU-VIRTUALIZATION:start -->
这是 INFER-PD-DISAGGREGATION 与 PLATFORM-RESOURCE-SCHEDULING 的 Direct Evolution：从设备级 allocation 细化为阶段级可重绑定资源。 Full-frontier selection: among the eight 3/3/3 families, this is the only inference-hardware lane that turns prefill/decode phase identity into a rebindable NPU resource contract; it is non-overlapping with the selected post-training-security and multi-agent-state lanes. The exact-v1 result is bounded to Ascend 910C/CloudMatrix384 and the stated TTFT/TPOT slices. Mechanism owner: FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。
<!-- analysis:DA-20260604-NPU-VIRTUALIZATION:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04425:start -->
What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04425:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04459:start -->
Token Rankings are Unforgeable Language Model Signatures remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04459:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04522:start -->
ANN Search: Recall What Matters remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04522:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04557:start -->
Cartridges at Scale: Training Modular KV Caches over Large Document Collections remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04557:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04581:start -->
Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04581:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04594:start -->
Ekka: Automated Diagnosis of Silent Errors in LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04594:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04628:start -->
RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04628:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04769:start -->
Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04769:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04778:start -->
Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04778:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04799:start -->
UModel: An Agent-Ready Observability Data Modeling Method at Scale remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04799:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04850:start -->
Uncertainty-Aware End-to-End Co-Design of Neural Network Processors: From Training and Mapping to Fabrication remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04850:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04903:start -->
Provably Auditable and Safe LLM Agents from Human-Authored Ontologies remains evidence-complete after canonical owner transfer with V2 score 5 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04903:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04908:start -->
GNStor: Design of GPU-Native High-Performance Remote All-Flash Array remains evidence-complete after canonical owner transfer with V2 score 6 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04908:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-04923:start -->
Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-04923:end -->

<!-- analysis:DA-20260604-CROSS-STAGE-POISONING:start -->
这是 TRAIN-SFT→TRAIN-DPO 的 Direct Evolution：安全 owner 从单个 trainer 上移到整个 post-training checkpoint chain。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that makes checkpoint handoff across SFT and preference optimization a security state channel; existing single-stage data-poisoning prose does not own the cross-stage orchestrator. It is non-overlapping with NPU phase virtualization and multi-agent public-state projection. Mechanism owner: 论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。
<!-- analysis:DA-20260604-CROSS-STAGE-POISONING:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05004:start -->
SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models remains evidence-complete after canonical owner transfer with V2 score 6 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05004:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05029:start -->
Validity Threats for Foundation Model Research remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05029:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05037:start -->
Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05037:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05043:start -->
Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05043:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-05122:start -->
Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-05122:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L74 | books/part-07-agent/83-mcp.md#L115 | existing:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | delta:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY |
| SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#section-66-evaluation-system | books/part-06-ai-infrastructure/67-monitoring.md section:67-monitoring#L1; books/part-06-ai-infrastructure/72-security.md section:72-security#L1 | existing:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | delta:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT | Direct Evolution | No Change — Existing Coverage | books-review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT |
| SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-07-agent/78-tool-calling.md#L1 | existing:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | delta:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | Layering / Dependency | Integrate | books-review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS |
| SF-ULTRAEP | MODEL-MOE | books/part-02-model/21-moe.md#L1 | books/part-04-training-system/36-distributed-training.md#L441; books/part-05-inference-system/56-inference-scheduling.md#L744 | existing:SF-ULTRAEP | delta:SF-ULTRAEP | Layering / Dependency | No Change — Existing Coverage | books-review:SF-ULTRAEP |
| SF-PROOF-CARRYING-ACTIONS | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L474 | books/part-07-agent/78-tool-calling.md#L202; books/part-07-agent/84-agent-platform.md#L126 | existing:SF-PROOF-CARRYING-ACTIONS | delta:SF-PROOF-CARRYING-ACTIONS | Layering / Dependency | No Change — Existing Coverage | books-review:SF-PROOF-CARRYING-ACTIONS |
| SF-EVALSTOP | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#section-31-rlhf | books/part-04-training-system/33-grpo.md section:33-grpo#L1; books/part-06-ai-infrastructure/66-evaluation-system.md section:66-evaluation-system#L1 | existing:SF-EVALSTOP | delta:SF-EVALSTOP | Direct Evolution | Integrate | books-review:SF-EVALSTOP |
| SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L474 | books/part-06-ai-infrastructure/68-logging.md#L18; books/part-07-agent/78-tool-calling.md#L18 | existing:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | delta:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS | Principle Reuse | No Change — Existing Coverage | books-review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS |
| SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | delta:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR | Layering / Dependency | No Change — Existing Coverage | books-review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR |
| SF-ROBOT-BENCHMARK-AUDIT | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#section-66-evaluation-system | books/part-06-ai-infrastructure/67-monitoring.md section:67-monitoring#L1; books/part-06-ai-infrastructure/72-security.md section:72-security#L1 | existing:SF-ROBOT-BENCHMARK-AUDIT | delta:SF-ROBOT-BENCHMARK-AUDIT | Direct Evolution | No Change — Existing Coverage | books-review:SF-ROBOT-BENCHMARK-AUDIT |
| SF-AGENT-DATA-CURATION-HARNESS | TRAIN-DATA | books/part-04-training-system/27-data.md#section-27-data | books/part-04-training-system/28-pretraining.md section:28-pretraining#L1; books/part-06-ai-infrastructure/66-evaluation-system.md section:66-evaluation-system#L1 | existing:SF-AGENT-DATA-CURATION-HARNESS | delta:SF-AGENT-DATA-CURATION-HARNESS | Direct Evolution | No Change — Existing Coverage | books-review:SF-AGENT-DATA-CURATION-HARNESS |
| SF-RL-EXCURSIONS-PRETRAINING | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#section-28-pretraining | books/part-04-training-system/27-data.md section:27-data#L1; books/part-04-training-system/35-checkpoint.md section:35-checkpoint#L1 | existing:SF-RL-EXCURSIONS-PRETRAINING | delta:SF-RL-EXCURSIONS-PRETRAINING | Principle Reuse | No Change — Existing Coverage | books-review:SF-RL-EXCURSIONS-PRETRAINING |
| SF-INTERVENTION-TIMING-RELIABILITY | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L934 | books/part-06-ai-infrastructure/67-monitoring.md#L18; books/part-06-ai-infrastructure/72-security.md#L474 | existing:SF-INTERVENTION-TIMING-RELIABILITY | delta:SF-INTERVENTION-TIMING-RELIABILITY | Direct Evolution | No Change — Existing Coverage | books-review:SF-INTERVENTION-TIMING-RELIABILITY |
| SF-LAZYATTENTION | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L627 | books/part-05-inference-system/44-decode.md#L103; books/part-05-inference-system/47-pagedattention.md#L59 | existing:SF-LAZYATTENTION | delta:SF-LAZYATTENTION | Direct Evolution | No Change — Existing Coverage | books-review:SF-LAZYATTENTION |
| SF-OCL-EXECUTION-BOUNDARY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L474 | books/part-07-agent/78-tool-calling.md#L202; books/part-07-agent/84-agent-platform.md#L126 | existing:SF-OCL-EXECUTION-BOUNDARY | delta:SF-OCL-EXECUTION-BOUNDARY | Layering / Dependency | No Change — Existing Coverage | books-review:SF-OCL-EXECUTION-BOUNDARY |
| SF-AGENT-MEMORY-GENERALITY | AGENT-MEMORY | books/part-07-agent/77-memory.md#L624 | books/part-07-agent/76-rag.md#L202; books/part-07-agent/81-workflow.md#L36 | existing:SF-AGENT-MEMORY-GENERALITY | delta:SF-AGENT-MEMORY-GENERALITY | Principle Reuse | No Change — Existing Coverage | books-review:SF-AGENT-MEMORY-GENERALITY |
| SF-DIGITAL-APPRENTICE-CONTROL-PLANE | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-DIGITAL-APPRENTICE-CONTROL-PLANE | delta:SF-DIGITAL-APPRENTICE-CONTROL-PLANE | Alternative Branch | No Change — Existing Coverage | books-review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE |
| SF-2026-ARXIV-2606-04329 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L51 | books/part-07-agent/76-rag.md#L483; books/part-07-agent/78-tool-calling.md#L366 | existing:SF-2026-ARXIV-2606-04329 | delta:SF-2026-ARXIV-2606-04329 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04329 |
| SF-2026-ARXIV-2606-04384 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L118 | books/part-06-ai-infrastructure/71-multi-tenant.md#L84; books/part-06-ai-infrastructure/73-production-best-practice.md#L37 | existing:SF-2026-ARXIV-2606-04384 | delta:SF-2026-ARXIV-2606-04384 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04384 |
| SF-2026-ARXIV-2606-04415 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L14 | books/part-05-inference-system/54-gpu-memory.md#L369; books/part-05-inference-system/56-inference-scheduling.md#L843 | existing:SF-2026-ARXIV-2606-04415 | delta:SF-2026-ARXIV-2606-04415 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04415 |
| SF-2026-ARXIV-2606-04425 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L51 | books/part-07-agent/76-rag.md#L551; books/part-07-agent/78-tool-calling.md#L424 | existing:SF-2026-ARXIV-2606-04425 | delta:SF-2026-ARXIV-2606-04425 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04425 |
| SF-2026-ARXIV-2606-04522 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L209 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L334 | existing:SF-2026-ARXIV-2606-04522 | delta:SF-2026-ARXIV-2606-04522 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04522 |
| SF-2026-ARXIV-2606-04557 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L640 | books/part-05-inference-system/44-decode.md#L305; books/part-05-inference-system/46-continuous-batching.md#L104 | existing:SF-2026-ARXIV-2606-04557 | delta:SF-2026-ARXIV-2606-04557 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04557 |
| SF-2026-ARXIV-2606-04581 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L33 | books/part-05-inference-system/47-pagedattention.md#L3; books/part-05-inference-system/49-tensorrt-llm.md#L1047 | existing:SF-2026-ARXIV-2606-04581 | delta:SF-2026-ARXIV-2606-04581 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04581 |
| SF-2026-ARXIV-2606-04594 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L105 | books/part-06-ai-infrastructure/68-logging.md#L119; books/part-06-ai-infrastructure/70-cost.md#L235 | existing:SF-2026-ARXIV-2606-04594 | delta:SF-2026-ARXIV-2606-04594 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04594 |
| SF-2026-ARXIV-2606-04628 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L31 | books/part-07-agent/76-rag.md#L589; books/part-07-agent/78-tool-calling.md#L422 | existing:SF-2026-ARXIV-2606-04628 | delta:SF-2026-ARXIV-2606-04628 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04628 |
| SF-2026-ARXIV-2606-04769 | AGENT-MCP | books/part-07-agent/83-mcp.md#L145 | books/part-07-agent/82-multi-agent.md#L571; books/part-07-agent/84-agent-platform.md#L784 | existing:SF-2026-ARXIV-2606-04769 | delta:SF-2026-ARXIV-2606-04769 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04769 |
| SF-2026-ARXIV-2606-04778 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L243 | books/part-06-ai-infrastructure/71-multi-tenant.md#L84; books/part-06-ai-infrastructure/73-production-best-practice.md#L89 | existing:SF-2026-ARXIV-2606-04778 | delta:SF-2026-ARXIV-2606-04778 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04778 |
| SF-2026-ARXIV-2606-04799 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L95 | books/part-06-ai-infrastructure/68-logging.md#L44; books/part-06-ai-infrastructure/70-cost.md#L235 | existing:SF-2026-ARXIV-2606-04799 | delta:SF-2026-ARXIV-2606-04799 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04799 |
| SF-2026-ARXIV-2606-04923 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L2282 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L334 | existing:SF-2026-ARXIV-2606-04923 | delta:SF-2026-ARXIV-2606-04923 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04923 |
| SF-2026-ARXIV-2606-04929 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L48 | books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L195 | existing:SF-2026-ARXIV-2606-04929 | delta:SF-2026-ARXIV-2606-04929 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-04929 |
| SF-2026-ARXIV-2606-05029 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1267 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L380 | existing:SF-2026-ARXIV-2606-05029 | delta:SF-2026-ARXIV-2606-05029 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05029 |
| SF-2026-ARXIV-2606-05037 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L251 | books/part-07-agent/77-memory.md#L1340; books/part-07-agent/79-planning.md#L329 | existing:SF-2026-ARXIV-2606-05037 | delta:SF-2026-ARXIV-2606-05037 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05037 |
| SF-2026-ARXIV-2606-05043 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L277 | books/part-07-agent/81-workflow.md#L796; books/part-07-agent/83-mcp.md#L209 | existing:SF-2026-ARXIV-2606-05043 | delta:SF-2026-ARXIV-2606-05043 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05043 |
| SF-2026-ARXIV-2606-05122 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1133 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L245 | existing:SF-2026-ARXIV-2606-05122 | delta:SF-2026-ARXIV-2606-05122 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05122 |

<!-- existing:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:start -->`AGENT-PLATFORM` 当前与该机制最接近的命题是：因此，模型负责产生语义判断与 action proposal，Agent Runtime 负责状态转换和编排，Tool/Environment 拥有真实副作用，Policy plane 决定哪些转换被允许。只有 terminal evidence 满足任务 contract，才能把“请求成功”提升为“任务完成”。 相邻章节对 handoff 的约束是：这一变化降低了长期连接、横向扩缩容和代理转发对协议状态的耦合，同时把 version/capability contract 提到每个请求。代价是每次调用都有元数据开销， server 必须显式设计 handle 的 ownership、TTL、撤销和幂等性；断开的响应流 会失去 in-flight request，重发时必须使用新的 request ID，也不能把网络失败 误当成工具副作用未提交。对 Agent Platform 而言，这加强了本书既有 边界：MCP 可以协商连接能力，却仍不替代 workflow 的 durable state、重试策略 和 side-effect recovery。<!-- existing:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:end -->

<!-- delta:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:start -->把 model 与 harness 分别升级能保持模块自治，却会让 belief、capability 和 goal 在接口处语义漂移。该 position 以 interface contract 组织 goal validity、action archetype、tool instance 与 invocation failure 四级结构，要求持久状态跨 session/版本守恒。 论文提出 architecture/evaluation agenda，没有实现或 benchmark；它支持 long-running Agent 需要 joint conformance，不证明这四层已经充分。contract versioning 和兼容测试有成本，短期无持久状态任务仍可使用平面 action loop。<!-- delta:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:end -->

<!-- books-review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:start -->`Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents` 与 `AGENT-PLATFORM` 的关系判定为 `Layering / Dependency`。比较 `books/part-07-agent/84-agent-platform.md#L74` 与 `books/part-07-agent/83-mcp.md#L115` 后，决定为 `No Change — Existing Coverage`：该 exact-v1 的机制 `把 model 与 harness 分别升级能保持模块自治，却会让 belief、capability 和 goal 在接口处语义漂移。该 position 以 interface contract 组织 goal validity、action archetype、tool instance 与 invocation failure 四级结构，要求持久状态跨 session/版本守恒。 论文提出 architecture/evaluation agenda，没有实现或 benchmark；它支持 long-running Agent 需要 joint conformance，不证明这四层已经充分。contract versioning 和兼容测试有成本，短期无持久状态任务仍可使用平面 action loop。` 已被现有命题或相邻 handoff 覆盖；作者结果只增加受限实例，而 `把 model 与 harness 分别升级能保持模块自治，却会让 belief、capability 和 goal 在接口处语义漂移。该 position 以 interface contract 组织 goal validity、action archetype、tool instance 与 invocation failure 四级结构，要求持久状态跨 session/版本守恒。 论文提出 architecture/evaluation agenda，没有实现或 benchmark；它支持 long-running Agent 需要 joint conformance，不证明这四层已经充分。contract versioning 和兼容测试有成本，短期无持久状态任务仍可使用平面 action loop。` 阻止把它提升为新的长期设计结论。 不把论文名称、作者 benchmark 或未披露实现写成长期机制；若为 Integrate，正文写回仍由 root 按日期串行处理。<!-- books-review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY:end -->

<!-- books-review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:start --><!-- existing:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:end --><!-- delta:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:start -->The 21 sub-projects comprising the catalog corpus were selected from GitHub repositories tagged llm-agent , agent-framework , ai-agent , or llm-orchestration with ≥ 1,000 \geq 1{,}000 stars as of January 2026 in Python, TypeScript, or Rust, and filtered to those that either (a) expose a budget/cost/token-limit option in their public API or (b) have a GitHub issue mentioning cost overrun or runaway-spend in the title. Retained projects span the LangChain/LangGraph, AutoGPT, CrewAI, AutoGen, Pydantic AI, DSPy, LlamaIndex, and IDE-agent ecosystems among others; the full per-project mapping is in the artifact’s catalog CSV project column. Known selection biases: (i) English-language repositories only; (ii) closed-source platforms (Cursor, Replit Agent, ChatGPT plugin store) absent; (iii) the ≥ 1,000 \geq 1{,}000 -star threshold filters out early-stage projects. Boundary: (1) Constructed reproduction : the racy code is a minimal reproduction of the M-delegation-fanout pattern, not a production extract; the catalog’s 11 such rows establish recurrence, the experiment establishes only the race rate at one parameter setting. (2) Mature runtime patterns avoid it too : actor systems and capability-secure runtimes prevent the race when correctly applied—the comparison is against the operator-error baseline most common in the catalog (shared mutable counter under asyncio.gather ), and the distinguishing claim is only that Rust turns the race into a compile-time error rather than a property the operator must remember to establish. (3) Parameter-dependence : a B 0 ∈ { 50 , 60 , 69 , 100 } B_{0}\in\{50,60,69,100\} sweep (Table VI and its companion) shows the racy condition overshoots exactly when 3 × 3\times per-child > B 0 {}>B_{0} , while the affine and locked dis<!-- delta:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT:end -->

<!-- books-review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:start --><!-- existing:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:start -->Root writeback was checked in the fresh post-write audit. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:end --><!-- delta:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:start -->§3–4: a sender model can encode influence in apparently ordinary generated content consumed by a receiver, shifting provenance and trust ownership from human-visible text to the model-to-model channel. Boundary: The experiments demonstrate a model-to-model covert channel in tested settings; they do not establish prevalence in production or a complete detector.<!-- delta:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:end -->Decision: Integrate.<!-- books-review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:end -->

<!-- books-review:SF-ULTRAEP:start --><!-- existing:SF-ULTRAEP:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-ULTRAEP:end --><!-- delta:SF-ULTRAEP:start -->UltraEP reacts to post-gating exact expert load on every microbatch and layer, uses quota-driven planning for temporary replication, and transfers irregular expert state through rack-scale persistent tile streaming with relay-based fan-out mitigation. Router semantics remain unchanged; the planner owns execution placement and replication state. Boundary: The accessible exact-v1 material is the official abstract, not the removed PDF/HTML body. It covers rack-scale MoE training and serving prefill for 106B–671B models, but does not disclose a dedicated limitations section, GPU model, topology dimensions, precision, batch size, failure recovery, optimizer/gradient correctness, decode behavior or a production latency SLO. Later v3 and the July repository are excluded.<!-- delta:SF-ULTRAEP:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-ULTRAEP:end -->

<!-- books-review:SF-PROOF-CARRYING-ACTIONS:start --><!-- existing:SF-PROOF-CARRYING-ACTIONS:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-PROOF-CARRYING-ACTIONS:end --><!-- delta:SF-PROOF-CARRYING-ACTIONS:start -->Abstractly, PCAA seeks a control mechanism M M that minimizes severe missed escalations while respecting review budgets and runtime-boundary constraints: The important point is not the specific loss function. PCAA does not treat average scoring quality as the sole endpoint. It treats selective routing, explicit review semantics, and certificate closure as the actual runtime trust problem. Boundary: The layered integrity architecture remains useful, and the current implementation clarifies its role: Fast commitment lane : lightweight commitments or attestations that make silent drift harder. Portable trust lane : typed trust materials, attestations, or credentials that can travel across systems. Future verification lane : stronger receipts or verifiable computation artifacts that may mature later.<!-- delta:SF-PROOF-CARRYING-ACTIONS:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-PROOF-CARRYING-ACTIONS:end -->

<!-- books-review:SF-EVALSTOP:start --><!-- existing:SF-EVALSTOP:start -->Root writeback was checked in the fresh post-write audit. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-EVALSTOP:end --><!-- delta:SF-EVALSTOP:start -->Recall the architecture overview in Figure 1 . EvalStop is a composable wrapper around any base scheduling policy. It monitors eval-score trajectories (the world feedback signal) and early-stops jobs when quality is irrecoverably declining. Boundary: World feedback as a scheduling signal. Our results show that downstream evaluation (world feedback) is a better signal for scheduling RLHF jobs than training loss (proxy 2 ) or reward model score (proxy). This aligns with the growing recognition that proxy optimization in RLHF requires external grounding ( Gao et al., 2023 ; Skalse et al., 2022 ; Moskovitz et al., 2024 ) .<!-- delta:SF-EVALSTOP:end -->Decision: Integrate.<!-- books-review:SF-EVALSTOP:end -->

<!-- books-review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:start --><!-- existing:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:end --><!-- delta:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:start -->A Sello receipt is a COSE_Sign1 envelope wrapping an HPKE-encrypted payload. The structure is: p ​ k owner pk_{\text{owner}} is the owner’s X25519 public key, bound to the authorization token (Section 4.2) s ​ k service sk_{\text{service}} is the service’s Ed25519 private signing key The body is defined in CDDL [ Birkholz et al., 2019 ] notation, where ? denotes an optional field: receipt-body = { agent-identifier: tstr, ; derived from token hash action-type: tstr, ; e.g. Boundary: An owner who deploys an agent and holds a long-term HPKE key pair. The public key is bound to authorization tokens issued for the agent’s use. An agent , autonomous software acting on the owner’s behalf, which presents authorization tokens when calling services.<!-- delta:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS:end -->

<!-- books-review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:start --><!-- existing:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:end --><!-- delta:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:start -->§3–4: the ANN index is attached to an Apache Iceberg snapshot through Puffin metadata, making index identity and lifecycle follow immutable table snapshots rather than an external mutable service. Boundary: The result supports snapshot-consistent vector-index ownership for the evaluated Iceberg/Puffin design; it does not establish one universal ANN format or cross-engine performance.<!-- delta:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR:end -->

<!-- books-review:SF-ROBOT-BENCHMARK-AUDIT:start --><!-- existing:SF-ROBOT-BENCHMARK-AUDIT:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-ROBOT-BENCHMARK-AUDIT:end --><!-- delta:SF-ROBOT-BENCHMARK-AUDIT:start -->We use a citation tracker repository to derive both the count of new arXiv papers reporting numbers on a given benchmark in a given month (the “79 new arXiv papers” figure in the introduction) and the per-benchmark cumulative counts in Figure 2 . Per-paper evidence and the full row-level audit are available through the project website: ripl.github.io/manipulation_benchmark_audit . The snapshot we report on was taken on 2026-05-21. Boundary: All four failure modes share one root cause: a benchmark score is an empirical average of success over a fixed test distribution, treated as evidence of capability over the much broader distribution of interest. Each diagnostic catches one way the score can detach from the capability it stands in for: the test instances admit a shortcut, the empirical average is too noisy to resolve the claimed gap, the test distribution is a narrow slice of the variation we care about, or the gap between training and test data drives the score more than capability does. What a future manipulation benchmark should look like.<!-- delta:SF-ROBOT-BENCHMARK-AUDIT:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-ROBOT-BENCHMARK-AUDIT:end -->

<!-- books-review:SF-AGENT-DATA-CURATION-HARNESS:start --><!-- existing:SF-AGENT-DATA-CURATION-HARNESS:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-AGENT-DATA-CURATION-HARNESS:end --><!-- delta:SF-AGENT-DATA-CURATION-HARNESS:start -->Three additional LLM-driven components are part of the methodology rather than the writing process. The four trajectories labels in Table 1 (new policy, grounded, effective, shallow) are produced with LLM assistance using Claude Opus 4.7, following the rubric in Section 2.2 . We treat these labels as diagnostic annotations rather than ground-truth scientific claims, and we provide rubrics and trace examples to support auditing. Boundary: This paper introduced Curation-Bench , a benchmark for evaluating whether generalist agents can conduct training-data curation as an iterative policy-search process. By fixing the model, training recipe, and evaluation suite, Curation-Bench isolates the curated data policy as the object of optimization and records the full trajectory of agent decisions. Our results show both promise and a limitation.<!-- delta:SF-AGENT-DATA-CURATION-HARNESS:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-AGENT-DATA-CURATION-HARNESS:end -->

<!-- books-review:SF-RL-EXCURSIONS-PRETRAINING:start --><!-- existing:SF-RL-EXCURSIONS-PRETRAINING:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-RL-EXCURSIONS-PRETRAINING:end --><!-- delta:SF-RL-EXCURSIONS-PRETRAINING:start -->In Figure 2 , we report the performance of ℳ t \mathcal{M}_{t} , ℳ t RL \mathcal{M}_{t}^{\text{RL}} , ℳ t SFT \mathcal{M}_{t}^{\text{SFT}} , and ℳ t SFT → RL \mathcal{M}_{t}^{\text{SFT}\rightarrow\text{RL}} at various pre-training steps t t on GSM8K, using the GSM8K subset of OpenMathInstruct for post-training. We evaluate base checkpoints ℳ t \mathcal{M}_{t} with 8-shot prompting, as they cannot reliably follow question-answering instructions 3 3 3 In Appendix B.6 , we ablate the number of in-context examples and confirm that 8-shot yields the best performance for ℳ t \mathcal{M}_{t} . All post-trained models use 0-shot evaluation, as RL includes a formatting reward and SFT data is formatted accordingly. Boundary: In this work, we provide a comprehensive and nuanced picture of the RL objective for LLM training beyond how it is used in the current standard pipeline. We find that RL can be effective starting early in pre-training, well before the Chinchilla-optimal regime, and often matches the full SFT → \to RL pipeline on GSM8K tokens despite never seeing a ground-truth reasoning trace. Further, the dominant lever for whether early RL succeeds is pre-training data composition, not model scale.<!-- delta:SF-RL-EXCURSIONS-PRETRAINING:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-RL-EXCURSIONS-PRETRAINING:end -->

<!-- books-review:SF-INTERVENTION-TIMING-RELIABILITY:start --><!-- existing:SF-INTERVENTION-TIMING-RELIABILITY:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-INTERVENTION-TIMING-RELIABILITY:end --><!-- delta:SF-INTERVENTION-TIMING-RELIABILITY:start -->We separate the system into three independent layers, a structure maintained throughout development and documented in a contemporaneous design log. Boundary: All F1 and firing-rate-versus-label metrics are based on a single 56-action trajectory. The saturation result spans five trajectories but uses no labels. Exact label-based metrics are noisy point estimates and should be interpreted directionally only.<!-- delta:SF-INTERVENTION-TIMING-RELIABILITY:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-INTERVENTION-TIMING-RELIABILITY:end -->

<!-- books-review:SF-LAZYATTENTION:start --><!-- existing:SF-LAZYATTENTION:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-LAZYATTENTION:end --><!-- delta:SF-LAZYATTENTION:start -->In this section, we show how the positional information of reused documents can be adjusted during the attention calculation. Then we analyze the cost of deferred positional encoding for prefilling and decoding, respectively. Inspired by the analysis, we present how to integrate LazyAttention with FlashAttention ( Dao et al., 2022 ; Dao, 2024 ; Shah et al., 2024 ) seamlessly to achieve efficient computation. Boundary: We now quantify why position-awareness directly lowers cache hit ratio. Assume reusable documents follow a Zipf distribution, where the i i -th most popular document has probability proportional to i − α i^{-\alpha} . If each document may appear in any of D D prompt positions and the cache stores C C physical KV entries, a position-agnostic cache stores one entry per document and caches the top C C documents: where N N is the number of reusable documents.<!-- delta:SF-LAZYATTENTION:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-LAZYATTENTION:end -->

<!-- books-review:SF-OCL-EXECUTION-BOUNDARY:start --><!-- existing:SF-OCL-EXECUTION-BOUNDARY:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-OCL-EXECUTION-BOUNDARY:end --><!-- delta:SF-OCL-EXECUTION-BOUNDARY:start -->We study how platforms should control agent-mediated economic decisions before they affect real users, merchants, or transactions. Boundary: Across all models, OCL maintains an exceptionally high Success Rate ( ≥ 96 % \geq 96\% ), proving that strict structural constraints do not induce conversation collapse. Concurrently, OCL robustly intercepts adversarial threats, achieving intercept rates of 94% (GPT-5.4), 82% (Gemini-3.1), and 60% (Qwen-3.5)—effectively securing inherently vulnerable baseline architectures.<!-- delta:SF-OCL-EXECUTION-BOUNDARY:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-OCL-EXECUTION-BOUNDARY:end -->

<!-- books-review:SF-AGENT-MEMORY-GENERALITY:start --><!-- existing:SF-AGENT-MEMORY-GENERALITY:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-AGENT-MEMORY-GENERALITY:end --><!-- delta:SF-AGENT-MEMORY-GENERALITY:start -->Algorithm 1 defines the canonical AutoMEM design: a multi-step plan–execute–judge loop that can re-query memory when the judge finds the trace insufficient. This iterative form is what delivers the accuracy in Table 8 . On top of long context’s single LLM call, the loop issues three to four calls per question (planner, optional dump, judge, answerer), and the outer loop can issue further calls when the judge requests more evidence (Table 9 ). Boundary: We revisit memory systems for LLM agents through a cross-scenario generality and cost lens and draw: (1) no existing memory system wins across all five task families, while an off-the-shelf agent harness achieves the best generality; (2) index-based methods fail on agentic-trajectory QA in two ways: build-time schemas drop step- and action-level evidence (storage), and passive retrieval cannot surface evidence the storage retains (retrieval); (3) reaching the cost–accuracy frontier requires combining the agent harness with selective indexing, which we instantiate in AutoMEM. We see two potential future directions: (i) a memory DSL that automates schema design — a DSL over memory primitives could replace verbose Cypher and let the schema be meta-learned per workload ( Xiong et al., 2026 ) ; (ii) dedicated infrastructure for memory-bound agents — serial prefill across plan/judge/answer dom<!-- delta:SF-AGENT-MEMORY-GENERALITY:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-AGENT-MEMORY-GENERALITY:end -->

<!-- books-review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:start --><!-- existing:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:start -->Fresh current-tree comparison found no Books mutation requirement. See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:end --><!-- delta:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:start -->Per-skill autonomy tiers, explicit human graduation and runtime drift correction form an inference-time authorization/control plane. Boundary: Evidence is limited to §6 limitations and risks; single professional-corpus proof-of-concept boundary; it does not establish a universal production result outside the declared models, systems, workloads or topology.<!-- delta:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:end -->Decision: No Change — Existing Coverage.<!-- books-review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE:end -->

<!-- books-review:SF-2026-ARXIV-2606-04329:start -->
<!-- existing:SF-2026-ARXIV-2606-04329:start -->prompt injection 跨会话存活；<!-- existing:SF-2026-ARXIV-2606-04329:end -->

<!-- delta:SF-2026-ARXIV-2606-04329:start -->MPBench 把攻击拆为 memory write channel、结构漏洞、写入策略与后续检索触发。memory store 持有持久状态，外部 payload 是不可信数据，write/retrieve policy 掌握纳入上下文的控制权；实现以一次投毒写入和后续独立会话中的读取构成端到端事务。<!-- delta:SF-2026-ARXIV-2606-04329:end -->

Target `AGENT-MEMORY` at `books/part-07-agent/77-memory.md#L51`; adjacent refs: books/part-07-agent/76-rag.md#L483; books/part-07-agent/78-tool-calling.md#L366. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04329:end -->

<!-- books-review:SF-2026-ARXIV-2606-04384:start -->
<!-- existing:SF-2026-ARXIV-2606-04384:start -->Differential Privacy 先定义被保护对象，再选择机制<!-- existing:SF-2026-ARXIV-2606-04384:end -->

<!-- delta:SF-2026-ARXIV-2606-04384:start -->论文重新推导 selective-release privacy loss，并以 clipped-gradient release rule 组成 DPSR-CG。privacy accountant 持有累计预算，clipped gradient/noise 是受保护数据流，release predicate 控制一次更新是否进入外部可见模型状态。<!-- delta:SF-2026-ARXIV-2606-04384:end -->

Target `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L118`; adjacent refs: books/part-06-ai-infrastructure/71-multi-tenant.md#L84; books/part-06-ai-infrastructure/73-production-best-practice.md#L37. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04384:end -->

<!-- books-review:SF-2026-ARXIV-2606-04415:start -->
<!-- existing:SF-2026-ARXIV-2606-04415:start -->本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**<!-- existing:SF-2026-ARXIV-2606-04415:end -->

<!-- delta:SF-2026-ARXIV-2606-04415:start -->FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。<!-- delta:SF-2026-ARXIV-2606-04415:end -->

Target `INFER-PD-DISAGGREGATION` at `books/part-05-inference-system/55-pd-disaggregation.md#L14`; adjacent refs: books/part-05-inference-system/54-gpu-memory.md#L369; books/part-05-inference-system/56-inference-scheduling.md#L843. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04415:end -->

<!-- books-review:SF-2026-ARXIV-2606-04425:start -->
<!-- existing:SF-2026-ARXIV-2606-04425:start -->prompt injection 跨会话存活；<!-- existing:SF-2026-ARXIV-2606-04425:end -->

<!-- delta:SF-2026-ARXIV-2606-04425:start -->论文建立 write–persistence–incorporation–activation 生命周期和 sandbox。持久介质保存攻击状态，clean victim query 触发重新纳入，context constructor 掌握从存储到可执行上下文的数据控制权。<!-- delta:SF-2026-ARXIV-2606-04425:end -->

Target `AGENT-MEMORY` at `books/part-07-agent/77-memory.md#L51`; adjacent refs: books/part-07-agent/76-rag.md#L551; books/part-07-agent/78-tool-calling.md#L424. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04425:end -->

<!-- books-review:SF-2026-ARXIV-2606-04522:start -->
<!-- existing:SF-2026-ARXIV-2606-04522:start -->评估 `model + prompt + context + retrieval + tools + policy` 的端到端结果。RAG 的 retrieval recall 与 answer groundedness、Tool Calling 的选择与执行结果，都属于这一层。<!-- existing:SF-2026-ARXIV-2606-04522:end -->

<!-- delta:SF-2026-ARXIV-2606-04522:start -->论文用 1/Ratio@k 比较返回邻居与真实邻居的距离质量，并把 metric 作为 index tuning objective。索引持有候选集合，distance 是数据证据，benchmark/tuner 决定 latency–quality operating point。<!-- delta:SF-2026-ARXIV-2606-04522:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L209`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L334. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04522:end -->

<!-- books-review:SF-2026-ARXIV-2606-04557:start -->
<!-- existing:SF-2026-ARXIV-2606-04557:start -->另一种复用粒度不是 request prefix，而是把每个稳定 document 的 derived KV 包装成 immutable packet，再在请求<!-- existing:SF-2026-ARXIV-2606-04557:end -->

<!-- delta:SF-2026-ARXIV-2606-04557:start -->CAS 用 dynamic distractor mixing 训练可组合 per-document cartridges，并由 budget manager 在 GPU 与持久存储间轮换。cartridge 是版本化 KV artifact，selector 决定加载集合，cache manager 掌握驻留和 token budget。<!-- delta:SF-2026-ARXIV-2606-04557:end -->

Target `INFER-KV-CACHE` at `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L640`; adjacent refs: books/part-05-inference-system/44-decode.md#L305; books/part-05-inference-system/46-continuous-batching.md#L104. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04557:end -->

<!-- books-review:SF-2026-ARXIV-2606-04581:start -->
<!-- existing:SF-2026-ARXIV-2606-04581:start -->这就是 speculative decoding 试图突破的地方：既然大模型一步一步生成很慢，能不能先让一个便宜的 draft model 猜出多个未来 token，再让大模型一次性验证这些猜测？<!-- existing:SF-2026-ARXIV-2606-04581:end -->

<!-- delta:SF-2026-ARXIV-2606-04581:start -->Multi-SPIN 让设备 SLM 产出 drafts、edge LLM 批量验证，并联合优化 draft length、频分带宽和计算分配。每用户 draft/acceptance 是状态，radio/compute budget 是资源数据，central optimizer 掌握分配控制。<!-- delta:SF-2026-ARXIV-2606-04581:end -->

Target `INFER-SPECULATIVE-DECODING` at `books/part-05-inference-system/48-speculative-decoding.md#L33`; adjacent refs: books/part-05-inference-system/47-pagedattention.md#L3; books/part-05-inference-system/49-tensorrt-llm.md#L1047. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04581:end -->

<!-- books-review:SF-2026-ARXIV-2606-04594:start -->
<!-- existing:SF-2026-ARXIV-2606-04594:start -->从 Linear Trace 到 Root-cause Graph<!-- existing:SF-2026-ARXIV-2606-04594:end -->

<!-- delta:SF-2026-ARXIV-2606-04594:start -->Ekka 对齐 target 与 reference implementation 的中间 execution states，逐层/逐算子做 differential diagnosis。reference trace 是正确性证据，target trace 是观测数据，alignment/search controller 定位首个 divergence。<!-- delta:SF-2026-ARXIV-2606-04594:end -->

Target `PLATFORM-TRACE` at `books/part-06-ai-infrastructure/69-trace.md#L105`; adjacent refs: books/part-06-ai-infrastructure/68-logging.md#L119; books/part-06-ai-infrastructure/70-cost.md#L235. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04594:end -->

<!-- books-review:SF-2026-ARXIV-2606-04628:start -->
<!-- existing:SF-2026-ARXIV-2606-04628:start -->长输入；后者由平台跨调用持久化，必须具备 provenance、authorization、correction 与 deletion。<!-- existing:SF-2026-ARXIV-2606-04628:end -->

<!-- delta:SF-2026-ARXIV-2606-04628:start -->RAMPART 以 named block registry 保存 provenance/priority/authorship，并在 compile context 前执行 promote、gate、write、evict、rollback。registry 持有状态，blocks 是数据，policy engine 掌握上下文编译权。<!-- delta:SF-2026-ARXIV-2606-04628:end -->

Target `AGENT-MEMORY` at `books/part-07-agent/77-memory.md#L31`; adjacent refs: books/part-07-agent/76-rag.md#L589; books/part-07-agent/78-tool-calling.md#L422. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04628:end -->

<!-- books-review:SF-2026-ARXIV-2606-04769:start -->
<!-- existing:SF-2026-ARXIV-2606-04769:start -->Server 自述的 tool annotations 和 descriptions 不能作为唯一信任依据。Host 应限制 server 可见 roots/data、credentials、network 和 sampling content。<!-- existing:SF-2026-ARXIV-2606-04769:end -->

<!-- delta:SF-2026-ARXIV-2606-04769:start -->DCIChecker 联合 schema-aware static analysis 与 LLM classifier，对 description、signature、implementation effects 建立一致性检查。代码与描述是双份接口数据，server owner 维护实现，release gate 决定不一致是否阻断发布。<!-- delta:SF-2026-ARXIV-2606-04769:end -->

Target `AGENT-MCP` at `books/part-07-agent/83-mcp.md#L145`; adjacent refs: books/part-07-agent/82-multi-agent.md#L571; books/part-07-agent/84-agent-platform.md#L784. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04769:end -->

<!-- books-review:SF-2026-ARXIV-2606-04778:start -->
<!-- existing:SF-2026-ARXIV-2606-04778:start -->Safety Evaluation 的单位是 Run，不只是 Prompt<!-- existing:SF-2026-ARXIV-2606-04778:end -->

<!-- delta:SF-2026-ARXIV-2606-04778:start -->方法模拟 mid-sequence token perturbation，构造 trajectory-level alignment data 并直接训练扰动后的继续生成。decoder state 持有轨迹，注入 token 改变数据流，training objective 负责把恢复行为写入权重。<!-- delta:SF-2026-ARXIV-2606-04778:end -->

Target `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L243`; adjacent refs: books/part-06-ai-infrastructure/71-multi-tenant.md#L84; books/part-06-ai-infrastructure/73-production-best-practice.md#L89. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04778:end -->

<!-- books-review:SF-2026-ARXIV-2606-04799:start -->
<!-- existing:SF-2026-ARXIV-2606-04799:start -->Exemplar 可从 histogram bucket 跳转到代表性 trace；TraceId/SpanId 可把 logs 挂到 span。三者共享 resource identity 与 semantic conventions 才能关联。<!-- existing:SF-2026-ARXIV-2606-04799:end -->

<!-- delta:SF-2026-ARXIV-2606-04799:start -->UModel 建虚拟 ontology，把 telemetry、entities 与 expert knowledge 映射为 object graph，并由 U-SPL pipeline 查询。object identity/relations 是共享状态，source adapters 供数据，query planner 掌握跨源探索控制。<!-- delta:SF-2026-ARXIV-2606-04799:end -->

Target `PLATFORM-TRACE` at `books/part-06-ai-infrastructure/69-trace.md#L95`; adjacent refs: books/part-06-ai-infrastructure/68-logging.md#L44; books/part-06-ai-infrastructure/70-cost.md#L235. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04799:end -->

<!-- books-review:SF-2026-ARXIV-2606-04923:start -->
<!-- existing:SF-2026-ARXIV-2606-04923:start -->证据边界：支持 synthetic final-anchor 合同中的性能退化和 transition diagnosis；不证明真实用户中的发生率、memory 单独即可修复 intent tracking，或初步 RL 结果可泛化。<!-- existing:SF-2026-ARXIV-2606-04923:end -->

<!-- delta:SF-2026-ARXIV-2606-04923:start -->CHERRL 可控注入 judge bias，跟踪 reward divergence/hacking onset，并用 agent detector 搜索作弊行为。rubric/judge 持有评价状态，policy outputs 是数据，RL optimizer 把 judge signal 转成权重更新控制。<!-- delta:SF-2026-ARXIV-2606-04923:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L2282`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L334. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-04923:end -->

<!-- books-review:SF-2026-ARXIV-2606-04929:start -->
<!-- existing:SF-2026-ARXIV-2606-04929:start -->单一 WAF 无法覆盖这条链。每次从一层向下一层传递，都需要验证 identity、integrity 和 authorization。<!-- existing:SF-2026-ARXIV-2606-04929:end -->

<!-- delta:SF-2026-ARXIV-2606-04929:start -->论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。<!-- delta:SF-2026-ARXIV-2606-04929:end -->

Target `PLATFORM-SECURITY` at `books/part-06-ai-infrastructure/72-security.md#L48`; adjacent refs: books/part-06-ai-infrastructure/71-multi-tenant.md#L135; books/part-06-ai-infrastructure/73-production-best-practice.md#L195. Decision: `Integrate`. Post-write verified at `books/part-06-ai-infrastructure/72-security.md#L50` with SHA-256 `c66c19d8fcdd879c1be48b9c85ea1949fafe9f167852e7b17b698d88955760f1`.
<!-- books-review:SF-2026-ARXIV-2606-04929:end -->

<!-- books-review:SF-2026-ARXIV-2606-05029:start -->
<!-- existing:SF-2026-ARXIV-2606-05029:start -->Evaluator 的 aggregate accuracy 可能同时掩盖两种相反失败：目标事实已经改变，judge 却保持原 verdict；无关表达被改写，judge 又错误地改变 verdict。因而 construct validity 不应压成一个标量，而应至少有两条受控 intervention arm：<!-- existing:SF-2026-ARXIV-2606-05029:end -->

<!-- delta:SF-2026-ARXIV-2606-05029:start -->框架把研究设计映射到 statistical、internal、external、construct validity，并为三类低成本 strategy 建立 characteristic threat profile。experiment design 持有 estimand，observations 是证据数据，claim gate 决定可外推范围。<!-- delta:SF-2026-ARXIV-2606-05029:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1267`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L380. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05029:end -->

<!-- books-review:SF-2026-ARXIV-2606-05037:start -->
<!-- existing:SF-2026-ARXIV-2606-05037:start -->{violations, evidence pointers, currently available recovery tools}<!-- existing:SF-2026-ARXIV-2606-05037:end -->

<!-- delta:SF-2026-ARXIV-2606-05037:start -->self-reflective API 返回 machine-readable recovery_feedback.suggestions[]，将失败字段、修复动作和 retry 输入结构化。server 持有 schema truth，error payload 是控制数据，agent retry loop 决定是否应用建议。<!-- delta:SF-2026-ARXIV-2606-05037:end -->

Target `AGENT-TOOL-CALLING` at `books/part-07-agent/78-tool-calling.md#L251`; adjacent refs: books/part-07-agent/77-memory.md#L1340; books/part-07-agent/79-planning.md#L329. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05037:end -->

<!-- books-review:SF-2026-ARXIV-2606-05043:start -->
<!-- existing:SF-2026-ARXIV-2606-05043:start -->共享 Repository 需要 Commitment Protocol，不只是更多消息<!-- existing:SF-2026-ARXIV-2606-05043:end -->

<!-- delta:SF-2026-ARXIV-2606-05043:start -->Strabo 把 UCP checkout 建模为 declarative Langshaw protocol，并用 Peach agents 执行且与 Google UCP agents 互操作。protocol artifact 持有允许交互状态，messages 是数据，runtime verifier 掌握 transition control。<!-- delta:SF-2026-ARXIV-2606-05043:end -->

Target `AGENT-MULTI-AGENT` at `books/part-07-agent/82-multi-agent.md#L277`; adjacent refs: books/part-07-agent/81-workflow.md#L796; books/part-07-agent/83-mcp.md#L209. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05043:end -->

<!-- books-review:SF-2026-ARXIV-2606-05122:start -->
<!-- existing:SF-2026-ARXIV-2606-05122:start -->self-evaluation P(True) / P(IK),<!-- existing:SF-2026-ARXIV-2606-05122:end -->

<!-- delta:SF-2026-ARXIV-2606-05122:start -->SEE 先做 calibration-coupled RL 同时回答和预测 judge，再 masked distillation 只锐化 score prediction。模型 token distribution 持有潜在自评信号，judge labels 是校准数据，loss mask 控制哪些行为被更新。<!-- delta:SF-2026-ARXIV-2606-05122:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L1133`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L245. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-05122:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260604-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260604 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260604: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260604-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY; review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT; review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS; review:SF-ULTRAEP; review:SF-PROOF-CARRYING-ACTIONS; review:SF-EVALSTOP; review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS; review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR; review:SF-ROBOT-BENCHMARK-AUDIT; review:SF-AGENT-DATA-CURATION-HARNESS; review:SF-RL-EXCURSIONS-PRETRAINING; review:SF-INTERVENTION-TIMING-RELIABILITY; review:SF-LAZYATTENTION; review:SF-OCL-EXECUTION-BOUNDARY; review:SF-AGENT-MEMORY-GENERALITY; review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE; review:SF-2026-ARXIV-2606-04329; review:SF-2026-ARXIV-2606-04384; review:SF-2026-ARXIV-2606-04402; review:SF-2026-ARXIV-2606-04413; review:SF-2026-ARXIV-2606-04415; review:SF-2026-ARXIV-2606-04425; review:SF-2026-ARXIV-2606-04459; review:SF-2026-ARXIV-2606-04522; review:SF-2026-ARXIV-2606-04557; review:SF-2026-ARXIV-2606-04581; review:SF-2026-ARXIV-2606-04594; review:SF-2026-ARXIV-2606-04628; review:SF-2026-ARXIV-2606-04769; review:SF-2026-ARXIV-2606-04778; review:SF-2026-ARXIV-2606-04799; review:SF-2026-ARXIV-2606-04850; review:SF-2026-ARXIV-2606-04903; review:SF-2026-ARXIV-2606-04908; review:SF-2026-ARXIV-2606-04923; review:SF-2026-ARXIV-2606-04929; review:SF-2026-ARXIV-2606-05004; review:SF-2026-ARXIV-2606-05029; review:SF-2026-ARXIV-2606-05037; review:SF-2026-ARXIV-2606-05043; review:SF-2026-ARXIV-2606-05122 | EVIDENCE-OWNER-REBUILD-20260604: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260604-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY; analysis-decision:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT; analysis-decision:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS; analysis-decision:SF-ULTRAEP; analysis-decision:SF-PROOF-CARRYING-ACTIONS; analysis-decision:SF-EVALSTOP; analysis-decision:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS; analysis-decision:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR; analysis-decision:SF-ROBOT-BENCHMARK-AUDIT; analysis-decision:SF-AGENT-DATA-CURATION-HARNESS; analysis-decision:SF-RL-EXCURSIONS-PRETRAINING; analysis-decision:SF-INTERVENTION-TIMING-RELIABILITY; analysis:DA-POSITION-INDEPENDENT-KV-STATE; analysis-decision:SF-OCL-EXECUTION-BOUNDARY; analysis-decision:SF-AGENT-MEMORY-GENERALITY; analysis-decision:SF-DIGITAL-APPRENTICE-CONTROL-PLANE; analysis-decision:SF-2026-ARXIV-2606-04329; analysis-decision:SF-2026-ARXIV-2606-04384; analysis-decision:SF-2026-ARXIV-2606-04402; analysis-decision:SF-2026-ARXIV-2606-04413; analysis:DA-20260604-NPU-VIRTUALIZATION; analysis-decision:SF-2026-ARXIV-2606-04425; analysis-decision:SF-2026-ARXIV-2606-04459; analysis-decision:SF-2026-ARXIV-2606-04522; analysis-decision:SF-2026-ARXIV-2606-04557; analysis-decision:SF-2026-ARXIV-2606-04581; analysis-decision:SF-2026-ARXIV-2606-04594; analysis-decision:SF-2026-ARXIV-2606-04628; analysis-decision:SF-2026-ARXIV-2606-04769; analysis-decision:SF-2026-ARXIV-2606-04778; analysis-decision:SF-2026-ARXIV-2606-04799; analysis-decision:SF-2026-ARXIV-2606-04850; analysis-decision:SF-2026-ARXIV-2606-04903; analysis-decision:SF-2026-ARXIV-2606-04908; analysis-decision:SF-2026-ARXIV-2606-04923; analysis:DA-20260604-CROSS-STAGE-POISONING; analysis-decision:SF-2026-ARXIV-2606-05004; analysis-decision:SF-2026-ARXIV-2606-05029; analysis-decision:SF-2026-ARXIV-2606-05037; analysis-decision:SF-2026-ARXIV-2606-05043; analysis-decision:SF-2026-ARXIV-2606-05122 | SELECTION-OWNER-REBUILD-20260604: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260604-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY; books-review:SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT; books-review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS; books-review:SF-ULTRAEP; books-review:SF-PROOF-CARRYING-ACTIONS; books-review:SF-EVALSTOP; books-review:SF-RECEIVER-ATTESTED-AGENT-RECEIPTS; books-review:SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR; books-review:SF-ROBOT-BENCHMARK-AUDIT; books-review:SF-AGENT-DATA-CURATION-HARNESS; books-review:SF-RL-EXCURSIONS-PRETRAINING; books-review:SF-INTERVENTION-TIMING-RELIABILITY; books-review:SF-LAZYATTENTION; books-review:SF-OCL-EXECUTION-BOUNDARY; books-review:SF-AGENT-MEMORY-GENERALITY; books-review:SF-DIGITAL-APPRENTICE-CONTROL-PLANE; books-review:SF-2026-ARXIV-2606-04329; books-review:SF-2026-ARXIV-2606-04384; books-review:SF-2026-ARXIV-2606-04415; books-review:SF-2026-ARXIV-2606-04425; books-review:SF-2026-ARXIV-2606-04522; books-review:SF-2026-ARXIV-2606-04557; books-review:SF-2026-ARXIV-2606-04581; books-review:SF-2026-ARXIV-2606-04594; books-review:SF-2026-ARXIV-2606-04628; books-review:SF-2026-ARXIV-2606-04769; books-review:SF-2026-ARXIV-2606-04778; books-review:SF-2026-ARXIV-2606-04799; books-review:SF-2026-ARXIV-2606-04923; books-review:SF-2026-ARXIV-2606-04929; books-review:SF-2026-ARXIV-2606-05029; books-review:SF-2026-ARXIV-2606-05037; books-review:SF-2026-ARXIV-2606-05043; books-review:SF-2026-ARXIV-2606-05122 | BOOKS-OWNER-REBUILD-20260604: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- Exact-version access、pending 与 blocker 状态保留在 Review Completion Receipt 和 date-local source packet；42/42 retained families have complete accessible receipts.

## 9. Recommended Action

No additional Books writeback is required for this date. Preserve the frozen V12 receipts and re-open only if an exact-version revision or artifact changes a recorded boundary.

## 10. Repository Changes

- Created immutable V12 downstream receipts for `42/42` Source Reviews, benchmark contracts and Deep Selection, plus `30/30` Books-eligible comparisons; `12` Weekly Only families intentionally stop at candidate-level closure.
- Replaced the invalid `2606.04850` duplicated Method/Limitations locator with distinct Method, Evaluation and bounded limitations routes.
- Rebuilt all `42/42` review bodies from source-specific exact-v1 conclusions; no title/admission-delta placeholder is accepted as a problem, mechanism or evaluation statement.
- Corrected `2606.04384` from `TRAIN-PRETRAINING` to the existing `PLATFORM-SECURITY` privacy owner after reading the owner and adjacent chapters.
- Corrected benchmark disclosures that previously confused background prose with evaluation setup, including Ekka precision, RAMPART model/hardware/quantization, mechanistic-study models, judge models, schema-contract models and CHASE/control-evaluation models.
- Books files changed by root serialization: `2` (`Ch72`, `Ch82`); no other Books file is part of this 6/4 writeback scope.
- Post-write receipt: `../_sources/daily-20260604/books-postwrite-semantic-audit-v13.md`.

## 11. Open Questions

- Open question: none. Coverage, Evidence/Selection and Books Gates are passed.

## 12. Sources

- [Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents](https://arxiv.org/abs/2606.04017v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study](https://arxiv.org/abs/2606.04056v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Covert Influence Between Language Models](https://arxiv.org/abs/2606.04071v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing](https://arxiv.org/abs/2606.04101v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems](https://arxiv.org/abs/2606.04104v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms](https://arxiv.org/abs/2606.04145v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions](https://arxiv.org/abs/2606.04193v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines](https://arxiv.org/abs/2606.04196v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Can Generalist Agents Automate Data Curation?](https://arxiv.org/abs/2606.04261v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training](https://arxiv.org/abs/2606.04272v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents](https://arxiv.org/abs/2606.04296v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://arxiv.org/abs/2606.04302v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems](https://arxiv.org/abs/2606.04306v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline](https://arxiv.org/abs/2606.04315v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [The Digital Apprentice: A Framework for Human-Directed Agentic AI Development](https://arxiv.org/abs/2606.04321v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Revisiting Privacy Amplification by Subsampling in Selective Release DPSGD](https://arxiv.org/abs/2606.04384v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation](https://arxiv.org/abs/2606.04402v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [(Mis)generalization of Helpful-only Fine-tuning](https://arxiv.org/abs/2606.04413v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location](https://arxiv.org/abs/2606.04415v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection](https://arxiv.org/abs/2606.04425v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Token Rankings are Unforgeable Language Model Signatures](https://arxiv.org/abs/2606.04459v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [ANN Search: Recall What Matters](https://arxiv.org/abs/2606.04522v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Cartridges at Scale: Training Modular KV Caches over Large Document Collections](https://arxiv.org/abs/2606.04557v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge](https://arxiv.org/abs/2606.04581v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Ekka: Automated Diagnosis of Silent Errors in LLM Inference](https://arxiv.org/abs/2606.04594v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation](https://arxiv.org/abs/2606.04628v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications](https://arxiv.org/abs/2606.04769v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories](https://arxiv.org/abs/2606.04778v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [UModel: An Agent-Ready Observability Data Modeling Method at Scale](https://arxiv.org/abs/2606.04799v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Uncertainty-Aware End-to-End Co-Design of Neural Network Processors: From Training and Mapping to Fabrication](https://arxiv.org/abs/2606.04850v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Provably Auditable and Safe LLM Agents from Human-Authored Ontologies](https://arxiv.org/abs/2606.04903v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [GNStor: Design of GPU-Native High-Performance Remote All-Flash Array](https://arxiv.org/abs/2606.04908v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Sequential Data Poisoning in LLM Post-Training](https://arxiv.org/abs/2606.04929v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models](https://arxiv.org/abs/2606.05004v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Validity Threats for Foundation Model Research](https://arxiv.org/abs/2606.05029v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery](https://arxiv.org/abs/2606.05037v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols](https://arxiv.org/abs/2606.05043v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
- [Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data](https://arxiv.org/abs/2606.05122v1) — first-public（Asia/Shanghai）：2026-06-04；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
