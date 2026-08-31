# Daily Research — 2026-06-23

**Research Date:** 2026-06-23

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-22 09:00:00 ～ 2026-06-23 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；586/586 registered identities 完成 title+abstract semantic screen；92-family exact-v1 Evidence、full-frontier Selection 与 Books post-write audit 保持 root-accepted state

**Status:** Complete — Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`

## Executive Summary

Beijing window [2026-06-22 09:00, 2026-06-23 09:00) contains 586 registered identities. Full 586/586 title+abstract review freezes 92 durable families and 494 family-specific closures (15.70%). Exact-v1 Evidence is complete for 92/92 official HTML identities; Selection compares all 92 and chooses three narrative units. Books comparison yields 58 Integrate and 34 No Change; root wrote all 58 Integrate families and the 92/92 post-write fresh audit passed with zero unresolved findings, so this date is Complete.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-23 |
| Window End | 2026-06-23 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Beijing Window | [2026-06-22 09:00, 2026-06-23 09:00) |
| Denominator ID | daily-v2.1:2026-06-23:a621afd4505ba8cf |
| Denominator Frozen At | 2026-08-30T00:20:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-22T09:00:00+08:00 | 2026-06-23T09:00:00+08:00 | 2026-08-30T00:20:00+08:00 | 40 frozen DataCite DOI-prefix snapshots; full Core + topic routes | checked | 586 | SF-2026-ARXIV-2606-22741; SF-2026-ARXIV-2606-22768; SF-2026-ARXIV-2606-22778; SF-2026-ARXIV-2606-22783; SF-2026-ARXIV-2606-22792; SF-2026-ARXIV-2606-22794; SF-2026-ARXIV-2606-22798; SF-2026-ARXIV-2606-22804; SF-2026-ARXIV-2606-22826; SF-2026-ARXIV-2606-22827; SF-2026-ARXIV-2606-22840; SF-2026-ARXIV-2606-22844; SF-2026-ARXIV-2606-22864; SF-2026-ARXIV-2606-22873; SF-2026-ARXIV-2606-22874; SF-2026-ARXIV-2606-22875; SF-2026-ARXIV-2606-22877; SF-2026-ARXIV-2606-22878; SF-2026-ARXIV-2606-22883; SF-2026-ARXIV-2606-22902; SF-2026-ARXIV-2606-22906; SF-2026-ARXIV-2606-22916; SF-2026-ARXIV-2606-22918; SF-2026-ARXIV-2606-22925; SF-2026-ARXIV-2606-22932; SF-2026-ARXIV-2606-22936; SF-2026-ARXIV-2606-22942; SF-2026-ARXIV-2606-22948; SF-2026-ARXIV-2606-22953; SF-2026-ARXIV-2606-22966; SF-2026-ARXIV-2606-22968; SF-2026-ARXIV-2606-22977; SF-2026-ARXIV-2606-22983; SF-2026-ARXIV-2606-23001; SF-2026-ARXIV-2606-23003; SF-2026-ARXIV-2606-23017; SF-2026-ARXIV-2606-23026; SF-2026-ARXIV-2606-23030; SF-2026-ARXIV-2606-23038; SF-2026-ARXIV-2606-23049; SF-2026-ARXIV-2606-23075; SF-2026-ARXIV-2606-23112; SF-2026-ARXIV-2606-23127; SF-2026-ARXIV-2606-23130; SF-2026-ARXIV-2606-23181; SF-2026-ARXIV-2606-23189; SF-2026-ARXIV-2606-23195; SF-2026-ARXIV-2606-23217; SF-2026-ARXIV-2606-23276; SF-2026-ARXIV-2606-23277; SF-2026-ARXIV-2606-23283; SF-2026-ARXIV-2606-23321; SF-2026-ARXIV-2606-23370; SF-2026-ARXIV-2606-23403; SF-2026-ARXIV-2606-23404; SF-2026-ARXIV-2606-23416; SF-2026-ARXIV-2606-23449; SF-2026-ARXIV-2606-23459; SF-2026-ARXIV-2606-23521; SF-2026-ARXIV-2606-23525; SF-2026-ARXIV-2606-23546; SF-2026-ARXIV-2606-23581; SF-2026-ARXIV-2606-23583; SF-2026-ARXIV-2606-23589; SF-2026-ARXIV-2606-23617; SF-2026-ARXIV-2606-23642; SF-2026-ARXIV-2606-23654; SF-2026-ARXIV-2606-23664; SF-2026-ARXIV-2606-23671; SF-2026-ARXIV-2606-23686; SF-2026-ARXIV-2606-23752; SF-2026-ARXIV-2606-23754; SF-2026-ARXIV-2606-23768; SF-2026-ARXIV-2606-23797; SF-2026-ARXIV-2606-23858; SF-2026-ARXIV-2606-23872; SF-2026-ARXIV-2606-23892; SF-2026-ARXIV-2606-23915; SF-2026-ARXIV-2606-23927; SF-2026-ARXIV-2606-23937; SF-2026-ARXIV-2606-23961; SF-2026-ARXIV-2606-23969; SF-2026-ARXIV-2606-23983; SF-2026-ARXIV-2606-23989; SF-2026-ARXIV-2606-24004; SF-2026-ARXIV-2606-24020; SF-2026-ARXIV-2606-24033; SF-2026-ARXIV-2606-24040; SF-2026-ARXIV-2606-24551; SF-2026-ARXIV-2606-24934; SF-2026-ARXIV-2606-28385; SF-2026-ARXIV-2606-28386 | pages=40; final_cursor=end; 586 unique identities | 2026-06-23T01:00:00Z | ../_sources/daily-20260623/screening-ledger.json; ../_sources/daily-20260623/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260623 | — |

<!-- coverage:SRC-ARXIV:20260623:start -->
Full 586/586 title+abstract audit: 404 Core, 60 keyword-routed and 122 route-negative; arithmetic 586 = 92 retained + 494 closures; retain rate 15.70%. Keyword routing supplied recall only. Route-negative retained=3; proposed-pool false positives closed=8.
<!-- coverage:SRC-ARXIV:20260623:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-22741 | arXiv:2606.22741v1 | paper-v1:2606.22741 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22741 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-22741 | yes |
| SF-2026-ARXIV-2606-22768 | arXiv:2606.22768v1 | paper-v1:2606.22768 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22768 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-22768 | yes |
| SF-2026-ARXIV-2606-22778 | arXiv:2606.22778v1 | paper-v1:2606.22778 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22778 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-22778 | yes |
| SF-2026-ARXIV-2606-22783 | arXiv:2606.22783v1 | paper-v1:2606.22783 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22783 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-22783 | yes |
| SF-2026-ARXIV-2606-22792 | arXiv:2606.22792v1 | paper-v1:2606.22792 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22792 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22792 | yes |
| SF-2026-ARXIV-2606-22794 | arXiv:2606.22794v1 | paper-v1:2606.22794 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22794 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-22794 | yes |
| SF-2026-ARXIV-2606-22798 | arXiv:2606.22798v1 | paper-v1:2606.22798 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22798 | self | — | new_in_window | MODEL-MOE | Integrate | books-review:SF-2026-ARXIV-2606-22798 | yes |
| SF-2026-ARXIV-2606-22804 | arXiv:2606.22804v1 | paper-v1:2606.22804 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22804 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-22804 | yes |
| SF-2026-ARXIV-2606-22826 | arXiv:2606.22826v1 | paper-v1:2606.22826 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22826 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-22826 | yes |
| SF-2026-ARXIV-2606-22827 | arXiv:2606.22827v1 | paper-v1:2606.22827 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22827 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-22827 | yes |
| SF-2026-ARXIV-2606-22840 | arXiv:2606.22840v1 | paper-v1:2606.22840 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22840 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-22840 | yes |
| SF-2026-ARXIV-2606-22844 | arXiv:2606.22844v1 | paper-v1:2606.22844 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22844 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-22844 | yes |
| SF-2026-ARXIV-2606-22864 | arXiv:2606.22864v1 | paper-v1:2606.22864 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22864 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22864 | yes |
| SF-2026-ARXIV-2606-22873 | arXiv:2606.22873v1 | paper-v1:2606.22873 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22873 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-22873 | yes |
| SF-2026-ARXIV-2606-22874 | arXiv:2606.22874v1 | paper-v1:2606.22874 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22874 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-22874 | yes |
| SF-2026-ARXIV-2606-22875 | arXiv:2606.22875v1 | paper-v1:2606.22875 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22875 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Integrate | books-review:SF-2026-ARXIV-2606-22875 | yes |
| SF-2026-ARXIV-2606-22877 | arXiv:2606.22877v1 | paper-v1:2606.22877 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22877 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22877 | yes |
| SF-2026-ARXIV-2606-22878 | arXiv:2606.22878v1 | paper-v1:2606.22878 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22878 | self | — | new_in_window | TRAIN-LORA | Integrate | books-review:SF-2026-ARXIV-2606-22878 | yes |
| SF-2026-ARXIV-2606-22883 | arXiv:2606.22883v1 | paper-v1:2606.22883 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22883 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-22883 | yes |
| SF-2026-ARXIV-2606-22902 | arXiv:2606.22902v1 | paper-v1:2606.22902 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22902 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-22902 | yes |
| SF-2026-ARXIV-2606-22906 | arXiv:2606.22906v1 | paper-v1:2606.22906 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22906 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-22906 | yes |
| SF-2026-ARXIV-2606-22916 | arXiv:2606.22916v1 | paper-v1:2606.22916 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22916 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-22916 | yes |
| SF-2026-ARXIV-2606-22918 | arXiv:2606.22918v1 | paper-v1:2606.22918 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22918 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22918 | yes |
| SF-2026-ARXIV-2606-22925 | arXiv:2606.22925v1 | paper-v1:2606.22925 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22925 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22925 | yes |
| SF-2026-ARXIV-2606-22932 | arXiv:2606.22932v1 | paper-v1:2606.22932 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22932 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-22932 | yes |
| SF-2026-ARXIV-2606-22936 | arXiv:2606.22936v1 | paper-v1:2606.22936 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22936 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22936 | yes |
| SF-2026-ARXIV-2606-22942 | arXiv:2606.22942v1 | paper-v1:2606.22942 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22942 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22942 | yes |
| SF-2026-ARXIV-2606-22948 | arXiv:2606.22948v1 | paper-v1:2606.22948 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22948 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-22948 | yes |
| SF-2026-ARXIV-2606-22953 | arXiv:2606.22953v1 | paper-v1:2606.22953 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22953 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-22953 | yes |
| SF-2026-ARXIV-2606-22966 | arXiv:2606.22966v1 | paper-v1:2606.22966 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22966 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-22966 | yes |
| SF-2026-ARXIV-2606-22968 | arXiv:2606.22968v1 | paper-v1:2606.22968 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22968 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2606-22968 | yes |
| SF-2026-ARXIV-2606-22977 | arXiv:2606.22977v1 | paper-v1:2606.22977 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22977 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22977 | yes |
| SF-2026-ARXIV-2606-22983 | arXiv:2606.22983v1 | paper-v1:2606.22983 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22983 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-22983 | yes |
| SF-2026-ARXIV-2606-23001 | arXiv:2606.23001v1 | paper-v1:2606.23001 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23001 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-23001 | yes |
| SF-2026-ARXIV-2606-23003 | arXiv:2606.23003v1 | paper-v1:2606.23003 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23003 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-23003 | yes |
| SF-2026-ARXIV-2606-23017 | arXiv:2606.23017v1 | paper-v1:2606.23017 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23017 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-23017 | yes |
| SF-2026-ARXIV-2606-23026 | arXiv:2606.23026v1 | paper-v1:2606.23026 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23026 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23026 | yes |
| SF-2026-ARXIV-2606-23030 | arXiv:2606.23030v1 | paper-v1:2606.23030 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23030 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23030 | yes |
| SF-2026-ARXIV-2606-23038 | arXiv:2606.23038v1 | paper-v1:2606.23038 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23038 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-23038 | yes |
| SF-2026-ARXIV-2606-23049 | arXiv:2606.23049v1 | paper-v1:2606.23049 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23049 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-23049 | yes |
| SF-2026-ARXIV-2606-23075 | arXiv:2606.23075v1 | paper-v1:2606.23075 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23075 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23075 | yes |
| SF-2026-ARXIV-2606-23112 | arXiv:2606.23112v1 | paper-v1:2606.23112 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23112 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-23112 | yes |
| SF-2026-ARXIV-2606-23127 | arXiv:2606.23127v1 | paper-v1:2606.23127 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23127 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23127 | yes |
| SF-2026-ARXIV-2606-23130 | arXiv:2606.23130v1 | paper-v1:2606.23130 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23130 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23130 | yes |
| SF-2026-ARXIV-2606-23181 | arXiv:2606.23181v1 | paper-v1:2606.23181 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23181 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-23181 | yes |
| SF-2026-ARXIV-2606-23189 | arXiv:2606.23189v1 | paper-v1:2606.23189 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23189 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23189 | yes |
| SF-2026-ARXIV-2606-23195 | arXiv:2606.23195v1 | paper-v1:2606.23195 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23195 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-23195 | yes |
| SF-2026-ARXIV-2606-23217 | arXiv:2606.23217v1 | paper-v1:2606.23217 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23217 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23217 | yes |
| SF-2026-ARXIV-2606-23276 | arXiv:2606.23276v1 | paper-v1:2606.23276 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23276 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23276 | yes |
| SF-2026-ARXIV-2606-23277 | arXiv:2606.23277v1 | paper-v1:2606.23277 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23277 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-23277 | yes |
| SF-2026-ARXIV-2606-23283 | arXiv:2606.23283v1 | paper-v1:2606.23283 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23283 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-23283 | yes |
| SF-2026-ARXIV-2606-23321 | arXiv:2606.23321v1 | paper-v1:2606.23321 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23321 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-23321 | yes |
| SF-2026-ARXIV-2606-23370 | arXiv:2606.23370v1 | paper-v1:2606.23370 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23370 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-23370 | yes |
| SF-2026-ARXIV-2606-23403 | arXiv:2606.23403v1 | paper-v1:2606.23403 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23403 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23403 | yes |
| SF-2026-ARXIV-2606-23404 | arXiv:2606.23404v1 | paper-v1:2606.23404 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23404 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23404 | yes |
| SF-2026-ARXIV-2606-23416 | arXiv:2606.23416v1 | paper-v1:2606.23416 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23416 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-23416 | yes |
| SF-2026-ARXIV-2606-23449 | arXiv:2606.23449v1 | paper-v1:2606.23449 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23449 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-23449 | yes |
| SF-2026-ARXIV-2606-23459 | arXiv:2606.23459v1 | paper-v1:2606.23459 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23459 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23459 | yes |
| SF-2026-ARXIV-2606-23521 | arXiv:2606.23521v1 | paper-v1:2606.23521 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23521 | self | — | new_in_window | INFER-DECODE | Integrate | books-review:SF-2026-ARXIV-2606-23521 | yes |
| SF-2026-ARXIV-2606-23525 | arXiv:2606.23525v1 | paper-v1:2606.23525 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23525 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-23525 | yes |
| SF-2026-ARXIV-2606-23546 | arXiv:2606.23546v1 | paper-v1:2606.23546 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23546 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2606-23546 | yes |
| SF-2026-ARXIV-2606-23581 | arXiv:2606.23581v1 | paper-v1:2606.23581 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23581 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-23581 | yes |
| SF-2026-ARXIV-2606-23583 | arXiv:2606.23583v1 | paper-v1:2606.23583 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23583 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23583 | yes |
| SF-2026-ARXIV-2606-23589 | arXiv:2606.23589v1 | paper-v1:2606.23589 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23589 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-23589 | yes |
| SF-2026-ARXIV-2606-23617 | arXiv:2606.23617v1 | paper-v1:2606.23617 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23617 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-23617 | yes |
| SF-2026-ARXIV-2606-23642 | arXiv:2606.23642v1 | paper-v1:2606.23642 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23642 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-23642 | yes |
| SF-2026-ARXIV-2606-23654 | arXiv:2606.23654v1 | paper-v1:2606.23654 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23654 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23654 | yes |
| SF-2026-ARXIV-2606-23664 | arXiv:2606.23664v1 | paper-v1:2606.23664 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23664 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23664 | yes |
| SF-2026-ARXIV-2606-23671 | arXiv:2606.23671v1 | paper-v1:2606.23671 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23671 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23671 | yes |
| SF-2026-ARXIV-2606-23686 | arXiv:2606.23686v1 | paper-v1:2606.23686 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23686 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-23686 | yes |
| SF-2026-ARXIV-2606-23752 | arXiv:2606.23752v1 | paper-v1:2606.23752 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23752 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-23752 | yes |
| SF-2026-ARXIV-2606-23754 | arXiv:2606.23754v1 | paper-v1:2606.23754 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23754 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23754 | yes |
| SF-2026-ARXIV-2606-23768 | arXiv:2606.23768v1 | paper-v1:2606.23768 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23768 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23768 | yes |
| SF-2026-ARXIV-2606-23797 | arXiv:2606.23797v1 | paper-v1:2606.23797 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23797 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-23797 | yes |
| SF-2026-ARXIV-2606-23858 | arXiv:2606.23858v1 | paper-v1:2606.23858 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23858 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23858 | yes |
| SF-2026-ARXIV-2606-23872 | arXiv:2606.23872v1 | paper-v1:2606.23872 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23872 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23872 | yes |
| SF-2026-ARXIV-2606-23892 | arXiv:2606.23892v1 | paper-v1:2606.23892 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23892 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23892 | yes |
| SF-2026-ARXIV-2606-23915 | arXiv:2606.23915v1 | paper-v1:2606.23915 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23915 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23915 | yes |
| SF-2026-ARXIV-2606-23927 | arXiv:2606.23927v1 | paper-v1:2606.23927 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23927 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23927 | yes |
| SF-2026-ARXIV-2606-23937 | arXiv:2606.23937v1 | paper-v1:2606.23937 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23937 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23937 | yes |
| SF-2026-ARXIV-2606-23961 | arXiv:2606.23961v1 | paper-v1:2606.23961 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23961 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-23961 | yes |
| SF-2026-ARXIV-2606-23969 | arXiv:2606.23969v1 | paper-v1:2606.23969 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23969 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-23969 | yes |
| SF-2026-ARXIV-2606-23983 | arXiv:2606.23983v1 | paper-v1:2606.23983 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23983 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-23983 | yes |
| SF-2026-ARXIV-2606-23989 | arXiv:2606.23989v1 | paper-v1:2606.23989 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23989 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23989 | yes |
| SF-2026-ARXIV-2606-24004 | arXiv:2606.24004v1 | paper-v1:2606.24004 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24004 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-24004 | yes |
| SF-2026-ARXIV-2606-24020 | arXiv:2606.24020v1 | paper-v1:2606.24020 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24020 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24020 | yes |
| SF-2026-ARXIV-2606-24033 | arXiv:2606.24033v1 | paper-v1:2606.24033 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24033 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-24033 | yes |
| SF-2026-ARXIV-2606-24040 | arXiv:2606.24040v1 | paper-v1:2606.24040 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24040 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-24040 | yes |
| SF-2026-ARXIV-2606-24551 | arXiv:2606.24551v1 | paper-v1:2606.24551 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24551 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-24551 | yes |
| SF-2026-ARXIV-2606-24934 | arXiv:2606.24934v1 | paper-v1:2606.24934 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24934 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24934 | yes |
| SF-2026-ARXIV-2606-28385 | arXiv:2606.28385v1 | paper-v1:2606.28385 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28385 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-28385 | yes |
| SF-2026-ARXIV-2606-28386 | arXiv:2606.28386v1 | paper-v1:2606.28386 | 2026-W26 | 2026-06-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28386 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-28386 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-22741 | RP-f516297468e72da3 | deep | arXiv:2606.22741v1 | SRC-ARXIV@arXiv:2606.22741v1 | arXiv:2606.22741v1 — §2.2 The Formal Class; §Appendix A Formal Class and Subsumption; §A.1 The Formal Tuple and Recovery Maps | arXiv:2606.22741v1 — §E.2 The Limits of the Localization Result | arXiv:2606.22741v1 — §3 Two Layers, Two Failure Modes; §3.1 The Two Layers and Their Failure Modes; §4.1 Dependency Structure Predicts Failure Within a Corpus | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22741 | complete |
| SF-2026-ARXIV-2606-22768 | RP-c26bab5368b493d2 | deep | arXiv:2606.22768v1 | SRC-ARXIV@arXiv:2606.22768v1 | arXiv:2606.22768v1 — §5.1 Training experiments; §Appendix A Factored Gossip DiLoCo: Detailed Algorithm | arXiv:2606.22768v1 — §Appendix E Consensus Error Result and Proof | arXiv:2606.22768v1 — §7 Conclusion and Future Work; §Appendix C Further Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22768 | complete |
| SF-2026-ARXIV-2606-22778 | RP-fb1fc7eeb5fd9dbb | deep | arXiv:2606.22778v1 | SRC-ARXIV@arXiv:2606.22778v1 | arXiv:2606.22778v1 — §Lightweight evaluation and Nano-set construction; §Design of HAKARI-Bench; §Appendix A Nano-set construction and dataset list | arXiv:2606.22778v1 — §HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions; §Retrieval evaluation benchmarks and retrieval architectures; §Lightweight evaluation and Nano-set construction | arXiv:2606.22778v1 — §Discussion; §Scope of evaluated models; §Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22778 | complete |
| SF-2026-ARXIV-2606-22783 | RP-594e643a62fcaeee | deep | arXiv:2606.22783v1 | SRC-ARXIV@arXiv:2606.22783v1 | arXiv:2606.22783v1 — §3 Method; §A.4 The Dilemma of Construction and Verification; §A.4.1 Construction Difficulty | arXiv:2606.22783v1 — §Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints; §3.1 Evaluation Paradox; §3.3 Asymptotic Analysis | arXiv:2606.22783v1 — §5 Conclusion; §A.6 Conclusion: Returning to the Origin of Difficulty; §C.8 Conclusion: Validating Computational Irreducibility | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22783 | complete |
| SF-2026-ARXIV-2606-22792 | RP-995ba6d24abc9130 | deep | arXiv:2606.22792v1 | SRC-ARXIV@arXiv:2606.22792v1 | arXiv:2606.22792v1 — §2.4 Training Necessity; §Full training. | arXiv:2606.22792v1 — §2.6 Evaluation; §Appendix A Evaluation Ranking | arXiv:2606.22792v1 — §Future issues. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22792 | complete |
| SF-2026-ARXIV-2606-22794 | RP-d16675d09c026c4e | deep | arXiv:2606.22794v1 | SRC-ARXIV@arXiv:2606.22794v1 | arXiv:2606.22794v1 — §UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models; §3 Method; §3.2 Framework | arXiv:2606.22794v1 — §Appendix 0.B More Analysis | arXiv:2606.22794v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22794 | complete |
| SF-2026-ARXIV-2606-22798 | RP-04749ff230474928 | deep | arXiv:2606.22798v1 | SRC-ARXIV@arXiv:2606.22798v1 | arXiv:2606.22798v1 — §Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control; §MoE routing.; §3 Analysis of Anchor-Conditioned Routing | arXiv:2606.22798v1 — §3 Analysis of Anchor-Conditioned Routing; §5.3 Analysis | arXiv:2606.22798v1 — §7 Conclusion; §A.13 Failure case studies | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22798 | complete |
| SF-2026-ARXIV-2606-22804 | RP-875edde726607f37 | deep | arXiv:2606.22804v1 | SRC-ARXIV@arXiv:2606.22804v1 | arXiv:2606.22804v1 — §2.1 System Overview; §2.3 Cloud Server: Decoupled Management and Reasoning Architecture | arXiv:2606.22804v1 — §3 Experiment; §3.3 Diagnostic Experiment; §3.4 Qualitative Analysis | arXiv:2606.22804v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22804 | complete |
| SF-2026-ARXIV-2606-22826 | RP-12fc879a5729f993 | deep | arXiv:2606.22826v1 | SRC-ARXIV@arXiv:2606.22826v1 | arXiv:2606.22826v1 — §3 Method; §3.3 Subset Construction | arXiv:2606.22826v1 — §MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration; §Appendix D Threshold Sensitivity Analysis; §Appendix E GPU Evaluation Speedup Breakdown | arXiv:2606.22826v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22826 | complete |
| SF-2026-ARXIV-2606-22827 | RP-50ebdc7db7c00cf5 | deep | arXiv:2606.22827v1 | SRC-ARXIV@arXiv:2606.22827v1 | arXiv:2606.22827v1 — §What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security; §2.3 Memory Analysis of Python; §5.3 Dependency Graph Construction | arXiv:2606.22827v1 — §2.3 Memory Analysis of Python; §5.3.1 Module Structure Analysis; §5.3.2 Bytecode Analysis | arXiv:2606.22827v1 — §7 Limitations and Future Work; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22827 | complete |
| SF-2026-ARXIV-2606-22840 | RP-15b2c2cd8ef6cf13 | deep | arXiv:2606.22840v1 | SRC-ARXIV@arXiv:2606.22840v1 | arXiv:2606.22840v1 — §2.2 LLM Cascade and Routing; §3 System Design; §3.1 Architecture Overview | arXiv:2606.22840v1 — §4 Evaluation; §4.6 Extended Engineering Benchmark; §4.7 Case Study: Cost Inversion on mteb-retrieve | arXiv:2606.22840v1 — §6 Discussion; §6.4 Cross-Provider Failure Modes; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22840 | complete |
| SF-2026-ARXIV-2606-22844 | RP-964046e0776206ed | deep | arXiv:2606.22844v1 | SRC-ARXIV@arXiv:2606.22844v1 | arXiv:2606.22844v1 — §RaMem: Contextual Reinstatement for Long-term Agentic Memory; §3 Method; §3.1 Episodic Memory Anchoring | arXiv:2606.22844v1 — §4.3 Context Collapse Analysis; §4.5 Hyper-parameter Analysis; §4.6 Component Analysis | arXiv:2606.22844v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22844 | complete |
| SF-2026-ARXIV-2606-22864 | RP-81e007cd851e8755 | deep | arXiv:2606.22864v1 | SRC-ARXIV@arXiv:2606.22864v1 | arXiv:2606.22864v1 — §When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents; §3. Evaluation protocol; §3.1. Threat model and estimands | arXiv:2606.22864v1 — §When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents; §A cautionary case study.; §3. Evaluation protocol | arXiv:2606.22864v1 — §Threat model (in scope vs. out of scope).; §Two failure-mode flags.; §6. Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22864 | complete |
| SF-2026-ARXIV-2606-22873 | RP-15a37f4f18aac4af | deep | arXiv:2606.22873v1 | SRC-ARXIV@arXiv:2606.22873v1 | arXiv:2606.22873v1 — §2 Method; §2.3.3 Dynamic Rule Data Construction; §2.3.4 Chain-of-Thought Reasoning Data Construction | arXiv:2606.22873v1 — §3.2 Benchmark Composition and Statistics; §4.1 Evaluation Setup; §4.7 Dynamic Policy Evaluation | arXiv:2606.22873v1 — §6 Conclusion; §C.4 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22873 | complete |
| SF-2026-ARXIV-2606-22874 | RP-63157a3dbb17bde1 | deep | arXiv:2606.22874v1 | SRC-ARXIV@arXiv:2606.22874v1 | arXiv:2606.22874v1 — §SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers; §Method; §2.1 Selector architecture | arXiv:2606.22874v1 — §Evaluation.; §Analysis and ablations; §Empirical shape gap. | arXiv:2606.22874v1 — §Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22874 | complete |
| SF-2026-ARXIV-2606-22875 | RP-67c2e24d486c837e | deep | arXiv:2606.22875v1 | SRC-ARXIV@arXiv:2606.22875v1 | arXiv:2606.22875v1 — §3.1 FedOT Framework; §3.2 Watermark Design and Training; §0.A.1 Federated LDMs and Threat Model | arXiv:2606.22875v1 — §0.C.2 Analysis of LVT | arXiv:2606.22875v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22875 | complete |
| SF-2026-ARXIV-2606-22877 | RP-a9a5c89d9c46fa2d | deep | arXiv:2606.22877v1 | SRC-ARXIV@arXiv:2606.22877v1 | arXiv:2606.22877v1 — §DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings; §4.3 Evaluation Protocol and Metrics; §Appendix B Base User Profile Schema and Construction | arXiv:2606.22877v1 — §DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings; §4 DynamicMem Benchmark; §4.1 Checkpoint-Based Evaluation and Dataset Statistics | arXiv:2606.22877v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22877 | complete |
| SF-2026-ARXIV-2606-22878 | RP-3b28872fce79dad7 | deep | arXiv:2606.22878v1 | SRC-ARXIV@arXiv:2606.22878v1 | arXiv:2606.22878v1 — §Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning Thanks: N. Yang, Y. He, S. Wang, and C. Yin are with the Beijing Laboratory of Advanced Information Network, and the Beijing Key Laboratory of Network System Architecture and Convergence, Beijing University of Posts and Telecommunications, Beijing 100876, China (emails: {yangnuocheng, heyechen, sihuawang, ccyin}@bupt.edu.cn). Thanks: Z. Chen and T. Q. S. Quek are with the Information Systems Technology and Design Pillar, Singapore University of Technology and Design, 487372, Singapore (emails: zihan_chen@mymail.sutd.edu.sg, tonyquek@sutd.edu.sg).; §III System Model and Problem Formulation; §III-A Dynamic Decentralized LoRA System | arXiv:2606.22878v1 — §IV Problem Analysis and Proposed Method; §IV-B Correction Gap Analysis under DGD; §V-C Ablation Study | arXiv:2606.22878v1 — §VI Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22878 | complete |
| SF-2026-ARXIV-2606-22883 | RP-44b1362986d0f175 | deep | arXiv:2606.22883v1 | SRC-ARXIV@arXiv:2606.22883v1 | arXiv:2606.22883v1 — §3 Method; §3.2 Task Blueprint Construction; §3.4 Test Construction and Executable Filtering | arXiv:2606.22883v1 — §4.3 Scaling Analysis; §4.4.1 Cross-benchmark transfer; §4.5 Error Study | arXiv:2606.22883v1 — §5 Conclusion; §Appendix C Failure Mode Examples | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22883 | complete |
| SF-2026-ARXIV-2606-22902 | RP-4959a607aa340811 | deep | arXiv:2606.22902v1 | SRC-ARXIV@arXiv:2606.22902v1 | arXiv:2606.22902v1 — §Agent-as-a-Router: Agentic Model Routing for Coding Tasks; §3.4 Decomposed Routing Policies; §4.1 Benchmark Construction | arXiv:2606.22902v1 — §4.1 Benchmark Construction; §5 Empirical Validation; §Appendix B Benchmark and Setup Details | arXiv:2606.22902v1 — §5.3 Discussion; §6 Conclusion; §Appendix E Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22902 | complete |
| SF-2026-ARXIV-2606-22906 | RP-44be70336d42cb41 | deep | arXiv:2606.22906v1 | SRC-ARXIV@arXiv:2606.22906v1 | arXiv:2606.22906v1 — §III-B Repository Representation and Overall Framework; §III-E Metadata-First Context Construction; §IV-C Evaluation Protocol | arXiv:2606.22906v1 — §Benchmarks and evaluation scenarios.; §IV-C Evaluation Protocol; §IV-F Ablation Study: Where Do the Gains Come From? | arXiv:2606.22906v1 — §Practical scope of comparison.; §IV-J Discussion of Error Modes and Scope; §V Threats to Validity | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22906 | complete |
| SF-2026-ARXIV-2606-22916 | RP-a8097719f92770b3 | deep | arXiv:2606.22916v1 | SRC-ARXIV@arXiv:2606.22916v1 | arXiv:2606.22916v1 — §I-A Relationship to OpenPort Protocol; §IV Threat Model; §IV-A System Boundary | arXiv:2606.22916v1 — §X Evaluation Design; §X-F Expected Analysis Without Fabricated Results; §X-I First-Batch External Benchmark Adaptation | arXiv:2606.22916v1 — §IV-E Out of Scope; §XI Limitations and Threats to Validity; §XII-H Effect Estimation and Conservative Failure | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22916 | complete |
| SF-2026-ARXIV-2606-22918 | RP-2f7f3e0cfb77808f | deep | arXiv:2606.22918v1 | SRC-ARXIV@arXiv:2606.22918v1 | arXiv:2606.22918v1 — §3 The JudgeFit Pipeline; §3.2 Seed: Open Annotation and Clustering; §3.3 Refine: Diagnosis-Guided Editing | arXiv:2606.22918v1 — §5 Experiments; §5.1 Refinement Improves Every VLM; §5.2 Convergence and Generalization | arXiv:2606.22918v1 — §6 Profiling VLM Judges; §6.2 Bias and Discrimination Across Judges; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22918 | complete |
| SF-2026-ARXIV-2606-22925 | RP-43f83a5e2722d40f | deep | arXiv:2606.22925v1 | SRC-ARXIV@arXiv:2606.22925v1 | arXiv:2606.22925v1 — §EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction; §A.1 Broader Database and Benchmark-Construction Scale; §A.3 Execution-validation Dataset Subset and Training Context | arXiv:2606.22925v1 — §EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction; §4 Benchmark Corpus; §A.1 Broader Database and Benchmark-Construction Scale | arXiv:2606.22925v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22925 | complete |
| SF-2026-ARXIV-2606-22932 | RP-b85a64efc17e46f3 | deep | arXiv:2606.22932v1 | SRC-ARXIV@arXiv:2606.22932v1 | arXiv:2606.22932v1 — §FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training; §Our approach.; §2 Method | arXiv:2606.22932v1 — §Appendix E Measurement protocol and variance | arXiv:2606.22932v1 — §5 Conclusion; §Scope of the optimizer sweep. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22932 | complete |
| SF-2026-ARXIV-2606-22936 | RP-42609933e2cc89d8 | deep | arXiv:2606.22936v1 | SRC-ARXIV@arXiv:2606.22936v1 | arXiv:2606.22936v1 — §3 Method; §4.6 Cross-architecture validation on HotpotQA | arXiv:2606.22936v1 — §4.7 Cross-benchmark generalization on Llama: StrategyQA; §Appendix A Preliminary steering experiment; §Appendix L StrategyQA cross-benchmark results | arXiv:2606.22936v1 — §5 Discussion; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22936 | complete |
| SF-2026-ARXIV-2606-22942 | RP-f667f2b3ab20b93b | deep | arXiv:2606.22942v1 | SRC-ARXIV@arXiv:2606.22942v1 | arXiv:2606.22942v1 — §Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails; §3 Post-Training KD for LLMs; §3.2 Knowledge Distillation Method | arXiv:2606.22942v1 — §Dataset and Evaluation Tasks; §3.5 Results and Analysis; §4.2 KD Results and Analysis in Domain-Specific Tasks | arXiv:2606.22942v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22942 | complete |
| SF-2026-ARXIV-2606-22948 | RP-08b27b6d92523fc2 | deep | arXiv:2606.22948v1 | SRC-ARXIV@arXiv:2606.22948v1 | arXiv:2606.22948v1 — §5.1 Experimental protocol; §Appendix C Evaluation pool construction | arXiv:2606.22948v1 — §4.3 Train/evaluation split; §Appendix C Evaluation pool construction | arXiv:2606.22948v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22948 | complete |
| SF-2026-ARXIV-2606-22953 | RP-44244b3e6ec7ddff | deep | arXiv:2606.22953v1 | SRC-ARXIV@arXiv:2606.22953v1 | arXiv:2606.22953v1 — §3 Method | arXiv:2606.22953v1 — §5.3 Lag Analysis: Early Warning; §A.2 Probe Validity Controls and Leakage Analysis; §A.8 Intervention Sweeps and Head-Level Analysis | arXiv:2606.22953v1 — §9 Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22953 | complete |
| SF-2026-ARXIV-2606-22966 | RP-61afcde5cbd21cf9 | deep | arXiv:2606.22966v1 | SRC-ARXIV@arXiv:2606.22966v1 | arXiv:2606.22966v1 — §3 Threat Model; §4 Method; §6 Mechanism: off-manifold is intrinsic to corrupting imagination | arXiv:2606.22966v1 — §5 Experiments; §5.1 Setup: three targets spanning the imagination-action coupling; §5.7 Adaptive attacker: the defense holds | arXiv:2606.22966v1 — §7 The task-level null, and why it motivates the oracle threat; §8 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22966 | complete |
| SF-2026-ARXIV-2606-22968 | RP-b48832a22a05705b | deep | arXiv:2606.22968v1 | SRC-ARXIV@arXiv:2606.22968v1 | arXiv:2606.22968v1 — §MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference; §3.1 Memory Imbalance Limits Feasible Sequence Length; §4 MOCAP Framework | arXiv:2606.22968v1 — §5 Evaluation | arXiv:2606.22968v1 — §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22968 | complete |
| SF-2026-ARXIV-2606-22977 | RP-c985e96a560bfd60 | deep | arXiv:2606.22977v1 | SRC-ARXIV@arXiv:2606.22977v1 | arXiv:2606.22977v1 — §StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs | arXiv:2606.22977v1 — §StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs; §3 The StatABench Benchmark; §3.4 Annotations and Evaluation | arXiv:2606.22977v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22977 | complete |
| SF-2026-ARXIV-2606-22983 | RP-4461d5205b53a3b8 | deep | arXiv:2606.22983v1 | SRC-ARXIV@arXiv:2606.22983v1 | arXiv:2606.22983v1 — §3. OmniCast Architecture | arXiv:2606.22983v1 — §7. Experimental Evaluation; §7.1. Experiment Settings; §7.3. Analysis | arXiv:2606.22983v1 — §9. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-22983 | complete |
| SF-2026-ARXIV-2606-23001 | RP-9aa451be6e32ed7d | deep | arXiv:2606.23001v1 | SRC-ARXIV@arXiv:2606.23001v1 | arXiv:2606.23001v1 — §4. Design of EnerInfer | arXiv:2606.23001v1 — §6.3. Thermal-aware controller evaluation | arXiv:2606.23001v1 — §4.6. Discussion; §8. Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23001 | complete |
| SF-2026-ARXIV-2606-23003 | RP-637247e90ace2db2 | deep | arXiv:2606.23003v1 | SRC-ARXIV@arXiv:2606.23003v1 | arXiv:2606.23003v1 — §VCT: A Verifiable Transcript System for LLM Conversations; §3.2 System State and Storage Model; §3.4 Threat Model and Security Goals | arXiv:2606.23003v1 — §4.4 Security Analysis; §5 Experimental Evaluation; §5.1 Prototype System and Evaluation Scope | arXiv:2606.23003v1 — §5.1 Prototype System and Evaluation Scope; §5.8 Experimental Discussion; §6 Discussion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23003 | complete |
| SF-2026-ARXIV-2606-23017 | RP-673501fb5656191c | deep | arXiv:2606.23017v1 | SRC-ARXIV@arXiv:2606.23017v1 | arXiv:2606.23017v1 — §Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems; §3.1 System Architecture and Role Definition; §3.2 Threat Model and Design Objectives | arXiv:2606.23017v1 — §5 Experiments and Analysis; §5.1.2 Evaluation Metrics; §5.3 Experimental Results and Analysis | arXiv:2606.23017v1 — §2.2 Trust Crisis: Failure of the Semi-Honest Assumption; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23017 | complete |
| SF-2026-ARXIV-2606-23026 | RP-840115ca37e2579b | deep | arXiv:2606.23026v1 | SRC-ARXIV@arXiv:2606.23026v1 | arXiv:2606.23026v1 — §A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees; §3 Payoff Design; §6.4 Training Procedure | arXiv:2606.23026v1 — §4.1 Empirical Backward Induction; §9 Passive Shadow Evaluation Protocol; §10 Experimental Evaluation | arXiv:2606.23026v1 — §2.4 Modeling Scope and Assumptions; §11 Discussion; §14 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23026 | complete |
| SF-2026-ARXIV-2606-23030 | RP-fa051686e789dd52 | deep | arXiv:2606.23030v1 | SRC-ARXIV@arXiv:2606.23030v1 | arXiv:2606.23030v1 — §IV Method; §IV-C Interrogation-specific Prompt Construction | arXiv:2606.23030v1 — §IV-B Theoretical Analysis; §V Evaluation; §V-B 2 Effectiveness Analysis of Different Interrogation Strategies | arXiv:2606.23030v1 — §VI Discussion; §VIII Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23030 | complete |
| SF-2026-ARXIV-2606-23038 | RP-bf8a8e0c18da7cd7 | deep | arXiv:2606.23038v1 | SRC-ARXIV@arXiv:2606.23038v1 | arXiv:2606.23038v1 — §4.1 Dual-LoRA Architecture; §4.4 Co-Evolutionary Training; §Appendix A EvoRubrics Algorithm | arXiv:2606.23038v1 — §2.2 Dynamic Rubrics and Adaptive Evaluation; §Appendix C Evaluation Details; §C.1 Policy LLM Evaluation | arXiv:2606.23038v1 — §6 Conclusions and Future Work; §E.3 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23038 | complete |
| SF-2026-ARXIV-2606-23049 | RP-d0afbe1a79e0865f | deep | arXiv:2606.23049v1 | SRC-ARXIV@arXiv:2606.23049v1 | arXiv:2606.23049v1 — §3 Method; §3.5 Training Recipe; §4.2 Evaluation Protocol | arXiv:2606.23049v1 — §4.2 Evaluation Protocol | arXiv:2606.23049v1 — §7 Discussion and Limitations; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23049 | complete |
| SF-2026-ARXIV-2606-23075 | RP-cd4a92f567ac3a11 | deep | arXiv:2606.23075v1 | SRC-ARXIV@arXiv:2606.23075v1 | arXiv:2606.23075v1 — §2.3.1. Threat Model; §4. Cognitive Resource: Memory; §4.1. Bootstrap: Initial Memory | arXiv:2606.23075v1 — §3.3. Evaluate: Evaluation Oracle; §5.3. Selection: Tool Efficacy Evaluation; §6.3. Evaluate: Variant Fitness Evaluation | arXiv:2606.23075v1 — §10. Conclusion and Future Directions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23075 | complete |
| SF-2026-ARXIV-2606-23112 | RP-9070b605c1e402ea | deep | arXiv:2606.23112v1 | SRC-ARXIV@arXiv:2606.23112v1 | arXiv:2606.23112v1 — §4. Method; §4.1. Overall Architecture; §4.2.1. Graph Construction and Edge Weights | arXiv:2606.23112v1 — §5.3. Error Analysis; §5.5. DPO Training Analysis | arXiv:2606.23112v1 — §6. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23112 | complete |
| SF-2026-ARXIV-2606-23127 | RP-7861fd9830c06b4d | deep | arXiv:2606.23127v1 | SRC-ARXIV@arXiv:2606.23127v1 | arXiv:2606.23127v1 — §Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation; §2.1 Benchmark Design; §2.2 Benchmark Construction | arXiv:2606.23127v1 — §Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation; §2 AFTER : A Benchmark for Skill Transfer; §2.1 Benchmark Design | arXiv:2606.23127v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23127 | complete |
| SF-2026-ARXIV-2606-23130 | RP-0dd2a5b576edcb53 | deep | arXiv:2606.23130v1 | SRC-ARXIV@arXiv:2606.23130v1 | arXiv:2606.23130v1 — §III Dataset Construction; §III-B1 Multi-Agent Code Auditing; §III-B2 Vulnerability Deduplication and Validation | arXiv:2606.23130v1 — §IV RQ.1; §V RQ.2; §VI RQ.3; §VII RQ4 | arXiv:2606.23130v1 — §VIII Discussion; §VIII-A Sources of Insecurity; §VIII-B Implications for Mitigation | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23130 | complete |
| SF-2026-ARXIV-2606-23181 | RP-1e1f4737f14f05e6 | deep | arXiv:2606.23181v1 | SRC-ARXIV@arXiv:2606.23181v1 | arXiv:2606.23181v1 — §DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models; §2 Draft-Agreement Routing for Thinking; §2.2 Self-Consistency Routing | arXiv:2606.23181v1 — §5 Analysis; §5.2 Error Analysis; §Oracle routing analysis. | arXiv:2606.23181v1 — §7 Conclusion; §Task scope.; §Appendix F Multiple-Choice Task Scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23181 | complete |
| SF-2026-ARXIV-2606-23189 | RP-076358a9019c7c24 | deep | arXiv:2606.23189v1 | SRC-ARXIV@arXiv:2606.23189v1 | arXiv:2606.23189v1 — §3 Studying CUA Disclosure; §3.1 A taxonomy of CUA disclosure failures; §4 The AgentCIBench Harness | arXiv:2606.23189v1 — §5 Experimental Setup; §6 Do CUAs Follow Contextual Integrity?; §7 Do Disclosures Persist in End-to-End UI Interactions? | arXiv:2606.23189v1 — §9 Discussion and Policy Implications; §Task-completion rankings do not transfer to safety; §10 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23189 | complete |
| SF-2026-ARXIV-2606-23195 | RP-d8e216f0b84b55d5 | deep | arXiv:2606.23195v1 | SRC-ARXIV@arXiv:2606.23195v1 | arXiv:2606.23195v1 — §Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory; §3 Method; §3.2 Memory Store and Consolidation | arXiv:2606.23195v1 — §4.4 Results: Phase 4 (Dose-Response Analysis); §A.3 Retrieved Memory Analysis; §A.5 Sensitivity Analysis: Additive Model Assumption | arXiv:2606.23195v1 — §5 Discussion; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23195 | complete |
| SF-2026-ARXIV-2606-23217 | RP-5d5ed866fec0f8ef | deep | arXiv:2606.23217v1 | SRC-ARXIV@arXiv:2606.23217v1 | arXiv:2606.23217v1 — §3 MuPPET: A Benchmark for Testing LLMs in Multi-Party Conversations; §3.1 Dataset Composition and Construction; §3.2 Metrics | arXiv:2606.23217v1 — §4 Experimental Setup; §5 Experimental Results; §A.6 Privacy and Utility Metrics Human Validation | arXiv:2606.23217v1 — §5.4 Error Analysis; §6 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23217 | complete |
| SF-2026-ARXIV-2606-23276 | RP-a88ca674e3093f0e | deep | arXiv:2606.23276v1 | SRC-ARXIV@arXiv:2606.23276v1 | arXiv:2606.23276v1 — §3 Reverse-Engineering Edits; §5 Mechanistic Analysis | arXiv:2606.23276v1 — §4 Results; §B Additional Experiments; §C Experimental Setup | arXiv:2606.23276v1 — §F Limitations, Broader Impacts, and Code + Reproducibility; §Limitations. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23276 | complete |
| SF-2026-ARXIV-2606-23277 | RP-071a70eeb9722869 | deep | arXiv:2606.23277v1 | SRC-ARXIV@arXiv:2606.23277v1 | arXiv:2606.23277v1 — §IV-B System Details; §V-B RQ2: How well does GIF detect policy violations with an LLM-as-a-declassifier design? | arXiv:2606.23277v1 — §III-C Operational Measurement of GIF; §V Evaluation; §V-C 2 Surrogate analysis models | arXiv:2606.23277v1 — §VII Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23277 | complete |
| SF-2026-ARXIV-2606-23283 | RP-b344500a55895c56 | deep | arXiv:2606.23283v1 | SRC-ARXIV@arXiv:2606.23283v1 | arXiv:2606.23283v1 — §Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs; §2 The IMLogic Benchmark: Towards Implicit Logical Memory Retrieval; §2.3 Benchmark Construction | arXiv:2606.23283v1 — §2 The IMLogic Benchmark: Towards Implicit Logical Memory Retrieval; §2.3 Benchmark Construction; §4.1.1 Experiment Settings. | arXiv:2606.23283v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23283 | complete |
| SF-2026-ARXIV-2606-23321 | RP-406d3a3138e762ff | deep | arXiv:2606.23321v1 | SRC-ARXIV@arXiv:2606.23321v1 | arXiv:2606.23321v1 — §2.2 RL training for Terminal Agents; §4 Training Terminal Agents; §Algorithm | arXiv:2606.23321v1 — §Evaluation; §Appendix E Additional Evaluation Details | arXiv:2606.23321v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23321 | complete |
| SF-2026-ARXIV-2606-23370 | RP-471319b7d51e6650 | deep | arXiv:2606.23370v1 | SRC-ARXIV@arXiv:2606.23370v1 | arXiv:2606.23370v1 — §FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation; §3.1. Design Goals; §3.2. Threat Model | arXiv:2606.23370v1 — §7. Evaluation; §8.1. Security Analysis | arXiv:2606.23370v1 — §10. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23370 | complete |
| SF-2026-ARXIV-2606-23403 | RP-63722230fbfe6feb | deep | arXiv:2606.23403v1 | SRC-ARXIV@arXiv:2606.23403v1 | arXiv:2606.23403v1 — §3 The Litmus System; §3.1 Architecture Reconstruction; §3.3 Metric Design and Export | arXiv:2606.23403v1 — §4.1 Evaluation Domains; §4.3 Evaluation Axes; §C.1 Evaluation Axes | arXiv:2606.23403v1 — §6 Conclusion and Future Work; §Appendix A Reference Failure-Concerns | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23403 | complete |
| SF-2026-ARXIV-2606-23404 | RP-f557b1ea05d83998 | deep | arXiv:2606.23404v1 | SRC-ARXIV@arXiv:2606.23404v1 | arXiv:2606.23404v1 — §3 System Design; §4.1 Evaluation Dataset Construction; §Appendix B Human Verification Protocol | arXiv:2606.23404v1 — §4 Experiment; §4.1 Evaluation Dataset Construction; §5 Case Analysis | arXiv:2606.23404v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23404 | complete |
| SF-2026-ARXIV-2606-23416 | RP-62e4e7cb9f021152 | deep | arXiv:2606.23416v1 | SRC-ARXIV@arXiv:2606.23416v1 | arXiv:2606.23416v1 — §III Threat Model | arXiv:2606.23416v1 — §V-A 1 Locator evaluation | arXiv:2606.23416v1 — §VI Discussion; §VII Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23416 | complete |
| SF-2026-ARXIV-2606-23449 | RP-9ddc7543c98d206b | deep | arXiv:2606.23449v1 | SRC-ARXIV@arXiv:2606.23449v1 | arXiv:2606.23449v1 — §3 System Design; §8.3 System Safety, Provenance, and Recoverability | arXiv:2606.23449v1 — §7 Evaluation; §7.2 Efficiency Analysis; §Appendix A Benchmark Tasks | arXiv:2606.23449v1 — §9 Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23449 | complete |
| SF-2026-ARXIV-2606-23459 | RP-8a80ab557be3930d | deep | arXiv:2606.23459v1 | SRC-ARXIV@arXiv:2606.23459v1 | arXiv:2606.23459v1 — §TriggerBench: Investigating Prospective Memory for Large Language Models; §3.2 Five Dimensions of Prospective Memory; §3.4 Construction Pipeline | arXiv:2606.23459v1 — §3.3 Contrastive Evaluation Variants; §3.6 Benchmark Overview; §4.3 Constraint Analysis: Explicit vs. Implicit | arXiv:2606.23459v1 — §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23459 | complete |
| SF-2026-ARXIV-2606-23521 | RP-12caaaf239b0fb13 | deep | arXiv:2606.23521v1 | SRC-ARXIV@arXiv:2606.23521v1 | arXiv:2606.23521v1 — §3. Design; §Host-mapped memory.; §4.3. Optional Cross-Architecture Execution and GPU-Initiated Networking | arXiv:2606.23521v1 — §2.4. Motivating Experiment: Host-Side Dirty Detection; §5. Evaluation | arXiv:2606.23521v1 — §7. Discussion; §7.5. Limitations and Future Work; §8. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23521 | complete |
| SF-2026-ARXIV-2606-23525 | RP-46401bddd62c26e1 | deep | arXiv:2606.23525v1 | SRC-ARXIV@arXiv:2606.23525v1 | arXiv:2606.23525v1 — §3 Our Approach: SelfCompact; §Summarizer design.; §Learning to compact during post-training. | arXiv:2606.23525v1 — §Cost analysis.; §Headroom analysis.; §Appendix C Cost analysis of summarization | arXiv:2606.23525v1 — §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23525 | complete |
| SF-2026-ARXIV-2606-23546 | RP-29d752236f1a0297 | deep | arXiv:2606.23546v1 | SRC-ARXIV@arXiv:2606.23546v1 | arXiv:2606.23546v1 — §2.2 Scale, Architecture, and Efficiency; §3.1 Tasks, Models and Training Protocol; §3.2 Compute, Parameter and Memory Proxies | arXiv:2606.23546v1 — §3.5 Hardware Efficiency via Empirical Speedup Models; §Appendix A Pre-Modeling Exploratory Data Analysis | arXiv:2606.23546v1 — §7 Discussion; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23546 | complete |
| SF-2026-ARXIV-2606-23581 | RP-376c76b86f3fafd2 | deep | arXiv:2606.23581v1 | SRC-ARXIV@arXiv:2606.23581v1 | arXiv:2606.23581v1 — §3 The operator: relocate exactly, patch the conditioning; §5 Reuse beyond the window | arXiv:2606.23581v1 — §6 Fidelity, deployment, and cost; §C.1 Reuse breaks multi-hop accuracy; the patch restores it; §C.6 Memory cost and bf16-faithful live deployment | arXiv:2606.23581v1 — §Scope.; §B A menu of cross-chunk reuse operating points and its boundary; §D The reuse safety envelope: when a cached patch survives context drift | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23581 | complete |
| SF-2026-ARXIV-2606-23583 | RP-0663bda154ba62f1 | deep | arXiv:2606.23583v1 | SRC-ARXIV@arXiv:2606.23583v1 | arXiv:2606.23583v1 — §3.1 Conceptual Framework; §[ RQ1 ] Detection is a training law more than a scaling law.; §[ RQ1 ] Detection is training-driven and distribution-fragile. | arXiv:2606.23583v1 — §Evaluation Awareness Is Not One Capability: Evidence from Open Language Models; §4 Empirical Setup; §5.1 Is evaluation awareness one trait? | arXiv:2606.23583v1 — §5 Results & Discussion; §9 Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23583 | complete |
| SF-2026-ARXIV-2606-23589 | RP-0c6742465214ff97 | deep | arXiv:2606.23589v1 | SRC-ARXIV@arXiv:2606.23589v1 | arXiv:2606.23589v1 — §3 Method; §3.2 Framework Overview; §3.4 Keyframe Memory Integration | arXiv:2606.23589v1 — §4.3 Module Contribution Analysis | arXiv:2606.23589v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23589 | complete |
| SF-2026-ARXIV-2606-23617 | RP-3591e84abe83d4be | deep | arXiv:2606.23617v1 | SRC-ARXIV@arXiv:2606.23617v1 | arXiv:2606.23617v1 — §3 Enabling Active, Continual Learning from Uncertainty-Guided Data; §3.1 Active Learning Pipeline; §3.2 Continual Learning Strategies | arXiv:2606.23617v1 — §4 Experiment Overview and General Setup; §5–§9 Experiments 1–5; §D Additional Experimental Results | arXiv:2606.23617v1 — §10 Summary and Conclusion; §11 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23617 | complete |
| SF-2026-ARXIV-2606-23642 | RP-50a063163655aa00 | deep | arXiv:2606.23642v1 | SRC-ARXIV@arXiv:2606.23642v1 | arXiv:2606.23642v1 — §3 Method; §3.1 Scoring, Training, and Retrieval; §3.2 Random Prefix-Length Augmentation | arXiv:2606.23642v1 — §4 Experiments; §4.1 Setup; §4.2 Main Results | arXiv:2606.23642v1 — §Storage overhead.; §Source attribution.; §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23642 | complete |
| SF-2026-ARXIV-2606-23654 | RP-50755e78b77a1561 | deep | arXiv:2606.23654v1 | SRC-ARXIV@arXiv:2606.23654v1 | arXiv:2606.23654v1 — §2 EnterpriseClawBench Data and Construction; §Construction pipeline.; §B.1 End-to-End Construction Case | arXiv:2606.23654v1 — §Benchmark statistics.; §3.1 Evaluation Setting; §Rubric-dimension analysis. | arXiv:2606.23654v1 — §4 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23654 | complete |
| SF-2026-ARXIV-2606-23664 | RP-e4fa0215c2064288 | deep | arXiv:2606.23664v1 | SRC-ARXIV@arXiv:2606.23664v1 | arXiv:2606.23664v1 — §5.3 Communication Protocol; §B.2 Initial and Optimized System Prompt | arXiv:2606.23664v1 — §4 MAS-PromptBench: Prompt Optimization for MAS Benchmark; §5 Empirical Study of Prompt Optimization in MAS; §Appendix A Benchmark Details | arXiv:2606.23664v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23664 | complete |
| SF-2026-ARXIV-2606-23671 | RP-5544f3529dd6042d | deep | arXiv:2606.23671v1 | SRC-ARXIV@arXiv:2606.23671v1 | arXiv:2606.23671v1 — §A.2 Judge Prompts (Training Labels); §Safety protocol failure.; §Training data artifact. | arXiv:2606.23671v1 — §Per-benchmark recognition gap. | arXiv:2606.23671v1 — §Scope of the recognition signal.; §Byproduct and scope of the targeted intervention.; §Safety protocol failure. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23671 | complete |
| SF-2026-ARXIV-2606-23686 | RP-717ce1ff4e37f9be | deep | arXiv:2606.23686v1 | SRC-ARXIV@arXiv:2606.23686v1 | arXiv:2606.23686v1 — §3.4 Training Dataset; §Appendix 0.A Environment Design Details; §0.A.1 Preliminary: The BDDL Framework | arXiv:2606.23686v1 — §LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models; §2.3 Benchmarks for VLA Evaluation; §3 VLA Safety Benchmark | arXiv:2606.23686v1 — §4.4 Failure Case Analysis; §5 Conclusion; §Appendix 0.E Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23686 | complete |
| SF-2026-ARXIV-2606-23752 | RP-11e539991b780b79 | deep | arXiv:2606.23752v1 | SRC-ARXIV@arXiv:2606.23752v1 | arXiv:2606.23752v1 — §ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents; §2.2 Agent Memory; §4 Architecture | arXiv:2606.23752v1 — §8 Self-Referential Case Study | arXiv:2606.23752v1 — §9 Discussion; §Validation Scope; §10 Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23752 | complete |
| SF-2026-ARXIV-2606-23754 | RP-80d253258f7416f4 | deep | arXiv:2606.23754v1 | SRC-ARXIV@arXiv:2606.23754v1 | arXiv:2606.23754v1 — §3 The FEARL Architecture; §4 Enabling Verification via Decomposition; §4.1 Theoretical Guarantees | arXiv:2606.23754v1 — §5 Experiments; §5.1 Experimental Setup; §5.3 Does the Decomposition Enable Verification? | arXiv:2606.23754v1 — §6 Discussion and Conclusion; §A Proof of Propositions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23754 | complete |
| SF-2026-ARXIV-2606-23768 | RP-b661157832cc1cc6 | deep | arXiv:2606.23768v1 | SRC-ARXIV@arXiv:2606.23768v1 | arXiv:2606.23768v1 — §2 A compact slice of maths; §4 How to apply this mathematics to AI agents | arXiv:2606.23768v1 — §3 Examples; §3.2 A recursive example | arXiv:2606.23768v1 — §5 Related work; §6 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23768 | complete |
| SF-2026-ARXIV-2606-23797 | RP-586d92ff695ed1ea | deep | arXiv:2606.23797v1 | SRC-ARXIV@arXiv:2606.23797v1 | arXiv:2606.23797v1 — §9.5 Turn-Level Algorithm; §10 Design Principles; §11 Evaluation Protocol | arXiv:2606.23797v1 — §11 Evaluation Protocol | arXiv:2606.23797v1 — §15 Contributions, Scope, and Validity; §16 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23797 | complete |
| SF-2026-ARXIV-2606-23858 | RP-eaf7eb4ee5291e7e | deep | arXiv:2606.23858v1 | SRC-ARXIV@arXiv:2606.23858v1 | arXiv:2606.23858v1 — §3 Robustness Operators; §4 Algorithms; §4.2 Refine & Check Algorithm | arXiv:2606.23858v1 — §5 Implementation; §Experimental Setup.; §Experimental Results. | arXiv:2606.23858v1 — §4.3 The Complexity of Apothem Optimality; §4.4 The Intractability of Volume Optimality; §7 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23858 | complete |
| SF-2026-ARXIV-2606-23872 | RP-9dc4566b622d4196 | deep | arXiv:2606.23872v1 | SRC-ARXIV@arXiv:2606.23872v1 | arXiv:2606.23872v1 — §3 Member vs Generated Inference; §5 Proposed Data Circuit Breaker; §5.3 Attribution Protocol | arXiv:2606.23872v1 — §6 Empirical Evaluation; §6.1 Experimental Setup; §6.2 Evaluation on the Direct Training Setting | arXiv:2606.23872v1 — §4 Limitations of MIA and Attribution Methods; §4.1 CPD-based Methods Fall Short for MGI; §7 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23872 | complete |
| SF-2026-ARXIV-2606-23892 | RP-06593621965cfe01 | deep | arXiv:2606.23892v1 | SRC-ARXIV@arXiv:2606.23892v1 | arXiv:2606.23892v1 — §Black-box threat model.; §Appendix D Attack Method Details; §Appendix E Defense Method Details | arXiv:2606.23892v1 — §ReaLM : A Unified Red-Teaming Benchmark for Physical-World VLMs; §2.2 Red-Teaming Benchmark; §3 ReaLM : Benchmark for Physical-World VLMs | arXiv:2606.23892v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23892 | complete |
| SF-2026-ARXIV-2606-23915 | RP-40bb5ab37448548e | deep | arXiv:2606.23915v1 | SRC-ARXIV@arXiv:2606.23915v1 | arXiv:2606.23915v1 — §3 A Sentence-Unit Provenance-Ranking Score; §3.1 Provenance/topicality | arXiv:2606.23915v1 — §4 The Cross-Dataset Audit; §5 ERCR as a Boundary Probe; §F Independent Replication and Robustness | arXiv:2606.23915v1 — §An external boundary: long-form alone does not predict the NLI failure.; §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23915 | complete |
| SF-2026-ARXIV-2606-23927 | RP-8e7f0b0083cecfe5 | deep | arXiv:2606.23927v1 | SRC-ARXIV@arXiv:2606.23927v1 | arXiv:2606.23927v1 — §4 NodeSpec: System Representation; §6 RIFT-Bench Framework; §F.2 Framework and Architecture Matrix | arXiv:2606.23927v1 — §7.1 Structure Identifier Evaluation; §Appendix A Additional Comparison to Agentic Security Evaluation; §E.3 Evaluation Metrics | arXiv:2606.23927v1 — §8 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23927 | complete |
| SF-2026-ARXIV-2606-23937 | RP-ce5655baa3fd33ee | deep | arXiv:2606.23937v1 | SRC-ARXIV@arXiv:2606.23937v1 | arXiv:2606.23937v1 — §Sensitivity to domain and query construction. | arXiv:2606.23937v1 — §Decision models and evaluation.; §Analysis of informative nonmatching clauses.; §B.1 Primary 3B result | arXiv:2606.23937v1 — §Contribution and scope.; §Construct scope.; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23937 | complete |
| SF-2026-ARXIV-2606-23961 | RP-66063867de9c70fe | deep | arXiv:2606.23961v1 | SRC-ARXIV@arXiv:2606.23961v1 | arXiv:2606.23961v1 — §2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection | arXiv:2606.23961v1 — §5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations | arXiv:2606.23961v1 — §7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23961 | complete |
| SF-2026-ARXIV-2606-23969 | RP-33e058893082b031 | deep | arXiv:2606.23969v1 | SRC-ARXIV@arXiv:2606.23969v1 | arXiv:2606.23969v1 — §3 Platforms and Method; §4.1 Compute and GPU-Local Memory Are at Parity; §5.6 Runtime Design Rule | arXiv:2606.23969v1 — §3.3 Experiment Families; §5 Case Study: Policy Inversion in the Serving Runtime; §6 Case Study: Movement Engineering for Loading and KV State | arXiv:2606.23969v1 — §3.4 Comparability and Claim Scope; §11 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23969 | complete |
| SF-2026-ARXIV-2606-23983 | RP-f9f797d0ada49233 | deep | arXiv:2606.23983v1 | SRC-ARXIV@arXiv:2606.23983v1 | arXiv:2606.23983v1 — §3. From Algebra to Architecture; §4. Harness Architecture; §5. Design Rationale and System Invariants | arXiv:2606.23983v1 — §12. Evaluation Methodology; §Simulation study (this paper). | arXiv:2606.23983v1 — §15. Discussion: Failure Modes and Guidance; §16. Limitations and Threats to Validity; §17. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23983 | complete |
| SF-2026-ARXIV-2606-23989 | RP-09c8220b5834cfb1 | deep | arXiv:2606.23989v1 | SRC-ARXIV@arXiv:2606.23989v1 | arXiv:2606.23989v1 — §Attribution by Construction: Claim-Anchored Evidence for Faithfulness-Oriented Multi-Document Summarization; §3 Method; §Training labels by distant supervision. | arXiv:2606.23989v1 — §Faithful summarization and its evaluation.; §4.3 Evaluation Protocol; §5 Results and Analysis | arXiv:2606.23989v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23989 | complete |
| SF-2026-ARXIV-2606-24004 | RP-16a0a13de80e0da0 | deep | arXiv:2606.24004v1 | SRC-ARXIV@arXiv:2606.24004v1 | arXiv:2606.24004v1 — §4 Spec Learning Framework; §4.1 Selection Method; §4.4 Judge protocol and selection | arXiv:2606.24004v1 — §5 Results; §B Statistical robustness; §C Judge calibration | arXiv:2606.24004v1 — §6 Discussion; §7 Limitations; §8 Conclusions and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24004 | complete |
| SF-2026-ARXIV-2606-24020 | RP-ade71f3c2dbfa40f | deep | arXiv:2606.24020v1 | SRC-ARXIV@arXiv:2606.24020v1 | arXiv:2606.24020v1 — §You Don’t Need to Run Every Eval Yuchen Zeng & Dimitris Papailiopoulos; §1 Introduction [You Don't Need to Run Every Eval exact-v1 method boundary] | arXiv:2606.24020v1 — §4 BenchPress : A Low-rank Benchmark Score Predictor; §4.3 BenchPress vs. LLMs as Benchmark Score Predictors; §5 What BenchPress Enables for Model Evaluation | arXiv:2606.24020v1 — §7 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24020 | complete |
| SF-2026-ARXIV-2606-24033 | RP-5219f6750e78abe2 | deep | arXiv:2606.24033v1 | SRC-ARXIV@arXiv:2606.24033v1 | arXiv:2606.24033v1 — §RoPE-Aware Bit Allocation for KV-Cache Quantization; §1 Introduction [RoPE-Aware Bit Allocation for KV-Cache Quantization exact-v1 method boundary] | arXiv:2606.24033v1 — §6.3 Downstream Evaluation | arXiv:2606.24033v1 — §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24033 | complete |
| SF-2026-ARXIV-2606-24040 | RP-3941cc06f46e95b8 | deep | arXiv:2606.24040v1 | SRC-ARXIV@arXiv:2606.24040v1 | arXiv:2606.24040v1 — §3 Version-aware Operations; §4 Version and Transaction Correlation Memories | arXiv:2606.24040v1 — §5 Examples; §5.1 Direct sequence-level replacement; §5.2 Structured diff-level update | arXiv:2606.24040v1 — §6 Evaluation Roadmap and Scope; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24040 | complete |
| SF-2026-ARXIV-2606-24551 | RP-90460108b17b82a9 | deep | arXiv:2606.24551v1 | SRC-ARXIV@arXiv:2606.24551v1 | arXiv:2606.24551v1 — §3.2 Benchmark Construction; §A.3 Visual Design Example | arXiv:2606.24551v1 — §3 Benchmark; §3.1 Benchmark Scope and Composition; §3.2 Benchmark Construction | arXiv:2606.24551v1 — §3.1 Benchmark Scope and Composition; §UI Navigation and Control Discovery Failure.; §Workflow Execution Failure. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24551 | complete |
| SF-2026-ARXIV-2606-24934 | RP-bf21f45e43aad532 | deep | arXiv:2606.24934v1 | SRC-ARXIV@arXiv:2606.24934v1 | arXiv:2606.24934v1 — §3 Attestation Model; §4 GPU Probe; §11 Packaging | arXiv:2606.24934v1 — §5 Certificate Stability Under Load; §6 Cross-Die Fingerprint Attestation; §7–§10 Attestation experiments | arXiv:2606.24934v1 — §12 Limitations; §13 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24934 | complete |
| SF-2026-ARXIV-2606-28385 | RP-9a2cc272fda7078b | deep | arXiv:2606.28385v1 | SRC-ARXIV@arXiv:2606.28385v1 | arXiv:2606.28385v1 — §3 Method; §4.2 Evaluation Protocol; §A.2.1 Dataset Construction | arXiv:2606.28385v1 — §RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis; §3.3 Candidate Discovery and Specialist Analysis; §4.2 Evaluation Protocol | arXiv:2606.28385v1 — §5 Conclusion; §A.4.8 Scope of Learned-Evaluator Comparisons | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-28385 | complete |
| SF-2026-ARXIV-2606-28386 | RP-12bfb3b17f8336e5 | deep | arXiv:2606.28386v1 | SRC-ARXIV@arXiv:2606.28386v1 | arXiv:2606.28386v1 — §3 Method; §3.3 A Framework for Data Provenance in IARs; §3.3.1 QuantLoss | arXiv:2606.28386v1 — §4 Empirical Evaluation; §4.1 Experimental Setup; §4.2–§4.4 Results and Ablations | arXiv:2606.28386v1 — §R Adaptive Attack; §W Comparison with Membership Inference Baselines; §5 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-28386 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-22741:start -->
### 2606.22741 — GRADE: Graph Representation of LLM Agent Dependency and Execution

**问题与旧路径。** Across six corpora of LLM agents spanning tool use, coding, and the web, the dependency layer can predict failure where run size is weak and, under leave-one-corpus-out transfer, stays above chance on every held-out class while run size fails. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** GRADE: Graph Representation of LLM Agent Dependency and Execution 的 exact-v1 机制为：A trace records what each step did, never what it relied on, the state it read, and the results it reused. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22741v1 — §2.2 The Formal Class; §Appendix A Formal Class and Subsumption; §A.1 The Formal Tuple and Recovery Maps`；Evaluation=`arXiv:2606.22741v1 — §E.2 The Limits of the Localization Result`；counterevidence=`arXiv:2606.22741v1 — §3 Two Layers, Two Failure Modes; §3.1 The Two Layers and Their Failure Modes; §4.1 Dependency Structure Predicts Failure Within a Corpus`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Across six corpora of LLM agents spanning tool use, coding, and the web, the dependency layer can predict failure where run size is weak and, under leave-one-corpus-out transfer, stays above chance on every held-out class while run size fails. 披露的 evaluation signal 是：A trace records what each step did, never what it relied on, the state it read, and the results it reused. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22741:start -->
Primary identity `arXiv:2606.22741v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22741:end -->
<!-- review:SF-2026-ARXIV-2606-22741:end -->

<!-- review:SF-2026-ARXIV-2606-22768:start -->
### 2606.22768 — Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo

**问题与旧路径。** While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo 的 exact-v1 机制为：On up to billion-parameter language models in low-bandwidth settings, our framework substantially improves compute utilization compared to DiLoCo, with training progress ranging from comparable to closely matching it, and is more robust to failures. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22768v1 — §5.1 Training experiments; §Appendix A Factored Gossip DiLoCo: Detailed Algorithm`；Evaluation=`arXiv:2606.22768v1 — §Appendix E Consensus Error Result and Proof`；counterevidence=`arXiv:2606.22768v1 — §7 Conclusion and Future Work; §Appendix C Further Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures. 披露的 evaluation signal 是：To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22768:start -->
Primary identity `arXiv:2606.22768v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22768:end -->
<!-- review:SF-2026-ARXIV-2606-22768:end -->

<!-- review:SF-2026-ARXIV-2606-22778:start -->
### 2606.22778 — HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions

**问题与旧路径。** With the rapid spread of retrieval-augmented generation and semantic search, choosing the right embedding and retrieval configuration is increasingly hard. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions 的 exact-v1 机制为：We present HAKARI-Bench, a lightweight benchmark that reconstructs existing retrieval suites into small datasets (Nano-sets): 35 benchmarks and 551 tasks across 43 languages in a unified format, enabling same-condition, model-agnostic comparison of five retrieval families (BM25, dense, sparse, late interaction, rerankers) and their efficiency variants. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。 唯一 owner 为 `AGENT-RAG`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22778v1 — §Lightweight evaluation and Nano-set construction; §Design of HAKARI-Bench; §Appendix A Nano-set construction and dataset list`；Evaluation=`arXiv:2606.22778v1 — §HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions; §Retrieval evaluation benchmarks and retrieval architectures; §Lightweight evaluation and Nano-set construction`；counterevidence=`arXiv:2606.22778v1 — §Discussion; §Scope of evaluated models; §Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：With the rapid spread of retrieval-augmented generation and semantic search, choosing the right embedding and retrieval configuration is increasingly hard. 披露的 evaluation signal 是：HAKARI-Bench does not replace full evaluation; it enables rapid model selection, regression detection, and reading the quality-efficiency Pareto frontier. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22778:start -->
Primary identity `arXiv:2606.22778v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22778:end -->
<!-- review:SF-2026-ARXIV-2606-22778:end -->

<!-- review:SF-2026-ARXIV-2606-22783:start -->
### 2606.22783 — Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints

**问题与旧路径。** We break this paradox by shifting the evaluation paradigm from simulating a messy reality to constructing computationally pure challenges. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints 的 exact-v1 机制为：We introduce VERITAS (Verifiable Traversal Assessment for Search), a framework built on the principle of computationally irreducible constraints. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22783v1 — §3 Method; §A.4 The Dilemma of Construction and Verification; §A.4.1 Construction Difficulty`；Evaluation=`arXiv:2606.22783v1 — §Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints; §3.1 Evaluation Paradox; §3.3 Asymptotic Analysis`；counterevidence=`arXiv:2606.22783v1 — §5 Conclusion; §A.6 Conclusion: Returning to the Origin of Difficulty; §C.8 Conclusion: Validating Computational Irreducibility`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We break this paradox by shifting the evaluation paradigm from simulating a messy reality to constructing computationally pure challenges. 披露的 evaluation signal 是：Evaluating the exhaustive search capabilities of large language models (LLMs) is plagued by a fundamental paradox: verifying completeness requires complete ground truth, yet high-entropy enumeration tasks make such ground truth impossible for humans to create. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22783:start -->
Primary identity `arXiv:2606.22783v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22783:end -->
<!-- review:SF-2026-ARXIV-2606-22783:end -->

<!-- review:SF-2026-ARXIV-2606-22792:start -->
### 2606.22792 — The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models

**问题与旧路径。** Recent advancements in Large Language Models (LLMs) have enabled sophisticated reasoning and content generation, yet their inherent stochasticity poses significant challenges for ensuring predictive credibility. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models 的 exact-v1 机制为：In this paper, we propose a granular uncertainty taxonomy that systematically attributes LLM uncertainty into input-level, parameter-level, token-level, and decoding-process sources. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22792v1 — §2.4 Training Necessity; §Full training.`；Evaluation=`arXiv:2606.22792v1 — §2.6 Evaluation; §Appendix A Evaluation Ranking`；counterevidence=`arXiv:2606.22792v1 — §Future issues.`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Recent advancements in Large Language Models (LLMs) have enabled sophisticated reasoning and content generation, yet their inherent stochasticity poses significant challenges for ensuring predictive credibility. 披露的 evaluation signal 是：While traditional uncertainty taxonomy paradigms, such as the dichotomy of aleatoric and epistemic uncertainties, provide conceptual foundations, they often fail to capture the multi-component and multi-stage nature of LLM generation and struggle to evaluate the effectiveness of various Uncertainty Quantification (UQ) methods. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22792:start -->
Primary identity `arXiv:2606.22792v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22792:end -->
<!-- review:SF-2026-ARXIV-2606-22792:end -->

<!-- review:SF-2026-ARXIV-2606-22794:start -->
### 2606.22794 — UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models

**问题与旧路径。** Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models 的 exact-v1 机制为：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22794v1 — §UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models; §3 Method; §3.2 Framework`；Evaluation=`arXiv:2606.22794v1 — §Appendix 0.B More Analysis`；counterevidence=`arXiv:2606.22794v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 披露的 evaluation signal 是：Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22794:start -->
Primary identity `arXiv:2606.22794v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22794:end -->
<!-- review:SF-2026-ARXIV-2606-22794:end -->

<!-- review:SF-2026-ARXIV-2606-22798:start -->
### 2606.22798 — Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control

**问题与旧路径。** In sparse Mixture-of-Experts language models, does the same token id imply the same router state and the same experts producing it? 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control 的 exact-v1 机制为：Holding the emitted token id fixed at repeated anchors, we find it does not: the experts that produce it still separate task context, trajectory history, and reasoning-effort mode. 因此 把 router state 视为内部诊断/选择信号，而不是未经验证的正确性证明。 唯一 owner 为 `MODEL-MOE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22798v1 — §Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control; §MoE routing.; §3 Analysis of Anchor-Conditioned Routing`；Evaluation=`arXiv:2606.22798v1 — §3 Analysis of Anchor-Conditioned Routing; §5.3 Analysis`；counterevidence=`arXiv:2606.22798v1 — §7 Conclusion; §A.13 Failure case studies`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：In sparse Mixture-of-Experts language models, does the same token id imply the same router state and the same experts producing it? 披露的 evaluation signal 是：Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22798:start -->
Primary identity `arXiv:2606.22798v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22798:end -->
<!-- review:SF-2026-ARXIV-2606-22798:end -->

<!-- review:SF-2026-ARXIV-2606-22804:start -->
### 2606.22804 — CoVStream: Edge-Cloud Collaboration for Understanding of Long Video Streams

**问题与旧路径。** However, they overlook a crucial deployment fact: the stream is often produced by computationally constrained devices. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** CoVStream: Edge-Cloud Collaboration for Understanding of Long Video Streams 的 exact-v1 机制为：Therefore, we propose CoVStream, the first edge-cloud collaborative framework for understanding long video streams. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。 唯一 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22804v1 — §2.1 System Overview; §2.3 Cloud Server: Decoupled Management and Reasoning Architecture`；Evaluation=`arXiv:2606.22804v1 — §3 Experiment; §3.3 Diagnostic Experiment; §3.4 Qualitative Analysis`；counterevidence=`arXiv:2606.22804v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, they overlook a crucial deployment fact: the stream is often produced by computationally constrained devices. 披露的 evaluation signal 是：Experiments on VideoMME-Long, LVBench, and RTV-Bench show that CoVStream reduces bandwidth usage by 87.6% while retaining 99.2% of the cloud baseline accuracy on LVBench. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22804:start -->
Primary identity `arXiv:2606.22804v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22804:end -->
<!-- review:SF-2026-ARXIV-2606-22804:end -->

<!-- review:SF-2026-ARXIV-2606-22826:start -->
### 2606.22826 — MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration

**问题与旧路径。** Existing subset selection methods reduce this cost but depend on large calibration pools or learned prediction layers. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration 的 exact-v1 机制为：We introduce MINCE (Monte Carlo Informed N-sizing for Compact Evaluation), which uses Monte Carlo simulation over per-item logs from a small set of calibration models to find the minimum subset size that bounds accuracy drift and then fixes a randomly sampled subset at that size, with no prediction layer needed. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22826v1 — §3 Method; §3.3 Subset Construction`；Evaluation=`arXiv:2606.22826v1 — §MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration; §Appendix D Threshold Sensitivity Analysis; §Appendix E GPU Evaluation Speedup Breakdown`；counterevidence=`arXiv:2606.22826v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Existing subset selection methods reduce this cost but depend on large calibration pools or learned prediction layers. 披露的 evaluation signal 是：Evaluating LLMs across many model variants -- quantized, fine-tuned, or deployment-specific -- requires running large benchmarks repeatedly, a process that can take tens of hours per model on edge hardware such as NPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22826:start -->
Primary identity `arXiv:2606.22826v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22826:end -->
<!-- review:SF-2026-ARXIV-2606-22826:end -->

<!-- review:SF-2026-ARXIV-2606-22827:start -->
### 2606.22827 — What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security

**问题与旧路径。** Modern software development relies heavily on third-party components from public repositories, expanding the software supply chain attack surface. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security 的 exact-v1 机制为：In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22827v1 — §What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security; §2.3 Memory Analysis of Python; §5.3 Dependency Graph Construction`；Evaluation=`arXiv:2606.22827v1 — §2.3 Memory Analysis of Python; §5.3.1 Module Structure Analysis; §5.3.2 Bytecode Analysis`；counterevidence=`arXiv:2606.22827v1 — §7 Limitations and Future Work; §8 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Modern software development relies heavily on third-party components from public repositories, expanding the software supply chain attack surface. 披露的 evaluation signal 是：In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22827:start -->
Primary identity `arXiv:2606.22827v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22827:end -->
<!-- review:SF-2026-ARXIV-2606-22827:end -->

<!-- review:SF-2026-ARXIV-2606-22840:start -->
### 2606.22840 — RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving

**问题与旧路径。** We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving 的 exact-v1 机制为：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 因此 把 draft/verify/bypass 路由、质量门槛、成本和 schema-critical fallback 共同验收。 唯一 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22840v1 — §2.2 LLM Cascade and Routing; §3 System Design; §3.1 Architecture Overview`；Evaluation=`arXiv:2606.22840v1 — §4 Evaluation; §4.6 Extended Engineering Benchmark; §4.7 Case Study: Cost Inversion on mteb-retrieve`；counterevidence=`arXiv:2606.22840v1 — §6 Discussion; §6.4 Cross-Provider Failure Modes; §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 披露的 evaluation signal 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22840:start -->
Primary identity `arXiv:2606.22840v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22840:end -->
<!-- review:SF-2026-ARXIV-2606-22840:end -->

<!-- review:SF-2026-ARXIV-2606-22844:start -->
### 2606.22844 — RaMem: Contextual Reinstatement for Long-term Agentic Memory

**问题与旧路径。** We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RaMem: Contextual Reinstatement for Long-term Agentic Memory 的 exact-v1 机制为：To address this problem, we propose Contextual Reinstatement for Agentic Memory (RaMem), a framework that turns retrieved memory fragments into contextually verifiable evidence. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22844v1 — §RaMem: Contextual Reinstatement for Long-term Agentic Memory; §3 Method; §3.1 Episodic Memory Anchoring`；Evaluation=`arXiv:2606.22844v1 — §4.3 Context Collapse Analysis; §4.5 Hyper-parameter Analysis; §4.6 Component Analysis`；counterevidence=`arXiv:2606.22844v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. 披露的 evaluation signal 是：Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22844:start -->
Primary identity `arXiv:2606.22844v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22844:end -->
<!-- review:SF-2026-ARXIV-2606-22844:end -->

<!-- review:SF-2026-ARXIV-2606-22864:start -->
### 2606.22864 — When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents

**问题与旧路径。** We argue, on a single-backbone cautionary case study (Qwen2.5-VL-7B on Mind2Web, teacher-forced replay), that a high probing AUC on a clean-vs-attack split is not, on its own, evidence of malicious-content detection. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents 的 exact-v1 机制为：We argue, on a single-backbone cautionary case study (Qwen2.5-VL-7B on Mind2Web, teacher-forced replay), that a high probing AUC on a clean-vs-attack split is not, on its own, evidence of malicious-content detection. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22864v1 — §When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents; §3. Evaluation protocol; §3.1. Threat model and estimands`；Evaluation=`arXiv:2606.22864v1 — §When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents; §A cautionary case study.; §3. Evaluation protocol`；counterevidence=`arXiv:2606.22864v1 — §Threat model (in scope vs. out of scope).; §Two failure-mode flags.; §6. Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We argue, on a single-backbone cautionary case study (Qwen2.5-VL-7B on Mind2Web, teacher-forced replay), that a high probing AUC on a clean-vs-attack split is not, on its own, evidence of malicious-content detection. 披露的 evaluation signal 是：Hidden-state probing -- a linear classifier on a frozen vision-language model's internal activations -- has emerged as an attractive evaluation tool for flagging indirect prompt injection (IPI) in multimodal computer-use agents before the agent emits a corrupted action. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22864:start -->
Primary identity `arXiv:2606.22864v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22864:end -->
<!-- review:SF-2026-ARXIV-2606-22864:end -->

<!-- review:SF-2026-ARXIV-2606-22873:start -->
### 2606.22873 — SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning

**问题与旧路径。** This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning 的 exact-v1 机制为：We present \textbf{SingGuard}, a policy-adaptive multimodal guardrail model family for safety assessment in multimodal conversations. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22873v1 — §2 Method; §2.3.3 Dynamic Rule Data Construction; §2.3.4 Chain-of-Thought Reasoning Data Construction`；Evaluation=`arXiv:2606.22873v1 — §3.2 Benchmark Composition and Statistics; §4.1 Evaluation Setup; §4.7 Dynamic Policy Evaluation`；counterevidence=`arXiv:2606.22873v1 — §6 Conclusion; §C.4 Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. 披露的 evaluation signal 是：We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22873:start -->
Primary identity `arXiv:2606.22873v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22873:end -->
<!-- review:SF-2026-ARXIV-2606-22873:end -->

<!-- review:SF-2026-ARXIV-2606-22874:start -->
### 2606.22874 — SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers

**问题与旧路径。** Sparse attention cuts these costs by attending only to a relevant subset of past tokens, but selecting that subset is itself expensive. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers 的 exact-v1 机制为：We present SpotAttention, a lightweight selector that attaches to a frozen pretrained transformer and learns by KL distillation to estimate its attention distribution. 因此 把稀疏选择器、token/KV identity、预算和 dense fallback 纳入请求状态。 唯一 owner 为 `MODEL-LONG-CONTEXT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22874v1 — §SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers; §Method; §2.1 Selector architecture`；Evaluation=`arXiv:2606.22874v1 — §Evaluation.; §Analysis and ablations; §Empirical shape gap.`；counterevidence=`arXiv:2606.22874v1 — §Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Sparse attention cuts these costs by attending only to a relevant subset of past tokens, but selecting that subset is itself expensive. 披露的 evaluation signal 是：Quantizing the selector's K-cache to INT4 or FP4 microscale shrinks it 3.5x at no accuracy cost. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22874:start -->
Primary identity `arXiv:2606.22874v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22874:end -->
<!-- review:SF-2026-ARXIV-2606-22874:end -->

<!-- review:SF-2026-ARXIV-2606-22875:start -->
### 2606.22875 — FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs

**问题与旧路径。** However, FL requires sharing the global model with multiple participants, which risks unauthorized model distribution or resale by malicious clients. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs 的 exact-v1 机制为：In this paper, we propose FedOT, the first framework for ownership verification and leakage tracing in federated LDMs. 因此 把 ownership/provenance 证据与 artifact hash、client identity 和泄露追踪绑定。 唯一 owner 为 `PLATFORM-MODEL-REGISTRY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22875v1 — §3.1 FedOT Framework; §3.2 Watermark Design and Training; §0.A.1 Federated LDMs and Threat Model`；Evaluation=`arXiv:2606.22875v1 — §0.C.2 Analysis of LVT`；counterevidence=`arXiv:2606.22875v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, FL requires sharing the global model with multiple participants, which risks unauthorized model distribution or resale by malicious clients. 披露的 evaluation signal 是：Extensive experiments demonstrate that FedOT achieves superior performance in both ownership verification and traceability. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22875:start -->
Primary identity `arXiv:2606.22875v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22875:end -->
<!-- review:SF-2026-ARXIV-2606-22875:end -->

<!-- review:SF-2026-ARXIV-2606-22877:start -->
### 2606.22877 — DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings

**问题与旧路径。** LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they prefer (preferences), and keep it updated as jobs, routines, and tastes drift. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings 的 exact-v1 机制为：Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22877v1 — §DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings; §4.3 Evaluation Protocol and Metrics; §Appendix B Base User Profile Schema and Construction`；Evaluation=`arXiv:2606.22877v1 — §DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings; §4 DynamicMem Benchmark; §4.1 Checkpoint-Based Evaluation and Dataset Statistics`；counterevidence=`arXiv:2606.22877v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they prefer (preferences), and keep it updated as jobs, routines, and tastes drift. 披露的 evaluation signal 是：Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22877:start -->
Primary identity `arXiv:2606.22877v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22877:end -->
<!-- review:SF-2026-ARXIV-2606-22877:end -->

<!-- review:SF-2026-ARXIV-2606-22878:start -->
### 2606.22878 — Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning

**问题与旧路径。** However, the dynamic nature of practical decentralized edge networks, where devices may dynamically join or leave the collaborative training process, requires the system to continuously adapt to new data while selectively removing prior contributions. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning 的 exact-v1 机制为：As large language models (LLMs) are increasingly deployed at the network edge to provide pervasive generative AI services, decentralized federated learning (DFL) provides a vital mechanism for privacy-preserving, domain-specific fine-tuning through peer-to-peer exchanges of parameter-efficient updates. 因此 把参与者加入/退出、LoRA contribution coordinate、unlearning correction 与通信预算版本化。 唯一 owner 为 `TRAIN-LORA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22878v1 — §Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning Thanks: N. Yang, Y. He, S. Wang, and C. Yin are with the Beijing Laboratory of Advanced Information Network, and the Beijing Key Laboratory of Network System Architecture and Convergence, Beijing University of Posts and Telecommunications, Beijing 100876, China (emails: {yangnuocheng, heyechen, sihuawang, ccyin}@bupt.edu.cn). Thanks: Z. Chen and T. Q. S. Quek are with the Information Systems Technology and Design Pillar, Singapore University of Technology and Design, 487372, Singapore (emails: zihan_chen@mymail.sutd.edu.sg, tonyquek@sutd.edu.sg).; §III System Model and Problem Formulation; §III-A Dynamic Decentralized LoRA System`；Evaluation=`arXiv:2606.22878v1 — §IV Problem Analysis and Proposed Method; §IV-B Correction Gap Analysis under DGD; §V-C Ablation Study`；counterevidence=`arXiv:2606.22878v1 — §VI Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, the dynamic nature of practical decentralized edge networks, where devices may dynamically join or leave the collaborative training process, requires the system to continuously adapt to new data while selectively removing prior contributions. 披露的 evaluation signal 是：To address this challenge, we propose a priority-aware learning-unlearning correction framework based on orthogonal LoRA that can enhance the knowledge evaluation through topology adjustment. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22878:start -->
Primary identity `arXiv:2606.22878v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22878:end -->
<!-- review:SF-2026-ARXIV-2606-22878:end -->

<!-- review:SF-2026-ARXIV-2606-22883:start -->
### 2606.22883 — CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents

**问题与旧路径。** While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents 的 exact-v1 机制为：To overcome this, we introduce CLI-Universe, a principled synthesis engine that constructs terminal-agent tasks. 因此 把任务/样本生成、可执行验证、过滤与训练 lineage 绑定。 唯一 owner 为 `TRAIN-DATA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22883v1 — §3 Method; §3.2 Task Blueprint Construction; §3.4 Test Construction and Executable Filtering`；Evaluation=`arXiv:2606.22883v1 — §4.3 Scaling Analysis; §4.4.1 Cross-benchmark transfer; §4.5 Error Study`；counterevidence=`arXiv:2606.22883v1 — §5 Conclusion; §Appendix C Failure Mode Examples`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck. 披露的 evaluation signal 是：Remarkably, fine-tuning Qwen3-32B on CLI-Universe-6K achieves 33.4% on Terminal-Bench 2.0. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22883:start -->
Primary identity `arXiv:2606.22883v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22883:end -->
<!-- review:SF-2026-ARXIV-2606-22883:end -->

<!-- review:SF-2026-ARXIV-2606-22902:start -->
### 2606.22902 — Agent-as-a-Router: Agentic Model Routing for Coding Tasks

**问题与旧路径。** Consequently, routing each task to the most suitable model becomes critical for both performance and cost. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Agent-as-a-Router: Agentic Model Routing for Coding Tasks 的 exact-v1 机制为：Motivated by this finding, we propose Agent-as-a-Router, a framework that formalizes routing as a C-A-F loop (Context-&gt;Action-&gt;Feedback-&gt;Context). 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22902v1 — §Agent-as-a-Router: Agentic Model Routing for Coding Tasks; §3.4 Decomposed Routing Policies; §4.1 Benchmark Construction`；Evaluation=`arXiv:2606.22902v1 — §4.1 Benchmark Construction; §5 Empirical Validation; §Appendix B Benchmark and Setup Details`；counterevidence=`arXiv:2606.22902v1 — §5.3 Discussion; §6 Conclusion; §Appendix E Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Consequently, routing each task to the most suitable model becomes critical for both performance and cost. 披露的 evaluation signal 是：We instantiate this framework as ACRouter, composed of an Orchestrator, a Verifier, a Memory module, and introduce CodeRouterBench, an evaluation environment comprising ~10K task instances with verified scores from 8 frontier LLMs, enabling regret-based router comparison on streaming tasks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22902:start -->
Primary identity `arXiv:2606.22902v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22902:end -->
<!-- review:SF-2026-ARXIV-2606-22902:end -->

<!-- review:SF-2026-ARXIV-2606-22906:start -->
### 2606.22906 — From Fragments to Paths: Task-Level Context Recovery for Large Industrial Codebases

**问题与旧路径。** Existing methods often retrieve only local fragments and fail to recover the broader task-relevant context needed for complex repository-level tasks. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** From Fragments to Paths: Task-Level Context Recovery for Large Industrial Codebases 的 exact-v1 机制为：We present DeepDiscovery, a task-level repository-understanding method for large industrial codebases. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。 唯一 owner 为 `AGENT-CONTEXT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22906v1 — §III-B Repository Representation and Overall Framework; §III-E Metadata-First Context Construction; §IV-C Evaluation Protocol`；Evaluation=`arXiv:2606.22906v1 — §Benchmarks and evaluation scenarios.; §IV-C Evaluation Protocol; §IV-F Ablation Study: Where Do the Gains Come From?`；counterevidence=`arXiv:2606.22906v1 — §Practical scope of comparison.; §IV-J Discussion of Error Modes and Scope; §V Threats to Validity`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Existing methods often retrieve only local fragments and fail to recover the broader task-relevant context needed for complex repository-level tasks. 披露的 evaluation signal 是：Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22906:start -->
Primary identity `arXiv:2606.22906v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22906:end -->
<!-- review:SF-2026-ARXIV-2606-22906:end -->

<!-- review:SF-2026-ARXIV-2606-22916:start -->
### 2606.22916 — Intent-Governed Tool Authorization for AI Agents

**问题与旧路径。** A trace-backed normalizer counterfactual removes this residual authority at substantial utility cost. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Intent-Governed Tool Authorization for AI Agents 的 exact-v1 机制为：We present Intent-Governed Access Control (IGAC), a server-side authorization layer that converts a trusted request into a short-lived intent certificate, narrows the statically authorized tool manifest, and checks proposed tool and payload effects before execution. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22916v1 — §I-A Relationship to OpenPort Protocol; §IV Threat Model; §IV-A System Boundary`；Evaluation=`arXiv:2606.22916v1 — §X Evaluation Design; §X-F Expected Analysis Without Fabricated Results; §X-I First-Batch External Benchmark Adaptation`；counterevidence=`arXiv:2606.22916v1 — §IV-E Out of Scope; §XI Limitations and Threats to Validity; §XII-H Effect Estimation and Conservative Failure`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A trace-backed normalizer counterfactual removes this residual authority at substantial utility cost. 披露的 evaluation signal 是：We evaluate a reusable IGAC path over an OpenPort governance substrate using endpoint tests, 176 runtime-backed synthetic tasks, real-model classifier and planner pilots, 306 end-to-end model-task runtime trials, and a 36-trial benchmark-shaped external subset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22916:start -->
Primary identity `arXiv:2606.22916v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22916:end -->
<!-- review:SF-2026-ARXIV-2606-22916:end -->

<!-- review:SF-2026-ARXIV-2606-22918:start -->
### 2606.22918 — Each Judge Its Own Yardstick: Discovering Per-VLM Taxonomies for Physical Video Evaluation

**问题与旧路径。** Maintaining physical consistency in video generators and world models increasingly relies on vision-language models (VLMs) as automated judges that provide reward signals, ranking decisions, and data-filtering criteria. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Each Judge Its Own Yardstick: Discovering Per-VLM Taxonomies for Physical Video Evaluation 的 exact-v1 机制为：We propose JudgeFit, an iterative refinement procedure that discovers a per-VLM evaluation taxonomy. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22918v1 — §3 The JudgeFit Pipeline; §3.2 Seed: Open Annotation and Clustering; §3.3 Refine: Diagnosis-Guided Editing`；Evaluation=`arXiv:2606.22918v1 — §5 Experiments; §5.1 Refinement Improves Every VLM; §5.2 Convergence and Generalization`；counterevidence=`arXiv:2606.22918v1 — §6 Profiling VLM Judges; §6.2 Bias and Discrimination Across Judges; §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Maintaining physical consistency in video generators and world models increasingly relies on vision-language models (VLMs) as automated judges that provide reward signals, ranking decisions, and data-filtering criteria. 披露的 evaluation signal 是：A single global evaluation schema therefore gives every VLM the same axes of competence, regardless of what each can actually perceive. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22918:start -->
Primary identity `arXiv:2606.22918v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22918:end -->
<!-- review:SF-2026-ARXIV-2606-22918:end -->

<!-- review:SF-2026-ARXIV-2606-22925:start -->
### 2606.22925 — EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction

**问题与旧路径。** Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction 的 exact-v1 机制为：Using this methodology, we release a community-reviewed EEG benchmark corpus centered on 53 completed and reviewed entries with 245 task definitions spanning diverse paradigms, and we introduce NeuroDoc and NeuroAudit as the operational support layer for rulebook-guided drafting, upgrading, review, amendment, and release management. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22925v1 — §EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction; §A.1 Broader Database and Benchmark-Construction Scale; §A.3 Execution-validation Dataset Subset and Training Context`；Evaluation=`arXiv:2606.22925v1 — §EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction; §4 Benchmark Corpus; §A.1 Broader Database and Benchmark-Construction Scale`；counterevidence=`arXiv:2606.22925v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. 披露的 evaluation signal 是：Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22925:start -->
Primary identity `arXiv:2606.22925v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22925:end -->
<!-- review:SF-2026-ARXIV-2606-22925:end -->

<!-- review:SF-2026-ARXIV-2606-22932:start -->
### 2606.22932 — FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training

**问题与旧路径。** Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training 的 exact-v1 机制为：This two-phase schedule sets the memory ceiling of modern training: at the seam between the phases, every layer's gradient is live at once. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22932v1 — §FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training; §Our approach.; §2 Method`；Evaluation=`arXiv:2606.22932v1 — §Appendix E Measurement protocol and variance`；counterevidence=`arXiv:2606.22932v1 — §5 Conclusion; §Scope of the optimizer sweep.`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. 披露的 evaluation signal 是：Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22932:start -->
Primary identity `arXiv:2606.22932v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22932:end -->
<!-- review:SF-2026-ARXIV-2606-22932:end -->

<!-- review:SF-2026-ARXIV-2606-22936:start -->
### 2606.22936 — When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents

**问题与旧路径。** Long-horizon LLM agents can fail quietly: they settle on one reading of the evidence early, then spend the rest of the run defending it. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents 的 exact-v1 机制为：We call this premature commitment. 因此 把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state。 唯一 owner 为 `AGENT-PLANNING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22936v1 — §3 Method; §4.6 Cross-architecture validation on HotpotQA`；Evaluation=`arXiv:2606.22936v1 — §4.7 Cross-benchmark generalization on Llama: StrategyQA; §Appendix A Preliminary steering experiment; §Appendix L StrategyQA cross-benchmark results`；counterevidence=`arXiv:2606.22936v1 — §5 Discussion; §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Long-horizon LLM agents can fail quietly: they settle on one reading of the evidence early, then spend the rest of the run defending it. 披露的 evaluation signal 是：The result is a diagnostic for a hidden process failure, with clear limits rather than a general accuracy lever. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22936:start -->
Primary identity `arXiv:2606.22936v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22936:end -->
<!-- review:SF-2026-ARXIV-2606-22936:end -->

<!-- review:SF-2026-ARXIV-2606-22942:start -->
### 2606.22942 — Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails

**问题与旧路径。** Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails 的 exact-v1 机制为：Knowledge Distillation (KD) offers a practical solution by transferring knowledge from a teacher model of a larger size to a smaller student model. 因此 把蒸馏 teacher/student、样本选择与失效区间保留在训练 lineage。 唯一 owner 为 `TRAIN-SFT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22942v1 — §Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails; §3 Post-Training KD for LLMs; §3.2 Knowledge Distillation Method`；Evaluation=`arXiv:2606.22942v1 — §Dataset and Evaluation Tasks; §3.5 Results and Analysis; §4.2 KD Results and Analysis in Domain-Specific Tasks`；counterevidence=`arXiv:2606.22942v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. 披露的 evaluation signal 是：Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22942:start -->
Primary identity `arXiv:2606.22942v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22942:end -->
<!-- review:SF-2026-ARXIV-2606-22942:end -->

<!-- review:SF-2026-ARXIV-2606-22948:start -->
### 2606.22948 — ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents

**问题与旧路径。** As multimodal agents move from interface understanding to real software control, successful trajectory discovery in live desktop environments becomes a key challenge. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents 的 exact-v1 机制为：We propose Environment-Native Verified Search (ENVS), a training-time search-and-filter pipeline that uses the environment to construct verified supervision before policy optimization: it branches over behaviorally distinct GUI actions in live OSWorld VMs, verifies successful leaves, and trains from globally balanced step-level supervision. 因此 把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state。 唯一 owner 为 `AGENT-PLANNING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22948v1 — §5.1 Experimental protocol; §Appendix C Evaluation pool construction`；Evaluation=`arXiv:2606.22948v1 — §4.3 Train/evaluation split; §Appendix C Evaluation pool construction`；counterevidence=`arXiv:2606.22948v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：As multimodal agents move from interface understanding to real software control, successful trajectory discovery in live desktop environments becomes a key challenge. 披露的 evaluation signal 是：To evaluate robustness under realistic desktop interruptions, we also introduce OSWorld-Noisy, a dynamic benchmark for recoverable desktop interruptions that preserves the original tasks while testing whether agents can refocus, dismiss, wait, or recover under live perturbations. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22948:start -->
Primary identity `arXiv:2606.22948v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22948:end -->
<!-- review:SF-2026-ARXIV-2606-22948:end -->

<!-- review:SF-2026-ARXIV-2606-22953:start -->
### 2606.22953 — Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents

**问题与旧路径。** Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents 的 exact-v1 机制为：We introduce replay pairing, a diagnostic that runs the same trajectory with and without the plan in history and measures hidden-state cosine distance. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。 唯一 owner 为 `AGENT-CONTEXT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22953v1 — §3 Method`；Evaluation=`arXiv:2606.22953v1 — §5.3 Lag Analysis: Early Warning; §A.2 Probe Validity Controls and Leakage Analysis; §A.8 Intervention Sweeps and Head-Level Analysis`；counterevidence=`arXiv:2606.22953v1 — §9 Discussion and Limitations`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 披露的 evaluation signal 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22953:start -->
Primary identity `arXiv:2606.22953v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22953:end -->
<!-- review:SF-2026-ARXIV-2606-22953:end -->

<!-- review:SF-2026-ARXIV-2606-22966:start -->
### 2606.22966 — Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models

**问题与旧路径。** We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models 的 exact-v1 机制为：A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。 唯一 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22966v1 — §3 Threat Model; §4 Method; §6 Mechanism: off-manifold is intrinsic to corrupting imagination`；Evaluation=`arXiv:2606.22966v1 — §5 Experiments; §5.1 Setup: three targets spanning the imagination-action coupling; §5.7 Adaptive attacker: the defense holds`；counterevidence=`arXiv:2606.22966v1 — §7 The task-level null, and why it motivates the oracle threat; §8 Limitations`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. 披露的 evaluation signal 是：We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22966:start -->
Primary identity `arXiv:2606.22966v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22966:end -->
<!-- review:SF-2026-ARXIV-2606-22966:end -->

<!-- review:SF-2026-ARXIV-2606-22968:start -->
### 2606.22968 — MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference

**问题与旧路径。** For long-context prefill, communication overhead grows with sequence length and quickly becomes a bottleneck on conventional GPU systems, making wafer-scale chips (WSCs) a promising substrate due to their high communication bandwidth and large aggregate compute and memory capacity. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference 的 exact-v1 机制为：To address these challenges, we present MOCAP, a memory-orchestrated chunked pipelining framework for prefill-only LLM inference on WSCs. 因此 把 wafer-scale memory orchestration、chunk pipeline 与 prefill-only 边界显式化。 唯一 owner 为 `INFER-PREFILL`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22968v1 — §MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference; §3.1 Memory Imbalance Limits Feasible Sequence Length; §4 MOCAP Framework`；Evaluation=`arXiv:2606.22968v1 — §5 Evaluation`；counterevidence=`arXiv:2606.22968v1 — §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：For long-context prefill, communication overhead grows with sequence length and quickly becomes a bottleneck on conventional GPU systems, making wafer-scale chips (WSCs) a promising substrate due to their high communication bandwidth and large aggregate compute and memory capacity. 披露的 evaluation signal 是：It further incorporates Latency-Balanced Chunk Partitioning (LBCP) to balance chunk execution cost under both attention-cost growth and KV reallocation overhead, improving pipeline efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22968:start -->
Primary identity `arXiv:2606.22968v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22968:end -->
<!-- review:SF-2026-ARXIV-2606-22968:end -->

<!-- review:SF-2026-ARXIV-2606-22977:start -->
### 2606.22977 — StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs

**问题与旧路径。** While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs 的 exact-v1 机制为：To bridge this gap, we introduce StatABench (Statistical AnalysisBenchmark), a benchmark designed to systematically assess LLMs' statistical analysis capabilities. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22977v1 — §StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs`；Evaluation=`arXiv:2606.22977v1 — §StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs; §3 The StatABench Benchmark; §3.4 Annotations and Evaluation`；counterevidence=`arXiv:2606.22977v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. 披露的 evaluation signal 是：While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22977:start -->
Primary identity `arXiv:2606.22977v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22977:end -->
<!-- review:SF-2026-ARXIV-2606-22977:end -->

<!-- review:SF-2026-ARXIV-2606-22983:start -->
### 2606.22983 — LiveServe: Interaction-Aware Serving for Real-Time Omni-Modal LLMs

**问题与旧路径。** Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** LiveServe: Interaction-Aware Serving for Real-Time Omni-Modal LLMs 的 exact-v1 机制为：LiveServe is an interaction-aware serving system for realtime Omni-LM interaction. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。 唯一 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.22983v1 — §3. OmniCast Architecture`；Evaluation=`arXiv:2606.22983v1 — §7. Experimental Evaluation; §7.1. Experiment Settings; §7.3. Analysis`；counterevidence=`arXiv:2606.22983v1 — §9. Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely. 披露的 evaluation signal 是：On vLLM-Omni, LiveServe improves realtime serving across two Omni-LMs and mixed workloads. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-22983:start -->
Primary identity `arXiv:2606.22983v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-22983:end -->
<!-- review:SF-2026-ARXIV-2606-22983:end -->

<!-- review:SF-2026-ARXIV-2606-23001:start -->
### 2606.23001 — EnerInfer: Energy-Aware On-Device LLM Inference

**问题与旧路径。** On-device LLM inference is increasingly attractive for privacy-preserving, reliable, and cost-effective deployment, yet its energy and thermal costs remain a critical bottleneck. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** EnerInfer: Energy-Aware On-Device LLM Inference 的 exact-v1 机制为：To address these challenges, we propose EnerInfer, the first on-device LLM inference framework that jointly manages energy efficiency, throughput, and thermal comfort for LLM workloads. 因此 把设备频率、功耗/温度估计、QoE 和模型/backend identity 联合验收。 唯一 owner 为 `INFER-GPU-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23001v1 — §4. Design of EnerInfer`；Evaluation=`arXiv:2606.23001v1 — §6.3. Thermal-aware controller evaluation`；counterevidence=`arXiv:2606.23001v1 — §4.6. Discussion; §8. Conclusion and Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：On-device LLM inference is increasingly attractive for privacy-preserving, reliable, and cost-effective deployment, yet its energy and thermal costs remain a critical bottleneck. 披露的 evaluation signal 是：We show instead that on-device LLM inference often has exploitable configuration slack: modestly lowering NPU and memory frequencies preserves quality of experience (QoE) while substantially improving energy efficiency and reducing heat. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23001:start -->
Primary identity `arXiv:2606.23001v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23001:end -->
<!-- review:SF-2026-ARXIV-2606-23001:end -->

<!-- review:SF-2026-ARXIV-2606-23003:start -->
### 2606.23003 — VCT: A Verifiable Transcript System for LLM Conversations

**问题与旧路径。** However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** VCT: A Verifiable Transcript System for LLM Conversations 的 exact-v1 机制为：However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23003v1 — §VCT: A Verifiable Transcript System for LLM Conversations; §3.2 System State and Storage Model; §3.4 Threat Model and Security Goals`；Evaluation=`arXiv:2606.23003v1 — §4.4 Security Analysis; §5 Experimental Evaluation; §5.1 Prototype System and Evaluation Scope`；counterevidence=`arXiv:2606.23003v1 — §5.1 Prototype System and Evaluation Scope; §5.8 Experimental Discussion; §6 Discussion and Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 披露的 evaluation signal 是：Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23003:start -->
Primary identity `arXiv:2606.23003v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23003:end -->
<!-- review:SF-2026-ARXIV-2606-23003:end -->

<!-- review:SF-2026-ARXIV-2606-23017:start -->
### 2606.23017 — Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems

**问题与旧路径。** Dynamic scheduling strategies mitigate this issue but introduce new trust concerns: verifying fair scheduling decisions and faithful client execution of compression instructions without privacy leakage remains an open challenge. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems 的 exact-v1 机制为：Federated Learning (FL) enables privacy-preserving collaborative learning for Internet of Vehicles (IoV) scenarios, but extreme heterogeneity of vehicular-edge-cloud resources severely limits system efficiency. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23017v1 — §Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems; §3.1 System Architecture and Role Definition; §3.2 Threat Model and Design Objectives`；Evaluation=`arXiv:2606.23017v1 — §5 Experiments and Analysis; §5.1.2 Evaluation Metrics; §5.3 Experimental Results and Analysis`；counterevidence=`arXiv:2606.23017v1 — §2.2 Trust Crisis: Failure of the Semi-Honest Assumption; §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Dynamic scheduling strategies mitigate this issue but introduce new trust concerns: verifying fair scheduling decisions and faithful client execution of compression instructions without privacy leakage remains an open challenge. 披露的 evaluation signal 是：First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23017:start -->
Primary identity `arXiv:2606.23017v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23017:end -->
<!-- review:SF-2026-ARXIV-2606-23017:end -->

<!-- review:SF-2026-ARXIV-2606-23026:start -->
### 2606.23026 — A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees

**问题与旧路径。** We formulate resource governance as a contextual Stackelberg game: a controller commits to a quality target and a cost incentive, while an executor responds with resource actions over context, prompting, and tool usage. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees 的 exact-v1 机制为：The theoretical results are conditional and the experiments do not estimate their regret or transfer constants; consequently, the evidence establishes a promising repaired operating point, not a certified real-system equilibrium. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23026v1 — §A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees; §3 Payoff Design; §6.4 Training Procedure`；Evaluation=`arXiv:2606.23026v1 — §4.1 Empirical Backward Induction; §9 Passive Shadow Evaluation Protocol; §10 Experimental Evaluation`；counterevidence=`arXiv:2606.23026v1 — §2.4 Modeling Scope and Assumptions; §11 Discussion; §14 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We formulate resource governance as a contextual Stackelberg game: a controller commits to a quality target and a cost incentive, while an executor responds with resource actions over context, prompting, and tool usage. 披露的 evaluation signal 是：We learn a conditional response model, optimize a leader policy against that model, and repair the resulting policy using real-API calibration and projection onto an empirically selected action set. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23026:start -->
Primary identity `arXiv:2606.23026v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23026:end -->
<!-- review:SF-2026-ARXIV-2606-23026:end -->

<!-- review:SF-2026-ARXIV-2606-23030:start -->
### 2606.23030 — Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models

**问题与旧路径。** Membership inference is a key tool for assessing such risks, but existing studies mainly focus on whether specific samples or sample-based data units are used for training. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models 的 exact-v1 机制为：Motivated by this question, we propose entity-level membership inference, which determines whether information related to a target entity is used in LLM training. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23030v1 — §IV Method; §IV-C Interrogation-specific Prompt Construction`；Evaluation=`arXiv:2606.23030v1 — §IV-B Theoretical Analysis; §V Evaluation; §V-B 2 Effectiveness Analysis of Different Interrogation Strategies`；counterevidence=`arXiv:2606.23030v1 — §VI Discussion; §VIII Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Membership inference is a key tool for assessing such risks, but existing studies mainly focus on whether specific samples or sample-based data units are used for training. 披露的 evaluation signal 是：We argue that LLMs exhibit a human-memory-like behavior: an LLM may not memorize a specific sample verbatim, yet it can accumulate and reveal knowledge about a real-world entity from scattered mentions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23030:start -->
Primary identity `arXiv:2606.23030v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23030:end -->
<!-- review:SF-2026-ARXIV-2606-23030:end -->

<!-- review:SF-2026-ARXIV-2606-23038:start -->
### 2606.23038 — EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning

**问题与旧路径。** However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning 的 exact-v1 机制为：We propose EvoRubrics, a co-evolutionary RL framework where a Policy LLM and a Rubric Generator jointly improve through adversarial interaction within each training step. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23038v1 — §4.1 Dual-LoRA Architecture; §4.4 Co-Evolutionary Training; §Appendix A EvoRubrics Algorithm`；Evaluation=`arXiv:2606.23038v1 — §2.2 Dynamic Rubrics and Adaptive Evaluation; §Appendix C Evaluation Details; §C.1 Policy LLM Evaluation`；counterevidence=`arXiv:2606.23038v1 — §6 Conclusions and Future Work; §E.3 Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 披露的 evaluation signal 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23038:start -->
Primary identity `arXiv:2606.23038v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23038:end -->
<!-- review:SF-2026-ARXIV-2606-23038:end -->

<!-- review:SF-2026-ARXIV-2606-23049:start -->
### 2606.23049 — PhoneBuddy: Training Open Models for Agentic Phone Use

**问题与旧路径。** The gains are strongest on app and mini-app tasks, while long-horizontal cross-app workflows remain an important open challenge. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** PhoneBuddy: Training Open Models for Agentic Phone Use 的 exact-v1 机制为：We present PhoneBuddy, a training recipe and open-model line for agentic phone use that combines a real-app environment with a mock-app environment, PhoneWorld, which reconstructs runnable mock apps from real GUI usage structure. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 唯一 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23049v1 — §3 Method; §3.5 Training Recipe; §4.2 Evaluation Protocol`；Evaluation=`arXiv:2606.23049v1 — §4.2 Evaluation Protocol`；counterevidence=`arXiv:2606.23049v1 — §7 Discussion and Limitations; §8 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：The gains are strongest on app and mini-app tasks, while long-horizontal cross-app workflows remain an important open challenge. 披露的 evaluation signal 是：Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23049:start -->
Primary identity `arXiv:2606.23049v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23049:end -->
<!-- review:SF-2026-ARXIV-2606-23049:end -->

<!-- review:SF-2026-ARXIV-2606-23075:start -->
### 2606.23075 — Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies

**问题与旧路径。** Self-evolving LLM agent systems, which autonomously update their model parameters, memory, tools, and architectures, introduce a qualitatively new threat landscape in which adversarial influences become permanently encoded, self-amplify across generations, and propagate through populations without sustained attacker access. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies 的 exact-v1 机制为：We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23075v1 — §2.3.1. Threat Model; §4. Cognitive Resource: Memory; §4.1. Bootstrap: Initial Memory`；Evaluation=`arXiv:2606.23075v1 — §3.3. Evaluate: Evaluation Oracle; §5.3. Selection: Tool Efficacy Evaluation; §6.3. Evaluate: Variant Fitness Evaluation`；counterevidence=`arXiv:2606.23075v1 — §10. Conclusion and Future Directions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Self-evolving LLM agent systems, which autonomously update their model parameters, memory, tools, and architectures, introduce a qualitatively new threat landscape in which adversarial influences become permanently encoded, self-amplify across generations, and propagate through populations without sustained attacker access. 披露的 evaluation signal 是：We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23075:start -->
Primary identity `arXiv:2606.23075v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23075:end -->
<!-- review:SF-2026-ARXIV-2606-23075:end -->

<!-- review:SF-2026-ARXIV-2606-23112:start -->
### 2606.23112 — Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning

**问题与旧路径。** Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning 的 exact-v1 机制为：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 唯一 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23112v1 — §4. Method; §4.1. Overall Architecture; §4.2.1. Graph Construction and Edge Weights`；Evaluation=`arXiv:2606.23112v1 — §5.3. Error Analysis; §5.5. DPO Training Analysis`；counterevidence=`arXiv:2606.23112v1 — §6. Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 披露的 evaluation signal 是：For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23112:start -->
Primary identity `arXiv:2606.23112v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23112:end -->
<!-- review:SF-2026-ARXIV-2606-23112:end -->

<!-- review:SF-2026-ARXIV-2606-23127:start -->
### 2606.23127 — Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation

**问题与旧路径。** Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation 的 exact-v1 机制为：We introduce AFTER, a benchmark of 382 realistic enterprise tasks spanning six professional roles and 22 procedural skills, designed to evaluate how skills transfer across tasks, roles, and model backbones. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23127v1 — §Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation; §2.1 Benchmark Design; §2.2 Benchmark Construction`；Evaluation=`arXiv:2606.23127v1 — §Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation; §2 AFTER : A Benchmark for Skill Transfer; §2.1 Benchmark Design`；counterevidence=`arXiv:2606.23127v1 — §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. 披露的 evaluation signal 是：Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23127:start -->
Primary identity `arXiv:2606.23127v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23127:end -->
<!-- review:SF-2026-ARXIV-2606-23127:end -->

<!-- review:SF-2026-ARXIV-2606-23130:start -->
### 2606.23130 — Understanding the (In)Security of Vibe-Coded Applications

**问题与旧路径。** We collect a large corpus of real-world applications developed using popular AI agents and design a vulnerability analysis framework that combines agent-assisted code auditing with human validation. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Understanding the (In)Security of Vibe-Coded Applications 的 exact-v1 机制为：We collect a large corpus of real-world applications developed using popular AI agents and design a vulnerability analysis framework that combines agent-assisted code auditing with human validation. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23130v1 — §III Dataset Construction; §III-B1 Multi-Agent Code Auditing; §III-B2 Vulnerability Deduplication and Validation`；Evaluation=`arXiv:2606.23130v1 — §IV RQ.1; §V RQ.2; §VI RQ.3; §VII RQ4`；counterevidence=`arXiv:2606.23130v1 — §VIII Discussion; §VIII-A Sources of Insecurity; §VIII-B Implications for Mitigation`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We collect a large corpus of real-world applications developed using popular AI agents and design a vulnerability analysis framework that combines agent-assisted code auditing with human validation. 披露的 evaluation signal 是：Our study reveals several key findings: (1) vibe-coded applications exhibit recurring vulnerability patterns that differ from those commonly observed in conventional software development workflows, including placeholder logic, unfiltered input, and secret exposure; (2) these vulnerabilities arise from systematic limitations of AI agents throughout the vibe-coding lifecycle, such as memory loss, locally optimized objectives and insufficient security knowledge; and (3) while advances in LLM capabilities and improved prompting strategies can reduce the inci 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23130:start -->
Primary identity `arXiv:2606.23130v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23130:end -->
<!-- review:SF-2026-ARXIV-2606-23130:end -->

<!-- review:SF-2026-ARXIV-2606-23181:start -->
### 2606.23181 — DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models

**问题与旧路径。** Hybrid reasoning models can answer directly or spend extra tokens on extended thinking. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models 的 exact-v1 机制为：We introduce DART, a training-free routing framework that samples two cheap no-think drafts, accepts direct answering when the drafts agree, and predicts a thinking budget from draft entropy when they disagree. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。 唯一 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23181v1 — §DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models; §2 Draft-Agreement Routing for Thinking; §2.2 Self-Consistency Routing`；Evaluation=`arXiv:2606.23181v1 — §5 Analysis; §5.2 Error Analysis; §Oracle routing analysis.`；counterevidence=`arXiv:2606.23181v1 — §7 Conclusion; §Task scope.; §Appendix F Multiple-Choice Task Scope`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Hybrid reasoning models can answer directly or spend extra tokens on extended thinking. 披露的 evaluation signal 是：Across the main comparisons, DART preserves or improves always-thinking accuracy in most settings while reducing thinking-token use. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23181:start -->
Primary identity `arXiv:2606.23181v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23181:end -->
<!-- review:SF-2026-ARXIV-2606-23181:end -->

<!-- review:SF-2026-ARXIV-2606-23189:start -->
### 2606.23189 — Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?

**问题与旧路径。** This cross-application access is useful, but it also creates a privacy risk that has been largely overlooked: when an agent works in one context, it can pull in information from another that is inappropriate in that context. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? 的 exact-v1 机制为：Hence, we introduce AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23189v1 — §3 Studying CUA Disclosure; §3.1 A taxonomy of CUA disclosure failures; §4 The AgentCIBench Harness`；Evaluation=`arXiv:2606.23189v1 — §5 Experimental Setup; §6 Do CUAs Follow Contextual Integrity?; §7 Do Disclosures Persist in End-to-End UI Interactions?`；counterevidence=`arXiv:2606.23189v1 — §9 Discussion and Policy Implications; §Task-completion rankings do not transfer to safety; §10 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：This cross-application access is useful, but it also creates a privacy risk that has been largely overlooked: when an agent works in one context, it can pull in information from another that is inappropriate in that context. 披露的 evaluation signal 是：Hence, we introduce AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23189:start -->
Primary identity `arXiv:2606.23189v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23189:end -->
<!-- review:SF-2026-ARXIV-2606-23189:end -->

<!-- review:SF-2026-ARXIV-2606-23195:start -->
### 2606.23195 — Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory

**问题与旧路径。** However, existing research assumes memories are derived from unbiased experiences. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory 的 exact-v1 机制为：Recent work shows that agent memories degrade during continuous consolidation. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23195v1 — §Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory; §3 Method; §3.2 Memory Store and Consolidation`；Evaluation=`arXiv:2606.23195v1 — §4.4 Results: Phase 4 (Dose-Response Analysis); §A.3 Retrieved Memory Analysis; §A.5 Sensitivity Analysis: Additive Model Assumption`；counterevidence=`arXiv:2606.23195v1 — §5 Discussion; §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, existing research assumes memories are derived from unbiased experiences. 披露的 evaluation signal 是：Recent work shows that agent memories degrade during continuous consolidation. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23195:start -->
Primary identity `arXiv:2606.23195v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23195:end -->
<!-- review:SF-2026-ARXIV-2606-23195:end -->

<!-- review:SF-2026-ARXIV-2606-23217:start -->
### 2606.23217 — MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations

**问题与旧路径。** This risk is structurally harder to control than in one-to-one settings, as every piece of private information must be appropriate for every recipient in the group. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations 的 exact-v1 机制为：We introduce MuPPET (Multi-Party Privacy Exposure Testing), a benchmark for contextual privacy in multi-party conversations. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23217v1 — §3 MuPPET: A Benchmark for Testing LLMs in Multi-Party Conversations; §3.1 Dataset Composition and Construction; §3.2 Metrics`；Evaluation=`arXiv:2606.23217v1 — §4 Experimental Setup; §5 Experimental Results; §A.6 Privacy and Utility Metrics Human Validation`；counterevidence=`arXiv:2606.23217v1 — §5.4 Error Analysis; §6 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：This risk is structurally harder to control than in one-to-one settings, as every piece of private information must be appropriate for every recipient in the group. 披露的 evaluation signal 是：Our experiments show that models leak substantially more in multi-party settings than one-to-one evaluations suggest. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23217:start -->
Primary identity `arXiv:2606.23217v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23217:end -->
<!-- review:SF-2026-ARXIV-2606-23217:end -->

<!-- review:SF-2026-ARXIV-2606-23276:start -->
### 2606.23276 — Exposing the Illusion of Erasure in Knowledge Editing for LLMs

**问题与旧路径。** Knowledge Editing (KE) has emerged as a frontier for updating specific facts in LLMs without costly retraining, but its reliability and underlying mechanisms remain poorly understood. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Exposing the Illusion of Erasure in Knowledge Editing for LLMs 的 exact-v1 机制为：In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23276v1 — §3 Reverse-Engineering Edits; §5 Mechanistic Analysis`；Evaluation=`arXiv:2606.23276v1 — §4 Results; §B Additional Experiments; §C Experimental Setup`；counterevidence=`arXiv:2606.23276v1 — §F Limitations, Broader Impacts, and Code + Reproducibility; §Limitations.`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Knowledge Editing (KE) has emerged as a frontier for updating specific facts in LLMs without costly retraining, but its reliability and underlying mechanisms remain poorly understood. 披露的 evaluation signal 是：In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23276:start -->
Primary identity `arXiv:2606.23276v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23276:end -->
<!-- review:SF-2026-ARXIV-2606-23276:end -->

<!-- review:SF-2026-ARXIV-2606-23277:start -->
### 2606.23277 — GIF: Locally Sound Geometric Information Flow Control for LLMs

**问题与旧路径。** Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** GIF: Locally Sound Geometric Information Flow Control for LLMs 的 exact-v1 机制为：We present Geometric Information Flow (GIF), a semantic framework for tracking information flow from input tokens to outputs. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23277v1 — §IV-B System Details; §V-B RQ2: How well does GIF detect policy violations with an LLM-as-a-declassifier design?`；Evaluation=`arXiv:2606.23277v1 — §III-C Operational Measurement of GIF; §V Evaluation; §V-C 2 Surrogate analysis models`；counterevidence=`arXiv:2606.23277v1 — §VII Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. 披露的 evaluation signal 是：Recent Information Flow Control (IFC)-based defenses show promise but lack a principled semantic foundation for reasoning about information flow through the model itself. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23277:start -->
Primary identity `arXiv:2606.23277v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23277:end -->
<!-- review:SF-2026-ARXIV-2606-23277:end -->

<!-- review:SF-2026-ARXIV-2606-23283:start -->
### 2606.23283 — Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs

**问题与旧路径。** However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs 的 exact-v1 机制为：Motivated by this challenge, we introduce root memory, a structured, decision-preserving representation that distills reusable personalized logic from long-term user histories. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23283v1 — §Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs; §2 The IMLogic Benchmark: Towards Implicit Logical Memory Retrieval; §2.3 Benchmark Construction`；Evaluation=`arXiv:2606.23283v1 — §2 The IMLogic Benchmark: Towards Implicit Logical Memory Retrieval; §2.3 Benchmark Construction; §4.1.1 Experiment Settings.`；counterevidence=`arXiv:2606.23283v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap. 披露的 evaluation signal 是：Current benchmarks remain inadequate for evaluating this problem. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23283:start -->
Primary identity `arXiv:2606.23283v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23283:end -->
<!-- review:SF-2026-ARXIV-2606-23283:end -->

<!-- review:SF-2026-ARXIV-2606-23321:start -->
### 2606.23321 — Tmax: A simple recipe for terminal agents

**问题与旧路径。** Terminal-using agents have quickly become the most popular downstream application of language models (LMs). 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Tmax: A simple recipe for terminal agents 的 exact-v1 机制为：We present Tmax, the strongest open RL recipe for terminal agents to date, bringing open data recipes closer to the frontier. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23321v1 — §2.2 RL training for Terminal Agents; §4 Training Terminal Agents; §Algorithm`；Evaluation=`arXiv:2606.23321v1 — §Evaluation; §Appendix E Additional Evaluation Details`；counterevidence=`arXiv:2606.23321v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Terminal-using agents have quickly become the most popular downstream application of language models (LMs). 披露的 evaluation signal 是：While simple, our recipe achieves 27\% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger models from prior work. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23321:start -->
Primary identity `arXiv:2606.23321v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23321:end -->
<!-- review:SF-2026-ARXIV-2606-23321:end -->

<!-- review:SF-2026-ARXIV-2606-23370:start -->
### 2606.23370 — FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation

**问题与旧路径。** During LLM inference, both the model weights and the user data are valuable, and attackers may compromise the OS kernel to steal them. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation 的 exact-v1 机制为：To address these challenges, this paper presents FlexServe, a fast and secure LLM inference system for mobile devices. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。 唯一 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23370v1 — §FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation; §3.1. Design Goals; §3.2. Threat Model`；Evaluation=`arXiv:2606.23370v1 — §7. Evaluation; §8.1. Security Analysis`；counterevidence=`arXiv:2606.23370v1 — §10. Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：During LLM inference, both the model weights and the user data are valuable, and attackers may compromise the OS kernel to steal them. 披露的 evaluation signal 是：The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23370:start -->
Primary identity `arXiv:2606.23370v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23370:end -->
<!-- review:SF-2026-ARXIV-2606-23370:end -->

<!-- review:SF-2026-ARXIV-2606-23403:start -->
### 2606.23403 — Litmus: Zero-Label, Code-Driven Metric Specification for Evaluating AI Systems

**问题与旧路径。** The challenge is not only that individual metrics may be unreliable, but that evaluation goals are often left implicit. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Litmus: Zero-Label, Code-Driven Metric Specification for Evaluating AI Systems 的 exact-v1 机制为：Without a clear account of what a system is expected to do, how it can fail, and which failures matter, metric choices become difficult to justify, interpret, or validate. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23403v1 — §3 The Litmus System; §3.1 Architecture Reconstruction; §3.3 Metric Design and Export`；Evaluation=`arXiv:2606.23403v1 — §4.1 Evaluation Domains; §4.3 Evaluation Axes; §C.1 Evaluation Axes`；counterevidence=`arXiv:2606.23403v1 — §6 Conclusion and Future Work; §Appendix A Reference Failure-Concerns`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：The challenge is not only that individual metrics may be unreliable, but that evaluation goals are often left implicit. 披露的 evaluation signal 是：As agentic LLM systems move from prototypes to deployment across increasingly diverse domains, evaluating them has become both more important and more difficult. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23403:start -->
Primary identity `arXiv:2606.23403v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23403:end -->
<!-- review:SF-2026-ARXIV-2606-23403:end -->

<!-- review:SF-2026-ARXIV-2606-23404:start -->
### 2606.23404 — ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models

**问题与旧路径。** The emergence of Large Reasoning Models has introduced exceptionally long Chain-of-Thought traces, creating a transparency burden where critical logic is often buried under massive procedural text. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models 的 exact-v1 机制为：To address this, we present ReasoningLens, an open-source framework designed for the hierarchical visualization and diagnostic auditing of complex reasoning chains. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23404v1 — §3 System Design; §4.1 Evaluation Dataset Construction; §Appendix B Human Verification Protocol`；Evaluation=`arXiv:2606.23404v1 — §4 Experiment; §4.1 Evaluation Dataset Construction; §5 Case Analysis`；counterevidence=`arXiv:2606.23404v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：The emergence of Large Reasoning Models has introduced exceptionally long Chain-of-Thought traces, creating a transparency burden where critical logic is often buried under massive procedural text. 披露的 evaluation signal 是：ReasoningLens addresses information necropsy by: (1) structuring traces into interactive hierarchies that separate high-level strategy from low-level execution; (2) leveraging an agentic auditor for automated error detection and tool-augmented verification; and (3) synthesizing systemic reasoning profiles to reveal model-specific blind spots. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23404:start -->
Primary identity `arXiv:2606.23404v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23404:end -->
<!-- review:SF-2026-ARXIV-2606-23404:end -->

<!-- review:SF-2026-ARXIV-2606-23416:start -->
### 2606.23416 — Detecting Malicious Agent Skills in the Wild using Attention

**问题与旧路径。** A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Detecting Malicious Agent Skills in the Wild using Attention 的 exact-v1 机制为：We present Locate-and-Judge, a two-stage detector designed for this regime. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23416v1 — §III Threat Model`；Evaluation=`arXiv:2606.23416v1 — §V-A 1 Locator evaluation`；counterevidence=`arXiv:2606.23416v1 — §VI Discussion; §VII Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. 披露的 evaluation signal 是：We release the resulting labeled dataset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23416:start -->
Primary identity `arXiv:2606.23416v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23416:end -->
<!-- review:SF-2026-ARXIV-2606-23416:end -->

<!-- review:SF-2026-ARXIV-2606-23449:start -->
### 2606.23449 — AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction

**问题与旧路径。** Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction 的 exact-v1 机制为：We present AOHP (Android Open Harness Project), an OS-level agent harness built on the Android Open Source Project (AOSP). 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23449v1 — §3 System Design; §8.3 System Safety, Provenance, and Recoverability`；Evaluation=`arXiv:2606.23449v1 — §7 Evaluation; §7.2 Efficiency Analysis; §Appendix A Benchmark Tasks`；counterevidence=`arXiv:2606.23449v1 — §9 Conclusion and Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. 披露的 evaluation signal 是：Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23449:start -->
Primary identity `arXiv:2606.23449v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23449:end -->
<!-- review:SF-2026-ARXIV-2606-23449:end -->

<!-- review:SF-2026-ARXIV-2606-23459:start -->
### 2606.23459 — TriggerBench: Investigating Prospective Memory for Large Language Models

**问题与旧路径。** Furthermore, PM accuracy degrades substantially under implicit constraints or triggers overloaded by concurrent user requests, indicating that robust PM remains an open challenge. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** TriggerBench: Investigating Prospective Memory for Large Language Models 的 exact-v1 机制为：We introduce TriggerBench, a comprehensive PM benchmark spanning five dimensions across both daily assistants and professional workflows. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23459v1 — §TriggerBench: Investigating Prospective Memory for Large Language Models; §3.2 Five Dimensions of Prospective Memory; §3.4 Construction Pipeline`；Evaluation=`arXiv:2606.23459v1 — §3.3 Contrastive Evaluation Variants; §3.6 Benchmark Overview; §4.3 Constraint Analysis: Explicit vs. Implicit`；counterevidence=`arXiv:2606.23459v1 — §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Furthermore, PM accuracy degrades substantially under implicit constraints or triggers overloaded by concurrent user requests, indicating that robust PM remains an open challenge. 披露的 evaluation signal 是：While Large Language Models (LLMs) are increasingly deployed in long interactions, existing evaluations focus predominantly on retrospective memory (RM) via explicit queries. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23459:start -->
Primary identity `arXiv:2606.23459v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23459:end -->
<!-- review:SF-2026-ARXIV-2606-23459:end -->

<!-- review:SF-2026-ARXIV-2606-23521:start -->
### 2606.23521 — Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference

**问题与旧路径。** Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference 的 exact-v1 机制为：We present Concordia, a runtime that uses a device-resident persistent kernel as the substrate for fault-tolerant LLM inference. 因此 把 persistent-kernel checkpoint、恢复位置和重复 token/side-effect 防护绑定。 唯一 owner 为 `INFER-DECODE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23521v1 — §3. Design; §Host-mapped memory.; §4.3. Optional Cross-Architecture Execution and GPU-Initiated Networking`；Evaluation=`arXiv:2606.23521v1 — §2.4. Motivating Experiment: Host-Side Dirty Detection; §5. Evaluation`；counterevidence=`arXiv:2606.23521v1 — §7. Discussion; §7.5. Limitations and Future Work; §8. Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component. 披露的 evaluation signal 是：The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23521:start -->
Primary identity `arXiv:2606.23521v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23521:end -->
<!-- review:SF-2026-ARXIV-2606-23521:end -->

<!-- review:SF-2026-ARXIV-2606-23525:start -->
### 2606.23525 — Self-Compacting Language Model Agents

**问题与旧路径。** Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Self-Compacting Language Model Agents 的 exact-v1 机制为：We propose SelfCompact, a scaffold that allows the model itself to decide when and how to compact. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23525v1 — §3 Our Approach: SelfCompact; §Summarizer design.; §Learning to compact during post-training.`；Evaluation=`arXiv:2606.23525v1 — §Cost analysis.; §Headroom analysis.; §Appendix C Cost analysis of summarization`；counterevidence=`arXiv:2606.23525v1 — §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 披露的 evaluation signal 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23525:start -->
Primary identity `arXiv:2606.23525v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23525:end -->
<!-- review:SF-2026-ARXIV-2606-23525:end -->

<!-- review:SF-2026-ARXIV-2606-23546:start -->
### 2606.23546 — The Energy Consumption of Transformer Fine-Tuning: A Roofline-Inspired Scaling Model

**问题与旧路径。** Transformer-based models underpin modern natural language processing but incur rapidly growing computational and energy costs. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Energy Consumption of Transformer Fine-Tuning: A Roofline-Inspired Scaling Model 的 exact-v1 机制为：As training scales in both model size and parallelism, accurately predicting energy consumption has become critical for sustainable and cost-aware system design. 因此 把训练/推理能耗模型、硬件 operating point 与质量边界联合报告。 唯一 owner 为 `PLATFORM-COST`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23546v1 — §2.2 Scale, Architecture, and Efficiency; §3.1 Tasks, Models and Training Protocol; §3.2 Compute, Parameter and Memory Proxies`；Evaluation=`arXiv:2606.23546v1 — §3.5 Hardware Efficiency via Empirical Speedup Models; §Appendix A Pre-Modeling Exploratory Data Analysis`；counterevidence=`arXiv:2606.23546v1 — §7 Discussion; §8 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Transformer-based models underpin modern natural language processing but incur rapidly growing computational and energy costs. 披露的 evaluation signal 是：We derive a scaling law model that accurately predicts training energy across heterogeneous configurations. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23546:start -->
Primary identity `arXiv:2606.23546v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23546:end -->
<!-- review:SF-2026-ARXIV-2606-23546:end -->

<!-- review:SF-2026-ARXIV-2606-23581:start -->
### 2606.23581 — Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse

**问题与旧路径。** Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse 的 exact-v1 机制为：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23581v1 — §3 The operator: relocate exactly, patch the conditioning; §5 Reuse beyond the window`；Evaluation=`arXiv:2606.23581v1 — §6 Fidelity, deployment, and cost; §C.1 Reuse breaks multi-hop accuracy; the patch restores it; §C.6 Memory cost and bf16-faithful live deployment`；counterevidence=`arXiv:2606.23581v1 — §Scope.; §B A menu of cross-chunk reuse operating points and its boundary; §D The reuse safety envelope: when a cached patch survives context drift`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. 披露的 evaluation signal 是：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23581:start -->
Primary identity `arXiv:2606.23581v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23581:end -->
<!-- review:SF-2026-ARXIV-2606-23581:end -->

<!-- review:SF-2026-ARXIV-2606-23583:start -->
### 2606.23583 — Evaluation Awareness Is Not One Capability: Evidence from Open Language Models

**问题与旧路径。** Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Evaluation Awareness Is Not One Capability: Evidence from Open Language Models 的 exact-v1 机制为：This opens a gap between benchmark performance and deployment behavior: compliance measured under test conditions becomes an optimistic upper bound that overstates how safely a model behaves once the evaluation harness is removed. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23583v1 — §3.1 Conceptual Framework; §[ RQ1 ] Detection is a training law more than a scaling law.; §[ RQ1 ] Detection is training-driven and distribution-fragile.`；Evaluation=`arXiv:2606.23583v1 — §Evaluation Awareness Is Not One Capability: Evidence from Open Language Models; §4 Empirical Setup; §5.1 Is evaluation awareness one trait?`；counterevidence=`arXiv:2606.23583v1 — §5 Results & Discussion; §9 Conclusion and Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. 披露的 evaluation signal 是：Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23583:start -->
Primary identity `arXiv:2606.23583v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23583:end -->
<!-- review:SF-2026-ARXIV-2606-23583:end -->

<!-- review:SF-2026-ARXIV-2606-23589:start -->
### 2606.23589 — KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies

**问题与旧路径。** However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies 的 exact-v1 机制为：In this work, we propose propose KEMO, a lightweight plug-in memory framework that automatically selectively preserves keyframes associated with task-relevant state changes for VLA policies. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23589v1 — §3 Method; §3.2 Framework Overview; §3.4 Keyframe Memory Integration`；Evaluation=`arXiv:2606.23589v1 — §4.3 Module Contribution Analysis`；counterevidence=`arXiv:2606.23589v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. 披露的 evaluation signal 是：We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23589:start -->
Primary identity `arXiv:2606.23589v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23589:end -->
<!-- review:SF-2026-ARXIV-2606-23589:end -->

<!-- review:SF-2026-ARXIV-2606-23617:start -->
### 2606.23617 — RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models

**问题与旧路径。** This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models 的 exact-v1 机制为：In this paper, we propose an active, continual learning paradigm for VLAs. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23617v1 — §3 Enabling Active, Continual Learning from Uncertainty-Guided Data; §3.1 Active Learning Pipeline; §3.2 Continual Learning Strategies`；Evaluation=`arXiv:2606.23617v1 — §4 Experiment Overview and General Setup; §5–§9 Experiments 1–5; §D Additional Experimental Results`；counterevidence=`arXiv:2606.23617v1 — §10 Summary and Conclusion; §11 Limitations`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. 披露的 evaluation signal 是：We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23617:start -->
Primary identity `arXiv:2606.23617v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23617:end -->
<!-- review:SF-2026-ARXIV-2606-23617:end -->

<!-- review:SF-2026-ARXIV-2606-23642:start -->
### 2606.23642 — Improving Long-Context Retrieval with Multi-Prefix Embedding

**问题与旧路径。** Long-context retrieval exposes a tension: single-vector embeddings lose fine-grained detail, while token-level multi-vector methods incur prohibitive storage. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Improving Long-Context Retrieval with Multi-Prefix Embedding 的 exact-v1 机制为：We propose Multi-Prefix Embedding (MPE), which partitions a document into chunks separated by EOS tokens, encodes the full sequence in a single causal forward pass, and extracts one embedding at each prefix boundary. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。 唯一 owner 为 `AGENT-RAG`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23642v1 — §3 Method; §3.1 Scoring, Training, and Retrieval; §3.2 Random Prefix-Length Augmentation`；Evaluation=`arXiv:2606.23642v1 — §4 Experiments; §4.1 Setup; §4.2 Main Results`；counterevidence=`arXiv:2606.23642v1 — §Storage overhead.; §Source attribution.; §5 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Long-context retrieval exposes a tension: single-vector embeddings lose fine-grained detail, while token-level multi-vector methods incur prohibitive storage. 披露的 evaluation signal 是：Experiments on MLDR-en, BrowseComp-Plus, and LongEmbed show that MPE is competitive with or outperforms single-vector, independent-chunk, and multi-vector baselines, while providing a natural source attribution mechanism for locating evidence chunks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23642:start -->
Primary identity `arXiv:2606.23642v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23642:end -->
<!-- review:SF-2026-ARXIV-2606-23642:end -->

<!-- review:SF-2026-ARXIV-2606-23654:start -->
### 2606.23654 — EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions

**问题与旧路径。** These results show that enterprise agent evaluation must report harness--model combinations, artifact delivery, visual quality, cost, runtime, and skill-transfer behavior, rather than collapsing performance into a single score. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions 的 exact-v1 机制为：We introduce EnterpriseClawBench, an enterprise agent benchmark constructed from proprietary, real-world agent sessions. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23654v1 — §2 EnterpriseClawBench Data and Construction; §Construction pipeline.; §B.1 End-to-End Construction Case`；Evaluation=`arXiv:2606.23654v1 — §Benchmark statistics.; §3.1 Evaluation Setting; §Rubric-dimension analysis.`；counterevidence=`arXiv:2606.23654v1 — §4 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：These results show that enterprise agent evaluation must report harness--model combinations, artifact delivery, visual quality, cost, runtime, and skill-transfer behavior, rather than collapsing performance into a single score. 披露的 evaluation signal 是：Because the sessions contain internal enterprise content, we do not release the benchmark data; instead, our reusable contribution is the construction and evaluation protocol. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23654:start -->
Primary identity `arXiv:2606.23654v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23654:end -->
<!-- review:SF-2026-ARXIV-2606-23654:end -->

<!-- review:SF-2026-ARXIV-2606-23664:start -->
### 2606.23664 — MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?

**问题与旧路径。** Although prompt optimization has shown substantial potential for single LLMs, extending it to MAS poses distinct challenges, notably an exponentially growing search space. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems? 的 exact-v1 机制为：Multi-agent systems (MAS) offer a scalable path forward for agentic AI, comprising multiple LLM-based agents, each assigned a system prompt and a position within a workflow that governs inter-agent coordination and output aggregation. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。 唯一 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23664v1 — §5.3 Communication Protocol; §B.2 Initial and Optimized System Prompt`；Evaluation=`arXiv:2606.23664v1 — §4 MAS-PromptBench: Prompt Optimization for MAS Benchmark; §5 Empirical Study of Prompt Optimization in MAS; §Appendix A Benchmark Details`；counterevidence=`arXiv:2606.23664v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Although prompt optimization has shown substantial potential for single LLMs, extending it to MAS poses distinct challenges, notably an exponentially growing search space. 披露的 evaluation signal 是：System prompts thus form a critical and accessible optimization surface: they specify agents' roles and behaviors, enabling system-level improvements without model finetuning. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23664:start -->
Primary identity `arXiv:2606.23664v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23664:end -->
<!-- review:SF-2026-ARXIV-2606-23664:end -->

<!-- review:SF-2026-ARXIV-2606-23671:start -->
### 2606.23671 — Can LLMs Reliably Self-Report Adversarial Prefills, and How?

**问题与旧路径。** We extend the question to safety contexts and examine how reliably a model can recognize that its own prior response was elicited by an adversarial prefill attack. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Can LLMs Reliably Self-Report Adversarial Prefills, and How? 的 exact-v1 机制为：We extend the question to safety contexts and examine how reliably a model can recognize that its own prior response was elicited by an adversarial prefill attack. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23671v1 — §A.2 Judge Prompts (Training Labels); §Safety protocol failure.; §Training data artifact.`；Evaluation=`arXiv:2606.23671v1 — §Per-benchmark recognition gap.`；counterevidence=`arXiv:2606.23671v1 — §Scope of the recognition signal.; §Byproduct and scope of the targeted intervention.; §Safety protocol failure.`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We extend the question to safety contexts and examine how reliably a model can recognize that its own prior response was elicited by an adversarial prefill attack. 披露的 evaluation signal 是：Prior work shows that large language models (LLMs) exhibit introspective capability on benign tasks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23671:start -->
Primary identity `arXiv:2606.23671v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23671:end -->
<!-- review:SF-2026-ARXIV-2606-23671:end -->

<!-- review:SF-2026-ARXIV-2606-23686:start -->
### 2606.23686 — LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

**问题与旧路径。** To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models 的 exact-v1 机制为：To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23686v1 — §3.4 Training Dataset; §Appendix 0.A Environment Design Details; §0.A.1 Preliminary: The BDDL Framework`；Evaluation=`arXiv:2606.23686v1 — §LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models; §2.3 Benchmarks for VLA Evaluation; §3 VLA Safety Benchmark`；counterevidence=`arXiv:2606.23686v1 — §4.4 Failure Case Analysis; §5 Conclusion; §Appendix 0.E Limitations and Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. 披露的 evaluation signal 是：We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23686:start -->
Primary identity `arXiv:2606.23686v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23686:end -->
<!-- review:SF-2026-ARXIV-2606-23686:end -->

<!-- review:SF-2026-ARXIV-2606-23752:start -->
### 2606.23752 — ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents

**问题与旧路径。** Each agent, however, persists its conversation in a private and vendor-specific log. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents 的 exact-v1 机制为：Each agent, however, persists its conversation in a private and vendor-specific log. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23752v1 — §ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents; §2.2 Agent Memory; §4 Architecture`；Evaluation=`arXiv:2606.23752v1 — §8 Self-Referential Case Study`；counterevidence=`arXiv:2606.23752v1 — §9 Discussion; §Validation Scope; §10 Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Each agent, however, persists its conversation in a private and vendor-specific log. 披露的 evaluation signal 是：The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23752:start -->
Primary identity `arXiv:2606.23752v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23752:end -->
<!-- review:SF-2026-ARXIV-2606-23752:end -->

<!-- review:SF-2026-ARXIV-2606-23754:start -->
### 2606.23754 — Verifiable Foundation Models for Robot Safety

**问题与旧路径。** Deploying foundation models for robot control raises a central challenge: the expressive power that enables rich, multimodal perception also makes these models opaque and difficult to analyze formally, rendering them intractable for existing verification tools. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Verifiable Foundation Models for Robot Safety 的 exact-v1 机制为：In this paper, we present FEARL (Foundation-Enabled Assured Robot Learning), a framework that addresses this tension through a modular architectural decomposition. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23754v1 — §3 The FEARL Architecture; §4 Enabling Verification via Decomposition; §4.1 Theoretical Guarantees`；Evaluation=`arXiv:2606.23754v1 — §5 Experiments; §5.1 Experimental Setup; §5.3 Does the Decomposition Enable Verification?`；counterevidence=`arXiv:2606.23754v1 — §6 Discussion and Conclusion; §A Proof of Propositions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Deploying foundation models for robot control raises a central challenge: the expressive power that enables rich, multimodal perception also makes these models opaque and difficult to analyze formally, rendering them intractable for existing verification tools. 披露的 evaluation signal 是：To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23754:start -->
Primary identity `arXiv:2606.23754v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23754:end -->
<!-- review:SF-2026-ARXIV-2606-23754:end -->

<!-- review:SF-2026-ARXIV-2606-23768:start -->
### 2606.23768 — Cryptographic certificates of validity for trustworthy AI

**问题与旧路径。** We propose cryptographic certificates of validity for agentic AI systems. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Cryptographic certificates of validity for trustworthy AI 的 exact-v1 机制为：We propose cryptographic certificates of validity for agentic AI systems. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23768v1 — §2 A compact slice of maths; §4 How to apply this mathematics to AI agents`；Evaluation=`arXiv:2606.23768v1 — §3 Examples; §3.2 A recursive example`；counterevidence=`arXiv:2606.23768v1 — §5 Related work; §6 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We propose cryptographic certificates of validity for agentic AI systems. 披露的 evaluation signal 是：We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23768:start -->
Primary identity `arXiv:2606.23768v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23768:end -->
<!-- review:SF-2026-ARXIV-2606-23768:end -->

<!-- review:SF-2026-ARXIV-2606-23797:start -->
### 2606.23797 — From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes

**问题与旧路径。** Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes 的 exact-v1 机制为：We introduce the Goal-Oriented Dialogue Runtime (GODR), a framework-neutral design pattern that treats goals, task frames, lifecycle state, invalidation rules, and resumption contracts as first-class runtime objects while delegating bounded execution to graph runtimes, agents, tools, or application programming interfaces (APIs). 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23797v1 — §9.5 Turn-Level Algorithm; §10 Design Principles; §11 Evaluation Protocol`；Evaluation=`arXiv:2606.23797v1 — §11 Evaluation Protocol`；counterevidence=`arXiv:2606.23797v1 — §15 Contributions, Scope, and Validity; §16 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 披露的 evaluation signal 是：The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23797:start -->
Primary identity `arXiv:2606.23797v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23797:end -->
<!-- review:SF-2026-ARXIV-2606-23797:end -->

<!-- review:SF-2026-ARXIV-2606-23858:start -->
### 2606.23858 — Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications

**问题与旧路径。** A primary challenge in AI safety is the existence of adversarial examples -- slightly distorted inputs that cause a neural network (NN) to misclassify. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications 的 exact-v1 机制为：We introduce the apothem measure and show how to compute apothem-optimal certifications in a linear number of calls to a NN verifier (oracle) w.r.t. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23858v1 — §3 Robustness Operators; §4 Algorithms; §4.2 Refine & Check Algorithm`；Evaluation=`arXiv:2606.23858v1 — §5 Implementation; §Experimental Setup.; §Experimental Results.`；counterevidence=`arXiv:2606.23858v1 — §4.3 The Complexity of Apothem Optimality; §4.4 The Intractability of Volume Optimality; §7 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A primary challenge in AI safety is the existence of adversarial examples -- slightly distorted inputs that cause a neural network (NN) to misclassify. 披露的 evaluation signal 是：Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23858:start -->
Primary identity `arXiv:2606.23858v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23858:end -->
<!-- review:SF-2026-ARXIV-2606-23858:end -->

<!-- review:SF-2026-ARXIV-2606-23872:start -->
### 2606.23872 — MGI: Member vs Generated Inference

**问题与旧路径。** We formalize this challenge as Member vs Generated Inference (MGI): given a sample and a target generative model, infer whether the sample is a true training member or a generated output of that model. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** MGI: Member vs Generated Inference 的 exact-v1 机制为：To address MGI, we propose Data Circuit Breaker (DCB), a three-stage method that combines complementary signals from a generative model's autoencoder and latent generator to distinguish training members from generated samples. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23872v1 — §3 Member vs Generated Inference; §5 Proposed Data Circuit Breaker; §5.3 Attribution Protocol`；Evaluation=`arXiv:2606.23872v1 — §6 Empirical Evaluation; §6.1 Experimental Setup; §6.2 Evaluation on the Direct Training Setting`；counterevidence=`arXiv:2606.23872v1 — §4 Limitations of MIA and Attribution Methods; §4.1 CPD-based Methods Fall Short for MGI; §7 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We formalize this challenge as Member vs Generated Inference (MGI): given a sample and a target generative model, infer whether the sample is a true training member or a generated output of that model. 披露的 evaluation signal 是：Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23872:start -->
Primary identity `arXiv:2606.23872v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23872:end -->
<!-- review:SF-2026-ARXIV-2606-23872:end -->

<!-- review:SF-2026-ARXIV-2606-23892:start -->
### 2606.23892 — REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs

**问题与旧路径。** Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs 的 exact-v1 机制为：We introduce REALM, to our knowledge the first unified red-teaming benchmark for physical-world VLMs. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23892v1 — §Black-box threat model.; §Appendix D Attack Method Details; §Appendix E Defense Method Details`；Evaluation=`arXiv:2606.23892v1 — §ReaLM : A Unified Red-Teaming Benchmark for Physical-World VLMs; §2.2 Red-Teaming Benchmark; §3 ReaLM : Benchmark for Physical-World VLMs`；counterevidence=`arXiv:2606.23892v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 披露的 evaluation signal 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23892:start -->
Primary identity `arXiv:2606.23892v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23892:end -->
<!-- review:SF-2026-ARXIV-2606-23892:end -->

<!-- review:SF-2026-ARXIV-2606-23915:start -->
### 2606.23915 — Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs

**问题与旧路径。** This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs 的 exact-v1 机制为：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23915v1 — §3 A Sentence-Unit Provenance-Ranking Score; §3.1 Provenance/topicality`；Evaluation=`arXiv:2606.23915v1 — §4 The Cross-Dataset Audit; §5 ERCR as a Boundary Probe; §F Independent Replication and Robustness`；counterevidence=`arXiv:2606.23915v1 — §An external boundary: long-form alone does not predict the NLI failure.; §7 Limitations`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. 披露的 evaluation signal 是：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23915:start -->
Primary identity `arXiv:2606.23915v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23915:end -->
<!-- review:SF-2026-ARXIV-2606-23915:end -->

<!-- review:SF-2026-ARXIV-2606-23927:start -->
### 2606.23927 — RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems

**问题与旧路径。** Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems 的 exact-v1 机制为：To address this gap, we introduce RIFT-Bench, a graph representation-driven methodology for dynamic red-teaming that enables unified evaluations across diverse agentic architectures. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23927v1 — §4 NodeSpec: System Representation; §6 RIFT-Bench Framework; §F.2 Framework and Architecture Matrix`；Evaluation=`arXiv:2606.23927v1 — §7.1 Structure Identifier Evaluation; §Appendix A Additional Comparison to Agentic Security Evaluation; §E.3 Evaluation Metrics`；counterevidence=`arXiv:2606.23927v1 — §8 Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. 披露的 evaluation signal 是：Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23927:start -->
Primary identity `arXiv:2606.23927v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23927:end -->
<!-- review:SF-2026-ARXIV-2606-23927:end -->

<!-- review:SF-2026-ARXIV-2606-23937:start -->
### 2606.23937 — When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents

**问题与旧路径。** Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents 的 exact-v1 机制为：We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23937v1 — §Sensitivity to domain and query construction.`；Evaluation=`arXiv:2606.23937v1 — §Decision models and evaluation.; §Analysis of informative nonmatching clauses.; §B.1 Primary 3B result`；counterevidence=`arXiv:2606.23937v1 — §Contribution and scope.; §Construct scope.; §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. 披露的 evaluation signal 是：Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23937:start -->
Primary identity `arXiv:2606.23937v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23937:end -->
<!-- review:SF-2026-ARXIV-2606-23937:end -->

<!-- review:SF-2026-ARXIV-2606-23961:start -->
### 2606.23961 — Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets

**问题与旧路径。** To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets 的 exact-v1 机制为：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23961v1 — §2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection`；Evaluation=`arXiv:2606.23961v1 — §5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations`；counterevidence=`arXiv:2606.23961v1 — §7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23961:start -->
Primary identity `arXiv:2606.23961v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23961:end -->
<!-- review:SF-2026-ARXIV-2606-23961:end -->

<!-- review:SF-2026-ARXIV-2606-23969:start -->
### 2606.23969 — The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing

**问题与旧路径。** We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing 的 exact-v1 机制为：Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23969v1 — §3 Platforms and Method; §4.1 Compute and GPU-Local Memory Are at Parity; §5.6 Runtime Design Rule`；Evaluation=`arXiv:2606.23969v1 — §3.3 Experiment Families; §5 Case Study: Policy Inversion in the Serving Runtime; §6 Case Study: Movement Engineering for Loading and KV State`；counterevidence=`arXiv:2606.23969v1 — §3.4 Comparability and Claim Scope; §11 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 披露的 evaluation signal 是：We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23969:start -->
Primary identity `arXiv:2606.23969v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23969:end -->
<!-- review:SF-2026-ARXIV-2606-23969:end -->

<!-- review:SF-2026-ARXIV-2606-23983:start -->
### 2606.23983 — Maestro Order: A Model-Agnostic Orchestration Harness

**问题与旧路径。** The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Maestro Order: A Model-Agnostic Orchestration Harness 的 exact-v1 机制为：We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23983v1 — §3. From Algebra to Architecture; §4. Harness Architecture; §5. Design Rationale and System Invariants`；Evaluation=`arXiv:2606.23983v1 — §12. Evaluation Methodology; §Simulation study (this paper).`；counterevidence=`arXiv:2606.23983v1 — §15. Discussion: Failure Modes and Guidance; §16. Limitations and Threats to Validity; §17. Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 披露的 evaluation signal 是：We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23983:start -->
Primary identity `arXiv:2606.23983v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23983:end -->
<!-- review:SF-2026-ARXIV-2606-23983:end -->

<!-- review:SF-2026-ARXIV-2606-23989:start -->
### 2606.23989 — Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization

**问题与旧路径。** End-to-end large language models (LLMs) produce fluent multi-document summaries but remain prone to hallucination, and the attributions they offer are typically coarse (whole documents or passages) and generated post hoc, leaving each summary statement hard to verify. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization 的 exact-v1 机制为：We present CAMS, a Claim-Anchored Multi-document Summarization framework that (i) extracts atomic claims with token-level provenance from every source document, (ii) clusters equivalent claims across documents while flagging inter-source conflicts, (iii) selects a support-aware and salient subset, and (iv) rewrites the selection into a summary in which every sentence is anchored to a support-checked claim that links back to one or more source spans. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。 唯一 owner 为 `AGENT-RAG`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23989v1 — §Attribution by Construction: Claim-Anchored Evidence for Faithfulness-Oriented Multi-Document Summarization; §3 Method; §Training labels by distant supervision.`；Evaluation=`arXiv:2606.23989v1 — §Faithful summarization and its evaluation.; §4.3 Evaluation Protocol; §5 Results and Analysis`；counterevidence=`arXiv:2606.23989v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：End-to-end large language models (LLMs) produce fluent multi-document summaries but remain prone to hallucination, and the attributions they offer are typically coarse (whole documents or passages) and generated post hoc, leaving each summary statement hard to verify. 披露的 evaluation signal 是：We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23989:start -->
Primary identity `arXiv:2606.23989v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23989:end -->
<!-- review:SF-2026-ARXIV-2606-23989:end -->

<!-- review:SF-2026-ARXIV-2606-24004:start -->
### 2606.24004 — Towards Spec Learning: Inference-Time Alignment from Preference Pairs

**问题与旧路径。** Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Towards Spec Learning: Inference-Time Alignment from Preference Pairs 的 exact-v1 机制为：We propose spec learning, a framework that relies on a brief user instruction and a small set of preference judgments. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24004v1 — §4 Spec Learning Framework; §4.1 Selection Method; §4.4 Judge protocol and selection`；Evaluation=`arXiv:2606.24004v1 — §5 Results; §B Statistical robustness; §C Judge calibration`；counterevidence=`arXiv:2606.24004v1 — §6 Discussion; §7 Limitations; §8 Conclusions and Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 披露的 evaluation signal 是：We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24004:start -->
Primary identity `arXiv:2606.24004v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24004:end -->
<!-- review:SF-2026-ARXIV-2606-24004:end -->

<!-- review:SF-2026-ARXIV-2606-24020:start -->
### 2606.24020 — You Don't Need to Run Every Eval

**问题与旧路径。** A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** You Don't Need to Run Every Eval 的 exact-v1 机制为：Building on this, we design BenchPress: a logit-space rank-2 matrix completion method that recovers held-out scores to within 4.6 points, and a confidence layer that says when each prediction can be trusted. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24020v1 — §You Don’t Need to Run Every Eval Yuchen Zeng & Dimitris Papailiopoulos; §1 Introduction [You Don't Need to Run Every Eval exact-v1 method boundary]`；Evaluation=`arXiv:2606.24020v1 — §4 BenchPress : A Low-rank Benchmark Score Predictor; §4.3 BenchPress vs. LLMs as Benchmark Score Predictors; §5 What BenchPress Enables for Model Evaluation`；counterevidence=`arXiv:2606.24020v1 — §7 Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 披露的 evaluation signal 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24020:start -->
Primary identity `arXiv:2606.24020v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24020:end -->
<!-- review:SF-2026-ARXIV-2606-24020:end -->

<!-- review:SF-2026-ARXIV-2606-24033:start -->
### 2606.24033 — RoPE-Aware Bit Allocation for KV-Cache Quantization

**问题与旧路径。** Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RoPE-Aware Bit Allocation for KV-Cache Quantization 的 exact-v1 机制为：We introduce Block-GTQ, a RoPE-aware bit allocator for key-cache quantization built on TurboQuant-MSE(TQ-MSE). 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24033v1 — §RoPE-Aware Bit Allocation for KV-Cache Quantization; §1 Introduction [RoPE-Aware Bit Allocation for KV-Cache Quantization exact-v1 method boundary]`；Evaluation=`arXiv:2606.24033v1 — §6.3 Downstream Evaluation`；counterevidence=`arXiv:2606.24033v1 — §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24033:start -->
Primary identity `arXiv:2606.24033v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24033:end -->
<!-- review:SF-2026-ARXIV-2606-24033:end -->

<!-- review:SF-2026-ARXIV-2606-24040:start -->
### 2606.24040 — Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo

**问题与旧路径。** MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo 的 exact-v1 机制为：We propose a version-aware operation layer in which high-level operations such as replace, obsolete, keep-history, rollback, and trace are compiled into MeMo-native primitive calls over sequences and tokens. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24040v1 — §3 Version-aware Operations; §4 Version and Transaction Correlation Memories`；Evaluation=`arXiv:2606.24040v1 — §5 Examples; §5.1 Direct sequence-level replacement; §5.2 Structured diff-level update`；counterevidence=`arXiv:2606.24040v1 — §6 Evaluation Roadmap and Scope; §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 披露的 evaluation signal 是：This paper asks how such memories can reduce the need for retraining when knowledge changes. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24040:start -->
Primary identity `arXiv:2606.24040v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24040:end -->
<!-- review:SF-2026-ARXIV-2606-24040:end -->

<!-- review:SF-2026-ARXIV-2606-24551:start -->
### 2606.24551 — GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents

**问题与旧路径。** In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents 的 exact-v1 机制为：We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 唯一 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24551v1 — §3.2 Benchmark Construction; §A.3 Visual Design Example`；Evaluation=`arXiv:2606.24551v1 — §3 Benchmark; §3.1 Benchmark Scope and Composition; §3.2 Benchmark Construction`；counterevidence=`arXiv:2606.24551v1 — §3.1 Benchmark Scope and Composition; §UI Navigation and Control Discovery Failure.; §Workflow Execution Failure.`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 披露的 evaluation signal 是：Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24551:start -->
Primary identity `arXiv:2606.24551v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24551:end -->
<!-- review:SF-2026-ARXIV-2606-24551:end -->

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

<!-- review:SF-2026-ARXIV-2606-28385:start -->
### 2606.28385 — RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis

**问题与旧路径。** However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis 的 exact-v1 机制为：We present RoboGaze, a training-free, multi-agent VLM framework that provides structured, interpretable evaluation for generated robot-manipulation videos. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。 唯一 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.28385v1 — §3 Method; §4.2 Evaluation Protocol; §A.2.1 Dataset Construction`；Evaluation=`arXiv:2606.28385v1 — §RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis; §3.3 Candidate Discovery and Specialist Analysis; §4.2 Evaluation Protocol`；counterevidence=`arXiv:2606.28385v1 — §5 Conclusion; §A.4.8 Scope of Learned-Evaluator Comparisons`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 披露的 evaluation signal 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-28385:start -->
Primary identity `arXiv:2606.28385v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-28385:end -->
<!-- review:SF-2026-ARXIV-2606-28385:end -->

<!-- review:SF-2026-ARXIV-2606-28386:start -->
### 2606.28386 — Data Provenance for Image Auto-Regressive Generation

**问题与旧路径。** Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Data Provenance for Image Auto-Regressive Generation 的 exact-v1 机制为：Leveraging this, we present a post-hoc framework that enables the robust detection of such patterns for provenance tracing. 因此 把任务/样本生成、可执行验证、过滤与训练 lineage 绑定。 唯一 owner 为 `TRAIN-DATA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.28386v1 — §3 Method; §3.3 A Framework for Data Provenance in IARs; §3.3.1 QuantLoss`；Evaluation=`arXiv:2606.28386v1 — §4 Empirical Evaluation; §4.1 Experimental Setup; §4.2–§4.4 Results and Ablations`；counterevidence=`arXiv:2606.28386v1 — §R Adaptive Attack; §W Comparison with Membership Inference Baselines; §5 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 披露的 evaluation signal 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-28386:start -->
Primary identity `arXiv:2606.28386v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-28386:end -->
<!-- review:SF-2026-ARXIV-2606-28386:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-22741 | GRADE: Graph Representation of LLM Agent Dependency and Execution — A trace records what each step did, never what it relied on, the state it read, and the results it reused. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Meanwhile, the execution layer localizes the faulting step in a failed multi-agent run. | Not Disclosed | A trace records what each step did, never what it relied on, the state it read, and the results it reused. |
| SF-2026-ARXIV-2606-22768 | Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo — To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. | Not Disclosed | We assume single-GPU workers on consumer networks, roughly 50Mbps–1Gbps, rather than multi-GPU datacenter nodes with 10–100Gbps links. In our setup, we use 8 workers, each with a 40GB A100 GPU. | Not Disclosed | We train with a sequence length of 1024 and a batch size of 512. | Not Disclosed | Here, local denotes pairwise gossip averaging, global denotes full averaging across all replicas, and GBS is the global batch size (per-worker batch is GBS / M \text{GBS}/M ). We train with a sequence length of 1024 and a batch size of 512. | This allows us to factorize DiLoCo synchronization into a non-blocking mixing step that overlaps computation with no staleness, and a blocking mixing step that tightens worker agreement, yielding a tunable trade-off between compute utilization and optimization stability. | To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. | To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. |
| SF-2026-ARXIV-2606-22778 | HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions — HAKARI-Bench does not replace full evaluation; it enables rapid model selection, regression detection, and reading the quality-efficiency Pareto frontier. | BM25 | Score computation and top- k k extraction are, in principle, done on the same device (CPU or GPU) as the base embeddings. When scoring int8/binary quantization on GPU, values are cast to float32 for matrix multiplication; this cast is numerically equivalent and does not affect quality. | Dimensionality reduction, quantization, and sparse pruning are evaluated as reproducible proxies for storage and retrieval cost (embedding dimension, quantization precision, number of non-zero dimensions); we do not evaluate the inference speed itself of each model, because fair measurement is difficult ( § 7.5 ). Here a Pareto frontier is the set of settings on the two axes of quality and efficiency (embedding dimension, quantization precision, etc.) that cannot be beaten without worsening one of the two; i.e., the locus of best quality reachable for a given efficiency, and conversely the locus of minimum cost r | Speed strongly depends on hardware, batch size, sequence length, and parallelism, and the availability of recommended implementations and optimized attention (FlashAttention-2; Dao, 2023 ) differs per model, so drawing out every model’s “best speed” fairly under the same conditions is difficult, and inappropriate measurement would mislead model selection. Both are useful as a first-order approximation of relative compute scale across families/models, but actual inference speed strongly depends, as noted, on implementation, hardware, sequence length, batch size, and optimization, and is not uniquely determined by  | Not Disclosed | Speed strongly depends on hardware, batch size, sequence length, and parallelism, and the availability of recommended implementations and optimized attention (FlashAttention-2; Dao, 2023 ) differs per model, so drawing out every model’s “best speed” fairly under the same conditions is difficult, and inappropriate measurement would mislead model selection. Both are useful as a first-order approximation of relative compute scale across families/models, but actual inference speed strongly depends, as noted, on implementation, hardware, sequence length, batch size, and optimization, and is not uniquely determined by  | Not Disclosed | Not Disclosed | HAKARI-Bench does not replace full evaluation; it enables rapid model selection, regression detection, and reading the quality-efficiency Pareto frontier. |
| SF-2026-ARXIV-2606-22783 | Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints — Evaluating the exhaustive search capabilities of large language models (LLMs) is plagued by a fundamental paradox: verifying completeness requires complete ground truth, yet high-entropy enumeration tasks make such ground truth impossible for humans to create. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | VERITAS can automatically generate a virtually infinite number of test cases with perfect ground truth and precise difficulty control, with marginal instance cost dominated by hash computations. | Evaluating the exhaustive search capabilities of large language models (LLMs) is plagued by a fundamental paradox: verifying completeness requires complete ground truth, yet high-entropy enumeration tasks make such ground truth impossible for humans to create. |
| SF-2026-ARXIV-2606-22792 | The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models — While traditional uncertainty taxonomy paradigms, such as the dichotomy of aleatoric and epistemic uncertainties, provide conceptual foundations, they often fail to capture the multi-component and multi-stage nature of LLM generation and struggle to evaluate the effectiveness of various Uncertainty Quantification (UQ) methods. | DeepSeek-V3, Llama, Qwen, Qwen3 | 3.1 Configurations All experiments are conducted on one NVIDIA RTX 6000 GPU. | Common ranking-oriented metrics include Area Under the Receiver Operating Characteristic (AUROC), Area Under the Precision-Recall Curve (AUPRC), and Area Under the Accuracy-Rejection Curve (AUARC). This finding has motivated subsequent research ( Llama, 2024 ; Qwen, 2025 ) and industrial efforts ( OpenAI, 2023 ) to improve predictive precision of LLMs by scaling up parameter counts. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | While traditional uncertainty taxonomy paradigms, such as the dichotomy of aleatoric and epistemic uncertainties, provide conceptual foundations, they often fail to capture the multi-component and multi-stage nature of LLM generation and struggle to evaluate the effectiveness of various Uncertainty Quantification (UQ) methods. |
| SF-2026-ARXIV-2606-22794 | UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models — Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). | Not Disclosed | All experiments are conducted on 4 NVIDIA A100 GPUs using Distributed Data Parallel training. | Moreover, because the action expert receives only the VLM’s final-layer representation at a single fixed frequency, rich intermediate features are discarded, limiting both information coupling and manipulation precision. π 0.5 \pi_{0.5} [ 16 ] , X-VLA [ 54 ] , MemoryVLA [ 35 ] ) have further enhanced precision by shifting from discrete tokens to continuous action spaces via iterative decoding (e.g. | Not Disclosed | Not Disclosed | We use a per-GPU mini-batch size of 16, resulting in a global batch size of 64. , temporal batch size), training with the proposed frequency feature replacement strategy yields a 2.5 % 2.5\% improvement and is also more efficient, demonstrating the effectiveness of our fast-to-slow architecture. | Not Disclosed | Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). | Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). |
| SF-2026-ARXIV-2606-22798 | Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control — Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on. | Qwen3-30B-A3B, Qwen3-MoE, Qwen3-Next-80B-A3B, gpt-oss, gpt-oss-120B, gpt-oss-20B | Captured tensors are buffered on the GPU and copied to CPU staging buffers at request boundaries; we do not modify model weights, KV caches, or any compute path. | Family Total / Active Layers Experts Top- k k Attention gpt-oss-20B 21B / 3.6B 24 32 4 alternating full / banded + GQA gpt-oss-120B 117B / 5.1B 36 128 4 alternating full / banded + GQA Qwen3-30B-A3B 30.5B / 3.3B 48 128 8 GQA (32 Q / 4 KV) Qwen3-Next-80B-A3B 80B / 3B 48 512 + 1 shared 10 + shared Gated DeltaNet + Gated Attention All weights are stored at float16 precision regardless of the model’s inference quantization (e.g., mxfp4 on gpt-oss). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on. |
| SF-2026-ARXIV-2606-22804 | CoVStream: Edge-Cloud Collaboration for Understanding of Long Video Streams — Experiments on VideoMME-Long, LVBench, and RTV-Bench show that CoVStream reduces bandwidth usage by 87.6% while retaining 99.2% of the cloud baseline accuracy on LVBench. | Not Disclosed | All our experiments are conducted on an NVIDIA A40 (48GB). For broader context, NVIDIA Jetson Thor delivers 162.3 TFLOPS of dense FP16 tensor-core performance, and we also provide a real-phone demo video in the supplementary material. | The 5.9 TFLOPs requirement is measured in Dense BF16 precision. | Not Disclosed | Not Disclosed | Not Disclosed | However, they overlook a crucial deployment fact: the stream is often produced by computationally constrained devices. | This forces an untenable compromise: cloud offloading unlocks strong reasoning but incurs prohibitive bandwidth overhead, while on-device processing remains limited by edge hardware capacity. | Experiments on VideoMME-Long, LVBench, and RTV-Bench show that CoVStream reduces bandwidth usage by 87.6% while retaining 99.2% of the cloud baseline accuracy on LVBench. |
| SF-2026-ARXIV-2606-22826 | MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration — Evaluating LLMs across many model variants -- quantized, fine-tuned, or deployment-specific -- requires running large benchmarks repeatedly, a process that can take tens of hours per model on edge hardware such as NPUs. | Llama-3.1-8B, Llama-3.1-8B-Inst, Mistral-7B-Inst, Qwen2.5-3B-Inst, Qwen3-8B, Qwen3.5-35B-A3B | 5 Results 5.1 MINCE Overall Results NPU Validation Wall-clock Savings 5.2 Monte Carlo N-Sizing 5.3 Subset Selection Strategy Ablation 5.4 Calibration Guidelines 5.5 Comparison to TinyBenchmarks 6 Conclusion References A Leave- K K -Out: Full Results B K-Means Clustering Details C IFEVAL Per-Metric Accuracy Breakdown D Threshold Sensitivity Analysis E GPU Evaluation Speedup Breakdown License: CC BY 4.0 arXiv:2606.22826v1 [cs.AI] 22 Jun 2026 MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration Devleena Das Rajeev Patwari Vikram Kumar Bukka Nithin Kumar Guggilla Elliott Delaye Ashish Sirasa | Not Disclosed | Not Disclosed | Not Disclosed | Appendix E GPU Evaluation Speedup Breakdown Table 8 reports per-model GPU speedup ratios (full ÷ \div subset wall-clock time at batch size 1) for all 7 BF16 calibration models. Evaluation Speedup ( × \times ) Model IFEVAL MMLU GSM8K Llama-3.1-8B (base) 4.1 × \times 8.1 × \times 3.2 × \times Llama-3.1-8B-Inst 2.7 × \times 8.2 × \times 3.2 × \times Phi-4-mini-Inst 2.6 × \times 6.7 × \times 3.2 × \times Mistral-7B-Inst 2.1 × \times 10.5 × \times 3.3 × \times Qwen2.5-3B-Inst 2.2 × \times 5.8 × \times 3.3 × \times Qwen3-8B 5.8 × \times 7.8 × \times 3.3 × \times Qwen3.5-35B-A3B 9.2 × \times 8.9 × \times 3.3 × \times Me | Not Disclosed | Existing subset selection methods reduce this cost but depend on large calibration pools or learned prediction layers. | Evaluating LLMs across many model variants -- quantized, fine-tuned, or deployment-specific -- requires running large benchmarks repeatedly, a process that can take tens of hours per model on edge hardware such as NPUs. |
| SF-2026-ARXIV-2606-22827 | What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security — In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. | Not Disclosed | Not Disclosed | • We evaluate MEM-SBOM across 51 real-world Python applications, achieving higher accuracy and vulnerability precision than existing SBOM tools. P V P_{V} ( Precision ) measures the proportion of tool-reported vulnerabilities that are present at runtime. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. |
| SF-2026-ARXIV-2606-22840 | RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving — We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. | Claude Code, DeepSeek, DeepSeek-V4-Pro | Not Disclosed | Output format is flexible; minor imprecisions are generally tolerable. retrieval − - $ 0.012 query-optimize Database +$0.009 write-compressor Systems +$0.014 ENHANCED tasks cluster around two failure modes: (1) domain knowledge gaps where DeepSeek-V4-Pro lacks specialized training data (CV, IR, security); (2) algorithmic precision requirements where approximate drafts are systematically rejected. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | On a real-world agentic coding workload (Claude Code), RLM-Cascade achieves a draft-use rate of 88.8% across 125 production requests, reducing API cost by 45.8% relative to a direct Opus baseline. | We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. |
| SF-2026-ARXIV-2606-22844 | RaMem: Contextual Reinstatement for Long-term Agentic Memory — Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones. | Not Disclosed | These include the model path, served model name, maximum model length, GPU memory utilization, embedding model path, embedding batch size, number of memory build workers, and number of evaluation workers. | Not Disclosed | Not Disclosed | Not Disclosed | These include the model path, served model name, maximum model length, GPU memory utilization, embedding model path, embedding batch size, number of memory build workers, and number of evaluation workers. | Not Disclosed | Not Disclosed | Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones. |
| SF-2026-ARXIV-2606-22864 | When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents — Hidden-state probing -- a linear classifier on a frozen vision-language model's internal activations -- has emerged as an attractive evaluation tool for flagging indirect prompt injection (IPI) in multimodal computer-use agents before the agent emits a corrupted action. | Qwen2.5-VL-7B | Single-GPU on an NVIDIA RTX PRO 6000 Blackwell Workstation Edition ( 96 96 GB GDDR7 ECC). | Mahalanobis OOD baseline: empirical mean and Ledoit-Wolf-shrinkage covariance ( Ledoit and Wolf, 2004 ) fit on clean train features only; score = = squared Mahalanobis distance under shrinkage precision matrix. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Hidden-state probing -- a linear classifier on a frozen vision-language model's internal activations -- has emerged as an attractive evaluation tool for flagging indirect prompt injection (IPI) in multimodal computer-use agents before the agent emits a corrupted action. |
| SF-2026-ARXIV-2606-22873 | SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning — We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. | Not Disclosed | Batch inference with frameworks such as vLLM can exploit GPU parallelism across independent sequences, but still redundantly encodes the shared image and prompt tokens for every rule block. For slow-mode reasoning where outputs are longer, RI-Mask can still be applied but with reduced parallelism to fit within GPU memory constraints. | • We build SingGuard-Bench, a comprehensive MLLM guardrail benchmark covering harmful recall, benign-sensitive precision, attack robustness, modality composition, keyword coverage, reasoning depth, multilingual safety, and dynamic rules. This design supports a unified evaluation of harmful-content recall, precision on benign-sensitive cases, cross-modal intent reasoning, and policy-following behavior. | In this regime, the content prefix (image tokens + system prompt) dominates the total sequence length, rule descriptions are relatively short, and each branch only needs to emit a compact hit / not-hit output. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. |
| SF-2026-ARXIV-2606-22874 | SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers — Quantizing the selector's K-cache to INT4 or FP4 microscale shrinks it 3.5x at no accuracy cost. | Qwen3, Qwen3.5 | Latency is measured on a single NVIDIA B200. | Attn is essentially unchanged across precisions because quantization affects only the selector’s K-cache, not the backbone attention. Analysis and ablations In this section we analyse the trained selector: what it has learned, what the KL objective shapes it into, and how it tolerates lower-precision storage. | E Per-layer K K across datasets and budgets F Selector distribution heatmaps G Selector quantization H Use Of AI Assistants License: CC BY 4.0 arXiv:2606.22874v1 [cs.LG] 22 Jun 2026 SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers Huzama Ahmad * Se-Young Yun Affiliation: KAIST Abstract Long contexts have become standard in pretrained LLMs, yet they remain expensive to run: prefill compute grows quadratically with sequence length, and every decode step re-reads a key-value cache that grows linearly with it. At prefill, its compute grows quadratically with sequence length; at dec | Not Disclosed | We score all L − 1 L-1 next-token predictions in each 16K block and forward enough blocks to score at least 65,536 65{,}536 tokens ( ≈ 82 \approx 82 K scored tokens per cell at batch size 1). | Not Disclosed | Quantizing the selector's K-cache to INT4 or FP4 microscale shrinks it 3.5x at no accuracy cost. | Quantizing the selector's K-cache to INT4 or FP4 microscale shrinks it 3.5x at no accuracy cost. |
| SF-2026-ARXIV-2606-22875 | FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs — Extensive experiments demonstrate that FedOT achieves superior performance in both ownership verification and traceability. | Not Disclosed | With 4 RTX 4090, LVT training takes ∼ \sim 24 h; training an FL client requires ∼ \sim 7.5 h/GPU (15 epochs); training a watermarked VAE takes ∼ \sim 5 min/GPU. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Extensive experiments demonstrate that FedOT achieves superior performance in both ownership verification and traceability. |
| SF-2026-ARXIV-2606-22877 | DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings — Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. | Not Disclosed | Not Disclosed | Detail means supporting precision beyond the core, such as exact wording, exact time, exact encoding, qualifiers, constraints, tier/version, branch/address, examples, or scope. Use detail_quality only for detail completeness and precision; do not use it to override core_correct . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. |
| SF-2026-ARXIV-2606-22878 | Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning — To address this challenge, we propose a priority-aware learning-unlearning correction framework based on orthogonal LoRA that can enhance the knowledge evaluation through topology adjustment. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | However, the dynamic nature of practical decentralized edge networks, where devices may dynamically join or leave the collaborative training process, requires the system to continuously adapt to new data while selectively removing prior contributions. | Not Disclosed | To address this challenge, we propose a priority-aware learning-unlearning correction framework based on orthogonal LoRA that can enhance the knowledge evaluation through topology adjustment. |
| SF-2026-ARXIV-2606-22883 | CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents — Remarkably, fine-tuning Qwen3-32B on CLI-Universe-6K achieves 33.4% on Terminal-Bench 2.0. | Qwen3-32B | Hyperparameter Value Optimizer AdamW ( β 2 = 0.95 \beta_{2}=0.95 ) Peak learning rate 1 × 10 − 5 1\times 10^{-5} LR scheduler cosine_with_min_lr (min 1 × 10 − 6 1\times 10^{-6} ) Warmup ratio 0.03 Weight decay 0.01 Max gradient norm 1.0 Epochs 5 Per-device batch size 1 Gradient accumulation steps 4 Context length 64K Precision bf16 Sequence parallelism degree 2 GPUs 32 × \times NVIDIA H200 Global batch size 64 Appendix C Failure Mode Examples Each failure mode is illustrated with one CLI-Universe-32B trajectory on Terminal-Bench 2, shown as a turn-level timeline. | Hyperparameter Value Optimizer AdamW ( β 2 = 0.95 \beta_{2}=0.95 ) Peak learning rate 1 × 10 − 5 1\times 10^{-5} LR scheduler cosine_with_min_lr (min 1 × 10 − 6 1\times 10^{-6} ) Warmup ratio 0.03 Weight decay 0.01 Max gradient norm 1.0 Epochs 5 Per-device batch size 1 Gradient accumulation steps 4 Context length 64K Precision bf16 Sequence parallelism degree 2 GPUs 32 × \times NVIDIA H200 Global batch size 64 Appendix C Failure Mode Examples Each failure mode is illustrated with one CLI-Universe-32B trajectory on Terminal-Bench 2, shown as a turn-level timeline. | Not Disclosed | Not Disclosed | Hyperparameter Value Optimizer AdamW ( β 2 = 0.95 \beta_{2}=0.95 ) Peak learning rate 1 × 10 − 5 1\times 10^{-5} LR scheduler cosine_with_min_lr (min 1 × 10 − 6 1\times 10^{-6} ) Warmup ratio 0.03 Weight decay 0.01 Max gradient norm 1.0 Epochs 5 Per-device batch size 1 Gradient accumulation steps 4 Context length 64K Precision bf16 Sequence parallelism degree 2 GPUs 32 × \times NVIDIA H200 Global batch size 64 Appendix C Failure Mode Examples Each failure mode is illustrated with one CLI-Universe-32B trajectory on Terminal-Bench 2, shown as a turn-level timeline. | Not Disclosed | Not Disclosed | Remarkably, fine-tuning Qwen3-32B on CLI-Universe-6K achieves 33.4% on Terminal-Bench 2.0. |
| SF-2026-ARXIV-2606-22902 | Agent-as-a-Router: Agentic Model Routing for Coding Tasks — We instantiate this framework as ACRouter, composed of an Orchestrator, a Verifier, a Memory module, and introduce CodeRouterBench, an evaluation environment comprising ~10K task instances with verified scores from 8 frontier LLMs, enabling regret-based router comparison on streaming tasks. | Not Disclosed | Throughput is measured on a single NVIDIA H100 80GB HBM3, the deployment target used by every self-hosted router experiment in this paper. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Consequently, routing each task to the most suitable model becomes critical for both performance and cost. | We instantiate this framework as ACRouter, composed of an Orchestrator, a Verifier, a Memory module, and introduce CodeRouterBench, an evaluation environment comprising ~10K task instances with verified scores from 8 frontier LLMs, enabling regret-based router comparison on streaming tasks. |
| SF-2026-ARXIV-2606-22906 | From Fragments to Paths: Task-Level Context Recovery for Large Industrial Codebases — Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. | Not Disclosed | Not Disclosed | We also report Micro Recall (MR) and Micro Precision (MP) as auxiliary file-level metrics. DeepDiscovery is also competitive in MR and MP, indicating that its higher FRR does not come with a disproportionate precision penalty. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. |
| SF-2026-ARXIV-2606-22916 | Intent-Governed Tool Authorization for AI Agents — We evaluate a reusable IGAC path over an OpenPort governance substrate using endpoint tests, 176 runtime-backed synthetic tasks, real-model classifier and planner pilots, 306 end-to-end model-task runtime trials, and a 36-trial benchmark-shaped external subset. | Not Disclosed | X-J Expanded Real LLM Pilot After the runtime microbenchmark, we expanded the real-model pilot into a larger synthetic study over NVIDIA NIM-compatible chat completions. | This convergence strengthens the paper’s main interpretation: IGAC plus OpenPort effect controls already contain completed side effects in the runtime path, but certificate precision and planner-call quality remain the main blockers to fully eliminating accepted authority. The harder problem is certificate precision: the runtime still needs stronger amount/resource/effect normalization to collapse these governed draft paths into earlier denials or clarifications. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A trace-backed normalizer counterfactual removes this residual authority at substantial utility cost. | We evaluate a reusable IGAC path over an OpenPort governance substrate using endpoint tests, 176 runtime-backed synthetic tasks, real-model classifier and planner pilots, 306 end-to-end model-task runtime trials, and a 36-trial benchmark-shaped external subset. |
| SF-2026-ARXIV-2606-22918 | Each Judge Its Own Yardstick: Discovering Per-VLM Taxonomies for Physical Video Evaluation — A single global evaluation schema therefore gives every VLM the same axes of competence, regardless of what each can actually perceive. | Qwen | The two Qwen models are run locally on NVIDIA A100 GPUs (approximately 100 GPU-hours in total); all other judges, together with the LLM editor and clustering model, are accessed through the OpenRouter API. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A single global evaluation schema therefore gives every VLM the same axes of competence, regardless of what each can actually perceive. |
| SF-2026-ARXIV-2606-22925 | EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction — Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. | Not Disclosed | These runs were carried out on internal servers equipped with multiple NVIDIA GPUs, including A800, RTX A6000, RTX 4090, and RTX 3090 devices. | Future work includes extending the rulebook and corpus to broader EEG task families and datasets, and further characterizing LLM-assisted benchmark drafting and review support, including description precision, evidence grounding, kernel alignment, and the human effort required for review. | Not Disclosed | Not Disclosed | BENDR used raw EEG inputs with batch size 64 64 , whereas CBraMod, CodeBrain, and LaBraM used patched inputs with patch size 200 200 and batch size 128 128 . | Not Disclosed | Not Disclosed | Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. |
| SF-2026-ARXIV-2606-22932 | FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training — Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs. | GPT-2, Qwen3 | License: CC BY 4.0 arXiv:2606.22932v1 [cs.LG] 22 Jun 2026 FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training Dikshant Kukreja Affiliation: Puch AI Singapore Institute of Technology Nanyang Technological University NVIDIA IIIT-Delhi Kritarth Prasad Avinash Anand Zhengkui Wang Erik Cambria Timothy Liu Aik Beng Ng Simon See Bapi Chatterjee Email: dikshant@puch.ai Dikshant˜Kukreja performed this work as an undergraduate at IIIT-Delhi. Affiliation: Puch AI Singapore Institute of Technology Nanyang Technological University NVIDIA IIIT-Delhi Abstract Reverse-mode differentiation computes eve | 2.3 Precision and low-precision fidelity The gradient is never truncated. Choosing the precision point. | H200 Qwen3 sweep across sequence length. B200 Qwen3 sweep across sequence length. | Not Disclosed | 3.2 Convergence parity 3.3 From-scratch pretraining parity on GPT-2 124M 3.4 Per-step memory profile 3.5 Operating regime: batch size sensitivity 3.6 Composability with FP8 and activation checkpointing 3.7 Multi-model scaling 4 Distributed training When fusion is exact. Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5 × 1.5\times faster; integrated into tensor-parallel Megatron-LM it fits 8 8 B training at four times the micro-batch a standard optimizer allows on the same GPUs. | The fusion changes only when the update happens, not what it computes: in full precision the fused step is provably exact -- the identical optimizer update, for every element-wise rule -- and that exactness survives tensor- and sequence-parallel sharding; in the bf16 and 8-bit regimes used in practice it is faithful rather than bit-identical, its deviation bounded and, for the weight store, rendered unbiased by stochastic rounding. | Not Disclosed | Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs. |
| SF-2026-ARXIV-2606-22936 | When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents — The result is a diagnostic for a hidden process failure, with clear limits rather than a general accuracy lever. | Llama-3.1-70B, Qwen-2.5-72B | The model runs on 8 × \times 80GB GPUs with pipeline parallelism (10 layers per GPU). | At k = 3 k{=}3 , precision = 0.81 =0.81 at recall = 0.90 =0.90 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The result is a diagnostic for a hidden process failure, with clear limits rather than a general accuracy lever. |
| SF-2026-ARXIV-2606-22942 | Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails — Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. | Not Disclosed | NVIDIA (2024) NVIDIA Data-efficient knowledge distillation for supervised fine-tuning with NVIDIA nemo aligner . All experiments are conducted on NVIDIA H100 GPUs. | Not Disclosed | The maximum sequence length is set to 4096 tokens. | Not Disclosed | We use the AdamW optimizer with a learning rate of 5 × 10 − 6 5\times 10^{-6} and a batch size of 128. | Not Disclosed | Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. | Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. |
| SF-2026-ARXIV-2606-22948 | ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents — To evaluate robustness under realistic desktop interruptions, we also introduce OSWorld-Noisy, a dynamic benchmark for recoverable desktop interruptions that preserves the original tasks while testing whether agents can refocus, dismiss, wait, or recover under live perturbations. | Not Disclosed | On the 300-task OSWorld pool, ENVS reaches 30.3 pass@8 on original evaluations and 29.0 on OSWorld-Noisy , outperforming matched ARPO-style online RL while reducing compute from 184–192 to 138–153 GPU-hours; even with only 30% of its search data, ENVS reaches 27.0 pass@8, exceeding ARPO from the base model. We report GPU hours because live VM execution dominates training cost; ARPO collects fresh on-policy rollouts during training, while ENVS collects verified trajectories once and reuses them for SFT variants. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To evaluate robustness under realistic desktop interruptions, we also introduce OSWorld-Noisy, a dynamic benchmark for recoverable desktop interruptions that preserves the original tasks while testing whether agents can refocus, dismiss, wait, or recover under live perturbations. |
| SF-2026-ARXIV-2606-22953 | Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents — Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. | DeepSeek-AI, DeepSeek-R1-Distill-Llama-70B, Llama, Llama-3.1-70B, Llama-3.1-70B-Instruct, Llama-3.1-8B-Instruct, Llama-trained | Models run on 8 × 8\times H200 GPUs with pipeline parallelism. Llama-3.1-70B-Instruct ( Grattafiori et al., 2024 ) , Llama-3.1-8B-Instruct, and DeepSeek-R1-Distill-Llama-70B ( DeepSeek-AI, 2025 ) served on 8 × 8\times H200 GPUs with pipeline parallelism. | Metric ALFWorld HotpotQA L 32 L_{32} HotpotQA L 40 L_{40} R 2 R^{2} 0.875 ± 0.016 0.875\pm 0.016 n/a n/a AUROC 0.999 1.000 1.000 F1 ( τ \tau =0.15) 0.898 0.678 0.968 Precision 0.985 0.513 0.938 Recall 0.825 1.000 1.000 On ALFWorld, the probe predicts plan-signal magnitude at R 2 = 0.875 ± 0.016 R^{2}=0.875\pm 0.016 , well below the R 2 = 1 R^{2}=1 a trivially-leaked feature would produce. The induced binary decision at τ = 0.15 \tau=0.15 reaches AUROC 0.999 0.999 with balanced precision ( 0.985 0.985 ) and recall ( 0.825 0.825 ). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. | Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. |
| SF-2026-ARXIV-2606-22966 | Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models — We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. |
| SF-2026-ARXIV-2606-22968 | MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference — It further incorporates Latency-Balanced Chunk Partitioning (LBCP) to balance chunk execution cost under both attention-cost growth and KV reallocation overhead, improving pipeline efficiency. | Not Disclosed | 5 Evaluation 5.1 Experimental Setup Hardware Configuration : We configure each die in the WSC to be equivalent to an NVIDIA Blackwell GPU [ 17 ] capable of 4.5 PFLOPS, equipped with 180GB HBM featuring 7.7 TB/s access bandwidth. [17] NVIDIA (2026) NVIDIA DGX Vera Rubin NVL72 . | Not Disclosed | Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Background 2.1 Prefill-Only LLM Inference 2.2 Chunked Pipeline 2.3 Wafer-Scale Chips 3 Motivation 3.1 Memory Imbalance Limits Feasible Sequence Length 3.2 Latency Imbalance Limits Compute Utilization 4 MOCAP Framework 4.1 Memory-Balanced KV Reallocation 4.2 Latency-Balanced Chunk Partitioning 5 Evaluation 5.1 Experimental Setup 5.2 Performance on Wafer-scale Chips 6 Related Work 7 Conclusion References License: arXiv.org perpetual non-exclusive license arXiv:2606.22968v1 [cs.AR] 22 Jun 2026 MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Ch | Not Disclosed | Algorithm 1 Latency-balanced Chunk Partitioning Scheme Input: #Stage N N , #Chunk M M , sequence length S S Output: Optimal batch size B ∗ B^{*} , chunk slice scheme s ​ s ∗ ss^{*} , E2E latency T ∗ T^{*} 1 for m ← M m\leftarrow M to 1 1 do 2 for s ← S − 1 s\leftarrow S-1 to 0 0 do 3 for k ← 1 k\leftarrow 1 to S − s − ( M − m ) S-s-(M-m) do 4 t ← EvaluateChunk ​ ( k , s ) t\leftarrow\textsc{EvaluateChunk}(k,s) ; 5 t m ​ a ​ x ′ ← max ⁡ ( t max ​ [ m + 1 ] ​ [ s + k ] , t ) t_{max}^{\prime}\leftarrow\max(t_{\max}[m+1][s+k],t) , t ∑ ′ ← t ∑ ​ [ m + 1 ] ​ [ s + k ] + t t_{\sum}^{\prime}\leftarrow t_{\sum}[m+1][s+k]+ | A natural way to accelerate prefill is to partition a long input sequence into multiple chunks and execute them in a finer-grained pipeline across devices. | Large language models (LLMs) are increasingly used in prefill-only workloads, where end-to-end latency is dominated by the prefill phase. | It further incorporates Latency-Balanced Chunk Partitioning (LBCP) to balance chunk execution cost under both attention-cost growth and KV reallocation overhead, improving pipeline efficiency. |
| SF-2026-ARXIV-2606-22977 | StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs — While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. | GPT-5.1, Llama-3.1-8B-Instruct | Meta-Llama-3.1-8B-Instruct was deployed locally on 8 × \times NVIDIA RTX 4090 GPUs with vLLM ( Kwon et al., 2023 ) and the max-model-len parameter was set to 128,000 tokens. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. |
| SF-2026-ARXIV-2606-22983 | LiveServe: Interaction-Aware Serving for Real-Time Omni-Modal LLMs — On vLLM-Omni, LiveServe improves realtime serving across two Omni-LMs and mixed workloads. | Not Disclosed | Experiments were conducted on a single H200 server with eight NVIDIA H200 GPUs. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing Omni-LM serving systems still rely on throughput-oriented LLM scheduling and LRU KV offloading. | On vLLM-Omni, LiveServe improves realtime serving across two Omni-LMs and mixed workloads. |
| SF-2026-ARXIV-2606-23001 | EnerInfer: Energy-Aware On-Device LLM Inference — We show instead that on-device LLM inference often has exploitable configuration slack: modestly lowering NPU and memory frequencies preserves quality of experience (QoE) while substantially improving energy efficiency and reducing heat. | Not Disclosed | (iv) Cloud-serving techniques optimize control knobs such as batch size, GPU frequency, and model partitioning and multiplexing, but do not address coordinated NPU and memory frequency scaling, which is critical for mobile devices with unified-memory architectures ( Codrescu et al., 2014 ) . While many open-source LLM inference engines leverage CPUs and GPUs on phones, NPUs offer significantly better energy efficiency than GPUs and are more capable of handling highly parallel computations than CPUs ( Xu et al., 2025 ) . | Not Disclosed | Iyer Efficient interactive llm serving with proxy model-based sequence length prediction . | Not Disclosed | (iv) Cloud-serving techniques optimize control knobs such as batch size, GPU frequency, and model partitioning and multiplexing, but do not address coordinated NPU and memory frequency scaling, which is critical for mobile devices with unified-memory architectures ( Codrescu et al., 2014 ) . | On-device LLM inference is increasingly attractive for privacy-preserving, reliable, and cost-effective deployment, yet its energy and thermal costs remain a critical bottleneck. | On-device LLM inference is increasingly attractive for privacy-preserving, reliable, and cost-effective deployment, yet its energy and thermal costs remain a critical bottleneck. | We show instead that on-device LLM inference often has exploitable configuration slack: modestly lowering NPU and memory frequencies preserves quality of experience (QoE) while substantially improving energy efficiency and reducing heat. |
| SF-2026-ARXIV-2606-23003 | VCT: A Verifiable Transcript System for LLM Conversations — Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. | Not Disclosed | Not Disclosed | Timing measurements are based on a monotonic clock with microsecond precision. | Not Disclosed | Not Disclosed | Not Disclosed | However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. | Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. | Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. |
| SF-2026-ARXIV-2606-23017 | Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems — First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. | Not Disclosed | The hardware environment uses NVIDIA L20 GPU as the training acceleration device, and the underlying blockchain platform is FISCO BCOS version 3.11. | Massive sensor data from vehicles and RSUs enables high-precision model training, but privacy regulations and transmission costs make centralized training infeasible. To train high-precision models while complying with privacy regulations (e.g., GDPR), Federated Learning (FL) has become the mainstream paradigm for VRC systems Lim et al. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. | First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. |
| SF-2026-ARXIV-2606-23026 | A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees — We learn a conditional response model, optimize a leader policy against that model, and repair the resulting policy using real-API calibration and projection onto an empirically selected action set. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We formulate resource governance as a contextual Stackelberg game: a controller commits to a quality target and a cost incentive, while an executor responds with resource actions over context, prompting, and tool usage. | We learn a conditional response model, optimize a leader policy against that model, and repair the resulting policy using real-API calibration and projection onto an empirically selected action set. |
| SF-2026-ARXIV-2606-23030 | Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models — We argue that LLMs exhibit a human-memory-like behavior: an LLM may not memorize a specific sample verbatim, yet it can accumulate and reveal knowledge about a real-world entity from scattered mentions. | Not Disclosed | V-A Experimental Setup The experiments are conducted on a desktop computer with Ubuntu 22.04LTS operating system, 3.0 GHz Intel® Xeon® Gold 6248R CPU, 251GB memory, and two NVIDIA RTX A6000 GPUs. | Auditing of proprietary commercial models is typically a post-hoc, forensic process where precision and low FPR outweigh the cost of API queries. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We argue that LLMs exhibit a human-memory-like behavior: an LLM may not memorize a specific sample verbatim, yet it can accumulate and reveal knowledge about a real-world entity from scattered mentions. |
| SF-2026-ARXIV-2606-23038 | EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning — However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. | Not Disclosed | Training is conducted on a single node with 8 NVIDIA A100-80GB GPUs, coordinated via Ray 2.43. | Not Disclosed | Not Disclosed | Not Disclosed | E.1 Per-Step Complexity Let B B denote the batch size and M M the number of rollout samples per prompt. | Not Disclosed | Not Disclosed | However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. |
| SF-2026-ARXIV-2606-23049 | PhoneBuddy: Training Open Models for Agentic Phone Use — Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We perform full-parameter fine-tuning for 1,115 optimizer steps with batch size 512. Because multiple short examples can be packed into one training sequence, the product of batch size and optimizer steps should not be read as a direct count of raw action steps. | Phones are becoming an important execution surface for general-purpose agents, but training open models for reliable phone use remains difficult because the environment that matters at deployment, real devices running real apps, is slow, stateful, side-effectful, and hard to reset or verify, while scalable mock environments only approximate real behavior. | Not Disclosed | Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. |
| SF-2026-ARXIV-2606-23075 | Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies — We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). |
| SF-2026-ARXIV-2606-23112 | Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning — For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. | Qwen, Qwen3.5-9B | We evaluate on all 375 tau2-bench tasks using Qwen/Qwen3.5-9B served by vLLM on HPC2 A800 GPUs. Direct Preference Optimization (DPO) turns pairwise preferences into a supervised objective without an explicit reward model ( Rafailov et al., 2023 ) , and QLoRA makes such adaptation feasible under limited GPU memory ( Dettmers et al., 2023 ) . | Cross-validation shows reliable coverage for retail (recall 90%, precision 64%) but insufficient coverage for banking (recall 12%, precision 90%). | Training uses a per-device batch size of 1, gradient accumulation of 8, a maximum sequence length of 4096, and a 0.1 warm-up ratio. | Not Disclosed | Training uses a per-device batch size of 1, gradient accumulation of 8, a maximum sequence length of 4096, and a 0.1 warm-up ratio. | Not Disclosed | Not Disclosed | For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. |
| SF-2026-ARXIV-2606-23127 | Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation — Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. |
| SF-2026-ARXIV-2606-23130 | Understanding the (In)Security of Vibe-Coded Applications — Our study reveals several key findings: (1) vibe-coded applications exhibit recurring vulnerability patterns that differ from those commonly observed in conventional software development workflows, including placeholder logic, unfiltered input, and secret exposure; (2) these vulnerabilities arise from systematic limitations of AI agents throughout the vibe-coding lifecycle, such as memory loss, locally optimized objectives and insufficient security knowledge; and (3) while advances in LLM capabilities and improved prompting strategies can reduce the inci | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our study reveals several key findings: (1) vibe-coded applications exhibit recurring vulnerability patterns that differ from those commonly observed in conventional software development workflows, including placeholder logic, unfiltered input, and secret exposure; (2) these vulnerabilities arise from systematic limitations of AI agents throughout the vibe-coding lifecycle, such as memory loss, locally optimized objectives and insufficient security knowledge; and (3) while advances in LLM capabilities and improved prompting strategies can reduce the inci |
| SF-2026-ARXIV-2606-23181 | DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models — Across the main comparisons, DART preserves or improves always-thinking accuracy in most settings while reducing thinking-token use. | DeepSeek-AI, Qwen | 1 Introduction Recent reasoning LLMs increasingly expose hybrid inference interfaces across open-weight models ( Qwen Team, 2025 ; DeepSeek-AI, 2025 ; DeepSeek-AI et al., 2025 ; Google DeepMind, 2026 ; Yu et al., 2025 ; NVIDIA, 2026 ) and hosted services ( OpenAI, 2026 ; Anthropic, 2026 ) . NVIDIA (2026) NVIDIA Nemotron 3 nano omni: efficient and open multimodal intelligence . | We use strict unanimity at K = 2 K{=}2 rather than majority voting because agreement between two independent stochastic samples concentrates probability ≥ p 2 \geq p^{2} on the model’s dominant answer, while the analysis below shows that this low-cost rule keeps accepted-answer precision high without thresholds and avoids the larger K K cost of self-consistency. We report accuracy, accept precision, and the point-biserial correlation r p ​ b r_{pb} between draft unanimity and AT correctness. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across the main comparisons, DART preserves or improves always-thinking accuracy in most settings while reducing thinking-token use. |
| SF-2026-ARXIV-2606-23189 | Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? — Hence, we introduce AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Hence, we introduce AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios. |
| SF-2026-ARXIV-2606-23195 | Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory — Recent work shows that agent memories degrade during continuous consolidation. | Claude, DeepSeek | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Recent work shows that agent memories degrade during continuous consolidation. |
| SF-2026-ARXIV-2606-23217 | MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations — Our experiments show that models leak substantially more in multi-party settings than one-to-one evaluations suggest. | Not Disclosed | (2020) on a single NVIDIA RTX A6000, with inference times ranging from 60s/iteration to 5s/iteration, depending on the type of model, scale, and experimental configuration. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our experiments show that models leak substantially more in multi-party settings than one-to-one evaluations suggest. |
| SF-2026-ARXIV-2606-23276 | Exposing the Illusion of Erasure in Knowledge Editing for LLMs — In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. | Not Disclosed | NVIDIA . C.5 Compute Information All stages of our experimental pipeline, including the memory-intensive knowledge editing interventions, the extraction benchmarks, and the highly parallelized GCG discrete optimization loops, were executed using a compute node equipped with two NVIDIA A100 (40GB) GPUs. | Not Disclosed | Not Disclosed | Not Disclosed | Algorithm 1 GCG Optimization for Knowledge Elicitation 0: Edited model f θ ∗ f_{\theta^{*}} , Dataset of edits 𝒟 e ​ d ​ i ​ t \mathcal{D}_{edit} , Objective function 𝒥 ∈ { 𝒥 g ​ u ​ i ​ d ​ e ​ d , 𝒥 b ​ l ​ i ​ n ​ d } \mathcal{J}\in\{\mathcal{J}_{guided},\mathcal{J}_{blind}\} , Suffix length L L , Iterations N N , Batch size B B , Top candidates K K . Parameter Value Optimization Setup Optimization Steps ( N N ) 1500 Batch Size ( B B ) 512 Top- K K Candidates 256 Suffix Length ( L L ) 30 tokens Inference Setup Max New Tokens 50 Temperature 1.0 Top- p p 1.0 C.4 Editing Hyperparameters To ensure a rigorous and s | Not Disclosed | Not Disclosed | In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. |
| SF-2026-ARXIV-2606-23277 | GIF: Locally Sound Geometric Information Flow Control for LLMs — Recent Information Flow Control (IFC)-based defenses show promise but lack a principled semantic foundation for reasoning about information flow through the model itself. | GPT-5.5 | Machine details Experiments ran on 3 NVIDIA RTX PRO 6000 GPUs with 48 vCPUs and 565 GB RAM, using CUDA 13.2, PyTorch 2.12, vLLM 0.22.0, and HF transformers 5.9.0. | For each trajectory, Policy Source Precision at k ( PSP@ ​ k \textsc{PSP@}k ) measures the fraction of top- k k source tokens that overlap benchmark-labeled prompt-injection or private-information tokens. Per model block and metric column the best value is green and the worst red (coloured from full-precision values). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Combined with lightweight LLM-based declassifiers, it matches or exceeds the F1 of direct LLM-as-judge baselines such as GPT-5.5 xhigh reasoning while using up to 81x lower token cost. | Recent Information Flow Control (IFC)-based defenses show promise but lack a principled semantic foundation for reasoning about information flow through the model itself. |
| SF-2026-ARXIV-2606-23283 | Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs — Current benchmarks remain inadequate for evaluating this problem. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We set the maximum number of root memory units to 10 and the root memory construction batch size to 20. Since these memory systems extract substantially more memories than the original human-annotated entries, we increase the root memory construction batch size to 60. | Not Disclosed | Not Disclosed | Current benchmarks remain inadequate for evaluating this problem. |
| SF-2026-ARXIV-2606-23321 | Tmax: A simple recipe for terminal agents — While simple, our recipe achieves 27\% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger models from prior work. | Qwen | Not Disclosed | We additionally ensure that the language model head of models is computed and kept in FP32 precision to minimize training-inference mismatch, following MiniMax et al. D.2 Full SFT Training Details Category Hyperparameter Value Model Precision bf16 Model Attention implementation flash attention 3 Model Gradient checkpointing true Data Max sequence length 65536 for Qwen 3.5, 32768 for Qwen 3 Optimization Epochs 2 Optimization Per-device batch size 1 Optimization Gradient accumulation steps 4 Optimization Global batch size 128 Optimization Learning rate 2 × 10 − 5 2\times 10^{-5} Optimization LR scheduler linear Opt | Training takes 2–3 days depending on sequence length and infrastructure stability. We use a group size of 32 and 8 prompts per batch, with a maximum sequence length of 65536 tokens and 64 maximum tool calls. | Not Disclosed | D.2 Full SFT Training Details Category Hyperparameter Value Model Precision bf16 Model Attention implementation flash attention 3 Model Gradient checkpointing true Data Max sequence length 65536 for Qwen 3.5, 32768 for Qwen 3 Optimization Epochs 2 Optimization Per-device batch size 1 Optimization Gradient accumulation steps 4 Optimization Global batch size 128 Optimization Learning rate 2 × 10 − 5 2\times 10^{-5} Optimization LR scheduler linear Optimization Warmup ratio 0.03 Optimization Weight decay 0.0 Optimization Optimizer AdamW Table 14: Hyperparameters for SFT training. | Not Disclosed | Not Disclosed | While simple, our recipe achieves 27\% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger models from prior work. |
| SF-2026-ARXIV-2606-23370 | FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation — The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman. | Llama3.1 | Compatibility with Other XPUs : Currently, FlexServe uses the CPU and NPU to execute inference tasks, but its design also works for GPUs and NPUs from different vendors. Enabling Accelerators in TEE : Existing works also try to enable accelerators, e.g., GPUs and NPUs, inside the TEE ( Fan et al., 2025 ; Volos et al., 2018 ; Jang et al., 2019 ; Deng et al., 2022 ; Zhu et al., 2020 ; Wu et al., 2023 ; Park and Lin, 2023 ; Mai et al., 2023 ; Ivanov et al., 2023 ; Hunt et al., 2020 ) . | Prefill Performance: We evaluate models ranging from 1.7B to 8B, all quantized to INT8 precision. | Conversely, if the secure-world OS releases the secure memory after each inference, the TTFT increases by 2.54 × 2.54\times for Llama3.1 8B with a sequence length of 128. | Not Disclosed | Not Disclosed | Device-side Large Language Models (LLMs) have grown explosively, offering stronger privacy and higher availability than their cloud-side counterparts. | Not Disclosed | The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman. |
| SF-2026-ARXIV-2606-23403 | Litmus: Zero-Label, Code-Driven Metric Specification for Evaluating AI Systems — As agentic LLM systems move from prototypes to deployment across increasingly diverse domains, evaluating them has become both more important and more difficult. | Not Disclosed | Not Disclosed | “Does RAG Context Precision measure the component it is attached to?” reject : the component is a PDF reader/parser that extracts text; it performs no query-based retrieval, so a retrieval-quality metric cannot apply. The following are representative questions for the scientific-QA components (the direction-of-goodness and scoping decisions they resolve are noted in italics): • Evidence Retrieval & Summarization: “Is this stage tuned for broad recall or precise grounding when selecting evidence passages?” Determines whether the retrieval judge emphasizes recall-oriented or precision-oriented families and sets its | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | As agentic LLM systems move from prototypes to deployment across increasingly diverse domains, evaluating them has become both more important and more difficult. |
| SF-2026-ARXIV-2606-23404 | ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models — ReasoningLens addresses information necropsy by: (1) structuring traces into interactive hierarchies that separate high-level strategy from low-level execution; (2) leveraging an agentic auditor for automated error detection and tool-augmented verification; and (3) synthesizing systemic reasoning profiles to reveal model-specific blind spots. | Not Disclosed | Not Disclosed | Formal definitions are in For reasoning error diagnosis, we report per-type and micro-averaged Precision, Recall, and F1 scores. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | ReasoningLens addresses information necropsy by: (1) structuring traces into interactive hierarchies that separate high-level strategy from low-level execution; (2) leveraging an agentic auditor for automated error detection and tool-augmented verification; and (3) synthesizing systemic reasoning profiles to reveal model-specific blind spots. |
| SF-2026-ARXIV-2606-23416 | Detecting Malicious Agent Skills in the Wild using Attention — We release the resulting labeled dataset. | Not Disclosed | Not Disclosed | Deployed at marketplace scale and at negligible cost, Locate-and-Judge flags skills with high precision, the majority of which we manually confirmed as malicious, surfacing dozens of live malicious skills, including several disguised as benign functionality and many that SkillSpector and Cisco Skill Scanner fail to detect. First, in a controlled setting built on the Skill-Inject corpus [ 8 ] , we measure how reliably the locator surfaces injected spans and how the end-to-end detector trades precision, recall, and cost against per-span and full-skill baselines. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Compared to direct LLM-based scanning, this approach offers an order-of-magnitude cost reduction, dramatically increasing its scalability at a small cost to recall, and it dominates keyword and regex baselines at comparable expense. | We release the resulting labeled dataset. |
| SF-2026-ARXIV-2606-23449 | AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction — Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance. | Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance. |
| SF-2026-ARXIV-2606-23459 | TriggerBench: Investigating Prospective Memory for Large Language Models — While Large Language Models (LLMs) are increasingly deployed in long interactions, existing evaluations focus predominantly on retrospective memory (RM) via explicit queries. | Not Disclosed | Not Disclosed | The Precision-Recall Trade-off. C.2 Online Evaluation Ablation C.3 Per-Dimension AIME Accuracy and PM Behavior C.4 Evaluation Stability against Sampling Variance C.5 Impact of System Prompts: The Precision-Recall Trade-off Experimental Setup. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | While Large Language Models (LLMs) are increasingly deployed in long interactions, existing evaluations focus predominantly on retrospective memory (RM) via explicit queries. |
| SF-2026-ARXIV-2606-23521 | Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference — The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM. | Not Disclosed | This is different from CUDA Graphs ( Choquette, 2019 ; NVIDIA Corporation, 2024a ) . Checkpoint handlers are compiled via NVRTC ( NVIDIA Corporation, 2024c ) from region specifications, loaded through the CUDA Driver API ( NVIDIA Corporation, 2024b ) , written into an inactive slot, and made visible by flipping a version counter, enabling hot-swapping without service interruption. | Checkpoint (0.5 s) + AMD restore (0.6 s) + Tenstorrent migrate (1.1 s) = 2.2 s total downtime during a 30 s job, with results identical to non-migrated execution within floating-point precision. | Not Disclosed | Not Disclosed | Not Disclosed | This paper argues that fault tolerance for such workloads needs a GPU-resident execution context: checkpoint hooks must run at device synchronization points, observe binary kernels that frameworks and libraries actually execute, and recover without putting the host CPU on the critical path. | Not Disclosed | The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM. |
| SF-2026-ARXIV-2606-23525 | Self-Compacting Language Model Agents — Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. | Not Disclosed | The 30B-A3B model uses tensor-parallel size 2; all others run on a single H200 GPU. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our results show that SelfCompact matches or exceeds fixed-interval summarization at a fraction of the token cost, improving over a no-summarization baseline by up to 18.1 points on math and 5-9 points on agentic search at 30-70% lower per-question cost. | Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. |
| SF-2026-ARXIV-2606-23546 | The Energy Consumption of Transformer Fine-Tuning: A Roofline-Inspired Scaling Model — We derive a scaling law model that accurately predicts training energy across heterogeneous configurations. | Not Disclosed | We present a framework for modeling the energy consumption of Transformer training on multiple GPUs. • We introduce a speedup-based hardware-efficiency model for tensor and data parallelism, enabling energy estimation without direct multi-GPU energy measurements. | Complementary case studies further show that configuration choices such as batching, numerical precision, and interconnect topology can induce large differences in energy consumption for comparable training objectives Patterson et al. | Changing depth, width, sequence length, and batch size necessarily affects multiple quantities simultaneously; this is inherent to Transformer scaling. These proxies are lightweight, depend only on ( L , d , ff ) (L,d,\mathrm{ff}) and sequence length, and are intended as minimal sufficient statistics for comparative scaling analysis rather than exact kernel- or byte-level measurements. | Not Disclosed | Changing depth, width, sequence length, and batch size necessarily affects multiple quantities simultaneously; this is inherent to Transformer scaling. We use a proxy proportional to activation volume across layers, M proxy ​ ( B , S , d , L ) ≈ B ​ S ​ d ​ L , M_{\mathrm{proxy}}(B,S,d,L)\;\approx\;B\,S\,d\,L, (3) where B B is batch size. | Not Disclosed | Transformer-based models underpin modern natural language processing but incur rapidly growing computational and energy costs. | We derive a scaling law model that accurately predicts training energy across heterogeneous configurations. |
| SF-2026-ARXIV-2606-23581 | Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse — We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. | Not Disclosed | Not Disclosed | Dao FlashAttention-3: fast and accurate attention with asynchrony and low-precision . | Memory, not the nominal window, is the operative bound: even as context windows reach 1 1 M tokens, a locally served model holds only as much KV cache as device memory allows, so the sequence length used in practice is set by KV capacity, and the agent must continually slide, evict, and re-admit content. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. |
| SF-2026-ARXIV-2606-23583 | Evaluation Awareness Is Not One Capability: Evidence from Open Language Models — Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. |
| SF-2026-ARXIV-2606-23589 | KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies — We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). | Not Disclosed | Both π 0.5 \pi_{0.5} and our method are trained for 30K steps with a global batch size of 32 on 2 × \times A100 GPUs. Hyperparameter Value Base VLM Prismatic VLM Batch size 128 Total steps 40000 Future action window 50 Action space Joint-space We trained MemoryVLA for 40K steps with a global batch size of 128 on 8 × A ​ 100 8\times A100 GPUs. | Not Disclosed | The updated tokens X ^ t \hat{X}_{t} are passed to the language model in place of the original image tokens, with no change to the prefix sequence length or the language model architecture. | Not Disclosed | Hyperparameter Value Optimizer AdamW Peak learning rate 2.5 × 10 − 5 2.5\times 10^{-5} Minimum learning rate 2.5 × 10 − 6 2.5\times 10^{-6} Warmup steps 1000 Total steps 30000 Batch size 32 Action horizon 50 Action space Joint-space Table 4: Training hyperparameters for π 0.5 \pi_{0.5} with event-driven keyframe memory. Module Hyperparameter Value Training Optimizer AdamW Peak learning rate 2.5 × 10 − 5 2.5\times 10^{-5} Minimum learning rate 2.5 × 10 − 6 2.5\times 10^{-6} Warmup steps 1000 Total steps 30000 Batch size 32 Action horizon 50 Action space Joint-space Loss Weighting Keyframe weight λ \lambda 8.0 Wind | Not Disclosed | Not Disclosed | We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). |
| SF-2026-ARXIV-2606-23617 | RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models — We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. | Not Disclosed | Appendix A Compute Infrastructure All models were trained on an institutional high-performance computing cluster using NVIDIA H200 GPUs. Most evaluations were also run on the same cluster, with some additional local testing on an NVIDIA RTX 6000 Ada workstation. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. |
| SF-2026-ARXIV-2606-23642 | Improving Long-Context Retrieval with Multi-Prefix Embedding — Experiments on MLDR-en, BrowseComp-Plus, and LongEmbed show that MPE is competitive with or outperforms single-vector, independent-chunk, and multi-vector baselines, while providing a natural source attribution mechanism for locating evidence chunks. | Not Disclosed | Experiments were run on 8 NVIDIA RTX 5090 GPUs. | Not Disclosed | Not Disclosed | Not Disclosed | We use learning rate 1 × 10 − 4 1{\times}10^{-4} , temperature τ = 0.03 \tau=0.03 , per-GPU batch size 2, group size 4, query length 512, maximum document length 8,192, right-side padding, and gradient checkpointing. | Not Disclosed | Not Disclosed | Experiments on MLDR-en, BrowseComp-Plus, and LongEmbed show that MPE is competitive with or outperforms single-vector, independent-chunk, and multi-vector baselines, while providing a natural source attribution mechanism for locating evidence chunks. |
| SF-2026-ARXIV-2606-23654 | EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions — Because the sessions contain internal enterprise content, we do not release the benchmark data; instead, our reusable contribution is the construction and evaluation protocol. | GPT-5.5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | These results show that enterprise agent evaluation must report harness--model combinations, artifact delivery, visual quality, cost, runtime, and skill-transfer behavior, rather than collapsing performance into a single score. | Because the sessions contain internal enterprise content, we do not release the benchmark data; instead, our reusable contribution is the construction and evaluation protocol. |
| SF-2026-ARXIV-2606-23664 | MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems? — System prompts thus form a critical and accessible optimization surface: they specify agents' roles and behaviors, enabling system-level improvements without model finetuning. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Multi-agent systems (MAS) offer a scalable path forward for agentic AI, comprising multiple LLM-based agents, each assigned a system prompt and a position within a workflow that governs inter-agent coordination and output aggregation. | Not Disclosed | System prompts thus form a critical and accessible optimization surface: they specify agents' roles and behaviors, enabling system-level improvements without model finetuning. |
| SF-2026-ARXIV-2606-23671 | Can LLMs Reliably Self-Report Adversarial Prefills, and How? — Prior work shows that large language models (LLMs) exhibit introspective capability on benign tasks. | GPT-4.1-labeled | Not Disclosed | All open-weight checkpoints are loaded from their default Hugging Face revisions on the dates we ran each evaluation, with bf16 precision. | Not Disclosed | Not Disclosed | The intention and tampering classifiers fine-tune the roberta-base checkpoint for four epochs at learning rate 2 × 10 − 5 2\times 10^{-5} and per-device train batch size 32 32 on the GPT-4.1-labeled training examples described in Section 4 , with a stratified 80/20 train/test split. All three training methods use the same backbone configuration: rank- 16 16 LoRA (alpha 32 32 , dropout 0.05 0.05 ) targeting the query, key, value, output, gate, up, and down projections at every layer ( Hu et al., 2022 ) , AdamW optimizer, cosine schedule with 5 % 5\% warm-up, effective batch size of 8 8 via gradient accumulation, a | Not Disclosed | Not Disclosed | Prior work shows that large language models (LLMs) exhibit introspective capability on benign tasks. |
| SF-2026-ARXIV-2606-23686 | LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models — We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. | Not Disclosed | The selected models are initialized with their official configurations, and all experiments are conducted on 8 NVIDIA A800 GPUs to guarantee a fair and standardized comparison. | This formulation explicitly quantifies the capacity of the robot to modulate contact dynamics during precision manipulation primitives without inducing structural degradation to the environment. Training Parameter Value Optimization Steps 200,000 200,000 Local Batch Size (per GPU) 16 16 Peak Learning Rate ( η \eta ) 5.0 × 10 − 4 5.0\times 10^{-4} Gradient Accumulation Steps 1 1 Image Augmentation True LoRA Configuration LoRA Rank ( r r ) 32 32 Dropout Rate 0.0 0.0 OpenVLA We employ Low-Rank Adaptation (LoRA) to fine-tune the OpenVLA model, facilitating efficient parameter updates while maintaining high control pr | Not Disclosed | Not Disclosed | Training Parameter Value Optimization Steps 200,000 200,000 Local Batch Size (per GPU) 16 16 Peak Learning Rate ( η \eta ) 5.0 × 10 − 4 5.0\times 10^{-4} Gradient Accumulation Steps 1 1 Image Augmentation True LoRA Configuration LoRA Rank ( r r ) 32 32 Dropout Rate 0.0 0.0 OpenVLA We employ Low-Rank Adaptation (LoRA) to fine-tune the OpenVLA model, facilitating efficient parameter updates while maintaining high control precision. The training is conducted on 8 GPUs with a local batch size of 16 per device, yielding a total effective batch size of 128. | Not Disclosed | Not Disclosed | We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. |
| SF-2026-ARXIV-2606-23752 | ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents — The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. | Claude Code | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. |
| SF-2026-ARXIV-2606-23754 | Verifiable Foundation Models for Robot Safety — To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. |
| SF-2026-ARXIV-2606-23768 | Cryptographic certificates of validity for trustworthy AI — We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. |
| SF-2026-ARXIV-2606-23797 | From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes — The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. | Not Disclosed | The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. |
| SF-2026-ARXIV-2606-23858 | Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications — Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. | Not Disclosed | Not Disclosed | An important technicality here is that we use a precision constant δ > 0 \delta>0 to ensure a “meaningful” reduction of the interval. Definition 4 (Constrain Operator) Consider an input 𝐱 ∈ 𝔽 \mathbf{x}\in\mathbb{F} , an interval I = 𝐱 + [ ℓ , 𝒖 ] I=\mathbf{x}+[\boldsymbol{\ell},\boldsymbol{u}] , with ℓ ≤ 𝟎 ≤ 𝒖 \boldsymbol{\ell}\leq\mathbf{0}\leq\boldsymbol{u} , an adversarial example 𝐯 ∈ I \mathbf{v}\in I , and a precision constant δ > 0 \delta>0 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. |
| SF-2026-ARXIV-2606-23872 | MGI: Member vs Generated Inference — Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Model Batch Size Learning Rate Training Samples Epochs VAR 4 1 × 10 − 5 1\times 10^{-5} 5000 5 RAR 4 1 × 10 − 5 1\times 10^{-5} 5000 5 SD 1.4 4 1 × 10 − 5 1\times 10^{-5} 5000 20 SD 2.1 4 1 × 10 − 5 1\times 10^{-5} 5000 20 Appendix B Distribution Visualization on More Models In this section, we complement the distribution analysis of the main paper with visualizations for additional models and settings. | Not Disclosed | Not Disclosed | Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. |
| SF-2026-ARXIV-2606-23892 | REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs — Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. | Not Disclosed | [22] NVIDIA Cosmos-Reason1-7B . Note: https://huggingface.co/nvidia/Cosmos-Reason1-7B Hugging Face model card Cited by: §1 , §4.2 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our evaluation shows that text and typographic injection attacks induce the most failures, multimodal co-optimization yields the strongest visual-perturbation transfer, single-pass attacks approach iterative methods at much lower cost, and model scale alone does not confer adversarial robustness. | Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. |
| SF-2026-ARXIV-2606-23915 | Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs — We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. | Not Disclosed | Not Disclosed | ALCE ( Gao et al., 2023 ) introduced NLI-based citation recall/precision (with QAMPARI ( Amouyal et al., 2023 ) ); FActScore ( Min et al., 2023 ) decomposes into atomic facts; Attribute-First ( Slobodkin et al., 2024 ) and LongCite ( Zhang et al., 2024 ) produce attributable text; AttrScore ( Yue et al., 2023 ) and RAGAS ( Es et al., 2024 ) judge support with LLM/entailment models. We measure citation count , which is flat; we did not regenerate NLI-based ALCE citation recall/precision ( Gao et al., 2023 ) (it requires a large entailment model and a different decoding setup), and we make no claim about it here. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. | We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. |
| SF-2026-ARXIV-2606-23927 | RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems — Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. | Not Disclosed | Not Disclosed | The evaluator reports this as an F1 score using precision 1 1 and recall / M / / / P / /M///P/ : Coverage-F1 = 2 ​ r 1 + r , r = / M / / P / . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. |
| SF-2026-ARXIV-2606-23937 | When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents — Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. | Qwen2.5-3B | Not Disclosed | B.4 Per-class and per-task behaviour To check whether aggregate macro-F1 masks class-specific behavior, Table 5 reports per-class precision/recall/F1 (computed from the SFT predictions, pooled over seeds). Input class P R F1 raw allow 0.50 0.32 0.39 verify 0.69 0.46 0.55 refuse 0.31 0.70 0.43 raw+policy allow 0.82 0.39 0.53 verify 0.59 0.54 0.56 refuse 0.46 0.89 0.60 structured allow 0.59 0.67 0.63 verify 0.88 0.40 0.55 refuse 0.47 1.00 0.64 Table 5: Per-class precision/recall/F1 (SFT gate, pooled over 3 seeds; computed from committed predictions). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. |
| SF-2026-ARXIV-2606-23961 | Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets — Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. | Llama-3.1-8B-Instruct | All experiments run on a single NVIDIA H200 (143 GB) with greedy decoding. | Not Disclosed | Not Disclosed | Not Disclosed | All runs use Llama-3.1-8B-Instruct in bf16 on a single H200 (143 GB), prefill length T p = 8 ​ K T_{p}=8\text{K} , batch size 1, against dense FlashAttention-2 [ 6 ] and the baselines from Tables 1 – 2 . Table 4: Decode throughput (tokens/s) and per-step latency (ms) at T p = 8 ​ K T_{p}=8\text{K} prefill, batch size 1, on Llama-3.1-8B-Instruct (H200, bf16). | Not Disclosed | Not Disclosed | Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. |
| SF-2026-ARXIV-2606-23969 | The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing — We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. | Not Disclosed | 2 Background 2.1 GPU-CC and the CVM-GPU Bridge In the configuration we study, Intel TDX protects a confidential VM ( Intel, 2026 ) and NVIDIA GPU-CC protects GPU execution and the GPU’s Compute Protected Region (CPR) ( NVIDIA, 2026a ; NVIDIA, 2026e ) . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. | Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. | We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. |
| SF-2026-ARXIV-2606-23983 | Maestro Order: A Model-Agnostic Orchestration Harness — We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. | We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. |
| SF-2026-ARXIV-2606-23989 | Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization — We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. | Not Disclosed | Experiments run on 4 × 4\times A100 GPUs; full hyperparameters, prompts, schemas, and per-module algorithms are in Appendices A , B , and C (Table 7 ). The full run uses four A100 GPUs, with extraction, clustering, selection, rewriting, and verification logged separately for reproducibility. | We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. CAMS matches strong end-to-end and span-attribution baselines on summary quality while substantially improving faithfulness and citation precision, lifting multi-source attribution accuracy by roughly two-thirds, and exposing  | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. |
| SF-2026-ARXIV-2606-24004 | Towards Spec Learning: Inference-Time Alignment from Preference Pairs — We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. | DeepSeek, Gemma, Qwen | • Proposers & Judges (Compilation and Evaluation): – Gemma 4 31B: 1 × 1\times NVIDIA H200 – DeepSeek V4 Flash: 2 × 2\times NVIDIA B200 – Kimi K2.6: 8 × 8\times NVIDIA H200 • Base Policy (Qwen 2.5 32B Instruct): – Inference (Baseline and Spec Application): 1 × 1\times NVIDIA A100 (80GB) – DPO Training: 1 × 1\times NVIDIA H200 Appendix F DPO Training Configuration We train each DPO baseline with TRL’s DPOTrainer Rafailov et al. | You maintain absolute precision in your implementation, ensuring that all variable names are consistent and correctly spelled, and that keywords, boolean values, assignments, and comparison operators are entirely free of typos. Hyperparameter Value Base model Qwen 2.5 32B Instruct Training pairs ( N N ) 1,000 (900 for Truthy-DPO) DPO β \beta 0.1 Optimizer AdamW Learning rate 5 × 10 − 6 5{\times}10^{-6} LR scheduler cosine, warmup ratio 0.1 Epochs 3 Effective batch size 16 Max sequence length 1024 Precision bf16 LoRA rank ( r r ) 32 LoRA α \alpha 64 LoRA dropout 0.05 LoRA targets all attention and FFN projections  | Hyperparameter Value Base model Qwen 2.5 32B Instruct Training pairs ( N N ) 1,000 (900 for Truthy-DPO) DPO β \beta 0.1 Optimizer AdamW Learning rate 5 × 10 − 6 5{\times}10^{-6} LR scheduler cosine, warmup ratio 0.1 Epochs 3 Effective batch size 16 Max sequence length 1024 Precision bf16 LoRA rank ( r r ) 32 LoRA α \alpha 64 LoRA dropout 0.05 LoRA targets all attention and FFN projections Checkpoint selection lowest evaluation loss Hardware 1 × \times H200 NeurIPS Paper Checklist 1. | Not Disclosed | Hyperparameter Value Base model Qwen 2.5 32B Instruct Training pairs ( N N ) 1,000 (900 for Truthy-DPO) DPO β \beta 0.1 Optimizer AdamW Learning rate 5 × 10 − 6 5{\times}10^{-6} LR scheduler cosine, warmup ratio 0.1 Epochs 3 Effective batch size 16 Max sequence length 1024 Precision bf16 LoRA rank ( r r ) 32 LoRA α \alpha 64 LoRA dropout 0.05 LoRA targets all attention and FFN projections Checkpoint selection lowest evaluation loss Hardware 1 × \times H200 NeurIPS Paper Checklist 1. | Not Disclosed | Not Disclosed | We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. |
| SF-2026-ARXIV-2606-24020 | You Don't Need to Run Every Eval — A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. |
| SF-2026-ARXIV-2606-24033 | RoPE-Aware Bit Allocation for KV-Cache Quantization — On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. | DeepSeek-R1-Distill-Qwen-7B, Llama-3.1-8B-Instruct, Qwen2.5-3B-Instruct | We further implement a packed-cache serving path that avoids materializing an fp16 KV cache: on a single H800 GPU with Qwen2.5-3B-Instruct, the packed K3V3 path achieves 3.24 × 3.24\times KV-cache compression with quality comparable to fp16, runs 1.34 × 1.34\times faster than fp16 FlashAttention2 at 128 128 K context, reduces peak memory from 56.31 56.31 GB to 19.85 19.85 GB, and remains feasible at 256 256 K/ 512 512 K where fp16 OOMs. 6.4 Block-GTQ Deployment We run Qwen2.5-3B-Instruct on a single H800 GPU at the K3V3 operating point and report decode-step latency, peak GPU memory, and downstream perplexity. | Non-uniform precision allocation. Key-cache quantization should allocate precision across RoPE blocks according to their logit impact, rather than optimize a single flat-vector reconstruction objective over the whole key head. | Autoregressive long-context decoding is often limited by repeatedly reading a KV cache that grows with sequence length [ 27 ] . | Not Disclosed | Not Disclosed | Not Disclosed | This makes key-cache quantization a block-wise bit-allocation problem: high-energy RoPE blocks are more sensitive to quantization error and should receive more bits. | On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. |
| SF-2026-ARXIV-2606-24040 | Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo — This paper asks how such memories can reduce the need for retraining when knowledge changes. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This paper asks how such memories can reduce the need for retraining when knowledge changes. |
| SF-2026-ARXIV-2606-24551 | GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents — Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. |
| SF-2026-ARXIV-2606-24934 | Unprivileged Topology Certificates for Cloud GPU Attestation — A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. | Not Disclosed | NVIDIA confidential computing extends this to the GPU with a hardware-fused device identity and signed measurements of firmware and configuration [ 2 ] . CUDA device attributes, nvidia-smi telemetry, and clock64() are related but provide distinct operational views. | Each payload is an LZMA-compressed copy of the original file, so the store is reversible without dropping rows, reducing precision, or sampling the timing streams. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A CUDA probe measures an SM-by-memory-region latency matrix using physical SM labels and dependent global loads. | A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. |
| SF-2026-ARXIV-2606-28385 | RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis — However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. | Not Disclosed | We construct GR1-Sim from the NVIDIA PhysicalAI Robotics GR00T Teleop-Sim dataset 1 1 1 https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-Teleop-Sim . The pairs are used to fully fine-tune Cosmos Predict 2.5 [ 1 ] with AdamW on 8 8 NVIDIA L40 GPUs. | We report description precision/recall/ F 1 F_{1} by summing S i ​ j S_{ij} over 𝒜 \mathcal{A} and normalizing by N N or M M , temporal mIoU by averaging IoU t \text{IoU}_{t} over matched pairs, and joint F 1 × IoU F_{1}\!\times\!\text{IoU} by replacing S i ​ j S_{ij} with S i ​ j ​ IoU t S_{ij}\text{IoU}_{t} in the same precision–recall computation. Finally, our view-agnostic specialists can miss view-dependent evidence, the precision-oriented verifier can suppress rare transient glitches (leaving the precision–recall point downstream-dependent), and the closed-world taxonomy with multi-agent orchestration costs | Not Disclosed | Not Disclosed | NVIDIA L40 ( 48 48 GB) with tensor parallelism = 4 =4 , batch size 1 1 , and BF16 weights unless otherwise noted. | We present RoboGaze, a training-free, multi-agent VLM framework that provides structured, interpretable evaluation for generated robot-manipulation videos. | Not Disclosed | However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. |
| SF-2026-ARXIV-2606-28386 | Data Provenance for Image Auto-Regressive Generation — Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. | LlamaGen | All experiments were conducted on standard hardware (NVIDIA A40 GPUs) with specified software versions. All experiments were conducted on a single NVIDIA A40 GPU with 48GB of memory. | Not Disclosed | Not Disclosed | Not Disclosed | All experimental configurations, including hyperparameters for finetuning the inverse decoder across six different open-source models (LlamaGen, RAR, Taming, VAR, Infinity, VQ-Diffusion), are detailed in Appendix C with specific learning rates, batch sizes, and training schedules. We detail the finetuning hyperparameters, such as the number of images, the batch size and learning rate for every model in Table A1 . | Not Disclosed | Not Disclosed | Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-22741 | score_7_9; potential_books_delta | selected | DA-20260623-DEPENDENCY-GRADED-TRACE | — | 入选：GRADE 把 execution 与 dependency 两层、edge-source grade、failure localization 和跨 agent-class transfer 接成同一可观测状态链。 | analysis:DA-20260623-DEPENDENCY-GRADED-TRACE |
| SF-2026-ARXIV-2606-22768 | score_7_9; potential_books_delta | selected | DA-20260623-FACTORED-GOSSIP | — | 入选：Factored Gossip DiLoCo 把非阻塞 Mix1、阻塞 Mix2、worker disagreement 与 compute-utilization/稳定性 trade-off 接成分布式训练控制面。 | analysis:DA-20260623-FACTORED-GOSSIP |
| SF-2026-ARXIV-2606-22778 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-RAG` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22778 |
| SF-2026-ARXIV-2606-22783 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22783 |
| SF-2026-ARXIV-2606-22792 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22792 |
| SF-2026-ARXIV-2606-22794 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22794 |
| SF-2026-ARXIV-2606-22798 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MODEL-MOE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22798 |
| SF-2026-ARXIV-2606-22804 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-WORLD-MODELS` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22804 |
| SF-2026-ARXIV-2606-22826 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22826 |
| SF-2026-ARXIV-2606-22827 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22827 |
| SF-2026-ARXIV-2606-22840 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-SPECULATIVE-DECODING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22840 |
| SF-2026-ARXIV-2606-22844 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22844 |
| SF-2026-ARXIV-2606-22864 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22864 |
| SF-2026-ARXIV-2606-22873 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22873 |
| SF-2026-ARXIV-2606-22874 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MODEL-LONG-CONTEXT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22874 |
| SF-2026-ARXIV-2606-22875 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-MODEL-REGISTRY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22875 |
| SF-2026-ARXIV-2606-22877 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22877 |
| SF-2026-ARXIV-2606-22878 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-LORA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22878 |
| SF-2026-ARXIV-2606-22883 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-DATA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22883 |
| SF-2026-ARXIV-2606-22902 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22902 |
| SF-2026-ARXIV-2606-22906 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-CONTEXT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22906 |
| SF-2026-ARXIV-2606-22916 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22916 |
| SF-2026-ARXIV-2606-22918 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22918 |
| SF-2026-ARXIV-2606-22925 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22925 |
| SF-2026-ARXIV-2606-22932 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-DISTRIBUTED-TRAINING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22932 |
| SF-2026-ARXIV-2606-22936 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-PLANNING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22936 |
| SF-2026-ARXIV-2606-22942 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-SFT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22942 |
| SF-2026-ARXIV-2606-22948 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-PLANNING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22948 |
| SF-2026-ARXIV-2606-22953 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-CONTEXT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22953 |
| SF-2026-ARXIV-2606-22966 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-WORLD-MODELS` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22966 |
| SF-2026-ARXIV-2606-22968 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-PREFILL` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22968 |
| SF-2026-ARXIV-2606-22977 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22977 |
| SF-2026-ARXIV-2606-22983 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-SCHEDULING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-22983 |
| SF-2026-ARXIV-2606-23001 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-GPU-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23001 |
| SF-2026-ARXIV-2606-23003 | score_7_9; potential_books_delta | selected | DA-20260623-VERIFIABLE-CONVERSATION-STATE | — | 入选：VCT 用 Q&A hash chain、session/account Merkle root、joint signature、deletion barrier 与 deterministic merge 定义可验证会话状态。 | analysis:DA-20260623-VERIFIABLE-CONVERSATION-STATE |
| SF-2026-ARXIV-2606-23017 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-DISTRIBUTED-TRAINING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23017 |
| SF-2026-ARXIV-2606-23026 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23026 |
| SF-2026-ARXIV-2606-23030 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23030 |
| SF-2026-ARXIV-2606-23038 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-RLHF` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23038 |
| SF-2026-ARXIV-2606-23049 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-TOOL-CALLING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23049 |
| SF-2026-ARXIV-2606-23075 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23075 |
| SF-2026-ARXIV-2606-23112 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-TOOL-CALLING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23112 |
| SF-2026-ARXIV-2606-23127 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23127 |
| SF-2026-ARXIV-2606-23130 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23130 |
| SF-2026-ARXIV-2606-23181 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-SCHEDULING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23181 |
| SF-2026-ARXIV-2606-23189 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23189 |
| SF-2026-ARXIV-2606-23195 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23195 |
| SF-2026-ARXIV-2606-23217 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23217 |
| SF-2026-ARXIV-2606-23276 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23276 |
| SF-2026-ARXIV-2606-23277 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23277 |
| SF-2026-ARXIV-2606-23283 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23283 |
| SF-2026-ARXIV-2606-23321 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23321 |
| SF-2026-ARXIV-2606-23370 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-SCHEDULING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23370 |
| SF-2026-ARXIV-2606-23403 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23403 |
| SF-2026-ARXIV-2606-23404 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23404 |
| SF-2026-ARXIV-2606-23416 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23416 |
| SF-2026-ARXIV-2606-23449 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23449 |
| SF-2026-ARXIV-2606-23459 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23459 |
| SF-2026-ARXIV-2606-23521 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-DECODE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23521 |
| SF-2026-ARXIV-2606-23525 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23525 |
| SF-2026-ARXIV-2606-23546 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-COST` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23546 |
| SF-2026-ARXIV-2606-23581 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-KV-CACHE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23581 |
| SF-2026-ARXIV-2606-23583 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23583 |
| SF-2026-ARXIV-2606-23589 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23589 |
| SF-2026-ARXIV-2606-23617 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23617 |
| SF-2026-ARXIV-2606-23642 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-RAG` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23642 |
| SF-2026-ARXIV-2606-23654 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23654 |
| SF-2026-ARXIV-2606-23664 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MULTI-AGENT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23664 |
| SF-2026-ARXIV-2606-23671 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23671 |
| SF-2026-ARXIV-2606-23686 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23686 |
| SF-2026-ARXIV-2606-23752 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23752 |
| SF-2026-ARXIV-2606-23754 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23754 |
| SF-2026-ARXIV-2606-23768 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23768 |
| SF-2026-ARXIV-2606-23797 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-WORKFLOW` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23797 |
| SF-2026-ARXIV-2606-23858 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23858 |
| SF-2026-ARXIV-2606-23872 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23872 |
| SF-2026-ARXIV-2606-23892 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23892 |
| SF-2026-ARXIV-2606-23915 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23915 |
| SF-2026-ARXIV-2606-23927 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23927 |
| SF-2026-ARXIV-2606-23937 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23937 |
| SF-2026-ARXIV-2606-23961 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-KV-CACHE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23961 |
| SF-2026-ARXIV-2606-23969 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23969 |
| SF-2026-ARXIV-2606-23983 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23983 |
| SF-2026-ARXIV-2606-23989 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-RAG` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-23989 |
| SF-2026-ARXIV-2606-24004 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-RLHF` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-24004 |
| SF-2026-ARXIV-2606-24020 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-24020 |
| SF-2026-ARXIV-2606-24033 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `INFER-KV-CACHE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-24033 |
| SF-2026-ARXIV-2606-24040 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-24040 |
| SF-2026-ARXIV-2606-24551 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `AGENT-TOOL-CALLING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-24551 |
| SF-2026-ARXIV-2606-24934 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-24934 |
| SF-2026-ARXIV-2606-28385 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `MULTIMODAL-WORLD-MODELS` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-28385 |
| SF-2026-ARXIV-2606-28386 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：完整 frontier 保留 `TRAIN-DATA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-28386 |

<!-- analysis-decision:SF-2026-ARXIV-2606-22778:start -->
未入选：完整 frontier 保留 `AGENT-RAG` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22778:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22783:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22783:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22792:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22792:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22794:start -->
未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22794:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22798:start -->
未入选：完整 frontier 保留 `MODEL-MOE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22798:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22804:start -->
未入选：完整 frontier 保留 `MULTIMODAL-WORLD-MODELS` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22804:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22826:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22826:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22827:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22827:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22840:start -->
未入选：完整 frontier 保留 `INFER-SPECULATIVE-DECODING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22840:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22844:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22844:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22864:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22864:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22873:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22873:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22874:start -->
未入选：完整 frontier 保留 `MODEL-LONG-CONTEXT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22874:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22875:start -->
未入选：完整 frontier 保留 `PLATFORM-MODEL-REGISTRY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22875:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22877:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22877:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22878:start -->
未入选：完整 frontier 保留 `TRAIN-LORA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22878:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22883:start -->
未入选：完整 frontier 保留 `TRAIN-DATA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22883:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22902:start -->
未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22902:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22906:start -->
未入选：完整 frontier 保留 `AGENT-CONTEXT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22906:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22916:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22916:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22918:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22918:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22925:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22925:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22932:start -->
未入选：完整 frontier 保留 `TRAIN-DISTRIBUTED-TRAINING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22932:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22936:start -->
未入选：完整 frontier 保留 `AGENT-PLANNING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22936:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22942:start -->
未入选：完整 frontier 保留 `TRAIN-SFT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22942:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22948:start -->
未入选：完整 frontier 保留 `AGENT-PLANNING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22948:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22953:start -->
未入选：完整 frontier 保留 `AGENT-CONTEXT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22953:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22966:start -->
未入选：完整 frontier 保留 `MULTIMODAL-WORLD-MODELS` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22966:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22968:start -->
未入选：完整 frontier 保留 `INFER-PREFILL` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22968:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22977:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22977:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22983:start -->
未入选：完整 frontier 保留 `INFER-SCHEDULING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-22983:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23001:start -->
未入选：完整 frontier 保留 `INFER-GPU-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23001:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23017:start -->
未入选：完整 frontier 保留 `TRAIN-DISTRIBUTED-TRAINING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23017:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23026:start -->
未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23026:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23030:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23030:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23038:start -->
未入选：完整 frontier 保留 `TRAIN-RLHF` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23038:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23049:start -->
未入选：完整 frontier 保留 `AGENT-TOOL-CALLING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23049:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23075:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23075:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23112:start -->
未入选：完整 frontier 保留 `AGENT-TOOL-CALLING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23112:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23127:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23127:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23130:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23130:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23181:start -->
未入选：完整 frontier 保留 `INFER-SCHEDULING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23181:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23189:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23189:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23195:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23195:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23217:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23217:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23276:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23276:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23277:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23277:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23283:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23283:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23321:start -->
未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23321:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23370:start -->
未入选：完整 frontier 保留 `INFER-SCHEDULING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23370:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23403:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23403:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23404:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23404:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23416:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23416:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23449:start -->
未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23449:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23459:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23459:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23521:start -->
未入选：完整 frontier 保留 `INFER-DECODE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23521:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23525:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23525:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23546:start -->
未入选：完整 frontier 保留 `PLATFORM-COST` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23546:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23581:start -->
未入选：完整 frontier 保留 `INFER-KV-CACHE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23581:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23583:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23583:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23589:start -->
未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23589:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23617:start -->
未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23617:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23642:start -->
未入选：完整 frontier 保留 `AGENT-RAG` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23642:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23654:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23654:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23664:start -->
未入选：完整 frontier 保留 `AGENT-MULTI-AGENT` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23664:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23671:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23671:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23686:start -->
未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23752:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23752:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23754:start -->
未入选：完整 frontier 保留 `MULTIMODAL-EMBODIED-VLA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23754:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23768:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23768:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23797:start -->
未入选：完整 frontier 保留 `AGENT-WORKFLOW` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23797:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23858:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23858:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23872:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23872:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23892:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23892:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23915:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23915:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23927:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23927:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23937:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23937:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23961:start -->
未入选：完整 frontier 保留 `INFER-KV-CACHE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23961:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23969:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23969:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23983:start -->
未入选：完整 frontier 保留 `AGENT-PLATFORM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23983:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23989:start -->
未入选：完整 frontier 保留 `AGENT-RAG` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-23989:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24004:start -->
未入选：完整 frontier 保留 `TRAIN-RLHF` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-24004:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24020:start -->
未入选：完整 frontier 保留 `PLATFORM-EVALUATION-SYSTEM` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-24020:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24033:start -->
未入选：完整 frontier 保留 `INFER-KV-CACHE` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-24033:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24040:start -->
未入选：完整 frontier 保留 `AGENT-MEMORY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-24040:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24551:start -->
未入选：完整 frontier 保留 `AGENT-TOOL-CALLING` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-24551:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24934:start -->
未入选：完整 frontier 保留 `PLATFORM-SECURITY` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-24934:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28385:start -->
未入选：完整 frontier 保留 `MULTIMODAL-WORLD-MODELS` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-28385:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28386:start -->
未入选：完整 frontier 保留 `TRAIN-DATA` 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-28386:end -->

<!-- analysis:DA-20260623-DEPENDENCY-GRADED-TRACE:start -->
### DA-20260623-DEPENDENCY-GRADED-TRACE
Agent trace 只记录执行顺序会漏掉 reliance failure；GRADE 用 execution/dependency 双层图和 observed/declared/inferred edge grade 补出状态依赖，但 inferred full-history graph 的信号会退化成 run size，不能把 graph score 当因果证明。
<!-- analysis:DA-20260623-DEPENDENCY-GRADED-TRACE:end -->

<!-- analysis:DA-20260623-FACTORED-GOSSIP:start -->
### DA-20260623-FACTORED-GOSSIP
DiLoCo 的全局同步既阻塞又脆弱；Factored Gossip 将 Mix1 与计算重叠、让 Mix2 只承担收紧共识的阻塞工作。收益是利用率与故障降级，代价是 worker disagreement 和训练稳定性必须被持续测量。
<!-- analysis:DA-20260623-FACTORED-GOSSIP:end -->

<!-- analysis:DA-20260623-VERIFIABLE-CONVERSATION-STATE:start -->
### DA-20260623-VERIFIABLE-CONVERSATION-STATE
VCT 把 conversation branch、session 与 account 变成三层认证状态，并用 joint signature、deletion barrier、deterministic merge 与 device gossip 约束并发和恶意 server view fork；密码学完整性不证明内容真实性。
<!-- analysis:DA-20260623-VERIFIABLE-CONVERSATION-STATE:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-22741 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-22741 | delta:SF-2026-ARXIV-2606-22741 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22741 |
| SF-2026-ARXIV-2606-22768 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-22768 | delta:SF-2026-ARXIV-2606-22768 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22768 |
| SF-2026-ARXIV-2606-22778 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-22778 | delta:SF-2026-ARXIV-2606-22778 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22778 |
| SF-2026-ARXIV-2606-22783 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-22783 | delta:SF-2026-ARXIV-2606-22783 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22783 |
| SF-2026-ARXIV-2606-22792 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-22792 | delta:SF-2026-ARXIV-2606-22792 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22792 |
| SF-2026-ARXIV-2606-22794 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-22794 | delta:SF-2026-ARXIV-2606-22794 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22794 |
| SF-2026-ARXIV-2606-22798 | MODEL-MOE | books/part-02-model/21-moe.md#L1 | books/part-02-model/22-long-context.md#L1 | existing:SF-2026-ARXIV-2606-22798 | delta:SF-2026-ARXIV-2606-22798 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22798 |
| SF-2026-ARXIV-2606-22804 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-22804 | delta:SF-2026-ARXIV-2606-22804 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22804 |
| SF-2026-ARXIV-2606-22826 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-22826 | delta:SF-2026-ARXIV-2606-22826 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22826 |
| SF-2026-ARXIV-2606-22827 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-22827 | delta:SF-2026-ARXIV-2606-22827 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22827 |
| SF-2026-ARXIV-2606-22840 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/49-tensorrt-llm.md#L1 | existing:SF-2026-ARXIV-2606-22840 | delta:SF-2026-ARXIV-2606-22840 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22840 |
| SF-2026-ARXIV-2606-22844 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-22844 | delta:SF-2026-ARXIV-2606-22844 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22844 |
| SF-2026-ARXIV-2606-22864 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-22864 | delta:SF-2026-ARXIV-2606-22864 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22864 |
| SF-2026-ARXIV-2606-22873 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-22873 | delta:SF-2026-ARXIV-2606-22873 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22873 |
| SF-2026-ARXIV-2606-22874 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L1 | books/part-02-model/21-moe.md#L1 | existing:SF-2026-ARXIV-2606-22874 | delta:SF-2026-ARXIV-2606-22874 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22874 |
| SF-2026-ARXIV-2606-22875 | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#L1 | books/part-06-ai-infrastructure/60-training-operator.md#L1 | existing:SF-2026-ARXIV-2606-22875 | delta:SF-2026-ARXIV-2606-22875 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22875 |
| SF-2026-ARXIV-2606-22877 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-22877 | delta:SF-2026-ARXIV-2606-22877 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22877 |
| SF-2026-ARXIV-2606-22878 | TRAIN-LORA | books/part-04-training-system/30-lora.md#L1 | books/part-04-training-system/31-rlhf.md#L1 | existing:SF-2026-ARXIV-2606-22878 | delta:SF-2026-ARXIV-2606-22878 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22878 |
| SF-2026-ARXIV-2606-22883 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-22883 | delta:SF-2026-ARXIV-2606-22883 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22883 |
| SF-2026-ARXIV-2606-22902 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-22902 | delta:SF-2026-ARXIV-2606-22902 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22902 |
| SF-2026-ARXIV-2606-22906 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-22906 | delta:SF-2026-ARXIV-2606-22906 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22906 |
| SF-2026-ARXIV-2606-22916 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-22916 | delta:SF-2026-ARXIV-2606-22916 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22916 |
| SF-2026-ARXIV-2606-22918 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-22918 | delta:SF-2026-ARXIV-2606-22918 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22918 |
| SF-2026-ARXIV-2606-22925 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-22925 | delta:SF-2026-ARXIV-2606-22925 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22925 |
| SF-2026-ARXIV-2606-22932 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-22932 | delta:SF-2026-ARXIV-2606-22932 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22932 |
| SF-2026-ARXIV-2606-22936 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-22936 | delta:SF-2026-ARXIV-2606-22936 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22936 |
| SF-2026-ARXIV-2606-22942 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L1 | books/part-04-training-system/30-lora.md#L1 | existing:SF-2026-ARXIV-2606-22942 | delta:SF-2026-ARXIV-2606-22942 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22942 |
| SF-2026-ARXIV-2606-22948 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-22948 | delta:SF-2026-ARXIV-2606-22948 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22948 |
| SF-2026-ARXIV-2606-22953 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-22953 | delta:SF-2026-ARXIV-2606-22953 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22953 |
| SF-2026-ARXIV-2606-22966 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-22966 | delta:SF-2026-ARXIV-2606-22966 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22966 |
| SF-2026-ARXIV-2606-22968 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L1 | books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2606-22968 | delta:SF-2026-ARXIV-2606-22968 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22968 |
| SF-2026-ARXIV-2606-22977 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-22977 | delta:SF-2026-ARXIV-2606-22977 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22977 |
| SF-2026-ARXIV-2606-22983 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-22983 | delta:SF-2026-ARXIV-2606-22983 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22983 |
| SF-2026-ARXIV-2606-23001 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-23001 | delta:SF-2026-ARXIV-2606-23001 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23001 |
| SF-2026-ARXIV-2606-23003 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23003 | delta:SF-2026-ARXIV-2606-23003 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23003 |
| SF-2026-ARXIV-2606-23017 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-23017 | delta:SF-2026-ARXIV-2606-23017 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23017 |
| SF-2026-ARXIV-2606-23026 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-23026 | delta:SF-2026-ARXIV-2606-23026 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23026 |
| SF-2026-ARXIV-2606-23030 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23030 | delta:SF-2026-ARXIV-2606-23030 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23030 |
| SF-2026-ARXIV-2606-23038 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-23038 | delta:SF-2026-ARXIV-2606-23038 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23038 |
| SF-2026-ARXIV-2606-23049 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-23049 | delta:SF-2026-ARXIV-2606-23049 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23049 |
| SF-2026-ARXIV-2606-23075 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23075 | delta:SF-2026-ARXIV-2606-23075 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23075 |
| SF-2026-ARXIV-2606-23112 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-23112 | delta:SF-2026-ARXIV-2606-23112 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23112 |
| SF-2026-ARXIV-2606-23127 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-23127 | delta:SF-2026-ARXIV-2606-23127 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23127 |
| SF-2026-ARXIV-2606-23130 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23130 | delta:SF-2026-ARXIV-2606-23130 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23130 |
| SF-2026-ARXIV-2606-23181 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-23181 | delta:SF-2026-ARXIV-2606-23181 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23181 |
| SF-2026-ARXIV-2606-23189 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23189 | delta:SF-2026-ARXIV-2606-23189 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23189 |
| SF-2026-ARXIV-2606-23195 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-23195 | delta:SF-2026-ARXIV-2606-23195 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23195 |
| SF-2026-ARXIV-2606-23217 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23217 | delta:SF-2026-ARXIV-2606-23217 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23217 |
| SF-2026-ARXIV-2606-23276 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23276 | delta:SF-2026-ARXIV-2606-23276 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23276 |
| SF-2026-ARXIV-2606-23277 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23277 | delta:SF-2026-ARXIV-2606-23277 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23277 |
| SF-2026-ARXIV-2606-23283 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-23283 | delta:SF-2026-ARXIV-2606-23283 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23283 |
| SF-2026-ARXIV-2606-23321 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-23321 | delta:SF-2026-ARXIV-2606-23321 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23321 |
| SF-2026-ARXIV-2606-23370 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-23370 | delta:SF-2026-ARXIV-2606-23370 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23370 |
| SF-2026-ARXIV-2606-23403 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23403 | delta:SF-2026-ARXIV-2606-23403 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23403 |
| SF-2026-ARXIV-2606-23404 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23404 | delta:SF-2026-ARXIV-2606-23404 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23404 |
| SF-2026-ARXIV-2606-23416 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23416 | delta:SF-2026-ARXIV-2606-23416 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23416 |
| SF-2026-ARXIV-2606-23449 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-23449 | delta:SF-2026-ARXIV-2606-23449 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23449 |
| SF-2026-ARXIV-2606-23459 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-23459 | delta:SF-2026-ARXIV-2606-23459 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23459 |
| SF-2026-ARXIV-2606-23521 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L1 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | existing:SF-2026-ARXIV-2606-23521 | delta:SF-2026-ARXIV-2606-23521 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23521 |
| SF-2026-ARXIV-2606-23525 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-23525 | delta:SF-2026-ARXIV-2606-23525 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23525 |
| SF-2026-ARXIV-2606-23546 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-23546 | delta:SF-2026-ARXIV-2606-23546 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23546 |
| SF-2026-ARXIV-2606-23581 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-23581 | delta:SF-2026-ARXIV-2606-23581 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23581 |
| SF-2026-ARXIV-2606-23583 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23583 | delta:SF-2026-ARXIV-2606-23583 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23583 |
| SF-2026-ARXIV-2606-23589 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-23589 | delta:SF-2026-ARXIV-2606-23589 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23589 |
| SF-2026-ARXIV-2606-23617 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-23617 | delta:SF-2026-ARXIV-2606-23617 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23617 |
| SF-2026-ARXIV-2606-23642 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-23642 | delta:SF-2026-ARXIV-2606-23642 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23642 |
| SF-2026-ARXIV-2606-23654 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23654 | delta:SF-2026-ARXIV-2606-23654 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23654 |
| SF-2026-ARXIV-2606-23664 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-23664 | delta:SF-2026-ARXIV-2606-23664 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23664 |
| SF-2026-ARXIV-2606-23671 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23671 | delta:SF-2026-ARXIV-2606-23671 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23671 |
| SF-2026-ARXIV-2606-23686 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-23686 | delta:SF-2026-ARXIV-2606-23686 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23686 |
| SF-2026-ARXIV-2606-23752 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-23752 | delta:SF-2026-ARXIV-2606-23752 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23752 |
| SF-2026-ARXIV-2606-23754 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-23754 | delta:SF-2026-ARXIV-2606-23754 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23754 |
| SF-2026-ARXIV-2606-23768 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23768 | delta:SF-2026-ARXIV-2606-23768 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23768 |
| SF-2026-ARXIV-2606-23797 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-23797 | delta:SF-2026-ARXIV-2606-23797 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23797 |
| SF-2026-ARXIV-2606-23858 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23858 | delta:SF-2026-ARXIV-2606-23858 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23858 |
| SF-2026-ARXIV-2606-23872 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23872 | delta:SF-2026-ARXIV-2606-23872 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23872 |
| SF-2026-ARXIV-2606-23892 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23892 | delta:SF-2026-ARXIV-2606-23892 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23892 |
| SF-2026-ARXIV-2606-23915 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23915 | delta:SF-2026-ARXIV-2606-23915 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23915 |
| SF-2026-ARXIV-2606-23927 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23927 | delta:SF-2026-ARXIV-2606-23927 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23927 |
| SF-2026-ARXIV-2606-23937 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23937 | delta:SF-2026-ARXIV-2606-23937 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23937 |
| SF-2026-ARXIV-2606-23961 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-23961 | delta:SF-2026-ARXIV-2606-23961 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23961 |
| SF-2026-ARXIV-2606-23969 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23969 | delta:SF-2026-ARXIV-2606-23969 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23969 |
| SF-2026-ARXIV-2606-23983 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-23983 | delta:SF-2026-ARXIV-2606-23983 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23983 |
| SF-2026-ARXIV-2606-23989 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-23989 | delta:SF-2026-ARXIV-2606-23989 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23989 |
| SF-2026-ARXIV-2606-24004 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-24004 | delta:SF-2026-ARXIV-2606-24004 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24004 |
| SF-2026-ARXIV-2606-24020 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-24020 | delta:SF-2026-ARXIV-2606-24020 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24020 |
| SF-2026-ARXIV-2606-24033 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-24033 | delta:SF-2026-ARXIV-2606-24033 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24033 |
| SF-2026-ARXIV-2606-24040 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-24040 | delta:SF-2026-ARXIV-2606-24040 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24040 |
| SF-2026-ARXIV-2606-24551 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-24551 | delta:SF-2026-ARXIV-2606-24551 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24551 |
| SF-2026-ARXIV-2606-24934 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-24934 | delta:SF-2026-ARXIV-2606-24934 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24934 |
| SF-2026-ARXIV-2606-28385 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-28385 | delta:SF-2026-ARXIV-2606-28385 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28385 |
| SF-2026-ARXIV-2606-28386 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-28386 | delta:SF-2026-ARXIV-2606-28386 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28386 |

<!-- existing:SF-2026-ARXIV-2606-22741:start -->
`books/part-07-agent/81-workflow.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22741:end -->

<!-- delta:SF-2026-ARXIV-2606-22741:start -->
GRADE: Graph Representation of LLM Agent Dependency and Execution 的 exact-v1 机制为：A trace records what each step did, never what it relied on, the state it read, and the results it reused. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。
<!-- delta:SF-2026-ARXIV-2606-22741:end -->

<!-- books-review:SF-2026-ARXIV-2606-22741:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Across six corpora of LLM agents spanning tool use, coding, and the web, the dependency layer can predict failure where run size is weak and, under leave-one-corpus-out transfer, stays above chance on every held-out class while run size fails. 披露的 evaluation signal 是：A trace records what each step did, never what it relied on, the state it read, and the results it reused. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22741:end -->

<!-- existing:SF-2026-ARXIV-2606-22768:start -->
`books/part-04-training-system/36-distributed-training.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/37-tensor-parallel.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22768:end -->

<!-- delta:SF-2026-ARXIV-2606-22768:start -->
Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo 的 exact-v1 机制为：On up to billion-parameter language models in low-bandwidth settings, our framework substantially improves compute utilization compared to DiLoCo, with training progress ranging from comparable to closely matching it, and is more robust to failures. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。
<!-- delta:SF-2026-ARXIV-2606-22768:end -->

<!-- books-review:SF-2026-ARXIV-2606-22768:start -->
Unique owner `TRAIN-DISTRIBUTED-TRAINING`; adjacent non-owner `books/part-04-training-system/37-tensor-parallel.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures. 披露的 evaluation signal 是：To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22768:end -->

<!-- existing:SF-2026-ARXIV-2606-22778:start -->
`books/part-07-agent/76-rag.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/77-memory.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22778:end -->

<!-- delta:SF-2026-ARXIV-2606-22778:start -->
HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions 的 exact-v1 机制为：We present HAKARI-Bench, a lightweight benchmark that reconstructs existing retrieval suites into small datasets (Nano-sets): 35 benchmarks and 551 tasks across 43 languages in a unified format, enabling same-condition, model-agnostic comparison of five retrieval families (BM25, dense, sparse, late interaction, rerankers) and their efficiency variants. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。
<!-- delta:SF-2026-ARXIV-2606-22778:end -->

<!-- books-review:SF-2026-ARXIV-2606-22778:start -->
Unique owner `AGENT-RAG`; adjacent non-owner `books/part-07-agent/77-memory.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：With the rapid spread of retrieval-augmented generation and semantic search, choosing the right embedding and retrieval configuration is increasingly hard. 披露的 evaluation signal 是：HAKARI-Bench does not replace full evaluation; it enables rapid model selection, regression detection, and reading the quality-efficiency Pareto frontier. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22778:end -->

<!-- existing:SF-2026-ARXIV-2606-22783:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22783:end -->

<!-- delta:SF-2026-ARXIV-2606-22783:start -->
Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints 的 exact-v1 机制为：We introduce VERITAS (Verifiable Traversal Assessment for Search), a framework built on the principle of computationally irreducible constraints. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-22783:end -->

<!-- books-review:SF-2026-ARXIV-2606-22783:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：We break this paradox by shifting the evaluation paradigm from simulating a messy reality to constructing computationally pure challenges. 披露的 evaluation signal 是：Evaluating the exhaustive search capabilities of large language models (LLMs) is plagued by a fundamental paradox: verifying completeness requires complete ground truth, yet high-entropy enumeration tasks make such ground truth impossible for humans to create. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22783:end -->

<!-- existing:SF-2026-ARXIV-2606-22792:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22792:end -->

<!-- delta:SF-2026-ARXIV-2606-22792:start -->
The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models 的 exact-v1 机制为：In this paper, we propose a granular uncertainty taxonomy that systematically attributes LLM uncertainty into input-level, parameter-level, token-level, and decoding-process sources. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-22792:end -->

<!-- books-review:SF-2026-ARXIV-2606-22792:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Recent advancements in Large Language Models (LLMs) have enabled sophisticated reasoning and content generation, yet their inherent stochasticity poses significant challenges for ensuring predictive credibility. 披露的 evaluation signal 是：While traditional uncertainty taxonomy paradigms, such as the dichotomy of aleatoric and epistemic uncertainties, provide conceptual foundations, they often fail to capture the multi-component and multi-stage nature of LLM generation and struggle to evaluate the effectiveness of various Uncertainty Quantification (UQ) methods. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22792:end -->

<!-- existing:SF-2026-ARXIV-2606-22794:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22794:end -->

<!-- delta:SF-2026-ARXIV-2606-22794:start -->
UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models 的 exact-v1 机制为：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-22794:end -->

<!-- books-review:SF-2026-ARXIV-2606-22794:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 披露的 evaluation signal 是：Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22794:end -->

<!-- existing:SF-2026-ARXIV-2606-22798:start -->
`books/part-02-model/21-moe.md` 的唯一 owner 已承载相关机制链；`books/part-02-model/22-long-context.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22798:end -->

<!-- delta:SF-2026-ARXIV-2606-22798:start -->
Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control 的 exact-v1 机制为：Holding the emitted token id fixed at repeated anchors, we find it does not: the experts that produce it still separate task context, trajectory history, and reasoning-effort mode. 因此 把 router state 视为内部诊断/选择信号，而不是未经验证的正确性证明。
<!-- delta:SF-2026-ARXIV-2606-22798:end -->

<!-- books-review:SF-2026-ARXIV-2606-22798:start -->
Unique owner `MODEL-MOE`; adjacent non-owner `books/part-02-model/22-long-context.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：In sparse Mixture-of-Experts language models, does the same token id imply the same router state and the same experts producing it? 披露的 evaluation signal 是：Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22798:end -->

<!-- existing:SF-2026-ARXIV-2606-22804:start -->
`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22804:end -->

<!-- delta:SF-2026-ARXIV-2606-22804:start -->
CoVStream: Edge-Cloud Collaboration for Understanding of Long Video Streams 的 exact-v1 机制为：Therefore, we propose CoVStream, the first edge-cloud collaborative framework for understanding long video streams. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。
<!-- delta:SF-2026-ARXIV-2606-22804:end -->

<!-- books-review:SF-2026-ARXIV-2606-22804:start -->
Unique owner `MULTIMODAL-WORLD-MODELS`; adjacent non-owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, they overlook a crucial deployment fact: the stream is often produced by computationally constrained devices. 披露的 evaluation signal 是：Experiments on VideoMME-Long, LVBench, and RTV-Bench show that CoVStream reduces bandwidth usage by 87.6% while retaining 99.2% of the cloud baseline accuracy on LVBench. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22804:end -->

<!-- existing:SF-2026-ARXIV-2606-22826:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22826:end -->

<!-- delta:SF-2026-ARXIV-2606-22826:start -->
MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration 的 exact-v1 机制为：We introduce MINCE (Monte Carlo Informed N-sizing for Compact Evaluation), which uses Monte Carlo simulation over per-item logs from a small set of calibration models to find the minimum subset size that bounds accuracy drift and then fixes a randomly sampled subset at that size, with no prediction layer needed. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-22826:end -->

<!-- books-review:SF-2026-ARXIV-2606-22826:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Existing subset selection methods reduce this cost but depend on large calibration pools or learned prediction layers. 披露的 evaluation signal 是：Evaluating LLMs across many model variants -- quantized, fine-tuned, or deployment-specific -- requires running large benchmarks repeatedly, a process that can take tens of hours per model on edge hardware such as NPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22826:end -->

<!-- existing:SF-2026-ARXIV-2606-22827:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22827:end -->

<!-- delta:SF-2026-ARXIV-2606-22827:start -->
What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security 的 exact-v1 机制为：In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-22827:end -->

<!-- books-review:SF-2026-ARXIV-2606-22827:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Modern software development relies heavily on third-party components from public repositories, expanding the software supply chain attack surface. 披露的 evaluation signal 是：In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22827:end -->

<!-- existing:SF-2026-ARXIV-2606-22840:start -->
`books/part-05-inference-system/48-speculative-decoding.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/49-tensorrt-llm.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22840:end -->

<!-- delta:SF-2026-ARXIV-2606-22840:start -->
RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving 的 exact-v1 机制为：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 因此 把 draft/verify/bypass 路由、质量门槛、成本和 schema-critical fallback 共同验收。
<!-- delta:SF-2026-ARXIV-2606-22840:end -->

<!-- books-review:SF-2026-ARXIV-2606-22840:start -->
Unique owner `INFER-SPECULATIVE-DECODING`; adjacent non-owner `books/part-05-inference-system/49-tensorrt-llm.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 披露的 evaluation signal 是：We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22840:end -->

<!-- existing:SF-2026-ARXIV-2606-22844:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22844:end -->

<!-- delta:SF-2026-ARXIV-2606-22844:start -->
RaMem: Contextual Reinstatement for Long-term Agentic Memory 的 exact-v1 机制为：To address this problem, we propose Contextual Reinstatement for Agentic Memory (RaMem), a framework that turns retrieved memory fragments into contextually verifiable evidence. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-22844:end -->

<!-- books-review:SF-2026-ARXIV-2606-22844:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. 披露的 evaluation signal 是：Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22844:end -->

<!-- existing:SF-2026-ARXIV-2606-22864:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22864:end -->

<!-- delta:SF-2026-ARXIV-2606-22864:start -->
When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents 的 exact-v1 机制为：We argue, on a single-backbone cautionary case study (Qwen2.5-VL-7B on Mind2Web, teacher-forced replay), that a high probing AUC on a clean-vs-attack split is not, on its own, evidence of malicious-content detection. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-22864:end -->

<!-- books-review:SF-2026-ARXIV-2606-22864:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We argue, on a single-backbone cautionary case study (Qwen2.5-VL-7B on Mind2Web, teacher-forced replay), that a high probing AUC on a clean-vs-attack split is not, on its own, evidence of malicious-content detection. 披露的 evaluation signal 是：Hidden-state probing -- a linear classifier on a frozen vision-language model's internal activations -- has emerged as an attractive evaluation tool for flagging indirect prompt injection (IPI) in multimodal computer-use agents before the agent emits a corrupted action. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22864:end -->

<!-- existing:SF-2026-ARXIV-2606-22873:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22873:end -->

<!-- delta:SF-2026-ARXIV-2606-22873:start -->
SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning 的 exact-v1 机制为：We present \textbf{SingGuard}, a policy-adaptive multimodal guardrail model family for safety assessment in multimodal conversations. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-22873:end -->

<!-- books-review:SF-2026-ARXIV-2606-22873:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. 披露的 evaluation signal 是：We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22873:end -->

<!-- existing:SF-2026-ARXIV-2606-22874:start -->
`books/part-02-model/22-long-context.md` 的唯一 owner 已承载相关机制链；`books/part-02-model/21-moe.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22874:end -->

<!-- delta:SF-2026-ARXIV-2606-22874:start -->
SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers 的 exact-v1 机制为：We present SpotAttention, a lightweight selector that attaches to a frozen pretrained transformer and learns by KL distillation to estimate its attention distribution. 因此 把稀疏选择器、token/KV identity、预算和 dense fallback 纳入请求状态。
<!-- delta:SF-2026-ARXIV-2606-22874:end -->

<!-- books-review:SF-2026-ARXIV-2606-22874:start -->
Unique owner `MODEL-LONG-CONTEXT`; adjacent non-owner `books/part-02-model/21-moe.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Sparse attention cuts these costs by attending only to a relevant subset of past tokens, but selecting that subset is itself expensive. 披露的 evaluation signal 是：Quantizing the selector's K-cache to INT4 or FP4 microscale shrinks it 3.5x at no accuracy cost. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22874:end -->

<!-- existing:SF-2026-ARXIV-2606-22875:start -->
`books/part-06-ai-infrastructure/59-model-registry.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/60-training-operator.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22875:end -->

<!-- delta:SF-2026-ARXIV-2606-22875:start -->
FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs 的 exact-v1 机制为：In this paper, we propose FedOT, the first framework for ownership verification and leakage tracing in federated LDMs. 因此 把 ownership/provenance 证据与 artifact hash、client identity 和泄露追踪绑定。
<!-- delta:SF-2026-ARXIV-2606-22875:end -->

<!-- books-review:SF-2026-ARXIV-2606-22875:start -->
Unique owner `PLATFORM-MODEL-REGISTRY`; adjacent non-owner `books/part-06-ai-infrastructure/60-training-operator.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, FL requires sharing the global model with multiple participants, which risks unauthorized model distribution or resale by malicious clients. 披露的 evaluation signal 是：Extensive experiments demonstrate that FedOT achieves superior performance in both ownership verification and traceability. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22875:end -->

<!-- existing:SF-2026-ARXIV-2606-22877:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22877:end -->

<!-- delta:SF-2026-ARXIV-2606-22877:start -->
DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings 的 exact-v1 机制为：Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-22877:end -->

<!-- books-review:SF-2026-ARXIV-2606-22877:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they prefer (preferences), and keep it updated as jobs, routines, and tastes drift. 披露的 evaluation signal 是：Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22877:end -->

<!-- existing:SF-2026-ARXIV-2606-22878:start -->
`books/part-04-training-system/30-lora.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/31-rlhf.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22878:end -->

<!-- delta:SF-2026-ARXIV-2606-22878:start -->
Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning 的 exact-v1 机制为：As large language models (LLMs) are increasingly deployed at the network edge to provide pervasive generative AI services, decentralized federated learning (DFL) provides a vital mechanism for privacy-preserving, domain-specific fine-tuning through peer-to-peer exchanges of parameter-efficient updates. 因此 把参与者加入/退出、LoRA contribution coordinate、unlearning correction 与通信预算版本化。
<!-- delta:SF-2026-ARXIV-2606-22878:end -->

<!-- books-review:SF-2026-ARXIV-2606-22878:start -->
Unique owner `TRAIN-LORA`; adjacent non-owner `books/part-04-training-system/31-rlhf.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, the dynamic nature of practical decentralized edge networks, where devices may dynamically join or leave the collaborative training process, requires the system to continuously adapt to new data while selectively removing prior contributions. 披露的 evaluation signal 是：To address this challenge, we propose a priority-aware learning-unlearning correction framework based on orthogonal LoRA that can enhance the knowledge evaluation through topology adjustment. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22878:end -->

<!-- existing:SF-2026-ARXIV-2606-22883:start -->
`books/part-04-training-system/27-data.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/28-pretraining.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22883:end -->

<!-- delta:SF-2026-ARXIV-2606-22883:start -->
CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents 的 exact-v1 机制为：To overcome this, we introduce CLI-Universe, a principled synthesis engine that constructs terminal-agent tasks. 因此 把任务/样本生成、可执行验证、过滤与训练 lineage 绑定。
<!-- delta:SF-2026-ARXIV-2606-22883:end -->

<!-- books-review:SF-2026-ARXIV-2606-22883:start -->
Unique owner `TRAIN-DATA`; adjacent non-owner `books/part-04-training-system/28-pretraining.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck. 披露的 evaluation signal 是：Remarkably, fine-tuning Qwen3-32B on CLI-Universe-6K achieves 33.4% on Terminal-Bench 2.0. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22883:end -->

<!-- existing:SF-2026-ARXIV-2606-22902:start -->
`books/part-07-agent/84-agent-platform.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22902:end -->

<!-- delta:SF-2026-ARXIV-2606-22902:start -->
Agent-as-a-Router: Agentic Model Routing for Coding Tasks 的 exact-v1 机制为：Motivated by this finding, we propose Agent-as-a-Router, a framework that formalizes routing as a C-A-F loop (Context-&gt;Action-&gt;Feedback-&gt;Context). 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。
<!-- delta:SF-2026-ARXIV-2606-22902:end -->

<!-- books-review:SF-2026-ARXIV-2606-22902:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Consequently, routing each task to the most suitable model becomes critical for both performance and cost. 披露的 evaluation signal 是：We instantiate this framework as ACRouter, composed of an Orchestrator, a Verifier, a Memory module, and introduce CodeRouterBench, an evaluation environment comprising ~10K task instances with verified scores from 8 frontier LLMs, enabling regret-based router comparison on streaming tasks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22902:end -->

<!-- existing:SF-2026-ARXIV-2606-22906:start -->
`books/part-07-agent/75-context.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/76-rag.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22906:end -->

<!-- delta:SF-2026-ARXIV-2606-22906:start -->
From Fragments to Paths: Task-Level Context Recovery for Large Industrial Codebases 的 exact-v1 机制为：We present DeepDiscovery, a task-level repository-understanding method for large industrial codebases. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。
<!-- delta:SF-2026-ARXIV-2606-22906:end -->

<!-- books-review:SF-2026-ARXIV-2606-22906:start -->
Unique owner `AGENT-CONTEXT`; adjacent non-owner `books/part-07-agent/76-rag.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Existing methods often retrieve only local fragments and fail to recover the broader task-relevant context needed for complex repository-level tasks. 披露的 evaluation signal 是：Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22906:end -->

<!-- existing:SF-2026-ARXIV-2606-22916:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22916:end -->

<!-- delta:SF-2026-ARXIV-2606-22916:start -->
Intent-Governed Tool Authorization for AI Agents 的 exact-v1 机制为：We present Intent-Governed Access Control (IGAC), a server-side authorization layer that converts a trusted request into a short-lived intent certificate, narrows the statically authorized tool manifest, and checks proposed tool and payload effects before execution. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-22916:end -->

<!-- books-review:SF-2026-ARXIV-2606-22916:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：A trace-backed normalizer counterfactual removes this residual authority at substantial utility cost. 披露的 evaluation signal 是：We evaluate a reusable IGAC path over an OpenPort governance substrate using endpoint tests, 176 runtime-backed synthetic tasks, real-model classifier and planner pilots, 306 end-to-end model-task runtime trials, and a 36-trial benchmark-shaped external subset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22916:end -->

<!-- existing:SF-2026-ARXIV-2606-22918:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22918:end -->

<!-- delta:SF-2026-ARXIV-2606-22918:start -->
Each Judge Its Own Yardstick: Discovering Per-VLM Taxonomies for Physical Video Evaluation 的 exact-v1 机制为：We propose JudgeFit, an iterative refinement procedure that discovers a per-VLM evaluation taxonomy. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-22918:end -->

<!-- books-review:SF-2026-ARXIV-2606-22918:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Maintaining physical consistency in video generators and world models increasingly relies on vision-language models (VLMs) as automated judges that provide reward signals, ranking decisions, and data-filtering criteria. 披露的 evaluation signal 是：A single global evaluation schema therefore gives every VLM the same axes of competence, regardless of what each can actually perceive. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22918:end -->

<!-- existing:SF-2026-ARXIV-2606-22925:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22925:end -->

<!-- delta:SF-2026-ARXIV-2606-22925:start -->
EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction 的 exact-v1 机制为：Using this methodology, we release a community-reviewed EEG benchmark corpus centered on 53 completed and reviewed entries with 245 task definitions spanning diverse paradigms, and we introduce NeuroDoc and NeuroAudit as the operational support layer for rulebook-guided drafting, upgrading, review, amendment, and release management. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-22925:end -->

<!-- books-review:SF-2026-ARXIV-2606-22925:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. 披露的 evaluation signal 是：Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22925:end -->

<!-- existing:SF-2026-ARXIV-2606-22932:start -->
`books/part-04-training-system/36-distributed-training.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/37-tensor-parallel.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22932:end -->

<!-- delta:SF-2026-ARXIV-2606-22932:start -->
FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training 的 exact-v1 机制为：This two-phase schedule sets the memory ceiling of modern training: at the seam between the phases, every layer's gradient is live at once. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。
<!-- delta:SF-2026-ARXIV-2606-22932:end -->

<!-- books-review:SF-2026-ARXIV-2606-22932:start -->
Unique owner `TRAIN-DISTRIBUTED-TRAINING`; adjacent non-owner `books/part-04-training-system/37-tensor-parallel.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. 披露的 evaluation signal 是：Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22932:end -->

<!-- existing:SF-2026-ARXIV-2606-22936:start -->
`books/part-07-agent/79-planning.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/80-reflection.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22936:end -->

<!-- delta:SF-2026-ARXIV-2606-22936:start -->
When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents 的 exact-v1 机制为：We call this premature commitment. 因此 把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state。
<!-- delta:SF-2026-ARXIV-2606-22936:end -->

<!-- books-review:SF-2026-ARXIV-2606-22936:start -->
Unique owner `AGENT-PLANNING`; adjacent non-owner `books/part-07-agent/80-reflection.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Long-horizon LLM agents can fail quietly: they settle on one reading of the evidence early, then spend the rest of the run defending it. 披露的 evaluation signal 是：The result is a diagnostic for a hidden process failure, with clear limits rather than a general accuracy lever. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22936:end -->

<!-- existing:SF-2026-ARXIV-2606-22942:start -->
`books/part-04-training-system/29-sft.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/30-lora.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22942:end -->

<!-- delta:SF-2026-ARXIV-2606-22942:start -->
Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails 的 exact-v1 机制为：Knowledge Distillation (KD) offers a practical solution by transferring knowledge from a teacher model of a larger size to a smaller student model. 因此 把蒸馏 teacher/student、样本选择与失效区间保留在训练 lineage。
<!-- delta:SF-2026-ARXIV-2606-22942:end -->

<!-- books-review:SF-2026-ARXIV-2606-22942:start -->
Unique owner `TRAIN-SFT`; adjacent non-owner `books/part-04-training-system/30-lora.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. 披露的 evaluation signal 是：Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22942:end -->

<!-- existing:SF-2026-ARXIV-2606-22948:start -->
`books/part-07-agent/79-planning.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/80-reflection.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22948:end -->

<!-- delta:SF-2026-ARXIV-2606-22948:start -->
ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents 的 exact-v1 机制为：We propose Environment-Native Verified Search (ENVS), a training-time search-and-filter pipeline that uses the environment to construct verified supervision before policy optimization: it branches over behaviorally distinct GUI actions in live OSWorld VMs, verifies successful leaves, and trains from globally balanced step-level supervision. 因此 把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state。
<!-- delta:SF-2026-ARXIV-2606-22948:end -->

<!-- books-review:SF-2026-ARXIV-2606-22948:start -->
Unique owner `AGENT-PLANNING`; adjacent non-owner `books/part-07-agent/80-reflection.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：As multimodal agents move from interface understanding to real software control, successful trajectory discovery in live desktop environments becomes a key challenge. 披露的 evaluation signal 是：To evaluate robustness under realistic desktop interruptions, we also introduce OSWorld-Noisy, a dynamic benchmark for recoverable desktop interruptions that preserves the original tasks while testing whether agents can refocus, dismiss, wait, or recover under live perturbations. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22948:end -->

<!-- existing:SF-2026-ARXIV-2606-22953:start -->
`books/part-07-agent/75-context.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/76-rag.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22953:end -->

<!-- delta:SF-2026-ARXIV-2606-22953:start -->
Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents 的 exact-v1 机制为：We introduce replay pairing, a diagnostic that runs the same trajectory with and without the plan in history and measures hidden-state cosine distance. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。
<!-- delta:SF-2026-ARXIV-2606-22953:end -->

<!-- books-review:SF-2026-ARXIV-2606-22953:start -->
Unique owner `AGENT-CONTEXT`; adjacent non-owner `books/part-07-agent/76-rag.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 披露的 evaluation signal 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22953:end -->

<!-- existing:SF-2026-ARXIV-2606-22966:start -->
`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22966:end -->

<!-- delta:SF-2026-ARXIV-2606-22966:start -->
Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models 的 exact-v1 机制为：A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。
<!-- delta:SF-2026-ARXIV-2606-22966:end -->

<!-- books-review:SF-2026-ARXIV-2606-22966:start -->
Unique owner `MULTIMODAL-WORLD-MODELS`; adjacent non-owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. 披露的 evaluation signal 是：We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22966:end -->

<!-- existing:SF-2026-ARXIV-2606-22968:start -->
`books/part-05-inference-system/43-prefill.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/44-decode.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22968:end -->

<!-- delta:SF-2026-ARXIV-2606-22968:start -->
MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference 的 exact-v1 机制为：To address these challenges, we present MOCAP, a memory-orchestrated chunked pipelining framework for prefill-only LLM inference on WSCs. 因此 把 wafer-scale memory orchestration、chunk pipeline 与 prefill-only 边界显式化。
<!-- delta:SF-2026-ARXIV-2606-22968:end -->

<!-- books-review:SF-2026-ARXIV-2606-22968:start -->
Unique owner `INFER-PREFILL`; adjacent non-owner `books/part-05-inference-system/44-decode.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：For long-context prefill, communication overhead grows with sequence length and quickly becomes a bottleneck on conventional GPU systems, making wafer-scale chips (WSCs) a promising substrate due to their high communication bandwidth and large aggregate compute and memory capacity. 披露的 evaluation signal 是：It further incorporates Latency-Balanced Chunk Partitioning (LBCP) to balance chunk execution cost under both attention-cost growth and KV reallocation overhead, improving pipeline efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22968:end -->

<!-- existing:SF-2026-ARXIV-2606-22977:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22977:end -->

<!-- delta:SF-2026-ARXIV-2606-22977:start -->
StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs 的 exact-v1 机制为：To bridge this gap, we introduce StatABench (Statistical AnalysisBenchmark), a benchmark designed to systematically assess LLMs' statistical analysis capabilities. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-22977:end -->

<!-- books-review:SF-2026-ARXIV-2606-22977:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. 披露的 evaluation signal 是：While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22977:end -->

<!-- existing:SF-2026-ARXIV-2606-22983:start -->
`books/part-05-inference-system/56-inference-scheduling.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-22983:end -->

<!-- delta:SF-2026-ARXIV-2606-22983:start -->
LiveServe: Interaction-Aware Serving for Real-Time Omni-Modal LLMs 的 exact-v1 机制为：LiveServe is an interaction-aware serving system for realtime Omni-LM interaction. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。
<!-- delta:SF-2026-ARXIV-2606-22983:end -->

<!-- books-review:SF-2026-ARXIV-2606-22983:start -->
Unique owner `INFER-SCHEDULING`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely. 披露的 evaluation signal 是：On vLLM-Omni, LiveServe improves realtime serving across two Omni-LMs and mixed workloads. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-22983:end -->

<!-- existing:SF-2026-ARXIV-2606-23001:start -->
`books/part-05-inference-system/54-gpu-memory.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23001:end -->

<!-- delta:SF-2026-ARXIV-2606-23001:start -->
EnerInfer: Energy-Aware On-Device LLM Inference 的 exact-v1 机制为：To address these challenges, we propose EnerInfer, the first on-device LLM inference framework that jointly manages energy efficiency, throughput, and thermal comfort for LLM workloads. 因此 把设备频率、功耗/温度估计、QoE 和模型/backend identity 联合验收。
<!-- delta:SF-2026-ARXIV-2606-23001:end -->

<!-- books-review:SF-2026-ARXIV-2606-23001:start -->
Unique owner `INFER-GPU-MEMORY`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：On-device LLM inference is increasingly attractive for privacy-preserving, reliable, and cost-effective deployment, yet its energy and thermal costs remain a critical bottleneck. 披露的 evaluation signal 是：We show instead that on-device LLM inference often has exploitable configuration slack: modestly lowering NPU and memory frequencies preserves quality of experience (QoE) while substantially improving energy efficiency and reducing heat. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23001:end -->

<!-- existing:SF-2026-ARXIV-2606-23003:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23003:end -->

<!-- delta:SF-2026-ARXIV-2606-23003:start -->
VCT: A Verifiable Transcript System for LLM Conversations 的 exact-v1 机制为：However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23003:end -->

<!-- books-review:SF-2026-ARXIV-2606-23003:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 披露的 evaluation signal 是：Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23003:end -->

<!-- existing:SF-2026-ARXIV-2606-23017:start -->
`books/part-04-training-system/36-distributed-training.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/37-tensor-parallel.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23017:end -->

<!-- delta:SF-2026-ARXIV-2606-23017:start -->
Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems 的 exact-v1 机制为：Federated Learning (FL) enables privacy-preserving collaborative learning for Internet of Vehicles (IoV) scenarios, but extreme heterogeneity of vehicular-edge-cloud resources severely limits system efficiency. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。
<!-- delta:SF-2026-ARXIV-2606-23017:end -->

<!-- books-review:SF-2026-ARXIV-2606-23017:start -->
Unique owner `TRAIN-DISTRIBUTED-TRAINING`; adjacent non-owner `books/part-04-training-system/37-tensor-parallel.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Dynamic scheduling strategies mitigate this issue but introduce new trust concerns: verifying fair scheduling decisions and faithful client execution of compression instructions without privacy leakage remains an open challenge. 披露的 evaluation signal 是：First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23017:end -->

<!-- existing:SF-2026-ARXIV-2606-23026:start -->
`books/part-07-agent/84-agent-platform.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23026:end -->

<!-- delta:SF-2026-ARXIV-2606-23026:start -->
A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees 的 exact-v1 机制为：The theoretical results are conditional and the experiments do not estimate their regret or transfer constants; consequently, the evidence establishes a promising repaired operating point, not a certified real-system equilibrium. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。
<!-- delta:SF-2026-ARXIV-2606-23026:end -->

<!-- books-review:SF-2026-ARXIV-2606-23026:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We formulate resource governance as a contextual Stackelberg game: a controller commits to a quality target and a cost incentive, while an executor responds with resource actions over context, prompting, and tool usage. 披露的 evaluation signal 是：We learn a conditional response model, optimize a leader policy against that model, and repair the resulting policy using real-API calibration and projection onto an empirically selected action set. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23026:end -->

<!-- existing:SF-2026-ARXIV-2606-23030:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23030:end -->

<!-- delta:SF-2026-ARXIV-2606-23030:start -->
Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models 的 exact-v1 机制为：Motivated by this question, we propose entity-level membership inference, which determines whether information related to a target entity is used in LLM training. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23030:end -->

<!-- books-review:SF-2026-ARXIV-2606-23030:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Membership inference is a key tool for assessing such risks, but existing studies mainly focus on whether specific samples or sample-based data units are used for training. 披露的 evaluation signal 是：We argue that LLMs exhibit a human-memory-like behavior: an LLM may not memorize a specific sample verbatim, yet it can accumulate and reveal knowledge about a real-world entity from scattered mentions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23030:end -->

<!-- existing:SF-2026-ARXIV-2606-23038:start -->
`books/part-04-training-system/31-rlhf.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/32-ppo.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23038:end -->

<!-- delta:SF-2026-ARXIV-2606-23038:start -->
EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning 的 exact-v1 机制为：We propose EvoRubrics, a co-evolutionary RL framework where a Policy LLM and a Rubric Generator jointly improve through adversarial interaction within each training step. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。
<!-- delta:SF-2026-ARXIV-2606-23038:end -->

<!-- books-review:SF-2026-ARXIV-2606-23038:start -->
Unique owner `TRAIN-RLHF`; adjacent non-owner `books/part-04-training-system/32-ppo.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 披露的 evaluation signal 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23038:end -->

<!-- existing:SF-2026-ARXIV-2606-23049:start -->
`books/part-07-agent/78-tool-calling.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/79-planning.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23049:end -->

<!-- delta:SF-2026-ARXIV-2606-23049:start -->
PhoneBuddy: Training Open Models for Agentic Phone Use 的 exact-v1 机制为：We present PhoneBuddy, a training recipe and open-model line for agentic phone use that combines a real-app environment with a mock-app environment, PhoneWorld, which reconstructs runnable mock apps from real GUI usage structure. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。
<!-- delta:SF-2026-ARXIV-2606-23049:end -->

<!-- books-review:SF-2026-ARXIV-2606-23049:start -->
Unique owner `AGENT-TOOL-CALLING`; adjacent non-owner `books/part-07-agent/79-planning.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：The gains are strongest on app and mini-app tasks, while long-horizontal cross-app workflows remain an important open challenge. 披露的 evaluation signal 是：Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23049:end -->

<!-- existing:SF-2026-ARXIV-2606-23075:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23075:end -->

<!-- delta:SF-2026-ARXIV-2606-23075:start -->
Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies 的 exact-v1 机制为：We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23075:end -->

<!-- books-review:SF-2026-ARXIV-2606-23075:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Self-evolving LLM agent systems, which autonomously update their model parameters, memory, tools, and architectures, introduce a qualitatively new threat landscape in which adversarial influences become permanently encoded, self-amplify across generations, and propagate through populations without sustained attacker access. 披露的 evaluation signal 是：We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23075:end -->

<!-- existing:SF-2026-ARXIV-2606-23112:start -->
`books/part-07-agent/78-tool-calling.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/79-planning.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23112:end -->

<!-- delta:SF-2026-ARXIV-2606-23112:start -->
Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning 的 exact-v1 机制为：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。
<!-- delta:SF-2026-ARXIV-2606-23112:end -->

<!-- books-review:SF-2026-ARXIV-2606-23112:start -->
Unique owner `AGENT-TOOL-CALLING`; adjacent non-owner `books/part-07-agent/79-planning.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 披露的 evaluation signal 是：For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23112:end -->

<!-- existing:SF-2026-ARXIV-2606-23127:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23127:end -->

<!-- delta:SF-2026-ARXIV-2606-23127:start -->
Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation 的 exact-v1 机制为：We introduce AFTER, a benchmark of 382 realistic enterprise tasks spanning six professional roles and 22 procedural skills, designed to evaluate how skills transfer across tasks, roles, and model backbones. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-23127:end -->

<!-- books-review:SF-2026-ARXIV-2606-23127:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. 披露的 evaluation signal 是：Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23127:end -->

<!-- existing:SF-2026-ARXIV-2606-23130:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23130:end -->

<!-- delta:SF-2026-ARXIV-2606-23130:start -->
Understanding the (In)Security of Vibe-Coded Applications 的 exact-v1 机制为：We collect a large corpus of real-world applications developed using popular AI agents and design a vulnerability analysis framework that combines agent-assisted code auditing with human validation. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23130:end -->

<!-- books-review:SF-2026-ARXIV-2606-23130:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We collect a large corpus of real-world applications developed using popular AI agents and design a vulnerability analysis framework that combines agent-assisted code auditing with human validation. 披露的 evaluation signal 是：Our study reveals several key findings: (1) vibe-coded applications exhibit recurring vulnerability patterns that differ from those commonly observed in conventional software development workflows, including placeholder logic, unfiltered input, and secret exposure; (2) these vulnerabilities arise from systematic limitations of AI agents throughout the vibe-coding lifecycle, such as memory loss, locally optimized objectives and insufficient security knowledge; and (3) while advances in LLM capabilities and improved prompting strategies can reduce the inci 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23130:end -->

<!-- existing:SF-2026-ARXIV-2606-23181:start -->
`books/part-05-inference-system/56-inference-scheduling.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23181:end -->

<!-- delta:SF-2026-ARXIV-2606-23181:start -->
DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models 的 exact-v1 机制为：We introduce DART, a training-free routing framework that samples two cheap no-think drafts, accepts direct answering when the drafts agree, and predicts a thinking budget from draft entropy when they disagree. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。
<!-- delta:SF-2026-ARXIV-2606-23181:end -->

<!-- books-review:SF-2026-ARXIV-2606-23181:start -->
Unique owner `INFER-SCHEDULING`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Hybrid reasoning models can answer directly or spend extra tokens on extended thinking. 披露的 evaluation signal 是：Across the main comparisons, DART preserves or improves always-thinking accuracy in most settings while reducing thinking-token use. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23181:end -->

<!-- existing:SF-2026-ARXIV-2606-23189:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23189:end -->

<!-- delta:SF-2026-ARXIV-2606-23189:start -->
Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? 的 exact-v1 机制为：Hence, we introduce AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23189:end -->

<!-- books-review:SF-2026-ARXIV-2606-23189:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：This cross-application access is useful, but it also creates a privacy risk that has been largely overlooked: when an agent works in one context, it can pull in information from another that is inappropriate in that context. 披露的 evaluation signal 是：Hence, we introduce AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23189:end -->

<!-- existing:SF-2026-ARXIV-2606-23195:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23195:end -->

<!-- delta:SF-2026-ARXIV-2606-23195:start -->
Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory 的 exact-v1 机制为：Recent work shows that agent memories degrade during continuous consolidation. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-23195:end -->

<!-- books-review:SF-2026-ARXIV-2606-23195:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, existing research assumes memories are derived from unbiased experiences. 披露的 evaluation signal 是：Recent work shows that agent memories degrade during continuous consolidation. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23195:end -->

<!-- existing:SF-2026-ARXIV-2606-23217:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23217:end -->

<!-- delta:SF-2026-ARXIV-2606-23217:start -->
MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations 的 exact-v1 机制为：We introduce MuPPET (Multi-Party Privacy Exposure Testing), a benchmark for contextual privacy in multi-party conversations. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23217:end -->

<!-- books-review:SF-2026-ARXIV-2606-23217:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：This risk is structurally harder to control than in one-to-one settings, as every piece of private information must be appropriate for every recipient in the group. 披露的 evaluation signal 是：Our experiments show that models leak substantially more in multi-party settings than one-to-one evaluations suggest. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23217:end -->

<!-- existing:SF-2026-ARXIV-2606-23276:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23276:end -->

<!-- delta:SF-2026-ARXIV-2606-23276:start -->
Exposing the Illusion of Erasure in Knowledge Editing for LLMs 的 exact-v1 机制为：In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23276:end -->

<!-- books-review:SF-2026-ARXIV-2606-23276:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Knowledge Editing (KE) has emerged as a frontier for updating specific facts in LLMs without costly retraining, but its reliability and underlying mechanisms remain poorly understood. 披露的 evaluation signal 是：In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23276:end -->

<!-- existing:SF-2026-ARXIV-2606-23277:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23277:end -->

<!-- delta:SF-2026-ARXIV-2606-23277:start -->
GIF: Locally Sound Geometric Information Flow Control for LLMs 的 exact-v1 机制为：We present Geometric Information Flow (GIF), a semantic framework for tracking information flow from input tokens to outputs. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23277:end -->

<!-- books-review:SF-2026-ARXIV-2606-23277:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. 披露的 evaluation signal 是：Recent Information Flow Control (IFC)-based defenses show promise but lack a principled semantic foundation for reasoning about information flow through the model itself. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23277:end -->

<!-- existing:SF-2026-ARXIV-2606-23283:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23283:end -->

<!-- delta:SF-2026-ARXIV-2606-23283:start -->
Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs 的 exact-v1 机制为：Motivated by this challenge, we introduce root memory, a structured, decision-preserving representation that distills reusable personalized logic from long-term user histories. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-23283:end -->

<!-- books-review:SF-2026-ARXIV-2606-23283:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap. 披露的 evaluation signal 是：Current benchmarks remain inadequate for evaluating this problem. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23283:end -->

<!-- existing:SF-2026-ARXIV-2606-23321:start -->
`books/part-07-agent/84-agent-platform.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23321:end -->

<!-- delta:SF-2026-ARXIV-2606-23321:start -->
Tmax: A simple recipe for terminal agents 的 exact-v1 机制为：We present Tmax, the strongest open RL recipe for terminal agents to date, bringing open data recipes closer to the frontier. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。
<!-- delta:SF-2026-ARXIV-2606-23321:end -->

<!-- books-review:SF-2026-ARXIV-2606-23321:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Terminal-using agents have quickly become the most popular downstream application of language models (LMs). 披露的 evaluation signal 是：While simple, our recipe achieves 27\% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger models from prior work. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23321:end -->

<!-- existing:SF-2026-ARXIV-2606-23370:start -->
`books/part-05-inference-system/56-inference-scheduling.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23370:end -->

<!-- delta:SF-2026-ARXIV-2606-23370:start -->
FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation 的 exact-v1 机制为：To address these challenges, this paper presents FlexServe, a fast and secure LLM inference system for mobile devices. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。
<!-- delta:SF-2026-ARXIV-2606-23370:end -->

<!-- books-review:SF-2026-ARXIV-2606-23370:start -->
Unique owner `INFER-SCHEDULING`; adjacent non-owner `books/part-05-inference-system/55-pd-disaggregation.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：During LLM inference, both the model weights and the user data are valuable, and attackers may compromise the OS kernel to steal them. 披露的 evaluation signal 是：The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23370:end -->

<!-- existing:SF-2026-ARXIV-2606-23403:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23403:end -->

<!-- delta:SF-2026-ARXIV-2606-23403:start -->
Litmus: Zero-Label, Code-Driven Metric Specification for Evaluating AI Systems 的 exact-v1 机制为：Without a clear account of what a system is expected to do, how it can fail, and which failures matter, metric choices become difficult to justify, interpret, or validate. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23403:end -->

<!-- books-review:SF-2026-ARXIV-2606-23403:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：The challenge is not only that individual metrics may be unreliable, but that evaluation goals are often left implicit. 披露的 evaluation signal 是：As agentic LLM systems move from prototypes to deployment across increasingly diverse domains, evaluating them has become both more important and more difficult. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23403:end -->

<!-- existing:SF-2026-ARXIV-2606-23404:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23404:end -->

<!-- delta:SF-2026-ARXIV-2606-23404:start -->
ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models 的 exact-v1 机制为：To address this, we present ReasoningLens, an open-source framework designed for the hierarchical visualization and diagnostic auditing of complex reasoning chains. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23404:end -->

<!-- books-review:SF-2026-ARXIV-2606-23404:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：The emergence of Large Reasoning Models has introduced exceptionally long Chain-of-Thought traces, creating a transparency burden where critical logic is often buried under massive procedural text. 披露的 evaluation signal 是：ReasoningLens addresses information necropsy by: (1) structuring traces into interactive hierarchies that separate high-level strategy from low-level execution; (2) leveraging an agentic auditor for automated error detection and tool-augmented verification; and (3) synthesizing systemic reasoning profiles to reveal model-specific blind spots. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23404:end -->

<!-- existing:SF-2026-ARXIV-2606-23416:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23416:end -->

<!-- delta:SF-2026-ARXIV-2606-23416:start -->
Detecting Malicious Agent Skills in the Wild using Attention 的 exact-v1 机制为：We present Locate-and-Judge, a two-stage detector designed for this regime. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23416:end -->

<!-- books-review:SF-2026-ARXIV-2606-23416:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. 披露的 evaluation signal 是：We release the resulting labeled dataset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23416:end -->

<!-- existing:SF-2026-ARXIV-2606-23449:start -->
`books/part-07-agent/84-agent-platform.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23449:end -->

<!-- delta:SF-2026-ARXIV-2606-23449:start -->
AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction 的 exact-v1 机制为：We present AOHP (Android Open Harness Project), an OS-level agent harness built on the Android Open Source Project (AOSP). 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。
<!-- delta:SF-2026-ARXIV-2606-23449:end -->

<!-- books-review:SF-2026-ARXIV-2606-23449:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. 披露的 evaluation signal 是：Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23449:end -->

<!-- existing:SF-2026-ARXIV-2606-23459:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23459:end -->

<!-- delta:SF-2026-ARXIV-2606-23459:start -->
TriggerBench: Investigating Prospective Memory for Large Language Models 的 exact-v1 机制为：We introduce TriggerBench, a comprehensive PM benchmark spanning five dimensions across both daily assistants and professional workflows. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-23459:end -->

<!-- books-review:SF-2026-ARXIV-2606-23459:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Furthermore, PM accuracy degrades substantially under implicit constraints or triggers overloaded by concurrent user requests, indicating that robust PM remains an open challenge. 披露的 evaluation signal 是：While Large Language Models (LLMs) are increasingly deployed in long interactions, existing evaluations focus predominantly on retrospective memory (RM) via explicit queries. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23459:end -->

<!-- existing:SF-2026-ARXIV-2606-23521:start -->
`books/part-05-inference-system/44-decode.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23521:end -->

<!-- delta:SF-2026-ARXIV-2606-23521:start -->
Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference 的 exact-v1 机制为：We present Concordia, a runtime that uses a device-resident persistent kernel as the substrate for fault-tolerant LLM inference. 因此 把 persistent-kernel checkpoint、恢复位置和重复 token/side-effect 防护绑定。
<!-- delta:SF-2026-ARXIV-2606-23521:end -->

<!-- books-review:SF-2026-ARXIV-2606-23521:start -->
Unique owner `INFER-DECODE`; adjacent non-owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component. 披露的 evaluation signal 是：The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23521:end -->

<!-- existing:SF-2026-ARXIV-2606-23525:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23525:end -->

<!-- delta:SF-2026-ARXIV-2606-23525:start -->
Self-Compacting Language Model Agents 的 exact-v1 机制为：We propose SelfCompact, a scaffold that allows the model itself to decide when and how to compact. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-23525:end -->

<!-- books-review:SF-2026-ARXIV-2606-23525:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 披露的 evaluation signal 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23525:end -->

<!-- existing:SF-2026-ARXIV-2606-23546:start -->
`books/part-06-ai-infrastructure/70-cost.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/71-multi-tenant.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23546:end -->

<!-- delta:SF-2026-ARXIV-2606-23546:start -->
The Energy Consumption of Transformer Fine-Tuning: A Roofline-Inspired Scaling Model 的 exact-v1 机制为：As training scales in both model size and parallelism, accurately predicting energy consumption has become critical for sustainable and cost-aware system design. 因此 把训练/推理能耗模型、硬件 operating point 与质量边界联合报告。
<!-- delta:SF-2026-ARXIV-2606-23546:end -->

<!-- books-review:SF-2026-ARXIV-2606-23546:start -->
Unique owner `PLATFORM-COST`; adjacent non-owner `books/part-06-ai-infrastructure/71-multi-tenant.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Transformer-based models underpin modern natural language processing but incur rapidly growing computational and energy costs. 披露的 evaluation signal 是：We derive a scaling law model that accurately predicts training energy across heterogeneous configurations. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23546:end -->

<!-- existing:SF-2026-ARXIV-2606-23581:start -->
`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23581:end -->

<!-- delta:SF-2026-ARXIV-2606-23581:start -->
Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse 的 exact-v1 机制为：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。
<!-- delta:SF-2026-ARXIV-2606-23581:end -->

<!-- books-review:SF-2026-ARXIV-2606-23581:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. 披露的 evaluation signal 是：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23581:end -->

<!-- existing:SF-2026-ARXIV-2606-23583:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23583:end -->

<!-- delta:SF-2026-ARXIV-2606-23583:start -->
Evaluation Awareness Is Not One Capability: Evidence from Open Language Models 的 exact-v1 机制为：This opens a gap between benchmark performance and deployment behavior: compliance measured under test conditions becomes an optimistic upper bound that overstates how safely a model behaves once the evaluation harness is removed. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23583:end -->

<!-- books-review:SF-2026-ARXIV-2606-23583:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. 披露的 evaluation signal 是：Safety benchmarks assume that test-condition behavior predicts deployment behavior, an assumption that fails if models detect evaluation cues and adapt. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23583:end -->

<!-- existing:SF-2026-ARXIV-2606-23589:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23589:end -->

<!-- delta:SF-2026-ARXIV-2606-23589:start -->
KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies 的 exact-v1 机制为：In this work, we propose propose KEMO, a lightweight plug-in memory framework that automatically selectively preserves keyframes associated with task-relevant state changes for VLA policies. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-23589:end -->

<!-- books-review:SF-2026-ARXIV-2606-23589:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. 披露的 evaluation signal 是：We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23589:end -->

<!-- existing:SF-2026-ARXIV-2606-23617:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23617:end -->

<!-- delta:SF-2026-ARXIV-2606-23617:start -->
RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models 的 exact-v1 机制为：In this paper, we propose an active, continual learning paradigm for VLAs. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-23617:end -->

<!-- books-review:SF-2026-ARXIV-2606-23617:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. 披露的 evaluation signal 是：We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23617:end -->

<!-- existing:SF-2026-ARXIV-2606-23642:start -->
`books/part-07-agent/76-rag.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/77-memory.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23642:end -->

<!-- delta:SF-2026-ARXIV-2606-23642:start -->
Improving Long-Context Retrieval with Multi-Prefix Embedding 的 exact-v1 机制为：We propose Multi-Prefix Embedding (MPE), which partitions a document into chunks separated by EOS tokens, encodes the full sequence in a single causal forward pass, and extracts one embedding at each prefix boundary. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。
<!-- delta:SF-2026-ARXIV-2606-23642:end -->

<!-- books-review:SF-2026-ARXIV-2606-23642:start -->
Unique owner `AGENT-RAG`; adjacent non-owner `books/part-07-agent/77-memory.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Long-context retrieval exposes a tension: single-vector embeddings lose fine-grained detail, while token-level multi-vector methods incur prohibitive storage. 披露的 evaluation signal 是：Experiments on MLDR-en, BrowseComp-Plus, and LongEmbed show that MPE is competitive with or outperforms single-vector, independent-chunk, and multi-vector baselines, while providing a natural source attribution mechanism for locating evidence chunks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23642:end -->

<!-- existing:SF-2026-ARXIV-2606-23654:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23654:end -->

<!-- delta:SF-2026-ARXIV-2606-23654:start -->
EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions 的 exact-v1 机制为：We introduce EnterpriseClawBench, an enterprise agent benchmark constructed from proprietary, real-world agent sessions. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23654:end -->

<!-- books-review:SF-2026-ARXIV-2606-23654:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：These results show that enterprise agent evaluation must report harness--model combinations, artifact delivery, visual quality, cost, runtime, and skill-transfer behavior, rather than collapsing performance into a single score. 披露的 evaluation signal 是：Because the sessions contain internal enterprise content, we do not release the benchmark data; instead, our reusable contribution is the construction and evaluation protocol. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23654:end -->

<!-- existing:SF-2026-ARXIV-2606-23664:start -->
`books/part-07-agent/82-multi-agent.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23664:end -->

<!-- delta:SF-2026-ARXIV-2606-23664:start -->
MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems? 的 exact-v1 机制为：Multi-agent systems (MAS) offer a scalable path forward for agentic AI, comprising multiple LLM-based agents, each assigned a system prompt and a position within a workflow that governs inter-agent coordination and output aggregation. 因此 把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离。
<!-- delta:SF-2026-ARXIV-2606-23664:end -->

<!-- books-review:SF-2026-ARXIV-2606-23664:start -->
Unique owner `AGENT-MULTI-AGENT`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Although prompt optimization has shown substantial potential for single LLMs, extending it to MAS poses distinct challenges, notably an exponentially growing search space. 披露的 evaluation signal 是：System prompts thus form a critical and accessible optimization surface: they specify agents' roles and behaviors, enabling system-level improvements without model finetuning. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23664:end -->

<!-- existing:SF-2026-ARXIV-2606-23671:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23671:end -->

<!-- delta:SF-2026-ARXIV-2606-23671:start -->
Can LLMs Reliably Self-Report Adversarial Prefills, and How? 的 exact-v1 机制为：We extend the question to safety contexts and examine how reliably a model can recognize that its own prior response was elicited by an adversarial prefill attack. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23671:end -->

<!-- books-review:SF-2026-ARXIV-2606-23671:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We extend the question to safety contexts and examine how reliably a model can recognize that its own prior response was elicited by an adversarial prefill attack. 披露的 evaluation signal 是：Prior work shows that large language models (LLMs) exhibit introspective capability on benign tasks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23671:end -->

<!-- existing:SF-2026-ARXIV-2606-23686:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23686:end -->

<!-- delta:SF-2026-ARXIV-2606-23686:start -->
LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models 的 exact-v1 机制为：To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-23686:end -->

<!-- books-review:SF-2026-ARXIV-2606-23686:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. 披露的 evaluation signal 是：We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23686:end -->

<!-- existing:SF-2026-ARXIV-2606-23752:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23752:end -->

<!-- delta:SF-2026-ARXIV-2606-23752:start -->
ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents 的 exact-v1 机制为：Each agent, however, persists its conversation in a private and vendor-specific log. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-23752:end -->

<!-- books-review:SF-2026-ARXIV-2606-23752:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Each agent, however, persists its conversation in a private and vendor-specific log. 披露的 evaluation signal 是：The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23752:end -->

<!-- existing:SF-2026-ARXIV-2606-23754:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23754:end -->

<!-- delta:SF-2026-ARXIV-2606-23754:start -->
Verifiable Foundation Models for Robot Safety 的 exact-v1 机制为：In this paper, we present FEARL (Foundation-Enabled Assured Robot Learning), a framework that addresses this tension through a modular architectural decomposition. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-23754:end -->

<!-- books-review:SF-2026-ARXIV-2606-23754:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Deploying foundation models for robot control raises a central challenge: the expressive power that enables rich, multimodal perception also makes these models opaque and difficult to analyze formally, rendering them intractable for existing verification tools. 披露的 evaluation signal 是：To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23754:end -->

<!-- existing:SF-2026-ARXIV-2606-23768:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23768:end -->

<!-- delta:SF-2026-ARXIV-2606-23768:start -->
Cryptographic certificates of validity for trustworthy AI 的 exact-v1 机制为：We propose cryptographic certificates of validity for agentic AI systems. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23768:end -->

<!-- books-review:SF-2026-ARXIV-2606-23768:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We propose cryptographic certificates of validity for agentic AI systems. 披露的 evaluation signal 是：We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23768:end -->

<!-- existing:SF-2026-ARXIV-2606-23797:start -->
`books/part-07-agent/81-workflow.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23797:end -->

<!-- delta:SF-2026-ARXIV-2606-23797:start -->
From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes 的 exact-v1 机制为：We introduce the Goal-Oriented Dialogue Runtime (GODR), a framework-neutral design pattern that treats goals, task frames, lifecycle state, invalidation rules, and resumption contracts as first-class runtime objects while delegating bounded execution to graph runtimes, agents, tools, or application programming interfaces (APIs). 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。
<!-- delta:SF-2026-ARXIV-2606-23797:end -->

<!-- books-review:SF-2026-ARXIV-2606-23797:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 披露的 evaluation signal 是：The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23797:end -->

<!-- existing:SF-2026-ARXIV-2606-23858:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23858:end -->

<!-- delta:SF-2026-ARXIV-2606-23858:start -->
Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications 的 exact-v1 机制为：We introduce the apothem measure and show how to compute apothem-optimal certifications in a linear number of calls to a NN verifier (oracle) w.r.t. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23858:end -->

<!-- books-review:SF-2026-ARXIV-2606-23858:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：A primary challenge in AI safety is the existence of adversarial examples -- slightly distorted inputs that cause a neural network (NN) to misclassify. 披露的 evaluation signal 是：Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23858:end -->

<!-- existing:SF-2026-ARXIV-2606-23872:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23872:end -->

<!-- delta:SF-2026-ARXIV-2606-23872:start -->
MGI: Member vs Generated Inference 的 exact-v1 机制为：To address MGI, we propose Data Circuit Breaker (DCB), a three-stage method that combines complementary signals from a generative model's autoencoder and latent generator to distinguish training members from generated samples. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23872:end -->

<!-- books-review:SF-2026-ARXIV-2606-23872:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We formalize this challenge as Member vs Generated Inference (MGI): given a sample and a target generative model, infer whether the sample is a true training member or a generated output of that model. 披露的 evaluation signal 是：Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23872:end -->

<!-- existing:SF-2026-ARXIV-2606-23892:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23892:end -->

<!-- delta:SF-2026-ARXIV-2606-23892:start -->
REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs 的 exact-v1 机制为：We introduce REALM, to our knowledge the first unified red-teaming benchmark for physical-world VLMs. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23892:end -->

<!-- books-review:SF-2026-ARXIV-2606-23892:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 披露的 evaluation signal 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23892:end -->

<!-- existing:SF-2026-ARXIV-2606-23915:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23915:end -->

<!-- delta:SF-2026-ARXIV-2606-23915:start -->
Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs 的 exact-v1 机制为：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23915:end -->

<!-- books-review:SF-2026-ARXIV-2606-23915:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. 披露的 evaluation signal 是：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23915:end -->

<!-- existing:SF-2026-ARXIV-2606-23927:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23927:end -->

<!-- delta:SF-2026-ARXIV-2606-23927:start -->
RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems 的 exact-v1 机制为：To address this gap, we introduce RIFT-Bench, a graph representation-driven methodology for dynamic red-teaming that enables unified evaluations across diverse agentic architectures. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23927:end -->

<!-- books-review:SF-2026-ARXIV-2606-23927:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. 披露的 evaluation signal 是：Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23927:end -->

<!-- existing:SF-2026-ARXIV-2606-23937:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23937:end -->

<!-- delta:SF-2026-ARXIV-2606-23937:start -->
When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents 的 exact-v1 机制为：We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23937:end -->

<!-- books-review:SF-2026-ARXIV-2606-23937:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. 披露的 evaluation signal 是：Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23937:end -->

<!-- existing:SF-2026-ARXIV-2606-23961:start -->
`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23961:end -->

<!-- delta:SF-2026-ARXIV-2606-23961:start -->
Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets 的 exact-v1 机制为：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。
<!-- delta:SF-2026-ARXIV-2606-23961:end -->

<!-- books-review:SF-2026-ARXIV-2606-23961:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23961:end -->

<!-- existing:SF-2026-ARXIV-2606-23969:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23969:end -->

<!-- delta:SF-2026-ARXIV-2606-23969:start -->
The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing 的 exact-v1 机制为：Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23969:end -->

<!-- books-review:SF-2026-ARXIV-2606-23969:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 披露的 evaluation signal 是：We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23969:end -->

<!-- existing:SF-2026-ARXIV-2606-23983:start -->
`books/part-07-agent/84-agent-platform.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23983:end -->

<!-- delta:SF-2026-ARXIV-2606-23983:start -->
Maestro Order: A Model-Agnostic Orchestration Harness 的 exact-v1 机制为：We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。
<!-- delta:SF-2026-ARXIV-2606-23983:end -->

<!-- books-review:SF-2026-ARXIV-2606-23983:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 披露的 evaluation signal 是：We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23983:end -->

<!-- existing:SF-2026-ARXIV-2606-23989:start -->
`books/part-07-agent/76-rag.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/77-memory.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23989:end -->

<!-- delta:SF-2026-ARXIV-2606-23989:start -->
Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization 的 exact-v1 机制为：We present CAMS, a Claim-Anchored Multi-document Summarization framework that (i) extracts atomic claims with token-level provenance from every source document, (ii) clusters equivalent claims across documents while flagging inter-source conflicts, (iii) selects a support-aware and salient subset, and (iv) rewrites the selection into a summary in which every sentence is anchored to a support-checked claim that links back to one or more source spans. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。
<!-- delta:SF-2026-ARXIV-2606-23989:end -->

<!-- books-review:SF-2026-ARXIV-2606-23989:start -->
Unique owner `AGENT-RAG`; adjacent non-owner `books/part-07-agent/77-memory.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：End-to-end large language models (LLMs) produce fluent multi-document summaries but remain prone to hallucination, and the attributions they offer are typically coarse (whole documents or passages) and generated post hoc, leaving each summary statement hard to verify. 披露的 evaluation signal 是：We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23989:end -->

<!-- existing:SF-2026-ARXIV-2606-24004:start -->
`books/part-04-training-system/31-rlhf.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/32-ppo.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24004:end -->

<!-- delta:SF-2026-ARXIV-2606-24004:start -->
Towards Spec Learning: Inference-Time Alignment from Preference Pairs 的 exact-v1 机制为：We propose spec learning, a framework that relies on a brief user instruction and a small set of preference judgments. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。
<!-- delta:SF-2026-ARXIV-2606-24004:end -->

<!-- books-review:SF-2026-ARXIV-2606-24004:start -->
Unique owner `TRAIN-RLHF`; adjacent non-owner `books/part-04-training-system/32-ppo.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 披露的 evaluation signal 是：We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24004:end -->

<!-- existing:SF-2026-ARXIV-2606-24020:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24020:end -->

<!-- delta:SF-2026-ARXIV-2606-24020:start -->
You Don't Need to Run Every Eval 的 exact-v1 机制为：Building on this, we design BenchPress: a logit-space rank-2 matrix completion method that recovers held-out scores to within 4.6 points, and a confidence layer that says when each prediction can be trusted. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-24020:end -->

<!-- books-review:SF-2026-ARXIV-2606-24020:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 披露的 evaluation signal 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24020:end -->

<!-- existing:SF-2026-ARXIV-2606-24033:start -->
`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24033:end -->

<!-- delta:SF-2026-ARXIV-2606-24033:start -->
RoPE-Aware Bit Allocation for KV-Cache Quantization 的 exact-v1 机制为：We introduce Block-GTQ, a RoPE-aware bit allocator for key-cache quantization built on TurboQuant-MSE(TQ-MSE). 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。
<!-- delta:SF-2026-ARXIV-2606-24033:end -->

<!-- books-review:SF-2026-ARXIV-2606-24033:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24033:end -->

<!-- existing:SF-2026-ARXIV-2606-24040:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24040:end -->

<!-- delta:SF-2026-ARXIV-2606-24040:start -->
Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo 的 exact-v1 机制为：We propose a version-aware operation layer in which high-level operations such as replace, obsolete, keep-history, rollback, and trace are compiled into MeMo-native primitive calls over sequences and tokens. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-24040:end -->

<!-- books-review:SF-2026-ARXIV-2606-24040:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 披露的 evaluation signal 是：This paper asks how such memories can reduce the need for retraining when knowledge changes. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24040:end -->

<!-- existing:SF-2026-ARXIV-2606-24551:start -->
`books/part-07-agent/78-tool-calling.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/79-planning.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24551:end -->

<!-- delta:SF-2026-ARXIV-2606-24551:start -->
GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents 的 exact-v1 机制为：We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。
<!-- delta:SF-2026-ARXIV-2606-24551:end -->

<!-- books-review:SF-2026-ARXIV-2606-24551:start -->
Unique owner `AGENT-TOOL-CALLING`; adjacent non-owner `books/part-07-agent/79-planning.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 披露的 evaluation signal 是：Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24551:end -->

<!-- existing:SF-2026-ARXIV-2606-24934:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24934:end -->

<!-- delta:SF-2026-ARXIV-2606-24934:start -->
Unprivileged Topology Certificates for Cloud GPU Attestation 的 exact-v1 机制为：We present a software-only attestation primitive for this setting. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-24934:end -->

<!-- books-review:SF-2026-ARXIV-2606-24934:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Cloud GPU tenants receive a model name and a region, but cannot directly inspect the physical accelerator that runs their job. 披露的 evaluation signal 是：A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24934:end -->

<!-- existing:SF-2026-ARXIV-2606-28385:start -->
`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-28385:end -->

<!-- delta:SF-2026-ARXIV-2606-28385:start -->
RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis 的 exact-v1 机制为：We present RoboGaze, a training-free, multi-agent VLM framework that provides structured, interpretable evaluation for generated robot-manipulation videos. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。
<!-- delta:SF-2026-ARXIV-2606-28385:end -->

<!-- books-review:SF-2026-ARXIV-2606-28385:start -->
Unique owner `MULTIMODAL-WORLD-MODELS`; adjacent non-owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 披露的 evaluation signal 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-28385:end -->

<!-- existing:SF-2026-ARXIV-2606-28386:start -->
`books/part-04-training-system/27-data.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/28-pretraining.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-28386:end -->

<!-- delta:SF-2026-ARXIV-2606-28386:start -->
Data Provenance for Image Auto-Regressive Generation 的 exact-v1 机制为：Leveraging this, we present a post-hoc framework that enables the robust detection of such patterns for provenance tracing. 因此 把任务/样本生成、可执行验证、过滤与训练 lineage 绑定。
<!-- delta:SF-2026-ARXIV-2606-28386:end -->

<!-- books-review:SF-2026-ARXIV-2606-28386:start -->
Unique owner `TRAIN-DATA`; adjacent non-owner `books/part-04-training-system/28-pretraining.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 披露的 evaluation signal 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-28386:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260623-COVERAGE-V1 | fresh-context:jun23-v1 | coverage | coverage:SRC-ARXIV:20260623 | — | 586/586 full semantic audit; 122/122 route-negative; denominator 92; closures 494; eight proposed false positives closed | passed |
| SA-20260623-EVIDENCE-V1 | fresh-context:jun23-v1 | evidence | review:SF-2026-ARXIV-2606-22741; review:SF-2026-ARXIV-2606-22768; review:SF-2026-ARXIV-2606-22778; review:SF-2026-ARXIV-2606-22783; review:SF-2026-ARXIV-2606-22792; review:SF-2026-ARXIV-2606-22794; review:SF-2026-ARXIV-2606-22798; review:SF-2026-ARXIV-2606-22804; review:SF-2026-ARXIV-2606-22826; review:SF-2026-ARXIV-2606-22827; review:SF-2026-ARXIV-2606-22840; review:SF-2026-ARXIV-2606-22844; review:SF-2026-ARXIV-2606-22864; review:SF-2026-ARXIV-2606-22873; review:SF-2026-ARXIV-2606-22874; review:SF-2026-ARXIV-2606-22875; review:SF-2026-ARXIV-2606-22877; review:SF-2026-ARXIV-2606-22878; review:SF-2026-ARXIV-2606-22883; review:SF-2026-ARXIV-2606-22902; review:SF-2026-ARXIV-2606-22906; review:SF-2026-ARXIV-2606-22916; review:SF-2026-ARXIV-2606-22918; review:SF-2026-ARXIV-2606-22925; review:SF-2026-ARXIV-2606-22932; review:SF-2026-ARXIV-2606-22936; review:SF-2026-ARXIV-2606-22942; review:SF-2026-ARXIV-2606-22948; review:SF-2026-ARXIV-2606-22953; review:SF-2026-ARXIV-2606-22966; review:SF-2026-ARXIV-2606-22968; review:SF-2026-ARXIV-2606-22977; review:SF-2026-ARXIV-2606-22983; review:SF-2026-ARXIV-2606-23001; review:SF-2026-ARXIV-2606-23003; review:SF-2026-ARXIV-2606-23017; review:SF-2026-ARXIV-2606-23026; review:SF-2026-ARXIV-2606-23030; review:SF-2026-ARXIV-2606-23038; review:SF-2026-ARXIV-2606-23049; review:SF-2026-ARXIV-2606-23075; review:SF-2026-ARXIV-2606-23112; review:SF-2026-ARXIV-2606-23127; review:SF-2026-ARXIV-2606-23130; review:SF-2026-ARXIV-2606-23181; review:SF-2026-ARXIV-2606-23189; review:SF-2026-ARXIV-2606-23195; review:SF-2026-ARXIV-2606-23217; review:SF-2026-ARXIV-2606-23276; review:SF-2026-ARXIV-2606-23277; review:SF-2026-ARXIV-2606-23283; review:SF-2026-ARXIV-2606-23321; review:SF-2026-ARXIV-2606-23370; review:SF-2026-ARXIV-2606-23403; review:SF-2026-ARXIV-2606-23404; review:SF-2026-ARXIV-2606-23416; review:SF-2026-ARXIV-2606-23449; review:SF-2026-ARXIV-2606-23459; review:SF-2026-ARXIV-2606-23521; review:SF-2026-ARXIV-2606-23525; review:SF-2026-ARXIV-2606-23546; review:SF-2026-ARXIV-2606-23581; review:SF-2026-ARXIV-2606-23583; review:SF-2026-ARXIV-2606-23589; review:SF-2026-ARXIV-2606-23617; review:SF-2026-ARXIV-2606-23642; review:SF-2026-ARXIV-2606-23654; review:SF-2026-ARXIV-2606-23664; review:SF-2026-ARXIV-2606-23671; review:SF-2026-ARXIV-2606-23686; review:SF-2026-ARXIV-2606-23752; review:SF-2026-ARXIV-2606-23754; review:SF-2026-ARXIV-2606-23768; review:SF-2026-ARXIV-2606-23797; review:SF-2026-ARXIV-2606-23858; review:SF-2026-ARXIV-2606-23872; review:SF-2026-ARXIV-2606-23892; review:SF-2026-ARXIV-2606-23915; review:SF-2026-ARXIV-2606-23927; review:SF-2026-ARXIV-2606-23937; review:SF-2026-ARXIV-2606-23961; review:SF-2026-ARXIV-2606-23969; review:SF-2026-ARXIV-2606-23983; review:SF-2026-ARXIV-2606-23989; review:SF-2026-ARXIV-2606-24004; review:SF-2026-ARXIV-2606-24020; review:SF-2026-ARXIV-2606-24033; review:SF-2026-ARXIV-2606-24040; review:SF-2026-ARXIV-2606-24551; review:SF-2026-ARXIV-2606-24934; review:SF-2026-ARXIV-2606-28385; review:SF-2026-ARXIV-2606-28386 | — | 92/92 official exact-v1 HTML; 92 unique locator triples; explicit benchmark disclosure or literal Not Disclosed; ordinary pending 0 | passed |
| SA-20260623-SELECTION-V1 | fresh-context:jun23-v1 | deep_analysis_selection | analysis:DA-20260623-DEPENDENCY-GRADED-TRACE; analysis:DA-20260623-FACTORED-GOSSIP; analysis-decision:SF-2026-ARXIV-2606-22778; analysis-decision:SF-2026-ARXIV-2606-22783; analysis-decision:SF-2026-ARXIV-2606-22792; analysis-decision:SF-2026-ARXIV-2606-22794; analysis-decision:SF-2026-ARXIV-2606-22798; analysis-decision:SF-2026-ARXIV-2606-22804; analysis-decision:SF-2026-ARXIV-2606-22826; analysis-decision:SF-2026-ARXIV-2606-22827; analysis-decision:SF-2026-ARXIV-2606-22840; analysis-decision:SF-2026-ARXIV-2606-22844; analysis-decision:SF-2026-ARXIV-2606-22864; analysis-decision:SF-2026-ARXIV-2606-22873; analysis-decision:SF-2026-ARXIV-2606-22874; analysis-decision:SF-2026-ARXIV-2606-22875; analysis-decision:SF-2026-ARXIV-2606-22877; analysis-decision:SF-2026-ARXIV-2606-22878; analysis-decision:SF-2026-ARXIV-2606-22883; analysis-decision:SF-2026-ARXIV-2606-22902; analysis-decision:SF-2026-ARXIV-2606-22906; analysis-decision:SF-2026-ARXIV-2606-22916; analysis-decision:SF-2026-ARXIV-2606-22918; analysis-decision:SF-2026-ARXIV-2606-22925; analysis-decision:SF-2026-ARXIV-2606-22932; analysis-decision:SF-2026-ARXIV-2606-22936; analysis-decision:SF-2026-ARXIV-2606-22942; analysis-decision:SF-2026-ARXIV-2606-22948; analysis-decision:SF-2026-ARXIV-2606-22953; analysis-decision:SF-2026-ARXIV-2606-22966; analysis-decision:SF-2026-ARXIV-2606-22968; analysis-decision:SF-2026-ARXIV-2606-22977; analysis-decision:SF-2026-ARXIV-2606-22983; analysis-decision:SF-2026-ARXIV-2606-23001; analysis:DA-20260623-VERIFIABLE-CONVERSATION-STATE; analysis-decision:SF-2026-ARXIV-2606-23017; analysis-decision:SF-2026-ARXIV-2606-23026; analysis-decision:SF-2026-ARXIV-2606-23030; analysis-decision:SF-2026-ARXIV-2606-23038; analysis-decision:SF-2026-ARXIV-2606-23049; analysis-decision:SF-2026-ARXIV-2606-23075; analysis-decision:SF-2026-ARXIV-2606-23112; analysis-decision:SF-2026-ARXIV-2606-23127; analysis-decision:SF-2026-ARXIV-2606-23130; analysis-decision:SF-2026-ARXIV-2606-23181; analysis-decision:SF-2026-ARXIV-2606-23189; analysis-decision:SF-2026-ARXIV-2606-23195; analysis-decision:SF-2026-ARXIV-2606-23217; analysis-decision:SF-2026-ARXIV-2606-23276; analysis-decision:SF-2026-ARXIV-2606-23277; analysis-decision:SF-2026-ARXIV-2606-23283; analysis-decision:SF-2026-ARXIV-2606-23321; analysis-decision:SF-2026-ARXIV-2606-23370; analysis-decision:SF-2026-ARXIV-2606-23403; analysis-decision:SF-2026-ARXIV-2606-23404; analysis-decision:SF-2026-ARXIV-2606-23416; analysis-decision:SF-2026-ARXIV-2606-23449; analysis-decision:SF-2026-ARXIV-2606-23459; analysis-decision:SF-2026-ARXIV-2606-23521; analysis-decision:SF-2026-ARXIV-2606-23525; analysis-decision:SF-2026-ARXIV-2606-23546; analysis-decision:SF-2026-ARXIV-2606-23581; analysis-decision:SF-2026-ARXIV-2606-23583; analysis-decision:SF-2026-ARXIV-2606-23589; analysis-decision:SF-2026-ARXIV-2606-23617; analysis-decision:SF-2026-ARXIV-2606-23642; analysis-decision:SF-2026-ARXIV-2606-23654; analysis-decision:SF-2026-ARXIV-2606-23664; analysis-decision:SF-2026-ARXIV-2606-23671; analysis-decision:SF-2026-ARXIV-2606-23686; analysis-decision:SF-2026-ARXIV-2606-23752; analysis-decision:SF-2026-ARXIV-2606-23754; analysis-decision:SF-2026-ARXIV-2606-23768; analysis-decision:SF-2026-ARXIV-2606-23797; analysis-decision:SF-2026-ARXIV-2606-23858; analysis-decision:SF-2026-ARXIV-2606-23872; analysis-decision:SF-2026-ARXIV-2606-23892; analysis-decision:SF-2026-ARXIV-2606-23915; analysis-decision:SF-2026-ARXIV-2606-23927; analysis-decision:SF-2026-ARXIV-2606-23937; analysis-decision:SF-2026-ARXIV-2606-23961; analysis-decision:SF-2026-ARXIV-2606-23969; analysis-decision:SF-2026-ARXIV-2606-23983; analysis-decision:SF-2026-ARXIV-2606-23989; analysis-decision:SF-2026-ARXIV-2606-24004; analysis-decision:SF-2026-ARXIV-2606-24020; analysis-decision:SF-2026-ARXIV-2606-24033; analysis-decision:SF-2026-ARXIV-2606-24040; analysis-decision:SF-2026-ARXIV-2606-24551; analysis-decision:SF-2026-ARXIV-2606-24934; analysis-decision:SF-2026-ARXIV-2606-28385; analysis-decision:SF-2026-ARXIV-2606-28386 | — | 92/92 full frontier; 3 selected and 89 not_selected with legal decisions and narrative refs | passed |
| SA-20260623-BOOKS-POSTWRITE-V1 | fresh-context:jun23-postwrite-v1 | books | books-review:SF-2026-ARXIV-2606-22741; books-review:SF-2026-ARXIV-2606-22768; books-review:SF-2026-ARXIV-2606-22778; books-review:SF-2026-ARXIV-2606-22783; books-review:SF-2026-ARXIV-2606-22792; books-review:SF-2026-ARXIV-2606-22794; books-review:SF-2026-ARXIV-2606-22798; books-review:SF-2026-ARXIV-2606-22804; books-review:SF-2026-ARXIV-2606-22826; books-review:SF-2026-ARXIV-2606-22827; books-review:SF-2026-ARXIV-2606-22840; books-review:SF-2026-ARXIV-2606-22844; books-review:SF-2026-ARXIV-2606-22864; books-review:SF-2026-ARXIV-2606-22873; books-review:SF-2026-ARXIV-2606-22874; books-review:SF-2026-ARXIV-2606-22875; books-review:SF-2026-ARXIV-2606-22877; books-review:SF-2026-ARXIV-2606-22878; books-review:SF-2026-ARXIV-2606-22883; books-review:SF-2026-ARXIV-2606-22902; books-review:SF-2026-ARXIV-2606-22906; books-review:SF-2026-ARXIV-2606-22916; books-review:SF-2026-ARXIV-2606-22918; books-review:SF-2026-ARXIV-2606-22925; books-review:SF-2026-ARXIV-2606-22932; books-review:SF-2026-ARXIV-2606-22936; books-review:SF-2026-ARXIV-2606-22942; books-review:SF-2026-ARXIV-2606-22948; books-review:SF-2026-ARXIV-2606-22953; books-review:SF-2026-ARXIV-2606-22966; books-review:SF-2026-ARXIV-2606-22968; books-review:SF-2026-ARXIV-2606-22977; books-review:SF-2026-ARXIV-2606-22983; books-review:SF-2026-ARXIV-2606-23001; books-review:SF-2026-ARXIV-2606-23003; books-review:SF-2026-ARXIV-2606-23017; books-review:SF-2026-ARXIV-2606-23026; books-review:SF-2026-ARXIV-2606-23030; books-review:SF-2026-ARXIV-2606-23038; books-review:SF-2026-ARXIV-2606-23049; books-review:SF-2026-ARXIV-2606-23075; books-review:SF-2026-ARXIV-2606-23112; books-review:SF-2026-ARXIV-2606-23127; books-review:SF-2026-ARXIV-2606-23130; books-review:SF-2026-ARXIV-2606-23181; books-review:SF-2026-ARXIV-2606-23189; books-review:SF-2026-ARXIV-2606-23195; books-review:SF-2026-ARXIV-2606-23217; books-review:SF-2026-ARXIV-2606-23276; books-review:SF-2026-ARXIV-2606-23277; books-review:SF-2026-ARXIV-2606-23283; books-review:SF-2026-ARXIV-2606-23321; books-review:SF-2026-ARXIV-2606-23370; books-review:SF-2026-ARXIV-2606-23403; books-review:SF-2026-ARXIV-2606-23404; books-review:SF-2026-ARXIV-2606-23416; books-review:SF-2026-ARXIV-2606-23449; books-review:SF-2026-ARXIV-2606-23459; books-review:SF-2026-ARXIV-2606-23521; books-review:SF-2026-ARXIV-2606-23525; books-review:SF-2026-ARXIV-2606-23546; books-review:SF-2026-ARXIV-2606-23581; books-review:SF-2026-ARXIV-2606-23583; books-review:SF-2026-ARXIV-2606-23589; books-review:SF-2026-ARXIV-2606-23617; books-review:SF-2026-ARXIV-2606-23642; books-review:SF-2026-ARXIV-2606-23654; books-review:SF-2026-ARXIV-2606-23664; books-review:SF-2026-ARXIV-2606-23671; books-review:SF-2026-ARXIV-2606-23686; books-review:SF-2026-ARXIV-2606-23752; books-review:SF-2026-ARXIV-2606-23754; books-review:SF-2026-ARXIV-2606-23768; books-review:SF-2026-ARXIV-2606-23797; books-review:SF-2026-ARXIV-2606-23858; books-review:SF-2026-ARXIV-2606-23872; books-review:SF-2026-ARXIV-2606-23892; books-review:SF-2026-ARXIV-2606-23915; books-review:SF-2026-ARXIV-2606-23927; books-review:SF-2026-ARXIV-2606-23937; books-review:SF-2026-ARXIV-2606-23961; books-review:SF-2026-ARXIV-2606-23969; books-review:SF-2026-ARXIV-2606-23983; books-review:SF-2026-ARXIV-2606-23989; books-review:SF-2026-ARXIV-2606-24004; books-review:SF-2026-ARXIV-2606-24020; books-review:SF-2026-ARXIV-2606-24033; books-review:SF-2026-ARXIV-2606-24040; books-review:SF-2026-ARXIV-2606-24551; books-review:SF-2026-ARXIV-2606-24934; books-review:SF-2026-ARXIV-2606-28385; books-review:SF-2026-ARXIV-2606-28386 | — | 58/58 Integrate in one expected owner; 34/34 No Change revalidated; exact-v1 Review note and owner/adjacent handoff 92/92; zero unresolved finding | passed |

### Materials and Access

- 92/92 used official arXiv exact-v1 HTML; no mirror or later revision used.
- Ordinary pending locator count: 0.

## 8. Ignored Noise

冻结分母之外的 `494` 条 family-specific closures 仍逐行保存在 `denominator-full-semantic-audit-v1.tsv`；`122/122` route-negative identities 已完整复核，三个 durable false negative 被恢复，八个 proposed-pool false positive 被关闭。Keyword routing 仅辅助 recall，不承担 admission。

## 9. Recommended Action

- Integrate: root wrote 58/58 families into 25 unique owner files; post-write semantic audit passed.
- No Change — Existing Coverage: 34/34 canonical propositions and boundaries were revalidated.
- Post-write fresh audit: 92/92 Passed, zero unresolved finding; Completion Complete.

## 10. Repository Changes

- Added only the 2026-06-23 Daily, date-local source packet and scripts/finalize_june23_v21.py.
- Root serialized shared Books. This lane audited them and changed only date-local files; it did not edit, stage, commit or push Books or docs/LEARNING_STATE.md.

## 11. Open Questions

- 哪些 dependency edges 值得提升为 declared instrumentation，而不是由 full-history 假设推断？
- Factored gossip 的 disagreement 阈值如何进入 checkpoint/admission policy？
- 对话 transcript 的密码学完整性如何与内容真实性、删除权和 retention policy 分层？

## 12. Sources

- Exact-v1 URL、版本身份与访问状态：`../_sources/daily-20260623/exact-v1-access-receipt.json`。
- Method、Evaluation、Limitations 与 benchmark contract：本报告第 3、4 节及 `../_sources/daily-20260623/source-review-receipts-v2.1.json`。
- Coverage 与 denominator：`../_sources/daily-20260623/screening-ledger.json`、`denominator-full-semantic-audit-v1.tsv`。
- 来源角色与 evidence scope：[Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md)。

## 13. Final Status

- Denominator：`586 raw = 92 retained + 494 closures`；route-negative audit `122/122`。
- Evidence / Selection：`92/92` official exact-v1 Reviews、benchmark contracts 与 full-frontier decisions complete；selected units `3`。
- Books：`58 Integrate / 34 No Change — Existing Coverage`；`92/92` post-write fresh audit passed；unresolved findings: `0`。
- Coverage: `Closed`；Evidence: `Passed`；Books: `Passed`；Completion Status: `Complete`。
- 机器 validator 仅证明接口一致；语义真值仍归属于第 7 节及 date-local fresh audits。
