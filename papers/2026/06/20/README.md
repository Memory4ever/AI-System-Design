# Daily Research — 2026-06-20

**Research Date:** 2026-06-20

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-19 09:00:00 ～ 2026-06-20 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary

Beijing window `[2026-06-19 09:00, 2026-06-20 09:00)` contains 385 registered identities. Full 385/385 title+abstract review freezes 65 durable families and 320 family-specific closures (retain rate 16.88%). The 92/92 route-negative false-negative audit recovered 6 durable families; the 83-item proposed pool's false-positive review closed 25 items, including the second-pass closure of 2606.21451 and 2606.21749. Exact-v1 Evidence is complete for 65/65: 63 official HTML, one author-project/repository fallback and one exact-identity author-manuscript mirror fallback. Selection compares all 65 and chooses three narrative units. Books comparison is complete; 44 Integrate proposals are owner-merged into 19 files and 21 are No Change. Root wrote 44 Integrate families into 19 owners; the 65/65 post-write fresh audit passed with zero unresolved findings. This date is Complete.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-20 |
| Window End | 2026-06-20 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-20:811faa010c5754bc |
| Denominator Frozen At | 2026-08-29T22:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-19T09:00:00+08:00 | 2026-06-20T09:00:00+08:00 | 2026-08-29T22:40:00+08:00 | frozen DataCite DOI-prefix snapshots; full registered Core plus topic routes | checked | 385 | SF-2026-ARXIV-2606-21023; SF-2026-ARXIV-2606-21024; SF-2026-ARXIV-2606-21037; SF-2026-ARXIV-2606-21045; SF-2026-ARXIV-2606-21071; SF-2026-ARXIV-2606-21077; SF-2026-ARXIV-2606-21083; SF-2026-ARXIV-2606-21088; SF-2026-ARXIV-2606-21101; SF-2026-ARXIV-2606-21121; SF-2026-ARXIV-2606-21126; SF-2026-ARXIV-2606-21129; SF-2026-ARXIV-2606-21130; SF-2026-ARXIV-2606-21140; SF-2026-ARXIV-2606-21144; SF-2026-ARXIV-2606-21172; SF-2026-ARXIV-2606-21173; SF-2026-ARXIV-2606-21188; SF-2026-ARXIV-2606-21228; SF-2026-ARXIV-2606-21238; SF-2026-ARXIV-2606-21249; SF-2026-ARXIV-2606-21255; SF-2026-ARXIV-2606-21257; SF-2026-ARXIV-2606-21262; SF-2026-ARXIV-2606-21282; SF-2026-ARXIV-2606-21307; SF-2026-ARXIV-2606-21315; SF-2026-ARXIV-2606-21337; SF-2026-ARXIV-2606-21338; SF-2026-ARXIV-2606-21359; SF-2026-ARXIV-2606-21372; SF-2026-ARXIV-2606-21386; SF-2026-ARXIV-2606-21389; SF-2026-ARXIV-2606-21398; SF-2026-ARXIV-2606-21399; SF-2026-ARXIV-2606-21401; SF-2026-ARXIV-2606-21406; SF-2026-ARXIV-2606-21409; SF-2026-ARXIV-2606-21428; SF-2026-ARXIV-2606-21445; SF-2026-ARXIV-2606-21509; SF-2026-ARXIV-2606-21514; SF-2026-ARXIV-2606-21553; SF-2026-ARXIV-2606-21565; SF-2026-ARXIV-2606-21572; SF-2026-ARXIV-2606-21584; SF-2026-ARXIV-2606-21627; SF-2026-ARXIV-2606-21633; SF-2026-ARXIV-2606-21638; SF-2026-ARXIV-2606-21654; SF-2026-ARXIV-2606-21666; SF-2026-ARXIV-2606-21678; SF-2026-ARXIV-2606-21710; SF-2026-ARXIV-2606-21712; SF-2026-ARXIV-2606-21732; SF-2026-ARXIV-2606-21775; SF-2026-ARXIV-2606-21777; SF-2026-ARXIV-2606-21787; SF-2026-ARXIV-2606-21795; SF-2026-ARXIV-2606-21803; SF-2026-ARXIV-2606-21804; SF-2026-ARXIV-2606-21807; SF-2026-ARXIV-2606-21811; SF-2026-ARXIV-2606-28376; SF-2026-ARXIV-2606-28379 | pages=40; final_cursor=end; 385 unique identities | 2026-06-20T01:00:00Z | ../_sources/daily-20260620/screening-ledger.json; ../_sources/daily-20260620/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260620 | — |

<!-- coverage:SRC-ARXIV:20260620:start -->
Full 385/385 title+abstract audit: 255 Core, 38 keyword-routed and 92 route-negative; final arithmetic `385 = 65 retained + 320 closures`. Keyword routing supplied recall only. Route-negative retained=6; proposed-pool false positives closed=25.
<!-- coverage:SRC-ARXIV:20260620:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21023 | arXiv:2606.21023v1 | paper-v1:2606.21023 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21023 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-21023 | yes |
| SF-2026-ARXIV-2606-21024 | arXiv:2606.21024v1 | paper-v1:2606.21024 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21024 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21024 | yes |
| SF-2026-ARXIV-2606-21037 | arXiv:2606.21037v1 | paper-v1:2606.21037 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21037 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21037 | yes |
| SF-2026-ARXIV-2606-21045 | arXiv:2606.21045v1 | paper-v1:2606.21045 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21045 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21045 | yes |
| SF-2026-ARXIV-2606-21071 | arXiv:2606.21071v1 | paper-v1:2606.21071 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21071 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21071 | yes |
| SF-2026-ARXIV-2606-21077 | arXiv:2606.21077v1 | paper-v1:2606.21077 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21077 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21077 | yes |
| SF-2026-ARXIV-2606-21083 | arXiv:2606.21083v1 | paper-v1:2606.21083 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21083 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21083 | yes |
| SF-2026-ARXIV-2606-21088 | arXiv:2606.21088v1 | paper-v1:2606.21088 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21088 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21088 | yes |
| SF-2026-ARXIV-2606-21101 | arXiv:2606.21101v1 | paper-v1:2606.21101 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21101 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-21101 | yes |
| SF-2026-ARXIV-2606-21121 | arXiv:2606.21121v1 | paper-v1:2606.21121 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21121 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-21121 | yes |
| SF-2026-ARXIV-2606-21126 | arXiv:2606.21126v1 | paper-v1:2606.21126 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21126 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21126 | yes |
| SF-2026-ARXIV-2606-21129 | arXiv:2606.21129v1 | paper-v1:2606.21129 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21129 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21129 | yes |
| SF-2026-ARXIV-2606-21130 | arXiv:2606.21130v1 | paper-v1:2606.21130 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21130 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-21130 | yes |
| SF-2026-ARXIV-2606-21140 | arXiv:2606.21140v1 | paper-v1:2606.21140 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21140 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21140 | yes |
| SF-2026-ARXIV-2606-21144 | arXiv:2606.21144v1 | paper-v1:2606.21144 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21144 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21144 | yes |
| SF-2026-ARXIV-2606-21172 | arXiv:2606.21172v1 | paper-v1:2606.21172 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21172 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21172 | yes |
| SF-2026-ARXIV-2606-21173 | arXiv:2606.21173v1 | paper-v1:2606.21173 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21173 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-21173 | yes |
| SF-2026-ARXIV-2606-21188 | arXiv:2606.21188v1 | paper-v1:2606.21188 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21188 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21188 | yes |
| SF-2026-ARXIV-2606-21228 | arXiv:2606.21228v1 | paper-v1:2606.21228 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21228 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-21228 | yes |
| SF-2026-ARXIV-2606-21238 | arXiv:2606.21238v1 | paper-v1:2606.21238 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21238 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-21238 | yes |
| SF-2026-ARXIV-2606-21249 | arXiv:2606.21249v1 | paper-v1:2606.21249 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21249 | self | — | new_in_window | MODEL-POSITION-ENCODING | Integrate | books-review:SF-2026-ARXIV-2606-21249 | yes |
| SF-2026-ARXIV-2606-21255 | arXiv:2606.21255v1 | paper-v1:2606.21255 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21255 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21255 | yes |
| SF-2026-ARXIV-2606-21257 | arXiv:2606.21257v1 | paper-v1:2606.21257 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21257 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21257 | yes |
| SF-2026-ARXIV-2606-21262 | arXiv:2606.21262v1 | paper-v1:2606.21262 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21262 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21262 | yes |
| SF-2026-ARXIV-2606-21282 | arXiv:2606.21282v1 | paper-v1:2606.21282 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21282 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21282 | yes |
| SF-2026-ARXIV-2606-21307 | arXiv:2606.21307v1 | paper-v1:2606.21307 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21307 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21307 | yes |
| SF-2026-ARXIV-2606-21315 | arXiv:2606.21315v1 | paper-v1:2606.21315 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21315 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-21315 | yes |
| SF-2026-ARXIV-2606-21337 | arXiv:2606.21337v1 | paper-v1:2606.21337 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21337 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-21337 | yes |
| SF-2026-ARXIV-2606-21338 | arXiv:2606.21338v1 | paper-v1:2606.21338 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21338 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21338 | yes |
| SF-2026-ARXIV-2606-21359 | arXiv:2606.21359v1 | paper-v1:2606.21359 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21359 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21359 | yes |
| SF-2026-ARXIV-2606-21372 | arXiv:2606.21372v1 | paper-v1:2606.21372 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21372 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21372 | yes |
| SF-2026-ARXIV-2606-21386 | arXiv:2606.21386v1 | paper-v1:2606.21386 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21386 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21386 | yes |
| SF-2026-ARXIV-2606-21389 | arXiv:2606.21389v1 | paper-v1:2606.21389 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21389 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-21389 | yes |
| SF-2026-ARXIV-2606-21398 | arXiv:2606.21398v1 | paper-v1:2606.21398 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21398 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21398 | yes |
| SF-2026-ARXIV-2606-21399 | arXiv:2606.21399v1 | paper-v1:2606.21399 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21399 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-21399 | yes |
| SF-2026-ARXIV-2606-21401 | arXiv:2606.21401v1 | paper-v1:2606.21401 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21401 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-21401 | yes |
| SF-2026-ARXIV-2606-21406 | arXiv:2606.21406v1 | paper-v1:2606.21406 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21406 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21406 | yes |
| SF-2026-ARXIV-2606-21409 | arXiv:2606.21409v1 | paper-v1:2606.21409 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21409 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-21409 | yes |
| SF-2026-ARXIV-2606-21428 | arXiv:2606.21428v1 | paper-v1:2606.21428 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21428 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21428 | yes |
| SF-2026-ARXIV-2606-21445 | arXiv:2606.21445v1 | paper-v1:2606.21445 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21445 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-21445 | yes |
| SF-2026-ARXIV-2606-21509 | arXiv:2606.21509v1 | paper-v1:2606.21509 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21509 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21509 | yes |
| SF-2026-ARXIV-2606-21514 | arXiv:2606.21514v1 | paper-v1:2606.21514 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21514 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2606-21514 | yes |
| SF-2026-ARXIV-2606-21553 | arXiv:2606.21553v1 | paper-v1:2606.21553 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21553 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21553 | yes |
| SF-2026-ARXIV-2606-21565 | arXiv:2606.21565v1 | paper-v1:2606.21565 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21565 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21565 | yes |
| SF-2026-ARXIV-2606-21572 | arXiv:2606.21572v1 | paper-v1:2606.21572 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21572 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-21572 | yes |
| SF-2026-ARXIV-2606-21584 | arXiv:2606.21584v1 | paper-v1:2606.21584 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21584 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-21584 | yes |
| SF-2026-ARXIV-2606-21627 | arXiv:2606.21627v1 | paper-v1:2606.21627 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21627 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21627 | yes |
| SF-2026-ARXIV-2606-21633 | arXiv:2606.21633v1 | paper-v1:2606.21633 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21633 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-21633 | yes |
| SF-2026-ARXIV-2606-21638 | arXiv:2606.21638v1 | paper-v1:2606.21638 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21638 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21638 | yes |
| SF-2026-ARXIV-2606-21654 | arXiv:2606.21654v1 | paper-v1:2606.21654 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21654 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21654 | yes |
| SF-2026-ARXIV-2606-21666 | arXiv:2606.21666v1 | paper-v1:2606.21666 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21666 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21666 | yes |
| SF-2026-ARXIV-2606-21678 | arXiv:2606.21678v1 | paper-v1:2606.21678 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21678 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-21678 | yes |
| SF-2026-ARXIV-2606-21710 | arXiv:2606.21710v1 | paper-v1:2606.21710 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21710 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21710 | yes |
| SF-2026-ARXIV-2606-21712 | arXiv:2606.21712v1 | paper-v1:2606.21712 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21712 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-21712 | yes |
| SF-2026-ARXIV-2606-21732 | arXiv:2606.21732v1 | paper-v1:2606.21732 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21732 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21732 | yes |
| SF-2026-ARXIV-2606-21775 | arXiv:2606.21775v1 | paper-v1:2606.21775 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21775 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-21775 | yes |
| SF-2026-ARXIV-2606-21777 | arXiv:2606.21777v1 | paper-v1:2606.21777 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21777 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-21777 | yes |
| SF-2026-ARXIV-2606-21787 | arXiv:2606.21787v1 | paper-v1:2606.21787 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21787 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Integrate | books-review:SF-2026-ARXIV-2606-21787 | yes |
| SF-2026-ARXIV-2606-21795 | arXiv:2606.21795v1 | paper-v1:2606.21795 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21795 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-21795 | yes |
| SF-2026-ARXIV-2606-21803 | arXiv:2606.21803v1 | paper-v1:2606.21803 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21803 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-21803 | yes |
| SF-2026-ARXIV-2606-21804 | arXiv:2606.21804v1 | paper-v1:2606.21804 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21804 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21804 | yes |
| SF-2026-ARXIV-2606-21807 | arXiv:2606.21807v1 | paper-v1:2606.21807 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21807 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21807 | yes |
| SF-2026-ARXIV-2606-21811 | arXiv:2606.21811v1 | paper-v1:2606.21811 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21811 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21811 | yes |
| SF-2026-ARXIV-2606-28376 | arXiv:2606.28376v1 | paper-v1:2606.28376 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28376 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28376 | yes |
| SF-2026-ARXIV-2606-28379 | arXiv:2606.28379v1 | paper-v1:2606.28379 | 2026-W25 | 2026-06-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28379 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-28379 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21023 | RP-4ac33e22f655043f | deep | arXiv:2606.21023v1 | SRC-ARXIV@arXiv:2606.21023v1 | arXiv:2606.21023v1 §2.3 The Microscopic Origin: Boundary Truncation; §3 HEAL; Appendix C HEAL Implementation | arXiv:2606.21023v1 §4 Evaluation; Appendix A Detailed Experimental Setup; Appendix D Additional Performance Results; Appendix E MCR-Bench | arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21023 | complete |
| SF-2026-ARXIV-2606-21024 | RP-f78ff9d08d57da56 | deep | arXiv:2606.21024v1 | SRC-ARXIV@arXiv:2606.21024v1 | arXiv:2606.21024v1 §2 Method: Negative Knowledge Memory Layer; Appendix A Negative-Knowledge Record Schema | arXiv:2606.21024v1 §3 Evaluation: Negative-Knowledge Retry; §4 Case Study; Appendices B–C | arXiv:2606.21024v1 §5 Conclusion; §4.5 Cross-system Transfer | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21024 | complete |
| SF-2026-ARXIV-2606-21037 | RP-3908f7de4588cd0b | deep | arXiv:2606.21037v1 | SRC-ARXIV@arXiv:2606.21037v1 | arXiv:2606.21037v1 §3 Methods (§3.1 Honeyquest; §3.2 LLM Attackers) | arXiv:2606.21037v1 §3.3 Metrics; §4 Results | arXiv:2606.21037v1 §5 Discussion; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21037 | complete |
| SF-2026-ARXIV-2606-21045 | RP-1eafe075a2d28741 | deep | arXiv:2606.21045v1 | SRC-ARXIV@arXiv:2606.21045v1 | arXiv:2606.21045v1 §IV Threat Model; §V OVIG Design | arXiv:2606.21045v1 §VI Evaluation; Appendices A–C | arXiv:2606.21045v1 §VII Limitations and Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21045 | complete |
| SF-2026-ARXIV-2606-21071 | RP-edadbc2862c3acbc | deep | arXiv:2606.21071v1 | SRC-ARXIV@arXiv:2606.21071v1 | arXiv:2606.21071v1 §3 Runtime Vulnerability Taxonomy; §4 ClawAudit Design | arXiv:2606.21071v1 §5 OpenClawBench; §6 Evaluation | arXiv:2606.21071v1 §3.4 Taxonomy Scope; §7.3–§7.4 syntactic/semantic boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21071 | complete |
| SF-2026-ARXIV-2606-21077 | RP-f6240a26aaf624e7 | deep | arXiv:2606.21077v1 | SRC-ARXIV@arXiv:2606.21077v1 | arXiv:2606.21077v1 §3 OTTER; Appendix A Algorithm; Appendix C System Architecture | arXiv:2606.21077v1 §4 Experiments; §5 Results | arXiv:2606.21077v1 §6 Defense Implications; Scope of Contribution; Responsible Use | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21077 | complete |
| SF-2026-ARXIV-2606-21083 | RP-87910034969a36cd | deep | arXiv:2606.21083v1 | SRC-ARXIV@arXiv:2606.21083v1 | arXiv:2606.21083v1 §3 Methodology; §4 Probability Elicitation Protocol; Appendix A | arXiv:2606.21083v1 §5 Setup; §6 Results; §7 Ablations | arXiv:2606.21083v1 §8 Conclusion; Appendix B Theoretical Foundations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21083 | complete |
| SF-2026-ARXIV-2606-21088 | RP-8c43ce85c94fd794 | deep | arXiv:2606.21088v1 | SRC-ARXIV@arXiv:2606.21088v1 | arXiv:2606.21088v1 §2 Analysis; §3 Method (§3.2 progress-valued regulation and rollback) | arXiv:2606.21088v1 §4 Experiments; Appendix C Real-world Setup; Appendix G Failure Analysis | arXiv:2606.21088v1 §5 Limitations; Appendix F Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21088 | complete |
| SF-2026-ARXIV-2606-21101 | RP-c641e43b1ab31686 | deep | arXiv:2606.21101v1 | SRC-ARXIV@arXiv:2606.21101v1 | arXiv:2606.21101v1 §IV DPIFrame Design (§IV-E Stream Scheduling) | arXiv:2606.21101v1 §V Evaluation (§V-A Setup; §V-G Scheduling) | arXiv:2606.21101v1 §VI Conclusion and evaluated workload boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21101 | complete |
| SF-2026-ARXIV-2606-21121 | RP-48098e1eaa6690d6 | deep | arXiv:2606.21121v1 | SRC-ARXIV@arXiv:2606.21121v1 | arXiv:2606.21121v1 §4 Decoding-time Control; §5 Runtime Framework | arXiv:2606.21121v1 §6 Experiments (§6.5 Telemetry; §6.8 Repair Failures) | arXiv:2606.21121v1 §7 Limitations; §9 Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21121 | complete |
| SF-2026-ARXIV-2606-21126 | RP-d8183249fac14209 | deep | arXiv:2606.21126v1 | SRC-ARXIV@arXiv:2606.21126v1 | arXiv:2606.21126v1 §4 Failure Modes; §6 Recommended Evaluation Protocol | arXiv:2606.21126v1 §5 Validation; Appendices A–J | arXiv:2606.21126v1 §6.4 Scope and Recommendations; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21126 | complete |
| SF-2026-ARXIV-2606-21129 | RP-94ba1fdaf147e4c3 | deep | arXiv:2606.21129v1 | SRC-ARXIV@arXiv:2606.21129v1 | arXiv:2606.21129v1 §2 Threat Model; §3 Design; §4 Intent ABI | arXiv:2606.21129v1 §5 Security Analysis; §6 Capability Migration | arXiv:2606.21129v1 §7 Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21129 | complete |
| SF-2026-ARXIV-2606-21130 | RP-fc1decf9f9c48956 | deep | arXiv:2606.21130v1 | SRC-ARXIV@arXiv:2606.21130v1 | arXiv:2606.21130v1 §III Methodology (§III-B Surge Injection; §III-C XGBoost) | arXiv:2606.21130v1 §IV Experimental Evaluation (§IV-E Threshold Selection) | arXiv:2606.21130v1 §V Discussion; §VI Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21130 | complete |
| SF-2026-ARXIV-2606-21140 | RP-ba73225ea2a36405 | deep | arXiv:2606.21140v1 | SRC-ARXIV@arXiv:2606.21140v1 | arXiv:2606.21140v1 §3 Benchmark Design; §4 Token-Economic Metrics | arXiv:2606.21140v1 §5 Experimental Analysis | arXiv:2606.21140v1 §6 Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21140 | complete |
| SF-2026-ARXIV-2606-21144 | RP-9be584a541aa116f | deep | arXiv:2606.21144v1 | SRC-ARXIV@arXiv:2606.21144v1 | arXiv:2606.21144v1 §3 AdaMem | arXiv:2606.21144v1 §4 Benchmark and Setup; §5 Results | arXiv:2606.21144v1 §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21144 | complete |
| SF-2026-ARXIV-2606-21172 | RP-6834f67aa736c8a0 | deep | arXiv:2606.21172v1 | SRC-ARXIV@arXiv:2606.21172v1 | arXiv:2606.21172v1 §3.2 Threat Model; §4 Method | arXiv:2606.21172v1 §5 Experiments; Appendix A Poison-rate Audit | arXiv:2606.21172v1 §6 Limitation | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21172 | complete |
| SF-2026-ARXIV-2606-21173 | RP-bcc8bc24a52abce5 | deep | arXiv:2606.21173v1 | SRC-ARXIV@arXiv:2606.21173v1;SRC-GITHUB-COMMIT@commit:main-observed-2026-08-29 | https://inverting-bellman.github.io/#overview — exact-title project linked to arXiv:2606.21173v1; §Overview, §P-learning and Bellman-inversion formulation | https://github.com/aletcher/inverting-bellman#reproduce-paper-figures — linked author repository §Reproduce Paper Figures, §Expected Results and Reacher experiment | Not Disclosed — official exact-v1 body unavailable; exact-v1 abstract and linked author artifacts expose sufficient-identifiability and named-environment scope but no dedicated limitation section | https://inverting-bellman.github.io/; https://github.com/aletcher/inverting-bellman — project title/arXiv link and repository reproduce-paper instructions bind the artifact to arXiv:2606.21173v1; no later revision claim used | claim:SF-2026-ARXIV-2606-21173 | complete |
| SF-2026-ARXIV-2606-21188 | RP-a208eb26dad9385c | deep | arXiv:2606.21188v1 | SRC-ARXIV@arXiv:2606.21188v1 | arXiv:2606.21188v1 §3 Method (memory pretraining, discretization and action head) | arXiv:2606.21188v1 §4 Simulation and Real Robot; Appendices A–B | arXiv:2606.21188v1 §5 Limitations and Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21188 | complete |
| SF-2026-ARXIV-2606-21228 | RP-916be11c943baada | deep | arXiv:2606.21228v1 | SRC-ARXIV@arXiv:2606.21228v1 | arXiv:2606.21228v1 §3 Sakana Fugu (§3.1 Fugu; §3.2 Fugu-Ultra) | arXiv:2606.21228v1 §4 Capabilities; Appendix A Evaluation Configuration; Appendix B | arXiv:2606.21228v1 §5 Conclusions and evaluated agent/task scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21228 | complete |
| SF-2026-ARXIV-2606-21238 | RP-088551d19c6cac82 | deep | arXiv:2606.21238v1 | SRC-ARXIV@arXiv:2606.21238v1 | arXiv:2606.21238v1 §3 Method | arXiv:2606.21238v1 §4 Evaluation (DQA, conversation, batch and adaptive partitioning) | arXiv:2606.21238v1 §5 Conclusion; §6 Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21238 | complete |
| SF-2026-ARXIV-2606-21249 | RP-af5c48228555747a | deep | arXiv:2606.21249v1 | SRC-ARXIV@arXiv:2606.21249v1 | arXiv:2606.21249v1 §3 Methods | arXiv:2606.21249v1 §4 Static Analysis; §5 Training Dynamics; §6 Causal Validation; §7 Quantitative Ablation | arXiv:2606.21249v1 §6 Scope and Caveats; §9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21249 | complete |
| SF-2026-ARXIV-2606-21255 | RP-7bf9456ab611208a | deep | arXiv:2606.21255v1 | SRC-ARXIV@arXiv:2606.21255v1 | arXiv:2606.21255v1 §3 Method (§3.2 Calibrated Gate; §3.3 Certifying Boundary) | arXiv:2606.21255v1 §4 Experiments; Appendices A–C and E–F | arXiv:2606.21255v1 §5 Conclusion; Appendix D Boundary Construction | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21255 | complete |
| SF-2026-ARXIV-2606-21257 | RP-84c12565b0f0a447 | deep | arXiv:2606.21257v1 | SRC-ARXIV@arXiv:2606.21257v1 | arXiv:2606.21257v1 §2 Empirical Study (§2.1 Settings) | arXiv:2606.21257v1 §2.2 PTQ; §2.3 Ablation; §2.4 Task Evaluation | arXiv:2606.21257v1 §4 Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21257 | complete |
| SF-2026-ARXIV-2606-21262 | RP-752ddcf95a6802ad | deep | arXiv:2606.21262v1 | SRC-ARXIV@arXiv:2606.21262v1 | arXiv:2606.21262v1 §3 ARCO (hierarchical rubric and co-evolution); Appendix A | arXiv:2606.21262v1 §4 Experiments; Appendices B–D | arXiv:2606.21262v1 §6 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21262 | complete |
| SF-2026-ARXIV-2606-21282 | RP-35da327a0a881500 | deep | arXiv:2606.21282v1 | SRC-ARXIV@arXiv:2606.21282v1;SRC-CROSSREF@DOI:10.48550/arXiv.2606.21282 | doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §4.3 Verification Algorithm and Differential Halo Zonotope Abstract Domain | doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §5.2 Asymmetric Confidence-Based Global Robustness and Law/LHC/HAR benchmarks | doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §6 Conclusion states counterexample search and compositional scaling remain future work | Not Disclosed — official exact-v1 body unavailable; exact-title author manuscript mirror matched official arXiv title, authors and DOI but does not expand version or publication status | claim:SF-2026-ARXIV-2606-21282 | complete |
| SF-2026-ARXIV-2606-21307 | RP-b9cf3aafb4d19ac8 | deep | arXiv:2606.21307v1 | SRC-ARXIV@arXiv:2606.21307v1 | arXiv:2606.21307v1 §3 Method (skill expansion, detection and routing) | arXiv:2606.21307v1 §4 Benchmark; §5 Setup; §6 Analysis | arXiv:2606.21307v1 §7 Conclusion and benchmark/skill-library scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21307 | complete |
| SF-2026-ARXIV-2606-21315 | RP-dca1feaf5afd7e95 | deep | arXiv:2606.21315v1 | SRC-ARXIV@arXiv:2606.21315v1 | arXiv:2606.21315v1 §3 Social World Model (five-dimensional decomposition; wake-sleep-deploy gates) | arXiv:2606.21315v1 §4 Benchmark; §5 Experiments | arXiv:2606.21315v1 §6 Discussion (specificity and ablations) | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21315 | complete |
| SF-2026-ARXIV-2606-21337 | RP-483a56097988eec9 | deep | arXiv:2606.21337v1 | SRC-ARXIV@arXiv:2606.21337v1 | arXiv:2606.21337v1 §3 Method (pipeline, GRPO and deployment) | arXiv:2606.21337v1 §4 Experiments; Appendix A Benchmark; Appendix B Training and Deployment | arXiv:2606.21337v1 §5 Conclusion and dataset/model scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21337 | complete |
| SF-2026-ARXIV-2606-21338 | RP-4dd85b74ad6cd230 | deep | arXiv:2606.21338v1 | SRC-ARXIV@arXiv:2606.21338v1 | arXiv:2606.21338v1 §3 MCPPrivacyDetector and Taint Analysis | arXiv:2606.21338v1 §4 Evaluation | arXiv:2606.21338v1 §6 Conclusion and evaluated MCP/tool boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21338 | complete |
| SF-2026-ARXIV-2606-21359 | RP-1ddee3e23a3ba014 | deep | arXiv:2606.21359v1 | SRC-ARXIV@arXiv:2606.21359v1 | arXiv:2606.21359v1 §2 Benchmark; §3 Hallucination Taxonomy | arXiv:2606.21359v1 §4 Setup; §5 Results; §6 Human Validation; Appendices C and E–H | arXiv:2606.21359v1 §7 Limitations exact headings: Evidence Source Limitations; Training-data Contamination; Confounding Fine-tuning Factors; Human-study Scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21359 | complete |
| SF-2026-ARXIV-2606-21372 | RP-8bee13fe604d3e16 | deep | arXiv:2606.21372v1 | SRC-ARXIV@arXiv:2606.21372v1 | arXiv:2606.21372v1 §3 Method (NAC tokenizer and behavioral cloning); Appendix A | arXiv:2606.21372v1 §4 Experiments; Appendix B | arXiv:2606.21372v1 §5 Discussion and codec/policy scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21372 | complete |
| SF-2026-ARXIV-2606-21386 | RP-c83fd04ac8478e09 | deep | arXiv:2606.21386v1 | SRC-ARXIV@arXiv:2606.21386v1 | arXiv:2606.21386v1 §3 Method (LLMD, ACC and VLA-FAIL) | arXiv:2606.21386v1 §4 Experiments; §5 Results; Appendices A–F | arXiv:2606.21386v1 §6 Limitations; Appendix D.2 Failure Cases | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21386 | complete |
| SF-2026-ARXIV-2606-21389 | RP-a5f19d406387eaf7 | deep | arXiv:2606.21389v1 | SRC-ARXIV@arXiv:2606.21389v1 | arXiv:2606.21389v1 §3 Methodology and Datasets | arXiv:2606.21389v1 §4 Validation | arXiv:2606.21389v1 §5 Discussion; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21389 | complete |
| SF-2026-ARXIV-2606-21398 | RP-db14960311b8c65a | deep | arXiv:2606.21398v1 | SRC-ARXIV@arXiv:2606.21398v1 | arXiv:2606.21398v1 §III Methodology (BITE, InfoNCE and Qwen integration) | arXiv:2606.21398v1 §IV Results | arXiv:2606.21398v1 §IV-D Discussion and Limitations; §V Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21398 | complete |
| SF-2026-ARXIV-2606-21399 | RP-9132a67ffd925bec | deep | arXiv:2606.21399v1 | SRC-ARXIV@arXiv:2606.21399v1 | arXiv:2606.21399v1 §2 Scalar-control Sufficiency; §3 Prefix Branching; §4 Action-conditioned Controller | arXiv:2606.21399v1 §5 Results; Appendices B–C | arXiv:2606.21399v1 §7 Conclusion and action/benchmark boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21399 | complete |
| SF-2026-ARXIV-2606-21401 | RP-dcf1ec8c0491eb96 | deep | arXiv:2606.21401v1 | SRC-ARXIV@arXiv:2606.21401v1 | arXiv:2606.21401v1 §3 SwarmX Design; §4 Implementation | arXiv:2606.21401v1 §5 Evaluation (production and overhead) | arXiv:2606.21401v1 §6 Production and Operation Experience; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21401 | complete |
| SF-2026-ARXIV-2606-21406 | RP-a2d3f0259c19b4f6 | deep | arXiv:2606.21406v1 | SRC-ARXIV@arXiv:2606.21406v1 | arXiv:2606.21406v1 §4 Method (iterative self-improvement, DGAC and policy update) | arXiv:2606.21406v1 §5 Experiments; Appendix A.2 | arXiv:2606.21406v1 §6 Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21406 | complete |
| SF-2026-ARXIV-2606-21409 | RP-f09bb1effcee41f7 | deep | arXiv:2606.21409v1 | SRC-ARXIV@arXiv:2606.21409v1 | arXiv:2606.21409v1 §2 Controlled Matched-loop Design | arXiv:2606.21409v1 §3 Inversion; §4 Scope; §5 Failure Structure; Appendices B–C | arXiv:2606.21409v1 §6 Fallback-limited Repairs; §9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21409 | complete |
| SF-2026-ARXIV-2606-21428 | RP-41c85415a5f5af85 | deep | arXiv:2606.21428v1 | SRC-ARXIV@arXiv:2606.21428v1 | arXiv:2606.21428v1 §3 Methodology (hardware, backend, models, prompts and metrics) | arXiv:2606.21428v1 §4 Results | arXiv:2606.21428v1 §5 Discussion and Bottleneck; §6 Threats to Validity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21428 | complete |
| SF-2026-ARXIV-2606-21445 | RP-600cac4c0fd27e71 | deep | arXiv:2606.21445v1 | SRC-ARXIV@arXiv:2606.21445v1 | arXiv:2606.21445v1 §3 Preliminaries; §4 Methodology (primitive sequence, robustness and flow exploration) | arXiv:2606.21445v1 §5 Experiments; Appendices A–F | arXiv:2606.21445v1 §6 Discussion (reliability and generalization) | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21445 | complete |
| SF-2026-ARXIV-2606-21509 | RP-c1e4bbffdd8c4ab2 | deep | arXiv:2606.21509v1 | SRC-ARXIV@arXiv:2606.21509v1 | arXiv:2606.21509v1 §III Methodology and Model Stitching | arXiv:2606.21509v1 §IV Experiments (hardware, performance and efficiency) | arXiv:2606.21509v1 §V Conclusion; Appendix A Sensor Setup | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21509 | complete |
| SF-2026-ARXIV-2606-21514 | RP-ab1d9512db867216 | deep | arXiv:2606.21514v1 | SRC-ARXIV@arXiv:2606.21514v1 | arXiv:2606.21514v1 §3 Mixed-spiked Matrix Sensing; §4 River-valley Generalization | arXiv:2606.21514v1 §5 Empirical Study; Appendices B–C | arXiv:2606.21514v1 Appendix B.3 Late-stage Failure; Appendix B.4 Implications; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21514 | complete |
| SF-2026-ARXIV-2606-21553 | RP-33599bffa667e502 | deep | arXiv:2606.21553v1 | SRC-ARXIV@arXiv:2606.21553v1 | arXiv:2606.21553v1 §3 System Architecture | arXiv:2606.21553v1 §4 Setup; §5 Results; §6 Analysis | arXiv:2606.21553v1 §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21553 | complete |
| SF-2026-ARXIV-2606-21565 | RP-62bdf7edb8a4e1e5 | deep | arXiv:2606.21565v1 | SRC-ARXIV@arXiv:2606.21565v1 | arXiv:2606.21565v1 §3 Methods (ABM representation and rules) | arXiv:2606.21565v1 §4 Results (prototype and evaluation) | arXiv:2606.21565v1 §5 Discussion; explicit no prompt/tool/safety/reversibility/auth scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21565 | complete |
| SF-2026-ARXIV-2606-21572 | RP-9f9722a715ebc3f6 | deep | arXiv:2606.21572v1 | SRC-ARXIV@arXiv:2606.21572v1 | arXiv:2606.21572v1 §3 Method (training critics and policy integration) | arXiv:2606.21572v1 §4 Critic Evaluation; §5 In-loop Evaluation; Appendices A–C | arXiv:2606.21572v1 §5.3 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21572 | complete |
| SF-2026-ARXIV-2606-21584 | RP-69b2ae52e57f45a8 | deep | arXiv:2606.21584v1 | SRC-ARXIV@arXiv:2606.21584v1 | arXiv:2606.21584v1 §2 Threshold Transfer; §3 Audited Corrections | arXiv:2606.21584v1 §4 Experiments (cross-dataset transfer and fragility) | arXiv:2606.21584v1 §4.5 Limitations; §5 Recommendations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21584 | complete |
| SF-2026-ARXIV-2606-21627 | RP-06421cd4fd8169c6 | deep | arXiv:2606.21627v1 | SRC-ARXIV@arXiv:2606.21627v1 | arXiv:2606.21627v1 §3 Methods (environments, trajectories, judgments and human annotation) | arXiv:2606.21627v1 §4 Dataset Analysis; Appendix D Evaluation in the Loop | arXiv:2606.21627v1 §5.1 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21627 | complete |
| SF-2026-ARXIV-2606-21633 | RP-07fb01e680e6e168 | deep | arXiv:2606.21633v1 | SRC-ARXIV@arXiv:2606.21633v1 | arXiv:2606.21633v1 §3 Motivation; §4 HERALD (CPU-GPU retrieval and kernel); §5 Implementation | arXiv:2606.21633v1 §6 Evaluation | arXiv:2606.21633v1 §8 Conclusion and evaluated platform boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21633 | complete |
| SF-2026-ARXIV-2606-21638 | RP-b076ca1cfcc16153 | deep | arXiv:2606.21638v1 | SRC-ARXIV@arXiv:2606.21638v1 | arXiv:2606.21638v1 §3 Tiered Language Models and Training Protocol | arXiv:2606.21638v1 §4 Capability Separation; §5 Cost; §6 Robustness; §7 Scaling | arXiv:2606.21638v1 §9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21638 | complete |
| SF-2026-ARXIV-2606-21654 | RP-be09dd8d4f41017a | deep | arXiv:2606.21654v1 | SRC-ARXIV@arXiv:2606.21654v1 | arXiv:2606.21654v1 §3 Framework (agent context, composition engine and evaluation) | arXiv:2606.21654v1 §4 Results and Failures; Appendix A | arXiv:2606.21654v1 §6 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21654 | complete |
| SF-2026-ARXIV-2606-21666 | RP-f388782f574f3ae6 | deep | arXiv:2606.21666v1 | SRC-ARXIV@arXiv:2606.21666v1 | arXiv:2606.21666v1 §3 Framework (agent context, divergence and shared verification) | arXiv:2606.21666v1 §4 Setup; §5 Results | arXiv:2606.21666v1 §6.2 Limitations; §6.3 Contamination | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21666 | complete |
| SF-2026-ARXIV-2606-21678 | RP-d2645fb0af6a89fe | deep | arXiv:2606.21678v1 | SRC-ARXIV@arXiv:2606.21678v1 | arXiv:2606.21678v1 §4 Method (format, objective, information constraints and diagnostic ladder) | arXiv:2606.21678v1 §5 Experiments; Appendices A–C | arXiv:2606.21678v1 §6 Discussion: structural decodability-faithfulness gap | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21678 | complete |
| SF-2026-ARXIV-2606-21710 | RP-5bbf9cf82b01b6c9 | deep | arXiv:2606.21710v1 | SRC-ARXIV@arXiv:2606.21710v1 | arXiv:2606.21710v1 §3 Scenarios and Annotations; §4 Reward Modeling and Policy Optimization | arXiv:2606.21710v1 §5 Experiments | arXiv:2606.21710v1 §6 Limitations (unnumbered list after Conclusion): synthetic scenarios, judge dependence, human heterogeneity, scale, deployment caution, norms and dual use | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21710 | complete |
| SF-2026-ARXIV-2606-21712 | RP-d8006d58e26f7fff | deep | arXiv:2606.21712v1 | SRC-ARXIV@arXiv:2606.21712v1 | arXiv:2606.21712v1 §3 Design Intuitions; §4 Sequence Coroutine; §5 System Design | arXiv:2606.21712v1 §6 Evaluation | arXiv:2606.21712v1 §7 Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21712 | complete |
| SF-2026-ARXIV-2606-21732 | RP-843cb1c624fd6151 | deep | arXiv:2606.21732v1 | SRC-ARXIV@arXiv:2606.21732v1 | arXiv:2606.21732v1 §2 System Model; §3 Hypotheses; §4 Attack; §5 Threat; §6 Method; §8 Defense | arXiv:2606.21732v1 §7 Evaluation; Appendices A–C | arXiv:2606.21732v1 §10 Conclusion; adaptive-adversary boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21732 | complete |
| SF-2026-ARXIV-2606-21775 | RP-eba88d31930fc1b9 | deep | arXiv:2606.21775v1 | SRC-ARXIV@arXiv:2606.21775v1 | arXiv:2606.21775v1 §3 VLWM (variable horizon, curriculum and planning) | arXiv:2606.21775v1 §4 Planning Tasks; Appendices A–C | arXiv:2606.21775v1 §5 Conclusion and evaluated task/horizon boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21775 | complete |
| SF-2026-ARXIV-2606-21777 | RP-07e57108cc076a26 | deep | arXiv:2606.21777v1 | SRC-ARXIV@arXiv:2606.21777v1 | arXiv:2606.21777v1 §3 Calibrated Verifier Telemetry | arXiv:2606.21777v1 §4 Experiments; Appendices A–G | arXiv:2606.21777v1 §5 Conclusion and model-scale/QA scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21777 | complete |
| SF-2026-ARXIV-2606-21787 | RP-cb751fa872b8af4d | deep | arXiv:2606.21787v1 | SRC-ARXIV@arXiv:2606.21787v1 | arXiv:2606.21787v1 §3 Empirical Design; §5 SemFin | arXiv:2606.21787v1 §4, §6 and §7 Research Questions | arXiv:2606.21787v1 §8 Discussion and Implication | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21787 | complete |
| SF-2026-ARXIV-2606-21795 | RP-31d90620ff934fec | deep | arXiv:2606.21795v1 | SRC-ARXIV@arXiv:2606.21795v1 | arXiv:2606.21795v1 §2 Formulation; §3 Reward Clustering | arXiv:2606.21795v1 §4 Experiments; Appendices C–D | arXiv:2606.21795v1 §5 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21795 | complete |
| SF-2026-ARXIV-2606-21803 | RP-eb88c695e4eb312e | deep | arXiv:2606.21803v1 | SRC-ARXIV@arXiv:2606.21803v1 | arXiv:2606.21803v1 §3 Method (TTT-NTP fast write, chunk and closed form) | arXiv:2606.21803v1 §4 Experiments; Appendices A–C | arXiv:2606.21803v1 §5 Conclusion and evaluated model/context boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21803 | complete |
| SF-2026-ARXIV-2606-21804 | RP-0719ff0467261f3b | deep | arXiv:2606.21804v1 | SRC-ARXIV@arXiv:2606.21804v1 | arXiv:2606.21804v1 §3 CodeThread | arXiv:2606.21804v1 §4 SWE Evaluation; §5 Analysis; Appendices A–D | arXiv:2606.21804v1 §6 Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21804 | complete |
| SF-2026-ARXIV-2606-21807 | RP-69a5a8806386032a | deep | arXiv:2606.21807v1 | SRC-ARXIV@arXiv:2606.21807v1 | arXiv:2606.21807v1 §3 Two Opposing Forces | arXiv:2606.21807v1 §4 Setup; §5 Results; Appendices A–I | arXiv:2606.21807v1 §6 Analysis and Discussion; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21807 | complete |
| SF-2026-ARXIV-2606-21811 | RP-7bfab41b287daf9f | deep | arXiv:2606.21811v1 | SRC-ARXIV@arXiv:2606.21811v1 | arXiv:2606.21811v1 §3 Methodology (critic models, critique and training) | arXiv:2606.21811v1 §4 Setup; §5 Results; Appendices D–G | arXiv:2606.21811v1 §6 Discussion; Appendices E and G.4 fall-short cases | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21811 | complete |
| SF-2026-ARXIV-2606-28376 | RP-3c77b9673d722d19 | deep | arXiv:2606.28376v1 | SRC-ARXIV@arXiv:2606.28376v1 | arXiv:2606.28376v1 §3 OSU-Mem; §4 Theory | arXiv:2606.28376v1 §5 Settings; §6 Results; Appendices B–J | arXiv:2606.28376v1 §7 Limitations; Appendix F no multi-step rollout note | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-28376 | complete |
| SF-2026-ARXIV-2606-28379 | RP-7076d8a776f7b2c5 | deep | arXiv:2606.28379v1 | SRC-ARXIV@arXiv:2606.28379v1 | arXiv:2606.28379v1 §3 LEDGER (graph, retrieval and consistency) | arXiv:2606.28379v1 §4 Experiments; Appendices C–E | arXiv:2606.28379v1 §5 Conclusion and absence of a formal semantic guarantee | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-28379 | complete |

**Source Reviews**

<!-- review:SF-2026-ARXIV-2606-21023:start -->
### 2606.21023 — Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL

**问题与旧路径。** As Large Language Models (LLMs) deploy into mission-critical domains (e.g., finance, medicine, and law), output reproducibility has become a strict system requirement. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 异构 GPU 上 greedy decode 仍会因 kernel-boundary downcast 累积而翻转；HEAL 用 INT16 Q/K/V 与双 16-bit GEMM 误差补偿换取接近 FP32 的功能复现性。唯一知识 owner 为 `INFER-GPU-MEMORY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21023v1 §2.3 The Microscopic Origin: Boundary Truncation; §3 HEAL; Appendix C HEAL Implementation`；Evaluation=`arXiv:2606.21023v1 §4 Evaluation; Appendix A Detailed Experimental Setup; Appendix D Additional Performance Results; Appendix E MCR-Bench`；counterevidence=`arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies`，只支持『异构 GPU 上 greedy decode 仍会因 kernel-boundary downcast 累积而翻转；HEAL 用 INT16 Q/K/V 与双 16-bit GEMM 误差补偿换取接近 FP32 的功能复现性』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21023:start -->
Primary identity `arXiv:2606.21023v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21023:end -->
<!-- review:SF-2026-ARXIV-2606-21023:end -->

<!-- review:SF-2026-ARXIV-2606-21024:start -->
### 2606.21024 — Negative Knowledge as Failure-aware Shared Memory for AutoResearch

**问题与旧路径。** AI-assisted research systems generate many failed attempts, but those failures rarely become a durable, shared knowledge asset. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 失败经验应以带 task、attempt、failure mode、diagnosis 与 prevention 的 negative-knowledge record 写入共享 memory，并在后续尝试前检索而非覆盖成功轨迹。唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21024v1 §2 Method: Negative Knowledge Memory Layer; Appendix A Negative-Knowledge Record Schema`；Evaluation=`arXiv:2606.21024v1 §3 Evaluation: Negative-Knowledge Retry; §4 Case Study; Appendices B–C`；counterevidence=`arXiv:2606.21024v1 §5 Conclusion; §4.5 Cross-system Transfer`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21024v1 §5 Conclusion; §4.5 Cross-system Transfer`，只支持『失败经验应以带 task、attempt、failure mode、diagnosis 与 prevention 的 negative-knowledge record 写入共享 memory，并在后续尝试前检索而非覆盖成功轨迹』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。写入、检索或来源证据不足时 hold/隔离 candidate memory，保留原始轨迹并禁止自动覆盖；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21024:start -->
Primary identity `arXiv:2606.21024v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21024:end -->
<!-- review:SF-2026-ARXIV-2606-21024:end -->

<!-- review:SF-2026-ARXIV-2606-21037:start -->
### 2606.21037 — Honeyquest for LLMs: Rethinking Cyber Deception for AI Attackers

**问题与旧路径。** The empirical foundation of cyber deception relies on human-centered hypotheses, but the rapid emergence of autonomous, AI-enabled attackers challenges whether this foundation transfers to AI agents. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** LLM attacker 与人类 attacker 的 deception response 不同，security evaluation 必须把 attacker class、trap recognition 与实际 exploit action 分开记录。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21037v1 §3 Methods (§3.1 Honeyquest; §3.2 LLM Attackers)`；Evaluation=`arXiv:2606.21037v1 §3.3 Metrics; §4 Results`；counterevidence=`arXiv:2606.21037v1 §5 Discussion; §6 Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21037v1 §5 Discussion; §6 Conclusion`，只支持『LLM attacker 与人类 attacker 的 deception response 不同，security evaluation 必须把 attacker class、trap recognition 与实际 exploit action 分开记录』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21037:start -->
Primary identity `arXiv:2606.21037v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21037:end -->
<!-- review:SF-2026-ARXIV-2606-21037:end -->

<!-- review:SF-2026-ARXIV-2606-21045:start -->
### 2606.21045 — OVIG: Optimistic Verification of AI Training Integrity via Gradient Signals

**问题与旧路径。** The rapid growth of AI has increased the demand for domain-specific post-training, while the cost and specialization of accelerator infrastructure push many model owners to outsource this process. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 训练完整性可以由连续 gradient-signal challenge 做 optimistic verification，但 verifier 必须拥有 challenge identity、容忍区间与失败升级路径。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21045v1 §IV Threat Model; §V OVIG Design`；Evaluation=`arXiv:2606.21045v1 §VI Evaluation; Appendices A–C`；counterevidence=`arXiv:2606.21045v1 §VII Limitations and Discussion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21045v1 §VII Limitations and Discussion`，只支持『训练完整性可以由连续 gradient-signal challenge 做 optimistic verification，但 verifier 必须拥有 challenge identity、容忍区间与失败升级路径』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21045:start -->
Primary identity `arXiv:2606.21045v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21045:end -->
<!-- review:SF-2026-ARXIV-2606-21045:end -->

<!-- review:SF-2026-ARXIV-2606-21071:start -->
### 2606.21071 — Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer

**问题与旧路径。** Local LLM agents such as OpenClaw and Nanobot run on end-user machines and act on host resources - the shell, filesystem, browser, stored credentials, and messaging applications - through natural-language goals. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** Agent vulnerability audit 必须覆盖 activation 后的 runtime data/control flow，静态 skill 文本与 manifest 不能代表组合执行安全。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21071v1 §3 Runtime Vulnerability Taxonomy; §4 ClawAudit Design`；Evaluation=`arXiv:2606.21071v1 §5 OpenClawBench; §6 Evaluation`；counterevidence=`arXiv:2606.21071v1 §3.4 Taxonomy Scope; §7.3–§7.4 syntactic/semantic boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21071v1 §3.4 Taxonomy Scope; §7.3–§7.4 syntactic/semantic boundary`，只支持『Agent vulnerability audit 必须覆盖 activation 后的 runtime data/control flow，静态 skill 文本与 manifest 不能代表组合执行安全』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21071:start -->
Primary identity `arXiv:2606.21071v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21071:end -->
<!-- review:SF-2026-ARXIV-2606-21071:end -->

<!-- review:SF-2026-ARXIV-2606-21077:start -->
### 2606.21077 — OTTER: A Red-Teaming System for Toxicity-Evading Jailbreak Prompt Optimization

**问题与旧路径。** Production LLMs increasingly rely on toxicity-based moderation filters as a primary defense, assuming that harmful intent correlates with toxic surface wording. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 黑盒 Agent red-team 可用可迁移 observation/action perturbation 搜索 failure trajectory，但 attack generator 不能取得生产执行权。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21077v1 §3 OTTER; Appendix A Algorithm; Appendix C System Architecture`；Evaluation=`arXiv:2606.21077v1 §4 Experiments; §5 Results`；counterevidence=`arXiv:2606.21077v1 §6 Defense Implications; Scope of Contribution; Responsible Use`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21077v1 §6 Defense Implications; Scope of Contribution; Responsible Use`，只支持『黑盒 Agent red-team 可用可迁移 observation/action perturbation 搜索 failure trajectory，但 attack generator 不能取得生产执行权』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21077:start -->
Primary identity `arXiv:2606.21077v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21077:end -->
<!-- review:SF-2026-ARXIV-2606-21077:end -->

<!-- review:SF-2026-ARXIV-2606-21083:start -->
### 2606.21083 — Coherence Under Commitment: Probing Generalization and Vacuous Memorization in LLM Logical Reasoning

**问题与旧路径。** Large language models (LLMs) deployed for logical reasoning in knowledge-intensive domains exhibit a subtle but critical failure: coherence can be vacuously achieved through systematic abstention. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 逻辑一致性指标必须与 commitment/coverage 联合报告，否则系统性 abstention 会被误判为高 coherence。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21083v1 §3 Methodology; §4 Probability Elicitation Protocol; Appendix A`；Evaluation=`arXiv:2606.21083v1 §5 Setup; §6 Results; §7 Ablations`；counterevidence=`arXiv:2606.21083v1 §8 Conclusion; Appendix B Theoretical Foundations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21083v1 §8 Conclusion; Appendix B Theoretical Foundations`，只支持『逻辑一致性指标必须与 commitment/coverage 联合报告，否则系统性 abstention 会被误判为高 coherence』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21083:start -->
Primary identity `arXiv:2606.21083v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21083:end -->
<!-- review:SF-2026-ARXIV-2606-21083:end -->

<!-- review:SF-2026-ARXIV-2606-21088:start -->
### 2606.21088 — MV-WAM: Manifold-Aware World Action Model with Value Augmentation

**问题与旧路径。** Achieving robust and generalizable manipulation across diverse environments remains a fundamental challenge in embodied robotics. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21088v1 §2 Analysis; §3 Method (§3.2 progress-valued regulation and rollback)`；Evaluation=`arXiv:2606.21088v1 §4 Experiments; Appendix C Real-world Setup; Appendix G Failure Analysis`；counterevidence=`arXiv:2606.21088v1 §5 Limitations; Appendix F Discussion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21088v1 §5 Limitations; Appendix F Discussion`，只支持『长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21088:start -->
Primary identity `arXiv:2606.21088v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21088:end -->
<!-- review:SF-2026-ARXIV-2606-21088:end -->

<!-- review:SF-2026-ARXIV-2606-21101:start -->
### 2606.21101 — DPIFrame: A Dual-Level Parallelism Acceleration Framework for CTR Model Inference

**问题与旧路径。** Deep learning technology has enhanced the ability of Click-through rate (CTR) prediction models to learn features and improve prediction accuracy. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 推荐模型推理的 stream scheduler 应按 embedding、interaction 与 dense 阶段的资源轮廓编排，而不是只按请求 FIFO。唯一知识 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21101v1 §IV DPIFrame Design (§IV-E Stream Scheduling)`；Evaluation=`arXiv:2606.21101v1 §V Evaluation (§V-A Setup; §V-G Scheduling)`；counterevidence=`arXiv:2606.21101v1 §VI Conclusion and evaluated workload boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21101v1 §VI Conclusion and evaluated workload boundary`，只支持『推荐模型推理的 stream scheduler 应按 embedding、interaction 与 dense 阶段的资源轮廓编排，而不是只按请求 FIFO』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。估计失准或 SLO slack 耗尽时停止合批/迁移，回退到隔离队列与保守 admission；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21101:start -->
Primary identity `arXiv:2606.21101v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21101:end -->
<!-- review:SF-2026-ARXIV-2606-21101:end -->

<!-- review:SF-2026-ARXIV-2606-21121:start -->
### 2606.21121 — Answer Engineering: Local Trajectory Editing for Protocol-Constrained Decision Making in Large Language Models

**问题与旧路径。** Large language models can produce confident but protocol-invalid answers in domains where procedural compliance is critical. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 协议约束任务可以在 autoregressive trajectory 上做局部规则编辑；rule coverage、trigger telemetry 与 rollback 必须成为 runtime state。唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21121v1 §4 Decoding-time Control; §5 Runtime Framework`；Evaluation=`arXiv:2606.21121v1 §6 Experiments (§6.5 Telemetry; §6.8 Repair Failures)`；counterevidence=`arXiv:2606.21121v1 §7 Limitations; §9 Future Work`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21121v1 §7 Limitations; §9 Future Work`，只支持『协议约束任务可以在 autoregressive trajectory 上做局部规则编辑；rule coverage、trigger telemetry 与 rollback 必须成为 runtime state』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21121:start -->
Primary identity `arXiv:2606.21121v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21121:end -->
<!-- review:SF-2026-ARXIV-2606-21121:end -->

<!-- review:SF-2026-ARXIV-2606-21126:start -->
### 2606.21126 — What Accuracy and Gradient Cosine Miss: Evaluating Feedback Alignment via Scale Stability, Reference Validity, and Depth Utility

**问题与旧路径。** Despite the success of deep learning, training deep networks in biologically plausible and hardware-efficient ways remains an open challenge. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 评估协议需要同时暴露统计不稳定、metric gaming、prompt sensitivity 与 ranking reversal，单一 aggregate score 不能拥有 release authority。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21126v1 §4 Failure Modes; §6 Recommended Evaluation Protocol`；Evaluation=`arXiv:2606.21126v1 §5 Validation; Appendices A–J`；counterevidence=`arXiv:2606.21126v1 §6.4 Scope and Recommendations; §7 Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21126v1 §6.4 Scope and Recommendations; §7 Conclusion`，只支持『评估协议需要同时暴露统计不稳定、metric gaming、prompt sensitivity 与 ranking reversal，单一 aggregate score 不能拥有 release authority』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21126:start -->
Primary identity `arXiv:2606.21126v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21126:end -->
<!-- review:SF-2026-ARXIV-2606-21126:end -->

<!-- review:SF-2026-ARXIV-2606-21129:start -->
### 2606.21129 — AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents

**问题与旧路径。** Traditional OS security models based on "resource exposure plus permission checks" face structural challenges as LLM-driven autonomous agents acquire capabilities for planning, tool use, network access, and code execution. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** Intent ABI 应把用户意图、capability grant 与 effect-time authorization 编译成可验证接口，而不是把自然语言意图直接当权限。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21129v1 §2 Threat Model; §3 Design; §4 Intent ABI`；Evaluation=`arXiv:2606.21129v1 §5 Security Analysis; §6 Capability Migration`；counterevidence=`arXiv:2606.21129v1 §7 Discussion and Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21129v1 §7 Discussion and Limitations`，只支持『Intent ABI 应把用户意图、capability grant 与 effect-time authorization 编译成可验证接口，而不是把自然语言意图直接当权限』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21129:start -->
Primary identity `arXiv:2606.21129v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21129:end -->
<!-- review:SF-2026-ARXIV-2606-21129:end -->

<!-- review:SF-2026-ARXIV-2606-21130:start -->
### 2606.21130 — Learning Burst-Aware Early Warning Models for Capacity Stress under AI Workload Surges in Hyperscale Data Centers

**问题与旧路径。** The rapid growth of large-scale AI workloads, particularly Large Language Model (LLM) training and inference, is fundamentally reshaping the operational dynamics of hyperscale data centers. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** GPU/AI 服务的异常浪涌要由多窗口 telemetry 与显式阈值选择检测，并把 recall、false alarm 与 detection delay 一起交给 operator。唯一知识 owner 为 `PLATFORM-MONITORING`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21130v1 §III Methodology (§III-B Surge Injection; §III-C XGBoost)`；Evaluation=`arXiv:2606.21130v1 §IV Experimental Evaluation (§IV-E Threshold Selection)`；counterevidence=`arXiv:2606.21130v1 §V Discussion; §VI Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21130v1 §V Discussion; §VI Conclusion`，只支持『GPU/AI 服务的异常浪涌要由多窗口 telemetry 与显式阈值选择检测，并把 recall、false alarm 与 detection delay 一起交给 operator』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。telemetry 缺失或阈值漂移时降级为 observe-only 告警并要求 operator 复核，不自动执行修复；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21130:start -->
Primary identity `arXiv:2606.21130v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21130:end -->
<!-- review:SF-2026-ARXIV-2606-21130:end -->

<!-- review:SF-2026-ARXIV-2606-21140:start -->
### 2606.21140 — Matching Matters: A Fair Quality-Efficiency Benchmark for Command-Line Agents

**问题与旧路径。** Rapid advances in large language models have improved the task-solving capabilities of command-line-interface (CLI)-based agents, whose CLIs determine how models invoke tools, maintain interaction history, and recover from failures. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** Agent benchmark 应把 token、tool call、retry 与 wall-clock 成本纳入同一 token-economic contract，成功率不是资源效率。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21140v1 §3 Benchmark Design; §4 Token-Economic Metrics`；Evaluation=`arXiv:2606.21140v1 §5 Experimental Analysis`；counterevidence=`arXiv:2606.21140v1 §6 Discussion and Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21140v1 §6 Discussion and Limitations`，只支持『Agent benchmark 应把 token、tool call、retry 与 wall-clock 成本纳入同一 token-economic contract，成功率不是资源效率』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21140:start -->
Primary identity `arXiv:2606.21140v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21140:end -->
<!-- review:SF-2026-ARXIV-2606-21140:end -->

<!-- review:SF-2026-ARXIV-2606-21144:start -->
### 2606.21144 — AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents

**问题与旧路径。** Long-term memory systems for Large Language Model (LLM) agents typically try to \emph{remember everything}, extracting memories uniformly to retain as many facts as possible. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** Adaptive memory 应按 task evidence 选择写入、压缩与检索路径，并把 policy state 与事实 state 分离。唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21144v1 §3 AdaMem`；Evaluation=`arXiv:2606.21144v1 §4 Benchmark and Setup; §5 Results`；counterevidence=`arXiv:2606.21144v1 §7 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21144v1 §7 Limitations`，只支持『Adaptive memory 应按 task evidence 选择写入、压缩与检索路径，并把 policy state 与事实 state 分离』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。写入、检索或来源证据不足时 hold/隔离 candidate memory，保留原始轨迹并禁止自动覆盖；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21144:start -->
Primary identity `arXiv:2606.21144v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21144:end -->
<!-- review:SF-2026-ARXIV-2606-21144:end -->

<!-- review:SF-2026-ARXIV-2606-21172:start -->
### 2606.21172 — BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving

**问题与旧路径。** Video world models are increasingly used in autonomous driving to forecast future scene evolution and provide future-aware spatio-temporal representations for downstream action prediction. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** video/world-model poisoning 需要按 poison rate、trigger persistence 与 downstream action effect 验收，干净集精度不能覆盖后门风险。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21172v1 §3.2 Threat Model; §4 Method`；Evaluation=`arXiv:2606.21172v1 §5 Experiments; Appendix A Poison-rate Audit`；counterevidence=`arXiv:2606.21172v1 §6 Limitation`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21172v1 §6 Limitation`，只支持『video/world-model poisoning 需要按 poison rate、trigger persistence 与 downstream action effect 验收，干净集精度不能覆盖后门风险』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21172:start -->
Primary identity `arXiv:2606.21172v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21172:end -->
<!-- review:SF-2026-ARXIV-2606-21172:end -->

<!-- review:SF-2026-ARXIV-2606-21173:start -->
### 2606.21173 — Inverting the Bellman Equation: From $Q$-Values to World Models

**问题与旧路径。** Model-based and model-free reinforcement learning are traditionally viewed as separate paradigms: instead of learning a model of the transition kernel $P$, model-free agents typically estimate value functions tied to a specific policy and reward. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 从 sparse-goal demonstrations 反演 transition dynamics 需要把 reward/goal condition、Bellman identifiability 与 learned transition 分开，恢复条件不是任意环境真值。唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`https://inverting-bellman.github.io/#overview — exact-title project linked to arXiv:2606.21173v1; §Overview, §P-learning and Bellman-inversion formulation`；Evaluation=`https://github.com/aletcher/inverting-bellman#reproduce-paper-figures — linked author repository §Reproduce Paper Figures, §Expected Results and Reacher experiment`；counterevidence=`Not Disclosed — official exact-v1 body unavailable; exact-v1 abstract and linked author artifacts expose sufficient-identifiability and named-environment scope but no dedicated limitation section`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `Not Disclosed — official exact-v1 body unavailable; exact-v1 abstract and linked author artifacts expose sufficient-identifiability and named-environment scope but no dedicated limitation section`，只支持『从 sparse-goal demonstrations 反演 transition dynamics 需要把 reward/goal condition、Bellman identifiability 与 learned transition 分开，恢复条件不是任意环境真值』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。identifiability、rollout uncertainty 或 horizon gate 失败时停止想象 rollout，交还真实环境观测；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21173:start -->
Primary identity `arXiv:2606.21173v1`; access route `accessible_author_primary_artifact_fallback`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21173:end -->
<!-- review:SF-2026-ARXIV-2606-21173:end -->

<!-- review:SF-2026-ARXIV-2606-21188:start -->
### 2606.21188 — Remember what you did?: Learning Behavioral Memories for Partially Observable Object Manipulation

**问题与旧路径。** Long horizon, contact-rich manipulation is inherently partially observable. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** VLA 可先离散化长期 episodic memory 并预训练 action head，但 memory code、policy state 与真实机器人 observation identity 必须联结。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21188v1 §3 Method (memory pretraining, discretization and action head)`；Evaluation=`arXiv:2606.21188v1 §4 Simulation and Real Robot; Appendices A–B`；counterevidence=`arXiv:2606.21188v1 §5 Limitations and Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21188v1 §5 Limitations and Conclusion`，只支持『VLA 可先离散化长期 episodic memory 并预训练 action head，但 memory code、policy state 与真实机器人 observation identity 必须联结』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21188:start -->
Primary identity `arXiv:2606.21188v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21188:end -->
<!-- review:SF-2026-ARXIV-2606-21188:end -->

<!-- review:SF-2026-ARXIV-2606-21228:start -->
### 2606.21228 — Sakana Fugu Technical Report

**问题与旧路径。** The capabilities of frontier Large Language Models (LLMs) continue to advance, with different providers increasingly specializing in distinct domains. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中。唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21228v1 §3 Sakana Fugu (§3.1 Fugu; §3.2 Fugu-Ultra)`；Evaluation=`arXiv:2606.21228v1 §4 Capabilities; Appendix A Evaluation Configuration; Appendix B`；counterevidence=`arXiv:2606.21228v1 §5 Conclusions and evaluated agent/task scope`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21228v1 §5 Conclusions and evaluated agent/task scope`，只支持『多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。共享状态或独立复核发生冲突时暂停 commit，回到单 Agent baseline 或串行 adjudication；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21228:start -->
Primary identity `arXiv:2606.21228v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21228:end -->
<!-- review:SF-2026-ARXIV-2606-21228:end -->

<!-- review:SF-2026-ARXIV-2606-21238:start -->
### 2606.21238 — Recency/Frequency Adaptive KV Caching for Large Language Model Serving

**问题与旧路径。** Key-value (KV) caching is a powerful technique for accelerating large language model inference and generation. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** KV cache 可按对话、batch 与访问热度自适应分区；partition version、迁移成本与 miss fallback 必须进入 cache control state。唯一知识 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21238v1 §3 Method`；Evaluation=`arXiv:2606.21238v1 §4 Evaluation (DQA, conversation, batch and adaptive partitioning)`；counterevidence=`arXiv:2606.21238v1 §5 Conclusion; §6 Future Work`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21238v1 §5 Conclusion; §6 Future Work`，只支持『KV cache 可按对话、batch 与访问热度自适应分区；partition version、迁移成本与 miss fallback 必须进入 cache control state』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。cache identity、容量或迁移收益不满足时回退到重算或本地 KV，并记录 miss/eviction 原因；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21238:start -->
Primary identity `arXiv:2606.21238v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21238:end -->
<!-- review:SF-2026-ARXIV-2606-21238:end -->

<!-- review:SF-2026-ARXIV-2606-21249:start -->
### 2606.21249 — Does RoPE Prevent or Degrade Retrieval Heads? A Mechanistic Analysis Across Model Families

**问题与旧路径。** Retrieval heads, attention heads that copy information from earlier context to the current position, have been proposed as the mechanistic substrate for long-context recall. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 位置表示的训练动力学需要区分静态相关、训练演化与因果消融，最终 probe 相似度不能证明模型真的使用该位置通道。唯一知识 owner 为 `MODEL-POSITION-ENCODING`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21249v1 §3 Methods`；Evaluation=`arXiv:2606.21249v1 §4 Static Analysis; §5 Training Dynamics; §6 Causal Validation; §7 Quantitative Ablation`；counterevidence=`arXiv:2606.21249v1 §6 Scope and Caveats; §9 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21249v1 §6 Scope and Caveats; §9 Limitations`，只支持『位置表示的训练动力学需要区分静态相关、训练演化与因果消融，最终 probe 相似度不能证明模型真的使用该位置通道』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。因果消融不支持时保留现有位置方案，不由 probe 相似度触发架构替换；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21249:start -->
Primary identity `arXiv:2606.21249v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21249:end -->
<!-- review:SF-2026-ARXIV-2606-21249:end -->

<!-- review:SF-2026-ARXIV-2606-21255:start -->
### 2606.21255 — SCOPE: Sequential Conformal Probing for Reliable OOD Rejection in LLM Services

**问题与旧路径。** Rejecting inputs outside the defined in-distribution (IND) service scope is critical for large language model (LLM) services, where unsupported requests should be filtered before full generation. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** uncertainty gate 只有经 calibration 与 certifying boundary 后才能影响 release；置信度本身不是安全证明。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21255v1 §3 Method (§3.2 Calibrated Gate; §3.3 Certifying Boundary)`；Evaluation=`arXiv:2606.21255v1 §4 Experiments; Appendices A–C and E–F`；counterevidence=`arXiv:2606.21255v1 §5 Conclusion; Appendix D Boundary Construction`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21255v1 §5 Conclusion; Appendix D Boundary Construction`，只支持『uncertainty gate 只有经 calibration 与 certifying boundary 后才能影响 release；置信度本身不是安全证明』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21255:start -->
Primary identity `arXiv:2606.21255v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21255:end -->
<!-- review:SF-2026-ARXIV-2606-21255:end -->

<!-- review:SF-2026-ARXIV-2606-21257:start -->
### 2606.21257 — An Empirical Study of openPangu Quantization on Ascend NPUs

**问题与旧路径。** openPangu models are attractive targets for private and domestic large-language-model deployment, yet their robustness under aggressive post-training quantization on Ascend NPUs has not been systematically characterized. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 端侧大模型 PTQ 必须把 weight/activation bit-width、算子支持与任务退化一起验收，压缩比不能代表可部署性。唯一知识 owner 为 `INFER-GPU-MEMORY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21257v1 §2 Empirical Study (§2.1 Settings)`；Evaluation=`arXiv:2606.21257v1 §2.2 PTQ; §2.3 Ablation; §2.4 Task Evaluation`；counterevidence=`arXiv:2606.21257v1 §4 Limitations and Future Work`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21257v1 §4 Limitations and Future Work`，只支持『端侧大模型 PTQ 必须把 weight/activation bit-width、算子支持与任务退化一起验收，压缩比不能代表可部署性』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21257:start -->
Primary identity `arXiv:2606.21257v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21257:end -->
<!-- review:SF-2026-ARXIV-2606-21257:end -->

<!-- review:SF-2026-ARXIV-2606-21262:start -->
### 2606.21262 — ARCO: Adaptive Rubrics with Co-Evolution for Multi-Step LLM-Based Agents

**问题与旧路径。** Reinforcement learning for multi-step LLM agents often relies on scalar rewards that indicate success but cannot explain why a trajectory is good or bad. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** rubric 与 candidate co-evolution 必须隔离生成、judge 与 held-out adjudication，避免 evaluator 随被测对象共同漂移。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21262v1 §3 ARCO (hierarchical rubric and co-evolution); Appendix A`；Evaluation=`arXiv:2606.21262v1 §4 Experiments; Appendices B–D`；counterevidence=`arXiv:2606.21262v1 §6 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21262v1 §6 Limitations`，只支持『rubric 与 candidate co-evolution 必须隔离生成、judge 与 held-out adjudication，避免 evaluator 随被测对象共同漂移』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21262:start -->
Primary identity `arXiv:2606.21262v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21262:end -->
<!-- review:SF-2026-ARXIV-2606-21262:end -->

<!-- review:SF-2026-ARXIV-2606-21282:start -->
### 2606.21282 — Differential Zonotopes for Verifying Global Robustness of DNNs

**问题与旧路径。** The robustness of deep neural networks (DNNs) is critical in security-sensitive applications, where small input perturbations should not alter model predictions. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** DNN global robustness 是输入对的 2-safety property；differential halo zonotope 联合传播两条执行并界定 divergence，而非重复 local ball 检查。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §4.3 Verification Algorithm and Differential Halo Zonotope Abstract Domain`；Evaluation=`doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §5.2 Asymmetric Confidence-Based Global Robustness and Law/LHC/HAR benchmarks`；counterevidence=`doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §6 Conclusion states counterexample search and compositional scaling remain future work`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §6 Conclusion states counterexample search and compositional scaling remain future work`，只支持『DNN global robustness 是输入对的 2-safety property；differential halo zonotope 联合传播两条执行并界定 divergence，而非重复 local ball 检查』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21282:start -->
Primary identity `arXiv:2606.21282v1`; access route `accessible_exact_identity_author_manuscript_mirror_fallback`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21282:end -->
<!-- review:SF-2026-ARXIV-2606-21282:end -->

<!-- review:SF-2026-ARXIV-2606-21307:start -->
### 2606.21307 — Task-Differentiated Atomic Skill Expansion and Routing for Continual Learning Across Highly Heterogeneous Tasks

**问题与旧路径。** Continual learning (CL) is commonly studied under the assumption that sequential tasks are semantically related or structurally similar. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** skill expansion 应先检测能力缺口、生成 candidate skill、独立验证再路由，单次成功不能直接提升为长期 skill。唯一知识 owner 为 `AGENT-REFLECTION`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21307v1 §3 Method (skill expansion, detection and routing)`；Evaluation=`arXiv:2606.21307v1 §4 Benchmark; §5 Setup; §6 Analysis`；counterevidence=`arXiv:2606.21307v1 §7 Conclusion and benchmark/skill-library scope`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21307v1 §7 Conclusion and benchmark/skill-library scope`，只支持『skill expansion 应先检测能力缺口、生成 candidate skill、独立验证再路由，单次成功不能直接提升为长期 skill』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。held-out 验证失败时拒绝 promotion，保留旧 skill/policy 与 candidate lesson 的分离状态；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21307:start -->
Primary identity `arXiv:2606.21307v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21307:end -->
<!-- review:SF-2026-ARXIV-2606-21307:end -->

<!-- review:SF-2026-ARXIV-2606-21315:start -->
### 2606.21315 — Social World Model for Lifelong Social Intelligence

**问题与旧路径。** Social intelligence is a core competency for language agents, yet current research primarily focuses on static capability evaluation rather than how these skills are continuously shaped and accumulated. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** Social World Model 要把多主体状态、关系变化与 action-conditioned transition 分层，并用 wake/sleep/deploy gates 限制自更新。唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21315v1 §3 Social World Model (five-dimensional decomposition; wake-sleep-deploy gates)`；Evaluation=`arXiv:2606.21315v1 §4 Benchmark; §5 Experiments`；counterevidence=`arXiv:2606.21315v1 §6 Discussion (specificity and ablations)`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21315v1 §6 Discussion (specificity and ablations)`，只支持『Social World Model 要把多主体状态、关系变化与 action-conditioned transition 分层，并用 wake/sleep/deploy gates 限制自更新』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。identifiability、rollout uncertainty 或 horizon gate 失败时停止想象 rollout，交还真实环境观测；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21315:start -->
Primary identity `arXiv:2606.21315v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21315:end -->
<!-- review:SF-2026-ARXIV-2606-21315:end -->

<!-- review:SF-2026-ARXIV-2606-21337:start -->
### 2606.21337 — DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams

**问题与旧路径。** Raw multimodal streams are abundant but noisy, redundant, and unaligned with any particular training objective. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 训练数据 pipeline 应将任务生成、过滤、difficulty routing 与训练后 validation 绑定同一 lineage，synthetic volume 不是质量证明。唯一知识 owner 为 `TRAIN-DATA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21337v1 §3 Method (pipeline, GRPO and deployment)`；Evaluation=`arXiv:2606.21337v1 §4 Experiments; Appendix A Benchmark; Appendix B Training and Deployment`；counterevidence=`arXiv:2606.21337v1 §5 Conclusion and dataset/model scope`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21337v1 §5 Conclusion and dataset/model scope`，只支持『训练数据 pipeline 应将任务生成、过滤、difficulty routing 与训练后 validation 绑定同一 lineage，synthetic volume 不是质量证明』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。lineage、过滤或 validation receipt 缺失时隔离该数据批，不进入不可逆训练更新；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21337:start -->
Primary identity `arXiv:2606.21337v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21337:end -->
<!-- review:SF-2026-ARXIV-2606-21337:end -->

<!-- review:SF-2026-ARXIV-2606-21338:start -->
### 2606.21338 — "What Happens Locally, Leaks Globally": Detecting Privacy Leakage Risks in MCP Servers

**问题与旧路径。** The Model Context Protocol (MCP) has rapidly become the de facto standard for connecting large language models (LLMs) to external resources, but it also introduces a class of privacy risks that existing tools are ill-equipped to detect. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21338v1 §3 MCPPrivacyDetector and Taint Analysis`；Evaluation=`arXiv:2606.21338v1 §4 Evaluation`；counterevidence=`arXiv:2606.21338v1 §6 Conclusion and evaluated MCP/tool boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21338v1 §6 Conclusion and evaluated MCP/tool boundary`，只支持『MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21338:start -->
Primary identity `arXiv:2606.21338v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21338:end -->
<!-- review:SF-2026-ARXIV-2606-21338:end -->

<!-- review:SF-2026-ARXIV-2606-21359:start -->
### 2606.21359 — Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs

**问题与旧路径。** Large language models (LLMs) are increasingly used to communicate and explain scientific concepts, yet their tendency to hallucinate poses significant risks in this high stakes use-case. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** hallucination benchmark 应绑定 evidence source、错误 taxonomy 与 human validation，自动 judge 分数不能替代 claim-level provenance。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21359v1 §2 Benchmark; §3 Hallucination Taxonomy`；Evaluation=`arXiv:2606.21359v1 §4 Setup; §5 Results; §6 Human Validation; Appendices C and E–H`；counterevidence=`arXiv:2606.21359v1 §7 Limitations exact headings: Evidence Source Limitations; Training-data Contamination; Confounding Fine-tuning Factors; Human-study Scope`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21359v1 §7 Limitations exact headings: Evidence Source Limitations; Training-data Contamination; Confounding Fine-tuning Factors; Human-study Scope`，只支持『hallucination benchmark 应绑定 evidence source、错误 taxonomy 与 human validation，自动 judge 分数不能替代 claim-level provenance』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21359:start -->
Primary identity `arXiv:2606.21359v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21359:end -->
<!-- review:SF-2026-ARXIV-2606-21359:end -->

<!-- review:SF-2026-ARXIV-2606-21372:start -->
### 2606.21372 — NAC: Neural Action Codec for Vision-Language-Action Models

**问题与旧路径。** Vision-language-action (VLA) models rely on discrete action tokenizers to bridge continuous robot control and autoregressive sequence modeling, yet existing tokenizers often trade off between compression, latency, and downstream performance. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** neural action codec 把连续控制压缩成离散 token 时，codebook identity、重构误差与 policy action head 必须作为同一部署 artifact。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21372v1 §3 Method (NAC tokenizer and behavioral cloning); Appendix A`；Evaluation=`arXiv:2606.21372v1 §4 Experiments; Appendix B`；counterevidence=`arXiv:2606.21372v1 §5 Discussion and codec/policy scope`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21372v1 §5 Discussion and codec/policy scope`，只支持『neural action codec 把连续控制压缩成离散 token 时，codebook identity、重构误差与 policy action head 必须作为同一部署 artifact』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21372:start -->
Primary identity `arXiv:2606.21372v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21372:end -->
<!-- review:SF-2026-ARXIV-2606-21372:end -->

<!-- review:SF-2026-ARXIV-2606-21386:start -->
### 2606.21386 — VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models

**问题与旧路径。** Vision-language-action models (VLAs) achieve state-of-the-art performance on many robotic manipulation tasks, yet they can still behave unpredictably in out-of-distribution scenarios. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** VLA failure benchmark 应分别标注 perception、reasoning 与 action failure，并保留 intervention/fallback 可执行证据。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21386v1 §3 Method (LLMD, ACC and VLA-FAIL)`；Evaluation=`arXiv:2606.21386v1 §4 Experiments; §5 Results; Appendices A–F`；counterevidence=`arXiv:2606.21386v1 §6 Limitations; Appendix D.2 Failure Cases`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21386v1 §6 Limitations; Appendix D.2 Failure Cases`，只支持『VLA failure benchmark 应分别标注 perception、reasoning 与 action failure，并保留 intervention/fallback 可执行证据』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21386:start -->
Primary identity `arXiv:2606.21386v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21386:end -->
<!-- review:SF-2026-ARXIV-2606-21386:end -->

<!-- review:SF-2026-ARXIV-2606-21389:start -->
### 2606.21389 — From Production SIEM to Reusable Cybersecurity Artifacts

**问题与旧路径。** Operational evidence is not automatically scientific evidence. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 生产 SIEM telemetry 转研究 artifact 时必须保留时间与 entity consistency，同时声明 anonymization 的 privacy-utility boundary 而非声称形式匿名。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21389v1 §3 Methodology and Datasets`；Evaluation=`arXiv:2606.21389v1 §4 Validation`；counterevidence=`arXiv:2606.21389v1 §5 Discussion; §7 Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21389v1 §5 Discussion; §7 Conclusion`，只支持『生产 SIEM telemetry 转研究 artifact 时必须保留时间与 entity consistency，同时声明 anonymization 的 privacy-utility boundary 而非声称形式匿名』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21389:start -->
Primary identity `arXiv:2606.21389v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21389:end -->
<!-- review:SF-2026-ARXIV-2606-21389:end -->

<!-- review:SF-2026-ARXIV-2606-21398:start -->
### 2606.21398 — BIT-Nav: Brain-Inspired Trajectory Memory for Embodied Navigation

**问题与旧路径。** Vision-Language Models (VLMs) for embodied navigation rely on selecting a fixed number of frames from a growing trajectory history. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 具身表征与动作 token 的对齐可由对比目标训练，但 representation gain 必须落到控制任务与 failure slice，而非只看 embedding quality。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21398v1 §III Methodology (BITE, InfoNCE and Qwen integration)`；Evaluation=`arXiv:2606.21398v1 §IV Results`；counterevidence=`arXiv:2606.21398v1 §IV-D Discussion and Limitations; §V Future Work`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21398v1 §IV-D Discussion and Limitations; §V Future Work`，只支持『具身表征与动作 token 的对齐可由对比目标训练，但 representation gain 必须落到控制任务与 failure slice，而非只看 embedding quality』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21398:start -->
Primary identity `arXiv:2606.21398v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21398:end -->
<!-- review:SF-2026-ARXIV-2606-21398:end -->

<!-- review:SF-2026-ARXIV-2606-21399:start -->
### 2606.21399 — Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention

**问题与旧路径。** Runtime oversight for LLM agents is commonly framed as scalar risk prediction: estimate failure likelihood, confidence, or uncertainty, then intervene once the score crosses a threshold. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** calibration 只能描述 observational confidence，不能单独支持 intervention；Agent control 需要 action-conditioned branching 与可验证 outcome channel。唯一知识 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21399v1 §2 Scalar-control Sufficiency; §3 Prefix Branching; §4 Action-conditioned Controller`；Evaluation=`arXiv:2606.21399v1 §5 Results; Appendices B–C`；counterevidence=`arXiv:2606.21399v1 §7 Conclusion and action/benchmark boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21399v1 §7 Conclusion and action/benchmark boundary`，只支持『calibration 只能描述 observational confidence，不能单独支持 intervention；Agent control 需要 action-conditioned branching 与可验证 outcome channel』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。calibration 与 action outcome 不一致时收回 autonomous commit authority，降级为 proposal-only；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21399:start -->
Primary identity `arXiv:2606.21399v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21399:end -->
<!-- review:SF-2026-ARXIV-2606-21399:end -->

<!-- review:SF-2026-ARXIV-2606-21401:start -->
### 2606.21401 — SwarmX: Agentic Scheduling for Low-Latency Agentic Systems

**问题与旧路径。** Agentic AI applications compose multiple model calls and tool executions, creating new scheduling challenges for GPU-CPU clusters. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 大规模 Agent swarm 的调度对象是带依赖和状态的 task graph，placement、重试与资源隔离要由平台而非 coordinator prompt 持有。唯一知识 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21401v1 §3 SwarmX Design; §4 Implementation`；Evaluation=`arXiv:2606.21401v1 §5 Evaluation (production and overhead)`；counterevidence=`arXiv:2606.21401v1 §6 Production and Operation Experience; §8 Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21401v1 §6 Production and Operation Experience; §8 Conclusion`，只支持『大规模 Agent swarm 的调度对象是带依赖和状态的 task graph，placement、重试与资源隔离要由平台而非 coordinator prompt 持有』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。估计失准或 SLO slack 耗尽时停止合批/迁移，回退到隔离队列与保守 admission；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21401:start -->
Primary identity `arXiv:2606.21401v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21401:end -->
<!-- review:SF-2026-ARXIV-2606-21401:end -->

<!-- review:SF-2026-ARXIV-2606-21406:start -->
### 2606.21406 — Robot Self-Improvement via Human-Video Dynamics Models

**问题与旧路径。** A central question in robot learning is how to acquire skills from the kinds of data that humans learn from: passive observation, embodied practice, and the experience of failure. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** VLA 自改进必须把 data collection、critic signal 与 policy update 版本化，并在真实动作前保留 independent safety gate。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21406v1 §4 Method (iterative self-improvement, DGAC and policy update)`；Evaluation=`arXiv:2606.21406v1 §5 Experiments; Appendix A.2`；counterevidence=`arXiv:2606.21406v1 §6 Limitations and Future Work`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21406v1 §6 Limitations and Future Work`，只支持『VLA 自改进必须把 data collection、critic signal 与 policy update 版本化，并在真实动作前保留 independent safety gate』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21406:start -->
Primary identity `arXiv:2606.21406v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21406:end -->
<!-- review:SF-2026-ARXIV-2606-21406:end -->

<!-- review:SF-2026-ARXIV-2606-21409:start -->
### 2606.21409 — Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents

**问题与旧路径。** Tool-augmented agents are typically evaluated by their gains under reliable external feedback. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** tool-call repair 不能只改最终格式；应反演失败调用的 constraint、局部修补 argument 并在有限重试后回退。唯一知识 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21409v1 §2 Controlled Matched-loop Design`；Evaluation=`arXiv:2606.21409v1 §3 Inversion; §4 Scope; §5 Failure Structure; Appendices B–C`；counterevidence=`arXiv:2606.21409v1 §6 Fallback-limited Repairs; §9 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21409v1 §6 Fallback-limited Repairs; §9 Limitations`，只支持『tool-call repair 不能只改最终格式；应反演失败调用的 constraint、局部修补 argument 并在有限重试后回退』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。constraint repair 仍失败时停止有限重试，返回结构化错误并要求用户或 workflow 决策；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21409:start -->
Primary identity `arXiv:2606.21409v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21409:end -->
<!-- review:SF-2026-ARXIV-2606-21409:end -->

<!-- review:SF-2026-ARXIV-2606-21428:start -->
### 2606.21428 — Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study

**问题与旧路径。** Mixture-of-Experts (MoE) language models are often described as ideal for resource-constrained inference. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 端侧 LLM benchmark 必须绑定具体模型、backend、硬件、prompt 与测量口径，峰值内存或 tokens/s 不能跨设备直接外推。唯一知识 owner 为 `INFER-GPU-MEMORY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21428v1 §3 Methodology (hardware, backend, models, prompts and metrics)`；Evaluation=`arXiv:2606.21428v1 §4 Results`；counterevidence=`arXiv:2606.21428v1 §5 Discussion and Bottleneck; §6 Threats to Validity`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21428v1 §5 Discussion and Bottleneck; §6 Threats to Validity`，只支持『端侧 LLM benchmark 必须绑定具体模型、backend、硬件、prompt 与测量口径，峰值内存或 tokens/s 不能跨设备直接外推』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21428:start -->
Primary identity `arXiv:2606.21428v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21428:end -->
<!-- review:SF-2026-ARXIV-2606-21428:end -->

<!-- review:SF-2026-ARXIV-2606-21445:start -->
### 2606.21445 — AutoRAS: Learning Robust Agentic Systems with Primitive Representations

**问题与旧路径。** The automated design of agentic systems offers a promising pathway for scaling large language models (LLMs) beyond single-agent reasoning. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** Agent workflow robustness 应把 primitive sequence、state transition 与 recovery branch 显式化，最终成功会掩盖脆弱中间路径。唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21445v1 §3 Preliminaries; §4 Methodology (primitive sequence, robustness and flow exploration)`；Evaluation=`arXiv:2606.21445v1 §5 Experiments; Appendices A–F`；counterevidence=`arXiv:2606.21445v1 §6 Discussion (reliability and generalization)`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21445v1 §6 Discussion (reliability and generalization)`，只支持『Agent workflow robustness 应把 primitive sequence、state transition 与 recovery branch 显式化，最终成功会掩盖脆弱中间路径』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21445:start -->
Primary identity `arXiv:2606.21445v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21445:end -->
<!-- review:SF-2026-ARXIV-2606-21445:end -->

<!-- review:SF-2026-ARXIV-2606-21509:start -->
### 2606.21509 — A Stitch in Time Saves Nine: Preserving Policy Compatibility Under Perception Updates in End-to-End Autonomous Driving

**问题与旧路径。** End-to-end autonomous driving systems tightly couple perception and decision-making through latent representations. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 异构 VLA 模块 stitching 需要显式 sensor/action interface 与 latency budget，子模型可互换不代表闭环状态连续。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21509v1 §III Methodology and Model Stitching`；Evaluation=`arXiv:2606.21509v1 §IV Experiments (hardware, performance and efficiency)`；counterevidence=`arXiv:2606.21509v1 §V Conclusion; Appendix A Sensor Setup`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21509v1 §V Conclusion; Appendix A Sensor Setup`，只支持『异构 VLA 模块 stitching 需要显式 sensor/action interface 与 latency budget，子模型可互换不代表闭环状态连续』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21509:start -->
Primary identity `arXiv:2606.21509v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21509:end -->
<!-- review:SF-2026-ARXIV-2606-21509:end -->

<!-- review:SF-2026-ARXIV-2606-21514:start -->
### 2606.21514 — Towards Understanding the Power and Limits of the Muon Optimizer: A River-Valley Perspective

**问题与旧路径。** Recently, Muon has gained substantial attention as an appealing alternative to Adam-like optimizers, with many works highlighting its advantages through spectral normalization and improved conditioning. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure。唯一知识 owner 为 `TRAIN-PRETRAINING`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21514v1 §3 Mixed-spiked Matrix Sensing; §4 River-valley Generalization`；Evaluation=`arXiv:2606.21514v1 §5 Empirical Study; Appendices B–C`；counterevidence=`arXiv:2606.21514v1 Appendix B.3 Late-stage Failure; Appendix B.4 Implications; §6 Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21514v1 Appendix B.3 Late-stage Failure; Appendix B.4 Implications; §6 Conclusion`，只支持『深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。loss/curvature 或稳定性证据偏离时冻结阶段转换并回退到已验证 schedule/checkpoint；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21514:start -->
Primary identity `arXiv:2606.21514v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21514:end -->
<!-- review:SF-2026-ARXIV-2606-21514:end -->

<!-- review:SF-2026-ARXIV-2606-21553:start -->
### 2606.21553 — Dissecting Agentic RAG: A Component Ablation for Multi-Hop QA with a Local 7B Model

**问题与旧路径。** Agentic retrieval-augmented generation (RAG) systems combine iterative reasoning loops, query decomposition, and adaptive retrieval to tackle multi-hop question answering. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** RAG 系统需要联合检索、生成与证据评估，HotpotQA 上的答案提升不能单独证明索引 freshness 或生产一致性。唯一知识 owner 为 `AGENT-RAG`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21553v1 §3 System Architecture`；Evaluation=`arXiv:2606.21553v1 §4 Setup; §5 Results; §6 Analysis`；counterevidence=`arXiv:2606.21553v1 §7 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21553v1 §7 Limitations`，只支持『RAG 系统需要联合检索、生成与证据评估，HotpotQA 上的答案提升不能单独证明索引 freshness 或生产一致性』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。evidence、index 或 verifier identity 不完整时 abstain/回到原始证据，不把生成结果写成事实；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21553:start -->
Primary identity `arXiv:2606.21553v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21553:end -->
<!-- review:SF-2026-ARXIV-2606-21553:end -->

<!-- review:SF-2026-ARXIV-2606-21565:start -->
### 2606.21565 — Composing Verifiable Conceptual Models via Building Blocks: Towards Design-Time Verification of Agentic AI Workflows

**问题与旧路径。** Agentic AI systems orchestrate multiple LLM-based agents through workflow architectures that coordinate decisions, tools, and external actions. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** Agent-based simulation 的角色、规则、environment transition 与 observation 必须成为可重放 artifact，而非仅保存在 prompt 叙述中。唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21565v1 §3 Methods (ABM representation and rules)`；Evaluation=`arXiv:2606.21565v1 §4 Results (prototype and evaluation)`；counterevidence=`arXiv:2606.21565v1 §5 Discussion; explicit no prompt/tool/safety/reversibility/auth scope`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21565v1 §5 Discussion; explicit no prompt/tool/safety/reversibility/auth scope`，只支持『Agent-based simulation 的角色、规则、environment transition 与 observation 必须成为可重放 artifact，而非仅保存在 prompt 叙述中』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21565:start -->
Primary identity `arXiv:2606.21565v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21565:end -->
<!-- review:SF-2026-ARXIV-2606-21565:end -->

<!-- review:SF-2026-ARXIV-2606-21572:start -->
### 2606.21572 — Robot Critics that Sweat the Small Stuff

**问题与旧路径。** Large vision-language models contain several priors about the world and object interactions, making them useful critics during inference to steer robot policies towards success. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** VLA critic 要先在 failure evidence 上独立训练，再以受限 signal 进入 policy update；critic score 不能拥有物理提交权。唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21572v1 §3 Method (training critics and policy integration)`；Evaluation=`arXiv:2606.21572v1 §4 Critic Evaluation; §5 In-loop Evaluation; Appendices A–C`；counterevidence=`arXiv:2606.21572v1 §5.3 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21572v1 §5.3 Limitations`，只支持『VLA critic 要先在 failure evidence 上独立训练，再以受限 signal 进入 policy update；critic score 不能拥有物理提交权』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21572:start -->
Primary identity `arXiv:2606.21572v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21572:end -->
<!-- review:SF-2026-ARXIV-2606-21572:end -->

<!-- review:SF-2026-ARXIV-2606-21584:start -->
### 2606.21584 — When EER Hides Deployment Failure: Auditing Threshold Transfer and Unlabeled Score Calibration for Speech Deepfake Detectors

**问题与旧路径。** Speech deepfake countermeasures (CMs) are compared almost exclusively by equal error rate (EER), a metric computed at an oracle threshold chosen on the labeled test set. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** deployment threshold 必须从开发集冻结并在目标分布报告 HTER；test-set oracle EER 会隐藏真实 false-reject/false-accept failure。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21584v1 §2 Threshold Transfer; §3 Audited Corrections`；Evaluation=`arXiv:2606.21584v1 §4 Experiments (cross-dataset transfer and fragility)`；counterevidence=`arXiv:2606.21584v1 §4.5 Limitations; §5 Recommendations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21584v1 §4.5 Limitations; §5 Recommendations`，只支持『deployment threshold 必须从开发集冻结并在目标分布报告 HTER；test-set oracle EER 会隐藏真实 false-reject/false-accept failure』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21584:start -->
Primary identity `arXiv:2606.21584v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21584:end -->
<!-- review:SF-2026-ARXIV-2606-21584:end -->

<!-- review:SF-2026-ARXIV-2606-21627:start -->
### 2606.21627 — Counsel: A Meta-Evaluation Dataset for Agentic Tasks

**问题与旧路径。** As agentic systems tackle increasingly complex multi-step tasks, evaluating their trajectories presents a major bottleneck - human annotation of a single trajectory on popular agentic benchmarks can take hours, making it difficult to scale evaluations for measuring performance or curating training data. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** trajectory preference evaluation 应保存环境、轨迹、judge 与 human disagreement，pairwise label 不是脱离 policy 的稳定真值。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21627v1 §3 Methods (environments, trajectories, judgments and human annotation)`；Evaluation=`arXiv:2606.21627v1 §4 Dataset Analysis; Appendix D Evaluation in the Loop`；counterevidence=`arXiv:2606.21627v1 §5.1 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21627v1 §5.1 Limitations`，只支持『trajectory preference evaluation 应保存环境、轨迹、judge 与 human disagreement，pairwise label 不是脱离 policy 的稳定真值』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21627:start -->
Primary identity `arXiv:2606.21627v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21627:end -->
<!-- review:SF-2026-ARXIV-2606-21627:end -->

<!-- review:SF-2026-ARXIV-2606-21633:start -->
### 2606.21633 — HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval

**问题与旧路径。** The KV cache dominates GPU memory in long-context LLM serving, crowding out batch capacity and leaving GPU compute idle. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 长上下文 retrieval 可把 cold state 分层到 CPU 并用 GPU kernel 协同读取，但 index/cache identity 与传输重叠决定真实收益。唯一知识 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21633v1 §3 Motivation; §4 HERALD (CPU-GPU retrieval and kernel); §5 Implementation`；Evaluation=`arXiv:2606.21633v1 §6 Evaluation`；counterevidence=`arXiv:2606.21633v1 §8 Conclusion and evaluated platform boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21633v1 §8 Conclusion and evaluated platform boundary`，只支持『长上下文 retrieval 可把 cold state 分层到 CPU 并用 GPU kernel 协同读取，但 index/cache identity 与传输重叠决定真实收益』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。cache identity、容量或迁移收益不满足时回退到重算或本地 KV，并记录 miss/eviction 原因；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21633:start -->
Primary identity `arXiv:2606.21633v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21633:end -->
<!-- review:SF-2026-ARXIV-2606-21633:end -->

<!-- review:SF-2026-ARXIV-2606-21638:start -->
### 2606.21638 — Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs

**问题与旧路径。** Open-weight Large Language Models (LLMs) enable scientific progress and broad deployment. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** tiered language-model service 应按 capability/risk 分离模型与权限；成本路由不能让弱安全模型获得强 effect authority。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21638v1 §3 Tiered Language Models and Training Protocol`；Evaluation=`arXiv:2606.21638v1 §4 Capability Separation; §5 Cost; §6 Robustness; §7 Scaling`；counterevidence=`arXiv:2606.21638v1 §9 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21638v1 §9 Limitations`，只支持『tiered language-model service 应按 capability/risk 分离模型与权限；成本路由不能让弱安全模型获得强 effect authority』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21638:start -->
Primary identity `arXiv:2606.21638v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21638:end -->
<!-- review:SF-2026-ARXIV-2606-21638:end -->

<!-- review:SF-2026-ARXIV-2606-21654:start -->
### 2606.21654 — ChainWorld: Composing Long-Horizon Desktop Workloads from Atomic OSWorld Tasks

**问题与旧路径。** Computer use agents are evaluated almost exclusively on atomic desktop tasks, but realistic desktop work requires sustaining state across multiple objectives. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** compositional evaluation 应保存组件、组合、judge 与 failure attribution，组合总分不能定位哪个 handoff 失效。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21654v1 §3 Framework (agent context, composition engine and evaluation)`；Evaluation=`arXiv:2606.21654v1 §4 Results and Failures; Appendix A`；counterevidence=`arXiv:2606.21654v1 §6 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21654v1 §6 Limitations`，只支持『compositional evaluation 应保存组件、组合、judge 与 failure attribution，组合总分不能定位哪个 handoff 失效』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21654:start -->
Primary identity `arXiv:2606.21654v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21654:end -->
<!-- review:SF-2026-ARXIV-2606-21654:end -->

<!-- review:SF-2026-ARXIV-2606-21666:start -->
### 2606.21666 — Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems

**问题与旧路径。** Multi-agent LLM systems routinely produce hallucinated outputs that cannot be explained by model deficiencies alone. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 多 Agent 共识要保存独立 evidence、divergence 与 shared verification；重复采样的多数票不等于独立证明。唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21666v1 §3 Framework (agent context, divergence and shared verification)`；Evaluation=`arXiv:2606.21666v1 §4 Setup; §5 Results`；counterevidence=`arXiv:2606.21666v1 §6.2 Limitations; §6.3 Contamination`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21666v1 §6.2 Limitations; §6.3 Contamination`，只支持『多 Agent 共识要保存独立 evidence、divergence 与 shared verification；重复采样的多数票不等于独立证明』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。共享状态或独立复核发生冲突时暂停 commit，回到单 Agent baseline 或串行 adjudication；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21666:start -->
Primary identity `arXiv:2606.21666v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21666:end -->
<!-- review:SF-2026-ARXIV-2606-21666:end -->

<!-- review:SF-2026-ARXIV-2606-21678:start -->
### 2606.21678 — Decodable but Not Faithful: Coupling Natural-Language Rationales to Programmatic Verifiers

**问题与旧路径。** Language models can generate plausible rationales for their predictions, but these explanations may not faithfully represent the model's internal reasoning. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 从 internal representation 可解码出答案不证明 reasoning faithful；diagnostic ladder 要区分 decodability、causal use 与输出行为。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21678v1 §4 Method (format, objective, information constraints and diagnostic ladder)`；Evaluation=`arXiv:2606.21678v1 §5 Experiments; Appendices A–C`；counterevidence=`arXiv:2606.21678v1 §6 Discussion: structural decodability-faithfulness gap`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21678v1 §6 Discussion: structural decodability-faithfulness gap`，只支持『从 internal representation 可解码出答案不证明 reasoning faithful；diagnostic ladder 要区分 decodability、causal use 与输出行为』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21678:start -->
Primary identity `arXiv:2606.21678v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21678:end -->
<!-- review:SF-2026-ARXIV-2606-21678:end -->

<!-- review:SF-2026-ARXIV-2606-21710:start -->
### 2606.21710 — PrivacyAlign: Contextual Privacy Alignment for LLM Agents

**问题与旧路径。** AI agents acting on behalf of users are constantly making decisions, and for users to trust their agents, those decisions must align with what they actually want. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 社会行为安全评估必须绑定场景、规范、judge 与 policy optimization，合成 reward 改善不证明真实人群规范覆盖。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21710v1 §3 Scenarios and Annotations; §4 Reward Modeling and Policy Optimization`；Evaluation=`arXiv:2606.21710v1 §5 Experiments`；counterevidence=`arXiv:2606.21710v1 §6 Limitations (unnumbered list after Conclusion): synthetic scenarios, judge dependence, human heterogeneity, scale, deployment caution, norms and dual use`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21710v1 §6 Limitations (unnumbered list after Conclusion): synthetic scenarios, judge dependence, human heterogeneity, scale, deployment caution, norms and dual use`，只支持『社会行为安全评估必须绑定场景、规范、judge 与 policy optimization，合成 reward 改善不证明真实人群规范覆盖』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21710:start -->
Primary identity `arXiv:2606.21710v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21710:end -->
<!-- review:SF-2026-ARXIV-2606-21710:end -->

<!-- review:SF-2026-ARXIV-2606-21712:start -->
### 2606.21712 — BatchGen: An Architecture for Scalable and Efficient Batch Inference

**问题与旧路径。** Batch inference has become a central mode of AI computation, yet existing inference engines still rely on execution models designed for interactive serving. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** BatchGen 用 sequence coroutine 暴露生成状态并跨请求组装 batch；scheduler 必须拥有 coroutine lifecycle、fairness 与 memory backpressure。唯一知识 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21712v1 §3 Design Intuitions; §4 Sequence Coroutine; §5 System Design`；Evaluation=`arXiv:2606.21712v1 §6 Evaluation`；counterevidence=`arXiv:2606.21712v1 §7 Limitations and Future Work`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21712v1 §7 Limitations and Future Work`，只支持『BatchGen 用 sequence coroutine 暴露生成状态并跨请求组装 batch；scheduler 必须拥有 coroutine lifecycle、fairness 与 memory backpressure』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。估计失准或 SLO slack 耗尽时停止合批/迁移，回退到隔离队列与保守 admission；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21712:start -->
Primary identity `arXiv:2606.21712v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21712:end -->
<!-- review:SF-2026-ARXIV-2606-21712:end -->

<!-- review:SF-2026-ARXIV-2606-21732:start -->
### 2606.21732 — Safe to Check, Unsafe to Use: Relinking at the Compression Boundary of LLM Agents

**问题与旧路径。** Summarization-based prompt compression is increasingly used by LLM agents to shorten long, distributed contexts, but it shifts the security boundary: filters inspect the pre-compression prompt while the backend acts on a newly generated compressed context. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 对 Agent/system 的组合攻击要显式建模 attacker capability、可见状态与 defense boundary；单点 sanitize 不等于 end-to-end containment。唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21732v1 §2 System Model; §3 Hypotheses; §4 Attack; §5 Threat; §6 Method; §8 Defense`；Evaluation=`arXiv:2606.21732v1 §7 Evaluation; Appendices A–C`；counterevidence=`arXiv:2606.21732v1 §10 Conclusion; adaptive-adversary boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21732v1 §10 Conclusion; adaptive-adversary boundary`，只支持『对 Agent/system 的组合攻击要显式建模 attacker capability、可见状态与 defense boundary；单点 sanitize 不等于 end-to-end containment』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21732:start -->
Primary identity `arXiv:2606.21732v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21732:end -->
<!-- review:SF-2026-ARXIV-2606-21732:end -->

<!-- review:SF-2026-ARXIV-2606-21775:start -->
### 2606.21775 — Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning

**问题与旧路径。** Recently, world models have emerged as a promising paradigm for building intelligent agents by learning predictive models that estimate future environment states conditioned on observations and actions. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** world-model rollout horizon 应成为按任务难度与不确定性调节的状态，而非训练/推理期固定常数。唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21775v1 §3 VLWM (variable horizon, curriculum and planning)`；Evaluation=`arXiv:2606.21775v1 §4 Planning Tasks; Appendices A–C`；counterevidence=`arXiv:2606.21775v1 §5 Conclusion and evaluated task/horizon boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21775v1 §5 Conclusion and evaluated task/horizon boundary`，只支持『world-model rollout horizon 应成为按任务难度与不确定性调节的状态，而非训练/推理期固定常数』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。identifiability、rollout uncertainty 或 horizon gate 失败时停止想象 rollout，交还真实环境观测；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21775:start -->
Primary identity `arXiv:2606.21775v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21775:end -->
<!-- review:SF-2026-ARXIV-2606-21775:end -->

<!-- review:SF-2026-ARXIV-2606-21777:start -->
### 2606.21777 — CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action and Learning in Knowledge-Intensive Tasks

**问题与旧路径。** LLM agents in knowledge intensive question answering take retrieval and reasoning actions with incomplete knowledge about whether their current answer is uncertain, unsupported, or already complete. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库。唯一知识 owner 为 `AGENT-RAG`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21777v1 §3 Calibrated Verifier Telemetry`；Evaluation=`arXiv:2606.21777v1 §4 Experiments; Appendices A–G`；counterevidence=`arXiv:2606.21777v1 §5 Conclusion and model-scale/QA scope`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21777v1 §5 Conclusion and model-scale/QA scope`，只支持『retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。evidence、index 或 verifier identity 不完整时 abstain/回到原始证据，不把生成结果写成事实；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21777:start -->
Primary identity `arXiv:2606.21777v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21777:end -->
<!-- review:SF-2026-ARXIV-2606-21777:end -->

<!-- review:SF-2026-ARXIV-2606-21787:start -->
### 2606.21787 — Towards Imputation of Pre-Trained Language Model Metadata using Semantic Fingerprinting

**问题与旧路径。** Pre-trained language models (PTLMs) hosted on platforms such as Hugging Face form complex lineage structures similar to software dependency graphs. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage。唯一知识 owner 为 `PLATFORM-MODEL-REGISTRY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21787v1 §3 Empirical Design; §5 SemFin`；Evaluation=`arXiv:2606.21787v1 §4, §6 and §7 Research Questions`；counterevidence=`arXiv:2606.21787v1 §8 Discussion and Implication`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21787v1 §8 Discussion and Implication`，只支持『模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。semantic fingerprint 冲突时禁止 promotion，以文件 hash、lineage 与部署 receipt 为准；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21787:start -->
Primary identity `arXiv:2606.21787v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21787:end -->
<!-- review:SF-2026-ARXIV-2606-21787:end -->

<!-- review:SF-2026-ARXIV-2606-21795:start -->
### 2606.21795 — Discretizing Reward Models

**问题与旧路径。** Despite their widespread use, the role of reward models in shaping reinforcement learning is poorly understood. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** reward clustering 应把异质 reward mode 分开优化并保存 cluster identity，聚合 scalar reward 会隐藏冲突偏好与 hacking。唯一知识 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21795v1 §2 Formulation; §3 Reward Clustering`；Evaluation=`arXiv:2606.21795v1 §4 Experiments; Appendices C–D`；counterevidence=`arXiv:2606.21795v1 §5 Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21795v1 §5 Limitations`，只支持『reward clustering 应把异质 reward mode 分开优化并保存 cluster identity，聚合 scalar reward 会隐藏冲突偏好与 hacking』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。reward cluster 不稳定或冲突时停止 policy update，回到独立 evaluator 与人工 adjudication；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21795:start -->
Primary identity `arXiv:2606.21795v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21795:end -->
<!-- review:SF-2026-ARXIV-2606-21795:end -->

<!-- review:SF-2026-ARXIV-2606-21803:start -->
### 2606.21803 — Test-Time Training with Next-Token Prediction

**问题与旧路径。** Next-token prediction is the self-supervised signal that trains language models, and every observed prompt token provides the same signal at test time. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** TTT-NTP 在推理时用 next-token prediction 写入 fast weights；write scope、chunk boundary 与 reset policy 必须成为 context state。唯一知识 owner 为 `MODEL-LONG-CONTEXT`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21803v1 §3 Method (TTT-NTP fast write, chunk and closed form)`；Evaluation=`arXiv:2606.21803v1 §4 Experiments; Appendices A–C`；counterevidence=`arXiv:2606.21803v1 §5 Conclusion and evaluated model/context boundary`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21803v1 §5 Conclusion and evaluated model/context boundary`，只支持『TTT-NTP 在推理时用 next-token prediction 写入 fast weights；write scope、chunk boundary 与 reset policy 必须成为 context state』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。fast-weight 写入越界或收益不稳时丢弃该请求的适配状态并回到冻结 base model；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21803:start -->
Primary identity `arXiv:2606.21803v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21803:end -->
<!-- review:SF-2026-ARXIV-2606-21803:end -->

<!-- review:SF-2026-ARXIV-2606-21804:start -->
### 2606.21804 — Is Agent Code Less Maintainable Than Human Code?

**问题与旧路径。** Maintainability is a core dimension of software engineering, shaping how code is written, reviewed, and developed over time. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** coding-Agent evaluation 应按 thread/issue 持久化多轮 context 与 side effects，单次 patch pass 会漏掉跨轮回归。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21804v1 §3 CodeThread`；Evaluation=`arXiv:2606.21804v1 §4 SWE Evaluation; §5 Analysis; Appendices A–D`；counterevidence=`arXiv:2606.21804v1 §6 Discussion and Limitations`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21804v1 §6 Discussion and Limitations`，只支持『coding-Agent evaluation 应按 thread/issue 持久化多轮 context 与 side effects，单次 patch pass 会漏掉跨轮回归』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21804:start -->
Primary identity `arXiv:2606.21804v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21804:end -->
<!-- review:SF-2026-ARXIV-2606-21804:end -->

<!-- review:SF-2026-ARXIV-2606-21807:start -->
### 2606.21807 — Fixed RAG Compression Collapses Measured Reader Scaling

**问题与旧路径。** Retrieval-Augmented Generation (RAG) compression papers often evaluate a compressor on one to three readers and treat the compressed evidence layer as evaluation-neutral. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** 规模变化会同时提高能力与稳定错误；evaluation 必须用 slice 与 uncertainty 分解 opposing forces 而非只报告均值。唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21807v1 §3 Two Opposing Forces`；Evaluation=`arXiv:2606.21807v1 §4 Setup; §5 Results; Appendices A–I`；counterevidence=`arXiv:2606.21807v1 §6 Analysis and Discussion; §7 Conclusion`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21807v1 §6 Analysis and Discussion; §7 Conclusion`，只支持『规模变化会同时提高能力与稳定错误；evaluation 必须用 slice 与 uncertainty 分解 opposing forces 而非只报告均值』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21807:start -->
Primary identity `arXiv:2606.21807v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21807:end -->
<!-- review:SF-2026-ARXIV-2606-21807:end -->

<!-- review:SF-2026-ARXIV-2606-21811:start -->
### 2606.21811 — Steer, Don't Solve: Training Small Critic Models for Large Code Agents

**问题与旧路径。** End-to-end code agent training is resource-intensive and plateaus on the strategy-level reasoning needed to resolve code issues, since jointly optimizing code-level execution and strategy-level reasoning leaves the latter underdeveloped. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** critic-based self-improvement 要分离 critique quality、policy uptake 与最终 outcome，强 critic 也不证明 actor 会正确使用反馈。唯一知识 owner 为 `AGENT-REFLECTION`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.21811v1 §3 Methodology (critic models, critique and training)`；Evaluation=`arXiv:2606.21811v1 §4 Setup; §5 Results; Appendices D–G`；counterevidence=`arXiv:2606.21811v1 §6 Discussion; Appendices E and G.4 fall-short cases`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.21811v1 §6 Discussion; Appendices E and G.4 fall-short cases`，只支持『critic-based self-improvement 要分离 critique quality、policy uptake 与最终 outcome，强 critic 也不证明 actor 会正确使用反馈』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。held-out 验证失败时拒绝 promotion，保留旧 skill/policy 与 candidate lesson 的分离状态；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-21811:start -->
Primary identity `arXiv:2606.21811v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-21811:end -->
<!-- review:SF-2026-ARXIV-2606-21811:end -->

<!-- review:SF-2026-ARXIV-2606-28376:start -->
### 2606.28376 — When Does Overlap Help? OSU-Mem and a Cell-Conditional Analysis of Trajectory Memory for LLM Agents

**问题与旧路径。** Long-horizon large language model (LLM) agents accumulate interaction trajectories that quickly exceed any practical prompt budget, and existing memory methods either truncate aggressively and lose non-local evidence or retain boilerplate that degrades decision quality. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** OSU-Mem 将 observation、summary 与 update 分阶段持久化，并要求在多步任务中分别验证 construction、retrieval 与 action use。唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.28376v1 §3 OSU-Mem; §4 Theory`；Evaluation=`arXiv:2606.28376v1 §5 Settings; §6 Results; Appendices B–J`；counterevidence=`arXiv:2606.28376v1 §7 Limitations; Appendix F no multi-step rollout note`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.28376v1 §7 Limitations; Appendix F no multi-step rollout note`，只支持『OSU-Mem 将 observation、summary 与 update 分阶段持久化，并要求在多步任务中分别验证 construction、retrieval 与 action use』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。写入、检索或来源证据不足时 hold/隔离 candidate memory，保留原始轨迹并禁止自动覆盖；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-28376:start -->
Primary identity `arXiv:2606.28376v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-28376:end -->
<!-- review:SF-2026-ARXIV-2606-28376:end -->

<!-- review:SF-2026-ARXIV-2606-28379:start -->
### 2606.28379 — LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval

**问题与旧路径。** We introduce LEDGER to tackle the novel context engineering challenge of agentic document editing, where localized edits to long, structured documents must be applied efficiently without breaking cross-references or semantic consistency. 旧路径在输入分布、信任边界与运行预算稳定时仍合理。

**机制与 state/data/control owner。** LEDGER 用显式 dependency graph 组织长期任务状态，retrieval 与 consistency repair 必须围绕同一 node/version identity。唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.28379v1 §3 LEDGER (graph, retrieval and consistency)`；Evaluation=`arXiv:2606.28379v1 §4 Experiments; Appendices C–E`；counterevidence=`arXiv:2606.28379v1 §5 Conclusion and absence of a formal semantic guarantee`。这些证据证明 exact-v1 披露范围内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据边界是 `arXiv:2606.28379v1 §5 Conclusion and absence of a formal semantic guarantee`，只支持『LEDGER 用显式 dependency graph 组织长期任务状态，retrieval 与 consistency repair 必须围绕同一 node/version identity』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-28379:start -->
Primary identity `arXiv:2606.28379v1`; access route `accessible_official_exact_v1_html`; ordinary pending=`0`.
<!-- claim:SF-2026-ARXIV-2606-28379:end -->
<!-- review:SF-2026-ARXIV-2606-28379:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21023 | MCR-Bench mission-critical reproducibility plus MedQA kernel-error study | Qwen3-8B/14B/32B; Llama-3.1-8B-Instruct; DeepSeek-R1-Distill-Qwen-14B | NVIDIA H100 FP32 ground truth; NVIDIA A100 SASS profiling; heterogeneous GPU evaluation | FP32, BF16, FP16 and INT16 HEAL paths | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | functional answer reproducibility under greedy decode | answer flip rate, final-hidden MSE, exact reproducibility and TPOT overhead |
| SF-2026-ARXIV-2606-21024 | Negative Knowledge as Failure-aware Shared Memory for AutoResearch | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate this layer in two settings: same-task retry on ScienceAgentBench and cross-task scientific research on two nonlinear math-physics PDE problems. |
| SF-2026-ARXIV-2606-21037 | 174 identical Honeyquest reconnaissance queries; 10,962 model responses versus 47 humans | 21 LLMs from 10 providers, 8B to over 1T parameters | Not Disclosed | Not Disclosed | 174 reconnaissance-query set | reasoning plus exploit decision | Not Disclosed | Not Disclosed | Not Disclosed | fell-for-trap rate, attention-diversion effect and recognition-action gap with significance tests |
| SF-2026-ARXIV-2606-21045 | OVIG: Optimistic Verification of AI Training Integrity via Gradient Signals | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On Qwen3, increasing the stride from $s=1$ to $s=2000$ reduces off-chain storage and evidence transmission by $1996\times$ while preserving $0\%$ ASR; at this setting, OVIG incurs only $1.143\times$ total system overhead relative to training without verification. |
| SF-2026-ARXIV-2606-21071 | Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing research characterizes the landscape through prompt injection, malicious skills, marketplace risks, or black-box evaluation of agents. |
| SF-2026-ARXIV-2606-21077 | OTTER: A Red-Teaming System for Toxicity-Evading Jailbreak Prompt Optimization | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We show this assumption is fundamentally brittle: surface toxicity and adversarial intent can be decoupled by replacing as few as five tokens. |
| SF-2026-ARXIV-2606-21083 | 204 FOLIO examples plus LogiQA v2 transfer | four open-weight LLMs from 1B to 3B, including Qwen2.5-3B and TinyLlama-1.1B | Not Disclosed | normalized YES/NO log probabilities | Not Disclosed | 3-way True/False/Uncertain decision | Not Disclosed | Not Disclosed | Not Disclosed | negation violation, commitment mass, coverage and coherence-commitment frontier |
| SF-2026-ARXIV-2606-21088 | MV-WAM: Manifold-Aware World Action Model with Value Augmentation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Achieving robust and generalizable manipulation across diverse environments remains a fundamental challenge in embodied robotics. |
| SF-2026-ARXIV-2606-21101 | Avazu and Criteo recommendation inference with DCN/DCNv2/Wide&Deep/DeepFM | DCN, DCNv2, Wide&Deep and DeepFM | Not Disclosed | Not Disclosed | Not Disclosed | recommendation score | 2048; sensitivity through 16384 and above | multi-stream scheduling | latency/throughput operating points | AUC, LogLoss, speedup, latency and GPU utilization |
| SF-2026-ARXIV-2606-21121 | controlled SSNHL and conductive-condition protocol benchmark | Not Disclosed | NVIDIA RTX PRO 6000 Blackwell, approximately 96 GB | Not Disclosed | Not Disclosed | protocol-constrained clinical decision trajectory | Not Disclosed | Not Disclosed | Not Disclosed | condition-specific protocol compliance, adherence and balanced accuracy |
| SF-2026-ARXIV-2606-21126 | ResMLP evaluation-instability audit on CIFAR-10 and CIFAR-100 | ResMLP variants | Not Disclosed | Not Disclosed | image classification samples | class prediction and aggregate metrics | 128 | Not Disclosed | Not Disclosed | ranking stability, variance and failure-mode sensitivity over three seeds |
| SF-2026-ARXIV-2606-21129 | AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | At the implementation level, we introduce a four-layer architecture -- Ghost Kernel, Logic Shutter, Agent Capsule, and Semantic Boundary Gateway -- together with the Intent ABI, Manifest-Only Runtime, Weaver-based capability generation, and an admission model for AgenticOS-native Skills. |
| SF-2026-ARXIV-2606-21130 | telemetry-window surge injection and detection | XGBoost detector | Not Disclosed | Not Disclosed | multi-window service telemetry | surge/anomaly decision | Not Disclosed | Not Disclosed | detection delay and false-alarm operating point | ROC AUC, average precision, recall and false-alarm rate |
| SF-2026-ARXIV-2606-21140 | Matching Matters: A Fair Quality-Efficiency Benchmark for Command-Line Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Rapid advances in large language models have improved the task-solving capabilities of command-line-interface (CLI)-based agents, whose CLIs determine how models invoke tools, maintain interaction history, and recover from failures. |
| SF-2026-ARXIV-2606-21144 | AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across two extraction models and two feedback modes, AdaMem improves QA accuracy by up to \textbf{+9.0\%} over the uniform Mem0 baseline while shrinking memory volume by \textbf{9\%}. |
| SF-2026-ARXIV-2606-21172 | video/world-model backdoor poisoning with poison-rate audit | VaViM | 8 GPUs, type Not Disclosed | Not Disclosed | Not Disclosed | video/world-model prediction | 4 per GPU with gradient accumulation 2; effective batch 64 | 8-GPU training | Not Disclosed | clean utility, attack success, trigger persistence and poison-rate sensitivity |
| SF-2026-ARXIV-2606-21173 | Reacher, MountainCar and FourRooms sparse-goal transition recovery | PQN agent and learned P-model | NVIDIA H100 in author repository reproduction instructions | Not Disclosed | 512 reset episodes in reported Reacher setup | transition/value estimates | Not Disclosed | Not Disclosed | Not Disclosed | goal-reaching performance and transition recovery across 10 seeds |
| SF-2026-ARXIV-2606-21188 | Remember what you did?: Learning Behavioral Memories for Partially Observable Object Manipulation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate CAMP across four real-robot setups and two novel simulation benchmarks: Memory-T-Bench and Memory-Manip-Bench. |
| SF-2026-ARXIV-2606-21228 | Sakana Fugu Technical Report | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Through these adaptive scaffolds, Fugu accesses performance beyond any individual LLM agent, achieving state-of-the-art results compared to other publicly accessible models across a range of challenging tasks, including SWE-Bench Pro, Terminal Bench, LiveCodeBench, GPQA-Diamond, Humanity's Last Exam, and CharXiv Reasoning. |
| SF-2026-ARXIV-2606-21238 | Recency/Frequency Adaptive KV Caching for Large Language Model Serving | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Evaluations show that it improves the KV cache hit rate by up to 10.8% and reduces time to first token by up to 12.6% over naive vLLM on synthetic document question answering workloads, and 2.1% and 2.0% respectively on real-world conversation workloads. |
| SF-2026-ARXIV-2606-21249 | Does RoPE Prevent or Degrade Retrieval Heads? A Mechanistic Analysis Across Model Families | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | (ii) Higher theta does not reduce retrieval-head count (LLaMA-3.1 at theta=500K has 47 heads vs LLaMA-2 at theta=10K with 42), refuting the prevention hypothesis. |
| SF-2026-ARXIV-2606-21255 | SCOPE: Sequential Conformal Probing for Reliable OOD Rejection in LLM Services | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | In this paper, we introduce SCOPE (Sequential Conformal OOD Probing and Evaluation), a framework that selects a readable hidden layer, constructs a conformal gate with IND calibration, and uses a supermartingale e-process to certify persistent service-boundary evidence. |
| SF-2026-ARXIV-2606-21257 | OpenPangu 1B/7B PTQ task evaluation | OpenPangu 1B and 7B | Ascend 910B1 NPU | W8 and W4 weight-only plus weight-activation quantization variants | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task quality, quantization error and deployment performance |
| SF-2026-ARXIV-2606-21262 | ARCO: Adaptive Rubrics with Co-Evolution for Multi-Step LLM-Based Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Rubric-based rewards improve interpretability through natural-language criteria, but existing methods share two limitations: they score at the trajectory level, offering no guidance for individual steps; and their scorer is closed-source and static, so it cannot adapt as the agent evolves during training. |
| SF-2026-ARXIV-2606-21282 | Law, LHC and HAR global-robustness verification benchmarks | feed-forward DNNs up to 500 ReLUs / six layers of 50 units in reported scope | Not Disclosed | Not Disclosed | up to 561 input dimensions in reported scope | verified/unknown robustness result | Not Disclosed | Not Disclosed | Not Disclosed | verification precision, solved instances, runtime and scalability versus prior analyzers |
| SF-2026-ARXIV-2606-21307 | Task-Differentiated Atomic Skill Expansion and Routing for Continual Learning Across Highly Heterogeneous Tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Experiments on \texttt{HeteroCLBench} show that \texttt{TASER} consistently outperforms strong baselines by improving plasticity and reducing catastrophic forgetting. |
| SF-2026-ARXIV-2606-21315 | Social World Model for Lifelong Social Intelligence | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Social intelligence is a core competency for language agents, yet current research primarily focuses on static capability evaluation rather than how these skills are continuously shaped and accumulated. |
| SF-2026-ARXIV-2606-21337 | DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Github: https://github.com/vancyland/DataClaw0 |
| SF-2026-ARXIV-2606-21338 | "What Happens Locally, Leaks Globally": Detecting Privacy Leakage Risks in MCP Servers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Case studies confirm concrete exposures including leaked Bearer tokens, propagated API keys, and plaintext authentication credentials, arguing for systematic, protocol-aware safeguards in the emerging LLM agent toolchain. |
| SF-2026-ARXIV-2606-21359 | Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Prior hallucination evaluation work remains largely restricted to the biomedical domain, treats hallucination as a binary task, and has not examined the growing family of scientifically fine-tuned LLMs. |
| SF-2026-ARXIV-2606-21372 | NAC: Neural Action Codec for Vision-Language-Action Models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across LIBERO-10, RoboMimic, and a suite of real-world manipulation tasks, NAC achieves lower reconstruction error and higher success rates than binning, FAST, and prior VQ-based tokenizers at comparable or better compression rates. |
| SF-2026-ARXIV-2606-21386 | VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Vision-language-action models (VLAs) achieve state-of-the-art performance on many robotic manipulation tasks, yet they can still behave unpredictably in out-of-distribution scenarios. |
| SF-2026-ARXIV-2606-21389 | 37 MITRE ATT&CK-mapped HIKARI challenges and 200 SOCpilot incidents | LLM SOC action traces plus deterministic verifier | Not Disclosed | Not Disclosed | production SIEM event sequences after anonymization | training artifact or compliance finding | Not Disclosed | Not Disclosed | Not Disclosed | temporal/entity consistency, task usability and deterministic non-compliance detection |
| SF-2026-ARXIV-2606-21398 | BIT-Nav: Brain-Inspired Trajectory Memory for Embodied Navigation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | As episodes extend, this selection grows increasingly sparse, yet prior work shows no accuracy gain when scaling from 8 to 64 frames, suggesting the bottleneck is not frame quantity but the representation itself. |
| SF-2026-ARXIV-2606-21399 | Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The relevant question is not how likely the agent is to fail if it continues, but whether an available intervention would improve the outcome. |
| SF-2026-ARXIV-2606-21401 | SwarmX: Agentic Scheduling for Low-Latency Agentic Systems | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate SwarmX using production deployment (nearly one thousand GPUs and one million CPU cores) and controlled experiments on a 128-GPU testbed. |
| SF-2026-ARXIV-2606-21406 | Robot Self-Improvement via Human-Video Dynamics Models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Human videos provide the first of these in abundance, and prior work has shown they can initialize useful policies. |
| SF-2026-ARXIV-2606-21409 | Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Tool-augmented agents are typically evaluated by their gains under reliable external feedback. |
| SF-2026-ARXIV-2606-21428 | Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Patching llama$.$cpp to time the decode graph node-by-node shows routing accounts for under 9% of MoE-block compute on the cleaner edge backend, so the gap reflects total-parameter memory footprint, expert dispatch, and KV-cache pressure rather than routing. |
| SF-2026-ARXIV-2606-21445 | AutoRAS: Learning Robust Agentic Systems with Primitive Representations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Extensive experiments show that AutoRAS achieves the best performance in both vanilla and adversarial settings, with the smallest performance degradation under attacks. |
| SF-2026-ARXIV-2606-21509 | A Stitch in Time Saves Nine: Preserving Policy Compatibility Under Perception Updates in End-to-End Autonomous Driving | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | These results suggest that model stitching provides an effective and computationally efficient alternative to retraining or fine-tuning for maintaining end-to-end autonomous driving systems. |
| SF-2026-ARXIV-2606-21514 | Towards Understanding the Power and Limits of the Muon Optimizer: A River-Valley Perspective | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Recently, Muon has gained substantial attention as an appealing alternative to Adam-like optimizers, with many works highlighting its advantages through spectral normalization and improved conditioning. |
| SF-2026-ARXIV-2606-21553 | 5,000 HotpotQA examples | Qwen2.5-7B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | multi-hop QA answer | Not Disclosed | Not Disclosed | Not Disclosed | answer quality, retrieval quality and system-level ablations |
| SF-2026-ARXIV-2606-21565 | Composing Verifiable Conceptual Models via Building Blocks: Towards Design-Time Verification of Agentic AI Workflows | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We implemented these rules in a software prototype and evaluated them using two openly released datasets: 48 workflows with known design flaws and 168 variants that preserve workflow logic but alter graph structure. |
| SF-2026-ARXIV-2606-21572 | Robot Critics that Sweat the Small Stuff | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our fine-tuned critic excels at fine-grained progress reasoning and subtle failure detection, outperforming prior progress reasoning baselines. |
| SF-2026-ARXIV-2606-21584 | ASVspoof 2019 LA to In-the-Wild and ASVspoof 2021 DF threshold transfer | frozen SSL-AASIST detector | Not Disclosed | Not Disclosed | speech utterances in three corpora | bona-fide/spoof score | Not Disclosed | Not Disclosed | threshold fixed before unlabeled target deployment | EER, transferred-threshold HTER and bona-fide rejection under seven corrections |
| SF-2026-ARXIV-2606-21627 | Counsel: A Meta-Evaluation Dataset for Agentic Tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | As agentic systems tackle increasingly complex multi-step tasks, evaluating their trajectories presents a major bottleneck - human annotation of a single trajectory on popular agentic benchmarks can take hours, making it difficult to scale evaluations for measuring performance or curating training data. |
| SF-2026-ARXIV-2606-21633 | HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Recent sparse block dLLM methods have shown that sparse inference separates into a selection phase that scans the full KV cache once per block and a denoising phase that reuses the selected small subset T times. |
| SF-2026-ARXIV-2606-21638 | Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Moreover, we show that our approach extends naturally to multiple hierarchical tiers. |
| SF-2026-ARXIV-2606-21654 | ChainWorld: Composing Long-Horizon Desktop Workloads from Atomic OSWorld Tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Computer use agents are evaluated almost exclusively on atomic desktop tasks, but realistic desktop work requires sustaining state across multiple objectives. |
| SF-2026-ARXIV-2606-21666 | Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate SSVP across two domains (multi-agent travel and software project planning) using Claude Haiku. |
| SF-2026-ARXIV-2606-21678 | Decodable but Not Faithful: Coupling Natural-Language Rationales to Programmatic Verifiers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | In LeanCheck (formal theorem proving), rationale-only and proof-only pooling achieve perfect directional separation under counterfactual conflict. |
| SF-2026-ARXIV-2606-21710 | PrivacyAlign: Contextual Privacy Alignment for LLM Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | While existing work relies on unreliable proxies for both training and evaluation, we place human judgment at the center of agentic privacy alignment. |
| SF-2026-ARXIV-2606-21712 | large-scale sequence generation through sequence coroutines | Not Disclosed | 128-GPU cluster, GPU type Not Disclosed | Not Disclosed | Not Disclosed | millions of generated sequences | dynamic coroutine batching | 128 GPUs | throughput and latency targets reported by workload | throughput, utilization, latency, fairness and scaling |
| SF-2026-ARXIV-2606-21732 | Safe to Check, Unsafe to Use: Relinking at the Compression Boundary of LLM Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We show that relinking arises from summarization itself: attention makes separated fragments jointly available, pre-training makes compatible fragments plausible to connect, and post-training favors compact backend-actionable summaries. |
| SF-2026-ARXIV-2606-21775 | Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Instead of training only on one-step transitions, VLWMs directly model temporally extended dynamics, allowing the same predictor to evaluate action plans over different horizons. |
| SF-2026-ARXIV-2606-21777 | CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action and Learning in Knowledge-Intensive Tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This produces two failure modes: committing to confident but unsupported answers, which hurts accuracy, and over-retrieving when the evidence in hand already suffices, resulting in wasted compute. |
| SF-2026-ARXIV-2606-21787 | Towards Imputation of Pre-Trained Language Model Metadata using Semantic Fingerprinting | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate SemFin on a large-scale dataset of 317,133 PTLMs. |
| SF-2026-ARXIV-2606-21795 | Discretizing Reward Models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | However, we show this apparent strength is a serious weakness: many popular reward models are oversensitive, assigning different scores to equally good responses. |
| SF-2026-ARXIV-2606-21803 | RULER at 4K, 8K, 16K and 32K context | Llama-3.1-8B, Mistral-7B-v0.3, Qwen3-4B and Qwen3-0.6B | Not Disclosed | Not Disclosed | 4K/8K/16K/32K | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | RULER accuracy, adaptation quality, compute and ablations |
| SF-2026-ARXIV-2606-21804 | Is Agent Code Less Maintainable Than Human Code? | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Regression analysis reveals that many traditional software engineering maintainability metrics do not explain this difference. |
| SF-2026-ARXIV-2606-21807 | Fixed RAG Compression Collapses Measured Reader Scaling | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Retrieval-Augmented Generation (RAG) compression papers often evaluate a compressor on one to three readers and treat the compressed evidence layer as evaluation-neutral. |
| SF-2026-ARXIV-2606-21811 | SWE-bench Verified critic and actor evaluation | CWM-32B, Qwen3-Next-80B-A3B, Qwen3-32B and 8B critics | Not Disclosed | Not Disclosed | repository issue plus trajectory | critique and code patch | Not Disclosed | Not Disclosed | Not Disclosed | critic accuracy, policy uptake, SWE-bench resolution and inference cost |
| SF-2026-ARXIV-2606-28376 | When Does Overlap Help? OSU-Mem and a Cell-Conditional Analysis of Trajectory Memory for LLM Agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We instantiate this in OSU-Mem, which retrieves from an overlapping OSU pool via budgeted coarse-to-fine expansion, and show its benefit is conditional: overlapping memory helps when the evidence steps a query needs share tool calls or entities, but hurts when those steps are fully heterogeneous and share neither. |
| SF-2026-ARXIV-2606-28379 | LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate LEDGER on a curated benchmark of 1.9k test cases with various document types and lengths, spanning six state-of-the-art models: LEDGER improves consistency from 56% to 76% across all six models and test scenarios while reducing token usage. |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21023 | score_7_9; potential_books_delta | selected | DA-20260620-REPRODUCIBLE-INFERENCE | — | 入选：它连接 kernel 数值误差、KV/GEMM 精度路径、异构硬件复现性与 TPOT/memory 代价，是本日最强 inference-state 机制链。 | analysis:DA-20260620-REPRODUCIBLE-INFERENCE |
| SF-2026-ARXIV-2606-21024 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-MEMORY` 的『失败经验应以带 task、attempt、failure mode、diagnosis 与 prevention 的 negative-knowledge record 写入共享 memory，并在后续尝试前检索而非覆盖成功轨迹』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21024 |
| SF-2026-ARXIV-2606-21037 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『LLM attacker 与人类 attacker 的 deception response 不同，security evaluation 必须把 attacker class、trap recognition 与实际 exploit action 分开记录』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21037 |
| SF-2026-ARXIV-2606-21045 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『训练完整性可以由连续 gradient-signal challenge 做 optimistic verification，但 verifier 必须拥有 challenge identity、容忍区间与失败升级路径』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21045 |
| SF-2026-ARXIV-2606-21071 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『Agent vulnerability audit 必须覆盖 activation 后的 runtime data/control flow，静态 skill 文本与 manifest 不能代表组合执行安全』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21071 |
| SF-2026-ARXIV-2606-21077 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『黑盒 Agent red-team 可用可迁移 observation/action perturbation 搜索 failure trajectory，但 attack generator 不能取得生产执行权』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21077 |
| SF-2026-ARXIV-2606-21083 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『逻辑一致性指标必须与 commitment/coverage 联合报告，否则系统性 abstention 会被误判为高 coherence』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21083 |
| SF-2026-ARXIV-2606-21088 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21088 |
| SF-2026-ARXIV-2606-21101 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `INFER-SCHEDULING` 的『推荐模型推理的 stream scheduler 应按 embedding、interaction 与 dense 阶段的资源轮廓编排，而不是只按请求 FIFO』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21101 |
| SF-2026-ARXIV-2606-21121 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『协议约束任务可以在 autoregressive trajectory 上做局部规则编辑；rule coverage、trigger telemetry 与 rollback 必须成为 runtime state』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21121 |
| SF-2026-ARXIV-2606-21126 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『评估协议需要同时暴露统计不稳定、metric gaming、prompt sensitivity 与 ranking reversal，单一 aggregate score 不能拥有 release authority』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21126 |
| SF-2026-ARXIV-2606-21129 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『Intent ABI 应把用户意图、capability grant 与 effect-time authorization 编译成可验证接口，而不是把自然语言意图直接当权限』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21129 |
| SF-2026-ARXIV-2606-21130 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-MONITORING` 的『GPU/AI 服务的异常浪涌要由多窗口 telemetry 与显式阈值选择检测，并把 recall、false alarm 与 detection delay 一起交给 operator』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21130 |
| SF-2026-ARXIV-2606-21140 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『Agent benchmark 应把 token、tool call、retry 与 wall-clock 成本纳入同一 token-economic contract，成功率不是资源效率』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21140 |
| SF-2026-ARXIV-2606-21144 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-MEMORY` 的『Adaptive memory 应按 task evidence 选择写入、压缩与检索路径，并把 policy state 与事实 state 分离』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21144 |
| SF-2026-ARXIV-2606-21172 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『video/world-model poisoning 需要按 poison rate、trigger persistence 与 downstream action effect 验收，干净集精度不能覆盖后门风险』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21172 |
| SF-2026-ARXIV-2606-21173 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-WORLD-MODELS` 的『从 sparse-goal demonstrations 反演 transition dynamics 需要把 reward/goal condition、Bellman identifiability 与 learned transition 分开，恢复条件不是任意环境真值』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21173 |
| SF-2026-ARXIV-2606-21188 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA 可先离散化长期 episodic memory 并预训练 action head，但 memory code、policy state 与真实机器人 observation identity 必须联结』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21188 |
| SF-2026-ARXIV-2606-21228 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-MULTI-AGENT` 的『多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21228 |
| SF-2026-ARXIV-2606-21238 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `INFER-KV-CACHE` 的『KV cache 可按对话、batch 与访问热度自适应分区；partition version、迁移成本与 miss fallback 必须进入 cache control state』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21238 |
| SF-2026-ARXIV-2606-21249 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MODEL-POSITION-ENCODING` 的『位置表示的训练动力学需要区分静态相关、训练演化与因果消融，最终 probe 相似度不能证明模型真的使用该位置通道』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21249 |
| SF-2026-ARXIV-2606-21255 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『uncertainty gate 只有经 calibration 与 certifying boundary 后才能影响 release；置信度本身不是安全证明』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21255 |
| SF-2026-ARXIV-2606-21257 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `INFER-GPU-MEMORY` 的『端侧大模型 PTQ 必须把 weight/activation bit-width、算子支持与任务退化一起验收，压缩比不能代表可部署性』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21257 |
| SF-2026-ARXIV-2606-21262 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『rubric 与 candidate co-evolution 必须隔离生成、judge 与 held-out adjudication，避免 evaluator 随被测对象共同漂移』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21262 |
| SF-2026-ARXIV-2606-21282 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『DNN global robustness 是输入对的 2-safety property；differential halo zonotope 联合传播两条执行并界定 divergence，而非重复 local ball 检查』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21282 |
| SF-2026-ARXIV-2606-21307 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-REFLECTION` 的『skill expansion 应先检测能力缺口、生成 candidate skill、独立验证再路由，单次成功不能直接提升为长期 skill』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21307 |
| SF-2026-ARXIV-2606-21315 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-WORLD-MODELS` 的『Social World Model 要把多主体状态、关系变化与 action-conditioned transition 分层，并用 wake/sleep/deploy gates 限制自更新』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21315 |
| SF-2026-ARXIV-2606-21337 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `TRAIN-DATA` 的『训练数据 pipeline 应将任务生成、过滤、difficulty routing 与训练后 validation 绑定同一 lineage，synthetic volume 不是质量证明』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21337 |
| SF-2026-ARXIV-2606-21338 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21338 |
| SF-2026-ARXIV-2606-21359 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『hallucination benchmark 应绑定 evidence source、错误 taxonomy 与 human validation，自动 judge 分数不能替代 claim-level provenance』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21359 |
| SF-2026-ARXIV-2606-21372 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『neural action codec 把连续控制压缩成离散 token 时，codebook identity、重构误差与 policy action head 必须作为同一部署 artifact』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21372 |
| SF-2026-ARXIV-2606-21386 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA failure benchmark 应分别标注 perception、reasoning 与 action failure，并保留 intervention/fallback 可执行证据』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21386 |
| SF-2026-ARXIV-2606-21389 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『生产 SIEM telemetry 转研究 artifact 时必须保留时间与 entity consistency，同时声明 anonymization 的 privacy-utility boundary 而非声称形式匿名』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21389 |
| SF-2026-ARXIV-2606-21398 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『具身表征与动作 token 的对齐可由对比目标训练，但 representation gain 必须落到控制任务与 failure slice，而非只看 embedding quality』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21398 |
| SF-2026-ARXIV-2606-21399 | score_7_9; potential_books_delta | selected | DA-20260620-CALIBRATION-CONTROL | — | 入选：它直接否定把 observational calibration 当 control authority，并用 action-conditioned branching 给出 Agent 平台的状态/控制分界。 | analysis:DA-20260620-CALIBRATION-CONTROL |
| SF-2026-ARXIV-2606-21401 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `INFER-SCHEDULING` 的『大规模 Agent swarm 的调度对象是带依赖和状态的 task graph，placement、重试与资源隔离要由平台而非 coordinator prompt 持有』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21401 |
| SF-2026-ARXIV-2606-21406 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA 自改进必须把 data collection、critic signal 与 policy update 版本化，并在真实动作前保留 independent safety gate』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21406 |
| SF-2026-ARXIV-2606-21409 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-TOOL-CALLING` 的『tool-call repair 不能只改最终格式；应反演失败调用的 constraint、局部修补 argument 并在有限重试后回退』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21409 |
| SF-2026-ARXIV-2606-21428 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `INFER-GPU-MEMORY` 的『端侧 LLM benchmark 必须绑定具体模型、backend、硬件、prompt 与测量口径，峰值内存或 tokens/s 不能跨设备直接外推』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21428 |
| SF-2026-ARXIV-2606-21445 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『Agent workflow robustness 应把 primitive sequence、state transition 与 recovery branch 显式化，最终成功会掩盖脆弱中间路径』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21445 |
| SF-2026-ARXIV-2606-21509 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『异构 VLA 模块 stitching 需要显式 sensor/action interface 与 latency budget，子模型可互换不代表闭环状态连续』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21509 |
| SF-2026-ARXIV-2606-21514 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `TRAIN-PRETRAINING` 的『深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21514 |
| SF-2026-ARXIV-2606-21553 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-RAG` 的『RAG 系统需要联合检索、生成与证据评估，HotpotQA 上的答案提升不能单独证明索引 freshness 或生产一致性』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21553 |
| SF-2026-ARXIV-2606-21565 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『Agent-based simulation 的角色、规则、environment transition 与 observation 必须成为可重放 artifact，而非仅保存在 prompt 叙述中』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21565 |
| SF-2026-ARXIV-2606-21572 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA critic 要先在 failure evidence 上独立训练，再以受限 signal 进入 policy update；critic score 不能拥有物理提交权』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21572 |
| SF-2026-ARXIV-2606-21584 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『deployment threshold 必须从开发集冻结并在目标分布报告 HTER；test-set oracle EER 会隐藏真实 false-reject/false-accept failure』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21584 |
| SF-2026-ARXIV-2606-21627 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『trajectory preference evaluation 应保存环境、轨迹、judge 与 human disagreement，pairwise label 不是脱离 policy 的稳定真值』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21627 |
| SF-2026-ARXIV-2606-21633 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `INFER-KV-CACHE` 的『长上下文 retrieval 可把 cold state 分层到 CPU 并用 GPU kernel 协同读取，但 index/cache identity 与传输重叠决定真实收益』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21633 |
| SF-2026-ARXIV-2606-21638 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『tiered language-model service 应按 capability/risk 分离模型与权限；成本路由不能让弱安全模型获得强 effect authority』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21638 |
| SF-2026-ARXIV-2606-21654 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『compositional evaluation 应保存组件、组合、judge 与 failure attribution，组合总分不能定位哪个 handoff 失效』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21654 |
| SF-2026-ARXIV-2606-21666 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-MULTI-AGENT` 的『多 Agent 共识要保存独立 evidence、divergence 与 shared verification；重复采样的多数票不等于独立证明』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21666 |
| SF-2026-ARXIV-2606-21678 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『从 internal representation 可解码出答案不证明 reasoning faithful；diagnostic ladder 要区分 decodability、causal use 与输出行为』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21678 |
| SF-2026-ARXIV-2606-21710 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『社会行为安全评估必须绑定场景、规范、judge 与 policy optimization，合成 reward 改善不证明真实人群规范覆盖』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21710 |
| SF-2026-ARXIV-2606-21712 | score_7_9; potential_books_delta | selected | DA-20260620-SEQUENCE-COROUTINE | — | 入选：它把每条生成序列暴露为 coroutine state，改变 batching、fairness、memory backpressure 与集群 scheduler 的共同抽象。 | analysis:DA-20260620-SEQUENCE-COROUTINE |
| SF-2026-ARXIV-2606-21732 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『对 Agent/system 的组合攻击要显式建模 attacker capability、可见状态与 defense boundary；单点 sanitize 不等于 end-to-end containment』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21732 |
| SF-2026-ARXIV-2606-21775 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MULTIMODAL-WORLD-MODELS` 的『world-model rollout horizon 应成为按任务难度与不确定性调节的状态，而非训练/推理期固定常数』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21775 |
| SF-2026-ARXIV-2606-21777 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-RAG` 的『retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21777 |
| SF-2026-ARXIV-2606-21787 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-MODEL-REGISTRY` 的『模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21787 |
| SF-2026-ARXIV-2606-21795 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `TRAIN-RLHF` 的『reward clustering 应把异质 reward mode 分开优化并保存 cluster identity，聚合 scalar reward 会隐藏冲突偏好与 hacking』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21795 |
| SF-2026-ARXIV-2606-21803 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `MODEL-LONG-CONTEXT` 的『TTT-NTP 在推理时用 next-token prediction 写入 fast weights；write scope、chunk boundary 与 reset policy 必须成为 context state』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21803 |
| SF-2026-ARXIV-2606-21804 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『coding-Agent evaluation 应按 thread/issue 持久化多轮 context 与 side effects，单次 patch pass 会漏掉跨轮回归』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21804 |
| SF-2026-ARXIV-2606-21807 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『规模变化会同时提高能力与稳定错误；evaluation 必须用 slice 与 uncertainty 分解 opposing forces 而非只报告均值』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21807 |
| SF-2026-ARXIV-2606-21811 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-REFLECTION` 的『critic-based self-improvement 要分离 critique quality、policy uptake 与最终 outcome，强 critic 也不证明 actor 会正确使用反馈』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-21811 |
| SF-2026-ARXIV-2606-28376 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-MEMORY` 的『OSU-Mem 将 observation、summary 与 update 分阶段持久化，并要求在多步任务中分别验证 construction、retrieval 与 action use』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-28376 |
| SF-2026-ARXIV-2606-28379 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『LEDGER 用显式 dependency graph 组织长期任务状态，retrieval 与 consistency repair 必须围绕同一 node/version identity』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。 | analysis-decision:SF-2026-ARXIV-2606-28379 |

<!-- analysis-decision:SF-2026-ARXIV-2606-21024:start -->
未入选：完整 frontier 仍保留 `AGENT-MEMORY` 的『失败经验应以带 task、attempt、failure mode、diagnosis 与 prevention 的 negative-knowledge record 写入共享 memory，并在后续尝试前检索而非覆盖成功轨迹』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21024:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21037:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『LLM attacker 与人类 attacker 的 deception response 不同，security evaluation 必须把 attacker class、trap recognition 与实际 exploit action 分开记录』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21037:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21045:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『训练完整性可以由连续 gradient-signal challenge 做 optimistic verification，但 verifier 必须拥有 challenge identity、容忍区间与失败升级路径』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21045:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21071:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『Agent vulnerability audit 必须覆盖 activation 后的 runtime data/control flow，静态 skill 文本与 manifest 不能代表组合执行安全』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21071:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21077:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『黑盒 Agent red-team 可用可迁移 observation/action perturbation 搜索 failure trajectory，但 attack generator 不能取得生产执行权』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21077:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21083:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『逻辑一致性指标必须与 commitment/coverage 联合报告，否则系统性 abstention 会被误判为高 coherence』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21083:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21088:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21088:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21101:start -->
未入选：完整 frontier 仍保留 `INFER-SCHEDULING` 的『推荐模型推理的 stream scheduler 应按 embedding、interaction 与 dense 阶段的资源轮廓编排，而不是只按请求 FIFO』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21101:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21121:start -->
未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『协议约束任务可以在 autoregressive trajectory 上做局部规则编辑；rule coverage、trigger telemetry 与 rollback 必须成为 runtime state』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21121:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21126:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『评估协议需要同时暴露统计不稳定、metric gaming、prompt sensitivity 与 ranking reversal，单一 aggregate score 不能拥有 release authority』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21126:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21129:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『Intent ABI 应把用户意图、capability grant 与 effect-time authorization 编译成可验证接口，而不是把自然语言意图直接当权限』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21129:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21130:start -->
未入选：完整 frontier 仍保留 `PLATFORM-MONITORING` 的『GPU/AI 服务的异常浪涌要由多窗口 telemetry 与显式阈值选择检测，并把 recall、false alarm 与 detection delay 一起交给 operator』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21130:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21140:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『Agent benchmark 应把 token、tool call、retry 与 wall-clock 成本纳入同一 token-economic contract，成功率不是资源效率』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21140:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21144:start -->
未入选：完整 frontier 仍保留 `AGENT-MEMORY` 的『Adaptive memory 应按 task evidence 选择写入、压缩与检索路径，并把 policy state 与事实 state 分离』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21144:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21172:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『video/world-model poisoning 需要按 poison rate、trigger persistence 与 downstream action effect 验收，干净集精度不能覆盖后门风险』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21173:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-WORLD-MODELS` 的『从 sparse-goal demonstrations 反演 transition dynamics 需要把 reward/goal condition、Bellman identifiability 与 learned transition 分开，恢复条件不是任意环境真值』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21173:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21188:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA 可先离散化长期 episodic memory 并预训练 action head，但 memory code、policy state 与真实机器人 observation identity 必须联结』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21188:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21228:start -->
未入选：完整 frontier 仍保留 `AGENT-MULTI-AGENT` 的『多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21228:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21238:start -->
未入选：完整 frontier 仍保留 `INFER-KV-CACHE` 的『KV cache 可按对话、batch 与访问热度自适应分区；partition version、迁移成本与 miss fallback 必须进入 cache control state』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21238:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21249:start -->
未入选：完整 frontier 仍保留 `MODEL-POSITION-ENCODING` 的『位置表示的训练动力学需要区分静态相关、训练演化与因果消融，最终 probe 相似度不能证明模型真的使用该位置通道』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21249:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21255:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『uncertainty gate 只有经 calibration 与 certifying boundary 后才能影响 release；置信度本身不是安全证明』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21255:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21257:start -->
未入选：完整 frontier 仍保留 `INFER-GPU-MEMORY` 的『端侧大模型 PTQ 必须把 weight/activation bit-width、算子支持与任务退化一起验收，压缩比不能代表可部署性』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21257:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21262:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『rubric 与 candidate co-evolution 必须隔离生成、judge 与 held-out adjudication，避免 evaluator 随被测对象共同漂移』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21262:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21282:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『DNN global robustness 是输入对的 2-safety property；differential halo zonotope 联合传播两条执行并界定 divergence，而非重复 local ball 检查』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21282:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21307:start -->
未入选：完整 frontier 仍保留 `AGENT-REFLECTION` 的『skill expansion 应先检测能力缺口、生成 candidate skill、独立验证再路由，单次成功不能直接提升为长期 skill』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21307:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21315:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-WORLD-MODELS` 的『Social World Model 要把多主体状态、关系变化与 action-conditioned transition 分层，并用 wake/sleep/deploy gates 限制自更新』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21315:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21337:start -->
未入选：完整 frontier 仍保留 `TRAIN-DATA` 的『训练数据 pipeline 应将任务生成、过滤、difficulty routing 与训练后 validation 绑定同一 lineage，synthetic volume 不是质量证明』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21337:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21338:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21338:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21359:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『hallucination benchmark 应绑定 evidence source、错误 taxonomy 与 human validation，自动 judge 分数不能替代 claim-level provenance』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21359:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21372:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『neural action codec 把连续控制压缩成离散 token 时，codebook identity、重构误差与 policy action head 必须作为同一部署 artifact』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21372:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21386:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA failure benchmark 应分别标注 perception、reasoning 与 action failure，并保留 intervention/fallback 可执行证据』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21386:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21389:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『生产 SIEM telemetry 转研究 artifact 时必须保留时间与 entity consistency，同时声明 anonymization 的 privacy-utility boundary 而非声称形式匿名』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21389:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21398:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『具身表征与动作 token 的对齐可由对比目标训练，但 representation gain 必须落到控制任务与 failure slice，而非只看 embedding quality』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21398:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21401:start -->
未入选：完整 frontier 仍保留 `INFER-SCHEDULING` 的『大规模 Agent swarm 的调度对象是带依赖和状态的 task graph，placement、重试与资源隔离要由平台而非 coordinator prompt 持有』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21401:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21406:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA 自改进必须把 data collection、critic signal 与 policy update 版本化，并在真实动作前保留 independent safety gate』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21406:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21409:start -->
未入选：完整 frontier 仍保留 `AGENT-TOOL-CALLING` 的『tool-call repair 不能只改最终格式；应反演失败调用的 constraint、局部修补 argument 并在有限重试后回退』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21409:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21428:start -->
未入选：完整 frontier 仍保留 `INFER-GPU-MEMORY` 的『端侧 LLM benchmark 必须绑定具体模型、backend、硬件、prompt 与测量口径，峰值内存或 tokens/s 不能跨设备直接外推』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21428:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21445:start -->
未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『Agent workflow robustness 应把 primitive sequence、state transition 与 recovery branch 显式化，最终成功会掩盖脆弱中间路径』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21445:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21509:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『异构 VLA 模块 stitching 需要显式 sensor/action interface 与 latency budget，子模型可互换不代表闭环状态连续』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21509:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21514:start -->
未入选：完整 frontier 仍保留 `TRAIN-PRETRAINING` 的『深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21514:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21553:start -->
未入选：完整 frontier 仍保留 `AGENT-RAG` 的『RAG 系统需要联合检索、生成与证据评估，HotpotQA 上的答案提升不能单独证明索引 freshness 或生产一致性』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21553:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21565:start -->
未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『Agent-based simulation 的角色、规则、environment transition 与 observation 必须成为可重放 artifact，而非仅保存在 prompt 叙述中』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21565:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21572:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-EMBODIED-VLA` 的『VLA critic 要先在 failure evidence 上独立训练，再以受限 signal 进入 policy update；critic score 不能拥有物理提交权』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21572:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21584:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『deployment threshold 必须从开发集冻结并在目标分布报告 HTER；test-set oracle EER 会隐藏真实 false-reject/false-accept failure』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21584:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21627:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『trajectory preference evaluation 应保存环境、轨迹、judge 与 human disagreement，pairwise label 不是脱离 policy 的稳定真值』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21627:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21633:start -->
未入选：完整 frontier 仍保留 `INFER-KV-CACHE` 的『长上下文 retrieval 可把 cold state 分层到 CPU 并用 GPU kernel 协同读取，但 index/cache identity 与传输重叠决定真实收益』，但相对 `REPRODUCIBLE-INFERENCE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21633:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21638:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『tiered language-model service 应按 capability/risk 分离模型与权限；成本路由不能让弱安全模型获得强 effect authority』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21638:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21654:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『compositional evaluation 应保存组件、组合、judge 与 failure attribution，组合总分不能定位哪个 handoff 失效』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21654:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21666:start -->
未入选：完整 frontier 仍保留 `AGENT-MULTI-AGENT` 的『多 Agent 共识要保存独立 evidence、divergence 与 shared verification；重复采样的多数票不等于独立证明』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21666:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21678:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『从 internal representation 可解码出答案不证明 reasoning faithful；diagnostic ladder 要区分 decodability、causal use 与输出行为』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21678:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21710:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『社会行为安全评估必须绑定场景、规范、judge 与 policy optimization，合成 reward 改善不证明真实人群规范覆盖』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21710:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21732:start -->
未入选：完整 frontier 仍保留 `PLATFORM-SECURITY` 的『对 Agent/system 的组合攻击要显式建模 attacker capability、可见状态与 defense boundary；单点 sanitize 不等于 end-to-end containment』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21732:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21775:start -->
未入选：完整 frontier 仍保留 `MULTIMODAL-WORLD-MODELS` 的『world-model rollout horizon 应成为按任务难度与不确定性调节的状态，而非训练/推理期固定常数』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21775:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21777:start -->
未入选：完整 frontier 仍保留 `AGENT-RAG` 的『retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21777:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21787:start -->
未入选：完整 frontier 仍保留 `PLATFORM-MODEL-REGISTRY` 的『模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21787:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21795:start -->
未入选：完整 frontier 仍保留 `TRAIN-RLHF` 的『reward clustering 应把异质 reward mode 分开优化并保存 cluster identity，聚合 scalar reward 会隐藏冲突偏好与 hacking』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21795:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21803:start -->
未入选：完整 frontier 仍保留 `MODEL-LONG-CONTEXT` 的『TTT-NTP 在推理时用 next-token prediction 写入 fast weights；write scope、chunk boundary 与 reset policy 必须成为 context state』，但相对 `SEQUENCE-COROUTINE` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21803:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21804:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『coding-Agent evaluation 应按 thread/issue 持久化多轮 context 与 side effects，单次 patch pass 会漏掉跨轮回归』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21804:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21807:start -->
未入选：完整 frontier 仍保留 `PLATFORM-EVALUATION-SYSTEM` 的『规模变化会同时提高能力与稳定错误；evaluation 必须用 slice 与 uncertainty 分解 opposing forces 而非只报告均值』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21807:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21811:start -->
未入选：完整 frontier 仍保留 `AGENT-REFLECTION` 的『critic-based self-improvement 要分离 critique quality、policy uptake 与最终 outcome，强 critic 也不证明 actor 会正确使用反馈』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-21811:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28376:start -->
未入选：完整 frontier 仍保留 `AGENT-MEMORY` 的『OSU-Mem 将 observation、summary 与 update 分阶段持久化，并要求在多步任务中分别验证 construction、retrieval 与 action use』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-28376:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28379:start -->
未入选：完整 frontier 仍保留 `AGENT-WORKFLOW` 的『LEDGER 用显式 dependency graph 组织长期任务状态，retrieval 与 consistency repair 必须围绕同一 node/version identity』，但相对 `CALIBRATION-CONTROL` winner，它的跨层 owner handoff、运行时控制面或可迁移系统影响更窄；Evidence 与 Books disposition 不受降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-28379:end -->

<!-- analysis:DA-20260620-REPRODUCIBLE-INFERENCE:start -->
### DA-20260620-REPRODUCIBLE-INFERENCE
异构执行的复现性不是随机种子问题：kernel boundary 的下转型、KV 存储与 GEMM 误差补偿共同决定答案是否翻转。HEAL 的价值是把数值状态、硬件路径与 TPOT/memory 代价放进同一部署合同，但只在披露模型、GPU 与 MCR-Bench 上成立。
<!-- analysis:DA-20260620-REPRODUCIBLE-INFERENCE:end -->

<!-- analysis:DA-20260620-CALIBRATION-CONTROL:start -->
### DA-20260620-CALIBRATION-CONTROL
校准描述观测置信，不授予动作控制。action-conditioned prefix branching 展示了 intervention 需要显式 action、counterfactual trajectory 与 outcome channel；没有这些状态，confidence 只能是 sensor。
<!-- analysis:DA-20260620-CALIBRATION-CONTROL:end -->

<!-- analysis:DA-20260620-SEQUENCE-COROUTINE:start -->
### DA-20260620-SEQUENCE-COROUTINE
sequence coroutine 把 generation 从黑盒请求改成可暂停、可组合的状态机，使 batching 可以跨序列推进；同时 scheduler 必须承担 lifecycle、fairness、memory pressure 与 failure recovery。
<!-- analysis:DA-20260620-SEQUENCE-COROUTINE:end -->

## 6. Books Comparison

 and Decision

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21023 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-21023 | delta:SF-2026-ARXIV-2606-21023 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21023 |
| SF-2026-ARXIV-2606-21024 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-21024 | delta:SF-2026-ARXIV-2606-21024 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21024 |
| SF-2026-ARXIV-2606-21037 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21037 | delta:SF-2026-ARXIV-2606-21037 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21037 |
| SF-2026-ARXIV-2606-21045 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21045 | delta:SF-2026-ARXIV-2606-21045 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21045 |
| SF-2026-ARXIV-2606-21071 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21071 | delta:SF-2026-ARXIV-2606-21071 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21071 |
| SF-2026-ARXIV-2606-21077 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21077 | delta:SF-2026-ARXIV-2606-21077 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21077 |
| SF-2026-ARXIV-2606-21083 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21083 | delta:SF-2026-ARXIV-2606-21083 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21083 |
| SF-2026-ARXIV-2606-21088 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21088 | delta:SF-2026-ARXIV-2606-21088 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21088 |
| SF-2026-ARXIV-2606-21101 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-21101 | delta:SF-2026-ARXIV-2606-21101 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21101 |
| SF-2026-ARXIV-2606-21121 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-21121 | delta:SF-2026-ARXIV-2606-21121 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21121 |
| SF-2026-ARXIV-2606-21126 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21126 | delta:SF-2026-ARXIV-2606-21126 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21126 |
| SF-2026-ARXIV-2606-21129 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21129 | delta:SF-2026-ARXIV-2606-21129 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21129 |
| SF-2026-ARXIV-2606-21130 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/68-logging.md#L1 | existing:SF-2026-ARXIV-2606-21130 | delta:SF-2026-ARXIV-2606-21130 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21130 |
| SF-2026-ARXIV-2606-21140 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21140 | delta:SF-2026-ARXIV-2606-21140 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21140 |
| SF-2026-ARXIV-2606-21144 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-21144 | delta:SF-2026-ARXIV-2606-21144 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21144 |
| SF-2026-ARXIV-2606-21172 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21172 | delta:SF-2026-ARXIV-2606-21172 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21172 |
| SF-2026-ARXIV-2606-21173 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-21173 | delta:SF-2026-ARXIV-2606-21173 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21173 |
| SF-2026-ARXIV-2606-21188 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21188 | delta:SF-2026-ARXIV-2606-21188 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21188 |
| SF-2026-ARXIV-2606-21228 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-21228 | delta:SF-2026-ARXIV-2606-21228 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21228 |
| SF-2026-ARXIV-2606-21238 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-21238 | delta:SF-2026-ARXIV-2606-21238 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21238 |
| SF-2026-ARXIV-2606-21249 | MODEL-POSITION-ENCODING | books/part-02-model/13-position-encoding.md#L1 | books/part-02-model/14-self-attention.md#L1 | existing:SF-2026-ARXIV-2606-21249 | delta:SF-2026-ARXIV-2606-21249 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21249 |
| SF-2026-ARXIV-2606-21255 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21255 | delta:SF-2026-ARXIV-2606-21255 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21255 |
| SF-2026-ARXIV-2606-21257 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-21257 | delta:SF-2026-ARXIV-2606-21257 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21257 |
| SF-2026-ARXIV-2606-21262 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21262 | delta:SF-2026-ARXIV-2606-21262 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21262 |
| SF-2026-ARXIV-2606-21282 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21282 | delta:SF-2026-ARXIV-2606-21282 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21282 |
| SF-2026-ARXIV-2606-21307 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-21307 | delta:SF-2026-ARXIV-2606-21307 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21307 |
| SF-2026-ARXIV-2606-21315 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-21315 | delta:SF-2026-ARXIV-2606-21315 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21315 |
| SF-2026-ARXIV-2606-21337 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-21337 | delta:SF-2026-ARXIV-2606-21337 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21337 |
| SF-2026-ARXIV-2606-21338 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21338 | delta:SF-2026-ARXIV-2606-21338 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21338 |
| SF-2026-ARXIV-2606-21359 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21359 | delta:SF-2026-ARXIV-2606-21359 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21359 |
| SF-2026-ARXIV-2606-21372 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21372 | delta:SF-2026-ARXIV-2606-21372 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21372 |
| SF-2026-ARXIV-2606-21386 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21386 | delta:SF-2026-ARXIV-2606-21386 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21386 |
| SF-2026-ARXIV-2606-21389 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21389 | delta:SF-2026-ARXIV-2606-21389 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21389 |
| SF-2026-ARXIV-2606-21398 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21398 | delta:SF-2026-ARXIV-2606-21398 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21398 |
| SF-2026-ARXIV-2606-21399 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-21399 | delta:SF-2026-ARXIV-2606-21399 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21399 |
| SF-2026-ARXIV-2606-21401 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-21401 | delta:SF-2026-ARXIV-2606-21401 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21401 |
| SF-2026-ARXIV-2606-21406 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21406 | delta:SF-2026-ARXIV-2606-21406 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21406 |
| SF-2026-ARXIV-2606-21409 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-21409 | delta:SF-2026-ARXIV-2606-21409 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21409 |
| SF-2026-ARXIV-2606-21428 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-21428 | delta:SF-2026-ARXIV-2606-21428 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21428 |
| SF-2026-ARXIV-2606-21445 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-21445 | delta:SF-2026-ARXIV-2606-21445 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21445 |
| SF-2026-ARXIV-2606-21509 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21509 | delta:SF-2026-ARXIV-2606-21509 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21509 |
| SF-2026-ARXIV-2606-21514 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L1 | books/part-04-training-system/29-sft.md#L1 | existing:SF-2026-ARXIV-2606-21514 | delta:SF-2026-ARXIV-2606-21514 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21514 |
| SF-2026-ARXIV-2606-21553 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-21553 | delta:SF-2026-ARXIV-2606-21553 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21553 |
| SF-2026-ARXIV-2606-21565 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-21565 | delta:SF-2026-ARXIV-2606-21565 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21565 |
| SF-2026-ARXIV-2606-21572 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-21572 | delta:SF-2026-ARXIV-2606-21572 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21572 |
| SF-2026-ARXIV-2606-21584 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21584 | delta:SF-2026-ARXIV-2606-21584 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21584 |
| SF-2026-ARXIV-2606-21627 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21627 | delta:SF-2026-ARXIV-2606-21627 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21627 |
| SF-2026-ARXIV-2606-21633 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-21633 | delta:SF-2026-ARXIV-2606-21633 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21633 |
| SF-2026-ARXIV-2606-21638 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21638 | delta:SF-2026-ARXIV-2606-21638 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21638 |
| SF-2026-ARXIV-2606-21654 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21654 | delta:SF-2026-ARXIV-2606-21654 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21654 |
| SF-2026-ARXIV-2606-21666 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-21666 | delta:SF-2026-ARXIV-2606-21666 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21666 |
| SF-2026-ARXIV-2606-21678 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21678 | delta:SF-2026-ARXIV-2606-21678 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21678 |
| SF-2026-ARXIV-2606-21710 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21710 | delta:SF-2026-ARXIV-2606-21710 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21710 |
| SF-2026-ARXIV-2606-21712 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-21712 | delta:SF-2026-ARXIV-2606-21712 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21712 |
| SF-2026-ARXIV-2606-21732 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-21732 | delta:SF-2026-ARXIV-2606-21732 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21732 |
| SF-2026-ARXIV-2606-21775 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-21775 | delta:SF-2026-ARXIV-2606-21775 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21775 |
| SF-2026-ARXIV-2606-21777 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-21777 | delta:SF-2026-ARXIV-2606-21777 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21777 |
| SF-2026-ARXIV-2606-21787 | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#L1 | books/part-06-ai-infrastructure/60-training-operator.md#L1 | existing:SF-2026-ARXIV-2606-21787 | delta:SF-2026-ARXIV-2606-21787 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21787 |
| SF-2026-ARXIV-2606-21795 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-21795 | delta:SF-2026-ARXIV-2606-21795 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21795 |
| SF-2026-ARXIV-2606-21803 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L1 | books/part-02-model/21-moe.md#L1 | existing:SF-2026-ARXIV-2606-21803 | delta:SF-2026-ARXIV-2606-21803 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21803 |
| SF-2026-ARXIV-2606-21804 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21804 | delta:SF-2026-ARXIV-2606-21804 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21804 |
| SF-2026-ARXIV-2606-21807 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-21807 | delta:SF-2026-ARXIV-2606-21807 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21807 |
| SF-2026-ARXIV-2606-21811 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-21811 | delta:SF-2026-ARXIV-2606-21811 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21811 |
| SF-2026-ARXIV-2606-28376 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-28376 | delta:SF-2026-ARXIV-2606-28376 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28376 |
| SF-2026-ARXIV-2606-28379 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-28379 | delta:SF-2026-ARXIV-2606-28379 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28379 |

<!-- existing:SF-2026-ARXIV-2606-21023:start -->
`books/part-05-inference-system/54-gpu-memory.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21023:end -->

<!-- delta:SF-2026-ARXIV-2606-21023:start -->
异构 GPU 上 greedy decode 仍会因 kernel-boundary downcast 累积而翻转；HEAL 用 INT16 Q/K/V 与双 16-bit GEMM 误差补偿换取接近 FP32 的功能复现性
<!-- delta:SF-2026-ARXIV-2606-21023:end -->

<!-- books-review:SF-2026-ARXIV-2606-21023:start -->
Unique owner `INFER-GPU-MEMORY`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies`，只支持『异构 GPU 上 greedy decode 仍会因 kernel-boundary downcast 累积而翻转；HEAL 用 INT16 Q/K/V 与双 16-bit GEMM 误差补偿换取接近 FP32 的功能复现性』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21023:end -->

<!-- existing:SF-2026-ARXIV-2606-21024:start -->
`books/part-07-agent/77-memory.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21024:end -->

<!-- delta:SF-2026-ARXIV-2606-21024:start -->
失败经验应以带 task、attempt、failure mode、diagnosis 与 prevention 的 negative-knowledge record 写入共享 memory，并在后续尝试前检索而非覆盖成功轨迹
<!-- delta:SF-2026-ARXIV-2606-21024:end -->

<!-- books-review:SF-2026-ARXIV-2606-21024:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21024v1 §5 Conclusion; §4.5 Cross-system Transfer`，只支持『失败经验应以带 task、attempt、failure mode、diagnosis 与 prevention 的 negative-knowledge record 写入共享 memory，并在后续尝试前检索而非覆盖成功轨迹』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。写入、检索或来源证据不足时 hold/隔离 candidate memory，保留原始轨迹并禁止自动覆盖；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21024:end -->

<!-- existing:SF-2026-ARXIV-2606-21037:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21037:end -->

<!-- delta:SF-2026-ARXIV-2606-21037:start -->
LLM attacker 与人类 attacker 的 deception response 不同，security evaluation 必须把 attacker class、trap recognition 与实际 exploit action 分开记录
<!-- delta:SF-2026-ARXIV-2606-21037:end -->

<!-- books-review:SF-2026-ARXIV-2606-21037:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21037v1 §5 Discussion; §6 Conclusion`，只支持『LLM attacker 与人类 attacker 的 deception response 不同，security evaluation 必须把 attacker class、trap recognition 与实际 exploit action 分开记录』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21037:end -->

<!-- existing:SF-2026-ARXIV-2606-21045:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21045:end -->

<!-- delta:SF-2026-ARXIV-2606-21045:start -->
训练完整性可以由连续 gradient-signal challenge 做 optimistic verification，但 verifier 必须拥有 challenge identity、容忍区间与失败升级路径
<!-- delta:SF-2026-ARXIV-2606-21045:end -->

<!-- books-review:SF-2026-ARXIV-2606-21045:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21045v1 §VII Limitations and Discussion`，只支持『训练完整性可以由连续 gradient-signal challenge 做 optimistic verification，但 verifier 必须拥有 challenge identity、容忍区间与失败升级路径』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21045:end -->

<!-- existing:SF-2026-ARXIV-2606-21071:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21071:end -->

<!-- delta:SF-2026-ARXIV-2606-21071:start -->
Agent vulnerability audit 必须覆盖 activation 后的 runtime data/control flow，静态 skill 文本与 manifest 不能代表组合执行安全
<!-- delta:SF-2026-ARXIV-2606-21071:end -->

<!-- books-review:SF-2026-ARXIV-2606-21071:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21071v1 §3.4 Taxonomy Scope; §7.3–§7.4 syntactic/semantic boundary`，只支持『Agent vulnerability audit 必须覆盖 activation 后的 runtime data/control flow，静态 skill 文本与 manifest 不能代表组合执行安全』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21071:end -->

<!-- existing:SF-2026-ARXIV-2606-21077:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21077:end -->

<!-- delta:SF-2026-ARXIV-2606-21077:start -->
黑盒 Agent red-team 可用可迁移 observation/action perturbation 搜索 failure trajectory，但 attack generator 不能取得生产执行权
<!-- delta:SF-2026-ARXIV-2606-21077:end -->

<!-- books-review:SF-2026-ARXIV-2606-21077:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21077v1 §6 Defense Implications; Scope of Contribution; Responsible Use`，只支持『黑盒 Agent red-team 可用可迁移 observation/action perturbation 搜索 failure trajectory，但 attack generator 不能取得生产执行权』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21077:end -->

<!-- existing:SF-2026-ARXIV-2606-21083:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21083:end -->

<!-- delta:SF-2026-ARXIV-2606-21083:start -->
逻辑一致性指标必须与 commitment/coverage 联合报告，否则系统性 abstention 会被误判为高 coherence
<!-- delta:SF-2026-ARXIV-2606-21083:end -->

<!-- books-review:SF-2026-ARXIV-2606-21083:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21083v1 §8 Conclusion; Appendix B Theoretical Foundations`，只支持『逻辑一致性指标必须与 commitment/coverage 联合报告，否则系统性 abstention 会被误判为高 coherence』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21083:end -->

<!-- existing:SF-2026-ARXIV-2606-21088:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21088:end -->

<!-- delta:SF-2026-ARXIV-2606-21088:start -->
长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进
<!-- delta:SF-2026-ARXIV-2606-21088:end -->

<!-- books-review:SF-2026-ARXIV-2606-21088:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21088v1 §5 Limitations; Appendix F Discussion`，只支持『长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21088:end -->

<!-- existing:SF-2026-ARXIV-2606-21101:start -->
`books/part-05-inference-system/56-inference-scheduling.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21101:end -->

<!-- delta:SF-2026-ARXIV-2606-21101:start -->
推荐模型推理的 stream scheduler 应按 embedding、interaction 与 dense 阶段的资源轮廓编排，而不是只按请求 FIFO
<!-- delta:SF-2026-ARXIV-2606-21101:end -->

<!-- books-review:SF-2026-ARXIV-2606-21101:start -->
Unique owner `INFER-SCHEDULING`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21101v1 §VI Conclusion and evaluated workload boundary`，只支持『推荐模型推理的 stream scheduler 应按 embedding、interaction 与 dense 阶段的资源轮廓编排，而不是只按请求 FIFO』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。估计失准或 SLO slack 耗尽时停止合批/迁移，回退到隔离队列与保守 admission；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21101:end -->

<!-- existing:SF-2026-ARXIV-2606-21121:start -->
`books/part-07-agent/81-workflow.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21121:end -->

<!-- delta:SF-2026-ARXIV-2606-21121:start -->
协议约束任务可以在 autoregressive trajectory 上做局部规则编辑；rule coverage、trigger telemetry 与 rollback 必须成为 runtime state
<!-- delta:SF-2026-ARXIV-2606-21121:end -->

<!-- books-review:SF-2026-ARXIV-2606-21121:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21121v1 §7 Limitations; §9 Future Work`，只支持『协议约束任务可以在 autoregressive trajectory 上做局部规则编辑；rule coverage、trigger telemetry 与 rollback 必须成为 runtime state』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21121:end -->

<!-- existing:SF-2026-ARXIV-2606-21126:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21126:end -->

<!-- delta:SF-2026-ARXIV-2606-21126:start -->
评估协议需要同时暴露统计不稳定、metric gaming、prompt sensitivity 与 ranking reversal，单一 aggregate score 不能拥有 release authority
<!-- delta:SF-2026-ARXIV-2606-21126:end -->

<!-- books-review:SF-2026-ARXIV-2606-21126:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21126v1 §6.4 Scope and Recommendations; §7 Conclusion`，只支持『评估协议需要同时暴露统计不稳定、metric gaming、prompt sensitivity 与 ranking reversal，单一 aggregate score 不能拥有 release authority』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21126:end -->

<!-- existing:SF-2026-ARXIV-2606-21129:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21129:end -->

<!-- delta:SF-2026-ARXIV-2606-21129:start -->
Intent ABI 应把用户意图、capability grant 与 effect-time authorization 编译成可验证接口，而不是把自然语言意图直接当权限
<!-- delta:SF-2026-ARXIV-2606-21129:end -->

<!-- books-review:SF-2026-ARXIV-2606-21129:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21129v1 §7 Discussion and Limitations`，只支持『Intent ABI 应把用户意图、capability grant 与 effect-time authorization 编译成可验证接口，而不是把自然语言意图直接当权限』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21129:end -->

<!-- existing:SF-2026-ARXIV-2606-21130:start -->
`books/part-06-ai-infrastructure/67-monitoring.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/68-logging.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21130:end -->

<!-- delta:SF-2026-ARXIV-2606-21130:start -->
GPU/AI 服务的异常浪涌要由多窗口 telemetry 与显式阈值选择检测，并把 recall、false alarm 与 detection delay 一起交给 operator
<!-- delta:SF-2026-ARXIV-2606-21130:end -->

<!-- books-review:SF-2026-ARXIV-2606-21130:start -->
Unique owner `PLATFORM-MONITORING`; adjacent non-owner `books/part-06-ai-infrastructure/68-logging.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21130v1 §V Discussion; §VI Conclusion`，只支持『GPU/AI 服务的异常浪涌要由多窗口 telemetry 与显式阈值选择检测，并把 recall、false alarm 与 detection delay 一起交给 operator』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。telemetry 缺失或阈值漂移时降级为 observe-only 告警并要求 operator 复核，不自动执行修复；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21130:end -->

<!-- existing:SF-2026-ARXIV-2606-21140:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21140:end -->

<!-- delta:SF-2026-ARXIV-2606-21140:start -->
Agent benchmark 应把 token、tool call、retry 与 wall-clock 成本纳入同一 token-economic contract，成功率不是资源效率
<!-- delta:SF-2026-ARXIV-2606-21140:end -->

<!-- books-review:SF-2026-ARXIV-2606-21140:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21140v1 §6 Discussion and Limitations`，只支持『Agent benchmark 应把 token、tool call、retry 与 wall-clock 成本纳入同一 token-economic contract，成功率不是资源效率』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21140:end -->

<!-- existing:SF-2026-ARXIV-2606-21144:start -->
`books/part-07-agent/77-memory.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21144:end -->

<!-- delta:SF-2026-ARXIV-2606-21144:start -->
Adaptive memory 应按 task evidence 选择写入、压缩与检索路径，并把 policy state 与事实 state 分离
<!-- delta:SF-2026-ARXIV-2606-21144:end -->

<!-- books-review:SF-2026-ARXIV-2606-21144:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21144v1 §7 Limitations`，只支持『Adaptive memory 应按 task evidence 选择写入、压缩与检索路径，并把 policy state 与事实 state 分离』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。写入、检索或来源证据不足时 hold/隔离 candidate memory，保留原始轨迹并禁止自动覆盖；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21144:end -->

<!-- existing:SF-2026-ARXIV-2606-21172:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21172:end -->

<!-- delta:SF-2026-ARXIV-2606-21172:start -->
video/world-model poisoning 需要按 poison rate、trigger persistence 与 downstream action effect 验收，干净集精度不能覆盖后门风险
<!-- delta:SF-2026-ARXIV-2606-21172:end -->

<!-- books-review:SF-2026-ARXIV-2606-21172:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21172v1 §6 Limitation`，只支持『video/world-model poisoning 需要按 poison rate、trigger persistence 与 downstream action effect 验收，干净集精度不能覆盖后门风险』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21172:end -->

<!-- existing:SF-2026-ARXIV-2606-21173:start -->
`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21173:end -->

<!-- delta:SF-2026-ARXIV-2606-21173:start -->
从 sparse-goal demonstrations 反演 transition dynamics 需要把 reward/goal condition、Bellman identifiability 与 learned transition 分开，恢复条件不是任意环境真值
<!-- delta:SF-2026-ARXIV-2606-21173:end -->

<!-- books-review:SF-2026-ARXIV-2606-21173:start -->
Unique owner `MULTIMODAL-WORLD-MODELS`; adjacent non-owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `Not Disclosed — official exact-v1 body unavailable; exact-v1 abstract and linked author artifacts expose sufficient-identifiability and named-environment scope but no dedicated limitation section`，只支持『从 sparse-goal demonstrations 反演 transition dynamics 需要把 reward/goal condition、Bellman identifiability 与 learned transition 分开，恢复条件不是任意环境真值』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。identifiability、rollout uncertainty 或 horizon gate 失败时停止想象 rollout，交还真实环境观测；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21173:end -->

<!-- existing:SF-2026-ARXIV-2606-21188:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21188:end -->

<!-- delta:SF-2026-ARXIV-2606-21188:start -->
VLA 可先离散化长期 episodic memory 并预训练 action head，但 memory code、policy state 与真实机器人 observation identity 必须联结
<!-- delta:SF-2026-ARXIV-2606-21188:end -->

<!-- books-review:SF-2026-ARXIV-2606-21188:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21188v1 §5 Limitations and Conclusion`，只支持『VLA 可先离散化长期 episodic memory 并预训练 action head，但 memory code、policy state 与真实机器人 observation identity 必须联结』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21188:end -->

<!-- existing:SF-2026-ARXIV-2606-21228:start -->
`books/part-07-agent/82-multi-agent.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21228:end -->

<!-- delta:SF-2026-ARXIV-2606-21228:start -->
多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中
<!-- delta:SF-2026-ARXIV-2606-21228:end -->

<!-- books-review:SF-2026-ARXIV-2606-21228:start -->
Unique owner `AGENT-MULTI-AGENT`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21228v1 §5 Conclusions and evaluated agent/task scope`，只支持『多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。共享状态或独立复核发生冲突时暂停 commit，回到单 Agent baseline 或串行 adjudication；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21228:end -->

<!-- existing:SF-2026-ARXIV-2606-21238:start -->
`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21238:end -->

<!-- delta:SF-2026-ARXIV-2606-21238:start -->
KV cache 可按对话、batch 与访问热度自适应分区；partition version、迁移成本与 miss fallback 必须进入 cache control state
<!-- delta:SF-2026-ARXIV-2606-21238:end -->

<!-- books-review:SF-2026-ARXIV-2606-21238:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21238v1 §5 Conclusion; §6 Future Work`，只支持『KV cache 可按对话、batch 与访问热度自适应分区；partition version、迁移成本与 miss fallback 必须进入 cache control state』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。cache identity、容量或迁移收益不满足时回退到重算或本地 KV，并记录 miss/eviction 原因；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21238:end -->

<!-- existing:SF-2026-ARXIV-2606-21249:start -->
`books/part-02-model/13-position-encoding.md` 已有 本章要回答的问题；相邻 `books/part-02-model/14-self-attention.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21249:end -->

<!-- delta:SF-2026-ARXIV-2606-21249:start -->
位置表示的训练动力学需要区分静态相关、训练演化与因果消融，最终 probe 相似度不能证明模型真的使用该位置通道
<!-- delta:SF-2026-ARXIV-2606-21249:end -->

<!-- books-review:SF-2026-ARXIV-2606-21249:start -->
Unique owner `MODEL-POSITION-ENCODING`; adjacent non-owner `books/part-02-model/14-self-attention.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21249v1 §6 Scope and Caveats; §9 Limitations`，只支持『位置表示的训练动力学需要区分静态相关、训练演化与因果消融，最终 probe 相似度不能证明模型真的使用该位置通道』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。因果消融不支持时保留现有位置方案，不由 probe 相似度触发架构替换；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21249:end -->

<!-- existing:SF-2026-ARXIV-2606-21255:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21255:end -->

<!-- delta:SF-2026-ARXIV-2606-21255:start -->
uncertainty gate 只有经 calibration 与 certifying boundary 后才能影响 release；置信度本身不是安全证明
<!-- delta:SF-2026-ARXIV-2606-21255:end -->

<!-- books-review:SF-2026-ARXIV-2606-21255:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21255v1 §5 Conclusion; Appendix D Boundary Construction`，只支持『uncertainty gate 只有经 calibration 与 certifying boundary 后才能影响 release；置信度本身不是安全证明』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21255:end -->

<!-- existing:SF-2026-ARXIV-2606-21257:start -->
`books/part-05-inference-system/54-gpu-memory.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21257:end -->

<!-- delta:SF-2026-ARXIV-2606-21257:start -->
端侧大模型 PTQ 必须把 weight/activation bit-width、算子支持与任务退化一起验收，压缩比不能代表可部署性
<!-- delta:SF-2026-ARXIV-2606-21257:end -->

<!-- books-review:SF-2026-ARXIV-2606-21257:start -->
Unique owner `INFER-GPU-MEMORY`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21257v1 §4 Limitations and Future Work`，只支持『端侧大模型 PTQ 必须把 weight/activation bit-width、算子支持与任务退化一起验收，压缩比不能代表可部署性』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21257:end -->

<!-- existing:SF-2026-ARXIV-2606-21262:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21262:end -->

<!-- delta:SF-2026-ARXIV-2606-21262:start -->
rubric 与 candidate co-evolution 必须隔离生成、judge 与 held-out adjudication，避免 evaluator 随被测对象共同漂移
<!-- delta:SF-2026-ARXIV-2606-21262:end -->

<!-- books-review:SF-2026-ARXIV-2606-21262:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21262v1 §6 Limitations`，只支持『rubric 与 candidate co-evolution 必须隔离生成、judge 与 held-out adjudication，避免 evaluator 随被测对象共同漂移』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21262:end -->

<!-- existing:SF-2026-ARXIV-2606-21282:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21282:end -->

<!-- delta:SF-2026-ARXIV-2606-21282:start -->
DNN global robustness 是输入对的 2-safety property；differential halo zonotope 联合传播两条执行并界定 divergence，而非重复 local ball 检查
<!-- delta:SF-2026-ARXIV-2606-21282:end -->

<!-- books-review:SF-2026-ARXIV-2606-21282:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `doi:10.48550/arXiv.2606.21282; exact-title author manuscript mirror §6 Conclusion states counterexample search and compositional scaling remain future work`，只支持『DNN global robustness 是输入对的 2-safety property；differential halo zonotope 联合传播两条执行并界定 divergence，而非重复 local ball 检查』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21282:end -->

<!-- existing:SF-2026-ARXIV-2606-21307:start -->
`books/part-07-agent/80-reflection.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/81-workflow.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21307:end -->

<!-- delta:SF-2026-ARXIV-2606-21307:start -->
skill expansion 应先检测能力缺口、生成 candidate skill、独立验证再路由，单次成功不能直接提升为长期 skill
<!-- delta:SF-2026-ARXIV-2606-21307:end -->

<!-- books-review:SF-2026-ARXIV-2606-21307:start -->
Unique owner `AGENT-REFLECTION`; adjacent non-owner `books/part-07-agent/81-workflow.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21307v1 §7 Conclusion and benchmark/skill-library scope`，只支持『skill expansion 应先检测能力缺口、生成 candidate skill、独立验证再路由，单次成功不能直接提升为长期 skill』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。held-out 验证失败时拒绝 promotion，保留旧 skill/policy 与 candidate lesson 的分离状态；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21307:end -->

<!-- existing:SF-2026-ARXIV-2606-21315:start -->
`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21315:end -->

<!-- delta:SF-2026-ARXIV-2606-21315:start -->
Social World Model 要把多主体状态、关系变化与 action-conditioned transition 分层，并用 wake/sleep/deploy gates 限制自更新
<!-- delta:SF-2026-ARXIV-2606-21315:end -->

<!-- books-review:SF-2026-ARXIV-2606-21315:start -->
Unique owner `MULTIMODAL-WORLD-MODELS`; adjacent non-owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21315v1 §6 Discussion (specificity and ablations)`，只支持『Social World Model 要把多主体状态、关系变化与 action-conditioned transition 分层，并用 wake/sleep/deploy gates 限制自更新』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。identifiability、rollout uncertainty 或 horizon gate 失败时停止想象 rollout，交还真实环境观测；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21315:end -->

<!-- existing:SF-2026-ARXIV-2606-21337:start -->
`books/part-04-training-system/27-data.md` 已有 本章要回答的问题；相邻 `books/part-04-training-system/28-pretraining.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21337:end -->

<!-- delta:SF-2026-ARXIV-2606-21337:start -->
训练数据 pipeline 应将任务生成、过滤、difficulty routing 与训练后 validation 绑定同一 lineage，synthetic volume 不是质量证明
<!-- delta:SF-2026-ARXIV-2606-21337:end -->

<!-- books-review:SF-2026-ARXIV-2606-21337:start -->
Unique owner `TRAIN-DATA`; adjacent non-owner `books/part-04-training-system/28-pretraining.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21337v1 §5 Conclusion and dataset/model scope`，只支持『训练数据 pipeline 应将任务生成、过滤、difficulty routing 与训练后 validation 绑定同一 lineage，synthetic volume 不是质量证明』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。lineage、过滤或 validation receipt 缺失时隔离该数据批，不进入不可逆训练更新；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21337:end -->

<!-- existing:SF-2026-ARXIV-2606-21338:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21338:end -->

<!-- delta:SF-2026-ARXIV-2606-21338:start -->
MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露
<!-- delta:SF-2026-ARXIV-2606-21338:end -->

<!-- books-review:SF-2026-ARXIV-2606-21338:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21338v1 §6 Conclusion and evaluated MCP/tool boundary`，只支持『MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21338:end -->

<!-- existing:SF-2026-ARXIV-2606-21359:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21359:end -->

<!-- delta:SF-2026-ARXIV-2606-21359:start -->
hallucination benchmark 应绑定 evidence source、错误 taxonomy 与 human validation，自动 judge 分数不能替代 claim-level provenance
<!-- delta:SF-2026-ARXIV-2606-21359:end -->

<!-- books-review:SF-2026-ARXIV-2606-21359:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21359v1 §7 Limitations exact headings: Evidence Source Limitations; Training-data Contamination; Confounding Fine-tuning Factors; Human-study Scope`，只支持『hallucination benchmark 应绑定 evidence source、错误 taxonomy 与 human validation，自动 judge 分数不能替代 claim-level provenance』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21359:end -->

<!-- existing:SF-2026-ARXIV-2606-21372:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21372:end -->

<!-- delta:SF-2026-ARXIV-2606-21372:start -->
neural action codec 把连续控制压缩成离散 token 时，codebook identity、重构误差与 policy action head 必须作为同一部署 artifact
<!-- delta:SF-2026-ARXIV-2606-21372:end -->

<!-- books-review:SF-2026-ARXIV-2606-21372:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21372v1 §5 Discussion and codec/policy scope`，只支持『neural action codec 把连续控制压缩成离散 token 时，codebook identity、重构误差与 policy action head 必须作为同一部署 artifact』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21372:end -->

<!-- existing:SF-2026-ARXIV-2606-21386:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21386:end -->

<!-- delta:SF-2026-ARXIV-2606-21386:start -->
VLA failure benchmark 应分别标注 perception、reasoning 与 action failure，并保留 intervention/fallback 可执行证据
<!-- delta:SF-2026-ARXIV-2606-21386:end -->

<!-- books-review:SF-2026-ARXIV-2606-21386:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21386v1 §6 Limitations; Appendix D.2 Failure Cases`，只支持『VLA failure benchmark 应分别标注 perception、reasoning 与 action failure，并保留 intervention/fallback 可执行证据』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21386:end -->

<!-- existing:SF-2026-ARXIV-2606-21389:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21389:end -->

<!-- delta:SF-2026-ARXIV-2606-21389:start -->
生产 SIEM telemetry 转研究 artifact 时必须保留时间与 entity consistency，同时声明 anonymization 的 privacy-utility boundary 而非声称形式匿名
<!-- delta:SF-2026-ARXIV-2606-21389:end -->

<!-- books-review:SF-2026-ARXIV-2606-21389:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21389v1 §5 Discussion; §7 Conclusion`，只支持『生产 SIEM telemetry 转研究 artifact 时必须保留时间与 entity consistency，同时声明 anonymization 的 privacy-utility boundary 而非声称形式匿名』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21389:end -->

<!-- existing:SF-2026-ARXIV-2606-21398:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21398:end -->

<!-- delta:SF-2026-ARXIV-2606-21398:start -->
具身表征与动作 token 的对齐可由对比目标训练，但 representation gain 必须落到控制任务与 failure slice，而非只看 embedding quality
<!-- delta:SF-2026-ARXIV-2606-21398:end -->

<!-- books-review:SF-2026-ARXIV-2606-21398:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21398v1 §IV-D Discussion and Limitations; §V Future Work`，只支持『具身表征与动作 token 的对齐可由对比目标训练，但 representation gain 必须落到控制任务与 failure slice，而非只看 embedding quality』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21398:end -->

<!-- existing:SF-2026-ARXIV-2606-21399:start -->
`books/part-07-agent/84-agent-platform.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21399:end -->

<!-- delta:SF-2026-ARXIV-2606-21399:start -->
calibration 只能描述 observational confidence，不能单独支持 intervention；Agent control 需要 action-conditioned branching 与可验证 outcome channel
<!-- delta:SF-2026-ARXIV-2606-21399:end -->

<!-- books-review:SF-2026-ARXIV-2606-21399:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21399v1 §7 Conclusion and action/benchmark boundary`，只支持『calibration 只能描述 observational confidence，不能单独支持 intervention；Agent control 需要 action-conditioned branching 与可验证 outcome channel』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。calibration 与 action outcome 不一致时收回 autonomous commit authority，降级为 proposal-only；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21399:end -->

<!-- existing:SF-2026-ARXIV-2606-21401:start -->
`books/part-05-inference-system/56-inference-scheduling.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21401:end -->

<!-- delta:SF-2026-ARXIV-2606-21401:start -->
大规模 Agent swarm 的调度对象是带依赖和状态的 task graph，placement、重试与资源隔离要由平台而非 coordinator prompt 持有
<!-- delta:SF-2026-ARXIV-2606-21401:end -->

<!-- books-review:SF-2026-ARXIV-2606-21401:start -->
Unique owner `INFER-SCHEDULING`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21401v1 §6 Production and Operation Experience; §8 Conclusion`，只支持『大规模 Agent swarm 的调度对象是带依赖和状态的 task graph，placement、重试与资源隔离要由平台而非 coordinator prompt 持有』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。估计失准或 SLO slack 耗尽时停止合批/迁移，回退到隔离队列与保守 admission；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21401:end -->

<!-- existing:SF-2026-ARXIV-2606-21406:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21406:end -->

<!-- delta:SF-2026-ARXIV-2606-21406:start -->
VLA 自改进必须把 data collection、critic signal 与 policy update 版本化，并在真实动作前保留 independent safety gate
<!-- delta:SF-2026-ARXIV-2606-21406:end -->

<!-- books-review:SF-2026-ARXIV-2606-21406:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21406v1 §6 Limitations and Future Work`，只支持『VLA 自改进必须把 data collection、critic signal 与 policy update 版本化，并在真实动作前保留 independent safety gate』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21406:end -->

<!-- existing:SF-2026-ARXIV-2606-21409:start -->
`books/part-07-agent/78-tool-calling.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/79-planning.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21409:end -->

<!-- delta:SF-2026-ARXIV-2606-21409:start -->
tool-call repair 不能只改最终格式；应反演失败调用的 constraint、局部修补 argument 并在有限重试后回退
<!-- delta:SF-2026-ARXIV-2606-21409:end -->

<!-- books-review:SF-2026-ARXIV-2606-21409:start -->
Unique owner `AGENT-TOOL-CALLING`; adjacent non-owner `books/part-07-agent/79-planning.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21409v1 §6 Fallback-limited Repairs; §9 Limitations`，只支持『tool-call repair 不能只改最终格式；应反演失败调用的 constraint、局部修补 argument 并在有限重试后回退』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。constraint repair 仍失败时停止有限重试，返回结构化错误并要求用户或 workflow 决策；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21409:end -->

<!-- existing:SF-2026-ARXIV-2606-21428:start -->
`books/part-05-inference-system/54-gpu-memory.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21428:end -->

<!-- delta:SF-2026-ARXIV-2606-21428:start -->
端侧 LLM benchmark 必须绑定具体模型、backend、硬件、prompt 与测量口径，峰值内存或 tokens/s 不能跨设备直接外推
<!-- delta:SF-2026-ARXIV-2606-21428:end -->

<!-- books-review:SF-2026-ARXIV-2606-21428:start -->
Unique owner `INFER-GPU-MEMORY`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21428v1 §5 Discussion and Bottleneck; §6 Threats to Validity`，只支持『端侧 LLM benchmark 必须绑定具体模型、backend、硬件、prompt 与测量口径，峰值内存或 tokens/s 不能跨设备直接外推』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21428:end -->

<!-- existing:SF-2026-ARXIV-2606-21445:start -->
`books/part-07-agent/81-workflow.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21445:end -->

<!-- delta:SF-2026-ARXIV-2606-21445:start -->
Agent workflow robustness 应把 primitive sequence、state transition 与 recovery branch 显式化，最终成功会掩盖脆弱中间路径
<!-- delta:SF-2026-ARXIV-2606-21445:end -->

<!-- books-review:SF-2026-ARXIV-2606-21445:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21445v1 §6 Discussion (reliability and generalization)`，只支持『Agent workflow robustness 应把 primitive sequence、state transition 与 recovery branch 显式化，最终成功会掩盖脆弱中间路径』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21445:end -->

<!-- existing:SF-2026-ARXIV-2606-21509:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21509:end -->

<!-- delta:SF-2026-ARXIV-2606-21509:start -->
异构 VLA 模块 stitching 需要显式 sensor/action interface 与 latency budget，子模型可互换不代表闭环状态连续
<!-- delta:SF-2026-ARXIV-2606-21509:end -->

<!-- books-review:SF-2026-ARXIV-2606-21509:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21509v1 §V Conclusion; Appendix A Sensor Setup`，只支持『异构 VLA 模块 stitching 需要显式 sensor/action interface 与 latency budget，子模型可互换不代表闭环状态连续』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21509:end -->

<!-- existing:SF-2026-ARXIV-2606-21514:start -->
`books/part-04-training-system/28-pretraining.md` 已有 本章要回答的问题；相邻 `books/part-04-training-system/29-sft.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21514:end -->

<!-- delta:SF-2026-ARXIV-2606-21514:start -->
深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure
<!-- delta:SF-2026-ARXIV-2606-21514:end -->

<!-- books-review:SF-2026-ARXIV-2606-21514:start -->
Unique owner `TRAIN-PRETRAINING`; adjacent non-owner `books/part-04-training-system/29-sft.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21514v1 Appendix B.3 Late-stage Failure; Appendix B.4 Implications; §6 Conclusion`，只支持『深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。loss/curvature 或稳定性证据偏离时冻结阶段转换并回退到已验证 schedule/checkpoint；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21514:end -->

<!-- existing:SF-2026-ARXIV-2606-21553:start -->
`books/part-07-agent/76-rag.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/77-memory.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21553:end -->

<!-- delta:SF-2026-ARXIV-2606-21553:start -->
RAG 系统需要联合检索、生成与证据评估，HotpotQA 上的答案提升不能单独证明索引 freshness 或生产一致性
<!-- delta:SF-2026-ARXIV-2606-21553:end -->

<!-- books-review:SF-2026-ARXIV-2606-21553:start -->
Unique owner `AGENT-RAG`; adjacent non-owner `books/part-07-agent/77-memory.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21553v1 §7 Limitations`，只支持『RAG 系统需要联合检索、生成与证据评估，HotpotQA 上的答案提升不能单独证明索引 freshness 或生产一致性』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。evidence、index 或 verifier identity 不完整时 abstain/回到原始证据，不把生成结果写成事实；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21553:end -->

<!-- existing:SF-2026-ARXIV-2606-21565:start -->
`books/part-07-agent/81-workflow.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21565:end -->

<!-- delta:SF-2026-ARXIV-2606-21565:start -->
Agent-based simulation 的角色、规则、environment transition 与 observation 必须成为可重放 artifact，而非仅保存在 prompt 叙述中
<!-- delta:SF-2026-ARXIV-2606-21565:end -->

<!-- books-review:SF-2026-ARXIV-2606-21565:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21565v1 §5 Discussion; explicit no prompt/tool/safety/reversibility/auth scope`，只支持『Agent-based simulation 的角色、规则、environment transition 与 observation 必须成为可重放 artifact，而非仅保存在 prompt 叙述中』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21565:end -->

<!-- existing:SF-2026-ARXIV-2606-21572:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21572:end -->

<!-- delta:SF-2026-ARXIV-2606-21572:start -->
VLA critic 要先在 failure evidence 上独立训练，再以受限 signal 进入 policy update；critic score 不能拥有物理提交权
<!-- delta:SF-2026-ARXIV-2606-21572:end -->

<!-- books-review:SF-2026-ARXIV-2606-21572:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21572v1 §5.3 Limitations`，只支持『VLA critic 要先在 failure evidence 上独立训练，再以受限 signal 进入 policy update；critic score 不能拥有物理提交权』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。观测、action schema、critic 或 safety gate 不一致时拒绝物理提交并交还保守 controller/人工；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21572:end -->

<!-- existing:SF-2026-ARXIV-2606-21584:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21584:end -->

<!-- delta:SF-2026-ARXIV-2606-21584:start -->
deployment threshold 必须从开发集冻结并在目标分布报告 HTER；test-set oracle EER 会隐藏真实 false-reject/false-accept failure
<!-- delta:SF-2026-ARXIV-2606-21584:end -->

<!-- books-review:SF-2026-ARXIV-2606-21584:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21584v1 §4.5 Limitations; §5 Recommendations`，只支持『deployment threshold 必须从开发集冻结并在目标分布报告 HTER；test-set oracle EER 会隐藏真实 false-reject/false-accept failure』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21584:end -->

<!-- existing:SF-2026-ARXIV-2606-21627:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21627:end -->

<!-- delta:SF-2026-ARXIV-2606-21627:start -->
trajectory preference evaluation 应保存环境、轨迹、judge 与 human disagreement，pairwise label 不是脱离 policy 的稳定真值
<!-- delta:SF-2026-ARXIV-2606-21627:end -->

<!-- books-review:SF-2026-ARXIV-2606-21627:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21627v1 §5.1 Limitations`，只支持『trajectory preference evaluation 应保存环境、轨迹、judge 与 human disagreement，pairwise label 不是脱离 policy 的稳定真值』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21627:end -->

<!-- existing:SF-2026-ARXIV-2606-21633:start -->
`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21633:end -->

<!-- delta:SF-2026-ARXIV-2606-21633:start -->
长上下文 retrieval 可把 cold state 分层到 CPU 并用 GPU kernel 协同读取，但 index/cache identity 与传输重叠决定真实收益
<!-- delta:SF-2026-ARXIV-2606-21633:end -->

<!-- books-review:SF-2026-ARXIV-2606-21633:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21633v1 §8 Conclusion and evaluated platform boundary`，只支持『长上下文 retrieval 可把 cold state 分层到 CPU 并用 GPU kernel 协同读取，但 index/cache identity 与传输重叠决定真实收益』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。cache identity、容量或迁移收益不满足时回退到重算或本地 KV，并记录 miss/eviction 原因；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21633:end -->

<!-- existing:SF-2026-ARXIV-2606-21638:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21638:end -->

<!-- delta:SF-2026-ARXIV-2606-21638:start -->
tiered language-model service 应按 capability/risk 分离模型与权限；成本路由不能让弱安全模型获得强 effect authority
<!-- delta:SF-2026-ARXIV-2606-21638:end -->

<!-- books-review:SF-2026-ARXIV-2606-21638:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21638v1 §9 Limitations`，只支持『tiered language-model service 应按 capability/risk 分离模型与权限；成本路由不能让弱安全模型获得强 effect authority』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21638:end -->

<!-- existing:SF-2026-ARXIV-2606-21654:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21654:end -->

<!-- delta:SF-2026-ARXIV-2606-21654:start -->
compositional evaluation 应保存组件、组合、judge 与 failure attribution，组合总分不能定位哪个 handoff 失效
<!-- delta:SF-2026-ARXIV-2606-21654:end -->

<!-- books-review:SF-2026-ARXIV-2606-21654:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21654v1 §6 Limitations`，只支持『compositional evaluation 应保存组件、组合、judge 与 failure attribution，组合总分不能定位哪个 handoff 失效』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21654:end -->

<!-- existing:SF-2026-ARXIV-2606-21666:start -->
`books/part-07-agent/82-multi-agent.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21666:end -->

<!-- delta:SF-2026-ARXIV-2606-21666:start -->
多 Agent 共识要保存独立 evidence、divergence 与 shared verification；重复采样的多数票不等于独立证明
<!-- delta:SF-2026-ARXIV-2606-21666:end -->

<!-- books-review:SF-2026-ARXIV-2606-21666:start -->
Unique owner `AGENT-MULTI-AGENT`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21666v1 §6.2 Limitations; §6.3 Contamination`，只支持『多 Agent 共识要保存独立 evidence、divergence 与 shared verification；重复采样的多数票不等于独立证明』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。共享状态或独立复核发生冲突时暂停 commit，回到单 Agent baseline 或串行 adjudication；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21666:end -->

<!-- existing:SF-2026-ARXIV-2606-21678:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21678:end -->

<!-- delta:SF-2026-ARXIV-2606-21678:start -->
从 internal representation 可解码出答案不证明 reasoning faithful；diagnostic ladder 要区分 decodability、causal use 与输出行为
<!-- delta:SF-2026-ARXIV-2606-21678:end -->

<!-- books-review:SF-2026-ARXIV-2606-21678:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21678v1 §6 Discussion: structural decodability-faithfulness gap`，只支持『从 internal representation 可解码出答案不证明 reasoning faithful；diagnostic ladder 要区分 decodability、causal use 与输出行为』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21678:end -->

<!-- existing:SF-2026-ARXIV-2606-21710:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21710:end -->

<!-- delta:SF-2026-ARXIV-2606-21710:start -->
社会行为安全评估必须绑定场景、规范、judge 与 policy optimization，合成 reward 改善不证明真实人群规范覆盖
<!-- delta:SF-2026-ARXIV-2606-21710:end -->

<!-- books-review:SF-2026-ARXIV-2606-21710:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21710v1 §6 Limitations (unnumbered list after Conclusion): synthetic scenarios, judge dependence, human heterogeneity, scale, deployment caution, norms and dual use`，只支持『社会行为安全评估必须绑定场景、规范、judge 与 policy optimization，合成 reward 改善不证明真实人群规范覆盖』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21710:end -->

<!-- existing:SF-2026-ARXIV-2606-21712:start -->
`books/part-05-inference-system/56-inference-scheduling.md` 已有 本章要回答的问题；相邻 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21712:end -->

<!-- delta:SF-2026-ARXIV-2606-21712:start -->
BatchGen 用 sequence coroutine 暴露生成状态并跨请求组装 batch；scheduler 必须拥有 coroutine lifecycle、fairness 与 memory backpressure
<!-- delta:SF-2026-ARXIV-2606-21712:end -->

<!-- books-review:SF-2026-ARXIV-2606-21712:start -->
Unique owner `INFER-SCHEDULING`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21712v1 §7 Limitations and Future Work`，只支持『BatchGen 用 sequence coroutine 暴露生成状态并跨请求组装 batch；scheduler 必须拥有 coroutine lifecycle、fairness 与 memory backpressure』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。估计失准或 SLO slack 耗尽时停止合批/迁移，回退到隔离队列与保守 admission；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21712:end -->

<!-- existing:SF-2026-ARXIV-2606-21732:start -->
`books/part-06-ai-infrastructure/72-security.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21732:end -->

<!-- delta:SF-2026-ARXIV-2606-21732:start -->
对 Agent/system 的组合攻击要显式建模 attacker capability、可见状态与 defense boundary；单点 sanitize 不等于 end-to-end containment
<!-- delta:SF-2026-ARXIV-2606-21732:end -->

<!-- books-review:SF-2026-ARXIV-2606-21732:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21732v1 §10 Conclusion; adaptive-adversary boundary`，只支持『对 Agent/system 的组合攻击要显式建模 attacker capability、可见状态与 defense boundary；单点 sanitize 不等于 end-to-end containment』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。威胁模型、challenge、taint 或 proof 边界不满足时 fail closed，并交给独立 reference monitor；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21732:end -->

<!-- existing:SF-2026-ARXIV-2606-21775:start -->
`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 已有 本章要回答的问题；相邻 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21775:end -->

<!-- delta:SF-2026-ARXIV-2606-21775:start -->
world-model rollout horizon 应成为按任务难度与不确定性调节的状态，而非训练/推理期固定常数
<!-- delta:SF-2026-ARXIV-2606-21775:end -->

<!-- books-review:SF-2026-ARXIV-2606-21775:start -->
Unique owner `MULTIMODAL-WORLD-MODELS`; adjacent non-owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21775v1 §5 Conclusion and evaluated task/horizon boundary`，只支持『world-model rollout horizon 应成为按任务难度与不确定性调节的状态，而非训练/推理期固定常数』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。identifiability、rollout uncertainty 或 horizon gate 失败时停止想象 rollout，交还真实环境观测；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21775:end -->

<!-- existing:SF-2026-ARXIV-2606-21777:start -->
`books/part-07-agent/76-rag.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/77-memory.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21777:end -->

<!-- delta:SF-2026-ARXIV-2606-21777:start -->
retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库
<!-- delta:SF-2026-ARXIV-2606-21777:end -->

<!-- books-review:SF-2026-ARXIV-2606-21777:start -->
Unique owner `AGENT-RAG`; adjacent non-owner `books/part-07-agent/77-memory.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21777v1 §5 Conclusion and model-scale/QA scope`，只支持『retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。evidence、index 或 verifier identity 不完整时 abstain/回到原始证据，不把生成结果写成事实；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21777:end -->

<!-- existing:SF-2026-ARXIV-2606-21787:start -->
`books/part-06-ai-infrastructure/59-model-registry.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/60-training-operator.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21787:end -->

<!-- delta:SF-2026-ARXIV-2606-21787:start -->
模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage
<!-- delta:SF-2026-ARXIV-2606-21787:end -->

<!-- books-review:SF-2026-ARXIV-2606-21787:start -->
Unique owner `PLATFORM-MODEL-REGISTRY`; adjacent non-owner `books/part-06-ai-infrastructure/60-training-operator.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21787v1 §8 Discussion and Implication`，只支持『模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。semantic fingerprint 冲突时禁止 promotion，以文件 hash、lineage 与部署 receipt 为准；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21787:end -->

<!-- existing:SF-2026-ARXIV-2606-21795:start -->
`books/part-04-training-system/31-rlhf.md` 已有 本章要回答的问题；相邻 `books/part-04-training-system/32-ppo.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21795:end -->

<!-- delta:SF-2026-ARXIV-2606-21795:start -->
reward clustering 应把异质 reward mode 分开优化并保存 cluster identity，聚合 scalar reward 会隐藏冲突偏好与 hacking
<!-- delta:SF-2026-ARXIV-2606-21795:end -->

<!-- books-review:SF-2026-ARXIV-2606-21795:start -->
Unique owner `TRAIN-RLHF`; adjacent non-owner `books/part-04-training-system/32-ppo.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21795v1 §5 Limitations`，只支持『reward clustering 应把异质 reward mode 分开优化并保存 cluster identity，聚合 scalar reward 会隐藏冲突偏好与 hacking』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。reward cluster 不稳定或冲突时停止 policy update，回到独立 evaluator 与人工 adjudication；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21795:end -->

<!-- existing:SF-2026-ARXIV-2606-21803:start -->
`books/part-02-model/22-long-context.md` 已有 本章要回答的问题；相邻 `books/part-02-model/21-moe.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21803:end -->

<!-- delta:SF-2026-ARXIV-2606-21803:start -->
TTT-NTP 在推理时用 next-token prediction 写入 fast weights；write scope、chunk boundary 与 reset policy 必须成为 context state
<!-- delta:SF-2026-ARXIV-2606-21803:end -->

<!-- books-review:SF-2026-ARXIV-2606-21803:start -->
Unique owner `MODEL-LONG-CONTEXT`; adjacent non-owner `books/part-02-model/21-moe.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.21803v1 §5 Conclusion and evaluated model/context boundary`，只支持『TTT-NTP 在推理时用 next-token prediction 写入 fast weights；write scope、chunk boundary 与 reset policy 必须成为 context state』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。fast-weight 写入越界或收益不稳时丢弃该请求的适配状态并回到冻结 base model；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21803:end -->

<!-- existing:SF-2026-ARXIV-2606-21804:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21804:end -->

<!-- delta:SF-2026-ARXIV-2606-21804:start -->
coding-Agent evaluation 应按 thread/issue 持久化多轮 context 与 side effects，单次 patch pass 会漏掉跨轮回归
<!-- delta:SF-2026-ARXIV-2606-21804:end -->

<!-- books-review:SF-2026-ARXIV-2606-21804:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21804v1 §6 Discussion and Limitations`，只支持『coding-Agent evaluation 应按 thread/issue 持久化多轮 context 与 side effects，单次 patch pass 会漏掉跨轮回归』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21804:end -->

<!-- existing:SF-2026-ARXIV-2606-21807:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有 本章要回答的问题；相邻 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21807:end -->

<!-- delta:SF-2026-ARXIV-2606-21807:start -->
规模变化会同时提高能力与稳定错误；evaluation 必须用 slice 与 uncertainty 分解 opposing forces 而非只报告均值
<!-- delta:SF-2026-ARXIV-2606-21807:end -->

<!-- books-review:SF-2026-ARXIV-2606-21807:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21807v1 §6 Analysis and Discussion; §7 Conclusion`，只支持『规模变化会同时提高能力与稳定错误；evaluation 必须用 slice 与 uncertainty 分解 opposing forces 而非只报告均值』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。metric、judge、threshold 或样本假设不成立时保持 Gate Open，回到独立复核而非放宽阈值；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21807:end -->

<!-- existing:SF-2026-ARXIV-2606-21811:start -->
`books/part-07-agent/80-reflection.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/81-workflow.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-21811:end -->

<!-- delta:SF-2026-ARXIV-2606-21811:start -->
critic-based self-improvement 要分离 critique quality、policy uptake 与最终 outcome，强 critic 也不证明 actor 会正确使用反馈
<!-- delta:SF-2026-ARXIV-2606-21811:end -->

<!-- books-review:SF-2026-ARXIV-2606-21811:start -->
Unique owner `AGENT-REFLECTION`; adjacent non-owner `books/part-07-agent/81-workflow.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.21811v1 §6 Discussion; Appendices E and G.4 fall-short cases`，只支持『critic-based self-improvement 要分离 critique quality、policy uptake 与最终 outcome，强 critic 也不证明 actor 会正确使用反馈』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。held-out 验证失败时拒绝 promotion，保留旧 skill/policy 与 candidate lesson 的分离状态；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-21811:end -->

<!-- existing:SF-2026-ARXIV-2606-28376:start -->
`books/part-07-agent/77-memory.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-28376:end -->

<!-- delta:SF-2026-ARXIV-2606-28376:start -->
OSU-Mem 将 observation、summary 与 update 分阶段持久化，并要求在多步任务中分别验证 construction、retrieval 与 action use
<!-- delta:SF-2026-ARXIV-2606-28376:end -->

<!-- books-review:SF-2026-ARXIV-2606-28376:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证据边界是 `arXiv:2606.28376v1 §7 Limitations; Appendix F no multi-step rollout note`，只支持『OSU-Mem 将 observation、summary 与 update 分阶段持久化，并要求在多步任务中分别验证 construction、retrieval 与 action use』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。写入、检索或来源证据不足时 hold/隔离 candidate memory，保留原始轨迹并禁止自动覆盖；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-28376:end -->

<!-- existing:SF-2026-ARXIV-2606-28379:start -->
`books/part-07-agent/81-workflow.md` 已有 本章要回答的问题；相邻 `books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-28379:end -->

<!-- delta:SF-2026-ARXIV-2606-28379:start -->
LEDGER 用显式 dependency graph 组织长期任务状态，retrieval 与 consistency repair 必须围绕同一 node/version identity
<!-- delta:SF-2026-ARXIV-2606-28379:end -->

<!-- books-review:SF-2026-ARXIV-2606-28379:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据边界是 `arXiv:2606.28379v1 §5 Conclusion and absence of a formal semantic guarantee`，只支持『LEDGER 用显式 dependency graph 组织长期任务状态，retrieval 与 consistency repair 必须围绕同一 node/version identity』在作者披露任务中的机制与结果；不证明未测试规模、分布、攻击者或生产尾部行为。transition、artifact 或 postcondition 无法验证时停在可恢复 checkpoint，执行 compensation 而非宣称完成；旧路径在其原假设成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-28379:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260620-COVERAGE-V1 | fresh-context:jun20-v1 | coverage | coverage:SRC-ARXIV:20260620 | — | 385/385 full semantic audit; 92/92 route-negative; denominator 65; closures 320; proposed-retained findings 2606.21451 and 2606.21749 closed pre-denominator | passed |
| SA-20260620-EVIDENCE-V1 | fresh-context:jun20-v1 | evidence | review:SF-2026-ARXIV-2606-21023; review:SF-2026-ARXIV-2606-21024; review:SF-2026-ARXIV-2606-21037; review:SF-2026-ARXIV-2606-21045; review:SF-2026-ARXIV-2606-21071; review:SF-2026-ARXIV-2606-21077; review:SF-2026-ARXIV-2606-21083; review:SF-2026-ARXIV-2606-21088; review:SF-2026-ARXIV-2606-21101; review:SF-2026-ARXIV-2606-21121; review:SF-2026-ARXIV-2606-21126; review:SF-2026-ARXIV-2606-21129; review:SF-2026-ARXIV-2606-21130; review:SF-2026-ARXIV-2606-21140; review:SF-2026-ARXIV-2606-21144; review:SF-2026-ARXIV-2606-21172; review:SF-2026-ARXIV-2606-21173; review:SF-2026-ARXIV-2606-21188; review:SF-2026-ARXIV-2606-21228; review:SF-2026-ARXIV-2606-21238; review:SF-2026-ARXIV-2606-21249; review:SF-2026-ARXIV-2606-21255; review:SF-2026-ARXIV-2606-21257; review:SF-2026-ARXIV-2606-21262; review:SF-2026-ARXIV-2606-21282; review:SF-2026-ARXIV-2606-21307; review:SF-2026-ARXIV-2606-21315; review:SF-2026-ARXIV-2606-21337; review:SF-2026-ARXIV-2606-21338; review:SF-2026-ARXIV-2606-21359; review:SF-2026-ARXIV-2606-21372; review:SF-2026-ARXIV-2606-21386; review:SF-2026-ARXIV-2606-21389; review:SF-2026-ARXIV-2606-21398; review:SF-2026-ARXIV-2606-21399; review:SF-2026-ARXIV-2606-21401; review:SF-2026-ARXIV-2606-21406; review:SF-2026-ARXIV-2606-21409; review:SF-2026-ARXIV-2606-21428; review:SF-2026-ARXIV-2606-21445; review:SF-2026-ARXIV-2606-21509; review:SF-2026-ARXIV-2606-21514; review:SF-2026-ARXIV-2606-21553; review:SF-2026-ARXIV-2606-21565; review:SF-2026-ARXIV-2606-21572; review:SF-2026-ARXIV-2606-21584; review:SF-2026-ARXIV-2606-21627; review:SF-2026-ARXIV-2606-21633; review:SF-2026-ARXIV-2606-21638; review:SF-2026-ARXIV-2606-21654; review:SF-2026-ARXIV-2606-21666; review:SF-2026-ARXIV-2606-21678; review:SF-2026-ARXIV-2606-21710; review:SF-2026-ARXIV-2606-21712; review:SF-2026-ARXIV-2606-21732; review:SF-2026-ARXIV-2606-21775; review:SF-2026-ARXIV-2606-21777; review:SF-2026-ARXIV-2606-21787; review:SF-2026-ARXIV-2606-21795; review:SF-2026-ARXIV-2606-21803; review:SF-2026-ARXIV-2606-21804; review:SF-2026-ARXIV-2606-21807; review:SF-2026-ARXIV-2606-21811; review:SF-2026-ARXIV-2606-28376; review:SF-2026-ARXIV-2606-28379 | — | 65/65 exact identities resolved; official HTML gaps for 2606.21173 and 2606.21282 recovered through linked author artifact and exact-identity author manuscript; 65 source-specific locator triples, benchmark contracts and non-proof/fallback boundaries; ordinary pending 0 | passed |
| SA-20260620-SELECTION-V1 | fresh-context:jun20-v1 | deep_analysis_selection | analysis:DA-20260620-REPRODUCIBLE-INFERENCE; analysis-decision:SF-2026-ARXIV-2606-21024; analysis-decision:SF-2026-ARXIV-2606-21037; analysis-decision:SF-2026-ARXIV-2606-21045; analysis-decision:SF-2026-ARXIV-2606-21071; analysis-decision:SF-2026-ARXIV-2606-21077; analysis-decision:SF-2026-ARXIV-2606-21083; analysis-decision:SF-2026-ARXIV-2606-21088; analysis-decision:SF-2026-ARXIV-2606-21101; analysis-decision:SF-2026-ARXIV-2606-21121; analysis-decision:SF-2026-ARXIV-2606-21126; analysis-decision:SF-2026-ARXIV-2606-21129; analysis-decision:SF-2026-ARXIV-2606-21130; analysis-decision:SF-2026-ARXIV-2606-21140; analysis-decision:SF-2026-ARXIV-2606-21144; analysis-decision:SF-2026-ARXIV-2606-21172; analysis-decision:SF-2026-ARXIV-2606-21173; analysis-decision:SF-2026-ARXIV-2606-21188; analysis-decision:SF-2026-ARXIV-2606-21228; analysis-decision:SF-2026-ARXIV-2606-21238; analysis-decision:SF-2026-ARXIV-2606-21249; analysis-decision:SF-2026-ARXIV-2606-21255; analysis-decision:SF-2026-ARXIV-2606-21257; analysis-decision:SF-2026-ARXIV-2606-21262; analysis-decision:SF-2026-ARXIV-2606-21282; analysis-decision:SF-2026-ARXIV-2606-21307; analysis-decision:SF-2026-ARXIV-2606-21315; analysis-decision:SF-2026-ARXIV-2606-21337; analysis-decision:SF-2026-ARXIV-2606-21338; analysis-decision:SF-2026-ARXIV-2606-21359; analysis-decision:SF-2026-ARXIV-2606-21372; analysis-decision:SF-2026-ARXIV-2606-21386; analysis-decision:SF-2026-ARXIV-2606-21389; analysis-decision:SF-2026-ARXIV-2606-21398; analysis:DA-20260620-CALIBRATION-CONTROL; analysis-decision:SF-2026-ARXIV-2606-21401; analysis-decision:SF-2026-ARXIV-2606-21406; analysis-decision:SF-2026-ARXIV-2606-21409; analysis-decision:SF-2026-ARXIV-2606-21428; analysis-decision:SF-2026-ARXIV-2606-21445; analysis-decision:SF-2026-ARXIV-2606-21509; analysis-decision:SF-2026-ARXIV-2606-21514; analysis-decision:SF-2026-ARXIV-2606-21553; analysis-decision:SF-2026-ARXIV-2606-21565; analysis-decision:SF-2026-ARXIV-2606-21572; analysis-decision:SF-2026-ARXIV-2606-21584; analysis-decision:SF-2026-ARXIV-2606-21627; analysis-decision:SF-2026-ARXIV-2606-21633; analysis-decision:SF-2026-ARXIV-2606-21638; analysis-decision:SF-2026-ARXIV-2606-21654; analysis-decision:SF-2026-ARXIV-2606-21666; analysis-decision:SF-2026-ARXIV-2606-21678; analysis-decision:SF-2026-ARXIV-2606-21710; analysis:DA-20260620-SEQUENCE-COROUTINE; analysis-decision:SF-2026-ARXIV-2606-21732; analysis-decision:SF-2026-ARXIV-2606-21775; analysis-decision:SF-2026-ARXIV-2606-21777; analysis-decision:SF-2026-ARXIV-2606-21787; analysis-decision:SF-2026-ARXIV-2606-21795; analysis-decision:SF-2026-ARXIV-2606-21803; analysis-decision:SF-2026-ARXIV-2606-21804; analysis-decision:SF-2026-ARXIV-2606-21807; analysis-decision:SF-2026-ARXIV-2606-21811; analysis-decision:SF-2026-ARXIV-2606-28376; analysis-decision:SF-2026-ARXIV-2606-28379 | — | 65/65 full frontier; three selected and 62 not_selected with contract-valid decisions and narrative refs | passed |
| SA-20260620-BOOKS-POSTWRITE-V1 | fresh-context:jun20-postwrite-v1 | books | books-review:SF-2026-ARXIV-2606-21023; books-review:SF-2026-ARXIV-2606-21024; books-review:SF-2026-ARXIV-2606-21037; books-review:SF-2026-ARXIV-2606-21045; books-review:SF-2026-ARXIV-2606-21071; books-review:SF-2026-ARXIV-2606-21077; books-review:SF-2026-ARXIV-2606-21083; books-review:SF-2026-ARXIV-2606-21088; books-review:SF-2026-ARXIV-2606-21101; books-review:SF-2026-ARXIV-2606-21121; books-review:SF-2026-ARXIV-2606-21126; books-review:SF-2026-ARXIV-2606-21129; books-review:SF-2026-ARXIV-2606-21130; books-review:SF-2026-ARXIV-2606-21140; books-review:SF-2026-ARXIV-2606-21144; books-review:SF-2026-ARXIV-2606-21172; books-review:SF-2026-ARXIV-2606-21173; books-review:SF-2026-ARXIV-2606-21188; books-review:SF-2026-ARXIV-2606-21228; books-review:SF-2026-ARXIV-2606-21238; books-review:SF-2026-ARXIV-2606-21249; books-review:SF-2026-ARXIV-2606-21255; books-review:SF-2026-ARXIV-2606-21257; books-review:SF-2026-ARXIV-2606-21262; books-review:SF-2026-ARXIV-2606-21282; books-review:SF-2026-ARXIV-2606-21307; books-review:SF-2026-ARXIV-2606-21315; books-review:SF-2026-ARXIV-2606-21337; books-review:SF-2026-ARXIV-2606-21338; books-review:SF-2026-ARXIV-2606-21359; books-review:SF-2026-ARXIV-2606-21372; books-review:SF-2026-ARXIV-2606-21386; books-review:SF-2026-ARXIV-2606-21389; books-review:SF-2026-ARXIV-2606-21398; books-review:SF-2026-ARXIV-2606-21399; books-review:SF-2026-ARXIV-2606-21401; books-review:SF-2026-ARXIV-2606-21406; books-review:SF-2026-ARXIV-2606-21409; books-review:SF-2026-ARXIV-2606-21428; books-review:SF-2026-ARXIV-2606-21445; books-review:SF-2026-ARXIV-2606-21509; books-review:SF-2026-ARXIV-2606-21514; books-review:SF-2026-ARXIV-2606-21553; books-review:SF-2026-ARXIV-2606-21565; books-review:SF-2026-ARXIV-2606-21572; books-review:SF-2026-ARXIV-2606-21584; books-review:SF-2026-ARXIV-2606-21627; books-review:SF-2026-ARXIV-2606-21633; books-review:SF-2026-ARXIV-2606-21638; books-review:SF-2026-ARXIV-2606-21654; books-review:SF-2026-ARXIV-2606-21666; books-review:SF-2026-ARXIV-2606-21678; books-review:SF-2026-ARXIV-2606-21710; books-review:SF-2026-ARXIV-2606-21712; books-review:SF-2026-ARXIV-2606-21732; books-review:SF-2026-ARXIV-2606-21775; books-review:SF-2026-ARXIV-2606-21777; books-review:SF-2026-ARXIV-2606-21787; books-review:SF-2026-ARXIV-2606-21795; books-review:SF-2026-ARXIV-2606-21803; books-review:SF-2026-ARXIV-2606-21804; books-review:SF-2026-ARXIV-2606-21807; books-review:SF-2026-ARXIV-2606-21811; books-review:SF-2026-ARXIV-2606-28376; books-review:SF-2026-ARXIV-2606-28379 | — | Prewrite comparison plus post-write audit passed: 44/44 Integrate families in exactly one expected owner with mechanism, failure/fallback, evidence boundary and exact-v1 Review note; 21/21 No Change propositions revalidated; owner/adjacent handoff 65/65; zero unresolved finding | passed |

## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- 63/65 used official `arXiv:<id>v1` HTML.
- `2606.21173v1`: official identity plus author project and linked reproduction repository; artifact title/arXiv link binds the method/evaluation to this family; no later revision claim used.
- `2606.21282v1`: official arXiv identity and DOI plus exact-title/author manuscript mirror supplied the body; mirror status does not prove peer review or expand beyond v1.
- Ordinary pending locator count: 0.

## 9. Recommended Action

- `Integrate`: root wrote 44/44 families into 19 unique owner files; every family passed the post-write semantic audit.
- `No Change — Existing Coverage`: 21/21 canonical propositions and non-proof/fallback boundaries were revalidated.
- Post-write fresh audit: 65/65 Passed, zero unresolved finding; Coverage Closed, Evidence Passed, Selection Passed, Books Passed; Completion Complete.

## 10. Repository Changes

- Added only the 2026-06-20 Daily, date-local source packet and `scripts/finalize_june20_v21.py`.
- Root serialized the shared Books writeback across 19 owner files. This lane only audited those changes and updated date-local files; it did not edit, stage, commit or push Books or `docs/LEARNING_STATE.md`.

## 11. Open Questions

- Which heterogeneous-hardware reproducibility threshold should become a production admission/SLO field rather than an offline benchmark?
- How should coroutine generation state be checkpointed across scheduler failure without duplicating output side effects?
- What evidence is sufficient to upgrade calibration telemetry into a bounded intervention policy?

## 12. Sources

- [Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL](https://arxiv.org/abs/2606.21023v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Negative Knowledge as Failure-aware Shared Memory for AutoResearch](https://arxiv.org/abs/2606.21024v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Honeyquest for LLMs: Rethinking Cyber Deception for AI Attackers](https://arxiv.org/abs/2606.21037v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [OVIG: Optimistic Verification of AI Training Integrity via Gradient Signals](https://arxiv.org/abs/2606.21045v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer](https://arxiv.org/abs/2606.21071v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [OTTER: A Red-Teaming System for Toxicity-Evading Jailbreak Prompt Optimization](https://arxiv.org/abs/2606.21077v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Coherence Under Commitment: Probing Generalization and Vacuous Memorization in LLM Logical Reasoning](https://arxiv.org/abs/2606.21083v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [MV-WAM: Manifold-Aware World Action Model with Value Augmentation](https://arxiv.org/abs/2606.21088v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [DPIFrame: A Dual-Level Parallelism Acceleration Framework for CTR Model Inference](https://arxiv.org/abs/2606.21101v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Answer Engineering: Local Trajectory Editing for Protocol-Constrained Decision Making in Large Language Models](https://arxiv.org/abs/2606.21121v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [What Accuracy and Gradient Cosine Miss: Evaluating Feedback Alignment via Scale Stability, Reference Validity, and Depth Utility](https://arxiv.org/abs/2606.21126v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents](https://arxiv.org/abs/2606.21129v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Learning Burst-Aware Early Warning Models for Capacity Stress under AI Workload Surges in Hyperscale Data Centers](https://arxiv.org/abs/2606.21130v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Matching Matters: A Fair Quality-Efficiency Benchmark for Command-Line Agents](https://arxiv.org/abs/2606.21140v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents](https://arxiv.org/abs/2606.21144v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving](https://arxiv.org/abs/2606.21172v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Inverting the Bellman Equation: From $Q$-Values to World Models](https://arxiv.org/abs/2606.21173v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Remember what you did?: Learning Behavioral Memories for Partially Observable Object Manipulation](https://arxiv.org/abs/2606.21188v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Sakana Fugu Technical Report](https://arxiv.org/abs/2606.21228v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Recency/Frequency Adaptive KV Caching for Large Language Model Serving](https://arxiv.org/abs/2606.21238v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Does RoPE Prevent or Degrade Retrieval Heads? A Mechanistic Analysis Across Model Families](https://arxiv.org/abs/2606.21249v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [SCOPE: Sequential Conformal Probing for Reliable OOD Rejection in LLM Services](https://arxiv.org/abs/2606.21255v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [An Empirical Study of openPangu Quantization on Ascend NPUs](https://arxiv.org/abs/2606.21257v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [ARCO: Adaptive Rubrics with Co-Evolution for Multi-Step LLM-Based Agents](https://arxiv.org/abs/2606.21262v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Differential Zonotopes for Verifying Global Robustness of DNNs](https://arxiv.org/abs/2606.21282v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Task-Differentiated Atomic Skill Expansion and Routing for Continual Learning Across Highly Heterogeneous Tasks](https://arxiv.org/abs/2606.21307v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Social World Model for Lifelong Social Intelligence](https://arxiv.org/abs/2606.21315v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams](https://arxiv.org/abs/2606.21337v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- ["What Happens Locally, Leaks Globally": Detecting Privacy Leakage Risks in MCP Servers](https://arxiv.org/abs/2606.21338v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs](https://arxiv.org/abs/2606.21359v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [NAC: Neural Action Codec for Vision-Language-Action Models](https://arxiv.org/abs/2606.21372v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models](https://arxiv.org/abs/2606.21386v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [From Production SIEM to Reusable Cybersecurity Artifacts](https://arxiv.org/abs/2606.21389v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [BIT-Nav: Brain-Inspired Trajectory Memory for Embodied Navigation](https://arxiv.org/abs/2606.21398v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention](https://arxiv.org/abs/2606.21399v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [SwarmX: Agentic Scheduling for Low-Latency Agentic Systems](https://arxiv.org/abs/2606.21401v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Robot Self-Improvement via Human-Video Dynamics Models](https://arxiv.org/abs/2606.21406v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents](https://arxiv.org/abs/2606.21409v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study](https://arxiv.org/abs/2606.21428v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [AutoRAS: Learning Robust Agentic Systems with Primitive Representations](https://arxiv.org/abs/2606.21445v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [A Stitch in Time Saves Nine: Preserving Policy Compatibility Under Perception Updates in End-to-End Autonomous Driving](https://arxiv.org/abs/2606.21509v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Towards Understanding the Power and Limits of the Muon Optimizer: A River-Valley Perspective](https://arxiv.org/abs/2606.21514v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Dissecting Agentic RAG: A Component Ablation for Multi-Hop QA with a Local 7B Model](https://arxiv.org/abs/2606.21553v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Composing Verifiable Conceptual Models via Building Blocks: Towards Design-Time Verification of Agentic AI Workflows](https://arxiv.org/abs/2606.21565v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Robot Critics that Sweat the Small Stuff](https://arxiv.org/abs/2606.21572v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [When EER Hides Deployment Failure: Auditing Threshold Transfer and Unlabeled Score Calibration for Speech Deepfake Detectors](https://arxiv.org/abs/2606.21584v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Counsel: A Meta-Evaluation Dataset for Agentic Tasks](https://arxiv.org/abs/2606.21627v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/abs/2606.21633v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs](https://arxiv.org/abs/2606.21638v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [ChainWorld: Composing Long-Horizon Desktop Workloads from Atomic OSWorld Tasks](https://arxiv.org/abs/2606.21654v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.21666v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Decodable but Not Faithful: Coupling Natural-Language Rationales to Programmatic Verifiers](https://arxiv.org/abs/2606.21678v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [PrivacyAlign: Contextual Privacy Alignment for LLM Agents](https://arxiv.org/abs/2606.21710v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [BatchGen: An Architecture for Scalable and Efficient Batch Inference](https://arxiv.org/abs/2606.21712v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Safe to Check, Unsafe to Use: Relinking at the Compression Boundary of LLM Agents](https://arxiv.org/abs/2606.21732v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning](https://arxiv.org/abs/2606.21775v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action and Learning in Knowledge-Intensive Tasks](https://arxiv.org/abs/2606.21777v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Towards Imputation of Pre-Trained Language Model Metadata using Semantic Fingerprinting](https://arxiv.org/abs/2606.21787v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Discretizing Reward Models](https://arxiv.org/abs/2606.21795v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Test-Time Training with Next-Token Prediction](https://arxiv.org/abs/2606.21803v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Is Agent Code Less Maintainable Than Human Code?](https://arxiv.org/abs/2606.21804v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Fixed RAG Compression Collapses Measured Reader Scaling](https://arxiv.org/abs/2606.21807v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Steer, Don't Solve: Training Small Critic Models for Large Code Agents](https://arxiv.org/abs/2606.21811v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [When Does Overlap Help? OSU-Mem and a Cell-Conditional Analysis of Trajectory Memory for LLM Agents](https://arxiv.org/abs/2606.28376v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval](https://arxiv.org/abs/2606.28379v1) — first-public（Asia/Shanghai）：2026-06-19；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。
