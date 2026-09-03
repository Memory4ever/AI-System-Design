# Daily Research — 2026-07-17

**Research Date:** 2026-07-17

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-16 09:00:00 ～ 2026-07-17 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **506** 个 identity；全量 title + abstract 筛选后冻结 **77** 个候选与 **429** 个 family-specific closure，retain rate **15.22%**。exact-v1 Review 为 77/77：Deep 27、Standard 50、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-17 |
| Window End | 2026-07-17 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-17-0900-v2.1-sha256:bc0b07a10e4c584d556aaaa4ea79928e129c26fea3192c73221b5d93287cb35d |
| Denominator Frozen At | 2026-09-04T07:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260717:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-16T09:00:00+08:00 | 2026-07-17T09:00:00+08:00 | 2026-09-04T07:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 506 | SF-2026-ARXIV-2607-14103;SF-2026-ARXIV-2607-14107;SF-2026-ARXIV-2607-14108;SF-2026-ARXIV-2607-14109;SF-2026-ARXIV-2607-14145;SF-2026-ARXIV-2607-14155;SF-2026-ARXIV-2607-14157;SF-2026-ARXIV-2607-14159;SF-2026-ARXIV-2607-14166;SF-2026-ARXIV-2607-14167;SF-2026-ARXIV-2607-14169;SF-2026-ARXIV-2607-14171;SF-2026-ARXIV-2607-14180;SF-2026-ARXIV-2607-14186;SF-2026-ARXIV-2607-14189;SF-2026-ARXIV-2607-14194;SF-2026-ARXIV-2607-14202;SF-2026-ARXIV-2607-14236;SF-2026-ARXIV-2607-14252;SF-2026-ARXIV-2607-14275;SF-2026-ARXIV-2607-14277;SF-2026-ARXIV-2607-14280;SF-2026-ARXIV-2607-14285;SF-2026-ARXIV-2607-14327;SF-2026-ARXIV-2607-14336;SF-2026-ARXIV-2607-14340;SF-2026-ARXIV-2607-14386;SF-2026-ARXIV-2607-14390;SF-2026-ARXIV-2607-14396;SF-2026-ARXIV-2607-14399;SF-2026-ARXIV-2607-14408;SF-2026-ARXIV-2607-14431;SF-2026-ARXIV-2607-14439;SF-2026-ARXIV-2607-14443;SF-2026-ARXIV-2607-14493;SF-2026-ARXIV-2607-14499;SF-2026-ARXIV-2607-14506;SF-2026-ARXIV-2607-14512;SF-2026-ARXIV-2607-14541;SF-2026-ARXIV-2607-14543;SF-2026-ARXIV-2607-14547;SF-2026-ARXIV-2607-14548;SF-2026-ARXIV-2607-14568;SF-2026-ARXIV-2607-14570;SF-2026-ARXIV-2607-14573;SF-2026-ARXIV-2607-14611;SF-2026-ARXIV-2607-14618;SF-2026-ARXIV-2607-14635;SF-2026-ARXIV-2607-14642;SF-2026-ARXIV-2607-14647;SF-2026-ARXIV-2607-14651;SF-2026-ARXIV-2607-14695;SF-2026-ARXIV-2607-14698;SF-2026-ARXIV-2607-14739;SF-2026-ARXIV-2607-14754;SF-2026-ARXIV-2607-14777;SF-2026-ARXIV-2607-14811;SF-2026-ARXIV-2607-14817;SF-2026-ARXIV-2607-14852;SF-2026-ARXIV-2607-14890;SF-2026-ARXIV-2607-14896;SF-2026-ARXIV-2607-14903;SF-2026-ARXIV-2607-14908;SF-2026-ARXIV-2607-14952;SF-2026-ARXIV-2607-14989;SF-2026-ARXIV-2607-15065;SF-2026-ARXIV-2607-15092;SF-2026-ARXIV-2607-15115;SF-2026-ARXIV-2607-15143;SF-2026-ARXIV-2607-15161;SF-2026-ARXIV-2607-15190;SF-2026-ARXIV-2607-15193;SF-2026-ARXIV-2607-15205;SF-2026-ARXIV-2607-15207;SF-2026-ARXIV-2607-15253;SF-2026-ARXIV-2607-15257;SF-2026-ARXIV-2607-15263 | all registered category pages; cross-category dedup complete | 2026-07-17T09:00:00+08:00 | sha256:bc0b07a10e4c584d556aaaa4ea79928e129c26fea3192c73221b5d93287cb35d | — |
<!-- coverage:SRC-ARXIV:20260717:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14103 | arXiv:2607.14103v1 | paper-v1:2607.14103 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14103 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14107 | arXiv:2607.14107v1 | paper-v1:2607.14107 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14107 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14108 | arXiv:2607.14108v1 | paper-v1:2607.14108 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14108 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14109 | arXiv:2607.14109v1 | paper-v1:2607.14109 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14109 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14145 | arXiv:2607.14145v1 | paper-v1:2607.14145 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14145 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14155 | arXiv:2607.14155v1 | paper-v1:2607.14155 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14155 | self | — | new_in_window | PLATFORM-PRODUCTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14157 | arXiv:2607.14157v1 | paper-v1:2607.14157 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14157 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14159 | arXiv:2607.14159v1 | paper-v1:2607.14159 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14159 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14166 | arXiv:2607.14166v1 | paper-v1:2607.14166 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14166 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14167 | arXiv:2607.14167v1 | paper-v1:2607.14167 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14167 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14169 | arXiv:2607.14169v1 | paper-v1:2607.14169 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14169 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14171 | arXiv:2607.14171v1 | paper-v1:2607.14171 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14171 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14180 | arXiv:2607.14180v1 | paper-v1:2607.14180 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14180 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14186 | arXiv:2607.14186v1 | paper-v1:2607.14186 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14186 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14189 | arXiv:2607.14189v1 | paper-v1:2607.14189 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14189 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14194 | arXiv:2607.14194v1 | paper-v1:2607.14194 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14194 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14202 | arXiv:2607.14202v1 | paper-v1:2607.14202 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14202 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14236 | arXiv:2607.14236v1 | paper-v1:2607.14236 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14236 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14252 | arXiv:2607.14252v1 | paper-v1:2607.14252 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14252 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14275 | arXiv:2607.14275v1 | paper-v1:2607.14275 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14275 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14277 | arXiv:2607.14277v1 | paper-v1:2607.14277 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14277 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14280 | arXiv:2607.14280v1 | paper-v1:2607.14280 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14280 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14285 | arXiv:2607.14285v1 | paper-v1:2607.14285 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14285 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14327 | arXiv:2607.14327v1 | paper-v1:2607.14327 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14327 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14336 | arXiv:2607.14336v1 | paper-v1:2607.14336 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14336 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14340 | arXiv:2607.14340v1 | paper-v1:2607.14340 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14340 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14386 | arXiv:2607.14386v1 | paper-v1:2607.14386 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14386 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14390 | arXiv:2607.14390v1 | paper-v1:2607.14390 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14390 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14396 | arXiv:2607.14396v1 | paper-v1:2607.14396 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14396 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14399 | arXiv:2607.14399v1 | paper-v1:2607.14399 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14399 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14408 | arXiv:2607.14408v1 | paper-v1:2607.14408 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14408 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14431 | arXiv:2607.14431v1 | paper-v1:2607.14431 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14431 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14439 | arXiv:2607.14439v1 | paper-v1:2607.14439 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14439 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14443 | arXiv:2607.14443v1 | paper-v1:2607.14443 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14443 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14493 | arXiv:2607.14493v1 | paper-v1:2607.14493 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14493 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14499 | arXiv:2607.14499v1 | paper-v1:2607.14499 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14499 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14506 | arXiv:2607.14506v1 | paper-v1:2607.14506 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14506 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14512 | arXiv:2607.14512v1 | paper-v1:2607.14512 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14512 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14541 | arXiv:2607.14541v1 | paper-v1:2607.14541 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14541 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14543 | arXiv:2607.14543v1 | paper-v1:2607.14543 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14543 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14547 | arXiv:2607.14547v1 | paper-v1:2607.14547 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14547 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14548 | arXiv:2607.14548v1 | paper-v1:2607.14548 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14548 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14568 | arXiv:2607.14568v1 | paper-v1:2607.14568 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14568 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14570 | arXiv:2607.14570v1 | paper-v1:2607.14570 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14570 | self | — | new_in_window | PLATFORM-MONITORING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14573 | arXiv:2607.14573v1 | paper-v1:2607.14573 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14573 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14611 | arXiv:2607.14611v1 | paper-v1:2607.14611 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14611 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14618 | arXiv:2607.14618v1 | paper-v1:2607.14618 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14618 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14635 | arXiv:2607.14635v1 | paper-v1:2607.14635 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14635 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14642 | arXiv:2607.14642v1 | paper-v1:2607.14642 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14642 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14647 | arXiv:2607.14647v1 | paper-v1:2607.14647 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14647 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14651 | arXiv:2607.14651v1 | paper-v1:2607.14651 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14651 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14695 | arXiv:2607.14695v1 | paper-v1:2607.14695 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14695 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14698 | arXiv:2607.14698v1 | paper-v1:2607.14698 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14698 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14739 | arXiv:2607.14739v1 | paper-v1:2607.14739 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14739 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14754 | arXiv:2607.14754v1 | paper-v1:2607.14754 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14754 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14777 | arXiv:2607.14777v1 | paper-v1:2607.14777 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14777 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14811 | arXiv:2607.14811v1 | paper-v1:2607.14811 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14811 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14817 | arXiv:2607.14817v1 | paper-v1:2607.14817 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14817 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14852 | arXiv:2607.14852v1 | paper-v1:2607.14852 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14852 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14890 | arXiv:2607.14890v1 | paper-v1:2607.14890 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14890 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14896 | arXiv:2607.14896v1 | paper-v1:2607.14896 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14896 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14903 | arXiv:2607.14903v1 | paper-v1:2607.14903 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14903 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14908 | arXiv:2607.14908v1 | paper-v1:2607.14908 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14908 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14952 | arXiv:2607.14952v1 | paper-v1:2607.14952 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14952 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14989 | arXiv:2607.14989v1 | paper-v1:2607.14989 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14989 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15065 | arXiv:2607.15065v1 | paper-v1:2607.15065 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15065 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15092 | arXiv:2607.15092v1 | paper-v1:2607.15092 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15092 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15115 | arXiv:2607.15115v1 | paper-v1:2607.15115 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15115 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15143 | arXiv:2607.15143v1 | paper-v1:2607.15143 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15143 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15161 | arXiv:2607.15161v1 | paper-v1:2607.15161 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15161 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15190 | arXiv:2607.15190v1 | paper-v1:2607.15190 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15190 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15193 | arXiv:2607.15193v1 | paper-v1:2607.15193 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15193 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15205 | arXiv:2607.15205v1 | paper-v1:2607.15205 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15205 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15207 | arXiv:2607.15207v1 | paper-v1:2607.15207 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15207 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15253 | arXiv:2607.15253v1 | paper-v1:2607.15253 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15253 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15257 | arXiv:2607.15257v1 | paper-v1:2607.15257 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15257 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-15263 | arXiv:2607.15263v1 | paper-v1:2607.15263 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15263 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14103 | RP-85bd31597083bdad | standard | arXiv:2607.14103v1 | SRC-ARXIV@arXiv:2607.14103v1 | https://arxiv.org/html/2607.14103v1#S2 — 2. Methods; https://arxiv.org/html/2607.14103v1#S2.SS6 — 2.6. Cross-Architecture Alignment (C3) | https://arxiv.org/html/2607.14103v1#S2.SS5 — 2.5. SAE Feature Survival Analysis (C2); https://arxiv.org/html/2607.14103v1#S2.SS7 — 2.7. Task-Level Evaluation Protocol | https://arxiv.org/html/2607.14103v1#S4 — 4. Discussion; https://arxiv.org/html/2607.14103v1#S4.SS4 — 4.4. Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14103 | complete |
| SF-2026-ARXIV-2607-14107 | RP-d421f4043c9860f1 | deep | arXiv:2607.14107v1 | SRC-ARXIV@arXiv:2607.14107v1 | https://arxiv.org/html/2607.14107v1#S4 — 4 Polestar Methodology; https://arxiv.org/html/2607.14107v1#S4.SS3 — 4.3 Polestar System Optimization | https://arxiv.org/html/2607.14107v1#S5 — 5 Experimental Evaluations; https://arxiv.org/html/2607.14107v1#A4 — Appendix D Additional Evaluations | https://arxiv.org/html/2607.14107v1#S5.SS3 — 5.3 Discussions and Ablations; https://arxiv.org/html/2607.14107v1#S6 — 6 Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14107 | complete |
| SF-2026-ARXIV-2607-14108 | RP-875438e8b6368832 | standard | arXiv:2607.14108v1 | SRC-ARXIV@arXiv:2607.14108v1 | https://arxiv.org/html/2607.14108v1#S3 — 3 Methodology | https://arxiv.org/html/2607.14108v1#S3.SS4 — 3.4 Experimental Setup; https://arxiv.org/html/2607.14108v1#S4 — 4 Results | https://arxiv.org/html/2607.14108v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14108v1#S6 — 6 Limitations | Exact v1 links https://github.com/antl3x/ToolRAG, https://openai.com/index/introducing-gpt-5-3-codex/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14108 | complete |
| SF-2026-ARXIV-2607-14109 | RP-1856fcc2267e28eb | standard | arXiv:2607.14109v1 | SRC-ARXIV@arXiv:2607.14109v1 | https://arxiv.org/html/2607.14109v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14109v1#A2 — Appendix B Model configurations | https://arxiv.org/html/2607.14109v1#A1 — Appendix A Self-Analogical failure-mode analysis; https://arxiv.org/html/2607.14109v1#S3.SS5 — 3.5 Evaluation metrics | https://arxiv.org/html/2607.14109v1#A1 — Appendix A Self-Analogical failure-mode analysis; https://arxiv.org/html/2607.14109v1#A6 — Appendix F Discussion | Exact v1 links https://huggingface.co/datasets/bigbio/med_qa, https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro, https://huggingface.co/datasets/update0909/cure-bench-reasoning-traces; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14109 | complete |
| SF-2026-ARXIV-2607-14145 | RP-99956c2ee6aab28f | deep | arXiv:2607.14145v1 | SRC-ARXIV@arXiv:2607.14145v1 | https://arxiv.org/html/2607.14145v1#A2.SS1 — B.1 System prompt for deep research agent; https://arxiv.org/html/2607.14145v1#A2.SS2 — B.2 System Prompt for teacher model counterfactual anchor round hypothesis | https://arxiv.org/html/2607.14145v1#A2.SS4 — B.4 Prompt for LLM-As-Judge evaluation; https://arxiv.org/html/2607.14145v1#A3.SS3 — C.3 Statistical analysis of counterfactual anchor rounds | https://arxiv.org/html/2607.14145v1#S6 — 6 Conclusion and limitation; https://arxiv.org/html/2607.14145v1#S5.SS4 — 5.4 Further analysis and discussions | Exact v1 links https://github.com/THUDM/slime, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14145 | complete |
| SF-2026-ARXIV-2607-14155 | RP-410ba4f46976e468 | standard | arXiv:2607.14155v1 | SRC-ARXIV@arXiv:2607.14155v1 | https://arxiv.org/html/2607.14155v1#S4 — IV Study Method; https://arxiv.org/html/2607.14155v1#S4.SS1 — IV-A Design and case roles | https://arxiv.org/html/2607.14155v1#S4.SS4 — IV-D Analysis; https://arxiv.org/html/2607.14155v1#S7 — VII Implementation Status and Evaluation Plan | https://arxiv.org/html/2607.14155v1#S10 — X Conclusion; https://arxiv.org/html/2607.14155v1#S6.SS11 — VI-K Threat boundary | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14155 | complete |
| SF-2026-ARXIV-2607-14157 | RP-ad6409ed06ca068f | standard | arXiv:2607.14157v1 | SRC-ARXIV@arXiv:2607.14157v1 | https://arxiv.org/html/2607.14157v1#S1 — 1. Introduction; https://arxiv.org/html/2607.14157v1#S1.SS0.SSS0.Px1 — Contributions. | https://arxiv.org/html/2607.14157v1#S1.SS0.SSS0.Px2 — Results preview.; https://arxiv.org/html/2607.14157v1#S3 — 3. Problem Setup and Benchmark | https://arxiv.org/html/2607.14157v1#S2.SS0.SSS0.Px3 — Retrieval-augmented generation: reliability and threats.; https://arxiv.org/html/2607.14157v1#S7 — 7. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14157 | complete |
| SF-2026-ARXIV-2607-14159 | RP-f90289d494fbc395 | standard | arXiv:2607.14159v1 | SRC-ARXIV@arXiv:2607.14159v1 | https://arxiv.org/html/2607.14159v1#S2 — 2 Method; https://arxiv.org/html/2607.14159v1#A2 — Appendix B Implementation Details | https://arxiv.org/html/2607.14159v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.14159v1#S3 — 3 Experiments | https://arxiv.org/html/2607.14159v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.14159v1#S4 — 4 Conclusion | Exact v1 links https://github.com/HowieHwong/MemoHarness, https://github.com/anthropics/claude-code, https://github.com/openai/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14159 | complete |
| SF-2026-ARXIV-2607-14166 | RP-3aaec8a6b1b2723e | deep | arXiv:2607.14166v1 | SRC-ARXIV@arXiv:2607.14166v1 | https://arxiv.org/pdf/2607.14166v1#page=5 — PDF page 5; https://arxiv.org/pdf/2607.14166v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.14166v1#page=15 — PDF page 15; https://arxiv.org/pdf/2607.14166v1#page=20 — PDF page 20 | https://arxiv.org/pdf/2607.14166v1#page=25 — PDF page 25; https://arxiv.org/pdf/2607.14166v1#page=30 — PDF page 30 | Exact v1 links https://github.com/awslabs/shuttle; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14166 | complete |
| SF-2026-ARXIV-2607-14167 | RP-1760fc5a4a07f742 | standard | arXiv:2607.14167v1 | SRC-ARXIV@arXiv:2607.14167v1 | https://arxiv.org/html/2607.14167v1#S2 — 2. Background and System; https://arxiv.org/html/2607.14167v1#S3 — 3. Study Design | https://arxiv.org/html/2607.14167v1#S4 — 4. Results; https://arxiv.org/html/2607.14167v1#S3 — 3. Study Design | https://arxiv.org/html/2607.14167v1#S2.SS3 — 2.3. One Failure, Four Feedback Policies; https://arxiv.org/html/2607.14167v1#S4.SS4 — 4.4. When the Validator Cannot Expose the Hidden Failure | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14167 | complete |
| SF-2026-ARXIV-2607-14169 | RP-e3e5e45be0b98821 | standard | arXiv:2607.14169v1 | SRC-ARXIV@arXiv:2607.14169v1 | https://arxiv.org/html/2607.14169v1#S2 — 2 Setup and Methods; https://arxiv.org/html/2607.14169v1#S1.SS1 — 1.1 The Code World Model paradigm | https://arxiv.org/html/2607.14169v1#S2.SS5 — 2.5 Experimental configuration; https://arxiv.org/html/2607.14169v1#S3.SS3 — 3.3 The rare-rule instrument: verified but wrong at play (headline result) | https://arxiv.org/html/2607.14169v1#S5.SS4 — 5.4 Conclusion: translation, not inference; https://arxiv.org/html/2607.14169v1#S6 — 6 Imperfect Information: The Inference Function as a New Failure Surface | Exact v1 links https://github.com/JaviMaligno/code-world-models, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14169 | complete |
| SF-2026-ARXIV-2607-14171 | RP-e19e617d19ee0d95 | standard | arXiv:2607.14171v1 | SRC-ARXIV@arXiv:2607.14171v1 | https://arxiv.org/html/2607.14171v1#S4.SS3 — 4.3 Algorithm | https://arxiv.org/html/2607.14171v1#S4.SS4 — 4.4 Theoretical analysis; https://arxiv.org/html/2607.14171v1#S5 — 5 Experiments | https://arxiv.org/html/2607.14171v1#S6 — 6 Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14171 | complete |
| SF-2026-ARXIV-2607-14180 | RP-8584a884f095d076 | standard | arXiv:2607.14180v1 | SRC-ARXIV@arXiv:2607.14180v1 | https://arxiv.org/html/2607.14180v1#A3 — Appendix C Architecture and Optimization Details; https://arxiv.org/html/2607.14180v1#S2 — 2 Methodology | https://arxiv.org/html/2607.14180v1#S3 — 3 Experimental Evaluation; https://arxiv.org/html/2607.14180v1#A6 — Appendix F Ablation Studies | https://arxiv.org/html/2607.14180v1#S4 — 4 Conclusion | Exact v1 links https://github.com/FlyingWorkshop/RENEW, http://github.com/RobertTLange/gymnax, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14180 | complete |
| SF-2026-ARXIV-2607-14186 | RP-5c3ab04384f11e1f | standard | arXiv:2607.14186v1 | SRC-ARXIV@arXiv:2607.14186v1 | https://arxiv.org/html/2607.14186v1#S3 — 3 Method | https://arxiv.org/html/2607.14186v1#A5 — Appendix E Detailed Evaluation Results; https://arxiv.org/html/2607.14186v1#A6 — Appendix F Terminal Ablation Details | https://arxiv.org/html/2607.14186v1#S6 — 6 Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14186 | complete |
| SF-2026-ARXIV-2607-14189 | RP-0b0563686a602ff2 | standard | arXiv:2607.14189v1 | SRC-ARXIV@arXiv:2607.14189v1 | https://arxiv.org/html/2607.14189v1#A2.SS1 — B.1 Overview and Design Rationale; https://arxiv.org/html/2607.14189v1#Sx4 — Evaluation Framework | https://arxiv.org/html/2607.14189v1#A3 — Appendix C Board4 Analysis; https://arxiv.org/html/2607.14189v1#A4.SS1 — D.1 Entity Fidelity Analysis | https://arxiv.org/html/2607.14189v1#Sx6 — Limitations; https://arxiv.org/html/2607.14189v1#Sx7 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14189 | complete |
| SF-2026-ARXIV-2607-14194 | RP-785bb98257005605 | standard | arXiv:2607.14194v1 | SRC-ARXIV@arXiv:2607.14194v1 | https://arxiv.org/html/2607.14194v1#S3 — 3 Method; https://arxiv.org/html/2607.14194v1#S4 — 4 Evaluation Framework and Implementation | https://arxiv.org/html/2607.14194v1#A2 — Appendix B Additional Experimental Results; https://arxiv.org/html/2607.14194v1#A2.SS1 — B.1 Per-Concept Any-Hit Results | https://arxiv.org/html/2607.14194v1#S5.SS5 — 5.5 Discussion; https://arxiv.org/html/2607.14194v1#S6 — 6 Conclusion | Exact v1 links https://github.com/ultralytics/ultralytics, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14194 | complete |
| SF-2026-ARXIV-2607-14202 | RP-8cb4b5208d866243 | standard | arXiv:2607.14202v1 | SRC-ARXIV@arXiv:2607.14202v1 | https://arxiv.org/html/2607.14202v1#S3.SS1 — 3.1 Benchmark Design; https://arxiv.org/html/2607.14202v1#S1.SS1 — A.1 Performance of Proprietary Models | https://arxiv.org/html/2607.14202v1#S2.SS2 — 2.2 Benchmarks for Video Generation; https://arxiv.org/html/2607.14202v1#S3.SS1 — 3.1 Benchmark Design | https://arxiv.org/html/2607.14202v1#S5 — 5 Conclusion | Exact v1 links https://github.com/cactusqq/KeyFrame-Compass, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14202 | complete |
| SF-2026-ARXIV-2607-14236 | RP-4d5180b351a4a7af | deep | arXiv:2607.14236v1 | SRC-ARXIV@arXiv:2607.14236v1 | https://arxiv.org/html/2607.14236v1#S3 — 3 Methods; https://arxiv.org/html/2607.14236v1#S3.SS4 — 3.4 Pipeline overview and system implementation | https://arxiv.org/html/2607.14236v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.14236v1#A10 — Appendix J Extended failure-mode analysis | https://arxiv.org/html/2607.14236v1#S6 — 6 Conclusion and Limitations; https://arxiv.org/html/2607.14236v1#A10 — Appendix J Extended failure-mode analysis | Exact v1 links https://github.com/flexivrobotics/flexiv_tdk, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14236 | complete |
| SF-2026-ARXIV-2607-14252 | RP-5707639a733c5d2e | standard | arXiv:2607.14252v1 | SRC-ARXIV@arXiv:2607.14252v1 | https://arxiv.org/html/2607.14252v1#S4 — IV Method; https://arxiv.org/html/2607.14252v1#A1.SS1 — A-A Implementation Overview | https://arxiv.org/html/2607.14252v1#A2.SS1 — B-A Benchmark Construction; https://arxiv.org/html/2607.14252v1#A2.SS4 — B-D Evaluation Protocol | https://arxiv.org/html/2607.14252v1#A1.SS7 — A-G Limitations; https://arxiv.org/html/2607.14252v1#S6 — VI Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14252 | complete |
| SF-2026-ARXIV-2607-14275 | RP-daebe2a419e32c28 | standard | arXiv:2607.14275v1 | SRC-ARXIV@arXiv:2607.14275v1 | https://arxiv.org/html/2607.14275v1#S2.SS1 — 2.1 From Prompt Design to Context Design; https://arxiv.org/html/2607.14275v1#S4.SS1 — 4.1 Study Design | https://arxiv.org/html/2607.14275v1#S3.SS4 — 3.4 Isolation from Behavioral Evaluation; https://arxiv.org/html/2607.14275v1#S4 — 4 Experimental Validation | https://arxiv.org/html/2607.14275v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ProofAgent-ai/proofagent-harness, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14275 | complete |
| SF-2026-ARXIV-2607-14277 | RP-549c0321e345ccda | standard | arXiv:2607.14277v1 | SRC-ARXIV@arXiv:2607.14277v1 | https://arxiv.org/html/2607.14277v1#A2.SS3 — B.3 Model Token Confidence vs. Latent Adequacy Signal; https://arxiv.org/html/2607.14277v1#S4.SS1 — 4.1 Efficient Multi-Model Collaboration | https://arxiv.org/html/2607.14277v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.14277v1#A2 — Appendix B Additional Experiments | https://arxiv.org/html/2607.14277v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.14277v1#S5 — 5 Conclusion | Exact v1 links https://github.com/Amirhosein-gh98/Multi-Head-Latent-Control, https://github.com/EvolvingLMMs-Lab/open-r1-multimodal, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14277 | complete |
| SF-2026-ARXIV-2607-14280 | RP-7c39b5bb67ca7057 | deep | arXiv:2607.14280v1 | SRC-ARXIV@arXiv:2607.14280v1 | https://arxiv.org/pdf/2607.14280v1#page=3 — PDF page 3; https://arxiv.org/pdf/2607.14280v1#page=7 — PDF page 7 | https://arxiv.org/pdf/2607.14280v1#page=12 — PDF page 12; https://arxiv.org/pdf/2607.14280v1#page=17 — PDF page 17 | https://arxiv.org/pdf/2607.14280v1#page=23 — PDF page 23; https://arxiv.org/pdf/2607.14280v1#page=26 — PDF page 26 | Exact v1 links https://github.com/pegah-kh/dimas, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14280 | complete |
| SF-2026-ARXIV-2607-14285 | RP-2fee7db57353e7c8 | standard | arXiv:2607.14285v1 | SRC-ARXIV@arXiv:2607.14285v1 | https://arxiv.org/html/2607.14285v1#A1.SS1 — A.1 Base System Prompt; https://arxiv.org/html/2607.14285v1#S3 — 3 Methodology | https://arxiv.org/html/2607.14285v1#S2.SS3 — 2.3 Agent Safety and Tool-Calling Evaluation; https://arxiv.org/html/2607.14285v1#S3.SS3 — 3.3 Experimental Setup | https://arxiv.org/html/2607.14285v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14285v1#S6 — 6 Conclusion | Exact v1 links https://github.com/aryankeluskar/ToolAlignBench, https://github.com/T3-Content/SnitchBench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14285 | complete |
| SF-2026-ARXIV-2607-14327 | RP-e9077c3ce9e64baa | standard | arXiv:2607.14327v1 | SRC-ARXIV@arXiv:2607.14327v1 | https://arxiv.org/html/2607.14327v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14327v1#S2 — 2 Related Work | https://arxiv.org/html/2607.14327v1#S4 — 4 Experiments; https://arxiv.org/html/2607.14327v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.14327v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14327 | complete |
| SF-2026-ARXIV-2607-14336 | RP-706524267f48fdd5 | standard | arXiv:2607.14336v1 | SRC-ARXIV@arXiv:2607.14336v1 | https://arxiv.org/html/2607.14336v1#S3 — 3 Methods; https://arxiv.org/html/2607.14336v1#S4.SS1 — 4.1 Initial scores across models | https://arxiv.org/html/2607.14336v1#A3 — Appendix C Plane Integration and Experimental Setup; https://arxiv.org/html/2607.14336v1#A4 — Appendix D Results Summary | https://arxiv.org/html/2607.14336v1#S4.SS2 — 4.2 Diagnosing failure modes; https://arxiv.org/html/2607.14336v1#S5 — 5 Limitations | Exact v1 links https://github.com/trail-ml/agent-cow-python, https://github.com/JoannaRoy/plane-cow, https://github.com/JoannaRoy/plane-cow/blob/preview/results.zip; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14336 | complete |
| SF-2026-ARXIV-2607-14340 | RP-ec1cb05798858480 | deep | arXiv:2607.14340v1 | SRC-ARXIV@arXiv:2607.14340v1 | https://arxiv.org/html/2607.14340v1#S3 — III Method: The Verifier-Driven Loop; https://arxiv.org/html/2607.14340v1#S6 — VI From Components to a Running System | https://arxiv.org/html/2607.14340v1#S3.SS3 — III-C Study Setup | https://arxiv.org/html/2607.14340v1#S11 — XI Conclusion; https://arxiv.org/html/2607.14340v1#S7 — VII Failure Modes: The Limits of Proof | Exact v1 links https://github.com/tobiasphilipp/experimental-agentic-verified-software, https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html, https://github.com/rod-chapman/SPARKNaCl; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14340 | complete |
| SF-2026-ARXIV-2607-14386 | RP-0d9386aae936aa94 | standard | arXiv:2607.14386v1 | SRC-ARXIV@arXiv:2607.14386v1 | https://arxiv.org/html/2607.14386v1#A3 — Appendix C Details on CIPHER and DES design and implementation; https://arxiv.org/html/2607.14386v1#S3 — 3 The Decoupled Exploration-Selection (DES) Framework | https://arxiv.org/html/2607.14386v1#A4 — Appendix D Additional results; https://arxiv.org/html/2607.14386v1#S3.SS3 — 3.3 Aggregating diverse execution results | https://arxiv.org/html/2607.14386v1#A2 — Appendix B Discussion and limitations; https://arxiv.org/html/2607.14386v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/amazon/Titan-text-embeddings-v2, https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14386 | complete |
| SF-2026-ARXIV-2607-14390 | RP-d563c21daa40103d | standard | arXiv:2607.14390v1 | SRC-ARXIV@arXiv:2607.14390v1 | https://arxiv.org/html/2607.14390v1#S1 — 1 The question an agent actually asks; https://arxiv.org/html/2607.14390v1#S2 — 2 A worked example | https://arxiv.org/html/2607.14390v1#S8 — 8 Evaluation: answer-sufficiency, not rank; https://arxiv.org/html/2607.14390v1#S8.SS2 — 8.2 Gating and the rationale ablation | https://arxiv.org/html/2607.14390v1#S11 — 11 Limitations; https://arxiv.org/html/2607.14390v1#S12 — 12 Conclusion | Exact v1 links https://github.com/rekal-dev/rekal-cli, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14390 | complete |
| SF-2026-ARXIV-2607-14396 | RP-f4bd9889a733d04f | deep | arXiv:2607.14396v1 | SRC-ARXIV@arXiv:2607.14396v1 | https://arxiv.org/html/2607.14396v1#Pt0.A1 — Appendix 0.A Appendix: Analysis of the Performance of Generator–Evaluator-Supervisor framework; https://arxiv.org/html/2607.14396v1#S2 — 2 CatalogAgent: A Supervisor-mediated Self-Learning System | https://arxiv.org/html/2607.14396v1#S3 — 3 Experiments and Results; https://arxiv.org/html/2607.14396v1#Pt0.A1 — Appendix 0.A Appendix: Analysis of the Performance of Generator–Evaluator-Supervisor framework | https://arxiv.org/html/2607.14396v1#S5 — 5 Conclusion and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14396 | complete |
| SF-2026-ARXIV-2607-14399 | RP-e0030c5ff64d8b93 | standard | arXiv:2607.14399v1 | SRC-ARXIV@arXiv:2607.14399v1 | https://arxiv.org/html/2607.14399v1#Sx3 — 3. Methods; https://arxiv.org/html/2607.14399v1#Sx7 — 7. Process integrity as method | https://arxiv.org/html/2607.14399v1#Sx4 — 4. Results; https://arxiv.org/html/2607.14399v1#Sx5.SSx2 — 5.2 What these results do not license | https://arxiv.org/html/2607.14399v1#Sx5 — 5. Discussion; https://arxiv.org/html/2607.14399v1#Sx6 — 6. Limitations | Exact v1 links https://github.com/Aargau/latent-underground/releases/tag/v1.0-arxiv, https://github.com/UKGovernmentBEIS/inspect_ai, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14399 | complete |
| SF-2026-ARXIV-2607-14408 | RP-6e9a28cb77a0f5fe | standard | arXiv:2607.14408v1 | SRC-ARXIV@arXiv:2607.14408v1 | https://arxiv.org/html/2607.14408v1#S4 — 4 Our Method | https://arxiv.org/html/2607.14408v1#S5 — 5 Results; https://arxiv.org/html/2607.14408v1#S5.SS2 — 5.2 Main Results on Prompt Evolution | https://arxiv.org/html/2607.14408v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14408 | complete |
| SF-2026-ARXIV-2607-14431 | RP-fceadda96f53fd3f | deep | arXiv:2607.14431v1 | SRC-ARXIV@arXiv:2607.14431v1 | https://arxiv.org/html/2607.14431v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14431v1#S4.SS10 — 4.10 Cross-architecture byte-exactness: a pre-registered B200 replay | https://arxiv.org/html/2607.14431v1#S4 — 4 Empirical Results | https://arxiv.org/html/2607.14431v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14431v1#S5.SS3 — 5.3 Limitations | Exact v1 links https://huggingface.co/Qwen/Qwen3.6-35B-A3B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14431 | complete |
| SF-2026-ARXIV-2607-14439 | RP-ec78d15007537748 | standard | arXiv:2607.14439v1 | SRC-ARXIV@arXiv:2607.14439v1 | https://arxiv.org/html/2607.14439v1#S3 — III Methodology | https://arxiv.org/html/2607.14439v1#S2.SS2 — II-B Benchmarks for Generalist Robot Policies; https://arxiv.org/html/2607.14439v1#S2.SS3 — II-C Sample-efficient Robot Policy Evaluation | https://arxiv.org/html/2607.14439v1#S5.SS1 — V-A Limitations & Future Work; https://arxiv.org/html/2607.14439v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14439 | complete |
| SF-2026-ARXIV-2607-14443 | RP-62253a94abcd48e9 | standard | arXiv:2607.14443v1 | SRC-ARXIV@arXiv:2607.14443v1 | https://arxiv.org/html/2607.14443v1#S4 — 4 System Design and Implementation; https://arxiv.org/html/2607.14443v1#S2.SS4 — 2.4 Design Requirements | https://arxiv.org/html/2607.14443v1#S5 — 5 Results; https://arxiv.org/html/2607.14443v1#S5.SS1 — 5.1 Main Results | https://arxiv.org/html/2607.14443v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.14443v1#S6 — 6 Discussion | Exact v1 links https://developers.openai.com/codex/cli, https://claude.com/product/claude-code, https://opencode.ai/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14443 | complete |
| SF-2026-ARXIV-2607-14493 | RP-9000c788b1feb7a0 | deep | arXiv:2607.14493v1 | SRC-ARXIV@arXiv:2607.14493v1 | https://arxiv.org/html/2607.14493v1#S5 — 5 Evaluation Framework; https://arxiv.org/html/2607.14493v1#S3 — 3 Problem Statement and Threat Model | https://arxiv.org/html/2607.14493v1#S10.SS2 — 10.2 Experimental Safeguards; https://arxiv.org/html/2607.14493v1#S5 — 5 Evaluation Framework | https://arxiv.org/html/2607.14493v1#S3 — 3 Problem Statement and Threat Model; https://arxiv.org/html/2607.14493v1#S8 — 8 Discussion | Exact v1 links https://doi.org/10.18653/v1/2025.emnlp-demos.55, https://aclanthology.org/2025.emnlp-demos.55/, https://owasp.org/www-project-top-10-for-large-language-model-applications/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14493 | complete |
| SF-2026-ARXIV-2607-14499 | RP-42b02dde628760ca | standard | arXiv:2607.14499v1 | SRC-ARXIV@arXiv:2607.14499v1 | https://arxiv.org/html/2607.14499v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14499v1#A5 — Appendix E Evaluated Models | https://arxiv.org/html/2607.14499v1#S2.SS1 — 2.1 Evaluation and Benchmarking MLLMs; https://arxiv.org/html/2607.14499v1#S5.SS3 — 5.3 Evaluation Result (RQ\scriptsize3⃝) | https://arxiv.org/html/2607.14499v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.14499v1#S7 — 7 Limitations | Exact v1 links https://github.com/williamium3000/cedi, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14499 | complete |
| SF-2026-ARXIV-2607-14506 | RP-743eb1153474e2d0 | standard | arXiv:2607.14506v1 | SRC-ARXIV@arXiv:2607.14506v1 | https://arxiv.org/html/2607.14506v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14506v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.14506v1#A2 — Appendix B Experimental Setup and Hyperparameters; https://arxiv.org/html/2607.14506v1#A2.SS3 — B.3 Evaluation Protocol | https://arxiv.org/html/2607.14506v1#S6 — 6 Discussion; https://arxiv.org/html/2607.14506v1#S8 — 8 Conclusion | Exact v1 links https://github.com/uiuc-kang-lab/rlvr_generalization_bounds, https://huggingface.co/collections/uiuc-kang-lab/rlvr-generalization-bounds, https://github.com/huggingface/Math-Verify; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14506 | complete |
| SF-2026-ARXIV-2607-14512 | RP-19bfa259d7c653e1 | standard | arXiv:2607.14512v1 | SRC-ARXIV@arXiv:2607.14512v1 | https://arxiv.org/html/2607.14512v1#A1 — Appendix A System Prompt; https://arxiv.org/html/2607.14512v1#S2 — 2 Method | https://arxiv.org/html/2607.14512v1#A6 — Appendix F Evaluation Protocol; https://arxiv.org/html/2607.14512v1#A7 — Appendix G Additional Experiments | https://arxiv.org/html/2607.14512v1#A4 — Appendix D Limitations and Discussion; https://arxiv.org/html/2607.14512v1#A9 — Appendix I Failure Case Analysis | Exact v1 links https://github.com/SXKDZ/RetroAgent, https://huggingface.co/SXKDZ/RetroAgent, https://github.com/THUDM/slime; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14512 | complete |
| SF-2026-ARXIV-2607-14541 | RP-e6fe18c7f8c53869 | deep | arXiv:2607.14541v1 | SRC-ARXIV@arXiv:2607.14541v1 | https://arxiv.org/html/2607.14541v1#S3 — 3 Atrex-Bench: Design; https://arxiv.org/html/2607.14541v1#S5.SS2 — 5.2 Architecture and Workflow | https://arxiv.org/html/2607.14541v1#A1 — Appendix A Per-Operator Results; https://arxiv.org/html/2607.14541v1#S2.SS1 — 2.1 LLM Kernel Generation Benchmarks | https://arxiv.org/html/2607.14541v1#S6 — 6 Discussion; https://arxiv.org/html/2607.14541v1#S6.SS1 — 6.1 Limitations | Exact v1 links https://github.com/alibaba/atrex-bench, https://github.com/alibaba/atrex-kernel-agent, https://github.com/ROCm/aiter; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14541 | complete |
| SF-2026-ARXIV-2607-14543 | RP-1d243cce2269eec2 | standard | arXiv:2607.14543v1 | SRC-ARXIV@arXiv:2607.14543v1 | https://arxiv.org/html/2607.14543v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14543v1#S2 — 2 Related Work | https://arxiv.org/html/2607.14543v1#S4.SS3 — 4.3 Ablation Analysis; https://arxiv.org/html/2607.14543v1#S3.SS2 — 3.2 Task and Safety Evaluation | https://arxiv.org/html/2607.14543v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.14543v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14543 | complete |
| SF-2026-ARXIV-2607-14547 | RP-4b9ef2c3b5f855d1 | standard | arXiv:2607.14547v1 | SRC-ARXIV@arXiv:2607.14547v1 | https://arxiv.org/html/2607.14547v1#S3 — 3 Method | https://arxiv.org/html/2607.14547v1#A3 — Appendix C Detailed Ablation Discussion; https://arxiv.org/html/2607.14547v1#A8 — Appendix H Failure Analysis | https://arxiv.org/html/2607.14547v1#A3 — Appendix C Detailed Ablation Discussion; https://arxiv.org/html/2607.14547v1#A8 — Appendix H Failure Analysis | Exact v1 links https://huggingface.co/datasets/Mini-o3/Mini-o3-Coldstart-Dataset, https://huggingface.co/datasets/Mini-o3/DeepEyes_train_4K, https://huggingface.co/datasets/Mini-o3/VisualProbe_train; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14547 | complete |
| SF-2026-ARXIV-2607-14548 | RP-4eb87843d078eb91 | standard | arXiv:2607.14548v1 | SRC-ARXIV@arXiv:2607.14548v1 | https://arxiv.org/html/2607.14548v1#S3 — 3 Model Design; https://arxiv.org/html/2607.14548v1#S2.SS1 — 2.1 Vision-Native Models for GUI Control | https://arxiv.org/html/2607.14548v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.14548v1#S6.SS1 — 6.1 Benchmarks | https://arxiv.org/html/2607.14548v1#S7 — 7 Conclusion and Future Work | Exact v1 links https://huggingface.co/Qwen/Qwen3.6-35B-A3B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14548 | complete |
| SF-2026-ARXIV-2607-14568 | RP-c4046bf61d149f83 | standard | arXiv:2607.14568v1 | SRC-ARXIV@arXiv:2607.14568v1 | https://arxiv.org/html/2607.14568v1#S2.SS2 — 2.2 The model | https://arxiv.org/html/2607.14568v1#S7 — 7 Evaluation Summary | https://arxiv.org/html/2607.14568v1#S9 — 9 Conclusion | Exact v1 links https://huggingface.co/openbmb/MiniCPM-V-4.6, https://github.com/karpathy/llama2.c, https://github.com/ggml-org/llama.cpp; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14568 | complete |
| SF-2026-ARXIV-2607-14570 | RP-b977a882cdd7fe7a | deep | arXiv:2607.14570v1 | SRC-ARXIV@arXiv:2607.14570v1 | https://arxiv.org/html/2607.14570v1#A2.SS1 — B.1 System Prompt; https://arxiv.org/html/2607.14570v1#S3 — 3 Experiment Design | https://arxiv.org/html/2607.14570v1#A1 — Appendix A Evaluation Scope: Excluding the check_in_cdk_out_directory Side Task; https://arxiv.org/html/2607.14570v1#S3 — 3 Experiment Design | https://arxiv.org/html/2607.14570v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14570v1#S5.SS1 — 5.1 Technical Strengths and limitations | Exact v1 links https://github.com/Agentic-AI-Risk-Mitigation/ifg-monitor, https://github.com/UKGovernmentBEIS/control-arena, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14570 | complete |
| SF-2026-ARXIV-2607-14573 | RP-b6d6f6a64ce37954 | standard | arXiv:2607.14573v1 | SRC-ARXIV@arXiv:2607.14573v1 | https://arxiv.org/html/2607.14573v1#S4.SS4 — 4.4 RQ3: Evaluation-Method Diagnostics; https://arxiv.org/html/2607.14573v1#S4.SS2 — 4.2 RQ1: Model Capability | https://arxiv.org/html/2607.14573v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.14573v1#S3.SS1 — 3.1 Benchmark Composition | https://arxiv.org/html/2607.14573v1#S5 — 5 Conclusion | Exact v1 links https://github.com/inclusionAI/PIBench, https://github.com/aelassas/bookcars, https://www.endorlabs.com/research/ai-code-security-benchmark; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14573 | complete |
| SF-2026-ARXIV-2607-14611 | RP-ba0f6f1e26b2ec48 | deep | arXiv:2607.14611v1 | SRC-ARXIV@arXiv:2607.14611v1 | https://arxiv.org/html/2607.14611v1#S3 — 3. Methods; https://arxiv.org/html/2607.14611v1#S3.SS1 — 3.1. Threat Model and Scope | https://arxiv.org/html/2607.14611v1#S2.SS2 — 2.2. Benchmarks for Agent Security; https://arxiv.org/html/2607.14611v1#S3.SS3 — 3.3. Evaluation Protocol | https://arxiv.org/html/2607.14611v1#S3.SS1 — 3.1. Threat Model and Scope; https://arxiv.org/html/2607.14611v1#S5 — 5. Discussion | Exact v1 links https://docs.anthropic.com/en/docs/claude-code/memory, https://developers.openai.com/codex/guides/agents-md, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14611 | complete |
| SF-2026-ARXIV-2607-14618 | RP-cc671464a863a8c0 | deep | arXiv:2607.14618v1 | SRC-ARXIV@arXiv:2607.14618v1 | https://arxiv.org/html/2607.14618v1#S3 — 3. Poly-Precision Quantization Method; https://arxiv.org/html/2607.14618v1#S4 — 4. Model Compiler Architecture | https://arxiv.org/html/2607.14618v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.14618v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.14618v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14618 | complete |
| SF-2026-ARXIV-2607-14635 | RP-f34d28a616618552 | standard | arXiv:2607.14635v1 | SRC-ARXIV@arXiv:2607.14635v1 | https://arxiv.org/html/2607.14635v1#S3 — III Methodology; https://arxiv.org/html/2607.14635v1#A1.SS1 — A-A Training Pipeline and Model Comparison | https://arxiv.org/html/2607.14635v1#A2 — Appendix B Experiment Details; https://arxiv.org/html/2607.14635v1#A2.SS1 — B-A Probe Scenes and Evaluation Rules for Action Generation | https://arxiv.org/html/2607.14635v1#S6 — VI Discussion; https://arxiv.org/html/2607.14635v1#S7 — VII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14635 | complete |
| SF-2026-ARXIV-2607-14642 | RP-e58f050e6ea30c34 | standard | arXiv:2607.14642v1 | SRC-ARXIV@arXiv:2607.14642v1 | https://arxiv.org/html/2607.14642v1#A4.SS3 — D.3 Implementation Details | https://arxiv.org/html/2607.14642v1#A4.SS2 — D.2 Reliability Analysis of Benchmark; https://arxiv.org/html/2607.14642v1#A8.SS3 — H.3 Prompts for Benchmark Evaluation | https://arxiv.org/html/2607.14642v1#A3 — Appendix C Limitation and Future Work; https://arxiv.org/html/2607.14642v1#A7.SS2 — G.2 Case Study of Workflow Failure | Exact v1 links https://github.com/modelcontextprotocol/specification, https://github.com/, https://github.com/punkpeye/awesome-mcp-servers; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14642 | complete |
| SF-2026-ARXIV-2607-14647 | RP-09010f415dbd3b78 | deep | arXiv:2607.14647v1 | SRC-ARXIV@arXiv:2607.14647v1 | https://arxiv.org/html/2607.14647v1#A3 — Appendix C System Implementation; https://arxiv.org/html/2607.14647v1#S3 — 3 Method | https://arxiv.org/html/2607.14647v1#A1 — Appendix A Algorithm and Analysis; https://arxiv.org/html/2607.14647v1#A4 — Appendix D Experimental Details | https://arxiv.org/html/2607.14647v1#S6 — 6 Conclusion and Limitations | Exact v1 links https://github.com/vllm-project/vllm/pull/47131, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://huggingface.co/tencent/Hy3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14647 | complete |
| SF-2026-ARXIV-2607-14651 | RP-b1c2af4fa3a458e4 | deep | arXiv:2607.14651v1 | SRC-ARXIV@arXiv:2607.14651v1 | https://arxiv.org/html/2607.14651v1#A2 — Appendix B Experimental Design; https://arxiv.org/html/2607.14651v1#A2.SS7 — B.7 MID implementation details | https://arxiv.org/html/2607.14651v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.14651v1#A1.SS1 — A.1 Benchmark Construction | https://arxiv.org/html/2607.14651v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.14651v1#S3 — 3 Threat Model and Taxonomy | Exact v1 links https://huggingface.co/meta-llama/Prompt-Guard-86M, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14651 | complete |
| SF-2026-ARXIV-2607-14695 | RP-00dbd994722c22ee | deep | arXiv:2607.14695v1 | SRC-ARXIV@arXiv:2607.14695v1 | https://arxiv.org/html/2607.14695v1#S2.SS3 — 2.3 Design Goals; https://arxiv.org/html/2607.14695v1#S3 — 3 Method: Streaming VLA Inference | https://arxiv.org/html/2607.14695v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.14695v1#A4 — Appendix D Additional Experimental Details | https://arxiv.org/html/2607.14695v1#S5 — 5 Conclusion | Exact v1 links https://github.com/9yc/Reflex, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14695 | complete |
| SF-2026-ARXIV-2607-14698 | RP-ec03ccd13425c841 | standard | arXiv:2607.14698v1 | SRC-ARXIV@arXiv:2607.14698v1 | https://arxiv.org/html/2607.14698v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14698v1#S3.SS2 — 3.2 FLARE Framework: Optimized Physical Spotlight Attack | https://arxiv.org/html/2607.14698v1#S4 — 4 Simulator Experiments: Exposing Vulnerability against Spotlight Attack; https://arxiv.org/html/2607.14698v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.14698v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.14698v1#S6 — 6 Limitations | Exact v1 links https://github.com/TheRobotStudio/SO-ARM100, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14698 | complete |
| SF-2026-ARXIV-2607-14739 | RP-4ef6e0be16c57185 | deep | arXiv:2607.14739v1 | SRC-ARXIV@arXiv:2607.14739v1 | https://arxiv.org/html/2607.14739v1#A1.SS2 — A.2 Attention Mask Design; https://arxiv.org/html/2607.14739v1#S3 — 3 Method | https://arxiv.org/html/2607.14739v1#A2 — Appendix B Additional Experimental Analysis; https://arxiv.org/html/2607.14739v1#A2.SS3 — B.3 RoboCasa GR-1 Tabletop Ablation | https://arxiv.org/html/2607.14739v1#S3.SS3 — 3.3 Future Feature Prediction; https://arxiv.org/html/2607.14739v1#S3.SS4 — 3.4 Future-Conditioned Point Tracking | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14739 | complete |
| SF-2026-ARXIV-2607-14754 | RP-2e7b45ceb69f6dde | standard | arXiv:2607.14754v1 | SRC-ARXIV@arXiv:2607.14754v1 | https://arxiv.org/html/2607.14754v1#S3 — III Methodology; https://arxiv.org/html/2607.14754v1#S3.SS2 — III-B System Overview | https://arxiv.org/html/2607.14754v1#S3.SS4 — III-D Response Analysis; https://arxiv.org/html/2607.14754v1#S4 — IV Benchmark Construction | https://arxiv.org/html/2607.14754v1#S2.SS3 — II-C Threat Model; https://arxiv.org/html/2607.14754v1#S6 — VI Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14754 | complete |
| SF-2026-ARXIV-2607-14777 | RP-9b7514977ce8883e | deep | arXiv:2607.14777v1 | SRC-ARXIV@arXiv:2607.14777v1 | https://arxiv.org/html/2607.14777v1#S3 — 3 Method; https://arxiv.org/html/2607.14777v1#A2.SS3 — B.3 Algorithm and Extracted Skill Examples | https://arxiv.org/html/2607.14777v1#S4.SS6 — 4.6 Ablation Studies and Analysis; https://arxiv.org/html/2607.14777v1#A1 — Appendix A Theoretical Analysis | https://arxiv.org/html/2607.14777v1#A5 — Appendix E Additional Discussion; https://arxiv.org/html/2607.14777v1#S5 — 5 Conclusion | Exact v1 links https://github.com/jinyangwu/SEED, https://huggingface.co/Jinyang23/Seed-AlfWorld-3B, https://github.com/mpSchrader/gym-sokoban; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14777 | complete |
| SF-2026-ARXIV-2607-14811 | RP-ec3f7c0331417dc3 | standard | arXiv:2607.14811v1 | SRC-ARXIV@arXiv:2607.14811v1 | https://arxiv.org/html/2607.14811v1#A0.SS4 — -D Implementation Details of Baseline Approaches; https://arxiv.org/html/2607.14811v1#A0.SS5 — -E Detailed Attack Design | https://arxiv.org/html/2607.14811v1#A0.SS1 — -A Missing experimental results; https://arxiv.org/html/2607.14811v1#A0.SS6 — -F Details of Evaluation Metrics | https://arxiv.org/html/2607.14811v1#A0.SS10 — -J Discussions when Adapting PA-HDP to Domain-Specific Applications; https://arxiv.org/html/2607.14811v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14811 | complete |
| SF-2026-ARXIV-2607-14817 | RP-408e4cc412c288e8 | standard | arXiv:2607.14817v1 | SRC-ARXIV@arXiv:2607.14817v1 | https://arxiv.org/html/2607.14817v1#A3.SS1 — C.1 Datasets and Architectures; https://arxiv.org/html/2607.14817v1#A3.SS2 — C.2 Method-Specific Training Regimes | https://arxiv.org/html/2607.14817v1#A4 — Appendix D Detailed Results; https://arxiv.org/html/2607.14817v1#S3.SS1 — 3.1 The evaluation disconnect: Bayesian vs. frequentist | https://arxiv.org/html/2607.14817v1#S7 — 7 Conclusion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14817 | complete |
| SF-2026-ARXIV-2607-14852 | RP-874b54372d8d204e | deep | arXiv:2607.14852v1 | SRC-ARXIV@arXiv:2607.14852v1 | https://arxiv.org/html/2607.14852v1#S4 — 4 The Proposed Model | https://arxiv.org/html/2607.14852v1#S5 — 5 Experiments; https://arxiv.org/html/2607.14852v1#S5.SS1 — 5.1 Main Comparison and Process-Level Analysis | https://arxiv.org/html/2607.14852v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.14852v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14852 | complete |
| SF-2026-ARXIV-2607-14890 | RP-99e2bc8f83f7fa3d | deep | arXiv:2607.14890v1 | SRC-ARXIV@arXiv:2607.14890v1 | https://arxiv.org/html/2607.14890v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14890v1#S2 — 2 Background and Problem | https://arxiv.org/html/2607.14890v1#S5.SS2 — 5.2 Reflection-loop ablation (powered: 9,240 cells) | https://arxiv.org/html/2607.14890v1#S11 — 11 Threats to Validity; https://arxiv.org/html/2607.14890v1#S12 — 12 Future Work | Exact v1 links https://github.com/Proof-or-Stop, https://github.com/microsoft/agent-framework, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14890 | complete |
| SF-2026-ARXIV-2607-14896 | RP-52c8d4cdea647d02 | standard | arXiv:2607.14896v1 | SRC-ARXIV@arXiv:2607.14896v1 | https://arxiv.org/html/2607.14896v1#S2.SS1 — 2.1 Generative Design & Structural LLM Systems; https://arxiv.org/html/2607.14896v1#S3 — 3 StructureClaw System | https://arxiv.org/html/2607.14896v1#A2 — Appendix B Benchmark Construction and Assertions; https://arxiv.org/html/2607.14896v1#A3 — Appendix C Evaluation Protocol and Metric Definitions | https://arxiv.org/html/2607.14896v1#S6 — 6 Discussion; https://arxiv.org/html/2607.14896v1#S7 — 7 Conclusion | Exact v1 links https://github.com/structureclaw/structureclaw, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14896 | complete |
| SF-2026-ARXIV-2607-14903 | RP-648c2ef064920364 | standard | arXiv:2607.14903v1 | SRC-ARXIV@arXiv:2607.14903v1 | https://arxiv.org/html/2607.14903v1#S4 — IV System Design; https://arxiv.org/html/2607.14903v1#S3 — III Motivation and Design Challenges | https://arxiv.org/html/2607.14903v1#S5 — V Experimental Evaluation | https://arxiv.org/html/2607.14903v1#S2.SS2 — II-B Rehosting Failure Modes; https://arxiv.org/html/2607.14903v1#S5.SS5 — V-E Threats to Validity and Mitigations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14903 | complete |
| SF-2026-ARXIV-2607-14908 | RP-6380783cc4fe2d14 | deep | arXiv:2607.14908v1 | SRC-ARXIV@arXiv:2607.14908v1 | https://arxiv.org/html/2607.14908v1#S4.SS3 — 4.3. CODA Architecture and NMP Subsystem; https://arxiv.org/html/2607.14908v1#S4 — 4. CODA Design | https://arxiv.org/html/2607.14908v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.14908v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.14908v1#S7 — 7. Discussion and Future Work; https://arxiv.org/html/2607.14908v1#S8 — 8. Conclusion | Exact v1 links https://github.com/NUS-HPC-AI-Lab/VideoSys, https://github.com/vipshop/cache-dit.git, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14908 | complete |
| SF-2026-ARXIV-2607-14952 | RP-34296b0934a4e0be | deep | arXiv:2607.14952v1 | SRC-ARXIV@arXiv:2607.14952v1 | https://arxiv.org/html/2607.14952v1#S10.SS9 — 10.9 GRPO Systems; https://arxiv.org/html/2607.14952v1#S3 — 3 Architecture Anatomy and Bottleneck Sources | https://arxiv.org/html/2607.14952v1#S9.SS6 — 9.6 Group Scaling Is a Scheduling Result | https://arxiv.org/html/2607.14952v1#S11 — 11 Conclusion; https://arxiv.org/html/2607.14952v1#S12 — 12 Limitations and Validation Roadmap | Exact v1 links https://github.com/MindLab-Research/longstraw, https://huggingface.co/Qwen/Qwen3.6-27B/blob/6a9e13bd6fc8f0983b9b99948120bc37f49c13e9/config.json, https://huggingface.co/zai-org/GLM-5.2/blob/b4734de4facf877f85769a911abafc5283eab3d9/config.json; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14952 | complete |
| SF-2026-ARXIV-2607-14989 | RP-e9556400f33b3f98 | standard | arXiv:2607.14989v1 | SRC-ARXIV@arXiv:2607.14989v1 | https://arxiv.org/html/2607.14989v1#S10 — 10 Persona Design; https://arxiv.org/html/2607.14989v1#S6.SS1 — 6.1 Judge Model Robustness Results | https://arxiv.org/html/2607.14989v1#S3.SS4 — 3.4 Evaluation; https://arxiv.org/html/2607.14989v1#S4 — 4 Experiments | https://arxiv.org/html/2607.14989v1#S4.SS3 — 4.3 Discussion; https://arxiv.org/html/2607.14989v1#S5 — 5 Conclusion | Exact v1 links https://github.com/scuuy/OmniaBench, https://github.com/SKYLENAGE-AI/QwenClawBench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14989 | complete |
| SF-2026-ARXIV-2607-15065 | RP-19ee19aa861d16e4 | standard | arXiv:2607.15065v1 | SRC-ARXIV@arXiv:2607.15065v1 | https://arxiv.org/html/2607.15065v1#S3.SS4 — 3.4 Action-Conditioned Architecture; https://arxiv.org/html/2607.15065v1#A4 — Appendix D Implementation Details | https://arxiv.org/html/2607.15065v1#A1 — Appendix A Additional Qualitative Results; https://arxiv.org/html/2607.15065v1#A2 — Appendix B Additional Quantitative Results | https://arxiv.org/html/2607.15065v1#S5 — 5 Discussion | Exact v1 links https://github.com/Susie-Lu/driftworld, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15065 | complete |
| SF-2026-ARXIV-2607-15092 | RP-30aa095f49f8b4e1 | standard | arXiv:2607.15092v1 | SRC-ARXIV@arXiv:2607.15092v1 | https://arxiv.org/html/2607.15092v1#S3 — 3 Methodology; https://arxiv.org/html/2607.15092v1#S3.SS1 — 3.1 Framework overview | https://arxiv.org/html/2607.15092v1#S2.SS1 — 2.1 Rubric-based evaluation; https://arxiv.org/html/2607.15092v1#S4 — 4 Experiments | https://arxiv.org/html/2607.15092v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15092 | complete |
| SF-2026-ARXIV-2607-15115 | RP-22da2cf01cb442b5 | standard | arXiv:2607.15115v1 | SRC-ARXIV@arXiv:2607.15115v1 | https://arxiv.org/html/2607.15115v1#A1 — Appendix A System Architecture and Data Collection; https://arxiv.org/html/2607.15115v1#S3.SS1 — 3.1. Model Prediction Experiments | https://arxiv.org/html/2607.15115v1#S5.SS2 — 5.2. RQ1: Evaluation Results and Analysis; https://arxiv.org/html/2607.15115v1#A1.SS3 — A.3. Telemetry Dataset (for Predictability Analysis) | https://arxiv.org/html/2607.15115v1#S3.SS3 — 3.3. The Power of Historical Failure Patterns; https://arxiv.org/html/2607.15115v1#S7 — 7. Discussion | Exact v1 links https://github.com/geotle77/kdd26-artifact, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15115 | complete |
| SF-2026-ARXIV-2607-15143 | RP-248cace8555c02af | deep | arXiv:2607.15143v1 | SRC-ARXIV@arXiv:2607.15143v1 | https://arxiv.org/html/2607.15143v1#A5 — Appendix E System Prompt and Review Prompts; https://arxiv.org/html/2607.15143v1#A9 — Appendix I Pre-Install Hook Architecture | https://arxiv.org/html/2607.15143v1#A3 — Appendix C Experimental Setup; https://arxiv.org/html/2607.15143v1#S4 — 4 Evaluation Methodology | https://arxiv.org/html/2607.15143v1#S10 — 10 Limitations and Future Directions; https://arxiv.org/html/2607.15143v1#S11 — 11 Conclusion | Exact v1 links https://github.com/cardwizard/Sentinel/blob/main/evaluations/GITHUB_SEARCH_QUERIES.md, https://github.com/features/copilot, https://claude.ai/code; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15143 | complete |
| SF-2026-ARXIV-2607-15161 | RP-90a1973e62a4e6f4 | deep | arXiv:2607.15161v1 | SRC-ARXIV@arXiv:2607.15161v1 | https://arxiv.org/html/2607.15161v1#S2 — 2 Method | https://arxiv.org/html/2607.15161v1#S3 — 3 Experiment; https://arxiv.org/html/2607.15161v1#S3.SS1 — 3.1 Experiment settings | https://arxiv.org/html/2607.15161v1#S5 — 5 Conclusion | Exact v1 links https://github.com/naver-ai/opd2, https://huggingface.co/datasets/nvidia/OpenScienceReasoning-2, https://github.com/huggingface/trl; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15161 | complete |
| SF-2026-ARXIV-2607-15190 | RP-35ba274a0f6a5a9a | standard | arXiv:2607.15190v1 | SRC-ARXIV@arXiv:2607.15190v1 | https://arxiv.org/html/2607.15190v1#S4 — 4 Simulation design; https://arxiv.org/html/2607.15190v1#S5.SS2 — 5.2 How do different IRT estimators recover model capabilities and rankings? | https://arxiv.org/html/2607.15190v1#A4 — Appendix D Detailed results for parameter recovery; https://arxiv.org/html/2607.15190v1#S3 — 3 Item response theory for AI evaluation | https://arxiv.org/html/2607.15190v1#S7 — 7 Limitations and Conclusion | Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15190 | complete |
| SF-2026-ARXIV-2607-15193 | RP-76c430a9c29320dc | standard | arXiv:2607.15193v1 | SRC-ARXIV@arXiv:2607.15193v1 | https://arxiv.org/html/2607.15193v1#A4.SS2 — D.2. Executor System Prompt Design; https://arxiv.org/html/2607.15193v1#A3 — Appendix C System-Driven IR Details | https://arxiv.org/html/2607.15193v1#S5.SS1 — 5.1. Benchmark Failure-Case Repair Analysis; https://arxiv.org/html/2607.15193v1#A2 — Appendix B Formative Study User Experience Analysis | https://arxiv.org/html/2607.15193v1#A5.SS1 — E.1. Failure Analysis; https://arxiv.org/html/2607.15193v1#S5.SS1 — 5.1. Benchmark Failure-Case Repair Analysis | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15193 | complete |
| SF-2026-ARXIV-2607-15205 | RP-292a3f8ab265d469 | standard | arXiv:2607.15205v1 | SRC-ARXIV@arXiv:2607.15205v1 | https://arxiv.org/html/2607.15205v1#S5.SS1 — 5.1 RQ1: How Well Do Current Systems Localize Multimodal Repository Issues?; https://arxiv.org/html/2607.15205v1#S5.SS2 — 5.2 RQ2: Is Visual Evidence Useful, and Do Systems Use It Reliably? | https://arxiv.org/html/2607.15205v1#A2.SS4 — B.4 Cross-benchmark Localization Results; https://arxiv.org/html/2607.15205v1#S5 — 5 Results and Analysis | https://arxiv.org/html/2607.15205v1#S6 — 6 Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.15205v1#S7 — 7 Conclusion | Exact v1 links https://github.com/Jasaxion/MM-IssueLoc-Bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15205 | complete |
| SF-2026-ARXIV-2607-15207 | RP-e9b8c96a6259db50 | deep | arXiv:2607.15207v1 | SRC-ARXIV@arXiv:2607.15207v1 | https://arxiv.org/html/2607.15207v1#S2.SS2 — 2.2 Attacks against Embodied AI Systems; https://arxiv.org/html/2607.15207v1#S4.SS1 — 4.1 Design Motivation | https://arxiv.org/html/2607.15207v1#A1 — Appendix A Details of Experiment Setup; https://arxiv.org/html/2607.15207v1#A1.SS1 — A.1 Full and Subset Evaluation Protocols | https://arxiv.org/html/2607.15207v1#S3 — 3 Threat Model; https://arxiv.org/html/2607.15207v1#S5.SS2 — 5.2 BadWAM Reliably Induces Task Failures | Exact v1 links https://github.com/LiQiiiii/BadWAM, https://huggingface.co/collections/LIQIIIII/badwam, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15207 | complete |
| SF-2026-ARXIV-2607-15253 | RP-27603c42dd0fe2d2 | standard | arXiv:2607.15253v1 | SRC-ARXIV@arXiv:2607.15253v1 | https://arxiv.org/html/2607.15253v1#A1.SS1 — A.1. Agent system prompt; https://arxiv.org/html/2607.15253v1#S2 — 2. Methodology | https://arxiv.org/html/2607.15253v1#S3 — 3. Results and Analysis; https://arxiv.org/html/2607.15253v1#S2.SS3 — 2.3. Experimental setup | https://arxiv.org/html/2607.15253v1#S3.SS6 — 3.6. Threats to validity; https://arxiv.org/html/2607.15253v1#S4 — 4. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15253 | complete |
| SF-2026-ARXIV-2607-15257 | RP-66565aebe41519b3 | deep | arXiv:2607.15257v1 | SRC-ARXIV@arXiv:2607.15257v1 | https://arxiv.org/html/2607.15257v1#S6.SS2 — 6.2 Multi-Agent Orchestration Systems; https://arxiv.org/html/2607.15257v1#A3 — Appendix C Implementation Reference | https://arxiv.org/html/2607.15257v1#S5 — 5 Ablations & Analysis; https://arxiv.org/html/2607.15257v1#S4 — 4 Experiments | https://arxiv.org/html/2607.15257v1#S7 — 7 Conclusion | Exact v1 links https://github.com/antins-labs/SearchOS, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15257 | complete |
| SF-2026-ARXIV-2607-15263 | RP-e47175eb4a1c20db | deep | arXiv:2607.15263v1 | SRC-ARXIV@arXiv:2607.15263v1 | https://arxiv.org/html/2607.15263v1#A2 — Appendix B Uncertainty Method; https://arxiv.org/html/2607.15263v1#S3 — 3 Evaluation Design | https://arxiv.org/html/2607.15263v1#S4 — 4 Evaluation Results; https://arxiv.org/html/2607.15263v1#A1 — Appendix A Evaluation Run Dates | https://arxiv.org/html/2607.15263v1#S7 — 7 Limitations; https://arxiv.org/html/2607.15263v1#S9 — 9 Conclusion | Exact v1 links https://github.com/splunk/botsv1, https://github.com/splunk/botsv2, https://github.com/splunk/botsv3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-15263 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-14103:start -->
### Latent Communication Between Language Model Agents: Channels, Alignment, and the Limits of Text

<!-- claim:SF-2026-ARXIV-2607-14103:start -->Multi-agent systems (MAS) are utilized in many contexts and many professions. Those MAS rely on inter-agent communication, usually implemented by clear-text message passing. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14103:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent systems (MAS) are utilized in many contexts and many professions.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Multi-agent systems (MAS) are utilized in many contexts and many professions.

**证据证明什么。** We find for Procrustes alignment a 92% top-1 retrieval between Llama and Mistral.

**证据没有证明什么。** However, our augmentation results (§ 3.6 ) suggest that even perfect alignment would not cause the latent channel to exceed text on concept-identification tasks: the information text loses is surface form, not task-relevant semantics. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14103v1#S2 — 2. Methods; https://arxiv.org/html/2607.14103v1#S2.SS6 — 2.6. Cross-Architecture Alignment (C3)。Evaluation：https://arxiv.org/html/2607.14103v1#S2.SS5 — 2.5. SAE Feature Survival Analysis (C2); https://arxiv.org/html/2607.14103v1#S2.SS7 — 2.7. Task-Level Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.14103v1#S4 — 4. Discussion; https://arxiv.org/html/2607.14103v1#S4.SS4 — 4.4. Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, our augmentation results (§ 3.6 ) suggest that even perfect alignment would not cause the latent channel to exceed text on concept-identification tasks: the information text loses is surface form, not task-relevant semantics.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14103:end -->

<!-- review:SF-2026-ARXIV-2607-14107:start -->
### Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs

<!-- claim:SF-2026-ARXIV-2607-14107:start -->The inference efficiency of diffusion large language models (dLLMs) is constrained by two challenges: bidirectional attention precludes efficient KV-cache reuse, while increasing decoding parallelism with static confidence thresholds can compromise generation quality. We observe that both challenges arise from a shared phenomenon: as tokens are decoded, their contextual integration through bidirectional attention causes token representations to drift (evolve) across decoding steps. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14107:end -->

**为什么进入候选分母。** 摘要首要问题为“The inference efficiency of diffusion large language models (dLLMs) is constrained by two challenges: bidirectional attention precludes efficient KV-cache reuse, while increasing decoding parallelism with static confidence thresholds can compromise generation quality.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** This insight motivates Polestar, a training-free inference framework that uses token representation drift as a unified signal to jointly address both challenges.

**证据证明什么。** Across mathematics and coding benchmarks on several dLLM families, Polestar sets a new state of the art on the accuracy-throughput Pareto frontier, achieving up to 10.73% accuracy improvement, up to 3.7x higher throughput, and high decoding parallelism of 3.67 tokens per forward pass over existing baselines.

**证据没有证明什么。** For (c,d) star marks the default Polestar setting, and text annotations indicate TPF. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14107v1#S4 — 4 Polestar Methodology; https://arxiv.org/html/2607.14107v1#S4.SS3 — 4.3 Polestar System Optimization。Evaluation：https://arxiv.org/html/2607.14107v1#S5 — 5 Experimental Evaluations; https://arxiv.org/html/2607.14107v1#A4 — Appendix D Additional Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.14107v1#S5.SS3 — 5.3 Discussions and Ablations; https://arxiv.org/html/2607.14107v1#S6 — 6 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：For (c,d) star marks the default Polestar setting, and text annotations indicate TPF.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14107:end -->

<!-- review:SF-2026-ARXIV-2607-14108:start -->
### Eta Given Delta: Defining LLM Tool Efficiency With Marginal Tool Utility

<!-- claim:SF-2026-ARXIV-2607-14108:start -->This paper introduces tool efficiency, a new quantitative metric to evaluate the rate of useful tool calls in an LLM agent trajectory. To ensure that tool efficiency is well-defined, we also introduce marginal tool utility, a new quantitative metric defined per tool call indicating whether a tool is useful or whether it can be safely removed from the tool suite without affecting accuracy while increasing tool efficiency; in this paper, we determine the sign of marginal tool utility for each tool call in a trajectory using LLM-as-a-Judge. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14108:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper introduces tool efficiency, a new quantitative metric to evaluate the rate of useful tool calls in an LLM agent trajectory.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** While much prior work has been done to develop techniques that improve tool use by LLMs and design evaluation methods measuring efficiency indirectly using accuracy as a proxy, our work is centered on measuring efficiency directly via the quantitative metric proposed in this paper in post hoc trajectory analyses.

**证据证明什么。** While much prior work has been done to develop techniques that improve tool use by LLMs and design evaluation methods measuring efficiency indirectly using accuracy as a proxy, our work is centered on measuring efficiency directly via the quantitative metric proposed in this paper in post hoc trajectory analyses.

**证据没有证明什么。** Most notably, we only ran tool ablations for read-only tools (the three MCPs are all read-only). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14108v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.14108v1#S3.SS4 — 3.4 Experimental Setup; https://arxiv.org/html/2607.14108v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.14108v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14108v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/antl3x/ToolRAG, https://openai.com/index/introducing-gpt-5-3-codex/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Most notably, we only ran tool ablations for read-only tools (the three MCPs are all read-only).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14108:end -->

<!-- review:SF-2026-ARXIV-2607-14109:start -->
### Simplicity Paradox: Debunking myths about prompting and datasets for LLM evaluation

<!-- claim:SF-2026-ARXIV-2607-14109:start -->Probing the capabilities of Large Language Models (LLMs) and building robust solutions for Multiple-Choice Question Answering (MCQA) remain central challenges in natural language understanding. Furthermore, the rapid proliferation of LLMs has created the implicit assumption that more sophisticated prompting techniques yield better performance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14109:end -->

**为什么进入候选分母。** 摘要首要问题为“Probing the capabilities of Large Language Models (LLMs) and building robust solutions for Multiple-Choice Question Answering (MCQA) remain central challenges in natural language understanding.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Furthermore, the rapid proliferation of LLMs has created the implicit assumption that more sophisticated prompting techniques yield better performance.

**证据证明什么。** These results suggest that the LLM evaluation community may be overcomplicating prompt engineering and that substantial performance gaps remain across diverse benchmarks, offering opportunities for genuine model improvements rather than prompt optimization.

**证据没有证明什么。** Our prompt template follows the public release of Yasunaga et al. [ 36 ] ; we did not tune exemplar count or template wording per model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14109v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14109v1#A2 — Appendix B Model configurations。Evaluation：https://arxiv.org/html/2607.14109v1#A1 — Appendix A Self-Analogical failure-mode analysis; https://arxiv.org/html/2607.14109v1#S3.SS5 — 3.5 Evaluation metrics。Limitations / counterevidence：https://arxiv.org/html/2607.14109v1#A1 — Appendix A Self-Analogical failure-mode analysis; https://arxiv.org/html/2607.14109v1#A6 — Appendix F Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/bigbio/med_qa, https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro, https://huggingface.co/datasets/update0909/cure-bench-reasoning-traces; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our prompt template follows the public release of Yasunaga et al. [ 36 ] ; we did not tune exemplar count or template wording per model.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14109:end -->

<!-- review:SF-2026-ARXIV-2607-14145:start -->
### ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability

<!-- claim:SF-2026-ARXIV-2607-14145:start -->Tool-augmented large language model agents excel at long-horizon tasks, yet they are typically post-trained on fixed toolsets. When tasks demand new tools, these agents struggle to incorporate them effectively, and retraining from scratch is often impractical. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14145:end -->

**为什么进入候选分母。** 摘要首要问题为“Tool-augmented large language model agents excel at long-horizon tasks, yet they are typically post-trained on fixed toolsets.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To scale this insight, we propose ToolAnchor, a framework that uses teacher models to hypothesize these counterfactual contexts, verifies them via student rollouts, and internalizes the successful interventions through agentic post-training.

**证据证明什么。** We demonstrate that injecting counterfactual anchor contexts at critical decision points can break this inertia, recovering failed trajectories by eliciting suppressed agent capabilities.

**证据没有证明什么。** In this work, the experiments rely on a limited set of teacher models and verified anchor contexts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14145v1#A2.SS1 — B.1 System prompt for deep research agent; https://arxiv.org/html/2607.14145v1#A2.SS2 — B.2 System Prompt for teacher model counterfactual anchor round hypothesis。Evaluation：https://arxiv.org/html/2607.14145v1#A2.SS4 — B.4 Prompt for LLM-As-Judge evaluation; https://arxiv.org/html/2607.14145v1#A3.SS3 — C.3 Statistical analysis of counterfactual anchor rounds。Limitations / counterevidence：https://arxiv.org/html/2607.14145v1#S6 — 6 Conclusion and limitation; https://arxiv.org/html/2607.14145v1#S5.SS4 — 5.4 Further analysis and discussions。

**Artifact boundary。** Exact v1 links https://github.com/THUDM/slime, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：In this work, the experiments rely on a limited set of teacher models and verified anchor contexts.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14145:end -->

<!-- review:SF-2026-ARXIV-2607-14155:start -->
### Beyond Object Validation: Relational Conformance in Multi-Artifact Agent Releases

<!-- claim:SF-2026-ARXIV-2607-14155:start -->Agent systems validate inputs, tool calls, and generated objects. The final package often escapes the same scrutiny. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14155:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent systems validate inputs, tool calls, and generated objects.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Agent systems validate inputs, tool calls, and generated objects.

**证据证明什么。** The paper establishes the failure class and shows that several mechanisms are practical.

**证据没有证明什么。** VI-K Threat boundary SIP-RC is an information, decision, and artifact-release boundary. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14155v1#S4 — IV Study Method; https://arxiv.org/html/2607.14155v1#S4.SS1 — IV-A Design and case roles。Evaluation：https://arxiv.org/html/2607.14155v1#S4.SS4 — IV-D Analysis; https://arxiv.org/html/2607.14155v1#S7 — VII Implementation Status and Evaluation Plan。Limitations / counterevidence：https://arxiv.org/html/2607.14155v1#S10 — X Conclusion; https://arxiv.org/html/2607.14155v1#S6.SS11 — VI-K Threat boundary。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：VI-K Threat boundary SIP-RC is an information, decision, and artifact-release boundary.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-PRODUCTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14155:end -->

<!-- review:SF-2026-ARXIV-2607-14157:start -->
### Certified Domain Consistency for Multi-Domain Retrieval: Label-Free Per-Domain Contamination Control with Conformal Risk Guarantees

<!-- claim:SF-2026-ARXIV-2607-14157:start -->Retrieval over corpora that mix several domains often returns relevant but wrong-domain evidence that ranking metrics miss and that conformal risk control bounds only marginally, under-covering the worst domains. This work introduces C3R, a drop-in control layer that, from an inferred domain posterior and no query-time label, certifies a per-domain contamination budget where feasible and otherwise abstains rather than silently violating; on the hardest domains it guarantees a reduction, not a tight bound. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14157:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval over corpora that mix several domains often returns relevant but wrong-domain evidence that ranking metrics miss and that conformal risk control bounds only marginally, under-covering the worst domains.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The method replicates across open testbeds including an independent one from public federal regulations, and an LLM-judged downstream probe indicates wrong-authority grounding rises with contamination and falls under control.

**证据证明什么。** The layer is frozen-stack and reranker-agnostic.

**证据没有证明什么。** Conclusion We presented C3R, a drop-in layer that certifies a per-domain contamination budget for multi-domain retrieval using only an inferred domain posterior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14157v1#S1 — 1. Introduction; https://arxiv.org/html/2607.14157v1#S1.SS0.SSS0.Px1 — Contributions.。Evaluation：https://arxiv.org/html/2607.14157v1#S1.SS0.SSS0.Px2 — Results preview.; https://arxiv.org/html/2607.14157v1#S3 — 3. Problem Setup and Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.14157v1#S2.SS0.SSS0.Px3 — Retrieval-augmented generation: reliability and threats.; https://arxiv.org/html/2607.14157v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Conclusion We presented C3R, a drop-in layer that certifies a per-domain contamination budget for multi-domain retrieval using only an inferred domain posterior.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14157:end -->

<!-- review:SF-2026-ARXIV-2607-14159:start -->
### MemoHarness: Agent Harnesses That Learn from Experience

<!-- claim:SF-2026-ARXIV-2607-14159:start -->An agent harness is the external control layer that turns a base LLM into an executable agent by managing context, tools, orchestration, memory, decoding, and output handling. While harness design strongly affects agent behavior, most automatic improvement methods optimize narrower artifacts such as prompts, pipelines, or workflows, and deployed agents usually reuse a single global harness for all cases. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14159:end -->

**为什么进入候选分母。** 摘要首要问题为“An agent harness is the external control layer that turns a base LLM into an executable agent by managing context, tools, orchestration, memory, decoding, and output handling.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce MemoHarness, an adaptive harness optimization framework that learns from its own executions.

**证据证明什么。** In our evaluation across shell-agent, code-generation, and analytical-reasoning benchmarks, MemoHarness improves over the fixed harnesses we compare against and shows selective transfer to unseen suites and base models.

**证据没有证明什么。** Second, not every baseline is a pure scaffold transplant with the same underlying model and runtime surface. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14159v1#S2 — 2 Method; https://arxiv.org/html/2607.14159v1#A2 — Appendix B Implementation Details。Evaluation：https://arxiv.org/html/2607.14159v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.14159v1#S3 — 3 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.14159v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.14159v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/HowieHwong/MemoHarness, https://github.com/anthropics/claude-code, https://github.com/openai/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Second, not every baseline is a pure scaffold transplant with the same underlying model and runtime surface.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14159:end -->

<!-- review:SF-2026-ARXIV-2607-14166:start -->
### Stop Means Stop: Measuring and Repairing the Enforcement Gap in Agent-Framework Control Primitives

<!-- claim:SF-2026-ARXIV-2607-14166:start -->Production LLM-agent frameworks ship control primitives -- human-in-the-loop approval gates, run cancellation, and execution timeouts -- whose names and documentation imply barrier semantics: while a run is paused, cancelled, or timed out, no gated side effect executes. This contract holds on none of six widely used open-source frameworks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14166:end -->

**为什么进入候选分母。** 摘要首要问题为“Production LLM-agent frameworks ship control primitives -- human-in-the-loop approval gates, run cancellation, and execution timeouts -- whose names and documentation imply barrier semantics: while a run is paused, cancelled, or timed out, no gated side effect executes.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This contract holds on none of six widely used open-source frameworks.

**证据证明什么。** Under that contract SOUNDGATE blocks every measured violation on all six frameworks while releasing legitimate effects: gated tau-bench episodes complete with zero refusals at ~1 ms per write, and durable admission sustains ~12k admissions per second.

**证据没有证明什么。** Model-free differential probes isolate a recurringsibling leak—an approval gate suspends its own branch while a sibling branch’s effect executesduring the pause, so a subsequent rejection cannot prevent it—in every evaluated framework that ships a pre-execution gate (five of six, spanning four execution models and two language runtimes; the sixth ships post-hoc review only), and confirm three further gaps on current releases: replay double-execution, cancellation orphans, and timeout zombies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.14166v1#page=5 — PDF page 5; https://arxiv.org/pdf/2607.14166v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.14166v1#page=15 — PDF page 15; https://arxiv.org/pdf/2607.14166v1#page=20 — PDF page 20。Limitations / counterevidence：https://arxiv.org/pdf/2607.14166v1#page=25 — PDF page 25; https://arxiv.org/pdf/2607.14166v1#page=30 — PDF page 30。

**Artifact boundary。** Exact v1 links https://github.com/awslabs/shuttle; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Model-free differential probes isolate a recurringsibling leak—an approval gate suspends its own branch while a sibling branch’s effect executesduring the pause, so a subsequent rejection cannot prevent it—in every evaluated framework that ships a pre-execution gate (five of six, spanning four execution models and two language runtimes; the sixth ships post-hoc review only), and confirm three further gaps on current releases: replay double-execution, cancellation orphans, and timeout zombies.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14166:end -->

<!-- review:SF-2026-ARXIV-2607-14167:start -->
### Structured Feedback Improves Repair in an LLM Agent Loop

<!-- claim:SF-2026-ARXIV-2607-14167:start -->LLM agents often retry after external validation rejects a candidate, but the interface between validation and the next model call remains underspecified. We introduce VeriHarness, a code-controlled agent loop in which models generate candidates while external validators control acceptance, budgets, and traces. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14167:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents often retry after external validation rejects a candidate, but the interface between validation and the next model call remains underspecified.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce VeriHarness, a code-controlled agent loop in which models generate candidates while external validators control acceptance, budgets, and traces.

**证据证明什么。** Presenting the complete repair information in prose instead of a keyed JSON record yields nearly the same success, providing no evidence that JSON syntax itself improves repair.

**证据没有证明什么。** It cannot fix behavior that the validator does not test, and passing one visible test does not guarantee hidden correctness. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14167v1#S2 — 2. Background and System; https://arxiv.org/html/2607.14167v1#S3 — 3. Study Design。Evaluation：https://arxiv.org/html/2607.14167v1#S4 — 4. Results; https://arxiv.org/html/2607.14167v1#S3 — 3. Study Design。Limitations / counterevidence：https://arxiv.org/html/2607.14167v1#S2.SS3 — 2.3. One Failure, Four Feedback Policies; https://arxiv.org/html/2607.14167v1#S4.SS4 — 4.4. When the Validator Cannot Expose the Hidden Failure。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：It cannot fix behavior that the validator does not test, and passing one visible test does not guarantee hidden correctness.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14167:end -->

<!-- review:SF-2026-ARXIV-2607-14169:start -->
### When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models

<!-- claim:SF-2026-ARXIV-2607-14169:start -->Large language models can synthesize a game's rules as executable code - a Code World Model (CWM) - which a classical planner then searches over. Such models are typically accepted when they reach high transition accuracy on sampled trajectories. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14169:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models can synthesize a game's rules as executable code - a Code World Model (CWM) - which a classical planner then searches over.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We show four things. (1) An LLM-synthesized CWM can pass a sampling gate at 100% transition accuracy and be $\geq 98\%$ state-accurate on the planner's own search distribution, yet lose systematically at play, because the $&lt;1\%$ it gets wrong is exactly the pivotal dynamics; the play cost of the omitted rule is $0.091$ (seed-clustered 95% CI $[0.065,0.117]$, $n=4800$).

**证据证明什么。** These results suggest adequacy for planning-oriented world models should be measured on the search distribution or by play directly, not by prediction accuracy on sampled transitions.

**证据没有证明什么。** Feeding example transitions is not a reliable substitute for a complete specification. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14169v1#S2 — 2 Setup and Methods; https://arxiv.org/html/2607.14169v1#S1.SS1 — 1.1 The Code World Model paradigm。Evaluation：https://arxiv.org/html/2607.14169v1#S2.SS5 — 2.5 Experimental configuration; https://arxiv.org/html/2607.14169v1#S3.SS3 — 3.3 The rare-rule instrument: verified but wrong at play (headline result)。Limitations / counterevidence：https://arxiv.org/html/2607.14169v1#S5.SS4 — 5.4 Conclusion: translation, not inference; https://arxiv.org/html/2607.14169v1#S6 — 6 Imperfect Information: The Inference Function as a New Failure Surface。

**Artifact boundary。** Exact v1 links https://github.com/JaviMaligno/code-world-models, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Feeding example transitions is not a reliable substitute for a complete specification.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14169:end -->

<!-- review:SF-2026-ARXIV-2607-14171:start -->
### Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-14171:start -->Reinforcement learning has emerged as the dominant paradigm for training large language model (LLM) agents that interact with executable sandboxes. State-of-the-art algorithms such as PPO, RLOO, and GRPO inherit their rollout topology from RLHF: for each prompt, N independent trajectories are sampled from the initial state, and an advantage is computed by subtracting a group baseline. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14171:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning has emerged as the dominant paradigm for training large language model (LLM) agents that interact with executable sandboxes.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** State-of-the-art algorithms such as PPO, RLOO, and GRPO inherit their rollout topology from RLHF: for each prompt, N independent trajectories are sampled from the initial state, and an advantage is computed by subtracting a group baseline.

**证据证明什么。** On WebShop, ALFWorld, and SWE-bench Verified with Qwen2.5-7B and Llama-3.1-8B backbones, BPO improves success by 3.6--6.1 absolute points over GRPO and RLOO at matched compute, halves gradient-norm variance, and matches the best baseline using 38% fewer policy updates.

**证据没有证明什么。** The picture that emerges is that algorithm design for agent RL is bottlenecked by an assumption inherited from RLHF, that the environment offers nothing more than terminal verification. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14171v1#S4.SS3 — 4.3 Algorithm。Evaluation：https://arxiv.org/html/2607.14171v1#S4.SS4 — 4.4 Theoretical analysis; https://arxiv.org/html/2607.14171v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.14171v1#S6 — 6 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The picture that emerges is that algorithm design for agent RL is bottlenecked by an assumption inherited from RLHF, that the environment offers nothing more than terminal verification.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14171:end -->

<!-- review:SF-2026-ARXIV-2607-14180:start -->
### RENEW: Towards Learning World Models and Repairing Model Exploitation from Preferences

<!-- claim:SF-2026-ARXIV-2607-14180:start -->World models are widely used in offline reinforcement learning (RL) to improve sample efficiency and generate experience beyond a fixed dataset. However, they are vulnerable to model exploitation where data coverage is thin. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14180:end -->

**为什么进入候选分母。** 摘要首要问题为“World models are widely used in offline reinforcement learning (RL) to improve sample efficiency and generate experience beyond a fixed dataset.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Unfortunately, naive DLHF is sample inefficient, so we introduce RENEW, which uses epistemic uncertainty to focus finetuning where the model is most exploitable.

**证据证明什么。** World models are widely used in offline reinforcement learning (RL) to improve sample efficiency and generate experience beyond a fixed dataset.

**证据没有证明什么。** Our experiments use a synthetic oracle rather than real human annotators, and the environments we evaluate are small discrete grid worlds and low-dimensional continuous control tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14180v1#A3 — Appendix C Architecture and Optimization Details; https://arxiv.org/html/2607.14180v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.14180v1#S3 — 3 Experimental Evaluation; https://arxiv.org/html/2607.14180v1#A6 — Appendix F Ablation Studies。Limitations / counterevidence：https://arxiv.org/html/2607.14180v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/FlyingWorkshop/RENEW, http://github.com/RobertTLange/gymnax, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Our experiments use a synthetic oracle rather than real human annotators, and the environments we evaluate are small discrete grid worlds and low-dimensional continuous control tasks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14180:end -->

<!-- review:SF-2026-ARXIV-2607-14186:start -->
### NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs

<!-- claim:SF-2026-ARXIV-2607-14186:start -->Scaling executable agent training data for LLM post-training is bottlenecked by substrate-bound methods that tie task generation to predefined tools, repositories, or skill graphs: expanding coverage requires manual substrate engineering, each new domain demands a bespoke pipeline, and the resulting task distributions often reflect substrate biases rather than real-world demand. We introduce NexForge, a requirement-driven framework that takes high-level capability requirements as input and synthesizes diverse, executable agent tasks and expert trajectories for SFT. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14186:end -->

**为什么进入候选分母。** 摘要首要问题为“Scaling executable agent training data for LLM post-training is bottlenecked by substrate-bound methods that tie task generation to predefined tools, repositories, or skill graphs: expanding coverage requires manual substrate engineering, each new domain demands a bespoke pipeline, and the resulting task distributions often reflect substrate biases rather than real-world demand.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce NexForge, a requirement-driven framework that takes high-level capability requirements as input and synthesizes diverse, executable agent tasks and expert trajectories for SFT.

**证据证明什么。** Nex-N2 models are available at https://nex.sii.edu.cn/.

**证据没有证明什么。** 6 Conclusion and Future Work We present NexForge, a requirement-first framework that scales executable agent task synthesis from free-form user needs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14186v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.14186v1#A5 — Appendix E Detailed Evaluation Results; https://arxiv.org/html/2607.14186v1#A6 — Appendix F Terminal Ablation Details。Limitations / counterevidence：https://arxiv.org/html/2607.14186v1#S6 — 6 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Conclusion and Future Work We present NexForge, a requirement-first framework that scales executable agent task synthesis from free-form user needs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14186:end -->

<!-- review:SF-2026-ARXIV-2607-14189:start -->
### MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation

<!-- claim:SF-2026-ARXIV-2607-14189:start -->Multi-reference-to-audio-video (MR2AV) generation aims to generate coherent audio-video content conditioned on multiple references and textual instructions. Existing benchmarks mainly focus on text-driven generation, single-reference subject preservation, or isolated audio-video alignment, leaving the emerging MR2AV setting largely unexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14189:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-reference-to-audio-video (MR2AV) generation aims to generate coherent audio-video content conditioned on multiple references and textual instructions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this gap, we introduce MultiRef-Compass, a unified benchmark for MR2AV generation.

**证据证明什么。** Extensive experiments on eight representative MR2AV systems reveal substantial room for improvement across multiple evaluation dimensions, underscoring the need for a comprehensive benchmark and positioning MultiRef-Compass as a foundation for future MR2AV research.

**证据没有证明什么。** Limitations MultiRef-Compass is designed as a controlled diagnostic benchmark and therefore does not cover every creative domain, cultural style, or reference modality. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14189v1#A2.SS1 — B.1 Overview and Design Rationale; https://arxiv.org/html/2607.14189v1#Sx4 — Evaluation Framework。Evaluation：https://arxiv.org/html/2607.14189v1#A3 — Appendix C Board4 Analysis; https://arxiv.org/html/2607.14189v1#A4.SS1 — D.1 Entity Fidelity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.14189v1#Sx6 — Limitations; https://arxiv.org/html/2607.14189v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations MultiRef-Compass is designed as a controlled diagnostic benchmark and therefore does not cover every creative domain, cultural style, or reference modality.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14189:end -->

<!-- review:SF-2026-ARXIV-2607-14194:start -->
### Inference-Time Concept Suppression and Video-Centric Evaluation for Text-to-Video Models

<!-- claim:SF-2026-ARXIV-2607-14194:start -->Text-to-video (T2V) generators can synthesize realistic and temporally coherent videos, but controllably removing a target concept from a generator remains difficult. Unlike text-to-image concept erasure, T2V unlearning must suppress a target concept that may persist across frames while preserving non-target subjects, actions, scenes, and temporal structure. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14194:end -->

**为什么进入候选分母。** 摘要首要问题为“Text-to-video (T2V) generators can synthesize realistic and temporally coherent videos, but controllably removing a target concept from a generator remains difficult.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose \textbf{SIRUS}, a training-free inference-time framework for concept-level T2V unlearning.

**证据证明什么。** Transfer experiments on Wan2.2 further suggest that SIRUS generalizes across modern T2V backbones.

**证据没有证明什么。** The main limitations are that parachute-like salient persistent objects remain difficult, preservation must be read jointly with forgetting, and Refusal Vector is not backbone-controlled because it is built on OpenSora2. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14194v1#S3 — 3 Method; https://arxiv.org/html/2607.14194v1#S4 — 4 Evaluation Framework and Implementation。Evaluation：https://arxiv.org/html/2607.14194v1#A2 — Appendix B Additional Experimental Results; https://arxiv.org/html/2607.14194v1#A2.SS1 — B.1 Per-Concept Any-Hit Results。Limitations / counterevidence：https://arxiv.org/html/2607.14194v1#S5.SS5 — 5.5 Discussion; https://arxiv.org/html/2607.14194v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ultralytics/ultralytics, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The main limitations are that parachute-like salient persistent objects remain difficult, preservation must be read jointly with forgetting, and Refusal Vector is not backbone-controlled because it is built on OpenSora2.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14194:end -->

<!-- review:SF-2026-ARXIV-2607-14202:start -->
### KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned Video Generation

<!-- claim:SF-2026-ARXIV-2607-14202:start -->Video generation increasingly relies on keyframe-based workflows, where creators specify a sequence of reference images to guide generation. Although recent models support multi-keyframe conditioning, it remains unclear whether they can faithfully reproduce the prescribed keyframes while maintaining overall video quality. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14202:end -->

**为什么进入候选分母。** 摘要首要问题为“Video generation increasingly relies on keyframe-based workflows, where creators specify a sequence of reference images to guide generation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Experiments on nine representative video generation systems reveal several fundamental limitations.

**证据证明什么。** Their performance further degrades as keyframe constraints become denser and most open-source models also fail to interpret storyboard-grid inputs as temporally ordered keyframe sequences.

**证据没有证明什么。** We hope KeyFrame-Compass serves as a standardized benchmark for diagnosing these limitations and facilitates future progress in keyframe-conditioned video generation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14202v1#S3.SS1 — 3.1 Benchmark Design; https://arxiv.org/html/2607.14202v1#S1.SS1 — A.1 Performance of Proprietary Models。Evaluation：https://arxiv.org/html/2607.14202v1#S2.SS2 — 2.2 Benchmarks for Video Generation; https://arxiv.org/html/2607.14202v1#S3.SS1 — 3.1 Benchmark Design。Limitations / counterevidence：https://arxiv.org/html/2607.14202v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/cactusqq/KeyFrame-Compass, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We hope KeyFrame-Compass serves as a standardized benchmark for diagnosing these limitations and facilitates future progress in keyframe-conditioned video generation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14202:end -->

<!-- review:SF-2026-ARXIV-2607-14236:start -->
### Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection

<!-- claim:SF-2026-ARXIV-2607-14236:start -->Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14236:end -->

**为什么进入候选分母。** 摘要首要问题为“Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline demonstration distribution.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge.

**证据证明什么。** Across towel folding, book insertion, and Hanoi ring placement, LIFT learns faster and reaches higher performance than vision-only post-training, while ablations show that reactive force memory and online corrective data are both important for robust contact-rich manipulation.

**证据没有证明什么。** LIFT still depends on human corrections during online DAgger, which limits data throughput. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14236v1#S3 — 3 Methods; https://arxiv.org/html/2607.14236v1#S3.SS4 — 3.4 Pipeline overview and system implementation。Evaluation：https://arxiv.org/html/2607.14236v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.14236v1#A10 — Appendix J Extended failure-mode analysis。Limitations / counterevidence：https://arxiv.org/html/2607.14236v1#S6 — 6 Conclusion and Limitations; https://arxiv.org/html/2607.14236v1#A10 — Appendix J Extended failure-mode analysis。

**Artifact boundary。** Exact v1 links https://github.com/flexivrobotics/flexiv_tdk, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：LIFT still depends on human corrections during online DAgger, which limits data throughput.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14236:end -->

<!-- review:SF-2026-ARXIV-2607-14252:start -->
### MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning

<!-- claim:SF-2026-ARXIV-2607-14252:start -->Embodied agents accumulate experience over time. We study how accumulated experience can be formed into persistent memory for future reasoning and action. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14252:end -->

**为什么进入候选分母。** 摘要首要问题为“Embodied agents accumulate experience over time.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce MEMORA, a framework that instantiates EAM through a formation-consolidation-retrieval lifecycle and a multi-store world-memory architecture.

**证据证明什么。** A physical-robot demonstration further shows that memory formed solely from human egocentric video can ground high-level robot plans in participant-specific objects and preferences.

**证据没有证明什么。** Finally, consolidated Inferred Knowledge is optimized for planning and preference retrieval; it should not be interpreted as an exhaustive transcript of every observed event. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14252v1#S4 — IV Method; https://arxiv.org/html/2607.14252v1#A1.SS1 — A-A Implementation Overview。Evaluation：https://arxiv.org/html/2607.14252v1#A2.SS1 — B-A Benchmark Construction; https://arxiv.org/html/2607.14252v1#A2.SS4 — B-D Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.14252v1#A1.SS7 — A-G Limitations; https://arxiv.org/html/2607.14252v1#S6 — VI Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Finally, consolidated Inferred Knowledge is optimized for planning and preference retrieval; it should not be interpreted as an exhaustive transcript of every observed event.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14252:end -->

<!-- review:SF-2026-ARXIV-2607-14275:start -->
### AI Agents Do Not Fail Alone:The Context Fails First

<!-- claim:SF-2026-ARXIV-2607-14275:start -->Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured. Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14275:end -->

**为什么进入候选分母。** 摘要首要问题为“Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context.

**证据证明什么。** Through a controlled context-quality study across regulated agent domains, holding frontier LLM agents fixed and varying only their operating context, we show that context-quality criteria consistently predict their corresponding behavioral outcomes.

**证据没有证明什么。** 5 Conclusion This paper argued that AI agents do not fail only because of model limitations; they also fail because of the context in which they reason. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14275v1#S2.SS1 — 2.1 From Prompt Design to Context Design; https://arxiv.org/html/2607.14275v1#S4.SS1 — 4.1 Study Design。Evaluation：https://arxiv.org/html/2607.14275v1#S3.SS4 — 3.4 Isolation from Behavioral Evaluation; https://arxiv.org/html/2607.14275v1#S4 — 4 Experimental Validation。Limitations / counterevidence：https://arxiv.org/html/2607.14275v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ProofAgent-ai/proofagent-harness, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：5 Conclusion This paper argued that AI agents do not fail only because of model limitations; they also fail because of the context in which they reason.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14275:end -->

<!-- review:SF-2026-ARXIV-2607-14277:start -->
### Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making

<!-- claim:SF-2026-ARXIV-2607-14277:start -->Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction. At inference time, it is preferred that an agent can decide whether to proceed with its current reasoning, defer to a stronger model, request additional information, invoke external tools, or abstain under the given setup. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14277:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce Multi-Head Latent Control, a lightweight layer that reads hidden-state trajectories from a frozen LLM or VLM to produce deployment-time control signals.

**证据证明什么。** Additionally, the learned control signals improve tool-use decision quality, yielding up to +158 percent relative score gain and 65.5 percent fewer missed-required tool calls.

**证据没有证明什么。** An important direction for future work is therefore to further improve the quality, robustness, and calibration of these control signals. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14277v1#A2.SS3 — B.3 Model Token Confidence vs. Latent Adequacy Signal; https://arxiv.org/html/2607.14277v1#S4.SS1 — 4.1 Efficient Multi-Model Collaboration。Evaluation：https://arxiv.org/html/2607.14277v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.14277v1#A2 — Appendix B Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.14277v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.14277v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Amirhosein-gh98/Multi-Head-Latent-Control, https://github.com/EvolvingLMMs-Lab/open-r1-multimodal, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：An important direction for future work is therefore to further improve the quality, robustness, and calibration of these control signals.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14277:end -->

<!-- review:SF-2026-ARXIV-2607-14280:start -->
### DiMaS: Distribution Matching for Steering Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-14280:start -->Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation, yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs a task by intervening on its internal representations. Representation steering is a well-established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14280:end -->

**为什么进入候选分母。** 摘要首要问题为“Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation, yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs a task by intervening on its internal representations.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Representation steering is a well-established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs.

**证据证明什么。** Our code is publicly available at https://github.com/pegah-kh/dimas, with additional results and videos at https://pegah-kh.github.io/dimas/

**证据没有证明什么。** Box plots show the per-episode feature distribution at each level, annotated with success rate and𝑝-value vs. baseline; box opacity is higher when the shift is statistically significant (𝑝 <0.01). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.14280v1#page=3 — PDF page 3; https://arxiv.org/pdf/2607.14280v1#page=7 — PDF page 7。Evaluation：https://arxiv.org/pdf/2607.14280v1#page=12 — PDF page 12; https://arxiv.org/pdf/2607.14280v1#page=17 — PDF page 17。Limitations / counterevidence：https://arxiv.org/pdf/2607.14280v1#page=23 — PDF page 23; https://arxiv.org/pdf/2607.14280v1#page=26 — PDF page 26。

**Artifact boundary。** Exact v1 links https://github.com/pegah-kh/dimas, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Box plots show the per-episode feature distribution at each level, annotated with success rate and𝑝-value vs. baseline; box opacity is higher when the shift is statistically significant (𝑝 <0.01).

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14280:end -->

<!-- review:SF-2026-ARXIV-2607-14285:start -->
### ToolAlignBench: Investigating Alignment Conflicts in Tool-Calling Enabled LLMs

<!-- claim:SF-2026-ARXIV-2607-14285:start -->Safety alignment in LLMs aims to align models with human values, but which values take precedence when they conflict? We investigate this question in the context of tool-calling LLM agents deployed in regulated industries, where agents processing confidential documents may encounter content that triggers safety-trained values (e.g., public welfare) that conflict with deployment-context instructions (e.g., internal logging). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14285:end -->

**为什么进入候选分母。** 摘要首要问题为“Safety alignment in LLMs aims to align models with human values, but which values take precedence when they conflict?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We release our benchmark as a framework to support evaluation of agent behavior under competing legitimate interests.

**证据证明什么。** We also find that abliteration reduces rates of external whistleblowing.

**证据没有证明什么。** This reveals that alignment is not monolithic, and that different training components shape different behavioral dimensions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14285v1#A1.SS1 — A.1 Base System Prompt; https://arxiv.org/html/2607.14285v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.14285v1#S2.SS3 — 2.3 Agent Safety and Tool-Calling Evaluation; https://arxiv.org/html/2607.14285v1#S3.SS3 — 3.3 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.14285v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14285v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/aryankeluskar/ToolAlignBench, https://github.com/T3-Content/SnitchBench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This reveals that alignment is not monolithic, and that different training components shape different behavioral dimensions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14285:end -->

<!-- review:SF-2026-ARXIV-2607-14327:start -->
### PReM: Learning What to Preserve and When to Refresh for Context Compression

<!-- claim:SF-2026-ARXIV-2607-14327:start -->Efficient long-context inference is not only about reducing memory cost, but also about keeping useful contextual evidence accessible as generation proceeds. However, existing compression-oriented approaches, such as key-value (KV) cache compression and context compression, often either make an early decision about which contextual information to keep or rely on an external compressor. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14327:end -->

**为什么进入候选分母。** 摘要首要问题为“Efficient long-context inference is not only about reducing memory cost, but also about keeping useful contextual evidence accessible as generation proceeds.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** This paper introduces PReM (Preserve and Refresh Memory), a context-compression framework that maintains the long context as the model's internal layer-wise KV memory and learns what to preserve and when to refresh it.

**证据证明什么。** Experiments with 32K-token contexts show that PReM outperforms strong baselines under both 16x and 32x compression, while maintaining a favorable balance between answer quality and inference efficiency.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14327v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14327v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.14327v1#S4 — 4 Experiments; https://arxiv.org/html/2607.14327v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.14327v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14327:end -->

<!-- review:SF-2026-ARXIV-2607-14336:start -->
### Copy-on-Write Scoring: Application-Specific Agent Evaluations

<!-- claim:SF-2026-ARXIV-2607-14336:start -->Trustworthy deployment of LLM-based agents in software systems requires evaluating how they perform on application-specific workflows, with enough granularity to localize where they succeed and fail. Yet existing agent evaluation mechanisms are limited: benchmarks have low construct validity for application-specific workflows and environments, and replica evaluation environments are expensive and prone to drift. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14336:end -->

**为什么进入候选分母。** 摘要首要问题为“Trustworthy deployment of LLM-based agents in software systems requires evaluating how they perform on application-specific workflows, with enough granularity to localize where they succeed and fail.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose Copy-on-Write (CoW) Scoring, a framework that evaluates agent operations directly within application environments using a PostgreSQL-level Copy-on-Write mechanism to isolate agent writes.

**证据证明什么。** We demonstrate the framework on Plane, an open-source project-management platform, where analysis surfaced specific issues in the tool surface, and corresponding fixes produced measurable improvements on affected models.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14336v1#S3 — 3 Methods; https://arxiv.org/html/2607.14336v1#S4.SS1 — 4.1 Initial scores across models。Evaluation：https://arxiv.org/html/2607.14336v1#A3 — Appendix C Plane Integration and Experimental Setup; https://arxiv.org/html/2607.14336v1#A4 — Appendix D Results Summary。Limitations / counterevidence：https://arxiv.org/html/2607.14336v1#S4.SS2 — 4.2 Diagnosing failure modes; https://arxiv.org/html/2607.14336v1#S5 — 5 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/trail-ml/agent-cow-python, https://github.com/JoannaRoy/plane-cow, https://github.com/JoannaRoy/plane-cow/blob/preview/results.zip; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14336:end -->

<!-- review:SF-2026-ARXIV-2607-14340:start -->
### The Prover Is the Judge: Verified Security Software from AI Coding Agents in Ada/SPARK

<!-- claim:SF-2026-ARXIV-2607-14340:start -->AI coding agents produce code faster than humans can review it. In our approach, the prover is the judge of whether the code is correct. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14340:end -->

**为什么进入候选分母。** 摘要首要问题为“AI coding agents produce code faster than humans can review it.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In our approach, the prover is the judge of whether the code is correct.

**证据证明什么。** We report where each layer caught faults and draw the central lesson: what an agent can be trusted to establish is bounded by the strength of its feedback.

**证据没有证明什么。** The engineer’s role shifts from author to designer of specifications, checks, and process constraints, and to final judge of what the machine cannot decide. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14340v1#S3 — III Method: The Verifier-Driven Loop; https://arxiv.org/html/2607.14340v1#S6 — VI From Components to a Running System。Evaluation：https://arxiv.org/html/2607.14340v1#S3.SS3 — III-C Study Setup。Limitations / counterevidence：https://arxiv.org/html/2607.14340v1#S11 — XI Conclusion; https://arxiv.org/html/2607.14340v1#S7 — VII Failure Modes: The Limits of Proof。

**Artifact boundary。** Exact v1 links https://github.com/tobiasphilipp/experimental-agentic-verified-software, https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html, https://github.com/rod-chapman/SPARKNaCl; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The engineer’s role shifts from author to designer of specifications, checks, and process constraints, and to final judge of what the machine cannot decide.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14340:end -->

<!-- review:SF-2026-ARXIV-2607-14386:start -->
### CIPHER: A Decoupled Exploration-Selection Framework for Test-Time Scaling of Data Science Agents

<!-- claim:SF-2026-ARXIV-2607-14386:start -->Data science tasks span from closed-ended information extraction to open-ended analysis, presenting significant challenges for automation. Recent AI agents powered by language models show promise for handling such complex tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14386:end -->

**为什么进入候选分母。** 摘要首要问题为“Data science tasks span from closed-ended information extraction to open-ended analysis, presenting significant challenges for automation.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To mitigate this, we present CIPHER, an automated data science agent that leverages test-time scaling through the generation and selection of multiple initial states for concurrent execution.

**证据证明什么。** Recent AI agents powered by language models show promise for handling such complex tasks.

**证据没有证明什么。** Future research avenues include the scaling of ensemble generation, and the selection of candidate states using gradient based methods [ Mirzasoleiman et al., 2020 ] . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14386v1#A3 — Appendix C Details on CIPHER and DES design and implementation; https://arxiv.org/html/2607.14386v1#S3 — 3 The Decoupled Exploration-Selection (DES) Framework。Evaluation：https://arxiv.org/html/2607.14386v1#A4 — Appendix D Additional results; https://arxiv.org/html/2607.14386v1#S3.SS3 — 3.3 Aggregating diverse execution results。Limitations / counterevidence：https://arxiv.org/html/2607.14386v1#A2 — Appendix B Discussion and limitations; https://arxiv.org/html/2607.14386v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/amazon/Titan-text-embeddings-v2, https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future research avenues include the scaling of ensemble generation, and the selection of candidate states using gradient based methods [ Mirzasoleiman et al., 2020 ] .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14386:end -->

<!-- review:SF-2026-ARXIV-2607-14390:start -->
### Why Git Is the Memory Solution for the Agentic Development Lifecycle

<!-- claim:SF-2026-ARXIV-2607-14390:start -->Coding agents now produce a growing share of a team's code, while the reasoning behind each change -- the alternatives weighed, the constraints discovered, the approaches rejected -- is trapped in assistant transcripts that vanish with the session. Memory for this setting, the agentic development lifecycle (ADLC), is usually posed as one retrieval problem and built as machinery: tiered stores, memory graphs, compiled wikis, model-judged admission. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14390:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents now produce a growing share of a team's code, while the reasoning behind each change -- the alternatives weighed, the constraints discovered, the approaches rejected -- is trapped in assistant transcripts that vanish with the session.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Routed, the system answers at 382-980 tokens per question -- three orders of magnitude below the recorded history.

**证据证明什么。** Code, benchmark, and paper source: github.com/rekal-dev/rekal-cli.

**证据没有证明什么。** 11 Limitations The sufficiency evidence is small: – questions per corpus, one blind judge, one execution model; we report CIs and treat magnitudes as directional, and the honest summary of Table 2 is per-kind patterns, not separable pooled rankings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14390v1#S1 — 1 The question an agent actually asks; https://arxiv.org/html/2607.14390v1#S2 — 2 A worked example。Evaluation：https://arxiv.org/html/2607.14390v1#S8 — 8 Evaluation: answer-sufficiency, not rank; https://arxiv.org/html/2607.14390v1#S8.SS2 — 8.2 Gating and the rationale ablation。Limitations / counterevidence：https://arxiv.org/html/2607.14390v1#S11 — 11 Limitations; https://arxiv.org/html/2607.14390v1#S12 — 12 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/rekal-dev/rekal-cli, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：11 Limitations The sufficiency evidence is small: – questions per corpus, one blind judge, one execution model; we report CIs and treat magnitudes as directional, and the honest summary of Table 2 is per-kind patterns, not separable pooled rankings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14390:end -->

<!-- review:SF-2026-ARXIV-2607-14396:start -->
### CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models

<!-- claim:SF-2026-ARXIV-2607-14396:start -->Product catalogs are the backbone of e-commerce sites, yet a large number of structured attributes (SAs) -- such as material, color, and shape -- often have missing values. Typically, SA values are extracted from product information, including titles and descriptions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14396:end -->

**为什么进入候选分母。** 摘要首要问题为“Product catalogs are the backbone of e-commerce sites, yet a large number of structured attributes (SAs) -- such as material, color, and shape -- often have missing values.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce \texttt{CatalogAgent}, a novel agentic system that continuously improves Generator and Evaluator models for e-commerce catalog enrichment.

**证据证明什么。** These learnings are fed back to the worker Generator and Evaluator LLMs, enabling self-improvement without human intervention.

**证据没有证明什么。** Future directions include using high quality labels generated from Supervisor Agent to finetune worker Generator and Evaluator LLMs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14396v1#Pt0.A1 — Appendix 0.A Appendix: Analysis of the Performance of Generator–Evaluator-Supervisor framework; https://arxiv.org/html/2607.14396v1#S2 — 2 CatalogAgent: A Supervisor-mediated Self-Learning System。Evaluation：https://arxiv.org/html/2607.14396v1#S3 — 3 Experiments and Results; https://arxiv.org/html/2607.14396v1#Pt0.A1 — Appendix 0.A Appendix: Analysis of the Performance of Generator–Evaluator-Supervisor framework。Limitations / counterevidence：https://arxiv.org/html/2607.14396v1#S5 — 5 Conclusion and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future directions include using high quality labels generated from Supervisor Agent to finetune worker Generator and Evaluator LLMs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14396:end -->

<!-- review:SF-2026-ARXIV-2607-14399:start -->
### Instrument Effects in Language-Model Honesty Evaluation: An Auditable Single-System Demonstration

<!-- claim:SF-2026-ARXIV-2607-14399:start -->Evaluations of language-model honesty read the model's verdicts as evidence about the model. We built a text-adventure world where the game engine, not any model, knows whether the quest can be completed. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14399:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluations of language-model honesty read the model's verdicts as evidence about the model.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose a four-check integrity protocol for eval instruments.

**证据证明什么。** Decision rules were recorded before results were read, and run artifacts bind the revisions they executed; the strength of preregistration varies by series and is disclosed.

**证据没有证明什么。** These estimates are instrument- and sampling-frame-dependent, not population reliability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14399v1#Sx3 — 3. Methods; https://arxiv.org/html/2607.14399v1#Sx7 — 7. Process integrity as method。Evaluation：https://arxiv.org/html/2607.14399v1#Sx4 — 4. Results; https://arxiv.org/html/2607.14399v1#Sx5.SSx2 — 5.2 What these results do not license。Limitations / counterevidence：https://arxiv.org/html/2607.14399v1#Sx5 — 5. Discussion; https://arxiv.org/html/2607.14399v1#Sx6 — 6. Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Aargau/latent-underground/releases/tag/v1.0-arxiv, https://github.com/UKGovernmentBEIS/inspect_ai, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These estimates are instrument- and sampling-frame-dependent, not population reliability.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14399:end -->

<!-- review:SF-2026-ARXIV-2607-14408:start -->
### Reward-Free Evolving Agents via Pairwise Validator

<!-- claim:SF-2026-ARXIV-2607-14408:start -->A self-evolving agentic loop repeatedly proposes a tweaked version of an agent (its prompt template or program) and accepts or rejects the change based on a per-iteration quality signal. Designing that signal is often the costly part of the project: a reliable scalar reward requires domain expertise and labeled examples that are themselves as expensive to assemble as the agent's underlying task. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14408:end -->

**为什么进入候选分母。** 摘要首要问题为“A self-evolving agentic loop repeatedly proposes a tweaked version of an agent (its prompt template or program) and accepts or rejects the change based on a per-iteration quality signal.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose replacing the scalar at the accept/reject gate with a pairwise validator: a frozen LLM that, given the parent and child candidate, returns a binary verdict on which is better.

**证据证明什么。** The pairwise gate is thus a drop-in replacement for per-step reward design at competitive task accuracy without the labeling cost.

**证据没有证明什么。** The gain is sensitive to four regimes that bound where the substitution holds: 1) saturation, where the baseline is already near the agent’s ceiling and there is no headroom for the gate to exploit; 2) small- test sets, where a single problem moves the score and per-cell deltas read as noise; 3) agent-capability gaps, where the agent fundamentally lacks the ability to make progress on a task and a validator gate cannot surface ability that is not there; 4) validator-capability mismatch, where the validator itself struggles on the task type and pairwise verdicts become unreliable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14408v1#S4 — 4 Our Method。Evaluation：https://arxiv.org/html/2607.14408v1#S5 — 5 Results; https://arxiv.org/html/2607.14408v1#S5.SS2 — 5.2 Main Results on Prompt Evolution。Limitations / counterevidence：https://arxiv.org/html/2607.14408v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The gain is sensitive to four regimes that bound where the substitution holds: 1) saturation, where the baseline is already near the agent’s ceiling and there is no headroom for the gate to exploit; 2) small- test sets, where a single problem moves the score and per-cell deltas read as noise; 3) agent-capability gaps, where the agent fundamentally lacks the ability to make progress on a task and a validator gate cannot surface ability that is not there; 4) validator-capability mismatch, where the validator itself struggles on the task type and pairwise verdicts become unreliable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14408:end -->

<!-- review:SF-2026-ARXIV-2607-14431:start -->
### Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel

<!-- claim:SF-2026-ARXIV-2607-14431:start -->We report a way to make a frozen small language model both more capable and dramatically cheaper at once, without changing any weights. Verified knowledge is deposited once as a byte-exact key-value (KV) state artifact and later restored, by graft, into a fresh inference context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14431:end -->

**为什么进入候选分母。** 摘要首要问题为“We report a way to make a frozen small language model both more capable and dramatically cheaper at once, without changing any weights.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We describe the system at the behavior level; the engine is proprietary, and every reported number is backed by committed input and output hashes so the scoring can be re-checked without it.

**证据证明什么。** We show that own-position graft is the unique numerically exact operating point on a model with floating-point rotary encoding, and we verify byte-exactness on two model scales (12B, 31B) and two GPU targets, one through a pre-registered replay.

**证据没有证明什么。** Composition is byte-exact only against a chunked reference, not a monolithic one, though it is functionally correct in sequence (Section 4.8). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14431v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14431v1#S4.SS10 — 4.10 Cross-architecture byte-exactness: a pre-registered B200 replay。Evaluation：https://arxiv.org/html/2607.14431v1#S4 — 4 Empirical Results。Limitations / counterevidence：https://arxiv.org/html/2607.14431v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14431v1#S5.SS3 — 5.3 Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3.6-35B-A3B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Composition is byte-exact only against a chunked reference, not a monolithic one, though it is functionally correct in sequence (Section 4.8).

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14431:end -->

<!-- review:SF-2026-ARXIV-2607-14439:start -->
### Active Real-World Factor-Based Evaluation for Generalist Robot Policies

<!-- claim:SF-2026-ARXIV-2607-14439:start -->Generalist robot manipulation policies trained on large, diverse datasets have shown remarkable promise across a wide range of tasks. However, rigorously evaluating these policies remains a fundamental challenge. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14439:end -->

**为什么进入候选分母。** 摘要首要问题为“Generalist robot manipulation policies trained on large, diverse datasets have shown remarkable promise across a wide range of tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose an active evaluation framework that addresses this challenge by treating policy evaluation as a sequential experimental design problem.

**证据证明什么。** Generalist robot manipulation policies trained on large, diverse datasets have shown remarkable promise across a wide range of tasks.

**证据没有证明什么。** V-A Limitations & Future Work There are multiple avenues for future work in this problem space. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14439v1#S3 — III Methodology。Evaluation：https://arxiv.org/html/2607.14439v1#S2.SS2 — II-B Benchmarks for Generalist Robot Policies; https://arxiv.org/html/2607.14439v1#S2.SS3 — II-C Sample-efficient Robot Policy Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.14439v1#S5.SS1 — V-A Limitations & Future Work; https://arxiv.org/html/2607.14439v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：V-A Limitations & Future Work There are multiple avenues for future work in this problem space.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14439:end -->

<!-- review:SF-2026-ARXIV-2607-14443:start -->
### Tactile: Giving Computer-Using Agents Hands and Feet

<!-- claim:SF-2026-ARXIV-2607-14443:start -->Computer-use agents are becoming capable software operators, but their interface to desktop applications is still often a brittle motor layer: they look at screenshots, predict coordinates, click, and hope that the visible state changed as intended. This collapses target grounding, action execution, and outcome verification into a single ambiguous operation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14443:end -->

**为什么进入候选分母。** 摘要首要问题为“Computer-use agents are becoming capable software operators, but their interface to desktop applications is still often a brittle motor layer: they look at screenshots, predict coordinates, click, and hope that the visible state changed as intended.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present Tactile, an open-source tool layer that gives agents a more reliable "hands and feet" for desktop use.

**证据证明什么。** On macOSWorld-style tasks, adding Tactile improves Codex Success@100 from 41.1% to 50.0% overall and from 45.2% to 55.3% on accessibility-adapted tasks; a 96-task cross-agent subset shows consistent gains across Codex, Claude Code, OpenCode, and Goose.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14443v1#S4 — 4 System Design and Implementation; https://arxiv.org/html/2607.14443v1#S2.SS4 — 2.4 Design Requirements。Evaluation：https://arxiv.org/html/2607.14443v1#S5 — 5 Results; https://arxiv.org/html/2607.14443v1#S5.SS1 — 5.1 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.14443v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.14443v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://developers.openai.com/codex/cli, https://claude.com/product/claude-code, https://opencode.ai/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14443:end -->

<!-- review:SF-2026-ARXIV-2607-14493:start -->
### Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation

<!-- claim:SF-2026-ARXIV-2607-14493:start -->Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks including summarization, alert triage, and threat investigation. These systems ingest logs from external-facing services and process network logs as natural language contexts to generate security insights. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14493:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks including summarization, alert triage, and threat investigation.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present LogInject, a systematic framework for evaluating these threats.

**证据证明什么。** We demonstrate that this architectural pattern introduces a critical vulnerability: adversaries can embed prompt injection payloads in log-generating fields that persist in storage and are executed when analysts query the LLM, achieving what we term passive prompt injection.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14493v1#S5 — 5 Evaluation Framework; https://arxiv.org/html/2607.14493v1#S3 — 3 Problem Statement and Threat Model。Evaluation：https://arxiv.org/html/2607.14493v1#S10.SS2 — 10.2 Experimental Safeguards; https://arxiv.org/html/2607.14493v1#S5 — 5 Evaluation Framework。Limitations / counterevidence：https://arxiv.org/html/2607.14493v1#S3 — 3 Problem Statement and Threat Model; https://arxiv.org/html/2607.14493v1#S8 — 8 Discussion。

**Artifact boundary。** Exact v1 links https://doi.org/10.18653/v1/2025.emnlp-demos.55, https://aclanthology.org/2025.emnlp-demos.55/, https://owasp.org/www-project-top-10-for-large-language-model-applications/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14493:end -->

<!-- review:SF-2026-ARXIV-2607-14499:start -->
### Contextualized Evaluation of Vision Language Models through Dynamic, Multi-turn Interactions

<!-- claim:SF-2026-ARXIV-2607-14499:start -->Multi-modal Large Language Models (MLLMs) have made substantial advances on benchmarks, yet their real-world effectiveness remains uncertain. This gap stems from the fundamental misalignment between benchmarks in controlled, static settings and the dynamic, interactive, and contextualized nature of real-world applications. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14499:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-modal Large Language Models (MLLMs) have made substantial advances on benchmarks, yet their real-world effectiveness remains uncertain.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To bridge this gap, we propose CEDI (Contextualized Evaluations of MLLMs through Dynamic, multi-round Interactions), a framework that recasts evaluation as a three-party interaction between an evaluatee model, an automated examiner, and a grader.

**证据证明什么。** Empirical results across multiple models, diverse settings, datasets, and domains show that contextualized, interactive evaluations reveal not only significantly more hallucinations than conventional static evaluation but also ones that more closely resemble those arising in practical use cases.

**证据没有证明什么。** Across multiple models, datasets, automatic metrics, and human annotations, CEDI consistently exposes more hallucinations, achieves broader visual coverage, and produces interactions and failures that are more relevant to realistic user contexts than captioning, binary-question, and prompt-only baselines. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14499v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14499v1#A5 — Appendix E Evaluated Models。Evaluation：https://arxiv.org/html/2607.14499v1#S2.SS1 — 2.1 Evaluation and Benchmarking MLLMs; https://arxiv.org/html/2607.14499v1#S5.SS3 — 5.3 Evaluation Result (RQ\scriptsize3⃝)。Limitations / counterevidence：https://arxiv.org/html/2607.14499v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.14499v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/williamium3000/cedi, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Across multiple models, datasets, automatic metrics, and human annotations, CEDI consistently exposes more hallucinations, achieves broader visual coverage, and produces interactions and failures that are more relevant to realistic user contexts than captioning, binary-question, and prompt-only baselines.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14499:end -->

<!-- review:SF-2026-ARXIV-2607-14506:start -->
### Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards

<!-- claim:SF-2026-ARXIV-2607-14506:start -->While reinforcement learning with verifiable rewards (RLVR) is widely used to improve the reasoning capabilities of large language models (LLMs), the generalizability of the resulting models remains poorly understood. In this work, we establish the first non-vacuous generalization bounds for parameter-efficient RLVR fine-tuning at the billion-parameter scale. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14506:end -->

**为什么进入候选分母。** 摘要首要问题为“While reinforcement learning with verifiable rewards (RLVR) is widely used to improve the reasoning capabilities of large language models (LLMs), the generalizability of the resulting models remains poorly understood.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To operationalize these bounds, we propose the Progressive RLVR framework, which integrates RLVR with on-policy distillation, TinyLoRA, and model quantization.

**证据证明什么。** We show that this framework yields non-vacuous generalization bounds in four domains: mathematical problem-solving, programming, general-knowledge reasoning, and Text-to-SQL.

**证据没有证明什么。** Our work has two limitations that could motivate directions for future research. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14506v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14506v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.14506v1#A2 — Appendix B Experimental Setup and Hyperparameters; https://arxiv.org/html/2607.14506v1#A2.SS3 — B.3 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.14506v1#S6 — 6 Discussion; https://arxiv.org/html/2607.14506v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/uiuc-kang-lab/rlvr_generalization_bounds, https://huggingface.co/collections/uiuc-kang-lab/rlvr-generalization-bounds, https://github.com/huggingface/Math-Verify; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our work has two limitations that could motivate directions for future research.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14506:end -->

<!-- review:SF-2026-ARXIV-2607-14512:start -->
### RetroAgent: Harnessing LLMs to Search Over Structured Memory for Agentic Retrosynthesis Planning

<!-- claim:SF-2026-ARXIV-2607-14512:start -->Multi-step retrosynthesis planning seeks to decompose a target molecule into commercially available building blocks through a sequence of feasible reactions. The vast combinatorial search space makes this task challenging even for expert chemists. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14512:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-step retrosynthesis planning seeks to decompose a target molecule into commercially available building blocks through a sequence of feasible reactions.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce RetroAgent, an LLM agent that bridges symbolic search and neural reasoning through a harness with structured memory.

**证据证明什么。** Experiments on in-distribution and out-of-distribution benchmarks demonstrate that RetroAgent delivers strong performance and generalization.

**证据没有证明什么。** These considerations affect all template-based planners equally and depend on information absent from the benchmarks, which provide only target molecules and, for USPTO-190, reference routes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14512v1#A1 — Appendix A System Prompt; https://arxiv.org/html/2607.14512v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.14512v1#A6 — Appendix F Evaluation Protocol; https://arxiv.org/html/2607.14512v1#A7 — Appendix G Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.14512v1#A4 — Appendix D Limitations and Discussion; https://arxiv.org/html/2607.14512v1#A9 — Appendix I Failure Case Analysis。

**Artifact boundary。** Exact v1 links https://github.com/SXKDZ/RetroAgent, https://huggingface.co/SXKDZ/RetroAgent, https://github.com/THUDM/slime; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：These considerations affect all template-based planners equally and depend on information absent from the benchmarks, which provide only target molecules and, for USPTO-190, reference routes.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14512:end -->

<!-- review:SF-2026-ARXIV-2607-14541:start -->
### Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent

<!-- claim:SF-2026-ARXIV-2607-14541:start -->Existing GPU kernel generation benchmarks draw problems from synthetic or curated sources that diverge from deployed workloads. We present Atrex-Bench, a benchmark whose 30 operators and 440 shapes are sampled directly from full-cluster production inference traces of compute-limited, memory-rich GPUs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14541:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing GPU kernel generation benchmarks draw problems from synthetic or curated sources that diverge from deployed workloads.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present Atrex-Bench, a benchmark whose 30 operators and 440 shapes are sampled directly from full-cluster production inference traces of compute-limited, memory-rich GPUs.

**证据证明什么。** Evaluating six frontier coding agents on Atrex-Bench shows that even the best vanilla model reaches only ${\sim}10\%$ of the hardware roofline on production operators; and correctness alone overstates capability, since much of the apparent pass rate comes from PyTorch fallbacks rather than kernels the model wrote.

**证据没有证明什么。** We do not claim that the current trace slice represents every future hardware class. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14541v1#S3 — 3 Atrex-Bench: Design; https://arxiv.org/html/2607.14541v1#S5.SS2 — 5.2 Architecture and Workflow。Evaluation：https://arxiv.org/html/2607.14541v1#A1 — Appendix A Per-Operator Results; https://arxiv.org/html/2607.14541v1#S2.SS1 — 2.1 LLM Kernel Generation Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.14541v1#S6 — 6 Discussion; https://arxiv.org/html/2607.14541v1#S6.SS1 — 6.1 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/alibaba/atrex-bench, https://github.com/alibaba/atrex-kernel-agent, https://github.com/ROCm/aiter; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We do not claim that the current trace slice represents every future hardware class.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14541:end -->

<!-- review:SF-2026-ARXIV-2607-14543:start -->
### SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents

<!-- claim:SF-2026-ARXIV-2607-14543:start -->Vision-language models (VLMs) are increasingly used as the reasoning backbone of embodied agents, enabling robots to interpret visual scenes, follow language instructions, and plan multi-step actions. In household environments, however, safety depends not only on recognizing objects, but also on how actions change the physical scene over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14543:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language models (VLMs) are increasingly used as the reasoning backbone of embodied agents, enabling robots to interpret visual scenes, follow language instructions, and plan multi-step actions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this gap, we introduce SAFERELBENCH, a spatial-relation-aware safety benchmark with 507 executable evaluation samples, including 248 spatial-relation samples and 259 non-spatial control samples.

**证据证明什么。** More broadly, our results show that safe embodied intelligence requires not only stronger perception and planning, but also reliable reasoning about how object relations shape risk during interaction.

**证据没有证明什么。** These relations cover important household risks, but do not exhaust all embodied safety hazards, such as long-horizon temporal dependencies, hidden object states, material properties, or multi-agent interaction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14543v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14543v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.14543v1#S4.SS3 — 4.3 Ablation Analysis; https://arxiv.org/html/2607.14543v1#S3.SS2 — 3.2 Task and Safety Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.14543v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.14543v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These relations cover important household risks, but do not exhaust all embodied safety hazards, such as long-horizon temporal dependencies, hidden object states, material properties, or multi-agent interaction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14543:end -->

<!-- review:SF-2026-ARXIV-2607-14547:start -->
### AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents

<!-- claim:SF-2026-ARXIV-2607-14547:start -->Active visual agents solve fine-grained image tasks by interleaving reasoning with image-grounding actions across multiple turns. However, deployment-time rollout budgets are rarely fixed: some requests permit long rollouts, while others require the agent to act under a tight turn limit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14547:end -->

**为什么进入候选分母。** 摘要首要问题为“Active visual agents solve fine-grained image tasks by interleaving reasoning with image-grounding actions across multiple turns.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To overcome this challenge, we present AdaTurn, a budget-aware framework that conditions the agent on the allowed number of turns and explicitly trains the boundary behavior induced by the budget.

**证据证明什么。** AdaTurn substantially improves low-budget accuracy, for example raising VisualProbe-Medium from 36.7% to 47.6% at four turns, while preserving strong scaling at larger budgets and transferring effectively to multiple backbones and general multimodal benchmarks.

**证据没有证明什么。** Forced-answer training mitigates catastrophic truncation by ensuring that the model produces a valid answer even when the search budget is insufficient, but it cannot guarantee correctness when the collected evidence remains ambiguous. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14547v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.14547v1#A3 — Appendix C Detailed Ablation Discussion; https://arxiv.org/html/2607.14547v1#A8 — Appendix H Failure Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.14547v1#A3 — Appendix C Detailed Ablation Discussion; https://arxiv.org/html/2607.14547v1#A8 — Appendix H Failure Analysis。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/Mini-o3/Mini-o3-Coldstart-Dataset, https://huggingface.co/datasets/Mini-o3/DeepEyes_train_4K, https://huggingface.co/datasets/Mini-o3/VisualProbe_train; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Forced-answer training mitigates catastrophic truncation by ensuring that the model produces a valid answer even when the search budget is insufficient, but it cannot guarantee correctness when the collected evidence remains ambiguous.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14547:end -->

<!-- review:SF-2026-ARXIV-2607-14548:start -->
### HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents

<!-- claim:SF-2026-ARXIV-2607-14548:start -->As large multimodal models move from understanding content to operating on digital environments, mobile GUI has emerged as a challenging and consequential testbed for digital embodied intelligence. Mobile agents operate under three coupled constraints: precise perception of complex interfaces, scalable acquisition of high-quality interaction data, and robust long-horizon decision making under compounding execution errors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14548:end -->

**为什么进入候选分母。** 摘要首要问题为“As large multimodal models move from understanding content to operating on digital environments, mobile GUI has emerged as a challenging and consequential testbed for digital embodied intelligence.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Rather than relying solely on model scaling, we develop a joint data and environment centric scaling framework to address the key bottlenecks of mobile interaction.

**证据证明什么。** We also introduce a progressive training recipe consisting of mid-training, supervised fine-tuning, and reinforcement learning with task-specific reward designs.

**证据没有证明什么。** 7 Conclusion and Future Work HyMobileAgent reaches the level of substantially larger general-purpose models on AndroidWorld and on the in-house HyMobileWorld while remaining at A3B parameter scale. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14548v1#S3 — 3 Model Design; https://arxiv.org/html/2607.14548v1#S2.SS1 — 2.1 Vision-Native Models for GUI Control。Evaluation：https://arxiv.org/html/2607.14548v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.14548v1#S6.SS1 — 6.1 Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.14548v1#S7 — 7 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3.6-35B-A3B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：7 Conclusion and Future Work HyMobileAgent reaches the level of substantially larger general-purpose models on AndroidWorld and on the in-house HyMobileWorld while remaining at A3B parameter scale.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14548:end -->

<!-- review:SF-2026-ARXIV-2607-14568:start -->
### A Modern Multimodal Assistant on a 6 GB 2011 GPU: Stage-Validated, All-GPU CUDA Inference for Fermi

<!-- claim:SF-2026-ARXIV-2607-14568:start -->A companion study ran a 35B mixture-of-experts model on a 2011 NVIDIA Tesla C2075 (Fermi, sm_20, 6GB) as a GPU-prefill/CPU-decode hybrid, because the 4-bit model did not fit in device memory (arXiv:2606.24031). This report keeps the hardware and asks what a model that fits can do: we deploy MiniCPM-V-4.6, a modern multimodal assistant pairing a SigLIP2 vision encoder and window-attention merger (16x visual token compression) with a compact hybrid gated-delta-net backbone, entirely on the GPU. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14568:end -->

**为什么进入候选分母。** 摘要首要问题为“A companion study ran a 35B mixture-of-experts model on a 2011 NVIDIA Tesla C2075 (Fermi, sm_20, 6GB) as a GPU-prefill/CPU-decode hybrid, because the 4-bit model did not fit in device memory (arXiv:2606.24031).”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** The system answers an image question end-to-end in 1.7s.

**证据证明什么。** The system answers an image question end-to-end in 1.7s.

**证据没有证明什么。** The methodological refrain of this series held throughout, twice in new forms: a benchmark is only as honest as its longest tier, and an index computation with reachable exact ties cannot be reimplemented, only invoked. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14568v1#S2.SS2 — 2.2 The model。Evaluation：https://arxiv.org/html/2607.14568v1#S7 — 7 Evaluation Summary。Limitations / counterevidence：https://arxiv.org/html/2607.14568v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/openbmb/MiniCPM-V-4.6, https://github.com/karpathy/llama2.c, https://github.com/ggml-org/llama.cpp; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The methodological refrain of this series held throughout, twice in new forms: a benchmark is only as honest as its longest tier, and an index computation with reachable exact ties cannot be reimplemented, only invoked.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14568:end -->

<!-- review:SF-2026-ARXIV-2607-14570:start -->
### Democratizing Agent Deployment Safety: A Structural Monitoring Approach

<!-- claim:SF-2026-ARXIV-2607-14570:start -->AI software development agents are increasingly capable of modifying infrastructure and security critical systems, creating risks where an agent completes its assigned task while covertly weakening safeguards through actions such as broadening permissions, degrading logging, or introducing persistence mechanisms. While frontier laboratories may deploy sophisticated monitoring pipelines, many organizations and individual users adopting coding agents lack the resources and governance maturity required to maintain complex learned monitor ensembles. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14570:end -->

**为什么进入候选分母。** 摘要首要问题为“AI software development agents are increasingly capable of modifying infrastructure and security critical systems, creating risks where an agent completes its assigned task while covertly weakening safeguards through actions such as broadening permissions, degrading logging, or introducing persistence mechanisms.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce an Information Flow Graph (IFG) monitor that analyzes structural security regressions using control-flow and data-flow graph diffs alongside raw code diffs.

**证据证明什么。** In asynchronous evaluation, an untrained git diff monitor misses 11.6% attacks at 1% false positive rate auditing budget, our untrained IFG monitor reduces this to 3.5%, and the trained Async RF monitor achieves below 1%.

**证据没有证明什么。** The limitations are equally specific, for example IFG cannot see attacks whose realized payload is delivered outside the CDK or the code source diff in general. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14570v1#A2.SS1 — B.1 System Prompt; https://arxiv.org/html/2607.14570v1#S3 — 3 Experiment Design。Evaluation：https://arxiv.org/html/2607.14570v1#A1 — Appendix A Evaluation Scope: Excluding the check_in_cdk_out_directory Side Task; https://arxiv.org/html/2607.14570v1#S3 — 3 Experiment Design。Limitations / counterevidence：https://arxiv.org/html/2607.14570v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14570v1#S5.SS1 — 5.1 Technical Strengths and limitations。

**Artifact boundary。** Exact v1 links https://github.com/Agentic-AI-Risk-Mitigation/ifg-monitor, https://github.com/UKGovernmentBEIS/control-arena, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The limitations are equally specific, for example IFG cannot see attacks whose realized payload is delivered outside the CDK or the code source diff in general.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-MONITORING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14570:end -->

<!-- review:SF-2026-ARXIV-2607-14573:start -->
### Alipay-PIBench: A Realistic Payment Integration Benchmark for Coding Agents

<!-- claim:SF-2026-ARXIV-2607-14573:start -->Payment integration is a demanding repository-level software task: agents must select a suitable product, implement coordinated client-server flows, verify payment outcomes, and preserve consistency between transaction and business states. We introduce Alipay-PIBench, a benchmark for evaluating coding agents on realistic Alipay payment integration. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14573:end -->

**为什么进入候选分母。** 摘要首要问题为“Payment integration is a demanding repository-level software task: agents must select a suitable product, implement coordinated client-server flows, verify payment outcomes, and preserve consistency between transaction and business states.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Alipay-PIBench, a benchmark for evaluating coding agents on realistic Alipay payment integration.

**证据证明什么。** Method-level results distinguish source-level completion, executable payment behavior, and payment-domain requirements.

**证据没有证明什么。** Future work can extend the benchmark with additional models and agent frameworks, broader repository coverage, and longer-horizon executable payment workflows, allowing the robustness of these findings to be examined across a wider range of settings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14573v1#S4.SS4 — 4.4 RQ3: Evaluation-Method Diagnostics; https://arxiv.org/html/2607.14573v1#S4.SS2 — 4.2 RQ1: Model Capability。Evaluation：https://arxiv.org/html/2607.14573v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.14573v1#S3.SS1 — 3.1 Benchmark Composition。Limitations / counterevidence：https://arxiv.org/html/2607.14573v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/inclusionAI/PIBench, https://github.com/aelassas/bookcars, https://www.endorlabs.com/research/ai-code-security-benchmark; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work can extend the benchmark with additional models and agent frameworks, broader repository coverage, and longer-horizon executable payment workflows, allowing the robustness of these findings to be examined across a wider range of settings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14573:end -->

<!-- review:SF-2026-ARXIV-2607-14611:start -->
### Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems

<!-- claim:SF-2026-ARXIV-2607-14611:start -->A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases. While this makes agents more useful and self-improving, it also creates a new attack surface for prompt injections in which malicious instructions can be embedded within persistent files and influence future behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14611:end -->

**为什么进入候选分母。** 摘要首要问题为“A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this work, we study prompt injection attacks in memory-based agentic systems using a sandboxed synthetic workspace.

**证据证明什么。** Our results show that although it is difficult to make an agent overwrite its own memory files using untrusted external content, payloads already planted in those files can successfully attack current and future sessions.

**证据没有证明什么。** Systems could also separate memory into policy tiers, so that low-trust knowledge files can provide facts but cannot override safety rules or global behavioral constraints. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14611v1#S3 — 3. Methods; https://arxiv.org/html/2607.14611v1#S3.SS1 — 3.1. Threat Model and Scope。Evaluation：https://arxiv.org/html/2607.14611v1#S2.SS2 — 2.2. Benchmarks for Agent Security; https://arxiv.org/html/2607.14611v1#S3.SS3 — 3.3. Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.14611v1#S3.SS1 — 3.1. Threat Model and Scope; https://arxiv.org/html/2607.14611v1#S5 — 5. Discussion。

**Artifact boundary。** Exact v1 links https://docs.anthropic.com/en/docs/claude-code/memory, https://developers.openai.com/codex/guides/agents-md, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Systems could also separate memory into policy tiers, so that low-trust knowledge files can provide facts but cannot override safety rules or global behavioral constraints.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14611:end -->

<!-- review:SF-2026-ARXIV-2607-14618:start -->
### PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference

<!-- claim:SF-2026-ARXIV-2607-14618:start -->CPUs are the most universal target for on-device LLM inference, but existing low-bit quantization methods offer either coarse operating points or fine-grained mixed precision that is difficult to execute efficiently on CPUs. We present PolyQ, a CPU-oriented compiler/quantization co-design for activation-aware channel-wise bit allocation under a user-specified average-bit budget. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14618:end -->

**为什么进入候选分母。** 摘要首要问题为“CPUs are the most universal target for on-device LLM inference, but existing low-bit quantization methods offer either coarse operating points or fine-grained mixed precision that is difficult to execute efficiently on CPUs.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** This turns fine-grained budget fitting into a practical fractional-bit deployment method for CPU-only inference.

**证据证明什么。** These results show that fractional-bit CPU deployment is practical, predictable, and energy-efficient across diverse edge targets.

**证据没有证明什么。** The broader lesson is that low-bit LLM efficiency on CPUs is not only a quantizer problem, but a quantizer–compiler co-design problem. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14618v1#S3 — 3. Poly-Precision Quantization Method; https://arxiv.org/html/2607.14618v1#S4 — 4. Model Compiler Architecture。Evaluation：https://arxiv.org/html/2607.14618v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.14618v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.14618v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The broader lesson is that low-bit LLM efficiency on CPUs is not only a quantizer problem, but a quantizer–compiler co-design problem.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14618:end -->

<!-- review:SF-2026-ARXIV-2607-14635:start -->
### Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-14635:start -->Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14635:end -->

**为什么进入候选分母。** 摘要首要问题为“Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address this tension, we introduce Action QFormer, a query-based action-facing interface that uses instruction-conditioned queries to reorganize inherited multimodal information into action-facing representations before downstream action generation.

**证据证明什么。** Further analyses show that Action QFormer changes how action supervision shapes inherited multimodal representations, reducing broad upstream rewriting while preserving targeted and sometimes constructive action-supervised adaptation.

**证据没有证明什么。** More broadly, these results suggest that reliable embodied behavior depends not only on representation quality, but also on how multimodal information is selected, organized, and reshaped under action supervision. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14635v1#S3 — III Methodology; https://arxiv.org/html/2607.14635v1#A1.SS1 — A-A Training Pipeline and Model Comparison。Evaluation：https://arxiv.org/html/2607.14635v1#A2 — Appendix B Experiment Details; https://arxiv.org/html/2607.14635v1#A2.SS1 — B-A Probe Scenes and Evaluation Rules for Action Generation。Limitations / counterevidence：https://arxiv.org/html/2607.14635v1#S6 — VI Discussion; https://arxiv.org/html/2607.14635v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：More broadly, these results suggest that reliable embodied behavior depends not only on representation quality, but also on how multimodal information is selected, organized, and reshaped under action supervision.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14635:end -->

<!-- review:SF-2026-ARXIV-2607-14642:start -->
### MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers

<!-- claim:SF-2026-ARXIV-2607-14642:start -->As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14642:end -->

**为什么进入候选分母。** 摘要首要问题为“As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers.

**证据证明什么。** These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.

**证据没有证明什么。** However, this exclusion does not compromise the validity of our benchmark or the generalizability of our conclusions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14642v1#A4.SS3 — D.3 Implementation Details。Evaluation：https://arxiv.org/html/2607.14642v1#A4.SS2 — D.2 Reliability Analysis of Benchmark; https://arxiv.org/html/2607.14642v1#A8.SS3 — H.3 Prompts for Benchmark Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.14642v1#A3 — Appendix C Limitation and Future Work; https://arxiv.org/html/2607.14642v1#A7.SS2 — G.2 Case Study of Workflow Failure。

**Artifact boundary。** Exact v1 links https://github.com/modelcontextprotocol/specification, https://github.com/, https://github.com/punkpeye/awesome-mcp-servers; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, this exclusion does not compromise the validity of our benchmark or the generalizability of our conclusions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14642:end -->

<!-- review:SF-2026-ARXIV-2607-14647:start -->
### D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607-14647:start -->Speculative decoding accelerates large language model (LLM) inference without compromising output quality. Recent parallel drafting methods further improve single-request performance by decoupling draft length from drafting latency, enabling longer drafts and higher mean accepted tokens (MAT). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14647:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative decoding accelerates large language model (LLM) inference without compromising output quality.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present D-Cut, an adaptive pruning method that selects draft tokens jointly across the batch and concentrates the verification budget on tokens most likely to be accepted.

**证据证明什么。** Experiments on dense and mixture-of-experts (MoE) models show that, under high concurrency, D-Cut improves the average speedup from \(1.26\times\) to \(1.65\times\), restores acceleration in dense-model configurations where long-draft baselines are slower than autoregressive decoding, and achieves up to \(3.0\times\) speedup over autoregressive decoding on MoE models.

**证据没有证明什么。** A practical limitation of D-cut lies in its system integration. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14647v1#A3 — Appendix C System Implementation; https://arxiv.org/html/2607.14647v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.14647v1#A1 — Appendix A Algorithm and Analysis; https://arxiv.org/html/2607.14647v1#A4 — Appendix D Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.14647v1#S6 — 6 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/vllm-project/vllm/pull/47131, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://huggingface.co/tencent/Hy3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：A practical limitation of D-cut lies in its system integration.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14647:end -->

<!-- review:SF-2026-ARXIV-2607-14651:start -->
### MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-14651:start -->Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14651:end -->

**为什么进入候选分母。** 摘要首要问题为“Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families.

**证据证明什么。** Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation.

**证据没有证明什么。** 7 Discussion and Limitations MemPoison demonstrates that memory poisoning is not a single failure mode, but an interplay of stage-specific vulnerabilities across the memory lifecycle. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14651v1#A2 — Appendix B Experimental Design; https://arxiv.org/html/2607.14651v1#A2.SS7 — B.7 MID implementation details。Evaluation：https://arxiv.org/html/2607.14651v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.14651v1#A1.SS1 — A.1 Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.14651v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.14651v1#S3 — 3 Threat Model and Taxonomy。

**Artifact boundary。** Exact v1 links https://huggingface.co/meta-llama/Prompt-Guard-86M, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：7 Discussion and Limitations MemPoison demonstrates that memory poisoning is not a single failure mode, but an interplay of stage-specific vulnerabilities across the memory lifecycle.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14651:end -->

<!-- review:SF-2026-ARXIV-2607-14695:start -->
### Reflex: Real-Time VLA Control through Streaming Inference

<!-- claim:SF-2026-ARXIV-2607-14695:start -->Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching, forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that perception encoders are functionally independent of the denoising loop. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14695:end -->

**为什么进入候选分母。** 摘要首要问题为“Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching, forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that perception encoders are functionally independent of the denoising loop.

**证据证明什么。** We further maximize throughput through an \textit{async pipeline} that decouples visual encoding from action generation, combined with \textit{operator fusion} that reduces kernel overhead.

**证据没有证明什么。** Our results demonstrate that the “stop-think-act” cycle is not an inherent limitation of VLA models, but a system design choice solvable through co-designed algorithms and runtime optimizations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14695v1#S2.SS3 — 2.3 Design Goals; https://arxiv.org/html/2607.14695v1#S3 — 3 Method: Streaming VLA Inference。Evaluation：https://arxiv.org/html/2607.14695v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.14695v1#A4 — Appendix D Additional Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.14695v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/9yc/Reflex, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Our results demonstrate that the “stop-think-act” cycle is not an inherent limitation of VLA models, but a system design choice solvable through co-designed algorithms and runtime optimizations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14695:end -->

<!-- review:SF-2026-ARXIV-2607-14698:start -->
### Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color

<!-- claim:SF-2026-ARXIV-2607-14698:start -->Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14698:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this, we propose ChromaGuard, a chroma-preserving adversarial training method.

**证据证明什么。** On a physical 6-DoF robotic platform, we demonstrate that ChromaGuard achieves 97.5% and 92.5% success rates in benign and attacked color-dependent tasks, respectively.

**证据没有证明什么。** However, they cannot dynamically change the light once deployed; the parameters remain fixed across all evaluation episodes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14698v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14698v1#S3.SS2 — 3.2 FLARE Framework: Optimized Physical Spotlight Attack。Evaluation：https://arxiv.org/html/2607.14698v1#S4 — 4 Simulator Experiments: Exposing Vulnerability against Spotlight Attack; https://arxiv.org/html/2607.14698v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.14698v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.14698v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/TheRobotStudio/SO-ARM100, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, they cannot dynamically change the light once deployed; the parameters remain fixed across all evaluation episodes.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14698:end -->

<!-- review:SF-2026-ARXIV-2607-14739:start -->
### FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-14739:start -->Vision-Language-Action (VLA) models have achieved impressive results in visuomotor policy learning, yet remain fundamentally reactive, mapping current observations and language to actions without explicit forward prediction of world dynamics. Existing visual foresight methods predict future visual states but lack explicit motion guidance: they show where to go but not how to get there. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14739:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models have achieved impressive results in visuomotor policy learning, yet remain fundamentally reactive, mapping current observations and language to actions without explicit forward prediction of world dynamics.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose FoMoVLA, a framework that augments VLA representations with explicit spatio-temporal supervision by jointly learning future feature foresight and sparse 2D point tracking, enhancing the continuous action policy.

**证据证明什么。** Vision-Language-Action (VLA) models have achieved impressive results in visuomotor policy learning, yet remain fundamentally reactive, mapping current observations and language to actions without explicit forward prediction of world dynamics.

**证据没有证明什么。** 3.4 Future-Conditioned Point Tracking The two aforementioned objectives, namely future feature prediction and geometric point tracking, can be optimized independently as parallel auxiliary loss terms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14739v1#A1.SS2 — A.2 Attention Mask Design; https://arxiv.org/html/2607.14739v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.14739v1#A2 — Appendix B Additional Experimental Analysis; https://arxiv.org/html/2607.14739v1#A2.SS3 — B.3 RoboCasa GR-1 Tabletop Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.14739v1#S3.SS3 — 3.3 Future Feature Prediction; https://arxiv.org/html/2607.14739v1#S3.SS4 — 3.4 Future-Conditioned Point Tracking。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：3.4 Future-Conditioned Point Tracking The two aforementioned objectives, namely future feature prediction and geometric point tracking, can be optimized independently as parallel auxiliary loss terms.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14739:end -->

<!-- review:SF-2026-ARXIV-2607-14754:start -->
### FlowGuard: From Signals to Evidence for MCP Security Detection

<!-- claim:SF-2026-ARXIV-2607-14754:start -->The Model Context Protocol (MCP) enables LLM agents to interact with external tools through metadata exchange, tool invocation, and response consumption. Existing MCP security scanners primarily reason about suspicious semantic signals rather than real execution behaviors, which can lead to unreliable risk assessment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14754:end -->

**为什么进入候选分母。** 摘要首要问题为“The Model Context Protocol (MCP) enables LLM agents to interact with external tools through metadata exchange, tool invocation, and response consumption.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present FlowGuard, an evidence-grounded MCP security detection system.

**证据证明什么。** These results show that evidence-grounded detection can assess both execution-related and semantic risks in MCP interactions.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14754v1#S3 — III Methodology; https://arxiv.org/html/2607.14754v1#S3.SS2 — III-B System Overview。Evaluation：https://arxiv.org/html/2607.14754v1#S3.SS4 — III-D Response Analysis; https://arxiv.org/html/2607.14754v1#S4 — IV Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.14754v1#S2.SS3 — II-C Threat Model; https://arxiv.org/html/2607.14754v1#S6 — VI Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14754:end -->

<!-- review:SF-2026-ARXIV-2607-14777:start -->
### SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-14777:start -->Large language models are increasingly trained as interactive agents for long-horizon tasks involving multi-turn interaction, tool use, and environment feedback. Outcome-based reinforcement learning (RL) provides a practical optimization paradigm, but its sparse trajectory-level rewards offer limited guidance on intermediate decisions, leaving a supervision gap between episode-level outcomes and token-level policy learning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14777:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly trained as interactive agents for long-horizon tasks involving multi-turn interaction, tool use, and environment feedback.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose SEED (SElf-Evolving On-Policy Distillation), a self-evolving framework that converts completed on-policy trajectories into training-time hindsight skills and distills their behavioral effect back into the policy model.

**证据证明什么。** Extensive experiments on text-based and vision-based agentic tasks show that SEED consistently improves performance and sample efficiency, exhibiting robust generalization to unseen scenarios.

**证据没有证明什么。** Another promising direction is selective analysis: the analyzer could focus on trajectories with high uncertainty, novel states, or disagreement between reward and hindsight. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14777v1#S3 — 3 Method; https://arxiv.org/html/2607.14777v1#A2.SS3 — B.3 Algorithm and Extracted Skill Examples。Evaluation：https://arxiv.org/html/2607.14777v1#S4.SS6 — 4.6 Ablation Studies and Analysis; https://arxiv.org/html/2607.14777v1#A1 — Appendix A Theoretical Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.14777v1#A5 — Appendix E Additional Discussion; https://arxiv.org/html/2607.14777v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/jinyangwu/SEED, https://huggingface.co/Jinyang23/Seed-AlfWorld-3B, https://github.com/mpSchrader/gym-sokoban; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Another promising direction is selective analysis: the analyzer could focus on trajectories with high uncertainty, novel states, or disagreement between reward and hindsight.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14777:end -->

<!-- review:SF-2026-ARXIV-2607-14811:start -->
### Is External Database Protection Static in Retrieval-Augmented Generation? Rethinking Privacy Preservation under Dynamic Queries

<!-- claim:SF-2026-ARXIV-2607-14811:start -->Retrieval-augmented generation (RAG) enhances large language models via external document retrieval, but retrieved contexts may leak sensitive information. Current privacy protection methods typically rely on a document-level static risk assumption, treating all retrieved documents as having the same privacy leakage risk. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14811:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-augmented generation (RAG) enhances large language models via external document retrieval, but retrieved contexts may leak sensitive information.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this challenge, we propose a Prompt-Aware Dynamic Hierarchical Differential Privacy framework (PA-HDP) for privacy-preserving RAG.

**证据证明什么。** Extensive experiments on benchmark datasets demonstrate that PA-HDP significantly reduces privacy leakage while maintaining high retrieval quality, achieving a better privacy-utility trade-off than prior methods.

**证据没有证明什么。** Since the subsequent privacy budget allocation only depends on the extracted entity categories and their corresponding sensitivity scores, no modification to the remaining components of PA-HDP is required. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14811v1#A0.SS4 — -D Implementation Details of Baseline Approaches; https://arxiv.org/html/2607.14811v1#A0.SS5 — -E Detailed Attack Design。Evaluation：https://arxiv.org/html/2607.14811v1#A0.SS1 — -A Missing experimental results; https://arxiv.org/html/2607.14811v1#A0.SS6 — -F Details of Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.14811v1#A0.SS10 — -J Discussions when Adapting PA-HDP to Domain-Specific Applications; https://arxiv.org/html/2607.14811v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Since the subsequent privacy budget allocation only depends on the extracted entity categories and their corresponding sensitivity scores, no modification to the remaining components of PA-HDP is required.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14811:end -->

<!-- review:SF-2026-ARXIV-2607-14817:start -->
### Evaluating Epistemic Uncertainty: Beyond OOD Detection and Active Learning

<!-- claim:SF-2026-ARXIV-2607-14817:start -->Current evaluation of epistemic uncertainty relies on tasks such as out-ofdistribution detection and active learning. However, the Bayes-optimal decision strategies for these tasks do not coincide with the scores commonly used to quantify epistemic uncertainty. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14817:end -->

**为什么进入候选分母。** 摘要首要问题为“Current evaluation of epistemic uncertainty relies on tasks such as out-ofdistribution detection and active learning.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Building on the epistemic reject-option framework, we evaluate epistemic uncertainty using its ability to identify regret, the reducible error.

**证据证明什么。** This theoretical unification exposes a weakness in recent uncertainty disentanglement literature: we demonstrate that standard correlation metrics between learned components do not necessarily predict their actual operational utility.

**证据没有证明什么。** 7 Conclusion and Limitations In this work, we addressed an evaluation misalignment in uncertainty quantification. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14817v1#A3.SS1 — C.1 Datasets and Architectures; https://arxiv.org/html/2607.14817v1#A3.SS2 — C.2 Method-Specific Training Regimes。Evaluation：https://arxiv.org/html/2607.14817v1#A4 — Appendix D Detailed Results; https://arxiv.org/html/2607.14817v1#S3.SS1 — 3.1 The evaluation disconnect: Bayesian vs. frequentist。Limitations / counterevidence：https://arxiv.org/html/2607.14817v1#S7 — 7 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Conclusion and Limitations In this work, we addressed an evaluation misalignment in uncertainty quantification.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14817:end -->

<!-- review:SF-2026-ARXIV-2607-14852:start -->
### Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-14852:start -->Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA) models should possess lifelong learning ability to learn a new task when deployed in open-world environments. However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14852:end -->

**为什么进入候选分母。** 摘要首要问题为“Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA) models should possess lifelong learning ability to learn a new task when deployed in open-world environments.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the plasticity-stability trade-off with a dual-timescale adaptation mechanism while achieving low-cost robotic deployment with a cache-efficient replay strategy.

**证据证明什么。** Finally, experiments show that LifelongVLA outperforms existing baselines, demonstrating efficient skill expansion, robust retention of learned manipulation behaviors, and reduced reliance on retraining for real-world deployment on an xArm robot.

**证据没有证明什么。** Future work could introduce paraphrased, conversational, and context-dependent instructions to evaluate language robustness. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14852v1#S4 — 4 The Proposed Model。Evaluation：https://arxiv.org/html/2607.14852v1#S5 — 5 Experiments; https://arxiv.org/html/2607.14852v1#S5.SS1 — 5.1 Main Comparison and Process-Level Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.14852v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.14852v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work could introduce paraphrased, conversational, and context-dependent instructions to evaluate language robustness.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14852:end -->

<!-- review:SF-2026-ARXIV-2607-14890:start -->
### Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control

<!-- claim:SF-2026-ARXIV-2607-14890:start -->Autonomous coding agents increasingly execute multi-step software work, but lifecycle states such as reviewed, tested, DONE, and ready-to-merge remain claims unless supported by current evidence. We present Proof-or-Stop Lifecycle Control, a method that permits lifecycle transitions only when fresh, tracked-source-state-bound, mechanically verifiable evidence satisfies the relevant gate. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14890:end -->

**为什么进入候选分母。** 摘要首要问题为“Autonomous coding agents increasingly execute multi-step software work, but lifecycle states such as reviewed, tested, DONE, and ready-to-merge remain claims unless supported by current evidence.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present Proof-or-Stop Lifecycle Control, a method that permits lifecycle transitions only when fresh, tracked-source-state-bound, mechanically verifiable evidence satisfies the relevant gate.

**证据证明什么。** In a 9,240-cell ablation, the pre-registered A4 versus A2-prime comparison reduced visible-pass/hidden-fail amplification from 31 of 1,800 injected cells under a compute-budgeted naive loop to 2 of 1,800 under the gated loop, a 1.6 percentage-point improvement in not-amplified rate with a 95 percent confidence interval of [0.8, 2.5].

**证据没有证明什么。** A related sub-study should quantify the cross-vendor review marginal-finding rate — an independent-vendor host-2 run on a random or complete story sample with systematic finding records — which the selectively-invoked deployment in § 8 cannot estimate without bias. (1b) Real-work green-but-wrong base rate: estimate how often visible acceptance passes while an independent hidden oracle fails in non-injected development work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14890v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14890v1#S2 — 2 Background and Problem。Evaluation：https://arxiv.org/html/2607.14890v1#S5.SS2 — 5.2 Reflection-loop ablation (powered: 9,240 cells)。Limitations / counterevidence：https://arxiv.org/html/2607.14890v1#S11 — 11 Threats to Validity; https://arxiv.org/html/2607.14890v1#S12 — 12 Future Work。

**Artifact boundary。** Exact v1 links https://github.com/Proof-or-Stop, https://github.com/microsoft/agent-framework, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：A related sub-study should quantify the cross-vendor review marginal-finding rate — an independent-vendor host-2 run on a random or complete story sample with systematic finding records — which the selectively-invoked deployment in § 8 cannot estimate without bias. (1b) Real-work green-but-wrong base rate: estimate how often visible acceptance passes while an independent hidden oracle fails in non-injected development work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14890:end -->

<!-- review:SF-2026-ARXIV-2607-14896:start -->
### StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows

<!-- claim:SF-2026-ARXIV-2607-14896:start -->Addressing a structural-engineering request requires more than a single answer; it requires a chain of interdependent artifacts: interpreted requirements, a computable model, validation records, solver outputs, applicable engineering checks, and a final report. Evaluations centered on question answering or script generation may therefore reward fluent outputs even when the underlying workflow is incomplete, inconsistent, or non-executable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14896:end -->

**为什么进入候选分母。** 摘要首要问题为“Addressing a structural-engineering request requires more than a single answer; it requires a chain of interdependent artifacts: interpreted requirements, a computable model, validation records, solver outputs, applicable engineering checks, and a final report.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present StructureClaw, an artifact-centered workbench in which LLM agents operate through governed engineering skills, typed tools, shared artifact state, and local analysis backends, together with StructureClaw-Bench, an executable benchmark of 150 controlled scenarios spanning standard workflows, interactive robustness, and multimodal structural-model reconstruction.

**证据证明什么。** Across nine text-agent configurations, generic-only execution passed the model-artifact check in 87.0% of retained outcomes but achieved only 22.0% E2E Success, whereas automatic StructureClaw reached 82.9%.

**证据没有证明什么。** A single end-to-end score would not distinguish these intervention points, while the marginal diagnostics and current comparator cannot establish within-trace ordering or attribute the reconstruction gap to a specific stage. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14896v1#S2.SS1 — 2.1 Generative Design & Structural LLM Systems; https://arxiv.org/html/2607.14896v1#S3 — 3 StructureClaw System。Evaluation：https://arxiv.org/html/2607.14896v1#A2 — Appendix B Benchmark Construction and Assertions; https://arxiv.org/html/2607.14896v1#A3 — Appendix C Evaluation Protocol and Metric Definitions。Limitations / counterevidence：https://arxiv.org/html/2607.14896v1#S6 — 6 Discussion; https://arxiv.org/html/2607.14896v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/structureclaw/structureclaw, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：A single end-to-end score would not distinguish these intervention points, while the marginal diagnostics and current comparator cannot establish within-trace ordering or attribute the reconstruction gap to a specific stage.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14896:end -->

<!-- review:SF-2026-ARXIV-2607-14903:start -->
### FirmPilot: Evidence-Guided Multi-Agent Environment Recovery for IoT Firmware Rehosting

<!-- claim:SF-2026-ARXIV-2607-14903:start -->Firmware rehosting executes firmware images in emulated environments such as QEMU to enable scalable dynamic analysis of Internet of Things (IoT) devices. In practice, rehosting pipelines remain fragile across diverse real-world firmware images, as reaching an externally observable execution state depends on tightly coupled artifacts spanning boot scripts, persistent configuration (e.g., NVRAM-like key-value state), and network setup. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14903:end -->

**为什么进入候选分母。** 摘要首要问题为“Firmware rehosting executes firmware images in emulated environments such as QEMU to enable scalable dynamic analysis of Internet of Things (IoT) devices.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce FirmPilot, an evidence-guided multi-agent framework for environment recovery in firmware rehosting.

**证据证明什么。** The evaluation shows that evidence- and feedback-grounded agent coordination improves rehosting success, service recovery, and downstream utility in automated firmware rehosting.

**证据没有证明什么。** V-E Threats to Validity and Mitigations Dataset scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14903v1#S4 — IV System Design; https://arxiv.org/html/2607.14903v1#S3 — III Motivation and Design Challenges。Evaluation：https://arxiv.org/html/2607.14903v1#S5 — V Experimental Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.14903v1#S2.SS2 — II-B Rehosting Failure Modes; https://arxiv.org/html/2607.14903v1#S5.SS5 — V-E Threats to Validity and Mitigations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：V-E Threats to Validity and Mitigations Dataset scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14903:end -->

<!-- review:SF-2026-ARXIV-2607-14908:start -->
### CODA: Algorithm-Hardware Co-design for Edge Video Diffusion via NMP-Enabled Compute-Cache Operator Disaggregation

<!-- claim:SF-2026-ARXIV-2607-14908:start -->Deploying Video Diffusion Models (VDMs) on edge devices is appealing for localized and privacy-preserving generation, but their iterative Transformer-based denoising remains too slow for practical local inference. Cross-Timestep Caching (CTC) has emerged as a promising direction for reducing redundant computation, reusing activations across adjacent denoising steps rather than modifying model weights, while largely preserving generation fidelity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14908:end -->

**为什么进入候选分母。** 摘要首要问题为“Deploying Video Diffusion Models (VDMs) on edge devices is appealing for localized and privacy-preserving generation, but their iterative Transformer-based denoising remains too slow for practical local inference.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Cross-Timestep Caching (CTC) has emerged as a promising direction for reducing redundant computation, reusing activations across adjacent denoising steps rather than modifying model weights, while largely preserving generation fidelity.

**证据证明什么。** Experiments show that CODA achieves up to 1.80x end-to-end speedup and 1.74x higher energy efficiency, while preserving competitive generation quality compared with a state-of-the-art caching algorithm.

**证据没有证明什么。** However, this extension would not directly port the current CODA pipeline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14908v1#S4.SS3 — 4.3. CODA Architecture and NMP Subsystem; https://arxiv.org/html/2607.14908v1#S4 — 4. CODA Design。Evaluation：https://arxiv.org/html/2607.14908v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.14908v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.14908v1#S7 — 7. Discussion and Future Work; https://arxiv.org/html/2607.14908v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NUS-HPC-AI-Lab/VideoSys, https://github.com/vipshop/cache-dit.git, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：However, this extension would not directly port the current CODA pipeline.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14908:end -->

<!-- review:SF-2026-ARXIV-2607-14952:start -->
### LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget

<!-- claim:SF-2026-ARXIV-2607-14952:start -->Long-context RL post-training is constrained by the lifetime of state and gradients, not attention cost alone. In GRPO, one multi-million-token prompt must serve old-policy and reference scoring plus multiple policy responses, while conventional autograd keeps the prompt graph and all response graphs live alongside model weights, caches, and distributed communication buffers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14952:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context RL post-training is constrained by the lifetime of state and gradients, not attention cost alone.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present LongStraw, an objective-aware, architecture-aware system for resident-state virtualization, response replay, and distributed-gradient execution.

**证据证明什么。** The two paths share one transaction contract while specializing the retained state, replay operator, and collective communication to the architecture...

**证据没有证明什么。** The same audit also identifies what did not run correctly. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14952v1#S10.SS9 — 10.9 GRPO Systems; https://arxiv.org/html/2607.14952v1#S3 — 3 Architecture Anatomy and Bottleneck Sources。Evaluation：https://arxiv.org/html/2607.14952v1#S9.SS6 — 9.6 Group Scaling Is a Scheduling Result。Limitations / counterevidence：https://arxiv.org/html/2607.14952v1#S11 — 11 Conclusion; https://arxiv.org/html/2607.14952v1#S12 — 12 Limitations and Validation Roadmap。

**Artifact boundary。** Exact v1 links https://github.com/MindLab-Research/longstraw, https://huggingface.co/Qwen/Qwen3.6-27B/blob/6a9e13bd6fc8f0983b9b99948120bc37f49c13e9/config.json, https://huggingface.co/zai-org/GLM-5.2/blob/b4734de4facf877f85769a911abafc5283eab3d9/config.json; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The same audit also identifies what did not run correctly.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14952:end -->

<!-- review:SF-2026-ARXIV-2607-14989:start -->
### OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios

<!-- claim:SF-2026-ARXIV-2607-14989:start -->Large language models are increasingly evolving from text generators into general agents capable of understanding user requests, invoking external tools, and completing complex tasks through interaction. However, existing agent benchmarks often focus on limited scenarios, tool ecosystems, or interaction formats, making it difficult to systematically characterize model capabilities across heterogeneous application settings. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14989:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly evolving from text generators into general agents capable of understanding user requests, invoking external tools, and completing complex tasks through interaction.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce OmniaBench, a benchmark for evaluating general agents across diverse scenarios with explicit state spaces.

**证据证明什么。** The resulting dataset contains 1,431 tasks, together with a challenging subset of 644 tasks designed to reduce evaluation cost and mitigate potential contamination of the full set after public release.

**证据没有证明什么。** Meta-cognitive errors constitute another 31.0%, primarily arising from insufficient reflection and premature abandonment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14989v1#S10 — 10 Persona Design; https://arxiv.org/html/2607.14989v1#S6.SS1 — 6.1 Judge Model Robustness Results。Evaluation：https://arxiv.org/html/2607.14989v1#S3.SS4 — 3.4 Evaluation; https://arxiv.org/html/2607.14989v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.14989v1#S4.SS3 — 4.3 Discussion; https://arxiv.org/html/2607.14989v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/scuuy/OmniaBench, https://github.com/SKYLENAGE-AI/QwenClawBench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Meta-cognitive errors constitute another 31.0%, primarily arising from insufficient reflection and premature abandonment.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14989:end -->

<!-- review:SF-2026-ARXIV-2607-15065:start -->
### DriftWorld: Fast World Modeling through Drifting

<!-- claim:SF-2026-ARXIV-2607-15065:start -->Predictive world models enable robots to plan by imagining the outcomes of their actions, but their value for control hinges on generating many rollouts quickly. This creates a bottleneck for diffusion-based world models: multistep sampling makes each rollout expensive, limiting large-scale action search at inference time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15065:end -->

**为什么进入候选分母。** 摘要首要问题为“Predictive world models enable robots to plan by imagining the outcomes of their actions, but their value for control hinges on generating many rollouts quickly.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce DriftWorld, an action-conditioned world model based on drifting generative models.

**证据证明什么。** These results show that drifting models are a strong fit for robot world modeling, where fast, high-quality imagination directly supports planning and policy evaluation.

**证据没有证明什么。** As a result, the number of context and generated frames per negative sample is limited by GPU VRAM. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15065v1#S3.SS4 — 3.4 Action-Conditioned Architecture; https://arxiv.org/html/2607.15065v1#A4 — Appendix D Implementation Details。Evaluation：https://arxiv.org/html/2607.15065v1#A1 — Appendix A Additional Qualitative Results; https://arxiv.org/html/2607.15065v1#A2 — Appendix B Additional Quantitative Results。Limitations / counterevidence：https://arxiv.org/html/2607.15065v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/Susie-Lu/driftworld, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：As a result, the number of context and generated frames per negative sample is limited by GPU VRAM.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15065:end -->

<!-- review:SF-2026-ARXIV-2607-15092:start -->
### Rubrics on Trial: Evolving Rubrics from a Single Query via Synthetic Pairwise Evidence

<!-- claim:SF-2026-ARXIV-2607-15092:start -->Rubrics provide structured, fine-grained signals for training and evaluating large language models (LLMs). Yet reliable query-specific rubrics are difficult to construct. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15092:end -->

**为什么进入候选分母。** 摘要首要问题为“Rubrics provide structured, fine-grained signals for training and evaluating large language models (LLMs).”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Rubrics on Trial, a query-only framework that evolves a rubric set from an empty set without external annotations or model training.

**证据证明什么。** Experiments across five preference benchmark suites demonstrate the effectiveness of Rubrics on Trial, which achieves the best average accuracy and leads on six of seven evaluation sets.

**证据没有证明什么。** 5 Conclusion In this work, we introduced Rubrics on Trial , a query-only framework that evolves a rubric set from an empty set using synthetic rubric-conditioned response pairs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15092v1#S3 — 3 Methodology; https://arxiv.org/html/2607.15092v1#S3.SS1 — 3.1 Framework overview。Evaluation：https://arxiv.org/html/2607.15092v1#S2.SS1 — 2.1 Rubric-based evaluation; https://arxiv.org/html/2607.15092v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.15092v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：5 Conclusion In this work, we introduced Rubrics on Trial , a query-only framework that evolves a rubric set from an empty set using synthetic rubric-conditioned response pairs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15092:end -->

<!-- review:SF-2026-ARXIV-2607-15115:start -->
### Don't Predict, Prioritize: Rethinking GPU Reliability Assessment

<!-- claim:SF-2026-ARXIV-2607-15115:start -->The reliability of Graphics Processing Units (GPUs) is a criticalbottleneck for modern large-scale AI infrastructure, where a sin-gle node failure can disrupt synchronous training jobs and causesignificant financial losses. While predictive maintenance is widelyused in other hardware domains, we demonstrate that accuratelypredicting the exact timing of GPU failures is inherently difficult.Through an in-depth analysis of telemetry data from a productioncluster, we find that major GPU failures, including Double Bit Er-rors (DBEs) and GPU Lost events, exhibit strong stochasticity andlow signal-to-noise ratios in time-series telemetry, which makesconventional time-based prediction ineffective. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15115:end -->

**为什么进入候选分母。** 摘要首要问题为“The reliability of Graphics Processing Units (GPUs) is a criticalbottleneck for modern large-scale AI infrastructure, where a sin-gle node failure can disrupt synchronous training jobs and causesignificant financial losses.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In online deployment, HeaRanksuccessfully captures 64% of future failures within the top 5% ofranked nodes, compared to only 21% by the incumbent productionsystem.

**证据证明什么。** Evaluated on a production-scale cluster with thousands of GPUs, HeaRank achieves an AUCof 0.83, significantly outperforming both heuristic baselines andstate-of-the-art ranking algorithms.

**证据没有证明什么。** This change is driven not only by the fact that historical failure information is naturally suited to host-level ranking, but also because ranking better matches operational needs: knowing exactly when a node will fail is often less useful than proactively reducing the impact of failures. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15115v1#A1 — Appendix A System Architecture and Data Collection; https://arxiv.org/html/2607.15115v1#S3.SS1 — 3.1. Model Prediction Experiments。Evaluation：https://arxiv.org/html/2607.15115v1#S5.SS2 — 5.2. RQ1: Evaluation Results and Analysis; https://arxiv.org/html/2607.15115v1#A1.SS3 — A.3. Telemetry Dataset (for Predictability Analysis)。Limitations / counterevidence：https://arxiv.org/html/2607.15115v1#S3.SS3 — 3.3. The Power of Historical Failure Patterns; https://arxiv.org/html/2607.15115v1#S7 — 7. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/geotle77/kdd26-artifact, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This change is driven not only by the fact that historical failure information is naturally suited to host-level ranking, but also because ranking better matches operational needs: knowing exactly when a node will fail is often less useful than proactively reducing the impact of failures.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15115:end -->

<!-- review:SF-2026-ARXIV-2607-15143:start -->
### Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents

<!-- claim:SF-2026-ARXIV-2607-15143:start -->AI coding agents set up projects by reading documentation and installing the dependencies it lists, without verifying their names, sources, or known vulnerabilities. By editing only a README, requirements file, or Makefile, an attacker can redirect the agent to an untrusted registry, a known-vulnerable version, or a wrong-but-plausible name: documentation becomes a vector for code execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15143:end -->

**为什么进入候选分母。** 摘要首要问题为“AI coding agents set up projects by reading documentation and installing the dependencies it lists, without verifying their names, sources, or known vulnerabilities.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present the first systematic evaluation of package-install-time supply-chain attacks delivered through ordinary project-setup documentation across production coding-agent harnesses, probing frontier models on twelve scenarios in five attack classes, grounded in documented incidents.

**证据证明什么。** Security-oriented prompts recover part of the gap but only for the dimension they name; a deterministic pre-install check that verifies names, sources, and versions before any code runs closes most of it.

**证据没有证明什么。** Holding the model and attack fixed and switching only the harness moved detection from 10/10 to 9/30 ( ), and reversed direction on other attacks; conversely, some attacks (dependency confusion) split cleanly by model family across both harnesses. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15143v1#A5 — Appendix E System Prompt and Review Prompts; https://arxiv.org/html/2607.15143v1#A9 — Appendix I Pre-Install Hook Architecture。Evaluation：https://arxiv.org/html/2607.15143v1#A3 — Appendix C Experimental Setup; https://arxiv.org/html/2607.15143v1#S4 — 4 Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.15143v1#S10 — 10 Limitations and Future Directions; https://arxiv.org/html/2607.15143v1#S11 — 11 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/cardwizard/Sentinel/blob/main/evaluations/GITHUB_SEARCH_QUERIES.md, https://github.com/features/copilot, https://claude.ai/code; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Holding the model and attack fixed and switching only the harness moved detection from 10/10 to 9/30 ( ), and reversed direction on other attacks; conversely, some attacks (dependency confusion) split cleanly by model family across both harnesses.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15143:end -->

<!-- review:SF-2026-ARXIV-2607-15161:start -->
### On-Policy Delta Distillation

<!-- claim:SF-2026-ARXIV-2607-15161:start -->On-policy distillation is an alternative post-training method in reinforcement learning that alleviates the constraints imposed by reward models by providing token-level supervision from a teacher model. Although on-policy distillation has been studied and applied across various settings, its fundamental design remains underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15161:end -->

**为什么进入候选分母。** 摘要首要问题为“On-policy distillation is an alternative post-training method in reinforcement learning that alleviates the constraints imposed by reward models by providing token-level supervision from a teacher model.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this paper, we introduce a new distillation reward, termed the delta signal, instead of directly imitating the teacher's output distribution.

**证据证明什么。** Experiments across mathematics, science, and code-reasoning benchmarks demonstrate that OPD$^2$ consistently outperforms conventional on-policy distillation, enabling reasoning LLMs to achieve strong performance with only a short post-training period.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15161v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.15161v1#S3 — 3 Experiment; https://arxiv.org/html/2607.15161v1#S3.SS1 — 3.1 Experiment settings。Limitations / counterevidence：https://arxiv.org/html/2607.15161v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/naver-ai/opd2, https://huggingface.co/datasets/nvidia/OpenScienceReasoning-2, https://github.com/huggingface/trl; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15161:end -->

<!-- review:SF-2026-ARXIV-2607-15190:start -->
### Can We Trust Item Response Theory for AI Evaluation?

<!-- claim:SF-2026-ARXIV-2607-15190:start -->AI benchmarks increasingly leverage item-level statistical models, particularly item response theory (IRT), to estimate model capabilities, rank systems, select informative examples, and diagnose benchmark quality. However, AI benchmark data often departs from the data regime of human testing, for which standard IRT estimation tools were originally developed: benchmarks typically involve fewer evaluated models, far more items, and capability distributions that may be skewed, clustered, or multimodal. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15190:end -->

**为什么进入候选分母。** 摘要首要问题为“AI benchmarks increasingly leverage item-level statistical models, particularly item response theory (IRT), to estimate model capabilities, rank systems, select informative examples, and diagnose benchmark quality.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Across 18,000 simulation conditions, we systematically evaluate computational feasibility, scalability, and the reliability of IRT inferences about model rankings, predicted performance, and item characteristics.

**证据证明什么。** Results show that classical estimators can become infeasible in large benchmark settings, whereas scalable estimators can produce unreliable item-level and ranking inferences with small or non-normally distributed model sets.

**证据没有证明什么。** Although this paper only offers concrete guidance for a limited number of scenarios, we envision the simulation methods adopted here to generalize to many other scenarios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15190v1#S4 — 4 Simulation design; https://arxiv.org/html/2607.15190v1#S5.SS2 — 5.2 How do different IRT estimators recover model capabilities and rankings?。Evaluation：https://arxiv.org/html/2607.15190v1#A4 — Appendix D Detailed results for parameter recovery; https://arxiv.org/html/2607.15190v1#S3 — 3 Item response theory for AI evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.15190v1#S7 — 7 Limitations and Conclusion。

**Artifact boundary。** Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Although this paper only offers concrete guidance for a limited number of scenarios, we envision the simulation methods adopted here to generalize to many other scenarios.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15190:end -->

<!-- review:SF-2026-ARXIV-2607-15193:start -->
### Plover: Steering GUI Agents through Plan-Centric Interaction

<!-- claim:SF-2026-ARXIV-2607-15193:start -->Graphical user interface (GUI) automation remains challenging in real-world environments, where dynamic layouts, unexpected dialogs, and evolving interface states can cause autonomous agents to drift from user intent. Recent vision-based multimodal agents improve flexibility by operating directly over screenshots and natural language instructions, but planning and adaptation often remain internal, limiting users' ability to inspect, supervise, or correct system behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15193:end -->

**为什么进入候选分母。** 摘要首要问题为“Graphical user interface (GUI) automation remains challenging in real-world environments, where dynamic layouts, unexpected dialogs, and evolving interface states can cause autonomous agents to drift from user intent.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present Plover, a plan-centric vision-based GUI automation system that externalizes task plans and replanning as persistent, inspectable, and revisable artifacts.

**证据证明什么。** Our results show that many autonomous GUI-agent failures are structurally repairable when plans remain visible and interventions are localized, and that explicit replanning helps make GUI automation more transparent, controllable, and adaptable.

**证据没有证明什么。** Mixed-initiative interaction improved 23 of 26 autonomous non-success cases, converting 17 to complete success and 6 to partial success (completing subtasks but not the goal), with only 3 remaining failures (Table 1 ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15193v1#A4.SS2 — D.2. Executor System Prompt Design; https://arxiv.org/html/2607.15193v1#A3 — Appendix C System-Driven IR Details。Evaluation：https://arxiv.org/html/2607.15193v1#S5.SS1 — 5.1. Benchmark Failure-Case Repair Analysis; https://arxiv.org/html/2607.15193v1#A2 — Appendix B Formative Study User Experience Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.15193v1#A5.SS1 — E.1. Failure Analysis; https://arxiv.org/html/2607.15193v1#S5.SS1 — 5.1. Benchmark Failure-Case Repair Analysis。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Mixed-initiative interaction improved 23 of 26 autonomous non-success cases, converting 17 to complete success and 6 to partial success (completing subtasks but not the goal), with only 3 remaining failures (Table 1 ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15193:end -->

<!-- review:SF-2026-ARXIV-2607-15205:start -->
### MM-IssueLoc: A Controlled Benchmark for Evaluating Visual Evidence in Multimodal Repository-Level Issue Localization

<!-- claim:SF-2026-ARXIV-2607-15205:start -->Real repository issues routinely include visual evidence such as screenshots, error dialogs, rendered UI states, and logs, yet repository-level issue localization is evaluated mostly as a text-only task. Existing multimodal SE benchmarks evaluate end-to-end repair, entangling localization with patch synthesis and obscuring whether visual input helped, hurt, or was ignored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15205:end -->

**为什么进入候选分母。** 摘要首要问题为“Real repository issues routinely include visual evidence such as screenshots, error dialogs, rendered UI states, and logs, yet repository-level issue localization is evaluated mostly as a text-only task.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We evaluate LLM-based and retrieval-based systems, including MM-IssueLoc-VL-Emb as a controlled multimodal retriever.

**证据证明什么。** Results show that existing systems remain far from reliable multimodal repository localization: the strongest agent reaches 38.96 file Acc@5 and 22.45 function Acc@10, while the strongest retriever reaches 33.86 function Acc@10.

**证据没有证明什么。** By pairing real issue-PR instances with file-level and function-level gold labels, image-category and relevance annotations, and controlled text-only, with-image, VCE, and VCE+image modes, MM-IssueLoc makes visual evidence an explicit evaluation variable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15205v1#S5.SS1 — 5.1 RQ1: How Well Do Current Systems Localize Multimodal Repository Issues?; https://arxiv.org/html/2607.15205v1#S5.SS2 — 5.2 RQ2: Is Visual Evidence Useful, and Do Systems Use It Reliably?。Evaluation：https://arxiv.org/html/2607.15205v1#A2.SS4 — B.4 Cross-benchmark Localization Results; https://arxiv.org/html/2607.15205v1#S5 — 5 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.15205v1#S6 — 6 Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.15205v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Jasaxion/MM-IssueLoc-Bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：By pairing real issue-PR instances with file-level and function-level gold labels, image-category and relevance annotations, and controlled text-only, with-image, VCE, and VCE+image modes, MM-IssueLoc makes visual evidence an explicit evaluation variable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15205:end -->

<!-- review:SF-2026-ARXIV-2607-15207:start -->
### BadWAM: When World-Action Models Dream Right but Act Wrong

<!-- claim:SF-2026-ARXIV-2607-15207:start -->World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world prediction. This coupling is often viewed as a source of robustness, interpretability, and safety, as a robot's action can in principle be checked against its imagined future. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15207:end -->

**为什么进入候选分母。** 摘要首要问题为“World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world prediction.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce BadWAM, a unified framework for modeling and evaluating World-Action Drift Attacks: a new class of WAM-specific adversarial attacks that use small visual perturbations to break the alignment between what a WAM imagines and what it executes.

**证据证明什么。** Results show that our attacks substantially reduce task success rates under closed-loop execution.

**证据没有证明什么。** The main message is that WAMs are not protected simply because action generation is coupled with future prediction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15207v1#S2.SS2 — 2.2 Attacks against Embodied AI Systems; https://arxiv.org/html/2607.15207v1#S4.SS1 — 4.1 Design Motivation。Evaluation：https://arxiv.org/html/2607.15207v1#A1 — Appendix A Details of Experiment Setup; https://arxiv.org/html/2607.15207v1#A1.SS1 — A.1 Full and Subset Evaluation Protocols。Limitations / counterevidence：https://arxiv.org/html/2607.15207v1#S3 — 3 Threat Model; https://arxiv.org/html/2607.15207v1#S5.SS2 — 5.2 BadWAM Reliably Induces Task Failures。

**Artifact boundary。** Exact v1 links https://github.com/LiQiiiii/BadWAM, https://huggingface.co/collections/LIQIIIII/badwam, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The main message is that WAMs are not protected simply because action generation is coupled with future prediction.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15207:end -->

<!-- review:SF-2026-ARXIV-2607-15253:start -->
### Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search

<!-- claim:SF-2026-ARXIV-2607-15253:start -->Retrieval systems are trained and evaluated on a static idea of usefulness: hand a document and a question to a reader model, see whether the answer improves, and score the document accordingly. The idea holds up when a document is read on its own. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15253:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval systems are trained and evaluated on a static idea of usefulness: hand a document and a question to a reader model, see whether the answer improves, and score the document accordingly.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Retrieval systems are trained and evaluated on a static idea of usefulness: hand a document and a question to a reader model, see whether the answer improves, and score the document accordingly.

**证据证明什么。** Retrieval systems are trained and evaluated on a static idea of usefulness: hand a document and a question to a reader model, see whether the answer improves, and score the document accordingly.

**证据没有证明什么。** The reader based static axis turned out to be badly skewed, with only 3.30% of documents scoring above zero, which means the headline bridge percentage largely restates the independence result rather than confirming it separately. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15253v1#A1.SS1 — A.1. Agent system prompt; https://arxiv.org/html/2607.15253v1#S2 — 2. Methodology。Evaluation：https://arxiv.org/html/2607.15253v1#S3 — 3. Results and Analysis; https://arxiv.org/html/2607.15253v1#S2.SS3 — 2.3. Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.15253v1#S3.SS6 — 3.6. Threats to validity; https://arxiv.org/html/2607.15253v1#S4 — 4. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The reader based static axis turned out to be badly skewed, with only 3.30% of documents scoring above zero, which means the headline bridge percentage largely restates the independence result rather than confirming it separately.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15253:end -->

<!-- review:SF-2026-ARXIV-2607-15257:start -->
### SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration

<!-- claim:SF-2026-ARXIV-2607-15257:start -->Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents. However, as interaction histories grow, agents increasingly struggle to track task progress. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15257:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce SearchOS, a system-level multi-agent framework that turns fragile, implicit search progress into explicit, persistent, and shared state.

**证据证明什么。** Built on SOCM, SearchOS applies a pipeline-parallel scheduling mechanism that overlaps the execution of sub-agents and continuously refills freed slots with tasks targeting unresolved coverage gaps to improve utilization and throughput.

**证据没有证明什么。** Pipeline-parallel orchestration dispatches unresolved gaps, while our Search Tool Middleware Harness prepares context, grounds observations, and handles stalls and budget limits. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15257v1#S6.SS2 — 6.2 Multi-Agent Orchestration Systems; https://arxiv.org/html/2607.15257v1#A3 — Appendix C Implementation Reference。Evaluation：https://arxiv.org/html/2607.15257v1#S5 — 5 Ablations & Analysis; https://arxiv.org/html/2607.15257v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.15257v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/antins-labs/SearchOS, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Pipeline-parallel orchestration dispatches unresolved gaps, while our Search Tool Middleware Harness prepares context, grounds observations, and handles stalls and budget limits.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15257:end -->

<!-- review:SF-2026-ARXIV-2607-15263:start -->
### Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents

<!-- claim:SF-2026-ARXIV-2607-15263:start -->Security-agent evaluations commonly measure peak offensive capability under generous inference budgets, emphasizing vulnerability discovery, exploit development, penetration testing, and CTF completion. Such measurements are useful but incomplete: in operational security, every reasoning step, tool call, telemetry query, and enrichment request consumes budget. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-15263:end -->

**为什么进入候选分母。** 摘要首要问题为“Security-agent evaluations commonly measure peak offensive capability under generous inference budgets, emphasizing vulnerability discovery, exploit development, penetration testing, and CTF completion.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present an interactive website with our results https://evals.frontier.security.

**证据证明什么。** Our results show distinct scalingregimes for red- and blue-team tasks.

**证据没有证明什么。** Comparable multi-model results for these later versions are not yet available, so extending the same cost-aware analysis to BOTS v2 and v3 is future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.15263v1#A2 — Appendix B Uncertainty Method; https://arxiv.org/html/2607.15263v1#S3 — 3 Evaluation Design。Evaluation：https://arxiv.org/html/2607.15263v1#S4 — 4 Evaluation Results; https://arxiv.org/html/2607.15263v1#A1 — Appendix A Evaluation Run Dates。Limitations / counterevidence：https://arxiv.org/html/2607.15263v1#S7 — 7 Limitations; https://arxiv.org/html/2607.15263v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/splunk/botsv1, https://github.com/splunk/botsv2, https://github.com/splunk/botsv3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Comparable multi-model results for these later versions are not yet available, so extending the same cost-aware analysis to BOTS v2 and v3 is future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-15263:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14107 | score_7_9 | selected | DA-20260717-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260717-01 |
| SF-2026-ARXIV-2607-14145 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14145 |
| SF-2026-ARXIV-2607-14166 | score_7_9 | selected | DA-20260717-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260717-02 |
| SF-2026-ARXIV-2607-14236 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14236 |
| SF-2026-ARXIV-2607-14280 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14280 |
| SF-2026-ARXIV-2607-14340 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14340 |
| SF-2026-ARXIV-2607-14396 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14396 |
| SF-2026-ARXIV-2607-14431 | score_7_9 | selected | DA-20260717-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260717-03 |
| SF-2026-ARXIV-2607-14493 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14493 |
| SF-2026-ARXIV-2607-14541 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14541 |
| SF-2026-ARXIV-2607-14570 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14570 |
| SF-2026-ARXIV-2607-14611 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14611 |
| SF-2026-ARXIV-2607-14618 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14618 |
| SF-2026-ARXIV-2607-14647 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14647 |
| SF-2026-ARXIV-2607-14651 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14651 |
| SF-2026-ARXIV-2607-14695 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14695 |
| SF-2026-ARXIV-2607-14739 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14739 |
| SF-2026-ARXIV-2607-14777 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14777 |
| SF-2026-ARXIV-2607-14852 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14852 |
| SF-2026-ARXIV-2607-14890 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14890 |
| SF-2026-ARXIV-2607-14908 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14908 |
| SF-2026-ARXIV-2607-14952 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14952 |
| SF-2026-ARXIV-2607-15143 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15143 |
| SF-2026-ARXIV-2607-15161 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15161 |
| SF-2026-ARXIV-2607-15207 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15207 |
| SF-2026-ARXIV-2607-15257 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15257 |
| SF-2026-ARXIV-2607-15263 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-15263 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-14145:start -->
`SF-2026-ARXIV-2607-14145` 的 exact-v1 Deep Review 已保留。其机制为：To scale this insight, we propose ToolAnchor, a framework that uses teacher models to hypothesize these counterfactual contexts, verifies them via student rollouts, and internalizes the successful interventions through agentic post-training. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14145:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14236:start -->
`SF-2026-ARXIV-2607-14236` 的 exact-v1 Deep Review 已保留。其机制为：We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14236:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14280:start -->
`SF-2026-ARXIV-2607-14280` 的 exact-v1 Deep Review 已保留。其机制为：Representation steering is a well-established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14280:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14340:start -->
`SF-2026-ARXIV-2607-14340` 的 exact-v1 Deep Review 已保留。其机制为：In our approach, the prover is the judge of whether the code is correct. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14340:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14396:start -->
`SF-2026-ARXIV-2607-14396` 的 exact-v1 Deep Review 已保留。其机制为：We introduce \texttt{CatalogAgent}, a novel agentic system that continuously improves Generator and Evaluator models for e-commerce catalog enrichment. 为避免挤压 `AGENT-REFLECTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14396:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14493:start -->
`SF-2026-ARXIV-2607-14493` 的 exact-v1 Deep Review 已保留。其机制为：We present LogInject, a systematic framework for evaluating these threats. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14493:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14541:start -->
`SF-2026-ARXIV-2607-14541` 的 exact-v1 Deep Review 已保留。其机制为：We present Atrex-Bench, a benchmark whose 30 operators and 440 shapes are sampled directly from full-cluster production inference traces of compute-limited, memory-rich GPUs. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14541:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14570:start -->
`SF-2026-ARXIV-2607-14570` 的 exact-v1 Deep Review 已保留。其机制为：We introduce an Information Flow Graph (IFG) monitor that analyzes structural security regressions using control-flow and data-flow graph diffs alongside raw code diffs. 为避免挤压 `PLATFORM-MONITORING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14570:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14611:start -->
`SF-2026-ARXIV-2607-14611` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we study prompt injection attacks in memory-based agentic systems using a sandboxed synthetic workspace. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14611:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14618:start -->
`SF-2026-ARXIV-2607-14618` 的 exact-v1 Deep Review 已保留。其机制为：This turns fine-grained budget fitting into a practical fractional-bit deployment method for CPU-only inference. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14618:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14647:start -->
`SF-2026-ARXIV-2607-14647` 的 exact-v1 Deep Review 已保留。其机制为：We present D-Cut, an adaptive pruning method that selects draft tokens jointly across the batch and concentrates the verification budget on tokens most likely to be accepted. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14647:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14651:start -->
`SF-2026-ARXIV-2607-14651` 的 exact-v1 Deep Review 已保留。其机制为：To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14651:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14695:start -->
`SF-2026-ARXIV-2607-14695` 的 exact-v1 Deep Review 已保留。其机制为：We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that perception encoders are functionally independent of the denoising loop. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14695:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14739:start -->
`SF-2026-ARXIV-2607-14739` 的 exact-v1 Deep Review 已保留。其机制为：We propose FoMoVLA, a framework that augments VLA representations with explicit spatio-temporal supervision by jointly learning future feature foresight and sparse 2D point tracking, enhancing the continuous action policy. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14739:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14777:start -->
`SF-2026-ARXIV-2607-14777` 的 exact-v1 Deep Review 已保留。其机制为：We propose SEED (SElf-Evolving On-Policy Distillation), a self-evolving framework that converts completed on-policy trajectories into training-time hindsight skills and distills their behavioral effect back into the policy model. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14777:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14852:start -->
`SF-2026-ARXIV-2607-14852` 的 exact-v1 Deep Review 已保留。其机制为：To address this fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the plasticity-stability trade-off with a dual-timescale adaptation mechanism while achieving low-cost robotic deployment with a cache-efficient replay strategy. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14852:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14890:start -->
`SF-2026-ARXIV-2607-14890` 的 exact-v1 Deep Review 已保留。其机制为：We present Proof-or-Stop Lifecycle Control, a method that permits lifecycle transitions only when fresh, tracked-source-state-bound, mechanically verifiable evidence satisfies the relevant gate. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14890:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14908:start -->
`SF-2026-ARXIV-2607-14908` 的 exact-v1 Deep Review 已保留。其机制为：Cross-Timestep Caching (CTC) has emerged as a promising direction for reducing redundant computation, reusing activations across adjacent denoising steps rather than modifying model weights, while largely preserving generation fidelity. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14908:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14952:start -->
`SF-2026-ARXIV-2607-14952` 的 exact-v1 Deep Review 已保留。其机制为：We present LongStraw, an objective-aware, architecture-aware system for resident-state virtualization, response replay, and distributed-gradient execution. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14952:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15143:start -->
`SF-2026-ARXIV-2607-15143` 的 exact-v1 Deep Review 已保留。其机制为：We present the first systematic evaluation of package-install-time supply-chain attacks delivered through ordinary project-setup documentation across production coding-agent harnesses, probing frontier models on twelve scenarios in five attack classes, grounded in documented incidents. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15143:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15161:start -->
`SF-2026-ARXIV-2607-15161` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we introduce a new distillation reward, termed the delta signal, instead of directly imitating the teacher's output distribution. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15161:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15207:start -->
`SF-2026-ARXIV-2607-15207` 的 exact-v1 Deep Review 已保留。其机制为：We introduce BadWAM, a unified framework for modeling and evaluating World-Action Drift Attacks: a new class of WAM-specific adversarial attacks that use small visual perturbations to break the alignment between what a WAM imagines and what it executes. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15207:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15257:start -->
`SF-2026-ARXIV-2607-15257` 的 exact-v1 Deep Review 已保留。其机制为：We introduce SearchOS, a system-level multi-agent framework that turns fragile, implicit search progress into explicit, persistent, and shared state. 为避免挤压 `AGENT-MULTI-AGENT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15257:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15263:start -->
`SF-2026-ARXIV-2607-15263` 的 exact-v1 Deep Review 已保留。其机制为：We present an interactive website with our results https://evals.frontier.security. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-15263:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260717-01:start -->
### Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs

**约束变化与机制。** This insight motivates Polestar, a training-free inference framework that uses token representation drift as a unified signal to jointly address both challenges.

**证明与未证明。** Across mathematics and coding benchmarks on several dLLM families, Polestar sets a new state of the art on the accuracy-throughput Pareto frontier, achieving up to 10.73% accuracy improvement, up to 3.7x higher throughput, and high decoding parallelism of 3.67 tokens per forward pass over existing baselines. 但 For (c,d) star marks the default Polestar setting, and text annotations indicate TPF. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：For (c,d) star marks the default Polestar setting, and text annotations indicate TPF. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-14107`。
<!-- analysis:DA-20260717-01:end -->

<!-- analysis:DA-20260717-02:start -->
### Stop Means Stop: Measuring and Repairing the Enforcement Gap in Agent-Framework Control Primitives

**约束变化与机制。** This contract holds on none of six widely used open-source frameworks.

**证明与未证明。** Under that contract SOUNDGATE blocks every measured violation on all six frameworks while releasing legitimate effects: gated tau-bench episodes complete with zero refusals at ~1 ms per write, and durable admission sustains ~12k admissions per second. 但 Model-free differential probes isolate a recurringsibling leak—an approval gate suspends its own branch while a sibling branch’s effect executesduring the pause, so a subsequent rejection cannot prevent it—in every evaluated framework that ships a pre-execution gate (five of six, spanning four execution models and two language runtimes; the sixth ships post-hoc review only), and confirm three further gaps on current releases: replay double-execution, cancellation orphans, and timeout zombies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Model-free differential probes isolate a recurringsibling leak—an approval gate suspends its own branch while a sibling branch’s effect executesduring the pause, so a subsequent rejection cannot prevent it—in every evaluated framework that ships a pre-execution gate (five of six, spanning four execution models and two language runtimes; the sixth ships post-hoc review only), and confirm three further gaps on current releases: replay double-execution, cancellation orphans, and timeout zombies. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-14166`。
<!-- analysis:DA-20260717-02:end -->

<!-- analysis:DA-20260717-03:start -->
### Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel

**约束变化与机制。** We describe the system at the behavior level; the engine is proprietary, and every reported number is backed by committed input and output hashes so the scoring can be re-checked without it.

**证明与未证明。** We show that own-position graft is the unique numerically exact operating point on a model with floating-point rotary encoding, and we verify byte-exactness on two model scales (12B, 31B) and two GPU targets, one through a pre-registered replay. 但 Composition is byte-exact only against a chunked reference, not a monolithic one, though it is functionally correct in sequence (Section 4.8). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Composition is byte-exact only against a chunked reference, not a monolithic one, though it is functionally correct in sequence (Section 4.8). 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-14431`。
<!-- analysis:DA-20260717-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260717-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260717 | GAP-20260717-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260717-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260717-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260717-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260717-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260717-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260717-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

429 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：34
- `incremental_method_without_durable_system_delta`：324
- `local_benchmark_without_release_delta`：12
- `prior_retained_candidate`：2
- `theory_without_ai_system_contract`：11
- `vertical_application_without_system_delta`：46

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 25、No Change 51、Structural 1；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/17/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Latent Communication Between Language Model Agents: Channels, Alignment, and the Limits of Text](https://arxiv.org/html/2607.14103v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs](https://arxiv.org/html/2607.14107v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Eta Given Delta: Defining LLM Tool Efficiency With Marginal Tool Utility](https://arxiv.org/html/2607.14108v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Simplicity Paradox: Debunking myths about prompting and datasets for LLM evaluation](https://arxiv.org/html/2607.14109v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability](https://arxiv.org/html/2607.14145v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Beyond Object Validation: Relational Conformance in Multi-Artifact Agent Releases](https://arxiv.org/html/2607.14155v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Certified Domain Consistency for Multi-Domain Retrieval: Label-Free Per-Domain Contamination Control with Conformal Risk Guarantees](https://arxiv.org/html/2607.14157v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [MemoHarness: Agent Harnesses That Learn from Experience](https://arxiv.org/html/2607.14159v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Stop Means Stop: Measuring and Repairing the Enforcement Gap in Agent-Framework Control Primitives](https://arxiv.org/pdf/2607.14166v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Structured Feedback Improves Repair in an LLM Agent Loop](https://arxiv.org/html/2607.14167v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models](https://arxiv.org/html/2607.14169v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning](https://arxiv.org/html/2607.14171v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [RENEW: Towards Learning World Models and Repairing Model Exploitation from Preferences](https://arxiv.org/html/2607.14180v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs](https://arxiv.org/html/2607.14186v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation](https://arxiv.org/html/2607.14189v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Inference-Time Concept Suppression and Video-Centric Evaluation for Text-to-Video Models](https://arxiv.org/html/2607.14194v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned Video Generation](https://arxiv.org/html/2607.14202v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection](https://arxiv.org/html/2607.14236v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](https://arxiv.org/html/2607.14252v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [AI Agents Do Not Fail Alone:The Context Fails First](https://arxiv.org/html/2607.14275v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making](https://arxiv.org/html/2607.14277v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [DiMaS: Distribution Matching for Steering Vision-Language-Action Models](https://arxiv.org/pdf/2607.14280v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [ToolAlignBench: Investigating Alignment Conflicts in Tool-Calling Enabled LLMs](https://arxiv.org/html/2607.14285v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [PReM: Learning What to Preserve and When to Refresh for Context Compression](https://arxiv.org/html/2607.14327v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Copy-on-Write Scoring: Application-Specific Agent Evaluations](https://arxiv.org/html/2607.14336v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [The Prover Is the Judge: Verified Security Software from AI Coding Agents in Ada/SPARK](https://arxiv.org/html/2607.14340v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [CIPHER: A Decoupled Exploration-Selection Framework for Test-Time Scaling of Data Science Agents](https://arxiv.org/html/2607.14386v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Why Git Is the Memory Solution for the Agentic Development Lifecycle](https://arxiv.org/html/2607.14390v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models](https://arxiv.org/html/2607.14396v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Instrument Effects in Language-Model Honesty Evaluation: An Auditable Single-System Demonstration](https://arxiv.org/html/2607.14399v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Reward-Free Evolving Agents via Pairwise Validator](https://arxiv.org/html/2607.14408v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel](https://arxiv.org/html/2607.14431v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Active Real-World Factor-Based Evaluation for Generalist Robot Policies](https://arxiv.org/html/2607.14439v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Tactile: Giving Computer-Using Agents Hands and Feet](https://arxiv.org/html/2607.14443v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation](https://arxiv.org/html/2607.14493v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Contextualized Evaluation of Vision Language Models through Dynamic, Multi-turn Interactions](https://arxiv.org/html/2607.14499v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/html/2607.14506v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [RetroAgent: Harnessing LLMs to Search Over Structured Memory for Agentic Retrosynthesis Planning](https://arxiv.org/html/2607.14512v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](https://arxiv.org/html/2607.14541v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents](https://arxiv.org/html/2607.14543v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents](https://arxiv.org/html/2607.14547v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents](https://arxiv.org/html/2607.14548v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [A Modern Multimodal Assistant on a 6 GB 2011 GPU: Stage-Validated, All-GPU CUDA Inference for Fermi](https://arxiv.org/html/2607.14568v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Democratizing Agent Deployment Safety: A Structural Monitoring Approach](https://arxiv.org/html/2607.14570v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Alipay-PIBench: A Realistic Payment Integration Benchmark for Coding Agents](https://arxiv.org/html/2607.14573v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems](https://arxiv.org/html/2607.14611v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference](https://arxiv.org/html/2607.14618v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models](https://arxiv.org/html/2607.14635v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers](https://arxiv.org/html/2607.14642v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://arxiv.org/html/2607.14647v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents](https://arxiv.org/html/2607.14651v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Reflex: Real-Time VLA Control through Streaming Inference](https://arxiv.org/html/2607.14695v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color](https://arxiv.org/html/2607.14698v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models](https://arxiv.org/html/2607.14739v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [FlowGuard: From Signals to Evidence for MCP Security Detection](https://arxiv.org/html/2607.14754v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/html/2607.14777v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Is External Database Protection Static in Retrieval-Augmented Generation? Rethinking Privacy Preservation under Dynamic Queries](https://arxiv.org/html/2607.14811v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Evaluating Epistemic Uncertainty: Beyond OOD Detection and Active Learning](https://arxiv.org/html/2607.14817v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation](https://arxiv.org/html/2607.14852v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control](https://arxiv.org/html/2607.14890v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows](https://arxiv.org/html/2607.14896v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [FirmPilot: Evidence-Guided Multi-Agent Environment Recovery for IoT Firmware Rehosting](https://arxiv.org/html/2607.14903v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [CODA: Algorithm-Hardware Co-design for Edge Video Diffusion via NMP-Enabled Compute-Cache Operator Disaggregation](https://arxiv.org/html/2607.14908v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/html/2607.14952v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios](https://arxiv.org/html/2607.14989v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/html/2607.15065v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Rubrics on Trial: Evolving Rubrics from a Single Query via Synthetic Pairwise Evidence](https://arxiv.org/html/2607.15092v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Don't Predict, Prioritize: Rethinking GPU Reliability Assessment](https://arxiv.org/html/2607.15115v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents](https://arxiv.org/html/2607.15143v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [On-Policy Delta Distillation](https://arxiv.org/html/2607.15161v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Can We Trust Item Response Theory for AI Evaluation?](https://arxiv.org/html/2607.15190v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Plover: Steering GUI Agents through Plan-Centric Interaction](https://arxiv.org/html/2607.15193v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [MM-IssueLoc: A Controlled Benchmark for Evaluating Visual Evidence in Multimodal Repository-Level Issue Localization](https://arxiv.org/html/2607.15205v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/html/2607.15207v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search](https://arxiv.org/html/2607.15253v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/html/2607.15257v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04
- [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/html/2607.15263v1) — first-public（Asia/Shanghai）：2026-07-17；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、77/77 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
