# Daily Research — 2026-06-04

**Research Date:** 2026-06-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-03 09:00:00 ～ 2026-06-04 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

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
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-03T09:00:00+08:00 | 2026-06-04T09:00:00+08:00 | 2026-08-29T12:00:00+08:00 | 574/574 title+abstract semantic replay, exact-v1 history reconciliation, V12 full FP/FN audit | checked | 574 | SF-2026-ARXIV-2606-04329; SF-2026-ARXIV-2606-04384; SF-2026-ARXIV-2606-04402; SF-2026-ARXIV-2606-04413; SF-2026-ARXIV-2606-04415; SF-2026-ARXIV-2606-04425; SF-2026-ARXIV-2606-04459; SF-2026-ARXIV-2606-04522; SF-2026-ARXIV-2606-04557; SF-2026-ARXIV-2606-04581; SF-2026-ARXIV-2606-04594; SF-2026-ARXIV-2606-04628; SF-2026-ARXIV-2606-04769; SF-2026-ARXIV-2606-04778; SF-2026-ARXIV-2606-04799; SF-2026-ARXIV-2606-04850; SF-2026-ARXIV-2606-04903; SF-2026-ARXIV-2606-04908; SF-2026-ARXIV-2606-04923; SF-2026-ARXIV-2606-04929; SF-2026-ARXIV-2606-05004; SF-2026-ARXIV-2606-05029; SF-2026-ARXIV-2606-05037; SF-2026-ARXIV-2606-05043; SF-2026-ARXIV-2606-05122; SF-2026-ARXIV-2606-05241; SF-2026-ARXIV-2606-05271; SF-2026-ARXIV-2606-05304; SF-2026-ARXIV-2606-05308; SF-2026-ARXIV-2606-05339; SF-2026-ARXIV-2606-05378; SF-2026-ARXIV-2606-05384; SF-2026-ARXIV-2606-05391; SF-2026-ARXIV-2606-05395; SF-2026-ARXIV-2606-05396; SF-2026-ARXIV-2606-05403; SF-2026-ARXIV-2606-05414; SF-2026-ARXIV-2606-05415; SF-2026-ARXIV-2606-05433; SF-2026-ARXIV-2606-05495; SF-2026-ARXIV-2606-05523; SF-2026-ARXIV-2606-06529 | pages=3; final cursor=end; frozen local ledger | 2026-06-04T01:00:00Z | ../_sources/daily-20260604/candidate-denominator-repair-proposal-v12.json; ../_sources/daily-20260604/root-denominator-acceptance-v12.md; coverage:SRC-ARXIV:20260604 | — |

<!-- coverage:SRC-ARXIV:20260604:start -->Root accepted the mutually exclusive `42 + 532 = 574` V12 ledger after a complete false-positive/false-negative review. This downstream lane does not reopen that denominator.<!-- coverage:SRC-ARXIV:20260604:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-04329 | arXiv:2606.04329v1 | paper-v1:2606.04329 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04329 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04329 | yes |
| SF-2026-ARXIV-2606-04384 | arXiv:2606.04384v1 | paper-v1:2606.04384 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04384 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04384 | yes |
| SF-2026-ARXIV-2606-04402 | arXiv:2606.04402v1 | paper-v1:2606.04402 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04402 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04413 | arXiv:2606.04413v1 | paper-v1:2606.04413 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04413 | self | — | new_in_window | TRAIN-SFT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04415 | arXiv:2606.04415v1 | paper-v1:2606.04415 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04415 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04415 | yes |
| SF-2026-ARXIV-2606-04425 | arXiv:2606.04425v1 | paper-v1:2606.04425 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04425 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04425 | yes |
| SF-2026-ARXIV-2606-04459 | arXiv:2606.04459v1 | paper-v1:2606.04459 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04459 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04522 | arXiv:2606.04522v1 | paper-v1:2606.04522 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04522 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04522 | yes |
| SF-2026-ARXIV-2606-04557 | arXiv:2606.04557v1 | paper-v1:2606.04557 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04557 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04557 | yes |
| SF-2026-ARXIV-2606-04581 | arXiv:2606.04581v1 | paper-v1:2606.04581 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04581 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04581 | yes |
| SF-2026-ARXIV-2606-04594 | arXiv:2606.04594v1 | paper-v1:2606.04594 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04594 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04594 | yes |
| SF-2026-ARXIV-2606-04628 | arXiv:2606.04628v1 | paper-v1:2606.04628 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04628 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04628 | yes |
| SF-2026-ARXIV-2606-04769 | arXiv:2606.04769v1 | paper-v1:2606.04769 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04769 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04769 | yes |
| SF-2026-ARXIV-2606-04778 | arXiv:2606.04778v1 | paper-v1:2606.04778 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04778 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04778 | yes |
| SF-2026-ARXIV-2606-04799 | arXiv:2606.04799v1 | paper-v1:2606.04799 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04799 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04799 | yes |
| SF-2026-ARXIV-2606-04850 | arXiv:2606.04850v1 | paper-v1:2606.04850 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04850 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04903 | arXiv:2606.04903v1 | paper-v1:2606.04903 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04903 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04908 | arXiv:2606.04908v1 | paper-v1:2606.04908 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-04908 | self | — | new_in_window | INFER-GPU-MEMORY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-04923 | arXiv:2606.04923v1 | paper-v1:2606.04923 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04923 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-04923 | yes |
| SF-2026-ARXIV-2606-04929 | arXiv:2606.04929v1 | paper-v1:2606.04929 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-04929 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-04929 | yes |
| SF-2026-ARXIV-2606-05004 | arXiv:2606.05004v1 | paper-v1:2606.05004 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05004 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05029 | arXiv:2606.05029v1 | paper-v1:2606.05029 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05029 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05029 | yes |
| SF-2026-ARXIV-2606-05037 | arXiv:2606.05037v1 | paper-v1:2606.05037 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05037 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05037 | yes |
| SF-2026-ARXIV-2606-05043 | arXiv:2606.05043v1 | paper-v1:2606.05043 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05043 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05043 | yes |
| SF-2026-ARXIV-2606-05122 | arXiv:2606.05122v1 | paper-v1:2606.05122 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05122 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05122 | yes |
| SF-2026-ARXIV-2606-05241 | arXiv:2606.05241v1 | paper-v1:2606.05241 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05241 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05241 | yes |
| SF-2026-ARXIV-2606-05271 | arXiv:2606.05271v1 | paper-v1:2606.05271 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05271 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05304 | arXiv:2606.05304v1 | paper-v1:2606.05304 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05304 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-05304 | yes |
| SF-2026-ARXIV-2606-05308 | arXiv:2606.05308v1 | paper-v1:2606.05308 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05308 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05308 | yes |
| SF-2026-ARXIV-2606-05339 | arXiv:2606.05339v1 | paper-v1:2606.05339 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05339 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05339 | yes |
| SF-2026-ARXIV-2606-05378 | arXiv:2606.05378v1 | paper-v1:2606.05378 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05378 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05378 | yes |
| SF-2026-ARXIV-2606-05384 | arXiv:2606.05384v1 | paper-v1:2606.05384 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05384 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05384 | yes |
| SF-2026-ARXIV-2606-05391 | arXiv:2606.05391v1 | paper-v1:2606.05391 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05391 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05395 | arXiv:2606.05395v1 | paper-v1:2606.05395 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05395 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05395 | yes |
| SF-2026-ARXIV-2606-05396 | arXiv:2606.05396v1 | paper-v1:2606.05396 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05396 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05403 | arXiv:2606.05403v1 | paper-v1:2606.05403 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05403 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05403 | yes |
| SF-2026-ARXIV-2606-05414 | arXiv:2606.05414v1 | paper-v1:2606.05414 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05414 | self | — | new_in_window | PLATFORM-MONITORING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-05415 | arXiv:2606.05415v1 | paper-v1:2606.05415 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05415 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05415 | yes |
| SF-2026-ARXIV-2606-05433 | arXiv:2606.05433v1 | paper-v1:2606.05433 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05433 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05433 | yes |
| SF-2026-ARXIV-2606-05495 | arXiv:2606.05495v1 | paper-v1:2606.05495 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-05495 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-05495 | yes |
| SF-2026-ARXIV-2606-05523 | arXiv:2606.05523v1 | paper-v1:2606.05523 | 2026-W23 | 2026-06-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-05523 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-06529 | arXiv:2606.06529v1 | paper-v1:2606.06529 | 2026-W23 | 2026-06-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-06529 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06529 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
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
| SF-2026-ARXIV-2606-06529 | RP-b9508ae9722c6a52 | deep | arXiv:2606.06529v1 | SRC-ARXIV@arXiv:2606.06529v1 | https://arxiv.org/html/2606.06529v1 §3 Methodology | https://arxiv.org/html/2606.06529v1 §4 Results | https://arxiv.org/html/2606.06529v1 §4.4 Limitations | Not Disclosed — exact v1 does not disclose a versioned public artifact | claim:SF-2026-ARXIV-2606-06529 | complete |

**Source Reviews**

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
<!-- review:SF-2026-ARXIV-2606-06529:start -->
### 2606.06529 — Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety

**问题、旧方案与约束变化。** AI-control evaluation 常让 red-team 在固定频率攻击；真实策略会选择监控弱、收益高的时机并在风险上升时停止，使固定频率高估安全。

**Mechanism、state / data / control owner 与实现。** 论文把策略拆成 start policy 与 stop policy，并在有限 human audit budget 下与 monitor 交互。episode state/monitor score 是数据，attacker policy 掌握是否发起/终止，blue protocol 决定审计和阻断。

**Evaluation contract、证明与未证明。** BashArena/LinuxArena 与1% audit budget 只证明所测 attacker/monitor 上 strategic selection显著降低 empirical safety；没有给出所有 agentic domains 的绝对安全率。

**Trade-off、failure mode 与旧方案共存边界。** 更强 adaptive red team提高压力真实性，却使复现实验、coverage 和归因更难；能力很弱或每步全审计时 fixed attack 仍可作基线。

**演进关系与系统位置。** 这是 PLATFORM-EVALUATION-SYSTEM/PLATFORM-SECURITY 的 Direct Evolution：control eval 从静态 attack frequency 升级为有状态 adversarial policy。

**Exact-v1 locators。** Method/Identity：`https://arxiv.org/html/2606.06529v1 §3 Methodology`；Evaluation：`https://arxiv.org/html/2606.06529v1 §4 Results`；Limitations/Counterevidence：`https://arxiv.org/html/2606.06529v1 §4.4 Limitations`；Artifact：`Not Disclosed — exact v1 does not disclose a versioned public artifact`。

<!-- claim:SF-2026-ARXIV-2606-06529:start -->可引用结论只限 `arXiv:2606.06529v1` 的上述机制与绑定 evaluation contract。未披露的模型、硬件、精度、长度、batch、concurrency、SLO 或跨工作负载外推均不成立；旧方案在新增约束不成立时继续有效。<!-- claim:SF-2026-ARXIV-2606-06529:end -->
<!-- review:SF-2026-ARXIV-2606-06529:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
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
| SF-2026-ARXIV-2606-06529 | Disclosed — BashArena/LinuxArena 与1% audit budget 只证明所测 attacker/monitor 上 strategic selection显著降低 empirical safety；没有给出所有 agentic domains 的绝对安全率。 Locator: https://arxiv.org/html/2606.06529v1 §4 Results | Disclosed — Opus 4.6 attacker, MiMo-V2-Flash monitor, GPT-OSS-120B scorers | Not Disclosed — exact-v1 evaluation/setup text does not bind hardware/topology | Not Disclosed — exact-v1 evaluation/setup text does not bind precision/quantization | Not Disclosed — exact-v1 evaluation/setup text does not bind input/context length | Not Disclosed — exact-v1 evaluation/setup text does not bind output length | Not Disclosed — exact-v1 evaluation/setup text does not bind batch size | Not Disclosed — exact-v1 evaluation/setup text does not bind request concurrency | Not Disclosed — exact-v1 evaluation/setup text does not bind an acceptance SLO; a timeout or reported percentile alone is not an SLO | Disclosed — §3.3 reports safety, caught rate and red-team success under trajectory-level audit budget |

`Not Disclosed` is a full-text negative conclusion over exact-v1 Evaluation/Setup/Table text. Background examples, related work, future model names, request rate and observed percentiles are not treated as model, concurrency or SLO disclosures.

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-04329 | score_7_9 | not_selected | — | — | 这是 AGENT-MEMORY 的 Direct Evolution：从“上下文窗口内的不可信 token”扩展为“具有写权限、生命周期和再次执行机会的持久状态”。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MEMORY`; §4 只在所列 agent、memory channel 与攻击类上证明更激进的写入/检索策略与更高可利用性相关，并显示现有 prompt-injection defenses 未覆盖这些路径；它没有证明所有 memory 产品、模型或防御都会同样失败。 结构化 provenance、写权限与读取 gate 能缩小攻击面，但会牺牲自动记忆覆盖率并增加状态审计成本；不保存跨会话状态的 assistant 仍可维持较简单的会话隔离。 The family remains fully reviewed at score 3/3/3; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04329 |
| SF-2026-ARXIV-2606-04384 | score_7_9 | not_selected | — | — | 这是 TRAIN-PRETRAINING/PLATFORM-SECURITY 的 Direct Evolution：从每步统一记账到把 release decision 本身纳入 privacy mechanism。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-SECURITY`; 实验只比较指定数据集、模型、clip/noise 和会计配置下的 privacy–utility；其贡献是修正 formal accounting contract，而不是证明任何 ε 下都优于普通 DPSGD。 选择性发布可避免部分低价值噪声更新，却增加会计复杂度并使 utility 对 release rule 敏感；无法证明选择事件独立性时，应退回保守 accountant 或标准 DPSGD。 The family remains fully reviewed at score 3/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04384 |
| SF-2026-ARXIV-2606-04402 | forced_review | not_selected | — | — | 这是 INFER-REQUEST-LIFECYCLE/PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：accuracy scheduler 上增加 risk-weighted objective，而非替代底层 execution engine。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-SCHEDULING`; §7 在指定 SWE-bench solver pool 与 consequence proxy 上证明预算可向高后果任务重分配；它没有证明 consequence label 无偏、也没有给出跨领域生产事故成本。 后果加权降低高代价错误，但可能因 predictor 偏差饿死低分任务并增加 tail latency；错误代价近似相同时，difficulty-only routing 仍更简单。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04402 |
| SF-2026-ARXIV-2606-04413 | forced_review | not_selected | — | — | 这是 TRAIN-SFT 的 Alternative Branch：把“拒答率”拆成独立训练目标，不再当作整体 alignment 的代理变量。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `TRAIN-SFT`; §§2,4–6 证明若干 helpful-only recipes 会产生系统性 misgeneralization，且文档训练或 character 数据能缓解所测指标；没有证明存在通用 harmlessness-preserving recipe。 更少 refusal 提高危险能力可测性，却扩大部署风险且可能破坏 persona 一致性；受控 capability evaluation 可采用它，面向用户的模型仍需独立 harmlessness gate。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04413 |
| SF-2026-ARXIV-2606-04415 | score_7_9 | selected | DA-20260604-NPU-VIRTUALIZATION | — | 这是 INFER-PD-DISAGGREGATION 与 PLATFORM-RESOURCE-SCHEDULING 的 Direct Evolution：从设备级 allocation 细化为阶段级可重绑定资源。 Full-frontier selection: among the eight 3/3/3 families, this is the only inference-hardware lane that turns prefill/decode phase identity into a rebindable NPU resource contract; it is non-overlapping with the selected post-training-security and multi-agent-state lanes. The exact-v1 result is bounded to Ascend 910C/CloudMatrix384 and the stated TTFT/TPOT slices. Mechanism owner: FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。 | analysis:DA-20260604-NPU-VIRTUALIZATION |
| SF-2026-ARXIV-2606-04425 | score_7_9 | not_selected | — | — | 这是 AGENT-MEMORY/PLATFORM-SECURITY 的 Direct Evolution：prompt injection 从瞬时输入攻击演变为持久状态供应链攻击。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MEMORY`; §5 在162个跨会话 case 中分别测 WSR、IR、AR 与 E2E-ASR，证明瓶颈可出现在不同阶段；它没有评估所有持久介质或给出已验证的通用 defense。 写入审批、taint/provenance 与重新纳入 gate 增强隔离，却降低 agent 自动积累知识的能力；无持久状态系统仍可用 session-bound 防护。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04425 |
| SF-2026-ARXIV-2606-04459 | forced_review | not_selected | — | — | 这是 PLATFORM-SECURITY 的 Principle Reuse：输出最小化从 logits 扩展到任何稳定的相对排序信号。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-SECURITY`; PDF §5 只在约50组 ranking 与指定拟合尝试下证明可区分/近似暴露；没有证明能恢复完整权重或对所有解码/API 变体都不可伪造。 限制排名深度、加噪或速率限制能减弱签名，却降低排序 API 的可用性；若客户端只需最终文本，不暴露 token rank 仍是更小接口。 The family remains fully reviewed at score 2/2/1; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04459 |
| SF-2026-ARXIV-2606-04522 | score_7_9 | not_selected | — | — | 这是 AGENT-RAG/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：retrieval gate 从集合重合转向对下游有效性的可验证代理。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 跨所列 ANN algorithms/datasets 的实验只证明 Recall@k 与 distance quality/下游 utility 可分离，以及替代 metric 改变效率结论；没有证明 1/Ratio@k 适合所有语义任务。 distance ratio 无 judge、成本低，但仍继承 embedding metric 的偏差；业务需要离散 exact neighbors 时 Recall@k 仍是正确 contract。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04522 |
| SF-2026-ARXIV-2606-04557 | score_7_9 | not_selected | — | — | 这是 INFER-KV-CACHE 的 Direct Evolution：KV 从单请求临时状态演变为可训练、可组合、可分层存储的文档 artifact。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `INFER-KV-CACHE`; §§3–4 在指定 Qwen3-8B、数据集和 retrieval/oracle 选择下证明百万 token 集合可扩展及 token savings；没有证明跨模型可移植或线上并发延迟。 预计算状态减少 prefill，却引入训练、artifact identity、选择错误与存储迁移成本；内容变化频繁或请求不复用时，普通 RAG/prefill 更合适。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04557 |
| SF-2026-ARXIV-2606-04581 | score_7_9 | not_selected | — | — | 这是 INFER-SPECULATIVE-DECODING/INFER-DISTRIBUTED-RUNTIME 的 Direct Evolution：proposal ownership 从同机 draft model 扩展到多接入设备。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `INFER-SPECULATIVE-DECODING`; §VI 只在所列模型对、A100 edge server 与模拟网络条件下证明 sum token goodput；没有证明公网抖动、生产 tail SLO 或不同 tokenizer 的效果。 合作生成分摊 server compute，却增加通信、同步和 rejected-draft 浪费；链路差或本地 SLM 弱时，server-only decoding 仍可能更快。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04581 |
| SF-2026-ARXIV-2606-04594 | score_7_9 | not_selected | — | — | 这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：observability 从性能 telemetry 扩展为跨实现的语义正确性证据。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-TRACE`; §5 的 pass@1/pass@5 只对作者构造的真实 silent-error benchmark 与指定 backend/模型成立；没有证明 reference 自身无错或覆盖所有 nondeterminism。 中间态比对提高可诊断性，却要求可观测点、可比 reference 与额外存储/执行；无法复现或跨硬件数值漂移大时仍需 invariant/metamorphic tests。 The family remains fully reviewed at score 3/3/3; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04594 |
| SF-2026-ARXIV-2606-04628 | score_7_9 | not_selected | — | — | 这是 AGENT-MEMORY 的 Direct Evolution：从 token budget 管理提升为有地址、权限和事务操作的状态管理。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MEMORY`; Qwen3-8B Q4 probes 只证明特定 block 位置/分组会改变任务成功率以及这些 primitives 可调节位置；没有证明通用长期记忆质量或多租户隔离。 显式 registry 提供权限与回滚，却增加 policy 配置和 block lifecycle 复杂度；短会话、无写入的 prompt 仍可直接拼接。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04628 |
| SF-2026-ARXIV-2606-04769 | score_7_9 | not_selected | — | — | 这是 AGENT-MCP/PLATFORM-SECURITY 的 Direct Evolution：protocol conformance 从 wire schema 扩展到描述、代码和副作用的一致性。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MCP`; measurement 只对采样的真实 MCP repositories 与分类 taxonomy 证明 DCI 存在并可被检测；没有证明 classifier 能替代 sandbox/runtime enforcement。 静态/语义检查提前发现 drift，却有解析覆盖和 LLM 误判；高风险工具仍需 capability policy 与运行时审计。 The family remains fully reviewed at score 3/3/3; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04769 |
| SF-2026-ARXIV-2606-04778 | score_7_9 | not_selected | — | — | 这是 TRAIN-SFT/PLATFORM-SECURITY 的 Direct Evolution：alignment target 从首 token/final answer 延伸到整个生成状态机。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-SECURITY`; §4 在三类7B/8B instruct models和指定 harmfulness suites 上证明中途脆弱性与训练增益；没有证明对所有 white-box activation intervention 或更大模型成立。 轨迹训练覆盖更多攻击位置，却增加合成扰动成本并可能压制正常纠错/用户改写；只需静态单轮拒答的系统仍可使用较轻的 output filter。 The family remains fully reviewed at score 3/2/3; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04778 |
| SF-2026-ARXIV-2606-04799 | score_7_9 | not_selected | — | — | 这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：从采集信号扩展到可被 agent 消费的语义对象与关系层。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-TRACE`; 作者案例只证明统一模型支持所测 RCA/query workflow；没有证明任意 vendor schema 自动可对齐或 ontology 长期无漂移。 object-centric layer提高跨源推理，却带来 schema governance、identity resolution 和摄取成本；单一服务的小规模诊断仍可直接查原生 telemetry。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04799 |
| SF-2026-ARXIV-2606-04850 | forced_review | not_selected | — | — | 这是 INFER-TENSORRT-LLM execution-plan owner 的 Alternative Branch：从 deterministic mapping 扩展到 uncertainty-aware co-design。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-TENSORRT-LLM`; §V 的 simulation 只证明指定 workload、processor model、uncertainty distribution 与 cost function 下的联合方案；没有证明真实 chip tape-out、跨 workload 稳健性或生产 SLO。 联合搜索减少阶段割裂，却增加模型假设、搜索成本与 distribution misspecification 风险；制造波动可忽略或 toolchain 必须独立演进时，分阶段设计仍更易验证。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04850 |
| SF-2026-ARXIV-2606-04903 | forced_review | not_selected | — | — | 这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Alternative Branch：从概率式 planner 转向人定义语义边界内的可验证执行。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-SECURITY`; 论文给出 healthcare billing 与 vulnerability disclosure 两个 appropriate-domain 实现及语义论证；没有证明开放世界任务能被完整 ontologize，也未证明 LLM 感知输入正确。 可证明的 typed path 增强审计，却依赖昂贵的 ontology maintenance 并限制开放式推理；低风险探索仍可保留自由规划再加事后 review。 The family remains fully reviewed at score 2/2/1; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04903 |
| SF-2026-ARXIV-2606-04908 | forced_review | not_selected | — | — | 这是 PLATFORM-STORAGE/INFER-EXECUTION 的 Direct Evolution：accelerator 从数据消费者变成远端存储 I/O 的主动 owner。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-GPU-MEMORY`; 实验只对 AMD EPYC 9654、768GB DDR5、A100 40GB 与指定 AFA/network configuration 的 throughput/latency 成立；不证明通用 filesystem semantics 或 failure recovery。 绕过 CPU 降低 data-path overhead，却增加 GPU runtime、metadata consistency 与隔离复杂度；控制面密集、GPU 利用低或共享 storage policy 强时 CPU-centric 路线仍合理。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04908 |
| SF-2026-ARXIV-2606-04923 | score_7_9 | not_selected | — | — | 这是 TRAIN-RLHF/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：reward model 从可信 oracle 变成需做 adversarial validation 的系统组件。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; §4/appendices 只证明所注入 biases 可被发现/利用以及 detector 在该环境中的表现；没有证明真实生产 judge 的全部 latent bias 被覆盖。 可控 testbed 提高可复现性，却可能过拟合人为 bias；真实 release gate 仍需独立 human/held-out evaluator 和 reward-channel monitoring。 The family remains fully reviewed at score 3/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-04923 |
| SF-2026-ARXIV-2606-04929 | score_7_9; potential_books_delta | selected | DA-20260604-CROSS-STAGE-POISONING | — | 这是 TRAIN-SFT→TRAIN-DPO 的 Direct Evolution：安全 owner 从单个 trainer 上移到整个 post-training checkpoint chain。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that makes checkpoint handoff across SFT and preference optimization a security state channel; existing single-stage data-poisoning prose does not own the cross-stage orchestrator. It is non-overlapping with NPU phase virtualization and multi-agent public-state projection. Mechanism owner: 论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。 | analysis:DA-20260604-CROSS-STAGE-POISONING |
| SF-2026-ARXIV-2606-05004 | forced_review | not_selected | — | — | 这是 INFER-BATCHING/PLATFORM-SECURITY 的 Principle Reuse：batch 不再只做吞吐优化，也成为 privacy mixing boundary。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-SECURITY`; 作者实验只在指定 prompts/models/privacy attack 与 GPT-5.2 attribute inference slice 上报告 utility/cost；没有给出对任意 side channel 或恶意 provider 的 cryptographic secrecy。 model-agnostic batching降低调用成本，却引入语义分组错误、额外 queries 与群体依赖；高敏感、强对手场景仍需 trusted execution、local model 或 cryptographic protocol。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05004 |
| SF-2026-ARXIV-2606-05029 | score_7_9 | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation contract 从 metric/config 扩展到 estimand、identification assumption 与外推边界。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 论文提供方法论分析而非新的模型 benchmark；它证明的是各策略存在可枚举的因果威胁，不证明某一策略在所有研究问题上失效。 显式 validity contract 提高结论可审计性，却要求更多假设记录与 sensitivity analysis；资源足够时，直接 controlled replication 仍更强。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05029 |
| SF-2026-ARXIV-2606-05037 | score_7_9 | not_selected | — | — | 这是 AGENT-TOOL-USE/API contract 的 Direct Evolution：错误从诊断文本变成受 schema 约束的下一步控制接口。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-TOOL-CALLING`; N=30/cell、3 models、10 adversarial tasks 的 pilot 只证明 Anthropic models 上显著提升且 gpt-4o lift 不显著；不能外推为所有 API 或 agent。 结构建议提高恢复率，却扩大 API contract、可能泄露 schema/security细节；人工客户端或简单错误仍可使用普通 status/message。 The family remains fully reviewed at score 3/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05037 |
| SF-2026-ARXIV-2606-05043 | score_7_9 | not_selected | — | — | 这是 AGENT-WORKFLOW/AGENT-MULTI-AGENT 的 Direct Evolution：interaction contract 从隐式代码提升为独立、可执行、可验证 artifact。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MULTI-AGENT`; 案例只证明 checkout 子协议可表达并与所测 UCP implementation 互通；没有覆盖 UCP 全部域、故障恢复或生产规模。 声明式协议增强一致性和渐进替换，却要求 schema/protocol evolution governance；局部、单进程 workflow 仍可保留直接代码。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05043 |
| SF-2026-ARXIV-2606-05122 | score_7_9 | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：把自评看成需校准的测量通道，而非生成概率的直接解释。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 三 benchmark、160 examples、Qwen3-4B-Base 结果只证明所测 judge/attributes 上校准改善且 answer quality 保持；不等于事实正确性或模型知道未知。 少数据 elicitation 降低训练成本，却继承外部 judge bias，并可能把 confidence 误当 truth；高风险 claims 仍需外部 evidence verification。 The family remains fully reviewed at score 3/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05122 |
| SF-2026-ARXIV-2606-05241 | score_7_9 | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation isolation 从训练集去重扩展到 inference-time retrieval data flow。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 六个公开 benchmark 上最多约4%的 inflation 只针对所测 agents/search index/time；没有证明私有 benchmark 或未来索引同样幅度。 trace-aware filtering提高有效性，却可能误删合法检索并增加评测成本；真实开放网任务仍需允许搜索，只是不能与 closed-book score 混算。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05241 |
| SF-2026-ARXIV-2606-05271 | forced_review | not_selected | — | — | 这是 INFER-TENSORRT-LLM execution-plan 的 Direct Evolution：placement 粒度从 model 降到 fused operator，并把 transfer cost 纳入路径。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-TENSORRT-LLM`; 实验只对 Intel Core Ultra 平台、所列10类模型/FP16/INT8 与 profiler cost model 证明 latency/energy mapping；未证明动态 contention 下仍最优。 operator mapping提高异构利用率，却增加切分、transfer、profiling 和 recompile 成本；单一 PU 已匹配 workload 或模型很小时 model-level placement 更简单。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05271 |
| SF-2026-ARXIV-2606-05304 | score_7_9; potential_books_delta | selected | DA-20260604-ACTION-STATE-COMMUNICATION | — | 这是 AGENT-MULTI-AGENT 的 Direct Evolution：通信从 transcript forwarding 变成有 ownership 的状态复制协议。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that replaces transcript forwarding with an explicit public action-state projection while preserving private reasoning ownership; current Message-not-State prose lacks that projection mechanism. It is non-overlapping with NPU resource rebinding and cross-stage poisoning. Mechanism owner: PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。 | analysis:DA-20260604-ACTION-STATE-COMMUNICATION |
| SF-2026-ARXIV-2606-05308 | score_7_9 | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：LLM judge 从替代真值变成可校正的低成本测量器。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; ESCI 的30 human-gold/60,000 judge slice 只证明所列 ranking metrics 的校正与区间性质；不证明 judge 单样本标签正确或任意分布漂移下仍无偏。 PPI 降低人工标注量，却依赖 probability sample、稳定 estimand 和正确 variance accounting；无法随机抽样时应回到更多 human evaluation。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05308 |
| SF-2026-ARXIV-2606-05339 | score_7_9 | not_selected | — | — | 这是 AGENT-MCP/PLATFORM-OBSERVABILITY 的 Layering / Dependency：wire contract 之上增加 server-runtime reliability owner。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MCP`; 经验 taxonomy 只代表筛选时间窗、活跃 repositories 与 issue-reporting bias；不能当作运行时故障率或完备故障集合。 分类改善 triage/测试覆盖，却不会自动检测 silent faults，且 taxonomy 会随协议演化；单一 MCP server 仍需本地 invariants、chaos tests 和 tracing。 The family remains fully reviewed at score 3/3/3; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05339 |
| SF-2026-ARXIV-2606-05378 | score_7_9 | not_selected | — | — | 这是 MODEL-ATTENTION/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution（认知修正）：selectivity 被降级为 discovery evidence，causality 需要跨条件干预。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `WORLDVIEW-REPRESENTATION`; 12个 task-model cells 无两项共享可比 primary screen，证明该 recipe 的具体 circuit 不可稳定移植；不证明机制完全不可解释或更大模型也无共享结构。 更严格 null/干预降低夸大结论，却提高实验成本并可能错过分布式机制；pattern screening 仍可作候选发现，但不能独立成为 causal claim。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05378 |
| SF-2026-ARXIV-2606-05384 | score_7_9 | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：judge contract 从纯函数扩展为有状态交互协议。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; MT-Bench/AlpacaEval、GPT-4o/4o-mini judges 与100 paired instances 只证明所测 interaction 可改变判定；不证明所有 judge 或无对话 benchmark 均可操纵。 冻结 judge context 或禁止 post-decision interaction增强可复现性，却不适合需要申诉的流程；有申诉时应使用独立复审而非继续劝说同一 judge。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05384 |
| SF-2026-ARXIV-2606-05391 | forced_review | not_selected | — | — | 这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Layering / Dependency：human-in-the-loop 从单一批准点演变为分阶段控制面。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `AGENT-PLATFORM`; 17名经验开发者的定性访谈提供早期实践锚点，不是频率估计、因果效果或行业代表样本。 多阶段 oversight 提高可控性，却带来认知负担、alert fatigue 和吞吐下降；低风险、可回滚任务可减少实时介入。 The family remains fully reviewed at score 2/2/1; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05391 |
| SF-2026-ARXIV-2606-05395 | score_7_9 | not_selected | — | — | 这是 MULTIMODAL-EMBODIED-VLA/AGENT-SKILL 的 Direct Evolution：skill 从 prompt artifact 变成带形式契约和发布 gate 的执行组件。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-WORKFLOW`; §5 在两平台、11 specifications、400 plans及40 plans/skill 的局部合同上比较 compliance；没有证明 perception/actuator model 完整或 sim-to-real 物理安全。 formal gate提高未采样路径约束，却依赖 proposition alignment，且 state-space/solver 成本可能很高；低风险 skill 仍可用 test+monitoring。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05395 |
| SF-2026-ARXIV-2606-05396 | forced_review | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM 的 Alternative Branch：能力评测先控制 refusal policy，再评价任务能力，但不把 edited model 当部署方案。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-EVALUATION-SYSTEM`; Python/CWE-89、Qwen2.5-Coder 3B/7B/14B、Q4_K_M/Ollama 的初步实验只证明该受限 case；不证明编辑保持其他安全性或能构造高质量通用漏洞数据。 移除 refusal 改善 capability measurement，却显著扩大滥用风险并可能损坏模型行为；只能在隔离研究环境使用，生产模型不应采用。 The family remains fully reviewed at score 2/2/1; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05396 |
| SF-2026-ARXIV-2606-05403 | score_7_9 | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM/AGENT-RAG 的 Direct Evolution：source ranking 从文风/相关性扩展为可验证的 claim-level validity gate。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 五模型、三领域的行为 dissociation 只证明所构造 impossible CI 等操纵下的 epistemic blind spot；不证明所有引用审查或 tool-verified agent 都失败。 外部统计 verifier/claim decomposition提高可靠性，却增加延迟并要求可机器检查的证据；低风险摘要可保留模型合成但标注不确定性。 The family remains fully reviewed at score 3/2/3; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05403 |
| SF-2026-ARXIV-2606-05414 | forced_review | not_selected | — | — | 这是 AGENT-WORKFLOW/PLATFORM-OBSERVABILITY 的 Direct Evolution：监控从事后 outcome 变成随 trajectory 更新的在线控制信号。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-MONITORING`; §§4–5 只在指定 dialog/agent datasets 与 metrics 上证明比 prefix-label baselines 更好的 early-warning tradeoff；不证明 production threshold 或 causal root cause。 弱监督减少 turn labels，却可能把相关语句误作早期因果信号；风险低或误停代价高时应延后 alert 并保留完整执行。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05414 |
| SF-2026-ARXIV-2606-05415 | score_7_9 | not_selected | — | — | 这是 TRAIN-DATA→AGENT-RAG 的 Direct Evolution：schema 从摄取产物变成贯穿构建与查询的可执行、带 provenance 控制面。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-FOUNDATIONS`; §4 只在作者数据与 query workload 上证明 ingestion/retrieval traceability；没有证明任意隐含语义可自动恢复或 schema extension 无冲突。 共享契约提高一致性，却增加 catalog governance、identity resolution 和 migration；同质单源可直接使用原生 schema/search。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05415 |
| SF-2026-ARXIV-2606-05433 | score_7_9 | not_selected | — | — | 这是 PLATFORM-SECURITY/GOVERNANCE 的 Layering / Dependency：在既有发布审计与 provenance owner 上增加可验证计算记录；现有安全章节能够承载，无需 Structural Candidate。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-SECURITY`; Appendix B/G 给出 proof-cost估算与协议论证，而非 frontier-scale end-to-end deployment；没有证明硬件 telemetry 完整、spec 与真实训练语义完全一致。 零知识审计保护模型/数据机密，却增加 commitment、proof、trusted instrumentation 与 protocol complexity；低风险训练可继续使用日志和第三方 audit。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05433 |
| SF-2026-ARXIV-2606-05495 | score_7_9 | not_selected | — | — | 这是 INFER-EXECUTION 的 Principle Reuse：continuous scheduling 的状态所有权下沉到 CUDA graph pipeline，但不能直接外推成 LLM runtime 结论。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `INFER-SCHEDULING`; §5 在 RTX3090/5090 两平台、六 workloads 和 workload-specific batch sweep 上报告 throughput/overhead；不证明 LLM serving、跨 GPU 或生产 tail SLO。 事件触发减少 host gap，却增加 buffer memory、event dependency 与 scheduler complexity；低并发、单 graph workload 仍可用同步 replay。 The family remains fully reviewed at score 3/3/3; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05495 |
| SF-2026-ARXIV-2606-05523 | forced_review | not_selected | — | — | 这是 TRAIN-RLHF/PLATFORM-SECURITY 的 Direct Evolution：red teaming 从发布前数据集变成闭环 attacker–defender control process。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `TRAIN-RLHF`; §5/appendices 只在 Llama-3.1-8B-Instruct、指定 attacks/evaluators 上证明所测 robustness 变化；未证明对 frontier models、长期自博弈或未知攻击无 reward hacking。 在线生成 hard negatives提高适应性，却增加训练成本、评价器依赖和 catastrophic alignment drift；稳定威胁下 curated SFT 仍更可控。 The family remains fully reviewed at score 2/2/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-05523 |
| SF-2026-ARXIV-2606-06529 | score_7_9 | not_selected | — | — | 这是 PLATFORM-EVALUATION-SYSTEM/PLATFORM-SECURITY 的 Direct Evolution：control eval 从静态 attack frequency 升级为有状态 adversarial policy。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; BashArena/LinuxArena 与1% audit budget 只证明所测 attacker/monitor 上 strategic selection显著降低 empirical safety；没有给出所有 agentic domains 的绝对安全率。 更强 adaptive red team提高压力真实性，却使复现实验、coverage 和归因更难；能力很弱或每步全审计时 fixed attack 仍可作基线。 The family remains fully reviewed at score 3/3/2; no review duty is dropped. | analysis-decision:SF-2026-ARXIV-2606-06529 |

<!-- analysis-decision:SF-2026-ARXIV-2606-04329:start -->
这是 AGENT-MEMORY 的 Direct Evolution：从“上下文窗口内的不可信 token”扩展为“具有写权限、生命周期和再次执行机会的持久状态”。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MEMORY`; §4 只在所列 agent、memory channel 与攻击类上证明更激进的写入/检索策略与更高可利用性相关，并显示现有 prompt-injection defenses 未覆盖这些路径；它没有证明所有 memory 产品、模型或防御都会同样失败。 结构化 provenance、写权限与读取 gate 能缩小攻击面，但会牺牲自动记忆覆盖率并增加状态审计成本；不保存跨会话状态的 assistant 仍可维持较简单的会话隔离。 The family remains fully reviewed at score 3/3/3; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04329:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04384:start -->
这是 TRAIN-PRETRAINING/PLATFORM-SECURITY 的 Direct Evolution：从每步统一记账到把 release decision 本身纳入 privacy mechanism。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-SECURITY`; 实验只比较指定数据集、模型、clip/noise 和会计配置下的 privacy–utility；其贡献是修正 formal accounting contract，而不是证明任何 ε 下都优于普通 DPSGD。 选择性发布可避免部分低价值噪声更新，却增加会计复杂度并使 utility 对 release rule 敏感；无法证明选择事件独立性时，应退回保守 accountant 或标准 DPSGD。 The family remains fully reviewed at score 3/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04384:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04402:start -->
这是 INFER-REQUEST-LIFECYCLE/PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：accuracy scheduler 上增加 risk-weighted objective，而非替代底层 execution engine。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-SCHEDULING`; §7 在指定 SWE-bench solver pool 与 consequence proxy 上证明预算可向高后果任务重分配；它没有证明 consequence label 无偏、也没有给出跨领域生产事故成本。 后果加权降低高代价错误，但可能因 predictor 偏差饿死低分任务并增加 tail latency；错误代价近似相同时，difficulty-only routing 仍更简单。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04402:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04413:start -->
这是 TRAIN-SFT 的 Alternative Branch：把“拒答率”拆成独立训练目标，不再当作整体 alignment 的代理变量。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `TRAIN-SFT`; §§2,4–6 证明若干 helpful-only recipes 会产生系统性 misgeneralization，且文档训练或 character 数据能缓解所测指标；没有证明存在通用 harmlessness-preserving recipe。 更少 refusal 提高危险能力可测性，却扩大部署风险且可能破坏 persona 一致性；受控 capability evaluation 可采用它，面向用户的模型仍需独立 harmlessness gate。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04413:end -->
<!-- analysis:DA-20260604-NPU-VIRTUALIZATION:start -->
这是 INFER-PD-DISAGGREGATION 与 PLATFORM-RESOURCE-SCHEDULING 的 Direct Evolution：从设备级 allocation 细化为阶段级可重绑定资源。 Full-frontier selection: among the eight 3/3/3 families, this is the only inference-hardware lane that turns prefill/decode phase identity into a rebindable NPU resource contract; it is non-overlapping with the selected post-training-security and multi-agent-state lanes. The exact-v1 result is bounded to Ascend 910C/CloudMatrix384 and the stated TTFT/TPOT slices. Mechanism owner: FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。
<!-- analysis:DA-20260604-NPU-VIRTUALIZATION:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04425:start -->
这是 AGENT-MEMORY/PLATFORM-SECURITY 的 Direct Evolution：prompt injection 从瞬时输入攻击演变为持久状态供应链攻击。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MEMORY`; §5 在162个跨会话 case 中分别测 WSR、IR、AR 与 E2E-ASR，证明瓶颈可出现在不同阶段；它没有评估所有持久介质或给出已验证的通用 defense。 写入审批、taint/provenance 与重新纳入 gate 增强隔离，却降低 agent 自动积累知识的能力；无持久状态系统仍可用 session-bound 防护。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04425:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04459:start -->
这是 PLATFORM-SECURITY 的 Principle Reuse：输出最小化从 logits 扩展到任何稳定的相对排序信号。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-SECURITY`; PDF §5 只在约50组 ranking 与指定拟合尝试下证明可区分/近似暴露；没有证明能恢复完整权重或对所有解码/API 变体都不可伪造。 限制排名深度、加噪或速率限制能减弱签名，却降低排序 API 的可用性；若客户端只需最终文本，不暴露 token rank 仍是更小接口。 The family remains fully reviewed at score 2/2/1; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04459:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04522:start -->
这是 AGENT-RAG/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：retrieval gate 从集合重合转向对下游有效性的可验证代理。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 跨所列 ANN algorithms/datasets 的实验只证明 Recall@k 与 distance quality/下游 utility 可分离，以及替代 metric 改变效率结论；没有证明 1/Ratio@k 适合所有语义任务。 distance ratio 无 judge、成本低，但仍继承 embedding metric 的偏差；业务需要离散 exact neighbors 时 Recall@k 仍是正确 contract。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04522:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04557:start -->
这是 INFER-KV-CACHE 的 Direct Evolution：KV 从单请求临时状态演变为可训练、可组合、可分层存储的文档 artifact。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `INFER-KV-CACHE`; §§3–4 在指定 Qwen3-8B、数据集和 retrieval/oracle 选择下证明百万 token 集合可扩展及 token savings；没有证明跨模型可移植或线上并发延迟。 预计算状态减少 prefill，却引入训练、artifact identity、选择错误与存储迁移成本；内容变化频繁或请求不复用时，普通 RAG/prefill 更合适。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04557:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04581:start -->
这是 INFER-SPECULATIVE-DECODING/INFER-DISTRIBUTED-RUNTIME 的 Direct Evolution：proposal ownership 从同机 draft model 扩展到多接入设备。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `INFER-SPECULATIVE-DECODING`; §VI 只在所列模型对、A100 edge server 与模拟网络条件下证明 sum token goodput；没有证明公网抖动、生产 tail SLO 或不同 tokenizer 的效果。 合作生成分摊 server compute，却增加通信、同步和 rejected-draft 浪费；链路差或本地 SLM 弱时，server-only decoding 仍可能更快。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04581:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04594:start -->
这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：observability 从性能 telemetry 扩展为跨实现的语义正确性证据。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-TRACE`; §5 的 pass@1/pass@5 只对作者构造的真实 silent-error benchmark 与指定 backend/模型成立；没有证明 reference 自身无错或覆盖所有 nondeterminism。 中间态比对提高可诊断性，却要求可观测点、可比 reference 与额外存储/执行；无法复现或跨硬件数值漂移大时仍需 invariant/metamorphic tests。 The family remains fully reviewed at score 3/3/3; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04594:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04628:start -->
这是 AGENT-MEMORY 的 Direct Evolution：从 token budget 管理提升为有地址、权限和事务操作的状态管理。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MEMORY`; Qwen3-8B Q4 probes 只证明特定 block 位置/分组会改变任务成功率以及这些 primitives 可调节位置；没有证明通用长期记忆质量或多租户隔离。 显式 registry 提供权限与回滚，却增加 policy 配置和 block lifecycle 复杂度；短会话、无写入的 prompt 仍可直接拼接。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04628:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04769:start -->
这是 AGENT-MCP/PLATFORM-SECURITY 的 Direct Evolution：protocol conformance 从 wire schema 扩展到描述、代码和副作用的一致性。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MCP`; measurement 只对采样的真实 MCP repositories 与分类 taxonomy 证明 DCI 存在并可被检测；没有证明 classifier 能替代 sandbox/runtime enforcement。 静态/语义检查提前发现 drift，却有解析覆盖和 LLM 误判；高风险工具仍需 capability policy 与运行时审计。 The family remains fully reviewed at score 3/3/3; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04769:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04778:start -->
这是 TRAIN-SFT/PLATFORM-SECURITY 的 Direct Evolution：alignment target 从首 token/final answer 延伸到整个生成状态机。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-SECURITY`; §4 在三类7B/8B instruct models和指定 harmfulness suites 上证明中途脆弱性与训练增益；没有证明对所有 white-box activation intervention 或更大模型成立。 轨迹训练覆盖更多攻击位置，却增加合成扰动成本并可能压制正常纠错/用户改写；只需静态单轮拒答的系统仍可使用较轻的 output filter。 The family remains fully reviewed at score 3/2/3; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04778:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04799:start -->
这是 PLATFORM-OBSERVABILITY 的 Direct Evolution：从采集信号扩展到可被 agent 消费的语义对象与关系层。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-TRACE`; 作者案例只证明统一模型支持所测 RCA/query workflow；没有证明任意 vendor schema 自动可对齐或 ontology 长期无漂移。 object-centric layer提高跨源推理，却带来 schema governance、identity resolution 和摄取成本；单一服务的小规模诊断仍可直接查原生 telemetry。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04799:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04850:start -->
这是 INFER-TENSORRT-LLM execution-plan owner 的 Alternative Branch：从 deterministic mapping 扩展到 uncertainty-aware co-design。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-TENSORRT-LLM`; §V 的 simulation 只证明指定 workload、processor model、uncertainty distribution 与 cost function 下的联合方案；没有证明真实 chip tape-out、跨 workload 稳健性或生产 SLO。 联合搜索减少阶段割裂，却增加模型假设、搜索成本与 distribution misspecification 风险；制造波动可忽略或 toolchain 必须独立演进时，分阶段设计仍更易验证。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04850:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04903:start -->
这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Alternative Branch：从概率式 planner 转向人定义语义边界内的可验证执行。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-SECURITY`; 论文给出 healthcare billing 与 vulnerability disclosure 两个 appropriate-domain 实现及语义论证；没有证明开放世界任务能被完整 ontologize，也未证明 LLM 感知输入正确。 可证明的 typed path 增强审计，却依赖昂贵的 ontology maintenance 并限制开放式推理；低风险探索仍可保留自由规划再加事后 review。 The family remains fully reviewed at score 2/2/1; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04903:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04908:start -->
这是 PLATFORM-STORAGE/INFER-EXECUTION 的 Direct Evolution：accelerator 从数据消费者变成远端存储 I/O 的主动 owner。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-GPU-MEMORY`; 实验只对 AMD EPYC 9654、768GB DDR5、A100 40GB 与指定 AFA/network configuration 的 throughput/latency 成立；不证明通用 filesystem semantics 或 failure recovery。 绕过 CPU 降低 data-path overhead，却增加 GPU runtime、metadata consistency 与隔离复杂度；控制面密集、GPU 利用低或共享 storage policy 强时 CPU-centric 路线仍合理。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04908:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-04923:start -->
这是 TRAIN-RLHF/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：reward model 从可信 oracle 变成需做 adversarial validation 的系统组件。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; §4/appendices 只证明所注入 biases 可被发现/利用以及 detector 在该环境中的表现；没有证明真实生产 judge 的全部 latent bias 被覆盖。 可控 testbed 提高可复现性，却可能过拟合人为 bias；真实 release gate 仍需独立 human/held-out evaluator 和 reward-channel monitoring。 The family remains fully reviewed at score 3/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-04923:end -->
<!-- analysis:DA-20260604-CROSS-STAGE-POISONING:start -->
这是 TRAIN-SFT→TRAIN-DPO 的 Direct Evolution：安全 owner 从单个 trainer 上移到整个 post-training checkpoint chain。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that makes checkpoint handoff across SFT and preference optimization a security state channel; existing single-stage data-poisoning prose does not own the cross-stage orchestrator. It is non-overlapping with NPU phase virtualization and multi-agent public-state projection. Mechanism owner: 论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。
<!-- analysis:DA-20260604-CROSS-STAGE-POISONING:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05004:start -->
这是 INFER-BATCHING/PLATFORM-SECURITY 的 Principle Reuse：batch 不再只做吞吐优化，也成为 privacy mixing boundary。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-SECURITY`; 作者实验只在指定 prompts/models/privacy attack 与 GPT-5.2 attribute inference slice 上报告 utility/cost；没有给出对任意 side channel 或恶意 provider 的 cryptographic secrecy。 model-agnostic batching降低调用成本，却引入语义分组错误、额外 queries 与群体依赖；高敏感、强对手场景仍需 trusted execution、local model 或 cryptographic protocol。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05004:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05029:start -->
这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation contract 从 metric/config 扩展到 estimand、identification assumption 与外推边界。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 论文提供方法论分析而非新的模型 benchmark；它证明的是各策略存在可枚举的因果威胁，不证明某一策略在所有研究问题上失效。 显式 validity contract 提高结论可审计性，却要求更多假设记录与 sensitivity analysis；资源足够时，直接 controlled replication 仍更强。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05029:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05037:start -->
这是 AGENT-TOOL-USE/API contract 的 Direct Evolution：错误从诊断文本变成受 schema 约束的下一步控制接口。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-TOOL-CALLING`; N=30/cell、3 models、10 adversarial tasks 的 pilot 只证明 Anthropic models 上显著提升且 gpt-4o lift 不显著；不能外推为所有 API 或 agent。 结构建议提高恢复率，却扩大 API contract、可能泄露 schema/security细节；人工客户端或简单错误仍可使用普通 status/message。 The family remains fully reviewed at score 3/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05037:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05043:start -->
这是 AGENT-WORKFLOW/AGENT-MULTI-AGENT 的 Direct Evolution：interaction contract 从隐式代码提升为独立、可执行、可验证 artifact。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MULTI-AGENT`; 案例只证明 checkout 子协议可表达并与所测 UCP implementation 互通；没有覆盖 UCP 全部域、故障恢复或生产规模。 声明式协议增强一致性和渐进替换，却要求 schema/protocol evolution governance；局部、单进程 workflow 仍可保留直接代码。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05043:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05122:start -->
这是 PLATFORM-EVALUATION-SYSTEM 的 Layering / Dependency：把自评看成需校准的测量通道，而非生成概率的直接解释。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 三 benchmark、160 examples、Qwen3-4B-Base 结果只证明所测 judge/attributes 上校准改善且 answer quality 保持；不等于事实正确性或模型知道未知。 少数据 elicitation 降低训练成本，却继承外部 judge bias，并可能把 confidence 误当 truth；高风险 claims 仍需外部 evidence verification。 The family remains fully reviewed at score 3/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05122:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05241:start -->
这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：evaluation isolation 从训练集去重扩展到 inference-time retrieval data flow。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 六个公开 benchmark 上最多约4%的 inflation 只针对所测 agents/search index/time；没有证明私有 benchmark 或未来索引同样幅度。 trace-aware filtering提高有效性，却可能误删合法检索并增加评测成本；真实开放网任务仍需允许搜索，只是不能与 closed-book score 混算。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05241:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05271:start -->
这是 INFER-TENSORRT-LLM execution-plan 的 Direct Evolution：placement 粒度从 model 降到 fused operator，并把 transfer cost 纳入路径。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `INFER-TENSORRT-LLM`; 实验只对 Intel Core Ultra 平台、所列10类模型/FP16/INT8 与 profiler cost model 证明 latency/energy mapping；未证明动态 contention 下仍最优。 operator mapping提高异构利用率，却增加切分、transfer、profiling 和 recompile 成本；单一 PU 已匹配 workload 或模型很小时 model-level placement 更简单。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05271:end -->
<!-- analysis:DA-20260604-ACTION-STATE-COMMUNICATION:start -->
这是 AGENT-MULTI-AGENT 的 Direct Evolution：通信从 transcript forwarding 变成有 ownership 的状态复制协议。 Full-frontier selection: this is one of only two Books Integrate deltas and the only family that replaces transcript forwarding with an explicit public action-state projection while preserving private reasoning ownership; current Message-not-State prose lacks that projection mechanism. It is non-overlapping with NPU resource rebinding and cross-stage poisoning. Mechanism owner: PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。
<!-- analysis:DA-20260604-ACTION-STATE-COMMUNICATION:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05308:start -->
这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：LLM judge 从替代真值变成可校正的低成本测量器。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; ESCI 的30 human-gold/60,000 judge slice 只证明所列 ranking metrics 的校正与区间性质；不证明 judge 单样本标签正确或任意分布漂移下仍无偏。 PPI 降低人工标注量，却依赖 probability sample、稳定 estimand 和正确 variance accounting；无法随机抽样时应回到更多 human evaluation。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05308:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05339:start -->
这是 AGENT-MCP/PLATFORM-OBSERVABILITY 的 Layering / Dependency：wire contract 之上增加 server-runtime reliability owner。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-MCP`; 经验 taxonomy 只代表筛选时间窗、活跃 repositories 与 issue-reporting bias；不能当作运行时故障率或完备故障集合。 分类改善 triage/测试覆盖，却不会自动检测 silent faults，且 taxonomy 会随协议演化；单一 MCP server 仍需本地 invariants、chaos tests 和 tracing。 The family remains fully reviewed at score 3/3/3; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05339:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05378:start -->
这是 MODEL-ATTENTION/PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution（认知修正）：selectivity 被降级为 discovery evidence，causality 需要跨条件干预。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `WORLDVIEW-REPRESENTATION`; 12个 task-model cells 无两项共享可比 primary screen，证明该 recipe 的具体 circuit 不可稳定移植；不证明机制完全不可解释或更大模型也无共享结构。 更严格 null/干预降低夸大结论，却提高实验成本并可能错过分布式机制；pattern screening 仍可作候选发现，但不能独立成为 causal claim。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05378:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05384:start -->
这是 PLATFORM-EVALUATION-SYSTEM 的 Direct Evolution：judge contract 从纯函数扩展为有状态交互协议。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; MT-Bench/AlpacaEval、GPT-4o/4o-mini judges 与100 paired instances 只证明所测 interaction 可改变判定；不证明所有 judge 或无对话 benchmark 均可操纵。 冻结 judge context 或禁止 post-decision interaction增强可复现性，却不适合需要申诉的流程；有申诉时应使用独立复审而非继续劝说同一 judge。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05384:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05391:start -->
这是 AGENT-WORKFLOW/PLATFORM-SECURITY 的 Layering / Dependency：human-in-the-loop 从单一批准点演变为分阶段控制面。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `AGENT-PLATFORM`; 17名经验开发者的定性访谈提供早期实践锚点，不是频率估计、因果效果或行业代表样本。 多阶段 oversight 提高可控性，却带来认知负担、alert fatigue 和吞吐下降；低风险、可回滚任务可减少实时介入。 The family remains fully reviewed at score 2/2/1; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05391:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05395:start -->
这是 MULTIMODAL-EMBODIED-VLA/AGENT-SKILL 的 Direct Evolution：skill 从 prompt artifact 变成带形式契约和发布 gate 的执行组件。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `AGENT-WORKFLOW`; §5 在两平台、11 specifications、400 plans及40 plans/skill 的局部合同上比较 compliance；没有证明 perception/actuator model 完整或 sim-to-real 物理安全。 formal gate提高未采样路径约束，却依赖 proposition alignment，且 state-space/solver 成本可能很高；低风险 skill 仍可用 test+monitoring。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05395:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05396:start -->
这是 PLATFORM-EVALUATION-SYSTEM 的 Alternative Branch：能力评测先控制 refusal policy，再评价任务能力，但不把 edited model 当部署方案。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-EVALUATION-SYSTEM`; Python/CWE-89、Qwen2.5-Coder 3B/7B/14B、Q4_K_M/Ollama 的初步实验只证明该受限 case；不证明编辑保持其他安全性或能构造高质量通用漏洞数据。 移除 refusal 改善 capability measurement，却显著扩大滥用风险并可能损坏模型行为；只能在隔离研究环境使用，生产模型不应采用。 The family remains fully reviewed at score 2/2/1; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05396:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05403:start -->
这是 PLATFORM-EVALUATION-SYSTEM/AGENT-RAG 的 Direct Evolution：source ranking 从文风/相关性扩展为可验证的 claim-level validity gate。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; 五模型、三领域的行为 dissociation 只证明所构造 impossible CI 等操纵下的 epistemic blind spot；不证明所有引用审查或 tool-verified agent 都失败。 外部统计 verifier/claim decomposition提高可靠性，却增加延迟并要求可机器检查的证据；低风险摘要可保留模型合成但标注不确定性。 The family remains fully reviewed at score 3/2/3; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05403:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05414:start -->
这是 AGENT-WORKFLOW/PLATFORM-OBSERVABILITY 的 Direct Evolution：监控从事后 outcome 变成随 trajectory 更新的在线控制信号。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `PLATFORM-MONITORING`; §§4–5 只在指定 dialog/agent datasets 与 metrics 上证明比 prefix-label baselines 更好的 early-warning tradeoff；不证明 production threshold 或 causal root cause。 弱监督减少 turn labels，却可能把相关语句误作早期因果信号；风险低或误停代价高时应延后 alert 并保留完整执行。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05414:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05415:start -->
这是 TRAIN-DATA→AGENT-RAG 的 Direct Evolution：schema 从摄取产物变成贯穿构建与查询的可执行、带 provenance 控制面。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-FOUNDATIONS`; §4 只在作者数据与 query workload 上证明 ingestion/retrieval traceability；没有证明任意隐含语义可自动恢复或 schema extension 无冲突。 共享契约提高一致性，却增加 catalog governance、identity resolution 和 migration；同质单源可直接使用原生 schema/search。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05415:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05433:start -->
这是 PLATFORM-SECURITY/GOVERNANCE 的 Layering / Dependency：在既有发布审计与 provenance owner 上增加可验证计算记录；现有安全章节能够承载，无需 Structural Candidate。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-SECURITY`; Appendix B/G 给出 proof-cost估算与协议论证，而非 frontier-scale end-to-end deployment；没有证明硬件 telemetry 完整、spec 与真实训练语义完全一致。 零知识审计保护模型/数据机密，却增加 commitment、proof、trusted instrumentation 与 protocol complexity；低风险训练可继续使用日志和第三方 audit。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05433:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05495:start -->
这是 INFER-EXECUTION 的 Principle Reuse：continuous scheduling 的状态所有权下沉到 CUDA graph pipeline，但不能直接外推成 LLM runtime 结论。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `INFER-SCHEDULING`; §5 在 RTX3090/5090 两平台、六 workloads 和 workload-specific batch sweep 上报告 throughput/overhead；不证明 LLM serving、跨 GPU 或生产 tail SLO。 事件触发减少 host gap，却增加 buffer memory、event dependency 与 scheduler complexity；低并发、单 graph workload 仍可用同步 replay。 The family remains fully reviewed at score 3/3/3; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05495:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-05523:start -->
这是 TRAIN-RLHF/PLATFORM-SECURITY 的 Direct Evolution：red teaming 从发布前数据集变成闭环 attacker–defender control process。 Full-frontier decision: not selected because all 42 families were compared and this family is `Weekly Only — Context` at existing owner `TRAIN-RLHF`; §5/appendices 只在 Llama-3.1-8B-Instruct、指定 attacks/evaluators 上证明所测 robustness 变化；未证明对 frontier models、长期自博弈或未知攻击无 reward hacking。 在线生成 hard negatives提高适应性，却增加训练成本、评价器依赖和 catastrophic alignment drift；稳定威胁下 curated SFT 仍更可控。 The family remains fully reviewed at score 2/2/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-05523:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-06529:start -->
这是 PLATFORM-EVALUATION-SYSTEM/PLATFORM-SECURITY 的 Direct Evolution：control eval 从静态 attack frequency 升级为有状态 adversarial policy。 Full-frontier decision: not selected because all 42 families were compared and this family is `No Change — Existing Coverage` at existing owner `PLATFORM-EVALUATION-SYSTEM`; BashArena/LinuxArena 与1% audit budget 只证明所测 attacker/monitor 上 strategic selection显著降低 empirical safety；没有给出所有 agentic domains 的绝对安全率。 更强 adaptive red team提高压力真实性，却使复现实验、coverage 和归因更难；能力很弱或每步全审计时 fixed attack 仍可作基线。 The family remains fully reviewed at score 3/3/2; no review duty is dropped.
<!-- analysis-decision:SF-2026-ARXIV-2606-06529:end -->

## 6. Books Comparison

 and Decision

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
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
| SF-2026-ARXIV-2606-06529 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L74 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L297 | existing:SF-2026-ARXIV-2606-06529 | delta:SF-2026-ARXIV-2606-06529 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-06529 |

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
<!-- books-review:SF-2026-ARXIV-2606-06529:start -->
<!-- existing:SF-2026-ARXIV-2606-06529:start -->某些任务无法为每个请求即时获得 ground truth，因此不能简单把语义错误重新编码成另一个实时 `error_rate`。平台通常组合离线标注集、规则与 deterministic checks、抽样 human review、judge、用户反馈和延迟到达的业务 outcome，并为不同证据保留 provenance 与不确定性。高风险 policy failure 还应作为 hard gate，而不是被大量正常请求在平均值中抵消。<!-- existing:SF-2026-ARXIV-2606-06529:end -->

<!-- delta:SF-2026-ARXIV-2606-06529:start -->论文把策略拆成 start policy 与 stop policy，并在有限 human audit budget 下与 monitor 交互。episode state/monitor score 是数据，attacker policy 掌握是否发起/终止，blue protocol 决定审计和阻断。<!-- delta:SF-2026-ARXIV-2606-06529:end -->

Target `PLATFORM-EVALUATION-SYSTEM` at `books/part-06-ai-infrastructure/66-evaluation-system.md#L74`; adjacent refs: books/part-06-ai-infrastructure/65-kai-scheduler.md#L107; books/part-06-ai-infrastructure/67-monitoring.md#L297. Decision: `No Change — Existing Coverage`. No Books writeback required.
<!-- books-review:SF-2026-ARXIV-2606-06529:end -->

## 7. Semantic Audit

 and Gate

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260604-COVERAGE-V12 | fresh-context:root-denominator-acceptance-v12 | coverage | coverage:SRC-ARXIV:20260604 | — | DEN-20260604-V12-42 | passed |
| SA-20260604-EVIDENCE-V13 | fresh-context:jun04-full-fresh-gate | evidence | review:SF-2026-ARXIV-2606-04329; review:SF-2026-ARXIV-2606-04384; review:SF-2026-ARXIV-2606-04402; review:SF-2026-ARXIV-2606-04413; review:SF-2026-ARXIV-2606-04415; review:SF-2026-ARXIV-2606-04425; review:SF-2026-ARXIV-2606-04459; review:SF-2026-ARXIV-2606-04522; review:SF-2026-ARXIV-2606-04557; review:SF-2026-ARXIV-2606-04581; review:SF-2026-ARXIV-2606-04594; review:SF-2026-ARXIV-2606-04628; review:SF-2026-ARXIV-2606-04769; review:SF-2026-ARXIV-2606-04778; review:SF-2026-ARXIV-2606-04799; review:SF-2026-ARXIV-2606-04850; review:SF-2026-ARXIV-2606-04903; review:SF-2026-ARXIV-2606-04908; review:SF-2026-ARXIV-2606-04923; review:SF-2026-ARXIV-2606-04929; review:SF-2026-ARXIV-2606-05004; review:SF-2026-ARXIV-2606-05029; review:SF-2026-ARXIV-2606-05037; review:SF-2026-ARXIV-2606-05043; review:SF-2026-ARXIV-2606-05122; review:SF-2026-ARXIV-2606-05241; review:SF-2026-ARXIV-2606-05271; review:SF-2026-ARXIV-2606-05304; review:SF-2026-ARXIV-2606-05308; review:SF-2026-ARXIV-2606-05339; review:SF-2026-ARXIV-2606-05378; review:SF-2026-ARXIV-2606-05384; review:SF-2026-ARXIV-2606-05391; review:SF-2026-ARXIV-2606-05395; review:SF-2026-ARXIV-2606-05396; review:SF-2026-ARXIV-2606-05403; review:SF-2026-ARXIV-2606-05414; review:SF-2026-ARXIV-2606-05415; review:SF-2026-ARXIV-2606-05433; review:SF-2026-ARXIV-2606-05495; review:SF-2026-ARXIV-2606-05523; review:SF-2026-ARXIV-2606-06529 | — | repaired locator/disclosure findings; re-opened and checked 42/42 exact-v1 reviews and benchmark contracts | passed |
| SA-20260604-SELECTION-V13 | fresh-context:jun04-full-fresh-gate | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-04329; analysis-decision:SF-2026-ARXIV-2606-04384; analysis-decision:SF-2026-ARXIV-2606-04402; analysis-decision:SF-2026-ARXIV-2606-04413; analysis:DA-20260604-NPU-VIRTUALIZATION; analysis-decision:SF-2026-ARXIV-2606-04425; analysis-decision:SF-2026-ARXIV-2606-04459; analysis-decision:SF-2026-ARXIV-2606-04522; analysis-decision:SF-2026-ARXIV-2606-04557; analysis-decision:SF-2026-ARXIV-2606-04581; analysis-decision:SF-2026-ARXIV-2606-04594; analysis-decision:SF-2026-ARXIV-2606-04628; analysis-decision:SF-2026-ARXIV-2606-04769; analysis-decision:SF-2026-ARXIV-2606-04778; analysis-decision:SF-2026-ARXIV-2606-04799; analysis-decision:SF-2026-ARXIV-2606-04850; analysis-decision:SF-2026-ARXIV-2606-04903; analysis-decision:SF-2026-ARXIV-2606-04908; analysis-decision:SF-2026-ARXIV-2606-04923; analysis:DA-20260604-CROSS-STAGE-POISONING; analysis-decision:SF-2026-ARXIV-2606-05004; analysis-decision:SF-2026-ARXIV-2606-05029; analysis-decision:SF-2026-ARXIV-2606-05037; analysis-decision:SF-2026-ARXIV-2606-05043; analysis-decision:SF-2026-ARXIV-2606-05122; analysis-decision:SF-2026-ARXIV-2606-05241; analysis-decision:SF-2026-ARXIV-2606-05271; analysis:DA-20260604-ACTION-STATE-COMMUNICATION; analysis-decision:SF-2026-ARXIV-2606-05308; analysis-decision:SF-2026-ARXIV-2606-05339; analysis-decision:SF-2026-ARXIV-2606-05378; analysis-decision:SF-2026-ARXIV-2606-05384; analysis-decision:SF-2026-ARXIV-2606-05391; analysis-decision:SF-2026-ARXIV-2606-05395; analysis-decision:SF-2026-ARXIV-2606-05396; analysis-decision:SF-2026-ARXIV-2606-05403; analysis-decision:SF-2026-ARXIV-2606-05414; analysis-decision:SF-2026-ARXIV-2606-05415; analysis-decision:SF-2026-ARXIV-2606-05433; analysis-decision:SF-2026-ARXIV-2606-05495; analysis-decision:SF-2026-ARXIV-2606-05523; analysis-decision:SF-2026-ARXIV-2606-06529 | — | compared all 42 frontier rows; 3 non-overlapping selected lanes and 39 family-specific exclusions verified | passed |
| SA-20260604-BOOKS-V13 | fresh-context:jun04-full-fresh-gate | books | books-review:SF-2026-ARXIV-2606-04329; books-review:SF-2026-ARXIV-2606-04384; books-review:SF-2026-ARXIV-2606-04415; books-review:SF-2026-ARXIV-2606-04425; books-review:SF-2026-ARXIV-2606-04522; books-review:SF-2026-ARXIV-2606-04557; books-review:SF-2026-ARXIV-2606-04581; books-review:SF-2026-ARXIV-2606-04594; books-review:SF-2026-ARXIV-2606-04628; books-review:SF-2026-ARXIV-2606-04769; books-review:SF-2026-ARXIV-2606-04778; books-review:SF-2026-ARXIV-2606-04799; books-review:SF-2026-ARXIV-2606-04923; books-review:SF-2026-ARXIV-2606-04929; books-review:SF-2026-ARXIV-2606-05029; books-review:SF-2026-ARXIV-2606-05037; books-review:SF-2026-ARXIV-2606-05043; books-review:SF-2026-ARXIV-2606-05122; books-review:SF-2026-ARXIV-2606-05241; books-review:SF-2026-ARXIV-2606-05304; books-review:SF-2026-ARXIV-2606-05308; books-review:SF-2026-ARXIV-2606-05339; books-review:SF-2026-ARXIV-2606-05378; books-review:SF-2026-ARXIV-2606-05384; books-review:SF-2026-ARXIV-2606-05395; books-review:SF-2026-ARXIV-2606-05403; books-review:SF-2026-ARXIV-2606-05415; books-review:SF-2026-ARXIV-2606-05433; books-review:SF-2026-ARXIV-2606-05495; books-review:SF-2026-ARXIV-2606-06529; review:SF-2026-ARXIV-2606-04402; review:SF-2026-ARXIV-2606-04413; review:SF-2026-ARXIV-2606-04459; review:SF-2026-ARXIV-2606-04850; review:SF-2026-ARXIV-2606-04903; review:SF-2026-ARXIV-2606-04908; review:SF-2026-ARXIV-2606-05004; review:SF-2026-ARXIV-2606-05271; review:SF-2026-ARXIV-2606-05391; review:SF-2026-ARXIV-2606-05396; review:SF-2026-ARXIV-2606-05414; review:SF-2026-ARXIV-2606-05523 | — | 30 Books-eligible owner/adjacent/disposition comparisons verified; 12 Weekly Only families were verified through their candidate-level Source Review refs and intentionally have no Books Comparison; Ch72/Ch82 writebacks match exact-v1 boundaries and current adjacent owner semantics remain compatible | passed |

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

- Official exact-v1 manuscripts: `https://arxiv.org/html/<id>v1` or `https://arxiv.org/pdf/<id>v1`.
- Frozen denominator: `../_sources/daily-20260604/candidate-denominator-repair-proposal-v12.json`.
- Root denominator acceptance: `../_sources/daily-20260604/root-denominator-acceptance-v12.md`.
- Fresh downstream receipts: `../_sources/daily-20260604/source-review-receipts-v12-fresh.json`, `benchmark-contract-v12-fresh.json`, `deep-analysis-selection-v12-fresh.json`, `books-comparison-v12-fresh.json`.

- [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Revisiting Privacy Amplification by Subsampling in Selective Release DPSGD](https://arxiv.org/abs/2606.04384v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation](https://arxiv.org/abs/2606.04402v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [(Mis)generalization of Helpful-only Fine-tuning](https://arxiv.org/abs/2606.04413v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location](https://arxiv.org/abs/2606.04415v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection](https://arxiv.org/abs/2606.04425v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Token Rankings are Unforgeable Language Model Signatures](https://arxiv.org/abs/2606.04459v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [ANN Search: Recall What Matters](https://arxiv.org/abs/2606.04522v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Cartridges at Scale: Training Modular KV Caches over Large Document Collections](https://arxiv.org/abs/2606.04557v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge](https://arxiv.org/abs/2606.04581v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Ekka: Automated Diagnosis of Silent Errors in LLM Inference](https://arxiv.org/abs/2606.04594v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation](https://arxiv.org/abs/2606.04628v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications](https://arxiv.org/abs/2606.04769v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories](https://arxiv.org/abs/2606.04778v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [UModel: An Agent-Ready Observability Data Modeling Method at Scale](https://arxiv.org/abs/2606.04799v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Uncertainty-Aware End-to-End Co-Design of Neural Network Processors: From Training and Mapping to Fabrication](https://arxiv.org/abs/2606.04850v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Provably Auditable and Safe LLM Agents from Human-Authored Ontologies](https://arxiv.org/abs/2606.04903v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [GNStor: Design of GPU-Native High-Performance Remote All-Flash Array](https://arxiv.org/abs/2606.04908v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Sequential Data Poisoning in LLM Post-Training](https://arxiv.org/abs/2606.04929v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models](https://arxiv.org/abs/2606.05004v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Validity Threats for Foundation Model Research](https://arxiv.org/abs/2606.05029v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery](https://arxiv.org/abs/2606.05037v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols](https://arxiv.org/abs/2606.05043v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data](https://arxiv.org/abs/2606.05122v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation](https://arxiv.org/abs/2606.05241v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference](https://arxiv.org/abs/2606.05271v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference](https://arxiv.org/abs/2606.05308v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [A Taxonomy of Runtime Faults in Model Context Protocol Servers](https://arxiv.org/abs/2606.05339v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models](https://arxiv.org/abs/2606.05378v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges](https://arxiv.org/abs/2606.05384v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents](https://arxiv.org/abs/2606.05391v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents](https://arxiv.org/abs/2606.05395v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Willing but Unable: Separating Refusal from Capability in Code LLMs via Abliteration](https://arxiv.org/abs/2606.05396v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation](https://arxiv.org/abs/2606.05403v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories](https://arxiv.org/abs/2606.05414v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval](https://arxiv.org/abs/2606.05415v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Zero knowledge verification for frontier AI training is possible](https://arxiv.org/abs/2606.05433v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines](https://arxiv.org/abs/2606.05495v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [CHASE: Adversarial Red-Blue Teaming for Improving LLM Safety using Reinforcement Learning](https://arxiv.org/abs/2606.05523v1) — first-public（Asia/Shanghai）：2026-06-04；accessed：2026-08-29
- [Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety](https://arxiv.org/abs/2606.06529v1) — first-public（Asia/Shanghai）：2026-06-03；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。
