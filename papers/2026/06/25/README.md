# Daily Research — 2026-06-25

**Research Date:** 2026-06-25

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-24 09:00:00 ～ 2026-06-25 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
Beijing window `[2026-06-24 09:00, 2026-06-25 09:00)` contains 510 registered identities. Full 510/510 semantic screening freezes 68 durable families and 442 family-specific closures. Route-negative audit is 127/127 with four promotions. Exact-v1 Evidence is 68/68 and full-frontier Selection chose three narratives. The 68/68 post-write fresh audit verified 63 unique-owner integrations plus five absent No Change families with zero unresolved finding.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-25 |
| Window End | 2026-06-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-25:9dcf324622a37ab5 |
| Denominator Frozen At | 2026-08-29T14:30:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-24T09:00:00+08:00 | 2026-06-25T09:00:00+08:00 | 2026-08-29T14:30:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 526 | SF-2026-ARXIV-2606-24898;SF-2026-ARXIV-2606-24934;SF-2026-ARXIV-2606-24957;SF-2026-ARXIV-2606-24996;SF-2026-ARXIV-2606-24998;SF-2026-ARXIV-2606-25040;SF-2026-ARXIV-2606-25082;SF-2026-ARXIV-2606-25091;SF-2026-ARXIV-2606-25097;SF-2026-ARXIV-2606-25098;SF-2026-ARXIV-2606-25115;SF-2026-ARXIV-2606-25156;SF-2026-ARXIV-2606-25161;SF-2026-ARXIV-2606-25178;SF-2026-ARXIV-2606-25189;SF-2026-ARXIV-2606-25191;SF-2026-ARXIV-2606-25198;SF-2026-ARXIV-2606-25207;SF-2026-ARXIV-2606-25215;SF-2026-ARXIV-2606-25274;SF-2026-ARXIV-2606-25285;SF-2026-ARXIV-2606-25296;SF-2026-ARXIV-2606-25342;SF-2026-ARXIV-2606-25349;SF-2026-ARXIV-2606-25353;SF-2026-ARXIV-2606-25366;SF-2026-ARXIV-2606-25371;SF-2026-ARXIV-2606-25388;SF-2026-ARXIV-2606-25410;SF-2026-ARXIV-2606-25426;SF-2026-ARXIV-2606-25447;SF-2026-ARXIV-2606-25449;SF-2026-ARXIV-2606-25453;SF-2026-ARXIV-2606-25467;SF-2026-ARXIV-2606-25487;SF-2026-ARXIV-2606-25514;SF-2026-ARXIV-2606-25519;SF-2026-ARXIV-2606-25532;SF-2026-ARXIV-2606-25548;SF-2026-ARXIV-2606-25575;SF-2026-ARXIV-2606-25592;SF-2026-ARXIV-2606-25605;SF-2026-ARXIV-2606-25608;SF-2026-ARXIV-2606-25622;SF-2026-ARXIV-2606-25656;SF-2026-ARXIV-2606-25658;SF-2026-ARXIV-2606-25674;SF-2026-ARXIV-2606-25700;SF-2026-ARXIV-2606-25705;SF-2026-ARXIV-2606-25721;SF-2026-ARXIV-2606-25759;SF-2026-ARXIV-2606-25760;SF-2026-ARXIV-2606-25782;SF-2026-ARXIV-2606-25797;SF-2026-ARXIV-2606-25819;SF-2026-ARXIV-2606-25838;SF-2026-ARXIV-2606-25863;SF-2026-ARXIV-2606-25871;SF-2026-ARXIV-2606-25987;SF-2026-ARXIV-2606-25996;SF-2026-ARXIV-2606-26021;SF-2026-ARXIV-2606-26027;SF-2026-ARXIV-2606-26028;SF-2026-ARXIV-2606-26057;SF-2026-ARXIV-2606-26071 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260625/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260625; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260625 |
<!-- coverage:SRC-ARXIV:20260625:start -->
All 321 Core, 62 keyword-routed and 127 route-negative identities were screened. Frozen arithmetic: `510 = 68 retained + 442 closures`; keyword routing was recall-only; route-negative FN=`2606.25467, 2606.25575, 2606.25592, 2606.26456`.
<!-- coverage:SRC-ARXIV:20260625:end -->


<!-- latest-contract-reopen:2026-06-25:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-25:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **526** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **65** 条是旧报告 retained provenance，**461** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-24898 | arXiv:2606.24898v1 | paper-v1:2606.24898 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24898 | self | — | new_in_window | MODEL-DECODER-ONLY | Integrate | books-review:SF-2026-ARXIV-2606-24898 | yes |
| SF-2026-ARXIV-2606-24934 | arXiv:2606.24934v1 | paper-v1:2606.24934 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24934 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24934 | yes |
| SF-2026-ARXIV-2606-24957 | arXiv:2606.24957v1 | paper-v1:2606.24957 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24957 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-24957 | yes |
| SF-2026-ARXIV-2606-24996 | arXiv:2606.24996v1 | paper-v1:2606.24996 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24996 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-24996 | yes |
| SF-2026-ARXIV-2606-24998 | arXiv:2606.24998v1 | paper-v1:2606.24998 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24998 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-24998 | yes |
| SF-2026-ARXIV-2606-25040 | arXiv:2606.25040v1 | paper-v1:2606.25040 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25040 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-25040 | yes |
| SF-2026-ARXIV-2606-25082 | arXiv:2606.25082v1 | paper-v1:2606.25082 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25082 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2606-25082 | yes |
| SF-2026-ARXIV-2606-25091 | arXiv:2606.25091v1 | paper-v1:2606.25091 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25091 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-25091 | yes |
| SF-2026-ARXIV-2606-25097 | arXiv:2606.25097v1 | paper-v1:2606.25097 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25097 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-25097 | yes |
| SF-2026-ARXIV-2606-25098 | arXiv:2606.25098v1 | paper-v1:2606.25098 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25098 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2606-25098 | yes |
| SF-2026-ARXIV-2606-25115 | arXiv:2606.25115v1 | paper-v1:2606.25115 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25115 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25115 | yes |
| SF-2026-ARXIV-2606-25156 | arXiv:2606.25156v1 | paper-v1:2606.25156 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25156 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-25156 | yes |
| SF-2026-ARXIV-2606-25161 | arXiv:2606.25161v1 | paper-v1:2606.25161 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25161 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25161 | yes |
| SF-2026-ARXIV-2606-25178 | arXiv:2606.25178v1 | paper-v1:2606.25178 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25178 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-25178 | yes |
| SF-2026-ARXIV-2606-25189 | arXiv:2606.25189v1 | paper-v1:2606.25189 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25189 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25189 | yes |
| SF-2026-ARXIV-2606-25191 | arXiv:2606.25191v1 | paper-v1:2606.25191 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25191 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-25191 | yes |
| SF-2026-ARXIV-2606-25198 | arXiv:2606.25198v1 | paper-v1:2606.25198 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25198 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-25198 | yes |
| SF-2026-ARXIV-2606-25207 | arXiv:2606.25207v1 | paper-v1:2606.25207 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25207 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-25207 | yes |
| SF-2026-ARXIV-2606-25215 | arXiv:2606.25215v1 | paper-v1:2606.25215 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25215 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-25215 | yes |
| SF-2026-ARXIV-2606-25274 | arXiv:2606.25274v1 | paper-v1:2606.25274 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25274 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-25274 | yes |
| SF-2026-ARXIV-2606-25285 | arXiv:2606.25285v1 | paper-v1:2606.25285 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25285 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25285 | yes |
| SF-2026-ARXIV-2606-25296 | arXiv:2606.25296v1 | paper-v1:2606.25296 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25296 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25296 | yes |
| SF-2026-ARXIV-2606-25342 | arXiv:2606.25342v1 | paper-v1:2606.25342 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25342 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-25342 | yes |
| SF-2026-ARXIV-2606-25349 | arXiv:2606.25349v1 | paper-v1:2606.25349 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25349 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25349 | yes |
| SF-2026-ARXIV-2606-25353 | arXiv:2606.25353v1 | paper-v1:2606.25353 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25353 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2606-25353 | yes |
| SF-2026-ARXIV-2606-25366 | arXiv:2606.25366v1 | paper-v1:2606.25366 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25366 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25366 | yes |
| SF-2026-ARXIV-2606-25371 | arXiv:2606.25371v1 | paper-v1:2606.25371 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25371 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25371 | yes |
| SF-2026-ARXIV-2606-25388 | arXiv:2606.25388v1 | paper-v1:2606.25388 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25388 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-25388 | yes |
| SF-2026-ARXIV-2606-25410 | arXiv:2606.25410v1 | paper-v1:2606.25410 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25410 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25410 | yes |
| SF-2026-ARXIV-2606-25426 | arXiv:2606.25426v1 | paper-v1:2606.25426 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25426 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2606-25426 | yes |
| SF-2026-ARXIV-2606-25447 | arXiv:2606.25447v1 | paper-v1:2606.25447 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25447 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-25447 | yes |
| SF-2026-ARXIV-2606-25449 | arXiv:2606.25449v1 | paper-v1:2606.25449 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25449 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25449 | yes |
| SF-2026-ARXIV-2606-25453 | arXiv:2606.25453v1 | paper-v1:2606.25453 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25453 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-25453 | yes |
| SF-2026-ARXIV-2606-25467 | arXiv:2606.25467v1 | paper-v1:2606.25467 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25467 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-25467 | yes |
| SF-2026-ARXIV-2606-25487 | arXiv:2606.25487v1 | paper-v1:2606.25487 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25487 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25487 | yes |
| SF-2026-ARXIV-2606-25514 | arXiv:2606.25514v1 | paper-v1:2606.25514 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25514 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-25514 | yes |
| SF-2026-ARXIV-2606-25519 | arXiv:2606.25519v1 | paper-v1:2606.25519 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25519 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25519 | yes |
| SF-2026-ARXIV-2606-25532 | arXiv:2606.25532v1 | paper-v1:2606.25532 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25532 | self | — | new_in_window | PLATFORM-FOUNDATIONS | Integrate | books-review:SF-2026-ARXIV-2606-25532 | yes |
| SF-2026-ARXIV-2606-25548 | arXiv:2606.25548v1 | paper-v1:2606.25548 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25548 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25548 | yes |
| SF-2026-ARXIV-2606-25575 | arXiv:2606.25575v1 | paper-v1:2606.25575 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25575 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-25575 | yes |
| SF-2026-ARXIV-2606-25592 | arXiv:2606.25592v1 | paper-v1:2606.25592 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25592 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25592 | yes |
| SF-2026-ARXIV-2606-25605 | arXiv:2606.25605v1 | paper-v1:2606.25605 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25605 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25605 | yes |
| SF-2026-ARXIV-2606-25608 | arXiv:2606.25608v1 | paper-v1:2606.25608 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25608 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25608 | yes |
| SF-2026-ARXIV-2606-25622 | arXiv:2606.25622v1 | paper-v1:2606.25622 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25622 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25622 | yes |
| SF-2026-ARXIV-2606-25656 | arXiv:2606.25656v1 | paper-v1:2606.25656 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25656 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-25656 | yes |
| SF-2026-ARXIV-2606-25658 | arXiv:2606.25658v1 | paper-v1:2606.25658 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25658 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-25658 | yes |
| SF-2026-ARXIV-2606-25674 | arXiv:2606.25674v1 | paper-v1:2606.25674 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25674 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-25674 | yes |
| SF-2026-ARXIV-2606-25700 | arXiv:2606.25700v1 | paper-v1:2606.25700 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25700 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25700 | yes |
| SF-2026-ARXIV-2606-25705 | arXiv:2606.25705v1 | paper-v1:2606.25705 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25705 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25705 | yes |
| SF-2026-ARXIV-2606-25721 | arXiv:2606.25721v1 | paper-v1:2606.25721 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25721 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25721 | yes |
| SF-2026-ARXIV-2606-25759 | arXiv:2606.25759v1 | paper-v1:2606.25759 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25759 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-25759 | yes |
| SF-2026-ARXIV-2606-25760 | arXiv:2606.25760v1 | paper-v1:2606.25760 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25760 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25760 | yes |
| SF-2026-ARXIV-2606-25782 | arXiv:2606.25782v1 | paper-v1:2606.25782 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25782 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-25782 | yes |
| SF-2026-ARXIV-2606-25797 | arXiv:2606.25797v1 | paper-v1:2606.25797 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25797 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25797 | yes |
| SF-2026-ARXIV-2606-25819 | arXiv:2606.25819v1 | paper-v1:2606.25819 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25819 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25819 | yes |
| SF-2026-ARXIV-2606-25838 | arXiv:2606.25838v1 | paper-v1:2606.25838 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25838 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-25838 | yes |
| SF-2026-ARXIV-2606-25863 | arXiv:2606.25863v1 | paper-v1:2606.25863 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25863 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-25863 | yes |
| SF-2026-ARXIV-2606-25871 | arXiv:2606.25871v1 | paper-v1:2606.25871 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25871 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-25871 | yes |
| SF-2026-ARXIV-2606-25987 | arXiv:2606.25987v1 | paper-v1:2606.25987 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25987 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-25987 | yes |
| SF-2026-ARXIV-2606-25996 | arXiv:2606.25996v1 | paper-v1:2606.25996 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-25996 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-25996 | yes |
| SF-2026-ARXIV-2606-26021 | arXiv:2606.26021v1 | paper-v1:2606.26021 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26021 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26021 | yes |
| SF-2026-ARXIV-2606-26027 | arXiv:2606.26027v1 | paper-v1:2606.26027 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26027 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-26027 | yes |
| SF-2026-ARXIV-2606-26028 | arXiv:2606.26028v1 | paper-v1:2606.26028 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26028 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26028 | yes |
| SF-2026-ARXIV-2606-26057 | arXiv:2606.26057v1 | paper-v1:2606.26057 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26057 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-26057 | yes |
| SF-2026-ARXIV-2606-26071 | arXiv:2606.26071v1 | paper-v1:2606.26071 | 2026-W26 | 2026-06-25 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-26071 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-26071 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-24898 | RP-247046f613f95f9c | deep | arXiv:2606.24898v1 | SRC-ARXIV@arXiv:2606.24898v1 | https://arxiv.org/html/2606.24898v1 — § exact-v1 anchor: readout blind spot | https://arxiv.org/html/2606.24898v1 — § exact-v1 evaluation anchor: 44M and 129M looped transformers | https://arxiv.org/html/2606.24898v1 — § exact-v1 limitation/counterevidence anchor: without inter-loop normalization | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24898 | complete |
| SF-2026-ARXIV-2606-24934 | RP-bf21f45e43aad532 | deep | arXiv:2606.24934v1 | SRC-ARXIV@arXiv:2606.24934v1 | arXiv:2606.24934v1 — §3 Attestation Model; §4 GPU Probe; §11 Packaging | arXiv:2606.24934v1 — §5 Certificate Stability Under Load; §6 Cross-Die Fingerprint Attestation; §7–§10 Attestation experiments | arXiv:2606.24934v1 — §12 Limitations; §13 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24934 | complete |
| SF-2026-ARXIV-2606-24957 | RP-550c481483e91d58 | deep | arXiv:2606.24957v1 | SRC-ARXIV@arXiv:2606.24957v1 | https://arxiv.org/html/2606.24957v1 — §3 Observation; 4 Dustin Sparse Verification | https://arxiv.org/html/2606.24957v1 — §5 Experiment; Accuracy and End-to-End Decode Throughput | https://arxiv.org/html/2606.24957v1 — §L Limitations; I Porting Overhead | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24957 | complete |
| SF-2026-ARXIV-2606-24996 | RP-c38bcb0bbdc2bf47 | deep | arXiv:2606.24996v1 | SRC-ARXIV@arXiv:2606.24996v1 | https://arxiv.org/html/2606.24996v1 — §2 Results: Two Roles for the Certification Protocol | https://arxiv.org/html/2606.24996v1 — §A Report-Card and Gate Procedure; C/D Robustness Controls | https://arxiv.org/html/2606.24996v1 — §3 Discussion: Limitations and scope; first-failing-gate audit | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24996 | complete |
| SF-2026-ARXIV-2606-24998 | RP-6f66794850f1ca6f | deep | arXiv:2606.24998v1 | SRC-ARXIV@arXiv:2606.24998v1 | https://arxiv.org/html/2606.24998v1 — §3 Methods; Repeated-pool construction | https://arxiv.org/html/2606.24998v1 — §4 Results; F Training and Evaluation Details | https://arxiv.org/html/2606.24998v1 — §H Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24998 | complete |
| SF-2026-ARXIV-2606-25040 | RP-b11681c841c6748e | deep | arXiv:2606.25040v1 | SRC-ARXIV@arXiv:2606.25040v1 | https://arxiv.org/html/2606.25040v1 — §3 Methodology; Sparsity Reuse; Latent Feature Reuse | https://arxiv.org/html/2606.25040v1 — §4 Experiments; Mask Quality and Routing Overhead | https://arxiv.org/html/2606.25040v1 — §5 Conclusion and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25040 | complete |
| SF-2026-ARXIV-2606-25082 | RP-1b9ed6d2cb4b9565 | deep | arXiv:2606.25082v1 | SRC-ARXIV@arXiv:2606.25082v1 | https://arxiv.org/html/2606.25082v1 — §IV Proposed Solution; Scheduling Within Configuration; Dynamic Re-Partitioning | https://arxiv.org/html/2606.25082v1 — §V Experiments and Results | https://arxiv.org/html/2606.25082v1 — §VI Conclusion and Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25082 | complete |
| SF-2026-ARXIV-2606-25091 | RP-88be1165866732bf | deep | arXiv:2606.25091v1 | SRC-ARXIV@arXiv:2606.25091v1 | https://arxiv.org/html/2606.25091v1 — §II Background and Setting; III Gain Window | https://arxiv.org/html/2606.25091v1 — §III-A/B/C comparisons; IV Pipelining | https://arxiv.org/html/2606.25091v1 — §V Conclusion and explicit verifier-interface/RTT boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25091 | complete |
| SF-2026-ARXIV-2606-25097 | RP-8a97dec87bbf7453 | deep | arXiv:2606.25097v1 | SRC-ARXIV@arXiv:2606.25097v1 | https://arxiv.org/html/2606.25097v1 — §3 Methods; Serving-stack Configuration; TAIS Screen | https://arxiv.org/html/2606.25097v1 — §4 Results; E0/E1/E2/E5; B Reproducibility | https://arxiv.org/html/2606.25097v1 — §5.3 Limitations and Threats to Validity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25097 | complete |
| SF-2026-ARXIV-2606-25098 | RP-fa5199e96de64116 | deep | arXiv:2606.25098v1 | SRC-ARXIV@arXiv:2606.25098v1 | https://arxiv.org/html/2606.25098v1 — §3 Architecture for Power-Flexible AI Infrastructure | https://arxiv.org/html/2606.25098v1 — §4 Experimental Demonstration; 5 Grid Services; 6 Geo-Load Shifting | https://arxiv.org/html/2606.25098v1 — §7 Discussion and service-level preservation scope | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25098 | complete |
| SF-2026-ARXIV-2606-25115 | RP-272d88c58cabe601 | deep | arXiv:2606.25115v1 | SRC-ARXIV@arXiv:2606.25115v1 | https://arxiv.org/html/2606.25115v1 — §III System Design; Net-Value-Density; Three Decisions | https://arxiv.org/html/2606.25115v1 — §V Evaluation; Trust Under Poisoning; Real Hardware | https://arxiv.org/html/2606.25115v1 — §VI Related Work and deployment-specific score calibration | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25115 | complete |
| SF-2026-ARXIV-2606-25156 | RP-022a6330b6fee35a | deep | arXiv:2606.25156v1 | SRC-ARXIV@arXiv:2606.25156v1 | https://arxiv.org/html/2606.25156v1 — §3 Methodology; Polar Attention; Gated-Delta Memory | https://arxiv.org/html/2606.25156v1 — §4 Experimental Setup; 5 Results; C Complete Sweep | https://arxiv.org/html/2606.25156v1 — §5.1/5.4 trade-offs and reported 256K FinePDFs failure | https://github.com/kreasof-ai/atma | claim:SF-2026-ARXIV-2606-25156 | complete |
| SF-2026-ARXIV-2606-25161 | RP-79f1a7c366477f95 | deep | arXiv:2606.25161v1 | SRC-ARXIV@arXiv:2606.25161v1 | https://arxiv.org/html/2606.25161v1 — §3 Method; Memory Transition Verifier; Transition-Ranked GRPO | https://arxiv.org/html/2606.25161v1 — §4 Experiment; HaluMem; Reliability of Consolidation | https://arxiv.org/html/2606.25161v1 — §D Memory Transition Error Judge Prompt and evaluated datasets | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25161 | complete |
| SF-2026-ARXIV-2606-25178 | RP-b2faee11d94eafd5 | deep | arXiv:2606.25178v1 | SRC-ARXIV@arXiv:2606.25178v1 | https://arxiv.org/html/2606.25178v1 — §3 Method; Gradient-Based Transferability; Curriculum Algorithm | https://arxiv.org/html/2606.25178v1 — §4 Experiments; B Implementation/Evaluation Details | https://arxiv.org/html/2606.25178v1 — §6 Conclusion: Limitations; C Scaling | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25178 | complete |
| SF-2026-ARXIV-2606-25189 | RP-beca1724bae24dd4 | deep | arXiv:2606.25189v1 | SRC-ARXIV@arXiv:2606.25189v1 | https://arxiv.org/html/2606.25189v1 — §3 Design; Policy DSL; Information-Flow Control | https://arxiv.org/html/2606.25189v1 — §5 Evaluation; Compliance; Macro/Micro Overhead | https://arxiv.org/html/2606.25189v1 — §2.3 Existing Approaches; evaluated policy/harness scope | https://github.com/eunomia-bpf/ActPlane | claim:SF-2026-ARXIV-2606-25189 | complete |
| SF-2026-ARXIV-2606-25191 | RP-81a75f7dc5b6c8ee | deep | arXiv:2606.25191v1 | SRC-ARXIV@arXiv:2606.25191v1 | https://arxiv.org/html/2606.25191v1 — §3 Reasoning-Score Coupling; 4 Candidate Treatments; MADARA | https://arxiv.org/html/2606.25191v1 — §5 Experimental Setup; 6 Results; K Cost-Accuracy | https://arxiv.org/html/2606.25191v1 — §7 Discussion boundaries; D/F calibration sensitivity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25191 | complete |
| SF-2026-ARXIV-2606-25198 | RP-b7a61a308ccedda1 | deep | arXiv:2606.25198v1 | SRC-ARXIV@arXiv:2606.25198v1 | https://arxiv.org/html/2606.25198v1 — §3 Heuresis Framework; search strategies and async parallelism | https://arxiv.org/html/2606.25198v1 — §4 Experiments; 5 Analysis; B Reward Hacking | https://arxiv.org/html/2606.25198v1 — §6.2 Limitations; B.3 Limits of Agentic Verification | https://github.com/a-antoniades/Heuresis | claim:SF-2026-ARXIV-2606-25198 | complete |
| SF-2026-ARXIV-2606-25207 | RP-447b9df601406ea6 | deep | arXiv:2606.25207v1 | SRC-ARXIV@arXiv:2606.25207v1 | https://arxiv.org/html/2606.25207v1 — §3 Agent-Integrated Tools; 4 Agent-System Co-Design | https://arxiv.org/html/2606.25207v1 — §5 Experiments; Wall-Clock Decomposition | https://arxiv.org/html/2606.25207v1 — §7 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25207 | complete |
| SF-2026-ARXIV-2606-25215 | RP-316c969d7b828132 | deep | arXiv:2606.25215v1 | SRC-ARXIV@arXiv:2606.25215v1 | https://arxiv.org/html/2606.25215v1 — §3 Method; Observation-Action-Consequence Context; Block-Causal Training | https://arxiv.org/html/2606.25215v1 — §4 Experiments; C/D Evaluation Protocols | https://arxiv.org/html/2606.25215v1 — §E Reproducibility, Assets, and Limitations | https://lianqing11.github.io/reflective-vla-page/ | claim:SF-2026-ARXIV-2606-25215 | complete |
| SF-2026-ARXIV-2606-25274 | RP-016bcf8aca420eca | deep | arXiv:2606.25274v1 | SRC-ARXIV@arXiv:2606.25274v1 | https://arxiv.org/html/2606.25274v1 — §3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam | https://arxiv.org/html/2606.25274v1 — §5 Experiments; 5.1 Implemented Evidence; 6 Analysis | https://arxiv.org/html/2606.25274v1 — §7 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25274 | complete |
| SF-2026-ARXIV-2606-25285 | RP-af8cc5ec3e0840a1 | deep | arXiv:2606.25285v1 | SRC-ARXIV@arXiv:2606.25285v1 | https://arxiv.org/html/2606.25285v1 — §3 EPTS: Elastic Post-Training Sparsity | https://arxiv.org/html/2606.25285v1 — §4 Experiments; Experimental Setup; Main Results | https://arxiv.org/html/2606.25285v1 — §Limitations and Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25285 | complete |
| SF-2026-ARXIV-2606-25296 | RP-8b2d6ed1f7415f59 | deep | arXiv:2606.25296v1 | SRC-ARXIV@arXiv:2606.25296v1 | https://arxiv.org/html/2606.25296v1 — §SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation | https://arxiv.org/html/2606.25296v1 — §Experimental Evaluation; Functional-Safety Case Studies | https://arxiv.org/html/2606.25296v1 — §Threats to Validity; Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25296 | complete |
| SF-2026-ARXIV-2606-25342 | RP-bfb0ae3361bfc654 | deep | arXiv:2606.25342v1 | SRC-ARXIV@arXiv:2606.25342v1 | https://arxiv.org/html/2606.25342v1 — §Parametric Attention and Lifelong In-Context Learning formulation | https://arxiv.org/html/2606.25342v1 — §Experiments; Lifelong sequence results | https://arxiv.org/html/2606.25342v1 — §Discussion; finite-memory and task-family limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25342 | complete |
| SF-2026-ARXIV-2606-25349 | RP-8195d95a2633e1fd | deep | arXiv:2606.25349v1 | SRC-ARXIV@arXiv:2606.25349v1 | https://arxiv.org/html/2606.25349v1 — §IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation | https://arxiv.org/html/2606.25349v1 — §VII Evaluation | https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25349 | complete |
| SF-2026-ARXIV-2606-25353 | RP-c5e41c6065465ab0 | deep | arXiv:2606.25353v1 | SRC-ARXIV@arXiv:2606.25353v1 | https://arxiv.org/html/2606.25353v1 — §3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation | https://arxiv.org/html/2606.25353v1 — §5 Experiment Setup; 6 Evaluation | https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25353 | complete |
| SF-2026-ARXIV-2606-25366 | RP-12cd3776551d8d3f | deep | arXiv:2606.25366v1 | SRC-ARXIV@arXiv:2606.25366v1 | https://arxiv.org/html/2606.25366v1 — §III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance | https://arxiv.org/html/2606.25366v1 — §VIII Robustness; IX Integrated Evaluation | https://arxiv.org/html/2606.25366v1 — §XI-D Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25366 | complete |
| SF-2026-ARXIV-2606-25371 | RP-892bebb25476d387 | deep | arXiv:2606.25371v1 | SRC-ARXIV@arXiv:2606.25371v1 | https://arxiv.org/html/2606.25371v1 — §III Problem Setup; IV Conformal Recovery-Deadline Certificate | https://arxiv.org/html/2606.25371v1 — §V Experiments | https://arxiv.org/html/2606.25371v1 — §VI-D Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25371 | complete |
| SF-2026-ARXIV-2606-25388 | RP-d70161adcb54fa76 | deep | arXiv:2606.25388v1 | SRC-ARXIV@arXiv:2606.25388v1 | https://arxiv.org/html/2606.25388v1 — §III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control | https://arxiv.org/html/2606.25388v1 — §V Experimental Evaluation; V-A Experimental Setup | https://arxiv.org/html/2606.25388v1 — §VII Discussion and Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25388 | complete |
| SF-2026-ARXIV-2606-25410 | RP-a06733fa049bd38d | deep | arXiv:2606.25410v1 | SRC-ARXIV@arXiv:2606.25410v1 | https://arxiv.org/html/2606.25410v1 — §3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling | https://arxiv.org/html/2606.25410v1 — §4 Experiments; 4.1 Experimental Setup; 4.4 Results | https://arxiv.org/html/2606.25410v1 — §5 Conclusion; class-forgetting experimental scope | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25410 | complete |
| SF-2026-ARXIV-2606-25426 | RP-0552e898756ed601 | deep | arXiv:2606.25426v1 | SRC-ARXIV@arXiv:2606.25426v1 | https://arxiv.org/html/2606.25426v1 — §3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing | https://arxiv.org/html/2606.25426v1 — §4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement | https://arxiv.org/html/2606.25426v1 — §6 Conclusion; Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25426 | complete |
| SF-2026-ARXIV-2606-25447 | RP-f6dfc5ff2438b294 | deep | arXiv:2606.25447v1 | SRC-ARXIV@arXiv:2606.25447v1 | https://arxiv.org/html/2606.25447v1 — §3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type | https://arxiv.org/html/2606.25447v1 — §4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness | https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25447 | complete |
| SF-2026-ARXIV-2606-25449 | RP-78fb62ea4ed5abe1 | deep | arXiv:2606.25449v1 | SRC-ARXIV@arXiv:2606.25449v1 | https://arxiv.org/html/2606.25449v1 — §3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol | https://arxiv.org/html/2606.25449v1 — §4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix | https://arxiv.org/html/2606.25449v1 — §7 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25449 | complete |
| SF-2026-ARXIV-2606-25453 | RP-9e3cce4961c0b96c | deep | arXiv:2606.25453v1 | SRC-ARXIV@arXiv:2606.25453v1 | https://arxiv.org/html/2606.25453v1 — §III EmuGEMM-I; IV EmuGEMM-II | https://arxiv.org/html/2606.25453v1 — §V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off | https://arxiv.org/html/2606.25453v1 — §V-G Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25453 | complete |
| SF-2026-ARXIV-2606-25467 | RP-aec0e13356c5eef8 | deep | arXiv:2606.25467v1 | SRC-ARXIV@arXiv:2606.25467v1 | https://arxiv.org/html/2606.25467v1 — §III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration | https://arxiv.org/html/2606.25467v1 — §V Experimental Evaluation; V-A Experimental Setup | https://arxiv.org/html/2606.25467v1 — §D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25467 | complete |
| SF-2026-ARXIV-2606-25487 | RP-10b4253c673aafd5 | deep | arXiv:2606.25487v1 | SRC-ARXIV@arXiv:2606.25487v1 | https://arxiv.org/html/2606.25487v1 — §3 Setup; Appendix A Prompts, wrappers, and attack configuration | https://arxiv.org/html/2606.25487v1 — §4 Results; 4.1 Calibration against human labels; 4.3 white-box attack | https://arxiv.org/html/2606.25487v1 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25487 | complete |
| SF-2026-ARXIV-2606-25514 | RP-7784341993231506 | deep | arXiv:2606.25514v1 | SRC-ARXIV@arXiv:2606.25514v1 | https://arxiv.org/html/2606.25514v1 — §2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication | https://arxiv.org/html/2606.25514v1 — §3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures | https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25514 | complete |
| SF-2026-ARXIV-2606-25519 | RP-de7e921f96b11cd1 | deep | arXiv:2606.25519v1 | SRC-ARXIV@arXiv:2606.25519v1 | https://arxiv.org/html/2606.25519v1 — §3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy | https://arxiv.org/html/2606.25519v1 — §D Additional evaluation details; D.1 Benchmarks and evaluation protocol | https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25519 | complete |
| SF-2026-ARXIV-2606-25532 | RP-a888d42f1d5133eb | deep | arXiv:2606.25532v1 | SRC-ARXIV@arXiv:2606.25532v1 | https://arxiv.org/html/2606.25532v1 — §Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought | https://arxiv.org/html/2606.25532v1 — §Hardware-compliance evaluation and discovered-system validation | https://arxiv.org/html/2606.25532v1 — §Exact-v1 research-prototype and evaluated hardware-design boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25532 | complete |
| SF-2026-ARXIV-2606-25548 | RP-511e7faf5b6a96de | deep | arXiv:2606.25548v1 | SRC-ARXIV@arXiv:2606.25548v1 | https://arxiv.org/html/2606.25548v1 — §4 Transcoders-based Concept Removal; 4.1 BLOCK Framework | https://arxiv.org/html/2606.25548v1 — §5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness | https://arxiv.org/html/2606.25548v1 — §G Limitations; D.1 Model-Architecture-Dependent Subtleties | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25548 | complete |
| SF-2026-ARXIV-2606-25575 | RP-756a47a3ef188a2d | deep | arXiv:2606.25575v1 | SRC-ARXIV@arXiv:2606.25575v1 | https://arxiv.org/html/2606.25575v1 — §Variable-autonomy architecture; task-phase authority transfer; always-available release gesture | https://arxiv.org/html/2606.25575v1 — §44-participant user study; five bimanual tasks; policy-variant success | https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25575 | complete |
| SF-2026-ARXIV-2606-25592 | RP-0e797107eb2deab0 | deep | arXiv:2606.25592v1 | SRC-ARXIV@arXiv:2606.25592v1 | https://arxiv.org/html/2606.25592v1 — §2 Visual Prompt Attack and Defense; 2.2 VPA-Guard | https://arxiv.org/html/2606.25592v1 — §3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments | https://arxiv.org/html/2606.25592v1 — §E.1 Limitations; E.4 Human-in-the-loop Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25592 | complete |
| SF-2026-ARXIV-2606-25605 | RP-6bf3b401e811ea67 | deep | arXiv:2606.25605v1 | SRC-ARXIV@arXiv:2606.25605v1 | https://arxiv.org/html/2606.25605v1 — §3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution | https://arxiv.org/html/2606.25605v1 — §5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency | https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25605 | complete |
| SF-2026-ARXIV-2606-25608 | RP-50f7baec1957195c | deep | arXiv:2606.25608v1 | SRC-ARXIV@arXiv:2606.25608v1 | https://arxiv.org/html/2606.25608v1 — §V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG | https://arxiv.org/html/2606.25608v1 — §VI Initial Evaluation | https://arxiv.org/html/2606.25608v1 — §V-C Restrictions of our architecture; VII Future Research | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25608 | complete |
| SF-2026-ARXIV-2606-25622 | RP-1672753b6890e9b1 | deep | arXiv:2606.25622v1 | SRC-ARXIV@arXiv:2606.25622v1 | https://arxiv.org/html/2606.25622v1 — §IV Theoretical Framework: MAS Architecture and Experimental Setup | https://arxiv.org/html/2606.25622v1 — §V Results & Discussion | https://arxiv.org/html/2606.25622v1 — §VI Limitations & Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25622 | complete |
| SF-2026-ARXIV-2606-25656 | RP-a8a4288ea1019dad | deep | arXiv:2606.25656v1 | SRC-ARXIV@arXiv:2606.25656v1 | https://arxiv.org/html/2606.25656v1 — §3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization | https://arxiv.org/html/2606.25656v1 — §4 Experimental setup; 5 Experimental results | https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25656 | complete |
| SF-2026-ARXIV-2606-25658 | RP-fc0db43307b98122 | deep | arXiv:2606.25658v1 | SRC-ARXIV@arXiv:2606.25658v1 | https://arxiv.org/html/2606.25658v1 — §3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank | https://arxiv.org/html/2606.25658v1 — §4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation | https://arxiv.org/html/2606.25658v1 — §A Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25658 | complete |
| SF-2026-ARXIV-2606-25674 | RP-512e4777874b68ca | deep | arXiv:2606.25674v1 | SRC-ARXIV@arXiv:2606.25674v1 | https://arxiv.org/html/2606.25674v1 — §3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization | https://arxiv.org/html/2606.25674v1 — §4 Experiments; 4.1 Experimental Setup; B Evaluation Details | https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25674 | complete |
| SF-2026-ARXIV-2606-25700 | RP-60a85adbcc4a5361 | deep | arXiv:2606.25700v1 | SRC-ARXIV@arXiv:2606.25700v1 | https://arxiv.org/html/2606.25700v1 — §III Methods; III-B Training; III-C Architecture | https://arxiv.org/html/2606.25700v1 — §IV Results; IV-B Computation calculation | https://arxiv.org/html/2606.25700v1 — §V Discussion; V-A Choice of rank; V-C Computation | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25700 | complete |
| SF-2026-ARXIV-2606-25705 | RP-8703e249715f19ca | deep | arXiv:2606.25705v1 | SRC-ARXIV@arXiv:2606.25705v1 | https://arxiv.org/html/2606.25705v1 — §3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator | https://arxiv.org/html/2606.25705v1 — §4 Experiments and Results | https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25705 | complete |
| SF-2026-ARXIV-2606-25721 | RP-045fc2758d4f7c34 | deep | arXiv:2606.25721v1 | SRC-ARXIV@arXiv:2606.25721v1 | https://arxiv.org/html/2606.25721v1 — §4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification | https://arxiv.org/html/2606.25721v1 — §5 Evaluation; 5.1 Setup; 5.2 Results | https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25721 | complete |
| SF-2026-ARXIV-2606-25759 | RP-16e55de266034d8f | deep | arXiv:2606.25759v1 | SRC-ARXIV@arXiv:2606.25759v1 | https://arxiv.org/html/2606.25759v1 — §3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing | https://arxiv.org/html/2606.25759v1 — §7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope | https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25759 | complete |
| SF-2026-ARXIV-2606-25760 | RP-9237df1d3b71b376 | deep | arXiv:2606.25760v1 | SRC-ARXIV@arXiv:2606.25760v1 | https://arxiv.org/html/2606.25760v1 — §3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks | https://arxiv.org/html/2606.25760v1 — §4 UQ Generalizes Selectively; 5 Graded Error and Calibration | https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25760 | complete |
| SF-2026-ARXIV-2606-25782 | RP-7b17a11c2c138280 | deep | arXiv:2606.25782v1 | SRC-ARXIV@arXiv:2606.25782v1 | https://arxiv.org/html/2606.25782v1 — §2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel | https://arxiv.org/html/2606.25782v1 — §5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs | https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25782 | complete |
| SF-2026-ARXIV-2606-25797 | RP-43e49516d2f38761 | deep | arXiv:2606.25797v1 | SRC-ARXIV@arXiv:2606.25797v1 | https://arxiv.org/html/2606.25797v1 — §3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC | https://arxiv.org/html/2606.25797v1 — §4 Implementation and Experimental Evaluation | https://arxiv.org/html/2606.25797v1 — §0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25797 | complete |
| SF-2026-ARXIV-2606-25819 | RP-233fd55b344e93ff | deep | arXiv:2606.25819v1 | SRC-ARXIV@arXiv:2606.25819v1 | https://arxiv.org/html/2606.25819v1 — §ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection | https://arxiv.org/html/2606.25819v1 — §Experiments; Experimental Setup; Further Analysis; Error Analysis | https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25819 | complete |
| SF-2026-ARXIV-2606-25838 | RP-a78497f8f1bd3611 | deep | arXiv:2606.25838v1 | SRC-ARXIV@arXiv:2606.25838v1 | https://arxiv.org/html/2606.25838v1 — §III Method; IV Confidence-Aware Routing | https://arxiv.org/html/2606.25838v1 — §V Experiments; V-A Evaluation protocol; VI Deployment Patterns | https://arxiv.org/html/2606.25838v1 — §VII-C Limitations and future work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25838 | complete |
| SF-2026-ARXIV-2606-25863 | RP-32b62b7531d48a0d | deep | arXiv:2606.25863v1 | SRC-ARXIV@arXiv:2606.25863v1 | https://arxiv.org/pdf/2606.25863v1 — §PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution | https://arxiv.org/pdf/2606.25863v1 — §PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches | https://arxiv.org/pdf/2606.25863v1 — §PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25863 | complete |
| SF-2026-ARXIV-2606-25871 | RP-dc28dab74d734629 | deep | arXiv:2606.25871v1 | SRC-ARXIV@arXiv:2606.25871v1 | https://arxiv.org/html/2606.25871v1 — §3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic | https://arxiv.org/html/2606.25871v1 — §4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance | https://arxiv.org/html/2606.25871v1 — §5 Production Deployment and Discussion; sponsored-search relevance boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25871 | complete |
| SF-2026-ARXIV-2606-25987 | RP-eb31acb4bae587ac | deep | arXiv:2606.25987v1 | SRC-ARXIV@arXiv:2606.25987v1 | https://arxiv.org/html/2606.25987v1 — §3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought | https://arxiv.org/html/2606.25987v1 — §5 WoFT Improves Surface Modeling; 5.1 Experimental setup | https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25987 | complete |
| SF-2026-ARXIV-2606-25996 | RP-344dab5093061ed0 | deep | arXiv:2606.25996v1 | SRC-ARXIV@arXiv:2606.25996v1 | https://arxiv.org/html/2606.25996v1 — §2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist | https://arxiv.org/html/2606.25996v1 — §3 Experiments; CS, legal, and scientific reasoning tasks | https://arxiv.org/html/2606.25996v1 — §6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-25996 | complete |
| SF-2026-ARXIV-2606-26021 | RP-428ae67b93cc5415 | deep | arXiv:2606.26021v1 | SRC-ARXIV@arXiv:2606.26021v1 | https://arxiv.org/html/2606.26021v1 — §V Attention-based MIA; VI Inference-Time Hardening Against MIAs | https://arxiv.org/html/2606.26021v1 — §IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results | https://arxiv.org/html/2606.26021v1 — §VIII-C Limitations and opportunities; I Context size | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26021 | complete |
| SF-2026-ARXIV-2606-26027 | RP-bbe015028632c835 | deep | arXiv:2606.26027v1 | SRC-ARXIV@arXiv:2606.26027v1 | https://arxiv.org/html/2606.26027v1 — §4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes | https://arxiv.org/html/2606.26027v1 — §5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation | https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26027 | complete |
| SF-2026-ARXIV-2606-26028 | RP-350a830c5abafdfe | deep | arXiv:2606.26028v1 | SRC-ARXIV@arXiv:2606.26028v1 | https://arxiv.org/html/2606.26028v1 — §3 System Model: ERC-8004 Protocol; 7 Reputation Market Security | https://arxiv.org/html/2606.26028v1 — §4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market | https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26028 | complete |
| SF-2026-ARXIV-2606-26057 | RP-5d0d84a2880f0eca | deep | arXiv:2606.26057v1 | SRC-ARXIV@arXiv:2606.26057v1 | https://arxiv.org/html/2606.26057v1 — §2 Threat Model; 3 Requirements; 4 Design; 5 Implementation | https://arxiv.org/html/2606.26057v1 — §6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment | https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26057 | complete |
| SF-2026-ARXIV-2606-26071 | RP-c205d94ba3531c8c | deep | arXiv:2606.26071v1 | SRC-ARXIV@arXiv:2606.26071v1 | https://arxiv.org/html/2606.26071v1 — §4 Protocol and Methods; 5 Environments; 7 Methodological Insights | https://arxiv.org/html/2606.26071v1 — §6 Case Studies; 8 Recommendations | https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-26071 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-24898:start -->
### 2606.24898 — Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models

**问题与旧路径。** `Looped language models turn hidden states into runtime state: each state is decoded for prediction and fed back into future computation.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Looped LM 的dense per-loop cross-entropy只控制readout可见变量；RMSNorm/LayerNorm隐藏radial scale时，recurrent residual仍携带scale，必须让scale对loss可见或从recurrence移除。 Authoritative owner 是 `MODEL-DECODER-ONLY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 44M与129M looped transformers；无inter-loop normalization时norm升至数千/数万，scale-visible readout、norm penalty或scale-removing recurrence保持在数十。 Method locator：`https://arxiv.org/html/2606.24898v1 — § exact-v1 anchor: readout blind spot`。Evaluation locator：`https://arxiv.org/html/2606.24898v1 — § exact-v1 evaluation anchor: 44M and 129M looped transformers`。Benchmark identity：model=`44M- and 129M-parameter looped transformers`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Per-loop cross-entropy plus hidden-state norm across baseline, scale-visible readout, norm-penalty, and scale-removing recurrence variants`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 两种小规模looped模型与variable-depth benchmark不证明所有recurrent architecture；norm稳定也不保证语义correctness或大规模收敛。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-24898:start -->
Claim boundary：只使用 `arXiv:2606.24898v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-24898:end -->
<!-- review:SF-2026-ARXIV-2606-24898:end -->

<!-- review:SF-2026-ARXIV-2606-24934:start -->
### 2606.24934 — Unprivileged Topology Certificates for Cloud GPU Attestation

**问题与旧路径。** Cloud GPU tenants receive a model name and a region, but cannot directly inspect the physical accelerator that runs their job. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Unprivileged Topology Certificates for Cloud GPU Attestation 的 exact-v1 机制为：We present a software-only attestation primitive for this setting. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24934v1 — §3 Attestation Model; §4 GPU Probe; §11 Packaging`；Evaluation=`arXiv:2606.24934v1 — §5 Certificate Stability Under Load; §6 Cross-Die Fingerprint Attestation; §7–§10 Attestation experiments`；counterevidence=`arXiv:2606.24934v1 — §12 Limitations; §13 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Cloud GPU tenants receive a model name and a region, but cannot directly inspect the physical accelerator that runs their job. 披露的 evaluation signal 是：A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24934:start -->
Primary identity `arXiv:2606.24934v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24934:end -->
<!-- review:SF-2026-ARXIV-2606-24934:end -->

<!-- review:SF-2026-ARXIV-2606-24957:start -->
### 2606.24957 — Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding

**问题与旧路径。** While speculative decoding improves inference throughput for multi-batch long-context Large Language Models (LLMs), its efficiency is often limited by a verification bottleneck where Key-Value (KV) cache loading dominates latency.

**机制、状态与控制流。** speculative verification 的 target KV 不再全读；Dustin 混合历史 attention 与 draft lookahead，semantic retrieval heads 在线估计关键 token，只对稀疏 KV 做 target verification。 唯一 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。

<!-- claim:SF-2026-ARXIV-2606-24957:start -->
Claim boundary：仅 `arXiv:2606.24957v1`；未证明边界定位 `https://arxiv.org/html/2606.24957v1 — §L Limitations; I Porting Overhead`。
<!-- claim:SF-2026-ARXIV-2606-24957:end -->
<!-- review:SF-2026-ARXIV-2606-24957:end -->

<!-- review:SF-2026-ARXIV-2606-24996:start -->
### 2606.24996 — From Forecasting Leaderboards to Deployment Decisions: A Fail-Closed Certification Protocol

**问题与旧路径。** Forecasting leaderboards rank models by predictive quality, but their winners are often read as deployment-ready top-1 advice.

**机制、状态与控制流。** deployment-facing leaderboard claim 必须经过 interface lock、clean positive anchor、native negative control、power/false-promotion 与 first-failing-gate report card；任一 gate 失败即禁止发布 selection inversion。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 证据来自 forecasting candidate families 与两个 locked interface；不证明所有 task metric 或业务成本可被同一 gate 捕获，underpowered audit 只能给 inconclusive。

<!-- claim:SF-2026-ARXIV-2606-24996:start -->
Claim boundary：仅 `arXiv:2606.24996v1`；未证明边界定位 `https://arxiv.org/html/2606.24996v1 — §3 Discussion: Limitations and scope; first-failing-gate audit`。
<!-- claim:SF-2026-ARXIV-2606-24996:end -->
<!-- review:SF-2026-ARXIV-2606-24996:end -->

<!-- review:SF-2026-ARXIV-2606-24998:start -->
### 2606.24998 — Internal Data Repetition Destroys Language Models

**问题与旧路径。** Language models are running out of high-quality training data, and even aggressively deduplicated corpora retain some amount of repetition.

**机制、状态与控制流。** 数据去重从 hygiene 建议升级为 compute allocation contract：相同样本的 internal repetition 先改善后破坏 eval loss，data owner 应记录 repeat count、unique pool 与 model-size-dependent peak。 唯一 owner 为 `TRAIN-DATA`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 结论绑定 synthetic repeated pools、模型尺度与 loss-floor fit；自然语料的语义近重复、curriculum 与 downstream contamination 未证明，不能由单一 repeat threshold 自动删除。

<!-- claim:SF-2026-ARXIV-2606-24998:start -->
Claim boundary：仅 `arXiv:2606.24998v1`；未证明边界定位 `https://arxiv.org/html/2606.24998v1 — §H Limitations`。
<!-- claim:SF-2026-ARXIV-2606-24998:end -->
<!-- review:SF-2026-ARXIV-2606-24998:end -->

<!-- review:SF-2026-ARXIV-2606-25040:start -->
### 2606.25040 — Chorus II: Cross-Request Sparsity Reuse for Efficient Image-to-Video Generation

**问题与旧路径。** Serving diffusion models for image-to-video generation is computationally expensive, posing significant challenges for large-scale deployment.

**机制、状态与控制流。** I2V scheduler 把相似请求历史 sparse mask 作为 request-conditioned prior，避免每请求 mask prediction；feature reuse 仅可选，并由 downsampled region 与 guidance enhancement 限制 semantic drift。 唯一 owner 为 `INFER-SCHEDULING`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 2.16x 来自论文 I2V workload/default config；相似度误路由、场景突变、跨模型 mask 不兼容和 feature boundary artifact 未证明，低置信时回退在线 mask/full compute。

<!-- claim:SF-2026-ARXIV-2606-25040:start -->
Claim boundary：仅 `arXiv:2606.25040v1`；未证明边界定位 `https://arxiv.org/html/2606.25040v1 — §5 Conclusion and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25040:end -->
<!-- review:SF-2026-ARXIV-2606-25040:end -->

<!-- review:SF-2026-ARXIV-2606-25082:start -->
### 2606.25082 — Energy Efficient Scheduling of AI/ML Workloads on Multi Instance GPUs with Dynamic Repartitioning

**问题与旧路径。** Increasing demand from AI/ML workloads is exacerbating the rising energy consumption of data centers.

**机制、状态与控制流。** MIG scheduler 同时拥有 configuration 内作业放置与 configuration 间 repartition；controller 以 power/performance state、partition action 与 reward 决定何时重分，而不是把 MIG 当静态 SKU。 唯一 owner 为 `PLATFORM-GPU-SCHEDULER`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 主要是 simulation 与测得的 MIG power characteristic；repartition downtime、state migration、真实混合作业 SLO 和多节点 GPU fabric 未闭合，收益不足时保留静态 partition。

<!-- claim:SF-2026-ARXIV-2606-25082:start -->
Claim boundary：仅 `arXiv:2606.25082v1`；未证明边界定位 `https://arxiv.org/html/2606.25082v1 — §VI Conclusion and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-25082:end -->
<!-- review:SF-2026-ARXIV-2606-25082:end -->

<!-- review:SF-2026-ARXIV-2606-25091:start -->
### 2606.25091 — Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off

**问题与旧路径。** Speculative decoding (SD) accelerates LLM inference by $1.5$-$3$ times when the draft and target models are co-located.

**机制、状态与控制流。** edge-cloud speculative decoding 的准入由 RTT、edge draft time、acceptance 与 target verification time 共同决定；single-request latency 不再是唯一目标，饱和 server 的 multi-tenant capacity 才可能 justify offload。 唯一 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。

<!-- claim:SF-2026-ARXIV-2606-25091:start -->
Claim boundary：仅 `arXiv:2606.25091v1`；未证明边界定位 `https://arxiv.org/html/2606.25091v1 — §V Conclusion and explicit verifier-interface/RTT boundary`。
<!-- claim:SF-2026-ARXIV-2606-25091:end -->
<!-- review:SF-2026-ARXIV-2606-25091:end -->

<!-- review:SF-2026-ARXIV-2606-25097:start -->
### 2606.25097 — Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion

**问题与旧路径。** Speculative decoding accelerates inference by letting a draft model propose tokens for a target model to verify, raising a concrete safety question: at temperature zero, can draft-side behavior leak into safety-scored outputs?

**机制、状态与控制流。** speculative decoding 上线前增加 target-aligned invariance screen：byte identity、McNemar、TOST 与 matched target-only arm 分离算法安全差异和 dtype/framework 噪声。 唯一 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。

<!-- claim:SF-2026-ARXIV-2606-25097:start -->
Claim boundary：仅 `arXiv:2606.25097v1`；未证明边界定位 `https://arxiv.org/html/2606.25097v1 — §5.3 Limitations and Threats to Validity`。
<!-- claim:SF-2026-ARXIV-2606-25097:end -->
<!-- review:SF-2026-ARXIV-2606-25097:end -->

<!-- review:SF-2026-ARXIV-2606-25098:start -->
### 2606.25098 — Power-Flexible AI Data Centers: A New Paradigm for Grid-Responsive Compute

**问题与旧路径。** The rapid expansion of artificial intelligence (AI) infrastructure is driving unprecedented growth in electricity demand from data centers.

**机制、状态与控制流。** grid signal 成为 cluster scheduler 的外部 control input，power telemetry/model 回写可用 curtailment budget；priority job 保留服务级别，elastic job 承担降载或跨地域迁移。 唯一 owner 为 `PLATFORM-GPU-SCHEDULER`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。

<!-- claim:SF-2026-ARXIV-2606-25098:start -->
Claim boundary：仅 `arXiv:2606.25098v1`；未证明边界定位 `https://arxiv.org/html/2606.25098v1 — §7 Discussion and service-level preservation scope`。
<!-- claim:SF-2026-ARXIV-2606-25098:end -->
<!-- review:SF-2026-ARXIV-2606-25098:end -->

<!-- review:SF-2026-ARXIV-2606-25115:start -->
### 2606.25115 — Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory

**问题与旧路径。** On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights.

**机制、状态与控制流。** 一个 value-minus-harm-per-byte score 同时控制 KEEP eviction、SHARE uplink 与 TRUST provenance gate；RAM、energy、uplink budget 与 poison risk 成为 memory lifecycle state。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** task-drift benchmark 与 Jetson 两臂/Hub testbed 不证明 score 跨设备、用户或攻击迁移；低校准或高风险 entry 应拒绝共享并回退本地可信 memory。

<!-- claim:SF-2026-ARXIV-2606-25115:start -->
Claim boundary：仅 `arXiv:2606.25115v1`；未证明边界定位 `https://arxiv.org/html/2606.25115v1 — §VI Related Work and deployment-specific score calibration`。
<!-- claim:SF-2026-ARXIV-2606-25115:end -->
<!-- review:SF-2026-ARXIV-2606-25115:end -->

<!-- review:SF-2026-ARXIV-2606-25156:start -->
### 2606.25156 — ATMA: Long-Context Language Modeling via Polar Attention and Gated-Delta Compression Memory

**问题与旧路径。** Length extrapolation in language models involves competing objectives: retrieval fidelity, long-document likelihood, short-context quality, and inference cost.

**机制、状态与控制流。** 长上下文设计从单一 accuracy 目标改为 retrieval、likelihood、short-context quality、decode state 与 kernel cost 的 Pareto；Polar direction/magnitude channel 配 gated-delta recurrent state。 唯一 owner 为 `MODEL-LONG-CONTEXT`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 378M、2K train、256K eval 中 FinePDFs exact retrieval 为 0%，hardware transition audit 非随机；不能宣称普遍外推，Raven/softmax/更短 context 仍是共存点。

<!-- claim:SF-2026-ARXIV-2606-25156:start -->
Claim boundary：仅 `arXiv:2606.25156v1`；未证明边界定位 `https://arxiv.org/html/2606.25156v1 — §5.1/5.4 trade-offs and reported 256K FinePDFs failure`。
<!-- claim:SF-2026-ARXIV-2606-25156:end -->
<!-- review:SF-2026-ARXIV-2606-25156:end -->

<!-- review:SF-2026-ARXIV-2606-25161:start -->
### 2606.25161 — TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory

**问题与旧路径。** Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows.

**机制、状态与控制流。** memory update 不再只按最终问答 reward；transition verifier 对 coverage、preservation、faithfulness 打分，同一旧 state 下比较候选 write/revise/delete，并用 preference-guided RL 训练 writer。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** MemoryAgentBench/HaluMem/Mem-alpha 与 verifier judge 不证明真实用户 consent、并发 writer、poisoning 或 judge drift；低置信 transition 应拒写并保留旧版本。

<!-- claim:SF-2026-ARXIV-2606-25161:start -->
Claim boundary：仅 `arXiv:2606.25161v1`；未证明边界定位 `https://arxiv.org/html/2606.25161v1 — §D Memory Transition Error Judge Prompt and evaluated datasets`。
<!-- claim:SF-2026-ARXIV-2606-25161:end -->
<!-- review:SF-2026-ARXIV-2606-25161:end -->

<!-- review:SF-2026-ARXIV-2606-25178:start -->
### 2606.25178 — Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR

**问题与旧路径。** Reinforcement learning with verifiable rewards (RLVR) has been extended from single-domain training to multi-domain reasoning suites spanning mathematics, programming, and science.

**机制、状态与控制流。** 多域 RLVR curriculum 不再只追当前 domain learnability；controller 从正在计算的 GRPO projected gradients 估计跨域 transfer，对 bandit arm value 做平滑后决定下一 domain。 唯一 owner 为 `TRAIN-GRPO`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 六域、Qwen3-1.7B/Llama3.2-3B 与 <1% overhead 不证明更大模型、non-verifiable reward 或 adversarial domain；gradient conflict 不稳定时回退 proportional/hand-designed mix。

<!-- claim:SF-2026-ARXIV-2606-25178:start -->
Claim boundary：仅 `arXiv:2606.25178v1`；未证明边界定位 `https://arxiv.org/html/2606.25178v1 — §6 Conclusion: Limitations; C Scaling`。
<!-- claim:SF-2026-ARXIV-2606-25178:end -->
<!-- review:SF-2026-ARXIV-2606-25178:end -->

<!-- review:SF-2026-ARXIV-2606-25189:start -->
### 2606.25189 — ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses

**问题与旧路径。** AI agents increasingly run in production through harnesses, the software around the LLM, including an engine that enforces safety and effectiveness policies, e.g., 'run tests before committing.' Enforcing these policies requires bridging a semantic gap: policy intent is expressed in underspecified natural language, while enforcement must act on concrete system actions, e.g., which test to run.

**机制、状态与控制流。** policy context 留在 agent/harness，但 enforcement 下沉 OS kernel；IFC DSL 表达跨 event ordering/data-flow，eBPF 覆盖绕过 tool-call layer 的 system action，并返回 semantic denial。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 1.9%–8.4% overhead 与论文 policy/task 不证明所有 syscall、container/runtime 或 kernel version；DSL 生成错误时必须 fail closed、人工修订或回退传统 sandbox。

<!-- claim:SF-2026-ARXIV-2606-25189:start -->
Claim boundary：仅 `arXiv:2606.25189v1`；未证明边界定位 `https://arxiv.org/html/2606.25189v1 — §2.3 Existing Approaches; evaluated policy/harness scope`。
<!-- claim:SF-2026-ARXIV-2606-25189:end -->
<!-- review:SF-2026-ARXIV-2606-25189:end -->

<!-- review:SF-2026-ARXIV-2606-25191:start -->
### 2606.25191 — To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG

**问题与旧路径。** Multi-agent document assessment for retrieval-augmented generation is computationally expensive, driving practitioners toward smaller, deployable models whose assessment mechanisms remain poorly understood.

**机制、状态与控制流。** document assessment 不再默认多 Agent scoring；pilot probe 测 reasoning-score coupling，弱模型路由到 per-document isolation，只有 score 有信息的模型才承担 assessment/reranking。 唯一 owner 为 `AGENT-RAG`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。

<!-- claim:SF-2026-ARXIV-2606-25191:start -->
Claim boundary：仅 `arXiv:2606.25191v1`；未证明边界定位 `https://arxiv.org/html/2606.25191v1 — §7 Discussion boundaries; D/F calibration sensitivity`。
<!-- claim:SF-2026-ARXIV-2606-25191:end -->
<!-- review:SF-2026-ARXIV-2606-25191:end -->

<!-- review:SF-2026-ARXIV-2606-25198:start -->
### 2606.25198 — Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty

**问题与旧路径。** Autonomous AI Research promises to accelerate the scientific progress of machine learning.

**机制、状态与控制流。** autonomous research loop 把 shared search state、lineage、quality/diversity/novelty archive 与 auditor verdict 作为 durable artifacts；40 个 fabrication 说明 score 结果必须过独立 audit 才能推进。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 3 个 ML domain、3,222 scored runs 未出现 Original 且 verifier 漏掉过 fabrication；不证明自动搜索能扩展 quality-novelty frontier，关键 claim 仍需独立复现/人工 gate。

<!-- claim:SF-2026-ARXIV-2606-25198:start -->
Claim boundary：仅 `arXiv:2606.25198v1`；未证明边界定位 `https://arxiv.org/html/2606.25198v1 — §6.2 Limitations; B.3 Limits of Agentic Verification`。
<!-- claim:SF-2026-ARXIV-2606-25198:end -->
<!-- review:SF-2026-ARXIV-2606-25198:end -->

<!-- review:SF-2026-ARXIV-2606-25207:start -->
### 2606.25207 — ASAP: Agent-System Co-Design for Wall-Clock-Centered Auto HPO Research for ML Experiments

**问题与旧路径。** Hyperparameter Optimization (HPO) is essential for maximizing machine learning model performance, and its core challenge is sample efficiency: finding strong configurations within a limited budget.

**机制、状态与控制流。** HPO agent 不替代单一 optimizer，而从多工具 proposal pool 选择；prefix-stable prompt 复用 KV，跨 iteration speculation 与 relative-error accept test 把 judge/tool latency 隐藏在 model evaluation 下。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** HPOBench/PD1 与给定 wall-clock regime 不证明昂贵、非平稳或安全敏感 experiment；accept test 不满足或 speculation 浪费时回退串行工具 loop。

<!-- claim:SF-2026-ARXIV-2606-25207:start -->
Claim boundary：仅 `arXiv:2606.25207v1`；未证明边界定位 `https://arxiv.org/html/2606.25207v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25207:end -->
<!-- review:SF-2026-ARXIV-2606-25207:end -->

<!-- review:SF-2026-ARXIV-2606-25215:start -->
### 2606.25215 — Reflective VLA: In-Context Action Consequences Make VLAs Generalize

**问题与旧路径。** Most vision-language-action (VLA) models are reactive: they predict the next action from the current instruction and observation, implicitly assuming that the current observation fully specifies the action-relevant state.

**机制、状态与控制流。** VLA state 从当前 observation 扩成 observation-action-consequence triplet buffer；shared attention 读历史后果，block-causal mask 防训练泄漏，KV cache 支撑实时滚动。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。

<!-- claim:SF-2026-ARXIV-2606-25215:start -->
Claim boundary：仅 `arXiv:2606.25215v1`；未证明边界定位 `https://arxiv.org/html/2606.25215v1 — §E Reproducibility, Assets, and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25215:end -->
<!-- review:SF-2026-ARXIV-2606-25215:end -->

<!-- review:SF-2026-ARXIV-2606-25274:start -->
### 2606.25274 — UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control

**问题与旧路径。** Time-series deployments often need delayed feasible decisions, not only accurate forecasts.

**机制、状态与控制流。** `3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25274:start -->
Claim boundary：仅 `arXiv:2606.25274v1`；未证明边界定位 `https://arxiv.org/html/2606.25274v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25274:end -->
<!-- review:SF-2026-ARXIV-2606-25274:end -->

<!-- review:SF-2026-ARXIV-2606-25285:start -->
### 2606.25285 — EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression

**问题与旧路径。** Post-Training Sparsity (PTS) has emerged as a crucial paradigm for compressing Large Language Models to facilitate efficient deployment on resource-constrained devices.

**机制、状态与控制流。** `3 EPTS: Elastic Post-Training Sparsity` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25285:start -->
Claim boundary：仅 `arXiv:2606.25285v1`；未证明边界定位 `https://arxiv.org/html/2606.25285v1 — §Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-25285:end -->
<!-- review:SF-2026-ARXIV-2606-25285:end -->

<!-- review:SF-2026-ARXIV-2606-25296:start -->
### 2606.25296 — SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety

**问题与旧路径。** With advances in autonomous driving and electric vehicle technologies, functional safety has become a critical requirement in automotive chip design.

**机制、状态与控制流。** `SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25296:start -->
Claim boundary：仅 `arXiv:2606.25296v1`；未证明边界定位 `https://arxiv.org/html/2606.25296v1 — §Threats to Validity; Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25296:end -->
<!-- review:SF-2026-ARXIV-2606-25296:end -->

<!-- review:SF-2026-ARXIV-2606-25342:start -->
### 2606.25342 — Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention

**问题与旧路径。** Lifelong continual learning remains an obstacle on the path to human-like intelligence.

**机制、状态与控制流。** `Parametric Attention and Lifelong In-Context Learning formulation` 所定义的源特定机制用于把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25342:start -->
Claim boundary：仅 `arXiv:2606.25342v1`；未证明边界定位 `https://arxiv.org/html/2606.25342v1 — §Discussion; finite-memory and task-family limitations`。
<!-- claim:SF-2026-ARXIV-2606-25342:end -->
<!-- review:SF-2026-ARXIV-2606-25342:end -->

<!-- review:SF-2026-ARXIV-2606-25349:start -->
### 2606.25349 — General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference

**问题与旧路径。** In secure two-party Transformer inference, linear layers are typically evaluated using Fully Homomorphic Encryption (FHE) through plaintext-ciphertext or ciphertext-ciphertext matrix multiplications, where key switching primarily occurs and dominates computational overhead in both FHE-based and hybrid FHE-MPC systems.

**机制、状态与控制流。** `IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25349:start -->
Claim boundary：仅 `arXiv:2606.25349v1`；未证明边界定位 `https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note`。
<!-- claim:SF-2026-ARXIV-2606-25349:end -->
<!-- review:SF-2026-ARXIV-2606-25349:end -->

<!-- review:SF-2026-ARXIV-2606-25353:start -->
### 2606.25353 — Cache-Resident LLM Inference in GB-Scale Last-Level Caches

**问题与旧路径。** Large language model (LLM) inference is increasingly dominated by data movement across the memory hierarchy.

**机制、状态与控制流。** `3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25353:start -->
Claim boundary：仅 `arXiv:2606.25353v1`；未证明边界定位 `https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works`。
<!-- claim:SF-2026-ARXIV-2606-25353:end -->
<!-- review:SF-2026-ARXIV-2606-25353:end -->

<!-- review:SF-2026-ARXIV-2606-25366:start -->
### 2606.25366 — Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield

**问题与旧路径。** Deep-space missions need onboard autonomy that is both capable and certifiable.

**机制、状态与控制流。** `III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25366:start -->
Claim boundary：仅 `arXiv:2606.25366v1`；未证明边界定位 `https://arxiv.org/html/2606.25366v1 — §XI-D Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25366:end -->
<!-- review:SF-2026-ARXIV-2606-25366:end -->

<!-- review:SF-2026-ARXIV-2606-25371:start -->
### 2606.25371 — Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers

**问题与旧路径。** Runtime assurance (RTA) protects a safety-critical system by switching from an advanced controller to a verified safe controller when a monitored condition is violated.

**机制、状态与控制流。** `III Problem Setup; IV Conformal Recovery-Deadline Certificate` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25371:start -->
Claim boundary：仅 `arXiv:2606.25371v1`；未证明边界定位 `https://arxiv.org/html/2606.25371v1 — §VI-D Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25371:end -->
<!-- review:SF-2026-ARXIV-2606-25371:end -->

<!-- review:SF-2026-ARXIV-2606-25388:start -->
### 2606.25388 — TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning

**问题与旧路径。** Reliable analytics and machine-learning pipelines depend on clean tabular data, yet production tables often contain missing values, typographical errors, inconsistent formats, violated dependencies, unit mismatches, and ambiguous categorical values.

**机制、状态与控制流。** `III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25388:start -->
Claim boundary：仅 `arXiv:2606.25388v1`；未证明边界定位 `https://arxiv.org/html/2606.25388v1 — §VII Discussion and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-25388:end -->
<!-- review:SF-2026-ARXIV-2606-25388:end -->

<!-- review:SF-2026-ARXIV-2606-25410:start -->
### 2606.25410 — DFMU: Data-Frugal Machine Unlearning

**问题与旧路径。** Machine unlearning is an emerging domain that ensures the safe removal of elements (includes concepts, attributes, entity and class) from the trained model along with least drop in model performance.

**机制、状态与控制流。** `3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Conclusion; class-forgetting experimental scope` 是 `DFMU: Data-Frugal Machine Unlearning` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; 4.4 Results` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25410:start -->
Claim boundary：仅 `arXiv:2606.25410v1`；未证明边界定位 `https://arxiv.org/html/2606.25410v1 — §5 Conclusion; class-forgetting experimental scope`。
<!-- claim:SF-2026-ARXIV-2606-25410:end -->
<!-- review:SF-2026-ARXIV-2606-25410:end -->

<!-- review:SF-2026-ARXIV-2606-25426:start -->
### 2606.25426 — Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX

**问题与旧路径。** On Apple Silicon the fp32 GEMMs dominating LLM prefill are dispatched by Accelerate to a matrix coprocessor (AMX) on the M1-M3.

**机制、状态与控制流。** `3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25426:start -->
Claim boundary：仅 `arXiv:2606.25426v1`；未证明边界定位 `https://arxiv.org/html/2606.25426v1 — §6 Conclusion; Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25426:end -->
<!-- review:SF-2026-ARXIV-2606-25426:end -->

<!-- review:SF-2026-ARXIV-2606-25447:start -->
### 2606.25447 — The Interplay of Harness Design and Post-Training in LLM Agents

**问题与旧路径。** Tool-integrated LLM agents are often wrapped within a harness: the scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation.

**机制、状态与控制流。** `3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25447:start -->
Claim boundary：仅 `arXiv:2606.25447v1`；未证明边界定位 `https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary`。
<!-- claim:SF-2026-ARXIV-2606-25447:end -->
<!-- review:SF-2026-ARXIV-2606-25447:end -->

<!-- review:SF-2026-ARXIV-2606-25449:start -->
### 2606.25449 — Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One

**问题与旧路径。** A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain.

**机制、状态与控制流。** `3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25449:start -->
Claim boundary：仅 `arXiv:2606.25449v1`；未证明边界定位 `https://arxiv.org/html/2606.25449v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25449:end -->
<!-- review:SF-2026-ARXIV-2606-25449:end -->

<!-- review:SF-2026-ARXIV-2606-25453:start -->
### 2606.25453 — EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication

**问题与旧路径。** Modern GPUs devote an increasing silicon budget to low-precision matrix-multiplication units, widening the precision-throughput gap for scientific computing workloads.

**机制、状态与控制流。** `III EmuGEMM-I; IV EmuGEMM-II` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25453:start -->
Claim boundary：仅 `arXiv:2606.25453v1`；未证明边界定位 `https://arxiv.org/html/2606.25453v1 — §V-G Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25453:end -->
<!-- review:SF-2026-ARXIV-2606-25453:end -->

<!-- review:SF-2026-ARXIV-2606-25467:start -->
### 2606.25467 — RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs

**问题与旧路径。** Intent-driven edge services allow multiple virtual network function (VNF) segments in a service function chain directed acyclic graph (SFC-DAG) to be locally reordered without changing service semantics, creating richer request-side orchestration freedom.

**机制、状态与控制流。** `III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration` 所定义的源特定机制用于让在线编排器共同持有请求资源耦合、准入和降级状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25467:start -->
Claim boundary：仅 `arXiv:2606.25467v1`；未证明边界定位 `https://arxiv.org/html/2606.25467v1 — §D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications`。
<!-- claim:SF-2026-ARXIV-2606-25467:end -->
<!-- review:SF-2026-ARXIV-2606-25467:end -->

<!-- review:SF-2026-ARXIV-2606-25487:start -->
### 2606.25487 — How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring

**问题与旧路径。** Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade.

**机制、状态与控制流。** `3 Setup; Appendix A Prompts, wrappers, and attack configuration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25487:start -->
Claim boundary：仅 `arXiv:2606.25487v1`；未证明边界定位 `https://arxiv.org/html/2606.25487v1 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25487:end -->
<!-- review:SF-2026-ARXIV-2606-25487:end -->

<!-- review:SF-2026-ARXIV-2606-25514:start -->
### 2606.25514 — Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution

**问题与旧路径。** Resolving issues with ambiguous and incomplete descriptions, particularly concerning complex bugs, requires a sophisticated, long-horizon workflow.

**机制、状态与控制流。** `2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication` 所定义的源特定机制用于把事件通信、角色分工与失败升级纳入多 Agent 协调状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25514:start -->
Claim boundary：仅 `arXiv:2606.25514v1`；未证明边界定位 `https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity`。
<!-- claim:SF-2026-ARXIV-2606-25514:end -->
<!-- review:SF-2026-ARXIV-2606-25514:end -->

<!-- review:SF-2026-ARXIV-2606-25519:start -->
### 2606.25519 — Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models

**问题与旧路径。** Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency.

**机制、状态与控制流。** `3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25519:start -->
Claim boundary：仅 `arXiv:2606.25519v1`；未证明边界定位 `https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details`。
<!-- claim:SF-2026-ARXIV-2606-25519:end -->
<!-- review:SF-2026-ARXIV-2606-25519:end -->

<!-- review:SF-2026-ARXIV-2606-25532:start -->
### 2606.25532 — Agentic evolution of physically constrained foundation models

**问题与旧路径。** Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs.

**机制、状态与控制流。** `Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought` 所定义的源特定机制用于把硬件约束和发现链纳入平台设计候选的验收边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25532:start -->
Claim boundary：仅 `arXiv:2606.25532v1`；未证明边界定位 `https://arxiv.org/html/2606.25532v1 — §Exact-v1 research-prototype and evaluated hardware-design boundary`。
<!-- claim:SF-2026-ARXIV-2606-25532:end -->
<!-- review:SF-2026-ARXIV-2606-25532:end -->

<!-- review:SF-2026-ARXIV-2606-25548:start -->
### 2606.25548 — Concept Removal for Frontier Image Generative Models

**问题与旧路径。** Image generative models are trained on massive, largely uncurated internet-scale datasets that contain undesirable visual concepts.

**机制、状态与控制流。** `4 Transcoders-based Concept Removal; 4.1 BLOCK Framework` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `G Limitations; D.1 Model-Architecture-Dependent Subtleties` 是 `Concept Removal for Frontier Image Generative Models` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25548:start -->
Claim boundary：仅 `arXiv:2606.25548v1`；未证明边界定位 `https://arxiv.org/html/2606.25548v1 — §G Limitations; D.1 Model-Architecture-Dependent Subtleties`。
<!-- claim:SF-2026-ARXIV-2606-25548:end -->
<!-- review:SF-2026-ARXIV-2606-25548:end -->

<!-- review:SF-2026-ARXIV-2606-25575:start -->
### 2606.25575 — One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand

**问题与旧路径。** Assistive robotic systems face a fundamental trade-off: fully autonomous systems lack user agency, while fully user-controlled systems demand continuous cognitive effort.

**机制、状态与控制流。** `Variable-autonomy architecture; task-phase authority transfer; always-available release gesture` 所定义的源特定机制用于把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25575:start -->
Claim boundary：仅 `arXiv:2606.25575v1`；未证明边界定位 `https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study`。
<!-- claim:SF-2026-ARXIV-2606-25575:end -->
<!-- review:SF-2026-ARXIV-2606-25575:end -->

<!-- review:SF-2026-ARXIV-2606-25592:start -->
### 2606.25592 — VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks

**问题与旧路径。** Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrate complex video dynamics with unprecedented controllability.

**机制、状态与控制流。** `2 Visual Prompt Attack and Defense; 2.2 VPA-Guard` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25592:start -->
Claim boundary：仅 `arXiv:2606.25592v1`；未证明边界定位 `https://arxiv.org/html/2606.25592v1 — §E.1 Limitations; E.4 Human-in-the-loop Discussion`。
<!-- claim:SF-2026-ARXIV-2606-25592:end -->
<!-- review:SF-2026-ARXIV-2606-25592:end -->

<!-- review:SF-2026-ARXIV-2606-25605:start -->
### 2606.25605 — Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints

**问题与旧路径。** Tool Calling and Structured Output are two core capabilities of modern Agent systems, yet their interaction under joint deployment conditions remains insufficiently understood.

**机制、状态与控制流。** `3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25605:start -->
Claim boundary：仅 `arXiv:2606.25605v1`；未证明边界定位 `https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25605:end -->
<!-- review:SF-2026-ARXIV-2606-25605:end -->

<!-- review:SF-2026-ARXIV-2606-25608:start -->
### 2606.25608 — An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz

**问题与旧路径。** This paper presents a novel approach to perform semi-automated BSI IT-Grundschutz certification using a MultiLarge Language Model system (MLS) with Hybrid RetrievalAugmented Generation (HybridRAG).

**机制、状态与控制流。** `V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `V-C Restrictions of our architecture; VII Future Research` 是 `An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `VI Initial Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25608:start -->
Claim boundary：仅 `arXiv:2606.25608v1`；未证明边界定位 `https://arxiv.org/html/2606.25608v1 — §V-C Restrictions of our architecture; VII Future Research`。
<!-- claim:SF-2026-ARXIV-2606-25608:end -->
<!-- review:SF-2026-ARXIV-2606-25608:end -->

<!-- review:SF-2026-ARXIV-2606-25622:start -->
### 2606.25622 — Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz

**问题与旧路径。** The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises.

**机制、状态与控制流。** `IV Theoretical Framework: MAS Architecture and Experimental Setup` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25622:start -->
Claim boundary：仅 `arXiv:2606.25622v1`；未证明边界定位 `https://arxiv.org/html/2606.25622v1 — §VI Limitations & Future Work`。
<!-- claim:SF-2026-ARXIV-2606-25622:end -->
<!-- review:SF-2026-ARXIV-2606-25622:end -->

<!-- review:SF-2026-ARXIV-2606-25656:start -->
### 2606.25656 — Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization

**问题与旧路径。** As advanced RAG variants like GraphRAG and Agentic RAG emerge, one leading question is when and how to use them.

**机制、状态与控制流。** `3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25656:start -->
Claim boundary：仅 `arXiv:2606.25656v1`；未证明边界定位 `https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap`。
<!-- claim:SF-2026-ARXIV-2606-25656:end -->
<!-- review:SF-2026-ARXIV-2606-25656:end -->

<!-- review:SF-2026-ARXIV-2606-25658:start -->
### 2606.25658 — Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding

**问题与旧路径。** Currently, streaming video understanding is still a daunting task for existing \emph{multimodal large language models} (MLLMs).

**机制、状态与控制流。** `3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25658:start -->
Claim boundary：仅 `arXiv:2606.25658v1`；未证明边界定位 `https://arxiv.org/html/2606.25658v1 — §A Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25658:end -->
<!-- review:SF-2026-ARXIV-2606-25658:end -->

<!-- review:SF-2026-ARXIV-2606-25674:start -->
### 2606.25674 — BitNet Text Embeddings

**问题与旧路径。** LLM-based text embedders have substantially improved retrieval and semantic representation quality, but their deployment remains costly: large backbone models slow down embedding inference, while high-dimensional full-precision embeddings impose substantial storage and bandwidth overhead on large-scale indexes.

**机制、状态与控制流。** `3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25674:start -->
Claim boundary：仅 `arXiv:2606.25674v1`；未证明边界定位 `https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization`。
<!-- claim:SF-2026-ARXIV-2606-25674:end -->
<!-- review:SF-2026-ARXIV-2606-25674:end -->

<!-- review:SF-2026-ARXIV-2606-25700:start -->
### 2606.25700 — Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning

**问题与旧路径。** When fine-tuning Large Language Models (LLMs), there has been success in minimizing both memory usage and computation with Parameter-Efficient Fine-Tuning (PEFT), like Low Rank Adaptation (LoRA).

**机制、状态与控制流。** `III Methods; III-B Training; III-C Architecture` 所定义的源特定机制用于把秩、适配器容量与计算预算绑定为显式训练配置；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `V Discussion; V-A Choice of rank; V-C Computation` 是 `Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning` 的 source-specific 反例/局限边界；若运行条件离开 `IV Results; IV-B Computation calculation` 的验证域，`TRAIN-LORA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25700:start -->
Claim boundary：仅 `arXiv:2606.25700v1`；未证明边界定位 `https://arxiv.org/html/2606.25700v1 — §V Discussion; V-A Choice of rank; V-C Computation`。
<!-- claim:SF-2026-ARXIV-2606-25700:end -->
<!-- review:SF-2026-ARXIV-2606-25700:end -->

<!-- review:SF-2026-ARXIV-2606-25705:start -->
### 2606.25705 — GUI agent: Guided Exploration of User-Sensitive Screens

**问题与旧路径。** LLM agents are increasingly being used to automate tasks for users within an open GUI environment.

**机制、状态与控制流。** `3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25705:start -->
Claim boundary：仅 `arXiv:2606.25705v1`；未证明边界定位 `https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary`。
<!-- claim:SF-2026-ARXIV-2606-25705:end -->
<!-- review:SF-2026-ARXIV-2606-25705:end -->

<!-- review:SF-2026-ARXIV-2606-25721:start -->
### 2606.25721 — Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution

**问题与旧路径。** Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents.

**机制、状态与控制流。** `4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25721:start -->
Claim boundary：仅 `arXiv:2606.25721v1`；未证明边界定位 `https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity`。
<!-- claim:SF-2026-ARXIV-2606-25721:end -->
<!-- review:SF-2026-ARXIV-2606-25721:end -->

<!-- review:SF-2026-ARXIV-2606-25759:start -->
### 2606.25759 — NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication

**问题与旧路径。** Large-scale neural-network training repeatedly aggregates gradients across devices, making communication a central cost in distributed learning.

**机制、状态与控制流。** `3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing` 所定义的源特定机制用于把集群运行剖面映射为运行时 bucket 与并行绑定状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25759:start -->
Claim boundary：仅 `arXiv:2606.25759v1`；未证明边界定位 `https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary`。
<!-- claim:SF-2026-ARXIV-2606-25759:end -->
<!-- review:SF-2026-ARXIV-2606-25759:end -->

<!-- review:SF-2026-ARXIV-2606-25760:start -->
### 2606.25760 — Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets

**问题与旧路径。** Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions.

**机制、状态与控制流。** `3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25760:start -->
Claim boundary：仅 `arXiv:2606.25760v1`；未证明边界定位 `https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details`。
<!-- claim:SF-2026-ARXIV-2606-25760:end -->
<!-- review:SF-2026-ARXIV-2606-25760:end -->

<!-- review:SF-2026-ARXIV-2606-25782:start -->
### 2606.25782 — Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation

**问题与旧路径。** With the widespread adoption of large language models (LLMs) in chatbots and everyday applications, companies increasingly need guardrails that are effective while remaining low-cost and low-latency.

**机制、状态与控制流。** `2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25782:start -->
Claim boundary：仅 `arXiv:2606.25782v1`；未证明边界定位 `https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency`。
<!-- claim:SF-2026-ARXIV-2606-25782:end -->
<!-- review:SF-2026-ARXIV-2606-25782:end -->

<!-- review:SF-2026-ARXIV-2606-25797:start -->
### 2606.25797 — Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes

**问题与旧路径。** Markov decision processes (MDPs) are a classic model of decision making under uncertainty, exhibiting both non-deterministic choice as well as probabilistic uncertainty.

**机制、状态与控制流。** `3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect` 是 `Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes` 的 source-specific 反例/局限边界；若运行条件离开 `4 Implementation and Experimental Evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25797:start -->
Claim boundary：仅 `arXiv:2606.25797v1`；未证明边界定位 `https://arxiv.org/html/2606.25797v1 — §0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect`。
<!-- claim:SF-2026-ARXIV-2606-25797:end -->
<!-- review:SF-2026-ARXIV-2606-25797:end -->

<!-- review:SF-2026-ARXIV-2606-25819:start -->
### 2606.25819 — Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability

**问题与旧路径。** Large language models are increasingly deployed as agents that solve tasks by interacting with external tool environments.

**机制、状态与控制流。** `ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25819:start -->
Claim boundary：仅 `arXiv:2606.25819v1`；未证明边界定位 `https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary`。
<!-- claim:SF-2026-ARXIV-2606-25819:end -->
<!-- review:SF-2026-ARXIV-2606-25819:end -->

<!-- review:SF-2026-ARXIV-2606-25838:start -->
### 2606.25838 — Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines

**问题与旧路径。** Production vision pipelines silently degrade on blurry input, wasting compute on downstream OCR, retrieval, and vision-language model (VLM) calls that cannot recover a usable output.

**机制、状态与控制流。** `III Method; IV Confidence-Aware Routing` 所定义的源特定机制用于让路由器基于请求置信度持有后端选择与回退权；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25838:start -->
Claim boundary：仅 `arXiv:2606.25838v1`；未证明边界定位 `https://arxiv.org/html/2606.25838v1 — §VII-C Limitations and future work`。
<!-- claim:SF-2026-ARXIV-2606-25838:end -->
<!-- review:SF-2026-ARXIV-2606-25838:end -->

<!-- review:SF-2026-ARXIV-2606-25863:start -->
### 2606.25863 — Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis

**问题与旧路径。** We study how security patches in highly configurable C/C++ systems map onto the space of compile-time variants.

**机制、状态与控制流。** `PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25863:start -->
Claim boundary：仅 `arXiv:2606.25863v1`；未证明边界定位 `https://arxiv.org/pdf/2606.25863v1 — §PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary`。
<!-- claim:SF-2026-ARXIV-2606-25863:end -->
<!-- review:SF-2026-ARXIV-2606-25863:end -->

<!-- review:SF-2026-ARXIV-2606-25871:start -->
### 2606.25871 — AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search

**问题与旧路径。** How can we generate high-quality relevance annotations at scale without the cost and delays of human labeling?

**机制、状态与控制流。** `3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25871:start -->
Claim boundary：仅 `arXiv:2606.25871v1`；未证明边界定位 `https://arxiv.org/html/2606.25871v1 — §5 Production Deployment and Discussion; sponsored-search relevance boundary`。
<!-- claim:SF-2026-ARXIV-2606-25871:end -->
<!-- review:SF-2026-ARXIV-2606-25871:end -->

<!-- review:SF-2026-ARXIV-2606-25987:start -->
### 2606.25987 — Weave of Formal Thought

**问题与旧路径。** Large language models (LLMs) attain remarkable surface fluency on code, yet they neither formally guarantee the syntactic validity of their output nor leverage the hierarchical structure defining the target language.

**机制、状态与控制流。** `3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25987:start -->
Claim boundary：仅 `arXiv:2606.25987v1`；未证明边界定位 `https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary`。
<!-- claim:SF-2026-ARXIV-2606-25987:end -->
<!-- review:SF-2026-ARXIV-2606-25987:end -->

<!-- review:SF-2026-ARXIV-2606-25996:start -->
### 2606.25996 — Autodata: An agentic data scientist to create high quality synthetic data

**问题与旧路径。** We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data.

**机制、状态与控制流。** `2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25996:start -->
Claim boundary：仅 `arXiv:2606.25996v1`；未证明边界定位 `https://arxiv.org/html/2606.25996v1 — §6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation`。
<!-- claim:SF-2026-ARXIV-2606-25996:end -->
<!-- review:SF-2026-ARXIV-2606-25996:end -->

<!-- review:SF-2026-ARXIV-2606-26021:start -->
### 2606.26021 — Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries

**问题与旧路径。** Tabular foundation models are commonly assumed to present limited privacy concerns as they are often pre-trained on large collections of synthetic data.

**机制、状态与控制流。** `V Attention-based MIA; VI Inference-Time Hardening Against MIAs` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26021:start -->
Claim boundary：仅 `arXiv:2606.26021v1`；未证明边界定位 `https://arxiv.org/html/2606.26021v1 — §VIII-C Limitations and opportunities; I Context size`。
<!-- claim:SF-2026-ARXIV-2606-26021:end -->
<!-- review:SF-2026-ARXIV-2606-26021:end -->

<!-- review:SF-2026-ARXIV-2606-26027:start -->
### 2606.26027 — Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It

**问题与旧路径。** Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities.

**机制、状态与控制流。** `4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes` 所定义的源特定机制用于把崩溃信号与监督修复绑定到策略更新门控；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26027:start -->
Claim boundary：仅 `arXiv:2606.26027v1`；未证明边界定位 `https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic`。
<!-- claim:SF-2026-ARXIV-2606-26027:end -->
<!-- review:SF-2026-ARXIV-2606-26027:end -->

<!-- review:SF-2026-ARXIV-2606-26028:start -->
### 2606.26028 — Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem

**问题与旧路径。** As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy?

**机制、状态与控制流。** `3 System Model: ERC-8004 Protocol; 7 Reputation Market Security` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26028:start -->
Claim boundary：仅 `arXiv:2606.26028v1`；未证明边界定位 `https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges`。
<!-- claim:SF-2026-ARXIV-2606-26028:end -->
<!-- review:SF-2026-ARXIV-2606-26028:end -->

<!-- review:SF-2026-ARXIV-2606-26057:start -->
### 2606.26057 — The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems

**问题与旧路径。** AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems.

**机制、状态与控制流。** `2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26057:start -->
Claim boundary：仅 `arXiv:2606.26057v1`；未证明边界定位 `https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility`。
<!-- claim:SF-2026-ARXIV-2606-26057:end -->
<!-- review:SF-2026-ARXIV-2606-26057:end -->

<!-- review:SF-2026-ARXIV-2606-26071:start -->
### 2606.26071 — Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment

**问题与旧路径。** A central goal of safety research is determining whether a model is misaligned.

**机制、状态与控制流。** `4 Protocol and Methods; 5 Environments; 7 Methodological Insights` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26071:start -->
Claim boundary：仅 `arXiv:2606.26071v1`；未证明边界定位 `https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary`。
<!-- claim:SF-2026-ARXIV-2606-26071:end -->
<!-- review:SF-2026-ARXIV-2606-26071:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-24898 | 44M与129M looped transformers；无inter-loop normalization时norm升至数千/数万，scale-visible readout、norm penalty或scale-removing recurrence保持在数十。 | 44M- and 129M-parameter looped transformers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Per-loop cross-entropy plus hidden-state norm across baseline, scale-visible readout, norm-penalty, and scale-removing recurrence variants |
| SF-2026-ARXIV-2606-24934 | Unprivileged Topology Certificates for Cloud GPU Attestation — A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. | Not Disclosed | NVIDIA confidential computing extends this to the GPU with a hardware-fused device identity and signed measurements of firmware and configuration [ 2 ] . CUDA device attributes, nvidia-smi telemetry, and clock64() are related but provide distinct operational views. | Each payload is an LZMA-compressed copy of the original file, so the store is reversible without dropping rows, reducing precision, or sampling the timing streams. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A CUDA probe measures an SM-by-memory-region latency matrix using physical SM labels and dependent global loads. | A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. |
| SF-2026-ARXIV-2606-24957 | While speculative decoding improves inference throughput for multi-batch long-context Large Language Models (LLMs), its efficiency is often limited by a verification bottleneck where Key-Value (KV) cache loading dominates latency. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Evaluations on PG-19 and LongBench with Qwen2.5-72B demonstrate that Dustin achieves a 27.85x speedup in self-attention and a 9.17x end-to-end decoding speedup at a 32k sequence length, all with negligible accuracy degradation. |
| SF-2026-ARXIV-2606-24996 | Forecasting leaderboards rank models by predictive quality, but their winners are often read as deployment-ready top-1 advice. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-24998 | Language models are running out of high-quality training data, and even aggressively deduplicated corpora retain some amount of repetition. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25040 | Serving diffusion models for image-to-video generation is computationally expensive, posing significant challenges for large-scale deployment. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Experiments show that default sparsity reuse configuration preserves generation quality with a \textbf{2.16$\times$} speedup. |
| SF-2026-ARXIV-2606-25082 | Increasing demand from AI/ML workloads is exacerbating the rising energy consumption of data centers. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25091 | Speculative decoding (SD) accelerates LLM inference by $1.5$-$3$ times when the draft and target models are co-located. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | DSD should therefore be evaluated primarily by multi-tenant capacity and server throughput, not only by single-request latency. |
| SF-2026-ARXIV-2606-25097 | Speculative decoding accelerates inference by letting a draft model propose tokens for a target model to verify, raising a concrete safety question: at temperature zero, can draft-side behavior leak into safety-scored outputs? | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25098 | real-world 130 kW GPU cluster under peak, emergency, sustained and carbon-aware dispatch | Not Disclosed | 130 kW GPU cluster | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | load reduction, sustained curtailment, priority-job service preservation and geo-shift performance |
| SF-2026-ARXIV-2606-25115 | On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25156 | 120-cell 1B-token factorial; matched 9.816B-token 2K training; evaluation through 256K | 378M NoPE/RoPE/Polar variants | Not Disclosed | Not Disclosed | 2K train; up to 256K evaluation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | retrieval accuracy, bits-per-byte, eight short-context tasks and kernel overhead |
| SF-2026-ARXIV-2606-25161 | Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | TrustMem relies on a Memory Transition Verifier to evaluate the transition process of memory updates in terms of coverage, preservation, and faithfulness. |
| SF-2026-ARXIV-2606-25178 | six-domain reasoning RLVR suite | Qwen3-1.7B and Llama3.2-3B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | macro accuracy, curriculum dynamics, ablation and wall-clock overhead |
| SF-2026-ARXIV-2606-25189 | coding policies, OctoBench tasks and safety benchmarks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | policy compliance, DSL coverage/cost and 1.9%-8.4% overhead |
| SF-2026-ARXIV-2606-25191 | Multi-agent document assessment for retrieval-augmented generation is computationally expensive, driving practitioners toward smaller, deployable models whose assessment mechanisms remain poorly understood. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25198 | 3,222 scored research runs across LLM pretraining, on-policy RL and model unlearning | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | asynchronous search strategies; exact worker count varies by experiment | Not Disclosed | quality, diversity, novelty and 40 confirmed fabrication audits |
| SF-2026-ARXIV-2606-25207 | Hyperparameter Optimization (HPO) is essential for maximizing machine learning model performance, and its core challenge is sample efficiency: finding strong configurations within a limited budget. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Yet these methods share two limitations with a common origin: they use the LLM as a single-tool replacement evaluated by iteration count. |
| SF-2026-ARXIV-2606-25215 | LIBERO, SimplerEnv-Bridge, LIBERO-Plus/Hard and real-robot protocols | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success under distribution shift, matched history ablation and latency-accuracy trade-off |
| SF-2026-ARXIV-2606-25274 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25285 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25296 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25342 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25349 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25353 | Not Disclosed | Not Disclosed | GB-scale last-level-cache server CPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | end-to-end performance; analytical-model validation; context-length/batch sensitivity |
| SF-2026-ARXIV-2606-25366 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25371 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25388 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25410 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25426 | Not Disclosed | Not Disclosed | Apple M1 AMX | FP32 bit-exact | 128-token prefill | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 12 LLM prefill GEMMs and llama.cpp full-forward tokens/s |
| SF-2026-ARXIV-2606-25447 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25449 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25453 | Not Disclosed | Not Disclosed | NVIDIA Hopper and Blackwell GPUs | INT8 Tensor Core emulation of higher precision | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | kernel efficiency, end-to-end throughput, precision-memory trade-off |
| SF-2026-ARXIV-2606-25467 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25487 | 596 human-labeled HarmBench completions; 30 confident true positives for white-box GCG | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | precision, recall, wrapper flip rate and white-box attack success |
| SF-2026-ARXIV-2606-25514 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25519 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25532 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25548 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25575 | 44 participants; five bimanual tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | completion time, task success and 7-point acceptance ratings |
| SF-2026-ARXIV-2606-25592 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25605 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25608 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25622 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25656 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25658 | Not Disclosed | LLaVA-OneVision and Qwen2.5-VL | Not Disclosed | Not Disclosed | hour-long streaming video; 12k visual-token memory budget | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | streaming/offline accuracy, compression ratio and storage |
| SF-2026-ARXIV-2606-25674 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25700 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25705 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25721 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25759 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25760 | 27 UQ methods across VLMs and GUI-grounding datasets | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | AUROC, PRR, graded severity, calibration and conformal click disks |
| SF-2026-ARXIV-2606-25782 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25797 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25819 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25838 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25863 | 1,192 Linux kernel, 289 FFmpeg and 100 PHP patches | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | VIC extraction coverage, manual precision, formula size and CVE-text recall |
| SF-2026-ARXIV-2606-25871 | six production offline use cases; 150M+ annotations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | accuracy, calibration gain and cascade compute cost |
| SF-2026-ARXIV-2606-25987 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-25996 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26021 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26027 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26028 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-26057 | 1,000 migration fixtures; 17 adversarial classes; 80+ robustness tests | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | byte equivalence, reject equivalence, latency and machine-checked fail-closed invariant |
| SF-2026-ARXIV-2606-26071 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-24898 | score_7_9; potential_books_delta | selected | DA-20260613-READOUT-BLIND-SPOT | — | 它揭示监督信号与runtime state的结构性盲区，独立于Agent安全与平台监控，构成今日第三个分析主线。 | analysis:DA-20260613-READOUT-BLIND-SPOT |
| SF-2026-ARXIV-2606-24934 | score_7_9; potential_books_delta | not_selected | — | — | Unprivileged Topology Certificates for Cloud GPU Attestation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24934 |
| SF-2026-ARXIV-2606-24957 | score_7_9; potential_books_delta | not_selected | — | — | Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24957 |
| SF-2026-ARXIV-2606-24996 | score_7_9; potential_books_delta | not_selected | — | — | From Forecasting Leaderboards to Deployment Decisions: A Fail-Closed Certification Protocol remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24996 |
| SF-2026-ARXIV-2606-24998 | score_7_9; potential_books_delta | not_selected | — | — | Internal Data Repetition Destroys Language Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24998 |
| SF-2026-ARXIV-2606-25040 | score_7_9; potential_books_delta | not_selected | — | — | Chorus II: Cross-Request Sparsity Reuse for Efficient Image-to-Video Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25040 |
| SF-2026-ARXIV-2606-25082 | score_7_9; potential_books_delta | not_selected | — | — | Energy Efficient Scheduling of AI/ML Workloads on Multi Instance GPUs with Dynamic Repartitioning remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25082 |
| SF-2026-ARXIV-2606-25091 | score_7_9; potential_books_delta | not_selected | — | — | Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25091 |
| SF-2026-ARXIV-2606-25097 | score_7_9; potential_books_delta | not_selected | — | — | Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25097 |
| SF-2026-ARXIV-2606-25098 | score_7_9; potential_books_delta | not_selected | — | — | Power-Flexible AI Data Centers: A New Paradigm for Grid-Responsive Compute remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25098 |
| SF-2026-ARXIV-2606-25115 | score_7_9; potential_books_delta | not_selected | — | — | Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25115 |
| SF-2026-ARXIV-2606-25156 | score_7_9; potential_books_delta | not_selected | — | — | ATMA: Long-Context Language Modeling via Polar Attention and Gated-Delta Compression Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25156 |
| SF-2026-ARXIV-2606-25161 | score_7_9; potential_books_delta | not_selected | — | — | TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25161 |
| SF-2026-ARXIV-2606-25178 | score_7_9; potential_books_delta | not_selected | — | — | Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25178 |
| SF-2026-ARXIV-2606-25189 | score_7_9; potential_books_delta | selected | DA-20260624-2606-25189 | — | 入选：policy context 留在 agent/harness，但 enforcement 下沉 OS kernel；IFC DSL 表达跨 event ordering/data-flow，eBPF 覆盖绕过 tool-call layer 的 system action，并返回 semantic denial。 | analysis:DA-20260624-2606-25189 |
| SF-2026-ARXIV-2606-25191 | score_7_9; potential_books_delta | not_selected | — | — | To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25191 |
| SF-2026-ARXIV-2606-25198 | score_7_9; potential_books_delta | not_selected | — | — | Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25198 |
| SF-2026-ARXIV-2606-25207 | score_7_9; potential_books_delta | not_selected | — | — | ASAP: Agent-System Co-Design for Wall-Clock-Centered Auto HPO Research for ML Experiments remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25207 |
| SF-2026-ARXIV-2606-25215 | score_7_9; potential_books_delta | not_selected | — | — | Reflective VLA: In-Context Action Consequences Make VLAs Generalize remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25215 |
| SF-2026-ARXIV-2606-25274 | score_7_9; potential_books_delta | not_selected | — | — | UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25274 |
| SF-2026-ARXIV-2606-25285 | score_7_9; potential_books_delta | not_selected | — | — | EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25285 |
| SF-2026-ARXIV-2606-25296 | score_7_9; potential_books_delta | not_selected | — | — | SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25296 |
| SF-2026-ARXIV-2606-25342 | score_7_9; potential_books_delta | not_selected | — | — | Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention remains evidence-complete after canonical owner transfer with V2 score 7 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25342 |
| SF-2026-ARXIV-2606-25349 | score_7_9; potential_books_delta | not_selected | — | — | General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25349 |
| SF-2026-ARXIV-2606-25353 | score_7_9; potential_books_delta | not_selected | — | — | Cache-Resident LLM Inference in GB-Scale Last-Level Caches remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-PREFILL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25353 |
| SF-2026-ARXIV-2606-25366 | score_7_9; potential_books_delta | not_selected | — | — | Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25366 |
| SF-2026-ARXIV-2606-25371 | score_7_9; potential_books_delta | not_selected | — | — | Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25371 |
| SF-2026-ARXIV-2606-25388 | score_7_9; potential_books_delta | not_selected | — | — | TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25388 |
| SF-2026-ARXIV-2606-25410 | score_7_9 | not_selected | — | — | DFMU: Data-Frugal Machine Unlearning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25410 |
| SF-2026-ARXIV-2606-25426 | score_7_9; potential_books_delta | not_selected | — | — | Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-PREFILL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25426 |
| SF-2026-ARXIV-2606-25447 | score_7_9; potential_books_delta | not_selected | — | — | The Interplay of Harness Design and Post-Training in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25447 |
| SF-2026-ARXIV-2606-25449 | score_7_9; potential_books_delta | not_selected | — | — | Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25449 |
| SF-2026-ARXIV-2606-25453 | score_7_9; potential_books_delta | not_selected | — | — | EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25453 |
| SF-2026-ARXIV-2606-25467 | score_7_9; potential_books_delta | not_selected | — | — | RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25467 |
| SF-2026-ARXIV-2606-25487 | score_7_9; potential_books_delta | not_selected | — | — | How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25487 |
| SF-2026-ARXIV-2606-25514 | score_7_9; potential_books_delta | not_selected | — | — | Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25514 |
| SF-2026-ARXIV-2606-25519 | score_7_9; potential_books_delta | not_selected | — | — | Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25519 |
| SF-2026-ARXIV-2606-25532 | score_7_9; potential_books_delta | not_selected | — | — | Agentic evolution of physically constrained foundation models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25532 |
| SF-2026-ARXIV-2606-25548 | score_7_9 | not_selected | — | — | Concept Removal for Frontier Image Generative Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25548 |
| SF-2026-ARXIV-2606-25575 | score_7_9; potential_books_delta | not_selected | — | — | One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25575 |
| SF-2026-ARXIV-2606-25592 | score_7_9; potential_books_delta | not_selected | — | — | VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25592 |
| SF-2026-ARXIV-2606-25605 | score_7_9; potential_books_delta | not_selected | — | — | Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25605 |
| SF-2026-ARXIV-2606-25608 | score_7_9 | not_selected | — | — | An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25608 |
| SF-2026-ARXIV-2606-25622 | score_7_9; potential_books_delta | not_selected | — | — | Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25622 |
| SF-2026-ARXIV-2606-25656 | score_7_9; potential_books_delta | not_selected | — | — | Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25656 |
| SF-2026-ARXIV-2606-25658 | score_7_9; potential_books_delta | not_selected | — | — | Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25658 |
| SF-2026-ARXIV-2606-25674 | score_7_9; potential_books_delta | not_selected | — | — | BitNet Text Embeddings remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25674 |
| SF-2026-ARXIV-2606-25700 | score_7_9 | not_selected | — | — | Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-LORA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25700 |
| SF-2026-ARXIV-2606-25705 | score_7_9; potential_books_delta | not_selected | — | — | GUI agent: Guided Exploration of User-Sensitive Screens remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25705 |
| SF-2026-ARXIV-2606-25721 | score_7_9; potential_books_delta | not_selected | — | — | Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25721 |
| SF-2026-ARXIV-2606-25759 | score_7_9; potential_books_delta | not_selected | — | — | NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25759 |
| SF-2026-ARXIV-2606-25760 | score_7_9; potential_books_delta | not_selected | — | — | Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25760 |
| SF-2026-ARXIV-2606-25782 | score_7_9; potential_books_delta | not_selected | — | — | Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25782 |
| SF-2026-ARXIV-2606-25797 | score_7_9 | not_selected | — | — | Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25797 |
| SF-2026-ARXIV-2606-25819 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25819 |
| SF-2026-ARXIV-2606-25838 | score_7_9; potential_books_delta | not_selected | — | — | Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-REQUEST-LIFECYCLE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25838 |
| SF-2026-ARXIV-2606-25863 | score_7_9; potential_books_delta | not_selected | — | — | Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25863 |
| SF-2026-ARXIV-2606-25871 | score_7_9; potential_books_delta | not_selected | — | — | AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25871 |
| SF-2026-ARXIV-2606-25987 | score_7_9; potential_books_delta | not_selected | — | — | Weave of Formal Thought remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25987 |
| SF-2026-ARXIV-2606-25996 | score_7_9; potential_books_delta | not_selected | — | — | Autodata: An agentic data scientist to create high quality synthetic data remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-25996 |
| SF-2026-ARXIV-2606-26021 | score_7_9; potential_books_delta | not_selected | — | — | Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26021 |
| SF-2026-ARXIV-2606-26027 | score_7_9; potential_books_delta | not_selected | — | — | Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26027 |
| SF-2026-ARXIV-2606-26028 | score_7_9; potential_books_delta | not_selected | — | — | Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26028 |
| SF-2026-ARXIV-2606-26057 | score_7_9; potential_books_delta | selected | DA-20260625-2606-26057 | — | 入选：`2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 | analysis:DA-20260625-2606-26057 |
| SF-2026-ARXIV-2606-26071 | score_7_9; potential_books_delta | not_selected | — | — | Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-26071 |

### Selected Analysis Narratives

<!-- analysis:DA-20260613-READOUT-BLIND-SPOT:start -->
### DA-20260613-READOUT-BLIND-SPOT
Looped model 把 hidden state 变成跨步 runtime state，但 readout-invariant scale不会被每步交叉熵直接约束。训练 exit 与控制 recurrence 是两个目标：要么让 scale 对 loss 可见，要么从 recurrence中移除。
<!-- analysis:DA-20260613-READOUT-BLIND-SPOT:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24934:start -->
Unprivileged Topology Certificates for Cloud GPU Attestation remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24934:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24957:start -->
Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24957:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24996:start -->
From Forecasting Leaderboards to Deployment Decisions: A Fail-Closed Certification Protocol remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24996:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24998:start -->
Internal Data Repetition Destroys Language Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24998:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25040:start -->
Chorus II: Cross-Request Sparsity Reuse for Efficient Image-to-Video Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25040:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25082:start -->
Energy Efficient Scheduling of AI/ML Workloads on Multi Instance GPUs with Dynamic Repartitioning remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25082:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25091:start -->
Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25091:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25097:start -->
Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25097:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25098:start -->
Power-Flexible AI Data Centers: A New Paradigm for Grid-Responsive Compute remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25098:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25115:start -->
Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25115:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25156:start -->
ATMA: Long-Context Language Modeling via Polar Attention and Gated-Delta Compression Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25156:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25161:start -->
TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25161:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25178:start -->
Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25178:end -->

<!-- analysis:DA-20260624-2606-25189:start -->
入选：policy context 留在 agent/harness，但 enforcement 下沉 OS kernel；IFC DSL 表达跨 event ordering/data-flow，eBPF 覆盖绕过 tool-call layer 的 system action，并返回 semantic denial。
<!-- analysis:DA-20260624-2606-25189:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25191:start -->
To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25191:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25198:start -->
Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25198:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25207:start -->
ASAP: Agent-System Co-Design for Wall-Clock-Centered Auto HPO Research for ML Experiments remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25207:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25215:start -->
Reflective VLA: In-Context Action Consequences Make VLAs Generalize remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25215:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25274:start -->
UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-PLANNING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25274:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25285:start -->
EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25285:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25296:start -->
SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25296:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25342:start -->
Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention remains evidence-complete after canonical owner transfer with V2 score 7 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25342:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25349:start -->
General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25349:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25353:start -->
Cache-Resident LLM Inference in GB-Scale Last-Level Caches remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-PREFILL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25353:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25366:start -->
Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25366:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25371:start -->
Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25371:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25388:start -->
TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25388:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25410:start -->
DFMU: Data-Frugal Machine Unlearning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25410:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25426:start -->
Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-PREFILL. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25426:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25447:start -->
The Interplay of Harness Design and Post-Training in LLM Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25447:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25449:start -->
Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25449:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25453:start -->
EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25453:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25467:start -->
RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25487:start -->
How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25487:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25514:start -->
Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25514:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25519:start -->
Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25519:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25532:start -->
Agentic evolution of physically constrained foundation models remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-FOUNDATIONS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25532:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25548:start -->
Concept Removal for Frontier Image Generative Models remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25548:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25575:start -->
One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25575:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25592:start -->
VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25592:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25605:start -->
Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25605:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25608:start -->
An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25608:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25622:start -->
Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25622:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25656:start -->
Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25656:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25658:start -->
Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25658:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25674:start -->
BitNet Text Embeddings remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25674:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25700:start -->
Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-LORA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25700:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25705:start -->
GUI agent: Guided Exploration of User-Sensitive Screens remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25705:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25721:start -->
Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25721:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25759:start -->
NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25759:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25760:start -->
Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25760:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25782:start -->
Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25782:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25797:start -->
Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25797:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25819:start -->
Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25819:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25838:start -->
Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-REQUEST-LIFECYCLE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25838:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25863:start -->
Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25863:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25871:start -->
AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25871:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25987:start -->
Weave of Formal Thought remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25987:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-25996:start -->
Autodata: An agentic data scientist to create high quality synthetic data remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-25996:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26021:start -->
Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26021:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26027:start -->
Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26027:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26028:start -->
Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26028:end -->

<!-- analysis:DA-20260625-2606-26057:start -->
### The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems

`2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

`8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- analysis:DA-20260625-2606-26057:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-26071:start -->
Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-26071:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-24898 | MODEL-DECODER-ONLY | Books/part-02-model/18-decoder-only.md#L1 | Books/part-02-model/17-transformer-layer.md#L1; Books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-24898 | delta:SF-2026-ARXIV-2606-24898 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24898 |
| SF-2026-ARXIV-2606-24934 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-24934 | delta:SF-2026-ARXIV-2606-24934 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24934 |
| SF-2026-ARXIV-2606-24957 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-24957 | delta:SF-2026-ARXIV-2606-24957 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24957 |
| SF-2026-ARXIV-2606-24996 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-24996 | delta:SF-2026-ARXIV-2606-24996 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24996 |
| SF-2026-ARXIV-2606-24998 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-24998 | delta:SF-2026-ARXIV-2606-24998 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24998 |
| SF-2026-ARXIV-2606-25040 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-25040 | delta:SF-2026-ARXIV-2606-25040 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25040 |
| SF-2026-ARXIV-2606-25082 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1 | existing:SF-2026-ARXIV-2606-25082 | delta:SF-2026-ARXIV-2606-25082 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25082 |
| SF-2026-ARXIV-2606-25091 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-25091 | delta:SF-2026-ARXIV-2606-25091 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25091 |
| SF-2026-ARXIV-2606-25097 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-25097 | delta:SF-2026-ARXIV-2606-25097 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25097 |
| SF-2026-ARXIV-2606-25098 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1 | existing:SF-2026-ARXIV-2606-25098 | delta:SF-2026-ARXIV-2606-25098 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25098 |
| SF-2026-ARXIV-2606-25115 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-25115 | delta:SF-2026-ARXIV-2606-25115 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25115 |
| SF-2026-ARXIV-2606-25156 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L1 | books/part-02-model/13-position-encoding.md#L1 | existing:SF-2026-ARXIV-2606-25156 | delta:SF-2026-ARXIV-2606-25156 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25156 |
| SF-2026-ARXIV-2606-25161 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-25161 | delta:SF-2026-ARXIV-2606-25161 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25161 |
| SF-2026-ARXIV-2606-25178 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/31-rlhf.md#L1 | existing:SF-2026-ARXIV-2606-25178 | delta:SF-2026-ARXIV-2606-25178 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25178 |
| SF-2026-ARXIV-2606-25189 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-25189 | delta:SF-2026-ARXIV-2606-25189 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25189 |
| SF-2026-ARXIV-2606-25191 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-25191 | delta:SF-2026-ARXIV-2606-25191 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25191 |
| SF-2026-ARXIV-2606-25198 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-25198 | delta:SF-2026-ARXIV-2606-25198 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25198 |
| SF-2026-ARXIV-2606-25207 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-25207 | delta:SF-2026-ARXIV-2606-25207 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25207 |
| SF-2026-ARXIV-2606-25215 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-25215 | delta:SF-2026-ARXIV-2606-25215 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25215 |
| SF-2026-ARXIV-2606-25274 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L140 | books/part-07-agent/80-reflection.md#L73 | existing:SF-2026-ARXIV-2606-25274 | delta:SF-2026-ARXIV-2606-25274 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25274 |
| SF-2026-ARXIV-2606-25285 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L186 | books/part-05-inference-system/55-pd-disaggregation.md#L409 | existing:SF-2026-ARXIV-2606-25285 | delta:SF-2026-ARXIV-2606-25285 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25285 |
| SF-2026-ARXIV-2606-25296 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25296 | delta:SF-2026-ARXIV-2606-25296 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25296 |
| SF-2026-ARXIV-2606-25342 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L374 | books/part-02-model/19-kv-cache.md#L131 | existing:SF-2026-ARXIV-2606-25342 | delta:SF-2026-ARXIV-2606-25342 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25342 |
| SF-2026-ARXIV-2606-25349 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25349 | delta:SF-2026-ARXIV-2606-25349 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25349 |
| SF-2026-ARXIV-2606-25353 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L33 | books/part-05-inference-system/42-what-happens-during-inference.md#L117 | existing:SF-2026-ARXIV-2606-25353 | delta:SF-2026-ARXIV-2606-25353 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25353 |
| SF-2026-ARXIV-2606-25366 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25366 | delta:SF-2026-ARXIV-2606-25366 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25366 |
| SF-2026-ARXIV-2606-25371 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25371 | delta:SF-2026-ARXIV-2606-25371 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25371 |
| SF-2026-ARXIV-2606-25388 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25388 | delta:SF-2026-ARXIV-2606-25388 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25388 |
| SF-2026-ARXIV-2606-25410 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25410 | delta:SF-2026-ARXIV-2606-25410 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25410 |
| SF-2026-ARXIV-2606-25426 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L33 | books/part-05-inference-system/42-what-happens-during-inference.md#L117 | existing:SF-2026-ARXIV-2606-25426 | delta:SF-2026-ARXIV-2606-25426 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25426 |
| SF-2026-ARXIV-2606-25447 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 | books/part-07-agent/78-tool-calling.md#L37 | existing:SF-2026-ARXIV-2606-25447 | delta:SF-2026-ARXIV-2606-25447 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25447 |
| SF-2026-ARXIV-2606-25449 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L900 | books/part-07-agent/76-rag.md#L57 | existing:SF-2026-ARXIV-2606-25449 | delta:SF-2026-ARXIV-2606-25449 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25449 |
| SF-2026-ARXIV-2606-25453 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L630 | books/part-05-inference-system/48-speculative-decoding.md#L113 | existing:SF-2026-ARXIV-2606-25453 | delta:SF-2026-ARXIV-2606-25453 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25453 |
| SF-2026-ARXIV-2606-25467 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L227 | books/part-05-inference-system/46-continuous-batching.md#L75 | existing:SF-2026-ARXIV-2606-25467 | delta:SF-2026-ARXIV-2606-25467 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25467 |
| SF-2026-ARXIV-2606-25487 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25487 | delta:SF-2026-ARXIV-2606-25487 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25487 |
| SF-2026-ARXIV-2606-25514 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L240 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25514 | delta:SF-2026-ARXIV-2606-25514 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25514 |
| SF-2026-ARXIV-2606-25519 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L186 | books/part-05-inference-system/55-pd-disaggregation.md#L409 | existing:SF-2026-ARXIV-2606-25519 | delta:SF-2026-ARXIV-2606-25519 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25519 |
| SF-2026-ARXIV-2606-25532 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L61 | books/part-06-ai-infrastructure/58-kubeflow.md#L71 | existing:SF-2026-ARXIV-2606-25532 | delta:SF-2026-ARXIV-2606-25532 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25532 |
| SF-2026-ARXIV-2606-25548 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25548 | delta:SF-2026-ARXIV-2606-25548 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25548 |
| SF-2026-ARXIV-2606-25575 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L179 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L259 | existing:SF-2026-ARXIV-2606-25575 | delta:SF-2026-ARXIV-2606-25575 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25575 |
| SF-2026-ARXIV-2606-25592 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25592 | delta:SF-2026-ARXIV-2606-25592 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25592 |
| SF-2026-ARXIV-2606-25605 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25605 | delta:SF-2026-ARXIV-2606-25605 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25605 |
| SF-2026-ARXIV-2606-25608 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25608 | delta:SF-2026-ARXIV-2606-25608 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25608 |
| SF-2026-ARXIV-2606-25622 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25622 | delta:SF-2026-ARXIV-2606-25622 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25622 |
| SF-2026-ARXIV-2606-25656 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-25656 | delta:SF-2026-ARXIV-2606-25656 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25656 |
| SF-2026-ARXIV-2606-25658 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L900 | books/part-07-agent/76-rag.md#L57 | existing:SF-2026-ARXIV-2606-25658 | delta:SF-2026-ARXIV-2606-25658 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25658 |
| SF-2026-ARXIV-2606-25674 | AGENT-RAG | books/part-07-agent/76-rag.md#L51 | books/part-07-agent/77-memory.md#L113 | existing:SF-2026-ARXIV-2606-25674 | delta:SF-2026-ARXIV-2606-25674 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25674 |
| SF-2026-ARXIV-2606-25700 | TRAIN-LORA | books/part-04-training-system/30-lora.md#L145 | books/part-04-training-system/29-sft.md#L194 | existing:SF-2026-ARXIV-2606-25700 | delta:SF-2026-ARXIV-2606-25700 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25700 |
| SF-2026-ARXIV-2606-25705 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25705 | delta:SF-2026-ARXIV-2606-25705 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25705 |
| SF-2026-ARXIV-2606-25721 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25721 | delta:SF-2026-ARXIV-2606-25721 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25721 |
| SF-2026-ARXIV-2606-25759 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L646 | books/part-04-training-system/37-tensor-parallel.md#L243 | existing:SF-2026-ARXIV-2606-25759 | delta:SF-2026-ARXIV-2606-25759 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25759 |
| SF-2026-ARXIV-2606-25760 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25760 | delta:SF-2026-ARXIV-2606-25760 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25760 |
| SF-2026-ARXIV-2606-25782 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25782 | delta:SF-2026-ARXIV-2606-25782 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25782 |
| SF-2026-ARXIV-2606-25797 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-25797 | delta:SF-2026-ARXIV-2606-25797 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-25797 |
| SF-2026-ARXIV-2606-25819 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25819 | delta:SF-2026-ARXIV-2606-25819 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25819 |
| SF-2026-ARXIV-2606-25838 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L80 | books/part-05-inference-system/43-prefill.md#L33 | existing:SF-2026-ARXIV-2606-25838 | delta:SF-2026-ARXIV-2606-25838 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25838 |
| SF-2026-ARXIV-2606-25863 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-25863 | delta:SF-2026-ARXIV-2606-25863 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25863 |
| SF-2026-ARXIV-2606-25871 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25871 | delta:SF-2026-ARXIV-2606-25871 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25871 |
| SF-2026-ARXIV-2606-25987 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55 | books/part-07-agent/81-workflow.md#L36 | existing:SF-2026-ARXIV-2606-25987 | delta:SF-2026-ARXIV-2606-25987 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25987 |
| SF-2026-ARXIV-2606-25996 | TRAIN-DATA | books/part-04-training-system/27-data.md#L130 | books/part-04-training-system/28-pretraining.md#L244 | existing:SF-2026-ARXIV-2606-25996 | delta:SF-2026-ARXIV-2606-25996 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-25996 |
| SF-2026-ARXIV-2606-26021 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26021 | delta:SF-2026-ARXIV-2606-26021 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26021 |
| SF-2026-ARXIV-2606-26027 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L231 | books/part-04-training-system/32-ppo.md#L330 | existing:SF-2026-ARXIV-2606-26027 | delta:SF-2026-ARXIV-2606-26027 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26027 |
| SF-2026-ARXIV-2606-26028 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26028 | delta:SF-2026-ARXIV-2606-26028 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26028 |
| SF-2026-ARXIV-2606-26057 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L204 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 | existing:SF-2026-ARXIV-2606-26057 | delta:SF-2026-ARXIV-2606-26057 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26057 |
| SF-2026-ARXIV-2606-26071 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L136 | books/part-06-ai-infrastructure/59-model-registry.md#L118 | existing:SF-2026-ARXIV-2606-26071 | delta:SF-2026-ARXIV-2606-26071 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-26071 |

<!-- existing:SF-2026-ARXIV-2606-24898:start -->
Read owner `MODEL-DECODER-ONLY` at `Books/part-02-model/18-decoder-only.md` and adjacent chapters `Books/part-02-model/17-transformer-layer.md; Books/part-04-training-system/28-pretraining.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-24898:end -->

<!-- delta:SF-2026-ARXIV-2606-24898:start -->
Looped LM 的dense per-loop cross-entropy只控制readout可见变量；RMSNorm/LayerNorm隐藏radial scale时，recurrent residual仍携带scale，必须让scale对loss可见或从recurrence移除。
<!-- delta:SF-2026-ARXIV-2606-24898:end -->

<!-- books-review:SF-2026-ARXIV-2606-24898:start -->
Relation `Direct Evolution`; disposition `Integrate`. 两种小规模looped模型与variable-depth benchmark不证明所有recurrent architecture；norm稳定也不保证语义correctness或大规模收敛。
<!-- books-review:SF-2026-ARXIV-2606-24898:end -->

<!-- existing:SF-2026-ARXIV-2606-24934:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24934:end -->

<!-- delta:SF-2026-ARXIV-2606-24934:start -->
Unprivileged Topology Certificates for Cloud GPU Attestation 的 exact-v1 机制为：We present a software-only attestation primitive for this setting. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-24934:end -->

<!-- books-review:SF-2026-ARXIV-2606-24934:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Cloud GPU tenants receive a model name and a region, but cannot directly inspect the physical accelerator that runs their job. 披露的 evaluation signal 是：A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24934:end -->

<!-- existing:SF-2026-ARXIV-2606-24957:start -->
Re-read `books/part-05-inference-system/48-speculative-decoding.md#L1` and adjacent `books/part-05-inference-system/49-tensorrt-llm.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24957:end -->

<!-- delta:SF-2026-ARXIV-2606-24957:start -->
speculative verification 的 target KV 不再全读；Dustin 混合历史 attention 与 draft lookahead，semantic retrieval heads 在线估计关键 token，只对稀疏 KV 做 target verification。
<!-- delta:SF-2026-ARXIV-2606-24957:end -->

<!-- books-review:SF-2026-ARXIV-2606-24957:start -->
Direct Evolution; Integrate queued for root. 静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。
<!-- books-review:SF-2026-ARXIV-2606-24957:end -->

<!-- existing:SF-2026-ARXIV-2606-24996:start -->
Re-read `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` and adjacent `books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24996:end -->

<!-- delta:SF-2026-ARXIV-2606-24996:start -->
deployment-facing leaderboard claim 必须经过 interface lock、clean positive anchor、native negative control、power/false-promotion 与 first-failing-gate report card；任一 gate 失败即禁止发布 selection inversion。
<!-- delta:SF-2026-ARXIV-2606-24996:end -->

<!-- books-review:SF-2026-ARXIV-2606-24996:start -->
Direct Evolution; Integrate queued for root. 证据来自 forecasting candidate families 与两个 locked interface；不证明所有 task metric 或业务成本可被同一 gate 捕获，underpowered audit 只能给 inconclusive。
<!-- books-review:SF-2026-ARXIV-2606-24996:end -->

<!-- existing:SF-2026-ARXIV-2606-24998:start -->
Re-read `books/part-04-training-system/27-data.md#L1` and adjacent `books/part-04-training-system/28-pretraining.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24998:end -->

<!-- delta:SF-2026-ARXIV-2606-24998:start -->
数据去重从 hygiene 建议升级为 compute allocation contract：相同样本的 internal repetition 先改善后破坏 eval loss，data owner 应记录 repeat count、unique pool 与 model-size-dependent peak。
<!-- delta:SF-2026-ARXIV-2606-24998:end -->

<!-- books-review:SF-2026-ARXIV-2606-24998:start -->
Direct Evolution; Integrate queued for root. 结论绑定 synthetic repeated pools、模型尺度与 loss-floor fit；自然语料的语义近重复、curriculum 与 downstream contamination 未证明，不能由单一 repeat threshold 自动删除。
<!-- books-review:SF-2026-ARXIV-2606-24998:end -->

<!-- existing:SF-2026-ARXIV-2606-25040:start -->
Re-read `books/part-05-inference-system/56-inference-scheduling.md#L1` and adjacent `books/part-05-inference-system/46-continuous-batching.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25040:end -->

<!-- delta:SF-2026-ARXIV-2606-25040:start -->
I2V scheduler 把相似请求历史 sparse mask 作为 request-conditioned prior，避免每请求 mask prediction；feature reuse 仅可选，并由 downsampled region 与 guidance enhancement 限制 semantic drift。
<!-- delta:SF-2026-ARXIV-2606-25040:end -->

<!-- books-review:SF-2026-ARXIV-2606-25040:start -->
Direct Evolution; Integrate queued for root. 2.16x 来自论文 I2V workload/default config；相似度误路由、场景突变、跨模型 mask 不兼容和 feature boundary artifact 未证明，低置信时回退在线 mask/full compute。
<!-- books-review:SF-2026-ARXIV-2606-25040:end -->

<!-- existing:SF-2026-ARXIV-2606-25082:start -->
Re-read `books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1` and adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25082:end -->

<!-- delta:SF-2026-ARXIV-2606-25082:start -->
MIG scheduler 同时拥有 configuration 内作业放置与 configuration 间 repartition；controller 以 power/performance state、partition action 与 reward 决定何时重分，而不是把 MIG 当静态 SKU。
<!-- delta:SF-2026-ARXIV-2606-25082:end -->

<!-- books-review:SF-2026-ARXIV-2606-25082:start -->
Direct Evolution; Integrate queued for root. 主要是 simulation 与测得的 MIG power characteristic；repartition downtime、state migration、真实混合作业 SLO 和多节点 GPU fabric 未闭合，收益不足时保留静态 partition。
<!-- books-review:SF-2026-ARXIV-2606-25082:end -->

<!-- existing:SF-2026-ARXIV-2606-25091:start -->
Re-read `books/part-05-inference-system/48-speculative-decoding.md#L1` and adjacent `books/part-05-inference-system/49-tensorrt-llm.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25091:end -->

<!-- delta:SF-2026-ARXIV-2606-25091:start -->
edge-cloud speculative decoding 的准入由 RTT、edge draft time、acceptance 与 target verification time 共同决定；single-request latency 不再是唯一目标，饱和 server 的 multi-tenant capacity 才可能 justify offload。
<!-- delta:SF-2026-ARXIV-2606-25091:end -->

<!-- books-review:SF-2026-ARXIV-2606-25091:start -->
Direct Evolution; Integrate queued for root. 这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。
<!-- books-review:SF-2026-ARXIV-2606-25091:end -->

<!-- existing:SF-2026-ARXIV-2606-25097:start -->
Re-read `books/part-05-inference-system/48-speculative-decoding.md#L1` and adjacent `books/part-05-inference-system/49-tensorrt-llm.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25097:end -->

<!-- delta:SF-2026-ARXIV-2606-25097:start -->
speculative decoding 上线前增加 target-aligned invariance screen：byte identity、McNemar、TOST 与 matched target-only arm 分离算法安全差异和 dtype/framework 噪声。
<!-- delta:SF-2026-ARXIV-2606-25097:end -->

<!-- books-review:SF-2026-ARXIV-2606-25097:start -->
Direct Evolution; Integrate queued for root. 证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。
<!-- books-review:SF-2026-ARXIV-2606-25097:end -->

<!-- existing:SF-2026-ARXIV-2606-25098:start -->
Re-read `books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1` and adjacent `books/part-06-ai-infrastructure/65-kai-scheduler.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25098:end -->

<!-- delta:SF-2026-ARXIV-2606-25098:start -->
grid signal 成为 cluster scheduler 的外部 control input，power telemetry/model 回写可用 curtailment budget；priority job 保留服务级别，elastic job 承担降载或跨地域迁移。
<!-- delta:SF-2026-ARXIV-2606-25098:end -->

<!-- books-review:SF-2026-ARXIV-2606-25098:start -->
Direct Evolution; Integrate queued for root. 130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。
<!-- books-review:SF-2026-ARXIV-2606-25098:end -->

<!-- existing:SF-2026-ARXIV-2606-25115:start -->
Re-read `books/part-07-agent/77-memory.md#L1` and adjacent `books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25115:end -->

<!-- delta:SF-2026-ARXIV-2606-25115:start -->
一个 value-minus-harm-per-byte score 同时控制 KEEP eviction、SHARE uplink 与 TRUST provenance gate；RAM、energy、uplink budget 与 poison risk 成为 memory lifecycle state。
<!-- delta:SF-2026-ARXIV-2606-25115:end -->

<!-- books-review:SF-2026-ARXIV-2606-25115:start -->
Direct Evolution; Integrate queued for root. task-drift benchmark 与 Jetson 两臂/Hub testbed 不证明 score 跨设备、用户或攻击迁移；低校准或高风险 entry 应拒绝共享并回退本地可信 memory。
<!-- books-review:SF-2026-ARXIV-2606-25115:end -->

<!-- existing:SF-2026-ARXIV-2606-25156:start -->
Re-read `books/part-02-model/22-long-context.md#L1` and adjacent `books/part-02-model/13-position-encoding.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25156:end -->

<!-- delta:SF-2026-ARXIV-2606-25156:start -->
长上下文设计从单一 accuracy 目标改为 retrieval、likelihood、short-context quality、decode state 与 kernel cost 的 Pareto；Polar direction/magnitude channel 配 gated-delta recurrent state。
<!-- delta:SF-2026-ARXIV-2606-25156:end -->

<!-- books-review:SF-2026-ARXIV-2606-25156:start -->
Direct Evolution; Integrate queued for root. 378M、2K train、256K eval 中 FinePDFs exact retrieval 为 0%，hardware transition audit 非随机；不能宣称普遍外推，Raven/softmax/更短 context 仍是共存点。
<!-- books-review:SF-2026-ARXIV-2606-25156:end -->

<!-- existing:SF-2026-ARXIV-2606-25161:start -->
Re-read `books/part-07-agent/77-memory.md#L1` and adjacent `books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25161:end -->

<!-- delta:SF-2026-ARXIV-2606-25161:start -->
memory update 不再只按最终问答 reward；transition verifier 对 coverage、preservation、faithfulness 打分，同一旧 state 下比较候选 write/revise/delete，并用 preference-guided RL 训练 writer。
<!-- delta:SF-2026-ARXIV-2606-25161:end -->

<!-- books-review:SF-2026-ARXIV-2606-25161:start -->
Direct Evolution; Integrate queued for root. MemoryAgentBench/HaluMem/Mem-alpha 与 verifier judge 不证明真实用户 consent、并发 writer、poisoning 或 judge drift；低置信 transition 应拒写并保留旧版本。
<!-- books-review:SF-2026-ARXIV-2606-25161:end -->

<!-- existing:SF-2026-ARXIV-2606-25178:start -->
Re-read `books/part-04-training-system/33-grpo.md#L1` and adjacent `books/part-04-training-system/31-rlhf.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25178:end -->

<!-- delta:SF-2026-ARXIV-2606-25178:start -->
多域 RLVR curriculum 不再只追当前 domain learnability；controller 从正在计算的 GRPO projected gradients 估计跨域 transfer，对 bandit arm value 做平滑后决定下一 domain。
<!-- delta:SF-2026-ARXIV-2606-25178:end -->

<!-- books-review:SF-2026-ARXIV-2606-25178:start -->
Direct Evolution; Integrate queued for root. 六域、Qwen3-1.7B/Llama3.2-3B 与 <1% overhead 不证明更大模型、non-verifiable reward 或 adversarial domain；gradient conflict 不稳定时回退 proportional/hand-designed mix。
<!-- books-review:SF-2026-ARXIV-2606-25178:end -->

<!-- existing:SF-2026-ARXIV-2606-25189:start -->
Re-read `books/part-06-ai-infrastructure/72-security.md#L1` and adjacent `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25189:end -->

<!-- delta:SF-2026-ARXIV-2606-25189:start -->
policy context 留在 agent/harness，但 enforcement 下沉 OS kernel；IFC DSL 表达跨 event ordering/data-flow，eBPF 覆盖绕过 tool-call layer 的 system action，并返回 semantic denial。
<!-- delta:SF-2026-ARXIV-2606-25189:end -->

<!-- books-review:SF-2026-ARXIV-2606-25189:start -->
Direct Evolution; Integrate queued for root. 1.9%–8.4% overhead 与论文 policy/task 不证明所有 syscall、container/runtime 或 kernel version；DSL 生成错误时必须 fail closed、人工修订或回退传统 sandbox。
<!-- books-review:SF-2026-ARXIV-2606-25189:end -->

<!-- existing:SF-2026-ARXIV-2606-25191:start -->
Re-read `books/part-07-agent/76-rag.md#L1` and adjacent `books/part-07-agent/77-memory.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25191:end -->

<!-- delta:SF-2026-ARXIV-2606-25191:start -->
document assessment 不再默认多 Agent scoring；pilot probe 测 reasoning-score coupling，弱模型路由到 per-document isolation，只有 score 有信息的模型才承担 assessment/reranking。
<!-- delta:SF-2026-ARXIV-2606-25191:end -->

<!-- books-review:SF-2026-ARXIV-2606-25191:start -->
Direct Evolution; Integrate queued for root. 7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。
<!-- books-review:SF-2026-ARXIV-2606-25191:end -->

<!-- existing:SF-2026-ARXIV-2606-25198:start -->
Re-read `books/part-07-agent/81-workflow.md#L1` and adjacent `books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25198:end -->

<!-- delta:SF-2026-ARXIV-2606-25198:start -->
autonomous research loop 把 shared search state、lineage、quality/diversity/novelty archive 与 auditor verdict 作为 durable artifacts；40 个 fabrication 说明 score 结果必须过独立 audit 才能推进。
<!-- delta:SF-2026-ARXIV-2606-25198:end -->

<!-- books-review:SF-2026-ARXIV-2606-25198:start -->
Direct Evolution; Integrate queued for root. 3 个 ML domain、3,222 scored runs 未出现 Original 且 verifier 漏掉过 fabrication；不证明自动搜索能扩展 quality-novelty frontier，关键 claim 仍需独立复现/人工 gate。
<!-- books-review:SF-2026-ARXIV-2606-25198:end -->

<!-- existing:SF-2026-ARXIV-2606-25207:start -->
Re-read `books/part-07-agent/81-workflow.md#L1` and adjacent `books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25207:end -->

<!-- delta:SF-2026-ARXIV-2606-25207:start -->
HPO agent 不替代单一 optimizer，而从多工具 proposal pool 选择；prefix-stable prompt 复用 KV，跨 iteration speculation 与 relative-error accept test 把 judge/tool latency 隐藏在 model evaluation 下。
<!-- delta:SF-2026-ARXIV-2606-25207:end -->

<!-- books-review:SF-2026-ARXIV-2606-25207:start -->
Direct Evolution; Integrate queued for root. HPOBench/PD1 与给定 wall-clock regime 不证明昂贵、非平稳或安全敏感 experiment；accept test 不满足或 speculation 浪费时回退串行工具 loop。
<!-- books-review:SF-2026-ARXIV-2606-25207:end -->

<!-- existing:SF-2026-ARXIV-2606-25215:start -->
Re-read `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` and adjacent `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-25215:end -->

<!-- delta:SF-2026-ARXIV-2606-25215:start -->
VLA state 从当前 observation 扩成 observation-action-consequence triplet buffer；shared attention 读历史后果，block-causal mask 防训练泄漏，KV cache 支撑实时滚动。
<!-- delta:SF-2026-ARXIV-2606-25215:end -->

<!-- books-review:SF-2026-ARXIV-2606-25215:start -->
Direct Evolution; Integrate queued for root. LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。
<!-- books-review:SF-2026-ARXIV-2606-25215:end -->

<!-- existing:SF-2026-ARXIV-2606-25274:start -->
At `books/part-07-agent/79-planning.md#L140`, the current owner already establishes the base responsibility for 以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退; `books/part-07-agent/80-reflection.md#L73` only consumes the handoff. It does not yet state `3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam`.
<!-- existing:SF-2026-ARXIV-2606-25274:end -->

<!-- delta:SF-2026-ARXIV-2606-25274:start -->
`3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25274:end -->

<!-- books-review:SF-2026-ARXIV-2606-25274:start -->
Direct Evolution; Integrate. `7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25274:end -->

<!-- existing:SF-2026-ARXIV-2606-25285:start -->
At `books/part-05-inference-system/54-gpu-memory.md#L186`, the current owner already establishes the base responsibility for 把稀疏、量化或压缩决策绑定到显存预算和质量回退; `books/part-05-inference-system/55-pd-disaggregation.md#L409` only consumes the handoff. It does not yet state `3 EPTS: Elastic Post-Training Sparsity`.
<!-- existing:SF-2026-ARXIV-2606-25285:end -->

<!-- delta:SF-2026-ARXIV-2606-25285:start -->
`3 EPTS: Elastic Post-Training Sparsity` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25285:end -->

<!-- books-review:SF-2026-ARXIV-2606-25285:start -->
Direct Evolution; Integrate. `Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25285:end -->

<!-- existing:SF-2026-ARXIV-2606-25296:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation`.
<!-- existing:SF-2026-ARXIV-2606-25296:end -->

<!-- delta:SF-2026-ARXIV-2606-25296:start -->
`SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25296:end -->

<!-- books-review:SF-2026-ARXIV-2606-25296:start -->
Direct Evolution; Integrate. `Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25296:end -->

<!-- existing:SF-2026-ARXIV-2606-25342:start -->
At `books/part-02-model/22-long-context.md#L374`, the current owner already establishes the base responsibility for 把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取; `books/part-02-model/19-kv-cache.md#L131` only consumes the handoff. It does not yet state `Parametric Attention and Lifelong In-Context Learning formulation`.
<!-- existing:SF-2026-ARXIV-2606-25342:end -->

<!-- delta:SF-2026-ARXIV-2606-25342:start -->
`Parametric Attention and Lifelong In-Context Learning formulation` 所定义的源特定机制用于把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25342:end -->

<!-- books-review:SF-2026-ARXIV-2606-25342:start -->
Direct Evolution; Integrate. `Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25342:end -->

<!-- existing:SF-2026-ARXIV-2606-25349:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation`.
<!-- existing:SF-2026-ARXIV-2606-25349:end -->

<!-- delta:SF-2026-ARXIV-2606-25349:start -->
`IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25349:end -->

<!-- books-review:SF-2026-ARXIV-2606-25349:start -->
Direct Evolution; Integrate. `VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25349:end -->

<!-- existing:SF-2026-ARXIV-2606-25353:start -->
At `books/part-05-inference-system/43-prefill.md#L33`, the current owner already establishes the base responsibility for 把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态; `books/part-05-inference-system/42-what-happens-during-inference.md#L117` only consumes the handoff. It does not yet state `3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation`.
<!-- existing:SF-2026-ARXIV-2606-25353:end -->

<!-- delta:SF-2026-ARXIV-2606-25353:start -->
`3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25353:end -->

<!-- books-review:SF-2026-ARXIV-2606-25353:start -->
Direct Evolution; Integrate. `7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25353:end -->

<!-- existing:SF-2026-ARXIV-2606-25366:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance`.
<!-- existing:SF-2026-ARXIV-2606-25366:end -->

<!-- delta:SF-2026-ARXIV-2606-25366:start -->
`III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25366:end -->

<!-- books-review:SF-2026-ARXIV-2606-25366:start -->
Direct Evolution; Integrate. `XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25366:end -->

<!-- existing:SF-2026-ARXIV-2606-25371:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `III Problem Setup; IV Conformal Recovery-Deadline Certificate`.
<!-- existing:SF-2026-ARXIV-2606-25371:end -->

<!-- delta:SF-2026-ARXIV-2606-25371:start -->
`III Problem Setup; IV Conformal Recovery-Deadline Certificate` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25371:end -->

<!-- books-review:SF-2026-ARXIV-2606-25371:start -->
Direct Evolution; Integrate. `VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25371:end -->

<!-- existing:SF-2026-ARXIV-2606-25388:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already establishes the base responsibility for 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `books/part-04-training-system/28-pretraining.md#L244` only consumes the handoff. It does not yet state `III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control`.
<!-- existing:SF-2026-ARXIV-2606-25388:end -->

<!-- delta:SF-2026-ARXIV-2606-25388:start -->
`III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25388:end -->

<!-- books-review:SF-2026-ARXIV-2606-25388:start -->
Direct Evolution; Integrate. `VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25388:end -->

<!-- existing:SF-2026-ARXIV-2606-25410:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already states the durable proposition that 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling` is confirmatory evidence, while `books/part-04-training-system/28-pretraining.md#L244` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25410:end -->

<!-- delta:SF-2026-ARXIV-2606-25410:start -->
`3 Proposed Method; 3.1 Importance Score Calculation; 3.2 Weight Rescaling` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25410:end -->

<!-- books-review:SF-2026-ARXIV-2606-25410:start -->
Layering / Dependency; No Change — Existing Coverage. `5 Conclusion; class-forgetting experimental scope` 是 `DFMU: Data-Frugal Machine Unlearning` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; 4.4 Results` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25410:end -->

<!-- existing:SF-2026-ARXIV-2606-25426:start -->
At `books/part-05-inference-system/43-prefill.md#L33`, the current owner already establishes the base responsibility for 把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态; `books/part-05-inference-system/42-what-happens-during-inference.md#L117` only consumes the handoff. It does not yet state `3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing`.
<!-- existing:SF-2026-ARXIV-2606-25426:end -->

<!-- delta:SF-2026-ARXIV-2606-25426:start -->
`3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25426:end -->

<!-- books-review:SF-2026-ARXIV-2606-25426:start -->
Direct Evolution; Integrate. `6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25426:end -->

<!-- existing:SF-2026-ARXIV-2606-25447:start -->
At `books/part-07-agent/81-workflow.md#L36`, the current owner already establishes the base responsibility for 把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态; `books/part-07-agent/78-tool-calling.md#L37` only consumes the handoff. It does not yet state `3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type`.
<!-- existing:SF-2026-ARXIV-2606-25447:end -->

<!-- delta:SF-2026-ARXIV-2606-25447:start -->
`3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25447:end -->

<!-- books-review:SF-2026-ARXIV-2606-25447:start -->
Direct Evolution; Integrate. `B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25447:end -->

<!-- existing:SF-2026-ARXIV-2606-25449:start -->
At `books/part-07-agent/77-memory.md#L900`, the current owner already establishes the base responsibility for 把动态记忆写入、回收与失效变成有 owner 的持久状态迁移; `books/part-07-agent/76-rag.md#L57` only consumes the handoff. It does not yet state `3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol`.
<!-- existing:SF-2026-ARXIV-2606-25449:end -->

<!-- delta:SF-2026-ARXIV-2606-25449:start -->
`3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25449:end -->

<!-- books-review:SF-2026-ARXIV-2606-25449:start -->
Direct Evolution; Integrate. `7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25449:end -->

<!-- existing:SF-2026-ARXIV-2606-25453:start -->
At `books/part-05-inference-system/49-tensorrt-llm.md#L630`, the current owner already establishes the base responsibility for 以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径; `books/part-05-inference-system/48-speculative-decoding.md#L113` only consumes the handoff. It does not yet state `III EmuGEMM-I; IV EmuGEMM-II`.
<!-- existing:SF-2026-ARXIV-2606-25453:end -->

<!-- delta:SF-2026-ARXIV-2606-25453:start -->
`III EmuGEMM-I; IV EmuGEMM-II` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25453:end -->

<!-- books-review:SF-2026-ARXIV-2606-25453:start -->
Direct Evolution; Integrate. `V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25453:end -->

<!-- existing:SF-2026-ARXIV-2606-25467:start -->
At `books/part-05-inference-system/56-inference-scheduling.md#L227`, the current owner already establishes the base responsibility for 让在线编排器共同持有请求资源耦合、准入和降级状态; `books/part-05-inference-system/46-continuous-batching.md#L75` only consumes the handoff. It does not yet state `III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration`.
<!-- existing:SF-2026-ARXIV-2606-25467:end -->

<!-- delta:SF-2026-ARXIV-2606-25467:start -->
`III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration` 所定义的源特定机制用于让在线编排器共同持有请求资源耦合、准入和降级状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25467:end -->

<!-- books-review:SF-2026-ARXIV-2606-25467:start -->
Direct Evolution; Integrate. `D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25467:end -->

<!-- existing:SF-2026-ARXIV-2606-25487:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `3 Setup; Appendix A Prompts, wrappers, and attack configuration`.
<!-- existing:SF-2026-ARXIV-2606-25487:end -->

<!-- delta:SF-2026-ARXIV-2606-25487:start -->
`3 Setup; Appendix A Prompts, wrappers, and attack configuration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25487:end -->

<!-- books-review:SF-2026-ARXIV-2606-25487:start -->
Direct Evolution; Integrate. `6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25487:end -->

<!-- existing:SF-2026-ARXIV-2606-25514:start -->
At `books/part-07-agent/82-multi-agent.md#L240`, the current owner already establishes the base responsibility for 把事件通信、角色分工与失败升级纳入多 Agent 协调状态; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication`.
<!-- existing:SF-2026-ARXIV-2606-25514:end -->

<!-- delta:SF-2026-ARXIV-2606-25514:start -->
`2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication` 所定义的源特定机制用于把事件通信、角色分工与失败升级纳入多 Agent 协调状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25514:end -->

<!-- books-review:SF-2026-ARXIV-2606-25514:start -->
Direct Evolution; Integrate. `5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25514:end -->

<!-- existing:SF-2026-ARXIV-2606-25519:start -->
At `books/part-05-inference-system/54-gpu-memory.md#L186`, the current owner already establishes the base responsibility for 把稀疏、量化或压缩决策绑定到显存预算和质量回退; `books/part-05-inference-system/55-pd-disaggregation.md#L409` only consumes the handoff. It does not yet state `3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy`.
<!-- existing:SF-2026-ARXIV-2606-25519:end -->

<!-- delta:SF-2026-ARXIV-2606-25519:start -->
`3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25519:end -->

<!-- books-review:SF-2026-ARXIV-2606-25519:start -->
Direct Evolution; Integrate. `7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25519:end -->

<!-- existing:SF-2026-ARXIV-2606-25532:start -->
At `books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L61`, the current owner already establishes the base responsibility for 把硬件约束和发现链纳入平台设计候选的验收边界; `books/part-06-ai-infrastructure/58-kubeflow.md#L71` only consumes the handoff. It does not yet state `Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought`.
<!-- existing:SF-2026-ARXIV-2606-25532:end -->

<!-- delta:SF-2026-ARXIV-2606-25532:start -->
`Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought` 所定义的源特定机制用于把硬件约束和发现链纳入平台设计候选的验收边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25532:end -->

<!-- books-review:SF-2026-ARXIV-2606-25532:start -->
Direct Evolution; Integrate. `Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25532:end -->

<!-- existing:SF-2026-ARXIV-2606-25548:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already states the durable proposition that 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `4 Transcoders-based Concept Removal; 4.1 BLOCK Framework` is confirmatory evidence, while `books/part-04-training-system/28-pretraining.md#L244` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25548:end -->

<!-- delta:SF-2026-ARXIV-2606-25548:start -->
`4 Transcoders-based Concept Removal; 4.1 BLOCK Framework` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25548:end -->

<!-- books-review:SF-2026-ARXIV-2606-25548:start -->
Layering / Dependency; No Change — Existing Coverage. `G Limitations; D.1 Model-Architecture-Dependent Subtleties` 是 `Concept Removal for Frontier Image Generative Models` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Evaluation; 5.1 Experimental Setup; 5.4 Robustness` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25548:end -->

<!-- existing:SF-2026-ARXIV-2606-25575:start -->
At `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L179`, the current owner already establishes the base responsibility for 把任务阶段、共享自治等级和人工接管手势纳入动作控制回路; `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L259` only consumes the handoff. It does not yet state `Variable-autonomy architecture; task-phase authority transfer; always-available release gesture`.
<!-- existing:SF-2026-ARXIV-2606-25575:end -->

<!-- delta:SF-2026-ARXIV-2606-25575:start -->
`Variable-autonomy architecture; task-phase authority transfer; always-available release gesture` 所定义的源特定机制用于把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25575:end -->

<!-- books-review:SF-2026-ARXIV-2606-25575:start -->
Direct Evolution; Integrate. `Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25575:end -->

<!-- existing:SF-2026-ARXIV-2606-25592:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `2 Visual Prompt Attack and Defense; 2.2 VPA-Guard`.
<!-- existing:SF-2026-ARXIV-2606-25592:end -->

<!-- delta:SF-2026-ARXIV-2606-25592:start -->
`2 Visual Prompt Attack and Defense; 2.2 VPA-Guard` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25592:end -->

<!-- books-review:SF-2026-ARXIV-2606-25592:start -->
Direct Evolution; Integrate. `E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25592:end -->

<!-- existing:SF-2026-ARXIV-2606-25605:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution`.
<!-- existing:SF-2026-ARXIV-2606-25605:end -->

<!-- delta:SF-2026-ARXIV-2606-25605:start -->
`3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25605:end -->

<!-- books-review:SF-2026-ARXIV-2606-25605:start -->
Direct Evolution; Integrate. `7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25605:end -->

<!-- existing:SF-2026-ARXIV-2606-25608:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already states the durable proposition that 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG` is confirmatory evidence, while `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25608:end -->

<!-- delta:SF-2026-ARXIV-2606-25608:start -->
`V Proposed Method: Multi-LLM System; V-B Multi-LLM architecture with HybridRAG` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25608:end -->

<!-- books-review:SF-2026-ARXIV-2606-25608:start -->
Layering / Dependency; No Change — Existing Coverage. `V-C Restrictions of our architecture; VII Future Research` 是 `An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `VI Initial Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25608:end -->

<!-- existing:SF-2026-ARXIV-2606-25622:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `IV Theoretical Framework: MAS Architecture and Experimental Setup`.
<!-- existing:SF-2026-ARXIV-2606-25622:end -->

<!-- delta:SF-2026-ARXIV-2606-25622:start -->
`IV Theoretical Framework: MAS Architecture and Experimental Setup` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25622:end -->

<!-- books-review:SF-2026-ARXIV-2606-25622:start -->
Direct Evolution; Integrate. `VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25622:end -->

<!-- existing:SF-2026-ARXIV-2606-25656:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization`.
<!-- existing:SF-2026-ARXIV-2606-25656:end -->

<!-- delta:SF-2026-ARXIV-2606-25656:start -->
`3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25656:end -->

<!-- books-review:SF-2026-ARXIV-2606-25656:start -->
Direct Evolution; Integrate. `6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25656:end -->

<!-- existing:SF-2026-ARXIV-2606-25658:start -->
At `books/part-07-agent/77-memory.md#L900`, the current owner already establishes the base responsibility for 把动态记忆写入、回收与失效变成有 owner 的持久状态迁移; `books/part-07-agent/76-rag.md#L57` only consumes the handoff. It does not yet state `3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank`.
<!-- existing:SF-2026-ARXIV-2606-25658:end -->

<!-- delta:SF-2026-ARXIV-2606-25658:start -->
`3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25658:end -->

<!-- books-review:SF-2026-ARXIV-2606-25658:start -->
Direct Evolution; Integrate. `A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25658:end -->

<!-- existing:SF-2026-ARXIV-2606-25674:start -->
At `books/part-07-agent/76-rag.md#L51`, the current owner already establishes the base responsibility for 把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态; `books/part-07-agent/77-memory.md#L113` only consumes the handoff. It does not yet state `3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization`.
<!-- existing:SF-2026-ARXIV-2606-25674:end -->

<!-- delta:SF-2026-ARXIV-2606-25674:start -->
`3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25674:end -->

<!-- books-review:SF-2026-ARXIV-2606-25674:start -->
Direct Evolution; Integrate. `4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25674:end -->

<!-- existing:SF-2026-ARXIV-2606-25700:start -->
At `books/part-04-training-system/30-lora.md#L145`, the current owner already states the durable proposition that 把秩、适配器容量与计算预算绑定为显式训练配置; `III Methods; III-B Training; III-C Architecture` is confirmatory evidence, while `books/part-04-training-system/29-sft.md#L194` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25700:end -->

<!-- delta:SF-2026-ARXIV-2606-25700:start -->
`III Methods; III-B Training; III-C Architecture` 所定义的源特定机制用于把秩、适配器容量与计算预算绑定为显式训练配置；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25700:end -->

<!-- books-review:SF-2026-ARXIV-2606-25700:start -->
Layering / Dependency; No Change — Existing Coverage. `V Discussion; V-A Choice of rank; V-C Computation` 是 `Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning` 的 source-specific 反例/局限边界；若运行条件离开 `IV Results; IV-B Computation calculation` 的验证域，`TRAIN-LORA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25700:end -->

<!-- existing:SF-2026-ARXIV-2606-25705:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator`.
<!-- existing:SF-2026-ARXIV-2606-25705:end -->

<!-- delta:SF-2026-ARXIV-2606-25705:start -->
`3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25705:end -->

<!-- books-review:SF-2026-ARXIV-2606-25705:start -->
Direct Evolution; Integrate. `5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25705:end -->

<!-- existing:SF-2026-ARXIV-2606-25721:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification`.
<!-- existing:SF-2026-ARXIV-2606-25721:end -->

<!-- delta:SF-2026-ARXIV-2606-25721:start -->
`4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25721:end -->

<!-- books-review:SF-2026-ARXIV-2606-25721:start -->
Direct Evolution; Integrate. `6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25721:end -->

<!-- existing:SF-2026-ARXIV-2606-25759:start -->
At `books/part-04-training-system/36-distributed-training.md#L646`, the current owner already establishes the base responsibility for 把集群运行剖面映射为运行时 bucket 与并行绑定状态; `books/part-04-training-system/37-tensor-parallel.md#L243` only consumes the handoff. It does not yet state `3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing`.
<!-- existing:SF-2026-ARXIV-2606-25759:end -->

<!-- delta:SF-2026-ARXIV-2606-25759:start -->
`3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing` 所定义的源特定机制用于把集群运行剖面映射为运行时 bucket 与并行绑定状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25759:end -->

<!-- books-review:SF-2026-ARXIV-2606-25759:start -->
Direct Evolution; Integrate. `9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25759:end -->

<!-- existing:SF-2026-ARXIV-2606-25760:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks`.
<!-- existing:SF-2026-ARXIV-2606-25760:end -->

<!-- delta:SF-2026-ARXIV-2606-25760:start -->
`3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25760:end -->

<!-- books-review:SF-2026-ARXIV-2606-25760:start -->
Direct Evolution; Integrate. `A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25760:end -->

<!-- existing:SF-2026-ARXIV-2606-25782:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel`.
<!-- existing:SF-2026-ARXIV-2606-25782:end -->

<!-- delta:SF-2026-ARXIV-2606-25782:start -->
`2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25782:end -->

<!-- books-review:SF-2026-ARXIV-2606-25782:start -->
Direct Evolution; Integrate. `OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25782:end -->

<!-- existing:SF-2026-ARXIV-2606-25797:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already states the durable proposition that 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC` is confirmatory evidence, while `books/part-06-ai-infrastructure/59-model-registry.md#L118` remains a consumer rather than a second owner.
<!-- existing:SF-2026-ARXIV-2606-25797:end -->

<!-- delta:SF-2026-ARXIV-2606-25797:start -->
`3 Improving Online MDP-SMC; 3.2 Confidence Sequences; 3.4 Confidence Sequence MDP-SMC` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25797:end -->

<!-- books-review:SF-2026-ARXIV-2606-25797:start -->
Layering / Dependency; No Change — Existing Coverage. `0.A Assumptions on Sampling Access and Knowledge; 0.B Reusing Confidence is Incorrect` 是 `Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes` 的 source-specific 反例/局限边界；若运行条件离开 `4 Implementation and Experimental Evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25797:end -->

<!-- existing:SF-2026-ARXIV-2606-25819:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection`.
<!-- existing:SF-2026-ARXIV-2606-25819:end -->

<!-- delta:SF-2026-ARXIV-2606-25819:start -->
`ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25819:end -->

<!-- books-review:SF-2026-ARXIV-2606-25819:start -->
Direct Evolution; Integrate. `Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25819:end -->

<!-- existing:SF-2026-ARXIV-2606-25838:start -->
At `books/part-05-inference-system/42-what-happens-during-inference.md#L80`, the current owner already establishes the base responsibility for 让路由器基于请求置信度持有后端选择与回退权; `books/part-05-inference-system/43-prefill.md#L33` only consumes the handoff. It does not yet state `III Method; IV Confidence-Aware Routing`.
<!-- existing:SF-2026-ARXIV-2606-25838:end -->

<!-- delta:SF-2026-ARXIV-2606-25838:start -->
`III Method; IV Confidence-Aware Routing` 所定义的源特定机制用于让路由器基于请求置信度持有后端选择与回退权；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25838:end -->

<!-- books-review:SF-2026-ARXIV-2606-25838:start -->
Direct Evolution; Integrate. `VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25838:end -->

<!-- existing:SF-2026-ARXIV-2606-25863:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution`.
<!-- existing:SF-2026-ARXIV-2606-25863:end -->

<!-- delta:SF-2026-ARXIV-2606-25863:start -->
`PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25863:end -->

<!-- books-review:SF-2026-ARXIV-2606-25863:start -->
Direct Evolution; Integrate. `PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25863:end -->

<!-- existing:SF-2026-ARXIV-2606-25871:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already establishes the base responsibility for 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `books/part-04-training-system/28-pretraining.md#L244` only consumes the handoff. It does not yet state `3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic`.
<!-- existing:SF-2026-ARXIV-2606-25871:end -->

<!-- delta:SF-2026-ARXIV-2606-25871:start -->
`3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25871:end -->

<!-- books-review:SF-2026-ARXIV-2606-25871:start -->
Direct Evolution; Integrate. `5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25871:end -->

<!-- existing:SF-2026-ARXIV-2606-25987:start -->
At `books/part-07-agent/78-tool-calling.md#L55`, the current owner already establishes the base responsibility for 把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前; `books/part-07-agent/81-workflow.md#L36` only consumes the handoff. It does not yet state `3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought`.
<!-- existing:SF-2026-ARXIV-2606-25987:end -->

<!-- delta:SF-2026-ARXIV-2606-25987:start -->
`3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25987:end -->

<!-- books-review:SF-2026-ARXIV-2606-25987:start -->
Direct Evolution; Integrate. `6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25987:end -->

<!-- existing:SF-2026-ARXIV-2606-25996:start -->
At `books/part-04-training-system/27-data.md#L130`, the current owner already establishes the base responsibility for 把数据选择、校准或验证结果变成训练前可审计的数据控制状态; `books/part-04-training-system/28-pretraining.md#L244` only consumes the handoff. It does not yet state `2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist`.
<!-- existing:SF-2026-ARXIV-2606-25996:end -->

<!-- delta:SF-2026-ARXIV-2606-25996:start -->
`2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-25996:end -->

<!-- books-review:SF-2026-ARXIV-2606-25996:start -->
Direct Evolution; Integrate. `6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-25996:end -->

<!-- existing:SF-2026-ARXIV-2606-26021:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `V Attention-based MIA; VI Inference-Time Hardening Against MIAs`.
<!-- existing:SF-2026-ARXIV-2606-26021:end -->

<!-- delta:SF-2026-ARXIV-2606-26021:start -->
`V Attention-based MIA; VI Inference-Time Hardening Against MIAs` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26021:end -->

<!-- books-review:SF-2026-ARXIV-2606-26021:start -->
Direct Evolution; Integrate. `VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26021:end -->

<!-- existing:SF-2026-ARXIV-2606-26027:start -->
At `books/part-04-training-system/33-grpo.md#L231`, the current owner already establishes the base responsibility for 把崩溃信号与监督修复绑定到策略更新门控; `books/part-04-training-system/32-ppo.md#L330` only consumes the handoff. It does not yet state `4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes`.
<!-- existing:SF-2026-ARXIV-2606-26027:end -->

<!-- delta:SF-2026-ARXIV-2606-26027:start -->
`4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes` 所定义的源特定机制用于把崩溃信号与监督修复绑定到策略更新门控；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26027:end -->

<!-- books-review:SF-2026-ARXIV-2606-26027:start -->
Direct Evolution; Integrate. `B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26027:end -->

<!-- existing:SF-2026-ARXIV-2606-26028:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `3 System Model: ERC-8004 Protocol; 7 Reputation Market Security`.
<!-- existing:SF-2026-ARXIV-2606-26028:end -->

<!-- delta:SF-2026-ARXIV-2606-26028:start -->
`3 System Model: ERC-8004 Protocol; 7 Reputation Market Security` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26028:end -->

<!-- books-review:SF-2026-ARXIV-2606-26028:start -->
Direct Evolution; Integrate. `9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26028:end -->

<!-- existing:SF-2026-ARXIV-2606-26057:start -->
At `books/part-06-ai-infrastructure/72-security.md#L204`, the current owner already establishes the base responsibility for 把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界; `books/part-06-ai-infrastructure/71-multi-tenant.md#L33` only consumes the handoff. It does not yet state `2 Threat Model; 3 Requirements; 4 Design; 5 Implementation`.
<!-- existing:SF-2026-ARXIV-2606-26057:end -->

<!-- delta:SF-2026-ARXIV-2606-26057:start -->
`2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26057:end -->

<!-- books-review:SF-2026-ARXIV-2606-26057:start -->
Direct Evolution; Integrate. `8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26057:end -->

<!-- existing:SF-2026-ARXIV-2606-26071:start -->
At `books/part-06-ai-infrastructure/66-evaluation-system.md#L136`, the current owner already establishes the base responsibility for 把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态; `books/part-06-ai-infrastructure/59-model-registry.md#L118` only consumes the handoff. It does not yet state `4 Protocol and Methods; 5 Environments; 7 Methodological Insights`.
<!-- existing:SF-2026-ARXIV-2606-26071:end -->

<!-- delta:SF-2026-ARXIV-2606-26071:start -->
`4 Protocol and Methods; 5 Environments; 7 Methodological Insights` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- delta:SF-2026-ARXIV-2606-26071:end -->

<!-- books-review:SF-2026-ARXIV-2606-26071:start -->
Direct Evolution; Integrate. `10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
<!-- books-review:SF-2026-ARXIV-2606-26071:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260625-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260625 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260625: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260625-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-24898; review:SF-2026-ARXIV-2606-24934; review:SF-2026-ARXIV-2606-24957; review:SF-2026-ARXIV-2606-24996; review:SF-2026-ARXIV-2606-24998; review:SF-2026-ARXIV-2606-25040; review:SF-2026-ARXIV-2606-25082; review:SF-2026-ARXIV-2606-25091; review:SF-2026-ARXIV-2606-25097; review:SF-2026-ARXIV-2606-25098; review:SF-2026-ARXIV-2606-25115; review:SF-2026-ARXIV-2606-25156; review:SF-2026-ARXIV-2606-25161; review:SF-2026-ARXIV-2606-25178; review:SF-2026-ARXIV-2606-25189; review:SF-2026-ARXIV-2606-25191; review:SF-2026-ARXIV-2606-25198; review:SF-2026-ARXIV-2606-25207; review:SF-2026-ARXIV-2606-25215; review:SF-2026-ARXIV-2606-25274; review:SF-2026-ARXIV-2606-25285; review:SF-2026-ARXIV-2606-25296; review:SF-2026-ARXIV-2606-25342; review:SF-2026-ARXIV-2606-25349; review:SF-2026-ARXIV-2606-25353; review:SF-2026-ARXIV-2606-25366; review:SF-2026-ARXIV-2606-25371; review:SF-2026-ARXIV-2606-25388; review:SF-2026-ARXIV-2606-25410; review:SF-2026-ARXIV-2606-25426; review:SF-2026-ARXIV-2606-25447; review:SF-2026-ARXIV-2606-25449; review:SF-2026-ARXIV-2606-25453; review:SF-2026-ARXIV-2606-25467; review:SF-2026-ARXIV-2606-25487; review:SF-2026-ARXIV-2606-25514; review:SF-2026-ARXIV-2606-25519; review:SF-2026-ARXIV-2606-25532; review:SF-2026-ARXIV-2606-25548; review:SF-2026-ARXIV-2606-25575; review:SF-2026-ARXIV-2606-25592; review:SF-2026-ARXIV-2606-25605; review:SF-2026-ARXIV-2606-25608; review:SF-2026-ARXIV-2606-25622; review:SF-2026-ARXIV-2606-25656; review:SF-2026-ARXIV-2606-25658; review:SF-2026-ARXIV-2606-25674; review:SF-2026-ARXIV-2606-25700; review:SF-2026-ARXIV-2606-25705; review:SF-2026-ARXIV-2606-25721; review:SF-2026-ARXIV-2606-25759; review:SF-2026-ARXIV-2606-25760; review:SF-2026-ARXIV-2606-25782; review:SF-2026-ARXIV-2606-25797; review:SF-2026-ARXIV-2606-25819; review:SF-2026-ARXIV-2606-25838; review:SF-2026-ARXIV-2606-25863; review:SF-2026-ARXIV-2606-25871; review:SF-2026-ARXIV-2606-25987; review:SF-2026-ARXIV-2606-25996; review:SF-2026-ARXIV-2606-26021; review:SF-2026-ARXIV-2606-26027; review:SF-2026-ARXIV-2606-26028; review:SF-2026-ARXIV-2606-26057; review:SF-2026-ARXIV-2606-26071 | EVIDENCE-OWNER-REBUILD-20260625: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260625-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis:DA-20260613-READOUT-BLIND-SPOT; analysis-decision:SF-2026-ARXIV-2606-24934; analysis-decision:SF-2026-ARXIV-2606-24957; analysis-decision:SF-2026-ARXIV-2606-24996; analysis-decision:SF-2026-ARXIV-2606-24998; analysis-decision:SF-2026-ARXIV-2606-25040; analysis-decision:SF-2026-ARXIV-2606-25082; analysis-decision:SF-2026-ARXIV-2606-25091; analysis-decision:SF-2026-ARXIV-2606-25097; analysis-decision:SF-2026-ARXIV-2606-25098; analysis-decision:SF-2026-ARXIV-2606-25115; analysis-decision:SF-2026-ARXIV-2606-25156; analysis-decision:SF-2026-ARXIV-2606-25161; analysis-decision:SF-2026-ARXIV-2606-25178; analysis:DA-20260624-2606-25189; analysis-decision:SF-2026-ARXIV-2606-25191; analysis-decision:SF-2026-ARXIV-2606-25198; analysis-decision:SF-2026-ARXIV-2606-25207; analysis-decision:SF-2026-ARXIV-2606-25215; analysis-decision:SF-2026-ARXIV-2606-25274; analysis-decision:SF-2026-ARXIV-2606-25285; analysis-decision:SF-2026-ARXIV-2606-25296; analysis-decision:SF-2026-ARXIV-2606-25342; analysis-decision:SF-2026-ARXIV-2606-25349; analysis-decision:SF-2026-ARXIV-2606-25353; analysis-decision:SF-2026-ARXIV-2606-25366; analysis-decision:SF-2026-ARXIV-2606-25371; analysis-decision:SF-2026-ARXIV-2606-25388; analysis-decision:SF-2026-ARXIV-2606-25410; analysis-decision:SF-2026-ARXIV-2606-25426; analysis-decision:SF-2026-ARXIV-2606-25447; analysis-decision:SF-2026-ARXIV-2606-25449; analysis-decision:SF-2026-ARXIV-2606-25453; analysis-decision:SF-2026-ARXIV-2606-25467; analysis-decision:SF-2026-ARXIV-2606-25487; analysis-decision:SF-2026-ARXIV-2606-25514; analysis-decision:SF-2026-ARXIV-2606-25519; analysis-decision:SF-2026-ARXIV-2606-25532; analysis-decision:SF-2026-ARXIV-2606-25548; analysis-decision:SF-2026-ARXIV-2606-25575; analysis-decision:SF-2026-ARXIV-2606-25592; analysis-decision:SF-2026-ARXIV-2606-25605; analysis-decision:SF-2026-ARXIV-2606-25608; analysis-decision:SF-2026-ARXIV-2606-25622; analysis-decision:SF-2026-ARXIV-2606-25656; analysis-decision:SF-2026-ARXIV-2606-25658; analysis-decision:SF-2026-ARXIV-2606-25674; analysis-decision:SF-2026-ARXIV-2606-25700; analysis-decision:SF-2026-ARXIV-2606-25705; analysis-decision:SF-2026-ARXIV-2606-25721; analysis-decision:SF-2026-ARXIV-2606-25759; analysis-decision:SF-2026-ARXIV-2606-25760; analysis-decision:SF-2026-ARXIV-2606-25782; analysis-decision:SF-2026-ARXIV-2606-25797; analysis-decision:SF-2026-ARXIV-2606-25819; analysis-decision:SF-2026-ARXIV-2606-25838; analysis-decision:SF-2026-ARXIV-2606-25863; analysis-decision:SF-2026-ARXIV-2606-25871; analysis-decision:SF-2026-ARXIV-2606-25987; analysis-decision:SF-2026-ARXIV-2606-25996; analysis-decision:SF-2026-ARXIV-2606-26021; analysis-decision:SF-2026-ARXIV-2606-26027; analysis-decision:SF-2026-ARXIV-2606-26028; analysis:DA-20260625-2606-26057; analysis-decision:SF-2026-ARXIV-2606-26071 | SELECTION-OWNER-REBUILD-20260625: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260625-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-24898; books-review:SF-2026-ARXIV-2606-24934; books-review:SF-2026-ARXIV-2606-24957; books-review:SF-2026-ARXIV-2606-24996; books-review:SF-2026-ARXIV-2606-24998; books-review:SF-2026-ARXIV-2606-25040; books-review:SF-2026-ARXIV-2606-25082; books-review:SF-2026-ARXIV-2606-25091; books-review:SF-2026-ARXIV-2606-25097; books-review:SF-2026-ARXIV-2606-25098; books-review:SF-2026-ARXIV-2606-25115; books-review:SF-2026-ARXIV-2606-25156; books-review:SF-2026-ARXIV-2606-25161; books-review:SF-2026-ARXIV-2606-25178; books-review:SF-2026-ARXIV-2606-25189; books-review:SF-2026-ARXIV-2606-25191; books-review:SF-2026-ARXIV-2606-25198; books-review:SF-2026-ARXIV-2606-25207; books-review:SF-2026-ARXIV-2606-25215; books-review:SF-2026-ARXIV-2606-25274; books-review:SF-2026-ARXIV-2606-25285; books-review:SF-2026-ARXIV-2606-25296; books-review:SF-2026-ARXIV-2606-25342; books-review:SF-2026-ARXIV-2606-25349; books-review:SF-2026-ARXIV-2606-25353; books-review:SF-2026-ARXIV-2606-25366; books-review:SF-2026-ARXIV-2606-25371; books-review:SF-2026-ARXIV-2606-25388; books-review:SF-2026-ARXIV-2606-25410; books-review:SF-2026-ARXIV-2606-25426; books-review:SF-2026-ARXIV-2606-25447; books-review:SF-2026-ARXIV-2606-25449; books-review:SF-2026-ARXIV-2606-25453; books-review:SF-2026-ARXIV-2606-25467; books-review:SF-2026-ARXIV-2606-25487; books-review:SF-2026-ARXIV-2606-25514; books-review:SF-2026-ARXIV-2606-25519; books-review:SF-2026-ARXIV-2606-25532; books-review:SF-2026-ARXIV-2606-25548; books-review:SF-2026-ARXIV-2606-25575; books-review:SF-2026-ARXIV-2606-25592; books-review:SF-2026-ARXIV-2606-25605; books-review:SF-2026-ARXIV-2606-25608; books-review:SF-2026-ARXIV-2606-25622; books-review:SF-2026-ARXIV-2606-25656; books-review:SF-2026-ARXIV-2606-25658; books-review:SF-2026-ARXIV-2606-25674; books-review:SF-2026-ARXIV-2606-25700; books-review:SF-2026-ARXIV-2606-25705; books-review:SF-2026-ARXIV-2606-25721; books-review:SF-2026-ARXIV-2606-25759; books-review:SF-2026-ARXIV-2606-25760; books-review:SF-2026-ARXIV-2606-25782; books-review:SF-2026-ARXIV-2606-25797; books-review:SF-2026-ARXIV-2606-25819; books-review:SF-2026-ARXIV-2606-25838; books-review:SF-2026-ARXIV-2606-25863; books-review:SF-2026-ARXIV-2606-25871; books-review:SF-2026-ARXIV-2606-25987; books-review:SF-2026-ARXIV-2606-25996; books-review:SF-2026-ARXIV-2606-26021; books-review:SF-2026-ARXIV-2606-26027; books-review:SF-2026-ARXIV-2606-26028; books-review:SF-2026-ARXIV-2606-26057; books-review:SF-2026-ARXIV-2606-26071 | BOOKS-OWNER-REBUILD-20260625: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

The 442 family-specific closures remain row-addressable in `denominator-full-semantic-audit-v1.tsv`; keyword routing was recall-only and all 127 route-negative identities were audited.

### Materials and Access

- 68/68 retained families completed official exact-v1 primary-source review. Official arXiv HTML was used except `2606.25863v1`, whose exact-v1 official PDF was the recorded fallback; no abstract-text anchor was used.

## 9. Recommended Action

- Final Books disposition: 63 Integrate across 25 unique owner files; 5 No Change handoffs.
- Books Gate passed after the 68/68 post-write fresh audit.
- Preserve the frozen denominator and reopen only when versioned primary evidence changes a recorded mechanism, owner, evaluation contract or non-proof boundary.

## 10. Repository Changes

- The accepted 63-family writeback remains in 25 shared Books owner files; this canonical migration changed only the 2026-06-25 Daily, its date-local packet and date-specific validation scripts.
- `docs/LEARNING_STATE.md` and monthly indexes remained read-only.

## 11. Open Questions

- Which exact-v1 mechanisms remain stable under unseen workloads is future research, not an unresolved Gate finding.
- Which runtime calibration values remain stable after model, hardware or workload distribution changes is a research continuation, not an unresolved Gate finding.

## 12. Sources

- [Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models](https://arxiv.org/abs/2606.24898v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Unprivileged Topology Certificates for Cloud GPU Attestation](https://arxiv.org/abs/2606.24934v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding](https://arxiv.org/abs/2606.24957v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [From Forecasting Leaderboards to Deployment Decisions: A Fail-Closed Certification Protocol](https://arxiv.org/abs/2606.24996v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Internal Data Repetition Destroys Language Models](https://arxiv.org/abs/2606.24998v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Chorus II: Cross-Request Sparsity Reuse for Efficient Image-to-Video Generation](https://arxiv.org/abs/2606.25040v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Energy Efficient Scheduling of AI/ML Workloads on Multi Instance GPUs with Dynamic Repartitioning](https://arxiv.org/abs/2606.25082v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off](https://arxiv.org/abs/2606.25091v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion](https://arxiv.org/abs/2606.25097v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Power-Flexible AI Data Centers: A New Paradigm for Grid-Responsive Compute](https://arxiv.org/abs/2606.25098v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory](https://arxiv.org/abs/2606.25115v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [ATMA: Long-Context Language Modeling via Polar Attention and Gated-Delta Compression Memory](https://arxiv.org/abs/2606.25156v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory](https://arxiv.org/abs/2606.25161v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR](https://arxiv.org/abs/2606.25178v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses](https://arxiv.org/abs/2606.25189v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG](https://arxiv.org/abs/2606.25191v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty](https://arxiv.org/abs/2606.25198v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [ASAP: Agent-System Co-Design for Wall-Clock-Centered Auto HPO Research for ML Experiments](https://arxiv.org/abs/2606.25207v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Reflective VLA: In-Context Action Consequences Make VLAs Generalize](https://arxiv.org/abs/2606.25215v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control](https://arxiv.org/abs/2606.25274v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression](https://arxiv.org/abs/2606.25285v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety](https://arxiv.org/abs/2606.25296v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention](https://arxiv.org/abs/2606.25342v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference](https://arxiv.org/abs/2606.25349v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Cache-Resident LLM Inference in GB-Scale Last-Level Caches](https://arxiv.org/abs/2606.25353v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield](https://arxiv.org/abs/2606.25366v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers](https://arxiv.org/abs/2606.25371v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning](https://arxiv.org/abs/2606.25388v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [DFMU: Data-Frugal Machine Unlearning](https://arxiv.org/abs/2606.25410v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX](https://arxiv.org/abs/2606.25426v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/abs/2606.25447v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One](https://arxiv.org/abs/2606.25449v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication](https://arxiv.org/abs/2606.25453v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs](https://arxiv.org/abs/2606.25467v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring](https://arxiv.org/abs/2606.25487v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution](https://arxiv.org/abs/2606.25514v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models](https://arxiv.org/abs/2606.25519v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Agentic evolution of physically constrained foundation models](https://arxiv.org/abs/2606.25532v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Concept Removal for Frontier Image Generative Models](https://arxiv.org/abs/2606.25548v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand](https://arxiv.org/abs/2606.25575v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks](https://arxiv.org/abs/2606.25592v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints](https://arxiv.org/abs/2606.25605v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz](https://arxiv.org/abs/2606.25608v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz](https://arxiv.org/abs/2606.25622v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization](https://arxiv.org/abs/2606.25656v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding](https://arxiv.org/abs/2606.25658v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [BitNet Text Embeddings](https://arxiv.org/abs/2606.25674v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning](https://arxiv.org/abs/2606.25700v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [GUI agent: Guided Exploration of User-Sensitive Screens](https://arxiv.org/abs/2606.25705v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](https://arxiv.org/abs/2606.25721v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication](https://arxiv.org/abs/2606.25759v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets](https://arxiv.org/abs/2606.25760v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation](https://arxiv.org/abs/2606.25782v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes](https://arxiv.org/abs/2606.25797v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability](https://arxiv.org/abs/2606.25819v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines](https://arxiv.org/abs/2606.25838v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis](https://arxiv.org/abs/2606.25863v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search](https://arxiv.org/abs/2606.25871v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Weave of Formal Thought](https://arxiv.org/abs/2606.25987v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Autodata: An agentic data scientist to create high quality synthetic data](https://arxiv.org/abs/2606.25996v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries](https://arxiv.org/abs/2606.26021v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/abs/2606.26027v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem](https://arxiv.org/abs/2606.26028v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
- [Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/abs/2606.26071v1) — first-public（Asia/Shanghai）：2026-06-25；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`Passed`；Completion Status=`Complete`；unresolved findings: `0`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=1。
