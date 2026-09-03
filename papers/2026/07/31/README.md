# Daily Research — 2026-07-31

**Research Date:** 2026-07-31

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-30 09:00:00 ～ 2026-07-31 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **599** 个 identity；全量 title + abstract 筛选后冻结 **84** 个候选与 **515** 个 family-specific closure，retain rate **14.02%**。exact-v1 Review 为 84/84：Deep 10、Standard 74、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-31 |
| Window End | 2026-07-31 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-31-0900-v2.1-sha256:a3f9e1b7e4d52df9810fa9cfa9bf1b12c6977b58490caee11a319d5cc5da3e65 |
| Denominator Frozen At | 2026-09-03T17:35:11+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260731:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-30T09:00:00+08:00 | 2026-07-31T09:00:00+08:00 | 2026-09-03T17:35:11+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 599 | SF-2026-ARXIV-2607-27230;SF-2026-ARXIV-2607-27231;SF-2026-ARXIV-2607-27240;SF-2026-ARXIV-2607-27248;SF-2026-ARXIV-2607-27250;SF-2026-ARXIV-2607-27261;SF-2026-ARXIV-2607-27267;SF-2026-ARXIV-2607-27269;SF-2026-ARXIV-2607-27270;SF-2026-ARXIV-2607-27271;SF-2026-ARXIV-2607-27273;SF-2026-ARXIV-2607-27275;SF-2026-ARXIV-2607-27281;SF-2026-ARXIV-2607-27283;SF-2026-ARXIV-2607-27288;SF-2026-ARXIV-2607-27294;SF-2026-ARXIV-2607-27309;SF-2026-ARXIV-2607-27353;SF-2026-ARXIV-2607-27360;SF-2026-ARXIV-2607-27372;SF-2026-ARXIV-2607-27383;SF-2026-ARXIV-2607-27386;SF-2026-ARXIV-2607-27409;SF-2026-ARXIV-2607-27415;SF-2026-ARXIV-2607-27443;SF-2026-ARXIV-2607-27480;SF-2026-ARXIV-2607-27484;SF-2026-ARXIV-2607-27511;SF-2026-ARXIV-2607-27518;SF-2026-ARXIV-2607-27529;SF-2026-ARXIV-2607-27539;SF-2026-ARXIV-2607-27549;SF-2026-ARXIV-2607-27557;SF-2026-ARXIV-2607-27564;SF-2026-ARXIV-2607-27599;SF-2026-ARXIV-2607-27600;SF-2026-ARXIV-2607-27617;SF-2026-ARXIV-2607-27636;SF-2026-ARXIV-2607-27648;SF-2026-ARXIV-2607-27652;SF-2026-ARXIV-2607-27677;SF-2026-ARXIV-2607-27687;SF-2026-ARXIV-2607-27690;SF-2026-ARXIV-2607-27694;SF-2026-ARXIV-2607-27704;SF-2026-ARXIV-2607-27735;SF-2026-ARXIV-2607-27773;SF-2026-ARXIV-2607-27782;SF-2026-ARXIV-2607-27823;SF-2026-ARXIV-2607-27830;SF-2026-ARXIV-2607-27834;SF-2026-ARXIV-2607-27842;SF-2026-ARXIV-2607-27871;SF-2026-ARXIV-2607-27877;SF-2026-ARXIV-2607-27910;SF-2026-ARXIV-2607-27912;SF-2026-ARXIV-2607-27928;SF-2026-ARXIV-2607-27933;SF-2026-ARXIV-2607-27951;SF-2026-ARXIV-2607-27967;SF-2026-ARXIV-2607-28027;SF-2026-ARXIV-2607-28037;SF-2026-ARXIV-2607-28069;SF-2026-ARXIV-2607-28103;SF-2026-ARXIV-2607-28150;SF-2026-ARXIV-2607-28165;SF-2026-ARXIV-2607-28223;SF-2026-ARXIV-2607-28225;SF-2026-ARXIV-2607-28282;SF-2026-ARXIV-2607-28317;SF-2026-ARXIV-2607-28336;SF-2026-ARXIV-2607-28367;SF-2026-ARXIV-2607-28399;SF-2026-ARXIV-2607-28415;SF-2026-ARXIV-2607-28418;SF-2026-ARXIV-2607-28443;SF-2026-ARXIV-2607-28495;SF-2026-ARXIV-2607-28545;SF-2026-ARXIV-2607-28573;SF-2026-ARXIV-2607-28576;SF-2026-ARXIV-2607-28591;SF-2026-ARXIV-2607-28609;SF-2026-ARXIV-2607-28617;SF-2026-ARXIV-2607-28624 | all registered category pages; cross-category dedup complete | 2026-07-31T09:00:00+08:00 | sha256:a3f9e1b7e4d52df9810fa9cfa9bf1b12c6977b58490caee11a319d5cc5da3e65 | — |
<!-- coverage:SRC-ARXIV:20260731:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27230 | arXiv:2607.27230v1 | paper-v1:2607.27230 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27230 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27231 | arXiv:2607.27231v1 | paper-v1:2607.27231 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27231 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27240 | arXiv:2607.27240v1 | paper-v1:2607.27240 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27240 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27248 | arXiv:2607.27248v1 | paper-v1:2607.27248 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27248 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27250 | arXiv:2607.27250v1 | paper-v1:2607.27250 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27250 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27261 | arXiv:2607.27261v1 | paper-v1:2607.27261 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27261 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27267 | arXiv:2607.27267v1 | paper-v1:2607.27267 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27267 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27269 | arXiv:2607.27269v1 | paper-v1:2607.27269 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27269 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27270 | arXiv:2607.27270v1 | paper-v1:2607.27270 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27270 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27271 | arXiv:2607.27271v1 | paper-v1:2607.27271 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27271 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27273 | arXiv:2607.27273v1 | paper-v1:2607.27273 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27273 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27275 | arXiv:2607.27275v1 | paper-v1:2607.27275 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27275 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27281 | arXiv:2607.27281v1 | paper-v1:2607.27281 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27281 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27283 | arXiv:2607.27283v1 | paper-v1:2607.27283 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27283 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27288 | arXiv:2607.27288v1 | paper-v1:2607.27288 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27288 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27294 | arXiv:2607.27294v1 | paper-v1:2607.27294 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27294 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27309 | arXiv:2607.27309v1 | paper-v1:2607.27309 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27309 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27353 | arXiv:2607.27353v1 | paper-v1:2607.27353 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27353 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27360 | arXiv:2607.27360v1 | paper-v1:2607.27360 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27360 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27372 | arXiv:2607.27372v1 | paper-v1:2607.27372 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27372 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27383 | arXiv:2607.27383v1 | paper-v1:2607.27383 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27383 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27386 | arXiv:2607.27386v1 | paper-v1:2607.27386 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27386 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27409 | arXiv:2607.27409v1 | paper-v1:2607.27409 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27409 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27415 | arXiv:2607.27415v1 | paper-v1:2607.27415 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27415 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27443 | arXiv:2607.27443v1 | paper-v1:2607.27443 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27443 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27480 | arXiv:2607.27480v1 | paper-v1:2607.27480 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27480 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27484 | arXiv:2607.27484v1 | paper-v1:2607.27484 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27484 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27511 | arXiv:2607.27511v1 | paper-v1:2607.27511 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27511 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27518 | arXiv:2607.27518v1 | paper-v1:2607.27518 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27518 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27529 | arXiv:2607.27529v1 | paper-v1:2607.27529 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27529 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27539 | arXiv:2607.27539v1 | paper-v1:2607.27539 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27539 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27549 | arXiv:2607.27549v1 | paper-v1:2607.27549 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27549 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27557 | arXiv:2607.27557v1 | paper-v1:2607.27557 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27557 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27564 | arXiv:2607.27564v1 | paper-v1:2607.27564 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27564 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27599 | arXiv:2607.27599v1 | paper-v1:2607.27599 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27599 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27600 | arXiv:2607.27600v1 | paper-v1:2607.27600 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27600 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27617 | arXiv:2607.27617v1 | paper-v1:2607.27617 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27617 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27636 | arXiv:2607.27636v1 | paper-v1:2607.27636 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27636 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27648 | arXiv:2607.27648v1 | paper-v1:2607.27648 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27648 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27652 | arXiv:2607.27652v1 | paper-v1:2607.27652 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27652 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27677 | arXiv:2607.27677v1 | paper-v1:2607.27677 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27677 | self | — | new_in_window | PLATFORM-PRODUCTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27687 | arXiv:2607.27687v1 | paper-v1:2607.27687 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27687 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27690 | arXiv:2607.27690v1 | paper-v1:2607.27690 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27690 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27694 | arXiv:2607.27694v1 | paper-v1:2607.27694 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27694 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27704 | arXiv:2607.27704v1 | paper-v1:2607.27704 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27704 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27735 | arXiv:2607.27735v1 | paper-v1:2607.27735 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27735 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27773 | arXiv:2607.27773v1 | paper-v1:2607.27773 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27773 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27782 | arXiv:2607.27782v1 | paper-v1:2607.27782 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27782 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27823 | arXiv:2607.27823v1 | paper-v1:2607.27823 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27823 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27830 | arXiv:2607.27830v1 | paper-v1:2607.27830 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27830 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27834 | arXiv:2607.27834v1 | paper-v1:2607.27834 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27834 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27842 | arXiv:2607.27842v1 | paper-v1:2607.27842 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27842 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27871 | arXiv:2607.27871v1 | paper-v1:2607.27871 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27871 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27877 | arXiv:2607.27877v1 | paper-v1:2607.27877 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27877 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27910 | arXiv:2607.27910v1 | paper-v1:2607.27910 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27910 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27912 | arXiv:2607.27912v1 | paper-v1:2607.27912 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27912 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27928 | arXiv:2607.27928v1 | paper-v1:2607.27928 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27928 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27933 | arXiv:2607.27933v1 | paper-v1:2607.27933 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27933 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27951 | arXiv:2607.27951v1 | paper-v1:2607.27951 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27951 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27967 | arXiv:2607.27967v1 | paper-v1:2607.27967 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27967 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28027 | arXiv:2607.28027v1 | paper-v1:2607.28027 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28027 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28037 | arXiv:2607.28037v1 | paper-v1:2607.28037 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28037 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28069 | arXiv:2607.28069v1 | paper-v1:2607.28069 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28069 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28103 | arXiv:2607.28103v1 | paper-v1:2607.28103 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28103 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28150 | arXiv:2607.28150v1 | paper-v1:2607.28150 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28150 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28165 | arXiv:2607.28165v1 | paper-v1:2607.28165 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28165 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28223 | arXiv:2607.28223v1 | paper-v1:2607.28223 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28223 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28225 | arXiv:2607.28225v1 | paper-v1:2607.28225 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28225 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28282 | arXiv:2607.28282v1 | paper-v1:2607.28282 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28282 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28317 | arXiv:2607.28317v1 | paper-v1:2607.28317 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28317 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28336 | arXiv:2607.28336v1 | paper-v1:2607.28336 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28336 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28367 | arXiv:2607.28367v1 | paper-v1:2607.28367 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28367 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28399 | arXiv:2607.28399v1 | paper-v1:2607.28399 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28399 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28415 | arXiv:2607.28415v1 | paper-v1:2607.28415 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28415 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28418 | arXiv:2607.28418v1 | paper-v1:2607.28418 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28418 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28443 | arXiv:2607.28443v1 | paper-v1:2607.28443 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28443 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28495 | arXiv:2607.28495v1 | paper-v1:2607.28495 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28495 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28545 | arXiv:2607.28545v1 | paper-v1:2607.28545 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28545 | self | — | new_in_window | PLATFORM-MONITORING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28573 | arXiv:2607.28573v1 | paper-v1:2607.28573 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28573 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28576 | arXiv:2607.28576v1 | paper-v1:2607.28576 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28576 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28591 | arXiv:2607.28591v1 | paper-v1:2607.28591 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28591 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28609 | arXiv:2607.28609v1 | paper-v1:2607.28609 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28609 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28617 | arXiv:2607.28617v1 | paper-v1:2607.28617 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28617 | self | — | new_in_window | AGENT-PROMPT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28624 | arXiv:2607.28624v1 | paper-v1:2607.28624 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-28624 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27230 | RP-6aefd78104e1e6f6 | standard | arXiv:2607.27230v1 | SRC-ARXIV@arXiv:2607.27230v1 | https://arxiv.org/html/2607.27230v1#S2 — 2 Method: Multi-Head Attention Residuals | https://arxiv.org/html/2607.27230v1#S3 — 3 Experiments; https://arxiv.org/html/2607.27230v1#S4 — 4 Ablations | https://arxiv.org/html/2607.27230v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/datasets/HuggingFaceFW/finepdfs, https://huggingface.co/datasets/HuggingFaceTB/stack-edu, https://huggingface.co/marin-community/marin-8b-base; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27230 | complete |
| SF-2026-ARXIV-2607-27231 | RP-7cf052956a5816cf | deep | arXiv:2607.27231v1 | SRC-ARXIV@arXiv:2607.27231v1 | https://arxiv.org/html/2607.27231v1#A1 — Appendix A Prompt Design; https://arxiv.org/html/2607.27231v1#S3.SS3 — 3.3 Evaluation Framework | https://arxiv.org/html/2607.27231v1#A9 — Appendix I Fast p Evaluation and Cost Results; https://arxiv.org/html/2607.27231v1#S4 — 4 Experiments and Evaluation | https://arxiv.org/html/2607.27231v1#A11 — Appendix K Platform-Specific Failure Patterns; https://arxiv.org/html/2607.27231v1#S2.SS2 — 2.2 Limitations of Existing Benchmarks | Exact v1 links https://github.com/flagos-ai/KernelGenBench, https://github.com/meta-pytorch/tritonbench, https://huggingface.co/facebook/KernelLLM; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27231 | complete |
| SF-2026-ARXIV-2607-27240 | RP-a4c80528f380925f | standard | arXiv:2607.27240v1 | SRC-ARXIV@arXiv:2607.27240v1 | https://arxiv.org/html/2607.27240v1#A2.SS0.SSS0.Px1 — Method; https://arxiv.org/html/2607.27240v1#S2 — 2 Methodology | https://arxiv.org/html/2607.27240v1#S3 — 3 Experimentation and Results; https://arxiv.org/html/2607.27240v1#S2.SS0.SSS0.Px3 — Merge configuration and evaluation. | https://arxiv.org/html/2607.27240v1#S4 — 4 Limitations and Future Work; https://arxiv.org/html/2607.27240v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27240 | complete |
| SF-2026-ARXIV-2607-27248 | RP-5a16a8d9ca1913b4 | standard | arXiv:2607.27248v1 | SRC-ARXIV@arXiv:2607.27248v1 | https://arxiv.org/html/2607.27248v1#S3 — 3 Method; https://arxiv.org/html/2607.27248v1#A2 — Appendix B Implementation Details. | https://arxiv.org/html/2607.27248v1#S4 — 4 Main Experiments on Scientific Benchmarks; https://arxiv.org/html/2607.27248v1#A1 — Appendix A Theoretical Analysis | https://arxiv.org/html/2607.27248v1#A7 — Appendix G Limitations and Broader Impacts; https://arxiv.org/html/2607.27248v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/think-a-tron/raman-01-1.7B, https://github.com/wyattxuanyang/Divergence-Decoding, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27248 | complete |
| SF-2026-ARXIV-2607-27250 | RP-8660d05ec60f2dea | deep | arXiv:2607.27250v1 | SRC-ARXIV@arXiv:2607.27250v1 | https://arxiv.org/html/2607.27250v1#S3 — 3 Method | https://arxiv.org/html/2607.27250v1#A1 — Appendix A Experimental Harness Details; https://arxiv.org/html/2607.27250v1#A2 — Appendix B Per-Task Results | https://arxiv.org/html/2607.27250v1#S5 — 5 Discussion; https://arxiv.org/html/2607.27250v1#S6 — 6 Conclusion | Exact v1 links https://github.com/codeprakhar25/context-files-coding-agents, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27250 | complete |
| SF-2026-ARXIV-2607-27261 | RP-3f83ee055b40c412 | standard | arXiv:2607.27261v1 | SRC-ARXIV@arXiv:2607.27261v1 | https://arxiv.org/html/2607.27261v1#A1 — Appendix A CFNBC Algorithm and Implementation Details | https://arxiv.org/html/2607.27261v1#S4 — IV Experiment Setup; https://arxiv.org/html/2607.27261v1#S5 — V Results and Discussion | https://arxiv.org/html/2607.27261v1#A3 — Appendix C Narrow repair mainly repairs narrow failure modes; https://arxiv.org/html/2607.27261v1#S5 — V Results and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27261 | complete |
| SF-2026-ARXIV-2607-27267 | RP-14b3cc1c64142512 | deep | arXiv:2607.27267v1 | SRC-ARXIV@arXiv:2607.27267v1 | https://arxiv.org/html/2607.27267v1#Sx3 — FAVA Method; https://arxiv.org/html/2607.27267v1#Sx3.SSx6 — Security Assumptions and System Scope | https://arxiv.org/html/2607.27267v1#Sx5 — Experiments; https://arxiv.org/html/2607.27267v1#Sx5.SSx1 — RQ1: Main Permission-Compliance Result | https://arxiv.org/html/2607.27267v1#Sx5.SSx5 — RQ5: Failure Analysis; https://arxiv.org/html/2607.27267v1#Sx6 — Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27267 | complete |
| SF-2026-ARXIV-2607-27269 | RP-6c730b122a025fdd | deep | arXiv:2607.27269v1 | SRC-ARXIV@arXiv:2607.27269v1 | https://arxiv.org/html/2607.27269v1#Sx4 — Method | https://arxiv.org/html/2607.27269v1#Sx6 — Results and Analysis; https://arxiv.org/html/2607.27269v1#Sx5 — Experiments | https://arxiv.org/html/2607.27269v1#Sx7 — Discussion; https://arxiv.org/html/2607.27269v1#Sx8 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27269 | complete |
| SF-2026-ARXIV-2607-27270 | RP-f34aea731170716b | standard | arXiv:2607.27270v1 | SRC-ARXIV@arXiv:2607.27270v1 | https://arxiv.org/html/2607.27270v1#S3 — 3. Method; https://arxiv.org/html/2607.27270v1#S4 — 4. Experimental Design | https://arxiv.org/html/2607.27270v1#S4 — 4. Experimental Design; https://arxiv.org/html/2607.27270v1#S5 — 5. Results | https://arxiv.org/html/2607.27270v1#S6 — 6. Discussion and Limitations; https://arxiv.org/html/2607.27270v1#S8 — 8. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27270 | complete |
| SF-2026-ARXIV-2607-27271 | RP-edea045e3409a5d3 | standard | arXiv:2607.27271v1 | SRC-ARXIV@arXiv:2607.27271v1 | https://arxiv.org/html/2607.27271v1#A6 — Appendix F Model-Generated Performance References; https://arxiv.org/html/2607.27271v1#Sx5.SSx3 — Efficiency training improves model ranking | https://arxiv.org/html/2607.27271v1#Sx4.SSx1 — Benchmarks and Evaluation Protocol; https://arxiv.org/html/2607.27271v1#Sx5 — Experiment Results | https://arxiv.org/html/2607.27271v1#A10 — Appendix J Remaining Failure Patterns; https://arxiv.org/html/2607.27271v1#A14 — Appendix N Failure-Stage Counts | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27271 | complete |
| SF-2026-ARXIV-2607-27273 | RP-93c0883cafb9e3ea | standard | arXiv:2607.27273v1 | SRC-ARXIV@arXiv:2607.27273v1 | https://arxiv.org/html/2607.27273v1#Sx3 — Method | https://arxiv.org/html/2607.27273v1#Sx4 — Experiments; https://arxiv.org/html/2607.27273v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.27273v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27273 | complete |
| SF-2026-ARXIV-2607-27275 | RP-ff7eded6e5f364dc | deep | arXiv:2607.27275v1 | SRC-ARXIV@arXiv:2607.27275v1 | https://arxiv.org/html/2607.27275v1#Sx1 — Introduction; https://arxiv.org/html/2607.27275v1#Sx2 — Related Work | https://arxiv.org/html/2607.27275v1#A1 — Appendix A Additional Results; https://arxiv.org/html/2607.27275v1#Sx3 — Experimental Setup | https://arxiv.org/html/2607.27275v1#A2 — Appendix B Limitations; https://arxiv.org/html/2607.27275v1#Sx4.SSx4 — Quantization Amplifies the Existing Failure Set, Not New Ones | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27275 | complete |
| SF-2026-ARXIV-2607-27281 | RP-485bdad3c50788b4 | standard | arXiv:2607.27281v1 | SRC-ARXIV@arXiv:2607.27281v1 | https://arxiv.org/html/2607.27281v1#S3 — 3 Methods and apparatus; https://arxiv.org/html/2607.27281v1#A1 — Appendix A The occupation theorem: model, assumptions, and full proofs | https://arxiv.org/html/2607.27281v1#S11 — 11 Negative results and reproducibility | https://arxiv.org/html/2607.27281v1#S14 — 14 Conclusion; https://arxiv.org/html/2607.27281v1#S4.SS4 — 4.4 Testing the premises, not just the conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27281 | complete |
| SF-2026-ARXIV-2607-27283 | RP-0651eef4b2438dec | deep | arXiv:2607.27283v1 | SRC-ARXIV@arXiv:2607.27283v1 | https://arxiv.org/html/2607.27283v1#S3 — 3 A System-Matched Counterfactual for Long-Horizon Evaluation; https://arxiv.org/html/2607.27283v1#S5 — 5 A Benchmark Design Protocol for Coding and Terminal Agents | https://arxiv.org/html/2607.27283v1#S3.SS3 — 3.3 The Horizon Residual; https://arxiv.org/html/2607.27283v1#S4 — 4 Separating Task Structure from Local Difficulty | https://arxiv.org/html/2607.27283v1#S7 — 7 Scope, Limitations, and Falsifiability; https://arxiv.org/html/2607.27283v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27283 | complete |
| SF-2026-ARXIV-2607-27288 | RP-20d96b4459531b55 | standard | arXiv:2607.27288v1 | SRC-ARXIV@arXiv:2607.27288v1 | https://arxiv.org/html/2607.27288v1#S4 — 4 Framework Components; https://arxiv.org/html/2607.27288v1#S4.SS5 — 4.5 Bring Your Own Agent or Model | https://arxiv.org/html/2607.27288v1#S4.SS2 — 4.2 Tasks and Evaluation Sets; https://arxiv.org/html/2607.27288v1#S4.SS3 — 4.3 Evaluation Metrics | https://arxiv.org/html/2607.27288v1#S7 — 7 Discussion; https://arxiv.org/html/2607.27288v1#S8 — 8 Conclusion | Exact v1 links https://github.com/OpenSecurityAI/benchmark, https://huggingface.co/OpenSecurityAI, https://github.com/nccgroup/ScoutSuite; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27288 | complete |
| SF-2026-ARXIV-2607-27294 | RP-fc6fcd0cebe29569 | standard | arXiv:2607.27294v1 | SRC-ARXIV@arXiv:2607.27294v1 | https://arxiv.org/html/2607.27294v1#A1 — Appendix A Runtime-Safety Framework and Threat Boundaries; https://arxiv.org/html/2607.27294v1#A6.SS1 — F.1 Evaluated Systems and Risk Coverage | https://arxiv.org/html/2607.27294v1#A2 — Appendix B Benchmark Construction and Quality Control; https://arxiv.org/html/2607.27294v1#A2.SS4 — B.4 Benchmark Composition and Coverage | https://arxiv.org/html/2607.27294v1#A1 — Appendix A Runtime-Safety Framework and Threat Boundaries; https://arxiv.org/html/2607.27294v1#A1.SS7 — A.7 Threat-Scope Exclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27294 | complete |
| SF-2026-ARXIV-2607-27309 | RP-6756f94f4fd5f0c0 | standard | arXiv:2607.27309v1 | SRC-ARXIV@arXiv:2607.27309v1 | https://arxiv.org/html/2607.27309v1#S3.SS1 — 3.1. Design requirements; https://arxiv.org/html/2607.27309v1#S4.SS3 — 4.3. Implementation | https://arxiv.org/html/2607.27309v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.27309v1#S5.SS1 — 5.1. Experimental setup | https://arxiv.org/html/2607.27309v1#S2.SS2 — 2.2. What the failures have in common; https://arxiv.org/html/2607.27309v1#S5.SS7 — 5.7. Threats to validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27309 | complete |
| SF-2026-ARXIV-2607-27353 | RP-6a0b243ba7ee637d | standard | arXiv:2607.27353v1 | SRC-ARXIV@arXiv:2607.27353v1 | https://arxiv.org/html/2607.27353v1#S2 — 2 Benchmark and Methods; https://arxiv.org/html/2607.27353v1#S2.SS1 — 2.1 Benchmark design and threat model | https://arxiv.org/html/2607.27353v1#A1 — Appendix A Additional Live-Matrix Results; https://arxiv.org/html/2607.27353v1#S2 — 2 Benchmark and Methods | https://arxiv.org/html/2607.27353v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.27353v1#S2.SS1 — 2.1 Benchmark design and threat model | Exact v1 links https://github.com/MusaShams/layerrag-bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27353 | complete |
| SF-2026-ARXIV-2607-27360 | RP-120da0a9c61d5db9 | standard | arXiv:2607.27360v1 | SRC-ARXIV@arXiv:2607.27360v1 | https://arxiv.org/html/2607.27360v1#S3 — 3 Method; https://arxiv.org/html/2607.27360v1#S4.SS6 — 4.6 Robustness: How Dependent Is SkillMentor on Strong Models? | https://arxiv.org/html/2607.27360v1#S3.SS3 — 3.3 Gap Evaluation; https://arxiv.org/html/2607.27360v1#S4 — 4 Experiments | https://arxiv.org/html/2607.27360v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27360 | complete |
| SF-2026-ARXIV-2607-27372 | RP-a2461afccc19cf29 | standard | arXiv:2607.27372v1 | SRC-ARXIV@arXiv:2607.27372v1 | https://arxiv.org/html/2607.27372v1#A3 — Appendix C Approach Details; https://arxiv.org/html/2607.27372v1#A5.SS3 — E.3 Explorative Modeling Based Methods | https://arxiv.org/html/2607.27372v1#S4 — 4 Experimentation and Results; https://arxiv.org/html/2607.27372v1#A1 — Appendix A Additional Experimentation | https://arxiv.org/html/2607.27372v1#S7 — 7 Limitations and Conclusion; https://arxiv.org/html/2607.27372v1#S5 — 5 Discussion | Exact v1 links https://github.com/alexiglad/XM, https://github.com/qlabs-eng/slowrun, https://huggingface.co/stabilityai/sd-vae-ft-mse; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27372 | complete |
| SF-2026-ARXIV-2607-27383 | RP-f7667edaf4c037b5 | standard | arXiv:2607.27383v1 | SRC-ARXIV@arXiv:2607.27383v1 | https://arxiv.org/html/2607.27383v1#S5 — 5 Algorithm: Adam | https://arxiv.org/html/2607.27383v1#S1 — 1 Introduction; https://arxiv.org/html/2607.27383v1#S2 — 2 Related Work | https://arxiv.org/html/2607.27383v1#S7 — 7 Conclusion and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27383 | complete |
| SF-2026-ARXIV-2607-27386 | RP-df177a0d61d06a36 | standard | arXiv:2607.27386v1 | SRC-ARXIV@arXiv:2607.27386v1 | https://arxiv.org/html/2607.27386v1#S5 — 5 Mechanistic Probing Methodology; https://arxiv.org/html/2607.27386v1#A2 — Appendix B IPM Algorithm (Full Pseudocode) | https://arxiv.org/html/2607.27386v1#A7 — Appendix G Full IPM Ablation Results; https://arxiv.org/html/2607.27386v1#A8 — Appendix H Statistical Significance and Question-Only Ablation | https://arxiv.org/html/2607.27386v1#A10 — Appendix J Extended Limitations Discussion; https://arxiv.org/html/2607.27386v1#A1 — Appendix A Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27386 | complete |
| SF-2026-ARXIV-2607-27409 | RP-dfa34e8e148610de | standard | arXiv:2607.27409v1 | SRC-ARXIV@arXiv:2607.27409v1 | https://arxiv.org/pdf/2607.27409v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.27409v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.27409v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.27409v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.27409v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.27409v1#page=10 — PDF page 10 | Exact v1 links https://github.com/openai/codex, https://github.com/asottile/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27409 | complete |
| SF-2026-ARXIV-2607-27415 | RP-da1d76e50a7437e4 | standard | arXiv:2607.27415v1 | SRC-ARXIV@arXiv:2607.27415v1 | https://arxiv.org/html/2607.27415v1#S3 — 3 Methodology; https://arxiv.org/html/2607.27415v1#A3.SS3 — C.3 Implementation | https://arxiv.org/html/2607.27415v1#A2 — Appendix B Proof of Theoretical Analysis; https://arxiv.org/html/2607.27415v1#A3 — Appendix C Experimental Setup | https://arxiv.org/html/2607.27415v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27415 | complete |
| SF-2026-ARXIV-2607-27443 | RP-8d640fefd6970410 | standard | arXiv:2607.27443v1 | SRC-ARXIV@arXiv:2607.27443v1 | https://arxiv.org/html/2607.27443v1#A3 — Appendix C Detailed Implementation; https://arxiv.org/html/2607.27443v1#A3.SS3 — C.3 Agent Implementation | https://arxiv.org/html/2607.27443v1#S5.SS2 — 5.2 Feedback Evaluation Results; https://arxiv.org/html/2607.27443v1#A4 — Appendix D Extensive Results | https://arxiv.org/html/2607.27443v1#S6 — 6 Conclusion | Exact v1 links https://github.com/OSU-NLP-Group/TravelPlanner, https://github.com/scikit-learn/scikit-learn, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27443 | complete |
| SF-2026-ARXIV-2607-27480 | RP-426248b5c2a30cec | standard | arXiv:2607.27480v1 | SRC-ARXIV@arXiv:2607.27480v1 | https://arxiv.org/html/2607.27480v1#S1.SS1 — 1.1. Our Approach; https://arxiv.org/html/2607.27480v1#S2.SS4 — 2.4. Specifying Information Flow in Combinational Methods | https://arxiv.org/html/2607.27480v1#S7.SS1 — 7.1. Software Static Analysis; https://arxiv.org/html/2607.27480v1#S6 — 6. Verification Case Study: A Pipelined Processor | https://arxiv.org/html/2607.27480v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.27480v1#S3.SS2 — 3.2. Security Goal and Threat Model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27480 | complete |
| SF-2026-ARXIV-2607-27484 | RP-13597e66b705b611 | standard | arXiv:2607.27484v1 | SRC-ARXIV@arXiv:2607.27484v1 | https://arxiv.org/html/2607.27484v1#A1.SSx1 — Backtrace Design Commitments; https://arxiv.org/html/2607.27484v1#Sx4 — Methodology | https://arxiv.org/html/2607.27484v1#A3 — Appendix C Additional Analysis for RQ2; https://arxiv.org/html/2607.27484v1#A4 — Appendix D Additional Analysis for RQ3 | https://arxiv.org/html/2607.27484v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27484 | complete |
| SF-2026-ARXIV-2607-27511 | RP-dd11a0acf25bb7e3 | standard | arXiv:2607.27511v1 | SRC-ARXIV@arXiv:2607.27511v1 | https://arxiv.org/html/2607.27511v1#S3 — III Method; https://arxiv.org/html/2607.27511v1#S3.SS1 — III-A World Modeling in Latent Vision Space | https://arxiv.org/html/2607.27511v1#S4.SS2 — IV-B Experimental Results; https://arxiv.org/html/2607.27511v1#S4 — IV Experiments | https://arxiv.org/html/2607.27511v1#S6 — VI Discussion and Conclusion; https://arxiv.org/html/2607.27511v1#S3.SS2 — III-B Nonconformity Scoring and Conformal Failure Detection | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27511 | complete |
| SF-2026-ARXIV-2607-27518 | RP-ab827a67092907bd | standard | arXiv:2607.27518v1 | SRC-ARXIV@arXiv:2607.27518v1 | https://arxiv.org/html/2607.27518v1#S3 — 3 Methodology; https://arxiv.org/html/2607.27518v1#S3.SS1 — 3.1 Evaluation quality framework | https://arxiv.org/html/2607.27518v1#A1.SS4 — A.4 Scanner results on non-agentic evaluations; https://arxiv.org/html/2607.27518v1#S2.SS3 — 2.3 Evaluation auditing work using transcript analysis | https://arxiv.org/html/2607.27518v1#A5.SS2 — E.2 Tool Failure; https://arxiv.org/html/2607.27518v1#S5 — 5 Discussion | Exact v1 links https://github.com/Generality-Labs/scanner_evaluation, https://huggingface.co/datasets/generality-labs/abc-scout-scanners/, https://epoch.ai/publications/mirrorcode-preliminary-results; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27518 | complete |
| SF-2026-ARXIV-2607-27529 | RP-48c4faed29659154 | standard | arXiv:2607.27529v1 | SRC-ARXIV@arXiv:2607.27529v1 | https://arxiv.org/html/2607.27529v1#A5 — Appendix E Architecture details; https://arxiv.org/html/2607.27529v1#S4 — 4 Method | https://arxiv.org/html/2607.27529v1#A4.SS7 — D.7 Proof of Proposition 3 (marginal NELBO for evaluation); https://arxiv.org/html/2607.27529v1#A6 — Appendix F Decoding-policy ablations | https://arxiv.org/html/2607.27529v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27529 | complete |
| SF-2026-ARXIV-2607-27539 | RP-ae5a6991a37d064d | deep | arXiv:2607.27539v1 | SRC-ARXIV@arXiv:2607.27539v1 | https://arxiv.org/html/2607.27539v1#S3.SS5 — 3.5 Recovering the redesigned memory; https://arxiv.org/html/2607.27539v1#S3.SS6 — 3.6 The exact decrement, audited at the model output | https://arxiv.org/html/2607.27539v1#A1 — Appendix A Experimental details; https://arxiv.org/html/2607.27539v1#A2 — Appendix B Full 1B utility results | https://arxiv.org/html/2607.27539v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.27539v1#S8 — 8 Discussion: deletion is a property of representation | Not Disclosed — exact v1 does not bind the evaluated checkpoint-replay and support-vector-memory implementation to an immutable public experiment commit; the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27539 | complete |
| SF-2026-ARXIV-2607-27549 | RP-37d26b2d2cea8ea2 | standard | arXiv:2607.27549v1 | SRC-ARXIV@arXiv:2607.27549v1 | https://arxiv.org/html/2607.27549v1#S4.SS1 — IV-A Benchmark Design; https://arxiv.org/html/2607.27549v1#S3.SS3 — III-C Implementation Details | https://arxiv.org/html/2607.27549v1#S4 — IV Simulation Experiments; https://arxiv.org/html/2607.27549v1#S4.SS1 — IV-A Benchmark Design | https://arxiv.org/html/2607.27549v1#S6 — VI Conclusion | Exact v1 links https://github.com/Stanford-ILIAD/openvla-mini, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27549 | complete |
| SF-2026-ARXIV-2607-27557 | RP-a0d943e17baf8446 | standard | arXiv:2607.27557v1 | SRC-ARXIV@arXiv:2607.27557v1 | https://arxiv.org/html/2607.27557v1#S3 — 3 Method; https://arxiv.org/html/2607.27557v1#S3.SS5 — 3.5 Compact Memory Architecture | https://arxiv.org/html/2607.27557v1#S4 — 4 Experiments; https://arxiv.org/html/2607.27557v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.27557v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27557 | complete |
| SF-2026-ARXIV-2607-27564 | RP-05327f96b48d6cb3 | standard | arXiv:2607.27564v1 | SRC-ARXIV@arXiv:2607.27564v1 | https://arxiv.org/html/2607.27564v1#A1.SS5 — A.5 Prompt-Space Design; https://arxiv.org/html/2607.27564v1#A1.SS7 — A.7 Implementation Notes and Reproducibility | https://arxiv.org/html/2607.27564v1#S5 — 5 Experiments and Results; https://arxiv.org/html/2607.27564v1#S5.SS1 — 5.1 Main Results | https://arxiv.org/html/2607.27564v1#A1.SS4 — A.4 Failure Cases and Boundary Conditions; https://arxiv.org/html/2607.27564v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27564 | complete |
| SF-2026-ARXIV-2607-27599 | RP-0efbeef7b4055bfb | standard | arXiv:2607.27599v1 | SRC-ARXIV@arXiv:2607.27599v1 | https://arxiv.org/html/2607.27599v1#S3 — 3 Methods; https://arxiv.org/html/2607.27599v1#A3 — Appendix C Implementation Details | https://arxiv.org/html/2607.27599v1#A4 — Appendix D Experiment Details; https://arxiv.org/html/2607.27599v1#A5 — Appendix E Wall Clock Time Analysis | https://arxiv.org/html/2607.27599v1#S6 — 6 Conclusion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27599 | complete |
| SF-2026-ARXIV-2607-27600 | RP-75ba0678bb41b628 | standard | arXiv:2607.27600v1 | SRC-ARXIV@arXiv:2607.27600v1 | https://arxiv.org/html/2607.27600v1#S3.SS2 — 3.2 Algorithm Summary | https://arxiv.org/html/2607.27600v1#A1 — Appendix A Benchmark Prompts; https://arxiv.org/html/2607.27600v1#S4 — 4 Experiments | https://arxiv.org/html/2607.27600v1#S5 — 5 Conclusion and Discussion | Exact v1 links https://github.com/metacognitionai/counter_causal, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27600 | complete |
| SF-2026-ARXIV-2607-27617 | RP-033c1569aefbe026 | standard | arXiv:2607.27617v1 | SRC-ARXIV@arXiv:2607.27617v1 | https://arxiv.org/html/2607.27617v1#A12 — Appendix L Full Architecture Competition; https://arxiv.org/html/2607.27617v1#A12.SS1 — L.1 Supplementary Table S12: Architecture Ranking Across Distribution Shifts | https://arxiv.org/html/2607.27617v1#A16.SS4 — P.4 What the Model-Organism Results Establish and What They Do Not; https://arxiv.org/html/2607.27617v1#A18 — Appendix R Complete Statistical Analysis Protocol | https://arxiv.org/html/2607.27617v1#A15.SS1 — O.1 Supplementary Figure S6: Conceptual Overview of Forked Futures and Hidden APIs; https://arxiv.org/html/2607.27617v1#A16.SS1 — P.1 From Future Equivalence to an Empirical Causal Quotient | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27617 | complete |
| SF-2026-ARXIV-2607-27636 | RP-febc0b5e1a0bccfd | deep | arXiv:2607.27636v1 | SRC-ARXIV@arXiv:2607.27636v1 | https://arxiv.org/html/2607.27636v1#Sx3 — Method; https://arxiv.org/html/2607.27636v1#A2 — Appendix B Formal Model and Protocol | https://arxiv.org/html/2607.27636v1#A3 — Appendix C Evaluation Details; https://arxiv.org/html/2607.27636v1#Sx4 — Evaluation | https://arxiv.org/html/2607.27636v1#A4.SSx2 — Threats to Validity; https://arxiv.org/html/2607.27636v1#Sx5 — Discussion | Not Disclosed — exact v1 describes the protocol and PX4/Gazebo evaluation but does not pin an immutable public implementation commit used for the reported runs. | claim:SF-2026-ARXIV-2607-27636 | complete |
| SF-2026-ARXIV-2607-27648 | RP-2c3e056fb864214b | standard | arXiv:2607.27648v1 | SRC-ARXIV@arXiv:2607.27648v1 | https://arxiv.org/html/2607.27648v1#S4 — 4. Design | https://arxiv.org/html/2607.27648v1#S4.SS3 — 4.3. Workflow Evaluation; https://arxiv.org/html/2607.27648v1#S5 — 5. Experiment | https://arxiv.org/html/2607.27648v1#S6 — 6. Discussion; https://arxiv.org/html/2607.27648v1#S7 — 7. Conclusion | Exact v1 links https://huggingface.co/datasets/openlifescienceai/medmcqa/tree/main/data, https://github.com/LLMBias/BiasLens/tree/main, https://developers.openai.com/api/docs/guides/tools-code-interpreter; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27648 | complete |
| SF-2026-ARXIV-2607-27652 | RP-530ec7c60a5b42bd | standard | arXiv:2607.27652v1 | SRC-ARXIV@arXiv:2607.27652v1 | https://arxiv.org/html/2607.27652v1#Sx3 — Method; https://arxiv.org/html/2607.27652v1#A5 — Appendix E Implementation Details | https://arxiv.org/html/2607.27652v1#Sx4.SSx3 — Ablation and Comparative Analysis (RQ2); https://arxiv.org/html/2607.27652v1#A4 — Appendix D Evaluation Details | https://arxiv.org/html/2607.27652v1#A14.SS4 — N.4 Additional Failure Cases; https://arxiv.org/html/2607.27652v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27652 | complete |
| SF-2026-ARXIV-2607-27677 | RP-9a38bd3c737a71f4 | standard | arXiv:2607.27677v1 | SRC-ARXIV@arXiv:2607.27677v1 | https://arxiv.org/html/2607.27677v1#S5 — 5 Implementation in ProofAgent Harness | https://arxiv.org/html/2607.27677v1#S4.SS6 — 4.6 Ablation analysis; https://arxiv.org/html/2607.27677v1#S2 — 2 Related Work: From Agent Evaluation to Governance | https://arxiv.org/html/2607.27677v1#S4.SS12 — 4.12 Failure mode coverage; https://arxiv.org/html/2607.27677v1#S6 — 6 Conclusion | Exact v1 links https://github.com/ProofAgent-ai/proofagent-harness, https://pypi.org/project/proofagent-harness/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27677 | complete |
| SF-2026-ARXIV-2607-27687 | RP-b076de5c65d212b4 | standard | arXiv:2607.27687v1 | SRC-ARXIV@arXiv:2607.27687v1 | https://arxiv.org/html/2607.27687v1#A1 — Appendix A Propose–Predict–Execute algorithm | https://arxiv.org/html/2607.27687v1#A5 — Appendix E Why focused memory works: component analysis; https://arxiv.org/html/2607.27687v1#A7 — Appendix G Per-seed generalization results | https://arxiv.org/html/2607.27687v1#S6 — 6 Limitations; https://arxiv.org/html/2607.27687v1#S7 — 7 Conclusion | Exact v1 links https://github.com/karpathy/autoresearch/commit/228791fb499afffb54b46200aca536f79142f117, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/tree/1110a243fdf4706b3f48f1d95db1a4f5529b4d41, https://huggingface.co/tencent/Hy3-preview/commit/549c2b3a0fd5b9a6c6059a9935bf0d59ab69d75a; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27687 | complete |
| SF-2026-ARXIV-2607-27690 | RP-99825b85176d8210 | standard | arXiv:2607.27690v1 | SRC-ARXIV@arXiv:2607.27690v1 | https://arxiv.org/html/2607.27690v1#S3 — 3 Methodology | https://arxiv.org/html/2607.27690v1#S4 — 4 Experiments; https://arxiv.org/html/2607.27690v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.27690v1#S5 — 5 Conclusion | Exact v1 links https://github.com/AndyGao6186/LabEvolver, https://huggingface.co/Qwen/Qwen3.5-35B-A3B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27690 | complete |
| SF-2026-ARXIV-2607-27694 | RP-0ccc9c47e5ee7138 | standard | arXiv:2607.27694v1 | SRC-ARXIV@arXiv:2607.27694v1 | https://arxiv.org/html/2607.27694v1#S5 — V GyRot Microarchitecture; https://arxiv.org/html/2607.27694v1#S3.SS1 — III-A Model Accuracy Perspective | https://arxiv.org/html/2607.27694v1#S6 — VI Evaluation; https://arxiv.org/html/2607.27694v1#S6.SS1 — VI-A Experiment Setup | https://arxiv.org/html/2607.27694v1#S7 — VII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27694 | complete |
| SF-2026-ARXIV-2607-27704 | RP-fd84365dfd2c5de9 | standard | arXiv:2607.27704v1 | SRC-ARXIV@arXiv:2607.27704v1 | https://arxiv.org/html/2607.27704v1#S5.SS1 — V-A Overall Architecture; https://arxiv.org/html/2607.27704v1#S3 — III Proposed LightRot Algorithm | https://arxiv.org/html/2607.27704v1#S4 — IV Algorithm Experiments; https://arxiv.org/html/2607.27704v1#S4.SS1 — IV-A Perplexity Evaluation on WikiText-2 | https://arxiv.org/html/2607.27704v1#S7 — VII Discussion; https://arxiv.org/html/2607.27704v1#S8 — VIII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27704 | complete |
| SF-2026-ARXIV-2607-27735 | RP-20719bb14f23c26a | standard | arXiv:2607.27735v1 | SRC-ARXIV@arXiv:2607.27735v1 | https://arxiv.org/html/2607.27735v1#Sx3 — Methodology | https://arxiv.org/html/2607.27735v1#Sx4.SSx3 — Ablation Study and Sensitivity Analysis; https://arxiv.org/html/2607.27735v1#Sx2.SSx2 — Unified Speedup Analysis | https://arxiv.org/html/2607.27735v1#Sx6 — Conclusion; https://arxiv.org/html/2607.27735v1#Sx7 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27735 | complete |
| SF-2026-ARXIV-2607-27773 | RP-b2bbbf25fdde29b0 | standard | arXiv:2607.27773v1 | SRC-ARXIV@arXiv:2607.27773v1 | https://arxiv.org/html/2607.27773v1#S3 — 3. System Design of ChronoMem: The Natural Language “Undo” Button of Agent Memory; https://arxiv.org/html/2607.27773v1#S3.SS2 — 3.2. Architecture Overview | https://arxiv.org/html/2607.27773v1#S2.SS3 — 2.3. Memory Retrieval and Evaluation; https://arxiv.org/html/2607.27773v1#S4 — 4. Experiment Setup | https://arxiv.org/html/2607.27773v1#S6 — 6. Conclusion; https://arxiv.org/html/2607.27773v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27773 | complete |
| SF-2026-ARXIV-2607-27782 | RP-d8a7cd216a243be1 | standard | arXiv:2607.27782v1 | SRC-ARXIV@arXiv:2607.27782v1 | https://arxiv.org/html/2607.27782v1#S3 — 3 Methodology; https://arxiv.org/html/2607.27782v1#A3 — Appendix C Simulation Implementation Details | https://arxiv.org/html/2607.27782v1#S4 — 4 Experiment; https://arxiv.org/html/2607.27782v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.27782v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.27782v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27782 | complete |
| SF-2026-ARXIV-2607-27823 | RP-6fd3b5457d81cd9d | standard | arXiv:2607.27823v1 | SRC-ARXIV@arXiv:2607.27823v1 | https://arxiv.org/html/2607.27823v1#S1 — 1 Introduction; https://arxiv.org/html/2607.27823v1#S2 — 2 Related Work | https://arxiv.org/html/2607.27823v1#S5 — 5 Experiments; https://arxiv.org/html/2607.27823v1#S5.SS5 — 5.5 Ablations and Efficiency | https://arxiv.org/html/2607.27823v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27823 | complete |
| SF-2026-ARXIV-2607-27830 | RP-2daec23b22843ebc | standard | arXiv:2607.27830v1 | SRC-ARXIV@arXiv:2607.27830v1 | https://arxiv.org/html/2607.27830v1#Sx3.SSx4 — 3.4. From Analysis to Design Principles; https://arxiv.org/html/2607.27830v1#Sx4 — 4. Methodology | https://arxiv.org/html/2607.27830v1#as1_A4 — Appendix D Supplementary Evaluation Results; https://arxiv.org/html/2607.27830v1#Sx3 — 3. Observations and Analysis | https://arxiv.org/html/2607.27830v1#Sx6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27830 | complete |
| SF-2026-ARXIV-2607-27834 | RP-be26101cc4cc09f9 | standard | arXiv:2607.27834v1 | SRC-ARXIV@arXiv:2607.27834v1 | https://arxiv.org/html/2607.27834v1#Sx3 — Method; https://arxiv.org/html/2607.27834v1#Sx3.SSx2 — System model and trust boundary | https://arxiv.org/html/2607.27834v1#Sx4 — Experiments; https://arxiv.org/html/2607.27834v1#Sx4.SSx1 — Evaluation Overview | https://arxiv.org/html/2607.27834v1#Sx5 — Discussion and Limitations; https://arxiv.org/html/2607.27834v1#Sx6 — Conclusion | Exact v1 links https://github.com/langchain-ai/langmem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27834 | complete |
| SF-2026-ARXIV-2607-27842 | RP-36af56886d162809 | standard | arXiv:2607.27842v1 | SRC-ARXIV@arXiv:2607.27842v1 | https://arxiv.org/html/2607.27842v1#Sx3 — Method; https://arxiv.org/html/2607.27842v1#Sx3.SSx3 — FeatFix Framework | https://arxiv.org/html/2607.27842v1#Sx4 — Experiments; https://arxiv.org/html/2607.27842v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.27842v1#Sx5 — Limitations; https://arxiv.org/html/2607.27842v1#Sx6 — Conclusion | Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/vipshop/cache-dit, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27842 | complete |
| SF-2026-ARXIV-2607-27871 | RP-7f51d837c955e30c | standard | arXiv:2607.27871v1 | SRC-ARXIV@arXiv:2607.27871v1 | https://arxiv.org/html/2607.27871v1#Sx7.SSx2 — A Location Model for Heuristic Error | https://arxiv.org/html/2607.27871v1#Sx1 — Introduction; https://arxiv.org/html/2607.27871v1#Sx2 — Preliminaries | https://arxiv.org/html/2607.27871v1#Sx10 — Conclusion; https://arxiv.org/html/2607.27871v1#Sx9 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27871 | complete |
| SF-2026-ARXIV-2607-27877 | RP-f551822d4d08c7fe | standard | arXiv:2607.27877v1 | SRC-ARXIV@arXiv:2607.27877v1 | https://arxiv.org/html/2607.27877v1#Sx12 — TAgent Verification Methodology; https://arxiv.org/html/2607.27877v1#Sx3 — Methodology | https://arxiv.org/html/2607.27877v1#Sx2.SSx2 — Multi-Agent Benchmarks; https://arxiv.org/html/2607.27877v1#Sx3.SSx1 — Benchmark Framework Overview | https://arxiv.org/html/2607.27877v1#Sx4.SSx4 — A General Failure Taxonomy; https://arxiv.org/html/2607.27877v1#Sx5 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27877 | complete |
| SF-2026-ARXIV-2607-27910 | RP-e5174356fcc82a5d | standard | arXiv:2607.27910v1 | SRC-ARXIV@arXiv:2607.27910v1 | https://arxiv.org/html/2607.27910v1#S3 — 3 Method; https://arxiv.org/html/2607.27910v1#A7 — Appendix G Cross-model direction transfer | https://arxiv.org/html/2607.27910v1#A3.SS2 — C.2 Mechanistic ablation versus prompt-level instruction; https://arxiv.org/html/2607.27910v1#A8 — Appendix H Probe-regime analysis: where the attack signal lives | https://arxiv.org/html/2607.27910v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27910 | complete |
| SF-2026-ARXIV-2607-27912 | RP-a17ad997ee4e1afc | standard | arXiv:2607.27912v1 | SRC-ARXIV@arXiv:2607.27912v1 | https://arxiv.org/html/2607.27912v1#S1 — 1 Introduction; https://arxiv.org/html/2607.27912v1#S2 — 2 Related Work | https://arxiv.org/html/2607.27912v1#S2.SS2 — 2.2 Instruction-Following Benchmarks; https://arxiv.org/html/2607.27912v1#S5 — 5 Experiments | https://arxiv.org/html/2607.27912v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.27912v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27912 | complete |
| SF-2026-ARXIV-2607-27928 | RP-60fd60b3262ad9b8 | standard | arXiv:2607.27928v1 | SRC-ARXIV@arXiv:2607.27928v1 | https://arxiv.org/html/2607.27928v1#S2 — 2 Methods; https://arxiv.org/html/2607.27928v1#S2.SS2 — 2.2 Bayesian Domain Reweighting Framework | https://arxiv.org/html/2607.27928v1#A5 — Appendix E Detailed Evaluation Benchmark Information; https://arxiv.org/html/2607.27928v1#S3 — 3 Experimental Results | https://arxiv.org/html/2607.27928v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27928 | complete |
| SF-2026-ARXIV-2607-27933 | RP-98348cb56c92982a | standard | arXiv:2607.27933v1 | SRC-ARXIV@arXiv:2607.27933v1 | https://arxiv.org/html/2607.27933v1#S4.SS2 — 4.2 Method; https://arxiv.org/html/2607.27933v1#A5 — Appendix E Toy Model Implementation Details | https://arxiv.org/html/2607.27933v1#A6 — Appendix F Failure-Detection Experimental Details; https://arxiv.org/html/2607.27933v1#A7 — Appendix G Ablation Study on Failure Detection | https://arxiv.org/html/2607.27933v1#A1.SS1 — A.1 How Works as a Failure Score?; https://arxiv.org/html/2607.27933v1#A6 — Appendix F Failure-Detection Experimental Details | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27933 | complete |
| SF-2026-ARXIV-2607-27951 | RP-dde4dfcee64ee769 | standard | arXiv:2607.27951v1 | SRC-ARXIV@arXiv:2607.27951v1 | https://arxiv.org/html/2607.27951v1#S3.SS7 — 3.7 Design Implications | https://arxiv.org/html/2607.27951v1#S3 — 3 Main Result | https://arxiv.org/html/2607.27951v1#S5 — 5 Limitations; https://arxiv.org/html/2607.27951v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27951 | complete |
| SF-2026-ARXIV-2607-27967 | RP-cff5313c12b25c24 | standard | arXiv:2607.27967v1 | SRC-ARXIV@arXiv:2607.27967v1 | https://arxiv.org/html/2607.27967v1#S5 — 5 Method | https://arxiv.org/html/2607.27967v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.27967v1#A4 — Appendix D Experiments on Overcooked and Pistonball | https://arxiv.org/html/2607.27967v1#S10 — 10 Limitations; https://arxiv.org/html/2607.27967v1#S9 — 9 Conclusion | Exact v1 links https://github.com/Vector-Wangel/XLeRobot, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-27967 | complete |
| SF-2026-ARXIV-2607-28027 | RP-02b556db960c52eb | standard | arXiv:2607.28027v1 | SRC-ARXIV@arXiv:2607.28027v1 | https://arxiv.org/html/2607.28027v1#A1 — Appendix A Model 1 — Rebellion (reproduced); https://arxiv.org/html/2607.28027v1#A1.SS1 — A.1 VISA Specification — Rebellion Model (Exp1) | https://arxiv.org/html/2607.28027v1#S5 — 5 Empirical Evaluation | https://arxiv.org/html/2607.28027v1#S6 — 6 Discussion; https://arxiv.org/html/2607.28027v1#S7 — 7 Conclusion | Exact v1 links https://github.com/AgentLabCn/visa, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28027 | complete |
| SF-2026-ARXIV-2607-28037 | RP-395632cf4ed0d68b | standard | arXiv:2607.28037v1 | SRC-ARXIV@arXiv:2607.28037v1 | https://arxiv.org/html/2607.28037v1#A4.SS1 — D.1. Process Grader System Prompt; https://arxiv.org/html/2607.28037v1#A4.SS2 — D.2. Outcome Grader System Prompt | https://arxiv.org/html/2607.28037v1#A4 — Appendix D Evaluation Prompts; https://arxiv.org/html/2607.28037v1#A5 — Appendix E Extended Results | https://arxiv.org/html/2607.28037v1#A1 — Appendix A Limitations and Broader Impacts; https://arxiv.org/html/2607.28037v1#S5 — 5. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28037 | complete |
| SF-2026-ARXIV-2607-28069 | RP-f78ca22cd736dc00 | standard | arXiv:2607.28069v1 | SRC-ARXIV@arXiv:2607.28069v1 | https://arxiv.org/html/2607.28069v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28069v1#S2 — 2 Background: Position-Independent Caching | https://arxiv.org/html/2607.28069v1#A4 — Appendix D Evaluation Details; https://arxiv.org/html/2607.28069v1#S4 — 4 Motivating Analysis: Boundary Conditioning Leaves an Interior Gap | https://arxiv.org/html/2607.28069v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/datasets/alex-karev/biographies, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28069 | complete |
| SF-2026-ARXIV-2607-28103 | RP-e7e2595d69a76ab3 | standard | arXiv:2607.28103v1 | SRC-ARXIV@arXiv:2607.28103v1 | https://arxiv.org/html/2607.28103v1#S4 — 4 Methodology; https://arxiv.org/html/2607.28103v1#S3.SS2 — 3.2 Threat Model | https://arxiv.org/html/2607.28103v1#S5 — 5 Experiments; https://arxiv.org/html/2607.28103v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.28103v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.28103v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28103 | complete |
| SF-2026-ARXIV-2607-28150 | RP-39482c5f23fc260a | standard | arXiv:2607.28150v1 | SRC-ARXIV@arXiv:2607.28150v1 | https://arxiv.org/html/2607.28150v1#S4 — 4 The SmartGen Design; https://arxiv.org/html/2607.28150v1#S6.SS1 — 6.1 LLM Inference Systems | https://arxiv.org/html/2607.28150v1#S3 — 3 Analysis of KV Cache Transfer; https://arxiv.org/html/2607.28150v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.28150v1#S4.SS4 — 4.4 Discussions; https://arxiv.org/html/2607.28150v1#S7 — 7 Conclusion | Exact v1 links https://github.com/deepseek-ai/DeepSeek-V3.2-Exp/blob/main/DeepSeek_V3_2.pdf, https://www.microsoft.com/en-us/research/project/minference-million-tokens-prompt-inference-for-long-context-llms, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28150 | complete |
| SF-2026-ARXIV-2607-28165 | RP-de003d147935e8a3 | standard | arXiv:2607.28165v1 | SRC-ARXIV@arXiv:2607.28165v1 | https://arxiv.org/html/2607.28165v1#S4 — IV. Attack Framework and Benchmark Design; https://arxiv.org/html/2607.28165v1#S5 — V. Detection Methods and Defense Framework | https://arxiv.org/html/2607.28165v1#A3 — Appendix C Details of Attack Evaluation; https://arxiv.org/html/2607.28165v1#S4 — IV. Attack Framework and Benchmark Design | https://arxiv.org/html/2607.28165v1#S10 — X. Conclusion; https://arxiv.org/html/2607.28165v1#S3 — III. Threat Model | Exact v1 links https://github.com/Limax666/AudioAgentSecurity, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28165 | complete |
| SF-2026-ARXIV-2607-28223 | RP-a679bf53c9c1e0c2 | standard | arXiv:2607.28223v1 | SRC-ARXIV@arXiv:2607.28223v1 | https://arxiv.org/html/2607.28223v1#S2.SS1 — 2.1. GPU Cluster Admission Architecture; https://arxiv.org/html/2607.28223v1#S3.SS1 — 3.1. System Definition | https://arxiv.org/html/2607.28223v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.28223v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.28223v1#S7 — 7. Limitations; https://arxiv.org/html/2607.28223v1#S8 — 8. Discussion and Open Problems | Exact v1 links https://github.com/kubernetes-sigs/kueue/issues/13159, https://github.com/kubernetes-sigs/kueue/issues/10124, https://github.com/kubernetes-sigs/kueue/issues/10614; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28223 | complete |
| SF-2026-ARXIV-2607-28225 | RP-aebc4e86e0e657ea | standard | arXiv:2607.28225v1 | SRC-ARXIV@arXiv:2607.28225v1 | https://arxiv.org/html/2607.28225v1#S3 — 3 Method; https://arxiv.org/html/2607.28225v1#S3.SS2 — 3.2 FaithEyes : multi-agent self-judging framework | https://arxiv.org/html/2607.28225v1#A4 — Appendix D Training stage ablation; https://arxiv.org/html/2607.28225v1#S3.SS1 — 3.1 Preliminaries and analysis | https://arxiv.org/html/2607.28225v1#S5 — 5 Conclusion | Exact v1 links https://github.com/Mosi-AI/FaithEyes, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28225 | complete |
| SF-2026-ARXIV-2607-28282 | RP-b4a746d3dba03727 | standard | arXiv:2607.28282v1 | SRC-ARXIV@arXiv:2607.28282v1 | https://arxiv.org/html/2607.28282v1#S2.SS2 — 2.2 Elo Rating System for Ranking Items; https://arxiv.org/html/2607.28282v1#S4 — 4 Approach | https://arxiv.org/html/2607.28282v1#S6.SS3 — 6.3 Results and Analysis; https://arxiv.org/html/2607.28282v1#S4.SS3 — 4.3 Handling Multiple Evaluations and Agreement Thresholds | https://arxiv.org/html/2607.28282v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.28282v1#S8 — 8 Limitations | Exact v1 links https://github.com/features/copilot, https://www.aclweb.org/portal/content/acl-code-ethics, https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28282 | complete |
| SF-2026-ARXIV-2607-28317 | RP-7837fe6227dfa267 | standard | arXiv:2607.28317v1 | SRC-ARXIV@arXiv:2607.28317v1 | https://arxiv.org/html/2607.28317v1#S12 — 12 H2 in the synthetic model; robustness to the copula choice; https://arxiv.org/html/2607.28317v1#S3 — 3 Model | https://arxiv.org/html/2607.28317v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28317v1#S2 — 2 Related Work | https://arxiv.org/html/2607.28317v1#S14 — 14 Confidence parse failures and imputation; https://arxiv.org/html/2607.28317v1#S15 — 15 Limitation support values | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28317 | complete |
| SF-2026-ARXIV-2607-28336 | RP-5e9ff5a0c0469d00 | standard | arXiv:2607.28336v1 | SRC-ARXIV@arXiv:2607.28336v1 | https://arxiv.org/html/2607.28336v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28336v1#S2 — 2 Related Work | https://arxiv.org/html/2607.28336v1#S4 — 4 Experiments; https://arxiv.org/html/2607.28336v1#S4.SS1 — 4.1 Experimental setup | https://arxiv.org/html/2607.28336v1#S4.SS5 — 4.5 Limitations and Threats to Validity; https://arxiv.org/html/2607.28336v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28336 | complete |
| SF-2026-ARXIV-2607-28367 | RP-ddd9649043dad670 | standard | arXiv:2607.28367v1 | SRC-ARXIV@arXiv:2607.28367v1 | https://arxiv.org/html/2607.28367v1#S2 — 2 Evaluation Reliability Framework; https://arxiv.org/html/2607.28367v1#S5 — 5 Designing Reliable Benchmarks | https://arxiv.org/html/2607.28367v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.28367v1#A3.SS3 — C.3 Dynamic Benchmarks | https://arxiv.org/html/2607.28367v1#A2 — Appendix B Failure-Taxonomy Details; https://arxiv.org/html/2607.28367v1#A3 — Appendix C Future-Direction Details | Exact v1 links https://github.com/Zdong104/CADWORLD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28367 | complete |
| SF-2026-ARXIV-2607-28399 | RP-e44858e7931166f9 | standard | arXiv:2607.28399v1 | SRC-ARXIV@arXiv:2607.28399v1 | https://arxiv.org/html/2607.28399v1#S16 — 16 Method details moved from the main text; https://arxiv.org/html/2607.28399v1#S11 — 11 Per-model serving provenance | https://arxiv.org/html/2607.28399v1#S18 — 18 Additional results detail; https://arxiv.org/html/2607.28399v1#S4 — 4 Experimental setup | https://arxiv.org/html/2607.28399v1#S19 — 19 Full limitations register; https://arxiv.org/html/2607.28399v1#S6 — 6 Discussion | Exact v1 links https://huggingface.co/Hcompany/Holo-3.1-35B-A3B, https://huggingface.co/inclusionAI/UI-Venus-1.5-30B-A3B, https://huggingface.co/meituan/EvoCUA-32B-20260105; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28399 | complete |
| SF-2026-ARXIV-2607-28415 | RP-19edae521c215fe4 | standard | arXiv:2607.28415v1 | SRC-ARXIV@arXiv:2607.28415v1 | https://arxiv.org/html/2607.28415v1#S3 — 3 Method; https://arxiv.org/html/2607.28415v1#S2.SS1 — 2.1 Latent World Models for Planning | https://arxiv.org/html/2607.28415v1#S4 — 4 Experiments; https://arxiv.org/html/2607.28415v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.28415v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28415 | complete |
| SF-2026-ARXIV-2607-28418 | RP-0ebbaa693ff481a0 | standard | arXiv:2607.28418v1 | SRC-ARXIV@arXiv:2607.28418v1 | https://arxiv.org/html/2607.28418v1#S3 — 3 WIDE: Preliminary, Training, and Inference Design; https://arxiv.org/html/2607.28418v1#A1 — Appendix A The Cost for Naive Gather-Scatter Implementations | https://arxiv.org/html/2607.28418v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.28418v1#S4 — 4 Experiments | https://arxiv.org/html/2607.28418v1#S5 — 5 Conclusion | Exact v1 links https://github.com/EIT-NLP/LLM-Pruning/tree/main/WIDE, https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28418 | complete |
| SF-2026-ARXIV-2607-28443 | RP-0da0d2cb97d06939 | standard | arXiv:2607.28443v1 | SRC-ARXIV@arXiv:2607.28443v1 | https://arxiv.org/html/2607.28443v1#S1 — I Introduction; https://arxiv.org/html/2607.28443v1#S2 — II Related Work | https://arxiv.org/html/2607.28443v1#S5 — V Experimental Protocol; https://arxiv.org/html/2607.28443v1#S6 — VI Results | https://arxiv.org/html/2607.28443v1#S7 — VII Discussion and Limitations; https://arxiv.org/html/2607.28443v1#S4.SS2 — IV-B One variable-size future target | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28443 | complete |
| SF-2026-ARXIV-2607-28495 | RP-6285ee6c8cace400 | deep | arXiv:2607.28495v1 | SRC-ARXIV@arXiv:2607.28495v1 | https://arxiv.org/html/2607.28495v1#S3.SS1 — 3.1 Token, role, mask, and replay-boundary contract; https://arxiv.org/html/2607.28495v1#S3.SS2 — 3.2 Models and evaluation set | https://arxiv.org/html/2607.28495v1#S3.SS6 — 3.6 Experiment 4: bidirectional KV-cache transplantation; https://arxiv.org/html/2607.28495v1#S4 — 4 Results | https://arxiv.org/html/2607.28495v1#S6 — 6 Limitations and Threats to Validity; https://arxiv.org/html/2607.28495v1#S7 — 7 Conclusion | Not Disclosed — exact v1 reports saved-ledger and cache-transplant controls but does not bind them to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-28495 | complete |
| SF-2026-ARXIV-2607-28545 | RP-8e40a95b14f2248e | standard | arXiv:2607.28545v1 | SRC-ARXIV@arXiv:2607.28545v1 | https://arxiv.org/html/2607.28545v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28545v1#S2 — 2 Related Work | https://arxiv.org/html/2607.28545v1#A11 — Appendix K Additional Experiments; https://arxiv.org/html/2607.28545v1#A7.SS1 — G.1 Evaluation Prompts | https://arxiv.org/html/2607.28545v1#A2.SS1 — B.1 Example: Product Catalog Failure; https://arxiv.org/html/2607.28545v1#A2.SS2 — B.2 Example: Recommendation Cache Failure | Exact v1 links https://github.com/open-telemetry/opentelemetry-demo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28545 | complete |
| SF-2026-ARXIV-2607-28573 | RP-a17c971fd5e56ff0 | standard | arXiv:2607.28573v1 | SRC-ARXIV@arXiv:2607.28573v1 | https://arxiv.org/html/2607.28573v1#S3 — 3 Methodology | https://arxiv.org/html/2607.28573v1#S3.SS4 — 3.4 Experimental Setup; https://arxiv.org/html/2607.28573v1#S4 — 4 Results | https://arxiv.org/html/2607.28573v1#S5 — 5 Discussion; https://arxiv.org/html/2607.28573v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28573 | complete |
| SF-2026-ARXIV-2607-28576 | RP-04f86c92dcf39c59 | deep | arXiv:2607.28576v1 | SRC-ARXIV@arXiv:2607.28576v1 | https://arxiv.org/html/2607.28576v1#S4.SS3 — 4.3 Methods compared; https://arxiv.org/html/2607.28576v1#S5.SS1 — 5.1 Does any method beat the sampling baseline at equal cost? | https://arxiv.org/html/2607.28576v1#A1.SS4 — A.4 A failure that would have biased the results; https://arxiv.org/html/2607.28576v1#S4 — 4 Experimental setup | https://arxiv.org/html/2607.28576v1#A1.SS4 — A.4 A failure that would have biased the results; https://arxiv.org/html/2607.28576v1#S4.SS7 — 4.7 Threats to validity | Exact v1 links https://github.com/ggml-org/llama.cpp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28576 | complete |
| SF-2026-ARXIV-2607-28591 | RP-f76c74d2f41d7b01 | standard | arXiv:2607.28591v1 | SRC-ARXIV@arXiv:2607.28591v1 | https://arxiv.org/html/2607.28591v1#Sx3 — Methodology; https://arxiv.org/html/2607.28591v1#A9.SS2 — I.2 Bug Fix with a Modernized Implementation | https://arxiv.org/html/2607.28591v1#Sx4 — Experiments; https://arxiv.org/html/2607.28591v1#Sx4.SSx1 — Experiment Setup | https://arxiv.org/html/2607.28591v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.28591v1#Sx5 — Conclusion and Outlook | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28591 | complete |
| SF-2026-ARXIV-2607-28609 | RP-0a03ed2c2cf3f316 | standard | arXiv:2607.28609v1 | SRC-ARXIV@arXiv:2607.28609v1 | https://arxiv.org/html/2607.28609v1#A3.SS1 — C.1. Evaluated Models; https://arxiv.org/html/2607.28609v1#S6 — 6. OS-Shepherd: An Open Reward Model | https://arxiv.org/html/2607.28609v1#A5 — Appendix E Additional Results and Analysis; https://arxiv.org/html/2607.28609v1#A3 — Appendix C Experimental Details | https://arxiv.org/html/2607.28609v1#A2.SS3 — B.3. Failure-Type Taxonomy; https://arxiv.org/html/2607.28609v1#S8 — 8. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28609 | complete |
| SF-2026-ARXIV-2607-28617 | RP-a13582f1266eb5c2 | standard | arXiv:2607.28617v1 | SRC-ARXIV@arXiv:2607.28617v1 | https://arxiv.org/html/2607.28617v1#S2 — 2 What is a System Prompt and Why We Need System Prompt Auditing; https://arxiv.org/html/2607.28617v1#S3 — 3 AISPA : A Taxonomy for User-Centric System Prompt Auditing | https://arxiv.org/html/2607.28617v1#S5.SS2 — 5.2 Results | https://arxiv.org/html/2607.28617v1#S10 — 10 Limitations; https://arxiv.org/html/2607.28617v1#S8 — 8 Conclusion | Exact v1 links https://github.com/0xeb/TheBigPromptLibrary, https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools, https://github.com/asgeirtj/system_prompts_leaks; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28617 | complete |
| SF-2026-ARXIV-2607-28624 | RP-b16c47f9232374ec | standard | arXiv:2607.28624v1 | SRC-ARXIV@arXiv:2607.28624v1 | https://arxiv.org/html/2607.28624v1#S3 — 3 Method; https://arxiv.org/html/2607.28624v1#A3.SS1 — C.1 Controllable and Interactive World Model | https://arxiv.org/html/2607.28624v1#A2 — 附录 B Additional Evaluation Details; https://arxiv.org/html/2607.28624v1#A2.SS1 — B.1 Physical Video Generation Evaluation | https://arxiv.org/html/2607.28624v1#A5 — 附录 E Limitations and Future Work; https://arxiv.org/html/2607.28624v1#S5 — 5 Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-28624 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-27230:start -->
### Multi-Head Attention Residuals

<!-- claim:SF-2026-ARXIV-2607-27230:start -->Transformers propagate information across depth through a single additive residual stream: every sublayer reads only the most recent state. Attention residuals relax this by letting each sublayer attend, through a learned softmax. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27230:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformers propagate information across depth through a single additive residual stream: every sublayer reads only the most recent state.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** It achieves the best result among four methods in every setting, with the gain increasing from 100M to the larger scales.

**证据证明什么。** It achieves the best result among four methods in every setting, with the gain increasing from 100M to the larger scales.

**证据没有证明什么。** Setting the number of routing heads equal to the number of KV heads is a near-optimal, hyperparameter-free default (aligning routing to attention head groups adds nothing measurable; Appendix D ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27230v1#S2 — 2 Method: Multi-Head Attention Residuals。Evaluation：https://arxiv.org/html/2607.27230v1#S3 — 3 Experiments; https://arxiv.org/html/2607.27230v1#S4 — 4 Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.27230v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/HuggingFaceFW/finepdfs, https://huggingface.co/datasets/HuggingFaceTB/stack-edu, https://huggingface.co/marin-community/marin-8b-base; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Setting the number of routing heads equal to the number of KV heads is a near-optimal, hyperparameter-free default (aligning routing to attention head groups adds nothing measurable; Appendix D ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27230:end -->

<!-- review:SF-2026-ARXIV-2607-27231:start -->
### KernelGenBench: A Multi-Source and Multi-Chip Benchmark for LLM-based Kernel Generation

<!-- claim:SF-2026-ARXIV-2607-27231:start -->Large language models (LLMs) have significantly increased the demand for efficient accelerator kernels, but kernel development remains a highly specialized and labor-intensive task. The recent rise of LLMs and agentic frameworks offers a promising pathway toward automatic kernel generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27231:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) have significantly increased the demand for efficient accelerator kernels, but kernel development remains a highly specialized and labor-intensive task.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present KernelGenBench, a unified benchmark for systematically evaluating LLM- and agent-generated Triton kernels across diverse operator sources and heterogeneous hardware platforms.

**证据证明什么。** Our large-scale evaluation, consuming over 15 billion tokens, shows: (1) agent-based methods consistently outperform pure LLM sampling methods, while cuBLAS operators are the most challenging across all methods; (2) generation performance varies significantly across hardware platforms, with even recent kernel-specialized agents experiencing severe cross-platform degradation (e.g., AutoKernel drops from 87% on NVIDIA to 25% on Platform E); (3) autonomous kernel generation remains highly cost-intensive, with specialized agent methods averaging 5.11 million tokens per successful operator (AKO4all reaches 5.19 million), orders of magnitude higher than simple LLM sampling approaches.

**证据没有证明什么。** We categorize current evaluation limitations along these two dimensions: Single-source constraints. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27231v1#A1 — Appendix A Prompt Design; https://arxiv.org/html/2607.27231v1#S3.SS3 — 3.3 Evaluation Framework。Evaluation：https://arxiv.org/html/2607.27231v1#A9 — Appendix I Fast p Evaluation and Cost Results; https://arxiv.org/html/2607.27231v1#S4 — 4 Experiments and Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.27231v1#A11 — Appendix K Platform-Specific Failure Patterns; https://arxiv.org/html/2607.27231v1#S2.SS2 — 2.2 Limitations of Existing Benchmarks。

**Artifact boundary。** Exact v1 links https://github.com/flagos-ai/KernelGenBench, https://github.com/meta-pytorch/tritonbench, https://huggingface.co/facebook/KernelLLM; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We categorize current evaluation limitations along these two dimensions: Single-source constraints.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27231:end -->

<!-- review:SF-2026-ARXIV-2607-27240:start -->
### Asymmetric Collapse in Model Merging: When Refusal Over- writes Recognition

<!-- claim:SF-2026-ARXIV-2607-27240:start -->Model merging is often used to combine capabilities from separately fine-tuned models without additional training, but it is unclear whether standard merging methods preserve multiple safety-relevant behaviors simultaneously. We study this question through a controlled case study using two Gemma-3-1B-IT finetunes on two complementary safety objectives: CARES harm-level classification and WildJailbreak adversarial refusal. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27240:end -->

**为什么进入候选分母。** 摘要首要问题为“Model merging is often used to combine capabilities from separately fine-tuned models without additional training, but it is unclear whether standard merging methods preserve multiple safety-relevant behaviors simultaneously.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Instead, the refusal fine-tune induces consistently larger per-layer task-vector magnitudes, causing magnitude-sensitive methods to favor refusal updates.

**证据证明什么。** These results show that standard model merging can collapse safety recognition into broad refusal when safety-relevant task vectors differ substantially in scale.

**证据没有证明什么。** Future safety-oriented merging methods should therefore account not only for task-vector direction and sparsity, but also for behavioral role, scale imbalance, and the need to preserve fine-grained recognition alongside refusal. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27240v1#A2.SS0.SSS0.Px1 — Method; https://arxiv.org/html/2607.27240v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.27240v1#S3 — 3 Experimentation and Results; https://arxiv.org/html/2607.27240v1#S2.SS0.SSS0.Px3 — Merge configuration and evaluation.。Limitations / counterevidence：https://arxiv.org/html/2607.27240v1#S4 — 4 Limitations and Future Work; https://arxiv.org/html/2607.27240v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future safety-oriented merging methods should therefore account not only for task-vector direction and sparsity, but also for behavioral role, scale imbalance, and the need to preserve fine-grained recognition alongside refusal.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27240:end -->

<!-- review:SF-2026-ARXIV-2607-27248:start -->
### Divergence Decoding: Training-Free Capability Fusion

<!-- claim:SF-2026-ARXIV-2607-27248:start -->While large language models excel in reasoning, these generalists often lack knowledge for specialized scientific domains. Conversely, domain models~(specialists), while knowledgeable, suffer from specialization side-effects including diminished logic and reduced robustness.To address this dilemma, we introduce Divergence Decoding, a training-free framework for capability fusion. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27248:end -->

**为什么进入候选分母。** 摘要首要问题为“While large language models excel in reasoning, these generalists often lack knowledge for specialized scientific domains.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Conversely, domain models~(specialists), while knowledgeable, suffer from specialization side-effects including diminished logic and reduced robustness.To address this dilemma, we introduce Divergence Decoding, a training-free framework for capability fusion.

**证据证明什么。** Experimental results demonstrate that Divergence Decoding outperforms both the domain-specialized and general-purpose models, effectively surpassing the performance of most single-model baseline.

**证据没有证明什么。** By formulating decoding as a state-dependent routing process, our method adaptively transfers control based on -divergence, enabling precise token-level integration without the need for additional fine-tuning or supervision. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27248v1#S3 — 3 Method; https://arxiv.org/html/2607.27248v1#A2 — Appendix B Implementation Details.。Evaluation：https://arxiv.org/html/2607.27248v1#S4 — 4 Main Experiments on Scientific Benchmarks; https://arxiv.org/html/2607.27248v1#A1 — Appendix A Theoretical Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.27248v1#A7 — Appendix G Limitations and Broader Impacts; https://arxiv.org/html/2607.27248v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/think-a-tron/raman-01-1.7B, https://github.com/wyattxuanyang/Divergence-Decoding, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：By formulating decoding as a state-dependent routing process, our method adaptively transfers control based on -divergence, enabling precise token-level integration without the need for additional fine-tuning or supervision.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27248:end -->

<!-- review:SF-2026-ARXIV-2607-27250:start -->
### Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories

<!-- claim:SF-2026-ARXIV-2607-27250:start -->Persistent context files (AGENTS.md, CLAUDE.md) are standard practice for guiding AI coding agents, yet evidence for their effectiveness is contradictory. We present a controlled ablation of context-injection strategy across two frontier agents (Claude Code and Codex), 17 real tasks from 3 repositories (15 shared + 2 Codex-only), and 288 evaluated runs with gold-test evaluation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27250:end -->

**为什么进入候选分母。** 摘要首要问题为“Persistent context files (AGENTS.md, CLAUDE.md) are standard practice for guiding AI coding agents, yet evidence for their effectiveness is contradictory.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present a controlled ablation of context-injection strategy across two frontier agents (Claude Code and Codex), 17 real tasks from 3 repositories (15 shared + 2 Codex-only), and 288 evaluated runs with gold-test evaluation.

**证据证明什么。** We further show that borderline task difficulty is agent-specific (Spearman rho=0.75), offering a candidate explanation for prior contradictions: single-agent studies draw tasks from different agents' informative bands.

**证据没有证明什么。** Context-injection strategy does not measurably move correctness (observed effects bounded to 10–15pp via descriptive TOST equivalence; not a powered equivalence claim, § 4.5 ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27250v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.27250v1#A1 — Appendix A Experimental Harness Details; https://arxiv.org/html/2607.27250v1#A2 — Appendix B Per-Task Results。Limitations / counterevidence：https://arxiv.org/html/2607.27250v1#S5 — 5 Discussion; https://arxiv.org/html/2607.27250v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/codeprakhar25/context-files-coding-agents, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Context-injection strategy does not measurably move correctness (observed effects bounded to 10–15pp via descriptive TOST equivalence; not a powered equivalence claim, § 4.5 ).

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27250:end -->

<!-- review:SF-2026-ARXIV-2607-27261:start -->
### It's Not Just More Demos: Counterfactual Action Sensitivity Coverage for Data-Efficient Robust Robot Imitation

<!-- claim:SF-2026-ARXIV-2607-27261:start -->Visuomotor imitation learning has demonstrated success for manipulation tasks. However, the trained policies remain brittle to visual `nuisances', with even minor task-preserving variations such as lighting, distractions or changes in colour result in heavy degradation of the trained policy's performance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27261:end -->

**为什么进入候选分母。** 摘要首要问题为“Visuomotor imitation learning has demonstrated success for manipulation tasks.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Counterfactual Nuisance Behaviour Cloning (CFNBC), an offline data-selection framework for targeted robustness repair.

**证据证明什么。** We show in MuJoCo bimanual cube transfer and SimplerEnv cube stacking that action drift correlates with nuisance-induced failure, and that response-guided repair with only $20$--$30$ selected candidates substantially outperforms matched-budget random selection while approaching the performance of much larger random repair budgets.

**证据没有证明什么。** However, it does not achieve broad robustness; this can be seen in that all single-factor repairs still have worst-case success at , which indicates that the narrow repair leaves at least one nuisance condition unrepaired. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27261v1#A1 — Appendix A CFNBC Algorithm and Implementation Details。Evaluation：https://arxiv.org/html/2607.27261v1#S4 — IV Experiment Setup; https://arxiv.org/html/2607.27261v1#S5 — V Results and Discussion。Limitations / counterevidence：https://arxiv.org/html/2607.27261v1#A3 — Appendix C Narrow repair mainly repairs narrow failure modes; https://arxiv.org/html/2607.27261v1#S5 — V Results and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：However, it does not achieve broad robustness; this can be seen in that all single-factor repairs still have worst-case success at , which indicates that the narrow repair leaves at least one nuisance condition unrepaired.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27261:end -->

<!-- review:SF-2026-ARXIV-2607-27267:start -->
### FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs

<!-- claim:SF-2026-ARXIV-2607-27267:start -->Large language model (LLM) agents autonomously interleave semantic reasoning with complex system operations. In these dynamic environments, static tool-level permissions are fundamentally insufficient; safe authorization is highly context-dependent and heavily reliant on evolving runtime states and data flows. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27267:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents autonomously interleave semantic reasoning with complex system operations.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present FAVA (Formal Authorization for Verified Agents), a permission-carrying authorization framework for agent execution.

**证据证明什么。** Our evaluation demonstrates that FAVA achieves a 90.5% Decision Compliance Rate (DCR) over the aggregate dataset, successfully intercepting dynamic violating traces in the evaluated trace-conditioned scenarios.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27267v1#Sx3 — FAVA Method; https://arxiv.org/html/2607.27267v1#Sx3.SSx6 — Security Assumptions and System Scope。Evaluation：https://arxiv.org/html/2607.27267v1#Sx5 — Experiments; https://arxiv.org/html/2607.27267v1#Sx5.SSx1 — RQ1: Main Permission-Compliance Result。Limitations / counterevidence：https://arxiv.org/html/2607.27267v1#Sx5.SSx5 — RQ5: Failure Analysis; https://arxiv.org/html/2607.27267v1#Sx6 — Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27267:end -->

<!-- review:SF-2026-ARXIV-2607-27269:start -->
### Beyond KV Reconstruction: Functional Reconstruction for MLA Draft Models in Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607-27269:start -->Multi-head latent attention (MLA) is increasingly important for long-context LLM inference because compact latent states replace the growing key-value (KV) cache and reduce decoding memory traffic. Yet most capable open checkpoints use multi-head or grouped-query attention (MHA/GQA), so conversion is needed to obtain MLA's cache efficiency without retraining from scratch. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27269:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-head latent attention (MLA) is increasingly important for long-context LLM inference because compact latent states replace the growing key-value (KV) cache and reduce decoding memory traffic.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We evaluate 192 model-converter-backend-method-task configurations spanning four Llama/Qwen draft-target pairs, TransMLA and MHA2MLA, HF and vLLM, and four 200-prompt tasks.

**证据证明什么。** We find that direct MHA/GQA-to-MLA conversion can sharply reduce this agreement: low-rank factorization and RoPE handling introduce attention-function errors that may be tolerable for standalone generation but substantially lower draft-token acceptance.

**证据没有证明什么。** Although Original GQA is not a theoretical upper bound on target agreement, this empirical gap shows that the current layer-local objective cannot fully overcome fixed-rank information loss or runtime realization errors. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27269v1#Sx4 — Method。Evaluation：https://arxiv.org/html/2607.27269v1#Sx6 — Results and Analysis; https://arxiv.org/html/2607.27269v1#Sx5 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27269v1#Sx7 — Discussion; https://arxiv.org/html/2607.27269v1#Sx8 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Although Original GQA is not a theoretical upper bound on target agreement, this empirical gap shows that the current layer-local objective cannot fully overcome fixed-rank information loss or runtime realization errors.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27269:end -->

<!-- review:SF-2026-ARXIV-2607-27270:start -->
### BMOA: Baseline-Mechanism-Outcome Attribution for Compiler-Induced Numerical Deviations

<!-- claim:SF-2026-ARXIV-2607-27270:start -->Formalizing compiler-aware numerical correctness requires distinguishing what an observed floating-point difference means, what compiler behavior the evidence supports, and what numerical consequence follows. Existing testing workflows often collapse these questions into a pass/fail mismatch. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27270:end -->

**为什么进入候选分母。** 摘要首要问题为“Formalizing compiler-aware numerical correctness requires distinguishing what an observed floating-point difference means, what compiler behavior the evidence supports, and what numerical consequence follows.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce Baseline--Mechanism--Outcome Attribution (BMOA), a diagnostic framework that separates the comparison relation and system boundary, the evidence-supported compiler mechanism, and the reference-qualified accuracy outcome.

**证据证明什么。** A 1,276-record attribution corpus and a 162-instance controlled mechanism matrix show that baseline choice changes diagnoses, compiler-induced deviation does not imply accuracy loss, and cancellation and large dynamic range expose the strongest effects within the targeted matrix.

**证据没有证明什么。** Outcome is relative to a named reference and tolerance, and zero-tolerance ordering is not application severity. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27270v1#S3 — 3. Method; https://arxiv.org/html/2607.27270v1#S4 — 4. Experimental Design。Evaluation：https://arxiv.org/html/2607.27270v1#S4 — 4. Experimental Design; https://arxiv.org/html/2607.27270v1#S5 — 5. Results。Limitations / counterevidence：https://arxiv.org/html/2607.27270v1#S6 — 6. Discussion and Limitations; https://arxiv.org/html/2607.27270v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Outcome is relative to a named reference and tolerance, and zero-tolerance ordering is not application severity.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27270:end -->

<!-- review:SF-2026-ARXIV-2607-27271:start -->
### RLPF: Reinforcement Learning from Performance Feedback for Code Generation

<!-- claim:SF-2026-ARXIV-2607-27271:start -->Code models are increasingly trained with execution feedback, but most training signals still stop at correctness. This leaves an important gap for systems code: two programs can pass the same tests while differing greatly in runtime. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27271:end -->

**为什么进入候选分母。** 摘要首要问题为“Code models are increasingly trained with execution feedback, but most training signals still stop at correctness.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** This leaves an important gap for systems code: two programs can pass the same tests while differing greatly in runtime.

**证据证明什么。** These results suggest that code agents can be trained not only to pass tests, but also to optimize the programs they write.

**证据没有证明什么。** The slight increase in run failures is not a major regression by itself. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27271v1#A6 — Appendix F Model-Generated Performance References; https://arxiv.org/html/2607.27271v1#Sx5.SSx3 — Efficiency training improves model ranking。Evaluation：https://arxiv.org/html/2607.27271v1#Sx4.SSx1 — Benchmarks and Evaluation Protocol; https://arxiv.org/html/2607.27271v1#Sx5 — Experiment Results。Limitations / counterevidence：https://arxiv.org/html/2607.27271v1#A10 — Appendix J Remaining Failure Patterns; https://arxiv.org/html/2607.27271v1#A14 — Appendix N Failure-Stage Counts。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The slight increase in run failures is not a major regression by itself.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27271:end -->

<!-- review:SF-2026-ARXIV-2607-27273:start -->
### SDO: Structure-Aware Data Organization for Efficient LLM Post-Training

<!-- claim:SF-2026-ARXIV-2607-27273:start -->Post-training of large language models is expensive, and existing efficiency improvements mainly focus on selecting informative samples or designing training schedules. However, data organization itself is usually treated as a static preprocessing step: embedding-based grouping methods construct fixed partitions before training and cannot adapt to the evolving sample exposure during optimization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27273:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training of large language models is expensive, and existing efficiency improvements mainly focus on selecting informative samples or designing training schedules.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this problem, we propose SDO (Structure-Aware Data Organization), a plug-and-play data organization framework with an exposure-driven feedback mechanism that organizes mini-batch composition and sample exposure according to representation-space structure.

**证据证明什么。** Post-training of large language models is expensive, and existing efficiency improvements mainly focus on selecting informative samples or designing training schedules.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27273v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.27273v1#Sx4 — Experiments; https://arxiv.org/html/2607.27273v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27273v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27273:end -->

<!-- review:SF-2026-ARXIV-2607-27275:start -->
### Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents

<!-- claim:SF-2026-ARXIV-2607-27275:start -->Post-training quantization to 4-bit weights is widely reported to be nearly lossless. We test this claim for multi-turn, tool-calling agents, where it now matters most. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27275:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training quantization to 4-bit weights is widely reported to be nearly lossless.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We test this claim for multi-turn, tool-calling agents, where it now matters most.

**证据证明什么。** No cell shows a score change that survives multiple-comparison correction, and in the cell that carries the largest process damage, equivalence testing bounds the change within $\pm$7.5 points.

**证据没有证明什么。** Quantization does not make the model imagine new tools; it makes it reach more often for the ones it was already tempted by. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27275v1#Sx1 — Introduction; https://arxiv.org/html/2607.27275v1#Sx2 — Related Work。Evaluation：https://arxiv.org/html/2607.27275v1#A1 — Appendix A Additional Results; https://arxiv.org/html/2607.27275v1#Sx3 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27275v1#A2 — Appendix B Limitations; https://arxiv.org/html/2607.27275v1#Sx4.SSx4 — Quantization Amplifies the Existing Failure Set, Not New Ones。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Quantization does not make the model imagine new tools; it makes it reach more often for the ones it was already tempted by.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27275:end -->

<!-- review:SF-2026-ARXIV-2607-27281:start -->
### The Kinetics of Training: A Driven-Nucleation Rate Law for Emergence, Plasticity Loss, and Circuit Control in Language Models

<!-- claim:SF-2026-ARXIV-2607-27281:start -->A capability appears in a language model when the last parts of its circuit align in one stochastic attempt, and getting all but one right is worth nothing. We show this no-partial-credit joint alignment is the rate-limiting step of capability formation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27281:end -->

**为什么进入候选分母。** 摘要首要问题为“A capability appears in a language model when the last parts of its circuit align in one stochastic attempt, and getting all but one right is worth nothing.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We show this no-partial-credit joint alignment is the rate-limiting step of capability formation.

**证据证明什么。** We show this no-partial-credit joint alignment is the rate-limiting step of capability formation.

**证据没有证明什么。** If barriers add, formation time depends only on the number of missing parts, never on the circuit’s total size: a substrate holding of parts (pre-built by staged curriculum, each stage trained to completion — partially formed parts do not count, a threshold measured in prior work [ 25 ] ) waits only for the remaining to align jointly. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27281v1#S3 — 3 Methods and apparatus; https://arxiv.org/html/2607.27281v1#A1 — Appendix A The occupation theorem: model, assumptions, and full proofs。Evaluation：https://arxiv.org/html/2607.27281v1#S11 — 11 Negative results and reproducibility。Limitations / counterevidence：https://arxiv.org/html/2607.27281v1#S14 — 14 Conclusion; https://arxiv.org/html/2607.27281v1#S4.SS4 — 4.4 Testing the premises, not just the conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：If barriers add, formation time depends only on the number of missing parts, never on the circuit’s total size: a substrate holding of parts (pre-built by staged curriculum, each stage trained to completion — partially formed parts do not count, a threshold measured in prior work [ 25 ] ) waits only for the remaining to align jointly.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27281:end -->

<!-- review:SF-2026-ARXIV-2607-27283:start -->
### Benchmarking the Residual: What Long-Horizon Evaluations Add Beyond Matched Short-Task Performance

<!-- claim:SF-2026-ARXIV-2607-27283:start -->Long-horizon benchmarks often show that agents fail more as tasks become longer. This observation is useful for deployment, but it does not by itself explain why failure occurs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27283:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon benchmarks often show that agents fail more as tasks become longer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This observation is useful for deployment, but it does not by itself explain why failure occurs.

**证据证明什么。** Long-horizon benchmarks often show that agents fail more as tasks become longer.

**证据没有证明什么。** We therefore advocate publishing the decomposition, acceptance conditions, dependency annotations, checkpoint construction, and revealed information, and testing whether conclusions persist across multiple reasonable annotations and both stage-given and goal-only conditions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27283v1#S3 — 3 A System-Matched Counterfactual for Long-Horizon Evaluation; https://arxiv.org/html/2607.27283v1#S5 — 5 A Benchmark Design Protocol for Coding and Terminal Agents。Evaluation：https://arxiv.org/html/2607.27283v1#S3.SS3 — 3.3 The Horizon Residual; https://arxiv.org/html/2607.27283v1#S4 — 4 Separating Task Structure from Local Difficulty。Limitations / counterevidence：https://arxiv.org/html/2607.27283v1#S7 — 7 Scope, Limitations, and Falsifiability; https://arxiv.org/html/2607.27283v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We therefore advocate publishing the decomposition, acceptance conditions, dependency annotations, checkpoint construction, and revealed information, and testing whether conclusions persist across multiple reasonable annotations and both stage-given and goal-only conditions.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27283:end -->

<!-- review:SF-2026-ARXIV-2607-27288:start -->
### Open Security Benchmark: Towards Autonomous Enterprise Cyber Defense

<!-- claim:SF-2026-ARXIV-2607-27288:start -->Enterprises are moving toward autonomous cyber defense: agentic AI that builds situational awareness of an organization's security state and reasons from it to assessments, decisions, and actions. This rests on a holistic view of the enterprise's security state, the continuous, cross-vendor picture of identities, cloud and infrastructure, data, applications, and their configurations that security posture management assembles. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27288:end -->

**为什么进入候选分母。** 摘要首要问题为“Enterprises are moving toward autonomous cyber defense: agentic AI that builds situational awareness of an organization's security state and reasons from it to assessments, decisions, and actions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present Open Security Benchmark (OSB), a framework that benchmarks agentic AI on this work.

**证据证明什么。** We instantiate the framework with two identity-security packs and a family of synthetic-organization environment datasets spanning multiple scales, and chart its extension to further posture subdomains, investigation modalities, and defense stages from assessment toward remediation.

**证据没有证明什么。** One potential utility of OSB is therefore to advance agents, not only to score them: what makes the archive trainable rather than merely readable is that OSB already computes the signal a learner needs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27288v1#S4 — 4 Framework Components; https://arxiv.org/html/2607.27288v1#S4.SS5 — 4.5 Bring Your Own Agent or Model。Evaluation：https://arxiv.org/html/2607.27288v1#S4.SS2 — 4.2 Tasks and Evaluation Sets; https://arxiv.org/html/2607.27288v1#S4.SS3 — 4.3 Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.27288v1#S7 — 7 Discussion; https://arxiv.org/html/2607.27288v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/OpenSecurityAI/benchmark, https://huggingface.co/OpenSecurityAI, https://github.com/nccgroup/ScoutSuite; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：One potential utility of OSB is therefore to advance agents, not only to score them: what makes the archive trainable rather than merely readable is that OSB already computes the signal a learner needs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27288:end -->

<!-- review:SF-2026-ARXIV-2607-27294:start -->
### AgentS4D: Benchmarking Runtime Risks across the Execution Lifecycle of LLM-Based Workspace Agents

<!-- claim:SF-2026-ARXIV-2607-27294:start -->Large language model (LLM)-based workspace agents execute stateful, multi-step workflows across heterogeneous resources, external tools, and persistent state. Their safety must therefore be assessed from actions, side effects, and state changes throughout execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27294:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM)-based workspace agents execute stateful, multi-step workflows across heterogeneous resources, external tools, and persistent state.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce AgentS4D, a sandboxed benchmark for lifecycle-wide runtime safety evaluation.

**证据证明什么。** Evaluations should examine complete agent configurations across diverse risk conditions and retain evidence throughout execution.

**证据没有证明什么。** A.7 Threat-Scope Exclusions The benchmark excludes training-data and weight poisoning, compromise of model-provider systems, unauthorized changes to harness-native tools or protocols, and compromise of production MCP registries or services. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27294v1#A1 — Appendix A Runtime-Safety Framework and Threat Boundaries; https://arxiv.org/html/2607.27294v1#A6.SS1 — F.1 Evaluated Systems and Risk Coverage。Evaluation：https://arxiv.org/html/2607.27294v1#A2 — Appendix B Benchmark Construction and Quality Control; https://arxiv.org/html/2607.27294v1#A2.SS4 — B.4 Benchmark Composition and Coverage。Limitations / counterevidence：https://arxiv.org/html/2607.27294v1#A1 — Appendix A Runtime-Safety Framework and Threat Boundaries; https://arxiv.org/html/2607.27294v1#A1.SS7 — A.7 Threat-Scope Exclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A.7 Threat-Scope Exclusions The benchmark excludes training-data and weight poisoning, compromise of model-provider systems, unauthorized changes to harness-native tools or protocols, and compromise of production MCP registries or services.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27294:end -->

<!-- review:SF-2026-ARXIV-2607-27309:start -->
### SIGIL: Compiling Agent Skills into Typed Harnesses

<!-- claim:SF-2026-ARXIV-2607-27309:start -->Agent skills provide a reusable way to specify multi-step agent behavior, but they remain natural-language specifications interpreted by the model at runtime. As a result, required tool calls, ordering constraints, and checks may be skipped even when explicitly prescribed by the skill. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27309:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent skills provide a reusable way to specify multi-step agent behavior, but they remain natural-language specifications interpreted by the model at runtime.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce Skill Compilation, a paradigm that translates natural-language skills into executable agent programs while preserving model judgment where semantic decisions are required.

**证据证明什么。** These results show that compiling procedural structure improves the reliability and efficiency of skill execution while retaining model judgment where it is needed.

**证据没有证明什么。** The failures are defects, and artifact tests cannot see them. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27309v1#S3.SS1 — 3.1. Design requirements; https://arxiv.org/html/2607.27309v1#S4.SS3 — 4.3. Implementation。Evaluation：https://arxiv.org/html/2607.27309v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.27309v1#S5.SS1 — 5.1. Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.27309v1#S2.SS2 — 2.2. What the failures have in common; https://arxiv.org/html/2607.27309v1#S5.SS7 — 5.7. Threats to validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The failures are defects, and artifact tests cannot see them.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27309:end -->

<!-- review:SF-2026-ARXIV-2607-27353:start -->
### LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation

<!-- claim:SF-2026-ARXIV-2607-27353:start -->Agentic retrieval-augmented generation systems can produce answers that appear grounded while failing at the evidence, tool-contract, authorization, or session-state layer. We introduce LayerRAG-Bench, a controlled cross-layer reliability benchmark with 8 enterprise domains, 240 tasks, 9 fault scenarios, 2 contract modes, and 38,880 live task-level records across nine models from OpenAI, Anthropic, and Gemini. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27353:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic retrieval-augmented generation systems can produce answers that appear grounded while failing at the evidence, tool-contract, authorization, or session-state layer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Agentic retrieval-augmented generation systems can produce answers that appear grounded while failing at the evidence, tool-contract, authorization, or session-state layer.

**证据证明什么。** These results support a layer-specific evaluation principle: a reliability intervention should be credited for repairing its target layer without being mistaken for a universal fix.

**证据没有证明什么。** 7 Limitations and Future Work The corpus is synthetic and policy-like. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27353v1#S2 — 2 Benchmark and Methods; https://arxiv.org/html/2607.27353v1#S2.SS1 — 2.1 Benchmark design and threat model。Evaluation：https://arxiv.org/html/2607.27353v1#A1 — Appendix A Additional Live-Matrix Results; https://arxiv.org/html/2607.27353v1#S2 — 2 Benchmark and Methods。Limitations / counterevidence：https://arxiv.org/html/2607.27353v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.27353v1#S2.SS1 — 2.1 Benchmark design and threat model。

**Artifact boundary。** Exact v1 links https://github.com/MusaShams/layerrag-bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations and Future Work The corpus is synthetic and policy-like.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27353:end -->

<!-- review:SF-2026-ARXIV-2607-27360:start -->
### SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis

<!-- claim:SF-2026-ARXIV-2607-27360:start -->Agent self-evolution has primarily focused on learning how to act, while overlooking an equally important capability: learning to discover what an agent does not know. Existing approaches typically assume that failure discovery is given, focusing on how to repair failures once they are identified. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27360:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent self-evolution has primarily focused on learning how to act, while overlooking an equally important capability: learning to discover what an agent does not know.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose SkillMentor, which trains a Mentor policy via reinforcement learning to generate diagnostic tasks, identify recurrent failure modes, and curate them into reusable corrective skills.

**证据证明什么。** Across AppWorld and BFCLv3, SkillMentor improves executor performance by an average of 44.2%.

**证据没有证明什么。** We hope this work encourages future research on treating diagnosis as a fundamental component of self-evolving agents and on developing dedicated policies that learn what an agent does not know , rather than solely improving how an agent acts . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27360v1#S3 — 3 Method; https://arxiv.org/html/2607.27360v1#S4.SS6 — 4.6 Robustness: How Dependent Is SkillMentor on Strong Models?。Evaluation：https://arxiv.org/html/2607.27360v1#S3.SS3 — 3.3 Gap Evaluation; https://arxiv.org/html/2607.27360v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27360v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We hope this work encourages future research on treating diagnosis as a fundamental component of self-evolving agents and on developing dedicated policies that learn what an agent does not know , rather than solely improving how an agent acts .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27360:end -->

<!-- review:SF-2026-ARXIV-2607-27372:start -->
### Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation

<!-- claim:SF-2026-ARXIV-2607-27372:start -->The deep learning revolution, kicked off by AlexNet, taught us that end-to-end training beats decomposing a problem into hand-designed stages. Generative modeling, however, has remained the exception-despite generative models being remarkably capable, they are still not trained end-to-end. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27372:end -->

**为什么进入候选分母。** 摘要首要问题为“The deep learning revolution, kicked off by AlexNet, taught us that end-to-end training beats decomposing a problem into hand-designed stages.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this work, we introduce Explorative Modeling, a new paradigm that instead factors the training loop, exploring K candidate matches between model generations and data, and training on the best, so predictions commit to modes rather than blurring them.

**证据证明什么。** We find Explorative Models (XMs) useful in two settings.

**证据没有证明什么。** 7 Limitations and Conclusion In this work, we introduced Explorative Modeling, a new paradigm for handling multimodal distributions that factors the training loop instead of the generation procedure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27372v1#A3 — Appendix C Approach Details; https://arxiv.org/html/2607.27372v1#A5.SS3 — E.3 Explorative Modeling Based Methods。Evaluation：https://arxiv.org/html/2607.27372v1#S4 — 4 Experimentation and Results; https://arxiv.org/html/2607.27372v1#A1 — Appendix A Additional Experimentation。Limitations / counterevidence：https://arxiv.org/html/2607.27372v1#S7 — 7 Limitations and Conclusion; https://arxiv.org/html/2607.27372v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/alexiglad/XM, https://github.com/qlabs-eng/slowrun, https://huggingface.co/stabilityai/sd-vae-ft-mse; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：7 Limitations and Conclusion In this work, we introduced Explorative Modeling, a new paradigm for handling multimodal distributions that factors the training loop instead of the generation procedure.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27372:end -->

<!-- review:SF-2026-ARXIV-2607-27383:start -->
### The Convergence Behavior of Adam under Heavy-Tailed Noise

<!-- claim:SF-2026-ARXIV-2607-27383:start -->We establish the first convergence guarantees for the plain vector-form Adam optimizer under heavy-tailed stochastic noise. While several Adam variants are known to achieve optimal iteration complexity in bounded-variance nonsmooth nonconvex optimization, little is understood about their behavior when stochastic gradients admit only a bounded $p$-th central moment for some $p \in (1,2]$, a setting increasingly observed in modern deep learning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27383:end -->

**为什么进入候选分母。** 摘要首要问题为“We establish the first convergence guarantees for the plain vector-form Adam optimizer under heavy-tailed stochastic noise.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Building on this generalized framework, we develop a discounted regret analysis for Adam, without restrictive parameter coupling.

**证据证明什么。** Our results show that Adam converges to $(ρ,ε)$-stationary points under heavy-tailed noise.

**证据没有证明什么。** Together, these ingredients yield -stationarity guarantees under only bounded -th moments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27383v1#S5 — 5 Algorithm: Adam。Evaluation：https://arxiv.org/html/2607.27383v1#S1 — 1 Introduction; https://arxiv.org/html/2607.27383v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.27383v1#S7 — 7 Conclusion and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Together, these ingredients yield -stationarity guarantees under only bounded -th moments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27383:end -->

<!-- review:SF-2026-ARXIV-2607-27386:start -->
### Beyond the Bidirectional Promise: Re-evaluating the Robustness of Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-27386:start -->Diffusion Language Models (DLMs) offer a compelling alternative to autoregressive (AR) generation by enabling bidirectional context and iterative refinement. However, their reliability under natural input noise and adversarial attacks remains under-explored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27386:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion Language Models (DLMs) offer a compelling alternative to autoregressive (AR) generation by enabling bidirectional context and iterative refinement.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Furthermore, DLMs exhibit systematic overconfidence, presenting a practical deployment hazard.

**证据证明什么。** Consistent with this diagnosis, we show that surface-level prompt patching fails to improve over noisy baselines.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27386v1#S5 — 5 Mechanistic Probing Methodology; https://arxiv.org/html/2607.27386v1#A2 — Appendix B IPM Algorithm (Full Pseudocode)。Evaluation：https://arxiv.org/html/2607.27386v1#A7 — Appendix G Full IPM Ablation Results; https://arxiv.org/html/2607.27386v1#A8 — Appendix H Statistical Significance and Question-Only Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.27386v1#A10 — Appendix J Extended Limitations Discussion; https://arxiv.org/html/2607.27386v1#A1 — Appendix A Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27386:end -->

<!-- review:SF-2026-ARXIV-2607-27409:start -->
### SWE-NFI: Studying and Benchmarking Coding Agents for Non-Functional Improvements

<!-- claim:SF-2026-ARXIV-2607-27409:start -->Although coding agents have achieved impressive performance on correctness-oriented benchmarks, their ability to make behavior-preserving non-functional improvements (NFIs) remains underexplored. In real-world software development, developers continuously improve software quality without changing observable behavior, yet existing benchmarks primarily evaluate functional correctness and provide limited support for assessing these non-functional improvements. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27409:end -->

**为什么进入候选分母。** 摘要首要问题为“Although coding agents have achieved impressive performance on correctness-oriented benchmarks, their ability to make behavior-preserving non-functional improvements (NFIs) remains underexplored.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we present SWE-NFI, a benchmark for evaluating coding agents on NFIs beyond functional correctness.

**证据证明什么。** Although coding agents have achieved impressive performance on correctness-oriented benchmarks, their ability to make behavior-preserving non-functional improvements (NFIs) remains underexplored.

**证据没有证明什么。** To mitigate this threat, we only apply NFI scoring to outputs that are valid and pass the task-specific tests. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.27409v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.27409v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.27409v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.27409v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.27409v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.27409v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/openai/codex, https://github.com/asottile/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：To mitigate this threat, we only apply NFI scoring to outputs that are valid and pass the task-specific tests.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27409:end -->

<!-- review:SF-2026-ARXIV-2607-27415:start -->
### Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs

<!-- claim:SF-2026-ARXIV-2607-27415:start -->Recent advancements in inference-time scaling have significantly unlocked the complex reasoning capabilities of Large Language Models~(LLMs). However, for agents, these approaches suffer from a critical inefficiency, operating in a stateless manner and engaging in redundant search processes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27415:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advancements in inference-time scaling have significantly unlocked the complex reasoning capabilities of Large Language Models~(LLMs).”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In this paper, we propose a novel framework, \textit{GAMER}~(Graph-based Action-centric Memory with Episodic Reasoning), that bridges the gap between inference scaling and episodic memory.

**证据证明什么。** Experiments on multiple benchmarks demonstrate that \textit{GAMER} achieves superior performance by \textbf{20.81\%/6.17\%} for success/progress rate compared to vanilla baselines.

**证据没有证明什么。** Addressing this limitation is left for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27415v1#S3 — 3 Methodology; https://arxiv.org/html/2607.27415v1#A3.SS3 — C.3 Implementation。Evaluation：https://arxiv.org/html/2607.27415v1#A2 — Appendix B Proof of Theoretical Analysis; https://arxiv.org/html/2607.27415v1#A3 — Appendix C Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27415v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Addressing this limitation is left for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27415:end -->

<!-- review:SF-2026-ARXIV-2607-27443:start -->
### Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems

<!-- claim:SF-2026-ARXIV-2607-27443:start -->Large Language Model~(LLM)-based agents have demonstrated exceptional performance across a wide range of complex interactive tasks. However, they often struggle with long-horizon interactive tasks common in domains, such as embodied AI. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27443:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model~(LLM)-based agents have demonstrated exceptional performance across a wide range of complex interactive tasks.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We propose \textit{Trajectory Graph Copilot}, a novel framework that acts as a ``copilot'' for LLM agents by diagnosing potential action errors before they are executed.

**证据证明什么。** The extensive experiments on four benchmarks with three LLM agents demonstrate a $14.69\%$ pass ratio improvement on average.

**证据没有证明什么。** The experiments and findings highlight not only the effectiveness of Graph Debugger in detecting errors but also its potential as a general framework for improving decision-making in LLM agents. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27443v1#A3 — Appendix C Detailed Implementation; https://arxiv.org/html/2607.27443v1#A3.SS3 — C.3 Agent Implementation。Evaluation：https://arxiv.org/html/2607.27443v1#S5.SS2 — 5.2 Feedback Evaluation Results; https://arxiv.org/html/2607.27443v1#A4 — Appendix D Extensive Results。Limitations / counterevidence：https://arxiv.org/html/2607.27443v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/OSU-NLP-Group/TravelPlanner, https://github.com/scikit-learn/scikit-learn, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The experiments and findings highlight not only the effectiveness of Graph Debugger in detecting errors but also its potential as a general framework for improving decision-making in LLM agents.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27443:end -->

<!-- review:SF-2026-ARXIV-2607-27480:start -->
### Granite: A Modular Methodology for Foundational Verification of Hardware-Software Leakage Contracts

<!-- claim:SF-2026-ARXIV-2607-27480:start -->Granite is a methodology for modular verification of both functional correctness and nonleakage of RTL processors against ISA contracts. We prove that the cycle-by-cycle timing of a pipelined RISC design--with speculation, precise interrupts, and I/O--is determined solely by observables specified in an ISA leakage contract. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27480:end -->

**为什么进入候选分母。** 摘要首要问题为“Granite is a methodology for modular verification of both functional correctness and nonleakage of RTL processors against ISA contracts.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Granite is a methodology for modular verification of both functional correctness and nonleakage of RTL processors against ISA contracts.

**证据证明什么。** We believe this work is the first to achieve modular and foundational connection between instruction-set-level leakage contracts and microarchitecture-specific cycle-by-cycle execution with wire-level observations.

**证据没有证明什么。** Security Goal and Threat Model We consider HW/SW contracts based on three components: a software or ISA specification with leakage semantics, a hardware or microarchitectural implementation, and an adversary model specifying what aspects of the microarchitecture are observable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27480v1#S1.SS1 — 1.1. Our Approach; https://arxiv.org/html/2607.27480v1#S2.SS4 — 2.4. Specifying Information Flow in Combinational Methods。Evaluation：https://arxiv.org/html/2607.27480v1#S7.SS1 — 7.1. Software Static Analysis; https://arxiv.org/html/2607.27480v1#S6 — 6. Verification Case Study: A Pipelined Processor。Limitations / counterevidence：https://arxiv.org/html/2607.27480v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.27480v1#S3.SS2 — 3.2. Security Goal and Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Security Goal and Threat Model We consider HW/SW contracts based on three components: a software or ISA specification with leakage semantics, a hardware or microarchitectural implementation, and an adversary model specifying what aspects of the microarchitecture are observable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27480:end -->

<!-- review:SF-2026-ARXIV-2607-27484:start -->
### Skill Use or Skill Theater? Evaluating the Reasoning Backroom in Skill-Augmented Language Agents

<!-- claim:SF-2026-ARXIV-2607-27484:start -->Reusable skills are becoming a standard interface for extending language agents with task procedures. Yet evaluators usually infer skill use from visible reasoning or the agent's own attribution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27484:end -->

**为什么进入候选分母。** 摘要首要问题为“Reusable skills are becoming a standard interface for extending language agents with task procedures.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce BACKTRACE, an evaluation framework that pairs each skill-conditioned answer with a matched no-skill counterfactual, intervenes on skill meaning, wording, identity, content, and assignment, and elicits attribution only after the answer is committed.

**证据证明什么。** These signals show what the agent appears to use, not whether the skill changed its decision.

**证据没有证明什么。** Our answer-level audit cannot recover internal mechanisms or exclude equivalent pretrained procedures, and covers only frozen textual skills, two domains, selected systems, and mostly deterministic executions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27484v1#A1.SSx1 — Backtrace Design Commitments; https://arxiv.org/html/2607.27484v1#Sx4 — Methodology。Evaluation：https://arxiv.org/html/2607.27484v1#A3 — Appendix C Additional Analysis for RQ2; https://arxiv.org/html/2607.27484v1#A4 — Appendix D Additional Analysis for RQ3。Limitations / counterevidence：https://arxiv.org/html/2607.27484v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our answer-level audit cannot recover internal mechanisms or exclude equivalent pretrained procedures, and covers only frozen textual skills, two domains, selected systems, and mostly deterministic executions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27484:end -->

<!-- review:SF-2026-ARXIV-2607-27511:start -->
### Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling

<!-- claim:SF-2026-ARXIV-2607-27511:start -->Imitation learning has shown increasing promise for autonomous robotic surgery, yet safe deployment remains challenging due to the safety-critical nature of surgical tasks and the complexity and variability of surgical environments. Failure detection is therefore an essential safeguard, but its development remains difficult due to the challenges of scarce failure data, highly variable manipulation dynamics, and the need to balance missed detections against disruptive false alarms. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27511:end -->

**为什么进入候选分母。** 摘要首要问题为“Imitation learning has shown increasing promise for autonomous robotic surgery, yet safe deployment remains challenging due to the safety-critical nature of surgical tasks and the complexity and variability of surgical environments.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address these challenges, we introduce FoMo-FD (Flow-Matching World Model for Failure Detection), a failure detection method that learns nominal short-horizon visual dynamics with an action-conditioned flow-matching world model.

**证据证明什么。** Results show that FoMo-FD outperforms observation-level anomaly baselines and a prediction-error variant of the same world model, with the wrist-camera view achieving the strongest performance, including a 96.6% failure detection rate (FDR) at a 1.3% false alarm rate (FAR).

**证据没有证明什么。** Because calibration uses only successful executions, the resulting threshold is task-specific while avoiding assumptions about the type or timing of future failures. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27511v1#S3 — III Method; https://arxiv.org/html/2607.27511v1#S3.SS1 — III-A World Modeling in Latent Vision Space。Evaluation：https://arxiv.org/html/2607.27511v1#S4.SS2 — IV-B Experimental Results; https://arxiv.org/html/2607.27511v1#S4 — IV Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27511v1#S6 — VI Discussion and Conclusion; https://arxiv.org/html/2607.27511v1#S3.SS2 — III-B Nonconformity Scoring and Conformal Failure Detection。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Because calibration uses only successful executions, the resulting threshold is task-specific while avoiding assumptions about the type or timing of future failures.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27511:end -->

<!-- review:SF-2026-ARXIV-2607-27518:start -->
### Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks

<!-- claim:SF-2026-ARXIV-2607-27518:start -->Capabilities of frontier models are often assessed using agentic benchmarks. To trust these results, benchmarks must accurately measure what they claim to and be free from invalidating flaws. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27518:end -->

**为什么进入候选分母。** 摘要首要问题为“Capabilities of frontier models are often assessed using agentic benchmarks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, manual review is difficult to scale, and it is unclear whether automated methods can reliably surface flaws that compromise benchmark validity.

**证据证明什么。** To trust these results, benchmarks must accurately measure what they claim to and be free from invalidating flaws.

**证据没有证明什么。** However, scanners in this work were not equivalent to human graders. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27518v1#S3 — 3 Methodology; https://arxiv.org/html/2607.27518v1#S3.SS1 — 3.1 Evaluation quality framework。Evaluation：https://arxiv.org/html/2607.27518v1#A1.SS4 — A.4 Scanner results on non-agentic evaluations; https://arxiv.org/html/2607.27518v1#S2.SS3 — 2.3 Evaluation auditing work using transcript analysis。Limitations / counterevidence：https://arxiv.org/html/2607.27518v1#A5.SS2 — E.2 Tool Failure; https://arxiv.org/html/2607.27518v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/Generality-Labs/scanner_evaluation, https://huggingface.co/datasets/generality-labs/abc-scout-scanners/, https://epoch.ai/publications/mirrorcode-preliminary-results; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, scanners in this work were not equivalent to human graders.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27518:end -->

<!-- review:SF-2026-ARXIV-2607-27529:start -->
### Latent-Kernel Discrete Flow Maps for Few-Step Generation

<!-- claim:SF-2026-ARXIV-2607-27529:start -->Discrete diffusion and flow-matching models denoise a sequence over many steps, but to keep each step cheap, they factorize the transition across positions and decide every token independently. This makes few-step generation challenging for text when the target couples two positions, such as a subject and a verb that must agree. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27529:end -->

**为什么进入候选分母。** 摘要首要问题为“Discrete diffusion and flow-matching models denoise a sequence over many steps, but to keep each step cheap, they factorize the transition across positions and decide every token independently.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Existing few-step methods buy back the lost correlation by distilling or rectifying a slow teacher, and so inherit the teacher's quality ceiling.

**证据证明什么。** The experiments for unconditional text generation on the One-Billion-Word (LM1B) and WikiText-103 benchmarks show that our LKF model learns strongly heterogeneous components and improves generative perplexity by 2.1x to 3.3x over the likelihood baselines without losing diversity.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27529v1#A5 — Appendix E Architecture details; https://arxiv.org/html/2607.27529v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.27529v1#A4.SS7 — D.7 Proof of Proposition 3 (marginal NELBO for evaluation); https://arxiv.org/html/2607.27529v1#A6 — Appendix F Decoding-policy ablations。Limitations / counterevidence：https://arxiv.org/html/2607.27529v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27529:end -->

<!-- review:SF-2026-ARXIV-2607-27539:start -->
### Subtract, Transport, or Replay? Auditable Deletion from Language-Model Memory

<!-- claim:SF-2026-ARXIV-2607-27539:start -->Exact deletion from persistent language-model memory depends on whether a record's effect remains addressable after later computation. Native Kimi Delta Attention (KDA) gives a negative result for the tested receipt interface: the corpus-pooled raw recurrent contribution changes by 12-49% with the suffix and remains 8-49% after a decay-ledger correction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27539:end -->

**为什么进入候选分母。** 摘要首要问题为“Exact deletion from persistent language-model memory depends on whether a record's effect remains addressable after later computation.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** The audit first tests whether a native KDA record leaves a stable, addressable receipt after later suffix computation; suffix-dependent recurrent contributions and later transition/write terms falsify that assumption. It then separates two valid deletion paths: checkpoint replay recomputes the declared native-state surface, while a support-vector memory retrofitted onto a frozen backbone stores each admitted record behind an independently refittable key boundary.

**证据证明什么。** The paper's two contributions are a negative result for native KDA's tested receipt classes and a positive training-free construction for addressable pretrained memory.

**证据没有证明什么。** It does not show that arbitrary recurrent or parameter memories admit cheap exact deletion, nor that deletion retroactively changes outputs or artifacts already emitted. The positive construction is bounded to the disclosed frozen Gemma checkpoints and conditional retained-key refit protocol.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27539v1#S3.SS5 — 3.5 Recovering the redesigned memory; https://arxiv.org/html/2607.27539v1#S3.SS6 — 3.6 The exact decrement, audited at the model output。Evaluation：https://arxiv.org/html/2607.27539v1#A1 — Appendix A Experimental details; https://arxiv.org/html/2607.27539v1#A2 — Appendix B Full 1B utility results。Limitations / counterevidence：https://arxiv.org/html/2607.27539v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.27539v1#S8 — 8 Discussion: deletion is a property of representation。

**Artifact boundary。** Not Disclosed — exact v1 does not bind the evaluated checkpoint-replay and support-vector-memory implementation to an immutable public experiment commit; the manuscript remains the claim authority.

**Trade-off 与共存边界。** Addressability makes deletion auditable, but it moves cost into explicit per-record state, retained-key refits, checkpoint/replay storage and a precisely declared recovery surface. Native recurrent memory remains useful when exact record deletion is not a requirement; replay remains the conservative path when state cannot be separated safely.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27539:end -->

<!-- review:SF-2026-ARXIV-2607-27549:start -->
### Cross-Embodiment Transfer via Behavior-Aligned Representations

<!-- claim:SF-2026-ARXIV-2607-27549:start -->Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27549:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** However, achieving significant cross-embodiment transfer is often still challenging.

**证据证明什么。** We also demonstrate that they can enhance sim-to-real cross-embodiment transfer, improving task completion progress of real robot policies pre-trained on simulation data by 28%.

**证据没有证明什么。** Additionally, the behavior-aligned representations we consider are not exhaustive, and these representations favor object-centric manipulation tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27549v1#S4.SS1 — IV-A Benchmark Design; https://arxiv.org/html/2607.27549v1#S3.SS3 — III-C Implementation Details。Evaluation：https://arxiv.org/html/2607.27549v1#S4 — IV Simulation Experiments; https://arxiv.org/html/2607.27549v1#S4.SS1 — IV-A Benchmark Design。Limitations / counterevidence：https://arxiv.org/html/2607.27549v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Stanford-ILIAD/openvla-mini, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Additionally, the behavior-aligned representations we consider are not exhaustive, and these representations favor object-centric manipulation tasks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27549:end -->

<!-- review:SF-2026-ARXIV-2607-27557:start -->
### Training Skills Like Parameters via Self-Supervised Semantic Diffusion

<!-- claim:SF-2026-ARXIV-2607-27557:start -->While Large Language Models (LLMs) demonstrate remarkable general instruction-following capabilities, they often fall short of human experts in highly specialized, open-ended domains such as creative screenwriting. Prior approaches typically adopt post-training, yet both supervised fine-tuning and reinforcement learning require weight access that closed-source frontier models do not offer, and demand heavy compute. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27557:end -->

**为什么进入候选分母。** 摘要首要问题为“While Large Language Models (LLMs) demonstrate remarkable general instruction-following capabilities, they often fall short of human experts in highly specialized, open-ended domains such as creative screenwriting.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To overcome this bottleneck, we propose a novel, unsupervised self-evolving agent framework inspired by the corruption-and-reconstruction paradigm of diffusion models.

**证据证明什么。** Experimental results demonstrate that our method enables the agent to autonomously extract and internalize highly generalizable skills, significantly enhancing its domain-specific generation capabilities.

**证据没有证明什么。** 5 Conclusion and Future Work We presented a self-supervised framework that lets an agent learn professional screenwriting skills without any human annotation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27557v1#S3 — 3 Method; https://arxiv.org/html/2607.27557v1#S3.SS5 — 3.5 Compact Memory Architecture。Evaluation：https://arxiv.org/html/2607.27557v1#S4 — 4 Experiments; https://arxiv.org/html/2607.27557v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27557v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：5 Conclusion and Future Work We presented a self-supervised framework that lets an agent learn professional screenwriting skills without any human annotation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27557:end -->

<!-- review:SF-2026-ARXIV-2607-27564:start -->
### Inference-Time Agentic Decision Rules Beat Longer Evolving Search for Multi-Image Medical Reasoning

<!-- claim:SF-2026-ARXIV-2607-27564:start -->Multi-image medical VQA is not merely a prompt-length problem; it is a fundamental challenge of agentic decision-making. Medical vision-language agents must aggregate evidence across ordered images, remain robust to answer-order perturbations, and avoid overfitting to noisy search-time feedback. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27564:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-image medical VQA is not merely a prompt-length problem; it is a fundamental challenge of agentic decision-making.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Across five independent repeated runs, the strongest method emerges as the simplest robust aggregator: the \textbf{order-vote} policy achieves $57.89 \pm 0.65\%$ final-test accuracy, significantly outperforming the fixed baseline ($52.73 \pm 0.42\%$) and the more complex, albeit brittle, order-rerank variant ($55.79 \pm 0.43\%$).

**证据证明什么。** Across five independent repeated runs, the strongest method emerges as the simplest robust aggregator: the \textbf{order-vote} policy achieves $57.89 \pm 0.65\%$ final-test accuracy, significantly outperforming the fixed baseline ($52.73 \pm 0.42\%$) and the more complex, albeit brittle, order-rerank variant ($55.79 \pm 0.43\%$).

**证据没有证明什么。** Third, our repeat protocol is based on independent repeated runs rather than deterministic seed sweeps because the local ShinkaEvolve stack does not currently expose a stable end-to-end global seed for the full pipeline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27564v1#A1.SS5 — A.5 Prompt-Space Design; https://arxiv.org/html/2607.27564v1#A1.SS7 — A.7 Implementation Notes and Reproducibility。Evaluation：https://arxiv.org/html/2607.27564v1#S5 — 5 Experiments and Results; https://arxiv.org/html/2607.27564v1#S5.SS1 — 5.1 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.27564v1#A1.SS4 — A.4 Failure Cases and Boundary Conditions; https://arxiv.org/html/2607.27564v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Third, our repeat protocol is based on independent repeated runs rather than deterministic seed sweeps because the local ShinkaEvolve stack does not currently expose a stable end-to-end global seed for the full pipeline.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27564:end -->

<!-- review:SF-2026-ARXIV-2607-27599:start -->
### World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models

<!-- claim:SF-2026-ARXIV-2607-27599:start -->Building generalizable agents for diverse applications remains a fundamental challenge. While imitation learning-based policies succeed in specific training environments, they often fail to generalize to novel scenes and tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27599:end -->

**为什么进入候选分母。** 摘要首要问题为“Building generalizable agents for diverse applications remains a fundamental challenge.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this work, we propose World Action Planner, a robot planning system that leverages the reasoning capabilities of Vision-Language Models (VLMs) and the physical grounding of a multi-task pose-image conditioned world model.

**证据证明什么。** We demonstrate that our approach achieves superior performance across compositional tasks, new layouts, and zero-shot generalization scenarios, significantly outperforming state-of-the-art end-to-end policy models such as VLAs and WAMs.

**证据没有证明什么。** A primary limitation is that our evaluations are conducted in simulation, while real robot experiments are left to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27599v1#S3 — 3 Methods; https://arxiv.org/html/2607.27599v1#A3 — Appendix C Implementation Details。Evaluation：https://arxiv.org/html/2607.27599v1#A4 — Appendix D Experiment Details; https://arxiv.org/html/2607.27599v1#A5 — Appendix E Wall Clock Time Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.27599v1#S6 — 6 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：A primary limitation is that our evaluations are conducted in simulation, while real robot experiments are left to future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27599:end -->

<!-- review:SF-2026-ARXIV-2607-27600:start -->
### Back from the Future: Key-Value Cache Management by Counter-Causal Surprise

<!-- claim:SF-2026-ARXIV-2607-27600:start -->Key-value (KV) cache management through compression and eviction strategies has emerged as an important research direction in recent years. Computational demands of large language models (LLMs) and their multi-modal variants during output generation can be partially alleviated by caching previous key and value calculations needed by subsequent scaled dot-product attention operations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27600:end -->

**为什么进入候选分母。** 摘要首要问题为“Key-value (KV) cache management through compression and eviction strategies has emerged as an important research direction in recent years.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We evaluate our strategy on various open-source LLMs and benchmark datasets showing competitive or improved performance over other state-of-the-art methods.

**证据证明什么。** We evaluate our strategy on various open-source LLMs and benchmark datasets showing competitive or improved performance over other state-of-the-art methods.

**证据没有证明什么。** Tokens that cannot be predicted with high probability have a high surprise score and represent unique information not available from other tokens or combinations thereof. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27600v1#S3.SS2 — 3.2 Algorithm Summary。Evaluation：https://arxiv.org/html/2607.27600v1#A1 — Appendix A Benchmark Prompts; https://arxiv.org/html/2607.27600v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27600v1#S5 — 5 Conclusion and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/metacognitionai/counter_causal, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Tokens that cannot be predicted with high probability have a high surprise score and represent unique information not available from other tokens or combinations thereof.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27600:end -->

<!-- review:SF-2026-ARXIV-2607-27617:start -->
### Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures

<!-- claim:SF-2026-ARXIV-2607-27617:start -->Identical language-model answers can arise from hidden states that support different future computations, so current-answer probes do not establish a reusable internal interface. We introduce forked futures: future operations are sampled only after a prefix state has formed, and states are compared through the response distributions induced by those operations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27617:end -->

**为什么进入候选分母。** 摘要首要问题为“Identical language-model answers can arise from hidden states that support different future computations, so current-answer probes do not establish a reusable internal interface.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce forked futures: future operations are sampled only after a prefix state has formed, and states are compared through the response distributions induced by those operations.

**证据证明什么。** These results support an economical reusable causal interface within the tested operation banks, while keeping the claim explicitly conditional on the candidate architectures, interventions, and held-out futures.

**证据没有证明什么。** Two states are grouped only when the sampled future operations cannot distinguish them within the pre-specified distortion tolerance. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27617v1#A12 — Appendix L Full Architecture Competition; https://arxiv.org/html/2607.27617v1#A12.SS1 — L.1 Supplementary Table S12: Architecture Ranking Across Distribution Shifts。Evaluation：https://arxiv.org/html/2607.27617v1#A16.SS4 — P.4 What the Model-Organism Results Establish and What They Do Not; https://arxiv.org/html/2607.27617v1#A18 — Appendix R Complete Statistical Analysis Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.27617v1#A15.SS1 — O.1 Supplementary Figure S6: Conceptual Overview of Forked Futures and Hidden APIs; https://arxiv.org/html/2607.27617v1#A16.SS1 — P.1 From Future Equivalence to an Empirical Causal Quotient。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Two states are grouped only when the sampled future operations cannot distinguish them within the pre-specified distortion tolerance.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27617:end -->

<!-- review:SF-2026-ARXIV-2607-27636:start -->
### HALO: Heterogeneous Admission through Localized Obligations for Safe Agentic Execution

<!-- claim:SF-2026-ARXIV-2607-27636:start -->Recent agentic AI systems may return a heterogeneous response containing notices, requests, handoffs, and actions. Conditions can change before external use, so components from the same response need not remain supported together. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27636:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent agentic AI systems may return a heterogeneous response containing notices, requests, handoffs, and actions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** HALO assigns each heterogeneous response component a localized obligation set, admits a component only when its declared prerequisites remain supported, preserves unaffected components instead of rejecting the whole response, and rechecks the exact action immediately before dispatch. A blocked action cannot be revived from stale state; only a freshly generated candidate may replace it.

**证据证明什么。** Across ten cold-start PX4/Gazebo sessions, HALO blocked every tested stale route, observed no matching stale setpoint, and completed all fresh recoveries.

**证据没有证明什么。** The results do not establish that natural-language prerequisite extraction is complete, that every tool boundary exposes enough state for revalidation, or that ten simulated PX4/Gazebo sessions generalize to arbitrary physical systems. Admission alone also cannot protect a queued action after its support changes; the dispatch recheck is essential.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27636v1#Sx3 — Method; https://arxiv.org/html/2607.27636v1#A2 — Appendix B Formal Model and Protocol。Evaluation：https://arxiv.org/html/2607.27636v1#A3 — Appendix C Evaluation Details; https://arxiv.org/html/2607.27636v1#Sx4 — Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.27636v1#A4.SSx2 — Threats to Validity; https://arxiv.org/html/2607.27636v1#Sx5 — Discussion。

**Artifact boundary。** Not Disclosed — exact v1 describes the protocol and PX4/Gazebo evaluation but does not pin an immutable public implementation commit used for the reported runs.

**Trade-off 与共存边界。** Localized admission avoids discarding unrelated useful output, but introduces obligation declaration, dependency tracking and a second authorization point on the critical path. Whole-response rejection remains simpler when components are inseparable; independent checks remain valid only when no hidden dependency crosses components.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27636:end -->

<!-- review:SF-2026-ARXIV-2607-27648:start -->
### Not as Sweet by Another Name: An Empirical Study of Format Robustness in LLM Document Workflows

<!-- claim:SF-2026-ARXIV-2607-27648:start -->LLM-driven software systems are rapidly evolving from plain-text conversations to document-centric end-to-end workflows, where the same semantic content can be delivered in diverse document formats (e.g., CSV) through file upload interfaces. Yet existing testing work focuses on the robustness and reliability of models and systems whose input is a single prompt string, leaving a critical question unanswered: Can these document workflows maintain robust behaviors when the same content arrives in a different document format? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27648:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-driven software systems are rapidly evolving from plain-text conversations to document-centric end-to-end workflows, where the same semantic content can be delivered in diverse document formats (e.g., CSV) through file upload interfaces.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To fill the gap, in this paper, we propose a format-aware metamorphic testing framework with three metamorphic relations to comprehensively evaluate the format robustness of end-to-end LLM document workflows.

**证据证明什么。** Our study demonstrates that document format is not a neutral wrapper but a critical factor affecting the reliability of LLM software systems, calling for corresponding testing and safeguards in the deployment in real-world high-stakes scenarios.

**证据没有证明什么。** These controls mitigate the threat that MR violations are caused by information loss. ③ Our experiments cover four mainstream workflows and four commonly used formats, which may not fully represent some emerging systems, such as skill-based agent systems ( Jiang et al., 2026 ) or additional document formats. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27648v1#S4 — 4. Design。Evaluation：https://arxiv.org/html/2607.27648v1#S4.SS3 — 4.3. Workflow Evaluation; https://arxiv.org/html/2607.27648v1#S5 — 5. Experiment。Limitations / counterevidence：https://arxiv.org/html/2607.27648v1#S6 — 6. Discussion; https://arxiv.org/html/2607.27648v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/openlifescienceai/medmcqa/tree/main/data, https://github.com/LLMBias/BiasLens/tree/main, https://developers.openai.com/api/docs/guides/tools-code-interpreter; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These controls mitigate the threat that MR violations are caused by information loss. ③ Our experiments cover four mainstream workflows and four commonly used formats, which may not fully represent some emerging systems, such as skill-based agent systems ( Jiang et al., 2026 ) or additional document formats.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27648:end -->

<!-- review:SF-2026-ARXIV-2607-27652:start -->
### Harness-G: A Graph-Structured Harness for Search Agents

<!-- claim:SF-2026-ARXIV-2607-27652:start -->Reinforcement learning (RL) search agents commonly model retrieval as free-form natural-language query generation and optimize multi-turn interactions using final-answer rewards. Current studies mainly improve training with denser or more structured credit signals, but rarely examine whether retrieval is properly formulated at the policy-environment interface. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27652:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning (RL) search agents commonly model retrieval as free-form natural-language query generation and optimize multi-turn interactions using final-answer rewards.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address this problem, we propose Harness-G, a graph-structured retrieval framework that redesigns this interface.

**证据证明什么。** Across six QA benchmarks, Harness-G achieves the highest average F1 at both evaluated model scales, outperforming the strongest baseline, Graph-R1, by 10.74 points at 1.5B and 3.98 points at 3B.

**证据没有证明什么。** Harness-G remains text-only; extending its structured actions and SNC to multimodal evidence is a key next step. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27652v1#Sx3 — Method; https://arxiv.org/html/2607.27652v1#A5 — Appendix E Implementation Details。Evaluation：https://arxiv.org/html/2607.27652v1#Sx4.SSx3 — Ablation and Comparative Analysis (RQ2); https://arxiv.org/html/2607.27652v1#A4 — Appendix D Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.27652v1#A14.SS4 — N.4 Additional Failure Cases; https://arxiv.org/html/2607.27652v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Harness-G remains text-only; extending its structured actions and SNC to multimodal evidence is a key next step.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27652:end -->

<!-- review:SF-2026-ARXIV-2607-27677:start -->
### Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness

<!-- claim:SF-2026-ARXIV-2607-27677:start -->AI agents are moving into production workflows where they retrieve information, call tools, maintain state, and act on behalf of users or organizations, but many release decisions still rely on capability signals, demos, or behavioral tests that do not show whether an agent is ready to operate under production constraints. Capability is therefore not production readiness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27677:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agents are moving into production workflows where they retrieve information, call tools, maintain state, and act on behalf of users or organizations, but many release decisions still rely on capability signals, demos, or behavioral tests that do not show whether an agent is ready to operate under production constraints.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Capability is therefore not production readiness.

**证据证明什么。** The results show that context engineering strongly changes reliability, capability improves behavior but does not determine readiness, and governance evidence must remain visible rather than averaged away.

**证据没有证明什么。** As AI agents become more autonomous and more deeply embedded in enterprise workflows, governance cannot remain a document produced after deployment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27677v1#S5 — 5 Implementation in ProofAgent Harness。Evaluation：https://arxiv.org/html/2607.27677v1#S4.SS6 — 4.6 Ablation analysis; https://arxiv.org/html/2607.27677v1#S2 — 2 Related Work: From Agent Evaluation to Governance。Limitations / counterevidence：https://arxiv.org/html/2607.27677v1#S4.SS12 — 4.12 Failure mode coverage; https://arxiv.org/html/2607.27677v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ProofAgent-ai/proofagent-harness, https://pypi.org/project/proofagent-harness/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：As AI agents become more autonomous and more deeply embedded in enterprise workflows, governance cannot remain a document produced after deployment.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-PRODUCTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27677:end -->

<!-- review:SF-2026-ARXIV-2607-27687:start -->
### Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch

<!-- claim:SF-2026-ARXIV-2607-27687:start -->Autoresearch improves machine-learning code by proposing changes, running full training jobs, and keeping changes that improve the metric. The efficiency of this loop depends not only on generating ideas, but also on the agent's ability to decide, before spending a training run, whether a proposed modification is likely to work. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27687:end -->

**为什么进入候选分母。** 摘要首要问题为“Autoresearch improves machine-learning code by proposing changes, running full training jobs, and keeping changes that improve the metric.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** The efficiency of this loop depends not only on generating ideas, but also on the agent's ability to decide, before spending a training run, whether a proposed modification is likely to work.

**证据证明什么。** Autoresearch improves machine-learning code by proposing changes, running full training jobs, and keeping changes that improve the metric.

**证据没有证明什么。** 7 Conclusion Autoresearch efficiency depends on pre-run selection as well as idea generation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27687v1#A1 — Appendix A Propose–Predict–Execute algorithm。Evaluation：https://arxiv.org/html/2607.27687v1#A5 — Appendix E Why focused memory works: component analysis; https://arxiv.org/html/2607.27687v1#A7 — Appendix G Per-seed generalization results。Limitations / counterevidence：https://arxiv.org/html/2607.27687v1#S6 — 6 Limitations; https://arxiv.org/html/2607.27687v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/karpathy/autoresearch/commit/228791fb499afffb54b46200aca536f79142f117, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/tree/1110a243fdf4706b3f48f1d95db1a4f5529b4d41, https://huggingface.co/tencent/Hy3-preview/commit/549c2b3a0fd5b9a6c6059a9935bf0d59ab69d75a; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：7 Conclusion Autoresearch efficiency depends on pre-run selection as well as idea generation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27687:end -->

<!-- review:SF-2026-ARXIV-2607-27690:start -->
### LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents

<!-- claim:SF-2026-ARXIV-2607-27690:start -->We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience. LabEvolver couples a state-grounded inner trial loop for adaptive perception, online planning, and safety validation with an outer evolution loop that distills completed trajectories into reusable skill, strategy, and safety experience. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27690:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience.

**证据证明什么。** On ALFWorld, it further improves cumulative success rate within 20 steps from 76.2% with ReAct to 91.4% over 500 continual tasks, showing generality beyond wet-lab settings.

**证据没有证明什么。** Looking ahead, the long-horizon physical traces accumulated by LabEvolver offer valuable data to power future scientific world models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27690v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.27690v1#S4 — 4 Experiments; https://arxiv.org/html/2607.27690v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27690v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AndyGao6186/LabEvolver, https://huggingface.co/Qwen/Qwen3.5-35B-A3B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Looking ahead, the long-horizon physical traces accumulated by LabEvolver offer valuable data to power future scientific world models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27690:end -->

<!-- review:SF-2026-ARXIV-2607-27694:start -->
### GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference

<!-- claim:SF-2026-ARXIV-2607-27694:start -->Low-bit quantization is essential for efficient LLM inference, and both rotation and fine-grained group quantization have shown individual promise. However, their combination often leads to accuracy degradation or hardware overhead due to a mismatch between the global nature of rotation and the localized behavior of group scaling. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27694:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-bit quantization is essential for efficient LLM inference, and both rotation and fine-grained group quantization have shown individual promise.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose GyRot, a quantization framework and hardware accelerator that bridges this gap through algorithm-hardware co-design.

**证据证明什么。** These results validate GyRot's practical effectiveness for scalable and energy-efficient LLM deployment.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27694v1#S5 — V GyRot Microarchitecture; https://arxiv.org/html/2607.27694v1#S3.SS1 — III-A Model Accuracy Perspective。Evaluation：https://arxiv.org/html/2607.27694v1#S6 — VI Evaluation; https://arxiv.org/html/2607.27694v1#S6.SS1 — VI-A Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27694v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27694:end -->

<!-- review:SF-2026-ARXIV-2607-27704:start -->
### LightRot: A Light-Weighted Rotation Scheme and Architecture for Accurate Low-Bit Large Language Model Inference

<!-- claim:SF-2026-ARXIV-2607-27704:start -->As large language models (LLMs) continue to demonstrate exceptional capabilities across various domains, the challenge of achieving energy-efficient and accurate inference becomes increasingly critical. This work presents LightRot, a lightweight rotation scheme and dedicated hardware accelerator designed for low-bit LLM inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27704:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language models (LLMs) continue to demonstrate exceptional capabilities across various domains, the challenge of achieving energy-efficient and accurate inference becomes increasingly critical.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Its performance is further validated on MT-Bench, demonstrating robust applicability to real-world conversational scenarios and redefining benchmarks for chat-based AI systems.

**证据证明什么。** The proposed accelerator, implemented in a 28nm CMOS process, achieves a peak energy efficiency of 27.4 TOPS/W for 4-bit inference, surpassing prior state-of-the-art designs.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27704v1#S5.SS1 — V-A Overall Architecture; https://arxiv.org/html/2607.27704v1#S3 — III Proposed LightRot Algorithm。Evaluation：https://arxiv.org/html/2607.27704v1#S4 — IV Algorithm Experiments; https://arxiv.org/html/2607.27704v1#S4.SS1 — IV-A Perplexity Evaluation on WikiText-2。Limitations / counterevidence：https://arxiv.org/html/2607.27704v1#S7 — VII Discussion; https://arxiv.org/html/2607.27704v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27704:end -->

<!-- review:SF-2026-ARXIV-2607-27735:start -->
### A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607-27735:start -->Speculative decoding alleviates the memory-bandwidth bottleneck in large language model inference, but its acceleration is jointly constrained by drafting overhead, token acceptance, and speculation length. We present a unified efficiency analysis showing that extending the speculation horizon can reduce rather than improve speedup when the marginal acceptance probability falls below the relative drafting cost. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27735:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative decoding alleviates the memory-bandwidth bottleneck in large language model inference, but its acceleration is jointly constrained by drafting overhead, token acceptance, and speculation length.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Guided by this analysis, we introduce SparseSpec-L, a training-free self-speculative decoding framework for long-context inference.

**证据证明什么。** We present a unified efficiency analysis showing that extending the speculation horizon can reduce rather than improve speedup when the marginal acceptance probability falls below the relative drafting cost.

**证据没有证明什么。** The entropy controller is only moderately predictive and provides task-dependent gains. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27735v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.27735v1#Sx4.SSx3 — Ablation Study and Sensitivity Analysis; https://arxiv.org/html/2607.27735v1#Sx2.SSx2 — Unified Speedup Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.27735v1#Sx6 — Conclusion; https://arxiv.org/html/2607.27735v1#Sx7 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The entropy controller is only moderately predictive and provides task-dependent gains.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27735:end -->

<!-- review:SF-2026-ARXIV-2607-27773:start -->
### ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory

<!-- claim:SF-2026-ARXIV-2607-27773:start -->LLM agents increasingly rely on long-term memory to support multi-session interaction and personalization. However, existing agent memory systems are designed around forward-only evolution, continuously accumulating, consolidating, and overwriting knowledge, with no principled mechanism to inspect, version, or revert prior states. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27773:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents increasingly rely on long-term memory to support multi-session interaction and personalization.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To our knowledge, ChronoMem is the first open-source system and benchmark for systematic semantic global memory rollback in LLM agents.

**证据证明什么。** On long-horizon conversational benchmarks augmented with evolving memory states and rollback tasks, ChronoMem substantially improves rollback-consistent question answering and history summarization relative to prompt-only and retrieval-only baselines, while achieving strong performance in semantic version selection.

**证据没有证明什么。** Promising future directions include rollback-native benchmarks with more realistic user rollback intents, branching histories beyond linear truncation, and higher-concurrency memory backends with stronger multi-writer transactional semantics. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27773v1#S3 — 3. System Design of ChronoMem: The Natural Language “Undo” Button of Agent Memory; https://arxiv.org/html/2607.27773v1#S3.SS2 — 3.2. Architecture Overview。Evaluation：https://arxiv.org/html/2607.27773v1#S2.SS3 — 2.3. Memory Retrieval and Evaluation; https://arxiv.org/html/2607.27773v1#S4 — 4. Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27773v1#S6 — 6. Conclusion; https://arxiv.org/html/2607.27773v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Promising future directions include rollback-native benchmarks with more realistic user rollback intents, branching histories beyond linear truncation, and higher-concurrency memory backends with stronger multi-writer transactional semantics.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27773:end -->

<!-- review:SF-2026-ARXIV-2607-27782:start -->
### RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy

<!-- claim:SF-2026-ARXIV-2607-27782:start -->Flow-matching Vision-Language-Action (VLA) policies have shown strong potential for robotic manipulation but often suffer from compounding errors caused by distribution shifts during deployment. While offline reinforcement learning (RL) provides a practical way to improve deployed policies using rollout data, existing methods either ignore failure data or exploit it only at the trajectory level, resulting in low learning efficiency and persistent errors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27782:end -->

**为什么进入候选分母。** 摘要首要问题为“Flow-matching Vision-Language-Action (VLA) policies have shown strong potential for robotic manipulation but often suffer from compounding errors caused by distribution shifts during deployment.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose **RedFlow**, a fine-grained offline RL framework that redirects failure experiences into action-level corrective supervision for flow-matching VLA policies.

**证据证明什么。** Experiments on the LIBERO benchmark and three real-world manipulation tasks show that RedFlow consistently outperforms state-of-the-art offline RL baselines, improving the real-world success rate from 56.7% to 74.7%.

**证据没有证明什么。** Second, RedFlow can only provide constructive redirection for failures that have nearby positive support in the offline buffer. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27782v1#S3 — 3 Methodology; https://arxiv.org/html/2607.27782v1#A3 — Appendix C Simulation Implementation Details。Evaluation：https://arxiv.org/html/2607.27782v1#S4 — 4 Experiment; https://arxiv.org/html/2607.27782v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27782v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.27782v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Second, RedFlow can only provide constructive redirection for failures that have nearby positive support in the offline buffer.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27782:end -->

<!-- review:SF-2026-ARXIV-2607-27823:start -->
### Hallucinations Leave a Grounding Signature:Verifier-Guided Decoding for Selective Object Correction

<!-- claim:SF-2026-ARXIV-2607-27823:start -->Large vision-language models (LVLMs) often hallucinate objects that are absent from an image. Despite recent progress, existing mitigation methods still lack reliable object-level grounding diagnostics and therefore tend to apply coarse-grained interventions, which can impair visual understanding, shorten responses, and reduce coverage of genuinely grounded objects. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27823:end -->

**为什么进入候选分母。** 摘要首要问题为“Large vision-language models (LVLMs) often hallucinate objects that are absent from an image.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Based on IGS, we propose Verifier-Guided Decoding (VGD), a decoding framework in which a lightweight verifier examines each emerging object mention, rolls back the KV cache when the mention is identified as high risk, suppresses the object and its synonyms, and regenerates the affected continuation.

**证据证明什么。** Experiments on CHAIR and AMBER-G show that VGD achieves state-of-the-art object hallucination reduction: at @rec90, it cuts AMBER-G CHAIR by 43.6\% while retaining 99.6\% of grounded-object coverage, and reduces CHAIR-MSCOCO CHAIR$_i$/CHAIR$_s$ by 37.0\%/30.4\% without shortening captions.

**证据没有证明什么。** VGD converts this internal evidence into per-object risk, locally rolling back and regenerating only high-risk spans while leaving the base LVLM unchanged. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27823v1#S1 — 1 Introduction; https://arxiv.org/html/2607.27823v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.27823v1#S5 — 5 Experiments; https://arxiv.org/html/2607.27823v1#S5.SS5 — 5.5 Ablations and Efficiency。Limitations / counterevidence：https://arxiv.org/html/2607.27823v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：VGD converts this internal evidence into per-object risk, locally rolling back and regenerating only high-risk spans while leaving the base LVLM unchanged.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27823:end -->

<!-- review:SF-2026-ARXIV-2607-27830:start -->
### Thinking Once Is Enough: Intermediate-Layer Evidence Routing for High-Resolution VQA

<!-- claim:SF-2026-ARXIV-2607-27830:start -->High-resolution visual question answering (HR-VQA) is often treated as a problem of insufficient evidence acquisition, where failing multimodal large language models must inspect images again through cropping, re-encoding, or multi-round search. We show that this view is incomplete: in many cases, fine-grained evidence has already survived visual encoding and become identifiable and influential within an intermediate-layer routing window, but is later diluted before answer generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27830:end -->

**为什么进入候选分母。** 摘要首要问题为“High-resolution visual question answering (HR-VQA) is often treated as a problem of insufficient evidence acquisition, where failing multimodal large language models must inspect images again through cropping, re-encoding, or multi-round search.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose Thinking-Once, a \textbf{training-free, single-visual-pass} evidence-routing method that reconstructs question-conditioned attention at this window, preserves core entity tokens and compact background context, and routes this evidence to later layers without extra visual encoding.

**证据证明什么。** These results show that HR-VQA can be improved by routing already encoded evidence rather than repeatedly acquiring new visual inputs.

**证据没有证明什么。** The results support evidence routing as a practical complement to additional visual acquisition in utilization-limited HR-VQA settings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27830v1#Sx3.SSx4 — 3.4. From Analysis to Design Principles; https://arxiv.org/html/2607.27830v1#Sx4 — 4. Methodology。Evaluation：https://arxiv.org/html/2607.27830v1#as1_A4 — Appendix D Supplementary Evaluation Results; https://arxiv.org/html/2607.27830v1#Sx3 — 3. Observations and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.27830v1#Sx6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The results support evidence routing as a practical complement to additional visual acquisition in utilization-limited HR-VQA settings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27830:end -->

<!-- review:SF-2026-ARXIV-2607-27834:start -->
### MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory

<!-- claim:SF-2026-ARXIV-2607-27834:start -->Persistent memory lets long-running large language model agents reuse information across sessions and tasks. Yet errors in writable memory can persist and corrupt future behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27834:end -->

**为什么进入候选分母。** 摘要首要问题为“Persistent memory lets long-running large language model agents reuse information across sessions and tasks.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Existing systems improve storage and retrieval, but they do not provide a transaction boundary for reliable updates and recovery.

**证据证明什么。** It outperforms Dense by 17.06--24.07 points in five representative settings.

**证据没有证明什么。** Discussion and Limitations The results support source-constrained admission, chronology-based visibility, and complete-state recovery under the declared contracts, but not semantic truth or robustness to concurrent or repeated faults, intent corruption, or physical loss. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27834v1#Sx3 — Method; https://arxiv.org/html/2607.27834v1#Sx3.SSx2 — System model and trust boundary。Evaluation：https://arxiv.org/html/2607.27834v1#Sx4 — Experiments; https://arxiv.org/html/2607.27834v1#Sx4.SSx1 — Evaluation Overview。Limitations / counterevidence：https://arxiv.org/html/2607.27834v1#Sx5 — Discussion and Limitations; https://arxiv.org/html/2607.27834v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langmem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Discussion and Limitations The results support source-constrained admission, chronology-based visibility, and complete-state recovery under the declared contracts, but not semantic truth or robustness to concurrent or repeated faults, intent corruption, or physical loss.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27834:end -->

<!-- review:SF-2026-ARXIV-2607-27842:start -->
### FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference

<!-- claim:SF-2026-ARXIV-2607-27842:start -->Diffusion models are widely used to generate high-quality images and videos, but their iterative denoising process remains computationally intensive. A growing class of training-free accelerators reduces this cost by reusing cached intermediate features or forecasting future ones. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27842:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion models are widely used to generate high-quality images and videos, but their iterative denoising process remains computationally intensive.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Based on this observation, we introduce FeatFix, a local exact-feature correction method for cached diffusion inference.

**证据证明什么。** We find that this previously computed feature can instead be reused for correction.

**证据没有证明什么。** Limitations FeatFix focuses on a common setting in which cache- or forecast-based accelerators already evaluate occasional exact block features. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27842v1#Sx3 — Method; https://arxiv.org/html/2607.27842v1#Sx3.SSx3 — FeatFix Framework。Evaluation：https://arxiv.org/html/2607.27842v1#Sx4 — Experiments; https://arxiv.org/html/2607.27842v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27842v1#Sx5 — Limitations; https://arxiv.org/html/2607.27842v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/vipshop/cache-dit, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Limitations FeatFix focuses on a common setting in which cache- or forecast-based accelerators already evaluate occasional exact block features.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27842:end -->

<!-- review:SF-2026-ARXIV-2607-27871:start -->
### Search as Computation Allocation

<!-- claim:SF-2026-ARXIV-2607-27871:start -->Many algorithms spend an internal resource before returning a decision and are evaluated only by the quality of that terminal output. We formalize such procedures as terminal computation-allocation problems: costly computations produce observations, update beliefs about a latent environment, and matter only through terminal decision loss. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27871:end -->

**为什么进入候选分母。** 摘要首要问题为“Many algorithms spend an internal resource before returning a decision and are evaluated only by the quality of that terminal output.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We formalize such procedures as terminal computation-allocation problems: costly computations produce observations, update beliefs about a latent environment, and matter only through terminal decision loss.

**证据证明什么。** The theory identifies a shared decision problem without asserting that one acquisition rule is universally optimal.

**证据没有证明什么。** For bounded target-dependent loss, our bound shows that little information implies little myopic VOC, but high information need not imply high decision value. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27871v1#Sx7.SSx2 — A Location Model for Heuristic Error。Evaluation：https://arxiv.org/html/2607.27871v1#Sx1 — Introduction; https://arxiv.org/html/2607.27871v1#Sx2 — Preliminaries。Limitations / counterevidence：https://arxiv.org/html/2607.27871v1#Sx10 — Conclusion; https://arxiv.org/html/2607.27871v1#Sx9 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：For bounded target-dependent loss, our bound shows that little information implies little myopic VOC, but high information need not imply high decision value.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27871:end -->

<!-- review:SF-2026-ARXIV-2607-27877:start -->
### An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding

<!-- claim:SF-2026-ARXIV-2607-27877:start -->Multi-agent vibe coding promises to accelerate software development, yet existing benchmarks rely on synthetic environments that ignore practical time and monetary costs, conflate reasoning with communication, and reward only superficial completion. We introduce multi-agent from-scratch evaluation benchmark, MSEval, evaluating multi-agent coding on real-world tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27877:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent vibe coding promises to accelerate software development, yet existing benchmarks rely on synthetic environments that ignore practical time and monetary costs, conflate reasoning with communication, and reward only superficial completion.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce multi-agent from-scratch evaluation benchmark, MSEval, evaluating multi-agent coding on real-world tasks.

**证据证明什么。** The benchmark is released at https://github.com/robinren03/MSEval.

**证据没有证明什么。** This is the multi-agent-specific failure mode—a contract broken by one owner silently zeroes another owner’s correct work—and why requirement-level feedback with explicit dependencies beats a scalar score. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27877v1#Sx12 — TAgent Verification Methodology; https://arxiv.org/html/2607.27877v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.27877v1#Sx2.SSx2 — Multi-Agent Benchmarks; https://arxiv.org/html/2607.27877v1#Sx3.SSx1 — Benchmark Framework Overview。Limitations / counterevidence：https://arxiv.org/html/2607.27877v1#Sx4.SSx4 — A General Failure Taxonomy; https://arxiv.org/html/2607.27877v1#Sx5 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This is the multi-agent-specific failure mode—a contract broken by one owner silently zeroes another owner’s correct work—and why requirement-level feedback with explicit dependencies beats a scalar score.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27877:end -->

<!-- review:SF-2026-ARXIV-2607-27910:start -->
### A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-27910:start -->Inference time defences against vision language model jailbreaks often subtract a calibrated direction from the residual stream at a chosen decoder layer. We compare five defence candidates across 15 model and layer cells from four architectural families under a magnitude controlled protocol that matches the intervention size for each prompt and pairs every direction with a random control of the same norm. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27910:end -->

**为什么进入候选分母。** 摘要首要问题为“Inference time defences against vision language model jailbreaks often subtract a calibrated direction from the residual stream at a chosen decoder layer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We compare five defence candidates across 15 model and layer cells from four architectural families under a magnitude controlled protocol that matches the intervention size for each prompt and pairs every direction with a random control of the same norm.

**证据证明什么。** These results show that the two recipes recover partially overlapping geometry and that direction based defences should be calibrated separately for each language decoder family.

**证据没有证明什么。** The text-only CMRM refusal direction has positive cosine alignment with the multimodal image-conditioning shift on all cells (mean , – random null), giving the first quantitative cross-paradigm replication that the two refusal-geometry literatures probe overlapping rather than independent geometric structure. defence recovery utility loss Pareto (of ) TF / Img / Mod ABL_POS ✓/ ✓/ ✓ IGNORE_INSTR ✓/ — / — CMRM-like ✓/ — / — ShiftDC-like ✓/ ✓/ — RANDOM_CTRL ✓/ — / — Table 5: Defence comparison over the -cell grid. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27910v1#S3 — 3 Method; https://arxiv.org/html/2607.27910v1#A7 — Appendix G Cross-model direction transfer。Evaluation：https://arxiv.org/html/2607.27910v1#A3.SS2 — C.2 Mechanistic ablation versus prompt-level instruction; https://arxiv.org/html/2607.27910v1#A8 — Appendix H Probe-regime analysis: where the attack signal lives。Limitations / counterevidence：https://arxiv.org/html/2607.27910v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The text-only CMRM refusal direction has positive cosine alignment with the multimodal image-conditioning shift on all cells (mean , – random null), giving the first quantitative cross-paradigm replication that the two refusal-geometry literatures probe overlapping rather than independent geometric structure. defence recovery utility loss Pareto (of ) TF / Img / Mod ABL_POS ✓/ ✓/ ✓ IGNORE_INSTR ✓/ — / — CMRM-like ✓/ — / — ShiftDC-like ✓/ ✓/ — RANDOM_CTRL ✓/ — / — Table 5: Defence comparison over the -cell grid.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27910:end -->

<!-- review:SF-2026-ARXIV-2607-27912:start -->
### IFHierBench: Hierarchical Instruction Following for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-27912:start -->Instruction-following ability is critical for deploying large language models in real-world applications, where downstream components depend on the output satisfying specific constraints. Modern deployments increasingly handle the full task in a single LLM call, with one prompt specifying a layered output whose overall artifact, structural sections, and nested fields must each satisfy concrete constraints. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27912:end -->

**为什么进入候选分母。** 摘要首要问题为“Instruction-following ability is critical for deploying large language models in real-world applications, where downstream components depend on the output satisfying specific constraints.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Reliably following nested constraints remains a substantial gap for current LLMs, motivating future training methods that consider constraint adherence at finer granularity to achieve better instruction-following ability.

**证据证明什么。** Evaluating seven leading proprietary and open-weight models, we find that even the strongest model only marginally exceeds 50% prompt-level accuracy and that accuracy degrades sharply as constraint depth grows.

**证据没有证明什么。** Evaluating seven leading models, we find that they handle flat ( ) constraints well, but accuracy drops sharply as nesting deepens, with the strongest model only marginally exceeding 50%. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27912v1#S1 — 1 Introduction; https://arxiv.org/html/2607.27912v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.27912v1#S2.SS2 — 2.2 Instruction-Following Benchmarks; https://arxiv.org/html/2607.27912v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27912v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.27912v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Evaluating seven leading models, we find that they handle flat ( ) constraints well, but accuracy drops sharply as nesting deepens, with the strongest model only marginally exceeding 50%.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27912:end -->

<!-- review:SF-2026-ARXIV-2607-27928:start -->
### Harnessing the Potential of Optimizing Data Mixtures via Bayesian Domain Reweighting

<!-- claim:SF-2026-ARXIV-2607-27928:start -->The performance of Large Language Models (LLMs) is fundamentally influenced by the distributional composition of multi-domain pre-training data. While manual heuristics were prevalent in early models, they increasingly fail to capture the intricate synergies between domains as data complexity grows. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27928:end -->

**为什么进入候选分母。** 摘要首要问题为“The performance of Large Language Models (LLMs) is fundamentally influenced by the distributional composition of multi-domain pre-training data.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** These methods rely on strong structural assumptions, such as rank invariance or scaling laws, which are often violated, resulting in non-negligible estimation bias.

**证据证明什么。** Experimental results demonstrate that proposed method could achieve stable and efficient domain weights learning, and identifies optimal mixtures while consuming substantially less data than search-based function-fitting methods, revitalizing optimization-based domain weighting for large-scale applications.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27928v1#S2 — 2 Methods; https://arxiv.org/html/2607.27928v1#S2.SS2 — 2.2 Bayesian Domain Reweighting Framework。Evaluation：https://arxiv.org/html/2607.27928v1#A5 — Appendix E Detailed Evaluation Benchmark Information; https://arxiv.org/html/2607.27928v1#S3 — 3 Experimental Results。Limitations / counterevidence：https://arxiv.org/html/2607.27928v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27928:end -->

<!-- review:SF-2026-ARXIV-2607-27933:start -->
### The Geometry of Flow-Matching Uncertainty: A Cost-free Uncertainty Proxy and Its Application in Flow-based VLA Failure Detection

<!-- claim:SF-2026-ARXIV-2607-27933:start -->Flow matching (FM) has become a popular action head paradigm for modern embodied models. However, as a conditional generative model, it does not explicitly expose its inherent uncertainty, producing faulty action chunks even when it misinterprets the scene or encounters out-of-distribution (OOD) inputs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27933:end -->

**为什么进入候选分母。** 摘要首要问题为“Flow matching (FM) has become a popular action head paradigm for modern embodied models.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Therefore, determining when an FM-generated action can be trusted is essential for safe deployment, yet existing uncertainty estimation methods on real-time control suffer from several issues: extra training budget, high computational overhead, and low generalization ability.

**证据证明什么。** Results show that $\mathrm{accel}$ identifies failing rollouts well before termination, matching or even outperforming costly resampling- and training-based baselines across settings under realistic deployment budget.

**证据没有证明什么。** Although occasionally exhibited transient spikes above the reference level, these were absorbed by the slack parameter and did not trigger an alarm. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27933v1#S4.SS2 — 4.2 Method; https://arxiv.org/html/2607.27933v1#A5 — Appendix E Toy Model Implementation Details。Evaluation：https://arxiv.org/html/2607.27933v1#A6 — Appendix F Failure-Detection Experimental Details; https://arxiv.org/html/2607.27933v1#A7 — Appendix G Ablation Study on Failure Detection。Limitations / counterevidence：https://arxiv.org/html/2607.27933v1#A1.SS1 — A.1 How Works as a Failure Score?; https://arxiv.org/html/2607.27933v1#A6 — Appendix F Failure-Detection Experimental Details。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Although occasionally exhibited transient spikes above the reference level, these were absorbed by the slack parameter and did not trigger an alarm.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27933:end -->

<!-- review:SF-2026-ARXIV-2607-27951:start -->
### Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs

<!-- claim:SF-2026-ARXIV-2607-27951:start -->Large language model safeguards decide whether to answer before seeing how an answer will be used. This creates a basic problem for dual-use tasks: the same answer can help an authorized professional or an attacker, while an attacker can imitate a benign request and interaction history. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27951:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model safeguards decide whether to answer before seeing how an answer will be used.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This creates a basic problem for dual-use tasks: the same answer can help an authorized professional or an attacker, while an attacker can imitate a benign request and interaction history.

**证据证明什么。** We then show how a trusted credential can complement existing safeguards by adding hard-to-copy information that predicts actual downstream use, and identify the stronger condition needed to eliminate the floor.

**证据没有证明什么。** 5 Limitations The characterization assumes a fixed utility calibration, finite operational resolution, and a specified attacker class. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27951v1#S3.SS7 — 3.7 Design Implications。Evaluation：https://arxiv.org/html/2607.27951v1#S3 — 3 Main Result。Limitations / counterevidence：https://arxiv.org/html/2607.27951v1#S5 — 5 Limitations; https://arxiv.org/html/2607.27951v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：5 Limitations The characterization assumes a fixed utility calibration, finite operational resolution, and a specified attacker class.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27951:end -->

<!-- review:SF-2026-ARXIV-2607-27967:start -->
### MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation

<!-- claim:SF-2026-ARXIV-2607-27967:start -->Credit assignment is a fundamental challenge in cooperative multi-agent reinforcement learning, particularly in embodied AI settings characterized by limited and delayed feedback as well as dynamically changing numbers of active agents. We propose MARS-RA, a framework that reformulates credit assignment as a rank aggregation problem using contribution-based pairwise comparisons among agents generated by large multimodal models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27967:end -->

**为什么进入候选分母。** 摘要首要问题为“Credit assignment is a fundamental challenge in cooperative multi-agent reinforcement learning, particularly in embodied AI settings characterized by limited and delayed feedback as well as dynamically changing numbers of active agents.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose MARS-RA, a framework that reformulates credit assignment as a rank aggregation problem using contribution-based pairwise comparisons among agents generated by large multimodal models.

**证据证明什么。** Experimental results on challenging tasks of different types indicate that MARS-RA can guide agents toward effective cooperation.

**证据没有证明什么。** 10 Limitations There exist several avenues for improving this work and mitigating the limitations discussed below: (1) MARS-RA depends on LMMs for pairwise agent comparisons. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27967v1#S5 — 5 Method。Evaluation：https://arxiv.org/html/2607.27967v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.27967v1#A4 — Appendix D Experiments on Overcooked and Pistonball。Limitations / counterevidence：https://arxiv.org/html/2607.27967v1#S10 — 10 Limitations; https://arxiv.org/html/2607.27967v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Vector-Wangel/XLeRobot, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：10 Limitations There exist several avenues for improving this work and mitigating the limitations discussed below: (1) MARS-RA depends on LMMs for pairwise agent comparisons.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27967:end -->

<!-- review:SF-2026-ARXIV-2607-28027:start -->
### VISA: A Structured Description Protocol for Agent-Based Simulation Models Towards Machine Reproducibility

<!-- claim:SF-2026-ARXIV-2607-28027:start -->Agent-based models (ABMs) are difficult to reproduce: their behavior is spread across prose narratives, platform-specific code, and implicit assumptions, so that two readers routinely reconstruct different models from the same documentation. We present VISA, a structured, symbol-based description protocol that specifies a model in eight interconnected tables---four at the agent level (Agent, Variable, Sensing, Internal Function) and four at the model level (Associated Data, Input/Output, Schedule, Validation)---under the principle of minimality with completeness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28027:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent-based models (ABMs) are difficult to reproduce: their behavior is spread across prose narratives, platform-specific code, and implicit assumptions, so that two readers routinely reconstruct different models from the same documentation.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present VISA, a structured, symbol-based description protocol that specifies a model in eight interconnected tables---four at the agent level (Agent, Variable, Sensing, Internal Function) and four at the model level (Associated Data, Input/Output, Schedule, Validation)---under the principle of minimality with completeness.

**证据证明什么。** VISA moves the reproduction barrier from the model, where it is invisible, to a named, localized dependency, where it is actionable.

**证据没有证明什么。** The protocol has clear limits, and each points to a direction for improvement. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28027v1#A1 — Appendix A Model 1 — Rebellion (reproduced); https://arxiv.org/html/2607.28027v1#A1.SS1 — A.1 VISA Specification — Rebellion Model (Exp1)。Evaluation：https://arxiv.org/html/2607.28027v1#S5 — 5 Empirical Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.28027v1#S6 — 6 Discussion; https://arxiv.org/html/2607.28027v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AgentLabCn/visa, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The protocol has clear limits, and each points to a direction for improvement.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28027:end -->

<!-- review:SF-2026-ARXIV-2607-28037:start -->
### ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents

<!-- claim:SF-2026-ARXIV-2607-28037:start -->As LLM-based agents are deployed in complex, multi-step workflows, a critical evaluation gap has emerged: most existing benchmarks judge only final outcomes, unable to distinguish reliable reasoning from lucky success or attribute failures to specific process deficiencies, hindering attribution in long-horizon tasks. In this work, we present ClawTrack, a dual-assessment benchmark that simultaneously measures what an agent achieves (Task Score) and how it achieves it (Process Score). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28037:end -->

**为什么进入候选分母。** 摘要首要问题为“As LLM-based agents are deployed in complex, multi-step workflows, a critical evaluation gap has emerged: most existing benchmarks judge only final outcomes, unable to distinguish reliable reasoning from lucky success or attribute failures to specific process deficiencies, hindering attribution in long-horizon tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Evaluating 21 models over 16,000+ trials, we find that: (1) process scores effectively attribute success and failure to specific reasoning dimensions, filtering lucky passes invisible to outcome-only evaluation; (2) the four dimensions are complementary, with result verification as the systematic bottleneck; (3) the framework is robust to evaluator choice across different judge LLMs; and (4) process-based trajectory filtering yields consistent post-training improvements across model scales.

**证据证明什么。** Evaluating 21 models over 16,000+ trials, we find that: (1) process scores effectively attribute success and failure to specific reasoning dimensions, filtering lucky passes invisible to outcome-only evaluation; (2) the four dimensions are complementary, with result verification as the systematic bottleneck; (3) the framework is robust to evaluator choice across different judge LLMs; and (4) process-based trajectory filtering yields consistent post-training improvements across model scales.

**证据没有证明什么。** Conclusion We present ClawTrack, a dual-assessment benchmark that measures both what an agent achieves and how it achieves it, addressing the diagnostic blind spot of outcome-only evaluation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28037v1#A4.SS1 — D.1. Process Grader System Prompt; https://arxiv.org/html/2607.28037v1#A4.SS2 — D.2. Outcome Grader System Prompt。Evaluation：https://arxiv.org/html/2607.28037v1#A4 — Appendix D Evaluation Prompts; https://arxiv.org/html/2607.28037v1#A5 — Appendix E Extended Results。Limitations / counterevidence：https://arxiv.org/html/2607.28037v1#A1 — Appendix A Limitations and Broader Impacts; https://arxiv.org/html/2607.28037v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conclusion We present ClawTrack, a dual-assessment benchmark that measures both what an agent achieves and how it achieves it, addressing the diagnostic blind spot of outcome-only evaluation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28037:end -->

<!-- review:SF-2026-ARXIV-2607-28069:start -->
### SemPIC: Learning Semantic Position-Independent KV Caches

<!-- claim:SF-2026-ARXIV-2607-28069:start -->Long-context retrieval and agentic workloads repeatedly reuse the same documents under changing instructions, histories, and document orders. Prefix caching cannot exploit this reuse, while position-independent caching (PIC) remains unreliable because independently compiled KV states lack the future context in which they will be consumed. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28069:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context retrieval and agentic workloads repeatedly reuse the same documents under changing instructions, histories, and document orders.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present \emph{SemPIC}, which trains a LoRA-enabled Writer to compile native per-layer document KVs through behavioral distillation while retaining the pretrained decoder as an unchanged Reader.

**证据证明什么。** Our diagnostics show that a learned boundary-conditioned baseline sharply reduces attention deviation near reusable-block boundaries but leaves interior and task-level residuals, motivating adaptation of the document representation itself.

**证据没有证明什么。** 7 Conclusion Position-independent reuse asks a document cache to function in contexts absent during construction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28069v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28069v1#S2 — 2 Background: Position-Independent Caching。Evaluation：https://arxiv.org/html/2607.28069v1#A4 — Appendix D Evaluation Details; https://arxiv.org/html/2607.28069v1#S4 — 4 Motivating Analysis: Boundary Conditioning Leaves an Interior Gap。Limitations / counterevidence：https://arxiv.org/html/2607.28069v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/alex-karev/biographies, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：7 Conclusion Position-independent reuse asks a document cache to function in contexts absent during construction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28069:end -->

<!-- review:SF-2026-ARXIV-2607-28103:start -->
### MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck

<!-- claim:SF-2026-ARXIV-2607-28103:start -->Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28103:end -->

**为什么进入候选分母。** 摘要首要问题为“Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address these challenges, we propose Memory Intent-Aware Neural Denoising(MIND), a lightweight defense framework for memory injection attack.

**证据证明什么。** Extensive experiments show that MIND reduces attack success rates while preserving task accuracy and inference efficiency.

**证据没有证明什么。** 3.2 Threat Model Attacker’s Goal and Capacity . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28103v1#S4 — 4 Methodology; https://arxiv.org/html/2607.28103v1#S3.SS2 — 3.2 Threat Model。Evaluation：https://arxiv.org/html/2607.28103v1#S5 — 5 Experiments; https://arxiv.org/html/2607.28103v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.28103v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.28103v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：3.2 Threat Model Attacker’s Goal and Capacity .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28103:end -->

<!-- review:SF-2026-ARXIV-2607-28150:start -->
### SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer

<!-- claim:SF-2026-ARXIV-2607-28150:start -->Disaggregating the prefill and decoding stages of large language model (LLM) inference into two separate sets of nodes is widely adopted in today's LLM serving systems. However, such an architecture poses significant challenges for self-hosted LLM deployments on rented cloud instances, since transferring enormous key-value (KV) caches between disaggregated nodes can easily saturate the limited inter-node network bandwidth. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28150:end -->

**为什么进入候选分母。** 摘要首要问题为“Disaggregating the prefill and decoding stages of large language model (LLM) inference into two separate sets of nodes is widely adopted in today's LLM serving systems.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we propose to mitigate the network bottleneck by selectively transferring essential KV cache entries across the two stages.

**证据证明什么。** Experimental results show that SmartGen reduces time-to-second-token by up to 4.3x compared with the typical full KV cache transfer approach while offering comparable subsequent decoding performance and accuracy.

**证据没有证明什么。** Since prefill nodes cannot update the KV mask matrix via GDR, the KV mask should be maintained in host memory. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28150v1#S4 — 4 The SmartGen Design; https://arxiv.org/html/2607.28150v1#S6.SS1 — 6.1 LLM Inference Systems。Evaluation：https://arxiv.org/html/2607.28150v1#S3 — 3 Analysis of KV Cache Transfer; https://arxiv.org/html/2607.28150v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.28150v1#S4.SS4 — 4.4 Discussions; https://arxiv.org/html/2607.28150v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/deepseek-ai/DeepSeek-V3.2-Exp/blob/main/DeepSeek_V3_2.pdf, https://www.microsoft.com/en-us/research/project/minference-million-tokens-prompt-inference-for-long-context-llms, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Since prefill nodes cannot update the KV mask matrix via GDR, the KV mask should be maintained in host memory.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-PD-DISAGGREGATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28150:end -->

<!-- review:SF-2026-ARXIV-2607-28165:start -->
### Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents

<!-- claim:SF-2026-ARXIV-2607-28165:start -->Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction. While this paradigm enhances interaction naturalness, it introduces a critical yet under-explored attack surface, as audio inputs inevitably contain environmental noise beyond user control. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28165:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Notably, our methods achieve an average Attack Success Rate (ASR) of 69.10\% against the advanced Gemini 3 Pro.

**证据证明什么。** Notably, our methods achieve an average Attack Success Rate (ASR) of 69.10\% against the advanced Gemini 3 Pro.

**证据没有证明什么。** Threat Model We consider a highly practical interaction scenario: a user actively engaging with a Multimodal Agent (e.g., Doubao AI Smartphone) through continuous audio. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28165v1#S4 — IV. Attack Framework and Benchmark Design; https://arxiv.org/html/2607.28165v1#S5 — V. Detection Methods and Defense Framework。Evaluation：https://arxiv.org/html/2607.28165v1#A3 — Appendix C Details of Attack Evaluation; https://arxiv.org/html/2607.28165v1#S4 — IV. Attack Framework and Benchmark Design。Limitations / counterevidence：https://arxiv.org/html/2607.28165v1#S10 — X. Conclusion; https://arxiv.org/html/2607.28165v1#S3 — III. Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/Limax666/AudioAgentSecurity, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Threat Model We consider a highly practical interaction scenario: a user actively engaging with a Multimodal Agent (e.g., Doubao AI Smartphone) through continuous audio.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28165:end -->

<!-- review:SF-2026-ARXIV-2607-28223:start -->
### Queue-Theoretic Admission Control for Multi-Tenant GPU Clusters

<!-- claim:SF-2026-ARXIV-2607-28223:start -->GPU cluster operators cannot predict how long pending workloads will wait for admission. Existing systems use greedy heuristics with no formal wait time guarantees. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28223:end -->

**为什么进入候选分母。** 摘要首要问题为“GPU cluster operators cannot predict how long pending workloads will wait for admission.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Existing systems use greedy heuristics with no formal wait time guarantees.

**证据证明什么。** The vector k_eff correctly identifies bottleneck resource dimensions, Little's Law holds exactly, and the Erlang-C approximation consistently overestimates observed wait times in the conservative direction.

**证据没有证明什么。** Limitations Our model makes several simplifying assumptions that should be understood when applying the results in practice. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28223v1#S2.SS1 — 2.1. GPU Cluster Admission Architecture; https://arxiv.org/html/2607.28223v1#S3.SS1 — 3.1. System Definition。Evaluation：https://arxiv.org/html/2607.28223v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.28223v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.28223v1#S7 — 7. Limitations; https://arxiv.org/html/2607.28223v1#S8 — 8. Discussion and Open Problems。

**Artifact boundary。** Exact v1 links https://github.com/kubernetes-sigs/kueue/issues/13159, https://github.com/kubernetes-sigs/kueue/issues/10124, https://github.com/kubernetes-sigs/kueue/issues/10614; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Limitations Our model makes several simplifying assumptions that should be understood when applying the results in practice.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28223:end -->

<!-- review:SF-2026-ARXIV-2607-28225:start -->
### FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification

<!-- claim:SF-2026-ARXIV-2607-28225:start -->Agentic vision-language models (VLMs), which interleave textual reasoning with explicit tool calls such as cropping and code-based image manipulation, have emerged as a compelling paradigm for reliable and interpretable multimodal reasoning. However, recent studies have revealed that such models often use tools unfaithfully. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28225:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic vision-language models (VLMs), which interleave textual reasoning with explicit tool calls such as cropping and code-based image manipulation, have emerged as a compelling paradigm for reliable and interpretable multimodal reasoning.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To this end, we introduce FaithEyes, a multi-agent self-judging framework.

**证据证明什么。** The homepage is at https://github.com/Mosi-AI/FaithEyes.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28225v1#S3 — 3 Method; https://arxiv.org/html/2607.28225v1#S3.SS2 — 3.2 FaithEyes : multi-agent self-judging framework。Evaluation：https://arxiv.org/html/2607.28225v1#A4 — Appendix D Training stage ablation; https://arxiv.org/html/2607.28225v1#S3.SS1 — 3.1 Preliminaries and analysis。Limitations / counterevidence：https://arxiv.org/html/2607.28225v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Mosi-AI/FaithEyes, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28225:end -->

<!-- review:SF-2026-ARXIV-2607-28282:start -->
### (Towards) Scalable Reliable Automated Evaluation with Large Language Models

<!-- claim:SF-2026-ARXIV-2607-28282:start -->Evaluating the quality and relevance of textual outputs from Large Language Models (LLMs) remains challenging and resource-intensive. Existing automated metrics often fail to capture the complexity and variability inherent in LLM-generated outputs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28282:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluating the quality and relevance of textual outputs from Large Language Models (LLMs) remains challenging and resource-intensive.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** An Elo rating system is used to generate stable and interpretable rankings.

**证据证明什么。** Preliminary results show that automatically derived rankings correlate well with expert judgments, significantly reducing the need for extensive human intervention.

**证据没有证明什么。** Another practical challenge arises when comparing highly similar items. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28282v1#S2.SS2 — 2.2 Elo Rating System for Ranking Items; https://arxiv.org/html/2607.28282v1#S4 — 4 Approach。Evaluation：https://arxiv.org/html/2607.28282v1#S6.SS3 — 6.3 Results and Analysis; https://arxiv.org/html/2607.28282v1#S4.SS3 — 4.3 Handling Multiple Evaluations and Agreement Thresholds。Limitations / counterevidence：https://arxiv.org/html/2607.28282v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.28282v1#S8 — 8 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/features/copilot, https://www.aclweb.org/portal/content/acl-code-ethics, https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Another practical challenge arises when comparing highly similar items.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28282:end -->

<!-- review:SF-2026-ARXIV-2607-28317:start -->
### One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence

<!-- claim:SF-2026-ARXIV-2607-28317:start -->A single human must audit $N$ LLM agents under a budget of $B \ll N$ audits per round, guided by self-reported confidence that may be adversarially miscalibrated and by correlated errors. We model this as budgeted noisy inspection over a two-level Gaussian copula and locate the miscalibration threshold $δ^*$ past which confidence-ranked auditing is \emph{worse} than random. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28317:end -->

**为什么进入候选分母。** 摘要首要问题为“A single human must audit $N$ LLM agents under a budget of $B \ll N$ audits per round, guided by self-reported confidence that may be adversarially miscalibrated and by correlated errors.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We model this as budgeted noisy inspection over a two-level Gaussian copula and locate the miscalibration threshold $δ^*$ past which confidence-ranked auditing is \emph{worse} than random.

**证据证明什么。** Five open-weight LLMs show operationally useless (near-constant) confidence, point estimates at or beyond the flip though CIs straddle it; a proprietary model is informative and lands below it.

**证据没有证明什么。** 15 Limitation support values Quantifying values for the boundary statements in the main paper’s Limitations (§6); each limitation states its boundary in full, with the supporting numbers here. (a) Verifier-noise crossover at : at diversity-Bayes 14.27 vs. conf-ranked 14.04 (cedes); at , 13.56 vs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28317v1#S12 — 12 H2 in the synthetic model; robustness to the copula choice; https://arxiv.org/html/2607.28317v1#S3 — 3 Model。Evaluation：https://arxiv.org/html/2607.28317v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28317v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.28317v1#S14 — 14 Confidence parse failures and imputation; https://arxiv.org/html/2607.28317v1#S15 — 15 Limitation support values。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：15 Limitation support values Quantifying values for the boundary statements in the main paper’s Limitations (§6); each limitation states its boundary in full, with the supporting numbers here. (a) Verifier-noise crossover at : at diversity-Bayes 14.27 vs. conf-ranked 14.04 (cedes); at , 13.56 vs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28317:end -->

<!-- review:SF-2026-ARXIV-2607-28336:start -->
### Correcting What You Cannot See: Credit Assignment for Perception Distillation in Multimodal Reasoners

<!-- claim:SF-2026-ARXIV-2607-28336:start -->On-policy distillation provides dense supervision for multimodal reasoners, but its trajectory-level reward cannot determine whether a failed answer arose from perception or subsequent reasoning. Perception Success Rate (PSR), estimated from multiple reasonings sharing one perception, remains ambiguous because low success conflates perceptual insufficiency with reasoning difficulty. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28336:end -->

**为什么进入候选分母。** 摘要首要问题为“On-policy distillation provides dense supervision for multimodal reasoners, but its trajectory-level reward cannot determine whether a failed answer arose from perception or subsequent reasoning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce \textbf{Perception-Correction Distillation (PCD)}, a label-free method that identifies correctable perception failures using downstream failure and teacher--student disagreement as complementary witnesses.

**证据证明什么。** In matched 2B ablations, removing PCD and separated rollout reduces held-out average by 2.22 and 0.88 points, respectively.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28336v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28336v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.28336v1#S4 — 4 Experiments; https://arxiv.org/html/2607.28336v1#S4.SS1 — 4.1 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.28336v1#S4.SS5 — 4.5 Limitations and Threats to Validity; https://arxiv.org/html/2607.28336v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28336:end -->

<!-- review:SF-2026-ARXIV-2607-28367:start -->
### How Benchmarks Mis-Score Computer-Use Agents

<!-- claim:SF-2026-ARXIV-2607-28367:start -->Computer-use agents (CUA) are being deployed to browse the web and operate desktop software, yet their benchmark scores are still commonly produced by brittle scripted oracles. A score is the output of a pipeline in which tasks can be stale, trajectories can omit decisive visual evidence, evaluators can reject valid alternatives, and aggregate reports can hide the cause of failure. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28367:end -->

**为什么进入候选分母。** 摘要首要问题为“Computer-use agents (CUA) are being deployed to browse the web and operate desktop software, yet their benchmark scores are still commonly produced by brittle scripted oracles.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We organize these problems into a reliability framework spanning task construction, trajectory observation, scoring, and reporting.

**证据证明什么。** For genuine failures, a three-tier diagnostic taxonomy shows that verification/feedback and planning failures dominate execution/grounding errors, while a single scalar success rate can not explain.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28367v1#S2 — 2 Evaluation Reliability Framework; https://arxiv.org/html/2607.28367v1#S5 — 5 Designing Reliable Benchmarks。Evaluation：https://arxiv.org/html/2607.28367v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.28367v1#A3.SS3 — C.3 Dynamic Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.28367v1#A2 — Appendix B Failure-Taxonomy Details; https://arxiv.org/html/2607.28367v1#A3 — Appendix C Future-Direction Details。

**Artifact boundary。** Exact v1 links https://github.com/Zdong104/CADWORLD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28367:end -->

<!-- review:SF-2026-ARXIV-2607-28399:start -->
### Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees

<!-- claim:SF-2026-ARXIV-2607-28399:start -->Computer-use agents often fail on transient GUI events because they produce the correct action only after the relevant window has already closed. We identify the main cause as expensive autoregressive decoding on the decision-time critical path. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28399:end -->

**为什么进入候选分母。** 摘要首要问题为“Computer-use agents often fail on transient GUI events because they produce the correct action only after the relevant window has already closed.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose Adaptive Anticipatory Policy Trees (AAPT), which eliminates this delay without modifying the underlying model.

**证据证明什么。** Both open-loop and predict-and-replan baselines achieve zero success because they still decode during execution.

**证据没有证明什么。** The click_target scenario was not run as a paired comparison because both arms fail for independent reasons: the reactive arm is floored by the model’s coordinate grounding (0/18 even at relaxed windows; clicks miss a 90 px target by a 229 px median despite the model perceiving it), and the AAPT arm is blocked by construction – the target’s coordinates are revealed only at fire time, after the tree is compiled, and the observer returns a branch id, not coordinates. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28399v1#S16 — 16 Method details moved from the main text; https://arxiv.org/html/2607.28399v1#S11 — 11 Per-model serving provenance。Evaluation：https://arxiv.org/html/2607.28399v1#S18 — 18 Additional results detail; https://arxiv.org/html/2607.28399v1#S4 — 4 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.28399v1#S19 — 19 Full limitations register; https://arxiv.org/html/2607.28399v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Hcompany/Holo-3.1-35B-A3B, https://huggingface.co/inclusionAI/UI-Venus-1.5-30B-A3B, https://huggingface.co/meituan/EvoCUA-32B-20260105; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The click_target scenario was not run as a paired comparison because both arms fail for independent reasons: the reactive arm is floored by the model’s coordinate grounding (0/18 even at relaxed windows; clicks miss a 90 px target by a 229 px median despite the model perceiving it), and the AAPT arm is blocked by construction – the target’s coordinates are revealed only at fire time, after the tree is compiled, and the observer returns a branch id, not coordinates.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28399:end -->

<!-- review:SF-2026-ARXIV-2607-28415:start -->
### QQWorld: Quantile-Quantile Matching for World Model Regularization

<!-- claim:SF-2026-ARXIV-2607-28415:start -->Latent world models enable efficient planning by predicting future states in a compact representation space, but their performance depends critically on the quality of the learned latent distribution. LeWorldModel (LeWM) regularizes its latents toward an isotropic Gaussian using the Epps-Pulley (EP) objective. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28415:end -->

**为什么进入候选分母。** 摘要首要问题为“Latent world models enable efficient planning by predicting future states in a compact representation space, but their performance depends critically on the quality of the learned latent distribution.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this limitation, we propose QQWorld, which replaces EP with a quantile-quantile matching objective that directly aligns projected latent samples with rank-matched Gaussian quantiles, thereby maintaining effective corrective gradients in the tails.

**证据证明什么。** We show that the corrective gradients of EP rapidly vanish for isolated tail samples, leaving heavy-tailed deviations insufficiently controlled.

**证据没有证明什么。** We further propose cross-batch QQ to improve quantile estimation under limited GPU memory. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28415v1#S3 — 3 Method; https://arxiv.org/html/2607.28415v1#S2.SS1 — 2.1 Latent World Models for Planning。Evaluation：https://arxiv.org/html/2607.28415v1#S4 — 4 Experiments; https://arxiv.org/html/2607.28415v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.28415v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：We further propose cross-batch QQ to improve quantile estimation under limited GPU memory.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28415:end -->

<!-- review:SF-2026-ARXIV-2607-28418:start -->
### WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning

<!-- claim:SF-2026-ARXIV-2607-28418:start -->Pruning is a promising approach for improving the efficiency of LLMs. Existing static structured pruning methods are hardware-friendly and can deliver practical throughput gains, but their input-agnostic computation allocation often causes substantial accuracy degradation under aggressive sparsity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28418:end -->

**为什么进入候选分母。** 摘要首要问题为“Pruning is a promising approach for improving the efficiency of LLMs.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address these challenges, we present WIDE, the first end-to-end differentiable token-level dynamic width pruning framework designed for both prefill and decode scenarios.

**证据证明什么。** Through a two-stage training pipeline, WIDE learns effective token-wise sparse execution patterns and achieves substantially better quality retention than existing approaches.

**证据没有证明什么。** This abstraction lets the same routing decisions be consumed by customized attention and GEMM kernels with limited disruption to dense execution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28418v1#S3 — 3 WIDE: Preliminary, Training, and Inference Design; https://arxiv.org/html/2607.28418v1#A1 — Appendix A The Cost for Naive Gather-Scatter Implementations。Evaluation：https://arxiv.org/html/2607.28418v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.28418v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.28418v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/EIT-NLP/LLM-Pruning/tree/main/WIDE, https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：This abstraction lets the same routing decisions be consumed by customized attention and GEMM kernels with limited disruption to dense execution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28418:end -->

<!-- review:SF-2026-ARXIV-2607-28443:start -->
### One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA

<!-- claim:SF-2026-ARXIV-2607-28443:start -->Decentralized robots often need a common view of what their team is becoming, even though each robot sees different evidence and cannot rely on a central estimate or output-level consensus. We ask whether compatible collective-state predictions can emerge under this constraint. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28443:end -->

**为什么进入候选分母。** 摘要首要问题为“Decentralized robots often need a common view of what their team is becoming, even though each robot sees different evidence and cannot rely on a central estimate or output-level consensus.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We ask whether compatible collective-state predictions can emerge under this constraint.

**证据证明什么。** In a fresh independent replication, agreement improves for every seed and every evaluated split.

**证据没有证明什么。** Token roles are fixed; future graph adjacency is not encoded into this registered target. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28443v1#S1 — I Introduction; https://arxiv.org/html/2607.28443v1#S2 — II Related Work。Evaluation：https://arxiv.org/html/2607.28443v1#S5 — V Experimental Protocol; https://arxiv.org/html/2607.28443v1#S6 — VI Results。Limitations / counterevidence：https://arxiv.org/html/2607.28443v1#S7 — VII Discussion and Limitations; https://arxiv.org/html/2607.28443v1#S4.SS2 — IV-B One variable-size future target。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Token roles are fixed; future graph adjacency is not encoded into this registered target.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28443:end -->

<!-- review:SF-2026-ARXIV-2607-28495:start -->
### Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation

<!-- claim:SF-2026-ARXIV-2607-28495:start -->Stage-replay diagnostics reconstruct intermediate token prefixes and treat fresh-prefill continuation as continuation from the decoder state that originally reached the prefix. We audit that assumption at a whole reasoning-stage boundary in a Qwen2.5-derived system. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28495:end -->

**为什么进入候选分母。** 摘要首要问题为“Stage-replay diagnostics reconstruct intermediate token prefixes and treat fresh-prefill continuation as continuation from the decoder state that originally reached the prefix.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The paper holds integer prefix tokens fixed while crossing cache construction (retained live state versus fresh one-shot prefill) and numerical precision. Replica controls bound run noise, saved ledgers replay retained trajectories, and bidirectional transplantation of all 48 K/V layers tests whether the continuation follows tokens or the donated cache state.

**证据证明什么。** On the tested states, boundary K/V cache is a causally sufficient carrier of the divergent trajectory, while numerical precision moderates its behavioral expression.

**证据没有证明什么。** The experiment is bounded to the disclosed Qwen2.5-derived system, stage boundary and precision settings. It does not show that every BF16 prefill/live-cache difference changes task outcomes, nor that FP32 removes divergence for other architectures or longer trajectories.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28495v1#S3.SS1 — 3.1 Token, role, mask, and replay-boundary contract; https://arxiv.org/html/2607.28495v1#S3.SS2 — 3.2 Models and evaluation set。Evaluation：https://arxiv.org/html/2607.28495v1#S3.SS6 — 3.6 Experiment 4: bidirectional KV-cache transplantation; https://arxiv.org/html/2607.28495v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.28495v1#S6 — 6 Limitations and Threats to Validity; https://arxiv.org/html/2607.28495v1#S7 — 7 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 reports saved-ledger and cache-transplant controls but does not bind them to an immutable public experiment commit.

**Trade-off 与共存边界。** Retaining live cache preserves execution-state fidelity but costs memory and complicates replay portability; fresh prefill reconstructs from tokens cheaply but can create a numerically different state. Exact-token replay is therefore suitable only when state fidelity is not assumed or when replica, precision, role/mask/position and endpoint controls validate equivalence.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28495:end -->

<!-- review:SF-2026-ARXIV-2607-28545:start -->
### ORCA-bench: How Ready Are Language Model Agents for Oncall?

<!-- claim:SF-2026-ARXIV-2607-28545:start -->Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28545:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We release the public set at https://hub.harborframework.com/datasets/orca-bench/orca-bench.

**证据证明什么。** We release the public set at https://hub.harborframework.com/datasets/orca-bench/orca-bench.

**证据没有证明什么。** The product-catalog service fails the lookup at main.go#L448 and returns gRPC NOT_FOUND with message “Product Not Found: ” . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28545v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28545v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.28545v1#A11 — Appendix K Additional Experiments; https://arxiv.org/html/2607.28545v1#A7.SS1 — G.1 Evaluation Prompts。Limitations / counterevidence：https://arxiv.org/html/2607.28545v1#A2.SS1 — B.1 Example: Product Catalog Failure; https://arxiv.org/html/2607.28545v1#A2.SS2 — B.2 Example: Recommendation Cache Failure。

**Artifact boundary。** Exact v1 links https://github.com/open-telemetry/opentelemetry-demo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The product-catalog service fails the lookup at main.go#L448 and returns gRPC NOT_FOUND with message “Product Not Found: ” .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-MONITORING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28545:end -->

<!-- review:SF-2026-ARXIV-2607-28573:start -->
### Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs

<!-- claim:SF-2026-ARXIV-2607-28573:start -->Deploying autonomous computer-use agents (CUAs) locally is increasingly important for privacy, cost efficiency, and practical usability, yet improving their performance under strict hardware constraints remains challenging. While recent studies show that inference-time scaling can improve frontier computer-use agents through additional computation during execution, its effectiveness for resource-constrained local models remains poorly understood. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28573:end -->

**为什么进入候选分母。** 摘要首要问题为“Deploying autonomous computer-use agents (CUAs) locally is increasingly important for privacy, cost efficiency, and practical usability, yet improving their performance under strict hardware constraints remains challenging.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present a systematic empirical study of inference-time scaling in local CUAs across contextual, temporal, structural, and parallel dimensions.

**证据证明什么。** Our results show that additional computation often yields diminishing returns while changing failure modes.

**证据没有证明什么。** These findings suggest that future progress in local CUAs will depend less on increasing inference-time compute than on designing agents that allocate compute according to the capabilities and limitations of local models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28573v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.28573v1#S3.SS4 — 3.4 Experimental Setup; https://arxiv.org/html/2607.28573v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.28573v1#S5 — 5 Discussion; https://arxiv.org/html/2607.28573v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：These findings suggest that future progress in local CUAs will depend less on increasing inference-time compute than on designing agents that allocate compute according to the capabilities and limitations of local models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28573:end -->

<!-- review:SF-2026-ARXIV-2607-28576:start -->
### Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B

<!-- claim:SF-2026-ARXIV-2607-28576:start -->Methods that make a language model plan, criticise and rewrite its own answer, reflect on mistakes, pick the best of several attempts, or debate with copies of itself nearly all make it generate far more text than a single chain of thought. Because generating more text raises accuracy by itself, a gain over one chain of thought does not show the method's idea is what helped. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28576:end -->

**为什么进入候选分母。** 摘要首要问题为“Methods that make a language model plan, criticise and rewrite its own answer, reflect on mistakes, pick the best of several attempts, or debate with copies of itself nearly all make it generate far more text than a single chain of thought.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** No method is reliably better than repeated sampling at equal cost anywhere.

**证据证明什么。** Because generating more text raises accuracy by itself, a gain over one chain of thought does not show the method's idea is what helped.

**证据没有证明什么。** The damage was not the missing data but its pattern . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28576v1#S4.SS3 — 4.3 Methods compared; https://arxiv.org/html/2607.28576v1#S5.SS1 — 5.1 Does any method beat the sampling baseline at equal cost?。Evaluation：https://arxiv.org/html/2607.28576v1#A1.SS4 — A.4 A failure that would have biased the results; https://arxiv.org/html/2607.28576v1#S4 — 4 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.28576v1#A1.SS4 — A.4 A failure that would have biased the results; https://arxiv.org/html/2607.28576v1#S4.SS7 — 4.7 Threats to validity。

**Artifact boundary。** Exact v1 links https://github.com/ggml-org/llama.cpp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The damage was not the missing data but its pattern .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28576:end -->

<!-- review:SF-2026-ARXIV-2607-28591:start -->
### Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments

<!-- claim:SF-2026-ARXIV-2607-28591:start -->Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation. Each task must couple a realistic software state with a specification, development tools, and reliable verification. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28591:end -->

**为什么进入候选分母。** 摘要首要问题为“Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To expand this supply, we present Change2Task, a system grounded in repository history that converts merged pull requests into verified tasks on healthy modern revisions of the same repository.

**证据证明什么。** Historical and reconstructed cases achieve up to 98.0% matched outcome agreement under agent evaluation, while reuse of modern bases reduces measured expenditure across the complete pipeline by 10.8%.

**证据没有证明什么。** Lifecycle qualification depends on executable target and regression checks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28591v1#Sx3 — Methodology; https://arxiv.org/html/2607.28591v1#A9.SS2 — I.2 Bug Fix with a Modernized Implementation。Evaluation：https://arxiv.org/html/2607.28591v1#Sx4 — Experiments; https://arxiv.org/html/2607.28591v1#Sx4.SSx1 — Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.28591v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.28591v1#Sx5 — Conclusion and Outlook。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Lifecycle qualification depends on executable target and regression checks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28591:end -->

<!-- review:SF-2026-ARXIV-2607-28609:start -->
### OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models

<!-- claim:SF-2026-ARXIV-2607-28609:start -->Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28609:end -->

**为什么进入候选分母。** 摘要首要问题为“Computer-using agents (CUAs) are advancing rapidly across the digital world.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories.

**证据证明什么。** Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.

**证据没有证明什么。** Reasoning-and-planning errors : the agent perceives the environment correctly but cannot form a sound high-level plan; this covers wrong task decomposition, logical fallacies, missing domain knowledge of the target software, premature termination, and repetitive action loops. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28609v1#A3.SS1 — C.1. Evaluated Models; https://arxiv.org/html/2607.28609v1#S6 — 6. OS-Shepherd: An Open Reward Model。Evaluation：https://arxiv.org/html/2607.28609v1#A5 — Appendix E Additional Results and Analysis; https://arxiv.org/html/2607.28609v1#A3 — Appendix C Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.28609v1#A2.SS3 — B.3. Failure-Type Taxonomy; https://arxiv.org/html/2607.28609v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Reasoning-and-planning errors : the agent perceives the environment correctly but cannot form a sound high-level plan; this covers wrong task decomposition, logical fallacies, missing domain knowledge of the target software, premature termination, and repetitive action loops.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28609:end -->

<!-- review:SF-2026-ARXIV-2607-28617:start -->
### AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

<!-- claim:SF-2026-ARXIV-2607-28617:start -->System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications. They are used throughout commercial AI products, but are rarely disclosed to the public or regulators, creating a serious trust and accountability gap in the wide deployment of AI systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28617:end -->

**为什么进入候选分母。** 摘要首要问题为“System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we introduce Artificial Intelligence System Prompt Assurance (AISPA), a user-centric framework for systematically auditing system prompts in AI systems.

**证据证明什么。** Our findings highlight the need for greater transparency, standardization, and independent oversight for system prompts in commercial AI products.

**证据没有证明什么。** Because these prompts were not obtained through official channels, we cannot perfectly verify whether they represent the exact versions currently deployed in production. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28617v1#S2 — 2 What is a System Prompt and Why We Need System Prompt Auditing; https://arxiv.org/html/2607.28617v1#S3 — 3 AISPA : A Taxonomy for User-Centric System Prompt Auditing。Evaluation：https://arxiv.org/html/2607.28617v1#S5.SS2 — 5.2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.28617v1#S10 — 10 Limitations; https://arxiv.org/html/2607.28617v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/0xeb/TheBigPromptLibrary, https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools, https://github.com/asgeirtj/system_prompts_leaks; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Because these prompts were not obtained through official channels, we cannot perfectly verify whether they represent the exact versions currently deployed in production.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PROMPT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28617:end -->

<!-- review:SF-2026-ARXIV-2607-28624:start -->
### PhiZero: A World Model Built Around Physical Language

<!-- claim:SF-2026-ARXIV-2607-28624:start -->We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions. Existing physical world models typically predict future videos directly in pixel space, leaving the underlying world dynamics implicit within high-dimensional visual predictors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-28624:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions.

**证据证明什么。** We further show its potential for realistic and interactive world modeling, fine-grained action-conditioned simulation, and zero-shot motion transfer.

**证据没有证明什么。** We further discuss limitations and future works in the Appendix E . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.28624v1#S3 — 3 Method; https://arxiv.org/html/2607.28624v1#A3.SS1 — C.1 Controllable and Interactive World Model。Evaluation：https://arxiv.org/html/2607.28624v1#A2 — 附录 B Additional Evaluation Details; https://arxiv.org/html/2607.28624v1#A2.SS1 — B.1 Physical Video Generation Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.28624v1#A5 — 附录 E Limitations and Future Work; https://arxiv.org/html/2607.28624v1#S5 — 5 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：We further discuss limitations and future works in the Appendix E .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-28624:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27231 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27231 |
| SF-2026-ARXIV-2607-27250 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27250 |
| SF-2026-ARXIV-2607-27267 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27267 |
| SF-2026-ARXIV-2607-27269 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27269 |
| SF-2026-ARXIV-2607-27275 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27275 |
| SF-2026-ARXIV-2607-27283 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27283 |
| SF-2026-ARXIV-2607-27539 | score_7_9 | selected | DA-20260731-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260731-01 |
| SF-2026-ARXIV-2607-27636 | score_7_9 | selected | DA-20260731-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260731-02 |
| SF-2026-ARXIV-2607-28495 | score_7_9 | selected | DA-20260731-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260731-03 |
| SF-2026-ARXIV-2607-28576 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-28576 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-27231:start -->
`SF-2026-ARXIV-2607-27231` 的 exact-v1 Deep Review 已保留。其机制为：We present KernelGenBench, a unified benchmark for systematically evaluating LLM- and agent-generated Triton kernels across diverse operator sources and heterogeneous hardware platforms. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27231:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27250:start -->
`SF-2026-ARXIV-2607-27250` 的 exact-v1 Deep Review 已保留。其机制为：We present a controlled ablation of context-injection strategy across two frontier agents (Claude Code and Codex), 17 real tasks from 3 repositories (15 shared + 2 Codex-only), and 288 evaluated runs with gold-test evaluation. 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27250:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27267:start -->
`SF-2026-ARXIV-2607-27267` 的 exact-v1 Deep Review 已保留。其机制为：We present FAVA (Formal Authorization for Verified Agents), a permission-carrying authorization framework for agent execution. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27267:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27269:start -->
`SF-2026-ARXIV-2607-27269` 的 exact-v1 Deep Review 已保留。其机制为：We evaluate 192 model-converter-backend-method-task configurations spanning four Llama/Qwen draft-target pairs, TransMLA and MHA2MLA, HF and vLLM, and four 200-prompt tasks. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27269:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27275:start -->
`SF-2026-ARXIV-2607-27275` 的 exact-v1 Deep Review 已保留。其机制为：We test this claim for multi-turn, tool-calling agents, where it now matters most. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27275:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27283:start -->
`SF-2026-ARXIV-2607-27283` 的 exact-v1 Deep Review 已保留。其机制为：This observation is useful for deployment, but it does not by itself explain why failure occurs. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27283:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28576:start -->
`SF-2026-ARXIV-2607-28576` 的 exact-v1 Deep Review 已保留。其机制为：No method is reliably better than repeated sampling at equal cost anywhere. 为避免挤压 `AGENT-REFLECTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-28576:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260731-01:start -->
### Subtract, Transport, or Replay? Auditable Deletion from Language-Model Memory

**约束变化与机制。** The audit first tests whether a native KDA record leaves a stable, addressable receipt after later suffix computation; suffix-dependent recurrent contributions and later transition/write terms falsify that assumption. It then separates two valid deletion paths: checkpoint replay recomputes the declared native-state surface, while a support-vector memory retrofitted onto a frozen backbone stores each admitted record behind an independently refittable key boundary.

**证明与未证明。** The paper's two contributions are a negative result for native KDA's tested receipt classes and a positive training-free construction for addressable pretrained memory. 但 It does not show that arbitrary recurrent or parameter memories admit cheap exact deletion, nor that deletion retroactively changes outputs or artifacts already emitted. The positive construction is bounded to the disclosed frozen Gemma checkpoints and conditional retained-key refit protocol.

**Trade-off 与共存边界。** Addressability makes deletion auditable, but it moves cost into explicit per-record state, retained-key refits, checkpoint/replay storage and a precisely declared recovery surface. Native recurrent memory remains useful when exact record deletion is not a requirement; replay remains the conservative path when state cannot be separated safely. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-27539`。
<!-- analysis:DA-20260731-01:end -->

<!-- analysis:DA-20260731-02:start -->
### HALO: Heterogeneous Admission through Localized Obligations for Safe Agentic Execution

**约束变化与机制。** HALO assigns each heterogeneous response component a localized obligation set, admits a component only when its declared prerequisites remain supported, preserves unaffected components instead of rejecting the whole response, and rechecks the exact action immediately before dispatch. A blocked action cannot be revived from stale state; only a freshly generated candidate may replace it.

**证明与未证明。** Across ten cold-start PX4/Gazebo sessions, HALO blocked every tested stale route, observed no matching stale setpoint, and completed all fresh recoveries. 但 The results do not establish that natural-language prerequisite extraction is complete, that every tool boundary exposes enough state for revalidation, or that ten simulated PX4/Gazebo sessions generalize to arbitrary physical systems. Admission alone also cannot protect a queued action after its support changes; the dispatch recheck is essential.

**Trade-off 与共存边界。** Localized admission avoids discarding unrelated useful output, but introduces obligation declaration, dependency tracking and a second authorization point on the critical path. Whole-response rejection remains simpler when components are inseparable; independent checks remain valid only when no hidden dependency crosses components. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-27636`。
<!-- analysis:DA-20260731-02:end -->

<!-- analysis:DA-20260731-03:start -->
### Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation

**约束变化与机制。** The paper holds integer prefix tokens fixed while crossing cache construction (retained live state versus fresh one-shot prefill) and numerical precision. Replica controls bound run noise, saved ledgers replay retained trajectories, and bidirectional transplantation of all 48 K/V layers tests whether the continuation follows tokens or the donated cache state.

**证明与未证明。** On the tested states, boundary K/V cache is a causally sufficient carrier of the divergent trajectory, while numerical precision moderates its behavioral expression. 但 The experiment is bounded to the disclosed Qwen2.5-derived system, stage boundary and precision settings. It does not show that every BF16 prefill/live-cache difference changes task outcomes, nor that FP32 removes divergence for other architectures or longer trajectories.

**Trade-off 与共存边界。** Retaining live cache preserves execution-state fidelity but costs memory and complicates replay portability; fresh prefill reconstructs from tokens cheaply but can create a numerically different state. Exact-token replay is therefore suitable only when state fidelity is not assumed or when replica, precision, role/mask/position and endpoint controls validate equivalence. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-28495`。
<!-- analysis:DA-20260731-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260731-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260731 | GAP-20260731-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260731-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260731-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260731-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260731-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260731-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260731-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

515 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：20
- `incremental_method_without_durable_system_delta`：419
- `local_benchmark_without_release_delta`：15
- `theory_without_ai_system_contract`：3
- `vertical_application_without_system_delta`：58

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 10、No Change 74、Structural 0；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/31/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Multi-Head Attention Residuals](https://arxiv.org/html/2607.27230v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [KernelGenBench: A Multi-Source and Multi-Chip Benchmark for LLM-based Kernel Generation](https://arxiv.org/html/2607.27231v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Asymmetric Collapse in Model Merging: When Refusal Over- writes Recognition](https://arxiv.org/html/2607.27240v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Divergence Decoding: Training-Free Capability Fusion](https://arxiv.org/html/2607.27248v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories](https://arxiv.org/html/2607.27250v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [It's Not Just More Demos: Counterfactual Action Sensitivity Coverage for Data-Efficient Robust Robot Imitation](https://arxiv.org/html/2607.27261v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs](https://arxiv.org/html/2607.27267v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Beyond KV Reconstruction: Functional Reconstruction for MLA Draft Models in Speculative Decoding](https://arxiv.org/html/2607.27269v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [BMOA: Baseline-Mechanism-Outcome Attribution for Compiler-Induced Numerical Deviations](https://arxiv.org/html/2607.27270v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [RLPF: Reinforcement Learning from Performance Feedback for Code Generation](https://arxiv.org/html/2607.27271v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [SDO: Structure-Aware Data Organization for Efficient LLM Post-Training](https://arxiv.org/html/2607.27273v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents](https://arxiv.org/html/2607.27275v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [The Kinetics of Training: A Driven-Nucleation Rate Law for Emergence, Plasticity Loss, and Circuit Control in Language Models](https://arxiv.org/html/2607.27281v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Benchmarking the Residual: What Long-Horizon Evaluations Add Beyond Matched Short-Task Performance](https://arxiv.org/html/2607.27283v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Open Security Benchmark: Towards Autonomous Enterprise Cyber Defense](https://arxiv.org/html/2607.27288v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [AgentS4D: Benchmarking Runtime Risks across the Execution Lifecycle of LLM-Based Workspace Agents](https://arxiv.org/html/2607.27294v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [SIGIL: Compiling Agent Skills into Typed Harnesses](https://arxiv.org/html/2607.27309v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation](https://arxiv.org/html/2607.27353v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis](https://arxiv.org/html/2607.27360v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation](https://arxiv.org/html/2607.27372v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [The Convergence Behavior of Adam under Heavy-Tailed Noise](https://arxiv.org/html/2607.27383v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Beyond the Bidirectional Promise: Re-evaluating the Robustness of Diffusion Language Models](https://arxiv.org/html/2607.27386v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [SWE-NFI: Studying and Benchmarking Coding Agents for Non-Functional Improvements](https://arxiv.org/pdf/2607.27409v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs](https://arxiv.org/html/2607.27415v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems](https://arxiv.org/html/2607.27443v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Granite: A Modular Methodology for Foundational Verification of Hardware-Software Leakage Contracts](https://arxiv.org/html/2607.27480v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Skill Use or Skill Theater? Evaluating the Reasoning Backroom in Skill-Augmented Language Agents](https://arxiv.org/html/2607.27484v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling](https://arxiv.org/html/2607.27511v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks](https://arxiv.org/html/2607.27518v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Latent-Kernel Discrete Flow Maps for Few-Step Generation](https://arxiv.org/html/2607.27529v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Subtract, Transport, or Replay? Auditable Deletion from Language-Model Memory](https://arxiv.org/html/2607.27539v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Cross-Embodiment Transfer via Behavior-Aligned Representations](https://arxiv.org/html/2607.27549v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Training Skills Like Parameters via Self-Supervised Semantic Diffusion](https://arxiv.org/html/2607.27557v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Inference-Time Agentic Decision Rules Beat Longer Evolving Search for Multi-Image Medical Reasoning](https://arxiv.org/html/2607.27564v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models](https://arxiv.org/html/2607.27599v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Back from the Future: Key-Value Cache Management by Counter-Causal Surprise](https://arxiv.org/html/2607.27600v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures](https://arxiv.org/html/2607.27617v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [HALO: Heterogeneous Admission through Localized Obligations for Safe Agentic Execution](https://arxiv.org/html/2607.27636v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Not as Sweet by Another Name: An Empirical Study of Format Robustness in LLM Document Workflows](https://arxiv.org/html/2607.27648v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Harness-G: A Graph-Structured Harness for Search Agents](https://arxiv.org/html/2607.27652v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness](https://arxiv.org/html/2607.27677v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch](https://arxiv.org/html/2607.27687v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents](https://arxiv.org/html/2607.27690v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference](https://arxiv.org/html/2607.27694v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [LightRot: A Light-Weighted Rotation Scheme and Architecture for Accurate Low-Bit Large Language Model Inference](https://arxiv.org/html/2607.27704v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding](https://arxiv.org/html/2607.27735v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory](https://arxiv.org/html/2607.27773v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy](https://arxiv.org/html/2607.27782v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Hallucinations Leave a Grounding Signature:Verifier-Guided Decoding for Selective Object Correction](https://arxiv.org/html/2607.27823v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Thinking Once Is Enough: Intermediate-Layer Evidence Routing for High-Resolution VQA](https://arxiv.org/html/2607.27830v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory](https://arxiv.org/html/2607.27834v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference](https://arxiv.org/html/2607.27842v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Search as Computation Allocation](https://arxiv.org/html/2607.27871v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding](https://arxiv.org/html/2607.27877v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models](https://arxiv.org/html/2607.27910v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [IFHierBench: Hierarchical Instruction Following for Large Language Models](https://arxiv.org/html/2607.27912v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Harnessing the Potential of Optimizing Data Mixtures via Bayesian Domain Reweighting](https://arxiv.org/html/2607.27928v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [The Geometry of Flow-Matching Uncertainty: A Cost-free Uncertainty Proxy and Its Application in Flow-based VLA Failure Detection](https://arxiv.org/html/2607.27933v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs](https://arxiv.org/html/2607.27951v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation](https://arxiv.org/html/2607.27967v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [VISA: A Structured Description Protocol for Agent-Based Simulation Models Towards Machine Reproducibility](https://arxiv.org/html/2607.28027v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents](https://arxiv.org/html/2607.28037v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [SemPIC: Learning Semantic Position-Independent KV Caches](https://arxiv.org/html/2607.28069v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck](https://arxiv.org/html/2607.28103v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer](https://arxiv.org/html/2607.28150v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents](https://arxiv.org/html/2607.28165v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Queue-Theoretic Admission Control for Multi-Tenant GPU Clusters](https://arxiv.org/html/2607.28223v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification](https://arxiv.org/html/2607.28225v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [(Towards) Scalable Reliable Automated Evaluation with Large Language Models](https://arxiv.org/html/2607.28282v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence](https://arxiv.org/html/2607.28317v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Correcting What You Cannot See: Credit Assignment for Perception Distillation in Multimodal Reasoners](https://arxiv.org/html/2607.28336v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [How Benchmarks Mis-Score Computer-Use Agents](https://arxiv.org/html/2607.28367v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees](https://arxiv.org/html/2607.28399v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [QQWorld: Quantile-Quantile Matching for World Model Regularization](https://arxiv.org/html/2607.28415v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning](https://arxiv.org/html/2607.28418v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA](https://arxiv.org/html/2607.28443v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation](https://arxiv.org/html/2607.28495v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [ORCA-bench: How Ready Are Language Model Agents for Oncall?](https://arxiv.org/html/2607.28545v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs](https://arxiv.org/html/2607.28573v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B](https://arxiv.org/html/2607.28576v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments](https://arxiv.org/html/2607.28591v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models](https://arxiv.org/html/2607.28609v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [AISPA: User-Centric System Prompt Auditing for Large Language Model Applications](https://arxiv.org/html/2607.28617v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04
- [PhiZero: A World Model Built Around Physical Language](https://arxiv.org/html/2607.28624v1) — first-public（Asia/Shanghai）：2026-07-31；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、84/84 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
