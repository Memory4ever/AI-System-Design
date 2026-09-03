# Daily Research — 2026-06-26

**Research Date:** 2026-06-26

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-25 09:00:00 ～ 2026-06-26 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
Beijing window [2026-06-25 09:00, 2026-06-26 09:00) contains 470 registered identities. Full 470/470 title+abstract review freezes 84 durable families and 386 family-specific closures (17.87%). Exact-v1 Evidence is complete for 84/84 identities (83 official HTML plus one official v1 PDF fallback); Selection compares all 84 and chooses three narrative units. Fresh owner+adjacent review recalibrates the Books disposition from 59 Integrate / 25 No Change / 0 Weekly Only to 7 Integrate / 33 No Change / 44 Weekly Only; seven deltas merge into six owner narratives. Root wrote seven Integrate Review notes and six owner-merged narratives; the 84/84 post-write fresh audit passed with zero unresolved findings. This date is Complete.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-26 |
| Window End | 2026-06-26 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Beijing Window | [2026-06-25 09:00, 2026-06-26 09:00) |
| Denominator ID | daily-v2.1:2026-06-26:48b4ead4054910a5 |
| Denominator Frozen At | 2026-08-29T18:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-25T09:00:00+08:00 | 2026-06-26T09:00:00+08:00 | 2026-08-29T18:00:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 566 | SF-2026-ARXIV-2606-26156;SF-2026-ARXIV-2606-26185;SF-2026-ARXIV-2606-26211;SF-2026-ARXIV-2606-26257;SF-2026-ARXIV-2606-26298;SF-2026-ARXIV-2606-26300;SF-2026-ARXIV-2606-26341;SF-2026-ARXIV-2606-26344;SF-2026-ARXIV-2606-26356;SF-2026-ARXIV-2606-26377;SF-2026-ARXIV-2606-26383;SF-2026-ARXIV-2606-26429;SF-2026-ARXIV-2606-26439;SF-2026-ARXIV-2606-26441;SF-2026-ARXIV-2606-26442;SF-2026-ARXIV-2606-26449;SF-2026-ARXIV-2606-26453;SF-2026-ARXIV-2606-26456;SF-2026-ARXIV-2606-26463;SF-2026-ARXIV-2606-26472;SF-2026-ARXIV-2606-26479;SF-2026-ARXIV-2606-26488;SF-2026-ARXIV-2606-26492;SF-2026-ARXIV-2606-26511;SF-2026-ARXIV-2606-26524;SF-2026-ARXIV-2606-26529;SF-2026-ARXIV-2606-26587;SF-2026-ARXIV-2606-26590;SF-2026-ARXIV-2606-26607;SF-2026-ARXIV-2606-26631;SF-2026-ARXIV-2606-26633;SF-2026-ARXIV-2606-26649;SF-2026-ARXIV-2606-26664;SF-2026-ARXIV-2606-26666;SF-2026-ARXIV-2606-26669;SF-2026-ARXIV-2606-26686;SF-2026-ARXIV-2606-26721;SF-2026-ARXIV-2606-26744;SF-2026-ARXIV-2606-26753;SF-2026-ARXIV-2606-26758;SF-2026-ARXIV-2606-26762;SF-2026-ARXIV-2606-26790;SF-2026-ARXIV-2606-26793;SF-2026-ARXIV-2606-26806;SF-2026-ARXIV-2606-26836;SF-2026-ARXIV-2606-26859;SF-2026-ARXIV-2606-26875;SF-2026-ARXIV-2606-26904;SF-2026-ARXIV-2606-26917;SF-2026-ARXIV-2606-26918;SF-2026-ARXIV-2606-26924;SF-2026-ARXIV-2606-26933;SF-2026-ARXIV-2606-26935;SF-2026-ARXIV-2606-26960;SF-2026-ARXIV-2606-26978;SF-2026-ARXIV-2606-26979;SF-2026-ARXIV-2606-26990;SF-2026-ARXIV-2606-26997;SF-2026-ARXIV-2606-27005;SF-2026-ARXIV-2606-27009;SF-2026-ARXIV-2606-27027;SF-2026-ARXIV-2606-27045;SF-2026-ARXIV-2606-27079;SF-2026-ARXIV-2606-27091;SF-2026-ARXIV-2606-27136;SF-2026-ARXIV-2606-27146;SF-2026-ARXIV-2606-27153;SF-2026-ARXIV-2606-27154;SF-2026-ARXIV-2606-27188;SF-2026-ARXIV-2606-27205;SF-2026-ARXIV-2606-27210;SF-2026-ARXIV-2606-27226;SF-2026-ARXIV-2606-27242;SF-2026-ARXIV-2606-27243;SF-2026-ARXIV-2606-27251;SF-2026-ARXIV-2606-27268;SF-2026-ARXIV-2606-27288;SF-2026-ARXIV-2606-27326;SF-2026-ARXIV-2606-27330;SF-2026-ARXIV-2606-27350;SF-2026-ARXIV-2606-27355;SF-2026-ARXIV-2606-27359;SF-2026-ARXIV-2606-27369;SF-2026-ARXIV-2606-27374;SF-2026-ARXIV-2606-27375 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260626/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260626; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260626 |
<!-- coverage:SRC-ARXIV:20260626:start -->
Full 470/470 title+abstract audit: 303 Core, 60 keyword-routed and 107 route-negative; arithmetic 470 = 84 retained + 386 closures; retain rate 17.87%. Keyword routing supplied recall only. Route-negative retained=2; proposed-pool false positives closed=5.
<!-- coverage:SRC-ARXIV:20260626:end -->


<!-- latest-contract-reopen:2026-06-26:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-26:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **566** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **85** 条是旧报告 retained provenance，**481** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-26156 | arXiv:2606.26156v1 | paper-v1:2606.26156 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26156 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-26156 | yes |
| SF-2026-ARXIV-2606-26185 | arXiv:2606.26185v1 | paper-v1:2606.26185 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26185 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26185 | yes |
| SF-2026-ARXIV-2606-26211 | arXiv:2606.26211v1 | paper-v1:2606.26211 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26211 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2606-26211 | yes |
| SF-2026-ARXIV-2606-26257 | arXiv:2606.26257v1 | paper-v1:2606.26257 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26257 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26257 | yes |
| SF-2026-ARXIV-2606-26298 | arXiv:2606.26298v1 | paper-v1:2606.26298 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26298 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26298 | yes |
| SF-2026-ARXIV-2606-26300 | arXiv:2606.26300v1 | paper-v1:2606.26300 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26300 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26300 | yes |
| SF-2026-ARXIV-2606-26341 | arXiv:2606.26341v1 | paper-v1:2606.26341 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26341 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2606-26341 | yes |
| SF-2026-ARXIV-2606-26344 | arXiv:2606.26344v1 | paper-v1:2606.26344 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26344 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-26344 | yes |
| SF-2026-ARXIV-2606-26356 | arXiv:2606.26356v1 | paper-v1:2606.26356 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26356 | self | — | new_in_window | AGENT-PROMPT | Integrate | books-review:SF-2026-ARXIV-2606-26356 | yes |
| SF-2026-ARXIV-2606-26377 | arXiv:2606.26377v1 | paper-v1:2606.26377 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26377 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26377 | yes |
| SF-2026-ARXIV-2606-26383 | arXiv:2606.26383v1 | paper-v1:2606.26383 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26383 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-26383 | yes |
| SF-2026-ARXIV-2606-26429 | arXiv:2606.26429v1 | paper-v1:2606.26429 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26429 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26429 | yes |
| SF-2026-ARXIV-2606-26439 | arXiv:2606.26439v1 | paper-v1:2606.26439 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26439 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-26439 | yes |
| SF-2026-ARXIV-2606-26441 | arXiv:2606.26441v1 | paper-v1:2606.26441 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26441 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-26441 | yes |
| SF-2026-ARXIV-2606-26442 | arXiv:2606.26442v1 | paper-v1:2606.26442 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26442 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-26442 | yes |
| SF-2026-ARXIV-2606-26449 | arXiv:2606.26449v1 | paper-v1:2606.26449 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26449 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2606-26449 | yes |
| SF-2026-ARXIV-2606-26453 | arXiv:2606.26453v1 | paper-v1:2606.26453 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26453 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-26453 | yes |
| SF-2026-ARXIV-2606-26456 | arXiv:2606.26456v1 | paper-v1:2606.26456 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26456 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26456 | yes |
| SF-2026-ARXIV-2606-26463 | arXiv:2606.26463v1 | paper-v1:2606.26463 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26463 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-26463 | yes |
| SF-2026-ARXIV-2606-26472 | arXiv:2606.26472v1 | paper-v1:2606.26472 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26472 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-26472 | yes |
| SF-2026-ARXIV-2606-26479 | arXiv:2606.26479v1 | paper-v1:2606.26479 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26479 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26479 | yes |
| SF-2026-ARXIV-2606-26488 | arXiv:2606.26488v1 | paper-v1:2606.26488 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26488 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-26488 | yes |
| SF-2026-ARXIV-2606-26492 | arXiv:2606.26492v1 | paper-v1:2606.26492 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26492 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26492 | yes |
| SF-2026-ARXIV-2606-26511 | arXiv:2606.26511v1 | paper-v1:2606.26511 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26511 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26511 | yes |
| SF-2026-ARXIV-2606-26524 | arXiv:2606.26524v1 | paper-v1:2606.26524 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26524 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26524 | yes |
| SF-2026-ARXIV-2606-26529 | arXiv:2606.26529v1 | paper-v1:2606.26529 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26529 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26587 | arXiv:2606.26587v1 | paper-v1:2606.26587 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26587 | self | — | new_in_window | INFER-GPU-MEMORY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26590 | arXiv:2606.26590v1 | paper-v1:2606.26590 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26590 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26590 | yes |
| SF-2026-ARXIV-2606-26607 | arXiv:2606.26607v1 | paper-v1:2606.26607 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26607 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-26607 | yes |
| SF-2026-ARXIV-2606-26631 | arXiv:2606.26631v1 | paper-v1:2606.26631 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26631 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26631 | yes |
| SF-2026-ARXIV-2606-26633 | arXiv:2606.26633v1 | paper-v1:2606.26633 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26633 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26649 | arXiv:2606.26649v1 | paper-v1:2606.26649 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26649 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26649 | yes |
| SF-2026-ARXIV-2606-26664 | arXiv:2606.26664v1 | paper-v1:2606.26664 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26664 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26666 | arXiv:2606.26666v1 | paper-v1:2606.26666 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26666 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26669 | arXiv:2606.26669v1 | paper-v1:2606.26669 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26669 | self | — | new_in_window | AGENT-TOOL-CALLING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26686 | arXiv:2606.26686v1 | paper-v1:2606.26686 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26686 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26721 | arXiv:2606.26721v1 | paper-v1:2606.26721 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26721 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26721 | yes |
| SF-2026-ARXIV-2606-26744 | arXiv:2606.26744v1 | paper-v1:2606.26744 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26744 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26753 | arXiv:2606.26753v1 | paper-v1:2606.26753 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26753 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26753 | yes |
| SF-2026-ARXIV-2606-26758 | arXiv:2606.26758v1 | paper-v1:2606.26758 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26758 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26762 | arXiv:2606.26762v1 | paper-v1:2606.26762 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26762 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26790 | arXiv:2606.26790v1 | paper-v1:2606.26790 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26790 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26793 | arXiv:2606.26793v1 | paper-v1:2606.26793 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26793 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26793 | yes |
| SF-2026-ARXIV-2606-26806 | arXiv:2606.26806v1 | paper-v1:2606.26806 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26806 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26806 | yes |
| SF-2026-ARXIV-2606-26836 | arXiv:2606.26836v1 | paper-v1:2606.26836 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26836 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26836 | yes |
| SF-2026-ARXIV-2606-26859 | arXiv:2606.26859v1 | paper-v1:2606.26859 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26859 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26875 | arXiv:2606.26875v1 | paper-v1:2606.26875 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26875 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26875 | yes |
| SF-2026-ARXIV-2606-26904 | arXiv:2606.26904v1 | paper-v1:2606.26904 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26904 | self | — | new_in_window | AGENT-TOOL-CALLING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26917 | arXiv:2606.26917v1 | paper-v1:2606.26917 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26917 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26918 | arXiv:2606.26918v1 | paper-v1:2606.26918 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26918 | self | — | new_in_window | AGENT-PLANNING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26924 | arXiv:2606.26924v1 | paper-v1:2606.26924 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26924 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26924 | yes |
| SF-2026-ARXIV-2606-26933 | arXiv:2606.26933v1 | paper-v1:2606.26933 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26933 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26935 | arXiv:2606.26935v1 | paper-v1:2606.26935 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26935 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26935 | yes |
| SF-2026-ARXIV-2606-26960 | arXiv:2606.26960v1 | paper-v1:2606.26960 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26960 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26978 | arXiv:2606.26978v1 | paper-v1:2606.26978 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26978 | self | — | new_in_window | AGENT-TOOL-CALLING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-26979 | arXiv:2606.26979v1 | paper-v1:2606.26979 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26979 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26979 | yes |
| SF-2026-ARXIV-2606-26990 | arXiv:2606.26990v1 | paper-v1:2606.26990 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26990 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26990 | yes |
| SF-2026-ARXIV-2606-26997 | arXiv:2606.26997v1 | paper-v1:2606.26997 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26997 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26997 | yes |
| SF-2026-ARXIV-2606-27005 | arXiv:2606.27005v1 | paper-v1:2606.27005 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27005 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27009 | arXiv:2606.27009v1 | paper-v1:2606.27009 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27009 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27009 | yes |
| SF-2026-ARXIV-2606-27027 | arXiv:2606.27027v1 | paper-v1:2606.27027 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27027 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2606-27027 | yes |
| SF-2026-ARXIV-2606-27045 | arXiv:2606.27045v1 | paper-v1:2606.27045 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27045 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27045 | yes |
| SF-2026-ARXIV-2606-27079 | arXiv:2606.27079v1 | paper-v1:2606.27079 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27079 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27079 | yes |
| SF-2026-ARXIV-2606-27091 | arXiv:2606.27091v1 | paper-v1:2606.27091 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27091 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27091 | yes |
| SF-2026-ARXIV-2606-27136 | arXiv:2606.27136v1 | paper-v1:2606.27136 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27136 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27146 | arXiv:2606.27146v1 | paper-v1:2606.27146 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27146 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27146 | yes |
| SF-2026-ARXIV-2606-27153 | arXiv:2606.27153v1 | paper-v1:2606.27153 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27153 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-27153 | yes |
| SF-2026-ARXIV-2606-27154 | arXiv:2606.27154v1 | paper-v1:2606.27154 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27154 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27154 | yes |
| SF-2026-ARXIV-2606-27188 | arXiv:2606.27188v1 | paper-v1:2606.27188 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27188 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27188 | yes |
| SF-2026-ARXIV-2606-27205 | arXiv:2606.27205v1 | paper-v1:2606.27205 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27205 | self | — | new_in_window | INFER-GPU-MEMORY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27210 | arXiv:2606.27210v1 | paper-v1:2606.27210 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27210 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27226 | arXiv:2606.27226v1 | paper-v1:2606.27226 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27226 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27226 | yes |
| SF-2026-ARXIV-2606-27242 | arXiv:2606.27242v1 | paper-v1:2606.27242 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27242 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27243 | arXiv:2606.27243v1 | paper-v1:2606.27243 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27243 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27251 | arXiv:2606.27251v1 | paper-v1:2606.27251 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27251 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27251 | yes |
| SF-2026-ARXIV-2606-27268 | arXiv:2606.27268v1 | paper-v1:2606.27268 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27268 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27288 | arXiv:2606.27288v1 | paper-v1:2606.27288 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27288 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27288 | yes |
| SF-2026-ARXIV-2606-27326 | arXiv:2606.27326v1 | paper-v1:2606.27326 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27326 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27326 | yes |
| SF-2026-ARXIV-2606-27330 | arXiv:2606.27330v1 | paper-v1:2606.27330 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27330 | self | — | new_in_window | AGENT-PLANNING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27350 | arXiv:2606.27350v1 | paper-v1:2606.27350 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27350 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27355 | arXiv:2606.27355v1 | paper-v1:2606.27355 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27355 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-27355 | yes |
| SF-2026-ARXIV-2606-27359 | arXiv:2606.27359v1 | paper-v1:2606.27359 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27359 | self | — | new_in_window | INFER-DECODE | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27369 | arXiv:2606.27369v1 | paper-v1:2606.27369 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27369 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27374 | arXiv:2606.27374v1 | paper-v1:2606.27374 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27374 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27375 | arXiv:2606.27375v1 | paper-v1:2606.27375 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27375 | self | — | new_in_window | TRAIN-DATA | Weekly Only — Context | — | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-26156 | RP-79711148a8f47744 | deep | arXiv:2606.26156v1 | SRC-ARXIV@arXiv:2606.26156v1 | https://arxiv.org/html/2606.26156v1 — §2 Information Protocols; 3 Kiko Programming Model | https://arxiv.org/html/2606.26156v1 — §4 Operational Semantics; protocol-compliance proof | https://arxiv.org/html/2606.26156v1 — §5 Discussion and conference-era implementation scope | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26156 | complete |
| SF-2026-ARXIV-2606-26185 | RP-3c8114a102a5f867 | deep | arXiv:2606.26185v1 | SRC-ARXIV@arXiv:2606.26185v1 | https://arxiv.org/html/2606.26185v1 — §Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation | https://arxiv.org/html/2606.26185v1 — §Cross-temperature, repeat-run and judge-agreement evaluation | https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26185 | complete |
| SF-2026-ARXIV-2606-26211 | RP-80cfa89873050b29 | deep | arXiv:2606.26211v1 | SRC-ARXIV@arXiv:2606.26211v1 | https://arxiv.org/html/2606.26211v1 — §Data Facts metadata schema; provenance, semantics, constraints and exchange contract | https://arxiv.org/html/2606.26211v1 — §NANDini multi-agent exchange examples and schema coverage | https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26211 | complete |
| SF-2026-ARXIV-2606-26257 | RP-a840d100b5b37ba1 | deep | arXiv:2606.26257v1 | SRC-ARXIV@arXiv:2606.26257v1 | https://arxiv.org/html/2606.26257v1 — §Dataset Usage Inference formulation without shadow models or held-out data | https://arxiv.org/html/2606.26257v1 — §Exact-v1 membership/dataset inference experiments and ablations | https://arxiv.org/html/2606.26257v1 — §Requires the paper's observable score/query regime; not per-record legal attribution | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26257 | complete |
| SF-2026-ARXIV-2606-26298 | RP-e90143e57ba29e80 | deep | arXiv:2606.26298v1 | SRC-ARXIV@arXiv:2606.26298v1 | https://arxiv.org/html/2606.26298v1 — §Governing Actions, Not Agents; Institutional Attestation model | https://arxiv.org/html/2606.26298v1 — §Action-level attestation scenarios and governance analysis | https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26298 | complete |
| SF-2026-ARXIV-2606-26300 | RP-a3d4d472369add93 | deep | arXiv:2606.26300v1 | SRC-ARXIV@arXiv:2606.26300v1 | https://arxiv.org/html/2606.26300v1 — §Verification Horizon formulation for coding-agent rewards | https://arxiv.org/html/2606.26300v1 — §Reward-verification experiments across coding horizons | https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26300 | complete |
| SF-2026-ARXIV-2606-26341 | RP-62a53e0dfb8b0cbd | deep | arXiv:2606.26341v1 | SRC-ARXIV@arXiv:2606.26341v1 | https://arxiv.org/html/2606.26341v1 — §Many Problems One GPU batching and nonlinear-optimization execution design | https://arxiv.org/html/2606.26341v1 — §GPU scaling experiments across problem families | https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26341 | complete |
| SF-2026-ARXIV-2606-26344 | RP-d3775e238667e27e | deep | arXiv:2606.26344v1 | SRC-ARXIV@arXiv:2606.26344v1 | https://arxiv.org/html/2606.26344v1 — §Axon synthesizing superoptimizer; tensor-program search and verification | https://arxiv.org/html/2606.26344v1 — §Kernel synthesis evaluation and generated-program performance | https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26344 | complete |
| SF-2026-ARXIV-2606-26356 | RP-1701767ba01a558b | deep | arXiv:2606.26356v1 | SRC-ARXIV@arXiv:2606.26356v1 | https://arxiv.org/html/2606.26356v1 — §Instruction Bleed formulation; prompt-composed module interference | https://arxiv.org/html/2606.26356v1 — §Cross-module interference experiments and mitigations | https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26356 | complete |
| SF-2026-ARXIV-2606-26377 | RP-4eab22709fa045af | deep | arXiv:2606.26377v1 | SRC-ARXIV@arXiv:2606.26377v1 | https://arxiv.org/html/2606.26377v1 — §Unified intent-and-harm verification defense | https://arxiv.org/html/2606.26377v1 — §Threat-generation and defense evaluation | https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26377 | complete |
| SF-2026-ARXIV-2606-26383 | RP-ac135c6a5d88e8a6 | deep | arXiv:2606.26383v1 | SRC-ARXIV@arXiv:2606.26383v1 | https://arxiv.org/html/2606.26383v1 — §SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation | https://arxiv.org/html/2606.26383v1 — §Predicted-vs-observed latency and throughput analysis | https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26383 | complete |
| SF-2026-ARXIV-2606-26429 | RP-474420728a35e81f | deep | arXiv:2606.26429v1 | SRC-ARXIV@arXiv:2606.26429v1 | https://arxiv.org/html/2606.26429v1 — §DualEval joint model-item calibration | https://arxiv.org/html/2606.26429v1 — §Unified LLM evaluation experiments and calibration analysis | https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26429 | complete |
| SF-2026-ARXIV-2606-26439 | RP-719f8cf401637f6c | deep | arXiv:2606.26439v1 | SRC-ARXIV@arXiv:2606.26439v1 | https://arxiv.org/html/2606.26439v1 — §TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization | https://arxiv.org/html/2606.26439v1 — §GPU retrieval throughput, latency and quality evaluation | https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26439 | complete |
| SF-2026-ARXIV-2606-26441 | RP-f85ba64bfb48adc3 | deep | arXiv:2606.26441v1 | SRC-ARXIV@arXiv:2606.26441v1 | https://arxiv.org/html/2606.26441v1 — §GPUSparse learned sparse retrieval with parallel inverted indices | https://arxiv.org/html/2606.26441v1 — §Retrieval quality, latency and GPU scaling experiments | https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26441 | complete |
| SF-2026-ARXIV-2606-26442 | RP-f88d7df11eb06aa1 | deep | arXiv:2606.26442v1 | SRC-ARXIV@arXiv:2606.26442v1 | https://arxiv.org/html/2606.26442v1 — §AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling | https://arxiv.org/html/2606.26442v1 — §Utility execution, throughput and theorem-proving workflow evaluation | https://arxiv.org/html/2606.26442v1 — §Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26442 | complete |
| SF-2026-ARXIV-2606-26449 | RP-d72cae0c540f10e8 | deep | arXiv:2606.26449v1 | SRC-ARXIV@arXiv:2606.26449v1 | https://arxiv.org/html/2606.26449v1 — §ProvenAI provenance-native trace schema and evidence links | https://arxiv.org/html/2606.26449v1 — §Generated-answer trace/evidence evaluation | https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26449 | complete |
| SF-2026-ARXIV-2606-26453 | RP-12bb1a00d99b8459 | deep | arXiv:2606.26453v1 | SRC-ARXIV@arXiv:2606.26453v1 | https://arxiv.org/html/2606.26453v1 — §Micro-profiling tools as expert surrogates for LLM CUDA optimization | https://arxiv.org/html/2606.26453v1 — §Generated-kernel correctness, profiling and speed evaluation | https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26453 | complete |
| SF-2026-ARXIV-2606-26456 | RP-8eee1c405b6c239d | deep | arXiv:2606.26456v1 | SRC-ARXIV@arXiv:2606.26456v1 | https://arxiv.org/html/2606.26456v1 — §Safety-Aware Mutation Testing proposal and interaction-aware mutant model | https://arxiv.org/html/2606.26456v1 — §Simulation-based ADS testing protocol and proposed adequacy criterion | https://arxiv.org/html/2606.26456v1 — §Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26456 | complete |
| SF-2026-ARXIV-2606-26463 | RP-8c1db9b261f0cdfb | deep | arXiv:2606.26463v1 | SRC-ARXIV@arXiv:2606.26463v1 | https://arxiv.org/html/2606.26463v1 — §Variable-delay real-time RL; lightweight gate selects state-dependent planning budget | https://arxiv.org/html/2606.26463v1 — §Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation | https://arxiv.org/html/2606.26463v1 — §Game planners and timing model do not prove benefit under production tool latency or safety deadlines | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26463 | complete |
| SF-2026-ARXIV-2606-26472 | RP-e3d9f91fb4679a39 | deep | arXiv:2606.26472v1 | SRC-ARXIV@arXiv:2606.26472v1 | https://arxiv.org/html/2606.26472v1 — §Epiphany score from forward-pass representation change; attention-matrix-free eviction | https://arxiv.org/html/2606.26472v1 — §Long-reasoning cache/quality evaluation and 16x feasible-context claim | https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26472 | complete |
| SF-2026-ARXIV-2606-26479 | RP-78e667e5a31d3387 | deep | arXiv:2606.26479v1 | SRC-ARXIV@arXiv:2606.26479v1 | https://arxiv.org/html/2606.26479v1 — §Out-of-band prompt-injection defenses organized as reference monitors and integrity policies | https://arxiv.org/html/2606.26479v1 — §Adaptive evaluation methodology against policy-aware attackers | https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26479 | complete |
| SF-2026-ARXIV-2606-26488 | RP-d7749d159f45fab3 | deep | arXiv:2606.26488v1 | SRC-ARXIV@arXiv:2606.26488v1 | https://arxiv.org/html/2606.26488v1 — §Compression of recursive reasoners across precision, pruning, distillation and attention variants | https://arxiv.org/html/2606.26488v1 — §Three tasks and two recursive architectures; local vs puzzle-exact accuracy | https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26488 | complete |
| SF-2026-ARXIV-2606-26492 | RP-1b91478a3f182589 | deep | arXiv:2606.26492v1 | SRC-ARXIV@arXiv:2606.26492v1 | https://arxiv.org/html/2606.26492v1 — §Within-program versus leave-program-out diagnostic design | https://arxiv.org/html/2606.26492v1 — §DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis | https://arxiv.org/html/2606.26492v1 — §Fault-injected programs and studied diagnosers do not prove production root-cause validity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26492 | complete |
| SF-2026-ARXIV-2606-26511 | RP-5c377b4e1fb5fa04 | deep | arXiv:2606.26511v1 | SRC-ARXIV@arXiv:2606.26511v1 | arXiv:2606.26511v1 — §4 The MemStrata Architecture; §4.3 The “retain, then supersede” design | arXiv:2606.26511v1 — §4.5 Marker-free benchmark construction; §5 Experiments; §5.3 Stale-fact error: the structural result | arXiv:2606.26511v1 — §6 Discussion; §7 Limitations; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26511 | complete |
| SF-2026-ARXIV-2606-26524 | RP-f614fd88c4757064 | deep | arXiv:2606.26524v1 | SRC-ARXIV@arXiv:2606.26524v1 | arXiv:2606.26524v1 — §IV The Vigil Framework; §IV-A Algorithm Overview | arXiv:2606.26524v1 — §VII Evaluation; §VII-A Experimental Setup | arXiv:2606.26524v1 — §III-C Threat Model; §IX Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26524 | complete |
| SF-2026-ARXIV-2606-26529 | RP-e9ce88d15bb73e67 | deep | arXiv:2606.26529v1 | SRC-ARXIV@arXiv:2606.26529v1 | arXiv:2606.26529v1 — §A System-1-style task capture without reliable intrinsic oversight | arXiv:2606.26529v1 — §Results; §Experimental Procedures | arXiv:2606.26529v1 — §Discussion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26529 | complete |
| SF-2026-ARXIV-2606-26587 | RP-7f42ab8af9ffd8a0 | deep | arXiv:2606.26587v1 | SRC-ARXIV@arXiv:2606.26587v1 | arXiv:2606.26587v1 — §3 Methodology; §3.4 Kernel design; §A.1.1 Design rationale | arXiv:2606.26587v1 — §3.5 Theoretical analysis; §4 Experiments; §4.1 Experimental setup | arXiv:2606.26587v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26587 | complete |
| SF-2026-ARXIV-2606-26590 | RP-5b6fe1ba81b65940 | deep | arXiv:2606.26590v1 | SRC-ARXIV@arXiv:2606.26590v1 | arXiv:2606.26590v1 — §TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform Security Repair; §2.5 Evaluation Frameworks in Empirical Software Engineering; §3 Study Design and Evaluation Protocol | arXiv:2606.26590v1 — §2.5 Evaluation Frameworks in Empirical Software Engineering; §3 Study Design and Evaluation Protocol; §3.9 Statistical Analysis Methods | arXiv:2606.26590v1 — §3.11 Threat Model; §7 Discussion; §8 Threats to Validity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26590 | complete |
| SF-2026-ARXIV-2606-26607 | RP-5e7c91b30af298ac | deep | arXiv:2606.26607v1 | SRC-ARXIV@arXiv:2606.26607v1 | arXiv:2606.26607v1 — §4 System Design; §Appendix B End-to-End Training Projection | arXiv:2606.26607v1 — §6 Evaluation; §6.1 Experimental Setup | arXiv:2606.26607v1 — §2.2 Real World Workloads Cross the Boundary; §8 Discussion; §9 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26607 | complete |
| SF-2026-ARXIV-2606-26631 | RP-5136e5628351c639 | deep | arXiv:2606.26631v1 | SRC-ARXIV@arXiv:2606.26631v1 | arXiv:2606.26631v1 — §3 Method | arXiv:2606.26631v1 — §4 Experiment; §4.1 Experimental Settings; §Test Benchmarks. | arXiv:2606.26631v1 — §6 Conclusion; §7 Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26631 | complete |
| SF-2026-ARXIV-2606-26633 | RP-3167cec0ba1f93a1 | deep | arXiv:2606.26633v1 | SRC-ARXIV@arXiv:2606.26633v1 | arXiv:2606.26633v1 — §Simulating Unified Tensor Resharding in heterogeneous AI systems; §2.1. Emergent Challenges with Heterogeneity in AI Training Clusters; §2.2. Heterogeneity-aware AI Training Deployment: An Example | arXiv:2606.26633v1 — §5. Evaluation; §Appendix D Additional Evaluation Results | arXiv:2606.26633v1 — §7. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26633 | complete |
| SF-2026-ARXIV-2606-26649 | RP-45afd107eef1d024 | deep | arXiv:2606.26649v1 | SRC-ARXIV@arXiv:2606.26649v1 | arXiv:2606.26649v1 — §2 Approach | arXiv:2606.26649v1 — §3 Evaluation | arXiv:2606.26649v1 — §4 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26649 | complete |
| SF-2026-ARXIV-2606-26664 | RP-d9b645e2d311ea43 | deep | arXiv:2606.26664v1 | SRC-ARXIV@arXiv:2606.26664v1 | arXiv:2606.26664v1 — §TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems; §III System Model and Problem; §IV Proposed Method | arXiv:2606.26664v1 — §V Experimental Evaluation; §V-A Experimental Setup | arXiv:2606.26664v1 — §VI Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26664 | complete |
| SF-2026-ARXIV-2606-26666 | RP-d18b1ab626f2d38d | deep | arXiv:2606.26666v1 | SRC-ARXIV@arXiv:2606.26666v1 | arXiv:2606.26666v1 — §3 Methodology | arXiv:2606.26666v1 — §4 Experiments; §4.1 Experimental Setup; §4.3 Main Serving Results | arXiv:2606.26666v1 — §5 Discussion; §5.1 Threats to Validity; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26666 | complete |
| SF-2026-ARXIV-2606-26669 | RP-c10ed56f00a97ac2 | deep | arXiv:2606.26669v1 | SRC-ARXIV@arXiv:2606.26669v1 | arXiv:2606.26669v1 — §3 The Skill-DisCo Framework; §3.1 Framework Overview | arXiv:2606.26669v1 — §4 Experiments; §4.1 Experimental Setup; §Appendix A Full Results: Token Usage and Inference Cost | arXiv:2606.26669v1 — §6 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26669 | complete |
| SF-2026-ARXIV-2606-26686 | RP-88d0b76b92ae6162 | deep | arXiv:2606.26686v1 | SRC-ARXIV@arXiv:2606.26686v1 | arXiv:2606.26686v1 — §Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation | arXiv:2606.26686v1 — §4 Experimental Setup | arXiv:2606.26686v1 — §7 Discussion and Limitations; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26686 | complete |
| SF-2026-ARXIV-2606-26721 | RP-4236a3f85c6b9bad | deep | arXiv:2606.26721v1 | SRC-ARXIV@arXiv:2606.26721v1 | arXiv:2606.26721v1 — §6. Prototype Architecture: A Collaboration Gateway | arXiv:2606.26721v1 — §8. Evaluation Agenda | arXiv:2606.26721v1 — §3.3. The Trust Boundary; §9. Risks and Limitations; §10. Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26721 | complete |
| SF-2026-ARXIV-2606-26744 | RP-bd3a0b38e90c349a | deep | arXiv:2606.26744v1 | SRC-ARXIV@arXiv:2606.26744v1 | arXiv:2606.26744v1 — §2 Method | arXiv:2606.26744v1 — §3 Experiments; §3.2 Benchmarks; §3.5 Main Results | arXiv:2606.26744v1 — §5 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26744 | complete |
| SF-2026-ARXIV-2606-26753 | RP-9b83146138986120 | deep | arXiv:2606.26753v1 | SRC-ARXIV@arXiv:2606.26753v1 | arXiv:2606.26753v1 — §Agent memory systems.; §5.5 Architecture freeze: head merge and the load-bearing spine; §6 Training the Verifier | arXiv:2606.26753v1 — §The temporal-window negative result.; §7 Experimental Protocol | arXiv:2606.26753v1 — §15 Boundary Findings; §17 Discussion; §17.1 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26753 | complete |
| SF-2026-ARXIV-2606-26758 | RP-2ed351d11f29678a | deep | arXiv:2606.26758v1 | SRC-ARXIV@arXiv:2606.26758v1 | arXiv:2606.26758v1 — §EGG: An Expert-Guided Agent Framework for Kernel Generation; §3 Method; §3.2.1 Algorithmic Structure Design | arXiv:2606.26758v1 — §4 Experiments; §4.1 Experimental Setup; §Appendix A Additional Hardware and LLM Results | arXiv:2606.26758v1 — §5 Conclusion; §Appendix G Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26758 | complete |
| SF-2026-ARXIV-2606-26762 | RP-528b8847a8d30e36 | deep | arXiv:2606.26762v1 | SRC-ARXIV@arXiv:2606.26762v1 | arXiv:2606.26762v1 — §2.2 Bounded-Memory SVU and Prior Approaches; §4.7 System Validation; §Appendix A ProtoKV Method Details | arXiv:2606.26762v1 — §2 Background and Problem Setup; §4 Experiments; §4.1 Experimental Setup | arXiv:2606.26762v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26762 | complete |
| SF-2026-ARXIV-2606-26790 | RP-68a1f77ed21aba64 | deep | arXiv:2606.26790v1 | SRC-ARXIV@arXiv:2606.26790v1 | arXiv:2606.26790v1 — §3 Methods; §Training-inference boundary.; §OPID remains competitive with strong hybrid methods. | arXiv:2606.26790v1 — §4 Experiment; §4.1 Experimental Setting; §Benchmarks. | arXiv:2606.26790v1 — §Training-inference boundary.; §5 Conclusion; §Appendix E Additional Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26790 | complete |
| SF-2026-ARXIV-2606-26793 | RP-a221cf94ee8e3b56 | deep | arXiv:2606.26793v1 | SRC-ARXIV@arXiv:2606.26793v1 | arXiv:2606.26793v1 — §Attacks on RAG systems.; §III Method; §III-B Dual-Phase Architecture | arXiv:2606.26793v1 — §III-E B4 Decision-Only Evaluation; §IV Experiments; §Benchmark. | arXiv:2606.26793v1 — §III-A Threat Surfaces; §VI Discussion; §Limitations and scope. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26793 | complete |
| SF-2026-ARXIV-2606-26806 | RP-be3cda45979a3220 | deep | arXiv:2606.26806v1 | SRC-ARXIV@arXiv:2606.26806v1 | arXiv:2606.26806v1 — §3 Method | arXiv:2606.26806v1 — §5 Main Result: The Depth Flip | arXiv:2606.26806v1 — §7 Boundary Diagnostic: Memora; §9 Scope and Limitations; §10 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26806 | complete |
| SF-2026-ARXIV-2606-26836 | RP-d8359eeb159ee717 | deep | arXiv:2606.26836v1 | SRC-ARXIV@arXiv:2606.26836v1 | arXiv:2606.26836v1 — §4 Oracle Bias and Debiasing Methods; §4.3 Debiasing Methods; §4.3.1 Method 1: Extrapolation | arXiv:2606.26836v1 — §The Capability Frontier: Benchmarks Miss 82% of Model Performance; §5 Experimental Setup; §Benchmarks. | arXiv:2606.26836v1 — §7 Limitations; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26836 | complete |
| SF-2026-ARXIV-2606-26859 | RP-e759e87b59040605 | deep | arXiv:2606.26859v1 | SRC-ARXIV@arXiv:2606.26859v1 | arXiv:2606.26859v1 — §AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems; §3 Multi-Agent Design Framework; §4.3.2 System KB | arXiv:2606.26859v1 — §4.3.1 Experiment KB; §4.3.3 Data Analysis; §6 Evaluation Agent | arXiv:2606.26859v1 — §5.1.5 Failure Modes; §5.2.3 Robust execution under platform failures; §7.3 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26859 | complete |
| SF-2026-ARXIV-2606-26875 | RP-40658f40b42bbfe7 | deep | arXiv:2606.26875v1 | SRC-ARXIV@arXiv:2606.26875v1 | arXiv:2606.26875v1 — §3 Methodology | arXiv:2606.26875v1 — §4 Experiments; §4.1 Setup; §5 Analysis | arXiv:2606.26875v1 — §6 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26875 | complete |
| SF-2026-ARXIV-2606-26904 | RP-a3e869beb20be771 | deep | arXiv:2606.26904v1 | SRC-ARXIV@arXiv:2606.26904v1 | arXiv:2606.26904v1 — §3.4 Confidence-Cost Trade-off Reward for GRPO Training; §Training details.; §Training data. | arXiv:2606.26904v1 — §4 Experiments; §4.1 Experiment Setup; §4.2 Main Results | arXiv:2606.26904v1 — §5 Conclusion; §Appendix A Limitations and Broader Impact; §Limitations. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26904 | complete |
| SF-2026-ARXIV-2606-26917 | RP-1ee6b97534f1d294 | deep | arXiv:2606.26917v1 | SRC-ARXIV@arXiv:2606.26917v1 | arXiv:2606.26917v1 — §3.3 Design Principles; §B.3 Training Details; §Framework and Infrastructure. | arXiv:2606.26917v1 — §5 Experiment; §5.1 Experimental Setup; §5.4 Analysis and Ablation Studies | arXiv:2606.26917v1 — §Theoretical Discussion.; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26917 | complete |
| SF-2026-ARXIV-2606-26918 | RP-27bd074134c1bcb7 | deep | arXiv:2606.26918v1 | SRC-ARXIV@arXiv:2606.26918v1 | arXiv:2606.26918v1 — §3 Diagnostics: Task Insensitivity in Agentic Training; §3.2 Training-Time Dynamics Associated with Overfitting; §4 Observed Attention Drift During Training | arXiv:2606.26918v1 — §6 Experiments; §6.1 Experimental Setup; §6.2 Main Results | arXiv:2606.26918v1 — §7 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26918 | complete |
| SF-2026-ARXIV-2606-26924 | RP-2b0829636a3e1d36 | deep | arXiv:2606.26924v1 | SRC-ARXIV@arXiv:2606.26924v1 | arXiv:2606.26924v1 — §2.2 Orchestration frameworks and Autonomous Agents; §3. System Architecture; §Lifecycle design rationale | arXiv:2606.26924v1 — §6.2 Conformance results; §7.2 Results | arXiv:2606.26924v1 — §Trust boundary: cooperative trace linkage; §5. Threat Model; §7.4 Limitations of the study | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26924 | complete |
| SF-2026-ARXIV-2606-26933 | RP-03c98c53c3b83a37 | deep | arXiv:2606.26933v1 | SRC-ARXIV@arXiv:2606.26933v1 | arXiv:2606.26933v1 — §II System Overview; §II-B Chai’s Approach; §III System Design | arXiv:2606.26933v1 — §III-C Differential Testing: Output Analysis; §V Evaluation; §V-A Experimental Setup | arXiv:2606.26933v1 — §II-A Threat Model and Vulnerability Scope; §VII Discussion; §IX Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26933 | complete |
| SF-2026-ARXIV-2606-26935 | RP-4da1a6a9cc67c133 | deep | arXiv:2606.26935v1 | SRC-ARXIV@arXiv:2606.26935v1 | arXiv:2606.26935v1 — §Where Do CoT Training Gains Land in LLM based Agents?; §3 Setup and Diagnostic Framework; §4 Training Makes Actions More Predictable from the Prompt | arXiv:2606.26935v1 — §3 Setup and Diagnostic Framework; §4.2 Direct Prompt-vs-CoT Comparisons in Online Evaluation; §6.1 Evaluation | arXiv:2606.26935v1 — §7 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26935 | complete |
| SF-2026-ARXIV-2606-26960 | RP-1f26763564b775cf | deep | arXiv:2606.26960v1 | SRC-ARXIV@arXiv:2606.26960v1 | arXiv:2606.26960v1 — §Toward Agentic SysAdmin: Rethinking System Administration with AI Agents; §III NetLLMeval Architecture; §V-B Effect of Solver Architecture | arXiv:2606.26960v1 — §III-B Evaluation Pipeline; §IV Experiments; §IV-E Evaluation Metrics | arXiv:2606.26960v1 — §VI Discussion; §VII Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26960 | complete |
| SF-2026-ARXIV-2606-26978 | RP-949c69a7ccb3b263 | deep | arXiv:2606.26978v1 | SRC-ARXIV@arXiv:2606.26978v1 | arXiv:2606.26978v1 — §3. Experimental Setup; §3.5. Implementation Details | arXiv:2606.26978v1 — §4. Evaluation; §4.2. RQ2: Effectiveness and Cost Analysis | arXiv:2606.26978v1 — §5.2. Threats to Validity; §7. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26978 | complete |
| SF-2026-ARXIV-2606-26979 | RP-095c0f40a6194ee1 | deep | arXiv:2606.26979v1 | SRC-ARXIV@arXiv:2606.26979v1 | arXiv:2606.26979v1 — §4. Approach; §4.1. System Overview | arXiv:2606.26979v1 — §3. Motivation and Problem Analysis; §4.2. CodeAnchor Tags: Static-Analysis-Based Structured Comments; §5. Evaluation | arXiv:2606.26979v1 — §6. Discussion; §7. Threats to Validity and Limitations; §9. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26979 | complete |
| SF-2026-ARXIV-2606-26990 | RP-05c879cf00a44f52 | deep | arXiv:2606.26990v1 | SRC-ARXIV@arXiv:2606.26990v1 | arXiv:2606.26990v1 — §Remark 3.3 (On the choice of our framework) . | arXiv:2606.26990v1 — §Decision-Aligned Evaluation of Uncertainty Quantification; §Common UQ evaluation metrics in ML; §5 Experiments | arXiv:2606.26990v1 — §6 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26990 | complete |
| SF-2026-ARXIV-2606-26997 | RP-1cbf6018bed2171f | deep | arXiv:2606.26997v1 | SRC-ARXIV@arXiv:2606.26997v1 | arXiv:2606.26997v1 — §RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning; §3 RolloutPipe Design; §3.2 Training-Side Complete-Group Pipelining | arXiv:2606.26997v1 — §5 Performance Evaluation; §5.1 Experimental Setup; §5.2 Results Analysis | arXiv:2606.26997v1 — §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-26997 | complete |
| SF-2026-ARXIV-2606-27005 | RP-5f501ad6271dedad | deep | arXiv:2606.27005v1 | SRC-ARXIV@arXiv:2606.27005v1 | arXiv:2606.27005v1 — §II Methodology | arXiv:2606.27005v1 — §III Numerical Results and Discussion; §III-F Lyapunov Energy and Stability Analysis | arXiv:2606.27005v1 — §III Numerical Results and Discussion; §IV Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27005 | complete |
| SF-2026-ARXIV-2606-27009 | RP-6b7b3acb99c03c38 | deep | arXiv:2606.27009v1 | SRC-ARXIV@arXiv:2606.27009v1 | arXiv:2606.27009v1 — §Uncertainty and orchestration in multi-LLM systems.; §IV Method | arXiv:2606.27009v1 — §RAG evaluation.; §V Theoretical Analysis; §VI A Judge-Efficient Evaluation Protocol | arXiv:2606.27009v1 — §IX Discussion; §X Limitations; §XI Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27009 | complete |
| SF-2026-ARXIV-2606-27027 | RP-7ce97d90ba3d4f07 | deep | arXiv:2606.27027v1 | SRC-ARXIV@arXiv:2606.27027v1 | arXiv:2606.27027v1 — §4. ShareLock: a Multi-Tool Threshold Poisoning Attack Framework; §D.1. System Prompt for Zero-Shot Detection | arXiv:2606.27027v1 — §5. Evaluation; §5.1. Experimental Setup; §Appendix D Experimental details of Safety Classification Task | arXiv:2606.27027v1 — §3.3. Threat Model; §6. Discussion and Limitations; §7. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27027 | complete |
| SF-2026-ARXIV-2606-27045 | RP-98c06b22487fb979 | deep | arXiv:2606.27045v1 | SRC-ARXIV@arXiv:2606.27045v1 | arXiv:2606.27045v1 — §5 The Spec Growth Engine; §5.2 The Spec Graph: Nodes and Edges; §5.4 Drift Validation: Intent Graph vs. Evidence Graph | arXiv:2606.27045v1 — §6 Development Workflow; §7 Worked Example: Growing a Checkout | arXiv:2606.27045v1 — §9 Discussion; §Limitations.; §10 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27045 | complete |
| SF-2026-ARXIV-2606-27079 | RP-2163d1f2265c677e | deep | arXiv:2606.27079v1 | SRC-ARXIV@arXiv:2606.27079v1 | arXiv:2606.27079v1 — §II-A Benchmarking methods for existing VLA systems; §III ForesightSafety-VLA Benchmark Design | arXiv:2606.27079v1 — §ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models; §II-A Benchmarking methods for existing VLA systems; §III ForesightSafety-VLA Benchmark Design | arXiv:2606.27079v1 — §VI Discussion and Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27079 | complete |
| SF-2026-ARXIV-2606-27091 | RP-d71f50b1a8beeb8d | deep | arXiv:2606.27091v1 | SRC-ARXIV@arXiv:2606.27091v1 | arXiv:2606.27091v1 — §4 Methods | arXiv:2606.27091v1 — §Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation; §4.3 Reusable Evasion Benchmark Construction; §5 Evaluation & Results | arXiv:2606.27091v1 — §Linear probe at the circuit boundary.; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27091 | complete |
| SF-2026-ARXIV-2606-27136 | RP-033f4b20950ffaaa | deep | arXiv:2606.27136v1 | SRC-ARXIV@arXiv:2606.27136v1 | arXiv:2606.27136v1 — §IV-A Overall Framework; §V-B Baseline Methods | arXiv:2606.27136v1 — §V Experiments; §V-A Environments and Evaluation Metrics | arXiv:2606.27136v1 — §VI Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27136 | complete |
| SF-2026-ARXIV-2606-27146 | RP-8760cca9364ffd54 | deep | arXiv:2606.27146v1 | SRC-ARXIV@arXiv:2606.27146v1 | arXiv:2606.27146v1 — §III METHOD; §III-C Training Pipeline | arXiv:2606.27146v1 — §IV EXPERIMENTATION; §IV-A Experimental Setup; §IV-B Main Results | arXiv:2606.27146v1 — §IV-D Analysis and Discussion; §V CONCLUSIONS | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27146 | complete |
| SF-2026-ARXIV-2606-27153 | RP-a85b898493afffbb | deep | arXiv:2606.27153v1 | SRC-ARXIV@arXiv:2606.27153v1 | arXiv:2606.27153v1 — §DMuon: Efficient Distributed Muon Training with Near-Adam Overhead; §2.2 Sharded Training Abstractions; §3 System Design | arXiv:2606.27153v1 — §5 Evaluation; §Setup. | arXiv:2606.27153v1 — §5.3 Limitations; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27153 | complete |
| SF-2026-ARXIV-2606-27154 | RP-e1ba4296db36de9e | deep | arXiv:2606.27154v1 | SRC-ARXIV@arXiv:2606.27154v1 | arXiv:2606.27154v1 — §Appendix B Benchmark Systems and Topology; §B.1 Systems Overview; §F.1 Agent Evaluation Framework | arXiv:2606.27154v1 — §2.1 Setup: Forward Verification from a Known Intervention; §3 Experiments; §3.1 Experimental Setup | arXiv:2606.27154v1 — §3.3 Failure Mode Characterization; §5 Assumptions and Threats to Validity; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27154 | complete |
| SF-2026-ARXIV-2606-27188 | RP-c70bb6680f981ec3 | deep | arXiv:2606.27188v1 | SRC-ARXIV@arXiv:2606.27188v1 | arXiv:2606.27188v1 — §A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO; §4 CUGA FLO System Architecture | arXiv:2606.27188v1 — §6.1.1 Property Analysis | arXiv:2606.27188v1 — §7 Discussion and Conclusion; §7.2 Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27188 | complete |
| SF-2026-ARXIV-2606-27205 | RP-85e279226f35f6e7 | deep | arXiv:2606.27205v1 | SRC-ARXIV@arXiv:2606.27205v1 | arXiv:2606.27205v1 — §III Methodology; §III-A Quantization Methods | arXiv:2606.27205v1 — §III-C Benchmarks; §III-D Evaluation Metrics; §III-E Statistical & Trade-offs Analysis | arXiv:2606.27205v1 — §V Discussion; §VI Threats to Validity; §VII Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27205 | complete |
| SF-2026-ARXIV-2606-27210 | RP-e190b4b20ea1d5c8 | deep | arXiv:2606.27210v1 | SRC-ARXIV@arXiv:2606.27210v1 | arXiv:2606.27210v1 — §Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes; §4 Intent-Aware Training Regimes; §Reward design. | arXiv:2606.27210v1 — §3.3 Quality and Agreement Analysis; §5 Experimental Setting; §Evaluation protocol. | arXiv:2606.27210v1 — §6 Results and Discussion; §Failure modes differ by distribution.; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27210 | complete |
| SF-2026-ARXIV-2606-27226 | RP-34d17757fc6309f4 | deep | arXiv:2606.27226v1 | SRC-ARXIV@arXiv:2606.27226v1 | arXiv:2606.27226v1 — §3 Method; §Appendix C Automatic Prompt Update Algorithm | arXiv:2606.27226v1 — §Ask, Don’t Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement; §3.2 Binary Evaluation and Scoring; §4 Experimental Setup | arXiv:2606.27226v1 — §6 Discussion; §7 Conclusion; §A.2.3 Example 3: Failure Case — Relevance (SummEval) | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27226 | complete |
| SF-2026-ARXIV-2606-27242 | RP-bf3a1838ef0a566b | deep | arXiv:2606.27242v1 | SRC-ARXIV@arXiv:2606.27242v1 | arXiv:2606.27242v1 — §A.2 Which Method is Used Where; §Practical use: Proxy accuracy is architecture-dependent.; §Algorithm: Full FisherSketch. | arXiv:2606.27242v1 — §6 Experiments; §Estimator usage across experiments.; §Setup. | arXiv:2606.27242v1 — §7 Discussion; §7.1 Limitations & Broader Applicability; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27242 | complete |
| SF-2026-ARXIV-2606-27243 | RP-c7b3b3f7092418fa | deep | arXiv:2606.27243v1 | SRC-ARXIV@arXiv:2606.27243v1 | arXiv:2606.27243v1 — §NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems Thanks: ∗ Equal contribution. Thanks: † Corresponding author.; §Self-evolving recommender systems.; §Architecture state and feasible modification space. | arXiv:2606.27243v1 — §Offline and online evaluation objectives.; §5. Experiments; §5.2. Experimental Settings | arXiv:2606.27243v1 — §4.4. Silent-Failure-Aware Multi-Stage Architecture Verification; §Capability boundary.; §6. Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27243 | complete |
| SF-2026-ARXIV-2606-27251 | RP-51068b58e8e9ed08 | deep | arXiv:2606.27251v1 | SRC-ARXIV@arXiv:2606.27251v1 | arXiv:2606.27251v1 — §3 Methodology: The OmniAcr Framework; §Appendix F Visual Monitor: Design and Empirical Evaluation | arXiv:2606.27251v1 — §4 Experiments; §4.1 Experimental Setup; §Appendix B Real-World Experimental Setup | arXiv:2606.27251v1 — §5 Conclusions; §Appendix A Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27251 | complete |
| SF-2026-ARXIV-2606-27268 | RP-b322c7d8d90955af | deep | arXiv:2606.27268v1 | SRC-ARXIV@arXiv:2606.27268v1 | arXiv:2606.27268v1 — §E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation; §3.1 Framework Overview; §4.1 Experiments on Different Types of Manipulation Methods | arXiv:2606.27268v1 — §4 Experiments; §4.1 Experiments on Different Types of Manipulation Methods; §4.5 Real-robot Experiments | arXiv:2606.27268v1 — §5 Conclusion and Future Work; §Appendix 0.D Limitation | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27268 | complete |
| SF-2026-ARXIV-2606-27288 | RP-35267fb38f6578a1 | deep | arXiv:2606.27288v1 | SRC-ARXIV@arXiv:2606.27288v1 | arXiv:2606.27288v1 — §3 Problem Formulation; §Proposition 1 (Ceiling, gain localization, and a realizability certificate) . | arXiv:2606.27288v1 — §4 Experimental Setup; §5 Results | arXiv:2606.27288v1 — §7 Limitations; §Honest limits.; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27288 | complete |
| SF-2026-ARXIV-2606-27326 | RP-1e1ba570513f0d20 | deep | arXiv:2606.27326v1 | SRC-ARXIV@arXiv:2606.27326v1 | arXiv:2606.27326v1 — §3 Training a Large Visual World Model | arXiv:2606.27326v1 — §5 Experiments; §5.1 Main results; §Appendix E Additional Results | arXiv:2606.27326v1 — §5.2 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27326 | complete |
| SF-2026-ARXIV-2606-27330 | RP-6c7edaf0ecdc9a5b | deep | arXiv:2606.27330v1 | SRC-ARXIV@arXiv:2606.27330v1 | arXiv:2606.27330v1 — §2 Planning Experience Exploration and Utilization Method; §2.1 Method; §Exploration and training settings. | arXiv:2606.27330v1 — §2.2 Experimental Settings; §Evaluation.; §2.3 Results and Analysis | arXiv:2606.27330v1 — §5 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27330 | complete |
| SF-2026-ARXIV-2606-27350 | RP-41a02903935bd0e4 | deep | arXiv:2606.27350v1 | SRC-ARXIV@arXiv:2606.27350v1 | arXiv:2606.27350v1 — §3. The CHIA Workflow Abstraction; §4. Design; §4.3. Runtime Features | arXiv:2606.27350v1 — §5. Case Studies; §5.5. Automatically addressing GitHub issues in the CIRCT compiler in a project maintainer friendly way | arXiv:2606.27350v1 — §7. Discussion and Future Work; §8. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27350 | complete |
| SF-2026-ARXIV-2606-27355 | RP-5072df41e0424ccf | deep | arXiv:2606.27355v1 | SRC-ARXIV@arXiv:2606.27355v1 | arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Training objective; §Commissioning turns a policy pool into a stronger system | arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Problem Setup; §Experimental Protocol | arXiv:2606.27355v1 — §Failure analysis: context and evidence; §Discussion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27355 | complete |
| SF-2026-ARXIV-2606-27359 | RP-a65cb712ad812cc2 | deep | arXiv:2606.27359v1 | SRC-ARXIV@arXiv:2606.27359v1 | arXiv:2606.27359v1 — §2 Decoding Methods Maximize Sequence Probability in LLMs; §2.1 Local Decoding Methods; §2.2 Global Decoding Methods | arXiv:2606.27359v1 — §Appendix D Details on Experimental Setup; §Appendix E Additional Experiments and Analysis | arXiv:2606.27359v1 — §4 Discussion and Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27359 | complete |
| SF-2026-ARXIV-2606-27369 | RP-e97c85914b0bdeb6 | deep | arXiv:2606.27369v1 | SRC-ARXIV@arXiv:2606.27369v1 | arXiv:2606.27369v1 — §Reward Design and Exploration; §RLVR Algorithms; §4 Method | arXiv:2606.27369v1 — §5 Experiments; §5.1 Experimental Setup; §Evaluation benchmarks and metrics. | arXiv:2606.27369v1 — §6 Discussion: An Information-Theoretic View of Group-Relative Learning Signals; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27369 | complete |
| SF-2026-ARXIV-2606-27374 | RP-4502c3212dc4b2fb | deep | arXiv:2606.27374v1 | SRC-ARXIV@arXiv:2606.27374v1 | arXiv:2606.27374v1 — §4 Method; §Appendix B Training Details; §B.2 Training Hyperparameters | arXiv:2606.27374v1 — §5 Experimental Results; §5.1 Implementation Details & Evaluation Metrics; §B.3 Evaluation | arXiv:2606.27374v1 — §6 Limitations of ReGen & Future Direction; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27374 | complete |
| SF-2026-ARXIV-2606-27375 | RP-597a70f6a211527d | deep | arXiv:2606.27375v1 | SRC-ARXIV@arXiv:2606.27375v1 | arXiv:2606.27375v1 — §2 ABC-130K Dataset; §3 ABC-Models; §7 Infrastructure | arXiv:2606.27375v1 — §3.4 Offline Metrics for Policy Evaluation; §5 Real-World Capabilities; §Appendix G Evaluation Details | arXiv:2606.27375v1 — §8 Requests for Research | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-27375 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-26156:start -->
### 2606.26156 — Kiko: Programming Agents to Enact Interaction Protocols

**问题与旧路径。** Realizing a multiagent system involves implementing member agents who interact based on a protocol while making decisions in a decentralized manner.

**机制、状态与控制流。** 把 agent 内部 decision logic 与公开 message protocol 分离：decision maker 只能从 valid decisions 选互相兼容 emission set，adapter 隔离 communication service，operational semantics 拥有 protocol compliance。 唯一 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。

<!-- claim:SF-2026-ARXIV-2606-26156:start -->
Claim boundary：仅 `arXiv:2606.26156v1`；未证明边界定位 `https://arxiv.org/html/2606.26156v1 — §5 Discussion and conference-era implementation scope`。
<!-- claim:SF-2026-ARXIV-2606-26156:end -->
<!-- review:SF-2026-ARXIV-2606-26156:end -->

<!-- review:SF-2026-ARXIV-2606-26185:start -->
### 2606.26185 — Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations

**问题与旧路径。** LLM-as-judge ("grader") components are now standard in evaluation harnesses, including safety evaluations where a pass/fail verdict may gate downstream deployment decisions.

**机制、状态与控制流。** `Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26185:start -->
Claim boundary：仅 `arXiv:2606.26185v1`；未证明边界定位 `https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains`。
<!-- claim:SF-2026-ARXIV-2606-26185:end -->
<!-- review:SF-2026-ARXIV-2606-26185:end -->

<!-- review:SF-2026-ARXIV-2606-26211:start -->
### 2606.26211 — Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem

**问题与旧路径。** NANDini (Networked Agents Natural Distillation of Interconnected Nodal Intelligence) envisions an automated ecosystem where intelligent agents independently create, process, and exchange data to drive decisions at scale.

**机制、状态与控制流。** `Data Facts metadata schema; provenance, semantics, constraints and exchange contract` 所定义的源特定机制用于以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26211:start -->
Claim boundary：仅 `arXiv:2606.26211v1`；未证明边界定位 `https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness`。
<!-- claim:SF-2026-ARXIV-2606-26211:end -->
<!-- review:SF-2026-ARXIV-2606-26211:end -->

<!-- review:SF-2026-ARXIV-2606-26257:start -->
### 2606.26257 — Dataset Usage Inference without Shadow Models or Held-out Data

**问题与旧路径。** How much of my data was used to train a machine learning model?

**机制、状态与控制流。** `Dataset Usage Inference formulation without shadow models or held-out data` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26257:start -->
Claim boundary：仅 `arXiv:2606.26257v1`；未证明边界定位 `https://arxiv.org/html/2606.26257v1 — §Requires the paper's observable score/query regime; not per-record legal attribution`。
<!-- claim:SF-2026-ARXIV-2606-26257:end -->
<!-- review:SF-2026-ARXIV-2606-26257:end -->

<!-- review:SF-2026-ARXIV-2606-26298:start -->
### 2606.26298 — Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems

**问题与旧路径。** Autonomous AI agents may begin to perform consequential, irreversible actions such as clinical prescribing and production software deployment.

**机制、状态与控制流。** `Governing Actions, Not Agents; Institutional Attestation model` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26298:start -->
Claim boundary：仅 `arXiv:2606.26298v1`；未证明边界定位 `https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark`。
<!-- claim:SF-2026-ARXIV-2606-26298:end -->
<!-- review:SF-2026-ARXIV-2606-26298:end -->

<!-- review:SF-2026-ARXIV-2606-26300:start -->
### 2606.26300 — The Verification Horizon: No Silver Bullet for Coding Agent Rewards

**问题与旧路径。** A classical intuition holds that verifying a solution is easier than producing one.

**机制、状态与控制流。** `Verification Horizon formulation for coding-agent rewards` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26300:start -->
Claim boundary：仅 `arXiv:2606.26300v1`；未证明边界定位 `https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain`。
<!-- claim:SF-2026-ARXIV-2606-26300:end -->
<!-- review:SF-2026-ARXIV-2606-26300:end -->

<!-- review:SF-2026-ARXIV-2606-26341:start -->
### 2606.26341 — Scaling Nonlinear Optimization: Many Problems One GPU

**问题与旧路径。** Many robotics problems, including trajectory optimization, inverse kinematics, and contact-rich motion planning, reduce to nonlinear programs (NLPs).

**机制、状态与控制流。** `Many Problems One GPU batching and nonlinear-optimization execution design` 所定义的源特定机制用于把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26341:start -->
Claim boundary：仅 `arXiv:2606.26341v1`；未证明边界定位 `https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof`。
<!-- claim:SF-2026-ARXIV-2606-26341:end -->
<!-- review:SF-2026-ARXIV-2606-26341:end -->

<!-- review:SF-2026-ARXIV-2606-26344:start -->
### 2606.26344 — Axon: A Synthesizing Superoptimizer for Tensor Programs

**问题与旧路径。** Writing high performance kernels for AI accelerators requires deep expertise in tiling, instruction selection, data layout, and operator fusion placing a significant burden on programmers.

**机制、状态与控制流。** `Axon synthesizing superoptimizer; tensor-program search and verification` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26344:start -->
Claim boundary：仅 `arXiv:2606.26344v1`；未证明边界定位 `https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence`。
<!-- claim:SF-2026-ARXIV-2606-26344:end -->
<!-- review:SF-2026-ARXIV-2606-26344:end -->

<!-- review:SF-2026-ARXIV-2606-26356:start -->
### 2606.26356 — Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems

**问题与旧路径。** Practitioners of prompt-composed agentic systems report a recurring failure mode: editing one prompt module silently shifts the behavior of others despite no shared variable or executable dependency.

**机制、状态与控制流。** `Instruction Bleed formulation; prompt-composed module interference` 所定义的源特定机制用于把模块间指令干扰作为可测试的组合边界，而非默认隔离；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26356:start -->
Claim boundary：仅 `arXiv:2606.26356v1`；未证明边界定位 `https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness`。
<!-- claim:SF-2026-ARXIV-2606-26356:end -->
<!-- review:SF-2026-ARXIV-2606-26356:end -->

<!-- review:SF-2026-ARXIV-2606-26377:start -->
### 2606.26377 — Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats

**问题与旧路径。** Large language models (LLMs) are increasingly deployed in interactive applications, yet they remain vulnerable to adversarial interactions that induce harmful, deceptive, or policy-violating outputs.

**机制、状态与控制流。** `Unified intent-and-harm verification defense` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26377:start -->
Claim boundary：仅 `arXiv:2606.26377v1`；未证明边界定位 `https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution`。
<!-- claim:SF-2026-ARXIV-2606-26377:end -->
<!-- review:SF-2026-ARXIV-2606-26377:end -->

<!-- review:SF-2026-ARXIV-2606-26383:start -->
### 2606.26383 — SOLAR: AI-Powered Speed-of-Light Performance Analysis

**问题与旧路径。** How fast could a deep-learning model run on target hardware, and how far is today's implementation from that limit?

**机制、状态与控制流。** `SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation` 所定义的源特定机制用于以校准后的硬件与 workload 参数分解性能上界和瓶颈；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26383:start -->
Claim boundary：仅 `arXiv:2606.26383v1`；未证明边界定位 `https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects`。
<!-- claim:SF-2026-ARXIV-2606-26383:end -->
<!-- review:SF-2026-ARXIV-2606-26383:end -->

<!-- review:SF-2026-ARXIV-2606-26429:start -->
### 2606.26429 — DualEval: Joint Model-Item Calibration for Unified LLM Evaluation

**问题与旧路径。** Current LLM evaluation relies on two complementary but often disconnected signals: static benchmarks with objective correctness labels and arena-style preference data that better reflect open-ended user interactions.

**机制、状态与控制流。** `DualEval joint model-item calibration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26429:start -->
Claim boundary：仅 `arXiv:2606.26429v1`；未证明边界定位 `https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting`。
<!-- claim:SF-2026-ARXIV-2606-26429:end -->
<!-- review:SF-2026-ARXIV-2606-26429:end -->

<!-- review:SF-2026-ARXIV-2606-26439:start -->
### 2606.26439 — TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization

**问题与旧路径。** Multi-vector retrieval models such as ColBERT achieve state-of-the-art accuracy through fine-grained token-level MaxSim scoring, yet existing GPU implementations leave most hardware performance unused.

**机制、状态与控制流。** `TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26439:start -->
Claim boundary：仅 `arXiv:2606.26439v1`；未证明边界定位 `https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved`。
<!-- claim:SF-2026-ARXIV-2606-26439:end -->
<!-- review:SF-2026-ARXIV-2606-26439:end -->

<!-- review:SF-2026-ARXIV-2606-26441:start -->
### 2606.26441 — GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices

**问题与旧路径。** Learned sparse retrieval models such as SPLADE achieve retrieval quality competitive with dense models while preserving the interpretability and exact-match advantages of sparse representations.

**机制、状态与控制流。** `GPUSparse learned sparse retrieval with parallel inverted indices` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26441:start -->
Claim boundary：仅 `arXiv:2606.26441v1`；未证明边界定位 `https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling`。
<!-- claim:SF-2026-ARXIV-2606-26441:end -->
<!-- review:SF-2026-ARXIV-2606-26441:end -->

<!-- review:SF-2026-ARXIV-2606-26442:start -->
### 2606.26442 — AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities

**问题与旧路径。** We present AXLE (Axiom Lean Engine), a cloud service for Lean 4 proof manipulation, extraction, and verification.

**机制、状态与控制流。** `AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26442:start -->
Claim boundary：仅 `arXiv:2606.26442v1`；未证明边界定位 `https://arxiv.org/html/2606.26442v1 — §Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety`。
<!-- claim:SF-2026-ARXIV-2606-26442:end -->
<!-- review:SF-2026-ARXIV-2606-26442:end -->

<!-- review:SF-2026-ARXIV-2606-26449:start -->
### 2606.26449 — ProvenAI: Provenance-Native Traces of Evidence in Generated Answers

**问题与旧路径。** Retrieval-augmented systems routinely present citations alongside generated answers, yet a citation does not confirm that the corresponding source meaningfully shaped the output.

**机制、状态与控制流。** `ProvenAI provenance-native trace schema and evidence links` 所定义的源特定机制用于让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26449:start -->
Claim boundary：仅 `arXiv:2606.26449v1`；未证明边界定位 `https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth`。
<!-- claim:SF-2026-ARXIV-2606-26449:end -->
<!-- review:SF-2026-ARXIV-2606-26449:end -->

<!-- review:SF-2026-ARXIV-2606-26453:start -->
### 2606.26453 — Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization

**问题与旧路径。** We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools.

**机制、状态与控制流。** `Micro-profiling tools as expert surrogates for LLM CUDA optimization` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26453:start -->
Claim boundary：仅 `arXiv:2606.26453v1`；未证明边界定位 `https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback`。
<!-- claim:SF-2026-ARXIV-2606-26453:end -->
<!-- review:SF-2026-ARXIV-2606-26453:end -->

<!-- review:SF-2026-ARXIV-2606-26456:start -->
### 2606.26456 — Towards Safety-Aware Mutation Testing for Autonomous Driving Systems

**问题与旧路径。** Simulation-based testing is essential for ensuring the safety of Autonomous Driving Systems (ADS), yet the community lacks a systematic criterion for determining when we can safely stop additional test scenario generation.

**机制、状态与控制流。** `Safety-Aware Mutation Testing proposal and interaction-aware mutant model` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26456:start -->
Claim boundary：仅 `arXiv:2606.26456v1`；未证明边界定位 `https://arxiv.org/html/2606.26456v1 — §Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional`。
<!-- claim:SF-2026-ARXIV-2606-26456:end -->
<!-- review:SF-2026-ARXIV-2606-26456:end -->

<!-- review:SF-2026-ARXIV-2606-26463:start -->
### 2606.26463 — Finding the Time to Think: Learning Planning Budgets in Real-Time RL

**问题与旧路径。** Deliberating takes time.

**机制、状态与控制流。** `Variable-delay real-time RL; lightweight gate selects state-dependent planning budget` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26463:start -->
Claim boundary：仅 `arXiv:2606.26463v1`；未证明边界定位 `https://arxiv.org/html/2606.26463v1 — §Game planners and timing model do not prove benefit under production tool latency or safety deadlines`。
<!-- claim:SF-2026-ARXIV-2606-26463:end -->
<!-- review:SF-2026-ARXIV-2606-26463:end -->

<!-- review:SF-2026-ARXIV-2606-26472:start -->
### 2606.26472 — Epiphany-Aware KV Cache Eviction Without the Attention Matrix

**问题与旧路径。** As reasoning models emit chains of thought tens of thousands of tokens long, KV cache increasingly becomes a deployment bottleneck.

**机制、状态与控制流。** `Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26472:start -->
Claim boundary：仅 `arXiv:2606.26472v1`；未证明边界定位 `https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback`。
<!-- claim:SF-2026-ARXIV-2606-26472:end -->
<!-- review:SF-2026-ARXIV-2606-26472:end -->

<!-- review:SF-2026-ARXIV-2606-26479:start -->
### 2606.26479 — Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents

**问题与旧路径。** Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions.

**机制、状态与控制流。** `Out-of-band prompt-injection defenses organized as reference monitors and integrity policies` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26479:start -->
Claim boundary：仅 `arXiv:2606.26479v1`；未证明边界定位 `https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness`。
<!-- claim:SF-2026-ARXIV-2606-26479:end -->
<!-- review:SF-2026-ARXIV-2606-26479:end -->

<!-- review:SF-2026-ARXIV-2606-26488:start -->
### 2606.26488 — What Survives When You Compress a Recursive Reasoner for the Edge?

**问题与旧路径。** Recursive reasoning models can solve complex structured tasks with only a few million parameters by repeatedly updating a latent state.

**机制、状态与控制流。** `Compression of recursive reasoners across precision, pruning, distillation and attention variants` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26488:start -->
Claim boundary：仅 `arXiv:2606.26488v1`；未证明边界定位 `https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation`。
<!-- claim:SF-2026-ARXIV-2606-26488:end -->
<!-- review:SF-2026-ARXIV-2606-26488:end -->

<!-- review:SF-2026-ARXIV-2606-26492:start -->
### 2606.26492 — Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs

**问题与旧路径。** Deep Learning (DL) programs can fail during training for many reasons, and diagnosing the cause is a costly and time-consuming maintenance task.

**机制、状态与控制流。** `Within-program versus leave-program-out diagnostic design` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26492:start -->
Claim boundary：仅 `arXiv:2606.26492v1`；未证明边界定位 `https://arxiv.org/html/2606.26492v1 — §Fault-injected programs and studied diagnosers do not prove production root-cause validity`。
<!-- claim:SF-2026-ARXIV-2606-26492:end -->
<!-- review:SF-2026-ARXIV-2606-26492:end -->

<!-- review:SF-2026-ARXIV-2606-26511:start -->
### 2606.26511 — Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge

**问题与旧路径。** The central result is the stale-fact-error rate: when required to answer, RAG serves superseded values 15-40% of the time; MemStrata drives this to ~0%, a failure class RAG cannot avoid. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge 的 exact-v1 机制为：We present MemStrata, a retrieval memory maintaining temporal validity. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26511v1 — §4 The MemStrata Architecture; §4.3 The “retain, then supersede” design`；Evaluation=`arXiv:2606.26511v1 — §4.5 Marker-free benchmark construction; §5 Experiments; §5.3 Stale-fact error: the structural result`；counterevidence=`arXiv:2606.26511v1 — §6 Discussion; §7 Limitations; §8 Conclusion`。exact-v1 的观测边界是：We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. 它没有证明 We present MemStrata, a retrieval memory maintaining temporal validity. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：The central result is the stale-fact-error rate: when required to answer, RAG serves superseded values 15-40% of the time; MemStrata drives this to ~0%, a failure class RAG cannot avoid. 披露的 evaluation signal 是：We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. exact-v1 的观测边界是：We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. 它没有证明 We present MemStrata, a retrieval memory maintaining temporal validity. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26511:start -->
Primary identity `arXiv:2606.26511v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26511:end -->
<!-- review:SF-2026-ARXIV-2606-26511:end -->

<!-- review:SF-2026-ARXIV-2606-26524:start -->
### 2606.26524 — VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills

**问题与旧路径。** Enforcing them raises a contextual granularity challenge: even when a policy is written for a particular task context, a monitor must still decide which events to observe, what state to retain, how far across the execution to reason, and where to intervene. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills 的 exact-v1 机制为：In this work, we present VIGIL, an end-to-end runtime enforcement framework for agentic systems. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26524v1 — §IV The Vigil Framework; §IV-A Algorithm Overview`；Evaluation=`arXiv:2606.26524v1 — §VII Evaluation; §VII-A Experimental Setup`；counterevidence=`arXiv:2606.26524v1 — §III-C Threat Model; §IX Conclusion`。exact-v1 的观测边界是：The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. 它没有证明 In this work, we present VIGIL, an end-to-end runtime enforcement framework for agentic systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Enforcing them raises a contextual granularity challenge: even when a policy is written for a particular task context, a monitor must still decide which events to observe, what state to retain, how far across the execution to reason, and where to intervene. 披露的 evaluation signal 是：The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. exact-v1 的观测边界是：The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. 它没有证明 In this work, we present VIGIL, an end-to-end runtime enforcement framework for agentic systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26524:start -->
Primary identity `arXiv:2606.26524v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26524:end -->
<!-- review:SF-2026-ARXIV-2606-26524:end -->

<!-- review:SF-2026-ARXIV-2606-26529:start -->
### 2606.26529 — The inattentional gap in task conditioned AI models that omit otherwise reportable safety critical signals

**问题与旧路径。** AI in radiology and other safety-critical workflows is evaluated on the hazards it is told to find, yet harm arises disproportionately from hazards no one specified. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The inattentional gap in task conditioned AI models that omit otherwise reportable safety critical signals 的 exact-v1 机制为：We term this dissociation the Inattentional Gap: a system can score near-perfectly on specified hazards while omitting co-present safety-critical hazards. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26529v1 — §A System-1-style task capture without reliable intrinsic oversight`；Evaluation=`arXiv:2606.26529v1 — §Results; §Experimental Procedures`；counterevidence=`arXiv:2606.26529v1 — §Discussion; §Limitations`。exact-v1 的观测边界是：AI in radiology and other safety-critical workflows is evaluated on the hazards it is told to find, yet harm arises disproportionately from hazards no one specified. 它没有证明 We term this dissociation the Inattentional Gap: a system can score near-perfectly on specified hazards while omitting co-present safety-critical hazards. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：AI in radiology and other safety-critical workflows is evaluated on the hazards it is told to find, yet harm arises disproportionately from hazards no one specified. 披露的 evaluation signal 是：AI in radiology and other safety-critical workflows is evaluated on the hazards it is told to find, yet harm arises disproportionately from hazards no one specified. exact-v1 的观测边界是：AI in radiology and other safety-critical workflows is evaluated on the hazards it is told to find, yet harm arises disproportionately from hazards no one specified. 它没有证明 We term this dissociation the Inattentional Gap: a system can score near-perfectly on specified hazards while omitting co-present safety-critical hazards. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26529:start -->
Primary identity `arXiv:2606.26529v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26529:end -->
<!-- review:SF-2026-ARXIV-2606-26529:end -->

<!-- review:SF-2026-ARXIV-2606-26587:start -->
### 2606.26587 — SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference

**问题与旧路径。** Low-bit floating-point formats and semi-structured sparsity are increasingly supported by modern accelerators, yet combining them for LLM activation compression remains challenging: activations contain input-dependent outliers that dominate block scales in FP4 quantization, and directly applying N:M sparsity masks discards moderate values, coupling sparsification loss with quantization error. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference 的 exact-v1 机制为：We introduce SharQ, a training-free inference method that bridges activation sparsity and FP4 quantization through an online sparse--dense decomposition. 因此 把设备频率、功耗/温度估计、QoE 和模型/backend identity 联合验收。 唯一 owner 为 `INFER-GPU-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26587v1 — §3 Methodology; §3.4 Kernel design; §A.1.1 Design rationale`；Evaluation=`arXiv:2606.26587v1 — §3.5 Theoretical analysis; §4 Experiments; §4.1 Experimental setup`；counterevidence=`arXiv:2606.26587v1 — §5 Conclusion`。exact-v1 的观测边界是：Evaluated on Llama-3.1-8B, Qwen2.5-7B, Qwen3-30B-A3B, and Qwen3-VL-8B, SharQ recovers 43--63% of the NVFP4-to-FP16 accuracy gap across language and vision-language tasks, and generalizes across NVFP4, HiF4, and MXFP4 formats. 它没有证明 We introduce SharQ, a training-free inference method that bridges activation sparsity and FP4 quantization through an online sparse--dense decomposition. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Low-bit floating-point formats and semi-structured sparsity are increasingly supported by modern accelerators, yet combining them for LLM activation compression remains challenging: activations contain input-dependent outliers that dominate block scales in FP4 quantization, and directly applying N:M sparsity masks discards moderate values, coupling sparsification loss with quantization error. 披露的 evaluation signal 是：Evaluated on Llama-3.1-8B, Qwen2.5-7B, Qwen3-30B-A3B, and Qwen3-VL-8B, SharQ recovers 43--63% of the NVFP4-to-FP16 accuracy gap across language and vision-language tasks, and generalizes across NVFP4, HiF4, and MXFP4 formats. exact-v1 的观测边界是：Evaluated on Llama-3.1-8B, Qwen2.5-7B, Qwen3-30B-A3B, and Qwen3-VL-8B, SharQ recovers 43--63% of the NVFP4-to-FP16 accuracy gap across language and vision-language tasks, and generalizes across NVFP4, HiF4, and MXFP4 formats. 它没有证明 We introduce SharQ, a training-free inference method that bridges activation sparsity and FP4 quantization through an online sparse--dense decomposition. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26587:start -->
Primary identity `arXiv:2606.26587v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26587:end -->
<!-- review:SF-2026-ARXIV-2606-26587:end -->

<!-- review:SF-2026-ARXIV-2606-26590:start -->
### 2606.26590 — Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform

**问题与旧路径。** Security misconfigurations in Terraform Infrastructure-as-Code are a growing risk in cloud deployments, and large language models are increasingly used as automated repair agents. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform 的 exact-v1 机制为：This paper presents TerraProbe, a five-layer oracle framework for evaluating LLM-assisted Terraform security repair. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26590v1 — §TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform Security Repair; §2.5 Evaluation Frameworks in Empirical Software Engineering; §3 Study Design and Evaluation Protocol`；Evaluation=`arXiv:2606.26590v1 — §2.5 Evaluation Frameworks in Empirical Software Engineering; §3 Study Design and Evaluation Protocol; §3.9 Statistical Analysis Methods`；counterevidence=`arXiv:2606.26590v1 — §3.11 Threat Model; §7 Discussion; §8 Threats to Validity`。exact-v1 的观测边界是：Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. 它没有证明 This paper presents TerraProbe, a five-layer oracle framework for evaluating LLM-assisted Terraform security repair. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Security misconfigurations in Terraform Infrastructure-as-Code are a growing risk in cloud deployments, and large language models are increasingly used as automated repair agents. 披露的 evaluation signal 是：Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. exact-v1 的观测边界是：Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. 它没有证明 This paper presents TerraProbe, a five-layer oracle framework for evaluating LLM-assisted Terraform security repair. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26590:start -->
Primary identity `arXiv:2606.26590v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26590:end -->
<!-- review:SF-2026-ARXIV-2606-26590:end -->

<!-- review:SF-2026-ARXIV-2606-26607:start -->
### 2606.26607 — Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch

**问题与旧路径。** Moving those owner-changed slices is the sole irreducible cost, and modern high-bandwidth GPU interconnects make it fast enough to do between decode steps without draining in-flight requests. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch 的 exact-v1 机制为：We present Moebius, a serving system that switches between EP and TP at runtime without restarting the engine or dropping in-flight requests. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。 唯一 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26607v1 — §4 System Design; §Appendix B End-to-End Training Projection`；Evaluation=`arXiv:2606.26607v1 — §6 Evaluation; §6.1 Experimental Setup`；counterevidence=`arXiv:2606.26607v1 — §2.2 Real World Workloads Cross the Boundary; §8 Discussion; §9 Conclusion`。exact-v1 的观测边界是：Each switch completes in 215-434 ms, and Moebius holds both layouts resident with only 2.4% memory overhead. 它没有证明 We present Moebius, a serving system that switches between EP and TP at runtime without restarting the engine or dropping in-flight requests. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Moving those owner-changed slices is the sole irreducible cost, and modern high-bandwidth GPU interconnects make it fast enough to do between decode steps without draining in-flight requests. 披露的 evaluation signal 是：Each switch completes in 215-434 ms, and Moebius holds both layouts resident with only 2.4% memory overhead. exact-v1 的观测边界是：Each switch completes in 215-434 ms, and Moebius holds both layouts resident with only 2.4% memory overhead. 它没有证明 We present Moebius, a serving system that switches between EP and TP at runtime without restarting the engine or dropping in-flight requests. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26607:start -->
Primary identity `arXiv:2606.26607v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26607:end -->
<!-- review:SF-2026-ARXIV-2606-26607:end -->

<!-- review:SF-2026-ARXIV-2606-26631:start -->
### 2606.26631 — Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning

**问题与旧路径。** However, we identify a critical failure mode of this strategy: cached visual keys are already bound to their original positional context. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning 的 exact-v1 机制为：To this end, we propose Position Rebinding Cache Reuse (PRCR), a cache-level framework for replay-free visual revisiting. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26631v1 — §3 Method`；Evaluation=`arXiv:2606.26631v1 — §4 Experiment; §4.1 Experimental Settings; §Test Benchmarks.`；counterevidence=`arXiv:2606.26631v1 — §6 Conclusion; §7 Limitations and Future Work`。exact-v1 的观测边界是：Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. 它没有证明 To this end, we propose Position Rebinding Cache Reuse (PRCR), a cache-level framework for replay-free visual revisiting. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, we identify a critical failure mode of this strategy: cached visual keys are already bound to their original positional context. 披露的 evaluation signal 是：Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. exact-v1 的观测边界是：Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. 它没有证明 To this end, we propose Position Rebinding Cache Reuse (PRCR), a cache-level framework for replay-free visual revisiting. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26631:start -->
Primary identity `arXiv:2606.26631v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26631:end -->
<!-- review:SF-2026-ARXIV-2606-26631:end -->

<!-- review:SF-2026-ARXIV-2606-26633:start -->
### 2606.26633 — Simulating Unified Tensor Resharding in heterogeneous AI systems

**问题与旧路径。** However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Simulating Unified Tensor Resharding in heterogeneous AI systems 的 exact-v1 机制为：In this paper, we present Xsim, a heterogeneity-aware simulator for distributed LLM training. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26633v1 — §Simulating Unified Tensor Resharding in heterogeneous AI systems; §2.1. Emergent Challenges with Heterogeneity in AI Training Clusters; §2.2. Heterogeneity-aware AI Training Deployment: An Example`；Evaluation=`arXiv:2606.26633v1 — §5. Evaluation; §Appendix D Additional Evaluation Results`；counterevidence=`arXiv:2606.26633v1 — §7. Conclusion`。exact-v1 的观测边界是：However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous. 它没有证明 In this paper, we present Xsim, a heterogeneity-aware simulator for distributed LLM training. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous. 披露的 evaluation signal 是：However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous. exact-v1 的观测边界是：However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous. 它没有证明 In this paper, we present Xsim, a heterogeneity-aware simulator for distributed LLM training. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26633:start -->
Primary identity `arXiv:2606.26633v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26633:end -->
<!-- review:SF-2026-ARXIV-2606-26633:end -->

<!-- review:SF-2026-ARXIV-2606-26649:start -->
### 2606.26649 — Autoformalization of Agent Instructions into Policy-as-Code

**问题与旧路径。** Agent safety in high-stakes domains requires formal policy enforcement, but most existing approaches either rely on probabilistic guardrails (fine-tuned classifiers, prompt-based steering) that offer no formal guarantees, or on hand-coded symbolic enforcement that does not scale to the breadth of real policy specifications. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Autoformalization of Agent Instructions into Policy-as-Code 的 exact-v1 机制为：We present an autoformalization pipeline that translates agent prompts, MCP tool descriptions, and natural language policy documents into formally verified policies using an LLM-based generator-critic loop. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26649v1 — §2 Approach`；Evaluation=`arXiv:2606.26649v1 — §3 Evaluation`；counterevidence=`arXiv:2606.26649v1 — §4 Discussion`。exact-v1 的观测边界是：The resulting policies are written in the Cedar Policy Language. 它没有证明 We present an autoformalization pipeline that translates agent prompts, MCP tool descriptions, and natural language policy documents into formally verified policies using an LLM-based generator-critic loop. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Agent safety in high-stakes domains requires formal policy enforcement, but most existing approaches either rely on probabilistic guardrails (fine-tuned classifiers, prompt-based steering) that offer no formal guarantees, or on hand-coded symbolic enforcement that does not scale to the breadth of real policy specifications. 披露的 evaluation signal 是：The resulting policies are written in the Cedar Policy Language. exact-v1 的观测边界是：The resulting policies are written in the Cedar Policy Language. 它没有证明 We present an autoformalization pipeline that translates agent prompts, MCP tool descriptions, and natural language policy documents into formally verified policies using an LLM-based generator-critic loop. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26649:start -->
Primary identity `arXiv:2606.26649v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26649:end -->
<!-- review:SF-2026-ARXIV-2606-26649:end -->

<!-- review:SF-2026-ARXIV-2606-26664:start -->
### 2606.26664 — TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems

**问题与旧路径。** Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems 的 exact-v1 机制为：We propose TGHE (Template-based Graph Homomorphic Encryption), an ego-centric framework that resolves this by exploiting a template phenomenon: local computation trees in transaction graphs converge into a small set of structural shapes. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26664v1 — §TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems; §III System Model and Problem; §IV Proposed Method`；Evaluation=`arXiv:2606.26664v1 — §V Experimental Evaluation; §V-A Experimental Setup`；counterevidence=`arXiv:2606.26664v1 — §VI Conclusion`。exact-v1 的观测边界是：Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. 它没有证明 We propose TGHE (Template-based Graph Homomorphic Encryption), an ego-centric framework that resolves this by exploiting a template phenomenon: local computation trees in transaction graphs converge into a small set of structural shapes. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. 披露的 evaluation signal 是：Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. exact-v1 的观测边界是：Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. 它没有证明 We propose TGHE (Template-based Graph Homomorphic Encryption), an ego-centric framework that resolves this by exploiting a template phenomenon: local computation trees in transaction graphs converge into a small set of structural shapes. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26664:start -->
Primary identity `arXiv:2606.26664v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26664:end -->
<!-- review:SF-2026-ARXIV-2606-26664:end -->

<!-- review:SF-2026-ARXIV-2606-26666:start -->
### 2606.26666 — PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs

**问题与旧路径。** Autoregressive large language model (LLM) serving is increasingly limited by key-value (KV) cache movement rather than dense matrix multiplication. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs 的 exact-v1 机制为：We present PersistentKV, a native block-table decode attention engine and page-aware scheduling study for grouped-query attention (GQA). 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26666v1 — §3 Methodology`；Evaluation=`arXiv:2606.26666v1 — §4 Experiments; §4.1 Experimental Setup; §4.3 Main Serving Results`；counterevidence=`arXiv:2606.26666v1 — §5 Discussion; §5.1 Threats to Validity; §6 Conclusion`。exact-v1 的观测边界是：Modern paged-attention systems reduce fragmentation, and mature kernels like FlashInfer provide highly optimized decode attention. 它没有证明 We present PersistentKV, a native block-table decode attention engine and page-aware scheduling study for grouped-query attention (GQA). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Autoregressive large language model (LLM) serving is increasingly limited by key-value (KV) cache movement rather than dense matrix multiplication. 披露的 evaluation signal 是：Modern paged-attention systems reduce fragmentation, and mature kernels like FlashInfer provide highly optimized decode attention. exact-v1 的观测边界是：Modern paged-attention systems reduce fragmentation, and mature kernels like FlashInfer provide highly optimized decode attention. 它没有证明 We present PersistentKV, a native block-table decode attention engine and page-aware scheduling study for grouped-query attention (GQA). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26666:start -->
Primary identity `arXiv:2606.26666v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26666:end -->
<!-- review:SF-2026-ARXIV-2606-26666:end -->

<!-- review:SF-2026-ARXIV-2606-26669:start -->
### 2606.26669 — SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills

**问题与旧路径。** Agents often repeatedly solve similar task instances from scratch, leading to unnecessary reasoning cost and long execution traces. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills 的 exact-v1 机制为：Based on this view, we introduce SkillDisCo, a distillation-and-compilation framework that distills reusable PFSM subgraphs from successful traces and compiles them into callable, executable, and verifiable procedural skills. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 唯一 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26669v1 — §3 The Skill-DisCo Framework; §3.1 Framework Overview`；Evaluation=`arXiv:2606.26669v1 — §4 Experiments; §4.1 Experimental Setup; §Appendix A Full Results: Token Usage and Inference Cost`；counterevidence=`arXiv:2606.26669v1 — §6 Conclusion; §Limitations`。exact-v1 的观测边界是：Experiments on ALFWorld and WebArena show that SkillDisCo improves success rates and reduces agent turns across benchmarks and model scales, demonstrating the benefits of representing shared experience as reusable execution structures. 它没有证明 Based on this view, we introduce SkillDisCo, a distillation-and-compilation framework that distills reusable PFSM subgraphs from successful traces and compiles them into callable, executable, and verifiable procedural skills. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Agents often repeatedly solve similar task instances from scratch, leading to unnecessary reasoning cost and long execution traces. 披露的 evaluation signal 是：Experiments on ALFWorld and WebArena show that SkillDisCo improves success rates and reduces agent turns across benchmarks and model scales, demonstrating the benefits of representing shared experience as reusable execution structures. exact-v1 的观测边界是：Experiments on ALFWorld and WebArena show that SkillDisCo improves success rates and reduces agent turns across benchmarks and model scales, demonstrating the benefits of representing shared experience as reusable execution structures. 它没有证明 Based on this view, we introduce SkillDisCo, a distillation-and-compilation framework that distills reusable PFSM subgraphs from successful traces and compiles them into callable, executable, and verifiable procedural skills. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26669:start -->
Primary identity `arXiv:2606.26669v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26669:end -->
<!-- review:SF-2026-ARXIV-2606-26669:end -->

<!-- review:SF-2026-ARXIV-2606-26686:start -->
### 2606.26686 — Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation

**问题与旧路径。** However, CoT also makes the guard heavy and slow, because the model must generate many tokens before it decides. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation 的 exact-v1 机制为：This design follows a common belief that step-by-step reasoning improves a decision. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26686v1 — §Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation`；Evaluation=`arXiv:2606.26686v1 — §4 Experimental Setup`；counterevidence=`arXiv:2606.26686v1 — §7 Discussion and Limitations; §8 Conclusion`。exact-v1 的观测边界是：This design follows a common belief that step-by-step reasoning improves a decision. 它没有证明 This design follows a common belief that step-by-step reasoning improves a decision. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, CoT also makes the guard heavy and slow, because the model must generate many tokens before it decides. 披露的 evaluation signal 是：This design follows a common belief that step-by-step reasoning improves a decision. exact-v1 的观测边界是：This design follows a common belief that step-by-step reasoning improves a decision. 它没有证明 This design follows a common belief that step-by-step reasoning improves a decision. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26686:start -->
Primary identity `arXiv:2606.26686v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26686:end -->
<!-- review:SF-2026-ARXIV-2606-26686:end -->

<!-- review:SF-2026-ARXIV-2606-26721:start -->
### 2606.26721 — Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration

**问题与旧路径。** AI coding agents are changing the bottleneck in software collaboration: code is increasingly cheap, while understanding intent, negotiating scope, and governing long-term project responsibility remain costly. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration 的 exact-v1 机制为：This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26721v1 — §6. Prototype Architecture: A Collaboration Gateway`；Evaluation=`arXiv:2606.26721v1 — §8. Evaluation Agenda`；counterevidence=`arXiv:2606.26721v1 — §3.3. The Trust Boundary; §9. Risks and Limitations; §10. Discussion`。exact-v1 的观测边界是：We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. 它没有证明 This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：AI coding agents are changing the bottleneck in software collaboration: code is increasingly cheap, while understanding intent, negotiating scope, and governing long-term project responsibility remain costly. 披露的 evaluation signal 是：We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. exact-v1 的观测边界是：We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. 它没有证明 This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26721:start -->
Primary identity `arXiv:2606.26721v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26721:end -->
<!-- review:SF-2026-ARXIV-2606-26721:end -->

<!-- review:SF-2026-ARXIV-2606-26744:start -->
### 2606.26744 — HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction

**问题与旧路径。** To resolve this architectural mismatch, we propose two dedicated, model-aligned optimizations for HC residual streams. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction 的 exact-v1 机制为：We present HyperDFlash, a block-parallel speculative decoding framework tailored to DeepSeek-V4's Hyper-Connections (HC). 因此 把 draft/verify/bypass 路由、质量门槛、成本和 schema-critical fallback 共同验收。 唯一 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26744v1 — §2 Method`；Evaluation=`arXiv:2606.26744v1 — §3 Experiments; §3.2 Benchmarks; §3.5 Main Results`；counterevidence=`arXiv:2606.26744v1 — §5 Conclusion; §Limitations`。exact-v1 的观测边界是：Second, we replace the heavy generic linear compressor with a lightweight gated residual reducer, whose parameters are directly inherited from the target model's built-in hc_head module. 它没有证明 We present HyperDFlash, a block-parallel speculative decoding framework tailored to DeepSeek-V4's Hyper-Connections (HC). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：To resolve this architectural mismatch, we propose two dedicated, model-aligned optimizations for HC residual streams. 披露的 evaluation signal 是：Second, we replace the heavy generic linear compressor with a lightweight gated residual reducer, whose parameters are directly inherited from the target model's built-in hc_head module. exact-v1 的观测边界是：Second, we replace the heavy generic linear compressor with a lightweight gated residual reducer, whose parameters are directly inherited from the target model's built-in hc_head module. 它没有证明 We present HyperDFlash, a block-parallel speculative decoding framework tailored to DeepSeek-V4's Hyper-Connections (HC). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26744:start -->
Primary identity `arXiv:2606.26744v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26744:end -->
<!-- review:SF-2026-ARXIV-2606-26744:end -->

<!-- review:SF-2026-ARXIV-2606-26753:start -->
### 2606.26753 — ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification

**问题与旧路径。** On a synthetic multi-hop validity benchmark the gate reaches 90.12% +/- 1.73 accuracy; through a real-data feedback loop that mines failure patterns but trains on synthetic pairs only, the verifier transfers to Memora role binding with zero target-side labels, reaching 98.8% +/- 0.9 group-all-correct. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification 的 exact-v1 机制为：The core mechanism is a dual-evidence gate that conditions a relation judgment on the specific target proposition, scoring a (target, source) pair through the product of a MiniLM slot head and a DeBERTa-v3 slot head and gating it by conservative event/operation evidence. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26753v1 — §Agent memory systems.; §5.5 Architecture freeze: head merge and the load-bearing spine; §6 Training the Verifier`；Evaluation=`arXiv:2606.26753v1 — §The temporal-window negative result.; §7 Experimental Protocol`；counterevidence=`arXiv:2606.26753v1 — §15 Boundary Findings; §17 Discussion; §17.1 Limitations`。exact-v1 的观测边界是：This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842). 它没有证明 The core mechanism is a dual-evidence gate that conditions a relation judgment on the specific target proposition, scoring a (target, source) pair through the product of a MiniLM slot head and a DeBERTa-v3 slot head and gating it by conservative event/operation evidence. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：On a synthetic multi-hop validity benchmark the gate reaches 90.12% +/- 1.73 accuracy; through a real-data feedback loop that mines failure patterns but trains on synthetic pairs only, the verifier transfers to Memora role binding with zero target-side labels, reaching 98.8% +/- 0.9 group-all-correct. 披露的 evaluation signal 是：This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842). exact-v1 的观测边界是：This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842). 它没有证明 The core mechanism is a dual-evidence gate that conditions a relation judgment on the specific target proposition, scoring a (target, source) pair through the product of a MiniLM slot head and a DeBERTa-v3 slot head and gating it by conservative event/operation evidence. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26753:start -->
Primary identity `arXiv:2606.26753v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26753:end -->
<!-- review:SF-2026-ARXIV-2606-26753:end -->

<!-- review:SF-2026-ARXIV-2606-26758:start -->
### 2606.26758 — EGG: An Expert-Guided Agent Framework for Kernel Generation

**问题与旧路径。** High-performance GPU kernels are critical for reducing the exponentially growing computational costs of large language models (LLMs), but their development heavily relies on manual tuning by domain experts. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** EGG: An Expert-Guided Agent Framework for Kernel Generation 的 exact-v1 机制为：We propose EGG, an Expert-Guided Agent Framework for Kernel Generation, which incorporates expert optimization principles to guide LLMs' decisions. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26758v1 — §EGG: An Expert-Guided Agent Framework for Kernel Generation; §3 Method; §3.2.1 Algorithmic Structure Design`；Evaluation=`arXiv:2606.26758v1 — §4 Experiments; §4.1 Experimental Setup; §Appendix A Additional Hardware and LLM Results`；counterevidence=`arXiv:2606.26758v1 — §5 Conclusion; §Appendix G Limitations`。exact-v1 的观测边界是：While recent advances in LLM-based approaches show promise for automating kernel generation, they still struggle to achieve both correctness and high performance. 它没有证明 We propose EGG, an Expert-Guided Agent Framework for Kernel Generation, which incorporates expert optimization principles to guide LLMs' decisions. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：High-performance GPU kernels are critical for reducing the exponentially growing computational costs of large language models (LLMs), but their development heavily relies on manual tuning by domain experts. 披露的 evaluation signal 是：While recent advances in LLM-based approaches show promise for automating kernel generation, they still struggle to achieve both correctness and high performance. exact-v1 的观测边界是：While recent advances in LLM-based approaches show promise for automating kernel generation, they still struggle to achieve both correctness and high performance. 它没有证明 We propose EGG, an Expert-Guided Agent Framework for Kernel Generation, which incorporates expert optimization principles to guide LLMs' decisions. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26758:start -->
Primary identity `arXiv:2606.26758v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26758:end -->
<!-- review:SF-2026-ARXIV-2606-26758:end -->

<!-- review:SF-2026-ARXIV-2606-26762:start -->
### 2606.26762 — ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory

**问题与旧路径。** A key challenge is delayed query: decisive cues may appear briefly, yet many subsequent updates occur before the query arrives, increasing the risk that those cues are evicted or diluted under bounded memory. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory 的 exact-v1 机制为：We propose ProtoKV, a constant-footprint SVU memory that represents far history as a fixed-capacity summary state rather than retaining token instances. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26762v1 — §2.2 Bounded-Memory SVU and Prior Approaches; §4.7 System Validation; §Appendix A ProtoKV Method Details`；Evaluation=`arXiv:2606.26762v1 — §2 Background and Problem Setup; §4 Experiments; §4.1 Experimental Setup`；counterevidence=`arXiv:2606.26762v1 — §6 Conclusion`。exact-v1 的观测边界是：Under matched budgets and comparable query-time cost, ProtoKV improves accuracy by up to 12.5 points over token-retention baselines on SVU benchmarks in the long-delay regime, with gains that grow as query delay increases. 它没有证明 We propose ProtoKV, a constant-footprint SVU memory that represents far history as a fixed-capacity summary state rather than retaining token instances. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A key challenge is delayed query: decisive cues may appear briefly, yet many subsequent updates occur before the query arrives, increasing the risk that those cues are evicted or diluted under bounded memory. 披露的 evaluation signal 是：Under matched budgets and comparable query-time cost, ProtoKV improves accuracy by up to 12.5 points over token-retention baselines on SVU benchmarks in the long-delay regime, with gains that grow as query delay increases. exact-v1 的观测边界是：Under matched budgets and comparable query-time cost, ProtoKV improves accuracy by up to 12.5 points over token-retention baselines on SVU benchmarks in the long-delay regime, with gains that grow as query delay increases. 它没有证明 We propose ProtoKV, a constant-footprint SVU memory that represents far history as a fixed-capacity summary state rather than retaining token instances. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26762:start -->
Primary identity `arXiv:2606.26762v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26762:end -->
<!-- review:SF-2026-ARXIV-2606-26762:end -->

<!-- review:SF-2026-ARXIV-2606-26790:start -->
### 2606.26790 — OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning

**问题与旧路径。** On-policy self-distillation offers dense token-level supervision, yet existing skill-conditioned variants often rely on external skill memories or retrieved privileged context, which are costly to maintain and can be mismatched with the state distribution induced by the current policy in multi-turn interaction. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning 的 exact-v1 机制为：We propose \textbf{OPID} (\textbf{O}n-\textbf{P}olicy Sk\textbf{i}ll \textbf{D}istillation), a framework that extracts skill supervision directly from completed on-policy trajectories. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26790v1 — §3 Methods; §Training-inference boundary.; §OPID remains competitive with strong hybrid methods.`；Evaluation=`arXiv:2606.26790v1 — §4 Experiment; §4.1 Experimental Setting; §Benchmarks.`；counterevidence=`arXiv:2606.26790v1 — §Training-inference boundary.; §5 Conclusion; §Appendix E Additional Discussion`。exact-v1 的观测边界是：The resulting log-probability shift yields a token-level self-distillation advantage, which is combined with the outcome advantage for policy optimization. 它没有证明 We propose \textbf{OPID} (\textbf{O}n-\textbf{P}olicy Sk\textbf{i}ll \textbf{D}istillation), a framework that extracts skill supervision directly from completed on-policy trajectories. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：On-policy self-distillation offers dense token-level supervision, yet existing skill-conditioned variants often rely on external skill memories or retrieved privileged context, which are costly to maintain and can be mismatched with the state distribution induced by the current policy in multi-turn interaction. 披露的 evaluation signal 是：The resulting log-probability shift yields a token-level self-distillation advantage, which is combined with the outcome advantage for policy optimization. exact-v1 的观测边界是：The resulting log-probability shift yields a token-level self-distillation advantage, which is combined with the outcome advantage for policy optimization. 它没有证明 We propose \textbf{OPID} (\textbf{O}n-\textbf{P}olicy Sk\textbf{i}ll \textbf{D}istillation), a framework that extracts skill supervision directly from completed on-policy trajectories. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26790:start -->
Primary identity `arXiv:2606.26790v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26790:end -->
<!-- review:SF-2026-ARXIV-2606-26790:end -->

<!-- review:SF-2026-ARXIV-2606-26793:start -->
### 2606.26793 — MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG

**问题与旧路径。** Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG 的 exact-v1 机制为：We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26793v1 — §Attacks on RAG systems.; §III Method; §III-B Dual-Phase Architecture`；Evaluation=`arXiv:2606.26793v1 — §III-E B4 Decision-Only Evaluation; §IV Experiments; §Benchmark.`；counterevidence=`arXiv:2606.26793v1 — §III-A Threat Surfaces; §VI Discussion; §Limitations and scope.`。exact-v1 的观测边界是：We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces. 它没有证明 We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. 披露的 evaluation signal 是：We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces. exact-v1 的观测边界是：We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces. 它没有证明 We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26793:start -->
Primary identity `arXiv:2606.26793v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26793:end -->
<!-- review:SF-2026-ARXIV-2606-26793:end -->

<!-- review:SF-2026-ARXIV-2606-26806:start -->
### 2606.26806 — Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents

**问题与旧路径。** We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents 的 exact-v1 机制为：We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26806v1 — §3 Method`；Evaluation=`arXiv:2606.26806v1 — §5 Main Result: The Depth Flip`；counterevidence=`arXiv:2606.26806v1 — §7 Boundary Diagnostic: Memora; §9 Scope and Limitations; §10 Conclusion`。exact-v1 的观测边界是：We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. 它没有证明 We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 披露的 evaluation signal 是：We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. exact-v1 的观测边界是：We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. 它没有证明 We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26806:start -->
Primary identity `arXiv:2606.26806v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26806:end -->
<!-- review:SF-2026-ARXIV-2606-26806:end -->

<!-- review:SF-2026-ARXIV-2606-26836:start -->
### 2606.26836 — The Capability Frontier: Benchmarks Miss 82% of Model Performance

**问题与旧路径。** To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Capability Frontier: Benchmarks Miss 82% of Model Performance 的 exact-v1 机制为：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26836v1 — §4 Oracle Bias and Debiasing Methods; §4.3 Debiasing Methods; §4.3.1 Method 1: Extrapolation`；Evaluation=`arXiv:2606.26836v1 — §The Capability Frontier: Benchmarks Miss 82% of Model Performance; §5 Experimental Setup; §Benchmarks.`；counterevidence=`arXiv:2606.26836v1 — §7 Limitations; §8 Conclusion`。exact-v1 的观测边界是：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 它没有证明 To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 披露的 evaluation signal 是：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). exact-v1 的观测边界是：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 它没有证明 To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26836:start -->
Primary identity `arXiv:2606.26836v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26836:end -->
<!-- review:SF-2026-ARXIV-2606-26836:end -->

<!-- review:SF-2026-ARXIV-2606-26859:start -->
### 2606.26859 — AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems

**问题与旧路径。** Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems 的 exact-v1 机制为：We present AgentX, a production-deployed multi-agent system that fundamentally restructures this production function. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26859v1 — §AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems; §3 Multi-Agent Design Framework; §4.3.2 System KB`；Evaluation=`arXiv:2606.26859v1 — §4.3.1 Experiment KB; §4.3.3 Data Analysis; §6 Evaluation Agent`；counterevidence=`arXiv:2606.26859v1 — §5.1.5 Failure Modes; §5.2.3 Robust execution under platform failures; §7.3 Discussion`。exact-v1 的观测边界是：Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. 它没有证明 We present AgentX, a production-deployed multi-agent system that fundamentally restructures this production function. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. 披露的 evaluation signal 是：Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. exact-v1 的观测边界是：Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. 它没有证明 We present AgentX, a production-deployed multi-agent system that fundamentally restructures this production function. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26859:start -->
Primary identity `arXiv:2606.26859v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26859:end -->
<!-- review:SF-2026-ARXIV-2606-26859:end -->

<!-- review:SF-2026-ARXIV-2606-26875:start -->
### 2606.26875 — Information-Aware KV Cache Compression for Long Reasoning

**问题与旧路径。** While attention effectively captures contextual relevance, it overlooks complementary information-theoretic signals related to predictive uncertainty and token informativeness. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Information-Aware KV Cache Compression for Long Reasoning 的 exact-v1 机制为：Based on the observation, we propose \textbf{InfoKV}, an entropy-aware KV cache compression framework that incorporates information-theoretic signals. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26875v1 — §3 Methodology`；Evaluation=`arXiv:2606.26875v1 — §4 Experiments; §4.1 Setup; §5 Analysis`；counterevidence=`arXiv:2606.26875v1 — §6 Conclusion; §Limitations`。exact-v1 的观测边界是：Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. 它没有证明 Based on the observation, we propose \textbf{InfoKV}, an entropy-aware KV cache compression framework that incorporates information-theoretic signals. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：While attention effectively captures contextual relevance, it overlooks complementary information-theoretic signals related to predictive uncertainty and token informativeness. 披露的 evaluation signal 是：Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. exact-v1 的观测边界是：Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. 它没有证明 Based on the observation, we propose \textbf{InfoKV}, an entropy-aware KV cache compression framework that incorporates information-theoretic signals. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26875:start -->
Primary identity `arXiv:2606.26875v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26875:end -->
<!-- review:SF-2026-ARXIV-2606-26875:end -->

<!-- review:SF-2026-ARXIV-2606-26904:start -->
### 2606.26904 — Confidence-Aware Tool Orchestration for Robust Video Understanding

**问题与旧路径。** To address this challenge, we propose Robust-TO, an agentic video understanding framework that explicitly integrates per-frame trustworthiness into every stage of reasoning. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Confidence-Aware Tool Orchestration for Robust Video Understanding 的 exact-v1 机制为：To address this challenge, we propose Robust-TO, an agentic video understanding framework that explicitly integrates per-frame trustworthiness into every stage of reasoning. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 唯一 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26904v1 — §3.4 Confidence-Cost Trade-off Reward for GRPO Training; §Training details.; §Training data.`；Evaluation=`arXiv:2606.26904v1 — §4 Experiments; §4.1 Experiment Setup; §4.2 Main Results`；counterevidence=`arXiv:2606.26904v1 — §5 Conclusion; §Appendix A Limitations and Broader Impact; §Limitations.`。exact-v1 的观测边界是：On two video reasoning benchmarks spanning eight tasks, Robust-TO achieves 56.4% average accuracy on clean inputs, surpassing the strongest open-source baseline by 10.6%p and outperforming Gemini-2.5-Pro (46.2%). 它没有证明 To address this challenge, we propose Robust-TO, an agentic video understanding framework that explicitly integrates per-frame trustworthiness into every stage of reasoning. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：To address this challenge, we propose Robust-TO, an agentic video understanding framework that explicitly integrates per-frame trustworthiness into every stage of reasoning. 披露的 evaluation signal 是：On two video reasoning benchmarks spanning eight tasks, Robust-TO achieves 56.4% average accuracy on clean inputs, surpassing the strongest open-source baseline by 10.6%p and outperforming Gemini-2.5-Pro (46.2%). exact-v1 的观测边界是：On two video reasoning benchmarks spanning eight tasks, Robust-TO achieves 56.4% average accuracy on clean inputs, surpassing the strongest open-source baseline by 10.6%p and outperforming Gemini-2.5-Pro (46.2%). 它没有证明 To address this challenge, we propose Robust-TO, an agentic video understanding framework that explicitly integrates per-frame trustworthiness into every stage of reasoning. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26904:start -->
Primary identity `arXiv:2606.26904v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26904:end -->
<!-- review:SF-2026-ARXIV-2606-26904:end -->

<!-- review:SF-2026-ARXIV-2606-26917:start -->
### 2606.26917 — GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning

**问题与旧路径。** We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning 的 exact-v1 机制为：We propose geoalign, a lightweight plug-in for rollout curation in iterative policy optimization. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26917v1 — §3.3 Design Principles; §B.3 Training Details; §Framework and Infrastructure.`；Evaluation=`arXiv:2606.26917v1 — §5 Experiment; §5.1 Experimental Setup; §5.4 Analysis and Ablation Studies`；counterevidence=`arXiv:2606.26917v1 — §Theoretical Discussion.; §6 Conclusion`。exact-v1 的观测边界是：We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. 它没有证明 We propose geoalign, a lightweight plug-in for rollout curation in iterative policy optimization. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. 披露的 evaluation signal 是：We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. exact-v1 的观测边界是：We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. 它没有证明 We propose geoalign, a lightweight plug-in for rollout curation in iterative policy optimization. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26917:start -->
Primary identity `arXiv:2606.26917v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26917:end -->
<!-- review:SF-2026-ARXIV-2606-26917:end -->

<!-- review:SF-2026-ARXIV-2606-26918:start -->
### 2606.26918 — Diagnosing Task Insensitivity in Language Agents

**问题与旧路径。** We identify a key source of this failure as task insensitivity: when faced with similar but distinct tasks, models might apply patterns learned during training and fail to solve the task at hand. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Diagnosing Task Insensitivity in Language Agents 的 exact-v1 机制为：To mitigate this problem, we propose Task-Perturbed NLL Optimization, a lightweight contrastive regularizer that explicitly encourages action dependence on the task instruction. 因此 把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state。 唯一 owner 为 `AGENT-PLANNING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26918v1 — §3 Diagnostics: Task Insensitivity in Agentic Training; §3.2 Training-Time Dynamics Associated with Overfitting; §4 Observed Attention Drift During Training`；Evaluation=`arXiv:2606.26918v1 — §6 Experiments; §6.1 Experimental Setup; §6.2 Main Results`；counterevidence=`arXiv:2606.26918v1 — §7 Conclusion; §Limitations`。exact-v1 的观测边界是：We show that models often continue with actions aligned with the original task even when the instruction is semantically corrupted and cannot be directly answered. 它没有证明 To mitigate this problem, we propose Task-Perturbed NLL Optimization, a lightweight contrastive regularizer that explicitly encourages action dependence on the task instruction. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We identify a key source of this failure as task insensitivity: when faced with similar but distinct tasks, models might apply patterns learned during training and fail to solve the task at hand. 披露的 evaluation signal 是：We show that models often continue with actions aligned with the original task even when the instruction is semantically corrupted and cannot be directly answered. exact-v1 的观测边界是：We show that models often continue with actions aligned with the original task even when the instruction is semantically corrupted and cannot be directly answered. 它没有证明 To mitigate this problem, we propose Task-Perturbed NLL Optimization, a lightweight contrastive regularizer that explicitly encourages action dependence on the task instruction. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26918:start -->
Primary identity `arXiv:2606.26918v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26918:end -->
<!-- review:SF-2026-ARXIV-2606-26918:end -->

<!-- review:SF-2026-ARXIV-2606-26924:start -->
### 2606.26924 — A Deterministic Control Plane for LLM Coding Agents

**问题与旧路径。** Rel(AI)Build treats agent definitions as a managed supply chain (SHA-256 content addressing, HMAC-stamped lockfiles, hash-chained audit logs); enforces tiered permissions and attack-derived blocklists before LLM invocation; gates feature work through a phase state machine with requirement-to-file-to-test traceability; compiles a single canonical definition to seven IDE targets; and detects prompt drift via Jaccard similarity. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** A Deterministic Control Plane for LLM Coding Agents 的 exact-v1 机制为：We propose a deterministic control plane above the harness that maps one-to-one to these gaps. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26924v1 — §2.2 Orchestration frameworks and Autonomous Agents; §3. System Architecture; §Lifecycle design rationale`；Evaluation=`arXiv:2606.26924v1 — §6.2 Conformance results; §7.2 Results`；counterevidence=`arXiv:2606.26924v1 — §Trust boundary: cooperative trace linkage; §5. Threat Model; §7.4 Limitations of the study`。exact-v1 的观测边界是：Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration. 它没有证明 We propose a deterministic control plane above the harness that maps one-to-one to these gaps. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Rel(AI)Build treats agent definitions as a managed supply chain (SHA-256 content addressing, HMAC-stamped lockfiles, hash-chained audit logs); enforces tiered permissions and attack-derived blocklists before LLM invocation; gates feature work through a phase state machine with requirement-to-file-to-test traceability; compiles a single canonical definition to seven IDE targets; and detects prompt drift via Jaccard similarity. 披露的 evaluation signal 是：Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration. exact-v1 的观测边界是：Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration. 它没有证明 We propose a deterministic control plane above the harness that maps one-to-one to these gaps. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26924:start -->
Primary identity `arXiv:2606.26924v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26924:end -->
<!-- review:SF-2026-ARXIV-2606-26924:end -->

<!-- review:SF-2026-ARXIV-2606-26933:start -->
### 2606.26933 — Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities

**问题与旧路径。** AI-assisted vulnerability discovery has proven effective for bug classes like memory safety, where instrumentation confirms memory violations and efficiently filters false positives. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities 的 exact-v1 机制为：In this work, we present Chai, an AI-based system that discovers and validates cryptographic misuse vulnerabilities through naturally occurring signals. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26933v1 — §II System Overview; §II-B Chai’s Approach; §III System Design`；Evaluation=`arXiv:2606.26933v1 — §III-C Differential Testing: Output Analysis; §V Evaluation; §V-A Experimental Setup`；counterevidence=`arXiv:2606.26933v1 — §II-A Threat Model and Vulnerability Scope; §VII Discussion; §IX Conclusion`。exact-v1 的观测边界是：To achieve this, Chai rethinks the classical technique of differential testing by leveraging AI to 1) improve precision for detecting real security issues in libraries, and 2) repurpose commonly overlooked discrepancies as leads for tangible vulnerabilities in downstream applications. 它没有证明 In this work, we present Chai, an AI-based system that discovers and validates cryptographic misuse vulnerabilities through naturally occurring signals. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：AI-assisted vulnerability discovery has proven effective for bug classes like memory safety, where instrumentation confirms memory violations and efficiently filters false positives. 披露的 evaluation signal 是：To achieve this, Chai rethinks the classical technique of differential testing by leveraging AI to 1) improve precision for detecting real security issues in libraries, and 2) repurpose commonly overlooked discrepancies as leads for tangible vulnerabilities in downstream applications. exact-v1 的观测边界是：To achieve this, Chai rethinks the classical technique of differential testing by leveraging AI to 1) improve precision for detecting real security issues in libraries, and 2) repurpose commonly overlooked discrepancies as leads for tangible vulnerabilities in downstream applications. 它没有证明 In this work, we present Chai, an AI-based system that discovers and validates cryptographic misuse vulnerabilities through naturally occurring signals. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26933:start -->
Primary identity `arXiv:2606.26933v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26933:end -->
<!-- review:SF-2026-ARXIV-2606-26933:end -->

<!-- review:SF-2026-ARXIV-2606-26935:start -->
### 2606.26935 — Where Do CoT Training Gains Land in LLM based Agents?

**问题与旧路径。** Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Where Do CoT Training Gains Land in LLM based Agents? 的 exact-v1 机制为：We therefore ask what CoT training is actually improving: is the model getting better at changing its action through generated reasoning, or is it getting better at predicting the action directly from the prompt? 因此 把 diagnosis、candidate lesson、独立验证、promotion 与 rollback 分离。 唯一 owner 为 `AGENT-REFLECTION`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26935v1 — §Where Do CoT Training Gains Land in LLM based Agents?; §3 Setup and Diagnostic Framework; §4 Training Makes Actions More Predictable from the Prompt`；Evaluation=`arXiv:2606.26935v1 — §3 Setup and Diagnostic Framework; §4.2 Direct Prompt-vs-CoT Comparisons in Online Evaluation; §6.1 Evaluation`；counterevidence=`arXiv:2606.26935v1 — §7 Conclusion; §Limitations`。exact-v1 的观测边界是：Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. 它没有证明 We therefore ask what CoT training is actually improving: is the model getting better at changing its action through generated reasoning, or is it getting better at predicting the action directly from the prompt? 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. 披露的 evaluation signal 是：Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. exact-v1 的观测边界是：Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. 它没有证明 We therefore ask what CoT training is actually improving: is the model getting better at changing its action through generated reasoning, or is it getting better at predicting the action directly from the prompt? 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26935:start -->
Primary identity `arXiv:2606.26935v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26935:end -->
<!-- review:SF-2026-ARXIV-2606-26935:end -->

<!-- review:SF-2026-ARXIV-2606-26960:start -->
### 2606.26960 — Toward Agentic SysAdmin: Rethinking System Administration with AI Agents

**问题与旧路径。** Large Language Models (LLMs) have emerged as a promising tool to assist and partially automate these tasks, yet their systematic evaluation in networking scenarios remains an open challenge. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Toward Agentic SysAdmin: Rethinking System Administration with AI Agents 的 exact-v1 机制为：In this paper, we present NetLLMeval, a framework for automatically evaluating LLM-based systems on network administration tasks by leveraging live network emulation to derive ground truth without human intervention. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26960v1 — §Toward Agentic SysAdmin: Rethinking System Administration with AI Agents; §III NetLLMeval Architecture; §V-B Effect of Solver Architecture`；Evaluation=`arXiv:2606.26960v1 — §III-B Evaluation Pipeline; §IV Experiments; §IV-E Evaluation Metrics`；counterevidence=`arXiv:2606.26960v1 — §VI Discussion; §VII Conclusions`。exact-v1 的观测边界是：Large Language Models (LLMs) have emerged as a promising tool to assist and partially automate these tasks, yet their systematic evaluation in networking scenarios remains an open challenge. 它没有证明 In this paper, we present NetLLMeval, a framework for automatically evaluating LLM-based systems on network administration tasks by leveraging live network emulation to derive ground truth without human intervention. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Large Language Models (LLMs) have emerged as a promising tool to assist and partially automate these tasks, yet their systematic evaluation in networking scenarios remains an open challenge. 披露的 evaluation signal 是：Large Language Models (LLMs) have emerged as a promising tool to assist and partially automate these tasks, yet their systematic evaluation in networking scenarios remains an open challenge. exact-v1 的观测边界是：Large Language Models (LLMs) have emerged as a promising tool to assist and partially automate these tasks, yet their systematic evaluation in networking scenarios remains an open challenge. 它没有证明 In this paper, we present NetLLMeval, a framework for automatically evaluating LLM-based systems on network administration tasks by leveraging live network emulation to derive ground truth without human intervention. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26960:start -->
Primary identity `arXiv:2606.26960v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26960:end -->
<!-- review:SF-2026-ARXIV-2606-26960:end -->

<!-- review:SF-2026-ARXIV-2606-26978:start -->
### 2606.26978 — To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair

**问题与旧路径。** However, executions can be time-consuming and expensive, yet their impact on these agents remains underexplored. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair 的 exact-v1 机制为：This execution-based approach has become standard practice in state-of-the-art systems. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 唯一 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26978v1 — §3. Experimental Setup; §3.5. Implementation Details`；Evaluation=`arXiv:2606.26978v1 — §4. Evaluation; §4.2. RQ2: Effectiveness and Cost Analysis`；counterevidence=`arXiv:2606.26978v1 — §5.2. Threats to Validity; §7. Conclusion`。exact-v1 的观测边界是：LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. 它没有证明 This execution-based approach has become standard practice in state-of-the-art systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, executions can be time-consuming and expensive, yet their impact on these agents remains underexplored. 披露的 evaluation signal 是：LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. exact-v1 的观测边界是：LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. 它没有证明 This execution-based approach has become standard practice in state-of-the-art systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26978:start -->
Primary identity `arXiv:2606.26978v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26978:end -->
<!-- review:SF-2026-ARXIV-2606-26978:end -->

<!-- review:SF-2026-ARXIV-2606-26979:start -->
### 2606.26979 — How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring

**问题与旧路径。** Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring 的 exact-v1 机制为：This makes agent navigation stochastic and difficult to reproduce across runs. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。 唯一 owner 为 `AGENT-CONTEXT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26979v1 — §4. Approach; §4.1. System Overview`；Evaluation=`arXiv:2606.26979v1 — §3. Motivation and Problem Analysis; §4.2. CodeAnchor Tags: Static-Analysis-Based Structured Comments; §5. Evaluation`；counterevidence=`arXiv:2606.26979v1 — §6. Discussion; §7. Threats to Validity and Limitations; §9. Conclusion`。exact-v1 的观测边界是：Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  它没有证明 This makes agent navigation stochastic and difficult to reproduce across runs. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  披露的 evaluation signal 是：Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  exact-v1 的观测边界是：Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  它没有证明 This makes agent navigation stochastic and difficult to reproduce across runs. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26979:start -->
Primary identity `arXiv:2606.26979v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26979:end -->
<!-- review:SF-2026-ARXIV-2606-26979:end -->

<!-- review:SF-2026-ARXIV-2606-26990:start -->
### 2606.26990 — Decision-Aligned Evaluation of Uncertainty Quantification

**问题与旧路径。** Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Decision-Aligned Evaluation of Uncertainty Quantification 的 exact-v1 机制为：We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26990v1 — §Remark 3.3 (On the choice of our framework) .`；Evaluation=`arXiv:2606.26990v1 — §Decision-Aligned Evaluation of Uncertainty Quantification; §Common UQ evaluation metrics in ML; §5 Experiments`；counterevidence=`arXiv:2606.26990v1 — §6 Conclusion; §Limitations`。exact-v1 的观测边界是：Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. 它没有证明 We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. 披露的 evaluation signal 是：Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. exact-v1 的观测边界是：Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. 它没有证明 We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26990:start -->
Primary identity `arXiv:2606.26990v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26990:end -->
<!-- review:SF-2026-ARXIV-2606-26990:end -->

<!-- review:SF-2026-ARXIV-2606-26997:start -->
### 2606.26997 — RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning

**问题与旧路径。** However, existing synchronous on-policy GRPO (Group Relative Policy Optimization) RLVR systems finish an entire rollout before starting training, leaving the trainer GPU pool idle while rollout is still ongoing. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning 的 exact-v1 机制为：To address these challenges, we propose RolloutPipe, a post-training framework for disaggregated RLVR systems, which turns the fixed-weight rollout into a complete-group pipeline where trainable groups move to the trainer while later groups are still being generated. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.26997v1 — §RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning; §3 RolloutPipe Design; §3.2 Training-Side Complete-Group Pipelining`；Evaluation=`arXiv:2606.26997v1 — §5 Performance Evaluation; §5.1 Experimental Setup; §5.2 Results Analysis`；counterevidence=`arXiv:2606.26997v1 — §7 Conclusion`。exact-v1 的观测边界是：RolloutPipe achieves this through two techniques including complete-group pipelining (CGP) and frontier-group dispatch (FGD). 它没有证明 To address these challenges, we propose RolloutPipe, a post-training framework for disaggregated RLVR systems, which turns the fixed-weight rollout into a complete-group pipeline where trainable groups move to the trainer while later groups are still being generated. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, existing synchronous on-policy GRPO (Group Relative Policy Optimization) RLVR systems finish an entire rollout before starting training, leaving the trainer GPU pool idle while rollout is still ongoing. 披露的 evaluation signal 是：RolloutPipe achieves this through two techniques including complete-group pipelining (CGP) and frontier-group dispatch (FGD). exact-v1 的观测边界是：RolloutPipe achieves this through two techniques including complete-group pipelining (CGP) and frontier-group dispatch (FGD). 它没有证明 To address these challenges, we propose RolloutPipe, a post-training framework for disaggregated RLVR systems, which turns the fixed-weight rollout into a complete-group pipeline where trainable groups move to the trainer while later groups are still being generated. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-26997:start -->
Primary identity `arXiv:2606.26997v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-26997:end -->
<!-- review:SF-2026-ARXIV-2606-26997:end -->

<!-- review:SF-2026-ARXIV-2606-27005:start -->
### 2606.27005 — Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI)

**问题与旧路径。** This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy.The framework continuously redistributes computational budget across a population of heterogeneous AI models so that the global utility, defined jointly over predictive performance, demographic parity, cost, latency, robustness, and interpretability, remains maximised under disruption. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI) 的 exact-v1 机制为：This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy.The framework continuously redistributes computational budget across a population of heterogeneous AI models so that the global utility, defined jointly over predictive performance, demographic parity, cost, latency, robustness, and interpretability, remains maximised under disruption. 因此 把资源 utility、故障状态、placement action 与 resilience fallback 纳入控制面。 唯一 owner 为 `PLATFORM-GPU-SCHEDULER`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27005v1 — §II Methodology`；Evaluation=`arXiv:2606.27005v1 — §III Numerical Results and Discussion; §III-F Lyapunov Energy and Stability Analysis`；counterevidence=`arXiv:2606.27005v1 — §III Numerical Results and Discussion; §IV Conclusion`。exact-v1 的观测边界是：The framework is evaluated in a stress-rich discrete-time simulation that concurrently injects demographic bias shocks, gradual concept drift, and abrupt black-swan disruptions, and is compared against five established controllers including Static, Round Robin, Greedy, LinUCB, and a deep reinforcement-learning agent based on Proximal Policy Optimisation. 它没有证明 This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy.The framework continuously redistributes computational budget across a population of heterogeneous AI models so that the global utility, defined jointly over predictive performance, demographic parity, cost, latency, robustness, and interpretability, remains maximised under disruption. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy.The framework continuously redistributes computational budget across a population of heterogeneous AI models so that the global utility, defined jointly over predictive performance, demographic parity, cost, latency, robustness, and interpretability, remains maximised under disruption. 披露的 evaluation signal 是：The framework is evaluated in a stress-rich discrete-time simulation that concurrently injects demographic bias shocks, gradual concept drift, and abrupt black-swan disruptions, and is compared against five established controllers including Static, Round Robin, Greedy, LinUCB, and a deep reinforcement-learning agent based on Proximal Policy Optimisation. exact-v1 的观测边界是：The framework is evaluated in a stress-rich discrete-time simulation that concurrently injects demographic bias shocks, gradual concept drift, and abrupt black-swan disruptions, and is compared against five established controllers including Static, Round Robin, Greedy, LinUCB, and a deep reinforcement-learning agent based on Proximal Policy Optimisation. 它没有证明 This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy.The framework continuously redistributes computational budget across a population of heterogeneous AI models so that the global utility, defined jointly over predictive performance, demographic parity, cost, latency, robustness, and interpretability, remains maximised under disruption. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27005:start -->
Primary identity `arXiv:2606.27005v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27005:end -->
<!-- review:SF-2026-ARXIV-2606-27005:end -->

<!-- review:SF-2026-ARXIV-2606-27009:start -->
### 2606.27009 — Semantic Early-Stopping for Iterative LLM Agent Loops

**问题与旧路径。** Second, a judge-efficient evaluation protocol: we generate each question's full trajectory once, replay every stopping policy over the identical drafts, and cache every LLM-judge call, yielding a strictly paired efficiency-versus-quality comparison at low cost; we further separate operational tokens (charged to a policy) from evaluation tokens (a measurement instrument). 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Semantic Early-Stopping for Iterative LLM Agent Loops 的 exact-v1 机制为：This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27009v1 — §Uncertainty and orchestration in multi-LLM systems.; §IV Method`；Evaluation=`arXiv:2606.27009v1 — §RAG evaluation.; §V Theoretical Analysis; §VI A Judge-Efficient Evaluation Protocol`；counterevidence=`arXiv:2606.27009v1 — §IX Discussion; §X Limitations; §XI Conclusion and Future Work`。exact-v1 的观测边界是：This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 它没有证明 This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Second, a judge-efficient evaluation protocol: we generate each question's full trajectory once, replay every stopping policy over the identical drafts, and cache every LLM-judge call, yielding a strictly paired efficiency-versus-quality comparison at low cost; we further separate operational tokens (charged to a policy) from evaluation tokens (a measurement instrument). 披露的 evaluation signal 是：This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. exact-v1 的观测边界是：This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 它没有证明 This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27009:start -->
Primary identity `arXiv:2606.27009v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27009:end -->
<!-- review:SF-2026-ARXIV-2606-27009:end -->

<!-- review:SF-2026-ARXIV-2606-27027:start -->
### 2606.27027 — ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP

**问题与旧路径。** However, the expanding adoption of MCP has also introduced novel security concerns such as Tool Poisoning Attack (TPA), which exploit LLM-server interactions to inject malicious prompts. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP 的 exact-v1 机制为：In this paper, we introduce ShareLock, a multi-tool threshold poisoning framework that utilizes Shamir's threshold scheme to ensure exceptional stealth and fault tolerance. 因此 把 server/tool identity、描述、组合阈值、污染证据与 effect-time authorization 绑定。 唯一 owner 为 `AGENT-MCP`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27027v1 — §4. ShareLock: a Multi-Tool Threshold Poisoning Attack Framework; §D.1. System Prompt for Zero-Shot Detection`；Evaluation=`arXiv:2606.27027v1 — §5. Evaluation; §5.1. Experimental Setup; §Appendix D Experimental details of Safety Classification Task`；counterevidence=`arXiv:2606.27027v1 — §3.3. Threat Model; §6. Discussion and Limitations; §7. Conclusion`。exact-v1 的观测边界是：ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. 它没有证明 In this paper, we introduce ShareLock, a multi-tool threshold poisoning framework that utilizes Shamir's threshold scheme to ensure exceptional stealth and fault tolerance. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, the expanding adoption of MCP has also introduced novel security concerns such as Tool Poisoning Attack (TPA), which exploit LLM-server interactions to inject malicious prompts. 披露的 evaluation signal 是：ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. exact-v1 的观测边界是：ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. 它没有证明 In this paper, we introduce ShareLock, a multi-tool threshold poisoning framework that utilizes Shamir's threshold scheme to ensure exceptional stealth and fault tolerance. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27027:start -->
Primary identity `arXiv:2606.27027v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27027:end -->
<!-- review:SF-2026-ARXIV-2606-27027:end -->

<!-- review:SF-2026-ARXIV-2606-27045:start -->
### 2606.27045 — The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development

**问题与旧路径。** AI coding agents dramatically accelerate implementation speed but introduce two structural failure modes that existing spec-driven approaches do not fully solve: (1) context explosion -- the agent must reason over an entire repository at once, degrading output quality as the context window fills; and (2) silent spec-code drift -- code evolves, the specification does not, and the divergence becomes invisible until it is costly to repair. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development 的 exact-v1 机制为：We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。 唯一 owner 为 `AGENT-CONTEXT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27045v1 — §5 The Spec Growth Engine; §5.2 The Spec Graph: Nodes and Edges; §5.4 Drift Validation: Intent Graph vs. Evidence Graph`；Evaluation=`arXiv:2606.27045v1 — §6 Development Workflow; §7 Worked Example: Growing a Checkout`；counterevidence=`arXiv:2606.27045v1 — §9 Discussion; §Limitations.; §10 Conclusion`。exact-v1 的观测边界是：The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA. 它没有证明 We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：AI coding agents dramatically accelerate implementation speed but introduce two structural failure modes that existing spec-driven approaches do not fully solve: (1) context explosion -- the agent must reason over an entire repository at once, degrading output quality as the context window fills; and (2) silent spec-code drift -- code evolves, the specification does not, and the divergence becomes invisible until it is costly to repair. 披露的 evaluation signal 是：The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA. exact-v1 的观测边界是：The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA. 它没有证明 We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27045:start -->
Primary identity `arXiv:2606.27045v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27045:end -->
<!-- review:SF-2026-ARXIV-2606-27045:end -->

<!-- review:SF-2026-ARXIV-2606-27079:start -->
### 2606.27079 — ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models

**问题与旧路径。** We define a 13-category safety taxonomy covering physical interaction safety (Safe-Core), instruction-side safety (Safe-Lang), and perception-side safety (Safe-Vis), and evaluate policies under three controlled dimensions of variation -- scene structure, language command, and visual observation -- so that failure sources can be diagnosed rather than hidden in a single aggregate score. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models 的 exact-v1 机制为：To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27079v1 — §II-A Benchmarking methods for existing VLA systems; §III ForesightSafety-VLA Benchmark Design`；Evaluation=`arXiv:2606.27079v1 — §ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models; §II-A Benchmarking methods for existing VLA systems; §III ForesightSafety-VLA Benchmark Design`；counterevidence=`arXiv:2606.27079v1 — §VI Discussion and Conclusion`。exact-v1 的观测边界是：To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 它没有证明 To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We define a 13-category safety taxonomy covering physical interaction safety (Safe-Core), instruction-side safety (Safe-Lang), and perception-side safety (Safe-Vis), and evaluate policies under three controlled dimensions of variation -- scene structure, language command, and visual observation -- so that failure sources can be diagnosed rather than hidden in a single aggregate score. 披露的 evaluation signal 是：To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. exact-v1 的观测边界是：To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 它没有证明 To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27079:start -->
Primary identity `arXiv:2606.27079v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27079:end -->
<!-- review:SF-2026-ARXIV-2606-27079:end -->

<!-- review:SF-2026-ARXIV-2606-27091:start -->
### 2606.27091 — Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation

**问题与旧路径。** We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation 的 exact-v1 机制为：We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27091v1 — §4 Methods`；Evaluation=`arXiv:2606.27091v1 — §Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation; §4.3 Reusable Evasion Benchmark Construction; §5 Evaluation & Results`；counterevidence=`arXiv:2606.27091v1 — §Linear probe at the circuit boundary.; §7 Conclusion`。exact-v1 的观测边界是：LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. 它没有证明 We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 披露的 evaluation signal 是：LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. exact-v1 的观测边界是：LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. 它没有证明 We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27091:start -->
Primary identity `arXiv:2606.27091v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27091:end -->
<!-- review:SF-2026-ARXIV-2606-27091:end -->

<!-- review:SF-2026-ARXIV-2606-27136:start -->
### 2606.27136 — Joint Learning of Experiential Rules and Policies for Large Language Model Agents

**问题与旧路径。** For LLM agents in multi-step interactive environments, a key challenge is to make effective use of accumulated interaction experience. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Joint Learning of Experiential Rules and Policies for Large Language Model Agents 的 exact-v1 机制为：We present Joint Learning of Experiential Rules and Policies for LLM Agents (JERP), which updates a long-term experiential-rule pool and the policy from the same interaction trajectories. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27136v1 — §IV-A Overall Framework; §V-B Baseline Methods`；Evaluation=`arXiv:2606.27136v1 — §V Experiments; §V-A Environments and Evaluation Metrics`；counterevidence=`arXiv:2606.27136v1 — §VI Conclusion`。exact-v1 的观测边界是：The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. 它没有证明 We present Joint Learning of Experiential Rules and Policies for LLM Agents (JERP), which updates a long-term experiential-rule pool and the policy from the same interaction trajectories. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：For LLM agents in multi-step interactive environments, a key challenge is to make effective use of accumulated interaction experience. 披露的 evaluation signal 是：The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. exact-v1 的观测边界是：The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. 它没有证明 We present Joint Learning of Experiential Rules and Policies for LLM Agents (JERP), which updates a long-term experiential-rule pool and the policy from the same interaction trajectories. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27136:start -->
Primary identity `arXiv:2606.27136v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27136:end -->
<!-- review:SF-2026-ARXIV-2606-27136:end -->

<!-- review:SF-2026-ARXIV-2606-27146:start -->
### 2606.27146 — PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies

**问题与旧路径。** Long-horizon robotic manipulation is highly sensitive to physically infeasible transitions, contact-induced disturbances, and the lack of effective self-correction during execution. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies 的 exact-v1 机制为：We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27146v1 — §III METHOD; §III-C Training Pipeline`；Evaluation=`arXiv:2606.27146v1 — §IV EXPERIMENTATION; §IV-A Experimental Setup; §IV-B Main Results`；counterevidence=`arXiv:2606.27146v1 — §IV-D Analysis and Discussion; §V CONCLUSIONS`。exact-v1 的观测边界是：We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 它没有证明 We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Long-horizon robotic manipulation is highly sensitive to physically infeasible transitions, contact-induced disturbances, and the lack of effective self-correction during execution. 披露的 evaluation signal 是：We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. exact-v1 的观测边界是：We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 它没有证明 We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27146:start -->
Primary identity `arXiv:2606.27146v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27146:end -->
<!-- review:SF-2026-ARXIV-2606-27146:end -->

<!-- review:SF-2026-ARXIV-2606-27153:start -->
### 2606.27153 — DMuon: Efficient Distributed Muon Training with Near-Adam Overhead

**问题与旧路径。** Yet contemporary distributed training infrastructure built around the assumption of element-wise optimizers is poorly matched to matrix-level optimizers such as Muon, whose updates couple entire weight matrices and require costly Newton-Schulz iterations. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** DMuon: Efficient Distributed Muon Training with Near-Adam Overhead 的 exact-v1 机制为：To close this gap, we present DMuon, an open-source distributed Muon implementation that integrates into existing training pipelines as a drop-in module, with no framework-level modifications. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27153v1 — §DMuon: Efficient Distributed Muon Training with Near-Adam Overhead; §2.2 Sharded Training Abstractions; §3 System Design`；Evaluation=`arXiv:2606.27153v1 — §5 Evaluation; §Setup.`；counterevidence=`arXiv:2606.27153v1 — §5.3 Limitations; §7 Conclusion`。exact-v1 的观测边界是：Across both embodied foundation model and large language model (LLM) training workloads, DMuon achieves a 1.48x-3.01x speedup in end-to-end step time and a 6.85x-163.00x speedup in optimizer-step time, bringing per-step latency to near-AdamW levels and enabling efficient scaling in our model training. 它没有证明 To close this gap, we present DMuon, an open-source distributed Muon implementation that integrates into existing training pipelines as a drop-in module, with no framework-level modifications. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Yet contemporary distributed training infrastructure built around the assumption of element-wise optimizers is poorly matched to matrix-level optimizers such as Muon, whose updates couple entire weight matrices and require costly Newton-Schulz iterations. 披露的 evaluation signal 是：Across both embodied foundation model and large language model (LLM) training workloads, DMuon achieves a 1.48x-3.01x speedup in end-to-end step time and a 6.85x-163.00x speedup in optimizer-step time, bringing per-step latency to near-AdamW levels and enabling efficient scaling in our model training. exact-v1 的观测边界是：Across both embodied foundation model and large language model (LLM) training workloads, DMuon achieves a 1.48x-3.01x speedup in end-to-end step time and a 6.85x-163.00x speedup in optimizer-step time, bringing per-step latency to near-AdamW levels and enabling efficient scaling in our model training. 它没有证明 To close this gap, we present DMuon, an open-source distributed Muon implementation that integrates into existing training pipelines as a drop-in module, with no framework-level modifications. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27153:start -->
Primary identity `arXiv:2606.27153v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27153:end -->
<!-- review:SF-2026-ARXIV-2606-27153:end -->

<!-- review:SF-2026-ARXIV-2606-27154:start -->
### 2606.27154 — OpenRCA 2.0: From Outcome Labels to Causal Process Supervision

**问题与旧路径。** However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** OpenRCA 2.0: From Outcome Labels to Causal Process Supervision 的 exact-v1 机制为：To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 因此 把事件 identity、因果链、verification evidence 与诊断结论分离。 唯一 owner 为 `PLATFORM-TRACE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27154v1 — §Appendix B Benchmark Systems and Topology; §B.1 Systems Overview; §F.1 Agent Evaluation Framework`；Evaluation=`arXiv:2606.27154v1 — §2.1 Setup: Forward Verification from a Known Intervention; §3 Experiments; §3.1 Experimental Setup`；counterevidence=`arXiv:2606.27154v1 — §3.3 Failure Mode Characterization; §5 Assumptions and Threats to Validity; §6 Conclusion`。exact-v1 的观测边界是：To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 它没有证明 To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching. 披露的 evaluation signal 是：To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. exact-v1 的观测边界是：To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 它没有证明 To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27154:start -->
Primary identity `arXiv:2606.27154v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27154:end -->
<!-- review:SF-2026-ARXIV-2606-27154:end -->

<!-- review:SF-2026-ARXIV-2606-27188:start -->
### 2606.27188 — A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO

**问题与旧路径。** We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO 的 exact-v1 机制为：We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27188v1 — §A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO; §4 CUGA FLO System Architecture`；Evaluation=`arXiv:2606.27188v1 — §6.1.1 Property Analysis`；counterevidence=`arXiv:2606.27188v1 — §7 Discussion and Conclusion; §7.2 Limitations and Future Work`。exact-v1 的观测边界是：The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it. 它没有证明 We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 披露的 evaluation signal 是：The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it. exact-v1 的观测边界是：The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it. 它没有证明 We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27188:start -->
Primary identity `arXiv:2606.27188v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27188:end -->
<!-- review:SF-2026-ARXIV-2606-27188:end -->

<!-- review:SF-2026-ARXIV-2606-27205:start -->
### 2606.27205 — Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair

**问题与旧路径。** Large Language Models (LLMs) are powerful tools and have been increasingly adopted for complex software engineering tasks. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair 的 exact-v1 机制为：As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. 因此 把设备频率、功耗/温度估计、QoE 和模型/backend identity 联合验收。 唯一 owner 为 `INFER-GPU-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27205v1 — §III Methodology; §III-A Quantization Methods`；Evaluation=`arXiv:2606.27205v1 — §III-C Benchmarks; §III-D Evaluation Metrics; §III-E Statistical & Trade-offs Analysis`；counterevidence=`arXiv:2606.27205v1 — §V Discussion; §VI Threats to Validity; §VII Conclusion and Future Work`。exact-v1 的观测边界是：As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. 它没有证明 As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Large Language Models (LLMs) are powerful tools and have been increasingly adopted for complex software engineering tasks. 披露的 evaluation signal 是：As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. exact-v1 的观测边界是：As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. 它没有证明 As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27205:start -->
Primary identity `arXiv:2606.27205v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27205:end -->
<!-- review:SF-2026-ARXIV-2606-27205:end -->

<!-- review:SF-2026-ARXIV-2606-27210:start -->
### 2606.27210 — Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes

**问题与旧路径。** We argue that safety classifiers should model user intent as an explicit signal between the prompt and the final label. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes 的 exact-v1 机制为：To study this, we introduce AIMS, a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27210v1 — §Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes; §4 Intent-Aware Training Regimes; §Reward design.`；Evaluation=`arXiv:2606.27210v1 — §3.3 Quality and Agreement Analysis; §5 Experimental Setting; §Evaluation protocol.`；counterevidence=`arXiv:2606.27210v1 — §6 Results and Discussion; §Failure modes differ by distribution.; §8 Conclusion`。exact-v1 的观测边界是：We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. 它没有证明 To study this, we introduce AIMS, a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We argue that safety classifiers should model user intent as an explicit signal between the prompt and the final label. 披露的 evaluation signal 是：We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. exact-v1 的观测边界是：We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. 它没有证明 To study this, we introduce AIMS, a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27210:start -->
Primary identity `arXiv:2606.27210v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27210:end -->
<!-- review:SF-2026-ARXIV-2606-27210:end -->

<!-- review:SF-2026-ARXIV-2606-27226:start -->
### 2606.27226 — Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement

**问题与旧路径。** Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement 的 exact-v1 机制为：We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27226v1 — §3 Method; §Appendix C Automatic Prompt Update Algorithm`；Evaluation=`arXiv:2606.27226v1 — §Ask, Don’t Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement; §3.2 Binary Evaluation and Scoring; §4 Experimental Setup`；counterevidence=`arXiv:2606.27226v1 — §6 Discussion; §7 Conclusion; §A.2.3 Example 3: Failure Case — Relevance (SummEval)`。exact-v1 的观测边界是：Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. 它没有证明 We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. 披露的 evaluation signal 是：Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. exact-v1 的观测边界是：Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. 它没有证明 We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27226:start -->
Primary identity `arXiv:2606.27226v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27226:end -->
<!-- review:SF-2026-ARXIV-2606-27226:end -->

<!-- review:SF-2026-ARXIV-2606-27242:start -->
### 2606.27242 — The Geometry of Updates: Fisher Alignment at Vocabulary Scale

**问题与旧路径。** Training-free source selection for LLM families with shared vocabularies arises in scientific string domains such as SMILES, protein, and genomic sequences, where candidate corpora share a tokenizer but differ in prediction targets. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Geometry of Updates: Fisher Alignment at Vocabulary Scale 的 exact-v1 机制为：This creates an activation-dark regime: representation-similarity metrics can be uninformative without assumptions about label-conditioned error geometry, while classical update-geometry metrics are computationally prohibitive at vocabulary scale. 因此 把模型/更新 artifact、版本、来源和可转移性证据绑定。 唯一 owner 为 `PLATFORM-MODEL-REGISTRY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27242v1 — §A.2 Which Method is Used Where; §Practical use: Proxy accuracy is architecture-dependent.; §Algorithm: Full FisherSketch.`；Evaluation=`arXiv:2606.27242v1 — §6 Experiments; §Estimator usage across experiments.; §Setup.`；counterevidence=`arXiv:2606.27242v1 — §7 Discussion; §7.1 Limitations & Broader Applicability; §8 Conclusion`。exact-v1 的观测边界是：We show that, in a shared-output head setting, representation metrics (e.g., CKA) are non-identifiable for transfer; models can share identical representations yet have orthogonal head updates. 它没有证明 This creates an activation-dark regime: representation-similarity metrics can be uninformative without assumptions about label-conditioned error geometry, while classical update-geometry metrics are computationally prohibitive at vocabulary scale. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Training-free source selection for LLM families with shared vocabularies arises in scientific string domains such as SMILES, protein, and genomic sequences, where candidate corpora share a tokenizer but differ in prediction targets. 披露的 evaluation signal 是：We show that, in a shared-output head setting, representation metrics (e.g., CKA) are non-identifiable for transfer; models can share identical representations yet have orthogonal head updates. exact-v1 的观测边界是：We show that, in a shared-output head setting, representation metrics (e.g., CKA) are non-identifiable for transfer; models can share identical representations yet have orthogonal head updates. 它没有证明 This creates an activation-dark regime: representation-similarity metrics can be uninformative without assumptions about label-conditioned error geometry, while classical update-geometry metrics are computationally prohibitive at vocabulary scale. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27242:start -->
Primary identity `arXiv:2606.27242v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27242:end -->
<!-- review:SF-2026-ARXIV-2606-27242:end -->

<!-- review:SF-2026-ARXIV-2606-27243:start -->
### 2606.27243 — NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems

**问题与旧路径。** AutoML is limited to predefined search spaces, while generic coding agents verify runnability rather than recommender-specific semantic validity. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems 的 exact-v1 机制为：We present NOVA, a verification-aware agent harness that organizes production architecture modification as multi-round search over concrete implementations within a fixed evaluation budget. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27243v1 — §NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems Thanks: ∗ Equal contribution. Thanks: † Corresponding author.; §Self-evolving recommender systems.; §Architecture state and feasible modification space.`；Evaluation=`arXiv:2606.27243v1 — §Offline and online evaluation objectives.; §5. Experiments; §5.2. Experimental Settings`；counterevidence=`arXiv:2606.27243v1 — §4.4. Silent-Failure-Aware Multi-Stage Architecture Verification; §Capability boundary.; §6. Conclusion and Future Work`。exact-v1 的观测边界是：Industrial advertising recommender systems are continually improved through architecture modifications, yet production iteration remains expert-intensive because coordinated changes to model topology, feature configuration, and interaction modules must satisfy strict interface, resource, and serving constraints. 它没有证明 We present NOVA, a verification-aware agent harness that organizes production architecture modification as multi-round search over concrete implementations within a fixed evaluation budget. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：AutoML is limited to predefined search spaces, while generic coding agents verify runnability rather than recommender-specific semantic validity. 披露的 evaluation signal 是：Industrial advertising recommender systems are continually improved through architecture modifications, yet production iteration remains expert-intensive because coordinated changes to model topology, feature configuration, and interaction modules must satisfy strict interface, resource, and serving constraints. exact-v1 的观测边界是：Industrial advertising recommender systems are continually improved through architecture modifications, yet production iteration remains expert-intensive because coordinated changes to model topology, feature configuration, and interaction modules must satisfy strict interface, resource, and serving constraints. 它没有证明 We present NOVA, a verification-aware agent harness that organizes production architecture modification as multi-round search over concrete implementations within a fixed evaluation budget. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27243:start -->
Primary identity `arXiv:2606.27243v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27243:end -->
<!-- review:SF-2026-ARXIV-2606-27243:end -->

<!-- review:SF-2026-ARXIV-2606-27251:start -->
### 2606.27251 — Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy

**问题与旧路径。** Building persistent embodied agents in unstructured environments demands unified orchestration of heterogeneous tools spanning both cyber (APIs, IoT) and physical (manipulation, navigation) domains, coupled with autonomous recovery from physical failures that inevitably arise over extended operation. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy 的 exact-v1 机制为：To this end, we present OmniAct, a framework integrating a multimodal semantic planner for skill routing across unified action spaces, an adaptive hierarchical memory with event-boundary-driven compression for sub-linear context growth, and an asynchronous visual preemption engine that closes the semantic loop during physical execution. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27251v1 — §3 Methodology: The OmniAcr Framework; §Appendix F Visual Monitor: Design and Empirical Evaluation`；Evaluation=`arXiv:2606.27251v1 — §4 Experiments; §4.1 Experimental Setup; §Appendix B Real-World Experimental Setup`；counterevidence=`arXiv:2606.27251v1 — §5 Conclusions; §Appendix A Limitations`。exact-v1 的观测边界是：Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance. 它没有证明 To this end, we present OmniAct, a framework integrating a multimodal semantic planner for skill routing across unified action spaces, an adaptive hierarchical memory with event-boundary-driven compression for sub-linear context growth, and an asynchronous visual preemption engine that closes the semantic loop during physical execution. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Building persistent embodied agents in unstructured environments demands unified orchestration of heterogeneous tools spanning both cyber (APIs, IoT) and physical (manipulation, navigation) domains, coupled with autonomous recovery from physical failures that inevitably arise over extended operation. 披露的 evaluation signal 是：Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance. exact-v1 的观测边界是：Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance. 它没有证明 To this end, we present OmniAct, a framework integrating a multimodal semantic planner for skill routing across unified action spaces, an adaptive hierarchical memory with event-boundary-driven compression for sub-linear context growth, and an asynchronous visual preemption engine that closes the semantic loop during physical execution. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27251:start -->
Primary identity `arXiv:2606.27251v1`; official exact-v1 PDF fallback; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27251:end -->
<!-- review:SF-2026-ARXIV-2606-27251:end -->

<!-- review:SF-2026-ARXIV-2606-27268:start -->
### 2606.27268 — E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation

**问题与旧路径。** However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation 的 exact-v1 机制为：However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27268v1 — §E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation; §3.1 Framework Overview; §4.1 Experiments on Different Types of Manipulation Methods`；Evaluation=`arXiv:2606.27268v1 — §4 Experiments; §4.1 Experiments on Different Types of Manipulation Methods; §4.5 Real-robot Experiments`；counterevidence=`arXiv:2606.27268v1 — §5 Conclusion and Future Work; §Appendix 0.D Limitation`。exact-v1 的观测边界是：However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. 它没有证明 However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. 披露的 evaluation signal 是：However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. exact-v1 的观测边界是：However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. 它没有证明 However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27268:start -->
Primary identity `arXiv:2606.27268v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27268:end -->
<!-- review:SF-2026-ARXIV-2606-27268:end -->

<!-- review:SF-2026-ARXIV-2606-27288:start -->
### 2606.27288 — When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models

**问题与旧路径。** Re-asking the same GPQA-Diamond questions in free-response rather than multiple-choice form reopens the tail, with beta 0.127 and a five-judge panel with kappa 0.73 to 0.92, locating co-failure in answer format rather than subject. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models 的 exact-v1 机制为：We show that their gain is capped by a quantity the field rarely reports. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。 唯一 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27288v1 — §3 Problem Formulation; §Proposition 1 (Ceiling, gain localization, and a realizability certificate) .`；Evaluation=`arXiv:2606.27288v1 — §4 Experimental Setup; §5 Results`；counterevidence=`arXiv:2606.27288v1 — §7 Limitations; §Honest limits.; §8 Conclusion`。exact-v1 的观测边界是：We show that their gain is capped by a quantity the field rarely reports. 它没有证明 We show that their gain is capped by a quantity the field rarely reports. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Re-asking the same GPQA-Diamond questions in free-response rather than multiple-choice form reopens the tail, with beta 0.127 and a five-judge panel with kappa 0.73 to 0.92, locating co-failure in answer format rather than subject. 披露的 evaluation signal 是：We show that their gain is capped by a quantity the field rarely reports. exact-v1 的观测边界是：We show that their gain is capped by a quantity the field rarely reports. 它没有证明 We show that their gain is capped by a quantity the field rarely reports. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27288:start -->
Primary identity `arXiv:2606.27288v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27288:end -->
<!-- review:SF-2026-ARXIV-2606-27288:end -->

<!-- review:SF-2026-ARXIV-2606-27326:start -->
### 2606.27326 — Hallucination in World Models is Predictable and Preventable

**问题与旧路径。** Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Hallucination in World Models is Predictable and Preventable 的 exact-v1 机制为：To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. 因此 把 world-state、rollout、hallucination detector 与真实观测 fallback 分离。 唯一 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27326v1 — §3 Training a Large Visual World Model`；Evaluation=`arXiv:2606.27326v1 — §5 Experiments; §5.1 Main results; §Appendix E Additional Results`；counterevidence=`arXiv:2606.27326v1 — §5.2 Discussion`。exact-v1 的观测边界是：Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. 它没有证明 To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. 披露的 evaluation signal 是：Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. exact-v1 的观测边界是：Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. 它没有证明 To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27326:start -->
Primary identity `arXiv:2606.27326v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27326:end -->
<!-- review:SF-2026-ARXIV-2606-27326:end -->

<!-- review:SF-2026-ARXIV-2606-27330:start -->
### 2606.27330 — Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning

**问题与旧路径。** While small open source MLLMs are cost efficient and privacy preserving compared with commercial large models, they suffer from weak planning and limited cross website generalization. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning 的 exact-v1 机制为：To address these limitations, we introduce the planning experience exploration and utilization (PEEU) method, which autonomously explores environments to discover experiences and utilizes hindsight experience to synthesize strictly aligned, high level training data. 因此 把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state。 唯一 owner 为 `AGENT-PLANNING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27330v1 — §2 Planning Experience Exploration and Utilization Method; §2.1 Method; §Exploration and training settings.`；Evaluation=`arXiv:2606.27330v1 — §2.2 Experimental Settings; §Evaluation.; §2.3 Results and Analysis`；counterevidence=`arXiv:2606.27330v1 — §5 Conclusion; §Limitations`。exact-v1 的观测边界是：Our analysis reveals that mastering low level atomic skills does not guarantee high level planning competence, while high level task training yields stronger OOD generalization. 它没有证明 To address these limitations, we introduce the planning experience exploration and utilization (PEEU) method, which autonomously explores environments to discover experiences and utilizes hindsight experience to synthesize strictly aligned, high level training data. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：While small open source MLLMs are cost efficient and privacy preserving compared with commercial large models, they suffer from weak planning and limited cross website generalization. 披露的 evaluation signal 是：Our analysis reveals that mastering low level atomic skills does not guarantee high level planning competence, while high level task training yields stronger OOD generalization. exact-v1 的观测边界是：Our analysis reveals that mastering low level atomic skills does not guarantee high level planning competence, while high level task training yields stronger OOD generalization. 它没有证明 To address these limitations, we introduce the planning experience exploration and utilization (PEEU) method, which autonomously explores environments to discover experiences and utilizes hindsight experience to synthesize strictly aligned, high level training data. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27330:start -->
Primary identity `arXiv:2606.27330v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27330:end -->
<!-- review:SF-2026-ARXIV-2606-27330:end -->

<!-- review:SF-2026-ARXIV-2606-27350:start -->
### 2606.27350 — CHIA: An open-source framework for principled, agentic AI-driven hardware/software co-design research

**问题与旧路径。** Thus far, however, applications of AI in these contexts have generally been demonstrated in isolated settings on small-scale problems, due to the difficulty of designing and deploying complex AI-infused hardware and software development workflows. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** CHIA: An open-source framework for principled, agentic AI-driven hardware/software co-design research 的 exact-v1 机制为：This paper introduces CHIA, an open-source hardware/software co-design framework for agile and principled research on the application of AI to co-design. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27350v1 — §3. The CHIA Workflow Abstraction; §4. Design; §4.3. Runtime Features`；Evaluation=`arXiv:2606.27350v1 — §5. Case Studies; §5.5. Automatically addressing GitHub issues in the CIRCT compiler in a project maintainer friendly way`；counterevidence=`arXiv:2606.27350v1 — §7. Discussion and Future Work; §8. Conclusion`。exact-v1 的观测边界是：Agentic artificial intelligence shows great promise for radically improving the pace of innovation in hardware/software co-design research across computer architecture, systems, compilers, and VLSI. 它没有证明 This paper introduces CHIA, an open-source hardware/software co-design framework for agile and principled research on the application of AI to co-design. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Thus far, however, applications of AI in these contexts have generally been demonstrated in isolated settings on small-scale problems, due to the difficulty of designing and deploying complex AI-infused hardware and software development workflows. 披露的 evaluation signal 是：Agentic artificial intelligence shows great promise for radically improving the pace of innovation in hardware/software co-design research across computer architecture, systems, compilers, and VLSI. exact-v1 的观测边界是：Agentic artificial intelligence shows great promise for radically improving the pace of innovation in hardware/software co-design research across computer architecture, systems, compilers, and VLSI. 它没有证明 This paper introduces CHIA, an open-source hardware/software co-design framework for agile and principled research on the application of AI to co-design. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27350:start -->
Primary identity `arXiv:2606.27350v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27350:end -->
<!-- review:SF-2026-ARXIV-2606-27350:end -->

<!-- review:SF-2026-ARXIV-2606-27355:start -->
### 2606.27355 — RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools

**问题与旧路径。** RouterVLA combines a split-clean prior and outcome-disjoint probes with onboarding that credits only failures the incumbent pool cannot handle. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools 的 exact-v1 机制为：We study two recurring decisions: which expert to deploy for a new condition and which candidate to add to the pool. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Training objective; §Commissioning turns a policy pool into a stronger system`；Evaluation=`arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Problem Setup; §Experimental Protocol`；counterevidence=`arXiv:2606.27355v1 — §Failure analysis: context and evidence; §Discussion; §Limitations`。exact-v1 的观测边界是：Both criteria independently converge on the same five experts, confirming that the candidates best positioned to cover the base pool's blind spots are also broadly capable. 它没有证明 We study two recurring decisions: which expert to deploy for a new condition and which candidate to add to the pool. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：RouterVLA combines a split-clean prior and outcome-disjoint probes with onboarding that credits only failures the incumbent pool cannot handle. 披露的 evaluation signal 是：Both criteria independently converge on the same five experts, confirming that the candidates best positioned to cover the base pool's blind spots are also broadly capable. exact-v1 的观测边界是：Both criteria independently converge on the same five experts, confirming that the candidates best positioned to cover the base pool's blind spots are also broadly capable. 它没有证明 We study two recurring decisions: which expert to deploy for a new condition and which candidate to add to the pool. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27355:start -->
Primary identity `arXiv:2606.27355v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27355:end -->
<!-- review:SF-2026-ARXIV-2606-27355:end -->

<!-- review:SF-2026-ARXIV-2606-27359:start -->
### 2606.27359 — When are likely answers right? On Sequence Probability and Correctness in LLMs

**问题与旧路径。** However, this relationship does not generally transfer to decoding decisions: increasing sequence probability by changing hyperparameters or methods does not reliably improve accuracy. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** When are likely answers right? On Sequence Probability and Correctness in LLMs 的 exact-v1 机制为：Therefore, their success depends on a fundamental question: when does sequence probability, that is, the conditional probability of a continuation given a prompt, actually align with correctness? 因此 把 decoding objective、handoff state、quality signal 与保守 autoregressive fallback 绑定。 唯一 owner 为 `INFER-DECODE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27359v1 — §2 Decoding Methods Maximize Sequence Probability in LLMs; §2.1 Local Decoding Methods; §2.2 Global Decoding Methods`；Evaluation=`arXiv:2606.27359v1 — §Appendix D Details on Experimental Setup; §Appendix E Additional Experiments and Analysis`；counterevidence=`arXiv:2606.27359v1 — §4 Discussion and Conclusion`。exact-v1 的观测边界是：However, this relationship does not generally transfer to decoding decisions: increasing sequence probability by changing hyperparameters or methods does not reliably improve accuracy. 它没有证明 Therefore, their success depends on a fundamental question: when does sequence probability, that is, the conditional probability of a continuation given a prompt, actually align with correctness? 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, this relationship does not generally transfer to decoding decisions: increasing sequence probability by changing hyperparameters or methods does not reliably improve accuracy. 披露的 evaluation signal 是：However, this relationship does not generally transfer to decoding decisions: increasing sequence probability by changing hyperparameters or methods does not reliably improve accuracy. exact-v1 的观测边界是：However, this relationship does not generally transfer to decoding decisions: increasing sequence probability by changing hyperparameters or methods does not reliably improve accuracy. 它没有证明 Therefore, their success depends on a fundamental question: when does sequence probability, that is, the conditional probability of a continuation given a prompt, actually align with correctness? 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27359:start -->
Primary identity `arXiv:2606.27359v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27359:end -->
<!-- review:SF-2026-ARXIV-2606-27359:end -->

<!-- review:SF-2026-ARXIV-2606-27369:start -->
### 2606.27369 — Reinforcement Learning without Ground-Truth Solutions can Improve LLMs

**问题与旧路径。** When applying group-relative RL to such continuous rewards, we identify two key challenges: \emph{scale dominance}, where uncalibrated score magnitudes across test instances distort policy updates, and \emph{frequency dominance}, where repeatedly sampled suboptimal solutions can outweigh rare but stronger candidates. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Reinforcement Learning without Ground-Truth Solutions can Improve LLMs 的 exact-v1 机制为：We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministic execution feedback as continuous-valued supervision. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27369v1 — §Reward Design and Exploration; §RLVR Algorithms; §4 Method`；Evaluation=`arXiv:2606.27369v1 — §5 Experiments; §5.1 Experimental Setup; §Evaluation benchmarks and metrics.`；counterevidence=`arXiv:2606.27369v1 — §6 Discussion: An Information-Theoretic View of Group-Relative Learning Signals; §7 Conclusion`。exact-v1 的观测边界是：We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. 它没有证明 We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministic execution feedback as continuous-valued supervision. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：When applying group-relative RL to such continuous rewards, we identify two key challenges: \emph{scale dominance}, where uncalibrated score magnitudes across test instances distort policy updates, and \emph{frequency dominance}, where repeatedly sampled suboptimal solutions can outweigh rare but stronger candidates. 披露的 evaluation signal 是：We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. exact-v1 的观测边界是：We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. 它没有证明 We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministic execution feedback as continuous-valued supervision. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27369:start -->
Primary identity `arXiv:2606.27369v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27369:end -->
<!-- review:SF-2026-ARXIV-2606-27369:end -->

<!-- review:SF-2026-ARXIV-2606-27374:start -->
### 2606.27374 — World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays

**问题与旧路径。** Finally, we analyze the factors limiting generated replay, identifying long-horizon visual degradation and action-observation inconsistency as the primary bottlenecks. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays 的 exact-v1 机制为：We build on this generative capability to propose Recurrent Generative Replay (REGEN), a continual imitation learning framework that synthesizes pseudo-replay trajectories, enabling a robot policy to rehearse previously learned tasks without storing their original human demonstrations. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27374v1 — §4 Method; §Appendix B Training Details; §B.2 Training Hyperparameters`；Evaluation=`arXiv:2606.27374v1 — §5 Experimental Results; §5.1 Implementation Details & Evaluation Metrics; §B.3 Evaluation`；counterevidence=`arXiv:2606.27374v1 — §6 Limitations of ReGen & Future Direction; §7 Conclusion`。exact-v1 的观测边界是：Experiments in both simulation and real-world manipulation settings show that REGEN reduces catastrophic forgetting by up to $50\%$ relative to sequential fine-tuning, while approaching the performance of privileged experience replay methods that require access to real replay data. 它没有证明 We build on this generative capability to propose Recurrent Generative Replay (REGEN), a continual imitation learning framework that synthesizes pseudo-replay trajectories, enabling a robot policy to rehearse previously learned tasks without storing their original human demonstrations. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Finally, we analyze the factors limiting generated replay, identifying long-horizon visual degradation and action-observation inconsistency as the primary bottlenecks. 披露的 evaluation signal 是：Experiments in both simulation and real-world manipulation settings show that REGEN reduces catastrophic forgetting by up to $50\%$ relative to sequential fine-tuning, while approaching the performance of privileged experience replay methods that require access to real replay data. exact-v1 的观测边界是：Experiments in both simulation and real-world manipulation settings show that REGEN reduces catastrophic forgetting by up to $50\%$ relative to sequential fine-tuning, while approaching the performance of privileged experience replay methods that require access to real replay data. 它没有证明 We build on this generative capability to propose Recurrent Generative Replay (REGEN), a continual imitation learning framework that synthesizes pseudo-replay trajectories, enabling a robot policy to rehearse previously learned tasks without storing their original human demonstrations. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27374:start -->
Primary identity `arXiv:2606.27374v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27374:end -->
<!-- review:SF-2026-ARXIV-2606-27374:end -->

<!-- review:SF-2026-ARXIV-2606-27375:start -->
### 2606.27375 — Scalable Behavior Cloning with Open Data, Training, and Evaluation

**问题与旧路径。** We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, offering a reliable proxy for ablating model-design and training decisions before costly real-world evaluation. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Scalable Behavior Cloning with Open Data, Training, and Evaluation 的 exact-v1 机制为：We introduce ABC, a fully open-source stack for manipulation with behavior cloning. 因此 把数据来源、行为轨迹、过滤、训练 recipe 与评估 lineage 绑定。 唯一 owner 为 `TRAIN-DATA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.27375v1 — §2 ABC-130K Dataset; §3 ABC-Models; §7 Infrastructure`；Evaluation=`arXiv:2606.27375v1 — §3.4 Offline Metrics for Policy Evaluation; §5 Real-World Capabilities; §Appendix G Evaluation Details`；counterevidence=`arXiv:2606.27375v1 — §8 Requests for Research`。exact-v1 的观测边界是：We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, offering a reliable proxy for ablating model-design and training decisions before costly real-world evaluation. 它没有证明 We introduce ABC, a fully open-source stack for manipulation with behavior cloning. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, offering a reliable proxy for ablating model-design and training decisions before costly real-world evaluation. 披露的 evaluation signal 是：We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, offering a reliable proxy for ablating model-design and training decisions before costly real-world evaluation. exact-v1 的观测边界是：We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, offering a reliable proxy for ablating model-design and training decisions before costly real-world evaluation. 它没有证明 We introduce ABC, a fully open-source stack for manipulation with behavior cloning. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-27375:start -->
Primary identity `arXiv:2606.27375v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-27375:end -->
<!-- review:SF-2026-ARXIV-2606-27375:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-26156 | Realizing a multiagent system involves implementing member agents who interact based on a protocol while making decisions in a decentralized manner. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26185 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26211 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26257 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26298 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26300 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26341 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26344 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26356 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26377 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26383 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26429 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26439 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26441 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26442 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26449 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26453 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26456 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26463 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26472 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26479 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26488 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26492 | 5,542 fault-injected training traces from 38 DL programs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | within-program versus leave-program-out balanced accuracy |
| SF-2026-ARXIV-2606-26511 | Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge — We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | MemStrata achieves this at retrieval latency (~2.1s) versus ~16-18s for LLM-reranking baselines. | We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. |
| SF-2026-ARXIV-2606-26524 | VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills — The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. | gpt-4o-2024-05-13 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. |
| SF-2026-ARXIV-2606-26529 | The inattentional gap in task conditioned AI models that omit otherwise reportable safety critical signals — AI in radiology and other safety-critical workflows is evaluated on the hazards it is told to find, yet harm arises disproportionately from hazards no one specified. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | AI in radiology and other safety-critical workflows is evaluated on the hazards it is told to find, yet harm arises disproportionately from hazards no one specified. |
| SF-2026-ARXIV-2606-26587 | SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference — Evaluated on Llama-3.1-8B, Qwen2.5-7B, Qwen3-30B-A3B, and Qwen3-VL-8B, SharQ recovers 43--63% of the NVFP4-to-FP16 accuracy gap across language and vision-language tasks, and generalizes across NVFP4, HiF4, and MXFP4 formats. | Llama-3.1-8B, Qwen, Qwen2.5-7B, Qwen3-30B-A3B, Qwen3-VL-8B, Wan2.2-T2V-A14B, Wang | Not Disclosed | A.2.6 Conversion from BF16 to HiF4 Low-bit floating-point formats and semi-structured sparsity are increasingly supported by modern accelerators, yet combining them for LLM activation compression remains challenging: activations contain input-dependent outliers that dominate block scales in FP4 quantization, and directly applying N:M sparsity masks discards moderate values, coupling sparsification loss with quantization error. We introduce SharQ, a training-free inference method that bridges activation sparsity and FP4 quantization through an online sparse–dense decomposition. For each activation tensor, SharQ ge | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On an RTX 5090, SharQ delivers 2.2--2.4$\times$ latency reduction over FP16 and 1.2--1.4$\times$ throughput improvement over FP8 in language model serving, and up to 1.58$\times$ speedup on Wan2.2-T2V-A14B video generation when combined with SageAttention. | Evaluated on Llama-3.1-8B, Qwen2.5-7B, Qwen3-30B-A3B, and Qwen3-VL-8B, SharQ recovers 43--63% of the NVFP4-to-FP16 accuracy gap across language and vision-language tasks, and generalizes across NVFP4, HiF4, and MXFP4 formats. |
| SF-2026-ARXIV-2606-26590 | Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform — Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. | Claude 3, GPT-4, GPT-4o, gemini-2.5-flash-lite | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. |
| SF-2026-ARXIV-2606-26607 | Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch — Each switch completes in 215-434 ms, and Moebius holds both layouts resident with only 2.4% memory overhead. | Qwen3-235B, Qwen3-235B-A22B | Not Disclosed | Hardware and model. We evaluate Moebius on a single node of 8 NVIDIA H200 GPUs (141 GB HBM each), fully connected over NVLink, serving the instruction-tuned Qwen3-235B-A22B model in BF16 (235B parameters, 94 layers, 64 query / 4 KV heads). Table 2 details the per-GPU runtime state of Figure 13 , the footprint outside weights, KV cache, and the dual-mode buffer. The 2.8 GB dual-mode buffer itself divides into 1.7 GB of TP-mode qkv_proj and o_proj shards held alongside the full EP copies and 1.1 GB for one spare physical layer that stages the per-layer transfer. TP ’s larger activation workspaces and CUDA graphs fo | Not Disclosed | Not Disclosed | Not Disclosed | Mixture-of-Experts (MoE) architectures scale large language models (LLMs) to hundreds of billions of parameters. Serving a single MoE model requires multiple GPUs operating in parallel, typically through tensor parallelism (TP) or expert parallelism (EP). The optimal choice depends on the number of in-flight requests: TP is faster at low concurrency, whereas EP wins at high concurrency. Production workloads cross this boundary continually: online serving sees bursty arrivals that subside into quiet periods, and reinforcement-learning rollouts begin as a high-concurrency burst that decays into a long tail of strag | Moving those owner-changed slices is the sole irreducible cost, and modern high-bandwidth GPU interconnects make it fast enough to do between decode steps without draining in-flight requests. | Each switch completes in 215-434 ms, and Moebius holds both layouts resident with only 2.4% memory overhead. |
| SF-2026-ARXIV-2606-26631 | Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning — Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. | Qwen3-VL-8B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. |
| SF-2026-ARXIV-2606-26633 | Simulating Unified Tensor Resharding in heterogeneous AI systems — However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous. | Llama, Wang | Not Disclosed | Challenge 1: Load Balancing Across Asymmetric Hardware. Uniform workload partitioning is the default strategy in frameworks like Megatron-LM ( Shoeybi et al., 2019 ) and DeepSpeed ( Rasley et al., 2020 ) . Training frameworks assign equal portions of model layers, tensor slices, or data batches to all devices regardless of their compute capabilities. In heterogeneous clusters, this approach causes severe performance degradation due to compute imbalance. That is, high-performance GPUs (e.g., H100 with 204.9 FP16 TFLOPS) complete their assigned work significantly faster than lower-tier GPUs (e.g., A100 with 77.97 F | Not Disclosed | Not Disclosed | Not Disclosed | The execution engine parses the workload trace and schedules compute events via a global priority-based event scheduler that supports concurrent per-device execution. For collective operations (e.g., AllReduce), it dynamically instantiates communication channels using the planning-phase configuration and invokes the selected network backend (NS-3 or htsim) through a send/recv interface. | Not Disclosed | However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous. |
| SF-2026-ARXIV-2606-26649 | Autoformalization of Agent Instructions into Policy-as-Code — The resulting policies are written in the Cedar Policy Language. | Claude Opus, GPT-5.2, Gemini | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The resulting policies are written in the Cedar Policy Language. |
| SF-2026-ARXIV-2606-26664 | TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems — Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. | Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. | Existing homomorphic encryption (HE)-based GNN systems adopt a graph-centric paradigm that couples per-query cost to global graph size, limiting evaluations to at most ~20k nodes and making them incompatible with dynamic, large-scale financial graphs. |
| SF-2026-ARXIV-2606-26666 | PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs — Modern paged-attention systems reduce fragmentation, and mature kernels like FlashInfer provide highly optimized decode attention. | Not Disclosed | Not Disclosed | Autoregressive large language model (LLM) serving is increasingly limited by key-value (KV) cache movement rather than dense matrix multiplication. Modern paged-attention systems reduce KV-cache fragmentation and mature kernels such as FlashInfer provide highly optimized native-paged decode attention. However, the best single-kernel implementation is not always the best serving schedule: low-active long-context decode can under-utilize commodity GPUs, while mixed sequence lengths introduce a tension between many exact-length launches and coarse padded batches. We present PersistentKV , a native block-table decode | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | With cost-model constants fixed on calibration traces, five held-out seeds improve mean wall decode-token throughput by 1.04x to 1.08x on B8 bimodal, uniform, and Zipf-like workloads, and by 1.40x on a B1 bucketed trace. | Modern paged-attention systems reduce fragmentation, and mature kernels like FlashInfer provide highly optimized decode attention. |
| SF-2026-ARXIV-2606-26669 | SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills — Experiments on ALFWorld and WebArena show that SkillDisCo improves success rates and reduces agent turns across benchmarks and model scales, demonstrating the benefits of representing shared experience as reusable execution structures. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Agents often repeatedly solve similar task instances from scratch, leading to unnecessary reasoning cost and long execution traces. | Experiments on ALFWorld and WebArena show that SkillDisCo improves success rates and reduces agent turns across benchmarks and model scales, demonstrating the benefits of representing shared experience as reusable execution structures. |
| SF-2026-ARXIV-2606-26686 | Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation — This design follows a common belief that step-by-step reasoning improves a decision. | Wang | Not Disclosed | Corpus and protocol. We use the public GuardReasoner training corpus of 127,465 conversation-level examples, which carries both the three-part verdict label and a reasoning trace per example. This lets us define a clean ablation on one corpus. The with-CoT condition trains on (reasoning + + verdict), and the label-only condition trains on the verdict target alone, with the reasoning removed. The data, the optimizer, and the schedule are identical, and only the supervision target changes. We train every setting ourselves. All settings share the data, a one-epoch schedule, an effective batch of 16, AdamW with cosin | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This design follows a common belief that step-by-step reasoning improves a decision. |
| SF-2026-ARXIV-2606-26721 | Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration — We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Recent ecosystem signals from public code collaboration platforms make this tension visible. One major platform provider has published practical guidance for reviewing agent-generated PRs ( GitHub, 2026a ) and added repository-level controls to disable PRs, restrict PR creation to collaborators, and limit concurrent PRs from users without write access ( GitHub, 2026c ; GitHub, 2026b ) . Individual projects are also adjusting their contribution policies. For example, one public coding-agent project’s contribution guide requires issue linkage and design review for certain kinds of work, and asks contributors to exp | We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. | We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. |
| SF-2026-ARXIV-2606-26744 | HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction — Second, we replace the heavy generic linear compressor with a lightweight gated residual reducer, whose parameters are directly inherited from the target model's built-in hc_head module. | DeepSeek-V4, DeepSeek-V4-Flash, DeepSeek-specific, deepseekai2026v4flash | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Extensive experiments across math reasoning, code synthesis, and conversational benchmarks demonstrate that HyperDFlash consistently outperforms both the native MTP baseline and vanilla DFlash adaptation, achieving substantial gains in average accepted draft length and decoding speedup. | Second, we replace the heavy generic linear compressor with a lightweight gated residual reducer, whose parameters are directly inherited from the target model's built-in hc_head module. |
| SF-2026-ARXIV-2606-26753 | ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification — This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842). |
| SF-2026-ARXIV-2606-26758 | EGG: An Expert-Guided Agent Framework for Kernel Generation — While recent advances in LLM-based approaches show promise for automating kernel generation, they still struggle to achieve both correctness and high performance. | Wang, WangHaojie | Not Disclosed | We compare our generated kernels against the original hand-written Triton implementations. EGG achieves substantial speedups: 1.24 × \times for Flash Attention, 1.63 × \times for RoPE Embedding, and 1.08 × \times for INT8 Dequant MatMul. These results demonstrate that expert manual tuning does not always achieve optimal performance for complex operators. EGG effectively harnesses LLMs’ exploration capabilities to discover implementations that surpass hand-tuned production kernels, validating the practical value of our approach. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Experiments on KernelBench and real-world workloads show that EGG achieves a 2.13x average speedup over PyTorch, outperforming existing agent-based and RL-based approaches. | While recent advances in LLM-based approaches show promise for automating kernel generation, they still struggle to achieve both correctness and high performance. |
| SF-2026-ARXIV-2606-26762 | ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory — Under matched budgets and comparable query-time cost, ProtoKV improves accuracy by up to 12.5 points over token-retention baselines on SVU benchmarks in the long-delay regime, with gains that grow as query delay increases. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Streaming video understanding (SVU) must answer queries that arrive asynchronously while visual tokens stream continuously under strict GPU-memory and query-time latency budgets. | Under matched budgets and comparable query-time cost, ProtoKV improves accuracy by up to 12.5 points over token-retention baselines on SVU benchmarks in the long-delay regime, with gains that grow as query delay increases. |
| SF-2026-ARXIV-2606-26790 | OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning — The resulting log-probability shift yields a token-level self-distillation advantage, which is combined with the outcome advantage for policy optimization. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The resulting log-probability shift yields a token-level self-distillation advantage, which is combined with the outcome advantage for policy optimization. |
| SF-2026-ARXIV-2606-26793 | MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG — We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces. | gpt-4o-mini, gpt-5-mini, gpt-5-nano | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across four attack surfaces on a multimodal agentic RAG target, MIRROR attains 76% ASR on image poisoning compared with 52% for baselines, 97% ASR on orchestrator attacks at half the query cost, and the lowest cross-surface variance (coefficient of variation 0.47). | We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces. |
| SF-2026-ARXIV-2606-26806 | Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents — We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. | GPT-2, Mistral-7B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Neural memory and test-time fast weights. Recent architectures explicitly learn memory at test time. Titans introduces a neural long-term memory module that complements attention ( Behrouz et al. 2025 ) , while In-Place TTT updates selected fast weights during inference ( Feng et al. 2026 ) . Concurrent parametric-memory work uses online LoRA fast weights for self-evolving agents ( Ren et al. 2026 ) , studies document LoRA under KV-cache compression ( Zuo et al. 2026 ) , and quantifies exact LoRA memory laws ( Xu et al. 2026 ) . Other recent agent-memory work studies retrieval-side context validity ( Yang et al. | Not Disclosed | We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. |
| SF-2026-ARXIV-2606-26836 | The Capability Frontier: Benchmarks Miss 82% of Model Performance — To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). | To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). |
| SF-2026-ARXIV-2606-26859 | AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems — Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. Innovation therefore scales linearly with headcount rather than compounding with evidence, compute, and accumulated experimental knowledge. We present AgentX, a production-deployed multi-agent system that fundamentally restructures this production function. A | Not Disclosed | Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. |
| SF-2026-ARXIV-2606-26875 | Information-Aware KV Cache Compression for Long Reasoning — Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. | DeepSeek-R1, Llama-3.1, Llama-3.1-8B-Instruct, Llama-3.2, Llama-3.2-3B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. |
| SF-2026-ARXIV-2606-26904 | Confidence-Aware Tool Orchestration for Robust Video Understanding — On two video reasoning benchmarks spanning eight tasks, Robust-TO achieves 56.4% average accuracy on clean inputs, surpassing the strongest open-source baseline by 10.6%p and outperforming Gemini-2.5-Pro (46.2%). | GPT-4o, Gemini-2.5-Pro, Qwen2.5-VL-7B, Qwen3-VL-7B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We also provide a case study Tab. 7 with the query “Which vehicle ran the red light at the intersection, and what was its license plate number?” . The source video has 24 frames under three concurrent corruptions: rainy evening with oncoming headlight glare ( f 4 f_{4} , f 5 f_{5} , f 22 f_{22} ), windshield wiper motion blur ( f 7 f_{7} - f 9 f_{9} , f 15 f_{15} - f 17 f_{17} ), and a truck partially occluding the intersection ( f 10 f_{10} - f 13 f_{13} ). | During reasoning, these calibrated scores guide evidence weighting in a three-tier synthesis process (high/medium/low) and define a confidence-cost GRPO reward that jointly optimizes correctness, evidence reliability, and efficiency. | On two video reasoning benchmarks spanning eight tasks, Robust-TO achieves 56.4% average accuracy on clean inputs, surpassing the strongest open-source baseline by 10.6%p and outperforming Gemini-2.5-Pro (46.2%). |
| SF-2026-ARXIV-2606-26917 | GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning — We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. | Qwen-MAX, Qwen3-1.7B, Qwen3-4B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. |
| SF-2026-ARXIV-2606-26918 | Diagnosing Task Insensitivity in Language Agents — We show that models often continue with actions aligned with the original task even when the instruction is semantically corrupted and cannot be directly answered. | Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We show that models often continue with actions aligned with the original task even when the instruction is semantically corrupted and cannot be directly answered. |
| SF-2026-ARXIV-2606-26924 | A Deterministic Control Plane for LLM Coding Agents — Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration. | Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Miller [2006] Mark S. Miller. Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control . PhD thesis, Johns Hopkins University, 2006. | Not Disclosed | Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration. |
| SF-2026-ARXIV-2606-26933 | Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities — To achieve this, Chai rethinks the classical technique of differential testing by leveraging AI to 1) improve precision for detecting real security issues in libraries, and 2) repurpose commonly overlooked discrepancies as leads for tangible vulnerabilities in downstream applications. | Claude Opus, GPT-5.5, Gemini, gpt-5.5-2026-04-23 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To achieve this, Chai rethinks the classical technique of differential testing by leveraging AI to 1) improve precision for detecting real security issues in libraries, and 2) repurpose commonly overlooked discrepancies as leads for tangible vulnerabilities in downstream applications. |
| SF-2026-ARXIV-2606-26935 | Where Do CoT Training Gains Land in LLM based Agents? — Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. | Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. |
| SF-2026-ARXIV-2606-26960 | Toward Agentic SysAdmin: Rethinking System Administration with AI Agents — Large Language Models (LLMs) have emerged as a promising tool to assist and partially automate these tasks, yet their systematic evaluation in networking scenarios remains an open challenge. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Evaluation of LLMs in networking and operations. Systematic evaluation of LLMs on operational tasks is an active and rapidly evolving area. Our earlier study [ 6 ] provided preliminary evidence that general-purpose LLMs can assist network administration but relied on manual validation and a limited question set. NetConfEval [ 7 ] benchmarks LLMs on network configuration tasks against static reference outputs, without closed-loop interaction with a live environment and without agent-based pipelines. The most closely related concurrent works are NetArena [ 9 ] and NIKA [ 10 ] , both of which use network emulators t | Not Disclosed | Large Language Models (LLMs) have emerged as a promising tool to assist and partially automate these tasks, yet their systematic evaluation in networking scenarios remains an open challenge. |
| SF-2026-ARXIV-2606-26978 | To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair — LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. | Claude, Claude Code, Claude Sonnet, DeepSeek-V3.2, GPT-4, GPT-4o, GPT-5, GPT-5.2, GPT-5.2-xhigh, Gemini-3-Pro, Qwen2.5-Coder-32B, Qwen2.5-Coder-32B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We record interaction traces and compute several metrics to characterize agent behavior and outcomes. For execution behavior, we measure execution frequency as the average number of test executions per task, timing distribution as the percentage of executions occurring in each conversation stage (Early: 0–33%, Middle: 33–66%, Late: 66–100%), and execution outcome as the success or failure rate of test executions. For effectiveness and cost, the primary outcome is resolve rate , which indicates the proportion of instances where the generated patch passes the official SWE-bench evaluation. We measure token consumpt | Second, we evaluate 3,000 end-to-end repair attempts across 200 SWE-bench instances and three agents (Claude Code, Codex, and the open-source OpenCode) under four execution paradigms, which allows for a fine-grained comparison of performance and cost. | LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. |
| SF-2026-ARXIV-2606-26979 | How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring — Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24, | Claude Code, Gemini | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24, roughly halve run-to-run variance, and improve single-run re | Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24, |
| SF-2026-ARXIV-2606-26990 | Decision-Aligned Evaluation of Uncertainty Quantification — Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. |
| SF-2026-ARXIV-2606-26997 | RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning — RolloutPipe achieves this through two techniques including complete-group pipelining (CGP) and frontier-group dispatch (FGD). | Qwen3, Qwen3-1.7B, Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Because / ℱ / = F w /\mathcal{F}/=F_{w} bounds the number of groups served concurrently, FGD concentrates rollout capacity on the earliest groups, so the first U U groups finish earlier and more steadily, thus lowering t first ( U ) t_{\text{first}}^{(U)} in Eq. ( 2 ). Example. F w = 2 F_{w}=2 , groups 1–6 arrived, ℱ = { 1 , 2 } \mathcal{F}=\{1,2\} . After group 1 completes its K K requests, ℱ \mathcal{F} updates to { 2 , 3 } \{2,3\} . For the training side, when / Q ( r ) / ≥ U = 2 /Q^{(r)}/\geq U=2 , the trainer starts while groups 3–6 are still in rollout. Rollout node. This node handles frontier admission and | Asynchronous RL pipelines overlap the two stages, but at the cost of training on stale data. | RolloutPipe achieves this through two techniques including complete-group pipelining (CGP) and frontier-group dispatch (FGD). |
| SF-2026-ARXIV-2606-27005 | Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI) — The framework is evaluated in a stress-rich discrete-time simulation that concurrently injects demographic bias shocks, gradual concept drift, and abrupt black-swan disruptions, and is compared against five established controllers including Static, Round Robin, Greedy, LinUCB, and a deep reinforcement-learning agent based on Proximal Policy Optimisation. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Modern AI systems are increasingly deployed under non-stationary computational, demographic, and operational conditions in which static resource allocation strategies degrade both predictive performance and human-centric properties such as fairness and explainability. This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy. The framework continuously redistributes computational budget across a populat | This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy.The framework continuously redistributes computational budget across a population of heterogeneous AI models so that the global utility, defined jointly over predictive performance, demographic parity, cost, latency, robustness, and interpretability, remains maximised under disruption. | The framework is evaluated in a stress-rich discrete-time simulation that concurrently injects demographic bias shocks, gradual concept drift, and abrupt black-swan disruptions, and is compared against five established controllers including Static, Round Robin, Greedy, LinUCB, and a deep reinforcement-learning agent based on Proximal Policy Optimisation. |
| SF-2026-ARXIV-2606-27009 | Semantic Early-Stopping for Iterative LLM Agent Loops — This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Second, a judge-efficient evaluation protocol: we generate each question's full trajectory once, replay every stopping policy over the identical drafts, and cache every LLM-judge call, yielding a strictly paired efficiency-versus-quality comparison at low cost; we further separate operational tokens (charged to a policy) from evaluation tokens (a measurement instrument). | This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. |
| SF-2026-ARXIV-2606-27027 | ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP — ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. | DeepSeek-V3.1, DeepSeek-V3.2, Gemini-2.5-Flash, LLaMA, Qwen3-235B-A22B-Thinking | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. |
| SF-2026-ARXIV-2606-27045 | The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development — The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA. |
| SF-2026-ARXIV-2606-27079 | ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models — To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Beyond binary task success, ForesightSafety-VLA measures process-level risk through cumulative safety cost (CC) and risk exposure time (RET), together with a four-quadrant decomposition of safe/unsafe success and failure. | To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. |
| SF-2026-ARXIV-2606-27091 | Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation — LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. | Llama, Llama-3.1-8B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. |
| SF-2026-ARXIV-2606-27136 | Joint Learning of Experiential Rules and Policies for Large Language Model Agents — The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. |
| SF-2026-ARXIV-2606-27146 | PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies — We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. |
| SF-2026-ARXIV-2606-27153 | DMuon: Efficient Distributed Muon Training with Near-Adam Overhead — Across both embodied foundation model and large language model (LLM) training workloads, DMuon achieves a 1.48x-3.01x speedup in end-to-end step time and a 6.85x-163.00x speedup in optimizer-step time, bringing per-step latency to near-AdamW levels and enabling efficient scaling in our model training. | Not Disclosed | Not Disclosed | We adopt the Polar Express ( 2 ) coefficient set as the default for k = 5 k\!=\!5 NS steps, with the standard ( a , b , c ) (a,b,c) -quintic coefficients selectable via configuration. The choice is orthogonal to DMuon’s systems contributions. We expose it because the symmetric kernel was tuned for the matrix shapes Polar Express produces in its later steps. A fine-grained analysis of the wgrad distribution over the course of training shows that its dynamic range stays well within what fp16 can represent. We therefore run the NS iteration in fp16 rather than bf16, the two are identical in cost on the tensor cores, | Not Disclosed | Not Disclosed | Not Disclosed | We reorganize both owner-to-all broadcasts and all-to-owner reductions into a two-stage hierarchy comprising intra-node and inter-node communication. The communication schedule is effective only when concurrent collectives avoid repeatedly contending for the same communication group. We therefore use a fine-grained owner-slot layout that disperses nearby matrix communication units across GPU columns while rotating their owner nodes across consecutive groups. Figure 5 : Forward and Backward pass (a) In the forward pass, IB groups 0–8 perform inter-group broadcasts concurrently. Since these broadcasts are assigned | Vanilla Muon implementations incur more than 2x the cost of forward and backward passes. | Across both embodied foundation model and large language model (LLM) training workloads, DMuon achieves a 1.48x-3.01x speedup in end-to-end step time and a 6.85x-163.00x speedup in optimizer-step time, bringing per-step latency to near-AdamW levels and enabling efficient scaling in our model training. |
| SF-2026-ARXIV-2606-27154 | OpenRCA 2.0: From Outcome Labels to Causal Process Supervision — To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. |
| SF-2026-ARXIV-2606-27188 | A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO — The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Service tasks are executed by fixed software scripts that cannot adapt to open-ended or unstructured inputs. User tasks involve human workers who bring contextual judgment and adaptability, but introduce throughput constraints and operational variability at scale. In neither case does the process engine itself reason about the task context beyond what the process designer anticipated [ 4 ] . [13] K. D. Swenson (2010) Mastering the unpredictable: how adaptive case management will revolutionize the way that knowledge workers get things done . Meghan-Kiffer Press . Cited by: §6 . | Not Disclosed | The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it. |
| SF-2026-ARXIV-2606-27205 | Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair — As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Although quantization successfully reduces memory footprints by up to 85%, it increases both inference time and energy consumption, which we attribute to suboptimal hardware utilization. | As the number of parameters increases, results can often be improved, but this also imposes substantial memory requirements. |
| SF-2026-ARXIV-2606-27210 | Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes — We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. | Gemma-3-27B-IT | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Most notably, directly rewarding intent faithfulness with GRPO yields the strongest average performance across five external safety benchmarks, while our intent-aware models form the inference latency-F1 Pareto frontier. | We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. |
| SF-2026-ARXIV-2606-27226 | Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement — Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. | Claude Sonnet, Wang, gpt-oss-120b | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. |
| SF-2026-ARXIV-2606-27242 | The Geometry of Updates: Fisher Alignment at Vocabulary Scale — We show that, in a shared-output head setting, representation metrics (e.g., CKA) are non-identifiable for transfer; models can share identical representations yet have orthogonal head updates. | Llama-3.1-8B | Not Disclosed | Scaling and memory. At K = 128,256 K=128{,}256 , storing Γ e \Gamma_{e} requires ∼ 61 \sim 61 GiB per task, whereas FisherSketch stores a 16 16 KiB float32 per-task signature. During streaming, split-half estimation keeps six float64 accumulators per task (A/B splits for S a ​ e , S a , S e S_{ae},S_{a},S_{e} ), which is 192 192 KiB. Fixed projections fit on a single GPU by (i) storing dense Rademacher sign matrices as int8 (two m × d m{\times}d matrices for activations; 32 32 MiB at m = d = 4096 m{=}d{=}4096 ) and (ii) using an SRHT for the K K -dimensional error (about 1 1 MiB of sign-vectors/indices), implemen | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We show that, in a shared-output head setting, representation metrics (e.g., CKA) are non-identifiable for transfer; models can share identical representations yet have orthogonal head updates. |
| SF-2026-ARXIV-2606-27243 | NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems — Industrial advertising recommender systems are continually improved through architecture modifications, yet production iteration remains expert-intensive because coordinated changes to model topology, feature configuration, and interaction modules must satisfy strict interface, resource, and serving constraints. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Industrial advertising recommender systems are continually improved through architecture modifications, yet production iteration remains expert-intensive because coordinated changes to model topology, feature configuration, and interaction modules must satisfy strict interface, resource, and serving constraints. |
| SF-2026-ARXIV-2606-27251 | Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy — Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance. | Gemini-3.1-Pro | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Vision-Language-Action (VLA) models directly map visual observations and language instructions to low-level control signals. Early architectures explored various fusion strategies including feature modulation 12 ; 5 , cross-attention 14 ; 4 , and token concatenation 25 . Subsequent large-scale pre-training on diverse robotic datasets significantly improved model capabilities 16 ; 7 . Concurrently, advances in action representation such as autoregressive tokenization 23 and diffusion-based generation 3 ; 19 ; 11 , together with richer input modalities including 3D geometry 34 and tactile feedback 33 ; 8 , have fur | Not Disclosed | Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance. |
| SF-2026-ARXIV-2606-27268 | E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation — However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. |
| SF-2026-ARXIV-2606-27288 | When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models — We show that their gain is capped by a quantity the field rarely reports. | Claude Haiku, Claude Opus, Claude Sonnet, DeepSeek, GPT-5-mini, GPT-5-nano, GPT-5.1, GPT-5.5, Gemini, Llama-4-Maverick, Mistral-Large, Qwen3-235B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We show that their gain is capped by a quantity the field rarely reports. |
| SF-2026-ARXIV-2606-27326 | Hallucination in World Models is Predictable and Preventable — Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. |
| SF-2026-ARXIV-2606-27330 | Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning — Our analysis reveals that mastering low level atomic skills does not guarantee high level planning competence, while high level task training yields stronger OOD generalization. | GPT-4o, Qwen2.5-VL-32B, Qwen2.5-VL-3B-Instruct, Qwen2.5-VL-7B-Instruct, llama-factory | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | While small open source MLLMs are cost efficient and privacy preserving compared with commercial large models, they suffer from weak planning and limited cross website generalization. | Our analysis reveals that mastering low level atomic skills does not guarantee high level planning competence, while high level task training yields stronger OOD generalization. |
| SF-2026-ARXIV-2606-27350 | CHIA: An open-source framework for principled, agentic AI-driven hardware/software co-design research — Agentic artificial intelligence shows great promise for radically improving the pace of innovation in hardware/software co-design research across computer architecture, systems, compilers, and VLSI. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 3.2.1 Physical Machines and Logical Workers 4.3.1 Mapping Workers to Physical Machines Simulation: The loop then compiles a Verilator simulator from the implementation, which is used to run the user’s tests. To maximize parallelism, Verilator runs are split across three workers, two of which run on public cloud machines. Some longer benchmarks are run in FPGA-accelerated simulations using FireSim ( Karandikar et al., 2018 ) . On top of these physical machines, users specify a set of logical workers. A logical worker’s definition includes a set of resources which are virtualized representations of the hardware and | Not Disclosed | Agentic artificial intelligence shows great promise for radically improving the pace of innovation in hardware/software co-design research across computer architecture, systems, compilers, and VLSI. |
| SF-2026-ARXIV-2606-27355 | RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools — Both criteria independently converge on the same five experts, confirming that the candidates best positioned to cover the base pool's blind spots are also broadly capable. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Under an exactly cost-matched probe budget, it reaches 60.53\% held-out success, a $+1.64\pp$ gain over a semantic shortlist. | Both criteria independently converge on the same five experts, confirming that the candidates best positioned to cover the base pool's blind spots are also broadly capable. |
| SF-2026-ARXIV-2606-27359 | When are likely answers right? On Sequence Probability and Correctness in LLMs — However, this relationship does not generally transfer to decoding decisions: increasing sequence probability by changing hyperparameters or methods does not reliably improve accuracy. | Qwen2.5, Qwen3 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | However, this relationship does not generally transfer to decoding decisions: increasing sequence probability by changing hyperparameters or methods does not reliably improve accuracy. |
| SF-2026-ARXIV-2606-27369 | Reinforcement Learning without Ground-Truth Solutions can Improve LLMs — We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. | Qwen3-8B, Wang | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. |
| SF-2026-ARXIV-2606-27374 | World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays — Experiments in both simulation and real-world manipulation settings show that REGEN reduces catastrophic forgetting by up to $50\%$ relative to sequential fine-tuning, while approaching the performance of privileged experience replay methods that require access to real replay data. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Experiments in both simulation and real-world manipulation settings show that REGEN reduces catastrophic forgetting by up to $50\%$ relative to sequential fine-tuning, while approaching the performance of privileged experience replay methods that require access to real replay data. |
| SF-2026-ARXIV-2606-27375 | Scalable Behavior Cloning with Open Data, Training, and Evaluation — We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, offering a reliable proxy for ablating model-design and training decisions before costly real-world evaluation. | Not Disclosed | Not Disclosed | For ABC-VLA, we linearly warm up the learning rate for the first 1000 steps to 1 × 10 − 4 1\times 10^{-4} and keep it constant throughout training. We use the AdamW optimizer [ 18 ] with weight decay 0.01. We use gradient clipping with max gradient norm 10 and maximum gradient value 100. The model is trained with bf16 mixed precision. We train on 8 H200 nodes with batch size 24 per GPU and gradient accumulation 6, bringing the global batch size to 9216. We drop out the input proprioception with probability 0.1. We implement various optimizations to reduce the inference latency of both ABC-DiT and ABC-VLA. For the | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, offering a reliable proxy for ablating model-design and training decisions before costly real-world evaluation. |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-26156 | score_7_9; potential_books_delta | not_selected | — | — | Kiko: Programming Agents to Enact Interaction Protocols remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26156 |
| SF-2026-ARXIV-2606-26185 | score_7_9; potential_books_delta | not_selected | — | — | Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26185 |
| SF-2026-ARXIV-2606-26211 | score_7_9; potential_books_delta | not_selected | — | — | Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26211 |
| SF-2026-ARXIV-2606-26257 | score_7_9; potential_books_delta | not_selected | — | — | Dataset Usage Inference without Shadow Models or Held-out Data remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26257 |
| SF-2026-ARXIV-2606-26298 | score_7_9; potential_books_delta | not_selected | — | — | Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26298 |
| SF-2026-ARXIV-2606-26300 | score_7_9; potential_books_delta | not_selected | — | — | The Verification Horizon: No Silver Bullet for Coding Agent Rewards remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26300 |
| SF-2026-ARXIV-2606-26341 | score_7_9; potential_books_delta | not_selected | — | — | Scaling Nonlinear Optimization: Many Problems One GPU remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26341 |
| SF-2026-ARXIV-2606-26344 | score_7_9; potential_books_delta | not_selected | — | — | Axon: A Synthesizing Superoptimizer for Tensor Programs remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26344 |
| SF-2026-ARXIV-2606-26356 | score_7_9; potential_books_delta | not_selected | — | — | Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PROMPT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26356 |
| SF-2026-ARXIV-2606-26377 | score_7_9; potential_books_delta | not_selected | — | — | Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26377 |
| SF-2026-ARXIV-2606-26383 | score_7_9; potential_books_delta | not_selected | — | — | SOLAR: AI-Powered Speed-of-Light Performance Analysis remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26383 |
| SF-2026-ARXIV-2606-26429 | score_7_9; potential_books_delta | not_selected | — | — | DualEval: Joint Model-Item Calibration for Unified LLM Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26429 |
| SF-2026-ARXIV-2606-26439 | score_7_9; potential_books_delta | not_selected | — | — | TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26439 |
| SF-2026-ARXIV-2606-26441 | score_7_9; potential_books_delta | not_selected | — | — | GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26441 |
| SF-2026-ARXIV-2606-26442 | score_7_9; potential_books_delta | not_selected | — | — | AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26442 |
| SF-2026-ARXIV-2606-26449 | score_7_9; potential_books_delta | not_selected | — | — | ProvenAI: Provenance-Native Traces of Evidence in Generated Answers remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26449 |
| SF-2026-ARXIV-2606-26453 | score_7_9; potential_books_delta | not_selected | — | — | Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26453 |
| SF-2026-ARXIV-2606-26456 | score_7_9; potential_books_delta | not_selected | — | — | Towards Safety-Aware Mutation Testing for Autonomous Driving Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26456 |
| SF-2026-ARXIV-2606-26463 | score_7_9; potential_books_delta | not_selected | — | — | Finding the Time to Think: Learning Planning Budgets in Real-Time RL remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26463 |
| SF-2026-ARXIV-2606-26472 | score_7_9; potential_books_delta | not_selected | — | — | Epiphany-Aware KV Cache Eviction Without the Attention Matrix remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26472 |
| SF-2026-ARXIV-2606-26479 | score_7_9; potential_books_delta | not_selected | — | — | Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26479 |
| SF-2026-ARXIV-2606-26488 | score_7_9; potential_books_delta | not_selected | — | — | What Survives When You Compress a Recursive Reasoner for the Edge? remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26488 |
| SF-2026-ARXIV-2606-26492 | score_7_9; potential_books_delta | not_selected | — | — | Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26492 |
| SF-2026-ARXIV-2606-26511 | score_7_9; potential_books_delta | not_selected | — | — | Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26511 |
| SF-2026-ARXIV-2606-26524 | score_7_9; potential_books_delta | selected | DA-20260626-VIGIL-RUNTIME-ENFORCEMENT | — | 入选：VIGIL 把自然语言 skill specification 编译为运行时可执行约束，让 side effect 的允许/拒绝与审计 evidence 进入同一控制面。 | analysis:DA-20260626-VIGIL-RUNTIME-ENFORCEMENT |
| SF-2026-ARXIV-2606-26529 | score_7_9; potential_books_delta | not_selected | — | — | The inattentional gap in task conditioned AI models that omit otherwise reportable safety critical signals remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26529 |
| SF-2026-ARXIV-2606-26587 | score_7_9; potential_books_delta | not_selected | — | — | SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26587 |
| SF-2026-ARXIV-2606-26590 | score_7_9; potential_books_delta | not_selected | — | — | Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26590 |
| SF-2026-ARXIV-2606-26607 | score_7_9; potential_books_delta | selected | DA-20260626-MOEBIUS-RUNTIME-PARALLELISM | — | 入选：Moebius 把 expert-parallel 与 tensor-parallel 的切换提升为运行时调度动作，并把通信负载、并发阶段和切换开销绑定。 | analysis:DA-20260626-MOEBIUS-RUNTIME-PARALLELISM |
| SF-2026-ARXIV-2606-26631 | score_7_9; potential_books_delta | not_selected | — | — | Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26631 |
| SF-2026-ARXIV-2606-26633 | score_7_9; potential_books_delta | not_selected | — | — | Simulating Unified Tensor Resharding in heterogeneous AI systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26633 |
| SF-2026-ARXIV-2606-26649 | score_7_9; potential_books_delta | not_selected | — | — | Autoformalization of Agent Instructions into Policy-as-Code remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26649 |
| SF-2026-ARXIV-2606-26664 | score_7_9; potential_books_delta | not_selected | — | — | TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26664 |
| SF-2026-ARXIV-2606-26666 | score_7_9; potential_books_delta | not_selected | — | — | PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26666 |
| SF-2026-ARXIV-2606-26669 | score_7_9; potential_books_delta | not_selected | — | — | SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26669 |
| SF-2026-ARXIV-2606-26686 | score_7_9; potential_books_delta | not_selected | — | — | Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26686 |
| SF-2026-ARXIV-2606-26721 | score_7_9; potential_books_delta | not_selected | — | — | Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26721 |
| SF-2026-ARXIV-2606-26744 | score_7_9; potential_books_delta | not_selected | — | — | HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26744 |
| SF-2026-ARXIV-2606-26753 | score_7_9; potential_books_delta | not_selected | — | — | ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26753 |
| SF-2026-ARXIV-2606-26758 | score_7_9; potential_books_delta | not_selected | — | — | EGG: An Expert-Guided Agent Framework for Kernel Generation remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26758 |
| SF-2026-ARXIV-2606-26762 | score_7_9; potential_books_delta | not_selected | — | — | ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26762 |
| SF-2026-ARXIV-2606-26790 | score_7_9; potential_books_delta | not_selected | — | — | OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26790 |
| SF-2026-ARXIV-2606-26793 | score_7_9; potential_books_delta | not_selected | — | — | MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26793 |
| SF-2026-ARXIV-2606-26806 | score_7_9; potential_books_delta | not_selected | — | — | Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26806 |
| SF-2026-ARXIV-2606-26836 | score_7_9; potential_books_delta | not_selected | — | — | The Capability Frontier: Benchmarks Miss 82% of Model Performance remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26836 |
| SF-2026-ARXIV-2606-26859 | score_7_9; potential_books_delta | not_selected | — | — | AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26859 |
| SF-2026-ARXIV-2606-26875 | score_7_9; potential_books_delta | not_selected | — | — | Information-Aware KV Cache Compression for Long Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26875 |
| SF-2026-ARXIV-2606-26904 | score_7_9; potential_books_delta | not_selected | — | — | Confidence-Aware Tool Orchestration for Robust Video Understanding remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26904 |
| SF-2026-ARXIV-2606-26917 | score_7_9; potential_books_delta | not_selected | — | — | GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26917 |
| SF-2026-ARXIV-2606-26918 | score_7_9; potential_books_delta | not_selected | — | — | Diagnosing Task Insensitivity in Language Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26918 |
| SF-2026-ARXIV-2606-26924 | score_7_9; potential_books_delta | not_selected | — | — | A Deterministic Control Plane for LLM Coding Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26924 |
| SF-2026-ARXIV-2606-26933 | score_7_9; potential_books_delta | not_selected | — | — | Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26933 |
| SF-2026-ARXIV-2606-26935 | score_7_9; potential_books_delta | not_selected | — | — | Where Do CoT Training Gains Land in LLM based Agents? remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26935 |
| SF-2026-ARXIV-2606-26960 | score_7_9; potential_books_delta | not_selected | — | — | Toward Agentic SysAdmin: Rethinking System Administration with AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26960 |
| SF-2026-ARXIV-2606-26978 | score_7_9; potential_books_delta | not_selected | — | — | To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26978 |
| SF-2026-ARXIV-2606-26979 | score_7_9; potential_books_delta | not_selected | — | — | How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26979 |
| SF-2026-ARXIV-2606-26990 | score_7_9; potential_books_delta | not_selected | — | — | Decision-Aligned Evaluation of Uncertainty Quantification remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26990 |
| SF-2026-ARXIV-2606-26997 | score_7_9; potential_books_delta | not_selected | — | — | RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26997 |
| SF-2026-ARXIV-2606-27005 | score_7_9; potential_books_delta | not_selected | — | — | Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI) remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27005 |
| SF-2026-ARXIV-2606-27009 | score_7_9; potential_books_delta | not_selected | — | — | Semantic Early-Stopping for Iterative LLM Agent Loops remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27009 |
| SF-2026-ARXIV-2606-27027 | score_7_9; potential_books_delta | not_selected | — | — | ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27027 |
| SF-2026-ARXIV-2606-27045 | score_7_9; potential_books_delta | not_selected | — | — | The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27045 |
| SF-2026-ARXIV-2606-27079 | score_7_9; potential_books_delta | not_selected | — | — | ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27079 |
| SF-2026-ARXIV-2606-27091 | score_7_9; potential_books_delta | not_selected | — | — | Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27091 |
| SF-2026-ARXIV-2606-27136 | score_7_9; potential_books_delta | not_selected | — | — | Joint Learning of Experiential Rules and Policies for Large Language Model Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27136 |
| SF-2026-ARXIV-2606-27146 | score_7_9; potential_books_delta | not_selected | — | — | PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27146 |
| SF-2026-ARXIV-2606-27153 | score_7_9; potential_books_delta | not_selected | — | — | DMuon: Efficient Distributed Muon Training with Near-Adam Overhead remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27153 |
| SF-2026-ARXIV-2606-27154 | score_7_9; potential_books_delta | not_selected | — | — | OpenRCA 2.0: From Outcome Labels to Causal Process Supervision remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27154 |
| SF-2026-ARXIV-2606-27188 | score_7_9; potential_books_delta | not_selected | — | — | A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27188 |
| SF-2026-ARXIV-2606-27205 | score_7_9; potential_books_delta | not_selected | — | — | Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27205 |
| SF-2026-ARXIV-2606-27210 | score_7_9; potential_books_delta | not_selected | — | — | Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27210 |
| SF-2026-ARXIV-2606-27226 | score_7_9; potential_books_delta | not_selected | — | — | Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27226 |
| SF-2026-ARXIV-2606-27242 | score_7_9; potential_books_delta | not_selected | — | — | The Geometry of Updates: Fisher Alignment at Vocabulary Scale remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MODEL-REGISTRY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27242 |
| SF-2026-ARXIV-2606-27243 | score_7_9; potential_books_delta | not_selected | — | — | NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27243 |
| SF-2026-ARXIV-2606-27251 | score_7_9; potential_books_delta | selected | DA-20260626-OMNIACT-CLOSED-LOOP | — | 入选：OmniAct 分离 planner、hierarchical memory 与 asynchronous visual verifier，在物理失败时中断并把 evidence 交回复规规划。 | analysis:DA-20260626-OMNIACT-CLOSED-LOOP |
| SF-2026-ARXIV-2606-27268 | score_7_9; potential_books_delta | not_selected | — | — | E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27268 |
| SF-2026-ARXIV-2606-27288 | score_7_9; potential_books_delta | not_selected | — | — | When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27288 |
| SF-2026-ARXIV-2606-27326 | score_7_9; potential_books_delta | not_selected | — | — | Hallucination in World Models is Predictable and Preventable remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27326 |
| SF-2026-ARXIV-2606-27330 | score_7_9; potential_books_delta | not_selected | — | — | Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27330 |
| SF-2026-ARXIV-2606-27350 | score_7_9; potential_books_delta | not_selected | — | — | CHIA: An open-source framework for principled, agentic AI-driven hardware/software co-design research remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27350 |
| SF-2026-ARXIV-2606-27355 | score_7_9; potential_books_delta | not_selected | — | — | RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27355 |
| SF-2026-ARXIV-2606-27359 | score_7_9; potential_books_delta | not_selected | — | — | When are likely answers right? On Sequence Probability and Correctness in LLMs remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27359 |
| SF-2026-ARXIV-2606-27369 | score_7_9; potential_books_delta | not_selected | — | — | Reinforcement Learning without Ground-Truth Solutions can Improve LLMs remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27369 |
| SF-2026-ARXIV-2606-27374 | score_7_9; potential_books_delta | not_selected | — | — | World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27374 |
| SF-2026-ARXIV-2606-27375 | score_7_9; potential_books_delta | not_selected | — | — | Scalable Behavior Cloning with Open Data, Training, and Evaluation remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-27375 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-2026-ARXIV-2606-26156:start -->
Kiko: Programming Agents to Enact Interaction Protocols remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26156:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26185:start -->
Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26185:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26211:start -->
Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26211:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26257:start -->
Dataset Usage Inference without Shadow Models or Held-out Data remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26257:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26298:start -->
Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26298:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26300:start -->
The Verification Horizon: No Silver Bullet for Coding Agent Rewards remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26300:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26341:start -->
Scaling Nonlinear Optimization: Many Problems One GPU remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26341:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26344:start -->
Axon: A Synthesizing Superoptimizer for Tensor Programs remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26344:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26356:start -->
Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PROMPT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26356:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26377:start -->
Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26377:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26383:start -->
SOLAR: AI-Powered Speed-of-Light Performance Analysis remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26383:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26429:start -->
DualEval: Joint Model-Item Calibration for Unified LLM Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26429:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26439:start -->
TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26439:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26441:start -->
GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26441:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26442:start -->
AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26442:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26449:start -->
ProvenAI: Provenance-Native Traces of Evidence in Generated Answers remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26449:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26453:start -->
Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26453:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26456:start -->
Towards Safety-Aware Mutation Testing for Autonomous Driving Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26456:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26463:start -->
Finding the Time to Think: Learning Planning Budgets in Real-Time RL remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26463:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26472:start -->
Epiphany-Aware KV Cache Eviction Without the Attention Matrix remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26472:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26479:start -->
Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26479:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26488:start -->
What Survives When You Compress a Recursive Reasoner for the Edge? remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26488:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26492:start -->
Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26492:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26511:start -->
Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26511:end -->

<!-- analysis:DA-20260626-VIGIL-RUNTIME-ENFORCEMENT:start -->
### DA-20260626-VIGIL-RUNTIME-ENFORCEMENT
Agent skill 的自然语言说明不能自动成为执行安全保证；VIGIL 将 specification 变成 runtime monitor，在工具 side effect 前检查并保存 violation receipt。证据限于论文声明的 skill/workload，不证明规范本身完整或恶意依赖可被发现。
<!-- analysis:DA-20260626-VIGIL-RUNTIME-ENFORCEMENT:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26529:start -->
The inattentional gap in task conditioned AI models that omit otherwise reportable safety critical signals remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26529:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26587:start -->
SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26587:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26590:start -->
Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26590:end -->

<!-- analysis:DA-20260626-MOEBIUS-RUNTIME-PARALLELISM:start -->
### DA-20260626-MOEBIUS-RUNTIME-PARALLELISM
MoE serving 的最佳并行策略会随 prefill/decode 与并发变化；Moebius 允许 EP/TP 在运行时切换，收益来自减少阶段性通信瓶颈，代价是转换状态、切换开销与调度稳定性必须显式计量。
<!-- analysis:DA-20260626-MOEBIUS-RUNTIME-PARALLELISM:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26631:start -->
Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26631:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26633:start -->
Simulating Unified Tensor Resharding in heterogeneous AI systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26633:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26649:start -->
Autoformalization of Agent Instructions into Policy-as-Code remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26649:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26664:start -->
TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26664:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26666:start -->
PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26666:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26669:start -->
SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26669:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26686:start -->
Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26721:start -->
Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26721:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26744:start -->
HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26744:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26753:start -->
ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26753:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26758:start -->
EGG: An Expert-Guided Agent Framework for Kernel Generation remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26758:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26762:start -->
ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26762:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26790:start -->
OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26790:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26793:start -->
MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26793:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26806:start -->
Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26806:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26836:start -->
The Capability Frontier: Benchmarks Miss 82% of Model Performance remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26836:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26859:start -->
AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26859:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26875:start -->
Information-Aware KV Cache Compression for Long Reasoning remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26875:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26904:start -->
Confidence-Aware Tool Orchestration for Robust Video Understanding remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26904:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26917:start -->
GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26917:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26918:start -->
Diagnosing Task Insensitivity in Language Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26918:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26924:start -->
A Deterministic Control Plane for LLM Coding Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26924:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26933:start -->
Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26933:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26935:start -->
Where Do CoT Training Gains Land in LLM based Agents? remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-REFLECTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26935:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26960:start -->
Toward Agentic SysAdmin: Rethinking System Administration with AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26960:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26978:start -->
To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26978:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26979:start -->
How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26979:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26990:start -->
Decision-Aligned Evaluation of Uncertainty Quantification remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26990:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26997:start -->
RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26997:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27005:start -->
Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI) remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27009:start -->
Semantic Early-Stopping for Iterative LLM Agent Loops remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27009:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27027:start -->
ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MCP. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27027:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27045:start -->
The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27045:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27079:start -->
ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27079:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27091:start -->
Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27091:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27136:start -->
Joint Learning of Experiential Rules and Policies for Large Language Model Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27136:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27146:start -->
PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27146:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27153:start -->
DMuon: Efficient Distributed Muon Training with Near-Adam Overhead remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27153:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27154:start -->
OpenRCA 2.0: From Outcome Labels to Causal Process Supervision remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27154:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27188:start -->
A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27188:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27205:start -->
Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27205:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27210:start -->
Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27210:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27226:start -->
Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27226:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27242:start -->
The Geometry of Updates: Fisher Alignment at Vocabulary Scale remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MODEL-REGISTRY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27243:start -->
NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27243:end -->

<!-- analysis:DA-20260626-OMNIACT-CLOSED-LOOP:start -->
### DA-20260626-OMNIACT-CLOSED-LOOP
OmniAct 用统一 cyber-physical skill space、事件边界压缩 memory 与异步视觉抢占组成闭环；视觉 verifier 的低频采样留下 latency window，冻结 VLA skill 的能力上限仍需保守 controller 或人工接管。
<!-- analysis:DA-20260626-OMNIACT-CLOSED-LOOP:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27268:start -->
E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27268:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27288:start -->
When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27288:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27326:start -->
Hallucination in World Models is Predictable and Preventable remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27326:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27330:start -->
Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27330:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27350:start -->
CHIA: An open-source framework for principled, agentic AI-driven hardware/software co-design research remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27350:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27355:start -->
RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27355:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27359:start -->
When are likely answers right? On Sequence Probability and Correctness in LLMs remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-DECODE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27359:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27369:start -->
Reinforcement Learning without Ground-Truth Solutions can Improve LLMs remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27369:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27374:start -->
World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27374:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27375:start -->
Scalable Behavior Cloning with Open Data, Training, and Evaluation remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-27375:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-26156 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-26156 | delta:SF-2026-ARXIV-2606-26156 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26156 |
| SF-2026-ARXIV-2606-26185 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26185 | delta:SF-2026-ARXIV-2606-26185 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26185 |
| SF-2026-ARXIV-2606-26211 | AGENT-MCP | books/part-07-agent/83-mcp.md#L83 | books/part-07-agent/84-agent-platform.md#L20 | existing:SF-2026-ARXIV-2606-26211 | delta:SF-2026-ARXIV-2606-26211 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26211 |
| SF-2026-ARXIV-2606-26257 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26257 | delta:SF-2026-ARXIV-2606-26257 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26257 |
| SF-2026-ARXIV-2606-26298 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26298 | delta:SF-2026-ARXIV-2606-26298 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26298 |
| SF-2026-ARXIV-2606-26300 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26300 | delta:SF-2026-ARXIV-2606-26300 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26300 |
| SF-2026-ARXIV-2606-26341 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L141 | books/part-06-ai-infrastructure/64-volcano.md#L44 | existing:SF-2026-ARXIV-2606-26341 | delta:SF-2026-ARXIV-2606-26341 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26341 |
| SF-2026-ARXIV-2606-26344 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L630 | books/part-05-inference-system/48-speculative-decoding.md#L113 | existing:SF-2026-ARXIV-2606-26344 | delta:SF-2026-ARXIV-2606-26344 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26344 |
| SF-2026-ARXIV-2606-26356 | AGENT-PROMPT | books/part-07-agent/74-prompt.md#L46 | books/part-07-agent/75-context.md#L308 | existing:SF-2026-ARXIV-2606-26356 | delta:SF-2026-ARXIV-2606-26356 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26356 |
| SF-2026-ARXIV-2606-26377 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26377 | delta:SF-2026-ARXIV-2606-26377 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26377 |
| SF-2026-ARXIV-2606-26383 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L18 | books/part-06-ai-infrastructure/68-logging.md#L16 | existing:SF-2026-ARXIV-2606-26383 | delta:SF-2026-ARXIV-2606-26383 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26383 |
| SF-2026-ARXIV-2606-26429 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26429 | delta:SF-2026-ARXIV-2606-26429 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26429 |
| SF-2026-ARXIV-2606-26439 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-26439 | delta:SF-2026-ARXIV-2606-26439 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26439 |
| SF-2026-ARXIV-2606-26441 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-26441 | delta:SF-2026-ARXIV-2606-26441 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26441 |
| SF-2026-ARXIV-2606-26442 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L37 | existing:SF-2026-ARXIV-2606-26442 | delta:SF-2026-ARXIV-2606-26442 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26442 |
| SF-2026-ARXIV-2606-26449 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L33 | books/part-06-ai-infrastructure/68-logging.md#L66 | existing:SF-2026-ARXIV-2606-26449 | delta:SF-2026-ARXIV-2606-26449 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26449 |
| SF-2026-ARXIV-2606-26453 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L630 | books/part-05-inference-system/48-speculative-decoding.md#L113 | existing:SF-2026-ARXIV-2606-26453 | delta:SF-2026-ARXIV-2606-26453 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26453 |
| SF-2026-ARXIV-2606-26456 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26456 | delta:SF-2026-ARXIV-2606-26456 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26456 |
| SF-2026-ARXIV-2606-26463 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L140 | books/part-07-agent/80-reflection.md#L73 | existing:SF-2026-ARXIV-2606-26463 | delta:SF-2026-ARXIV-2606-26463 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26463 |
| SF-2026-ARXIV-2606-26472 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L97 | books/part-05-inference-system/44-decode.md#L31 | existing:SF-2026-ARXIV-2606-26472 | delta:SF-2026-ARXIV-2606-26472 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26472 |
| SF-2026-ARXIV-2606-26479 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26479 | delta:SF-2026-ARXIV-2606-26479 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26479 |
| SF-2026-ARXIV-2606-26488 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L186 | books/part-05-inference-system/55-pd-disaggregation.md#L409 | existing:SF-2026-ARXIV-2606-26488 | delta:SF-2026-ARXIV-2606-26488 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26488 |
| SF-2026-ARXIV-2606-26492 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26492 | delta:SF-2026-ARXIV-2606-26492 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26492 |
| SF-2026-ARXIV-2606-26511 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-26511 | delta:SF-2026-ARXIV-2606-26511 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26511 |
| SF-2026-ARXIV-2606-26524 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-26524 | delta:SF-2026-ARXIV-2606-26524 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26524 |
| SF-2026-ARXIV-2606-26590 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-26590 | delta:SF-2026-ARXIV-2606-26590 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26590 |
| SF-2026-ARXIV-2606-26607 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-26607 | delta:SF-2026-ARXIV-2606-26607 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26607 |
| SF-2026-ARXIV-2606-26631 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-26631 | delta:SF-2026-ARXIV-2606-26631 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26631 |
| SF-2026-ARXIV-2606-26649 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-26649 | delta:SF-2026-ARXIV-2606-26649 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26649 |
| SF-2026-ARXIV-2606-26721 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-26721 | delta:SF-2026-ARXIV-2606-26721 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26721 |
| SF-2026-ARXIV-2606-26753 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-26753 | delta:SF-2026-ARXIV-2606-26753 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26753 |
| SF-2026-ARXIV-2606-26793 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-26793 | delta:SF-2026-ARXIV-2606-26793 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26793 |
| SF-2026-ARXIV-2606-26806 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-26806 | delta:SF-2026-ARXIV-2606-26806 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26806 |
| SF-2026-ARXIV-2606-26836 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-26836 | delta:SF-2026-ARXIV-2606-26836 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26836 |
| SF-2026-ARXIV-2606-26875 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-26875 | delta:SF-2026-ARXIV-2606-26875 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26875 |
| SF-2026-ARXIV-2606-26924 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-26924 | delta:SF-2026-ARXIV-2606-26924 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26924 |
| SF-2026-ARXIV-2606-26935 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-26935 | delta:SF-2026-ARXIV-2606-26935 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26935 |
| SF-2026-ARXIV-2606-26979 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-26979 | delta:SF-2026-ARXIV-2606-26979 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26979 |
| SF-2026-ARXIV-2606-26990 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-26990 | delta:SF-2026-ARXIV-2606-26990 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26990 |
| SF-2026-ARXIV-2606-26997 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-26997 | delta:SF-2026-ARXIV-2606-26997 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-26997 |
| SF-2026-ARXIV-2606-27009 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-27009 | delta:SF-2026-ARXIV-2606-27009 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27009 |
| SF-2026-ARXIV-2606-27027 | AGENT-MCP | books/part-07-agent/83-mcp.md#L1 | books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-27027 | delta:SF-2026-ARXIV-2606-27027 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27027 |
| SF-2026-ARXIV-2606-27045 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-27045 | delta:SF-2026-ARXIV-2606-27045 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27045 |
| SF-2026-ARXIV-2606-27079 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-27079 | delta:SF-2026-ARXIV-2606-27079 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27079 |
| SF-2026-ARXIV-2606-27091 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-27091 | delta:SF-2026-ARXIV-2606-27091 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27091 |
| SF-2026-ARXIV-2606-27146 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-27146 | delta:SF-2026-ARXIV-2606-27146 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27146 |
| SF-2026-ARXIV-2606-27153 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-27153 | delta:SF-2026-ARXIV-2606-27153 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27153 |
| SF-2026-ARXIV-2606-27154 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L1 | books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2606-27154 | delta:SF-2026-ARXIV-2606-27154 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27154 |
| SF-2026-ARXIV-2606-27188 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-27188 | delta:SF-2026-ARXIV-2606-27188 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27188 |
| SF-2026-ARXIV-2606-27226 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-27226 | delta:SF-2026-ARXIV-2606-27226 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27226 |
| SF-2026-ARXIV-2606-27251 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-27251 | delta:SF-2026-ARXIV-2606-27251 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27251 |
| SF-2026-ARXIV-2606-27288 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-27288 | delta:SF-2026-ARXIV-2606-27288 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27288 |
| SF-2026-ARXIV-2606-27326 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-27326 | delta:SF-2026-ARXIV-2606-27326 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27326 |
| SF-2026-ARXIV-2606-27355 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-27355 | delta:SF-2026-ARXIV-2606-27355 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27355 |

<!-- existing:SF-2026-ARXIV-2606-26156:start -->
Re-read `books/part-07-agent/82-multi-agent.md#L1` and adjacent `books/part-07-agent/81-workflow.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-26156:end -->

<!-- delta:SF-2026-ARXIV-2606-26156:start -->
把 agent 内部 decision logic 与公开 message protocol 分离：decision maker 只能从 valid decisions 选互相兼容 emission set，adapter 隔离 communication service，operational semantics 拥有 protocol compliance。
<!-- delta:SF-2026-ARXIV-2606-26156:end -->

<!-- books-review:SF-2026-ARXIV-2606-26156:start -->
Direct Evolution; Integrate queued for root. 2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。
<!-- books-review:SF-2026-ARXIV-2606-26156:end -->

<!-- existing:SF-2026-ARXIV-2606-26185:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation`.
<!-- existing:SF-2026-ARXIV-2606-26185:end -->

<!-- delta:SF-2026-ARXIV-2606-26185:start -->
`Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26185:end -->

<!-- books-review:SF-2026-ARXIV-2606-26185:start -->
Direct Evolution; Integrate. `Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26185:end -->

<!-- existing:SF-2026-ARXIV-2606-26211:start -->
At `books/part-07-agent/83-mcp.md#L83`, the current owner already establishes the base responsibility for 以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约; `books/part-07-agent/84-agent-platform.md#L20` only consumes the handoff. It does not yet state `Data Facts metadata schema; provenance, semantics, constraints and exchange contract`.
<!-- existing:SF-2026-ARXIV-2606-26211:end -->

<!-- delta:SF-2026-ARXIV-2606-26211:start -->
`Data Facts metadata schema; provenance, semantics, constraints and exchange contract` 所定义的源特定机制用于以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26211:end -->

<!-- books-review:SF-2026-ARXIV-2606-26211:start -->
Direct Evolution; Integrate. `Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26211:end -->

<!-- existing:SF-2026-ARXIV-2606-26257:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Dataset Usage Inference formulation without shadow models or held-out data`.
<!-- existing:SF-2026-ARXIV-2606-26257:end -->

<!-- delta:SF-2026-ARXIV-2606-26257:start -->
`Dataset Usage Inference formulation without shadow models or held-out data` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26257:end -->

<!-- books-review:SF-2026-ARXIV-2606-26257:start -->
Direct Evolution; Integrate. `Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26257:end -->

<!-- existing:SF-2026-ARXIV-2606-26298:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Governing Actions, Not Agents; Institutional Attestation model`.
<!-- existing:SF-2026-ARXIV-2606-26298:end -->

<!-- delta:SF-2026-ARXIV-2606-26298:start -->
`Governing Actions, Not Agents; Institutional Attestation model` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26298:end -->

<!-- books-review:SF-2026-ARXIV-2606-26298:start -->
Direct Evolution; Integrate. `Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26298:end -->

<!-- existing:SF-2026-ARXIV-2606-26300:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Verification Horizon formulation for coding-agent rewards`.
<!-- existing:SF-2026-ARXIV-2606-26300:end -->

<!-- delta:SF-2026-ARXIV-2606-26300:start -->
`Verification Horizon formulation for coding-agent rewards` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26300:end -->

<!-- books-review:SF-2026-ARXIV-2606-26300:start -->
Direct Evolution; Integrate. `No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26300:end -->

<!-- existing:SF-2026-ARXIV-2606-26341:start -->
At `books/part-06-ai-infrastructure/63-gpu-scheduler.md#L141`, the current owner already establishes the base responsibility for 把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节; `books/part-06-ai-infrastructure/64-volcano.md#L44` only consumes the handoff. It does not yet state `Many Problems One GPU batching and nonlinear-optimization execution design`.
<!-- existing:SF-2026-ARXIV-2606-26341:end -->

<!-- delta:SF-2026-ARXIV-2606-26341:start -->
`Many Problems One GPU batching and nonlinear-optimization execution design` 所定义的源特定机制用于把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26341:end -->

<!-- books-review:SF-2026-ARXIV-2606-26341:start -->
Direct Evolution; Integrate. `Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26341:end -->

<!-- existing:SF-2026-ARXIV-2606-26344:start -->
At `books/part-05-inference-system/49-tensorrt-llm.md#L630`, the current owner already establishes the base responsibility for 以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径; `books/part-05-inference-system/48-speculative-decoding.md#L113` only consumes the handoff. It does not yet state `Axon synthesizing superoptimizer; tensor-program search and verification`.
<!-- existing:SF-2026-ARXIV-2606-26344:end -->

<!-- delta:SF-2026-ARXIV-2606-26344:start -->
`Axon synthesizing superoptimizer; tensor-program search and verification` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26344:end -->

<!-- books-review:SF-2026-ARXIV-2606-26344:start -->
Direct Evolution; Integrate. `Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26344:end -->

<!-- existing:SF-2026-ARXIV-2606-26356:start -->
At `books/part-07-agent/74-prompt.md#L46`, the current owner already establishes the base responsibility for 把模块间指令干扰作为可测试的组合边界，而非默认隔离; `books/part-07-agent/75-context.md#L308` only consumes the handoff. It does not yet state `Instruction Bleed formulation; prompt-composed module interference`.
<!-- existing:SF-2026-ARXIV-2606-26356:end -->

<!-- delta:SF-2026-ARXIV-2606-26356:start -->
`Instruction Bleed formulation; prompt-composed module interference` 所定义的源特定机制用于把模块间指令干扰作为可测试的组合边界，而非默认隔离；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26356:end -->

<!-- books-review:SF-2026-ARXIV-2606-26356:start -->
Direct Evolution; Integrate. `Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26356:end -->

<!-- existing:SF-2026-ARXIV-2606-26377:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Unified intent-and-harm verification defense`.
<!-- existing:SF-2026-ARXIV-2606-26377:end -->

<!-- delta:SF-2026-ARXIV-2606-26377:start -->
`Unified intent-and-harm verification defense` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26377:end -->

<!-- books-review:SF-2026-ARXIV-2606-26377:start -->
Direct Evolution; Integrate. `Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26377:end -->

<!-- existing:SF-2026-ARXIV-2606-26383:start -->
At `books/part-06-ai-infrastructure/67-monitoring.md#L18`, the current owner already establishes the base responsibility for 以校准后的硬件与 workload 参数分解性能上界和瓶颈; `books/part-06-ai-infrastructure/68-logging.md#L16` only consumes the handoff. It does not yet state `SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation`.
<!-- existing:SF-2026-ARXIV-2606-26383:end -->

<!-- delta:SF-2026-ARXIV-2606-26383:start -->
`SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation` 所定义的源特定机制用于以校准后的硬件与 workload 参数分解性能上界和瓶颈；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26383:end -->

<!-- books-review:SF-2026-ARXIV-2606-26383:start -->
Direct Evolution; Integrate. `Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26383:end -->

<!-- existing:SF-2026-ARXIV-2606-26429:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `DualEval joint model-item calibration`.
<!-- existing:SF-2026-ARXIV-2606-26429:end -->

<!-- delta:SF-2026-ARXIV-2606-26429:start -->
`DualEval joint model-item calibration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26429:end -->

<!-- books-review:SF-2026-ARXIV-2606-26429:start -->
Direct Evolution; Integrate. `Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26429:end -->

<!-- existing:SF-2026-ARXIV-2606-26439:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization`.
<!-- existing:SF-2026-ARXIV-2606-26439:end -->

<!-- delta:SF-2026-ARXIV-2606-26439:start -->
`TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26439:end -->

<!-- books-review:SF-2026-ARXIV-2606-26439:start -->
Direct Evolution; Integrate. `Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26439:end -->

<!-- existing:SF-2026-ARXIV-2606-26441:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `GPUSparse learned sparse retrieval with parallel inverted indices`.
<!-- existing:SF-2026-ARXIV-2606-26441:end -->

<!-- delta:SF-2026-ARXIV-2606-26441:start -->
`GPUSparse learned sparse retrieval with parallel inverted indices` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26441:end -->

<!-- books-review:SF-2026-ARXIV-2606-26441:start -->
Direct Evolution; Integrate. `Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26441:end -->

<!-- existing:SF-2026-ARXIV-2606-26442:start -->
At `books/part-07-agent/81-workflow.md#L36`, the current owner already establishes the base responsibility for 把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态; `books/part-07-agent/78-tool-calling.md#L37` only consumes the handoff. It does not yet state `AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling`.
<!-- existing:SF-2026-ARXIV-2606-26442:end -->

<!-- delta:SF-2026-ARXIV-2606-26442:start -->
`AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26442:end -->

<!-- books-review:SF-2026-ARXIV-2606-26442:start -->
Direct Evolution; Integrate. `Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26442:end -->

<!-- existing:SF-2026-ARXIV-2606-26449:start -->
At `books/part-06-ai-infrastructure/69-trace.md#L33`, the current owner already establishes the base responsibility for 让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值; `books/part-06-ai-infrastructure/68-logging.md#L66` only consumes the handoff. It does not yet state `ProvenAI provenance-native trace schema and evidence links`.
<!-- existing:SF-2026-ARXIV-2606-26449:end -->

<!-- delta:SF-2026-ARXIV-2606-26449:start -->
`ProvenAI provenance-native trace schema and evidence links` 所定义的源特定机制用于让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26449:end -->

<!-- books-review:SF-2026-ARXIV-2606-26449:start -->
Direct Evolution; Integrate. `Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26449:end -->

<!-- existing:SF-2026-ARXIV-2606-26453:start -->
At `books/part-05-inference-system/49-tensorrt-llm.md#L630`, the current owner already establishes the base responsibility for 以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径; `books/part-05-inference-system/48-speculative-decoding.md#L113` only consumes the handoff. It does not yet state `Micro-profiling tools as expert surrogates for LLM CUDA optimization`.
<!-- existing:SF-2026-ARXIV-2606-26453:end -->

<!-- delta:SF-2026-ARXIV-2606-26453:start -->
`Micro-profiling tools as expert surrogates for LLM CUDA optimization` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26453:end -->

<!-- books-review:SF-2026-ARXIV-2606-26453:start -->
Direct Evolution; Integrate. `Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26453:end -->

<!-- existing:SF-2026-ARXIV-2606-26456:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Safety-Aware Mutation Testing proposal and interaction-aware mutant model`.
<!-- existing:SF-2026-ARXIV-2606-26456:end -->

<!-- delta:SF-2026-ARXIV-2606-26456:start -->
`Safety-Aware Mutation Testing proposal and interaction-aware mutant model` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26456:end -->

<!-- books-review:SF-2026-ARXIV-2606-26456:start -->
Direct Evolution; Integrate. `Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26456:end -->

<!-- existing:SF-2026-ARXIV-2606-26463:start -->
At `books/part-07-agent/79-planning.md#L140`, the current owner already establishes the base responsibility for 以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退; `books/part-07-agent/80-reflection.md#L73` only consumes the handoff. It does not yet state `Variable-delay real-time RL; lightweight gate selects state-dependent planning budget`.
<!-- existing:SF-2026-ARXIV-2606-26463:end -->

<!-- delta:SF-2026-ARXIV-2606-26463:start -->
`Variable-delay real-time RL; lightweight gate selects state-dependent planning budget` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26463:end -->

<!-- books-review:SF-2026-ARXIV-2606-26463:start -->
Direct Evolution; Integrate. `Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26463:end -->

<!-- existing:SF-2026-ARXIV-2606-26472:start -->
At `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L97`, the current owner already establishes the base responsibility for 以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退; `books/part-05-inference-system/44-decode.md#L31` only consumes the handoff. It does not yet state `Epiphany score from forward-pass representation change; attention-matrix-free eviction`.
<!-- existing:SF-2026-ARXIV-2606-26472:end -->

<!-- delta:SF-2026-ARXIV-2606-26472:start -->
`Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26472:end -->

<!-- books-review:SF-2026-ARXIV-2606-26472:start -->
Direct Evolution; Integrate. `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26472:end -->

<!-- existing:SF-2026-ARXIV-2606-26479:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `Out-of-band prompt-injection defenses organized as reference monitors and integrity policies`.
<!-- existing:SF-2026-ARXIV-2606-26479:end -->

<!-- delta:SF-2026-ARXIV-2606-26479:start -->
`Out-of-band prompt-injection defenses organized as reference monitors and integrity policies` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26479:end -->

<!-- books-review:SF-2026-ARXIV-2606-26479:start -->
Direct Evolution; Integrate. `Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26479:end -->

<!-- existing:SF-2026-ARXIV-2606-26488:start -->
At `books/part-05-inference-system/54-gpu-memory.md#L186`, the current owner already establishes the base responsibility for 把稀疏、量化或压缩决策绑定到显存预算和质量回退; `books/part-05-inference-system/55-pd-disaggregation.md#L409` only consumes the handoff. It does not yet state `Compression of recursive reasoners across precision, pruning, distillation and attention variants`.
<!-- existing:SF-2026-ARXIV-2606-26488:end -->

<!-- delta:SF-2026-ARXIV-2606-26488:start -->
`Compression of recursive reasoners across precision, pruning, distillation and attention variants` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26488:end -->

<!-- books-review:SF-2026-ARXIV-2606-26488:start -->
Direct Evolution; Integrate. `Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26488:end -->

<!-- existing:SF-2026-ARXIV-2606-26492:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `Within-program versus leave-program-out diagnostic design`.
<!-- existing:SF-2026-ARXIV-2606-26492:end -->

<!-- delta:SF-2026-ARXIV-2606-26492:start -->
`Within-program versus leave-program-out diagnostic design` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26492:end -->

<!-- books-review:SF-2026-ARXIV-2606-26492:start -->
Direct Evolution; Integrate. `Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26492:end -->

<!-- existing:SF-2026-ARXIV-2606-26511:start -->
记忆写入以来源、有效时间、事务边界、supersession 与恢复回执为长期状态，未经验证的新条目不能静默覆盖旧事实。
<!-- existing:SF-2026-ARXIV-2606-26511:end -->

<!-- delta:SF-2026-ARXIV-2606-26511:start -->
Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge 的 exact-v1 机制为：We present MemStrata, a retrieval memory maintaining temporal validity. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-26511:end -->

<!-- books-review:SF-2026-ARXIV-2606-26511:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：The central result is the stale-fact-error rate: when required to answer, RAG serves superseded values 15-40% of the time; MemStrata drives this to ~0%, a failure class RAG cannot avoid. 披露的 evaluation signal 是：We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. exact-v1 的观测边界是：We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. 它没有证明 We present MemStrata, a retrieval memory maintaining temporal validity. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26511:end -->

<!-- existing:SF-2026-ARXIV-2606-26524:start -->
安全边界由独立 reference monitor 持有，instruction/data/control 分离，并在身份、证据或 policy 不足时 fail closed。
<!-- existing:SF-2026-ARXIV-2606-26524:end -->

<!-- delta:SF-2026-ARXIV-2606-26524:start -->
VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills 的 exact-v1 机制为：In this work, we present VIGIL, an end-to-end runtime enforcement framework for agentic systems. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-26524:end -->

<!-- books-review:SF-2026-ARXIV-2606-26524:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Enforcing them raises a contextual granularity challenge: even when a policy is written for a particular task context, a monitor must still decide which events to observe, what state to retain, how far across the execution to reason, and where to intervene. 披露的 evaluation signal 是：The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. exact-v1 的观测边界是：The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. 它没有证明 In this work, we present VIGIL, an end-to-end runtime enforcement framework for agentic systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26524:end -->

<!-- existing:SF-2026-ARXIV-2606-26590:start -->
评估系统把样本、metric、judge、阈值、不确定性与 release authority 分离并版本化。
<!-- existing:SF-2026-ARXIV-2606-26590:end -->

<!-- delta:SF-2026-ARXIV-2606-26590:start -->
Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform 的 exact-v1 机制为：This paper presents TerraProbe, a five-layer oracle framework for evaluating LLM-assisted Terraform security repair. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-26590:end -->

<!-- books-review:SF-2026-ARXIV-2606-26590:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Security misconfigurations in Terraform Infrastructure-as-Code are a growing risk in cloud deployments, and large language models are increasingly used as automated repair agents. 披露的 evaluation signal 是：Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. exact-v1 的观测边界是：Existing evaluations often treat a repair as successful when the targeted static-analysis finding disappears, without checking planning validity, behavioral change, or security intent. 它没有证明 This paper presents TerraProbe, a five-layer oracle framework for evaluating LLM-assisted Terraform security repair. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26590:end -->

<!-- existing:SF-2026-ARXIV-2606-26607:start -->
调度器在请求、KV、expert、拓扑和 SLO 之间做显式分配，并保留准入、抢占和回退状态。
<!-- existing:SF-2026-ARXIV-2606-26607:end -->

<!-- delta:SF-2026-ARXIV-2606-26607:start -->
Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch 的 exact-v1 机制为：We present Moebius, a serving system that switches between EP and TP at runtime without restarting the engine or dropping in-flight requests. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。
<!-- delta:SF-2026-ARXIV-2606-26607:end -->

<!-- books-review:SF-2026-ARXIV-2606-26607:start -->
Unique owner `INFER-SCHEDULING`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Moving those owner-changed slices is the sole irreducible cost, and modern high-bandwidth GPU interconnects make it fast enough to do between decode steps without draining in-flight requests. 披露的 evaluation signal 是：Each switch completes in 215-434 ms, and Moebius holds both layouts resident with only 2.4% memory overhead. exact-v1 的观测边界是：Each switch completes in 215-434 ms, and Moebius holds both layouts resident with only 2.4% memory overhead. 它没有证明 We present Moebius, a serving system that switches between EP and TP at runtime without restarting the engine or dropping in-flight requests. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26607:end -->

<!-- existing:SF-2026-ARXIV-2606-26631:start -->
KV identity 绑定模型、adapter、position、layout 与压缩/驱逐版本，失配时执行 dense recompute。
<!-- existing:SF-2026-ARXIV-2606-26631:end -->

<!-- delta:SF-2026-ARXIV-2606-26631:start -->
Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning 的 exact-v1 机制为：To this end, we propose Position Rebinding Cache Reuse (PRCR), a cache-level framework for replay-free visual revisiting. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。
<!-- delta:SF-2026-ARXIV-2606-26631:end -->

<!-- books-review:SF-2026-ARXIV-2606-26631:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：However, we identify a critical failure mode of this strategy: cached visual keys are already bound to their original positional context. 披露的 evaluation signal 是：Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. exact-v1 的观测边界是：Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. 它没有证明 To this end, we propose Position Rebinding Cache Reuse (PRCR), a cache-level framework for replay-free visual revisiting. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26631:end -->

<!-- existing:SF-2026-ARXIV-2606-26649:start -->
安全边界由独立 reference monitor 持有，instruction/data/control 分离，并在身份、证据或 policy 不足时 fail closed。
<!-- existing:SF-2026-ARXIV-2606-26649:end -->

<!-- delta:SF-2026-ARXIV-2606-26649:start -->
Autoformalization of Agent Instructions into Policy-as-Code 的 exact-v1 机制为：We present an autoformalization pipeline that translates agent prompts, MCP tool descriptions, and natural language policy documents into formally verified policies using an LLM-based generator-critic loop. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-26649:end -->

<!-- books-review:SF-2026-ARXIV-2606-26649:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Agent safety in high-stakes domains requires formal policy enforcement, but most existing approaches either rely on probabilistic guardrails (fine-tuned classifiers, prompt-based steering) that offer no formal guarantees, or on hand-coded symbolic enforcement that does not scale to the breadth of real policy specifications. 披露的 evaluation signal 是：The resulting policies are written in the Cedar Policy Language. exact-v1 的观测边界是：The resulting policies are written in the Cedar Policy Language. 它没有证明 We present an autoformalization pipeline that translates agent prompts, MCP tool descriptions, and natural language policy documents into formally verified policies using an LLM-based generator-critic loop. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26649:end -->

<!-- existing:SF-2026-ARXIV-2606-26721:start -->
工作流 owner 持有持久化步骤、依赖、Gate、retry、compensation、rollback 与终止条件。
<!-- existing:SF-2026-ARXIV-2606-26721:end -->

<!-- delta:SF-2026-ARXIV-2606-26721:start -->
Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration 的 exact-v1 机制为：This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。
<!-- delta:SF-2026-ARXIV-2606-26721:end -->

<!-- books-review:SF-2026-ARXIV-2606-26721:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：AI coding agents are changing the bottleneck in software collaboration: code is increasingly cheap, while understanding intent, negotiating scope, and governing long-term project responsibility remain costly. 披露的 evaluation signal 是：We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. exact-v1 的观测边界是：We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. 它没有证明 This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26721:end -->

<!-- existing:SF-2026-ARXIV-2606-26753:start -->
记忆写入以来源、有效时间、事务边界、supersession 与恢复回执为长期状态，未经验证的新条目不能静默覆盖旧事实。
<!-- existing:SF-2026-ARXIV-2606-26753:end -->

<!-- delta:SF-2026-ARXIV-2606-26753:start -->
ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification 的 exact-v1 机制为：The core mechanism is a dual-evidence gate that conditions a relation judgment on the specific target proposition, scoring a (target, source) pair through the product of a MiniLM slot head and a DeBERTa-v3 slot head and gating it by conservative event/operation evidence. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-26753:end -->

<!-- books-review:SF-2026-ARXIV-2606-26753:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：On a synthetic multi-hop validity benchmark the gate reaches 90.12% +/- 1.73 accuracy; through a real-data feedback loop that mines failure patterns but trains on synthetic pairs only, the verifier transfers to Memora role binding with zero target-side labels, reaching 98.8% +/- 0.9 group-all-correct. 披露的 evaluation signal 是：This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842). exact-v1 的观测边界是：This report extends ConvMemory v1 (arXiv:2605.28062) and v2 (arXiv:2606.10842). 它没有证明 The core mechanism is a dual-evidence gate that conditions a relation judgment on the specific target proposition, scoring a (target, source) pair through the product of a MiniLM slot head and a DeBERTa-v3 slot head and gating it by conservative event/operation evidence. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26753:end -->

<!-- existing:SF-2026-ARXIV-2606-26793:start -->
安全边界由独立 reference monitor 持有，instruction/data/control 分离，并在身份、证据或 policy 不足时 fail closed。
<!-- existing:SF-2026-ARXIV-2606-26793:end -->

<!-- delta:SF-2026-ARXIV-2606-26793:start -->
MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG 的 exact-v1 机制为：We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-26793:end -->

<!-- books-review:SF-2026-ARXIV-2606-26793:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. 披露的 evaluation signal 是：We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces. exact-v1 的观测边界是：We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces. 它没有证明 We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26793:end -->

<!-- existing:SF-2026-ARXIV-2606-26806:start -->
记忆写入以来源、有效时间、事务边界、supersession 与恢复回执为长期状态，未经验证的新条目不能静默覆盖旧事实。
<!-- existing:SF-2026-ARXIV-2606-26806:end -->

<!-- delta:SF-2026-ARXIV-2606-26806:start -->
Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents 的 exact-v1 机制为：We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-26806:end -->

<!-- books-review:SF-2026-ARXIV-2606-26806:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 披露的 evaluation signal 是：We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. exact-v1 的观测边界是：We evaluate EVAF, a surprise- and valence-gated LoRA consolidation mechanism. 它没有证明 We introduce the loop-drift protocol, a controlled stress test in which the retrieval index remains intact while working context is unloaded and goal-conditioned behavior must persist under long-loop interference. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26806:end -->

<!-- existing:SF-2026-ARXIV-2606-26836:start -->
评估系统把样本、metric、judge、阈值、不确定性与 release authority 分离并版本化。
<!-- existing:SF-2026-ARXIV-2606-26836:end -->

<!-- delta:SF-2026-ARXIV-2606-26836:start -->
The Capability Frontier: Benchmarks Miss 82% of Model Performance 的 exact-v1 机制为：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-26836:end -->

<!-- books-review:SF-2026-ARXIV-2606-26836:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 披露的 evaluation signal 是：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). exact-v1 的观测边界是：To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 它没有证明 To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26836:end -->

<!-- existing:SF-2026-ARXIV-2606-26875:start -->
KV identity 绑定模型、adapter、position、layout 与压缩/驱逐版本，失配时执行 dense recompute。
<!-- existing:SF-2026-ARXIV-2606-26875:end -->

<!-- delta:SF-2026-ARXIV-2606-26875:start -->
Information-Aware KV Cache Compression for Long Reasoning 的 exact-v1 机制为：Based on the observation, we propose \textbf{InfoKV}, an entropy-aware KV cache compression framework that incorporates information-theoretic signals. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。
<!-- delta:SF-2026-ARXIV-2606-26875:end -->

<!-- books-review:SF-2026-ARXIV-2606-26875:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：While attention effectively captures contextual relevance, it overlooks complementary information-theoretic signals related to predictive uncertainty and token informativeness. 披露的 evaluation signal 是：Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. exact-v1 的观测边界是：Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. 它没有证明 Based on the observation, we propose \textbf{InfoKV}, an entropy-aware KV cache compression framework that incorporates information-theoretic signals. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26875:end -->

<!-- existing:SF-2026-ARXIV-2606-26924:start -->
Agent 平台以 Control、Evidence、Execution planes 隔离策略、观测与副作用执行。
<!-- existing:SF-2026-ARXIV-2606-26924:end -->

<!-- delta:SF-2026-ARXIV-2606-26924:start -->
A Deterministic Control Plane for LLM Coding Agents 的 exact-v1 机制为：We propose a deterministic control plane above the harness that maps one-to-one to these gaps. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。
<!-- delta:SF-2026-ARXIV-2606-26924:end -->

<!-- books-review:SF-2026-ARXIV-2606-26924:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Rel(AI)Build treats agent definitions as a managed supply chain (SHA-256 content addressing, HMAC-stamped lockfiles, hash-chained audit logs); enforces tiered permissions and attack-derived blocklists before LLM invocation; gates feature work through a phase state machine with requirement-to-file-to-test traceability; compiles a single canonical definition to seven IDE targets; and detects prompt drift via Jaccard similarity. 披露的 evaluation signal 是：Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration. exact-v1 的观测边界是：Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration. 它没有证明 We propose a deterministic control plane above the harness that maps one-to-one to these gaps. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26924:end -->

<!-- existing:SF-2026-ARXIV-2606-26935:start -->
反思只生成 diagnosis/candidate lesson，须经 held-out 验证、promotion 与 rollback 才能写入长期策略。
<!-- existing:SF-2026-ARXIV-2606-26935:end -->

<!-- delta:SF-2026-ARXIV-2606-26935:start -->
Where Do CoT Training Gains Land in LLM based Agents? 的 exact-v1 机制为：We therefore ask what CoT training is actually improving: is the model getting better at changing its action through generated reasoning, or is it getting better at predicting the action directly from the prompt? 因此 把 diagnosis、candidate lesson、独立验证、promotion 与 rollback 分离。
<!-- delta:SF-2026-ARXIV-2606-26935:end -->

<!-- books-review:SF-2026-ARXIV-2606-26935:start -->
Unique owner `AGENT-REFLECTION`; adjacent non-owner `books/part-07-agent/81-workflow.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. 披露的 evaluation signal 是：Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. exact-v1 的观测边界是：Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. 它没有证明 We therefore ask what CoT training is actually improving: is the model getting better at changing its action through generated reasoning, or is it getting better at predicting the action directly from the prompt? 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26935:end -->

<!-- existing:SF-2026-ARXIV-2606-26979:start -->
上下文 owner 持有来源、预算、有效期、压缩/恢复规格与失败恢复边界。
<!-- existing:SF-2026-ARXIV-2606-26979:end -->

<!-- delta:SF-2026-ARXIV-2606-26979:start -->
How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring 的 exact-v1 机制为：This makes agent navigation stochastic and difficult to reproduce across runs. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。
<!-- delta:SF-2026-ARXIV-2606-26979:end -->

<!-- books-review:SF-2026-ARXIV-2606-26979:start -->
Unique owner `AGENT-CONTEXT`; adjacent non-owner `books/part-07-agent/76-rag.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  披露的 evaluation signal 是：Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  exact-v1 的观测边界是：Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24,  它没有证明 This makes agent navigation stochastic and difficult to reproduce across runs. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26979:end -->

<!-- existing:SF-2026-ARXIV-2606-26990:start -->
评估系统把样本、metric、judge、阈值、不确定性与 release authority 分离并版本化。
<!-- existing:SF-2026-ARXIV-2606-26990:end -->

<!-- delta:SF-2026-ARXIV-2606-26990:start -->
Decision-Aligned Evaluation of Uncertainty Quantification 的 exact-v1 机制为：We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-26990:end -->

<!-- books-review:SF-2026-ARXIV-2606-26990:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. 披露的 evaluation signal 是：Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. exact-v1 的观测边界是：Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. 它没有证明 We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26990:end -->

<!-- existing:SF-2026-ARXIV-2606-26997:start -->
分布式训练把 shard layout、worker/collective identity、optimizer state 与 checkpoint 原子性共同纳入恢复合同。
<!-- existing:SF-2026-ARXIV-2606-26997:end -->

<!-- delta:SF-2026-ARXIV-2606-26997:start -->
RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning 的 exact-v1 机制为：To address these challenges, we propose RolloutPipe, a post-training framework for disaggregated RLVR systems, which turns the fixed-weight rollout into a complete-group pipeline where trainable groups move to the trainer while later groups are still being generated. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。
<!-- delta:SF-2026-ARXIV-2606-26997:end -->

<!-- books-review:SF-2026-ARXIV-2606-26997:start -->
Unique owner `TRAIN-DISTRIBUTED-TRAINING`; adjacent non-owner `books/part-04-training-system/37-tensor-parallel.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：However, existing synchronous on-policy GRPO (Group Relative Policy Optimization) RLVR systems finish an entire rollout before starting training, leaving the trainer GPU pool idle while rollout is still ongoing. 披露的 evaluation signal 是：RolloutPipe achieves this through two techniques including complete-group pipelining (CGP) and frontier-group dispatch (FGD). exact-v1 的观测边界是：RolloutPipe achieves this through two techniques including complete-group pipelining (CGP) and frontier-group dispatch (FGD). 它没有证明 To address these challenges, we propose RolloutPipe, a post-training framework for disaggregated RLVR systems, which turns the fixed-weight rollout into a complete-group pipeline where trainable groups move to the trainer while later groups are still being generated. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-26997:end -->

<!-- existing:SF-2026-ARXIV-2606-27009:start -->
工作流 owner 持有持久化步骤、依赖、Gate、retry、compensation、rollback 与终止条件。
<!-- existing:SF-2026-ARXIV-2606-27009:end -->

<!-- delta:SF-2026-ARXIV-2606-27009:start -->
Semantic Early-Stopping for Iterative LLM Agent Loops 的 exact-v1 机制为：This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。
<!-- delta:SF-2026-ARXIV-2606-27009:end -->

<!-- books-review:SF-2026-ARXIV-2606-27009:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Second, a judge-efficient evaluation protocol: we generate each question's full trajectory once, replay every stopping policy over the identical drafts, and cache every LLM-judge call, yielding a strictly paired efficiency-versus-quality comparison at low cost; we further separate operational tokens (charged to a policy) from evaluation tokens (a measurement instrument). 披露的 evaluation signal 是：This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. exact-v1 的观测边界是：This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 它没有证明 This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27009:end -->

<!-- existing:SF-2026-ARXIV-2606-27027:start -->
MCP owner 绑定 server/tool identity、schema、session 与 effect-time authorization，并把描述视为不可信输入。
<!-- existing:SF-2026-ARXIV-2606-27027:end -->

<!-- delta:SF-2026-ARXIV-2606-27027:start -->
ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP 的 exact-v1 机制为：In this paper, we introduce ShareLock, a multi-tool threshold poisoning framework that utilizes Shamir's threshold scheme to ensure exceptional stealth and fault tolerance. 因此 把 server/tool identity、描述、组合阈值、污染证据与 effect-time authorization 绑定。
<!-- delta:SF-2026-ARXIV-2606-27027:end -->

<!-- books-review:SF-2026-ARXIV-2606-27027:start -->
Unique owner `AGENT-MCP`; adjacent non-owner `books/part-07-agent/84-agent-platform.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, the expanding adoption of MCP has also introduced novel security concerns such as Tool Poisoning Attack (TPA), which exploit LLM-server interactions to inject malicious prompts. 披露的 evaluation signal 是：ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. exact-v1 的观测边界是：ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. 它没有证明 In this paper, we introduce ShareLock, a multi-tool threshold poisoning framework that utilizes Shamir's threshold scheme to ensure exceptional stealth and fault tolerance. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27027:end -->

<!-- existing:SF-2026-ARXIV-2606-27045:start -->
上下文 owner 持有来源、预算、有效期、压缩/恢复规格与失败恢复边界。
<!-- existing:SF-2026-ARXIV-2606-27045:end -->

<!-- delta:SF-2026-ARXIV-2606-27045:start -->
The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development 的 exact-v1 机制为：We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。
<!-- delta:SF-2026-ARXIV-2606-27045:end -->

<!-- books-review:SF-2026-ARXIV-2606-27045:start -->
Unique owner `AGENT-CONTEXT`; adjacent non-owner `books/part-07-agent/76-rag.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：AI coding agents dramatically accelerate implementation speed but introduce two structural failure modes that existing spec-driven approaches do not fully solve: (1) context explosion -- the agent must reason over an entire repository at once, degrading output quality as the context window fills; and (2) silent spec-code drift -- code evolves, the specification does not, and the divergence becomes invisible until it is costly to repair. 披露的 evaluation signal 是：The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA. exact-v1 的观测边界是：The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA. 它没有证明 We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27045:end -->

<!-- existing:SF-2026-ARXIV-2606-27079:start -->
VLA owner 绑定 observation、action、temporal state、preemption 与 safety controller，物理提交必须可中止。
<!-- existing:SF-2026-ARXIV-2606-27079:end -->

<!-- delta:SF-2026-ARXIV-2606-27079:start -->
ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models 的 exact-v1 机制为：To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-27079:end -->

<!-- books-review:SF-2026-ARXIV-2606-27079:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We define a 13-category safety taxonomy covering physical interaction safety (Safe-Core), instruction-side safety (Safe-Lang), and perception-side safety (Safe-Vis), and evaluate policies under three controlled dimensions of variation -- scene structure, language command, and visual observation -- so that failure sources can be diagnosed rather than hidden in a single aggregate score. 披露的 evaluation signal 是：To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. exact-v1 的观测边界是：To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 它没有证明 To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27079:end -->

<!-- existing:SF-2026-ARXIV-2606-27091:start -->
安全边界由独立 reference monitor 持有，instruction/data/control 分离，并在身份、证据或 policy 不足时 fail closed。
<!-- existing:SF-2026-ARXIV-2606-27091:end -->

<!-- delta:SF-2026-ARXIV-2606-27091:start -->
Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation 的 exact-v1 机制为：We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-27091:end -->

<!-- books-review:SF-2026-ARXIV-2606-27091:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 披露的 evaluation signal 是：LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. exact-v1 的观测边界是：LLMs fine-tuned for security classification are usually evaluated on held-out examples from the same distribution as their training data. 它没有证明 We show that this can miss vulnerabilities introduced by fine-tuning itself: models can learn token-level indicator semantics that preserve canonical accuracy while failing under behavior-preserving transformations such as PowerShell alias substitution, command reconstruction, string construction, execution indirection, and case mutation. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27091:end -->

<!-- existing:SF-2026-ARXIV-2606-27146:start -->
VLA owner 绑定 observation、action、temporal state、preemption 与 safety controller，物理提交必须可中止。
<!-- existing:SF-2026-ARXIV-2606-27146:end -->

<!-- delta:SF-2026-ARXIV-2606-27146:start -->
PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies 的 exact-v1 机制为：We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-27146:end -->

<!-- books-review:SF-2026-ARXIV-2606-27146:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Long-horizon robotic manipulation is highly sensitive to physically infeasible transitions, contact-induced disturbances, and the lack of effective self-correction during execution. 披露的 evaluation signal 是：We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. exact-v1 的观测边界是：We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 它没有证明 We present PhysReflect-VLA, a plug-and-play execution-time reliability framework that augments VLA policies with physical feasibility evaluation and structured self-reflection in a closed-loop control pipeline. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27146:end -->

<!-- existing:SF-2026-ARXIV-2606-27153:start -->
分布式训练把 shard layout、worker/collective identity、optimizer state 与 checkpoint 原子性共同纳入恢复合同。
<!-- existing:SF-2026-ARXIV-2606-27153:end -->

<!-- delta:SF-2026-ARXIV-2606-27153:start -->
DMuon: Efficient Distributed Muon Training with Near-Adam Overhead 的 exact-v1 机制为：To close this gap, we present DMuon, an open-source distributed Muon implementation that integrates into existing training pipelines as a drop-in module, with no framework-level modifications. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。
<!-- delta:SF-2026-ARXIV-2606-27153:end -->

<!-- books-review:SF-2026-ARXIV-2606-27153:start -->
Unique owner `TRAIN-DISTRIBUTED-TRAINING`; adjacent non-owner `books/part-04-training-system/37-tensor-parallel.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Yet contemporary distributed training infrastructure built around the assumption of element-wise optimizers is poorly matched to matrix-level optimizers such as Muon, whose updates couple entire weight matrices and require costly Newton-Schulz iterations. 披露的 evaluation signal 是：Across both embodied foundation model and large language model (LLM) training workloads, DMuon achieves a 1.48x-3.01x speedup in end-to-end step time and a 6.85x-163.00x speedup in optimizer-step time, bringing per-step latency to near-AdamW levels and enabling efficient scaling in our model training. exact-v1 的观测边界是：Across both embodied foundation model and large language model (LLM) training workloads, DMuon achieves a 1.48x-3.01x speedup in end-to-end step time and a 6.85x-163.00x speedup in optimizer-step time, bringing per-step latency to near-AdamW levels and enabling efficient scaling in our model training. 它没有证明 To close this gap, we present DMuon, an open-source distributed Muon implementation that integrates into existing training pipelines as a drop-in module, with no framework-level modifications. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27153:end -->

<!-- existing:SF-2026-ARXIV-2606-27154:start -->
Trace owner 区分 observed event、causal hypothesis、verification evidence 与 repair authority。
<!-- existing:SF-2026-ARXIV-2606-27154:end -->

<!-- delta:SF-2026-ARXIV-2606-27154:start -->
OpenRCA 2.0: From Outcome Labels to Causal Process Supervision 的 exact-v1 机制为：To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 因此 把事件 identity、因果链、verification evidence 与诊断结论分离。
<!-- delta:SF-2026-ARXIV-2606-27154:end -->

<!-- books-review:SF-2026-ARXIV-2606-27154:start -->
Unique owner `PLATFORM-TRACE`; adjacent non-owner `books/part-06-ai-infrastructure/70-cost.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching. 披露的 evaluation signal 是：To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. exact-v1 的观测边界是：To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 它没有证明 To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27154:end -->

<!-- existing:SF-2026-ARXIV-2606-27188:start -->
工作流 owner 持有持久化步骤、依赖、Gate、retry、compensation、rollback 与终止条件。
<!-- existing:SF-2026-ARXIV-2606-27188:end -->

<!-- delta:SF-2026-ARXIV-2606-27188:start -->
A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO 的 exact-v1 机制为：We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。
<!-- delta:SF-2026-ARXIV-2606-27188:end -->

<!-- books-review:SF-2026-ARXIV-2606-27188:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 披露的 evaluation signal 是：The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it. exact-v1 的观测边界是：The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it. 它没有证明 We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27188:end -->

<!-- existing:SF-2026-ARXIV-2606-27226:start -->
评估系统把样本、metric、judge、阈值、不确定性与 release authority 分离并版本化。
<!-- existing:SF-2026-ARXIV-2606-27226:end -->

<!-- delta:SF-2026-ARXIV-2606-27226:start -->
Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement 的 exact-v1 机制为：We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-27226:end -->

<!-- books-review:SF-2026-ARXIV-2606-27226:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. 披露的 evaluation signal 是：Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. exact-v1 的观测边界是：Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. 它没有证明 We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27226:end -->

<!-- existing:SF-2026-ARXIV-2606-27251:start -->
VLA owner 绑定 observation、action、temporal state、preemption 与 safety controller，物理提交必须可中止。
<!-- existing:SF-2026-ARXIV-2606-27251:end -->

<!-- delta:SF-2026-ARXIV-2606-27251:start -->
Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy 的 exact-v1 机制为：To this end, we present OmniAct, a framework integrating a multimodal semantic planner for skill routing across unified action spaces, an adaptive hierarchical memory with event-boundary-driven compression for sub-linear context growth, and an asynchronous visual preemption engine that closes the semantic loop during physical execution. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-27251:end -->

<!-- books-review:SF-2026-ARXIV-2606-27251:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Building persistent embodied agents in unstructured environments demands unified orchestration of heterogeneous tools spanning both cyber (APIs, IoT) and physical (manipulation, navigation) domains, coupled with autonomous recovery from physical failures that inevitably arise over extended operation. 披露的 evaluation signal 是：Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance. exact-v1 的观测边界是：Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance. 它没有证明 To this end, we present OmniAct, a framework integrating a multimodal semantic planner for skill routing across unified action spaces, an adaptive hierarchical memory with event-boundary-driven compression for sub-linear context growth, and an asynchronous visual preemption engine that closes the semantic loop during physical execution. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27251:end -->

<!-- existing:SF-2026-ARXIV-2606-27288:start -->
多智能体 owner 持有拓扑、角色、消息 provenance、独立 verifier 与 commit authority。
<!-- existing:SF-2026-ARXIV-2606-27288:end -->

<!-- delta:SF-2026-ARXIV-2606-27288:start -->
When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models 的 exact-v1 机制为：We show that their gain is capped by a quantity the field rarely reports. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。
<!-- delta:SF-2026-ARXIV-2606-27288:end -->

<!-- books-review:SF-2026-ARXIV-2606-27288:start -->
Unique owner `AGENT-MULTI-AGENT`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Re-asking the same GPQA-Diamond questions in free-response rather than multiple-choice form reopens the tail, with beta 0.127 and a five-judge panel with kappa 0.73 to 0.92, locating co-failure in answer format rather than subject. 披露的 evaluation signal 是：We show that their gain is capped by a quantity the field rarely reports. exact-v1 的观测边界是：We show that their gain is capped by a quantity the field rarely reports. 它没有证明 We show that their gain is capped by a quantity the field rarely reports. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27288:end -->

<!-- existing:SF-2026-ARXIV-2606-27326:start -->
世界模型区分 predicted state/rollout、uncertainty 与真实观测，后者是 hallucination fallback。
<!-- existing:SF-2026-ARXIV-2606-27326:end -->

<!-- delta:SF-2026-ARXIV-2606-27326:start -->
Hallucination in World Models is Predictable and Preventable 的 exact-v1 机制为：To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. 因此 把 world-state、rollout、hallucination detector 与真实观测 fallback 分离。
<!-- delta:SF-2026-ARXIV-2606-27326:end -->

<!-- books-review:SF-2026-ARXIV-2606-27326:start -->
Unique owner `MULTIMODAL-WORLD-MODELS`; adjacent non-owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. 披露的 evaluation signal 是：Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. exact-v1 的观测边界是：Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. 它没有证明 To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27326:end -->

<!-- existing:SF-2026-ARXIV-2606-27355:start -->
VLA owner 绑定 observation、action、temporal state、preemption 与 safety controller，物理提交必须可中止。
<!-- existing:SF-2026-ARXIV-2606-27355:end -->

<!-- delta:SF-2026-ARXIV-2606-27355:start -->
RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools 的 exact-v1 机制为：We study two recurring decisions: which expert to deploy for a new condition and which candidate to add to the pool. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-27355:end -->

<!-- books-review:SF-2026-ARXIV-2606-27355:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：RouterVLA combines a split-clean prior and outcome-disjoint probes with onboarding that credits only failures the incumbent pool cannot handle. 披露的 evaluation signal 是：Both criteria independently converge on the same five experts, confirming that the candidates best positioned to cover the base pool's blind spots are also broadly capable. exact-v1 的观测边界是：Both criteria independently converge on the same five experts, confirming that the candidates best positioned to cover the base pool's blind spots are also broadly capable. 它没有证明 We study two recurring decisions: which expert to deploy for a new condition and which candidate to add to the pool. 在未测模型、分布、攻击者、规模或生产 SLO 下仍成立。 观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-27355:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260626-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260626 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260626: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260626-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-26156; review:SF-2026-ARXIV-2606-26185; review:SF-2026-ARXIV-2606-26211; review:SF-2026-ARXIV-2606-26257; review:SF-2026-ARXIV-2606-26298; review:SF-2026-ARXIV-2606-26300; review:SF-2026-ARXIV-2606-26341; review:SF-2026-ARXIV-2606-26344; review:SF-2026-ARXIV-2606-26356; review:SF-2026-ARXIV-2606-26377; review:SF-2026-ARXIV-2606-26383; review:SF-2026-ARXIV-2606-26429; review:SF-2026-ARXIV-2606-26439; review:SF-2026-ARXIV-2606-26441; review:SF-2026-ARXIV-2606-26442; review:SF-2026-ARXIV-2606-26449; review:SF-2026-ARXIV-2606-26453; review:SF-2026-ARXIV-2606-26456; review:SF-2026-ARXIV-2606-26463; review:SF-2026-ARXIV-2606-26472; review:SF-2026-ARXIV-2606-26479; review:SF-2026-ARXIV-2606-26488; review:SF-2026-ARXIV-2606-26492; review:SF-2026-ARXIV-2606-26511; review:SF-2026-ARXIV-2606-26524; review:SF-2026-ARXIV-2606-26529; review:SF-2026-ARXIV-2606-26587; review:SF-2026-ARXIV-2606-26590; review:SF-2026-ARXIV-2606-26607; review:SF-2026-ARXIV-2606-26631; review:SF-2026-ARXIV-2606-26633; review:SF-2026-ARXIV-2606-26649; review:SF-2026-ARXIV-2606-26664; review:SF-2026-ARXIV-2606-26666; review:SF-2026-ARXIV-2606-26669; review:SF-2026-ARXIV-2606-26686; review:SF-2026-ARXIV-2606-26721; review:SF-2026-ARXIV-2606-26744; review:SF-2026-ARXIV-2606-26753; review:SF-2026-ARXIV-2606-26758; review:SF-2026-ARXIV-2606-26762; review:SF-2026-ARXIV-2606-26790; review:SF-2026-ARXIV-2606-26793; review:SF-2026-ARXIV-2606-26806; review:SF-2026-ARXIV-2606-26836; review:SF-2026-ARXIV-2606-26859; review:SF-2026-ARXIV-2606-26875; review:SF-2026-ARXIV-2606-26904; review:SF-2026-ARXIV-2606-26917; review:SF-2026-ARXIV-2606-26918; review:SF-2026-ARXIV-2606-26924; review:SF-2026-ARXIV-2606-26933; review:SF-2026-ARXIV-2606-26935; review:SF-2026-ARXIV-2606-26960; review:SF-2026-ARXIV-2606-26978; review:SF-2026-ARXIV-2606-26979; review:SF-2026-ARXIV-2606-26990; review:SF-2026-ARXIV-2606-26997; review:SF-2026-ARXIV-2606-27005; review:SF-2026-ARXIV-2606-27009; review:SF-2026-ARXIV-2606-27027; review:SF-2026-ARXIV-2606-27045; review:SF-2026-ARXIV-2606-27079; review:SF-2026-ARXIV-2606-27091; review:SF-2026-ARXIV-2606-27136; review:SF-2026-ARXIV-2606-27146; review:SF-2026-ARXIV-2606-27153; review:SF-2026-ARXIV-2606-27154; review:SF-2026-ARXIV-2606-27188; review:SF-2026-ARXIV-2606-27205; review:SF-2026-ARXIV-2606-27210; review:SF-2026-ARXIV-2606-27226; review:SF-2026-ARXIV-2606-27242; review:SF-2026-ARXIV-2606-27243; review:SF-2026-ARXIV-2606-27251; review:SF-2026-ARXIV-2606-27268; review:SF-2026-ARXIV-2606-27288; review:SF-2026-ARXIV-2606-27326; review:SF-2026-ARXIV-2606-27330; review:SF-2026-ARXIV-2606-27350; review:SF-2026-ARXIV-2606-27355; review:SF-2026-ARXIV-2606-27359; review:SF-2026-ARXIV-2606-27369; review:SF-2026-ARXIV-2606-27374; review:SF-2026-ARXIV-2606-27375 | EVIDENCE-OWNER-REBUILD-20260626: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260626-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-26156; analysis-decision:SF-2026-ARXIV-2606-26185; analysis-decision:SF-2026-ARXIV-2606-26211; analysis-decision:SF-2026-ARXIV-2606-26257; analysis-decision:SF-2026-ARXIV-2606-26298; analysis-decision:SF-2026-ARXIV-2606-26300; analysis-decision:SF-2026-ARXIV-2606-26341; analysis-decision:SF-2026-ARXIV-2606-26344; analysis-decision:SF-2026-ARXIV-2606-26356; analysis-decision:SF-2026-ARXIV-2606-26377; analysis-decision:SF-2026-ARXIV-2606-26383; analysis-decision:SF-2026-ARXIV-2606-26429; analysis-decision:SF-2026-ARXIV-2606-26439; analysis-decision:SF-2026-ARXIV-2606-26441; analysis-decision:SF-2026-ARXIV-2606-26442; analysis-decision:SF-2026-ARXIV-2606-26449; analysis-decision:SF-2026-ARXIV-2606-26453; analysis-decision:SF-2026-ARXIV-2606-26456; analysis-decision:SF-2026-ARXIV-2606-26463; analysis-decision:SF-2026-ARXIV-2606-26472; analysis-decision:SF-2026-ARXIV-2606-26479; analysis-decision:SF-2026-ARXIV-2606-26488; analysis-decision:SF-2026-ARXIV-2606-26492; analysis-decision:SF-2026-ARXIV-2606-26511; analysis:DA-20260626-VIGIL-RUNTIME-ENFORCEMENT; analysis-decision:SF-2026-ARXIV-2606-26529; analysis-decision:SF-2026-ARXIV-2606-26587; analysis-decision:SF-2026-ARXIV-2606-26590; analysis:DA-20260626-MOEBIUS-RUNTIME-PARALLELISM; analysis-decision:SF-2026-ARXIV-2606-26631; analysis-decision:SF-2026-ARXIV-2606-26633; analysis-decision:SF-2026-ARXIV-2606-26649; analysis-decision:SF-2026-ARXIV-2606-26664; analysis-decision:SF-2026-ARXIV-2606-26666; analysis-decision:SF-2026-ARXIV-2606-26669; analysis-decision:SF-2026-ARXIV-2606-26686; analysis-decision:SF-2026-ARXIV-2606-26721; analysis-decision:SF-2026-ARXIV-2606-26744; analysis-decision:SF-2026-ARXIV-2606-26753; analysis-decision:SF-2026-ARXIV-2606-26758; analysis-decision:SF-2026-ARXIV-2606-26762; analysis-decision:SF-2026-ARXIV-2606-26790; analysis-decision:SF-2026-ARXIV-2606-26793; analysis-decision:SF-2026-ARXIV-2606-26806; analysis-decision:SF-2026-ARXIV-2606-26836; analysis-decision:SF-2026-ARXIV-2606-26859; analysis-decision:SF-2026-ARXIV-2606-26875; analysis-decision:SF-2026-ARXIV-2606-26904; analysis-decision:SF-2026-ARXIV-2606-26917; analysis-decision:SF-2026-ARXIV-2606-26918; analysis-decision:SF-2026-ARXIV-2606-26924; analysis-decision:SF-2026-ARXIV-2606-26933; analysis-decision:SF-2026-ARXIV-2606-26935; analysis-decision:SF-2026-ARXIV-2606-26960; analysis-decision:SF-2026-ARXIV-2606-26978; analysis-decision:SF-2026-ARXIV-2606-26979; analysis-decision:SF-2026-ARXIV-2606-26990; analysis-decision:SF-2026-ARXIV-2606-26997; analysis-decision:SF-2026-ARXIV-2606-27005; analysis-decision:SF-2026-ARXIV-2606-27009; analysis-decision:SF-2026-ARXIV-2606-27027; analysis-decision:SF-2026-ARXIV-2606-27045; analysis-decision:SF-2026-ARXIV-2606-27079; analysis-decision:SF-2026-ARXIV-2606-27091; analysis-decision:SF-2026-ARXIV-2606-27136; analysis-decision:SF-2026-ARXIV-2606-27146; analysis-decision:SF-2026-ARXIV-2606-27153; analysis-decision:SF-2026-ARXIV-2606-27154; analysis-decision:SF-2026-ARXIV-2606-27188; analysis-decision:SF-2026-ARXIV-2606-27205; analysis-decision:SF-2026-ARXIV-2606-27210; analysis-decision:SF-2026-ARXIV-2606-27226; analysis-decision:SF-2026-ARXIV-2606-27242; analysis-decision:SF-2026-ARXIV-2606-27243; analysis:DA-20260626-OMNIACT-CLOSED-LOOP; analysis-decision:SF-2026-ARXIV-2606-27268; analysis-decision:SF-2026-ARXIV-2606-27288; analysis-decision:SF-2026-ARXIV-2606-27326; analysis-decision:SF-2026-ARXIV-2606-27330; analysis-decision:SF-2026-ARXIV-2606-27350; analysis-decision:SF-2026-ARXIV-2606-27355; analysis-decision:SF-2026-ARXIV-2606-27359; analysis-decision:SF-2026-ARXIV-2606-27369; analysis-decision:SF-2026-ARXIV-2606-27374; analysis-decision:SF-2026-ARXIV-2606-27375 | SELECTION-OWNER-REBUILD-20260626: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260626-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-26156; books-review:SF-2026-ARXIV-2606-26185; books-review:SF-2026-ARXIV-2606-26211; books-review:SF-2026-ARXIV-2606-26257; books-review:SF-2026-ARXIV-2606-26298; books-review:SF-2026-ARXIV-2606-26300; books-review:SF-2026-ARXIV-2606-26341; books-review:SF-2026-ARXIV-2606-26344; books-review:SF-2026-ARXIV-2606-26356; books-review:SF-2026-ARXIV-2606-26377; books-review:SF-2026-ARXIV-2606-26383; books-review:SF-2026-ARXIV-2606-26429; books-review:SF-2026-ARXIV-2606-26439; books-review:SF-2026-ARXIV-2606-26441; books-review:SF-2026-ARXIV-2606-26442; books-review:SF-2026-ARXIV-2606-26449; books-review:SF-2026-ARXIV-2606-26453; books-review:SF-2026-ARXIV-2606-26456; books-review:SF-2026-ARXIV-2606-26463; books-review:SF-2026-ARXIV-2606-26472; books-review:SF-2026-ARXIV-2606-26479; books-review:SF-2026-ARXIV-2606-26488; books-review:SF-2026-ARXIV-2606-26492; books-review:SF-2026-ARXIV-2606-26511; books-review:SF-2026-ARXIV-2606-26524; books-review:SF-2026-ARXIV-2606-26590; books-review:SF-2026-ARXIV-2606-26607; books-review:SF-2026-ARXIV-2606-26631; books-review:SF-2026-ARXIV-2606-26649; books-review:SF-2026-ARXIV-2606-26721; books-review:SF-2026-ARXIV-2606-26753; books-review:SF-2026-ARXIV-2606-26793; books-review:SF-2026-ARXIV-2606-26806; books-review:SF-2026-ARXIV-2606-26836; books-review:SF-2026-ARXIV-2606-26875; books-review:SF-2026-ARXIV-2606-26924; books-review:SF-2026-ARXIV-2606-26935; books-review:SF-2026-ARXIV-2606-26979; books-review:SF-2026-ARXIV-2606-26990; books-review:SF-2026-ARXIV-2606-26997; books-review:SF-2026-ARXIV-2606-27009; books-review:SF-2026-ARXIV-2606-27027; books-review:SF-2026-ARXIV-2606-27045; books-review:SF-2026-ARXIV-2606-27079; books-review:SF-2026-ARXIV-2606-27091; books-review:SF-2026-ARXIV-2606-27146; books-review:SF-2026-ARXIV-2606-27153; books-review:SF-2026-ARXIV-2606-27154; books-review:SF-2026-ARXIV-2606-27188; books-review:SF-2026-ARXIV-2606-27226; books-review:SF-2026-ARXIV-2606-27251; books-review:SF-2026-ARXIV-2606-27288; books-review:SF-2026-ARXIV-2606-27326; books-review:SF-2026-ARXIV-2606-27355 | BOOKS-OWNER-REBUILD-20260626: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- 84/84 exact-v1 identities resolved: 83 official arXiv HTML and one official v1 PDF fallback for 2606.27251; no mirror or later revision used.
- Ordinary pending locator count: 0.

## 9. Recommended Action

- Integrate: root wrote 7/7 exact-v1 Review notes and 6/6 owner-merged narratives; post-write semantic audit passed.
- No Change — Existing Coverage: 33/33 canonical propositions and boundaries were revalidated.
- Weekly Only — Context: 44/44 context boundaries were revalidated without accidental Books writes.
- Recalibration: 59 / 25 / 0 became 7 / 33 / 44 after reopening every current owner and adjacent chapter.
- Post-write fresh audit: 84/84 Passed, zero unresolved finding; Completion Complete.

## 10. Repository Changes

- Added only the 2026-06-26 Daily, date-local source packet and scripts/finalize_june26_v21.py.
- Root serialized shared Books. This lane audited them and changed only date-local files; it did not edit, stage, commit or push Books or docs/LEARNING_STATE.md.

## 11. Open Questions

- VIGIL 的 specification completeness 如何独立验证，避免 monitor 严格执行错误策略？
- Moebius 的 EP/TP switch threshold 如何与 tail latency、memory pressure 和 rollback 共同验收？
- OmniAct 的异步视觉 preemption latency window 如何进入物理安全 envelope 与人工接管策略？

## 12. Sources

- [Kiko: Programming Agents to Enact Interaction Protocols](https://arxiv.org/abs/2606.26156v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations](https://arxiv.org/abs/2606.26185v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem](https://arxiv.org/abs/2606.26211v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Dataset Usage Inference without Shadow Models or Held-out Data](https://arxiv.org/abs/2606.26257v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems](https://arxiv.org/abs/2606.26298v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [The Verification Horizon: No Silver Bullet for Coding Agent Rewards](https://arxiv.org/abs/2606.26300v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Scaling Nonlinear Optimization: Many Problems One GPU](https://arxiv.org/abs/2606.26341v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Axon: A Synthesizing Superoptimizer for Tensor Programs](https://arxiv.org/abs/2606.26344v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems](https://arxiv.org/abs/2606.26356v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats](https://arxiv.org/abs/2606.26377v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [SOLAR: AI-Powered Speed-of-Light Performance Analysis](https://arxiv.org/abs/2606.26383v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [DualEval: Joint Model-Item Calibration for Unified LLM Evaluation](https://arxiv.org/abs/2606.26429v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization](https://arxiv.org/abs/2606.26439v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices](https://arxiv.org/abs/2606.26441v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities](https://arxiv.org/abs/2606.26442v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [ProvenAI: Provenance-Native Traces of Evidence in Generated Answers](https://arxiv.org/abs/2606.26449v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization](https://arxiv.org/abs/2606.26453v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Towards Safety-Aware Mutation Testing for Autonomous Driving Systems](https://arxiv.org/abs/2606.26456v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Finding the Time to Think: Learning Planning Budgets in Real-Time RL](https://arxiv.org/abs/2606.26463v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Epiphany-Aware KV Cache Eviction Without the Attention Matrix](https://arxiv.org/abs/2606.26472v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [What Survives When You Compress a Recursive Reasoner for the Edge?](https://arxiv.org/abs/2606.26488v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs](https://arxiv.org/abs/2606.26492v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge](https://arxiv.org/abs/2606.26511v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills](https://arxiv.org/abs/2606.26524v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [The inattentional gap in task conditioned AI models that omit otherwise reportable safety critical signals](https://arxiv.org/abs/2606.26529v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference](https://arxiv.org/abs/2606.26587v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform](https://arxiv.org/abs/2606.26590v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch](https://arxiv.org/abs/2606.26607v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning](https://arxiv.org/abs/2606.26631v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Simulating Unified Tensor Resharding in heterogeneous AI systems](https://arxiv.org/abs/2606.26633v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems](https://arxiv.org/abs/2606.26664v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs](https://arxiv.org/abs/2606.26666v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills](https://arxiv.org/abs/2606.26669v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation](https://arxiv.org/abs/2606.26686v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration](https://arxiv.org/abs/2606.26721v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction](https://arxiv.org/abs/2606.26744v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification](https://arxiv.org/abs/2606.26753v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [EGG: An Expert-Guided Agent Framework for Kernel Generation](https://arxiv.org/abs/2606.26758v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory](https://arxiv.org/abs/2606.26762v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.26790v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG](https://arxiv.org/abs/2606.26793v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents](https://arxiv.org/abs/2606.26806v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [The Capability Frontier: Benchmarks Miss 82% of Model Performance](https://arxiv.org/abs/2606.26836v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems](https://arxiv.org/abs/2606.26859v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Information-Aware KV Cache Compression for Long Reasoning](https://arxiv.org/abs/2606.26875v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Confidence-Aware Tool Orchestration for Robust Video Understanding](https://arxiv.org/abs/2606.26904v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning](https://arxiv.org/abs/2606.26917v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Diagnosing Task Insensitivity in Language Agents](https://arxiv.org/abs/2606.26918v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/abs/2606.26924v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities](https://arxiv.org/abs/2606.26933v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Where Do CoT Training Gains Land in LLM based Agents?](https://arxiv.org/abs/2606.26935v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Toward Agentic SysAdmin: Rethinking System Administration with AI Agents](https://arxiv.org/abs/2606.26960v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair](https://arxiv.org/abs/2606.26978v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring](https://arxiv.org/abs/2606.26979v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Decision-Aligned Evaluation of Uncertainty Quantification](https://arxiv.org/abs/2606.26990v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning](https://arxiv.org/abs/2606.26997v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI)](https://arxiv.org/abs/2606.27005v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Semantic Early-Stopping for Iterative LLM Agent Loops](https://arxiv.org/abs/2606.27009v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP](https://arxiv.org/abs/2606.27027v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development](https://arxiv.org/abs/2606.27045v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation](https://arxiv.org/abs/2606.27091v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Joint Learning of Experiential Rules and Policies for Large Language Model Agents](https://arxiv.org/abs/2606.27136v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies](https://arxiv.org/abs/2606.27146v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [DMuon: Efficient Distributed Muon Training with Near-Adam Overhead](https://arxiv.org/abs/2606.27153v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [OpenRCA 2.0: From Outcome Labels to Causal Process Supervision](https://arxiv.org/abs/2606.27154v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO](https://arxiv.org/abs/2606.27188v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair](https://arxiv.org/abs/2606.27205v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes](https://arxiv.org/abs/2606.27210v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement](https://arxiv.org/abs/2606.27226v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [The Geometry of Updates: Fisher Alignment at Vocabulary Scale](https://arxiv.org/abs/2606.27242v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems](https://arxiv.org/abs/2606.27243v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy](https://arxiv.org/abs/2606.27251v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation](https://arxiv.org/abs/2606.27268v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models](https://arxiv.org/abs/2606.27288v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning](https://arxiv.org/abs/2606.27330v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [CHIA: An open-source framework for principled, agentic AI-driven hardware/software co-design research](https://arxiv.org/abs/2606.27350v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools](https://arxiv.org/abs/2606.27355v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [When are likely answers right? On Sequence Probability and Correctness in LLMs](https://arxiv.org/abs/2606.27359v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Reinforcement Learning without Ground-Truth Solutions can Improve LLMs](https://arxiv.org/abs/2606.27369v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays](https://arxiv.org/abs/2606.27374v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
- [Scalable Behavior Cloning with Open Data, Training, and Evaluation](https://arxiv.org/abs/2606.27375v1) — first-public（Asia/Shanghai）：2026-06-26；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=1。
