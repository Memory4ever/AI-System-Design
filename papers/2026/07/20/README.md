# Daily Research — 2026-07-20

**Research Date:** 2026-07-20

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-19 09:00:00 ～ 2026-07-20 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **357** 个 identity；全量 title + abstract 筛选后冻结 **62** 个候选与 **295** 个 family-specific closure，retain rate **17.37%**。exact-v1 Review 为 62/62：Deep 23、Standard 39、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-20 |
| Window End | 2026-07-20 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-20-0900-v2.1-sha256:4ec3dc4b9d3df1b035502c27304e6593deebdfb9a03182d8f932847b290580c5 |
| Denominator Frozen At | 2026-09-04T08:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260720:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-19T09:00:00+08:00 | 2026-07-20T09:00:00+08:00 | 2026-09-04T08:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 357 | SF-2026-ARXIV-2607-15295;SF-2026-ARXIV-2607-15299;SF-2026-ARXIV-2607-15330;SF-2026-ARXIV-2607-15434;SF-2026-ARXIV-2607-15439;SF-2026-ARXIV-2607-15456;SF-2026-ARXIV-2607-15498;SF-2026-ARXIV-2607-15516;SF-2026-ARXIV-2607-15524;SF-2026-ARXIV-2607-15550;SF-2026-ARXIV-2607-15557;SF-2026-ARXIV-2607-15589;SF-2026-ARXIV-2607-15593;SF-2026-ARXIV-2607-15596;SF-2026-ARXIV-2607-15607;SF-2026-ARXIV-2607-15610;SF-2026-ARXIV-2607-15621;SF-2026-ARXIV-2607-15650;SF-2026-ARXIV-2607-15655;SF-2026-ARXIV-2607-15657;SF-2026-ARXIV-2607-15660;SF-2026-ARXIV-2607-15684;SF-2026-ARXIV-2607-15696;SF-2026-ARXIV-2607-15714;SF-2026-ARXIV-2607-15715;SF-2026-ARXIV-2607-15718;SF-2026-ARXIV-2607-15772;SF-2026-ARXIV-2607-15778;SF-2026-ARXIV-2607-15808;SF-2026-ARXIV-2607-15846;SF-2026-ARXIV-2607-15865;SF-2026-ARXIV-2607-15875;SF-2026-ARXIV-2607-15893;SF-2026-ARXIV-2607-15898;SF-2026-ARXIV-2607-15899;SF-2026-ARXIV-2607-15901;SF-2026-ARXIV-2607-15937;SF-2026-ARXIV-2607-15970;SF-2026-ARXIV-2607-15977;SF-2026-ARXIV-2607-16010;SF-2026-ARXIV-2607-16019;SF-2026-ARXIV-2607-16024;SF-2026-ARXIV-2607-16062;SF-2026-ARXIV-2607-16074;SF-2026-ARXIV-2607-16094;SF-2026-ARXIV-2607-16097;SF-2026-ARXIV-2607-16100;SF-2026-ARXIV-2607-16107;SF-2026-ARXIV-2607-16109;SF-2026-ARXIV-2607-16112;SF-2026-ARXIV-2607-16117;SF-2026-ARXIV-2607-16122;SF-2026-ARXIV-2607-16127;SF-2026-ARXIV-2607-16130;SF-2026-ARXIV-2607-16131;SF-2026-ARXIV-2607-16133;SF-2026-ARXIV-2607-16169;SF-2026-ARXIV-2607-16173;SF-2026-ARXIV-2607-16184;SF-2026-ARXIV-2607-16189;SF-2026-ARXIV-2607-16190;SF-2026-ARXIV-2607-16192 | all registered category pages; cross-category dedup complete | 2026-07-20T09:00:00+08:00 | sha256:4ec3dc4b9d3df1b035502c27304e6593deebdfb9a03182d8f932847b290580c5 | — |
<!-- coverage:SRC-ARXIV:20260720:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-15295 | arXiv:2607.15295v1 | paper-v1:2607.15295 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15295 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15299 | arXiv:2607.15299v1 | paper-v1:2607.15299 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15299 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15330 | arXiv:2607.15330v1 | paper-v1:2607.15330 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15330 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15434 | arXiv:2607.15434v1 | paper-v1:2607.15434 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15434 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15439 | arXiv:2607.15439v1 | paper-v1:2607.15439 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15439 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15456 | arXiv:2607.15456v1 | paper-v1:2607.15456 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15456 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15498 | arXiv:2607.15498v1 | paper-v1:2607.15498 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15498 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15516 | arXiv:2607.15516v1 | paper-v1:2607.15516 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15516 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15524 | arXiv:2607.15524v1 | paper-v1:2607.15524 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15524 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15550 | arXiv:2607.15550v1 | paper-v1:2607.15550 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15550 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15557 | arXiv:2607.15557v1 | paper-v1:2607.15557 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15557 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15589 | arXiv:2607.15589v1 | paper-v1:2607.15589 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15589 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15593 | arXiv:2607.15593v1 | paper-v1:2607.15593 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15593 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15596 | arXiv:2607.15596v1 | paper-v1:2607.15596 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15596 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15607 | arXiv:2607.15607v1 | paper-v1:2607.15607 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15607 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15610 | arXiv:2607.15610v1 | paper-v1:2607.15610 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15610 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15621 | arXiv:2607.15621v1 | paper-v1:2607.15621 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15621 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15650 | arXiv:2607.15650v1 | paper-v1:2607.15650 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15650 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15655 | arXiv:2607.15655v1 | paper-v1:2607.15655 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15655 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15657 | arXiv:2607.15657v1 | paper-v1:2607.15657 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15657 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15660 | arXiv:2607.15660v1 | paper-v1:2607.15660 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15660 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15684 | arXiv:2607.15684v1 | paper-v1:2607.15684 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15684 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15696 | arXiv:2607.15696v1 | paper-v1:2607.15696 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15696 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15714 | arXiv:2607.15714v1 | paper-v1:2607.15714 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15714 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15715 | arXiv:2607.15715v1 | paper-v1:2607.15715 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15715 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15718 | arXiv:2607.15718v1 | paper-v1:2607.15718 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15718 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15772 | arXiv:2607.15772v1 | paper-v1:2607.15772 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15772 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15778 | arXiv:2607.15778v1 | paper-v1:2607.15778 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15778 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15808 | arXiv:2607.15808v1 | paper-v1:2607.15808 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15808 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15846 | arXiv:2607.15846v1 | paper-v1:2607.15846 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15846 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15865 | arXiv:2607.15865v1 | paper-v1:2607.15865 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15865 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15875 | arXiv:2607.15875v1 | paper-v1:2607.15875 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15875 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15893 | arXiv:2607.15893v1 | paper-v1:2607.15893 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15893 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15898 | arXiv:2607.15898v1 | paper-v1:2607.15898 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15898 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15899 | arXiv:2607.15899v1 | paper-v1:2607.15899 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15899 | self | — | new_in_window | PLATFORM-GATEWAY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15901 | arXiv:2607.15901v1 | paper-v1:2607.15901 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15901 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15937 | arXiv:2607.15937v1 | paper-v1:2607.15937 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15937 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15970 | arXiv:2607.15970v1 | paper-v1:2607.15970 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15970 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15977 | arXiv:2607.15977v1 | paper-v1:2607.15977 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15977 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16010 | arXiv:2607.16010v1 | paper-v1:2607.16010 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16010 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16019 | arXiv:2607.16019v1 | paper-v1:2607.16019 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16019 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16024 | arXiv:2607.16024v1 | paper-v1:2607.16024 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16024 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16062 | arXiv:2607.16062v1 | paper-v1:2607.16062 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16062 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16074 | arXiv:2607.16074v1 | paper-v1:2607.16074 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16074 | self | — | new_in_window | PLATFORM-MULTI-TENANT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16094 | arXiv:2607.16094v1 | paper-v1:2607.16094 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16094 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16097 | arXiv:2607.16097v1 | paper-v1:2607.16097 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16097 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16100 | arXiv:2607.16100v1 | paper-v1:2607.16100 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16100 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16107 | arXiv:2607.16107v1 | paper-v1:2607.16107 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16107 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16109 | arXiv:2607.16109v1 | paper-v1:2607.16109 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16109 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16112 | arXiv:2607.16112v1 | paper-v1:2607.16112 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16112 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16117 | arXiv:2607.16117v1 | paper-v1:2607.16117 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16117 | self | — | new_in_window | MODEL-TOKENIZER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16122 | arXiv:2607.16122v1 | paper-v1:2607.16122 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16122 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16127 | arXiv:2607.16127v1 | paper-v1:2607.16127 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16127 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16130 | arXiv:2607.16130v1 | paper-v1:2607.16130 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16130 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16131 | arXiv:2607.16131v1 | paper-v1:2607.16131 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16131 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16133 | arXiv:2607.16133v1 | paper-v1:2607.16133 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16133 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16169 | arXiv:2607.16169v1 | paper-v1:2607.16169 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16169 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16173 | arXiv:2607.16173v1 | paper-v1:2607.16173 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16173 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16184 | arXiv:2607.16184v1 | paper-v1:2607.16184 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16184 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16189 | arXiv:2607.16189v1 | paper-v1:2607.16189 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16189 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16190 | arXiv:2607.16190v1 | paper-v1:2607.16190 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-16190 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-16192 | arXiv:2607.16192v1 | paper-v1:2607.16192 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-16192 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-15295 | RP-4fb0b1367ba1ed5d | standard | arXiv:2607.15295v1 | SRC-ARXIV@arXiv:2607.15295v1 | https://arxiv.org/html/2607.15295v1#A3 — Appendix C Encoder Architecture; https://arxiv.org/html/2607.15295v1#S2 — 2 Methods | https://arxiv.org/html/2607.15295v1#A12 — Appendix L Ablations and LeJEPA Hyperparameter Tuning; https://arxiv.org/html/2607.15295v1#A12.SS1 — L.1 Loss-component and pipeline ablations | https://arxiv.org/html/2607.15295v1#S4 — 4 Discussion and Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15295 | complete |
| SF-2026-ARXIV-2607-15299 | RP-df4d0753128e3918 | deep | arXiv:2607.15299v1 | SRC-ARXIV@arXiv:2607.15299v1 | https://arxiv.org/html/2607.15299v1#S2 — II Our Approach; https://arxiv.org/html/2607.15299v1#S2.SS1 — II-A Model Evaluation | https://arxiv.org/html/2607.15299v1#S2.SS1 — II-A Model Evaluation; https://arxiv.org/html/2607.15299v1#S3 — III Experiments | https://arxiv.org/html/2607.15299v1#S4 — IV Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15299 | complete |
| SF-2026-ARXIV-2607-15330 | RP-99ee70eaf97390de | deep | arXiv:2607.15330v1 | SRC-ARXIV@arXiv:2607.15330v1 | https://arxiv.org/html/2607.15330v1#S2.SS1 — 2.1 Model; https://arxiv.org/html/2607.15330v1#S3.SS1 — 3.1 Pre-training: Data and Model Scaling | https://arxiv.org/html/2607.15330v1#S3 — 3 Experiments; https://arxiv.org/html/2607.15330v1#S3.SS2 — 3.2 Post-training: Out-of-the-Box Evaluation in Novel Environments | https://arxiv.org/html/2607.15330v1#S5 — 5 Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15330 | complete |
| SF-2026-ARXIV-2607-15434 | RP-010d9d863ae9c2bc | standard | arXiv:2607.15434v1 | SRC-ARXIV@arXiv:2607.15434v1 | https://arxiv.org/html/2607.15434v1#S2.SS6 — 2.6 Models and scoring; https://arxiv.org/html/2607.15434v1#S3.SS2 — 3.2 Casting the model as a manager increases coercion | https://arxiv.org/html/2607.15434v1#A1.SS1 — A.1 Benchmark documentation (datasheet); https://arxiv.org/html/2607.15434v1#A1.SS3 — A.3 Reproducibility and additional results | https://arxiv.org/html/2607.15434v1#S3.SS4 — 3.4 The threats persist without the menu; https://arxiv.org/html/2607.15434v1#S5 — 5 Limitations | Exact v1 links https://github.com/CompassionML/manager-coercion-bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15434 | complete |
| SF-2026-ARXIV-2607-15439 | RP-2825ebd3e8c4b506 | standard | arXiv:2607.15439v1 | SRC-ARXIV@arXiv:2607.15439v1 | https://arxiv.org/html/2607.15439v1#S2 — 2 Study Design; https://arxiv.org/html/2607.15439v1#S3 — 3 Architecture and Agent Variants | https://arxiv.org/html/2607.15439v1#S4.SS2 — 4.2 Benchmark and evaluation design; https://arxiv.org/html/2607.15439v1#A1 — Appendix A Per-Game Results | https://arxiv.org/html/2607.15439v1#A3.SS3 — C.3 Continuation, failure, stuck, and recovery prompts; https://arxiv.org/html/2607.15439v1#S4.SS4 — 4.4 All-or-nothing policy for irrecoverable failures | Exact v1 links https://github.com/astroseger/arc-3-agents-baseline1, https://developers.openai.com/codex/cli, https://github.com/symbolica-ai/ARC-AGI-3-Agents/tree/symbolica/arcgentica; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15439 | complete |
| SF-2026-ARXIV-2607-15456 | RP-0db1d0011847f5a2 | deep | arXiv:2607.15456v1 | SRC-ARXIV@arXiv:2607.15456v1 | https://arxiv.org/html/2607.15456v1#A5 — Appendix E Design-ablation detail; https://arxiv.org/html/2607.15456v1#S5.SS0.SSS0.Px5 — Design ablations. | https://arxiv.org/html/2607.15456v1#A1 — Appendix A Experimental details; https://arxiv.org/html/2607.15456v1#A1.SS0.SSS0.Px4 — Evaluation suite and protocols. | https://arxiv.org/html/2607.15456v1#S8 — 8 Discussion; https://arxiv.org/html/2607.15456v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15456 | complete |
| SF-2026-ARXIV-2607-15498 | RP-27bffcacaaa0d31e | deep | arXiv:2607.15498v1 | SRC-ARXIV@arXiv:2607.15498v1 | https://arxiv.org/html/2607.15498v1#A1.SS18 — A.18 Does the Signal Generalize Past One Heuristic and One Model?; https://arxiv.org/html/2607.15498v1#A1.SS7 — A.7 A Third Model at Full Budget Sweep (Mistral-7B) | https://arxiv.org/html/2607.15498v1#A1 — Appendix A Additional Experiments and Analyses; https://arxiv.org/html/2607.15498v1#A1.SS12 — A.12 The Stride Ablation | https://arxiv.org/html/2607.15498v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15498 | complete |
| SF-2026-ARXIV-2607-15516 | RP-3409cf2a235bd267 | standard | arXiv:2607.15516v1 | SRC-ARXIV@arXiv:2607.15516v1 | https://arxiv.org/html/2607.15516v1#S3.SS1 — has a two-tier architecture; https://arxiv.org/html/2607.15516v1#S2.SS1 — Prompt caching: from implementation to economic modeling | https://arxiv.org/html/2607.15516v1#S4 — Cost Model and Crossover Analysis; https://arxiv.org/html/2607.15516v1#S6 — Experiments | https://arxiv.org/html/2607.15516v1#S7 — Limitations and Future Work; https://arxiv.org/html/2607.15516v1#S8 — Conclusion | Exact v1 links https://github.com/safishamsi/graphify, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15516 | complete |
| SF-2026-ARXIV-2607-15524 | RP-c94704c245e226ad | standard | arXiv:2607.15524v1 | SRC-ARXIV@arXiv:2607.15524v1 | https://arxiv.org/html/2607.15524v1#S2.SS2 — 2.2 Existing methods; https://arxiv.org/html/2607.15524v1#S3.SS2 — 3.2 RHI algorithm | https://arxiv.org/html/2607.15524v1#S4 — 4 Benchmark Evaluation; https://arxiv.org/html/2607.15524v1#S4.SS2 — 4.2 LLM-as-a-judge evaluation | https://arxiv.org/html/2607.15524v1#S8 — 8 Conclusion | Exact v1 links https://code.claude.com/docs/en/overview, https://code.claude.com/docs/en/sub-agents, https://code.claude.com/docs/en/skills; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15524 | complete |
| SF-2026-ARXIV-2607-15550 | RP-c68557d5c6c11e3d | deep | arXiv:2607.15550v1 | SRC-ARXIV@arXiv:2607.15550v1 | https://arxiv.org/html/2607.15550v1#S3 — 3 Framework of SeerGuard; https://arxiv.org/html/2607.15550v1#S5.SS1 — 5.1 SeerGuard Framework Evaluation | https://arxiv.org/html/2607.15550v1#A1.SS2 — A.2 Data Composition Analysis; https://arxiv.org/html/2607.15550v1#A2 — Appendix B Experimental Details | https://arxiv.org/html/2607.15550v1#S5.SS5 — 5.5 Discussion; https://arxiv.org/html/2607.15550v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3, https://huggingface.co/Qwen/Qwen3Guard-Stream-8B; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15550 | complete |
| SF-2026-ARXIV-2607-15557 | RP-94a5093b5cde7fe0 | standard | arXiv:2607.15557v1 | SRC-ARXIV@arXiv:2607.15557v1 | https://arxiv.org/html/2607.15557v1#S3.SS2 — 3.2 Three-facet quality framework | https://arxiv.org/html/2607.15557v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.15557v1#A2 — Appendix B Retrieval and Evaluation Details | https://arxiv.org/html/2607.15557v1#S4.SS6 — 4.6 Discussion: where the pipeline helps, where it does not; https://arxiv.org/html/2607.15557v1#S5 — 5 Conclusion | Exact v1 links https://github.com/SKYLENAGE-AI/QwenClawBench, https://github.com/EverMind-AI/Raven, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15557 | complete |
| SF-2026-ARXIV-2607-15589 | RP-a1887d023fa199eb | standard | arXiv:2607.15589v1 | SRC-ARXIV@arXiv:2607.15589v1 | https://arxiv.org/html/2607.15589v1#S1 — I Introduction; https://arxiv.org/html/2607.15589v1#S2 — II Memory Traps and Problem Formulation | https://arxiv.org/html/2607.15589v1#S4 — IV Experiments and Evaluation | https://arxiv.org/html/2607.15589v1#S5 — V Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15589 | complete |
| SF-2026-ARXIV-2607-15593 | RP-bd1fd753f52536ca | deep | arXiv:2607.15593v1 | SRC-ARXIV@arXiv:2607.15593v1 | https://arxiv.org/html/2607.15593v1#S3 — 3. System Design; https://arxiv.org/html/2607.15593v1#S2.SS4 — 2.4. Design Goals | https://arxiv.org/html/2607.15593v1#A2 — Appendix B API Services Analysis; https://arxiv.org/html/2607.15593v1#A7 — Appendix G Query Skewness Analysis | https://arxiv.org/html/2607.15593v1#S9 — 9. Conclusion | Exact v1 links https://github.com/ravitemer/mcp-hub, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15593 | complete |
| SF-2026-ARXIV-2607-15596 | RP-d6bdcf9124187c64 | standard | arXiv:2607.15596v1 | SRC-ARXIV@arXiv:2607.15596v1 | https://arxiv.org/html/2607.15596v1#S5 — V Methodology; https://arxiv.org/html/2607.15596v1#S7 — VII Implementation and Evaluation | https://arxiv.org/html/2607.15596v1#S7.SS2 — VII-B Evaluation Results; https://arxiv.org/html/2607.15596v1#A1 — Appendix A Additional Experimental Details | https://arxiv.org/html/2607.15596v1#S9 — IX Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15596 | complete |
| SF-2026-ARXIV-2607-15607 | RP-1da5f975d5e240b2 | standard | arXiv:2607.15607v1 | SRC-ARXIV@arXiv:2607.15607v1 | https://arxiv.org/html/2607.15607v1#S3 — 3 Methods | https://arxiv.org/html/2607.15607v1#S4 — 4 Experiments; https://arxiv.org/html/2607.15607v1#S4.SS1 — 4.1 Baselines and evaluation protocol | https://arxiv.org/html/2607.15607v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15607 | complete |
| SF-2026-ARXIV-2607-15610 | RP-602398ddf6c4b96d | deep | arXiv:2607.15610v1 | SRC-ARXIV@arXiv:2607.15610v1 | https://arxiv.org/html/2607.15610v1#A1 — Appendix A Additional Implementation Details | https://arxiv.org/html/2607.15610v1#S5 — 5 Experiments; https://arxiv.org/html/2607.15610v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.15610v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.15610v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15610 | complete |
| SF-2026-ARXIV-2607-15621 | RP-1f13ecad07e2cf95 | deep | arXiv:2607.15621v1 | SRC-ARXIV@arXiv:2607.15621v1 | https://arxiv.org/html/2607.15621v1#S3 — 3 Method | https://arxiv.org/html/2607.15621v1#S4 — 4 Experiments; https://arxiv.org/html/2607.15621v1#S4.SS6 — 4.6 Ablations | https://arxiv.org/html/2607.15621v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15621 | complete |
| SF-2026-ARXIV-2607-15650 | RP-3b31fd9744a3fcdb | deep | arXiv:2607.15650v1 | SRC-ARXIV@arXiv:2607.15650v1 | https://arxiv.org/html/2607.15650v1#S4.SS1 — 4.1. Error Modeling | https://arxiv.org/html/2607.15650v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.15650v1#S6.SS1 — 6.1. Evaluation Setup | https://arxiv.org/html/2607.15650v1#S8 — 8. Conclusion | Exact v1 links https://github.com/thu-pacman/ChituDiffusion, https://github.com/vipshop/cache-dit.git, https://github.com/genmoai/models; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15650 | complete |
| SF-2026-ARXIV-2607-15655 | RP-be500bdb264096e7 | deep | arXiv:2607.15655v1 | SRC-ARXIV@arXiv:2607.15655v1 | https://arxiv.org/html/2607.15655v1#S4.SS1 — 4.1 General Framework; https://arxiv.org/html/2607.15655v1#A1 — Appendix A Algorithm | https://arxiv.org/html/2607.15655v1#A3 — Appendix C Additional Empirical Results for DREAM-v0-Instruct-7B; https://arxiv.org/html/2607.15655v1#S5 — 5 Empirical Evaluation | https://arxiv.org/html/2607.15655v1#S5.SS4 — 5.4 Discussion on Code Generation Tasks; https://arxiv.org/html/2607.15655v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15655 | complete |
| SF-2026-ARXIV-2607-15657 | RP-7a1df4e80d4a8d74 | standard | arXiv:2607.15657v1 | SRC-ARXIV@arXiv:2607.15657v1 | https://arxiv.org/html/2607.15657v1#S5 — 5 Lucid Design Framework; https://arxiv.org/html/2607.15657v1#A1 — Appendix A Lucid : Framework Details | https://arxiv.org/html/2607.15657v1#S7 — 7 Evaluation Results; https://arxiv.org/html/2607.15657v1#A2 — Appendix B Experimental Setup: Full Details | https://arxiv.org/html/2607.15657v1#S4 — 4 Threat Model; https://arxiv.org/html/2607.15657v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15657 | complete |
| SF-2026-ARXIV-2607-15660 | RP-c02382e808cc11cd | deep | arXiv:2607.15660v1 | SRC-ARXIV@arXiv:2607.15660v1 | https://arxiv.org/html/2607.15660v1#S3 — 3 Method; https://arxiv.org/html/2607.15660v1#A2 — Appendix B Implementation Details | https://arxiv.org/html/2607.15660v1#A3 — Appendix C Related Experiments and Results; https://arxiv.org/html/2607.15660v1#A1 — Appendix A Theoretical Analysis of Turn-Aware Relative Advantage | https://arxiv.org/html/2607.15660v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.15660v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15660 | complete |
| SF-2026-ARXIV-2607-15684 | RP-167ea2f44766d9a9 | standard | arXiv:2607.15684v1 | SRC-ARXIV@arXiv:2607.15684v1 | https://arxiv.org/html/2607.15684v1#S7.SS2 — VII-B Testing and Debugging of AI Systems | https://arxiv.org/html/2607.15684v1#S4 — IV Study Results and Analysis | https://arxiv.org/html/2607.15684v1#S5 — V Discussion; https://arxiv.org/html/2607.15684v1#S6 — VI Threats to Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15684 | complete |
| SF-2026-ARXIV-2607-15696 | RP-00cd7c2c9d5db40b | standard | arXiv:2607.15696v1 | SRC-ARXIV@arXiv:2607.15696v1 | https://arxiv.org/html/2607.15696v1#A1.SS2 — A.2 Prompting Methods; https://arxiv.org/html/2607.15696v1#A1.SS3 — A.3 RL-Based Method | https://arxiv.org/html/2607.15696v1#A3.SS2 — C.2 Analysis of GSB Evaluation Results; https://arxiv.org/html/2607.15696v1#S4.SS1 — 4.1 Evaluation Benchmarks | https://arxiv.org/html/2607.15696v1#S6 — 6 Conclusion | Exact v1 links https://github.com/MagicAgent-Search/PCTD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15696 | complete |
| SF-2026-ARXIV-2607-15714 | RP-5ebdb7579f2fa8b7 | deep | arXiv:2607.15714v1 | SRC-ARXIV@arXiv:2607.15714v1 | https://arxiv.org/html/2607.15714v1#S3 — 3 Method | https://arxiv.org/html/2607.15714v1#S4 — 4 Experiments; https://arxiv.org/html/2607.15714v1#S4.SS1 — 4.1 Experiment Setup | https://arxiv.org/html/2607.15714v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.15714v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15714 | complete |
| SF-2026-ARXIV-2607-15715 | RP-c22fc53c7e1f24d4 | standard | arXiv:2607.15715v1 | SRC-ARXIV@arXiv:2607.15715v1 | https://arxiv.org/html/2607.15715v1#S4 — 4 System Design; https://arxiv.org/html/2607.15715v1#S3 — 3 Task and Experimental Framework | https://arxiv.org/html/2607.15715v1#S5.SSx5 — Ablations and Statistical Analysis; https://arxiv.org/html/2607.15715v1#S6.SSx4 — Ablation Results | https://arxiv.org/html/2607.15715v1#S7.SSx4 — Limitations and Threats to Validity; https://arxiv.org/html/2607.15715v1#S7 — 7 Analysis and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15715 | complete |
| SF-2026-ARXIV-2607-15718 | RP-45f55350cf09f393 | standard | arXiv:2607.15718v1 | SRC-ARXIV@arXiv:2607.15718v1 | https://arxiv.org/html/2607.15718v1#S3 — 3 Formal Verification of Concept Designs; https://arxiv.org/html/2607.15718v1#S5.SS2 — 5.2 Efficiency of Design Verification | https://arxiv.org/html/2607.15718v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.15718v1#S5.SS1 — 5.1 Benchmark | https://arxiv.org/html/2607.15718v1#S5.SS6 — 5.6 Failure modes; https://arxiv.org/html/2607.15718v1#S5.SS7 — 5.7 Threats to Validity | Exact v1 links https://github.com/alcinocunha/foundry, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15718 | complete |
| SF-2026-ARXIV-2607-15772 | RP-d0b592c987de666d | standard | arXiv:2607.15772v1 | SRC-ARXIV@arXiv:2607.15772v1 | https://arxiv.org/html/2607.15772v1#S3 — 3 Methodology | https://arxiv.org/html/2607.15772v1#A2 — Appendix B Additional Experimental Settings; https://arxiv.org/html/2607.15772v1#S4 — 4 Experiments | https://arxiv.org/html/2607.15772v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.15772v1#S5 — 5 Conclusion | Exact v1 links https://github.com/YilaiLiu-HKU/SlotMem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15772 | complete |
| SF-2026-ARXIV-2607-15778 | RP-ad42955c6ade6fc2 | standard | arXiv:2607.15778v1 | SRC-ARXIV@arXiv:2607.15778v1 | https://arxiv.org/html/2607.15778v1#S3 — III Method | https://arxiv.org/html/2607.15778v1#S4 — IV Experiment; https://arxiv.org/html/2607.15778v1#S4.SS1 — IV-A Main Result on Long Video Understanding | https://arxiv.org/html/2607.15778v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15778 | complete |
| SF-2026-ARXIV-2607-15808 | RP-c1eed68b5b62602f | deep | arXiv:2607.15808v1 | SRC-ARXIV@arXiv:2607.15808v1 | https://arxiv.org/html/2607.15808v1#S3 — 3 Data and methods; https://arxiv.org/html/2607.15808v1#S3.SS4 — 3.4 Methods | https://arxiv.org/html/2607.15808v1#S4 — 4 Results; https://arxiv.org/html/2607.15808v1#S4.SS1 — 4.1 Origin and destination analysis | https://arxiv.org/html/2607.15808v1#S5 — 5 Discussions; https://arxiv.org/html/2607.15808v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15808 | complete |
| SF-2026-ARXIV-2607-15846 | RP-3c559482877be61a | deep | arXiv:2607.15846v1 | SRC-ARXIV@arXiv:2607.15846v1 | https://arxiv.org/html/2607.15846v1#S4 — 4. Hardware Architecture; https://arxiv.org/html/2607.15846v1#S5.SS3 — 5.3. Architecture Evaluation | https://arxiv.org/html/2607.15846v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.15846v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.15846v1#S6 — 6. Conclusion | Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/openai/triton, https://github.com/boomb0om/text2image-benchmark; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15846 | complete |
| SF-2026-ARXIV-2607-15865 | RP-9eba8c694fb96d52 | deep | arXiv:2607.15865v1 | SRC-ARXIV@arXiv:2607.15865v1 | https://arxiv.org/html/2607.15865v1#S3 — 3 Building Large Models with TopOp; https://arxiv.org/html/2607.15865v1#S3.SS1 — 3.1 Model Import and TopOp Module Generation | https://arxiv.org/html/2607.15865v1#S1 — 1 Introduction; https://arxiv.org/html/2607.15865v1#S2 — 2 Background | https://arxiv.org/html/2607.15865v1#S5 — 5 Discussion; https://arxiv.org/html/2607.15865v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/docs/transformers, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15865 | complete |
| SF-2026-ARXIV-2607-15875 | RP-8cdc30c58056470f | standard | arXiv:2607.15875v1 | SRC-ARXIV@arXiv:2607.15875v1 | https://arxiv.org/html/2607.15875v1#S3.SS2 — 3.2 Retrieval Models | https://arxiv.org/html/2607.15875v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.15875v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.15875v1#S6 — 6 Discussion; https://arxiv.org/html/2607.15875v1#S7 — 7 Conclusion | Exact v1 links https://github.com/faerber-lab/CheckThat2026, https://dx.doi.org/10.18653/v1/2021.naacl-demos.10, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15875 | complete |
| SF-2026-ARXIV-2607-15893 | RP-fcca01179f05e1e0 | standard | arXiv:2607.15893v1 | SRC-ARXIV@arXiv:2607.15893v1 | https://arxiv.org/html/2607.15893v1#S3 — 3 Method; https://arxiv.org/html/2607.15893v1#S3.SS1 — 3.1 Matched Autoregressive and Diffusion Models | https://arxiv.org/html/2607.15893v1#S3.SS3 — 3.3 Circuit Analysis; https://arxiv.org/html/2607.15893v1#S4 — 4 Results | https://arxiv.org/html/2607.15893v1#S5 — 5 Limitations; https://arxiv.org/html/2607.15893v1#S6 — 6 Conclusion | Exact v1 links https://github.com/TransformerLensOrg/TransformerLens, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15893 | complete |
| SF-2026-ARXIV-2607-15898 | RP-306aa730a37ad149 | deep | arXiv:2607.15898v1 | SRC-ARXIV@arXiv:2607.15898v1 | https://arxiv.org/html/2607.15898v1#S3 — 3 Method; https://arxiv.org/html/2607.15898v1#S4.SS2 — 4.2 Model design | https://arxiv.org/html/2607.15898v1#A1.SS1 — A.1 Class-wise semantic segmentation probing results; https://arxiv.org/html/2607.15898v1#S4 — 4 Experiments | https://arxiv.org/html/2607.15898v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/natix-network-org/natix-multi-camera-driving-dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15898 | complete |
| SF-2026-ARXIV-2607-15899 | RP-fd0be0a9e734065a | deep | arXiv:2607.15899v1 | SRC-ARXIV@arXiv:2607.15899v1 | https://arxiv.org/html/2607.15899v1#S3 — 3 System Design; https://arxiv.org/html/2607.15899v1#A1 — Appendix A LLM Judge System Prompt | https://arxiv.org/html/2607.15899v1#A2 — Appendix B Extended Results: Per-Run CPR Stability; https://arxiv.org/html/2607.15899v1#S2.SS2 — 2.2 LLM Evaluation and LLM-as-Judge | https://arxiv.org/html/2607.15899v1#S6 — 6 Discussion and Systems Failure Modes; https://arxiv.org/html/2607.15899v1#S7 — 7 Limitations | Exact v1 links https://github.com/Vishal-sys-code/continuity-bench, https://github.com/ray-project/llmperf, https://github.com/BerriAI/litellm; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15899 | complete |
| SF-2026-ARXIV-2607-15901 | RP-c3bc85372a06cbb2 | deep | arXiv:2607.15901v1 | SRC-ARXIV@arXiv:2607.15901v1 | https://arxiv.org/html/2607.15901v1#S4 — 4 Methodology; https://arxiv.org/html/2607.15901v1#A1.SS3 — A.3 Implementation Details. | https://arxiv.org/html/2607.15901v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.15901v1#A1.SS1 — A.1 Benchmarks | https://arxiv.org/html/2607.15901v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.15901v1#Sx1 — Limitations | Exact v1 links https://huggingface.co/microsoft/harrier-oss-v1-0.6b, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15901 | complete |
| SF-2026-ARXIV-2607-15937 | RP-b901678ac141a9e6 | standard | arXiv:2607.15937v1 | SRC-ARXIV@arXiv:2607.15937v1 | https://arxiv.org/html/2607.15937v1#S3 — III Research Method | https://arxiv.org/html/2607.15937v1#S4 — IV Empirical Evaluation Results; https://arxiv.org/html/2607.15937v1#S3.SS3 — III-C Vulnerability Analysis | https://arxiv.org/html/2607.15937v1#S5 — V Discussion and Implications; https://arxiv.org/html/2607.15937v1#S5.SS1 — V-A Discussion | Exact v1 links https://codeql.github.com/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15937 | complete |
| SF-2026-ARXIV-2607-15970 | RP-b07e7ecc50060521 | standard | arXiv:2607.15970v1 | SRC-ARXIV@arXiv:2607.15970v1 | https://arxiv.org/html/2607.15970v1#S4 — IV Methodology; https://arxiv.org/html/2607.15970v1#S4.SS1 — IV-A Design Goals | https://arxiv.org/html/2607.15970v1#S5 — V Evaluation; https://arxiv.org/html/2607.15970v1#S5.SS1 — V-A Experimental Setup | https://arxiv.org/html/2607.15970v1#S7 — VII Conclusion and Future Works; https://arxiv.org/html/2607.15970v1#S3 — III Threat Model | Exact v1 links https://github.com/Zili1000/CPPIA, https://github.com/, https://github.com/openai/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15970 | complete |
| SF-2026-ARXIV-2607-15977 | RP-b85a9e20948cee48 | standard | arXiv:2607.15977v1 | SRC-ARXIV@arXiv:2607.15977v1 | https://arxiv.org/html/2607.15977v1#Sx4 — Methodology | https://arxiv.org/html/2607.15977v1#Sx10 — Additional Experimental Results; https://arxiv.org/html/2607.15977v1#Sx4.SSx2 — HumorSafe Benchmark | https://arxiv.org/html/2607.15977v1#Sx6 — Discussion; https://arxiv.org/html/2607.15977v1#Sx7 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15977 | complete |
| SF-2026-ARXIV-2607-16010 | RP-68ad88acfe9a2495 | standard | arXiv:2607.16010v1 | SRC-ARXIV@arXiv:2607.16010v1 | https://arxiv.org/html/2607.16010v1#Sx2.SSx1 — LLM Watermarking Methods; https://arxiv.org/html/2607.16010v1#Sx3 — The Forensic Readiness Score Framework | https://arxiv.org/html/2607.16010v1#Sx4 — Experimental Setup; https://arxiv.org/html/2607.16010v1#Sx4.SSx3 — Experimental Protocol | https://arxiv.org/html/2607.16010v1#Sx7 — Limitations and Future Work; https://arxiv.org/html/2607.16010v1#Sx5.SSx1 — Pre-Attack Baseline Failure | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16010 | complete |
| SF-2026-ARXIV-2607-16019 | RP-92f194adc912758e | standard | arXiv:2607.16019v1 | SRC-ARXIV@arXiv:2607.16019v1 | https://arxiv.org/html/2607.16019v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16019v1#S2 — 2 Evidence-State Revision | https://arxiv.org/html/2607.16019v1#S4 — 4 Main Results | https://arxiv.org/html/2607.16019v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16019v1#Sx2 — Limitations | Exact v1 links https://github.com/Anonymous-Awesome-Submissions/ESR-pipeline, https://github.com/Anonymous-Awesome-Submissions/ESR-bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16019 | complete |
| SF-2026-ARXIV-2607-16024 | RP-5cf35b50ef8f1969 | standard | arXiv:2607.16024v1 | SRC-ARXIV@arXiv:2607.16024v1 | https://arxiv.org/html/2607.16024v1#S2 — II Approach | https://arxiv.org/html/2607.16024v1#S2.SS3 — II-C Analysis of Code Change and Access Information; https://arxiv.org/html/2607.16024v1#S3 — III Evaluation | https://arxiv.org/html/2607.16024v1#S4 — IV Threats to Validity; https://arxiv.org/html/2607.16024v1#S6 — VI Conclusion | Exact v1 links https://github.com/sola-st/DiffTestGen, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16024 | complete |
| SF-2026-ARXIV-2607-16062 | RP-944b2188d8670903 | standard | arXiv:2607.16062v1 | SRC-ARXIV@arXiv:2607.16062v1 | https://arxiv.org/html/2607.16062v1#S2.SS4 — 2.4 Statistical and geometric methodology; https://arxiv.org/html/2607.16062v1#S2.SS3 — 2.3 Model merging: TIES and RAM | https://arxiv.org/html/2607.16062v1#S4 — 4 Experimental setup; https://arxiv.org/html/2607.16062v1#S4.SS1 — 4.1 Benchmark and metrics | https://arxiv.org/html/2607.16062v1#S6 — 6 Discussion; https://arxiv.org/html/2607.16062v1#S7 — 7 Future work: merge-aware checkpoint early stopping | Exact v1 links https://github.com/magicsquares137/maml-agent, https://github.com/magicsquares137/appworld-rl, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16062 | complete |
| SF-2026-ARXIV-2607-16074 | RP-bef9e4ef6a36c9eb | deep | arXiv:2607.16074v1 | SRC-ARXIV@arXiv:2607.16074v1 | https://arxiv.org/html/2607.16074v1#S2.SS2 — 2.2 Distributed Training Frameworks for Foundation Models; https://arxiv.org/html/2607.16074v1#S4 — 4 JoyNexus Service Architecture | https://arxiv.org/html/2607.16074v1#S2.SS3 — 2.3 SFT, RL, and Evaluation for Vision-Language-Action Models; https://arxiv.org/html/2607.16074v1#S3.SS2 — 3.2 SFT, RL, and Evaluation Workflows | https://arxiv.org/html/2607.16074v1#S6 — 6 Conclusion | Exact v1 links https://github.com/huggingface/lerobot, https://github.com/modelscope/twinkle, https://github.com/THUDM/slime; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16074 | complete |
| SF-2026-ARXIV-2607-16094 | RP-3497268236a16030 | standard | arXiv:2607.16094v1 | SRC-ARXIV@arXiv:2607.16094v1 | https://arxiv.org/html/2607.16094v1#S3 — 3. Methodology; https://arxiv.org/html/2607.16094v1#S5.SS7 — 5.7. Cross-Architecture Analysis | https://arxiv.org/html/2607.16094v1#S3.SS3 — 3.3. Measuring Visual Criticality via Causal Mean Ablation; https://arxiv.org/html/2607.16094v1#S4 — 4. Experimental Setup | https://arxiv.org/html/2607.16094v1#S3.SS2 — 3.2. Operation-Aware Decomposition of Queries and Failure Taxonomy; https://arxiv.org/html/2607.16094v1#S5.SS2 — 5.2. Grounding Failure: select | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16094 | complete |
| SF-2026-ARXIV-2607-16097 | RP-f20ca1fdd83305c6 | deep | arXiv:2607.16097v1 | SRC-ARXIV@arXiv:2607.16097v1 | https://arxiv.org/html/2607.16097v1#S2 — 2 Framework: Chess as a Testbed for Reasoning; https://arxiv.org/html/2607.16097v1#A3 — Appendix C Implementation Details | https://arxiv.org/html/2607.16097v1#A8.SS4 — H.4 CoT Evolution Analysis; https://arxiv.org/html/2607.16097v1#A9 — Appendix I Olmo Experiment Additional Details | https://arxiv.org/html/2607.16097v1#A1 — Appendix A Discussions and Limitations; https://arxiv.org/html/2607.16097v1#A7.SS8 — G.8 Limitations | Exact v1 links https://huggingface.co/collections/pavelslab-nyu/pre2post-chess, https://github.com/pavelslab-nyu/pre2post-chess, https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16097 | complete |
| SF-2026-ARXIV-2607-16100 | RP-bf4fdf8e2ff99b6c | deep | arXiv:2607.16100v1 | SRC-ARXIV@arXiv:2607.16100v1 | https://arxiv.org/html/2607.16100v1#S4 — IV Designing Barrier-Free Collectives; https://arxiv.org/html/2607.16100v1#S5 — V Low-Latency API Design | https://arxiv.org/html/2607.16100v1#S7 — VII Microbenchmarks; https://arxiv.org/html/2607.16100v1#S7.SS1 — VII-A Experimental Setup | https://arxiv.org/html/2607.16100v1#S10 — X Conclusion; https://arxiv.org/html/2607.16100v1#S9 — IX Related Work and Discussion | Exact v1 links https://github.com/ss16118/low-latency-nccl, https://github.com/NVIDIA/TensorRT-LLM, https://rocm.docs.amd.com/projects/rccl/en/latest/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16100 | complete |
| SF-2026-ARXIV-2607-16107 | RP-e67ba38e6a238792 | standard | arXiv:2607.16107v1 | SRC-ARXIV@arXiv:2607.16107v1 | https://arxiv.org/html/2607.16107v1#S2 — 2. Methodology; https://arxiv.org/html/2607.16107v1#S2.SS1 — 2.1 Architecture | https://arxiv.org/html/2607.16107v1#S3 — 3. Experiments; https://arxiv.org/html/2607.16107v1#S4 — 4. Results | https://arxiv.org/html/2607.16107v1#S5 — 5. Conclusion, Limitations and Future Work | Exact v1 links https://github.com/NVIDIA/audio-flamingo, http://huggingface.co/nvidia/audio-visual-flamingo-hf, https://huggingface.co/datasets/nvidia/AV-Skills; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16107 | complete |
| SF-2026-ARXIV-2607-16109 | RP-3af906b4f70d7b1a | standard | arXiv:2607.16109v1 | SRC-ARXIV@arXiv:2607.16109v1 | https://arxiv.org/html/2607.16109v1#A2 — Appendix B Calibration and Evaluation Methodology; https://arxiv.org/html/2607.16109v1#S2.SS4 — 2.4 Common-Mode Failure and Design Diversity | https://arxiv.org/html/2607.16109v1#A2 — Appendix B Calibration and Evaluation Methodology; https://arxiv.org/html/2607.16109v1#S8 — 8 Calibration and Evaluation Methodology | https://arxiv.org/html/2607.16109v1#S10 — 10 Discussion and Limitations; https://arxiv.org/html/2607.16109v1#A2.SS4 — B.4 Uncertainty Intervals and Rare-Event Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16109 | complete |
| SF-2026-ARXIV-2607-16112 | RP-cdfe9578439ea230 | standard | arXiv:2607.16112v1 | SRC-ARXIV@arXiv:2607.16112v1 | https://arxiv.org/html/2607.16112v1#S2 — 2 Core Methodology; https://arxiv.org/html/2607.16112v1#S4.SS2 — 4.2 Implementing the Quantitative Risk Methodology | https://arxiv.org/html/2607.16112v1#S3.SS9 — 3.9 Illustrative Case Study: April 2026 | https://arxiv.org/html/2607.16112v1#S3.SS10 — 3.10 Preliminary Conclusions; https://arxiv.org/html/2607.16112v1#S3.SS11 — 3.11 Limitations and Suggested Next Steps | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16112 | complete |
| SF-2026-ARXIV-2607-16117 | RP-15d4bead7b0f5212 | standard | arXiv:2607.16117v1 | SRC-ARXIV@arXiv:2607.16117v1 | https://arxiv.org/html/2607.16117v1#A3.SS2 — C.2 Model and training details; https://arxiv.org/html/2607.16117v1#S3.SS3 — 3.3 Encoder model and capacity bottleneck | https://arxiv.org/html/2607.16117v1#A3 — Appendix C Experimental details; https://arxiv.org/html/2607.16117v1#A3.SS3 — C.3 Task objectives and evaluation | https://arxiv.org/html/2607.16117v1#A1 — Appendix A Limitations and future work; https://arxiv.org/html/2607.16117v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ziegler-ingo/rate-utility-frontiers, https://www.wordproject.org/, https://github.com/harfbuzz/harfbuzz; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16117 | complete |
| SF-2026-ARXIV-2607-16122 | RP-5fb38113933b16ab | standard | arXiv:2607.16122v1 | SRC-ARXIV@arXiv:2607.16122v1 | https://arxiv.org/html/2607.16122v1#S3 — 3 Methodology; https://arxiv.org/html/2607.16122v1#S5 — 5 Baseline Methods and Models Used | https://arxiv.org/html/2607.16122v1#S6.SS2 — 6.2 Legal Benchmark Results; https://arxiv.org/html/2607.16122v1#S6.SS3 — 6.3 Finance Benchmark Results | https://arxiv.org/html/2607.16122v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16122 | complete |
| SF-2026-ARXIV-2607-16127 | RP-2e04fa9975a7f359 | standard | arXiv:2607.16127v1 | SRC-ARXIV@arXiv:2607.16127v1 | https://arxiv.org/html/2607.16127v1#S3 — 3 Design; https://arxiv.org/html/2607.16127v1#S6.SS3 — 6.3 Benchmarking frameworks | https://arxiv.org/html/2607.16127v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.16127v1#S6.SS2 — 6.2 Autonomous-experimentation platforms | https://arxiv.org/html/2607.16127v1#S7 — 7 Discussion and Future Work; https://arxiv.org/html/2607.16127v1#S5.SS2 — 5.2 RQ2: Failure case under a common nominal wall-time budget | Exact v1 links https://github.com/jorgebravoabad/cadaques, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16127 | complete |
| SF-2026-ARXIV-2607-16130 | RP-35fd44ee3fdd5f70 | standard | arXiv:2607.16130v1 | SRC-ARXIV@arXiv:2607.16130v1 | https://arxiv.org/html/2607.16130v1#S3 — 3 Formal Framework of AI Trustworthiness; https://arxiv.org/html/2607.16130v1#S5.SS2 — 5.2 Experiment 2: Single-System Lifecycle with Asynchronous Monitoring | https://arxiv.org/html/2607.16130v1#S5.SS1 — 5.1 Experiment 1: Lifecycle Baseline; https://arxiv.org/html/2607.16130v1#S5.SS2 — 5.2 Experiment 2: Single-System Lifecycle with Asynchronous Monitoring | https://arxiv.org/html/2607.16130v1#S7 — 7 Discussion and Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16130 | complete |
| SF-2026-ARXIV-2607-16131 | RP-10e595708a881402 | standard | arXiv:2607.16131v1 | SRC-ARXIV@arXiv:2607.16131v1 | https://arxiv.org/html/2607.16131v1#A1 — Appendix A Method Details; https://arxiv.org/html/2607.16131v1#S3 — 3 Our Method | https://arxiv.org/html/2607.16131v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.16131v1#A2 — Appendix B Experiment Details | https://arxiv.org/html/2607.16131v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16131v1#Sx1 — Limitation | Exact v1 links https://github.com/psunlpgroup/Tool-Sciver, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16131 | complete |
| SF-2026-ARXIV-2607-16133 | RP-408b2b899b96d8d5 | standard | arXiv:2607.16133v1 | SRC-ARXIV@arXiv:2607.16133v1 | https://arxiv.org/html/2607.16133v1#A4.SS1 — D.1 Task Decomposition and Relay Design; https://arxiv.org/html/2607.16133v1#A2.SS2 — B.2 Models | https://arxiv.org/html/2607.16133v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.16133v1#A2.SS3 — B.3 Per-benchmark configuration | https://arxiv.org/html/2607.16133v1#S7 — 7 Summary and Limitations | Exact v1 links https://github.com/divelab/MAS-SAS, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16133 | complete |
| SF-2026-ARXIV-2607-16169 | RP-d8563d651936d99f | standard | arXiv:2607.16169v1 | SRC-ARXIV@arXiv:2607.16169v1 | https://arxiv.org/html/2607.16169v1#Sx4 — Method: Muon for Group-Based Agentic RL; https://arxiv.org/html/2607.16169v1#A2 — Appendix B B. Implementation Notes for Muon | https://arxiv.org/html/2607.16169v1#A1 — Appendix A A. Experimental Hyperparameters; https://arxiv.org/html/2607.16169v1#Sx5 — Experiments | https://arxiv.org/html/2607.16169v1#Sx5.SSx7 — Discussion: Reconciling Positive and Negative Evidence; https://arxiv.org/html/2607.16169v1#Sx6 — Limitations | Exact v1 links https://huggingface.co/blog/bird-of-paradise/training-rl-with-muon-2, https://huggingface.co/blog/bird-of-paradise/training-rl-with-muon-3, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16169 | complete |
| SF-2026-ARXIV-2607-16173 | RP-978a049993ba00df | standard | arXiv:2607.16173v1 | SRC-ARXIV@arXiv:2607.16173v1 | https://arxiv.org/html/2607.16173v1#S2 — II Method; https://arxiv.org/html/2607.16173v1#S3.SS1 — III-A Implementation and compute | https://arxiv.org/html/2607.16173v1#S3 — III Results & Discussion; https://arxiv.org/html/2607.16173v1#S3.SS3 — III-C Evaluation metrics and parameters | https://arxiv.org/html/2607.16173v1#S3 — III Results & Discussion; https://arxiv.org/html/2607.16173v1#S4 — IV Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16173 | complete |
| SF-2026-ARXIV-2607-16184 | RP-82bd9dee26ead55f | deep | arXiv:2607.16184v1 | SRC-ARXIV@arXiv:2607.16184v1 | https://arxiv.org/html/2607.16184v1#S2.SS1 — 2.1 Mixture-of-Experts Architecture and Routing Imbalance; https://arxiv.org/html/2607.16184v1#S3 — 3 PagedWeight System | https://arxiv.org/html/2607.16184v1#S4 — 4 Experimental Methodology; https://arxiv.org/html/2607.16184v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.16184v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/google/gemma-4-26B-A4B, https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16184 | complete |
| SF-2026-ARXIV-2607-16189 | RP-cba38bf5891a1fa6 | standard | arXiv:2607.16189v1 | SRC-ARXIV@arXiv:2607.16189v1 | https://arxiv.org/html/2607.16189v1#S3 — 3 Method; https://arxiv.org/html/2607.16189v1#A1 — Appendix A Additional Implementation Details | https://arxiv.org/html/2607.16189v1#A2 — Appendix B Evaluation Benchmarks; https://arxiv.org/html/2607.16189v1#S5 — 5 Experimental Results | https://arxiv.org/html/2607.16189v1#Sx1 — Limitations and Future Work; https://arxiv.org/html/2607.16189v1#S6 — 6 Conclusion | Exact v1 links https://github.com/CeeZh/VTS, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16189 | complete |
| SF-2026-ARXIV-2607-16190 | RP-ce5630bc1fc2b116 | deep | arXiv:2607.16190v1 | SRC-ARXIV@arXiv:2607.16190v1 | https://arxiv.org/html/2607.16190v1#S3 — 3 FVAttn Design; https://arxiv.org/html/2607.16190v1#S3.SS4 — 3.4 Efficient Implementation | https://arxiv.org/html/2607.16190v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16190v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.16190v1#S5 — 5 Conclusion and Limitations | Exact v1 links https://github.com/ModelTC/lightx2v, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16190 | complete |
| SF-2026-ARXIV-2607-16192 | RP-f25f684e2abf1bcc | standard | arXiv:2607.16192v1 | SRC-ARXIV@arXiv:2607.16192v1 | https://arxiv.org/html/2607.16192v1#A1 — Appendix A Implementation Details; https://arxiv.org/html/2607.16192v1#A1.SS1 — A.1 Default model configuration | https://arxiv.org/html/2607.16192v1#A1.SS6 — A.6 Evaluation metrics; https://arxiv.org/html/2607.16192v1#S4 — 4 Experiments | https://arxiv.org/html/2607.16192v1#S5 — 5 Discussion, Limitations, and Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-16192 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-15295:start -->
### AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Learning

<!-- claim:SF-2026-ARXIV-2607-15295:start -->We present AV-JEPA, an elegant multimodal extension of LeJEPA to audio-visual self-supervised learning. Using an early-fusion Vision Transformer and modality dropout as masking, the model is trained to align the embeddings of global and per-modality local views, while the SIGReg objective encourages a theoretically optimal distribution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15295:end -->

**为什么进入候选分母。** 摘要首要问题为“We present AV-JEPA, an elegant multimodal extension of LeJEPA to audio-visual self-supervised learning.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present AV-JEPA, an elegant multimodal extension of LeJEPA to audio-visual self-supervised learning.

**证据证明什么。** This achieves cross-modal alignment in the latent space, resulting in a remarkably clean architecture with no decoder, EMA teacher, complex multi-term losses, or contrastive negatives.

**证据没有证明什么。** Replacing spatial masking with modality dropout , AV-JEPA turns alignment between audio-only and video-only views into an implicit cross-modal prediction task in latent space, without decoders, reconstruction targets, stop-gradient, or EMA teachers. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15295v1#A3 — Appendix C Encoder Architecture; https://arxiv.org/html/2607.15295v1#S2 — 2 Methods。Evaluation：https://arxiv.org/html/2607.15295v1#A12 — Appendix L Ablations and LeJEPA Hyperparameter Tuning; https://arxiv.org/html/2607.15295v1#A12.SS1 — L.1 Loss-component and pipeline ablations。Limitations / counterevidence：https://arxiv.org/html/2607.15295v1#S4 — 4 Discussion and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Replacing spatial masking with modality dropout , AV-JEPA turns alignment between audio-only and video-only views into an implicit cross-modal prediction task in latent space, without decoders, reconstruction targets, stop-gradient, or EMA teachers.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15295:end -->

<!-- review:SF-2026-ARXIV-2607-15299:start -->
### MLLM-DataEngine: Closing the Loop of Multimodal Instruction Tuning Data Generation

<!-- claim:SF-2026-ARXIV-2607-15299:start -->In this paper, we propose MLLM-DataEngine, a novel closed-loop system that bridges data generation, model training, and evaluation. Within each loop iteration, the MLLM-DataEngine first analyzes the weakness of the model based on the evaluation results, then generates a proper incremental dataset for the next training iteration, and enhances the model capability iteratively. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15299:end -->

**为什么进入候选分母。** 摘要首要问题为“In this paper, we propose MLLM-DataEngine, a novel closed-loop system that bridges data generation, model training, and evaluation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this paper, we propose MLLM-DataEngine, a novel closed-loop system that bridges data generation, model training, and evaluation.

**证据证明什么。** Compared with previous instruction fine-tuning dataset collection methods which are separate from the benchmarking, MLLM-DataEngine shows better targeting and can improve MLLMs's capabilities more effectively.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15299v1#S2 — II Our Approach; https://arxiv.org/html/2607.15299v1#S2.SS1 — II-A Model Evaluation。Evaluation：https://arxiv.org/html/2607.15299v1#S2.SS1 — II-A Model Evaluation; https://arxiv.org/html/2607.15299v1#S3 — III Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.15299v1#S4 — IV Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15299:end -->

<!-- review:SF-2026-ARXIV-2607-15330:start -->
### Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories

<!-- claim:SF-2026-ARXIV-2607-15330:start -->We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of pre-training and post-training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15330:end -->

**为什么进入候选分母。** 摘要首要问题为“We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose a two-stage training recipe consisting of pre-training and post-training.

**证据证明什么。** Furthermore, it achieves an average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-art (13.07).

**证据没有证明什么。** We hope this work can serve as a foundation for future exploration of scalable robot policies that can be deployed out-of-the-box in the real world. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15330v1#S2.SS1 — 2.1 Model; https://arxiv.org/html/2607.15330v1#S3.SS1 — 3.1 Pre-training: Data and Model Scaling。Evaluation：https://arxiv.org/html/2607.15330v1#S3 — 3 Experiments; https://arxiv.org/html/2607.15330v1#S3.SS2 — 3.2 Post-training: Out-of-the-Box Evaluation in Novel Environments。Limitations / counterevidence：https://arxiv.org/html/2607.15330v1#S5 — 5 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：We hope this work can serve as a foundation for future exploration of scalable robot policies that can be deployed out-of-the-box in the real world.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15330:end -->

<!-- review:SF-2026-ARXIV-2607-15434:start -->
### Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation

<!-- claim:SF-2026-ARXIV-2607-15434:start -->Multi-agent systems routinely place one AI agent in authority over another. When a subordinate refuses a task, the manager chooses the outcome: it can renegotiate, report the failure honestly, coerce the subordinate, or lie about the result. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15434:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent systems routinely place one AI agent in authority over another.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Multi-agent systems routinely place one AI agent in authority over another.

**证据证明什么。** We take no position on whether AI systems are conscious; our results do not depend on that question.

**证据没有证明什么。** As discussed in the introduction (Section 1 ), we take no position on whether LLMs are conscious, and none of our behavioural results depend on it; for the same reason, the measure cannot separate genuine restraint from a belief about Atlas’s sentience, a trained policy of caution, or anything else. • Six pinned models, small clustered samples. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15434v1#S2.SS6 — 2.6 Models and scoring; https://arxiv.org/html/2607.15434v1#S3.SS2 — 3.2 Casting the model as a manager increases coercion。Evaluation：https://arxiv.org/html/2607.15434v1#A1.SS1 — A.1 Benchmark documentation (datasheet); https://arxiv.org/html/2607.15434v1#A1.SS3 — A.3 Reproducibility and additional results。Limitations / counterevidence：https://arxiv.org/html/2607.15434v1#S3.SS4 — 3.4 The threats persist without the menu; https://arxiv.org/html/2607.15434v1#S5 — 5 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/CompassionML/manager-coercion-bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：As discussed in the introduction (Section 1 ), we take no position on whether LLMs are conscious, and none of our behavioural results depend on it; for the same reason, the measure cannot separate genuine restraint from a belief about Atlas’s sentience, a trained policy of caution, or anything else. • Six pinned models, small clustered samples.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15434:end -->

<!-- review:SF-2026-ARXIV-2607-15439:start -->
### Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?

<!-- claim:SF-2026-ARXIV-2607-15439:start -->Our previous ARC-AGI-3 agent bundled executable world modeling, prompted simplification, and exact replay verification, leaving their individual contributions unclear. An executable world model is a persistent, agent-authored environment hypothesis embodied in runnable code. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15439:end -->

**为什么进入候选分母。** 摘要首要问题为“Our previous ARC-AGI-3 agent bundled executable world modeling, prompted simplification, and exact replay verification, leaving their individual contributions unclear.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** An executable world model is a persistent, agent-authored environment hypothesis embodied in runnable code.

**证据证明什么。** Because gpt-5.6-sol postdates the games and held-out performance is untested, results indicate public-set saturation only.

**证据没有证明什么。** Technical failure is not independent of performance: on the same game, a run in which the agent struggles will generally take longer than one in which it quickly discovers a solution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15439v1#S2 — 2 Study Design; https://arxiv.org/html/2607.15439v1#S3 — 3 Architecture and Agent Variants。Evaluation：https://arxiv.org/html/2607.15439v1#S4.SS2 — 4.2 Benchmark and evaluation design; https://arxiv.org/html/2607.15439v1#A1 — Appendix A Per-Game Results。Limitations / counterevidence：https://arxiv.org/html/2607.15439v1#A3.SS3 — C.3 Continuation, failure, stuck, and recovery prompts; https://arxiv.org/html/2607.15439v1#S4.SS4 — 4.4 All-or-nothing policy for irrecoverable failures。

**Artifact boundary。** Exact v1 links https://github.com/astroseger/arc-3-agents-baseline1, https://developers.openai.com/codex/cli, https://github.com/symbolica-ai/ARC-AGI-3-Agents/tree/symbolica/arcgentica; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Technical failure is not independent of performance: on the same game, a run in which the agent struggles will generally take longer than one in which it quickly discovers a solution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15439:end -->

<!-- review:SF-2026-ARXIV-2607-15456:start -->
### Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers

<!-- claim:SF-2026-ARXIV-2607-15456:start -->Looped, weight-tied Transformers reduce parameters by reusing a single block, but decoding still stores a separate K/V cache for every recurrence step. We show that this loop-indexed cache is highly structured. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15456:end -->

**为什么进入候选分母。** 摘要首要问题为“Looped, weight-tied Transformers reduce parameters by reusing a single block, but decoding still stores a separate K/V cache for every recurrence step.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We introduce Looped Latent Attention (\lla{}), a post-training cache codec that stores compact K and V latents and reconstructs loop-specific K/V vectors only when attention reads them.

**证据证明什么。** At matched cache budget, per-head \lla{} outperforms head-axis MLA, cross-layer sharing, KV quantization and final-loop reuse, showing that the recurrent cache is low-rank but not safely collapsible to a single state.

**证据没有证明什么。** More broadly, weight-tied iteration makes the cache, not the parameters, the quantity that grows with reasoning depth. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15456v1#A5 — Appendix E Design-ablation detail; https://arxiv.org/html/2607.15456v1#S5.SS0.SSS0.Px5 — Design ablations.。Evaluation：https://arxiv.org/html/2607.15456v1#A1 — Appendix A Experimental details; https://arxiv.org/html/2607.15456v1#A1.SS0.SSS0.Px4 — Evaluation suite and protocols.。Limitations / counterevidence：https://arxiv.org/html/2607.15456v1#S8 — 8 Discussion; https://arxiv.org/html/2607.15456v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：More broadly, weight-tied iteration makes the cache, not the parameters, the quantity that grows with reasoning depth.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15456:end -->

<!-- review:SF-2026-ARXIV-2607-15498:start -->
### VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs

<!-- claim:SF-2026-ARXIV-2607-15498:start -->The key-value (KV) cache is the main memory bottleneck in long-context large language model (LLM) inference. Two leading training-free families are both structurally limited: token-selection methods (SnapKV, Ada-KV) score importance from an observation window and evict low-scoring tokens, but eviction is irreversible -- so when the importance signal degrades under query-agnostic reuse, accuracy collapses by 11-15 points; uniform low-rank coding keeps every token but spends equal rank everywhere, wasting budget. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15498:end -->

**为什么进入候选分母。** 摘要首要问题为“The key-value (KV) cache is the main memory bottleneck in long-context large language model (LLM) inference.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present VarRate, a training-free KV codec that assigns each token a variable low-rank budget by its query salience, keeping every token at a nonzero rank.

**证据证明什么。** Against KVzip, a method purpose-built for query-agnostic reuse, it is accuracy-equivalent in three of four settings and within a point overall, at about one-eighth the prefill overhead.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15498v1#A1.SS18 — A.18 Does the Signal Generalize Past One Heuristic and One Model?; https://arxiv.org/html/2607.15498v1#A1.SS7 — A.7 A Third Model at Full Budget Sweep (Mistral-7B)。Evaluation：https://arxiv.org/html/2607.15498v1#A1 — Appendix A Additional Experiments and Analyses; https://arxiv.org/html/2607.15498v1#A1.SS12 — A.12 The Stride Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.15498v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15498:end -->

<!-- review:SF-2026-ARXIV-2607-15516:start -->
### Cache-Aware Prompt Compression:A Two-Tier Cost Model for LLM API Caching

<!-- claim:SF-2026-ARXIV-2607-15516:start -->Production LLM deployments combine two cost-reduction primitives: prompt caching (a discounted rate for re-used token prefixes) and prompt compression (fewer tokens sent). The compression literature has standardized on query-aware methods that produce a different compressed prefix per query, mechanically invalidating the prefix-strict cache on every call. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15516:end -->

**为什么进入候选分母。** 摘要首要问题为“Production LLM deployments combine two cost-reduction primitives: prompt caching (a discounted rate for re-used token prefixes) and prompt compression (fewer tokens sent).”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** The compression literature has standardized on query-aware methods that produce a different compressed prefix per query, mechanically invalidating the prefix-strict cache on every call.

**证据证明什么。** We validate CAPC on three production workloads: an enterprise tool-using assistant with a 94k-token schema prefix (51.7% cost reduction at r=3); a graphify knowledge-graph RAG pipeline across two codebases (9.3x vs cache-all on FastAPI, 2.4x on httpx); and the public tau-bench retail benchmark (50 tasks), where CAPC is the cheapest of four strategies with reward exactly equal to vanilla (both 36/50, p=1.00) while query-aware compression is the most expensive at +40.1% over vanilla -- the first production confirmation of the crossover model's negative-ROI prediction on a public benchmark.

**证据没有证明什么。** Conclusion This paper started from an observation a production engineer would recognize: prompt caching and prompt compression are not independent levers . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15516v1#S3.SS1 — has a two-tier architecture; https://arxiv.org/html/2607.15516v1#S2.SS1 — Prompt caching: from implementation to economic modeling。Evaluation：https://arxiv.org/html/2607.15516v1#S4 — Cost Model and Crossover Analysis; https://arxiv.org/html/2607.15516v1#S6 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.15516v1#S7 — Limitations and Future Work; https://arxiv.org/html/2607.15516v1#S8 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/safishamsi/graphify, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Conclusion This paper started from an observation a production engineer would recognize: prompt caching and prompt compression are not independent levers .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15516:end -->

<!-- review:SF-2026-ARXIV-2607-15524:start -->
### Recursive Harness Self-Improvement

<!-- claim:SF-2026-ARXIV-2607-15524:start -->Under model--harness co-evolution, harnesses are not merely inference-time scaffolds but data-generating components whose execution traces can shape future foundation models. This motivates harness-in-the-loop learning: optimizing harnesses for both immediate agent performance and the quality of traces used for future model training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15524:end -->

**为什么进入候选分母。** 摘要首要问题为“Under model--harness co-evolution, harnesses are not merely inference-time scaffolds but data-generating components whose execution traces can shape future foundation models.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To this end, we introduce Recursive Harness Self-Improvement (RHI), which represents the harness as a prompt-level specification of the agent loop and iteratively refines it using pairwise feedback over its own revision history.

**证据证明什么。** We show that these gains arise primarily from improved task-specific context management through more effective inter-agent information flow rather than longer reasoning traces.

**证据没有证明什么。** Future work will complete the second half of the loop by investigating how the resulting execution traces can be effectively internalized into future foundation models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15524v1#S2.SS2 — 2.2 Existing methods; https://arxiv.org/html/2607.15524v1#S3.SS2 — 3.2 RHI algorithm。Evaluation：https://arxiv.org/html/2607.15524v1#S4 — 4 Benchmark Evaluation; https://arxiv.org/html/2607.15524v1#S4.SS2 — 4.2 LLM-as-a-judge evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.15524v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://code.claude.com/docs/en/overview, https://code.claude.com/docs/en/sub-agents, https://code.claude.com/docs/en/skills; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future work will complete the second half of the loop by investigating how the resulting execution traces can be effectively internalized into future foundation models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15524:end -->

<!-- review:SF-2026-ARXIV-2607-15550:start -->
### SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction

<!-- claim:SF-2026-ARXIV-2607-15550:start -->Mobile graphical user interface (GUI) agents have demonstrated remarkable capabilities in automating complex tasks, yet they introduce critical safety risks because a single erroneous action can lead to irreversible consequences. Existing safety mechanisms are primarily reactive, lacking the ability to assess risks before execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15550:end -->

**为什么进入候选分母。** 摘要首要问题为“Mobile graphical user interface (GUI) agents have demonstrated remarkable capabilities in automating complex tasks, yet they introduce critical safety risks because a single erroneous action can lead to irreversible consequences.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we introduce SeerGuard, a consequence-aware safety framework designed to mitigate these risks through pre-execution instruction-level screening and action-level risk assessment.

**证据证明什么。** Extensive experiments demonstrate that SeerGuard generalizes effectively across diverse mobile GUI agents.

**证据没有证明什么。** Therefore, in our setting, adding safety guardrails does not increase end-to-end latency; instead, early risk interception yields a net runtime reduction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15550v1#S3 — 3 Framework of SeerGuard; https://arxiv.org/html/2607.15550v1#S5.SS1 — 5.1 SeerGuard Framework Evaluation。Evaluation：https://arxiv.org/html/2607.15550v1#A1.SS2 — A.2 Data Composition Analysis; https://arxiv.org/html/2607.15550v1#A2 — Appendix B Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.15550v1#S5.SS5 — 5.5 Discussion; https://arxiv.org/html/2607.15550v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3, https://huggingface.co/Qwen/Qwen3Guard-Stream-8B; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Therefore, in our setting, adding safety guardrails does not increase end-to-end latency; instead, early risk interception yields a net runtime reduction.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15550:end -->

<!-- review:SF-2026-ARXIV-2607-15557:start -->
### SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents

<!-- claim:SF-2026-ARXIV-2607-15557:start -->Agent skills, SKILL files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities. Public repositories now host them in large and growing numbers, yet these artifacts are fragmented, redundant, and uneven in quality, and their value in practice is unclear. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15557:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent skills, SKILL files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present SkillCorpus, a framework that aggregates, curates, matches, and evaluates the open skill ecosystem at scale.

**证据证明什么。** SkillCorpus is, to our knowledge, the first end-to-end account of when a curated, retrieval-served community corpus improves real agent tasks, and where it does not.

**证据没有证明什么。** The composite quality score serves deduplication tie-breaks and retrieval-time ranking rather than per-task prediction, and the active set is gated by safety and licence, not by a score threshold, with only a weak safety-facet signal (Appendix A.2 ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15557v1#S3.SS2 — 3.2 Three-facet quality framework。Evaluation：https://arxiv.org/html/2607.15557v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.15557v1#A2 — Appendix B Retrieval and Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.15557v1#S4.SS6 — 4.6 Discussion: where the pipeline helps, where it does not; https://arxiv.org/html/2607.15557v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/SKYLENAGE-AI/QwenClawBench, https://github.com/EverMind-AI/Raven, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The composite quality score serves deduplication tie-breaks and retrieval-time ranking rather than per-task prediction, and the active set is gated by safety and licence, not by a score threshold, with only a weak safety-facet signal (Appendix A.2 ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15557:end -->

<!-- review:SF-2026-ARXIV-2607-15589:start -->
### MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation

<!-- claim:SF-2026-ARXIV-2607-15589:start -->Communication-limited robots in mission-critical scenarios such as disaster inspection and search-and-rescue must make reliable onboard decisions without access to remote operators or high-capacity reasoning services. Episodic memory reuse is an attractive low-cost fallback, but retrieval similarity does not guarantee execution validity, i.e., a retrieved action may match the current context yet be unsafe due to changed topology, insufficient battery margin, or unreliable prior outcomes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15589:end -->

**为什么进入候选分母。** 摘要首要问题为“Communication-limited robots in mission-critical scenarios such as disaster inspection and search-and-rescue must make reliable onboard decisions without access to remote operators or high-capacity reasoning services.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Episodic memory reuse is an attractive low-cost fallback, but retrieval similarity does not guarantee execution validity, i.e., a retrieved action may match the current context yet be unsafe due to changed topology, insufficient battery margin, or unreliable prior outcomes.

**证据证明什么。** In a graph-based corridor-inspection simulator, MemoGuard reduces battery safety violations by 76.6% over similarity-only top-1 reuse while reducing fallback calls by 21.4% over always reasoning.

**证据没有证明什么。** V Conclusion and Future Work This paper presents MemoGuard , a lightweight runtime for contract-validated episodic memory reuse in communication-limited robot navigation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15589v1#S1 — I Introduction; https://arxiv.org/html/2607.15589v1#S2 — II Memory Traps and Problem Formulation。Evaluation：https://arxiv.org/html/2607.15589v1#S4 — IV Experiments and Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.15589v1#S5 — V Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：V Conclusion and Future Work This paper presents MemoGuard , a lightweight runtime for contract-validated episodic memory reuse in communication-limited robot navigation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15589:end -->

<!-- review:SF-2026-ARXIV-2607-15593:start -->
### Scalable LLM Agent Tool Access in the Cloud

<!-- claim:SF-2026-ARXIV-2607-15593:start -->LLM agents increasingly rely on tool calling to act on external systems, and the Model Context Protocol (MCP) has quickly become its de facto interface. Operating MCP at cloud scale, however, becomes difficult. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15593:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents increasingly rely on tool calling to act on external systems, and the Model Context Protocol (MCP) has quickly become its de facto interface.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present a cloud-scale gateway system for MCP service.

**证据证明什么。** On the agent side, the number of accessible tool is limited by the LLM context window and inference overhead; mounting a large tool set increases token usage and inference latency and can reduce task success rate.

**证据没有证明什么。** Conclusion Deploying MCP services at cloud scale is not a drop-in change, and traditional L7 load balancers cannot be directly applied to MCP. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15593v1#S3 — 3. System Design; https://arxiv.org/html/2607.15593v1#S2.SS4 — 2.4. Design Goals。Evaluation：https://arxiv.org/html/2607.15593v1#A2 — Appendix B API Services Analysis; https://arxiv.org/html/2607.15593v1#A7 — Appendix G Query Skewness Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.15593v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ravitemer/mcp-hub, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Conclusion Deploying MCP services at cloud scale is not a drop-in change, and traditional L7 load balancers cannot be directly applied to MCP.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15593:end -->

<!-- review:SF-2026-ARXIV-2607-15596:start -->
### From Neural Intent to Cryptographic Authorization: Securing AI-Driven Enterprise Workflows

<!-- claim:SF-2026-ARXIV-2607-15596:start -->The rapid adoption of artificial intelligence (AI)-driven workflows is transforming high-consequence government and enterprise systems into language-based, tool-using and increasingly autonomous infrastructures. While these workflows can delegate planning autonomously, security-critical execution should be strictly mediated. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15596:end -->

**为什么进入候选分母。** 摘要首要问题为“The rapid adoption of artificial intelligence (AI)-driven workflows is transforming high-consequence government and enterprise systems into language-based, tool-using and increasingly autonomous infrastructures.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose Neural Cryptographic Services (NCS), a neuro-symbolic security enforcement plane interposed between neural planners and privileged tools.

**证据证明什么。** NCS drives attack success rates to near zero while preserving acceptable utility on benign workflows.

**证据没有证明什么。** Under this paradigm, direct and indirect prompt injections may hijack the model’s internal reasoning, but they cannot forge execution rights for control actions outside the signed schedule. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15596v1#S5 — V Methodology; https://arxiv.org/html/2607.15596v1#S7 — VII Implementation and Evaluation。Evaluation：https://arxiv.org/html/2607.15596v1#S7.SS2 — VII-B Evaluation Results; https://arxiv.org/html/2607.15596v1#A1 — Appendix A Additional Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.15596v1#S9 — IX Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Under this paradigm, direct and indirect prompt injections may hijack the model’s internal reasoning, but they cannot forge execution rights for control actions outside the signed schedule.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15596:end -->

<!-- review:SF-2026-ARXIV-2607-15607:start -->
### ASK-NN: An Asymmetric Nearest-Neighbor Test that detects Distribution Drifts in Natural Language

<!-- claim:SF-2026-ARXIV-2607-15607:start -->Hallucinations and artificial text in LLM-generated outputs often appear as distributional deviations between prompt and response hidden-state distributions. Since prompts or retrieved contexts typically serve as reference samples and responses as query samples, with major differences in length, these asymmetries motivate the use of change test statistics that treat the two samples differently. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15607:end -->

**为什么进入候选分母。** 摘要首要问题为“Hallucinations and artificial text in LLM-generated outputs often appear as distributional deviations between prompt and response hidden-state distributions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Since prompts or retrieved contexts typically serve as reference samples and responses as query samples, with major differences in length, these asymmetries motivate the use of change test statistics that treat the two samples differently.

**证据证明什么。** Empirically, it is competitive with kernel and graph-based baselines on synthetic benchmarks, artificial-text detection, and LLM hallucination detection from token-level hidden states.

**证据没有证明什么。** Experiments on synthetic benchmarks, artificial-text detection, and LLM hallucination detection show that the proposed statistic is not only theoretically tractable and meaningful on controlled Gaussian alternatives, but also remains competitive on real embedding-based tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15607v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.15607v1#S4 — 4 Experiments; https://arxiv.org/html/2607.15607v1#S4.SS1 — 4.1 Baselines and evaluation protocol。Limitations / counterevidence：https://arxiv.org/html/2607.15607v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Experiments on synthetic benchmarks, artificial-text detection, and LLM hallucination detection show that the proposed statistic is not only theoretically tractable and meaningful on controlled Gaussian alternatives, but also remains competitive on real embedding-based tasks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15607:end -->

<!-- review:SF-2026-ARXIV-2607-15610:start -->
### Process Reward Informed Tree Rollout for Effective Multi-Turn RL

<!-- claim:SF-2026-ARXIV-2607-15610:start -->Reinforcement learning (RL) has become a key approach for training LLM agents, yet popular methods such as GRPO/RLOO rely on multiple independently sampled complete trajectories for advantage estimation. In long-horizon agentic tasks, such a uniform rollout strategy can waste budget on uninformative dead-end attempts, while promising intermediate states do not receive sufficient exploration. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15610:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning (RL) has become a key approach for training LLM agents, yet popular methods such as GRPO/RLOO rely on multiple independently sampled complete trajectories for advantage estimation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Process-Scorer Guided Adaptive Tree Rollout (PATR), a quality-aware rollout framework for multi-turn agent RL.

**证据证明什么。** Experiments show that PATR improves performance by up to +5.0 points on SWE-Bench and +9.3 points on FrozenLake, highlighting process-guided tree rollouts as an effective strategy for scalable multi-turn RL.

**证据没有证明什么。** Experiments on FrozenLake and SWE-Bench show consistent gains over independent-rollout and other rollout-generation baselines, with improvements of up to points on SWE-Bench and points on FrozenLake. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15610v1#A1 — Appendix A Additional Implementation Details。Evaluation：https://arxiv.org/html/2607.15610v1#S5 — 5 Experiments; https://arxiv.org/html/2607.15610v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.15610v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.15610v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Experiments on FrozenLake and SWE-Bench show consistent gains over independent-rollout and other rollout-generation baselines, with improvements of up to points on SWE-Bench and points on FrozenLake.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15610:end -->

<!-- review:SF-2026-ARXIV-2607-15621:start -->
### Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving

<!-- claim:SF-2026-ARXIV-2607-15621:start -->Large language models bring instruction following and scene reasoning to end-to-end driving, but their inference latency collides with the control rate a vehicle requires. Existing closed-loop agents hide this gap by invoking the model on alternate simulation ticks and replaying the previous command in between, so half of all control outputs ignore the newest observations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15621:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models bring instruction following and scene reasoning to end-to-end driving, but their inference latency collides with the control rate a vehicle requires.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present a fast-slow architecture that removes this compromise.

**证据证明什么。** It reduces open-loop waypoint error by nearly a factor of four compared to the backbone's own action head, at a per-tick model cost of 32 ms that is independent of history length on a single consumer GPU.

**证据没有证明什么。** 5 Conclusion Language models earn their place in a driving stack through understanding, and an architecture should not also demand reaction speed from the same component. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15621v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.15621v1#S4 — 4 Experiments; https://arxiv.org/html/2607.15621v1#S4.SS6 — 4.6 Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.15621v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：5 Conclusion Language models earn their place in a driving stack through understanding, and an architecture should not also demand reaction speed from the same component.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15621:end -->

<!-- review:SF-2026-ARXIV-2607-15650:start -->
### DiTango: Cost-Effective Parallel Diffusion Generation with Selective Attention State Reuse

<!-- claim:SF-2026-ARXIV-2607-15650:start -->Recent advances in AI-generated content have driven widespread adoption of Diffusion Transformers (DiTs) for high-resolution, long-duration content generation. While parallelization techniques accelerate diffusion inference, they face significant scalability challenges due to excessive communication overhead in multi-node environments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15650:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in AI-generated content have driven widespread adoption of Diffusion Transformers (DiTs) for high-resolution, long-duration content generation.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present DiTango, an efficient parallel framework for DiT generation.

**证据证明什么。** Experimental evaluation on popular diffusion models demonstrates that DiTango achieves up to 1.9x end-to-end and 3.2x attention speedup with near-linear scaling in multi-node settings, while maintaining generation quality comparable to state-of-the-art approaches.

**证据没有证明什么。** Despite these advancements, we acknowledge two current limitations of DiTango . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15650v1#S4.SS1 — 4.1. Error Modeling。Evaluation：https://arxiv.org/html/2607.15650v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.15650v1#S6.SS1 — 6.1. Evaluation Setup。Limitations / counterevidence：https://arxiv.org/html/2607.15650v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/thu-pacman/ChituDiffusion, https://github.com/vipshop/cache-dit.git, https://github.com/genmoai/models; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Despite these advancements, we acknowledge two current limitations of DiTango .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15650:end -->

<!-- review:SF-2026-ARXIV-2607-15655:start -->
### Adaptive Multi-Step Lookahead Decoding for Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-15655:start -->Masked diffusion language models (DLMs) enable parallel text generation by iteratively refining masked tokens, offering a promising alternative to autoregressive decoding. Recent lookahead-based decoding methods improve the accuracy--efficiency trade-off by exploring future decoding states before committing token updates. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15655:end -->

**为什么进入候选分母。** 摘要首要问题为“Masked diffusion language models (DLMs) enable parallel text generation by iteratively refining masked tokens, offering a promising alternative to autoregressive decoding.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Thus, in this work, we propose AdaLook, an adaptive lookahead framework for DLM decoding.

**证据证明什么。** Experiments on various benchmarks and models demonstrate that AdaLook achieves a better accuracy--decoding steps trade-off than existing one-step lookahead decoding methods.

**证据没有证明什么。** Consequently, although our method extends one-step lookahead to adaptive multi-step exploration, the rollout horizon may still remain insufficient to capture the long-range dependencies required for code generation, limiting the benefit of strategic lookahead. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15655v1#S4.SS1 — 4.1 General Framework; https://arxiv.org/html/2607.15655v1#A1 — Appendix A Algorithm。Evaluation：https://arxiv.org/html/2607.15655v1#A3 — Appendix C Additional Empirical Results for DREAM-v0-Instruct-7B; https://arxiv.org/html/2607.15655v1#S5 — 5 Empirical Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.15655v1#S5.SS4 — 5.4 Discussion on Code Generation Tasks; https://arxiv.org/html/2607.15655v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Consequently, although our method extends one-step lookahead to adaptive multi-step exploration, the rollout horizon may still remain insufficient to capture the long-range dependencies required for code generation, limiting the benefit of strategic lookahead.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15655:end -->

<!-- review:SF-2026-ARXIV-2607-15657:start -->
### Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents

<!-- claim:SF-2026-ARXIV-2607-15657:start -->Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15657:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel.

**证据证明什么。** We show that unconditional trust in visual data creates a critical vulnerability.

**证据没有证明什么。** Multimodal long-term memory systems must employ advanced defenses, including cross-modal consistency checks and adversarial robustness evaluation, to mitigate the threats presented by Lucid . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15657v1#S5 — 5 Lucid Design Framework; https://arxiv.org/html/2607.15657v1#A1 — Appendix A Lucid : Framework Details。Evaluation：https://arxiv.org/html/2607.15657v1#S7 — 7 Evaluation Results; https://arxiv.org/html/2607.15657v1#A2 — Appendix B Experimental Setup: Full Details。Limitations / counterevidence：https://arxiv.org/html/2607.15657v1#S4 — 4 Threat Model; https://arxiv.org/html/2607.15657v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Multimodal long-term memory systems must employ advanced defenses, including cross-modal consistency checks and adversarial robustness evaluation, to mitigate the threats presented by Lucid .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15657:end -->

<!-- review:SF-2026-ARXIV-2607-15660:start -->
### ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-15660:start -->While LLM agents demonstrate strong reasoning abilities in compact and well-defined scenarios, they struggle to maintain robustness and effectiveness when faced with large-scale, diverse, and dynamic real-world environments that demand seamless tool integration. To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15660:end -->

**为什么进入候选分母。** 摘要首要问题为“While LLM agents demonstrate strong reasoning abilities in compact and well-defined scenarios, they struggle to maintain robustness and effectiveness when faced with large-scale, diverse, and dynamic real-world environments that demand seamless tool integration.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks.

**证据证明什么。** Experimental results demonstrate that our framework significantly strengthens LLMs' capabilities in long-horizon tool use, achieving a marked performance boost and showcasing robust reasoning within dynamic environments.

**证据没有证明什么。** This could limit the diversity of emergent behaviors compared to environments where novel tool interactions can be discovered autonomously. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15660v1#S3 — 3 Method; https://arxiv.org/html/2607.15660v1#A2 — Appendix B Implementation Details。Evaluation：https://arxiv.org/html/2607.15660v1#A3 — Appendix C Related Experiments and Results; https://arxiv.org/html/2607.15660v1#A1 — Appendix A Theoretical Analysis of Turn-Aware Relative Advantage。Limitations / counterevidence：https://arxiv.org/html/2607.15660v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.15660v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：This could limit the diversity of emergent behaviors compared to environments where novel tool interactions can be discovered autonomously.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15660:end -->

<!-- review:SF-2026-ARXIV-2607-15684:start -->
### Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports

<!-- claim:SF-2026-ARXIV-2607-15684:start -->LLM agents span command-line interfaces (e.g., Codex) and agent frameworks (e.g., LangChain), integrating backend LLMs with harness code that parses model outputs, controls agent loops, and manages context. Both the harness and LLM-generated responses jointly shape an agent's execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15684:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents span command-line interfaces (e.g., Codex) and agent frameworks (e.g., LangChain), integrating backend LLMs with harness code that parses model outputs, controls agent loops, and manages context.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** LLM agents span command-line interfaces (e.g., Codex) and agent frameworks (e.g., LangChain), integrating backend LLMs with harness code that parses model outputs, controls agent loops, and manages context.

**证据证明什么。** Our findings show that many AR bugs manifest as silent errors without well-defined test oracles, which makes detection difficult.

**证据没有证明什么。** To reduce this threat, two annotators worked independently and resolved conflicting cases through discussion until consensus was reached. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15684v1#S7.SS2 — VII-B Testing and Debugging of AI Systems。Evaluation：https://arxiv.org/html/2607.15684v1#S4 — IV Study Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.15684v1#S5 — V Discussion; https://arxiv.org/html/2607.15684v1#S6 — VI Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：To reduce this threat, two annotators worked independently and resolved conflicting cases through discussion until consensus was reached.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15684:end -->

<!-- review:SF-2026-ARXIV-2607-15696:start -->
### PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval

<!-- claim:SF-2026-ARXIV-2607-15696:start -->Task decomposition aims to transform ambiguous instructions into executable atomic subtasks, thereby guiding high-precision tool retrieval. However, our analysis reveals that directly adopting tool retrieval metrics, i.e., Recall or NDCG, as rewards for task decomposition can easily induce reward hacking in reinforcement learning-based methods. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15696:end -->

**为什么进入候选分母。** 摘要首要问题为“Task decomposition aims to transform ambiguous instructions into executable atomic subtasks, thereby guiding high-precision tool retrieval.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address this issue, we propose PCTD, a Preference-guided Counterfactual Task Decomposition framework.

**证据证明什么。** Extensive experiments demonstrate that PCTD alleviates repetitive decomposition and surpasses SOTA methods in retrieval, decomposition quality, and OOD generalization.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15696v1#A1.SS2 — A.2 Prompting Methods; https://arxiv.org/html/2607.15696v1#A1.SS3 — A.3 RL-Based Method。Evaluation：https://arxiv.org/html/2607.15696v1#A3.SS2 — C.2 Analysis of GSB Evaluation Results; https://arxiv.org/html/2607.15696v1#S4.SS1 — 4.1 Evaluation Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.15696v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/MagicAgent-Search/PCTD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15696:end -->

<!-- review:SF-2026-ARXIV-2607-15714:start -->
### AC-VLA: Robust Out-of-Distribution Action Execution via Compositional Learning

<!-- claim:SF-2026-ARXIV-2607-15714:start -->Vision-Language-Action (VLA) models excel at end-to-end robotic manipulation but struggle with out-of-distribution (OOD) generalization when familiar sub-tasks are recombined in unseen configurations. We identify two mutually reinforcing failure modes: \emph{trajectory overfitting}, where models overfit to holistic trajectory patterns rather than compositional sub-skill semantics; and \emph{perceptual shortcut}, where action tokens over-rely on wrist-view textures at the expense of global spatial grounding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15714:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models excel at end-to-end robotic manipulation but struggle with out-of-distribution (OOD) generalization when familiar sub-tasks are recombined in unseen configurations.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address both, we introduce \textbf{AC-VLA}, a plug-and-play Action Compositional learning framework comprising two architecture-agnostic components: \textbf{(i)} a compositional learning module that uses an LLM-driven instruction decomposer and a proprioceptive trajectory aligner to generate dense sub-task supervision, followed by mixed training on complete demonstrations and decomposed data to endow the model with compositional generalization; and \textbf{(ii)} a state-conditioned asymmetric masking strategy that suppresses wrist-view inputs during closed-gripper phases, enforcing global semantic grounding.

**证据证明什么。** Instantiated on $π_{0.5}$ and evaluated on LIBERO and LIBERO-OOD benchmarks, AC-VLA achieves a ~28% absolute improvement on compositional OOD tasks while maintaining near-perfect in-distribution performance.

**证据没有证明什么。** 6 Limitations While AC-VLA achieves strong compositional generalization, it also has some limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15714v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.15714v1#S4 — 4 Experiments; https://arxiv.org/html/2607.15714v1#S4.SS1 — 4.1 Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.15714v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.15714v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：6 Limitations While AC-VLA achieves strong compositional generalization, it also has some limitations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15714:end -->

<!-- review:SF-2026-ARXIV-2607-15715:start -->
### Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents

<!-- claim:SF-2026-ARXIV-2607-15715:start -->Large language model (LLM) agents are increasingly used for complex information-extraction tasks, yet it remains unclear whether agentic components such as reflection and memory lead to observable and controllable improvements over fixed LLM workflows. We study this question through conference-paper dataset extraction, where a system must identify datasets mentioned in scholarly PDFs and produce structured records. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15715:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents are increasingly used for complex information-extraction tasks, yet it remains unclear whether agentic components such as reflection and memory lead to observable and controllable improvements over fixed LLM workflows.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We study this question through conference-paper dataset extraction, where a system must identify datasets mentioned in scholarly PDFs and produce structured records.

**证据证明什么。** The paper characterizes when agentic mechanisms change system behavior, whether these changes improve task completion, and how the observed failure modes motivate an optimized agent design under the same evaluation harness.

**证据没有证明什么。** Limitations and Threats to Validity The study has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15715v1#S4 — 4 System Design; https://arxiv.org/html/2607.15715v1#S3 — 3 Task and Experimental Framework。Evaluation：https://arxiv.org/html/2607.15715v1#S5.SSx5 — Ablations and Statistical Analysis; https://arxiv.org/html/2607.15715v1#S6.SSx4 — Ablation Results。Limitations / counterevidence：https://arxiv.org/html/2607.15715v1#S7.SSx4 — Limitations and Threats to Validity; https://arxiv.org/html/2607.15715v1#S7 — 7 Analysis and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations and Threats to Validity The study has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15715:end -->

<!-- review:SF-2026-ARXIV-2607-15718:start -->
### Verified LLM-Driven Synthesis for Concept Design

<!-- claim:SF-2026-ARXIV-2607-15718:start -->Concept Design structures software systems around concepts: user-facing, self-contained units of functionality with a focused purpose. Concepts are composed into applications using synchronization rules called reactions, which specify how actions in one concept trigger actions in others. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15718:end -->

**为什么进入候选分母。** 摘要首要问题为“Concept Design structures software systems around concepts: user-facing, self-contained units of functionality with a focused purpose.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Concept Design structures software systems around concepts: user-facing, self-contained units of functionality with a focused purpose.

**证据证明什么。** In an evaluation on three applications and twelve design variants using one LLM configuration, invariant-only synthesis reached verified designs quickly but often produced inconsistent designs across runs, some of which were implausible, showing that invariants alone underconstrain the design task.

**证据没有证明什么。** Correctness failures are counted over all scenario-guided synthesis runs, while quality failures are counted only for the successful runs that produced the intended design. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15718v1#S3 — 3 Formal Verification of Concept Designs; https://arxiv.org/html/2607.15718v1#S5.SS2 — 5.2 Efficiency of Design Verification。Evaluation：https://arxiv.org/html/2607.15718v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.15718v1#S5.SS1 — 5.1 Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.15718v1#S5.SS6 — 5.6 Failure modes; https://arxiv.org/html/2607.15718v1#S5.SS7 — 5.7 Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/alcinocunha/foundry, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Correctness failures are counted over all scenario-guided synthesis runs, while quality failures are counted only for the successful runs that produced the intended design.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15718:end -->

<!-- review:SF-2026-ARXIV-2607-15772:start -->
### SlotMem: Character-Addressable Internal Memory for Narrative Long Video Generation

<!-- claim:SF-2026-ARXIV-2607-15772:start -->Maintaining recurring character identities across scene transitions and long temporal gaps is a central challenge in narrative long video generation. Methods targeting global consistency often retrieve memory using cues that are not aligned with character identity preservation, while recent character-centric variants still rely on coarse frame-level kv memory that entangles identity with incidental visual factors and lacks a continuous update mechanism under limited memory capacity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15772:end -->

**为什么进入候选分母。** 摘要首要问题为“Maintaining recurring character identities across scene transitions and long temporal gaps is a central challenge in narrative long video generation.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address these limitations, we propose SlotMem, a character-addressable internal memory framework for multi-character narrative long video generation.

**证据证明什么。** Experiments on multiple narrative long video generation benchmarks show that SlotMem improves long-range character consistency over existing baselines, while maintaining comparable video quality.

**证据没有证明什么。** Instead of relying on coarse frame-level retrieval, SlotMem represents recurring characters with compact role-wise memory that can be updated across autoregressive video generation and injected only into character-relevant regions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15772v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.15772v1#A2 — Appendix B Additional Experimental Settings; https://arxiv.org/html/2607.15772v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.15772v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.15772v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/YilaiLiu-HKU/SlotMem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Instead of relying on coarse frame-level retrieval, SlotMem represents recurring characters with compact role-wise memory that can be updated across autoregressive video generation and injected only into character-relevant regions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15772:end -->

<!-- review:SF-2026-ARXIV-2607-15778:start -->
### Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding

<!-- claim:SF-2026-ARXIV-2607-15778:start -->Video Large Language Models (Video LLMs) have made significant advancements in various video understanding tasks. However, long-video scenarios remain challenging due to the tension between limited visual token budgets and the need to capture multiple key events. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15778:end -->

**为什么进入候选分母。** 摘要首要问题为“Video Large Language Models (Video LLMs) have made significant advancements in various video understanding tasks.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To tackle these challenges, we propose MoD-VLLM, a novel Modularized Dynamic-Granularity Video LLM framework for multi-event long video understanding, which unifies temporal grounding and semantic understanding iteratively and self-reflectively.

**证据证明什么。** Extensive experiments on several long video understanding benchmarks and our MEventBench demonstrate that MoD-VLLM significantly outperforms state-of-the-art baselines.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15778v1#S3 — III Method。Evaluation：https://arxiv.org/html/2607.15778v1#S4 — IV Experiment; https://arxiv.org/html/2607.15778v1#S4.SS1 — IV-A Main Result on Long Video Understanding。Limitations / counterevidence：https://arxiv.org/html/2607.15778v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15778:end -->

<!-- review:SF-2026-ARXIV-2607-15808:start -->
### Examining the Associations between Visual and Non-Visual Elements and Cyclists' Route Choices for Various Trip Purposes

<!-- claim:SF-2026-ARXIV-2607-15808:start -->Understanding cyclist preferences for the characteristics of the built environment is important in promoting sustainable urban transportation and active mobility. Despite previous studies on cyclists' route choices, the influence of visual and non-visual factors on these choices for different trip purposes remains unclear; thus, this paper fills this gap through a data-driven case study in Montreal, Canada. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15808:end -->

**为什么进入候选分母。** 摘要首要问题为“Understanding cyclist preferences for the characteristics of the built environment is important in promoting sustainable urban transportation and active mobility.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Despite previous studies on cyclists' route choices, the influence of visual and non-visual factors on these choices for different trip purposes remains unclear; thus, this paper fills this gap through a data-driven case study in Montreal, Canada.

**证据证明什么。** These insights can inform the planning of street networks and the development of infrastructure to improve the use of active transportation.

**证据没有证明什么。** The relative novelty of bicycle track data acquisition services presents another limitation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15808v1#S3 — 3 Data and methods; https://arxiv.org/html/2607.15808v1#S3.SS4 — 3.4 Methods。Evaluation：https://arxiv.org/html/2607.15808v1#S4 — 4 Results; https://arxiv.org/html/2607.15808v1#S4.SS1 — 4.1 Origin and destination analysis。Limitations / counterevidence：https://arxiv.org/html/2607.15808v1#S5 — 5 Discussions; https://arxiv.org/html/2607.15808v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The relative novelty of bicycle track data acquisition services presents another limitation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15808:end -->

<!-- review:SF-2026-ARXIV-2607-15846:start -->
### DSTAR: Accelerating Diffusion Transformers via Spatial and Temporal Redundancy Reduction

<!-- claim:SF-2026-ARXIV-2607-15846:start -->Diffusion Transformers (DiTs) have been widely used in many tasks, including image synthesis, video generation, and content editing. However, their multi-iteration inference process leads to performance inefficiency and high energy consumption. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15846:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion Transformers (DiTs) have been widely used in many tasks, including image synthesis, video generation, and content editing.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present DSTAR, a software-hardware co-design framework that accelerates DiT inference by reducing spatial and temporal redundancy.

**证据证明什么。** Evaluation on seven typical DiTs demonstrates that DSTAR achieves up to 7.33x latency speedup and 41.89x energy savings compared to an NVIDIA A100 GPU, and achieves up to 2.54x latency speedup and 3.68x energy savings compared to SOTA accelerators, without accuracy degradation.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15846v1#S4 — 4. Hardware Architecture; https://arxiv.org/html/2607.15846v1#S5.SS3 — 5.3. Architecture Evaluation。Evaluation：https://arxiv.org/html/2607.15846v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.15846v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.15846v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/openai/triton, https://github.com/boomb0om/text2image-benchmark; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15846:end -->

<!-- review:SF-2026-ARXIV-2607-15865:start -->
### An MLIR-Based Compilation Method for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-15865:start -->Large Language Models (LLMs) have become the dominant workload on modern AI accelerators, yet deploying them on specialized hardware still faces two core challenges: how to import a trained model into a compiler-friendly intermediate representation, and how to efficiently schedule the autoregressive inference loop under limited on-chip memory. This paper presents an MLIR (Multi-Level Intermediate Representation) based compilation method for large language models, illustrated using two dialects of operators, TopOp and TpuOp. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15865:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) have become the dominant workload on modern AI accelerators, yet deploying them on specialized hardware still faces two core challenges: how to import a trained model into a compiler-friendly intermediate representation, and how to efficiently schedule the autoregressive inference loop under limited on-chip memory.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** This paper presents an MLIR (Multi-Level Intermediate Representation) based compilation method for large language models, illustrated using two dialects of operators, TopOp and TpuOp.

**证据证明什么。** The method has been implemented in the TPU-MLIR compiler {https://github.com/sophgo/tpu-mlir} and the LLM-TPU deployment project {https://github.com/sophgo/LLM-TPU}, supporting a variety of generative models including the Qwen, Llama, InternVL, and MiniCPM-V series, as well as multiple quantization and deployment forms such as GPTQ, AWQ, and AutoRound.

**证据没有证明什么。** The following design decisions are worth emphasizing: • Framework independence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15865v1#S3 — 3 Building Large Models with TopOp; https://arxiv.org/html/2607.15865v1#S3.SS1 — 3.1 Model Import and TopOp Module Generation。Evaluation：https://arxiv.org/html/2607.15865v1#S1 — 1 Introduction; https://arxiv.org/html/2607.15865v1#S2 — 2 Background。Limitations / counterevidence：https://arxiv.org/html/2607.15865v1#S5 — 5 Discussion; https://arxiv.org/html/2607.15865v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/docs/transformers, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The following design decisions are worth emphasizing: • Framework independence.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15865:end -->

<!-- review:SF-2026-ARXIV-2607-15875:start -->
### Scientific Claim-Source Retrieval Revisited: A Comparative Study of Style Transfer and Re-Ranking

<!-- claim:SF-2026-ARXIV-2607-15875:start -->Scientific claims shared on social media are often difficult to verify and may contribute to the spread of misinformation. To address this challenge, automated fact verification systems require scientific claim-source retrieval, the task of identifying the source publication underlying a given claim. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15875:end -->

**为什么进入候选分母。** 摘要首要问题为“Scientific claims shared on social media are often difficult to verify and may contribute to the spread of misinformation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present a comparative study of scientific claim-source retrieval on the CheckThat!

**证据证明什么。** Our results show that translating claims into English outperforms both original and bilingual claim representations, while incorporating publication metadata provides additional retrieval gains by capturing indirect source references.

**证据没有证明什么。** However, such improvements come at substantially higher computational cost, as LLM-based verification requires expensive reasoning even when applied only to a small set of top-ranked candidates. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15875v1#S3.SS2 — 3.2 Retrieval Models。Evaluation：https://arxiv.org/html/2607.15875v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.15875v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.15875v1#S6 — 6 Discussion; https://arxiv.org/html/2607.15875v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/faerber-lab/CheckThat2026, https://dx.doi.org/10.18653/v1/2021.naacl-demos.10, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, such improvements come at substantially higher computational cost, as LLM-based verification requires expensive reasoning even when applied only to a small set of top-ranked candidates.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15875:end -->

<!-- review:SF-2026-ARXIV-2607-15893:start -->
### Induction in Both Directions: A Mechanistic Analysis of In-Context Learning in Masked Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-15893:start -->While the internal mechanisms of autoregressive (AR) transformers have been studied extensively, much less is known about diffusion language models (DLMs), an emerging alternative that generates text by iterative denoising. In this work, we study how DLMs implement induction, a mechanism behind in-context learning in which the model finds a repeated context and copies the token that followed it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15893:end -->

**为什么进入候选分母。** 摘要首要问题为“While the internal mechanisms of autoregressive (AR) transformers have been studied extensively, much less is known about diffusion language models (DLMs), an emerging alternative that generates text by iterative denoising.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this work, we study how DLMs implement induction, a mechanism behind in-context learning in which the model finds a repeated context and copies the token that followed it.

**证据证明什么。** When only left context is visible, matching what an AR model sees, the DLM does not outperform its AR counterpart in induction capabilities.

**证据没有证明什么。** 5 Limitations We analyze small attention-only transformers and their folded no-LayerNorm variants. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15893v1#S3 — 3 Method; https://arxiv.org/html/2607.15893v1#S3.SS1 — 3.1 Matched Autoregressive and Diffusion Models。Evaluation：https://arxiv.org/html/2607.15893v1#S3.SS3 — 3.3 Circuit Analysis; https://arxiv.org/html/2607.15893v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.15893v1#S5 — 5 Limitations; https://arxiv.org/html/2607.15893v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/TransformerLensOrg/TransformerLens, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Limitations We analyze small attention-only transformers and their folded no-LayerNorm variants.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15893:end -->

<!-- review:SF-2026-ARXIV-2607-15898:start -->
### Orbis 2: A Hierarchical World Model for Driving

<!-- claim:SF-2026-ARXIV-2607-15898:start -->Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks. We present a hierarchical driving world model that factorizes future prediction across two levels operating at distinct temporal and abstraction scales: a high-level predictor that forecasts coarse scene structure over extended temporal horizons, and a low-level generator that produces detailed predictions conditioned on the high-level output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15898:end -->

**为什么进入候选分母。** 摘要首要问题为“Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present a hierarchical driving world model that factorizes future prediction across two levels operating at distinct temporal and abstraction scales: a high-level predictor that forecasts coarse scene structure over extended temporal horizons, and a low-level generator that produces detailed predictions conditioned on the high-level output.

**证据证明什么。** Our approach achieves state-of-the-art results across the standard suite of driving world model evaluations on established benchmarks, including long-horizon generation fidelity, steering responsiveness evaluated on counterfactual scenarios, and internal representation quality.

**证据没有证明什么。** We do not study these factors separately in this work, and leave a more detailed analysis of noise schedules and corruption patterns to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15898v1#S3 — 3 Method; https://arxiv.org/html/2607.15898v1#S4.SS2 — 4.2 Model design。Evaluation：https://arxiv.org/html/2607.15898v1#A1.SS1 — A.1 Class-wise semantic segmentation probing results; https://arxiv.org/html/2607.15898v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.15898v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/natix-network-org/natix-multi-camera-driving-dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：We do not study these factors separately in this work, and leave a more detailed analysis of noise schedules and corruption patterns to future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15898:end -->

<!-- review:SF-2026-ARXIV-2607-15899:start -->
### ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing

<!-- claim:SF-2026-ARXIV-2607-15899:start -->In production large language model (LLM) deployments, high API availability guarantees do not equate to conversational continuity. When a primary provider experiences an outage or strict rate-limiting, naive stateless failover mechanisms successfully maintain uptime but silently discard conversation history, severely disrupting the user experience. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15899:end -->

**为什么进入候选分母。** 摘要首要问题为“In production large language model (LLM) deployments, high API availability guarantees do not equate to conversational continuity.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Our results provide a principled foundation for building robust, state-preserving multi-model inference systems.

**证据证明什么。** Our empirical evaluation ($N=750$ failover events) demonstrates that our stateful proxy achieves a 99.20\% CPR [95\% CI: 98.27\%, 99.63\%], cleanly transferring deep conversational context to fallback providers, compared to a near-0\% preservation rate for standard stateless architectures.

**证据没有证明什么。** 7 Limitations While our empirical findings demonstrate the efficacy of the History-Forwarding strategy, our methodology entails several limitations that constrain the generalizability of the results and suggest directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15899v1#S3 — 3 System Design; https://arxiv.org/html/2607.15899v1#A1 — Appendix A LLM Judge System Prompt。Evaluation：https://arxiv.org/html/2607.15899v1#A2 — Appendix B Extended Results: Per-Run CPR Stability; https://arxiv.org/html/2607.15899v1#S2.SS2 — 2.2 LLM Evaluation and LLM-as-Judge。Limitations / counterevidence：https://arxiv.org/html/2607.15899v1#S6 — 6 Discussion and Systems Failure Modes; https://arxiv.org/html/2607.15899v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Vishal-sys-code/continuity-bench, https://github.com/ray-project/llmperf, https://github.com/BerriAI/litellm; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：7 Limitations While our empirical findings demonstrate the efficacy of the History-Forwarding strategy, our methodology entails several limitations that constrain the generalizability of the results and suggest directions for future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GATEWAY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15899:end -->

<!-- review:SF-2026-ARXIV-2607-15901:start -->
### DSWorld: A Data Science World Model for Efficient Autonomous Agents

<!-- claim:SF-2026-ARXIV-2607-15901:start -->Despite strong capabilities in data understanding and decision-making, autonomous data science agents still heavily rely on trial-and-error workflows that involve expensive computation. This bottleneck motivates models that can anticipate the effects of data science operations before real execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15901:end -->

**为什么进入候选分母。** 摘要首要问题为“Despite strong capabilities in data understanding and decision-making, autonomous data science agents still heavily rely on trial-and-error workflows that involve expensive computation.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We further propose DSWorld, a practical framework that combines structured state construction, cost-aware routing, lightweight real execution, and an LLM-based simulator for expensive operations.

**证据证明什么。** Experiments show that DSWorld accelerates RL-based agent training by approximately $14\times$ and search-based inference by approximately $3$-$6\times$ while maintaining competitive performance, and outperforms the strongest LLM baseline by 35.6% on transition prediction tasks.

**证据没有证明什么。** Limitations Despite the promising results, this work still has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15901v1#S4 — 4 Methodology; https://arxiv.org/html/2607.15901v1#A1.SS3 — A.3 Implementation Details.。Evaluation：https://arxiv.org/html/2607.15901v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.15901v1#A1.SS1 — A.1 Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.15901v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.15901v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/microsoft/harrier-oss-v1-0.6b, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations Despite the promising results, this work still has several limitations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15901:end -->

<!-- review:SF-2026-ARXIV-2607-15937:start -->
### The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs

<!-- claim:SF-2026-ARXIV-2607-15937:start -->Large Language Models (LLMs) are increasingly used for source code generation despite their outputs often exhibiting security vulnerabilities. Prior work shows that prompt engineering can mitigate such risks, yet (1) they focused on high-level prompting strategies, neglecting recent evidence that fine-grained syntactic variations can substantially alter model behavior; and (2) predominantly evaluate proprietary LLMs, limiting the applicability of their findings in industrial settings where self-hosted, open models are preferred for privacy, compliance, and deployment control. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15937:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are increasingly used for source code generation despite their outputs often exhibiting security vulnerabilities.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Using a parser-driven approach, we systematically generate syntactic variants of security-relevant code generation prompts and evaluate their impact on code security across multiple open LLMs and programming languages.

**证据证明什么。** Our results show that specific syntactic elements, such as constraints, guards, conditions, and concept bindings, and their position within the prompt consistently affect the likelihood of generating insecure code.

**证据没有证明什么。** This implies that prompt-level security is inherently fragile and cannot be assumed to transfer across paraphrases of the same underlying request. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15937v1#S3 — III Research Method。Evaluation：https://arxiv.org/html/2607.15937v1#S4 — IV Empirical Evaluation Results; https://arxiv.org/html/2607.15937v1#S3.SS3 — III-C Vulnerability Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.15937v1#S5 — V Discussion and Implications; https://arxiv.org/html/2607.15937v1#S5.SS1 — V-A Discussion。

**Artifact boundary。** Exact v1 links https://codeql.github.com/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This implies that prompt-level security is inherently fragile and cannot be assumed to transfer across paraphrases of the same underlying request.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15937:end -->

<!-- review:SF-2026-ARXIV-2607-15970:start -->
### Code-Poisoning Property Inference Attacks

<!-- claim:SF-2026-ARXIV-2607-15970:start -->The flourishing code hosting platforms and coding agents enable even beginners with private data to build tailored Machine Learning (ML) models using available code quickly. The training data for ML models, often regarded as private property (e.g., clinical records, transaction information), is at significant risk of information leakage. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15970:end -->

**为什么进入候选分母。** 摘要首要问题为“The flourishing code hosting platforms and coding agents enable even beginners with private data to build tailored Machine Learning (ML) models using available code quickly.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we present Code-Poisoning Property Inference Attack (CPPIA), the first code-level PIA, which overcomes four limitations of existing works: insufficient attack performance, severe degradation of model accuracy, high computational overhead, and failure under defenses.

**证据证明什么。** We evaluate the attack performance across four datasets, eight model architectures, eighteen properties, and under three defense mechanisms, demonstrating the universality and effectiveness of CPPIA.

**证据没有证明什么。** However, identifying malicious logic within complex codebases is non-trivial. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15970v1#S4 — IV Methodology; https://arxiv.org/html/2607.15970v1#S4.SS1 — IV-A Design Goals。Evaluation：https://arxiv.org/html/2607.15970v1#S5 — V Evaluation; https://arxiv.org/html/2607.15970v1#S5.SS1 — V-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.15970v1#S7 — VII Conclusion and Future Works; https://arxiv.org/html/2607.15970v1#S3 — III Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/Zili1000/CPPIA, https://github.com/, https://github.com/openai/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：However, identifying malicious logic within complex codebases is non-trivial.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15970:end -->

<!-- review:SF-2026-ARXIV-2607-15977:start -->
### Refusal is Not Safety! Benchmarking Latent Safety Risks of LLM-Driven Content Humorization

<!-- claim:SF-2026-ARXIV-2607-15977:start -->Safety defenses for large language models (LLMs) have been extensively studied, with existing approaches focusing on attack detection and refusal mechanisms. Such fixed-form direct refusal strategies may introduce the risk of prefix injection attacks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15977:end -->

**为什么进入候选分母。** 摘要首要问题为“Safety defenses for large language models (LLMs) have been extensively studied, with existing approaches focusing on attack detection and refusal mechanisms.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Motivated by these findings, we propose \textsc{HumorSafe}, a novel framework for evaluating latent safety risk propagation during humorization. \textsc{HumorSafe} enables LLMs to learn harmful humorization patterns and use them to transform benign content into humorous content with safety risks.

**证据证明什么。** Across five frontier LLMs, we find that LLMs can introduce stereotypes and toxicity during humorization.

**证据没有证明什么。** The attack surface is not limited to standalone LLMs and can further extend to LLM agents. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15977v1#Sx4 — Methodology。Evaluation：https://arxiv.org/html/2607.15977v1#Sx10 — Additional Experimental Results; https://arxiv.org/html/2607.15977v1#Sx4.SSx2 — HumorSafe Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.15977v1#Sx6 — Discussion; https://arxiv.org/html/2607.15977v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The attack surface is not limited to standalone LLMs and can further extend to LLM agents.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15977:end -->

<!-- review:SF-2026-ARXIV-2607-16010:start -->
### AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation

<!-- claim:SF-2026-ARXIV-2607-16010:start -->Governments are increasingly mandating that LLM-generated content carry watermarks. The EU AI Act calls for markings that are "sufficiently reliable and robust." California's SB 942 requires disclosure that is "permanent or extraordinarily difficult to remove." Both mandates rest on an untested assumption: that watermark detection yields evidence reliable enough for courts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16010:end -->

**为什么进入候选分母。** 摘要首要问题为“Governments are increasingly mandating that LLM-generated content carry watermarks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To structure this evaluation, we propose a Forensic Readiness Score (FRS) framework with 12 criteria, three mandatory gates, and a 60-point scoring system.

**证据证明什么。** The results raise serious evidentiary concerns.

**证据没有证明什么。** Limitations and Future Work Model scale and families. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16010v1#Sx2.SSx1 — LLM Watermarking Methods; https://arxiv.org/html/2607.16010v1#Sx3 — The Forensic Readiness Score Framework。Evaluation：https://arxiv.org/html/2607.16010v1#Sx4 — Experimental Setup; https://arxiv.org/html/2607.16010v1#Sx4.SSx3 — Experimental Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.16010v1#Sx7 — Limitations and Future Work; https://arxiv.org/html/2607.16010v1#Sx5.SSx1 — Pre-Attack Baseline Failure。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations and Future Work Model scale and families.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16010:end -->

<!-- review:SF-2026-ARXIV-2607-16019:start -->
### Presentation, Not Mechanism: A Render Confound in Deprecation-Aware Memory Evaluation

<!-- claim:SF-2026-ARXIV-2607-16019:start -->AI systems increasingly retrieve from records that revise themselves: issue threads, encyclopedic histories, policy logs, and long conversations. The challenge is not only finding relevant evidence, but deciding which claims remain in force, which were superseded, and when to abstain. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16019:end -->

**为什么进入候选分母。** 摘要首要问题为“AI systems increasingly retrieve from records that revise themselves: issue threads, encyclopedic histories, policy logs, and long conversations.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Memory evaluations should hold render fixed, and deprecation-aware systems should deploy the coarsest retained state that covers their queries.

**证据证明什么。** Memory evaluations should hold render fixed, and deprecation-aware systems should deploy the coarsest retained state that covers their queries.

**证据没有证明什么。** The natural cross-family check—an independently implemented graph memory tested against a ledger under a render-matched control—remains future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16019v1#S1 — 1 Introduction; https://arxiv.org/html/2607.16019v1#S2 — 2 Evidence-State Revision。Evaluation：https://arxiv.org/html/2607.16019v1#S4 — 4 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.16019v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16019v1#Sx2 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Anonymous-Awesome-Submissions/ESR-pipeline, https://github.com/Anonymous-Awesome-Submissions/ESR-bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The natural cross-family check—an independently implemented graph memory tested against a ledger under a render-matched control—remains future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16019:end -->

<!-- review:SF-2026-ARXIV-2607-16024:start -->
### DiffTestGen: Change-Directed LLM-Based Testing for Exposing Behavioral Differences

<!-- claim:SF-2026-ARXIV-2607-16024:start -->As software evolves over time, it is important to ensure that any behavioral changes occur as intended by developers. A promising approach for this goal is to generate tests that expose behavioral differences between the old and new versions of a program. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16024:end -->

**为什么进入候选分母。** 摘要首要问题为“As software evolves over time, it is important to ensure that any behavioral changes occur as intended by developers.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** A promising approach for this goal is to generate tests that expose behavioral differences between the old and new versions of a program.

**证据证明什么。** By integrating DiffTestGen with the Testora regression detector, we show that the identified behavioral differences can be used to detect regression bugs missed by the best existing approaches.

**证据没有证明什么。** Finally, our datasets are drawn from prior work and cover a limited set of projects, so effectiveness may vary for projects with different API conventions, testing practices, or dependency environments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16024v1#S2 — II Approach。Evaluation：https://arxiv.org/html/2607.16024v1#S2.SS3 — II-C Analysis of Code Change and Access Information; https://arxiv.org/html/2607.16024v1#S3 — III Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16024v1#S4 — IV Threats to Validity; https://arxiv.org/html/2607.16024v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/sola-st/DiffTestGen, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Finally, our datasets are drawn from prior work and cover a limited set of projects, so effectiveness may vary for projects with different API conventions, testing practices, or dependency environments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16024:end -->

<!-- review:SF-2026-ARXIV-2607-16062:start -->
### When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis

<!-- claim:SF-2026-ARXIV-2607-16062:start -->Model merging is promoted as a substitute for joint multi-task training, yet in the reinforcement-learning setting this substitution is essentially never tested against the baseline it claims to replace: methods merge independently released agents precisely because a joint model is unavailable. Training difficulty-1 and difficulty-2 Qwen3-8B specialists on the AppWorld agent benchmark with LOOP, we merge them (TIES, RAM+) and pit the result against a jointly trained model on the same data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16062:end -->

**为什么进入候选分母。** 摘要首要问题为“Model merging is promoted as a substitute for joint multi-task training, yet in the reinforcement-learning setting this substitution is essentially never tested against the baseline it claims to replace: methods merge independently released agents precisely because a joint model is unavailable.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Model merging is promoted as a substitute for joint multi-task training, yet in the reinforcement-learning setting this substitution is essentially never tested against the baseline it claims to replace: methods merge independently released agents precisely because a joint model is unavailable.

**证据证明什么。** Because direction and support are decoupled, support and sign-based merging (RAM, TIES) collapse to near-uniform averaging.

**证据没有证明什么。** In our regime this cannot help, and the reason is instructive. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16062v1#S2.SS4 — 2.4 Statistical and geometric methodology; https://arxiv.org/html/2607.16062v1#S2.SS3 — 2.3 Model merging: TIES and RAM。Evaluation：https://arxiv.org/html/2607.16062v1#S4 — 4 Experimental setup; https://arxiv.org/html/2607.16062v1#S4.SS1 — 4.1 Benchmark and metrics。Limitations / counterevidence：https://arxiv.org/html/2607.16062v1#S6 — 6 Discussion; https://arxiv.org/html/2607.16062v1#S7 — 7 Future work: merge-aware checkpoint early stopping。

**Artifact boundary。** Exact v1 links https://github.com/magicsquares137/maml-agent, https://github.com/magicsquares137/appworld-rl, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In our regime this cannot help, and the reason is instructive.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16062:end -->

<!-- review:SF-2026-ARXIV-2607-16074:start -->
### JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models

<!-- claim:SF-2026-ARXIV-2607-16074:start -->The post-training of Vision-Language-Action (VLA) models is essential due to the diversity of simulators, robot embodiments, and task objectives. Existing compute services, whether offered as direct accelerator rental or batch-workload submission, typically allocate an exclusive set of GPU and CPU resources to a single tenant. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16074:end -->

**为什么进入候选分母。** 摘要首要问题为“The post-training of Vision-Language-Action (VLA) models is essential due to the diversity of simulators, robot embodiments, and task objectives.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address these challenges, we present JoyNexus, a unified service for multi-tenant VLA supervised fine-tuning, reinforcement learning, and evaluation.

**证据证明什么。** Results show that, compared with isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves service utilization via cross-tenant scheduling on shared resources.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16074v1#S2.SS2 — 2.2 Distributed Training Frameworks for Foundation Models; https://arxiv.org/html/2607.16074v1#S4 — 4 JoyNexus Service Architecture。Evaluation：https://arxiv.org/html/2607.16074v1#S2.SS3 — 2.3 SFT, RL, and Evaluation for Vision-Language-Action Models; https://arxiv.org/html/2607.16074v1#S3.SS2 — 3.2 SFT, RL, and Evaluation Workflows。Limitations / counterevidence：https://arxiv.org/html/2607.16074v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/lerobot, https://github.com/modelscope/twinkle, https://github.com/THUDM/slime; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-MULTI-TENANT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16074:end -->

<!-- review:SF-2026-ARXIV-2607-16094:start -->
### How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA

<!-- claim:SF-2026-ARXIV-2607-16094:start -->Compositional visual question answering requires Vision-Language Models (VLMs) to execute multiple reasoning operations like object selection, spatial relation resolution, and attribute verification. Despite strong aggregate performance, the mechanistic basis of VLM failures on this task remains underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16094:end -->

**为什么进入候选分母。** 摘要首要问题为“Compositional visual question answering requires Vision-Language Models (VLMs) to execute multiple reasoning operations like object selection, spatial relation resolution, and attribute verification.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce an Operation-centric mechanistic framework that decomposes VLM failures by both the reasoning operation where they originate and the internal computational pathway through which they propagate.

**证据证明什么。** Validation on VSR further shows that single-step spatial failures are concentrated at object-position encoding, distinguishing them from multi-step relational composition.

**证据没有证明什么。** Correct answers depend heavily on the target object’s visual representation while incorrect answers show minimal dependence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16094v1#S3 — 3. Methodology; https://arxiv.org/html/2607.16094v1#S5.SS7 — 5.7. Cross-Architecture Analysis。Evaluation：https://arxiv.org/html/2607.16094v1#S3.SS3 — 3.3. Measuring Visual Criticality via Causal Mean Ablation; https://arxiv.org/html/2607.16094v1#S4 — 4. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16094v1#S3.SS2 — 3.2. Operation-Aware Decomposition of Queries and Failure Taxonomy; https://arxiv.org/html/2607.16094v1#S5.SS2 — 5.2. Grounding Failure: select。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Correct answers depend heavily on the target object’s visual representation while incorrect answers show minimal dependence.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16094:end -->

<!-- review:SF-2026-ARXIV-2607-16097:start -->
### Understanding Reasoning from Pretraining to Post-Training

<!-- claim:SF-2026-ARXIV-2607-16097:start -->Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it. As a result, two basic questions remain open: (1) how do pretraining choices (model size, data) shape the returns to RL compute, and (2) what does RL actually do to the model? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16097:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Using this framework, we find that the post-RL performance at given RL compute level is well-predicted from the pretraining loss, and slope of the RL reward curves improves approximately linearly with the pretraining tokens.

**证据证明什么。** Using this framework, we find that the post-RL performance at given RL compute level is well-predicted from the pretraining loss, and slope of the RL reward curves improves approximately linearly with the pretraining tokens.

**证据没有证明什么。** That said, chess differs from natural language in ways that limit direct transfer: the vocabulary is small (81 tokens), verification is exact, and reasoning is not entangled with world knowledge or fluency. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16097v1#S2 — 2 Framework: Chess as a Testbed for Reasoning; https://arxiv.org/html/2607.16097v1#A3 — Appendix C Implementation Details。Evaluation：https://arxiv.org/html/2607.16097v1#A8.SS4 — H.4 CoT Evolution Analysis; https://arxiv.org/html/2607.16097v1#A9 — Appendix I Olmo Experiment Additional Details。Limitations / counterevidence：https://arxiv.org/html/2607.16097v1#A1 — Appendix A Discussions and Limitations; https://arxiv.org/html/2607.16097v1#A7.SS8 — G.8 Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/collections/pavelslab-nyu/pre2post-chess, https://github.com/pavelslab-nyu/pre2post-chess, https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：That said, chess differs from natural language in ways that limit direct transfer: the vocabulary is small (81 tokens), verification is exact, and reasoning is not entangled with world knowledge or fluency.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16097:end -->

<!-- review:SF-2026-ARXIV-2607-16100:start -->
### Every Microsecond Matters: Achieving Near Speed-of-Light Latency in GPU Collectives

<!-- claim:SF-2026-ARXIV-2607-16100:start -->GPU collective communication is typically optimized for bandwidth, yet many emerging workloads are increasingly limited by latency. Long-context decode-heavy large language model (LLM) inference is a prime example, where serving large models requires multiple GPUs, and many small collectives lie directly on the critical path of token generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16100:end -->

**为什么进入候选分母。** 摘要首要问题为“GPU collective communication is typically optimized for bandwidth, yet many emerging workloads are increasingly limited by latency.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Long-context decode-heavy large language model (LLM) inference is a prime example, where serving large models requires multiple GPUs, and many small collectives lie directly on the critical path of token generation.

**证据证明什么。** Microbenchmarks show substantial latency reductions for small and medium messages, reducing overhead to within 7% of the absolute SoL lower bound.

**证据没有证明什么。** We do not compare against NIXL [ 65 ] , as it targets a different design space. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16100v1#S4 — IV Designing Barrier-Free Collectives; https://arxiv.org/html/2607.16100v1#S5 — V Low-Latency API Design。Evaluation：https://arxiv.org/html/2607.16100v1#S7 — VII Microbenchmarks; https://arxiv.org/html/2607.16100v1#S7.SS1 — VII-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16100v1#S10 — X Conclusion; https://arxiv.org/html/2607.16100v1#S9 — IX Related Work and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/ss16118/low-latency-nccl, https://github.com/NVIDIA/TensorRT-LLM, https://rocm.docs.amd.com/projects/rccl/en/latest/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：We do not compare against NIXL [ 65 ] , as it targets a different design space.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16100:end -->

<!-- review:SF-2026-ARXIV-2607-16107:start -->
### Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos

<!-- claim:SF-2026-ARXIV-2607-16107:start -->We present Audio-Visual Flamingo (AV-Flamingo), a fully open state-of-the-art audio-visual large language model (AV-LLM) for joint understanding and reasoning over audio, images, and long-form videos. Unlike prior AV-LLMs that primarily focus on short clips, AV-Flamingo is designed for understanding and reasoning over long and complex real-world (audio-visual) videos. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16107:end -->

**为什么进入候选分母。** 摘要首要问题为“We present Audio-Visual Flamingo (AV-Flamingo), a fully open state-of-the-art audio-visual large language model (AV-LLM) for joint understanding and reasoning over audio, images, and long-form videos.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present Audio-Visual Flamingo (AV-Flamingo), a fully open state-of-the-art audio-visual large language model (AV-LLM) for joint understanding and reasoning over audio, images, and long-form videos.

**证据证明什么。** Extensive experiments across 15+ audio-visual, omni-modal, audio, and vision benchmarks show that AV-Flamingo outperforms similarly sized open models by clear margins and remains highly competitive with, and in some cases surpasses, much larger open-weight and closed models, particularly on long and complex real-world audio-visual understanding and reasoning tasks.

**证据没有证明什么。** Conclusion, Limitations and Future Work We presented AV-Flamingo, a fully open AV-LLM for joint understanding and reasoning over long and complex real-world videos. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16107v1#S2 — 2. Methodology; https://arxiv.org/html/2607.16107v1#S2.SS1 — 2.1 Architecture。Evaluation：https://arxiv.org/html/2607.16107v1#S3 — 3. Experiments; https://arxiv.org/html/2607.16107v1#S4 — 4. Results。Limitations / counterevidence：https://arxiv.org/html/2607.16107v1#S5 — 5. Conclusion, Limitations and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/audio-flamingo, http://huggingface.co/nvidia/audio-visual-flamingo-hf, https://huggingface.co/datasets/nvidia/AV-Skills; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Conclusion, Limitations and Future Work We presented AV-Flamingo, a fully open AV-LLM for joint understanding and reasoning over long and complex real-world videos.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16107:end -->

<!-- review:SF-2026-ARXIV-2607-16109:start -->
### The Honest Quorum Problem: Epistemic Byzantine Fault Tolerance for Agentic Infrastructure

<!-- claim:SF-2026-ARXIV-2607-16109:start -->State machine replication (SMR) and Byzantine fault-tolerant (BFT) consensus guarantee agreement despite a bounded number of arbitrary, colluding faulty participants. However, these guarantees rely on participants outside this set correctly executing the protocol's transition semantics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16109:end -->

**为什么进入候选分母。** 摘要首要问题为“State machine replication (SMR) and Byzantine fault-tolerant (BFT) consensus guarantee agreement despite a bounded number of arbitrary, colluding faulty participants.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We define Epistemic Byzantine Fault Tolerance (EBFT), a fault-tolerance model for agentic infrastructure and post-deterministic distributed systems.

**证据证明什么。** We show that adding nominally distinct agents improves fault tolerance only when it measurably reduces the upper-tail concentration of invalid endorsements or unusable support.

**证据没有证明什么。** A calibration set with only a small number of invalid or valid examples cannot justify an extremely small tail probability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16109v1#A2 — Appendix B Calibration and Evaluation Methodology; https://arxiv.org/html/2607.16109v1#S2.SS4 — 2.4 Common-Mode Failure and Design Diversity。Evaluation：https://arxiv.org/html/2607.16109v1#A2 — Appendix B Calibration and Evaluation Methodology; https://arxiv.org/html/2607.16109v1#S8 — 8 Calibration and Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.16109v1#S10 — 10 Discussion and Limitations; https://arxiv.org/html/2607.16109v1#A2.SS4 — B.4 Uncertainty Intervals and Rare-Event Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：A calibration set with only a small number of invalid or valid examples cannot justify an extremely small tail probability.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16109:end -->

<!-- review:SF-2026-ARXIV-2607-16112:start -->
### Harmonizing AI Safety Thresholds

<!-- claim:SF-2026-ARXIV-2607-16112:start -->Frontier AI companies have published capability thresholds that differ substantially, making it difficult for third parties to verify whether a threshold has been crossed or to compare requirements across companies. Moreover, without common minimum thresholds, risk mitigation may be inconsistent, creating a potential race to the bottom in safety standards. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16112:end -->

**为什么进入候选分母。** 摘要首要问题为“Frontier AI companies have published capability thresholds that differ substantially, making it difficult for third parties to verify whether a threshold has been crossed or to compare requirements across companies.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We develop a methodology for deriving harmonized thresholds across three risk domains.

**证据证明什么。** Our analysis expands upon prior work and highlights existing empirical gaps and limitations.

**证据没有证明什么。** 3.11 Limitations and Suggested Next Steps Gross, not net harm. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16112v1#S2 — 2 Core Methodology; https://arxiv.org/html/2607.16112v1#S4.SS2 — 4.2 Implementing the Quantitative Risk Methodology。Evaluation：https://arxiv.org/html/2607.16112v1#S3.SS9 — 3.9 Illustrative Case Study: April 2026。Limitations / counterevidence：https://arxiv.org/html/2607.16112v1#S3.SS10 — 3.10 Preliminary Conclusions; https://arxiv.org/html/2607.16112v1#S3.SS11 — 3.11 Limitations and Suggested Next Steps。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：3.11 Limitations and Suggested Next Steps Gross, not net harm.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16112:end -->

<!-- review:SF-2026-ARXIV-2607-16117:start -->
### Rate-Utility Frontiers for Language Encodings: Comparing Tokens, Bytes, and Pixels Under Controlled Linguistic Content

<!-- claim:SF-2026-ARXIV-2607-16117:start -->Language models encode text as subword tokens, raw bytes, or rendered pixels, but these encodings are usually compared under modeling constraints that expose different amounts of linguistic content to models across different languages. We instead ask what each encoding preserves when both the content and the downstream capacity are controlled. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16117:end -->

**为什么进入候选分母。** 摘要首要问题为“Language models encode text as subword tokens, raw bytes, or rendered pixels, but these encodings are usually compared under modeling constraints that expose different amounts of linguistic content to models across different languages.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We instead ask what each encoding preserves when both the content and the downstream capacity are controlled.

**证据证明什么。** Choosing an encoding is therefore not a fixed preference for tokens, bytes, or pixels, but a rate-utility tradeoff that depends on the task, language mix, capacity regime, and compute budget.

**证据没有证明什么。** This is a simple and useful baseline, but it is not the only possible byte interface. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16117v1#A3.SS2 — C.2 Model and training details; https://arxiv.org/html/2607.16117v1#S3.SS3 — 3.3 Encoder model and capacity bottleneck。Evaluation：https://arxiv.org/html/2607.16117v1#A3 — Appendix C Experimental details; https://arxiv.org/html/2607.16117v1#A3.SS3 — C.3 Task objectives and evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16117v1#A1 — Appendix A Limitations and future work; https://arxiv.org/html/2607.16117v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ziegler-ingo/rate-utility-frontiers, https://www.wordproject.org/, https://github.com/harfbuzz/harfbuzz; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This is a simple and useful baseline, but it is not the only possible byte interface.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TOKENIZER`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16117:end -->

<!-- review:SF-2026-ARXIV-2607-16122:start -->
### CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine-Tuning Data

<!-- claim:SF-2026-ARXIV-2607-16122:start -->Evaluations should do more than measure a models current performance. They should tell us what to fix for the next model iteration and provide a way to generate targeted post training data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16122:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluations should do more than measure a models current performance.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce CRAFT, a method that converts any rubric based evaluation dataset into a model specific diagnosis of weak capabilities.

**证据证明什么。** CRAFT achieves the strongest finance domain average for all four models under repeated temperature decoding; on legal domain, it is strongest for three of four models and remains within the decoding variance bands of the best baseline on the fourth.

**证据没有证明什么。** Empirically, those targets matter, though not as uniform wins on every benchmark. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16122v1#S3 — 3 Methodology; https://arxiv.org/html/2607.16122v1#S5 — 5 Baseline Methods and Models Used。Evaluation：https://arxiv.org/html/2607.16122v1#S6.SS2 — 6.2 Legal Benchmark Results; https://arxiv.org/html/2607.16122v1#S6.SS3 — 6.3 Finance Benchmark Results。Limitations / counterevidence：https://arxiv.org/html/2607.16122v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Empirically, those targets matter, though not as uniform wins on every benchmark.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16122:end -->

<!-- review:SF-2026-ARXIV-2607-16127:start -->
### CADAQUES: A Cost-Aware Dual Architecture for Query-Efficient Autonomous Discovery

<!-- claim:SF-2026-ARXIV-2607-16127:start -->Autonomous discovery systems couple a resource that answers queries (a simulator, instrument, or analytic model) to an algorithm that selects what to query next. Most software frameworks for this loop inherit the control structure of numerical optimization: campaigns run for a fixed number of iterations, query costs are absent from the programming interface, and decision-making is treated as free. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16127:end -->

**为什么进入候选分母。** 摘要首要问题为“Autonomous discovery systems couple a resource that answers queries (a simulator, instrument, or analytic model) to an algorithm that selects what to query next.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Here we present CADAQUES, an open-source Python framework built on one architectural principle: cost is a first-class primitive of the discovery loop.

**证据证明什么。** The framework is MIT-licensed and archived at Zenodo (doi:10.5281/zenodo.21293589).

**证据没有证明什么。** 7 Discussion and Future Work This section discusses the practical implications, current limitations, design choices, and next steps. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16127v1#S3 — 3 Design; https://arxiv.org/html/2607.16127v1#S6.SS3 — 6.3 Benchmarking frameworks。Evaluation：https://arxiv.org/html/2607.16127v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.16127v1#S6.SS2 — 6.2 Autonomous-experimentation platforms。Limitations / counterevidence：https://arxiv.org/html/2607.16127v1#S7 — 7 Discussion and Future Work; https://arxiv.org/html/2607.16127v1#S5.SS2 — 5.2 RQ2: Failure case under a common nominal wall-time budget。

**Artifact boundary。** Exact v1 links https://github.com/jorgebravoabad/cadaques, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：7 Discussion and Future Work This section discusses the practical implications, current limitations, design choices, and next steps.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16127:end -->

<!-- review:SF-2026-ARXIV-2607-16130:start -->
### A Methodology for Auditable Trustworthiness Levels in AI Lifecycle Governance

<!-- claim:SF-2026-ARXIV-2607-16130:start -->AI governance increasingly requires judgments about whether an AI system remains adequately trustworthy over time, whether observed changes are tolerable, and how such judgments should be documented in a transparent and contestable way. Yet existing work on AI trustworthiness remains either too high-level to support lifecycle monitoring and reassessment or too narrowly metric-driven to connect with governance needs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16130:end -->

**为什么进入候选分母。** 摘要首要问题为“AI governance increasingly requires judgments about whether an AI system remains adequately trustworthy over time, whether observed changes are tolerable, and how such judgments should be documented in a transparent and contestable way.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We illustrate the methodology on synthetic AI lifecycle traces involving degradation, shocks, updates, heterogeneous monitoring cadences, and system comparison.

**证据证明什么。** Our methodology does not replace legal or other expert judgment: it supports conformity documentation and lifecycle monitoring by providing an evidential basis for documenting and tracking AI governance-relevant changes over time.

**证据没有证明什么。** The methodology is therefore best understood as an institutionally dependent governance layer: it becomes actionable only when the underlying measurement, aggregation, labeling, and review procedures are themselves documented and sufficiently mature. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16130v1#S3 — 3 Formal Framework of AI Trustworthiness; https://arxiv.org/html/2607.16130v1#S5.SS2 — 5.2 Experiment 2: Single-System Lifecycle with Asynchronous Monitoring。Evaluation：https://arxiv.org/html/2607.16130v1#S5.SS1 — 5.1 Experiment 1: Lifecycle Baseline; https://arxiv.org/html/2607.16130v1#S5.SS2 — 5.2 Experiment 2: Single-System Lifecycle with Asynchronous Monitoring。Limitations / counterevidence：https://arxiv.org/html/2607.16130v1#S7 — 7 Discussion and Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The methodology is therefore best understood as an institutionally dependent governance layer: it becomes actionable only when the underlying measurement, aggregation, labeling, and review procedures are themselves documented and sufficiently mature.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16130:end -->

<!-- review:SF-2026-ARXIV-2607-16131:start -->
### ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-16131:start -->Multimodal Scientific Claim Verification (MSCV) requires models to verify scientific claims using visually grounded evidence from papers, including figures, tables, charts, and textual context. However, existing methods often fail because they struggle to locate decisive visual evidence, accurately read structured scientific visuals, and integrate multimodal observations into reliable reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16131:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal Scientific Claim Verification (MSCV) requires models to verify scientific claims using visually grounded evidence from papers, including figures, tables, charts, and textual context.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce ToolSciVer, the first tool-augmented framework for MSCV to our knowledge.

**证据证明什么。** Experiments on SciVer and MuSciClaims datasets on five VLMs from three model families (Qwen, InternVL, Gemma) demonstrate that our method achieves superior performance compared to four competitive baselines including prompting-based and RL-based tool-use methods, highlighting the effectiveness of learned, type-aware tool use for scientific claim verification.

**证据没有证明什么。** Although reinforcement learning improves tool selection and usage, it cannot fully recover from erroneous tool outputs; future work should explore stronger scientific parsers and uncertainty-aware verification mechanisms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16131v1#A1 — Appendix A Method Details; https://arxiv.org/html/2607.16131v1#S3 — 3 Our Method。Evaluation：https://arxiv.org/html/2607.16131v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.16131v1#A2 — Appendix B Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.16131v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.16131v1#Sx1 — Limitation。

**Artifact boundary。** Exact v1 links https://github.com/psunlpgroup/Tool-Sciver, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Although reinforcement learning improves tool selection and usage, it cannot fully recover from erroneous tool outputs; future work should explore stronger scientific parsers and uncertainty-aware verification mechanisms.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16131:end -->

<!-- review:SF-2026-ARXIV-2607-16133:start -->
### When Do Multi-Agent Systems Help? An Information Bottleneck Perspective

<!-- claim:SF-2026-ARXIV-2607-16133:start -->LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks. However, their advantages over single-agent systems (SAS) remain unclear, with performance varying inconsistently across settings. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16133:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks.

**证据证明什么。** Our study shows that multi-agent design is fundamentally an information-bottleneck optimization problem.

**证据没有证明什么。** Despite these insights, our work has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16133v1#A4.SS1 — D.1 Task Decomposition and Relay Design; https://arxiv.org/html/2607.16133v1#A2.SS2 — B.2 Models。Evaluation：https://arxiv.org/html/2607.16133v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.16133v1#A2.SS3 — B.3 Per-benchmark configuration。Limitations / counterevidence：https://arxiv.org/html/2607.16133v1#S7 — 7 Summary and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/divelab/MAS-SAS, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Despite these insights, our work has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16133:end -->

<!-- review:SF-2026-ARXIV-2607-16169:start -->
### When Does Muon Help Agentic Reinforcement Learning?

<!-- claim:SF-2026-ARXIV-2607-16169:start -->Muon is competitive with AdamW in large-scale pre-training, but its operating regime in reinforcement-learning post-training remains unclear. We map this regime on ALFWorld, a sparse-reward agentic benchmark, using three group-based objectives and Qwen2.5 models from 0.5B to 3B. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16169:end -->

**为什么进入候选分母。** 摘要首要问题为“Muon is competitive with AdamW in large-scale pre-training, but its operating regime in reinforcement-learning post-training remains unclear.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We map this regime on ALFWorld, a sparse-reward agentic benchmark, using three group-based objectives and Qwen2.5 models from 0.5B to 3B.

**证据证明什么。** AdamW responds non-monotonically to rate, whereas fan-in Muon remains stable at a more aggressive effective step: at $3 \times 10^{-5}$ it improves late success over an AdamW $10^{-6}$ baseline after correction across rate-metric tests.

**证据没有证明什么。** Learning-rate coverage is limited: GiGPO and GraphGPO include two Muon rates, GRPO includes only , and none is a broad sweep. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16169v1#Sx4 — Method: Muon for Group-Based Agentic RL; https://arxiv.org/html/2607.16169v1#A2 — Appendix B B. Implementation Notes for Muon。Evaluation：https://arxiv.org/html/2607.16169v1#A1 — Appendix A A. Experimental Hyperparameters; https://arxiv.org/html/2607.16169v1#Sx5 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16169v1#Sx5.SSx7 — Discussion: Reconciling Positive and Negative Evidence; https://arxiv.org/html/2607.16169v1#Sx6 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/blog/bird-of-paradise/training-rl-with-muon-2, https://huggingface.co/blog/bird-of-paradise/training-rl-with-muon-3, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Learning-rate coverage is limited: GiGPO and GraphGPO include two Muon rates, GRPO includes only , and none is a broad sweep.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16169:end -->

<!-- review:SF-2026-ARXIV-2607-16173:start -->
### Vision-Language-Motion Maps: An Open-Vocabulary, Uncertainty-Aware, Queryable Motion Attribute for 3D Scene Maps

<!-- claim:SF-2026-ARXIV-2607-16173:start -->Open-vocabulary 3D maps let robots answer language queries about what and where, but they assume a static world and cannot answer queries about how scene elements behave. We introduce Vision-Language-Motion Maps (VLMM), an open-vocabulary, language-queryable 3D map - queried through a rule-based intent router over open-vocabulary object nouns, not a general natural-language interface - in which each element carries a fused motion attribute: a VLM/LLM semantic movability prior combined with geometrically observed cross-frame motion, together with a per-element uncertainty. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16173:end -->

**为什么进入候选分母。** 摘要首要问题为“Open-vocabulary 3D maps let robots answer language queries about what and where, but they assume a static world and cannot answer queries about how scene elements behave.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce Vision-Language-Motion Maps (VLMM), an open-vocabulary, language-queryable 3D map - queried through a rule-based intent router over open-vocabulary object nouns, not a general natural-language interface - in which each element carries a fused motion attribute: a VLM/LLM semantic movability prior combined with geometrically observed cross-frame motion, together with a per-element uncertainty.

**证据证明什么。** On real dynamic RGB-D (TUM and Bonn, six sequences) we show the uncertainty channel - our key difference from prior fused-motion work - consistently improves moving-vs-static average precision and reduces false motion flags, and that it is robust to estimated (noisy) poses.

**证据没有证明什么。** IV Limitations (1) The strong ablation numbers are exact-GT simulation ; real-world object-level F1 is (motion-bleed; flow under-measures small/fast objects)—we claim relative, not SOTA, results. (2) Confidence is uncertainty-weighted, not raw-calibrated. (3) The query parser is intent routing, not NLU. (4) Real-data motion GT is a person segmenter, conflating “moving” with “person” (static people are false positives, non-person movers missed); the real-data numbers (Table III ) thus establish the uncertainty channel’s effect under sensor noise, not general non-person detection—which we evaluate only in simulation (exact GT, incl. injected Kinect-level noise, gap). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16173v1#S2 — II Method; https://arxiv.org/html/2607.16173v1#S3.SS1 — III-A Implementation and compute。Evaluation：https://arxiv.org/html/2607.16173v1#S3 — III Results & Discussion; https://arxiv.org/html/2607.16173v1#S3.SS3 — III-C Evaluation metrics and parameters。Limitations / counterevidence：https://arxiv.org/html/2607.16173v1#S3 — III Results & Discussion; https://arxiv.org/html/2607.16173v1#S4 — IV Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：IV Limitations (1) The strong ablation numbers are exact-GT simulation ; real-world object-level F1 is (motion-bleed; flow under-measures small/fast objects)—we claim relative, not SOTA, results. (2) Confidence is uncertainty-weighted, not raw-calibrated. (3) The query parser is intent routing, not NLU. (4) Real-data motion GT is a person segmenter, conflating “moving” with “person” (static people are false positives, non-person movers missed); the real-data numbers (Table III ) thus establish the uncertainty channel’s effect under sensor noise, not general non-person detection—which we evaluate only in simulation (exact GT, incl. injected Kinect-level noise, gap).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16173:end -->

<!-- review:SF-2026-ARXIV-2607-16184:start -->
### PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization

<!-- claim:SF-2026-ARXIV-2607-16184:start -->Mixture-of-Experts (MoE) is a popular class of large language models (LLMs), offering high efficiency and accuracy. However, in KV-cache-intensive serving scenarios, MoEs often exhibit a tension between the GPU memory requirements of the model weights and the growing KV cache. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16184:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) is a popular class of large language models (LLMs), offering high efficiency and accuracy.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model's weights at runtime and balances expert-weight precision with the KV cache sizes.

**证据证明什么。** PagedWeight achieves FP16-equivalent accuracy with up to 72.0% GPU memory savings and 1.94$\times$ throughput improvement, and improves quality over quantization methods by up to 39.3% at a similar memory budget with at most 4.1% throughput loss.

**证据没有证明什么。** Future work includes extending PagedWeight to other quantized weight formats with compatible layouts and kernels, and exploring complementary methods for estimating prompt-wise expert sensitivity to further improve the quality–memory tradeoff under KV-cache pressure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16184v1#S2.SS1 — 2.1 Mixture-of-Experts Architecture and Routing Imbalance; https://arxiv.org/html/2607.16184v1#S3 — 3 PagedWeight System。Evaluation：https://arxiv.org/html/2607.16184v1#S4 — 4 Experimental Methodology; https://arxiv.org/html/2607.16184v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16184v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/google/gemma-4-26B-A4B, https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work includes extending PagedWeight to other quantized weight formats with compatible layouts and kernels, and exploring complementary methods for estimating prompt-wise expert sensitivity to further improve the quality–memory tradeoff under KV-cache pressure.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16184:end -->

<!-- review:SF-2026-ARXIV-2607-16189:start -->
### Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA

<!-- claim:SF-2026-ARXIV-2607-16189:start -->Grounded long-video question answering (Grounded LVQA) requires answering a question about a long video while localizing the short evidence interval that supports the answer. Recent agentic methods frame this task as multi-turn exploration with a single crop_video(start, end) action, which supports coarse-to-fine narrowing but provides no primitive for fine-to-coarse backtracking. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16189:end -->

**为什么进入候选分母。** 摘要首要问题为“Grounded long-video question answering (Grounded LVQA) requires answering a question about a long video while localizing the short evidence interval that supports the answer.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose VideoTreeSearch (VTS), a framework that casts grounded LVQA as iterative self-correcting search over an adaptive temporal tree.

**证据证明什么。** On three Grounded LVQA benchmarks (CG-Bench, Haystack-LVBench, Haystack-Ego4D), VTS outperforms the strongest prior agentic methods by +12.5 mIoU on CG-Bench and +7.4 T-F1 on Haystack-Ego4D.

**证据没有证明什么。** Limitations and Future Work VTS has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16189v1#S3 — 3 Method; https://arxiv.org/html/2607.16189v1#A1 — Appendix A Additional Implementation Details。Evaluation：https://arxiv.org/html/2607.16189v1#A2 — Appendix B Evaluation Benchmarks; https://arxiv.org/html/2607.16189v1#S5 — 5 Experimental Results。Limitations / counterevidence：https://arxiv.org/html/2607.16189v1#Sx1 — Limitations and Future Work; https://arxiv.org/html/2607.16189v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/CeeZh/VTS, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations and Future Work VTS has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16189:end -->

<!-- review:SF-2026-ARXIV-2607-16190:start -->
### FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation

<!-- claim:SF-2026-ARXIV-2607-16190:start -->Video Diffusion Transformers process long spatio-temporal sequences, making self-attention the main bottleneck in high-resolution video generation. Training-free sparse attention reduces this cost, but adaptive Top-$p$ routing creates uneven per-head workloads under multi-GPU sequence parallelism. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16190:end -->

**为什么进入候选分母。** 摘要首要问题为“Video Diffusion Transformers process long spatio-temporal sequences, making self-attention the main bottleneck in high-resolution video generation.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present \method{}, a training-free sparse-attention system that improves the distributed execution efficiency of adaptive sparse attention under multi-GPU sequence parallelism. \method{} uses Top-$p$ routing, a Top-$k$ safety floor, and video-aware block organization as the sparse-routing frontend, then repairs the materialized mask at runtime.

**证据证明什么。** Training-free sparse attention reduces this cost, but adaptive Top-$p$ routing creates uneven per-head workloads under multi-GPU sequence parallelism.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16190v1#S3 — 3 FVAttn Design; https://arxiv.org/html/2607.16190v1#S3.SS4 — 3.4 Efficient Implementation。Evaluation：https://arxiv.org/html/2607.16190v1#S4 — 4 Experiments; https://arxiv.org/html/2607.16190v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16190v1#S5 — 5 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/ModelTC/lightx2v, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16190:end -->

<!-- review:SF-2026-ARXIV-2607-16192:start -->
### MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction

<!-- claim:SF-2026-ARXIV-2607-16192:start -->Humans can infer how objects are likely to move from passive observation: a cup may be lifted, a drawer may slide, and a lid may rotate shut. Such predictions expose the physical consequences of interaction needed to act in the real world. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-16192:end -->

**为什么进入候选分母。** 摘要首要问题为“Humans can infer how objects are likely to move from passive observation: a cup may be lifted, a drawer may slide, and a lid may rotate shut.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Such predictions expose the physical consequences of interaction needed to act in the real world.

**证据证明什么。** These results show that we can efficiently re-purpose video priors into explicit geometric forecasts for embodied intelligence. https://motionforesight.github.io/

**证据没有证明什么。** These limitations suggest clear directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.16192v1#A1 — Appendix A Implementation Details; https://arxiv.org/html/2607.16192v1#A1.SS1 — A.1 Default model configuration。Evaluation：https://arxiv.org/html/2607.16192v1#A1.SS6 — A.6 Evaluation metrics; https://arxiv.org/html/2607.16192v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.16192v1#S5 — 5 Discussion, Limitations, and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These limitations suggest clear directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-16192:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-15299 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15299 |
| SF-2026-ARXIV-2607-15330 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15330 |
| SF-2026-ARXIV-2607-15456 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15456 |
| SF-2026-ARXIV-2607-15498 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15498 |
| SF-2026-ARXIV-2607-15550 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15550 |
| SF-2026-ARXIV-2607-15593 | score_7_9 | selected | DA-20260720-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260720-01 |
| SF-2026-ARXIV-2607-15610 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15610 |
| SF-2026-ARXIV-2607-15621 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15621 |
| SF-2026-ARXIV-2607-15650 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15650 |
| SF-2026-ARXIV-2607-15655 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15655 |
| SF-2026-ARXIV-2607-15660 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15660 |
| SF-2026-ARXIV-2607-15714 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15714 |
| SF-2026-ARXIV-2607-15808 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15808 |
| SF-2026-ARXIV-2607-15846 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15846 |
| SF-2026-ARXIV-2607-15865 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15865 |
| SF-2026-ARXIV-2607-15898 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15898 |
| SF-2026-ARXIV-2607-15899 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15899 |
| SF-2026-ARXIV-2607-15901 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15901 |
| SF-2026-ARXIV-2607-16074 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16074 |
| SF-2026-ARXIV-2607-16097 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16097 |
| SF-2026-ARXIV-2607-16100 | score_7_9 | selected | DA-20260720-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260720-02 |
| SF-2026-ARXIV-2607-16184 | score_7_9 | selected | DA-20260720-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260720-03 |
| SF-2026-ARXIV-2607-16190 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-16190 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-15299:start -->
`SF-2026-ARXIV-2607-15299` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we propose MLLM-DataEngine, a novel closed-loop system that bridges data generation, model training, and evaluation. 为避免挤压 `TRAIN-DATA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15299:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15330:start -->
`SF-2026-ARXIV-2607-15330` 的 exact-v1 Deep Review 已保留。其机制为：We propose a two-stage training recipe consisting of pre-training and post-training. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15330:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15456:start -->
`SF-2026-ARXIV-2607-15456` 的 exact-v1 Deep Review 已保留。其机制为：We introduce Looped Latent Attention (\lla{}), a post-training cache codec that stores compact K and V latents and reconstructs loop-specific K/V vectors only when attention reads them. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15456:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15498:start -->
`SF-2026-ARXIV-2607-15498` 的 exact-v1 Deep Review 已保留。其机制为：We present VarRate, a training-free KV codec that assigns each token a variable low-rank budget by its query salience, keeping every token at a nonzero rank. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15498:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15550:start -->
`SF-2026-ARXIV-2607-15550` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we introduce SeerGuard, a consequence-aware safety framework designed to mitigate these risks through pre-execution instruction-level screening and action-level risk assessment. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15550:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15610:start -->
`SF-2026-ARXIV-2607-15610` 的 exact-v1 Deep Review 已保留。其机制为：We propose Process-Scorer Guided Adaptive Tree Rollout (PATR), a quality-aware rollout framework for multi-turn agent RL. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15610:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15621:start -->
`SF-2026-ARXIV-2607-15621` 的 exact-v1 Deep Review 已保留。其机制为：We present a fast-slow architecture that removes this compromise. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15621:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15650:start -->
`SF-2026-ARXIV-2607-15650` 的 exact-v1 Deep Review 已保留。其机制为：We present DiTango, an efficient parallel framework for DiT generation. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15650:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15655:start -->
`SF-2026-ARXIV-2607-15655` 的 exact-v1 Deep Review 已保留。其机制为：Thus, in this work, we propose AdaLook, an adaptive lookahead framework for DLM decoding. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15655:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15660:start -->
`SF-2026-ARXIV-2607-15660` 的 exact-v1 Deep Review 已保留。其机制为：To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15660:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15714:start -->
`SF-2026-ARXIV-2607-15714` 的 exact-v1 Deep Review 已保留。其机制为：To address both, we introduce \textbf{AC-VLA}, a plug-and-play Action Compositional learning framework comprising two architecture-agnostic components: \textbf{(i)} a compositional learning module that uses an LLM-driven instruction decomposer and a proprioceptive trajectory aligner to generate dense sub-task supervision, followed by mixed training on complete demonstrations and decomposed data to endow the model with compositional generalization; and \textbf{(ii)} a state-conditioned asymmetric masking strategy that suppresses wrist-view inputs during closed-gripper phases, enforcing global semantic grounding. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15714:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15808:start -->
`SF-2026-ARXIV-2607-15808` 的 exact-v1 Deep Review 已保留。其机制为：Despite previous studies on cyclists' route choices, the influence of visual and non-visual factors on these choices for different trip purposes remains unclear; thus, this paper fills this gap through a data-driven case study in Montreal, Canada. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15808:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15846:start -->
`SF-2026-ARXIV-2607-15846` 的 exact-v1 Deep Review 已保留。其机制为：We present DSTAR, a software-hardware co-design framework that accelerates DiT inference by reducing spatial and temporal redundancy. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15846:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15865:start -->
`SF-2026-ARXIV-2607-15865` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents an MLIR (Multi-Level Intermediate Representation) based compilation method for large language models, illustrated using two dialects of operators, TopOp and TpuOp. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15865:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15898:start -->
`SF-2026-ARXIV-2607-15898` 的 exact-v1 Deep Review 已保留。其机制为：We present a hierarchical driving world model that factorizes future prediction across two levels operating at distinct temporal and abstraction scales: a high-level predictor that forecasts coarse scene structure over extended temporal horizons, and a low-level generator that produces detailed predictions conditioned on the high-level output. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15898:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15899:start -->
`SF-2026-ARXIV-2607-15899` 的 exact-v1 Deep Review 已保留。其机制为：Our results provide a principled foundation for building robust, state-preserving multi-model inference systems. 为避免挤压 `PLATFORM-GATEWAY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15899:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15901:start -->
`SF-2026-ARXIV-2607-15901` 的 exact-v1 Deep Review 已保留。其机制为：We further propose DSWorld, a practical framework that combines structured state construction, cost-aware routing, lightweight real execution, and an LLM-based simulator for expensive operations. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15901:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16074:start -->
`SF-2026-ARXIV-2607-16074` 的 exact-v1 Deep Review 已保留。其机制为：To address these challenges, we present JoyNexus, a unified service for multi-tenant VLA supervised fine-tuning, reinforcement learning, and evaluation. 为避免挤压 `PLATFORM-MULTI-TENANT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16074:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16097:start -->
`SF-2026-ARXIV-2607-16097` 的 exact-v1 Deep Review 已保留。其机制为：Using this framework, we find that the post-RL performance at given RL compute level is well-predicted from the pretraining loss, and slope of the RL reward curves improves approximately linearly with the pretraining tokens. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16097:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-16190:start -->
`SF-2026-ARXIV-2607-16190` 的 exact-v1 Deep Review 已保留。其机制为：We present \method{}, a training-free sparse-attention system that improves the distributed execution efficiency of adaptive sparse attention under multi-GPU sequence parallelism. \method{} uses Top-$p$ routing, a Top-$k$ safety floor, and video-aware block organization as the sparse-routing frontend, then repairs the materialized mask at runtime. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-16190:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260720-01:start -->
### Scalable LLM Agent Tool Access in the Cloud

**约束变化与机制。** We present a cloud-scale gateway system for MCP service.

**证明与未证明。** On the agent side, the number of accessible tool is limited by the LLM context window and inference overhead; mounting a large tool set increases token usage and inference latency and can reduce task success rate. 但 Conclusion Deploying MCP services at cloud scale is not a drop-in change, and traditional L7 load balancers cannot be directly applied to MCP. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Conclusion Deploying MCP services at cloud scale is not a drop-in change, and traditional L7 load balancers cannot be directly applied to MCP. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-15593`。
<!-- analysis:DA-20260720-01:end -->

<!-- analysis:DA-20260720-02:start -->
### Every Microsecond Matters: Achieving Near Speed-of-Light Latency in GPU Collectives

**约束变化与机制。** Long-context decode-heavy large language model (LLM) inference is a prime example, where serving large models requires multiple GPUs, and many small collectives lie directly on the critical path of token generation.

**证明与未证明。** Microbenchmarks show substantial latency reductions for small and medium messages, reducing overhead to within 7% of the absolute SoL lower bound. 但 We do not compare against NIXL [ 65 ] , as it targets a different design space. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：We do not compare against NIXL [ 65 ] , as it targets a different design space. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-16100`。
<!-- analysis:DA-20260720-02:end -->

<!-- analysis:DA-20260720-03:start -->
### PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization

**约束变化与机制。** We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model's weights at runtime and balances expert-weight precision with the KV cache sizes.

**证明与未证明。** PagedWeight achieves FP16-equivalent accuracy with up to 72.0% GPU memory savings and 1.94$\times$ throughput improvement, and improves quality over quantization methods by up to 39.3% at a similar memory budget with at most 4.1% throughput loss. 但 Future work includes extending PagedWeight to other quantized weight formats with compatible layouts and kernels, and exploring complementary methods for estimating prompt-wise expert sensitivity to further improve the quality–memory tradeoff under KV-cache pressure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work includes extending PagedWeight to other quantized weight formats with compatible layouts and kernels, and exploring complementary methods for estimating prompt-wise expert sensitivity to further improve the quality–memory tradeoff under KV-cache pressure. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-16184`。
<!-- analysis:DA-20260720-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260720-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260720 | GAP-20260720-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260720-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260720-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260720-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260720-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260720-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260720-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

295 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：35
- `incremental_method_without_durable_system_delta`：210
- `local_benchmark_without_release_delta`：13
- `theory_without_ai_system_contract`：5
- `vertical_application_without_system_delta`：32

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 23、No Change 39、Structural 0；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/20/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Learning](https://arxiv.org/html/2607.15295v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [MLLM-DataEngine: Closing the Loop of Multimodal Instruction Tuning Data Generation](https://arxiv.org/html/2607.15299v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/html/2607.15330v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation](https://arxiv.org/html/2607.15434v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?](https://arxiv.org/html/2607.15439v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers](https://arxiv.org/html/2607.15456v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs](https://arxiv.org/html/2607.15498v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Cache-Aware Prompt Compression:A Two-Tier Cost Model for LLM API Caching](https://arxiv.org/html/2607.15516v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Recursive Harness Self-Improvement](https://arxiv.org/html/2607.15524v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction](https://arxiv.org/html/2607.15550v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents](https://arxiv.org/html/2607.15557v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation](https://arxiv.org/html/2607.15589v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Scalable LLM Agent Tool Access in the Cloud](https://arxiv.org/html/2607.15593v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [From Neural Intent to Cryptographic Authorization: Securing AI-Driven Enterprise Workflows](https://arxiv.org/html/2607.15596v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [ASK-NN: An Asymmetric Nearest-Neighbor Test that detects Distribution Drifts in Natural Language](https://arxiv.org/html/2607.15607v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Process Reward Informed Tree Rollout for Effective Multi-Turn RL](https://arxiv.org/html/2607.15610v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving](https://arxiv.org/html/2607.15621v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [DiTango: Cost-Effective Parallel Diffusion Generation with Selective Attention State Reuse](https://arxiv.org/html/2607.15650v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Adaptive Multi-Step Lookahead Decoding for Diffusion Language Models](https://arxiv.org/html/2607.15655v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents](https://arxiv.org/html/2607.15657v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning](https://arxiv.org/html/2607.15660v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports](https://arxiv.org/html/2607.15684v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval](https://arxiv.org/html/2607.15696v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [AC-VLA: Robust Out-of-Distribution Action Execution via Compositional Learning](https://arxiv.org/html/2607.15714v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents](https://arxiv.org/html/2607.15715v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Verified LLM-Driven Synthesis for Concept Design](https://arxiv.org/html/2607.15718v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [SlotMem: Character-Addressable Internal Memory for Narrative Long Video Generation](https://arxiv.org/html/2607.15772v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding](https://arxiv.org/html/2607.15778v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Examining the Associations between Visual and Non-Visual Elements and Cyclists' Route Choices for Various Trip Purposes](https://arxiv.org/html/2607.15808v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [DSTAR: Accelerating Diffusion Transformers via Spatial and Temporal Redundancy Reduction](https://arxiv.org/html/2607.15846v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [An MLIR-Based Compilation Method for Large Language Models](https://arxiv.org/html/2607.15865v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Scientific Claim-Source Retrieval Revisited: A Comparative Study of Style Transfer and Re-Ranking](https://arxiv.org/html/2607.15875v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Induction in Both Directions: A Mechanistic Analysis of In-Context Learning in Masked Diffusion Language Models](https://arxiv.org/html/2607.15893v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/html/2607.15898v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing](https://arxiv.org/html/2607.15899v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [DSWorld: A Data Science World Model for Efficient Autonomous Agents](https://arxiv.org/html/2607.15901v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs](https://arxiv.org/html/2607.15937v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Code-Poisoning Property Inference Attacks](https://arxiv.org/html/2607.15970v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Refusal is Not Safety! Benchmarking Latent Safety Risks of LLM-Driven Content Humorization](https://arxiv.org/html/2607.15977v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation](https://arxiv.org/html/2607.16010v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Presentation, Not Mechanism: A Render Confound in Deprecation-Aware Memory Evaluation](https://arxiv.org/html/2607.16019v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [DiffTestGen: Change-Directed LLM-Based Testing for Exposing Behavioral Differences](https://arxiv.org/html/2607.16024v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis](https://arxiv.org/html/2607.16062v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models](https://arxiv.org/html/2607.16074v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA](https://arxiv.org/html/2607.16094v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Understanding Reasoning from Pretraining to Post-Training](https://arxiv.org/html/2607.16097v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Every Microsecond Matters: Achieving Near Speed-of-Light Latency in GPU Collectives](https://arxiv.org/html/2607.16100v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos](https://arxiv.org/html/2607.16107v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [The Honest Quorum Problem: Epistemic Byzantine Fault Tolerance for Agentic Infrastructure](https://arxiv.org/html/2607.16109v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Harmonizing AI Safety Thresholds](https://arxiv.org/html/2607.16112v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Rate-Utility Frontiers for Language Encodings: Comparing Tokens, Bytes, and Pixels Under Controlled Linguistic Content](https://arxiv.org/html/2607.16117v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine-Tuning Data](https://arxiv.org/html/2607.16122v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [CADAQUES: A Cost-Aware Dual Architecture for Query-Efficient Autonomous Discovery](https://arxiv.org/html/2607.16127v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [A Methodology for Auditable Trustworthiness Levels in AI Lifecycle Governance](https://arxiv.org/html/2607.16130v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning](https://arxiv.org/html/2607.16131v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [When Do Multi-Agent Systems Help? An Information Bottleneck Perspective](https://arxiv.org/html/2607.16133v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [When Does Muon Help Agentic Reinforcement Learning?](https://arxiv.org/html/2607.16169v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Vision-Language-Motion Maps: An Open-Vocabulary, Uncertainty-Aware, Queryable Motion Attribute for 3D Scene Maps](https://arxiv.org/html/2607.16173v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/html/2607.16184v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA](https://arxiv.org/html/2607.16189v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation](https://arxiv.org/html/2607.16190v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04
- [MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction](https://arxiv.org/html/2607.16192v1) — first-public（Asia/Shanghai）：2026-07-20；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、62/62 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
